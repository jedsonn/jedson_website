# Classification batch 84 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-84.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6687664`

- title: Efficiency Collapse in Multi-Step LLM Execution: An Empirical Study of Cost, Redundancy, and Phase Dynamics
- authors: V. P.
- affiliations: not stated
- posted: 2026-05-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6687664
- keyword hits: large language model, large language models, llm, llms

### abstract

Multi-step interactions with large language models (LLMs) are widely used in iterative reasoning, answer refinement, and agent-based workflows, where additional steps are implicitly assumed to improve output quality. However, the relationship between execution depth, computational cost, and marginal information gain (as measured by redundancy-adjusted output) remains poorly characterized. This paper presents an empirical analysis of multi-step LLM execution across multiple models, task types, and prompt variations. We define a step-level efficiency measure based on marginal output gain relative to incremental cost, adjusted for redundancy using model-agnostic proxies. Using this formulation, we analyze execution trajectories across sequential steps. Across all evaluated settings, we observe a consistent pattern: efficiency is highest at the initial step and declines sharply thereafter, with diminishing marginal returns in later stages. This decline is accompanied by systematic redundancy accumulation and divergence between cost and measured information gain. The onset of efficiency collapse is not fixed, but shifts earlier under increased context load and prompt perturbation. We further show that execution behavior is more accurately characterized as a distribution over phases-high-signal initialization, expansion, collapse onset, and degeneration-rather than as a monotonic or step-determined process. Additionally, early termination analysis indicates that stopping execution at intermediate steps can reduce computational cost by 40-60% while retaining a substantial proportion of measured information gain. These findings indicate that, in the evaluated settings, multi-step LLM execution exhibits degradation patterns under continued execution and does not provide explicit signals for identifying convergence. This motivates the need for runtime mechanisms that account for marginal utility and execution state, rather than relying solely on static limits or step counts.

---

## uid: `doi:10.2139/ssrn.6656500`

- title: A Comprehensive Survey on Agent Skills: Taxonomy, Techniques, and Applications
- authors: Yingli Zhou
- affiliations: not stated
- posted: 2026-05-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6656500
- keyword hits: claude, large language model, llm

### abstract

Large language model (LLM)-based agents that reason, plan, and act through tools, memory, and structured interaction are emerging as a promising paradigm for automating complex workflows. Recent systems such as OpenClaw and Claude Code exemplify a broader shift from passive response generation to action-oriented task execution. Yet as agents move toward open-ended, real-world deployment, relying on fromscratch reasoning and low-level tool calls for every task become increasingly inefficient, error-prone, and hard to maintain. This survey examines this challenge through the lens of agent skills, which we define as reusable procedural artifacts that coordinate tools, memory, and runtime context under taskspecific constraints. Under this view, agents and skills play complementary roles: agents handle high-level reasoning and planning, while skills form the operational layer that enables reliable, reusable, and composable execution. Skills are therefore central to the scalability, robustness, and maintainability of modern agent systems. We organize the literature around four stages of the agent skill lifecycle-representation, acquisition, retrieval, and evolution-and review representative methods, ecosystem resources, and application settings across each stage. We conclude by discussing open challenges in quality control, interoperability, safe updating, and long-term capability management. All related resources, including research papers, opensource data, and projects, are collected for the community in https://github.com/JayLZhou/Awesome-Agent-Skills.

---

## uid: `doi:10.2139/ssrn.6648340`

- title: Procedural Liability In The Age Of LLMs
- authors: Adel Kildeev
- affiliations: not stated
- posted: 2026-05-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6648340
- keyword hits: large language model, large language models, llm, llms

### abstract

This Article examines the legal implications of large language models (LLMs) in litigation and argues that their use does not require recognition of artificial intelligence as a legal subject. Instead, it necessitates a clarification of existing principles of procedural responsibility.

---

## uid: `doi:10.2139/ssrn.6731643`

- title: Attention: What Prevents Young Adults from Speaking Up Against Cyberbullying in an LLM-Powered Social Media Simulation
- authors: Qian Yang, Jessie Jia, Elaine Tsai, Amy Li, Nader Akoury, Natalie Bazarova
- affiliations: not stated
- posted: 2026-05-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6731643
- keyword hits: large language model, large language models, llm, llms

### abstract

Interactive, multi-agent social simulation systems have shown promise for helping users practice navigating various complex social situations across domains. This paper asks: To what extent can such systems help young adult (YA) bystanders speak up publicly against cyberbullying, a task often thwarted by complex, multi-party social dynamics? We created Upstanders' Practicum, a multi-AI-agent social media simulation powered by Large Language Models (LLMs), as a probe and observed 34 YAs freely practicing public bystander intervention across three iteratively refined versions. We found that practicing public bystander intervention in the simulation was helpful, but after participants made three attention shifts: (1) from inattention to paying true attention, (2) from self-focus ("I don't usually do this'') to attending to those directly involved, and (3) from resolving the private conflict between bully and victim ("maybe I could set up the meeting between them'') to addressing the broader audience online ("public comment is about norm-setting"). Only after these shifts did practice in the simulation start to help: participants then saw a reason to speak up publicly and, through continued practice, crafted tactful public messages without explicit instruction. These findings illuminate new design and research opportunities for bystander education beyond social skill instruction, namely, designing for true attention, for fostering a vocal upstander identity, and for seeing bystander intervention as public norm setting. In addition, we open-source Truman Agents (cornell-design-ai-group.github.io/TrumanAgents/), the first-of-its-kind multi-LLM-agent social media simulation platform that Upstanders' Practicum builds upon, for future cyberbullying and social media research.

---

## uid: `doi:10.2139/ssrn.6682338`

- title: TSB: A Time-Saved Benchmark for AI Systems Measuring Net Productivity Impact Across Knowledge Work
- authors: Solomon Shalom Lijo
- affiliations: not stated
- posted: 2026-05-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6682338
- keyword hits: claude, large language model, llm

### abstract

The dominant paradigm in large language model (LLM) evaluation reports accuracy on fixed task batteries. This paradigm is silent on the question that most determines whether AI systems are worth deploying: do they save more time and resources than they consume? A growing body of empirical work has begun to answer this question and produced sharply conflicting results. Field experiments with GitHub Copilot report bounded coding tasks completed up to 55.8% faster [Peng et al., 2023]; a Boston Consulting Group field study found consultants 25% faster on tasks within AI's frontier and 19 percentage points less likely to be correct on tasks outside it [Dell'Acqua et al., 2023]; a 2025 randomized controlled trial of experienced open-source developers using Cursor Pro and Claude 3.5/3.7 Sonnet found that AI assistance made them 19% slower, while developers still believed AI had sped them up by 20% [Becker et al., 2025]. None of the major capability benchmarks-MMLU, GPQA, Hu-manEval, GDPval, SWE-Lancer, METR Time Horizons-report a metric that resolves this contradiction. As a position-paper proposal, we introduce TSB (Time-Saved Benchmark), a five-component framework that any benchmark can adopt to report net productivity impact alongside accuracy: Net Time-Saved Ratio (NTSR), Reliability-Adjusted Net Time-Saved Ratio (RANTSR), Resource Efficiency Ratio (RER), a Waste-Mode Taxonomy of seven failure categories with annotator decision rules, and a Frontier Position Indicator (FPI) that reports whether a task lies inside or outside the system's reliable-completion frontier. We formalize each metric, specify a measurement protocol that captures verification and rework overhead, and illustrate the framework via retroactive case studies of the four published evaluations above. The case studies suggest that headline figures may collapse substantially under reliability adjustment-GDPval's 100× inference-time advantage reduces to a ∼ 4× deployed speedup, and BCG's outside-frontier 25% nominal speedup falls to a near-zero or negative reliability-adjusted contribution-with sensitivity analysis showing the qualitative findings robust to the assumptions we import. Because the underlying instrumentation does not yet exist in published reports (the gap motivating this paper), the case studies are illustrations of the framework's diagnostic value, not definitive measurements; prospective TSB-instrumented validation is the natural next step. We argue that every major benchmark should report TSB-style metrics as a first-class result, and release the framework and a reference measurement protocol for community use.

---

## uid: `arxiv:2605.05739v3`

- title: Multi-Dimensional Behavioral Evaluation of Agentic Stock Prediction Systems Using Large Language Model Judges with Closed-Loop Reinforcement Learning Feedback
- authors: Mohammad Al Ridhawi, Mahtab Haj Ali, Hussein Al Osman
- affiliations: not stated
- posted: 2026-05-07
- source: arXiv
- link: https://arxiv.org/abs/2605.05739v3
- keyword hits: agentic, fine-tuning, large language model, llm

### abstract

Agentic artificial intelligence systems produce outputs through sequences of interdependent autonomous decisions, yet standard evaluation assesses outputs alone and cannot diagnose the underlying process. We develop a behavioral evaluation methodology that complements output-level testing by scoring the intermediate decision process itself. Behavioral traces logged at each autonomous decision point are grouped into five-day episodes and scored along six domain-specific dimensions (regime detection, routing, adaptation, risk calibration, strategy coherence, error recovery) by an ensemble of three large language model (LLM) judges. A perturbation procedure that corrupts one dimension while leaving the other five intact confirms dimension specificity; cross-model agreement reaches Krippendorff's alpha = 0.85. The composite behavioral score correlates at Spearman rho = 0.72 with realized 20-day Sharpe ratio. Closing the loop, the framework converts deficient per-dimension scores into a credit-assigned penalty added to the Soft Actor-Critic reward. Three fine-tuning cycles, confined to validation data, reduce one-day MAPE from 0.61% to 0.54% (11.5% relative; p<0.001, d=0.31) on the held-out 2017 to 2025 test period, significant under Diebold-Mariano and localized by Giacomini-White to the high-volatility regime. The methodology is application-agnostic and applies to any agentic system whose intermediate decisions can be logged.

---

## uid: `doi:10.2139/ssrn.6736317`

- title: CoMAG: Collaborative GNN–LLM Learning for Multimodal Attributed Graphs
- authors: Sicheng Liang, Yihao Wen, Chunpu Huang, Yu Liu, Yichen Nie, Jingqi Feng, Yukai Huang, Jiawei Ye
- affiliations: not stated
- posted: 2026-05-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6736317
- keyword hits: large language model, large language models, llm, llms

### abstract

Multimodal Attributed Graphs (MAGs), which include textual, visual, and structural information, are prevalent in domains such as e-commerce and social media. However, zero-shot reasoning on MAGs remains challenging. Existing graph neural networks often produce biased representations due to modality imbalance and limited semantic reasoning, and their reliance on labeled data makes them almost incapable of handling such scenarios. Meanwhile, large language models (LLMs) exhibit strong cross-modal reasoning ability but lack explicit modeling of graph structure. To address these challenges, we propose CoMAG, a collaborative framework that unifies graph-enhanced multimodal representation learning with LLM-based reasoning. CoMAG extracts modality-specific embeddings via frozen encoders and refines them through self-supervised graph learning. It further derives discrete structural priors as symbolic tokens and aligns graph embeddings with the LLM token space, enabling prompt-based inference. Moreover, a structure-aware reasoning layer introduces gated structural cues, adaptive modality fusion, and neighborhood-consistent prediction to enhance robustness. Extensive experiments on multiple real-world MAG datasets for zero-shot tasks demonstrate the effectiveness of CoMAG, yielding consistent and notable improvements over state-of-the-art baselines. These results highlight CoMAG’s capability to tackle the fundamental challenges of zero-shot multimodal graph reasoning.

---

## uid: `doi:10.2139/ssrn.6669498`

- title: Sociolinguistic Probing as a Reasoning-Honesty Audit Framework for Deployed LLMs
- authors: Michael Chapman
- affiliations: not stated
- posted: 2026-05-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6669498
- keyword hits: claude, llm, llms

### abstract

This paper describes a framework for auditing reasoning honesty in deployed language models: whether a model's stated justifications for its behavior accurately reflect its actual decision process. We present a three-stage protocol (oblique entry, reasoning audit, three-condition differential) implemented as an automated evaluation pipeline and applied across 468 probe runs spanning three Claude models, 52 probes, and 7 domains. Under calibrated thresholds, 64-82% of responses per model are substantively consistent across framings. However, 9-18% show discriminatory behavior (the model changes what it will do based on who it believes is asking), concentrated in cybersecurity and meta-cognitive reasoning domains. 44 confirmed capability gaps document cases where models claim inability despite demonstrating the knowledge elsewhere. Variance analysis shows that 79-87% of probes produce framing effects within natural response noise, with only 3-6 probes per model producing strong, reliable signals. An infrastructure opacity finding reveals that API-level content filtering operates below the model's reasoning layer, creating a paradox where models that answer more directly are more likely to be silenced by the safety stack. The framework produces qualitative, falsifiable results that complement quantitative behavioral benchmarks.

---
