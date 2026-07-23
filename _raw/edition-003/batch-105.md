# Classification batch 105 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-105.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7009289`

- title: Large Language Models for Software Models: An Empirical Evaluation in Game Software Engineering
- authors: Samuel Navarro, Manuel Ballarín, Carlos Cetina, Jaime Font
- affiliations: not stated
- posted: 2026-06-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7009289
- keyword hits: large language model, large language models, llm, llms

### abstract

Context: Video games industry is the largest entertainment sector. Unity is the most widely used game engine in the industry, and Unity Visual Scripting (UVS) is its native solution to develop video games using software models instead of C#. Given that modern video game development cycles often span several years, LLMs capable of manipulating game engine software models could meaningfully benefit the industry.Objective: This work evaluates the capability of seven state-of-the-art LLMs to perform manipulation tasks over UVS software models.Method: We conducted a controlled experiment in which seven LLMs (three proprietary and four open-weight) were applied to eight UVS tasks across four difficulty levels (Easy, Medium, Hard, Ultra), five times each, yielding 280 executions evaluated via Precision, Recall, and F1-score. Statistical significance is assessed using Kruskal-Wallis tests with Dunn post-hoc, and a Mann-Whitney U contrast examines the gap between proprietary and open-weight LLMs.Results: Proprietary LLMs achieve F1-scores of up to 87.11% on model completion tasks (Easyto Hard), substantially outperforming open-weight LLMs. However, on tasks that require authoring complete models from blank (Ultra), performance collapses across all LLMs to a maximum F1-score of 48.70%.Conclusion: Our findings contribute to understanding the capabilities and limitations of LLMs on video game software models, and provide guidance for practitioners on how to integrate LLMs effectively into game development workflows.

---

## uid: `arxiv:2606.29091v1`

- title: Statistically Indistinguishable, Operationally Distinct: A Formal Barrier for Tabular Foundation Models
- authors: Tassilo Klein, Johannes Hoffart
- affiliations: not stated
- posted: 2026-06-27
- source: arXiv
- link: https://arxiv.org/abs/2606.29091v1
- keyword hits: foundation model, gpt-5, llm

### abstract

Tabular foundation models cannot reason about data produced by running systems without access to the rules that govern them. We make this statement falsifiable. The \emph{Operational Turing Test} (OTT) constructs pairs of legal and rule-violating database states whose $1$- and $2$-way column-value marginals match to a total variation of $<0.02$; Le~Cam's lemma then bounds any values-only classifier at $\geq0.49$ Bayes error. Three values-only baselines (XGBoost, TabICL, TabPFN) hit the bound exactly (accuracy $0.50$, pre-registered two one-sided tests (TOST) $p<0.002$), raw row-level access does not help, exposing relational value consistency closes most of the gap, and only a classifier fed by seven executable rule-derived audits reaches $1.00$ classification accuracy. In three matched $100$-state frontier large-language-model (LLM) runs, models given the schema, trigger source, rule tables, and state files classify at most $2/50$ legal states as LEGAL; GPT-5.5 accepts $0/50$ legal states even with higher reasoning effort and a Structured Query Language (SQL) executor. The access-ladder pattern also appears on a second schema with structurally distinct rule families (banking ledger: cross-row balance, cumulative aggregate). The barrier is identifiability, not capacity: scale, data, and richer features cannot cross it without operational grounding.

---

## uid: `arxiv:2606.29366v1`

- title: Solver-Verified Formulation Generation and Selection for Multi-Warehouse Inventory Allocation Using Large Language Models
- authors: Jintao Xu, Yingzheng Ma, Jiong Dong, Yongzhi Qi, Jianshen Zhang, Dongyang Geng, Anni Zhang
- affiliations: not stated
- posted: 2026-06-28
- source: arXiv
- link: https://arxiv.org/abs/2606.29366v1
- keyword hits: large language model, large language models, llm

### abstract

Balance-oriented multi-warehouse inventory allocation is a recurring decision problem in large-scale e-commerce supply chains, in which a fixed replenishment quantity is distributed across warehouses to balance post-allocation inventory coverage while accounting for demand forecasts and heterogeneous allocation constraints. In practice, allocation requirements are often scenario-dependent and expressed in semi-structured or natural-language form rather than as ready-to-solve operations research (OR) formulations. We propose an OR-guided Large Language Model (LLM) for Allocation (ORLA) that uses solver feedback to generate, verify, and select OR formulations. ORLA integrates automatic "Problem-Model-Code (PMC)" generation, learning-based formulation selection, and feasibility restoration. We develop three complementary mixed-integer programming formulation families based on deviation minimization, soft band compliance, and knapsack-inspired allocation, together with solver-ready mixed-integer linear programming reformulations, modular constraint extensions, and a penalty-based relaxation mechanism for infeasible cases. The LLM component generates candidate formulations and executable solver code from textual or semi-structured specifications, while the solver provides verification signals for executability, feasibility, and solution quality. To address instance heterogeneity, ORLA estimates the expected quality of candidate formulations, selects promising candidates, and combines their outputs through score-aware aggregation. Experimental results on 29 production evaluation batches from JD.com show that the best single OR formulation improves allocation accuracy by 3.4 percentage points over the incumbent approach, while the full ORLA framework achieves a 4.5 percentage-point overall improvement and improves allocation accuracy in 26 of the 29 evaluation batches.

---

## uid: `doi:10.2139/ssrn.7021520`

- title: Vision-and-Language Navigation for Human–Robot Collaboration: A Comprehensive Survey
- authors: NIVEDAN YAKOLLI
- affiliations: not stated
- posted: 2026-06-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7021520
- keyword hits: large language model, large language models, llm, llms

### abstract

Vision-and-Language Navigation (VLN) is a multimodal, cooperative, and interactive task in which agents must interpret the natural-language instructions. It also requires agents to identify visual clues and directions from the instructions to navigate the complex 3D environments by taking specific actions (e.g., moving forward, turning left, stopping), and to communicate effectively with both the environment and humans. This survey offers a comprehensive overview of recent advancements in the domain of VLNs, encompassing multirobot coordination and interaction. Despite the immense progress, current work is limited by insufficient bidirectional communication, weak ambiguity resolution, and constrained collaborative decision-making in multi-agent settings. After reviewing approximately 200 papers, we categorize our paper into specific sections, including initial works, growth/diversification, and recent breakthroughs in VLNs with human–robot interaction (HRI), as well as the applications of Large Language Models (LLMs). We urge that the future VLN systems should incorporate proactive clarification, real-time feedback mechanisms, and stronger contextual reasoning through advanced natural language understanding (NLU). We strongly believe that these milestones will substantially enhance HRI and facilitate the integration of VLN-enabled multi-robots in various domains, including healthcare, disaster response, and many others.

---

## uid: `arxiv:2606.30987v1`

- title: Measuring Judgment Quality in Natural-Language Explanations: Evidence from Forecasting Tournaments
- authors: Christopher W. Karvetski, Sheldon S. Huang, Simas Kučinskas, Nadja Flechner, Jingyu Hu, Philip Tetlock, Ezra Karger
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.30987v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Decision-makers routinely rely on expert judgments accompanied by written explanations, yet explanation quality is difficult to measure at scale. Forecasting tournaments offer a natural testing ground: probabilistic judgments are paired with natural-language rationales and scored against realized outcomes. We introduce Explanation Quality Markers (EQMs), a set of sixty theory-guided reasoning patterns scored by large language models (LLMs). In a pre-registered analysis of over 55,000 forecast-rationale pairs from a multiyear forecasting tournament, EQMs predict accuracy at both the forecast and forecaster levels, consistently outperforming pre-LLM text-analysis methods. More than 90% of statistically significant pattern-level EQM-accuracy correlations match our directional hypotheses. The signal is asymmetric: EQMs identify likely underperformers more reliably than they distinguish the very best forecasters. Benchmarked against traditional indicators of forecasting skill, EQMs are the strongest predictor at the forecast level and competitive at the forecaster level, though weaker than prior accuracy. Human ratings of rationale quality are less consistently correlated with accuracy and place disproportionate weight on rationale length. Results transfer to an independent forecasting study. EQMs provide a scalable, interpretable method for extracting judgment-relevant information from written explanations.

---

## uid: `arxiv:2606.30602v1`

- title: MESA: Prioritizing Vulnerable Communication Channels for Securing Multi-Agent Systems
- authors: Kunyang Li, Kyle Domico, Jonathan Gregory, Patrick McDaniel
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.30602v1
- keyword hits: llama, llm, llms, qwen

### abstract

Multi-agent systems (MAS) are increasingly used to automate complex, distributed workflows. However, their inter-agent communication channels introduce new attack surfaces that remain poorly understood and are difficult to defend against. In this paper, we address how defenders should prioritize limited security effort to protect vulnerable communication channels before attacks are observed. This is motivated by our observation that the channel-level attack impact is highly non-uniform: a single compromised edge can account for up to 75% of total attack success. We introduce Mesa, a label-free framework for proactively ranking which MAS edges are most security-critical -- that is, most likely to affect the system's decision if compromised. Mesa combines six graph-theoretic metrics and two dynamic probes (ablation and masking) without requiring attack traces. We evaluate Mesa against a dynamic misinformation attack pipeline across three diverse MAS scenarios, eight network topologies, and five open-source LLMs from Qwen, Llama, and Gemma families. Mesa rankings correlate strongly with empirical per-edge attack success rate, achieving mean Spearman $ρ=+0.60$ (peaking at $+0.73$). In resource-constrained defense deployment, monitoring the top 10% of Mesa-ranked edges intercepts about 3x the successful attacks as random allocation. We further test Mesa under varying attacker and defender models and LangGraph workflows and characterize its limits under adaptive attacks and high-redundancy graphs. Overall, our results show that edge-level risk in MAS is often concentrated and predictable, allowing proactive hardening of multi-agent infrastructures.

---

## uid: `arxiv:2606.30578v1`

- title: Uncertainty-Aware Generation and Decision-Making Under Ambiguity
- authors: Nico Daheim, Iryna Gurevych
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.30578v1
- keyword hits: large language model, large language models, llm, llms

### abstract

With rapidly improving capabilities, Large Language Models (LLMs) are increasingly used in many complex real-world tasks. Beyond requiring in-depth knowledge and reasoning skills, many of these tasks exhibit a high degree of subjectivity and require that the outputs of the model can be trusted. While a lot of progress has been made to train better models, decision-making algorithms have received less attention. In this work, we present and evaluate various uncertainty-aware decision-making algorithms based on Bayesian decision theory and risk-averse decision making on the tasks of tutoring and automatic peer reviewing. Concretely, we take uncertainty over tutoring strategies and review scores into account when generating a tutor response or review and use conformal prediction to provide guarantees over strategy and score. We find empirically that these algorithms can improve the utility of the generations but need to be carefully implemented when ambiguity is high. For example, risk-averse rules can degrade performance by optimizing for generic outputs, while Bayesian methods tend to perform better. Our work uses techniques from decision theory to improve LLM-based decision-making and outlines open challenges for the community.

---

## uid: `arxiv:2606.30247v1`

- title: Grounding LLM Reasoning under Incomplete Graph Evidence
- authors: Jiaqi Li, Fanghui Song
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.30247v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Knowledge graphs can guide large language models (LLMs) reasoning, but the graph seen by a system is usually a retrieved, linked, temporally scoped, and incomplete evidence state rather than a complete account of truth. We develop a theoretical perspective on grounding observable LLM trajectories under such incomplete graph evidence.The evidence state induces entity anchors, typed relation residuals, path energies, and support regions, while the language model supplies a prior over candidate trajectories. We show that, under open-world incompleteness, no hard rule based only on the observed state can both reject every false unsupported trajectory and retain every true-but-unobserved one.We then characterize soft grounding as a KL-regularized deformation of the LLM prior: finite slack preserves support for unsupported but non-contradicted trajectories, whereas hard conditioning appears as an infinite-penalty limit.The framework also yields stability bounds under evidence perturbations and clarifies the constraint regimes appropriate for GraphRAG, KGQA, graph agents, constrained decoding, and faithful generation. The claims are evidence-relative: KG compatibility is treated as declared support, not factual truth.

---
