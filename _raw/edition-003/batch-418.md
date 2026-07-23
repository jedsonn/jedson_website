# Classification batch 418 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-418.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6970419`

- title: Maximum Entropy Source-Anchored Sparse Retrieval with LLM-Free Indexing for Graph-Augmented RAG
- authors: Haranadh Gavara
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6970419
- keyword hits: llm, retrieval-augmented

### abstract

Graph-augmented Retrieval-Augmented Generation (RAG) commonly relies on dense knowledge-graph construction, where entities and relations are extracted from source documents and materialized as a retrieval structure. While this can improve relational access, it also introduces high indexing cost, graph growth, and noisy traversal through over-connected semantic hubs. This paper presents MaxEntRAG, a sparse source-anchored retrieval framework that uses Maximum Entropy (MaxEnt) filtering for LLM-free indexing and LLM-free graph construction. Instead of using an LLM to construct an exhaustive synthetic knowledge graph, Max-EntRAG builds a compact transitive retrieval structure around maximum-entropy anchors. Source spans act as grounded hyperedges, sentence and paragraph boundaries provide local context, and probabilistic traversal decides how far retrieval should expand for a given query. The method is designed to preserve the minimum useful connectivity required for multi-hop evidence retrieval while avoiding low-information edges that increase graph density without improving answer relevance. The paper studies this trade-off through the Density Paradox: beyond a critical density, additional semantic connectivity can reduce retrieval precision by dispersing query signal across plausible but irrelevant paths. Experiments on GraphRAG-Bench (Medical and Novel subsets), HotpotQA, and MuSiQue show that sparse maximum-entropy anchoring can approach strong graph-based retrieval baselines while avoiding LLM-based graph construction and maintaining substantially lower indexing cost, graph density, and query latency. The results suggest that many RAG workloads do not require complete LLM-generated knowledge graphs; they require compact, source-grounded, high-information retrieval structures that can be indexed and connected without LLM extraction.

---

## uid: `doi:10.2139/ssrn.7113771`

- title: When private providers serve public healthcare: Survival analysis and demand forecasting in an integrated Italian region
- authors: Giulia Guidi, Sahar Paktinat, Cristina Ugolini, Rossella Verzulli, Barbara Bordini
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7113771
- keyword hits: prompting

### abstract

Background. Population ageing and the rising prevalence of lifestyle-related conditions exert increasing pressure on publicly funded healthcare systems, prompting a dual challenge of maintaining quality of care while addressing capacity constraints. While the expansion of public-private mix has become a common policy response across European health systems, empirical evidence on how private providers interact with public capacity and long-term quality in highly regulated settings remains limited. Objective. Our study addresses this gap by examining the role of accredited private providers within a publicly funded, universal health system facing growing capacity pressures driven by population ageing and the increasing burden of chronic conditions. Methods. We focus on knee arthroplasty procedures delivered in Emilia-Romagna, a large Italian region where considerable emphasis is placed on co-ordination and co-operation between public and private providers. First, we conduct a survival analysis to assess whether clinical quality as proxied by knee arthroplasty survival rates differ between public and accredited private hospitals. Second, we develop forecasting models that integrate demographic projections, epidemiological trends, and historical utilization patterns to forecast future demand for knee arthroplasty. Results. The findings show no significant ownership-related differences in prosthesis survival once patient and procedural characteristics are accounted for. The simulation exercise based on forecasting allows policymakers to evaluate the long-term sustainability of future healthcare needs in a mixed public-private healthcare system.Conclusions. The results suggest that, in a highly regulated healthcare system, shifting standardized elective procedures to accredited private hospitals may help manage excess demand without undermining quality of care.

---

## uid: `doi:10.2139/ssrn.6979418`

- title: Modernizing America's Property Records: An Infrastructure for Serving Property Record Data to AI Agents
- authors: Kavin Sakthivel
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6979418
- keyword hits: ai agent

### abstract

United States property-tax and assessment data is authoritative but it has no national home: it is produced independently by roughly 3,144 county and county-equivalent offices, each with its own field names, code tables, file formats, access path, and terms of use. The data is consequential for underwriting, valuation, planning, and tax fairness, yet at national scale it is reachable only through proprietary aggregators that are closed, human-oriented, and silent about where each value came from. We argue that the work of turning this fragmented record into a single, lawful, agent-queryable substrate is, at its core, a sequence of classification problems, and we build a system on that premise. A national discovery layer probes and classifies the property-tax access point of every U.S. county, tagging each candidate by platform, exposed field capability, and a legal-access tier; it reaches a primary endpoint for 3,085 of 3,144 jurisdictions (98.1%). An end-to-end pipeline then extracts, classifies, and harmonizes records onto one canonical schema, demonstrated in depth on the District of Columbia, where 221,163 properties, 442,526 assessments, and 833,870 tax records are normalized and served to AI agents through a live Model Context Protocol (MCP) interface that has answered 811 production queries. Provenance and a machine-readable license travel with every value; a source registry physically disables sources whose terms forbid automated use, making lawful sourcing an enforced property of the system rather than a promise. We report coverage, the distribution of the classification stages, and the compliance mechanism on real data, and we are explicit about scope: national discovery is complete, DC harmonization is complete, and national harmonization is shown to be feasible rather than finished.

---

## uid: `arxiv:2607.16074v1`

- title: JoyNexus: Service-Oriented Multi-Tenant Post-Training for VLA Models
- authors: Haoran Sun, Wentao Zhang, Junyang Hua, Hedan Yang, Yongjian Guo, Yifei Zhang, Xiaolong Xiang, Mingxi Luo
- affiliations: not stated
- posted: 2026-07-17
- source: arXiv
- link: https://arxiv.org/abs/2607.16074v1
- keyword hits: fine-tuning

### abstract

The post-training of Vision-Language-Action (VLA) models is essential due to the diversity of simulators, robot embodiments, and task objectives. Existing compute services, whether offered as direct accelerator rental or batch-workload submission, typically allocate an exclusive set of GPU and CPU resources to a single tenant. While this paradigm maximizes client flexibility, it burdens users with infrastructure adaptation, and the fixed card-hour accounting model renders short or bursty workloads both expensive for tenants and inefficient for the service provider. To address these challenges, we present JoyNexus, a unified service for multi-tenant VLA supervised fine-tuning, reinforcement learning, and evaluation. JoyNexus decouples the Training Model Service, Inference Model Service, and Environment Service, each accessed through APIs and backed by resident shared base models with tenant-specific slots. Tenants can directly invoke high-level semantic APIs for training, rollout, and evaluation, or compose custom algorithms using lower-level APIs and their assigned endpoints. Multiple tenants submit workloads concurrently; their action modules, optimizers, rollout records, and policy versions remain isolated, and the service is scheduled by the global Training Queue and Inference Queue. To further improve multi-tenant training efficiency, JoyNexus introduces group batching for heterogeneous VLA data schemas that share a compatible model-facing prefix, enabling a single shared backbone forward pass over grouped samples. Finally, we evaluate JoyNexus through workload simulation and a group-batching pipeline in a realistic embodied scenario. Results show that, compared with isolated single-tenant execution, JoyNexus reduces aggregate GPU time and improves service utilization via cross-tenant scheduling on shared resources.

---

## uid: `arxiv:2607.16038v1`

- title: SciForge: An AI-Native, Multimodal Workbench for Scientific Discovery
- authors: SciForge Team, Zhangyang Gao, Minghao Fang, Yifei Liu, Hanhui Yang, Xinyu Gu, Shixiang Tang, Siqi Sun
- affiliations: not stated
- posted: 2026-07-17
- source: arXiv
- link: https://arxiv.org/abs/2607.16038v1
- keyword hits: agentic

### abstract

Scientific work increasingly spans heterogeneous artifacts -- papers, code, datasets, scientific file formats, model outputs, figures, manuscripts, and team decisions -- yet general-purpose AI assistants rarely preserve these objects as a coherent, auditable research state. We present SciForge, a multimodal research-native AI workbench that reserves the graphical interface for human judgment while search, parsing, model routing, workflow execution, plotting, writing, and presentation generation run as modular agent-accessible services. SciForge is built around five pillars: (i) \emph{goal-scoped scientific decision governance} for \textbf{goal-oriented} research, with review gates and shared review surfaces; (ii) \emph{translate-then-reason} for \textbf{multimodal} input, routing scientific objects through domain translators before the agent reasons; (iii) \emph{evidence governance} for \textbf{auditable} traceability, linking claims to provenance chains and audit findings; (iv) \emph{collaborative team science} for \textbf{collaborative} research, enabling multi-role decision governance, with shared team workspaces planned for future releases; and (v) \emph{real-world application scenarios} for \textbf{practical} impact, demonstrated through eight end-to-end user cases, with flagship demonstrations including multi-day agentic research sprints for gene discovery, AI-guided de novo protein design, molecular optimization, and genome-to-BGC discovery. The system combines a thin interaction layer, contextual research capability patterns, an Agent Runtime and Workflow Engine, an Evidence-DAG audit sidecar and a Scientific Model Router. SciForge currently runs as a desktop application, with mobile supervision support; future releases will deepen team collaboration. The system is open-source and available at https://github.com/AGI4Sci/SciForge

---

## uid: `arxiv:2607.15879v2`

- title: DECODEM: Data Extraction from Corporate Organizational Documents via Enhanced Methods
- authors: Jens Frankenreiter
- affiliations: not stated
- posted: 2026-07-17
- source: arXiv
- link: https://arxiv.org/abs/2607.15879v2
- keyword hits: prompting

### abstract

Much empirical legal research depends on translating unstructured text into structured variables. In corporate governance research as elsewhere, this translation has traditionally relied on human coding of documents such as charters and bylaws, a process that is costly, difficult to scale, and often opaque. This paper introduces DECODEM, a set of benchmark datasets for evaluating the automated extraction of corporate governance variables from organizational documents. The benchmarks pair randomly sampled corporate charters and bylaws with high-quality human annotations covering a range of governance provisions commonly studied in empirical work. Using these datasets, the paper evaluates several large-language-model extraction pipelines that vary in prompt design, task decomposition, and document handling. The underlying task consists of a set of document-level binary classification problems, one for each governance variable. The results show that automated extraction is feasible at a high level of accuracy for many provisions, with median performance near the upper bound across approaches. At the same time, performance varies systematically across variables, with a small number of provisions accounting for most of the remaining errors. More elaborate prompting strategies and cascading pipelines do not consistently improve performance for frontier models, but substantially narrow the gap between frontier and efficiency-oriented models in some settings, suggesting that pipeline design can partly substitute for model capability. By providing a standardized benchmark and a systematic evaluation of extraction methods, the paper demonstrates that current frontier models can extract legally meaningful information from complex corporate documents with high accuracy and suggests an important future role for automated feature extraction in constructing corporate governance datasets.

---

## uid: `doi:10.2139/ssrn.7004618`

- title: Regenerative Agentic Science How the Displaced Expert Becomes the Builder
- authors: Surendra Reddy
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7004618
- keyword hits: agentic

### abstract

The marginal cost of turning subject-matter knowledge into working software is collapsing as capable AI coding agents absorb the execution of technical work. This paper argues that the same shift carries two faces: it displaces the routine, execution-bound roles that formed the lower rungs of knowledge work, and it unbundles domain expertise from coding skill, leaving expert judgment as the scarce and appreciating input. Drawing on recent labor-exposure estimates and an industry analysis of roughly 400,000 agentic coding sessions, the paper locates the binding constraint not in whether a system can be built but in whether someone with deep domain command owns its intent, its verification, and its governance. It introduces Regenerative Agentic Science as the discipline of building agents that regenerate a person's command of their field rather than substitute for it, and contrasts it deliberately with the prevailing meaning of agentic science, which centers machine autonomy and reduced human dependence. The paper specifies five commitments that distinguish regenerative from extractive agentic systems, illustrates the pattern across healthcare, law, finance, education, the skilled trades, operations, and agriculture, and states the conditions under which the thesis would fail, including the erosion of returns to expertise and capture by platforms.

---

## uid: `doi:10.2139/ssrn.7139658`

- title: Hardening Agentic AI: A Type-and-Effect Framework for Verified Delegation
- authors: Marco Aldinucci, Andrea Bracciali, Iacopo Colonnelli, Doriana Medić, Alberto Mulone, Luca Roversi, Marco  Edoardo Santimaria
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7139658
- keyword hits: agentic, llm

### abstract

Workflows are well-established automation mechanisms for business and scientific applications. Traditionally, they are specified in declarative or imperative languages and executed by users on distributed computing infrastructures. With the emergence of agentic AI, workflow systems are becoming external capabilities that an agentic delegate, a controlled operational actor between the user/model side and the workflow/tool side, can invoke to execute simulations, run data-analysis pipelines, or coordinate distributed services. Through protocols such as the Model Context Protocol (MCP), delegates may also access workflow descriptions, logs, provenance records, and runtime interfaces to inspect executions, diagnose failures, propose modifications, and trigger runtime actions. These capabilities introduce new operational and security risks, particularly when sensitive data, untrusted inputs, and privileged execution coexist within the same agentic loop.This paper revisits coordination languages for distributed systems through the lens of agentic AI. Building upon KLAIM and type-based access control for mobile code, we investigate how locality, mobility, and typed interactions can be used to strengthen the security boundary around LLM-based delegates operating over workflow systems. We introduce the notion of an agentic delegate as a model-mediated operational actor that combines an LLM, execution context, tool interfaces, policy constraints, and dynamically evolving authority.We propose Hard-KLAIM, a type-and-effect framework for controlling delegated agentic actions across distributed workflow localities. Hard-KLAIM explicitly distinguishes observation, proposal, commitment, and execution, ensuring that transitions between these phases satisfy explicit effect, locality, policy, and commitment constraints, thereby preventing unauthorized or silent escalation from analysis to execution.

---
