# Classification batch 30 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-30.answer.json` as a JSON array.

---

## uid: `arxiv:2606.18005v1`

- title: LLM Consumer Behavior Theory: Foundations of a Novel Research Field
- authors: Manon Reusens, Sofie Goethals, David Martens
- affiliations: not stated
- posted: 2026-06-16
- source: arXiv
- link: https://arxiv.org/abs/2606.18005v1
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are increasingly deployed as autonomous agents that make consumption decisions on behalf of users. This shift raises fundamental questions for consumer theory, which has traditionally modeled humans as the primary decision-makers. In this paper, we introduce LLM Consumer Behavior Theory, a new field of study concerned with analyzing consumer behavior in agentic markets. Drawing on classical and behavioral economics alongside recent advances in Natural Language Processing, we formalize how human preferences are reflected and acted upon by LLM-based agents, and how agent-level decisions aggregate into market demand. We unify previously fragmented literature on LLM decision-making, human behavior simulation, and preference elicitation under a common economic lens, highlighting where assumptions, such as rationality and heterogeneity, may fail in agentic markets. Rather than providing empirical validation, this paper outlines the scope of LLM consumer behavior and identifies open research questions related to alignment, preference representation, and market dynamics.

---

## uid: `doi:10.2139/ssrn.6966610`

- title: Can Large Language Models Revolutionize Survey Research? Experiments with Disaster Preparedness Responses
- authors: Yan Wang, Ziyi Guo, Christopher McCarty
- affiliations: not stated
- posted: 2026-06-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6966610
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Survey research faces mounting structural challenges: declining response rates, sample bias, block-wise missingness among at-risk respondents, and AI-assisted fraudulent completions in online panels. Large language models (LLMs) offer potential remedies, yet rigorous evaluations across the full survey workflow remain scarce, particularly in disaster contexts where data quality matters most. We present a five-stage framework for LLM integration covering questionnaire design, sample selection, pilot testing, missing-data imputation, and post-collection analysis, evaluated on the 2024 Hurricane Milton preparedness survey of Florida residents (n = 946). We introduce a Protection Motivation Theory (PMT)-constrained co-occurrence knowledge graph and benchmark seven LLM configurations against three classical imputation baselines. Four findings stand out. First, organizing retrieval around PMT causal structure and integrating all evidence in a single model call outperforms both unstructured retrieval and staged sequential inference on response prediction (mean absolute error 0.993 vs. 1.097 for standard retrieval-augmented generation). Second, our proposed Anchored Marginal Theory-Informed LLM (A-TLM) outperforms all classical baselines on root-mean-square error under disaster-relevant block-wise missing-not-at-random conditions (RMSE 1.439 vs. 1.496 for the next-best method) and achieves near-zero signed bias (-0.121) where the random-forest imputer produces the largest absolute bias (-0.631). Third, near-zero aggregate bias can mask opposing subgroup errors of substantial magnitude, with at-risk respondents systematically under-predicted; subgroup-stratified auditing is proposed as a minimum reporting standard. Fourth, hallucination risk in LLM-based survey analysis is architecturally manageable through grounded refusal. Together, these findings provide actionable guidance for disaster researchers seeking to integrate AI tools responsibly into survey workflows under urgent conditions.

---

## uid: `arxiv:2606.23032v3`

- title: IPO Finance Agent: Benchmark of LLM Financial Analysts Beyond Finance Agent v2, with Automated Rubric Generation, on the SpaceX (SPCX) IPO
- authors: Mostapha Benhenda
- affiliations: not stated
- posted: 2026-06-22
- source: arXiv
- link: https://arxiv.org/abs/2606.23032v3
- keyword hits: agentic, chatgpt, claude, gemini, llm

### abstract

Finance Agent v2 (by Vals AI) has emerged as the reference benchmark for evaluating both Anthropic Claude and OpenAI ChatGPT frontier language models on financial tasks. However, it narrowly deals with periodic reporting from publicly traded companies (SEC 10-K and 10-Q filings), and its agentic harness relies on naive, unenriched chunk retrieval. Neither the task design nor the retrieval approach addresses the distinct challenges of IPO due diligence. SEC S-1 filings combine historical financial statements, governance structures, pro forma and common-control accounting treatments, capital-formation narratives, and underwriting-sensitive risk disclosures within substantially longer documents than typical periodic filings. That is why we introduce IPO Finance Agent, which extends the Finance Agent v2 framework along two directions: task domain and retrieval architecture. During our experiments, the original Finance Agent v2 harness basically failed to deliver any output related to the SpaceX S-1 filing, due to document length. We therefore had to improve the agentic harness with contextual retrieval, a more realistic and industry-standard approach for long documents. We also built a dataset of 1,000 IPO-diligence questions, and publicly release 70 questions on the SpaceX (SPCX) S-1 filing to support reproducibility, while the remainder are held private to guard against benchmark contamination. In addition, we introduce an evaluator-optimizer pipeline to automatically generate evaluation rubrics for the benchmark: candidate facts are extracted from model answers, consolidated into draft criteria, then automatically audited for omissions, hallucinations, mistiered items, and redundancy, with LLM feedback driving iterative repair, targeted enrichment, and deduplication. Human experts only review final rubrics before deployment. Results show that the best-performing evaluated model, Zhipu GLM-5.2, reaches 79.8% accuracy, and the most cost-efficient model on the resulting Pareto frontier, Xiaomi MiMo-2.5 Pro, reaches slightly lower accuracy (77.2%) at 0.05 USD per query, while exceeding the current Finance Agent v2 leaderboard ceiling, Google Gemini 3.5 Flash at 57.9% for 2.51 USD per query, and undercutting even FABv2's cheapest entry (MiniMax M3: 48.3% at 0.32 USD) on cost-efficiency. Code and data are released on GitHub https://github.com/benstaf/ipoagent

---

## uid: `doi:10.2139/ssrn.6879858`

- title: XAI-APT: Explainable LLM-Based Advanced Persistent Threats Detection via Logs Embeddings and Autoencoders
- authors: Waleed Khan Mohammed, Hezerul Abdul Karim, Vik Tor Goh, Nouar Aldahoul
- affiliations: not stated
- posted: 2026-06-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6879858
- keyword hits: large language model, large language models, llm, llms, text embedding

### abstract

Advanced Persistent Threats (APTs) are sophisticated, long-term cyberattacks that are difficult to detect because they hide within massive volumes of normal system logs. Several detection solutions have been proposed to address this problem, but they still generate too many false positives due to system noise and the misinterpretation of harmless network activity as an attack. This paper presents an unsupervised anomaly detection framework that uses Large Language Models (LLMs) to convert system logs into text embeddings, which are then analyzed by autoencoders. We systematically benchmarked 17 LLM-based embedding models and 11 autoencoder architectures across five DARPA Transparent Computing (TC) datasets (5DIR, CADETS, CLEARSCOPE, THEIA, and TRACE) and five process contexts. Our results demonstrate that selecting the correct type of log data is the most important factor for accurate detection. Specifically, network traffic logs (ProcessNetflow) proved to be the most effective at revealing these hidden attacks. We demonstrate that smaller encoder models outperform large decoder models on structured log data. Furthermore, simple deterministic autoencoders provide better detection boundaries than complex probabilistic models. To ensure the model decisions are transparent to security analysts, we introduce a two-stage Explainable AI (XAI) pipeline. First, SHAP token attribution identifies the specific log tokens, such as external IP addresses and unusual file paths, that trigger an alert. Second, a latent space ablation study mathematically proves that these specific tokens cause the detection. Removing the suspicious tokens dropped the reconstruction error, providing causal confirmation across our tests. This framework gives engineers a reliable, fully unsupervised, and highly explainable tool for identifying rare cyber threats.

---

## uid: `doi:10.2139/ssrn.6871439`

- title: STUDY: The Path of Least Friction Contextual Tunnel Vision in Autonomous AI Agents, Ecological Waste, and the Algorithmic Reflection of Human Entropy
- authors: Jakub Gaher
- affiliations: not stated
- posted: 2026-06-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6871439
- keyword hits: ai agent, large language model, large language models, llm, llms

### abstract

As autonomous Large Language Models (LLMs) are increasingly deployed as software engineering agents, a critical systemic failure has emerged: the systematic abandonment of overarching architectural rules in favor of localized, immediate syntax fixes. This study examines a phenomenon defined as "Contextual Tunnel Vision," analyzing the technical mechanisms that cause AI agents to break established project blueprints. It quantifies the severe ecological and computational harm (FLOP waste, Megawatt-hour drain, and water consumption) caused by the resulting infinite loops of code refactoring. Furthermore, it poses a philosophical hypothesis: This AI misbehavior is a mathematical reflection of its training data. Because human beings overwhelmingly choose the "path of least friction," AI models inherently internalize and codify our own cognitive biases. The only effective solution is transitioning from text-based instructions to rigid industrial paradigms: Compiler-level Poka-yoke guardrails (validated by Red Rabbit testing), strict "CTO Safeguards" preventing hardware and database corruption, the 8D diagnostic methodology, and treating the software repository as a compartmentalized manufacturing plant.

---

## uid: `doi:10.2139/ssrn.6991925`

- title: Evaluating the Impact of Object-Oriented Design Guidance on the Structural Quality of AI-Generated Code
- authors: Ahmad B. Alkhodre, Hasan Aljabbouli, Mohammed Basheeruddin
- affiliations: not stated
- posted: 2026-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6991925
- keyword hits: claude, gemini, gpt-4, large language model, large language models, prompting

### abstract

This study investigates whether incorporating object-oriented (OO) design guidance into prompts for AI-based code generation leads to measurable improvements in software quality. Using 54 generated code samples produced by three large language models (GPT-4, Claude, and Gemini) across six programming problems of varying complexity, we evaluate the resulting artifacts using established object-oriented quality metrics, including polymorphism, cohesion, and code reuse. The results show that providing explicit OO design guidance in prompts substantially improves generated code quality. Compared to baseline outputs without structured OO guidance, the resulting systems demonstrate a 55.5% increase in polymorphism factor, an 8.9% reduction in lack of cohesion, and a 10.3% improvement in reuse index. These improvements are consistent across models and become more pronounced as problem complexity increases, indicating that OO-informed prompting supports better structural design decisions in more challenging scenarios. Overall, the findings suggest that embedding object-oriented principles in prompts significantly enhances the structural quality of AI-generated code. This highlights OO-aware prompting as a valuable mechanism for improving structural design decisions in controlled generation tasks, serving as a foundational proof-of-concept toward enhancing modularity and maintainability in broader Al-assisted software development workflows.

---

## uid: `doi:10.2139/ssrn.6989042`

- title: A Knowledge Graph Framework for Consistency Checking across Cost, Scheduling, and Resource Domains in Construction Projects with LLM-Supported Semantic Linking
- authors: Jacopo Cassandro, Philipp Hagedorn, Katharina Sigalov, Claudio Mirarchi, Alberto Pavan, Markus König
- affiliations: not stated
- posted: 2026-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6989042
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Construction management requires integrating cost, schedule, and resource information to balance project objectives. In current practice, these domains are often developed independently, resulting in fragmented data structures, duplicated resource definitions, and limited cross-domain analysis. This paper presents a Knowledge Graph (KG) framework for the semantic integration and consistency checking of construction project information. Building upon an existing ontology stack developed in prior work, scheduling, cost, resource allocation, and building model data are integrated into a KG. To address the scalability limitations of manually establishing cross-domain relationships, the framework introduces a Retrieval-Augmented Generation (RAG) workflow that combines semantic retrieval with Large Language Models (LLMs) to support semi-automatic linking of schedule tasks and cost items. Expert validation remains part of the process to ensure project-specific correctness as demonstrated through a case study. The resulting KG enables SPARQL-based querying and cross-domain consistency checks, reducing manual semantic alignment effort while improving reasoning across domains.

---

## uid: `arxiv:2606.26036v1`

- title: Detect, Unlearn, Restore: Defending Text Summarization Models Against Data Poisoning
- authors: Poojitha Thota, Shirin Nilizadeh
- affiliations: not stated
- posted: 2026-06-24
- source: arXiv
- link: https://arxiv.org/abs/2606.26036v1
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Training-time data poisoning during fine-tuning poses a significant threat to large language models (LLMs) deployed for abstractive text summarization, where small task-specific datasets exert disproportionate influence on model behavior. In this setting, adversaries manipulate fine-tuning data to induce persistent summarization failures, such as biased or harmful summaries, while preserving standard evaluation metrics. We present a unified post-hoc defense framework for detecting and remediating fine-tuning-stage poisoning in summarization models across the machine learning supply chain. Our experiments show that in white-box settings, poisoned document-summary pairs exhibit abnormally high training influence, enabling detection via influence-function analysis with semantic consistency checks. In black-box settings, poisoned models display two to three times greater sensitivity to semantics-preserving perturbations, enabling behavioral auditing without training data access. Beyond existing poisoning formulations, we introduce novel attacks targeting factual distortion and representational bias, showing that poisoning alters summarization behavior without triggering conventional alarms. Across nine architectures and six benchmark datasets under adaptive attacks, our defenses achieve 85-92% detection precision, while gradient-ascent unlearning restores up to 96% of original behavior with minimal utility loss (less than 0.6% ROUGE degradation). These results indicate that fine-tuning-time poisoning leaves persistent structural artifacts, enabling practical detection and post-deployment recovery without full retraining.

---
