# Classification batch 23 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-23.answer.json` as a JSON array.

---

## uid: `arxiv:2608.18058v1`

- title: Delegation Asymmetry in Agentic Recommender Systems: Measuring Two-Sided Receptivity in Online Dating
- authors: Daria Leshchikova, Valentina V. Kuskova, Dmitry Zaytsev, Valerii Klimov
- affiliations: not stated
- posted: 2026-08-18
- source: arXiv
- link: https://arxiv.org/abs/2608.18058v1
- keyword hits: agentic, llm

### abstract

Autonomous LLM agents that converse on a user's behalf are an emerging design pattern in matching platforms, yet their viability depends on a condition rarely examined: users must accept not only delegating conversation to an agent, but also receiving agent-mediated communication from others. We study this condition using two large-scale surveys of active users of a major dating platform (N=2,894 on generative profile features; N=2,617 on autonomous conversational agents, fielded in two languages). We develop a latent-variable measurement model of agent receptivity based on graded response models with latent regression, and show via model comparison that willingness to send and willingness to receive agent communication are distinct constructs: highly correlated (rho=0.92) but separable (Delta BIC=52), with partial measurement invariance across languages. The model quantifies a systematic delegation asymmetry: deploying one's own agent requires far lower receptivity (threshold -0.38) than engaging a counterpart's agent (+0.32; full engagement +1.39), and mean deployment propensity exceeds engagement propensity roughly threefold. Under a random-pairing counterfactual derived from stated receptivity, only 4-13% of directed dyads combine agent deployment with receiver engagement, with a pronounced gender-directional imbalance. Design counterfactuals quantify the levers: a reciprocity requirement cuts interaction volume by half or more by excluding nearly two-thirds of would-be deployment, while routing agent contacts on receive receptivity triples per-contact engagement, a lift that survives out-of-sample validation with the target item held out (AUC 0.88, 3.1x quartile lift under respondent-level cross-validation). We discuss implications for agentic recommender design, including disclosure, opt-in mechanics, and receptivity-aware matchmaking.

---

## uid: `doi:10.2139/ssrn.7301980`

- title: Agentic Workflow Drift in Life Sciences: Extending the Reasoning-Layer Risk Taxonomy to GxP-Regulated Pharmaceutical and Biotechnology Operations
- authors: Maureen Doyle-Spare
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7301980
- keyword hits: agentic, large language model

### abstract

Agentic AI is beginning to support regulated activities across pharmaceutical manufacturing, biotechnology, pharmacovigilance, clinical development, and regulatory affairs through emerging copilots, autonomous workflow orchestration, and AI-assisted quality operations. In these settings, consequential determinations turn on the operational meaning of regulated terms, whether a deviation is critical, whether an adverse event is serious, whether a batch may be released, whether a subject is eligible. These deployments change where regulated operational decisions are formed. Rather than executing predetermined logic alone, autonomous agents increasingly reconcile multiple validated sources to determine what a regulated term means at runtime, and act on the resolved interpretation without a qualified reviewer resolving it first. Every checkpoint clears, every system performs as designed, and the organization is still wrong. This shift introduces a distinct governance exposure. Agentic Workflow Drift is the mechanism by which agentic systems satisfy mandatory validation checkpoints while executing under an unauthorized operational interpretation, producing outcomes that are procedurally compliant and substantively wrong. The analysis distinguishes the reasoning layer within the GxP control environment, demonstrates that computer system validation, 21 CFR Part 11 controls, data integrity programs, and quality management system review each govern an artifact that exists before or after the moment of interpretation, and shows that none governs the interpretation itself as a distinct object. The same reasoning surface also permits deliberate manipulation. That deliberate form is Agentic Workflow Subversion, treated here as a distinct and serious exposure, because in medical research and manufacturing the deliberate steering of an agent's resolved interpretation can influence batch release, safety reporting, and trial eligibility, and through them patient safety and product quality. The concepts translate naturally into established GxP practice, mapping the Reasoning Baseline, the Semantic Deviation Index, and the Deterministic Gate onto established GxP concepts such as predetermined acceptance criteria, review by exception, and quality-controlled definitions, rather than replacing the validation disciplines already familiar to regulated organizations. In the preparation of this manuscript, a large language model assistant supported structural editing and consistency checking of terminology and references against the author's prior working papers. The author reviewed and edited all content and remains fully responsible for the manuscript.

---

## uid: `doi:10.2139/ssrn.7307798`

- title: Beyond Statistical Approximation: Mediating the Cognitive Gaps in Non-Agentic Architectures
- authors: Bhavya Shahi
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7307798
- keyword hits: agentic, large language model, large language models

### abstract

Contemporary large language models rely fundamentally upon autoregressive Transformer architectures that optimize conditional probability distributions over vast text corpora. While these models display remarkable surface fluency across diverse text generation tasks, a foundational disparity exists between statistical token prediction and epistemological grounding. Unmediated single-pass forward execution leaves non-agentic architectures inherently vulnerable to hallucination dynamics, epistemic drift, and compounding structural errors across extended context windows. Building upon the foundational framework established by Dr. Aris Thorne and Prof. Elena Vance, this study examines the structural constraints of statistical approximation and formalizes the mathematical mechanics of error propagation in unassisted autoregressive generation. The investigation explores how the absence of intrinsic world models and dynamic error-correction subroutines limits single-pass models during multi-stage analytical tasks. To resolve these operational boundaries, a recursive verification framework is evaluated, illustrating how closed-loop feedback, state monitoring, and multi-layered verification mechanisms systematically mediate identified cognitive gaps. Mathematical modeling demonstrates that while single-pass feedforward systems suffer from exponential decay in logical fidelity as sequence length and step complexity expand, the integration of agentic verification loops attenuates step-wise error probabilities. This error reduction stabilizes systemic outputs and preserves structural cohesion across complex analytical trajectories, indicating that architectural evolution from static feedforward generation to dynamic agentic mediation is essential for epistemologically grounded computational intelligence.

---

## uid: `doi:10.2139/ssrn.7321286`

- title: OFRA: Outcome-Aware and Test-Time Oracle-Free Risk-Aware Answer Gating for Poisoned Retrieval-Augmented Generation
- authors: Wei She, Zikai Dong, Yongkang Yang, Zhao Tian, Wei Liu, Defeng Kong
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7321286
- keyword hits: deepseek, retrieval-augmented

### abstract

Poisoned retrieval-augmented generation (RAG) is commonly assessed with aggregate attack success rate (ASR), but a lower ASR does not reveal whether a targeted failure becomes correct, abstain-like, or another error. We present OFRA, an outcome-aware intelligent decision framework for test-time oracle-free answer gating. OFRA partitions generated outputs into four mutually exclusive, protocol-defined states---targeted incorrect, guarded-correct, abstain-like, and untargeted incorrect---and analyzes paired transitions among them. It then formulates post-generation control as a selective-answering problem over heterogeneous candidate paths. The gate is trained and selected offline, while its deployed interface uses only observable answer-status, agreement, routing, output-length, and evidence-processing signals; gold answers, attacker targets, correctness labels, and adversarial-source annotations are excluded at test time.On a held-out Natural Questions protocol with DeepSeek-V4-Flash, the lightweight OFRA-RF instantiation achieves $4.17\%$ attacked ASR at $36.25\%$ coverage and $11.49\%$ conditional ASR. On benign inputs, it reaches $53.75\%$ coverage with a $0.42\%$ wrong-target rate. Agreement-only remains a strong comparator at $5.00\%$ ASR and $46.67\%$ coverage, and its paired ASR difference from OFRA-RF is not statistically significant. Transition accounting shows that most removed targeted failures become abstain-like rather than directly corrected, so OFRA-RF is best interpreted as selective risk control. Supporting evaluations across datasets, generators, attacks, poisoning densities, semantic rerankers, graph-side paths, and response-verification interfaces reinforce that relevance and coverage alone do not determine poisoning safety. OFRA therefore provides an intelligent risk--coverage decision protocol rather than a universally dominant classifier, and its learned gate remains candidate-pool specific.

---

## uid: `doi:10.2139/ssrn.7323044`

- title: An Integrated Web-based Decision Support System with LLM-assisted Mitigation for Carbon Footprint Management in Marine Aquaculture
- authors: Xiaomin Wang, Yulong Wang, Changkun Lin, Ting Jiang, Chenxin Zhang, Ziyi Cong, Hanxue Li, Xuhan Wei
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7323044
- keyword hits: llm, retrieval-augmented

### abstract

Effective carbon-footprint management in marine aquaculture requires integrated assessment and evidence-based mitigation. We developed a web-based decision support system with three interconnected innovations: (i) automated, traceable life cycle inventory construction via guided questionnaires; (ii) spatially explicit carbon-footprint assessment coupling technosphere emissions with species-specific natural carbon processes and regional environmental parameters; and (iii) LLM-assisted, human-reviewed mitigation support using retrieval-augmented generation to translate sensitivity-ranked inputs into evidence-linked, user-reviewable candidate measures. An oyster-farming case study demonstrates the end-to-end workflow from data collection through assessment, interpretation, and scenario recalculation. By making the assessment chain traceable and interpretable, this platform provides a foundation to inform cleaner production, green procurement, policy analysis for industrial restructuring, and product carbon-footprint verification for marine aquaculture industry. The modelling framework is transferable to credible, data-informed carbon management for other food production systems.

---

## uid: `doi:10.2139/ssrn.7323498`

- title: Uncertainty Quantification for Financial Foundation Models: A Survey
- authors: Zijie Zhao, Mingjun Sun, Shenbo Xu
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7323498
- keyword hits: agentic, foundation model

### abstract

Financial foundation models increasingly support workflows spanning financial question answering, disclosure analysis, forecasting, and decision-making. In these settings, uncertainty may concern whether evidence is valid and available at the relevant time, whether an interpretation is justified, which outcomes remain plausible, or which action is preferred under costs and risk constraints. Because these objects arise at different points in a workflow, uncertainty cannot be reduced to confidence in a final output. We introduce a source-aware framework that distinguishes six sources of uncertainty across evidence and context, model and inference, and outcome and action, while treating agentic workflows as the execution layer through which uncertainty can propagate, change form, or be reduced. We develop a mechanism-based taxonomy grounded in how methods construct or verify uncertainty and reliability representations, and use it to assess their applicability across financial task domains. We further map finance-specific empirical studies across the taxonomy and task domains to characterize the current research landscape. The analysis reveals a literature that remains largely compartmentalized by task, with limited work connecting evidence and reasoning reliability to downstream prediction and constrained action. By connecting where uncertainty arises, how it is represented, and how it bears on downstream decisions, this survey provides a unified foundation for studying and evaluating uncertainty in financial foundation models.

---

## uid: `doi:10.2139/ssrn.7329421`

- title: InvoiceOCR-Synth: An annotation-noise-free synthetic dataset of receipt and invoice images for document information extraction
- authors: Alamgir Munir Qazi, Jamal Abdul Nasir, Pratheesh Chambeth, Waqar  Shahid Qureshi
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7329421
- keyword hits: fine-tuning, large language model

### abstract

Publicly available invoice data is scarce: real financial documents carry commercially sensitive and personally identifying information that prevents redistribution, and the few public corpora are human-annotated. This article presents a synthetic corpus of receipt and invoice images for evaluating document information extraction systems, including Vision Language Models (VLMs) and OCR pipelines. The data were produced with a generate-then-render pipeline that inverts the conventional annotation workflow: structured JSON records are sampled first, and images are rendered from those records afterwards. A local open-source large language model (openai/gpt-oss-20b) generated 1,000 fictional records conforming to a 32-field schema covering supplier and customer identity, reference numbers, dates, currency, line items, structured tax breakdowns, and monetary totals, spanning five currencies and fifteen document types. Arithmetic relationships between quantities, unit prices, line amounts, tax bases, tax values, and totals were enforced at generation time; a post-hoc audit identified 62 records whose tax summaries were inconsistent with their own line items were excluded rather than repaired, so that every released label matches its rendered image exactly. Each of the 938 retained records was rendered through one of six Jinja2 HTML/CSS templates with randomised fonts and colour schemes and rasterised to PNG at 150 DPI, then degraded under three image-quality conditions using the Augraphy library: clean, faded, and bad scan. Because all three image-quality conditions use the same ground-truth annotations, the dataset contains 2,814 images with consistent labels. This makes it suitable for evaluating model robustness, benchmarking document information extraction systems and fine-tuning.

---

## uid: `doi:10.2139/ssrn.7291581`

- title: Generative AI‐aided Data Acquisition and Parameter Learning Framework for Complex Vehicle Automation and Traffic Control Systems
- authors: Mukundhan Narasimhan, Lili Du
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7291581
- keyword hits: generative ai, generative artificial intelligence

### abstract

Vehicle automation and traffic control systems often rely on parameters that must adapt to changing traffic conditions to achieve optimal performance. However, these parameters are typically difficult to formulate analytically; optimization‐based selection is computationally expensive, and data‐driven learning‐based calibration requires large quantities of representative state–parameter training data that are often unavailable. To address this challenge, this study proposes a novel Generative AI‐aided Data Acquisition and Parameter Learning framework (GenPL). The GenPL organically integrates reinforcement learning‐guided data acquisition, retrospective optimization, generative artificial intelligence, and neural network learning into a unified methodology for adaptive parameter estimation. Specifically, an RL‐aided Data Acquisition (RL‐DAQ) module generates a high‐quality simulation dataset consisting of state–optimal parameter pairs. Meanwhile, an AI‐aided Data Generation (AI‐GEN) module employs a novel Optimal Transport Tabular Variational Autoencoder (OTTVAE) to augment this simulation dataset by generating synthetic samples that preserve multidimensional state–parameter relationships. The resulting simulation and synthetic datasets are then used to train a neural network for real‐time parameter prediction. The framework is demonstrated through adaptive weight estimation for the Complex‐SMD controller embedded within the Sequential Truck Platoon Formation (StPF) protocol (Narasimhan et al., 2026). Using a full‐factorial benchmark design, the study first directly evaluates dataset quality in terms of data quality, learning utility, and operational utility. The results show that OTTVAE substantially improves the representativeness of the training dataset relative to conventional tabular generative models. Operational evaluations conducted on a realistic freeway testbed further demonstrate that StPF equipped with GenPL‐learned adaptive weights consistently outperforms both static weight configurations and neural networks trained solely on simulation data, yielding greater and more robust travel time reductions across a wide range of traffic conditions. The findings suggest that adaptive parameter learning can be effectively reformulated as a data acquisition, augmentation, and learning problem, providing a general framework for transportation control systems facing data scarcity and computationally expensive online optimization.

---
