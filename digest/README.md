# LLM Research Digest

A running scan of new research that uses or studies large language models in
accounting, finance, economics, and management.

**Live site:** https://jedsonn.github.io/llm-research-digest
**Feed:** `/feed.xml` · **Data:** `/data/papers.json`

## What makes this different from a paper alert

Two things.

**A second axis.** Papers are classified by field and by what the model is doing
in the paper: measuring something (instrument), being studied (object), standing
in for a human (agent), or being scrutinised (method). Field alone puts almost
everything in one bucket. Role does not.

**Three fixed lines instead of an abstract.** Every entry answers the same three
questions in the same order: what the setting is, what the model actually did and
whether it was validated, and what the result was. The middle line is the one no
abstract reports consistently, and it is why this exists.

## Where the records come from

Open metadata APIs only. Crossref for DOI records, including SSRN deposits under
prefix `10.2139` and NBER under `10.3386`. arXiv through its public API. OpenAlex
and Semantic Scholar to fill in abstracts a publisher did not deposit.

No publisher site is queried automatically and nothing is scraped. Abstracts are
used as input to write the summary lines and are never republished or committed
to this repository.

## Authors

If your paper appears here, you are welcome to send your own three lines and they
will replace whatever the pipeline generated, labelled as yours. You can also ask
for a correction or for the entry to be removed. Open an issue or email the
address on the site.

## Running it

See `SPEC.md` for the full build and the routine prompt.

```bash
pip install -r requirements.txt
python3 scripts/harvest.py  --edition 1 --date $(date -u +%F)
python3 scripts/enrich.py   --edition 1
python3 scripts/classify.py prepare --edition 1 --batch-size 8
#   a model reads data/runs/edition-001/batch-K.md and writes batch-K.answer.json
python3 scripts/classify.py apply --edition 1
python3 scripts/dedupe.py   --edition 1
python3 scripts/build_site.py --edition 1 --date $(date -u +%F)
```

## Licence

Code MIT. The curated classifications and summary lines CC BY 4.0. Bibliographic
metadata belongs to its originating source under that source's terms.

## Disclaimer

Independent. Not affiliated with, sponsored by, or endorsed by SSRN, Elsevier,
arXiv, or any publisher listed.
