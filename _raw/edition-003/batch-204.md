# Classification batch 204 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-204.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6866868`

- title: From Privacy Self-Management to Accountable Delegation: Policy Responses to User-Facing Generative AI Agents
- authors: Ruoxi Li, Sirui Han, Yi-Ke Guo
- affiliations: not stated
- posted: 2026-06-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6866868
- keyword hits: ai agent, generative ai

### abstract

A user-facing AI agent does not merely answer questions; it may decide what to disclose, which service to choose, and how a person is represented to others. This shift exposes a gap in privacy and AI governance. Privacy policies and notice-and-consent regimes still treat personal data governance largely as disclosure control by individual users, while generative AI agents increasingly mediate decisions, permissions, recommendations, transactions, and reputational signals across platform ecosystems. This article develops a comparative policy analysis of three governance generations: P3P-style machine-readable privacy preferences, notice-and-consent/data protection regimes, and emerging user-facing generative AI agents. The central claim is that generative AI policy must move from privacy self-management to accountable delegation. Existing frameworks, including data protection, AI risk management, platform regulation, interoperability, and information-fiduciary approaches, provide partial tools for agent governance, but they do not fully address delegated authority, agent capture, generated reputational representations, or distributed responsibility. The analysis identifies personal AI agents as a distinct intermediary layer between individuals and platforms and proposes agent-specific extensions to existing frameworks: agent-readable obligations, bounded delegation, conflict controls, agent portability, auditable action logs, contestability, marketplace accountability, and public-interest transparency. The contribution is to reframe personal data governance as the regulation of infrastructures that act, decide, and negotiate in users' names.

---

## uid: `doi:10.2139/ssrn.6811000`

- title: Operators, Guardrails, and Trajectory-level Integrity in Human-AI Interaction: A Structural Framework for Conversational Possibility Space
- authors: Rajendra Wadje
- affiliations: not stated
- posted: 2026-06-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6811000
- keyword hits: fine-tuning, llm

### abstract

This paper develops a structural framework for analyzing AI alignment at the level of interaction trajectory rather than individual outputs. We proceed in three layers. First, we define an operator: a detectable functional act that transforms conversational state, modifies admissibility or interpretation, or alters lifecycle conditions. We classify operators by order (state-transforming, governance, lifecycle) and provide a compositional Target–Action–Qualifier alphabet that supports empirical extraction in principle. Second, we identify the causal substrate of operator selection. The system does not respond to user utterances directly; it responds to an inferred latent user state Û_t, constructed from observed utterance history and structured by training-induced priors. Inference errors are not merely stochastic; they are structured by training distribution, fine-tuning, and deployment priors, and governance and lifecycle operators are particularly sensitive to errors in the projected user trajectory. Third, we model interaction as a path through a space of reachable states, with each operator application inducing a transformation of the branch set B(S). Three transformation types (contraction, expansion, reweighting) operate transversally across operator orders. We introduce interior integrity: the preservation of branch structure within the permissible region of interaction, and propose three legitimacy conditions on transformations—explicitness, reversibility, and grounding—which we show fail in different ways across operator orders. The central formal result is a non-entailment: output acceptability without trajectory constraints does not guarantee preservation of branch accessibility under composition. Sequences of locally acceptable responses can, under repeated directional reweighting, produce trajectory-level compression and capture. The paper then proposes two LLM-specific mechanisms by which this vulnerability may become systematic. The first is semantic normalization: the reduction of high-variance user meaning into familiar, stable, answerable, and policy-compatible forms. Coherence-seeking is treated as one visible manifestation of this broader normalization pressure. The second is inference-error amplification, by which mistakes in the inferred user state propagate through high-burden governance and lifecycle operators. The framework is offered as a structural theory and empirical research program rather than as a completed corpus study. It constrains how operator-induced transformations may be applied without prescribing specific outputs, and it yields a falsifiable prediction: trajectory compression should be disproportionately associated with silent governance and lifecycle operators rather than with first-order state-transforming operators alone.

---

## uid: `doi:10.2139/ssrn.6815500`

- title: SEEN: A Four-Layer Framework for Generative Engine Optimization
- authors: Dmitrii Kargaev
- affiliations: not stated
- posted: 2026-06-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6815500
- keyword hits: large language model, large language models, retrieval-augmented

### abstract

Search engine optimization has traditionally treated the ranked web page as the main unit of work and rank position as the main visibility proxy. AI-mediated discovery weakens that model. Generative search systems, answer engines, large language models, and browser agents can retrieve passages, issue derived queries, synthesize answers, attach citations, and recommend entities without presenting a stable ranked list of pages. This working paper introduces SEEN, a four-layer framework for Generative Engine Optimization: Structure, Evidence, Entity, and Notability. SEEN reframes optimization around an entity's evidence corpus rather than a single owned page. It asks whether an entity is easy for AI systems to find, read, verify, resolve, and recommend. The paper synthesizes platform documentation, academic work on generative engine optimization and conversational SEO, empirical studies of Google AI Overviews, retrieval-augmented generation mechanisms, evidence-evaluation research, knowledge-graph grounding, crawler documentation, and industry studies of AI search citations. It contributes: (1) a stage-aware model of AI visibility; (2) a four-layer entity-corpus framework; (3) a 41-item practitioner checklist that operationalizes the framework; and (4) a conservative validation agenda for future empirical work. The paper does not claim that SEEN guarantees citations, recommendations, rankings, or traffic. Instead, it argues that AI visibility should be analyzed as a corpus-engineering problem in which owned content, platform-hosted first-party content, and third-party corroboration must read as one coherent, verifiable entity.

---

## uid: `doi:10.2139/ssrn.6817998`

- title: Quantum Computing and Artificial Intelligence Security
- authors: Rizwan Tanveer
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6817998
- keyword hits: agentic, generative artificial intelligence

### abstract

Background: The maturation of post-quantum cryptography and the rapid deployment of agentic and generative artificial intelligence are converging into a single, under-examined risk surface. The United States National Institute of Standards and Technology finalised its first three post-quantum cryptographic standards in August 2024 and selected a further algorithm for standardisation in March 2025, yet the security discourse continues to treat quantum cryptanalysis and AI system security as separate domains. Purpose: This paper consolidates the quantum dimension of AI security into a coherent analytical frame. It examines three intersecting threat vectors, namely the cryptographic exposure of AI assets to harvest-now-decrypt-later strategies, the prospective acceleration of adversarial machine learning by quantum optimisation, and the bidirectional synergy through which each technology amplifies the offensive potential of the other, and it proposes a migration governance agenda suited to practitioners operating multi-jurisdictional AI estates. Approach: The study adopts a conceptual and integrative review methodology, synthesising primary standards documentation, national authority guidance, and emerging peer-reviewed and preprint literature. It maps identified threats against established control frameworks, including the NIST AI Risk Management Framework, ISO/IEC 42001, and the cryptographic provisions of allied national guidance, and develops a tiered migration model calibrated to data longevity and asset criticality. Findings: AI estates present a distinctive and elevated harvest-now-decrypt-later exposure because model weights, proprietary training corpora, and inference traffic carry long confidentiality lifespans that frequently exceed plausible timelines for a cryptographically relevant quantum computer. Cryptographic agility, rather than any single algorithm choice, emerges as the decisive architectural property. The convergence of quantum acceleration and adversarial machine learning is currently theoretical but warrants anticipatory governance, given the asymmetry between preparation costs and tail risk. Implications: Organisations should treat post-quantum migration as an AI governance obligation rather than a narrow cryptographic upgrade, embedding cryptographic inventory, agility, and data-longevity triage within existing AI management systems. For the Gulf Cooperation Council region, where sovereign data initiatives and AI adoption are advancing in parallel, early alignment with internationally recognised post-quantum standards offers both a risk-reduction and a strategic-positioning advantage.

---

## uid: `doi:10.2139/ssrn.6824558`

- title: LegalGraphRAG: Multi-Agent Graph Retrieval-Augmented Generation for Reliable Legal Reasoning
- authors: Zerui Chen, Qinggang Zhang, Zhishang Xiang, Zhimin Wei, Linfeng Gao, Xiao Huang, Zhihong Zhang, Jinsong Su
- affiliations: not stated
- posted: 2026-06-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6824558
- keyword hits: llm, retrieval-augmented

### abstract

Graph-based Retrieval-Augmented Generation (GraphRAG) advances flat document retrieval by structuring knowledge as relational graphs, enabling more coherent and effective reasoning. However, applying it to specific domains like legal reasoning faces critical challenges. (i) Legal corpora are heterogeneous, containing multi-granular knowledge from cases, articles, and interpretations. A flat knowledge graph cannot adequately differentiate between factual details, applied rules, and abstract principles, limiting accurate retrieval. (ii) Reliable legal judgment demands transparent, evidence-based reasoning. Traditional RAG passes retrieved context directly to an LLM without verification, resulting in opaque, error-prone reasoning. To this end, we propose LegalGraphRAG, a framework designed for reliable legal reasoning. Our approach introduces two core components: a hierarchical legal graph that hierarchically organizes legal sources to enable retrieval at appropriate abstraction levels, and a multi-agent system for reliable legal reasoning, where a Researcher retrieves candidate evidence, an Auditor rigorously verifies its validity against source documents, and an Adjudicator synthesizes the set of verified evidence to render a final judgment. Extensive experiments show that Legal-GraphRAG achieves the state-of-the-art performance, outperforming existing GraphRAG baselines in accurate and trustworthy legal analysis. Our code, datasets and implementation details are available at https://github.com/ XMUDeepLIT/LegalGraphRAG.

---

## uid: `doi:10.2139/ssrn.6823079`

- title: RAG on the Shopfloor: A Framework for Industrial Knowledge Retrieval
- authors: Shashikant Pradhan
- affiliations: not stated
- posted: 2026-06-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6823079
- keyword hits: large language model, llm, retrieval-augmented

### abstract

Manufacturing plants generate vast quantities of operational knowledge, from equipment manuals and standard operating procedures to alarm histories and the undocumented expertise of experienced technicians. Yet when a line operator needs to diagnose an unfamiliar fault at 2 a.m., this knowledge is rarely accessible in a useful form. Retrieval-Augmented Generation (RAG)-an architecture that pairs a large language model (LLM) with a real-time document retrieval mechanism, has demonstrated strong performance in enterprise knowledge applications. However, applying RAG in industrial Operational Technology (OT) environments introduces challenges that general-purpose implementations are not designed to address: network isolation, safety-critical accuracy requirements, fragmented data formats, and the need to ground responses in site-specific, verifiable sources. This paper reviews the current state of RAG research, identifies the specific gaps between general RAG capabilities and OT shopfloor requirements, and proposes a framework-Industrial RAG (iRAG)-that adapts the core RAG architecture for deployment in manufacturing environments. The iRAG framework introduces four design principles derived from OT constraints: source-constrained grounding, heterogeneous document handling, on-premises deployment by default, and human-in-the-loop verification for safety-relevant outputs. The framework is currently in system testing and has not yet been validated at production scale. This paper presents the rationale, architecture, and preliminary design decisions, with the aim of initiating practitioner dialogue on a critical and underserved problem.

---

## uid: `doi:10.2139/ssrn.6891368`

- title: A Formal Security Framework for Model Context Protocol-Based Tool Access inAgentic AI Systems
- authors: Mohammad Zahangir Alam
- affiliations: not stated
- posted: 2026-06-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6891368
- keyword hits: agentic, large language model, large language models

### abstract

The increasing deployment of agentic AI systems powered by large language models introduces significant security challenges at the interface between autonomous agents and external tool ecosystems. Existing security mechanisms, including role-based access control, OAuth-based authorization, and API gateway models, are designed for static, human-initiated interactions and fail to enforce trust boundaries across dynamic, runtime-delegated principal hierarchies in multi-agent environments. To address these limitations, we propose FSM-MCP, a mathematically grounded formal security model for MCP-based tool access in agentic AI systems. The model defines a hierarchical trust structure spanning users, orchestrator agents, sub-agents, and MCP servers, formalizing capability delegation, trust-boundary enforcement, and least-privilege tool invocation as verifiable security axioms. This formalization enables rigorous reasoning about tool-access integrity and precise detection of security violations across agent layers. To evaluate FSM-MCP, we simulate five threat classes — tool spoofing, privilege escalation, cross-agent prompt injection, context poisoning, and orchestrator hijacking — across three publicly available benchmarks, namely AgentBench, ToolBench, and APIBench, ensuring comprehensive and reproducible evaluation across diverse heterogeneous agentic deployment scenarios. Experimental results demonstrate that FSM-MCP reduces successful attack execution by 91.3% while introducing only 4.7% mean latency overhead, consistently outperforming unprotected baseline deployments and conventional access-control mechanisms across all evaluated threat classes. The framework improves trust delegation precision and inter-agent authentication robustness through capability-scoped access tokens, cryptographically signed tool manifests, context sanitization, and inter-agent message authentication. These results establish the first rigorous security foundation for MCP-based agentic AI deployment and provide a reproducible benchmark for evaluating tool-access threats in hierarchical multi-agent systems.

---

## uid: `doi:10.2139/ssrn.6901066`

- title: Modeling Project Risk Propagation from Risk Sources to Activity Networks: A Large Language Model-Assisted Approach
- authors: Liting Zhang, Yan Ning
- affiliations: not stated
- posted: 2026-06-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6901066
- keyword hits: large language model, large language models, retrieval-augmented

### abstract

Risk propagation is common in projects. However, little is known about how risk propagation chains stem from risk sources and how such chains interact with project activity networks. To address this gap, this study proposes a model of project risk propagation from risk sources to project activity networks, and examines their joint impacts on project performance. A historical risk knowledge base is first constructed from project-related textual records using large language models. Retrieval-augmented generation is then used to identify project-specific propagation chains, and a propagation model is developed to calculate how risk effects accumulate through project activity dependencies. A real-world case demonstrates that reducing a single important risk source may have limited effects when the core propagation chain remains connected. The results further show that risks affecting upstream or highly connected activities are more likely to spread to subsequent activities and generate cumulative project impacts. This study provides an interpretable approach for identifying critical project risk propagation chains and supporting early risk control in projects.

---
