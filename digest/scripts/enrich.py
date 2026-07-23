"""Stage 2. Fill missing abstracts so the classifier has something to read.

Crossref abstract coverage for SSRN deposits is patchy, so records arrive with
titles but no abstract. We try OpenAlex, then Semantic Scholar, both by DOI.

Abstracts are cached under .cache/ which is gitignored. They are classifier
input only. They are never rendered on the site and never committed. What gets
published is our own three bullets, plus title, authors, and a link.

Never store or publish the Semantic Scholar tldr field. That is their generated
content.

Usage:
  python3 scripts/enrich.py --edition 12
"""

import argparse
import hashlib
import os
import time

from common import (
    CFG, ROOT, detect_models, guarded_get, log, read_json, score_relevance,
    strip_tags, write_json,
)

OPENALEX_DOI = "https://api.openalex.org/works/doi:"
S2 = "https://api.semanticscholar.org/graph/v1/paper/DOI:"
CACHE = os.path.join(ROOT, CFG["enrichment"]["cache_dir"])


def cache_path(doi):
    return os.path.join(CACHE, hashlib.sha1(doi.encode()).hexdigest() + ".txt")


def cached(doi):
    p = cache_path(doi)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as fh:
            return fh.read()
    return None


def put_cache(doi, text):
    os.makedirs(CACHE, exist_ok=True)
    with open(cache_path(doi), "w", encoding="utf-8") as fh:
        fh.write(text or "")


def invert(inv):
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[k] for k in sorted(pos))[:6000]


def from_openalex(doi):
    try:
        resp = guarded_get(OPENALEX_DOI + doi, params={"mailto": CFG["run"]["polite_mailto"]})
        return invert(resp.json().get("abstract_inverted_index")), "openalex"
    except Exception:  # noqa: BLE001
        return "", ""


def openalex_citations(doi):
    """Open citation count from OpenAlex. Honest, open impact signal — shown
    only when > 0, so brand-new papers (nearly all of ours) display nothing
    rather than a misleading zero. SSRN download counts are proprietary and
    off-limits (no scraping), so citations are the open substitute."""
    if not doi:
        return None
    try:
        resp = guarded_get(OPENALEX_DOI + doi, params={"mailto": CFG["run"]["polite_mailto"]})
        n = resp.json().get("cited_by_count")
        return int(n) if isinstance(n, int) else None
    except Exception:  # noqa: BLE001
        return None


def from_s2(doi):
    if not CFG["enrichment"].get("semanticscholar_enabled"):
        return "", ""
    headers = {}
    key = os.environ.get("S2_API_KEY")
    if key:
        headers["x-api-key"] = key
    try:
        resp = guarded_get(S2 + doi, params={"fields": "abstract"}, headers=headers)
        return strip_tags(resp.json().get("abstract") or ""), "semanticscholar"
    except Exception:  # noqa: BLE001
        return "", ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--edition", type=int, required=True)
    args = ap.parse_args()

    run_dir = os.path.join(ROOT, "data", "runs", "edition-%03d" % args.edition)
    recs = read_json(os.path.join(run_dir, "harvested.json"), [])
    if not recs:
        raise SystemExit("No harvested.json for edition %d" % args.edition)

    filled, already, missing = 0, 0, 0
    for rec in recs:
        if rec.get("abstract"):
            already += 1
        elif rec.get("doi"):
            hit = cached(rec["doi"])
            if hit is not None:
                rec["abstract"], rec["abstract_source"] = hit, "cache"
            else:
                for fn in (from_openalex, from_s2):
                    text, src = fn(rec["doi"])
                    if text:
                        rec["abstract"], rec["abstract_source"] = text, src
                        break
                    time.sleep(0.6)
                put_cache(rec["doi"], rec.get("abstract", ""))
            if rec.get("abstract"):
                filled += 1
            else:
                missing += 1
        else:
            missing += 1

        score, hits = score_relevance(rec)
        rec["relevance"], rec["matched_terms"] = score, hits
        rec["models"] = detect_models((rec.get("title") or "") + " " + (rec.get("abstract") or ""))
        fams = set(rec["models"])
        if fams:
            rec["open_weights"] = bool(fams & set(CFG.get("open_weight_families", [])))

    kept = [r for r in recs if r["relevance"] >= CFG["run"]["min_relevance"]]
    kept.sort(key=lambda r: (-r["relevance"], r.get("posted", "")))
    cap = CFG["run"]["max_papers_per_edition"]
    if len(kept) > cap:
        log("Capping %d records to %d by relevance." % (len(kept), cap))
        kept = kept[:cap]

    # Citation counts are OPT-IN. Keyless OpenAlex rate-limits rapid per-paper
    # calls, and the retry backoff can stall a large edition for over an hour.
    # For fresh papers citations are ~0 anyway, so default off; enable with
    # enrichment.citations_enabled: true only for small runs.
    cited = 0
    if CFG.get("enrichment", {}).get("citations_enabled"):
        for rec in kept:
            if rec.get("doi"):
                n = openalex_citations(rec["doi"])
                if n is not None:
                    rec["citations"] = n
                    if n > 0:
                        cited += 1
                time.sleep(0.2)

    log("Abstracts: %d already, %d fetched, %d unavailable. Carrying %d records. %d with citations."
        % (already, filled, missing, len(kept), cited))
    write_json(os.path.join(run_dir, "enriched.json"), kept)


if __name__ == "__main__":
    main()
