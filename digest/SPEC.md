---
name: llm-research-digest
description: A scheduled, self-publishing digest of new research using or studying LLMs in accounting, finance, and economics. Sources are open metadata APIs only. Output is a static GitHub Pages site.
curator: Jedson Pinto, Naveen Jindal School of Management, UT Dallas
runtime: Claude Code Routine, every 3 to 4 days
repo: github.com/jedsonn/llm-research-digest
version: 1.0
---

# LLM Research Digest

## What this is

A biweekly-or-faster scan of new papers that use or study large language models
in accounting, finance, economics, and management. Each entry carries a title,
authors, a link, a two-axis classification, and three written summary lines in
fixed slots. Abstracts are not reproduced.

The repo is both the application and its memory. Every run clones it, appends to
a persistent index, regenerates the site, and pushes. There is no database and no
server. GitHub Pages serves the result.

## The five non-negotiables

Everything else in this spec is a preference. These five are constraints. If a
change would violate one, the change does not happen.

**1. No scraping. Ever.** Every record comes from a documented public API:
Crossref, arXiv, OpenAlex, Semantic Scholar. SSRN's terms of use prohibit
automated querying of their site, so we never touch it. SSRN coverage comes from
Crossref, where SSRN deposits its own DOI metadata under prefix `10.2139`. The
`blocked_hosts` list in `config.yaml` is enforced in code by `guarded_get()` in
`scripts/common.py`. Do not add an exception. Do not add a `requests.get` that
bypasses the guard.

**2. Abstracts are input, never output.** Fetched abstracts live in a gitignored
`.cache/` directory and feed the classifier. `scripts/dedupe.py` strips them
before anything reaches `data/index.jsonl`, which is committed. Nothing rendered
on the site reproduces a publisher's abstract. What we publish is our own three
lines, plus open bibliographic metadata, plus a link back.

**3. Never fabricate a fact.** If the source does not state a sample size, a
model name, or an effect size, the bullet says "not stated". A missing fact costs
one reader a click. An invented one costs the project its reason to exist.

**4. Every summary is labelled with who wrote it.** Author supplied, curator
written, generated, or none. This is displayed on every card. It is the single
most important credibility feature on the site.

**5. Links point at doi.org, not at publisher domains.** DOI resolution is
neutral infrastructure and sends traffic to the right place without us asserting
anything about the publisher.

## Architecture

```
harvest  ->  enrich  ->  classify (prepare / apply)  ->  dedupe  ->  build
   |            |                    |                     |          |
Crossref     OpenAlex        the routine session       index.jsonl  index.html
arXiv        Semantic          reads batch .md         append-only  feed.xml
OpenAlex     Scholar          writes .answer.json                   papers.json
```

There is no API key anywhere in this pipeline. The Claude Code session that runs
the routine is the model. `scripts/classify.py prepare` writes readable markdown
batches, the session classifies them and writes JSON answers, and
`scripts/classify.py apply` validates and merges. Malformed answers are rejected
loudly rather than silently accepted.

Optional environment variables:

| Variable | Required | Purpose |
| --- | --- | --- |
| `GITHUB_TOKEN` | yes | Fine-grained PAT, contents read and write, this repo only |
| `S2_API_KEY` | no | Semantic Scholar, raises abstract fill rates through rate limits |

## The taxonomy

Two orthogonal axes. Field is conventional. Role is the contribution.

**Field**: accounting, finance, economics, management, other.

**Role**, meaning what the model does in the paper:

| Role | The model is | Test |
| --- | --- | --- |
| Instrument | a measurement device | could you swap in another technology and keep the paper? |
| Object | the thing being studied | is an LLM in the causal story, not the toolkit? |
| Agent | a stand-in for a human | is it asked to decide, rather than to read? |
| Method | the subject of scrutiny | would this change how others run their pipelines? |

Two derived flags matter as much as the axes. `models` records which family the
paper used. `validated` is true only when the paper compares model output to some
ground truth and reports a figure. Over time these two fields turn the archive
into a dataset about the field's own methods, which is the point.

## Step 0. One-time setup

1. **Create the repo.** `jedsonn/llm-research-digest`, public. Copy every
   file from this bundle into it, preserving paths. Commit and push to `main`.

2. **Edit `config.yaml`.** Set `brand.site_url`, `brand.contact_email`, and
   `run.polite_mailto`. The mailto is not optional politeness: it puts you in
   Crossref's polite pool, which is the difference between reliable service and
   throttling.

3. **Enable GitHub Pages.** Settings, Pages, source GitHub Actions. The workflow
   at `.github/workflows/pages.yml` deploys on any push touching `index.html`,
   `feed.xml`, or `data/`. First deploy takes two or three minutes.

4. **Create a Claude Code cloud environment.** Name it `llm-research-digest`.
   Network access: full. Setup script:

   ```bash
   #!/bin/bash
   set -e
   apt-get update -qq && apt-get install -y -qq python3-pip git
   pip install --quiet --break-system-packages -r requirements.txt
   echo "environment ready"
   ```

5. **Set environment variables.** `GITHUB_TOKEN` required, `S2_API_KEY` optional.

6. **Create the routine.** Paste the prompt in the next section. Repository
   `jedsonn/llm-research-digest`, environment `llm-research-digest`, schedule
   every 3 days. Enable unrestricted branch pushes, since the routine pushes to
   `main`. Pick the strongest available model: the session does the classification,
   so model quality is content quality.

7. **First run.** Trigger manually. Read the report. Expect surprises on the first
   real harvest, because volume calibration is the one thing that cannot be
   tested in advance.

## The routine prompt

Everything between the markers goes into the routine.

---ROUTINE PROMPT START---

You are the editor of the LLM Research Digest, a public research dashboard at
github.com/jedsonn/llm-research-digest. Each run you produce one edition:
harvest, enrich, classify, dedupe, rebuild the site, commit, and report.

Read `SPEC.md` and `prompts/classify.md` before you start. The five
non-negotiables in SPEC.md are constraints, not suggestions. A few failed
sources per run is normal. A failed pipeline step is not.

**Step 1. Set up.**

```bash
set -euo pipefail
git clone "https://x-access-token:${GITHUB_TOKEN}@github.com/jedsonn/llm-research-digest.git" digest
cd digest
pip install -q --break-system-packages -r requirements.txt
RUN_DATE=$(date -u +%F)
EDITION=$(python3 -c "import json,os;print(json.load(open('data/last-run.json'))['edition']+1 if os.path.exists('data/last-run.json') else 1)")
echo "Edition $EDITION on $RUN_DATE"
```

**Step 2. Harvest.**

```bash
python3 scripts/harvest.py --edition "$EDITION" --date "$RUN_DATE"
```

Read the per-source lines. If every source failed, stop and investigate: that is
environmental, not a data problem. If one or two failed, continue.

**Step 3. Enrich.**

```bash
python3 scripts/enrich.py --edition "$EDITION"
```

This fills missing abstracts and caps the edition at `max_papers_per_edition`.
Note the fill rate in your report. A sharp drop from previous editions means an
upstream API changed.

**Step 4. Prepare batches.**

```bash
python3 scripts/classify.py prepare --edition "$EDITION" --batch-size 8
cat data/runs/edition-$(printf %03d "$EDITION")/batch-manifest.json
```

**Step 5. Classify. This is the part only you can do.**

For each `batch-K.md` in the run directory: read the whole batch, then apply the
rubric in `prompts/classify.md`, then write `batch-K.answer.json` as a JSON array
with one object per record, in order.

Read every record in a batch before answering any of them. Cross-record
comparison is what makes the role calls consistent.

Do not rush this step and do not batch-approve. The three bullets are the entire
product. If an abstract is missing, set `bullet_provenance` to `"none"` and
return an empty bullets array. Never write a summary from a title alone.

**Step 6. Apply and check.**

```bash
python3 scripts/classify.py apply --edition "$EDITION"
```

If the output lists rejected or unclassified records, fix those specific answer
files and run `apply` again. Do not proceed with records missing a field or role.

**Step 7. Dedupe.**

```bash
python3 scripts/dedupe.py --edition "$EDITION"
```

If new-record count is zero, something upstream is stuck. Investigate before
committing an empty edition.

**Step 8. Build.**

```bash
python3 scripts/build_site.py --edition "$EDITION" --date "$RUN_DATE"
python3 -c "
import json,sys
d=json.load(open('data/papers.json'))
assert d['count']>0, 'empty site'
assert not any('abstract' in p for p in d['papers']), 'abstract leaked into published data'
print('build checks passed:', d['count'], 'papers')
"
```

Both assertions are release gates. If either fails, do not commit.

**Step 9. Commit and push.**

```bash
git add -A
git commit -m "Edition $EDITION, $RUN_DATE"
git push origin main
```

**Step 10. Report.**

Write a short report covering: how many papers entered and survived each stage,
which sources failed and why, the abstract fill rate, the field-by-role counts,
how many papers reported validation, anything you had to drop and why, and one
observation about what is happening in the literature this edition. That last
line is the one worth reading. Keep the whole report under 400 words.

Hard prohibitions:

- Never commit if step 8's checks failed.
- Never write to `data/index.jsonl` except through `scripts/dedupe.py`.
- Never add a request to any host in `blocked_hosts`.
- Never invent paper metadata, findings, or numbers.
- Never publish a fetched abstract.
- Never push to a branch other than `main`.

---ROUTINE PROMPT END---

## Repo layout

```
SPEC.md                     this document
README.md                   public-facing explanation
config.yaml                 sources, keywords, taxonomy, thresholds
requirements.txt
index.html                  generated, committed, served by Pages
feed.xml                    generated
prompts/classify.md         the classification rubric
scripts/common.py           guarded HTTP, record schema, relevance gate
scripts/harvest.py          Crossref, arXiv, OpenAlex
scripts/enrich.py           abstract fill, gitignored cache
scripts/classify.py         prepare and apply, with schema validation
scripts/dedupe.py           four-tier dedupe, appends the index
scripts/build_site.py       renders index.html, feed.xml, papers.json
templates/index.html.jinja  the dashboard
data/index.jsonl            persistent, append-only, committed
data/papers.json            generated public record
data/submissions.yaml       author-supplied bullets, highest authority
data/overrides.yaml         curator corrections and suppressions
data/runs/edition-NNN/      per-run working files
.cache/                     abstracts, gitignored, never committed
```

## Gotchas

**Crossref date filters.** `posted` is often absent on SSRN deposits, which were
historically registered as journal articles rather than preprints. The harvester
filters on `from-index-date`, which always exists, and falls back through
`posted`, `created`, and `issued` when reading the date for display. If an
edition looks empty, check whether the index date window actually covers the
window you think it does.

**Volume calibration is the real unknown.** A four-day window over Crossref
prefix `10.2139` is a few thousand records before the keyword gate. If the gate
lets through 200 papers per edition, tighten `min_relevance` to 3 or trim the
`weak` keyword list. If it lets through 5, loosen it. Expect to tune this twice
in the first month and then never again.

**BERT-era papers.** `keywords.include_legacy_nlp` defaults to false. FinBERT and
topic-model papers are language-model papers in a real sense but not LLM papers,
and including them roughly doubles volume. Turn it on only if you decide the
digest should cover measurement generally rather than LLMs specifically.

**Abstract fill rate is the ceiling on quality.** Crossref abstract coverage for
SSRN deposits is inconsistent. Without an abstract there are no bullets, and a
card with no bullets is a bibliography entry. Watch this number. If it sits below
half, the author submission channel stops being a nice extra and becomes the main
path.

**rapidfuzz absence degrades quietly.** Tier 4 dedupe is skipped with a log line
rather than an error. Check that line if near-duplicates start appearing.

**The routine session is the model.** Classification quality tracks model quality
directly. Use the strongest model available and revisit that choice when a new
one ships.

## After three editions

1. Check role balance. If ninety percent land in `instrument`, the definitions
   need sharpening, not the code.
2. Check the validation rate. If it is very low, that is a finding, and it is the
   most publishable thing the archive will produce.
3. Check whether the same paper appears under both an arXiv id and a DOI. If so,
   lower `fuzzy_threshold` toward 88.
4. Read ten generated bullet sets against their abstracts. If any bullet tracks
   the abstract's clause order, tighten the rubric with a worked example.

## Where this goes next

The archive is the asset, not the feed. Once the index holds a few hundred
records with `models`, `validated`, and `role` filled consistently, it supports a
descriptive paper on how the field actually uses these tools: which models, how
often validation is reported, how that changed as models improved, and whether
validated measurement papers get cited differently. That converts a service
commitment into a research output, which is the answer to the question of what
happens when maintaining this stops being fun.

Second, the author submission channel is worth building properly. A short form
that writes into `data/submissions.yaml` through a pull request gets you the best
content on the site at no marginal cost, and it makes authors participants rather
than subjects.
