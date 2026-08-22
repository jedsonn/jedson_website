# Classification batch 14 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-14.answer.json` as a JSON array.

---

## uid: `arxiv:2608.14950v1`

- title: DA-RAC: Distance-Aware Calibration of LLM Judges for Trustworthy AI Auditing
- authors: Cheng Wu, Vishal Anand, Jaya Krishna Mandivarapu, Xiya Liu, Rui Zhuang
- affiliations: not stated
- posted: 2026-08-15
- source: arXiv
- link: https://arxiv.org/abs/2608.14950v1
- keyword hits: chain-of-thought, generative ai, llm

### abstract

Generative AI systems are increasingly producing real-world artifacts, however their efficacy and validity are often evaluated via context-free LLM-scoring. These judges can be miscalibrated by irrelevant in-context reference examples, creating false confidence and allowing low-quality or harmful outputs to pass evaluation. We study this failure mode as context-induced miscalibration and introduce DA-RAC, a distance-aware reference-anchored calibration method for LLM judges. DA-RAC retrieves semantically and structurally similar labeled anchors for each judgement scenario, weights them by distance, and exposes neighborhood difficulty as a calibration and triage signal. On multi-run LLM-judge evaluation benchmarks, it improves calibration and reduces false-pass risk relative to zero-shot, chain-of-thought evaluation, and static-anchor baselines. Mechanistic analysis shows that judge scores vary systematically with anchor distance, while static references can induce misleading decision boundaries. Thus LLM-judgement requires not only better models, but also calibrated, auditable reference selection, especially when automated evaluation is used to support high-impact AI generated artifacts. Judgments should be grounded in relevant, inspectable, and contestable interpretive artifacts.

---

## uid: `doi:10.1145/3832783.3834531`

- title: Kozuchi Agent: A Language-Agnostic Open-Weight Agent for Software Repair
- authors: Mehdi Bahrami, Kosaku Kimura, Satoshi Munakata, Satoshi Nakashima, Yu Ishikawa, Kosuke Maeda, Nao Soma, Kenichi Kobayashi
- affiliations: not stated
- posted: 2026-08-16
- source: arXiv
- link: https://arxiv.org/abs/2608.15579v1
- keyword hits: fine-tuning, llm, qwen

### abstract

Industrial software-engineering teams increasingly need LLM agents that turn bug reports into correct patches, yet benchmark-scale operation adds long horizons, tool-use discipline, context persistence, heterogeneous clusters, and evaluation reuse. We present Kozuchi Agent, a language-agnostic open-weight repair agent and CI-operated evaluation pipeline. Explicit phases, persistent state, deterministic tools, a model-independent action interface, and cross-agent test-time selection make runs auditable and repeatable. With locally hosted Qwen3.5-27B, no fine-tuning, and TTS@8, Kozuchi resolves 374/500 SWE-bench Verified instances on the official evaluator. Unchanged on Multi-SWE-bench Java, the same 27-billion-parameter agent resolves 41/128 instances (32.03%), ranking first among strict open-weight submissions and fourth of 42 overall; on Python it ranks 12th of 135 and first among open-weight systems. Per-phase behavior remains within +/-5 percentage points across languages. Remaining failures mainly reflect semantic correctness, Java-specific harness issues, and selection errors. Across both tracks, results compare favorably with open/local peers by parameter count. Analysis of candidate diversity, selector regret, and patch reliability shows that the remaining gap is primarily semantic correctness and selection rather than edit formatting or proprietary-model access. Operationally, reusable CI stages reduce operator touch-points from five to one across heterogeneous internal clusters.

---

## uid: `doi:10.2139/ssrn.7305416`

- title: S-BEED: Sparse Bayesian Ensemble with Entropy-Calibrated Debate for Medical Multiple-Choice Question Answering
- authors: Wangyun Dan, Suyang Xi, Chenzi Guo, Ximing Ran, Zhaohui Qin
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7305416
- keyword hits: large language model, large language models, prompting

### abstract

Background and Objective: Both accuracy and reliable calibration are necessary for deploying large language models in medical question answering, where overconfident errors translate directly into clinical risk. Existing approaches, whether single-model prompting, static ensemble voting, or free-form multi-agent debate, either yield poorly calibrated confidence estimates or incur prohibitive inference costs.Methods: We introduce S-BEED, a sparse multi-agent framework that treats the group belief distribution over candidate answers, rather than a single hard label, as the primary object of inference, giving clinicians and downstream systems an interpretable uncertainty signal they can act on. For each question, a slice-aware router activates a small subset of reliable agents that revise their option-level beliefs through a structured, entropy-weighted debate, and the aggregated group belief is calibrated at the output layer.Results: Across MedQA, MMLU-Clinical, and MedMCQA-Single, S-BEED achieves the highest accuracy and the lowest expected calibration error on all three datasets while using far fewer tokens than dense and dedicated multi-agent baselines (up to roughly 94% fewer) and remaining comparable in cost to simple ensembling. In a selective-prediction analysis, deferring the least-confident predictions reduces error faster for S-BEED than for the single-best model on every dataset. A single-parameter output-layer temperature scaling further improves the calibration error, the Brier score, and the negative log-likelihood without changing accuracy, indicating that the raw group beliefs are well ranked but over-sharpened, and ablation experiments confirm that sparse routing, the structured debate protocol, entropy-aware influence weighting, and early convergence stopping each contribute to overall performance.Conclusions: Treating a sparse, calibrated group belief as the primary inference target yields medical question answering that is simultaneously more accurate, better calibrated, and more efficient than existing approaches.

---

## uid: `doi:10.2139/ssrn.7313387`

- title: Coordinating Multiple Rewards in Rank Space for Spatial Reasoning
- authors: Han Wang, Ziru Wang, Haowen Sun, Xinzhe Chen, Xingyu Chen, Zeyang Liu, Xuguang Lan
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7313387
- keyword hits: chain-of-thought, large language model, large language models

### abstract

Multimodal large language models (MLLMs) have achieved remarkable progress in vision–language tasks, but continue to struggle with spatial reasoning. Existing spatial MLLMs rely on large-scale datasets, explicit 3D inputs, architecture-specific modifications, or sparse Reinforcement Learning (RL) methods that provide insufficient guidance for spatially-grounded reasoning.Moreover, such algorithms based on sparse outcome-driven rewards often yield ``right-answer wrong-path'' false positives, where conclusions are correct but the underlying geometric logic is flawed. Although process reward models are typically introduced to provide dense intermediate supervision, combining noisy process scores with outcome rewards via standard zzz-score normalization contaminates in-group statistics and induces reward hacking. Meanwhile, on already-correct groups the vanishing outcome signal leaves flawed "right-answer wrong-path" reasoning uncorrected. Together these failure modes stall or even degrade spatial-reasoning gains. To overcome this, we propose RT-GRPO, a Rank-Transformed GRPO framework that constructs advantages in rank space rather than using raw reward values. Our framework introduces two key innovations: (i) a lexicographic advantage formulation that prioritizes format compliance as a hard gate, outcome correctness as the primary order, and process quality strictly to break ties; and (ii) a batch-level information weighting mechanism that suppresses zero-signal groups while preserving gradients for process refinement in already-correct groups. Evaluations across three complementary benchmarks (RoboBench, RoboSpatial-HOME, and 3DSRBench) demonstrate that RT-GRPO establishes a new state-of-the-art among comparably sized models. Furthermore, real-world deployment on a Franka FR3 robot confirms its superior robustness and the practical efficacy of its chain-of-thought reasoning.

---

## uid: `doi:10.2139/ssrn.7313999`

- title: The Knowledge-Model Separation Reframing LLM Migration as an Evaluation Event in Enterprise Operational AI
- authors: John Rendek
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7313999
- keyword hits: fine-tuning, large language model, large language models, llm

### abstract

Enterprise teams building on large language models treat every model upgrade as a re-platforming event: prompts get re-tuned, fine-tunes get redone, and confidence in the system resets to zero. This paper argues that most of that cost is unnecessary, and that it is unnecessary because most operational AI systems already contain, whether or not their builders have named it, three distinct kinds of intelligence that do not need to travel together. Knowledge-the facts, records, and relationships an enterprise depends on-belongs in an external, queryable structure, most durably a knowledge graph, that the LLM reads rather than memorizes. Patterns-the statistical regularities that predict outcomes from operational data-belong in trained models such as gradient-boosted trees, which persist independently of any LLM. Behavior-the house style, tone, and task-specific habits an organization wants from its AIbelongs, when it is needed at all, in small adapter modules that can be retrained cheaply and separately from both of the above. Once knowledge and pattern are separated from the LLM itself, swapping the LLM stops being a retraining event and becomes an evaluation event: the new model is graded by replaying the organization's own decision log against it, the same way a student is examined on material rather than retaught it from scratch. This paper situates that claim against the published literature on retrievalaugmented generation, graph-based retrieval, parametric knowledge, knowledge editing, and parameterefficient fine-tuning, and argues that its contribution is the synthesis: naming knowledge-model separation as the design principle that makes LLM interchangeability a property an enterprise can engineer for, rather than an accident of vendor lock-in avoidance.

---

## uid: `doi:10.2139/ssrn.7317098`

- title: WeClaw: An Open-Source Adaptive Runtime Framework for Tool-Augmented Desktop LLM Agents
- authors: YONGGANG WENG
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7317098
- keyword hits: deepseek, llm, prompting, qwen

### abstract

Desktop LLM agents that invoke tools fail in mundane but costly ways: large tool catalogs inflate prompts, the same tool-specific errors recur across sessions, and long conversations can lose tool-call/result pairing during compression. WeClaw, an open-source and deployed adaptive runtime for desktop agents, treats these failures as software-reliability problems rather than isolated prompting mistakes. It combines Progressive Tool Exposure with Failure-Driven Escalation (PTE-FD), Event-Based Experience Auto-Capture (EBEAC), and a Robust Context Pipeline (RCR). PTE-FD first exposes about ten recommended tools and broadens the set only after observable execution failures. EBEAC records failure patterns from the runtime event bus without extra LLM calls. RCR preserves the structural contract between assistant tool calls and tool results before context pruning. We evaluated PTE-FD across four OpenAI-compatible back-ends (deepseek-v4-flash, qwen-max, moonshot-v1-8k, and glm-4-flash), using three seeds per model and N=288 pooled matched outcomes per model. PTE-FD achieved the highest tool-selection accuracy for every back-end, significantly outperforming full static exposure (Holm-Bonferroni-corrected p

---

## uid: `doi:10.2139/ssrn.7318619`

- title: Governing AI Coding Agents: From Repository Artifacts to Organizational Capability
- authors: Muhammad Hamza
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7318619
- keyword hits: ai agent, claude, llm

### abstract

Purpose: Software projects are increasingly adopting repository-level governance artifacts, such as CLAUDE.md and AGENTS.md, to communicate projectspecific guidance to AI coding agents. Although these artifacts have become an important mechanism for governing AI coding agents, little is known about the governance practices and governance liabilities they represent or the extent to which they reflect broader organizational governance capability. This study investigates repository-level AI agent governance through the lens of organizational capability theory. Method: We conducted an exploratory sequential mixed-methods study. Using the STGT4DA methodology, we developed taxonomies of governance practices and governance liabilities and converted them into a structured codebook for LLM-based classification. The classification approach was evaluated against manually coded reference labels, and the retained governance constructs were subsequently applied to a corpus of 555 AI agent governance artifacts collected from public GitHub repositories to investigate whether repository-level governance artifacts exhibit characteristics theoretically associated with organizational capability across repositories. Results: The findings reveal that these artifacts primarily emphasize project orientation, knowledge transfer, and implementation guidance, whereas verification, oversight, accountability, and continuous governance management remain comparatively limited. The analysis also identifies recurring governance liabilities that may limit the effectiveness of AI agent governance. Furthermore, the artifact-level governance capability score is not systematically associated with the repository maturity indicators examined in this study or with application domains used as broad proxies for operational risk, and the observed governance artifacts provide limited evidence of the characteristics associated with institutionalized governance. These findings indicate that the presence of repository-level governance artifacts alone should not be interpreted as evidence of mature organizational governance capability. Conclusion: This study provides an ecosystem-scale empirical investigation of repository-level AI agent governance from an organizational capability perspective. By examining governance artifacts according to the governance functions they perform rather than solely the information they contain, the proposed taxonomies, LLM-based classification approach evaluated against manually coded reference labels, and empirical findings provide a foundation for systematically evaluating AI agent governance in both research and practice.

---

## uid: `doi:10.2139/ssrn.7316998`

- title: Agentic Schema Convergence: An AI-Driven Pipeline for Combined Schema Design and Data Migration in Technology M&A
- authors: Athresh Guruprakash
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7316998
- keyword hits: agentic, large language model, large language models

### abstract

Schema convergence and data mapping are consistently the slowest, most manual stages of technology M&A integration-typically weeks of analyst effort, tribal knowledge, and spreadsheet-based mapping documents that go stale before implementation finishes. Recent work applying large language models to schema matching and entity resolution suggests these tasks are structurally well suited to AI assistance, but most published work treats schema matching as an isolated benchmark task rather than as one stage in an end-to-end migration pipeline with real compliance and reliability constraints. This paper proposes Agent-Assisted Schema Convergence (AASC), a five-agent architecture-Schema Intelligence, Data Profiling, Canonical Design, Mapping, and Pipeline Design agents-that carries the work from raw source/destination schema review through to a deployable migration pipeline, with a defined human-in-the-loop checkpoint at every stage and no agent output auto-applied to production schema or data without reviewer sign-off. The Mapping Agent's confidence-scoring and review-queue design receives the most detailed treatment, since it is where automation and regulatory risk intersect most directly. Two case illustrations are worked through: a ticket/interaction data migration (chosen specifically because it is comparatively PII-light yet still carries distinct compliance obligations that argue for separating it from the main customer data migration) and a customer/account data migration, where the same fiveagent pipeline runs with materially different review posture. The result is a practical, implementable blueprint for where agentic AI can accelerate M&A data integration work, and an equally explicit account of where it cannot yet be trusted to run unsupervised.

---
