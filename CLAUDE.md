# Working notes

## Installed skills and when each applies

Skills live in `.claude/skills/` and load in every session on this repo.

- **ponytail** (+ `-review`, `-audit`, `-debt`, `-gain`, `-help`) — lazy senior
  dev discipline: YAGNI, stdlib before dependencies, one line before fifty.
  Apply to any coding task here: pipeline scripts, workflows, site JS. This
  repo's code is deliberately small and dependency-light; keep it that way.
  Skills only — the upstream plugin's session hooks are NOT installed.
- **design-taste-frontend** — anti-slop frontend design for landing pages,
  portfolios, and redesigns. Apply to the personal site's pages. Do NOT apply
  it to `/digest`: that is a dense data listing with an established design
  system (`styles.css`), and the skill itself excludes dashboards and data
  tables. When building a Claude Artifact, `artifact-design` governs; this
  skill may inform the visual direction inside it, never override it.
- **writing-clearly-and-concisely** — Strunk's Elements of Style rules for
  prose a HUMAN reads: site copy, digest paper bullets, LinkedIn posts,
  README and doc text, commit messages.
- **asd-ste100** — Simplified Technical English for text a MACHINE parses,
  see below.

The two writing skills split by reader, and the split is the whole point.
Human reader → Strunk. Agent, tool, or pipeline reader → STE. When a string
has both audiences (an error message a user reads and a script greps),
write it under STE and then check it reads naturally aloud.

## Writing style for agent-facing text

The **asd-ste100** skill (`.claude/skills/asd-ste100/`) is installed in this repo.
Apply Simplified Technical English whenever writing text that another agent, a
tool, or an automated pipeline has to parse without a human to resolve
ambiguity: tool descriptions, error messages, system prompts, routine prompts,
inter-session handoff messages, and workflow/agent instructions.

Rules in short: one meaning per word, active voice, simple tenses, one
instruction per sentence, no dropped words, short sentences. Invoke the skill
by name for a full before/after rewrite with rule citations.

Do NOT apply STE to human-facing prose — site copy, the digest's paper bullets,
LinkedIn posts, teaching-case cards. Voice matters there; STE is deliberately
flat. Use `writing-clearly-and-concisely` for those instead.

## Repo layout

- Root: the static personal site (hand-written HTML, shared `styles.css`,
  GitHub Pages from `main`). No Jekyll — `.nojekyll` is committed.
- `digest/`: the AI Business Research digest pipeline and its published site
  at `/digest`. See `digest/README.md` and `digest/SPEC.md`.
