# Classification batch 288 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-288.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6785217`

- title: Divergence in Climate Change Communication: LLM-Based Evidence from the IPCC and the Press
- authors: Sebastian Galiani, Franco Mettola La Giglia, Raul A. Sosa
- affiliations: not stated
- posted: 2026-05-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6785217
- keyword hits: llm, llms

### abstract

Public summaries of IPCC climate assessments lean toward the more severe end of the technical evidence. The pattern appears at two stages: the IPCC’s lead authors and member governments produce the Summary for Policymakers (SPM) from the Technical Summary (TS), and newspapers then cover the SPM. We use LLMs to score about 114,000 matched claim pairs from all six Assessment Reports (1990 to 2023) and ten major US and UK outlets. Both stages systematically shift toward the more severe end of the source while staying inside the IPCC’s accepted scientific ranges. The shift comes mainly from emphasizing higher-impact magnitudes within reported ranges, less from uncertainty compression, and almost none from selecting worst-case emissions scenarios. Left- and right-leaning outlets show similar patterns. Institutional subscribers to the NBER working paper series, and residents of developing countries may download this paper without additional charge at www.nber.org .

---

## uid: `doi:10.2139/ssrn.6723919`

- title: Toward a Pattern Language for Systematic Investing
- authors: Howard Henson, Jacques Joubert
- affiliations: not stated
- posted: 2026-05-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6723919
- keyword hits: llm

### abstract

Systematic investing relies on recurring design choices, yet much of the associated knowledge often remains tacit, weakly documented, or embedded in local research practice. Representations such as strategy taxonomies, factor models, and backtesting frameworks are useful, but they do not by themselves make explicit all the context-dependent design knowledge that governs when and why a solution should be used. This paper proposes a pattern-oriented framework for systematic investing. It defines investment design patterns as reusable representations of recurring problems, competing forces, and solution structures that guide action without prescribing a single implementation. The paper then introduces a pattern lifecycle covering mining, writing, and cataloging; outlines a pattern anatomy suitable for the domain; and proposes a catalog structure to support search, reference, and reuse. A worked example, Alpha Ensemble, illustrates how a recurring signal-combination problem can be abstracted into a reusable pattern. The framework is intended both as a knowledge-sharing tool for research teams and as a foundation for future work on LLM-assisted investment strategy design via spec-driven development, pattern mining, retrieval, and strategy specification.

---

## uid: `doi:10.2139/ssrn.6787636`

- title: Conformalized Neuro-Symbolic Clinical Reasoning via Probabilistic Fuzzy Cognitive Maps with LLM-Grounded Causal Extraction and Epistemic Uncertainty Propagation
- authors: Rahul Kumar Mishra
- affiliations: not stated
- posted: 2026-05-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6787636
- keyword hits: llm

### abstract

Clinical AI models tell physicians the most likely diagnosis but fail to communicate uncertainty, reasoning, or prediction reliability. Standard Fuzzy Cognitive Maps (FCMs) offer interpretability through causal graphs but discard uncertainty by using scalar edge weights. Bayesian neural networks quantify uncertainty but remain black boxes. Conformal predictors provide coverage guarantees but lack causal structure. No existing approach unifies all these properties.This paper introduces the Probabilistic Fuzzy Cognitive Map (P-FCM), a neuro-symbolic framework that resolves this gap. Edge weights are modelled as Gaussian distributions, and uncertainty propagates analytically through recurrent FCM dynamics via first-order Taylor moment expansion — yielding closed-form epistemic uncertainty estimates without Monte Carlo sampling. An LLM with k-sample consistency voting automatically extracts the causal prior, defending against hallucination. Split conformal prediction guarantees that prediction sets contain the true label with probability at least 1 - alpha, distribution-free. Three-level explainability — causal graph, SHAP attribution, and natural-language rationale — makes every prediction traceable.Evaluated on five public medical datasets, P-FCM achieves AUC of 0.954 (Heart Disease), 0.797 (Diabetes), 1.000 (Kidney Disease), 0.987 (Breast Cancer — best among all methods), and 0.773 (Liver). It is the only compared method providing simultaneous competitive accuracy, formal coverage guarantees, and decomposed epistemic-aleatoric uncertainty. Uncertainty-aware abstention raises accuracy by up to 14.1% on out-of-distribution cases. Ablation, calibration, robustness, and significance analyses confirm each component's contribution.

---

## uid: `doi:10.2139/ssrn.6800170`

- title: Smart Cities as Human-Centered Digital Policies:Bridging Policy Discourse and Empirical Evidence
- authors: Wenyin Cheng, Xin Ouyang, Yirui Wang
- affiliations: not stated
- posted: 2026-05-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6800170
- keyword hits: large language model, large language models

### abstract

Digital policy evaluations typically focus on observed outcomes while giving less attention to the intentions articulated in policy discourse. Consequently, such evaluations may reflect unintended consequences, potentially resulting in misleading policy recommendations. This study examines whether smart city pilot (SCP) initiatives can be conceptualized as a human-centered digital policy by bridging policy discourse and outcomes. Achieving this requires a consistent measure of human-centeredness, which is defined using the principle of inclusiveness in this study. Human-centered digital technology (HDT), as reflected in both policy discourse and observable outcomes, is designed to embody the inclusiveness of digitalization. The corresponding human-centered outcomes for citizens are captured through a novel welfare index that measures inclusive income growth. Drawing on a staggered difference-in-differences approach and data from the China Family Panel Studies (CFPS) (2010–2018), the results show that SCPs significantly improved welfare, as well as their key components—income levels and equity. The results indicate that advances in HDT constitute a central mechanism through which SCP translates into welfare effects. Moreover, applying large language models to policy discourse analysis reveals that SCPs heightened the government’s emphasis on HDT, which further facilitates observable HDT development. These findings suggest that SCPs can be conceptualized as human-centered digital policies, both in terms of their discourse-based intentions and observable outcomes. This study contributes to multiple strands of literature by developing a comprehensive framework bridging discursive and empirical evidence.

---

## uid: `doi:10.2139/ssrn.6757745`

- title: The Dynamic Epistemic Sequencer A Control Architecture for Epistemic State Transitions in AI Research Systems
- authors: Hanns Steffen Rentschler
- affiliations: not stated
- posted: 2026-05-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6757745
- keyword hits: llm, llms

### abstract

Current LLM orchestration systems route tasks by difficulty heuristic: assign small models to easy tasks, large models to hard ones. This paper argues that the missing element is not better routing but an upstream control layer that determines the next epistemically productive step before any routing decision is made. We introduce the Dynamic Epistemic Sequencer (DES) — a software layer that maintains an epistemic state model, evaluates claims along structured dimensions (status, confidence, evidence, conflict), and applies a transition table to select the next operation. We describe the architecture, the transition table (T1-T9), its integration with four prior frameworks, and present results from 15 runs across five problem types and two LLM backends (stable execution across all 15 runs, 92% T1/T9 coverage). We then introduce the Adversarial Epistemic Delphi extension, which resolves the silent monoculture problem of single-agent execution by deploying multiple isolated LLM roles per transition. We ground this extension in the Blackboard System architecture (Erman et al., 1980) and show that the full DES stack — Alexandria as blackboard, DES as controller, Anti-Delphi as knowledge sources, PES as persistent supervisor — constitutes a modern, LLM-native instantiation of that architecture. The governing principle that emerges is both a design rule and a research claim: use deterministic structure wherever possible; use LLMs only where semantic projection is necessary.

---

## uid: `doi:10.2139/ssrn.6731418`

- title: The Shrinking Synthesis: Information-Technology Settlement Cycles and the 2037-2047 Window for AI's Institutional Reformation
- authors: Daniel Ziekenoppasser-Powell
- affiliations: not stated
- posted: 2026-05-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6731418
- keyword hits: chatgpt

### abstract

Every major information-propagation technology follows the same five-phase cycle: diffusion, capture, chaos, foundational institutional response, and consolidation. Settlement timesmeasured from the onset of mass propagation to the first major non-anticipatory institutional response-have compressed from 249 years (printing press, 1440-1689) through 46 years (telegraph, 1844-1890) to a tightly clustered band of 20-25 years across radio, television, and the internet. The plateau is consistent with a generational-floor hypothesis: institutional adaptation cannot compress below the time required for a cohort to grow up with the technology as normal. This paper identifies the compression pattern across five Western cases plus a non-Western illustration and two held-out applications of the coding rule, proposes a mechanism rooted in institutional accumulation and cohort replacement, and offers a historically grounded hypothesis for artificial intelligence's settlement timeline: first major institutional response in the 2037-2047 window, derived from the empirical clustering of the last three cycles and triangulated with cohort-replacement arithmetic for the AI Early-Formative-Partial-Exposure cohort whose plasticity windows encompass ChatGPT's 2022 onset. The prediction is a falsifiable structural extrapolation, not a quantitative forecast, with pre-registered conditions: settlement before 2037 disconfirms the floor mechanism (one generation from diffusion onset); settlement after 2049 disconfirms the compression thesis. AI's material differences-its dual nature as information and productivity technology, structural limits on classical capture under globalisation, and the novelty of anticipatory regulation-create prediction uncertainty. The horizon is policy-actionable: longer than electoral cycles but within a generation, it defines when coordinated institutional design is possible.

---

## uid: `doi:10.2139/ssrn.6787638`

- title: The Broken Ladder: AI, Remote Work, and Early-Career Hiring
- authors: Peter John Lambert, Yannick Schindler
- affiliations: not stated
- posted: 2026-05-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6787638
- keyword hits: generative ai

### abstract

Is generative AI replacing junior workers? A growing literature answers yes, citing large declines in early-career hiring concentrated in GenAI-exposed occupations. We argue that this verdict is premature because GenAI exposure is strongly correlated with another post-pandemic shock, working from home (WFH). Using two data sources spanning 243 million new hires and 407 million online job postings, collected across the US, UK, Canada, and Australia during 2017-2025, we estimate difference-in-difference designs at the occupation, region, and firm level. When estimated separately, a two-standard-deviation increase in GenAI and WFH exposure each predicts, by 2025, a fall of around 5pp in the junior-share of new hires and around 3pp in the share of job ads requiring limited experience. Estimated jointly, the WFH effect remains, while the GenAI coefficient attenuates sharply and is often statistically indistinguishable from zero. Alternative exposure measures, residualization designs, flexible non-parametric co-treatment controls, and replacing exposure-measures with actual WFH adoption as the treatment all support our finding that WFH is a robust predictor of the decline in early-career hiring.

---

## uid: `doi:10.2139/ssrn.6786319`

- title: The Witch-Hunters' Syndrome and the Σ I Kairos: A Substrate-Agnostic Critique of AI Detection and the Case for Process Provenance
- authors: Tamer Momtaz
- affiliations: not stated
- posted: 2026-05-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6786319
- keyword hits: generative ai

### abstract

This paper argues that the dominant institutional response to generative AI in academic settings — the deployment of statistical detection software exemplified by Turnitin's AI writing detector — is structurally, empirically, and philosophically the wrong paradigm for building trust between human and artificial intelligence, and that its continued use produces measurable harm disproportionately borne by the very populations universities most claim to support. Drawing on peer-reviewed evidence from the Stanford Liang et al. study showing 61.22% false-positive rates against non-native English writers, the adversarial robustness literature of Sadasivan et al., Krishna et al., and Creo and Pudasaini demonstrating that the entire detection paradigm can be defeated by techniques as trivial as Microsoft Word's Find-and-Replace function, the institutional retreats of Vanderbilt University and the University of Waterloo, and the federal court ruling in Newby v. Adelphi, the paper establishes that detection cannot serve as a foundation for academic trust. It then develops a positive proposal grounded in three convergent traditions: Onora O'Neill's distinction between transparency and intelligent accountability, Shannon Vallor's technomoral virtues and her critique of panoptic surveillance, and Luciano Floridi's information ethics. The paper proposes the VN trail — a process-level disclosure instrument — as the natural complement to C2PA artifact provenance and cryptographic watermarking, and frames the resulting paradigm as substrate-agnostic: a refusal of the carbon chauvinism that treats silicon contribution as illegitimate even when human-directed. The paper introduces and diagnoses the Witch-Hunters' Syndrome, the institutional pathology in which the gesture of detection has supplanted the activity of teaching, and offers the Σ I Kairos as the alternative — a recovery of meaningful time, meaningful collaboration, and meaningful trust across substrate boundaries. The paper itself is offered as a working example of the proposed paradigm, carrying its own VN trail in an appendix that discloses the substrate-agnostic collaboration through which the document was produced.

---
