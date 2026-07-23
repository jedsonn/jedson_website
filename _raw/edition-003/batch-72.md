# Classification batch 72 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-72.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7120281`

- title: Vertical Scaling of Subdomain-Specific Small Language Models: A Framework for High-Stakes Domains - A Systematic Review of Methodologies, Applications, and Future Directions in Finance, Law, Medicine, and Government
- authors: Ismet Beljulji
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7120281
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

The rapid advancement of large language models (LLMs) has transformed natural language processing across industries, yet their high computational cost, latency, and lack of domain-specific precision limit their deployment in high-stakes environments. This has catalyzed interest in Small Language Models (SLMs) adapted to narrow, specialized subdomains through parameter-efficient fine-tuning (PEFT). This review paper systematically examines the emerging paradigm of subdomainspecific SLMs, focusing on their application in four high-stakes domains: financial compliance, legal reasoning, medical diagnosis, and governmental policy analysis. We argue that domain purity-the use of highly curated, narrow datasets-outweighs dataset scale in determining SLM performance for specialized tasks. Synthetic data generation is explored as a scalable and cost-effective force multiplier for subdomain adaptation. We synthesize existing literature, identify key challenges such as overfitting, structural instability, and deployment constraints, and propose a unified framework for vertical scaling across subdomains. Finally, we outline a roadmap for future research and call for open-source, community-driven development to democratize access to subdomain-specific AI systems.

---

## uid: `doi:10.2139/ssrn.7162222`

- title: Enhancing Southeast Asian Grammatical Error Correction with New Benchmarks and Optimized Layer-wise Fine-tuning
- authors: zihao yu, Ying Li, Zhengtao Yu, Wenjun Wang, Shengxiang Gao, Cunli Mao, Yuxin Huang, Hua Lai
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7162222
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Large Language Models (LLMs) have achieved remarkable success in high-resource grammatical error correction (GEC). However, they still face significant challenges in Southeast Asian low-resource languages due to the scarcity of high-quality parallel corpora and the complexity of distinct grammatical structures. In this work, we propose a unified LLM framework for Southeast Asian multi-lingual GEC tasks efficiently by lexical-guided data augmentation and an optimized layer-wise fine-tuning approach. Specifically, we formulate linguistically-informed confusion sets to guide LLMs in generating synthetic corpora and ensure their quality by further leveraging dual constraints of affinity and diversity. Meanwhile, we propose an optimized layer-wise fine-tuning approach that accurately detects and activates language-specific neural layers to adapt a single LLM for multiple Southeast Asian GEC tasks, where a composite score of $L_2$ norm and cosine similarity is used to quantify language-specific layer importance. Experimental results on four benchmark datasets demonstrate that our optimized layer-wise fine-tuning approach can significantly improve the generalization capabilities of LLMs in Southeast Asian low-resource GEC tasks. Detailed experimental analyses demonstrate that our proposed benchmark dataset introduces a significant variety of authentic errors, improving the model's ability to understand the syntactic structures of Southeast Asian low-resource languages. In-depth visualization results demonstrate that our approach effectively identifies and prioritizes layers critical for linguistic processing, providing evidence for future fine-grained optimization of Southeast Asian GEC tasks.

---

## uid: `doi:10.2139/ssrn.7157742`

- title: LightWDN-Agent: A Quality-Gated Multi-Agent Framework for Privacy-Aware Automation of Water Distribution Network Simulations
- authors: Chong Wang, Hexiang Yan, Wenchong Tian, Kunlun XIN, Jiaying Wang, Tao Tao, Shuping Li
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7157742
- keyword hits: large language model, large language models, llm, retrieval-augmented

### abstract

Large language model (LLM)-based agents offer a promising paradigm for automating engineering workflows in water distribution network (WDN) simulations. However, existing frameworks generally assume that user instructions are directly executable, rely heavily on cloud-based inference, and often lack robust domain-specific semantic grounding, limiting their reliability and practical deployment. This study presents LightWDN-Agent, a lightweight multi-agent framework for natural language-driven WDN simulation that integrates quality-aware task validation, retrieval-augmented semantic grounding, and local–cloud collaborative inference. The framework first evaluates the executability of user queries and requests clarification for ambiguous or incomplete instructions before task execution. It then incorporates domain knowledge, tool descriptions, and historical successful cases through retrieval-augmented generation to constrain task planning and improve semantic consistency. Finally, routine reasoning is performed using lightweight local models, while cloud-based large language models are invoked only for complex reasoning and runtime error correction, enabling privacy-aware and resource-efficient deployment. The framework was evaluated using a benchmark comprising 39 representative WDN simulation tasks and 117 natural language queries with different quality levels. The proposed quality-gating strategy effectively prevented ambiguity propagation, improving execution reliability while reducing redundant reasoning. Threshold calibration identified an appropriate operating range that balances task acceptance and execution success. Approximately 69.3% of inference tokens were processed locally, with 38.5% of tasks completed entirely without external API calls. In addition, removing retrieval-augmented semantic grounding reduced the task completion rate from 100% to 46.15% and substantially increased token consumption. The results demonstrate that reliable natural language-driven WDN automation requires not only strong language models but also executability regulation, structured semantic grounding, and deployment-aware inference allocation, providing a practical framework for intelligent and privacy-preserving water system management.

---

## uid: `doi:10.2139/ssrn.7127378`

- title: Generative and Agentic AI Through the Lens of Model Risk Management: A Multisector Framework for Identifying Opportunities and Circumventing Risks
- authors: Advaith Nila Narayanan
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7127378
- keyword hits: agentic, generative artificial intelligence, llm, llms

### abstract

The rapid ascent of Generative Artificial Intelligence (GenAI) and its more autonomous successor, agentic AI, represents a watershed moment for organizations in virtually every sector, including healthcare, insurance, law, energy, and finance. For risk management professionals, these technologies are simultaneously the ultimate tool and the ultimate threat. We argue that while the non-deterministic nature and autonomy of these models introduce novel failure modes—such as hallucination, prompt injection, and execution drift, the core principles of model risk management (MRM), namely, Meaningful Challenge, Conceptual Soundness, and Ongoing Monitoring, remain the most robust defense. Although MRM matured as a formal discipline within quantitatively intensive industries, its principles are fundamentally sector-agnostic: any organization that uses a model to inform consequential decisions faces model risk and benefits from a disciplined framework for controlling it. This study provides a detailed account of what traditional MRM is, why it is needed, and how its components can be adapted, and offers a strategic roadmap for risk professionals in any industry to extend existing governance structures to the unique risks of LLMs and autonomous agents. We also discuss the critical question: What opportunities and risks do new technologies pose for risk professionals? using MRM principles as a foundational framework, appropriately adapted to the unique challenges posed by GenAI. We explore how the principles of meaningful challenge, conceptual soundness, and rigorous governance apply to non-deterministic, billion-parameter models, and we develop sector-specific analyses of GenAI model risk in healthcare, insurance, and legal services, together with an examination of numerical, computational, and energy-related risks unique to large-scale AI systems.

---

## uid: `doi:10.2139/ssrn.7153775`

- title: A DXF-Native Pipeline for Automated Cross-Standard Annotation Conversion in Mechanical Engineering Drawings
- authors: Chaoyang Zhang, Shu Wu
- affiliations: not stated
- posted: 2026-07-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7153775
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

When a mechanical drawing crosses jurisdictions, annotations written under one national standard (GB, ISO, ANSI, JIS) must be manually reworked for another. Rule-based translators handle predictable patterns but break on anything non-standard. Large language models (LLMs) offer flexibility, yet hallucinate at rates above 80%, fabricating numbers and symbols in ways that are hard to catch. Retrieval-augmented generation (RAG) retrieves relevant examples but indexes documents coarsely, without access to the internal structure of annotation entities. This paper presents a pipeline that stays entirely within the DXF entity layer: no rasterisation, no intermediate format conversion, no loss of layer or block metadata. Five design choices set it apart. (1) A DXF-native extraction–regeneration framework that preserves layer hierarchy, linetype definitions, and block attributes. (2) An Entity Masking module that replaces dimensional values and standard symbols with typed placeholders before LLM exposure and restores them afterwards, keeping critical numeric parameters out of the model's reach. (3) A Trident Router that dispatches each annotation to one of three pathways: rule (33.6%), RAG (21.8%), or LLM (44.6%). (4) A Dual-Loop Verification module coupling standard-compliance checking with spatial collision detection, cutting the hallucination rate from 0.829 to 0.050. (5) Validation on 11 factory drawings (1,563 annotations) against three baselines and six ablations. The full pipeline reaches a Term Accuracy of 0.844, a 1.33× to 5.37× margin over baselines, with perfect Entity Preservation (1.000) and zero spatial collisions.

---

## uid: `doi:10.2139/ssrn.7163179`

- title: DSDA-GasGPT: An Aero-engine Gas Path Fault Diagnosis Method Based on Two-Stage Decoupling for Mitigating LLMs Hallucinations
- authors: Yongzhan Chen, xiaofei wang, haomin DAI, Chengyue Li, yanli Gao, Zhaogeng Zhong, jianling Qu
- affiliations: not stated
- posted: 2026-07-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7163179
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Intelligent fault diagnosis of the gas path system of an aircraft engine is of vital importance for ensuring flight safety and operational reliability. Recently, large language models (LLMs) have provided a novel solution for fault diagnosis of the air path of an aero-engine due to their powerful semantic understanding and context reasoning capabilities. However, when small-parameter LLMs are used for fault diagnosis, due to insufficient representation capacity, they are prone to the problem of cascading hallucination, generating highly deceptive pseudo-expert fault analyses. To address the problem, we proposed the Dual-Stage decoupled Diagnosis-Analysis (DSDA) framework, and an intelligent fault diagnosis model tailored for aero-engine gas path systems GasGPT. DSDA-GasGPT initially employs a semantic encoding module to transform sensor data into structured text, effectively capitalizing on the semantic extraction and reasoning of LLMs. Building on this, we utilize LoRA for supervised fine-tuning of the LLMs to enhance their adaptability to the aero-engine fault diagnosis domain. Subsequently, DSDA-GasGPT performs context-aware reasoning analysis to output fault diagnosis results and causal analyses. In gas path fault diagnosis experiments, DSDA-GasGPT achieved an accuracy of 95.43% and a Correct Diagnosis and Analysis (CDA) rate of 95.25%, representing an improvement of approximately 12% to 20% compared to baseline algorithms. Furthermore, the incidence of cascading hallucinations was reduced to 4.57%, outperforming existing state-of-the-art (SOTA) algorithms. The model's superior generalization capability and engineering applicability were further validated through ablation studies, integration experiments, and tests on imbalanced datasets.

---

## uid: `doi:10.2139/ssrn.4351817`

- title: 'Let’s Have a Chat': Principles for the Effective Application of ChatGPT and Large Language Models in the Practice of Forensic Accounting
- authors: Daniel Street, Joseph Wilck
- affiliations: not stated
- posted: 2023-02-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.4351817
- keyword hits: chatgpt, large language model, large language models

### abstract

NOT AVAILABLE. You have title and authors only. Set bullet_provenance to "none", return an empty bullets array, and classify field and role only if the title makes it unambiguous.

---

## uid: `doi:10.2139/ssrn.4412788`

- title: Can ChatGPT Forecast Stock Price Movements? Return Predictability and Large Language Models
- authors: Alejandro Lopez-Lira, Yuehua Tang
- affiliations: not stated
- posted: 2023-04-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.4412788
- keyword hits: chatgpt, large language model, large language models

### abstract

NOT AVAILABLE. You have title and authors only. Set bullet_provenance to "none", return an empty bullets array, and classify field and role only if the title makes it unambiguous.

---
