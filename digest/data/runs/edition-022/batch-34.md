# Classification batch 34 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-34.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7291235`

- title: Chasing One Rabbit or Many: Pandemic Driven Shifts in Attentional Dominance Among IT and Financial Services Organizations
- authors: Venugopal Balijepally, Jaemin Kim, Yashashri Kadam
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7291235
- keyword hits: generative ai

### abstract

We introduce attentional dominance—operationalized as the degree to which a single issue or a narrow set of issues monopolizes collective organizational attention, thereby displacing competing topics from the strategic agenda—as a novel construct within attention-based view (ABV) scholarship. Integrating ABV’s structural distribution principle and industry velocity, we evaluate pandemic-driven strategic shifts by analyzing 80 S&P 500 shareholder letters (2020–2023). Our findings reveal that dominance patterns diverge by industry velocity: high-velocity IT firms exhibited low dominance during the pandemic—framing the crisis as a distributed opportunity landscape—but transitioned to elevated dominance post-pandemic around innovation and generative AI. Conversely, low-velocity financial firms displayed crisis-induced high dominance, followed by post-pandemic diversification driven by institutional normalization. Our work extends ABV theory by conceptualizing attentional dominance as a distributional, portfolio-level construct.

---

## uid: `doi:10.2139/ssrn.7290194`

- title: A Skeleton-Grounded Vision–Language Framework for Biomechanical Critique of Amateur Tennis Strokes
- authors: Chai Beng Tan, Muhammad Hisyam Rosle
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7290194
- keyword hits: gpt-4, instruction-tuned, prompting

### abstract

Markerless human pose estimation provides accessible joint-level kinematic information, but its coordinate-based output does not directly support interpretable biomechanical feedback. Vision–language models (VLMs) can generate natural-language critiques, yet their application to raw sports images is limited by weak joint-level grounding and hallucinated or sycophantic responses. This study presents a two-stage skeleton-grounded vision–language framework for analysing amateur tennis strokes. First, a lightweight pose estimator detects COCO-17 keypoints and confidence scores, which are converted into a kinematics-aware visual prompt containing labelled joints, on-image joint angles, and confidence-modulated skeletal edges. Second, a 3-billion-parameter instruction-tuned VLM generates biomechanical critiques using structured prompting, with optional deterministic pose evidence, overlay-versus-raw visual contrastive decoding, and a motion-history skeleton composite for temporal cues. The framework was evaluated on 36 amateur tennis clips from the THETIS dataset, comprising 108 scored frames per condition, using a reference-free protocol based on a GPT-4o judge, hallucination-rate analysis, biomechanics-vocabulary coverage, and paired statistical testing. Compared with raw frames, the full skeletal overlay significantly improved biomechanical accuracy and completeness. Adding deterministic evidence or visual contrastive decoding produced the largest gains, increasing biomechanical accuracy from 2.56 to 3.09 and 3.00, respectively, while reducing the hallucination rate from 0.70 to 0.57 and 0.59. Temporal representations increased motion-related vocabulary but weakened grounding, whereas contrastive decoding restored grounding while suppressing some motion language. Overall, the results demonstrate that explicit pose-based visual grounding and decoder-level control can improve the reliability of VLM-generated sports feedback, although absolute critique quality remains moderate and further validation with expert-annotated references is required.

---

## uid: `doi:10.2139/ssrn.7304839`

- title: LLM-Driven Adaptive Testcase Generation for EDA Validation with PPA and Coverage Feedback: Typed-Intent Compilation and Hierarchical Pareto Bandits
- authors: Haijian Zhang
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7304839
- keyword hits: llm

### abstract

Large-language-model (LLM) test generation for hardware verification is attractive because an LLM can express semantic corner cases that are difficult to obtain from purely random stimulus. In practice, however, directly asking an LLM to emit executable HDL creates a fragile loop: syntax errors, stale state, non-reproducible model calls, and a reward signal dominated by functional coverage. This paper develops a concrete alternative, TICAP (Typed-Intent Coverage-and-PPA adaptive generation), in which the LLM is restricted to a typed, auditable test-intent vocabulary and an online bandit compiles and schedules those intents using two feedback channels: functional coverage gain and switching-activity-envelope gain. A second-level allocator, H-TICAP, distributes a fixed global verification budget across designs using authentic synthesis/static-timing PPA context and online coverage-yield posteriors. The PPA context is taken from the public LogikBench FreePDK45 baseline produced with Yosys 0.66 and OpenSTA 3.1.0; no locally unavailable physical-design result is invented. We evaluate the inner policy on 21 parameterized instances derived from seven real LogikBench RTL families and the hierarchical policy on the seven default LogikBench configurations. All testcase-selection results are generated by the released Python artifact, with 20 independent seeds for the main experiments. At a 512-vector per-DUT budget, typed adaptive methods reach about 0.945 coverage AUC and approximately 0.99 final functional coverage, versus 0.679 AUC and 0.738 final coverage for uniform random stimulus. Relative to a frozen LLM-intent schedule, the full policy raises switching-activity-bin coverage from 0.8231 to 0.8300 while maintaining essentially the same coverage AUC. Under a global 4096-vector portfolio budget, H-TICAP achieves 0.9478 PPA-weighted coverage compared with 0.9457 for a strong coverage-only adaptive allocator (paired one-sided Wilcoxon p = 0.0123) and 0.8932 for uniform typed allocation. Ablations, sensitivity sweeps, cross-scale analysis, and deterministic mutation tests show where PPA feedback helps and where it does not. The main empirical conclusion is intentionally narrow: LLM semantics are most useful when compiled into safe intent primitives, while PPA feedback becomes materially useful at the portfolio-allocation level rather than as a replacement for functional coverage within a nearly saturated single-DUT test.

---

## uid: `doi:10.2139/ssrn.7316479`

- title: Human-Centered Cybersecurity in the Enterprise A Governance and Risk Management Framework for Security Culture, Usability, and Resilience
- authors: Prabhat McDonnough-Contreras
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7316479
- keyword hits: chatgpt

### abstract

The analysis draws on academic literature, government frameworks, and professional research while extending those discussions toward the practical implementation of HCC within enterprise environments. The Enterprise Human-Centered Cybersecurity Framework (E-HCCF) developed in this paper represents my proposed synthesis of organizational maturity, human-centered measurement, and continuous improvement within a governance and risk-management structure. It is offered as a conceptual framework for further consideration and evaluation and should not be interpreted as an official NIST framework, recommendation, or position. Marymount University is listed as my current academic affiliation. The views and conclusions expressed in this paper are my own and do not imply institutional endorsement. AI Use Disclosure During the preparation of this work, I used OpenAI's ChatGPT to support literature discovery, source verification, language refinement, structural editing, and publication formatting. All AI-assisted output was critically reviewed, revised, and verified by me, and I take full responsibility for the content of this paper.

---

## uid: `doi:10.2139/ssrn.7306419`

- title: Economic Uncertainty, Investor Sentiment, and Corporate Fourth-Quarter Investments
- authors: Bochen Li, Michael A. Goldstein*, lili shao, Tong Yu
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7306419
- keyword hits: llm

### abstract

Firms often increase capital expenditures in the fourth fiscal quarter to exhaust remaining budgets before year-end, a behavior commonly attributed to agency conflicts and "use-it-or-lose-it" incentives. We examine whether economic uncertainty and investor sentiment affect the magnitude of this fourth-quarter investment effect. Using novel large-language-model (LLM) measures constructed from Wall Street Journal news articles, together with conventional uncertainty proxies, we find that heightened uncertainty significantly reduces excess fourth-quarter capital expenditures, whereas optimistic investor sentiment amplifies year-end investment. The results suggest that uncertainty disciplines managerial spending, while favorable sentiment exacerbates discretionary investment. Our findings highlight how economic narratives and market conditions influence corporate investment decisions and demonstrate the usefulness of LLM-based textual measures for studying managerial behavior.

---

## uid: `doi:10.2139/ssrn.7318040`

- title: Budget-Constrained Evidence Distillation and Risk-Controlled Escalation for LLM-Augmented Failure Triage in Large-Scale AI Development Pipelines
- authors: Wenyu Zhao
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7318040
- keyword hits: large language model, llm

### abstract

Large-scale artificial-intelligence (AI) development pipelines fail constantly, and each failure produces thousands of log lines that an engineer, or increasingly a large language model (LLM), must read in order to assign a root cause. Feeding whole logs to an LLM is economically impossible at fleet scale, and the truncation heuristics used in practice-keep the first or the last k tokens, or grep for ERROR-discard the decisive evidence surprisingly often. We formalise the resulting bottleneck as budget-constrained evidence distillation: given a token budget B, select the subset of log lines that maximises the diagnostic information handed to a downstream reasoner. We present Ledger, which (i) scores every line with a contrastive template salience learned from run-level pass/fail labels only, augmented by rarity, severity, temporal-locality and (optionally) entity-sequence and parameter-anomaly channels; (ii) selects lines by maximising a monotone submodular objective that combines facility-location coverage with a concave with severity filtering and 14.3% with tail truncation; the LLM was correct on every excerpt that contained the evidence, so the entire gap is attributable to selection. The conformal router captures 100% of never-before-seen failure modes while issuing 35% fewer LLM calls than confidence-threshold routing. We also report two negative results: the parameter-anomaly channel pays off only on the 4.5% of evidence lines whose template also occurs in passing runs, and strict within-group deduplication-a natural design choice-costs 15 points of recall.

---

## uid: `doi:10.2139/ssrn.7318298`

- title: Teaching Legal Research in the Age of Generative AI: Designing an Experiential Course for a New Legal Research Landscape
- authors: Lauren E. Diaz
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7318298
- keyword hits: generative ai, generative artificial intelligence

### abstract

Generative artificial intelligence is transforming legal research faster than any prior technological development, yet legal research instruction has not kept pace. Law schools have responded not only slowly, but unevenly. This piecemeal response persists because, although there is growing consensus that AI belongs in the curriculum, there is far less meaningful guidance on how to teach AI-assisted legal research. This Article argues that law schools should treat AI-assisted legal research as a core part of legal research pedagogy, not as a disconnected topic in legal technology, academic integrity, or ethics. Legal research instruction must prepare students not just to use AI tools, but to question, verify, revise, and, when necessary, reject AI output. This Article develops a model of AI-assisted research competence centered on judgment, verification, and reflection, and argues that this competence should be taught across the curriculum: through integrated instruction in first-year legal research and writing courses and sustained, experiential instruction in advanced courses for upper-level students. The goal is not to replace traditional legal research instruction, but to build on it. AI makes traditional legal research skills more important, not less. Without them, students cannot verify AI output, and an AI tool that cannot be verified cannot be safely used. This Article therefore proposes an additive model: preserve foundational research instruction, integrate AI legal research pedagogy at multiple points in the curriculum, and create sustained experiential opportunities for students to develop the habits of verification, ethical reasoning, tool evaluation, and supervised professional judgment.

---

## uid: `doi:10.2139/ssrn.7291461`

- title: TablEye: Seeing small Tables through the Lens of Images
- authors: Seungeon Lee, Sang-Chul Lee
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7291461
- keyword hits: large language model, llm

### abstract

Few-shot tabular learning is increasingly important: labeled tables are costly and rare in high-stakes domains such as medical diagnosis, yet the field lags far behind few-shot learning in vision and language. The gap persists because tabular data lacks the shared structure that lets models transfer prior knowledge across datasets, and existing remedies impose their own constraints—semi-few-shot methods need a large unlabeled pool, while language-model methods require meaningful feature names and billions of parameters. We propose TablEye, which instead transfers prior knowledge from the image domain to tabular data: each row is converted into a tabular image that preserves feature semantics through spatial relations, and few-shot algorithms then reuse prior knowledge learned from natural images. This cross-domain transfer makes the rich prior knowledge of large-scale image data available to tabular tasks without restricting the dataset. Using no unlabeled data and a model up to five orders of magnitude smaller than a large language model (LLM) baseline, TablEye surpasses the LLM-based TabLLM by up to 0.11 AUC in a 4-shot task and the semi-few-shot STUNT by about 3.00% accuracy in a 1-shot setting, while handling high-dimensional tables with uninformative feature names that text-based methods cannot process. These results position cross-domain visual priors as a practical, constraint-free route to data-efficient tabular learning

---
