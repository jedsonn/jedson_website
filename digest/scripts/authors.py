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
import re
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


def profile_inst(au):
    """Best institution from an OpenAlex author profile: the last-known one, then
    the most recent historical affiliation if last-known is empty."""
    insts = au.get("last_known_institutions") or []
    if insts and insts[0].get("display_name"):
        return insts[0]["display_name"]
    for aff in (au.get("affiliations") or []):
        name = (aff.get("institution") or {}).get("display_name")
        if name:
            return name
    return ""


def norm_name(s):
    return re.sub(r"[^a-z]", "", (s or "").lower())


def resolve_by_name(existing, mailto):
    """Authors still missing an institution are usually SSRN-deposited entities
    whose OpenAlex profile carries no affiliation. Search OpenAlex by display
    name and accept a canonical profile ONLY on an exact normalized-name match
    for an established author (>= 8 works), so we never misattribute a school to
    the wrong same-named person. Returns {normalized_name: institution}."""
    want = {}
    for rec in existing.values():
        for a in rec.get("authors", []):
            if not a.get("inst") and a.get("name"):
                nk = norm_name(a["name"])
                if len(nk) >= 8:  # skip initials-only / too-short names
                    want.setdefault(nk, a["name"])
    print("Name-resolving %d unique authors still missing an institution." % len(want))
    out = {}
    for i, (nk, name) in enumerate(want.items()):
        try:
            resp = guarded_get("https://api.openalex.org/authors", params={
                "search": name, "per-page": 5, "mailto": mailto,
                "select": "id,display_name,works_count,last_known_institutions,affiliations",
            })
            for au in resp.json().get("results", []):
                if norm_name(au.get("display_name")) != nk:
                    continue
                if (au.get("works_count") or 0) < 8:
                    continue
                inst = profile_inst(au)
                if inst:
                    out[nk] = inst
                break
        except Exception as exc:  # noqa: BLE001
            if i % 100 == 0:
                print("  name-resolve error near %d: %s" % (i, str(exc)[:80]))
        time.sleep(0.15)
    print("Name-resolved institutions for %d authors." % len(out))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int, default=40)
    ap.add_argument("--resolve-names", action="store_true",
                    help="Also resolve still-missing institutions by author-name "
                         "search. Best-effort and slower (one OpenAlex query per "
                         "unresolved author); off by default because same-named "
                         "researchers can be misattributed.")
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

    # Second pass: query every unique author's OpenAlex profile for their
    # last-known institution (backfills preprints that tagged no affiliation)
    # AND their h-index (flags "top researcher" papers so the technical filter
    # never hides them).
    H_TOP = 40  # h-index at/above which an author counts as a top researcher
    meta = {}  # aid -> {"inst": str, "h": int}
    for uid, rec in existing.items():
        for a in rec.get("authors", []):
            if a.get("url"):
                aid = a["url"].rstrip("/").split("/")[-1]  # A5112431388
                if aid.startswith("A"):
                    meta.setdefault(aid, {"inst": "", "h": 0})
    ids = list(meta.keys())
    print("Looking up %d unique authors on OpenAlex (institution + h-index)." % len(ids))
    for i in range(0, len(ids), 50):
        chunk = ids[i:i + 50]
        try:
            resp = guarded_get("https://api.openalex.org/authors", params={
                "filter": "openalex_id:" + "|".join(chunk), "per-page": 50,
                "select": "id,last_known_institutions,affiliations,summary_stats",
                "mailto": mailto,
            })
            for au in resp.json().get("results", []):
                aid = (au.get("id") or "").rstrip("/").split("/")[-1]
                if aid not in meta:
                    continue
                inst = profile_inst(au)
                if inst:
                    meta[aid]["inst"] = inst
                h = ((au.get("summary_stats") or {}).get("h_index")) or 0
                meta[aid]["h"] = int(h)
        except Exception as exc:  # noqa: BLE001
            print("  author batch %d failed: %s" % (i // 50, str(exc)[:120]))
        time.sleep(0.3)

    backfilled, topcount = 0, 0
    for uid, rec in existing.items():
        top = False
        for a in rec.get("authors", []):
            if not a.get("url"):
                continue
            aid = a["url"].rstrip("/").split("/")[-1]
            m = meta.get(aid) or {}
            if not a.get("inst") and m.get("inst"):
                a["inst"] = m["inst"]
                backfilled += 1
            if m.get("h", 0) >= H_TOP:
                top = True
        if top:
            rec["top_author"] = True
            topcount += 1

    # Third pass (opt-in): resolve still-missing institutions by author name,
    # then rebuild each record's affiliation list from the final institutions.
    name_inst = resolve_by_name(existing, mailto) if args.resolve_names else {}
    resolved = 0
    for uid, rec in existing.items():
        for a in rec.get("authors", []):
            if not a.get("inst") and a.get("name"):
                inst = name_inst.get(norm_name(a["name"]))
                if inst:
                    a["inst"] = inst
                    resolved += 1
        affs = []
        for a in rec.get("authors", []):
            if a.get("inst") and a["inst"] not in affs:
                affs.append(a["inst"])
        rec["affiliations"] = affs[:8]

    write_json(out_path, existing)
    print("Wrote %d author records (%d newly enriched, %d backfilled, %d name-resolved, %d with a top-researcher author)."
          % (len(existing), got, backfilled, resolved, topcount))


if __name__ == "__main__":
    main()
