# Classification batch 2 of 20, edition 17

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-017/batch-2.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7181158`

- title: WiDM-LLM: Wireless Decision-Making with Large Language Models for 6G Communication Systems
- authors: Pimchanok Srisuk
- affiliations: not stated
- posted: 2026-08-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7181158
- keyword hits: chain-of-thought, fine-tuning, large language model, large language models, llama, llm, llms, prompting

### abstract

The integration of large language models (LLMs) into wireless communication decision-making has emerged as a promising direction for addressing the complexity, heterogeneity, and dynamism of future 6G networks. However, three fundamental bottlenecks hinder practical deployment: the modality gap between discrete LLM token spaces and continuous wireless signals such as channel state information, the high computational cost of autoregressive inference conflicting with stringent real-time latency budgets, and the scarcity of high-quality annotated communication datasets. We propose WiDM-LLM, an end-to-end decision-making framework that unifies multimodal sensing, task-adaptive prompting, chain-of-thought reasoning, and parameterefficient fine-tuning for 6G wireless systems. WiDM-LLM introduces a multimodal sensing encoder that maps vision, LiDAR, IMU, and CSI inputs into a shared token space through a learned modality translation network, a task-adaptive prompt generator that dynamically fills structured prompt slots from network state observations, a chain-of-thought reasoning engine that executes four verifiable reasoning sub-steps with a physics consistency checker, and a closedloop feedback module that updates the prompt from observed rewards. Parameter-efficient LoRA fine-tuning on LLaMA-3-8B with vLLM acceleration reduces decision latency to 21.3 ms, well within the 5G NR mini-slot budget. On the DeepMIMO benchmark with 10 users and 4 cells, WiDM-LLM achieves a sum-rate of 18.73 bps/Hz and a QoS satisfaction rate of 95.2%, outperforming the strongest baseline MultiAgent-LLM by 4.3% and 1.7 percentage points respectively, while reducing latency from 65.4 ms to 21.3 ms. Additional experiments on three unseen scenarios, scaling up to 20 users, and an auxiliary channel estimation task confirm the generalization and scalability of the framework. Human evaluation by five domain experts further shows that WiDM-LLM produces more rational, fair, robust, and explainable decisions than all baselines.

---

## uid: `doi:10.2139/ssrn.7200918`

- title: Systematic Execution Failures of LLM Delegates in RFQ Markets
- authors: Anqi Peter Li, Ethan Yip, Kundana Kommini, Li Yu Chen
- affiliations: not stated
- posted: 2026-08-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7200918
- keyword hits: gpt-4, instruction-tuned, large language model, large language models, llm, llms, qwen

### abstract

Large language models are increasingly deployed as economic delegates, executing trades, negotiations, and quote acceptances on a principal's behalf. Whether they act in the principal's interest under adversarial menu design, a standard interface in multi-dealer RFQ auctions, has not been characterized. We show that they do not. Across fourteen instruction-tuned model caches (nine open-weight models from 3.8B to 72B parameters, most of them 4-bit quantized, and two frontier snapshots), forced-choice LLM delegates on an RFQ price ladder give up +3.8 to +9.4 basis points of expected execution cost against the least-cost action. Part of that is a calibration artifact rather than a model failure: a delegate that optimally uses the reservation price its own prompt shows still incurs +2.8 to +3.2 bps under the same metric. The LLMspecific excess over that reference is +0.6 to +6.5 bps under the canonical menu ordering, +2.7 to +6.5 across the openweight caches and +0.6 for GPT-4o; reversing the ordering on the two frontier models raises both, GPT-4o's to +1.2. A calibration-free statistic that compares only offered prices, using no outside-option calibration and no rational reference, puts the misranking at +0.4 to +5.4 bps; its sign is forced by the support rule, so what carries information is the size, and it is large: eight of the fourteen give up at least 63% of the loss a delegate ignoring price entirely would take. We formalize the setting as a screening threat model in which the attacker posts a committing menu and the delegate's revealed choice is the leakage channel, prove a bound relating a screening dealer's extractable surplus to the mutual information its menus draw about willingness to pay, and evaluate it: the bound holds on every cache, loosely, with 113× to 1000× slack. A row-level answer-label support audit scores each cache on its complete rows rather than discarding decisive delegates whole, and one sentence of prompt instruction cuts Qwen-2.5-32B's execution harm from +5.83 to +4.96 bps and its dealer extraction by 96%. The support audit fails closed whenever the required response distribution is not observed.

---

## uid: `doi:10.2139/ssrn.7136499`

- title: Metacognitive Multi-Agent Framework for Preserving Critical Thinking in AI-Driven Education
- authors: Vedant Mhatre, Jai Desar, Aadi Singh Chauhan
- affiliations: not stated
- posted: 2026-08-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7136499
- keyword hits: generative artificial intelligence, large language model, large language models, llm, llms, mistral, qwen

### abstract

The rapid integration of Generative Artificial Intelligence (GenAI) and Large Language Models (LLMs) in higher education has dramatically boosted immediate student productivity but introduced severe concerns regarding systemic cognitive outsourcing. Traditional tutoring interfaces often function as directresponse mechanisms, providing immediate, fully formed answers that bypass productive cognitive friction and active student engagement. To resolve this learning-performance paradox, this paper details MAS (Metacognitive AI Scaffolding), a multi-agent instructional framework that models student-AI interaction as a sequential decision-making process over a hidden cognitive state. By combining Bayesian Knowledge Tracing (BKT) to track latent mastery and a Markov Decision Process (MDP) to adapt Socratic interventions, MAS restructures conversational tutoring to balance information leakage against student fatigue. This study expands upon previous theoretical work by executing a live, LLM-backed experimental evaluation using Mistral-14B and Qwen-14B architectures against multiple baseline conditions. Utilizing both a parameterized synthetic student cohort and historical student data traces, the quantitative analysis demonstrates that while direct-response systems foster critical dependency, MAS significantly enhances long-term mastery and independent task completion, as validated by the Cognitive Independence Score (CIS).

---

## uid: `doi:10.2139/ssrn.7135619`

- title: Role-Based Access Control (RBAC) as a Prompt Constraint for Enterprise LLMs
- authors: Kenzie Harris
- affiliations: not stated
- posted: 2026-08-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7135619
- keyword hits: fine-tuning, generative ai, large language model, large language models, llm, llms, prompt engineering

### abstract

The widespread adoption of Large Language Models (LLMs) within enterprise environments introduces a critical challenge: balancing the benefits of broad generative AI capabilities with the stringent need for data security, regulatory compliance, and operational integrity. Current approaches to securing LLM interactions primarily rely on input filtering or output sanitization, which are often reactive and fail to enforce dynamic, context-aware permissions. This research proposes a novel framework that integrates Role-Based Access Control (RBAC) principles directly into the prompt engineering and inference pipeline. We conceptualize RBAC not merely as an authentication layer, but as a proactive, semantic constraint on the LLM's generation process. Our framework dynamically constructs system prompts and instruction sets based on a user's authenticated role, effectively anchoring the model's behavior to a predefined set of permissible actions, data domains, and response formats. By constraining the LLM's cognitive space at the point of inference, we demonstrate that it is possible to enforce finegrained authorization policies without fine-tuning the underlying model, thus preserving performance while drastically reducing the risk of privilege escalation, sensitive data leakage, and unauthorized knowledge synthesis. Through a series of experiments involving role-specific prompt templates, dynamic contextual memory, and policy-enforcing pre-processing, we evaluate the system's efficacy across key metrics including security compliance, response accuracy, and operational efficiency. The findings indicate that RBAC-as-a-prompt-constraint offers a robust, scalable, and model-agnostic solution for deploying LLMs in high-stakes business environments, establishing a new paradigm for enterprise AI governance.

---

## uid: `arxiv:2608.01046v1`

- title: DeBERTa-Sentinel: Toward Transparent and Trustworthy Detection of AI-Generated Text
- authors: Muhammad Yousaf Rehman, Muhammad Islam
- affiliations: not stated
- posted: 2026-08-02
- source: arXiv
- link: https://arxiv.org/abs/2608.01046v1
- keyword hits: claude, large language model, large language models, llama, llm, llms

### abstract

The rapid spread of large language models (LLMs) across the web raises concerns about misinformation, academic integrity, automated content manipulation, and risks to vulnerable online communities. Existing transformer-based detectors, such as GPT-Sentinel, show promise but struggle to generalize to diverse model outputs and paraphrasing attacks, limiting their role in building trustworthy web ecosystems. This work introduces DeBERTa-Sentinel, a responsible AI-generated text detection framework leveraging DeBERTa-v3's disentangled attention to capture subtle structural irregularities in synthetic content. A central design principle is transparency: unlike black-box commercial detectors, DeBERTa-Sentinel exposes token-level explanations of its decisions, enabling affected stakeholders journalists, educators, and platform trust and safety teams to audit, challenge, and contextualize detection outcomes. Using the GLC-AIText dataset of 28,057 human and LLM-generated samples (GPT, LLaMA, and Claude) with a 60-20-20 split, DeBERTa-Sentinel achieves 98.21\% validation accuracy and surpasses the RoBERTa-Sentinel baseline from NeurIPS 2025, achieving 97.53\% test accuracy, 95.89\% precision, 99.33\% recall, and 99.53\% ROC-AUC, and maintaining a 0.665\% false negative rate. The model's interpretability reveals linguistic markers such as academic phrasing and formal transitions associated with synthetic text, directly supporting stakeholder needs for verifiable, auditable content-authenticity decisions. By advancing responsible detection methods that reduce bias and enhance explainability, DeBERTa-Sentinel promotes trustworthy, ethical, and human-centric AI systems. Code and data are available at https://github.com/Galileo-Galili/HUMAN-VS-AI-TEXT-DETECTION.

---

## uid: `doi:10.2139/ssrn.7149198`

- title: GIT-DPO: Gradient-Informed Token-Weighted Direct Preference Optimization for LLM Alignment
- authors: Saimir Gora
- affiliations: not stated
- posted: 2026-08-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7149198
- keyword hits: large language model, large language models, llama, llm, llms, mistral, qwen

### abstract

Direct Preference Optimization (DPO) has emerged as a popular alternative to Reinforcement Learning from Human Feedback (RLHF) for aligning Large Language Models (LLMs) with human preferences, eliminating the need for explicit reward modeling. However, DPO and most of its variants treat all tokens in a response uniformly during preference optimization, assigning equal optimization pressure to every token regardless of its actual contribution to the preference judgment. This uniform treatment is suboptimal because only a small subset of tokens, such as factual claims, safety-critical terms, or key instruction-following phrases, typically determines the preference label, while the remaining tokens act as noise that dilutes the optimization signal. We propose GIT-DPO, a novel token-level preference optimization framework that combines two complementary innovations: a gradient-based token attribution mechanism that dynamically computes fine-grained importance weights by measuring the sensitivity of the DPO loss to perturbations in each token's log-probability, and a contrastive dual-pair loss that simultaneously pulls the policy toward preferred responses, pushes it away from dispreferred responses, and regularizes low-importance tokens toward the reference model. Extensive experiments on Al-pacaEval 2.0, Arena-Hard, and MT-Bench across three backbone LLMs (Llama-3-8B-Instruct, Mistral-7B-Instruct, Qwen2.5-7B-Instruct) demonstrate that GIT-DPO consistently outperforms nine strong baselines including DPO, SimPO, TDPO, ORPO, KTO, ConfPO, Selective-DPO, and AlignDistil. On Llama-3-8B-Instruct, GIT-DPO achieves a length-controlled win rate of 22.84 percent on AlpacaEval 2.0, outperforming the strongest baseline by 2.74 percentage points, while converging 1.5 times faster than standard DPO with only 5 to 8 percent additional training time per step.

---

## uid: `doi:10.2139/ssrn.7180420`

- title: An Empirical Evaluation of LLM-Augmented SAST for False Positive Mitigation in Financial Core-Banking Systems
- authors: Martin Gunner, Mckenzie Curtis
- affiliations: not stated
- posted: 2026-08-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7180420
- keyword hits: gpt-3, gpt-4, large language model, llama, llm, llms

### abstract

Static Application Security Testing (SAST) tools in financial core-banking systems generate excessive false positives, overwhelming security teams and undermining DevSecOps efficiency. This paper empirically evaluates Large Language Model augmentation for false positive mitigation in this high-stakes domain. Drawing on experiments conducted throughout 2024, we assess proprietary and open-source LLMs-including GPT-4o, GPT-3.5 Turbo, and Llama 3.1 70B-as post-processing triage layers for SAST findings across benchmark datasets and real-world banking codebases. Our results show that hybrid LLM-SAST approaches achieve F1 scores of 0.91-0.95, significantly outperforming standalone SAST (0.10-0.55) and independent LLM analysis (0.61-0.68). GPT-4o demonstrates the strongest performance, correctly identifying 80 of 128 false positives while preserving 100% true positive detection. Effectiveness depends critically on the precision of provided code context, with performance degrading substantially when context is incomplete. We propose a practical architectural framework for deployment in regulated financial environments, addressing compliance, data sovereignty, and human-in-the-loop validation requirements. This work provides empirical guidance for financial institutions seeking to reduce alert fatigue while maintaining rigorous security standards in core-banking systems.

---

## uid: `doi:10.2139/ssrn.7217223`

- title: TraDeGen: A Translation-Detection-Generation Framework for Mitigating Knowledge-Conflicting Hallucinations in Java to C\# Code Translation
- authors: Bhargav Anantha, Umamaheswara Sharma B
- affiliations: not stated
- posted: 2026-08-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7217223
- keyword hits: fine-tuning, large language model, large language models, llama, llm, llms

### abstract

Context: Large Language Models (LLMs) have advanced in automated code generation and cross-language translation. However, they frequently suffer from hallucinations, where generated code deviates from intended functionality, factual knowledge, or programming context. These errors, including misuse of APIs, undeclared variables,invoking wrong APIs and logical inconsistencies, pose critical challenges to the reliability of LLM-based code translation systems.Objectives: This work addresses the problem of detecting and mitigating knowledge-conflicting hallucinations in Java-to-C# code translation. In addition to that, the objective is to create a publicly available hallucination-aware dataset.Methods: We have created a novel dataset by injecting controlled, context-aware hallucinations into parallel Java and C# code pairs. The injection process combines pattern-guided analysis with LLM-based transformation to generate realistic and structurally consistent errors. A multi-stage framework called - Translation-Detection-Generation - is proposed, consisting of three components: a translation model for Java-to-C\# conversion, a classification model based on for multi-class hallucination detection, and a correction model for generating refined code. The framework employs an iterative feedback mechanism, where detected hallucinations are iteratively corrected through multiple refinement cycles.Results: Experimental evaluation carried across multiple Code-based LLMs such as CodeT5+, PLBART, CodeLLaMA and CodeBERT using the proposed pipeline. Among the tested architectures, encoder-decoder models such as CodeT5+ and PLBART have better translation and correction ability than encoder-only and decoder-only models. In particular, fine-tuned CodeT5+, when employed in the proposed architecture, outperformed the same without fine-tuning with 0.56 points in terms of CodeBLEU. A similar results can be observed using the measures such as N-gram, Syntax, and Dataflow for the other models as well.Conclusion: If we detect a correct hallucination type, and if we employ the hallucinated code as a prompt then, the fine-tuned models can generate context-aware codes by iteratively removing the hallucinations.

---
