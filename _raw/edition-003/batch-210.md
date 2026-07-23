# Classification batch 210 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-210.answer.json` as a JSON array.

---

## uid: `arxiv:2607.01388v1`

- title: RusFinChain: A Russian Benchmark for Verifiable Chain-of-Thought Reasoning in Finance with Fuzzy-Aligned Evaluation
- authors: M. K. Arabov
- affiliations: not stated
- posted: 2026-07-01
- source: arXiv
- link: https://arxiv.org/abs/2607.01388v1
- keyword hits: chain-of-thought, llm, llms

### abstract

Multi-step symbolic reasoning is essential for robust financial analysis, yet most benchmarks neglect intermediate reasoning steps. FINCHAIN introduced verifiable Chain-of-Thought (CoT) evaluation but is limited to English. FINESSE-Bench includes a Russian block but relies on multiple-choice questions without step-level supervision. We present RusFinChain, the first Russian-language symbolic benchmark for verifiable CoT reasoning in finance. It spans 17 domains, 172 topics, and comprises 5,280 parameterized examples from executable Python templates, ensuring contamination-free evaluation. Each example includes a gold-standard reasoning chain with intermediate numeric values for automatic verification. We also introduce enhanced metrics: Fuzzy Numeric Alignment and Soft-Attention Alignment. We evaluate 8 open-weight LLMs on a stratified sample, generating 8,100 responses. Results reveal a substantial reasoning gap: models achieve Hard F1 of ~0.65 for step alignment, but only ~29% of final answers are correct. Our fuzzy and soft metrics show stronger correlation with final-answer correctness (Spearman rho approx 0.48) than the original ChainEval (rho approx 0.38-0.46), demonstrating superior diagnostic power. We release dataset, code, and evaluation framework to foster verifiable financial AI for the Russian-speaking community.

---

## uid: `doi:10.2139/ssrn.7042054`

- title: Regime-Aware Peer Specialization for Robust RAG under Heterogeneous Knowledge Conflicts
- authors: Bo Wang, Huang Heyan, Yaolin Li, Yang-Hao Zhou, Jiahao Teng, Ziyi Yang, Ge Shi, Feng Chong
- affiliations: not stated
- posted: 2026-07-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7042054
- keyword hits: fine-tuning, prompting, qwen, retrieval-augmented

### abstract

Retrieval-augmented generation (RAG) improves language models by grounding generation in external context. However, it can be fragile when the retrieved context conflicts with the model's parametric knowledge. Such conflicts span a reliability spectrum, ranging from reliable and partially reliable evidence to adversarial context. Existing remedies often handle such heterogeneous conflicts with regime-agnostic supervision, which can conflate incompatible learning signals across reliability regimes. To disentangle these signals, we propose RAPS-DA,, a regime-aware peer specialization framework that addresses conflict at two complementary granularities. At the sample level, conflicts are divided into three regimes, including Grounding, Arbitration, and Resistance, with one same-scale peer specialist trained per regime from a shared base model. Each sample is then hard-routed to its regime-matched peer for on-policy reverse-KL supervision. At the token level, a dual-layer selector uses inter-teacher disagreement, student–teacher divergence, and student entropy to filter uninformative or unstable tokens, upweight confidently misaligned ones, and gradually focus supervision on high-conflict tokens as the student matures. Gains stem from specialization at a fixed model scale, not from a stronger teacher, and the peer specialists exist only during training, so the deployed student requires no regime labels or peer access. Experiments on five conflict scenarios and two out-of-distribution benchmarks show RAPS-DA, surpasses all prompting, decoding, fine-tuning, RL, and single-teacher baselines. On Qwen-7B, it achieves the largest gains in the Resistance regime, exceeding the best RL baseline by 11.2 points, and a single 7B student closes 69.6\% of the gap to an oracle regime-matched specialist.

---

## uid: `doi:10.2139/ssrn.6942138`

- title: Trust as a Scarce Resource: Verification Scarcity, the Competence Trap, and the Economics of Governed AI
- authors: Robert Dogonowski
- affiliations: not stated
- posted: 2026-07-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6942138
- keyword hits: ai agent, claude

### abstract

AI capability scales computationally; trust scales institutionally. This paper argues that the binding constraint on safe, deployable AI is not generation capacity but verification scarcity: the capacity to validate AI-mediated outputs grows more slowly than the capacity to generate them. We model an organization that deploys an AI agent and allocates costly verification effort to outputs whose error risk is imperfectly observed. Three results organize the analysis. First, under correct beliefs the optimal verification policy never produces a welfare trap: by the envelope theorem, expected loss is monotone in true risk even when undetected risk is not. Second, when verification responds to perceived rather than true risk, undetected risk rises as reliability improves if and only if the product of two elasticities-detection with respect to verification, and verification with respect to perceived risk-exceeds the odds of non-detection. This competence trap condition corrects and sharpens an inequality used informally in deployment practice. Third, when perceived risk is * I thank seminar participants and practitioner colleagues for comments. This paper is part of a companion series on the organizational economics of artificial intelligence (Dogonowski, 2026a,b,c). AI assistance disclosure: drafting, formalization support, and numerical verification scripts were prepared with the assistance of Anthropic's Claude; all analytical results were independently verified numerically in Python by the author, and all errors remain the author's own. 1 itself generated by detected errors, the model exhibits self-confirming equilibria: a zero-verification equilibrium in which nothing is checked, no errors are found, and no checking appears warranted is locally stable whenever hλ 2 r < κ, a threshold in harm, detection efficiency, true risk, and verification cost. Minimum verification floors and independent audits are shown to bound undetected risk and to eliminate the collapse equilibrium. A trust-state dynamic with asymmetric transitions generates hysteresis and rationalizes pilot-to-production failures, symbolic oversight, and abrupt trust collapses as equilibrium phenomena of a single structural constraint.

---

## uid: `doi:10.2139/ssrn.7044241`

- title: Agentic AI for Knowledge-Driven Hull-Form Design in High-Speed Autonomous Surface Vessels
- authors: Rameen Sheikh, Ashok Kumar, Pavlos Loizou, Agus Hasan, Dong  Trong Nguyen
- affiliations: not stated
- posted: 2026-07-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7044241
- keyword hits: agentic, llm

### abstract

High-speed autonomous surface vessels require hull forms that balance resistance, running attitude, hydrodynamic stability, and mission-related constraints. Computational fluid dynamics (CFD) supports detailed assessment of planing-hull performance, but knowledge generated by individual parametric studies is rarely reused in subsequent design projects. This paper proposes a knowledge-driven agentic AI framework that transforms CFD-derived evidence into reusable design support for early-stage hull-form development.Unsteady Reynolds-averaged Navier-Stokes simulations are conducted for straked-hull configurations, building a database of deadrise angle effects on resistance, trim, sinkage, pressure distribution, and wave characteristics. An LLM-based design manager retrieves relevant historical cases, interprets hydrodynamic trends, evaluates conflicting tool recommendations, and selects candidate deadrise angles through an auditable reasoning trace. The framework integrates case retrieval, Savitsky-based physics priors, Bayesian optimisation, CFD-derived oracle, and episodic reflection, with a human designer retained in the loop. The agent identifies the resistance-optimal deadrise angle using 60% fewer oracle evaluations than an exhaustive parametric sweep at 30 kn. Out-of-library validation at 45 kn confirms the efficiency advantage under genuine extrapolation, locating the optimum after four evaluations versus nine for the exhaustive sweep. The study demonstrates how CFD campaigns can be converted into reusable engineering memory, providing a basis for future agentic hull-form design systems.

---

## uid: `arxiv:2607.02703v1`

- title: LLMoxie: Exploring Agentic AI for Scientific Software Development
- authors: Landung Setiawan, Anant Mittal, Cordero Core, Anshul Tambay, Carlos Garcia Jurado Suarez, David A. C. Beck, Andrew J. Connolly, Vani Mandava
- affiliations: not stated
- posted: 2026-07-02
- source: arXiv
- link: https://arxiv.org/abs/2607.02703v1
- keyword hits: agentic, llm

### abstract

In this paper, we describe LLMoxie, an institutional AI platform whose three-tiered architecture supports multi-cloud and on-premise inference, a LiteLLM/MLflow control plane for authentication, budgeting, PII masking, and observability, and an application augmentation layer for AI coding agents. Layered on top, an open-source RSE-Plugins ecosystem encodes accumulated RSE knowledge as a Plugin-Agent-Skill hierarchy spanning scientific Python practice, domain-specific knowledge, a six-phase research-and-implement workflow, and project lifecycle management. Scientific software is judged less by raw code quality than by whether it can be cited, audited, reproduced, and extended. Off-the-shelf AI coding agents, optimized against commercial software benchmarks, are poorly calibrated for this setting: they ignore the conventions of the scientific Python libraries they invoke, mishandle sensitive or embargoed data, and leave decision trails that are difficult to reconstruct after the fact. We report on twenty months of practice at a university-based research software engineering (RSE) center, where RSEs embedded across astronomy, earth and climate science, agriculture, and health projects worked to close this gap. We characterize the recurring infrastructure, governance, and process challenges of adopting Agentic AI inside a multi-domain RSE center, describe the platform and plugin design, and distill operational lessons from real scientific software deployments. Together, the platform and plugins shift AI coding agents from generic code generators into domain-aware collaborators that respect community norms and produce auditable provenance of technical reasoning.

---

## uid: `doi:10.2139/ssrn.7051818`

- title: EF-LLM: A Continual Learning-Based Framework for AI-Assisted Automation, Enhanced Sparse Prediction, and Hallucination Detection
- authors: Zihang Qiu, Jayashri Ravishankar, Anam Malik, Zhongyang Wang, Renyou Xie
- affiliations: not stated
- posted: 2026-07-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7051818
- keyword hits: fine-tuning, large language model, llm

### abstract

Accurate prediction helps achieve supply-demand balance in energy systems, thereby supporting operational decision-making and scheduling. Traditional models, which lack AI-assisted automation, often rely heavily on expert knowledge, incur high labor costs, and perform poorly under sparse-data conditions. To address these challenges, this work proposes an Energy Forecasting Large Language Model (EF-LLM), which integrates domain knowledge and temporal data for time-series forecasting while supporting both pre-forecast operations and post-forecast decision-making. EF-LLM’s human–artificial intelligence (AI) interaction capabilities further lower the entry barrier for forecasting tasks and reduce the need for additional expert involvement. To support these functions, a continual learning framework with updatable Low-Rank Adaptation (LoRA) and a multi-channel architecture is developed to align heterogeneous multimodal data, enabling EF-LLM to continuously acquire and adapt multimodal knowledge. In addition, EF-LLM improves prediction accuracy under sparse-data conditions by leveraging its ability to process and fuse multimodal information. A Fusion Parameter-Efficient Fine-Tuning (F-PEFT) method is further introduced to effectively exploit both time-series data and textual information. EF-LLM is also the first energy-specific LLM to detect hallucinations and quantify their occurrence rate, achieved via multi-task learning and semantic similarity analysis. This work has achieved success in energy prediction scenarios for load, PV, and wind power forecast.

---

## uid: `doi:10.2139/ssrn.7065060`

- title: CPT-Seg: A Crack Pattern Transfer-Enhanced Two-Stage Transfer Learning Framework for Generalizable Crack Segmentation
- authors: Pengwei Guo, Xiao Tan, Sandra  Barbosa Nunes, Neil Yorke-Smith, Xugang Hua, Yi Bao
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7065060
- keyword hits: fine-tuning, generative ai

### abstract

Deep learning-based crack segmentation is often limited by scarce annotated data and the limited controllability of existing augmentation methods. To address these challenges, this study proposes CPT-Seg, a unified framework that integrates controllable crack pattern transfer with downstream crack segmentation. A crack pattern transfer module is developed to decouple crack geometry from surface texture through mask-guided fusion, Stable Diffusion Inpainting, and LoRA fine-tuning, enabling realistic crack generation on diverse surfaces while preserving geometric fidelity. The generated images are incorporated into a two-stage transfer learning strategy, where synthetic crack images are used for pre-training and real annotated images for fine-tuning. Experimental results demonstrate that the proposed crack pattern transfer approach achieves a PSNR of 18.22 dB, SSIM of 0.550, LPIPS of 0.351, and FID of 134.74, demonstrating strong image quality and structural consistency. When applied to crack segmentation, the data generated improved the IoU from 88.0% to 88.9% and the F1-score from 92.5% to 93.5% compared with training on real data alone. Cross-dataset validation further confirms robust generalization across concrete and pavement crack datasets. The proposed framework provides an effective solution to alleviate data scarcity and dataset bias, bridging generative AI and vision-based structural health monitoring.

---

## uid: `doi:10.2139/ssrn.6976218`

- title: Context Collapse in Long-Horizon Agents: Benchmarking Hierarchical Memory against RAG and Summarization
- authors: Ebaad Raheem
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6976218
- keyword hits: large language model, llm, retrieval-augmented

### abstract

Autonomous Large Language Model (LLM) agents that operate over long conversations face a critical weakness: context collapse, where factual details gradually drift and similar meanings interfere, weakening the agent's ability to track its own state. This letter presents a carefully controlled benchmark of four memory designs; Baseline (full, untruncated history), Rolling Summary (repeated summarization of the dialogue), Retrieval-Augmented Generation (RAG), and a Hierarchical Memory system; evaluated across 800 fully reproducible conversational runs covering Legal, Medical, Tech, and Travel domains. Key facts are inserted at turn one and queried at five fixed recall distances using a two-level evaluation method that prevents the judge model from hallucinating. The Hierarchical architecture reaches an overall Factual Retention Rate (FRR) of 41.6%, performing competitively with the Baseline (40.6%) while using 34.8% fewer context tokens. RAG and Rolling Summary achieve 37.9% and 31.0%, respectively. Rolling Summary reduces context tokens by 60.5% but raises LLM API calls by roughly 205%, making it both expensive and harmful to performance. A strong primacy effect appears across all architectures as the conversation grows: at medium lengths (distances 14-19) retention becomes erratic (Baseline FRR falls to 39.0%), but then retention paradoxically jumps to 55.0% at maximum length, as attention locks tightly onto the start of the prompt. Domains differ sharply in fragility; the Medical domain collapses to a Baseline FRR of 12.0% and generates 192 explicit refusals under Rolling Summary, whereas Legal sustains 88.8%. These findings show that even with the full conversation history available, the Baseline essentially ties with hierarchical memory (40.6% vs. 41.6%, p = 0.31), yet domain collapse (Medical 12.0%) remains. Full context alone is not enough; memory structured at multiple levels offers greater resilience.

---
