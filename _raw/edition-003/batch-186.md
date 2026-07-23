# Classification batch 186 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-186.answer.json` as a JSON array.

---

## uid: `arxiv:2607.15495v1`

- title: Verbalizable Representations Form a Global Workspace in Language Models
- authors: Wes Gurnee, Nicholas Sofroniew, Adam Pearce, Mateusz Piotrowski, Isaac Kauvar, Runjin Chen, Anna Soligo, Paul Bogdan
- affiliations: not stated
- posted: 2026-07-16
- source: arXiv
- link: https://arxiv.org/abs/2607.15495v1
- keyword hits: large language model, large language models

### abstract

Out of everything the human brain processes, only a small fraction is consciously accessible, in the sense of being available for verbal report, deliberate control, and flexible reasoning. In this paper, we present evidence that an analogous functional distinction has emerged in large language models. Using a new interpretability technique, the Jacobian lens, we identify the representations a model is poised to verbalize at any point in its processing. These representations, which we collectively call the J-space, exhibit the functional properties characteristic of a global workspace: their contents can be reported, deliberately summoned and held, used to carry the intermediate steps of silent reasoning, and passed as arguments to arbitrary downstream computations, while automatic processing such as text parsing and routine inference proceeds without them. The J-space also has structural signatures that global workspace theory associates with conscious access: it carries coherent content only in an intermediate band of layers, holds on the order of tens of concepts at a time, and is broadcast by the model's weights more widely than other representations. These properties make it a practical window into a model's unspoken thinking. In alignment audits, it reveals strategic deliberation, evaluation awareness, and trained-in misaligned dispositions that never appear in the model's outputs. We find that post-training installs the Assistant's point of view in the workspace, and we introduce counterfactual reflection training, which improves behavior by training only what a model would say if interrupted and asked to reflect. These results indicate that language models maintain a small, privileged set of representations bearing some of the functional hallmarks of conscious access, and that decoding these representations sheds light on ongoing cognitive processes.

---

## uid: `arxiv:2607.15202v1`

- title: Self-Evolving Human-Centered Framework for Explainable Depression Symptom Annotation
- authors: Hoang-Loc Cao, Van Pham, Truong Thanh Hung Nguyen, Phuc Truong Loc Nguyen, Phuc Ho, Veronica Whitford, Hung Cao
- affiliations: not stated
- posted: 2026-07-16
- source: arXiv
- link: https://arxiv.org/abs/2607.15202v1
- keyword hits: large language model, llm

### abstract

Annotation quality is a major bottleneck in building reliable and explainable artificial intelligence (XAI) systems for mental health research. In depression-related datasets, labels are often assigned without structured evidence, symptom-level justification, or traceable alignment with the criteria of the Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition, Text Revision (DSM-5-TR), limiting both transparency and downstream model interpretability. We propose a self-evolving, expert-in-the-loop annotation framework for Major Depressive Disorder (MDD) that combines large language model (LLM)-assisted labeling with expert verification. The framework is intended to support the construction of explainable, DSM-5-TR-aligned datasets rather than to perform clinical diagnosis. It operates in three stages: candidate evidence selection from textual records, criterion-level DSM-5-TR analysis, and case-level synthesis that produces label-level diagnostic and severity annotations. A dual-memory architecture, composed of Example Memory and Reflection Memory, is designed to internalize expert feedback and iteratively improve future annotations without retraining. We describe this mechanism and leave its evaluation across multiple feedback cycles to future work. In addition to final labels, the framework exports clinical evidence, reasoning traces, and edit histories, enabling comprehensive auditability. In a pilot study using expert-reviewed samples, the proposed approach improves annotation consistency and explainability while reducing manual revision effort.

---

## uid: `doi:10.2139/ssrn.6990198`

- title: Forecast Accuracy is Not Decision Accuracy: Delegated Overbooking with Generative-AI Agents
- authors: Ziqi Zhong, Yuhang Du
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6990198
- keyword hits: agentic, ai agent, llm

### abstract

Generative-AI systems are beginning to translate customer-level beliefs into operational capacity commitments. We study when a firm should let a foundation-model agent turn post-purchase attendance beliefs into an overbooking action. The setting is general-admission live-event retailing, where demand is sold against an estimated safety capacity and the firm bears deniedadmission and unused-capacity costs. We compare two deployments of the same frontier LLM cores: forecast augmentation, in which the model supplies buyer-level no-show probabilities to a newsvendor optimizer, and agentic replacement, in which the model receives the decision right. Using 110,696 ticketing transactions, 2,022 realized events, 13,440 direct-agent decisions, and identification arms that pin down beliefs, objectives, and capacity statements, we show that the central failure is decision-relevant calibration. Mean-calibrated LLM predictors compress the low no-show tail priced by asymmetric general-admission costs; a mechanically correct optimizer therefore overbooks sharply. Direct agents are often less costly because they act conservatively, but they do not reliably beat a base-rate fail-safe. Same-belief agents usually execute the supplied rule, while unconstrained agents reveal model-specific postures. Cross-validated governance recovers performance mainly by hard-coding the objective or withholding delegation. The implication is to price the capacity decision, not the forecast, and to delegate only after shadow scoring proves that the governed policy beats the fail-safe.

---

## uid: `doi:10.2139/ssrn.7090918`

- title: From Conflict to Convergence: A Taxonomy of Hybrid Econometric-Deep Learning Architectures for Financial Volatility Forecasting (2019-2026)
- authors: Fuli Yang
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7090918
- keyword hits: large language model, large language models

### abstract

Financial volatility forecasting has long been divided between two competing paradigms: the econometric GARCH family, prized for its interpretability and grounding in stylized facts, and deep learning (DL) architectures, prized for their flexibility in capturing high-dimensional nonlinear dependence. This paper provides the first taxonomy-based systematic review of the emerging literature that reconciles these paradigms into hybrid econometric-deep learning architectures. Motivated by the persistent limitations of each approach in isolation-GARCH's rigidity under regime change and high-dimensional inputs, and DL's tendency to overfit and ignore volatility clustering, leverage effects, and fat tails-we argue that the period 2019-2026 constitutes a distinct "convergence window" catalyzed by the Transformer era. Applying PRISMA-style screening criteria to peer-reviewed outlets rated SCI/SSCI Q1/Q2 or ABS 3-star and above, and requiring that eligible studies contain both an explicit econometric volatility component and a deep learning component, we synthesize the literature into three structural paradigms: (A) Pipeline Integration, in which GARCH-derived features feed downstream neural networks; (B) Residual Correction, in which GARCH and DL models operate in parallel and are combined at the output layer; and (C) Parameter Embedding, in which neural networks generate time-varying GARCH parameters within a jointly trained end-to-end system. We find that Paradigm C models consistently deliver the largest and most robust out-of-sample QLIKE and Model Confidence Set gains, particularly during volatile regimes, but at substantial costs to interpretability and computational tractability. We further identify textual sentiment extracted via large language models as the next frontier exogenous driver, particularly within Paradigm C architectures. The review concludes with a research agenda emphasizing standardized benchmarking, regime-aware hybrid design, sentiment-augmented parameter networks, and cross-asset transfer learning.

---

## uid: `doi:10.2139/ssrn.7135544`

- title: The safety–efficacy gap in health-related generative AI: a mixed-methods analysis of public user discourse
- authors: Zhining Yang, Runyuan Pei, Yuyang Zhang, Xingyi Tang, Haoming Ma, Meihua Piao
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7135544
- keyword hits: generative ai, generative artificial intelligence

### abstract

Generative artificial intelligence (GAI) is rapidly becoming an everyday source of health information, yet how the public actually experiences and evaluates this technology remains poorly understood, particularly outside English-language digital ecosystems. We analysed 12,290 publicly accessible user-generated texts posted on two major Chinese platforms, BiliBili and Zhihu, between January 2021 and March 2025, combining computationally assisted thematic analysis with weakly supervised sentiment classification. User discourse was organised into an eight-theme framework spanning functional competency, content fidelity, interactivity, risk and safeguards, and related evaluative dimensions. Negative and affectively intense negative comments dominated the corpus (77.3%) and concentrated in themes concerning interaction quality, content reliability, core functionality and perceived safeguards, whereas appraisals of practical value remained comparatively favourable. We interpret this pattern as a perceived Safety–Efficacy Gap: users acknowledge the usefulness of GAI for accessing health information while withholding trust because of concerns about reliability, source traceability and governance. These findings can inform developers, platform operators, regulators and health educators seeking to align GAI systems with public expectations of trustworthy health information.

---

## uid: `doi:10.2139/ssrn.6984519`

- title: Cloud LLMs, Local Models, and the Case for Human-Bounded Scholarship
- authors: William C. Houze
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6984519
- keyword hits: llm, llms

### abstract

This essay asks where the world is actually putting its compute, its capital, and its trust, and argues that the convergent answer carries a lesson for scholarship. As of mid-2026 the evidence does not show that large models are failing or that scaling has stopped paying; it shows a direction of travel — across the technical substrate, the capital markets, the international landscape, the return-focused analyst class, and the security establishment — toward right-sizing : frontier-scale cloud models reserved for a minority of genuinely hard tasks, with smaller, local, and sovereign models carrying the bulk of practical, sensitive, and high-volume work. Beneath the economics sits an epistemic fact: scaling and retrieval improve fluency, recall, and the provenance a model can display, but they do not reliably close the gap between provenance and veracity. That gap is what human verification exists to close. The prescription that follows is the essay's thesis — a human-bounded, Maestro standard for scholarship in which the human retains intellectual sovereignty and directs the model as an instrument. The claim is calibrated to present evidence and is defeasible: a material advance in scaling, training efficiency, architecture, or a novel compute substrate such as quantum could shift the balance.

---

## uid: `doi:10.2139/ssrn.6991638`

- title: How Americans Spend Their Time Online
- authors: David Lazer, Burak Ozturan, Christo Wilson, David Choffnes, Cassidy Waldrip, Hsiu-Chi Lu, John Wihbey
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6991638
- keyword hits: chatgpt, large language model, llm

### abstract

We examine where people spend their time online, analyzing desktop browsing data collected from the National Internet Observatory (NIO). Key findings include: • A few platforms dominate where we spend our time. The top 10 platforms captured about half (49%) of all online time, with Gmail at number one with 16.4%. • A tiny number of companies dominate where we spend time. Most user attention is funneled through a handful of corporations. Alphabet (Google's parent company) alone accounts for 35% of total browsing time in our sample, followed by Meta (8.9%), Microsoft (5.1%), Yahoo (4.3%), and Amazon (3.0%). These five companies capture more than half of all time Americans spend online on desktop. • Americans spend half their online time on just two things: social media (25.3%) and email (24.9%). • AI is already bigger than news. Large Language Model (LLM) tools, such as ChatGPT, now account for 2.9% of total online time, while news is only 2.5%. • The Web is highly age-segregated. Users over 65 spend 36.7% of their online time on email and 14% on Facebook, versus 11% and 2%, respectively, for users under 30. Older people are still using Yahoo and AOL for email (9%, 2%, respectively), both of which barely register among younger users. The oldest cohort spends 4.7% of their time on news sites, far more than the youngest cohort (1.2%). In contrast, users under 30 spend 13% of their time on YouTube, 9% on Google apps (Docs, Drive, Meet, Classroom, and other Google services excluding Gmail, Search, and YouTube), and 3% on ChatGPT, as compared to 6%, 3%, and <1%, respectively, among the oldest cohort.

---

## uid: `doi:10.2139/ssrn.6992279`

- title: Generative AI Adoption as a Dividend Policy Signal: Evidence from Emerging Market Firms in India and Latin America
- authors: Alfredo Merlet
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6992279
- keyword hits: generative ai, generative artificial intelligence

### abstract

Why would firms that invest in generative artificial intelligence (GenAI) alter their dividend commitmentsand does this signal operate differently across emerging markets with divergent institutional structures? This paper addresses this question by examining the relationship between GenAI adoption and corporate dividend policy in a comparative panel of listed firms in India and Latin America (Brazil, Chile, Mexico, and Argentina) over the period 2020-2024. Drawing on signaling theory, agency theory, and the pecking order hypothesis, we propose a dynamic signaling framework in which GenAI adoption generates a non-linear payout trajectory: an initial reduction in dividends (reflecting investment-phase capital retention), followed by higher payouts as productivity gains materialize. We further hypothesize that institutional quality moderates this mechanism, amplifying the payout effect in markets with stronger governance frameworksnotably India relative to most Latin American economies. The study employs fixed-effects panel data models with lagged specifications and interaction terms. Data on GenAI adoption are constructed via natural language processing (NLP) of annual reports; financial variables are sourced from Compustat Global and Refinitiv. Our findings (illustrative at pre-data stage) contribute to the literatures on AI in corporate finance, dividend policy in emerging markets, and the institutional conditionality of technology adoption effects. This study responds to a documented gap in Scopus-indexed literature: no existing paper examines the intersection of GenAI adoption, payout behavior, and institutional quality across India and Latin America simultaneously.

---
