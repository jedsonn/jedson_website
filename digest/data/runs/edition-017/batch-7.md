# Classification batch 7 of 20, edition 17

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-017/batch-7.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7190278`

- title: Beyond the Black-Box Cloud: How Liquid AI Fits the Operational and Ethical Realities of Health and Social Care
- authors: James A Lomastro
- affiliations: not stated
- posted: 2026-08-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7190278
- keyword hits: large language model, large language models, llm, llms

### abstract

The rapid integration of Large Language Models (LLMs) into healthcare and social services has exposed a fundamental mismatch. Commercial AI is engineered for cloud-based, centralized, and largely static operation, optimized for the economics of consumer search, retail recommendation, and marketing content. Human care systems operate on the opposite set of terms: decentralized, privacy-sensitive, continuously changing, and answerable to statutory and accreditation obligations that carry no equivalent in the commercial internet. When a model built for one environment is dropped into the other, the mismatch does not stay theoretical. It shows up as PHI transiting servers an organization does not control, as unpredictable per-token bills that compete with direct care budgets, and as generalist models that reason about Medicaid eligibility with the same statistical looseness they bring to writing ad copy.

---

## uid: `doi:10.2139/ssrn.7240159`

- title: CyberRerankBench: Benchmarking Rerankers for Cybersecurity Retrieval-Augmented Generation
- authors: Nasheet Khan, Md  Shariful Islam, Sajal Saha
- affiliations: not stated
- posted: 2026-08-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7240159
- keyword hits: agentic, large language model, large language models, llm, llms, retrieval-augmented

### abstract

Retrieval-Augmented Generation (RAG) is increasingly used to make Large Language Models (LLMs) more reliable in cybersecurity by grounding outputs in external evidence. But RAG is only as good as what it retrieves, and the reranking stage that filters that evidence has not been tested against conditions cybersecurity actually presents: noisy logs, attack patterns that look nearly identical in embedding space, and reasoning that must trace back to formal policy. We introduce CyberRerankBench to close this gap. The benchmark sits inside an agentic Network Intrusion Detection System (NIDS) pipeline combining Vertical Federated Learning (VFL) for data-local detection across enterprise domains, SHAP-based attribution for explainability, and LLM reasoning constrained to a knowledge base spanning MITRE ATT\&CK, NIST SP 800-53, CIS Controls v8, and ISO/IEC 27001. Retrieval queries are built dynamically from detection outputs and attribution signals, so reranking is evaluated under conditions resembling an actual SOC workflow rather than a static document set. We test ten retrieval configurations across three tracks (Section~\ref{sec:terminology}): six modes on the policy corpus, two on a domain-index ablation, and two on a response playbook track, scored with headline MiniLM metrics plus parallel grades from CySecBERT, CTI-BERT, and SecureBERT. Using CICIDS-2017, we run 250 stratified scenarios per track, 2{,}500 mode--scenario rows total. Dense MiniLM retrieval leads on faithfulness for the policy corpus track; the response playbook track improves pool recall but weakens utilization; cyber-domain encoders reorder rankings, revealing an encoder--corpus mismatch. No reranker wins everywhere — we treat class- and encoder-aware routing as a direction for future work.

---

## uid: `arxiv:2608.06202v1`

- title: What Current AI Benchmarks Leave Unmeasured: Modality, Search, Citations, and Implications (for Safety Evaluations)
- authors: Ro Encarnación, Tina Behzad, Emma Lurie, Danaé Metaxa
- affiliations: not stated
- posted: 2026-08-06
- source: arXiv
- link: https://arxiv.org/abs/2608.06202v1
- keyword hits: chatgpt, large language model, llm, llms

### abstract

Large language model (LLM) benchmark evaluations are routinely used to support claims about model safety, reliability, and deployment readiness. Yet most evaluations rely on a single access modality (model APIs), perform a single run per prompt, and report accuracy as the primary outcome metric, without accounting for conditions such as web search that may have effects on model behavior in deployment. We audit these assumptions for one of the most widely-used LLMs, comparing two modalities, ChatGPT's chat UI and OpenAI's API, with and without web search enabled. We use a stratified total sample of 401 prompts from two popular benchmarks, BBQ and SafetyBench, collecting 4,812 total responses across three repeated runs per prompt. Beyond standard performance measures, we evaluate model output dimensions including response consistency, response text similarity, citation grounding, and abstention behavior. For instance, chat UI responses were less accurate than API responses on both benchmarks with search disabled. Enabling web search reduced accuracy by up to 8 percentage points, and even reversed the direction of modality performance trends for one benchmark. Repeated runs of the same prompt produced inconsistent responses in up to 21\% of prompts. The two modalities also grounded answers in different citations, and abstention behavior was also inconsistent across both modalities. These results illustrate that, even within a model family, reporting only simple accuracy metrics can obscure important forms of model behavioral variation relevant to AI safety assessments. We argue that AI safety evaluations should systematically account for modality, multi-run consistency, search conditions, and response-level behaviors to better reflect how deployed AI systems behave in practice.

---

## uid: `arxiv:2608.06123v1`

- title: Poli-Bias: Understanding and Measuring Large Language Model Biases in International Political Conflicts
- authors: Massi-Nissa Abboud, Aladin Djuhera, Elena Cabrio, Holger Boche
- affiliations: not stated
- posted: 2026-08-06
- source: arXiv
- link: https://arxiv.org/abs/2608.06123v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Measuring political bias in large language models (LLMs) remains challenging as it can manifest through subtle differences in framing, argumentation, and legal reasoning that are difficult to capture with a single metric. In this work, we introduce Poli-Bias, a counterfactual framework for measuring whether LLMs treat legally equivalent conflict scenarios differently depending on the countries involved. Poli-Bias compares responses to paired prompts in which country identities are systematically swapped across diverse geopolitical relationships, legal violations, and reasoning tasks. Rather than reducing bias to a single judgment, our framework decomposes response disparities into five interpretable dimensions, revealing how and where unequal treatment manifests. Across 13 contemporary LLMs spanning diverse model families and sizes, we find that country identities and user affiliations can systematically affect how equivalent actions are described, evaluated, and defended under international law. Our results thus establish Poli-Bias as a fine-grained framework for auditing political even-handedness and sycophancy in LLMs.

---

## uid: `arxiv:2608.05823v1`

- title: Decomposed Entailment for Factuality Checking and Hallucination Detection
- authors: Achir Oukelmoun, Nasredine Semmar, Gaël De Chalendar
- affiliations: not stated
- posted: 2026-08-06
- source: arXiv
- link: https://arxiv.org/abs/2608.05823v1
- keyword hits: large language model, large language models, llm, llms

### abstract

The reliability of Large Language Models (LLMs) is often compromised by factual inconsistencies, including hallucinations---cases where generated content is not supported by the underlying source. We present HallDetect, a lightweight, reference-free, and black-box framework for hallucination detection that we evaluate not only on summarization but across a broader range of source-grounded generation settings. HallDetect builds on decomposition-based factuality evaluation: generated content is decomposed into atomic claims, each verified by a compact encoder-based entailment model through a contrastive formulation over a multi-scale library of source chunks, and aggregated with an asymmetric score in which a single confidently contradicted claim flags the response. Under a controlled protocol in which all methods share the same 4-bit quantized backbones and consumer-grade hardware budget, HallDetect outperforms comparably resourced generative and embedding-based baselines on three of four benchmarks while remaining stable across backbone families, and yields a claim-to-span audit trail that localizes each error.

---

## uid: `doi:10.2139/ssrn.7203138`

- title: Green AI Beyond Operational Energy GAILA: A Lifecycle-Oriented Environmental Reporting and Decision-Support Framework for Large Language Models Conceptual Article / Working Paper
- authors: Alyaa Sabri Awadh
- affiliations: not stated
- posted: 2026-08-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7203138
- keyword hits: large language model, large language models, llm, llms

### abstract

The environmental discussion surrounding large language models (LLMs) is frequently reduced to the electricity used during model training or inference. Although these operational indicators are essential, they do not capture the full environmental burden of AI systems, which also depends on semiconductor and server manufacturing, data acquisition and storage, facility cooling, electricity sourcing, water consumption, hardware utilization, and end-oflife practices. This conceptual article introduces the Green AI Lifecycle Assessment (GAILA), a lifecycle-oriented environmental reporting and decision-support framework for LLM systems. GAILA organizes environmental evidence across six dimensions: hardware manufacturing; data acquisition and storage; model training; model optimization and inference; infrastructure operation; and hardware end-of-life management. The framework requires an explicit decision question, system boundary, functional unit, evidence provenance, normalization procedure, uncertainty disclosure, and joint interpretation of environmental indicators with service-quality metrics such as accuracy, throughput, latency, and memory demand. Rather than collapsing heterogeneous impacts into a single universal sustainability score, GAILA produces a multidimensional lifecycle profile that identifies hotspots, excluded stages, trade-offs, and context-dependent deployment choices. The article positions GAILA relative to operational carbon trackers, inference-energy benchmarks, and conventional life-cycle assessment, and illustrates how it can support researchers, cloud providers, universities, public institutions, and regulators. A research agenda is proposed for empirical validation, machine-readable reporting templates, interoperable datasets, uncertainty analysis, and governance-oriented sustainability disclosure. GAILA is presented as a reporting and decision-support framework, not as a certification standard or a substitute for direct power measurement and formal life-cycle assessment.

---

## uid: `doi:10.2139/ssrn.7207699`

- title: Explainable Artificial Intelligence as AI Literacy Scaffolding
- authors: Brady Lund, Zoë Abbie Teel, Brett Porter, Anuradha Chandrasekaran
- affiliations: not stated
- posted: 2026-08-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7207699
- keyword hits: large language model, large language models, llm, llms

### abstract

Purpose. This conceptual paper responds to the growing gap in AI literacy among users of large language models (LLMs) and other artificial intelligence systems in recent years. While explainable AI (XAI) has largely been framed as a mechanism for transparency and accountability, its potential to be used as a developmental learning support for end users remains underexplored. The purpose of this paper is to conceptualize explainability as a form of literacy scaffolding that supports the gradual, in-situ development of AI literacy skills through explanation-driven interaction. Design. A conceptual framework is developed through an integrative analysis of literature from explainable AI, AI literacy, educational scaffolding theory, and human-AI teaming research. Key concepts are defined, and theoretical parallels are drawn between scaffolding processes in education and explanation-driven interaction with AI systems. Findings. We argue that AI explanations can function as a scaffold that supports users in learning not only about specific outputs but also about model behavior, limitations, and potential bias. This framework is organized around three core scaffolding principles: the contingent support calibrated to the learner's Zone of Proximal Development, progressive fading of explanatory support as competence grows, and the reframing of explanations as entry points for inquiry rather than disclosure endpoints. These principles collectively support the development of calibrated trust among users rather than uncritical acceptance or unwarranted skepticism toward AI models. Originality/Value. This paper offers a theoretical framework for understanding explainability as AI literacy scaffolding and outlines implications for the design and evaluation of XAI systems. It further proposes methodological approaches for empirically identifying and measuring scaffolding behavior in user interactions with XAI. By positioning explainability as a mechanism for fostering durable AI literacy and calibrated trust, this work contributes to information science scholarship on human–AI interaction and responsible AI use

---

## uid: `doi:10.2139/ssrn.7201826`

- title: "Numbers Don't Speak for Themselves": Words, Narrative, and Storytelling in Financial Decision-making
- authors: Mark Rzepczynski
- affiliations: not stated
- posted: 2026-08-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7201826
- keyword hits: large language model, large language models, llm, llms

### abstract

The dichotomy between verbal and numerical information and valuation models is a finance issue underexplored in descriptions of investment strategies. Positive finance focuses on quantitative decisionmaking; however, normative finance demonstrates that words and narratives convey information, impart meaning, drive sentiment, and impact markets. A growing body of work applies natural language processing (NLP) to measure sentiment and large language models (LLMs) to tokenize linguistic information, linking textual signals to asset returns and driving investment strategies. Yet the mechanisms by which language shapes investment behavior and decision-making remain underexamined. Neither investment behaviors nor investment strategies are based solely on numbers; words and narratives influence risk and return expectations and drive investor activity. Exploring the use of language is critical because narrative assessment is increasingly important for describing market sentiment and memes, as well as for inputs and outputs for NLP and LLM algorithms.

---
