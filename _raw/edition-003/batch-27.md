# Classification batch 27 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-27.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6617061`

- title: Agent Brain: A Biologically Inspired Memory System for Autonomous AI Agents, with Head-to-Head Evaluation on LongMemEval
- authors: Theshoth Sritharan
- affiliations: not stated
- posted: 2026-05-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6617061
- keyword hits: ai agent, claude, gpt-4, large language model, llm

### abstract

This technical report describes Agent Brain, a biologically inspired memory system for autonomous AI agents. In contrast to stateless Large Language Model interactions, Agent Brain provides persistent, weighted, and self-organizing memory that emulates human cognitive processes: perception, storage, retrieval, consolidation, and forgetting. The system integrates eleven successive layers: (1) a Perception Gate for multi-dimensional evaluation of incoming information, (2) a Deduplication Guard based on Cosine Similarity, (3) typed memory storage 21.04.26, 02:17 Agent Brain v2 file:///Users/thesh/claude code/figment-aura-agent/ImmoPilot-Brain/docs/AGENT-BRAIN-PREPRINT-V2-EN.html 1/35 (episodic, semantic, procedural), (4) Named Entity Recognition using flair/ner-german-large (F1 92.31%), (5) a Knowledge Graph for associative retrieval, (6) LLM-based Query Expansion, (7) Hybrid Search via Reciprocal Rank Fusion, (8) Cross-Encoder Re-Ranking for precise relevance assessment, (9) an implicit Feedback Loop based on the Free Spaced Repetition Scheduler (FSRS), (10) a nightly Dream Cycle with five consolidation phases, and (11) complete Workspace Isolation with Row-Level Security. The central innovation lies in the combination of implicit feedback (without manual user feedback) with Spaced Repetition for agent memory, as well as a multi-stage Dream Cycle that unifies consolidation, creative association formation, and predictive pattern recognition. The system has been in production use since early 2026 for Swiss property management (Immobilienbewirtschaftung) with over 5,000 memories, 10,000 entities, and eight specialized agents. Head-to-head evaluation on LongMemEval. On the public weaviate/longmemeval-m-cleaned benchmark (500 QA pairs across 510 multi-turn workspaces, GPT-4o judge), Agent Brain achieves 71.7% accuracy, outperforming the next-best publicly reported memory system (Zep, 63.8%) by 7.9 percentage points, Mem0 (49.0%) by 22.7 pp, LangMem (47.1%) by 24.6 pp, and OpenAI Memory (40.2%) by 31.5 pp. We also reporttransparently-a 1.9 pp regression when enabling the Dream Cycle consolidation pipeline, and a 2.2 pp gap versus our own pgvector-only control, and discuss both findings in §15.4.

---

## uid: `doi:10.2139/ssrn.6705499`

- title: Seeing the Goal, Missing the Truth: Human Accountability for AI Bias
- authors: Sean S. Cao, Wei Jiang, Hui Xu
- affiliations: not stated
- posted: 2026-05-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6705499
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

This research explores how human-defined goals influence the behavior of Large Language Models (LLMs) through purpose-conditioned cognition. Using financial prediction tasks, we show that revealing the downstream use (e.g., predicting stock returns or earnings) of LLM outputs leads the LLM to generate biased sentiment and competition measures, even though these measures are intended to be downstream task–independent. Goal-aware prompting shifts these intermediate measures toward the disclosed downstream objective, producing in-sample overfitting. Specifically, purpose leakage improves performance on data prior to the LLM’s knowledge cutoff, but provides no advantage after the cutoff. This bias is strong enough that regularization of prompt instructions cannot fully address this form of overfitting. We further show that the bias can arise from users’ unintentional conversational context that hints at the purpose. Overall, we document that AI bias due to “seeing the goal” is not an algorithmic flaw, but stems from human accountability in research design. Institutional subscribers to the NBER working paper series, and residents of developing countries may download this paper without additional charge at www.nber.org .

---

## uid: `doi:10.2139/ssrn.6654060`

- title: Foundational Reasoning and Feedback Protocol (FRFP):Technical Specification
- authors: Vijaya Nadendla
- affiliations: not stated
- posted: 2026-05-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6654060
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

Large language models (LLMs) are increasingly used to analyze complex socio-technical systems. However, standard prompting workflows often allow models to implicitly combine hypothesis generation, interpretation, and conclusion endorsement into a single narrative output. This creates risks of persuasive but weakly grounded analyses. This document provides an engineering-oriented technical specification for the Foundational Reasoning and Feedback Protocol (FRFP). The protocol defines a structured reasoning architecture designed to separate representation, measurement, decision, and governance layers during analytical tasks. The specification translates theoretical principles into implementable procedures suitable for LLM-based analysis pipelines. The goal of FRFP is not to guarantee correctness of model outputs. Instead, it ensures that generated analyses are structurally transparent, auditable, and suitable for human evaluation.

---

## uid: `doi:10.2139/ssrn.6750643`

- title: Adaptive Edge-Cloud Orchestration for Large Language Models in Mission-Critical Regulated Environments
- authors: sakir alim
- affiliations: not stated
- posted: 2026-05-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6750643
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Large language models (LLMs) are increasingly considered for mission-critical applications in healthcare, financial services, and regulated enterprise decision support. However, centralized cloud inference alone is often insufficient for environments that require low latency, privacy preservation, explainability, and compliance with emerging artificial intelligence governance frameworks. This paper proposes an Adaptive Edge-Cloud LLM Orchestration framework, named AEC-LLMO, for secure and context-aware deployment of LLM services in regulated environments. The framework combines edge AI, cloud inference, federated learning, policy-aware routing, privacy-preserving preprocessing, explainable AI modules, and auditable compliance logging. Rather than treating edge and cloud inference as independent deployment options, AEC-LLMO dynamically assigns each request to local small language models, confidential cloud LLMs, or hybrid retrieval-augmented pipelines based on sensitivity, latency, task complexity, and regulatory constraints. A lightweight simulation using 10,000 synthetic regulated-domain requests indicates that the proposed approach reduces latency relative to cloud-only mean inference while maintaining higher task utility than edge-only deployment and improving compliance traceability. The paper contributes a concise architecture, an orchestration methodology, and an evaluation template for regulated LLM adoption. The findings suggest that adaptive hybrid AI systems can support scalable and privacy-preserving LLM deployment where static routing, purely centralized inference, or isolated edge models are operationally inadequate.

---

## uid: `doi:10.2139/ssrn.6754124`

- title: LLM-Driven Automated Framework for Intrinsic Medical Record Quality Assessment with Retrieval-Augmented Generation
- authors: Zhao Hang, Zhong Bing
- affiliations: not stated
- posted: 2026-05-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6754124
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Medical record quality control is pivotal for safeguarding healthcare safety and ensuring the integrity of scientific research data. However, traditional manual review processes are labor-intensive, prone to inconsistency, and susceptible to high false-negative rates. While rule-based automated systems offer efficiency, they lack the semantic adaptability required for complex clinical contexts. To address these limitations, this study proposes an automated framework for intrinsic medical record quality assessment driven by Large Language Models (LLMs). The framework leverages locally deployed open-source inference models integrated with Retrieval-Augmented Generation (RAG) technology to enhance domain-specific generalization and mitigate hallucinations. Furthermore, automated Extract-Transform-Load (ETL) pipelines and AI workflow orchestration are implemented within an on-premise environment to ensure data privacy and operational efficiency. Experiments conducted on a dataset of 3,000 real electronic medical records from Zunyi Municipal Hospital of Traditional Chinese Medicine demonstrate that the proposed framework significantly outperforms traditional methods, achieving a 90.6% reduction in per-record processing time and improving overall defect detection recall by 17.6 percentage points. This approach offers a novel private deployment paradigm for medical data governance with substantial clinical application potential.

---

## uid: `doi:10.2139/ssrn.6776140`

- title: From Ambiguity to Execution: An Agentic Neuro-Symbolic Framework for Transforming Building Regulations into Deterministic Constraints
- authors: Nikoo Mirhosseini, Davood Shojaei, Soheil Sabri
- affiliations: not stated
- posted: 2026-05-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6776140
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Integrating Large Language Models (LLMs) into Automated Compliance Checking (ACC) introduces "Spatial Hallucinations" and "Serialization Bottlenecks" when processing massive Building Information Models (BIM). This research proposes an Agentic Neuro-Symbolic Framework that decouples semantic interpretation from geometric verification. Instead of relying on generative LLMs for spatial reasoning, an agentic orchestrator synthesizes dynamic logic for a deterministic geometry kernel (IfcOpenShell). Evaluated against the Australian National Construction Code (NCC 2022), the framework autonomously resolves ISO 16739 ontological ambiguity. By employing connectivity graph traversal, it isolates targeted structural sub-graphs, reducing computational complexity from O(N) to O(K) and bypassing context-window limits. Offloading spatial mathematics to this deterministic environment achieves a zero-hallucination rate, generating immutable audit trails for digital permitting. This establishes a highly scalable, context-dependent foundation, proving AI in engineering must orchestrate deterministic tools rather than probabilistically predict physical realities.

---

## uid: `doi:10.2139/ssrn.6778889`

- title: Evidence-Traceable LLM Reporting for Industrial Process Fault Detection and Diagnosis
- authors: Jiyu Chen, Wei Peng, Lixin Zhang, Mingfu Zhu, Yifan Hu, Ming Zhai, Rui Xi, Tien-Chien Jen
- affiliations: not stated
- posted: 2026-05-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6778889
- keyword hits: deepseek, large language model, large language models, llm, prompting

### abstract

Large language models can turn fault-diagnosis outputs into readable reports, but may also produce evidence-like fields that are not machine-checkable against process data. This study examines evidence-traceable LLM reporting for industrial fault detection and diagnosis. Diagnostic tools populate an evidence record, fixed report fields are checked against that record, and LLM-generated text is evaluated separately from structured evidence transcription. On the Tennessee Eastman Process benchmark, evidence fidelity is measured with Evidence Field Traceability, Untraceable Report Rate, and a preliminary rule-based Report Actionability Score. A passive LLM given all tool outputs in a loose prompt has URR = 77.1%, driven by paraphrased SHAP variable identifiers rather than numeric-field errors. Exact-table prompting and validator-regeneration eliminate structured-field violations when evidence is preassembled. A ReAct implementation, EviFDD-Agent, achieves EFT = 0.997 and URR = 1.4% with DeepSeek-V4-Flash (n = 210), whereas DeepSeek-V4-Pro is less stable and 11.8 times slower. The LLM is therefore positioned above deterministic evidence serialization: critical evidence fields are produced by tools or schema-controlled serializers, while the model is reserved for constrained narrative explanation, recommendation drafting, and auditable tool interaction.

---

## uid: `doi:10.2139/ssrn.6794971`

- title: EntropyRAG: Entropy-Aware Retrieval-Augmented Generation for Knowledge Graph Question Answering
- authors: Donglin Qi, Long Cheng, Haofei Wang, Yan Zhang, Dayan Wan
- affiliations: not stated
- posted: 2026-05-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6794971
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Large language models (LLMs) have shown strong performance in natural lan-guage understanding and generation. However, their knowledge is mainly derived from pre-training corpora, making it difficult to capture emerging domain knowledge in a timely man-ner, and they are prone to hallucinations when evidence is insufficient. Retrieval-augmentedgeneration (RAG) mitigates this issue by leveraging the updatable and auditable structuredfacts in knowledge graphs, thereby improving faithfulness and interpretability. However,existing knowledge graph retrieval methods often underutilize graph-structured informationand lack adaptive control over subgraph expansion during retrieval. To address these issues,we propose an entropy-aware retrieval-augmented generation method for knowledge graphquestion answering. Our framework consists of two stages. In the retrieval stage, we designa GNN-based retriever with an entropy-aware mechanism over edge attention distributionsto adaptively control subgraph expansion, reducing subgraph size while improving the qual-ity of candidate answers and reasoning paths. In the generation stage, we fuse graph-siderepresentations with structured prompts by encoding the retrieved subgraph into a structure-aware graph vector and injecting it into the LLM as a soft prompt to support final answergeneration. Experiments on WebQSP and CWQ show that EntropyRAG achieves com-petitive performance against representative LLM-based and graph-based retrieval baselines,with clearer gains over representative GNN-based retrieval methods on the multi-hop CWQbenchmark.

---
