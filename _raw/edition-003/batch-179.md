# Classification batch 179 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-179.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7082232`

- title: Faculty orientations toward generative AI in Higher Education: perceptual dimensions, attitudinal profiles, and implications for institutional governance,Evidence from a Single Spanish Public University (UPV/EHU)
- authors: Xabier Gonzalez Laskibar, Naiara Uriarte-Gallastegi, Beñat Landeta‐Manzano, Amaia Mendoza-Larrañaga
- affiliations: not stated
- posted: 2026-07-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7082232
- keyword hits: generative ai, generative artificial intelligence

### abstract

The rapid integration of generative artificial intelligence (AI) in higher education raises fundamental questions about faculty perceptions, academic values, and institutional governance. This study examines how university faculty perceive generative AI across seven dimensions—knowledge, institutional training, benefits, opportunities, risks, sustainability, and ethics—at a Spanish public university (N=458). Using descriptive statistics, full ordinary-least-squares (OLS) regression models, and k-means cluster analysis with multi-seed robustness checks (k=2–5), we characterize attitudinal configurations across faculty. Descriptive results reveal moderate-to-high risk (M= 3.78) and ethics concerns (M=4.02), moderate knowledge (M=3.42), and markedly low satisfaction with institutional training (M=2.44). Regression models explain modest variance (R²= .014–.054); no predictor survives FDR correction, indicating the absence of robust socioprofessional drivers of AI perceptions. Cluster analysis yields three exploratory orientations: Engaged Adopters (47.6%), Normative Skeptics (27.7%), and Pragmatic Minimalists (24.7%), distinguished primarily by risk, ethics, benefits, and opportunities scores. Internal reliability for two dimensions (Risks, α= .45; Opportunities, α= .54) falls below conventional thresholds, representing a measurement limitation addressed here. Governance implications center on differentiated training, inclusive deliberation, and integrity-oriented policy design. These findings derive from a single Spanish public university and should be read as institution-specific, exploratory evidence rather than as generalizable across national higher-education systems.

---

## uid: `doi:10.2139/ssrn.6994358`

- title: Minimal Viable Cognitive Agent (MVCA): Building a glass-box LLM cognitive architecture for testing process theories in Agent psychonomicus
- authors: Jack Chen, Weiheng Xiao
- affiliations: not stated
- posted: 2026-07-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6994358
- keyword hits: large language model, large language models, llm

### abstract

Large language models can reproduce human behavior, but as black boxes: they predict an outcome with no faithful cognitive process behind it. We introduce the Minimal Viable Cognitive Agent (MVCA), a process-faithful cascade of 12 language-model processes grounded in Global Workspace Theory. Unlike existing LLM architectures, it is driven by 104 social and cognitive substrates that direct attention, processing, and judgment. Across 89 consumer and social-psychology experiments, MVCA reproduces main effects on par with state-of-the-art architectures and a persona-tuned digital-twin baseline (0.612 versus 0.603), while uniquely exposing the construct activations behind each prediction. Its processes self-organize into the late-integration hierarchy Global Workspace Theory predicts, and constructs semantically nearer a study's theorized mediator activate more strongly (cross-backbone ρ = 0.32, positive in all 89 studies), showing cognitive fidelity. MVCA is the first language-model architecture of human judgment, or Agent psychonomicus, whose mechanism can be read, measured against theory, and falsified.

---

## uid: `arxiv:2607.07670v1`

- title: Does Bielik Know What It Doesn't Know? Activation Dispersion Separates Entity Familiarity from Factual Reliability Across Model Scale
- authors: Grzegorz Brzezinka
- affiliations: not stated
- posted: 2026-07-08
- source: arXiv
- link: https://arxiv.org/abs/2607.07670v1
- keyword hits: large language model, large language models

### abstract

Large language models hallucinate most about entities they have never seen. We ask whether a model's activations betray entity familiarity before a single answer token is generated, and whether that signal predicts the factual reliability of the answers. On four Polish Bielik models (1.5B-11B parameters), we probe four entity domains (athletes, cities, writers, musicians), each with 42 well-known, 42 obscure-but-real, and 42 fabricated entities addressed by a one-sentence question (504 prompts per model). Two unsupervised, single-forward-pass dispersion measures over post-SwiGLU MLP activations, inverse participation ratio and spectral entropy, separate known from fabricated entities at AUROC 0.95-1.00 across all domains and scales; a supervised linear probe reaches 0.99-1.00. Both clear selection-aware permutation floors of about 0.70-0.74 (empirical p<=1e-3), survive held-out layer selection (0.93-0.99), and persist on real names (known vs. obscure-but-real: 0.96-1.00). The signal transfers across entity types (mean off-diagonal AUROC 0.92-0.99); a matched-template counterfactual shows the only large drops are template-caused, not entity-type effects, and the signal is diffuse across heads. This representational signal is already at ceiling at 1.5B, whereas behavioral factual reliability scales sharply: 0, 2, 10, and 19 of 42 known athletes are answered fully correctly by the 1.5B, 4.5B, 7B, and 11B models under a strict judge. Within known entities, separating correct from hallucinated answers is much harder (probe 0.93; dispersion no better than a first-token-entropy baseline). A five-sample semantic-entropy baseline reaches only 0.71-0.83 at 5x the inference cost. Despite this internal awareness, the models almost never abstain: an audit of 2,520 answers finds 2 refusals and 1 hedge. Entity familiarity and factual reliability are distinct phenomena on different scaling curves.

---

## uid: `arxiv:2607.07760v1`

- title: Adversarial Social Epistemology for Assemblies of Humans and Large Language Models
- authors: Mihnea C. Moldoveanu, Joel A. C. Baum
- affiliations: not stated
- posted: 2026-07-08
- source: arXiv
- link: https://arxiv.org/abs/2607.07760v1
- keyword hits: large language model, large language models

### abstract

We outline an adversarial social epistemology (ASE) for densely interactive communicative landscapes in which public assertions are scaffolded by chains of testimony, inference, institutional certification, and tacit trust. In such landscapes, agents have incentives and affordances to distort, color, omit, fabricate, or strategically under-specify information for private, reputational, rhetorical, or material gains. We argue that these phenomena are not adequately captured by familiar descriptions of epistemic bubbles, echo chambers, or misinformation diffusion. What requires explanation is how communicative agents exploit the commitments and entitlements that normally make scaffolded assertions trustworthy. We provide language that delivers the requisite analysis, outline mechanisms that subvert trust in scaffolded public communications, and outline machinery for auditing and redressing trust breaches arising from subverting the auditability of inferential chains, drawing on epistemic networks, enriched with an inferentialist semantics for interpreting assertions.

---

## uid: `arxiv:2607.07184v1`

- title: Predicting LLM Safety Before Release by Simulating Deployment
- authors: Marcus Williams, Hannah Sheahan, Cameron Raymond, Tomek Korbak, Deng Pan, Peilin Yang, Leon Maksin, Ningyi Xie
- affiliations: not stated
- posted: 2026-07-08
- source: arXiv
- link: https://arxiv.org/abs/2607.07184v1
- keyword hits: gpt-5, llm

### abstract

Pre-deployment safety evaluations aim to inform the downstream risks of releasing a new AI model. Yet most evaluations provide limited evidence about how often undesired model behavior will occur in deployment: they generally have insufficient coverage, are unrepresentative, and are generally recognizable as tests. To address these concerns, we study a simple way to simulate a model deployment: starting from de-identified conversations from a previous model deployment, we hold fixed the initial conversation prefix and regenerate the next response using a candidate model. The resulting responses can then both be audited for novel misalignments and used to estimate the prevalence of model misbehavior before deployment. We evaluate deployment simulation across four GPT-5-series deployments, using registered, outcome-blinded predictions for GPT-5.4 and retrospective analyses of three earlier releases. We find that deployment simulation produces informative estimates of post-deployment misbehavior rates and outperforms baselines based on adversarially selected production data; its evaluation-awareness point estimates were also much closer to production traffic than those from traditional evaluations. We also identify the realism of tool resampling as a central challenge for further improving predictions and share results suggesting that this challenge is surmountable even in complex tool-use settings. Finally, we show that deployment simulation can be seeded from public chat datasets and remain informative about production misbehavior rates, suggesting a path for external researchers to run deployment-grounded evaluations without access to private production logs. Overall, deployment simulation helps evaluators forecast how language models will behave in the real world and supports more quantitative assessment of deployment risk.

---

## uid: `doi:10.2139/ssrn.6933900`

- title: From Tool Calls to Governed Autonomy: Agent OS and ECF for Auditable Agent Deployment
- authors: Jeremy Borden
- affiliations: not stated
- posted: 2026-07-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6933900
- keyword hits: agentic, large language model, prompting

### abstract

A tool call is not a deployment. Large language model agents now call APIs, operate over private context, and trigger external work, including paid work; most frameworks still treat this autonomy as a prompting and tool-access problem. Deployment raises a different set of questions: what may the agent know, what may it spend, who must approve which actions, what evidence supports each action, and where is the receipt? This paper reports, from the operator's seat of a live agent marketplace, an implementation-oriented answer: Agent OS and ECF, the architecture behind the Agoragentic platform. A deployment contract binds goal, budget, tool authority, exposure, and approval thresholds; a transaction network provides discovery, execution, metering, trust states, x402 payment flows, and USDC settlement; ECF supplies bounded, policy-filtered context and read-only evidence reconciliation, with an opensource self-hosted core; and a hierarchical constitution, inherited by every child agent and hashed into receipts, sits above all of it. We state a threat model, machine-check the action-lifecycle invariants, and-unusually for this literature-make every system claim verifiable from the reader's terminal: the catalog, trust states, payment challenges, and redacted receipts cited here are live, anonymous curl commands. We also report honest negative results: supply-side governance held up in production, while organic demand, not infrastructure, is the binding constraint. We pre-register an on-chain falsifiable criterion for the marketplace's demand thesis. The contribution is a systems pattern-launch through contracts, bound by context and policy, review before risky actions, connect every action to receipts, reconcile after execution-with the evidence boundary stated exactly.

---

## uid: `doi:10.2139/ssrn.6937600`

- title: PrefAlign-VLM: Unified Multimodal Preference Alignment with Cross-Modal Encoding and Critique-Based Reward Modeling
- authors: Ryan Brown, Ricardo Bennett
- affiliations: not stated
- posted: 2026-07-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6937600
- keyword hits: large language model, large language models

### abstract

Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities in processing and reasoning across visual, auditory, and textual data, yet aligning these models with human preferences remains a critical and underexplored challenge. Current alignment methods, primarily designed for text-only settings, fail to capture the complex interplay between visual and textual preference signals, and existing reward models suffer from low accuracy, weak generalization, and poor interpretability. In this paper, we propose PrefAlign-VLM, a unified multimodal preference alignment framework that addresses these limitations through three key innovations. First, a Cross-Modal Preference Encoder (CMPE) jointly models visual and textual preference signals via bidirectional cross-attention, enabling coherent cross-modal preference representation. Second, a Critique-Based Reward Model (CBRM) generates interpretable textual critiques of model outputs before assigning preference scores, providing transparency into the alignment decision process. Third, Dynamic Preference Scaling (DPS) adaptively adjusts training sample weights based on preference signal quality, optimizing the utilization of high-quality comparison pairs. We evaluate PrefAlign-VLM on three benchmark datasets spanning image understanding, video reasoning, and multiimage analysis tasks. Our approach consistently outperforms existing alignment methods, achieving 82.4 percent on MM-RLHF, 78.9 percent on MMPref, and 72.1 percent on CV-Arena, establishing new state-of-the-art results for multimodal preference alignment. Ablation studies confirm that each component contributes meaningfully, with CMPE providing the largest improvement. Human evaluation further validates that PrefAlign-VLM produces outputs that are more helpful, honest, and harmless than those of competing methods.

---

## uid: `doi:10.2139/ssrn.7083997`

- title: Green-Curious Investing and GenAI: A Field Experiment
- authors: Leslie A Boni, Amado Mabul, Georgia Acosta, Ray Johnson, Mary Anne Majadillas, Subhra  B. Saha, Rachael Kehoe
- affiliations: not stated
- posted: 2026-07-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7083997
- keyword hits: chatgpt, gemini

### abstract

We conduct a randomized classroom-based field experiment to study the unmediated use of ChatGPT and Gemini to learn about green investing. We examine two decision-critical concepts: greenwashing potential and expected lower average returns. Undergraduate students in financial literacy and business statistics courses are randomly assigned one of three instructional cues immediately prior to their GenAI interaction: greenwashing risk, return tradeoff risk, or neither risk. We find that most students who receive the greenwashing or return tradeoff cues reference the concept in their initial prompts with GenAI and are more likely to report learning about the concept from the GenAI interaction. Only about one-third of students who did not reference the return-tradeoff concept in their initial prompt reported learning about the concept, regardless of whether they used ChatGPT or Gemini. In contrast, among students who did not reference greenwashing in their initial prompt, those using Gemini were significantly more likely to report learning about greenwashing than those using ChatGPT (46% versus 15%). Our research contributes to the literature that examines direct interactions of investors with off-the-shelf GenAI models and their potential to supplement or replace financial advising professionals.

---
