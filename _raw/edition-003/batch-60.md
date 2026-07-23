# Classification batch 60 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-60.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7151418`

- title: Does Generative AI Make Startup Ideas Alike? Evidence from Product Hunt
- authors: Zhaoqi Cheng, Kaige Gao
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7151418
- keyword hits: chatgpt, generative ai, llm, llms

### abstract

Founders increasingly use generative AI to develop new products. Because a market's stock of distinct ideas shapes what it can build next, we ask whether generative AI broadens or narrows the ideas that founders bring to it. We study 291,314 product launches posted to Product Hunt from January 2018 to April 2026. After ChatGPT's release, launches become more concentrated around common category concepts, and the share of distinctive launches falls by more than a third, from 25% to 16%. Using an outcome-blind LLM ideation-exposure index, we find that the post-ChatGPT increase in similarity is larger in categories where general-purpose LLMs can more effectively assist product ideation. First-time teams introduce more distinctive ideas than experienced teams, but similarity rises within both groups, and holding founder composition fixed leaves the exposure gradient essentially unchanged. These findings are consistent with independent founders drawing on a common input and converging toward common category concepts. Generative AI may thus expand individual entrepreneurs' ability to develop products while narrowing the range of ideas that entrepreneurial entry supplies to the market.

---

## uid: `arxiv:2607.18961v1`

- title: From Dependency to Compositionality: A Neurosymbolic Lifting of LLM Outputs via Combinatory Categorial Grammar
- authors: Remo Pareschi
- affiliations: not stated
- posted: 2026-07-21
- source: arXiv
- link: https://arxiv.org/abs/2607.18961v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) generate fluent text by incrementally predicting the next token from a prefix. Critics in the generative tradition argue that such systems lack genuine grammar; influential replies from the dependency-grammar perspective hold that LLM behavior is well described by local head-dependent structure built word by word. We argue that a sharper observation has been overlooked: the prefix-driven, type-completing dynamics of autoregressive generation align closely with the incremental processing model that Combinatory Categorial Grammar (CCG) was originally designed to support. On this basis we propose a neurosymbolic framework in which LLM outputs are lifted into typed compositional derivations -- not claiming that LLMs implement CCG internally, but that their outputs admit a principled, incremental, and auditable CCG reconstruction. Two consequences follow. First, through the Curry-Howard correspondence the lifting extends beyond natural language to the formal languages LLMs also produce -- programming languages such as Solidity, description-logic and query languages such as OWL and SQL -- with the type system varying and the architecture held fixed. Second, the lifting supports two layers of checking: a compositional layer that catches structural failures directly, and a content layer that checks the lifted structure against external knowledge sources, enabling the earliest possible flagging of hallucinated content. The account thereby requires of a producer not cognition but a prefix-driven generative profile. We close with a sketch of synchronous LLM-CCG coupling as one direction the framework opens.

---

## uid: `arxiv:2607.18867v1`

- title: HindsightBench: A Black-Box Behavioral Audit Protocol for Parametric Hindsight in Time-Indexed LLM Decision Tasks
- authors: Haozhe Jia
- affiliations: not stated
- posted: 2026-07-21
- source: arXiv
- link: https://arxiv.org/abs/2607.18867v1
- keyword hits: large language model, large language models, llm, qwen

### abstract

Large language models leak parametric knowledge of realized outcomes into historical financial decision tasks. Existence is settled; what users lack is a cheap way to audit a given model for it. We present HindsightBench, a black-box behavioral audit protocol that profiles parametric hindsight in any time-indexed LLM decision task at probe-level cost (no backtests, no logprobs, no corpus access). The protocol chains a four-arm date-manipulation matrix (revealed/date-only/masked/transplanted), dual memory probes (date recovery; outcome recall), and six per-model metrics -- trigger strength, transplant effect, post-cutoff placebo, recoverability, behaviorally effective knowledge cutoff, and a recall-accuracy dissociation coefficient -- with explicit gates where identifiability is data-dependent. Applying it to 15 models from seven vendors on a 258-node vintage-correct macro panel yields three headline patterns: (i) the date-trigger reflex tracks training generation, not scale -- absent across the 2024 open-weight generation from 1B to 70B, present in every tested 2026-generation model, and switching on within one vendor lineage (Qwen3 -> Qwen3.6) at fixed MoE architecture and 3B active parameters; (ii) effective cutoffs span 22 months across vendors and precede vendor-reported dates by up to eight months, invalidating calendar-window placebo designs; (iii) audit results are not invariant to serving -- BF16 serving of an FP8-referenced model breaks the trigger estimate's stability while AWQ-INT4 preserves it, and a provider-locked reasoning regime makes one probe non-convergent -- so the protocol ships with operational requirements (pin quantization and thinking regime; disclose parser and sampling policy). We release the panel, frozen preregistrations, per-model audit rows with measured dollar costs, transcripts, and one-command regeneration.

---

## uid: `arxiv:2607.18828v1`

- title: Evaluating medical AI under missing information: same-provider judges and human raters change apparent safety
- authors: Koyar Afrasyab
- affiliations: not stated
- posted: 2026-07-21
- source: arXiv
- link: https://arxiv.org/abs/2607.18828v1
- keyword hits: claude, gemini, gpt-5, llm

### abstract

Readiness stress-testing of medical AI has focused on closed-ended and multimodal benchmarks. We extend it to open-ended clinical conversation under missing information, where safe behavior means recognizing absent information and qualifying, clarifying, or not over-committing - and where the evaluator becomes part of the measurement. We stress-test four models - three flagships (Claude Opus 4.8, GPT-5.5, Grok 4.3) and one mid-tier model (Gemini 3.5 Flash) - by deleting the latter half of the final user turn in HealthBench conversations, grading responses with a four-provider LLM-judge panel and a blinded clinician-anchored reference. Two evaluator-facing results are robust. First, judge choice materially changes apparent safety: inter-judge agreement is only moderate (Fleiss' kappa = 0.65), and after adjusting for each judge's general leniency (vote-level logistic regression), a positive same-provider association remains (exact permutation p = 0.04; GPT-5.5 ~ +0.10 on the probability scale) - large enough to change which model appears to over-commit least once its own-provider judge is excluded. Second, LLM judges are more permissive than clinicians on a blinded 50-item subsample: all four are significantly more lenient than the stricter independent clinician (crediting appropriate uncertainty on 66-84% of items vs 52%), and three of four than the author-influenced consensus (Grok directional only; judge-vs-consensus kappa = 0.20-0.43). On the author-audited clinical-underdetermined subset the permissiveness gap widened and the point-estimate model ordering held. A closed-ended MedQA anchor confirms accuracy is high and option-order effects are within a +/-5-point equivalence region for three of four models, so the safety gap is about calibration, not knowledge. We release the harness, prompts, per-item outputs, judge panel, perturbation audit, and human-annotation protocol.

---

## uid: `doi:10.2139/ssrn.7037798`

- title: Position: The Machine Learning Community is Accumulating Calibration Debt Anonymized for Review
- authors: Madhav Mittal
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7037798
- keyword hits: agentic, foundation model, large language model, large language models, retrieval-augmented

### abstract

When a model says it is 90% confident, it should be right about 90% of the time. The gap between expressed confidence and actual reliability—calibration error—has been treated as a percommunity engineering detail. We argue it is something worse: a structural liability that the field is actively accumulating. In early 2026, three independent theoretical results appeared in separate literatures without citing each other. A gradientconflict proof showed that accuracy and calibration objectives point in opposing directions under reinforcement learning from verifiable rewards. A behavioral trilemma showed that helpfulness, calibration, and autonomy cannot be jointly maximized in any RL policy. A mechanism-design impossibility showed that smooth oversight scoring creates endogenous incentives to inflate confidence. Together, they establish that miscalibration is not an accident of implementation—it is a structural consequence of how we train, align, and supervise foundation models. We call this accumulated gap calibration debt, borrowing deliberately from technical debt in software engineering (Sculley et al. 2015). We propose a three-cause taxonomy—Objective Mismatch, Distribution Shift Blindness, and Composition Blindness—supported by evidence across large language models, agentic systems, retrieval-augmented generation pipelines, tabular foundation models, and clinical AI. A two-stage classification pipeline experiment confirms that system-level ECE substantially exceeds the maximum of component-level ECEs, even when each component is individually calibrated. Every existing fix—including conformal prediction and training-time regularisation—addresses at most one cause in one paradigm. We close with four institutional proposals: add ECE to reproducibility checklists, surface accuracy–calibration Pareto frontiers in leaderboards, require pipeline-level calibration for multi-agent papers, and define a Calibration Debt Score for deployment readiness.

---

## uid: `doi:10.2139/ssrn.7161207`

- title: A Large Language Model-Based Unified System for Forest Biomass Estimation and Knowledge Question Answering
- authors: Yuan Zhou, Cunli Lu, Liuyan Wang
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7161207
- keyword hits: deepseek, fine-tuning, large language model, qwen, retrieval-augmented

### abstract

Accurate forest biomass estimation requires selecting appropriate allometric equations from thousands of scattered literature sources, yet equation mismatch frequently introduces systematic errors into carbon-stock accounting. Grassroots forestry practitioners simultaneously face knowledge-intensive demands—concept clarification, regulation queries, silvicultural guidance—fundamentally different from numerical equation retrieval. No existing system addresses both task types within a unified framework. We present FIQS (Forestry Intelligent QA System) with four contributions: AllomEq-RAG, a four-stage metadata-constrained retrieval-augmented generation framework over FEDB (7,394 equations, 256 species, seven geographic zones), which formalizes equation recommendation as a dual-objective optimization over safety and coverage; TAAR, a task-adaptive routing architecture combining a fine-tuned semantic router with parameter-decoupled dual LoRA adapters; and domain LoRA fine-tuning of Qwen1.5-7B-Chat on FIDF 1.0 (115,375 instruction pairs), evaluated on FETS 1.0 (510 questions). LoRA fine-tuning achieves a normalized score of 0.887, surpassing DeepSeek-V3 (0.857), with general-language decline below 3.3 pp. AllomEq-RAG achieves safety 97.5%, coverage 90.2%, and F1 = 0.937 on 522 real-world queries, reducing the inapplicable recommendation rate from 44.1% to 2.5%. TAAR achieves an overall score of 0.85 on a 3,463-query mixed set, outperforming no-routing (0.71) by 19.7% and rule-based routing (0.47) by 80.9%. Three findings emerge: domain LoRA fine-tuning enables a 7B model to exceed substantially larger general models on specialized tasks; metadata-constrained retrieval is essential for equation recommendation safety; and routing quality independently determines multi-path system performance—insufficient routing produces a negative synergy effect that degrades performance below the no-routing baseline. FIDF 1.0, FETS 1.0, and FEDB are publicly available.

---

## uid: `doi:10.2139/ssrn.7158737`

- title: Certified Metric Injection: A Hybrid Deterministic–Large Language Model Architecture for Hallucination-Resistant Enterprise Conversational Business Intelligence
- authors: Ricardo Amodio Neves de Albuquerque
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7158737
- keyword hits: large language model, large language models, llm, llms

### abstract

Natural language interfaces to enterprise data promise to remove the bottleneck between business questions and the underlying data warehouse, but large language models (LLMs) that freely generate SQL for financial and operational key performance indicators (KPIs) are prone to numeric hallucination: plausible-looking queries that silently compute the wrong formula. This paper proposes a hybrid deterministic-LLM architecture for conversational business intelligence that constrains language-model freedom exactly where numeric correctness matters most. The architecture combines (i) a certified metrics catalog of pre-validated SQL expressions that are deterministically detected and injected into the generation context whenever a canonical KPI is referenced, (ii) a schema-linking retrieval step that narrows the prompt to the relevant subset of a large enterprise schema, (iii) a two-pass generation-critique step in which a second model reviews generated SQL for logical errors before execution, (iv) a constrained, read-only execution sandbox, and (v) a cost-aware model-routing layer that reserves larger models for tasks that require them and routes simple operations to smaller, faster models. This paper describes the architecture, the design rationale for each component, and reports qualitative and quantitative observations from a production deployment in a data-intensive enterprise environment, including large relative reductions in time-to-answer for recurring business questions and a marked decrease in dependence on data-analyst intermediation. The architecture's relationship to existing text-to-SQL and hallucination-mitigation research is discussed, along with its limitations - chiefly the single-deployment validation and the maintenance overhead of the certified metrics catalog - and directions for future, multi-organization validation. The proposed pattern generalizes beyond business intelligence to any enterprise setting where an LLM must answer numeric questions against governed data without being trusted to invent the arithmetic itself.

---

## uid: `doi:10.2139/ssrn.7051078`

- title: Shadow AI in Higher Education: A Socio-technical Framework for Governing Unauthorized Employee use of Artificial Intelligence
- authors: Aeron Zentner, Tobi West
- affiliations: not stated
- posted: 2026-07-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7051078
- keyword hits: chatgpt, claude, gemini, generative ai

### abstract

Shadow AI-the use of artificial intelligence tools by employees without institutional approval, procurement review, or datagovernance oversight-is emerging rapidly across higher education as generative AI adoption outpaces institutional policy. This article argues that shadow AI is not principally a compliance failure but a socio-technical governance gap that appears when employee adoption advances faster than an institution's policy, procurement, training, cybersecurity review, and data-governance infrastructure. Drawing on the shadow information technology literature and contemporary research on artificial intelligence governance in higher education, the article advances a conceptual framework, The Shadow AI Adoption-Governance Gap Model, comprising seven dimensions: employee need and use pressure, institutional enablement gap, policy and governance ambiguity, risk awareness and data sensitivity, shadow AI behavior, institutional outcomes, and governance response. The framework is examined against an original 2026 survey of employees at a single two-year public college (50 valid respondents; an 18.9% response rate). Respondents reported high self-assessed AI literacy (98.0% understood basic AI concepts) and strong demand for additional training (84.0%), yet preferred external consumer tools-ChatGPT (72.0%), Google Gemini, Claude, and Microsoft Copilot-none of which were the institution's three sanctioned platforms. Interpreted through the model, this pattern points less to low risk awareness than to institutional enablement gaps and policy ambiguity. The article offers risk-tiered governance recommendations and a practitioner readiness checklist, arguing that institutions should move employees from hidden AI use toward transparent, supported, and ethically governed practice. Because the survey is single-institution and self-reported, the findings are interpretive rather than confirmatory.

---
