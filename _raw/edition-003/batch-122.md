# Classification batch 122 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-122.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6876298`

- title: CNAF: Towards Reliable LLM Reasoning in High-Stakes Decision-Making with Step-Level Causal Necessity Validation
- authors: Zhizheng Huang, Genbao Xu, Yiheng Han, Nan Ma
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6876298
- keyword hits: chain-of-thought, large language model, large language models, llm

### abstract

Reasoning with large language models in high-stakes decision-making settings requires not only correct conclusions but also reasoning processes that are inspectable, traceable, and causally reliable. However, existing chain-of-thought methods are generally outcome-oriented and tend to produce reasoning steps that appear plausible but are causally invalid. Their core limitation is that they cannot distinguish the surface logical plausibility of a step from its causal necessity for the final conclusion, which undermines the credibility of complex task decomposition. To address this issue, we propose CNAF (Causal Necessity-Aware Framework), a step-level causal necessity validation framework for high-stakes decision-making scenarios. The framework contains three core modules: (1) CausalStep, which performs counterfactual testing on each reasoning step to quantify its true contribution to the correctness of the final conclusion; (2) Div-DPP, which applies determinantal point processes to diversity-weight multiple solution paths for the same problem and identify invariant key logic that remains stable across paths; and (3) a low-cost causal supervision construction pipeline, which combines offline data synthesis with staged training to automatically produce trainable causal supervision signals for small and medium-sized models. Experimental results show that CNAF significantly outperforms existing methods on general benchmarks such as GSM8K, BBH, and ARC, as well as on high-risk industry datasets including ElecBench, FinQA, and CUAD. In particular, it delivers clear gains in the causal reliability and step-level interpretability of the reasoning process. By shifting task decomposition from generating seemingly plausible reasoning to validating the causal necessity of each step, CNAF provides effective support for the trustworthy deployment of large language models in real-world high-stakes decision-making applications such as power fault diagnosis and financial analysis.

---

## uid: `doi:10.2139/ssrn.6817643`

- title: SoK: AI-Assisted Threat Intelligence Pipelines -A Taxonomy and Research Agenda for the Agentic Transition
- authors: Nishant Tyagi
- affiliations: not stated
- posted: 2026-06-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6817643
- keyword hits: agentic, large language model, large language models

### abstract

Cyber Threat Intelligence (CTI) is in the middle of an architectural transition. Organizations are layering machine learning, large language models, and most recently autonomous agents into operational pipelines faster than the literature can document, and production practice has outpaced academic evaluation. Most published evaluations still focus on isolated model performance, while practitioners report that production success depends on governance, integration, and human-AI collaboration. This systematization makes three contributions. First, it operationalizes the CTI Autonomy-Stakes Framework through the Behavioral Autonomy Criteria (chained reasoning, state change, external effect, approval gating), a proposed set of observable tests for classifying AI-CTI systems by actual behavior rather than vendor description. The framework locates systems on dimensions of agent autonomy and decision consequence, with a "Guarded Agency" zone where viable production systems should sit. Second, it organizes the field into three architectural generations-rule-based with analyst review, AI-assisted analysis, and agent-directed execution-plus an autonomous-defense boundary, and grounds the framing in the documented evolution of named SOAR and SIEM platforms. Third, it identifies a research agenda focused on the evaluation gaps and adversarial-robustness questions most likely to determine whether the agentic transition produces trustworthy systems, in an environment where threat actors themselves are now operating AI-augmented tooling. The corpus weighs practitioner-authored and platform-derived sources alongside peer-reviewed work; in a field where production systems appear before academic evaluation of them, a SoK restricted to peer-reviewed sources would describe a field that does not exist.

---

## uid: `doi:10.2139/ssrn.6885261`

- title: Artificial Intelligence in Finance as Algorithmic Decision Formation: A Systematic Scoping Review
- authors: Yoocheol Noh, Jaeweon You
- affiliations: not stated
- posted: 2026-06-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6885261
- keyword hits: ai agent, llm, llms

### abstract

Artificial intelligence is no longer a peripheral analytical technique in finance. It increas ingly participates in the production of financial information, the learning of decision cri teria, the execution of financial actions, and the redesign of governance processes. Yet the AI finance literature remains dispersed across machine learning methods, credit scoring, asset pricing, market microstructure, financial NLP, regulatory technology, model risk, and financial stability. This article develops a systematic scoping review and integrative conceptual synthesis of AI finance. Drawing on a formal Scopus/Web of Science search and a staged screening and full-text confirmation protocol, the review organizes the field into five recursive clusters: AI methods, AI-finance applications, financial theories reinter preted by AI, market-level consequences, and governance and regulatory responses. The article advances an Algorithmic Decision-Formation framework that conceptualizes AI fi nance through four mechanisms: representation, criterion formation, operationalization, and governance-mediated redesign. The framework specifies the finance-specific coupling through which learned criteria become institutional, market, and supervisory decision structures. We show that AI in finance is not merely a means of automating existing decisions but a recursive system that shapes what financial information is recognized, how decision criteria are learned, how model outputs become institutional and market actions, and how governance feedback restructures financial decision systems. This per spective reframes governance and financial stability as constitutive of AI finance rather than peripheral regulatory concerns. The framework supports cumulative and compara tive research on mechanism-level questions involving alternative data, financial NLP and LLMs, delegated AI agents, model risk, financial stability, platform concentration, and cross-jurisdictional regulatory variation.

---

## uid: `doi:10.2139/ssrn.6885432`

- title: An Agentic AI Framework with Large Language Models and Chain-of-Thought for UAV-Assisted Logistics Scheduling with Mobile Edge Computing
- authors: Hanwen Zhang, Dusit Niyato, Wei Zhang, Xin Lou, Malcolm  Yoke Hean Low
- affiliations: not stated
- posted: 2026-06-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6885432
- keyword hits: agentic, chain-of-thought, large language model, large language models, retrieval-augmented

### abstract

In cloud manufacturing, unmanned aerial vehicles (UAVs) can support both product collection and mobile edge computing (MEC). This joint operation forms a hybrid scheduling problem, where physical logistics decisions are coupled with computational task scheduling. In this paper, UAVs collect finished products from manufacturing stations and transport them back to a central depot. Meanwhile, computational tasks generated by industrial sensor devices at these stations are processed locally, at UAVs, or offloaded via UAVs to the cloud. This coupling makes the problem challenging. A UAV can provide MEC services only during its service window at a station, so routing decisions directly determine when UAV-assisted offloading is available. Routing decisions also affect the UAV energy budget and the availability of onboard computing and communication resources for computational task execution under task deadline constraints. To address this, we propose an agentic-AI-assisted optimization framework with two components. First, we develop an agentic AI that combines large language models, retrieval-augmented generation, and chain-of-thought reasoning to translate user input into an interpretable mathematical formulation for the hybrid scheduling problem. Second, we design a hierarchical deep reinforcement learning approach based on proximal policy optimization (PPO), where the upper layer learns UAV routing and the lower layer optimizes per-slot task execution and resource allocation. Simulation results show that the proposed framework yields more consistent formulations, while the hierarchical PPO achieves full product collection in 99.6% of the last 500 episodes and maintains a 100% deadline satisfaction rate, with more stable performance than the advantage actor-critic approach.

---

## uid: `doi:10.2139/ssrn.6890079`

- title: FlattenGPT: Depth Compression for Transformer with Layer Flattening
- authors: Ruihan Xu, Qingpei Guo, Yao Zhu, Xiangyang Ji, Ming Yang, Shiliang Zhang
- affiliations: not stated
- posted: 2026-06-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6890079
- keyword hits: llama, llm, prompting, qwen

### abstract

Recent works have indicated redundancy across transformer blocks, prompting the research of depth compression to prune less crucial blocks. However, current ways of entire-block pruning suffer from risks of discarding meaningful cues learned in those blocks, leading to substantial performance degradation. As another line of model compression, channel pruning can better preserve performance, while it cannot reduce model depth and thus often brings limited latency reduction in autoregressive inference. To pursue better model compression and acceleration, this paper proposes FlattenGPT, a novel way to detect and reduce depth-wise redundancies.By flatting two adjacent blocks into one, it compresses the network depth, meanwhile enables more effective parameter redundancy detection and removal. FlattenGPT allows to preserve the knowledge learned in all blocks, and remains consistent with the original transformer architecture. Extensive experiments demonstrate that FlattenGPT enhances model efficiency with a decent trade-off to performance. It outperforms existing pruning methods in both zero-shot accuracies and WikiText-2 perplexity across various model types and parameter sizes. On LLaMA-2/3 and Qwen-1.5 models, FlattenGPT retains 90-96% of zero-shot performance with a compression ratio of 20%. It also outperforms other pruning methods in accelerating LLM inference, making it promising for enhancing the efficiency of transformers.

---

## uid: `doi:10.2139/ssrn.6836181`

- title: Remote Sensing Image Change Captioning in the Age of Foundation Models
- authors: Keyan Chen, Chenyang Liu, Wenyuan Li, Bowen Chen, Zhengxia Zou, Shijian Lu, Zhenwei Shi
- affiliations: not stated
- posted: 2026-06-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6836181
- keyword hits: agentic, foundation model, in-context learning, large language model, retrieval-augmented

### abstract

Earth observation (EO) foundation models are advancing the understanding of dynamic Earth-surface processes by learning transferable representations from multi-temporal and multi-source data, providing a foundation for monitoring land-cover and land-use dynamics. However, conventional change detection methods typically represent changes as binary or multi-class maps, which indicate where changes occur, but provide limited information about scene-level context, attribute variations, spatial relations, or structured temporal transitions. Remote sensing image change captioning (RSICC) addresses this limitation by formulating change understanding as a language generation task conditioned on bi-temporal or multi-temporal observations, thereby linking pixel-level visual evidence to object- and scene-level semantic interpretation. Recent studies have extended RSICC from task-specific encoder–decoder models to multimodal large language model (MLLM) systems that support instruction following, retrieval, dialogue, and agentic geospatial reasoning. This paper systematically reviews deep learning-based RSICC. It formalizes the task, clarifies its relation to change detection and image captioning, and analyzes three major challenges: pseudo-change suppression under acquisition and environmental variability, fine-grained grounding of multi-scale targets, and spatiotemporal reasoning under limited supervision. It then examines the methodological evolution of RSICC, covering sequential encoder–decoder baselines, attention-based fusion models, localization-aware multi-task learning, and recent MLLM-based frameworks for parameter-efficient adaptation, retrieval-augmented generation, in-context learning, and agentic reasoning. It further summarizes benchmark datasets, evaluation protocols, and empirical trade-offs among accuracy, model capacity, and latency. The analysis identifies persistent weaknesses in current evaluation: biased handling of unchanged samples and insufficient assessment of long-form, long-horizon temporal, and factually grounded descriptions. Finally, it discusses future research directions, including scalable long-tail data generation, unified multi-source representation, physically grounded temporal reasoning, hallucination control, and efficient deployment.

---

## uid: `doi:10.2139/ssrn.6878393`

- title: Dynamic Knowledge Graph-Based Research Gap Discovery: A Graph-Theoretic Alternative to RAG-Based Synthesis
- authors: Saravanakumar Kandasamy, Rahul Dachepally
- affiliations: not stated
- posted: 2026-06-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6878393
- keyword hits: agentic, llm, prompting, retrieval-augmented

### abstract

Conducting a Systematic Literature Review (SLR) by hand is slow, error-prone, and increasingly impractical as publication volumes continue to grow. Mulla et al.~\cite{mulla2026hcai} partially addressed this by pairing an agentic AI pipeline with Retrieval-Augmented Generation (RAG) for gap synthesis; yet the resulting gap statements are non-reproducible, opaque, and confined to single-paper analysis. We take a different route. Rather than prompting a language model to narrate gaps, we build a \textbf{Dynamic Knowledge Graph-Based Research Gap Discovery Engine} that treats gaps as measurable structural anomalies in a temporal knowledge graph. Typed triples $\langle$entity, relation, entity$\rangle$ are extracted from each filtered paper, merged into a publication-timestamped multigraph, and then analysed by two complementary algorithms: orphan cluster detection using Louvain community partitioning, and temporal decay analysis that flags concepts whose citation activity has stalled. Every gap output carries a composite confidence score and a concrete subgraph path that reviewers can inspect and contest. On an eight-paper medical image segmentation corpus (96 nodes, 79 edges), the engine surfaced 30 distinct research gaps --- 3.75$\times$ the yield of the Mulla et al.\ RAG baseline (8 gaps) and 1.25$\times$ that of a direct LLM prompt (24 gaps) --- with fully deterministic, traceable outputs. The system ships as a domain-agnostic Streamlit application, and our findings suggest that graph-theoretic gap discovery is both more productive and more auditable than free-text generation for research synthesis tasks.

---

## uid: `doi:10.2139/ssrn.6836918`

- title: Divergent Minds, Convergent Baselines: A Bounded-Rationality Account of LLM-Human Strategic Behaviour
- authors: Po Han Teo
- affiliations: not stated
- posted: 2026-06-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6836918
- keyword hits: fine-tuning, llm, llms

### abstract

Researchers have started using LLM agents in place of human subjects in behavioural and politicalscience experiments, often as a cheaper substitute for laboratory pools. The substitution does not hold up in strategic settings: humans and LLMs reliably make different choices, and neither fine-tuning on human response data nor persona conditioning has closed the gap. The behavioural-economics literature has, since Simon's introduction of bounded rationality, modelled human strategic behaviour as a classical baseline plus an additive correction term δ. The framework proposed here reads δ as the mathematical signature of bounded computation: the gap between what an unboundedly-rational agent would compute and what a computationally bounded agent actually produces. For canonical games whose solutions are present in standard training corpora, LLMs retrieve and recombine corpus material, bypassing the bound that produces δ in humans. The framing extends to reasoning-distilled models through cognitive-hierarchy theory: their accessible level-k strategic reasoning is bounded by compute budget and context length rather than by the cognitive constraints that bound humans, and the δ they produce, if any, carries different structural signatures. Four operational tests (conditional dependence, distributional asymmetry, path-dependence under repetition, and paraphrase-robustness) are proposed to discriminate human-shaped δ from LLM-shaped δ. A moderator prediction is that |δ| scales with peer-signal individuation in the decision environment, with a quantitative bound of Cohen's d ≥ 0.5 between named-opponent and aggregate-opponent settings.

---
