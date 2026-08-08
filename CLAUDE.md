# Working notes

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
flat.

## Repo layout

- Root: the static personal site (hand-written HTML, shared `styles.css`,
  GitHub Pages from `main`). No Jekyll — `.nojekyll` is committed.
- `digest/`: the AI Business Research digest pipeline and its published site
  at `/digest`. See `digest/README.md` and `digest/SPEC.md`.
