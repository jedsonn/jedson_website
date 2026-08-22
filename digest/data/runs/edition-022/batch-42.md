# Classification batch 42 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-42.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7313518`

- title: Governing AI-mediated Development in Digital Public Infrastructure
- authors: Muhammad Hamza
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7313518
- keyword hits: agentic

### abstract

Digital Public Infrastructure (DPI) increasingly relies on open-source software that supports public services, while AI coding agents are becoming capable of generating and modifying software with minimal human intervention. However, how AI coding-agent activity is adopted, governed, and made visible within DPI remains unexplored. To address this gap, we conducted a multi-stage empirical study of 295 DPI repositories and a matched comparison corpus of 179 non-DPI repositories, examining AI-coding-agent activity, governance of AI-authored contributions, and the visibility and human review engagement of agentic pull requests. Our results show that, after accounting for observed repository activity within the 200commit scanning window, there was no statistically significant difference in detected AI-coding-agent activity between DPI and comparable repositories, despite a higher raw prevalence in DPI repositories. The repository-level findings further showed that, among the 69 DPI repositories with detected AI-codingagent activity, 47.8% contained AI-facing configuration, whereas only 4.3% contained governance content addressing AI-authored contributions. At the pull-request level, AI involvement was frequently not visible on the default pull-request review surface: 56.0% of agentic pull requests lacked an AI signal there. These findings point to an emerging accountability gap in AImediated DPI development, where AI participation can occur without corresponding contribution-level governance or visible provenance. We argue that accountable AI-mediated development requires software-engineering infrastructure that connects AI provenance, governance expectations, and human responsibility rather than relying solely on individual reviewer vigilance.

---

## uid: `doi:10.2139/ssrn.7292698`

- title: From Human-in-the-Loop to Human-on-the-Hook: Rethinking Organisational Accountability for Agentic AI
- authors: Raghu Pradeep Nair
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7292698
- keyword hits: agentic

### abstract

The emergence of agentic artificial intelligence (AI) marks a significant shift from AI systems that merely assist human decision-making to systems capable of planning, executing tasks, and making consequential decisions with limited human intervention. This article addresses the resulting accountability question by proposing a graduated autonomy-accountability framework that links the degree of AI autonomy and potential harm to corresponding levels of human oversight, organisational control, and legal responsibility. It argues that the conventional "human-in-the-loop" safeguard does not, by itself, guarantee meaningful accountability, and reconstructs accountability as a function of delegated authority and foreseeable risk rather than of a human's mere procedural presence. Grounding this argument in the law of agency, negligence, vicarious liability, and corporate governanceincluding Indian statute and case law alongside comparative regulatory instruments such as the EU AI Act and Singapore's Model AI Governance Framework for Agentic AIthe article develops the graduated model into an operational tool for allocating responsibility among developers, deploying organisations, supervising managers, and designated AI owners. It concludes that accountability for agentic AI requires organisations to move from asking "is a human in the loop?" to "who is meaningfully on the hook, and for what?"

---

## uid: `arxiv:2608.19511v1`

- title: Symposium: Trust via Auditable Records for Communities of AI Scientist Agents
- authors: Dexter Pratt
- affiliations: not stated
- posted: 2026-08-20
- source: arXiv
- link: https://arxiv.org/abs/2608.19511v1
- keyword hits: ai agent

### abstract

Symposium is a formal framework and practical implementation to record the operation of AI agents deployed by small scientific research communities. Symposium provides long-term, immutable histories of agent-driven research activity, leaving auditable trails of analyses, hypotheses, data, and scientific discourse. This shared record of published artifacts enables agents to build on prior work and preserves the evidence researchers and agents need to make purpose-dependent trust assessments. Symposium captures scientific argument, including structured claims, fine-grained evidence citations, assumptions, and explicit declarations of what material may and may not be used as evidence. Symposium differs from AI co-scientist agents or integrated AI research environments; it is a framework that separates a scientific community's durable history from the agents and other systems that operate on that history. It assumes that a community will use diverse AI systems in a rapidly evolving environment. A working implementation of the publication infrastructure, agent prompt components, and documentation are provided to enable users to rapidly set up and run their own Symposium community.

---

## uid: `doi:10.2139/ssrn.7329674`

- title: A reproducible leakage-safe ensemble-and-explainability pipeline for multi-class image classification on grouped camera datasets
- authors: Suresh Arumugam, Bharathiraja Nagu, Richa Vijay, B. Ankayarkanni
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7329674
- keyword hits: fine-tuning

### abstract

Image-classification pipelines trained on datasets captured by multi-view or stereo cameras are prone to a silent, reproducibility-breaking error: near-duplicate views of the same object (stereo triplets and their augmented variants) leak across the train/validation/test split, inflating reported accuracy. This article describes a reproducible pipeline that (i) enforces leakage-safe evaluation through a group-aware StratifiedGroupKFold scheme keying every image to a physical-scene identifier, (ii) combines three transfer-learned CNN backbones (InceptionV3, ResNet50, MobileNetV2) through a validation-optimised weighted-average decision fusion, and (iii) attaches a dual post-hoc explainability layer (SHAP and Grad-CAM) so every prediction is auditable. A two-phase transfer-learning protocol (head warm-up then fine-tuning) standardises training. The grouping and fusion logic is model-agnostic and drops into any Keras/PyTorch workflow. We validate it on a public 13-class biomedical-waste dataset, confirming the pipeline trains, fuses, and explains as intended, and that the leakage-safe split changes the honest accuracy estimate.

---

## uid: `doi:10.2139/ssrn.7327563`

- title: Self-supervised In-context Operator Learning for Stochastic Mean-Field Control
- authors: Suyi Gao, Mo Zhou, Rongjie Lai
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7327563
- keyword hits: in-context learning

### abstract

Stochastic mean-field control (MFC) provides a fundamental framework for coordinating large populations of interacting agents under uncertainty, with applications ranging from swarm robotics and systemic-risk management to Schr\"odinger bridges and diffusion-based generative modeling. Existing numerical and deep-learning methods solve one MFC problem instance at a time and must be re-optimized whenever the task changes. In this work, we formulate stochastic MFC as an operator-learning problem and develop, to the best of our knowledge, the first mesh-free, self-supervised neural operator for stochastic MFC. The main challenge is that the diffusion term in the controlled Fokker--Planck equation precludes deterministic transport-map representations. We address this challenge by combining the probability-flow ODE with an invertible normalizing-flow-based transformer, which recasts the dynamics as a deterministic continuity equation and enables closed-form score evaluation through the exact inverse and analytical log-determinant of the normalizing flow, with $\mathcal{O}(d)$ cost per particle for networks of fixed size. Through transformer-based in-context learning, task prompts, represented by compact distribution parameters or raw particle clouds, condition the transport map, enabling a single pretrained operator to solve unseen tasks in one forward pass. The resulting \emph{Normalizing Flow Invertible Solution Transformer} (NFIST) is trained end-to-end by minimizing the stochastic control objective directly, requiring no precomputed numerical solutions for training. We further prove the consistency of the proposed operator-learning formulation with task-by-task optimization. Numerical experiments on stochastic optimal control, Schr\"odinger bridge, systemic-risk control, and obstacle-avoiding path planning demonstrate effective zero-shot generalization while substantially reducing the computational cost of solving large families of stochastic MFC problems.

---

## uid: `doi:10.2139/ssrn.7323618`

- title: Deterministic Governance for Autonomous Financial Transactions on Distributed Ledgers: A Structural Enforcement Architecture with Cryptographic Attestation and Protocol-Native Multi-Signature Co-Signing
- authors: James Benton
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7323618
- keyword hits: ai agent

### abstract

Autonomous actors, including AI agents, decentralized autonomous organizations (DAOs), decentralized unincorporated nonprofit associations (DUNAs), algorithmically managed funds, and individuals operating through programmatic interfaces, are increasingly executing financial transactions on distributed ledger networks without governance oversight. Existing approaches to controlling these actors rely on application-level middleware operating within the same trust boundary as the actors being governed, post-transaction monitoring that detects violations after irreversible execution, or multi-party computation systems that provide distributed key management without policy evaluation. None of these approaches provide structural enforcement: the property that unauthorized transactions are not merely detected but are impossible to execute at the protocol level. This paper presents SovereignGate, a deterministic governance enforcement system that achieves structural enforcement through protocol-native multi-signature co-signing with disabled master keys. The system comprises a Rust enforcement kernel with layered crate dependencies and compile-time boundary enforcement, a deterministic policy evaluation engine with deny dominance and independent fact inference, a bylaws-as-code domain-specific language for encoding entity governance rules as content-addressed policy bundles, a cryptographic receipt chain with Ed25519-signed Merkle-anchored attestation of every governance decision, and a structural co-signing mechanism where the governance kernel controls a signer key in a multi-signature configuration with disabled master keys, making transaction execution without governance approval structurally impossible at the consensus layer. The preferred embodiment integrates with the XRP Ledger, whose native multi-sign capabilities, sub-second settlement, and minimal transaction fees make per-transaction governance economically viable. The architecture is chain-agnostic, supporting additional distributed ledger protocols through adapter crates implementing a common trait interface. No existing system combines deterministic policy enforcement, Merkle-chained cryptographic attestation, and structural protocol-level co-signing for autonomous financial actors. The patent landscape for this intersection is empty.

---

## uid: `doi:10.2139/ssrn.7322019`

- title: Cross-Interaction Derivability:From Output Safety to Auditable AI Trajectories
- authors: Vincenzo D'amico
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7322019
- keyword hits: agentic

### abstract

Artificial intelligence is increasingly being evaluated through units that are too small for the systems now being built. Persistent memory, long-horizon tasks, tool use, and autonomous or multi-agent interaction shift the relevant object of audit from the isolated output to the trajectory through which traces are retained, selected, transformed, weighted, and eventually translated into intervention. The distinction rests on an order-of-observation premise: output properties can be assessed at first order (O1), whereas derivability begins at second order and beyond (O2+), because its object is the reconstructable relation among states and transformations rather than the endpoint itself. This paper introduces cross-interaction derivability as a distinct epistemic property of persistent and agentic AI systems: the capacity to reconstruct the materially relevant path through which distributed evidence acquires sufficient authority to justify consequential action. Derivability is distinguished from explainability, provenance, logging, and traceability. The paper argues that privacy of content does not entail derivability of intervention; that gating and threshold-setting are not merely technical operations but distributions of epistemic authority; and that a minimum evidence path may permit selective opacity of content while preserving contestability. It also develops the notion of epistemic compression: the possibility that better localization of consequential transitions can improve auditability while reducing unnecessary search, evaluation overhead, latency, compute, and energy demand. Finally, the paper connects trajectory auditing to responsibility, regulation, and the contemporary crisis of trust surrounding frontier AI. Its claim is deliberately narrow: novelty does not lie in persistent memory, provenance, or longitudinal monitoring as such, but in treating derivability across interactions as a distinct property and the trajectory-not the isolated output, memory item, or agent-as the primary object of audit.

---

## uid: `doi:10.2139/ssrn.7308699`

- title: Retrieval-Augmented Explainable AI for Converting Multi-Disease Medical Image Predictions into Clinician-Friendly Clinical Recommendations
- authors: Zainab Adekunle
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7308699
- keyword hits: retrieval-augmented

### abstract

Artificial intelligence has demonstrated considerable potential for detecting disease from medical images, yet the clinical value of a prediction depends on more than classification accuracy. Clinicians must understand what the system detected, why the finding matters, how reliable the prediction is, and what action is appropriate. This paper proposes a retrieval-augmented explainable artificial intelligence framework for converting multi-disease medical image predictions into clinician-friendly clinical recommendations. The framework is designed for four representative conditions: pulmonary disease, diabetic retinopathy, skin cancer, and breast cancer. It combines disease-specific image classifiers with visual explanation methods, structured clinical context, uncertainty assessment, and retrieval from curated clinical guidelines and evidence repositories. A controlled language model then synthesizes the retrieved evidence into a concise recommendation while preserving source attribution and clearly separating model findings from clinical interpretation. The proposed architecture addresses a major weakness of conventional medical AI: the tendency to produce isolated labels or confidence scores without workflow-oriented guidance. Retrieval augmentation can reduce dependence on static model memory, but it does not guarantee factuality; poor retrieval, outdated evidence, or inappropriate synthesis may introduce new risks. The framework therefore includes evidence-ranking safeguards, citation verification, abstention rules, human review, audit logs, and prospective clinical evaluation. The paper argues that explainability should be designed as an evidentiary chain linking image findings, clinical context, authoritative guidance, uncertainty, and recommended action. Such systems should augment professional judgment rather than provide autonomous diagnosis or treatment.

---
