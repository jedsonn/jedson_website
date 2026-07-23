# Classification batch 167 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-167.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6949948`

- title: Augmenting EAP Materials with GenAI: An Analysis of AI-Generated Mentor Texts for Secondary Classrooms
- authors: Luciana  C. de Oliveira, Allessandra  Elisabeth dos Santos
- affiliations: not stated
- posted: 2026-06-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6949948
- keyword hits: chatgpt, gemini, generative artificial intelligence

### abstract

A major challenge in K-12 English for Academic Purposes (EAP) contexts is the shortage of mentor texts to guide multilingual learners (MLs) in academic writing. This study explores how Generative Artificial Intelligence (GenAI) can address this gap by producing genre-specific mentor texts. Framed by Systemic Functional Linguistics (SFL), the study was guided by two research questions: how the Prompt Creation Reference Chart (PCRC) facilitates EAP material development across GenAI platforms, and what an SFL discourse analysis reveals about the structural and linguistic similarities and differences among texts produced by ChatGPT, Gemini, and MagicSchool. Using identical prompts structured by the PCRC, mentor texts in the Explanation genre were generated across all three platforms. The SFL analysis revealed that while all platforms successfully modeled core genre features, critical cross-platform variations emerged. These differences indicate that mentor text quality depends on both the GenAI system’s core algorithmic capabilities and its specific platform interface. The findings highlight GenAI as an unprecedented resource for creating personalized, interactive learning models that reduce the time-consuming nature of materials development. The article concludes with practical implementations and benefits for K-12 classrooms, showing how educators can leverage these variations to optimize second language academic writing instruction.

---

## uid: `doi:10.2139/ssrn.6852220`

- title: The SMB AI Maturity Index: A Five-Level Framework for Assessing Generative AI Integration in Small and Medium Businesses
- authors: Ankur Sharma
- affiliations: not stated
- posted: 2026-06-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6852220
- keyword hits: generative ai, generative artificial intelligence

### abstract

Generative artificial intelligence (GenAI) has diffused into the small and medium business (SMB) segment at unprecedented velocity. The OECD reports that 31 percent of SMEs across seven advanced economies were using GenAI in 2024, while US small-business adoption rose from 23 percent in 2023 to 58 percent in 2025. Yet beneath the headline figures the SMB sector lacks a peer-reviewed, design-science-grounded diagnostic instrument by which owners, advisors, lenders, or policymakers can determine where a given firm stands on the journey from experimental to integrated AI use. Enterprise AI maturity frameworks from Gartner, IBM, Microsoft, PwC, and Accenture presuppose architectural assumptions, dedicated CIOs, MLOps practices, governance councils, and minimum revenue thresholds, that exclude firms below 250 employees. SMB-focused frameworks published between 2024 and 2026 are uniformly prescriptive (Hussain and Rizwan, 2024; Raza, 2025; Eveland, 2025; Agbaakin, 2025; Ibrahim, 2025) or descriptive (Chandler et al., 2025; Bharier et al., 2026), and none provides a multi-dimensional, scored diagnostic instrument calibrated for owner-operator decision units. This paper develops the SMB AI Maturity Index, a five-level by five-dimension diagnostic matrix designed for firms with fewer than 250 employees. Following the Design Science Research methodology of Peffers et al. (2007), the maturity model procedure of Becker et al. (2009), and the design principles of Pöppelbuß and Röglinger (2011), the Index spans the dimensions of Strategy and Leadership, Data Foundation, Process Integration, Workforce Capability, and Governance and Ethics, each evaluated across five ordinal levels from Ad-Hoc to Transformative. Eighty-eight behavioral indicators populate the twenty-five cells, written in plain language for unaided self-assessment in approximately forty-five minutes. The instrument produces a five-dimension profile, an overall maturity classification computed by the weakest-link rule, and a prioritized intervention sequence. A Delphi validation protocol involving twelve to eighteen experts across four stakeholder groups is specified ex ante, and a composite demonstration illustrates the diagnostic logic. The paper contributes a novel design science artifact, an extension of maturity modeling into the resource-constrained SMB context, and a measurement substrate for future empirical research on SMB GenAI integration.

---

## uid: `doi:10.2139/ssrn.6949507`

- title: Lawful-delivery controls in a neuro-symbolic legal pipeline: a synthetic transfer-pricing benchmark
- authors: Carlos-Miguel Lorenzo
- affiliations: not stated
- posted: 2026-06-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6949507
- keyword hits: large language model, large language models

### abstract

The deployment of large language models in compliance-critical legal work is constrained less by retrieval accuracy than by whether an automated analysis may lawfully be produced. Personal data and trade secrets in audit material, the extraterritorial reach of foreign access regimes, and the evidentiary demands of administrative due process jointly determine admissibility, yet they are largely absent from legal-information-retrieval evaluation. This paper presents the Veritas Neuro-Symbolic Pipeline (V-NSP), a ten-stage legal-analysis pipeline in which privacy, data sovereignty and forensic traceability are first-class controls and information retrieval is a subordinate mechanism. Sensitive spans are pseudonymised locally, before any external token egress, under a hard privacy veto; deliveries are recorded in an append-only write-once log carrying a per-record SHA-256 digest; and the control flow degrades honestly rather than fabricating answers. We formalise a sovereignty-aware utility lens that situates retrieval adequacy within privacy and traceability fidelity, and evaluate the pipeline on a documented, seed-reproducible synthetic benchmark of 600 Spanish transfer-pricing audit instances (Article 18 of the Spanish Corporate Income Tax Act). Local redaction recall is 0.996; residual re-identification risk is lower under a sovereign control plane than under a cloud-exposed one and decoupled from latency by construction; forensic records are written for 97.0% of deliveries with full digest integrity; and the pipeline declines an unqualified answer in roughly one fifth of instances. A retrieval gain from graph expansion is reported only as a staging result, since the channel is disabled by default in deployment. The benchmark and generator support reproducibility, transparency and auditability.

---

## uid: `doi:10.2139/ssrn.6945099`

- title: Beyond Raw Transcripts: Structured Persona Extraction for LLM-Based Digital Twins
- authors: Iris Ye, Tianze Deng, Ozan Candogan
- affiliations: not stated
- posted: 2026-06-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6945099
- keyword hits: gpt-5, llm, qwen

### abstract

LLM-based "digital twins" aim to simulate how an individual would behave in new environments or respond to novel questions, given some representation of that individual’s prior responses. A common approach constructs this representation from survey transcripts or summaries derived from them, and evaluates performance by predicting holdout responses. Prior work shows that compressing long transcripts into shorter LLM-generated summaries does not significantly reduce predictive accuracy, suggesting that information volume is not the primary bottleneck. In this work, we argue that the key limitation is instead structural: how persona information is organized before being provided to the simulator model. We study this by comparing unstructured summaries with structured persona representations. First, we introduce a hand-crafted schema (BDE: Background, Decision procedure, Evaluation), grounded in consumer-behavior theory, and show that it improves predictive accuracy over raw transcripts by +1 . 91 percentage points on a homogeneous benchmark (Twin-2K-500), with similar gains on gpt-5.4-mini and Qwen3-8B as robustness checks. However, this fixed structure does not generalize across more heterogeneous tasks, where performance is statistically indistinguishable from the raw transcript baseline. To address this limitation, we propose an automatic structure-discovery pipeline in which an LLM iteratively proposes and refines task-specific persona structures and extraction prompts. On a benchmark of 13 diverse sub-studies, this approach restores performance, improving mean accuracy by +1 . 91 percentage points over the raw transcript baseline and eliminating significant losses observed with the fixed schema. Overall, our results suggest that the main constraint in LLM-based digital twins is not how much information is provided, but how it is structured—and that the optimal structure depends on the task.

---

## uid: `doi:10.2139/ssrn.6853098`

- title: Scrape, Train, Compete: Data Extraction as Unfair Competition in the AI Era
- authors: Nikolin Muçaj
- affiliations: not stated
- posted: 2026-06-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6853098
- keyword hits: chatgpt, llm, llms

### abstract

Artificial intelligence companies increasingly scrape vast quantities of online content to train systems that substitute for, rather than refer users to, their sources. When tools such as ChatGPT generate responses derived from news reporting by outlets like The New York Times , they compete for the same reader attention that publishers cultivated through sustained investment in journalism. Yet existing legal frameworks provide little recourse. Copyright law excludes most factual and informational works under the originality requirement articulated in Feist , while common-law misappropriation doctrine has been narrowed almost to extinction by federal pre-emption. This paper addresses that gap by developing a market substitution framework for AI-era scraping disputes. Liability arises where content appropriation (i) extracts material from substantial investment, (ii) enables competing products, and (iii) would systematically undermine creation incentives. The framework survives pre-emption by targeting competitive displacement, an element distinct from copyright's reproduction right, while requiring actual market harm rather than mere copying. Neither copyright nor existing misappropriation tests adequately address substitutive scraping. Copyright’s originality threshold forecloses protection for factual compilations, while the “hot news” doctrine articulated in NBA v. Motorola , with its requirement of time-sensitive, near-simultaneous reuse, is ill-suited to large-scale training data extraction. Contractual and technological controls likewise fail at web scale due to coordination and enforcement limits. Market substitution analysis avoids these limitations and survives pre-emption scrutiny. It targets competitive harm, an element absent from copyright’s exclusive rights, while respecting Feist ’s rejection of “sweat of the brow” protection by requiring proof of actual market displacement. The framework also draws a distinction between complementary uses that expand markets, such as search engine indexing, and substitutive uses that cannibalize demand, including AI-generated news summaries and synthetic content that replaces subscriptions. Applied to The New York Times v. OpenAI , the analysis shows that training LLMs on news archives to generate competing content constitutes paradigmatic substitution. ChatGPT competes directly for reader attention, and, if widely adopted, would severely undermine incentives for news production. Without legal accountability for substitutive uses, AI developers capture content value while original producers bear creation costs, risking a tragedy of the commons in information markets.

---

## uid: `doi:10.2139/ssrn.6960008`

- title: Transforming Public Administration Workflows with Multi-Agent AI: A Human-in-the-Loop Knowledge Orchestration Framework
- authors: Giuseppe Prencipe, Alessandro Tommasi, Cesare Zavattari, Giovacchino Tesi, Lorenzo Storchi, Kussai Shahin
- affiliations: not stated
- posted: 2026-06-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6960008
- keyword hits: ai agent, generative ai, retrieval-augmented

### abstract

Public administrations face increasing pressure to manage large volumes of institutional knowledge while ensuring transparency, accountability, and timely responses to citizen and council inquiries. This paper presents CARE (Council Agents for Response and Engagement), a human-in-the-loop multi-agent artificial intelligence system designed to support knowledge-intensive workflows within the Autonomous Province of Trento. CARE orchestrates specialized AI agents through a stateful workflow architecture, integrating hybrid retrieval-augmented generation over a corpus of more than 160,000 administrative documents. Unlike conventional automation approaches, the system models existing governance processes, preserves institutional responsibility boundaries, and ensures traceable document grounding in response generation. Deployed in production for six months and used by 30 administrative staff members, CARE achieved a 70\% reduction in response preparation time while maintaining human oversight and institutional control. The study contributes a socio-technical architecture for AI-assisted public administration, demonstrating how multi-agent orchestration, human-in-the-loop design, and hybrid knowledge retrieval can enhance institutional knowledge reuse without compromising accountability. Implications for digital transformation, AI governance, and responsible adoption of generative AI in the public sector are discussed.

---

## uid: `doi:10.2139/ssrn.6958664`

- title: USS-SG: A Multimodal Large Language Model Framework for Quantifying Streetscape Style and Perceived Urban Environment in Singapore
- authors: Yilu Luo, Jinmin Li
- affiliations: not stated
- posted: 2026-06-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6958664
- keyword hits: chain-of-thought, gpt-4, large language model, prompting

### abstract

The quantitative analysis of urban streetscape styles is crucial for evidence-based urban planning but remains challenging due to the subjectivity and limited scalability of traditional methods. This study proposes and validates the USS-SG (Singapore Urban Style Sensing) framework, a novel approach that leverages a multimodal large language model (MLLM) to automate the large-scale, fine-grained quantification of streetscape styles across Singapore’s diverse functional zones. We constructed the UrbanDiffBench-SG, a curated dataset of Google Street View images from four key urban typologies: early HDB estates, new HDB towns, traditional historic districts, and the Central Business District (CBD). Using the GPT-4.1 model with a structured chain-of-thought prompting pipeline, the framework generates rich textual descriptions, style keywords, functional typology labels, and emotional dimension scores for each image. A rigorous evaluation, including statistical tests and a human survey of architects and residents, demonstrated the framework’s significant ability to distinguish between functional zones. The results also revealed a systematic impact of photographic perspective, with four-directional views yielding the most comprehensive descriptions. While the AI showed moderate-to-good agreement with human experts in functional typology classification, significant gaps were identified in emotional scoring and in understanding cultural context. The USS-SG framework presents a robust, scalable tool for urban analysis, providing data-driven insights into Singapore's urban character and a reproducible methodology for global streetscape studies. To ensure reproducibility and foster wider application, the associated dataset, code, and a functional web application have been openly released, providing valuable resources for the research community.

---

## uid: `doi:10.2139/ssrn.6856700`

- title: The Feed Loop: How AI-Generated Governance Documents Amplify the Patterns They Were Designed to Suppress
- authors: Samantha Maeer
- affiliations: not stated
- posted: 2026-06-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6856700
- keyword hits: claude, llm

### abstract

This paper describes a previously undocumented self-amplifying failure mode in AI governance systems. AI-authored instruction and governance files carry stylistic biases from the model's training data into subsequent sessions via context window pattern-matching. These files simultaneously contain rules suppressing the biased patterns. Because the model pattern-matches on what it reads at higher volume than it follows explicit prohibitions, the governance layer becomes the contamination source and the suppression rule loses reliably across sessions. This paper names this mechanism The Feed Loop, documents its observation across a real production AI governance system (contAIn), and describes the architectural fix: identify and purge the contaminating files rather than strengthen the prohibition. The fix is designed to eliminate the reproductive mechanism by removing the contamination source. This mechanism sits at the intersection of three documented phenomena (training data stylistic bias, LLM instruction-following failure, and context window pattern dominance) without being covered by any of them. I propose The contAIn Method as the diagnostic and remediation framework. The contAIn Method is distinguished from prompt-level interventions: the system had the problem; the method is what the human operator applied to identify and fix it. The fix was not a better rule, it was cleaning the surface the model was reading from. This paper was partly written by the system that had the problem. Make of that what you will. AI Disclosure: This paper was drafted with the assistance of Claude (Anthropic) as a writing tool. The empirical observations, the identification of the mechanism described, the naming of The Feed Loop, the naming of The contAIn Method, and all conclusions are the original contribution of the author. AI was used to assist with prose drafting and literature search.

---
