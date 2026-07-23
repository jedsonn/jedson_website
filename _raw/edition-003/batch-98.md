# Classification batch 98 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-98.answer.json` as a JSON array.

---

## uid: `arxiv:2606.12848v1`

- title: (Human) Attention Is (Still) All You Need: Human oversight makes AI-assisted social science reliable
- authors: Chen Zhu, Xiaolu Wang, Weilong Zhang
- affiliations: not stated
- posted: 2026-06-11
- source: arXiv
- link: https://arxiv.org/abs/2606.12848v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are increasingly used for tasks once reserved for trained researchers, including hypothesis generation, specification choice, and drafting conclusions. We argue that the reliability of AI-assisted research depends not only on model capability, but also on how cognitive labour is structured between humans and machines. We study this problem through Human-in-the-Loop Economic Research (HLER), a decision architecture based on pre-commitment, decision sequencing, accountability, and attention allocation. In a pre-specified 2*4 factorial experiment with 280 complete research runs across four datasets, an unconstrained multi-agent baseline produced critical failures in 72% of runs. Using the same underlying model, the same agent decomposition, and identical prompts for the shared reasoning agents, HLER reduced the failure rate to 16% by imposing three architectural commitments: LLMs reason but do not execute data work, data and estimation are handled deterministically, and three human decision gates bind the workflow. Fisher's exact test rejects equality of failure rates at p<0.001. Reliability gains were largest on the least publicly represented dataset, a Qing-dynasty population register, consistent with a task-based production model with Frechet-distributed output quality. An 80-run ablation suggests that deterministic computation and human gates contribute independently, with exploratory evidence of complementarity. We interpret HLER as a research harness rather than an autonomous AI scientist: it sharply reduces failures, makes residual weaknesses more visible, and prevents unreliable claims from being advanced as publication-ready outputs.

---

## uid: `doi:10.2139/ssrn.6927019`

- title: A Repository-Level Merge Conflict Resolution Method Based on Large Language Models
- authors: Weifeng Zhang, Zhenyu Dong, Han Zhao, Yunshi Gu, Lei Xu
- affiliations: not stated
- posted: 2026-06-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6927019
- keyword hits: large language model, large language models, llm, prompting, retrieval-augmented

### abstract

CONTEXT: Merge conflicts remain a costly obstacle in collaborative software development, and their correct resolution often depends on repository-specific conventions that are not visible from the conflicting code block alone. OBJECTIVES:This study investigates whether historical conflict-resolution records from the same repository can improve LLM-based merge conflict resolution under a leakage-free chronological evaluation setting. METHODS:We propose a repository-level retrieval-augmented generation framework that retrieves relevant historical conflict-resolution pairs using BM25-based sparse retrieval, CodeT5-based dense retrieval with L2 distance, and reciprocal rank fusion. Retrieved examples are incorporated into structured prompts, together with quality filtering, similarity gating, and output-parsing safeguards. We evaluate the approach on 11 repositories across multiple programming languages and compare it with no-context LLM prompting, cross-/intra-repository LLM baselines, and MergeBERT. RESULTS: Retrieved repository history consistently improves exact-match accuracy over no-context prompting with the same base LLM. The overall score is higher than MergeBERT under the same chronological split, although performance varies by repository, conflict type, and available historical-data volume. CONCLUSION:Repository-specific historical retrieval provides useful in-context guidance for LLM-based conflict resolution, but exact-match evaluation is conservative, LLM latency remains non-negligible, and developer validation is still required before fully automated deployment.

---

## uid: `doi:10.2139/ssrn.6928677`

- title: Automated Generation of Complexity-Validated Decision Scenarios Using Large Language Models
- authors: Ratna  Babu Chinnam, Toni Somers, Abdalla Doleh
- affiliations: not stated
- posted: 2026-06-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6928677
- keyword hits: large language model, large language models, llm, llms

### abstract

Problem: Cognitive decision-making research requires diverse, complexity-controlled scenarios, but manual generation is slow, inconsistent, and biased.Solution: We present an automated pipeline that generates structured decision scenarios with large language models (LLMs) and validates their complexity using a composite framework derived from Wood (1986), Campbell (1988), Liu and Li (2012), and Sweller (1994).Results: We evaluated 4,238 scenarios across domains and complexity tiers. Measurement validation exceeded psychometric standards: inter-LLM agreement was near-perfect (ICC = 0.997; κ = 0.971), test-retest reliability was excellent (ICC = 0.995, p = 0.178 for drift), and known-groups validity showed large tier separation (η² = 0.587, all pairwise p

---

## uid: `doi:10.2139/ssrn.6929036`

- title: AHierarchical Error-Corrective Graph Framework for AutonomousAgents with LLM-Based Action Generation
- authors: CONG CAO
- affiliations: not stated
- posted: 2026-06-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6929036
- keyword hits: large language model, large language models, llm, llms

### abstract

While the integration of Reinforcement Learning (RL) and Large Language Models (LLMs) hasenabled agents to generate high-level action plans for complex embodied tasks, robust executionremains an open challenge. Existing approaches struggle with three critical limitations: Firstly,traditional methods typically rely on single-dimensional metrics or simple weighted scoring mechanisms, which makes it difficult to comprehensively characterize the transferability of strategiesin different tasks. This limitation is particularly pronounced in dynamic or partially observableenvironments. Secondly, current agent feedback mechanisms often focus solely on overall task successor failure, without providing structured attribution for the causes of failure. Finally, existing RetrievalAugmented Generation (RAG) methods have achieved some success in mitigating LLM hallucinations, but their retrieval processes primarily depend on vector similarity or token-based matching,capturing only superficial semantic proximity and failing to fully leverage the structured relationshipsamong historical experiences, actions, and events. This limitation restricts retrieval quality, semanticalignment, and contextual consistency. To address these issues, we propose a Hierarchical ErrorCorrective Graph Framework (HECG) for Autonomous Agents with LLM-Based Action Generation,which incorporates three core innovations: (1) Multi-Dimensional Transferable Strategy (MDTS):By integrating task quality, execution cost, risk, and LLM-based semantic reasoning scores, MDTSachieves multi-dimensional alignment for the precise selection of high-quality candidate strategies,effectively reducing negative transfer risk. (2) Error Matrix Classification (EMC): Unlike simpleconfusion matrices, EMC provides structured attribution by categorizing errors into ten types basedon severity and recoverability, offering clear and actionable guidance for subsequent error correctionand replanning.(3) Causal-Context Graph Retrieval (CCGR): CCGR construct graphs from historicalstates, actions, and event sequences to identify subgraphs most relevant to the current context. Thiscaptures deep structural dependencies beyond flat vector similarity, allowing agents to acceleratestrategy adaptation and improve execution reliability. Extensive experiments in simulated embodiedenvironments (e.g., VirtualHome) demonstrate that HECG significantly outperforms state-of-the-artLLM planners, achieving substantial improvements in task success rates, execution efficiency, anderror recovery. Ultimately, our framework bridges the gap between high-level semantic reasoning androbust low-level execution in complex, multi-step tasks. The implementation and experimental codeare publicly available at:https://gitlab.com/magicmaster356a/cozy-hierplan

---

## uid: `doi:10.2139/ssrn.6838425`

- title: DSA Risk Assessment -Social Media Mental Harm Automatic Annotation Case Study
- authors: Tadeusz Zbiegień, Tejas Goyal, Jaromir Savelka, Ewa Ilczuk, Małgorzata Kuśmierczyk, Krystyna Mokrzycka, Przemysław Pałka
- affiliations: not stated
- posted: 2026-06-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6838425
- keyword hits: claude, llm, llms

### abstract

The EU's Digital Services Act (DSA) requires Very Large Online Platforms (VLOPs) to identify and mitigate systemic risks to users' mental well-being through annual risk assessments. However, analyzing these lengthy, heterogeneous reports is labor-intensive for regulators and researchers. This study evaluates the capability of four LLMs (GPT 5.2, GPT5mini, Claude Sonnet 4.5, and Claude Opus 4.5) to automatically annotate mental-healthrelated content in DSA risk reports. Using a human-annotated benchmark of 14 VLOP risk assessments from 2023-2024, we developed a hierarchical annotation schema distinguishing between risk types (internal/external) and mitigation measures (platform-level/external). Our asynchronous, zero-shot annotation pipeline reduced processing time from approximately four hours of human labor per document to under two minutes. Results show Claude Opus achieved the highest sentence-level coverage (56-65%), though all models exhibited systematic biases, such as over-triggering on general risk categories, while under-detecting specific mitigation measures. Although not yet suitable for fully automated compliance assessment, the proposed pipeline establishes a potential foundation for future research on computational oversight and empirical analysis of platform governance under the DSA framework.

---

## uid: `doi:10.2139/ssrn.6926957`

- title: The Physical Feedback Loop in LLM-Assisted Embedded Development: A Dual Case Study of Human Roles and Bug Patterns
- authors: Mingbo Zhang, Weibin Jiang, Ziping Zhang
- affiliations: not stated
- posted: 2026-06-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6926957
- keyword hits: large language model, large language models, llm, llms

### abstract

Context: Large Language Models (LLMs) are widely used for code generation, yet existing empirical studies focus on pure software scenarios. Embedded systems development introduces physical hardware as a verification step that cannot be fully simulated in digital environments, potentially fundamentally altering human-AI collaboration patterns.,Objective: This study aims to identify the roles that require ongoing human involvement in LLM-assisted embedded development and the collaborative structure these roles constitute, and to document observed bug patterns in AI-generated embedded code.,Method: We conducted a dual case study using thematic analysis on complete dialogue logs from an ESP32 smart car (90 rounds of conversation, 70 effective rounds) and an ESP32-CAM camera (47 rounds of interaction, 42 effective rounds). A dual-coding scheme (permitting multiple behavior codes per round) was adopted, with two researchers independently coding human behavior and bug types (per-code Kappa range: main case 0.41–0.80, validation case 0.31–1.00; individual codes with sparse events showed lower values).,Results: We identified three human roles forming a Physical Feedback Loop (PFL): Physical Observer (~49% of effective rounds), Bug Finder (60.6% of bug instances required human physical observation; 30.3% involved potentially automatable runtime errors), and Requirement Executor (~31% of rounds). Across both cases, eight bug types (T1-T8) were documented; approximately 70% (23/33) of instances required hardware verification. Observer and Finder roles co-occurred within 3 consecutive rounds in 86.5% of cases, indicating frequent co-occurrence (a permutation test showed no statistically significant sequential ordering, p=0.37). Cascading bugs introduced by AI repair operations were observed only in the networked integrated system.,Conclusions: In LLM-assisted embedded development, humans must complete the full "observation-diagnosis → decision" physical loop. Within the scope of this study, AI accelerated code generation but did not replace human involvement in hardware verification and system impact assessment.

---

## uid: `doi:10.2139/ssrn.6932539`

- title: Overcoming High Volume and Complexity: Developing a Large Language Model-Assisted Scoping Review Method for Identifying Long-term Caesarean Section Outcomes
- authors: Edwina Mead, Darren Rajit, Vanessa Scarf, Emily Callander
- affiliations: not stated
- posted: 2026-06-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6932539
- keyword hits: gemini, large language model, llm

### abstract

Background and objective: The unprecedented growth in medical literature limits the feasibility of traditional systematic review methods, particularly in high-volume clinical fields like maternity care. To address this meta-scientific challenge, this paper presents a novel methodological approach using a hybrid workflow that combines Large Language Model (LLM) semantic data extraction with programmatic filtering to automate title and abstract screening. Methods: To provide a critical evaluation of this LLM-assisted approach, the hybrid workflow was deployed on a high-volume clinical dataset (51,281 records retrieved from six databases) as a validation case study. Google Gemini 1.5-pro and 2.5-flash were used to extract 12 structured semantic variables from abstracts, followed by a seven-stage rule-based filtering pipeline to determine eligibility. To ensure transparent reporting, the workflow’s diagnostic accuracy was validated against a large-scale manual audit to calculate sensitivity, specificity, and error rates. Results: The hybrid workflow reduced the human manual screening burden by 96% while maintaining accuracy comparable to dual-human review. Validation against a demonstrated an estimated sensitivity of 89.9% (95% confidence interval; CI 87.3-92.1%) and specificity of 96.4% (95% CI 96.2-96.5%), with a false negative rate of 0.18% (95% CI 0.09-0.35%). This automated phase was completed at a total API cost of US$458.73. Subgroup analysis found no change in screening accuracy after changing LLM. Discussion: This approach offers a scalable, transparent, cost-effective, and model-agnostic solution for evidence synthesis in high-volume medical fields. By decoupling data extraction from inclusion logic, this method allows researchers to maintain granular control over complex eligibility criteria, facilitating the development of living reviews as global research output continues to expand.

---

## uid: `doi:10.2139/ssrn.6868459`

- title: A Multi-Dimensional Labeling System for "Fixed Income Plus" Fund Managers: An Integrated Approach Combining Quantitative Metrics, Portfolio Structure, and Large Language Model Analysis
- authors: Dan Yang
- affiliations: not stated
- posted: 2026-06-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6868459
- keyword hits: deepseek, large language model, llm

### abstract

Background: With the rapid expansion of "fixed income plus" (FI+) fund products-including secondary bond funds and convertible bond funds-investors increasingly demand tools for manager style identification and performance attribution. Conventional fund evaluation relies on single quantitative metrics or opaque qualitative ratings, which fail to capture the multi-dimensional nature of FI+ strategies. Objective: This study constructs a six-dimensional labeling system for FI+ fund managers by integrating quantitative metrics, portfolio structure, and large language model (LLM) textual analysis, and systematically compares fund performance across label combinations. Methods: We select 25 representative FI+ funds (15 secondary bond funds + 10 convertible bond funds) from January 2022 to December 2024. Three analytical layers are employed: (1) nine quantitative indicators computed from daily net-asset-value (NAV) data; (2) bond-type classification and credit-downgrade analysis based on portfolio holdings; and (3) structured text analysis of 224 fund periodic reports using DeepSeek Chat large language model via API (temperature = 0.1). A six-dimensional label system is built covering "return-risk profile," "operating style," "drawdown control," "equity style," "interest-rate band," and "credit style." Findings: (1) Low-volatility funds (annualized volatility < 3%) achieved an average return of 2.4%, significantly outperforming high-volatility funds at-2.33% (Kruskal-Wallis test, *p* < 0.05). (2) "Left-side layout" funds exhibited a significantly higher Sharpe ratio (0.38) than "right-side follower" funds (-0.13)(Wilcoxon rank-sum test, W = 15, p = 0.042). (3) Managers with a neutral sentiment expression outperformed those with dominant optimism (annualized 0.58% vs.-1.72%). (4) Credit-downgrade strategies did not generate excess returns during the sample period. Implications: The labeling framework provides an objective, quantifiable toolkit for fund screening, performance attribution, and product design. The methodology is replicable and extensible to other fund categories.

---
