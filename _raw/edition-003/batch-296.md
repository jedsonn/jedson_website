# Classification batch 296 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-296.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6841449`

- title: Allocation of $USD 70 Billion on Global Respiratory Research Funding 2000-2023: Analysis of Dynamics of Funding and International Collaboration
- authors: Anbang Du, Rifat Atun, Beining Zhang, See PDF
- affiliations: not stated
- posted: 2026-05-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6841449
- keyword hits: large language model, large language models

### abstract

Background: Respiratory diseases accounted for three of the top five causes of deaths globally in 2021. Research is crucial to understanding disease determinants, effects of interventions, and to improving patient outcomes. We analysed global patterns and temporal trends for public and philanthropic investments, research collaborations and publications for respiratory research. Methods: We searched Digital Science Dimensions database for respiratory disease-related research funding awards between Jan 1, 2000, and Dec 31, 2023. We combined human expert input with a novel automated framework based on machine learning and large language models to categorise funding awards by respiratory disease type (e.g. acute infection, airways, lung cancer), priority research theme (e.g. vaccine, climate threats, antimicrobial resistance), and research phase (e.g. preclinical, phase 1-4 trials, public health). Funding amount was compared with the global burden of specific conditions, measured by disability-adjusted life-years using data from the Global Burden of Disease study. We analysed co-authorship networks of countries, showing the evolution of research collaboration over time. Findings: We identified 73,093 awards totaling $69.6bn in 2000 to 2023. Preclinical research received $51.9 bn (74.6% of total funding), phase 1-4 trials $5.7bn (8.3%) and public health $8.3bn (11.9%). The most funded respiratory disease type was acute infection ($32.1 bn, 46.1%), followed by airway diseases ($14.4bn, 20.7%), and lung cancer ($8.8bn, 12.6%). Analysis by priority theme revealed $17.3bn allocated to vaccination research (24.8%), with low levels of investment into research on climate threats ($1.1bn, 1.6%), antimicrobial resistance ($0.6bn, 0.8%) and pandemic preparedness ($0.4bn, 0.6%). By funding received per associated respiratory DALY, high-income countries received $61/DALY whereas low-income countries $0.016/DALY. Respiratory infection received more than $15/DALY while non-infection less than $10/DALY in 2019-2020, reversing the trend of prior two decades. Network analysis revealed that collaboration intensity peaks roughly three years after funding injections in the years of global respiratory events. The collaboration network of co-authorship is characterised by a rigid core of high-income countries and a flexible periphery of low- and middle-income countries through time. Interpretation: There is inequity between rich and poor countries in the current respiratory disease funding landscape. Rich countries have been consistently central to global research collaboration, with widening yet volatile involvement of poor countries over time. The current funding landscape is not obviously well prepared for current and future respiratory threats such as antimicrobial resistance, climate change and future pandemics. Long-term investment can build sustainable research networks with more equitable and efficient allocation of funds.

---

## uid: `doi:10.2139/ssrn.6793726`

- title: Mining Subscenario Refactoring Opportunities in Behaviour-Driven Software Test Suites: ML Classifiers and LLM-Judge Baselines
- authors: Ali Hassaan Mughal, Noor Fatima, Muhammad Bilal
- affiliations: not stated
- posted: 2026-05-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6793726
- keyword hits: large language model, llm

### abstract

Context. Behaviour-Driven Development (BDD) software test suites accumulate duplicated step subsequences. Three published refactoring patterns are available (within-file Background, within-repo reusable-scenario invocation, cross-organisational shared higher-level step), but no prior work automates which recurring subsequences are worth extracting or which mechanism applies. Objective. Rank recurring step subsequences ("slices") by refactoring suitability (extraction-worthy), pre-map each to one of the three patterns, and quantify prevalence across the public BDD ecosystem. Method. Every contiguous L-step window (L ∈ [2, 18]) in a 339-repository / 276-upstream-owner Gherkin corpus is keyed by paraphrase-robust cluster identifiers and counted under three scopes. Sentence-BERT (SBERT) / Uniform Manifold Approximation and Projection (UMAP) / Hierarchical Density-Based Clustering (HDBSCAN) recovers paraphrase-equivalent slices. Three authors label a stratified 200-slice pool against a written rubric. An eXtreme Gradient Boosting (XGBoost) extraction-worthy classifier trained under 5-fold crossvalidation is compared with a tuned rule baseline and two open-weight Large Language Model (LLM) judges. Results. The miner produces 5,382,249 slices collapsing to 692,020 recurring patterns. Three-author Fleiss' κ = 0.56 (extraction-worthy) and 0.79 (mechanism). The classifier reaches out-of-fold F1 = 0.891 (95 % CI [0.852, 0.927]), outperforming both the rule baseline (F1 = 0.836, p = 0.017) and the better LLM judge (F1 = 0.728, p < 10−4). 75.0 %, 59.5 %, and 11.7 % of scenarios carry a within-file Background, within-repo reusable-scenario, or cross-organisational shared-step candidate. Conclusion. Paraphrase-robust subscenario discovery yields a corpus-wide census of BDD refactoring opportunities; pipeline, classifier predictions, labelled pool, and rubric are released under Apache-2.0.

---

## uid: `doi:10.2139/ssrn.6848253`

- title: SCALA-NIDS: Safety-Constrained LLM-Advised Closed-Loop Adaptation for Online Open-World Network Intrusion Detection
- authors: Xiaojie Qin, Qingjun Yuan, Haopeng Fan, Jing Tao, Pinghui Wang, Jihong Teng, Siqi Lu, Yongjuan Wang
- affiliations: not stated
- posted: 2026-05-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6848253
- keyword hits: llm

### abstract

Network Intrusion Detection Systems (NIDS) in real-world environments face continuously evolving traffic streams caused by network reconfiguration, service migration, emerging attacks, and mixed distribution drift. Conventional closed-set and i.i.d.-based detectors often degrade under such online open-world conditions, while existing online adaptation methods usually lack coordinated drift perception, strategy decision-making, model updating, and safety validation. This paper proposes \textbf{Safety-Constrained LLM-Advised Adaptation for Network Intrusion Detection Systems (SCALA-NIDS)}, a closed-loop framework for online open-world NIDS. SCALA-NIDS follows a ``Detection--Response--Validation'' cycle by integrating runtime drift monitoring, constrained LLM-guided strategy reasoning, deterministic adaptation execution, and safety-gated validation. Given a structured Stats Snapshot, the LLM advisor selects only high-level adaptation intents, which are mapped to predefined update configurations to ensure controllability and safety. SCALA-NIDS further introduces a strategy-driven multi-level teacher--student adaptation controller that coordinates sample selection, objective weighting, and model updating with source-data retention, target-sample selection, domain alignment, and consistency regularization. A Safety & Fallback Gate rejects or revokes risky updates. Experiments on UNSW-NB15 and NSL-KDD under temporally ordered online evaluation show that SCALA-NIDS achieves the highest accuracy (95.93%) and F1-score (94.42%) on UNSW-NB15, the highest F1-score (91.93%) on NSL-KDD, and the best average accuracy (93.18%) and F1-score (93.18%) across both datasets. Ablation and LLM-backend studies further confirm the effectiveness and practicality of the proposed framework.

---

## uid: `doi:10.2139/ssrn.6845460`

- title: When Simpler Segmentation Wins: Geometric Fidelity and Energy Efficiency in Edge Plankton Biometry
- authors: David Sosa-Trejo, Antonio Bandera, Martín González, Santiago Hernández-León
- affiliations: not stated
- posted: 2026-05-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6845460
- keyword hits: foundation model

### abstract

Deploying advanced visual recognition on embedded hardware often requires a compromise between analytical precision and processing overhead. This letter explores this tension by benchmarking segmentation algorithms for high-fidelity marine biometry. We introduce IsPlanktonBIO, a dual-stage architecture designed to perform high-precision biometry by extracting organism dimensions and taxonomic identity directly on low-power devices. We compare a contemporary zero-shot transformer (Segment Anything Model 2) against a deterministic contour-based pipeline. Results from the DYB-PlanktonNet dataset expose a counterintuitive phenomenon: the deterministic approach exhibits superior spatial delineation. While foundation models demonstrate strong semantic grouping, their boundary-smoothing tendency truncates the fragile structural features required to accurately derive size. Consequently, the deterministic method achieves a higher correlation with standard sizing metrics (R2=0.70 vs. R2=0.51). Furthermore, migrating the framework to a Multi-Processor System-on-Chip (MPSoC) via 8-bit quantization reduced energy consumption to 0.362 J per inference, a level compatible with the constraints of battery-powered autonomous systems. However, this deployment revealed weaknesses under class imbalance: accuracy dropped by over 27% within rare morphotypes. These findings redefine how the oceanic carbon pump can be measured, by making continuous in situ biometry feasible on low-power edge platforms.

---

## uid: `doi:10.2139/ssrn.6793201`

- title: AI and Big Data Security, Governance, and Regulatory Compliance in Enterprise Cloud Platforms: A Regulatory Document Analysis for the Saudi Public Sector
- authors: Muhammad Omar Muftakhar
- affiliations: not stated
- posted: 2026-05-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6793201
- keyword hits: generative ai

### abstract

Saudi Arabia's digital transformation agenda has produced a regulatory environment that is comprehensive in its ambition but uneven in its operational specificity when applied to artificial intelligence and big data workloads. Public-sector enterprises in the Kingdom are deploying AI capabilities at scale, embedding machine learning into enterprise resource planning processes, integrating cloud-native data platforms with SAP and adjacent systems, and increasingly evaluating generative AI for content generation, summarization, and process automation. Each of these deployments operates within a regulatory perimeter defined by the Saudi Data and AI Authority, the National Cybersecurity Authority, and the Communications and Space Technology Commission, and each raises governance questions that the current instruments address at the level of principle but not at the level of operational implementation. This paper investigates how five governance domains central to enterprise AI and big data deployments, namely data lineage and classification, model lifecycle governance, integration trust and identity, observability and audit-readiness, and ethics operationalization, are addressed by the principal Saudi regulatory instruments: the National Strategy for Data and AI, the Personal Data Protection Law, the SDAIA AI Ethics Principles, the Cloud Computing Regulatory Framework, and the Essential and Cloud Cybersecurity Controls. The study uses a systematic document analysis methodology, cross-referencing the Saudi instruments against the NIST AI Risk Management Framework and against published technical guidance from SAP Business Technology Platform and Amazon Web Services. Across the five domains, the study finds that regulatory coverage is coherent at the policy level but leaves significant operational implementation gaps, particularly for model lifecycle governance, AI-derived data classification, and the integrated audit-readiness requirement that emerges from combining NCA logging obligations with SDAIA explicability principles. The study also examines generative AI compliance considerations, including prompt governance, hallucination risk, and cross-border model placement, finding that current instruments do not yet address these concerns with sufficient specificity for enterprise implementation. The findings contribute to an understanding of how regulated public-sector organizations can structure compliant AI and big data programmes while the regulatory framework continues to mature.

---

## uid: `doi:10.2139/ssrn.6849594`

- title: Synergistic Integration of Large Language Model and Machine Learning for Launch Vehicle Pricing Factor Analysis and Modeling
- authors: Beiyu Yi, Xin Zheng, Hui Min, Nannan Shi, Xiaodan Liu
- affiliations: not stated
- posted: 2026-05-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6849594
- keyword hits: large language model, llm

### abstract

This study presents a novel launch vehicle price - modeling framework that integrates LLM - augmented features with machine learning. LLM analysis expands the parameter set from 16 to 18, enhancing the model's ability to capture price - influencing factors. The methodology combines PLS regression and XGBoost - Optuna for hyperparameter optimization and ensemble modeling, facilitating analysis and model construction. Multiple model configurations were evaluated, and the optimal model performed outstandingly, with an R² of 0.9977, RMSE of 12.4, and MAE of 5.9851, outperforming traditional multivariate linear regression. The accuracy improvement is due to the LLM's ability to extract latent features from textual data, which, when integrated with structured parameters, enhances prediction accuracy. Further validation shows the framework's applicability in the aerospace industry. For instance, LLM - augmented features are correlated with key price determinants, consistent with industry trends. The model's precision supports strategic pricing, fills gaps in existing methods, and allows for dynamic adjustments for evolving technologies.

---

## uid: `doi:10.2139/ssrn.6847023`

- title: Machines That Reason, Institutions That Judge: Artificial Intelligence and the Nature of Judgment
- authors: Haim V. Levy
- affiliations: not stated
- posted: 2026-05-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6847023
- keyword hits: large language model, large language models

### abstract

This Article develops a jurisprudential account of judgment in light of artificial intelligence systems capable of simulating legal reasoning. Large language models can generate outputs that replicate the structure of adjudicative justification, including rule articulation, fact application, and reasoned conclusions. This capacity raises a foundational question: if the form of judicial reasoning can be reproduced without human deliberation, what constitutes judgment as a legal and institutional act? Drawing on a structured analysis of model-generated opinions across federal cases, the Article shows that justificatory form can be simulated with considerable fidelity. It argues, however, that judgment is not reducible to doctrinal accuracy or argumentative coherence. Rather, judgment is an institutional practice grounded in authority, accountability, and the public attribution of responsibility. The central implication is that while machines may generate reasons, judgment-understood as an act of legal authority-remains irreducibly institutional.

---

## uid: `doi:10.2139/ssrn.6847484`

- title: The Cyber Risk of Non-Financial Firms
- authors: Francesco Columba, Manuel Cugliari, Marco Orlandi, Federica Vassalli
- affiliations: not stated
- posted: 2026-05-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6847484
- keyword hits: large language model

### abstract

This work proposes an indicator of cyber risk vulnerability for Italian non-financial firms, applying natural language processing and a large language model to data extracted from financial statements, news reports, and cyber industry reports. The indicator is based on a taxonomy tailored to Italy, addressing dimensions of cyber risk that so far have not been considered within a unified methodological framework. The new taxonomy captures, for a large and heterogeneous sample of f irms, the occurrence of cyberattacks, the degree of firms’ regulatory compliance and the utilization of cyber defence technologies and security certifications. The aptness of including cyber risk in credit risk models is suggested by the data on cyberattacks in Italy, which have been on the rise since 2019. The negative impact of cyber incidents on firms’ vulnerability in the aftermath of an attack outweighs the mitigating effects of defensive actions, which require some time to have an impact. Also, firms tend to increase the amount of information on cyber risk in official reporting only after suffering an attack. Overall, the findings indicate that cyber risk may have material effects on business continuity and, hence, it has to be incorporated into credit risk assessments.

---
