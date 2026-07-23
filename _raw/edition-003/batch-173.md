# Classification batch 173 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-173.answer.json` as a JSON array.

---

## uid: `arxiv:2606.29871v1`

- title: AI Training Manager: Bounded Closed-Loop Control of Adaptive Training Recipes
- authors: Anjali Rao, Nikhil Kamalkumar Advani
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.29871v1
- keyword hits: llm, llms

### abstract

We present the AI Training Manager, a bounded LLM-based supervisory controller for adaptive machine learning training. Standard training pipelines often rely on fixed recipes or single-axis schedulers, which can struggle with mid-run failures such as severe overfitting, loss imbalance, exploration collapse, or unsafe exploration. Rather than replacing mathematical optimizers or acting as an unconstrained coding agent, the manager operates through a schema-conditioned interface: it reads structured telemetry snapshots from an active run, audits a constrained action space, and returns validated updates to training parameters such as learning rate, regularization strength, loss-weight coefficients, and exploration settings. We evaluate this architecture across supervised language modeling and reinforcement learning. On TinyStories, the manager detects and corrects overfitting, achieving a validation loss 60% lower than the baseline while producing auditable intervention logs. In this supervised setting, we additionally show that manager inference does not need to block the training loop: training can continue while a manager response is pending, and validated updates can be applied asynchronously once available. In a robotic manipulation reinforcement-learning task, we use the same bounded decision interface in an episodic closed-loop setting, where manager updates are applied at evaluation or checkpoint boundaries. The manager mitigates both conservative and unsafe exploration regimes. These results suggest that schema-conditioned LLMs can serve as bounded supervisory managers for live training runs, complementing conventional optimizers and schedulers with interpretable, multi-axis intervention capabilities

---

## uid: `arxiv:2606.29799v1`

- title: The CRISTAL Method: Neurosymbolic analysis from AI-synthesized world models
- authors: Rafael Kaufmann, Felix Neubürger, Michael Walters, Thomas Kopinski, Dimitrije Marković
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.29799v1
- keyword hits: llm, llms

### abstract

This project introduces the CRISTAL Method (Coherent Reliable Intentional Synthesis of Truthful Analysis Logic), a neurosymbolic framework for automating complex analysis workflows, with fundamental investment analysis as a primary use case. This domain poses major challenges: high structural uncertainty, noisy and subjective data, tight attention budgets, and the need for justified, reproducible decisions. Human analysts often struggle in this domain due to cognitive biases and limitations, suggesting significant value in automation. But while LLM-based agents have been proposed as analytical aids, their limitations -- poor numerical reasoning, unawareness of uncertainty, and lack of reproducibility -- hinder their effectiveness in this context. CRISTAL addresses these gaps through a principled blend of statistical model synthesis, continuous learning, and active learning. Starting from a natural-language prior knowledge curriculum, CRISTAL builds a dynamic, interpretable probabilistic program that enables full Bayesian inference, including uncertainty quantification and budget-aware data acquisition. CRISTAL continually refines its world model during analysis, leveraging LLMs for code synthesis and learning. We validate CRISTAL on a novel benchmark of synthetic equities with rich financial and textual data. On a company classification task, CRISTAL achieves Bayes-optimal accuracy with just 5 examples and a 5-second budget, outperforming state-of-the-art LLMs that plateau around 40\% accuracy even with order-of-magnitude more input data and compute.

---

## uid: `arxiv:2606.29713v1`

- title: SEVA: Self-Evolving Verification Agent with Process Reward for Fact Attribution
- authors: Aojie Yuan, Yi Nian, Haiyue Zhang, Zijian Su, Yue Zhao
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.29713v1
- keyword hits: gpt-4, llm

### abstract

Hallucination is the reliability bottleneck for LLM-based agents, and fact attribution verifiers are the last line of defense -- yet today's verifiers emit only opaque binary labels, leaving agents unable to self-correct and operators unable to audit. We present SEVA, a structured verification agent that emits evidence alignments, step-by-step reasoning chains, calibrated confidence, and a six-category error diagnosis with actionable fixes. Training such an agent with RL is non-trivial: standard binary reward on multi-component output triggers advantage collapse -- within-group reward variance vanishes and the GRPO gradient disappears. We resolve this with a process reward that decomposes verification quality into five independent components weighted 70/30 toward process signals, restoring the gradient and inducing an implicit curriculum -- the agent first masters verification behavior (alignment 0.917 -> 0.997, format 72% -> 100%), then outcomes (F1 64.9 -> 69.0). Structured output further enables a Verify -> Reflect -> Probe -> Refine self-evolution loop, which over four rounds on a 7B model surfaces an unexpected structural finding: each round produces a benchmark-specialist, not a generalist (+15 pp on HaluEval, -10 to -14 pp on TruthfulQA in the same model, persistent at 4x data). On ClearFacts, SEVA-3B matches GPT-4o-mini (69.0 vs. 69.8 F1) while producing substantially richer, auditable output -- confirming a principle that should generalize: for any RL task with multi-component generation, reward granularity must match output granularity.

---

## uid: `doi:10.2139/ssrn.7027106`

- title: Detecting AI-Generated Fake Reviews Through Cross-Modal Inconsistency: A Probabilistic Adaptive Multimodal Approach
- authors: Yan Li, YUNQIAN LI, Long Zhang
- affiliations: not stated
- posted: 2026-06-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7027106
- keyword hits: generative ai, qwen

### abstract

Generative AI has enabled industrial-scale production of high-fidelity fake reviews that evade traditional detectors. Existing multimodal methods rely on deterministic alignment assumptions, overlooking the stochastic variability of authentic expressions and the systematic cross-modal inconsistencies inherent in AI-generated content. This study proposes the Inconsistency-Driven Adaptive Modulation Network (IDAMN), shifting detection from surface plausibility to probabilistic structural consistency verification. IDAMN employs a Mixture Density Network to model the conditional distribution of authentic multimodal data across three inconsistency dimensions—text-image semantic, text-image affective, and text-rating—quantifying deviation as probabilistic surprisal rather than deterministic distance. An inconsistency-guided FiLM mechanism dynamically modulates features by amplifying informative dissonance signals while suppressing noise without fixed thresholds. On a 1,387-sample multimodal dataset, IDAMN achieves 95.32% accuracy and 95.31% F1 score, substantially outperforming ablation variants (removing MDN drops F1 to 0.7888) and large multimodal models including Qwen-3-VL-Plus (F1=0.6512) and GLM-4.6V-106B (F1=0.6667). These findings demonstrate that explicit probabilistic inconsistency modeling provides a robust, interpretable foundation for detecting AI-generated deception, with direct implications for platform governance and trustworthy decision support in AIGC-era digital markets.

---

## uid: `doi:10.2139/ssrn.7029007`

- title: Executable Engineering Information for Coordinated Multi-Robot Construction Assembly
- authors: Qi Wang, Maowei Jiang, Yuxin Ren, Ruiqi Li, Miao Zhang, Peter Bus
- affiliations: not stated
- posted: 2026-06-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7029007
- keyword hits: large language model, llm

### abstract

This paper presents a Contract Language for Assembly Missions and Predicates (CLAMP), an executable engineering information framework for coordinated multi-robot construction assembly. CLAMP represents component data as records, mission clauses, action contracts, state predicates, handover rules, release conditions, confirmation records, and audit traces. A deterministic layer validates preconditions, updates states, regulates responsibility transfer, and gates release across a Universal Robot (UR) arm, automated guided vehicle (AGV), cable robot (CB), and installation-confirmation role with mixed-reality (MR)-style visualization and bounded large language model (LLM) advisory output. Unity experiments with ten timber assembly cases evaluated nominal execution, baselines, ablations, and robustness. CLAMP completed 380 missions and 8,290 actions without nominal failures, achieved 1.38 ± 0.63 mm final error, reduced template-baseline error from 42.42 mm to 9.23 mm, and recorded no authorized precondition violations or unverified releases.

---

## uid: `doi:10.2139/ssrn.7027101`

- title: When models do not know what they do not know
- authors: itsik elbert
- affiliations: not stated
- posted: 2026-06-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7027101
- keyword hits: large language model, large language models

### abstract

We test whether managerial reliance on backtested, mechanically generated cash-flow forecasts systematically distorts corporate investment. This is motivated by recent evidence that large language models, when forecasting financial outcomes from historical data alone, reproduce the same extrapolative bias long documented in human forecasters (Chen, Green, Gulen, and Zhou, 2024). Using a 195,337 firm-year panel (1999–2025) and a fully out-of-sample mechanical forecasting model, we construct an “algorithmic bias” measure independent of any specific vendor or technology and show that it is an economically significant predictor of subsequent investment: a one-standard-deviation increase corresponds to an 11% relative increase in investment intensity. Three pre-specified amplification hypotheses — that this sensitivity intensifies during structural breaks, in technology-intensive firms, or under low analyst dispersion — are rejected in the pooled tests. We then test 14 distinct heterogeneity hypotheses and apply within-family false-discovery-rate correction (Benjamini and Hochberg, 1995), a standard not yet routine in this literature. Five effects survive: financial constraints and corporate diversification attenuate bias sensitivity in both investment and overinvestment specifications; the S&P earnings-quality ranking shows a coherent, independently motivated attenuation pattern; and a direct SEC EDGAR text-mining measure of AI/ML disclosure — covering 5,588 firms, 2016–2024 — shows that firms explicitly disclosing AI/ML-based forecasting exhibit significantly LESS persistent algorithmic bias than non-disclosing firms. We interpret this convergent, FDR-robust evidence as identifying financial flexibility and organizational sophistication, not technological adoption per se, as the mechanism that determines whether a firm can correct a forecasting model's known weaknesses before that weakness becomes a capital-allocation mistake.

---

## uid: `doi:10.2139/ssrn.7012019`

- title: Development and Validation of a Multidimensional AI Addiction Scale: A Psychometric Approach Grounded in Behavioral Addiction Frameworks
- authors: Sezer Kizilates, Leonie Vogelsmeier, Aras Bozkurt, Sonsoles López Pernas, Mohammed Saqr
- affiliations: not stated
- posted: 2026-06-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7012019
- keyword hits: generative ai, generative artificial intelligence

### abstract

The rapid integration of generative artificial intelligence (GenAI) systems into educational settings has transformed student engagement and learning processes. However, empirical evidence increasingly demonstrates that heavy reliance on these tools may foster problematic dependency patterns characterized by cognitive offloading, reduced critical thinking, and functional impairment. While validated measurement instruments exist for internet, social media, and smartphone addiction, these tools are inadequate for capturing the unique psychological mechanisms underlying generative AI dependency, particularly the novel dimensions of cognitive reliance and parasocial attachment. This study addresses this critical gap by developing and validating a multidimensional AI Addiction Scale specifically designed for university students. Grounded in established behavioral addiction frameworks (DSM-5-TR and ICD-11) and informed by three complementary theoretical perspectives-the Interaction of Person-Affect-Cognition-Execution (I-PACE) model, Social Cognitive Theory, and Cognitive Load Theory-the study employed a rigorous three-stage psychometric development process: (1) expert review-guided item generation and content validation, (2) exploratory factor analysis (EFA) for dimensionality refinement, and (3) confirmatory factor analysis (CFA) for structural validation. Data were collected from 525 university students. The final 28-item scale demonstrates robust psychometric properties (CFI = 0.898, RMSEA = 0.062, SRMR = 0.047) across five theoretically coherent dimensions: Loss of Control, Cognitive Reliance, Socio-emotional Connection, Functional and Social Impairment, and Tolerance and Withdrawal. The scale provides a systematic, validated instrument for identifying and measuring problematic generative AI use among students, with important implications for educational institutions seeking to balance AI integration with the preservation of cognitive autonomy and critical thinking skills.

---

## uid: `doi:10.2139/ssrn.7027983`

- title: What Investors Disagree About: LLM-Decomposed Retail Disagreement and the Cross-Section of Stock Returns
- authors: Kefu Yi, Feng Wu
- affiliations: not stated
- posted: 2026-06-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7027983
- keyword hits: large language model, llm

### abstract

We use a large language model to read 220 million posts on China's largest stock forum and decompose investor disagreement by content. Disagreement about fundamentals generates Miller-type overpricing—over our 2016–2024 sample, high-disagreement stocks earn about 0.7% lower monthly risk-adjusted returns, with the premium markedly stronger in the first half of the period than in the recent low-participation years—whereas disagreement classified as noise does not, instead reflecting sentiment. Aggregate and dictionary measures pool these opposing contents and even point the wrong way, because aggregate disagreement is closely tied to sentiment. The fundamental-disagreement premium is nearly orthogonal to analyst forecast dispersion, survives standard and China-specific factor models, and is not driven by realized earnings surprises. In an event study of 36,000 earnings announcements, pre-announcement fundamental disagreement predicts significantly negative announcement returns—most clearly for fundamental content—consistent with overpricing that reverses when fundamentals are revealed.

---
