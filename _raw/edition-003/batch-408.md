# Classification batch 408 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-408.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7075247`

- title: A Field-Scale AI Surrogate: Graph Network Simulator for Soil Moisture Prediction
- authors: Tamima Rashid, Balasubramaniam Natarajan
- affiliations: not stated
- posted: 2026-07-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7075247
- keyword hits: fine-tuning

### abstract

Accurate field-scale volumetric water content (VWC) prediction is essential for precision irrigation management. However, Richards-equation solvers such as HYDRUS-1D provide vertical 1D flow within a single soil column and do not represent spatial distribution across a field. In this paper, we demonstrate the feasibility of an AI surrogate simulator to obtain field-scale VWC estimates. Specifically, we use a process-based hydrology model as a physics engine to generate synthetic training data (here HYDRUS-1D, though the framework is agnostic to the choice of simulator), and we propose and train a Graph Network Simulator (GNS) on these simulations, evaluating it zero-shot against real sensor records, at two independently instrumented agricultural sites with contrasting climates, crops, and soils: Cook Agronomy Farm in Pullman, Washington (semi-arid Pacific Northwest, multi-crop rotation, silt loam, strong topographic gradient) and the ARDEC research farm in Fort Collins, Colorado (high-plains irrigated corn, sandy clay loam, flat terrain). With no real-sensor supervision, the GNS lowers MAE relative to HYDRUS-1D at both sites (a 20% reduction at 30 cm at Cook Agronomy Farm, and an improvement at all five measured depths, 9% on average, at ARDEC), showing that field-scale lateral message passing recovers spatial structure absent from 1D simulation. The learned soil physics representations generalise across sites. A model trained at one site transfers to the other with only partial fine-tuning, and a single model jointly trained on both sites serves each. Among adaptations on observed data, multi-step unrolled fine-tuning on in-situ sensors is the only strategy that improves rollouts, whereas coarse-resolution satellite soil moisture measurement does not; the remaining accuracy ceiling is HYDRUS-1D's own structural bias at depth, independent of graph design.

---

## uid: `doi:10.2139/ssrn.7075425`

- title: Agentic Aggregation for Electric Bus Depot Coordination: Operational Trade-Offs, Contextual Pricing, and Deployment Implications
- authors: Ali Eslami, Jônatas  Augusto Manzolli, Luis F. Miranda-Moreno, Jiangbo Yu
- affiliations: not stated
- posted: 2026-07-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7075425
- keyword hits: agentic

### abstract

Agentic systems are changing how complex operational tasks are coordinated by connecting heterogeneous data sources, introducing a new paradigm for simplifying tasks, connecting datasets, and automating processes. Electric bus fleets provide a relevant test case for this paradigm. Their operation requires continuous coordination between service reliability, battery state-of-charge, charger availability, electricity prices, route-energy uncertainty, and vehicle-to-grid (V2G) opportunities. This paper proposes an agentic aggregator framework that streamlines this decision environment by coupling an optimization-based electric bus scheduling model with supervisory agents for disturbance detection, tariff adaptation, and schedule evaluation. The optimization core enforces physical feasibility across routes, chargers, batteries, and V2G exchanges, while the agentic layer interprets changing operating conditions, triggers real-time re-optimization when needed, and defines how flexibility value is allocated between the aggregator and the public transport operator (PTO). A realistic depot case study evaluates day-ahead and real-time operations under profit-based and operation-based coordination modes, considering service delays, route-energy deviations, electricity price shocks, and combined disturbances. The results show that agentic aggregation can support adaptive fleet-grid coordination by maintaining feasible schedules, activating re-optimization selectively, and improving the use of charging and V2G flexibility. However, they also reveal a critical trade-off: the same agentic capability that reduces operational complexity can extract value from the PTO when configured around profit-oriented pricing. These findings suggest that agentic aggregators can become useful tools for managing electric bus V2G operations, but their deployment in public-fleet contexts requires transparent coordination modes, auditable tariff-setting, and explicit value-sharing rules.

---

## uid: `doi:10.2139/ssrn.7075188`

- title: Edge-Enabled Digital twin-Based Federated Explainable Agentic Artificial Intelligence for Real-Time Sustainable Smart City Governance
- authors: CHIRANJEEVI PANDI, Sailesh Iyer
- affiliations: not stated
- posted: 2026-07-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7075188
- keyword hits: agentic

### abstract

The increasing complexity of smart city ecosystems and the demand for real-time urban governance present challenges in privacy preservation, communication overhead, scalability, transparency, and adaptive decision-making. Existing frameworks often rely on centralized architectures and investigate digital twins, federated learning, explainable artificial intelligence, and agentic intelligence independently, limiting coordination and sustainability. This study proposes an Edge-Enabled Digital Twin-Based Federated Explainable Agentic Artificial Intelligence framework for real-time sustainable smart city governance. The proposed framework integrates edge intelligence, digital twin synchronization, federated learning, explainable decision-making, and agentic reasoning within a unified architecture to enable collaborative and adaptive urban intelligence. Representative datasets from transportation, energy management, environmental monitoring, healthcare, and public safety are used for evaluation in a distributed simulation environment. Experimental results demonstrate that the proposed framework outperforms conventional intelligent approaches by improving decision accuracy, reducing communication overhead, and enhancing transparency and responsiveness. Overall, the proposed framework provides a scalable, privacy-aware, and trustworthy foundation for sustainable smart city governance through transparent, adaptive, and intelligent decision support.

---

## uid: `doi:10.2139/ssrn.6922218`

- title: Does AI Create a "Permanent Underclass"? From Market Structure to Complementary Assets, Industry Resilience, and the Choice of Metric
- authors: Yoichiro Hara
- affiliations: not stated
- posted: 2026-07-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6922218
- keyword hits: agentic

### abstract

In April 2026, the New York Times warned that Silicon Valley is "bracing for a permanent underclass." This working paper tests that claim against standard economics in two stages: first building the logic with established frameworks (the economics of tort law, industrial organization, complementary-assets theory, effective demand), then verifying the facts that logic presupposes against primary sources (Epoch AI, METR, the World Economic Forum, the EU AI Act, Stanford's Digital Economy Lab, the ILO, the NBER). Five findings organize the analysis. (1) What gates AI substitution is not capability but the insurability of residual error: deployable automation = min(capability, insurability). (2) The frontier labs can hold market share while earning little durable rent: open-weight models trail the frontier by roughly three months and enterprise spending is violently contested. Share is not rent; profit migrates instead to the adjacent complementary assets. (3) Followed to its end, the underconsumption logic does reach "a permanent underclass is a stable equilibrium," but measured reliability gaps (the best generalist robot policy completes 17.7% of real-hardware tasks; agent autonomy remains capped) pull the near-term shape back to a ratcheting Minsky cycle: partial substitution punctuated by financial crises. (4) The reprieve is a clock, not a wall: the agentic task horizon doubles roughly every seven months. (5) Whether the picture is pessimistic or optimistic is a question of metric: measured in rent, wealth concentrates; measured in consumer surplus, AI is strongly equalizing. The future splits: access to capability more equal than ever, and the wealth that access converts into more concentrated than ever.

---

## uid: `doi:10.2139/ssrn.7075267`

- title: Foundation Models Collaboration via Decoupled Cross-Modal Distillation and Semantic Decomposition for Weakly Supervised Remote Sensing Segmentation
- authors: jing li, Dong Zhao, Dan Zhang
- affiliations: not stated
- posted: 2026-07-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7075267
- keyword hits: foundation model, prompting

### abstract

Pixel-level annotation of remote sensing imagery is prohibitively expensive, driving demand for weakly supervised approaches that rely solely on image-level labels. However, class activation maps generated by classification networks tend to focus on discriminative sub-regions and suffer from incomplete activation and boundary adhesion, especially in remote sensing scenes with dense land-cover coexistence and large scale variations. To address these issues, this paper proposes a three-stage weakly supervised segmentation framework. First, a lightweight adaptation branch is built upon the cross-modal prior of CLIP, and a Sigmoid-based multi-label decoupled distillation strategy converts the conventional class-competitive constraint into independent category-wise response optimization, improving the semantic completeness of initial activation maps. Second, DINOv2 features are employed to decompose adhered large-scale regions before SAM prompting, and spatial-semantic constraints are introduced to guide point-box prompt generation and mask filtering, producing refined pseudo-labels with improved boundary quality and class consistency. Finally, a compact network is warm-started and retrained on refined pseudo-labels, requiring no foundation model at inference. Experiments on Potsdam, LoveDA, and DeepGlobe achieve mIoU scores of 53.16%, 52.66%, and 62.98%, respectively, outperforming recent weakly supervised segmentation methods with a maximum gain of 6.55% and showing consistent performance across different remote sensing scenarios using only image-level supervision.

---

## uid: `doi:10.2139/ssrn.7070619`

- title: From Alliances to Swarms: Rethinking Competition and Collaboration in the Age of AI
- authors: Yves L. Doz, Soumitra Dutta
- affiliations: not stated
- posted: 2026-07-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7070619
- keyword hits: agentic

### abstract

Established frameworks for inter-organizational strategy-alliance theory, ecosystem analysis, and platform economics-have been developed primarily for a world in which coordination between firms is deliberate, contract-governed, and mediated by human managers. The proliferation of agentic artificial intelligence is rendering these assumptions progressively inadequate. This paper argues that competition and collaboration in AI-enabled environments increasingly occur through what we term swarms: temporary, real-time configurations of agentic agents, data, capabilities, and protocols drawn from multiple firms and ecosystems that assemble to execute a specific interaction, compete and collaborate simultaneously, and dissolve upon its completion. Swarms represent a qualitatively new unit of inter-organizational strategy-distinct from alliances (which are durable relational structures) and from ecosystems (which are enduring participation environments)-and require a correspondingly new analytical framework. We propose a three-layer model in which capability bundle (the capability base defined by M&A and alliances), context (the ecosystem environment within which capabilities can interact), and dynamics (the swarms through which capabilities create and capture value in real time) operate as interdependent competitive layers. We further introduce the Swarm Stack, a six-layer architecture-capability, interface, agent, coordination, competition, and governance-that describes the infrastructure of swarm-based inter-organizational competition. We identify five sources of swarm advantage (selection, prediction, coordination, latency, and trust), examine the distinctive governance challenges that cross-organizational agentic interaction creates, and discuss implications for strategy theory and the reconceptualization of strategic leadership.

---

## uid: `doi:10.2139/ssrn.7069660`

- title: Incentive-Compatible Token Design as a Signal of Venture Quality
- authors: Guillaume Andrieu
- affiliations: not stated
- posted: 2026-07-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7069660
- keyword hits: token embedding

### abstract

This paper examines whether token design can serve as a signal of venture quality in decentralized fundraising environments. We develop a simple model in which an entrepreneur privately informed about project quality chooses between a neutral token and an incentive-compatible token embedding a milestone-contingent feature. While the latter increases the likelihood of attracting external funding, it imposes a private cost on the entrepreneur.Because token design is publicly observable prior to investment, it affects investor beliefs and financing decisions. The model shows that a separating equilibrium arises only for an intermediate range of design costs. If incentive-compatible features are too inexpensive, low-quality ventures mimic high-quality ones and the signal loses credibility. If they are too costly, even high-quality entrepreneurs refrain from adopting them, leading to pooling outcomes.The paper highlights how signaling can be embedded directly in token architecture through observable design choices that constrain entrepreneurial behavior. The model also yields testable empirical implications: token structures imposing meaningful constraints on founders should attract greater investor participation, whereas nearly costless features should not predict venture quality. These predictions are consistent with emerging evidence on token-based financing.

---

## uid: `arxiv:2607.06495v1`

- title: Pitwall: Faithful Natural-Language Race-Strategy Briefings from a Calibrated Real-Time Monte Carlo Engine
- authors: Juan S. Santillana
- affiliations: not stated
- posted: 2026-07-07
- source: arXiv
- link: https://arxiv.org/abs/2607.06495v1
- keyword hits: fine-tuning

### abstract

Live sports commentary is grounded generation under a deadline: statements concern real, named athletes, the grounding state changes every few seconds, and no reference text exists at generation time. We present Pitwall, a production system that generates natural-language Formula 1 strategy briefings in English, Spanish, and Portuguese, treating faithfulness as an architectural property rather than an aspiration: every published sentence is decomposed into typed factual claims (positions, gaps, tyres, pace, overtakes, race control) and each claim is verified against the probabilistic race state that prompted it. The same verifier gates the fine-tuning data: of 3,045 model-written targets, only the 81.9% whose every claim is state-supported are retained, the rest falling back to a provably faithful template, so the generator never sees an ungrounded target. Verification is meaningful because of the grounding substrate: a vectorized Monte Carlo engine (N=2,000 per-lap race continuations) calibrated on 126 races (2018-2024) and validated on fully held-out 2025-2026 seasons (winner-in-top-3 90.3% over 155 backtests; held-out Brier 0.0745). A recurring finding spans both halves of the system: virtues trade off and must be gated separately. In simulation, calibration-optimal is not decision-optimal; in generation, fine-tuning on richer targets buys vividness that collapses into hallucination when the grounding state is sparse -- a failure a four-base replication traces to base-model instruction adherence, not scale, and that sparse-context auditing removes from the production model. End-to-end operation -- live timing to verified trilingual briefings -- was confirmed at two consecutive live Grands Prix (Austria and Britain, 2026); at Silverstone a timestamped probability trace, committed to disk before the outcome was known, locked onto the eventual winner ten laps before the flag.

---
