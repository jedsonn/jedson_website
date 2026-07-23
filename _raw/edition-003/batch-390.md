# Classification batch 390 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-390.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6812599`

- title: Classification as Architecture: A Foundational Defense Layer for Sovereign Agentic AI
- authors: John Larson
- affiliations: not stated
- posted: 2026-06-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6812599
- keyword hits: agentic

### abstract

Current agent governance frameworks govern actions: which tools an agent may invoke, which resources it may access, whether its behavior remains within a trust budget. Regulated deployment requires a different question. Which data may flow to which model, under what classification, assembled from which sources? This paper develops the answer as an architectural property of the deployment rather than a policy assertion about it. We propose classification-as-architecture (CaA): every contributing fragment of an agent's inference context carries a classification label, bound to the fragment's storage object or loader capability, assembly produces a context whose classification is the maximum of contributing labels, and the routing layer is structurally incapable of constructing an inference request whose context classification exceeds the authorized tier of the target model. The test is sharp. An authorized agent acting in good faith cannot route higher-classification content to an unauthorized model tier by normal-path behavior. Not because policy would flag it. Because the request fails to construct. The thesis is one layer of a layered defense, not a standalone answer. Classification-as-architecture prevents structural leaks before inference begins. Action-governance frameworks, runtime guardrails, and audit layers catch behavioral leaks above the architectural foundation. Published frameworks (the Microsoft Agent Governance Toolkit, Singapore IMDA's agentic AI framework, the NIST AI RMF, OWASP Agentic Top 10) are examples of those upper layers, being rapidly adopted by industry as of this writing. A coverage analysis of nine current frameworks against a four-axis sovereignty decomposition (infrastructure, data, intelligence, operator) finds zero Full ratings on the Sovereign Intelligence and Sovereign Operator axes, a systematic gap that classification-as-architecture is one structural response to. The thesis is necessary for organizations with a genuine requirement to prevent classified data leakage (regulated finance, defense, healthcare, IP-sensitive deployments). Organizations without that requirement may adopt action-governance alone or not at all; this paper takes no position on their architecture..

---

## uid: `doi:10.2139/ssrn.6834138`

- title: A Risk-Stratified Governance Framework for Agentic AI in the Conduct of Human Subjects Research
- authors: Allison Curry, Johnathon  P. Ehsani
- affiliations: not stated
- posted: 2026-06-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6834138
- keyword hits: agentic

### abstract

Prevention research produces evidence that reduces disease and injury burden, yet recruitment, consent, and follow-up move through manual, disconnected workflows that limit pace, scale, and consistency. Agentic AI—systems carrying out multi-step tasks within human-set rules—may accelerate these workflows and broaden participant engagement. In 2022, the Secretary's Advisory Committee on Human Research Protections concluded that 45 CFR 46.116—the federal regulation governing informed consent—is ill-suited to AI-involving research. Although the National Institute of Standards and Technology, the World Health Organization, and recent clinical research guidance offer general principles for oversight, transparency, and lifecycle review, none specify how oversight should scale with what an agentic system does and how closely a human supervises it during day-to-day research operations. In this paper, we propose a risk-stratified framework crossing three functional tiers with three oversight stages. Tiers distinguish back-end infrastructure (Tier 1), staff support and low-risk logistics (Tier 2), and substantive participant-facing functions (Tier 3); stages move from review of every interaction (Stage 1) to sampling-based audit (Stage 2) to fully autonomous operation (Stage 3). Movement to less supervision requires performance equivalent to the current standard, with pre-specified thresholds for comprehension, voluntariness, and equitable performance across important strata (e.g., language, literacy, disability). The IRB holds final classification authority, and fully autonomous Tier 3 deployment is deferred pending ethics review and direct empirical evidence in research operations. We offer the framework as a starting point for that conversation—model- and platform-agnostic, an initial baseline open to refinement rather than a finished standard, and written for investigators, IRBs, sponsors, and institutional AI governance bodies.

---

## uid: `doi:10.2139/ssrn.6875178`

- title: TruKT-Seg: A Trustworthy Knowledge Transfer Framework for Semi-Supervised Industrial Defect Segmentation under Low-Annotation Regimes
- authors: Pan Jiang, Rencheng Song, Liwei Zhang, Hongsen Xiong, Huangan Xu, Liang Huang, Haojie Xia, Jin Zhang
- affiliations: not stated
- posted: 2026-06-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6875178
- keyword hits: foundation model, prompting

### abstract

The prohibitive cost of pixel-level annotation has made semi-supervised learning a practical necessity for industrial defect segmentation, while real-time inference remains a stringent deployment requirement. However, existing semi-supervised methods lack explicit control over the reliability of transferred structural priors in regions with blurred boundaries and tiny defects, causing pseudo-label noise to be progressively amplified during training. To address this issue, a trustworthy knowledge transfer framework (TruKT-Seg) is proposed for low-annotation industrial defect segmentation. During training, a foundation model is introduced as an external source of structural priors, and a dual-reliability mechanism is designed to decouple prior utilization into reliable acquisition and reliable absorption. Specifically, evidential learning is used to construct a reliability-oriented knowledge representation for the student, based on which query reliability and an uncertainty-adaptive budget select reliable semantic anchors for reliability-aware prompting, while transfer reliability controls how strongly the queried priors should be absorbed. On this basis, trustworthy knowledge transfer is achieved through reliability-aware query selection, distribution matching, and spatial-semantic student refinement. Experiments on three industrial defect segmentation benchmarks demonstrate that TruKT-Seg achieves superior segmentation performance under low-annotation settings. In particular, 81.92% mean Intersection-over-Union is achieved at 45.96 frames per second on a representative industrial defect segmentation dataset with only 10% labeled data, demonstrating a strong balance between segmentation accuracy and real-time efficiency.

---

## uid: `doi:10.2139/ssrn.6812342`

- title: After the Breach: Cyberattacks and the CEO Risk-Taking Incentives
- authors: Brian Yang, Eun Kyung Lee, Quynh Nga Le, Nhan Huynh
- affiliations: not stated
- posted: 2026-06-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6812342
- keyword hits: prompting

### abstract

This study examines whether cyberattacks reshape CEO risk-taking incentives. Using U.S. public firms and actual cyber incident data, we construct a propensity-score-matched sample and estimate difference-in-differences models. We find that firms significantly reduce CEO Vega after cyberattacks, indicating a decline in option-based risk-taking incentives. The effect is stronger for CEO Flow Vega, suggesting that boards primarily adjust newly granted option compensation rather than accumulated option holdings. Dynamic analyses show no evidence of pre-trends, while the post-attack decline strengthens over time. Mechanism tests reveal that firms reduce option grants and increase restricted stock compensation, while CEO Delta remains largely unchanged, indicating a targeted reduction in compensation convexity rather than a broad weakening of pay-performance alignment. The effect is stronger for severe, visible, and sensitive breaches, and for firms with higher cyber-risk exposure and stronger growth opportunities. Overall, the findings suggest that cyberattacks serve as governance shocks, prompting boards to redesign CEO compensation toward more conservative risk-taking incentives.

---

## uid: `doi:10.2139/ssrn.6878910`

- title: Multi-Scale Factor-Integrated BA-LSTM Model for Medium- to Long-Term Runoff Forecasting Across Multiple Basins
- authors: Jinggang Chu, Lei Ye, Wenyu Ouyang, Xiangyi Le, Lei Zhang, Rijie Huang
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6878910
- keyword hits: fine-tuning

### abstract

Against the backdrop of climate change, medium- to long-term runoff forecasting is crucial for water resources management. While deep learning models, particularly Long Short-Term Memory (LSTM) networks, have shown substantial promise in unified multi-basin modeling, they struggle to capture the spatially heterogeneous impacts of global- and astronomical-scale teleconnection factors. To address this gap, we propose the Basin-Aware Long Short-Term Memory LSTM (BA-LSTM), which introduces a dynamic feature modulation module based on static basin properties. For the first time, global and astronomical factors are explicitly incorporated into a unified multi-basin modeling framework, equipped with learnable basin-aware weights that modulate the heterogeneous sensitivities of different basins to identical macroscopic forcings. Tested across 669 basins globally, the BA-LSTM achieved a median testing Nash-Sutcliffe Efficiency (NSE) of 0.776, outperforming both local basin-by-basin models with an NSE of 0.706 and traditional global LSTM architectures with an NSE of 0.698, representing improvements of 9.9% and 11.2%, respectively. Spatially, the proposed framework demonstrated exceptional robustness across diverse continental hydro-climatic regimes, effectively mitigating the regional predictive biases inherent in traditional modeling. Furthermore, we demonstrated the model’s strong cross-basin generalization through transfer learning in data-scarce regions of China, specifically the Songhua River and Wu River basins, where a fine-tuning strategy leveraging global pre-trained weights significantly improved predictive reliability over local benchmarks by achieving testing NSE values of 0.791 and 0.874, respectively. Finally, an Integrated Gradients (IG) analysis was conducted to interpret the internal model sensitivity, revealing that basin-scale factors dominate, with precipitation contributing approximately 50% of the relative sensitivity, while explicit multi-scale varying feature importance within the trained BA-LSTM is captured. Our findings provide a robust and interpretable framework for integrating multi-scale forcings into large-sample hydrological modeling.

---

## uid: `doi:10.2139/ssrn.6876241`

- title: Parameter-Efficient Fine-Tuning for Multimodal Fusion: A Survey of Injection-Driven Integration Mechanisms
- authors: Yin Rong, Zhuoyifan Zhang, Xiaoshuai Hao, Jian Li, Haichao Shi, Haoran Li, Hao Peng, Yu Liu
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6876241
- keyword hits: fine-tuning, foundation model

### abstract

Multimodal information fusion has become a fundamental paradigm for enabling comprehensive understanding and generation across heterogeneous data sources. Recent advances in multimodal foundation models (MFMs) have significantly improved cross-modal learning capabilities; however, their massive parameter scale poses critical challenges for efficient adaptation, including prohibitive computational costs and the risk of disrupting pre-trained cross-modal alignments. In this survey, we present a comprehensive review of parameter-efficient fine-tuning (PEFT) for multimodal models from the perspective of information fusion. Specifically, we view PEFT as a set of parameterized fusion mechanisms that regulate how multimodal information is aligned, interacted, and integrated within pre-trained architectures. Based on this view, we systematically categorize existing approaches into four paradigms: additive injection for explicit feature-level fusion, reparameterization for implicit cross-modal coupling, input-level parameterization for semantic-guided fusion, and advanced collaborative methods for adaptive and context-aware fusion.Furthermore, we analyze these paradigms from multiple perspectives, including task adaptability, parameter efficiency, and structural flexibility, highlighting the trade-offs in designing multimodal fusion strategies. We also discuss key challenges in multimodal fusion, such as mitigating modal disparity and enhancing cross-modal alignment under constrained adaptation. Finally, we outline promising future directions toward scalable, adaptive, and intelligent multimodal fusion systems.This survey provides a unified perspective on multimodal PEFT through the lens of information fusion, offering practical insights for developing efficient and robust multimodal learning systems.

---

## uid: `doi:10.2139/ssrn.6878983`

- title: Greening the deal: Can Mergers Redirect Innovation?
- authors: Melissa Newham, David Jaggi, Jan-Alexander Posth
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6878983
- keyword hits: text embedding

### abstract

This paper examines how mergers and acquisitions (M&As) affect the direction of corporate innovation. Using data on U.S. M&A transactions from 1988–2015 matched with detailed patent data, we construct novel measures of changes in the technological orientation of acquirers based on patent text embeddings. We estimate dynamic treatment effects in a staggered difference-in-differences framework that compares merging firms to matched controls over a 17-year period, centered on the deal announcement year. We find a large and statistically significant shift in the acquirer's innovation direction toward the target’s knowledge base post-deal. This positive effect is driven by deals between acquirers and targets that operate in technologically distinct domains. Using a subsample of deals involving targets that hold clean patents, we find that “dirty” acquirers—firms whose patent portfolios are concentrated in dirty technologies—show particularly strong post-deal shifts toward their target’s clean technologies, accompanied by increased citations to the target’s clean patents and increased clean patent filings by the acquirer. Overall, our results point to the potential for M&A to reshape innovation trajectories and mitigate against path dependencies.

---

## uid: `doi:10.2139/ssrn.6867525`

- title: STAR: Mitigating Hallucinations in Vision-Language Models through Object-Centric Prompting
- authors: Jianbing Ma, Haoge Han
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6867525
- keyword hits: prompting, qwen

### abstract

Large Vision-Language Models (LVLMs) have achieved remarkable success in visual understanding tasks, yet persistent object hallucinations remain a critical bottleneck for their reliable deployment. Existing mitigation strategies often suffer from high computational costs or the inherent resolution constraints of visual encoders. We propose a lightweight and training-free Spatial Truth-Anchored Recognition (STAR) framework designed to suppress hallucinations by leveraging CNN-based object detection priors. Our approach systematically integrates structured object-level evidence---including category labels, spatial coordinates, and confidence scores---directly into the reasoning prompt. The framework operates through a synergistic two-stage mechanism: global context alignment to establish robust visual anchors, and adaptive local verification via high-resolution cropping for low-confidence regions. Extensive experiments on the MME, POPE, and CHAIR benchmarks demonstrate that STAR consistently outperforms state-of-the-art decoding-time interventions across various model scales, including Gemma-3 and Qwen-3.5-VL. Our results provide empirical evidence that explicit object-centric anchors effectively counteract the dominance of statistical language priors, offering a generalizable and efficient solution for enhancing the factual grounding of LVLMs.

---
