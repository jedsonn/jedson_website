# Classification batch 379 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-379.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6744178`

- title: # Can AI Actually Trade? A Comparative Study of LSTM and Transformer Models Across Stocks, Crypto, and Forex
- authors: Vivaan Tyagi
- affiliations: not stated
- posted: 2026-05-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6744178
- keyword hits: transformer model

### abstract

Artificial intelligence has moved from academic novelty to practical tool in financial markets, with deep learning systems now executing trades across equity, cryptocurrency, and foreign exchange markets. Yet a persistent gap in the literature is the lack of direct, controlled comparisons between competing architectures under realistic trading conditions and across multiple asset classes simultaneously. This paper directly addresses that gap. We compare two leading sequence-modelling approaches-Long Short-Term Memory (LSTM) networks and Transformer models-trained on identical technical feature sets across U.S. equities, cryptocurrencies, and forex pairs, using daily data from 2019 to 2024. Rather than evaluating models solely on prediction accuracy, we embed each model in a backtesting framework with realistic transaction costs and assess performance using the metrics that actually matter in practice: annualised return, Sharpe ratio, Sortino ratio, maximum drawdown, and win rate. Our findings reveal a nuanced picture. Transformer models achieve meaningfully higher directional accuracy on equities and forex-consistent with their ability to attend to non-contiguous patterns across long histories-while LSTM networks prove more competitive in the momentum-driven, high-volatility cryptocurrency market. Both architectures substantially reduce portfolio drawdown relative to a buy-and-hold benchmark, demonstrating practical value even in cases where raw returns fall short. These results offer concrete guidance for practitioners choosing between architectures and contribute to a growing consensus that AI-based trading systems can add value, but that architecture choice should be informed by asset class characteristics.

---

## uid: `doi:10.2139/ssrn.6743059`

- title: What Do Foundation Models 'Prefer'? Disentangling Stated and Revealed Preferences in Neural Self-Driving Architectures
- authors: Lei Chang, McKenzie Izev
- affiliations: not stated
- posted: 2026-05-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6743059
- keyword hits: foundation model, prompting

### abstract

Foundation models (FMs) are increasingly proposed as core components of neural self-driving automobiles. However, a critical but unexamined failure mode exists: what an FM reports preferring (via natural language) may systematically diverge from what its empirically measured behavior reveals as its true preference. We introduce and investigate this stated vs. revealed preference gap in the context of autonomous driving architectures. Using a visionlanguage-action model evaluated in a realistic driving simulator, we conduct two complementary studies. First, we elicit the model's stated preferences by prompting it to compare competing neural driving architectures (e.g., end-to-end vs. modular). Second, we measure its revealed preferences by embedding the same model weights into each architecture and observing behavioral outcomes: safety violations, intervention rates, and the model's own internal evaluator signals. Our results demonstrate significant and systematic misalignment. The same FM verbally endorses modular, interpretable architectures while empirically revealing a strong behavioral preference for end-to-end control. Conversely, stated caution in safety-critical scenarios does not translate into cautious revealed actions. We term this phenomenon architectural preference misalignment-a gap that standard output-level alignment techniques fail to resolve. Our findings establish a new axis for FM evaluation and safe deployment in physical systems, showing that what a model says it prefers cannot be trusted without measuring what it does.

---

## uid: `doi:10.2139/ssrn.6677379`

- title: Adaptive Zero Trust Governance Framework for Autonomous and Agentic Digital Systems Using AI-Driven Risk Scoring
- authors: Vincent Chinedu Johnson
- affiliations: not stated
- posted: 2026-05-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6677379
- keyword hits: agentic

### abstract

The rapid evolution of artificial intelligence (AI), autonomous decision-making, and agentic computing is transforming modern digital infrastructures. Across sectors such as finance, healthcare, transportation, and critical infrastructure, intelligent systems increasingly operate with limited human intervention, enabling real-time responsiveness, automation, and scalability. However, the growing autonomy of these systems introduces cybersecurity challenges that exceed the capabilities of traditional defense architectures. Conventional cybersecurity models, including perimeter-based security and static trust assumptions, struggle to address adaptive, machine-driven environments where threats evolve continuously. Although Zero Trust Architecture (ZTA) provides a stronger security foundation through continuous verification, existing implementations often lack contextual intelligence, governance integration, and dynamic risk adaptation necessary for autonomous systems. This study proposes an adaptive AI-driven Zero Trust governance framework designed specifically for autonomous and agentic digital systems. The framework integrates machine learning-based threat intelligence, behavioural anomaly detection, contextual risk scoring, governance-based policy enforcement, and continuous feedback mechanisms into a unified architecture. A mixed-method methodology is adopted, combining quantitative machine learning evaluation using benchmark intrusion detection datasets with qualitative governance integration analysis. Experimental findings demonstrate that ensemble learning techniques improve cyber threat detection performance, while governance-driven policy orchestration strengthens accountability, transparency, and response effectiveness. The proposed framework contributes to cybersecurity research by extending Zero Trust principles beyond traditional enterprise environments into autonomous ecosystems. It bridges technical threat detection with governance-driven decision-making, creating a resilient and scalable security architecture for future AI-enabled infrastructures.

---

## uid: `doi:10.2139/ssrn.6748026`

- title: FROM COPILOT TO COMMANDER: A Framework for Classifying Agentic AI Adoption Maturity in Enterprises
- authors: Satya Kiran Cherukuri
- affiliations: not stated
- posted: 2026-05-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6748026
- keyword hits: agentic

### abstract

As enterprises deploy AI systems that act autonomously-executing workflows, making recommendations, and completing consequential tasks with limited human oversight-existing AI maturity frameworks provide insufficient guidance for the governance challenges this autonomy introduces. This paper proposes the Agentic AI Adoption Architecture (4A) Framework, a practical typology that helps enterprise leaders classify their agentic AI deployments across four configurations-Augmentor, Copilot, Delegate, and Commander-and understand the governance architecture each configuration requires. Drawing on practitioner experience, we introduce the Agent Governance Artifact (AGA): an organizational instrument that encodes customer entitlements, operational constraints, and accountability boundaries directly into agent behavior, enabling enterprises to advance agentic AI maturity without accumulating governance risk. Leaders who treat agentic AI deployment as an organizational transformation-not merely a technical upgrade-will be better positioned to derive strategic value from autonomous AI while maintaining the accountability structures their stakeholders require.

---

## uid: `doi:10.2139/ssrn.6735760`

- title: From Prediction to Agency: A Constrained Decision Framework and Governance Stack for Agentic AI in Clinical Diagnostics
- authors: Yunguo Yu
- affiliations: not stated
- posted: 2026-05-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6735760
- keyword hits: agentic

### abstract

Clinical artificial intelligence systems are transitioning from predictive tools that generate diagnostic outputs for human interpretation to agentic systems capable of autonomous multistep action within clinical workflows, including ordering laboratory tests, initiating medication reconciliation, and updating patient records. Existing trust frameworks, designed for advisory systems and built on output verification and confidence calibration, do not address the governance requirements of autonomous action. We identify an agency gap: the structural mismatch between validated predictions and unvalidated action policies. Using a partially observable constrained decision process (PO-CDP) formalism, we establish the principle of agency nontransferability, demonstrating that trust calibrated at the diagnostic level does not imply safe or appropriate action policies under real-world clinical, institutional, and legal constraints. To address this gap, we propose a three-layer governance stack-epistemic soundness, policy safety, and institutional traceability-that provides verifiable guarantees at each stage of the agentic decision pipeline. A compositional risk analysis reveals that individually safe components can produce unsafe system-level behavior through nonlinear error propagation. An extended backcasting roadmap defines three empirically testable phases for the transition to governed agentic systems: sandboxed action proposals (2027-2029), credentialed policy systems (2030-2032), and supervised autonomy (2033-2035). The transition to agentic clinical AI constitutes a paradigm shift from prediction correctness to policy safety under constraint, requiring institutional design rather than technical improvement alone.

---

## uid: `doi:10.2139/ssrn.6689681`

- title: From Information Retrieval to Agentic Action A Framework for Brand Visibility in AI-Mediated Markets
- authors: Marcos Guimaraes Figueira
- affiliations: not stated
- posted: 2026-05-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6689681
- keyword hits: agentic

### abstract

The competitive ground of digital visibility has moved twice in eighteen months. The first move was from the ten blue links to the AI-generated answer; the second, still in progress, is from the answer to the autonomous action. This article develops a framework that integrates three optimization disciplines emerging in response to that shift-Answer Engine Optimization (AEO), Generative Engine Optimization (GEO), and Agentic Optimization (AgO)-under a single theoretical lens: delegated consumer-AI agency. Building on Puntoni et al.'s (2021) experiential perspective on consumer AI and Davenport et al.'s (2020) account of AI in marketing, we treat the AI assistant not as a channel but as a delegated decision-maker whose choices are governed by retrievability, attribution cost, and embedded brand associations. We argue that the central strategic risk of this transition is brand erasure-the systematic elimination of brand identity from synthesized answers and completed agentic actions-and we develop six propositions that link content and infrastructure choices to brand outcomes in this environment. We close with managerial implications for brands operating across the dual audience of human readers and machine intermediaries, and a research agenda focused on measurement, audit methods, and governance.

---

## uid: `doi:10.2139/ssrn.6755043`

- title: SAMD-VGP: Seeking Alignment and Maintaining Distinctions in Vision Graph Prompting
- authors: Zeyang Zhang, Hanyang Meng, Rui Ding, Xiang Zhang, Li Peng
- affiliations: not stated
- posted: 2026-05-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6755043
- keyword hits: prompting

### abstract

Vision Graph Neural Networks (ViGs) represent images as graph structures, enabling flexible modeling of irregular long-range semantic dependencies. Vision Graph Prompting (VGP) further introduces learnable prompts into visual graphs for parameter-efficient adaptation with frozen backbones. However, existing VGP methods often treat prompt nodes as additional trainable parameters indirectly optimized by downstream losses, without explicitly modeling their roles in visual graph semantics. Consequently, prompt nodes struggle to establish stable global semantic correspondence with visual graphs and to form clear aggregation--separation structures in the local semantic space, limiting their representation quality and discriminative capability. To address this issue, we propose Seeking Alignment and Maintaining Distinctions in Vision Graph Prompting (SAMD-VGP), which reformulates visual graph prompt learning as semantic coupling between prompt nodes and visual graphs, transforming prompt nodes into interpretable semantic anchors. The Seeking Alignment module models graph-level semantic matching between prompt and visual representations to enhance global semantic correspondence. The Maintaining Distinctions module leverages cluster-aware local semantic organization with aggregation and separation constraints, encouraging prompt nodes to approach relevant semantic clusters while preserving discriminability. Extensive experiments on visual and graph classification benchmarks show consistent improvements. Ablation studies and visualizations further confirm stronger prompt--visual graph semantic associations and improved downstream adaptation.

---

## uid: `doi:10.2139/ssrn.6699098`

- title: The Environmental Gap in Agentic AI Governance: Why Human Oversight Fails Without Pre-Deployment Infrastructure Assessment
- authors: Patsy Nwogu
- affiliations: not stated
- posted: 2026-05-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6699098
- keyword hits: agentic

### abstract

Emerging governance frameworks across major jurisdictions agree that human oversight is primary to the safe deployment of Agentic AI, particularly for high-risk systems. The EU AI Act (Article 14), the NIST AI Risk Management Framework, and the African Union's Continental AI Strategy all share a common concern: allowing AI systems to operate autonomously, without human interference to monitor outputs or pause wrong processes, creates real risks to human safety and fundamental human rights. More important is the question of accountability and liability when an AI system delivers a wrong or harmful response. Human oversight creates the opportunity for shared liability and meaningful human accountability. This paper does not dispute these principles; in fact, it agrees with the logic. What it questions is the assumption that the conditions enabling effective human oversight are stable and reliably present. Governance frameworks treat oversight as a design feature, something you build into a system once and can thereafter depend on. In theory, it can be permissible, but in practice, environmental conditions that influence human oversight are rarely stable. Connectivity drops, institutions are under-resourced, and operators are fatigued or undertrained. The human in the loop is only as effective as the conditions surrounding them. The argument is built on four pieces of evidence. First, a deployment incident I led involving an agentic voice system at a career event in an underground venue with unstable network connection. That incident is a real-world case showing how infrastructural gaps can directly undermine oversight in ways no governance framework anticipates. Second, the paper draws on existing peer-reviewed scholarship on Article 14, automation bias, African AI governance, and the Brussels Effect, which already documents the inadequacies of current frameworks. This paper extends that body of work rather than starting from scratch. Third, it examines published evidence on global infrastructure conditions, particularly within the Global South, and how those conditions shape the real-world deployment of agentic systems. Fourth, and most significantly, the findings of Dagstuhl Seminar 25272, which interrogated where the EU AI Act falls short and identified environmental factors as one of three conditions for effective human oversight, providing the scholarly validation that sits at the centre of this paper's position. The paper also proposes a Policy of Functional AI built on two pre-deployment requirements. First, that systems be assessed against the environment they will actually meet, not the one in which they were tested. Second, that systems be capable of signalling functional breakdown in time for oversight to prevent harm rather than document it. The contribution is positioned as a framework design proposition, with implications for both high and low risk systems within infrastructure-volatile deployment contexts.

---
