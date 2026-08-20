# Classification batch 1 of 22, edition 21

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-021/batch-1.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7295938`

- title: Who Audits the Reviewers? A Multi-Model Consensus Framework for Characterizing Failures in LLM-Assisted Peer Review
- authors: Olalekan J. Akintande
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7295938
- keyword hits: gemini, gpt-4, large language model, large language models, llama, llm, llms, prompting

### abstract

Large Language Models (LLMs) are increasingly used to assist with academic peer review, yet their outputs remain prone to systematic errors often presented with high confidence. This paper presents a comprehensive empirical characterization of failure modes in LLM-assisted academic review through a controlled experiment involving 15 papers, 5 LLMs, 3 prompt conditions, and 672 independent judge-review evaluations across 11 error types. We find that Unsupported Claims is the most prevalent error (mean frequency 3.02 per review), followed by Plausible Reasoning Gaps (2.86) and Confirmation Bias (2.19). Llama 3.1 70B consistently outperforms commercial alternatives, including GPT-4o (overall error mean 3.23 vs. 3.53), challenging assumptions regarding the superiority of proprietary architectures. Structured prompting reduces error frequency by approximately 35%, while self-correction reduces errors by 44% on average; however, self-correction efficacy is highly architecture-dependent, ranging from a 50.73% reduction in GPT-4o to negligible improvements in Gemini 3.5 Flash. Inter-judge agreement is poor (mean Fleiss' Kappa:-0.013), with a 2.6-fold stringency differential between judges, mirroring human peer review variability. A counterintuitive "Self-Correction Paradox" emerges wherein higher-quality reviews generate both increased consensus and specific points of heightened disagreement. Logistic regression confirms that model choice, prompt condition, and domain, particularly in Medicine, are significant predictors of error prevalence. Novice reviewers miss 2.5% of errors on average. We propose a robust failure taxonomy and offer practical recommendations for journals, emphasizing that while LLMs offer promising structural support, rigorous human oversight remains indispensable.

---

## uid: `doi:10.2139/ssrn.7279064`

- title: Detection without Calibration: Benchmarking Domestic and International Large Language Models for Quality Control of Mandarin ¹⁸F-FDG PET/CT reports
- authors: Jingbo Wang, Weiqing Tang, Xingdi Ma, Huimin Yan, Ying Yuan
- affiliations: not stated
- posted: 2026-08-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7279064
- keyword hits: claude, deepseek, gpt-5, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are increasingly used for automated quality control (QC) of radiology reports. However, the reliability of LLMs on reports in Mandarin, and the relative performance of domestic versus international flagship models, remain unknown. We benchmarked 14 LLM configurations, seven Chinese-developed (“domestic”) and seven international models, on 1,000 whole-body ¹⁸F-FDG PET/CT reports split into an error-injected “junior-doctor” arm and a low-residual “finalised” arm (500 each), using a controlled error-injection gold standard. Under each blinded zero-shot prompt, each model flagged six error types and assigned a 1–5 overall score. Two distinct abilities: error-detection macro-F1 (0.356-0.667) and overall-score calibration (ICC[2,1] 0.099-0.627), were weakly and not significantly correlated across models (Spearman ρ = 0.38, p = 0.18); the dissociation was instead evident in sharp rank reversals, the strongest detector (Claude-Opus-4.8 0.667) calibrating poorly (0.491), while the three best-calibrated models were all domestic (MiMo 0.627, GLM-5 0.612, DeepSeek 0.609). Once the access channel was controlled, domestic and international error detection were statistically indistinguishable (Δmacro-F1= -0.011, P = 0.84); domestic models showed consistent but not significant advantages in calibration (ΔICC = +0.142) and Chinese-character-error detection (ΔF1 = +0.109), accompanied with large reductions in cost (US$0.09–2.71 vs $0.26–14.5 per 1,000 reports) and on-premise deployability. Re-running two flagships through both agent channels and clean APIs showed that agent channel inflated both detection and calibration (GPT-5.5 ΔICC = +0.098, 95% CI 0.070-0.128), confirming that uncontrolled benchmarks over-credit agent-channel models. Missed-diagnosis detection was the universal weakness (best 0.467) and the one category where the human physicians outperformed every model. Raw detection ability does not guarantee a trustworthy score, and domestic and international models differ by deployment-relevant profile rather than by overall performance rank; both essential distinctions for performing clinical nuclear-medicine QC.

---

## uid: `doi:10.2139/ssrn.7274513`

- title: WeedExpert-R1: Incentivizing Botanical Reasoning in MLLMs with Reinforcement Learning for Precision Weed Grounding
- authors: Zonglin Yang, Wei-zhen Liang, Nevin Lawrence, Xin Qiao, Benjamin  S. Riggan, Chi-En Chiang, Fuchen Li
- affiliations: not stated
- posted: 2026-08-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7274513
- keyword hits: chain-of-thought, fine-tuning, gemini, gpt-5, large language model, large language models, llm, qwen

### abstract

Precision weed control requires both species-level identification and per-instance localization, butconventional object detectors are constrained by a closed-vocabulary paradigm that hinders cross-regiondeployment and lack the reasoning capability to justify their predictions in complex agricultural scenes.Recently, multimodal large language models (MLLMs) have demonstrated strong visual perceptionand reasoning in visual grounding, offering a promising alternative. However, their insufficient domainspecificbotanical knowledge often leads to hallucinations during fine-grained weed identification. Inthis study,WeedExpert-R1 is introduced, a multimodal reasoning model that, following the R1-styletraining paradigm, incentivizes visually grounded botanical reasoning through verifiable rewards.Specifically, a domain-specific Chain-of-Thought (CoT) synthesis pipeline is proposed. It pairs ahuman-curated botanical trait dictionary, covering leaf shape, margin, petiole, and stem morphology,with an Auditor–Synthesizer LLM workflow to generate high-quality reasoning data for supervisedfine-tuning as a cold start. This pipeline bridges the gap between textual botanical knowledge and thevisual perception of MLLMs. Group Relative Policy Optimization (GRPO) is then applied withverifiable rewards (format, accuracy, count, and length penalty) to further enhance the model’scapability to perceive and localize diverse weeds. WeedExpert-R1-4B achieves 75.82%, 89.30%,and 87.81% on Precision@(F1=1, IoU≥0.5), Precision@0.5, and Recall@0.5 across 37 weed specieson a benchmark suite of six weed datasets (3SeasonWeedDet10, CottonWeedDet12, CottonWeedDet3,Weed-crop,Weed25, and PREEC), and outperforms both frontier proprietary models (GPT-5.4, Gemini-3.1-Pro) and larger open-source baselines (Qwen3-VL-30B-Instruct, Gemma-4-31B-it). Moreover,qualitative results on unseen species further illustrate the open-vocabulary capability ofWeedExpert-R1,suggesting potential for deployment across diverse regions and crops without retraining.

---

## uid: `doi:10.2139/ssrn.7279498`

- title: AIgentXR: Generative AI Agents and Extended Reality for Teleoperation of Unmanned Aerial Vehicles
- authors: Alhassan Mumuni, Fuseini Mumuni, Masha Ahoba Buah
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7279498
- keyword hits: agentic, ai agent, generative ai, generative artificial intelligence, large language model, large language models, llm, llms

### abstract

Unmanned Aerial Vehicles (UAVs), or drones, are increasingly deployed in complex and safety-critical environments, where human-machine interaction and collaboration is often critical to achieving mission objectives. Yet their operation still relies heavily on ground control stations (GCS) based on traditional 2D graphical user interfaces (GUIs). These interfaces permit very limited interaction with the human operator. They also limit situational awareness, increase cognitive load, and, thereby, constrain overall mission effectiveness. Recent advances in generative artificial intelligence (AI), especially Large Language Models (LLMs), and Extended Reality (XR) present new opportunities to overcome these limitations. This work explores the integration of LLM-based intelligent agents with XR to create immersive and intuitive user interfaces (UIs) for teleoperating UAVs. We develop a proof-of-concept UI, AIgentXR, based on these techniques and conduct practical studies on the use of agentic AI and XR to improve the teleoperation of UAVs. The focus is on improving mission execution efficiency, increasing interaction intuitiveness, reducing cognitive load on operators, and enhancing situational awareness. We performed extensive quantitative evaluation of our approach using predictive human-computer interaction (HCI) models and also conduct benchmark comparisons with approaches based on conventional ground control stations.The results suggest that XR-assisted agentic interaction may provide a promising direction for future human-centered UAV control systems, particularly in complex missions requiring rapid situational understanding and intuitive supervisory control.

---

## uid: `doi:10.2139/ssrn.7276907`

- title: Beyond Superficial Similarity: A Psychometric Fidelity Framework (PFF) for Validating AI Digital Twins in Mental Health Research
- authors: Susanna Joo, Myeong-Sook Yoon
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7276907
- keyword hits: claude, gemini, gpt-5, large language model, llm, llms

### abstract

Despite the growing potential of Large Language Model (LLM)-based psychobehavioral digital twins in mental health research, standardized protocols for verifying their empirical and psychometric validity are lacking. Existing evaluations often rely on descriptive-level comparisons or AUC, failing to assess whether AI-generated synthetic data preserves the underlying psychological structures of human respondents. This study proposes the Psychometric Fidelity Framework (PFF), an evaluation protocol across four tiers: distributional, structural, network, and clinical fidelity. We analyzed an integrated dataset (N = 2,256) comprising empirical survey data from South Korean university students (n = 756) and synthetic datasets generated by GPT-5.5, Gemini 3.5 Flash, and Claude 3.6 Sonnet (n = 500 each). Three validated instruments were employed: the Patient Health Questionnaire–9 (PHQ-9), UCLA Loneliness Scale–6 (UCLA-6), and Alcohol Use Disorders Identification Test–K (AUDIT-K). Results revealed systematic psychometric failures across all PFF tiers. LLMs failed to replicate the characteristic positive skewness of empirical mental health distributions. Furthermore, Cronbach’s alpha and confirmatory factor analysis revealed psychometric discrepancies between most LLMs and survey data. The theoretically expected correlations were absent or inconsistent. Crucially, the dissociation between indistinguishable AUCs and distorted prevalence, and between distinguishable AUCs and similar prevalence, highlights that descriptive or AUC-based comparisons are insufficient for validation. The PFF provides a systematic standard for validating AI-generated data and establishes the necessary boundary conditions for integrating psychobehavioral digital twins into mental health research and evidence-based practice.

---

## uid: `arxiv:2608.17715v1`

- title: Communicating Credit Risk with Large Language Models: Evaluation of Explanations from Standard and Alternative Data-Based Models
- authors: Sahab Zandi, Noah Kostesku, Christophe Mues, María Óskarsdóttir, Cristián Bravo
- affiliations: not stated
- posted: 2026-08-18
- source: arXiv
- link: https://arxiv.org/abs/2608.17715v1
- keyword hits: deepseek, gemini, large language model, large language models, llm, llms

### abstract

Credit decisioning is a high-stakes task in which model outputs must be accurate and explainable to support compliant decisions. Although modern credit risk models such as eXtreme Gradient Boosting (XGBoost) and Graph Neural Networks (GNNs) improve predictive performance, their explanations are often too technical for stakeholders creating communication gaps that can shape approvals, denials, and fairness judgments. We examine whether Large Language Models (LLMs) can serve as explanation layers that translate post-hoc explanation artefacts into stakeholder-appropriate risk narratives. Using Freddie Mac single-family loan-level data, we develop three pipelines: standard tabular (XGBoost + SHAP), and two with alternative data, a pure network-based (GNN + GNNExplainer), and a bimodal one (combining tabular and network data). We generate narratives with three LLM configurations: a small fine-tuned LLM (Gemma 3 4B), a large fine-tuned LLM (DeepSeek R1 70B), and a zero-shot commercial LLM (Gemini 2.5). Explanation quality is evaluated through automated checks across all pipelines and a human study of bimodal explanations comparing credit risk professionals and non-professionals on eight decision-relevant dimensions. We have three main findings. First, the pipeline accounts for higher variance in evidence-grounding scores than the language model, meaning that the binding constraint on explanation quality is the evidence representation, not the model used. Second, the explanation narratives reliably name the influential factors but are less reliable when stating the direction of influence, which may be consequential for adverse-action communication. Finally, professionals apply stricter evidentiary standards than non-professionals. We discuss implications for the governance of risk models, including deployment considerations and the value of domain-aligned LLMs in regulated credit settings.

---

## uid: `doi:10.2139/ssrn.7312181`

- title: Beyond Human-like Responses: Evaluating the Implicit Personality Alignment of Large Language Models
- authors: Qinyi Hu, Fei Xie, Zhen Li, Xucong Hu, Meng Zhang, Mowei Shen, Jifan Zhou
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7312181
- keyword hits: chatgpt, claude, gpt-4, large language model, large language models, llm, llms

### abstract

Despite widespread adoption of large language models (LLMs), our understanding of these competent assistants remains limited. Since personality serves as a key predictor of behavioral patterns, this study investigates whether LLMs have implicitly learned to display personality through a rigorous psychometric approach. We employed role-playing prompts to assess the "personality" of 100 fictional characters enacted by ChatGPT-4o and Claude Haiku 3.5 using two validated personality measures: a self-evaluation scale (NEO-FFI-R) and a situational judgment test (SJT). Performance was benchmarked against human participants (N = 113). Results revealed limitations in LLMs' personality coherence: both LLMs demonstrated inferior test-retest reliability to human participants, especially in terms of behavioral tendencies which showed particularly pronounced instability. More critically, construct validity analysis revealed false inference and inconsistencies between self-evaluated personality and behavioral tendencies. These discrepancies demonstrate that current LLMs are responding based on personality-related knowledge to pretend they have specific personality, rather than having a stable and consistent inner personality as humans.

---

## uid: `doi:10.2139/ssrn.7308958`

- title: Cost-Aware Preference-Based Bayesian Optimization for Structured Prompt Configuration of Large Language Models
- authors: Muhammad Amir Saeed, Sadia Saba, Antonio Candelieri
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7308958
- keyword hits: large language model, large language models, llama, llm, llms, qwen

### abstract

Prompt configuration strongly affects the accuracy, reliability, and cost of large language models (LLMs), but jointly tuning instructions, output contracts, demonstrations, reasoning cues, and decoding settings creates a large mixed discrete black-box optimization problem. We propose MNL-PCO, a cost-aware, preference-based Bayesian optimization framework that uses a ridge-regularized multinomial-logit (MNL) discrete-choice surrogate over structured prompt components. The surrogate is learned from pairwise preferences induced by observed configuration scores and provides directly interpretable component utilities without requiring learned prompt embeddings or kernel design. Evaluations are performed at three validation-subset fidelities (15%, 40%, and 100%); expected improvement is weighted by a fidelity-information factor, normalized by a pre-evaluation token-cost proxy, and combined with periodic full-fidelity promotion. We evaluate MNL-PCO in two stages. A controlled study covers four simulation regimes, 30 paired seeds per regime, a 23,328-configuration space, and 11 methods/ablations. MNL-PCO obtains the highest mean selected-prompt accuracy among the principal methods in all four regimes (0.907-0.960), significantly outperforming Hyperband and random-search baselines after Holm correction. On 100 unseen simulated configurations, its mean held-out Spearman correlation is 0.807 versus 0.667 for direct-score ridge. We then evaluate two local open-weight models-Llama 3.2 1B and Qwen2.5 1.5B-on IMDb, SST-2, and AG News with five paired seeds per setting and actual token/runtime accounting. MNL-PCO has the best mean test accuracy in four of six model-task settings and the best average accuracy rank (1.83), but it does not dominate IMDb, and the direct-score ridge surrogate ranks unseen live configurations better. These results support MNL-PCO as a competitive, interpretable structured-search method while also identifying the limits of an additive MNL utility model on real LLM behavior.

---
