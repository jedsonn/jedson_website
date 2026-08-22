# Classification batch 32 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-32.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7315789`

- title: A Checkpoint-Augmented Program Knowledge Graph for Auditable Bounded Inference and Selective Release in Code Reasoning
- authors: Emmanuel  Adebowale Adediran
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7315789
- keyword hits: llm

### abstract

Bytechain-KG is an implemented knowledge-based architecture for auditable bounded code reasoning. Its knowledge representation encodes typed program entities, data and control dependencies, checkpoint obligations, support predicates, and release rules in a checkpoint-augmented program knowledge graph. Graph queries derive the terminal support slice and ordered proof plan; bounded transition rules infer concrete states; contradiction and independently replayed proof rules decide whether to release a returned or raised result or to abstain. On a development-aligned, repaired 800-case CRUXEval-derived conformance protocol, reported as descriptive conformance evidence rather than held-out evaluation, Bytechain-KG released 766 cases, abstained on 34, and recorded no covered error (95.75% support coverage; one-sided 95% covered-error upper bound 0.39%). BytechainBench v1.0 adds 614 owned records for length composition, fresh-family variation, and implementation invariance; 167/174 covered transformation pairs preserved both outputs and canonical proof signatures. The replay verifier rejected every applicable corruption across six mutation classes. In a development-aligned 200-case neuro-symbolic diagnostic, an LLM hypothesis generator adjudicated by executor states and proof guards achieved 90.0% exact accuracy, while the fully guarded executor-only release achieved 96.5%; direct prediction achieved 27.5%. These secondary diagnostic results do not support a frontier-model claim. The contribution is a bounded knowledge-representation, inference, and selective-decision mechanism, not a novel Python sandbox or unrestricted correctness proof.

---

## uid: `doi:10.2139/ssrn.7310918`

- title: Who Governs Autonomous AI Execution? Execution Governance AI (EGA) V9: A Deterministic Runtime Governance Framework for Trustworthy Autonomous Workflows
- authors: DaeJung Byun
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7310918
- keyword hits: foundation model

### abstract

As autonomous AI systems transition from language-generation tools to execution-driven agents, maintaining trustworthy runtime execution without sacrificing performance, operational cost, deployment simplicity, or security has become a fundamental engineering challenge. How can autonomous AI systems satisfy these requirements simultaneously without modifying existing AI applications or foundation models? Execution Governance AI (EGA) V9 addresses this challenge through a deterministic runtime-governance framework that combines deterministic replay, provenance-aware verification, trust-state evaluation, and fail-closed containment as a unified executiongovernance layer.

---

## uid: `doi:10.2139/ssrn.7312218`

- title: Digital Colonialism, AI, and the Cross-Border Migration of African Knowledge: Rethinking Intellectual Property Justice in the Global South
- authors: Mutoniwase Mbaya Aroobe
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7312218
- keyword hits: generative ai

### abstract

This paper examines whether existing intellectual property and data governance regimes adequately regulate the cross-border extraction and use of African knowledge in artificial intelligence (AI) systems. As generative AI technologies increasingly depend on large datasets collected across jurisdictions, African cultural expressions, legal materials, indigenous knowledge, languages, educational resources, and creative works are being incorporated into global AI infrastructures, often without meaningful consent, attribution, compensation, or equitable benefitsharing. The paper argues that current copyright and related intellectual property frameworks are insufficient to address the legal and structural inequalities created by transnational AI data practices, and it proposes a reform-oriented framework built on transparency, cross-border benefitsharing, recognition of collective knowledge interests, and equitable participation in AI governance.

---

## uid: `doi:10.2139/ssrn.7293760`

- title: Early-truncation and Information Leakage in Small Non-reasoning-tuned Language Models
- authors: Santosh Kumar
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7293760
- keyword hits: chain-of-thought, instruction-tuned, qwen

### abstract

Chain-of-thought (CoT) reasoning traces are increasingly used as an interpretability aid, yet whether small language models' answers are genuinely determined by the reasoning they display, or already fixed well before the trace completes, remains poorly characterized outside the frontier end of the model-size spectrum. We present a systematic, inference-only study of early-truncation answer leakage in a matched Qwen2.5 model family spanning 0.5B to 7B parameters, in both base and instruction-tuned variants, on GSM8K. Using organic truncation (no forced interruption), we measure the point at which an answer first becomes recoverable, the rate at which forced early answers diverge from the full-trace answer, and the gap between free continuation and forced extraction at matched prefixes, throughout tracking commitment rate as an explicit covariate to guard against abstention confounds. We find that leakage point does not scale monotonically: it rises from 0.5B through 3B before dropping sharply at 7B, and a mixed-effects model shows truncation robustness depends significantly on scale only once the comparison range extends to 7B (p < 0.001), a trend invisible within 0.5B-3B alone. Instruction-tuned models show consistently larger detection-extraction gaps than their base counterparts at matched scale, coupled with measurably higher hedging under forced extraction. These results suggest that truncation-based CoT diagnostics calibrated on a narrow small-model range can substantially underestimate the robustness of a nearby larger small model, with direct implications for on-device deployment settings where such lightweight diagnostics are most needed.

---

## uid: `arxiv:2608.19165v1`

- title: ChildSafeAds Shared Task 2026: Commercial Content in Child-Facing YouTube Videos
- authors: Thales Bertaglia, Catalina Goanta, Gerasimos Spanakis, Gunes Acar
- affiliations: not stated
- posted: 2026-08-19
- source: arXiv
- link: https://arxiv.org/abs/2608.19165v1
- keyword hits: gpt-5

### abstract

ChildSafeAds is a shared task on commercial content in YouTube videos likely to reach children and teenagers. It contains 3,360 videos from 939 channels. Each instance begins with a segment submitted to SponsorBlock, an open-source crowdsourced browser extension whose users mark sponsor segments so that others can skip them. We pair the segment with its available transcript, video and channel information, and a sales or service page linked from the video description. Systems determine what kind of offer is being promoted (ST1), assign product categories (ST2), and identify legal risk flags (ST3). The evidence is divided into four cumulative access levels, from the transcript to the linked page, so results can be compared against the cost of collecting the data. 45.5\% of videos in our data failed to properly use the in-platform ad disclosure method (the ``Includes paid promotion'' label). GPT-5.4 produced the labels after the expert organiser team reviewed samples and iterated on the taxonomy, prompts and model choices. GPT-5.6-luna independently labelled the development set. This report describes the task, data and evaluation. An updated version will add participating systems and shared-task results.

---

## uid: `arxiv:2608.19083v1`

- title: When Readability and Source Retention Diverge: An Evaluability Gap in AI Translation
- authors: Chenchen Mao, Hanjing Shi, Haiyan Jia, Emily Wegrzyn, Dominic DiFranzo
- affiliations: not stated
- posted: 2026-08-19
- source: arXiv
- link: https://arxiv.org/abs/2608.19083v1
- keyword hits: llm

### abstract

Readable AI output can leave an evaluability gap: even when the source is shown, an overall-quality judgment may not reflect what an output preserves. We investigated how source-text condition and output rendering relate to perceived translation quality, and how output and system appraisals relate to trust and stated disclosure willingness in a plain-text interface. A focal 2 * 2 comparison (N=306) using TransLingo examined simple generated narratives and complex literary-philosophical prose alongside LLM-generated readability-oriented outputs and researcher-revised fidelity-oriented outputs. A descriptive stimulus audit indicated greater source retention in fidelity-oriented outputs in both source-text conditions. Factorial analyses showed a significant rendering-by-source-text-condition interaction in perceived quality. Participants rated fidelity-oriented outputs higher than readability-oriented outputs for the simple narratives, whereas no reliable rendering difference emerged for the complex prose. A corresponding source-condition-dependent pattern was observed for perceived intelligence, agency-oriented anthropomorphic attribution, and task-performance trust. A separate theory-ordered appraisal-structure SEM characterized concurrent associations among perceived quality, perceived intelligence, agency-oriented anthropomorphic attribution, task-performance trust, and stated disclosure willingness across six domains, with task-performance trust as the proximal correlate of stated willingness. The observed rating pattern distinguishes source access from source evaluability: for the complex stimuli, displaying the source did not ensure that one overall-quality rating reflected differences in retained content. It also separates support for evaluating translation output from data-handling support for decisions about what personal text to entrust to a system.

---

## uid: `arxiv:2608.18836v1`

- title: Verifiable abstention makes AI leak diagnosis accountable in water distribution networks
- authors: Tianwei Mu, Yue Wang, Mingzhe Yuan, Manhong Huang, Wenhong Wang, Xuerui Yin, Qing Luo, Min Xiao
- affiliations: not stated
- posted: 2026-08-19
- source: arXiv
- link: https://arxiv.org/abs/2608.18836v1
- keyword hits: llm

### abstract

Utilities lose a substantial share of treated water to leakage, yet rarely trust artificial-intelligence localizers to dispatch crews: guessing everywhere cannot justify excavation. The gap is accountability, not accuracy: no method proves when it should not act. Here we recast leak localization as decision-making under verifiable abstention. A physics-grounded executor agent falsifies hypotheses (leak, demand, sensor, valve) against a digital twin; an independent supervisor agent, with a large-language-model (LLM) auditor, checks evidence against a code-verifiable contract, then certifies a dispatch, requests evidence or abstains. Under field-grade noise, a 32% forced baseline becomes 96% decision precision on acted events. On an independently generated benchmark it acts on only 4 of 33 leaks, all correct. A 194-event register of audited real leak locations with twin-simulated pressures and flows yields five excavation dispatches, three correct, and 44% survey recovery at full district precision. Accountable abstention offers a defensible route to autonomous water-infrastructure operation.

---

## uid: `arxiv:2608.18795v1`

- title: Decomposing Wrong-Consensus Agreement in LLM Self-Consistency: A GPT-4.1 Case Study
- authors: Lizhuo Zhang, Mengmeng Tang, Chenfeng Long, Xiaoyong Tang, Xiang Luo
- affiliations: not stated
- posted: 2026-08-19
- source: arXiv
- link: https://arxiv.org/abs/2608.18795v1
- keyword hits: gpt-4, llm

### abstract

Majority voting over multiple LLM samples is widely used to raise answer accuracy, yet its gain varies erratically: on hard questions it can even backfire. This paper gives a quantitative account of this failure. A pluralistic agreement index Gamma is defined as the expected fraction of the samples of a wrong run that agree with the consensus, normalized by a reference scale d=(1-p)/(C-1), and is decomposed into a mechanical component (what a vote delivers given only a per-case answer preference) and a preference-unexplained residual. The mechanical null is difficulty-matched and leak-free: each case is resimulated at its own accuracy and option preference, estimated from the case's other runs, so no run predicts its own agreement. On GPT-4.1 the decomposition shows benchmark-associated direction (an observational ordering over n=4 cells per benchmark, not a significance claim). On multiple-choice GPQA-Diamond, the per-case answer preference explains 81-93% of the held-out test-run agreement index: the shared-bias-dominates account over-claims here, because a wrong but attractive option the whole cohort latches onto is captured by the per-case preference channel (whether that preference is induced by shared training bias is not identified). On open-domain AIME, the mechanical preference explains only 59-78% (21-29% if shrunk to pure noise), and a preference-unexplained residual of 1.56-2.80 Gamma units survives, which a run-level preference-heterogeneity reference more than absorbs (1.4-2.1). A self-consistency backfire on hard questions is reproduced (binned voting gap down to -0.09, coupled CI [-0.12,-0.07]), and the highest-agreement bin reaches an accuracy of only 0.42-0.83, a 1.2-3.6x lift over base rate: agreement is graded evidence, not certification. No new voting method is proposed; code and evidence are committed and reproducible.

---
