# Classification batch 166 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-166.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6886361`

- title: Reproducibility is the New Copyleft: Defining AGI-oriented Reproducible Builds
- authors: Masayuki Hatta
- affiliations: not stated
- posted: 2026-06-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6886361
- keyword hits: large language model, large language models

### abstract

The concept of copyleft, as implemented in licenses such as the GNU General Public License, was a legal hack that used copyright to guarantee user freedom by tying the availability of source code to every act of distribution. Its normative force rested on an implicit technical premise: that source code and object code stand in a well-defined, humanly auditable, and reproducible relationship. Large language models and, prospectively, Artificial General Intelligence (AGI) systems systematically violate this premise. The training artifacts jointly required to reconstruct a given model-code, data, weights, hyperparameters, toolchain, and hardware configuration-are each subject to independent legal, technical, and economic constraints that no current open-source framework fully resolves. Sufficiently capable AI systems can also rewrite licensed source into functionally equivalent derivatives stripped of their original obligations, a form of laundering against which copyleft has no effective defense. This paper argues that a functional analogue of copyleft for AGI must be grounded not in share-alike clauses over code, but in reproducible builds: a practice guaranteeing bit-exact reconstructability from declared inputs. We review the history and logic of copyleft, critically examine Maffulli's Second Liberation thesis according to which AI fulfills Stallman's dream, and show that the argument collapses unless AGI systems are themselves reproducible. Drawing on the Open Source AI Definition (OSAID), the Model Openness Framework (MOF), OpenMDW, and deterministicinference research by Thinking Machines Lab, SGLang, and others, we define seven requirements for AGI-oriented reproducible builds. We further argue that the Model Context Protocol (MCP) and analogous AIto-AI coupling mechanisms constitute a new dynamic linking layer for which copyleft-style licensing is ill-suited, and that Masnick's "protocols, not platforms" framework offers a more promising governance template for the AI linking layer.

---

## uid: `doi:10.2139/ssrn.6927344`

- title: AI Labor-Displacement News and the Reallocation of Coder Employment
- authors: Laurentiu Guinea
- affiliations: not stated
- posted: 2026-06-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6927344
- keyword hits: generative ai, large language model, large language models

### abstract

Debate about the labor-market effects of generative AI has focused on whether employment is declining in highly exposed occupations. This paper asks a different question: when AI labor-displacement news rises, where is employment reallocated within those occupations? We study coding-intensive occupations, a natural laboratory because computer programming is one of the most prominent applications of large language models and because coders are employed across a wide range of sectors. We construct a newspaper-based AI labor-displacement index and combine it with a destination-share framework that compares the actual allocation of coder employment across industries to an industry-growth counterfactual. We then compare coders to a low-exposure comparison group defined as the bottom employment-weighted quintile of AI exposure. Higher AI labor-displacement news is associated with a coder-specific medium-run reallocation away from core tech and toward strategic sectors, relative both to the industry counterfactual and to the low-exposure comparison group. In quarterly pooled coderversus-comparison-group cumulative local projections, a one-standard-deviation increase in the standardized, smoothed AI labor-displacement index raises the detrended strategic-minus-core rotation measure by about 0.31 percentage points more for coders than for the comparison group over quarters 4 through 6, and the joint null of no effect over that window is rejected. Core-tech destinations decline in the medium run, strategic destinations rise with a lag, and destination concentration falls. The evidence suggests that the early labor-market effects of generative AI are better understood as sectoral reallocation within exposed occupations than as immediate aggregate employment collapse.

---

## uid: `doi:10.2139/ssrn.6898283`

- title: The Cartesian Machine Perception, Emergence, and the Illusion of Control
- authors: Tudor Mitranescu
- affiliations: not stated
- posted: 2026-06-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6898283
- keyword hits: large language model, large language models

### abstract

This essay argues that the persistent epistemic failures of contemporary artificial intelligence-hallucination, brittleness, adversarial vulnerability, and the incapacity for genuine understanding-are not engineering deficiencies but structural consequences of a Cartesian philosophical framework that has shaped computational research since its inception. Tracing the intellectual genealogy from Descartes' mechanistic philosophy through the Von Neumann architecture, symbolic AI, and large language models, the essay demonstrates that each successive AI paradigm has inherited rather than transcended the foundational assumptions of disembodied representationalism: that intelligence consists in the formal manipulation of context-independent symbols, that knowledge can be exhaustively formalised, and that mind is separable from embodied, situated engagement with the world. Drawing on phenomenology, hermeneutics, Buddhist and Daoist philosophy, Indigenous epistemologies, systems theory, virtue ethics, and the capabilities approach, it constructs a post-Cartesian framework in which cognition is understood as irreducibly embodied, enacted, and intersubjective. The essay concludes with implications for AI governance-including the EU AI Act's humanin-the-loop requirements, the risk of 'virtue drift' in professional legal and judicial contexts, and the need for technomoral virtue cultivation alongside regulatory compliance. Written as a philosophical prolegomena to a subsequent legal study of AI governance, the essay establishes the interpretive coordinates through which current AI regulation may be critically and constructively assessed.

---

## uid: `doi:10.2139/ssrn.6923109`

- title: Regime-Aware Multi-Scale Attention-RNN for Financial Time-Series Forecasting: Bridging Hybrid Architectures and Foundation Models
- authors: Vishnu Vardhan Reddy Yeruva
- affiliations: not stated
- posted: 2026-06-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6923109
- keyword hits: foundation model, llama

### abstract

Financial time-series forecasting remains one of the most challenging applications of deep learning due to non-stationarity, regime shifts, and low signal-to-noise ratios. While hybrid attention-RNN architectures have demonstrated superiority over pure Transformers on financial benchmarks, existing models apply uniform attention mechanisms regardless of prevailing market conditions, failing to adapt to the fundamentally different dynamics of bull, bear, and crisis regimes. Simultaneously, recent time-series foundation models (TimesFM, Chronos, Lag-Llama) have shown poor zero-shot performance on financial data, with R² values as low as −2.80% and directional accuracy below 50%. This paper introduces RAMAR (Regime-Aware Multi-scale Attention-RNN), a novel architecture that addresses both limitations through four innovations: (1) a regime detection module using Hidden Markov Models to classify market states in real-time; (2) regime-conditioned attention whose scoring functions, temperature, and weight distributions explicitly adapt to detected market regimes; (3) cross-frequency fusion attention that dynamically aligns daily technical indicators with monthly macroeconomic releases and quarterly fundamental data from Crunchbase; and (4) multi-horizon output heads producing simultaneous 1-day, 5-day, and 20-day forecasts with regime-conditioned temporal scale selection. Evaluated on S&P 500 constituents (2010–2025), RAMAR achieves RMSE of 0.0128, R² of 0.962, and directional accuracy of 62.4%—reducing RMSE by 17.9% over TFT [1] and 16.9% over MCI-GRU [5], while outperforming zero-shot TimesFM by 58.9%. Regime-specific analysis reveals RAMAR’s largest advantage during bear markets and crisis periods, where standard models degrade most severely. Ablation studies confirm that regime-conditioned attention alone accounts for 37.2% of total improvement, while cross-frequency macro fusion contributes an additional 18.4%.

---

## uid: `doi:10.2139/ssrn.6898581`

- title: Version-Snapshot Stability of an AI-Presence Consistency Score
- authors: Pablo Ulpiano Gonzalez Castro
- affiliations: not stated
- posted: 2026-06-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6898581
- keyword hits: gpt-4, gpt-5

### abstract

The AIAS™ (AI Availability Score) program operationalizes AI Availability as a measurable brand-growth layer alongside Mental and Physical Availability. Its Consistency component is presently scored by CPC = 1/(1+CV), the coefficient-of-variation transform locked in methodology version v1.7. v1.7 established that this score is not a mean-independent consistency construct — it is mechanically coupled to recall level (|ρ| with Presence = 0.77) — and did not adopt it; a mean-independent redefinition was escalated to v1.8. The present study sets construct validity aside to ask a logically prior question: is the v1.7 score even version-stable? A measure that moves with the model vintage on which it is taken cannot track a brand across time, whatever its construct status. A pre-registered two-arm design measured CPC on a fixed 24-brand automotive registry under two model-version snapshots — an older vintage and the current frontier — across a six-model panel, holding probe wording, registry, and frame battery identical and varying only the dated model identifier; the contrast was made deliberately maximal across model generations. Brand-mention extraction reused the prior coder verbatim (pre-registered); a pre-scoring spot-check confirmed symmetric extraction across arms. Rank-order stability cleared the registered threshold marginally (Spearman ρ = 0.708) but proved fragile under a pre-registered leave-one-provider-out analysis (ρ ranging 0.48–0.82), with instability concentrated in the gpt-4o→gpt-5.x jump. Magnitude stability was falsified (mean |ΔCPC| = 0.077, exceeding the 0.5·SD tolerance of 0.069), though with no net directional drift — version change reshuffles which brands read as consistent without shifting the overall level. The emerging-brand instability prediction was falsified: no brand crossed the recall floor between arms. The v1.7 CPC score is therefore at best partially and provider-dependently version-stable; version-fragility compounds the recall-coupling already identified in v1.7 as grounds for the v1.8 redefinition. The contribution is a characterization of the interim instrument, not a validation of it.

---

## uid: `doi:10.2139/ssrn.6844478`

- title: The Archimedean Shadow: The Real Line as Quotient Structure in the Plenum Field A Companion Note
- authors: Kenneth Reidbord
- affiliations: not stated
- posted: 2026-06-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6844478
- keyword hits: claude, deepseek

### abstract

This note records a structural consequence of the Plenum Field quotient theorem established in Reidbord (2026b). In that construction, the standard part map st: F_fin-> R is a surjective ordered-ring homomorphism with kernel I(F), yielding R ≅ F_fin / I(F). It follows that, within the Plenum framework, the real line is quotient-derived rather than quotientterminal: it appears as the Archimedean residue of a richer non-Archimedean structure after collapse of the infinitesimal ideal. This observation does not prove, refute, or alter the Continuum Hypothesis or the Goedel-Cohen independence results. It instead concerns the relational placement of R inside the Plenum framework: the real line remains the complete Archimedean ordered field, but it is no longer the final continuum horizon of that framework. AI Disclosure. AI systems, including Claude, DeepSeek R1, and GPT, were used as drafting, formalization, adversarial review, and precision-checking tools during the development of this note. The author is responsible for all mathematical claims, interpretations, and errors. 1. Purpose and Scope This note is a companion to the Plenum Field paper (Reidbord 2026b). It does not introduce a new Plenum construction. Its purpose is to isolate a structural consequence of the quotient theorem proved there. The consequence is this: within the Plenum framework, the real line R is not quotient-terminal. It is the Archimedean quotient of a richer non-Archimedean structure. This note states that observation precisely, proves it from the quotient theorem, and notes what it does and does not imply for the Continuum Hypothesis. No claim is made that CH is resolved, that the Plenum is the true continuum, or that prior foundational frameworks are defective. The scope is limited to what the Plenum quotient theorem directly implies about the relational placement of R within that framework.

---

## uid: `arxiv:2606.15031v2`

- title: Partial Identification from LLM Prompts
- authors: Xiaohong Chen, Ashesh Rambachan, Elie Tamer
- affiliations: not stated
- posted: 2026-06-13
- source: arXiv
- link: https://arxiv.org/abs/2606.15031v2
- keyword hits: large language model, large language models, llm

### abstract

Large language models are increasingly used as binary classifiers when the true label is latent. We study partial identification of the prevalence $θ= P(X^* = 1)$ from panels of LLM reports whose errors may be arbitrarily dependent given the truth. The design of replication determines the observable, and hence the identifying content: repeated prompts to one model yield a count, several named models a response vector, and both a response matrix. Cast as a two-component finite mixture, the problem makes the identification failure transparent: absent restrictions that separate the latent components, the prevalence $θ$ is completely unidentified, and weak stochastic-ordering restrictions (first-order dominance, monotone likelihood ratio, mean ordering) leave the identified set at $[0,1]$. Identifying power comes instead from externally calibrated scores and events, which discipline the mixture in the spirit of the misclassification and corrupted-data literature. We characterize the resulting bounds, establishing validity and sharpness, and give an exact account of the identifying information in the full score distribution beyond its mean. When named models are asked repeated versions of the same question, what identifies $θ$ is not the number of positive answers but which models agree across prompts -- a feature a vote count discards. An extension derives implied bounds on regression coefficients when $X^*$ is a regressor of interest that is not directly observed.

---

## uid: `doi:10.2139/ssrn.6923198`

- title: Would You Trust a Doctor Who Uses ChatGPT?
- authors: Tinglong Dai
- affiliations: not stated
- posted: 2026-06-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6923198
- keyword hits: chatgpt, generative ai

### abstract

In this chapter, we examine what generative AI is doing to medicine. Drawing on a body of recent evidence, we argue that technical progress is necessary but not sufficient: even as models improve, the institutional scaffolding that absorbs them will decide whether that progress translates into trustworthy care. Visible AI use can lower peer and patient ratings of physicians. Liability and reimbursement pressures distort when and how AI is used. Sustained reliance can corrode the skills clinicians still need. Today's generative AI systems produce what is plausible, not what is feasible under hard constraints, and the agent frameworks built around them do not close that gap. The enthusiasm for AI as a substitute for clinical judgment is, at best, premature and, at worst, a category mistake. Better models will help, but only alongside the procurement, workflow design, local validation, and auditable governance that turn a technical artifact into a clinical instrument. In medicine, trust has always been institutional. The question is not whether to use AI, but whether the surrounding clinical system has made that use worthy of trust.

---
