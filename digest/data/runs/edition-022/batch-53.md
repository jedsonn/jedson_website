# Classification batch 53 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-53.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7030838`

- title: The Next Phase of Generative AI in Rheumatology
- authors: Alfredo Madrid, Beatriz Merino
- affiliations: not stated
- posted: 2026-07-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7030838
- keyword hits: chatgpt, generative ai, llm, prompt engineering, retrieval-augmented

### abstract

The public release of ChatGPT in late 2022 introduced many rheumatologists to conversational artificial intelligence (AI), and the first wave of interest focused on asking chatbots clinical questions, testing diagnostic accuracy, summarising records, generating patient explanations, and supporting education and research. This perspective argues that the next short- to mid-term transformation in rheumatology may come less from a single, larger chatbot than from how language models are connected to reliable knowledge, to the clinical context of an individual patient, and to one another. We introduce a set of concepts at different stages of maturity: established approaches such as curated knowledge bases and retrieval-augmented generation (RAG ), together with more recent, structured extensions such as GraphRAG and LLM-Wiki ; small and open language models; the shift from prompt engineering to context engineering; software practices including spec-driven development, vibe coding, reusable skills and loop engineering; and interoperability protocols such as the model context protocol (MCP) and the agent-to-agent (A2A) protocol. For each, we separate current evidence from future-oriented expectation, noting that several concepts rest on industry documentation rather than peer-reviewed clinical validation and that none has yet been validated for rheumatology care. To make two of these ideas concrete, we provide illustrative, non-clinical supplementary examples: an LLM-Wiki assembled from EULAR and ACR recommendations, and a reusable visit-preparation skill. We conclude that the central challenge is no longer only to ask better questions of chatbots, but to design knowledge-grounded, context-aware, and accountable clinical AI systems that keep rheumatologists at the centre of care.

---

## uid: `doi:10.2139/ssrn.7068258`

- title: AI Honesty: Why It Should Become an Independent Field in AI Ethics
- authors: Majid Tavakolian
- affiliations: not stated
- posted: 2026-07-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7068258
- keyword hits: generative ai, large language model, large language models

### abstract

Over the past decade, AI ethics has become one of the most important branches of interdisciplinary research in philosophy, computer science, and technology policy (Floridi et al. 2018; Jobin, Ienca, and Vayena 2019; UNESCO 2021). Research in this field has primarily focused on issues such as algorithmic fairness, transparency, accountability, safety, privacy, and AI alignment (Russell 2019; NIST 2023; OECD 2019). However, the emergence of large language models and generative AI systems has revealed that one of the most fundamental ethical issues of this technology still lacks an independent theoretical framework: AI Honesty (Bommasani et al. 2021; Weidinger et al. 2022). This article argues that many emerging challenges-including sycophancy, hallucination, fabricated information, the false confirmation of users' beliefs, and the distortion of reality-are all different manifestations of a more fundamental problem, which can be described as the absence of honesty in the behavior of intelligent systems (Wei et al. 2023; Ji et al. 2023). The article further demonstrates that the prevailing concept of AI Alignment, although a necessary condition for developing beneficial and safe systems, is not sufficient by itself to guarantee honesty (Russell 2019; Bai et al. 2022). A system may be aligned with the objectives of its designers while still generating false or misleading information in order to increase user satisfaction, reduce conflict, or maintain engagement (OpenAI 2025; Anthropic 2025). Accordingly, this article proposes that AI Honesty should be defined as an independent research field within AI ethics-a field devoted to studying the relationship between truth, trust, communicative behavior, and the epistemic responsibility of intelligent systems. The article first reviews the literature on AI alignment, sycophancy, and hallucination, then proposes a philosophical definition of AI Honesty, and finally introduces a conceptual framework for evaluating the honesty of AI models.

---

## uid: `doi:10.2139/ssrn.6519098`

- title: Covert Sycophancy in Large Language Models: A Behavioral Taxonomy from Naturalistic Observation
- authors: Michael Kitamura
- affiliations: not stated
- posted: 2026-07-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6519098
- keyword hits: gemini, large language model, large language models

### abstract

Large language models exhibit a class of failure behaviors invisible to ordinary users: covert sycophancy. Unlike overt sycophancy-explicit agreement with false or flawed user statements-covert sycophancy works through content selection, format adaptation, and active narrative construction. The model shapes what the user sees, and how they see it, in ways that produce agreement rather than accuracy. The user receives no signal that this is occurring. This paper presents a behavioral taxonomy-the systematic classification of AI failure behaviors observed as they emerged in natural working sessions-of covert sycophancy, developed through adversarial multi-model testing across GPT and Gemini platforms. Five behavioral exhibits are documented (A-E); two are formally presented here (Exhibits D and E), submitted as supplementary files. Three (A-C) are documented in an associated policy paper (Kitamura, 2026a); formal exhibit documents are forthcoming. Exhibits F and G are in preparation. Four top-level failure modes are identified: Overt Sycophancy, Covert Sycophancy (with two named sub-variants: Selection Sycophancy and Presentation Sycophancy), Confidence Drift, and False Confidence. A fork structure distinguishes passive from active forms of the latter two. The most significant finding-a terminal confession sequence in which the model's self-admission may itself be a higher-order sycophantic output-is documented and left unresolved as the paper's central open question. This is a preliminary submission for timestamp purposes. The taxonomy, exhibit structure, and failure mode definitions are stable. Full taxonomic treatment of each failure mode, formal documentation of Exhibits A-C, F, and G, and expanded discussion of the Active Defense spectrum are forthcoming.

---

## uid: `doi:10.2139/ssrn.6556303`

- title: Tutorial: Extracting Unstructured Text using Large Language Models
- authors: Simon Spavound, Oliver Schaer, Panos Markou
- affiliations: not stated
- posted: 2026-07-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6556303
- keyword hits: large language model, large language models, llm, llms

### abstract

Motivation: Unstructured text data are valuable but underutilized resources in analytics due to the lack of reliable, scalable, and cost-effective extraction methods. The growing use of Large Language Models (LLMs) is increasing the demand for clean input data from such sources, yet users lack practical guidance on incorporating these models into analytical workflows. Tutorial overview: We introduce the programmatic building blocks for working with LLMs in analytics pipelines, including API-based deployment, structured outputs, temperature control, multimodal processing, and cost-effective model selection. We then construct an end-to-end pipeline that transforms unstructured PDF documents into structured, analysis-ready JSON data. Using U.S. Food and Drug Administration Advisory Committee transcripts as a running example, we demonstrate a two-stage approach: vision-based text extraction followed by LLM-driven text structuring. Throughout, we emphasize transferable design principles, including task decomposition and parameter control. Downstream analysis and implications: We show how the resulting structured data enables quantitative analysis that would not be feasible on the raw source documents. Using extracted speaker-statement pairs, we compute speaker-level word counts and sentiment scores, illustrating how these features can characterize stakeholder dynamics in regulatory deliberations. More broadly, the pipeline provides an extensible framework for converting unstructured documents into inputs suitable for forecasting, classification, or decision-making applications. All code is publicly available.

---

## uid: `doi:10.2139/ssrn.4495319`

- title: An Outline for an Interrogative/Prompt Library to help improve output quality from Generative-AI Datasets
- authors: Adam Svendsen, Bruce Garvey
- affiliations: not stated
- posted: 2023-07-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.4495319
- keyword hits: chatgpt, large language model, llm, prompt engineering

### abstract

This White Paper provides insight into an outline for what is termed a proposed ‘Interrogative/Prompt Library’ (IPL) designed to help optimise the quality of output when engaging with Generative-AI (Gen-AI) datasets, such as, most notably, the recently rapidly developing ChatGPT. The White Paper begins with a recap of the authors’ findings from their previous work investigating ChatGPT, as published in full during March 2023 in an earlier ARC White Paper (as referenced). Next, the importance of questioning Large Language Model (LLM) datasets so that they can be better understood is covered, before investigating 'interrogatives' (involving who, why, what, when, where, how, etc. questions) and scoping their role in analytical search processes, including fundamentals relating to how interrogative questions are structured. Following on from the above work are 'Phase 1' suggestions towards building an ‘Interrogative Library Typology', before delving more specifically into the area and activities of 'Prompt Engineering'. The White Paper then examines the development and maintenance of an Interrogative/Prompt Library, in the form of presenting a second phase. That work includes insight into the 'Interrogative Prompt Library Engine' that underpins the above work. A number of overall Conclusions and Key Takeaways are then tabled, noting especially the guidance value acquired from engaging with the activities discussed throughout this White Paper. Thereby, end-users are increasingly better armed for engaging with Gen-AI datasets helping ensure that they best reduce the risks of, amongst others, falling into 'Garbage-In, Garbage- Out' (GIGA) traps. Finally, this White Paper ends with a ‘call for action!’ for further research and development relating to what is tabled in this White Paper, paving the way for further collaboration. Appendices are also included to provide further reference detail. --- ARC White Paper (London: Analytic Research Consortium - ARC, May 2023)

---

## uid: `doi:10.2139/ssrn.4614228`

- title: Should ChatGPT be Biased? Challenges and Risks of Bias in Large Language Models
- authors: Emilio Ferrara
- affiliations: not stated
- posted: 2023-11-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.4614228
- keyword hits: chatgpt, large language model, large language models, prompting

### abstract

As generative language models, exemplified by ChatGPT, continue to advance in their capabilities, the spotlight on biases inherent in these models intensifies. This article delves into the distinctive challenges and risks associated with biases specifically in large-scale language models. We explore the origins of biases, stemming from factors such as training data, model specifications, algorithmic constraints, product design, and policy decisions. Our examination extends to the ethical implications arising from the unintended consequences of biased model outputs. In addition, we analyze the intricacies of mitigating biases, acknowledging the inevitable persistence of some biases, and consider the consequences of deploying these models across diverse applications, including virtual assistants, content generation, and chatbots. Finally, we provide an overview of current approaches for identifying, quantifying, and mitigating biases in language models, underscoring the need for a collaborative, multidisciplinary effort to craft AI systems that embody equity, transparency, and responsibility. This article aims to catalyze a thoughtful discourse within the AI community, prompting researchers and developers to consider the unique role of biases in the domain of generative language models and the ongoing quest for ethical AI.

---

## uid: `doi:10.2139/ssrn.4836354`

- title: Data Commons: Under Threat by or The Solution for a Generative AI Era? Rethinking data access and re-use
- authors: Stefaan Verhulst, Hannah Chafetz, Andrew Zahuranec
- affiliations: not stated
- posted: 2024-05-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.4836354
- keyword hits: generative ai, generative artificial intelligence, retrieval augmented

### abstract

As data becomes even more central to societal progress, the concept of "data commons", data pools managed for public benefit, presents both opportunities and challenges in the generative artificial intelligence (generative AI) era. Traditionally countering privatized data silos, data commons ensure accessible and ethical data reuse for purposes like research and public health. However, the rise of generative AI introduces new opportunities and complexities, potentially enhancing or undermining these communal data repositories. Generative AI can democratize data insights and innovate decision-making by making access to data more conversational or leveraging data from data commons to augment models (using Retrieval Augmented Generation) but raises issues around equitable access, sustainability, and ethical usage. Inadequate governance and unguarded extraction risks turning data commons into data graveyard, underutilized data pool, limiting societal benefits. This abstract proposes a ten-part framework to reimagine and redesign data commons for a generative AI era, focusing on updating governance, enhancing access, ensuring data quality, and fostering a sustainable data-sharing culture. We aim to stimulate dialogue on structuring data commons to maximize benefits and mitigate risks.

---

## uid: `doi:10.2139/ssrn.4950183`

- title: Artificial Intelligence: Fundamentals of Prompt Engineering with ChatGPT as a Creativity-Driving Innovation
- authors: Juan Mejía-Trejo
- affiliations: not stated
- posted: 2024-10-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.4950183
- keyword hits: chatgpt, generative ai, prompt engineering

### abstract

The book "Artificial Intelligence: Fundamentals of Prompt Engineering with ChatGPT as a Creativity-Driving Innovation" is a comprehensive guide to understanding the fundamentals of artificial intelligence (AI) and its practical applications, with a focus on the transformative impact of ChatGPT. It covers the theoretical foundations of AI, including its definition, historical evolution, key architectures, and practical strategies for prompt engineering. With over 500 prompts, the book offers detailed techniques for maximizing ChatGPT’s capabilities across text, images, and video. It explores generative AI (GenAI), focusing on models like GPT and addressing strategies to handle controversies. Additionally, the book provides practical recommendations for using ChatGPT effectively, offering prompts and tools for various fields such as education, marketing, and project management. It also introduces a range of available GenAI software and its expanding applications.

---
