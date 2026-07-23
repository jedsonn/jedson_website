# Classification batch 176 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-176.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7048020`

- title: Domain-Constrained Abstraction Learning for Interpretable Clinical Risk Prediction
- authors: Seyed  Hossein Parizad, Sona Taheri, Sattar Seifollahi, Malihe Akhavan-Abdollahian
- affiliations: not stated
- posted: 2026-07-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7048020
- keyword hits: large language model, llm

### abstract

Predicting clinical risk from electronic health records (EHRs) is expected to enable personalised medicine and improve healthcare quality. However, relevant information in the EHRs is distributed across heterogeneous modalities, including laboratory measurements, clinical notes, medication orders, coded diagnoses, and social indicators. Many existing models pool all inputs into a single feature space and learn end-to-end. These approaches often achieve strong predictive performance, but they reinforce the common belief that improving model interpretability must reduce accuracy, a perceived transparency tax. This belief leads practitioners to choose black-box models, even in clinical settings where understanding the model's reasoning is essential. In this paper, we propose Domain-Constrained Abstraction Learning (DCAL), a modular prediction framework that routes clinically related inputs to dedicated specialist models. For each domain, constraints and feature definitions are derived through large language model (LLM)-guided clinical knowledge extraction. A meta-learner then integrates the resulting structured domain-level summaries to generate the final prediction. This framework produces an explicitly defined, fully inspectable prediction pathway, without relying on post-hoc explanation methods.We instantiate DCAL framework as an Interpretable Multi-Specialist Ensemble (IMSE) and evaluate it on all-cause unplanned 30-day readmission using 268,328 hospital admissions from MIMIC-IV. IMSE achieves an area under the receiver operating characteristic curve (AUC) of 0.73 on the temporal test set, with statistically significant improvements over both a monolithic multilayer perceptron (MLP; ΔAUC = +0.003, p = 0.037) and a monolithic gradient-boosted machine (GBM; ΔAUC = +0.003, p = 0.042). The specialists learn distinct internal representations (pairwise centred kernel alignment, CKA ≈ 0), and targeted input corruption reveals a clinically plausible hierarchy of domains (history ≫ pharmacy > laboratory). The resulting domain-specific summary features, such as severity tiers, organ dysfunction scores, and medication burden classes, depend on clinically coherent groupings that cannot be obtained through arbitrary feature decomposition. These results demonstrate that structuring intermediate representations by clinical domains preserves strong predictive performance while making model reasoning transparent and auditable at each stage of the pipeline. More broadly, findings suggest that correct clinical abstraction is the primary design objective, with competitive accuracy and transparency both emerging as consequences of that structure rather than as competing design goals.

---

## uid: `arxiv:2607.04439v1`

- title: ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes
- authors: Qihao Zhao, Yangyu Huang, Yalun Dai, Lingao Xiao, Jianjun Gao, Xin Zhang, Wenshan Wu, Scarlett Li
- affiliations: not stated
- posted: 2026-07-05
- source: arXiv
- link: https://arxiv.org/abs/2607.04439v1
- keyword hits: large language model, large language models

### abstract

Large language models have made research ideation increasingly accessible, yet effective idea development requires more than generating candidate directions. Researchers must ground a problem in current literature, identify meaningful bottlenecks, differentiate from existing solutions, and evaluate risks before committing to implementation. We present ResearchStudio-Idea as a reusable skill suite for this first mile of research ideation. The suite includes Paper-Search, a standalone multi-source literature search skill; Scoop-Check, a standalone prior-art collision checker for novelty claims; and IdeaSpark, the end-to-end skill that composes evidence grounding, pattern-guided generation, collision retrieval, audit, and idea-card rendering into one workflow. IdeaSpark is constructed from a corpus of 1,947 machine learning conference papers collected from ICLR, ICML, and NeurIPS between 2021 and 2025, including Oral papers, a separately tracked high-citation subset, and rejected submissions. Analysis of these outcomes reveals 31 recurring ideation sub-patterns, consolidated into 15 reusable ideation patterns. Each pattern is operationalized as a structured card containing research contexts, bottleneck types, differentiation strategies, supporting precedents, and common failure modes. Given a research problem and an evidence bundle, IdeaSpark evaluates evidence readiness, reconstructs the surrounding research context, identifies unresolved bottlenecks, selects relevant patterns, instantiates one candidate direction, retrieves potentially conflicting prior work, and performs outcome-informed auditing. This workflow transforms reusable ideation patterns into traceable research proposals. Blind automated-judge evaluations show that IdeaSpark consistently produces stronger research proposals than no-skill and generic-skill baselines while maintaining competitive novelty.

---

## uid: `arxiv:2607.04261v2`

- title: Shortcut Learning in Legal Judgment Prediction: Empirical Evidence from the UK Employment Tribunal
- authors: Joe Watson, Joana Ribeiro de Faria, Marcus Tomalin, Måns Magnusson, Huiyuan Xie, Hao Tian Yeung, Christine Carter, Jonathan Rutherford
- affiliations: not stated
- posted: 2026-07-05
- source: arXiv
- link: https://arxiv.org/abs/2607.04261v2
- keyword hits: llm, llms

### abstract

Current Legal Judgment Prediction (LJP) is constrained by its reliance on post-hoc judicial materials, increasing the likelihood that models perform retrospective classification rather than true forecasting. This paper empirically investigates shortcut learning in this context by studying claim-level outcome prediction in UK Employment Tribunal (UKET) decisions. Using a corpus of 33,158 individual claims, we predict outcomes from claim texts and LLM-extracted case summaries, evaluating models ranging from interpretable TF-IDF-based classifiers to black-box LLMs. While headline predictive performance figures appear strong, we demonstrate that such performance in LJP systems trained on post-hoc judicial text can be driven by the retrospective nature of the source material. Stratifying the test data by human judgments of leakage reveals that performance increases where outcome-revealing cues are embedded in the narrative. Moreover, a model trained on just the 4% of features identified as leakage achieves high performance, outperforming human experts. These findings substantiate concerns that LJP performance may be exaggerated by linguistic artefacts. Yet this vulnerability is not fatal to the research agenda. Instead, post-hoc judgments might be treated as potentially contaminated texts, requiring active auditing. Retraining models after masking leakage features results in only a negligible reduction in Macro-F1. Hence, while models will opportunistically exploit shortcuts when available, they remain capable of extracting useful predictive signals when these artefacts are removed.

---

## uid: `doi:10.2139/ssrn.7067713`

- title: MLCWStudio: a web application for Multi-LLM Consensus Weighting of social capital outreach indicators for blockchain-enabled microfinance
- authors: Nur Aima Shafie, zahari Md Rodzi, zuraidah sanusi, Aziatul Waznah Ghazali, mariyam niyaf mohamed
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7067713
- keyword hits: large language model, large language models

### abstract

Composite indicators reduce many criteria to a single comparable score, and their most consequential design choice is how the criteria are weighted. Subjec tive methods are meaning-aware but costly and hard to reproduce; objective methods are reproducible but meaning-blind. MLCW Studio is an open source, browser-based application that operationalises Multi-LLM Consensus Weighting (MLCW), a procedure that reconciles semantic importance weights elicited from a panel of large language models with objective entropy weights through a single fusion parameter, and quantifies inter-assessor agreement. Through an upload-first, no-code interface, analysts load indicator data (Excel or CSV), derive objective and semantic weights, fuse them, and rank units with 95% bootstrap confidence intervals, sensitivity analysis, four alternative weighting methods, and agreement diagnostics. Results export as multi-sheet Excel and interactive HTML reports, and, with user-supplied keys, a gen uine multi-vendor elicitation can be run live. By making a reproducible and meaning-aware weighting method usable by non-programmers, the software broadens access to defensible composite indicators across economics, finance, and policy research. The application is deployed on Streamlit Community Cloud and released on GitHub under a permissive licence.

---

## uid: `doi:10.2139/ssrn.7014818`

- title: From AI Literacy to AI Fluency: A Developmental Framework for Higher Education
- authors: Aeron Zentner
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7014818
- keyword hits: generative ai, generative artificial intelligence

### abstract

Generative artificial intelligence has moved rapidly into teaching, learning, research, and administrative work, yet the dominant institutional response has centered on AI literacy alone. This conceptual article argues that AI literacy, defined as understanding basic concepts, recognizing tools, performing basic tasks, and identifying broad risks such as bias, hallucination, privacy harm, and misinformation, is necessary but insufficient for higher education in the generative era. The article advances a developmental AI Fluency framework that extends literacy toward strategic, critical, ethical, and contextual use of artificial intelligence while preserving human judgment, authorship, accountability, and disciplinary standards. The framework specifies six developmental levels, from AI Exposure and AI Awareness through Functional and Critical AI Literacy and on to Disciplinary AI Fluency, Generative AI Fluency, and Responsible AI Leadership, with the lower tiers forming a literacy band and the higher tiers forming a fluency band. It pairs these levels with six competency domains spanning conceptual understanding, operational skill, epistemic verification, ethical and legal judgment, metacognitive and human agency, and disciplinary transfer. A central claim is that fluency is a socio-technical capacity rather than an individual skill alone, depending on curriculum design, assessment redesign, faculty development, equitable access, policy, data governance, and human-centered principles. The article concludes that institutions should treat AI fluency as a core learning outcome and offers implications for practice and a research agenda.

---

## uid: `doi:10.2139/ssrn.7068291`

- title: Evidence-conditioned Weak-answerer Diagnosis for Traceable Quality Control of Educational Quizzes Generated by Artificial Intelligence
- authors: bo han
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7068291
- keyword hits: large language model, large language models, qwen

### abstract

Engineering deployment of artificial intelligence systems based on large language models requires quality-control mechanisms that are traceable, cost-aware and robust to noisy source material. Quiz items generated from open educational videos may be answerable from general knowledge, recoverable only when lecture evidence is shown, or defective even with the source provided. The artificial intelligence contribution of this paper is an evidence-conditioned weak-answerer diagnosis for traceable quality control of generated educational quizzes. The key signal is paired blind/source answering by the same small model: an item answered incorrectly without context but correctly with its own source segment is treated as a difficult source-grounded item, whereas an item that remains wrong with the source is routed to revision. The engineering application is a video-to-quiz quality-control pipeline that recommends whether an item should be kept, kept with source evidence, or repaired. On a 1,997-item Open163 benchmark, this diagnosis separates items into source-unneeded, source-recovered and evidence-failed groups, sending only 30.05% of items to a strong reviser while preserving the 437 source-recovered items as valid difficult questions. Targeted revision with Qwen2.5-32B, a 32-billion-parameter model, improves weak-answerer accuracy by 13.22 percentage points in the blind setting and 10.78 points with source context, with paired McNemar tests significant at p

---

## uid: `doi:10.2139/ssrn.7067669`

- title: Moral Advice as Interactional Negotiation: How Framing, Conversational Pushback, and Social Position Shape LLM Sycophancy in Eldercare Dilemmas
- authors: Minne Chen, Yourong Yao
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7067669
- keyword hits: llm, llms

### abstract

As users increasingly turn to conversational AI for guidance on morally contested personal decisions, understanding how these systems generate moral judgments has become an important question for human-AI interaction research. We argue that in morally contested domains, the guidance users receive reflects neither a fixed ethical framework nor a uniform sycophantic tendency, but an interactional negotiation whose direction and degree are jointly moderated by question framing, sustained user pressure, and the social position of the moral subject. Using a factorial vignette experiment with a standardized three-round conversational protocol, we presented LLMs with eldercare dilemmas that varied in framing and persona, followed by escalating user disagreements. Across 1,620 conversations, we found consistent asymmetries in both baseline evaluations and conversational accommodation. Caregiving affirmation elicited near-uniform endorsement, while non-caregiving framing produced more variable baseline stances. Accommodation was rapid when users challenged caregiving endorsement (90.1% shifted after one round of pushback) but slower and less universal for non-caregiving disapproval (53.3% early accommodation). Persona cues shaped these patterns. Female personas received more sympathetic evaluations of non-caregiving decisions, while the presence of sisters increased accommodation. These findings suggest that AI moral advice is less a fixed ethical framework than a partially stable negotiation between embedded norms and user pressure, shaped by dilemma framing and personas’ social position. Functioning as a black box while experienced as objective, this process carries social and ethical, not merely technical, implications.

---

## uid: `doi:10.2139/ssrn.7067272`

- title: A Survey on Multi-Robot Collaboration and Communication: Taxonomy, Challenges, and Future Directions
- authors: Owais Ahmed, Adeel Khalid, Daniel Byers, M.  Hassan Tanveer
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7067272
- keyword hits: large language model, llm

### abstract

Multi-robot collaboration and communication enable teams of autonomous agents to collectively sense, plan, and act in applications spanning search and rescue, precision agriculture, warehouse logistics, and disaster response. Despite significant algorithmic progress, coordinating large heterogeneous robot teams in bandwidth-constrained, dynamic environments remains challenging. This survey consolidates state-of-the-art advances across communication architectures, task allocation strategies, perception frameworks, and learning paradigms. We present a comprehensive taxonomy organized into three primary dimensions: task allocation and coordination (including Large Language Model (LLM)-based planning and human-in-the-loop interfaces), communication and mapping frameworks (encompassing distributed Simultaneous Localization and Mapping (SLAM), opportunistic protocols, and collaborative perception), and learning and control methods (spanning multi-modal deep reinforcement learning and distributed optimization). Particular emphasis is placed on emerging paradigms including spectral prioritization for bandwidth-efficient SLAM, opportunistic communication for intermittent connectivity, semantic and mechanical interaction, protocol adaptability for agricultural and warehouse applications, and reinforcement learning for dynamic task allocation with infeasible task handling. Our comparative analysis evaluates scalability, communication efficiency, interpretability, and real-world validation across representative frameworks. We identify critical open challenges and outline future research directions toward scalable, interpretable, and trustworthy multi-robot systems deployable in real-world environments.

---
