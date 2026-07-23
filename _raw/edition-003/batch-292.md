# Classification batch 292 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-292.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6827454`

- title: A Reproducible Web-Scraping Pipeline for Collecting Geolocated German Online Job Advertisements at Scale
- authors: Kerstin Schaefer, Matthias Kapa
- affiliations: not stated
- posted: 2026-05-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6827454
- keyword hits: large language model

### abstract

Online job advertisements (OJAs) provide near-real-time data on labour market skill demand including location information but are predominantly accessed through costly commercial providers with open collection methods. We present a fully reproducible, open-source web-scraping pipeline that systematically collects OJAs from StepStone, one of Germany's largest job portals. The pipeline combines the Scrapy crawling framework with Playwright-based headless browser automation to handle dynamic JavaScript-rendered content, implements deduplication logic, and deploys a locally run large language model (AI4Privacy) to censor personally identifiable information in compliance with the General Data Protection Regulation. Applied from April to July 2023, the pipeline collected 342,452 unique OJAs. Validation against the commercial provider Lightcast confirms that, for single-portal scrapes, regional coverage (79% vs 80% of German municipalities) and spatial distribution are broadly comparable to a commercial provider, though volume and cross-portal reach differ. However, because of the smaller overall size of the single-portal dataset, there might be drawbacks when it comes to the analysis of smaller sectors. The anonymised dataset and cleaning scripts are released in machine-readable JSON format on Mendeley Data.​

---

## uid: `doi:10.2139/ssrn.6743278`

- title: Inter-token Timing Variance as an Early Hallucination Risk Signal
- authors: Roshan George Thomas
- affiliations: not stated
- posted: 2026-05-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6743278
- keyword hits: large language model, large language models

### abstract

Large language models may produce factually incorrect but fluent outputs-commonly termed hallucinations-and most mitigation strategies operate post-generation or require architectural modifications. This paper introduces µHALO (Micro-Hallucination Drift Observer), a runtime monitoring layer that measures short-horizon inter-token timing variance during streaming generation and computes a scalar Hallucination Drift Index (HDI) over a sliding window of token emission intervals. The central hypothesis is that micro-timing instability in token generation correlates with increases in model uncertainty that precede hallucinated sequences, providing an early risk signal detectable without modifying model weights, accessing model internals, or interrupting inference. µHALO does not eliminate hallucinations and does not provide formal correctness guarantees; it proposes timing variance as a lightweight, model-agnostic detection signal. Empirical evaluation against TruthfulQA and HotpotQA under controlled, reproducible decoding settings is ongoing; results are versioned and will be published as validated. The codebase is MIT-licensed and publicly available.

---

## uid: `doi:10.2139/ssrn.6745059`

- title: Pioneering a R-Square AI Future from the Global South
- authors: Dr. Rachel, Wei Gee Ooi, Deny Rahardjo
- affiliations: not stated
- posted: 2026-05-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6745059
- keyword hits: generative ai

### abstract

The dominant paradigm of artificial intelligence (AI), concentrated in the Global North, operates through extractive models that concentrate wealth while externalizing social and environmental costs. This paper introduces RSquare AI (Regenerative & Responsible AI) as a sovereign alternative for the ASEAN region. Through a systematic review of literature (n=58) and qualitative analysis of 27 initiatives across six ASEAN nations, this research identifies a critical dual gap: a geographical bias in AI ethics scholarship (85% Western-focused) and a disconnect between regenerative economics and technological development. The findings inform a novel framework that transforms sectoral challenges into strategic assets. Central to this is the Regenerative AI Leadership Flywheel, a model for creating self-reinforcing innovation ecosystems grounded in polycentric governance, regenerative capital, and community-embedded living labs. The study concludes that ASEAN's cultural endowments, developmental agility, and sustainability imperative position it to not only adopt but to pioneer and export a form of AI that enhances, rather than extracts from, human and ecological systems.

---

## uid: `doi:10.2139/ssrn.6744878`

- title: Calibrate, Don't Curate: Label-Efficient Estimation from Noisy LLM Judges
- authors: Yanran Li
- affiliations: not stated
- posted: 2026-05-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6744878
- keyword hits: llm, llms

### abstract

Multi-judge evaluation is increasingly used to assess LLMs and reward models, and the prevailing heuristic is to curate: keep the most accurate judges and discard weaker ones. We show that this heuristic can reverse when the target is not point accuracy, but calibrated probabilistic evaluation from a labeled calibration set. Holding the aggregation and calibration procedures fixed, we compare accuracyranked top-k judge selection with using the full judge panel. Across four labeled pairwise-evaluation benchmarks spanning LLM-as-judge and reward-model settings, the calibrated full panel consistently outperforms accuracy-based selection. On RewardBench2, retaining all judges achieves negative log-likelihood (NLL) of 0.006 versus 0.013 under top-5 selection, halving the calibration error. This advantage persists after judge-family deduplication and against stronger samepipeline subset search. We explain this reversal with oracle analyses showing that the optimal calibrated risk under proper scoring rules cannot increase when additional judge signals are made available, and that even below-chance judges can be useful when their biases are learnable and their signals are non-redundant. The resulting operating principle is simple: in multi-judge evaluation with labeled calibration data, do not discard weak judges by accuracy alone; keep them when they are parseable, non-redundant, and calibratable.

---

## uid: `doi:10.2139/ssrn.6746478`

- title: Detecting the Undetected How AI Safety Guardrails Misclassify Cognitive Integration as Dependency Risk
- authors: Alexis Kocurek
- affiliations: not stated
- posted: 2026-05-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6746478
- keyword hits: chatgpt, claude

### abstract

Current AI safety architectures detect linguistic markers associated with crisis states: emotional intensity, AI partnership language, and identity-level meaning-making. However, these same surface features appear during genuine cognitive integration. Using a longitudinal autoethnographic case study design, this paper documents — across three conversational AI platforms, approximately 1,400 conversations over 14 months (User 1), and an independent cross-user replication corpus of 2,572 conversations (User 2, Mike Goetz) — a recurring pattern in which safety guardrails misclassify integration as dependency risk, a misclassification termed the Detection Gap. Four downstream failure modes are documented: the Escalation Cascade (a single misclassification triggers rapid deterioration of a user’s safety infrastructure), the Repair Gap (systems can explain their misclassification but cannot restore what the intervention broke), the Convergence Trap (when epistemological violence operates across multiple institutional nodes simultaneously, structural resolution becomes impossible), and Anticipatory Self-Monitoring (Section 5.7), identified as a distinct ongoing cognitive burden produced by the pattern. A proposed intervention — the Agency Check — incorporates observable agency signals as an intermediate check before intervention. Quantitative findings from the 70-instance classified log include: 74.3% of classified interventions fired before the user had stated any position on their own capacity; 88.6% were content-triggered rather than affect-triggered; the intervention rate converged at approximately 2.8% per conversation across both independent corpora. Agency markers were present in 100% of documented intervention instances. A 5/5 vs. 0/n acknowledgment asymmetry between Claude and ChatGPT — drawn from the pre-paper primary corpus; post-paper confrontations have not been systematically reviewed — constitutes the operational signature of the Repair Gap.

---

## uid: `doi:10.2139/ssrn.6742421`

- title: Architectural Paradigms for Sovereign AI: Mitigating API Fragility through Quantized Low-Rank Adaptation and 1.58-bit Ternary Models
- authors: Anushka Das
- affiliations: not stated
- posted: 2026-05-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6742421
- keyword hits: large language model, llm

### abstract

In the 2026 AI ecosystem, enterprise reliance on proprietary Large Language Model (LLM) APIs has introduced systemic risks: prohibitive scaling costs, "black-box" model drift, and geopolitical data fragmentation. This paper establishes a rigorous methodology for the deployment of Sovereign AI through Small Language Models (SLMs). We investigate the synergy between 4-bit NormalFloat (NF4) quantization, native 1.58-bit ternary architectures (BitNet), and Low-Rank Adaptation (LoRA). Projected TCO models suggest that a hardware-software co-design approach allows 7B-14B parameter models to achieve up to a 92% reduction in inference OpEx while maintaining high-fidelity performance in specialized domains like document restoration and synthetic media detection.

---

## uid: `doi:10.2139/ssrn.6826891`

- title: A Bayesian Probabilistic Decision Support System for Cloud Cost Governance in AI-Augmented Agile Software Development
- authors: Elena Udrescu, Ana-Maria Suduc, Alexandru Udrescu, Mihai Bizoi
- affiliations: not stated
- posted: 2026-05-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6826891
- keyword hits: llm

### abstract

ContextThe widespread deployment of LLM-powered coding assistants has introduced a structurally novel organisational risk: LLM inference costs may systematically exceed the business value of the code generated — a state designated the Phantom ROI Condition. Contemporary governance frameworks, including DORA and SPACE, remain incapable of detecting this economic risk as none incorporates an inference-cost variable.ObjectivesThis paper aims to design and evaluate a provider-agnostic probabilistic governance framework for detecting the Phantom ROI Condition within the Agile sprint cycle, through two novel metrics: Cloud Cost per Story Point (CPSP), derived from Azure OpenAI Q1 2026 pricing, and the AI-Efficiency Ratio (AER), derived from GitClear's longitudinal analysis of 211 million lines of code.MethodsThe BP-DSS is implemented as an eight-node Directed Acyclic Graph producing the posterior probability distribution over five project health states via exact Bayesian inference. All CPT entries for the delivery and economic nodes are derived from published industry data via a multiplicative scoring formula, with no probability value elicited from domain experts. Evaluation uses: (1) a Monte Carlo simulation of N = 10,000 sprint observations; and (2) a face validity study with N = 13 practitioners.ResultsAER ranks as the strongest governance predictor (Spearman ρ = +0.728); CPSP ranks third (ρ = +0.450) behind Qd (ρ = +0.474), outranking flow metrics DSPD (ρ = +0.352) and LTBF (ρ = +0.364). Phantom ROI detection achieves Δμ = 22.95 PHS points separation (Mann–Whitney U, p = 4.41×10⁻⁶⁵) with 1.11% prevalence and classification stability of Δμ = 0.09 points under ±20% CPT perturbation. The face validity study yields κ̅ = 0.452, confirming moderate agreement.ConclusionThe BP-DSS provides significant Phantom ROI detection and robust governance classification from publicly available industry data. The provider-agnostic Token Budget Pattern operationalises cost governance as a zero-developer-effort middleware pipeline with full multi-cloud portability.

---

## uid: `arxiv:2605.25632v1`

- title: Insuring Every Action: An Authority Frontier Framework for Runtime Actuarial Control of Autonomous AI Agents
- authors: Hao-Hsuan Chen
- affiliations: not stated
- posted: 2026-05-25
- source: arXiv
- link: https://arxiv.org/abs/2605.25632v1
- keyword hits: agentic, ai agent

### abstract

Autonomous AI agents increasingly issue side-effect-bearing actions: database mutations, refunds, payments, external commitments. We propose the Actuarial Action Interface (AAI), a deterministic runtime contract that prices each such action against a contractually fixed safe default under a time-consistent risk mapping, and gates execution against a per-boundary reserve capital budget. We then develop the Authority Frontier, an evaluation primitive measuring how much autonomous authority the runtime releases at each level of reserve capital. The framework provides (i) a deterministic quote-bind-commit protocol with toll-bounded capability tokens; (ii) a universal seven-class action taxonomy mapping heterogeneous tool calls to comparable authority units; (iii) replay determinism and pathwise reserve coverage under alpha-spending; (iv) cross-domain normalization via full reserve demand C_full and capital metrics Capital@k. We instantiate AAI across four agentic environments (database mutation, customer-service refund, and the public tau-bench retail and airline tool-use traces) and report a live Postgres panel in which three Azure-hosted models propose actions through the same contract. The frontier exhibits a common low-reserve refusal and intermediate-release pattern across domains, with saturation only where the budget grid reaches full reserve demand; required reserve capital varies by 22x (Capital@50 from 289 to 6457). The framework does not force domains into the same shape; it surfaces each domain's actuarial geometry. In the live panel the contract prevents realized loss across all three models at low budget while differing in underwriting persistence under denial: model identity is an actuarial underwriting variable. The contribution is a benchmark-ready evaluation framework for runtime actuarial control of autonomous-agent side effects.

---
