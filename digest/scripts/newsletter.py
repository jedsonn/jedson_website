"""Render the weekly digest email from data/papers.json.

Email-safe HTML: table layout, inline styles, web-safe fonts, ~600px. No
external CSS or images, so it renders in Gmail/Outlook/Apple Mail alike.

Selection: papers posted on/after --since (default 7 days back), ordered
date desc -> US top university -> featured -> salience, capped at --top.
Pass --sample to ignore the date window and just take the top featured papers
(useful for previewing the template against the current index).

Usage:
  python3 scripts/newsletter.py --out email.html --top 10 --sample
  python3 scripts/newsletter.py --out email.html --top 10 --since 2026-07-17 \
      --date 2026-07-24 --unsub "https://www.jedsonpinto.com/digest/unsub?t=TOKEN"
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


def esc(s):
    return html.escape(str(s or ""))


def rank(p):
    return (p.get("posted") or "", 1 if p.get("us_top") else 0,
            1 if p.get("prestige") else 0, p.get("salience") or 0)


def byline(p):
    det = p.get("authors_detailed") or []
    names = [a.get("name", "") for a in det] or (p.get("authors") or [])
    if not names:
        return ""
    shown = ", ".join(names[:6]) + (", et al." if len(names) > 6 else "")
    affs = p.get("affiliations") or []
    tail = "  ·  " + esc(" · ".join(affs[:2])) if affs else ""
    return esc(shown) + tail


def paper_row(p):
    tag = "%s&nbsp;&nbsp;·&nbsp;&nbsp;%s" % (esc(FIELD.get(p.get("field"), p.get("field"))),
                                             esc(p.get("posted", "")))
    star = ('<span style="color:%s;font-weight:700;">&#9733; featured</span>&nbsp;&nbsp;·&nbsp;&nbsp;'
            % ACCENT) if p.get("prestige") else ""
    bl = p.get("bullets") or []
    bullets = ""
    if len(bl) == 3:
        bullets = "".join(
            '<div style="font:400 13.5px/1.5 %s;color:%s;margin:3px 0;">%s</div>'
            % (SANS, INK, esc(b)) for b in bl)
    else:
        bullets = ('<div style="font:italic 13px/1.5 %s;color:%s;">Metadata only — follow the link.</div>'
                   % (SANS, INK3))
    bl_line = byline(p)
    byhtml = ('<div style="font:400 12.5px/1.45 %s;color:%s;margin:2px 0 9px;">%s</div>'
              % (SANS, INK2, bl_line)) if bl_line else '<div style="height:6px;"></div>'
    return (
        '<tr><td style="padding:20px 32px;border-bottom:1px solid %s;">'
        '<div style="font:600 10px %s;letter-spacing:1.2px;text-transform:uppercase;color:%s;">%s%s</div>'
        '<a href="%s" style="display:block;font:700 17px/1.3 %s;color:%s;text-decoration:none;margin:7px 0 0;">%s</a>'
        '%s%s'
        '</td></tr>'
        % (RULE, SANS, INK3, star, tag,
           esc(p.get("url", "")), SERIF, ACCENT, esc(p.get("title", "")),
           byhtml, bullets)
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--since", default=None, help="ISO date; default 7 days before --date")
    ap.add_argument("--date", default=datetime.now(timezone.utc).strftime("%Y-%m-%d"))
    ap.add_argument("--sample", action="store_true", help="ignore date window; take top featured")
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
    <div style="font:400 13px/1.5 %(sans)s;color:%(ink2)s;margin:6px 0 0;">The week's new work using or studying AI and large language models in accounting, finance, and economics.</div>
  </td></tr>
  %(rows)s
  <tr><td style="padding:22px 32px;background:%(paper)s;">
    <a href="https://www.jedsonpinto.com/digest" style="font:600 13px %(sans)s;color:%(accent)s;text-decoration:none;">See all %(total)s papers on the dashboard &rarr;</a>
    <div style="font:400 11.5px/1.6 %(sans)s;color:%(ink3)s;margin-top:14px;">
      You are receiving this because you subscribed at jedsonpinto.com/digest.<br>
      <a href="%(unsub)s" style="color:%(ink3)s;text-decoration:underline;">Unsubscribe</a> &nbsp;·&nbsp; Curated by Jedson Pinto, UT Dallas. Independent; not affiliated with SSRN, arXiv, or any publisher.
    </div>
  </td></tr>
</table>
</td></tr></table>
</body></html>""" % {
        "rule": RULE, "ink": INK, "ink2": INK2, "ink3": INK3, "accent": ACCENT,
        "paper": PAPER, "sans": SANS, "serif": SERIF,
        "date": esc(nice_date), "rows": rows, "total": total, "unsub": esc(args.unsub),
    }

    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(email)
    print("Wrote %s with %d papers (of %d in pool)." % (args.out, len(picks), len(pool)))


if __name__ == "__main__":
    main()
