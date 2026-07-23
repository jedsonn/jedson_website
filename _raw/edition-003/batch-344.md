# Classification batch 344 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-344.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6959458`

- title: Context Engineering at Enterprise Scale: Multi-Signal Repository Discovery for LLM-Assisted Software Development
- authors: Papa Rao Avasarala
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6959458
- keyword hits: large language model, llm

### abstract

Large language model (LLM) agents that assist software development require accurate identification of relevant source code repositories from enterprise catalogs containing hundreds or thousands of entries. Existing approaches rely on either keyword search or embedding-based similarity alone, each suffering from well-known failure modes: keyword search misses semantically equivalent terms while vector search conflates superficially similar but functionally distinct services. We present a five-layer scope resolution algorithm that combines tagbased exact matching, full-text search, capability indexing, vector nearest-neighbor retrieval, and identifier re-scoring into a unified scoring framework. The algorithm employs compound-term boosting (3× multiplier for multi-word matches), square-root length normalization, and a dual-mode entity extraction pipeline combining synchronous regex patterns with asynchronous LLMbased semantic extraction. Deployed internally at a Fortune 50 retailer across an internal enterprise catalog of 871 application repositories, the algorithm achieves a 94.6% scope resolution success rate across 879 pipeline executions during early adoption (as of June 2026), and resolves monorepo sub-applications that single-strategy approaches consistently miss. We present the algorithm design, scoring formulation, and enterprise evaluation results from an ongoing internal adoption.

---

## uid: `doi:10.2139/ssrn.7012498`

- title: Generative AI as an Inequality Amplifier: Language Compatibility, Leapfrogging and Productivity Growth
- authors: Yang Chen, Anxu Wang
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7012498
- keyword hits: chatgpt, generative ai

### abstract

We provide the first causal evidence that generative AI amplifies global inequality through linguistic compatibility with training data. Exploiting the November 2022 release of ChatGPT as a natural experiment across 169 economies, we find that a onestandard-deviation increase in Language Intensity-a country's linguistic compatibility with AI training data-raises productivity growth by 0.94 percentage points. This produces "linguistic leapfrogging": low-income but linguistically compatible economies-Ghana, Nigeria-match the gains of wealthy Anglophone nations, while high-income but incompatible economies like Japan see none. We conduct a controlled experiment to provide micro-foundations: across twelve languages, a generative AI tool delivers business decisions of lower economic value and higher cost as language resourcedness falls, and while a frontier model nearly closes the quality gap, the cost gap-fixed at the tokenizer-is structural and does not. A structural model of AI-augmented technology adoption, calibrated to our empirical estimate, projects these patterns forward and shows that multilingual AI development would cut the inequality cost of AI-driven growth by 59 percent. Our results challenge standard views of technology diffusion and reveal that AI introduces a new axis of global stratification along linguistic lines.

---

## uid: `doi:10.2139/ssrn.6959638`

- title: Mandate : Underwriting, Monitoring and Governing AI Agents that Transact and Borrow A Credit-Risk and Accountability Workflow for Agentic Commerce
- authors: John Christiansen
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6959638
- keyword hits: agentic, ai agent

### abstract

Autonomous and semi-autonomous AI agents have begun to transact and, in short order, will borrow on behalf of consumers and businesses. The payment industry has moved quickly to build the rails for this: identity, authorisation and settlement standards are emerging from the card networks and the protocol consortia-Google and Coinbase's Agent Payments Protocol (AP2), the Stripe-OpenAI Agentic Commerce Protocol (ACP), Coinbase's x402, and the card networks' agentic tokens (Mastercard Agent Pay, Visa Intelligent Commerce). These rails settle who the agent is and that a payment may be made. They do not decide how much credit to extend, whether it is affordable, whether the agent has been compromised or has drifted from its principal's intent, or who is accountable when something goes wrong. Those are credit risk and conduct questions. This paper sets out MANDATE, an end-to-end decision workflow that treats an agent as a bounded delegate operating under a mandate envelope. The workflow combines: (i) the mandate envelope as the unit of bounded, time-boxed, revocable authority; (ii) a three-layer dynamic limit that tightens under uncertainty rather than refreshing periodically; (iii) a credit-grounded agent trust score; (iv) an online behavioural change-point monitor - a Mahalanobis drift statistic on a streaming baseline, winsorised and fed to a Page-Hinkley test-paired with a graduated, reversible circuit breaker; (v) a hash-chained provenance ledger; and (vi) a transparent liability-attribution matrix. A conformance gap-map scores a deploying firm's readiness control-by-control, and a thin adapter layer maps each standardised rail onto the same engine. On an illustrative synthetic stream into which a behavioural compromise is injected-with every transaction kept below the static per-transaction cap-the monitor detects the regime change two transactions after onset and the breaker revokes the mandate shortly afterward, while the ledger detects a retrospective tamper. All figures and thresholds are illustrative and configurable. The contribution is a coherent, auditable workflow that closes the credit-and-conduct gap the payment rails leave open.

---

## uid: `doi:10.2139/ssrn.6969839`

- title: A Study on an Explainable Causal-Enhanced LLM Agent for Predicting the Forming Quality of Automotive Component Materials
- authors: Jingcheng Zhao, Jiayu Fan, Liangze Li
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6969839
- keyword hits: llm

### abstract

Raw material composition, heat treatment, cooling, equipment parameters and die condition have an impact on the forming quality of materials for automotive components. Current prediction models can detect the defect or deviation in the performance, but are not so much supported for finding out the root cause of anomaly and for making the changes in the process. In this paper, a causal enhanced LLM Agent explainable analysis framework is proposed. The study builds a multi-source manufacturing dataset that includes the composition of raw materials, heat treatment curves, forming pressure, cooling time, die condition, inspection outcome, and rework records;Random Forest, Multi-Layer Perceptron, XGBoost, and TabNet are used to predict strength deviation, surface defect grades, and batch pass rates;SHAP, NOTEARS, and counterfactual reasoning are combined to identify the key process variables and their influence paths;In addition, a RAG-LLM Agent is built to fuse the process specifications, material handbooks, historical anomaly cases, and model interpretation results, which helps to generate quality root cause analysis and process adjustment recommendation. As an example, a material forming manufacturing line for automotive parts had 68,000 batch records, 42 process variables and 11 quality metric categories included in the experiment. Across ten repeated group-stratified evaluations, XGBoost achieved a macro-F1 score of 0.892 with a 95% confidence interval of 0.888-0.896, compared with 0.838 for Random Forest, 0.856 for MLP, and 0.874 for TabNet. The increase over Random Forest was 0.054 in absolute terms and 6.4% in relative terms, and the paired bootstrap test confirmed that the difference was statistically significant at p<0.001.The causal constraint also improved the key variable identification consistency by 18.7%, Among 200 independently reviewed reports, the Agent's primary root-cause conclusion matched the engineer consensus in 169 cases, yielding an exact agreement rate of 84.5% and a Cohen's kappa of 0.781. The time taken to identify problems was also reduced from 47 minutes to 19 minutes. The study shows that output of causal reasoning and the LLM Agent can improve interpretability of the prediction of material quality and the impact of process interventions.

---

## uid: `doi:10.2139/ssrn.6956618`

- title: The Sovereignty Trap: National AI Strategies, Compute Nationalism, and the Fragmentation of the Global AI Supply Chain
- authors: Ali Sadhik Shaik
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6956618
- keyword hits: foundation model

### abstract

Nations are increasingly treating artificial intelligence capabilities as matters of sovereignty-triggering a global wave of national AI strategies that combine industrial policy, compute infrastructure investment, data governance rules, and talent retention mechanisms into comprehensive programs designed to ensure that no nation is dependent on foreign AI capabilities for its economic competitiveness, national security, or democratic governance. India's IndiaAI Mission invests in sovereign compute capacity and indigenous foundation models. The European Union's compute sovereignty proposals aim to reduce dependence on US cloud hyperscalers. Gulf states are constructing AI cities as geopolitical positioning instruments. And US export controls on advanced semiconductors are reshaping the global compute supply chain by restricting China's access to frontier AI hardware. This paper examines how this emergent 'compute nationalism' affects multinational enterprise AI strategy across three dimensions: infrastructure access and cost, talent flows, and market fragmentation. The paper introduces the Compute Sovereignty Impact Model (CSIM), which maps how sovereign AI initiatives create three enterprise-level disruption mechanisms: infrastructure bifurcation (separate compute stacks for different jurisdictions), talent pool fragmentation (national strategies competing for fixed global AI talent), and compliance multiplexing (maintaining parallel governance and deployment architectures per jurisdiction). Using evidence from India, the EU, the Gulf states, and the US-China technology decoupling, the paper demonstrates that the current trajectory leads to a fragmented global AI supply chain that increases enterprise infrastructure costs by an estimated 25-40%, reduces cross-border innovation velocity, and creates new forms of geopolitical risk. The paper proposes the Sovereign-Ready Enterprise Architecture (SREA)-a three-principle design framework for multinational AI systems that enables operation across sovereign compute environments while maintaining operational coherence. The paper concludes with implications for corporate geopolitical risk teams, government AI strategy advisors, and venture investors with cross-border AI portfolios.

---

## uid: `doi:10.2139/ssrn.7115525`

- title: The Reverse Information Paradox: When AI PlatformsRetain Too Much or Too Little Data
- authors: Vijaya Marisetty, Varsha Mamidi
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7115525
- keyword hits: generative ai

### abstract

Users must often reveal proprietary context to obtain useful generative AI output, while providersmay retain that context for future model improvement. We formalize this user-side analogue ofArrow’s information paradox. Retention discourages disclosure, yet retained data may generatesocial value. A two-wedge model shows that platforms under-retain when benefit appropriabilityis weaker than harm internalization and over-retain when the reverse holds. The ratio of thesewedges is a sufficient statistic for the sign and magnitude of the distortion. A single correctiveinstrument is a subsidy under under-retention and a tax under over-retention.

---

## uid: `doi:10.2139/ssrn.7095059`

- title: Decision-Aware Surplus Learning for Discrete Choice Modeling
- authors: Yingnan Yan, Yafeng Yin, Xi Lin
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7095059
- keyword hits: llm

### abstract

Discrete choice models in transportation are often estimated from available choice data and then used to support downstream design problems. This estimate-then-optimize workflow faces two limitations. First, available data may be sparse or weakly informative in the policyinduced utility regions where candidate designs are evaluated. Second, the analyst typically fixes the substitution geometry before calibration by selecting a probability architecture such as multinomial logit (MNL). This paper develops decision-aware surplus learning, a framework for estimating discrete choice models used in downstream decision making. The learned object is a structurally valid surplus-generated response map: its gradient gives counterfactual choice probabilities, and its curvature reflects local substitution patterns. The framework has two components. Surplus learning represents the surplus function as a convex combination of admissible atoms from a fixed dictionary, estimates utility parameters through a convex Fenchel-Young problem for fixed geometry, and selects surplus-geometry weights through an outer criterion. Decision-aware learning augments the estimator with pseudo-choice responses from behavioral query sources, such as targeted stated-preference surveys, behavioral simulators, or LLM-based pseudo-respondents, and weights these responses toward policy-induced utility regions where response errors are most consequential for downstream design. Conditional regret analysis clarifies how errors in the learned response map can translate into decision loss and why counterfactual coverage and query-source credibility are central. Controlled experiments show that surplus learning can improve recovery of non-MNL probabilities and local curvature, and that decisionaware pseudo-choice queries can improve downstream decisions when the policy-relevant region is weakly covered by available data.

---

## uid: `arxiv:2607.13314v2`

- title: Tabular Foundation Models for Discrete Choice Estimation
- authors: Liu Liu, Dan Zhang
- affiliations: not stated
- posted: 2026-07-14
- source: arXiv
- link: https://arxiv.org/abs/2607.13314v2
- keyword hits: fine-tuning, foundation model, in-context learning

### abstract

Tabular foundation models (TFMs) generate predictions on structured data via in-context learning, without task-specific estimation. We ask whether TFMs can be effectively applied to discrete choice, a central demand estimation framework in marketing and operations, and find that directly applying TFMs yields limited performance. The gap is structural: TFMs assume row-independent observations, whereas discrete choice is inherently set-valued and subject to persistent consumer preference heterogeneity. We propose a reformulation that encodes both choice-set dependence and individual heterogeneity within a row-based learning framework. Evaluated on a yogurt scanner panel, individual-level heterogeneity encoding is the dominant driver of predictive accuracy. The best reformulation outperforms hierarchical Bayesian estimation on both holdout log-likelihood and hit rate, running 16 times faster, a practical advantage for large-scale demand estimation. The advantage is largest in the medium-data regime (10--40 purchase occasions per consumer), where parametric Bayesian shrinkage most distorts estimates for atypical consumers. Fine-tuning on population choice data provides additional gains for consumers with shallow purchase histories, where in-context learning has limited individual-specific signal to condition on. These results establish a principled approach for applying foundation models to consumer choice problems more broadly.

---
