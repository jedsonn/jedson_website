# Classification batch 70 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-70.answer.json` as a JSON array.

---

## uid: `arxiv:2607.06411v2`

- title: RuBench: A Repository-Level Agentic Coding Benchmark with Natively Authored Russian Task Specifications
- authors: Evgeny Shilov
- affiliations: not stated
- posted: 2026-07-07
- source: arXiv
- link: https://arxiv.org/abs/2607.06411v2
- keyword hits: agentic, claude, gemini, gpt-5

### abstract

Developers increasingly delegate real maintenance work to product-grade coding agents, and many state tasks in their native language, in the style of a customer request rather than a curated English issue. We introduce RuBench 1.0, a benchmark of 25 tasks mined from recent fix commits in five live open-source repositories (aiohttp, aiogram, Laravel, NestJS, Fastify), each specified natively in Russian -- written from scratch, not translated -- and judged by the upstream maintainer's regression tests, which we withhold from release. All fix commits postdate the training-data cutoffs of every evaluated model. Round 1 evaluates Claude Code with Opus 4.8, Sonnet 5, and Haiku 4.5, and Codex CLI with GPT-5.5 (3 independent runs each; pass@1 with task-level uncertainty); the best configuration resolves 78.7% of tasks. Auditing full trajectories of an hors-concours configuration (Claude Code + Fable 5), we caught the product silently substituting the model on 20% of tasks via an official safeguard fallback -- evidence that the deployed product, not the model, is the unit actually measured. Version 2 adds Round 2: seven further configurations on the same frozen set under a per-configuration freshness gate -- the Russian-market agents SourceCraft CLI (ds, legacy) and Koda CLI (koda-pro), Antigravity with Gemini 3.1 Pro and 3.5 Flash, and Codex CLI with GPT-5.6 Sol and Luna. SourceCraft's flagship resolves 68.1% (N=23), above GPT-5.5 and both Gemini rows. A tool-call contamination re-audit of all 437 Round-2 trajectories finds the Russian and Gemini columns clean (0/293 cells) while flagging systematic oracle-hunting in the GPT-5.6 family (8/69 and 13/75 cells), including one case of mining a prior round's artifacts from the run machine's disk; honest scores are published alongside raw ones. We release statements, metadata, trajectories, and diffs; oracles are withheld with a SHA-256 manifest.

---

## uid: `doi:10.2139/ssrn.6970578`

- title: A Survey of Financial Large Language Models: From Domain Adaptation to Agentic Financial Intelligence
- authors: Yue Dai
- affiliations: not stated
- posted: 2026-07-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6970578
- keyword hits: agentic, instruction-tuned, large language model, large language models, retrieval-augmented

### abstract

Financial large language models (FinLLMs) have rapidly evolved from domain-adapted encoders for sentiment analysis into instruction-tuned, retrieval-augmented, multimodal, and agentic systems for financial analysis. This survey synthesizes recent work on FinLLMs across data construction, model adaptation, retrieval-augmented generation, benchmarks, applications, and risk control. We organize the literature into six layers: financial corpora and data governance, domain-specific language modeling, financial reasoning and numerical analysis, retrieval and evidence grounding, multimodal and time-series integration, and agentic workflow automation. We also discuss adjacent financial research on analyst information environments, sustainability disclosure, satellite imagery, segment reporting, and volatility modeling, because these domains define realistic use cases and evaluation targets for Fin-LLM systems. Our central argument is that the next generation of FinLLMs should be evaluated less as isolated text generators and more as auditable decision-support systems operating under temporal, regulatory, and economic constraints.

---

## uid: `arxiv:2607.08046v1`

- title: What LLM Forecasters Know but Don't Say: Probing Internal Representations for Calibration and Faithfulness
- authors: Raphaël Sarfati, Pratyush Ranjan Tiwari, Siddharth Boppana, Christopher J. Earls, Srikar Varadaraj, Eric Ho
- affiliations: not stated
- posted: 2026-07-09
- source: arXiv
- link: https://arxiv.org/abs/2607.08046v1
- keyword hits: chain-of-thought, large language model, large language models, llm

### abstract

Large language models fine-tuned for forecasting can be accurate yet poorly calibrated, and their chain-of-thought (CoT) reasoning may not faithfully reflect the evidence behind a forecast. We ask whether internal representations offer a more direct window into both. Working with Eternis-Forecaster 8B on OpenForesight, we train representation-pooling probes on intermediate activations and find they achieve substantially better calibration; a result that also holds for GLM-4.7-Flash and GLM-4.5-Air. We then assess CoT faithfulness through evidence ablation and diversionary injection: removing an influential source in the prompt often changes the model's forecast while leaving the reasoning trace untouched. The same probes function as lie detectors: their activations track behavioral shifts far better than the reasoning trace does, and they also predict the direction of change in 84% of cases, including when the CoT conceals the perturbation's influence. Finally, forced answering reveals that forecasts are largely fixed before reasoning begins: a single pre-reasoning pass recovers the committed answer and confidence, and routing questions by the spread of this pre-set answer distribution saves 30-47% of generated tokens, with no loss of accuracy. Together, these results establish probing internal representations as a practical tool for calibrating, auditing, and triaging language model forecasters and reasoning models more broadly.

---

## uid: `doi:10.2139/ssrn.7091050`

- title: MOP-VQA: Conservative Prompt-View Fusion for Reliable Caption-Based Video Question Answering
- authors: Hui Zhang, Mangang Xie, Xiwen Wang, Jie Xu, Qiangqiang Ma
- affiliations: not stated
- posted: 2026-07-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7091050
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

Caption-based video question answering (VideoQA) reduces visual computation by combining video captions with large language models (LLMs). However, its predictions are highly sensitive to prompt design. Existing prompt ensemble methods improve accuracy but may incorrectly overwrite correct answers, resulting in unreliable predictions. To address this issue, we propose multi-view option-centric prompting video question answering (MOP-VQA), a lightweight training-free framework for reliability-aware prompt fusion. MOP-VQA constructs five deterministic prompt views to provide complementary reasoning. It includes two variants for different deployment goals. MOP-VQA Enhanced Direct Prediction (MOP-VQA-D) improves prediction accuracy through prompt optimization without additional inference cost. MOP-VQA Conservative Multi-View Filtering (MOP-VQA-F) adopts a conservative update strategy to reduce overwrite risk and improve prediction reliability. Experiments on NExT-QA and IntentQA show that MOP-VQA consistently improves caption-based VideoQA. MOP-VQA-D achieves accuracy gains of 1.82\% and 1.47\%, respectively. MOP-VQA-F reduces prediction changes by more than 25\% while obtaining higher overwrite precision on high-consensus samples. These results show that prompt optimization and conservative answer Filtering are both important for building reliable caption-based VideoQA systems. Code, prompt templates, and implementation details are publicly available at https://github.com/Zhxhf/D2-MOP.

---

## uid: `doi:10.2139/ssrn.6942498`

- title: How Large Language Models Surface Personal Brands: An Entity-Signal Framework and Cross-System Analysis of ChatGPT, Claude, and Perplexity
- authors: Bhavik Sarkhedi
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6942498
- keyword hits: chatgpt, claude, large language model, large language models, retrieval-augmented

### abstract

Professional discovery is migrating from ranked link lists to generated answers. When a prospect asks an assistant who the strongest expert in a category is, a large language model returns names, and the mechanism that decides which names appear is not the ranking logic that search engine optimization was built to influence. This paper introduces the AI Visibility Framework (AVF), a six-signal model of citation eligibility that governs whether a personal brand is retrieved, quoted, and recommended inside AI-generated answers across systems such as ChatGPT, Claude, and Perplexity. The six signals are web-wide reputation, source colocation, structured presence, distinctiveness, freshness, and crawl accessibility. Each signal is defined, assigned scoring criteria drawn from practitioner workflows, and weighted by its contribution to citation likelihood. The framework is grounded in entity-knowledge theory in large language models (Petroni et al., 2019; Kandpal et al., 2023) and in retrieval-augmented generation (Brown et al., 2020), and it extends the Personal Brand Equity Index (Sarkhedi, 2026a) by specifying the mechanism through which brand equity converts into machine visibility. Drawing on reported industry data compiled between December 2025 and June 2026, including a 527 percent yearover-year rise in AI referral traffic, the 60 percent of Google searches that end without a click, and the finding that 41 percent of AI-influenced conversions never appear in analytics, the paper argues that the relevant performance indicators shift from traffic to revenue, branded search, and cost per closed deal. A cross-system analysis shows that ChatGPT, Claude, and Perplexity weight sources differently, so visibility must be pursued one engine at a time. The framework is offered as a diagnostic tool for practitioners and as a research agenda for the emerging field of generative engine optimization.

---

## uid: `doi:10.2139/ssrn.7102725`

- title: Multi-agent cooperative centralized management of industrial heat-electrical integrated energy system based on load prediction, incipient fault warning and fault recovery decision
- authors: Jiaxuan Yang, Gangjun Gong, Yuanyuan Li, Zhening Zhang, Yan Liu, Gui Lu
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7102725
- keyword hits: large language model, llm, llms, retrieval-augmented

### abstract

Centralized management is critical for the efficient and safe operation of an integrated energy system. In practice, fragmented management solutions focus on a single aspect of operations, such as load forecasting or fault detection, while overlooking the collaborative management of the entire integrated energy system under real-world operating conditions. To address it, a multi-agent centralized management method based on load prediction, incipient fault warning, and fault recovery decision is proposed for an industrial heat-electrical integrated energy system (IHE-IES), in which two types of agents are designed in this framework: one is a lightweight task-specific (LTS-based) discriminative agent, the other is a large language model-based (LLM-based) generative agent. Specifically, an LTS-based discriminative agent handles real-time specific load prediction and incipient fault warning tasks that require high efficiency and low latency but involve relatively regular patterns well within the capacity of compact models. In contrast, fault recovery decision-making demands reasoning over specialized domain expert knowledge across different industrial subsystems in IHE-IES and the generation of structured, professional fault logs. Based on the LTS-based discriminative agent’s prediction and detection results, an LLM-based generative agent, embedded with an IHE-IES fault knowledge graph retrieval-augmented generation (RAG) approach, is developed to provide professional, structured, and context-aware fault recovery decisions. Comparative experiments demonstrate that the proposed management method achieves superior performance. For load prediction, the accuracy improves by an average of 32.51% and 19.36% compared to state-of-the-art methods on short- and long-term prediction. For the incipient fault warning, the fault detection rate increases by an average of 8.93%. For fault recovery decision-making, the proposed agent demonstrates better fault recovery generation capability than LLMs with equivalent parameter counts. As one of the first few studies to cooperate multiple agents in IHE-IES operation management, it provides a novel, effective centralized operation management scheme for IHE-IES.

---

## uid: `doi:10.2139/ssrn.7113405`

- title: A Multi-strategy Semantic Enhancement Method with Genetic Algorithm and Dempster-Shafer Theory: A High-Quality Instruction Set Construction Framework for Predictive Maintenance LLM Fine-Tuning
- authors: Shen Hong, Zhang Jiacheng, Wu Jiaqian, Hou Yisha, Gan Chenyu, Xiaodong Zhang
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7113405
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

With the rapid development of Large Language Models (LLMs), the scarcity of high-quality Supervised Fine-Tuning (SFT) data emerges as a critical bottleneck restricting the improvement of model performance. Existing automated data synthesis methods face challenges such as domain semantic fragmentation, severe instruction homogeneity, and lack of interpretability in quality evaluation. In intelligent manufacturing and predictive maintenance scenarios, production scheduling, equipment condition monitoring, and maintenance decision-making are highly coupled. Complex mappings exist among sensor time-series data, failure modes, and downtime costs, imposing higher requirements on the cross-modal semantic representation and complex decision reasoning capabilities of instruction data. Hence, this paper proposes a full-cycle intelligent data construction framework, and an end-to-end system named IntelliData-Forge generates high-quality fine-tuning instruction datasets. First, this paper proposes an adaptive chunking algorithm based on structural entropy and semantic coherence for unstructured long documents, which incorporates a reinforcement learning strategy optimizer to maximize the preservation of contextual integrity. Second, this paper introduces an instruction evolution engine that uses a genetic algorithm integrated with MAP-Elites to achieve directional expansion within the complexity and topic spaces through multi-dimensional crossover and mutation operators. Finally, this paper constructs a multi-dimensional quality evaluation system based on Dempster-Shafer (DS) evidence theory, which utilizes the conflict coefficient K to quantify evaluation uncertainty and trigger an active learning mechanism, thereby achieving closed-loop monitoring of data quality. The experimental results demonstrate that IntelliData-Forge outperforms existing baseline methods across multiple key metrics, including RUL prediction error, fault classification accuracy, decision consistency, and instruction diversity. In particular, the RUL prediction error decreases significantly, while fault classification accuracy and decision consistency achieve substantial improvements.

---

## uid: `doi:10.2139/ssrn.7113516`

- title: Event Log Extraction from Unstructured Enterprise Messaging Using LLMs
- authors: Juntao Gao
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7113516
- keyword hits: large language model, llm, llms, retrieval-augmented

### abstract

High-quality event logs are essential for process mining, yet critical business information increasinglyresides in customer service conversations.Existing extraction methods based on Large LanguageModels (LLMs) struggle with hallucination and domain-knowledge gaps when processingsuch conversational text. We propose an LLMs-driven event log extraction framework purposebuiltfor customer service conversations. It orchestrates a retrieval–extraction–verificationpipeline: Retrieval-Augmented Generation (RAG) injects external domain knowledge to groundactivity recognition; a Self-Consistency module aggregates ten independent extraction passesthrough confidence-weighted voting. A dedicated verification Large Language Model (LLM)then adjudicates low-confidence predictions, jointly suppressing hallucination and recognitionerrors. Across three public customer-service dialogue datasets, LLMs-based Event Log ExtractionMethod (LLMs-EEM) attains an average F1-score of 93%, surpassing the NLI-BARTbaseline by 4 percentage points and standalone LLM methods by 8 percentage points. Theseresults confirm that the multi-stage collaborative design simultaneously improves extractionaccuracy and robustness in complex conversational environments.

---
