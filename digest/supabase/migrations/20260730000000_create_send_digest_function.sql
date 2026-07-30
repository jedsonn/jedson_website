-- Send one digest edition to every active subscriber via Resend.
-- Applied to the live project (rumo) on 2026-07-30.
--
-- Reads the API key from Vault (digest_resend_api_key). The html_template
-- must contain the sentinel @@UNSUB_URL@@ where each recipient's personal
-- unsubscribe link goes (newsletter.py / send.py use the same convention).
-- Audience: every non-unsubscribed row. The confirmed flag is deliberately
-- not filtered on until a double-opt-in flow exists (see digest/SEND.md).
create or replace function public.send_digest(subject text, html_template text)
returns table(email text, request_id bigint)
language plpgsql
security definer
set search_path = ''
as $$
declare
  k text;
  u text;
  r record;
  rid bigint;
begin
  select decrypted_secret into k
  from vault.decrypted_secrets
  where name = 'digest_resend_api_key'
  limit 1;
  if k is null then
    raise exception 'digest_resend_api_key not found in vault';
  end if;

  for r in
    select ws.email, ws.unsub_token
    from public.web_subscribers ws
    where ws.unsubscribed_at is null
    order by ws.created_at
  loop
    u := 'https://nmkbznbjgfuqopezfncs.supabase.co/functions/v1/unsub?t=' || r.unsub_token::text;
    select net.http_post(
      url := 'https://api.resend.com/emails',
      headers := jsonb_build_object(
        'Authorization', 'Bearer ' || k,
        'Content-Type', 'application/json'),
      body := jsonb_build_object(
        'from', 'AI Business Research <digest@myresolve.ai>',
        'to', jsonb_build_array(r.email),
        'subject', subject,
        'html', replace(html_template, '@@UNSUB_URL@@', u),
        'reply_to', 'jedson.pinto@utdallas.edu',
        'headers', jsonb_build_object(
          'List-Unsubscribe', '<' || u || '>, <mailto:jedson.pinto@utdallas.edu?subject=Unsubscribe>',
          'List-Unsubscribe-Post', 'List-Unsubscribe=One-Click')),
      timeout_milliseconds := 15000
    ) into rid;
    email := r.email;
    request_id := rid;
    return next;
  end loop;
end;
$$;

-- Sending mail must never be reachable through the public API keys.
revoke execute on function public.send_digest(text, text) from public, anon, authenticated;
