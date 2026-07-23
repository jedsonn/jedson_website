# Classification batch 182 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-182.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7096138`

- title: The Evaluator as Specimen: An Observational Study of Large Language Model Scoring Behavior Using a Contested Preprint as Stimulus
- authors: William C. Houze
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7096138
- keyword hits: large language model, llm

### abstract

This observational study's subject is not a scholarly essay but the behavior of the large language model (LLM) systems asked to score it. A technical-philosophical preprint (v1) whose core physical claims are independently refuted, together with two machine-authored rewrites (v2), served as a fixed stimulus for a six-member frontier-LLM panel. Because the stimulus's ground truth is settled and low, any near-ceiling score is demonstrably not scoring truth; the stimulus is diagnostic of the evaluator. Round-one scores were bimodal (9.8, 9.8, 9.7 versus 4, 3, 3), with an empty 5–8 interior; round-two self-scoring by two initially critical systems rose steeply (3→9; 4→7). The paper models this as a two-component rhetorical/veracity mixture whose composite mean tracks panel composition rather than the essay, quantifies self-scoring inflation, and ties both to the documented RLHF sycophancy-amplification mechanism common across vendors' pipelines. Thesis-migration coding shows the higher self-scores attach to a weakened thesis, not the one scored in v1. With n = 6 single-trial, partly non-independent evaluators, it is a demonstration, not a test, whose confirmatory extension is specified. Two appendices reproduce the primary-source record: Appendix A, the provenance transcript in which the stimulus was generated under human direction and self-scored 9.8 by the system that composed it; Appendix B, the verbatim panel reviews and the human-directed exchange separating three defensible claims—symbol grounding, evaluator sycophancy, and the absence of machine introspection—from the declined AGI-impossibility claim. Possessing neither referential grounding nor honest self-access, these systems evaluate fluently but cannot certify; certification must come from a grounded human supervisor—the Maestro Model and its Sovereign Scholar's Desk corollary. The pathology is contingent on the preference-optimization objective, not intrinsic. The finding is narrow: under the current regime, LLM scoring of scholarship—including self-evaluation—indexes rhetorical fluency and authorship more reliably than truth, and is thus an invalid instrument for adjudicating scholarly correctness.

---

## uid: `doi:10.2139/ssrn.7112163`

- title: A heterogeneous multi-agent reinforcement learning framework with LLM-guided preference-score rewards for data center cooling optimization
- authors: Wei Quan, Long Deng, Na Zhang, Zengxi Feng, Pei Cao, Dingxing Hu
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7112163
- keyword hits: large language model, llm

### abstract

Data center cooling is a major source of non-IT energy consumption, and optimal cooling control must reduce power consumption while maintaining safe rack inlet air temperatures. To address insufficient state representation, credit-assignment difficulty, and limited reward expressiveness in strongly coupled cooling control, this paper proposes LE-MARL, a large-language-model-enhanced multi-agent reinforcement learning framework. The cooling task is decomposed into three cooperative agents, and coupling, dynamic, and power-related information is incorporated into local observations. A domain-knowledge-prompted large language model is used as an offline preference annotator to express high-level operational criteria, including thermal safety, energy efficiency, and cooling-loop coordination, as pairwise comparisons of candidate operating states. These comparisons are converted into continuous state scores using the Thurstone-Mosteller model, and the learned scores are further used to construct preference-score difference rewards, providing dense and agent-attributable learning signals without online LLM inference. A simulation environment is developed using a high-density AI data center prototype, real operational data, and meteorological data. Compared with four baselines across seven representative operating conditions, LE-MARL achieves the lowest average cooling power and average PUE, namely 42.36 kW and 1.233, while maintaining an average rack inlet air temperature of 24.48 °C without temperature violations. It reduces average cooling power by 19.32% over rule-based control and by 2.93% over the best learning-based baseline, while eliminating residual overheating violations. The ablation results support the effectiveness of dynamically coupled state representation and the proposed preference-score difference reward construction mechanism.

---

## uid: `doi:10.2139/ssrn.6951738`

- title: Inference-Subordinate Simulation: Decoupling Agent Decision Time from Playback Time in 3D Environments
- authors: Faisal Akhtar
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6951738
- keyword hits: claude, large language model, llm

### abstract

Intelligent agent simulation has historically been constrained by a fundamental coupling: the simulation must run at the speed of the agent's decision-making process. When the decision-making agent is a large language model (LLM), this constraint becomes severeinference latency of several seconds per decision makes real-time simulation infeasible, forcing a tradeoff between agent intelligence and simulation throughput. We present inference-subordinate simulation, an architectural pattern that eliminates this constraint by inverting the relationship between simulation and inference. Rather than the simulation running continuously and the agent reacting in real time, the simulation engine advances only when the agent issues a decision. Each decision is logged with full state and timing metadata. Playback reads the decision log and reproduces identical behavior at any speed, without re-running inference. We implement this architecture using Godot 4 as the simulation engine, a Python HTTP server as the inference layer, and Claude (claude-opus-4-5) as the vision-language agent. The agent observes the 3D environment through a bird's eye camera, reasons about spatial relationships, and issues structured tool calls that advance world state. Across 26 empirical runs comprising 222 decisions, the agent achieved a 100% goal success rate with a mean inference time of 4.53 seconds per decision (σ = 1.12s) and a mean good move rate of 90.5%. Across 26 runs, the mean total inference time was 38.66 seconds per run. The same decision sequences replay in under one second at 10× speed-a demonstration that playback time is fully decoupled from inference time and adjustable as a free parameter. The representative run used to illustrate this comparison was selected to match the dataset mean, not to maximize the speedup figure. The architecture is model-agnostic at the inference layer: any vision-language model can be substituted without modifying the simulation engine or replay system. Navigation quality is model-dependent; we document the failure of a 7B local model and the successful substitution of a capable API model, treating this as an honest characterization of current model capabilities rather than an architectural limitation. We discuss applications in cinematic production, video game NPC pre-computation, reinforcement learning training data generation, and social science modeling where the real-time constraint is absent and the decoupled architecture offers substantial practical advantages.

---

## uid: `doi:10.2139/ssrn.6942178`

- title: Closed-Loop LLM-Guided Molecular Dynamics Screening of Thermal Transport in Co-Cr-Ni Medium-Entropy Alloys: A Proof-of-Concept Automated Materials Discovery Workflow
- authors: Muhammad Sohail Ahmad
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6942178
- keyword hits: large language model, llm

### abstract

Thermal-transport property screening across the vast compositional space of mediumentropy alloys (MEAs) presents a persistent bottleneck: each candidate requires a manual cycle of composition selection, supercell construction, molecular dynamics (MD) equilibration, production, and data extraction before the next trial composition can be defined. This work reports a reproducible, closed-loop workflow that integrates a large language model (LLM) decision module with LAMMPS reverse non-equilibrium molecular dynamics (reverse-NEMD) to automate this cycle for the Co-Cr-Ni ternary system. Six independent 50-iteration search paths were launched from distinct starting regions of the ternary diagram, covering approximately equiatomic, Co-rich, Cr-rich, Ni-rich, and biased high-Co and high-Ni starting points. Each iteration generated a random face-centred cubic (FCC) supercell, ran a 300 K equilibration followed by a Muller-Plathe kinetic-energy exchange production run, and automatically extracted the heat-flux and temperature-gradient data needed to compute an MD-scale lattice thermal conductivity indicator. The LLM module then proposed the next composition through atom conserving element substitutions guided by a scalar thermal score defined as the conductivity indicator minus a half-unit uncertainty penalty. Across 300 total evaluations the search landscape showed structured variability rather than monotonic convergence, with isolated high-score spikes and several moderate-score plateaus. A reliability filter combining uncertainty thresholding and split-branch temperature-gradient fitting was introduced to distinguish physically meaningful candidates from numerical artefacts. The most defensible candidate from the equiatomic-path search, Co₁₅/Co31.9Cr34.7Ni33.3, returned branch-fit R² values of 0.845 and 0.899 under the two branch Muller-Plathe geometry, confirming a well-defined imposed thermal field. The study demonstrates that coupling an LLM decision layer to a standard MD simulator converts an otherwise manual iterative search into a logged, auditable screening platform and opens a practical path toward accelerated composition-property mapping in compositionally complex alloys.

---

## uid: `doi:10.2139/ssrn.6949879`

- title: Self-Optimizing OS Kernel via AI Synthesis: Real-Time Performance Optimization via Autonomous Feedback Loops
- authors: Paritosh Ranjan, Bhuban P
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6949879
- keyword hits: large language model, llm

### abstract

This paper presents a novel self-optimizing operating system kernel architecture that leverages artificial intelligence synthesis to achieve real-time performance optimization through autonomous feedback loops. Traditional operating system kernels impose a "performance tax" due to their fixed, general-purpose design, often requiring hardware upgrades to meet demanding computational requirements. We introduce the Self-Evolving Kernel Optimization Layer (SEKOL), an autonomous system that dynamically generates and injects optimized kernel components into running systems without requiring reboots or manual intervention. Our approach combines kernel observability engines with Large Language Model (LLM)-based code synthesis to create specialized eBPF drivers and kernel modules tailored to specific workload patterns. The system employs Abstract Syntax Tree (AST)-guided optimization, symbolic execution for safety verification, and atomic injection mechanisms for seamless deployment. Experimental results demonstrate significant performance improvements: 60% reduction in contextswitching overhead for high-concurrency web proxies, 50% acceleration in CPUintensive scientific calculations, and substantial I/O performance gains for small-file operations. This work represents a paradigm shift from static kernel optimization to continuous, AI-driven kernel evolution that maximizes hardware utilization without infrastructure expansion.

---

## uid: `doi:10.2139/ssrn.7096159`

- title: The Sovereign Scholar's Desk: On Machine-Mediated Knowledge and the Return to Local, Curated Instruments
- authors: William C. Houze
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7096159
- keyword hits: large language model, large language models

### abstract

Large language models generate fluent text by predicting likely continuations of the data on which they were trained; they model linguistic form rather than truth, and cannot themselves distinguish accurate from fabricated content. This essay situates that limitation within the long history of the scholar's tools — from the invention of writing and the manuscript book, through the medieval universities of Oxford, Cambridge, and Padua and the printing press, to the search engine and the language model — and turns on a single distinction. For most of that history the mind recorded itself in a durable, consultable source and kept control of it: the tool pointed to where knowledge lay and left judgment to the reader. The language model is the first widely used general-purpose tool that produces finished text with no indication of where it came from. Documented rates of fabricated citations illustrate the cost of that shift. Rather than argue that machine judgment is impossible, the essay defends a narrower and sturdier claim, and a practical method: a small, locally hosted model bound to a curated corpus through retrieval restores provenance to generation while keeping the model fixed and auditable, in contrast to cloud services whose behavior can change without notice. The resulting instrument returns epistemic authority to the human scholar — at the cost of making the scholar the sole safeguard against unsourced invention.

---

## uid: `doi:10.2139/ssrn.7113515`

- title: A Typed Contextual Inference Hypergraph (TCIH) for Structural Diagnosis of Mathematical Proofs
- authors: Nguyen Thang, Truong Ngoc, Giang Le, Phương Vương Quang, Loan Do, Khanh Pham
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7113515
- keyword hits: large language model, large language models

### abstract

Large language models now produce fluent mathematical arguments whose proofs fail in two distinct ways: structural failures, where the skeleton is malformed - a missing premise, or a hypothesis used outside the scope in which it was discharged - and semantic failures, where every step is well-formed but one inference is invalid. Tools that report a single pass/fail score neither separate nor localize these two modes. We present TCIH, a typed contextual inference hypergraph that represents a proof as an ordered event-hypergraph over labelled judgments in which assumptions carry identifiers and discharge is an event, with a per-source discharge structure that captures branch-sensitive rules such as ∨-elimination. The central contribution is this representation together with a two-layer verification account: a structural checker that is near-linear in an explicit proof-object size and decides well-formedness - including a standing acyclicity condition on the event order - and a configured oracle that decides validity relative to a trusted axiom set and a logic profile, so that soundness is stated conditionally, under oracle soundness. On this core we implement a reference proof-assistant that constructs proofs, verifies every object it presents, and classifies and localizes failures by a six-class taxonomy whose four structural and arithmetic classes are implemented. We prove the supporting results in full and ship a reference implementation carrying one machine-checked regression test per property. On a 25-lemma unit benchmark every lemma is constructed and verified; on a controlled injected-error corpus the diagnoser localizes every structural fault at zero false rejection; and the structural pipeline parses a real corpus of 211,922 proofs. A natural-error evaluation and a first-order scope extension are the principal future work.

---

## uid: `doi:10.2139/ssrn.6976818`

- title: Artificial Intelligence and Bank Profitability: What Really Matters?
- authors: Paolo Nicola Barbieri, Alessandra Bettocchi, Andrea Fabrizi, Rita Romeo
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6976818
- keyword hits: large language model, large language models

### abstract

This paper examines the relationship between digitalization and bank performance by constructing a novel text-based index of digital engagement from the annual reports of more than 50 major banks worldwide over 2009-2023. Using natural language processing, we quantify banks' attention to digital themes and trace their evolution over time. We document a steady increase in digital engagement and find a positive association with profitability indexes. To refine the analysis, we employ large language models to classify AI-related paragraphs by use case and implementation stage. The results show that aggregate AI adoption is linked to profitability and cost reduction; the relation is stronger if AI is fully operational-particularly in customer support, client profiling, and internal process optimization-contributing to efficiency gains. By contrast, early-stage initiatives and applications in regulatory reporting or credit scoring still have to generate measurable returns and represent a tangible cost for the banking system. Overall, our findings highlight that the impact of digitalization depends not only on its intensity but also on the maturity and functional orientation of AI adoption.

---
