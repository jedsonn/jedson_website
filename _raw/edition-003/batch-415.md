# Classification batch 415 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-415.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7118983`

- title: Improving the Generalization of UAV-Based Forest Biomass Estimation through Multimodal Fusion and Transfer Learning
- authors: YunHong Xie, Yifu Wang, Yifan Wang, Siyu Qiu, Yuhan Bai, Yujun Sun
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7118983
- keyword hits: fine-tuning

### abstract

Accurate estimation of forest aboveground biomass (AGB) is fundamental for assessing terrestrial carbon stocks and supporting climate change studies. However, under high-resolution UAV remote sensing conditions, pronounced canopy structural heterogeneity, spectral saturation, and substantial regional differences in forest types and site conditions often limit the transferability of data-driven models, making poor generalization a major bottleneck for large-scale AGB applications. To address this challenge, we propose a multimodal deep regression framework that integrates UAV-based RGB imagery and LiDAR point clouds with transfer learning to improve the generalization of forest biomass estimation across regions. The framework jointly exploits spectral–textural information from RGB imagery and three-dimensional structural information from LiDAR data through cross-modal feature fusion, enabling complementary representation of forest canopy properties. Furthermore, a selective transfer learning strategy is introduced to account for modality-specific feature stability by applying differentiated transfer and fine-tuning schemes to individual network branches, thereby mitigating domain shift effects between regions. Comprehensive experiments were conducted using the PureForest dataset in France as the source domain and two heterogeneous target regions in Fujian and Tibet, China. The results indicate that the multimodal fusion model significantly outperforms unimodal methods in the source region, achieving a maximum R2 of 0.924. Compared to machine learning regression, raster regression, and point cloud regression, the R2 values are improved by 0.088, 0.107, and 0.102, respectively. In cross-regional applications, introducing transfer learning further enhances model stability and prediction accuracy. Specifically, the multimodal model with transfer learning applied only to the point cloud branch achieves the highest R2 values of 0.811 and 0.899 in Fujian and Tibet regions, respectively, representing improvements of 0.047 and 0.023 over non-transferred models, demonstrating superior generalization performance. These findings indicate that multimodal fusion of structural and spectral information effectively alleviates modeling instability in high-resolution UAV-based AGB estimation, and that modality-aware selective transfer learning provides a promising pathway for improving cross-regional generalization, supporting scalable forest carbon monitoring and management.

---

## uid: `doi:10.2139/ssrn.7069098`

- title: From Wages to Watts: Energy as the Measure of Synthetic Labor in Two Emerging Economic Architectures
- authors: David Galipeau
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7069098
- keyword hits: ai agent

### abstract

Two independent proposals now argue that the unit in which economic value is measured is shifting from the wage to the watt. Brian Roemmele's JouleWork prices the output of autonomous AI agents in an energy-denominated wage unit and runs it, in a live "Zero-Human Company," as a continuous thermodynamic payroll. The framework presented in Citizen 5.0: A New Social Contract for Artificial Intelligence (Galipeau, 2027; hereafter Citizen 5.0) makes the joule a unit of public account and an ecological budget, taxes the surplus that synthetic labor captures when it displaces human work through a Synthetic Labor Tax, and governs compute through a Joule Standard and a Metabolic Ledger. This paper compares the two on four dimensions held separate from any value judgment: their mathematical formulations, their methodological approach, their results to date, and their prospects for realization. The comparison finds that the frameworks measure different objects, an agent's energy-weighted output as against a firm's displacement surplus; that they operate at different layers, a firminternal wage as against a societal account; and that they rest on opposite governance logics, bottom-up market selection as against top-down fiscal deliberation, while converging on a shared thermodynamic premise and a shared token mechanism. Neither is implemented at scale, both are explicitly illustrative, and each supplies what the other lacks. Beyond the comparison, the paper offers one constructive result, stated formally as a falsifiable proposition: a firm running JouleWork-style accounting makes the Citizen 5.0 tax base directly observable, reducing its central measurement problem from three unknowns per task to one, and so positioning JouleWork as a candidate micro-foundation for the Citizen 5.0 architecture rather than a rival to it. The independent convergence of a builder and an institutionalist on energy-denominated value is read here not as a settled result but as a signal that the field is at its beginning. The paper closes with a research agenda.

---

## uid: `doi:10.2139/ssrn.6961418`

- title: The Register Gap: A Meaning Intelligence Framework for Nigerian Public Discourse
- authors: Celestine Achi
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6961418
- keyword hits: gemini, prompting

### abstract

We introduce the Meaning Intelligence Framework (MIF™), a nine-dimension annotation and evaluation schema for Nigerian public discourse that separates surface sentiment from true communicative intent. Existing benchmarks for Nigerian languages, including NaijaSenti and AfriSenti, treat sentiment classification as a three-way polarity task (positive, negative, neutral). We argue that the dominant failure mode of AI systems on Nigerian discourse is not translation failure but context failure: the same utterance carries opposite pragmatic force depending on speaker, audience, and situation. The MIF operationalises this insight across nine scored dimensions: register, surface sentiment, true intent, irony, coded subtext, risk tier, annotator confidence, speaker emotion, and recommended communications action. We construct a 30-item calibration dataset spanning Standard English, Nigerian English, Nigerian Pidgin, and code-mixed registers, and evaluate a frontier language model (Gemini 2.5 Flash) under zero-shot and schema-informed prompting conditions. The headline finding is the Register Gap: zero-shot register classification accuracy is 33.3%, rising to 73.3% (+40 points) when the model receives the MIF schema in-context. The composite Meaning Intelligence Score increases by 5.4 points (73.2 to 78.6) under schema-informed prompting, with the largest practical gains in register identification, coded-subtext detection (+10 points), and strategic action recommendation (+10.3 points). We also identify a mobilisation blind spot: the model misclassifies a mobilisation signal disguised as humour as a routine warning in both conditions, demonstrating a failure mode with direct consequences for media monitoring and crisis communications. We release the framework specification, annotation guidelines, and the 30-item public calibration set to support reproducibility, while retaining a private holdout corpus for contamination-protected evaluation.

---

## uid: `doi:10.3386/w35431`

- title: Assessing the Benefits of Optimized Agentic AI Systems for Asset Pricing
- authors: Ralph S. Koijen, Bradford Levy
- affiliations: not stated
- posted: 2026-07-14
- source: NBER
- link: https://doi.org/10.3386/w35431
- keyword hits: agentic

### abstract

Evaluating optimized AI systems for asset pricing is fundamentally difficult for two reasons.First, models are trained on all data, implying that any backtest or analysis using historical data suffers from look-ahead bias.In addition, markets are reflexive -as investors adopt AI, prices adjustwhich may erode the very patterns the AI system was trained to exploit.We introduce a real-time, out-of-sample benchmark designed to sidestep both problems.The benchmark measures how well AI systems can explain contemporaneous stock returns around earnings announcements using only information available at announcement time, including the text of the announcement itself.Applying this benchmark to a range of agentic AI systems -which extract structured signals from earnings call transcripts and optimize over those signals -we find that the best-optimized systems more than double the explained variation in returns relative to standard benchmarks (R2 increasing from 8% to close to 20%).We show that AI-based optimization can deliver efficiency gains relative to traditional machine learning methods while also improving interpretability as our approach produces human-readable economic mechanisms that explain price movements.These learned rules can be compared to the drivers of realized returns in existing asset pricing models to identify missing sources of variation in a data-driven, self-evolving way that integrates empirical learning with economic structure.We release an SDK for researchers to improve on our results.Saturating this benchmark would represent fundamental progress in understanding how capital markets process firm-level information.

---

## uid: `arxiv:2607.12248v2`

- title: When Directional Accuracy Lies: A Base-Rate-Honest Benchmark for LoRA-Adapted TimesFM on Equity Forecasting
- authors: Taizhen Cheung
- affiliations: not stated
- posted: 2026-07-14
- source: arXiv
- link: https://arxiv.org/abs/2607.12248v2
- keyword hits: fine-tuning

### abstract

Large pretrained time-series models such as TimesFM are attractive for financial forecasting, but raw directional accuracy is a misleading scoreboard in equity markets. An early LoRA adapter in this project appeared to reach roughly 80% directional accuracy; we show this is not evidence of skill. Over a long horizon in a rising market, a trivial "always-up" rule attains comparably high accuracy without using the input at all. To separate genuine skill from this base-rate artifact, we build a reproducible, frozen-data benchmark with expanding walk-forward folds, a stratified held-out-ticker split, honest baselines (zero-shot TimesFM, always-up, random-walk, persistence, AR(1)), and paired significance tests (McNemar, Diebold-Mariano) under Benjamini-Hochberg FDR control. We apply the identical method to two universes -- a tech-heavy NASDAQ-100 and a broad S&P 500 -- reporting excess accuracy over the always-up base rate. Three findings replicate. First, when the historical ~80% condition is recreated, the high number is a base rate of ~0.70 that the fine-tuned model scores below. Second, pooled LoRA shows no directional skill over the base rate at any horizon on either universe (negative at the six-month horizon). Third, per-sector specialization is significantly worse than a single pooled adapter (Diebold-Mariano p<0.001 on held-out stocks at h=128). Fine-tuning's only measurable benefit is a statistically significant reduction in point-forecast error relative to zero-shot TimesFM, which nonetheless does not beat naive baselines and confers no tradeable directional edge. The contribution is methodological: a defensible, fully seeded protocol that prevents the base-rate trap, together with the replicated negative result it produces.

---

## uid: `arxiv:2607.13311v1`

- title: Finding the Right Tables and Columns: A Benchmark and Corpus-Adaptive Embeddings for SQL Schema Retrieval
- authors: Qingcheng Zeng, Puxuan Yu, Aman Mehta, Fuheng Zhao, Rajhans Samdani
- affiliations: not stated
- posted: 2026-07-14
- source: arXiv
- link: https://arxiv.org/abs/2607.13311v1
- keyword hits: fine-tuning

### abstract

Retrieval in the SQL setting has largely been studied as the task of finding, within a large collection of SQL statements, the statement that answers a natural-language question. At scale, however, a more fundamental retrieval problem precedes generation: schema retrieval, identifying the tables and columns a question requires in a database that may contain thousands of them, far more than fit in a model's context. We argue that this step warrants first-class evaluation. To this end, we recast five text-to-SQL datasets (Spider, BIRD, BEAVER, and two LiveSQLBench variants) as retrieval tasks at both table and column granularity, covering realistic and enterprise-scale schemas under two document representations, and we show that off-the-shelf text and code embedders transfer poorly to this setting. We then propose corpus-adaptive fine-tuning: natural-language queries are synthesized directly from the target schema corpus, granularity-aware hard negatives are mined, and a 305M-parameter embedder is fine-tuned contrastively. This procedure raises average recall@10 from 60.4 to 75.6 (nDCG@10 from 51.9 to 68.0), making the 305M model the strongest retriever under one billion parameters and competitive with state-of-the-art embedders of 4-8B parameters, more than an order of magnitude larger. The same recipe improves an 8B state-of-the-art embedder from 77.8 to 78.4 recall@10, matching the best result on the benchmark and indicating that the adaptation is backbone-agnostic. Leave-one-corpus-out experiments and a leakage audit show that these gains reflect a transferable schema-retrieval ability rather than memorization of the evaluation data. Our results establish schema linking as a standalone retrieval task and lightweight, label-free corpus adaptation as a practical route to deploying it at enterprise scale.

---

## uid: `doi:10.2139/ssrn.6967238`

- title: A Socioeconomic Analysis of AI Agents and the Restructuring of the Knowledge Labor Market
- authors: Ignacio Kramcsak
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6967238
- keyword hits: ai agent

### abstract

The widespread deployment of autonomous Artificial Intelligence (AI) agents is fundamentally reshaping the socioeconomic structure of knowledge-based industries. This paper examines the impact of these technologies on labor market dynamics, specifically focusing on the generational tension between senior and junior professionals. Utilizing a mixed-methods research design that combines macroeconomic technology adoption data with a qualitative analysis of vanguard industry case studies, we analyze how the automation of complex cognitive workflows alters the traditional talent pipeline. The findings reveal the emergence of "Synthetic Seniority": junior workers experience an immediate amplification of their operational output but lack the critical judgment required to audit subtle algorithmic failures. Concurrently, senior professionals who fail to adapt to the governance of multi-agent systems face accelerated obsolescence due to the economic non-viability of manual execution timelines. We conclude that AI agents do not generate a linear path toward technological unemployment; instead, they trigger a structural fragmentation of the labor market, shifting economic value away from technical execution and toward strategic human judgment and risk management. This shift underscores an urgent need to reconfigure corporate training frameworks and school-to-work transition models.

---

## uid: `doi:10.2139/ssrn.6968279`

- title: Closing the AI Proof Gap: An Evidence Architecture for Operationalizing NIST AI RMF, ISO/IEC 42001, and EU AI Act Requirements Across Board Governance, Regulatory Disclosure, and D&O Underwriting
- authors: Rohan Sharma
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6968279
- keyword hits: agentic

### abstract

This paper identifies and defines the AI Proof Gap: the institutional distance between high-level AI governance commitments and the documentary evidence that boards, D&O underwriters, regulators, and external assessors require in order to verify that AI risks are being governed in practice. Despite the proliferation of governance frameworks-including the NIST AI Risk Management Framework, ISO/IEC 42001, the EU AI Act's documentation requirements, and sector-specific crosswalk resources-few organizations have developed a coherent operational model for translating standards obligations into reusable evidence artifacts. This paper makes four contributions. First, it defines the AI Proof Gap as an analytic category distinct from, but related to, prior work on AI accountability, algorithmic auditing, and ethics washing. Second, it presents the Unified AI Evidence Framework (UAEF), a five-layer architecture that maps standards and profiles, internal ownership structures, documentary evidence requirements, audience-specific disclosure interfaces, and the special governance demands of agentic AI systems. Third, it demonstrates that boards, insurers, regulators, and conformity bodies often require structurally overlapping forms of the same underlying evidence, and that organizations treating these demands as unrelated produce governance theater rather than governance substance. Fourth, it outlines how the UAEF can be operationalized through a practitioner instrument or software-assisted evidence system. The central claim of the paper is both theoretical and practical: closing the AI Proof Gap requires moving the AI governance field downstream from standards interpretation to evidence design.

---
