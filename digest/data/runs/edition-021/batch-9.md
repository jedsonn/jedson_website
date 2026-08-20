# Classification batch 9 of 22, edition 21

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-021/batch-9.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7264339`

- title: Code-Generated Tool Orchestration versus Native Function Calling in Stateful Business Workflows: A Multi-Model Benchmark Study
- authors: Abasiono Mbat, Oselumese Agbonrofo, Oladimeji Abaniwonnda, Samuel Oyefusi
- affiliations: not stated
- posted: 2026-08-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7264339
- keyword hits: agentic, claude, gpt-5, large language model, llm

### abstract

Tool-augmented large language model (LLM) agents typically rely on iterative functioncalling loops, yet an alternative paradigm asks the model to emit executable code that orchestrates tools inside a sandbox. We present a reproducible benchmark comparing these two approaches across eight stateful business workflow scenarios with deterministic end-state validation. The harness includes Model Context Protocol (MCP) compatibility adapters, progressive tool discovery, execution rollback, and structured observability traces. Frontier models (GPT-5.3 Codex and Claude Opus 4.6) are fully validated in both modes and decrease the number of aggregate tokens in the code mode by 76.6% and 93.7% respectively. Lower-capability models exhibit retry-heavy behaviour, execution-contract failures, and tool-sequence mismatches that erode efficiency gains. Our central finding is capability-conditioned: code mode yields substantial efficiency and reliability benefits for capable models operating within a well-engineered agentic harness, but these benefits do not generalise uniformly. We provide architectural analysis of sandbox mechanics, tool exposure design, and MCP-to-code translation, positioning code mode as a high-leverage orchestration strategy rather than a universal replacement.

---

## uid: `doi:10.2139/ssrn.7287450`

- title: When RAG Hurts: Retrieval-Augmented Generation Degrades Performance in Metallurgical Root Cause Analysis
- authors: Ahmad Ridwan Fauzi, Sendi  Nugraha Pratama, acep purqon, Yumna  Zahran Ramadhan, Muhammad Ardiansyah
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7287450
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Metallurgical failure analysis requires deep domain expertise to identify root causes from complex material evidence. This study evaluates the capability of large language models (LLMs) to perform automated root cause analysis in metallurgical failure cases, with and without retrieval-augmented generation (RAG). A dataset of 195 failure analysis papers spanning nine metallurgical failure categories was constructed, each containing expert-extracted input narratives and ground truth root cause descriptions. Three configurations were evaluated: non-RAG (no retrieval), default RAG (unfiltered), and filtered RAG (deduplicated corpus), with the non-RAG versus filtered RAG comparison performed across three LLMs. For the primary analysis model (MiMo-v2.5), non-RAG achieved 75.9% CORRECT verdicts versus 63.1% for filtered RAG, a 12.8 percentage point decrease (p

---

## uid: `doi:10.2139/ssrn.7287387`

- title: OpenAI API compatible AI Inference Service support in HPC environment
- authors: Adam Matuš, Tomáš Martinovič, Arif  Görkem Özer, Jakub Konvička, Firat Cekinel, Pinar Karagoz, Ismail  Hakki Toroslu, Jakub Krejčí
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7287387
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Driven by the rise of Artificial Intelligence (AI) and Large Language Models (LLMs), the demand for high-density GPU resources has escalated significantly. High-Performance Computing (HPC) centers possess the necessary hardware, yet their conventional infrastructure and software ecosystems make hosting user-friendly AI services highly complex. This paper presents an innovative inference service designed specifically for HPC environments. By integrating batch scheduling, strategic project pre-allocations, and the High-End Application Environment (HEAppE) middleware, the service exposes a seamless, cloud-like Application Programming Interface (API) for LLMs, which can also be extended for broader AI inference tasks including agentic AI. To support common generative use-cases, such as text-to-text or image-to-text tasks, the service is designed to be fully compatible with the industry-standard OpenAI API. We evaluate the performance of this solution using standardized benchmarks against a bare-metal baseline to demonstrate its minimal orchestration overhead. This service has been developed within the scope of the Horizon Europe project EXA4MIND.

---

## uid: `arxiv:2608.15673v1`

- title: PL-Guard: Probabilistic Logic Reasoning for LLM Guardrails
- authors: Satchit Chatterji, Shihan Wang, Giovanni Sileno, Erman Acar
- affiliations: not stated
- posted: 2026-08-16
- source: arXiv
- link: https://arxiv.org/abs/2608.15673v1
- keyword hits: large language model, llm, prompting, qwen

### abstract

Large language model guardrails can be viewed as policy-consistency problems: a system must determine which policy-relevant facts hold in a prompt-response pair and what those facts imply under a given policy. Common approaches, including policy prompting and LLM-as-a-judge pipelines, often overlap the tasks of semantic grounding and policy reasoning: the model both interprets the prompt-response pair and reasons about whether a policy has been violated. This can lead to unsafe compliance with harmful prompts, or refusals to assist benign ones. To separate grounding and reasoning roles, we propose PL-Guard, a neurosymbolic guardrail architecture. Using a symbolic policy interface consisting of predicates and ProbLog rules, a local LLM grounds prompt-response pairs into predicate probabilities using renormalized True/False token scores, while ProbLog performs explicit probabilistic rule inference over the symbolic policy. On the XSTest benchmark, an offline Qwen-based evaluator finds that PL-Guard with a hand-curated policy reduces unsafe compliance from 22.0% for the base model to 0.5%, and below the 6.0% rate of an LLM-as-a-judge baseline. This comes at the cost of higher over-refusal than the LLM-as-a-judge baseline, 14.4% versus 5.2%. These results suggest that separating neural grounding from probabilistic symbolic reasoning can expose the safety-helpfulness tradeoff while making the guardrail's intermediate reasoning steps explicit and auditable.

---

## uid: `doi:10.2139/ssrn.7299984`

- title: From Semantic Intent to Adaptive Geometric Priors: A Large Language Model-Driven Search Framework for Interactive Pipe Routing
- authors: Chenyi Wang, Zili Wang, Yanru Chen, Shuyou Zhang, Yun Fang, Jianrong Tan, Sijing Chen
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7299984
- keyword hits: chain-of-thought, large language model, large language models, llm, llms

### abstract

Interactive pipe routing requires that designers’ qualitative intentions be translated into geometric guidance without compromising collision avoidance, clearance, or layout quality. Direct coordinate generation by large language models (LLMs) is unreliable in constrained three-dimensional scenes, whereas conventional routing algorithms cannot readily interpret natural-language requirements. This paper presents a semantic-to-geometric adaptive search-domain framework that converts design intent into probabilistic soft geometric priors for subsequent optimization. A dual-agent architecture separates semantic distillation from spatial reasoning: LLM1 maps free-form instructions to standardized engineering commands, and LLM2 infers sparse routing corridors under chain-of-thought supervision. The inferred samples are represented as continuous probabilistic domains rather than mandatory waypoints. Domain-aware Radius Inference for Voxelized Environments (DRIVE) predicts domain scale from voxelized obstacle topology, pipe attributes sampled along the initial pipe path, and path-level descriptors. On held-out reasoning cases, the dual-agent configuration achieves 90.8% exact accuracy, while DRIVE reaches R2​ = 0.976 for radius prediction. In various routing tests, the adaptive domain reduced the number of exploration nodes by up to 48.8% and the number of effective iterations by 32.3% compared to blind search, while maintaining path quality. Compared to fixed waypoints, the adaptive domain still exhibits stronger robustness to displacement guidance. Engineering case studies further validated the effectiveness of search domain-coordinated general, parallel, and branch pipeline routing schemes in ship engine rooms and chemical plant layouts. These results demonstrate that the probabilistic search domain provides a controllable interface between natural language intent and geometry-aware pipeline optimization.

---

## uid: `arxiv:2608.16391v1`

- title: Ventor-QTest: Threat-Model-Driven Verification of Vendor-Hosted LLM APIs
- authors: Xiangfan Wu, Zonghao Ying, Huiyu Wu, Xing Zheng, Huangsheng Cheng, Xiaorong Shi, Jing Guo
- affiliations: not stated
- posted: 2026-08-17
- source: arXiv
- link: https://arxiv.org/abs/2608.16391v1
- keyword hits: agentic, large language model, large language models, llm

### abstract

As large language models become increasingly widespread, third-party providers that deploy open-weight models have become an important part of the ecosystem. Auditing the quality of their inference APIs is therefore an open problem. We formalize hosted model routing as a stochastic process and propose \mbox{\textbf{Ventor-QTest}}, a composite black-box audit that requires no probability information from the target API. Its repeated-request component sends each frozen constrained context to the target multiple times, reconstructs a categorical output distribution from the returned text counts, and reports \emph{average fidelity loss} (AFL) as a null-bias-corrected, within-window mean coarsened-KL statistic. Its long-sequence component uses independent runs to report \emph{extreme fidelity loss} (EFL) through the empirical upper tail of a run-level reference-centered-surprisal statistic. Across three logprob-capable route conditions, AFL shows strong linear descriptive agreement with a logprob-derived coarsened-KL comparator. Across seven route snapshots, 20-run sequence probes reveal route-specific EFL variation. AFL and EFL have little detectable route-level association with GPQA-Diamond accuracy. In contrast, pronounced EFL coincides with a decline in Terminal-Bench pass rate as task exposure increases. This pattern may arise because correctness in long-horizon tasks is more sensitive to extreme fidelity loss. These results motivate reporting AFL and EFL jointly, particularly when auditing long-horizon agentic tasks. The open-source implementation is available at https://github.com/Tencent/AI-Infra-Guard/tree/main/services/api_checker/ventor_qtest.

---

## uid: `doi:10.2139/ssrn.7283098`

- title: LLMs Make Robust Stochastic Optimization Easier: An Agentic Workflow
- authors: Ziyu Wang, Zhuolin Wang, Yi Chen, Zhi Chen, Guodong Lyu
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7283098
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Distributionally robust optimization (DRO) provides a principled framework for decision-making under uncertainty, but its practical use remains challenging. Users must identify uncertain quantities, specify ambiguity sets, formulate worst-case objectives or constraints, and implement the resulting model in solver-compatible code. These barriers limit adoption by practitioners and make DRO difficult to teach and learn. Although large language models (LLMs) offer new opportunities for automated optimization modeling from natural-language (NL) descriptions, existing approaches largely focus on deterministic optimization and often fail to produce reliable DRO formulations and implementations. This paper studies the automatic translation of NL descriptions of problems into mathematical formulations and executable code. We construct an NL-to-DRO dataset through a human-guided reverse-engineering pipeline. Each instance contains three components: an NL description of the DRO problem, an intermediate representation (IR) of the mathematical formulation, and executable code in Robust Stochastic Optimization Made Easy. The dataset covers diverse DRO structures and supports systematic evaluation of automated DRO modeling. We further develop an LLM-based workflow centered on the IR for formulation construction, validation, and implementation generation, supported by a knowledge library built from the dataset (website coming soon). Computational experiments with both closed-source and open-source LLMs show that the proposed workflow substantially improves modeling reliability over direct code generation, achieving success rates of up to 91.1\% for closed-source models and approximately 60\% for fine-tuned open-source models. These results demonstrate that our IR-centered agentic workflow can lower implementation barriers for practitioners, provide reusable instructional resources for educators, and help students connect NL problem statements with rigorous DRO formulations and executable code.

---

## uid: `doi:10.2139/ssrn.7296758`

- title: Multi-Agent AI Systems for Autonomous Software Development
- authors: Yeswanth Kumar Polishetty
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7296758
- keyword hits: agentic, large language model, large language models, llm

### abstract

Autonomous artificial intelligence (AI) agents, Large Language Models (LLAM), and the use of multi-agents are quickly changing the landscape of software engineering by making more software development methods more automated. With the increasing complexity of software systems, there is an increasing demand of intelligent systems that can automatically aid requirements analysis, software design, code generation, testing, debugging, documentation, deployment and maintenance. A promising trend has been to delegate these tasks to Multi-Agent AI Systems which allocate these duties to autonomous agents which communicate, plan tasks, examine the output of other autonomous agents and enhance their software artifacts through iterative improvement. This paper explores the role and capabilities of Multi-agent AI in autonomous software engineering, along with the benefits and challenges in the form of a Systematic Literature Review (SLR) and comparative analysis of recent studies on the autonomous software development using a LLM and multi-agent systems. The results suggest that multi-agent systems can allocate software engineering tasks among specialized agents, which eliminates the reliance on a single AI system and can serve the purpose of requirements analysis, planning, code generation, testing, debugging, code review and documentation (Rasheed et al., 2024; Qian et al., 2024). Examples of such frameworks as ChatDev, AutoGen Studio, AutoDev, CodePori, and Magentic-One show various methods of coordinating agents and performing independent tasks (Tufano et al., 2024; Dibia et al., 2024). Task separation, software quality assurance, and workflow automation can be enhanced with the help of collaborative agent architectures, but their efficiency will largely rely on communication standards, coordination, context management, and evaluation objectives (Talebirad and Nadiri, 2023; Manish, 2024). The common obstacles consist of hallucinated/untrusted code, unreliable inter-agent communication, physical security threats, computational expenses, little human control, and the inability to confidently assess autonomousdevelopment procedures (Suri et al., 2023). In general, Multi-Agent AI has a great potential to transform AI-assisted software engineering to more autonomous development cycles, yet careful validation, proper governance, and meaningful human oversight is a necessary requirement to ensure effective and safe adoption.

---
