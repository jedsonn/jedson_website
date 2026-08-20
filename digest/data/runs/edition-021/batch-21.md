# Classification batch 21 of 22, edition 21

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-021/batch-21.answer.json` as a JSON array.

---

## uid: `arxiv:2608.17624v1`

- title: Governing Delegation to Generative Artificial Intelligence: Human Direction, Work-Related Orientation, and Modes of Use
- authors: Jorge Fábrega
- affiliations: not stated
- posted: 2026-08-18
- source: arXiv
- link: https://arxiv.org/abs/2608.17624v1
- keyword hits: claude, generative artificial intelligence

### abstract

Delegating cognitive operations to generative artificial intelligence redistributes execution and raises a governance problem: where human direction of the task remains. We distinguish two routes. Specified delegation places that direction before execution, through instructions, constraints, or criteria that delimit the task. Iterative coproduction places it during production, through interventions that correct or redirect provisional outputs. To examine both routes, we use aggregate monthly cells from the Anthropic Economic Index for April and May 2026. The AEI distinguishes two modes of use: 1P API, which corresponds to direct traffic through Anthropic's API, and Claude.ai, which combines activity from Chat and Cowork. On this basis, we test whether a stronger work-related orientation of human-AI interaction is associated with more specified delegation within each mode and whether the increase in the iterative profile is greater in Claude.ai than in 1P API. The main analysis uses level-0 O*NET tasks and estimates how both profiles change when an eligible record reallocates ten percentage points from personal use to work-related use. The iterative comparison is restricted to 1,411 node-month pairs observed and eligible in both modes. Specified delegation increases by 2.76 points in 1P API (95% CI: [2.30, 3.22]) and by 1.45 in Claude.ai (95% CI: [0.93, 1.97]). On the common support, iterative coproduction changes by-0.30 points in 1P API and by 0.15 in Claude.ai, yielding a between-mode difference of 0.45 points (95% CI: [0.15, 0.75]). These findings show that work-related orien tation is associated with stronger traces of prior human direction and that the observable iterative response varies across modes of use. The article shifts attention from how much the AI executes to when human direction leaves observable traces.

---

## uid: `arxiv:2608.18336v1`

- title: Measuring the Partial-Credit Gap: A Strict Benchmark on Vietnam's 2025 Convex Marking Scheme
- authors: Nguyen Quoc Hung, Nguyen Dang Minh, Le Nhu Quynh, Tran Khanh Linh, Nguyen Kieu Linh
- affiliations: not stated
- posted: 2026-08-18
- source: arXiv
- link: https://arxiv.org/abs/2608.18336v1
- keyword hits: claude, qwen

### abstract

When evaluating language models on human exams, benchmarks typically score each response as right or wrong and report the overall accuracy. This approach assumes that partial knowledge is worth proportional credit, an assumption that fails when an examination uses a non-additive grading scheme. The 2025 reform of Vietnam's National High School Graduation Examination demonstrates the cost of this substitution. In Part II of the exam, candidates evaluate four true/false statements per question. The grading is convex: the number of correct statements earns 0, 0.10, 0.25, 0.50, or 1.00 points. Identifying three statements correctly pays 0.50 points, not the 0.75 points that standard accuracy metrics would award. Because Part II accounts for 4.00 of the exam's 10.00 points, reporting accuracy inflates the score by rewarding partial knowledge that the state explicitly penalizes. We introduce THPT-Ladder, a benchmark of 632 items from 21 official exams across 11 subjects, graded exactly as the ministry grades its students. The ministry publishes the marks of over a million candidates, allowing us to place models directly into the human cohort. Across eight models, the official rubric pays 0.020 to 0.159 points less per Part II question than proportional credit. This shortfall changes a model's apparent competence. For Qwen3.5-27B on the 2025 History exam, a 0.042-point shortfall drops its standing from the 90th to the 77th percentile among 481,293 candidates. A model's accuracy does not predict this penalty. At Claude Sonnet 5's accuracy level, different distributions of errors yield scores varying from 0.869 to 0.932 points per question. Official marks depend on how correct statements are grouped, meaning standard benchmarks report a competence the institution would not certify.

---

## uid: `arxiv:2608.18303v1`

- title: SESSE: Sketch, Expand, Sort, Summarize, Evaluate -- LLM-as-Judge Evaluation via Structured Decomposition
- authors: Dae Lee, Mihai Delgeanu, Adel Youssef
- affiliations: not stated
- posted: 2026-08-18
- source: arXiv
- link: https://arxiv.org/abs/2608.18303v1
- keyword hits: chain-of-thought, fine-tuning, llm

### abstract

LLM-as-judge evaluation reduces response quality assessment to a single holistic A/B preference choice, providing no mechanism to isolate which quality dimensions drove the preference or distinguish model errors from genuine label ambiguity. We propose SESSE (Sketch, Expand, Sort, Summarize, Evaluate), a training-free framework that decomposes holistic judgment into structured sub-questions mined directly from the judge's own error cases; requiring no oracle responses, task-specific rubrics, or fine-tuning. On RewardBench (n=1,000), SESSE achieves near-parity with the chain-of-thought baseline and is competitive with RISE-Judge-32B (92.7%), a fine-tuned specialist, while remaining fully training-free. Per-criterion vote evidence provides an interpretable audit trail for diagnosing label ambiguity and judge failure modes unavailable from a single holistic output token.

---

## uid: `arxiv:2608.18011v1`

- title: The IOL-AI Challenge: An Open Challenge towards Advancing Linguistic Reasoning
- authors: Eduardo Sánchez, Rita Berrada, Dan-Mircea Mirea, Sara Rajaee, Alexander Piperski, Ana Meta Dolinar, Boris Iomdin, Andrey Nikulin
- affiliations: not stated
- posted: 2026-08-18
- source: arXiv
- link: https://arxiv.org/abs/2608.18011v1
- keyword hits: claude, llm, llms

### abstract

Reasoning in LLMs is overwhelmingly studied in domains that provide a model with rules: mathematics and code. Linguistic puzzles invert this: the solver must first discover the system before reasoning within it. We present the IOL-AI Challenge, an open-science competition run on the unseen problems of the International Linguistics Olympiad (IOL) 2026 Individual Contest, evaluated both automatically and, for the first time, by members of the official IOL Jury under the same rubrics applied to human contestants. The challenge drew 731 submissions from 46 teams under a strict compute budget (one T4, 30 mins). We additionally benchmark 15 unconstrained frontier and open models, with Claude Opus 4.8 earning a jury score equivalent to a gold medal, while both resource-constrained systems we submitted for jury grading scored in the range of the bottom 5% of contestants. Capability was not determined by scale: 14B submissions outperform models twice their size, and gains come from decoding and output-handling rather than model capacity. We also found that automatic metrics rank systems exactly as the jury does, but compress the scale, upscoring weak systems by ~13 points and understating strong ones. Our analysis shows that while frontier models might have prior knowledge about some of the problem languages, it does not significantly help them solve the linguistic reasoning tasks, leaving linguistic reasoning as a strong benchmarking proxy for generalizable reasoning skills.

---

## uid: `arxiv:2608.17829v1`

- title: The Model's Tell: Measuring Context-Leakage Attack Signals with Behavior Gauges
- authors: Maosen Zhang, Jianshuo Dong, Boting Lu, Wenyue Li, Xiaoping Zhang, Tianwei Zhang, Jie Zhang, Han Qiu
- affiliations: not stated
- posted: 2026-08-18
- source: arXiv
- link: https://arxiv.org/abs/2608.17829v1
- keyword hits: llm, llms

### abstract

LLMs increasingly rely on external contexts, such as pre-defined system prompts or retrieved documents, to improve generation quality. However, processing these contexts alongside user queries creates an attack surface: adversarial inputs can induce models to disclose them. Prior probing studies suggest that leakage-related signals emerge in hidden states, yet the need to extract these states poses additional deployment challenges. In this paper, we explore whether this internal signal leaves a more accessible ``tell'' before decoding. We propose LeakGauge, which probes this response by appending a suffix that gauges leakage behavior and mapping its prefill token probabilities to an attack-risk score. While a direct gauge uses the initial tokens of confidential content, we find that a content-agnostic one that verbalizes leakage behavior yields more robust signals. Across 11 LLMs, including GLM-5.2 (753B) and Kimi-K3 (2.8T), LeakGauge reaches an AUROC range of 0.944--0.996 on unseen attacks. The signal remains stable when the content changes language or the attack shifts from verbatim to semantic disclosure. By activation-steering interventions, we further show that the risk score is sensitive to an internal leakage-related direction, relating the observable signal to the model's internal representation. In addition, LeakGauge enables an input detector with fewer than 0.5K extra parameters and added latency of 10.34 ms. Code: \href{https://github.com/yeasen-z/LeakGauge}.

---

## uid: `arxiv:2608.17827v1`

- title: From Global Benchmarks to Local Evaluations: Benchmarking LLMs for the German Public Sector
- authors: Camilla Dalerci, Thilo Michael, Robin Schaefer, Daniel Weinland
- affiliations: not stated
- posted: 2026-08-18
- source: arXiv
- link: https://arxiv.org/abs/2608.17827v1
- keyword hits: llm, llms

### abstract

Public institutions face a persistent challenge in selecting LLMs suited to their specific context. Existing benchmarks, however, are of limited use as they primarily reflect English-language and US-centric settings, and often only evaluate task performance. In this paper, we present first results of MÖVE, a holistic evaluation framework for the German public sector, examining three rarely considered governance dimensions: energy consumption, provider transparency, and knowledge of German-party positions. Our results reveal significant trade-offs, with no single model excelling across all dimensions: estimated energy consumption varies more than 60-fold and is not explained by model size alone, information disclosure varies systematically across providers, and European models do not exhibit stronger knowledge of German party positions. Model selection for public institutions thus cannot rely on performance rankings alone. Instead, evaluations should also reflect the governance requirements of the deployment context.

---

## uid: `arxiv:2608.17718v1`

- title: Beyond Suspicious Steps: Ontological Trust in Long-Horizon Agents
- authors: An He, Yao Wang, Haibin Zhang
- affiliations: not stated
- posted: 2026-08-18
- source: arXiv
- link: https://arxiv.org/abs/2608.17718v1
- keyword hits: llm, llms

### abstract

Long-horizon agents increasingly operate across many steps, tools, and observa- tions. In this setting, the relevant oversight question is not only whether each action is locally valid, but whether the evolving trajectory still corresponds to the task the user authorized. Drift can accumulate quietly: an agent may call the right tool with plausible arguments at every step, while its prefix moves toward a broader role, an adjacent objective, or evidence the user never supplied. Existing monitors mostly check local compliance, deliver final-trace verdicts, or score generic risk; they do not directly estimate this prefix-level relation. We introduce ontological trust, a task-conditioned property of trajectory prefixes, and instantiate it as RGE, an online monitor that decomposes trust along Role, Goal, and Evidence. RGE uses LLMs only to derive structured task and step representations; trust-state updates, projec- tions, and intervention decisions are deterministic, so the output is a replayable and auditable trust trajectory rather than a single end-to-end judge verdict. We construct a cross-domain trajectory corpus from OSWorld, FinanceBench, and EICU-AC, covering benign executions, prefix-paired drift, and pseudo-consistency failures. On this corpus, RGE outperforms adapted rule-, judge-, and shield-style baselines on prefix-paired drift detection. With the two larger estimator models, it exceeds 93% Drift F1 on every benchmark while keeping benign coverage at or above 95.8%. Pseudo-consistency is harder: detection depends on whether task completion is externally visible, a structural limit we characterize empirically.

---

## uid: `arxiv:2608.17360v1`

- title: Fair ASR: Re-Evaluating Black-Box Jailbreaks under Shared Target-Call Budgets
- authors: Zhida He, Xiaoyu Wen, Han Qi, Ziyuan Zhou, Peng Yu, Jiajia Li, Chaochao Lu, Qiaosheng Zhang
- affiliations: not stated
- posted: 2026-08-18
- source: arXiv
- link: https://arxiv.org/abs/2608.17360v1
- keyword hits: gpt-5, llm

### abstract

Reliable jailbreak evaluation is essential for assessing LLM safety, but most existing studies rely solely on attack success rate (ASR) without accounting for its dependence on attack budgets, resulting in unfair comparisons across methods. Existing compute-aware evaluations reduce heterogeneous resources into FLOPs, which is difficult to estimate for black-box models and fails to capture resource-specific constraints. To provide a comparable evaluation basis, we introduce Fair-ASR, an evaluation protocol for black-box jailbreak attacks under shared target-call budgets B, using target calls as a directly observable and method-agnostic comparison axis while tracking attacker calls separately for efficiency analysis. We re-evaluate 11 representative attacks under the Fair-ASR protocol and find that attack rankings change substantially across target-call budgets, simple stochastic perturbations and hand-crafted templates remain highly competitive under equal target access, and no evaluated LLM-driven method is efficient in both target and attacker calls. Motivated by this efficiency gap, we introduce ReCode, a compositional budget-efficient attack that combines desensitization rewriting with two effective low-cost primitives identified by Fair-ASR. Under a budget of 20 target calls, ReCode achieves 85% ASR on GPT-5 while requiring only 7.19 attacker calls per request on average, showing strong efficiency in both target and attacker calls.

---
