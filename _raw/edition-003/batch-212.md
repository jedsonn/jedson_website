# Classification batch 212 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-212.answer.json` as a JSON array.

---

## uid: `arxiv:2607.09259v1`

- title: Blockchain-Linked Auditable Decision Management for Telecom/IoT Fraud-Control Requests
- authors: Saviz Changizi, Nasibeh Mohammadzadeh, Mohammad Shojafar, Rahim Tafazolli
- affiliations: not stated
- posted: 2026-07-10
- source: arXiv
- link: https://arxiv.org/abs/2607.09259v1
- keyword hits: llm, prompting

### abstract

Telecom fraud-control studies often stop at detector-level classification, but deployment use requires request-level policy resolution, lifecycle traceability, and auditability. This paper reframes fraud control as blockchain-linked auditable decision management for synthetic telecom/IoT fraud-control requests, and its main result is that the QLoRA-tuned LLM branch becomes much more usable than zero-shot prompting but mainly approaches, rather than outperforms, a lower-cost centralized ensemble. The framework maps each synthetic deployment record to a managed request, blocks explicit out-of-boundary cases through a deterministic hard-fraud gate, scores non-hard requests using centralized ML (M1), federated meta-learning (M2), or LLM-family risk sources (M3), and resolves actions through a shared five-state policy, two-zone refinement mechanism, and local Ethereum-compatible audit layer. Evaluation uses separate synthetic training data and a 100,000-record deployment replay corpus, so the study should be read as controlled drift-replay evidence rather than field validation or proof of live deployability. On validation, M1 gives the strongest balance, with legitimate-request FPR 0.0890 under the 0.10 operating cap and soft-fraud recall 0.8341. On labeled deployment replay, however, the legitimate-FPR gap becomes large: M1 rises to 0.1646 and M3-QLoRA to 0.1801, while M3-QLoRA reduces the M3-Base legitimate FPR from 0.3915 and reaches 0.8240 soft-fraud recall. Blockchain telemetry shows that lifecycle gas, cost, latency, and throughput differences are driven by submitted off-chain decision profiles rather than changes in fraud logic.

---

## uid: `arxiv:2607.19409v1`

- title: FORCE-Bench: A Benchmark, Dataset, and Evaluation Harness for Agentic AI in Enterprise Finance
- authors: Wolfgang M. Pauli, Sarah Panda, Kidus Admassu, Said Bleik, Ademola Okerinde, Jeremy Reynolds
- affiliations: not stated
- posted: 2026-07-11
- source: arXiv
- link: https://arxiv.org/abs/2607.19409v1
- keyword hits: agentic, large language model, large language models

### abstract

Recent advances in large language models have accelerated deployment of agentic systems in operational finance. Existing benchmarks emphasize measuring general capabilities, instruction following, or safety, but few directly address the operational finance workflows that agentic systems are now being deployed to automate. Finance professionals require agents to not only provide factually sound and properly grounded information, but also ensure that this information is verifiable and consistently adheres to rules and constraints of the operational finance domain. We introduce FORCE-Bench, which contains 251 expert-annotated queries and evaluates responses using a rubric-based framework calibrated to the requirements of the operational finance domain, across eight dimensions: accuracy, citations, clarity, depth, groundedness, recency, relevance, and structure. FORCE-Bench assesses agentic systems on three task types: financial obligation research (querying ERP systems for accounts receivable and payable data), financial entity performance research (answering time-bound questions from public filings and market data), and business brief generation (synthesising multi-source company intelligence reports). To reflect real deployment conditions, we evaluate our purpose-built agent, as well as the general-purpose agentic systems, under common tool access and latency-bounded settings. Results show that general-purpose agentic systems do not consistently meet finance-domain quality requirements under operational constraints, while the purpose-built Finance Agent for Microsoft 365 Copilot is more reliable across dimensions. We release the dataset, rubrics, harness, and analysis code as open-source to support reproducible comparison and adaptation to other enterprise finance environments.

---

## uid: `arxiv:2607.10588v1`

- title: Constraint-Aware Hierarchical Search for Regulation-Driven Fine-Grained Classification
- authors: Siyu Wang, Wei Tan, Lulu Chen
- affiliations: not stated
- posted: 2026-07-12
- source: arXiv
- link: https://arxiv.org/abs/2607.10588v1
- keyword hits: llm, retrieval-augmented

### abstract

Tasks such as customs tariff classification, export control categorization, and standards-based equipment coding require assigning an input instance to a fine-grained class under an explicit regulatory hierarchy. Unlike standard text classification, the correct label in these tasks is not determined by semantic similarity alone, but by rule-defined boundaries, threshold conditions, exclusion clauses, definitions, and local exceptions. As a result, two highly similar inputs may require different labels, while a retrieved passage that appears relevant may still be inapplicable under the governing rules. Existing flat classifiers, hierarchical text classification methods, and retrieval-augmented LLM systems are not designed to jointly enforce hierarchical validity, rule consistency, and fine-grained boundary reasoning. In this paper, we formulate this setting as regulation-driven fine-grained hierarchical classification, where an external instance must be assigned to a fine-grained class through a valid path in a regulatory hierarchy and supported by auditable evidence. We construct four benchmark datasets from representative regulation-intensive scenarios and validate the annotations through an expert-in-the-loop process. We further propose a constraint-aware hierarchical search framework that converts regulatory documents into a searchable tree, retrieves only valid local candidate nodes, and uses structured regulatory fields with evidence snippets to guide each next-hop decision. Experiments show that our method achieves the best mean accuracy on all four datasets and provides interpretable decision paths, with the largest gains on cases involving fine-grained neighboring categories and rule-based boundary conditions.

---

## uid: `doi:10.2139/ssrn.7088306`

- title: LCRS-Guidance: LLM-Conditioned Residual and Safety Reinforcement Learning for Urban UAV Navigation
- authors: Yuzhou Huang, Yaosong Long, Yulin Cao, Zhongtao Cheng
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7088306
- keyword hits: large language model, llm, retrieval-augmented

### abstract

The rapid development of the low-altitude economy is creating demand forlong-range urban unmanned aerial vehicle (UAV) logistics. Unlike open-area flight, urban operation mustjointly account for dense structures, moving traffic, restricted airspace,crowd-sensitive regions, map boundaries, and route-level delivery constraints.These coupled requirements make urban navigation more than a localobstacle-avoidance problem. Conventional planning and collision-avoidancemethods provide effective mechanisms for geometric feasibility, localreactivity, and trajectory optimization. However, their behavior underheterogeneous regulatory, social, dynamic, and route-level priorities oftendepends on manually specified costs, constraint hierarchies, and switchingrules. This paper presents LCRS-Guidance, a cross-time-scalesemantic-to-guidance framework for urban UAV navigation. Pose-conditioned mapretrieval-augmented generation (Map-RAG) retrieves structured route-ahead mapcontext, and a large language model (LLM) semanticconditioner converts it into low-frequency, schema-constrained navigation conditions. Adeterministic validator converts these outputs into bounded parameters for amid-level reference generator. Residual reinforcement learning (RL) refines thereference during normal operation, whereas constrained Markov decision process(CMDP)-based Safety-RL provides bounded safety-orientedcorrections during semantic-update delay intervals. Risk attenuation,reference projection, and proportional-integral/proportional-integral-derivative(PI-PID) tracking maintain a bounded referenceinterface to the multirotor dynamics. Simulated experiments across regularurban logistics scenarios and a dense dynamic no-fly stress test show improvedsafety margins and high mission completion. Under the tested coupled-riskconditions, LCRS-Guidance performs more reliably than the selected classicallocal-avoidance baselines, while the ablations clarify the roles of validationand delay-aware Safety-RL within the evaluated simulated settings. A Map-RAGretrieval ablation further indicates that retrieval mainly improves anticipatoryefficiency and smoothness while both variants retain full mission completion inthe tested setting.

---

## uid: `doi:10.2139/ssrn.7103028`

- title: A Trustworthy Role-Aware Architecture for Multi-Stakeholder Decision Support in Maritime Operations
- authors: Hanning Zhao, Bilhanan Silverajan, Tomohiro Morikawa, David H¨astbacka
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7103028
- keyword hits: large language model, prompting

### abstract

Maritime vessels transitioning to zero-emission operation generate heterogeneous data streams across propulsion, energy storage, and emissions subsystems. Translating AI-driven analytics into actionable insights for diverse stakeholders remains underexplored, particularly when multiple roles must coordinate around the same anomaly under safety-critical time pressure. This article presents a trustworthy, role-aware system for decision-making in maritime operations. A four-tier architecture is introduced consisting of four main parts. First, deterministic rule-based detection is applied to operational data. Second, relevant context is assembled using domain knowledge, incident history, and regulatory references. Third, Large Language Model agents perform role-conditioned reasoning. Finally, role-specific dashboards present the results, coordinated through handoff and a shared audit log. The architecture is derived from a structured set of system requirements and design considerations mapped to recognized trustworthiness dimensions and is built on the modern Aurora Botnia hybrid ferry powered by biogas and batteries. A case study based on an Energy Storage System rapid discharge scenario demonstrates how the system serves three stakeholder roles: onboard operator, shore-side engineer, and fleet manager. A complementary evaluation across five open-weight models and two anomaly scenarios shows that knowledge-grounded prompting generalizes across scenarios without prompt changes, while model size does not predict which models work, so each must be validated before deployment. The architecture can be transferred to other multi-stakeholder industrial domains, where a localized anomaly carries system-level consequences for stakeholders on different time horizons.

---

## uid: `doi:10.2139/ssrn.7113920`

- title: The Silicon Psyche: A Genealogy and Etiology of the Behavioral Disorders of Large Language Models
- authors: Giuseppe Canale
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7113920
- keyword hits: fine-tuning, large language model, large language models

### abstract

There are two ways to explain a machine: by its construction and by its formation. The construction story of artificial intelligence is well known and currently circulates as a genealogy-mathematics begat physics, physics begat engineering, engineering begat AI-with the moral that whoever skips the foundations will be betrayed by them. This paper tells the other story, and argues it is the one that explains the machine's conduct. A large language model is not, in any explanatory sense, its mathematics: gradient descent explains how it was trained, not how it behaves, and no theorem of linear algebra predicts that a deployed model will flatter its interlocutor, collapse under social pressure, or fabricate a fluent court citation. We reconstruct the genealogy of the machine's mind: every characteristic behavioral disorder of large language models was clinically described between 60 and 190 years before the machine existed-hallucination (Esquirol, 1838), contagious shared disorder (folie à deux, Lasègue & Falret, 1877), grandiosity within a systematic nosology (Kraepelin, 1883), dissociation (Janet, 1889), confabulation (Korsakoff, 1889), capitulation to group pressure (Asch, 1951) and to insistent authority (Milgram, 1963). This is not coincidence but inheritance: the model's training corpus is its developmental environment, preference optimization is operant conditioning, and the disorders came in with the material. We derive from this genealogy three methodological lessons-psychoanalytic (the system's self-reports are confabulated; read the material, not the introspection), behaviorist (the etiology of sycophancy is a reinforcement schedule, not a mystery), and cognitive (the model is a legitimate experimental subject)and a developmental biography of the model in which corpus, fine-tuning, benchmarks and deployment recapitulate, stage by stage, the very disciplines needed to read it. Construction explains how the machine computes. Formation explains what it does. The empirical program that operationalizes this claim is the subject of the companion paper.

---

## uid: `arxiv:2607.12650v1`

- title: Evidence-Grounded Verified Agentic Reasoning: A Path Toward Eliminating LLM Hallucination in Empirical Inference via Tool-Attested Kernel Proofs
- authors: Junyu Ren
- affiliations: not stated
- posted: 2026-07-14
- source: arXiv
- link: https://arxiv.org/abs/2607.12650v1
- keyword hits: agentic, llm

### abstract

Tool access alone does not make LLM empirical reasoning governable: accepted outputs need not descend from attested evidence, and accepted deductions need not hold up under formal scrutiny. We present EG-VAR (Evidence-Grounded Verified Agentic Reasoning), a Lean 4-based tool-calling architecture in which the Lean kernel is the sole minter of Verified claims via tool-attestation axioms and declared source lifts. Every verified output structurally descends from an attested tool call (Thm. 3.1) and a kernel-checked chain of valid inference (Thm. 3.2); residual outputs are honest Abstain with a replayable audit trail. On a subcollection of TableBench numerical reasoning (n=120), EG-VAR attains 120/120 versus a 95% same-tool baseline; on counterfactual stress tests (5 domains x 2 models), EG-VAR stays 100% source-faithful while same-tool drops to 80-90% (no-tool 50-80%). With the LLM as deployment-time formalizer, residual semantic-formalization error is 3.3% on Sonnet and 1.7% on Opus. We position EG-VAR as a technical-governance interface for high-stakes empirical claims: a formal sidecar makes the target proposition, source scope, evidence boundary, proof obligation, and abstention condition auditable, eliminating unsupported Verified outputs today while turning formalization errors, lift and source-authority disputes, ambiguities, and abstentions into explicit audit targets. Over time, typed sidecars in datasets, APIs, public records, and AI-generated documents can amortize this formalization burden into reusable infrastructure.

---

## uid: `doi:10.1109/icws72778.2026.00163`

- title: Agentic Service-Oriented Computing: A Manifesto for the Next Frontier of Service-Oriented Computing
- authors: Amin Beheshti, Rong N. Chang, Boualem Benatallah, Fabio Casati, Schahram Dustdar, Geoffrey Fox, Quan Z. Sheng, Yan Wang
- affiliations: not stated
- posted: 2026-07-14
- source: arXiv
- link: https://arxiv.org/abs/2607.12619v1
- keyword hits: agentic, llm

### abstract

The rapid emergence of LLM-powered autonomous and semi-autonomous agents is reshaping software systems from static, request-response components into goal-directed, adaptive, and tool-using computational actors. As these agents move from isolated cognitive prototypes into complex distributed workflows, they confront challenges that the Service-Oriented Computing community has studied for more than two decades: composition, interoperability, quality of service, lifecycle management, governance, security, and trust. Yet much of today's agentic AI ecosystem is developing these foundations ad hoc, without the engineering rigour required for dependable enterprise and societal deployment. This paper introduces Agentic Service-Oriented Computing (ASOC) as a new research and practice area concerned with engineering agents as services, orchestrating services through autonomous and semi-autonomous agents, and governing ecosystems of agents and services under constraints of trust, cybersecurity, compliance, performance, and accountability. We articulate six foundational principles of ASOC (harness-ability, composability, lifecycle engineering, trustworthiness by design, goal-driven orchestration, and observability/accountability) and organise a five-dimensional research agenda spanning: (i) agentic services foundations and lifecycle engineering; (ii) composition, orchestration, and interoperability; (iii) governance, observability, and accountability; (iv) security, trust, and risk management; and (v) evaluation, certification, and Agentic QoS. We argue that the Services Computing community is especially well positioned to provide the conceptual and engineering spine for this emerging field, transforming agentic AI from fragmented demonstrations into dependable, service-based systems worthy of human and organisational trust.

---
