# Classification batch 358 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-358.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7049518`

- title: AI Premium: Insights from the US Corporate Bond Market
- authors: Mathieu Mercadier, Tianqi Luo, Anh Vu, Lu Xu
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7049518
- keyword hits: chatgpt

### abstract

This paper examines whether sectoral artificial intelligence (AI) intensity is reflected in corporate bond pricing at issuance. Using a sample of bonds issued by U.S. firms between 2015 and 2025, we document an AI premium whereby firms in more AI-intensive sectors issue bonds at higher yield spreads, even after accounting for credit ratings and R&D intensity. Across the four dimensions of the OECD AI-intensity taxonomy, AI use is associated with the largest premium, whereas AI human capital, AI innovation, and AI exposure exhibit weaker or statistically insignificant associations. Medium- and long-term bonds exhibit a significant AI premium, with the largest effect observed for medium-term maturities, while no significant premium is detected for short-term bonds. The difference-in-differences analysis shows that the AI premium increases significantly following the launch of ChatGPT, whereas earlier AI milestones, including AlphaGo and the introduction of the Transformer, are not associated with a comparable change in issuance spreads.

---

## uid: `doi:10.2139/ssrn.7026918`

- title: Procedra: A Source-Supported Software Artifact for Human-in-the-Loop Industrial AI
- authors: Aleksander Shuvalov
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7026918
- keyword hits: large language model

### abstract

Industrial work instructions are often created through document-heavy workflows that require engineers, technologists, supervisors, and safety specialists to coordinate task context, local procedures, source materials, and reviewer decisions. Plain large language model generation is not sufficient for this setting because fluent procedural text can obscure missing information, unsupported assumptions, and accountability boundaries. This working paper presents Procedra, a source-supported software artifact and controlled local-demo prototype for human-in-the-loop industrial AI. Positioned as an early-stage design-science artifact, Procedra transforms task descriptions, technical context, enterprise documents, curated public references, and optional video-derived signals into structured, review-ready work-instruction drafts. The prototype combines schema-validated generation, deterministic fallback behavior, retrieval-based context handling, rule-based quality evaluation, local verification prompts, expert-review questions, version history, workflow decisions, execution checklist evidence, and audit events. The paper contributes a bounded artifact description, a source-supported drafting workflow pattern, and an evidence protocol that separates implementation evidence from customer, field, safety, and compliance validation. It does not claim production deployment, certified compliance, measured productivity gains, or replacement of approved local procedures and qualified expert review.

---

## uid: `doi:10.2139/ssrn.7038158`

- title: It's Not the Technology Why Enterprise AI Fails to Create Value
- authors: Abbas Mistrah
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7038158
- keyword hits: generative artificial intelligence

### abstract

Enterprises have invested heavily in generative artificial intelligence (GenAI), yet the returns remain elusive. Across the most widely cited industry studies of 2025, only a small minority of initiatives produce measurable financial impact, while the large majority stall before reaching value. The dominant public explanation blames the technology-its tendency to hallucinate, its immaturity, or unready data. This paper argues that this explanation is largely mistaken. Synthesizing convergent evidence from three independent 2025 studies and integrating four established research streams-information-systems success and project-escalation research, technology-acceptance theory, behavioral work on algorithm aversion, and the economics of general-purpose technologies-we advance a layered model of GenAI value failure. The model distinguishes three causal layers: selection (which problem is chosen, and who is put in charge of it), organization and adoption (how work is redesigned, and whether people trust and use the system), and execution and technology (tooling, data, and integration). We argue that failures most often originate in the upper, least-scrutinized layer and cascade downward, surfacing as the technical and organizational symptoms practitioners typically diagnose. Because prevailing prioritization practice is dominated by heterogeneous, atheoretical vendor frameworks, the selection layer is precisely where rigor is most lacking. We therefore propose a selection-first framework that evaluates candidate use cases along four theoretically grounded dimensions-value, feasibility, risk, and adoptability-within a gated portfolio logic adapted from new-product-development research. The paper contributes a diagnostic reframing of a widely misunderstood phenomenon and a practical instrument for acting on it, and it sets out an agenda for the empirical validation the framework now requires.

---

## uid: `arxiv:2607.20379v1`

- title: Train the Model, Not the Reader: Decodability Supervision for Verifiable Activation Explanations
- authors: Hiskias Dingeto
- affiliations: not stated
- posted: 2026-07-22
- source: arXiv
- link: https://arxiv.org/abs/2607.20379v1
- keyword hits: qwen

### abstract

Natural-language autoencoders score explanations of hidden activations by reconstruction: an explanation is deemed faithful if the activation can be regenerated from it. The test is structurally insensitive to individual false claims: if flipping a claim does not change the reconstruction, the claim is never penalized. We show the test is passed in two ways, neither faithful. On a released Qwen-2.5-7B verbalizer, explanations reconstruct well above chance while ~2% of specific claims are reconstruction-dependent, so the score tracks gist, not specific facts. Under exact synthetic ground truth, the standard recipe develops co-adapted private codes (false wording the reconstruction depends on) in 5/5 runs, and fixes that leave the target model unchanged do not help. We contribute two audit protocols, the grounded-vs-true cross and the evaluator swap, and RECAP (Readable Encodings via Co-trained Auxiliary Predictors): linear heads trained alongside the target model to keep designated content decodable. On RECAP-trained sandbox models, fresh verbalizers state the designated content truly and the codes vanish, at a +0.001-nat cost. This replicates on a pretrained Pythia-160M: the content becomes reliably probe-decodable, though a fresh verbalizer conveys it only in part (truth 0.44-0.46 vs a near-zero control). For interpretability, high reconstruction does not certify individual claims. For AI safety, RECAP makes designated internal content independently checkable against probes rather than asserted by prose a model can game: an independent probe scores the verbalizer's true claims above its false ones (AUC 0.96, vs 0.82 without RECAP). Against an adversary that edits an explanation to maximize the reconstruction score while lying (suppressing ~87% of its lie penalty), the RECAP probe still flags the lies (AUC 0.95) while the control probe collapses to chance (0.51).

---

## uid: `arxiv:2607.19935v1`

- title: MOF-Sleuth: Tool-Grounded Reward Alignment for Explainable Fine-Grained MOF CIF Auditing
- authors: Yu Liu, Zhiwei Yang, Diandian Guo, Kun Peng, Fangfang Yuan, Cong Cao, Chaozhuo Li, Zhiyuan Ma
- affiliations: not stated
- posted: 2026-07-22
- source: arXiv
- link: https://arxiv.org/abs/2607.19935v1
- keyword hits: llm

### abstract

Large metal-organic framework (MOF) databases support simulation, screening, and machine learning through crystallographic information files (CIFs). Subtle chemical and structural errors in these inputs can compromise downstream results and hinder manual inspection. LLM advances in computational chemistry offer paths beyond predictive screening toward fine-grained diagnosis with evidence-grounded explanations. However, two challenges remain: (i) limited fine-grained attribution: MOF-specific validators and machine-learning models scale detection but provide fixed checks, readiness scores, or coarse labels rather than evidence-grounded explanations; and (ii) unreliable CIF reasoning: direct LLM auditing is costly and unreliable because chemical evidence is implicit across atom-site records and requires geometric, connectivity, occupancy, and charge calculations. Both stem from weak coupling between chemical evidence and language-model explanation. We introduce MOF-Sleuth, a reinforcement-guided CIF auditing agent with two modules: a deterministic Forensic Lab and a Sleuth reasoning engine. The Lab derives composition, geometry, connectivity, occupancy, coordination, and charge evidence, and Sleuth uses this evidence to produce an evidence-grounded explanation, error types, and a binary decision. Reward-guided reinforcement learning (RL) turns tool measurements into chemical explanation-level supervision, rewarding not only the final answer but also cited chemical evidence and evidence-supported diagnoses. We introduce Chemically Grounded Diagnosis (Chem-GD), a metric that assesses whether a correct diagnosis is explained by factual, relevant CIF-derived evidence. Across four benchmarks, MOF-Sleuth establishes state-of-the-art performance among LLM-based approaches and MOF-specific machine-learning methods, demonstrating gains in detection, attribution, and grounded explanation quality.

---

## uid: `doi:10.2139/ssrn.7047158`

- title: Back to Solana Beach Days: Kaypro and the Human-Cognition Standard Before the Predictive LLM Machine
- authors: William C. Houze
- affiliations: not stated
- posted: 2026-07-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7047158
- keyword hits: llm

### abstract

This essay ranges across many scenes of writing, but its argument turns on two of them, set side by side. In the first, dated to the early 1980s, a writer composes book-length prose on a Kaypro portable computer running CP/M and WordStar: the human supplies every word, while the machine registers keystrokes and drives a printer without contributing content of its own. In the second, dated to 2026, a writer issues a prompt and a hyperscale datacenter returns prose, figures, and calculations whose epistemic status the writer is often poorly positioned to confirm. I argue that the difference between these scenes is not primarily a matter of efficiency, nostalgia, or deskilling, but of where formal causation sits and, more decisively, of whether the human can still vouch for—can warrant—what reaches the page. The Kaypro produced zero semantic surplus: nothing in its output supplied wording or substance the writer had not authored. The predictive model produces such surplus by design, and the cost it imposes is a verification premium that, when left unpaid, lets unwarranted content enter the record as settled knowledge. Drawing on my own experience coauthoring two TAB Books manuals on the Kaypro, on the documentary record of the machine preserved at the Smithsonian, and on a contemporaneous writer’s account of the Kaypro as a liberating instrument, I frame the early personal computer as the limiting case of a transparent, pass-through tool and the predictive model as its structural opposite. The Kaypro workflow becomes a benchmark—a human-cognition standard against which the modern human–machine relation can be measured and, where appropriate, found wanting. The standard it names is not that the machine must never supply wording, but that the human must remain the warrant of the result, whether by authoring it or by auditing it. As the disciplined heir to the Kaypro I set the bounded instrument—a small, source-bound language model the scholar runs locally over a curated corpus, here the Maestro–Stradivarius Language Model (MSLM). Opaque in mechanism but bounded in provenance, it admits machine-supplied wording only on terms the human can audit, and so carries the Kaypro’s standard into 2026 by discipline rather than by incapacity. Appendix A sets out, verified against primary sources and cited, a practical path by which a reader may build one. Appendix B then carries that instrument into use, walking one revision cycle in which machine-supplied surplus is audited against an admitted corpus and only what traces to it is kept. That instrument, however, is reached for only at need. Appendix C measures the choice by the scale of the corpus: where the sources can be read in full, an unaided scholar—online search to find, hand and judgment to digest, citation to bind—keeps the standard whole with no language model at all, and is the default; the bounded instrument is warranted only where the corpus outgrows what one reader can hold, and the opaque frontier model at no scale. Appendix C sets out that scale schema and a step-by-step build for the case that warrants it. That landscape is itself the endpoint of a documented drift: Appendix D samples a single national computing-magazine spine from 1980 to 2015 and traces, issue by issue, the migration of warrant off the scholar’s desk—and with it a measurable slide along the theoria–techne gradient, from technique that serves the scholar’s thinking toward technique that performs it.

---

## uid: `doi:10.2139/ssrn.7051578`

- title: The Governance Gap: Contestable AI Institutions Beyond Model-centric Ethics
- authors: Dara Dehghan
- affiliations: not stated
- posted: 2026-07-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7051578
- keyword hits: generative ai

### abstract

Debates about the ethics of artificial intelligence (AI) have been dominated by a model-centric view: if systems could be made more fair, interpretable, robust, and private, AI would align with our values. We argue that much applied AI ethics mis-specifies its primary object. “The AI system” is treated as a bounded technical artefact, when the decisive locus of harm — and therefore of governance — is the institution that embeds it. The harms that animate AI ethics work rarely originate in model weights alone. They arise when statistical systems are woven into hospitals and insurers, courts and police, banks and employers, platforms and public agencies that allocate rights, resources, and coercive power. This misalignment produces a governance gap: responsibility is simultaneously over-individualised and over-abstracted, while the design of contestable, revisable decision processes remains underspecified. We develop a framework centred on contestable AI institutions: socio-technical arrangements designed so that affected parties can understand, challenge, and reshape the pipeline from data collection and modelling through deployment and oversight. The account combines ethical analysis, technical constraints, and emerging legal regimes, and is grounded in case studies in health care, criminal justice, policing, finance, employment, and generative AI. We recast applied AI ethics as an institutional design problem and specify what it would take for AI-supported systems to become contestable in practice.

---

## uid: `doi:10.2139/ssrn.7046079`

- title: Secure Explainable Audit Trails for Workflows in Agentic AI
- authors: Subhasis Thakur
- affiliations: not stated
- posted: 2026-07-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7046079
- keyword hits: agentic, chain of thought

### abstract

An Explainable Audit Trail (EAT) records process execution traces of an agentic workflow, the underlying reasoning behind the agent's decision, and results of audits on the execution traces and validity of agent's reasoning. EAT can enable an organisation to efficiently remain compliant with regulations by presenting its audit results to it. However, current state of the art in EAT for agentic workflows lacks privacy protection of agent's models which can be intellectual properties of the organisation. Exposing audit trails to external entities may facilitate orchestration of attacks on the agent's model. Auditing a complex workflow will require verification of dependencies among tasks as preconditions to execute a task. Further, it is necessary for the audit algorithm to ensure that a process execution trace follows the pre-planned process execution model for security reasons, i.e., audit should include functionality that can check if the agents have deviated from its planned process execution models. In this paper, we build a secure EAT that can address these gaps in the state of the art in EAT for agentic workflows. Our main contribution is the application of zero-knowledge proof on verifying audit procedures. It can prove that audit has validated correctness of chain of thoughts for each task executed by the agents, if the there execution trace at the runtime matches the planned process execution model, and a complete traceability among logs of a complex workflow involving dependencies among the tasks in terms of preconditions. Our solution can enable an organisation to provide a trust-less infrastructure to verify the audit results to external entities such as regulators while not exposing the audit trails. We used lattice-based zero knowledge proof for this procedure which is not only extremely time-efficient but also quantum-safe. We provide an analysis on security and privacy of the EAT procedure. We show experimental evaluation of this EAT procedure with large workflow dataset.

---
