# Classification batch 100 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-100.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6959674`

- title: Set-Valued Prediction for Large Language Models with Feasibility-Aware Coverage Guarantees
- authors: Ye Li, Anqi Hu, Yuanchang Ye, Shiyan Tong, Zhiyuan Wang, Bo Fu
- affiliations: not stated
- posted: 2026-06-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6959674
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) inherently operate over a large generation space, yet conventional usage typically reports the most likely generation (MLG) as a point prediction, which underestimates the model's capability: although the top-ranked response can be incorrect, valid answers may still exist within the broader output space and can potentially be discovered through repeated sampling. This observation motivates moving from point prediction to set-valued prediction, where the model produces a set of candidate responses rather than a single MLG. In this paper, we propose a principled framework for set-valued prediction, which provides feasibility-aware coverage guarantees. We show that, given the finite-sampling nature of LLM generation, coverage is not always achievable: even with multiple samplings, LLMs may fail to yield an acceptable response for certain questions within the sampled candidate set. To address this, we establish a minimum achievable risk level (MRL), below which statistical coverage guarantees cannot be satisfied. Building on this insight, we then develop a data-driven calibration procedure that constructs prediction sets from sampled responses by estimating a rigorous threshold, ensuring that the resulting set contains a correct answer with a desired probability whenever the target risk level is feasible. Extensive experiments on six language generation tasks with five LLMs demonstrate both the statistical validity and the predictive efficiency of our framework.

---

## uid: `doi:10.2139/ssrn.6855321`

- title: Profiling Writing Skills at Scale: A Hybrid Stylometry-LLM Pipeline for Formative Feedback
- authors: Stuti Pande, Yige Song, Kamila Misiejuk, Sonsoles López Pernas, Mohammed Saqr, Eduardo Oliveira
- affiliations: not stated
- posted: 2026-06-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6855321
- keyword hits: generative artificial intelligence, large language model, large language models, llm

### abstract

Providing timely, personalised feedback in large-scale learning environments remains a persistent challenge. Generative artificial intelligence offers scalability, yet limited interpretability and concerns around ungrounded feedback constrain its use for formative assessment. This Work-in-Progress paper presents an early-stage hybrid pipeline that combines stylometric analysis with large language models (LLM) to support interpretable writing feedback at scale. Linguistic features are projected into low-dimensional, pedagogically interpretable indicators using Principal Component Analysis. Across two essay corpora comprising 2,828 student texts (PAN14 and ASAP), we observe stable patterns corresponding to two dominant dimensions of writing style: Syntactic Complexity and Lexical Richness. These dimensions are used to structure LLM-generated feedback and to support targeted diagnostic comments and cohort-level visualisation for instructor oversight in large classes. Ongoing work will examine how this approach informs instructional decision-making and student writing development in authentic learning contexts.

---

## uid: `doi:10.2139/ssrn.6848738`

- title: Asymmetric Intelligence Discount (Aid): Stock-Price Reactions to Parallel Domain Shocks in Generative AI
- authors: Grzegorz Wojarnik
- affiliations: not stated
- posted: 2026-06-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6848738
- keyword hits: claude, gemini, generative ai

### abstract

This letter examines stock-price reactions to three public generative AI events at a comparable product stage: the release of Google Gemini 3 (18 November 2025), the launch of Google Project Genie (29 January 2026), and the public availability of the Claude legal/Cowork plug-in, mapped to the 30 January 2026 trading session. The analysis applies a market model to Alphabet as the originator, to the gaming portfolio, and to the professional-information portfolio, with a consumer-staples portfolio as a low-directexposure negative control, and follows prices through one trading quarter ([0,+63]). After Gemini 3, Alphabet's cumulative abnormal return in [0,+5] was +10.77% (t = +2.72), rising to +13.09% (t = +3.26) against the technology benchmark XLK. After Project Genie, the gaming portfolio's average cumulative abnormal return was-13.00% (t =-4.67) and remained negative after one quarter (-14.40%). After Claude, the comparable return for the professional-information portfolio was-14.67% (t =-6.95) in [0,+5] and reversed to +7.77% after one quarter. Treated-minus-control differences in [0,+5] were-22.06 pp for gaming and-23.74 pp for professional information. For Claude, the analysis also applies a conditional reverse DCF that maps implied revenue-erosion paths (0.68-1.92 pp per year in the no-marginbenefit scenario) and audits public disclosures. The letter develops the Asymmetric Intelligence Discount (AID) framework around three dimensions of asymmetry in market attention and formulates three falsifiable directional predictions. The findings document parallel domain repricings and provide an auditable starting point for further tests of the interpretive AID hypothesis.

---

## uid: `doi:10.2139/ssrn.6958779`

- title: Open-Ended Bias Discovery in Large Language Models
- authors: Thai Huy Nguyen, Ngoc Hoang Luong
- affiliations: not stated
- posted: 2026-06-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6958779
- keyword hits: large language model, large language models, llm, llms

### abstract

Large Language Models (LLMs), despite being trained on large-scale datasets, are known to exhibit biases due to imbalances in latent subjective features. Prior research has largely relied on manually crafted test examples to assess whether models demonstrate preferential behavior toward certain characteristics. However, such manual approaches limit the scalability and coverage of bias analysis. To address this, recent works have increasingly focused on automatic methods for bias discovery. In this paper, we propose URBias, an unsupervised framework for discovering a set of diverse prompts that reveal biases in LLMs across dimensions. Our approach leverages Quality-Diversity optimization with automatic learning of the underlying features and bias evaluation via LLM-as-a-Judge. By optimizing both diversity and bias exposure, our method explores a wide range of prompts across features such as topics and task formats. We evaluate our method on various state-of-the-art LLMs, which serve both as prompt generators and target models. Empirically, our pipeline generates a more diverse set of test cases, achieving at least 4.5x boost of coverage compared to manual datasets. We also observe that our method uncovers a broader range of more complex biases within various models.

---

## uid: `doi:10.2139/ssrn.6942921`

- title: Can AI-Assisted Analysis of Antidepressant Drug Online Reviewers (ADORE) Inform Real-World Use of Antidepressants?
- authors: Magid Abraham, Thomas  R. Insel, Husseini  K. Manji, Akshay Swaminathan
- affiliations: not stated
- posted: 2026-06-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6942921
- keyword hits: claude, gemini, large language model, large language models

### abstract

Background: Antidepressant selection is constrained by limited comparative-effectiveness data, with randomised trials measuring symptom reduction rather than patient-reported tolerability. We tested whether AI-assisted analysis of patient-written online reviews recovers drug-level tolerability signals that converge with the strongest randomised evidence. Methods: We did a cross-sectional analysis of 8,428 reviews of 17 antidepressants for major depressive disorder posted to Drugs.com (Oct 2008 – Jun 2023; ≥1 month reported use). Each review was classified across 17 clinical dimensions by two independent large language models (Claude Sonnet 4·5, Gemini 2·5 Pro) using identical structured prompts. A 100-review subsample was independently rated by two expert reviewers. We compared ADORE (Antidepressant Drug Online Reviewers) top-rating prevalence per drug with Cipriani's 2018 network meta-analysis retention and efficacy odds ratios (Spearman correlation). Findings: Mean inter-LLM Cohen's κ was 0·81 (range 0·62–0·96). Expert reviewers showed substantial agreement with the dual-AI consensus (mean κ = 0·75 and 0·80); inter-reviewer agreement (κ = 0·66) was lower than each reviewer's agreement with the AI consensus. Top rating was achieved by 49·3% and transformative response by 20·6% of users. ADORE top rating correlated strongly with Cipriani retention odds ratios (ρ = +0·79, p < 0·001) but not with efficacy odds ratios (ρ = −0·14, p = 0·64). Within-SNRI heterogeneity was substantial: desvenlafaxine matched SSRIs whereas venlafaxine (OR 0·78) and levomilnacipran (OR 0·61) underperformed. Emotional blunting was the strongest negative predictor of satisfaction (OR 0·20). Interpretation: AI-classified patient reviews recover the drug-level tolerability signal of randomised retention data and identify within-class heterogeneity invisible to class-level guidelines. Within the comparable-efficacy range of contemporary antidepressants, tolerability — especially the avoidance of emotional blunting — dominates patient satisfaction.

---

## uid: `doi:10.2139/ssrn.6962764`

- title: Human-Centred AI Urbanism: Integrating Emotional Data and Interactive Large Language Models for Geospatial Understanding
- authors: hee  sun choi, David  Sky Cheng
- affiliations: not stated
- posted: 2026-06-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6962764
- keyword hits: large language model, large language models, llm, llms

### abstract

Large Language Models (LLMs) offer powerful urban data analysis capabilities but fail to capture subjective emotional experiences, creating a disconnect between data-driven strategies and citizens’ lived realities (Liu et al., 2025; Zheng et al., 2025). Challenges like semantic complexity, domain-specific terminology, and inherent training biases further limit LLMs’ urban adaptability (Liu et al., 2025). This paper proposes a Human-Centred AI Urbanism framework integrating emotion-based geospatial mapping with Interactive LLMs (ILLMs) to foster more empathetic urban development.,We show that systematically incorporating diverse emotional data validated through human feedback allows ILLMs to transcend current limitations (Choi et al., 2025; Huang et al., 2020; Rokhsaritalemi et al., 2023). Our approach emphasizes continuous human-computer looping, where user responses and expert insights iteratively refine LLM interpretations, addressing biases and improving geospatial analysis precision (Peng et al., 2023; Zheng et al., 2025). This interactive paradigm leverages LLMs’ pattern recognition while grounding them in authentic human experiences, bridging computational efficiency and human well-being.,This research positions LLMs as integral components of a participatory urban data ecosystem. By focusing on continuous human emotion integration through ILLMs, we provide a pathway for understanding urban complexity ”for people,” leading to more adaptive, inclusive, and emotionally intelligent planning solutions. This paradigm shift will catalyse urban environments that genuinely resonate with inhabitants’ emotional and social needs.

---

## uid: `doi:10.2139/ssrn.6960640`

- title: ScamFerret: An LLM Agent for Multi-type and Multilingual Scam Website Detection
- authors: Hiroki Nakano, Takashi Koide, Daiki Chiba
- affiliations: not stated
- posted: 2026-06-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6960640
- keyword hits: gpt-4, large language model, llm, llms

### abstract

Scam websites defraud consumers worldwide across multiple scam types, including fake online shopping, cryptocurrency scams, and investment scams.Existing detection systems require type-specific labeled datasets and feature engineering, limiting coverage as new scam types emerge.We propose ScamFerret, a Large Language Model (LLM)-based agent that classifies URLs as scam or legitimate by autonomously collecting evidence from web content, infrastructure records, and social media, producing a binary classification and a human-readable rationale without per-type training data.We construct the first ground-truth dataset of 4,780 websites covering eleven scam types in English and seven languages for fake online shopping, with balanced scam--legitimate pairs for four major types.We evaluate six LLMs against six baselines and assess reasoning quality using three metrics (logical consistency, evidence-based reasoning, and feature compliance) validated by human annotation.The best-performing configuration, GPT-4.1, achieves 0.968 mean detection rate across eleven English scam types and 0.983 mean accuracy across seven languages.Model scale systematically shapes evidence-gathering behavior and determines the cost-accuracy trade-off, enabling practitioners to choose between high-accuracy and cost-efficient configurations.These results demonstrate that a single LLM-based agent generalizes across scam types and languages without per-type or per-language training.

---

## uid: `doi:10.2139/ssrn.6946157`

- title: Load Balancing for Large Language Model Inference Serving: A Control and Learning Oriented Survey
- authors: Hanbo Ma, Zhongguo Li, Junan Wang, Chunyi Cao, Donglin Li, Jun Yang, Zhengtao Ding
- affiliations: not stated
- posted: 2026-06-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6946157
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are widely deployed as interactive neural inference services, where performance depends on how compute, memory, communication bandwidth, and persistent state are allocated under non-stationary demand. This survey studies load balancing for LLM inference serving as an intelligent scheduling and resource-allocation problem for large-scale learning systems. The analysis focuses on imbalance induced by prefill–decode phase asymmetry, key–value (KV) cache residency, heavy-tailed request variability, heterogeneous hardware, and service-level objectives (SLOs). A structured review protocol codes representative studies by imbalance source, observable signals, control knobs, assumptions, limitations, and evaluation evidence. We introduce a state– action–constraint abstraction, compare six strategy families, and synthesize evaluation practice around tail latency, time to first token (TTFT), token cadence, goodput, robustness, and energy per SLO-compliant token. Open directions are discussed for long-context and multimodal serving, decentralized deployment, green inference, and autonomous self-adaptive serving.

---
