# Classification batch 203 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-203.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6852810`

- title: The disruptive turn in scientific workflows: Human orchestration of agentic AI in empirical research
- authors: Claudio Nigro, Enrica Iannuzzi, Leonardo Di Gioia, Roberto Popolo, Francesco Caputo
- affiliations: not stated
- posted: 2026-05-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6852810
- keyword hits: agentic, generative artificial intelligence

### abstract

The deployment of generative artificial intelligence in academic research has moved from speculative possibility to documented practice in roughly three years. This paper offers a reflexive case study of one such workflow, used to construct an open-source Python pipeline for cross-country M&A risk analysis on 4,689 international transactions covering 2008 to 2025. The workflow combines two complementary AI surfaces – a conversational counterpart for ideation and a literature-aware agent for file-system and code-execution tasks – alongside a retrieval-specialised plugin for systematic literature search.,The paper reports three contributions. The human–AI division of labor is traced across seven release iterations of the pipeline, with each design decision, bug-fix pattern, and validation choice categorised as AI-proposed-and-human-validated or human-proposed-and-AI-implemented. Quantitative outcomes are reported at the dataset level, including a 93.2 percent ticker resolution rate, an 84.0 percent usable-record rate after seven validation tests, and a mean per-record quality score of 88.1 out of 100. The agentic surfaces contributed substantial time savings on tasks within the technological frontier yet introduced characteristic errors that the human orchestration was required to catch.,The case study is anchored in Christensen’s disruptive innovation framework, in the recent literature on agentic AI architectures, and in the methodological reflexive turn in management research. The pipeline, the validation evidence, and the human-AI orchestration log are released as a citable replication package on GitHub and Zenodo.

---

## uid: `doi:10.2139/ssrn.6801118`

- title: Layered Agentic Retrieval: A Publishing Architecture for Agent-Native Web Surfaces
- authors: Francesco Marinoni Moretto
- affiliations: not stated
- posted: 2026-06-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6801118
- keyword hits: agentic, ai agent, retrieval-augmented

### abstract

As AI agents transition from read-only assistants to autonomous actors, the human-readable web is failing them. Current retrofitting approaches, such as schema.org-enhanced HTML or Retrieval-Augmented Generation (RAG), force agents to parse unstructured or weakly-structured corpora or expend finite token budgets on human-centric rendering pipelines. In response, a parallel publishing layer is taking shape: major AI operators — including OpenAI, Anthropic, Stripe, and Google — are increasingly exposing machine-legible surfaces optimized for autonomous traversal, deterministic retrieval, and reduced token consumption. This paper identifies and analyzes this emerging publishing pattern as Layered Agentic Retrieval (LAR). LAR is a publisher-side architectural commitment to surface deterministic, machine-legible data designed explicitly for agent traversal. We articulate LAR's three core commitments — plain-text substrates, progressive disclosure, and workflow-organized hierarchies — and situate it within the lineages of RESTful hypermedia and the Semantic Web. By delineating the limits of current retrofitting approaches, this paper establishes LAR as a dedicated institutional layer through which publishers can expose machine-legible retrieval, policy, and operational surfaces to autonomous agents — the structural artifact onto which cryptographic attestation attaches and on which emerging legal provenance frameworks can operate.

---

## uid: `doi:10.2139/ssrn.6862780`

- title: Knowledge-Driven Reinforcement Learning for Prefabricated Construction Supply Chain Scheduling: A Two-Phase Large Language Model Integration Framework
- authors: Chunlin Wu, Yaxuan Yang, Rundong Xin
- affiliations: not stated
- posted: 2026-06-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6862780
- keyword hits: large language model, llm, retrieval-augmented

### abstract

Prefabricated construction supply chains require coordinated scheduling across production, transportation, and assembly under transport uncertainty, storage constraints, and assembly precedence requirements. However, existing approaches rely on stage-isolated optimization, static heuristics, or black-box AI models that cannot simultaneously ensure engineering feasibility, interpretability, and adaptive decision-making under dynamic operational conditions. To address this problem, this study proposes a knowledge-driven AI framework that formulates the three-stage scheduling problem as a Markov Decision Process and solves it using a Maskable Proximal Policy Optimization agent under a two-phase large language model integration architecture. In the offline phase, engineering constraints are extracted from technical standards and project documents through a retrieval-augmented generation pipeline and embedded into reinforcement learning via action-masking rules. In the online phase, an entropy-triggered LLM consultation mechanism provides interpretable scheduling guidance under high-uncertainty operational states, while a Random Forest classifier generates real-time delay-risk predictions for risk-aware dispatching. Evaluated over 50 episodes across eight combined stress scenarios without retraining, the proposed framework achieves 100% task completion under moderately stressed conditions , whereas a Greedy baseline drops to completion rates as low as 80% under compound pressures. Sensitivity analysis identifies site storage capacity and dispatch batch size as the dominant feasibility determinants. This study contributes a knowledge-driven and constraint-aware AI framework that bridges symbolic engineering knowledge, interpretable reasoning, and adaptive reinforcement learning for industrialized construction logistics, advancing trustworthy and uncertainty-resilient AI decision-making paradigms for complex construction supply chains. The findings provide practical guidance for capacity planning, delivery-rhythm design, and risk-aware coordination in industrialized construction projects.

---

## uid: `doi:10.2139/ssrn.6862081`

- title: A physics-informed residual correction framework for pretrained tabular foundation model based battery health prognostics
- authors: Zhiqiang Li, Liu Teng, Wei Li, Weiwei Huo
- affiliations: not stated
- posted: 2026-06-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6862081
- keyword hits: foundation model, in-context learning

### abstract

Accurate prediction of battery state of health (SOH) and remaining useful life (RUL) is essential for the safe and economical operation of lithium-ion battery systems, yet remains challenging due to complex degradation mechanisms and limited training data. This paper proposes a physics-informed residual correction framework that integrates a pretrained tabular foundation model with physics-informed neural networks for battery health prognostics. The framework operates through three hierarchical layers: a TabPFN prior layer that generates strong initial predictions via in-context learning, a lightweight correction head with zero-initialized output layer that learns the residual between the prior and the true target while preserving the pretrained prior at the start of training, and a multi-granularity physics-informed constraint layer offering a continuous spectrum from purely data-driven to strongly physics-constrained modeling. The framework requires only partial charging data from the 3.5 V to 4.0 V voltage window, generating 12 input features suitable for battery management system deployment. Experiments on three publicly available datasets (CALCE, MICH, SNL_NMC) demonstrate that the proposed TabPFN-DeepHPM achieves the best overall SOH R2 of 0.917 and RUL R2 of 0.873, with SOH RMSE of 0.020 and RUL RMSE of 42.6 cycles. The PINN-only baseline without TabPFN prior yields substantially lower RUL R2 of 0.815, confirming the critical importance of the pretrained prior. Ablation studies reveal that the zero initialization preserves the TabPFN prior at training onset, the 256-neuron correction head achieves Pareto optimality in the accuracy-efficiency tradeoff, and the residual corrections are bidirectional with no systematic bias (SOH correction standard deviation below 0.030 across all datasets).

---

## uid: `doi:10.2139/ssrn.6863640`

- title: AlignPromptGPT: Aligned Prompting for Industrial Image Anomaly Detection
- authors: Qingling Zhao, Kui Zhao, Zonghua Gu
- affiliations: not stated
- posted: 2026-06-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6863640
- keyword hits: large language model, llm, prompting

### abstract

Industrial visual anomaly detection is a key capability for automated quality inspection, yet practical systems must simultaneously localize subtle defects and provide human-interpretable explanations. Recent vision-language pipelines couple a frozen multimodal encoder with a Large Language Model (LLM) to enable joint pixel-level scoring and text responses, but their cross-modal alignment and prompt construction remain lightweight and can lead to ambiguous anomaly maps or unstable "normal/abnormal" decisions. This paper proposes AlignPromptGPT, a lightweight prompt-enhanced framework that preserves the overall AnomalyGPT architecture while improving two critical components. First, an EnhancedLinearLayer augments the original linear projector with a residual non-linear branch, strengthening patch-to-text alignment for fine-grained defects. Second, a PromptMaker compresses intermediate visual features into position-sensitive prompt tokens and introduces an anomaly-aware scaling mechanism, guiding the LLM to focus on defective regions and generate more consistent explanations. Experiments on MVTec AD show that AlignPromptGPT achieves 96.25% I-AUROC and 89.16% P-AUROC, and improves the accuracy of image-level textual judgements to 86.27%. Moreover, the fine-tuned checkpoint is reduced to 20.3 MB, and the inference throughput is improved to 1.57 FPS on a single RTX 4090D. These results demonstrate that AlignPromptGPT delivers accurate, efficient, and interpretable industrial anomaly detection.

---

## uid: `doi:10.2139/ssrn.6864440`

- title: Effects of Usage Goals and Personality Traits on Engagement and Prompting Patterns in Generative AI Use
- authors: Yu  Jun Lee, Jaejin Hwang, Jinwon Lee, Jiyeon Ha, Kellisyn Gersich, Kyung-Sun Lee
- affiliations: not stated
- posted: 2026-06-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6864440
- keyword hits: chatgpt, generative ai, prompting

### abstract

The objective of this study was to examine the effect of individual factors including the primary usage goals and personal tendencies to the engagement level and prompting behavior patterns when interacting with generative AI (Gen AI). Forty university students who already subscribed and actively used ChatGPT 5.0 participated in this study. Three different types of tasks (Task 1: title generation, Task 2: scenario generation, and Task 3: data analysis and visualization) based on varying levels of creativity and complexity were conducted. Questionnaires were conducted to gather individual participants AI usage behaviors and Big Five Personality Inventory. The results showed that participants who primarily used Gen AI for coding exhibited a higher frequency of communication with the AI compared to those using it for other purposes. Especially, users who primarily use Gen AI for coding exhibited a marked difference in keyword usage during Task 3 (Data Analysis and Visualization) compared to non-coding users. As a result of hierarchical clustering based on the Big Five personality traits, the participants were classified into three distinct clusters (Cluster 1: average level, Cluster 2: high extraversion, and Cluster 3: high neuroticism). These different cluster groups based on the personality also exhibited different Gen AI usage patterns. The results suggest that both the user's habitual usage goals and their psychological traits significantly influence their interaction patterns with Gen AI. Future studies could consider a larger and more diverse participant pool to generalize the findings.

---

## uid: `doi:10.2139/ssrn.6801139`

- title: AI Adoption Life Cycle: A Cross-Sector Scientific Synthesis of Market Maturity, Governance, and Strategic Implications
- authors: David Sarikhan
- affiliations: not stated
- posted: 2026-06-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6801139
- keyword hits: agentic, generative ai

### abstract

This paper examines the market position of artificial intelligence (AI) within an adoption life cycle, responding to the practical question of whether AI is still emerging, scaling, maturing, or already entering renewal. Rather than treating AI as a single homogeneous technology, the paper develops a cross-sector synthesis that distinguishes between adoption breadth, deployment depth, lifecycle governance, and adaptive maturity. Evidence from recent adoption surveys and AIindex reports indicates that AI use has become widespread across organizations and households, but enterprise-wide scaling and measurable value capture remain uneven. Accordingly, the paper argues that AI, as a broad market, is best classified as in late growth and scaling, moving into early lifecycle integration and governance. However, specific AI applications occupy different stages of maturity: digital twins, predictive analytics, and process automation are closer to maturity in selected sectors, while agentic AI and frontier generative AI remain closer to experimentation or early growth, despite rapidly growing attention. A five-stage AI adoption life cycle is proposed: design and experimentation; growth and scaling; lifecycle integration and governance; maturity and adaptive intelligence; and reconfiguration or renewal. The paper concludes that the most scientifically defensible answer is conditional: AI is no longer merely introductory, but it is not uniformly mature. Its present position is a distributed, sector-dependent transition from growth to governance-supported maturity.

---

## uid: `doi:10.2139/ssrn.6866864`

- title: From Privacy Self-Management to Accountable Delegation: Policy Responses to User-Facing Generative AI Agents
- authors: Ruoxi Li, Sirui Han, Yi-Ke Guo
- affiliations: not stated
- posted: 2026-06-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6866864
- keyword hits: ai agent, generative ai

### abstract

A user-facing AI agent does not merely answer questions; it may decide what to disclose, which service to choose, and how a person is represented to others. This shift exposes a gap in privacy and AI governance. Privacy policies and notice-and-consent regimes still treat personal data governance largely as disclosure control by individual users, while generative AI agents increasingly mediate decisions, permissions, recommendations, transactions, and reputational signals across platform ecosystems. This article develops a comparative policy analysis of three governance generations: P3P-style machine-readable privacy preferences, notice-and-consent/data protection regimes, and emerging user-facing generative AI agents. The central claim is that generative AI policy must move from privacy self-management to accountable delegation. Existing frameworks, including data protection, AI risk management, platform regulation, interoperability, and information-fiduciary approaches, provide partial tools for agent governance, but they do not fully address delegated authority, agent capture, generated reputational representations, or distributed responsibility. The analysis identifies personal AI agents as a distinct intermediary layer between individuals and platforms and proposes agent-specific extensions to existing frameworks: agent-readable obligations, bounded delegation, conflict controls, agent portability, auditable action logs, contestability, marketplace accountability, and public-interest transparency. The contribution is to reframe personal data governance as the regulation of infrastructures that act, decide, and negotiate in users' names.

---
