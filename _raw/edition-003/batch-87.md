# Classification batch 87 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-87.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6709818`

- title: Evaluating Large Language Model Ensembles as Probabilistic Forecasters: An Empirical Study on Live Real-World Events
- authors: Demetre Tsiklauri
- affiliations: not stated
- posted: 2026-05-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6709818
- keyword hits: large language model, large language models, llm, qwen

### abstract

Accurate real-time probability forecasts are important for policy, markets, and operational decisions, and live prediction markets, to this day, remain a high quality crowd benchmark for it. We test whether ensembles of off-the-shelf large language models are able to produce competitive forecasts on the same live events, and evaluated twenty-one models on N =23 Polymarket binary contracts at three pre-resolution snapshots (T1-T3), using repeated snapshot sampling and fixed cross-time/cross-model pooling operators. The performance of the models are scored with Brier and log loss, plus unitwise win counts and calibration tests, against time-synchronized Polymarket medians and a coin-flip baseline. The strongest fixed ensemble recipe, MedianOfMedians, improves compared to GPT o3 at every snapshot (mean Brier 0.129/0.069/0.115 vs. 0.173/0.163/0.203), and ultimately beats the coin-flip baseline on most contracts (20/23, 19/21, 18/21). Though the same ensemble remains weaker on average relative to the Polymarket mean Brier (0.056/0.008/0.000), especially at later stages when the market prices have largely converged. Despite the success of MedianOfMedians over individual models, some single models still showed notable unit-level wins, such as Qwen 3-235B-A22B-2507 (best T1 PMB: 12/23), which indicates useful but uneven and model-specific signal. Overall, LLM ensembling is a practical low-latency complement to quantitative systems for live forecasting, but cash-backed human aggregates still remain the more accurate source for event forecasting.

---

## uid: `doi:10.2139/ssrn.6765414`

- title: Analysing Moral Bias in Finetuned LLMs through Mechanistic Interpretability
- authors: Bianca Raimondi, Daniela Dalbagno, Maurizio Gabbrielli
- affiliations: not stated
- posted: 2026-05-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6765414
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) have been shown to internalize human-like biases during finetuning, yet the mechanisms by which these biases manifest remain unclear. In this work, we investigated whether the well-known Knobe effect, a moral bias in intentionality judgements, emerges in finetuned LLMs and whether it can be traced back to specific components of the model. We conducted a Layer-Patching analysis across 3 open-weights LLMs and demonstrated that the bias is not only learned during finetuning but also localized in a specific set of layers. Surprisingly, we found that patching activations from the corresponding pretrained model into just a critical layer is sufficient to eliminate the effect. Our findings indicate that social biases in LLMs can be interpreted, localized, and mitigated through targeted interventions, without the need for model retraining.

---

## uid: `doi:10.2139/ssrn.6771695`

- title: Generative Query Expansion for Bug Localization via Local LLMs
- authors: Allysson Costa e Silva, Marcelo Maia, João Batista Mendes, Christine Martins de Matos
- affiliations: not stated
- posted: 2026-05-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6771695
- keyword hits: large language model, llama, llm, llms

### abstract

Context: The process of bug localization is typically impaired by the semantic disconnect between usersubmittedreports and technical software artifacts. Objective: This study investigates the impact of fusingLarge Language Model (LLM) generative capabilities with continuous dense vector spaces to improve buglocalization accuracy. Method: We propose a hybrid pipeline using a 4-vector dense fusion strategy thatcombines a Doc2Vec semantic space with Hypothetical Document Embeddings (HyDE) generated via Llama3 (8B). The framework was evaluated on 633 bug reports from six open-source Java systems, incorporatingmultiple configurations and independent runs to mitigate stochasticity. Results: The proposed strategymitigates LLM volatility and significantly outperforms baseline methods in the majority of datasets, achievingMean Reciprocal Rank (MRR) improvements of up to 67.77% (p

---

## uid: `doi:10.2139/ssrn.6773311`

- title: Towards a Safety Copilot: Predicting and Interpreting Risky Non-Motorist Behaviors with a Fine-Tuned Large Language Model
- authors: Amin Moeinaddini, Carmelo D&apos;Agostino, Yuanchang Xie, Mahmoud Mesbah, Jia Hu, Tianren Zhang, Yajie Zou
- affiliations: not stated
- posted: 2026-05-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6773311
- keyword hits: large language model, llama, llm, llms

### abstract

Non‐motorist fatalities represent a substantial and growing share of U.S. traffic deaths. These incidents are driven by complex, context-dependent risky behaviors such as failure to yield, improper crossings, and inattentiveness. Predicting these behaviors and their collision outcomes remains a critical challenge for advanced driver-assistance and traffic safety systems. This study introduces a copilot safety framework that reframes accident prediction as a text-reasoning task, leveraging a fine-tuned large language model (LLM) to jointly predict risky non-motorist behavior, vehicle–non-motorist collision angle, and number of fatalities from structured accident narratives. We fine-tune Llama 3.1 8B with Low-Rank Adaptation on 69,719 fatal accident records from the Fatality Analysis Reporting System (2015–2023), converting each incident into a natural-language prompt that includes several categories of context: general accident information, non‐motorist demographics, environmental conditions, weather, traffic maneuvers, road surface information, and vehicle details. On a held-out test set, the fine-tuned LLM achieves the highest predictive performance among all models across all three tasks, but absolute performance is low for the challenging 10‐class non‐motorist behavior task. For collision angle, the LLM attains high accuracy but a much lower macro F1 due to severe class imbalance, while for single vs. multiple fatality classification, it achieves near‐perfect scores. Shapley value analysis reveals that the LLM’s feature attributions agree in sign with a logistic regression benchmark in approximately 70% of feature–class pairs overall; however, when restricting to statistically significant logit coefficients, 18 direct sign conflicts emerge, concentrated in complex accident types (e.g., side impacts, improper turns) and low‐prevalence classes. A prototype deployment integrating a vision-language model (VLM) with the LLM copilot demonstrates the feasibility of extracting real-world scenario descriptors from pre-accident video and generating interpretable, feature‐attributed predictions. The findings highlight that while fine‐tuned LLMs can outperform traditional methods on several accident prediction tasks, they still struggle with highly imbalanced, linguistically subtle behaviors, and their post‐hoc explanations may hallucinate directionally incorrect effects for safety‐critical features. Improving data quality, class balance, and explanation faithfulness remains essential before such models can inform driver warnings or engineering countermeasures.

---

## uid: `doi:10.2139/ssrn.6771196`

- title: Generative Multi-Modal Sensor Fusion for Mobile Robotics: Methods, Challenges, and Trust Considerations
- authors: Komeil Asli, Mohammad Loni, Henrik Andreasson, Martin Magnusson, Masoud Ebrahimi
- affiliations: not stated
- posted: 2026-05-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6771196
- keyword hits: generative ai, llm, llms

### abstract

Mobile Robots rely on multi-sensor fusion for robust perception, localization, and decision-making. However, traditional fusion methods often struggle to effectively integrate highly heterogeneous data, resolve modality conflicts, and remain reliable under adverse conditions. Generative AI (transformers, GANs, VAEs, diffusion models, LLMs) offers a new paradigm for cross-modal learning and uncertainty modeling. This survey systematically reviews Generative AI-driven sensor fusion in mobile robotics, categorizing methods by generative model family and application domain. Furthermore, we discuss the trustworthiness of sensor fusion systems, covering robustness, explainability, calibration, and privacy, and identified key open challenges and future research directions. Our contributions include: (1) a taxonomy of generative AI fusion methods by model family, (2) application-wise synthesis across perception, localization, planning, and safety, (3) a dataset catalog with coverage gap analysis, (4) a unified evaluation framework for generative fusion, and (5) a comprehensive trustworthiness lens addressing robustness, explainability, validation, and privacy across all sections.

---

## uid: `doi:10.2139/ssrn.6621459`

- title: Square Root Law for Optimal Excavator Bucket Cleaning Threshold, Cascade Effects on Fleet Haul Cycle Time, and Dual Anti-Adherent Mechanism in Open-Pit Mining Operations
- authors: Matheus Castro
- affiliations: not stated
- posted: 2026-05-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6621459
- keyword hits: claude, gemini, large language model, large language models

### abstract

Competing Interests: The author is affiliated with Easy Ore Handling Technology, a company that develops anti-adherent fluids and carry-back monitoring systems discussed in this manuscript. However, the analytical framework presented is product-agnostic: the efficacy parameter η accepts values from any commercial formulation, including those of competing suppliers. The reported efficacy range η ≈ 0.70-0.85 is consistent with field experience and does not imply that any specific formulation achieves this level. No other financial or non-financial competing interests are declared. Use of Large Language Models and AI-Assisted Technologies: During the preparation of this manuscript, the author used Claude (Anthropic), Grok (xAI), and Gemini (Google DeepMind) to assist with drafting and editing text, generating mathematical derivations, and producing figures. The author reviewed, verified, and takes full responsibility for all content, including mathematical results, numerical examples, and conclusions. The underlying research concept, physical model, and analytical framework-including the bucket accumulation model, the cascade condition derivation, and the dual anti-adherent mechanism-were developed entirely by the author.

---

## uid: `arxiv:2605.16699v1`

- title: Your SaaS Is an Insurance Product: A Modeling Framework
- authors: Caio Gomes
- affiliations: not stated
- posted: 2026-05-15
- source: arXiv
- link: https://arxiv.org/abs/2605.16699v1
- keyword hits: chatgpt, claude, llm

### abstract

Capped-usage SaaS products -- LLM subscriptions such as Claude Code and ChatGPT, cloud platforms such as Vercel and Cloudflare Workers, corporate benefit platforms, identity-verification services with liability transfer -- share a structural signature with insurance products: a fixed premium decoupled from realized consumption, stochastic per-user demand with heavy-tailed severity, a non-fungible cap that resets on a fixed schedule, and a portfolio-level exposure that requires reserve adequacy under tail risk. We argue that this is not an analogy. It is the same operational problem actuarial science has been tooled for decades to address, restated with new dependent variables (tokens, bandwidth bytes, function-invocations, gym check-ins) in place of medical claims. This paper proposes a modeling framework for capped-usage SaaS pricing built from frequency-severity decomposition, premium calculation principles, and Monte Carlo reserve adequacy. We map the framework to publicly observable subscription tiers in two domains (LLM services and cloud platforms), ground it in canonical health-insurance economics (Arrow 1963; Pauly 1968; Manning et al. 1987; Brot-Goldberg et al. 2017), and demonstrate divergence from traditional unit economics through a worked example. The contribution is operational rather than theoretical: not a new theorem, but vocabulary and tools currently absent from cs.LG/stat.ML practice.

---

## uid: `doi:10.2139/ssrn.6777210`

- title: ProxyDAN：Efficient Jailbreak Attack Acceleration Framework Based on Proxy Models
- authors: hanyang zhang, lei sun
- affiliations: not stated
- posted: 2026-05-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6777210
- keyword hits: large language model, large language models, llm, llms

### abstract

The aligned Large Language Models (LLMs) are powerful language understand-ing and decision-making tools that are created through extensive alignment with human feedback. However, these large models remain susceptible to jailbreak attacks。Attackers can induce models to generate malicious outputs that violate alignment objectives through carefully crafted prompts. Studying jailbreak attacks not only helps reveal potential vulnerabilities in models but also provides crucial insights for building more robust security defense mechanisms. Auto-DAN, as a landmark achievement in automatically generating covert jailbreak prompts, has propelled the advancement of optimization-based jailbreak techniques. However, its attack efficiency still requires improvement.This paper addresses the high computational cost in Auto-DAN caused by the genetic algorithm's heavy reliance on model queries by proposing an efficient alternative optimization scheme. We observe that the genetic algorithm repeatedly invokes the target model for scoring during iterations, yet utilizes only its outputs rather than gradient information, resulting in substantial token and time consumption. To address this, we designed a lightweight surrogate model. By sampling response data from the target model, we fine-tuned a pre-trained language model to approximate the target model's scoring behavior. Furthermore, we proposed two hybrid evaluation strategies that significantly reduce reliance on the target model while maintaining high attack success rates.Experiments on the AdvBench dataset demonstrate that our method reduces overall computation time by 15% to 60% while maintaining attack success rates comparable to the baseline, and reduces token consumption to 20% of the original method. This research provides a new technical approach for efficient jailbreak attacks and defenses, and offers insights for lightweight design in large-model security evaluation systems.

---
