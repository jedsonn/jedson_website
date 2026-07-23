# Classification batch 82 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-82.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6585898`

- title: A Multi-Layer Query Guardrail Framework for Stateless LLM Deployments
- authors: Srinadh Chintakindi
- affiliations: not stated
- posted: 2026-05-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6585898
- keyword hits: large language model, large language models, llm, llms

### abstract

Large Language Models (LLMs) deployed via stateless Application Programming Interfaces (APIs) present a fundamental challenge for application developers: since no conversational state is preserved between calls, users can freely send queries outside the intended application domain, leading to context drift, misuse, and unnecessary API cost. Existing guardrail solutions operate primarily at the model output level or rely on monolithic safety classifiers, leaving the input-side query control problem unaddressed particularly in cost sensitive, domain specific deployments. In this paper, we propose a three-layer query control pipeline designed to enforce conversational context lock-in in a stateless LLM environments. The first layer applies a lightweight word-level filter that intercepts obvious violations before any API call is made. The second layer employs a semantic intent classifier using fastText and GloVe embeddings, trained on over one million samples, to detect subtle out-of-domain queries that evade keyword filters. The third layer uses an LLM-level guardrail prompt as a final safety net to prevent harmful or off-scope responses from reaching the user. Each layer acts as a progressive gate, allowing only contextually valid queries to advance. Our system makes API calls stops domain drift and cuts down the cost of inference while keeping the user experience consistent. This work explains the problem of controlling queries without saving information presents a multi-layer architecture to solve this problem and talks about the design choices made across these layers. We see this as a simple and easy to use alternative to model alignment techniques, for LLM applications that are locked to a specific domain.

---

## uid: `doi:10.2139/ssrn.6690759`

- title: The Metacognitive Bottleneck: Japanese Riddles Reveal Fundamental Limits of Machine Insight and Self-Evaluation in Reasoning AI
- authors: Masaharu Mizumoto, Nguyen Dat, Zhiheng Han, Xingfu Li, Yo Nakawake, Minh Le Nguyen
- affiliations: not stated
- posted: 2026-05-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6690759
- keyword hits: large language model, large language models, llm, llms

### abstract

Abstract: Benchmark saturation and training-data contamination increasingly obscure whether reported gains in large language models (LLMs) reflect genuine advances in reasoning or familiarity with recurring patterns in benchmark problems. We introduce the NazoNazo Benchmark, a renewable and extensible evaluation dataset derived from Japanese children’s riddles that isolates a specific class of reasoning processes: insight-like representational restructuring and metacognitive evaluation. Rather than modeling reasoning in general, these tasks provide a focused test of failure modes that are difficult to detect in standard benchmarks.We curate 201 riddles and establish a human reference on a 120-item subset (n = 126; mean accuracy 52.9%). The benchmark is fully open, low-cost to refresh, and designed for continual evaluation under reduced contamination risk. We evaluate 38 frontier LLMs (2023–2025) under a strict retrieval-free, zero-shot protocol. On the human-comparison subset, non-reasoning models achieve 7.6% accuracy and reasoning-oriented models reach 17.6%, leaving a substantial gap to human performance.Beyond accuracy, analysis of model-generated thought-logs reveals a consistent and a consistent pattern of errors, what we call verification failure, in which models generate correct intermediate candidates but fail to endorse them as final answers. This dissociation between candidate generation and endorsement indicates a metacognitive bottleneck in current systems. By isolating the gap between generation and verification, this work provides a practical framework for diagnosing reasoning reliability and suggests concrete directions for improvement, including better calibration, structured verification, and stopping mechanisms.

---

## uid: `doi:10.2139/ssrn.6610138`

- title: Do LLMs Need Coordinates? A Practitioner's Perspective
- authors: Toshiyasu Watanabe
- affiliations: not stated
- posted: 2026-05-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6610138
- keyword hits: large language model, large language models, llm, llms

### abstract

This paper suggests that one central difficulty in the current use of large language models (LLMs) may lie less in a shortage of knowledge than in a shortage of coordinates. It is offered as the observations of a single practitioner, not as a theoretical claim backed by authority. Two approaches from classical multivariate analysis are recalled: one that commits in advance to a view of what is being studied, and one that lets the axes emerge post hoc from the data. The current mainstream prescriptions, including retrieval augmentation, context-window expansion, and scaling, are read here as large-scale extensions of the second posture. From this perspective, hallucination and model collapse may be read, at least in part, as the sort of convergence one would expect when material is supplied without a specified direction. A modest proposal follows: that a coordinate system, designed by the practitioner in advance, be supplied alongside the material rather than inferred from it. One such set of axes, concerning what exists, when it changes, and who decides, is offered as one example.

---

## uid: `doi:10.2139/ssrn.6684179`

- title: Reduced Social References in Alzheimer’s Disease Speech: A Language-Independent Analysis
- authors: Bárbara Malcorra, Marina Ribeiro, César Rennó-Costa, Lilian  Cristine Hübner
- affiliations: not stated
- posted: 2026-05-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6684179
- keyword hits: large language model, large language models, llm, llms

### abstract

Alzheimer’s Disease (AD) is a neurodegenerative disorder affecting millions worldwide, characterized by significant cognitive impairments, including deficits in language production. Despite extensive research, important questions remain about which specific aspects of communication are most affected by the disease and whether these language changes are consistently identified across different languages or specific to certain idioms. These challenges arise from limited datasets of AD-related discourse and the inherently complex, multidimensional nature of natural language. Under these conditions, Large Language Models (LLMs), a form of artificial intelligence (AI), have demonstrated impressive accuracy in identifying discourse samples from AD patients. However, AI models often function as “black boxes,” offering little insight into the linguistic patterns they detect. In this study, we assess whether a novel explainable artificial intelligence (XAI) technique, which can pinpoint linguistic features associated with the most relevant aspects of speech for classification, provides insights into how evoked speech differs between AD patients and healthy controls in English and Brazilian Portuguese. The English dataset involved the Cookie Theft picture description task, while the Portuguese dataset used the Dog Story narrative task. The models based on the BERT family created for each language dataset achieved over 80% accuracy. Our analysis revealed several shared linguistic features relevant to both models, with a notable decrease in social references within AD speech samples. These reduced social references were identified as critical drivers in the models’ classification decisions, offering valuable insights into the linguistic markers of AD across different languages.

---

## uid: `doi:10.2139/ssrn.6696221`

- title: LLM-augmented taxonomy for >4500 palaeopalynology genera
- authors: Michael  Henry Stephenson, Jiaxi Yang, Alessandro Carniti, Shu-zhong Shen, Jun-xuan Fan, Jieping Ye
- affiliations: not stated
- posted: 2026-05-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6696221
- keyword hits: generative ai, large language model, llm

### abstract

The classification of fossil organisms—paleontological taxonomy—provides the essential language for interpreting Earth’s history by assigning context and information to fossil specimens. However, this knowledge is not only locked within heterogeneous texts in the historical peer-reviewed and other literature, making identification challenging, but is also compartmentalized across continents and geological eras and systems exaggerating differences, rather than indicating similarity and connection. Here, we introduce an open-access Large Language Model (LLM)-augmented taxonomy system (LATS) that seeks to overcome these barriers. Applied to the Jansonius and Hills Catalogue, the definitive 4,500+ genus compendium for Phanerozoic spores and pollen, the LATS converts specialized literature into a globally accessible, machine-readable knowledge graph which enables guided genus-level identification, matching user specimen description with genus diagnoses/descriptions, and also serves as a discovery engine, detecting probable synonymies and morphological trends to reveal new connections through geological time and geography. This framework demonstrates how generative AI can revolutionize taxonomic practice for paleontology and, potentially, for any major biological group, both fossil and extant, whose history is embedded in descriptive literature.

---

## uid: `doi:10.2139/ssrn.6704599`

- title: Interpretable ML and Text-Based LLMs in Finance: Regulatory Explainability and Portfolio Decision Transparency
- authors: Wenhui Ge
- affiliations: not stated
- posted: 2026-05-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6704599
- keyword hits: large language model, large language models, llm, llms

### abstract

This paper reviews the literature on interpretable machine learning and text-based large language models in finance. It argues that explainability in finance serves two distinct but related purposes: meeting regulatory demands and improving transparency in portfolio decisions. Using this distinction, the paper synthesizes prior work on interpretable ML models, applications of LLM-based financial text systems, and grounding architectures that make outputs inspectable and usable. The review highlights common limitations in evidence reliability, point-in-time evaluation, explanation stability, and institutional deployment. It concludes that further progress will depend on linking transparent predictive structure with grounded language-based reasoning.

---

## uid: `doi:10.2139/ssrn.6710203`

- title: PhysCISC: A Process-Credibility Weighted Self-Consistency Voting Framework for Physics Reasoning with Large Language Models
- authors: Tingyu Zhang, Yan Cen
- affiliations: not stated
- posted: 2026-05-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6710203
- keyword hits: chain-of-thought, large language model, large language models, prompting, qwen

### abstract

Self-consistency (SC) improves chain-of-thought prompting by sampling multiple reasoning paths and voting, but it often requires many samples. Confidence-Informed Self-Consistency (CISC) reduces this cost by weighted voting using an answer-confidence signal such as P(True); for physics, this signal can overweight confident but flawed derivations. We propose PhysCISC, which replaces P(True) with a process-credibility signal that reflects the rigor and completeness of a full physics reasoning chain. Each sampled solution is self-scored with a 0–9 rubric (no extra training; one additional forward pass) and then aggregated via softmax-weighted voting. We also build a Chinese physics multiple-choice dataset of 4078 questions (six domains; five reasoning types) curated from printed problem books. On Qwen2.5-7B-Instruct, PhysCISC achieves 60.15% accuracy with 2 samples and 68.86% with 32 samples, improving over SC (57.60% / 67.75%) and CISC (58.58% / 68.20%), and reaching SC’s 32-sample accuracy with about 12 samples. Process-credibility provides stronger within-question discrimination (WQD) than P(True) (0.576 vs. 0.519). We further evaluate on three public physics benchmarks converted to the same four-option format: UGPhysics NV&EX (600), SciBench-Physics (267), and MMLU-Physics (488); PhysCISC is competitive with, or better than, SC and CISC across all three datasets. The dataset and reproducible code are released on Zenodo.

---

## uid: `doi:10.2139/ssrn.6599860`

- title: Pathoscope: An Explainable AI Framework for Scalable Genomic Variant Interpretation
- authors: Aakash Medge, Roshan Gaud, Aditya Sonkar, Shobha Lolge
- affiliations: not stated
- posted: 2026-05-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6599860
- keyword hits: large language model, large language models, llm, llms

### abstract

The rapid growth of genomic sequencing data has introduced significant challenges in the accurate and scalable interpretation of genetic variants, particularly Variants of Uncertain Significance (VUS). Existing bioinformatics tools primarily generate highly technical outputs that often require expert-driven analysis and lack interpretability for broader clinical use. This paper presents Pathoscope, an AI-driven framework designed to enhance the interpretability and efficiency of genomic variant analysis. The proposed system integrates automated variant assessment, ensemble-based computational predictions, and explainable artificial intelligence to generate structured and context-aware interpretations. By combining curated genomic databases with Large Language Models (LLMs), the framework enables the transformation of complex molecular data into meaningful insights. The system employs a modular pipeline architecture supported by parallel data processing and optimized caching strategies to improve scalability and reduce processing time. Experimental evaluation demonstrates that the proposed approach improves interpretability and significantly reduces manual analysis effort compared to conventional workflows. These results highlight the potential of AI-assisted frameworks in advancing genomic intelligence for precision medicine applications.

---
