# Classification batch 211 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-211.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6909859`

- title: Governing Artificial Intelligence in Further Education: A Structured Policy Analysis Using PATHWAY
- authors: Roba Alsaigh, Rashid Mehmood, Iyad Katib
- affiliations: not stated
- posted: 2026-07-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6909859
- keyword hits: generative ai, prompting

### abstract

Artificial intelligence is transforming educational practice, prompting institutions to establish policies that ensure responsible, ethical, and effective use of emerging technologies. This research examines an anonymised AI policy from a UK Further Education (FE) college and evaluates its alignment with national expectations and international governance trends. To structure this analysis, the work applies the PATHWAY AI Governance Framework, a conceptual model developed to guide systematic review of institutional AI policies through staged analysis of Policy provisions, Regulatory Alignment, Threats and gaps, Harmonisation through recommendations, Workflow and oversight considerations, Assurance, and Yield of governance insights. Results reveal strong alignment with UK requirements for safeguarding, data protection, online safety, and academic integrity, as well as a clear recognition of the risks and limitations associated with generative AI. At the same time, several areas for future development are identified, including risk-based governance, fairness considerations, cross-border data issues, audit mechanisms, and differentiated controls for advanced AI systems. By situating a real FE policy within the broader landscape of AI governance, this work offers a structured, replicable method for evaluating institutional readiness and strengthening policy design. The intention is to inspire further research, practical adoption, and informed debate on responsible AI integration across the education sector.

---

## uid: `arxiv:2607.05876v2`

- title: Think Before You Grid-Search: Floor-First Triage for LLM Serving
- authors: Yihua Liu
- affiliations: not stated
- posted: 2026-07-07
- source: arXiv
- link: https://arxiv.org/abs/2607.05876v2
- keyword hits: agentic, deepseek, llm

### abstract

LLM serving optimization typically benchmarks many configurations and reaches for heavy profilers when latency targets are missed. We argue for the reverse discipline: estimation is the analytical layer of profiling -- without it, optimization degenerates to grid search. Floor First is a residual-driven triage workflow. Each decode step is modeled as a five-dimensional resource vector (HBM bytes, FLOPs, network bytes, network messages, KV capacity); summing within a resource and maximizing across resources gives an optimistic floor, the plain sum a pessimistic one. Where a measurement lands inside this [max, sum] interval reads out overlap quality before any profiler is opened, and profilers escalate only on residuals above a stated threshold. Deployment alternatives are compared by wall ordering -- which resource wall binds first as load grows -- rather than by point benchmarks. The account is compositional: new attention or state-space variants enter by declaring one module, and the workflow ships as a zero-dependency calculator plus an agent skill that enforces the discipline in agentic optimization loops. As a case study we analyze a DeepSeek-V3.2-style 671B MoE/MLA model on 16 NVIDIA H20 GPUs, whose ridge point of ~74 FLOP/byte (vs ~590 for H100) makes it an extreme decode-oriented part. The floors show TP16 decoding is KV-capacity-limited to ~70 concurrent 8K requests; sparse attention removes the KV-bandwidth term but not the capacity wall; an EP16+DP-attention layout accepts slightly worse same-batch weight traffic for an order-of-magnitude higher capacity wall (~644) -- while single-stream latency favors TP by 2.4x. The layout judgment is thus a computable function of the operating point, explaining why production deployments on identical hardware have shipped opposite attention layouts.

---

## uid: `arxiv:2607.07052v1`

- title: Progressive Crystallization: Turning Agent Exploration into Deterministic, Lower-Cost Workflows in Production
- authors: Arun Malik
- affiliations: not stated
- posted: 2026-07-08
- source: arXiv
- link: https://arxiv.org/abs/2607.07052v1
- keyword hits: ai agent, llm

### abstract

AI agents deployed for IT operations are typically permanent cost centers because every execution requires full LLM inference, even for previously solved problems. This paper introduces progressive crystallization, a lifecycle that treats agent exploration as a discovery mechanism rather than a permanent execution model. It defines a three-stage execution taxonomy, from fully agent-orchestrated to hybrid to fully deterministic workflows, together with an evidence-based promotion mechanism that converts repeatedly validated agent behaviors into cheaper and more reproducible deterministic workflows, while automatically demoting workflows that regress. Evaluated on a production cloud networking AIOps system processing tens of thousands of incidents per month, the approach increased deterministic execution from 0% to 45% over eight months, reduced per-incident agent costs by more than 70% despite doubling incident volume, and improved safety through greater reproducibility and auditability. The paper also presents the execution taxonomy, promotion and demotion criteria, trace extraction methodology, economic model, safety considerations, and discusses limitations and threats to validity.

---

## uid: `arxiv:2607.08681v1`

- title: SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized Energy Markets
- authors: Shilin Ou, Yifan Xu, Luyao Zhang
- affiliations: not stated
- posted: 2026-07-09
- source: arXiv
- link: https://arxiv.org/abs/2607.08681v1
- keyword hits: agentic, llm

### abstract

As agentic AI systems are increasingly applied to cyber-physical environments, their evaluation requires assessment of both task performance and trustworthiness. In decentralized energy markets, autonomous agents may improve market utility, but may also exploit invalid physical data, create artificial liquidity, and produce unstable governance decisions. Therefore, we propose SolarChain-Eval, a physics-constrained benchmark for evaluating trustworthy economic agents. It formulates market governance as a Gymnasium-compatible Markov Decision Process, where agents make hourly decisions. SolarChain-Eval evaluates each policy across multiple dimensions, including market utility, physical safety, slippage, action smoothness, spatial fairness, and auditability. To support agentic evaluation, SolarChain-Eval incorporates an LLM-based Planner/Auditor layer. The Planner defines episode-level action bounds and audit rules, while the Auditor reviews and revises high-risk actions. All interventions are recorded through structured logs, including trigger signals, proposed actions, revised actions, and audit rationales. Experiments with static, random, myopic, RL, and RL+LLM policies reveal a clear utility-safety trade-off. RL agents improve market utility but can still produce unsafe behavior. When the physics penalty is removed, reward-maximizing agents exploit invalid generation and increase artificial liquidity. The LLM Planner/Auditor improves auditability and mitigates selected risks, but it cannot fully compensate for a misspecified reward function. These results indicate that trustworthy agentic AI evaluation requires both physical constraints and transparent intervention traces. We release data and code as open access on GitHub for replicability.

---

## uid: `arxiv:2607.08960v1`

- title: Eluna: An Agentic LLM System for Automating Warehouse Operations with Reasoning and Task Execution
- authors: Ning Liu, Kalle Kujanpää, Zhaoxuan Zhu, P Aditya Sreekar, Kaiwen Liu, Chuanneng Sun, Jorge Marchena Menendez, Matthew Bales
- affiliations: not stated
- posted: 2026-07-09
- source: arXiv
- link: https://arxiv.org/abs/2607.08960v1
- keyword hits: agentic, llm

### abstract

Warehouse operations are governed by Standard Operating Procedures (SOPs) that encode complex, multi-system decision logic, which must be executed reliably under strict time constraints, yet LLM agents lack mechanisms to enforce procedural compliance and degrade under the context overload full SOP specifications introduce. We present Eluna, a production-deployed agentic system for reliable SOP execution. Eluna is a graph-guided, multi-agent framework that encodes SOPs as directed acyclic graphs with progressive disclosure and delegates independent tasks to parallel sub-agents, each with persistent code execution and live data access. To meet production latency and accuracy needs, we use asymmetric episodic distillation where a strong teacher is improved through episodic error memories, then a smaller student is fine-tuned on the corrected trajectories with memory stripped, internalizing corrections without inference-time overhead. On a 13-task benchmark and two production applications, our fine-tuned models match or exceed their teacher, beat all larger off-the-shelf baselines, and reach 94% expert agreement on the ticket processing application.

---

## uid: `arxiv:2607.08010v1`

- title: Tool-Making and Self-Evolving LLM Agents in Low-Latency Systems
- authors: Kalle Kujanpää, Ning Liu, Shahnawaz Alam, Yeshwanth Reddy Sura, Tianyu Yang, Kristina Klinkner, Shervin Malmasi
- affiliations: not stated
- posted: 2026-07-09
- source: arXiv
- link: https://arxiv.org/abs/2607.08010v1
- keyword hits: agentic, llm

### abstract

Production LLM agents often waste latency and reliability by regenerating code for the same procedural steps on every request. We replace this inference-time coding loop with an agentic tool-making pipeline that compiles repeated SOP steps into validated, versioned tools before deployment. The tool-maker grounds synthesis in the live environment as it collects execution traces, observes backend schemas and values, generates candidate tools, and repairs them against labeled cases. At runtime, the production agent calls these tools directly and falls back to code generation only when needed. We deploy the approach in a Fulfillment Center alarm-triage system, where an agent diagnoses alarms against a 44-node SOP over heterogeneous metric backends. In production, tool calls reduce p50 latency by 42%. On 1,500 historical alarms, they reduce end-to-end error rate by up to 53% by suppressing run-to-run variance in repeated steps. Because tools return compact structured verdicts, they also enable a simpler direct-call architecture, reducing p50 latency by a further 62% in a controlled ablation. Versioned tools also improve auditability and expose specification gaps and upstream data drift. Our results show that self-evolving agents can make industrial LLM systems faster, more reliable, and easier to operate.

---

## uid: `doi:10.2139/ssrn.7094539`

- title: Cross-Layer Manifold Attack and Projection for Robust Safety Alignment of Large Language Models
- authors: Ziwen Peng, Jiayu Du, Qi Zhou, Jin Zhu, Jianpeng Li
- affiliations: not stated
- posted: 2026-07-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7094539
- keyword hits: fine-tuning, large language model, large language models

### abstract

Jailbreak attacks reveal a critical weakness in the safety alignment of current large language models: although aligned models may refuse harmful requests at the output level, they can still retain latent pathways associated with unsafe responses internally, and these pathways may be reactivated by adversarial prompts. In this paper, we propose Cross-layer Manifold Attack (CMA), which suppresses harmful-manifold components while amplifying benign-manifold components in hidden states across multiple layers, progressively shifting the model's internal representations from refusal-related regions toward compliance-related regions and thereby inducing jailbreak responses.Building on this finding, we propose Cross-layer Manifold Projection (CMP). Rather than treating jailbreak robustness solely as a behavioral classification problem, CMP formulates it as a problem of controlling internal representations. Specifically, CMP estimates harmful and benign manifolds in the hidden states of each layer and applies CMA-style perturbations during training on harmful samples to simulate jailbreak-like latent shifts. The model is then safety-tuned to maintain stable refusal behavior under these perturbed hidden states.Experiments across multiple model architectures show that CMP substantially improves robustness against adversarial jailbreak attacks while largely preserving general capabilities. Compared with existing adversarial fine-tuning baselines, CMP also tends to incur lower over-refusal. In particular, CMP shows its clearest advantage under CMA-based evaluation and remains competitive under other latent-space perturbations, suggesting that representation-aware training improves robustness beyond standard output-level refusal supervision.

---

## uid: `doi:10.2139/ssrn.6939558`

- title: Discovery Yield: A Framework for Evaluating Automated Financial Hypothesis Discovery
- authors: Kishore Mantripragada
- affiliations: not stated
- posted: 2026-07-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6939558
- keyword hits: agentic, large language model, large language models

### abstract

The increasing availability of financial data and computational resources has enabled researchers to evaluate large numbers of candidate trading strategies. However, large-scale hypothesis exploration introduces a substantial risk of false discoveries, where apparently profitable signals emerge purely by chance. As a result, the effectiveness of a hypothesis generation process cannot be assessed solely by the number of promising strategies it produces. This paper formulates financial hypothesis discovery as a structured search problem and introduces Discovery Yield, a metric that measures the proportion of tested hypotheses that survive statistical validation procedures. We propose an automated framework that combines hypothesis generation, historical backtesting, statistical significance testing, and False Discovery Rate (FDR) correction within a unified evaluation pipeline. To demonstrate the framework, we conduct an empirical case study using daily SPY data spanning 2000-2024. Candidate hypotheses are evaluated through interpretable mean-reversion rules, systematic grid search, and random search procedures. While multiple hypotheses exhibit apparent statistical significance under conventional hypothesis testing, none survive Benjamini-Hochberg False Discovery Rate correction. Similarly, large-scale random search produces no statistically validated discoveries despite evaluating a substantially larger set of candidate rules. These findings illustrate the severity of the multiple-testing problem in quantitative finance and highlight the importance of rigorous statistical validation in automated strategy discovery. More broadly, the proposed framework provides a foundation for evaluating future hypothesis generation systems, including large language models, agentic research systems, and other automated discovery methods.

---
