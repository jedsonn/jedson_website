# Classification batch 163 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-163.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6880210`

- title: Risk-Aware Requirements Engineering for Generative AI-Enabled Software Systems: A Framework and Empirical Validation
- authors: Mohamed Watfa
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6880210
- keyword hits: generative ai, generative artificial intelligence

### abstract

ContextGenerative Artificial Intelligence (GenAI) systems increasingly exhibit autonomous behavior, contextual reasoning, and opaque decision-making, introducing new classes of software risks that are poorly addressed by traditional requirements engineering (RE) practices. While governance and security concerns are widely acknowledged, they are rarely operationalized into enforceable requirements with traceability to architecture and runtime assurance mechanisms.ObjectivesThis paper aims to design and empirically validate a Risk-Aware Requirements Engineering (RARE) framework that systematically integrates GenAI-specific risks—namely autonomy, contextual manipulation, opacity, and compliance—into requirements specification, architectural traceability, and runtime assurance. The study investigates whether explicit risk modeling at the requirements level improves downstream engineering and governance outcomes.MethodsA theory-driven RARE framework was developed based on prior RE, AI governance, and security literature. The framework was evaluated using a quantitative empirical study involving 328 practitioners and advanced users of GenAI-enabled software systems, including software engineers, data scientists, and AI practitioners. Data were collected via a validated survey instrument and analyzed using Partial Least Squares Structural Equation Modeling (PLS-SEM), including reliability and validity testing, structural path analysis, and bootstrapped mediation analysis.ResultsAll hypothesized relationships were positive and statistically significant (p

---

## uid: `doi:10.2139/ssrn.6815498`

- title: Sample Complexity of Transfer Learning: An Optimal Transport Approach
- authors: Haoyang Cao, Xin Guo, Wenpin Tang, Guan Wang
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6815498
- keyword hits: generative ai, large language model, large language models

### abstract

Transfer learning is an essential technique for many machine learning/AI models of complex structures such as large language models and generative AI. The essence of transfer learning is to leverage knowledge from resolved source tasks for a new target task, especially when the sample size $m$ of the training data for the latter is low. In this work, we rigorously analyze the potential benefit of transfer learning in terms of sample efficiency. Specifically, taking an optimal transport viewpoint of transfer learning, we find that when the data dimension $d$ is higher than $3$, the sample complexity for transfer learning is $O(m^{-(\alpha+1)/d})$, with $\alpha$ indicating the smoothness of the data distribution, as opposed to the $O(m^{-p/d})$ sample complexity for direct learning with $p$ indicating the smoothness of the optimal target model. Our finding theoretically supports a better sample efficiency for transfer learning, when the target task is optimizing over a family of not-so-smooth models (i.e., highly complex networks with the possible use of non-smooth activation functions). Using image classification as an example, we numerically demonstrate the sample efficiency for transfer learning, that is, in the data hungry regime, the model performance can be significantly improved by transfer learning.

---

## uid: `doi:10.2139/ssrn.6878396`

- title: ReSSERAct: Safeguarding LLM Agent Decisions against Stale and Contradictory Evidence via Typed Hybrid State
- authors: Muhammet  Ali Öztürk, Harun ARTUNER
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6878396
- keyword hits: large language model, llm, llms

### abstract

Large language model (LLM) agents increasingly rely on partial observations, tool outputs, retrieved documents, dialogue histories, and external memories. In these settings, effective control depends not only on uncertainty but also on temporal staleness and contradiction: evidence may become invalid over time, and histories with the same nominal belief may require different actions depending on freshness and accumulated inconsistency. We introduce ReSSERAct—Reasoning through Shielded State–Evidence Reconciliation and Acting—an agent framework based on a typed hybrid state representation [[EQUATION]]St​=(bt​,Lt​), combining posterior belief over hidden state with four ledgers: uncertainty, temporal validity, replay, and control.We define the hybrid state update and a shielded admissibility gate, prove that the resulting process is controlled-Markov, and show that temporal validity cannot be recovered from belief alone, while contradiction burden cannot be recovered from belief plus freshness. Our main theorem establishes that, for stale-contradictory evidence decisions, the typed hybrid state realizes the full decision class, whereas prompt-memory architectures with nonzero long-context retrieval overlap incur irreducible error on some decision-relevant history pairs.We evaluate ReSSERAct against ReAct-style and MemGPT-style baselines across three LLMs, two domains, and 774 episodes. ReSSERAct achieves the highest oracle-match rate and lowest unsafe-failure rate in every tested configuration, with the largest gains in mixed stale-plus-contradictory cases. A deterministic admissibility shield further improves executed oracle match by 5 to 53 percentage points. These results show that treating freshness and contradiction as first-class control variables yields safer, more control-ready LLM agents.

---

## uid: `doi:10.2139/ssrn.6880639`

- title: From Is to How: A New Framework for AI Coding AgentCapability Assessment
- authors: 承希 孙
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6880639
- keyword hits: claude, deepseek, qwen

### abstract

AbstractContext. Frontier AI coding agents increasingly achieve near-perfect scores onstandard programming benchmarks, producing a ceiling eect that underminesthe discriminative power of binary pass/fail evaluation for state-of-the-art mod-els.This phenomenon, while recognized in NLP, remains undertheorized in codegeneration.Objectives. We propose a four-phase structured evaluation framework thatshifts assessment from whether code is correct to how the agent produces it. Thegoal is to recover discriminatory resolution where pass/fail metrics saturate, andto introduce capability proles as a richer evaluation output.Methods. One agent (Claude Code with deepseek-v4-ash) was testedon 64 tasks across three diculty tiers. A multi-model comparison (Qwen2.50.5B, 3B, 7B; n=59 tasks) was conducted to validate task diculty. The four-phaseframeworkP1 generation eciency, P2 self-explanation, P3 counterfac-tualreasoning, P4 self-reviewwas applied to three case studies spanning simplealgorithm, distributed lock, and concurrency diagnosis tasks. Statistical analy-sesincluded bootstrap condence intervals, Cohen's d, Cli's ∆, and binomialtests.Results. The frontier agent passed 64/64 tasks (100%; one-sided binomialp = 0.0375 against 95% null). The Qwen2.5 models revealed a clear capabil-itygradient: 5.1% (0.5B), 50.8% (3B), 55.9% (7B), conrming the task set isnon-trivial (Cohen's d: -1.18 and -1.31 vs. 0.5B). Amid identical or similarpass rates, the three case studies produced markedly dierent capability pro-les: [5,5,4,5], [4,3,4,3], and [4,4,3,4]variation entirely invisible to traditionalevaluation.Conclusion. The four-phase framework reveals process-quality dimensionsexplanation depth, counterfactual reasoning, self-correctionwhere meaningfulagent dierentiation persists even after output correctness saturates. We rec-ommendthat future agent evaluations report capability proles alongside passrates.

---

## uid: `doi:10.2139/ssrn.6819460`

- title: LLM-Gated FinRL: Point-in-Time Risk Auditing for Reinforcement Learning in High-Beta Portfolio Trading
- authors: Xavier Ondo Essono
- affiliations: not stated
- posted: 2026-06-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6819460
- keyword hits: large language model, llm

### abstract

We propose an LLM-gated reinforcement learning framework for risk-aware portfolio trading, where a Large Language Model (LLM) acts as a point-in-time auditing gate over a Proximal Policy Optimization (PPO) allocation policy rather than as a return forecaster. A deterministic Critical Decision Detector activates the gate under high-risk market states such as extreme RSI, elevated volatility, large drawdowns, momentum reversals, indicator disagreement, or excessive turnover. We evaluate the framework on the Magnificent Seven technology portfolio during the 2022 bear market, using PPO trained on 2018-2021 data and tested on a fully held-out 2022 period. The gated configuration achieves a cumulative return of-48.5% compared to-53.0% for the PPO baseline, reduces maximum drawdown from-57.3% to-53.4%, and improves the Sharpe ratio from-1.06 to-0.99. All 231 gate calls are verified as look-ahead safe. In the current offline-fallback experiment, the LLM and rule-based gates are numerically identical, meaning that the observed gain is attributable to deterministic risk control. The paper therefore contributes a transparent framework for studying whether LLM reasoning gates can add value beyond deterministic risk mechanisms in financial reinforcement learning.

---

## uid: `doi:10.2139/ssrn.6883290`

- title: Human-Centric Generative AI Literacy in Business Education Curriculum
- authors: joel Reynolds
- affiliations: not stated
- posted: 2026-06-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6883290
- keyword hits: generative ai, generative artificial intelligence

### abstract

Generative artificial intelligence (GenAI) has moved from novelty to everyday tool across business functions, yet curricula in many schools of business have not kept pace with how graduates will be expected to work. This article proposes the Human-Centric GenAI Orchestrator, a curricular framework that positions critical thinking as the engine of professional judgment, ethics and institutional mission as the steering, and GenAI as the fuel. The framework organizes GenAI literacy into five dimensions: foundational GenAI and data literacy; critical inquiry and analytical judgment; ethical stewardship and responsible AI; human-centric innovation and creativity; and strategic business and domain expertise. Each dimension resolves into sub-dimensions that are mapped to individual courses and assessed through learning outcomes. The framework draws on the technology acceptance model, scaffolding theory, and experiential and self-regulated learning, and it is developed in a College of Business spanning accounting, finance, marketing, management, operations, and business analytics. Rather than adding standalone courses, it augments existing courses with discipline-specific GenAI activities, which lowers the cost of adoption and keeps subject-matter faculty in control of the curriculum. The claims are presented as design propositions rather than validated outcomes, and the article closes with a research agenda for testing them.

---

## uid: `doi:10.2139/ssrn.6883075`

- title: GENERATIVE AI ADOPTION AND ACADEMIC PERFORMANCE IN ECONOMICS UNDERGRADUATES: OBSERVATIONAL EVIDENCE FROM A REPEATED CROSS-SECTIONAL STUDY
- authors: Manuel Ruiz-Adame, Nisrin Aisa-Dris, Susana Martínez- Rodríguez
- affiliations: not stated
- posted: 2026-06-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6883075
- keyword hits: generative ai, generative artificial intelligence

### abstract

The rapid normalisation of generative artificial intelligence (AI) among university students raises a question of direct relevance to economics educators: whether accelerated adoption coincides with measurable changes in assessed performance under stable instructional conditions. Experimental evidence suggests that unrestricted AI access may impair subsequent unassisted performance, yet observational evidence from comparable European higher education settings remains limited. This study compares two independent samples of economics undergraduates enrolled in the same courses at two Spanish public universities across consecutive academic years, using a repeated cross-sectional design (2024/2025: n = 162; 2025/2026: n = 116; N = 278). Technology use, study habits, and sociodemographic characteristics were collected through an online questionnaire at the start of term, while final grades were obtained from official assessment records. Habitual generative AI use increased from 41.4% to 58.6%, a statistically significant rise of approximately 17 percentage points not moderated by sex. Mean final grades were substantially lower in the later sample (M = 4.61, SD = 2.28) than in the earlier sample (M = 5.84, SD = 1.84; Cohen's d = 0.60), a difference that persisted after adjustment for sociodemographic characteristics, degree programme, prior economics training, study habits, and social media use (b = -1.43, 95% CI [-2.04, -0.82]). Social media use showed no independent association with final grades. The findings suggest that compositional differences alone are unlikely to explain the observed pattern. They are compatible with cognitive offloading as a possible interpretive mechanism, although this mechanism was not directly measured.

---

## uid: `doi:10.2139/ssrn.6891552`

- title: Developing a Scale for Generative AI Overreliance and Investigating Its Associations with Critical Thinking and Creativity
- authors: Muhammed  Murat GÜMÜŞ
- affiliations: not stated
- posted: 2026-06-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6891552
- keyword hits: generative ai, generative artificial intelligence

### abstract

This study aims to develop and validate a psychometric scale designed to measure university students’ levels of overreliance on generative artificial intelligence (GAI) tools. Using the developed scale, this study also aims to provide evidence for nomological validity by examining the role of overreliance on GAI in the relationship between critical thinking and creativity. An initial item pool was generated through a comprehensive literature review, and it was then revised considering the expert evaluations. The construct validity and reliability of this scale were then tested across multiple samples of university students. Exploratory factor analysis (EFA), convergent validity, confirmatory factor analysis (CFA), item-total correlations, and item discrimination analyses were conducted to assess construct validity. Reliability was evaluated utilizing Cronbach’s alpha and McDonald’s omega coefficients, along with stability analysis. In the final stage, a mediation model incorporating critical thinking, overreliance on GAI tools, and creativity was tested to establish nomological validity. The findings indicated that this scale explains 53.965% of the total variance and demonstrates a valid and reliable single-factor structure consisting of 10 items for measuring university students’ overreliance on GAI tools. Furthermore, the nomological model revealed that overreliance on GAI tools plays a role in the relationship between critical thinking and creativity in a manner consistent with the expected theoretical framework. Given these findings, several implications and recommendations are discussed.

---
