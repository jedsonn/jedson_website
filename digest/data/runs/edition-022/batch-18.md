# Classification batch 18 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-18.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7284398`

- title: Leaving the Scene after Vehicle-Train Collisions: Factors Associated with Post-crash Flight at U.S. Highway-Rail Grade Crossings
- authors: Pouyan Saiedian, Salvador Hernandez, Rakan  Mohammad Radwan Albatayneh, SM Rahat Rahman
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7284398
- keyword hits: large language model, llm

### abstract

Objectives: This study examines factors associated with post-crash flight among surviving drivers in highway-rail grade-crossing (HRGC) crashes, with emphasis on driver impairment. This study extracts post-crash-flight and impairment indicators from Federal Railroad Administration (FRA) narratives and evaluates their associations with driver, vehicle, crossing, environmental, train, and crash characteristics. Methods: A national FRA dataset of more than 17,000 HRGC crashes from 2005-2025 was analyzed. A large language model extracted binary indicators of post-crash flight and driver impairment from crash narratives. Post-crash flight was modeled as the target variable using binary logistic regression. Findings: Descriptive results showed that 4.77% of surviving drivers left the scene after an HRGC crash. The model indicated that driver impairment was strongly associated with this behavior: impaired drivers had 2.54 times the odds of leaving the scene than other drivers. Injured drivers had 88.7% lower odds of leaving than uninjured drivers. Higher odds were also associated with younger age, male drivers, passing another vehicle before the crash, and crashes occurring in darkness. These findings show that post-crash flight is related to driver condition, risky behavior, environmental conditions, and crash context. Novelty: This study is among the first national analyses of drivers leaving the scene after vehicle-train collisions at HRGCs. It also shows how structured FRA data can be combined with LLM-derived indicators of driver impairment and post-crash flight extracted from crash narratives. Practical Applications: The findings can support targeted crossing surveillance, rapid preservation of locomotive and crossing-camera recordings, and improved coordination between railroads and local lawenforcement agencies. The model may also help insurance companies identify higher-risk claims, prioritize investigations and support fraud detection. In addition, the results support adding structured fields for postcrash flight and driver impairment to FRA reporting systems, which could improve driver identification, data quality, infrastructure-damage recovery, and safety planning.

---

## uid: `doi:10.2139/ssrn.7305334`

- title: Model-Fixable or Architecture-Fixable? A Failure Taxonomy for Model-Agnostic Clinical Entity Extraction and Ontology Coding
- authors: Hemachandran Babu, Priyadarsini K
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7305334
- keyword hits: large language model, llm

### abstract

Background and Objective: Clinical entity extraction systems built around a single large language model inherit that model's specific quirks and failure modes. Swapping the model later causes some errors to vanish while new ones appear. Existing work reports per-model accuracy without asking whether an error belongs to the model or to the surrounding system. This paper asks whether extraction failures can be systematically attributed to the model versus the architecture so that teams know what to fix.Methods: We propose a modular model-agnostic framework for clinical entity extraction and ontology coding, in which extraction, ontology coding and validation are separated into independent components communicating through a fixed schema so that the underlying LLM can be replaced without redesigning the system. Building on this we developed a failure taxonomy synthesized from failure patterns already reported across the clinical NLP and LLM extraction literature, classifying each failure mode as either model-fixable (changes when the LLM is swapped) or architecture-fixable (persists regardless of which model sits underneath).Results: The taxonomy identifies distinct failure categories and classifies them against the criteria alongside a proposed controlled validation experiment for testing these classifications empirically. As this classification is derived from literature synthesis rather than a new experiment run, the model-fixable/architecture-fixable labels are proposed classification hypotheses, meant to guide future testing and not confirmed results.Conclusion: Separating model level failures from architecture-level failures gives clinical NLP teams a systematic way to decide whether a performance problem calls for a model upgrade or a pipeline redesign rather than defaulting to the easiest option.

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
