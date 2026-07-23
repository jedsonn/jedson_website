# Classification batch 351 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-351.answer.json` as a JSON array.

---

## uid: `arxiv:2607.17181v1`

- title: Talaria: Session-Aware Serverless Serving of Hundred-Billion-Parameter LLMs
- authors: Utopia Meng, Unicornt Zhao, Derek Li, Goalen Gao, Frank Du
- affiliations: not stated
- posted: 2026-07-19
- source: arXiv
- link: https://arxiv.org/abs/2607.17181v1
- keyword hits: llm, llms

### abstract

Serverless multi-model LLM systems multiplex popularity-skewed model catalogs over shared GPU pools, yet typically schedule each request independently. Tool-using agents break this abstraction: a session repeatedly calls an LLM across short tool gaps, carries a long reusable KV prefix, and is judged by session completion time (SCT). Load-only routing can separate a continuation from both its model and KV state, while round-based model multiplexing can delay even a correctly placed continuation until the target model's next slot. Both failures are especially costly for hundred-billion-parameter models: their weights constrain residency, while long-context KV is expensive to reconstruct or move. We present Talaria, a session-aware serverless multi-model serving system that makes session continuity a joint placement-and-admission decision. Its router ranks placements by model residency, KV locality, and instance pressure, while soft reservations account for likely returns in the last serving instance's admission budget. Session-prefill (SP) admits budget-eligible continuations before the active model slot closes. An instance-local substrate keeps HBM addresses stable, preserves host-restorable KV, and stages weights across model switches. On a single TP=8 server, we replay 30 SWE-Bench model-sessions (960 calls) over three models, each with more than 100B total parameters. Against an otherwise identical round scheduler with SP, host-KV restoration, and D2D staging disabled, Talaria cuts p50 SCT from 1000 s to 189 s and p95 from 2296 s to 867 s, speedups of 5.3x and 2.6x.

---

## uid: `arxiv:2607.17112v1`

- title: Learning Dispute Structure for Settlement Prediction in Financial ADR: A Multi-Task and Cross-Institutional Approach
- authors: Koutarou Tamura
- affiliations: not stated
- posted: 2026-07-19
- source: arXiv
- link: https://arxiv.org/abs/2607.17112v1
- keyword hits: large language model, large language models

### abstract

This paper presents a unified dataset and modeling framework for financial alternative dispute resolution (ADR) cases collected from multiple Japanese ADR organizations. Each case consists of paired claims from the complainant and the respondent with a binary settlement outcome. We introduce a functional tagging scheme to represent dispute structures and propose a multi-task model that jointly performs dispute classification and settlement prediction. Experimental results show that incorporating dispute structure improves prediction performance, and large language models achieve comparable or superior performance in several domains. These findings suggest that dispute structures are partially shared across ADR domains.

---

## uid: `arxiv:2607.17070v1`

- title: Bridging the Information Gap: Semantic Densification and Hindsight Distillation for Cold-Start Prediction
- authors: Hao Duong Le, Yifei Gao, Huan Li, Lun Jiang, Chen Bai, Ke Xing, Chen Zhang
- affiliations: not stated
- posted: 2026-07-19
- source: arXiv
- link: https://arxiv.org/abs/2607.17070v1
- keyword hits: llm

### abstract

New-user cold-start is a critical bottleneck for e-commerce platforms: predicting user lifetime value (LTV) and conversion rate (CVR) for users with sparse interaction history. Two prior directions -- LLM-based semantic augmentation and learning using privileged information (LUPI) -- each face a key limitation. First, LLM augmentation produces unstructured rationales that are noisy and hard to operationalize in production. Second, naive student-teacher distillation can be brittle due to an information gap between the privileged teacher and the sparse student; moreover, this gap is heterogeneous across users. We propose SemRaD, a Semantic Reasoning-aware Distillation framework addressing both limitations. First, a Structured Semantic Reasoning Pipeline replaces free-form rationales with a structured schema built via a discover-curate-audit workflow, producing per user a Densified Semantic Profile (consumed by the deployed student via a Semantic-Gated Encoder that focuses on the most informative dimensions) and a Hindsight Distillation Target reconciled from pre- and post-conversion reasoning (used only at training). Second, to bridge this gap and handle its heterogeneity, a Hindsight-Aware Distillation Network transfers privileged knowledge via the hindsight target, with Distillation Experts improving transfer under per-user variability. On a large-scale industrial dataset, SemRaD lifts +1.9% LTV (Gini) and +1.0% CVR (AUROC) over a production-grade base; a four-week online A/B at Keeta confirms +1.0% LTV / +0.43% CVR. SemRaD also matches the production system's LTV using only 9% of the training data while improving CVR by 0.8%.

---

## uid: `arxiv:2607.17047v1`

- title: Solver-Hard Is Not Model-Hard: A Hardness-Controlled Diagnostic for LLM Constraint Reasoning
- authors: Lucky Verma
- affiliations: not stated
- posted: 2026-07-19
- source: arXiv
- link: https://arxiv.org/abs/2607.17047v1
- keyword hits: llm

### abstract

LLM constraint reasoners are often evaluated near the random-SAT phase transition, confounding density and solver hardness. We test instance-level transfer while near-matching clause density. At aligned size bins, with near-matched density and matched maximum clause width, we compare proof-hard expander-Tseitin and proof-easy ladder-Tseitin formulas, pigeonhole anchors, and density-mismatched controls. Theory separates their resolution hardness; a solver-specific Glucose mean-conflict proxy differs by up to $51\times$, and five other solvers preserve the direction. Across three included models (243 instances each; a fourth is excluded for abstention), the near-matched-density accuracy gaps range from $-32$ to $+20$ points, with a pooled gap of $+1.7$ points ($p=0.74$) and a wrong-signed correctness-versus-conflict association ($r=+0.15$). A proof-preserving relabeling lowers accuracy in all five clusters for one model (mean $-93$ points) but not another, exposing model-surface sensitivity. In a preregistered extension, provider-reported completion-token spend does not consistently increase with the proxy after accounting for formula length and censoring. At 16k, the reasoning model spends more on proof-easy matched formulas and exhausts its budget on the solver-easiest UNSAT family; the 32k C1 gap is absent. These scoped dissociations concern verdict accuracy and observed token spend, not certificate solving, exact proof length, or allocation efficiency.

---

## uid: `doi:10.2139/ssrn.7150539`

- title: Mechanical Responses of an AI-Hypothesized Super-elastic Fe-Mn-Al-Ni-Si-C Alloy
- authors: Frank Cai, Song Cai, Xiaoming Wang, Jie Yan
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7150539
- keyword hits: large language model, llm

### abstract

Iron-based shape memory alloys (Fe-SMAs) offer a low-cost alternative to Nitinol, but their super-elastic response is highly sensitive to composition and processing. Large language model (LLM) deep-research agents can now propose new alloy compositions in seconds, raising the question of whether such proposals actually work once synthesized. Here we report the synthesis and mechanical characterization of an LLM-hypothesized Fe-Mn-Al-Si-Ni-C composition, benchmarked against an established super-elastic Fe-Mn-Al-Ni alloy processed under identical conditions. The AI-hypothesized alloy was readily castable but failed to exhibit super-elasticity under any condition tested, deforming instead like a conventional elastic metal. Synchrotron X-ray diffraction showed that this failure stems from a phase-stability mismatch: the AI alloy forms a stable dual-phase microstructure with a minor ordered Fe-Al phase that does not support the transformation pathway the benchmark alloy relies on, likely promoted by its elevated carbon content. We conclude that LLM-proposed alloy compositions cannot be assumed to work as intended and should be screened for competing phase stability and interstitial content before physical synthesis is attempted.

---

## uid: `doi:10.2139/ssrn.7012638`

- title: Computational Simulation of Post-Capitalist Resource Allocation: A Multi-Agent LLM Model of the Value Consensus Currency
- authors: Paul-Henry Paltmann
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7012638
- keyword hits: llama, llm

### abstract

The historical "Socialist Calculation Debate" argued that decentralized market pricing is the only viable mechanism for resource allocation, yet the emergence of advanced artificial intelligence and algorithmic planning has reopened this discourse. This paper addresses the critical problem of how to computationally model a post-scarcity, moneyless economy-specifically the Value Consensus Currency (VCC) framework. To achieve this, we deploy a multi-agent simulation using the Llama-3.1-8b model as a proxy for boundedly rational socioeconomic actors. The simulation operates over a 100-epoch cycle across three distinct configurations: a balanced Baseline, a Climate Shock, and a Consumer Hegemony. Our results computationally suggest that while algorithmic resource allocation is mathematically stable under balanced demographic conditions, the system remains highly vulnerable to psychological heuristics. Without supreme, non-derogable ecological constraints (jus cogens), the simulated human-like short-term biases and unchecked consumption preferences of the agents consistently tend to trigger severe ecological degradation.

---

## uid: `doi:10.2139/ssrn.7008878`

- title: From Prediction to Discovery: A Review of Scientific Discovery with Foundation Models
- authors: Thomas Wang
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7008878
- keyword hits: foundation model

### abstract

Foundation models-large neural networks pre-trained on broad data with self-supervised objectives and adapted to many downstream tasks-have moved from natural-language processing into the empirical sciences, where they now predict protein structures, design materials and molecules, forecast the weather, prove mathematical conjectures, and drive autonomous laboratories. This review synthesizes the rapidly growing literature on foundation models as instruments of scientific discovery, as distinct from generic prediction. We propose a four-mode taxonomy that organizes the field: foundation models as (i) predictive surrogates that replace expensive simulation or experiment; (ii) generative designers that propose novel candidates in protein, molecule, and materials space; (iii) autonomous agents that plan, execute, and iterate experimental campaigns; and (iv) objects of discovery in their own right, whose learned internal representations encode latent scientific knowledge that interpretability can read out. We survey landmark systems across structural biology, single-cell and genomic biology, chemistry and materials science, the Earth sciences, and mathematics, and we give particular attention to the fourth mode-discovery from a model's internals-using recent work on single-cell transformers as a detailed case study. A recurring theme is that the scientific value of a foundation model depends less on raw predictive accuracy than on whether its outputs and internal mechanisms can be validated against external ground truth and causal experiment. We close with the central methodological challengeshallucination, leakage and contamination, benchmark saturation, and reproducibility-and argue that the next phase of progress will be defined by tools that turn predictive black boxes into auditable scientific instruments.

---

## uid: `doi:10.2139/ssrn.7148596`

- title: Social media and city branding in the age of AI: Longitudinal identity shifts, algorithmic amplification, and the experience dissonance spiral
- authors: Arshad Iqbal, Sohail Asghar
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7148596
- keyword hits: generative artificial intelligence

### abstract

Generative artificial intelligence is reshaping how cities construct and project brand identities across social media platforms. Despite scholarly attention to city branding, three empirical gaps persist: whether AI-generated city content produces measurable long-term shifts in resident place identity; whether platform recommendation algorithms exert a stronger causal influence on destination attribute salience than content quality; and whether the pathway from AI-inflated pre-visit imagery to post-visit reputational damage can be formally modelled. This study addresses all three gaps through a tripartite empirical design spanning Singapore (high AI adoption), Barcelona (intermediate), and Lahore (low). The design comprises: (1) a 24- month longitudinal panel survey (N = 1,812 residents, three waves) using the 24-item Place Identity Scale (PIS-24); (2) a cross- platform algorithmic audit of 36 sock-puppet accounts across TikTok, Instagram, and YouTube, yielding 241,920 recommendation observations; and (3) a five-stage recursive structural equation model estimated on 14,280 tourist data points with six- month post-visit sentiment tracking. High AI-adoption cities exhibit significant resident place identity decline (Cohen’s d = 0.41, p

---
