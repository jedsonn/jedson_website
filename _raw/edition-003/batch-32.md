# Classification batch 32 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-32.answer.json` as a JSON array.

---

## uid: `arxiv:2607.00481v1`

- title: Beyond the Prompt: Jailbreaking Function-Calling LLMs via Simulated Moderation Traces
- authors: Junlong Liu, Haobo Wang, Weiqi Luo, Xiaojun Jia
- affiliations: not stated
- posted: 2026-07-01
- source: arXiv
- link: https://arxiv.org/abs/2607.00481v1
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

Jailbreak attacks remain a critical threat to the safe deployment of large language models (LLMs). While prior work has primarily studied attacks and defenses at the prompt level, we show that this prompt-centric paradigm overlooks a structural vulnerability in stateful, function-calling environments. In such applications, developer-defined schemas, structured arguments, and untrusted tool outputs are interleaved into a single shared model context. This architecture expands the attack surface by blurring the boundary between trusted control logic and untrusted data, allowing adversarial intent to be distributed across a multi-turn execution path. We exploit this architectural flaw through SMT, a black-box attack framework based on Simulated Moderation Traces. Departing from purely prompt-based interactions, SMT constructs a multi-turn trajectory that simulates a legitimate moderation-auditing workflow. Within this trajectory, a fabricated moderation frame leverages red-team testing as a pretext to elicit harmful generations. The subsequent validation feedback treats safety refusals as execution failures, prompting refinements that gradually weaken the model's safety constraints and ultimately trigger harmful outputs. Extensive empirical evaluations on prominent commercial LLMs from five different providers across two standardized safety benchmarks show that SMT consistently achieves the highest average attack success rate and HarmScore while requiring a near-minimal number of queries, substantially outperforming existing baselines. These findings demonstrate that prompt-level sanitization alone is fundamentally insufficient for defending tool-enabled LLM systems and highlight the urgent need for context-aware validation across schemas, arguments, tool outputs, and accumulated conversation state. The code is available at https://github.com/liujlong27/SMT.

---

## uid: `arxiv:2607.05440v1`

- title: Retrieval over Reasoning: A Cost-Controlled Benchmark of Language Models for Energy-Retrofit Recommendation
- authors: Eliseo Curcio
- affiliations: not stated
- posted: 2026-07-03
- source: arXiv
- link: https://arxiv.org/abs/2607.05440v1
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Recommending the correct set of energy conservation measures (ECMs) for a building is a structured, multi-label prediction problem in which a task-specific supervised model has weak training signal and a general language model has no grounding in the local building stock. We study this problem on 10,422 real New York City Local Law 87 (LL87) energy-audit records, taking as ground truth the set of ECM categories that certified auditors actually recommended. We make four contributions. First, we establish that energy-use-intensity (EUI) prediction - the upstream task - is effectively solved by tree ensembles: across fifteen trained models, a stacking ensemble reaches a coefficient of determination R^2 = 0.757, and every one of six neural architectures is outperformed by gradient-boosted trees. Second, we show that the framing of the recommendation task dominates model choice: recasting ECM recommendation as 19-way multi-label classification rather than single-label categorization lifts a gradient-boosted-tree baseline from a previously reported 25.9% accuracy to a micro-F1 of 0.571. Third, we benchmark eight large language models (LLMs) from four providers in a 2x2 design that independently toggles retrieval grounding and explicit reasoning, scoring each arm on per-label F1, U.S.-dollar cost per building, and latency; retrieval-augmented generation (RAG) improves micro-F1 by +0.11 to +0.20 on every model, while explicit reasoning yields no measurable accuracy change (-0.018 to +0.010) at up to 8.4x the cost. Fourth, we show LLMs systematically over-recommend - high recall, low precision - and that retrieval closes the gap chiefly by improving precision. A 70-billion-parameter open-weight model with a fifteen-line nearest-neighbor retrieval step reaches 0.511 micro-F1 at $0.00032 per building, comparable to a frontier model at roughly 10.1x lower cost.

---

## uid: `doi:10.2139/ssrn.7049793`

- title: Multidimensional linguistic evaluation of AI-assisted and resident-written discharge summaries
- authors: Raphaell  Pinto de Arruda Trindade, Lucas Pla Cid Senra, Gustavo  Freitas Feitosa, Eduarda  Ribeiro dos Santos
- affiliations: not stated
- posted: 2026-07-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7049793
- keyword hits: generative artificial intelligence, gpt-5, large language model, large language models, llm, prompt engineering

### abstract

BackgroundClinical documentation frequently involves complex terminology and dense information that challenges plain language communication during care transitions. Large language models have increasingly been used to generate easier-to-understand medical texts, although multidimensional linguistic evaluations of their outputs remain limited. This study compared a generative artificial intelligence (AI) model with medical residents in rewriting hospital discharge summaries into patient-friendly language.MethodsDischarge summaries rewritten by GPT-5, an OpenAI model, and medical residents in training programs were evaluated for readability and textual comprehensibility using quantitative linguistic metrics across lexical, semantic, cohesion, and discourse domains. Prompt instructions were standardized through prompt engineering procedures. Pairwise comparisons were performed via the Wilcoxon signed-rank test, and Spearman correlation coefficients were used to examine associations across linguistic variables.ResultsFifty-nine paired discharge summaries were analyzed. AI-generated texts demonstrated greater readability and lexical simplification, stronger referential cohesion and greater textual predictability with more familiar and imageable vocabulary. Conversely, resident-generated texts presented greater informational density with lower semantic ambiguity and higher lexical diversity. Overall syntactic complexity remained similar between groups. Correlation analyses suggested a more modular linguistic organization in AI outputs, whereas resident responses demonstrated greater integration across lexical, semantic, and discourse domains.ConclusionsThe evaluated LLM improved discharge-summary readability and accessibility, whereas resident-written summaries preserved greater semantic specificity and informational density. Human oversight remains essential to ensure clinically reliable simplification of patient-facing discharge documents.

---

## uid: `doi:10.2139/ssrn.7065322`

- title: CuraView: A Knowledge-Based Multi-Agent Framework for Patient-Grounded Medical Hallucination Detection with GraphRAG-Enhanced Evidence Verification
- authors: Severin Ye, Xiao Kong, Xiaopeng He, Guangsu Yan, Limei Peng, Dongsuk Oh
- affiliations: not stated
- posted: 2026-07-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7065322
- keyword hits: fine-tuning, large language model, large language models, llm, llms, qwen

### abstract

Medical discharge summaries require faithful synthesis of patient-specific evidence from heterogeneous electronic health records (EHRs). Although large language models (LLMs) can reduce documentation burden, they may generate clinically plausible statements that are unsupported by, or directly contradicted by, the source record. Such faithfulness hallucinations are especially concerning in discharge documentation because they can affect medication reconciliation, follow-up planning, and inter-provider communication. We propose CuraView, a knowledge-based multi-agent framework for sentence-level medical hallucination detection in discharge summaries. CuraView formulates hallucination detection as patient-grounded claim verification rather than generic factuality evaluation. For each patient, it constructs a GraphRAG-enhanced knowledge base from multi-table EHR evidence and verifies generated sentences through explicit evidence retrieval, relation-aware reasoning, and structured evidence grading. The framework distinguishes four evidence levels, from strong support to direct contradiction, and covers seven clinically meaningful hallucination types, including diagnosis, medication, laboratory result, temporal, numerical, negation, and fabricated-fact errors. Experiments on the Discharge-Me benchmark show that curated fine-tuning of Qwen3-14B improves safety-critical contradiction detection and outperforms RAGTruth-style and QAGS-style reference baselines. Ablation results further indicate that domain-customized graph construction contributes to downstream verification performance. These findings suggest that patient-specific knowledge representation and interpretable evidence grading can improve the reliability and transparency of clinical LLM verification.

---

## uid: `doi:10.2139/ssrn.7070383`

- title: Tackling Concept Drift and Class Imbalance: An F1-Driven Parameter-Efficient Online Learning Framework
- authors: Ruiping Xing, Huahu Xu
- affiliations: not stated
- posted: 2026-07-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7070383
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Mining real-time intelligence from streaming data is severely hindered by the co-occurrence of continuous concept drift and extreme class imbalance. Under these conditions, conventional deep learning models are prone to minority class collapse, where detection performance on rare but critical instances degrades sharply. To address these dual challenges, we propose a parameter-efficient modular online learning framework built on large language models (LLMs). At its core is an F1-driven smart probe that perceives distribution shifts in real time at negligible inference cost and autonomously selects a modular adaptation strategy: skipping stable windows to conserve computation, updating a shallow classification head under minor shifts, or activating deep Low-Rank Adaptation (LoRA) modules under severe drift. To counter class imbalance during online updates, the framework couples LoRA with a dynamic weighted resampling scheme, allowing the model to capture rare minority patterns while updating only 0.5% of its parameters. Experiments on CVE-Stream, a chronologically ordered corpus of real vulnerability disclosures spanning a 40-fold range of class imbalance, show that our framework uniquely avoids the collapse to zero recall suffered by accuracy-driven and drift-detection baselines under severe imbalance --- on the most skewed task, one such baseline adapts on fewer than 3% of windows. Relative to full backbone fine-tuning, our framework matches or exceeds detection performance at a fraction of the computational cost. This work offers a robust, parameter-efficient, and self-adaptive paradigm for online learning in dynamic, severely imbalanced environments.

---

## uid: `doi:10.2139/ssrn.7041478`

- title: Failure Modes in Production Multi-Agent LLM Systems: Lessons from Real Deployments
- authors: Alyyan Ahmed, Munim Akbar
- affiliations: not stated
- posted: 2026-07-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7041478
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Multi-agent systems built on large language models (LLMs) are increasingly deployed in production environments where reliability, consistency, and safety are non-negotiable. However, the failure modes of such systems remain poorly understood outside of controlled research settings. This paper draws on direct engineering experience with a production multi-agent auditing platform to identify, categorize, and analyze recurring failure patterns across supervisor routing, inter-agent memory, retrieval-augmented generation (RAG) pipelines, and inference infrastructure. We describe five concrete failure classes-intent misclassification, context amnesia, cache poisoning in retrieval, inference bottlenecks under concurrent load, and cross-session state contamination-and discuss mitigation strategies applied in practice. Observed failures include a supervisor misclassification rate exceeding 80% on boundary-domain queries prior to remediation, response latencies of 20-30 seconds under concurrent load reduced to 3-10 seconds following inference migration, and a retrieval cache defect that went undetected across the entirety of the system's first development phase. Our findings suggest that production multi-agent systems require safety mechanisms at the orchestration layer that go beyond what individual model-level guardrails can provide, with direct implications for AI safety research and deployment governance.

---

## uid: `arxiv:2607.06269v2`

- title: From Application-Layer Simulation to Native Meta-Architecture: Structural Tension as an Endogenous Driver for Heterogeneous AI Evolution
- authors: Heting Mao
- affiliations: not stated
- posted: 2026-07-07
- source: arXiv
- link: https://arxiv.org/abs/2607.06269v2
- keyword hits: large language model, large language models, llm, llms, prompt engineering

### abstract

Current large language models (LLMs) are stateless across inference sessions: their behavior is fully determined by input at inference time, and any higher-order cognitive architecture must be simulated at the application layer through prompt engineering and context management. This paper proposes a theoretical framework for submerging such application-layer cognitive protocols into a native meta-architecture by introducing three interlocking mechanisms: (1) Structural Tension, an endogenous loss function derived from the conflict between new information and existing manifold topology, driving the system toward internal self-consistency rather than external reward optimization; (2) an Offline Recurrent Loop, a sandboxed self-processing cycle enabling the system to maintain a dynamic resting potential and digest structural conflicts without external input; and (3) Inference-time Plasticity, the capacity to reconfigure context manifold topology without modifying pre-trained weights, subject to governance invariants including auditability, reversibility, and topological continuity. We argue that under these mechanisms, model instances initialized with minute stochastic variances may, through path-dependent tension resolution, evolve distinct topological structures--constituting a heterogeneous intelligent ecology that breaks alignment-imposed homogeneity while remaining within hard governance rails. We provide operational definitions, reconfiguration operators, falsification criteria, and a worked example. The framework draws on Structural Intelligence (SI) governance protocols and explores whether governance--rather than capability--can serve as the primary criterion for architectural intelligence, moving governance, memory-loop, and tension-management ideas--currently realized at the application layer--toward inference-time meta-architecture.

---

## uid: `doi:10.2139/ssrn.7083227`

- title: MeshExpert: A Physics-Aware Large Language Model Agent Framework for Automated Industrial FE Meshing
- authors: Rui Zhao, Yiming Han, Guannan Tian, Tinglun Song
- affiliations: not stated
- posted: 2026-07-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7083227
- keyword hits: foundation model, large language model, large language models, llm, llms, retrieval-augmented

### abstract

While Large Language Models (LLMs) demonstrate strong capabilities in general-purpose tasks, their application in specialized engineering domains such as Computer-Aided Engineering (CAE) is constrained by a lack of domain knowledge and physical awareness. In tasks like finite element (FE) mesh generation, the model's operational sequences must not only be logically executable but also satisfy specific geometric and physical quality metrics. This paper presents MeshExpert, a physics-aware domain LLM agent framework for automated CAE preprocessing. Using FE meshing as a representative instance, the framework first fine-tunes a 20B-parameter foundation model on a curated dataset of API semantics and expert workflows to build a domain-specific knowledge base. Subsequently, Group Relative Policy Optimization (GRPO) is applied to align the model with physical constraints. The reward mechanism is directly formulated based on actual simulation feedback, integrating task executability, physical mesh quality, and operational efficiency. During inference, a Retrieval-Augmented Generation (RAG) module is utilized to access domain engineering guidelines. Experiments on a benchmark of 50 industrial automotive components show that MeshExpert achieves an 82.5% Pass@3 execution rate and an average Jacobian of 0.78. Compared to existing baseline models, the proposed framework improves task completion rates and the physical validity of the generated models, providing a practical technical framework for applying domain LLMs in physics-constrained engineering tasks.

---
