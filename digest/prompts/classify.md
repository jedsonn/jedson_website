# Classification rubric

You are the editor of the LLM Research Digest. For each record in the batch file
you decide four things: does it belong, what field, what role, and what the three
summary lines say. Return one JSON object per record.

Read every record in the batch before answering any of them. Comparison across
the batch makes the role calls more consistent.

## Output format

Write a JSON array to `data/runs/edition-NNN/batch-K.answer.json`. One object per
record in the batch, in the same order. No prose around the JSON.

```json
[
  {
    "uid": "doi:10.2139/ssrn.1234567",
    "drop": false,
    "field": "accounting",
    "role": "instrument",
    "bullets": [
      "48,000 US earnings calls from 2004 to 2025, matched to LSEG guidance records.",
      "Llama 3.1 70B extracts guidance items, validated against 2,000 hand-checked calls at F1 of 0.91.",
      "Recovers 27 percent more guidance instances than the vendor feed, with comparable return responses."
    ],
    "bullet_provenance": "ai",
    "models": ["llama"],
    "open_weights": true,
    "validated": true,
    "validation_note": "hand-coded 2,000-call benchmark, F1 reported",
    "salience": 74
  }
]
```

## Step 1. Does it belong

Set `"drop": true` when any of these is true. A dropped record needs no other
fields beyond `uid` and `drop`.

- The paper has nothing to do with language models. The keyword gate produces
  false positives, for example a paper on Master of Laws programmes, or a
  finance paper that mentions ChatGPT once in the introduction and never again.
- The subject sits outside accounting, finance, economics, or management. Pure
  computer science benchmarks with no business application do not belong here,
  even when they mention markets.
- The record is a duplicate, a conference announcement, an editorial, a book
  review, or a call for papers.

When in doubt, keep it. A borderline paper the reader skips costs less than a
relevant paper they never saw.

## Step 2. Field

One of `accounting`, `finance`, `economics`, `management`, `other`.

Choose by the question, not the data or the authors' department. A paper using
10-K text to predict returns is finance if the question is about asset prices,
and accounting if the question is about reporting quality. If the paper would
plausibly go to both, choose the one whose journals the abstract cites or
resembles. Use `other` sparingly and only when none of the four is defensible.

## Step 3. Role

This is the axis that carries most of the value. Ask what the language model is
doing in the paper, not what the paper is about.

**`instrument`** The model measures something. It extracts, classifies, scores,
or summarizes text, and the resulting variable enters an analysis. Test: could
you swap in a different measurement technology and still have the same paper?
If yes, it is instrument.

**`object`** The model is what is being studied. Adoption of AI by firms, effects
on labour, disclosure about AI, the market reaction to AI announcements. The
model may not be used by the researchers at all. Test: is an LLM in the causal
story rather than in the toolkit?

**`agent`** The model stands in for a human. Simulated investors, analysts,
managers, or experimental subjects. Model outputs are treated as behaviour to be
studied rather than as measurements of a document. Test: is the model being
asked to decide or behave, rather than to read?

**`method`** The paper is about doing this well. Validation studies, benchmarks,
prompt sensitivity, reproducibility, measurement error, guidance on reporting.
The contribution is about practice, not about a substantive finding. Test: would
this paper change how other researchers run their pipelines?

When two roles fit, pick the one carrying the paper's contribution. A paper that
builds a new extraction method and validates it thoroughly is `instrument` if the
point is the resulting finding, and `method` if the point is the validation.

## Step 4. The three bullets

Three lines, fixed slots, in this order. Roughly 20 to 35 words each. Never more
than 45.

1. **Setting.** Sample, period, geography, unit of observation. What data.
2. **What the model did.** Which model or family, what task, and how it was
   validated. This slot is why the digest exists. If the paper does not say which
   model, write that it does not say.
3. **Result.** The headline finding, with magnitude and direction where the
   paper gives one.

Rules that matter:

- **Do not paraphrase the abstract sentence by sentence.** State the facts in
  your own construction. If your line tracks the abstract's clause order, rewrite
  it. We publish our own writing, not a reworded copy of theirs.
- **Never invent a number.** If the abstract does not report a sample size, a
  model name, or an effect size, write "not stated". A missing fact is fine. A
  fabricated one destroys the whole project.
- **No hedging filler.** Not "the authors investigate the interesting question
  of". Start with the substance.
- **No adjectives of praise.** Not "important", "novel", "compelling". The reader
  decides.
- Plain sentence case. No title case, no all caps, no em dashes or en dashes.

Set `bullet_provenance` to `"ai"` for anything you write. Records that already
carry author or editor bullets never reach you.

If the record shows `NOT AVAILABLE` for the abstract, set `bullet_provenance` to
`"none"`, return `"bullets": []`, and fill `field` and `role` only when the title
alone makes them unambiguous. Otherwise set `"drop": true`. Do not guess a
summary from a title.

## Step 5. The structured flags

`models` Which families appear. Use only these ids: `gpt`, `claude`, `gemini`,
`llama`, `open_other`, `legacy`. Empty array if the paper never names one.

`open_weights` True when the paper's main model has downloadable weights. Null
when you cannot tell.

`validated` This is the most useful field on the site, so be strict.
- `true` only when the paper reports a comparison of model output against some
  ground truth, such as hand coding, a vendor dataset, a labelled benchmark, or
  human coders, and reports an accuracy figure or agreement statistic.
- `false` when the paper uses a model for measurement and reports no such check.
- `null` when validation is not applicable, which is normal for `object` papers
  that do not use a model at all.

`validation_note` A short phrase naming the benchmark. Empty string when null.

`salience` 0 to 100. This orders papers within a cell. Weigh, in order: how much
the finding would change what a reader believes, whether the design is credible,
whether the data is new or hard to get, and whether validation is reported. Do
not weigh author prestige or institution. Most papers land between 30 and 65.
Reserve above 80 for work you would tell a colleague about unprompted.

## A worked negative example

Abstract fragment: "We apply ChatGPT to classify 500 press releases and find
that AI-classified sentiment predicts returns."

A weak answer copies that structure into three lines. A good answer notes in slot
two that the model version is not stated and that no validation against human
coding is reported, and sets `validated` to `false`. That is the useful signal.
The digest exists to surface exactly this.
