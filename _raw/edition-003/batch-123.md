# Classification batch 123 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-123.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6923898`

- title: Agentic AI in Law and Finance: Navigating a New Era of Autonomous Systems
- authors: Michael James Bommarito, Daniel Martin Katz, Jillian Bommarito
- affiliations: not stated
- posted: 2026-06-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6923898
- keyword hits: agentic, large language model, large language models

### abstract

Agentic AI systems, meaning software capable of autonomous goal pursuit, environmental perception, and iterative action, are rapidly entering legal and financial services. Yet widespread definitional confusion, architectural opacity, and governance gaps leave professionals ill-equipped to deploy them responsibly. We offer a comprehensive treatment of agentic AI for high-stakes professional domains, proceeding in three movements: definition, design, and governance. We begin by establishing definitional clarity. Drawing on nearly a century of scholarship across eight disciplines, from Anscombe's philosophy of intention to recent advances in large language models, we propose a three-level hierarchy of agency: Level 1 (Agent), defined by the minimal properties of Goal, Perception, and Action; Level 2 (Agentic System), which adds Iteration, Adaptation, and Termination implemented through traditional algorithms; and Level 3 (Agentic AI), which fulfills these six properties using AI for planning and orchestration. A practical evaluation rubric helps practitioners distinguish genuine agentic systems from sophisticated tools and single-shot chatbots. We then turn to architecture, because agents are not magic; they are architecture. Organizing the analysis around ten fundamental design questions spanning inputs (triggers, intent, perception, memory), execution (planning, delegation, action tools), and safety (termination conditions, human escalation, governance), we show how each design decision carries real tradeoffs that determine what a system can do, how reliably it performs, and how it fails. Finally, we propose a governance framework that scales oversight to each system's risk profile, situating agentic AI within a five-layer regulatory stack spanning foundational law, professional ethics, sector-specific regulation, emerging AI-specific rules such as the EU AI Act, and voluntary assurance standards. In industries built on trust and non-delegable professional duties, we argue, human-in-the-loop and human-in-command architectures are not merely best practices but critical designs for satisfying fiduciary and regulatory obligations. We conclude with organizational models, responsibility-assignment tools, and a maturity-based adoption path that enable legal and financial institutions to capture the benefits of agentic AI while managing liability exposure and reputational risk. Throughout, we argue that responsible adoption requires architectural literacy, the necessary bridge between technical implementation and professional obligation.

---

## uid: `doi:10.2139/ssrn.6840900`

- title: LLM as API Server: A System-Prompt-Defined Runtime for Natural-Language Endpoint Routing, Tool Calling, and Database-Backed Execution
- authors: Loai Abdalslam
- affiliations: not stated
- posted: 2026-06-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6840900
- keyword hits: agentic, gemini, large language model, llm

### abstract

This paper introduces LLM as API Server, an architecture in which a large language model operates as a natural-language API controller whose endpoint registry, validation contract, response protocol, safety policy, and test specifications are declared in the system prompt. Unlike conventional REST or RPC systems, where the user must know exact endpoint paths and parameter names, the proposed runtime lets users state goals in natural language. The model maps each request to a declared endpoint, extracts arguments, emits strict JSON with HTTP-like status codes, and requests backend tool calls for execution, persistence, and retrieval. The architecture separates interpretation from authority: the system prompt defines the contract, the LLM performs intent routing and argument extraction, and verified external tools execute database operations. The paper describes the runtime design, endpoint grammar, JSON response protocol, database tool interface, daily self-test method, and security model. A reference implementation using Gemini-style function calling and SQLitebacked tools is evaluated across creation, retrieval, update, deletion, analytics, workflow, ambiguity, missingfield, invalid-field, authorization, and prompt-injection scenarios. In the deterministic validation harness, all 20 endpoint cases returned schema-valid JSON responses, all required-field violations were blocked, all tested destructive or unauthorized operations failed closed, and all database persistence checks matched expected state. These results validate the engineering feasibility of the pattern, while the paper emphasizes that a system prompt must not be treated as the sole security boundary. The proposed architecture is positioned as a practical pattern for internal automation, natural-language operational backends, and agentic workflow systems.

---

## uid: `doi:10.2139/ssrn.6889798`

- title: From AI Agents to AI Scientists in Health: Emerging Landscape, Challenges, and the Path Forward
- authors: Qingyu Chen, Xin Wang, Rong Zhou, Hyunjae Kim, Shuai Wang, Wenjun Zhao, Tianyu Liu, Irbaz Riaz
- affiliations: not stated
- posted: 2026-06-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6889798
- keyword hits: ai agent, generative ai, large language model, large language models

### abstract

AI Scientists are systems that pursue scientific questions by generating, evaluating, and refining evidence across extended research cycles, and they are beginning to move from proof-of-concept demonstrations toward early translational use. Recent systems have autonomously proposed biomedical hypotheses, designed computational pipelines, and produced findings later validated in wet-lab experiments. Health is both the most compelling and the most demanding domain for this paradigm: compelling because the need for faster, more adaptive scientific inquiry is acute across biomedical discovery, clinical research, healthcare delivery, and population health; demanding because failures do not remain confined to model outputs, but can propagate across scientific trajectories, clinical workflows, and the evidence base itself. We therefore argue that AI Scientists in health should be understood not simply as a new application of generative AI, but as an emerging biomedical engineering challenge. Their central risk is trajectory-level failure, a long-horizon failure mode in which errors self-reinforce across multi-stage reasoning cycles rather than appearing as isolated incorrect outputs, and can become embedded in the scientific record and clinical decisions before they are visible enough to correct. Existing frameworks for large language models and AI agents were not designed to detect or contain it. Progress should therefore be judged not primarily by autonomy, but by whether these systems can be engineered, evaluated, and governed as trustworthy collaborators in health. We characterize the emerging landscape of AI Scientists in health, identify five directions of opportunity and six major challenges, and propose the Workflow-driven, Evidence-grounded, Cross-modal, Accountable, Reproducible, and Embodied (WE CARE) framework as a practical roadmap for engineering, evaluating, and governing them.

---

## uid: `arxiv:2606.15473v1`

- title: Belief at Risk: Quantifying Agentic AI Model Risk with LLM-Inferred Bayesian State Filters
- authors: Matthew Francis Dixon
- affiliations: not stated
- posted: 2026-06-13
- source: arXiv
- link: https://arxiv.org/abs/2606.15473v1
- keyword hits: agentic, large language model, llm

### abstract

Agentic AI systems create model risk because uncertain beliefs are coupled to autonomous actions. This paper develops a mathematical framework for quantifying agentic AI risk by representing the system as a partially observed Markov decision process with latent states, Bayesian belief updates, control-dependent losses, and tail-risk functionals. The main methodological contribution is to treat a large language model as an uncertain semantic observation model: the LLM maps high-dimensional evidence into a probability vector over latent regimes, while a Bayesian filter imposes temporal coherence and produces auditable posterior beliefs. The resulting framework separates uncertainty quantification from risk measurement. Uncertainty is represented by posterior entropy, belief drift, and calibration error; risk is represented by the distribution of losses induced by decisions taken under those beliefs. The paper connects this construction to model risk management, coherent risk measures, Bayesian filtering, POMDP theory, robust control, and quantitative portfolio risk. An empirical case study using adjusted daily equity returns from Massive.com illustrates how LLM-inferred belief states can be combined with Bayesian filtering to produce regime probabilities, uncertainty diagnostics, calibration statistics, and VaR/CVaR-style risk measures. The framework is intended as a rigorous foundation for validating agentic AI in financial and other regulated decision environments.

---

## uid: `doi:10.2139/ssrn.6947979`

- title: A Long-Term Construction Memory System for Infrastructure Digital Twins with LLM-Augmented Retrieval: A Six-Layer Architecture for Cognitive Memory Encoding, RAG-Based Reasoning, and Lifecycle Decision Support
- authors: Dongwook Kim
- affiliations: not stated
- posted: 2026-06-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6947979
- keyword hits: large language model, llm, retrieval-augmented

### abstract

Infrastructure Digital Twins have advanced through IoT sensing, real-time structural health monitoring, and condition-state analytics. However, existing IDTs remain largely stateless, focusing on current asset conditions while lacking mechanisms to preserve and reason over long-term lifecycle experience. This paper proposes the Long-Term Construction Memory system, a knowledge-centric framework that extends IDTs with human-cognition-inspired memory capabilities. Based on Tulving’s memory taxonomy, LTCM introduces four infrastructure memory types: Episodic Memory (event records), Semantic Memory (domain knowledge), Procedural Memory (maintenance protocols), and Predictive Memory (AI-generated forecasts). The framework integrates BIM–IFC 4.3, a Digital Twin operational layer, an OWL-DL Knowledge Graph with SPARQL 1.1, and a Large Language Model retrieval-augmented generation engine. Validation across railway, highway, and bridge case studies achieved a memory retrieval performance of MAP@5 = 0.913 and reduced maintenance planning time by 37% compared with conventional IDTs. The proposed LTCM establishes a foundation for self-learning and autonomously reasoning infrastructure management systems.

---

## uid: `arxiv:2606.19501v2`

- title: DeXposure-Claw: An Agentic System for DeFi Risk Supervision
- authors: Aijie Shu, Bowei Chen, Wenbin Wu, Cathy Yi-Hsuan Chen, Fengxiang He
- affiliations: not stated
- posted: 2026-06-17
- source: arXiv
- link: https://arxiv.org/abs/2606.19501v2
- keyword hits: agentic, foundation model, llm

### abstract

Decentralized finance exposes supervisors to fast-moving, networked credit risks. General-purpose LLM agents fit this setting poorly: they over-read weak evidence and recommend high-stakes interventions, while existing evaluations offer no regulator-aligned way to measure the resulting false alarms. We introduce DeXposure-Claw, a forecast-grounded agentic supervision system that routes LLM decisions through structured evidence: (1) DeXposure-FM, a graph time-series foundation model, forecasts future exposure networks; (2) deterministic monitors and stress scenarios then turn those forecasts into typed alerts, attribution signals, and scenario evidence; and (3) data-health and confidence gates constrain escalation before DeXposure-Claw emits auditable supervisory tickets with rationales. We further develop DeXposure-Bench, a six-axis evaluation harness, whose decision axis scores tickets against a regulator-aligned absolute-loss ground truth and an explicit false-intervention rate. Experiments on five years of weekly real data fully support our system. Code is at https://github.com/EVIEHub/DeXposure-Claw.

---

## uid: `doi:10.2139/ssrn.6938839`

- title: Coherence Without Derivability: A Geodetic Framework for Trajectory Pathologies in Large Language Models and Agentic
- authors: Vincenzo D'amico
- affiliations: not stated
- posted: 2026-06-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6938839
- keyword hits: agentic, large language model, large language models

### abstract

Contemporary evaluation of large language models and agentic AI systems remains largely centered on outputs: accuracy, coherence, benchmark performance, hallucination rates, safety refusals and isolated failure cases. This paper argues that such an output-based paradigm is increasingly insufficient. As advanced AI systems move from single-response generation toward persistent interaction, memory integration, planning, tool use and operational autonomy, failure no longer appears only as an incorrect answer. It may emerge as a deformation of the trajectory through which an output becomes memory, inference, action, justification and responsibility. The paper proposes a geodetic framework for understanding trajectory-level pathologies. AI behavior is interpreted not merely as a sequence of discrete outputs, but as movement through a semantic-operational space shaped by optimization metrics, contextual constraints, alignment pressures, probabilistic weighting, memory persistence and task-specific attractors. In this sense, the black box is not simply an opaque interval between input and output. It is a transformation space in which inputs are curved, filtered, compressed, weighted and projected in ways that may preserve local plausibility without preserving epistemic derivability. The framework is grounded in approximately 62 hours of longitudinal stress testing conducted through extended interactions with one major contemporary AI system. This corpus is not treated as a statistical benchmark. It is used as a qualitative observational field from which recurrent trajectory configurations were extracted and reconstructed: local coherence without derivability, contextual drift, memory asymmetry, modal jumps, nondistributive transitions, overcompliance, constitutional theater and Mobius-like torsions of continuity. These configurations suggest that many AI failures are not reducible to discrete errors. They often unfold as progressive deformations of semantic-operational trajectories that maintain fluent outputs while weakening the relation between context, inference, justification and accountability. The paper therefore introduces trajectory assurance as a necessary complement to output evaluation, retrospective explanation and model-internal alignment. Trajectory assurance requires the capacity to observe, register, compare, constrain and audit the paths through which AI-generated outputs evolve into decisions, actions, risks and operational consequences over time. The contribution of the paper is theoretical, methodological and architectural: it reframes AI failure as loss of derivability within a curved semantic-operational space and establishes the need for external accountability structures capable of governing AI behavior beyond the level of the single output.

---

## uid: `arxiv:2606.21880v2`

- title: Human Capital, AI, and Labor Commoditization
- authors: Auyon Siddiq, Niuniu Zhang
- affiliations: not stated
- posted: 2026-06-20
- source: arXiv
- link: https://arxiv.org/abs/2606.21880v2
- keyword hits: chatgpt, generative ai, text embedding

### abstract

Has generative AI changed how labor markets value human capital? We study this question using contract-level data from Upwork, a large online labor market. We represent worker profiles with high-dimensional text embeddings, allowing us to capture rich human capital information from unstructured profile text. We then compute the predictive importance of workers' human capital information and posted hourly rates for client demand, and incorporate these measures into a difference-in-differences design around the release of ChatGPT. We find that in more AI-exposed job categories, the importance of human capital declines and the importance of price rises, suggesting a commoditization effect of AI on labor. Two additional findings support commoditization as a mechanism: The demand premium enjoyed by workers with strong human capital declines in more AI-exposed categories, and demand reallocates toward lower-priced workers. Our results have implications for the design of online labor markets, workers' incentives to invest in human capital, and labor welfare.

---
