# Classification batch 2 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-2.answer.json` as a JSON array.

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

## uid: `doi:10.2139/ssrn.7299354`

- title: How accurate are Large Language Models on Multimodal Theory-of-Mind Tasks?,A comparison with Humans
- authors: Eddie Bullock, Carrie Allison, Charles Nduka, Marcin  A. Radecki, Simon Braschi, Ofer Golan, Simon Baron-Cohen
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7299354
- keyword hits: claude, gemini, gpt-5, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) demonstrate impressive performance on text-based theory of mind (ToM) tasks, which involve the ability to attribute mental states to others. However, comparisons of LLM vs. human performance on more naturalistic ToM tasks are sparse. The present study evaluated four state-of-the-art LLMs (GPT-5, GPT-5 Mini, Gemini 3 Flash, and Claude Opus 4.5) on ToM performance using two video and audio-based batteries, EU-Emotion (20 mental states) and Mindreading (359 mental states). On both batteries, all models performed significantly above chance. On the EU-Emotion, video-only accuracy ranged from 67.80% to 74.58%, with the top two models (Gemini 3 Flash, GPT-5) significantly exceeding the human video benchmark (63%). Adding audio and video input raised Gemini 3 Flash’s EU-Emotion accuracy to 81.36%, and its audio only performance (58.47%) exceeded the human audio benchmark (45.19%). On Mindreading, video-only accuracy was lower overall (57.49%-65.40%), with Claude Opus 4.5 scoring significantly below GPT-5 and Gemini 3 Flash. Gemini 3 Flash's Mindreading accuracy increased with modality, from 65.40% (video-only) to 85.32% (multimodal). Video-only accuracy declined from EU-Emotion to Mindreading across all models, reaching significance only for Claude Opus 4.5. These findings suggest that contemporary LLMs can exceed human-level performance on video and audio-based ToM tasks; however, unimodal models underperform multimodal models, and this is larger on the Mindreading dataset. As LLMs are increasingly deployed in mental health, education, or social assistance contexts, these findings offer novel insights into machine ToM capacities and limitations.

---

## uid: `doi:10.2139/ssrn.7291459`

- title: From Prompts to Reproducible Chemometric Workflows: Evaluating ChatGPT and Gemini for FTIR Spectral Analysis
- authors: Endler  Marcel Borges
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7291459
- keyword hits: chatgpt, gemini, gpt-5, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are increasingly being used to assist with computational data analysis, but their ability to generate complete and reproducible chemometric workflows requires systematic evaluation. This study evaluated the use of Gemini 3.1 Pro and ChatGPT (GPT-5.5) for R-based analysis of ATR-FTIR spectral data. The prompts provided in the manuscript specified the analytical procedures and parameters for spectral preprocessing, principal component analysis (PCA), partial least-squares discriminant analysis (PLS-DA), latent-variable optimization, repeated cross-validation, permutation testing, and classification performance evaluation. The complete R scripts generated from these prompts are provided in the Supporting Information, allowing the generated workflows to be examined and reproduced. Both LLMs were evaluated using identical analytical parameters, including preprocessing procedures, spectral regions, number of latent variables, random seeds, data-splitting procedures, and classification thresholds. Under these controlled conditions, the validation metrics obtained from the two independently generated workflows were identical, demonstrating agreement in the resulting chemometric analyses. An independent FTIR dataset was additionally used to examine the consistency of the generated spectral-processing and PLS-DA workflows. Overall, the study demonstrates the potential of LLMs to generate complete R-based chemometric workflows while emphasizing the importance of providing explicit analytical specifications and independently verifying the generated scripts.

---

## uid: `arxiv:2608.20106v1`

- title: OenoBench: A Wine-Domain Benchmark for Knowledge-Grounded Evaluation of Large Language Models
- authors: Nikita Khudov
- affiliations: not stated
- posted: 2026-08-20
- source: arXiv
- link: https://arxiv.org/abs/2608.20106v1
- keyword hits: claude, deepseek, gemini, large language model, large language models, llm

### abstract

We introduce OenoBench, a wine-domain knowledge benchmark of 3,266 multiple-choice questions across six pillars (regions, grape varieties, viticulture, winemaking, producers, business) and four difficulty tiers. The corpus is built from 38,104 atomic, source-anchored facts extracted by 35 provenance-verified scrapers from government registries (INAO, TTB, OIV), peer-reviewed journals, and Wikipedia/Wikidata. Our methodological contribution is an LLM-driven pipeline in which language models reformat verified facts and audit the result, but never serve as the source of truth: every claim traces to a URL, every question is generated by one of five strategies across five generator families, and every question is scored by a nine-agent audit calibrated against a human gold sheet via Cohen's $κ$. Evaluating sixteen frontier configurations, we find: (i) overall accuracy spans 53%-84%, led by o3 at 83.6%; (ii) reasoning-mode lift concentrates in DeepSeek R1 (+6.8pp) and is absent in Claude Opus and Gemini Pro; (iii) Anthropic shows +9pp self preference on its own questions while Google shows -8pp inverse preference; (iv) frontier open-weight models share the cost-vs-accuracy Pareto frontier with proprietary reasoning models; and (v) every config gains around 33pp on closed-book solvable items, revealing a parametric-recall ceiling that only the contextual slice avoids. We release corpus, audit findings, human-review app, and construction code under CC-BY-SA-4.0.

---

## uid: `doi:10.2139/ssrn.7281921`

- title: Comorbidity Phenotyping from Inpatient Clinical Notes with Large Language Models for Risk Adjustment
- authors: Elliot Martin, Kiarash Riazi, Robin  L. Walker, Catherine Eastwood, Danielle Southern, Na Li, Bing Li, Jeff Bakal
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7281921
- keyword hits: large language model, large language models, llama, llm, llms, prompting

### abstract

Background: Risk adjustment is fundamental to hospital performance measurement, comparative effectiveness studies, and quality improvement. While widely used International Classification of Diseases (ICD)-based algorithms can miss clinically important conditions, electronic medical records (EMRs) contain richer clinical information, yet much of it embedded in unstructured clinical notes. We developed a large language model (LLM)-based framework to identify comorbidities from inpatient EMR clinical notes and evaluated whether these EMR-derived comorbidities improve risk adjustment compared with ICD-based approaches. Methods: We studied 10,659 adult inpatient admissions from Calgary hospitals between 2017 and 2022 using linked chart review, EMR, and discharge abstract data. We developed a framework that combines principled keyword-based text selection and few-shot prompting, and tested it with two open-weight LLMs: Llama 3 70B Instruct and Phi-4. Keywords and LLM outputs were clinically reviewed. Performance was evaluated against chart review labels on a held-out test set of 9594 admissions, and logistic regression risk-adjustment models were compared for in-hospital mortality, unplanned index admission, and 365-day post-discharge readmission. Findings: Compared with ICD-based algorithms, both LLM approaches demonstrated substantially higher sensitivity across most comorbidities while maintaining moderate-to-high positive predictive value. For congestive heart failure as an example, sensitivity was 0.97 for Llama 3 70B Instruct and 0.92 for Phi-4 compared with 0.40 for ICD-based ascertainment. Similar improvements were observed across most comorbidities. In risk-adjustment models accounting for age, sex, and comorbidities, LLM outputs generated c-statistics close to the chart review c-statistics. Interpretation: In a large real-world inpatient cohort, LLM-derived comorbidities from EMR clinical notes improved comorbidity ascertainment for risk adjustment compared with ICD-based comorbidities, achieving performance comparable to chart review. The framework was designed to support health system implementation and can be adapted to other clinical phenotyping tasks.

---

## uid: `arxiv:2608.17051v1`

- title: Institution-Specific LLM Prompting Recovers PHI That De-identification Systems and Their Gold Standards Both Miss
- authors: Daniel Palacios, Matthew Brady Neeley, Angel Adetomike Otto, Shalini Dhamodharan, John P. Woodhouse, Chi-fan Lin, Mark Zobeck, Zhandong Liu
- affiliations: not stated
- posted: 2026-08-17
- source: arXiv
- link: https://arxiv.org/abs/2608.17051v1
- keyword hits: agentic, in-context learning, large language model, large language models, llm, llms, prompting

### abstract

Secondary use of electronic health records requires de-identification, yet existing systems miss \emph{institutionally situated} protected health information (PHI) such as hospital abbreviations, building names, and internal codes whose status is locally determined. We ask whether large language models (LLMs) with in-context learning (ICL) can close this gap and control the precision--recall trade-off. On 100 annotated pediatric oncology notes (5,322 PHI spans) from Texas Children's Hospital, we benchmarked eight LLMs against two purpose-built systems (Stanford TiDE, OpenMed PII) and two pattern-based baselines. Each LLM ran under three prompts of increasing specificity: (1) a HIPAA-aligned baseline, (2) baseline plus the institutional PHI categories it missed, and (3) prompt 2 plus instructions against over-redacting clinical content. We then compared 14~multi-agent and ensemble configurations against the best single prompt, with recall the primary safety metric. LLMs outperformed the purpose-built systems (best F1=0.918$\pm$0.001 vs.\ TiDE 0.779), with advantages concentrated in contextual categories. Naming the missed categories recovered 79\% (48/61) of them, and discouraging over-redaction restored precision. No agentic architecture beat calibrated single-pass prompting (F1 0.906--0.907), but LLM outputs surfaced 414~candidate annotation gaps; re-annotation confirmed 227~PHI spans, against which the final prompt reached recall=0.981 (F1=0.907$\pm$0.002). Well-calibrated ICL resolves both the institutional PHI gap and the precision--recall trade-off in one LLM call per note. LLMs cost more to run than traditional methods, but that cost buys a way to audit the reference standard. LLMs are a legitimate, adaptable alternative to purpose-built de-identification systems; institution-specific prompt development should be the primary adaptation strategy.

---

## uid: `arxiv:2608.17379v2`

- title: PTXBench: Benchmark and Adapt LLMs for GPU Kernel Optimization with Architecture-specific PTX
- authors: Genghan Zhang, Yixin Dong, Chengze Fan, Zhichen Zeng, Yueming Yuan, Shaowei Zhu, Kunle Olukotun
- affiliations: not stated
- posted: 2026-08-18
- source: arXiv
- link: https://arxiv.org/abs/2608.17379v2
- keyword hits: fine-tuning, large language model, large language models, llm, llms, qwen

### abstract

We introduce PTXBench, a benchmark for evaluating and adapting large language models (LLMs) to use architecture-specific PTX for GPU kernel optimization. PTXBench measures functional correctness, whether selected target instructions execute at runtime, and speedup over frontier libraries across GEMM and attention workloads on H100 and B200 GPUs. Our evaluation shows that architecture-specific PTX capability remains uneven: success rates fall substantially on complex attention backward workloads, and executing the target instructions does not necessarily translate into competitive performance. No evaluated model consistently matches frontier libraries across the suite. We further adapt Qwen3.6-27B using supervised fine-tuning. Repair-conditioned training improves several tasks, but generalization remains uneven; data coverage, balance, and the quality of the reasoning teacher matter in addition to dataset size. PTXBench provides an auditable testbed for measuring and improving LLMs' ability to exploit evolving GPU architectures.

---

## uid: `doi:10.2139/ssrn.7309964`

- title: LLM2Spike: Single-Step Spiking Inference for Decoder-Only Large Language Modelsvia Hybrid Dense-Spiking Conversion
- authors: Wanyi Jia, Chenlin Zhou, Qiuyang Chen, Yunhao Ma, Qingyan Meng, Zhengyu Ma, Huihui Zhou
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7309964
- keyword hits: in-context learning, large language model, large language models, llama, llm, llms, qwen

### abstract

Although Large Language Models (LLMs) exhibit strong in-context learning and emergent capabilities, their deployment is still hindered by high computational and energy costs. Event-driven spiking computation provides a promising direction for energy-efficient LLM inference. In this work, we investigate a hybrid artificial neural network to spiking neural network (ANN–to-SNN) framework for decoder-only LLMs, where a pretrained ANN is partially converted into a spiking neural network (SNN) for low-power inference. However, existing ANN-to-SNN conversion methods rely on multi-step simulation, which limits efficiency in low-latency settings. We identify two key challenges for single-step spiking LLM inference: heavy-tailed activation distributions that induce large discretization errors, and the lack of temporal integration in T=1 inference, which leads to progressive error amplification across Transformer layers. To address these issues, we propose a single-step hybrid spiking inference framework. We introduce a spiking neuron tailored to heavy-tailed activations, improving representation accuracy under extreme low-latency inference. We further propose a partial spiking strategy that preserves early Transformer layers in dense form to stabilize information propagation. In addition, we design a subspace-aware distillation method that reduces operator-level error accumulation by focusing supervision on dominant transformation directions. Experiments on LLaMA-2, LLaMA-3.2, and Qwen-2.5 models across six reasoning benchmarks (1.5B–14B parameters) show that our method preserves 97.6% of full-model performance under T=1 inference, while reducing estimated energy consumption by 30.43%. The method scales robustly to 14B models, demonstrating consistent performance across model sizes.

---
