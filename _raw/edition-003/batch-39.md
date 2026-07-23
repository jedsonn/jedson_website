# Classification batch 39 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-39.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6616078`

- title: Predicting the Next Words From Shannon's Entropy to Large Language Models
- authors: Joerg Osterrieder
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6616078
- keyword hits: claude, gemini, gpt-4, large language model, large language models

### abstract

In 1948, Claude Shannon sat in his office at Bell Labs and played a game. He asked colleagues to guess the next letter in a passage of English text, one letter at a time, and recorded how often they guessed correctly. The experiment was simple, almost playful, but the insight it yielded was anything but: the structure of a language can be measured by how predictable it is, and any system that predicts well must, in some deep sense, understand the patterns that make the language what it is. Shannon was not trying to build a chatbot or a translation engine. He was trying to quantify information. Yet the task he chose, predicting what comes next, turned out to be the same task that, seven decades later, would drive the most powerful artificial intelligence systems ever constructed. GPT-4, Claude, Gemini, and their successors are all, at their mathematical core, next-word prediction machines. They estimate P(w_next | w<t) over vocabularies of tens of thousands of tokens, and they do it well enough to write code, summarize legal briefs, tutor students in calculus, and carry on open-ended conversations that pass casual inspection as human. The distance from Shannon’s letter-guessing experiment to a frontier large language model is enormous in engineering terms, billions of parameters, trillions of training tokens, thousands of GPUs, but the conceptual distance is surprisingly short. This book is about that distance: the ideas, the mathematics, and the engineering that connect a probability distribution over the next word to the full sweep of modern natural language processing.

---

## uid: `doi:10.2139/ssrn.6616122`

- title: Layered Convergence in Autonomous Agent Memory: A Multi-Model Cognitive Architecture for Persistent Recall in Long-Running LLM Agents
- authors: Lance Harris
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6616122
- keyword hits: large language model, large language models, llm, llms

### abstract

Autonomous agents built on large language models (LLMs) operate under a structural limitation that constrains their utility in sustained, multi-domain environments: each session begins with no episodic, procedural, or declarative memory of prior sessions. Existing memory augmentation systems address this limitation through single-model approaches, including vector-based extraction (Mem0), temporal knowledge graphs (Zep/Graphiti), multi-strategy retrieval (Hindsight), OS-inspired tiered management (Letta/MemGPT), and framework-coupled recall (LangMem), each optimizing for one category of recall while leaving others unaddressed. This paper presents a multi-model cognitive architecture in which five complementary memory systems operate concurrently: (1) identity-prompt memory providing behavioral continuity via session-loaded configuration files; (2) structured constraint memory enabling programmatic policy enforcement with audit trails; (3) vector-enhanced semantic memory combining BM25 keyword matching with cosine-similarity search, temporal decay, and maximal marginal relevance re-ranking; (4) relational learning memory closing feedback loops between expert recommendations and their real-world outcomes; and (5) a hierarchical temporal knowledge graph organized into domain-scoped partitions with cross-domain tunnels and dynamic context assembly. Each model was introduced to address a specific failure mode observed during eight weeks of production deployment, and each operates additively without replacing its predecessors. A combinatorial ablation study across all 32 possible subsets of the five models, totaling 3,520 evaluation runs across eight capability dimensions, validates the architecture using Shapley value decomposition. Three findings stand out. First, only two of the five models carry measurable weight under structural evaluation: Model II accounts for 104% of constraint enforcement capability, and Model V accounts for 100% of all retrieval capability, while Models I, III, and IV show near-zero contribution, an expected result given the evaluation's routing through constraint-check and palace-search pathways. Second, upgrading the constraint checker from keyword matching to semantic rule detection raised constraint enforcement from 59.8% to 73.3%, with Model II's Shapley value increasing from 0.286 to 0.430. Third, two new evaluation dimensions reveal previously unmeasured contributions: semantic recall scenarios show Model III (vector search) providing independent recall value (Shapley 0.025, 25% of total), and cross-model flow scenarios confirm that Models II and V contribute additively with zero interaction. The full architecture achieves 80.0% on factual recall with zero policy violations observed across nine weekly advisory council cycles in production. Constraint enforcement, feedback-loop learning, and dynamic context assembly are not present in any evaluated commercial or open-source memory system. The architecture was deployed without modifying the host platform's source code, suggesting portability across agent frameworks.

---

## uid: `doi:10.2139/ssrn.6630758`

- title: INOCULATING CITIZENS AGAINST SYCOPHANCY IN LARGE LANGUAGE MODELS
- authors: John Marvel, Sangwon Ju
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6630758
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models are systematically sycophantic, validating users' prior beliefs rather than challenging them. As AI systems increasingly shape how people understand, evaluate, and relate to their government, sycophantic LLMs that reinforce rather than challenge anti-government sentiment threaten trust in public institutions, democratic competence, and the civic health of the American polity. Drawing on psychological inoculation theory, we report results from a pre-registered experiment testing whether sycophancy disclosure can mitigate its effects. We randomly assigned 1,492 participants to converse with either a sycophantic or a challenger LLM, crossing this manipulation with three disclosure conditions: no disclosure, passive disclosure (a written forewarning), and active disclosure (forewarning plus practice identifying sycophantic responses). We measured pre-and post-conversation agency ratings and certainty, along with perceptions of LLM credibility and conversational quality. Sycophantic AI suppressed attitude updating and inflated certainty among non-inoculated participants, while the challenger LLM produced positive attitude updating and flat-to-decreasing certainty. Neither passive nor active disclosure attenuated these effects. Active disclosure did reduce subjects' perceptions of the sycophantic LLM's credibility and of the quality of their conversational experience with it, but those reassessments did not translate into revised agency ratings or reduced certainty. We also document a pattern we call the "paradox of certainty": within each LLM condition, ratings and certainty moved in opposite directions, so subjects grew more confident in lower ratings and less confident in higher ones. As AI conversations become a primary channel through which citizens form views of public institutions, our findings suggest that the civic costs of sycophantic validation are not amenable to straightforward, disclosure-based policy interventions.

---

## uid: `doi:10.2139/ssrn.6652239`

- title: Transformer-Based Asset Pricing Models
- authors: Chinmay Sood
- affiliations: not stated
- posted: 2026-04-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6652239
- keyword hits: large language model, large language models, llm, llms

### abstract

The application of transformer-based deep learning architectures to asset pricing represents one of the most rapidly developing intersections of machine learning and empirical finance. Building on foundational breakthroughs in the machine learning literaturemost notably the self-attention mechanism introduced by Vaswani et al. (2017)financial economists have begun adapting these architectures to the challenges of return prediction, stochastic discount factor (SDF) estimation, and textual analysis of financial disclosures. This report provides a structured, critical review of the literature spanning three interconnected research streams: (1) the broad application of machine learning to asset pricing, which provides the methodological substrate upon which transformerbased approaches are built; (2) the specific adaptation of attention mechanisms and transformer encoders to time-series financial data; and (3) the use of pre-trained large language models (LLMs) including BERT, GPT, and their financial domain adaptationsfor extracting return-relevant signals from unstructured text. We critically compare competing methodologies, evaluate the robustness of reported findings, and identify persistent gaps in the extant literature including issues of interpretability, data snooping, transaction cost sensitivity, and the economic mechanisms Transformer-Based Asset Pricing Models-Research Report | Page 2 underlying transformer-learned signals. The report concludes with a structured agenda for future research.

---

## uid: `doi:10.2139/ssrn.6659258`

- title: From "Effects of X on Y" to "From X to Y": Evidence of Stylistic Convergence in Academic Titles after Mass LLM Adoption
- authors: Subham Shrivastava
- affiliations: not stated
- posted: 2026-04-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6659258
- keyword hits: chatgpt, large language model, large language models, llm, llms

### abstract

The public release of ChatGPT in November 2022 marked the beginning of mass adoption of large language models (LLMs) for general writing tasks. Whether and how this adoption has affected the style of academic writing is a question of growing methodological and sociological interest. We investigate one specific rhetorical pattern-the "From X to Y" title construction-across 2,039,999 paper titles from OpenAlex spanning 2010-2026 and twelve scholarly fields. The pattern's prevalence is remarkably stable from 2010 through 2022 (range: 0.74-0.86%) and then nearly doubles in the following 2.5 years, reaching 1.46% in early 2026. The inflection occurs in 2024, consistent with a 6-12 month publication lag from the November 2022 ChatGPT release. The aggregate trend, however, masks substantial cross-field heterogeneity. Fields with low pre-2023 baselines (medicine, energy, decision sciences, computer science) show relative increases of 75-103%, while fields with high pre-2023 baselines (arts and humanities, social sciences, earth and planetary sciences) change by 11% or less. We interpret this asymmetry as evidence of stylistic convergence: rather than introducing a new pattern, LLMs appear to be homogenizing academic title styles across disciplines toward a common rhetorical register that resembles the literary-essay norms historically used by humanities scholars. We argue that the policyrelevant question raised by this finding is not how many papers were AI-drafted, but whether the diversity of disciplinary writing styles is a feature worth preserving.

---

## uid: `doi:10.2139/ssrn.6455698`

- title: Sub -Millisecond Systemic Risk Resolution: Applied Operator Splitting, Dynamic SLA Calibration, and AI Guardrails in Macro-Financial Networks Author: Oleksii Slieptsov Founder and Chief Executive Officer, Scientific Analytics Alliance Inc. Association for Financial Professionals (AFP); PrivatBank JSC CB
- authors: Oleksii Slieptsov
- affiliations: not stated
- posted: 2026-04-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6455698
- keyword hits: large language model, large language models, llm, llms

### abstract

Traditional stochastic models, particularly Monte Carlo simulations, remain the industry standard for macro-financial stress testing. However, their high computational latency, often from seconds to minutes, prevents real-time integration with multi-agent systems (MAS) based on large language models (LLMs). This paper presents a hybrid Risk OS architecture that removes this computational bottleneck through a deterministic operator splitting method (adaptive Remizov / Lie-Trotter algorithm). Empirical server-side tests show that the mathematical core can be accelerated by up to 14,800x (from 7.9 s to 0.54 ms) while preserving asymptotic convergence (terminal divergence of 0.3159% at 10,000 paths). A built-in dynamic SLA calibration algorithm enforces a hard terminal error cap of ≤1.0000% , even under extreme cross-asset volatility regimes. To prevent semantic hallucinations in AI reasoning, the platform introduces a software guardrail layer (Taxonomy Router) that enforces ontological isolation. The resulting architecture enables institutional-grade "Sovereign Digital Twins" on standard cloud infrastructure (FinOps), while preserving real-time UX.

---

## uid: `doi:10.2139/ssrn.6441079`

- title: Answer Engine Optimisation in Indian Higher Education: An Exploratory Study of University Visibility in AI-Generated Responses
- authors: Jaydip Parikh
- affiliations: not stated
- posted: 2026-04-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6441079
- keyword hits: chatgpt, gemini, large language model, llm

### abstract

The rapid adoption of large language model (LLM)-based AI tools — including ChatGPT, Perplexity AI, Google Gemini, and Google Search Generative Experience (SGE) - has fundamentally altered how prospective students discover and evaluate higher education institutions in India. This exploratory working paper examines the visibility of Indian universities in AI-generated responses and introduces the concept of Answer Engine Optimisation (AEO) as applied to the Indian higher education context. Drawing on the author's practitioner experience working with Indian universities on digital marketing and student recruitment strategy, this paper documents preliminary observations about which institution types tend to appear in AI-generated responses and why. It argues that a measurable AEO Gap exists between an institution's actual quality and its AI-visible reputation — and that this gap disproportionately affects private universities outside the IIT/IIM tier, including many with strong NIRF rankings. Recommendations for improving AI visibility are provided, with implications for institutional reputation management, student recruitment, and NIRF Perception scores.

---

## uid: `doi:10.2139/ssrn.6662538`

- title: How Effectively Do LLM-Driven, Micro-Tailored Political Messages Influence Public Opinion Compared to General Persuasive Messaging, and What Are the Implications for Democratic Fairness?
- authors: Aaryan Srivastava
- affiliations: not stated
- posted: 2026-04-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6662538
- keyword hits: gpt-4, large language model, large language models, llm, llms

### abstract

The emergence of large language models (LLMs) as tools for automated political messaging represents a qualitative shift in the landscape of computational persuasion. This paper compares the mechanisms and effects of LLM-driven political microtargeting against earlier algorithmic influence systems (specifically Facebook's political content curation) drawing on Cathy O'Neil's 2016 analysis in Weapons of Math Destruction and the 2024 experimental study by Hackenburg and Margetts. While the Hackenburg and Margetts study finds that GPT-4-generated messages can shift political opinions by up to 12 percentage points, a margin potentially sufficient to affect electoral outcomes, it also finds that microtargeted messaging does not consistently outperform generic messaging. This paper argues that the more significant finding is not the marginal performance gap between microtargeting and generic persuasion, but rather the three structural harms LLMs introduce at scale: expanded reach unconstrained by corporate gatekeeping, compounded opacity at both the identity and reasoning levels, and amplified demographic exploitation. Together, these properties intensify the threats O'Neil identified in 2016 and raise new concerns for the integrity of democratic discourse.

---
