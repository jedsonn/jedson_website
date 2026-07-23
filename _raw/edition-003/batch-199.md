# Classification batch 199 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-199.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6739460`

- title: A Multi-Stage Intent Classification and Retrieval Framework for Intelligent Agricultural Advisory
- authors: Soumalya De, Rousan Ali
- affiliations: not stated
- posted: 2026-05-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6739460
- keyword hits: large language model, llama, retrieval-augmented

### abstract

Accurate intent detection and semantic retrieval are essential for intelligent farmer advisory systems operating under noisy, multilingual inputs. Existing approaches often rely on predefined intents or static retrieval methods, resulting in poor generalization. This paper proposes a hybrid intent-aware Retrieval-Augmented Generation (RAG) framework that combines fuzzy intent matching and embedding-based semantic similarity with a confidence-driven Zero-Shot fallback mechanism. A hybrid confidence score is computed for intent selection, and when the confidence falls below a threshold, a Zero-Shot large language model is invoked to prevent forced misclassification. The system further incorporates probabilistic query interpretation to handle spelling errors and ambiguity. Semantic retrieval is performed using sentence-level embeddings with a scalable Pinecone vector database, followed by context-aware response generation using a fine-tunable LLaMA-3.1-8B model. Experimental results and ablation studies demonstrate that the proposed approach achieves superior performance, attaining an accuracy of 0.84 compared to conventional baselines, while maintaining a balanced Zero-Shot invocation rate. Thus this paper proposes a novel decision support system to agronomy by providing an overview of the recent trends.

---

## uid: `doi:10.2139/ssrn.6741395`

- title: Patch-Aware Retrieval-Augmented Generation for Large Language Model Decision Support in Transportation Infrastructure Delivery
- authors: Dan Liu, Hao Wang, Hao  Frank Yang, Maria Santo, Bin Hu, Giri Venkiteela
- affiliations: not stated
- posted: 2026-05-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6741395
- keyword hits: large language model, llm, retrieval-augmented

### abstract

Transportation infrastructure agencies rely on large, frequently updated specification documents to support materials acceptance, contract administration, and construction compliance. However, after the base specifications are published, agencies may issue official amendment bulletins that revise, replace, or remove selected subsections. Conventional large language model (LLM) systems with retrieval-augmented generation (RAG) can retrieve relevant base text, but may overlook these amendments, producing answers that appear correct while being contractually outdated. This study proposes DS-TID — Decision Support for Transportation Infrastructure Delivery — an amendment-aware RAG framework for LLM-based decision support in transportation construction specifications. DS-TID instantiates a Patch-Aware RAG architectural pattern in which a stable base specification index is augmented at retrieval time by a section-identifier-keyed amendment registry. When a retrieved base section is affected by an active bulletin, the corresponding amendment is deterministically injected into the LLM prompt as authoritative evidence, together with change-type and effective-date metadata. This design preserves the stability of the base index and avoids re-embedding the full corpus whenever new bulletins are issued. The framework also integrates hierarchy-preserving chunking, row-level table evidence units, adaptive dense–lexical retrieval fusion, citation-constrained generation, and conservative abstention. We implement DS-TID using the Standard Specifications for Road and Bridge Construction, the Division Construction and Materials Material Procedures, and active Baseline Document Change (BDC) bulletins. On a 100-query expert-annotated benchmark, the system achieves 0.90 end-to-end accuracy and correctly abstains on all out-of-scope queries in the tested partition. On a 14-question practitioner-grade benchmark, it reaches 94% aggregate response-quality accuracy, with clear gains over baseline RAG systems and commercial-chatbot baselines. The results show that reliable LLM decision support for transportation infrastructure delivery requires not only semantic retrieval, but also up-to-date amendments, preserved document structure, and clear refusal to answer when the evidence is insufficient.

---

## uid: `doi:10.2139/ssrn.6746678`

- title: The Agentic GTM Stack A Comprehensive Conceptual Framework for Autonomous Market Validation, Enterprise Cognition, and Human-Guided Go-To-Market Systems
- authors: Deepak Amirtha Raj
- affiliations: not stated
- posted: 2026-05-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6746678
- keyword hits: agentic, large language model, large language models

### abstract

Traditional go-to-market systems were historically constrained by manual workflows, fragmented tooling, and operational bottlenecks. Recent advances in large language models, orchestration systems, and persistent memory infrastructure have enabled the rise of agentic GTM systems. This paper introduces "The Agentic GTM Stack," a conceptual framework describing how autonomous yet human-guided AI systems transform outbound from a transactional sales mechanism into a persistent market cognition architecture. The framework proposes seven interconnected layers: Infrastructure, Market Intelligence, Identity, Orchestration, Cognitive, Execution, and Memory. Together, these layers enable startups and enterprises to rapidly validate product-market fit, compress learning cycles, accelerate trust formation, and continuously adapt based on real-world market interaction.

---

## uid: `doi:10.2139/ssrn.6748939`

- title: LegalSaathi: An AI-Powered Multilingual Legal Document Platform for Inclusive Legal Access in India
- authors: Sujal Karawade
- affiliations: not stated
- posted: 2026-05-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6748939
- keyword hits: large language model, llm, retrieval-augmented

### abstract

Access to legal services in India remains deeply inequitable. Over 65% of India's population resides in rural or semi-urban areas with limited access to legal professionals, and existing legal technology tools are predominantly English-centric and designed for trained lawyers. This paper presents LegalSaathi, an AI-powered multilingual legal document platform engineered to bridge this gap by serving two distinct user segments: educated legal professionals and uneducated or rural citizens. The system employs a Retrieval-Augmented Generation (RAG) pipeline grounded in verified Indian legal databases-Indian Kanoon and SCC Online-to prevent hallucinated citations, a persistent failure mode in large language model (LLM)-based legal systems. LegalSaathi introduces a dual-interface design (Simple Mode and Advanced Mode), an 8-step document scanning workflow, a 7-step document creation workflow, and 14 functional modules spanning AI drafting, multilingual summarization, risk detection, argument building, and verified lawyer connectivity. The platform further proposes 10 additional modules including Aadhaar eSign integration, DigiLocker identity verification, offline mode, and a court date manager. Evaluation targets include 100% citation accuracy, 94%+ query response precision, and a user satisfaction score of 4.2/5. This work represents a significant contribution to the democratization of legal access in developing economies.

---

## uid: `doi:10.2139/ssrn.6749434`

- title: InstructGen: Generating Scalable and Realistic Visual-Language Navigation Data with Unlabeled Internet Videos
- authors: yu yan, Peiyang Li, Jianqin Yin
- affiliations: not stated
- posted: 2026-05-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6749434
- keyword hits: large language model, large language models, prompt engineering

### abstract

Vision-and-Language Navigation (VLN) task requires agents to navigate autonomously in 3D visual environments by following natural language instructions. High-quality training data is essential for enhancing both navigation performance and generalization capability. While synthetic path–instruction pairs have significantly increased data scale, template-based generation struggles to align with navigation processes and deviates from real human–robot interaction instructions, leading to an instruction-level sim-to-real gap. To address it, we propose InstructGen, a VLN path-instruction pairs generation framework based on Multimodal Large Language Models (MLLMs), and introduce the corresponding dataset GenVLN. Specifically, we use YouTube house tour videos as realistic navigation scenes and design an innovative prompt engineering strategy to activate MLLM’s visual understanding and text generation capabilities, enabling the model to generate instructions aligned with visual observations and spatial information at varying granularities. Additionally, we design a self-supervised correction mechanism that optimizes the consistency between instructions and navigation trajectories and the fluency of language expressions, reducing potential hallucinations during generation. Experiments on R2R and RxR show that agents trained with GenVLN achieve strong navigation performance and robust generalization in unseen environments, highlighting the effectiveness of high-quality generated instructions.

---

## uid: `doi:10.2139/ssrn.6749439`

- title: Knowledge-Grounded LLM-Driven Augmentation via Graph RAG for Phishing URL Detection
- authors: Mi-Ju Kim, Seok-Jun Buu
- affiliations: not stated
- posted: 2026-05-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6749439
- keyword hits: llm, retrieval-augmented

### abstract

Integrating prior rule knowledge into generative data augmentation remains an open problem when detectors must generalize under distribution shift. URL-based phishing illustrates this problem at scale. Numerous detection rules have been proposed, yet adversaries continually mutate URL structures, eroding the effectiveness of static rule-based systems and causing the training distribution to drift away from deployment conditions. Although LLM-based augmentation can expand training diversity, unconstrained generation risks producing samples that are structurally plausible but phishing-inconsistent, limiting their utility for detector training. To address these challenges, this study proposes a knowledge-grounded augmentation framework that integrates a phishing rule knowledge graph with Graph Retrieval-Augmented Generation (Graph RAG) and performs LLM-driven URL augmentation, instantiated for phishing URL detection. The system reconstructs prior rule lists and association-rule information into a searchable graph structure and injects them, together with dataset-adjusted risk scores, into LLM prompts to generate structurally plausible phishing URL variants. After syntax validation and deduplication, the resulting samples are used to train a dual-branch detector that combines character-level and word-level URL representations. Experiments on five datasets show that the proposed system achieves consistently strong performance, with the best result of 99.81% accuracy and an F1-score of 0.9970 on DS1. Additional analyses confirm that the generated URLs preserve alignment with the original phishing distribution while providing structural diversity beyond simple replication.

---

## uid: `doi:10.2139/ssrn.6676238`

- title: Algorithmic Accountability in the Age of Agentic Accounting: Bridging the "Skepticism Gap" in Autonomous Multi-Agent Workflows
- authors: Muhammad Bilal Mianoor
- affiliations: not stated
- posted: 2026-05-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6676238
- keyword hits: agentic, generative ai

### abstract

As the accounting profession shifts from generative AI "chatbots" to autonomous "Agentic AI" systems, a critical regulatory and ethical vacuum has emerged. This paper identifies the "Skepticism Gap", the dangerous erosion of professional auditor judgment when faced with autonomous, multi-agent financial workflows. By synthesizing recent developments in Agentic AI Optimization (AAIO) and current Australian regulatory shifts, this note proposes a Tri-Level Verification Model to restore human accountability in increasingly automated financial ecosystems.

---

## uid: `doi:10.2139/ssrn.6702761`

- title: Agentic AI Systems: Architectures, Autonomy, and Emergent Behaviours
- authors: Rizwan Tanveer
- affiliations: not stated
- posted: 2026-05-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6702761
- keyword hits: agentic, large language model

### abstract

Background. Agentic artificial intelligence systems, defined by their capacity to reason, plan, and act autonomously through external tools and environments, represent a categorical shift in the operational profile of deployed AI. Architectures grounded in reasoning-and-acting paradigms, plan-and-execute decompositions, and tool-augmented designs have moved from research prototypes into enterprise deployment within three years, yet the security, safety, and governance literature has not kept pace with the speed of operational adoption. Purpose. This paper synthesises the contemporary literature on agentic AI architectures, autonomy taxonomies, emergent behaviours, memory and state management, and evaluation methodologies. It positions agentic AI as a distinct security and governance category requiring frameworks not satisfied by predictive AI controls, large language model controls, or traditional software assurance practices. Approach. The paper adopts a narrative literature review methodology drawing on authoritative primary sources, including the OWASP Top 10 for Agentic Applications (2025), the Cloud Security Alliance MAESTRO framework (2025), the DeepMind Levels of AGI autonomy taxonomy (Morris et al., 2024), foundational agent architecture research (Yao et al., 2023; Wang et al., 2024), and the emerging agentic red-teaming and evaluation literature. Findings. Three structural findings are advanced. First, agent architectures introduce attack surfaces (tool invocation, memory persistence, multi-step reasoning trajectories) that have no direct analogue in either traditional software or non-agentic AI systems. Second, autonomy is best treated as a continuum, operationalised through delegation boundaries, rather than as a binary property, with distinct security implications at each level. Third, evaluation methodologies designed for static models systematically underestimate risk in dynamic agentic systems, requiring red-teaming approaches that test for emergent behaviours, goal drift, and cascading failures across multi-step trajectories. Implications. Practitioners deploying agentic AI require architecture-aware governance: tool-invocation controls, memory-hygiene practices, autonomy classification at the system-design stage, continuous behavioural monitoring, and red-teaming methodologies tailored to multi-step agent operations. The paper provides a structured reference for translating architectural choices into security and governance controls.

---
