# Classification batch 213 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-213.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6965278`

- title: Execution-Bound Advisory Automation for Agentic AI: A Reproducible AIBOM-Driven CSAF-VEX Framework
- authors: Petar Radanliev, Omar Santos, Carsten Maple, Kayvan Atefi
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6965278
- keyword hits: agentic, foundation model

### abstract

Introduction: Agentic AI systems integrate foundation models, prompt templates, tool connectors, orchestration logic, and containerised dependencies, creating exploitability conditions that cannot be inferred from static Software Bills of Materials (SBOMs). Artificial Intelligence Bills of Materials (AIBOM) extend transparency to AIspecific artefacts, yet current CSAF/VEX workflows remain based on static component-CVE correlation without runtime validation. Materials and Methods: A protocol-driven framework is presented that binds SBOM and AIBOM artefacts to deterministic environment capture and structured runtime telemetry. Exploitability is computed from declared artefacts, observed activation conditions, and enforced execution policies. CSAF-VEX advisories are generated from combined static and runtime evidence, cryptographically signed, and validated through deterministic replay. Evaluation uses approximately 10,000 component entries across synthetic Agentic AI workloads (50-5,000 components), incorporating OSV, GitHub Advisory, KEV, and EPSS datasets. Results: Under controlled experimental conditions, the framework achieves an F1score of 0.93 (precision 0.96, recall 0.92), reduces false positives by up to 42% relative to static SBOM-CVE matching without runtime validation, and alters exploitability outcomes in 31% of AI-specific artefact cases through AIBOM extension. Advisory artefacts remain reproducible under deterministic replay. Discussion: Binding AIBOM artefacts to runtime telemetry transforms CSAF-VEX generation from static disclosure into execution-grounded exploitability assessment for Agentic AI supply chains.

---

## uid: `arxiv:2607.14275v1`

- title: AI Agents Do Not Fail Alone:The Context Fails First
- authors: Fouad Bousetouane
- affiliations: not stated
- posted: 2026-07-15
- source: arXiv
- link: https://arxiv.org/abs/2607.14275v1
- keyword hits: ai agent, llm

### abstract

Context engineering has become central to building reliable AI agents, yet it remains largely unmeasured. Agents do not fail in isolation: their behavior is shaped by the instructions, tools, memory, retrieved knowledge, guardrails, and untrusted inputs accumulated in their context. When this context is weak, agents drift, hallucinate, misuse tools, ignore constraints, become vulnerable to injection, and waste tokens. This paper validates context-engineering quality as an independent leading indicator of agent reliability. We implement the measurement in ProofAgent-Harness, an open-source infrastructure for AI agent evaluation that uses multi-juror, consensus-based scoring. The harness assesses context across seven criteria: role clarity, guardrail coverage, instruction consistency, tool schema quality, grounding sufficiency, injection hardening, and token efficiency. Crucially, the context score is isolated from behavioral metrics and release decisions, enabling a non-circular validation. Through a controlled context-quality study across regulated agent domains, holding frontier LLM agents fixed and varying only their operating context, we show that context-quality criteria consistently predict their corresponding behavioral outcomes. Grounding sufficiency predicts hallucination resistance, guardrail coverage predicts manipulation resistance, instruction consistency predicts instruction following, and tool-schema quality predicts tool use. These findings establish context measurement as a validated preflight signal for agent reliability and position context engineering as an auditable layer of agent evaluation and governance.

---

## uid: `arxiv:2607.13707v1`

- title: The Test Oracle Problem in Synthetic LLM-as-Judge Corpora: Disappearance, Distortion and a Validation Protocol
- authors: Serkan Ballı
- affiliations: not stated
- posted: 2026-07-15
- source: arXiv
- link: https://arxiv.org/abs/2607.13707v1
- keyword hits: llm, prompting

### abstract

Studies of bias in LLM-as-judge systems typically build synthetic corpora by prompting an LLM to generate a hallucinated answer to pair with a factual one, then presenting both to a judge. We report a case in which this generation step silently failed, and use it to argue that the failure mode is structural rather than incidental. In a multilingual (Turkish/English) faithfulness-judgment corpus, a decoding-budget parameter shared between judging and generation calls truncated one producer's hallucinated answers to a few words. The resulting items produced a large, statistically robust effect: a 32-point cross-lingual collapse in one judge's selection accuracy, replicated from N=50 to N=500, explained by a three-layer mechanistic account, and confirmed by a controlled producer-swap experiment, none of which was real. The effect vanished to ceiling once the shared parameter was corrected, and only manual reading of the raw generations, not any aggregate statistical check, exposed the fault. A second measured bias (Markdown-formatting preference) was not fabricated but distorted by the same fault, its magnitude and in one case its sign shifting with stimulus length, a mode aggregate metrics cannot distinguish from the first. We frame the underlying vulnerability using the test oracle problem: corpora whose negative examples are LLM-generated carry no mechanical way to verify item integrity, while corpora built by deterministic perturbation of a gold answer carry an item-level oracle for free. A positive control supports this claim directly: an analogous fault injected into a minimal perturbation-based corpus is caught with 100% accuracy by a zero-cost, zero-human gold-to-negative string comparison. We close with a validation protocol, derived from our own case, for analysts working in the oracle-less regime that we argue describes most contemporary multilingual LLM-as-judge corpora.

---

## uid: `doi:10.2139/ssrn.6976098`

- title: Three Paradigms, One Label: Why AI Investment Fails and How to Fix It
- authors: Alok Khatri, Anisha Gyawali
- affiliations: not stated
- posted: 2026-07-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6976098
- keyword hits: agentic, generative ai

### abstract

Despite 88% of organizations using AI in at least one business function, only approximately 6% generate substantial enterprise value from these investments. Annual AI infrastructure spending reached $47.4 billion in early 2024, up 97% year-over-year, yet most organizations struggle to translate adoption into measurable performance gains. One of the prominent reasons this gap exists is because organizations treat all AI as a single category, applying inappropriate investment logic across fundamentally different problems. This paper develops a three-paradigm framework distinguishing Traditional AI (production problem), Generative AI (deployment problem), and Agentic AI (governance problem). Observational findings indicate that generative AI productivity improvements of 40 to 60 percent emerge within weeks when organizations focus on workflow redesign and workforce capability rather than proprietary model development. Organizations reporting substantial financial impact are 2.8 times more likely to have fundamentally redesigned workflows, yet fewer than one-third of AI adopters have done so. Most organizations continue allocating nearly half of AI budgets to technical departments rather than deployment capabilities. Investment strategy should align with paradigm-specific constraints. For common enterprise use cases, deployment capability rather than model development represents the binding constraint. Organizations must diagnose whether initiatives require production investments (proprietary models), deployment investments (workflow redesign), or governance investments (accountability structures) before allocating resources. Misalignment between paradigm and investment approach explains much of the observed gap between AI adoption and enterprise value capture.

---

## uid: `doi:10.2139/ssrn.6975000`

- title: From AI Detection to Inquiry Governance: Initial Validation of the ALPE Framework for AI-Mediated Learning
- authors: Franklin Garvida
- affiliations: not stated
- posted: 2026-07-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6975000
- keyword hits: agentic, generative artificial intelligence

### abstract

The rapid adoption of generative artificial intelligence (GenAI) has destabilized a foundational assumption of educational assessment: that a student's final submission reliably represents the cognitive processes that produced it. Output-based approaches to academic integrity can no longer distinguish learners who engage substantively with AI from those who passively delegate cognitive labor. This paper introduces the Academic Legitimacy and Provider Evaluation (ALPE) Framework, a process-based governance framework that reorients assessment from product authenticity toward inquiry transparency, cognitive accountability, and epistemic agency. The framework defines a five-stage continuum-from Output Only to Agentic and Generative Inquiry-that enables institutions to evaluate the legitimacy of AImediated inquiry. The paper reports preliminary validation evidence. An independent conceptual validation confirmed the epistemological coherence of the continuum. A sixmember expert panel with over a decade of experience in AI literacy and assessment rated the stage definitions as clear, relevant, and distinct (CVI = 0.83). An inter-rater reliability study, in which five faculty raters classified 30 ecologically valid scenarios without prior training, achieved a Fleiss' Kappa of 0.81 (95% CI [0.77, 0.86]); all disagreements were confined to adjacent or near-adjacent stages and clustered at the theoretically predicted Stage 2-3 boundary. These results provide initial support for ALPE as a reliable governance framework and converge across two independent methods on the same conceptual seam. The paper concludes by outlining a future validation agenda and discussing implications for AI literacy, assessment design, and institutional governance in the age of AI.

---

## uid: `doi:10.2139/ssrn.7119315`

- title: OmniGene-4: A Locally-Deployable Bio-Language MoE Model with BioPAWS-2
- authors: Liang Wang
- affiliations: not stated
- posted: 2026-07-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7119315
- keyword hits: fine-tuning, foundation model

### abstract

We present two coupled contributions for biological foundation modeling. First, OmniGene-4, a unified bio-language Mixture-of-Experts model built on Gemma-4-26B-A4B (128 experts/layer, top-8 routing, ≈3.8B active parameters) trained at ~1.5 GPU-days of total fine-tuning — roughly four orders of magnitude less compute than recent specialized MoE bio-models — and locally deployable (4-bit / Q4_K_M GGUF on a single 24 GB GPU such as an RTX 4090). One model spans eight modalities (DNA, protein, structural alphabets, natural language, and, in the multi-modal extension OmniGene-4-MM, molecular/medical/chart imagery). It exhibits two capabilities that do not depend on task-specific training: zero-shot remote-homology detection (82.6%, exceeding ESM-2 3B, MMseqs2, and DIAMOND by 28–31 pp on identical pairs), and a router-level decomposition suggesting continued pretraining (CPT) reshapes middle-layer routing while supervised fine-tuning (SFT) adjusts output-layer routing. Second, to evaluate such models fairly — the landscape being fragmented across paradigm-specific formats (PLM-plus-head benchmarks vs. free-form QA, with no common axis) — we release BioPAWS-2, a public chat-form instruction-tuning benchmark and training resource (9 task families, 22 tasks, 306K examples) with a dual zero-shot / fine-tune protocol. We treat data integrity as first-class: an MMseqs2 leakage audit is released, all sequence tasks use entity-disjoint splits (homology leakage 0.78→0.08), and re-running every supervised result on the clean splits moves the headline by only -1.4 points. A matched raw-Gemma-base control under identical joint fine-tuning shows biological CPT confers no material advantage under SFT (0.769 vs. 0.760) — we use our own benchmark to argue against a self-serving conclusion, establishing BioPAWS-2 as a model-agnostic resource and locating OmniGene-4's value in deployment cost, modality breadth, and zero-shot behaviour rather than SFT headroom. Model checkpoints and the full benchmark/code are public.

---

## uid: `doi:10.2139/ssrn.7117525`

- title: Enhancing Policy Question Answering with Traceable GraphRAG: A Hierarchical Knowledge Graph Framework with Constrained Generation
- authors: Shijie Peng, Mingjie Li, Wei Long, Chi Liu, Kaishu Zhang
- affiliations: not stated
- posted: 2026-07-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7117525
- keyword hits: llm, retrieval-augmented

### abstract

To address the limitations of conventional Retrieval-Augmented Generation (RAG) in policy and compliance-centric question answering—where coarse-grained chunking and isolated vector retrieval destroy document topology and cause semantic fragmentation, hallucinations, and poor traceability—this paper proposes Traceable Hierarchical GraphRAG (TH-GraphRAG), a novel framework tailored for structured regulatory documents. The framework introduces a three-tier Hierarchical Policy Knowledge Graph (HPKG) to preserve the Document-Chapter-Article logical topology and cross-clause references, utilizes a vector-graph hybrid retrieval mechanism that fuses dense semantic matching with graph structural reasoning to recall clauses alongside their hierarchical context, and implements a hard-constrained generative paradigm with mandatory clause-level citation and post-processing verification to guarantee 100% citation correctness. Under ideal LLM faithfulness assumptions, theoretical analysis verifies the framework's citation label correctness and conditional hallucination boundedness; furthermore, empirical evaluations on a real-world hierarchical regulatory dataset (RHPD) demonstrate that TH-GraphRAG achieves state-of-the-art performance with 94.6% answer accuracy, 100% citation precision, and 98.3% structural compliance, significantly outperforming 10 representative baselines ($p=0.002$) and establishing a trustworthy, deployable foundation for intelligent governance in high-stakes domains.

---

## uid: `arxiv:2607.16345v2`

- title: AEVAL: From Anecdotal to Deterministic Testing for Agentic Skill Workflows
- authors: Tejas Singh Anand, Yuet Ying Christina Wang, Wanting Jiang, Steve Masson, Tian Zheng, Bingjie Zhou
- affiliations: not stated
- posted: 2026-07-16
- source: arXiv
- link: https://arxiv.org/abs/2607.16345v2
- keyword hits: agentic, llm

### abstract

Modern agentic systems increasingly rely on skills: installable packages of natural language and code that teach an LLM agent to perform a domain task. As skill repositories grow, developers need automated quality signals on every change, yet evaluation today is largely anecdotal: a developer asks an agent to "try the skill," watches a demo, and forms a subjective impression. This yields neither reproducibility across runs nor comparability across versions, and scales poorly to marketplaces where one regression can silently break dozens of downstream workflows. We present AEVAL (Agentic Evaluation), a CI-integrated framework that replaces this practice with a deterministic, reproducible test pipeline for agentic skills. Every skill change triggers a test event: the skill runs against a developer declared evaluation contract inside an automated executor, emitting a structured, evidence grounded quality signal that downstream CI can route on. A key ingredient is a structural separation between executor and grader, preventing a subtle but pervasive failure mode: an agent that silently self-corrects during execution and then grades its own patched outputs as passing. Our contributions are: (i) a deterministic, change-triggered evaluation protocol with per-skill contracts and per-run artifact schemas; (ii) a formalization of self correction bias as a distinct failure mode of naive agentic evaluators; (iii) an executor/grader separation with a first-attempt grading rule and explicit self-correction tracking; and (iv) a tiered, grounded evidence fix suggestion scheme (LV1 causal, LV2 quality) posted as inline merge-request comments. Validated on real skills in a production agentic stack across multiple agent SDKs, AEVAL converts spurious 100% pass rates into reproducible first-attempt fail signals with an auditable record of every executor fix.

---
