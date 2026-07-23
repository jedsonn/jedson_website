# Classification batch 352 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-352.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7008939`

- title: Compressing Science: A Survey of Compression and Compactification Techniques for Scientific Foundation Models
- authors: Thomas Wang
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7008939
- keyword hits: foundation model

### abstract

Foundation models are reshaping the natural sciences: transformer-scale networks pre-trained on protein sequences, single-cell transcriptomes, genomic DNA, atmospheric states, and inter-atomic potentials now match or exceed bespoke pipelines across structural biology, genomics, weather forecasting, and materials discovery. Yet the same scale that grants these scientific foundation models (SFMs) their generality makes them expensive to train, costly to serve, awkward to deploy at the bench or on the edge, and difficult to interpret. This review synthesises two literatures that have so far evolved largely in parallel: the mature toolbox of neural network compression-pruning, quantization, knowledge distillation, and low-rank adaptation-and the rapidly maturing family of SFMs. We organise compression methods into a taxonomy, survey their (still nascent) application to scientific models, and argue that SFMs raise compression questions that text-and-vision models do not: faithfulness to physical and biological invariants, preservation of uncertainty calibration for downstream scientific decisions, and the relationship between a model's redundancy and the low-dimensional manifolds its representations are known to occupy. We connect compression to scaling-law analyses that quantify how much capacity an SFM actually needs, and to mechanistic findings that performant, compact algorithms can be extracted directly from the internals of large biological models rather than trained from scratch. We close with open problems-hardware-aware co-design, compression-aware pre-training, evaluation beyond perplexity, and "compactification" as a route to interpretable, distributable scientific AI.

---

## uid: `doi:10.2139/ssrn.7010858`

- title: Do Focal Entities Coordinate their Industries? An Empirical Falsification Study
- authors: Leo Lee
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7010858
- keyword hits: deepseek

### abstract

A companion paper to Price as a Construct of Time advances two empirically load-bearing claims: that "boundary entities" exert asymmetric synchronization spillovers on other firms in their industry, and that such entities occupy an intermediate position in tangible/intangible balance-sheet space rather than the pure-intangible corner. We subject both claims to a falsification standard: an effect counts only if it survives the benchmarks a sophisticated desk already owns. These refer to large-cap-leads-small-cap lead-lag, sector beta, a common "AI factor," liquidity, and documented economic-link return predictability. Using NVIDIA, Tesla and Meta as candidate boundary entities and the January 27, 2025 DeepSeek episode together with the April 2025 H20 export-control charge as the two cleanest natural experiments, we find: (i) focal→ecosystem repricing is real and directionally asymmetric, but its channels are individually identical to pre-existing mechanical anomalies, and it does not separate from size plus a common AI factor in a single correlated episode; (ii) all three candidate entities are genuinely intermediate in composition. Each retains a non-trivial tangible anchor unlike a pure software firm yet a focality composite is so collinear with log market capitalization and AI-membership that "boundary status" is, on present evidence, largely size relabeled. The headline result is negative, and we report it as the finding: the boundary construct is descriptively valid and analytically useful for risk, but is not a standalone source of alpha. We distinguish a falsifiable residual, a shock taxonomy separating narrative-reabsorbable from tangible-constraint events, that does survive.

---

## uid: `doi:10.2139/ssrn.7149764`

- title: Adapting Single-modal EEG Foundation Models to Multimodal Affective Computing via Spectral Cross-modal Prompting
- authors: MeiYan Xu, ChuanCheng Lin, Chenyu Liu, Xun Zhang, Xinliang Zhou, Peiliang Gong, Ziyu Jia, Yijie Pan
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7149764
- keyword hits: fine-tuning, foundation model, prompting

### abstract

Despite the remarkable success of foundation models in single-modal EEG analysis, their extension to multimodal affective tasks remains constrained by pervasive modality gaps and the prohibitive computational overhead of conventional fine-tuning. This paper presents Frequency-domain Informed Prompt Tuning (FIPT), a parameter-efficient framework designed to adapt pre-trained EEG backbones (e.g., LaBraM, CBraMod) to multimodal emotion recognition. By freezing the backbone's core weights, we introduce a Spectral-Rhythmic Alignment Module (SRAM) that synchronizes heterogeneous physiological signals in a unified frequency space, effectively mitigating cross-modal discrepancies. To further bridge the representation gap, we employ a Knowledge-Augmented Hybrid Prompting strategy, which injects Power Spectral Density (PSD) priors to anchor the model’s attention on biologically significant oscillatory features.Extensive evaluations on four diverse public datasets demonstrate that FIPT consistently achieves state-of-the-art performance. Our sensitivity analysis reveals that the framework effectively leverages spectral priors for guided adaptation, providing a robust, interpretable, and scalable paradigm for multimodal affective computing.

---

## uid: `doi:10.2139/ssrn.7011520`

- title: Emotion as System: A Foundational Architecture for Affect, Meaning, Perception, and Action
- authors: Brendon Hawkins
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7011520
- keyword hits: large language model, large language models

### abstract

Affective computing has historically focused on systems that recognize, express, respond to, or influence emotion. This paper extends that lineage by proposing a foundational systems architecture for describing emotion as structural behavior, operable at individual, collective, and computational scales. Within this architecture, affect operates as an energetic substrate. Emotion configures a global field of sensitivity and responsiveness. Meaning introduces mass that deforms the field. Perception traces trajectories through it. Action follows gradients shaped by its geometry. Field, mass, trajectory, and gradient form a structural vocabulary intended to be operationalized computationally, tested empirically, and extended through design — work the paper frames as openings rather than results. Recent interpretability work on large language models recovers the same primary axes of valence and arousal, and the same clustered geometry, that organize human affective experience. This provides convergent evidence that emotion has computable structure. The contribution here is architectural: it supplies a system definition that makes emotion available as an object of formal reasoning across affective science, affective computing, design, and AI systems.

---

## uid: `doi:10.2139/ssrn.7123186`

- title: Operating Model Lab: OrgSpec-as-Code Discrete-Event Simulation for Operating-Model Design
- authors: Amit Batra
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7123186
- keyword hits: llm

### abstract

Operating-model decisions-how to split work across teams, regions and time zones, and where to insert automation-are typically made on judgment, static spreadsheets, and averages. Averages hide the queueing behaviour that actually determines whether service levels hold under month-end peaks, quality shocks and regional outages. This paper introduces Operating Model Lab, an open, code-based framework that lets an operating model be written as version-controlled configuration, simulated by a deterministic discrete-event engine run as a seeded Monte-Carlo experiment, and compared across structural variants on a single interactive dashboard. The framework's distinguishing feature is a governance separation: a large-language-model (LLM) copilot designs, critiques and narrates but never computes, while an independent calculation-QA layer re-derives every headline number by a second method (flow conservation, capacity algebra, queueing monotonicity, and held-out surrogate validation) and holds veto power over publication. On a fully fictional three-region worked example, the framework shows that no candidate structure clears a 90 percent service-level floor at baseline settings, identifies the specific lever combinations that do, and prints the cost of each-a result that a spreadsheet built on averages would have missed. We describe the modelling language, the engine, the validation regime, and the limitations, and release the full system as open source so that results are reproducible and independently checkable.

---

## uid: `doi:10.2139/ssrn.7005899`

- title: Exploring the Intersection of AI, Language, and Law: A Bibliometric Analysis
- authors: Zihang Lan, Xu Zhang
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7005899
- keyword hits: llm, llms

### abstract

This study investigates the interdisciplinary nexus of AI, language, and law through a comprehensive bibliometric analysis of 610 peer-reviewed publications sourced from Web of Science and Scopus (2001-2024). Utilizing VOSviewer, CiteSpace, and R bibliometrix, we map intellectual structures, collaboration networks, and thematic trajectories in this emerging field. Results reveal three developmental phases, an incubation period (2001-2013) dominated by symbolic systems, an emergence phase (2014-2018) with increasing cross-domain integration, and a maturation phase (2019-2024) marked by the mainstream adoption of LLMs in legal applications, yet the domain remains fragmented with limited co-citation coherence and underdeveloped interdisciplinary synthesis. Keyword co-occurrence and citation burst analyses indicate evolving focal points from traditional NLP to explainable AI and forensic linguistics, with ethical concerns and semantic complexity emerging as critical bottlenecks. This study contributes a systematic framework for understanding the epistemological, methodological, and geopolitical contours of AI-language-law scholarship and offers strategic directions for fostering integrated, inclusive, and transparent legal-AI systems.

---

## uid: `doi:10.2139/ssrn.7149238`

- title: From Classical Phishing to Neurophishing: A Cognitive-Technical Frameworkfor Adaptive Manipulation and Human-Centric Security
- authors: Denir  Valencio de Campos, MANUEL  PAMBASANGE JORGE, ANA  PATRÍCIA CORREIA GOMES, Jorge Sa Silva
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7149238
- keyword hits: generative artificial intelligence

### abstract

Phishing has evolved from static, rule-based deception into a dynamic form of cognitive manipulation that exploits emotional cues, attentional shifts, and subtle behavioral patterns. Advances in generative Artificial Intelligence, psychometric profiling, biometric sensing, and immersive augmented and virtual reality environments now enable adversaries to adapt their tactics in real time, responding to fluctuations in cognitive load, emotional arousal, and interaction behavior. This emerging class of threats, termed neurophishing, departs from traditional phishing by leveraging continuous feedback loops to influence perception, judgment, and decision-making. Drawing on cybersecurity, cognitive psychology, behavioral science, and neurotechnology, this article traces the progression from classical social engineering to phishing and ultimately to neurophishing. We outline a taxonomy of attack modalities, examine the cognitive mechanisms underlying susceptibility, and analyze the sociotechnical implications of adaptive cognitive interference. Finally, we propose a multilayered defense model that integrates cognitive governance, emotional literacy, defensive biometrics, anomaly detection, and human-centric security principles to safeguard cognitive autonomy in increasingly immersive and AI-mediated environments.

---

## uid: `doi:10.2139/ssrn.7014258`

- title: The Cybersecurity Consequences of AI Strategy: How Automation-orientation and Augmentation-orientation Shape Data Breach Risk
- authors: Santhosh Srinivas, Leting Zhang, Kevin Hong
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7014258
- keyword hits: llm

### abstract

Artificial intelligence (AI) has become a strategic cornerstone of organizational transformation, offering the potential to enhance cybersecurity while introducing new risks. Yet the cybersecurity implications of AI adoption remain poorly understood empirically. We argue that security outcomes depend not only on whether firms use AI, but also on the strategic orientation firms take toward AI deployment. Drawing on organizational control theory, we develop a framework theorizing how AI Automation Strategy and AI Augmentation Strategy shape two organizational control capabilities, visibility and intervenability, with consequences for breach risk. Using LLM-assisted classification of large-scale job-posting data linked to data breach records for 3,006 U.S. public firms from 2018 to 2024, we find that AI Automation Strategy is associated with higher breach risk while AI Augmentation Strategy is associated with lower breach risk. These findings remain consistent across panel fixed-effects models, difference-indifferences analyses, Oster bounds, falsification tests, and alternative model specifications. Mechanism evidence shows that automation operates by eroding visibility of AI-mediated workflows and downstream operations, reflected in longer breach detection latency, while augmentation operates by improving both visibility and intervenability, reflected in shorter breach detection and containment latency. We further find that these associations respond to different organizational levers: AI Integration Depth attenuates automation's riskamplifying association, whereas AI Governance strengthens augmentation's protective association, an asymmetry suggesting that the effectiveness of organizational safeguards depends on the AI strategy in play. The cybersecurity consequences of AI thus depend critically on how AI is assigned to organizational work, embedded in firm operations, and governed through organizational oversight.

---
