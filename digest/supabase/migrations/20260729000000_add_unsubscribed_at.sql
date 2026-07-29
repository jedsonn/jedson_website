-- web_subscribers: track opt-out for the newsletter send pipeline.
-- Applied to the live project on 2026-07-29. Additive and idempotent.
alter table public.web_subscribers
  add column if not exists unsubscribed_at timestamptz;

comment on column public.web_subscribers.unsubscribed_at is
  'Set by the unsub edge function when a subscriber opts out via their unsub_token. NULL = active. Newsletter send filters on this being NULL.';
