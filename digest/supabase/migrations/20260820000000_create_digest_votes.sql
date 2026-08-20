-- Digest paper voting: up, down, or unrelated.
-- One vote per client per paper (upsert to change vote; delete to retract).
-- Applied to the live project (rumo) on 2026-08-20.
create table public.digest_votes (
  id        bigint generated always as identity primary key,
  paper_uid text    not null,
  vote      text    not null check (vote in ('up', 'down', 'unrelated')),
  client_id text    not null,
  created_at timestamptz not null default now()
);

create unique index digest_votes_uid_client on public.digest_votes (paper_uid, client_id);
create index digest_votes_uid on public.digest_votes (paper_uid);

alter table public.digest_votes enable row level security;

create policy "anon_insert" on public.digest_votes
  for insert to anon with check (true);
create policy "anon_select" on public.digest_votes
  for select to anon using (true);
create policy "anon_update" on public.digest_votes
  for update to anon using (true) with check (true);
