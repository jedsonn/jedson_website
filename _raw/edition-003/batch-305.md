# Classification batch 305 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-305.answer.json` as a JSON array.

---

## uid: `arxiv:2606.08998v3`

- title: The Token Not Taken: Sampling, State, and the Stochasticity of AI Agents
- authors: Muhammad Zia Hydari, Raja Iqbal
- affiliations: not stated
- posted: 2026-06-08
- source: arXiv
- link: https://arxiv.org/abs/2606.08998v3
- keyword hits: agentic, ai agent, foundation model

### abstract

Agentic AI systems can behave differently across runs: the same request may produce a different plan, a different tool call, a different code edit, or a different final answer. Such variability arises from several layers that are often conflated. At the core of many current agents is a foundation model, a large pretrained model adaptable to many downstream tasks, embedded in an orchestration loop that plans, calls tools, observes results, and updates state. One explicit intrinsic source of variability in such systems is token generation: the model computes scores over possible next tokens, the scores are converted into probabilities, and a decoder may sample tokens using a pseudo-random number generator. A small sampled token difference can then cascade downstream into a different tool call, code path, search query, or agent state. Other sources of variability are extrinsic to token sampling, including changing environments, live data, serving infrastructure, batch effects, and numerical details. By separating these layers, this tutorial clarifies what it means to call agentic AI systems stochastic, when such variability can be reproduced under matched conditions, and why deterministic execution need not imply identical behavior in deployed settings.

---

## uid: `doi:10.2139/ssrn.6832660`

- title: Generative AI and the Right to Privacy in Myanmar
- authors: Thandar Yi Lin
- affiliations: not stated
- posted: 2026-06-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6832660
- keyword hits: generative ai, generative artificial intelligence

### abstract

Generative artificial intelligence creates new challenges for the right to privacy around the world. In Myanmar, these challenges combine with weak laws, widespread surveillance systems, and a harsh political climate. This article looks at how generative AI makes existing privacy problems in Myanmar worse. It reviews Myanmar's privacy laws, identifies specific risks posed by generative AI, and proposes changes to align Myanmar's approach with international human rights standards. The article argues that without strong legal protections, generative AI will likely be used for government control rather than helping people develop.

---

## uid: `doi:10.2139/ssrn.6906956`

- title: From Digital Consumption to Sovereign Compute: A Socio-Technical Framework for Generative AI in African Education
- authors: Raymond Onuoha
- affiliations: not stated
- posted: 2026-06-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6906956
- keyword hits: generative ai

### abstract

This paper explores the critical imperatives for integrating Generative AI (GenAI) into African education to prepare its workforce for the evolving global digital economy. It moves beyond adoption metrics to assess the structural alignment between technical infrastructures and social subsystems. Employing a qualitative multiple case study design, the research utilizes Socio-technical Systems (STS) directed documentary analysis of purposively selected initiatives—including AIMS/NEF, NgREN, and localized platforms like Digemy and AltSchool—to diagnose the ’compute divide’ and data sovereignty risks inherent in current models. The findings surface concrete misalignments in sovereign compute capacity, teacher autonomy, and policy governance. Finally, the paper proposes a phased policy roadmap to transition African education from ’API dependency’ to ’jointly optimized’ ecosystems, offering actionable pathways for policymakers to bridge the digital divide and foster leadership in the global AI discourse.

---

## uid: `doi:10.2139/ssrn.6902336`

- title: DiverseGuide: Automata-Based Steering for Diverse Structured Generation
- authors: Xiaokun Luan, Zeming Wei, Yihao Zhang, Meng Sun
- affiliations: not stated
- posted: 2026-06-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6902336
- keyword hits: large language model, large language models

### abstract

DiverseGuide is an open-source software artifact for diversity-aware structured generation with large language models subject to regular-expression constraints. Automata-based generators can guarantee validity by masking invalid tokens, but mask-only decoding does not actively explore the valid space defined by a constraint. DiverseGuide addresses this limitation by compiling each regular expression into a deterministic finite automaton (DFA), applying token-level masking over the DFA, and steering generation with path-history rewards, local-loop penalties, and adaptive logit scaling. The implementation provides a Hugging Face-compatible Python API, a Rust backend for regular-expression compilation and token-level DFA transitions, and optional native acceleration for diversity evaluation. The versioned artifact includes a validity-only baseline, tests, documentation, containerized setup, and scripts for reproducing the reported empirical results.

---

## uid: `doi:10.2139/ssrn.6905318`

- title: Fusing Large Language Model Reasoning with Modularity Optimization for Community Detection
- authors: Yujin He, Chuang Liu, Jianzhang Zhang, Ruiqi Li, Xiu-Xiu Zhan
- affiliations: not stated
- posted: 2026-06-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6905318
- keyword hits: large language model, llm

### abstract

Community detection aims to reveal mesoscale organization in complex networks, yet no single optimization criterion performs reliably across all network structures. Motivated by this limitation, we develop LLMRMO (Large Language Model-based Reasoning with Modularity Optimization), a community detection framework that combines semantic reasoning with structural refinement. LLMRMO first employs a large language model (LLM) guided by structured prompts to identify candidate community centers and infer a local leader-follower organization around them, producing an initial semantically informed partition. The partition is subsequently refined through a modularity-driven merging procedure with an additional community similarity constraint to avoid unreasonable aggregation across highly imbalanced groups. Experiments on diverse real-world networks show that LLMRMO achieves consistently stronger performance than 16 widely used baselines, with an average improvement of 14.3% in pairwise F_1-score over the best competing method. The proposed framework also remains effective for multiscale and homogeneous community structures where explicit centers are difficult to distinguish. Beyond network data, the framework can be naturally extended to clustering tasks on vector-derived similarity networks.

---

## uid: `doi:10.2139/ssrn.6907295`

- title: Cultural Ecosystem Services Mediate Landscape Effects on Resident Well-being in Urban Parks
- authors: Jiaxuan Shi, Dong Sun, Mei Lyu, Yumeng Meng, Hiroatsu Fukuda
- affiliations: not stated
- posted: 2026-06-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6907295
- keyword hits: large language model, large language models

### abstract

Urban parks are important components of urban green infrastructure and provide key spaces for aesthetic experience, recreation, social interaction, and emotional restoration. However, the mechanisms linking physical landscape features, cultural ecosystem service (CES) perceptions, and public sentiment remain insufficiently explained. Focusing on 15 urban parks in Shenyang, China, this study constructs a ”landscape features–CES perceptions–public sentiment” framework. Social media text, user-generated images, natural language processing, large language models, and image semantic segmentation were integrated to quantify CES perceptions, sentiment, and physical landscape features. Structural equation modeling was then used to examine their relationships.The results show that CES perceptions can be classified into five types: Landscape–Emotion, Landscape–Leisure, Cultural–Recognition, Comprehensive and Balanced, and Service–Problem types. The parks also show clear differences in openness, greenness, enclosure, landscape diversity, blue vision, and pedestrian activity. Overall, public sentiment is generally positive. Higher sentiment is mainly associated with waterfront activities, seasonal landscapes, sports and leisure activities, and everyday life scenes, whereas lower sentiment is more closely related to traffic environments, spatial quality, and insufficient service experiences. The structural equation model indicates that CES perceptions mediate the relationship between physical landscape features and public sentiment. In particular, the Blue Vision Index enhances positive sentiment by strengthening Leisure–Social CES, forming the most stable indirect pathway. Pedestrian activity has a dual effect, as it promotes leisure and social perceptions while also increasing problem-related perceptions.Overall, public sentiment is not directly determined by landscape elements themselves, but is formed through public viewing, use, interpretation, and meaning construction of park landscapes. These findings deepen the understanding of the ”physical environment–CES perceptions–public sentiment” relationship and provide references for urban park renewal, waterfront space optimization, and experience-oriented green space planning.

---

## uid: `doi:10.2139/ssrn.6908572`

- title: Separating Genuine Complexity from Concealment in 10-K Filings: Evidence from Income-Decreasing Restatements
- authors: Sripal Konchada
- affiliations: not stated
- posted: 2026-06-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6908572
- keyword hits: large language model

### abstract

A 10-K can be hard to read because the firm is genuinely complex or because managementis concealing unfavorable content, and the two are observationally identical onthe page. We separate them by projecting a battery of textual complexity measuresonto direct proxies for genuine business complexity, a large language model’s readingof the business description together with XBRL extension counts and segment structure,and treating the residual as opacity. Across 73,889 filings from 2011 to 2023,residual opacity predicts subsequent income-decreasing restatements, the realization ofburied bad news, with an odds ratio of 2.02. The relation survives a full battery ofrestatement-prediction controls among large, monitored firms (z = 2.38), while genuinecomplexity carries the opposite sign. Opacity that a firm’s business does not justifyforecasts the later correction of the record.

---

## uid: `doi:10.2139/ssrn.6456683`

- title: Predictive Home Network Automation: An Agentic AI-Driven CPE and Wi-Fi Orchestration Framework for Proactive Session Management
- authors: Rohan Rajidi
- affiliations: not stated
- posted: 2026-06-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6456683
- keyword hits: agentic, ai agent

### abstract

The proliferation of gigabit broadband access, hyper-dense Internet of Things (IoT) ecosystems, and latency-sensitive applications has fundamentally altered the performance requirements of the residential network. Traditional reactive network management, relying on manual troubleshooting and static rule-based automation, is increasingly inadequate for maintaining the strict Quality of Experience (QoE) demanded by modern digital services. This research report provides an exhaustive, in-depth analysis of a novel paradigm in telecommunications: predictive home network automation powered by Agentic Artificial Intelligence (AI). By synthesizing the capabilities of the Broadband Forum's User Services Platform (TR-369) with hierarchical multi-agent machine learning architectures, this research details a framework capable of deeply optimizing Customer Premises Equipment (CPE) and Wi-Fi mesh networks far beyond the traditional boundaries of the modem. The integration of session automation, facilitated by intent-based application programming interfaces (APIs) such as CAMARA Session Insights, enables AI agents to dynamically allocate resources, seamlessly steer mesh nodes, and execute proactive fault resolution before service degradation becomes perceptible to the end user. This comprehensive report investigates the theoretical foundations, algorithmic implementations-including Deep Reinforcement Learning (DRL) and Graph Neural Networks (GNN)-and evaluation metrics necessary to deploy autonomous, self-healing home networks.

---
