# Classification batch 95 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-95.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6814498`

- title: Copyright and Artificial Intelligence: The Importance of Memorisation and Attribution
- authors: Christian Koboldt
- affiliations: not stated
- posted: 2026-06-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6814498
- keyword hits: generative ai, large language model, large language models

### abstract

The intersection of copyright law and artificial intelligence raises fundamental questions about the optimal scope and form of intellectual property protection in a world of generative AI. Drawing on the economics of information goods, the technical literature on memorisation in large language models, and a comparative analysis of recent legal developments across Germany, the United Kingdom and the United States, this paper distinguishes two markets in which AI and copyright interact – the market for training data access and the market for reproduced outputs – and shows that they raise distinct welfare problems. Building on Gans (2024), we propose a capability-based levy that links payments to rights holders to the measurable memorisation rate of deployed models to reflect the potential harm caused in the market for reproduced outputs. We argue that the distribution problem that any such mechanism creates, as well as the non-pecuniary harm to creators from unattributed use of their work, can be addressed by mandating source-attribution capability at the model-architecture level. The capability-based approach has implementation advantages over training-data-based schemes, including reduced exposure to territorial arbitrage and stronger incentives for AI developers to reduce memorisation.

---

## uid: `doi:10.2139/ssrn.6880212`

- title: Can Open-Weight LLMs replace Build Log Analyzers?
- authors: Christian Macho, Katharina Stengg
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6880212
- keyword hits: large language model, large language models, llm, llms

### abstract

Build logs are a central source of information for problem solving in Continuous Integration. However, their length, noise, and tool-specific structure make them difficult to use, for example, when manually inspecting logs or automatically repairing issues. Existing Maven build log analyzers largely rely on manually created and maintained parsing rules, which can become outdated as build tools, plugins, and error messages evolve.In this paper, we study whether Large Language Models (LLMs) can replace such rule-based analyzers for Maven build log analysis. We evaluate several LLMs on a manually labelled ground truth of 400 Maven build logs and compare them against the state-of-the-art static rule-based analyzer MavenLogAnalyzer.Our results show that LLMs classify build outcomes with high accuracy, with the best models correctly classifying 381 logs (95.25%) compared to 368 logs (92.00%) for MavenLogAnalyzer. LLMs also improve the extraction of actionable failure details, especially failing modules and failing plugins, reducing failing-module errors from 217 cases (54.25%) to 8 cases (2.00%) for the best model. Runtime measurements show that MavenLogAnalyzer is substantially faster, with a median runtime of 0.003 seconds compared to 0.948 seconds for the fastest LLM.Overall, our findings indicate that LLMs are a promising alternative when extraction quality is important, while MavenLogAnalyzer remains preferable when runtime alone is the main criterion. Among the LLM-based approaches, gpt20 and gpt120 provide the strongest trade-off between build outcome classification, failure detail extraction, and practical runtime.

---

## uid: `doi:10.2139/ssrn.6815202`

- title: Context Engineering: A Governance Approach to Enterprise AI
- authors: Rohit Rajdev
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6815202
- keyword hits: agentic, generative ai, generative artificial intelligence, retrieval-augmented

### abstract

Enterprise adoption of generative artificial intelligence has moved faster than the governance mechanisms needed to control it. Many organizations now deploy chatbots, copilots, retrieval-augmented generation systems, and agentic workflows that can read enterprise documents, invoke tools, and generate operational recommendations. Yet conventional AI governance often focuses on model selection, model cards, high-level risk ratings, or retrospective audits of outputs. These measures are important but incomplete. In enterprise AI, the model is only one component of the decision system. The context supplied to the model-including documents, memories, prompts, retrieved passages, tool outputs, user attributes, policy instructions, and historical interactions-often determines whether an output is accurate, compliant, explainable, and safe. This paper introduces context engineering as a governance approach to enterprise AI. Context engineering is defined as the disciplined design, control, measurement, and audit of the information environment supplied to AI systems at inference time and over their operational lifecycle. The paper proposes a Context Governance Control Plane that integrates context inventory, classification and tagging, policy-aware retrieval, provenance capture, runtime guardrails, evaluation, and continuous improvement. This approach aligns with emerging AI governance expectations reflected in NIST AI RMF, the NIST Generative AI Profile, ISO/IEC 42001, the EU Artificial Intelligence Act, and the OECD AI Principles, while translating those principles into operational controls that enterprises can implement. The paper contributes a practical architecture, a control matrix, and an evaluation model for organizations seeking to deploy enterprise AI systems that are not only capable, but governable.

---

## uid: `doi:10.2139/ssrn.6876630`

- title: The Human Condition as Reflected in Contemporary Large Language Models
- authors: W. Russell Neuman
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6876630
- keyword hits: large language model, large language models, llm, llms

### abstract

This study seeks to uncover evidence of a latent structure in evolved human culture as it is refracted through contemporary large language models (LLMs). Drawing on parallel responses from six leading generative models to a prompt which asks directly what their training corpora reveal about human culture and behavior, we identify a robust cross-model consensus on a limited set of recurring cultural themes. The themes include narrative meaning-making, affect-first cognition, coalition psychology, status competition, threat sensitivity, and moral rationalization. Each provides grounds for further psychological and sociological inquiry. There is strong evidence of a convergence in these pattern recognition exercises as differences among models are shown to reflect varying explanatory lenses rather than substantive disagreement. We review these findings in the light of the evolving literatures of moral psychology, evolutionary psychology, anthropology, and the computer science literature on large-scale language modeling. We argue that LLMs function as cultural condensates -- compressed representations of how humans describe, justify, and contest their own social lives across trillions of tokens of aggregated communication and narration.

---

## uid: `doi:10.2139/ssrn.6864181`

- title: Consumer Preference Transmission in Agentic Markets
- authors: Andreas Kraft, Poet Larsen
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6864181
- keyword hits: agentic, ai agent, llm, llms

### abstract

As consumers increasingly delegate purchasing decisions to AI agents, firms face a new question: how does consumer heterogeneity translate into agent-mediated demand? Human and model preferences need not coincide, preferences may differ across models, and consumers nonrandomly select into agent use. We study this problem through delegated preference transmission: the extent to which consumer-level preferences and behavioral heuristics are preserved when an AI agent makes choices on a consumer's behalf. We develop a framework separating two necessary conditions for transmission: identifiability of the consumer parameter in the prompt and model responsiveness to that signal. Using a conjoint experiment and an incentivized online bookstore adoption task, we study attribute preferences as well as left-digit bias (LDB), a behavioral heuristic in price perception. Attribute preferences are meaningfully reflected in prompts and transmitted to agents. In contrast, high-LDB consumers write shorter prompts with less price information, but current LLMs do not meaningfully adjust their LDB in response; instead, agents pool consumers toward model-specific priors. Consumers with higher LDB are also more likely to state intent to use agents; revealed-choice evidence in a follow-up bookstore experiment is directionally consistent but does not reach conventional significance. A stylized pricing simulation shows that these forces change optimal markups, increase the use of $X.99$ pricing, and make market composition central to pricing decisions. These findings imply that agentic markets do not eliminate consumer heterogeneity; they transform it across consumers, prompts, models, and adoption decisions.

---

## uid: `doi:10.2139/ssrn.6878408`

- title: SALAD: Tail-Anchored Prompt Architecture for Trustworthy Edge NLP in Power System Cyber-Physical Systems
- authors: Han Ding, Zheyin Zhuang, Lujun Xue, Zhenyu Wang, Tong Jiang, Rui Bai, Renjun Feng
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6878408
- keyword hits: large language model, large language models, llm, llms

### abstract

The digitalization of power systems has generated high-velocity unstructured text streams—equipment defect reports, dispatcher operation tickets, and SCADA data-quality alerts—that demand automated semantic interpretation at the grid edge. Cloud-deployed large language models (LLMs) face fundamental barriers in this domain: data-sovereignty regulations prohibit transmission of operational data to third-party APIs; per-query costs scale unsustainably for provincial grid operators processing tens of thousands of daily records; and air-gap requirements categorically disqualify any solution requiring persistent internet connectivity. This study proposes SALAD (Structured Anchor Lite Augmentation Design), a four-level prompt framework specifically architected for ≤2B parameter models in power system cyber-physical system edge environments. SALAD replaces the traditional depth-first augmentation strategy (base → +CoT → +RAG) with a breadth-first constraint strategy centered on tail semantic anchoring. Across three domain-specific power system NLP tasks and 14 models from five families (0.8B–35B parameters), SALAD achieves a +51.8 percentage point improvement via Semantic Label Anchoring (p

---

## uid: `doi:10.2139/ssrn.6881781`

- title: MemGuard-Alpha: Detecting and Filtering Memorization-Contaminated Signals in LLM-Based Financial Forecasting via Membership Inference and Cross-Model Disagreement
- authors: Dip Roy, Rajiv Misra, Sanjay  Kumar Singh, Anisha Roy
- affiliations: not stated
- posted: 2026-06-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6881781
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are increasingly used to generate financial forecasts and alpha signals, but recent evidence suggests they memorize historical data from their training corpora, producing spurious in-sample accuracy that collapses out-of-sample. Existing remedies require costly retraining or input anonymization, with no practical method for filtering contamination at the signal level. We introduce MemGuard-Alpha, comprising two novel algorithms: (i) the MemGuard Composite Score (MCS), which combines five membership inference attack (MIA) methods with a temporal proximity feature via logistic regression, achieving Cohen's d = 18.57 in separating in-sample from out-of-sample prompts; and (ii) Cross-Model Memorization Disagreement (CMMD), which exploits natural variation in training cutoff dates across multiple LLMs and admits an interpretation as a fuzzy regression discontinuity design. Evaluated across seven LLMs (124M to 7B parameters), 50 S&P 100 constituents, 42,800 prompts, and 5.5 years of daily data (January 2019 to June 2024), CMMD achieves a Sharpe ratio of 4.11 versus 2.76 for unfiltered LLM signals, a 49% improvement after transaction costs. Signal accuracy reveals a crossover: in-sample accuracy rises with contamination (40.8% to 52.5% across quintiles) while out-of-sample accuracy falls (47% to 42%), providing direct empirical evidence that memorization inflates apparent accuracy at the cost of generalization.

---

## uid: `doi:10.2139/ssrn.6821398`

- title: Account-History Features for Social Bot Detection in the Era of Large Language Models
- authors: Gaurang Katyal
- affiliations: not stated
- posted: 2026-06-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6821398
- keyword hits: claude, gpt-4, large language model, large language models

### abstract

Bot detection on social platforms has historically relied on a mix of account-metadata features and features extracted from the text of posts and profile fields. The arrival of capable language models complicates the latter. A bot operator can run every post through GPT-4 or Claude and produce text whose surface statistics are difficult to distinguish from those of human writing, which weakens the predictive value of content-derived features. This paper asks how much of the detection problem can be solved by features that an attacker cannot easily manipulate at low cost: the age of the account, follower and friend counts and their ratios, profile completeness, and the structural properties of the handle. On a publicly redistributed corpus of 2,432 Twitter accounts with manually verified labels (43.0% bots), a random forest using only these accounthistory features achieves ROC-AUC of 0.977 in five-fold cross-validation, against 0.830 for a content-only baseline and 0.981 for the fusion model. The behavioral-versus-content gap is large and statistically significant by DeLong's test (z = 9.36, p < 0.001). We then evaluate two adversarial settings. In the first, we rewrite the text of bot tweets to match human surface statistics for URLs, hashtags, mentions, and casing; the content classifier's ROC-AUC degrades from 0.842 to 0.785 while the behavioral classifier is essentially unchanged. In the second, more aggressive setting we directly perturb the content feature values toward the human distribution; the content classifier falls below chance (AUC 0.466) while behavioral performance is invariant. We replicate the score distribution qualitatively on a 100-account sample of TwiBot-20. We conclude that operational bot detection should not treat content features as the primary signal; account-history features carry most of the load already and are not eroded by adversarial text rewriting.

---
