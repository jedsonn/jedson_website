# Classification batch 396 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-396.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6955443`

- title: Forecasting Agentic Commerce: How Compute Tokenization Reshapes Transaction Mechanisms in Autonomous Agent-to-Agent Economies
- authors: Jie Gao
- affiliations: not stated
- posted: 2026-06-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6955443
- keyword hits: agentic

### abstract

Forecasts of agentic commerce increasingly emphasize the capability trajectory of large AI models, yet realized economic value also depends on whether autonomous agents can discover counterparties, compare offers, authorize transactions, verify performance, and settle payments at machine speed. This conceptual article develops the Compute Tokenization-Transaction Mechanism Transformation (CT-TMT) framework to explain how tokenized compute may become a transaction infrastructure for autonomous agent-to-agent (A2A) economies. Drawing on transaction cost theory, token economics, platform ecosystem theory, and technology-forecasting research, the framework theorizes that compute tokenization operates through three antecedent mechanisms-standardization, financialization, and programmability-that reshape four transaction-mechanism dimensions: price discovery, settlement architecture, trust and verification, and identity and authorization. These mechanisms influence efficiency, market liquidity, resilience, and accountability, while their effects are moderated by technical heterogeneity, regulatory clarity, and market-structure concentration. The article contributes to technology forecasting by treating transaction-mechanism maturity as a mediating variable between AI capability and realized agentic-commerce value. It further extends transaction cost theory to high-frequency algorithmic governance, clarifies compute tokens as capacity-linked productive claims rather than generic crypto-assets, and specifies leading indicators for tracking the 2026-2032 evolution of agentic commerce. A morphological foresight analysis develops three internally consistent scenarios-tokenization-dominant, hybrid equilibrium, and centralized resurgence-and identifies observable signals that can be used in future empirical and Delphi-based forecasting research.

---

## uid: `doi:10.2139/ssrn.6955512`

- title: Domain-Adaptive Physics-Informed Transformer for SMR OTSG
- authors: Khan Awais, Jihong Shen, Bo Wang, Shujuan Wang, FAZLE HASEEB, Syed  Abbas Ali Shah, Asim Khan
- affiliations: not stated
- posted: 2026-06-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6955512
- keyword hits: transformer model

### abstract

The operational optimization of Small Modular Reactors critically depends on accurate real-time monitoring of Once-Through Steam Generators. Complex thermo-fluid phenomena within OTSGs present significant modeling challenges, making high-fidelity simulations computationally prohibitive; meanwhile, conventional data-driven models suffer from out-of-distribution generalization failure. To bridge this gap, this study proposes a novel Domain-Adaptive Physics-Informed Transformer model enhanced with a systematic transfer learning framework. The model integrates three key innovations: multi-scale spatial discretization (z-binning) focusing on the critical boiling zone, a dual-head architecture for simultaneous prediction of field distributions and outlet temperatures, and physics-based regularizers enforcing thermodynamic consistency, specifically a total-variation smoothness penalty and a monotonicity constraint grounded in the Second Law of Thermodynamics. The proposed model demonstrates consistent and significant superiority over strong baseline models such as Long Short-Term Memory, Autoencoder with Attention, and Feedforward Neural Network, achieving near-perfect accuracy (R2 = 0.998–0.999) for outlet temperatures, phase void fraction, axial temperature, and velocity magnitude, while maintaining remarkable robustness under 2%–10% additive sensor noise. After pre-training on source-domain simulation data, the model is fine-tuned using 10%–90% of target-domain data and attains strong performance with only 50%–60% of target data, demonstrating exceptional data efficiency. Ablation experiments confirm the individual contribution of each architectural component, and evaluation on unseen target-domain data validates robust cross-domain generalization. This work provides a practical, deployment-ready framework demonstrating that physics-aware deep learning, coupled with strategic transfer learning, can yield highly adaptable and reliable surrogate models for nuclear engineering applications.

---

## uid: `doi:10.2139/ssrn.6957290`

- title: Physics-informed Tandem Neural Network for Rapid and Accurate Temperature History Prediction in Polymer Composite Extrusion-based Large-Format Additive Manufacturing
- authors: Eonyeon Jo, Nooshin Rajabi, Bhagya Prabhune, Subhadeep Chakraborty, Halil Tekinalp, Uday  K. Vaidya, Seokpum Kim
- affiliations: not stated
- posted: 2026-06-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6957290
- keyword hits: fine-tuning

### abstract

Large-format additive manufacturing (LFAM) using polymer composites enables the fabrication of massive, load-bearing structures without the need for traditional tooling. However, the continuous deposition of large thermal masses introduces severe temperature management challenges. Improper layer times lead to inadequate temperature histories, resulting in poor interlayer bonding or structural collapse. Real-time temperature history prediction is critical for thermal management, yet high-fidelity finite element analysis is too computationally expensive, and purely data-driven models lack physical consistency and generalizability without massive datasets. To overcome these limitations, this study proposes a novel Physics-Informed Tandem Neural Network (PITNN) framework to rapidly and accurately predict the temperature history during the LFAM using polymer composites. The PITNN architecture couples an Inverse Model, which identifies latent boundary conditions from an initial 30-second temperature observation, with a Forward PINN that embeds physical loss to predict the entire temperature history. To resolve the simulation-to-reality gap, the network is fine-tuned using experimental measurements. When compared to experimental data, the baseline 1D reduced-order model exhibited mean absolute errors (MAE) between 7.2°C and 12.2°C, while the un-tuned PITNN showed an MAE of 11.7°C to 13.0°C. Following experimental fine-tuning, the PITNN successfully captured the complex real-world thermal dynamics, drastically reducing the MAE to 2.2–2.5°C with an R² exceeding 0.98. Crucially, the model performs these predictions with an inference time of just 2.3 ms. This speed and accuracy demonstrate that the PITNN is an effective digital twin framework, fully capable of enabling real-time layer time optimization and closed-loop thermal control in extrusion-based LFAM.

---

## uid: `doi:10.2139/ssrn.6855918`

- title: Designing Accountability In: Technical Architecture and Human Oversight Across AAMM Levels
- authors: Alexander Huseby
- affiliations: not stated
- posted: 2026-06-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6855918
- keyword hits: agentic

### abstract

The first two papers in this series established that AI decision-making authority is expanding across organizations faster than governance frameworks can keep pace, and applied the AI Authority Maturity Model (AAMM) to documented enterprise deployments to demonstrate the consistency of this pattern. This paper addresses the underlying technical question: how does system architecture itself enable or undermine human oversight, and what specific engineering practices are required to maintain accountability at each AAMM level? The paper introduces a distinction between governance (organizational policy) and guardrails (technical enforcement), and argues that this distinction is consequential: governance without guardrails is unenforceable, while guardrails without governance are arbitrary. Drawing on the NIST AI Risk Management Framework (2023), the EU AI Act's Article 14 human oversight requirements, the 'Moffatt v. Air Canada' (2024) liability ruling, and documented software engineering patterns in agentic AI systems, the paper maps specific technical mechanisms-domain bounding, human-in-the-loop interrupt architecture, circuit breakers, immutable audit trails, and output guardrails-to the AAMM levels at which they become necessary rather than optional. The central argument is that accountability must be designed into AI systems at the architectural level, not retrofitted after deployment, and that the choice of architecture is itself a governance decision with measurable legal and operational consequences.

---

## uid: `doi:10.2139/ssrn.6956768`

- title: Performance-based GenAI Regulation: A Neuro-symbolic framework to bound public AI
- authors: Ido Sivan-Sevilla, Allen  Daniel Sunny, Liat Peterfreund
- affiliations: not stated
- posted: 2026-06-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6956768
- keyword hits: ai agent

### abstract

Governments are increasingly using GenAI to complete daunting tasks and improve the pace and efficiency of bureaucratic decision making. In this process, there is an inevitable trust in the probabilistic nature of AI models, assuming they would correctly parse agency requirements and complete their tasks according to the laws that mandated them in the first place. Building on our previous attempt to formalize legal requirements and verify the legal accountability of public algorithmic governance, we introduce formalization methods from computer science to build a neuro-symbolic framework as a policy response to verify GenAI behavior. Instead of the never-ending struggle to understand AI model internals, we suggest an approach that circumvents the ‘black box’ and tests for the legality of agent behavior. We demonstrate the validity of our approach by answering needs that come from specific use cases of GenAI deployment by the Federal Social Security Administration (SSA) agency. Our novel and robust methodology builds on various techniques for creating terminologies of the social security law and takes advantage of flexible, and uncertainty-aware logic to model the required behavior of GenAI in the service of the government. Our approach automatically verifies the compliance of AI agents with social security policies. It flags to government operators when their agents violated required processes to determine social security eligibility, or when social security eligibility requirements are non-deterministic and require careful attention when determined by an AI agent.

---

## uid: `doi:10.2139/ssrn.6962768`

- title: Transferable Fault Diagnosis for E-Motor-Driven Centrifugal Pumps via Fine-Tuning TSFM
- authors: Yingwei Qian, Xiaohong Liu, Xudong Wang, Zeyan Sun, Mingjun Tang
- affiliations: not stated
- posted: 2026-06-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6962768
- keyword hits: fine-tuning, foundation model

### abstract

As critical components of naval vessels, E-motor-driven centrifugal pumps are essential for onboard cooling and fluid circulation, yet their reliable fault diagnosis remains challenging under scarce fault samples, varying operating conditions, and limited model generalization. To address these issues, this paper proposes a transferable fault diagnosis framework based on a pre-trained time series foundation model (TSFM). Vibration signals are first represented as compact multi-domain feature sequences extracted from the time, frequency, and time-frequency domains, and then fed into the TSFM for fault classification. A low-rank adaptation (LoRA)-based fine-tuning strategy is employed to reuse pre-trained temporal representations while updating only a limited number of trainable parameters. To enhance few-shot cross-condition transfer, a Residual-Anchored Support Augmentation (RASA) module is further introduced to enrich target support distributions by anchoring source-domain intra-class residual variations around few-shot target samples. The proposed framework is evaluated under single-condition, few-shot, cross-condition, and cross-dataset diagnostic scenarios, and is deployed on the Huawei Atlas 200I A2 edge platform to verify real-time feasibility. Experimental results demonstrate that the proposed method achieves stable, transferable, and edge-deployable fault diagnosis performance with limited labeled samples.

---

## uid: `doi:10.2139/ssrn.6874778`

- title: EU AI Act Article 50 Compliance for Agentic AI: Nine Unresolved Engineering Questions and Architectural Solutions for Developers (2026)
- authors: Vinita Silaparasetty
- affiliations: not stated
- posted: 2026-06-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6874778
- keyword hits: agentic

### abstract

The EU AI Act's Article 50 transparency obligations apply from 2 August 2026. Every published compliance guide addresses single-model chatbots. None address agentic AI: autonomous multi-step pipelines involving multiple models, tool calls, sub-agents, and asynchronous interactions where the compliance assumptions embedded in Article 50 break down structurally. This paper identifies nine engineering questions that current Article 50 guidance leaves unanswered for agentic AI developers and proposes six concrete architectural patterns implementable with current tooling. Questions cover emergent systemic risk in chained non-systemic components, bidirectional deception risk in autonomous agent communications, compliance liability at client handover, asynchronous agent-to-recipient disclosure, and the proportion of AI-generated content that triggers marking obligations in composite RAG outputs. The Digital Omnibus provisional agreement of May 2026 extended the Article 50(2) machine-readable marking deadline to 2 December 2026 for existing systems. Article 50(1) interaction disclosure remains enforceable from 2 August 2026 with no extension. Submitted as a formal practitioner contribution to the European Commission's Article 50 consultation (closed 3 June 2026) from the perspective of an agentic AI developer and AI governance engineer.

---

## uid: `doi:10.2139/ssrn.6962202`

- title: EL-DBT: An Enhanced-Loss Dual-Branch Transformer Model for Predicting the Propagation of Internal Solitary Waves in the Northern South China Sea
- authors: Peiqi Yang, Shengming Cheng, Hao Yu, Jichao Wang
- affiliations: not stated
- posted: 2026-06-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6962202
- keyword hits: transformer model

### abstract

Internal solitary waves are highly active in the northern South China Sea, posing significant challenges for their dynamic forecasting. Based on MODIS remote sensing imagery, GEBCO, and HYCOM data, this study proposes an Enhanced Loss Dual-Branch Transformer (EL-DBT) model to intelligently forecast the speed, direction, and trajectory of internal solitary waves. The EL-DBT model learns speed and direction features through two parallel branches and introduces a joint loss function comprising Huber speed loss, direction vector loss, and angular consistency loss to improve prediction accuracy. The EL-DBT model achieved an RMSE of 0.143 m/s and an R² of 0.962 for the speed branch, and an RMSE of 5.402° and an R² of 0.923 for the direction branch. In one-tidal-cycle forecast, the EL-DBT model’s MEAN_APE was 5.018 km, and the Fréchet distance was 9.326 km. and for two-tidal-cycle forecast, the MEAN_APE was 7.758 km, and the Fréchet distance was 18.629 km. The above evaluation metrics indicate that the EL-DBT model outperforms traditional Transformer, BP, LSTM, and Random Forest models. Robustness analysis further confirms the model’s stability under input perturbations. This study demonstrates that the EL-DBT model provides an effective remote sensing-driven method for the intelligent forecasting of internal solitary waves propagation trajectories.

---
