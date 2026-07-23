# Classification batch 177 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-177.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7065072`

- title: Predicting the Unseen: Multi-modal LLMs with Memory Consolidation for Video Future Event Predictio
- authors: Chenghang Lai, Xuli Shen, Haibo Wang, Manhui Zheng, Duantengchuan Li
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7065072
- keyword hits: large language model, llm, llms

### abstract

Video future event prediction is an emerging and challenging task that aims to forecast the potential progression of video narratives based on prior content. The primary challenge lies in capturing complex temporal dependencies and inter-event relationships within video sequences to predict subsequent events accurately. This paper proposes a novel multi-modal large language model for video future event prediction. We propose an autoregressive segment-level prediction strategy that divides long videos into shorter segments, leveraging integrated memory from the current segment to iteratively predict subsequent segment content until the final event prediction. The model incorporates a memory consolidation module comprising a visual memory consolidation component and a scene graph knowledge reasoning component, which consolidate visual and scene graph knowledge memory, respectively. To predict the content of the next segment, the visual memory consolidation component captures the cumulative visual context up to the current segment, encoding it into a fixed-length global memory to effectively model long-range dependencies while reducing redundant information. Additionally, the scene graph knowledge reasoning component extracts structured relational information from each segment and tracks the evolution of static object relationships to uncover latent temporal dynamics, thereby enhancing contextual representations. Experimental results show that our approach surpasses existing methods, with ablation studies validating the effectiveness of our designed modules.

---

## uid: `arxiv:2607.05355v1`

- title: Faithfulness to Refusal: A Causal Audit of Neuron Selectors
- authors: Ananth Eswar, Pratinav Seth, Utsav Avaiya, Vinay Kumar Sankarapu
- affiliations: not stated
- posted: 2026-07-06
- source: arXiv
- link: https://arxiv.org/abs/2607.05355v1
- keyword hits: llm, llms

### abstract

Attribution scores increasingly identify which neuron rows of a language model matter for applications such as pruning, interpretability, and editing for safety, yet whether they identify causally important rows is rarely tested directly. We address this with two paired audits built on one-shot neuron-row zeroing. We first audit selectors at the language-modeling level: attribution methods substantially outperform activation and magnitude-based baselines at identifying dispensable rows across five LLMs. We then adapt the same intervention into a behavior test by driving it with a contrastive harmful-versus-benign signal; the attributed rows are sufficient to install refusal on hate and crime while keeping benign over-refusal low and preserving language model fluency, and specific in that layer-matched random controls at the same depths fail. Highly rank-stable selectors can be among the least causally valid. Refusal moreover lives in a redundant subspace, where different attribution methods install it through largely disjoint row sets, so the recovered edit is one realization of a sufficient set rather than a unique mechanism. Together, these findings show that rank-stability proxies miss the kinds of selector failures a direct causal audit can surface.%

---

## uid: `arxiv:2607.05483v1`

- title: PatchOptic for Shared-State LLM Workflows with Projected Views and Verified Structured Updates
- authors: Zhaoyu Bai, Jiaqi Cai
- affiliations: not stated
- posted: 2026-07-06
- source: arXiv
- link: https://arxiv.org/abs/2607.05483v1
- keyword hits: agentic, llm, retrieval-augmented

### abstract

Agentic workflows often operate over shared, structured state. Because LLM context windows are limited, each model invocation is typically shown only the state fragment needed for the current workflow step, a pattern commonly known as progressive disclosure. Modern systems construct such model-facing views using grep-like keyword search, retrieval-augmented generation (RAG), abstract-syntax-tree (AST) queries, and task-specific agent skills. These methods make the read side manageable, but they do not define when a locally proposed rewrite is valid after it is applied back to the full state. The missing piece is a contract between local updates and global validity. We introduce PatchOptic, an optic-inspired interface for shared-state LLM workflows. Optics are compositional bidirectional accessors that describe how views of structured data are read and updated. PatchOptic borrows this view/update intuition and realizes it through projected reads and verified structured patches. Each workflow step declares a projected read view, an authorized write region, and a patch-source region. Beyond runtime enforcement, the same declaration yields a path-level footprint that supports delegation, sub-workflow composition, and static certificates for reordering independent steps within the same phase. We evaluate this design with PatchBench, a benchmark with 46 cases across domains. The results show that projected reads reduce reported leakage and token cost while preserving accepted-output quality under the strong actor. Runtime verification blocks declared workflow-contract violations before commit, and patch-read enforcement rejects compromised patch artifacts that use hidden sources.

---

## uid: `arxiv:2607.04572v2`

- title: Context-Masked Truncated Reasoning Audits for Answer-Key Dependence in LLM Tutors
- authors: Bonan Shen, Dingyan Shang, Youting Wang, Tao Ning, Bowen Liu
- affiliations: not stated
- posted: 2026-07-06
- source: arXiv
- link: https://arxiv.org/abs/2607.04572v2
- keyword hits: large language model, llm

### abstract

Large language model (LLM) tutors may have access to teacher notes, answer keys, rubrics, or retrieved solutions while producing student-facing explanations. We study whether truncated reasoning probes can distinguish direct access to such private context from answer information carried by the written explanation. Using Truncated Reasoning AUC Evaluation (TRACE), we evaluate 1000 GSM8K problems under question-only, correct answer-key, and wrong answer-key contexts. When forced-answer probes retain the private key, answer-key TRACE AUC rises from 0.375 to 0.900, and the gold answer is recoverable with no explanation at all in 998 of 1000 cases. We then introduce a context-masked replay: answer-key-generated prefixes are probed under the corresponding question-only prompt. Masking reduces 10\% prefix accuracy from 0.997 to 0.126 and median AUC from 0.900 to 0.375, nearly matching question-only values of 0.113 and 0.375. On 746 pairs where both explanations end correctly, the masked mean AUC difference is $-0.0086$ with a 95\% bootstrap interval spanning zero. Wrong keys still account for 272 of 387 incorrect final responses, showing that private artifacts can influence outputs even when early-prefix evidence disappears after masking. These results establish context masking as necessary for attributing early answer availability to an explanation rather than its hidden input.

---

## uid: `doi:10.2139/ssrn.7071890`

- title: Capability trade-offs in generative AI: How absorptive capacity and customer orientation selectively configure organisational gains and risks
- authors: Ahmed Almoraish, Seongsoo Jang, Mansour Alyahya, Spyridon Gounaris
- affiliations: not stated
- posted: 2026-07-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7071890
- keyword hits: generative ai, generative artificial intelligence

### abstract

Generative artificial intelligence (GenAI) is embedded in professional service work, yet its consequences remain uneven and capability dependent. This study examines how GenAI usage shapes organisational gains and risks in B2B marketing agencies and how absorptive capacity and customer orientation selectively configure these outcomes. Drawing on Sociotechnical Systems and Dynamic Capabilities theories, the research combines interviews with agency managers (n = 20), a two wave survey (n = 425) and archival financial data (n = 255).GenAI usage strengthens employee content creativity, employee experience, marketing performance and financial performance. It also improves fulfilment of client data privacy expectations, indicating stronger privacy risk management, while increasing employee job insecurity. Absorptive capacity weakens employee and commercial gains and privacy risk management, but reduces workforce risk. Customer orientation strengthens employee and commercial gains and privacy risk management, yet does not reduce job insecurity. Archival results show positive associations with profit margin, labour productivity and revenue growth, but not return on assets.The study develops a capability trade off explanation of GenAI value creation. Rather than treating organisational capabilities as interchangeable or uniformly value enhancing, it shows that knowledge integration and market facing capabilities produce contrasting effects across employee, commercial, privacy and workforce domains. This extends Sociotechnical Systems theory by explaining how outcomes coexist within the same work system and refines Dynamic Capabilities theory by showing that capability value depends on the outcome pursued.For managers, GenAI deployment should combine customer focused application with employee safeguards, privacy controls, human oversight and capability development tailored to the outcomes sought.

---

## uid: `doi:10.2139/ssrn.6913278`

- title: Generative AI and the Future of Legal Scholarship (June 2026 Edition)
- authors: Andrew Perlman
- affiliations: not stated
- posted: 2026-07-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6913278
- keyword hits: generative ai, generative artificial intelligence

### abstract

For a century and a half, legal scholarship has been organized around a single artifact: the article. The article bundled four functions—discovery, communication, credentialing, and archiving—and every institution of the legal academy, from the student-edited law review to the tenure file to the judicial citation, is built on the artifact's distinctive properties: scarcity, fixity, and attributability. Generative artificial intelligence does not merely assist this system. It dissolves its organizing scarcity. When any competent legal argument can be produced on demand at negligible cost, the authored text loses the properties on which the artifact regime depends. The emerging literature has responded with what this Article calls the authentication paradigm: disclosure rules, certification regimes, and attestations of human authorship. This Article argues that authentication is a category error. It attempts to restore artificial scarcity to texts, when the scarcity that mattered was never textual. In its place, this Article develops a theory of latent scholarship. In the generative age, the de facto repository of legal thought is no longer the corpus of published writings but the model—the latent space from which arguments are drawn—and the scholarly acts that matter are those that form, validate, commit to, and architect regions of that space. The unit of scholarship accordingly shifts from the article to the maintained normative system: an executable, benchmarked, versioned instantiation of a legal theory that can be run against any case, probed adversarially, and revised in public. Influence shifts from the weight of authority to the authority of weights. The Article elaborates the theory's institutional corollaries—law reviews reconstituted as validation institutions, peer review as adversarial evaluation, tenure metrics keyed to measurable uptake, a Daubert framework for machine-mediated normative systems, and corpus stewardship as a public trust—and confronts the strongest objections, including the charge that this is Langdellian scientism reborn, the dangers of model collapse and epistemic monoculture, and the risk that the imperial scholar will simply be succeeded by the imperial model.

---

## uid: `doi:10.2139/ssrn.7074665`

- title: Governing Generative AI Concentration: Policy Responses to Geographic, Epistemic, and Network Inequalities in Global ICT Innovation (2018–2024)
- authors: Serhat Burmaoglu, ESRA DUNDAR ARAVACIK, Furkan Oguzhan Polat, Arif Soyler
- affiliations: not stated
- posted: 2026-07-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7074665
- keyword hits: generative ai, generative artificial intelligence

### abstract

This study examines policy implications of geographic, epistemic, and network concentration in generative artificial intelligence (GenAI) innovation. Analyzing 111,512 patent and publication records from 2018–2024 through bibliometric analysis, network science, and computational text analysis, we map three dimensions of concentration relevant to ICT governance. First, geographic distribution exhibits extreme inequality (Gini coefficient 0.762), with China and the United States jointly accounting for 58.1% of global GenAI innovation. Concentration intensifies over the observation period, with the Herfindahl-Hirschman Index rising from 1611.6 to 2358.6. Second, thematic analysis reveals that only 3.9% of documents address any inclusion theme under the validated baseline classification, with a pronounced hierarchy of attention: low-resource computing (1.5%) and accessibility (1.4%) dominate, while disadvantaged-population needs (0.3%) and digital-equity promotion (0.0%) are effectively absent. Third, international collaboration networks display preferential attachment dynamics (QAP β = 0.586, R2 = 0.723) consistent with cumulative advantage rather than equitable knowledge co-creation. We interpret these patterns through a decolonial framework that treats concentration as structural rather than incidental, while explicitly stating falsification conditions. We argue that the bipolar US–China configuration represents a new hegemon pattern in which a formerly peripheral state replicates rather than disrupts extractive dynamics. The paper develops concrete policy instruments across three governance domains: (i) data sovereignty frameworks (drawing on the Te Hiku Māori model and emerging African Union proposals); (ii) public investment in indigenous AI capacity (the Masakhane NLP and AI4D Africa models); and (iii) reciprocal collaboration funding (modelled on World Bank–AfDB co-investment instruments).

---

## uid: `doi:10.2139/ssrn.7069191`

- title: Fluctuation-Adaptive Model Scheduling for Dynamic Large-SmallModel Collaboration in Heterogeneous Edge Networks
- authors: DF D
- affiliations: not stated
- posted: 2026-07-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7069191
- keyword hits: large language model, large language models

### abstract

Deploying large language models at the network edge enables low-latency inference, but heterogeneous edge nodes and volatile wireless links pose formidable scheduling challenges.Bandwidth fluctuations severely degrade collaborative inference when large and small models exchange activations across unreliable paths. Existing schedulers often ignore link dynamics or react too late.This paper introduces the Fluctuation-Adaptive Model Scheduling (FAMS) framework for large-small model collaboration, explicitly incorporating real-time network dynamics into scheduling decisions. FAMS integrates three tightly coupled modules: (i) a wavelet-based detector extracting spectral features to classify link regimes; (ii) a graph-aware partitioning engine redistributing computation based on prevailing link quality; and (iii) a constrained reinforcement learning scheduler, trained via Lagrangian-relaxation proximal policy optimization (LR-PPO),balancing latency and accuracy under per-request deadlines.Extensive experiments are conducted on a physical testbed comprising NVIDIA Jetson modules, Raspberry Pi boards, and a cloud GPU server, driven by Lumos5G and CRAWDAD 5G/Wi-Fi traces. Across 10,000 text-generation requests from MMLU and HellaSwag, FAMS reduces average inference latency by 31.7% relative to the strongest baseline, while maintaining accuracy within 1.1 percentage points of cloud-only deployment. Under compound fluctuation scenarios, the latency advantage widens to 46.1%. Ablations confirm all modules contribute meaningfully, with dynamic task routing yielding the largest individual gain.

---
