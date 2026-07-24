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
from datetime import datetime, timezone

from jinja2 import Environment, FileSystemLoader, select_autoescape

from common import CFG, ROOT, log, read_jsonl, write_json

# Top research institutions (accounting/finance/economics). A paper affiliated
# with any of these is never hidden by the technical filter. Lowercase
# substrings matched against OpenAlex institution display names.
TOP_INSTITUTIONS = [
    "harvard", "stanford", "massachusetts institute of technology", "mit sloan",
    "university of chicago", "university of pennsylvania", "wharton", "columbia",
    "new york university", "berkeley", "northwestern", "yale", "duke university",
    "university of michigan", "los angeles", "cornell", "carnegie mellon",
    "university of texas at dallas", "university of texas at austin", "ohio state",
    "indiana university", "university of washington", "university of southern california",
    "dartmouth", "university of north carolina", "emory", "georgetown",
    "university of rochester", "washington university in st", "university of illinois",
    "boston college", "university of minnesota", "michigan state", "arizona state",
    "university of iowa", "university of wisconsin", "national university of singapore",
    "hong kong university of science", "university of hong kong", "nanyang technological",
    "tsinghua", "peking university", "university of toronto", "princeton",
    "california institute of technology", "university of maryland", "london business school",
    "insead", "university of oxford", "university of cambridge",
    "london school of economics", "bocconi", "university of mannheim",
]

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
                    p["affiliations"] = a["affiliations"]
                if a.get("top_author"):
                    p["prestige"] = True  # a highly-cited author
            affs = " ; ".join(p.get("affiliations") or []).lower()
            if affs and any(t in affs for t in TOP_INSTITUTIONS):
                p["prestige"] = True  # a top-50 institution
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
