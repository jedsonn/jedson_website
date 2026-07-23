# Classification batch 126 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-126.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7083993`

- title: Reproducible LLM-Based Measurement Depends on the Serving Stack
- authors: Hsiang-Chieh (Alex) Yang
- affiliations: not stated
- posted: 2026-07-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7083993
- keyword hits: large language model, llm, prompting

### abstract

Researchers in finance and accounting increasingly build measures by prompting a large language model (LLM) and recording its answer. Such a measure is reproducible only if re-running the model returns the same response. The common safeguard, forcing the model to take its most likely answer instead of sampling at random, does not guarantee reproducibility. To find where reproducibility holds, I apply three prompts to 500 earnings-call transcripts and re-run each ten times across 36 model-and-stack combinations. Even with that safeguard in place, reproducibility depends on the serving stack, the software and hardware that run the model. Self-hosted standard open-weight models reproduce their own output on 96.6 to 100 percent of cases. But two computers loading identical weights agree only 92.2 percent of the time, so even the hardware matters. The same open model reproduces 97.5 percent of the time at one cloud provider and 64.5 percent at another, and closed models fall to 9.1 percent. This can change what a study concludes. In a long-short portfolio, the average return survives a change of stack, but the cloud-served model reverses its predicted direction for a fifth of firms and does not always reproduce its own forecast. I provide a recipe for running the model so it reproduces, and an archive of each model call that lets another researcher verify a self-hosted measure exactly. Studies should report the serving stack and prefer models they can run themselves.

---

## uid: `arxiv:2607.08028v1`

- title: From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents
- authors: Joongho Ahn, Moonsoo Kim
- affiliations: not stated
- posted: 2026-07-09
- source: arXiv
- link: https://arxiv.org/abs/2607.08028v1
- keyword hits: large language model, llm, prompting

### abstract

Enterprise large language model (LLM) applications often begin as prototypes whose behavior is carried by prompts and retrieval context. Productization adds requirements for source boundaries, entity routing, answer contracts, and reproducible traces. We present a harness-engineering approach that reconstructs this pattern into a traceable, auditable LLM-agent architecture: deterministic behavior moves into code, manifests, schemas, and validation artifacts around a replaceable composition boundary, while source-backed claims remain the authority for runtime answers. We instantiate it on a public-data slice of five Korean corporate groups (25 listed companies) and evaluate three research questions. (1) The harness preserves its source-grounding, entity-routing, trace, output-hygiene, and recommendation-language contracts across the fixed validation scenarios; a fault-injection control confirms the validators flag deliberately broken contracts. (2) The checks the harness enforces held under model substitution: across three hosted models, they passed on all 270 composition-boundary runs; failures were confined to the model-composed side and were caught and recorded. (3) The code-owned guarantees are load-bearing, not reproducible by prompting alone: holding the model fixed and varying only the enforcement layer, prompt instructions alone let recommendation-language and internal-trace-leakage violations reach the reader, which the harness blocks entirely. A bolt-on external guardrail prevents such violations too but over-refuses, dropping utility to 88/120 where the harness preserves full utility (120/120); in this ablation, only code-owned enforcement preserves both safety and utility. The result is a reusable engineering pattern for turning exploratory prototypes into auditable applications with versioned source, control, and validation artifacts.

---

## uid: `arxiv:2607.10522v1`

- title: Towards Autonomous and Auditable Medical Imaging Model Development
- authors: Shengyuan Liu, Jia-Xuan Jiang, Boyun Zheng, Cheng Wang, Zipei Wang, Wentao Pan, Hongtao Wu, Houwen Peng
- affiliations: not stated
- posted: 2026-07-12
- source: arXiv
- link: https://arxiv.org/abs/2607.10522v1
- keyword hits: agentic, large language model, llm

### abstract

Large language model (LLM) agents are beginning to automate machine learning engineering (MLE) by coupling planning, code execution, debugging, and empirical feedback. Translating this capability to medical imaging remains difficult because each task imposes modality-specific experimentation and strict requirements for validation protocols and prediction artifacts. Here we introduce AMID, an autonomous multi-agent framework for medical imaging model development. AMID first proposes Data-Conditioned Method Planning, which refines coarse task-level search spaces into executable, parallelizable method lanes grounded in task-specific data analysis and runnable medical-imaging resources. It then develops Verification-Guided Two-Stage Optimization, moving from broad early exploration of diverse method lanes to selective exploitation of promising candidates while enforcing strict verification of validation protocols, metric computation, and prediction artifacts throughout the optimization. Across 20 medical imaging challenge tasks spanning diverse modalities and prediction types, AMID outperformed evaluated general-purpose MLE systems and, on several tasks, approached or matched strong human-designed challenge solutions. These results suggest that AMID can turn task-specific medical imaging model development from bespoke manual engineering into an agentic workflow for producing high-performing and auditable model artifacts across heterogeneous tasks.

---

## uid: `doi:10.2139/ssrn.7088419`

- title: Assessing the Design and Operational Integrity of Hyperscale Datacenters
- authors: William C. Houze
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7088419
- keyword hits: agentic, large language model, llm

### abstract

A 2026 hyperscale datacenter can be engineered to near-perfection and will still not make the large language model (LLM) running inside it trustworthy, because the property that makes any assertion trustworthy is not located in the machine. This essay begins with an honest engineering audit of the datacenter substrate — silicon noise, cosmic-ray soft errors, silent data corruption, error-correcting codes, power delivery, and the numerics of distributed training — in order to establish a single distinction the whole argument rests on: operational integrity (the machine computes what it was built to compute) is not epistemic integrity (the output is true and warranted). These two properties are close to orthogonal, and the datacenter can guarantee only the first. Driving the hardware to zero error leaves hallucination, ambiguity, and the generative non-uniqueness of language untouched, because those arise from architecture and statistics, not from the transistor. The essay then relocates the question of integrity from the substrate to a relation — the relation between an output and a ground that can answer for it — and argues that the machine can supply one term of that relation (the assertion) but structurally cannot supply the other (the answerability). It offers reflexive evidence: when two leading frontier systems were asked to assess the same material, they diverged, one produced a self-flattering ranking, and, asked whether they had answered "without pattern matching," one denied and one admitted the impossibility. The systems tasked with assessing integrity became, in the assessing, specimens of its absence. The conclusion is not that the tool is worthless — it is enormously valuable — but that its output is not agentic in any true sense, that pattern matching is the operation and not a mind, and that the burden of standing behind what the machine says remains, irreducibly, with the human user who alone occupies the answerable position.

---

## uid: `doi:10.2139/ssrn.6957878`

- title: User-Defined Propositional Rule Injection for Privacy-Conscious AI Assistants: Extending Contextual Integrity with Instance-Level Privacy Constraints
- authors: Aminah Ali, Qurat ul Ain
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6957878
- keyword hits: large language model, llama, llm, prompting

### abstract

Large language model (LLM) assistants increasingly mediate access to sensitive personal data, yet existing privacy alignment techniques encode constraints at the system level, fixed by developers and applied uniformly across all users. This paper introduces User-Defined Rule Injection, a lightweight prompting mechanism that extends the Contextual Integrity (CI) framework of Ghalebikesabi et al. (2024) by allowing individual users to author explicit propositional privacy rules-for example, NOT(share(medical_history) AND recipient(employer))-that are injected directly into an LLM's prompt at inference time. We reproduce the original paper's three-strategy evaluation and introduce a fourth strategy, evaluating all four across two benchmarks: a CI form-filling benchmark spanning five real-world contexts, and a novel Privacy Dialogue Benchmark we construct covering five conversational AI domains. Using TinyLlama-1.1B-Chat as the inference model, we find that all four strategies collapse to majority-class prediction, yielding identical F1 scores of 70.6% and 66.7% on the two benchmarks respectively, regardless of the privacy information provided in the prompt. This consistent failure mode-replicated across two independent benchmarks-provides direct evidence that prompting-based privacy strategies, including both Contextual Integrity reasoning and propositional rule injection, require a threshold level of model instruction-following capability to function, and that this threshold is not met by sub-2-billion-parameter models. We discuss the implications of this finding for the design of personalised privacy-enforcement systems and outline a path toward classifier-based enforcement that does not depend on in-context reasoning.

---

## uid: `arxiv:2607.12058v1`

- title: AutoTrace: From Patches to Triggers via Agentic Interprocedural Exploration
- authors: Arastoo Zibaeirad, Marco Vieira, Thomas Zimmermann
- affiliations: not stated
- posted: 2026-07-13
- source: arXiv
- link: https://arxiv.org/abs/2607.12058v1
- keyword hits: agentic, llm, llms

### abstract

Given a vulnerability-fixing commit, trigger localization asks which specific statement turns the vulnerable program state into a concrete unsafe operation. This question is harder than binary vulnerability detection because the answer demands interprocedural, causal reasoning: in a substantial fraction of real-world CVEs the triggering statement lies several call layers outside the patched function, beyond the reach of static rule sets and pattern-matching language models alike. We present AutoTrace, an agentic pipeline that localizes vulnerability triggers by exploring a code property graph layer by layer, with LLM agents deciding where to look next and deterministic admissibility gates deciding what evidence is required before a trigger can be reported. Agents never accept a trigger on their own authority; every reported trigger is backed by explicit evidence drawn from the graph, so the pipeline covers both intra- and interprocedural vulnerabilities without relying on ungrounded model judgment. On the full InterPVD benchmark, AutoTrace reaches 75.0% VulnHit and 80.8% FuncHit, surpassing the prior state of the art on the same corpus. Building on the same machinery, we construct SinkTrace-Bench, a dataset that exposes each vulnerability as a source-to-sink (S2S) causal chain from attacker-controlled input through propagation to the dangerous operation, drawn from matched vulnerable and patched program states. It comprises 1,542 verifier-confirmed, perfectly balanced vulnerable/safe samples whose label fidelity we audit against expert annotations. Benchmarking frontier LLMs on it, we find that even the strongest struggle to separate the matched pairs, exposing the causal-reasoning gap that trigger localization targets. Artifact available at https://github.com/Erroristotle/AutoTrace.

---

## uid: `arxiv:2607.12056v1`

- title: Designing Agent-Ready Websites for AI Web Agents: A Framework for Machine Readability, Actionability, and Decision Reliability
- authors: Said Elnaffar, Farzad Rashidi
- affiliations: not stated
- posted: 2026-07-13
- source: arXiv
- link: https://arxiv.org/abs/2607.12056v1
- keyword hits: ai agent, gemini, gpt-4

### abstract

Online shopping is increasingly shifting toward a model in which AI agents independently search for products, compare options, evaluate constraints, and carry out parts of the purchasing process for users. Website design must now support both human and agent-mediated interaction. This paper introduces the agent-ready website, a design framework for enhancing the readability, interpretability, verifiability, and actionability of e-commerce platforms for AI agents. Existing web design, SEO, and generative engine optimization (GEO) metrics do not fully assess a website's capacity for agent-mediated interaction. The proposed framework is structured around three dimensions agent interpretability, agent executability, and agent decision reliability supported by features such as machine readability, semantic clarity, agent actionability, and contextual decision-reliability signals. The framework is evaluated through a controlled experiment comparing a human-oriented baseline and an agent-ready version of an identical website prototype, with identical catalogs, pricing, stock, and shopping workflows. The evaluation involved five tasks, three browser-agent models (GPT-4.1, Gemini-2.5 Flash, and Grok-4 Fast), and 300 runs, measuring PASS,PARTIAL,FAIL outcomes, strict and functional success rates, error patterns, step counts, and token consumption. The agent-ready website achieved 134 PASS runs out of 150 versus 74 out of 150 for the baseline (strict success rates of 89.3% vs. 49.3%), with the largest gains in product detail extraction, comparison, and multi-constraint selection. It also reduced PARTIAL outcomes from 43 to 3 and lowered the average step count from 9.31 to 6.49. These results provide preliminary evidence that enhanced structural clarity, action cues, evidence signals, and temporal validity indicators can substantially improve the reliability and efficiency of AI browser agents.

---

## uid: `arxiv:2607.11698v1`

- title: Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming
- authors: Xutao Mao, Xiang Zheng, Cong Wang
- affiliations: not stated
- posted: 2026-07-13
- source: arXiv
- link: https://arxiv.org/abs/2607.11698v1
- keyword hits: agentic, claude, llm

### abstract

Production LLM agents such as Claude Code and Codex operate over untrusted content, files, commands, and workspace state, making safety failures directly actionable. Red-teaming must therefore keep pace with evolving models and tools. Existing approaches mainly optimize attack success and preserve artifacts such as benchmarks, payloads, or attack programs, which record where attacks succeed but not the enabling conditions behind unsafe agent behavior. We study automated red-teaming for production LLM agents using one agentic research environment to discover reusable vulnerability knowledge about another. We present AHA, a falsifiable discovery loop that proposes a vulnerability hypothesis, constructs a falsifier, instantiates a valid attack, executes it in a sandboxed harness, reflects on the trajectory, and promotes confirmed findings into a Vulnerability Concept Graph (VCG). Each concept links an attacker-facing surface to an unsafe trajectory through a claim, enabling condition, falsifier, transfer prediction, and supporting evidence. Across Claude Code and Codex on three scenarios covering direct and indirect attacks, the discovered concepts reveal a reusable vulnerability core across models and agents. A frozen VCG requires no further search and outperforms the strongest frozen discovery baseline by 14.2 percentage points under the same single-shot protocol, while transferring across scenarios and attack channels. The resulting VCG provides an auditable artifact for production safety teams to inspect vulnerabilities, validate patches, and accumulate reusable safety knowledge. Our code is available at https://github.com/henrymao2004/Auto-research-red-teaming-in-sleep.

---
