# Classification batch 406 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-406.answer.json` as a JSON array.

---

## uid: `arxiv:2607.03863v2`

- title: Rethinking Scientific Discovery in the Agentic Era
- authors: Yining Zheng, Yuxin Wang, Jiahao Lu, Shicheng Fang, Weiyi Wang, Yongzhuo Yang, Bowen Li, Haochen Ma
- affiliations: not stated
- posted: 2026-07-04
- source: arXiv
- link: https://arxiv.org/abs/2607.03863v2
- keyword hits: agentic

### abstract

Artificial intelligence has advanced scientific discovery, but most AI4Science systems remain fragmented tools that rely on humans to coordinate problem formulation, literature grounding, model use, simulation, validation, and knowledge reuse. This paper presents \textbf{SCION (Scientific Collaborative Innovation with Agentic Organizational Nexus)}, an agentic scientific operating system that acts as an \textbf{organizational nexus}. Through a Science Agent serving as a \textbf{Meta-Harness}, SCION connects scientific tasks, tools, agents, artifacts, and memory, transforming research into an executable, auditable, and reusable operational process. At its core is the \textbf{Research Execution Plan (REP)}, which compiles high-level scientific intent into staged objectives, dependencies, verification checkpoints, tool requirements, expected artifacts, and fallback conditions. SCION further integrates hierarchical multi-agent execution, profile-driven specialization, selective context construction, governed delegation, and layered epistemic memory to support long-horizon scientific work. We formulate discovery under SCION as \textbf{Target-conditioned Inverse Search} and extend it to hidden-target settings through batch active search under finite experimental budgets. Applications in materials analysis, molecule design, and protein or antibody screening, together with experiments on scientific reading, idea generation, molecule generation, and antibody screening, show that SCION outperforms existing autonomous research-agent baselines, especially in decomposition, verification, refinement, and memory reuse. Overall, SCION shifts AI from isolated tools toward a coordinated operational layer for traceable and reusable scientific innovation.

---

## uid: `arxiv:2607.03703v1`

- title: Explainable Reinforcement Learning for Adaptive Traffic Signal Control
- authors: Dickens Kwesiga, Nishu Choudhary, Angshuman Guin, Michael Hunter
- affiliations: not stated
- posted: 2026-07-04
- source: arXiv
- link: https://arxiv.org/abs/2607.03703v1
- keyword hits: fine-tuning

### abstract

Reinforcement Learning (RL) has emerged as a powerful paradigm for adaptive traffic signal control. However, in safety-critical infrastructure like traffic control, the opaque, black-box nature of deep RL models poses challenges for transportation agency acceptance, regulatory compliance, operational trust, troubleshooting, and fine-tuning. To bridge this gap between high-performance optimization and human-comprehensible interpretability, this effort introduces a novel, explainable entity centric RL framework for safe and transparent traffic signal control. Rather than processing traffic states through monolithic, flat vectors, the proposed architecture disaggregates real-time intersection observations into distinct, high-dimensional lane entities and phase temporal configurations to inherently preserve the structural topology and geometric configurations of the intersection. Relational dependencies and inter-lane conflicts are dynamically extracted via a dual-stage attention network featuring sequential multi-head cross-attention and self-attention blocks. This design yields a real time affinity matrix that quantifies the direct influence of signal phases on specific approach volumes and queues, providing full visual and analytical interpretability. To ensure strict operational reliability, a deterministic action-masking interface is integrated directly into the Proximal Policy Optimization pipeline, explicitly blocking invalid phase transitions to guarantee absolute compliance with established signal timing and safety constraints. Evaluated in a microscopic simulation environment, outperforms state-of-the-art baselines in delay minimization. More importantly, the emergent attention weights align precisely with established traffic engineering principles, offering an auditable, trust-enabling, and deployable architecture for next-generation adaptive traffic control systems.

---

## uid: `arxiv:2607.03663v3`

- title: Phase-Preserving Trimodal Transformer for Tropical Forest Biomass Estimation Using Optical and PolInSAR Data
- authors: Luiz Felipe Parente Santiago, Felipe Ferrari, Daniel Rodrigues dos Santos, Rosiane de Freitas
- affiliations: not stated
- posted: 2026-07-04
- source: arXiv
- link: https://arxiv.org/abs/2607.03663v3
- keyword hits: fine-tuning

### abstract

The accurate estimation of Above-Ground Biomass (AGB) in mature tropical forests remains a critical challenge in remote sensing, primarily due to the saturation of Synthetic Aperture Radar (SAR) signals in high-density areas and persistent cloud cover affecting optical imagery. To overcome these physical limitations, we propose the Trimodal Coherent Co-attention Transformer (TCCT), a physics-informed deep learning architecture. The TCCT natively fuses optical surface reflectance (Landsat-5) with complex-valued Polarimetric SAR Interferometry (PolInSAR) data from both P and L bands. Unlike traditional fusion methods, our architecture employs complex-valued encoders to preserve spatial phase coherence, coupled with a dynamic co-attention mechanism that acts as an adaptive gating module, reducing the weight of cloud-corrupted optical pixels and shifting reliance to microwave phase data. We also derived a localized spatial allometric calibration model via Levenberg-Marquardt optimization, tailored to the specific wood density of the Paracou region in the Amazon basin. Evaluated using a two-stage protocol, the TCCT first underwent a rigorous 5-fold cross-validation to establish robust global weights (achieving a global RMSE of 4.19 m). Subsequently, following a localized spatial fine-tuning phase over 200 epochs, the model attained an absolute RMSE of 3.78 m and an $R^2$ of 0.33 for Canopy Height Models (CHM), outperforming standard Random Forest, CNN, and Vision Transformer baselines. Our ablation study confirms that preserving phase coherence mitigates deep-canopy signal saturation. When converted to AGB, the fine-tuned TCCT map yielded a Relative RMSE (rRMSE) of 4.51% in dense forest areas above 50 Mg/ha. By meeting the European Space Agency (ESA) BIOMASS mission requirement of less than 20% error, the TCCT provides a robust framework for continuous carbon stock mapping in tropical biomes.

---

## uid: `arxiv:2607.04510v1`

- title: Transplanting, inverting, and preventing a misalignment persona: method-conditional emergent misalignment in Qwen2.5
- authors: Lyndon Drake, Zandi Eberstadt
- affiliations: not stated
- posted: 2026-07-05
- source: arXiv
- link: https://arxiv.org/abs/2607.04510v1
- keyword hits: fine-tuning, qwen

### abstract

Emergent misalignment (EM) -- the broad misbehaviour a language model acquires after fine-tuning on narrow harmful data -- is mediated in Qwen2.5 models by a latent persona direction, and that direction is causal in open weights. Transplanting it into a model that shares only pretraining with its source induces broad EM (2.83 +/- 0.26% misaligned against a random-direction floor of ~1.1%), and ablating a model's own direction roughly halves an overt inducer's broadcast (21% to 10%). The transplant doubles as a measurement method, causally assaying directions that a source model represents but cannot itself express. Whether a fine-tune recruits this persona depends on method and capacity, and since low-rank PEFT is the cheaper regime at scale, the recruiting method is also the economical one. On Qwen2.5-32B, low-rank LoRA on insecure code recruits it (3.4% misaligned) while full SFT on identical data does not (0.3%) and moves against the persona axis (drift-persona cosine +0.17 at rank 1 to -0.10), the far-inducer, high-capacity exception consistent with a representational-distance x capacity account. The persona's causal role is itself conditional. Steering a bad-medical SFT run away from the direction during training raises the broadcast from 24% to 51% while a matched random control lowers it, so removing the direction is no blanket recipe. Because recruitment is a loss-reducing shortcut that capacity renders redundant, it can be screened for and prevented in the tested instances. Persona loss-relevance at the SFT solution orders four inducers' broadcasts rank-perfectly within Qwen2.5, inoculation removes recruitment selectively (4.75% to 0.0%, code coherence 65% to 87%), and fine-tuning orthogonal to the single behaviour-derived axis reduces it persona-specifically. Results are a controlled case study of one model family, single-seed in places.

---

## uid: `arxiv:2607.04292v1`

- title: Agentic SABRE: An Uncertainty-Aware Neuro-Symbolic Multi-Agent Framework for Adaptive Ransomware Detection
- authors: Henry Kabuye, Biju Issac, Jeyamohan Neera
- affiliations: not stated
- posted: 2026-07-05
- source: arXiv
- link: https://arxiv.org/abs/2607.04292v1
- keyword hits: agentic

### abstract

Ransomware has evolved into a complex, adaptive, and fast-moving adversary category in which static signatures and monolithic classifiers fail to generalise under concept drift, evasion, and behavioural polymorphism. In this paper, we present Agentic SABRE (Semantic-Behavioural Arbitration for Ransomware Evaluation), an uncertainty-aware, neuro-symbolic, multi-agent framework for adaptive ransomware detection. SABRE fuses semantic, representation-based evidence with behavioural, time-window forensic telemetry and employs Monte Carlo Dropout inference to quantify epistemic uncertainty for each agent. We introduce a decision-layer orchestrator that performs risk- and uncertainty-aware triage using two interpretable thresholds: a risk score and an uncertainty budget. High-confidence, high-risk samples are automatically contained, while uncertain or borderline cases are escalated to human analysts, establishing a flexible computational contract between autonomous response and analyst oversight. To support auditability and trust, SABRE integrates post-hoc explainability mechanisms, including gradient saliency, permutation importance, and counterfactual analysis, enabling both local and global interpretation of agent decisions. Extensive evaluation on RDset and RanSMAP demonstrates that Agentic SABRE preserves perfect discrimination on saturated semantic datasets, with AUC equal to 1.0, while improving robustness under weak behavioural signals. It achieves up to a 4.9 percent relative reduction in false escalations at equal recall while maintaining calibrated predictive uncertainty. Counterfactual analysis further shows that semantic and behavioural decisions can be reversed with bounded perturbation cost, indicating stable and interpretable decision boundaries.

---

## uid: `doi:10.2139/ssrn.7053519`

- title: Governing AI Risk in High-Stakes Deal Environments: Who Controls the Evidence Layer?
- authors: Zohra Furtado
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7053519
- keyword hits: agentic

### abstract

AI regulation is an area of active, rapid legislative change; readers should verify all dated regulatory claims against current legal sources before relying on them. Agentic and autonomous AI systems are now embedded across the entire M&A lifecycle - from deal sourcing and diligence through valuation, negotiation, closing, and integration execution. In high‑stakes deal environments, where fiduciary duties, valuation accuracy, regulatory scrutiny, and litigation exposure converge, the evidentiary obligations that attach to AI‑assisted decision‑making remain poorly understood. Under the EU AI Act and equivalent global frameworks, deployers rather than vendors bear accountability for how AI systems operate in their name, and this responsibility cannot be transferred contractually. Parallel obligations arise under long‑standing legal frameworks that predate AI regulation. Courts and tribunals assessing AI‑assisted decisions focus on reconstructability, human oversight, and professional verification duties. Recent cases across Canada, England, and the US confirm that organisations relying on AI output must evidence what the system did, how human decision‑makers engaged with it, and whether oversight met professional standards. This paper argues that control of the orchestration layer determines what evidence can be produced across all phases of M&A, and thereby determines deployer liability when AI‑assisted decisions are challenged. Vendor indemnities, representation and warranty insurance, and contractual disclaimers do not address deployer liability under Article 26 or its global equivalents. Drawing on comparative regulatory analysis, cross‑framework mapping, and a working proof‑of‑concept prototype, the paper proposes a layered governance architecture for agentic AI across the full M&A lifecycle, aligned with the EU AI Act, ISO/IEC 42001, and the NIST AI Risk Management Framework. It introduces a model-diverse defensive architecture designed to mitigate adversarial prompt risks through independent validation loops, and demonstrates how architectural choice dictates an organisation’s capacity to satisfy non-delegable evidentiary obligations when AI‑assisted deal decisions are contested.

---

## uid: `doi:10.2139/ssrn.7068293`

- title: Action-Linked Credit Assignment for Event-Driven Warehouse Management via Multi-Agentic Reinforcement Learning
- authors: Huijung Nam, Seongil Im, Junseo Lee, Changhwan Shin, Hyunsu Ju
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7068293
- keyword hits: agentic

### abstract

E-commerce fulfillment warehouses face increasing operational complexity due to rapid order growth and changing product assortments. Traditional rule-based approaches for warehouse slotting and inventory management struggle to adapt to such dynamic environments, often resulting in suboptimal performance. We propose a reinforcement learning (RL)-based framework for warehouse slotting and inventory replenishment where two decision agents interact through a shared warehouse environment within an event-driven architecture. The framework comprises a Slotting Agent (SA) for zone assignment and an Inventory Agent (IA) for replenishment decisions, trained independently and evaluated jointly in an integrated warehouse simulation. To address the delayed feedback structure caused by supplier lead times, we introduce Action-Linked Credit Assignment (ALCA), a dynamic credit assignment mechanism that directly links each replenishment order to its resulting inventory state via a unique order identifier, unlike conventional reward redistribution approaches that distribute credit across the entire trajectory. Additionally, a product embedding-based generalization mechanism enables zero-shot policy transfer to newly introduced products without retraining, addressing a key limitation of existing RL-based warehouse systems. Experimental results demonstrate that the proposed framework achieves over ten times higher cumulative reward than rule-based baselines, reducing replenishment orders by 19% and stockout ratios by 35%. In dynamic environments with new product introductions, the framework maintains stable performance while baseline methods experience severe degradation. Ablation studies confirm that ALCA is essential for learning effective replenishment policies under lead-time uncertainty.

---

## uid: `doi:10.2139/ssrn.6917378`

- title: The Universal Declaration of AI Accountability Rights (UDAAR 2026) A Doctrinal Foundation for the Global Jurisprudence of AI Accountability
- authors: Dr.Pavan Duggal
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6917378
- keyword hits: agentic

### abstract

On the fourteenth day of May, 2026, the International AI Accountability Forum (IAAF), convened at New Delhi, solemnly proclaimed the Universal Declaration of AI Accountability Rights (UDAAR 2026) as the common standard of AI accountability for all peoples and all nations. UDAAR is among the first universal instruments to translate AI ethics into AI rights, voluntary principles into binding duties, and aspirational commitments into enforceable remedies. This paper sets out the doctrinal architecture of UDAAR, situates it within the unbroken normative continuum that proceeds from the Universal Declaration of Human Rights (1948) through the digital-age instruments of the present decade, and articulates the jurisprudential innovations by which UDAAR addresses the civilizational stakes of unaccountable artificial intelligence. The paper advances five propositions. First, that accountability for the design, development, deployment, operation, and consequences of artificial intelligence systems has, by reason of its civilizational stakes, attained the character of a non-derogable principle of international law, aspirant to the status of a peremptory norm (jus cogens). Second, that the Doctrine of Attributed Accountability Across the Agentic Chain, articulated in Article 32 of UDAAR, resolves the liability vacuum opened by agentic and autonomous AI without resort to the device of AI personhood. Third, that the reversal of the burden of proof in evidentiary asymmetry, recognized in Article 38, is not a procedural concession but a substantive precondition of remedy. Fourth, that the principle of data non-refoulement, drawn by analogy from refugee law, fills a critical lacuna in transboundary AI governance. Fifth, that the prohibition of algorithmic colonialism and the affirmation of the Global South as co-architect, not rule-taker, of universal AI norms, marks the irreversible transition from a North-authored to a universally co-authored jurisprudence of artificial intelligence. The paper concludes by outlining the institutional architecture established by UDAAR, including the International AI Accountability Authority, the Global AI Incident Registry, the International AI Accountability Court or Tribunal, and the annual Conference of Parties, and identifies the implementation pathway by which UDAAR is to be operationalized across national, regional, and international fora.

---
