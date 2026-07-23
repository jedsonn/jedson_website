# Classification batch 342 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-342.answer.json` as a JSON array.

---

## uid: `arxiv:2607.12161v2`

- title: Token Reduction Is Not Cost Reduction
- authors: Sarel Weinberger, Amir Hozez
- affiliations: not stated
- posted: 2026-07-13
- source: arXiv
- link: https://arxiv.org/abs/2607.12161v2
- keyword hits: claude

### abstract

Context-reduction layers for API-based coding agents, including command-output compressors, retrieval rankers, and API-boundary proxies, are commonly evaluated by how much context or tool output they remove. We ask a different question: which interventions actually reduce end-to-end billed cost while preserving task success? Our primary evidence is a pre-specified, hash-frozen, paired campaign of 2,908 provider-billed Claude Code runs, of which 2,848 were analyzed, covering 103 tasks, seven repositories, and three models. The campaign compared a baseline with two generations of hook-based compression and an API-boundary proxy within a broader measured program of roughly 5,500 billed executions. Three findings emerge. First, prompt-cache traffic dominated cost composition, accounting for about 87% of reconstructed four-component cost (about 80% of the actual bill), with an 8.7% dollar-weighted residual not attributable from retained telemetry. Second, local payload reduction was not a reliable predictor of end-to-end billed cost. An arm that removed 38% of estimated raw tool-output tokens incurred 6.8% higher paired cost (95% CI: +2.8% to +11.3%), while per-task reduction showed only a weak association with cost change (Pearson r = 0.15). Third, aggressive compression can remove action-critical evidence: on SWE-bench-derived Go tasks, compression reduced successful patch application from 27/40 to 15/40 by corrupting verbatim edit anchors. We propose evaluating context-reduction systems by success-adjusted billed cost rather than token reduction alone.

---

## uid: `arxiv:2607.12085v1`

- title: Operationalising Multi-Dimensional Evaluation for Conversational Agents: A Scalable, Governed Pipeline with Selective Re-evaluation and Model Benchmarking
- authors: Niranjan Kumar M, Balaji Nagarajan, Karthik Nair, Faysal Satter, Nithin Surendran
- affiliations: not stated
- posted: 2026-07-13
- source: arXiv
- link: https://arxiv.org/abs/2607.12085v1
- keyword hits: llm

### abstract

Evaluating retail conversational agents requires methods beyond lexical-overlap metrics to assess intent alignment, factuality, helpfulness, clarity, tone, and overall response quality. Although LLM-as-a-judge methods provide scalable alternatives to human evaluation, production deployment introduces challenges in governance, reproducibility, cost, schema consistency, traceability, and reliability. We present GenAI Evaluation, a governed, configuration-driven pipeline for large-scale evaluation of retail conversational systems. It processes production chatbot logs through normalization, sharding, asynchronous execution, and schema-constrained LLM scoring. The framework evaluates helpfulness, truthfulness, clarity, tone alignment, and translation-specific dimensions. Selective re-evaluation processes only incomplete, malformed, or schema-invalid records, while schema locking, versioned configurations, validation logs, and record-level provenance support auditability. The framework processes approximately 50,000 records daily and has evaluated more than two million interactions. Validation used 12,980 stratified-random human-labeled records from four trained annotators. Classification covered 14 intents, 156 sub-intents, 18 major domains, and 129 sub-domains. The pipeline achieved a macro F1 score of 0.93 and 89% human-acceptability accuracy for translation.

---

## uid: `arxiv:2607.11346v2`

- title: Compile, Then Page: Executable SOP Programs and a Capability-Gated Runtime for Procedural LLM Agents
- authors: Chenglin Yu, Li Yin, Ying Yu, Qingxin Fan, RunyangRay Zhong, Hongxia Yang, Ming Li
- affiliations: not stated
- posted: 2026-07-13
- source: arXiv
- link: https://arxiv.org/abs/2607.11346v2
- keyword hits: llm

### abstract

Enterprise agents must follow long-horizon, conditional, safety-critical standard operating procedures (SOPs). We compile machine-readable SOP constraints into executable pseudo-code and run them with a program-guided (PG) stack machine that pages the active frame while an LLM performs semantic execution. A three-arm SOPBench study across six models separates representation from runtime: compiled text never significantly hurts and gains up to 16.0 points where official prose underperforms. Runtime guidance is capability-gated. Two strong models independently show positive seven-domain PG contrasts (58:19 and 75:31 discordant pairs), whereas weak models are harmed. A full-program cursor ablation (active frame first, complete program retained) recovers much of the strong-model refusal gain; selective visibility adds a smaller improvement. Paired probe and audit measurements track this divide to spontaneous state discipline rather than reconstruction ability. On Bank the three primary arms rise from 70.4 to 86.4 to 92.8, with 100% refusal correctness. Practical guidance: compile first; enable active-frame paging only after a model-level discipline check.

---

## uid: `arxiv:2607.11276v1`

- title: Automated Textbook Auditing with Multi-Agent LLM Systems
- authors: Ciprian Cristescu, Adrian-Marius Dumitran, Angela-Liliana Dumitran, Gabriel Stefan
- affiliations: not stated
- posted: 2026-07-13
- source: arXiv
- link: https://arxiv.org/abs/2607.11276v1
- keyword hits: llm

### abstract

Ensuring the quality of educational materials requires more than standard proofreading: textbooks must be audited for factual accuracy, domain-specific technical correctness, and linguistic quality simultaneously -- a task that general-purpose grammar checkers cannot address. We present \textbf{AI Textbook Auditor}, a modular multi-agent pipeline for automated quality assurance of educational materials across subject domains. The system accepts a textbook PDF and produces a structured, human-reviewable report via two analysis tracks: a \textbf{Factual and Technical Track} in which an ensemble of specialized LLM agents detects factual inaccuracies, code errors, incorrect definitions, and conceptual inconsistencies, augmented with web search for humanities domains; and a \textbf{Grammar Track} operating PDF-natively to preserve diacritical encoding. A \textbf{Judge Agent} filters false positives using domain-specific rules before presenting findings to a human reviewer. The pipeline supports two ingestion modes -- vision-native page rendering and PyMuPDF text extraction -- and is domain-adaptable via custom prompts encoding subject-specific error taxonomies. We demonstrate the system on two Romanian upper-secondary textbooks: a CS textbook (56 technical findings across seven categories, with an expert-validated precision of 62.5\%) and a history and social sciences textbook (72 findings spanning factual errors, ideological bias, and grammar). The system is designed as a triage tool that reduces the manual effort of locating candidate issues, with human expert validation required before any editorial action.

---

## uid: `arxiv:2607.11149v2`

- title: The Hidden Footprint: Making Storage a First-Class Metric for LLM Agent Evaluation
- authors: Chenglin Yu, Hongquan Gui, Ying Yu, Hongxia Yang, Tao Zeng, Ming Li
- affiliations: not stated
- posted: 2026-07-13
- source: arXiv
- link: https://arxiv.org/abs/2607.11149v2
- keyword hits: llm

### abstract

LLM agent benchmarks measure task completion, reliability, and inference cost, but not the persistent data an agent run leaves on disk, including logs, context snapshots, checkpoints, and debug traces. We introduce AgentFootprint, a cross-framework benchmark of post-run agent storage footprint. Its serialization-aware metric suite measures total retention, channel composition, duplication, growth, compressibility, and conversation-history reconstructability. It addresses a measurement trap: naive byte-level measurement understates duplication by an order of magnitude because database paging and JSON escaping obscure repeated content. A fixed-trace control separates agent-generated logical volume from persistence-layer amplification: replaying the same trajectory through seven persisting frameworks yields a 6.7x spread. Under identical models, tools, and tasks, configurations with 100% accuracy differ by 15.7x in retained bytes, although their defaults support different recovery and audit capabilities. Three full-history configurations grow superlinearly on a repeated-observation stress task. Exported trajectories from 108 instance-normalized SWE-bench Verified submissions span three orders of magnitude per instance, with no detectable correlation with resolve rate. A content-addressed store reduces retention by 4.8x-32.7x while preserving every reconstructability score. These results establish persistent storage as a resource metric to report jointly with accuracy and reconstructability.

---

## uid: `arxiv:2607.10972v1`

- title: From Checker to Forecaster: Code-Owned Evaluation of Model-Generated Strategic Routes Under Delayed Ground Truth
- authors: Aleh Manchuliantsau
- affiliations: not stated
- posted: 2026-07-13
- source: arXiv
- link: https://arxiv.org/abs/2607.10972v1
- keyword hits: llm

### abstract

Many evaluations of model outputs rely either on contracts checkable at evaluation time or on feedback that arrives within the operating loop. We study the complementary setting in which ground truth is delayed, censored, or private, so deterministic code cannot check correctness at scoring time and must instead issue a code-owned provisional forecast. RouteCast instantiates this regime for model-generated typed strategic routes: models propose candidate routes and structured factors; point-in-time evidence, reference classes, and deterministic transformations produce a provisional forecast-ranking; later outcomes evaluate the forecast. In a retrospective venture pilot on 21 binary-outcome cases (6 positive, 15 negative), the whole-packet RouteCast score showed preliminary retrospective discrimination (AUC 0.756, 95% CI [0.471,0.980]), while a blind LLM judge reached AUC 0.678 [0.419,0.897] and an identity-exposed LLM judge reached AUC 0.761 [0.515,0.944], consistent with recognition- or outcome-related leakage risk. A preregistered decomposition ablation on the same binary subset found that converting the identical inputs into typed staged routes was indistinguishable from the whole-packet score (Delta AUC = -0.144, 95% CI [-0.471,0.176]) and from a deterministic heuristic (Delta AUC = -0.089, 95% CI [-0.412,0.278]). The pilot establishes an auditable feasibility result and exposes failure modes; it does not establish prospective calibration, causal decision improvement, route-decomposition advantage, or cross-domain validity.

---

## uid: `doi:10.2139/ssrn.7118010`

- title: SemanticZip: Improving Text Steganographic Capacity via LLM-Guided Semantic Lossless Compression
- authors: Shi Ke, Wang Jingang, Liu Peng
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7118010
- keyword hits: large language model, llm

### abstract

Existing generative text steganography methods primarily focus on optimizing the embedding stage while neglecting semantic redundancy mining and efficient coding in the preprocessing phase, which severely limits improvements in steganographic capacity. To address this issue, we propose a large language model-based framework for capacity enhancement, comprising an Adaptive Semantic Lossless Extraction module and a Probability-guided Entropy Adaptive Coding module. The former innovatively establishes a semantic lossless evaluation system to maximize the compression space of redundant text while ensuring strict semantic consistency. The latter integrates arithmetic coding with LLM probability distribution-based token-rank mapping and introduces entropy constraints, achieving highly efficient bitstream compression that approaches the Shannon entropy limit. Experimental results demonstrate that when integrated with mainstream generative steganographic algorithms, our framework increases steganographic capacity by 30.25\% and reduces processing time by 8.23 seconds on average. This method significantly improves transmission efficiency and minimizes transmission frequency, thereby further enhancing steganographic covertness and resistance to steganalysis.

---

## uid: `doi:10.2139/ssrn.7111099`

- title: The Digital Resurrection: Navigating the Legal and Ethical Boundaries of AI Post-Mortem Avatars in Healthcare
- authors: Pranay Katariya
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7111099
- keyword hits: generative ai

### abstract

The rise of high-fidelity generative AI has enabled the construction of post-mortem avatars capable of simulating the voice, personality, and medical knowledge of deceased individuals. In healthcare contexts, such avatars raise unprecedented challenges to a legal architecture predicated on a strict binary of life where rights and duties attach to the living and dissolve at death. This article argues that this binary is no longer tenable. Drawing on Dadbot and emergent regulatory developments under the Data (Use and Access) Act 2025, it proposes a new juridical category to govern the post-mortem deployment of data. This article concludes by proposing the introduction of a 'Digital Executor of Bio Identity' as the centrepiece of a reformed governance framework.

---
