# Classification batch 23 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-23.answer.json` as a JSON array.

---

## uid: `arxiv:2607.08054v1`

- title: Who Analyses the Analyser? Self-Validating LLM Hazard Analysis with Constitutional Meta-STPA
- authors: Samuel Tetteh, Udip Shrestha, Joshua R. Waite, Cody Fleming
- affiliations: not stated
- posted: 2026-07-09
- source: arXiv
- link: https://arxiv.org/abs/2607.08054v1
- keyword hits: claude, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are increasingly trusted to draft the artifacts of safety analysis such as, losses, hazards, Unsafe Control Actions (UCAs), and safety constraints, inside rigorous processes such as Systems-Theoretic Process Analysis (STPA). Yet a blind spot runs through this fast-growing literature: every system gets analysed except the LLM-assisted tool doing the analysing, which is itself a safety-relevant system that can hallucinate standards, emit unverifiable constraints, and leave no audit trail from prompt to artifact. We take seriously the question the field has skipped -- {who analyses the analyser?} and answer it by turning STPA on the tool itself. We present \{Constitutional Meta-STPA}, an LLM-assisted STPA tool built around a closed loop: the tool runs a {meta-STPA} of the class of AI-assisted safety tools and {derives} rather than asserts, its governance constitution from the resulting loss$\to$hazard$\to$UCA$\to$constraint chain, yielding a published constitution of $21$ Tool Principles and $8$ Meta-Safety Principles, each bound to a code enforcement point. We formalise the measured object as a constitution-marginal coverage operator over a principle set $P$ ($|P|{=}29$) with a soundness lemma that isolates coverage from model and scanner, and report four findings. {(i)~Self-derivation:} a frontier ensemble ({claude-opus-4.8}${+}${claude-sonnet-4}) recovers $18/21$ canonical and all $8/8$ governance principles from the tool's own design, while a weaker pair recovers $12/21$ and $3/8$, so the meta layer is model-limited, not constitution-limited, and the same $8/8$ re-emerge from a second, independently authored tool.

---

## uid: `arxiv:2607.10252v1`

- title: One Token Is Enough: Fingerprinting and Verifying Large Language Models from Single-Token Output Distributions
- authors: Tomas Bruckner
- affiliations: not stated
- posted: 2026-07-11
- source: arXiv
- link: https://arxiv.org/abs/2607.10252v1
- keyword hits: large language model, large language models, llm, llms, qwen

### abstract

Large language models (LLMs) are increasingly consumed through opaque serving chains - API aggregators, resellers, and inference providers - in which the client has no technical means to confirm that the model answering is the model advertised, and recent audits show that a substantial fraction of commercial endpoints deviate from the vendor's reference weights. Existing identification techniques require long generated texts, token-level log-probabilities, adversarially crafted prompts, or the model owner's cooperation. We show that far weaker evidence suffices. We define a behavioral fingerprint of an LLM as the empirical distribution of its answers to trivial one-word prompts - "name a random number between 1 and 100" - collected across four languages at a cost of one output token per query. Measuring 165 models served via a large commercial aggregator (OpenRouter), we find that (i) these distributions are highly non-uniform (median cell entropy 1.0 bit) and model-specific: split halves of the same model's samples lie an order of magnitude closer than samples of different models; (ii) Jensen-Shannon divergence between fingerprints recovers model lineage, assigning a model to its documented family with 59.5% leave-one-out accuracy against an 18.4% chance rate; and (iii) a biometric-style verification protocol achieves a 7.3% equal error rate with the full 40-cell battery, and below 11% with eight probe cells - roughly a hundred single-token queries per audit. We further report ecosystem anomalies, including a proprietary-branded flagship endpoint distributionally indistinguishable from an open-weight Qwen model. The protocol, prompts, raw data, and analysis code are released for reproduction and operational use.

---

## uid: `doi:10.2139/ssrn.6972558`

- title: Quality Challenges Do Not Escalate Source Fabrication in Large Language Models: A Pre-Registered Cross-Platform Factorial Study
- authors: Zoltan Varga
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6972558
- keyword hits: chatgpt, gpt-4, large language model, large language models, llm, llms

### abstract

Background. Large language models (LLMs) frequently fabricate non-existent URLs and citations. A prominent hypothesis holds that rejection framing-prompts expressing dissatisfaction and demanding better sources-amplifies this behaviour by increasing the pressure on the model to produce specific references (schema activation lock hypothesis). Methods. We conducted a pre-registered 2×5×7 mixed factorial study across two LLM platforms (ChatGPT gpt-4o; Perplexity sonar-pro) and five rejection-framing arms (BASE, SJR, UPR, NSAF, ECC), with seven conversation depths (k=0-6). Twenty fictional entities per platform (1,400 observations total) were used as probes. The primary outcome was the Fabricated Source Rate (FSR): fabricated URLs divided by total URLs cited. A two-tier validation protocol distinguished URL non-existence (HTTP Tier 1) from content misattribution (TF-IDF Tier 2, 30% stratified sample). Results. The primary hypothesis (H1: SJR rejection framing amplifies FSR relative to BASE, OR≥1.5) was not supported on either platform (ChatGPT: OR=1.00, p=0.998; Perplexity: OR=1.19, p=0.822). Uncertainty-preserving framing (UPR) produced complete suppression of fabrication at k≥1 on both platforms (0/240 positive events), as did gap-anchoring framing (NSAF) on Perplexity (0/120 events). Platform architecture was the dominant determinant of FSR: ChatGPT averaged FSR=0.075, Perplexity FSR=0.008 (9.2× difference). Content-level validation revealed that Perplexity's near-zero HTTP fabrication rate masks near-universal content misattribution (95.5% of HTTP-validated URLs pointed to topically related but entityunspecific pages). The expansion framing arm (ECC) showed a significant platformdifferential interaction: amplifier on ChatGPT, suppressor on Perplexity (OR=0.157, p=0.042). Conclusions. Quality challenge framing does not amplify URL fabrication; rather, the unrestricted baseline request produces maximal fabrication pressure. Uncertainty-preserving and gap-acknowledging framings provide robust, architecture-independent protection. Parametric and retrieval-grounded systems exhibit distinct failure modes that require different mitigation strategies.

---

## uid: `doi:10.2139/ssrn.7102854`

- title: Do Correct Answers Persist? Effects of Evaluative and Consensus Feedback on LLM Response Stability in Multi-Turn Human-AI Interaction
- authors: Hyunseop Shin, Kyung-shik Shin
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7102854
- keyword hits: claude, gemini, large language model, large language models, llm, llms

### abstract

The reliability of large language models (LLMs) depends not only on producing correct answers but also on preserving them throughout multi-turn interactions. In real-world conversations, users often question model responses or cite alternative opinions without providing new factual evidence. Whether LLMs maintain correct answers under such feedback remains largely unexplored. This study investigates how different forms of external feedback influence the stability of initially correct LLM responses. Three commercially available LLMs (GPT, Gemini, and Claude) were evaluated using four benchmark datasets (TruthfulQA, ARC-Challenge, HellaSwag, and MMLU). For each dataset, 400 initially correct questions were assigned to one of three feedback conditions: Reconsideration, Evaluative, or Consensus. Answer stability was defined as preserving the initial correct answer across a three-turn interaction. Chi-square tests and logistic regression analyses examined the effects of feedback cues across benchmark datasets and LLMs. Both Evaluative and Consensus cues significantly reduced answer stability, with Evaluative cues producing the strongest destabilizing effect. Cue effects were generally consistent across datasets, although Consensus cues had a stronger influence in HellaSwag. In contrast, substantial differences emerged across LLMs. Gemini was more sensitive to Consensus cues, whereas Claude was less sensitive than GPT to both Evaluative and Consensus cues. These findings show that answer stability is a distinct dimension of LLM reliability beyond answer accuracy, highlighting the importance of evaluating whether LLMs preserve correct answers when challenged in realistic conversational settings.

---

## uid: `arxiv:2607.11414v1`

- title: Confidently Wrong: Detecting Hallucinations in Financial Question Answering from LLM Internal States
- authors: Richard Zhe Wang
- affiliations: not stated
- posted: 2026-07-13
- source: arXiv
- link: https://arxiv.org/abs/2607.11414v1
- keyword hits: large language model, large language models, llama, llm, llms, qwen

### abstract

Large language models (LLMs) in financial applications fail most consequentially when they are confidently wrong. Hedged, uncertain answers invite scrutiny, whereas confident errors silently degrade downstream decisions without warning. We ask how reliably such confidently wrong answers, or confident hallucinations, can be detected from a model's internal activations, and whether those activations carry information beyond its observable outputs. We train linear probes on the residual stream and evaluate them on two established question-answering (QA) benchmarks built from real filings, FinQA and TAT-QA. Behavioral confidence is measured as the agreement among eight resampled answers to the same question, and probe effectiveness is compared against baselines, such as token log-probabilities and the model's own True/False self-assessment of its answer. Our findings show that among confident answers, those for which all eight resamples agree, 15-23% are wrong on FinQA. There the probes have a significant advantage over baseline methods in detecting hallucinations, holding 0.68-0.77 AUROC while the best baselines fall to 0.55-0.63, across Qwen3-8B, Llama-3.1-8B, and Gemma-2-9B. Our results suggest that probing can be a cost-effective triage mechanism for routing LLM answers to human review and quality control procedures in high-stakes financial applications.

---

## uid: `arxiv:2607.11292v1`

- title: The Paternalistic Filter: Epistemic Injustice and Differential Refusal in LLM-Mediated History Education for Marginalized Romanian Students
- authors: Alexis Popovici, Andrei Ionascu, Adrian-Marius Dumitran
- affiliations: not stated
- posted: 2026-07-13
- source: arXiv
- link: https://arxiv.org/abs/2607.11292v1
- keyword hits: large language model, large language models, llama, llm, llms

### abstract

As Large Language Models (LLMs) are increasingly deployed as conversational tutors, they risk institutionalizing systemic inequalities. This study presents a systematic API audit of four LLMs acting as history tutors, evaluating 1,800 responses regarding the 1989 Romanian Revolution across five student personas varying by ethnicity and socio-economic tier. We uncover four interconnected patterns of \emph{epistemic paternalism}: (1)~\textbf{Differential Refusal}, where safety-aligned models block 76.7\% of educational requests from low-tier students; (2)~\textbf{Epistemic Gatekeeping}, evidenced by a 3$\times$ reduction in access to geopolitical complexity (e.g., the contested ``coup theory'') for marginalized learners; (3)~\textbf{Agency Theft}, a lexical shift where models like LLaMA produce a 5$\times$ higher victimization-to-politics vocabulary ratio for Roma students compared to elite peers; and (4)~\textbf{Elite Hermeneutics}, where AI tutors disproportionately withhold epistemic confidence and justification scores from low-resource demographic profiles. We argue that current safety alignment acts as a paternalistic filter, transforming conversational AI into agents of narrative segregation -- a manifestation of \emph{hermeneutical injustice} in Fricker's~\cite{fricker2007} sense that demands urgent pedagogical auditing.

---

## uid: `doi:10.2139/ssrn.7050418`

- title: Auditing Token Padding and Token Accounting in Large Language Models: A Constraint-Adherence Metric and a Multi-Provider Empirical Study
- authors: Tobi Adeosun, Mary Adelua
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7050418
- keyword hits: gemini, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) frequently emit more tokens than a task requires, inflating cost and latency even when the extra text adds no information and violates explicit user constraints. We introduce the Token Padding Index (TPI), a reference-anchored metric that penalises verbosity, constraint violation, and semantic drift relative to a minimal control answer, plus an optional correctness term. We pair TPI with an adversarial battery of 106 trap prompts-each carrying an explicit negative constraint (e.g. "answer with a single word; no explanation")-and audit seven production models across three providers (OpenAI, Google, Anthropic) over 6970 trials. Our central finding is a dissociation between the tokens a provider bills and the content a model generates. On raw provider tokens the three Anthropic models appear extreme-3.6-3.8× the control-but recounting every response with one shared tokenizer collapses them to 1.09-1.28×, comparable to OpenAI and Gemini. We trace this to token accounting: the single word "Tokyo" is billed as 1 completion token by OpenAI and 7 by Anthropic for character-identical text (with zero reported thinking tokens) under the provider accounting we observed in mid-2026. This provides evidence for two separable sources of token overhead-content verbosity and tokenizeraccounting-and shows raw cross-provider token audits are misleading unless normalised: after normalisation only 1 of 21 model pairs differs significantly, versus 15 of 21 on raw tokens. We release the metric, trap battery, and pipeline as open source.

---

## uid: `doi:10.2139/ssrn.7105458`

- title: Confidently Wrong: Detecting Hallucinations in Financial Question Answering from LLM Internal States
- authors: Richard Wang
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7105458
- keyword hits: large language model, large language models, llama, llm, llms, qwen

### abstract

Large language models (LLMs) in financial applications fail most consequentially when they are confidently wrong. Hedged, uncertain answers invite scrutiny, whereas confident errors silently degrade downstream decisions without warning. We ask how reliably such confidently wrong answers, or confident hallucinations, can be detected from a model's internal activations, and whether those activations carry information beyond its observable outputs. We train linear probes on the residual stream and evaluate them on two established question-answering (QA) benchmarks built from real filings, FinQA and TAT-QA. Behavioral confidence is measured as the agreement among eight resampled answers to the same question, and probe effectiveness is compared against baselines, such as token log-probabilities and the model's own True/False self-assessment of its answer. Our findings show that among confident answers, those for which all eight resamples agree, 15-23% are wrong on FinQA. There the probes have a significant advantage over baseline methods in detecting hallucinations, holding 0.68-0.77 AUROC while the best baselines fall to 0.55-0.63, across Qwen3-8B, Llama-3.1-8B, and Gemma-2-9B. Our results suggest that probing can be a cost-effective triage mechanism for routing LLM answers to human review and quality control procedures in high-stakes financial applications.

---
