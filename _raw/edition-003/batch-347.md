# Classification batch 347 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-347.answer.json` as a JSON array.

---

## uid: `arxiv:2607.13477v1`

- title: Auditing Protocol-Level Shortcuts in Large Audio Language Model Judges for Speech Evaluation
- authors: Joonyong Park, David M. Chan, Yuki Saito, Hiroshi Saruwatari
- affiliations: not stated
- posted: 2026-07-15
- source: arXiv
- link: https://arxiv.org/abs/2607.13477v1
- keyword hits: qwen

### abstract

Large audio-language models (LALMs) are increasingly used as automatic judges for speech evaluation. However, high agreement with human ratings does not guarantee that their verdicts are grounded in the audio. A judge may instead rely on specialist labels or reference data supplied by the evaluation protocol itself, taking a shortcut in place of listening to the audio. In this paper, we audit such protocol-level ``shortcuts'' in LALM judges across three common deployment protocols: feature-blueprint judging, where the audio is replaced by a structured text description of acoustic features, reference-conditioned judging, and pairwise A/B comparison. Across six judges and four attributes, we find that several LALMs rely on protocol-level shortcuts. For example, in feature-blueprint judging, incorrect specialist labels reduce five judges' emotion accuracy to 0.10 or below, and in concatenated A/B comparisons, Qwen3-Omni-Thinking often picks the same slot regardless of order swaps. These results indicate that aggregate agreement can overstate the validity of LALM judges unless the model and the evaluation protocol are assessed jointly, and that each model-protocol pair should be evaluated with a matched shortcut probe.

---

## uid: `doi:10.2139/ssrn.6978498`

- title: FLEX-MoE: Failure-Born Orthogonal Experts for Self-Improving Language Models
- authors: Alessio Rocchi
- affiliations: not stated
- posted: 2026-07-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6978498
- keyword hits: qwen

### abstract

When a deployed language model keeps making the same mistakes, FLEX-MoE grows a new, removable expert for them instead of retraining shared weights. A frozen base model captures its own verifier-checked failures, clusters the recurring ones, and trains one external LoRA expert per cluster-with no task labels and no fixed expert inventory. Each expert is born in the subspace orthogonal to the activations the base already uses correctly, which gives an auditable preservation target before anything is deployed. On a controlled arithmetic benchmark, failure-born experts significantly improve heldout accuracy over frozen Qwen2.5 backbones (paired test p ≈ 0.007 on the 1.5B model; marginal on the 3B, over five seeds), the repair signal transfers to a second, non-arithmetic verification domain, and the orthogonal projection preserves accuracy while its leakage reduction follows the projector's energy threshold by construction. For deployment we adopt a realistic boundedregression criterion rather than demanding exactly zero regressions: a risk-certified routing gate then yields a positive result on three held-out seeds-+3.4 heldout points at ∼ 24% expert coverage with zero base-relative regressions-whereas stricter zero-regression gates collapse to the frozen base. We frame self-improvement as failure-born capacity, structural preservation, and a local deployment certificate, and give a benchmark for the last.

---

## uid: `doi:10.2139/ssrn.6970159`

- title: Inflation Targeting in the Time of Supply Shocks: A Large-Language-Model Reading of India's Reserve Bank, 1997-2025
- authors: Dr. Sridevi Tandley Omprakash, Karan Singh Bagavathinathan
- affiliations: not stated
- posted: 2026-07-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6970159
- keyword hits: large language model, llm

### abstract

India's Phillips curve has looked at the familiar missing relationship across 1997-2025, a period that spans the 2016 adoption of flexible inflation targeting and is dominated by recurrent supply shocks. We ask whether that flatness survives once demand and supply disturbances are separated and whether the Reserve Bank of India's own account of each quarter agrees. We measure the demand supply split three ways: a mechanical inflation with output-gap co-movement rule; a gap-blind reading of the Reserve Bank's quarterly assessments by a large language model (LLM) under a fixed, pre-specified protocol; and the Bank's revealed practice. The pooled output-gap slope is statistically zero, but this is an artefact of pooling disturbances: conditioning on the shock, the demand-pull slope is +2.2 before targeting and switches off to zero after it, while the supply-driven (cost-push) slope stays negative throughout the signature of a central bank that offsets demand before it reaches prices. Read independently of the gap, the language model recovers the same regime contrast, reading 77 of 115 quarters as supply-led with demand a frequent co-driver; three independent model families agree on the classification (Fleiss κ = 0.45). The paper's contribution is to identify which channel flattened, and to scale the narrative identification of supply and demand shocks with a hybrid design that leaves the econometrics classical and uses the language model only to read the policy record at scale.

---

## uid: `doi:10.2139/ssrn.7111158`

- title: Fuzzy and Configurational Approaches to Generative-AI Adoption: A UTAUT2 Systematic Review
- authors: Ricardo Abreu
- affiliations: not stated
- posted: 2026-07-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7111158
- keyword hits: generative artificial intelligence

### abstract

Generative artificial intelligence (GenAI) has rapidly moved from novelty to an everyday tool, and understanding why individuals adopt it has become a central concern for management and information-systems research. The dominant framework for this inquiry, the extended Unified Theory of Acceptance and Use of Technology (UTAUT2), is typically estimated using linear, variable-centred methods that report the average effect of each antecedent. A smaller but growing body of work instead applies fuzzy-set and configurational techniques, which treat adoption as arising from combinations of conditions rather than from independent drivers. This review synthesises that body of work. Following PRISMA 2020, we searched five databases and identified seventeen empirical studies that pair UTAUT2 with a fuzzy or configurational method across GenAI and adjacent technologies, appraising each with the Mixed Methods Appraisal Tool. Three findings recur. First, performance expectancy and hedonic motivation are the most reliable predictors of adoption intention, whereas effort expectancy and social influence are markedly context-dependent. Second, facilitating conditions and habit relate more strongly to actual use than to intention, suggesting they operate at the stage where decisions become behaviour. Third, the configurational studies show that high adoption is achieved through several distinct and substitutable antecedent combinations rather than a single dominant path. Together, these results indicate that UTAUT2’s explanatory value is conditional on the analytical lens and context, and that fuzzy and configurational methods reveal equifinal, asymmetric adoption patterns that linear models leave hidden. We outline the implications for how GenAI adoption should be modelled

---

## uid: `doi:10.2139/ssrn.6971298`

- title: Navigating AI Privacy Governance: The KITE Framework for Program Management in Technology Organizations
- authors: Ali Muzaffar
- affiliations: not stated
- posted: 2026-07-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6971298
- keyword hits: generative ai

### abstract

Privacy governance in AI-intensive organizations has evolved into a complex operational discipline that existing normative and regulatory frameworks insufficiently address at the practitioner level. This paper presents the KITE framework-comprising Knowledge, Influence, Transparency, and Empathy-as a practitioner-derived model for operationalizing privacy program management in AI product development environments. Developed inductively through three years of direct experience managing over 1,200 AI and product privacy reviews per month, KITE identifies twelve numbered sub-practices (K1-K3, I1-I3, T1-T3, E1-E3) that form a comprehensive program management methodology. The paper demonstrates KITE's operational value through a generative AI enterprise connector feature scenario-modeled on a dynamic, user-configured data integration product-presenting a phase-by-phase execution model and a risk exposure matrix showing root-cause analysis and mitigation across eight critical risk categories. KITE is mapped to NIST CSF 2.0, IEEE Ethically Aligned Design v2, GDPR, and the EU AI Act.

---

## uid: `doi:10.2139/ssrn.6990818`

- title: Distributed Deep Learning and Intelligent Soil-Water Analytics in Precision Agriculture: A Comprehensive Review
- authors: Polina Lemenkova
- affiliations: not stated
- posted: 2026-07-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6990818
- keyword hits: foundation model

### abstract

Efficient management of soil-water resources is critical for global food security under intensifying climatic and demographic pressures. This review provides a comprehensive synthesis of artificial intelligence (AI) and distributed deep learning methodologies applied to soil-water interactions in precision agriculture. The physical and hydraulic foundations of soil-water systems-including water retention, unsaturated flow governed by the Richards equation, and soil degradation processes-are examined and situated within a unified framework of AI-based modeling and decision support. Classical machine learning (ML) algorithms (Random Forests, Support Vector Machines, gradient boosting) and deep learning architectures (convolutional neural networks, long short-term memory networks, transformers) are evaluated with respect to their capacity to predict soil moisture dynamics, estimate hydraulic properties, support smart irrigation scheduling, and generate digital soil maps at field-to-regional scales. Distributed training paradigms, federated learning for privacy-preserving multi-farm analytics, and edge AI deployment on low-power IoT hardware are assessed as enabling infrastructures for scalable agricultural intelligence. This review further addresses explainability, uncertainty quantification, and ethical dimensions inherent to AI-driven agricultural systems. Key challenges-including training data scarcity in data-poor regions, model interpretability, integration with physics-based hydrological models, and real-time deployment constraints-are critically discussed. Prospective research directions encompass physics-informed neural networks, foundation models for earth observation, autonomous digital twins of soil-water systems, and federated learning architectures aligned with data sovereignty frameworks. The synthesis underscores AI's transformative potential for sustainable agricultural water management while delineating the technical and sociotechnical barriers that must be resolved to realize this potential at a global scale.

---

## uid: `arxiv:2607.14713v1`

- title: Does Multi-Agent Debate Improve AI Feedback on Research Papers?
- authors: Tomas Havranek, Zuzana Irsova
- affiliations: not stated
- posted: 2026-07-16
- source: arXiv
- link: https://arxiv.org/abs/2607.14713v1
- keyword hits: gemini

### abstract

Probably not, at least for meta-analyses in economics. In a pre-registered, identity-masked, within-paper experiment, the authors of 44 meta-analyses ranked three AI reports on their own paper by usefulness for improving it: a single pass by a frontier model against two multi-agent debate tools we built and expected to win. All reports were held to a common length and template. The authors preferred the single pass, by 0.66 rank points over mad-research (95% CI 0.32 to 1.00) and 0.57 over paper-workshop (0.16 to 0.95), though paper-workshop spent roughly thirty times the tokens. Authors who recalled their journal referee report usually placed it first and never last; in a separate exercise, three AI judges almost always placed the real journal referee report last. Among the three AI reports, Gemini (the judge whose model family wrote none of the reports) would have ranked paper-workshop first in the authors' place, reversing the single-pass preference. The reversal warns against substituting an AI judge for the author. We measure perceived usefulness for finished papers; whether AI should referee papers is a separate question.

---

## uid: `arxiv:2607.15079v2`

- title: BrainPilot: Automating Brain Discovery with Agentic Research
- authors: Haoxuan Li, Tianci Gao, Jianhe Li, Yang Fan, Runze Shi, Weiran Wang, Tianxiang Zhao, Zezhao Wu
- affiliations: not stated
- posted: 2026-07-16
- source: arXiv
- link: https://arxiv.org/abs/2607.15079v2
- keyword hits: agentic, ai agent

### abstract

Understanding the brain increasingly depends on integrating evidence across scales, modalities, and disciplines. Addressing a single research question therefore requires a coordinated sequence of operations, from surveying prior work to executing analyses and interpreting results in light of domain knowledge. AI agents promise to accelerate this process, but current agents lack domain expertise in brain science, may fabricate claims, drift during multi-step reasoning, and offer few defined points for expert intervention. These failures are especially costly in brain science, where conclusions feed into downstream scientific claims and depend on laboratory-specific expertise and careful human judgment. We present \textbf{BrainPilot} a \textbf{fully open-source} multi-agent system that accelerates brain science research with traceable logs and agent-verified results. A principal investigator (PI) agent coordinates specialist agents grounded in curated domain knowledge: a unified brain science knowledge base containing 7{,}233 indexed items and a skill library of 72 reusable methodology units across seven research domains. Every major step is recorded in the Graph of Trace, an auditable record that links subgoals, tool use, evidence, and claims and allows researchers to follow and inspect the workflow. An Auditor agent further integrates fabrication checking into the workflow. For evaluation, we run three brain science tasks from Agents' Last Exam, introduce our own benchmark, \textbf{BrainPilotBench-v0}, and present additional end-to-end case studies. Across these evaluations, BrainPilot with an open-source backbone model attains performance comparable to state-of-the-art agent framework with less costs.

---
