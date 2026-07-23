# Classification batch 21 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-21.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6945287`

- title: COST-SENSITIVE ARCHITECTURE AUDITING FOR LLM-BASED TABULAR PREDICTION: EVIDENCE FROM FREIGHT CANCELLATION MANAGEMENT
- authors: Wenyi Kuang
- affiliations: not stated
- posted: 2026-06-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6945287
- keyword hits: claude, gpt-4, large language model, large language models, llm

### abstract

Large language models are increasingly used to make predictions from structured business data, but good prediction scores do not always translate to better decisions. We study this gap in freight cancellation management, where a retailer decides which shipments to intervene on, and where releasing a shipment that later gets cancelled costs far more than an unnecessary intervention. We introduce a cost-sensitive architecture audit that evaluates a whole system, not a model in isolation. The audit asks four questions: what information the system uses, whether its predicted probabilities cross the firm’s cost-implied decision threshold, how those probabilities are converted into actions, and whether the prediction cost is justified. We apply the audit to a 372,590 freight-shipment panel, comparing GPT-4o and Claude Sonnet 4.6 with calibrated tabular models, logistic regression, and a simple fallback rule. Prompted GPT-4o ranks shipment cancellation probability competitively (AUC 0.810, against 0.808 for XGBoost and 0.832 for logistic regression), but its predicted probabilities are above the focal firm’s cost-implied decision threshold [[EQUATION]]. The LLM’s deployed policy therefore intervenes on every shipment while adding cost without providing new actions relative to an always-intervene rule. Several simpler tabular models instead act selectively and save costs against the always-intervene baseline; logistic regression saves the most while the LLM saves none. Post-hoc calibration and out-of-time validation confirm that the central issue is not ranking quality but whether predictions change decisions. The study offers a reusable evaluation template for machine-learning systems in cost-sensitive operational settings.

---

## uid: `doi:10.2139/ssrn.6951046`

- title: A Knowledge Graph-Enhanced Dual-Agent LLM Framework for Synthetic Aviation Safety Report Generation under Class Imbalance
- authors: Xiao Jing, Zhenyu Gao, Dimitri Mavris
- affiliations: not stated
- posted: 2026-06-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6951046
- keyword hits: large language model, large language models, llama, llm, llms, qwen

### abstract

Aviation safety reports constitute a rich database from which advanced language technologies extract actionable operational intelligence. Aviation safety analytics has grown substantially as machine learning (ML) models have been developed to perform diverse information extraction and classification tasks on accident narratives. However, aviation safety databases exhibit severe class imbalance, where the most safety-critical scenarios appear too infrequently for reliable supervised ML. Large language models (LLMs) generate synthetic reports that offer a solution to augment scarce safety data, yet often produce physically impossible scenarios that violate domain constraints. In this paper, we introduce a knowledge graph (KG) enhanced dual-agent framework for generating physically grounded, high-fidelity synthetic accident reports that address this data limitation. We construct a three layer unified KG of 2.29 million RDF triples, encoding aircraft performance constraints, detailed infrastructure from 30,287 U.S. airports, and two decades of regional weather risk profiles. Two fine-tuned LLMs generate reports conditioned on SPARQL queries to the KG, which an asymmetric dual judge pair of Qwen and Llama evaluates across 20 binary metrics spanning deterministic physical verification and linguistic quality assessment. In a volume-controlled ablation, KG-grounded synthetic reports raise the stringent dual-consensus acceptance rate from 36% to 64%. A downstream augmentation scaling analysis shows that adding 250 such high-fidelity synthetic reports improves Encounter with Weather recall from 66 % to 73 % without degrading performance on other event categories. The approach has the potential to generalize to other safety-critical transportation domains requiring verifiable AI-generated content.

---

## uid: `doi:10.2139/ssrn.6958667`

- title: Enhancing Requirements Change Risk Assessment through LLM-assisted and Rule-based Analysis
- authors: Mandira Roy, Souvick Das, Novarun Deb, Nabendu Chaki, Agostino Cortesi
- affiliations: not stated
- posted: 2026-06-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6958667
- keyword hits: large language model, large language models, llm, llms, prompt engineering, retrieval-augmented

### abstract

Context: Incremental software development approaches such as Agile and DevOps are characterized by continuous requirements evolution, making effective change management essential. The existing change analysis techniques for assessing such evolving requirements largely focus on functional requirements, and often neglect dependencies and/or conflicts with non-functional requirements. Objectives: This limits proper risk assessment and may lead to cascading system-level failures. A structured early risk assessment may lead to reduced refactoring. Method: This paper presents a hybrid AI-assisted framework for requirement change risk assessment that explicitly models dependencies and conflicts among heterogeneous requirements. The approach combines rule-based reasoning with Large Language Models (LLMs), enhanced through prompt engineering and Retrieval-Augmented Generation. Unlike most of the prior works, LLMs are first used to identify dependencies and conflicts among requirements. A rule-based engine then exploits these derived relationships to perform impact propagation and risk estimation. Results: An empirical evaluation of the User Story dataset reveals that the proposed system accurately identifies inter-requirement relationships with an average precision of 86\%, supporting scalable risk assessment across projects of varying sizes and complexities. This enables the early detection of high-risk changes in an evolving software system. The derived risks are validated using a consensus-based mechanism implemented using LLMs. Conclusion: RASC effectively evaluates the impact and operational risk associated with incorporating proposed changes into the system design within an incremental development environment. Performing such assessments at early stages helps minimize extensive refactoring efforts, reduces maintenance overhead, and prevents delays in software delivery schedules.

---

## uid: `doi:10.2139/ssrn.6860580`

- title: Exploring a Multi-Agent Framework with Large Language Models for Nuclear Design Automation
- authors: Erpin Zhang, Weizhen Liu, Yu-Yan Xu, Chenglin Ye, Yunqi Xue, Shenglong Qiang, Guanghui Yuan, Ting Liu
- affiliations: not stated
- posted: 2026-06-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6860580
- keyword hits: deepseek, large language model, large language models, llm, llms

### abstract

Traditional nuclear reactor design workflows involve complex simulations, parameter optimization, and result analyses, and many of these steps still rely heavily on expert manual effort, which limits efficiency, reproducibility, and scalable engineering deployment. To address this problem, we developed MANDiF-CORCA, a multi-agent framework that couples large language models (LLMs) with an industrial deterministic reactor core analysis code for auditable workflow automation. The framework combines artifact-gated execution, state-machine-constrained coordination, and structured code-based data collection so that each workflow stage advances only after the required intermediate files are successfully generated and verified. Using an HPR1000-based reactor model, we evaluated four LLM backbones on nine representative tasks and further demonstrated the framework on six engineering scenarios, including critical boron search, distributed power analysis, control rod worth evaluation, reactivity-coefficient calculation, and operational-domain assessment. In the comparative evaluation, average workflow success rates ranged from 83.54% to 96.30%, with DeepSeek-V3.2-Exp achieving the best overall performance. Robustness tests further showed that the framework remained stable for specific tasks but became more sensitive to model temperature and semantic perturbation in more complex workflows. Overall, the study shows that coupling LLM agents with industrial deterministic reactor design software provides a feasible path toward robust, auditable, and reproducible workflow automation in nuclear design.

---

## uid: `arxiv:2606.24950v1`

- title: MacroLens: A Multi-Task Benchmark for Contextual Financial Reasoning under Macroeconomic Scenarios
- authors: Patara Trirat, Jin Myung Kwak, Jay Heo, Heejun Lee, Sung Ju Hwang
- affiliations: not stated
- posted: 2026-06-23
- source: arXiv
- link: https://arxiv.org/abs/2606.24950v1
- keyword hits: foundation model, large language model, large language models, llm, llms

### abstract

Financial decision-making is contextual: forecasting prices, valuing companies, and assessing event exposure weigh price history, accounting fundamentals, macroeconomic regime, and contemporaneous text. A benchmark over these four signals is hard to build because finance violates four assumptions of time-series evaluation: text must be gated by its publication date to prevent look-ahead, quarterly fundamentals are reported with a one- to ninety-day lag, filing text is partly redundant with the numerical statement fields it accompanies, and macroeconomic regimes leak across calendar splits. No public benchmark addresses all four signals jointly. MacroLens covers 4,416 U.S. small- and micro-cap equities over 2021-2026. Seven tasks share one point-in-time panel of prices, 46.8M XBRL accounting facts, 53 macroeconomic series, 295,860 SEC filings, and 215,882 news articles, plus a scenario layer of 1,130 macroeconomic events across 49 types automatically detected and rendered as natural language. Tasks span contextual forecasting, public and private valuation, statement generation from fundamentals and descriptions, scenario-conditioned returns, and real-estate valuation. We evaluate 19 methods across six families spanning naive heuristics through time-series foundation models, fine-tuned LLM-based time-series models, and zero-shot large language models (LLMs), plus a five-step feature-context ablation on two frontier LLMs and a gradient-boosted baseline. MacroLens is released at https://huggingface.co/datasets/DeepAuto-AI/MacroLens.

---

## uid: `doi:10.2139/ssrn.6890263`

- title: Evaluating Cognitive Resilience of Large Language Models under Structural Opacity: An Algorithmic Audit of Local Government Financing Vehicles (LGFVs)
- authors: Chieh-Ting Tsai
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6890263
- keyword hits: chatgpt, large language model, large language models, llm, llms

### abstract

This paper investigates the cognitive resilience of Large Language Models (LLMs) when confronting environments marked by institutionalized information asymmetry and implicit risk transfers. Using China’s Local Government Financing Vehicles (LGFVs) as a complex empirical case, we examine how different model architectures interpret a dual-track mechanism in which platforms leverage implicit state credit for capital acquisition while enforcing corporate isolation during fiscal distress. This structure facilitates the hidden transfer of financial burdens to the public. Models exhibiting high sycophancy bias and semantic evasion (e.g., ChatGPT) were excluded during preliminary screening due to insufficient operational reliability. Comparative analysis of the remaining models reveals a clear architectural divergence: institutional-weighted models demonstrate systemic blindness by over-indexing officially sanitized data, while social-weighted models exhibit a higher empirical detection rate but remain highly vulnerable to coordinated narrative manipulation (astroturfing). We introduce the concept of the “Incorporeal Trap” to explain these limitations. Because LLMs lack physical existence and survival costs, they are information-theoretically decoupled from material human externalities. Consequently, when operating within systematically corrupted data environments, these models tend to function as internal mechanisms that reinforce structural opacity.

---

## uid: `doi:10.2139/ssrn.7005928`

- title: Simulacromorphism: When Humans Mistake the Machine for the Mind
- authors: Hrishitva Patel, Kyrie Zhixuan Zhou, Jinjun Xiong
- affiliations: not stated
- posted: 2026-06-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7005928
- keyword hits: generative ai, large language model, large language models, llm, llms

### abstract

The rapid advancement of large language models (LLMs) has created a new challenge in digitally mediated environments: the increasing difficulty of distinguishing human-generated content from machine-generated output. While prior research has examined anthropomorphism, the tendency to attribute human characteristics to non-human entities, and more recently LLMorphism, the tendency to understand human cognition through the lens of language model architectures, little attention has been given to the inverse phenomenon. This commentary introduces Simulacromorphism, defined as the erroneous attribution of human origin, identity, or agency to artificial intelligence systems and their outputs. Drawing on theories of anthropomorphism, simulacra, human-computer interaction, and artificial intelligence, we position Simulacromorphism as a distinct cognitive and sociotechnical phenomenon with significant implications for cybersecurity, digital trust, and governance in increasingly AI-mediated environments. We develop a conceptual framework that differentiates Simulacromorphism from related constructs and situates it within broader debates concerning human–AI indistinguishability, authenticity, and attribution. Building on these foundations, we propose a three-layer governance architecture consisting of signal verification, attribution calibration, and identity validation to guide future approaches to human–AI differentiation. The commentary concludes by outlining a research agenda for studying Simulacromorphism and calling for the development of benchmark frameworks capable of systematically distinguishing human from artificial agents as generative AI becomes increasingly integrated into social, organizational, and institutional contexts.

---

## uid: `doi:10.2139/ssrn.6893598`

- title: When Machines Begin to Dream
- authors: Northon Salomão De Oliveira
- affiliations: not stated
- posted: 2026-06-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6893598
- keyword hits: generative ai, large language model, large language models, llm, llms

### abstract

When Machines Begin to Dream addresses a critical, untheorized structural blind spot in contemporary artificial intelligence governance: the rise of "machinic interiority". This term describes the latent, multi-dimensional generative space inside advanced deep neural networks and large language models (LLMs). Within this space, complex pattern synthesis creates novel semantic outputs that cannot be traced back or attributed to any single human input, programmer intention, or training data point. ​The author posits that global legal systems are suffering from a profound institutional inertia, operating on obsolete Cartesian assumptions that legally cognizable cognition must be strictly biological and that human-like intentionality is a prerequisite for legal subjecthood. As generative AI increasingly acts with statistical autonomy, this baseline assumption loses both descriptive and normative validity, leaving traditional liability, contract, tort, and administrative frameworks in a state of catastrophic interpretive distortion. ​The Analytical Gap & Pluralistic Methodology While existing scholarship covers immediate algorithmic harms—such as data privacy violations, algorithmic bias, and platform intermediary liability—it systematically overlooks the deeper jurisprudential threat: does AI possess a legally cognizable form of generative autonomy, and how must governance evolve to recognize it? ​To solve this, the paper employs a multi-jurisdictional and interdisciplinary approach: ​Six-Jurisdiction Comparative Analysis: A deep dive into the diverging regulatory models of the European Union (the risk-based EU AI Act), the United States (fragmented, sectoral administrative actions), China (state-centered algorithmic management), Brazil (active legislative debates around PL 2338/2023 and the LGPD framework), Canada (AIDA and voluntary code framework), and the United Kingdom (post-Brexit focus on frontier AI safety). ​Jurisprudential Review: An examination of ten landmark judicial and quasi-judicial decisions (including Loomis v. Wisconsin, Thaler v. Comptroller-General, Schrems II, and Mata v. Avianca) detailing the friction between traditional litigation standards and generative opacity. ​Interdisciplinary Triangulation: The legal dogmatics are mapped against cognitive neuroscience (Antonio Damasio), psychoanalytic theory (Sigmund Freud's and Jacques Lacan's frameworks on the unconscious and the "Other"), behavioral economics (Daniel Kahneman), and systems sociology (Niklas Luhmann). ​The Diagnostic & Institutional Failure Mapping The paper tests its framework against three urgent, high-stakes institutional case studies where generative opacity is actively causing un-remedied societal friction: ​Clinical Medicine: Where the deployment of LLM-based clinical decision systems operates under a false "legitimacy halo effect," distorting medical validation protocols and obscuring accountability when diagnostic errors cause deep, bodily harm. ​Legal Services: Where sophisticated professionals utilize opaque generation tools, creating a profound risk mismatch between attorney professional responsibilities and un-falsifiable machinic "hallucinations". ​Electoral Democracy: Where massive personalization and microtargeted political messaging optimized by AI systematically exploit cognitive biases, posing a severe threat to democratic self-governance and cognitive liberty. ​The Pragmatic Solution: The Graduated Cognitive Accountability Framework (GCAF) Rather than falling into speculative traps regarding machine consciousness, the paper advances an operationally realistic regulatory model: the Graduated Cognitive Accountability Framework (GCAF). This architecture is built upon four operational pillars: ​Mandatory Opacity Impact Assessments (OIAs): Pre-deployment evaluations measuring attribution, process, and deployment opacity, modeled structurally on the GDPR's impact assessments.

---
