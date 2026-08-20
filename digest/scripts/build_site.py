"""Stage 5. Render the static site from the persistent index.

Outputs at the repo root, which is what GitHub Pages serves:
  index.html        dashboard, all papers, client-side filtering
  feed.xml          RSS of the most recent items
  data/papers.json  the public record, so other people can build on it

The site always renders the whole index, not just this edition. The edition
number and date in the masthead describe the most recent run.

Usage:
  python3 scripts/build_site.py --edition 12 --date 2026-07-23
"""

import argparse
import html
import json
import os
import re
from datetime import datetime, timezone

from jinja2 import Environment, FileSystemLoader, select_autoescape

from common import CFG, ROOT, log, read_jsonl, write_json

# Top US research universities (accounting/finance/economics/management).
# A paper affiliated with any of these is never hidden by the technical
# filter, and it appears in the "Featured" view.  The list is deliberately
# US-centric: the digest serves US scholars and the featured toggle is an
# information-overload filter, not a quality ranking.
#
# Each entry is a lowercase substring matched against OpenAlex display names.
# Be specific enough to avoid false positives: "northwestern university"
# (not "northwestern" alone, which matches Northwestern Polytechnical U.).
US_TOP = [
    "harvard university", "harvard business school",
    "stanford university", "stanford graduate school",
    "massachusetts institute of technology", "mit sloan",
    "university of chicago", "booth school",
    "university of pennsylvania", "wharton",
    "columbia university", "columbia business school",
    "new york university", "nyu stern",
    "university of california, berkeley", "haas school",
    "northwestern university", "kellogg school",
    "yale university",
    "duke university", "fuqua school",
    "university of michigan, ann arbor", "ross school",
    "university of california, los angeles",
    "cornell university", "johnson school",
    "carnegie mellon university", "tepper school",
    "university of texas at dallas", "the university of texas at dallas", "naveen jindal school",
    "university of texas at austin", "the university of texas at austin", "mccombs school",
    "ohio state university",
    "indiana university bloomington", "kelley school",
    "university of washington, seattle",
    "university of southern california", "marshall school",
    "dartmouth college", "tuck school",
    "university of north carolina at chapel hill", "kenan-flagler",
    "emory university", "goizueta",
    "georgetown university",
    "university of rochester", "simon school",
    "washington university in st. louis", "olin school",
    "university of illinois urbana", "gies college",
    "boston college", "carroll school",
    "university of minnesota", "carlson school",
    "michigan state university", "broad college",
    "arizona state university", "carey school",
    "university of iowa", "tippie college",
    "university of wisconsin-madison",
    "princeton university",
    "california institute of technology",
    "university of maryland, college park", "smith school",
    "johns hopkins university",
    "rutgers university", "rutgers business school",
    "university of virginia", "darden school",
    "boston university", "questrom school",
    "georgia institute of technology",
    "rice university", "jones school",
    "vanderbilt university", "owen school",
    "university of notre dame", "mendoza college",
    "university of florida", "warrington college",
]

# Elite non-US schools that also qualify for featured. Keep this short:
# the best European business schools plus the University of Toronto.
INTL_TOP = [
    "london business school",
    "london school of economics",
    "university of oxford", "said business school",
    "university of cambridge", "judge business school",
    "insead",
    "bocconi", "sda bocconi",
    "university of mannheim",
    "university of toronto", "rotman school",
]

# The union is checked for the prestige flag; US_TOP also gets the us_top
# sort bonus.
TOP_INSTITUTIONS = US_TOP + INTL_TOP


def _aff_matches(affs_list, patterns):
    """True if at least one affiliation matches a pattern.

    Each affiliation is checked individually (not joined) and the pattern
    must appear at the START of the lowercased name.  This prevents false
    positives like "California University of Pennsylvania" matching the
    "university of pennsylvania" pattern.
    """
    for a in affs_list:
        al = a.lower()
        for t in patterns:
            if al.startswith(t):
                return True
    return False


# OpenAlex attaches noisy affiliations to authors — hospitals/clinics from
# name collisions, and publisher imprints ("Harvard University Press") standing
# in for the university. These substrings mark a display affiliation as noise
# and are dropped (the top-institution flags above are computed on the cleaned
# list, so a real co-author's school still counts).
AFFILIATION_DROP = (
    "hospital", "hôpital", "clinic", "medical center", "medical centre",
    "health system", "cancer center", "cancer centre",
)


def clean_affiliations(affs):
    """Tidy affiliations for display: normalize publisher imprints
    (`X University Press` -> `X University`), drop non-academic mismatches, and
    surface any recognized top institution first so the featured school leads the
    line instead of a stray first-author affiliation. Stable within each tier."""
    normed, seen = [], set()
    for a in affs:
        a = re.sub(r"\s+University Press\b", " University", a).strip()
        if a and a not in seen:
            seen.add(a)
            normed.append(a)
    kept = [a for a in normed if not any(n in a.lower() for n in AFFILIATION_DROP)]
    kept = kept or normed  # never blank the list entirely

    def prio(a):
        if _aff_matches([a], US_TOP):
            return 0
        if _aff_matches([a], TOP_INSTITUTIONS):
            return 1
        return 2

    return sorted(kept, key=prio)


PUBLIC_FIELDS = [
    "uid", "doi", "arxiv_id", "title", "authors", "affiliations", "posted",
    "added", "source_label", "url", "alt_urls", "field", "role", "bullets",
    "bullet_provenance", "models", "open_weights", "validated",
    "validation_note", "salience", "edition", "n", "citations", "audience",
]


def public_view(rec):
    """Publish our own writing plus open metadata. Never publish abstracts."""
    out = {k: rec.get(k) for k in PUBLIC_FIELDS if rec.get(k) not in (None, "", [])}
    out.setdefault("bullets", [])
    out.setdefault("bullet_provenance", "none")
    out.setdefault("authors", [])
    out.setdefault("models", [])
    out["validated"] = rec.get("validated")
    return out


def build_rss(papers, brand, limit):
    now = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
    items = []
    for p in papers[:limit]:
        desc = " ".join(p.get("bullets") or []) or "Metadata only. Follow the link for the paper."
        items.append(
            "<item><title>%s</title><link>%s</link><guid isPermaLink=\"false\">%s</guid>"
            "<category>%s</category><category>%s</category><description>%s</description></item>"
            % (html.escape(p.get("title", "")), html.escape(p.get("url", "")),
               html.escape(p.get("uid", "")), html.escape(p.get("field", "")),
               html.escape(p.get("role", "")), html.escape(desc))
        )
    return ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
            "<rss version=\"2.0\"><channel>"
            "<title>%s</title><link>%s</link><description>%s</description>"
            "<lastBuildDate>%s</lastBuildDate>%s</channel></rss>"
            % (html.escape(brand["name"]), html.escape(brand["site_url"]),
               html.escape(brand["tagline"]), now, "".join(items)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--edition", type=int, required=True)
    ap.add_argument("--date", required=True)
    args = ap.parse_args()

    index = read_jsonl(os.path.join(ROOT, "data", "index.jsonl"))
    if not index:
        raise SystemExit("data/index.jsonl is empty. Nothing to build.")

    # Editorial exclusions (duplicates, junk). The index stays append-only; these
    # uids are simply not rendered. One uid per line in data/exclude.txt; # comments.
    excl = set()
    epath = os.path.join(ROOT, "data", "exclude.txt")
    if os.path.exists(epath):
        for line in open(epath, encoding="utf-8"):
            uid = line.split("#")[0].strip()
            if uid:
                excl.add(uid)
    if excl:
        before = len(index)
        index = [r for r in index if r.get("uid") not in excl]
        log("Excluded %d record(s) via data/exclude.txt." % (before - len(index)))

    papers = [public_view(r) for r in index]
    # Stable archive number: index.jsonl is append-order (oldest first), so the
    # newest paper's number equals the running total ever classified.
    for i, p in enumerate(papers):
        p["n"] = i + 1

    # Attach OpenAlex author profiles + institutions (open metadata) if present,
    # and flag papers from top-tier institutions so the technical filter never
    # hides them.
    apath = os.path.join(ROOT, "data", "authors.json")
    if os.path.exists(apath):
        amap = json.load(open(apath, encoding="utf-8"))
        for p in papers:
            a = amap.get(p.get("uid"))
            if a and a.get("authors"):
                p["authors_detailed"] = a["authors"]
                if a.get("affiliations"):
                    p["affiliations"] = clean_affiliations(a["affiliations"])
            affs_list = p.get("affiliations") or []
            if affs_list and _aff_matches(affs_list, TOP_INSTITUTIONS):
                p["prestige"] = True  # recognized institution
            if affs_list and _aff_matches(affs_list, US_TOP):
                p["us_top"] = True  # US top university — sorts first
    papers.sort(key=lambda p: (p.get("posted") or "", p.get("edition") or 0), reverse=True)

    this_edition = sum(1 for r in index if r.get("edition") == args.edition)
    with_bullets = sum(1 for p in papers if len(p.get("bullets") or []) == 3)
    log("Index %d papers. This edition %d. With three bullets %d (%.0f%%)."
        % (len(papers), this_edition, with_bullets, 100.0 * with_bullets / max(len(papers), 1)))

    env = Environment(loader=FileSystemLoader(os.path.join(ROOT, "templates")),
                      autoescape=select_autoescape(["html"]))
    tpl = env.get_template("index.html.jinja")

    payload = json.dumps({
        "papers": papers,
        "fields": CFG["taxonomy"]["fields"],
        "roles": CFG["taxonomy"]["roles"],
    }, ensure_ascii=False)

    rendered = tpl.render(
        brand=CFG["brand"],
        roles=CFG["taxonomy"]["roles"],
        fields=CFG["taxonomy"]["fields"],
        edition={"number": args.edition, "date": args.date, "count": this_edition},
        payload=payload,
    )
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(rendered)

    with open(os.path.join(ROOT, "feed.xml"), "w", encoding="utf-8") as fh:
        fh.write(build_rss(papers, CFG["brand"], CFG["site"]["rss_items"]))

    write_json(os.path.join(ROOT, "data", "papers.json"),
               {"generated": args.date, "edition": args.edition,
                "count": len(papers), "papers": papers})
    write_json(os.path.join(ROOT, "data", "last-run.json"),
               {"edition": args.edition, "date": args.date, "total": len(papers),
                "this_edition": this_edition, "with_bullets": with_bullets})

    log("Wrote index.html, feed.xml, data/papers.json, data/last-run.json")


if __name__ == "__main__":
    main()
