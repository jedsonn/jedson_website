"""Enrich papers with author institutions and profile links from OpenAlex.

Author names, OpenAlex profile URLs, and institutions are open bibliographic
metadata (not abstracts), so the output data/authors.json is committed and
served. Runs where there is network (GitHub Actions), batched by DOI to stay
inside OpenAlex's polite rate limits.

Output: data/authors.json = { uid: {authors: [{name, url, inst}], affiliations: [...]} }
"""
import argparse
import json
import os
import time

from common import CFG, ROOT, guarded_get, read_jsonl, write_json

OPENALEX = "https://api.openalex.org/works"


def lookup_doi(rec):
    """The DOI OpenAlex indexes this record under (arXiv papers use a 10.48550 DOI)."""
    if rec.get("doi"):
        return rec["doi"].lower()
    aid = rec.get("arxiv_id")
    if aid:
        return ("10.48550/arxiv." + aid.split("v")[0]).lower()
    return None


def author_entry(a):
    au = a.get("author") or {}
    name = au.get("display_name") or ""
    url = au.get("id") or ""  # https://openalex.org/A...
    inst = ""
    insts = a.get("institutions") or []
    if insts and insts[0].get("display_name"):
        inst = insts[0]["display_name"]
    elif a.get("raw_affiliation_strings"):
        inst = a["raw_affiliation_strings"][0]
    return {"name": name, "url": url, "inst": inst}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int, default=40)
    args = ap.parse_args()

    index = read_jsonl(os.path.join(ROOT, "data", "index.jsonl"))
    out_path = os.path.join(ROOT, "data", "authors.json")
    existing = {}
    if os.path.exists(out_path):
        existing = json.load(open(out_path, encoding="utf-8"))

    # only enrich records we don't already have
    todo = [r for r in index if r.get("uid") not in existing or not existing.get(r["uid"], {}).get("authors")]
    by_doi = {}
    for r in todo:
        d = lookup_doi(r)
        if d:
            by_doi.setdefault(d, r["uid"])
    dois = list(by_doi.keys())
    print("Enriching %d of %d records via OpenAlex (%d resolvable DOIs)." % (len(todo), len(index), len(dois)))

    mailto = CFG["run"]["polite_mailto"]
    got = 0
    for i in range(0, len(dois), args.batch):
        chunk = dois[i:i + args.batch]
        flt = "doi:" + "|".join(chunk)
        try:
            resp = guarded_get(OPENALEX, params={
                "filter": flt, "per-page": args.batch,
                "select": "doi,authorships", "mailto": mailto,
            })
            works = resp.json().get("results", [])
        except Exception as exc:  # noqa: BLE001
            print("  batch %d failed: %s" % (i // args.batch, str(exc)[:120]))
            time.sleep(1)
            continue
        for w in works:
            wdoi = (w.get("doi") or "").replace("https://doi.org/", "").lower()
            uid = by_doi.get(wdoi)
            if not uid:
                continue
            authors = [author_entry(a) for a in (w.get("authorships") or [])]
            affs = []
            for a in authors:
                if a["inst"] and a["inst"] not in affs:
                    affs.append(a["inst"])
            existing[uid] = {"authors": authors, "affiliations": affs[:8]}
            if authors:
                got += 1
        time.sleep(0.3)

    write_json(out_path, existing)
    print("Wrote %d author records to data/authors.json (%d newly enriched)." % (len(existing), got))


if __name__ == "__main__":
    main()
