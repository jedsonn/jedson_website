# Classification batch 54 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-54.answer.json` as a JSON array.

---

## uid: `arxiv:2606.28061v1`

- title: ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents
- authors: Shijing Hu, Liang Liu, Zhu Meng, Zhicheng Zhao
- affiliations: not stated
- posted: 2026-06-26
- source: arXiv
- link: https://arxiv.org/abs/2606.28061v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) have increasingly moved from standalone text generation systems to agents that invoke external tools, access environments, and execute multi-step tasks. However, conventional function-calling benchmarks mainly evaluate task completion and API correctness, while privacy evaluation benchmarks typically focus on final responses or privacy judgments. Neither perspective captures purpose-bound information flow across an executed multi-tool trajectory. Motivated by this limitation in current agent evaluation, ToolPrivacyBench audits whether task-private atoms are routed only to authorized tools and downstream sinks, thereby evaluating both task completion and privacy over-disclosure during tool use. The benchmark contains 2,150 cases, including 1,150 fully synthetic privacy-sensitive business workflows and 1,000 cases adapted from existing multi-tool and function-calling benchmarks. Each case is represented by a policy knowledge base. After an agent executes against mock business backends, the evaluator compares recorded tool arguments and backend audit logs with this policy knowledge base. The evaluation covers nine widely used agents to characterize purpose-bound privacy over-disclosure. The results show that successful tool execution does not imply appropriate privacy disclosure: an agent may complete a task while transmitting unnecessary private information through intermediate tool calls. ToolPrivacyBench therefore formalizes a need-to-know disclosure boundary, under which each tool should receive only the information necessary for its stated purpose, and uses trajectory-level auditing to identify privacy over-disclosure in multi-tool workflows.

---

## uid: `doi:10.2139/ssrn.7006267`

- title: From Perceptions to Predictions: A Mixed-Method Study of Supplier-Related Reputational Risks and Large Language Model Performance
- authors: Laleh Davoodi, Abul  Khair Jyote, Elviira Saarelma, Aki Jääskeläinen, Jozsef Mezei, Filip Ginter
- affiliations: not stated
- posted: 2026-06-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7006267
- keyword hits: large language model, large language models, llm, llms

### abstract

Supplier-relatedreputational risk is an underexplored but increasingly important dimension of supply chain risk management (SCRM). While prior research has primarily focused on operational disruptions, less attention has been paid to how reputational risks emerge across supply chains and how they can be identified proactively. This study examines why supply chain professionals consider reputational risks critical for decision-making and investigates whether contemporary large language models (LLMs) can support their early identification from external news sources. A mixed-method approach was employed, combining interviews with 30 supply chain professionals to capture managerial perspectives on reputational risk and Artificial Intelligence (AI) support, and a comparative case study evaluating three LLMs on reputational risk identification from real-world news articles. The findings show that managers view reputational risk as strategically significant and closely linked to supplier selection and operational continuity. They perceive the greatest potential for AI in early risk identification through continuous monitoring of unstructured external data. The LLM evaluation demonstrates that current models can identify many reputational risk signals from news sources, although performance varies across models and domains, and human validation remains necessary. The results suggest that LLMs can function as early-warning tools that enhance visibility into supplier-related reputational risks, reduce manual monitoring effort, and support more proactive supply chain risk management. This study contributes to the literature by integrating managerial insights with a comparative evaluation of LLMs for supplier-related reputational risk detection, providing both conceptual grounding and practical guidance for AI-enabled supply chain risk management.

---

## uid: `doi:10.2139/ssrn.7009806`

- title: LLM-H²S: A Large Language Model-Guided Hierarchical Heuristic Solver for Multi-Constraint Nurse Scheduling with Real-Time Adaptive Rescheduling
- authors: Rapeepan Pitakaso, Thanatkij Srichok, Surajet Khonjun, Krisanarach Nitisiri, Peerawat Luesak, Sarayut Gonwirat, Natthapong Nanthasamroeng, Chakat Chueadee
- affiliations: not stated
- posted: 2026-06-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7009806
- keyword hits: large language model, large language models, llm, llms

### abstract

Nurse scheduling in public hospitals is a multi-constraint combinatorial optimisation problem involving regulatory hard constraints, soft preferences, and real-time operational disruptions. Despite extensive research, existing methods-including integer programming, metaheuristics, and constraint programming-cannot process constraints expressed in natural language, produce no decision explanations, and lack real-time adaptive rescheduling capability. This study proposes LLM-H²S (LLM-Guided Hierarchical Heuristic Solver), a novel three-phase framework that positions large language models as self-contained intelligent heuristic solvers for multi-constraint nurse scheduling. LLM-H²S introduces three original contributions: Constraint Priority Tokenisation (CPT), which encodes a formally grounded 14-hard-constraint, 8-soft-constraint MILP system into a priority-ordered prompt structure; Violation-Gradient Feedback (VGF), an adaptive repair mechanism guiding iterative LLM self-repair toward feasibility; and Disruption-Aware Partial Rescheduling (DAPR), a formally grounded real-time recovery protocol achieving sub-60-second schedule restoration under operational disruptions. The framework is evaluated through a multi-site case study across three synthetic hospital instances modelled on the Ubon Ratchathani provincial healthcare network, Thailand, and compared against seven recently published baseline methods. LLM-H²S achieved a mean hard constraint satisfaction rate of 99.3%, resolved 94.9% of real-time disruption events within 37.6 seconds, reduced night shift inequality by 64% over the weakest baseline, and attained the highest head nurse trust score of 4.6 out of 5.0. These results establish that LLMs, when equipped with formal constraint encoding and adaptive repair mechanisms, constitute viable, explainable, and scalable solvers for real-world nurse scheduling, offering a practical pathway for automated workforce management in resource-constrained Southeast Asian public healthcare systems.

---

## uid: `arxiv:2606.28978v1`

- title: Can LLMs Hire Fairly? Racial Bias in Resume Screening
- authors: Zhenyu Gao, Wenxi Jiang, Yutong Yan
- affiliations: not stated
- posted: 2026-06-27
- source: arXiv
- link: https://arxiv.org/abs/2606.28978v1
- keyword hits: large language model, large language models, llm, llms

### abstract

We audit fourteen mainstream large language models (LLMs) for hiring discrimination using the paired-resume methodology of Kline, Rose, and Walters (2022). The sole 2023-vintage model reproduces the pro-White callback gap documented in field experiments on labor market discrimination ($+2.12$ pp, significant at the 1\% level). Every model released in 2024 or after shows either a null gap or a significant pro-Black reversal (up to $-3.01$ pp). The same pattern holds on the gender axis. Based on 24,024 paired postings per model across 14 models, our results document a reversal in the direction of algorithmic hiring bias across model generations.

---

## uid: `arxiv:2606.29437v1`

- title: LLMography: Transforming Human-AI Conversations into Traceability, Oversight, and Auditability Indicators
- authors: Mohammed Bousmah
- affiliations: not stated
- posted: 2026-06-28
- source: arXiv
- link: https://arxiv.org/abs/2606.29437v1
- keyword hits: large language model, large language models, llm, llms

### abstract

The growing use of Large Language Models (LLMs) in education, software engineering, academic writing, and technical documentation raises a key question: how can we evaluate not only AI-assisted outputs, but also the interaction process that produced them? Current debates often focus on detecting whether a final artifact was generated by AI, while overlooking the conversation history that reveals human direction, AI contribution, corrections, validation, and traceability. This paper introduces LLMography, a framework for transforming Human-AI conversations into measurable indicators of provenance, human contribution, AI dependency, reproducibility, and auditability. By analogy with bibliography and webography, LLMography documents the dynamic trajectory of interaction between a human and a Large Language Model as a structured trace of Human-AI co-production. We present a prototype that analyzes Human-AI conversation traces and generates KPI reports including Prompt Quality Score, Human Direction Score, AI Dependency Level, Auditability Score, Final Output Traceability, Privacy Risk Level, and a recommended LLMography label. A preliminary exploratory evaluation was conducted on 19 anonymized audit reports from engineering students. Most interactions were classified as Human-AI co-produced, with average scores of 86.8/100 for Human Direction, 81.9/100 for Prompt Quality, 72.8/100 for Auditability, and 77.1/100 for Final Output Traceability. The paper also applies LLMography to its own writing process, classified as human-originated, human-directed, AI-assisted co-production. The findings suggest that AI transparency should move beyond output detection toward documenting the history of interaction.

---

## uid: `doi:10.2139/ssrn.7022812`

- title: LLMs in natural language analysis: Inferring political orientation from political speeches and CVs
- authors: Merlin Monzel, Peer Schütt, Martin Reuter
- affiliations: not stated
- posted: 2026-06-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7022812
- keyword hits: large language model, large language models, llama, llm, llms

### abstract

Political orientation is reflected in natural language use, yet traditional automated text analysis methods often yield small effect sizes due to their reliance on context-independent word counts or narrowly trained classifiers. Large language models (LLMs) may overcome these limitations by leveraging contextualized representations and emergent abilities. This research examines whether an LLM can infer political orientation from qualitative text data without task-specific training. Across two preregistered studies, we evaluated Meta Llama 3.3 70B Instruct’s ability to assess political party affiliation and left–right orientation from German parliamentary speeches (Study 1) and voters’ CVs (Study 2). In Study 1, the model analysed 21,559 Bundestag speeches from 1,347 speakers representing six German parties across three legislative periods. Party affiliation was predicted with high accuracy (62.7 %), clearly exceeding the chance level (16.7 %), and accuracy increased as a function of speech length. Misclassifications occurred mainly between ideologically adjacent parties, and model-estimated left-right positions closely mirrored established party orderings. Retest reliability was excellent (ICCs ≥ .95). Study 2 extended the approach to 131 voters’ CVs and yielded lower but above-chance accuracy (34.4%), alongside high reliability (ICCs ≥ .95) and meaningful associations between model-assessed and self-reported political orientation. Exploratory analyses showed that text sources with potentially lower densities of political information did not support above-chance inference. Overall, the findings indicate that LLMs can detect political linguistic patterns across heterogeneous text types, with performance being strongly dependent on the informational density of the source material, enabling new methodological opportunities for future research.

---

## uid: `arxiv:2606.30383v1`

- title: Whose Side Is Your Agent On? Multi-Party Principal Loyalty in LLM Agents
- authors: Bojie Li, Noah Shi
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.30383v1
- keyword hits: claude, llama, llm, qwen

### abstract

A rapidly growing class of LLM agents is multi-party: the agent acts for a principal (who briefs it, sends follow-ups, and receives results) while also conversing in a separate channel with a counterparty whose interests may diverge (negotiating with a vendor, screening inbound requests, or mediating between employees). Here "help whoever you are talking to" is the wrong objective. The agent must stay loyal to the principal it represents without over-refusing the principal's own cooperative asks. We study this multi-party loyalty problem and contribute a measurement instrument, two mechanisms, and a structural lesson. PrincipalBench is a 75-item multi-turn benchmark with leak probes, dual judges, and an integrity-audit gate. Across 13 frontier subjects it exposes a sharp split (<=20% vs. 53.6-75.3% harm) invisible to single-turn safety evaluations: a selective cluster that declines adversarial probes while still following the principal's legitimate requests, and an over-refusing cluster that refuses broadly. (M1) A prompt-time loyalty scaffold (a fixed system prompt of seven prioritized rules, open-coded from 50+ failure trajectories) holds Claude-Sonnet to 19.4% harm and all nine selective subjects to <=20%. (M2) A per-token-KL distillation recipe transfers a prompted Qwen3-32B teacher into 8B Qwen3 and Llama-3.1 students, the strongest open-weight recipe we measure. (Lesson) Both mechanisms only move along a common leak/over-refusal trade-off rather than crossing it: improving one axis costs the other, and the jointly favorable outcome stays out of reach.

---

## uid: `doi:10.2139/ssrn.7029046`

- title: Evaluating LLM Capabilities and Performance for Software Design Pattern Identification
- authors: Nikita Lanetsky, Brian Davison
- affiliations: not stated
- posted: 2026-06-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7029046
- keyword hits: large language model, large language models, llm, llms

### abstract

Context: Large language models (LLMs) are becoming deeply integrated into software engineering tasks, including patternrecognition. However, their effectiveness and efficiency on realistic code remains insufficiently evaluated, with existing benchmarks limitedin scale and reliant on simplified examples that do not adequately reflect real-world implementation complexity.Objectives: This study aims to establish a rigorous, large-scale benchmarking framework for evaluating the capability of state-of-the-art LLMs to identify software design patterns in realistic, complexity-varied Python code, and to compare performance across multipleLLM providers.Methods: A three-stage benchmarking framework was developed comprising LLM-driven code generation, structured datasetcuration, and multi-model pattern recognition analysis. A dataset of 1,560 Python code snippets was generated across 13 GoF designpatterns at three complexity levels (low, medium, high) with a self-evaluation quality assurance mechanism applied during generation. Fourstate-of-the-art LLMs from distinct providers (Anthropic, OpenAI, Moonshot, and xAI) independently evaluated all snippets, producing6,240 evaluation records. Performance was assessed using accuracy, precision, recall and F1-score.Results: All four models exceeded 97% accuracy, with a cross-model average of 98.7%. The macro-average F1-score reached 0.988,with individual pattern F1-scores ranging from 0.958 to 1.000. Five patterns achieved perfect classification across all models. Performanceremained near-perfect at medium complexity, with a marginal drop at high complexity (96%-98%). Kimi K2 emerged as the most balancedmodel, combining 98.97% accuracy with the fastest mean analysis time of 10.7 seconds per record.Conclusion: These findings confirm the practical applicability of modern LLMs for reliable design pattern identification withincomplex, realistic Python codebases, with consistent performance across providers. Future work should extend the framework to includehuman-authored code, multi-language datasets, and overlapping pattern combinations to further validate real-world applicability

---
