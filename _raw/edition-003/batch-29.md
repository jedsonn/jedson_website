# Classification batch 29 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-29.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6878405`

- title: Small Language Graph: A Local AI Framework for Secure and Scalable Engineering Knowledge Access in Industry
- authors: Bogdan Bogachov, Qingqing Mao, Yaoyao Fiona Zhao
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6878405
- keyword hits: gpt-4, large language model, large language models, llama, retrieval-augmented

### abstract

Despite recent advances in large language models, small and medium engineering firms face persistent barriers in applying them to proprietary documentation. Cloud APIs raise confidentiality concerns, while large local models require costly GPU infrastructure and small models often lack sufficient domain performance. This work introduces the Small Language Graph (SLG), a lightweight adaptation framework for local deployment on consumer hardware. SLG uses small language models (Llama-3.2-1B-Instruct) as expert nodes in a graph-based architecture, where each node is fine-tuned on an isolated subsection chunk from engineering manuals and an orchestrator routes each query to the most relevant expert. Experiments on three aviation maintenance documents show that at full dataset scale, SLG outperforms all evaluated baselines --- GPT-4.1, retrieval-augmented generation, fine-tuned Llama-3.2-1B-Instruct, and fine-tuned Llama-3.1-8B-Instruct --- on four of five evaluation metrics. At smaller data volumes the fine-tuned Llama-3.1-8B-Instruct leads, but its performance degrades substantially as the corpus grows, whereas SLG maintains stable accuracy. Critically, unlike GPT-4.1 and RAG, SLG processes all data locally, avoiding the confidentiality risks and recurring costs of external cloud APIs. In addition, SLG trains 2.9 times faster than the 8B baseline and runs with under 7~GB VRAM and under 10 seconds of inference time. These results support SLG as a practical approach for secure, local question answering over hierarchically structured engineering documents under hardware constraints.

---

## uid: `doi:10.2139/ssrn.6816879`

- title: Prompt Injection Attacks: Theory, Techniques, Defense, and Secure AI Systems
- authors: Ketan Sarvakar
- affiliations: not stated
- posted: 2026-06-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6816879
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

The rapid adoption of Large Language Models (LLMs) has transformed human-computer interaction, enabling intelligent assistants, autonomous agents, and retrieval-augmented systems across industries. However, these systems introduce a new class of security vulnerabilities known as prompt injection attacks. Unlike traditional software exploits that target code execution or memory corruption, prompt injection manipulates natural language instructions to alter an AI system's intended behavior. These attacks can bypass safeguards, leak confidential information, manipulate outputs, misuse integrated tools, and compromise decision-making systems. This paper examines the theory and mechanisms of prompt injection attacks, categorizes major attack techniques, explores real-world scenarios, reviews recent literature, and evaluates defensive approaches for building secure AI systems. The study argues that prompt security must be treated as a foundational component of AI cybersecurity and governance.

---

## uid: `doi:10.2139/ssrn.6816538`

- title: From Semantic Layers to AI-Native Data Interfaces: Evolution, Challenges, and Governance
- authors: Venkata Manikanta Sangaraju
- affiliations: not stated
- posted: 2026-06-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6816538
- keyword hits: ai agent, large language model, large language models, llm, llms

### abstract

For many years, semantic layers have been a central part of business intelligence and analytical systems. They simplify complex database schemas, maintain consistent business metrics, improve governance, and make analytics more accessible to non-technical users.With the rapid adoption of AI-augmented analytics and large language models (LLMs), the role of semantic layers is changing significantly. Semantic layers now support not only human analysts but also AI agents and semi-automated analytics systems. This shift has exposed weaknesses in current semantic-layer implementations, particularly in schema interpretation, metric reliability, governance, and the accuracy of AI-generated analytics.This paper examines the evolution of semantic layers in modern analytics environments. This study builds upon an extensive review of more than 150 academic papers, industry reports, technical documentation, and vendor architectures published between 1990 and 2025. Drawing from databases such as Scopus, DBLP, and Google Scholar, and using search terms including "semantic layer," "metrics layer," "OLAP," and "text-to-SQL," we examined a wide range of semantic layer implementations spanning four generations of design. Based on this synthesis, we propose a taxonomy that categorizes these approaches into cube-based systems, metrics-oriented platforms, headless semantic layers, and emerging AI-first knowledge graph-driven systems.The paper also identifies several issues that arise when LLMs interact directly with raw data and database tables. Common problems include schema ambiguity, uncontrolled exploratory queries, hallucinated joins, inconsistent metric interpretation, and exposure of sensitive enterprise data.Building on these findings, the paper outlines a set of design principles for AI-first analytical systems. In these environments, semantic layers function less as simple abstraction mechanisms and more as governed control planes between AI systems and enterprise data infrastructure. The findings suggest that semantic layers are becoming increasingly important for governance, security, reliability, and controlled access to enterprise data.

---

## uid: `arxiv:2606.08285v1`

- title: Beyond Agent Architecture: Execution Assumptions and Reproducibility in LLM-Based Trading Systems
- authors: Junyi Yao, Zihao Zheng
- affiliations: not stated
- posted: 2026-06-06
- source: arXiv
- link: https://arxiv.org/abs/2606.08285v1
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) and agentic systems are increasingly proposed for financial trading, yet their reported performance remains difficult to compare because studies vary in data provenance, temporal split discipline, execution timing, turnover treatment, and transaction-cost modeling. This article presents a targeted topical review and reproducibility audit of execution realism in LLM-based trading research. A coded evidence matrix covering 30 trade-relevant primary studies is used to assess point-in-time controls, split transparency, held-out evaluation, cost and turnover treatment, execution semantics, universe definition, and artifact release. Across the audited sample, architecture reporting is generally clearer than the evaluation assumptions needed to judge whether a trading result is economically interpretable or reproducible. A 10-equity worked example is included only as a methodological scaffold to illustrate how explicit friction and timing choices can materially compress active-strategy results. The main conclusion is that the next useful step for LLM trading research is not only better agent design, but also clearer reporting standards for execution realism, reproducibility, and evaluation comparability.

---

## uid: `doi:10.2139/ssrn.6877678`

- title: Query Carefully Revisited: Detecting Unanswerable Queries in Text-to-SQL Across Datasets and Models in Biomedicine
- authors: Jasmin Saxer, Luise Linzmeier, Jonathan Fürst, Andreas Weiler, Kurt Stockinger
- affiliations: not stated
- posted: 2026-06-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6877678
- keyword hits: large language model, large language models, llama, prompting, qwen

### abstract

Text-to-SQL systems allow users to query databases using natural language. However, users often ask questions that are ambiguous, incomplete, or cannot be answered with the given database. In such cases, models may still generate SQL queries, which can lead to incorrect or misleading results. In this work, we focus on detecting unanswerable queries in text-to-SQL systems.We evaluate our approach on two datasets and databases, ScienceBenchmark (OncoMX) and SM3-Text-to-Query, and extend SM3 with a new dataset of 400 unanswerable questions across eight categories. We compare four large language models under different prompting strategies, including zero-shot and few-shot settings with answerable questions (AQ) and non-answerable questions (NAQ), as well as a Do-Not-Answer (DNA) rule.The results show that few-shot prompting improves performance for AQs, while adding NAQs and the DNA rule does not reduce overall performance. For AQs, Qwen3.5-27B performs best across both datasets, while Llama-3.3-70B-Instruct achieves the best results for detecting NAQs. Overall, Llama-3.3-70B-Instruct provides the best balance between AQs and detecting NAQs. We also show that the SQL correction loop for handling SQL syntax errors has limited impact, with most improvements happening within one or two iterations and almost no effect on detecting NAQs. In summary, the results show that detecting NAQs can be integrated into text-to-SQL systems without reducing performance. This is important for building reliable text-to-SQL systems with real-world applications - especially in biomedical settings.

---

## uid: `doi:10.2139/ssrn.6902294`

- title: Prompt-Based Attacks and Defenses in Large Language Models: A Systematic Review of Threat Models, Taxonomies, and Evaluation Practices
- authors: Victória Guimarães, Débora Medeiros, Leandro Reis, Hugo Mesquita, Thiago Rocha
- affiliations: not stated
- posted: 2026-06-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6902294
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Large Language Models (LLMs) are increasingly integrated into applications that combine user prompts, retrieved documents, external files, tool outputs, and agentic workflows. This integration expands the attack surface of LLM-based systems and enables prompt-based attacks that operate not only through direct user input, but also through contextual information incorporated during inference. This paper presents a systematic literature review of prompt-based attacks and defenses in LLMs, covering 89 primary studies published between 2023 and February 2026. The review follows Kitchenham's guidelines and uses PRISMA to structure the selection process. We introduce a unified threat model, represented as y = F(x,c), where x denotes the direct user prompt and c denotes external context assembled by the system during inference. Based on this model, we propose a taxonomy of attacks organized around two axes: attack surface and attack technique. Among the 89 selected studies, 40 focus exclusively on attacks, 24 focus exclusively on defenses, and 25 address both attacks and defenses. This yields an attack pool of 65 studies and a defense pool of 49 studies. The findings suggest an emerging shift, especially in recent studies, from direct prompt manipulation toward context-mediated attacks, including Indirect Prompt Injection, Tool/Agent Hijacking, and Retrieval-based Injection/RAG Poisoning. We organize mitigation strategies according to their pipeline stage: Pre-Model, Intra-Prompt, and Post-Model. Finally, we integrate both taxonomies to examine whether defenses are positioned at stages where adversarial payloads are visible and actionable. The analysis shows stronger defensive coverage for attacks targeting the direct prompt surface, while context-mediated, hybrid, and agentic attacks remain only partially covered. These findings highlight the need for context-aware, multi-stage, and action-level defenses for modern RAG and agent-based LLM systems.

---

## uid: `doi:10.2139/ssrn.6914470`

- title: AI-Powered Radiology Report Simplification in Arabic: A Prospective Evaluation of Patient Comprehension and Clinical Safety
- authors: Mohammad Alsayed, Mohammed  Moeenaldeen Alsayed, Akram Maghrabi, Ali Alzahrani, Abdulbari Felemban, Sara Badirah, Faisal Alabdulkarim, Hana Sheitt
- affiliations: not stated
- posted: 2026-06-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6914470
- keyword hits: large language model, large language models, llm, llms, prompt engineering, qwen

### abstract

AbstractBackgroundRadiology reports are written for clinicians, leaving the majority of patients unable to understand their own imaging findings. Large language models (LLMs) offer a means to simplify reports for patient-facing use; however, most implementations rely on cloud-based platforms that raise data privacy and regulatory concerns. Arabic-speaking populations—over 400 million people worldwide—remain substantially underserved in medical AI research, with no prospectively validated AI Arabic radiology report simplification system previously reported. ObjectiveThis study aimed to evaluate patient comprehension and radiologist-assessed clinical safety of an on-site, institutionally governed AI system that generates simplified radiology reports in plain English and Arabic for Arabic-speaking outpatients. MethodsIn this prospective single-center observational study conducted at King Faisal Specialist Hospital and Research Centre – Jeddah (KFSHRC-J) in January 2026, 98 adult outpatients (mean age 50.0 ± 14.9 years; 50 men, 48 women; IRB #2251488) reviewed three versions of their own radiology report in randomized order: a traditional radiologist report, an AI-simplified English report, and an AI-simplified Arabic report. The system used a two-stage pipeline: Qwen3-14B-FP8 with structured prompt engineering for English simplification (Stage 1), and a fine-tuned Hala-1.2B model for Arabic translation (Stage 2; 8,319 training samples). Patient comprehension was measured on a 5-point Likert scale (1=Very Easy; 5=Very Difficult). Three board-certified radiologists independently assessed clinical safety using a standardized seven-domain rubric; inter-rater agreement was quantified using ICC(2,k). ResultsAI-simplified Arabic reports produced a median comprehension score of 1 (IQR 1–2) versus 5 (IQR 3–5) for traditional reports (p

---

## uid: `arxiv:2606.17383v1`

- title: Model Validation of Agentic AI Systems: A POMDP-Based Framework for Belief-State, Forecast, and Policy Validation
- authors: Matthew Francis Dixon
- affiliations: not stated
- posted: 2026-06-16
- source: arXiv
- link: https://arxiv.org/abs/2606.17383v1
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Agentic artificial intelligence systems introduce a new class of model risk. Unlike traditional predictive models, autonomous agents continuously acquire information, form beliefs regarding latent states of the environment, generate forecasts, select actions, and adapt their behavior over time. Existing validation methodologies focus primarily on predictive accuracy and therefore provide limited insight into the quality of the underlying decision process. This paper proposes a model validation framework for agentic AI based on Partially Observable Markov Decision Processes (POMDPs). The framework decomposes autonomous decision making into information, beliefs, forecasts, actions, and utility, allowing each component to be validated independently. Large language models (LLMs) are formalized as approximate Bayesian filtering operators, and a model-risk taxonomy is developed encompassing state-space, filtering, forecast, policy, utility-specification, and parameter risks. The model risk validation methodology is demonstrated through a portfolio-management case study in which an agent infers latent market regimes from market and macroeconomic information, generates belief-conditioned forecasts, and constructs portfolios using a Black--Litterman framework. Empirical validation combines performance analysis, belief calibration diagnostics, coverage tests, ablation studies, and parameter-sensitivity analysis. The results indicate that latent-state inference contributes independently to decision quality and that the principal conclusions remain robust across a broad range of parameter values. The principal contribution of the paper is a practical framework for extending established model risk management concepts to autonomous AI systems and providing a rigorous foundation for their validation, governance, and monitoring.

---
