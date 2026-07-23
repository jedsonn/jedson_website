# Classification batch 202 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-202.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6740079`

- title: Brand Erasure: A Research Agenda for Brand Theory in Agentic AI Markets
- authors: Marcos Guimaraes Figueira
- affiliations: not stated
- posted: 2026-05-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6740079
- keyword hits: agentic, foundation model

### abstract

Brand theory was built for an era in which consumers found brands through search, evaluated them through marketing communications, and chose them through deliberate decision processes. That era is ending. AI assistants-generative chat interfaces, voice agents, and the autonomous systems that act on users' behalf-are becoming the dominant intermediary between consumers and the products, services, and content that satisfy their needs. In this layer, the brand can be omitted from the answer, paraphrased into the synthesis, or substituted at the moment of action without the consumer ever noticing. This article advances brand erasure as a research construct and lays out an agenda for the work that needs to follow. It distinguishes erasure from adjacent constructs (dilution, disintermediation, algorithmic invisibility), argues that customer-based brand equity (Keller, 1993) requires extension into the latent-space substrate of foundation models, and proposes five research questions that map the empirical and theoretical work the field has not yet done. The agenda is written for marketing scholars, but its consequences extend to information retrieval, platform governance, and the regulation of attribution in AI systems.

---

## uid: `doi:10.2139/ssrn.6826576`

- title: Structured Knowledge-Guided Self-Evolution for LLM Agents via Group Relative Policy Optimization
- authors: Jen-Wei Hsueh, Jiale Wang, Hai-Tao Zheng, Lan Zhou, Hong-Gee Kim, Guangxin Wang
- affiliations: not stated
- posted: 2026-05-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6826576
- keyword hits: large language model, llm, prompting

### abstract

Large language model agents can solve increasingly complex tasks, but their behavior is still often governed by fixed prompts, manually designed rules, or external supervision. This makes adaptation costly when the environment changes. We formulate agent self-evolution as a structured policy learning problem and propose SEAF, a self-evolutionary framework that combines explicit knowledge updates with policy optimization. SEAF separates interaction into two stages: in-episode execution, where the agent uses retrieved experience and environment rules to choose actions, and post-episode evolution, where trajectories are distilled into structured knowledge and used to update the policy. The framework maintains two complementary knowledge stores: Environment Rules (ER), which capture causal constraints of the environment, and Strategy Memory (SM), which records successful heuristics and recurring failure patterns. To internalize these experiences, SEAF applies Group Relative Policy Optimization (GRPO) with weighted reward broadcasting, allowing sparse episode-level rewards to provide more informative step-level training signals. Experiments on logic games and the TravelPlanner benchmark show that SEAF improves both rule discovery and long-horizon planning, outperforming prompting baselines, automated agent methods, and vanilla GRPO on most evaluation metrics.

---

## uid: `doi:10.2139/ssrn.6811820`

- title: Fine-Tuned Multimodal Large Language Models for Clinical Interpretation of Medical Imaging Findings
- authors: Tolulope Barakat
- affiliations: not stated
- posted: 2026-05-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6811820
- keyword hits: fine-tuning, large language model, large language models

### abstract

The integration of artificial intelligence into clinical diagnostics has evolved past simple categorical categorization, transitioning toward unified diagnostic synthesis capable of contextual reporting. While traditional deep neural frameworks yield stable performance across localized tasks, they are structurally constrained by their inability to synthesize textual descriptions, parse multi-pathological patterns, or reconcile image features with nuanced medical records. This paper presents a comprehensive study of parameterefficient and instructional fine-tuning methodologies designed for Multimodal Large Language Models (MLLMs) to support clinical radiology and multi-modal diagnostic interpretation. By binding custom deep convolutional tokenizers and vision-language mapping layers to highly parameterized autoregressive text decoders, the system learns to map complex spatial medical arrays directly to detailed, coherent clinical findings. Empirical evaluation across diverse imaging benchmarks proves that targeted alignment optimization enables the framework to generate reports with high structural accuracy and clinical relevance while eliminating linguistic hallucination patterns. By translating dense mathematical tensor spaces directly into verifiable text rationales, this architecture establishes an alternative standard for interpretable diagnostic assistants, ensuring compliance with strict regulatory, safety, and operational standards in real-world clinical environments.

---

## uid: `doi:10.2139/ssrn.6817598`

- title: Distributing Accountability, Not Capability: Phase Separation and the LLM Workflow Quadrant in Autonomous AI Agent Architectures
- authors: Tatsuya Shimomoto
- affiliations: not stated
- posted: 2026-05-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6817598
- keyword hits: ai agent, llm

### abstract

Autonomous AI agents in business deployments exhibit a recurring failure mode: when an incident occurs, responsibility cannot be redirected to a separable contributor. The dominant discourse treats this as a single phenomenon, addressed by sandboxing, human-in-the-loop overload, or what Elish (2019) named the moral crumple zone. This paper argues the phenomenon is two architecturally distinct failure modes that have been conflated, and that the conflation is sustained by a missing positive name and a missing time-axis. The paper introduces two contributions. First, a four-quadrant decomposition of business AI work — along the axes of deterministic vs semantic-judgment and pre-defined vs exploratory — yields a positive name for the cell most current LLM applications occupy: the LLM Workflow Quadrant. The quadrant is defined by a single load-bearing property: the path is decided in advance by humans or by code, and the LLM is called as a single bounded step within that path; the property divides naturally into a conversational sub-form (specialized chat agents) and a batch sub-form (single-purpose LLM functions inside deterministic pipelines). The decomposition distinguishes principled from artificial redirect impossibility: the former intrinsic to autonomous loops, the latter the product of routing workflow work through autonomous-loop architecture by elimination, with four downstream symptoms (the RPA exception-handling bottleneck, the sandbox-strength demand, the structural distortion of human-in-the-loop, and the dissolution of the accountability chain at postmortem). Second, a Phase Separation axis (design vs operation), independent of Quadrant, surfaces a Phase-crossing decision — recorded at deployment time, in one sentence — required when an autonomous-loop component is placed in the operation phase. The Phase axis descends recursively to skill-design granularity, where the Quadrant 3 ↔ Quadrant 4 boundary is a continuous gradient on which model capability is downstream of phase, not the primary lever. The consequence is procedural rather than architectural: deployments make the Phase-crossing decision explicit, designate a pre-named gap-bearer for principled-impossibility placements, and route artificial-impossibility cases to re-architecture. The framework complements existing AI risk-management and management-system standards by recording the judgment layer they presuppose. Both rules are stated as experimental; the open questions are the research agenda.

---

## uid: `doi:10.2139/ssrn.6840244`

- title: AGEE: A Multi-Dimensional Process-Level Metric for Evaluating Agent Exploration over Knowledge Graphs
- authors: Murat Gök
- affiliations: not stated
- posted: 2026-05-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6840244
- keyword hits: chain-of-thought, llm, qwen

### abstract

Existing benchmarks for autonomous agents reduce trajectories to a single scalar—task success rate or Hits@1—hiding how, rather than whether, an agent explores its environment. Yet chain-of-thought reasoning is frequently unfaithful: two agents with identical task performance can reach the answer through different traversals. We introduce AGEE (Agent Graph Exploration Efficiency), a three-component composite metric decomposing exploration into structural coverage (Shannon entropy of visited communities, stabilised by James-Stein shrinkage), information gain rate (diminishing-returns weighted discovery), and exploration efficiency (coverage-AUC against a closed-form ideal). Components are aggregated via a weighted power mean at p=0.5, satisfying seven axiomatic properties adapted from Moffat's framework. We validate AGEE on 800 ReAct-style attempts by Qwen-2.5-7B on the MetaQA-2hop knowledge graph (43,234 entities; 134,741 triples), with BFS, Greedy, and Random-Walk baselines and six synthetic topologies. Two findings emerge that outcome metrics cannot reveal. First, the LLM operates in two distinct modes: it traverses the graph on 40.5% of questions (Hits@1 = 75.3%) and answers from parametric memory on the remaining 59.5% (Hits@1 = 10.9%); chi-square strongly supports mode-correctness dependence (χ² = 82.97, p

---

## uid: `doi:10.2139/ssrn.6849321`

- title: Three-Year Evidence from Approximately 5,000 A-Share Stocks on the Limits of Pre-trained TSFM Integration
- authors: Yilin Zhong, Yuqi Fu, Sixuan Zhu
- affiliations: not stated
- posted: 2026-05-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6849321
- keyword hits: fine-tuning, foundation model

### abstract

We evaluate Kronos, a pre-trained time-series foundation model (TSFM) for financial markets, for daily volatility prediction across approximately 5,000 Chinese A-share stocks in each of three consecutive calendar years (2023–2025) under a strict lagged-only protocol. Zero-shot Kronos underperforms all traditional baselines; fine-tuning further degrades accuracy due to an encoder bypass code path we term fine-tuning collapse; and the Kronos–MS-GARCH (Multi-Scale GARCH) hybrid is statistically indistinguishable from MS-GARCH alone (p = 0.42, Cohen's d = 0.06). A parsimonious HAR-RV model achieves the lowest MAE (1.29% in 2025) and ranks first or second in every year, while Kronos ranks last with MAE 2.4×–2.6× that of HAR-RV. Three mechanisms explain this boundary: BSQ quantization distortion, volatility-from-price derivation mismatch, and fine-tuning collapse. General-purpose TSFMs provide no measurable gain for daily A-share volatility forecasting.

---

## uid: `doi:10.2139/ssrn.6791859`

- title: Agentic AI, Large Language Model Methodologies, and Workflow-Level ROI in Portfolio Risk Analysis at Navy Federal Credit Union: An Evidence-Constrained Quasi-Experimental Comparison of the Pre-Agentic Era (2023-2024) and the 2025 Transition
- authors: Matthias Mbarga
- affiliations: not stated
- posted: 2026-05-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6791859
- keyword hits: agentic, large language model

### abstract

This study examines whether publicly available evidence is consistent with an improvement in the workflow-level return on investment (ROI) of portfolio risk analysis at Navy Federal Credit Union after the institution moved from bounded digital-investment automation toward a broader generative and agentic artificial intelligence (AI) posture. The paper deliberately avoids claiming observed client alpha, portfolio outperformance, or causal financial effects because Navy Federal does not publicly disclose member-level portfolio returns, advisory assets by workflow type, workflow-cycle times, analyst labor costs, or a standalone AI ROI figure. Instead, the study uses an evidence-constrained quasi-experimental comparison of a pre-agentic baseline period (2023-2024) and a 2025 transition period. The analysis triangulates three evidence layers: public institution-level financial indicators, observable digital-investment capability disclosures, and an Author-Constructed Agentic Portfolio Risk Capability Index (APRCI). To make the APRCI more defensible, the revised methodology provides a five-dimension codebook, score anchors, source-to-score crosswalk, equal-weighting rationale, and sensitivity checks under alternative assumptions. Results show that assets increased from USD 170.8 billion in 2023 to USD 197.2 billion in 2025, members’ equity increased from USD 14.2 billion to USD 18.9 billion, and net income increased from USD 1.37 billion to USD 1.91 billion. At the same time, the delinquency ratio rose from 1.59% to 1.96%, indicating that stronger analytics would have operated in a more risk-intensive environment rather than an artificially benign one. The APRCI increases from 48 in 2023 to 64 in 2024 and 92 in 2025, with conservative sensitivity analysis still supporting a large directional capability gain. The bounded conclusion is that the public record is consistent with improved workflow-level ROI potential through faster review preparation, richer monitoring, improved documentation, stronger explanation capacity, and more scalable human-in-the-loop governance. The magnitude of ROI remains unobserved and should be tested in future work using de-identified workflow telemetry or synthetic portfolio-review datasets.

---

## uid: `doi:10.2139/ssrn.6789618`

- title: Agentic AI, Large Language Model Methodologies, and Workflow-Level ROI in Portfolio Risk Analysis at Navy Federal Credit Union: An Evidence-Constrained Quasi-Experimental Comparison of the Pre-Agentic Era (2023-2024) and the 2025 Transition
- authors: Matthias Mbarga
- affiliations: not stated
- posted: 2026-05-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6789618
- keyword hits: agentic, large language model

### abstract

This study examines whether publicly available evidence is consistent with an improvement in the workflow-level return on investment (ROI) of portfolio risk analysis at Navy Federal Credit Union after the institution moved from bounded digital-investment automation toward a broader generative and agentic artificial intelligence (AI) posture. The paper deliberately avoids claiming observed client alpha, portfolio outperformance, or causal financial effects because Navy Federal does not publicly disclose member-level portfolio returns, advisory assets by workflow type, workflow-cycle times, analyst labor costs, or a standalone AI ROI figure. Instead, the study uses an evidence-constrained quasi-experimental comparison of a pre-agentic baseline period (2023–2024) and a 2025 transition period. The analysis triangulates three evidence layers: public institution-level financial indicators, observable digital-investment capability disclosures, and an Author-Constructed Agentic Portfolio Risk Capability Index (APRCI). To make the APRCI more defensible, the revised methodology provides a five-dimension codebook, score anchors, source-to-score crosswalk, equal-weighting rationale, and sensitivity checks under alternative assumptions. Results show that assets increased from USD 170.8 billion in 2023 to USD 197.2 billion in 2025, members’ equity increased from USD 14.2 billion to USD 18.9 billion, and net income increased from USD 1.37 billion to USD 1.91 billion. At the same time, the delinquency ratio rose from 1.59% to 1.96%, indicating that stronger analytics would have operated in a more risk-intensive environment rather than an artificially benign one. The APRCI increases from 48 in 2023 to 64 in 2024 and 92 in 2025, with conservative sensitivity analysis still supporting a large directional capability gain. The bounded conclusion is that the public record is consistent with improved workflow-level ROI potential through faster review preparation, richer monitoring, improved documentation, stronger explanation capacity, and more scalable human-in-the-loop governance. The magnitude of ROI remains unobserved and should be tested in future work using de-identified workflow telemetry or synthetic portfolio-review datasets.

---
