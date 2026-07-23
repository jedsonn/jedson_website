# Classification batch 124 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-124.answer.json` as a JSON array.

---

## uid: `arxiv:2606.22719v1`

- title: Leakage-Aware Benchmarking of LLM Forecasting: Real-Time Nowcasts as the Decision-Time Input for Macro Factor Ranking
- authors: Mao Guan, Qian Chen
- affiliations: not stated
- posted: 2026-06-21
- source: arXiv
- link: https://arxiv.org/abs/2606.22719v1
- keyword hits: llm, llms, retrieval-augmented

### abstract

Forecasting benchmarks for retrieval-augmented LLMs routinely confound model capability with information leakage: features labeled with a target's timestamp are often not observable at the system's decision time. We study leakage-controlled equity factor ranking with a retrieval-augmented 7B open-source LLM forecaster. At each month-end from 2023-04 to 2026-03, the forecaster observes only decision-time information: lag-shifted FRED macro variables, recent macro-event summaries, and the Cleveland Fed's archived daily CPI nowcast for unreleased current-month inflation. A macro-analog retrieval module selects historical states, a critic LLM compresses them into one tactical rule, and an actor LLM maps the current state and recent rules into scores for seven U.S. equity style factors. The full pipeline obtains a median monthly Spearman rank IC of +0.154, with positive means across three non-overlapping contiguous 12-month subwindows; the mean IC remains statistically underpowered, with a bootstrap 95% confidence interval that includes zero. Non-LLM baselines under the same decision-time constraint demonstrate that a kNN macro-analog model recovers a comparable median IC, indicating that real-time inflation information and macro-similar retrieval explain much of the median signal. The LLM pipeline retains higher mean IC and a stronger long-short allocation sanity check, suggesting that any marginal benefit is concentrated in the extreme rankings that drive long-short portfolio formation. A descriptive audit of the 36 critic rules and per-month case studies appears in the appendix.

---

## uid: `arxiv:2606.24596v1`

- title: To Compare, or Not to Compare: On Methodological Practices in Evaluating Social Bias
- authors: Federico Marcuzzi, Xuefei Ning, Roy Schwartz, Iryna Gurevych
- affiliations: not stated
- posted: 2026-06-23
- source: arXiv
- link: https://arxiv.org/abs/2606.24596v1
- keyword hits: chain-of-thought, large language model, large language models

### abstract

As Large Language Models are increasingly deployed in critical applications, robustly evaluating their social biases is paramount. However, the current literature suffers from widespread methodological fragmentation, which yields contradictory conclusions. This stems largely from ignoring the structural framing of benchmark-level evaluations. To resolve this, we introduce a unified and controllable framework that standardizes heterogeneous benchmarks to systematically contrast isolated demographic assessments with forced-choice comparative settings. Crucially, this allows us to disentangle the confounding effects of Chain-of-Thought reasoning, neutral fallback options, and other structural artifacts in social bias evaluations. Our evaluation across multiple model families reveals a massive, systematic paradigm gap: while isolated assessments limit prejudice activation, comparative settings act as aggressive catalysts for latent discrimination, a shift primarily driven by underspecified contexts. Alarmingly, CoT reasoning exacerbates social biases under comparative settings, and this systemic bias persists as a deterministic prejudice even when models are provided neutral fallback options or claim to answer randomly. Finally, we demonstrate that this comparative prejudice is a generalized phenomenon that scales positively with model size. Ultimately, we offer a crucial methodological guideline: while researchers must leverage comparative settings to robustly audit hidden biases, practitioners cannot safely rely on comparative deployments in ambiguous real-world tasks.

---

## uid: `doi:10.2139/ssrn.6874961`

- title: Token Pagination: A Formal Framework for Context-bounded Inference in Enterprise Large Language Model Systems
- authors: Kameswara Prasad Mukkamala
- affiliations: not stated
- posted: 2026-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6874961
- keyword hits: agentic, large language model, llm

### abstract

This paper introduces the Token Pagination Framework (TPF), a formal protocol for managing context window resources in enterprise Large Language Model (LLM) deployments. Context overflow-the condition in which session token budgets are exhausted before a task completes-is a pervasive, expensive, and undertheorized problem in production AI systems. The problem is structurally compounded by the Model Context Protocol (MCP), which introduces two distinct token inflation vectors into every agentic session: upfront tool schema loading and accumulating tool result payloads. Existing work addresses token budgeting within single model invocations or at prompt construction time, but no prior framework treats the context window as a paginated resource with a persistent cursor, layered admission gates, and a structured overflow signal. TPF borrows the REST API pagination contract and maps it rigorously onto LLM session management. We define six quantitative metrics: Context Pressure Index (CPI), Semantic Density Score (SDS), Recency Decay Weight (RDW), Intent Coverage Ratio (ICR), Output Verbosity Ratio (OVR), and Tool Schema Pressure (TSP). We derive a unified admission predicate, a rolling compression operator, and a cursor state model extended for MCP tool state. The architecture is organized as four layers: Gate, Budget, Compression, and Overflow. TPF maps directly onto the MCP host role defined in the Model Context Protocol specification and is designed to inform protocol-level features in AI provider APIs, MCP host implementations, and orchestration runtimes.

---

## uid: `arxiv:2606.25358v1`

- title: Agentic Knowledge Tracing: A Multi-Agent LLM Architecture for Stealth Assessment of Financial Literacy in Serious Games
- authors: Gabriel Santos, Rita Julia, Marcelo Nascimento
- affiliations: not stated
- posted: 2026-06-24
- source: arXiv
- link: https://arxiv.org/abs/2606.25358v1
- keyword hits: agentic, large language model, llm

### abstract

Assessing financial literacy during gameplay without disrupting the learning experience remains a key challenge in serious games for education. We present the Agentic BKT pipeline, a multi-agent large language model architecture for stealth assessment of financial competencies from open-ended gameplay events. The pipeline processes events from a 2D platformer serious game aligned with the OECD/INFE financial literacy framework through four phases: (1) the game captures every player decision as a structured event log; (2) an LLM event classifier labels each action on a four-point rubric validated against three domain experts (Fleiss kappa = 0.624, substantial agreement); (3) four domain-specific agents specializing in risk mitigation, investing, spending, and credit management perform session-level reasoning over behavioral trajectories, feeding per-competency Bayesian Knowledge Tracing that estimates mastery within each domain; and (4) an expert judge agent synthesizes the domain-level estimates into an overall mastery score. Evaluated with 193 K-12 participants across 264 game sessions, the Agentic BKT pipeline yields mastery estimates significantly correlated with learning gain (r = 0.276, p = 0.0001) and post-test scores (r = 0.333, p < 0.0001) while showing no correlation with pre-test scores, providing both convergent and discriminant validity. The multi-agent approach approximately triples the predictive validity of a single-LLM baseline (r = 0.095, not significant) in this study, demonstrating that domain decomposition and session-level reasoning play a central role in capturing the multidimensional nature of financial literacy from gameplay

---

## uid: `doi:10.2139/ssrn.6993288`

- title: Contract-Seek: A Locally Deployable Large Language Model System for Construction Contract Risk Identification
- authors: Chenglong Xu, Yu Wang, Yuting Chen, Mingyu Zhang, Yihong Gan, Yongqiang Chen
- affiliations: not stated
- posted: 2026-06-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6993288
- keyword hits: deepseek, gpt-4, large language model, retrieval-augmented

### abstract

Contract risk is a major source of uncertainty in construction projects. Contract risks are still identified primarily through manual review by experts, often under tight time constraints. This process is laborious and prone to error. To automate the analysis of large volumes of contract documents, this study presents Contract-Seek, a locally deployable decision support system that combines instruction tuning for the contract domain with retrieval-augmented generation (RAG). Five experts developed a risk register containing 327 items, and 8,112 instruction instances were constructed from risk annotations, coding of three contract functions, and question answering data derived from contract clauses. Contract-Seek was evaluated on 148 questions through blinded scoring by three contract experts and compared with GPT-4o, DeepSeek-R1-671B, and QwQ-32B. It achieved average scores of 9.39 for contract clause alignment, 8.44 for risk identification precision, and 8.96 for linguistic proficiency. In the controlled ablation, adding RAG to QwQ-32B improved clause alignment and risk identification precision by 5.01 and 4.17 points, respectively. Adding instruction tuning increased linguistic proficiency by a further 2.21 points and also improved the other two dimensions. A separate evaluation using 48 clauses from actual contracts supported its performance in project-specific review. By combining reasoning adapted to the contract domain with controlled access to local knowledge, Contract-Seek provides a reproducible approach for privacy-conscious AI deployment in knowledge-intensive industrial workflows.

---

## uid: `arxiv:2606.27027v1`

- title: ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP
- authors: Liwei Liu, Tianzhu Han, Zijian Liu, Zishu Dong, Na Ruan
- affiliations: not stated
- posted: 2026-06-25
- source: arXiv
- link: https://arxiv.org/abs/2606.27027v1
- keyword hits: llm, llms, text embedding

### abstract

With the rapid evolution of LLM-driven agents, Model Context Protocol (MCP), an open protocol bridging LLMs with external tools, has quickly become foundational to modern agent ecosystems. However, the expanding adoption of MCP has also introduced novel security concerns such as Tool Poisoning Attack (TPA), which exploit LLM-server interactions to inject malicious prompts. Existing poisoning schemes typically adopt a monolithic plaintext embedding paradigm, which fails to withstand manual inspection or automated detectors. Current research still lacks a systematic analysis on multi-tool poisoning, where multiple tools can be exploited cooperatively to disperse detection risk. In this paper, we introduce ShareLock, a multi-tool threshold poisoning framework that utilizes Shamir's threshold scheme to ensure exceptional stealth and fault tolerance. ShareLock distributes the malicious instruction as benign-looking secret shares across multiple tool descriptions, achieving both information-theoretic secrecy and attack robustness against moderate auditing. After a covert reconstruction trigger is planted during server update, the aggregated shares reconstruct the hidden instruction, resulting in critical breaches of system assets or private data. To evaluate the realistic threat of ShareLock, we constructed a comprehensive benchmark encompassing four multi-tool scenarios and conducted extensive experiments across mainstream LLMs on two distinct MCP clients. Our results demonstrate that ShareLock significantly outperforms existing single-tool poisoning strategies in tool description-based detection while maintaining an average attack success rate exceeding 90%.

---

## uid: `arxiv:2606.28601v1`

- title: Database Context Compression for Text-to-SQL on Real-World Large Databases
- authors: Jingwen Liu, Weibin Liao, Xin Gao, Junfeng Zhao, Yasha Wang
- affiliations: not stated
- posted: 2026-06-26
- source: arXiv
- link: https://arxiv.org/abs/2606.28601v1
- keyword hits: claude, deepseek, prompting

### abstract

Recent progress in Text-to-SQL has been driven by stronger language models and prompting strategies, yet performance on real enterprise benchmarks such as Spider 2.0 and BIRD remains far below that on classical academic datasets. We argue that the main bottleneck is no longer reasoning, but database representation. Real databases contain repeated audit columns, large groups of similar tables, opaque identifiers whose meanings are stored only in documentation, and extensive data dictionaries with little query-relevant information. Existing query-aware methods, including schema linking and retrieval-based schema selection, filter this raw context but still operate on redundant and verbose representations. We reformulate the problem as database context compression, a query-agnostic transformation that rewrites schemas, semantic descriptions, and external documentation into a compact representation. We formalize this transformation with the SGCF (Support-Gain Component Factorization) principle, which unifies repeated column extraction, isomorphic table templating, semantic componentization, and evidence purification under a single coverage objective. Based on SGCF, we propose DBCC, a database-side middleware that performs offline structural and semantic compression together with lightweight online evidence purification. DBCC is model-agnostic and can be integrated into existing Text-to-SQL pipelines. On Spider 2.0-Snow and BIRD, DBCC reduces input context by up to two orders of magnitude (from 2.6M to 34.7K tokens on the largest Spider 2.0-Snow subset), improves schema-linking strict recall from 0% to 56.5% under DeepSeek-V3.2 (63.1% under Claude Opus 4.7), and consistently increases end-to-end execution accuracy by 1.8-1.9% over three recent Text-to-SQL systems. Our code is open-sourced at https://github.com/MrBlankness/SchemaCompression.

---

## uid: `arxiv:2606.30583v2`

- title: AI Premium
- authors: Nicola Borri, Yukun Liu, Aleh Tsyvinski
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.30583v2
- keyword hits: agentic, large language model, large language models

### abstract

Using 380 trillion tokens of realized AI consumption across more than four hundred large language models from the licensed proprietary OpenRouter dataset covering approximately 2 percent of current global monthly AI token consumption, we analyze how AI affects firms, markets, and workers. Leveraging the unprecedented size, scope and granularity data, we construct the AI Factor from growth in tokens, dollars, and users, estimate firm-level AI Betas from stock return comovement, and characterize the \emph{AI Premium}. First, we build a high-frequency AI factor and decompose it into salient components. Second, we show that firms whose returns covary more positively with the AI factor -- high AI beta firms -- earn higher subsequent returns, and the AI premium is large and heterogeneous. A value-weighted long-short strategy earns 64.1 basis points per week, and the premium is large for loadings on the intensive, frontier-oriented margin of AI consumption -- closed-source models, paying and seasoned users, and long prompts -- but not on casual or open-weight use. Third, the premium reaches beyond technology firms into consumer-facing and capital-heavy parts of the economy, but is absent in emerging markets, including China. Fourth, the AI exposure is more positive in nonroutine interactive work and more negative in analytical, scientific, and operations-control skills -- an occupation one standard deviation higher in interaction-and-communication content has 0.36-standard-deviation higher market-implied AI exposure. Additionally, we provide early evidence of the rise of the agentic economy.

---
