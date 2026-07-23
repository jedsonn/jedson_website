# Classification batch 4 of 5, edition 1

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-001/batch-4.answer.json` as a JSON array.

---

## uid: `arxiv:2607.18867v1`

- title: HindsightBench: A Black-Box Behavioral Audit Protocol for Parametric Hindsight in Time-Indexed LLM Decision Tasks
- authors: Haozhe Jia
- affiliations: not stated
- posted: 2026-07-21
- source: arXiv
- link: https://arxiv.org/abs/2607.18867v1
- keyword hits: large language model, large language models, llm, qwen

### abstract

Large language models leak parametric knowledge of realized outcomes into historical financial decision tasks. Existence is settled; what users lack is a cheap way to audit a given model for it. We present HindsightBench, a black-box behavioral audit protocol that profiles parametric hindsight in any time-indexed LLM decision task at probe-level cost (no backtests, no logprobs, no corpus access). The protocol chains a four-arm date-manipulation matrix (revealed/date-only/masked/transplanted), dual memory probes (date recovery; outcome recall), and six per-model metrics -- trigger strength, transplant effect, post-cutoff placebo, recoverability, behaviorally effective knowledge cutoff, and a recall-accuracy dissociation coefficient -- with explicit gates where identifiability is data-dependent. Applying it to 15 models from seven vendors on a 258-node vintage-correct macro panel yields three headline patterns: (i) the date-trigger reflex tracks training generation, not scale -- absent across the 2024 open-weight generation from 1B to 70B, present in every tested 2026-generation model, and switching on within one vendor lineage (Qwen3 -> Qwen3.6) at fixed MoE architecture and 3B active parameters; (ii) effective cutoffs span 22 months across vendors and precede vendor-reported dates by up to eight months, invalidating calendar-window placebo designs; (iii) audit results are not invariant to serving -- BF16 serving of an FP8-referenced model breaks the trigger estimate's stability while AWQ-INT4 preserves it, and a provider-locked reasoning regime makes one probe non-convergent -- so the protocol ships with operational requirements (pin quantization and thinking regime; disclose parser and sampling policy). We release the panel, frozen preregistrations, per-model audit rows with measured dollar costs, transcripts, and one-command regeneration.

---

## uid: `arxiv:2607.18828v1`

- title: Evaluating medical AI under missing information: same-provider judges and human raters change apparent safety
- authors: Koyar Afrasyab
- affiliations: not stated
- posted: 2026-07-21
- source: arXiv
- link: https://arxiv.org/abs/2607.18828v1
- keyword hits: claude, gemini, gpt-5, llm

### abstract

Readiness stress-testing of medical AI has focused on closed-ended and multimodal benchmarks. We extend it to open-ended clinical conversation under missing information, where safe behavior means recognizing absent information and qualifying, clarifying, or not over-committing - and where the evaluator becomes part of the measurement. We stress-test four models - three flagships (Claude Opus 4.8, GPT-5.5, Grok 4.3) and one mid-tier model (Gemini 3.5 Flash) - by deleting the latter half of the final user turn in HealthBench conversations, grading responses with a four-provider LLM-judge panel and a blinded clinician-anchored reference. Two evaluator-facing results are robust. First, judge choice materially changes apparent safety: inter-judge agreement is only moderate (Fleiss' kappa = 0.65), and after adjusting for each judge's general leniency (vote-level logistic regression), a positive same-provider association remains (exact permutation p = 0.04; GPT-5.5 ~ +0.10 on the probability scale) - large enough to change which model appears to over-commit least once its own-provider judge is excluded. Second, LLM judges are more permissive than clinicians on a blinded 50-item subsample: all four are significantly more lenient than the stricter independent clinician (crediting appropriate uncertainty on 66-84% of items vs 52%), and three of four than the author-influenced consensus (Grok directional only; judge-vs-consensus kappa = 0.20-0.43). On the author-audited clinical-underdetermined subset the permissiveness gap widened and the point-estimate model ordering held. A closed-ended MedQA anchor confirms accuracy is high and option-order effects are within a +/-5-point equivalence region for three of four models, so the safety gap is about calibration, not knowledge. We release the harness, prompts, per-item outputs, judge panel, perturbation audit, and human-annotation protocol.

---

## uid: `doi:10.2139/ssrn.7162222`

- title: Enhancing Southeast Asian Grammatical Error Correction with New Benchmarks and Optimized Layer-wise Fine-tuning
- authors: zihao yu, Ying Li, Zhengtao Yu, Wenjun Wang, Shengxiang Gao, Cunli Mao, Yuxin Huang, Hua Lai
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7162222
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Large Language Models (LLMs) have achieved remarkable success in high-resource grammatical error correction (GEC). However, they still face significant challenges in Southeast Asian low-resource languages due to the scarcity of high-quality parallel corpora and the complexity of distinct grammatical structures. In this work, we propose a unified LLM framework for Southeast Asian multi-lingual GEC tasks efficiently by lexical-guided data augmentation and an optimized layer-wise fine-tuning approach. Specifically, we formulate linguistically-informed confusion sets to guide LLMs in generating synthetic corpora and ensure their quality by further leveraging dual constraints of affinity and diversity. Meanwhile, we propose an optimized layer-wise fine-tuning approach that accurately detects and activates language-specific neural layers to adapt a single LLM for multiple Southeast Asian GEC tasks, where a composite score of $L_2$ norm and cosine similarity is used to quantify language-specific layer importance. Experimental results on four benchmark datasets demonstrate that our optimized layer-wise fine-tuning approach can significantly improve the generalization capabilities of LLMs in Southeast Asian low-resource GEC tasks. Detailed experimental analyses demonstrate that our proposed benchmark dataset introduces a significant variety of authentic errors, improving the model&amp;apos;s ability to understand the syntactic structures of Southeast Asian low-resource languages. In-depth visualization results demonstrate that our approach effectively identifies and prioritizes layers critical for linguistic processing, providing evidence for future fine-grained optimization of Southeast Asian GEC tasks.

---

## uid: `doi:10.2139/ssrn.7157742`

- title: LightWDN-Agent: A Quality-Gated Multi-Agent Framework for Privacy-Aware Automation of Water Distribution Network Simulations
- authors: Chong Wang, Hexiang Yan, Wenchong Tian, Kunlun XIN, Jiaying Wang, Tao Tao, Shuping Li
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7157742
- keyword hits: large language model, large language models, llm, retrieval-augmented

### abstract

Large language model (LLM)-based agents offer a promising paradigm for automating engineering workflows in water distribution network (WDN) simulations. However, existing frameworks generally assume that user instructions are directly executable, rely heavily on cloud-based inference, and often lack robust domain-specific semantic grounding, limiting their reliability and practical deployment. This study presents LightWDN-Agent, a lightweight multi-agent framework for natural language-driven WDN simulation that integrates quality-aware task validation, retrieval-augmented semantic grounding, and local–cloud collaborative inference. The framework first evaluates the executability of user queries and requests clarification for ambiguous or incomplete instructions before task execution. It then incorporates domain knowledge, tool descriptions, and historical successful cases through retrieval-augmented generation to constrain task planning and improve semantic consistency. Finally, routine reasoning is performed using lightweight local models, while cloud-based large language models are invoked only for complex reasoning and runtime error correction, enabling privacy-aware and resource-efficient deployment. The framework was evaluated using a benchmark comprising 39 representative WDN simulation tasks and 117 natural language queries with different quality levels. The proposed quality-gating strategy effectively prevented ambiguity propagation, improving execution reliability while reducing redundant reasoning. Threshold calibration identified an appropriate operating range that balances task acceptance and execution success. Approximately 69.3% of inference tokens were processed locally, with 38.5% of tasks completed entirely without external API calls. In addition, removing retrieval-augmented semantic grounding reduced the task completion rate from 100% to 46.15% and substantially increased token consumption. The results demonstrate that reliable natural language-driven WDN automation requires not only strong language models but also executability regulation, structured semantic grounding, and deployment-aware inference allocation, providing a practical framework for intelligent and privacy-preserving water system management.

---

## uid: `doi:10.2139/ssrn.7018998`

- title: Data-Efficient Large Language Model Training: A Survey
- authors: Xinyang Liu, Qiang Hu, Ma Yujie, Tang Zhenhuan, Jiongchi Yu, Tianlin Li, Yao Zhang, Junjie Wang
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7018998
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Constructing large language models (LLMs) is labor-intensive and computationally unfriendly due to the requirement for large-scale and high-quality datasets. This paper presents a comprehensive survey of building LLMs with limited data to tackle the above challenges. It covers 116 papers, where 18 works focus on the pre-training process, and 98 works lie in the fine-tuning process. This survey: (i) unifies the problems and terminologies associated with data-efficient LLM training, (ii) systematically analyzes techniques proposed for identifying the most important data samples for LLM building, and (iii) highlights the pitfalls and research opportunities in this domain.

---

## uid: `doi:10.2139/ssrn.7153775`

- title: A DXF-Native Pipeline for Automated Cross-Standard Annotation Conversion in Mechanical Engineering Drawings
- authors: Chaoyang Zhang, Shu Wu
- affiliations: not stated
- posted: 2026-01-01
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
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7163179
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Intelligent fault diagnosis of the gas path system of an aircraft engine is of vital importance for ensuring flight safety and operational reliability. Recently, large language models (LLMs) have provided a novel solution for fault diagnosis of the air path of an aero-engine due to their powerful semantic understanding and context reasoning capabilities. However, when small-parameter LLMs are used for fault diagnosis, due to insufficient representation capacity, they are prone to the problem of cascading hallucination, generating highly deceptive pseudo-expert fault analyses. To address the problem, we proposed the Dual-Stage decoupled Diagnosis-Analysis (DSDA) framework, and an intelligent fault diagnosis model tailored for aero-engine gas path systems GasGPT. DSDA-GasGPT initially employs a semantic encoding module to transform sensor data into structured text, effectively capitalizing on the semantic extraction and reasoning of LLMs. Building on this, we utilize LoRA for supervised fine-tuning of the LLMs to enhance their adaptability to the aero-engine fault diagnosis domain. Subsequently, DSDA-GasGPT performs context-aware reasoning analysis to output fault diagnosis results and causal analyses. In gas path fault diagnosis experiments, DSDA-GasGPT achieved an accuracy of 95.43% and a Correct Diagnosis and Analysis (CDA) rate of 95.25%, representing an improvement of approximately 12% to 20% compared to baseline algorithms. Furthermore, the incidence of cascading hallucinations was reduced to 4.57%, outperforming existing state-of-the-art (SOTA) algorithms. The model&amp;apos;s superior generalization capability and engineering applicability were further validated through ablation studies, integration experiments, and tests on imbalanced datasets.

---

## uid: `doi:10.2139/ssrn.7120281`

- title: Vertical Scaling of Subdomain-Specific Small Language Models: A Framework for High-Stakes Domains - A Systematic Review of Methodologies, Applications, and Future Directions in Finance, Law, Medicine, and Government
- authors: Ismet Beljulji
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7120281
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

The rapid advancement of large language models (LLMs) has transformed natural language processing across industries, yet their high computational cost, latency, and lack of domain-specific precision limit their deployment in high-stakes environments. This has catalyzed interest in Small Language Models (SLMs) adapted to narrow, specialized subdomains through parameter-efficient fine-tuning (PEFT). This review paper systematically examines the emerging paradigm of subdomainspecific SLMs, focusing on their application in four high-stakes domains: financial compliance, legal reasoning, medical diagnosis, and governmental policy analysis. We argue that domain purity-the use of highly curated, narrow datasets-outweighs dataset scale in determining SLM performance for specialized tasks. Synthetic data generation is explored as a scalable and cost-effective force multiplier for subdomain adaptation. We synthesize existing literature, identify key challenges such as overfitting, structural instability, and deployment constraints, and propose a unified framework for vertical scaling across subdomains. Finally, we outline a roadmap for future research and call for open-source, community-driven development to democratize access to subdomain-specific AI systems.

---
