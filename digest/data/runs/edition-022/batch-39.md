# Classification batch 39 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-39.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7278200`

- title: What Small Models Know About Kazakh Morphology and Cannot Be Asked
- authors: Alikhan Tuganbayev
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7278200
- keyword hits: prompting, qwen

### abstract

Multiple-choice benchmarks report that language models underperform in Kazakh relative to Russian, but cannot say why: a model can answer them without ever producing a Kazakh word form. We introduce a generative benchmark of Kazakh nominal inflection covering eight morphological categories over fifty regular noun stems, with gold answers computed from vowel-harmony and consonant-assimilation rules rather than annotated by hand. Holding items and gold answers byteidentical while varying only the language of the instruction, we find that small models are limited by instruction comprehension rather than by morphological knowledge. gemma3-4b scores 16.6% under Kazakh instructions against 48.8% in Russian and 52.0% in English, with a noise floor of 2.7 points; qwen2.5-3b scores 4.3% and 21.0%. The deficit is not uniform: categories whose Kazakh grammatical terminology is common show little or no penalty, while those with more specialised terminology fall to zero. A single in-context example raises Kazakh-instructed accuracy to 54.7% and five raise it to 74.7%, eliminating the gap, with gains concentrated precisely in the categories that had failed-the knowledge was present throughout and the instruction could not reach it. This reconciles our findings with prior work reporting a 1-5 point instruction-language penalty for Turkish and Finnish under fewshot prompting: demonstrations substitute for instruction comprehension and therefore mask the effect. The gap also vanishes with scale, gemma-4-31b reaching 98.7% and 100.0% with one genuine morphological error in 300 items. We further report five methodological findings for cross-lingual generative evaluation, including a translated case label that moved one category by 41 points and was fully rescued by examples, a morpheme that resists isolated elicitation on grammatical grounds, and hidden reasoning tokens that silently consume the output budget and are scored as errors.

---

## uid: `doi:10.2139/ssrn.7269779`

- title: Federated Agentic Intelligence for Cross-Agency Law Enforcement: A Governance-by-Design Architecture
- authors: Andrew Wang
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7269779
- keyword hits: agentic

### abstract

Two Australian mass-casualty events-the Wieambilla welfare check ambush of December 2022 and the Bondi Beach terrorist attack of December 2025-share a structural signature: intelligence relevant to the decisions made immediately before each event existed within the holdings of multiple agencies and was never synthesised. At Wieambilla, threat intelligence in the New South Wales Police Force (NSWPF) system did not reach Queensland Police Service (QPS) officers dispatched to the same address. At Bondi Beach, community threat assessments provided to police from late November 2025 and updated six days before the attack reached multiple commands and intelligence units; the Royal Commission on Antisemitism and Social Cohesion has reserved for further inquiry the integration pathway between their receipt and the resourcing decision for the event (Royal Commission on Antisemitism and Social Cohesion, 2026, paras 4.27, 2.40-2.41, 2.45-2.50). These are not failures of individual officers or agencies. They are structural failures of architecture. This paper proposes a governance-by-design architecture for federated agentic AI operating across Australian law enforcement and regulatory agencies that addresses this structural gap. The architecture is jurisdiction-agnostic at the technical layer and is demonstrated in the Australian context because the research is conducted there and the primary sources are accessible; §7.2 identifies the legislative mapping required for Australian deployment, which would need to be conducted independently for each jurisdiction in which the architecture is adopted. The proposed system enables cross-agency investigative intelligence synthesis without requiring raw evidence or personal data to leave any agency's custody. Three contributions are advanced. First, a federated agentic intelligence architecture-including the sovereign agency node layer, the inter-agency federation layer, the dynamic coordination lead model, the fail-safe mechanism, and the verification mode — capable of cross-agency investigative reasoning at operational scale. Second, a mapping of that architecture's outputs to forensic chain-of-custody requirements and to the Evidence Act 1995 (Cth), introducing the concept of the ante-hoc design requirement: an architectural mechanism that pre-constitutes the evidentiary material needed to satisfy the section 146 presumption and to resist its rebuttal, generated at the moment of output rather than reconstructed afterwards. Third, a taxonomy of six failure modes, derived from documented Australian law enforcement intelligence failures and the author's operational experience, is offered as a living instrument that the sector can adopt, extend, and evaluate against real outcomes as the architecture matures in deployment. All six failure modes have at least one documented instance across the coronial and Royal Commission records and the contemporaneous public record following the Bondi attack.

---

## uid: `doi:10.2139/ssrn.7300707`

- title: Edge language models and agentic AI in building automation: a scoping review of evidence maturity and authority tiers
- authors: Raimo Simson, Martin Kiil, Karl-Villem Võsa, Jarek Kurnitski
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7300707
- keyword hits: agentic

### abstract

Building automation and control systems (BACS) face EU regulatory pressure alongside the maturation of edge-deployable small language models and agentic frameworks. This PRISMA-ScR scoping review synthesises 264 peer-reviewed journal articles (262 in-scope primary + 2 background reviews) on language-model and agentic-AI applications in BACS over January 2022 – May 2026, and proposes two original frameworks: an E1–E4 evidence-maturity scale and a T1–T4 read/write control-authority taxonomy. Screening and E×T-coding reliability were checked by dual screeners (κ = 0.733–0.895) and a second coder on a stratified sample (κ_E = 0.786, κ_T = 0.715). The peer-reviewed evidence base has not yet matured to deployment-grade: only one LM/agentic-AI record reaches long-field evidence (E4), a read-only GPT-based diagnostic; a non-LM Autoformer FDD comparator anchors field-level transformer evidence at the same tier. No LM/agentic-AI study reaches E4 × T3 (supervisory autonomous) or E4 × T4 (direct-write), and no T4 record appears anywhere; a targeted preprint/conference scan returns the same outcome, and supervisory-autonomous (T3) evidence concentrates in simulation. The orchestrator-plus-specialists pattern recurs in multi-agent BACS papers, but the Model Context Protocol and Agent-to-Agent protocol sit above the BACS interoperability layer rather than within it; commodity edge hardware runs quantised small language models at sub-1 Wh/query without yet a BACS-validated operational deployment. The T1–T4 framework offers a practical risk-screening heuristic for EU AI Act assessment. Multi-building year-long validation, BACS-specific benchmarks, operational-technology red-teaming, and AI-layer energy accounting are open priorities for 2026–2028.

---

## uid: `arxiv:2608.17148v1`

- title: Authorization Before Context: A Model-Neutral Audience Boundary Against Cross-Audience Memory Leakage in Agentic Systems
- authors: Sibo Liu
- affiliations: not stated
- posted: 2026-08-17
- source: arXiv
- link: https://arxiv.org/abs/2608.17148v1
- keyword hits: agentic

### abstract

A personal language agent learns a fact from one audience and may later place it in the prompt it assembles for another. This memory-to-context step is an attack surface: ambiguous or inconsistent channels, cross-audience prying, and poisoned memory can each cause the system to assemble context containing a fact relevant to the query yet unauthorized for the current viewers. We introduce authorization before context: a single, anti-monotone audience-membership rule applied at the memory-to-context transition. Each item carries the audience present when it was recorded; the current viewer set is read from channel metadata and falls back to public when ambiguous; and the item is admitted only when every current viewer already belonged to its audience. We prove that this rule gives every participant cross-channel recall while ensuring, by exclusion rather than by model behavior, that nothing recorded for a narrower audience reaches a broader one and that poisoned memory cannot widen its own audience. The boundary is a model-neutral invariant on the exact assembled context: a forbidden fact must be absent before the model is called. On a synthetic Contextual-Integrity suite, no forbidden fact entered the context our boundary assembled, whereas unscoped baselines included such facts by construction; we further audit that every read path fails closed. The evidence is preliminary and synthetic.

---

## uid: `arxiv:2608.16357v1`

- title: MELD: A Protocol for Merging Knowledge Across Distributed Agentic Memories
- authors: Lauri Lovén, Jaakko Sauvola, Jukka Riekki, Sasu Tarkoma
- affiliations: not stated
- posted: 2026-08-17
- source: arXiv
- link: https://arxiv.org/abs/2608.16357v1
- keyword hits: agentic

### abstract

Autonomous agents share a transport and can call each other's tools, but they cannot share what they know: no protocol lets two agents' memories reconcile a fact phrased two ways, link related facts held apart, or reconcile contradictory knowledge without silently discarding either claim. We present MELD, a self-managing coherence mechanism for a federation of agent memories whose run-time model is the knowledge graph itself. Each brain admits every incoming claim through a five-outcome procedure (insert, merge, relate, conflict, or reject), decided from three signals (scoped claim-key identity, embedding similarity, and a natural-language-inference verdict) under context and freshness gates, and acting through exactly one auditable, authenticated Patch, the only object that mutates state. A binding onto standard publish/subscribe transport with a per-claim status CRDT keeps sovereign brains coherent in claim status without a coordinator: self-healing after partitions and under lossy routing, and self-protecting against silent rewrite by a peer, under a benign-fault model. MELD does not adjudicate truth; a detected contradiction is preserved for later adjudication, never silently resolved. On HotpotQA distractor, distributed merge is recall-non-inferior to a centralized store under a pre-specified equivalence test and recall-superior to naive union at about 11% less live storage; the merge classifier separates at AUC 0.968 with a 0.013 false-merge rate on adjudicated candidate pairs; the status CRDT reconverges in 30/30 real partition-heal trials where last-writer-wins manages 11/30; and semantic routing delivers about 3x fewer messages at matched recall. We evaluate on a real computing continuum spanning an operator-grade 5G edge, national HPC, and a local tier, with empirically calibrated thresholds.

---

## uid: `doi:10.2139/ssrn.7305682`

- title: LiteTSM-TDiff: Lightweight Temporal Shift and Temporal Difference Encoding for Edge-Efficient Human Action Recognition on UCF101 and HMDB51
- authors: Karen Shaylee, Rajiv Vincent, Rajesh M, Arun  Kumar Sivaraman, Kamalavelu Velayutham
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7305682
- keyword hits: fine-tuning

### abstract

Video-based human action recognition on edge devices requires models that can achieve a good balance between accuracy, model size, and inference speed. Most state-of-the-art methods use Kinetics-pretrained backbones and computationally expensive 3D convolutions. These requirements make them difficult to deploy on resource-constrained devices. This work presents LiteTSM-TDiff, a lightweight single-stream action recognition architecture based on an ImageNet-pretrained MobileNetV2 backbone. The proposed model does not require video-scale pretraining. It focuses on reducing computational requirements while maintaining effective temporal feature learning. The architecture combines two complementary temporal modules. LiteTSM is a fixed bidirectional temporal shift module applied at the output of MobileNetV2 block 14 (7×7 spatial resolution, 160 channels). It enables temporal communication between adjacent frames without adding any learnable parameters or additional GFLOPs. LiteTDiff is a lightweight temporal difference encoder based on a gated residual Conv1d bottleneck. It explicitly models first-order motion dynamics from post-global-average-pooling temporal feature sequences. The module adds approximately 1.642M learnable parameters. To improve training stability, a staged training protocol is used. The protocol separates backbone-frozen warmup from joint fine-tuning. The complete model is evaluated on UCF101 and HMDB51 using the standard three-split protocol. LiteTSM-TDiff achieves 81.10% ± 0.24% Top-1 accuracy on UCF101 and 51.66% ± 1.23% Top-1 accuracy on HMDB51. The model contains 3.995M parameters. It requires 4.792 GFLOPs per 8-frame clip. It achieves a CPU inference latency of approximately 164–167 ms per clip. Ablation studies confirm that both LiteTSM and LiteTDiff provide meaningful and complementary improvements. Cross-dataset transfer from UCF101 to HMDB51 achieves 53.40% Top-1 accuracy.

---

## uid: `doi:10.2139/ssrn.7301221`

- title: AI Data Governance Layer (ADGL): Governing Knowledge, Analysis, and Consequences in Model-Agnostic AI Systems Submission Draft v1.2 GBSN Research
- authors: GBSN Research
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7301221
- keyword hits: retrieval-augmented

### abstract

Artificial intelligence systems increasingly operate as execution chains rather than isolated models: they retrieve or receive information, transform that information through one or more analytical procedures, and then return, recommend, or trigger consequential outcomes. Existing governance mechanisms address important parts of this chain-including organizational risk, access control, usage rights, provenance, model documentation, human oversight, and agent authorization-but they do not by themselves provide a shared runtime semantic contract for three distinct questions: what knowledge may influence a case, what analysis may be performed on that knowledge, and what consequence a governed result may produce. This paper develops the AI Data Governance Layer (ADGL) as a model-, storage-, retrieval-, and enforcement-agnostic policy architecture organized into Knowledge Governance, Analysis Governance, and Consequence Governance, with Audit and Provenance as a cross-cutting plane. The architecture is derived from a synthesis of prior work in usage control, information-flow control, provenance, data/model documentation, production ML engineering, algorithmic auditing, human-automation interaction, retrieval-augmented systems, prompt-injection research, and current agent-security standardization. ADGL distinguishes INFORM, DECIDE, and ACT consequences so that informational systems, humanowned decisions, and machine-executable actions can share one semantic architecture without making autonomous action the default. An executable reference toolkit implements the proposed semantics through eight reference cases and 25 published normative conformance checks; a later toolkit revision adds 11 candidate execution-integrity checks that are reported separately from the normative evaluation. The paper presents the design requirements, formal execution model, implementation boundaries, initial performance characterization, comparative positioning, limitations, and open questions relevant to possible standardization.

---

## uid: `doi:10.2139/ssrn.7308998`

- title: Physics-informed lithium-ion battery SOH estimation from multi-source partial charging segments
- authors: Jilong Ma, Pengfei Bi, Yingyue Tan, Xin Liu, Xiong Zhang, Huijuan Zhang, Jinling Ma, Yu Wang
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7308998
- keyword hits: transformer model

### abstract

Accurate state of health (SOH) estimation is essential for the safe operation and service life management of lithium-ion batteries. In practical applications, complete charging profiles are often unavailable because of random user charging behavior, while partial charging segments cover only a limited operating range and may contain insufficient degradation information. To address this issue, this work proposes a physics-informed SOH estimation method based on partial charging segments and input from multiple sources. Local voltage, current, and temperature responses are extracted from the 0.7–0.8 interval of normalized charged capacity during charging and combined with the cycle index and initial capacity. A gated depthwise separable convolution module captures local curve patterns, while a causal Transformer models degradation dependencies across cycles. To improve physical consistency, a degradation dynamics residual, a monotonicity constraint, and a smoothness constraint are introduced during training. An adaptive loss weighting mechanism is also used to balance the data fitting loss and physics-informed constraint losses. The proposed method is validated on the XJTU and MIT datasets. Across nine test batches, the method achieves average MAPE and RMSE values of 0.3998% and 0.0075 Ah, respectively.

---
