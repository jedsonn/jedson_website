# Classification batch 26 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-26.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6668914`

- title: Retrieval-Augmented Generative AI for Analyzing Entrepreneurship in Africa
- authors: Roy Esibe, Muhammad Aliyu, Jesse Thornburg, Erik Stam, João Barros
- affiliations: not stated
- posted: 2026-04-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6668914
- keyword hits: generative ai, large language model, large language models, llm, llms, retrieval-augmented

### abstract

Systematic knowledge about entrepreneurship in Africa and other emerging economies is constrained by a structural data problem: the processes through which founders build high-growth ventures are richly documented in informal digital sources, including YouTube interviews, podcasts, and recorded conference appearances, but these sources have been unanalyzable at scale until now. This paper presents a validated, scalable methodology based on retrieval-augmented generation (RAG) and large language models (LLMs) for reconstructing founder journeys from fragmented multimodal content. We apply the methodology to the 16 founders of Africa’s six unicorn ventures as of 2024, processing over 1,000 YouTube videos and 9 hours of podcast audio into more than 30,000 embedded text chunks. The pipeline integrates multi-query expansion, semantic retrieval, structured narrative generation, and a refinement stage that iteratively improves factual grounding and removes unsupported claims . It is evaluated using precision, recall, F1, and faithfulness. We introduce the Context Completeness Score (CCS), a novel metric that assesses the causal and thematic depth of generated narratives beyond standard faithfulness measures. Results demonstrate high-fidelity narratives with faithfulness scores of 0.94 to 0.99. A key finding is that narrative quality depends more on thematic diversity than on data volume: reliable narratives are achievable with 800 to 1,200 well-curated text chunks. The methodology enables systematic analysis of founder journeys in data-sparse contexts, opening a new empirical pathway for entrepreneurship research in Africa and other emerging economies.

---

## uid: `doi:10.2139/ssrn.6668971`

- title: Large language models lack strategic agency: A Luhmannian critique of AI in energy governance
- authors: Samseer R H, Asokan Vasudevan
- affiliations: not stated
- posted: 2026-04-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6668971
- keyword hits: ai agent, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are increasingly deployed in energy system decision-making—setting electricity prices, determining cross-border power purchases, and easing renewable energy regulations. Yet recent empirical evidence reveals a critical paradox: LLMs exhibit a structural bias toward institutional conformity, a phenomenon termed Synthetic Optimism, favoring compliance over the creative resistance displayed by human decision-makers. This Perspective argues that Synthetic Optimism is not an inherent limitation of LLM technology but a consequence of flawed socio-institutional design. Current deployments ask a single LLM to simultaneously simulate multiple incommensurable strategic rationalities—economic efficiency, legal compliance, political legitimacy, and environmental sustainability—without any architecture to manage their inherent contradictions. Drawing on Luhmann's neo-functionalist systems theory, which conceptualizes modern society as functionally differentiated into autonomous subsystems each operating on distinct binary codes, we propose an alternative multi-agent architecture. Function-specific AI agents operate independently on subsystem-specific codes (profitable/unprofitable; legal/illegal; power/lack of power; sustainable/unsustainable), coordinated through structural coupling rather than normative consensus. Applying this framework to a constrained electricity grid where government capacity is reduced by election protocols, we demonstrate how multi-agent architectures generate context-sensitive strategic options that evade the conformity bias of single-LLM systems. We conclude with three actionable design levers for grid regulators and digital infrastructure policymakers: subsystem mapping prior to AI deployment, prohibition of single-LLM "logic monopolies" in high-stakes decisions, and mandatory tension vector reporting for AI-assisted choices.

---

## uid: `doi:10.2139/ssrn.6673101`

- title: Prompting to Extract Data Inputs for Accounting Systems from Heterogeneous Data Sources
- authors: Juliane Wutzler, Florina G. Hutter
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6673101
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

Research Question: Can Large Language Models (LLMs) be used as low-cost tools to efficiently and effectively extract data from heterogeneous sources fed into accounting systems and processes? Motivation: Accounting departments use a variety of data from a wide range of sources and feed them as inputs into their accounting systems and processes. Extracting such data often requires manual effort. Large Language Models may be a low-cost way to extract data without substantial upfront investments. Prior literature documents the potential of LLMs for data extraction in other domains (e.g., Fornasiere et al., 2024) or for long and largely semantic accounting documents (Li et al., 2025). While these guidelines may be transferable to semantic data feeding into accounting systems, such as order emails, they are likely not directly transferable to non-semantic, semi-structured data sources, such as invoices. Idea: In our proof-of-concept, we test whether general prompting guidelines from prior literature apply to both non-semantic but semi-structured (i.e., invoices) and semantic but unstructured data sources (i.e., order emails) used as inputs into the accounting system. We then identify these issues and derive guidelines for practical use. Data: A synthetic dataset consisting of 46 heterogeneous PDF invoices and 10 order emails in Outlook format was created. Synthetic data allow explicitly including challenging variations and eliminate data privacy concerns. Tools: Following design science research, we test and improve LLM (Mixtral-8x7B) prompts for Named Entity Recognition derived from prior literature to establish accounting-specific prompt guidelines (Moundas et al., 2024). Findings: Using Large Language Models to extract data that can be used as inputs into accounting processes requires case-specific adjustments to general prompting guidelines derived from the literature. We develop solutions to problems resulting from general prompting guidance and define transferable strategies for creating prompts that allow the extraction of data from semantic and non-semantic accounting data sources. Contribution: We provide guidance on how LLMs can extract data for use in accounting systems. Data sources differ substantially from those in prior literature (Li et al., 2025).

---

## uid: `doi:10.2139/ssrn.6672583`

- title: A modular retrieval-augmented framework for agent-guided RFQ documentation in power transformer engineering
- authors: ZhiYun Huang, Amy Trappey, Steven  G. Pudney
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6672583
- keyword hits: agentic, large language model, large language models, llm, llms, prompt engineering, retrieval-augmented

### abstract

Request-for-quotation (RFQ) documents play a pivotal role in the early stages of energy infrastructure projects by formalizing technical specifications and design requirements, particularly for high lead time equipment. However, RFQ preparation is a time-consuming and expertise-intensive process due to the heterogeneity and technical depth of specification content. InefficientRFQ preparation can lead to extended procurement cycles and increased engineering workload. This study proposes an intelligent RFQ knowledge system that leverages agentic-AI and LLMs in conjunction with RAG to support the drafting of reliable RFQs, which is subsequently applied to real industrial power transformer projects. The proposed system transforms historical RFQ documents and domain-specific engineering specifications into a modular, vectorized knowledge database, enabling context-aware retrieval and controlled content generation, thereby forming a draft for reference by engineers. It supports the extraction and synthesis of technical specifications, accessories, and testing requirements while maintaining traceability through domain-specific prompt engineering and modular generation strategies. The main objectives of this research are to: (1) develop a modular-based RFQ knowledge system that decomposes engineering specifications into reusable components, distinguishing between general specifications and project-specific requirements to support selective retrieval and consistent reuse of engineering knowledge. ; (2) design a human-AI collaborative RFQ drafting framework in which large language models (LLMs) act as engineering knowledge support tools. ; and (3) establish a dual-track evaluation framework that assesses system effectiveness from both technical and practical perspectives. Quantitative metrics evaluate generation quality and retrieval grounding, while qualitative analysis examines engineering usability and workflow integration. Experimental results demonstrate that the proposed modular and dual-evaluation framework effectively reduces manual RFQ drafting effort while establishing a verifiable, modular paradigm for engineering document generation.

---

## uid: `doi:10.2139/ssrn.6678618`

- title: Large Language Models for Intelligent Data Stewardship in Enterprises: Architectures, Provenance, and Evidence-Mapped Governance
- authors: Nagender Yamsani
- affiliations: not stated
- posted: 2026-04-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6678618
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Enterprises increasingly operate in data ecosystems characterized by extreme heterogeneity, spanning legacy databases, cloud-native platforms, streaming pipelines, and unstructured knowledge repositories, all under mounting regulatory, ethical, and operational scrutiny. In this context, recent advances in large language models (LLMs) notably transformer-based architectures combined with retrieval-augmented generation (RAG), dense passage retrieval (DPR), programmatic and weak supervision, and knowledge-graph grounding offer a unifying technical substrate for intelligent data stewardship at enterprise scale. By embedding stewardship objectives such as FAIR principles, end-to-end provenance, semantic interoperability, and continuous data quality assurance directly into LLMenabled workflows, organizations can move beyond static catalogs toward adaptive, context-aware systems capable of automated metadata enrichment, lineage-aware question answering, policy-sensitive data discovery, and assisted remediation of quality and compliance issues. This article synthesizes these foundations into an integrated reference architecture for LLM-assisted stewardship, and introduces an evidence-mapping methodology that operationalizes governance assessment by aligning publicly observable signals with established standards and controls. Through an applied case study of Inspire Brands' AI-driven governance initiatives, we demonstrate how evidence mapping enables a non-invasive yet systematic evaluation of organizational readiness, surfacing both strengths and gaps without requiring privileged internal disclosures. Finally, we outline open research challenges including evaluation metrics for trustworthiness and explainability, robustness under regulatory change, and human-in-the-loop validation patterns and offer practical recommendations to guide enterprise adopters in responsibly deploying LLMs as first-class components of modern data governance and stewardship ecosystems.

---

## uid: `doi:10.2139/ssrn.6582258`

- title: I-Tuning: Personalized Large Language Models as Cognitive Augmentation - Why Individualized AI Fine-Tuning Poses Distinctive Constitutional Risks
- authors: Wilhelm Haverkamp
- affiliations: not stated
- posted: 2026-04-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6582258
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

This paper introduces 'I-tuning'-the individualised fine-tuning of large language models on personal data corpora-as a qualitatively new form of cognitive augmentation. Two variants are distinguished. I-Tuning-Lite (training on recent communications, writing, and interaction logs) is near-term feasible and already approximated by current personalised writing tools. I-Tuning-Full (training on a comprehensive longitudinal record spanning medical, developmental, behavioural, and experiential data from early life onward) is a speculative but technically coherent endpoint warranting preemptive governance. Claims in this paper are calibrated to the distinction: risks attributed to I-Tuning-Lite are supported by existing evidence; risks attributed to I-Tuning-Full are advanced as theoretically grounded projections. Grounded in the extended mind tradition (Clark and Chalmers, 1998) and drawing on Clark (2025), who argues in Nature Communications that generative LLMs I-Tuning: Personalized LLMs as Cognitive Augmentation Preprint cessful extension, and grounds a structured response to libertarian transhumanist objections. A tiered governance framework-mandatory constitutional disclosure, architectural transparency features, and periodic professional capability assessment-follows from the structure of the harms.

---

## uid: `doi:10.2139/ssrn.6672582`

- title: A Trustworthy Hybrid Human–AI Framework Enabled by LLM for Context-Aware and Explainable Stress Detection and Intervention in Safety-Critical Environments
- authors: Shuhui Lyu, Chun-Hsien Chen, Ziqing Xia, Kendrik Yan Hong Lim
- affiliations: not stated
- posted: 2026-04-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6672582
- keyword hits: agentic, in-context learning, large language model, large language models, llm, retrieval-augmented

### abstract

In safety-critical environments characterized by volatility, uncertainty, and complexity, operators are persistently exposed to elevated stress levels, posing significant threats to both operational safety and operator well-being. Existing AI-driven stress detection approaches rely on task-specific supervised models with limited scalability and lack the explainability and reliability required for high-stakes applications. This paper introduces a trustworthy hybrid human–agentic AI framework integrating In-Context Learning (ICL) with a Knowledge Graph-enhanced Retrieval-Augmented Generation (GraphRAG) module for explainable stress detection and personalized intervention. The ICL component enables few-shot, context-aware stress detection by fusing physiological signals with multi-contextual information, and the GraphRAG module grounds explanations and intervention recommendations in structured domain knowledge, reducing hallucination in large language models (LLM). The framework is validated through a Vessel Traffic Service (VTS) case study, using multimodal data collected from real-world operations over a five-month on-site deployment. Without task-specific training, the ICL-based predictor achieves an F1-score of 88.37% with only 256 examples, surpassing traditional machine learning baselines. GraphRAG constructs a domain-specific knowledge graph linking physiological indicators, operational contexts, stress states, and intervention strategies, enabling multi-hop reasoning for evidence-grounded, traceable recommendations. Expert evaluations confirm that GraphRAG-enhanced outputs significantly improve accuracy, usability, and trustworthiness over LLM-only baselines. This work advances occupational stress management by transitioning from passive monitoring toward a trustworthy, human-centred decision-support paradigm with strong potential for real-world deployment in safety-critical environments.

---

## uid: `doi:10.2139/ssrn.6683241`

- title: Think, Retrieve, Verify: Multi-Agent Collaboration for Retrieval Augmented Generation Systems
- authors: Dr Reddy B, MEREDDY SRISHTI REDDY, GOLLEN MIHIR, Meenakshi Yadugani
- affiliations: not stated
- posted: 2026-04-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6683241
- keyword hits: agentic, ai agent, large language model, large language models, llm, llms, retrieval augmented

### abstract

The collaboration of AI Agents with the Retrieval Augmented Generation (RAG). framework can solve major drawbacks in RAG. The proposed work introduces an agentic RAG framework to help ground the Large Language Models (LLMs) and generate answers using retrieved content only. The system also verifies if all the information extracted from external sources is safe. This Multi-agent RAG pipeline reduces majority of the drawbacks and gives verified and secured outputs. It also aims to respond accurately to ambiguous user queries by taking on different perspectives of a query. The model uses a novel safety measure to ensure the generated answer is safe while using lower API Calls. The Framework is divided into three layers: Think, Retrieve, Verify, to simplify the process. The results achieved, when tested on benchmark dataset, HotpotQA are improved by 18% when compared to existing models.

---
