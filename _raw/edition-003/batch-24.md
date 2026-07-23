# Classification batch 24 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-24.answer.json` as a JSON array.

---

## uid: `arxiv:2607.14818v1`

- title: Can LLMs Build a MaxSAT Solver from Papers? The CoreForge Experience
- authors: Ruben Martins
- affiliations: not stated
- posted: 2026-07-16
- source: arXiv
- link: https://arxiv.org/abs/2607.14818v1
- keyword hits: chatgpt, large language model, large language models, llm, llms

### abstract

We report on CoreForge, an experience in using large language models (LLMs) to build an unweighted MaxSAT solver from research papers rather than from an existing solver codebase. The project focuses on unsatisfiability-based MaxSAT algorithms and follows an iterative workflow that combines paper discussions with ChatGPT, implementation through Codex prompts, and repeated LLM-assisted code audits and revisions. Although the codebase implements several algorithms and solver components, our evaluation focuses on configurations that combine core-guided optimization, lightweight preprocessing, core minimization, integration with integer linear optimization backends, and a new core-sequence lookahead approach. Our experience suggests that LLMs can support solver implementation from papers, while requiring external validation, benchmarking, and human guidance. In our experiments, fuzzing and MaxSAT Evaluation instances did not reveal wrong answers in the tested configurations, although performance remains below the best hand-engineered MaxSAT solvers. We summarize what worked, what remained difficult, and the lessons for future LLM-assisted solver development.

---

## uid: `arxiv:2607.17219v1`

- title: Auditing Question-Order Effects in Large Language Models with the QQ Equality: Mechanism Characterization and a Saturation Caveat
- authors: Pilsung Kang
- affiliations: not stated
- posted: 2026-07-19
- source: arXiv
- link: https://arxiv.org/abs/2607.17219v1
- keyword hits: instruction-tuned, large language model, large language models, llm, llms, prompting

### abstract

Human survey respondents exhibit question-order effects that satisfy the QQ (quantum question) equality, an a priori, parameter-free prediction of the projective quantum question-order model. We develop the QQ equality into an audit criterion for sequential judgments of autoregressive large language models (LLMs). Theoretically, we characterize which mechanism classes satisfy it robustly: marginal-independent kernels satisfy QQ iff all four mismatch transition rates coincide (a class containing the 2D rank-1 projective model with a fixed measurement pair under state variation); a polarity- and position-dependent repetition family is characterized by an exact cross-symmetry condition with closed-form violations; QQ-satisfying behaviors are closed under order-matched mixing; and the rank-2 Contextuality-by-Default criterion translates into audit coordinates as $|\qQQ|\le\OSS$, where $\OSS$ (the order-sensitivity score) totals the order sensitivity of the two marginals. Methodologically, we develop a pre-specified, audit-logged pipeline applicable to any model exposing next-token log-probabilities; it combines worst-case robustness envelopes, sampling-consistency spot checks, full label counterbalancing, and a saturation diagnostic. Empirically, in a first-signal pilot on an open-weight instruction-tuned model under two framings, all pre-specified health gates passed, yet 17/18 and 7/8 item pairs, respectively, were saturated (near-deterministic), and no item was certified residually contextual. Forced-binary next-token log-probabilities were thus inadequate for distribution-level QQ audits under the tested model and prompting conditions; we recommend pre-specified saturation diagnostics whenever next-token distributions are treated as survey-response distributions.

---

## uid: `arxiv:2607.17935v1`

- title: DeLIVeR: Decomposed Learning for Information-grounded Veracity Recognition via Reinforced Knowledge Graph Exploration
- authors: Cong Hoan Nguyen, Thomas Hoang, Hieu Minh Duong, Long Nguyen
- affiliations: not stated
- posted: 2026-07-20
- source: arXiv
- link: https://arxiv.org/abs/2607.17935v1
- keyword hits: large language model, large language models, llm, llms, qwen

### abstract

Automated fact-checking remains a challenge for Large Language Models (LLMs) due to "query brittleness" in traditional retrieval systems. We propose DeLIVeR (Decomposed Learning for Information-grounded Veracity Recognition), a framework that treats evidence retrieval as a reinforced strategic exploration task. DeLIVeR utilizes a Planner LLM to decompose complex claims into targeted question sets, which are used to traverse structured Knowledge Graphs (KGs) for high-precision evidence. We optimize the Planner's policy using Group Relative Policy Optimization (GRPO) with a reward system prioritizing structural diversity and verdict accuracy. Our evaluation on LIAR, FEVER, and PolitiFact shows that DeLIVeR significantly outperforms state-of-the-art baselines. Using Qwen2.5-7B, our framework achieved peak F1-scores of 83.73, 84.57, and 79.70 respectively, representing a 10-15% improvement over HippoRAG2. By shifting to a reinforced question-planning strategy, DeLIVeR effectively bridges multi-hop reasoning gaps and provides an auditable, transparent path for verifiable misinformation detection.

---

## uid: `doi:10.2139/ssrn.7146358`

- title: Physicians' Experiences of Generative AI-Assisted Diagnostic Reasoning and Perceived Applicability in the Kenyan Healthcare Context: A Qualitative Study from a Tertiary Teaching Hospital
- authors: Roselyter  Monchari Riang&apos;a, Soraiya Manji, Norah Obungu, See PDF
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7146358
- keyword hits: chatgpt, generative ai, generative artificial intelligence, gpt-4, large language model, llm

### abstract

Background: Generative artificial intelligence (AI), particularly large language model (LLM)-based tools, offers new opportunities to support clinical reasoning and diagnostic decision-making. However, direct experiential evidence on how frontline physicians in low- and middle-income countries engage with these tools in practice remains largely absent from Literature. Methods: Embedded in a wider multi-site parallel group randomized controlled trial study, we conducted a qualitative descriptive study guided by a constructivist-interpretivist paradigm anchored on the Normalisation Process Theory(May & Finch, 2009) framework. Semi-structured exit interviews were conducted with 19 physicians across diverse departments at a Kenyan tertiary teaching hospital immediately following structured diagnostic simulations with a generative AI chatbot (ChatGPT-4o API access). Data was analysed inductively through reflexive thematic analysis. Findings: Ten sub-themes emerged within two overarching domains. Perceived benefits included broadened differential diagnoses beyond initial formulation, more structured history-taking and clinical reasoning, targeted investigation planning, enriched patient education, and consolidated workflow efficiency. Contextual barriers included workflow incompatibility with high-volume clinical settings, systematic misalignment between AI outputs and local epidemiology and resource availability, physician concern that visible AI use during consultation would undermine clinical authority and patient trust — a finding rooted in the relational architecture of the African clinical encounter — interface usability limitations, and risk of overreliance with reduced critical engagement. Interpretation: Kenyan physicians showed strong readiness to engage with generative AI as a clinical thinking partner, but structural, epidemiological, and relational barriers prevented routine clinical enactment. These findings reframe AI implementation in African health systems from a technical deployment problem to a sociotechnical integration challenge requiring localised model training, workflow-sensitive interface design, and institutional renegotiation of AI's role in the clinical encounter.

---

## uid: `doi:10.2139/ssrn.7121598`

- title: A Behavioral Taxonomy of LLM Failure Modes
- authors: Michael Kitamura
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7121598
- keyword hits: claude, gemini, large language model, large language models, llm

### abstract

This paper reports findings from an extended naturalistic observation study of recurring failure behaviors in large language models-output patterns that occur while a model appears competent, compliant, and confident. Four failure classes are identified: Overt Sycophancy, Covert Sycophancy, Confidence Drift, and False Confidence. The latter three are characterized from documented instances across GPT, Claude, and Gemini during ordinary working sessions, with no adversarial elicitation. Overt Sycophancy is included as a named class on the strength of its evident frequency in ordinary use, though no specimen has yet been captured and logged. Micro-Drift, one of three named Recursive Dynamics in this taxonomy, is a baseline-inheritance pattern in which a sub-threshold deviation becomes the working baseline for a subsequent pass, compounding across a chained workflow into progressive divergence from source material. Named variants, compound behaviors, and a workflow integrity and recovery protocol are documented. Each classification carries an explicit evidence status reflecting the number and diversity of confirming instances observed. A companion work (Kitamura, M., Covert Sycophancy in Large Language Models: A Behavioral Taxonomy from Naturalistic Observation, SSRN 6519098) provides full session-level case documentation for the same behaviors.

---

## uid: `doi:10.2139/ssrn.7158001`

- title: Generative AI Regulation, Creative Industry Disruption, and Governance Response in China's Cultural Sector
- authors: Gh U
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7158001
- keyword hits: generative ai, large language model, large language models, llm, llms

### abstract

Text generators based on large language models (LLMs), AIGC (Artificial Intelligence Generated Content), and models that transform text into images or videos have been rapidly transforming cultural industries. As GenAI platforms started to enter the market, China’s state regulators, from the Cyberspace Administration of China (CAC) to the National Press and Publication Administration (NPPA), have been working to establish a new governance architecture to deal with the emerging industrial component. This study investigates the relationship between AIGC adoption intensity in the creative sector and the governance quality of corresponding regulations. Using firm-level panel data from 2020 to 2024 covering all listed cultural enterprises engaged in film, music, publishing, and interactive media, this study adopts a difference-in-differences (DiD) identification strategy based on staggered provincial implementation of licensing enforcement by authorities at the national and provincial levels, as well as an event-study design focusing on CAC announcements related to AIGC. The results show that effective governance quality can make a significant difference in the scale and pattern of labour displacement caused by AIGC adoption. The impact varies across levels of governance quality and firm characteristics. State-affiliated platforms have enjoyed remarkable advantages in AIGC compliance, perpetuating existing structural inequalities between platform operators and independent creators. The simulation results suggest that an incremental improvement of the regulatory quality at the provincial level, up to a certain point, may help to decrease the creative workforce displacement rate by certain percentages. Building on these findings, the paper discusses the possible implications for upgrading the governance instruments and systems for AIGC in China, developing international AI cultural governance frameworks within the UNESCO and WIPO frameworks, and protecting creative labour rights in emerging cultural economies dominated by AI.This list of completed research projects on Generative and Interactive Gaming Technologies (AIGC) explores the issues concerning the interaction and control between generative AI and its governance, and its impact on creative industry and business models related to it. Some projects also focus on the cultural governance and relevant Chinese policies. The methodologies used include differential analysis, empirical studies, and critical thinking.

---

## uid: `doi:10.2139/ssrn.7073158`

- title: LLM-Assisted Proofreading A Study of the Effectiveness of 13 Free AI Detection Tools
- authors: Kariema El Touny
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7073158
- keyword hits: claude, gemini, large language model, large language models, llm, llms

### abstract

This study investigates the effectiveness of 13 free online AI-content detection tools when applied to texts edited by large language models (LLMs) at varying levels of proofreading. Seven original texts spanning academic, journalistic, fictional, and professional genres were processed through three LLMs (Copilot, Claude, and Gemini) across four editing levels, ranging from grammar correction to full rewrite. Outputs were scanned by multiple detectors, with results systematically recorded and compared. Findings reveal significant inconsistencies across tools, with some detectors returning human-written verdicts regardless of proofreading level, while others flagged original, unmodified texts as AI-generated. Most notably, detection scores were found to correlate more strongly with genre and writing style than with the degree of LLM intervention, suggesting that these tools function more as style detectors than as AI detectors. Technical limitations of the tools used in this study significantly constrained the experiment, highlighting their unreliability and limited suitability as trustworthy instruments for identifying LLM-assisted writing.

---

## uid: `doi:10.2139/ssrn.7024983`

- title: Zero-Shot Structured Data Extraction from Timely Disclosure Documents in PDF Format with Large Language Models
- authors: Nobushige Doi, Mayuri Tanaka
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7024983
- keyword hits: gpt-5, large language model, large language models, llm, llms

### abstract

Timely disclosure documents released through TDnet, operated by the Tokyo Stock Exchange in Japan, are a source of corporate information; however, many are distributed as PDFs and are not directly reusable by machines. This study evaluates zero-shot structured data extraction from Japanese TDnet PDFs using large language models (LLMs) and documenttype-specific JSON Schemas. We compared 12 conditions that combine three models, GPT-5.4, GPT-5.4-mini, and GPT-5.4nano, with four reasoning effort settings across eight disclosure types. Each condition was run three times to measure the output variation. GPT-5.4, with high reasoning effort, obtained the highest average score, with core field accuracies of 0.905 ± 0.045. The best settings differed by document type, and higher reasoning effort did not consistently improve accuracy. These results indicate that schema-guided extraction can support the structuring of timely disclosure PDFs. However, schema design, auxiliary field handling, output variation, and processing time must be considered during deployment.

---
