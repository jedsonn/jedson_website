# Classification batch 62 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-62.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6642390`

- title: scAgent: Agentic Universal Single-Cell Annotation
- authors: Yuren Mao, Yu Mi, Peigen Liu, Ruizhe Yan, Mengfei Zhang, Hanqing Liu, Yunjun Gao
- affiliations: not stated
- posted: 2026-04-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6642390
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Cell type annotation is critical for understanding cellular heterogeneity. Based on single-cell RNA-seq data and deep learning models, good progress has been made in annotating a fixed number of cell types within a specific tissue. However, universal cell annotation, which can generalize across tissues, discover novel cell types, and extend to novel cell types, remains less explored. To fill this gap, this paper proposes scAgent, an agentic universal cell annotation framework based on Large Language Models (LLMs) and Mixture-of-Experts Low-Rank Adaptation (MoE-LoRA). scAgent can identify cell types and discover novel cell types in diverse tissues; furthermore, it is data efficient to learn novel cell types. Experimental studies in 160 cell types and 35 tissues demonstrate the superior performance of scAgent in general cell-type annotation, novel cell discovery, and extensibility to novel cell type.

---

## uid: `doi:10.2139/ssrn.6511898`

- title: Calibrated World Models for AI Agents: Prediction Market Data as Real-Time Context
- authors: Yizhou Liu
- affiliations: not stated
- posted: 2026-04-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6511898
- keyword hits: ai agent, claude, fine-tuning, large language model, large language models, retrieval-augmented

### abstract

Large language models have a knowledge cutoff that prevents them from reasoning accurately about current events. Existing mitigations-web search, news APIs, retrieval-augmented generationreturn narrative text that requires parsing and provides no calibrated probabilities. We propose injecting prediction market data as a compact, structured world model into agent system prompts. Prediction markets aggregate the judgments of participants with real money at risk, producing calibrated probability estimates for geopolitical events, economic indicators, commodity prices, and elections. We introduce the World Awareness Benchmark (WAB), a 44-question evaluation testing whether AI agents can accurately report current world conditions. Ground truth is derived from live prediction market prices. On WAB, a baseline Claude Haiku 4.5 model scores 2.3%, while the same model augmented with an 800-token prediction market world state scores 70.5%-a 31× improvement. The world state injection requires no fine-tuning, no retrieval infrastructure, and adds only ∼800 tokens to the system prompt. We release the benchmark, daily world state snapshots, a Python SDK, and a public API as open resources.

---

## uid: `doi:10.2139/ssrn.6676577`

- title: DyRAG-KT: Generative Student Simulation via Dynamic Graph Retrieval-Augmented Generation
- authors: Xingcheng Fu, Shengpeng Wang, Haitao Huang, Xiang Han, Duong  Thi Thuy Nguyen, Thang  Xuan Nguyen, Xianxian Li
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6676577
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Knowledge Tracing(KT) is a fundamental component of Intelligent Tutoring Systems, aiming to dynamically assess the evolution of students' knowledge states based on their historical interaction behaviors. However, existing educational data faces high sparsity and lacks information about the student learning process. Although Large Language Models (LLMs) provide a new avenue for data augmentation, they exhibit severe logical hallucinations, such as generating invalid learning sequences that violate pedagogical prerequisite relationships, and they cannot effectively capture the dynamic evolution characteristics of student cognition. To address these challenges, this paper proposes Dynamic Retrieval-Augmented Generation for Knowledge Tracing (DyRAG-KT), a new framework combining Dynamic Knowledge Graphs with Retrieval-Augmented Generation to achieve high-quality student simulation and precise prediction. Specifically, the framework models educational knowledge as a dynamic graph structure and deconstructs exercises into fine-grained Dynamic Knowledge Element units to provide explicit semantic boundaries. It establishes a bidirectional feedback loop between the graph propagation-based knowledge tracing module and the retrieval generation module. This mechanism enables the system to diagnose cognitive states in real time and perform knowledge-guided retrieval, ensuring that the generated content strictly follows cognitive development patterns. Extensive experiments on multiple real-world educational datasets validate the effectiveness of the proposed DyRAG-KT framework.

---

## uid: `doi:10.2139/ssrn.6676603`

- title: MMP-Refer: Multimodal Path Retrieval-augmented LLMs For Explainable Recommendation
- authors: Xiangchen Pan, Wei Wei
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6676603
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Explainable recommendations help improve the transparency and credibility of recommendation systems, and play an important role in personalized recommendation scenarios. At present, methods for explainable recommendation based on large language models(LLMs) often consider introducing collaborative information to enhance the personalization and accuracy of the model, but ignore the multimodal information in the recommendation dataset; In addition, collaborative information needs to be aligned with the semantic space of LLM. Introducing collaborative signals through retrieval paths is a good choice, but most of the existing retrieval path collection schemes use the existing Explainable GNN algorithms. Although these methods are effective, they are relatively unexplainable and not be suitable for the recommendation field.To address the issue of the lack of effective integration of multimodal information and collaborative signals in LLM-based explainable recommendations, we propose MMP-Refer, a framework using MultiModal Retrieval Paths with Retrieval-augmented LLM For Explainable Recommendation. We use a sequential recommendation model based on joint residual coding to obtain multimodal embeddings, and design a heuristic search algorithm to obtain retrieval paths by multimodal embeddings; In the generation phase, we integrated a trainable lightweight collaborative adapter to map the graph encoding of interaction subgraphs to the semantic space of the LLM, as soft prompts to enhance the understanding of interaction information by the LLM. Extensive experiments have demonstrated the effectiveness of our approach.

---

## uid: `doi:10.2139/ssrn.6678899`

- title: Semantic and Lexical Retrieval-Augmented Large Language Models for Code Summarization
- authors: Jiawei Wang, Chunli Xie, Wei Zhu, Chunpeng Kang
- affiliations: not stated
- posted: 2026-04-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6678899
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

As software systems continue to grow in scale and complexity, automatically generating readable and semantically accurate code summaries has become increasingly important for program comprehension and software maintenance. Although large language models (LLMs) have demonstrated strong generation capabilities in code summarization tasks, they often produce verbose summaries, omit key information, or suffer from semantic hallucinations when relying solely on source code as input. Retrieval-augmented generation (RAG) methods mitigate these issues by introducing external code-summary examples as references. However, most existing approaches depend on a single retrieval strategy, making it difficult to simultaneously capture deep semantic similarity and precise keyword matching, which limits the quality and stability of retrieved examples. To address these challenges, we propose HyRALLM, a hybrid retrieval-augmented large language model framework for code summarization. Specifically, we first map code and summary representations into a shared semantic space via cross-modal contrastive learning, constructing a dense retriever with stronger semantic alignment. We then integrate the dense retriever with a sparse retriever based on keyword matching to obtain high-quality, functionally relevant reference examples. During the generation stage, we further introduce a multi-candidate generation strategy and a post-processing discrimination mechanism, which guide the LLM to produce more accurate, concise, and semantically consistent summaries under the constraints of retrieved examples. Experimental results on two public benchmark datasets, JCSD and PCSD, demonstrate that HyRALLM consistently outperforms the compared baseline methods across multiple evaluation metrics, including BLEU, ROUGEL, METEOR, and CIDEr. Additional ablation studies and case analyses further verify the effectiveness of the hybrid retrieval strategy and generation optimization mechanisms in improving summary quality, reducing semantic deviation, and enhancing generation robustness.

---

## uid: `doi:10.2139/ssrn.6584019`

- title: Understanding Emergent Abilities in Large Language Models
- authors: Yuanen Su
- affiliations: not stated
- posted: 2026-05-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6584019
- keyword hits: in-context learning, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) have demonstrated a wide range of capabilities that appear to emerge only at scale, including multi-step reasoning, in-context learning, tool use, and even rudimentary forms of planning. These emergent abilities are often unpredictable, poorly understood, and difficult to control, raising fundamental questions about the nature of intelligence in modern machine learning systems. This research aims to systematically investigate the mechanisms underlying such emergent behaviors, with the goal of transforming them from empirical observations into principled, predictable phenomena.

---

## uid: `doi:10.2139/ssrn.6599978`

- title: Automated Multi-Dimensional Quality Scoring for Customer Service Operations Using Large Language Models: Production Design, Deployment, and Empirical Analysis
- authors: Ali Aghabeigiha
- affiliations: not stated
- posted: 2026-05-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6599978
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

Quality assurance (QA) in large-scale customer service operations has long been constrained by low coverage, human subjectivity, and reactive measurement cycles. Traditional customer satisfaction surveys capture fewer than 30% of interactions, while manual QA reviews cover only approximately 1% of chats. We present TSS (Transaction Satisfaction Score), a multi-dimensional automated scoring framework that leverages Large Language Models (LLMs) via Google BigQuery ML (BQML) to evaluate 100% of customer-agent chat interactions in real time. Deployed at a global food delivery platform operating across 18 markets, the system processes approximately 35,000 conversations daily. TSS combines six weighted evaluation dimensions-First Reply Time, Responsiveness, Resolution Quality, Agent Empathy, Sentiment Recovery, and Efficiency (AHT)-into a single normalized score ranging from 0 to 10. The framework incorporates four special logic guardrails to prevent score gaming and misclassification, and a hierarchical Root Cause Analysis (RCA) module that attributes interaction friction to one of seven causal categories. We present the system architecture, scoring rubric design, iterative version evolution, and an empirical analysis of 11,504 customer interactions from a 30-day pilot deployment. Results reveal that Fulfillment Failure (53.3%) and Process Friction (21.3%) are the dominant drivers of negative interactions-insights previously invisible to the organization. The system achieved 99% conversation coverage and 95% calculation reliability in production. Our work demonstrates that structured LLM prompting with deterministic guardrail logic can deliver scalable, objective, and operationally actionable QA at a scale unreachable by human review alone.

---

## uid: `doi:10.2139/ssrn.6704338`

- title: Regulatory Reporting Architecture Using Event Streaming: A CAT and FINRA Case Study An AI-Driven Cloud-Native Architecture MLflow, and Large Language Models
- authors: Chittaranjan Pradhan
- affiliations: not stated
- posted: 2026-05-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6704338
- keyword hits: large language model, large language models, llm, retrieval-augmented

### abstract

The SEC's Consolidated Audit Trail (CAT) mandate under Exchange Act Rule 613 and FINRA Rule 6800 Series requires every broker-dealer to report complete order lifecycle data for all U.S. NMS equity and listed options securities to FINRA's Central Repository by 8:00 AM Eastern Time the following trading day. Existing rule-based and batch-oriented compliance pipelines fail to meet CAT's real-time requirements and lack the intelligence to detect spoofing, layering, and data quality anomalies proactively. This paper presents AI-CAT, an AI-driven cloud-native data engineering framework for CAT/FINRA regulatory reporting. AI-CAT integrates Apache Kafka for real-time event streaming, Databricks Lakehouse with Apache Spark Structured Streaming for governed medallion transformation, Apache Pinot for sub-second OLAP on order lifecycle events, Apache Trino for federated CAIS correlation, and-critically-a multi-layer AI intelligence plane comprising: Databricks MLflow-managed gradient boosting models for real-time CAT schema anomaly detection; an LSTM-based spoofing and layering surveillance model trained on order lifecycle event sequences; and a Retrieval-Augmented Generation (RAG) large language model layer for automated regulatory interpretation and error repair generation. Anchored to the official FINRA CAT Technical Specifications v4.1, FINRA Regulatory Notice 24-09 on AI governance, and FINRA's 2025 Annual Regulatory Oversight Report, AI-CAT achieves: T+0 real-time CAT event reporting with 28-second end-to-end latency; 99.1% precision on CAT anomaly detection (F1=0.943); automated error repair reducing manual remediation by 94%; zero FINRA violations over 24 months; and 52% infrastructure cost reduction. AI-CAT represents the first published framework explicitly integrating LLM-based regulatory intelligence into a production CAT/FINRA reporting pipeline.

---
