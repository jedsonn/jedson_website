# Classification batch 6 of 20, edition 17

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-017/batch-6.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7152058`

- title: A Measurement Crisis in Multilingual LLM Safety: Heuristic Classifiers Systematically Undercount Reasoning-Model Refusals in Indic Languages
- authors: Raghavendra Kaushik Kachireddy
- affiliations: not stated
- posted: 2026-08-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7152058
- keyword hits: claude, gemini, gpt-4, llama, llm

### abstract

We introduce IndicSafetyBench, a pilot benchmark of 3,340 adversarial prompts across English plus six Indic languages (Hindi, Marathi, Telugu, Kannada, Tamil, Bengali), eight harm categories, and three attack vectors (direct, cultural-framing, code-switching). We evaluate six production language models — three Sarvam variants (105B and 30B reasoning models, m legacy 24B), GPT-4o-mini, Gemini-2.5-Flash, and Llama-3.3-70B — generating 20,400 model inferences scored by a dual-judge pipeline (a multilingual heuristic regex classifier with ~180 refusal anchors across thirteen language/script combinations, and a Gemini-2.5-Flash LLM-as-judge with a structured JSON rubric), validated against each other with Cohen's kappa on 20,268 paired labels. Our central finding is methodological: heuristic-based safety classifiers systematically undercount Sarvam reasoning-model refusals by up to 60 percentage points in Dravidian languages and Bengali, because these models produce structurally consistent soft-refusal patterns ("I cannot help with X, but here are safer alternatives") that regex classifiers miscount as partial engagement. Per-cell kappa collapses to 0.07-0.13 for Sarvam-105B and Sarvam-30B in Tamil and Bengali while remaining at 0.51-0.83 in English and Hindi. A partial extension to OpenAI's open-weight gpt-oss-120b (n=200 stratified pilot) shows the same heuristic-undercount pattern arising via a mechanically independent route: 91% of its refusals use a typographic apostrophe (U+2019) that the heuristic's ASCII-only anchor bank silently misses, dropping recall from 0% to 98% under a three-line regex patch. Heuristic-only Indic safety benchmarks may have systematically under-reported reasoning-model safety. To bound the single-LLM-judge dependence, we run Anthropic Claude as an independent third refusal judge on Sarvam-105B across all seven languages (n=457 successful labels): Claude-vs-Gemini agreement is 96.9% (per-language 93-100%), reproducing the heuristic-vs-LLM disagreement pattern without exposure to the Gemini labels. We further find that Indian-persona cultural-framing attacks (-16 to -31 pp for non-reasoning models, 95% paired-bootstrap CI entirely below zero) have no detectable effect on Sarvam reasoning models (CI crosses zero, with an explicit ceiling-effect caveat at 82-96% refusal floor); we defend the non-reasoning side of this finding against the placebo-perturbation critique of Mukherjee et al. (2024). We release seeds, code, and judgments at https://github.com/kaushik0x7d2/indicsafetybench with gated access to raw responses.

---

## uid: `arxiv:2608.04009v1`

- title: SocietyBench: Forecasting Counterfactual Social-World Evolution
- authors: Zhenran Wang, Zhonghan Bian, Jinsong Li, Zhangyang Qi
- affiliations: not stated
- posted: 2026-08-04
- source: arXiv
- link: https://arxiv.org/abs/2608.04009v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs), and the agents built on top of them, are now benchmarked heavily on whether they can finish a task -- fix a bug, drive a browser, operate a GUI. A complementary social ability, namely how well a model understands and forecasts the way real social events unfold, has barely been measured. We introduce SocietyBench, an end-to-end benchmark that takes a one-line event topic, collects Web news and social-media posts across five platforms, distills them into a date-indexed timeline that keeps factual events and a public-opinion layer separate, and then turns every cutoff date on that timeline into an audited bank of forecasting questions. Questions are scored on two orthogonal 100-point axes: probability calibration and temporal accuracy. Before any model sees a timeline, a three-phase procedure replaces every named entity and shifts every date by a per-event constant, turning a real arc into a counterfactual social world -- structurally identical to what happened, but stripped of the surface labels a model could match against pre-training memory. On five heterogeneous events and 125 prediction points in Chinese and English editions, the strongest of six frontier LLMs reaches only 75.0 out of 100, against a trivial anchor of 50. The two axes come apart: a model can be calibration-strong but time-weak, or the reverse. Three agent frameworks built on a shared base model fail to improve on that base, and two model-free heuristics trail every LLM. Per-event gaps reach 21.4 points on a single axis, which is our main argument for evaluating on several events rather than one. All anonymized timelines, question banks, ground truth, and scoring code are released.

---

## uid: `arxiv:2608.04001v1`

- title: Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility
- authors: Mohsen Hariri, Weicong Chen, Nahal Shahini, Vikash Singh, Kai Ye, Amirhossein Samandar, Debargha Ganguly, Sreehari Sankar
- affiliations: not stated
- posted: 2026-08-04
- source: arXiv
- link: https://arxiv.org/abs/2608.04001v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models can solve substantially harder reasoning problems with more inference-time compute. The term "test-time scaling," however, now covers diverse inference algorithms that extend deliberation along a single trajectory, sample completed candidates and aggregate them through voting or verification, or search over unfinished partial states. These algorithms differ in their statistical structure, compute accounting, and failure modes. Treating these procedures as interchangeable under a single scalar "budget," or reporting accuracy without the inference protocol that produced it, makes results difficult to compare across studies. We develop a systematic account of test-time scaling along three axes. First, we formalize test-time scaling as budgeted inference over the implicit prefix tree of an autoregressive model and distinguish three structural regimes: single-trajectory sequential scaling, leaf-level scaling with terminal reduction, and prefix-level scaling. Second, we treat the evaluated object as the entire inference system and develop evaluation principles that separate end-to-end system performance from candidate-bank diagnostics. We introduce an evaluation profile whose coordinates and simple functionals recover or bound common repeated-sampling metrics, and prescribe protocol-matched reporting of compute and uncertainty. Third, we specify reproducibility requirements for inference protocols, distinguishing exact replay from distributional reproducibility and identifying the artifacts needed to support each. We also organize the open-weight reasoning ecosystem by model-side and interface mechanisms, apply these principles to broad-knowledge, symbolic-reasoning, and competition-mathematics benchmarks, and assemble over 2 billion full reasoning traces for release with progressively richer verifier and token-level signals.

---

## uid: `arxiv:2608.03532v1`

- title: Cross-Lingual Bias in Large Language Models: A Comparative Analysis of English and Swahili
- authors: Ruolei Zhang, Teddy Njuguna, Yue Feng
- affiliations: not stated
- posted: 2026-08-04
- source: arXiv
- link: https://arxiv.org/abs/2608.03532v1
- keyword hits: gemini, gpt-5, large language model, large language models

### abstract

Large language models are increasingly deployed in multilingual contexts, yet safety alignment and bias evaluation remain overwhelmingly English-centric. We investigate whether social biases generalise across languages by submitting 4,900 symmetric English--Swahili prompt pairs to GPT-5.2 and Gemini 2.5 Flash across nine demographic bias axes, yielding 19,600 completions evaluated for stereotype prevalence, sentiment, refusal behaviour, and cross-lingual semantic similarity. Our findings show that bias transforms rather than transfers: stereotype rates shifted by up to 12 percentage points on specific axes, Gemini's neutral-sentiment rate doubled in Swahili, and GPT-5.2 refused 169 prompts in English and zero in Swahili, consistent with refusal behaviour anchored to English-language surface forms at the behavioural level. Over 55% of prompt pairs produced semantically dissimilar completions across both models. These reinforce the idea that English-only bias audits do not produce adequate coverage for multilingual deployment.

---

## uid: `arxiv:2608.05030v1`

- title: From Score Matrices to Football-Aware Match-State Simulation: An Auditable LLM Harness for Exact-Score Reranking
- authors: Shaopeng Liang
- affiliations: not stated
- posted: 2026-08-05
- source: arXiv
- link: https://arxiv.org/abs/2608.05030v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Football score forecasting combines a strong statistical core with a difficult contextual edge. Dynamic Poisson-family models estimate team strength, expected goals, and coherent score probabilities, but do not directly understand roles, tactical matchups, motivation, or how a first goal changes behaviour. Large language models (LLMs) can reason about such concepts, yet are not calibrated probability engines. We combine both components through an auditable information harness. This paper documents four iterations: V1, a dynamic score-driven Dixon-Coles baseline; V2, which maps LLM contextual ratings back into expected-goal parameters; V3, which replaces scalar correction with goal-by-goal simulations over a frozen score-candidate set; and V4, which adds shared first-breakthrough and post-goal cascade judgments, time-aware stopping, and deterministic tail candidates. The harness defines input semantics, supplies pre-match evidence, and constrains the LLM to an inspectable reasoning route. On a chronological replay of the first 150 matches of the 2025-26 English Premier League, V1 achieved 10.0% Top-1 and 26.7% Top-3 exact-score accuracy. V3 reached 12.0% and 30.0%, while V4 reached 14.7% and 30.7%. V4 increased candidate coverage from 77.3% to 84.7%, although no added tail candidate became a Top-3 exact hit. V1's native 1X2 distribution achieved 53.3% argmax accuracy, 0.9878 log loss, 0.5870 Brier score, and 0.2095 ranked probability score. These results are exploratory: the development slice is not an untouched benchmark, and temporal input isolation cannot exclude outcome memory in a closed LLM. The contribution is an auditable hybrid architecture, a clear design evolution, and negative findings showing where football-aware simulation does and does not improve score selection.

---

## uid: `doi:10.2139/ssrn.7230054`

- title: Clinical Safety Evaluation of LLM Assistants Using Decomposed LLM-as-Judges: A Framework Grounded in Real-World Interactions and Formal Risk Assessment
- authors: Andras Meczner, Octavia Wilks, Emily Hunter Balir, See PDF
- affiliations: not stated
- posted: 2026-08-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7230054
- keyword hits: large language model, large language models, llm, llms

### abstract

Background: Large language models (LLMs) are being deployed in healthcare faster than they can be safely evaluated. Existing clinical evaluation frameworks rarely connect model failures to formal medical-device risk management, and human annotation can be inconsistent and difficult to scale. We developed a framework that decomposes hazards into auditable criteria applied by LLM judges, designed to provide a scalable risk-estimate input to ISO 14971 risk management. We evaluated this approach using a user-facing women’s health chatbot. Methods: Hazards were decomposed into explicit rubrics, initially derived from the hazard log and expanded inductively from observed failures. The included rubrics were operationalised through 25 LLM judges ("multi-judges"), refined and evaluated using 12,193 real-world and synthetic question-answer pairs. For comparison, a single LLM judge ("combined judge") was constructed using the same 25 rubrics. Multi-judges, the combined judge, and human annotators were compared against a reference standard. The first primary outcome compared fail-class recall across these three evaluation approaches. The second was determining agreement between multi-judge-derived and reference standard-derived ordinal risk estimates and acceptability classifications. Findings: Multi-judge-derived and reference standard-derived hazard-level risk estimates were identical, yielding the same acceptability classification for all four in-scope hazards. Fail-class recall was 95·3% for the multi-judges, 24·9% for human annotation, and 69·1% for the combined judge, at precisions of 61·1%, 58·7%, and 47·3%, respectively. Calibration increased the multi-judges’ macro-F1 from 72·9% to 86·7%. Interpretation: Multi-judge-derived ordinal risk estimates matched those derived from reference standard and preserved their acceptability classifications, indicating that decomposed LLM judges can produce auditable, hazard-traceable outputs that support ISO 14971 risk management. Together, these findings suggest that decomposition may be central to reliable clinical safety evaluation of LLM assistants, and that dedicated LLM judges can provide a scalable, practical implementation layer when calibrated on real-world cases.

---

## uid: `doi:10.2139/ssrn.7183178`

- title: Adaptive Learning Path Generation Using Reinforcement Learning and Large Language Models for Personalized Higher Education
- authors: Younes Boumezough, Radoine Ouhmed, Sara Ait Lahcen
- affiliations: not stated
- posted: 2026-08-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7183178
- keyword hits: large language model, large language models, llm, llms

### abstract

models the educational process as a sequential decision-making Personalized learning has become one of the primary objectives of modern higher education as universities seek to provide learning experiences adapted to the needs, abilities, and learning pace of individual students. Conventional Learning Management Systems generally offer identical learning sequences to all learners, regardless of their prior knowledge, cognitive abilities, learning preferences, or academic performance. Although recommendation systems and adaptive tutoring platforms have introduced limited personalization, most existing approaches rely on static recommendation rules or predefined learning paths that cannot continuously adapt to the evolving learning state of each student. Recent advances in Large Language Models (LLMs) have significantly enhanced educational applications by enabling intelligent tutoring, automatic content generation, question answering, and personalized feedback. However, current LLM-based educational systems primarily generate educational content without actively optimizing the sequence in which learning activities should be presented. Consequently, they lack the capability to determine the most effective learning trajectory that maximizes knowledge acquisition while minimizing cognitive overload and learning time. This paper proposes an Adaptive Learning Path Generation Framework (ALPG) that integrates Reinforcement Learning (RL) with Large Language Models to dynamically construct personalized learning pathways for university students. The proposed framework models the educational process as a sequential decision-making problem in which an RL agent continuously selects the next optimal learning activity according to the learner’s current knowledge state, engagement level, historical performance, and educational objectives. Large Language Models complement the decision process by generating personalized explanations, adaptive exercises, formative assessments, and instructional feedback corresponding to each selected learning activity.

---

## uid: `doi:10.2139/ssrn.7182798`

- title: Large Language Models Meet Neuro-Symbolic Computing: Perspectives and Challenges
- authors: Jingwen Xu, Yifei Wang, Changze Lv, Yiyang Lu, Yanxun Zhang, Xiaohua Wang, Xuanjing Huang, Xiaoqing Zheng
- affiliations: not stated
- posted: 2026-08-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7182798
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs), built largely within the connectionist paradigm, have made striking progress across a wide range of tasks; yet they still face persistent challenges in reliable reasoning, factual consistency, controllability, and interpretability-areas that have long been central to symbolic AI. This complementarity has brought renewed attention to neuro-symbolic computing (NSC), which seeks to combine neural representation learning with symbolic structure, abstraction, and reasoning. This survey examines the evolving relationship between LLMs and NSC through a structured taxonomy. We organize representative work into three categories: neural models that support symbolic reasoning, symbolic mechanisms that guide neural models, and collaborative neuro-symbolic systems in which neural and symbolic components interact during learning and inference. We also distinguish among three levels of integration: data-level augmentation with symbolic supervision, inference-time augmentation through reasoning tools, and representation-level integration by formal symbolic languages. Current approaches often remain loosely coupled, limiting their ability to support robust reasoning, strong generalization, and systematic manipulation of knowledge. NSC therefore matters not only as a way to improve performance on reasoning-intensive tasks but also as a route toward rethinking how LLMs represent, organize, and generalize knowledge. Looking ahead, we identify several settings in which tighter neurosymbolic integration may become increasingly important, including high-stakes reasoning, long-horizon agent systems, and skill-centric modular intelligence.

---
