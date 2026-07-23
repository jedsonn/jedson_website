# Classification batch 286 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-286.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6757918`

- title: Mapping Urban Food Sharing at Scale: Discovering and Classifying Food Sharing Initiatives Across 105 European Cities
- authors: Hyunji Cho, Ivan Bacher, Patricia Buffini, Anna Davies, Gareth Jones, Anastasiia Potyagalova, Hao Wu
- affiliations: not stated
- posted: 2026-05-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6757918
- keyword hits: large language model, llm

### abstract

Urban food sharing initiatives-including community fridges, food banks, gleaning networks, cooperative kitchens, and surplus redistribution platforms-represent a growing segment of the urban sustainability landscape. Despite increasing scholarly and policy interest, there is currently no widely adopted and systematically documented methodology for mapping such initiatives at continental scale. This paper presents a methodology developed in the EU Horizon Europe project CULTIVATE (Grant Agreement No. 101083377), including an end-to-end data pipeline for discovering, classifying, and curating food sharing initiatives (FSIs) across 105 European cities. The pipeline integrates multilingual web discovery across 25 languages, large language model (LLM)-assisted classification using an agent-based, on-the-fly retrieval approach, structured human-in-the-loop verification, and a medallion data architecture for progressive data refinement and quality assurance. Across five iterative rounds, the system processed approximately 210,000 candidate URLs per iteration (around 3 GB of extracted unstructured text), improving classification accuracy on a fixed reference set from 32% to 74% through prompt refinement, exclusion rule development, and architectural changes. The resulting dataset comprises approximately 3,000 validated FSIs after multistrategy deduplication and forms the empirical basis of the Food Sharing Map hosted on the Sharing Solutions platform. We document the full pipeline methodology, report accuracy trajectories and deduplication outcomes, and discuss the challenges of multilingual web-based discovery and the role of human oversight in LLM-assisted classification. The pipeline and its design principles provide a reusable methodological framework for large-scale, web-based discovery and curation of community-level initiatives in other policy-relevant domains.

---

## uid: `doi:10.2139/ssrn.6779495`

- title: AI-Generated Synthetic Video as a Training Resource for Invasive Species Classifiers: A Reproducible Bio-Prompting Framework for Synthetic-to-real Generalisation
- authors: Joao  Pedro Torres da Silva, Jordi Aguiló Gisbert, Francesca Suita, Manuel Ibáñez-Arnal, Jordi López-Ramón
- affiliations: not stated
- posted: 2026-05-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6779495
- keyword hits: generative artificial intelligence, prompt engineering, prompting

### abstract

The limited availability of labelled visual data remains a major constraint for training reliable species classifiers in ecological applications. Although synthetic data generation using generative artificial intelligence represents a promising alternative, robust methodological frameworks are still lacking to evaluate its effectiveness and its ability to generalise to real-world data.In this work, we present a reproducible framework based on biologically informed prompt engineering to generate ecologically plausible synthetic data and systematically assess synthetic-to-real generalisation. Two widely used generative paradigms, Text-to-Video (T2V) and Image-to-Video (I2V), were employed to construct training datasets. These datasets were used to train five convolutional neural network architectures, ranging from lightweight models to pre-trained deep networks, using invasive psittacines as a case study.Evaluation on an independent set of unseen real-world images showed that both paradigms achieve comparable overall performance across architectures, with no statistically significant differences in F1-score. However, clear differences emerged in error profiles: models trained with I2V exhibited higher precision and fewer false positives, whereas those trained with T2V achieved higher recall at the cost of increased false positives. These patterns were consistent across runs, indicating that they reflect systematic differences between generative paradigms rather than random variability.The results demonstrate that synthetic video data can serve as a robust and cost-effective complement to real-world data in ecological classification tasks, provided that its generation and evaluation are embedded within a rigorous and reproducible methodological framework.The code and data used in this study are available for peer review in an anonymous private repository:

---

## uid: `doi:10.2139/ssrn.6778921`

- title: The Mark Does Not Travel: Provenance State-Transition-Based Governance for Synthetic Media Distribution Chains
- authors: Junhwa Youm, Yoonmo Yang, Yunyi Hong, Daon Choi, Jee Won Park, Sungmi ‍Park
- affiliations: not stated
- posted: 2026-05-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6778921
- keyword hits: generative ai

### abstract

As synthetic media governance matures, the central regulatory challenge is shifting from how content is generated to how transparency is maintained across multi-party lifecycles. Major regimes, including the EU AI Act, California transparency statutes, South Korea’s AI Basic Act, and China’s labeling measures, require synthetic media to remain identifiable, yet existing duties remain largely tied to the static point of provision. In real distribution environments, platform compression, metadata stripping, visual editing, and model-to-model regeneration can erase or disconnect initial provenance signals, creating a legal and forensic compliance gap.This paper introduces a Provenance State Transition (PST) framework that reframes synthetic content governance from source-marking compliance to lifecycle-based provenance readiness. The framework models how visible watermarks, invisible watermarks, and C2PA manifests degrade across six distribution stages, producing forensic chain statuses such as intact, missing, and replaced. Through an observational audit of major generative AI platforms under twelve damage scenarios, we show the fragility of standalone marking mechanisms. We further present a proof-of-concept platform-side chain-extension prototype that logs pre- and post-processing verification states, preserving provenance history even when embedded indicators are erased. This work provides a taxonomy, empirical baseline, and technical architecture for distributing accountability across the synthetic media lifecycle.

---

## uid: `doi:10.2139/ssrn.6779306`

- title: Self-Adaptive Pruning for Graph of Thoughts in Multi-Hop Rea-soning
- authors: Miao Fan, Jiaren Zou
- affiliations: not stated
- posted: 2026-05-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6779306
- keyword hits: large language model, large language models

### abstract

Graph-of-Thought reasoning with large language models over knowledge graphs enables structured multi-hop inference, but existing methods rely on static pruning strategies that make irreversible local decisions. As a result, early prediction errors can prematurely eliminate valid reasoning paths, leading to error propagation and semantic drift in long-chain reasoning.In this paper, we propose a self-adaptive predictive pruning framework that incorporates uncertainty into the reasoning process. We formulate pruning as an uncertainty-aware decision problem, where the confidence of candidate relations is estimated via entropy over model predictions. Based on this signal, the framework dynamically adjusts pruning thresholds to balance exploration and efficiency during search.To further improve robustness, we introduce a lightweight feedback mechanism that revisits previously pruned paths when potential reasoning failures are detected, enabling recovery from early errors without incurring excessive search cost. Extensive experiments on multiple multi-hop question answering benchmarks demonstrate that our approach consistently outperforms strong baselines in both accuracy and robustness, particularly on tasks requiring long reasoning chains. Moreover, it achieves better performance under the same computational budget, effectively controlling search space growth while improving reasoning efficiency.

---

## uid: `arxiv:2605.30363v1`

- title: Enhancing Regime Shift Detection Using Unstructured Data: A Study on the Treasury Market
- authors: Mingxuan Yi, Vidal Mehra, Jing Chen, John Cartlidge
- affiliations: not stated
- posted: 2026-05-17
- source: arXiv
- link: https://arxiv.org/abs/2605.30363v1
- keyword hits: large language model, llm

### abstract

Regime shifts in financial markets reorganise the joint dynamics of asset prices and macro variables, breaking any single-regime calibration. They are nonetheless difficult to detect reliably because the data signal is noisy and heavily multicollinear, while the contemporaneous text that announces them is unstructured. Standard regime shift detection methods rely solely on structured time-series data and ignore policy communications, even though these texts often signal shifts before they materialise in observed prices. We propose a text-enhanced regime shift detection pipeline that combines large language model (LLM) reasoning over central-bank communications with statistical validation on multivariate financial time series. The framework is detector-agnostic: text-proposed candidates are validated using a bootstrap likelihood-ratio test on a vector autoregression (VAR), while data-driven candidates from arbitrary regime detectors are ratified through a lenient LLM text check. We evaluate the framework on 2010-2024 FOMC minutes paired with a 14-variable U.S. Treasury and macroeconomic panel, using four interchangeable data-driven detectors. The proposed pipeline achieves F1 = 0.82 against a verified anchor list of monetary-policy regime shifts, with same-day modal detection latency and consistently stronger performance than pure data-driven baselines. The results demonstrate that combining unstructured policy text with statistical structural-break detection improves the robustness and interpretability of regime shift identification in financial markets.

---

## uid: `doi:10.2139/ssrn.6753841`

- title: Cited-Listicle Rank-Tier Exposure, Author Type, and LLM Brand Visibility: A Two-Part Model of Selection and Prominence in Generative Engine Responses Working Paper
- authors: Jan Ehrlinspiel, Tomek Rudzki, Malte Landwehr
- affiliations: not stated
- posted: 2026-05-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6753841
- keyword hits: large language model, llm

### abstract

We study how exposure to repeatedly cited third-party listicles at different rank tiers relates to two outcomes in Large Language Model (LLM) responses: whether a brand is mentioned (the selection equation), and, conditional on being mentioned, where the brand appears (the prominence equation). Using chat-level panel data from three markets (B2B SaaS: 1.67M observations, 21 brands, 6 engines; Emerging MarTech: 1.27M observations, 111 brands, 7 engines; US finance: 2.80M observations, 45 brands, 3 engines), we estimate Part 1 as a Correlated Random Effects logit and Part 2 as an OLS prominence equation on the visibility = 1 subsample, both with prompt × model × date fixed effects and Mundlak brand means (Mundlak, 1978; Wooldridge, 2010). A parallel OLS specification on the full panel summarizes the joint association with the mention-count outcome. Across all three markets, higher-ranked third-party exposure is positively associated with mention probability, and top-tier exposure is associated with earlier conditional placement. The gradient is most monotonic in Emerging MarTech, concentrated at top tiers in US finance, and flatter in B2B SaaS. Author-type and lower-support estimates are interpreted as exploratory. The estimates are conditional within-brand associations, not causal effects of moving a brand's rank on a single listicle.

---

## uid: `doi:10.2139/ssrn.6790565`

- title: Artificial Intelligence Exposure and Corporate Cash Holdings
- authors: Mohsen Aram
- affiliations: not stated
- posted: 2026-05-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6790565
- keyword hits: chatgpt

### abstract

This paper examines whether industry exposure to artificial intelligence (AI) shifts the cash holdings of U.S. public firms, and which of two opposing channels dominates: a precautionary build-up, or an efficiency-and-substitution channel. Using a panel of U.S. public firms from 2015 through 2025, we combine an industry AI exposure measure (AIIE) with the AI Economic Uncertainty (AIEU) index in a shift-share design and exploit the November 2022 launch of ChatGPT as a discrete capability shock. We document a systematic sign flip across fixed-effects structures. Under industry fixed effects, AI-exposed industries hold more cash on average; under firm fixed effects, the same firms reduce their cash as AIEU rises. After the ChatGPT launch, exposed firms lower their cash by roughly one percentage point in a clean step that persists through 2025. The pattern is consistent with efficiency-and-substitution channel.

---

## uid: `doi:10.2139/ssrn.6758258`

- title: Federated Mutual Knowledge Transfer for Early Anomaly Detection in Automotive Welding Robots
- authors: Durgeshkrishna B S, Kannappan R, Thejeshwar Raj P, Leena Sri R
- affiliations: not stated
- posted: 2026-05-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6758258
- keyword hits: large language model, llm

### abstract

In modern automotive manufacturing, keeping robotic welding lines fast and reliable is increasingly important. These systems often face challenges like electrode wear, gradual temperature changes, and slight mechanical issues. These problems can cause poor weld quality and unexpected downtime. Traditional maintenance strategies usually react only after problems occur or depend on fixed schedules that do not reflect the actual condition of the machinery. To tackle this issue, this paper presents a predictive maintenance approach that uses edge intelligence supported by a central language model. Smart Local Models (SLMs) at each welding unit continuously monitor key sensor data, such as grip pressure, heat buildup, and vibration signals. Instead of sending large amounts of raw data, only relevant anomaly information is sent to the central Large Language Model (LLM). The LLM interprets patterns, identifies potential failures early, and helps make timely maintenance decisions. This proactive approach helps extend equipment lifespan, reduce interruptions, and improve manufacturing performance in industry 4.0.

---
