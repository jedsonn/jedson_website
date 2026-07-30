# Newsletter send pipeline

How the weekly digest email actually reaches subscribers. The site's subscribe
form writes rows to the Supabase `web_subscribers` table; this pipeline reads
that table, renders the edition email, and delivers it through **Resend**.

Nothing here sends on a schedule. A send is always a deliberate, manual action.

## Pieces

| Piece | Where | Role |
|---|---|---|
| `scripts/newsletter.py` | this repo | Renders the email HTML (`build_email`) and picks the papers (`select`). Single source of the template. |
| `scripts/send.py` | this repo | Reads confirmed subscribers, renders once, personalizes the unsubscribe link, sends via Resend. **Dry run by default.** |
| `.github/workflows/digest-newsletter.yml` | this repo | Manual `workflow_dispatch` wrapper. `dry_run` defaults to **true**. |
| `supabase/functions/unsub/` | deployed to Supabase | Public one-click / confirm unsubscribe endpoint, authenticated by each row's `unsub_token`. |
| `web_subscribers.unsubscribed_at` | Supabase | Opt-out timestamp. `NULL` = active. Added by `supabase/migrations/20260729000000_add_unsubscribed_at.sql`. |

## One-time setup

**Resend**
1. Create a Resend account and verify the sending domain (e.g. `jedsonpinto.com`)
   — SPF/DKIM records. Sending from an unverified domain will bounce.
2. Create an API key.

**GitHub repo → Settings → Secrets and variables → Actions**

Secrets:
- `SUPABASE_SERVICE_ROLE_KEY` — reads the subscriber list. The table's RLS has
  only an INSERT policy (for the public subscribe form), so reads need this
  privileged key. Keep it secret; it is never exposed to the site.
- `RESEND_API_KEY` — used only on a real send.

Variables:
- `MAIL_FROM` — must be on a Resend-verified domain. Currently
  `AI Business Research <digest@myresolve.ai>` (the workflow's default):
  myresolve.ai is the account's one verified domain, and the free plan allows
  exactly one, so `digest@jedsonpinto.com` waits on a plan upgrade, a domain
  swap, or a second account.
- `MAIL_REPLY_TO` — optional, defaults to `jedson.pinto@utdallas.edu`.
- `SUPABASE_URL` — optional; a default is baked into the workflow.

The unsubscribe endpoint (`unsub`) needs no extra config — Supabase injects
`SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY` into edge functions at runtime.

## Sending

**From GitHub (normal path):** Actions → *Digest newsletter* → *Run workflow*.
- Leave `dry_run = true` (default) → renders the email, lists who would receive
  it, uploads a `digest-preview` artifact. **Sends nothing.**
- Set `test_email` and `dry_run = false` → one real message to that address.
- Set `dry_run = false` (no `test_email`) → real send to the `audience`.

**Locally (for development):**
```bash
cd digest
# preview only, no network beyond the template render:
python3 scripts/send.py --test you@uni.edu --date 2026-07-29 --out /tmp/d.html
# real single test (needs RESEND_API_KEY + MAIL_FROM in env):
python3 scripts/send.py --test you@uni.edu --send
# real send to confirmed subscribers (needs SUPABASE_* + RESEND_* + MAIL_FROM):
python3 scripts/send.py --date 2026-07-29 --send
```

`send.py --help` lists every flag. Key ones: `--audience {confirmed,all}`,
`--top N`, `--since DATE`, `--limit N`, `--sample` (ignore the date window),
`--out FILE` (write the preview).

## Sending through the database (no GitHub secrets needed)

The 2026-07-29 test edition went out this way, and it remains a first-class
path. The Resend key lives in Supabase **Vault** (secret name
`digest_resend_api_key`, project `rumo`), and a SQL function wraps the whole
send — same pattern the site's `notify_feedback_email` / `notify_subscribe_email`
triggers already use with the older `resend_api_key` secret:

```sql
select * from public.send_digest(
  'AI Business Research — weekly digest, <DATE>',
  $html$ ...rendered email with @@UNSUB_URL@@ in the footer... $html$
);
```

`send_digest(subject, html_template)` reads the key from Vault, loops over
active (non-unsubscribed) subscribers, swaps `@@UNSUB_URL@@` for each
recipient's tokenized unsubscribe link, and POSTs to Resend via `pg_net` with
the RFC 8058 headers. It returns one row per recipient with the async
`request_id`; check delivery with
`select status_code, content from net._http_response where id = <request_id>`.

Render the template with `newsletter.py` (use `--unsub '@@UNSUB_URL@@'`).
Execute rights are revoked from `public` / `anon` / `authenticated`, so the
public API keys can never trigger a send — only privileged access (SQL editor,
MCP, service role) can. Source: `supabase/migrations/20260730000000_create_send_digest_function.sql`.

This is why sending works from environments that cannot reach api.resend.com
directly: the database makes the outbound call.

## Unsubscribe

Every email carries a per-recipient link, `…/functions/v1/unsub?t=<unsub_token>`,
and the RFC 8058 `List-Unsubscribe` / `List-Unsubscribe-Post` headers so Gmail
and Apple Mail show a native one-click unsubscribe.

- A **click** (GET) shows a confirm page — a plain GET never opts anyone out, so
  link scanners that prefetch the URL can't unsubscribe people by accident.
- **Confirm** (or the mail client's one-click, both POST) sets `unsubscribed_at`.

If `UNSUB_BASE_URL` / `SUPABASE_URL` are unset, `send.py` falls back to a
`mailto:` unsubscribe — still compliant, but you process those by hand.

## Known gap: no confirmed subscribers yet

The subscribe form inserts rows with `confirmed = false` and **nothing flips it
to true** — there is no double opt-in flow. So `--audience confirmed` (the
default) currently resolves to **zero recipients**, and a real send is a no-op.

Two ways forward when you want mail to actually go out:
1. **Confirm addresses manually** (fine for a tiny list):
   `update web_subscribers set confirmed = true where email = '…';`
   then send with the default `confirmed` audience.
2. **Send to everyone** who hasn't opted out: run with `audience = all`. Skips
   the confirmation gate; use only for addresses you know opted in.

The clean long-term fix is a double opt-in: on subscribe, email a confirmation
link (another edge function, mirroring `unsub`) that sets `confirmed = true`.
That was scoped out of this pipeline deliberately — the sending machinery is
here and works; wiring confirmation is a separate, additive step.
