# Classification batch 322 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-322.answer.json` as a JSON array.

---

## uid: `arxiv:2606.28002v1`

- title: Dialogue to Detection: A Multimodal Hybrid NLP Pipeline for Insurance Fraud Detection
- authors: Muhammad Shakeel Akram, Amal Htait, Abdul Hamid Sadka, Emma Meisingseth, Karishma Jaitly
- affiliations: not stated
- posted: 2026-06-26
- source: arXiv
- link: https://arxiv.org/abs/2606.28002v1
- keyword hits: llm

### abstract

Insurance fraud imposes substantial financial losses and operational inefficiencies, raising premiums and impacting trust among legitimate policyholders. Early detection at FNOL remains a persistent challenge. Existing approaches rely largely on private, text-only datasets, limiting progress on multimodal methods that integrate linguistic, behavioural, and speaker-based indicators. We introduce a synthetic multimodal framework that replicates FNOL conditions. It generates agent-customer dialogue transcripts and two-speaker audios, performs ASR and diarisation. Downstream modules combine NER, regex-based feature extraction, LLM-RAG retrieval, and speaker embeddings in a rule-based risk score to flag narrative reuse, structural inconsistencies, and cross-case voice repetition while balancing sensitivity and false positives. Dataset validation and component-level evaluations show stability and transfer potential, offering a reproducible baseline beyond text-only fraud detection.

---

## uid: `doi:10.2139/ssrn.7002721`

- title: STACRE: Towards Automatic Android App Crash Reproduction from Stack Traces via Static Analysis and LLM
- authors: Zhenyu Dai, Jianwei Chen, Yihan Ouyang, Hongyan Zhang, Yuexin Zhang, Liwei Lin
- affiliations: not stated
- posted: 2026-06-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7002721
- keyword hits: llm, llms

### abstract

Context: Crash reproduction plays a crucial role in the continuous improvement of software application quality and the enhancement of stability. Most existing studies on Android application crash reproduction focus on analyzing the steps to reproduction extracted from the text descriptions in Android application crash reports. There is a severe lack of automated reproduction approaches for crash reports that only contain stack traces, and implementing such automation remains highly challenging.Objectives: To address the difficulty in automated crash reproduction for crash reports containing only stack traces, we propose STACRE, an automated crash reproduction approach for Android apps toward stack traces and integrates static analysis with LLMs.Methods: STACRE consists of two phases: static analysis and dynamic exploration. In the static analysis phase, it extracts crash-related information from the application and stack traces and constructs a PTMCG static model that correlates GUI pages with Java methods via reverse engineering, so as to improve the utilization efficiency of stack trace information. In the dynamic exploration phase, it leverages LLM to simulate manual reproduction thinking and predict user interactions. Combined with the SARSA reinforcement learning algorithm adapted for Android scenarios, it avoids local optima and collaboratively predicts operations that trigger crashes. Meanwhile, STACRE dynamically updates the PTMCG model to continuously optimize the performance of reinforcement learning and enhance the capability of crash prediction.Results: Experimental results on 45 real-world crash reports show that STACRE achieves a crash reproduction success rate of 68.89% with an average reproduction time of 1413 seconds, outperforming other state-of-the-art tools by a notable margin.Conclusion: STACRE effectively resolves the difficulty of automated reproduction for Android crash reports that contain only stack trace information and markedly improves the success rate and efficiency of crash reproduction.

---

## uid: `doi:10.2139/ssrn.7008301`

- title: Prototype-Guided Visual Recalibration for LLM-based Medical Report Generation
- authors: Li Li, Yuhong Shi, Kang An, Xiangbo Zhu, Xiao Yun, Jianyi Liu
- affiliations: not stated
- posted: 2026-06-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7008301
- keyword hits: llm, llms

### abstract

Conventional encoder-decoder models have achieved remarkable progress in medical report generation, providing a solid foundation for automated diagnosis. Recently, LLMs have achieved outstanding performance in general scenarios. However, how to effectively apply the generative capabilities learned by LLMs from massive general domain data to the medical field remains a highly challenging task. If only a shallow linear mapping is used, the LLM often receives blurry visual tokens. This ambiguity makes it difficult for generative models to effectively base their outputs on visual evidence, leading to excessive reliance on linguistic priors and generating generic or erroneous reports. To address this issue, we propose a prototype guided medical report generation framework aimed at recalibrating visual representations using an internal semantic prototype library. Specifically, the framework designs a geometric prototype constraint module that enforces strict geometric alignment between visual embeddings and disease text semantics in the metric space. In addition, we have added a prototype guided reconstruction module to reconstruct visual representations in a space centered around the prototype. By transforming ambiguous visual features into discriminative tokens via prototypes, our method significantly enhances the LLM's comprehension of image content. Extensive experiments on benchmark datasets have shown that our method outperforms the compared models. Code: https://github.com/LiLiXJTU/GeoProto-LLM.

---

## uid: `doi:10.2139/ssrn.7010979`

- title: Title:- AI Cortex to Physical Muscle: Real-Time LLM-to-Joint Translation
- authors: Rachna Miglani, SUNEEL CHOPRA
- affiliations: not stated
- posted: 2026-06-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7010979
- keyword hits: large language model, llm

### abstract

Translating high-level artificial intelligence directly into the physical muscle actuation in real time remains a fundamental challenge in the embodied robotics and neuroprosthetics. This paper presents a novel and framework for real-time LLM-to-joint translation, bridging an AI "cortex" — powered by the Large Language Model — to physical muscle actuators controlling articulated joints. The system employs the hierarchical architecture where the LLM interprets natural language and task-level goals into symbolic motion primitives, which are then decoded by a lightweight neural translator into joint-angle trajectories and corresponding muscle and activation signals. A predictive proprioceptive loop compensates for LLM inference latency (80–150 ms) by the forecasting joint states 200 ms ahead, enabling stable closed-loop control at the effective latencies below 50 ms. Validated on a multi-joint limb with the pneumatic artificial muscles, the framework achieves real-time translation of abstract and commands (e.g., "reach and grasp") into coordinated muscle-joint actions with 90% zero-shot generalization to the novel verbal instructions. This work demonstrates that and language-driven AI cortex can directly and robustly command physical muscle systems in the real time, opening pathways for intelligent, compliant, and linguistically and interactive physical agents.

---

## uid: `doi:10.2139/ssrn.7010223`

- title: CoLLM: AI engineering toolbox for end-to-end deep learning in collider analyses
- authors: Ahmed Hammad, Mihoko Nojiri, Waleed Esmail
- affiliations: not stated
- posted: 2026-06-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7010223
- keyword hits: large language model, large language models

### abstract

Recent improvements in large language models have opened new opportunities for accelerating and automating scientific workflows. In parallel, modern collider analyses are becoming increasingly complex and demand substantial programming and deep learning expertise. CoLLM alleviates this workload by using pretrained large language models to generate physically consistent analysis code for event selection. Additionally, it automates subsequent deep learning analyses. To further reduce reliance on programming or deep learning experience, CoLLM provides a graphical user interface that allows users to perform end-to-end analyses through an interactive interface. The main motivation behind CoLLM is to lower the coding burden and simplify the technical complexity of collider analyses, which increasingly depend on sophisticated event selections and advanced deep learning methods.

---

## uid: `doi:10.2139/ssrn.6892319`

- title: Generative AI Art and Copyright Governance: Rethinking the Adaptation Right and its Limits
- authors: Orit Fischman-Afori
- affiliations: not stated
- posted: 2026-06-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6892319
- keyword hits: generative ai

### abstract

Generative AI has become part of contemporary artistic practice, enabling the creation of texts, images, music, and audiovisual works through processes of variation, recombination, and transformation. As AI-generated outputs increasingly resemble existing works, disputes have intensified over how such creative connections should be understood and governed. Much of the current copyright debate approaches these questions through the lens of reproduction, focusing on copying during AI training or in the process of generating outputs. This emphasis leaves an important gap: how to evaluate creative reliance that is non-literal, indirect, and difficult to trace to specific technical processes. This article addresses that gap by revisiting the copyright framework governing adaptations and derivative works. Rather than treating copyright doctrine as a fixed set of rules, the analysis approaches it as an evolving conceptual framework shaped by changing modes of cultural production. By examining the historical development of the adaptation right, its implementation across jurisdictions, and its relationship to the principle that copyright protects expression rather than ideas, the article highlights its potential to govern forms of creative transformation that fall between copying and independent creation. Building on this insight, the article proposes an output-oriented inquiry based on “substantial recognisable linkage,” asking whether an AI-generated work can reasonably be perceived as drawing on protectable expression in a prior work, rather than merely reflecting shared styles, genres, or ideas. Focusing on the observable qualities of AI-generated outputs as they are perceived in their cultural context, this approach offers a conceptual vocabulary aligned with creative practices such as remix, variation, and stylistic exploration. At the same time, the article emphasises that any broader reliance on adaptation-based protection must be accompanied by robust exceptions and limitations, in order to preserve artistic experimentation, cultural exchange, and freedom of expression in AI-mediated creative environments.

---

## uid: `doi:10.2139/ssrn.6892440`

- title: Product Architecture and the 2B/2C Divide: Why Target Customer Clarity Matters
- authors: Jian Ding, Yixiao Zhou
- affiliations: not stated
- posted: 2026-06-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6892440
- keyword hits: generative ai

### abstract

Why do some digital products charge users directly (2C), while others rely on businessside monetization (2B)? Existing two-sided market and media economics literatures treat user heterogeneity as exogenous and assume 2C pricing is always feasible, focusing on "how to price" conditional on a given product architecture. They do not explain whether unified 2C pricing is structurally possible at all, nor why some product architectures systematically preclude it. This paper shifts the question from optimal pricing to contractual feasibility. Building on transaction cost theory, we argue that product architecture determines whether a firm can draw a coherent target customer persona. When a product bundles highly heterogeneous use cases (e.g., a superapp, a generalpurpose AI model), no single persona fits; unified 2C pricing becomes infeasible because the firm cannot effectively separate consumers by their willingness to pay at acceptable cost. Monetization then shifts to 2B channels or layered contracts. To isolate this mechanism, we employ an extreme-case design with within-firm comparisons (Tencent WeChat vs. its gaming and music units) and longitudinal changes (The New York Times before and after divestiture). Cross-industry evidence from media, platforms, software, and AI confirms that narrower, coherent products support 2C pricing, whereas broader, heterogeneous systems necessitate 2B models. This paper contributes by endogenizing user heterogeneity to observable product structure, moving beyond the abstract parameters of existing models. Furthermore, it extends the logic of audience clarity-originally confined to media economics-to digital platforms, open-source software, and generative AI, demonstrating that functional heterogeneity imposes similar structural.

---

## uid: `doi:10.2139/ssrn.6892378`

- title: Business Insider: A Multi-agent Knowledge Graph Architecture for Corporate Control Inference and Strategic Vulnerability Analysis across Regulatory Jurisdictions
- authors: Amit  Vishnu Bhise
- affiliations: not stated
- posted: 2026-06-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6892378
- keyword hits: large language model

### abstract

This paper presents Business Insider, a multi-agent knowledge graph architecture for corporate control inference and strategic vulnerability analysis across multiple regulatory jurisdictions. The system constructs dynamically updated, multi-relational knowledge graphs from live government corporate registries-MCA India, SEC EDGAR (USA), and BRIS / Companies House (EU)-and applies a formally defined analytical pipeline to infer indirect ownership, quantify governance risk, and generate sovereign intelligence reports. The core technical contributions are: (1) a Graph-Based Ownership Inference Engine (GOIE) performing recursive control propagation using a Neumann series formulation with cycle-safe DFS traversal; (2) a Weak Founder Detection (WFD) module computing a multi-component governance vulnerability score calibrated per jurisdiction; (3) a graph-centrality Influence Network Mapper combining betweenness centrality, eigenvector centrality, PageRank, and degree centrality; and (4) a market power and acquisition attractiveness scoring engine. These components are orchestrated by five domain-specialized agents executing an eight-stage structured Intelligence Lifecycle, with all natural language synthesis performed by a locally deployed large language model for complete data sovereignty. Experimental evaluation across 22 companies spanning three jurisdictions demonstrates 93.8% indirect ownership inference accuracy, four retroactively validated governance risk classifications, a 200% improvement in relationship coverage over direct-only graph methods, and a 97% reduction in analyst effort compared to manual approaches. Source code is publicly available.

---
