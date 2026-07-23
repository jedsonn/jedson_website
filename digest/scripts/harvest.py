"""Stage 1. Harvest candidate records from open metadata APIs.

No scraping. Every source here is a documented public API:
  Crossref  https://api.crossref.org        (SSRN, NBER, and any DOI prefix)
  arXiv     https://export.arxiv.org/api    (Atom, metadata is CC0)
  OpenAlex  https://api.openalex.org        (CC0)

Usage:
  python3 scripts/harvest.py --edition 12 --date 2026-07-23
  python3 scripts/harvest.py --edition 12 --date 2026-07-23 --days 7 --limit 5
"""

import argparse
import os
import time
import xml.etree.ElementTree as ET

from common import (
    CFG, ROOT, blank_record, guarded_get, log, make_uid, norm_title,
    score_relevance, strip_tags, window, write_json,
)

CROSSREF = "https://api.crossref.org/works"
ARXIV = "https://export.arxiv.org/api/query"
OPENALEX = "https://api.openalex.org/works"
ATOM = "{http://www.w3.org/2005/Atom}"


def cr_date(parts):
    if not parts:
        return ""
    dp = parts.get("date-parts", [[]])
    if not dp or not dp[0]:
        return ""
    bits = dp[0] + [1, 1]
    return "%04d-%02d-%02d" % (bits[0], bits[1], bits[2])


def harvest_crossref(src, start, end):
    """Fetch every DOI under a prefix indexed in the window, then filter locally.

    Local keyword filtering beats Crossref's fuzzy query parameter. A prefix
    plus a few days is only a few thousand records, which is three or four
    pages at 1000 rows.
    """
    rows, cursor, seen = [], "*", 0
    while True:
        params = {
            "filter": "prefix:%s,from-index-date:%s,until-index-date:%s" % (src["prefix"], start, end),
            "rows": 1000,
            "cursor": cursor,
            "mailto": CFG["run"]["polite_mailto"],
            "select": "DOI,title,author,abstract,posted,created,issued,URL,type,subject",
        }
        resp = guarded_get(CROSSREF, params=params)
        msg = resp.json().get("message", {})
        items = msg.get("items", [])
        if not items:
            break
        for it in items:
            seen += 1
            rec = blank_record()
            rec["doi"] = (it.get("DOI") or "").lower()
            rec["title"] = strip_tags((it.get("title") or [""])[0])
            rec["abstract"] = strip_tags(it.get("abstract") or "")
            rec["abstract_source"] = "crossref" if rec["abstract"] else ""
            rec["posted"] = cr_date(it.get("posted")) or cr_date(it.get("created")) or cr_date(it.get("issued"))
            for a in it.get("author", []) or []:
                nm = " ".join(x for x in [a.get("given"), a.get("family")] if x).strip()
                if nm:
                    rec["authors"].append(nm)
                for aff in a.get("affiliation", []) or []:
                    if aff.get("name"):
                        rec["affiliations"].append(aff["name"])
            rec["affiliations"] = sorted(set(rec["affiliations"]))[:6]
            rec["source_label"] = src["label"]
            rec["source_id"] = src["id"]
            rec["url"] = "https://doi.org/" + rec["doi"] if rec["doi"] else (it.get("URL") or "")
            rec["uid"] = make_uid(rec)
            if rec["title"]:
                rows.append(rec)
        cursor = msg.get("next-cursor")
        if not cursor or len(items) < 1000:
            break
        time.sleep(1)
    log("  crossref %s: %d records scanned" % (src["prefix"], seen))
    return rows


def harvest_arxiv(src, start, end):
    rows, offset = [], 0
    while offset < 600:
        params = {
            "search_query": src["query"],
            "start": offset,
            "max_results": 200,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        resp = guarded_get(ARXIV, params=params, headers={"Accept": "application/atom+xml"})
        root = ET.fromstring(resp.content)
        entries = root.findall(ATOM + "entry")
        if not entries:
            break
        stop = False
        for e in entries:
            published = (e.findtext(ATOM + "published") or "")[:10]
            if published and published < start:
                stop = True
                continue
            if published and published > end:
                continue
            rec = blank_record()
            raw_id = e.findtext(ATOM + "id") or ""
            rec["arxiv_id"] = raw_id.rsplit("/", 1)[-1]
            rec["title"] = strip_tags(e.findtext(ATOM + "title") or "")
            rec["abstract"] = strip_tags(e.findtext(ATOM + "summary") or "")
            rec["abstract_source"] = "arxiv" if rec["abstract"] else ""
            rec["posted"] = published
            for a in e.findall(ATOM + "author"):
                nm = a.findtext(ATOM + "name")
                if nm:
                    rec["authors"].append(nm.strip())
            doi_el = e.find("{http://arxiv.org/schemas/atom}doi")
            if doi_el is not None and doi_el.text:
                rec["doi"] = doi_el.text.lower()
            rec["source_label"] = src["label"]
            rec["source_id"] = src["id"]
            rec["url"] = "https://arxiv.org/abs/" + rec["arxiv_id"]
            rec["uid"] = make_uid(rec)
            if rec["title"]:
                rows.append(rec)
        if stop:
            break
        offset += 200
        time.sleep(3)
    log("  arxiv %s: %d in window" % (src["id"], len(rows)))
    return rows


def openalex_abstract(inv):
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[k] for k in sorted(pos))[:6000]


def harvest_openalex(src, start, end):
    rows, cursor = [], "*"
    terms = "large language model|LLM|ChatGPT|generative AI|foundation model"
    while True:
        params = {
            "filter": "from_created_date:%s,to_created_date:%s,title_and_abstract.search:%s" % (start, end, terms),
            "per-page": 200,
            "cursor": cursor,
            "mailto": CFG["run"]["polite_mailto"],
        }
        resp = guarded_get(OPENALEX, params=params)
        body = resp.json()
        items = body.get("results", [])
        if not items:
            break
        for it in items:
            rec = blank_record()
            rec["doi"] = (it.get("doi") or "").replace("https://doi.org/", "").lower()
            rec["title"] = strip_tags(it.get("title") or "")
            rec["abstract"] = openalex_abstract(it.get("abstract_inverted_index"))
            rec["abstract_source"] = "openalex" if rec["abstract"] else ""
            rec["posted"] = it.get("publication_date") or ""
            for a in it.get("authorships", []) or []:
                nm = (a.get("author") or {}).get("display_name")
                if nm:
                    rec["authors"].append(nm)
                for inst in a.get("institutions", []) or []:
                    if inst.get("display_name"):
                        rec["affiliations"].append(inst["display_name"])
            rec["affiliations"] = sorted(set(rec["affiliations"]))[:6]
            host = ((it.get("primary_location") or {}).get("source") or {}).get("display_name") or "OpenAlex"
            rec["source_label"] = host[:40]
            rec["source_id"] = src["id"]
            rec["url"] = "https://doi.org/" + rec["doi"] if rec["doi"] else (it.get("id") or "")
            rec["uid"] = make_uid(rec)
            if rec["title"]:
                rows.append(rec)
        cursor = (body.get("meta") or {}).get("next_cursor")
        if not cursor:
            break
        time.sleep(1)
    log("  openalex: %d records" % len(rows))
    return rows


HANDLERS = {"crossref_prefix": harvest_crossref, "arxiv": harvest_arxiv, "openalex": harvest_openalex}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--edition", type=int, required=True)
    ap.add_argument("--date", required=True)
    ap.add_argument("--days", type=int, default=None)
    ap.add_argument("--limit", type=int, default=0, help="cap sources, for smoke tests")
    args = ap.parse_args()

    start, end = window(args.days)
    log("Harvest window %s to %s" % (start, end))

    enabled = [s for s in CFG["sources"] if s.get("enabled")]
    if args.limit:
        enabled = enabled[: args.limit]

    all_rows, coverage = [], []
    for src in enabled:
        log("Source: %s" % src["name"])
        try:
            rows = HANDLERS[src["kind"]](src, start, end)
            coverage.append({"id": src["id"], "name": src["name"], "status": "ok", "raw": len(rows)})
            all_rows.extend(rows)
        except Exception as exc:  # noqa: BLE001
            log("  FAILED: %s" % exc)
            coverage.append({"id": src["id"], "name": src["name"], "status": "failed", "raw": 0, "error": str(exc)[:300]})

    kept = []
    for rec in all_rows:
        score, hits = score_relevance(rec)
        rec["relevance"] = score
        rec["matched_terms"] = hits
        if score >= CFG["run"]["min_relevance"]:
            kept.append(rec)

    by_uid = {}
    for rec in kept:
        cur = by_uid.get(rec["uid"])
        if cur is None or len(rec.get("abstract") or "") > len(cur.get("abstract") or ""):
            by_uid[rec["uid"]] = rec
    kept = sorted(by_uid.values(), key=lambda r: (-r["relevance"], r.get("posted", "")), reverse=False)

    ok = sum(1 for c in coverage if c["status"] == "ok")
    log("Sources ok %d of %d. Raw %d. Passed gate %d. Unique %d."
        % (ok, len(coverage), len(all_rows), len(kept), len(by_uid)))
    if ok == 0:
        raise SystemExit("Every source failed. Check network before continuing.")

    out = os.path.join(ROOT, "data", "runs", "edition-%03d" % args.edition)
    write_json(os.path.join(out, "harvested.json"), kept)
    write_json(os.path.join(out, "coverage.json"),
               {"edition": args.edition, "date": args.date, "window": [start, end], "sources": coverage,
                "raw": len(all_rows), "kept": len(kept)})
    log("Wrote %s/harvested.json" % out)


if __name__ == "__main__":
    main()
