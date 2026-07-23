# Classification batch 11 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-11.answer.json` as a JSON array.

---

## uid: `doi:10.5281/zenodo.21380237`

- title: Harnessing LLMs for Reliable Academic Supervision: A Comparative Study
- authors: Akash Raj
- affiliations: not stated
- posted: 2026-07-16
- source: arXiv
- link: https://arxiv.org/abs/2607.14707v2
- keyword hits: gpt-4, gpt-5, large language model, large language models, llm, llms

### abstract

Large language models routinely produce fluent answers to single-shot prompts, yet deploying them as reliable components of a domain decision system is substantially harder. Closing this gap is the work of harness engineering: the deliberate composition of deterministic scaffolding (symbolic filters, retrieval, schema-typed I/O, LLM-as-judge loops, HITL gates, persistent state, audit trails) around an LLM core. We present a case study in academic supervision, a domain combining high-stakes recommendation, longitudinal accountability, and structured operational workflows. We compare a baseline Academic Supervision Assistant (ASA), a GPT-5 chatbot with no scaffolding, against a multi-module system, Academic Supervision System (ASuS) that wraps the much smaller GPT-4o-mini in a LangGraph harness with symbolic semantic retrieval, schema-validated outputs, LLM-as-judge with bounded retry, HITL gates, deterministic weighted risk scoring with LLM narration, and a per-node SQLite audit trail. The evaluation rubric is retargeted at six harness-mechanism dimensions (grounding, explainability, consistency, process integrity, cognitive load, constraint adherence). A blind ten-rater hybrid evaluation, supplemented by a 2 x 2 model-harness ablation, finds that ASuS, despite using a much smaller base model, outscores ASA on every dimension. Across ten raters the pooled mean for ASuS is 4.08 versus 1.23 for ASA, and 8 of 10 raters reject the null at alpha = 0.05 on a paired Wilcoxon test; full numbers are in Sections 6.4 and 6.7. The ablation confirms that the structural contributions of the harness are largely model-invariant. We extract seven recurring harness-engineering patterns and argue that where reliability, traceability, and institutional consistency matter more than open-ended fluency, harness engineering challenges the prevailing 'bigger model is better' intuition.

---

## uid: `doi:10.2139/ssrn.7135523`

- title: Integrating Artificial Intelligence, Large Language Models and Natural Language Processing into Qualitative Research: A Comparative Analysis
- authors: Holly Shannon, Joseph-Omer Dyer, Bryce Bogie, Michael Kalu, Alessandro Reis, Mirella Veras
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7135523
- keyword hits: chatgpt, gpt-3, gpt-4, large language model, large language models, llm, llms

### abstract

Objectives: Qualitative analysis can offer experiences and perspectives not captured in quantitative data, however it can be a time-consuming and subjective process. Artificial intelligence (AI) could improve the efficiency and detection of patterns in qualitative analysis. We aimed to directly compare human-conducted thematic analysis with large language models (LLMs) to compare the resultant themes and how the themes varied in terms of accuracy, efficiency, and depth of analysis. Additionally, we explored how natural language processing (NLP) can supplement qualitative analysis through topic modeling and semantic analysis. Methods: Human thematic analysis was conducted on focus group data transcripts using an inductive reflexive approach. Parallel inductive thematic analyses were conducted using LLMs (ChatGPT versions 3.5 and 4o). Topic modeling and semantic analysis were also conducted with AI-assisted NLP in R and Python. Results: ChaGPT-3.5 generated thirteen themes, GPT-4o generated nine, and human analysis identified five themes, with fourteen subthemes. Cosine similarity analysis revealed limited convergence with human-derived themes for ChatGPT-3.2 (21.2%) and ChatGPT-4o (10.5%). Additionally, NLP analyses had limited interpretability due to the prevalence of filler words; although, both methods were consistent in identifying trust as the most common emotional expression.Conclusion: Both LLM models (ChatGPT versions 3.5 and 4o) were not superior to human-conducted thematic analysis. Using AI tools, such as LLMs and NLP, can support qualitative analysis by enhancing efficiency, but remain limited in interpretive coding and theme refinement.

---

## uid: `doi:10.2139/ssrn.7123198`

- title: Harnessing LLMs for Reliable Academic Supervision: A Comparative Study A Case Study in Harness Engineering
- authors: Akash Raj
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7123198
- keyword hits: gpt-4, gpt-5, large language model, large language models, llm, llms

### abstract

Large language models routinely produce fluent answers to single-shot prompts, yet deploying them as reliable components of a domain decision system is substantially harder. Closing this gap is the work of harness engineering: the deliberate composition of deterministic scaffolding (symbolic filters, retrieval, schema-typed I/O, LLM-as-judge loops, HITL gates, persistent state, audit trails) around an LLM core. We present a case study in academic supervision, a domain combining high-stakes recommendation, longitudinal accountability, and structured operational workflows. We compare a baseline (ASA), a GPT-5 chatbot with no scaffolding, against a multi-module system (ASuS) that wraps the much smaller GPT-4o-mini in a LangGraph harness with symbolic-semantic retrieval, schema-validated outputs, LLM-as-judge with bounded retry, HITL gates, deterministic weighted risk scoring with LLM narration, and a per-node SQLite audit trail. The evaluation rubric is retargeted at six harness-mechanism dimensions (grounding, explainability, consistency, process integrity, cognitive load, constraint adherence). A blind ten-rater hybrid evaluation, supplemented by a 2 × 2 model-harness ablation, finds that ASuS, despite using a much smaller base model, outscores ASA on every dimension. Across ten raters the pooled mean for ASuS is 4.08 versus 1.23 for ASA, and 8 of 10 raters reject the null at α = 0.05 on a paired Wilcoxon test; full numbers are in §6.4 and §6.7. The ablation confirms that the structural contributions of the harness are largely model-invariant. We extract seven recurring harnessengineering patterns and argue that where reliability, traceability, and institutional consistency matter more than open-ended fluency, harness engineering challenges the prevailing 'bigger model is better' intuition.

---

## uid: `doi:10.2139/ssrn.7120478`

- title: Foundation Models and Large Language Models in Healthcare: A Narrative Review of Applications, Evidence, and Emerging Challenges
- authors: Babatola Joshua
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7120478
- keyword hits: fine-tuning, foundation model, large language model, large language models, llm, llms, prompting

### abstract

Foundation models and large language models (LLMs) have moved rapidly from generalpurpose natural language processing tools to candidate components of clinical infrastructure. Trained on broad corpora and subsequently adapted through fine-tuning, retrieval augmentation, or prompting, these systems now demonstrate competitive performance on medical licensing examinations, clinical documentation, diagnostic reasoning, and patient communication tasks. This review synthesises the technical foundations of LLMs in healthcare, traces their evolution from transformer-based architectures to multimodal clinical foundation models, and critically appraises the peer-reviewed evidence base underpinning their clinical use. Drawing on studies published predominantly between 2019 and 2025, the review examines applications across documentation, decision support, patient-facing communication, and biomedical research, and situates these applications within a broader discussion of reliability, bias, privacy, interpretability, and regulatory status. The evidence indicates that although benchmark and simulated-case performance is often impressive, prospective clinical validation remains limited, and demonstrated capability does not yet equate to demonstrated safety or effectiveness in routine care. Persistent challenges include hallucination, uneven performance across demographic subgroups, ambiguous regulatory classification, and the practical difficulty of integrating probabilistic language systems into accountable clinical workflows. The review concludes that foundation models are best conceived as adjunctive tools requiring structured human oversight, robust governance, and prospective evaluation rather than autonomous clinical agents, and it proposes priority directions for future research, including standardised evaluation frameworks, equity-focused benchmarking, and longitudinal outcome studies.

---

## uid: `doi:10.2139/ssrn.6638719`

- title: A Comprehensive Survey on Prompting Strategies and Retrieval-Augmented Generation for Automated Financial Metrics Extraction
- authors: Mokshita Kochhar, Manish Khodaskar
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6638719
- keyword hits: large language model, large language models, llm, llms, prompting, retrieval augmented, retrieval-augmented

### abstract

There is an exponential growth in unstructured data in finance these days, such as earnings reports and call transcripts, and regulatory filings too, and this is growing exponentially, making it difficult to manage manually. Hence, it is essential to have automated systems to obtain key metrics without wasting time. This survey is all about exploring the existing methods, especially large language models along with various prompting strategies and another technique called "Retrieval Augmented Generation" to obtain information about finance. The survey includes more than 30 papers, starting from traditional NLP methods, moving to neural networks, and finally to recent LLMs, along with various checks to see how they perform. The results are based on various datasets, including a few, such as "FinQA," which includes 8,281 pairs for question answering, "ConvFinQA," which includes 3,892 conversations and more than 14,000 questions within them, and "TAT-QA," which includes 16,552 questions within them. State of the art models achieve 58 to 62%, but human experts achieve 89 to 91%, and this 30% gap is what's left to be addressed. Some key issues arise, such as numerical multi-step reasoning, which is somewhat tricky, and combining all kinds of heterogeneous data sources, and how to best acquire appropriate domain expertise for finance. That's what it seems to be, and that's what's holding everything back. For anyone looking to combine natural language processing and finance tech, this is a good resource, even though some of it is a bit scattered in how it all ties together.

---

## uid: `doi:10.2139/ssrn.6400178`

- title: Enhancing Information Retrieval through Multi-Agent Reasoning Frameworks in Open Deep Search Architectures
- authors: Faith Harris
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6400178
- keyword hits: gpt-4, large language model, large language models, llm, llms, retrieval-augmented

### abstract

The exponential growth of digital information and the increasing complexity of user queries have exposed fundamental limitations in traditional information retrieval systems and conventional retrieval-augmented generation (RAG) pipelines. While large language models (LLMs) have demonstrated remarkable capabilities in natural language understanding and generation, their application to deep information seeking tasks-queries requiring multi-hop reasoning, synthesis across disparate sources, and iterative refinement-remains constrained by monolithic architectures and opaque, proprietary systems. This work presents a comprehensive examination of multi-agent reasoning frameworks operating within open deep search architectures, a paradigm that decomposes complex information retrieval tasks into collaborative, specialized agents coordinated through transparent and extensible workflows. We systematically analyze the architectural foundations, methodological innovations, and empirical performance of contemporary multi-agent search systems including ManuSearch, Open Deep Search (ODS), Table-as-Search, and SPD-RAG. Our investigation reveals that hierarchical multi-agent architectures, featuring specialized roles such as planning agents, search agents, reading agents, and coordinating supervisors, consistently outperform single-agent baselines and closed-source competitors on benchmarks requiring deep reasoning over long-tail entities and wide-scale information collection. Key innovations include query and subgraph dual evolution mechanisms, reinforcement learning for dynamic tool selection, and parallelized document-level processing that optimizes both accuracy and computational efficiency. The findings demonstrate that open deep search architectures not only democratize access to advanced information retrieval capabilities but also establish new performance standards, with frameworks like ODS-v2 surpassing GPT-4o Search Preview on the FRAMES benchmark and SPD-RAG achieving superior results on multi-document QA at substantially lower computational cost. This work contributes a unified taxonomy of multi-agent reasoning frameworks, a synthesis of design principles for open search architectures, and a roadmap for future research addressing challenges in tool integration scalability, heterogeneous data source harmonization, and adaptive reasoning under uncertainty.

---

## uid: `doi:10.2139/ssrn.6445618`

- title: VWAB: Vibe Write App Build A Framework for Domain-Expert-Driven Application Development in the Age of Generative AI
- authors: Raghu Kundurthi
- affiliations: not stated
- posted: 2026-04-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6445618
- keyword hits: generative ai, large language model, large language models, llm, llms, prompting

### abstract

We introduce VWAB (Vibe Write App Build), a conceptual framework describing a novel paradigm of software application development in which domain experts-rather than software engineers-serve as the primary builders, with large language models (LLMs) functioning as the complete technical scaffold. Distinct from Vibe Coding, which describes LLM-assisted acceleration of developer workflows, VWAB addresses the emergent phenomenon wherein practitioners with deep subject matter expertise but limited programming knowledge can produce deployable, production-quality applications through iterative natural language prompting. We formalize the four VWAB pillars: (1) Vibe-domain intuition as the primary input modality; (2) Write-narrative-driven specification replacing formal code authorship; (3) App-the production artifact as the terminal output, not a prototype or demonstration; and (4) Build-the LLM as complete technical orchestrator across the full stack. We present a case study in which a Unity Catalog Data Governance Architect with zero mobile development experience produced a functional iOS/Android crossword puzzle application using the VWAB methodology, overcoming a sequence of environment configuration failures, dependency version conflicts, SDK mismatches, and hardware constraints exclusively through contextual prompting. We discuss VWAB's implications for enterprise knowledge worker productivity, the democratization of software authorship, and the evolving boundary between subject matter expertise and technical execution. We argue that VWAB represents a qualitative phase transition in the human-AI collaboration model-from AI as tool to AI as co-builder-with significant implications for workforce transformation, enterprise capability development, and the epistemology of software creation.

---

## uid: `doi:10.2139/ssrn.6672580`

- title: Distinguishing the Roles of Agentic AI in ManufacturingEcosystem
- authors: nowrin Akter surovi, Paul Witherell, Maja Vukovic, Soundar Kumara
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6672580
- keyword hits: agentic, foundation model, large language model, large language models, llm, llms

### abstract

Agent-based systems have been widely adopted in industries such as communication, business, and manufacturing, to support distributed decision-making, scalability, and responsiveness in complex environments. In manufacturing, conventional agent-based systems automate tasks ranging from product design to supply chain management, but they remain constrained by fixed rules and narrow-domain models, limiting their ability to adapt to changing conditions or reason over unstructured and multimodal data. Recent advances in artificial intelligence, particularly Large Language Models (LLMs) and multimodal Foundation Models (FMs), introduce new capabilities such as contextual analysis, flexible task execution, and natural language interaction. However, their systematic role within manufacturing agent-based systems remains insufficiently explored. In this paper, we investigate Agentic AI, defined as LLM-driven, goal-oriented agents operating within structured workflows, and analyze how it extends the roles and behaviors of agents in the manufacturing ecosystem. We present a system-level framework that formalizes agent roles and enables role-constrained orchestration with human-in-the-loop oversight in manufacturing systems. Our approach integrates Agentic AI through explicit role definitions, structured task decomposition, and closed-loop human supervision. The approach is illustrated through a melt-pool image analysis case study in powder bed fusion additive manufacturing, and contrasted with a conventional agent-based pipeline. The results highlight functional differences in adaptability, interpretability, and decision support, indicating that Agentic AI systems can complement conventional agents by providing contextual analysis and actionable recommendations, where human oversight is important. Our framework outlines role-constrained AI capabilities in manufacturing, illustrating how Agentic AI can transform, extend, and integrate with existing manufacturing agent-based systems.

---
