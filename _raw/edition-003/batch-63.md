# Classification batch 63 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-63.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6715818`

- title: Human-AI Interaction in Creative Tasks: an Experimental Investigation
- authors: Federico Atzori, Luca Corazzini, Valeria Maggian, Filippo Pavesi, Massimo Scotti
- affiliations: not stated
- posted: 2026-05-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6715818
- keyword hits: chatgpt, generative ai, gpt-4, large language model, prompting

### abstract

We investigate how generative AI shapes creative performance and human-AI interaction in an open-ended writing task that employs a laboratory experiment in which participants are randomly assigned to either receive access to a large language model (ChatGPT-4.2) or not. Creative performance is measured by the average score assigned by independent evaluators recruited through the Prolific platform, and detailed logs of human-AI interaction are analyzed to measure AI use, prompting intensity, ideation requests, and the textual overlap between AI outputs and participants' final writings. Three main results emerge. First, AI access increases performance, but the gain is entirely driven by active use: participants with access who do not submit queries perform no better than those without AI. Second, the relationship between interaction intensity and performance is concave, peaking at roughly eight queries, consistent with iterative exploration rather than mechanical copying. Third, structural mediation analyses show that ideation requests affect performance primarily indirectly, by increasing downstream incorporation of AI-generated language; the direct effect of requesting an idea from the AI is negligible once execution-stage reliance is accounted for. We further document heterogeneity in AI reliance: cultural capital (proxied by books owned) predicts lower AI use, while prior AI exposure predicts higher use. By contrast, incentive schemes have limited effects on both outcomes and AI-related behaviors.

---

## uid: `doi:10.2139/ssrn.6727185`

- title: Decoding Maliciousness: A Scalable Framework for Malicious PyPI Package Detection via Multi-source Semantic Fusion
- authors: jiutian wang, Deming Mao, Ye Han, Zhaoheng Quan, Bingwen Wang
- affiliations: not stated
- posted: 2026-05-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6727185
- keyword hits: large language model, large language models, llm, llms, prompt engineering

### abstract

Context: The Python Package Index (PyPI) has become a primary target for software supply chain attacks. Existing detection methods often rely on single-dimensional analysis, which struggles to meet the scalability and real-time requirements of modern software ecosystems.Objectives: This study aims to develop a scalable and automated framework to accurately identify malicious PyPI packages by fusing multi-dimensional features, specifically focusing on the integration of code structural patterns and deep semantic understanding.Methods: We propose a framework that first employs static analysis to construct API call graphs and calculate four graph centrality metrics to capture structural features. Subsequently, Large Language Models (LLMs) with specialized prompt engineering are introduced to screen high-centrality APIs and eliminate noise. Finally, optimized structural features are fused with metadata features to construct a robust classification model.Results: Evaluations on a large-scale dataset of over 20,000 samples demonstrate that the proposed method achieves 97.2% precision and 97.3% F1-score. Notably, the framework exhibits exceptional efficiency, with an average end-to-end detection time of less than 1 second per package. It also shows strong robustness in highly imbalanced (1:50) scenarios.Conclusion: Our approach offers a high-precision, scalable solution for securing the open-source software supply chain. By effectively combining graph-based structural analysis with LLM-powered semantics, it provides a practical tool for advancing software quality assurance in real-world environments.

---

## uid: `doi:10.2139/ssrn.6670339`

- title: Breaking AI: A Practitioner's Framework for LLM and Agentic AI Security Testing
- authors: Dishanth CA
- affiliations: not stated
- posted: 2026-05-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6670339
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

The rapid enterprise deployment of Large Language Models (LLMs) and autonomous agentic AI systems has outpaced the security practices required to operate them safely. Traditional penetration testing methodologies — built on deterministic system assumptions — fail to address the probabilistic, natural-language attack surface introduced by AI deployments. This paper presents a structured, five-phase practitioner framework for LLM and agentic AI security testing, grounded in documented real-world attack patterns and aligned to OWASP LLM Top 10 (2025), OWASP Agentic Top 10 (2026), and MITRE ATLAS v5.1.0. The framework addresses four critical attack classes — indirect prompt injection via RAG corpus poisoning, agentic goal hijacking through multi-turn social engineering, system prompt leakage, and MCP tool poisoning — providing exploitation methodology, detection engineering guidance, and MITRE ATLAS technique mappings for each. Defensive countermeasures are presented across prevention, detection, and response layers, including sample detection logic for integration into SIEM and CI/CD pipelines. The paper establishes that organizations deploying AI systems without AI-specific security testing face material risks of data exfiltration, unauthorized autonomous action, and regulatory violation — and that a structured methodology mapped to existing frameworks is sufficient to close the execution gap.

---

## uid: `doi:10.2139/ssrn.6686418`

- title: Behavioral Digital Twins: Causally Constrained Synthetic Populations for Public Health Policy Simulation
- authors: Yichao Jin
- affiliations: not stated
- posted: 2026-05-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6686418
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Public health policy simulation increasingly relies on synthetic populations generated by large language models (LLMs), yet unconstrained generative agents frequently produce behavior that violates empirically observed choice patterns-a phenomenon we term causal hallucinations. We introduce Behavioral Digital Twins (BDT), a causally constrained framework that integrates three components: (1) discrete choice experiment (DCE) data as empirical ground truth; (2) structural causal models (SCMs) that capture the dependency structure among utility-relevant attributes; and (3) guided agent generation that enforces SCM-derived utility constraints during inference. BDT operates in three stages: inferring behavioral dependency structures from DCE responses via causal discovery (Stage 1), applying SCM-guided utility constraints to align synthetic agents with the empirical choice frontier (Stage 2), and evaluating counterfactual policy scenarios in a privacy-preserving local sandbox (Stage 3). We validate BDT on a real-world vaccination-timing DCE dataset collected from 1,027 adults in Wuhan, China. In synthetic validation, BDT reduced frontier-deviation MSE by up to 34% relative to unconstrained LLM agents. In a pilot experiment using a 10% sample of the DCE data and a 1.5B-parameter model deployed entirely on local consumer-grade hardware, BDT constraints reduced the causal hallucination rate from 50.0% to 22.2%-a reduction of over half-while maintaining a modest improvement in pointwise probability calibration. The repair effect is concentrated in high-wait regions where the unconstrained LLM systematically violates logical monotonicity, assigning higher acceptance probabilities to objectively worse alternatives. These findings establish three contributions. First, causal alignment through SCMguided constraints demonstrably outperforms unconstrained LLM generation in preserving the logical consistency of synthetic choice behavior. Second, the BDT framework offers a replicable blueprint for injecting behavioral discipline into LLM-based synthetic populations without requiring model retraining or fine-tuning. Third, the entire pipeline operates on workstation-class hardware with local data, supporting data sovereignty and compliance with health-data regulations such as HIPAA and GDPR. Taken together, BDT provides a principled approach to building causally grounded synthetic populations for privacy-preserving digital pre-trials of public health interventions.

---

## uid: `doi:10.2139/ssrn.6685878`

- title: The End of the Foundation Model Era: Commoditization, National Security, and the Path to AGI
- authors: Jared James Grogan
- affiliations: not stated
- posted: 2026-05-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6685878
- keyword hits: agentic, foundation model, large language model, large language models

### abstract

The foundation model era — roughly 2020 to 2025 — is over. The forces that defined it have inverted. Open source models have reached frontier performance while inference costs approach zero, exposing what was always structurally true: pre-training large language models at scale is not a durable competitive moat. The US government's formal designation of Anthropic as a supply chain risk in February 2026 accelerated a transition already underway — but did not cause it. The paper argues that the AI industry is restructuring simultaneously along four axes: economic, as the circular financing structure that inflated foundation model valuations collapses; technical, as the pre-training scaling paradigm gives way to post-training optimization, test-time compute, and agentic composition; commercial, as application-layer integrators displace the foundation model companies whose commodity they now consume; and political, as the government asserts its historic role as gatekeeper of strategic technology. These are not separate disruptions. They are one structural shift, arriving together. The most consequential and least-discussed dimension is the permanent divergence between commercial AI and a classified national security AI track — built on different data, governed by different rules, and developing capabilities the public ecosystem cannot see, measure, or govern. Like every dual-use technology that has altered the calculus of state power, AI is being brought under government authority not by design but by the structural logic of what it is. The paper further argues that open-weight models are the counterintuitive instrument of sovereign control: a government that holds the weights commands the capability on its own terms, without dependence on vendor policy, financial continuity, or personnel clearance. The apparent openness of distributed model weights is, from a deploying government's sovereignty standpoint, the most governable architecture — because what cannot be withdrawn by a vendor's API policy cannot be taken away. The paper draws on public financial disclosures, primary government and corporate sources, and academic literature in AI scaling, innovation economics, and national security technology policy.

---

## uid: `doi:10.2139/ssrn.6696098`

- title: Scalable Semantic Search with Generative AI Using Azure Cognitive Search: A Retrieval-Augmented Generation Framework
- authors: Rahul Modi
- affiliations: not stated
- posted: 2026-05-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6696098
- keyword hits: generative ai, large language model, large language models, retrieval-augmented

### abstract

The need to have large-scale enterprise knowledge retrieval with high relevance and low latency is also obliging semantic search systems to deliver on these requirements. This paper explores a scalable semantic search engine which combines retrievalaugmented generation (RAG) with Azure Cognitive Search and Azure OpenAI large language models. The system was evaluated on a corpus of 1.2 million enterprise style documents which were technical manuals, research articles and structured metadata records. The network proposed is a weighted synthesis using generative model and language models along with vector-based retrieval to produce responses to the given context. The experimental comparison of the proposed method and a baseline semantic retrieval system on embedding-based search was carried out. Findings indicate that the RAG-based system increased retrieval accuracy (0.78 to 0.89) and recall accuracy (0.72-0.87) by 17% in F1-score. Experiments on scalability also confirmed that there is consistent response latency when the query load is large, and that average response times are less than 1.05 seconds with datasets of more than two million indexed documents. Such results show that by combining generative AI and enterprise semantic search, it is possible to maximize contextual retrieval accuracy but still have scalable performance in large knowledge repositories.

---

## uid: `doi:10.2139/ssrn.6751686`

- title: Grounding large language models in hydrologic modelling
- authors: Yingjia Li, Shiruo Hu, Feng Zhang, Xinpeng Yu, Wei Luo, Dingxiao Liu, Bin Xu, Jianshi Zhao
- affiliations: not stated
- posted: 2026-05-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6751686
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Although large language models (LLMs) possess extensive hydrological knowledge, they often struggle to appropriately simulate complex physical processes in hydrological systems. To address this limitation, we present an LLM-based agentic intelligent modelling approach for hydrological time-series forecasting (HydroAIM). HydroAIM decouples the multi-agent architecture through the model context protocol (MCP) to integrate an expert task workflow, a standardised algorithmic workflow (SAW) library, and an iterative feedback closed-loop execution toolbox. Comprehensive experiments demonstrated that across 100 modelling tasks of varying types utilising four LLMs, HydroAIM achieved an execution success rate of 91%. Ablation studies have revealed that removing the expert task workflow causes complete system failure owing to planning chaos, plummeting the success rate to 0%. This result indicates that long-horizon task planning is the core bottleneck restricting LLMs from executing hydrological modelling tasks. Furthermore, when applied to 671 catchments in the Catchment Attributes and Meteorology for Large-sample Studies (CAMELS) dataset without human intervention, HydroAIM achieves median Nash-Sutcliffe efficiency (NSE) values of 0.63 and 0.64 for local and global modelling, respectively, meeting the application benchmarks established by traditional physical models. This study not only demonstrates the capability of LLMs as a hydrologic modelling tool but also provides a scalable pathway for grounding general LLMs in quantitative tasks within specialised scientific domains.

---

## uid: `doi:10.2139/ssrn.6752740`

- title: A Reproducible Prompting Method for Coding Classroom Behaviors from Observation Transcripts Using Large Language Models
- authors: Vanessa Peters, Xin Wei
- affiliations: not stated
- posted: 2026-05-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6752740
- keyword hits: large language model, large language models, llm, prompting

### abstract

Classroom observations are central to research on teaching quality, but the cost and labor of training human coders limits how widely this method can be applied. This paper documents a reproducible method for using a large language model to code instructor and student behaviors from speaker-labeled classroom transcripts. The method was validated against human-coded proportion scores from 25 undergraduate STEM classes across four prompting conditions. Prompt templates, the script that calls the model, and the validation statistics behind the reported results are provided so that researchers can adapt the approach to their own observation instruments and transcription tools. The key elements of the method are summarized below.• The method uses an LLM to estimate how much of a class session is spent on different teaching and learning behaviors from audio transcripts rather than in-person observation.• It tests a progression of prompting strategies, from no guidance to step-by-step reasoning with worked examples, and evaluates agreement with human-coded reference scores.• The method captures broad instructional patterns (e.g., lecturing vs. student activity) but shows limited performance for behaviors requiring nonverbal or auditory cues.

---
