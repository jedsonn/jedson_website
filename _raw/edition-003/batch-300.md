# Classification batch 300 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-300.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6810959`

- title: Dual-use Risks of Frontier Artificial Intelligence
- authors: Rizwan Tanveer
- affiliations: not stated
- posted: 2026-06-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6810959
- keyword hits: claude

### abstract

Background. The dual-use risks of frontier artificial intelligence systems have moved from prospective concern to operational reality. Anthropic's activation of AI Safety Level 3 safeguards for Claude Opus 4 in May 2025, explicitly because chemical, biological, radiological, and nuclear (CBRN) uplift risks could no longer be confidently ruled out, marked a watershed in the industry's acknowledgement of risk. The United Kingdom AI Security Institute's first public Frontier Trends Report documented frontier model performance on apprentice-level cyber tasks rising from sub-nine per cent in late 2023 to approximately fifty per cent by 2026, with the first model completing expert-level tasks in 2025. The regulatory architecture intended to manage these risks remains unsettled: the United States Bureau of Industry and Security issued a Framework for Artificial Intelligence Diffusion in January 2025 and rescinded it in May 2025, leaving a regulatory gap that subsequent guidance has only partially filled. Purpose. This paper provides a synthesis of dual-use risk evidence for frontier AI across cyber offensive uplift and CBRN uplift, maps the contemporary regulatory architecture including its current volatility, examines the diversion and weight-exfiltration risks that connect dual-use concerns to AI supply chain governance, and analyses the Gulf Cooperation Council strategic context where the United Arab Emirates and the Kingdom of Saudi Arabia occupy a distinctive position in global AI diffusion policy. Approach. The paper adopts a narrative review methodology combining contemporary 2024 to 2026 empirical evaluations of frontier AI capabilities (including the UK AI Security Institute trends report, Anthropic Frontier Red Team disclosures, Frontier Model Forum threshold work, and independent third-party assessments), primary regulatory document analysis (the BIS Framework for AI Diffusion and its rescission, the EU AI Act systemic risk provisions, EU Regulation 2021 slash 821 on dual-use exports, the UAE Strategic Goods regime under Cabinet Resolution 50 of 2020), and analysis of voluntary industry safety frameworks (the Anthropic Responsible Scaling Policy, Google DeepMind Frontier Safety Framework version 2.0, OpenAI Preparedness Framework, and parallel instruments from Microsoft, Amazon, and G42). Findings. Three findings emerge. First, the empirical evidence base for cyber offensive uplift is now substantial, with multiple converging signals indicating that frontier models provide meaningful tactical uplift to human cyber operators, particularly when paired with appropriate scaffolding; the evidence base for CBRN uplift is more contested due to sensitivity restrictions on full evaluation data, but is sufficient to support the precautionary safeguards that leading labs have implemented. Second, the regulatory architecture is in active flux: the AI Diffusion Rule episode illustrates that unilateral commodity-based export controls struggle with a technology that diffuses through training compute, weights distribution, and inference access in ways that traditional dual-use frameworks were not designed to capture. Third, the GCC strategic context is distinctive: the United Arab Emirates and Saudi Arabia are positioned as Tier 2 destinations in US export-control thinking, with the UAE in particular having demonstrated a willingness to accommodate US security concerns through G42's divestment of Chinese hardware and the March 2025 US-UAE 1.4 trillion technology investment framework. Implications. Practitioners deploying frontier AI in the GCC region operate under a multi-layered governance regime that combines formal export controls, voluntary industry safety frameworks, and emerging EU AI Act systemic risk obligations. The diversion risks examined in Section 5 connect directly to the AI Supply Chain Trust Boundary Model developed in Paper 10 of this slate, with weight exfiltration at Layer 2 representing the operational manifestation of the most consequential dual-use diversion concern. Future work will extend the analysis through comparative regulatory mapping (Paper 14) and operational identity considerations, including weight-level attestation (Paper 15).

---

## uid: `doi:10.2139/ssrn.6840438`

- title: KAL: Connecting Knowledge Graphs to Geometric Memory Systems
- authors: Wingyan Lau, Agus Sudjianto
- affiliations: not stated
- posted: 2026-06-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6840438
- keyword hits: llm

### abstract

Prior work in this series has developed Geometric Memory Systems (GMS) along three dimensions: a benchmark for measuring structured retrieval [Sudjianto, 2026a], an evaluation framework showing that LLM-as-judge is unreliable on structured tasks [Sudjianto and Lau, 2026b], and a multi-agent architecture in which GMS serves as both persistent memory and governance mechanism [Sudjianto et al., 2026c]. GMS itself supports multiple downstream consumer modes-verification primitive, agent memory, validation harness-but across all of them the knowledge graph that GMS operates over is assumed to exist. This paper addresses the assumption directly: how should a knowledge graph be designed and exposed so that GMS can consume it cleanly? We introduce the Knowledge Adapter Layer (KAL)-the knowledge plug-in for GMS, and a design specification for the data plane that sits between a knowledge graph (relational store, native graph database, or RDF endpoint) and GMS, regardless of how GMS is used downstream. KAL has three design components. The adapter protocol is a small typed Python interface that any knowledge graph can implement: it groups operations into reads, writes, and similarity search, and pairs them with a capability descriptor that says which subset of the surface a given backend actually supports. The data crossing the protocol boundarytyped nodes, triples, literals, queries, and query results-carries the per-triple metadata GMS consumes (confidence, status, per-engine scores, evaluator identity) as first-class fields rather than opaque payloads. The federation router takes multiple adapters and presents them as a single graph to the caller: it fans queries out concurrently, merges results under a backend-independent content-hash dedup rule that handles both node-object and literalobject triples, enforces per-adapter timeouts so one slow source cannot stall the rest, and surfaces partial failures as structured error data so callers can distinguish "adapter returned nothing" from "adapter timed out." The schema discipline is the contract a customer's knowledge graph must satisfy in order to participate: typed entities with stable identifiers, a controlled predicate vocabulary, edge-attached provenance and verification metadata, and an external-ID registry that lets the same logical entity be addressed through Neo4j node IDs, Postgres UUIDs, or SPARQL URIs without identity collisions across stores. The protocol is symmetric under a second federation axis: the same triple can carry verification metadata from multiple GMS instances-a parent agent and its sub-agents, or multiple departmental GMSs within one organisation-and the federation primitives the protocol already exposes serve both axes without surface extension. A reference design grounds the specification: a Postgres adapter against the existing Knowlytix relational schema. The paper closes with KG autotuning as a self-improving consumer mode in which GMS's own geometric signals propose typed mutations to the KG through the same protocol surfaceturning KAL-readiness from a one-time onboarding contract into a property the deployment maintains under drift, and letting GMS land as a self-improving knowledge system rather than as a verifier-in-isolation. KAL is released as knowlytix-kal under Apache-2.0.

---

## uid: `arxiv:2606.05449v1`

- title: Insurance of Agentic AI
- authors: Quanyan Zhu
- affiliations: not stated
- posted: 2026-06-03
- source: arXiv
- link: https://arxiv.org/abs/2606.05449v1
- keyword hits: agentic, ai agent

### abstract

Agentic artificial intelligence (AI) systems are transforming the risk landscape by extending beyond information generation to autonomous planning, tool invocation, decision execution, and persistent modification of digital and physical environments. These capabilities introduce novel exposures that do not fit neatly within traditional insurance categories such as cyber, professional liability, product liability, or directors and officers coverage. This paper examines the emerging insurance market for agentic AI and develops a framework for understanding its underwriting, pricing, reinsurance, and product-design implications. We characterize agentic AI as a continuum of autonomy and delegated authority, emphasizing the distinction between informational outputs and systems capable of independently generating insured events through external actions. We analyze major risk pathways, including hallucinations, prompt-injection attacks, autonomous decision errors, model drift, dependency failures, and cyber-physical harms, and evaluate how existing insurance products are adapting to address these exposures. The paper further proposes an actuarial framework based on exposure assessment, scenario analysis, dependency mapping, and accumulation-risk management, drawing parallels to the evolution of cyber insurance. Finally, we present a coordinated insurance architecture that integrates cyber, technology errors and omissions, product liability, performance-warranty, and affirmative AI-liability coverages through explicit allocation mechanisms and dedicated AI aggregates. The analysis suggests that the future of agentic-AI insurance lies not in a single monoline product but in a layered ecosystem of complementary coverages supported by improved governance, transparency, telemetry, and regulatory clarity.

---

## uid: `doi:10.2139/ssrn.6878931`

- title: GradeFlow: A Dynamic Web-Based Grading and Records System with Offline AI-Powered Student Intervention Analysis for Teachers
- authors: ARNEL  CATAHURAN MAGHINAY
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6878931
- keyword hits: large language model, llama

### abstract

GradeFlow is a fully offline, web-based dynamic grading and academic records system designed for teachers in higher education and secondary institutions. The software invention addresses the persistent challenge educators face in building flexible, institution-specific grading workflows without relying on expensive commercial platforms or internet connectivity. GradeFlow enables teachers to define any number of grading criteria per term — including quizzes, major exams, projects, recitation, and class participation — each with independently configurable weights and maximum scores. Term grades and final grades are computed in real time using a weighted summation model, with support for a transmutation formula (the model) that maps raw percentage scores to transmuted equivalent grades as commonly required in Philippine higher education and similar systems.The system provides a spreadsheet-style gradebook interface that supports direct keyboard navigation, inline editing, and block paste from external tools such as Microsoft Excel or Google Sheets. One-click PDF report generation produces per-term criterion breakdowns and final grade sheets with pass/fail indicators and class summaries. A novel offline artificial intelligence intervention analysis engine, powered by a locally installed large language model (Ollama with the phi3.5 model), generates per-student intervention priority scores, identifies declining grade trends, isolates the highest-impact weak areas, flags missing or incomplete work, and produces concrete, prioritized instructional actions — all without transmitting any student data to external servers. Multi-teacher support, role-based access control (teacher, program chair, and administrator roles), attendance tracking, and customizable school branding complete the feature set. GradeFlow is free, requires no API keys, and runs on any standard XAMPP or WAMP local server environment.

---

## uid: `doi:10.2139/ssrn.6878994`

- title: Measuring Generative AI Dependency: Scale Development and Validation among University Students
- authors: Lisi Mai, Eiman Yassin, Joo-Young Jung
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6878994
- keyword hits: generative ai

### abstract

This study develops and validates the Generative AI Dependency Scale, a theoretically grounded instrument based on Media System Dependency (MSD) theory. The scale assesses how university students depend on generative AI to fulfill diverse goals in everyday lives. A multi-phase process was employed, including theoretical deduction from MSD’s goal typology, focus group interviews to generate items, and expert panel review to assess content validity. Survey data were collected from 555 Chinese university students with prior generative AI experience, with (n = 175) for exploratory and (n = 380) for confirmatory factor analyses. EFA revealed a nine-factor, 26-item structure, explaining 61.17% of variance. CFA confirmed the adequacy of the nine-factor model, with a satisfactory model fit. While MSD’s understanding and play goals were retained, the orientation goal differentiated into four action-oriented dimensions, and emotional comfort and support emerged as a new dimension. The study’s implications for measuring human-AI interaction and extending MSD theory to generative technologies are discussed.

---

## uid: `doi:10.2139/ssrn.6879978`

- title: Uncertainty-informed alloy design for additive manufacturing via a multi-functional large language model
- authors: Jixuan Dong, Hasan Al Jame, Bo Ni, S. Mohadeseh Taheri-Mousavi
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6879978
- keyword hits: large language model, large language models

### abstract

Integrating uncertainty quantification efficiently in alloy design is critical to achieve reliable properties in additively manufactured components for critical applications. Recent progress in applying large language models to conduct physics-based alloy design (e.g., AlloyGPT) has demonstrated a unique potential in handling multiple tasks of a forward prediction and inverse design of composition-structure-property relationships within a unified model. Here, the AlloyGPT model is extended and analyzed to enable uncertainty-informed robust alloy design. A dataset of 500,000 compositions spanning the standardized chemistry of model Alloy 718 was generated. Yield strengths were calculated using Calculation of Phase Diagrams (CALPHAD)-based simulations. Local perturbation of composition by ±0.10 wt.% variations led to 50–80 MPa changes in yield strength. The uncertainties were integrated in the text form to train the alloy specific language model. AlloyGPT predicts mean yield strength and standard deviation with high accuracy (R2 > 0.99). It also successfully performed constraint-driven inverse design of compositions satisfying a 1100 MPa target strength with ≤ 50 MPa variability and revealed a diverse set of feasible compositional solutions. To achieve both high strength and resilience to additive manufacturing-induced compositional variability, the model-suggested compositional windows highlight the need for control of critical elements (i.e., Al, Ti, Cr), while allowing broader flexibility for others. The choice of critical elements was consistent with results from sensitivity analyses. These explorations and advancements are expected to establish an uncertainty-informed, multi-functional language model. This model will facilitate robust forward predictions and inverse design across diverse alloy systems, including gradient designs for additive manufacturing.

---

## uid: `doi:10.2139/ssrn.6841658`

- title: Reducing Empty Backhauls in Freight Transport Using Hybrid Recommendation
- authors: Margaret Cullen
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6841658
- keyword hits: chatgpt

### abstract

Empty backhauls represent a persistent source of inefficiency in freight transport, leading to increased operational costs, unnecessary carbon emissions, and underutilized vehicle capacity. This study, completed in 2021, proposes and evaluates a hybrid recommendation system designed to reduce empty backhaul occurrences in road freight logistics. The hybrid model integrates collaborative filtering-leveraging historical trip patterns of similar carriers-with content-based filtering that matches real-time shipment attributes (e.g., origin, destination, vehicle type, time windows, and load constraints). Unlike single-method approaches, the hybrid system addresses cold-start and data-sparsity issues common in logistics platforms. The system was implemented and tested using operational data from a mid-sized European freight exchange platform, covering 18 months of lane-level shipping records. Results indicate a 23% reduction in empty backhaul trips among participating carriers, with a corresponding 17% decrease in deadhead mileage. The recommendation engine achieved a precision of 0.84 and recall of 0.79 in suggesting profitable, feasible backhaul loads, outperforming standalone collaborative (precision 0.72) and content-based (precision 0.69) models. Moreover, user acceptance testing with 45 fleet dispatchers showed a mean usability score of 4.2/5. These findings demonstrate that a hybrid recommendation approach, using only pre-2021 data integration and algorithmic techniques, can meaningfully mitigate empty backhaul inefficiencies without requiring real-time IoT or autonomous vehicle technologies. The study concludes with practical implementation guidelines for logistics service providers and suggests policy measures to incentivize data sharing for wider system effectiveness. AI Disclosure: The author used ChatGPT solely for editing, proofreading, and formatting of citations. After using this AI tool, the author reviewed and revised the content as needed and takes full responsibility for the final version of the publication.

---

## uid: `doi:10.2139/ssrn.6878395`

- title: Provisions Governing Disclosure of the Use of Generative Artificial Intelligence in Research Works: A Risk Assessment-Based Governance Model from the Perspective of Qatari Law
- authors: Nagi  Saleh Alyami, Bahaaeddin  M.S. khwaira
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6878395
- keyword hits: generative artificial intelligence

### abstract

This study aims to analyze the duty to disclose the use of generative artificial intelligence in research works. It reviews its effects on originality, attributing the work to the researcher, and data protection from the perspective of the Qatari Law on the Protection of Copyright, in light of modern comparative trends. Using an analytical and comparative legal lens, this study investigates the adequacy of regulations concerning the protection of copyright and data in accordance with Qatari laws relevant to AI-enhanced research outputs. It also relies on international scientific publishing policies and the American and European approaches to human authorship and creative contribution. The study concludes that Qatari law, although it does not expressly regulate the duty to disclose the use of artificial intelligence in research works, provides, through the rules on innovative works, moral rights, and data protection, a general foundation that can be built upon. However, it requires a more specific institutional disclosure framework. The study shows that disclosure is not a mere formal procedure. Rather, it is a governance tool for identifying the intervention of artificial intelligence, assessing originality, protecting data, and limiting plagiarism. The study proposes a model based on risk assessment. This model distinguishes between low-risk, medium-risk, and high-risk use, as well as prohibited use, and links each level to appropriate requirements for disclosure, documentation, and human review.

---
