# Classification batch 208 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-208.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6886558`

- title: Economic Narrative Indices and Media-Based Sentiment Measures: A Systematic Review of Methodologies, Applications, and Research Gaps (2007-2025)
- authors: Ann Naser Nabil
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6886558
- keyword hits: large language model, large language models, transformer model

### abstract

This systematic review synthesizes evidence from 46 empirical studies (2007-2025) that extract sentiment from textual data for economic forecasting, supplemented by 20 theoretical papers developing macroeconomic models of sentiment. We conduct a comprehensive quantitative synthesis establishing that sentiment-based models improve forecast accuracy by 12-20% (median RMSE reduction), with the precise estimate depending on baseline strength: studies using strong benchmarks (professional forecasts, ARIMA) report ∼12-15%, while those using weak baselines (AR(1)) report larger but less realistic gains. The unconditional median across all studies is 20%, but this pools comparisons against baselines of markedly different strength: approximately 35% of reviewed studies compare against AR(1) or nearunconditional benchmarks, while only ∼25% compare against professional forecasts (SPF, Blue Chip). Well-documented publication bias toward positive forecasting results further tempers the headline figure. We document clear methodological evolution from dictionary-based approaches (55% of studies) through traditional ML and transformer models to emerging Large Language Models (3%), characterize validation practices (83% employ out-of-sample testing, but only 33% follow real-time data protocols), and assess methodological quality via structured riskof-bias scoring. Critical geographic and linguistic gaps persist: 56% of studies focus on the US, 84% analyze English text, and zero sentiment indices exist for Africa, Latin America, or Bangla-speaking regions (265 million speakers). We develop a best-practices framework for sentiment forecasting validation and propose expansion strategies, using the Bangla Economic Narrative Index (BENI) as a case study for bridging geographic gaps.

---

## uid: `arxiv:2606.28520v1`

- title: Detecting Clinical Hallucinations in LVLMs via Counterfactual Visual Grounding Uncertainty
- authors: Xiao Song, Haonan Qin, Zhaoxu Zhang, Jiong Zhang, Yuqi Fang, Caifeng Shan
- affiliations: not stated
- posted: 2026-06-26
- source: arXiv
- link: https://arxiv.org/abs/2606.28520v1
- keyword hits: agentic, qwen

### abstract

Large vision-language models (LVLMs) are increasingly used for clinical image understanding, yet they remain vulnerable to \emph{hallucinations}--producing textual findings or attributes not supported by the image. We present a vision-traceable hallucination detection framework that audits arbitrary LVLM responses via visual evidence grounding, requiring neither modification nor internal access to the hidden states of LVLMs. Given an LVLM response, we extract visually verifiable entities and use a medical-domain-adapted Qwen-VL grounding verifier to localize each entity on the input image. To enhance the robustness of our detection method, we introduce a counterfactual entity perturbation method and estimate visual evidence uncertainty by contrasting factual and counterfactual grounding results. Specifically, we compute an entity-level uncertainty score from the positive confidence, counterfactual confidence, and their grounding overlap for binary hallucination decision-making. Experiments on multiple medical imaging modalities and LVLM backbones demonstrate that our method consistently improves hallucination detection performance over recent baselines, while providing interpretable localization evidence and strong cross-model transferability. Code and dataset are available at https://github.com/Agentic-CliniAI/CounterVHD.

---

## uid: `arxiv:2606.28479v1`

- title: Decomposing Memorization Reduction in Privacy-Preserving Fine-Tuning of SLMs for CSIRTs
- authors: Cristhian Kapelinski, Diego Kreutz
- affiliations: not stated
- posted: 2026-06-26
- source: arXiv
- link: https://arxiv.org/abs/2606.28479v1
- keyword hits: fine tuning, fine-tuning, prompting

### abstract

CSIRTs increasingly fine tune language models on vulnerability scan records, but these records expose internal network topology and create privacy risks under regulations such as GDPR and LGPD. We present the first empirical study of how DP SGD and HMAC pseudonymization interact when fine tuning small language models with 1B to 3B parameters on structured CSIRT data. We evaluate 96 LoRA adapters across four SLMs and four training regimes, including raw fine tuning, QLoRA with large batch training, and DP SGD with epsilon equal to 2 and 8. We also audit memorization using 20 planted canaries, four extraction attacks, and a dual attack targeting HMAC pseudonymized identifiers. Our results show three main findings. First, matched update controls reproduce the observed reduction in memorization by reducing the number of optimizer updates alone, accounting for 66 percent to 132 percent of the measured effect, with a mean of 100 percent across three seeds and four models. In this setting, DP SGD provides the formal privacy guarantee but does not produce additional measurable reductions in memorization. Second, HMAC pseudonymization removes the original identifiers from the exposure surface, reducing exposure by 40 percent to 61 percent, while pseudonymized identifiers remain close to the expected random baseline and do not become a secondary memorization target. Third, F1 scores remain between 0.19 and 0.28 across all 96 adapters using four shot prompting, indicating that, under the evaluated training budget, 1B to 3B SLMs do not achieve operationally useful performance.

---

## uid: `arxiv:2606.27936v1`

- title: Agentic AI-Powered Re-Identification: An Emerging, Scalable Threat to Mobility Microdata Privacy
- authors: Oscar Thees, Roman Müller, Matthias Templ
- affiliations: not stated
- posted: 2026-06-26
- source: arXiv
- link: https://arxiv.org/abs/2606.27936v1
- keyword hits: agentic, large language model

### abstract

The widespread collection of fine-grained location data by commercial data brokers creates a re-identification risk that is not widely recognised by the public. While prior research has established that mobility traces are highly unique and that individuals can, in principle, be identified from a handful of spatio-temporal points, such attacks have historically required significant manual effort from skilled analysts, limiting their practical scale. In this feasibility study, we demonstrate in a real world setting that agentic AI fundamentally changes this threat model. We present an end-to-end pipeline in which large language model agents autonomously search the open web, cross-reference public records and social media, and resolve raw coordinate sequences to candidate identities - without human intervention. We evaluate the pipeline on a spatio-temporal dataset containing simulated location points anchored at and around true home and work addresses, focusing on a high-risk disclosure scenario. Our results demonstrate that, from spatio-temporal data and public sources alone, our agentic AI successfully re-identified 18 of the 25 re-identifiable individuals (72%) and 18 of 43 cases overall (41.9%). We discuss implications for Statistical Disclosure Control (SDC) practice and outline the near-future escalation that data custodians and regulators must anticipate. De facto anonymity - an implicit foundation of SDC practice - is shifting. Agentic AI strengthens the case that re-identification is reasonably likely by any means under the GDPR Recital-26 standard, at costs of minutes-and-dollars per target.

---

## uid: `doi:10.2139/ssrn.7005639`

- title: From Citizen Queries to Expert Review: Evaluating a Retrieval-Augmented Municipal Legal Assistant
- authors: Juan Barrera Valdés, Miriam Zulma Sanchez Hernández
- affiliations: not stated
- posted: 2026-06-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7005639
- keyword hits: llama, llm, retrieval-augmented

### abstract

Citizens who need to understand a municipal regulation face long documents, technical,language, and sanctions scattered across articles and tables. A retrieval-augmented generation (RAG) assistant can answer such questions, but evaluating one is not reducible to a single accuracy number: a legal answer can satisfy an automated judge and still be legally inadequate, and a citizen can find an answer useful without it being legally complete.,This article evaluates ValladolIA, a deployed assistant for two municipal regulations of Morelia, Mexico, and a central contribution is the evaluation design itself. The evaluation is organized into five layers, each with a declared scope: an expert judge benchmark of 47 questions answered by four legal judges; an automated LLM-as-judge validator (llama3); 664 real production interactions logged over three and a half months; explicit citizen feedback on 50 of those interactions; and a later qualitative expert review of 12 questions. Reported with their labels, the LLM-judge (llama3) overall score rose from 5.46 to 7.56 on a fixed 35-case set (a 0 to 10 score, an automated agreement signal distinct from human accuracy), the production distribution concentrates on infractions and articles (95.2% of 664 interactions), and feedback is positive but low-coverage (49 likes and 1 dislike among the 50 interactions of 664 that left any, a perceived-usefulness signal over a self-selected subsample separate from precision). The five layers measure different constructs and are kept separate, each reported under its own scope.

---

## uid: `arxiv:2606.28896v1`

- title: A Task-Driven and Quality-Assured Agent Framework for SAR Data Generation
- authors: Xuanting Wu, Fan Zhanga, Fei Ma, Ling Guan, Guochun Ma, Yongsheng Zhou
- affiliations: not stated
- posted: 2026-06-27
- source: arXiv
- link: https://arxiv.org/abs/2606.28896v1
- keyword hits: agentic, llm

### abstract

Synthetic aperture radar (SAR) data augmentation is important for improving the generalization of data-driven SAR interpretation models, yet practical augmentation workflows are often hindered by heterogeneous dataset formats, task-dependent metadata requirements, diverse generation methods, and weak validation of generated samples. This paper presents the \textbf{S}AR \textbf{A}ugmentation and \textbf{G}eneration \textbf{A}gent (SAGA), a schema-grounded and benefit-aware agent framework for task-oriented SAR data generation and augmentation. Given a natural-language request and heterogeneous SAR inputs, SAGA extracts observable dataset facts, validates executable dataset schemas, selects feasible augmentation strategies through validator-constrained planning, and compiles the selected strategy into an auditable augmentation workflow. Generated data are further assessed by quality, distribution, SAR-artifact, duplicate, leakage, and optional downstream-task evaluators to support evidence-qualified augmentation claims. By separating semantic proposal from deterministic validation and execution, SAGA improves the reliability and reproducibility of SAR augmentation decisions. Experiments on controlled agentic benchmarks and downstream SAR interpretation tasks show that SAGA improves schema grounding, skill planning, invalid-sample rejection, and downstream augmentation utility compared with rule-based, LLM-only, ReAct-style, and fixed-augmentation baselines.

---

## uid: `arxiv:2606.29467v3`

- title: mamabench and mamaretrieval: Benchmarks for Evaluating Medical Retrieval-Augmented Generation in Maternal, Neonatal, and Reproductive Health
- authors: Yi Ren
- affiliations: not stated
- posted: 2026-06-28
- source: arXiv
- link: https://arxiv.org/abs/2606.29467v3
- keyword hits: llm, retrieval-augmented

### abstract

Medical question-answering benchmarks rarely cover the maternal, neonatal, child, and reproductive-health questions a nurse-midwife asks, and, to our knowledge, no public chunk-level relevance benchmark exists for maternal-health guideline retrieval. We release two benchmarks that fill these gaps. mamabench is a scope-filtered QA set of 25,949 items assembled from seven existing expert-authored sources across multiple-choice, short-answer, and rubric-graded tracks; to help users calibrate the LLM judge that scores the rubric track, we re-scope HealthBench's physician-labelled meta-evaluation to the domain. mamaretrieval pairs 3,185 clinical queries with graded (0-6) relevance labels over a 63,650-chunk maternal-health guideline corpus, using a decomposed rubric that distinguishes a chunk that answers a query from one merely on its topic. Three decisions shape both: assemble and filter expert sources rather than author questions, grade relevance rather than binarise it, and measure and disclose the limits of the labels -- scope-classifier agreement, a frontier-judge check, and a pooling-completeness audit -- rather than treat them as an oracle. A companion paper uses the benchmarks to evaluate a deployed on-device assistant; both are released openly for research.

---

## uid: `doi:10.2139/ssrn.7021488`

- title: Building factorial prompt matrices using query targets and configurable factor classes: A methods framework for conversational AI response behavior research
- authors: Kevin Corti, Meghan Leaver
- affiliations: not stated
- posted: 2026-06-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7021488
- keyword hits: large language model, llm, prompting

### abstract

The term “factorial prompt matrix” (FPM) names and formalizes the emerging yet unstandardized practice of creating data structures that organize systematically varied prompts used to elicit responses from conversational AI (CAI) products. We introduce a methods framework for designing and implementing FPMs that, though broadly applicable, is primarily intended for social and behavioral scientists interested in controlled observational or experimental research on CAI response behavior. FPMs start from a principled sampling spine of CAI query “target” items that are then crossed with configurable factors drawn from four classes: (1) the large language model (LLM), (2) the product-system, (3) the user context, and (4) the query design. This produces a factorial grid of distinct prompts that can be passed to CAIs (e.g., using APIs). Using the ICD-11 (International Classification of Diseases, Eleventh Revision) as a spine for generating medical prompts, we demonstrate use of FPMs to analyze CAI information retrieval behaviors such as web search invocation. Key methodological contributions: A formalized data structure (FPMs) for systematically constructing and deploying prompts to CAIs.A modular, four-class schema for conceptually organizing the configurable factors of a CAI prompting protocol.Demonstration of FPMs across single-factor and multi-factor observational and experimental research designs.

---
