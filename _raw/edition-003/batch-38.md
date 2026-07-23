# Classification batch 38 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-38.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6564458`

- title: Convergence Point Theory An Empirical Study on the Higher-Order Determinants of LLM Token Prediction Entropy and the Effects of RLHF-Induced Artificial Convergence Points (2026.04.30 Paper Revision)
- authors: Ji Hong Park
- affiliations: not stated
- posted: 2026-04-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6564458
- keyword hits: deepseek, llama, llm, mistral, qwen

### abstract

This study begins with the question: what properties of user utterances determine the internal uncertainty of AI language models? Prior research has sought to explain this phenomenon through individual variables such as utterance abstraction, lexical difficulty, and reasoning demand, but no overarching principle unifying these accounts has been proposed. This study introduces the concept of the Convergence Point — defined as the structural density of human knowledge consensus embedded within a user utterance — and argues that this density functions as the higher-order condition governing an AI model's token prediction entropy. Experiments were conducted in parallel using llama_cpp-based token prediction entropy measurement, core/structure-separated entropy analysis, TransformerLens-based Logit Lens analysis, and RLHF bias measurement. A total of five systematic experimental trials were carried out across five models: Mistral-7B-Instruct, Meta-Llama-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-7B, Gemma-2-9B-it, and Qwen3-8B. The results showed that entropy decreased by up to 68% when high-density Convergence Points were provided, and that entropy varied systematically across a four-tier spectrum — Full Consensus, medical consensus, Partial Consensus, and Non-consensus — with this pattern reproduced consistently across all five models. Furthermore, Artificial Convergence Points implanted in Non-consensus domains via RLHF exhibited stronger entropy-suppression effects than high-density Convergence Points provided directly by humans, suggesting that RLHF can function as a source of spurious convergence in domains where genuine consensus does not exist. This study proposes that Convergence Point Theory can integrate under a single overarching principle phenomena previously explained in isolation — including hallucination, prompt effects, and response instability on philosophical questions — and offers structural implications for the design of AI role boundaries and alignment strategies.

---

## uid: `doi:10.2139/ssrn.6585258`

- title: Generative Augmented Inference
- authors: Cheng Lu, Mengxin Wang, Dennis Zhang, Heng Zhang
- affiliations: not stated
- posted: 2026-04-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6585258
- keyword hits: large language model, large language models, llm, llms

### abstract

Data-driven operations management often relies on parameters estimated from costly human-generated labels, such as purchase decisions, expert annotations, or survey responses. Recent advances in large language models (LLMs) and other AI systems offer inexpensive auxiliary data, but introduce a new challenge: AI outputs are not direct observations of the target outcomes, but could involve high-dimensional representations with complex and unknown relationships to human labels. Conventional methods leverage AI predictions as direct proxies for true labels, which can be inefficient or unreliable when this relationship is weak or misspecified. We propose Generative Augmented Inference (GAI), a general framework that incorporates AI-generated outputs as informative features for estimating models of human-labeled outcomes. GAI uses an orthogonal moment construction that enables consistent estimation and valid inference with flexible, nonparametric relationship between LLM-generated outputs and human labels. We establish asymptotic normality and show a "safe default" property: relative to human-data-only estimators, GAI weakly improves estimation efficiency under arbitrary auxiliary signals and yields strict gains whenever the auxiliary information is predictive. Empirically, GAI performs strongly across diverse settings, outperforming benchmark estimators. In conjoint analysis with weak auxiliary signals, GAI reduces estimation error by approximately 50% and lowers human labeling requirements by more than 75%. In retail pricing, where all methods have access to the same auxiliary inputs, GAI consistently outperforms alternative estimators, highlighting the value of its construction rather than differences in information. In health insurance choice, it cuts labeling requirements by over 90% while maintaining decision accuracy. Across applications, GAI improves confidence interval coverage without inflating width. Overall, GAI provides a principled and scalable approach to integrating AI-generated information into decision-making pipelines.

---

## uid: `doi:10.2139/ssrn.6332878`

- title: Structure Without Knowledge Is Not Enough: Evidence from Taguchi Orthogonal Arrays
- authors: Ray Fatahi
- affiliations: not stated
- posted: 2026-04-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6332878
- keyword hits: llama, llm, mistral, qwen

### abstract

We show that structured decision inputstyped rules, scored evidence, domain ontologies are a precondition for LLM verdict robustness to be both achievable and testable. Using Taguchi L 9 orthogonal arrays to evaluate four decision-pipeline factors in 9 structured trials (vs. 3 4 = 81 exhaustive), we compare two datasets (n = 50 each): structured governance decisions derived from statutory rules and unstructured ethical scenarios from the Val-uePrism corpus, with a controlled within-subject follow-up on a 25-scenario subset. The central nding is that L 9 stability scores discriminate correct from incorrect verdicts on structured inputs (AUROC = 0.70 overall), rising to 0.83 on the medium-diculty tier where factor perturbations are most informative. On unstructured inputs, the same scores carry no diagnostic information (AUROC = 0.43, anti-correlated with correctness). The model's own condence scores are uninformative on both datasets (AUROC = 0.50). Separately, self-consistency testing (repeated evaluation at elevated temperature) returns perfect agreement across all 100 decisions, detecting no instability whatsoever. This indicates that domain formalization is not merely benecial for decision quality but necessary for robustness diagnostics to be meaningful. Supporting this, structured inputs produce signicantly higher verdict stability (s = 0.90 vs. 0.73, non-overlapping 95% CIs) and more concentrated instability proles. However, this comparison is confounded by domain and construction dierences between the two datasets. The L 9 ANOVA decomposition identies which operational factors drive instability for each decisiondiagnostic capability that random sampling cannot provide despite comparable detection rates. A controlled within-subject experiment (E6) conrms that structural formalization causally improves verdict stability (Wilcoxon p = 0.031, d = 0.41) but does not improve discriminative power (AUROC 0.44 → 0.34, n.s.), establishing that diagnostic value requires domain knowledge encoded in the structurenot structure alone. A cross-model evaluation across three 7B-class architectures (Llama, Mistral, Qwen) reveals that stability proles are model-specic (ICC = 0.07), meaning robustness certication does not transfer across models.

---

## uid: `doi:10.2139/ssrn.6415040`

- title: Auto Sim Ai: A Large Language Model-Based System For Survey Research Simulation
- authors: Jiajia Li
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6415040
- keyword hits: deepseek, large language model, large language models, llm, llms

### abstract

Survey research is central to the social sciences, but participant recruitment, cost, and timelines constrain traditional studies. Advances in Large Language Models (LLMs) create new opportunities for computational simulation of survey responses. We present Auto Sim AI, an open-source platform for LLM-based survey simulation with virtual personas. The system supports synthetic population generation, survey administration, intervention studies, and longitudinal designs with cross-wave conversation memory. It integrates multiple providers (LM Studio, DeepSeek, OpenAI), intelligent response caching for reproducible reruns, and standard scoring rules for PHQ-9, GAD-7, PSS-10, and WHO-5. We detail the modular architecture, persona-generation workflow, and an implementationfocused technical evaluation. As an application, we conduct virtual pilot testing for a nationwide survey of low-carbon knowledge, attitudes, and behaviors (target sample N = 1200). This manuscript is a preprint and has not yet undergone peer review; empirical validation against human responses is in progress. Accordingly, this version emphasizes system design, methodology, and preliminary application results, and both the manuscript and software will continue to receive iterative, versioned updates. Initial findings suggest value for instrument refinement and research design optimization, while important caveats regarding validity and appropriate use cases remain.

---

## uid: `doi:10.2139/ssrn.6619518`

- title: AI-Assisted Thinking Protocol: A Design-Based Study of Verification-First Learning
- authors: Haifa Alsubhi
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6619518
- keyword hits: chatgpt, claude, deepseek, gemini

### abstract

Current AI tutoring tools prioritize explanation delivery over understanding verification, reinforcing what Koriat and Bjork (2005) call the illusion of competence: learners believe they understand without being able to apply knowledge. This paper presents the AI-Assisted Thinking Protocol (AATP), a verification-first framework implemented as a structured prompt for generalpurpose AI systems. Rather than delivering explanations, the protocol requires learners to articulate understanding in their own words, apply concepts to novel situations, and pass transfer tests before progressing. We report on iterative protocol development across six versions and preliminary evidence from eight learning sessions conducted by two participants across two domains (mathematics for machine learning and data preparation) using five AI platforms (ChatGPT, Claude, DeepSeek, Gemini, and Copilot). Key findings include: five documented detection events in which the protocol identified and corrected shallow understanding; one participant correcting the AI during a session, indicating metacognitive development; voluntary upgrade from a simplified to the full protocol version by an external tester; 85% retention after one week without review; and zero-shot protocol absorption by Google NotebookLM, confirming behavioral distinctiveness. Limitations, design implications, and a research agenda for formal validation are discussed.

---

## uid: `doi:10.2139/ssrn.6636938`

- title: LLMs and Data Management for International Relations Scholars: Moving Beyond EuGene-Style Software
- authors: Paul Poast
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6636938
- keyword hits: large language model, large language models, llm, llms

### abstract

Large-n, machine readable spreadsheet data have been a fixture of international relations academic research for almost a century. As advancements in computing power and access led to the growing prominence of studies using large-n datasets throughout the 1970s, 1980s, and 1990s, so did the need for international relations scholars to have tools that could manage, organize, and even create such datasets. The EUGene software developed by Bennett and Stam (2000), as well as successor programs, filled that need. This paper argues and demonstrates that the advent of Large Language Models (LLMS) have rendered such software obsolete. International relations scholars should now make LLMs part of their data preparation workflows and, in doing so, will find that their research can be enhanced in ways that were previously computationally constrained if not fully infeasible.

---

## uid: `doi:10.2139/ssrn.6605178`

- title: The Model-Efficient Market Hypothesis Price Discovery, Consensus Hallucination, and the Limits of Informational Efficiency in LLM-Mediated Markets
- authors: Jeevan Renjith
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6605178
- keyword hits: foundation model, large language model, large language models, llm

### abstract

The Efficient Market Hypothesis (Fama, 1970) rests on an axiom so foundational that it is almost never named: cognitive independence. Prices are informative because investors process information through separate, uncorrelated reasoning processes; disagreement is the substrate of discovery. We argue that the diffusion of large language models across the investment industry dissolves this axiom. When a dominant fraction of portfolio managers, analysts, and research platforms delegates the step between information and interpretation to a small oligopoly of foundation models, the population of interpreters collapses toward a narrow band of shared posteriors. Information remains abundant and effectively free. What becomes scarce, costly, and price-determining is interpretation itself.

---

## uid: `doi:10.2139/ssrn.6618802`

- title: Data Value Density Enhancement for Large Language Model Training: A Comprehensive Survey
- authors: Yiliu Sun, Yanchao Lu, Jiaxi Cao, Linyang Li, Wei Liu, Chen Gong
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6618802
- keyword hits: large language model, large language models, llm, llms

### abstract

Driven by the scaling laws of Large Language Models (LLMs), increasing the volume of training data has been one of the primary strategies for enhancing the capabilities of LLMs over the past few years. However, as the accessible yet unused internet data becomes increasingly scarce, improving model performance by merely increasing data volume is no longer sustainable. In response, researchers have shifted their focus toward improving the performance of LLMs with limited training data and have proposed a variety of modern methods. Despite the progress, this research field lacks a clear definition and a comprehensive review, resulting in unclear research objectives and a fragmented landscape of methodologies. To bridge this gap, this paper provides a comprehensive survey aimed at offering a thorough understanding of the methodologies in this field. Specifically, we introduce the concept of "Data Value Density (DVD) enhancement" for LLM training, which serves as a unified perspective to summarize the main progresses of this research field. Based on the formal definition of DVD enhancement, we categorize existing methods into five primary directions. By employing this unified taxonomy, we provide an extensive review of state-of-the-art DVD enhancement techniques and highlight their strengths and weaknesses. Additionally, we review the representative datasets used for training and evaluating DVD enhancement models. Finally, we identify four major challenges faced by the current methods of DVD enhancement and present promising research directions for future advancements in this field.

---
