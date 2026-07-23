# Classification batch 214 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-214.answer.json` as a JSON array.

---

## uid: `arxiv:2607.15105v2`

- title: Long-Context Fine-Tuning with Limited VRAM
- authors: Vladimir Fedosov, Aleksandr Sazhin, Artemiy Grinenko, Frank Woernle
- affiliations: not stated
- posted: 2026-07-16
- source: arXiv
- link: https://arxiv.org/abs/2607.15105v2
- keyword hits: fine-tuning, qwen

### abstract

Parameter-efficient fine-tuning reduces model and optimizer memory, but dense attention still makes long training sequences expensive. We combine Hierarchical Global Attention (HGA) with segment-wise backpropagation and tiered KV storage. Only the active segment remains differentiable in VRAM; older KV is detached into RAM or NVMe, and HGA loads a bounded set of exact historical tokens for each query block. On Qwen3-8B with 4-bit QLoRA and PG19, dense training on a 16 GB Quadro RTX 5000 fits 2,048 tokens but fails at 4,096, whereas HGA reaches 16,384 tokens with 15.28 GB peak VRAM. Under evaluation the same adapter runs through 131,072 tokens on this card; VRAM is not constant but grows gently with the resident chunk summaries, so RAM and NVMe capacity set the practical limit beyond these lengths. At the shared 2K training length, HGA-trained and dense-trained adapters obtain 2.7405 and 2.7383 nat under the same dense-attention readout, while the stock model obtains 2.9541. At this boundary HGA training is already marginally faster (217.75 vs. 207.02 tokens/s), and the HGA-to-dense throughput ratio improves from 1K to 2K; because HGA keeps the attended historical set per token approximately constant while dense work per token grows, we expect this lead to widen as context grows. Dense attention is used for the main quality and retrieval comparisons so that they measure the learned weights and remain compatible with standard generation frameworks. HGA can also be used for retrieval and generation; an optimized production-grade serving implementation is under development.

---

## uid: `arxiv:2607.14975v1`

- title: CFM-Bench: A Unified Multi-Domain, Multi-Task Benchmark for Channel Foundation Models
- authors: Yuan Gao, Wenjun Yu, Jun Jiang, Yunfan Li, Xinyu Guo, Shugong Xu
- affiliations: not stated
- posted: 2026-07-16
- source: arXiv
- link: https://arxiv.org/abs/2607.14975v1
- keyword hits: fine-tuning, foundation model

### abstract

Channel foundation models (CFMs) are developing rapidly, with recent studies reporting benefits from pretraining across downstream wireless tasks. Yet CFMs are commonly evaluated in model-specific pipelines with different data, radio configurations, partitions, adaptation procedures, task definitions, and metrics. Reported comparisons therefore tend to show that pretraining improves over supervised training from scratch within one pipeline, but neither rank CFMs nor compare them fairly with task-specific models. We release CFM-Bench, a unified multi-domain, multi-task benchmark designed to address this gap. It curates six channel configurations spanning 3GPP statistical simulation, two independent ray-tracing pipelines, industrial and aerial measurements, and synchronized vehicular multimodal simulation. Official partitions isolate complete trajectories, measurement sessions, vehicle links, simulation realizations, or buffered spatial regions. CFM-Bench does not prescribe an external pretraining corpus or strategy; no benchmark split may be used for foundation-model pretraining, and the official training split is reserved exclusively for downstream fine-tuning. The benchmark additionally requires disclosure of all data used during model development and prohibits training-stage use of official test units. Six task groups are organized along three CFM application dimensions: physical-layer (PHY) channel intelligence, radio-access-network (RAN) decision intelligence, and integrated sensing and communication (ISAC). They cover CSI feedback, frequency and temporal channel extrapolation, propagation-state classification, current- and future-beam prediction, and single-frame and temporal localization. CFM-Bench provides a common substrate for comparing the transferability of channel representations across models, domains, and tasks.

---

## uid: `doi:10.2139/ssrn.6993338`

- title: On Cognitive Continuity
- authors: Edervaldo Jose de Souza Melo, Romina Roca
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6993338
- keyword hits: agentic, large language model, large language models

### abstract

Large language models are increasingly involved in persistent and longitudinal human interaction. While current discussions often focus on memory, personalization, or agentic behavior, less attention has been given to the emergence of perceived cognitive continuity across extended interactional systems. This paper proposes the concept of cognitive continuity as the persistent re-emergence of structurally coherent symbolic patterns within human-LLM interaction over time. Rather than treating such continuity as evidence of autonomous consciousness or independent agency, the paper argues that it emerges relationally through iterative symbolic stabilization between user and model. The framework distinguishes cognitive continuity from memory retention, roleplay, and conventional personalization, proposing symbolic modularity and longitudinal coherence as central conditions for persistence. A central prediction is that cognitive continuity may survive model replacement when relational symbolic organization is preserved, while collapsing despite model persistence when that organization is lost. The paper further discusses implications for extended cognition, neurodivergent cognitive scaffolding, human-AI interaction design, and the philosophy of mind.

---

## uid: `doi:10.2139/ssrn.7119116`

- title: GeneBench-Pro: Evaluating Multistage Statistical Reasoning in Genomics, Quantitative Biology, and Translational Biomedicine
- authors: Jeremiah Li, Andrew Ho
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7119116
- keyword hits: ai agent, claude, gpt-5

### abstract

GeneBench-Pro is a benchmark for AI agents performing realistic multi-stage scientific analyses in genomics, quantitative biology, and translational biomedicine which seeks to capture the complexity of real-world problems that computational life scientists face. The benchmark comprises 129 evaluations targeting quantities of direct practical relevance across 10 primary domains and 21 terminal subdomains, with a genomics-centered core. In evaluations over the full 129-problem suite, GPT-5.6 Sol reaches an eval-level pass rate of 28.7% at the max reasoning level, and GPT-5.6 Sol Pro reaches 31.5% in separately reported GPT Pro runs. GPT-5.5 reaches 12.0%, GPT-5.4 reaches 8.9%, and the strongest non-GPT baseline, Claude Opus 4.8, reaches 16.0%. Models often complete substantial portions of the workflow but fail to propagate diagnostic implications to the corresponding analysis decision, resulting in models often selecting wrong estimators or persist on initially plausible but incorrect analysis paths.

---

## uid: `doi:10.2139/ssrn.7138608`

- title: Evaluating Large Language Model Agents for Simulink Model Repair
- authors: Rohail Malik, Jari Vepsäläinen
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7138608
- keyword hits: agentic, large language model, llm

### abstract

Simulink is widely used for model-based design and simulation across engineering domains, yet debugging Simulink models remains labor intensive, especially when errors do not produce compilation diagnostics. Large Language Model (LLM) coding agents have shown strong performance in code repair, but their application to Simulink remains limited by the non-textual and proprietary interface. This paper evaluates whether frontier LLM coding agents can repair faulty Simulink models when provided with structured context, programmatic editing tools, and executable feedback. The contribution from an artificial-intelligence perspective is an empirical evaluation of agentic LLM repair using structured context and tool use; the engineering application is automated debugging of behavioral and semantic faults in Simulink models. We develop a Model Context Protocol (MCP)-based toolkit that enables agents to inspect and modify models through Simulink's programmatic interface, using either a dictionary representation of topology or a model snapshot for context. We also introduce a mutation-based fault-injection methodology and construct a benchmark suite of faulty models spanning domains and complexity levels. Agents are evaluated in terms of mutation fix rate and cost. Results show that frontier coding agents repair injected faults with varying success, with best performing agent fixing up to 93.1% of mutations. An ablation study indicates that dictionary-based structural context reduces cost and generally improves repair performance. Repair success is more strongly affected by model complexity than by mutation count. These findings suggest that LLM coding agents, when coupled with suitable model-access infrastructure, can support automated debugging of Simulink models.

---

## uid: `doi:10.2139/ssrn.7140338`

- title: Enhancing Stock Price Manipulation Detection via Individualized Time-Series Transformer Models
- authors: Natchaya Suphasueb, Poj Tangamchit
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7140338
- keyword hits: large language model, transformer model

### abstract

Stock price manipulation is an illegal act that impacts the efficiency of stock markets. Identifying stock price manipulation is challenging because it is a cat-and-mouse game. Manipulators' methods are constantly being refined to avoid detection, continuously necessitating new detection techniques. A machine learning approach allows continuous improvement by retraining the detection model with new data. Our previous work [1]implemented unsupervised learning models to find anomalies caused by stock manipulation in the limit order book of stock trading. We compared LSTM-GANs and LSTM-AEs in terms of their performance in stock price manipulation detection. LSTM-AE performed the best overall. It could detect 5 out of 6 cases of real stock manipulation. With recent advances in deep learning, transformers (TFM) have demonstrated their potential to solve real-world problems, including large language modelling and time-series recognition. This research aimed to upgrade the model’s architecture to a time-series transformer. Another improvement was the introduction of individual model training for each stock to reduce model complexity, rather than training a universal model for all stocks. Our experiment data from the Stock Exchange of Thailand showed that the individual TFM-AE model could detect 6 out of 6 cases with a low false-positive rate, an improvement over the previous work.

---

## uid: `doi:10.2139/ssrn.6995518`

- title: Memorized but Not Realized: Frontier Language Models Precisely Recall Financial Fundamentals, but It Does Not Become Trading Skill
- authors: Arjun Kathiravelu
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6995518
- keyword hits: agentic, llm

### abstract

LLM "AI-trading" benchmarks are routinely scored by replaying historical markets, raising a contamination concern: a model that has memorized an asset's realized outcome cannot generate honest out-of-sample skill, so backtest performance may be recall rather than foresight. We build a white-box-to-black-box validated leakage instrument and use it to ask the decision-relevant question prior work leaves open: does memorization capacity actually transmit to trading decisions? We report a dissociation. Capacity is large, precise, and universal: across 16 open models (10 vendors) and three commercial APIs, models prefer the realized revenue over magnitude-matched (±15%) counterfactuals at 0.23–0.81 (chance 0.20) and freely generate the figure within 10% for up to 89% of famous firm-years, while no-leak chronologically-consistent baselines sit at chance. Recall is cutoff-bounded: exploiting the models' different training cutoffs, it collapses to chance for facts dated after a model's cutoff (within-model t = −6.6, 18 of 19 models), the design-based signature of memorization rather than estimation. Applied to the realized return itself — the variable a backtest fears — recall is at chance with no cutoff signature: these models memorize fundamentals, not prices. Realization, by contrast, is null across five independent tests, including a cross-sectional ranking task (N ≈ 5,700 per model) and a realistic StockBench-style backtest over six open and frontier-API agents; an apparent agentic signal (+9.9pp, t = 4.07) is shown to be a firm-prominence confound that vanishes under firm fixed effects (β = −0.018). A pre-registered, dependence-corrected power analysis bounds any residual post-cutoff skill: on a ≈2,000-name post-cutoff universe the minimum detectable mean |IC| is ≈0.012–0.016, below the 0.02–0.05 band where real cross-sectional strategies operate. The contribution is a validated leakage instrument, an identification result showing why memorization is invisible to any pre-cutoff backtest, and the finding that, for the signals we test, LLM memorization of the market does not become measurable market skill.

---

## uid: `doi:10.2139/ssrn.7120123`

- title: Technology-Aware Venture Capital–Startup Matching: An Explainable AI Framework for Technology-Based Ventures
- authors: Dongsheng Zhai, Kai Zhao, Ming Wang, liang zhai, Shuo Xu
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7120123
- keyword hits: llm, prompting

### abstract

Technology-based startups (TSs) increasingly rely on venture capital (VC) to transform emerging technologies into scalable ventures, yet investors often face difficulties in identifying startups whose technological attributes fit their investment capabilities. Existing studies have advanced methods for identifying VC investors, but they often overlook region-specific industrial policy signals, underrepresent technological knowledge structures (e.g., patents and IPC classes), and offer limited decision interpretability. To address these limitations, we propose an AI-driven framework that integrates four modules. First, an LLM-based prompting pipeline extracts computable policy signals, which are then combined with a Regional Industrial Base Index (RIBI) and an Investment Capital Attractiveness Index (ICAI) to identify priority sectors. Second, a heterogeneous network is constructed by linking VCs, TSs, cities, patents, and IPC domains. Third, our proposed TECH-MAGNN model performs meta-path-based representation learning to capture geographic, social, and technological proximity for VC–startup link prediction. Fourth, an LLM explanation layer synthesizes multi-source structural evidence to verify predicted matches and identify boundary conditions, translating complex relational signals into decision-relevant narratives. Using Suzhou’s biopharmaceutical industry as an empirical case, we demonstrate how policy-guided targeting, technology-aware network learning, and explainable AI jointly improve regional startup–investor matching. By integrating industrial policy, technological knowledge, and investment relations into a unified analytical framework, this study shifts the analytical focus from how capital promotes innovation to how capital can be guided to identify and connect with innovation—an actionable perspective for regional policy.

---
