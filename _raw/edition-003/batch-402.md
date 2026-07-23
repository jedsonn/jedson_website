# Classification batch 402 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-402.answer.json` as a JSON array.

---

## uid: `arxiv:2606.28670v1`

- title: MACROCAST: A Vintage-Consistent Time Series Foundation Model for Real-Time Macroeconomic Forecasting
- authors: Andrea Carriero, Davide Pettenuzzo, Shubhranshu Shekhar
- affiliations: not stated
- posted: 2026-06-27
- source: arXiv
- link: https://arxiv.org/abs/2606.28670v1
- keyword hits: fine-tuning, foundation model

### abstract

We introduce MACROCAST, a lightweight Time Series Foundation Model (TSFM) for real-time macroeconomic forecasting. Existing TSFMs suffer from data leakage in two forms: temporal contamination, as the model may have seen the realized values of the series it forecasts, and revision bias, as training on fully revised data diverges from the preliminary, vintage-specific releases available to real-time forecasters. MACROCAST is, to our knowledge, the first TSFM that rules out both forms of leakage entirely: at no stage of training is the model exposed to information that would not have been available to a forecaster in real time. We train MACROCAST first on purely synthetic time series in approximately one GPU-day and then fine-tune it on synthetic time series drawn from Bayesian VARs, dynamic factor models, and ARIMA specifications estimated on vintage-specific ALFRED data. Because pretraining uses only simulated data and fine-tuning uses only real-time vintages, no observed future or revised value ever enters the model; each fine-tuning run takes nine minutes. Evaluated on the FRED-MD database in a genuine real-time out-of-sample exercise, MACROCAST improves on the AR(1) benchmark for roughly 80% of series-horizon pairs, matches or surpasses Chronos-2 -- the strongest currently available TSFM -- and outperforms the Bayesian VAR and dynamic factor model benchmarks, all in a data-leakage-free manner.

---

## uid: `arxiv:2606.29600v1`

- title: One Scene, Two Depths: Probing Geometric Ambiguity in Monocular Foundation Models
- authors: Xiaohao Xu, Feng Xue, Xiang Li, Haowei Li, Shusheng Yang, Tianyi Zhang, Matthew Johnson-Roberson, Xiaonan Huang
- affiliations: not stated
- posted: 2026-06-28
- source: arXiv
- link: https://arxiv.org/abs/2606.29600v1
- keyword hits: foundation model, prompting

### abstract

A faithful 3D world representation should account for layered geometry, where a single camera ray may contain multiple visible and geometrically valid surfaces. Monocular depth estimation, however, reduces this structure to one scalar depth per pixel. Transparent scenes make this ambiguity measurable: the same ray can pass through foreground glass and observe the background, turning the supervised target into a convention of annotation, data, and training rather than a scene-intrinsic truth. A learned predictor exposes this convention as its depth-layer preference. We introduce MultiDepth-3k (MD-3k), a sparse two-layer ordinal benchmark for measuring depth-layer preference and multi-layer spatial relationship accuracy (ML-SRA). On MD-3k, leading depth foundation models exhibit diverse layer preferences under standard RGB input, showing that the same layered geometry can be resolved differently across models. We further find that Laplacian Visual Prompting (LVP), a training-free spectral input transformation, can substantially change the reported layer for certain frozen models. The strongest RGB/LVP pair, DAv2-L, reaches 75.5% ML-SRA. These results suggest that depth foundation models may express complementary geometric hypotheses that standard RGB inference leaves unexpressed. We invite the community to rethink depth supervision and evaluation through an ambiguity-aware lens, where multiple valid 3D interpretations are treated as geometric structure to be measured, preserved, and expressed.

---

## uid: `doi:10.2139/ssrn.7022853`

- title: Order-Aware and Speed-Disentangled Subspace Learning for Cross-Speed Bearing Misalignment Diagnosis
- authors: Jing Wang, Ming Yang, Ganlu Gao, Xinmei Zhang
- affiliations: not stated
- posted: 2026-06-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7022853
- keyword hits: fine-tuning

### abstract

Servo-motor bearing-misalignment diagnosis from drive-internal current signals is hard: features drift with rotational speed, the reshape-and-render image keeps only magnitude (discarding the misalignment-signaling phase coupling), and the representation entangles speed and fault factors. We reframe the task as disentangling a speed-invariant diagnostic subspace from a speed-redundant nuisance subspace, via four choices: (i) an order-aware image conversion that fixes misalignment harmonics to speed-invariant columns; (ii) an order-coherent phase-coupling (OPC) descriptor, an order-domain bicoherence absent from the magnitude image; (iii) a learned subspace projection with an orthogonality-and-speed-adversarial decomposition into a diagnostic z_f and a speed-redundant z_p; and (iv) an attributed ELAN/Inception backbone. On a 400 W servo bench (Q/D currents and speed; nine classes; 500/1000/1500 r/min), OASP-Net reaches 98.7/96.4/93.1% accuracy under a trial-independent split - 8.5-9.1 pp above IC+CNN and 3.8-5.5 pp above the strongest baseline MSSE+CCA. Under zero-fine-tuning cross-speed transfer it retains at least 92.9% of same-speed accuracy across six shifts, and leave-one-speed-out decomposition adds 2.9 pp on held-out speeds. A class-conditioned MMD of 0.06 on z_f (versus 0.41 on the raw input image) and a speed probe at 34.8% on z_f versus 95.8% on z_p confirm disentanglement. We also flag two non-improvements: lowest-severity classes at 1500 r/min, and a learned-vs-random-Phi same-speed tie that pays off only across speeds.

---

## uid: `arxiv:2606.30986v1`

- title: The Organizational Behavior of Agentic AI: Collective Intelligence in Human-Agent Workflows
- authors: Canhui Liu
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.30986v1
- keyword hits: agentic, llm

### abstract

Agentic artificial intelligence is increasingly deployed not as a single assistant but as a collective of planners, solvers, reviewers, memory managers, tool users, and orchestrators. These systems are entering organisational workflows under familiar labels such as teams, managers, committees, markets, and workflows. This article asks whether such agent collectives exhibit organisational behaviour in a sense that is analytically comparable to, yet distinct from, human organisational behaviour. I argue that agentic AI is a partial organisational analogue. It resembles a human organisation because it differentiates work, coordinates interdependence, performs recurrent routines, crosses boundaries, and produces collective outcomes. It differs because these patterns are not sustained by motivation, identity, trust, employment, socialisation, or moral accountability. They are sustained by context architecture: prompts, memory, traces, schemas, tools, validators, and permissions. The article develops contextual transaction cost as the central mechanism linking these similarities and differences. Computational theorising, synthetic task simulations, real LLM agent traces, and robustness analyses show that human-imitation forms often underperform when they add lossy handoffs, correlated deliberation, and verification burdens, whereas shared-state and adaptive forms perform better when they make context durable, inspectable, and task-contingent. The article contributes to organisation studies by theorising agentic AI as an emerging object of organising and by specifying the interface conditions under which human and agentic organisational behaviour can jointly support collective intelligence.

---

## uid: `arxiv:2606.30473v1`

- title: Field Order Should Not Matter: Permutation-Invariant Embedding Model Fine-Tuning for Structured Metadata Retrieval
- authors: Aivin V. Solatorio, Olivier Dupriez, Rafael Macalaba
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.30473v1
- keyword hits: fine-tuning, llm

### abstract

We study retrieval over catalogs of structured metadata, where each record is a small schema whose fields answer different kinds of query. Embedding a record with a text encoder first serializes its fields into a string, which forces a choice of field order. We show this choice, usually treated as an implementation detail, silently controls retrieval quality once the encoder is fine-tuned. A standard fine-tune loses 7.4 nDCG@10 points when the index is rebuilt under a different field order, because it reads absolute position instead of the field labels. We propose permutation-invariant fine-tuning ($\textbf{PI-FT}$), which serializes each record under a freshly sampled field order with random field dropout, so meaning binds to the labels rather than to position. The change is about two lines in the data loader; it costs negligible in-distribution accuracy and cuts the order-change penalty to 0.2 points. We study this in the discovery of development statistics, a catalog of nearly 10,000 indicators that should be searchable in many languages by a model small enough to self-host. As AI assistants and agents increasingly mediate access to public data and statistics, this retrieval step decides whether an answer is grounded in the right indicator or series, making discoverability a precondition for disseminating data through AI. Because usage logs cannot provide training signal for indicators no one has searched, we generate the queries instead. $\textbf{DevDataBench}$ is a fully LLM-generated benchmark of grounded, facet-targeted queries across 15 languages, covering every indicator for both training and evaluation. A fine-tuned 118M-parameter CPU encoder outperforms every zero-shot baseline, including $\texttt{text-embedding-3-large}$ (0.707 vs.\ 0.556 nDCG@10), with the largest gains in low-resource languages. We release the benchmark, pipeline, models, and a reusable PI-FT framework.

---

## uid: `arxiv:2606.30970v2`

- title: Behavioral Governance for Autonomous AI Agents: The AgentBound Framework
- authors: Anuj Kaul, Qianlong Lan, Pranay Gupta
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.30970v2
- keyword hits: ai agent

### abstract

Autonomous AI agents increasingly perform consequential actions on behalf of human principals, including financial transactions, external communications, and enterprise workflows. Existing agent infrastructure relies on identity federation and delegated authorization to authenticate workloads and control resource access, but it cannot determine whether an authorized action should be executed under the current behavioral and operational context. We present AgentBound, a runtime governance framework that provides verifiable behavioral oversight for autonomous AI agents. AgentBound evaluates each proposed action using three independent authorities: delegated authorization, owner-signed behavioral constitutions, and site action contracts. Their judgments are conservatively composed through a formal decision model to determine whether an action should be permitted, reviewed, or denied before execution. To provide accountability, AgentBound generates cryptographically verifiable governance receipts that bind every action to the exact delegation, policy, and semantic artifacts governing the decision, enabling independent replay verification and policy provenance. The framework also introduces standing delegation for long-running agents, allowing periodic workloads to operate under continuously refreshed governance policies while preserving revocability and bounded authority. We present the formal foundation, system architecture, governance receipt protocol, and AgentBound-Bench, a benchmark framework for evaluating governance correctness, authority composition, and accountability. Rather than replacing model alignment, AgentBound complements it by providing a deterministic governance layer between authorization and execution, transforming governance from a process that must be trusted into one that can be independently verified.

---

## uid: `arxiv:2606.30344v1`

- title: Early Cue Precision Shapes Visual Shortcut Learning in Controlled Cue-Manipulation Benchmarks
- authors: Chanho Park, Woochan Lee, Janyeong Oh, Geongho Gong, Minshu Kim, Yeachan Kwak, Seongim Choi
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.30344v1
- keyword hits: fine-tuning

### abstract

Visual classifiers can achieve high matched-distribution accuracy while relying on low-level cues that fail under conflict or suppression. We test whether this failure is shaped by early cue precision: the reliability with which a low-level cue predicts the label during early learning or downstream probe fitting. Across synthetic shape-texture tasks, sequential digit training, a 10-class frozen-representation audit, and a CIFAR-10 natural-image-based texture-overlay benchmark, we manipulate object-texture match probability and evaluate matched-ID accuracy, conflict accuracy, texture-choice rate, and suppression behavior. Degraded-but-predictive input does not substitute for cue decorrelation. In 10-class digit probes, conflict accuracy drops from 0.589 under chance-like cue precision to 0.005 under target-perfect texture. In CIFAR-10 frozen probes, conflict accuracy drops from 0.569 to 0.114, while texture choice rises from 0.049 to 0.855; this ordering persists across texture-overlay strengths alpha in {0.15,0.25,0.35,0.50}. End-to-end CIFAR-10 training shows that low early cue precision improves pre-target conflict behavior, but shortcut-rich fine-tuning can rapidly overwrite this benefit. Cue decorrelation must therefore be maintained during downstream adaptation rather than treated as a one-time inoculation.

---

## uid: `arxiv:2606.29727v1`

- title: DeepTrans Studio: Turning Expert Interventions into Shared Team Knowledge in Agentic Translation Workflows
- authors: Ziyang Lian, Qingya Zhang, Hao Wang, Huiwen Xiong, Qi Yang, Lingyi Meng, Xiaoyi Gu, Rui Wang
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.29727v1
- keyword hits: agentic, llm

### abstract

Professional translation is often a team-based process: translators, reviewers, and project managers must coordinate terminology, legal force, and accountability across documents. Yet many LLM-based translation tools treat human corrections as isolated edits. Expert decisions made in one segment or by one member are rarely captured as reusable knowledge for the rest of the team. We present DeepTrans Studio, a collaborative translation workspace that lets professionals intercept selected nodes in an agentic translation workflow, review evidence, revise AI outputs, and save approved decisions to a shared team memory. During the demo, attendees will role-play translators and reviewers, resolve preset terminology and legal-modal risks, and see how their decisions are propagated to downstream segments and surfaced in a teammate's workspace as reusable precedents. The demo illustrates how human interventions in AI-mediated work can become shared, traceable knowledge rather than one-off corrections.

---
