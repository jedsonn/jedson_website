# Classification batch 8 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-8.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7312838`

- title: Task-Specific Full Fine-Tuning for Retrieval-Augmented Generation A Controlled Cross-Family Empirical Study of Open-Weight Large Language Models
- authors: Sascha Frank, Rawel Singh
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7312838
- keyword hits: fine-tuning, large language model, large language models, llama, qwen, retrieval-augmented

### abstract

Retrieval-Augmented Generation (RAG) depends not only on retrieval quality but also on the generator's ability to use supplied evidence, abstain when support is insufficient, and follow task-specific output requirements. While prior work has shown that such behaviours can be improved through targeted adaptation, less is known about how the same RAG-specific training corpus affects different model families and parameter scales. We conduct a controlled empirical study of task-specific full fine-tuning across ten open-weight model configurations from the Gemma, Llama, and Qwen families, ranging from approximately 0.5B to 14B parameters. All models are exposed to the same fixed German-language training corpus and evaluated in a paired base-versus-fine-tuned design on identical test instances. Fine-tuning improves the aggregate benchmark score for all ten configurations, but the magnitude and distribution of gains vary substantially. The strongest and most consistent improvement occurs in hard-negative handling, whereas grounded question-answering scores decrease for nine of ten fine-tuned models under the benchmark metric. Structured output and citation behaviour generally improve, but not uniformly. Within the Qwen family, model size is associated with stronger absolute performance but not with larger fine-tuning gains, and several smaller fine-tuned models outperform larger untuned models from the same family on the evaluated task distribution. These results support interpreting task-specific full fine-tuning as behavioural adaptation rather than uniform capability enhancement. Model size, base performance, final task performance, and adaptation gain should therefore be treated as distinct considerations when selecting and adapting generators for specialized RAG systems.

---

## uid: `doi:10.2139/ssrn.7327622`

- title: MoTIF+: A Prompt-Enhanced Multimodal Pre-trained Foundation Model for Traffic Event Detection and Understanding
- authors: Zihe Wang, Zhiyong Cui, Zikang Yang, Ziru Li, Haiyang Yu, Yilong Ren
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7327622
- keyword hits: foundation model, large language model, large language models, llm

### abstract

Traffic event detection and understanding are essential for highway management, but remain challenging due to complex dynamics, limited incident samples and uncertainties. Traditional neural networks focus mainly on local target detection and rule-based incident judgement, showing weak global perception. Multimodal large language models enhance scene understanding but remain constrained by spatial perception and event judgement. This study proposes MoTIF+ as a prompt enhanced multimodal pre-trained foundation model for traffic event detection and understanding to address these limitations. MoTIF+ builds a basic LLM through self supervised and unsupervised pre-training paradigm using highway related knowledge. Highway video question-answer data are used for multimodal instruction tuning, where Q-Former aligns video representations with semantics and Q-LoRA enables efficient adaptation. An optimized YOLO performs traffic detection and preliminary judgement. To coordinate detection and analysis, we propose Evidence Prompt Fusion (EPF), which converts categories, boxes, scores, and hypotheses into structured prompts and region-aligned evidence tokens. EPF introduces visual evidence as verifiable constraints to support reasoning over video, media, and evidence for secondary verification and standardized analysis. Experiments on highway videos show that MoTIF+ achieves an accuracy of 85.36% and an F1-score of 86.43%, outperforming representative multimodal video understanding baselines. With 39.2 ms latency, MoTIF+ is practical for real-time supervision and provides an interpretable framework for highway detection and understanding.

---

## uid: `doi:10.2139/ssrn.7328911`

- title: LLM-Guided Heterogeneous Graph Meta-Learning for Few-shot Automated Feature Selection
- authors: jian wang, tianjiao xie, junhua fei, xiao li
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7328911
- keyword hits: large language model, large language models, llm, llms

### abstract

In high-risk cold-start decision-making tasks, feature selection under small-sample conditions is prone to dual disturbances from statistical noise and semantic bias in large language models (LLMs). To address this challenge, we propose LLM-MetaFS, a novel framework that maps LLM semantic logic and data-driven statistical correlations into a dual-path topology to construct a Heterogeneous Meta-Feature Graph (HMFG), enabling joint modeling of feature redundancy and complex interdependencies. We further design the ContextFormer network, which employs an asymmetric mask and a topology-value space smoothing mechanism to enforce causal information propagation. Additionally, we introduce a task-driven cross-attention modulation module (TD-CAM) to dynamically balance knowledge priors and statistical evidence, effectively suppressing spurious correlations and correcting semantic deviations. Finally, the model achieves zero-shot transfer via cross-domain meta-training, functioning as a plug-and-play component seamlessly integrable into AutoML pipelines. Extensive experiments on ten high-risk domain datasets demonstrate that LLM-MetaFS substantially outperforms several state-of-the-art baselines, with an average improvement of 11.40% in classification tasks and a 22.40% reduction in regression prediction error, confirming its robustness and effectiveness under cold-start scenarios.

---

## uid: `doi:10.2139/ssrn.7311959`

- title: Adaptive Artificial Intelligence Learning Platform With Dynamic Roadmaps: An Architectural Proof-of-Concept
- authors: Antonio Sulistio
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7311959
- keyword hits: claude, gemini, generative artificial intelligence, llm

### abstract

Conventional Learning Management Systems (LMS) force all students through a single, static instructional sequence regardless of prior knowledge or learning pace, causing student disengagement and elevated attrition rates. While predictive AI approaches dynamically re-route static materials, they are constrained by fixed content repositories. This paper presents an architectural proof-of-concept for an adaptive web-based platform that utilizes Generative Artificial Intelligence (GenAI) to construct, evaluate, and re-author personalized educational roadmaps in real time. The platform integrates a diagnostic pre-test with response integrity filtering, an 80% mastery cri- terion gate, and a two-stage remediation protocol (Tier-1 micro simplification and Tier-2 macro-syllabus reconstruction). Built on Next.js 14, PostgreSQL, Redis, and BullMQ, the system implements a dual-model LLM failover architecture (Gemini 3.1 Flash primary with Claude 4.5 Haiku fallback) to ensure reliability. In an empirical evaluation of 13 filtered learner sessions, 11 sessions achieved positive cognitive growth measured by Hake’s Normalized Gain (μ = 0.674, SD = 0.321), yielding an 84.6% progression rate. While preliminary findings confirm functional viability, we acknowledge limitations including sample size constraints, absence of a control group, and potential Hawthorne effects. We outline enterprise integration pathways via IMS LTI v1.3, cognitive load fatigue mitigation, and a framework for future randomized controlled trials. Index Terms—Adaptive learning, artificial intelligence, dynamic roadmaps, learning management systems, mastery learning, remediation protocols, zone of proximal development, educational technology.

---

## uid: `doi:10.2139/ssrn.7325082`

- title: Evolution Pathways of LLM-Based Multi-Agent Collaboration Systems and a Four-Layer Reference Architecture for Financial Intelligence Applications
- authors: Zhiming Chen
- affiliations: not stated
- posted: 2026-08-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7325082
- keyword hits: large language model, large language models, llm, llms

### abstract

The rapid advancement of Large Language Models (LLMs) has accelerated the adoption of Multi-Agent Systems (MAS) as a dominant paradigm for tackling complex, multi-step tasks. In highstakes domains such as finance, MAS architectures offer unprecedented capabilities in quantitative strategy development, investment research, and trading-system validation. This paper is positioned as a Reference Architecture Proposal with Evolution Taxonomy and Synthesized Empirical Analysis. It makes three principal contributions. First, we propose a four-stage evolution model synthesizing the development trajectory from 2023 H2 to 2026 H1, charting the progression from SOP-encoded frameworks (MetaGPT) through role-plus-tool coordination (CrewAI, AutoGen) and state-managed systems (LangGraph) to the emerging Agent Operating System paradigm (PilotDeck, AgentOS). Second, we introduce a four-layer reference architecture (L1 Model, L2 Capability, L3 Collaboration, L4 Governance) that explicitly captures governance responsibilities-permissions, audit, compliance, and failure recovery-which are systematically absent in existing frameworks. To the best of our knowledge, this is the first work to formalize Governance (L4) as a mandatory, runtimeenforced architectural layer specifically for high-stakes MAS deployments. Third, we instantiate the architecture in three end-to-end financial applications: quantitative strategy research-and-development, investment-research document generation, and trading-system testing and validation. Empirical results from real-world deployments and reproduced benchmarks demonstrate that the L4 governance layer is necessary to address 76.5% of system failures identified in the MAST taxonomy (system design 44.2% and inter-agent non-coordination 32.3%); the original Golchian (2026) benchmark reports that LangGraph outperforms competing frameworks by 4 to 13 percentage points on complex tasks (>7 steps), as reproduced here under the original authors' experimental setup; and that homogeneous multi-agent debate incurs 2.1 to 3.4 times the token cost of isolated self-correction without accuracy gains. These metrics are intended to illustrate the architectural impact of the L4 layer, not to claim production-grade deployable alpha. We further propose a seven-dimensional evaluation framework encompassing task completion, communication cost, context drift, and four financialperformance metrics, providing a reproducible basis for future empirical work. All architectural diagrams, evaluation templates, and L4 component interaction patterns are released under an opensource license at https://github.com/gtht-fintech/llm-mas-finance-architecture to facilitate replication and extension.

---

## uid: `doi:10.2139/ssrn.7287450`

- title: When RAG Hurts: Retrieval-Augmented Generation Degrades Performance in Metallurgical Root Cause Analysis
- authors: Ahmad Ridwan Fauzi, Sendi  Nugraha Pratama, acep purqon, Yumna  Zahran Ramadhan, Muhammad Ardiansyah
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7287450
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Metallurgical failure analysis requires deep domain expertise to identify root causes from complex material evidence. This study evaluates the capability of large language models (LLMs) to perform automated root cause analysis in metallurgical failure cases, with and without retrieval-augmented generation (RAG). A dataset of 195 failure analysis papers spanning nine metallurgical failure categories was constructed, each containing expert-extracted input narratives and ground truth root cause descriptions. Three configurations were evaluated: non-RAG (no retrieval), default RAG (unfiltered), and filtered RAG (deduplicated corpus), with the non-RAG versus filtered RAG comparison performed across three LLMs. For the primary analysis model (MiMo-v2.5), non-RAG achieved 75.9% CORRECT verdicts versus 63.1% for filtered RAG, a 12.8 percentage point decrease (p

---

## uid: `doi:10.2139/ssrn.7287387`

- title: OpenAI API compatible AI Inference Service support in HPC environment
- authors: Adam Matuš, Tomáš Martinovič, Arif  Görkem Özer, Jakub Konvička, Firat Cekinel, Pinar Karagoz, Ismail  Hakki Toroslu, Jakub Krejčí
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7287387
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Driven by the rise of Artificial Intelligence (AI) and Large Language Models (LLMs), the demand for high-density GPU resources has escalated significantly. High-Performance Computing (HPC) centers possess the necessary hardware, yet their conventional infrastructure and software ecosystems make hosting user-friendly AI services highly complex. This paper presents an innovative inference service designed specifically for HPC environments. By integrating batch scheduling, strategic project pre-allocations, and the High-End Application Environment (HEAppE) middleware, the service exposes a seamless, cloud-like Application Programming Interface (API) for LLMs, which can also be extended for broader AI inference tasks including agentic AI. To support common generative use-cases, such as text-to-text or image-to-text tasks, the service is designed to be fully compatible with the industry-standard OpenAI API. We evaluate the performance of this solution using standardized benchmarks against a bare-metal baseline to demonstrate its minimal orchestration overhead. This service has been developed within the scope of the Horizon Europe project EXA4MIND.

---

## uid: `arxiv:2608.15673v1`

- title: PL-Guard: Probabilistic Logic Reasoning for LLM Guardrails
- authors: Satchit Chatterji, Shihan Wang, Giovanni Sileno, Erman Acar
- affiliations: not stated
- posted: 2026-08-16
- source: arXiv
- link: https://arxiv.org/abs/2608.15673v1
- keyword hits: large language model, llm, prompting, qwen

### abstract

Large language model guardrails can be viewed as policy-consistency problems: a system must determine which policy-relevant facts hold in a prompt-response pair and what those facts imply under a given policy. Common approaches, including policy prompting and LLM-as-a-judge pipelines, often overlap the tasks of semantic grounding and policy reasoning: the model both interprets the prompt-response pair and reasons about whether a policy has been violated. This can lead to unsafe compliance with harmful prompts, or refusals to assist benign ones. To separate grounding and reasoning roles, we propose PL-Guard, a neurosymbolic guardrail architecture. Using a symbolic policy interface consisting of predicates and ProbLog rules, a local LLM grounds prompt-response pairs into predicate probabilities using renormalized True/False token scores, while ProbLog performs explicit probabilistic rule inference over the symbolic policy. On the XSTest benchmark, an offline Qwen-based evaluator finds that PL-Guard with a hand-curated policy reduces unsafe compliance from 22.0% for the base model to 0.5%, and below the 6.0% rate of an LLM-as-a-judge baseline. This comes at the cost of higher over-refusal than the LLM-as-a-judge baseline, 14.4% versus 5.2%. These results suggest that separating neural grounding from probabilistic symbolic reasoning can expose the safety-helpfulness tradeoff while making the guardrail's intermediate reasoning steps explicit and auditable.

---
