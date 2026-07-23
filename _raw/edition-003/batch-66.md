# Classification batch 66 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-66.answer.json` as a JSON array.

---

## uid: `arxiv:2606.11238v2`

- title: Artificial Intelligence in Ship Finance: Applications, Opportunities, and a Case Study in AI-Augmented Loan Origination
- authors: Lasse Dierich, Orestis Schinas
- affiliations: not stated
- posted: 2026-05-29
- source: arXiv
- link: https://arxiv.org/abs/2606.11238v2
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Ship finance is a data-intensive and document-heavy segment of asset-based lending, requiring the integration of financial, technical, contractual, and regulatory information from heterogeneous and largely unstructured sources. Increasing environmental regulation and ESG reporting requirements are adding further complexity to underwriting and loan-origination processes. Recent advances in artificial intelligence (AI), particularly large language models (LLMs), create new opportunities for processing and analysing such information. This paper reviews potential applications of AI in ship finance, with a particular focus on LLM-based systems for document comprehension, information extraction, and workflow automation. We present ShipFinance.ai, a modular agentic architecture to support loan application workflows in ship finance. The proposed system combines an LLM-based extraction module, financial analysis components, external maritime data services, and a controlled document-generation module with a chatbot interface to support the preparation of standardized financing applications. The paper discusses the key challenges for using such models in production. We argue that AI-assisted systems can support maritime finance professionals in managing increasingly complex information and reporting requirements.

---

## uid: `doi:10.2139/ssrn.6842778`

- title: The Zero-Training Enterprise Brain: A Live Semantic Reasoning Architecture for Training-Free Organizational Intelligence
- authors: Shashank Kumar
- affiliations: not stated
- posted: 2026-06-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6842778
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) have become the default engine for enterprise AI, but their fundamental limitations-prohibitive training costs, catastrophic hallucination, staleness, and inability to guarantee correctness-render them unsuitable for high-stakes organizational reasoning. We propose a radical alternative: a Zero-Training Enterprise Brain (ZTEB), a purely symbolic, real-time reasoning architecture that never sees a dataset. ZTEB ingests live enterprise events into a continuously updated semantic graph, then answers queries through deterministic inference over explicitly asserted facts and rules. No training, no fine-tuning, no probabilistic token prediction, and therefore no hallucinations. Every answer carries full provenance, every "I don't know" is an intentional output rather than a silent gap, and the system reflects the organization's current state with sub-second latency. We present the formal architecture of ZTEB, a reference implementation atop Apache Kafka, Neo4j, and a RETE-based rule engine, and a concrete evaluation plan for comparing it against state-of-the-art LLM-based retrieval systems on accuracy, cost, latency, and hallucination rate. This paper argues that the future of enterprise AI lies not in larger models but in structured, live, deterministic reasoning.

---

## uid: `doi:10.2139/ssrn.6810323`

- title: Human-AI Interaction Across Predictive, Generative, and Agentic AI
- authors: Rizwan Tanveer
- affiliations: not stated
- posted: 2026-06-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6810323
- keyword hits: agentic, generative ai, large language model, large language models

### abstract

Background. Human-AI interaction has moved from a human-computer interaction research topic to an operational and regulatory concern. The April 2025 rollback of an OpenAI model update after the system became, in the company's own characterisation, overly flattering or agreeable, the March 2026 Science publication demonstrating that sycophantic AI reduces prosocial intentions and promotes dependence, and the August 2026 implementation deadline for European Union AI Act Article 14 human oversight requirements have placed appropriate reliance, calibrated trust, and meaningful oversight at the centre of practitioner and regulatory attention. The literature, however, remains fragmented across disciplines, modalities, and jurisdictions. Purpose. This paper provides a comprehensive synthesis of human-AI interaction research and practice across three contemporary AI modalities, predictive, generative, and agentic, and integrates this synthesis with the regulatory architectures emerging in the European Union and the Gulf Cooperation Council. The paper is designed as a reference contribution for the wider fifteen-paper slate and as a scholar-practitioner resource for senior cybersecurity, governance, and risk audiences. Approach. The paper adopts a narrative review methodology combining contemporary 2024 to 2026 empirical literature on trust calibration, appropriate reliance, and oversight effectiveness; primary regulatory document analysis (the EU AI Act, ISO/IEC 42001, NIST AI Risk Management Framework, UAE Information Assurance Standards, UAE Personal Data Protection Law, the UAE Charter for the Development and Use of Artificial Intelligence, and Saudi Arabian regulatory instruments); and analysis of recent documented incidents including the OpenAI sycophancy rollback and the body of academic work on emergent sycophancy in large language models. Findings. Three observations emerge from the synthesis. First, the constructs of trust, calibration, and reliance, while conceptually distinct, are increasingly conflated in practitioner discourse; appropriate reliance, the behavioural outcome that practitioner and regulatory frameworks ultimately require, is empirically distinguishable from trust as an attitude and warrants separate measurement. Second, the modality-specific risk profiles differ substantially: predictive AI risks are concentrated in confidence miscalibration and rubber-stamp oversight; generative AI risks are concentrated in sycophancy and anthropomorphic trust manipulation; agentic AI risks are concentrated in oversight tractability as system autonomy increases. Third, the EU AI Act Article 14 oversight architecture is more developed than its GCC counterparts, but GCC regulatory instruments include user awareness, transparency, and cultural appropriateness considerations that EU instruments under-address; cultural bias documented in large language models toward Western entities creates a trust calibration problem in Arabic-speaking user populations that has a limited counterpart in EU deployment contexts. Implications. Practitioners deploying AI systems across modalities should distinguish trust, calibration, and reliance in their human factors design and assessment. Multi-jurisdictional deployments in the GCC require interaction design that accommodates both EU AI Act oversight obligations and GCC-specific cultural, linguistic, and regulatory expectations. Empirical validation through practitioner vignette surveys is reserved for subsequent research in this slate. Future work will extend the analysis through comparative regulatory mapping (Paper 14) and the assessment of dual-use interaction risks (Paper 12).

---

## uid: `doi:10.2139/ssrn.6812678`

- title: Generating and Verifying Expert-Level Legal Reasoning: A Proof-of-Concept Study in Polish Criminal Law
- authors: Tadeusz Zbiegień, Kamil Mamak, Mikołaj Małecki, Michał Rachalski, Benjamin Shishko, Przemysław Pałka
- affiliations: not stated
- posted: 2026-06-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6812678
- keyword hits: agentic, chain-of-thought, claude, llm, llms, prompting

### abstract

LLMs are increasingly likely to be used in legal work, including criminal-law settings where unsupported reasoning may have serious consequences. Existing legal benchmarks and exam-style evaluations suggest that LLMs can perform well on some tasks, but do not adequately test expert-level, open-ended, jurisdiction-specific legal analysis. They also tell us little about whether such systems can reliably assess the quality of their own outputs in agentic workflows. To address these gaps, we designed an expert-authored Polish criminal-law vignette and a 54-item rubric and evaluated four LLMs together with a multi-agent pipeline. This paper presents the results of two experiments: case-solving performance and verifier performance. We find that chain-of-thought prompting substantially improves answer generation, with GPT CoT and Claude CoT achieving the strongest results, while the best multi-agent run is competitive but does not exceed the strongest CoT systems. By contrast, verifier performance lags behind generation: apart from GPT CoT and Claude CoT, most systems assess their own answers too leniently relative to expert judgment. We therefore argue that solving a legal case and reliably evaluating such a solution are distinct capabilities. This distinction matters for agentic legal systems, where a weak verifier may reinforce rather than correct erroneous output. Although preliminary and limited to a single vignette, this study shows the value of expert-authored, rubric-based evaluation for legal AI and highlights verifier reliability as an important bottleneck for agentic legal systems.

---

## uid: `doi:10.2139/ssrn.6890914`

- title: PC-RadNet: A Prompt-Calibrated, Parameter-Efficient Foundation Model for Comprehensive Multi-Task Segmentation, Clinical Assessment and Report Generation in Spine MRI
- authors: Rao  Farhat Masood, Imtiaz Ahmad Taj
- affiliations: not stated
- posted: 2026-06-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6890914
- keyword hits: foundation model, llm, llms, retrieval-augmented

### abstract

Lumbar spine MRI analysis requires concurrent anatomical segmentation, disc degeneration grading, disc height quantification, multi-label pathology detection and structured report generation. These tasks are traditionally addressed by separate resource-intensive models that impose spatial annotation requirements at inference. We propose PC-RadNet, a lightweight, prompt-calibrated multi-task framework that unifies these capabilities within a single architecture. Built upon a frozen DINOv2 backbone with 2.73 M trainable parameters, PC-RadNet introduces a Spine Domain Adapter for radiological feature adaptation, a Prompt Calibrator for multi-conditional feature gating and a multi-task head ensemble for simultaneous prediction of segmentation masks, Pfirrmann grades, disc heights and spinal disorders. A retrieval-augmented template filling (RATF) module generates structured radiology reports from PC-RadNet predictions compliant with RSNA guidelines. Trained on multi-planar lumbar Internal Dataset (LSMA-PQR), PC-RadNet achieves a mean Dice coefficient D=0.861 and mean IoU J=0.770 for prompted segmentation, 92.3% within-one-grade accuracy for Pfirrmann grading, disc height MAE of 0.57 mm and patient-level disorder macro-F1 of 0.57. The RATF report generator attains disorder-level F1 of 0.798, outperforming twelve benchmarked medical LLMs while maintaining a 0.63 GB VRAM footprint at inference. Zero-shot evaluation on SPIDER and RSNA 2024 confirms cross-institutional transfer of grading performance, with segmentation constrained by acquisition divergence. Code is available at (https://github.com/farhatmasood/pc-radnet).

---

## uid: `doi:10.2139/ssrn.6915109`

- title: SEAL: A Novel Methodology for Evaluating the Security of Agentic LLMs
- authors: Irene Gosálvez White, Pedro García-Teodoro, Roberto Magán Carrión
- affiliations: not stated
- posted: 2026-06-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6915109
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

The adoption of large language models (LLMs) as agentic systems introduces security risks that extend beyond traditional prompt-based interactions. This paper presents a novel framework intended to generate datasets for benchmarking the security of LLMs with tool-calling capabilities. Our methodology, termed SEAL, integrates automated red teaming through PyRIT for adversarial prompt generation and Promptfoo for structured evaluation under controlled inference-time settings, without requiring training-time modifications or external guardrails. The evaluation covers three adversarial strategies intended to measure confidentiality, integrity, and availability: direct tool injection, system prompt exfiltration, and indirect prompt injection with semantic denial-of-service (SDoS) effects. We further assess a semantic defense-in-depth strategy based on progressively hardened system prompts. Through extensive experimentation we demonstrate the validity and usefulness of SEAL for automated evaluation of the security level of agentic LLMs. The results obtained for the evaluated models, including both open-source and commercial systems, indicate that commercially aligned models and larger open-source architectures exhibit greater security stability across most assessed dimensions. However, a critical trade-off emerges between robustness and operational availability.

---

## uid: `doi:10.2139/ssrn.6910515`

- title: Mapping Urban Mixed Land Use via Multimodal Fusion and Large Language Models
- authors: Youcheng song, Chang Xia, Weilin Wang, Haijun Wang, Bin Zhang, Haoran Zeng, Yaotao Liang, Xiaoxu Cao
- affiliations: not stated
- posted: 2026-06-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6910515
- keyword hits: chain-of-thought, large language model, large language models, llm

### abstract

Accurate identification of mixed urban land use is critical for sustainable planning, yet traditional supervised methods are often constrained by the "semantic gap" and heavy reliance on labeled data. This study proposes an interpretable Geospatial AI (GeoAI) framework that integrates multimodal fusion with zero-shot Large Language Model (LLM) reasoning. Validated in Beijing and Changsha, the framework generates high-fidelity parcels from crowdsourced road networks and aligns spatial locations with textual Point of Interest (POI) embeddings via contrastive learning. These representations are synthesized with multispectral imagery, 3D morphology, and space syntax metrics. Following unsupervised clustering, a zero-shot Chain-of-Thought (CoT) inference mechanism assigns land-use semantics, providing explicit reasoning traces without requiring parcel-level training labels. Results demonstrate area-weighted overall accuracies of 70.91% and 76.90%, respectively, surpassing baseline benchmarks. By bridging unsupervised learning with LLM-driven semantic synthesis, this framework offers a transparent, scalable solution for mapping urban functional complexity and transit-oriented development patterns, moving beyond traditional deterministic single-label mapping.

---

## uid: `doi:10.2139/ssrn.6910158`

- title: EVALUATING GENERATIVE AI RELIABILITY FOR CLINICAL NOTE ABSTRACTION IN PEDIATRIC HEALTHCARE SETTINGS
- authors: VINOD RUFUS MOTANI
- affiliations: not stated
- posted: 2026-06-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6910158
- keyword hits: generative ai, generative artificial intelligence, large language model, large language models, prompt engineering

### abstract

Generative Artificial Intelligence has been altering the healthcare field in many ways. GenAI can be used to abstract clinical notes from EHRs. Analysis of EHR clinical notes refers to collecting insights from clinical notes for analyzing disease conditions. Particularly in Pediatric healthcare environments, this process takes up a lot of time and manual efforts. The long tail of variables and unique patients is why this is so. The suggested approach uses advanced large language models and connects them via prompt engineering to determine all the key patient’s information in the clinical notes, summarize and cluster them. Also, it preserves clinical accuracy and contextual relevance during the abstraction process. We compiled a set of clinical notes of a pediatric patient for quantitative experimentation. A healthcare practitioner's team used clinical notes to do abstractions. Furthermore, AI models were utilized to generate similar abstractions. The human abstract was analysed against each of the generated abstractions and performance was evaluated using respective metrics accuracy, precision, recall and F1-score, and reliability index in 5-fold cross-validation. The outcome proved generative AI detracts significantly from abstraction time.

---
