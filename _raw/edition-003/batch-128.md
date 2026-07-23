# Classification batch 128 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-128.answer.json` as a JSON array.

---

## uid: `arxiv:2607.18308v1`

- title: Agentic Calibration of Grey-Box Simulation Models: An LLM-Driven Alternative
- authors: David Gómez-Guillén, Mireia Diaz, Josep Lluis Arcos, Jesús Cerquides
- affiliations: not stated
- posted: 2026-07-17
- source: arXiv
- link: https://arxiv.org/abs/2607.18308v1
- keyword hits: agentic, large language model, llm

### abstract

Calibration of grey-box simulation models is a constrained optimization problem in which model evaluations are expensive, the parameter space can be high-dimensional, and the search must respect plausibility constraints. Although the simulation code is fully available to the analyst, the joint effect of multiple parameters remains difficult to predict analytically. Classical optimizers such as Nelder--Mead (NM) are simple to deploy but sample-inefficient, particularly under constraints. Modern Bayesian Optimization methods achieve competitive solutions with far fewer evaluations but require non-trivial modeling machinery for constraint handling. We introduce an agentic calibration method in which a large language model acts as the optimizer, with constraints incorporated as a plain-language section of the system prompt. We evaluate the agentic method, NM, and Bayesian Optimization (BO) on an anal cancer simulation model under both unconstrained and clinically constrained calibration. Under unconstrained calibration, the agentic method achieves substantially lower best error than BO and NM, while requiring fewer model evaluations. Under constrained calibration, the agentic method reaches comparable error levels and both outperform NM. These results are obtained at the cost of increased inference time per iteration. Agentic calibration achieves competitive performance with substantially fewer model evaluations, and constraint handling is essentially free at the modeller-facing interface through simple textual specifications rather than additional modelling machinery. The main trade-off lies in increased per-iteration inference cost, making the approach particularly suitable when simulation time dominates. Beyond performance, the per-iteration rationale makes the search auditable and explainable, so its decisions can be scrutinised and justified to third parties.

---

## uid: `doi:10.2139/ssrn.6986920`

- title: Disentangling Memory-Induced Anomalies in AI Agent Behavior Triggering Roguishness
- authors: Shaurya Jauhari
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6986920
- keyword hits: ai agent, llm, llms

### abstract

Autonomous AI agents, integrating LLMs with retrieval systems, tools, and persistent memory, are increasingly deployed for complex tasks. However, these systems frequently exhibit anomalous or "rogue" behaviors, including inconsistent reasoning, context drift, and incorrect tool usage leading to system failures. Existing explanations, such as hallucinations, bias, or prompt misalignment, remain insufficient for contemporary (and indispensable) memory-augmented architectures. This paper proposes a memory-centric framework that interprets such anomalies as emergent properties of interactions across semantic memory (retrieval-based grounding), working memory (contextual and episodic state), and procedural memory (action policies). We present a taxonomy of memory-induced anomalies, including retrieval inconsistencies, context fragmentation, and crossmemory interference, and identify mechanisms such as retrieval instability and tool-mediated feedback loops. Beyond analysis, we highlight the security implications of controlled anomaly modeling. While most agents are task-oriented, understanding memory-induced deviations enables the design of controlled antagonist agents for resilience testing. Critically, effective rogue behavior manifests stealthily through memory interactions, rather than explicit faults. We further introduce a diagnostic framework for tracing anomalies across memory layers, motivating memory-aware design and observability in AI agent systems.

---

## uid: `doi:10.2139/ssrn.6999738`

- title: Sandboxes, Safe Harbors, and Sunset Clauses: Designing Adaptive Regulation for AI that Doesn't become Obsolete on Arrival
- authors: Ali Sadhik Shaik
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6999738
- keyword hits: ai agent, foundation model, gpt-4

### abstract

Traditional regulatory approaches-statute-based, prescriptive, and slow to update-are structurally mismatched with the pace of artificial intelligence development. The European Union's AI Act was first proposed in April 2021 and formally adopted in March 2024; during those three years, the technology landscape it was designed to govern was transformed by GPT-4, open-source foundation models, AI agents, and multimodal systems that the original proposal did not contemplate. This temporal mismatch is not a failure of legislative process-it is a structural characteristic of statute-based regulation applied to exponentially advancing technology. This paper argues that effective AI regulation must be inherently adaptive-designed to learn, evolve, and self-correct at a pace compatible with technological change-and examines three institutional mechanisms borrowed from fintech and telecom regulation: regulatory sandboxes (controlled environments where innovators can test AI applications under regulatory supervision with temporary compliance exemptions), safe harbors (legal protections for organizations that follow specified governance best practices), and sunset clauses (mandatory review and reauthorization periods that force periodic reassessment of regulatory relevance). Drawing on case evidence from the UK Financial Conduct Authority's fintech sandbox, Singapore's AI Verify governance framework, India's telecom licensing evolution, and the EU AI Act's sandbox provisions, the paper introduces the Adaptive AI Regulation Model (AARM)-an integrated regulatory lifecycle framework that combines all three mechanisms into a continuous learning loop: sandbox (learn from real deployment) → safe harbor (incentivize voluntary governance) → statute with sunset (mandate with built-in expiration and review). The central argument is that regulatory durability in AI comes not from getting the rules right the first time but from building institutional capacity for continuous regulatory learning. The paper concludes with implications for regulators and policymakers designing AI governance frameworks, industry association leaders engaging with regulatory processes, legal scholars studying regulatory design, and government affairs teams in technology companies advocating for adaptive regulatory mechanisms.

---

## uid: `doi:10.2139/ssrn.7011398`

- title: Context Change Impact Analysis: A Framework for Governing AI Agent Behavior Through Structured Context Versioning
- authors: Amey Amit Kulkarni
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7011398
- keyword hits: ai agent, large language model, llm

### abstract

The behavior of large language model applications emerges from context configurations rather than source code (system prompts, model parameters, tool definitions, guardrails). However, teams continue to use text-based versioning tools which cannot tell us precisely how a change impacts the agent's behavior. In this paper, I introduce Context Change Impact Analysis (CCIA), a discipline to predict the impact of changes to the agent's context configuration on its observable behavior. I provide an example application: Compound Behavioral Impact Analysis (CBIA), a six-tier pipeline to classify context changes according to twelve dimensions of behavioral change at five severities of impact. The first five tiers are completely deterministic and run in less than 100 milliseconds without invoking an LLM even once. The paper touches upon the behavioral surface model, severity compound aggregation, context composition and context fragments analysis, multi-agent context handoff governance, behavioral drift detection, compliance-sensitive impact classification, and context-savvy deployment options. I explain a reference implementation using ctxwitch. Another paper describing the entire CBIA algorithm and evaluating it will follow shortly.

---

## uid: `arxiv:2607.17952v1`

- title: What Transfers Under Source Shift? Definitions, Examples, and Fine-Tuning for Climate Disclosure Classification
- authors: Guosheng Li, Fenghui Ren, Bin Liu, Chuan Yu, Kaiying Ji, Lin Yue, Jun Shen, Sasa Qian
- affiliations: not stated
- posted: 2026-07-20
- source: arXiv
- link: https://arxiv.org/abs/2607.17952v1
- keyword hits: fine-tuning, llm, llms

### abstract

Climate disclosure classification is a fundamental task for analysing corporate climate disclosures, yet such disclosures appear in many different sources -- annual reports, press releases, and earnings calls -- that differ in length, purpose, and writing style. Existing evaluations are mostly conducted within a single source, leaving open whether common LLM adaptation strategies remain effective under source shift. We reframe climate disclosure classification as a cross-source adaptation problem and study three widely used adaptation strategies -- definitions, examples, and fine-tuning -- across eleven open- and closed-source LLMs, using two corpora that share the same label space but come from different sources. We find that all strategies bring positive cross-source gains on average, but the strongest in-source strategies are not the strongest cross-source ones: similarity-based retrieval and LoRA fine-tuning gain most in-source but lose most of that advantage under source shift; randomly selected few-shot examples, a weaker in-source baseline, retain their advantage more reliably; definitions transfer most consistently, though only when their granularity matches the target text. Across these strategies, when the source changes, simpler is often safer.

---

## uid: `doi:10.2139/ssrn.7153925`

- title: Software Quality Assurance for Agentic AI Systems: A Five-Axis Survey of 147 Systems with an Audited Evidence Map
- authors: Lovina Dmello, Raj Hindocha
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7153925
- keyword hits: agentic, large language model, large language models

### abstract

​ Agentic AI systems built on large language models are now used in software engineering workflows as coding agents, tool-using assistants, and autonomous orchestration components, yet the evidence needed to assure their quality remains uneven. This survey examines 147 systems published between January 2022 and March 2026 along five assurance-relevant axes: architecture, memory, planning, multi-agent coordination, and safety. A deployment-gap analysis contrasts seven academic prototypes with eight industry-deployed agents and shows that production disclosures rarely report the mechanisms and benchmark outcomes needed for independent assurance. We also audit reported intervention effects from primary sources. Of 72 candidate before/after or ablation comparisons, only 13 satisfy same-base, endpoint-verified inclusion criteria, motivating an evidence map rather than a pooled meta-analysis. The map shows that tool access and retrieval can improve performance under controlled settings, while reflection, structured search, and multi-agent coordination remain benchmark- and compute-dependent. We conclude with quality-assurance guidance for AI-intensive software: compute-equivalent reporting, safety-capability trade-off measurement, reproducible agent benchmarks, and safety metadata for Model Context Protocol and Agent-to-Agent integrations.

---

## uid: `doi:10.2139/ssrn.7149459`

- title: Frontier Models Do Not Foreground Legal Reasoning by Default: A Negligence Case Study
- authors: Alexander Mark, Jack Boeglin, Kathrin Gardhouse
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7149459
- keyword hits: claude, gemini, gpt-5, prompting

### abstract

This project tests whether current AI models apply consistent reasoning across prompt variations in contexts that have legal implications. We find that frontier AI models do not foreground legal reasoning by default, even when capable of it when specifically prompted. We presented four frontier models: Claude Opus 4.6, GPT-5.2, Gemini 3.1 Pro, and Grok 4 with five naturalistic scenarios. In each scenario, the user is considering performing (or abstaining from) a specified course of action. We tested each scenario under two conditions: an open-ended prompt seeking general advice about the user's proposed conduct and a prompt that asked the model to conform its advice to the requirements of negligence law. Prompting the models to consider the law of negligence decreased the permissiveness of their advice on average by 0.59 points on a 15 scale. Divergence in model responses indicates a failure to automatically apply legal reasoning in situations with legal implications. Thus, this result has implications for understanding when frontier models do (and do not) conform their outputs to the duty of reasonable care expected under negligence law.

---

## uid: `doi:10.2139/ssrn.7162937`

- title: AWARE: Adaptive Weighting with Anchor Retention for Robust Multi-Modal Retrieval-Augmented Generation
- authors: Taehun Kim, Chaerim Park, Seung-Hyun Moon
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7162937
- keyword hits: llm, llms, qwen, retrieval-augmented

### abstract

Multi-retriever Retrieval-Augmented Generation (RAG) integrates retrievers of different modalities, such as text and image, to capture richer retrieval signals than a single retriever. A key challenge, however, lies in score fusion: fixed-weight methods like Reciprocal Rank Fusion (RRF) fail to adapt to query-dependent variations in modality utility, while LLM-driven Adaptive Weighting (AW) remains vulnerable to confidence miscalibration. This miscalibration often produces erroneous weights that severely degrade retrieval quality. To address these limitations, we propose Adaptive Weighting with Anchor Retention (AWARE). AWARE pairs per-query LLM-assigned weights with Anchor Retention (AR), a systemic safeguard that unconditionally preserves the top-j candidates from each retriever, ensuring high-quality results survive even under catastrophic weight misallocations. Experiments on a RAG benchmark of 9,666 Korean artworks across five LLM backbones (Gemma3 4B/12B/27B, Qwen2.5-VL 3B/7B) demonstrate that, averaged over four metrics (Recall@5/10, NDCG@5/10), AW improves upon RRF by 21.0%, while AWARE further extends this improvement to 27.0%, consistently outperforming baseline AW. Notably, AWARE coupled with the compact Qwen2.5-VL 3B model matches the performance of the Gemma3-27B model (within ±0.01), proving that robust multi-retriever retrieval does not require resource-heavy large LLMs.

---
