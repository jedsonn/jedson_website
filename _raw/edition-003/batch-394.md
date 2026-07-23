# Classification batch 394 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-394.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6904799`

- title: Diagnosing Source Confounds in Fake-News Benchmarks: Sufficiency, Mechanism, and Causation in the ISOT Case
- authors: Kelvin Afriyie Apenteng
- affiliations: not stated
- posted: 2026-06-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6904799
- keyword hits: transformer model

### abstract

Automated fake-news detection is widely benchmarked on the ISOT dataset (Ahmed, Traore and Saad, 2017), on which transformer models routinely report accuracies above 99%. This paper argues that such detectors largely learn to identify the source of an article rather than to assess the truth of its story. High accuracy is rather an artefact of how the dataset was constructed. Its real articles are drawn almost entirely from a single wire service (Reuters), while its fake articles come from a heterogeneous set of flagged websites. Through a sequence of experiments on the full 44,898-article corpus, the paper shows that the token "reuters" alone separates the two classes at a 66:1 ratio, and that a five-line rule keying on that single token achieves 99.20% accuracy with no training. This demonstrates that the source confound alone is sufficient to reproduce benchmark-topping accuracy. Again, a methodology-validated RoBERTa model reaches 100% under a clean three-way split in which the test set is evaluated only once, confirming the score is not an artefact of model selection. After removal of all the attribution markers, a RoBERTa model still records near-perfect accuracy (99.98%), indicating a confound that runs deeper than the surface token. A Logistic Regression classifier using only fifteen content-free stylometric features still separates the classes at 79.43% on the original corpus and 80.12% after marker removal. On the other hand, the same RoBERTa model transfers negatively to two out-of-distribution corpora (LIAR 43.29%, COVID-19 47.80%), scoring below their majority-class baselines. A final causal token-injection experiment shows that prepending the word "Reuters" to out-of-distribution articles inverts the model’s predictions. On the LIAR test set, prepending the token to every article moves accuracy from 43.29% to 56.84%, and prepending it only to genuinely fake articles drives accuracy down to 0.13%. A complementary re-evaluation on genuine non-Reuters news articles (AG News) shows the same effect in reverse. The RoBERTa model classifies almost two-thirds of authentic real articles as fake, and prepending the token "Reuters" raises recall on identical content from 0.35 to 1.00. The paper concludes that high accuracy on ISOT is not, by itself, evidence of misinformation-detection capability, and sets out the implications for benchmark construction and evaluation practice.

---

## uid: `doi:10.2139/ssrn.6898819`

- title: Will the Agentic AI Boom Become a Financial Crisis?
- authors: Anton Sokolov
- affiliations: not stated
- posted: 2026-06-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6898819
- keyword hits: agentic

### abstract

This article asks whether the current agentic-AI investment boom is more likely to end as a publicequity correction, an infrastructure-financing hangover, or a broader financial crisis. The analysis combines Perez's installation/deployment paradigm, Kondratieff long-wave vocabulary, boom-bust theory, historical comparators, public market concentration evidence, issuer filing denominators, official private-credit and financial-stability reports, AI adoption and productivity evidence, and public evidence on delegated-action controls. The central finding is conditional. AI appears technologically real and financially exuberant, and the financing edge of the buildout is becoming more credit-sensitive. Present public evidence supports a dotcom-like equity correction or telecom-like capex-credit hangover more strongly than a 2008-style systemic crisis. Four findings drive that conclusion. First, AI/data-center credit is no longer merely hypothetical: public ABS, delayed-draw term-loan, project-finance, and infrastructure-fund materials show a visible financing channel with both concentrated and diversified collateral pools. Second, realized loss and recovery evidence exists at the data-center/mining/HPC edge and protective loss-allocation terms are visible in utility and project-finance documents. Third, fund-by-fund exposure is dollar-valued in public schedules, while bank-by-bank evidence is strongest as public role mapping rather than retained loss exposure. Fourth, filing-grade revenue validation is material at hyperscaler, supplier, and selected neocloud layers, but capex payback is uneven and not proven across the full stack. The unresolved mechanism is the attestation bottleneck: high-value agentic-AI revenue remains less bankable where delegated action is not publicly shown to be attributable, authorized, provenance-bound, replayable, statusaware, and meaningfully reviewed. A transparent 500,000-run synthetic sensitivity lab is used only to rank evidence priorities; it is not a market-probability forecast.

---

## uid: `doi:10.2139/ssrn.6850202`

- title: Fairness Without Fault: Takings, Torts, and Climate Adaptation
- authors: Shannon Roesler
- affiliations: not stated
- posted: 2026-06-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6850202
- keyword hits: prompting

### abstract

This Article examines whether federal takings doctrine should impose constitutional liability on governments for property damage arising from infrastructure design and climate adaptation decisions. As climate disruption intensifies, state and local governments increasingly make choices that redistribute risk among property owners rather than eliminate it, prompting claims that government has taken private property by exposing it to flooding, erosion, wildfire, or other harms. Using Devillier v. Texas as a case study, I demonstrate how these claims reflect a growing conflation of tort and takings principles in federal law. This doctrinal confusion risks constitutionalizing ordinary infrastructure failures and land-use tradeoffs made under conditions of uncertainty. I therefore caution against proposals to recognize an affirmative governmental duty to protect private property under the Takings Clause and explain why negligence-based or duty-oriented approaches are ill suited to climate adaptation and inconsistent with both tort law and constitutional doctrine. Finally, I explore the broader consequences of expanding takings liability, including increased federal court oversight of local land-use decisions, diminished deference to state law, and the expansion of absolutist conceptions of property rights that may inhibit climate adaptation. I conclude by arguing for a clarified intent requirement to restore doctrinal limits and preserve governmental capacity to manage climate and disaster risks.

---

## uid: `doi:10.2139/ssrn.6923108`

- title: HybridRAG-Finance: Agent-Guided Information Summarization with Vector and Graph Retrieval for Financial Documents
- authors: Mazen  Wael Baioumy, Kostas Plataniotis, Yuri Lawryshyn
- affiliations: not stated
- posted: 2026-06-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6923108
- keyword hits: retrieval-augmented

### abstract

Financial institutions require document analysis systems that retrieve numerically precise, auditable answers from filings such as 10-K reports, yet existing Retrieval-Augmented Generation (RAG) architectures fall short of this requirement: vector-based retrieval struggles with hierarchical and relational reasoning, while graph-based retrieval falters on free-form semantic queries. This paper introduces HybridRAG-Finance, a framework whose central contribution is an iterative Summary Quality Control Agent that scores each generated summary along four dimensions (semantic similarity, completeness, factual accuracy, and specificity) and revises it until a quality threshold is met, before any information enters the retrieval stores. The validated summaries populate, in parallel, a ChromaDB vector store and a Neo4j knowledge graph organized by the GICS sector taxonomy, in which each node carries a confidence score produced by the agent, enabling reliability-filtered retrieval. Financially engineered prompts preserve numerical values, currencies, and time periods exactly throughout the pipeline. We evaluate the system on a benchmark of 60 questions formulated independently by financial analysts at a major institutional investment firm, with human-verified ground-truth answers, using the RAGAS evaluation framework. HybridRAG-Finance achieves 98% faithfulness and 97% context recall, outperforming VectorRAG and GraphRAG baselines on the metrics most critical for financial document analysis, while maintaining comparable retrieval latency.

---

## uid: `doi:10.2139/ssrn.6929718`

- title: Cross-chemistry battery state-of-health estimation from adaptive partial charging using interpretable physics-informed Efficient Kolmogorov-Arnold networks
- authors: Zekariyas  Yohannes Abebe, Yonghong Xu, Yidi Wei, Jian Li, Boru Jia
- affiliations: not stated
- posted: 2026-06-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6929718
- keyword hits: fine-tuning

### abstract

Accurate and robust state-of-health (SOH) estimation is essential for safe battery operation, second-life decision-making, and efficient battery management. Many existing methods rely on fixed feature-extraction windows, often unavailable in practice. High-performing data-driven models offer limited physical interpretability and generalize poorly across chemistries and operating conditions. To address these limitations, this study proposes a physics-informed efficient Kolmogorov-Arnold network (PI-EKAN) for SOH estimation from adaptive partial charging data. The framework employs prefix-specific Bayesian optimization (PS-BO) to select informative SOC windows and extract seven voltage-based descriptors from partial charging segments. These descriptors feed into coupled solution and dynamics networks trained via bounded uncertainty-weighted multi-objective optimization. Across eight datasets, PI-EKAN achieves an average MAPE of 0.58%, an RMSE of 0.63%, and an R² above 0.96. It exceeds 0.995 on four datasets and reduces average MAPE by 29.06% over the MLP-based PINN baseline. PS-BO adaptively identified chemistry-dependent SOC intervals that preserve degradation signals, remaining robust under restricted charging windows, low sampling frequency, and synthetic perturbations designed to emulate BMS SOC estimation errors. In cross-chemistry transfer, single-cell fine-tuning achieved 1.13% average MAPE across 16 transfer pairs, while hybrid EKAN-LoRA low-rank adaptation achieved comparable accuracy. PI-EKAN also maintained accuracy with only 20% of training cells available. Post-hoc feature attribution and PI-EKAN spline function analysis consistently identify voltage shape descriptors as leading contributors across most chemistries. Both methods broadly agree, suggesting PI-EKAN captures degradation-relevant patterns rather than dataset-specific artifacts. These results establish PI-EKAN as a practical, interpretable framework for SOH estimation from partial charging data with cross-chemistry transferability. The source code is available at https://github.com/zackjohan/IAW-PI-EKAN-for-SOH.git

---

## uid: `doi:10.2139/ssrn.6846561`

- title: FADP: A Sovereignty-Native HTTP Payment Protocol for Autonomous Agent Transactions
- authors: Abhijeeth Ganji, Priyanka Velpula
- affiliations: not stated
- posted: 2026-06-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6846561
- keyword hits: agentic

### abstract

We present FADP (the Fluid Agentic Payment Protocol), an HTTP-native twophase protocol for secure DeFi agent-to-agent transactions and agentic payments that couples on-chain transactions with cryptographic identity attestation in a single round-trip. Every FADP identity proof is unique per agent, unforgeable under standard cryptographic assumptions, and unreplayable by construction via four-dimensional nonce protection — making it the first HTTP payment protocol with formal guarantees on all three properties simultaneously. FADP extends RFC 7231's HTTP 402 status code [1] with three header namespaces — X-FADP-* for payment challenge and proof, XPauli-* for zero-knowledge identity binding [2], and X-FLDP-* for ECDSA request signing — yielding a wire format in which the server can verify who placed an order, that the request is fresh, and that the payment is on-chain final, all from headers alone. The protocol operates in a strict two-phase model: Phase α (initialization) provisions seven keys across three categories (local private, server public, internal proving), and Phase β (runtime) executes the 402 → onchain settlement → 200 cycle. Private keys never cross the network at any phase; the server holds only public material; the chain is the source of truth for payment finality. We prove four theorems — protocol correctness, liveness independence, replay impossibility, and identity-payment binding — and introduce three new metrics for HTTP-native payment protocols: Authentication Round-Trip Count (ART), Payment Atomicity Score (PAS), and Sovereignty Inheritance (SI). The reference implementation is deployed on Base Mainnet as a beta MVP prototype and submitted to the IETF as draft-fluid-fadp-01. Median end-to-end cycle latency is ~160–215 ms (analytical from measured components: 2 RTT plus on-chain confirmation), and per-call cost is approximately $0.001–$0.01 in stablecoin payment. To our knowledge, FADP is the first published HTTP payment protocol that (i) couples payment with cryptographic identity attestation in a single response, (ii) operates entirely within the existing RFC 7231 status-code framework with no L4 or L3 modifications, and (iii) inherits strict self-custody guarantees (Σ = 5) from a companion identity standard.

---

## uid: `doi:10.2139/ssrn.6879318`

- title: How AI Agent Deployment Structure Shapes Investor Evaluations: A Processing Fluency Perspective on One-Person Companies
- authors: Feiyu Wang, Guohou Shan, Ying Wu, Jingfeng Yin, Jibao Gu
- affiliations: not stated
- posted: 2026-06-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6879318
- keyword hits: ai agent

### abstract

The One-Person Company (OPC) is an emerging human-AI collaboration model referring to a venture in which a single founder coordinates an ensemble of specialized AI agents that perform all operational work. Despite growing real-world adoption, how structure design shapes the cognitive responses of external evaluators remains theoretically unexamined. Drawing on complex adaptive systems (CAS) and processing fluency theory (PFT), we propose that agent control mode (centralized vs. decentralized) and workflow pattern (sequential vs. parallel) in OPC differentially influence investors' processing fluency, which in turn drives investment intentions and investors' word-of-mouth. We further theorize that agent control mode and workflow pattern operate as cognitive substitutes rather than complements. We test our hypotheses in an online experiment with 274 investors. Results show that centralized control and sequential workflow each independently enhance processing fluency, which in turn improves investor evaluations. However, when both features are present at the same time, each one's marginal contribution to fluency is reduced. Our findings contribute to Information Systems research by extending human-AI interaction research from dyadic to one-to-many configurations, integrating CAS and PFT to explain external cognition of complex AI-driven organizations, and revealing a substitution dynamic in how conjunctive structural properties jointly shape evaluative outcomes.

---

## uid: `doi:10.2139/ssrn.6945731`

- title: The Socioeconomic Costs of Warming Cities: Extreme Heat and Corporate Monopsony Power in China
- authors: Junkang Zhang, Song Limin, Yao shiqi, Ping Chen
- affiliations: not stated
- posted: 2026-06-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6945731
- keyword hits: prompting

### abstract

While extreme climate events are known to disrupt urban economies, their hidden socioeconomic consequences on urban labor markets and income inequality remain insufficiently understood. Constructing a city-level extreme temperature metric and linking it to a comprehensive dataset of 170,004 firms from the China Tax Survey (2008–2016), we quantify the impact of urban heat exposure on local labor market dynamics. We find that city-level extreme heat shocks significantly strengthen firms’ monopsony power, increasing wage markdowns by approximately 4.6%. Mechanism analyses indicate that urban heat manifests primarily as a negative shock to labor productivity, prompting firms to accelerate capital-labor substitution and altering the local market environment, which collectively weaken workers’ bargaining position. Furthermore, we show that urban environmental governance and local government subsidies effectively mitigate these effects, whereas strict urban household registration (Hukou) restrictions exacerbate negative distributional outcomes by impeding labor mobility across cities. These findings highlight a hidden mechanism through which urban heat exacerbates socioeconomic inequality. Safeguarding vulnerable workforces in warming cities requires targeted urban policies, particularly easing migration barriers and enhancing workplace climate adaptation.

---
