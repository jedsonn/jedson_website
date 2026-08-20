# Classification batch 2 of 22, edition 21

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-021/batch-2.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7257278`

- title: How Large Language Models Work: Architecture, Training, and Applications
- authors: Aditya Mane
- affiliations: not stated
- posted: 2026-08-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7257278
- keyword hits: claude, fine-tuning, gemini, large language model, large language models, llm, llms

### abstract

Over the last few years, Large Language Models like GPT, Claude, and Gemini have gone from research curiosities to tools people use every day, for writing, coding, and even analyzing data. But most users, and even a lot of students studying AI, don't really know what's happening inside these systems when they generate a response. This paper tries to unpack that process in a way that's technical enough to be useful but doesn't require a background in advanced mathematics. It walks through how NLP evolved into the Transformer architecture, what tokenization and embeddings actually do, how the self-attention mechanism lets a model understand context, and how models are trained through pretraining, fine-tuning, and RLHF. It also touches on where these models are used in practice and where they still fall short-hallucination, bias, and the sheer computational cost involved. The goal is a clear, grounded explanation of how LLMs actually work, not just what they can do.

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

## uid: `doi:10.2139/ssrn.7286578`

- title: Responsible Adoption of Generative Artificial Intelligence in Customer Care Services: Evidence from Vietnamese Commercial Banks and Managerial Implications
- authors: An Nguyen Hoang Phuong
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7286578
- keyword hits: generative artificial intelligence, large language model, large language models, llm, llms, retrieval-augmented

### abstract

Generative Artificial Intelligence (GenAI) and Large Language Models (LLMs) haveemerged as transformative technologies capable of fundamentally reshapingcustomerservice operations within the financial services sector. This study investigates thestrategic adoption of GenAI in customer care services across Vietnamese commercial banks, identifying operational bottlenecks and establishing a responsible implementationframework. Employing a qualitative exploratory methodology combining desk research andmultiple-case study analysis of three digitally proactive institutions—Military Commercial JointStock Bank (MBBank), Tien Phong Commercial Joint Stock Bank (TPBank), andVietnamTechnological and Commercial Joint Stock Bank (Techcombank)—the paper examines organizational and technological foundations prerequisite to advanced AI adoption. The findings indicate that while GenAI substantially enhances conversational quality, contextual understanding, and customer journey continuity, its sustainable valueisfundamentally constrained by data governance maturity and integration architecture. Toresolve these friction points, this study proposes a five-layer ResponsibleGenAI Adoption Framework incorporating Retrieval-Augmented Generation (RAG) architectureand Human-in-the-loop (HITL) oversight mechanisms, formalized through four researchpropositions. The study provides actionable managerial implications for commercial banking executives and regulatory recommendations for policymakers in emergingfinancial markets.

---

## uid: `doi:10.2139/ssrn.7291518`

- title: AI-Driven Financial Infrastructure How LLMs, Deep Learning, and Autonomous Agents Reshape Payments, Credit, and Market Microstructure
- authors: Hunter Hughes
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7291518
- keyword hits: agentic, generative ai, large language model, large language models, llm, llms

### abstract

"AI in finance" is treated as a single diffusion. It is three occupations of three different layers, running on three clocks. Deep learning already prices credit and scores fraud. Large language models now read the unstructured remainder-filings, chat, policy, code. Agents want to initiate payments and trades. The IIF-EY survey of 61 institutions in October 2025 finds 90 percent of firms with AI in production and, among those, generative-AI production at 84 percent, up from 48 percent a year earlier. Agentic systems are in production at 23 percent. Primary investment still sits in predictive models: 60 percent of firms, against 34 percent in generative AI. That ranking is the finding, not a lag. Scoring is a probabilistic task that financial firms have been doing with neural nets since the 1990s. Settlement is not. The IMF three-layer map-intent, authorisation, settlement-is the right decomposition. Agents belong in the first layer. The second and third must remain deterministic or the rail stops being a rail. Credit is the intermediate case. FinRegLab shows that XGBoost lifts ROC-AUC by about two points over logistic regression on the same bureau file, and that a cash-flow hybrid on top of that is another few tenths. Machine learning increased simulated approvals by nearly 4 percent and cut approved defaulters by at least 9 percent. That is a better scorecard. It is not a new credit market, and it is not a fair-lending regime. Market microstructure is the layer where the three generations collide. High-frequency systems have been agentic in a narrow sense for fifteen years. What is new is an LLM that can read a headline, write an order, and share a prompt template with every other desk that bought the same model. The Financial Stability Board named the resulting vulnerabilities in 2024: third-party concentration, correlated behaviour, cyber, and model risk. The policy error is to regulate "AI" as a capability. Regulate the layer it is allowed to occupy.

---

## uid: `arxiv:2608.17379v1`

- title: PTXBench: Benchmark and Adapt LLMs for GPU Kernel Optimization with Architecture-specific PTX
- authors: Genghan Zhang, Yixin Dong, Chengze Fan, Zhichen Zeng, Yueming Yuan, Shaowei Zhu, Kunle Olukotun
- affiliations: not stated
- posted: 2026-08-18
- source: arXiv
- link: https://arxiv.org/abs/2608.17379v1
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

## uid: `doi:10.2139/ssrn.7315788`

- title: Knowledge-Guided Document-Level Relation Extraction with LLMs:A Benchmark-Driven Survey of Semantic, Graph-Based,Ontology-Based, and Agentic RAG
- authors: Gabriel Medeiros, Cecilia Zanni-Merk
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7315788
- keyword hits: agentic, large language model, large language models, llm, llms, prompting, retrieval-augmented

### abstract

Document-level relation extraction is a central step for transformingunstructured text into structured knowledge that can support knowledgegraphs, decision support systems, and explainable artificial intelligenceapplications. Recent large language models have made relation extractionmore flexible through zero-shot and few-shot prompting, but their predictionsoften remain weakly grounded, difficult to validate, and sensitive tohallucinations when relations depend on multi-sentence evidence or domainknowledge. In parallel, retrieval-augmented generation, knowledge graphs,ontologies, and agentic workflows have introduced new mechanisms forgrounding, semantic control, and provenance-aware prediction. However,existing surveys usually study relation extraction, retrieval-augmentedgeneration, graph-based retrieval, ontology-guided reasoning, and agenticRAG as separate research lines. This paper addresses this gap through abenchmark-driven survey of knowledge-guided document-level relationextraction with LLMs. It first proposes a taxonomy that organizes methodsinto LLM-only extraction, flat semantic retrieval, ontology-guided RAG,knowledge graph-based RAG, agentic RAG, and validation-orientedneuro-symbolic pipelines. It then introduces RAGTree, a unified benchmarkframework that adapts representative strategies from these families to acommon relation extraction protocol. Experiments are conducted withgpt-oss-20B on MAVEN-ERE, EventStoryLine, FinCausal, DocRED, andCausalBank, using micro-averaged precision, recall, and F1. The observedresults do not identify a single strategy as strongest across all datasets.Ontology-guided, knowledge graph-based, and agentic methods providecomplementary advantages under different dataset conditions, whileretrieval alignment, recall limitations, and orchestration complexityremain open challenges.

---
