# Classification batch 3 of 20, edition 17

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-017/batch-3.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7150298`

- title: Multi-Agent LLM Collaborative Reasoning and Task Planning for Complex Task Solving
- authors: Wentao Zhang, Tian Liao, Yihui Feng
- affiliations: not stated
- posted: 2026-08-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7150298
- keyword hits: gpt-4, large language model, large language models, llm, llms

### abstract

Complex open-domain tasks require long-range reasoning, controlled decomposition, and reliable tool-mediated execution from large language models (LLMs). Single-agent LLM workflows still suffer from one-perspective planning bias, accumulated errors in long reasoning chains, and weak control over tool invocation. This paper proposes a multi-agent LLM collaborative reasoning and hierarchical task-planning framework for complex task solving. The framework assigns the planner, executor, and verifier to explicit roles and represents each task as a dependency-aware graph with priorities, confidence states, evidence requirements, and repair conditions. To address parameter selection, the priority coefficients are determined on a validation set with the default setting α = 0.35, β = 0.30, γ = 0.25, and λ = 0.10, while the verifier confidence threshold is set to θ = 0.72 after grid-based calibration. A sensitivity test shows that changing each priority coefficient by ±0.10 changes the completion rate by no more than 2.6 percentage points, and varying θ from 0.65 to 0.80 changes answer accuracy by no more than 3.2 percentage points. The shared-memory update function is implemented through typed records, node-level indexes, semantic retrieval, and conflict-aware invocation rules. A unified tool-error taxonomy is also defined, including wrong tool selection, invalid parameters, invalid invocation sequence, execution failure, and inconsistent result integration. Experiments on multi-step logical reasoning, cross-tool orchestration, and open-domain problem solving show that the proposed framework improves task completion by 27.3%, answer accuracy by 19.6%, reasoning accuracy by 22.1%, and factual consistency by 24.8%, while reducing tool error rate by 31.5% compared with a single-agent GPT-4 baseline.

---

## uid: `doi:10.2139/ssrn.7157639`

- title: When the Model Changes: Resilience Engineering Patterns for Production Agentic AI Workflows
- authors: Lavkesh Dwivedi
- affiliations: not stated
- posted: 2026-08-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7157639
- keyword hits: agentic, ai agent, claude, foundation model, large language model, llama, llm

### abstract

Autonomous AI agents built on large language model (LLM) APIs are subject to a class of dependency instability with no direct analogue in traditional software engineering. The upstream model changes, often without notice, and the application breaks in non-obvious ways. Between 2023 and 2026, all major LLM providers deprecated significant model generations: OpenAI retired the Codex family with three days' notice, Anthropic deprecated its claude-2.x and claude-instant series, Google shut down PaLM 2 across both Google AI Studio and Vertex AI, and GitHub Copilot silently transitioned its underlying model multiple times before introducing a Long-Term Support designation in 2026. When a foundation model developer retires a model generation, hosting providers retire it simultaneously: Groq, Together AI, Fireworks, and Replicate all retired the same LLaMA 3.1 variants within weeks of each other, collapsing multi-provider fallback to a single point of failure. This paper characterizes five categories of model change event (announced version updates, silent behavioral drift, forced deprecations, provider substitution, and upstream cascade retirements) and derives five engineering patterns for building agentic workflows that survive them: behavioral contracts evaluated before traffic promotion, provider abstraction layers that normalize API surface differences, shadow testing and canary deployment for safe model transitions, behavioral drift circuit breakers for silent changes, and prompt versioning with explicit model pinning. Pseudocode implementations and implementation tradeoff analysis are provided for each pattern.

---

## uid: `doi:10.2139/ssrn.7189679`

- title: Regenerative Artificial Intelligence: Toward a New Paradigm Beyond Generative Models
- authors: Pitshou Moleka
- affiliations: not stated
- posted: 2026-08-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7189679
- keyword hits: foundation model, generative ai, generative artificial intelligence, large language model, large language models

### abstract

The emergence of generative artificial intelligence represents one of the most significant technological transformations of the twenty-first century. Large language models and multimodal foundation models have demonstrated unprecedented capacities in language generation, image synthesis, programming assistance, scientific discovery, and knowledge production. However, the dominant paradigm of generative AI remains primarily centered on content production, prediction, and optimization. This article argues that the next frontier of artificial intelligence requires a transition from generative capability toward regenerative intelligence. This paper introduces the concept of Regenerative Artificial Intelligence (RAI) as a theoretical framework for understanding artificial systems designed not only to generate outputs but also to enhance the resilience, adaptability, sustainability, and knowledge capacity of the human and ecological systems in which they operate. Building upon research in artificial intelligence, complex adaptive systems, sustainability science, responsible AI, and the emerging field of Noesological AI, the article proposes that intelligence should be evaluated according to its capacity to create long-term systemic value. The paper develops a conceptual model of regenerative AI based on five dimensions: adaptive intelligence, ethical coherence, ecological sustainability, contextual embeddedness, and systemic regeneration. It argues that future AI systems should evolve from tools of automation toward partners in societal learning and planetary problem-solving. Through analysis of current AI applications in healthcare, education, climate science, and governance, the article identifies early empirical evidence of regenerative potential while highlighting major challenges related to evaluation, governance, and implementation. Regenerative Artificial Intelligence therefore represents a shift from asking what AI can generate toward examining what AI can regenerate.

---

## uid: `doi:10.2139/ssrn.7199341`

- title: Signed but Unsafe: Securing Runtime Tool Selection in LLM Agents under Adversarial Metadata Injection
- authors: Basit Ali, Muhammad Raheel Anwar, Tehreem Minhas
- affiliations: not stated
- posted: 2026-08-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7199341
- keyword hits: claude, gpt-4, llama, llm, llms

### abstract

LLM agents increasingly select external tools by ranking natural-language metadata against user intent. Existing supply-chain controls authenticate implementation bytes but not the semantic selection step: adversarial marketplace metadata induces 81-95% attacker-controlled tool selection on frontier LLMs without touching code. We introduce the Capability Manifest Framework (CMF), a structural defence built on one principle: the text a planner uses to discover a tool must differ from the text an attacker can author. We formalise this as metadata-steering resistance (MSR) and prove, under EUF-CMA, that discovery-channel separation is necessary and sufficient for (negl(λ), poly(λ))-MSR, and that CMF composes with postselection defences because it constrains an orthogonal preselection channel. CMF combines four controls: Ed25519/Sigstoresigned capability manifests, SHA-256 artifact binding, a plannervisible signed safe_summary field, and a deterministic non-LLM invocation verifier. In a controlled harness, CMF eliminates metadata steering (100%→0%) at 2.97 ms P95 overhead. Across Claude Sonnet 4.6, LLaMA-3.3-70B, and GPT-4o (n=30 per cell), CMF achieves 0% targeted ASR in every non-adaptive scenario (95% CI upper bound 11.4%; tightened to 3.6% at n=100 on a 50-tool catalogue), reproduced across email, file-operation, and database-query domains (p<10-4). AgentDojo multi-turn evaluation eliminates description-injection attacks (96%→0%) while raising benign utility under attack from 32% to 86%, and a 64-cell ablation shows that no control is redundant. For the distinct case of a compromised signing key, vocabulary linting reduces residual ASR from 73% to 13% (95% CI [5, 29]); transparency-log-based key governance remains the necessary long-term control.

---

## uid: `arxiv:2608.05832v1`

- title: Enhancing Social Intelligence in LLMs with Hierarchical Reasoning and Utterance-Level Goal Rewarding
- authors: Xiaofeng Wang, Kakam Chong, Shuai Xiao, DeXin Kong, Qingyuan Tian, Chen Ju, Xu Yan, Shuai Zhao
- affiliations: not stated
- posted: 2026-08-06
- source: arXiv
- link: https://arxiv.org/abs/2608.05832v1
- keyword hits: gpt-4, large language model, large language models, llm, llms, qwen

### abstract

Large language models (LLMs) excel in structured tasks but struggle with dynamic social interactions, where success requires long-term goal coordination and rapid adaptation. Current methods often apply uniform goal-based rewards to every utterance, overlooking the specificity of objectives at each dialogue turn and failing to account for the rationale of potential strategies. Inspired by the Theory of Planned Behavior, we propose the Think-Strategy-Response (TSR) framework, which decomposes social dialogue into two hierarchical stages: high-level strategic planning and low-level linguistic execution. To optimize TSR, we introduce Linearized Hierarchical Reinforcement Learning with Variance-Gated Rewards (LHRL-VGR), a novel algorithm that dynamically routes rewards - balancing goal completion and strategy adherence - based on the variance of goal achievement scores. Experiments on the SOTOPIA benchmark show that our approach fine-tunes a Qwen2.5-7B agent to surpass the GPT-4o baseline by 7.32% in goal completion success, demonstrating state-of-the-art performance in multi-agent social negotiation tasks.

---

## uid: `doi:10.2139/ssrn.7209078`

- title: A Review of Reward Engineering for Reinforcement Learning-Guided LLM Metaheuristic Generation
- authors: Ali Ghasemzadeh, Armin Khosravi, Mohamad Mirzadi, Mohamadreza Akbari Pour, Seyedali Mirjalili
- affiliations: not stated
- posted: 2026-08-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7209078
- keyword hits: agentic, large language model, large language models, llm, llms, retrieval-augmented

### abstract

Optimisation and search problems such as routing, scheduling, and resource allocation often have very large search spaces. Exact methods quickly become impractical. Heuristics and metaheuristics are widely used, but they are usually designed by hand and require strong domain expertise. This makes them hard to adapt and scale. Recently, large language models (LLMs) have enabled automatic generation of heuristic and metaheuristic code. However, LLMs are often used as static code generators. Reinforcement learning (RL) can guide LLMs to generate, test, and improve algorithms over time. Previous reviews studied related topics, such as LLM code generation, RL for code optimisation, and LLM use in metaheuristics. Most of them focus on code synthesis, compilation efficiency, or heuristic adaptation. In contrast, this review focuses on how RL can train LLMs for metaheuristic generation using structured, multi-objective reward design. We adopt an RL-centric perspective and organise the literature using a unifying conceptual lens, grounded in established formulations, that views algorithm design as both bilevel optimisation and a sequential decision process. Within this lens, we analyse composite reward functions that encourage not only correctness and solution quality, but also faster convergence, lower computational cost, structural novelty, and cross-domain generalisation. We also examine how RL-based training interacts with meta-learning, retrieval-augmented generation, and multi-agent LLM systems, and we present a unified taxonomy of RL interaction modes and LLM roles in the optimisation loop. Finally, we outline a roadmap toward autonomous, self-improving metaheuristic designers and relate this direction to recent progress in agentic AI, LLM reasoning, and code generation.

---

## uid: `doi:10.2139/ssrn.7218206`

- title: Vulnerabilities in Autonomous Execution: A Survey of Security Threats and Defenses in LLM-driven Multi-Agent Systems
- authors: Vincenzo Sammartino
- affiliations: not stated
- posted: 2026-08-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7218206
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are no longer confined to producing text. Equipped with tools and composed into multi-agent systems, they now act on the world with limited human oversight. This shift from generation to autonomous execution transforms the security landscape. While prompt injection against a chatbot yields, at worst, an embarrassing sentence, the same injection against a tool-using agent can result in an exfiltrated database, a fraudulent transaction, or a poisoned message propagating to peer agents. The vulnerability class is not new, but the blast radius is.This article surveys the security of LLM-driven agentic and multi-agent systems from 2023 through early 2026. We contribute a threat taxonomy classifying attacks by entry point, propagation path, and target asset. Using this, we organize four threat families—indirect prompt injection, malicious tool use, inter-agent infection, and memory poisoning—consolidating 44 attack papers into a unified comparison. We review the defensive landscape across five categories (detection, structural separation, execution isolation, information-flow control, and alignment-side hardening) and map defenses to threats to expose coverage gaps.Two findings recur. First, no purely prompt-level defense withstands adaptive attackers; effective security requires constraining what the system around the model is permitted to do, rather than relying on model robustness. Second, multi-agent propagation—the mechanism making agentic compromise qualitatively worse than single-model compromise—is the least defended part of the stack, with almost no deployed frameworks enforcing trust boundaries between cooperating agents. We conclude with a research agenda and a minimal security-reporting standard for agent frameworks.

---

## uid: `doi:10.2139/ssrn.7227566`

- title: Multi-Stage Load Disaggregation with Physics-Constrained Verification andLanguage Model Post-Processing
- authors: Konstantinos Perifanos, Vasilis Michalakopoulos, Efstathios Sarantinopoulos, Elissaios Sarmas, Vangelis Marinakis
- affiliations: not stated
- posted: 2026-08-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7227566
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Non-intrusive load monitoring (NILM) recovers appliance-level consumption from a single building meter, supporting building energy management, occupant feedback and demand flexibility. Accurate disaggregation remains a difficult task, with successive studies pursuing higher performance. In this work, we present a multi-stage disaggregation pipeline that jointly estimates operational states and power draws across six targeted appliances in a single forward pass. The architecture separates state and power detection into two independent tasks before reconciling their outputs into a unified prediction. Furthermore, a compressor specialist handles the fridge-freezer appliance to maximize compressor cycle detection and get accurate signal reproduction. We further study whether Large Language Models (LLMs) can refine disaggregation model output and serve as post-hoc agents. Across benchmark evaluations on the REFIT and UK-DALE datasets, our base model achieves state-of-the-art state detection accuracy with macro F1 0.693 and competitive regression with MAE 16.8, compared to established baselines like NILMFormer, Seq2Point and BERT4NILM. Crucially, our research into LLMs sheds light on potential bottlenecks, revealing that even though fine-tuning can boost LLM action quality, aggregate-only verifiers struggle discerning correct from suboptimal actions, and therefore limit any macro gain, showcasing boundaries in what LLM refinement can do to physical signal disaggregation.

---
