# Classification batch 403 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-403.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7026391`

- title: AN EXPLAINABLE HYBRID CNN-BILSTM-TRANSFORMER FRAMEWORK FOR EEG-BASED EMOTIONAL STATE DECODING
- authors: INDRANEEL K, TRINATHBASU MIRIYALA
- affiliations: not stated
- posted: 2026-06-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7026391
- keyword hits: transformer model

### abstract

Electroencephalogram (EEG) signals are direct neural responses linked to emotional processes for emotion recognition. Signal analysis is the most important research area of affective computing, intelligent healthcare, brain‒computer interfaces and human‒computer interactions. Owing to the complex intersubject variability, spatiotemporal dependencies, and noisy and nonstationary nature of EEG signals with nonlinear characteristics, decoding the emotional state is a difficult task. To overcome these drawbacks, the current paper introduces a powerful deep learning architecture for spatial–temporal relevance (DLA-STR) for emotional-state pattern extraction and decoding from EEG signals. The proposed framework employs state-of-the-art EEG autoencoder-based latent feature compression, a convolutional neural network (CNN), bidirectional long short-term memory (BiLSTM) and bidirectional transformer-based multi-head self-attention mechanisms to collectively learn the spectral, spatial, and temporal representations of EEG signals that reflect emotional conditions: happy, sad, angry, neutral, and surprised. The proposed DLA-STR framework achieved an overall classification accuracy of 95.13%, precision of 95.08%, recall of 95.11%, F1-score of 95.03%, and ROC-AUC of 0.972, showing strong discriminative capability for emotional-state decoding. The fivefold cross-validation results further confirmed the robustness of the framework, with a mean accuracy of 95.10 ± 0.28%. The ablation study also verified the contribution of each architectural component, where the full CNN-BiLSTM-Transformer model achieved better performance than CNN-only, BiLSTM-only, CNN-BiLSTM, CNN-Transformer, and BiLSTM-Transformer variants. Further, the computational analysis showed that the proposed model maintains real-time feasibility with an inference time of 41ms, making it suitable for practical affective computing and neuroadaptive interface applications.

---

## uid: `doi:10.2139/ssrn.7010051`

- title: The Polar Geometry of Work
- authors: Joakim Storck, Jonatan Andersson
- affiliations: not stated
- posted: 2026-06-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7010051
- keyword hits: text embedding

### abstract

The task-based tradition treats occupations as bundles of tasks but lacks a formal representation of how those bundles relate to one another. Two properties of work are conflated: the kind of work an occupation involves, and how sharply focused it is within its domain. We propose a framework that separates them. Tasks have positions defined by angular direction (task domain) and radial position (task specificity), and occupations inherit their positions from their tasks. Specificity, which the human capital tradition defines at the worker level, becomes a structural property of the task itself, present in every direction. Depth is a special case of it: the specificity a worker reaches by investing in the competence a domain demands. We find that the market rewards specificity only as depth: in analytical directions specificity is depth and is rewarded; in service-oriented directions it carries no such investment and is not. We realize the framework from O*NET task statements using text embeddings, and test it against descriptors of skills, abilities, wages, and educational requirements. The framework’s predictions hold, and the results reproduce across encoders. Angular distance between occupations predicts pair-level differences in capabilities, wages, and educational requirements. The framework reframes labor market polarization as a continuous bipolar organization in task space, not a divide between categories of workers. Cognitive depth concentrates in the analytical and human-centered directions and carries the wage premium that divides high-wage from low-wage occupations.

---

## uid: `doi:10.2139/ssrn.7025876`

- title: Capacity attenuation anomaly detection of energy storage lithium batteries based on Transformer multimodal fusion
- authors: Chenchen Dong, Dashuai Sun
- affiliations: not stated
- posted: 2026-06-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7025876
- keyword hits: transformer model

### abstract

In order to solve the problem that the traditional capacity calculation method in the lithium-ion battery (LIB) system has significant errors and is difficult to accurately detect the abnormal capacity attenuation of single cells, this paper proposes an early capacity attenuation evaluation algorithm for energy storage batteries based on Transformer multimodal fusion(BTMF). By analyzing the voltage, temperature and current during the battery aging process, the algorithm innovatively designs a multivariate cooperative interval counting feature extraction strategy for one-dimensional and two-dimensional data to effectively capture the key features of capacity attenuation. For two-dimensional data, in order to enhance the model's perception of local details and global context dependencies, a channel-space dual attention parallel mechanism is proposed, and the two work together to improve the robustness of feature representation. At the same time, the algorithm introduces a hybrid fusion mechanism of soft and hard collaboration in multimodal feature fusion, realizes feature-level soft attenuation through dynamically generated channel-level attenuation coefficients, and suppresses the noise interference of secondary modes. Finally, the effectiveness of the dual attention mechanism is verified through accelerated aging experiments, and the performance of BTMF is verified in the actual data of large-scale energy storage power stations. At the same time, it is compared with a variety of Transformer models. The results show that BTMF significantly improves the accuracy and inference performance of capacity attenuation evaluation, providing reliable technical support for battery health management.

---

## uid: `doi:10.2139/ssrn.7025873`

- title: Domain-adaptive mixture-of-experts for cross-dataset lithium-ion battery state of health prediction via adaptive strategy selection
- authors: Liu Teng, Wei Li, Zhiqiang Li, Weiwei Huo
- affiliations: not stated
- posted: 2026-06-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7025873
- keyword hits: fine-tuning

### abstract

Accurate cross-dataset state of health prediction for lithium-ion batteries remains challenging due to distribution shifts arising from diverse cathode chemistries, operating temperatures, and charge-discharge protocols across heterogeneous battery fleets. This study proposes a Domain-Adaptive Mixture-of-Experts framework that automatically selects the optimal domain adaptation strategy for each target domain through a lightweight linear gating network comprising merely 32 learnable parameters. The framework integrates a shared Transformer-based backbone with four adaptation strategies spanning the full spectrum of target-domain information utilization, namely Zero-shot transfer, Test-Time Adaptation, Fine-Tuning, and Model-Agnostic Meta-Learning. Comprehensive evaluation on 564 battery cells from seven publicly available datasets under Leave-One-Domain-Out Cross Validation protocol demonstrates that the proposed framework achieves an average coefficient of determination of 0.864 with perfect oracle strategy alignment under full domain training and maintains competitive generalization at average R2 of 0.795 when each target domain is held out during gating network training. Hard argmax selection consistently outperforms weighted fusion across all seven domains with an average margin of +0.027 in R2, confirming that the four adaptation strategies compete rather than cooperate in this application context. Feature ablation analysis identifies sample count as the dominant determinant of strategy selection with performance degradation of ΔR2=-0.182 upon removal, followed by degradation slope and knee-point ratio as secondary signals. The proposed framework provides a practically deployable solution for battery management systems operating across heterogeneous fleets with minimal computational overhead and strong cross-dataset generalization capability.

---

## uid: `arxiv:2607.00245v1`

- title: Agent-to-Agent Finance: Blockchain Payments and Trust Infrastructure for Autonomous AI Agents
- authors: Hui Gong
- affiliations: not stated
- posted: 2026-06-30
- source: arXiv
- link: https://arxiv.org/abs/2607.00245v1
- keyword hits: ai agent

### abstract

Autonomous AI agents are beginning to occupy a position between analytical tools and transacting counterparties. They can interpret goals, call external tools, negotiate with other agents, access data and computation, and in some settings initiate payments or blockchain transactions. This development creates a distinct problem for financial markets: if software agents can act economically, market participants need infrastructure for identity, authorisation, payment, verification, reputation and accountability. This article develops the concept of agent-to-agent finance as the layer of machine-mediated financial interaction in which autonomous agents discover counterparties, purchase services, express transaction intent, execute payments and generate auditable evidence. The argument is not that blockchain is a universal substrate for finance, but that programmable settlement, smart wallets, decentralised registries and verifiable computation can address specific coordination frictions created by autonomous agents. Drawing on recent work on blockchain A2A payments, ERC-8004 agent registries, provenance-based wallets, deterministic inference, DeFi intent mining, and official evidence on AI adoption in financial services, the article situates agent-to-agent finance as an emerging form of financial market infrastructure. It argues that the decisive design question is bounded autonomy: how to let agents transact without making markets more opaque, fragile or unaccountable.

---

## uid: `arxiv:2606.31935v1`

- title: Delegation Rights: Property, Agency, and Investment Incentives in the Age of AI Agents
- authors: Yukun Zhang, Kemu Xu
- affiliations: not stated
- posted: 2026-06-30
- source: arXiv
- link: https://arxiv.org/abs/2606.31935v1
- keyword hits: ai agent

### abstract

AI agents increasingly operate inside digital accounts by exercising privileges that users already hold, raising a new control question: whether an existing account entitlement must be exercised manually or may be exercised through a user-authorized automated proxy. We define \emph{delegation rights} as the revocable, identity-preserving, scope-limited, and mode-specific authority of an account holder to authorize such proxy execution. We develop a three-party incomplete-contracts model with a User, an AI Agent provider, and a Platform. The contested object is not platform ownership, account transferability, data portability, or unrestricted API access, but residual control over the mode of account execution. Under Platform Control, the platform can protect infrastructure, identity systems, privacy boundaries, and third parties, but its discretionary veto weakens the User--Agent coalition's disagreement payoff and depresses relationship-specific investment. Under User Control, hold-up is reduced, but security, privacy, congestion, and third-party risks may remain insufficiently internalized. We then analyze \emph{Certified Delegation}, under which access protection is conditional on verifiable authorization, revocability, auditability, rate-limit compliance, data minimization, and risk mitigation. Certification is therefore not merely a technical safety screen; it is a conditional allocation of residual control. Illustrative mechanism simulations show how this regime can reduce deadweight loss by restoring delegation incentives while bounding residual risk.

---

## uid: `arxiv:2607.00250v3`

- title: LV-ROVER-MLT: Low-Resource Maltese OCR by Synthetic Fine-Tuning and Multi-Stream Arbitration
- authors: Adam Darmanin
- affiliations: not stated
- posted: 2026-06-30
- source: arXiv
- link: https://arxiv.org/abs/2607.00250v3
- keyword hits: fine-tuning

### abstract

Maltese OCR is constrained by the absence of a public, reusable paragraph-scale training corpus. We address this by generating synthetic Maltese line images, fine-tuning the Tesseract 5 LSTM, and combining five deterministic Tesseract configurations through anchor-preserving, lexicon-gated word-level arbitration. The method uses a fixed anchor stream, a longest-stream fallback, a confusion-based anchor corrector, and a Maltese-specific diacritic-restoration gate. Unlike canonical ROVER, candidate streams cannot restructure the anchor through insertions or deletions; they propose only eligible substitutions at aligned anchor positions. On the 422-paragraph development set of the DocEng 2026 Maltese OCR competition, the organizers' fine-tuned Tesseract baseline obtains CER 0.0234. Our pre-convention pipeline reaches CER 0.01317, a 44% reduction. Synthetic fine-tuning provides the largest single gain, while multi-stream arbitration contributes a further material reduction beyond the selected anchor, reaching CER 0.01220 in the current replay with paired-resampling support. A development-tuned label-convention normalization chain further reduces CER to 0.00700. We report recognition gains separately from benchmark-specific quote and dash normalization. We also evaluate portability on Hungarian and Luxembourgish. Luxembourgish improves significantly over our stock baseline, while the Hungarian result is inconclusive. Finally, we release a 36,803-pair Maltese OCR corpus derived from EUR-Lex and Wikipedia. The held-out competition result remains under organizer embargo and is not reported

---

## uid: `doi:10.2139/ssrn.7036761`

- title: An Agent-Driven Edge–Cloud Expert System for Radio-Frequency Fingerprint Authentication in Open Radio Access Networks
- authors: Yubo Wang, Qiao Liu, Jin Cao, Ziyi Gao, Hui Li, Jingyuan Han, Yong Wang, Huanhuan Wu
- affiliations: not stated
- posted: 2026-07-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7036761
- keyword hits: llm, retrieval-augmented

### abstract

Radio-frequency fingerprint (RFF) authentication is a promising physical-layer complement to credential-based access control in Open Radio Access Networks (Open RAN). However, temporal channel variation, receiver-state changes, site-specific propagation, and unknown access attempts can cause static fingerprinting models to drift from reliable operating points. This paper proposes an agent-driven edge--cloud expert system for continuous RFF authentication under domain dynamics. The system treats authentication maintenance as a closed-loop expert decision process rather than a one-shot signal classification task. At the edge, a control agent monitors authentication feasibility and performs low-latency operating-point correction through cached-score threshold replay and Pareto-filtered selection, avoiding repeated model execution during routine adaptation. When local correction becomes insufficient, a cloud coordination agent reuses cross-site operational experience to provide event-driven assistance. A retrieval-augmented LLM advisory agent generates bounded guidance proposals from similar historical cases, while model refresh handles severe mismatch or cold-start conditions. A conservative fallback advisor maintains bounded operation during edge--cloud interruption. Experiments on LoRa and 5G New Radio (5G NR) datasets under cross-time and cross-location shifts show that static RFF authentication degrades under domain dynamics, whereas the proposed expert system improves feasibility recovery and decision stability. System measurements further indicate millisecond-scale edge authentication, kilobyte-scale guidance exchanges, and model reprovisioning outside the per-signal critical path.

---
