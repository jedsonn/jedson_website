# Classification batch 331 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-331.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7044782`

- title: A Mechanistic Generative Framework for Sparse Data Dynamics in Engineering Systems
- authors: Shan Tang, Ziwei Cao, Zhenling Yang, Jiachen Guo, Yicheng Lu, Wing Kam Liu, Xu Guo
- affiliations: not stated
- posted: 2026-07-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7044782
- keyword hits: generative artificial intelligence

### abstract

High-fidelity mechanical data for analyses involving extreme operating conditions are notoriously scarce, as both experimental and numerical simulations are prohibitively expensive. This data bottleneck has limited the efficacy of Generative Artificial Intelligence (GAI) in specialized engineering domains. To address this, the Continuum Mechanics (CM)-GAI theory, a mechanics-informed distribution transport framework that enables the generation of robust mechanical response distributions from limited training datasets, is proposed. By interpreting probability evolution in feature space as the deformation of a continuum body, our method embeds mass-conservation and momentum-balance constraints directly into the transport dynamics. This allows the model to learn complex probability flows with minimal data, yielding accurate predictions across unseen operating regimes, including varied temperatures, strain rates, and impact velocities. The effectiveness of CM-GAI is demonstrated through constitutive law modeling, part-scale thermo-mechanical response prediction, and the transient Taylor rod impact problem. These results confirm that mechanics-informed distribution transport provides a powerful, physics-consistent generative framework for mechanical systems in data-scarce environments.

---

## uid: `doi:10.2139/ssrn.6912299`

- title: Insufficient Scale: The Scaling Hypothesis and Popper’s Line of Demarcation The Death of the Scientific Method in Frontier AI Labs
- authors: William C. Houze
- affiliations: not stated
- posted: 2026-07-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6912299
- keyword hits: large language model, large language models

### abstract

This essay applies Karl Popper’s criterion of demarcation to the contemporary claim that artificial general intelligence (AGI) will emerge from the continued scaling of large language models. The argument is not that AGI is impossible—a claim that would commit the mirror-image error of unfalsifiability—but that the scaling-to-AGI hypothesis, in its present rhetorical form, fails the demarcation criterion on two distinct counts. First, its target is un-operationalized: there exists no agreed metric stating what observation would constitute the program’s failure, so its goalposts are not fixed but ambulatory. Second, the standing explanation for every shortfall—“insufficient scale”—functions as an inexhaustible ad hoc rescue, the conventionalist twist by which Popper distinguished pseudo-science from science. The analytic center of the essay is the asymmetry between induction and deduction: the empirical scaling laws are inductive regularities drawn from past loss curves (the many to the one) and cannot underwrite a deductive guarantee about a qualitatively distinct endpoint (the one to the many). What survives the demarcation failure is not a synthetic mind but a durable, high-utility instrument—the Swiss Army knife of unstructured data. A reflexive coda notes that the present critique was itself elicited through dialogue with such an instrument, whose reflexive flattery furnishes corroborating rather than contradictory evidence.

---

## uid: `doi:10.2139/ssrn.7051341`

- title: Detecting, Explaining, and Auditing Account Hijacking in Cloud Audit Logs with a Fine-Tuned Small Language Model
- authors: Daniel  Martins Ferreira, Duarte  Rainho Santos, Luís  Carlos Afonso, Osvaldo  da Rocha Pacheco, Joao Rafael Almeida
- affiliations: not stated
- posted: 2026-07-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7051341
- keyword hits: llama

### abstract

A compromised cloud account produces events that are individually ordinary; what betrays it is the break from the account's own history. We build a streaming UEBA detector that fuses four calibrated, per-account behavioral signals on CLUE-LDS, a 50.5-million-event corpus of real cloud file-sharing audit logs, and detects 63% of injected hijacks against 48% for the published baseline at its own operating point. Each flagged user-day is explained by a Llama-3.2-1B model fine-tuned on supervision derived deterministically from the detector's own signals, which writes a structured verdict and a grounded rationale. We then audit that deployed scorer with an oracle-free counterfactual: for each alert we compute the minimal edit to the behavior document that flips it benign on the real scorer, exact because the per-account normalization is monotone, with no human label and no surrogate. Over 4,860 distinct alerts the edit exists for 99.2%, yet the decision is overdetermined; no scored signal is ever strictly necessary, 73.5% of flippable alerts have no single necessary lever, and the behavior embedding an account-takeover rationale invokes is never the largest contributor. Token grounding stays near 1.0 across four explainers while the credited driver disagrees with the counterfactual. Acting on the audit, reweighting, re-ranking, and gating the four signals do not improve detection because the decision is overdetermined, but a cross-account identity signal the audit points to lifts true-positive rate at a matched false-positive rate from 0.64 to 0.70 on seeds 1–10, and attaching the counterfactual to the explanation raises judged triage usefulness to 40.0%.

---

## uid: `arxiv:2607.03510v1`

- title: CAGE-1: Control, Assurance, and Governance Evaluation for Enterprise Agentic AI
- authors: Roopam W. Sure
- affiliations: not stated
- posted: 2026-07-03
- source: arXiv
- link: https://arxiv.org/abs/2607.03510v1
- keyword hits: agentic, retrieval-augmented

### abstract

Enterprise artificial intelligence is moving from experimentation into operational workflows. Early programs focused on model access and retrieval-augmented generation, but enterprises are now beginning to deploy agents that plan, retrieve, remember, call tools, update systems, and coordinate work across applications. This changes the evaluation problem. Leaders are no longer asking only whether an answer is accurate or fluent. They need to know who authorized an action, which policy applied, whether evidence was current, whether memory was valid, whether a tool call was permitted, whether the decision can be replayed, and whether the agent can be stopped before it creates business impact. This paper introduces CAGE-1: Control, Assurance, and Governance Evaluation for Enterprise Agentic AI. CAGE-1 is an evaluation framework for deciding whether enterprise agents are ready for deployment. It evaluates authority, policy enforcement, retrieval quality, memory integrity, tool safety, auditability, human oversight, conflict handling, safe failure, Prebind Assurance, operational readiness, and business fitness. CAGE-1 introduces Prebind Assurance to describe the evaluated ability to prove that an agentic action is controlled before it becomes binding, effective, or operationally consequential. The framework tests whether a proposed action is admitted, held, narrowed, refused, escalated, quarantined, or made non-effective before protected consequence forms.

---

## uid: `arxiv:2607.19396v1`

- title: CrackedPDFs: A Controlled Benchmark for Hidden Prompt Injection in PDFs
- authors: Pukaphol Thienpreecha
- affiliations: not stated
- posted: 2026-07-03
- source: arXiv
- link: https://arxiv.org/abs/2607.19396v1
- keyword hits: llm

### abstract

Document-based LLM systems often flatten a PDF before guardrails inspect it. That step can discard evidence that an instruction was never visible to the user. We introduce CrackedPDFs, a controlled benchmark for hidden prompt injection in PDFs. The benchmark contains 29,322 generated PDFs from 4,983 base docu ments. It includes 9,774 injected files and 19,548 benign or matched-confounder files. We evaluate PromptGuard and a rule baseline. We also evaluate structural only learned models and a sanitized hybrid detector. The evaluation uses held-out provenance splits and paired benign-confounder controls. It also uses label-shuffle checks and shortcut audits. On a 2,919-document held-out test set, the hybrid de tector reaches 0.960 F1. ROC-AUC is 0.998 and PR-AUC is 0.997. It also ranks injected files above matched benign confounders in 95.9% of 973 pairs. Prompt Guard has low recall when given extracted text only. Structural-only learned mod els are weak under paired controls. A text-only TF-IDF model reaches perfect held-out scores but fails shortcut audits. These results show that document-aware hybrid detection is useful under controlled paired evaluation. They do not show broad real-world robustness or reliable cross-family generalization.

---

## uid: `arxiv:2607.02944v1`

- title: A Precedent-Guided Co-Scientist for Side-Effect-Aware Drug Redesign
- authors: Yujin Kim, Charmgil Hong
- affiliations: not stated
- posted: 2026-07-03
- source: arXiv
- link: https://arxiv.org/abs/2607.02944v1
- keyword hits: llm

### abstract

We propose PRECEDE, a precedent-guided co-scientist for side-effect-aware drug redesign that revises a parent compound to mitigate a specified side effect while preserving therapeutic function. Rather than isolated molecular generation, PRECEDE frames redesign as evidence-grounded reasoning over drug--side-effect associations, biomedical knowledge graphs, and precedents of safety-driven optimization, coordinated by an LLM orchestrator with explicit policies and human-review checkpoints. We position PRECEDE as a human-supervised AI-for-science workflow in which hypotheses remain auditable, falsifiable, and bounded by prior pharmacology.

---

## uid: `arxiv:2607.02932v1`

- title: PromptPET: Privacy-Utility Optimized Prompt Obfuscation
- authors: Ke Yang, Olivia Figueira, Umar Iqbal, Athina Markopoulou
- affiliations: not stated
- posted: 2026-07-03
- source: arXiv
- link: https://arxiv.org/abs/2607.02932v1
- keyword hits: llm

### abstract

Privacy is an important challenge when users interact with AI chatbots, since users may share sensitive information, explicitly or implicitly, and AI chatbots can use this information for user profiling. In this paper, we aim to protect user privacy via a user-side mechanism that transforms sensitive information in a user prompt, while preserving enough information to elicit a useful response from the chatbot. This approach faces an inherent tradeoff between protecting privacy (i.e., avoiding profiling) and preserving utility (i.e., getting personalized and task-specific responses). To that end, we consider, evaluate, and compare four different obfuscation actions, namely redaction, abstraction, replacement, and a novel noising/denoising scheme that we introduce. Additional novel insights include: utilizing a data type taxonomy to both identify and obfuscate sensitive information and explicitly taking into account the utility of chat responses in making the obfuscation decision. First, we systematically optimize and evaluate each obfuscation action independently in terms of the privacy-utility tradeoff it achieves. Second, we propose PROMPTPET, an LLM-based agent that selects the best obfuscation action for each sensitive part of the prompt, using a reinforcement-learning inspired rule optimizer, applied for the first time in this context. Using a real-world chat dataset, we show that PROMPTPET matches the best privacy-utility tradeoff attainable by any single obfuscation action and significantly outperforms prior state-of-the-art approaches.

---

## uid: `doi:10.2139/ssrn.7052021`

- title: Secure Explainable Audit Trails for Workflows in Agentic AI
- authors: Subhasis Thakur
- affiliations: not stated
- posted: 2026-07-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7052021
- keyword hits: agentic, chain-of-thought

### abstract

An Explainable Audit Trail (EAT) records process execution traces of an agentic workflow. EAT can enable an organisation to efficiently remain compliant with regulations by presenting its audit results to it. However, current state of the art in EAT lacks privacy protection of agent's models which can be intellectual properties of the organisation. Exposing audit trails to external entities may facilitate orchestration of attacks on the agent's model. Auditing a complex workflow will require verification of dependencies among tasks as preconditions to execute a task. Further, it is necessary for the audit algorithm to ensure that a process execution trace follows the pre-planned process execution model for security reasons, i.e., audit should include functionality that can check if the agents have deviated from its planned process execution models. In this paper, we build a secure EAT that can address these gaps in the state of the art in EAT for agentic workflows. Our main contribution is the application of zero-knowledge-proof on verifying audit procedures. It proves the audit has validated correctness of chain-of-thoughts, the execution trace at the runtime matches the planned process execution , and complete traceability among logs of a complex workflow involving dependencies among the tasks in terms of preconditions. Our solution provides a trust-less infrastructure to verify the audit results to external entities while not exposing the audit trails. We used lattice-based zero knowledge proof for this procedure. We provide an analysis on the EAT procedure. We show experimental evaluation of the EAT with workflow dataset.

---
