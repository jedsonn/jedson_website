# Classification batch 25 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-25.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7151327`

- title: Cross-Model and Cross-Version Evaluation of Large Language Models in Breast Cancer Tumor Board Decision Support
- authors: ONUR ALKAN, Fatih Atalah, Arda Işık
- affiliations: not stated
- posted: 2026-07-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7151327
- keyword hits: chatgpt, gemini, gpt-4, gpt-5, large language model, large language models

### abstract

Background: Multidisciplinary breast tumor boards require integrating clinical guidelines and patient factors under time pressure, making decision support tools attractive. This study compared the performance of ChatGPT-5.2, ChatGPT-4o, and Gemini 3 in responding to simulated breast tumor board cases, evaluating response quality across five domains and readability in Turkish and English. Methods: Five synthetic breast cancer cases were submitted to three large language models. Three evaluators independently scored outputs on accuracy, completeness, clarity, audience suitability, and risk of misinformation using a 5-point Likert scale. We calculated intraclass correlation coefficients for reliability and used the Friedman test for model comparisons. Readability was assessed using the Ateşman index (Turkish) and Flesch/Gunning Fog indices (English). Results: Ninety evaluations were included; inter-rater reliability was moderate to good (intraclass correlation coefficient: 0.510-0.789). Gemini scored highest in accuracy (4.00 ± 0.99), ChatGPT-4o in completeness (4.33 ± 0.47) and clarity (4.47 ± 0.23), and ChatGPT-5.2 in specialist suitability (4.40 ± 0.40). Differences were not statistically significant (p > 0.05). English responses scored higher than Turkish ones. Turkish readability varied significantly by model (p = 0.015); English readability was comparable. Conclusions: The three models performed similarly, each showing relative domain strengths. English responses scored higher clinically, and Turkish readability varied by model. Language-specific validation is essential before clinical integration.

---

## uid: `doi:10.2139/ssrn.6204619`

- title: Seeing the Goal, Missing the Truth: Human Accountability for AI Bias
- authors: Sean S. Cao, Wei Jiang, Hui Xu
- affiliations: not stated
- posted: 2026-03-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6204619
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

This research explores how human-defined goals influence the behavior of Large Language Models (LLMs) through purpose-conditioned cognition. Using financial prediction tasks, we show that revealing the downstream use (e.g., predicting stock returns or earnings) of LLM outputs leads the LLM to generate biased sentiment and competition measures, even though these measures are intended to be downstream task–independent. Goal-aware prompting shifts intermediate measures toward the disclosed downstream objective. This purpose leakage improves performance before the LLM’s knowledge cutoff, but with no advantage post-cutoff. AI bias due to "seeing the goal" is not an algorithmic flaw, but stems from human accountability in research design to ensure the statistical validity and reliability of AI-generated measurements.

---

## uid: `doi:10.2139/ssrn.6461160`

- title: LLM Embedding-based Attribution (LEA): Quantifying Source Contributions to Generative Model's Response for Vulnerability Analysis
- authors: Reza Fayyazi, Michael Zuzak, Shanchieh Yang
- affiliations: not stated
- posted: 2026-03-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6461160
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Large Language Models (LLMs) are increasingly used for cybersecurity threat analysis, but their deployment in security-sensitive environments raises trust and safety concerns. With over 21,000 vulnerabilities disclosed in 2025, manual analysis is infeasible, making scalable and verifiable AI support critical. When querying LLMs, dealing with emerging vulnerabilities is challenging as they have a training cut-off date. While Retrieval-Augmented Generation (RAG) can inject up-to-date context to alleviate the cut-off date limitation, it remains unclear how much LLMs rely on retrieved evidence versus the model's internal knowledge, and whether the retrieved information is meaningful. This uncertainty could mislead security analysts and increase security risks. Therefore, this work proposes LLM Embedding-based Attribution (LEA) to analyze the generated responses for vulnerability exploitation analysis. More specifically, LEA quantifies the relative contribution of internal knowledge vs. retrieved content in the generated responses. We evaluate LEA on 500 critical vulnerabilities disclosed between 2016 and 2025, across three RAG settings using three LLMs. Our results demonstrate LEA’s ability to detect clear distinctions between non-retrieval, generic-retrieval, and valid-retrieval scenarios with over 95% accuracy on larger models. LEA offers security analysts with a metric to audit RAG-enhanced workflows in their enterprise network, improving the trustworthy deployment of AI in cybersecurity.

---

## uid: `doi:10.2139/ssrn.6405998`

- title: Enterprise Usage of AI Agents: A Comprehensive Survey on Applications, Frameworks, and Future Productivity Impact
- authors: Soumyajit Sarkar
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6405998
- keyword hits: ai agent, large language model, large language models, llm, llms

### abstract

The rapid advancement of large language models (LLMs) has catalyzed the emergence of AI agents-autonomous software entities capable of perceiving, reasoning, planning, and executing complex tasks within enterprise environments. This paper presents a comprehensive survey of AI agent deployment in enterprise settings, examining architectural paradigms, multi-agent collaboration frameworks, and real-world case studies across industries including customer service, software engineering, financial analysis, and supply chain management. We compare leading frameworks such as LangGraph, AutoGen, CrewAI, and Amazon Bedrock Agents, evaluating their suitability for production workloads. Furthermore, we analyze quantitative productivity metrics and return-on-investment data from early adopters, and project the transformative impact of AI agents on enterprise productivity through 2030. Our findings indicate that enterprises deploying AI agents report 35-55% improvements in operational efficiency, with multi-agent architectures enabling previously infeasible levels of automation in knowledge-intensive workflows.

---

## uid: `doi:10.2139/ssrn.6608518`

- title: MedRAG: Retrieval-Augmented Generation for Medical QA-Comparing Base and RAG-Augmented LLM Performance on Evidence from Peer-Reviewed Clinical Research
- authors: Kunal Dhanda
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6608518
- keyword hits: large language model, large language models, llama, llm, llms, retrieval-augmented

### abstract

Large language models (LLMs) deployed for medical question answering must provide precise, evidencegrounded responses-yet their parametric knowledge frequently fails on specific quantitative findings from recent clinical trials and systematic reviews. We build a medical retrieval-augmented generation (MedRAG) system by indexing 5025 peer-reviewed papers across 104 clinical domains-retrieved via PubMed and the Consensus academic search engine, embedded using sentence-transformers, and stored in a ChromaDB vector database. We evaluate a local LLaMA 3.2 base model against its RAG-augmented counterpart on 25 medical QA questions stratified by domain and difficulty. The base model achieves 0.760 accuracy while the RAG-augmented system achieves 1.000, a gain of 24 percentage points. Qualitative analysis of the 6 base-model failures reveals two distinct hallucination patterns: (i) fabrication, where the model invents specific trial names, authors, and effect sizes with confident language; and (ii) confident substitution, where the model returns plausible but numerically wrong statistics. RAG eliminates both patterns by grounding responses in retrieved evidence. Mean gold-keyword hit rate improves from 2.36 to 4.20 keywords per question. These results demonstrate that lightweight RAG over curated clinical literature substantially improves LLM factual accuracy for medical QA on consumer hardware.

---

## uid: `doi:10.2139/ssrn.6591118`

- title: COLLEGIATE COMPANION: ENHANCING STUDENT SUPPORT USING LLM-POWERED CHATBOTS
- authors: Amaanudeen s
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6591118
- keyword hits: large language model, large language models, llama, llm, llms, retrieval-augmented

### abstract

In recent years, the integration of artificial intelligence in education has gained significant attention due to its potential to enhance personalized learning and academic support systems. This paper presents Collegiate Companion, an AI-powered academic support system designed to provide accurate, subject-specific assistance using Large Language Models (LLMs) integrated with Retrieval-Augmented Generation (RAG). The system addresses key challenges in traditional academic support, including limited instructor availability, repetitive query handling, and dependence on internet connectivity. Unlike conventional cloud-based chatbots, the proposed system operates entirely offline using lightweight local models deployed through Ollama, ensuring privacy, reliability, and uninterrupted access. The architecture leverages structured document ingestion, embedding generation using FastEmbed, and efficient vector storage through ChromaDB to retrieve relevant academic content from course-specific PDFs. The retrieved context is used to generate precise and syllabus-aligned responses, significantly reducing hallucination and improving answer relevance. Additionally, a feedbackdriven mechanism is incorporated to continuously enhance system performance. Experimental evaluation demonstrates improved response accuracy (88-92%) and reduced latency (1.5-3 seconds). The system provides scalable academic assistance while maintaining data privacy. The proposed solution highlights the potential of locally deployed LLM systems in transforming personalized education.

---

## uid: `doi:10.2139/ssrn.6577019`

- title: Large Language Models in Qualitative Research: Governance, Validity, and the Limits of Computational Assistance
- authors: Moses Boudourides
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6577019
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

Qualitative and mixed-methods research faces intensifying pressure from expanding data volumes, prompting interest in large language models (LLMs) as analytic aids. However, LLM fluency risks conflating linguistic coherence with interpretation, obscuring judgment and scholarly responsibility. This article examines a protocol for LLM-assisted qualitative coding and literature synthesis. Drawing on qualitative traditions centered on meaning and theory-building, we develop a framework organized around research design, human judgment, and three dimensions of validity: interpretive, integrative, and bibliographic. Two empirical demonstrations ground the framework: a Dual-Coding Experiment on fifteen open-access interview transcripts reveals both “Context Collapse” and “Analytical Reach,” while a Bibliographic Stress Test documents a 63.2 percent distortion rate in LLM-generated literature syntheses. Responsible integration of LLMs requires strengthening—not relaxing—the methodological commitments that define qualitative inquiry.

---

## uid: `doi:10.2139/ssrn.6396898`

- title: FrameScope: A Real-Time Framework for Ideological Bias Detection in User-Generated Text
- authors: Zachary Adam
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6396898
- keyword hits: gemini, generative ai, gpt-4, large language model, llm, prompt engineering

### abstract

The proliferation of algorithmically curated content and the increasing polarization of public discourse have generated urgent demand for automated tools capable of detecting ideological bias in natural language text. This paper presents FrameScope, an open-source, real-time bias detection framework that classifies user-generated text along an ideological spectrum by leveraging a multi-model ensemble architecture. The system submits input text simultaneously to three large language model (LLM) backends-OpenAI GPT-4o, Google Gemini 1.5 Pro, and an open-source alternative via HuggingFace Transformers-each configured with identical classification prompts. The independent classifications are aggregated through a weighted consensus mechanism that produces a composite bias score ranging from-1.0 (strongly biased toward Position A) to +1.0 (strongly biased toward Position B), along with a confidence metric derived from inter-model agreement. A pre-compiled response bank, indexed by bias intensity and direction, delivers deterministic contextual feedback without relying on generative AI for response content, thereby circumventing content policy restrictions inherent in commercial LLM APIs. The system is implemented as a FastAPI backend with a React-based web dashboard, providing real-time visualization of bias classification, model agreement matrices, and historical analysis. This paper details the system architecture, the prompt engineering strategy for bias classification, the consensus aggregation algorithm, the response bank design, and presents a comparative evaluation of classification accuracy across the three model backends using a manually annotated corpus of 500 politically and ideologically charged text samples. Results indicate that the multi-model ensemble achieves 14.3 percent higher classification accuracy than any individual model, while the inter-model agreement metric provides a reliable proxy for classification confidence. FrameScope is released under the MIT License and is freely available for research and educational use.

---
