# Classification batch 71 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-71.answer.json` as a JSON array.

---

## uid: `arxiv:2607.13034v1`

- title: Do AI Agents Know When a Task Is Simple? Toward Complexity-Aware Reasoning and Execution
- authors: Junjie Yin, Xinyu Feng
- affiliations: not stated
- posted: 2026-07-14
- source: arXiv
- link: https://arxiv.org/abs/2607.13034v1
- keyword hits: ai agent, gpt-4, large language model, llm

### abstract

Large language model (LLM) agents increasingly automate multi-step engineering and informatics workflows, yet they rarely ask how much effort a task actually requires. They often follow a maximum-context-first strategy--re-reading files and dependencies they have already seen--turning a one-line edit into a small code-base audit. We argue the missing capability is task-aware execution-scope estimation: judging a task's difficulty, the information it truly needs, and the shortest reliable path before committing budget. We formalize minimum-sufficient execution and the Agent Cognitive Redundancy Ratio (ACRR), and propose E3 (Estimate, Execute, Expand): the agent estimates an initial operating point, executes a minimum viable path, and expands scope only when verification fails. On MSE-Bench--a deterministic benchmark of 121 edits in a capability-controlled simulator--E3 matches the strongest baseline's 100% success while cutting cost by 85%, tokens by 91%, and inspected files by 92%, and further beats a strong adaptive retrieval baseline by 16%; the gains survive held-out instruction wording and essentially every cost weighting. A companion real-model harness (LLM-Case) corroborates the effect on a live gpt-4o agent editing a real open-source library, with every candidate patch graded by actually running the project's real pytest suite against a measured oracle: the over-reading is milder but real, and E3 is the leanest and fastest policy at comparable task success--its one shortfall a provider rate-limit, not a wrong edit. We frame this as a controlled probe of execution redundancy, not a measurement of any deployed agent, and position task-aware execution as a step toward engineering-grounded AI (EGAI)--agents whose effort is anchored in the engineering reality of the task. We release the framework and benchmark.

---

## uid: `arxiv:2607.14178v1`

- title: ReasFlow: Assisting Reasoning-Centric Scientific Discovery in Applied Mathematics via a Knowledge-Based Multi-Agent System
- authors: Yutong He, Daibo Li, Guohong Li, Jiahe Geng, Zhengyang Huang, Can Ren, Zekun Zhang, Yifan Liu
- affiliations: not stated
- posted: 2026-07-15
- source: arXiv
- link: https://arxiv.org/abs/2607.14178v1
- keyword hits: ai agent, large language model, large language models, llm

### abstract

Recent advances in Large Language Models have fueled autonomous AI agents capable of tackling complex scientific tasks, yet existing automated research systems remain predominantly focused on empirically driven domains with quantitative benchmarks, leaving theory-driven discovery, particularly in mathematically grounded disciplines requiring rigorous proofs and synthesis of domain knowledge, largely underexplored. Key challenges include the difficulty of verifying theoretical reasoning at scale, insufficient reasoning ability for autonomous frontier exploration, and a scarcity of procedural heuristics in the literature. We introduce ReasFlow, an end-to-end autonomous agent system for reasoning-centric scientific discovery that operationalizes a collaborative paradigm where the human expert acts as Principal Investigator while the agent executes rigorous derivations as a capable graduate student. ReasFlow incorporates (i) a robust internal verification loop that audits logical coherence and corrects fundamental errors prior to human inspection, and (ii) an automated knowledge retrieval and self-improvement mechanism that proactively surfaces both declarative facts and overlooked procedural heuristics, substantially reducing expert intervention. The system unifies literature synthesis, algorithm design, theorem proving, experimentation, and manuscript preparation in a single system. Deployed to autonomously generate five complete research papers with rigorous theoretical and empirical content from minimal prompts, ReasFlow consistently achieves the highest evaluation scores among state-of-the-art open-access baselines under a curated LLM-based review rubric. ReasFlow is publicly accessible via the ReasLab platform, providing a collaborative workspace for AI-assisted theoretical research. Github repo: https://github.com/ReasLab/ReasFlow.git.

---

## uid: `doi:10.2139/ssrn.7117418`

- title: A Reference Architecture for Agentic Data Quality in Microsoft Fabric and Azure
- authors: Naveen Ayalla
- affiliations: not stated
- posted: 2026-07-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7117418
- keyword hits: agentic, large language model, large language models, llama

### abstract

Enterprise data pipelines are increasingly exposed to schema drift, incomplete metadata, statistical anomalies, ambiguous business semantics, and growing operational cost. Conventional rule-based validation remains essential because it is deterministic and auditable, but it becomes expensive to maintain when data sources and business definitions change frequently. Large language models can interpret contextual descriptions and propose mappings or explanations, yet their probabilistic outputs introduce hallucination, privacy, and governance risks. This paper presents a reference architecture for agentic data quality in Microsoft Fabric and Azure that combines deterministic Python and PySpark validation with a bounded Llama-family reasoning layer, structured agent-to-agent communication, and human-in-the-loop review. The design separates structural, statistical, semantic, policy, and governance checks; routes only ambiguous exceptions to an AI model; and records every decision, evidence item, rule version, and reviewer action. Microsoft Fabric provides orchestration, notebooks, OneLake storage, lakehouse tables, semantic models, and reporting, while Azure services provide schema management, event-driven coordination, secrets management, observability, and optional model hosting. The paper does not claim production-scale benchmark results. Instead, it contributes a precise architecture, decision policy, threat model, cost model, and reproducible proof-of-concept protocol using a public retail customer dataset with injected quality faults. The central design principle is controlled autonomy: AI may recommend and explain, but deterministic gates and accountable humans retain authority over high-impact data decisions.

---

## uid: `arxiv:2607.16097v1`

- title: Understanding Reasoning from Pretraining to Post-Training
- authors: Jingyan Shen, Ang Li, Salman Rahman, Yifan Sun, Micah Goldblum, Matus Telgarsky, Pavel Izmailov
- affiliations: not stated
- posted: 2026-07-17
- source: arXiv
- link: https://arxiv.org/abs/2607.16097v1
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Reinforcement learning (RL) has become central to improving large language models (LLMs) on complex reasoning tasks, yet RL post-training is largely studied in isolation from the pretraining that precedes it. As a result, two basic questions remain open: (1) how do pretraining choices (model size, data) shape the returns to RL compute, and (2) what does RL actually do to the model? These questions are difficult to study in the standard LLM setting: pretraining corpora are vast and uncontrolled, making it hard to attribute behaviors to pretraining versus RL, and systematic compute sweeps across both stages are prohibitively expensive. To address these challenges, we use chess as a controlled testbed for studying reasoning across the full pretraining-to-post-training pipeline. We follow the standard LLM training pipeline by pretraining language models from 5M to 1B parameters on human chess games, supervised fine-tuning on synthetic reasoning traces, and running RL on chess puzzles with verifiable rewards. Using this framework, we find that the post-RL performance at given RL compute level is well-predicted from the pretraining loss, and slope of the RL reward curves improves approximately linearly with the pretraining tokens. Beyond scaling, we find that RL does not simply sharpen the SFT policy: on easy puzzles it amplifies correct moves the SFT policy already preferred, while on hard puzzles it surfaces correct moves that were nearly absent under SFT. We further test whether our findings transfer beyond chess by training a 1B language model on math-domain text, where the same predictive pattern emerges: longer-pretrained checkpoints reach higher post-RL performance and improve faster under RL. In sum, we provide a quantitative account of the pretraining-to-RL interface and a controlled testbed for studying the science of reasoning across the full pretraining-to-post-training pipeline.

---

## uid: `doi:10.2139/ssrn.7135996`

- title: DARLIN: Domain-Guided Augmented Retrieval for LLM-Based Interpretable and Transferable HVAC Control
- authors: Yun-Dam Ko, Rishee  Kumar Jain
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7135996
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Advanced HVAC control strategies in buildings such as Model Predictive Control and Reinforcement Learning can deliver substantial energy savings but face persistent barriers to real-world adoption, including reliance on building-specific models or extensive training datasets, limited transferability across buildings and climates, and opaque decision-making. We introduce DARLIN, a retrieval-augmented framework that uses Large Language Models (LLMs) to control HVAC cooling setpoints without any modeling or training. At each control step, DARLIN retrieves relevant guidance from a knowledge base built from thousands of open-access building science papers, combines it with real-time system observations, and generates a short-horizon cooling setpoint trajectory together with a human-readable rationale. In a calibrated EnergyPlus simulation of a real office building in Stanford, California, USA, DARLIN reduced cooling energy by 7.7\% relative to a rule-based control baseline in a mild climate, while also improving occupant comfort, which the baseline degraded through afternoon overcooling. Analysis of the generated rationales shows trend-aware, predictive, history-informed, and corrective reasoning, with each setpoint decision traceable to a stated condition and a cited strategy. Applied to a different building across 15 climate zones with no building- and climate-specific changes, DARLIN achieved an average cooling energy saving of 14.4\% while improving aggregate thermal comfort. By combining LLM reasoning with domain knowledge, DARLIN offers a scalable, transferable, and interpretable approach to intelligent building control and energy utilization.

---

## uid: `doi:10.2139/ssrn.7123419`

- title: Artificial Intelligence, Algorithmic Trading, and Financial Market Microstructure: A Systematic Literature Review
- authors: Fuli Yang, Shiyu Lin, Jing Huang
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7123419
- keyword hits: ai agent, large language model, large language models, llm, llms

### abstract

The past two decades have witnessed a structural transformation in financial market microstructure: human traders have been displaced by algorithmic agents operating at microsecond timescales. This paper provides a systematic review of the academic literature on how algorithmic trading (AT), high-frequency trading (HFT), and artificial intelligence—including large language models (LLMs) and machine learning classifiers—have reshaped three foundational dimensions of market quality: liquidity provision, price discovery, and market stability. Following a PRISMA-compliant protocol, we screened 847 initial records across Web of Science, Scopus, SSRN, and Google Scholar, ultimately synthesizing 60 studies meeting pre-specified inclusion criteria. We organize the literature around three central debates. The first concerns whether algorithmic market-making constitutes genuine liquidity supply or phantom liquidity that evaporates under stress, amplifying flash crashes across equity, Treasury, and foreign exchange markets. The second examines the tension between AI-enhanced informational efficiency and systemic fragility induced by algorithmic herding, correlated machine-learning strategies, and retail-driven social media trading. The third surveys the regulatory challenge of detecting AI-facilitated market manipulation—including spoofing and quote stuffing—through natural language processing and high-frequency surveillance. Drawing on foundational contributions from Kyle (1985), Glosten and Milgrom (1985), and Budish, Cramton, and Shim (2015), we characterize the current paradigm as "algorithmic ecology"—a co-evolutionary ecosystem in which AI agents, human traders, exchanges, and regulators continuously adapt to one another's strategies. We identify a fundamental paradigm shift: market microstructure research must transition from models of rational human agents toward frameworks accommodating the strategic behavior, correlated failures, and emergent dynamics of algorithmic agents.

---

## uid: `doi:10.2139/ssrn.7017778`

- title: High-Growth Institutional Entrepreneurship in Africa: What AI Does and Does Not Tell You
- authors: Muhammad Aliyu, Roy  Ngu Esibe, Erik Stam, Jesse Thornburg, João Barros
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7017778
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

High-growth ventures remain understudied in Africa due to persistent data scarcity. This paper analyses the co-evolution of high-growth ventures and entrepreneurial ecosystems across the African continent. We introduce a scalable methodology that leverages retrieval-augmented generation (RAG) and large language models (LLMs) to extract founder-level insights from unstructured online data, producing AI-generated founder narratives. Recent advancements in LLMs and RAG enable the systematic synthesis of qualitative data into structured, comparable narratives at a scale and speed unattainable by traditional qualitative methods. To address the limitations of AI, we supplement these narratives with primary founder interviews, identifying blind spots and defining the boundaries of effective human-AI collaboration. Our analysis reveals that AI-generated narratives, may contain factual errors, framing errors and overlook private considerations that founders do not disclose publicly. We argue that AI-assisted qualitative research in data-sparse contexts still requires primary triangulation. Furthermore, we formalize the distinction between source-faithfulness and ground truth-faithfulness (from the founder's perspective) as a critical evaluative framework for AI-assisted research. Our findings also reveal that African unicorn founders not only scale high-growth ventures but also actively construct institutions: "high-growth institutional entrepreneurship".

---

## uid: `doi:10.2139/ssrn.7018998`

- title: Data-Efficient Large Language Model Training: A Survey
- authors: Xinyang Liu, Qiang Hu, Ma Yujie, Tang Zhenhuan, Jiongchi Yu, Tianlin Li, Yao Zhang, Junjie Wang
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7018998
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Constructing large language models (LLMs) is labor-intensive and computationally unfriendly due to the requirement for large-scale and high-quality datasets. This paper presents a comprehensive survey of building LLMs with limited data to tackle the above challenges. It covers 116 papers, where 18 works focus on the pre-training process, and 98 works lie in the fine-tuning process. This survey: (i) unifies the problems and terminologies associated with data-efficient LLM training, (ii) systematically analyzes techniques proposed for identifying the most important data samples for LLM building, and (iii) highlights the pitfalls and research opportunities in this domain.

---
