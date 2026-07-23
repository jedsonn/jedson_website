# Classification batch 2 of 5, edition 1

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-001/batch-2.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7121598`

- title: A Behavioral Taxonomy of LLM Failure Modes
- authors: Michael Kitamura
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7121598
- keyword hits: claude, gemini, large language model, large language models, llm

### abstract

This paper reports findings from an extended naturalistic observation study of recurring failure behaviors in large language models-output patterns that occur while a model appears competent, compliant, and confident. Four failure classes are identified: Overt Sycophancy, Covert Sycophancy, Confidence Drift, and False Confidence. The latter three are characterized from documented instances across GPT, Claude, and Gemini during ordinary working sessions, with no adversarial elicitation. Overt Sycophancy is included as a named class on the strength of its evident frequency in ordinary use, though no specimen has yet been captured and logged. Micro-Drift, one of three named Recursive Dynamics in this taxonomy, is a baseline-inheritance pattern in which a sub-threshold deviation becomes the working baseline for a subsequent pass, compounding across a chained workflow into progressive divergence from source material. Named variants, compound behaviors, and a workflow integrity and recovery protocol are documented. Each classification carries an explicit evidence status reflecting the number and diversity of confirming instances observed. A companion work (Kitamura, M., Covert Sycophancy in Large Language Models: A Behavioral Taxonomy from Naturalistic Observation, SSRN 6519098) provides full session-level case documentation for the same behaviors.

---

## uid: `doi:10.2139/ssrn.7024983`

- title: Zero-Shot Structured Data Extraction from Timely Disclosure Documents in PDF Format with Large Language Models
- authors: Nobushige Doi, Mayuri Tanaka
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7024983
- keyword hits: gpt-5, large language model, large language models, llm, llms

### abstract

Timely disclosure documents released through TDnet, operated by the Tokyo Stock Exchange in Japan, are a source of corporate information; however, many are distributed as PDFs and are not directly reusable by machines. This study evaluates zero-shot structured data extraction from Japanese TDnet PDFs using large language models (LLMs) and documenttype-specific JSON Schemas. We compared 12 conditions that combine three models, GPT-5.4, GPT-5.4-mini, and GPT-5.4nano, with four reasoning effort settings across eight disclosure types. Each condition was run three times to measure the output variation. GPT-5.4, with high reasoning effort, obtained the highest average score, with core field accuracies of 0.905 ± 0.045. The best settings differed by document type, and higher reasoning effort did not consistently improve accuracy. These results indicate that schema-guided extraction can support the structuring of timely disclosure PDFs. However, schema design, auxiliary field handling, output variation, and processing time must be considered during deployment.

---

## uid: `doi:10.2139/ssrn.7025538`

- title: DataPrep-bench: Benchmarking LLMs as Training Data Preparators
- authors: Hao Liang, Qifeng Cai, Yibo Lin, Jianzhuo Du, Qifeng Xia, Sizhe Qiu, Linzhuang Sun, Meiyi Qiang
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7025538
- keyword hits: fine-tuning, large language model, large language models, llama, llm, llms

### abstract

The quality of training data fundamentally determines the capabilities of large language models (LLMs), yet no unified benchmark exists to measure how well LLMs, agents, and data-centric workflows actually prepare training data end to end. We view LLM-driven data preparation as comprising two complementary capabilities: data construction, which transforms raw sources into supervised training data, and data quality evaluation, which predicts the training value of candidate datasets before downstream training; throughout, “quality” refers to downstream training utility rather than surface-level textual properties. We introduce DataPrep-Bench, the first unified benchmark that jointly evaluates both capabilities under a shared downstream-grounded protocol over six domains and multiple base models. For data construction, methods consume identical raw sources and are scored by fine-tuning a base model on their outputs jointly with Dolly-15k; alongside this track we release Data-Construction-Skill, a skill-guided agent that lifts the Dolly-only baseline by nearly 20 points absolute on Llama-3.1-8B Finance and is competitive with the strongest agent- and DataFlow-based methods in knowledge-extraction-dense domains. For data quality evaluation, scoring functions are scored by Pearson correlation with downstream performance on a shared candidate pool; we release the Distributional Alignment Score (DAS), a distribution-based evaluator that uses MMD between a candidate dataset and a domain proxy. DAS attains the strongest cross-model correlation in four of six domains and is the only metric clearing r &amp;gt; 0.70 simultaneously in Math, Science, and Medical, outperforming existing quality-, diversity-, and heuristic-based evaluators. DataPrep-Bench provides a unified, downstream-grounded framework for measuring progress on both capabilities as co-equal targets of LLM-driven data preparation.

---

## uid: `doi:10.2139/ssrn.7158720`

- title: Agentic Digital Twins for Community Energy Management: LLM-Orchestrated Control with Physics-Informed Simulation and Carbon-Aware Planning
- authors: Rui Wang
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7158720
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Buildings account for approximately 40% of global energy consumption and associated carbonemissions. Community-level demand flexibility through coordinated battery storage dispatch offerssignificant potential for peak demand reduction and carbon mitigation, yet existing control approachesface fundamental limitations: model predictive control (MPC) requires accurate system models andstruggles with distribution shift; deep reinforcement learning (DRL) is sample-inefficient and brittleto unseen scenarios; and standalone large language models (LLMs) lack physical grounding forsafe real-time control. This paper presents an agentic digital twin framework that integrates LLM-based reasoning with physics-informed digital twin simulation and machine learning forecastingtools. The LLM serves as an orchestrator that queries the twin state, invokes forecasting models,evaluates counterfactual dispatch scenarios through twin simulation, and commits carbon-awarebattery schedules. We evaluate the proposed method against four baselines — rule-based control,MPC, proximal policy optimization (PPO), and a standalone LLM without twin access — on theCityLearn 2020 benchmark across three California climate zones (hot-humid, hot-dry, and cold) with9 buildings and 30-day episodes. Results demonstrate that the agentic twin achieves 21.5% lowerpeak demand than DRL (𝑝 &lt; 0.001) and 2.3% lower carbon emissions than MPC (𝑝 &lt; 0.001), whileperforming comparably to MPC on peak metrics. Ablation studies reveal that carbon-aware planningcontributes the largest performance gain (26.5% peak reduction), followed by cost-aware LLM routing(19.8%). The system operates at approximately $9.85 per 30-day episode for a 9-building community,demonstrating economic feasibility for real-world deployment.

---

## uid: `doi:10.3386/w35374`

- title: A Practitioner's Guide to Using Large Language Models and Generative AI in Economic History
- authors: Andreas Ferrara
- affiliations: not stated
- posted: 2026-06-30
- source: NBER
- link: https://doi.org/10.3386/w35374
- keyword hits: agentic, generative ai, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are lowering the entry barriers to working with exciting data sources that used to require strong data science skills, such as handwritten ledgers, text, images, or sound recordings.This guide provides an introduction for researchers who are new to LLMs.It sets out a step-by-step workflow for turning a research idea into working code and data, and describes the four main ways of interacting with an LLM: the chat window, editor-integrated assistants, agentic coding tools, and the API.It then works through the decisions a practitioner meets in sequence, beginning with whether an LLM is the right tool and whether the data are allowed to be sent to one, then how to select models, write prompts, manage context limits, and control costs, and finally how to validate, reproduce, document, and correct LLM-generated measures in regression settings.A review of recent research shows how these tools already extract, link, harmonize, and classify historical data at scale.Four worked examples with replication files illustrate the use of LLMs.They classify emotions in paintings, link census records without names, measure newspaper salience and sentiment around the 1882 Chinese Exclusion Act, and score the emotional delivery of Franklin D. Roosevelt's wartime speeches.The guide also condenses the workflow, the bestpractice recommendations, and the preparation of replication packages into summary tables and checklists to aid applied economists.

---

## uid: `arxiv:2607.20270v1`

- title: Which Values Do LLMs Confuse? A Schwartz-Based Recognition Study
- authors: Andrei Chetvergov, Stepan Ukolov, Timofei Sivoraksha, Alexander Evseev, Mikhail Solovev, Valeriia Kuschenko, Maria Chistyakova, Sergey Bolovtsov
- affiliations: not stated
- posted: 2026-07-22
- source: arXiv
- link: https://arxiv.org/abs/2607.20270v1
- keyword hits: instruction-tuned, large language model, large language models, llm, llms

### abstract

Large language models are increasingly evaluated through the values they endorse, but such evaluations presuppose that models can identify the value expressed in a concrete situation. We study this prerequisite as controlled top-1 recognition over Schwartz's ten basic values. Our evaluation set contains 1,000 Russian situational texts, balanced across the ten values and independently labeled by two human annotators per item. We evaluate 21 instruction-tuned LLM runs under a fixed ranked-response protocol; 20 runs with reliable outputs form the semantic panel. Pooled Acc@1 is 0.683 and Acc@3 is 0.892, showing that models often locate the correct motivational region while ranking close alternatives unstably. Adjacent values account for 50.9% of semantic errors, compared with 24.4% under a checkpoint-specific null. Eight directed confusions recur across checkpoints and human-confirmed subsets. Several are strongly asymmetric, including Universalism to Benevolence, Tradition to Conformity, and Security to Power, whereas Stimulation-Hedonism forms a bidirectional boundary. Their severity is checkpoint-specific and can bias higher-order value profiles. The results motivate value-recognition evaluation that combines exact accuracy, ranked recovery, and directed error analysis.

---

## uid: `doi:10.2139/ssrn.5370043`

- title: Large Language Models for Supply Chain Decisions
- authors: David Simchi-Levi, Konstantina Mellou, Ishai Menache, Jeevan Pathuri
- affiliations: not stated
- posted: 2025-07-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.5370043
- keyword hits: large language model, large language models, llm, llms

### abstract

Supply Chain Management requires addressing a variety of complex decision-making challenges, from sourcing strategies to planning and execution. Over the last few decades, advances in computation and information technologies have enabled the transition from manual, intuition and experience-based decision-making, into more automated and data-driven decisions using a variety of tools that apply optimization techniques. These techniques use mathematical methods to improve decision-making. Unfortunately, business planners and executives still need to spend considerable time and effort to (i) understand and explain the recommendations coming out of these technologies; (ii) analyze various scenarios and answer what-if questions; and (iii) update the mathematical models used in these tools to reflect current business environments. Addressing these challenges requires involving data science teams and/or the technology providers to explain results or make the necessary changes in the technology and hence significantly slows down decision making. Motivated by the recent advances in Large Language Models (LLMs), we report how this disruptive technology can democratize supply chain technology - namely, facilitate the understanding of tools'outcomes, as well as the interaction with supply chain tools without human-in-the-loop. Specifically, we report how we apply LLMs to address the three challenges described above, thus substantially reducing the time to decision from days and weeks to minutes and hours as well as dramatically increasing planners'and executives'productivity and impact.

---

## uid: `doi:10.2139/ssrn.7028322`

- title: Scalable Linear Bayes Prediction for Mixtures of Experts and LLMs
- authors: Nicholas G. Polson, Vadim Sokolov, Daniel Zantedeschi
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7028322
- keyword hits: large language model, large language models, llm, llms

### abstract

A companion paper shows that Bayes Linear (BL) estimation and cross-fitted prediction-powered inference (Cross-PPI) solve the same Kalman-gain equation, differing only in whether the effective prior precision comes from a subjective elicitation V −1 0 or the information matrix N −1X ⊤ u Xu of an unlabelled pool. This paper extends that duality to dynamic, non-Gaussian, and large-scale settings, and uses it to explain—and quantitatively demonstrate—why sparse Mixture-of-Experts (MoE) training of large language models (LLMs) is efficient. We prove four results. First, the Ensemble Kalman Filter (EnKF, Evensen, 1994) is BL applied sequentially with a Monte Carlo prior; we bound its excess risk relative to the exact Kalman filter as O(p/M) in ensemble size M and confirm the rate numerically. Second, the Bengtsson–Snyder–Nychka (BSN) mixture filter (Bengtsson et al., 2003) extends the EnKF to non-Gaussian forecasts via a Gaussian mixture with per-component Kalman updates; we prove it degenerates gracefully to the EnKF under unimodality, and—new to this paper—prove a threshold theorem identifying exactly when the mixture helps and when it hurts, governed by the ratio of observation noise to modal separation. A controlled experiment confirms the predicted crossover: a 40% error reduction under weak observations reverses to a 41% increase under strong observations. Third, we formalise the Linear Bayes Mixtureof-Experts (LB-MoE) estimator, prove its consistency and asymptotic normality, and give a parallel-complexity theorem with the honest bound min(K,1 + N p2/p 3 )—correcting an over-optimistic K× claim and confirmed by real linear-algebra timing. Fourth, we connect LB-MoE to sparse LLM MoE architectures through five exact structural correspondences, and prove that the Adam optimiser is a diagonal Kalman filter with exponential forgetting that violates the BL tower property. We make this last point vivid with a sequential continual-learning experiment: training on five tasks in turn, exact BL recovers the oracle joint-fit solution to within numerical precision (relative error 7×10−5 ) and shows essentially no forgetting, while SGD and Adam exhibit 5.1× and 3.5× forgetting ratios on the earliest task—a direct, quantitative demonstration of what the tower property buys a learning algorithm. We further resolve three open problems left by the conference version of this work: a general-K extension of the mixture threshold theorem, confirmed to widen monotonically with the number of modes; a bias-floor (rather than continuous-rate) characterisation of LoRA rank, confirmed by a sharp numerical cliff at the true update rank; and an exact federated BL aggregation theorem with a closed-form differential-privacy-utility tradeoff, confirmed to machine precision in the no-privacy limit.

---
