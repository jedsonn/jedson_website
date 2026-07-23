"""Stage 4. Deduplicate against the persistent index.

Four tiers, cheapest first:
  1. DOI exact
  2. arXiv id exact
  3. normalized title exact
  4. fuzzy title at or above config threshold, same first author surname

A paper posted to both arXiv and SSRN is one entry with both links, not two.

The index at data/index.jsonl is append-only and is committed. It is the
memory of the whole project. Never rewrite it by hand.

Usage:
  python3 scripts/dedupe.py --edition 12
"""

import argparse
import os
from datetime import datetime, timezone

from common import CFG, ROOT, append_jsonl, log, norm_title, read_json, read_jsonl, write_json

try:
    from rapidfuzz import fuzz
    HAVE_FUZZ = True
except ImportError:
    HAVE_FUZZ = False


def surname(rec):
    if not rec.get("authors"):
        return ""
    return rec["authors"][0].split()[-1].lower()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--edition", type=int, required=True)
    ap.add_argument("--date", default=None,
                    help="Run date (YYYY-MM-DD) stamped as 'added' on new records. Defaults to today (UTC).")
    args = ap.parse_args()
    added_date = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")

    run_dir = os.path.join(ROOT, "data", "runs", "edition-%03d" % args.edition)
    incoming = read_json(os.path.join(run_dir, "classified.json"), [])
    if not incoming:
        raise SystemExit("No classified.json for edition %d" % args.edition)

    index_path = os.path.join(ROOT, "data", "index.jsonl")
    index = read_jsonl(index_path)

    by_doi = {r["doi"]: r for r in index if r.get("doi")}
    by_arxiv = {r["arxiv_id"]: r for r in index if r.get("arxiv_id")}
    by_title = {norm_title(r["title"]): r for r in index if r.get("title")}
    thresh = CFG["dedupe"]["fuzzy_threshold"]
    require_author = CFG["dedupe"]["require_same_first_author"]

    fresh, merged, dupes = [], 0, 0
    seen_this_run = {}

    for rec in incoming:
        nt = norm_title(rec.get("title", ""))
        hit = None
        if rec.get("doi") and rec["doi"] in by_doi:
            hit = by_doi[rec["doi"]]
        elif rec.get("arxiv_id") and rec["arxiv_id"] in by_arxiv:
            hit = by_arxiv[rec["arxiv_id"]]
        elif nt and nt in by_title:
            hit = by_title[nt]
        elif nt and HAVE_FUZZ:
            for cand_title, cand in by_title.items():
                if abs(len(cand_title) - len(nt)) > 40:
                    continue
                if fuzz.token_set_ratio(nt, cand_title) >= thresh:
                    if not require_author or surname(cand) == surname(rec):
                        hit = cand
                        break

        if hit is not None:
            dupes += 1
            continue

        prior = seen_this_run.get(nt)
        if prior is not None:
            for k in ("doi", "arxiv_id"):
                if rec.get(k) and not prior.get(k):
                    prior[k] = rec[k]
            labels = set(filter(None, [prior.get("source_label"), rec.get("source_label")]))
            prior["source_label"] = " and ".join(sorted(labels))
            if rec.get("url") and rec["url"] != prior.get("url"):
                prior.setdefault("alt_urls", []).append(rec["url"])
            merged += 1
            continue

        rec["edition"] = args.edition
        rec["added"] = added_date
        seen_this_run[nt] = rec
        fresh.append(rec)

    # The index is committed to git. Abstracts belong to their authors and
    # publishers, and we only ever needed them as classifier input. Drop them
    # here so they never enter version control. The gitignored .cache keeps a
    # copy for reruns.
    for rec in fresh:
        rec.pop("abstract", None)
        rec.pop("abstract_source", None)

    log("Incoming %d. New %d. Cross-source merges %d. Already in index %d."
        % (len(incoming), len(fresh), merged, dupes))
    if not HAVE_FUZZ:
        log("NOTE: rapidfuzz not installed, tier 4 fuzzy matching was skipped.")

    write_json(os.path.join(run_dir, "final.json"), fresh)
    append_jsonl(index_path, fresh)
    log("Appended %d records to data/index.jsonl (now %d total)." % (len(fresh), len(index) + len(fresh)))


if __name__ == "__main__":
    main()
