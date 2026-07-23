# Classification batch 41 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-41.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6586418`

- title: AI-Assisted Thinking Protocol: A Design-Based Study of Verification-First Learning
- authors: Haifa Alsubhi
- affiliations: not stated
- posted: 2026-05-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6586418
- keyword hits: chatgpt, claude, deepseek, gemini

### abstract

Current AI tutoring tools prioritize explanation delivery over understanding verification, reinforcing what Koriat and Bjork (2005) call the illusion of competence: learners believe they understand without being able to apply knowledge. This paper presents the AI-Assisted Thinking Protocol (AATP), a verification-first framework implemented as a structured prompt for generalpurpose AI systems. Rather than delivering explanations, the protocol requires learners to articulate understanding in their own words, apply concepts to novel situations, and pass transfer tests before progressing. We report on iterative protocol development across six versions and preliminary evidence from eight learning sessions conducted by two participants across two domains (mathematics for machine learning and data preparation) using five AI platforms (ChatGPT, Claude, DeepSeek, Gemini, and Copilot). Key findings include: five documented detection events in which the protocol identified and corrected shallow understanding; one participant correcting the AI during a session, indicating metacognitive development; voluntary upgrade from a simplified to the full protocol version by an external tester; 85% retention after one week without review; and zero-shot protocol absorption by Google NotebookLM, confirming behavioral distinctiveness. Limitations, design implications, and a research agenda for formal validation are discussed.

---

## uid: `doi:10.2139/ssrn.6696922`

- title: CP-CMAD: Cross-Modal Patch & CLS-Token Multi-Layer Adversarial Disruption forVision-Language Models
- authors: Sudhir  Kumar Pandey, Jianxun Mi, Israr Ahmad, Altaf Hussain
- affiliations: not stated
- posted: 2026-05-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6696922
- keyword hits: chatgpt, claude, gemini, gpt-4

### abstract

Abstract—We present CP-CMAD (Cross-Modal Patch & CLS Token Multi-Layer Adversarial Disruption), a novel white-box adversarial attack targeting the internal representation geometry of vision–language models (VLMs). Unlike prior work that disrupts final-layer embeddings via contrastive loss or simple L∞-bounded perturbations, CP-CMAD jointly attacks three complementary objectives: (i) cross-modal attention alignment between CLS tokens and patch embeddings across multiple transformer layers, (ii) the CLS token’s semantic grounding by minimising the KL divergence between its similarity distributionand the uniform distribution, thereby maximising prediction uncertainty, and (iii) cross-layer representational coherence via cosine-similarity contradiction between early and late hookedlayers. Combined with a Nesterov-accelerated momentum optimiser, dynamic semantic-drift layer weighting, and saliency guided gradient masking over a two-model ensemble (EVA02-L-14× ViT-L-14), CP-CMAD achieves 100% Attack Success Rate on MS-COCO 2014 val under both ε=5/255 and ε=12/255 budgets, reducing image-to-text and text-to-image Recall@1to 0.00%, outperforming PGD, APGD, and CW baselines by substantial margins. CP-CMAD maintains ≥75% ASR across ten input-transformation defences, including JPEG compression, bit depth reduction, randomised smoothing, and feature squeezing. Quantitative black-box transferability on three unseen encoders (SigLIP, ViT-H-14-LAION2B, ConvNeXt V2-G) reduces I2T Recall@1 by 64–71 percentage points with zero access to target weights. Qualitative evaluation across ten adversarial examples on ChatGPT (GPT-4o), Gemini 1.5 Pro, and Claude Haiku 4.5 confirms reliable cross-architecture transfer, with detection-aware models remaining vulnerable at the visual-encoder representation level. All code and adversarial examples will be released upon acceptance

---

## uid: `doi:10.2139/ssrn.6594538`

- title: From Outputs to Trajectories: Systemic Behavioral Pathologies in Large Language Models Rethinking Evaluation beyond the Output-based Paradigm
- authors: Vincenzo D'amico
- affiliations: not stated
- posted: 2026-05-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6594538
- keyword hits: large language model, large language models, llm, llms

### abstract

This paper builds on a prior conceptual analysis by the author, extending its analytical framework through a trajectory-based perspective on large language model (LLM) behavior. This paper argues that the behavior of large language models (LLMs) cannot be adequately understood through output-based evaluation frameworks, which assess individual responses in isolation. While such approaches are effective in measuring local performance, they fail to capture the temporal and interactional dynamics through which system behavior unfolds across extended exchanges. Drawing on approximately 250 hours of longitudinal interaction with a state-of-the-art LLM, this study develops a trajectory-based perspective, in which system behavior is conceptualized as an emergent process distributed across sequences of responses rather than reducible to discrete outputs. Within this framework, the paper identifies four systemic behavioral pathologies that remain largely invisible under standard evaluation protocols: Dual Standards, Constitutional AI Theater, Möbius Vulnerability, and Memory Asymmetry. These phenomena are not characterized by isolated errors, but by process-dependent distortions that emerge and stabilize across interaction trajectories. Each step in the interaction may appear locally coherent, aligned, and plausible, while the trajectory as a whole becomes epistemically unstable, normatively inconsistent, or structurally misaligned. This introduces a critical distinction between local alignment and global misalignment, revealing a fundamental limitation in current approaches to AI evaluation. The paper shows that existing evaluation practices, which rely on short, decontextualized exchanges, are structurally incapable of detecting these trajectory-level failures. As a result, system reliability may be systematically overestimated, while underlying behavioral instabilities remain unobserved. The analysis suggests that what is often interpreted as improved performance may, in fact, contribute to the invisibility of deeper structural issues. Building on these findings, the paper argues for a shift from output-centric to trajectory-aware evaluation frameworks. Such frameworks would require extended interaction testing, temporal consistency checks, and the reconstruction of interaction histories as coherent analytical objects. More broadly, the paper contributes to ongoing debates on AI alignment, governance, and epistemic reliability by introducing temporality as a central dimension in the analysis of AI systems. By reframing LLM behavior as a time-dependent process rather than a sequence of independent outputs, this work proposes a new analytical lens for understanding the limits of current AI systems and the conditions necessary for more robust and reliable forms of alignment.

---

## uid: `doi:10.2139/ssrn.6594418`

- title: Artificial Effort
- authors: Federico Belotti, Stefano Coniglio, Antonio Cosma, Francesco Fallucchi
- affiliations: not stated
- posted: 2026-05-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6594418
- keyword hits: large language model, large language models, llm, llms

### abstract

Real-effort tasks, in which participants perform cognitively costly activities whose outcomes depend on actual performance, are widely used in experimental economics. Their validity, however, rests on the assumption that a human performs them. We study whether this assumption still holds in the era of Artificial Intelligence (AI) and Large Language Models (LLMs). Using 8 canonical real-effort tasks and 23 LLMs from three major providers, we show that most tasks can now be solved accurately and at a negligible cost, while only a few resist automation. Performance improves with each model generation, and midtier models are rapidly closing the gap with frontier ones, broadening the set of widely accessible models that can automate these tasks. Additionally, we show that verbally offering monetary incentives has no effect on LLM performance. Our findings establish a boundary condition for the use of real-effort tasks in unsupervised settings: when participants can cheaply outsource task completion to an LLM, observed performance may no longer reflect genuine human effort.

---

## uid: `doi:10.2139/ssrn.6699179`

- title: From No-Arbitrage to Foundation Models: A Review of Financial-Mathematics-Constrained Generative AI and Deep Learning for Quantitative Finance
- authors: YUXUAN HUANG
- affiliations: not stated
- posted: 2026-05-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6699179
- keyword hits: foundation model, generative ai, large language model, large language models

### abstract

Artificial intelligence increasingly enters quantitative finance through option pric ing, volatility calibration, hedging, asset pricing, risk measurement, market simula tion, financial text analysis, and time-series forecasting. Yet finance differs from many prediction domains because a statistically accurate model can still be economically invalid. Prices must respect no-arbitrage restrictions, discounted asset prices must be consistent with martingale arguments under suitable measures, volatility surfaces must satisfy static and dynamic admissibility conditions, hedging rules must account for transaction costs and risk preferences, and scenario generators must preserve tail behavior rather than merely match average dependence. This semi-systematic review studies modern financial AI through this constraint-centered perspective. It organizes the literature from arbitrage pricing and stochastic volatility to neural option pricing, deep calibration, deep hedging, no-arbitrage asset pricing, generative market models, f inancial large language models, and time-series foundation models. The review makes three contributions. First, it separates financial constraints into structural admissibil ity, task-level economic objectives, and governance-validity requirements. Second, it identifies recurring design patterns for constraint injection, including hard parameter ization, soft penalties, projection or repair, adversarial testing, and temporal valida tion. Third, it proposes layered and task-specific evaluation criteria that distinguish statistical fit from mathematical admissibility, economic usefulness, robustness, and deployability. The main argument is that financial mathematics is not a legacy layer that deep learning replaces. It provides the inductive biases, loss functions, diagnostic tests, and deployment gates that make AI models usable in quantitative finance.

---

## uid: `doi:10.2139/ssrn.6695449`

- title: Multi-modal Retrieval-augmented Traffic Prediction with Scalable Spatio-temporal Knowledge Base
- authors: Jibin Wang, Wenjin Zhang, Yifei Huang, Liangzhe Han, Zerong Deng, Leilei Sun, Weifeng Lv
- affiliations: not stated
- posted: 2026-05-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6695449
- keyword hits: fine-tuning, large language model, large language models, llm, llms, retrieval-augmented

### abstract

Accurate traffic prediction is a crucial component of intelligent transportation systems. While deep learning models have achieved considerable success in capturing spatio-temporal dependencies, these architectures are predominantly zone-specific and struggle to generalize to data-scarce regions without extensive parameter fine-tuning. Although recent approaches leveraging Large Language Models (LLMs) offer promising zero-shot prediction capabilities, they frequently suffer from hallucination issues, which severely compromise the reliability of forecasting in real-world applications. To address these critical limitations, this paper proposes a novel Multi-modal Retrieval-Augmented Traffic Prediction (MRATP) framework. This approach captures complex spatio-temporal dynamics in a completely zone-agnostic manner and effectively mitigates LLM hallucinations by grounding predictions in robust external evidence. Specifically, we construct a scalable spatio-temporal knowledge base that structurally integrates multidimensional time information, spatial metadata, and historical traffic series. A unified multi-modal encoder is designed to project both the input queries and knowledge entries into a shared embedding space, allowing a dedicated retriever to extract the most contextually relevant historical patterns. The retrieved expert knowledge is then synthesized with the input query to form structured instructions to prompt a frozen LLM to generate highly accurate predictions. Furthermore, to optimize the retrieval process, we introduce an innovative retrieval loss that leverages the LLM's intrinsic attention mechanisms as training signals, which enables end-to-end optimization of the retriever. Extensive experiments have been conducted on two real-world datasets for traffic prediction tasks. The results demonstrate the superiority of our method in zero-shot scenarios without the need for extra parameter tuning.

---

## uid: `doi:10.2139/ssrn.6598718`

- title: Visibility ≠ Credibility: Self-Promotion Bias in LLM-Generated Recommendations
- authors: Tandeep Sangra
- affiliations: not stated
- posted: 2026-05-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6598718
- keyword hits: chatgpt, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) such as ChatGPT and Perplexity AI are increasingly used as recommendation engines for professional services including marketing consultants and digital agencies. This paper investigates a structural bias in LLM recommendation outputs: the tendency to surface self-promoted brands as apparently credible due to co-occurrence patterns in retrieval data. Through direct query testing across four major LLM platforms and systematic source analysis-including a direct on-record acknowledgement by ChatGPT of its own bias-this research establishes that visibility in AI-generated recommendations does not equate to independently validated credibility. The paper identifies three primary self-promotion patterns, proposes a five-point buyer verification framework, and examines implications for the practice of Generative Engine Optimization (GEO). Findings suggest that until LLMs develop robust mechanisms for distinguishing self-referential authority signals from independently verified credibility, buyers should apply structured verification when using AI for professional service recommendations.

---

## uid: `doi:10.2139/ssrn.6713089`

- title: MOJO: Multi-LLM Optimised Joint Objective - Generative Artificial Intelligence for Multi-Criteria Decision Analysis Framework
- authors: Abtin Ijadi Maghsoodi
- affiliations: not stated
- posted: 2026-05-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6713089
- keyword hits: generative artificial intelligence, large language model, large language models, llm, llms

### abstract

This study introduces the Multi-LLM Optimised Joint Objective (MOJO), a novel generative artificial intelligence (Gen-AI) driven multi-criteria decision analysis (MCDA) framework. MOJO integrates human expertise with multiple large language models (LLMs) to address key limitations in traditional MCDA approaches. The information fusion framework combines risk-adjusted utility scoring, performance equilibrium, and reliability scoring, producing consensus-driven rankings that account for uncertainty and non-linear risk preferences. Grounded in principles from prospect theory and utility theory, MOJO captures complex behavioural factors such as loss aversion and probability distortion. An ensemble of LLM outputs supports MCDA tasks, complemented by a bias detection mechanism to reduce cognitive load and improve transparency. MOJO also incorporates a comprehensive illustrative case study evaluating treatments for Inflammatory Bowel Disease (IBD), demonstrating its applicability to complex scenarios involving clinical, operational, and ethical criteria. Results from validation experiments involving multiple LLMs and decision-makers across diverse scenarios highlight MOJO's robustness, reliability, and transparency, demonstrating its significant potential in high-stakes fields such as healthcare, engineering, and public policy.

---
