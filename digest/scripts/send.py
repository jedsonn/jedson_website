"""Send the weekly digest email to confirmed subscribers.

Pipeline: read confirmed, non-unsubscribed rows from `web_subscribers`
(Supabase REST, service-role key — the table's RLS has no SELECT policy, so a
privileged key is required), render the edition email once via
`newsletter.build_email`, substitute a per-recipient unsubscribe link, and
deliver each message through Resend.

SAFETY — this script does not send anything unless you ask it to:
  * default is a DRY RUN: it lists recipients and writes the rendered email to
    a file, but sends zero messages.
  * `--send` is required to actually deliver to the subscriber list.
  * `--test you@example.com` sends exactly one message to one address and never
    touches the subscriber list (still needs --send to leave the machine).

Environment (all read from the process env; nothing is hard-coded):
  SUPABASE_URL / SB_URL          e.g. https://xxxx.supabase.co
  SUPABASE_SERVICE_ROLE_KEY      service-role key (RLS bypass) to read the list
  RESEND_API_KEY                 Resend API key (only needed to actually send)
  MAIL_FROM                      verified sender, e.g.
                                 "AI Business Research <digest@jedsonpinto.com>"
  MAIL_REPLY_TO                  optional reply-to (default: config contact_email)
  UNSUB_BASE_URL                 optional; unsubscribe endpoint. Defaults to
                                 {SUPABASE_URL}/functions/v1/unsub. Each
                                 recipient gets {UNSUB_BASE_URL}?t=<unsub_token>.
                                 Set to empty to fall back to a mailto: opt-out.

Usage:
  # Preview only (no send, no keys beyond the DB read):
  python3 scripts/send.py --date 2026-07-29 --out /tmp/digest.html
  # One real test message to yourself:
  python3 scripts/send.py --test you@uni.edu --send
  # Real send to all confirmed subscribers:
  python3 scripts/send.py --date 2026-07-29 --send
"""
import argparse
import json
import os
import sys
import time
from urllib.parse import quote

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import newsletter  # noqa: E402  (sibling module; single source of the template)

CONTACT = "jedson.pinto@utdallas.edu"
UNSUB_SENTINEL = "@@UNSUB_URL@@"  # rendered once, replaced per recipient
RESEND_ENDPOINT = "https://api.resend.com/emails"


def env(*names, default=None):
    for n in names:
        v = os.environ.get(n)
        if v:
            return v
    return default


def die(msg):
    sys.stderr.write("error: %s\n" % msg)
    sys.exit(2)


def fetch_subscribers(sb_url, key, audience="confirmed"):
    """Return [{email, unsub_token}, ...] from web_subscribers via REST.

    Only active (not unsubscribed) rows. `audience` 'confirmed' additionally
    requires confirmed=true; 'all' takes every non-unsubscribed row."""
    base = sb_url.rstrip("/") + "/rest/v1/web_subscribers"
    params = ["select=email,unsub_token", "unsubscribed_at=is.null",
              "order=created_at.asc"]
    if audience == "confirmed":
        params.append("confirmed=eq.true")
    headers = {"apikey": key, "Authorization": "Bearer " + key,
               "Accept": "application/json"}
    rows, offset, page = [], 0, 1000
    while True:
        h = dict(headers)
        h["Range-Unit"] = "items"
        h["Range"] = "%d-%d" % (offset, offset + page - 1)
        r = requests.get(base + "?" + "&".join(params), headers=h, timeout=30)
        if r.status_code not in (200, 206):
            die("Supabase read failed (%d): %s" % (r.status_code, r.text[:300]))
        batch = r.json()
        rows.extend(batch)
        if len(batch) < page:
            break
        offset += page
    # de-dupe by email, keep first (a unique index should already prevent dupes)
    seen, out = set(), []
    for row in rows:
        e = (row.get("email") or "").strip()
        if e and e.lower() not in seen:
            seen.add(e.lower())
            out.append({"email": e, "unsub_token": row.get("unsub_token")})
    return out


def unsub_url(token, base):
    if base and token:
        return "%s?t=%s" % (base.rstrip("/"), quote(str(token)))
    # No endpoint configured (or a test with no token): mailto opt-out. Fully
    # CAN-SPAM compliant and honored by Gmail/Apple as a List-Unsubscribe target.
    return "mailto:%s?subject=Unsubscribe%%20digest" % CONTACT


def send_one(api_key, mail_from, reply_to, to_email, subject, html, unsub):
    """Send one email through Resend. Returns (ok, detail)."""
    headers = {"Authorization": "Bearer " + api_key,
               "Content-Type": "application/json"}
    # RFC 8058 one-click unsubscribe. mailto is always included as a fallback.
    lu = "<%s>, <mailto:%s?subject=Unsubscribe>" % (unsub, CONTACT) \
        if unsub.startswith("http") else "<%s>" % unsub
    payload = {
        "from": mail_from,
        "to": [to_email],
        "subject": subject,
        "html": html,
        "reply_to": reply_to,
        "headers": {
            "List-Unsubscribe": lu,
            "List-Unsubscribe-Post": "List-Unsubscribe=One-Click",
        },
    }
    try:
        r = requests.post(RESEND_ENDPOINT, headers=headers,
                          data=json.dumps(payload), timeout=30)
    except requests.RequestException as e:
        return False, "request error: %s" % e
    if r.status_code in (200, 201):
        try:
            return True, r.json().get("id", "sent")
        except ValueError:
            return True, "sent"
    return False, "HTTP %d: %s" % (r.status_code, r.text[:300])


def main():
    ap = argparse.ArgumentParser(description="Send the weekly digest to subscribers.")
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--since", default=None, help="ISO date; default 7 days before --date")
    ap.add_argument("--date", default=None, help="edition date (default: today UTC)")
    ap.add_argument("--sample", action="store_true",
                    help="ignore date window; pick prestige papers (preview)")
    ap.add_argument("--subject", default=None)
    ap.add_argument("--audience", choices=["confirmed", "all"], default="confirmed",
                    help="'confirmed' (default) or 'all' non-unsubscribed rows")
    ap.add_argument("--test", metavar="EMAIL", default=None,
                    help="send a single message to EMAIL; ignore the subscriber list")
    ap.add_argument("--limit", type=int, default=None, help="cap number of recipients")
    ap.add_argument("--out", default=None, help="also write the rendered email HTML here")
    ap.add_argument("--send", action="store_true",
                    help="ACTUALLY send. Without this it is a dry run.")
    args = ap.parse_args()

    # --- render the edition (once) ---
    data = newsletter.load_papers()
    picks, total, nice_date = newsletter.select(
        data, args.top, args.since, args.date, args.sample)
    if not picks:
        die("No papers selected for this window — nothing to send. "
            "Check --date/--since or use --sample to preview.")
    subject = args.subject or ("AI Business Research — weekly digest, " + nice_date)
    html_tpl = newsletter.build_email(picks, total, nice_date, UNSUB_SENTINEL)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(html_tpl.replace(UNSUB_SENTINEL, unsub_url(None, None)))
        print("Wrote preview -> %s" % args.out)

    # --- resolve recipients ---
    unsub_base = env("UNSUB_BASE_URL", default=None)
    sb_url = env("SUPABASE_URL", "SB_URL")
    if unsub_base is None and sb_url:
        unsub_base = sb_url.rstrip("/") + "/functions/v1/unsub"

    if args.test:
        recipients = [{"email": args.test, "unsub_token": None}]
    else:
        if not sb_url:
            die("SUPABASE_URL (or SB_URL) is required to read the subscriber list.")
        key = env("SUPABASE_SERVICE_ROLE_KEY")
        if not key:
            die("SUPABASE_SERVICE_ROLE_KEY is required to read the subscriber list.")
        recipients = fetch_subscribers(sb_url, key, args.audience)
        if args.limit:
            recipients = recipients[:args.limit]

    print("Edition: %s  |  %d papers shown of %s total  |  subject: %s"
          % (nice_date, len(picks), "{:,}".format(total), subject))
    print("Audience: %s  |  recipients: %d%s"
          % (("test" if args.test else args.audience), len(recipients),
             ("" if unsub_base else "  (mailto unsubscribe — no endpoint set)")))

    if not recipients:
        print("\nNo recipients. Nothing to send.")
        if args.audience == "confirmed" and not args.test:
            print("Note: no subscribers have confirmed=true. Confirm addresses or "
                  "send with --audience all once a confirmation flow exists.")
        return

    # --- dry run stops here ---
    if not args.send:
        print("\nDRY RUN — no email sent. Recipients that WOULD receive it:")
        for r in recipients:
            print("  - %s" % r["email"])
        print("\nRe-run with --send to deliver.")
        return

    # --- real send ---
    api_key = env("RESEND_API_KEY")
    mail_from = env("MAIL_FROM")
    reply_to = env("MAIL_REPLY_TO", default=CONTACT)
    if not api_key:
        die("RESEND_API_KEY is required to send.")
    if not mail_from:
        die("MAIL_FROM is required to send (e.g. 'Digest <digest@yourdomain>').")

    ok, failed = 0, []
    for i, r in enumerate(recipients):
        uu = unsub_url(r["unsub_token"], unsub_base)
        html = html_tpl.replace(UNSUB_SENTINEL, uu)
        success, detail = send_one(api_key, mail_from, reply_to,
                                   r["email"], subject, html, uu)
        if success:
            ok += 1
            print("  sent  %s  (%s)" % (r["email"], detail))
        else:
            failed.append((r["email"], detail))
            print("  FAIL  %s  (%s)" % (r["email"], detail))
        if i + 1 < len(recipients):
            time.sleep(0.6)  # stay under Resend's ~2 req/s

    print("\nDone. %d sent, %d failed." % (ok, len(failed)))
    if failed:
        for e, d in failed:
            sys.stderr.write("failed: %s — %s\n" % (e, d))
        sys.exit(1)


if __name__ == "__main__":
    main()
