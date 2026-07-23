# Classification batch 125 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-125.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6907841`

- title: Machine Learning for Bug Report Severity Prediction: A Review of Recent Methods and Emerging Trends
- authors: Praveen Kumar
- affiliations: not stated
- posted: 2026-07-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6907841
- keyword hits: large language model, large language models, llm, retrieval-augmented

### abstract

The severity label on a bug report decides which defects get fixed first, so getting it right matters for software maintenance. In practice the label is assigned by hand, usually by whoever files the report, and study after study of open source trackers has shown the same two things: the assignments are inconsistent, and most reports never move off the default level. That observation has driven more than fifteen years of work on predicting severity automatically from the report text. This paper reviews machine learning approaches to the problem, with the emphasis on methods published between 2023 and 2026. Over that stretch the field drifted away from the classical TF-IDF pipeline toward fine-tuned transformers, graph-based models, and most recently large language models paired with retrieval-augmented generation. We sort the literature into five method families, line up representative studies by dataset, features and reported results, and explain why those numbers rarely mean the same thing from one paper to the next.We finish with the problems the newer models have not actually fixed: severe class imbalance, label noise from default severities, weak cross-project generalisation, and the cost and consistency of running LLM-based triage in a real pipeline.

---

## uid: `arxiv:2607.02846v1`

- title: Object-Centric Environment Modeling for Agentic Tasks
- authors: Yiyang Li, Tianyi Ma, Zehong Wang, Yijun Ma, Yanfang Ye
- affiliations: not stated
- posted: 2026-07-03
- source: arXiv
- link: https://arxiv.org/abs/2607.02846v1
- keyword hits: agentic, large language model, llm

### abstract

Large language model (LLM) agents can improve through accumulated experience, but free-form textual memories become difficult to maintain, validate, and reuse as interactions grow. Recent symbolic approaches learn executable skills or programmatic world models, yet often store local procedures or assume simplified dynamics. We propose Object-Centric Environment Modeling (OCM), which organizes experience into an executable object-centric environment model. OCM maintains two connected code bases: object knowledge, which defines environment entities and mechanisms as Python classes, and procedure knowledge, which records reusable interaction patterns that must import and use the object model. OCM works in an online setting: after each episode, OCM reflects on the trajectory, updates both knowledge bases, and verifies that all procedures execute against the updated object model. During future interaction, the agent uses progressive knowledge disclosure to inspect compact code signatures first and read source code only when needed. Experiments show that OCM achieves the best average rank across benchmarks and reduces invalid actions, demonstrating that agents can benefit from building object-centric environment models.

---

## uid: `arxiv:2607.04391v1`

- title: Memory-Orchestrated Semantic System (MOSS): An Auditable Agentic Memory Architecture
- authors: Serge Lacasse, Jérémie Hatier, Alex Baker
- affiliations: not stated
- posted: 2026-07-05
- source: arXiv
- link: https://arxiv.org/abs/2607.04391v1
- keyword hits: agentic, ai agent, llm, retrieval-augmented

### abstract

Long-term memory remains a structural weakness of AI agents. The dominant approach, retrieval-augmented generation (RAG), relies on embedding-based similarity search, which is opaque by construction, difficult to audit, and bounded by the theoretical limits of vector representations. We present the Memory-Orchestrated Semantic System (MOSS), an agentic memory architecture in which the agent drives retrieval over a structured relational database. MOSS is model-agnostic, storage-agnostic, and API-agnostic: it runs on any relational engine, connects to any LLM provider (or to deterministic non-LLM processes), and deploys on any infrastructure, local or cloud. Its retrieval execution is symbolic and reproducible (once a query is formulated, no LLM participates in the retrieval loop) and every step of the system, from indexing to answer formulation, is logged and inspectable, making MOSS auditable by construction. Rather than imposing an external ontology, MOSS derives its conceptual vocabulary from the corpus itself. We report on a longitudinal deployment unique in the agentic-memory literature: a year of continuous production over an individual scholar's working corpus--a conversational corpus reaching back to October 2024 (some 44 million tokens, retroactively indexed) comprising 110,183 segments, alongside 163,494 catalogued documents, 569 inductively derived concepts, 322,662 concept annotations, and eleven metadata graphs totaling approximately five million relations--across four successive infrastructure generations. While the present case is that of a single researcher, the architecture is in no way specific to one person: it serves a team, an institution, or any entity that accumulates knowledge over time. We argue that auditable, sovereign, structurally unbounded memory is a precondition for AI agents intended to accompany a person or an organization over years rather than sessions.

---

## uid: `arxiv:2607.04281v1`

- title: Risk-Constrained Freshness-Aware Semantic Caching for Open-Web Retrieval-Augmented LLMs
- authors: Muhammad Mansoor, Tahir Ahmad, Yeo-Chan Yoon
- affiliations: not stated
- posted: 2026-07-05
- source: arXiv
- link: https://arxiv.org/abs/2607.04281v1
- keyword hits: llm, llms, retrieval-augmented

### abstract

Semantic caching reduces the latency and cost of retrieval-augmented generation (RAG) by serving cached answers to semantically similar queries, but most existing methods do not model the time-varying freshness of open-web evidence. We present FreshCache, a three-tier semantic cache that treats cache reuse as a risk-constrained temporal inference problem: before approving a cache hit, FreshCache estimates the probability that the cached result is stale using a fitted exponential decay model enhanced by a learned MLP, and approves reuse only when that probability falls below a per-tier error budget across answers (epsilon = 0.10), URL lists (epsilon = 0.20), and page content (epsilon = 0.35). This allows the system to degrade gracefully as entries age rather than forcing a binary choice between a stale hit and a full pipeline execution. We introduce FreshCache-Bench, a benchmark of 8,072 base queries across five freshness classes with ground truth staleness labels drawn from real web snapshots at 1, 12, 24 hours, and 7 days after a baseline crawl, expanded to 31,201 queries via paraphrase generation. At the 24-hour evaluation window, FreshCache_MLP achieves 97% search API savings at 0.1% hash-based stale error, and an LLM-judge evaluation on 396 confirmed change pairs shows that only 34.3% of detected content changes actually affect answer correctness, placing true answer-affecting stale error at approximately 0.034%. The rule-based FreshCache achieves 98% search savings at 3.3% stale error under a temporal holdout calibration, outperforming SemanticTTL (14.9% stale, 72% saved), vCache (7.2% stale, 47% saved), and SCALM (5.2% stale, 96% saved). Ablations show the temporal risk gate accounts for an 11.6 point reduction in stale error over similarity-only reuse, and the learned MLP reduces stale error a further 3.2 points over the rule-based model.

---

## uid: `arxiv:2607.04558v1`

- title: EEG-SpikeAgent: Agentic Closed-Loop Program Synthesis for Automated EEG Spike Detection
- authors: Sonali Santhosh, Kelly Shuhong Yu, Eugene Chang, Jonathan Kim, Kie Shidara, Danilo Bernardo
- affiliations: not stated
- posted: 2026-07-06
- source: arXiv
- link: https://arxiv.org/abs/2607.04558v1
- keyword hits: agentic, large language model, llm

### abstract

Automated detection of interictal epileptiform discharges in scalp electroencephalography (EEG) is clinically important, but recent high-performing deep-learning models often trade interpretability for accuracy. We introduce EEG-SpikeAgent, a closed-loop program-synthesis framework that uses a large language model (LLM) agentic system to generate signal-processing features for spike detection in scalp EEG. The system iteratively proposes one deterministic EEG feature module at a time, executes the resulting code on EEG to generate tabular features, evaluates performance via a tabular classifier, summarizes run-level metrics, and feeds structured diagnostics back to the model for refinement. Across iterations, EEG-SpikeAgent proposes and refines candidate signal features and decision rules informed by model performance. We evaluated EEG-SpikeAgent on VEPISET, a public 29-channel dataset of 4-second epochs containing 2,516 discharge-containing and 22,933 non-discharge epochs. Across five-fold cross-validation with a gradient-boosted tree classifier, agent-generated features achieved an area under the receiver operating characteristic curve of 0.935, balanced accuracy of 0.699, F1 score of 0.557, sensitivity of 0.401, and specificity of 0.996 at the default operating point. At an operating point with sensitivity 0.80, mean precision was 0.470 and mean specificity was 0.900. Artifact-aware feature generation improved balanced accuracy and F1 score over spike-only feature search. These results indicate that LLM-based program synthesis can automate EEG feature engineering in auditable and inspectable code-driven manner for clinical and methodological review.

---

## uid: `doi:10.2139/ssrn.7001538`

- title: From Parrots to Murmuration: How Policy and Infrastructure Shape AI Agent Autonomy - A Conditional-Autonomy Framework with the Coefficient γ, the Governance Factor κ, and the Leverage GIL
- authors: Byoungchan Eum
- affiliations: not stated
- posted: 2026-07-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7001538
- keyword hits: ai agent, large language model, large language models

### abstract

Five years after Bender et al. (2021) reframed large language models as stochastic parrots, the evaluative question has shifted from comprehension to autonomy: as models become agents that act on the world, how do we measure how much they act without human help? The leading answer, the Autonomy Index AIx = 1-interventions/steps (AlShikh et al., 2025), inherits two limitations from a half-century of robotics autonomy metrics. It is unconditional on policy: a strict regime makes the same agent look less autonomous, though the difference lies in the rules. And it is agnostic to infrastructure: every intervention is costed identically, when tooling changes per-intervention cost by an order of magnitude. We propose a conditional-autonomy framework closing both gaps-the policy-conditional coefficient γ Π , the economic form C(γ) with infrastructure factor κ, and Governance Infrastructure Leverage (GIL)-and prove four properties, including an EVOI floor exhibiting a κ-paradox: better infrastructure raises the EVOI-justified intervention rate while lowering total cost. We execute the synthetic experiment (N =120,000): the unconditional rate confounds a strict-tooled deployment with a lax ad-hoc one (0.500 vs. 0.501) while γ Π separates them; GIL recovers the planted κ = 12 exactly; the κ-paradox emerges as predicted. We also condition on time context-after-hours latent-harm exposure runs ∼11× business hours at indistinguishable γ Π-and specify the canonicalization and review-quality requirements that make γ reproducible. Autonomy is not an intrinsic agent property but an emergent property of agent, policy, and infrastructure-a murmuration, not a parrot.

---

## uid: `doi:10.2139/ssrn.7082872`

- title: An Interpretable Multi-Hop Evaluation Framework for Dialogue Systems via Chain-of-Thought Reasoning
- authors: Zeyang Liu, Dongsheng Guo, Lixuan Wang, Zhiwei Xu, Zhumin Chen
- affiliations: not stated
- posted: 2026-07-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7082872
- keyword hits: chain-of-thought, large language model, llm, llms

### abstract

Evaluating dialogue quality remains a fundamental challenge in intelligent systems. Traditional reference-based metrics often fail to capture the rich semantic and contextual diversity of valid responses, while recent large language model (LLM)-based evaluators suffer from limited transparency and reliability due to their black-box nature. To address these limitations, we propose a multi-hop reasoning framework for interpretable dialogue evaluation. The proposed approach introduces a structured reasoning–validation–correction loop that guides LLMs to explicitly construct and refine the logical connections between dialogue context and candidate responses. Instead of directly assigning scores, the framework first generates an intermediate reasoning chain, then verifies its consistency, and iteratively corrects potential errors. This design improves both the robustness and interpretability of the evaluation process. We integrate the proposed framework with existing reference-based metrics and conduct extensive experiments on widely used dialogue datasets. Results demonstrate that our approach consistently improves alignment with human judgments, achieving up to 23.0% relative gains in predictive power. Furthermore, the framework provides transparent reasoning traces that enhance trust and usability in real-world evaluation scenarios. This work contributes to the design of intelligent evaluation systems by incorporating structured reasoning mechanisms into automated assessment processes, offering a practical and extensible solution for dialogue system evaluation.

---

## uid: `arxiv:2607.07379v1`

- title: Physics-Audited Agentic Discovery in Scientific Machine Learning
- authors: Diab W. Abueidda, Bilal Ahmed, Panos Pantidis, Mostafa E. Mobasher
- affiliations: not stated
- posted: 2026-07-08
- source: arXiv
- link: https://arxiv.org/abs/2607.07379v1
- keyword hits: agentic, large language model, llm

### abstract

In agentic scientific machine learning (SciML), large language model (LLM) agents can discover surrogate models and select one by an automated score, typically an error metric. A low error, however, does not establish that the predicted fields satisfy the physics that matter for mechanics, such as boundary conditions, superposition, stiffness scaling, or causality. We introduce Physics-Audited Agentic SciML (PA-SciML), a verification-first workflow for agentic SciML discovery. The workflow fixes a scoring evaluator before search, derives reviewable machine-checkable physics requirements, checks each trained candidate on its outputs, and separately searches prescribed input ranges or measured load-history spans for high-violation cases without reference solution fields. A surrogate is reported as verified only under the stated checks. When enabled, the workflow also adds advisory numerical probes before training and tests one modeling change at a time to record which isolated edits are associated with score gains before reuse. In the reported computational-solid-mechanics numerical examples, the static elasticity run selects a surrogate with lower validation error than the error-only baseline while both selected models pass the common linear-elastic checks. In the transient elastodynamics run, an error-only baseline with similar mean error fails a stricter causality check by responding to future parts of the loading history, while the selected surrogate passes the stated checks. The main distinction is per-candidate physics evidence on predicted fields, not a richer aggregate score.

---
