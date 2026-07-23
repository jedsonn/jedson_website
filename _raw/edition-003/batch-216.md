# Classification batch 216 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-216.answer.json` as a JSON array.

---

## uid: `arxiv:2607.19266v1`

- title: Toward Auditable Fraud Detection: Combining Graph Features, Model Explanations, and Agentic Case Investigation
- authors: Rahil Sharma
- affiliations: not stated
- posted: 2026-07-21
- source: arXiv
- link: https://arxiv.org/abs/2607.19266v1
- keyword hits: agentic, llm

### abstract

Fraud detection systems must scale with rising transaction volume while remaining explainable and reviewable. We study a layered pipeline on the PaySim dataset that combines a gradient-boosted classifier, graph-derived structural features, an autoencoder-based anomaly signal, TreeSHAP explanations, and a bounded LLM investigation agent applied to cases the classifier scores uncertainly. Before any model comparison, we identify and remove a simulator-specific balance shortcut that would otherwise inflate baseline performance. After this correction, neither the graph features nor the anomaly signal improves Average Precision on the full test set. Both, however, rank fraud better within the subset of cases receiving intermediate baseline scores. In a controlled experiment with injected multi-account fraud rings, engineered structural features recover all injected test transactions, while the tabular baseline misses roughly a quarter of them. The investigation agent underperforms direct thresholding of the classifier it relies on, reaching 65.0% accuracy against 71.7% on a balanced 60-case sample, despite having access to model explanations, graph context, and retrieved reference cases. Of the eight decisions the agent changed, six replaced correct classifier outputs with errors, and it produced a coherent written rationale in each case. An exploratory disagreement-based escalation rule flagged two of these agent errors for human review without flagging any correct decision. We conclude that each component of a layered fraud system contributes only under specific conditions, and that a plausible rationale from an investigation agent is not evidence of a better decision.

---

## uid: `doi:10.2139/ssrn.7153940`

- title: Creating Privacy Value Through Artificial Intelligence Prompt Literacy: The Role of Self-Investment
- authors: Johanna Zimmermann, Yakov Bart, Koen Pauwels
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7153940
- keyword hits: generative artificial intelligence, prompting

### abstract

Generative artificial intelligence (GenAI) is reshaping how consumers and employees disclose data to digital systems. Unlike the discrete disclosure decisions examined in previous literature on privacy settings, GenAI use unfolds through interactive prompting in which users share information to cocreate outputs. This research examines how self-investment in such disclosure processes shapes perceived privacy value, defined as the perceived net value of benefits relative to privacy risks. Across four studies, we show that greater self-investment increases perceived ownership of the cocreated output; moreover, the effect of self-investment on ownership is strongest when interactions involve sensitive data disclosure, with ownership subsequently shaping privacy value through perceived benefits and privacy risks. Finally, AI prompt literacy is an actionable antecedent of self-investment: a field intervention and an online experiment show that even modest improvements in practical prompting capability can increase engagement with GenAI. The findings contribute to privacy, GenAI, and cocreation research by showing that privacy evaluations in GenAI contexts are dynamic, self-invested, and shaped by users' ability to guide the interaction.

---

## uid: `doi:10.2139/ssrn.7057118`

- title: The Cognitive Unit : A New Unit of Analysis for the AI Age-From Individual to Human-Agent Value Creation
- authors: Alex Lin
- affiliations: not stated
- posted: 2026-07-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7057118
- keyword hits: ai agent, generative artificial intelligence

### abstract

Since the Industrial Revolution, the social sciences have implicitly treated the Individual as the basic unit of analysis for value creation, labor, organization, and civilization. The proliferation of generative artificial intelligence and multi-agent orchestration is reorganizing how cognitive labor-memory, reasoning, drafting, and execution-is performed, increasingly distributing it across human operators and networks of AI agents. This paper introduces the Cognitive Unit as a new unit of analysis for the AI age: a value-creating system composed of a sovereign human observer coordinating multiple AI agents, external memory, and cognitive workflows. Drawing on secondorder cybernetics (von Foerster, 2003), process philosophy (Whitehead, 1929/1978), and the author's prior work on Personal Sovereign AI and the Process-Paradox Framework (Lin, 2026a, 2026b), the paper argues that the Cognitive Unit, rather than the Individual, increasingly constitutes the basic unit through which value is created in contemporary economies. The paper develops the internal architecture of the Cognitive Unit, proposes three testable propositions concerning its productivity, and traces its implications for economics, sociology, management, political science, education, and civilizational theory.

---

## uid: `doi:10.2139/ssrn.7048978`

- title: Bayesian World Models
- authors: Nicholas G. Polson, Vadim Sokolov
- affiliations: not stated
- posted: 2026-07-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7048978
- keyword hits: in-context learning, large language model, large language models

### abstract

A world model learns a compressed, predictive representation of an environment and lets an agent plan by "dreaming"-rolling the model forward in latent space rather than in the costly real world (Ha and Schmidhuber, 2018). We argue that such a model, if it is to be rolled forward and optimized against, must be Bayesian. A world model is a family of one-step predictive kernels, and the only family that composes coherently into a joint law over trajectories is a σadditive posterior predictive, which under exchangeability is Bayesian updating on an unknown mechanism (de Finetti). Three consequences follow. First, large language models already are Bayesian world models: next-token prediction is an amortized Dirichlet-multinomial posterior predictive whose noninformative limit is a Bayesian bootstrap over corpus continuations, with temperature as tempering and in-context learning as posterior updating (Dalal and Misra, 2024; Rubin, 1981; Newton et al., 2021). Second, conformal prediction gives finite-sample marginal coverage for a single step but cannot serve as the belief state: by the separations of Datta et al. (2025), per-step coverage does not compose across a rollout, and a controller planning in a rankreduced dream is provably deficient. Third, "cheating the world model" (Ha and Schmidhuber, 2018) is off-support misspecification, curable only by epistemic uncertainty that widens where data are scarce-exactly the mechanism that safe model-based agents such as LAMBDA (As et al., 2022) use, and which lets us prove that a multi-step safety constraint is a path-space functional requiring the coherent kernel. The design principle is one line: carry a σ-additive predictive kernel as the state; attach conformal wrappers only as terminal guardrails.

---

## uid: `doi:10.2139/ssrn.7163765`

- title: Explainable Deep Learning Models for National-Scale Electricity Demand Forecasting in Indian Smart Grid Systems
- authors: Sitanath Biswas, Dipanjana Biswas, Shubhashree Sahoo, sujata dash, Milind Kundu
- affiliations: not stated
- posted: 2026-07-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7163765
- keyword hits: generative ai, transformer model

### abstract

Accurate electricity demand forecasting is essential for the efficient planning and operation of modern smart grids, particularly in rapidly urbanizing countries such as India where demand patterns exhibit significant temporal variability and regional heterogeneity. While recent research increasingly explores attention-based and generative AI models for energy forecasting, their practical advantages over established deep learning approaches remain insufficiently validated on large-scale real-world datasets. This study aims to evaluate and compare the forecasting performance of Long Short-Term Memory (LSTM) and Transformer models for state-level electricity demand prediction across India. A nationwide analysis was conducted using state-level electricity load data from 2014 to 2024 at daily resolution. Both LSTM and Transformer architectures were implemented under a unified experimental framework. The models were trained using historical load data along with meteorological variables and calendar-based features. Forecasting performance was evaluated using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE). To enhance model transparency and interpretability, Shapley Additive explanations (SHAP) were applied to analyze global feature importance and instance-level prediction behaviour. Experimental results demonstrate that the LSTM model consistently outperforms the Transformer architecture, achieving a lower MAE of 0.0384 and RMSE of 0.0541. The findings indicate that recurrent neural network architectures remain highly effective for short-term electricity demand forecasting, particularly in scenarios characterized by strong autoregressive temporal patterns. SHAP analysis further reveals that historical load values are the most influential predictors in the forecasting process, while the contribution of exogenous variables such as weather and calendar features appears comparatively limited at the daily forecasting scale. The results highlight that despite the growing popularity of attention-based architectures, traditional recurrent models like LSTM continue to provide strong predictive performance for time-series electricity demand forecasting. The interpretability provided by SHAP analysis also enhances trust and transparency in AI-driven energy forecasting systems, which is critical for real-world smart grid applications. This study demonstrates that LSTM remains a robust and reliable approach for daily electricity demand forecasting in large-scale smart grid environments. The findings provide practical guidance for selecting appropriate forecasting models and emphasize the importance of interpretable AI techniques for supporting data-driven decision-making in modern energy management systems.

---

## uid: `doi:10.2139/ssrn.4337484`

- title: Education in the Era of Generative Artificial Intelligence (AI): Understanding the Potential Benefits of ChatGPT in Promoting Teaching and Learning
- authors: David Baidoo-Anu, Leticia Owusu Ansah
- affiliations: not stated
- posted: 2023-01-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.4337484
- keyword hits: chatgpt, generative artificial intelligence

### abstract

NOT AVAILABLE. You have title and authors only. Set bullet_provenance to "none", return an empty bullets array, and classify field and role only if the title makes it unambiguous.

---

## uid: `doi:10.2139/ssrn.4341500`

- title: Is ChatGPT Leading Generative AI? What is Beyond Expectations?
- authors: Ömer Aydın, Enis Karaarslan
- affiliations: not stated
- posted: 2023-01-31
- source: SSRN
- link: https://doi.org/10.2139/ssrn.4341500
- keyword hits: chatgpt, generative ai

### abstract

NOT AVAILABLE. You have title and authors only. Set bullet_provenance to "none", return an empty bullets array, and classify field and role only if the title makes it unambiguous.

---

## uid: `doi:10.2139/ssrn.4335945`

- title: Large Language Models as Fiduciaries: A Case Study Toward Robustly Communicating With Artificial Intelligence Through Legal Standards
- authors: John Nay
- affiliations: not stated
- posted: 2023-02-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.4335945
- keyword hits: large language model, large language models

### abstract

NOT AVAILABLE. You have title and authors only. Set bullet_provenance to "none", return an empty bullets array, and classify field and role only if the title makes it unambiguous.

---
