# Classification batch 414 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-414.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6960301`

- title: Racing Against Automation: Dynamic Incentives When AI Can Preempt the Human
- authors: Ying-Ju Chen, Feng Tian, Yangge Xiao, Yufei Zhu
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6960301
- keyword hits: ai agent

### abstract

Recent advances in artificial intelligence (AI), and AI agents in particular, are reshaping innovation by enabling autonomous search, evaluation, and iteration toward new discoveries. Yet human researchers remain essential in novel and poorly structured settings. A human agent may be more productive but privately chooses effort, creating a moral hazard problem; the AI agent requires no incentives but is costly to operate and can preempt the human agent’s success. This raises a natural question: When, if ever, should the firm race the AI agent against the human agent rather than rely on either one alone? We develop a continuous-time principal–agent model in which a principal draws on both a human agent and an independent AI agent in the search for innovation. We establish that when the AI agent is not cost-effective, the principal never deploys it and relies on human-alone search. In contrast, when the AI agent is cost-effective, a natural conjecture is that the principal should always keep it active as a rival, since it can accelerate breakthroughs and, by threatening to preempt the human agent, strengthen the human agent’s incentives. We show that this intuition can fail: persistent AI rivalry may lower both the human agent’s and the principal’s payoffs relative to human-alone search, so aggressive competition can hurt both parties. Instead, the optimal contract may begin with human-alone search, transition to a human–AI race, and finally switch to autonomous AI search if no breakthrough occurs. Relative to a human–human benchmark, deploying the AI agent alongside the human can also align the preferences of the principal and the focal human agent over whether competition should come from an AI agent or another human. In an extension with imperfect AI-generated outcomes, the optimal contract features time-varying verification. In sum, AI rivalry is a double-edged sword: it can accelerate discovery and discipline human effort, but deploying it too early crowds out valuable human-alone search, so firms may optimally delay it even when the AI is productive.

---

## uid: `arxiv:2607.11433v1`

- title: Omni-Decision: A Progressive Evidence-State Agent System for Omni-Modal QA
- authors: Ming Ma, Yi Zhu, Yiran Zhong, Feida Zhu, Weigao Sun, Junhan Shi, Lingrui Mei, Tianming Yang
- affiliations: not stated
- posted: 2026-07-13
- source: arXiv
- link: https://arxiv.org/abs/2607.11433v1
- keyword hits: agentic

### abstract

Omni-modal evidence-seeking QA requires agents to answer questions whose evidence is sparsely distributed across videos, audio, images, web pages, and computation results. Existing agentic multimodal systems often leave evidence in scratchpads, tool trajectories, or free-form histories, making it difficult to track what has been grounded, what remains missing, and when the evidence is sufficient to answer. We propose Omni-Decision, a training-free evidence-state system that turns omni-modal QA into a query-scoped evidence-closure process. For each query, Omni-Decision maintains a structured evidence state containing confirmed evidence, unresolved conflicts, fact and computation dependencies, and open evidence needs. A shared state view conditions planning, evidence acquisition, validation, repair, and finalization. Heterogeneous observations from media, web, computation, and verification modules are normalized, judged, and committed through deterministic state updates. This design enables targeted evidence acquisition, preserves sparse cross-modal cues, and provides inspectable control over repair and stopping. Omni-Decision achieves 45.6% accuracy on OmniGAIA and 58.3% on WorldSense, improving over the baselines by +27.3 and +30.2 percentage points, respectively. No-state ablations and trajectory audits further support the role of explicit evidence-state control in multi-step omni-modal evidence seeking.

---

## uid: `arxiv:2607.13081v1`

- title: SingGuard-NSFA: Extensible Guardrails for Agentic AI via Generative Reasoning and Real-Time Classification
- authors: SingGuard Team
- affiliations: not stated
- posted: 2026-07-13
- source: arXiv
- link: https://arxiv.org/abs/2607.13081v1
- keyword hits: agentic

### abstract

We present nsfaguard, a guardrail framework for securing agentic AI systems against operational threats, such as prompt injection, sensitive information extraction, malicious code requests, dangerous tool misuse, and resource exhaustion. We first introduce the NSFA taxonomy, which organizes 185 risk variants into a CIA-triad-grounded hierarchy and is cross-validated against three well-established OWASP guidelines. Based on this taxonomy, we construct a benchmark suite spanning 133 languages, comprising over 93K purpose-built samples targeting both user queries and agent responses, along with 3,435 cross-source samples adapted from five public agent-security datasets. To detect these operational threats in practice, we develop a dual-mode approach combining SFT-based generative reasoning for interpretable offline auditing with discriminative classification heads on the frozen backbone, enabling real-time detection at approximately 50,ms. We release four models with 0.8B, 2B, 4B, and 9B parameters, all achieving $\geq$94% F1 on purpose-built benchmarks and surpassing the strongest competing guardrails by 6 to 12 absolute points. On cross-source evaluation, the 9B model attains 91.29% F1 with a more balanced precision--recall trade-off. Moreover, ablation experiments show that classification heads can equip a guardrail with risk detection capabilities beyond its original scope and achieve state-of-the-art performance. These results demonstrate the extensibility of the approach and its generality as a plug-in enhancement.

---

## uid: `doi:10.2139/ssrn.6963200`

- title: Gendered Language in Job Advertisements: A Linguistic Analysis of Bias in Recruitment Discourse
- authors: Roya Samad-Zada
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6963200
- keyword hits: agentic

### abstract

This article examines whether the language used in job advertisements is gender-neutral and discusses the linguistic mechanisms through which bias is produced in recruitment discourse. The starting point of the study is that job advertisements are not merely texts providing technical information about open positions, but also construct, through language, the type of employee that organizations are looking for, the personality traits they value, and the behavioral patterns they associate with the "suitable candidate." Within this framework, the main objective of the article is to identify masculine and feminine connotations in Turkish job advertisements, to reveal in which sectors and professional roles these expressions are concentrated, and to analyze how the texts construct an "ideal candidate" model. The research is designed based on a qualitative research approach; an interpretive method combining document analysis, qualitative content analysis, and discourse analysis has been adopted. The dataset consists of a total of 80 Turkish job advertisements selected from the fields of finance and banking, information and technology, sales and marketing, and administrative support and customer relations. During the analysis process, job advertisements were evaluated under categories such as recurring phrasing, agentic language, communal language, emphasis on leadership and authority, expectation of emotional labor, appearance and representationfocused discourse, and implicit exclusionary indicators. The findings show that masculine-coded qualities such as competition, resultsorientedness, leadership, initiative, high-paced work, and working under pressure are more prominent, especially in technical and managerial positions. In contrast, more communal and feminine-sounding qualities such as communication skills, adaptability, patience, friendliness, orderliness, representation ability, and appearance are more frequently emphasized in customer relations, front office, assistant, and support roles. Furthermore, the study reveals that in many advertisements that do not explicitly specify gender, an implicit but effective exclusionary mechanism operates through phrases such as "young and dynamic team," "adaptability to a fastpaced environment," "flexible working hours," and "will represent the organization well." In conclusion, this article argues that job advertisements are discursive structures that can reproduce gender norms. The study concluded that language recruitment is not merely a matter of corporate style; it is a crucial issue of equality that can impact candidates' sense of belonging, their desire to apply, and their access to the position. Therefore, a more inclusive and thoughtful job advertisement should be considered a factor that can strengthen not only the quality of communication but also fairness and diversity in recruitment processes.

---

## uid: `doi:10.2139/ssrn.7004578`

- title: Tax Incentives and Venture Capital Risk-Taking: Evidence from the QSBS Program
- authors: Murillo Campello, Guilherme Junqueira
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7004578
- keyword hits: prompting

### abstract

Do tax subsidies prompt investors to take on risk? We address this question by looking at investors' responses to changes to the Qualified Small Business Stock (QSBS) program, which reduces capital gains taxes on startup investing. We do so under a framework in which some startup investors — venture capitalists (VCs) — combine outside funding with incentive-based compensation, while others invest their own funds. Using bunching, triple-differences, and matching designs that exploit industry eligibility, investment vintage, and holding-period requirements, we analyze data from 158 thousand investor – firm pairings over two decades. We identify strategic investment timing, with subsidies prompting bunching at tax-eligible holding-period thresholds. Most notably, when and where tax subsidies apply, VCs shift their project selection toward riskier ventures: they invest more in pre-commercial stage startups, become more likely to provide startups with their initial capital, and invest more in startups with pre-existing debt, while becoming less likely to co-syndicate their investments. Tax-subsidized VC-backed ventures show higher failure rates, but on the flip side, attain higher valuations at exit and are more likely to reach "unicorn status." None of these patterns are observed for comparable non-VC investors in startups exposed to the same tax subsidies. Our tests further show that tax incentives lead to reallocation toward more innovative industries, yielding more impactful patents. Our study is the first to show that tax policy can shift entrepreneurial financing toward riskier, more innovative, and valuable startups.

---

## uid: `doi:10.2139/ssrn.6960280`

- title: Context Engineering for Agentic Systems: A Five-Phase Pipeline for Enterprise Repository Knowledge Extraction
- authors: Papa Rao Avasarala
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6960280
- keyword hits: agentic, llm

### abstract

LLM-based coding agents operating at enterprise scale require accurate, structured context about organizational codebases-which repositories exist, what capabilities they expose, how services interconnect, and what APIs are available. We present a five-phase automated enrichment pipeline that constructs this context substrate from raw GitHub repositories: (1) GitHub API crawl with intelligent file prioritization, (2) deterministic metadata extraction via regex and configuration parsing, (3) AST-based code analysis using tree-sitter for endpoint and dependency detection, (4) LLM-based capability summarization with structured output, and (5) vector embedding generation for semantic search. The pipeline processes approximately 900 repositories across 80+ development teams at a Fortune 50 retailer, extracting over 4,400 capabilities, more than 3,300 service dependency edges, and generating 3,072-dimensional embeddings per entry. New repositories are enriched on demand. The system includes monorepo detection that automatically creates sub-application documents, enabling resolution to specific subpaths. Validated by 40+ teams who manually reviewed their own enriched entries, the pipeline achieves approximately 95% accuracy across 60 evaluated repositories, with the 5% miss rate attributable to scan depth limitations. The enriched catalog enables a downstream scope resolution algorithm to achieve 94.6% success across 879 autonomous pipeline executions, demonstrating that accurate context engineering is the critical enabler for agentic software development at enterprise scale.

---

## uid: `doi:10.2139/ssrn.7105498`

- title: The Enforcement Gap: Why Africa's AI Regulations Need Runtime Enforcement
- authors: Oluwajuwon Omotayo
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7105498
- keyword hits: ai agent

### abstract

Africa is not facing an AI regulation gap; it is facing an AI enforcement gap. Nigeria, Kenya, South Africa, and the African Union have all moved quickly on data protection, financial conduct, and AI-specific rules, with real enforcement to back them, including a $220 million penalty against Meta and a ₦766.2 million penalty against MultiChoice Nigeria. At the same time, AI agents are already approving loans, screening transactions, and accessing patient records at production scale, built on frameworks (LangChain, LangGraph, CrewAI, AutoGen) with no built-in awareness of the jurisdiction they operate in. This paper argues that the resulting accountability gap is not a policy problem to be solved with more legislation, but an infrastructure problem, requiring a runtime enforcement layer that evaluates AI agent actions against jurisdiction-specific policy before execution. Drawing on firsthand experience translating Nigerian, Kenyan, and South African regulatory frameworks into machine-checkable policy, including a contribution merged into Microsoft's Agent Governance Toolkit that was outdated by a change in Nigerian law eight days later, the paper documents where legal requirements map cleanly onto code, where they don't, and what an operative runtime enforcement model looks like in practice. It closes with specific recommendations for developers, fintechs, and regulators, including the African Union's Continental AI Strategy Phase 2.

---

## uid: `doi:10.2139/ssrn.7112938`

- title: Multi-Agent Reinforcement Learning with Biological Graph Architecture (BDH) for Multi-Echelon Supply Chain Optimization Under Disruptions
- authors: Thanh Nguyen Nhat
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7112938
- keyword hits: chain-of-thought

### abstract

Managing a multi-echelon supply chain under demand volatility and disruption risks is a complex sequential decision-making problem. Current Deep Reinforcement Learning (DRL) models relying on Multi-Layer Perceptrons (MLP) or Graph Neural Networks (GNN) often struggle to capture complex network topologies or suffer from oversmoothing and scalability issues in large-scale graphs. To overcome these limitations, this research proposes a novel Multi-Agent Reinforcement Learning (MARL) framework integrating Proximal Policy Optimization (PPO) with the Dragon Hatchling (BDH) architecture as the core policy network. BDH is a biologically inspired, scale-free network model that leverages local neuron interactions and Hebbian working memory. By modeling a two-echelon supply chain environment subject to stochastic demand and lead-time disruptions, the proposed BDH-PPO model enables agents to autonomously reason and adapt to supply shocks without relying on computationally expensive chain-of-thought processes. Through rigorous simulation, we demonstrate that the BDH-PPO model converges faster and outperforms static inventory policies (e.g., base-stock, (s, Q)) in minimizing total operational costs while effectively dampening the Bullwhip Effect. Current State of the Art (The Gap): While Transformer-based models and traditional RL have been extensively used, BDH represents a novel "post-Transformer" architecture. To date, no existing Q1/Q2 Scopus literature has published the direct integration of BDH as the Policy Network in a MARL framework for supply chain inventory control. This project aims to be the pioneer in translating BDH's cognitive reasoning capabilities from NLP tasks into the domain of Control and Logistics.

---
