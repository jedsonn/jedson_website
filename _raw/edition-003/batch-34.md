# Classification batch 34 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-34.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7113581`

- title: A Systematic Literature Review of Retrieval-Augmented Generation Methods for the Software Vulnerability Lifecycle
- authors: Zhijie Chen, Luyao Xu, Zhihao Lin, Xiaolin JU, Xiang Chen
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7113581
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

The software vulnerability lifecycle, spanning vulnerability discovery, analysis, and mitigation, is increasingly knowledge-intensive and difficult to automate. Although large language models (LLMs) have shown promise in vulnerability-related tasks, standalone LLMs often suffer from outdated knowledge, hallucinations, and limited evidence traceability. Retrieval-Augmented Generation (RAG) has therefore emerged as a promising paradigm for grounding vulnerability-oriented LLM systems in external knowledge and task-relevant evidence. However, existing RAG-based studies in this area remain fragmented across lifecycle stages, knowledge sources, technical designs, and evaluation settings. To address this gap, this paper presents a systematic literature review of Retrieval-Augmented Generation methods for the software vulnerability lifecycle. We systematically collected and analyzed 30 primary studies published between 2025 and 2026, and examined them from four perspectives: lifecycle tasks, knowledge resources, RAG settings, and experimental settings. Our analysis shows that current research is concentrated on vulnerability discovery, while vulnerability analysis and mitigation remain comparatively underexplored. Existing methods rely on heterogeneous knowledge resources, including vulnerability databases, code artifacts, patches, audit reports, issue reports, security advisories, and knowledge graphs, and they are evolving from simple retrieve-then-generate pipelines toward more evidence-aware, structure-aware, and workflow-aware RAG systems. Nevertheless, evaluation practices remain highly fragmented across datasets, baselines, backbone models, and metrics, and RAG-specific aspects such as retrieval quality, grounding, and faithfulness are still insufficiently evaluated. Based on these findings, we summarize key challenges and future directions, including full-lifecycle vulnerability management, high-quality vulnerability knowledge bases, vulnerability-specific retrieval and reasoning mechanisms, standardized RAG-aware evaluation, and practical deployment.

---

## uid: `arxiv:2607.11183v2`

- title: Amplitude-Only FFN Intervention for Tool-Structured LLM Inference Method: Gated Evaluation Protocol, and Cross-Model Empirical Results
- authors: Sheng Xu, Junhua Wang, Boyuan Huang, Ke Jia, Jiadun Zhu, Zhen Chen
- affiliations: not stated
- posted: 2026-07-13
- source: arXiv
- link: https://arxiv.org/abs/2607.11183v2
- keyword hits: agentic, large language model, large language models, llm, qwen

### abstract

Large language models increasingly operate as tool-using agents, where small format, argument, or function-call errors can invalidate otherwise plausible responses. We study inference-time feed-forward network (FFN) intervention for improving structured outputs without retraining model weights. Our project began with Orthogonal Residual Projection (ORP), a direction-changing repair attempt that revealed sensitive SwiGLU FFN intervention sites but often caused more harm than fixes. We therefore propose Amplitude Gating (AG), a non-destructive alternative that preserves pretrained FFN weight directions and modulates only activation magnitudes during generation. We define a fine-grained intervention system spanning P1/P2/P3 and branch-specific P1s/P2a/P2b sites, and introduce an evaluation protocol that separates combination-oracle headroom from fixed configurations and learned gates, enforces sample-level accounting, and uses task-aware metrics for binary and partial-credit datasets. Across Qwen3.5-9B, Qwen3-8B, and Qwen2.5-7B, AG is weakly positive in aggregate but strongest on tool-structured tasks. On Qwen3.5-9B, a category-level learned gate improves tool/structured/agentic performance from 38.66% to 42.92% (+4.27 percentage points), with Hermes function-call tasks reaching about +7.6 points. On Qwen3-8B, Hermes JSON mode improves by +11.36 points. Qwen2.5-7B retains oracle headroom but current learned gates fail to capture it, showing that deployment requires model- and category-specific routing. Comparisons of entropy AG with Newton-Schulz-windowed AG show that neither family is uniformly dominant. These results identify tool-structured inference as the most credible first target for safe FFN-level inference optimization, while prospective online validation and broader cross-model evaluation remain necessary.

---

## uid: `arxiv:2607.11141v1`

- title: NextFund: A Unified Performance Tracking Platform for Agentic Portfolio Management
- authors: Changlun Li, Peixian Ma, Qiqi Duan, Zhenyu Lin, Peineng Wu
- affiliations: not stated
- posted: 2026-07-13
- source: arXiv
- link: https://arxiv.org/abs/2607.11141v1
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) based agents are beginning to participate in portfolio construction and market analysis, where decisions must be justified under evolving information and risk constraints. Current assessment practice, however, remains poorly aligned with this setting: many studies rely on static examinations or report only terminal portfolio returns, while the intermediate evidence, analyst judgments, and execution steps that produced those returns stay largely invisible. We introduce NextFund, an evaluation platform that makes financial-agent behavior observable under live market conditions. The platform couples time-consistent market access, coordinated multi-agent analysis, and persistent logging of the full decision path from observation to trade. Through an interactive Trading Arena, users can compare models across markets, inspect equity curves, and drill from leaderboard outcomes down to individual justifications. We present NextFund on Hong Kong, U.S., and China A-share equities, illustrating how inspectable decision histories enable fairer benchmarking and more actionable diagnosis. Our demo is available at https://paradoox.cn/nextfund/.

---

## uid: `arxiv:2607.14309v1`

- title: Traccia: An OpenTelemetry-Based Governance Platform for AI Systems
- authors: Nutan Kumar Naik, Aditya Kumar Saroj, Vijay Prasad Poudel, Saurav Samantray, Abhishek Patel
- affiliations: not stated
- posted: 2026-07-15
- source: arXiv
- link: https://arxiv.org/abs/2607.14309v1
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

The rapid development of Large Language Models (LLMs) and Artificial Intelligent (AI) powered autonomous agents has fundamentally changed the existing forms of software governance. In spite of the rigorous standards of transparency and account ability required according to the international frameworks such as the European Union's AI Act, there is a considerable gap between theory and reality. The present study discusses the inherent drawbacks of currently utilized platforms for LLM evaluation, machine learning workflow, and application performance monitoring in general. It has been shown that current disjointed solutions fail to protect unbound state space agentic architecture from serious threats such as alignment drift, SaaS security concerns, and unauthorized deployment of shadow AI systems. Moreover, a solution is proposed for overcoming the discussed challenges in form of a coherent multi-level AI governance stack Traccia built on the top of OpenTelemetry infrastructure platform. Traccia resolves the last mile for AI Alignment by adding the telemetry data, passive semantic guardrail assessment, and execution lineage into a hashed trace ledger. Traccia automatically creates compliance evidence packages by appending tamper-resistant fingerprints and SHA-256 content hash, that map to regulatory requirements (Articles 12, 14, 19, 26(6), and 50 of the EU AI Act) without invading any data privacy. By performing this evaluation in a methodical manner, a solid machine-readable base has been created for enterprise-wide management of autonomous AI systems.

---

## uid: `doi:10.2139/ssrn.6990301`

- title: A Survey on Large Language Models for Hardware Description Language Generation
- authors: Ce Guo
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6990301
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

Large Language Models (LLMs) have rapidly moved from generating software in languages such as Python and C into the generation of hardware description languages (HDLs), most prominently Verilog. Unlike software code, HDL describes physical circuits: a design is useful only if it is not merely syntactically and functionally correct, but also synthesizable and able to meet hard resource, timing, and power budgets on a concrete target such as an FPGA or ASIC. This shift in success criteria reshapes every part of the generation pipeline, from data curation and model adaptation to prompting, repair, and evaluation. Despite a fast-growing body of work, a newcomer to the field faces a fragmented literature with inconsistent benchmarks, evaluation criteria, and synthesis flows. In this survey we provide a structured, up-to-date review of LLMs for HDL generation. We introduce a taxonomy that organizes the field along four axes (data and benchmarks, model adaptation, inference-time techniques, and feasibility-aware optimization), and we map representative systems onto it. We contrast HDL generation with general code generation throughout, summarize how evaluation has evolved from string similarity to simulation, formal equivalence, and resource-aware metrics, and close with the open challenges (cross-vendor portability, synthesis-loop cost, real-silicon validation, and fair attribution of gains) that we believe will shape the next few years.

---

## uid: `doi:10.2139/ssrn.6970438`

- title: Large-Scale Evaluation of MaxEntRAG-Flow: Incremental Evidence Structures for Real-Time Context Compression and Joint Probabilistic Graph Retrieval in Long-Context LLMs
- authors: Haranadh Gavara
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6970438
- keyword hits: large language model, large language models, llm, llms, qwen, retrieval-augmented

### abstract

Large Language Models (LLMs) have achieved remarkable progress in processing long documents, but practical deployment in streaming, interactive, and high-throughput environments remains constrained by the cost of long-context generation, including key-value (KV) cache pressure and increased latency. Retrieval-Augmented Generation (RAG) addresses this by retrieving evidence before generation [5], but conventional sparse or dense retrieval usually treats paragraphs as independent blocks. GraphRAG-style systems preserve structure more explicitly [4], while token-level compression systems such as LongLLMLingua reduce prompt length through model-guided pruning [3]. Existing approaches to long-context retrieval face a trade-off between efficiency and structural fidelity. Sparse or dense retrievers are fast, but they generally operate over independent chunks and do not explicitly preserve co-occurrence paths across source spans. Stronger compression and graph-based retrieval methods can improve evidence selection, but they often depend on offline extraction, summarization, clustering, or model-assisted graph construction, making them less suitable for conversational systems with continuously updated evidence. MaxEntRAG-Flow [1] was originally formulated as an LLM-free, source-anchored sparse retrieval framework for cost-efficient graph-augmented RAG. This paper evaluates its use as a context-compression mechanism and shows that its probabilistic evidence structure can reduce context size, retrieval latency, and interaction cost while preserving useful QA performance across long-context benchmarks. We evaluate this previously defined engine against Oracle full context, prompt truncation, slidingwindow retrieval, BM25-style VectorRAG, and a fixed MaxEntRAG-Flow Top-3 variant on LongBench [8], ZeroSCROLLS [2], MuSiQue [6], LooGLE [7], and NaturalQuestions using a local Qwen-3B model. The full threshold sweep τ prob ∈ {0.1, 0.2,. .. , 1.0} shows that MaxEntRAG-Flow can compress context aggressively while exposing benchmark-specific quality behavior. Across the four long-context benchmarks, the average retrieved context decreases from 1812.3 tokens at τ prob = 0.1 to 603.4 tokens at τ prob = 0.9 and 1.0, while average QA F1 varies between 10.8% and 9.6%. The experiments also show that update and retrieval latency are central to the method's value: MaxEntRAG-Flow has non-zero online update cost but very low retrieval latency, while prompt truncation and sliding-window baselines can carry much higher downstream retrieval or prompt-preparation latency under this setup. The contribution of this paper is a threshold-dynamics and systems-cost analysis of a source-anchored evidence structure under controlled long-context retrieval settings.

---

## uid: `doi:10.1145/3807503.3819448`

- title: Auditing Retrieval-Augmented LLM Hypotheses for Longitudinal Cell Painting Morphology
- authors: Gilchan Park, Guang Zhao, Byung-Jun Yoon, Shinjae Yoo
- affiliations: not stated
- posted: 2026-07-17
- source: arXiv
- link: https://arxiv.org/abs/2607.19415v1
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

High-content morphological profiling (Cell Painting) yields sensitive, high-dimensional signatures of cellular state, but translating longitudinal morphology trajectories into interpretable biology remains difficult, especially for weak, chronic perturbations such as low-dose-rate ionizing radiation. Large language models (LLMs) can synthesize heterogeneous evidence into biological narratives, yet their scientific use requires quantitative auditing. We present an evaluation-first, retrieval-augmented interpretation framework for longitudinal Cell Painting morphology, applied to a 9-week RPE-1 time course across five dose rates (0.003--6.0 mGy/hr). Week-matched treated-control morphology deltas are combined with retrieved perturbation neighbors, pathway context, and literature evidence through stable evidence identifiers, enabling an LLM to generate structured, evidence-linked hypotheses that are hierarchically summarized while preserving provenance. We introduce two quantitative auditing tests: V1 citation validity, which verifies that cited evidence identifiers exist in the prompt, and V2 proxy-based morphology compatibility, which evaluates consistency between predicted biological processes and the most altered morphology features. In our experiments, V1 detected no invalid evidence references, while V2 showed meaningful morphology compatibility that increased with perturbation strength and was positively associated with an independent morphology drift summary. The framework produces auditable, falsifiable biological hypotheses, including an adaptive phenotype involving metabolic reprogramming and proteostatic stress at lower dose rates (0.003--0.3 mGy/hr). Current limitations include proxy-based evaluation and the lack of ground-truth mechanism labels.

---

## uid: `doi:10.2139/ssrn.7122635`

- title: CycloneGPT: Automating Cyclone Separator Design through an Iterative Retrieval-Augmented Large Language Model
- authors: Danhui Yang, Yi Yu, Cong Shi, Ding Wang, Yifei Sun, Jia Xu, Yulong Chang, Hualin Wang
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7122635
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Separation processes, particularly cyclone separators, are among the most important operations in the chemical industry, accounting for 40-60% of total energy and capital costs in petroleum refining, power generation, and chemical processing. Despite the widespread deployment, cyclone design still relies heavily on empirical correlations, extensive experimentation, and computationally expensive computational fluid dynamics simulations, creating significant barriers to rapid design optimization. In this work, we propose `CycloneGPT', an iterative Retrieval-Augmented Generation (RAG) enhanced Large Language Models (LLMs) framework for cyclone design. Regarding the contribution in artificial intelligence (AI), CycloneGPT incorporates an iterative inference search strategy that decomposes queries and detects coverage gaps in the generated response, and initiates targeted re-retrieval cycles until comprehensive coverage is achieved, effectively overcoming the single-pass limitation of conventional RAG systems for multi-faceted engineering design. A specialized knowledge base grounded in authoritative references further eliminates hallucination through domain-specific retrieval. For the engineering application, we apply this AI framework to automate the structural design and parameter optimization of cyclone separators. Systematic evaluation across domain-specific Query and Answer (Q&A) and real-world design scenarios demonstrated that CycloneGPT achieved 96.8\% answer accuracy and 92.6% response completeness, compared to 23.6% and 16.7% for baseline LLMs. Physical validation using three-dimensional-printed hydrocyclone prototypes further confirmed the practical effectiveness of CycloneGPT-generated design recommendations. Beyond accuracy, energy efficiency analysis demonstrates that CycloneGPT substantially reduces the computational footprint and operational energy consumption compared to the traditional design paradigm. The framework not only democratizes expert-level cyclone design capabilities but also establishes a new paradigm for industrial equipment design.​

---
