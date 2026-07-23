# Classification batch 67 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-67.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6845541`

- title: MemLLM: Zero-copy Shared Memory Interface for Unbounded Context Management in on-device LLM Inference
- authors: Hari Prasad Sampatirao
- affiliations: not stated
- posted: 2026-06-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6845541
- keyword hits: large language model, llama, llm, token embedding

### abstract

We present MemLLM, a zero-copy shared memory interface for large language model (LLM) inference that enables unbounded context management on resource-constrained on-device platforms. Inspired by the Linux memif (memory interface) paradigm used in high-performance packet I/O frameworks such as DPDK and VPP, MemLLM establishes a directly mapped virtual address space shared between an application process and an LLM inference server. Token embeddings, key-value (KV) cache entries, and control metadata are exchanged without serialization or copying, eliminating a dominant bottleneck in multi-turn conversational inference. We prototype MemLLM on Windows using named shared memory and TCP-based session establishment, demonstrating the core zerocopy ring protocol in a cross-process setting. An initial empirical evaluation comparing MemLLM against a local HTTP baseline (Ollama) running the same Phi-3-mini-4k model on identical hardware shows that MemLLM exhibits 1.25x lower mean inter-turn latency and significantly lower variance (stdev 20.7s vs 40.3s) as context grows. We further establish that cloud-based inference (Groq API, Llama-3.1-8B) introduces orders-of-magnitude higher latency (563ms mean vs 53s for on-device inference), confirming that the on-device inference domain where MemLLM operates is qualitatively distinct. These preliminary results motivate a more rigorous evaluation on Linux with memfd and hardware accelerators.

---

## uid: `doi:10.2139/ssrn.6923111`

- title: KGER-PP: Knowledge Graph-Enhanced Reasoning for Process Planning based on Large Language Models
- authors: Xueqian Feng, Peihan Wen
- affiliations: not stated
- posted: 2026-06-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6923111
- keyword hits: chain-of-thought, large language model, large language models, llm, llms

### abstract

As manufacturing systems become more complex and dynamic, process planning must adapt to address the increased complexity, uncertainty, and demand for real-time decision-making. Knowledge graph can be used to store and process multi-modal complex process knowledge and support large-scale, dynamic manufacturing environments in form of process knowledge graph (PKG). However, the complex characteristics of PKG schemas and structures remain significant challenges for their effective utilisation in real-world manufacturing scenarios. Therefore, we propose the Knowledge Graph-Enhanced Reasoning framework for Process Planning (KGER-PP), integrating PKG with Large Language Models (LLMs) to enhance process knowledge reasoning. Firstly, a process planning semantic parsing module is introduced to transform natural language questions related to process planning into executable structured representations. Secondly, a structural and semantic enhancement method (StSeEM) is designed to generate knowledge-rich rationales that bridge the interpretability gap in answer generation by integrating structured information at the initial embedding stage and exploiting semantic knowledge via the chain-of-thought reasoning capabilities of LLMs. Thirdly, a graph-guided tuning method is proposed to align explicit reasoning paths with textual representations with a multi-modal future fusion mechanism, mitigating LLMs' hallucination risks through enforced factuality constraints. Finally, experimental results show that the proposed KGER-PP framework achieves the best performance in knowledge-intensive reasoning rationale generation tasks and outperforms the current state-of-the-art methods in process knowledge reasoning research. The code of our work is available at https://github.com/WenWph/KGER-PP.git

---

## uid: `doi:10.2139/ssrn.6947162`

- title: A Verifier-Grounded Knowledge-Based LLM Framework with Reinforcement Learning for Reliable NL-to-CTL Specification Generation
- authors: Ghalya Alwhishi, Jamal Bentahar
- affiliations: not stated
- posted: 2026-06-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6947162
- keyword hits: fine-tuning, large language model, llm, qwen

### abstract

Generating formal temporal-logic specifications from natural-language (NL) requirements is a key challenge for trustworthy knowledge-based systems, because the generated specifications must be both syntactically executable and semantically faithful. Small syntactic errors or temporal-operator misinterpretations can make a formula unusable for model checking or semantically incorrect. This paper presents a reinforcement-learning (RL)-enhanced knowledge-based LLM framework for reliable NL$\rightarrow$CTL specification generation under formal constraints. The framework combines neural structured generation with symbolic verifier feedback to produce NuSMV-ready Computation Tree Logic (CTL) formulas that are syntactically executable and semantically aligned with reference specifications. Unlike prior work that mainly evaluates generated formulas using string-level metrics, we refine the specification generator itself by incorporating NuSMV into training and evaluation through large language model (LLM) fine-tuning and reinforcement learning.The framework is instantiated with two model families, T5 and Qwen3, and evaluated through supervised baselines, verifier-guided syntax refinement, and verifier-grounded semantic refinement. Starting from supervised fine-tuning on a cleaned corpus of 30{,}446 NL--CTL pairs, we apply model-specific refinement strategies: RL-based NuSMV feedback for T5 syntax refinement, supervised NuSMV-guided syntax refinement for Qwen3, and RL-based semantic refinement using truth-set agreement rewards for both model families. Evaluation combines normalized match, NuSMV parse success, and verifier-grounded semantic agreement over shared SMV models, enabling controlled within-model and cross-model comparisons.We also implement interactive NL$\rightarrow$CTL$\rightarrow$NuSMV tools and validate them on a cybersecurity case study. The results show that combining LLM training, RL-based verifier-guided refinement, and symbolic semantic evaluation provides a trustworthy path to reliable temporal-logic specification generation in knowledge-based verification workflows.

---

## uid: `arxiv:2606.17165v3`

- title: Statistical Foundations of LLM-based A/B Testing: A Surrogacy Framework for Human Causal Inference
- authors: Joel Persson, Mårten Schultzberg, Sebastian Ankargren
- affiliations: not stated
- posted: 2026-06-15
- source: arXiv
- link: https://arxiv.org/abs/2606.17165v3
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

Organizations and researchers show increasing interest in using large language models (LLMs) in place of human participants in A/B tests, in the hope of experimenting faster and at lower cost. We study when a treatment effect estimated on LLM outcomes can recover the effect for the human population of interest. Distributional equivalence between LLM and human outcomes would make any standard estimator valid but is unrealistic. We therefore develop a statistical framework that adapts surrogate endpoint theory to LLMs, showing that calibrating LLM outcomes to human outcomes identifies the average treatment effect under surrogacy and comparability conditions that are jointly weaker than distributional equivalence. We present a falsification test for surrogacy and a bound on the worst-case bias from limited overlap between the LLM and human samples. We further show that the stochasticity inherent to LLMs can weaken surrogacy for identification while also introducing bias and variance during estimation, but that using an average over multiple LLM draws per unit as the surrogate mitigates these issues. Simulations validate the results, and an empirical application to the Upworthy Research Archive dataset shows that raw LLM outputs recover only 39% of the human treatment effect while nonparametric calibration closes the gap. A central takeaway is that A/B testing on LLM responses is correct only by assumption, whereas A/B testing on humans is correct by design, and that the required assumptions are hardest to justify precisely where LLMs promise the greatest benefit. We discuss the choice of LLM, prompting, and temperature as design variables, the compounded challenge posed by long-term outcomes, and how to size human pilot studies for validation.

---

## uid: `doi:10.2139/ssrn.6948350`

- title: From Engineering Knowledge to Engineering Decisions: The Emerging Role of Large Language Models in Process Systems Engineering
- authors: Ching-Mei Wen, Marianthi Ierapetritou
- affiliations: not stated
- posted: 2026-06-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6948350
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) have emerged as a new class of tools for interacting with engineering information. Many systems-level engineering studies require information distributed across technical documents, databases, engineering diagrams, operational records, and computational models to be collected, organized, and interpreted before quantitative analysis can begin. LLMs offer new capabilities for supporting these activities through information extraction, knowledge organization, and interaction with computational tools. This perspective examines recent developments in context and harness engineering, knowledge graphs, and agentic workflows and discusses their relevance to engineering applications. Particular attention is given to the growing use of graph-based representations in both Artificial Intelligence (AI) and Process Systems Engineering (PSE), including knowledge graphs, process flow diagrams, P&IDs, signed directed graphs, and supply-chain networks. The discussion focuses on how LLMs can support the integration of engineering information, computational models, and decision-support workflows. The discussion highlights the potential of agentic and knowledge-grounded frameworks for connecting engineering information with computational analysis and decision support.

---

## uid: `doi:10.2139/ssrn.6949575`

- title: Graph-Augmented Intelligence: Structural Representations for Explainable, Efficient, and Grounded Artificial Intelligence
- authors: Pankaj Rahi
- affiliations: not stated
- posted: 2026-06-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6949575
- keyword hits: large language model, large language models, llm, llms, transformer model

### abstract

Graph-based Artificial Intelligence (AI) has emerged as a transformative paradigm wherein graph-structured representations serve as the backbone for enhancing intelligent systems. Unlike traditional AI approaches that operate on vectorized or sequential data, graph-augmented intelligence leverages the inherent relational capacity of graphs to model dependencies, encode external knowledge, and provide structural interpretability. This article presents a comprehensive framework for Graph-Augmented Intelligence (GAI), focusing on three foundational pillars: explainability, efficiency, and groundedness. This research article introduces a novel architecture that integrates dynamic knowledge graphs with large language models (LLMs) to reduce hallucinations while maintaining computational efficiency. Furthermore, a graph-based attention mechanism has been proposed that explicitly models inter-layer dependencies in deep neural networks, enabling model compression via structural pruning. Through extensive experiments on benchmark datasets-including PubMed, FB15k-237, and WebQSP. it is also demonstrated that the nealy proposed GAI framework achieves a 23.4% improvement in F1 score for question answering, reduces model size by 41.7% via graph-aware pruning, and improves explainability metrics by 34.2% compared to baseline Transformer models. Hence the results of the newly proposed framework underscore the potential of structural representations to address critical limitations in contemporary AI systems, paving the way for more transparent, lightweight, and factually reliable models.

---

## uid: `doi:10.2139/ssrn.6958668`

- title: Security Weaknesses in LLM-Generated Source Code: An Empirical Vulnerability Analysis of Iterative AI-Assisted Development
- authors: Halil Dursunoglu, Kaan Sulkalar
- affiliations: not stated
- posted: 2026-06-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6958668
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

Context: Large Language Models (LLMs) are increasingly integrated into software engineeringworkflows for code generation, debugging, refactoring, and feature development. While previousresearch has examined the security of one-shot code generation, the longitudinal impact of iterativeAI-assisted software refinement on software security remains insufficiently understood.Objective: This study investigates how software vulnerabilities evolve throughout iterative AI-assisted development workflows and introduces a framework for measuring security degradationduring conversational software refinement.Method: We propose SecureIterate, a longitudinal evaluation framework that combines promptorchestration, version tracking, static analysis, runtime validation, fuzz testing, and CWE/OWASP-based vulnerability normalization. Using 1,250 generated software versions spanning multiple pro-gramming languages, application categories, and commercial and open-source LLM families, weevaluate vulnerability propagation across repeated refinement stages. Security Drift Score (SDS) andWeighted Security Drift Score (WSDS) are introduced to quantify longitudinal security changes.Results: The experimental results reveal statistically significant vulnerability growth throughoutiterative refinement cycles. Common weaknesses included SQL injection, improper authentication,hardcoded credentials, path traversal, insecure deserialization, and unsafe dependency usage. Cross-model analysis showed that vulnerability propagation occurred across all evaluated LLM families.Runtime validation and fuzz testing identified additional security issues not detected through staticanalysis alone. Security-aware prompting, static-analysis-guided refinement, and dependency verifi-cation reduced vulnerability growth and improved security outcomes.Conclusion: The findings demonstrate that iterative AI-assisted software development can introducemeasurable security drift despite functional improvements. SecureIterate provides a reproducibleframework for evaluating longitudinal software security and highlights the importance of continuoussecurity validation, automated assurance mechanisms, and human oversight in AI-assisted softwareengineering workflows.

---

## uid: `doi:10.2139/ssrn.6857278`

- title: MindVault AI: A Full-Stack RAG-Based Intelligent Study Assistant with Collaborative Learning Support
- authors: Nishanthi Shri, Purushothaman R
- affiliations: not stated
- posted: 2026-06-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6857278
- keyword hits: large language model, llama, llm, retrieval-augmented

### abstract

Students today face significant information overload, struggling to synthesize knowledge from diverse academic sources including PDFs, lecture slides, videos, and web articles. MindVault AI addresses this challenge through a Retrieval-Augmented Generation (RAG) architecture [1] that unifies multiformat document ingestion, dense semantic vector search, and large language model (LLM)-powered response generation into a cohesive, full-stack study assistant. The system ingests PDF documents (including scanned pages via OCR), Microsoft Word files, PowerPoint presentations, YouTube video transcripts, and web articles, converting each source into semantically indexed chunks stored in a FAISS vector index [2]. At query time, a Sentence-BERT encoder [3] retrieves the most contextually relevant passages, forwarded to a Llama-3 model via the Groq inference API to produce grounded, citation-backed answers. Beyond conversational retrieval, MindVault AI offers automated generation of multiple-choice questions, timed examinations, spaced-repetition flashcards, hierarchical mind maps, and document summariesall derived from the learner's own uploaded content. A peruser progress tracker records examination outcomes, identifies weak topic clusters, and visualizes learning trajectories over time. A real-time collaborative Study Rooms feature powered by WebSockets enables shared AI-assisted sessions across multiple users. Evaluations demonstrate strong retrieval quality (context precision 0.84, context recall 0.81), high answer faithfulness (0.87), and an end-to-end query latency under 2 seconds on commodity CPU hardware, confirming practical viability for real-time deployment.

---
