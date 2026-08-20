# Classification batch 18 of 22, edition 21

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-021/batch-18.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7289632`

- title: Adaptive Weather-Aware Home Energy Management through Large Language Model-Based Appliance Scheduling
- authors: sokipriala jonah, Queen Moses, Abiola Babatunde, Michael Ajao-Olarinoye, Daniel Bammeke
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7289632
- keyword hits: large language model, llm

### abstract

Residential flexibility can reduce electricity costs, increase local photovoltaic (PV) utilisation, and support demand-side operation, but conventional Home Energy Management Systems often require users to translate everyday preferences into technical constraints. This paper presents an adaptive, weather-aware energy-management agent that converts natural-language requirements into coordinated schedules for multiple flexible household loads. To our knowledge, it is the first autonomous LLM-based HEMS to jointly optimise appliance schedules using dynamic retail prices, weather-derived PV forecasts, household demand, self-consumption, export revenue, calendar deadlines, and household power limits within a unified net-cost objective.Five language-model controllers are evaluated against an extended mixed-integer linear programming oracle across tariff-volatility and weather regimes, forecast uncertainty, constraint conflicts, and a seven-day rolling deployment. Results show reliable multi-appliance coordination and near-optimal operating cost under dynamic tariffs. Constraint-conflict testing reveals model-specific failures under deadlines, power caps, irregular schedules, and infeasible requests, demonstrating that economic performance alone is insufficient for evaluating autonomous energy controllers.Weather-aware scheduling provides regime-dependent cost and PV self-consumption benefits by coordinating flexible demand with forecast generation. Across the seven-day evaluation, the agents capture 96.7–98.0% of the savings available between an off-peak timer and the optimisation oracle, while outperforming immediate-start and greedy policies. The findings demonstrate the potential of LLM-based residential energy control while highlighting the need for an independent deterministic feasibility layer before physical actuation.

---

## uid: `doi:10.2139/ssrn.7291663`

- title: Combining Case-Based Reasoning and Open AI Language Models for Experience-Driven Artificial Intelligence
- authors: Thacha Lawanna
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7291663
- keyword hits: large language model, large language models, llm

### abstract

Integrating Case-Based Reasoning (CBR) with large language models provides a promising foundation for artificial intelligence systems capable of learning from and adapting previous problem-solving experiences. This study proposes an experience-driven CBR–OpenAI framework combining the Retrieve–Reuse–Revise–Retain cycle with semantic understanding and generative reasoning. Publicly available CaseHOLD and CUAD datasets were adopted to support evaluation using realistic cases. The framework retrieves relevant historical experiences, adapts previous solutions to new contexts, evaluates generated responses, and retains validated outcomes for future reasoning. Performance was assessed through retrieval accuracy, solution accuracy, contextual relevance, solution adaptability, explainability, experience reuse effectiveness, and response consistency. The proposed framework demonstrated consistently strong results, achieving 94.5% retrieval accuracy, 95.1% solution accuracy, 96.0% contextual relevance, 96.4% solution adaptability, 96.2% explainability, 95.7% experience reuse effectiveness, and a best value of 96.6% for response consistency, with an overall effectiveness of 95.8%. Comparative and ablation analyses further demonstrated the complementary contributions of case retrieval, LLM-supported adaptation, revision, and experience retention. These findings indicate that combining explicit experiential memory with language-model reasoning can provide a balanced foundation for adaptive, explainable, context-aware, and continuously evolving artificial intelligence systems.

---

## uid: `arxiv:2608.15424v1`

- title: ETHOS: Towards a Modular Ethics Framework for Clinical Multi-Agent Systems
- authors: Rakesh Sharma, Sydney Pugh, Cameron Beeche, Pankhuri Singhal, Rachel Wu, Margaret Eby, Jeffrey Duda, James Gee
- affiliations: not stated
- posted: 2026-08-15
- source: arXiv
- link: https://arxiv.org/abs/2608.15424v1
- keyword hits: large language model, large language models

### abstract

The rapid adoption of large language models has enabled the development of clinical multi-agent systems (MAS) capable of integrating multimodal patient data and supporting increasingly complex clinical decision-making. However, the deployment of these systems in real-world healthcare settings raises critical ethical concerns related to safety, fairness, accountability, transparency, and patient trust. While numerous organizations, including the World Health Organization, the National Academy of Medicine, and the FUTURE-AI consortium, have proposed ethical frameworks and governance principles for healthcare AI, these efforts remain largely conceptual. To address this challenge, we present ETHOS (Ethics and Trust through Hierarchical Oversight System), a modular ethics framework designed as a governance meta-agent that can be integrated with any existing multi-agent system without requiring changes to its underlying architecture. ETHOS translates stakeholder-informed ethical requirements into executable runtime oversight through a layered governance approach consisting of deterministic checks, contextual reviews, and a final ethics critic. These components continuously evaluate intermediate reasoning steps and final outputs, enabling the system to identify ethical risks, request revisions, or suppress responses that fail predefined safety and trustworthiness criteria. We demonstrate ETHOS within a hepatology clinical decision-support MAS. Results show that ETHOS improves decision reliability by detecting incomplete, inconsistent, or out-of-scope evidence and appropriately increasing abstention when safe recommendations cannot be supported. By embedding ethical governance directly into system operation, ETHOS provides a practical and auditable mechanism for transforming high-level AI ethics principles into deployable safeguards.

---

## uid: `arxiv:2608.15223v1`

- title: TRACE-BN: Transferring Bangla-English Tutoring Behavior to a Sub-1B Offline Language Model
- authors: Khan Raiyan Ibne Reza, Sanjana Aktar Maria, Mohammad Tushar Abdullah, Asfee Bhuiyan Leen, Sumaiya Tabassum Nimi
- affiliations: not stated
- posted: 2026-08-15
- source: arXiv
- link: https://arxiv.org/abs/2608.15223v1
- keyword hits: gemini, qwen

### abstract

Bangla-English tutoring requires more than producing a correct translation: learners also need explanations of grammar differences, awareness of their likely errors, and targeted practice. We present TRACE-BN, a curriculum-guided dataset of structured tutoring traces for Bangla-speaking learners of English at the CEFR A1-A2 level. Each trace combines word-level glosses, literal and natural translations, Bangla grammar explanations, a plausible learner error, and a targeted practice question with its answer. The traces are generated by Gemini 3.5 Flash Lite as the teacher model from NCTB Classes 9-10 English curriculum units, then filtered for structural validity, script integrity, and semantic duplication. We transfer the resulting structured tutoring behavior to Qwen3-0.6B using LoRA with 4-bit quantization for resource-constrained offline deployment. On held-out inputs, schema validity increases from 85.4% to 95.8%, while, against teacher-model references, chrF++ improves from 15.28 to 34.77 and BLEU from 4.52 to 21.03. Field-level evaluation by two independent judges shows improvements across translation, grammar explanation, learner-error diagnosis, and practice alignment, while a human audit supports the quality of the supervision data. The results show that curriculum-guided structured supervision can transfer multi-component tutoring behavior to a sub-1B model under these resource constraints. The dataset, model checkpoints, and code are publicly available at https://huggingface.co/datasets/RaiyanKhaan/Trace-BN

---

## uid: `arxiv:2608.15193v1`

- title: Valhalla: A Layered Knowledge-State and Service-Governance Framework for Long-Term Scientific Knowledge Work
- authors: Yuyang Zheng, Nan Li, Wenxia Deng, Lige Yan, Xiang Li, Si Chen
- affiliations: not stated
- posted: 2026-08-15
- source: arXiv
- link: https://arxiv.org/abs/2608.15193v1
- keyword hits: large language model, llm

### abstract

As large language model (LLM) agents are increasingly adopted in scientific research, external knowledge bases, knowledge graphs, and long-term memory have improved information retrieval and task continuity. However, most structured knowledge systems remain node-centric, representing files, concepts, results, and judgments as nodes and relations in a graph. While suitable for personal knowledge management, such structures often depend on individual organizational practices, limiting knowledge sharing, integration, and reorganization across users. This paper presents Valhalla, a layered knowledge-state and service-governance framework for long-term scientific knowledge work. Valhalla replaces flat graphs with layered encapsulation and stable semantic boundaries through a five-layer File-Resource-Entity-Relationship-Graph (FREG) model. File and Resource preserve source identity and provenance, Entity represents knowledge objects, Relationship captures semantic judgments, and Graph provides task-oriented knowledge views, enabling knowledge states from different researchers to be exchanged and reorganized under a unified structure. We further introduce a Router-Contract-Workflow service-governance architecture, inspired by the microkernel paradigm, to constrain how language models access, modify, and extend knowledge states while maintaining structural consistency and auditable operational boundaries. We implement a Valhalla prototype and validate knowledge ingestion, cross-member integration, and scientific writing support through an antibody-design review task comprising 26 paper resources, 80 knowledge entities, and 92 semantic relations. Rather than proposing a new knowledge-extraction algorithm, Valhalla offers a paradigm for organizing collaborative scientific knowledge, transforming individualized knowledge structures into transferable and reorganizable shared knowledge states.

---

## uid: `doi:10.2139/ssrn.7292390`

- title: Nuclear fusion for AI: A pathway to power data centers sustainably
- authors: Layla Araiinejad, Vineet Jagadeesan Nair
- affiliations: not stated
- posted: 2026-08-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7292390
- keyword hits: large language model, large language models

### abstract

This perspective examines whether nuclear fusion can provide a scalable, low-carbonpower source for rapidly growing AI-driven data center demand. As large language models,cloud computing, and cryptocurrency mining accelerate electricity consumption growth,data centers are projected to account for a substantially larger share of U.S. and globalelectricity use in the coming decades, creating significant pressure on grid reliability anddecarbonization goals. We evaluate the technical and economic alignment between datacenter load profiles and nuclear power, particularly fusion, through a comparative analysisof capacity factors, levelized cost of electricity, grid interconnection constraints, anddeployment pathways. Unlike intermittent renewables, nuclear fission and fusion offerhigh-capacity-factor, firm baseload generation suited to AI training and inference workloadsthat require continuous, reliable power. Preliminary techno-economic analysis suggeststhat several Nth-of-a-kind fusion concepts, particularly magnetic confinement systems, maybecome cost-competitive with firmed renewable systems and advanced fission forhyperscale data center applications. Co-location of fusion plants with data centers furtherreduces transmission bottlenecks, improves resilience, and aligns with emerginghyperscaler procurement strategies. We also assess recent regulatory developments andargue that fusion’s favorable safety profile and reduced waste burden improve its long-termsocial and political viability relative to fission. We conclude that fusion represents astrategically important pathway for sustainably powering next-generation computinginfrastructure and should be prioritized in both policy and industrial deployment planning.Nuclear fusion for AI: A pathway topower data centers sustainably

---

## uid: `doi:10.2139/ssrn.7294155`

- title: Governing General-Purpose AI in Society: Layered Data-Protection Synergies Between the EU AI Act, the GDPR, and Germany's Federal Data Protection Act
- authors: Jui  Jen Peng, I-Chun Chen
- affiliations: not stated
- posted: 2026-08-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7294155
- keyword hits: chatgpt, foundation model

### abstract

General-purpose AI (GPAI) and the foundation models underpinning systems such as ChatGPT are reshaping how societies deliver public services and allocate informational power, yet are trained on vast web-scraped corpora that ingest personal and special-category data, generating risks of re-identification, inversion, and memorisation. This article examines how three European instruments jointly govern the societal deployment of GPAI: the General Data Protection Regulation (GDPR), Germany's Federal Data Protection Act (BDSG), and the Artificial Intelligence Act (AI Act), whose general-purpose AI regime introduces provider obligations for technical documentation, training-data transparency, and systemic-risk management. Using a mixed-methods design that integrates doctrinal legal analysis, comparative policy examination, reflexive thematic analysis of six elite expert interviews in Berlin and Munich, and documentary enforcement statistics from the Federal Commissioner for Data Protection (BfDI), the European Data Protection Board (EDPB), and the CMS GDPR Enforcement Tracker, the study reconstructs a three-layered governance model in which the GDPR establishes foundational data rights, the BDSG supplies national proportionality and enforcement adaptations, and the AI Act extends risk-tiered obligations across the AI life cycle. Three themes structure the findings: regulatory frameworks and obligations, data-protection challenges and safeguards, and enforcement and capacity. The analysis surfaces lawful-basis adaptations for indirect data collection, differential privacy and data minimisation as technical baselines against pipeline opacity, and a documented reliance on complaint-driven enforcement that constrains proactive oversight. Contrasting the EU-German configuration with the U.S. approach, the article advances five policy recommendations and positions layered regulation as a transferable societal governance model for general-purpose AI.

---

## uid: `arxiv:2608.15746v1`

- title: Propaganda Forensics: Recovering the Generation Pipeline of an AI-Driven Influence Campaign
- authors: Benjamin Icard, Elouan Vuichard, Louis Lefebvre, Lila Sainero, Thomas Girault, Alice Breton, Tanguy Launay, Gauvain Bourgne
- affiliations: not stated
- posted: 2026-08-16
- source: arXiv
- link: https://arxiv.org/abs/2608.15746v1
- keyword hits: llama, mistral

### abstract

We present a forensic analysis of the generation pipeline behind a recent AI-driven influence campaign. We introduce PROPAGIA, a corpus of 2,646 propagandist French articles from the Storm-1516/CopyCop campaign disclosed by VIGINUM and INSIKT GROUP in 2025. For comparison, we rely on SIPA, a corpus of human-written French mainstream press from the same period. Using topic modeling, vagueness and sentiment analysis, we first isolate persuasion techniques characteristic of propaganda, with PROPAGIA far exceeding SIPA in vagueness, subjectivity and negativity, and citing fewer sources. We then find prompt instruction leaks on 50 of the 84 PROPAGIA websites, including a verbatim ten-point editorial specification accounting for several of these differences, together with high cross-article redundancy. Finally, we show that rewriting-based detection supports INSIKT GROUP's attribution to the Llama 3 family, but also suggests the involvement of Mistral-family models.

---
