"""Render the weekly digest email from data/papers.json.

A lean teaser: ~5 papers, each shown as title + institutions only (no summaries),
plus a prominent link to the dashboard. The point is to drive clicks to the page,
where the full three-bullet summaries live.

Email-safe HTML: table layout, inline styles, web-safe fonts, ~600px, no images.

Selection: papers posted on/after --since (default 7 days back), ranked by
US top university -> featured (top institution / prominent author) -> salience,
capped at --top. So the email always leads with the week's top-institution /
highest-quality work. --sample ignores the date window (preview against the
current index).

Usage:
  python3 scripts/newsletter.py --out email.html --top 5 --sample
  python3 scripts/newsletter.py --out email.html --top 5 --since 2026-07-17 \
      --date 2026-07-24 --unsub "https://.../unsub?t=TOKEN"
"""
import argparse
import html
import json
import os
from datetime import datetime, timedelta, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INK, INK2, INK3 = "#14181d", "#565f6a", "#8b939e"
ACCENT, RULE, PAPER = "#1a5276", "#e4e8ec", "#f6f7f9"
SERIF = "Georgia,'Times New Roman',serif"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"
FIELD = {"accounting": "Accounting", "finance": "Finance",
         "economics": "Economics", "management": "Management", "other": "Other"}
SITE = "https://www.jedsonpinto.com/digest"


def esc(s):
    return html.escape(str(s or ""))


def rank(p):
    # Quality first for a 5-paper highlight: top US school, then any featured,
    # then salience; recency only breaks ties.
    return (1 if p.get("us_top") else 0, 1 if p.get("prestige") else 0,
            p.get("salience") or 0, p.get("posted") or "")


def institutions(p):
    affs = p.get("affiliations") or []
    if not affs:
        return ""
    shown = affs[:3]
    txt = " · ".join(shown) + (" +%d more" % (len(affs) - 3) if len(affs) > 3 else "")
    return esc(txt)


def authors_line(p):
    det = p.get("authors_detailed") or []
    names = [a.get("name", "") for a in det] or (p.get("authors") or [])
    if not names:
        return ""
    return esc(", ".join(names[:3]) + (" +%d" % (len(names) - 3) if len(names) > 3 else ""))


def paper_row(p):
    star = ('<span style="color:%s;">&#9733;</span> ' % ACCENT) if p.get("prestige") else ""
    tag = "%s%s&nbsp;&nbsp;·&nbsp;&nbsp;%s" % (
        star, esc(FIELD.get(p.get("field"), p.get("field"))), esc(p.get("posted", "")))
    inst = institutions(p)
    auth = authors_line(p)
    # Authors first, then a lighter, smaller institution line beneath them.
    meta = ""
    if auth:
        meta += ('<div style="font:400 12px/1.45 %s;color:%s;margin:4px 0 0;">%s</div>'
                 % (SANS, INK3, auth))
    if inst:
        meta += ('<div style="font:400 11px/1.4 %s;color:%s;margin:2px 0 0;">%s</div>'
                 % (SANS, INK3, inst))
    # Title clamped to a single line with an ellipsis so rows stay uniform.
    return (
        '<tr><td style="padding:13px 32px;border-bottom:1px solid %s;">'
        '<div style="font:600 10px %s;letter-spacing:1.2px;text-transform:uppercase;color:%s;">%s</div>'
        '<a href="%s" style="display:block;font:400 15px/1.3 %s;color:%s;text-decoration:none;margin:5px 0 0;'
        'white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">%s</a>'
        '%s'
        '</td></tr>'
        % (RULE, SANS, INK3, tag, esc(p.get("url", "")), SERIF, ACCENT,
           esc(p.get("title", "")), meta)
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--since", default=None, help="ISO date; default 7 days before --date")
    ap.add_argument("--date", default=datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    ap.add_argument("--sample", action="store_true", help="ignore date window; preview")
    ap.add_argument("--unsub", default="{{UNSUBSCRIBE_URL}}")
    args = ap.parse_args()

    data = json.load(open(os.path.join(ROOT, "data", "papers.json"), encoding="utf-8"))
    papers = data["papers"]
    total = data.get("count", len(papers))

    if args.sample:
        pool = [p for p in papers if p.get("prestige")] or papers
    else:
        since = args.since or (datetime.strptime(args.date, "%Y-%m-%d") - timedelta(days=7)).strftime("%Y-%m-%d")
        pool = [p for p in papers if (p.get("posted") or "") >= since]
    pool.sort(key=rank, reverse=True)
    picks = pool[:args.top]

    nice_date = datetime.strptime(args.date, "%Y-%m-%d").strftime("%B %-d, %Y")
    rows = "".join(paper_row(p) for p in picks)

    email = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI Business Research — weekly</title></head>
<body style="margin:0;padding:0;background:#eceef1;">
<table role="presentation" width="100%%" cellpadding="0" cellspacing="0" style="background:#eceef1;">
<tr><td align="center" style="padding:24px 12px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;background:#ffffff;border:1px solid %(rule)s;border-radius:12px;overflow:hidden;">
  <tr><td style="padding:28px 32px 18px;border-bottom:2px solid %(ink)s;">
    <div style="font:600 11px %(sans)s;letter-spacing:2px;text-transform:uppercase;color:%(accent)s;">Weekly digest &nbsp;·&nbsp; %(date)s</div>
    <div style="font:400 27px/1.05 %(serif)s;color:%(ink)s;margin:8px 0 0;">AI Business Research</div>
    <div style="font:400 13px/1.5 %(sans)s;color:%(ink2)s;margin:6px 0 0;">A few of this week's new papers using AI and large language models in accounting, finance, and economics &mdash; open the dashboard for the full set and the summaries.</div>
    <div style="text-align:center;margin:18px 0 2px;"><a href="%(site)s" style="display:inline-block;background:%(accent)s;color:#ffffff;font:600 13px %(sans)s;text-decoration:none;padding:11px 26px;border-radius:8px;">Browse all %(total)s papers &rarr;</a></div>
  </td></tr>
  %(rows)s
  <tr><td style="padding:18px 32px 22px;background:%(paper)s;border-top:1px solid %(rule)s;">
    <div style="font:400 11.5px/1.6 %(sans)s;color:%(ink3)s;">
      You are receiving this because you subscribed at jedsonpinto.com/digest.<br>
      <a href="%(unsub)s" style="color:%(ink3)s;text-decoration:underline;">Unsubscribe</a> &nbsp;·&nbsp; Curated by Jedson Pinto, UT Dallas. Independent; not affiliated with SSRN, arXiv, or any publisher.
    </div>
  </td></tr>
</table>
</td></tr></table>
</body></html>""" % {
        "rule": RULE, "ink": INK, "ink2": INK2, "ink3": INK3, "accent": ACCENT,
        "paper": PAPER, "sans": SANS, "serif": SERIF, "site": SITE,
        "date": esc(nice_date), "rows": rows, "total": "{:,}".format(total), "unsub": esc(args.unsub),
    }

    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(email)
    print("Wrote %s with %d papers (of %d in pool)." % (args.out, len(picks), len(pool)))


if __name__ == "__main__":
    main()
