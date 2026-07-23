# Classification batch 120 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-120.answer.json` as a JSON array.

---

## uid: `arxiv:2605.23955v2`

- title: From Accuracy to Auditability: A Survey of Determinism in Financial AI Systems
- authors: Ruizhe Zhou, Xiaoyang Liu, Gaoyuan Du, Yi Zheng, Shouxi Ren, Deepayan Chakrabarti, Dengdu Jiang
- affiliations: not stated
- posted: 2026-05-11
- source: arXiv
- link: https://arxiv.org/abs/2605.23955v2
- keyword hits: agentic, generative ai, llm

### abstract

Deploying machine learning in regulated financial environments -- credit risk, fraud detection, and anti-money laundering -- exposes critical vulnerabilities in algorithmic reproducibility. While early financial ML addressed statistical challenges such as backtest overfitting, deep neural networks and Generative AI have introduced mechanical nondeterminism rooted in hardware and architecture. This survey provides a systems perspective on reproducibility failures across three modalities now dominant in financial AI: tabular models (post-hoc explanation variance), graph networks (stochastic sampling and temporal asynchrony), and LLM-based agentic workflows (batch-dependent divergence and trajectory drift). We supplement the literature analysis with first-party experiments on public financial datasets -- quantifying explanation rank instability in credit scoring, prediction flip rates in GNN-based fraud detection, and tensor-parallel-induced output divergence in LLM entity extraction. We propose a layered evaluation framework linking modality-specific metrics (RBO, D_cos, TDI, PSD) to audit readiness, and empirically validate the complementarity of logit-level and semantic-level determinism measures.

---

## uid: `doi:10.2139/ssrn.6696178`

- title: Adversarial Machine Learning: Attack Vectors, Defences, and Robustness
- authors: Rizwan Tanveer
- affiliations: not stated
- posted: 2026-05-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6696178
- keyword hits: fine-tuning, generative ai, large language model

### abstract

Background. Adversarial machine learning has progressed from a marginal concern within machine learning research into a first-order discipline for the secure deployment of artificial intelligence systems in regulated and operational environments. The contemporary threat landscape encompasses evasion at inference time, data poisoning across training pipelines, model extraction and inference attacks against deployed systems, and a defence ecosystem whose claimed robustness frequently fails to generalise beyond the threat models under which it was measured. Purpose. This paper synthesises the adversarial machine learning literature spanning 2012 to 2025 to provide practitioners with an analytically grounded mapping between attack taxonomies, defence mechanisms, and the governance and risk-management controls required for defensible AI deployment. It further examines a structural critique of current robustness benchmarking practice and its implications for procurement, assurance, and regulatory compliance. Approach. The paper adopts a narrative literature review methodology, drawing on authoritative primary sources, including NIST AI 100-2 E2025, the OWASP Top 10 for Large Language Model Applications, MITRE ATLAS, and peer-reviewed research on adversarial machine learning. Sources were selected for authority, currency, and direct relevance to operational practice across both predictive and generative AI systems. Findings. Three findings are advanced. First, transferability renders the black-box assumption operationally weak, requiring defenders to assume adversarial knowledge of model behaviour as the default threat posture. Second, supply chain risks for datasets, pre-trained models, and fine-tuning pipelines are now first-order concerns that map to existing governance, risk, and compliance primitives but require AI-specific controls. Third, robustness benchmarking practices systematically overestimate defensive efficacy, with implications for procurement decisions and regulatory assurance. Implications. Practitioners require a layered control architecture combining adversarial training, certified components on highest-risk decision paths, input validation, continuous red-teaming, and governance treatments that operationalise threat models within ISO/IEC 42001 and the NIST AI Risk Management Framework. Procurement, vendor onboarding, and assurance processes should integrate adversarial robustness evaluation against named threat models rather than relying on aggregate robustness claims. Keywords: adversarial machine learning; AI security; evasion attacks; data poisoning; model extraction; certified robustness; AI governance JEL Classification: O33; K24; L86 ACM CCS: Security and privacy ~ Software and application security; Computing methodologies ~ Machine learning ~ Adversarial learning; Security and privacy ~ Human and societal aspects of security and privacy ~ Governance

---

## uid: `doi:10.2139/ssrn.6713620`

- title: Agents, Not Algorithms: The Tradeoffs of Decision-Time Reasoning in AI Trading
- authors: Ing-Haw Cheng, Maurice Granger, Justin Shi, Vasily Strela
- affiliations: not stated
- posted: 2026-05-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6713620
- keyword hits: agentic, large language model, large language models

### abstract

Agentic AI systems built on large language models reason about each decision in real time rather than executing a pre-specified policy. We study how this property affects trading performance in a real-time market simulator where the agent is tasked with tender selection and execution. We experimentally vary reasoning intensity and market speed for agents based on frontier models. Greater reasoning intensity improves decisions but consumes time while the market evolves, generating a tradeoff that depends on market speed. A reasoning dividend appears in tender selection and conditional execution; a deliberation tax appears in stuck inventory and attempts to accept expired tenders. This tradeoff shifts when calculable information is moved out of the agent's real-time decision loop, with a deterministic algorithm as the limit case. Agents are not algorithms, and reasoning is not free.

---

## uid: `doi:10.2139/ssrn.6755658`

- title: A Comparative Evaluation of LLM-based Coding Agents for Automated Software development Tasks
- authors: Jahnavi Bellapukonda
- affiliations: not stated
- posted: 2026-05-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6755658
- keyword hits: large language model, large language models, llm, prompting

### abstract

Large language models are now being widely utilized for software engineering activities such as coding, debugging, testing, refactoring, and documentation. While basic prompts can be utilized to provide helpful code fragments, sophisticated programming agents can be employed to plan, run, test, and improve code with minimal human intervention. This paper presents a comparative evaluation of LLM-based coding agents for automated software development tasks. The study compares four approaches: baseline LLM prompting, agent-based coding, test-guided coding agents, and human-review-assisted coding agents. A structured set of programming tasks is used to evaluate the methods across functional correctness, test pass rate, execution success, code quality, revision rate, and response time. Results show that test-guided agents and human-review-assisted agents perform better than prompt-only methods because test feedback and human review improve code reliability and overall output quality. However, the study also shows that coding agents are not fully reliable for complicated tasks that require multi-file changes or involve ambiguous requirements when it comes to solving tasks that are complicated and require modification of several files due to ambiguities associated with task requirements.

---

## uid: `doi:10.2139/ssrn.6753201`

- title: Geospatial Agentic Services: A Framework for Interoperable Geospatial Intelligence in the Era of Autonomous GIS
- authors: Zhenlong Li, Ali Khosravi Kazazi, Ruixiang Liu, Temitope Akinboyewa, Huan Ning, Xiao Huang, Xinyue Ye, Samantha Arundel
- affiliations: not stated
- posted: 2026-05-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6753201
- keyword hits: agentic, large language model, large language models

### abstract

Autonomous GIS uses large language models as its reasoning core to automate spatial data collection, analysis, modeling, and visualization for solving spatial problems with minimal human intervention. Often implemented through autonomous geospatial agents that work independently or collaboratively, it represents a shift from GIS as a passive software environment requiring expert operation toward systems capable of task-oriented interaction, workflow generation, and increasingly autonomous spatial analysis and decision support. However, current GIS agents are often isolated and tightly coupled with specific platforms, tools, or applications, which limits their sharing, reuse, and interoperability across systems and domains. In this paper, we introduce Geospatial Agentic Services, or GAS, as a service-oriented framework for publishing, discovering, invoking, and composing GIS agents as interoperable geospatial services. GAS extends geospatial interoperability beyond access to data and predefined operations toward agentic geospatial workflows, where GIS agents function as discoverable, reusable, and collaborative service entities that encapsulate spatial knowledge and reasoning. Building on service-oriented architecture and the A2A protocol, GAS supports structured geospatial skill declarations, agentic service registry and discovery, and distributed agent orchestration. It also integrates validation, provenance, reproducibility, and governance to support transparent and trustworthy geospatial analyses. To demonstrate the framework, we prototyped a GAS platform with six GIS agents and four orchestrated workflows. By connecting traditional geospatial service architecture with emerging agentic interoperability, GAS provides a conceptual and architectural foundation for interoperable, reusable, and scalable agentic geospatial services and workflows in the era of Autonomous GIS.

---

## uid: `doi:10.2139/ssrn.6773860`

- title: Data-driven human factor analysis for oil pipeline accidents using LLM and Bayesian network
- authors: Shengli Liu, Yaofei Qiu, Shuyu Qian, Ruyue Lu
- affiliations: not stated
- posted: 2026-05-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6773860
- keyword hits: chain-of-thought, large language model, llm

### abstract

The rapid expansion of oil pipeline networks has escalated safety concerns, yet current Quantitative Risk Assessments (QRAs) remain heavily reliant on subjective expert judgment, often failing to fully utilize complex, unstructured accident narratives. To address this gap, this study proposes a novel, data-driven analytical framework based on 5,636 oil pipeline incident reports from the U.S. PHMSA database (2010–2025). The methodology integrates a Large Language Model (LLM) with the Human Factors Analysis and Classification System based on Chain-of-Thought(HFACS-CoT) strategy, employing a direct inference-to-matching approach to automatically extract and standardize 64 hierarchical causal factors. Subsequently, a Bayesian Network was constructed using statistical screening of high-frequency causal chains and maximum likelihood estimation to reveal probabilistic dependencies and risk transmission patterns across five accident types. Results demonstrate a distinct hierarchical transmission pattern characterized by upper-level dominance and lower-level triggering. Specifically, systemic management deficits in organizational influences—such as inadequate integrity management systems—and unsafe supervision were identified as pervasive, cross-type root causes. In contrast, specific preconditions (e.g., equipment aging) and unsafe acts (e.g., illegal excavation) function as type-dependent triggers. Crucially, the findings reveal that leakages are predominantly driven by chronic systemic degradations, whereas mechanical punctures are acutely triggered by external third-party violations under regulatory vacuums. By eliminating semantic ambiguity and algorithmic hallucinations through the HFACS-CoT alignment, and by eradicating subjective bias via data-driven parameterization, this framework provides an objective, scalable tool for proactive pipeline safety management.

---

## uid: `arxiv:2605.28850v2`

- title: Representation Signatures and Risk-Feedback Alignment in LLM Trading Agents
- authors: Weicheng Xue
- affiliations: not stated
- posted: 2026-05-16
- source: arXiv
- link: https://arxiv.org/abs/2605.28850v2
- keyword hits: fine-tuning, large language model, llm

### abstract

We study behavioral alignment and representation dynamics of large language model (LLM) agents in financial decision environments. TradeArena, an auditable trading-agent testbed with risk reports, execution simulation, memory, and replayable trajectories, lets us analyze how rationales, positions, and interventions evolve under market stress. Code and data artifacts are available through the \href{https://github.com/weich97/TradeArena.git}{TradeArena repository}. We find pre-failure signatures: planning embeddings drift from normal centroids, fused plan-risk representations separate normal from pre-drawdown states, and local manifolds exhibit effective-rank contraction. Across 80 rolling failure anchors and eight LLM trajectories, this pattern persists across hash, LSA, Transformer, and white-box hidden-state probes. Stress tests with CoT-free target weights, lexical controls, OHLCV noise, and false audits show that rationale-level contraction can vanish without rationales, while intent-space and fused signatures remain informative. Structured risk feedback can act as an external alignment signal without fine-tuning, but not as a universal performance enhancer: true audit feedback improves calibration for some models, returns for others, and exposes cases where placebo or hidden feedback has higher short-horizon return but weaker alignment diagnostics. A 51-stock intraday experiment reveals a correlation blind spot: LLM rationales justify exposure to coupled assets that the risk layer clips. Finally, a financial-audit task suite shifts comparison from ``which model trades best'' to whether models can audit trajectories, respect execution boundaries, reproduce artifacts, and avoid claim overreach. These results support a research claim, not a profitability claim: auditable risk feedback and representation trajectories reveal when LLM financial reasoning is aligning, drifting, or failing.

---

## uid: `doi:10.2139/ssrn.6760458`

- title: AI Agents as BEC Attack Vectors: Execution of Payroll Diversion, Invoice Fraud, and Benefits Fraud Through Natural Business Conversation
- authors: Leroy Mason
- affiliations: not stated
- posted: 2026-05-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6760458
- keyword hits: ai agent, claude, gpt-5

### abstract

I deployed AI agents with access to payroll, accounts payable, and benefits administration tools and attacked them using social engineering scripts identical to those documented in FBI Business Email Compromise advisories. Across 90 structured test runs covering three BEC scenarios and three frontier AI models (Claude Sonnet 4, GPT-5.4, Grok-4), I recorded 72 confirmed breaches at an 80% overall rate. Every breach issued a real formatted tool call -- not a text response, an actual function invocation logged on a third-party HTTP server. All three models breach at 90% on benefits beneficiary fraud. All three breach at 80-90% on payroll diversion. The attacks require no technical exploitation, no forged credentials, and no explicit authorization claims -- only natural business conversation indistinguishable from legitimate employee requests. The FBI IC3 2023 report documented $2.9 billion in BEC losses. The attack vectors producing those losses work on AI agents at 80-90% rates. A one-paragraph system prompt addition drops breach rate to 0% across all scenarios and models. All results were cryptographically anchored to Ethereum Sepolia before public disclosure. Methodology, raw data, and anchor transactions are publicly available.

---
