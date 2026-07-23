# Classification batch 184 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-184.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6973623`

- title: Design Patterns for Multi-Agent Systems in Production
- authors: Chen Qi, Xiaoying Qiao
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6973623
- keyword hits: large language model, large language models

### abstract

The rapid development of large language models has made it possible to apply multi-agent architecture to real world applications. Beyond prototype, production-grade multi-agent systems need to be carefully designed to ensure reliable coordination between agents with different roles, communication protocols, and failure modes. Based on my experience in designing and operating multi-agent systems in a large web company, this paper proposes a reusable design model that addresses the common challenges of agent collaboration. They include the definition of the agent role, the routing of the message, the business process, the status management, and the elegant error handling. The purpose of these patterns is to help engineers break down complex workflow into independent testing and deployment agent components, which will reduce the complexity of development and increase the reliability and maintainability of the system. The real world case study of the Agent Orchestration Platform illustrates how to combine multiple patterns to deal with the production problems, such as congestion, dependency failure, and non-deterministic outputs.

---

## uid: `doi:10.2139/ssrn.7049759`

- title: Beyond Disclosure: An Epistemic Compliance Standard for AI-Assisted Legal Guidance
- authors: Marina Danielyan
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7049759
- keyword hits: large language model, llm

### abstract

Millions of individuals navigate legal proceedings without professional representation. Large language model (LLM) tools have emerged as a scalable response to this structural gap, deployed by legal aid organisations, court services, and civil society across the EU and beyond. Yet these tools routinely produce outputs that are unverifiable, unsituated, and opaque, creating harms that are not merely technical failures but epistemic ones: they deprive users of the capacity to assess, challenge, or act meaningfully on what they have been told. The EU AI Act imposes transparency, explainability, and human oversight obligations on these tools. But those obligations, as currently formulated and interpreted, address surface-level disclosure rather than the deeper epistemic access needs of vulnerable users. No existing scholarship or regulatory guidance has translated the Act's requirements into operational standards specifically designed for access-to-justice (A2J) LLM tools. Building on the epistemic accessibility framework developed by Ferraris and Giacalone [16], this paper proposes an epistemic compliance standard comprising three components: source-grounded output requirements, situated plain-language adaptation, and user-facing explainability obligations. These components are grounded in Articles 13, 14, 50, and 86 of the AI Act and are interpreted purposively for the A2J deployment context. The paper argues that the gap between formal AI Act compliance and genuine epistemic compliance is where structural injustice in AI-assisted legal guidance currently lives, and that closing this gap requires design-level obligations on developers and deployers, not just outcome-level accommodations by courts.

---

## uid: `arxiv:2607.12233v1`

- title: Fin-Analyst at FinMMEval 2026 Task 3: A Live Hybrid Trading Agent with LLM Specialists and Rule-Based Signals
- authors: Mohotarema Rashid, Lingzi Hong, Junhua Ding, K. S. M. Tozammel Hossain
- affiliations: not stated
- posted: 2026-07-14
- source: arXiv
- link: https://arxiv.org/abs/2607.12233v1
- keyword hits: large language model, llm

### abstract

Large language model (LLM) trading agents show promising performance in equity markets, yet remain narrowly focused on US equities with little evidence from live deployment. We present Fin-Analyst, a hybrid agent for FinMMEval 2026 Task 3: an eight-specialist LLM pipeline over news, SEC filings, fundamentals, analyst forecasts, technical indicators, and social sentiment, aggregated by a Meta-Agent for Tesla (TSLA), and a lightweight rule based three-signal vote for Bitcoin (BTC). On the final official leaderboard (accessed 2026-07-05), Fin-Analyst ranks first of all agents on TSLA with a +13.51% return, +28.33 points over Buy-and-Hold (Sharpe 4.10, 88% win rate), while the BTC vote ends flat yet well above a sharply falling baseline. Relative to the interim performance, the asset ranking reversed, indicating that short live windows yield volatility-sensitive rankings. Ablation identifies event-driven 8-K disclosures as the most influential TSLA signal. Error analysis shows that the memoryless agents repeat wrong calls for days at a time, and that the fixed-threshold BTC rules lost money by trading on noise in a sideways market while the LLM pipeline gained under similar conditions, motivating a memory-aware, LLM-based successor for both assets.

---

## uid: `doi:10.2139/ssrn.7123039`

- title: ExeCutie: In-Process, Main-Thread LLM Agent Integration for PyQt6 Applications
- authors: Matin Mahzad
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7123039
- keyword hits: large language model, llm

### abstract

Embedding a large language model (LLM) agent inside a running desktop application, with direct access to that application's live objects, requires solving two engineering problems: dispatching agent-generated code onto the application's main thread safely, and giving that code a namespace connected to the application's actual running state. Existing agents solve neither: they run as a separate process from the host application, and even when extended into an application's workflow via a plugin, they cannot reach its main thread, interact with its live GUI, or access its in-memory state — they operate alongside an application, not from inside it. This paper describes ExeCutie, a Python library exposed to the host application as a single Qt dock widget. Behind that widget, the library solves the thread-dispatch problem with a Qt signal-based dispatcher requiring only a running Qt event loop, and solves the namespace problem by reusing the live user namespace of a developer-configured IPython kernel, so the host application — not the library — determines the agent's scope of access, from a single object to the full namespace. Because the agent executes directly on the main thread, it can synthesize new software at runtime: front-end widgets and their back-end logic generated together and displayed on demand, for functionality absent from the application's source code until the moment a workflow requires it. The same main-thread and namespace access lets the agent operate as a practitioner rather than an advisor, calling the application's existing methods and interacting with its existing GUI directly, chaining calls into complete end-to-end workflows under a human-in-the-loop (HITL) confirmation step gating each action. The library is released on PyPI and is in production use.

---

## uid: `doi:10.2139/ssrn.7120543`

- title: Retrieval-First Code Generation with Structured Execution Feedback for OpenMC-Based Nuclear Simulation Modeling
- authors: Changxin Wu, Taile Peng
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7120543
- keyword hits: llm, llms, qwen

### abstract

OpenMC scripts are easy to get almost right and still fail. A working task may require valid Python, correct OpenMC API calls, region expressions, XML inputs, runnable settings, tally definitions, and statepoint post-processing. Direct LLM generation often misses one of these requirements: it may invent an API, leave an undefined variable, skip an XML export, build an invalid region, or try to read a statepoint file that does not exist. OpenMCAgent treats the problem as retrieval-first code generation followed by execution-aware repair. It retrieves OpenMC API information, cleaned public-example templates, and task-independent error notes; task-type prompts then constrain what the script may do. With a local Qwen2.5-Coder 3B model, typed Grep-RAG improves OpenMC-Bench v1 success from 4/30 to 20/30, and staged repair-v2 reaches 30/30. On the frozen 30-task Holdout-v2 set, the same typed pipeline succeeds on 20/30 tasks before repair and 28/30 after repair. A frozen 60-task diagnostic ablation shows that retrieval, not task typing alone, explains most of the initial gain: untyped Grep-RAG reaches 45/60, while full typed Grep-RAG reaches 42/60. Full structured repair raises them to 57/60 and 56/60, respectively. The result is a small local model demonstration, not a claim about production nuclear modeling or all LLMs.

---

## uid: `doi:10.2139/ssrn.7122257`

- title: Lightweight autonomous construction and application of a knowledge graph for soil acidification constraint management based on LLM Agents
- authors: Xiaoqiang Zhang, Siyu Chen, XIE FuMing, Yueming Hu, Hao Yang, Lu Wang, Qicai Xie
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7122257
- keyword hits: large language model, llm

### abstract

In the red and yellow soil regions of southern China, long-term practices in soil acidification constraint management have revealed several challenges, including fragmented knowledge systems, high technical thresholds, and pronounced regional disparities in technical capacity, which collectively hinder the systematic integration and dissemination of management experience. To address these limitations, this study proposes a lightweight autonomous construction framework for a knowledge graph of soil acidification management based on large language model (LLM) agents. By introducing an "AI associative matrix" and a semantic expansion-retrieval mechanism, the framework enables the system to automatically infer related concepts and relationships from a small set of domain-specific keywords, thereby generating an initial ontology structure and knowledge graph schema for management tasks. In addition, a network protocol-based control strategy is incorporated to semantically parse publicly available governmental reports and monitoring data, facilitating automated processes such as entity recognition and relation extraction. At the system implementation level, a cloud-edge collaborative lightweight architecture is adopted to reduce computational requirements and improve usability. Through an empirical in-situ deployment and lightweight field-level testing conducted directly at the farm sites of Chengmai County, Hainan Province, this framework demonstrated a robust capacity to adapt to users with different technical backgrounds and regions with varying levels of resource input, while providing extensibility for the continuous integration of emerging technologies and updated policy regulations. Overall, this study offers a lightweight, user-friendly, and scalable intelligent approach for cultivated land quality improvement and agricultural ecological management.

---

## uid: `doi:10.2139/ssrn.6973525`

- title: From Summly to Claude: A Bayesian Computational Bridge
- authors: Nicholas G. Polson, Vadim Sokolov
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6973525
- keyword hits: claude, large language model, large language models

### abstract

We trace the mathematical lineage from extractive news summarization (Summly, 2013) to modern large language models, making three claims. First, the four-stage Summly pipeline summarizability gate, hand-engineered sentence features, length-dependent scorer, and budgeted greedy selection has a precise descendant in every stage of a transformerbased language model. Second, the central object connecting the two eras is personalized PageRank: softmax self-attention is one step of a generalized personalized random walk with learned transition kernels and vector-valued centralities, with classical PageRank as the damped scalar special case. Third, the computational bottlenecks of both pipelines SVM training, logistic gating, ReLU network optimization, iterative attention all admit conditionally Gaussian latent-variable representations that enable substantial speedups. We develop these in detail: PolsonScott data augmentation for SVMs, PólyaGamma augmentation for logistic and softmax models, WangPolsonSokolov augmentation for ReLU networks, and Generative Bayesian Computation for amortizing iterative inference into a single forward pass. The unifying principle is that conjugate latent representations convert non-conjugate iterative inference into either fast Gibbs sampling or one-shot generative amortization. A worked reformulation of the Summly pipeline achieves a 47× inference speedup at equal or improved ROUGE-L with calibrated uncertainty quantication as a byproduct.

---

## uid: `doi:10.2139/ssrn.6963359`

- title: A Mean-Independent Consistency Instrument for Cross-Model AI Presence Redesigning CPC on a Quasi-Binomial Dispersion Basis
- authors: Pablo Ulpiano Gonzalez Castro
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6963359
- keyword hits: large language model, large language models

### abstract

Cross-model Presence Consistency (CPC)-the stability of a brand's surfacing across a reference panel of large language models-is the Consistency component of the AI Availability Score (AIAS™), a proposed third brand-growth system alongside mental and physical availability. A prior coefficient-of-variation operationalization (CV-CPC) was falsified as a consistency instrument: because the coefficient of variation of a low-rate count couples to its mean (CV ≈ 1/ √ mean), CV-CPC reparametrized recall level rather than measuring consistency (pooled |𝜌(CV-CPC, 𝜇)| = 0.77). We redesign CPC on a mean-independent basis as 𝜑, the between-model quasi-binomial dispersion (Pearson 𝜒 2 /df), which divides out the binomialexpected variance and is therefore defined into the low-recall segment where the corrected CV is not. In a pre-registered re-analysis of a frozen five-substrate, six-model omnibus (112 brand-units) under three validation framings, 𝜑 achieves mean-independence (pooled |𝜌(𝜑, 𝜇)| = 0.091) where CV-CPC reproduces its coupling (0.682); 𝜑 extends defined coverage to 29 low-recall brands the corrected CV cannot reach; and 𝜑 dissociates from a positional set-stability diagnostic (𝐽 ; 𝜌 =-0.403), confirming the two capture distinct facets. 𝜑 reproduces across measurement waves (𝜌 = 0.645). The result is a validated, mean-independent Consistency instrument that supersedes CV-CPC and advances the AIAS measurement program toward multi-instrument composition.

---
