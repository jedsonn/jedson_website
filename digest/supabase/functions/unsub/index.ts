// Unsubscribe endpoint for the weekly digest.
//
// Public (verify_jwt = false) — authenticated by the unguessable per-subscriber
// `unsub_token` (a UUID capability token) carried in the URL, not by a JWT.
// The only thing it can do is set `unsubscribed_at` on the one row whose token
// matches. It never reads or returns subscriber data.
//
// GET  /unsub?t=<token>  -> a confirmation page with a "Confirm" button.
//                           (A plain GET never unsubscribes, so email/link
//                           scanners that prefetch the URL can't opt people out.)
// POST /unsub?t=<token>  -> performs the unsubscribe. Serves both the confirm
//                           form and RFC 8058 List-Unsubscribe one-click.
//
// Env injected by Supabase at runtime: SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY.
import "jsr:@supabase/functions-js/edge-runtime.d.ts";

const SUPABASE_URL = Deno.env.get("SUPABASE_URL")!;
const SERVICE_KEY = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
const REST = `${SUPABASE_URL}/rest/v1/web_subscribers`;
const SITE = "https://www.jedsonpinto.com/digest";
const UUID_RE =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

function page(title: string, message: string, status = 200): Response {
  const html = `<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${title} — AI Business Research</title>
<style>
  body{margin:0;background:#eceef1;font:16px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;color:#14181d;}
  .wrap{max-width:520px;margin:8vh auto;padding:0 20px;}
  .card{background:#fff;border:1px solid #e4e8ec;border-radius:12px;padding:32px 30px;text-align:center;}
  h1{font:400 22px/1.2 Georgia,'Times New Roman',serif;margin:0 0 10px;}
  p{color:#565f6a;margin:0 0 18px;}
  .btn{display:inline-block;background:#1a5276;color:#fff;text-decoration:none;font-weight:600;font-size:15px;padding:11px 26px;border:0;border-radius:8px;cursor:pointer;}
  .muted{font-size:13px;color:#8b939e;margin-top:22px;}
  a{color:#1a5276;}
</style></head><body><div class="wrap"><div class="card">
<h1>${title}</h1>${message}
<div class="muted">AI Business Research · <a href="${SITE}">jedsonpinto.com/digest</a></div>
</div></div></body></html>`;
  return new Response(html, {
    status,
    headers: { "content-type": "text/html; charset=utf-8" },
  });
}

async function tokenExists(token: string): Promise<boolean> {
  const r = await fetch(
    `${REST}?unsub_token=eq.${token}&select=unsub_token`,
    { headers: { apikey: SERVICE_KEY, Authorization: `Bearer ${SERVICE_KEY}` } },
  );
  if (!r.ok) return false;
  const rows = await r.json();
  return Array.isArray(rows) && rows.length > 0;
}

Deno.serve(async (req: Request) => {
  const url = new URL(req.url);
  const token = (url.searchParams.get("t") || "").trim();

  if (!UUID_RE.test(token)) {
    return page("Invalid link",
      "<p>This unsubscribe link is missing or malformed. If you keep getting the digest, reply to any issue and I'll remove you by hand.</p>",
      400);
  }

  if (req.method === "GET") {
    // Show a confirm button. GET must never mutate (prefetch-safe).
    return page("Unsubscribe",
      `<p>Stop receiving the weekly AI Business Research digest?</p>
       <form method="POST" action="/functions/v1/unsub?t=${token}">
         <button class="btn" type="submit">Confirm unsubscribe</button>
       </form>`);
  }

  if (req.method === "POST") {
    const res = await fetch(
      `${REST}?unsub_token=eq.${token}&unsubscribed_at=is.null`,
      {
        method: "PATCH",
        headers: {
          apikey: SERVICE_KEY,
          Authorization: `Bearer ${SERVICE_KEY}`,
          "content-type": "application/json",
          Prefer: "return=representation",
        },
        body: JSON.stringify({ unsubscribed_at: new Date().toISOString() }),
      },
    );
    if (!res.ok) {
      return page("Something went wrong",
        "<p>We couldn't process that just now. Please try again in a moment.</p>",
        502);
    }
    const updated = await res.json();
    if (Array.isArray(updated) && updated.length > 0) {
      return page("Unsubscribed",
        "<p>You're off the list. You won't get the weekly digest anymore. Thanks for reading — the full dashboard stays open to everyone.</p>");
    }
    // 0 rows updated: token already unsubscribed, or unknown.
    if (await tokenExists(token)) {
      return page("Already unsubscribed",
        "<p>You were already removed — no further emails will be sent.</p>");
    }
    return page("Invalid link",
      "<p>We couldn't find that subscription. It may have already been removed.</p>",
      404);
  }

  return page("Method not allowed",
    "<p>Use the link from the email.</p>", 405);
});
