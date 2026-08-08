# Classification batch 9 of 20, edition 17

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-017/batch-9.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7228108`

- title: Evidence-Constrained Multimodal Report Generation for Power-System Transient Simulation Review
- authors: Xinyuan Xiang, Jie Zhang, Jiayue Li, Jie Zeng, Hongyu Wang, Dongxia Zhang
- affiliations: not stated
- posted: 2026-08-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7228108
- keyword hits: large language model, large language models, llm, prompting

### abstract

Transient simulation studies in modern power systems produce dense multi-channel recordings that contain the evidence needed for engineering review, but converting these waveforms into traceable reports remains labor intensive. Directly prompting large language models with raw waveform samples can omit local events, misstate numerical evidence, and weaken stability conclusions. This paper advances a report-oriented formulation of transient recording analysis and presents an evidence-constrained multimodal framework that converts dense simulation outputs into auditable engineering reports. Deterministic programs first compute numerical indicators and rule-based stability evidence, render grouped waveform figures, and segment selected channels to extract local trend, range, and extrema attributes. Multimodal generation then converts channel evidence into textual waveform descriptions, while a final language model writes the report under an evidence-consistency protocol that prioritizes rule evidence over numerical indicators, channel descriptions, and visual figures. We evaluate the framework on 320 BPA simulation cases from the IEEE 9-bus, IEEE 39-bus, IEEE 68-bus, and an anonymized regional 109-bus system. Across the tested systems, the framework preserves deterministic stability categories in all cases, achieves numerical faithfulness of 0.9803--0.9927, trend-description accuracy of 0.9000--0.9750, and expert usability scores of 4.23--4.52. Component analysis shows that deterministic evidence constrains conclusions, channel descriptions support trend interpretation, figures improve reviewability, and the consistency protocol reduces unsupported claims. The results indicate that deterministic transient analysis and LLM-based reporting can be combined for offline simulation review within the tested short-circuit simulation scope.

---

## uid: `doi:10.2139/ssrn.7206925`

- title: From Textual Requirements to Microservice Architectures: A Comprehensive Evaluation of LLM-Based Design Synthesis
- authors: Danyllo  Wagner Albuquerque, José Renan, Guillermo Rodríguez, Jorge  Andrés Diaz-Pace, Emanuel  Dantas Filho, Ademar Fran&ccedil;a de Sousa Neto, Mirko Perkusich, Kyller Gorgônio
- affiliations: not stated
- posted: 2026-08-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7206925
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

Microservice architectures have become a dominant paradigm for modernizing monolithic systems. However, identifying appropriate services remains a challenging and largely manual task. Existing decomposition approaches are predominantly code-centric, limiting their applicability in early design stages where only textual requirements are available. [Problem]. Despite recent advances in Large Language Models (LLMs), there is still limited empirical evidence regarding their ability to synthesize complete microservice architectures directly from natural-language requirements, including both service definitions and inter-service interactions. [Goal]. This study investigates whether an LLM can bridge the gap between requirements engineering and architectural design by generating microservice architectures solely from textual requirements, and evaluates the structural agreement and perceived quality of the generated solutions. [Method]. We conduct a mixed-method study using the OpenAI o3 model under zero-shot (ZS) and few-shot (FS) prompting strategies across two systems (Bookstore and PetClinic), with one execution per system and prompting condition. Generated architectures are evaluated through (i) quantitative comparison with implemented reference architectures using precision, recall, and F1-score for service identification and communication recovery, and (ii) a blinded expert assessment of correctness, completeness, modularity, and plausibility, supplemented by a structured descriptive synthesis of open-ended feedback. [Results]. The findings indicate that OpenAI o3 can identify services from requirements, achieving higher agreement with the references under FS prompting (F1 ≈ 0.79 for ZS and ≈ 0.97 for FS). Communication recovery is more challenging, with ZS producing overly dense architectures characterized by high recall but low precision (F1 ≈ 0.61). FS prompting improves structural agreement and perceived architectural quality, achieving F1 ≈ 0.82 for communication recovery while reducing unsupported dependencies. Expert evaluation corroborates these findings, indicating that FS-generated architectures are consistently perceived as more modular, coherent, and plausible than ZS outputs. [Conclusion]. Within the evaluated scope, OpenAI o3 shows potential to support requirements-driven architectural synthesis, particularly when guided by minimal exemplar-based prompting. The results should be interpreted as model- and context-specific evidence from two relatively small systems and a single execution per condition, rather than as model-independent proof of effectiveness.

---

## uid: `arxiv:2608.03731v1`

- title: CARE-Bench: Benchmarking Patient-Facing LLM Triage
- authors: Yining Hua, Hongbin Na, Cyrus Ayubcha
- affiliations: not stated
- posted: 2026-08-04
- source: arXiv
- link: https://arxiv.org/abs/2608.03731v1
- keyword hits: gpt-5, llm, llms, prompting

### abstract

Patient-facing medical LLMs and agents increasingly answer symptom questions before clinician contact, where the key safety question is what action the user should take next. We introduce CARE-Bench, a source-grounded benchmark that evaluates sequential patient-facing triage as a four-label per-turn current-action task. CARE-Bench contains 500 cases and 1,059 evaluated patient-disclosure prefixes reconstructed from medical dialogue, consultation, and follow-up-question sources. We evaluate 11 models on 269 held-out rounds under unprompted and minimally prompted open-ended protocols, using a fixed GPT-5.5 mapper to code each response into the four-label action space. Unprompted macro-F1 remains low, ranging from 31.2 to 50.4. Prompting improves 10 of 11 models, with prompted macro-F1 ranging from 46.9 to 63.4, but substantial threshold errors remain. Prompted models often recommend care before needed clarification is obtained; when the correct action was to ask for more information, only 33.5% of prompted outputs preserved the step. The persistence of these errors after prompting suggests that patient-facing triage is not a simple prompting problem and supports explicit evaluation of action timing before deployment.

---

## uid: `arxiv:2608.03291v1`

- title: The Tell-Tale Trace: Detecting Reasoning Failures in LLMs Using Chain-of-Thought Dynamics
- authors: Shashwat Sourav, Aishwarya Balwani
- affiliations: not stated
- posted: 2026-08-04
- source: arXiv
- link: https://arxiv.org/abs/2608.03291v1
- keyword hits: chain-of-thought, large language model, llama, llm, llms

### abstract

Chain-of-thought (CoT) reasoning improves large language model (LLM) performance while also providing an observable interface to the model's reasoning process. Existing approaches that leverage verbalized CoTs to monitor reasoning correctness, however, largely evaluate the semantic correctness or consistency of individual intermediate steps, rather than how the reasoning process evolves across the trace. As a result, failures distributed across the reasoning trajectory, rather than those localized to a single incorrect step, remain comparatively underexplored. Furthermore, verbalized CoTs need not faithfully reflect the model's internal reasoning, motivating analyses that do not treat individual statements as literal accounts of internal computation. In this work, we therefore ask whether the dynamics of visible CoT can be leveraged to systematically distinguish successful from failed reasoning without assuming such semantic faithfulness. We study a range of LLMs on verifiable Boolean satisfiability tasks with variable complexity, enabling controlled comparisons near each model's capability frontier. Tagging CoT sentences by reasoning function reveals premature verification collapse on SAT problems: incorrect traces enter clause checking earlier, repeat similar operations, and finalize sooner. On UNSAT problems, models presumptuously move towards incorrect SAT conclusions, checking candidate assignments rather than deriving contradictions across constructed cases. Subsequently, a targeted proof-search prompt intervention raises Llama3-70B accuracy from 13.3% to 85%, correcting 84.6% of these errors. These results show that capability failures can manifest as distributed, task-dependent changes in the structure of visible reasoning, and that CoT dynamics agnostic to whether the verbalized trace reflects the model's internal computations can help diagnose and correct failures.

---

## uid: `doi:10.2139/ssrn.7184598`

- title: LLM-Powered Intelligent Document Analyzer for Educational Content Understanding
- authors: Phadtare Nutan Devram, Gadhagoni Sharath, Raghav Mehra
- affiliations: not stated
- posted: 2026-08-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7184598
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

We propose a new multi-modal system for educational content analysis, utilizing large language models (LLMs) and vision technologies. Our system takes in scanned or digital copies of textbook pages, performs OCR and image analysis to identify text and graphics, and then uses an LLM (such as GPT- 4 with vision capabilities) to analyze the content. The system builds a knowledge graph of educational concepts and uses Socratic questioning techniques for explanation and question- answer generation. This system design incorporates modules for preprocessing, concept mapping, summarization, and assessment item generation. In our user studies, students using our automatic lecture summary system outperformed those with direct content access, demonstrating the educational value of our system. We show that our content analyzer generates highly comprehensive, fluency-maximized summaries and Bloom-aligned quizzes, substantially improving educational content understanding. Our contributions are: (1) A system pipeline combining OCR, vision analysis, knowledge graph building, and LLM reasoning for textbooks and lectures; (2) A new prompting technique for generating brief explanations and structured question generation; and (3) An interactive feedback mechanism with educators to improve system output. The system shows significant ROUGE- L and accuracy improvements over baselines, suggesting its utility for adaptive learning and automated educational content processing.

---

## uid: `doi:10.2139/ssrn.7177038`

- title: Observation-Centered Runtime Safety for Foundation-Model Agents: A Model-Agnostic Geometry–Risk–Control Architecture
- authors: Tomohiko Nakamura
- affiliations: not stated
- posted: 2026-08-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7177038
- keyword hits: claude, fine-tuning, foundation model, large language model, large language models

### abstract

Alignment research for large language models has focused primarily on model-centric interventions-fine-tuning, preference optimization, and decoding-time filters. These methods improve average behavior, yet they do not continuously observe or constrain the runtime trajectory of an agent as it acts in a tool-using environment. We present an observationcentered runtime safety architecture that treats semantic state as a measurable trajectory and separates safety into five strictly layered concerns: Observation, Geometry, Risk, Control, and (future) Execution. The architecture is realized as the SensOS Runtime Safety Layer through a staged experimental program. Heterogeneous agent events are normalized into an Observation Object and projected to a trajectory; a model-agnostic geometry engine estimates curvature, boundary distance, density, stability, and basin membership; a risk engine converts those descriptors into a continuous risk valuation with hysteresis and early warning; and a control engine maps risk to a graduated L0-L7 decision under an approval interlock. Execution against a live agent is intentionally excluded: control outputs are decisions only, pending a separate safety review. On a real Claude Code session (n = 489 events), end-to-end observation pipeline latency was 0.094 ms mean per event (alert-only; zero alerts at threshold 0.5). Geometry, risk, and control packages exhibit production-grade software engineering quality-full statement and branch test coverage (95/151/107 tests)-with measured sub-millisecond risk and control latencies (0.0067/0.0039 ms mean). These figures characterize software quality and microbenchmarks, not validated operational safety. We do not claim live intervention efficacy; we claim a coherent, measured, and architecturally honest decision spine for runtime safety without modifying foundation models.

---

## uid: `arxiv:2608.04828v1`

- title: Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?
- authors: Jinyi Han, Yuanjian Xu, Ying Liao, Xinyi Wang, Zishang Jiang, Zixiang Di, Fanyang Lu, Zhichao Hu
- affiliations: not stated
- posted: 2026-08-05
- source: arXiv
- link: https://arxiv.org/abs/2608.04828v1
- keyword hits: agentic, large language model, llm, llms

### abstract

Large language model (LLM) agents increasingly rely on skills, structured documents that specify when to act, which procedure to follow, and which tools are allowed. Existing evaluations mostly judge the quality of a skill or its contribution to task success, leaving unexamined whether an agent can recognize a relevant skill and apply it on its own. We introduce Skill-Use, a benchmark that evaluates skill use under progressive disclosure, where an agent sees only a skill's name and short description and must retrieve the full procedure before following it. Skill-Use separates three facets of skill use. Trigger measures whether the agent invokes the relevant skill, Compliance measures how faithfully it follows the prescribed procedure, and Boundary measures whether it avoids forbidden operations. A Skill-Use (SU) score combines the three and credits execution only after the skill is triggered. Skill-Use pairs 79 real skills with 177 executable tasks across nine domains, each grounded in real files, run in an isolated Docker sandbox, and scored by a trajectory-based rubric. Evaluating eight LLMs under two agent harnesses, we find that reliable skill use remains out of reach, as the strongest configuration reaches an SU of only 0.613. Triggering and procedural compliance fail as independent bottlenecks, and both scores and model rankings shift with the harness, so skill use behaves as a capability conditioned on the harness rather than a fixed property of the model.

---

## uid: `arxiv:2608.04646v1`

- title: Evaluating Theory of Mind in Reasoning Models: Robustness over Reasoning
- authors: Ian B. de Haan, Peter van der Putten, Max van Duijn
- affiliations: not stated
- posted: 2026-08-05
- source: arXiv
- link: https://arxiv.org/abs/2608.04646v1
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

Large language models (LLMs) have recently shown strong performance on Theory of Mind (ToM) tests, prompting debate about the nature and validity of the underlying capabilities. At the same time, reasoning-oriented LLMs trained via reinforcement learning with verifiable rewards have demonstrated notable improvements across a range of benchmarks. In this work, we examine the behavior of such reasoning models in ToM tasks using novel adaptations of machine psychological experiments together with results from established benchmarks. We observe that reasoning models consistently exhibit increased robustness to prompt variations and task perturbations. Our analysis suggests these gains come at least partly from models being more robust at reaching the correct answer under prompt and task variation. We read this as evidence for a robustness-based account rather than for a new ToM-specific ability.

---
