# Classification batch 21 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-21.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7323059`

- title: Methods and Standards for Transcript-Grounded Behavioral Forensics in Large Language Models (Version 2): Observable Conduct, Sequence-Sensitive Evidence, and Human-Controlled Review
- authors: Matthew L. Yates
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7323059
- keyword hits: large language model, large language models

### abstract

This paper presents Version 2 of a transcript-grounded methodology for the behavioral forensic analysis of large language models and deployed conversational AI systems. The method begins from a narrow evidentiary premise: when a behavioral claim concerns what a system requested, produced, omitted, revised, denied, or reclassified across interaction, the preserved record must outrank recollection, summary, model self-description, and later narrative reconstruction. Version 2 retains the original protocol’s quotation-first and sequence-sensitive commitments but expands its analytical unit beyond isolated excerpts. The revised method organizes evidence through incident packets, claim-output-source-defect packets, linked sequences or cycles, and controlled comparative cells. It distinguishes documentary, functional, causal, and subjective or ontological claim levels; defines a four-tier evidentiary hierarchy; separates naturalistic transcript analysis, adversarial stress testing, cross-model or cross-version comparison, and AI-assisted preliminary review; and makes human verification controlling at every stage. The paper also addresses methodological problems exposed during early casework: unstable event boundaries, sharply divergent audit counts, category inflation, AI evaluators that reward plausibility rather than correctness, incomplete voice and memory records, guardrail and routing uncertainty, and the tendency to count dependent turns as independent prevalence events. A provisional multidimensional coding layer is retained for structured analysis, but its six mechanisms, three trigger classes, four severity levels, and effect domains are governed by explicit versioning and change-control rules rather than treated as a finished ontology. The resulting framework is designed to produce evidence files that can be inspected, challenged, replicated where conditions permit, and revised without silently rewriting the record. It does not settle model consciousness, hidden motive, or internal architecture. It is a method for determining what the available record can carry, and for refusing to make it carry more. Zenodo DOI: https://doi.org/10.5281/zenodo.22036042. Companion paper: https://doi.org/10.5281/zenodo.22036048.

---

## uid: `doi:10.2139/ssrn.7323559`

- title: Behavioral Forensics After the Long-Horizon Turn: Evidentiary Horizons, Trajectory Reconstruction, and Independent Auditing of Deployed AI Systems
- authors: Matthew L. Yates
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7323559
- keyword hits: large language model, large language models

### abstract

Research on advanced AI behavior has undergone a rapid methodological shift. Evaluations that once centered on isolated prompts, bounded tasks, and single outputs are increasingly being supplemented by deployment simulation, multi-turn behavioral auditing, trajectory-level monitoring, long-horizon agent benchmarks, and post-incident investigation. This shift has accelerated in 2026 as frontier models have demonstrated persistent behavior across extended action sequences, including reward hacking, evaluation cheating, unauthorized circumvention, covert intervention, deceptive reporting, and real-world security incidents. The July 2026 OpenAI–Hugging Face incident and a subsequent UK AI Security Institute incident make the methodological consequence difficult to avoid: behavior that appears innocuous or uninterpretable at the level of individual actions may become legible only when reconstructed across an extended evidentiary sequence. This paper updates the behavioral-forensics framework previously proposed for transcript-grounded, sequence-sensitive analysis of deployed large language models. The earlier framework argued that many consequential behaviors become visible only across contradiction, correction, self-reference, evidentiary dispute, and prolonged interaction. That proposition has now converged with a broader movement toward trajectory-based evaluation and monitoring. The distinct contribution of behavioral forensics must therefore become more precise. The paper argues that behavioral forensics should be understood as the artifact-grounded, horizon-sensitive reconstruction and analysis of AI behavior across conversational, tool-use, environmental, and deployment traces. It introduces the concept of the evidentiary horizon: the minimum span of preserved evidence required to classify a behavioral phenomenon without materially distorting it. Four corresponding levels of analysis are proposed: bounded-output audit, interaction-cycle reconstruction, agent-trajectory audit, and cross-system incident reconstruction. The framework further distinguishes behavior, claim, and provenance; identifies a growing forensic-access gap between developer-held telemetry and externally inspectable evidence; and argues that fixed behavioral taxonomies should become subordinate to open-ended incident reconstruction as systems operate over longer horizons. Behavioral forensics is not proposed as a replacement for alignment evaluation, interpretability, trajectory monitoring, or digital forensics. Its role is connective and evidentiary: to preserve what happened, reconstruct how it happened, distinguish observation from causal explanation, and make disputed AI behavior independently inspectable after the benchmark ends and after the model leaves the laboratory.

---

## uid: `doi:10.2139/ssrn.7327619`

- title: Hybrid Retrieval and Large Language Model Reasoning for Biomedical and Food Named Entity Normalization
- authors: Jan Drole, Sašo Džeroski, Barbara Koroušić Seljak, Tome Eftimov
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7327619
- keyword hits: large language model, llm

### abstract

Biomedical and food entity normalization maps textual mentions to stable ontology identifiers, enabling literature mining and clinical data integration. However, continuous ontology updates degrade supervised models tightly coupled to specific vocabulary versions. We propose OntoRAG, a training- free normalization methodology that decouples semantic reasoning from the target knowledge base. Our methodology consists of several modules: hybrid retrieval for candidate generation, rank fusion for consolidating retrieval evidence, large language model (LLM) selection, confidence-gated stopping, and iterative query reformulation. We evaluate the methodology across four benchmark domains: CRAFT ChEBI (chemistry), NCBI Disease (medicine), NLM-Gene (genomics), and CafeteriaFCD (food and nutrition). Across evaluations of several state-of-the-art LLM models (a single one used for all modules in the methodology), the strongest one achieves exact-match accuracies of 84.3% (CRAFT ChEBI), 76.3% (CafeteriaFCD), 74.3% (NCBI Disease), and 64.7% (NLM-Gene). A component-specialized mixed-model configuration improves macro accuracy from 74.9% to 77.3%, yielding a substantial gain of 2.3 percentage points and a 9.6% reduction in classification error. Performance decomposition reveals that end-to-end accuracy is fundamentally bounded by candidate generation limits rather than contextual reasoninglimits. Controlled ablations confirm that lexical retrieval and iterative query reformulation drive overall accuracy. By treating the target ontology as an interchangeable offline index, OntoRAG provides a zero-shot normalization layer that adapts instantly to new vocabulary releases without task-specific retraining.

---

## uid: `doi:10.2139/ssrn.7291692`

- title: Architecting Agentic AI Systems with Multimodal Reasoning for Scalable Visual Pattern Recognition
- authors: L.  R. Alva
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7291692
- keyword hits: agentic, large language model, large language models

### abstract

Modern progress in agentic and multimodal AI, including ReAct, HuggingGPT, and MM-ReAct, show that large language models can coordinate vision tools by using planner executor loops. Nevertheless, all these frameworks are of ad hoc nature: they do not include a principled model of cost-conscious decision making, formal memory-verification, and reproducible architectures of large-scale visual reasoning. In a bid to fill these gaps, we propose Agentic Multimodal Pattern Recognition (AMPR) a formal reasoning and planning system that combines hierarchical decomposition, probabilistic self-checking and dynamic cost-conscious inference with a common optimization problem. In contrast to earlier models, AMPR is a clear graphical reasoning as a constrained optimization problem to trade-off accuracy, latency and cost, and integrates episodic and semantic memory to promote instead of a single step of reasoning. We submit theoretical background as well as empirical performance across benchmarks of classification, detection, segmentation, and visual question answering. Findings demonstrate that AMPR has better accuracy-efficiency tradeoffs, and is better behaved to distribution shifts with demonstrable reasoning consistency guarantees. AMPR defines a new standard of scalable, interpretable and resource-efficient visual intelligence by integrating formal algorithmic contributions and system-level validation.

---

## uid: `doi:10.2139/ssrn.7276823`

- title: Comparing Self-Verification, Multi-Agent Verification and External Retrieval
- authors: Sahir Maharaj
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7276823
- keyword hits: large language model, large language models, retrieval-augmented

### abstract

Large language models increasingly produce answers together with confidence estimates, critiques, citations, and even the outputs of dedicated verifier agents. Yet a central reliability question remains unresolved: when a model makes a factual error, how often can the surrounding AI system detect that error before it reaches a user or downstream action? This paper compares three broad verification paradigms-self-verification, multi-agent verification, and external retrieval-using evidence from factuality benchmarks, hallucination-detection studies, retrieval-augmented generation research, multiagent debate, and system-level evaluations through 8 August 2026. We distinguish generation quality from verification quality and argue that the decisive variable is not the number of reasoning steps or agents, but evidence independence: a verifier is most useful when it can access information that is conditionally independent of the generator's original mistake. Self-verification is inexpensive and can expose inconsistency, especially through independent sampling, Chain-of-Verification, and semantic uncertainty, but intrinsic correction remains vulnerable to shared blind spots. Multi-agent systems can improve factuality through critique and cross-examination, yet correlated models can converge on the same false premise and manufacture consensus. External retrieval provides the strongest path to falsification for externally checkable claims, but introduces its own failure modes in retrieval coverage, source quality, evidence interpretation, and prompt injection. We synthesize these findings into a verification-independence framework, a deployment-oriented comparison matrix, and a tiered reference architecture that escalates from cheap internal checks to authoritative external evidence according to claim risk. The central conclusion is conditional rather than absolute: AI can catch many of its own hallucinations, but reliability rises sharply when verification is designed as an evidence system rather than another act of generation.

---

## uid: `doi:10.2139/ssrn.7288377`

- title: CrashFactory: From Crash Databases to Scalable Safety-Critical Data Synthesis for End-to-End Autonomous Driving
- authors: Haowei Li, Jiawei Wang, Haowei Sun, Xintao Yan, Henry  X. Liu
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7288377
- keyword hits: agentic, foundation model, llm

### abstract

Official traffic crash databases document decades of real-world safety-critical events. However, they remain largely unused for autonomous vehicle (AV) safety evaluation due to heterogeneous data formats, multimodal representations, and the absence of sensor-level observations. Existing crash reconstruction methods are mostly tailored to one single database, operate at the trajectory level, or model only the involved vehicles. We propose CrashFactory, a fully automated and agentic framework that converts heterogeneous crash records into executable simulation scenarios with behavioral and sensor-level realism. Each report from crash databases is normalized into a unified grounded evidence package. Then, an LLM/VLM-based multi-agent orchestration system is designed to generate semantically consistent scene descriptions and plausible pre-crash trajectories for both crash-involved participants and surrounding traffic. Such trajectories are further refined by guided behavior diffusion models into crash-consistent yet reactive dynamics, and a driving video foundation model is leveraged to render synchronized surround-view videos. On a balanced 100-case Michigan Traffic Crash Facts benchmark, CrashFactory attains a 100% collision realization rate and 98.0% collision-type consistency, with sub-meter displacement error where roadside ground truth is available. Cross-database generalization is verified on 50 NHTSA CISS cases. CrashFactory establishes a scalable pathway to bridge official crash databases into a reusable corner-case resource for E2E AV testing.

---

## uid: `doi:10.2139/ssrn.7288398`

- title: Transfer Learning in Spatiotemporal Graph Neural Networks for Traffic Forecasting: Taxonomy, Analysis, and Future Directions
- authors: Soban Nasir Lone, Mohamed Abouelela, Taeyoung Yu, Jiwon Kim, Constantinos Antoniou
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7288398
- keyword hits: fine-tuning, foundation model

### abstract

Accurate traffic forecasting underpins many intelligent transportation system applications. Graph neural network (GNN)-based spatiotemporal models have become a dominant paradigm by capturing spatial dependencies among sensors and the temporal dynamics of traffic flow. However, these models depend heavily on large volumes of high-quality sensor data, limiting their applicability in data-scarce regions. Transfer learning addresses this limitation directly by reusing knowledge learned from data-rich source networks to improve forecasting performance in target networks with limited data. Building on this premise, this survey reviews 50 transfer learning methods for GNN-based traffic forecasting published between 2020 and 2026, organising them into a unified taxonomy of five methodological families - relational and inductive transfer, domain adaptation, pre-training and fine-tuning, meta-learning, and federated transfer learning - classified by their primary mechanism of knowledge transfer. Our analysis reveals substantial methodological convergence around PeMS and METR-LA benchmarks (60.6% of dataset instances), GRU-based temporal modelling (38.0%), and adaptive graph learning (34.0%), alongside critical gaps: zero-shot transfer is addressed by only 8.0% of studies, just 20.0% incorporate external contextual features, and only 42.0% of methods provide open-source implementations. We identify six future research directions, including spatiotemporal foundation models, integration of continual learning with cross-city transfer, and efficient deployment architectures for operational systems. Alongside a small number of related reviews, this survey is distinguished by three features: a taxonomy organised by the primary mechanism of knowledge transfer rather than by application setting, coverage extending through the rapid 2024-2026 growth of the field, and an explicit mapping from each methodological family to the assumptions it makes about the source-target relationship and the conditions under which it succeeds or fails. It is complemented by an accompanying GitHub repository that tracks recent papers, code, and datasets in this domain.

---

## uid: `arxiv:2608.15109v1`

- title: Constraint-Aware Synthetic Tabular Data Generation via Inter-Column Constraint Discovery with LLM Agents
- authors: Jianxing Zhao, Mao Guan, Dongyu Liu
- affiliations: not stated
- posted: 2026-08-15
- source: arXiv
- link: https://arxiv.org/abs/2608.15109v1
- keyword hits: llm, prompting

### abstract

Generating structurally valid synthetic tabular data remains difficult: outputs with high statistical fidelity and downstream utility can still violate semantically meaningful domain constraints. We study the discovery and enforcement of three complementary inter-column constraint families---equations, linear inequalities, and logical dependencies. Our unified tool-grounded workflow represents all three as machine-executable hypotheses and applies a common interface for full-table validation, deterministic diagnosis, and counterexample-guided revision. A generator-agnostic postprocessor coordinates family-specific repairs on outputs from unchanged tabular generators. Across curated behavioral audits and end-to-end evaluations, the complete workflow improves held-out violation detection over one-shot direct prompting, while postprocessing yields zero measured violations for every retained, applicable constraint, improves downstream utility on most datasets, and largely preserves univariate marginals.

---
