# Classification batch 419 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-419.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7140491`

- title: A Deep Reinforcement Learning Algorithm for the Vehicle Routing Problem with Stochastic Demands and Outsourcing
- authors: Mohsen Dastpak, Fausto Errico, Ola Jabali
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7140491
- keyword hits: fine-tuning

### abstract

We introduce the vehicle routing problem with stochastic demands and outsourcing options (VRP-SDO). In this problem, we consider a logistics service provider (LSP) that must partition a set of customer requests with uncertain demands into customers outsourced to a common carrier and customers committed to its own fleet. The former are exclusively served by the common carrier, whereas the LSP fully serves its committed customers with a fixed fleet. The latter induces a vehicle routing problem with stochastic demand (VRP-SD), which is solved dynamically while allowing multiple vehicle visits to a customer. Specifically, the demand of committed customers is revealed once visited. If the vehicle capacity is not sufficient to serve it, the residual demand may be served by other vehicles or by the same vehicle after having restocked at the depot. Moreover, vehicles are allowed to replenishment trips to the depot. Vehicles exceeding regular work-shift duration incur an overtime cost. The unit outsourcing cost is inversely correlated with the expected total demand of the outsourced customers. The VRP-SDO objective is to minimize expected total travel and overtime costs, as well as the outsourcing costs. We propose an iterative two-level solution methodology for the VRP-SDO. The first level partitions customers into committed and outsourced subsets, while the second level solves the resulting VRP-SD and estimates its expected routing cost. Solving this stochastic dynamic problem for a fixed set of committed customers is computationally demanding. Given that the VRP-SD must be evaluated repeatedly for different subsets of committed customers throughout the iterative search, solving it from scratch at every iteration is computationally impractical. Therefore, we propose learning an offline routing policy which estimates routing costs almost instantaneously for any subset of committed customers. We demonstrate our methodology using an iterated local search (ILS) algorithm that primarily establishes the first-level partitions. We formulate the second level problem as a Markov decision process and solve it using a deep Q-network (DQN). To represent the state of the system, we propose a graph attention network (GAT) that aggregates customer and vehicle information based on their relevance to the vehicle selecting an action, capturing the spatial structure induced by their relative locations. The DQN is trained offline on instances with variable customer cardinality and location, yielding a routing policy applicable to any daily realization of customers. We further introduce an online fine-tuning step that improves the accuracy of the routing cost approximation during the search. Extensive experiments show that our DQN for the VRP-SD reduces routing costs by 19.6\% relative to a state-of-the-art methodology, and by at least 29.6\% when compared to classical routing heuristics. Our overall solution algorithm for the VRP-SDO yields savings of 13.7\% on average relative to the version whose routing policy does not use the GAT representation. Furthermore, our method generates the high-quality decisions within minutes, whereas the benchmarks that do not use an offline-trained cost estimator require more than one hour on average.

---

## uid: `doi:10.2139/ssrn.6994880`

- title: Two-Rail Verification: A Public-Private Evidence-Separation Kernel for Institutional AI
- authors: Jun Gorai
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6994880
- keyword hits: ai agent

### abstract

AI agents and institutional automation increasingly require public accountability, while many operational records must remain private due to personal data, trade secrets, contractual terms, security constraints, or audit boundaries. This paper introduces Two-Rail Verification, a public-private evidence-separation kernel for institutional AI and AI-agent governance. The proposed kernel distinguishes between a Public Rail, where public claims, status, version, timestamps, hashes, and verification routes can be placed, and a Private Rail, where raw records, personal data, cost structures, contracts, internal logs, secrets, and unpublished evidence remain protected. The contribution is not a new cryptographic primitive, a certification scheme, or a production assurance claim. Rather, Two-Rail organizes existing concepts such as hashes, signatures, manifests, verification kits, verifiable credentials, selective disclosure, zero-knowledge proofs, transparency logs, audit trails, and assurance reports into an institutional evidence-separation discipline. The kernel is expressed through four minimal requirements: cross-rail write prohibition, verified public claims, a verifiable public surface, and an accountability interface. The paper discusses the public-private evidence problem, adjacent technical and governance concepts, minimal public-surface design, use cases for AI agents and institutional records, and limitations. It does not claim third-party verification, complete signature coverage, legal compliance, safety guarantees, or an effective royalty-free patent pledge. Related patent applications may be pending, but any future patent pledge or license should be published separately with an effective date and stable URL.

---

## uid: `doi:10.2139/ssrn.7129759`

- title: Bio-homeostasis Information Theory: A Resource Audit Framework for Statistical Pattern Maintenance in Dynamical Systems
- authors: Mingjun Li, Fangfang Zhang
- affiliations: not stated
- posted: 2026-07-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7129759
- keyword hits: ai agent

### abstract

Living systems and their artificial counterparts undergo significant state changes when subjected to interventions such as treatment, stimulation, training, or recovery. Despite divergent mechanisms across domains—from cellular perturbation and cancer therapy to neural interfaces and persistent AI agents—these systems share a common structural challenge: when bifurcations accumulate, what resources are required to maintain a declared statistical pattern within an acceptable neighborhood? To address this, we propose Biostasis Information Theory (BIT), a resource‑audit framework for statistical pattern maintenance under changing conditions. BIT defines system class, measurement family, feature library, bifurcation process, innovation source, distortion function, budget constraint, and bridging residual. Its core metric is the bifurcation information rate, derived from the rate‑distortion converse: if the effective correction budget falls below the rate required to keep innovation distortion within tolerance, maintaining the declared pattern becomes information‑theoretically impossible. BIT‘s contributions are fourfold. First, it unifies mechanistically disparate fields under a common resource‑constrained maintenance problem. Second, it introduces the bifurcation information rate as a computable necessary condition for feasibility. Third, it proposes the demand–budget–bridge triad, distinguishing BIT from homeostasis, control theory, and active inference. Finally, it systematically defines failure modes—budget insufficiency, feature‑library mismatch, noisy measurement, and bridging failure—and provides experimental guidelines and synthetic demonstrations. By making maintenance claims auditable, BIT offers a new theoretical foundation for resource management in dynamical systems across biology and artificial intelligence.

---

## uid: `doi:10.2139/ssrn.7145678`

- title: Simplifying Nature Away? Ex-Ante Evidence on the EFRAG ESRS Cuts from Three Years of European Nature Disclosures *
- authors: Chiara Colesanti Senni, Saeid Vaghefi, Maud Abdelli, Jochen Krimphoff, Markus Leippold
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7145678
- keyword hits: retrieval-augmented

### abstract

The European Commission adopted revised European Sustainability Reporting Standards (ESRS) on 3 July 2026, following EFRAG's December 2025 technical advice. Using the datapoint schedule in that technical advice, which reduces required datapoints, when material, by 61% overall and ESRS E4 biodiversity datapoints by 78%, we assess the nature-related disclosures of STOXX Europe 600 companies over FY2023-FY2025 (801 TNFD and 1,047 ESRS firm-year observations) with a retrieval-augmented generation pipeline that extends the ASKNATURE system. Three findings bear on the proposal. First, mandatory reporting delivers: ESRS disclosures carry a specificity premium of +0.13 on the unit scale (p < 0.01) and an enforceability premium of +0.16 (p < 0.01) over voluntary TNFD reporting, and ESRS E1+E2 evidence depth rises from 0.785 to 0.805 (FY2025 partial) with narrowing variance under the CSRD. Second, mandatory reporting has limits: it produces no commitment premium, the roughly 4:1 positive-to-negative sentiment skew in nature-impact reporting survives the mandate, and dual TNFD+ESRS reporters show no disclosure premium over single-framework reporters. Third, under proportional datapoint retention the simplification would erase 57% of observable ESRS evidence depth on average and 78% of E4 biodiversity evidence, collapsing the cross-sector differentiation on which institutional nature-risk screening relies. The improving climate-disclosure trend under the CSRD offers no assurance that biodiversity disclosure would survive the simplified regime. Preserving core quantitative E4 requirements, in particular the E4-5 KPIs and site-level granularity, is necessary to keep European nature reporting from reverting to the voluntary cheap-talk baseline we document.

---

## uid: `doi:10.2139/ssrn.7148593`

- title: From Urban Scaling Laws to Learnable Spatial Mechanisms: Universal Urban Downscaling with Meta-Learning Framework
- authors: Sunggyun Park, Dongwoo Lee, Sybil Derrible
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7148593
- keyword hits: fine-tuning

### abstract

This study proposes the Universal Urban Downscaling Model (UUDM), a novel meta-learning framework for hierarchical spatial disaggregation. Operating on the premise that universal spatial patterns governed by land use underpin all urban indicators, UUDM employs meta-learning to “learn to learn” these fundamental relationships from rich auxiliary geospatial data. This approach is particularly well-suited to the framework, as it enables rapid adaptation to new urban indicators with minimal data while extracting hierarchical spatial features that capture generalizable patterns underlying diverse urban phenomena. Extensive experiments on a large-scale dataset of 518 urban indicators validate our model. With comprehensive cross-validation, UUDM consistently outperforms specialized baselines, establishing state-of-the-art performance for general-purpose downscaling and proving the viability of a single, unified framework. More critically, the model exhibits remarkable zero-shot generalization. When trained on diverse domains, it accurately performs downscaling for tasks from completely unseen, highly dynamic population domains without any fine-tuning. This confirms that the model learns fundamental, transferable principles of urban spatial dynamics rather than task-specific patterns. UUDM, therefore, can provide a robust methodology for fine-grained urban analytics, enabling integrated policy simulations and reducing reliance on costly domain-specific data collection. Our work translates the idea of urban scaling laws by learning a transferable spatial scaling mechanism for intra-urban inference. Rather than estimating indicator-specific relationships, UUDM learns a transferable spatial scaling mechanism that governs how diverse urban phenomena are redistributed across spatial resolutions, offering a new paradigm for developing urban AI that is both generalizable and highly adaptable to different cities and unforeseen future challenges.

---

## uid: `doi:10.2139/ssrn.7009140`

- title: Gene Regulatory Network Inference in the Era of Biological Foundation Models Methods, Evidence, and Evaluation
- authors: Liu Chen
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7009140
- keyword hits: fine-tuning, foundation model

### abstract

Gene regulatory network (GRN) inference-the reconstruction of directed, mechanistic relationships between transcription factors and their target genes from observational and perturbational data-has been a central and stubbornly difficult problem in computational biology for two decades. The arrival of biological foundation models (BFMs): transformers pretrained by selfsupervision on hundreds of millions of single-cell transcriptomes or billions of nucleotides, has prompted a wave of claims that these models encode latent regulatory knowledge and can serve as general-purpose engines for network reconstruction. This review critically synthesizes the state of that intersection. We first formalize the GRN inference problem and review the lineage of classical methods-tree-based regression, information-theoretic measures, ordinary-differential-equation models, and the motif-aware SCENIC family-that remain strong baselines. We then survey the BFM landscape across genomic and single-cell modalities and catalog the principal strategies by which these models are repurposed for regulatory inference: attention-map extraction, embedding similarity, gene-program perturbation in silico, and supervised fine-tuning. Throughout, we foreground evaluation: the scarcity and bias of experimental ground truth, the fragility of benchmark rankings to seemingly innocuous protocol choices, and the recurring finding that zero-shot foundation-model performance frequently fails to dominate simple baselines. We connect these observations to emerging scaling-law evidence for masked-reconstruction transformers on transcriptomic data, which clarifies where additional pretraining compute does and does not help. We conclude that foundation models are best understood not as turnkey GRN oracles but as flexible priors whose regulatory signal is real but diffuse, and whose honest assessment demands multi-axis, perturbation-grounded benchmarking.

---

## uid: `arxiv:2607.18548v1`

- title: Engineering Trustworthy Agentic AI for Critical Systems
- authors: Omar Al-Refai, Ibrahim Shahbaz, Adam Ali Husseinat, Michael Mandulak, Jaewon Kim, Eman Hammad
- affiliations: not stated
- posted: 2026-07-20
- source: arXiv
- link: https://arxiv.org/abs/2607.18548v1
- keyword hits: agentic

### abstract

Agentic artificial intelligence systems, capable of autonomous perception, planning, tool use, and multi-step action, are increasingly proposed for critical engineering domains where decisions carry physical, operational, or economic consequences. This survey addresses a gap in current literature by treating trustworthiness, whether agentic behavior can be verified, audited, and trusted under the constraints that engineering practice actually requires, as a first-class engineering property, rather than evaluating agentic AI by task capability alone. The study adopts a trustworthiness model organized around five cross-cutting dimensions: safety and constraint satisfaction; robustness and reliability; transparency and interpretability; accountability and auditability; and privacy and security. This is mapped onto an agentic assurance workflow spanning perception through audit. Building on this foundation, agentic systems architectures, threats, concrete trust mechanisms, and quantitative metrics are surveyed for direct application in agentic systems development and evaluation. These principles are then examined across four constraint-bound engineering domains: power systems, autonomous vehicles/robotics/UAVs, high-performance computing, and communication networks, identifying recurring design patterns, shared failure modes, and domain-specific gaps. Synthesizing across those domains, agentic AI trustworthiness is shown to be a single problem, with a path outlined toward a reusable, cross-domain assurance framework analogous to the graded certification regimes used by mature safety-critical engineering fields.

---

## uid: `arxiv:2607.18102v2`

- title: FinSAgent: Corpus-Aligned Multi-Agent RAG Framework for Evidence-Grounded SEC Filing Question Answering
- authors: Jijun Chi, Zhenghan Tai, Hanwei Wu, Tung Sum Thomas Kwok, Hailin He, Zixing Liao, Bohuai Xiao, Chaolong Jiang
- affiliations: not stated
- posted: 2026-07-20
- source: arXiv
- link: https://arxiv.org/abs/2607.18102v2
- keyword hits: retrieval-augmented

### abstract

Financial question answering over U.S. Securities and Exchange Commission (SEC) filings requires retrieving and synthesizing heterogeneous evidence dispersed across long, standardized, and highly redundant disclosures. Existing retrieval-augmented and multi-agent systems typically derive retrieval queries directly from the user's question and rank candidates by semantic similarity. Together, these choices create prior-corpus misalignment: a mismatch between model priors and the target filings' structure, terminology, and evidence standards. As a result, query generation misses corpus-specific evidence, while semantic reranking favors topically similar but evidentially invalid false-positive chunks. We propose FinSAgent, an evidence-grounded multi-agent framework that reframes SEC filing QA as corpus-aligned retrieval planning and corrects both ends with a single principle: inject corpus-side conditioning wherever model priors would otherwise dominate. FinSAgent combines (1) role-specialized agents anchored to the mandated 10-K item structure, (2) database-aware query decomposition that conditions each agent's sub-queries on a lightweight, summary-level view of the local corpus, and (3) multi-path retrieval with a learned feature-gated reranker that separates evidential validity from semantic similarity. Across five offline financial QA benchmarks, FinSAgent improves retrieval coverage and answer correctness over strong single-agent and multi-agent baselines; in a three-arm randomized online experiment with 1,000 anonymous user ratings, it also receives higher scores than baselines.

---
