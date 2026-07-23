# Classification batch 103 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-103.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6989769`

- title: CauSAIL: Causal Graph-Grounded Multimodal LLMs for Maritime Supply Chain Disruption Detection
- authors: Khan  Enaet Hossain, Md.  Sajeebul Islam Sk., Md. Golam Rabiul
- affiliations: not stated
- posted: 2026-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6989769
- keyword hits: fine-tuning, large language model, llm, llms, retrieval-augmented

### abstract

Maritime supply chain disruptions arise from complex interactions among vessel movements, port operations, satellite observations, public events, trade dependencies, corporate filings, and global pressure indicators. Existing monitoring systems often collapse these diverse modalities into static feature representations and rely on Retrieval-Augmented language models without sufficient causal grounding, modality control, and feature verification. We present CauSAIL that addresses these gaps through four connected modules: (1) integration of seven open-access datasets through a port-month alignment pipeline; (2) develop a Causal Temporal Supply Chain Knowledge Graph (CT-SCKG) and build Retrieval-Augmented Fine-Tuning (RAFT)-based feature sets to ground LLM decisions in structured and textual features; (3) develop a Suppression-Focal Modality-Aware LAFAM module (MA-LAFAM) to combine diverse modalities by handling missing modalities and class imbalance; (4) propose mathematical bias-mitigation methods to reduce seven IBM-recognised LLM bias types. Experimental results show that CauSAIL effectively identifies port-month disruption patterns by connecting vessel traces, satellite imagery, supply-chain relations, and retrieved documents. Ablation study demonstrates that vessel movement Automatic Identification System (AIS) features provide major disruption signal, and CT-SCKG, RAFT feature, MA-LAFAM, and mathematical bias-mitigation methods improve robustness and reduce unsupported LLM decisions. These experimental results suggest that reliable maritime intelligence systems benefit from grounded system design rather than large language model scale alone. We release our data and code here \footnote{\url{https://github.com/mdsajeebulislamsk/CauSAIL}}.

---

## uid: `doi:10.2139/ssrn.6990359`

- title: Heterogeneous Feature Fusion-Empowered Multimodal Large Language Models for Bearing Fault Diagnosis
- authors: Qinglang Li, Hao Zhang, Dandan Peng, Bin Luo, Hui Cheng, Chenyu Liu
- affiliations: not stated
- posted: 2026-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6990359
- keyword hits: large language model, large language models, llm, llms

### abstract

The deployment of general Large Language Models (LLMs) in industrial fault diagnosis faces severe challenges due to the substantial adaptation gap between linguistic knowledge and high-dimensional physical signals. These challenges are mainly manifested in representational heterogeneity, reliability risks in the reasoning process, and blurred decision boundaries under long-tail distributions. To address these issues, this study proposes Heterogeneous Feature Fusion-Empowered Multimodal Large Language Model (HFF-MLLM), a framework that empowers LLMs through deep heterogeneous feature fusion and physical-information-based constraints. Specifically, the proposed architecture first establishes a cross-modal alignment mechanism based on dual-path projection, which maps the local dynamics of one-dimensional time series and the global spectral patterns of two-dimensional continuous wavelet transform images into a unified latent space. By leveraging complementary multimodal semantics, this design effectively overcomes the performance bottleneck associated with shallow fusion strategies. Meanwhile, to ensure the credibility of the reasoning process, a hybrid reasoning strategy is introduced. This module uses key signal indicators as explicit physical-feature guidance and imposes conditional constraints on the generation process via Low-Rank Adaptation (LoRA), thereby effectively suppressing the non-factual reasoning bias induced by purely data-driven paradigms. In addition, to address manifold collapse in imbalanced scenarios, a dynamic balance calibration mechanism integrating focal loss and entropy regularization is employed to reshape discriminative decision boundaries and suppress model overconfidence. Extensive empirical evaluations conducted on four datasets (CWRU, JNU, SEU, and their mixture) and across four LLM backbones and two Pre-trained Language Model (PLM) backbones verify the superior generalization capability of the proposed framework, which achieves peak accuracies of 99.32\% and 99.66\% on the JNU and SEU datasets, respectively.

---

## uid: `doi:10.2139/ssrn.6986845`

- title: Modeling Information-Driven Epidemic Dynamics with Risk Perception, Network Heterogeneity, and LLM-Based Information Signals
- authors: Akhil Kumar Srivastav, Jun Tanimoto
- affiliations: not stated
- posted: 2026-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6986845
- keyword hits: large language model, large language models, llm

### abstract

Infectious disease dynamics are influenced not only by biological transmission processes but also by information dissemination and human behavioral responses. To investigate these interactions, we develop an information-driven epidemic--behavioral framework that couples disease transmission, risk perception, and vaccination behavior through an information signal \(L(t)\). The proposed model incorporates multiple information-generation mechanisms, including prevalence-driven information, social reinforcement, information saturation, and delayed information transmission. Numerical simulations demonstrate that information structure plays a critical role in epidemic control. In particular, social reinforcement sustains risk perception and vaccination willingness, resulting in lower infection prevalence and a reduced effective reproduction number, whereas delayed information weakens behavioral adaptation and promotes recurrent outbreaks. Sensitivity analyses further show that information effectiveness and behavioral responsiveness jointly determine epidemic outcomes. To assess the robustness of these findings, the model is extended to a heterogeneous scale-free network using a heterogeneous mean-field formulation. The network results remain qualitatively consistent with the deterministic model, confirming that the beneficial effects of sustained information reinforcement persist under heterogeneous contact structures. Finally, we introduce an LLM-driven information layer that enables information signals to be constructed from digital information sources, including media activity, online search behavior, and textual information processed by large language models. Numerical experiments indicate that LLM-derived information can enhance risk perception, stabilize vaccination behavior, and improve epidemic control. The proposed framework provides a unified approach for studying information-driven epidemic dynamics, behavioral adaptation, and AI-assisted public-health interventions.

---

## uid: `doi:10.2139/ssrn.6989090`

- title: Text-Based ESG Beliefs and Mutual Fund Performance: Evidence from LLM Analysis of Fund Narratives
- authors: Yi Li, Andrew Urquhart, Wei Zhang
- affiliations: not stated
- posted: 2026-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6989090
- keyword hits: large language model, large language models, llm

### abstract

ESG beliefs are a key conceptual dimension shaping how investors integrate sustainability into investment decisions. We develop a novel text-based measure of fund managers' ESG-related narrative orientation by applying large language models to the strategy statements and market outlooks in mutual fund reports, and use it as an empirical proxy for managers' underlying ESG beliefs. Stronger ESG-related orientation in these narratives is positively associated with subsequent fund performance, yet investors do not appear to fully price it. The performance gains stem from superior stock selection: managers with stronger orientation overweight firms with higher ESG scores while remaining attentive to fundamentals. The effect is amplified after the carbon neutrality pledge, in favorable markets, and in funds with more institutional investors. Our findings highlight the economic importance of ESG-related managerial heterogeneity and provide new evidence on how sustainability considerations are incorporated into asset management.

---

## uid: `arxiv:2606.26079v1`

- title: Same Evidence, Different Answer: Auditing Order Sensitivity in Multimodal Large Language Models
- authors: Akshay Paruchuri, Sanmi Koyejo, Ehsan Adeli
- affiliations: not stated
- posted: 2026-06-24
- source: arXiv
- link: https://arxiv.org/abs/2606.26079v1
- keyword hits: gemini, large language model, large language models

### abstract

Standard benchmarks for multimodal large language models (MLLMs) score each item on one canonical ordering and miss whether order-irrelevant shuffling changes the answer, a baseline reliability property called for by emerging AI evaluation guidelines. We introduce Facet-Probe, a five-facet audit (option, evidence-chunk, document-rank, image-set, and mixed-modality ordering) of 18 frontier and open-weight MLLMs. A Bayesian item-response model separates ordering noise from per-facet bias, and a same-ordering control estimates the decoder-stochastic floor for observed flips. We find that none of the 18 MLLMs we audit are order-invariant: screened per-facet panel-mean flip rates span 24-50%. A Gemini same-ordering control at temperature 0 estimates a substantial ordering excess over a same-input decoder-noise floor in verified cells. Capability predicts but does not eliminate flips; the best model still flips on 13.4% of trials. In our Gemini mitigation tests, training-free prompt changes are modality-conditional and do not transfer from text to visual reasoning. These results suggest that prompt-level mitigation alone is unlikely to provide general order robustness, motivating future work on training-time and architectural approaches. We propose cross-ordering flip rate as a standard reporting axis for MLLMs.

---

## uid: `arxiv:2606.25984v2`

- title: InvestPhilBench: A Multi-Layer Benchmark for Evaluating Large Language Model Procedural Reasoning in Expert Investment Philosophy
- authors: Mingguang Chen, Bo Qu
- affiliations: not stated
- posted: 2026-06-24
- source: arXiv
- link: https://arxiv.org/abs/2606.25984v2
- keyword hits: claude, large language model, large language models

### abstract

Large language models are increasingly deployed as investment research assistants, yet no benchmark tests whether they can accurately reconstruct and apply the specific procedural decision frameworks of expert investors. We introduce InvestPhilBench, a multi-layer benchmark spanning eight cognitive tiers, from principle identification (L1) to novel framework extrapolation (L8). The v0.6 release comprises 118 primary-source-verified principle cards, 25 decision-framework cards with explicit topology metadata, and 243 QA questions (197 dev / 46 held-out test). For reproducible scoring at scale we introduce the Benchmark Automated Scoring Pipeline (BASP), five algorithmic metrics, the Failure Mode Detection Protocol (FMDP) covering six failure modes, and Gate Reconstruction Accuracy (GRA), a per-gate metric for questions with gold reasoning programs. This release is primarily a benchmark-and-methodology contribution: its empirical study -- a four-model sanity wave on the 188-question development split (closed-book) -- is deliberately preliminary and stress-tests the metric design rather than ranking models. The wave shows a sharp provider-tier split (BASP 0.906 vs. 0.438), though these mixed-judge numbers are confounded upper bounds. The central methodological finding survives the caveat: the BASP composite saturates at the frontier (Claude L4 = 0.932) while GRA still exposes a procedural deficit (frontier L4 GRA ~0.77, L7 GRA 0.57-0.62) -- composite scoring rewards fluent prose and hides the procedural gap. On a 100-item expert-annotated gold set, the automated BASP composite tracks the human reference at Pearson r = 0.72 (MAE = 0.10). v0.6 also implements a unified judge and true model-in-the-loop retrieval/oracle conditions; the de-confounded multi-model leaderboard and full three-condition run are v1.0 deliverables.

---

## uid: `doi:10.2139/ssrn.6997375`

- title: Research on Large Language Models for Building EnergyConsumption Integrating Domain-Specific Fine-Tuning andMulti-Agent Retrieval-Augmented Generation
- authors: wang panyue, yan hairong, Yuying Sun
- affiliations: not stated
- posted: 2026-06-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6997375
- keyword hits: fine-tuning, large language model, large language models, qwen, retrieval-augmented

### abstract

Facing the "dual carbon" goals and the demand for refined operation and maintenance of smart buildings, this paper proposes a large language model for the building energy consumption domain that integrates domain-specific fine-tuning with multi-agent retrieval-augmented generation. The proposed model addresses issues such as fragmented building energy consumption data, insufficient utilization of domain knowledge, and limited intelligent analysis capabilities. Based on Qwen2.5-7B, an instruction dataset covering energy consumption data, equipment operation and maintenance,fault diagnosis, and energy-saving strategies is constructed, and LoRA is employed for domainadaptation. Meanwhile, a knowledge base is established and a RAG mechanism is introduced to improve response accuracy and interpretability. Furthermore, a multi-agent collaborative framework is designed to enable intent parsing, data querying, knowledge retrieval, load forecasting, and energysaving decision-making. Experimental results demonstrate that the proposed model outperforms general-purpose large language models in tasks such as domain-specific question answering, Text-toSQL, knowledge recall, anomaly analysis, and load forecasting, thereby providing effective support for energy-efficient operation and maintenance as well as low-carbon decision-making in smart buildings.

---

## uid: `doi:10.2139/ssrn.6997097`

- title: Constraint-Based Entity Resolution with Small Language Models for Knowledge-Based Fault Injection in Heterogeneous AI Infrastructure
- authors: Yuanfang Chi
- affiliations: not stated
- posted: 2026-06-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6997097
- keyword hits: large language model, large language models, llm

### abstract

Fault injection is a critical methodology for validating the stability and fault tolerance of heterogeneous AI infrastructure. In knowledge-based fault injection, entity resolution is a key prerequisite for constructing reliable fault knowledge, determining whether heterogeneous alarm records can be normalized to the same fault entity. However, alarm data collected from monitoring systems, logs, device management platforms, and operational interfaces exhibit substantial variation in format, terminology, semantic granularity, and contextual scope, making safe and consistent entity aggregation difficult. Although large language models provide strong semantic reasoning capabilities, their inference cost and deployment overhead limit production applicability. Small language models are more operationally feasible, but their limited capacity makes them susceptible to ambiguity and weak contextual discrimination in fault-domain inputs. We propose a constraint-based entity resolution framework using small language models for knowledge-based fault injection. The framework formulates fault entity resolution as a domain-constrained decision problem that integrates heterogeneous alarm attributes, contextual signals, and external evidence under explicit consistency constraints, including type consistency, granularity consistency, causal-role consistency, vendor-context consistency, and evidence consistency. We introduce a Chain of Constraint reasoning mechanism that decomposes the decision into an ordered sequence of constraint evaluations and employs short-circuit inference to prevent unsafe merges. Evaluation results show that the proposed method consistently outperforms traditional LLM-based baselines in precision, recall, and F1 score. By embedding domain knowledge into the reasoning process, the proposed approach improves controllability, interpretability, and deployment efficiency, and provides a practical foundation for scalable fault aggregation and unified fault representation.

---
