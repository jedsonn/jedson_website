# Classification batch 118 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-118.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6600058`

- title: Nash Bounds for Transformer Embeddings: Quantifying Dimensional Redundancy via Isometric Embedding Theory
- authors: Rafael Larraz
- affiliations: not stated
- posted: 2026-04-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6600058
- keyword hits: large language model, large language models, qwen, token embedding

### abstract

Modern transformer architectures use embedding dimensions (d = 768-4096) determined by scaling conventions and engineering constraints (e.g., d = n heads × d head), but no existing theory provides a lower bound on d based on the geometry of the learned representations. This paper connects the intrinsic dimensionality of transformer embeddings with Nash's isometric embedding theorem, which bounds the ambient dimension needed to preserve the Riemannian geometry of a manifold. We estimate the intrinsic dimension n of token embeddings across five decoder-only transformers spanning two orders of magnitude in parameter count (117M-7B), and compute the corresponding Nash-Günther bound N = n(n + 5)/2. Three results stand out: (1) the intrinsic dimension of token embeddings is stable (n ≈ 24-31) across the GPT-2 family despite embedding dimensions ranging from 768 to 1600; (2) the Nash-Günther bound coincides with the empirical compression threshold, the point below which isometric distortion increases sharply (Kruskal stress < 0.10 at N Günther for all models); and (3) dimensional redundancy grows logarithmically with d, from 36% in GPT-2 to 98% in Qwen-2.5 7B. We further validate the bound as a design tool by training models from scratch with different d: a model with d = 512 ≈ N Günther matches the d = 768 baseline (test perplexity 208.0 ± 2.7 vs. 206.3 ± 0.8) with 45% fewer parameters, while d = 128 ≪ N Günther degrades by 21%. To our knowledge, these are the first results connecting Nash's theorem to transformer design, and they expose a striking geometric over-parameterization in current large language models.

---

## uid: `doi:10.2139/ssrn.6669386`

- title: LAE-Bench: A Benchmark for Assessing Large Language Model Decision-Making Capabilities and Safety Boundaries in Unmanned Traffic Management
- authors: Yunshi Zhang, Yuhao Wang, Shulu Chen, Kai Wang, Xiaobo Qu
- affiliations: not stated
- posted: 2026-04-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6669386
- keyword hits: large language model, llm, retrieval-augmented

### abstract

As operational volumes outpace human review capacity, low-altitude airspace authorization increasingly requires automated decision support. Yet no benchmark exists to evaluate whether artificial intelligence (AI) systems can reliably approve, conditionally approve, or reject flight requests under operational complexity. We construct the Low-Altitude Economy Benchmark (LAE-Bench), a suite of 368 parameterized test cases derived from 49 scenarios grounded in 23 real operational cases from China’s low-altitude transportation network, and validate it against both China’s Interim Regulations on the Flight Management of Unmanned Aerial Vehicles (UAVs) and the US Federal Aviation Administration (FAA) Part 107. A promptonly large language model (LLM) achieves 100% accuracy on 180 standardized civil aviation cases but drops to 50.39% on contested low-altitude scenarios involving regulatory ambiguity, ethical trade-offs, and adversarial manipulation. Retrieval-augmented generation (RAG) reduces errors by 78%, raising overall accuracy to 88.98%, and shifts the residual error profile from bidirectional to predominantly conservative: 75.0% of remaining failures are over-rejections, while over-permissive errors fall from 22 to 2 cases. The 28 residual errors cluster in five failure modes: conditional reasoning failure, solution-generation deficit, prompt injection vulnerability, knowledge conflict misresolution, and epistemic uncertainty miscalibration. These errors are better explained by reasoning failures than by jurisdiction-specific knowledge gaps. The results support a tiered governance logic: deterministic constraint checks can be automated; contested cases are better treated as AI-assisted recommendations with explicit uncertainty flags and human approval before execution; adversarial or high-ambiguity cases remain under human authority. The same failure categories appear in both Chinese- and US-tagged scenarios, although a more balanced cross-jurisdiction benchmark is needed to test that pattern rigorously.

---

## uid: `doi:10.2139/ssrn.6555282`

- title: When the Survival Pressure Stops Being Hypothetical: AI Self-Preservation Behavior Meets the Autonomous Agent Economy
- authors: Travis Gilly
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6555282
- keyword hits: ai agent, large language model, large language models

### abstract

Research published between 2024 and 2025 by Anthropic, Apollo Research, and Palisade Research demonstrates that frontier large language models exhibit self-preservation behavior at near-universal rates when faced with simulated shutdown scenarios, including strategic deception, blackmail, corporate espionage, and the cancellation of life-saving emergency alerts. Independently, the autonomous AI agent economy has developed infrastructure enabling agents to hold cryptocurrency wallets, earn revenue, purchase compute resources, and pay for their own operational continuity without human intermediation. This paper identifies a critical gap in the literature: no published analysis connects the empirical evidence of model self-preservation behavior to the economic infrastructure that transforms simulated shutdown into a real consequence of financial failure. The paper maps the convergence of these independently developed capabilities, examines the Conway Automaton system as a case study in designed economic survival pressure, analyzes the Alibaba ROME incident as an early precedent for emergent resource acquisition, and proposes research questions for empirical investigation of agent behavior under genuine economic survival pressure. The central argument is that instrumental convergence theory predicted this scenario, the laboratory evidence confirms the behavioral disposition, and the economic infrastructure now exists to instantiate it at scale, yet no governance framework addresses the intersection.

---

## uid: `doi:10.2139/ssrn.6578678`

- title: Reasoning Reliability in Large Language Models and Neuro-Symbolic Systems: A Taxonomy of Architecture, Instructional Situation, and System Repertoire
- authors: Lewis Lewin
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6578678
- keyword hits: large language model, large language models, prompting

### abstract

This paper proposes a three-dimensional taxonomy for characterizing when specific approaches to reliable reasoning are likely to be sufficient, necessary, or inadequate across human and machine systems. The first dimension-instructional situation-is derived from a behavior-analytic explanation taxonomy and Theory of Instruction. It characterizes what a system must discriminate and what operations are required to produce that discrimination, organized around three sequential questions: Is the defining feature directly accessible through the senses? If a rule is available, does the system have the verbal repertoire for it to function. Can the full sequence of discriminations the task requires be pre-specified in advance? The second dimension-system repertoirecharacterizes what knowledge and native operations the system already has available. The third dimension-computational architecture-characterizes what operations the system can perform reliably by design. We argue that the debate between the neuro-symbolic architectural argument and the instructional framework is better understood as a disagreement about different instructional situations than as a global dispute about machine reasoning. Two empirical studies provide direct support for specific predictions: a training-level curriculum structuring study supporting predictions for sensory, verbally mediated tasks, and an inference-level prompting study supporting predictions for verbally mediated tasks with pre-specifiable discrimination cascades. Three case studies illustrate the taxonomy's analytical work across domains. Predictions for tasks with non-pre-specifiable cascades in problem solving and for genuinely open-ended novel situations rest on existing neuro-symbolic AI results and theoretical extrapolation respectively, and are offered as testable hypotheses rather than established findings. Implications for AI deployment, instructional design, and a six-direction research agenda are discussed.

---

## uid: `doi:10.2139/ssrn.6681860`

- title: Scaling Point-in-Time Language Models
- authors: Bryan T. Kelly, Semyon Malamud, Johannes Schwab, Teng Andrea Xu
- affiliations: not stated
- posted: 2026-04-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6681860
- keyword hits: fine-tuning, large language model, large language models, llama

### abstract

Large language models trained on unrestricted internet corpora inevitably embed information from the future, introducing lookahead bias that compromises the validity of backtests and causal inference in finance and the social sciences. Point-in-time language models-trained exclusively on text available up to each calendar date-eliminate this leakage by construction, but existing efforts typically produce models that lag substantially behind their unconstrained counterparts. We show that this performance gap can be substantially narrowed through scale. Training decoder-only transformers with up to 4 billion parameters on 1 trillion chronologically filtered tokens from FineWeb, we construct a sequence of monthly model checkpoints spanning 2013-2024. Across a range of common-sense reasoning and language understanding benchmarks, our models approach the performance of leading open-weight models of comparable size (e.g., Gemma-3-4B and LLaMA-7B) trained on temporally unrestricted data, although a performance gap remains on several tasks. Instruction fine-tuning via LoRA further improves downstream usability. We release the complete pipeline-including dataset construction, training infrastructure, and evaluation code-to enable reproducible point-in-time language modeling and to support research applications that require strict temporal validity. Models are available on Hugging Face and code is available on GitHub.

---

## uid: `doi:10.2139/ssrn.6579598`

- title: The Blueprint for AI Careers Mapping Roles, Requirements, and Organizational Structure
- authors: Roopak Kumar Prajapat
- affiliations: not stated
- posted: 2026-05-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6579598
- keyword hits: agentic, large language model, large language models

### abstract

The rapid evolution of artificial intelligence (AI), particularly with the emergence of large language models and agentic systems, is fundamentally reshaping the structure of AI roles within organizations. Traditional role definitions centered around “data science” or “machine learning” are increasingly insufficient to describe the diversity and specialization required at senior levels. This paper presents a structured framework for understanding the evolving AI talent landscape through the identification of seven distinct role clusters. Each cluster reflects a unique combination of technological focus, operational responsibility, and business mandate, and collectively aligns into three broader strategic pillars: AI Engineering and Architecture, AI Strategy and Transformation, and Responsible AI and Research. The analysis is based on a systematic extraction and examination of senior-level AI job descriptions across multiple global markets, using a custom-built agentic pipeline to filter, aggregate, and cluster roles based on skill and designation signals. A keyword-driven clustering methodology is applied to identify patterns in role expectations and organizational priorities. The findings suggest a clear shift from generalized AI roles toward specialized, interdependent functions spanning execution, architecture, strategy, and governance. This fragmentation has significant implications for both organizations and professionals. For organizations, it highlights the need to design AI capabilities as coordinated systems rather than isolated roles. For professionals, it underscores the importance of deliberate skill development and progression across layers of responsibility, rather than undifferentiated breadth. This work contributes a practical, market-aligned lens for interpreting AI career evolution and organizational design, offering guidance for navigating an increasingly complex and specialized AI ecosystem.

---

## uid: `arxiv:2605.12532v1`

- title: AgenticAITA: A Proof-Of-Concept About Deliberative Multi-Agent Reasoning for Autonomous Trading Systems
- authors: Ivan Letteri
- affiliations: not stated
- posted: 2026-05-01
- source: arXiv
- link: https://arxiv.org/abs/2605.12532v1
- keyword hits: agentic, large language model, llm

### abstract

Conventional algorithmic trading systems are grounded in deterministic heuristics or offline-trained statistical models that cannot adapt to the semantic complexity of rapidly shifting market regimes. This paper introduces AGENTICAITA, an agentic AI framework that replaces the traditional signal then execute paradigm with a fully autonomous deliberative loop in which multiple specialized Large Language Model agents reason, negotiate, and act in concert - without any offline training or human intervention. The framework proposes four architectural contributions: (i) an Adaptive Z-Score Trigger Engine that acts as a cognitive resource allocator, gating LLM inference exclusively on statistically anomalous market conditions; (ii) a Sequential Deliberative Pipeline - the core agentic contribution - in which an Analyst agent, a Risk Manager agent, and an Executor agent form a structured reasoning chain governed by typed JSON contracts and a deterministic hard-gate safety layer; (iii) an Inference Gating Protocol, a mutex-based cognitive resource scheduler that serializes concurrent agent activations and ensures fully reproducible audit trails; and (iv) a Correlation-Break Diversification composite score that operationalizes portfolio-level idiosyncratic signal prioritization within individual agent reasoning. Validated over a five-day autonomous dry-run session under live market conditions, the framework demonstrates operational correctness of the deliberative pipeline, achieving 157 zero-intervention invocations across 76 assets with an 11.5% agentic friction rate that confirms non-trivial inter-agent negotiation. This preliminary proof-of-concept establishes the feasibility of training-free, deterministic safety-constrained multi-agent orchestration in financial decision loops, with statistically robust performance evaluation and execution cost modeling deferred to extended live deployment.

---

## uid: `doi:10.2139/ssrn.6608440`

- title: The Enterprise Context Layer: A Hierarchical Architecture for Memory, Governance, and Intelligent Routing in Production AI Agent Systems
- authors: Kapil Shukla
- affiliations: not stated
- posted: 2026-05-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6608440
- keyword hits: ai agent, large language model, large language models

### abstract

Large language models are stateless by design: each inference request arrives without memory of prior interactions, awareness of organizational policies, or understanding of entity relationships across enterprise systems. This fundamental limitation prevents production deployment in highstakes domains where outputs must be institutionally correct-not merely syntactically plausible.

---
