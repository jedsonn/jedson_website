# Classification batch 58 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-58.answer.json` as a JSON array.

---

## uid: `arxiv:2607.13305v1`

- title: Accuracy Without Grounding: Diagnosing Visual Dependency Dissociation in Video LLM Benchmarks
- authors: Jae Joong Lee
- affiliations: not stated
- posted: 2026-07-14
- source: arXiv
- link: https://arxiv.org/abs/2607.13305v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Benchmark accuracy in video large language models (LLMs) is often treated as evidence of visual understanding. We audit this assumption across twenty models spanning 2-78B parameters and ten architecture families. We introduce the Visual Dependency Gap (VDG), the difference in per-question correctness between original-video and black-screen conditions. Paired McNemar tests on MVBench show that accuracy and visual dependency are separable: models differ on original video (p = 0.0003) but not on black screens (p = 0.53). Across models, task-type rankings are stable: Attribute Perception is strongly visual, whereas Temporal Reasoning approaches the language-only baseline. A diagnostic ladder from black screen to single frame, shuffled frames, and original video reveals that frame diversity supplies most of the visual benefit, while temporal order contributes near-zero accuracy across sixteen open-weight models. An ablation from 0.5 to 24 FPS rules out sparse sampling as the cause. H.264 experiments further show that stable aggregate accuracy conceals bidirectional question-level answer flips. The diagnostic also generalizes to four API-accessed models, whose VDG values range from 0.025 to 0.315. These results motivate VDG as a standard audit for whether video benchmarks measure visually grounded capability. Code is available at https://github.com/JaeLee18/accuracy-without-grounding.

---

## uid: `arxiv:2607.12723v1`

- title: Bulkhead: Automated Semantic Detection and Remediation of Container Escape Vulnerabilities
- authors: Qiyuan Fan, Zhi Li, Junjie Li, XiaoFeng Wang, Bin Yuan, Deqing Zou
- affiliations: not stated
- posted: 2026-07-14
- source: arXiv
- link: https://arxiv.org/abs/2607.12723v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Filesystem isolation in container ecosystems is often weakened by cross-boundary path misresolution, causing path traversal (PaTra) vulnerabilities. These vulnerabilities stem from insecure host-container interactions and have become increasingly pervasive as cloud systems mount shared resources, such as GPUs and agent workspaces, into containers to support AI workloads. Existing defenses remain inadequate. Kernel-level protections are intrusive, can destabilize system calls, and have therefore not been accepted into the Linux mainline. Detection methods rely on static rule matching or manual code auditing. Static rules can flag path-related functions but fail to capture the semantics needed to determine whether a host-container interaction exists, causing many false positives. Manual review requires domain expertise, making it costly, inefficient, and difficult to scale. To address this threat, we present Bulkhead, an automated framework that integrates large language models (LLMs) with formal methods for semantic vulnerability discovery and remediation. Bulkhead uses a multi-agent system to identify and repair PaTra vulnerabilities through multi-dimensional knowledge patterns generalized from known cases. It first applies high-risk functional patterns to locate entry points for cross-boundary interactions in containerized code, then uses call-chain patterns to recover the corresponding execution paths at suitable depth. The Detection pipeline analyzes these call chains against the application scenarios and threat model, identifying vulnerabilities such as missing security checks and TOCTOU flaws in cross-boundary interactions, and generating proof-of-concept (PoC) exploits for validation. These PoCs then guide patch generation. To ensure remediation correctness, the Patch pipeline performs assertion-driven verification using predefined model-checking templates.

---

## uid: `doi:10.2139/ssrn.7121419`

- title: Hugging Outsiders: Prior Success and Novelty in Open-Weight LLM Development
- authors: Julian Just
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7121419
- keyword hits: large language model, large language models, llm, llms

### abstract

This paper examines how contributors’ prior success and the novelty of contributed models relate to the adoption of open-weight large language models (LLMs) on the Hugging Face (HF) platform. Building on the attention-based view of innovation diffusion and on work on legitimacy and novelty, we argue that contributors without a track record on the platform struggle to attract downloads but can partly close the gap by releasing more novel models. Using a panel of 606 foundational LLMs released between July 2024 and December 2025 and tracking their downloads over time, we show that prior success strongly predicts adoption, that novelty has a positive effect, and that the two interact. Novelty pays off far more for contributors without a track record, while established contributors attract downloads even when their models are incremental. A series of separate regressions estimated at each monthly download snapshot shows that established contributors hold a downloads advantage at every snapshot examined, and that the extra payoff to novelty for contributors without a track record is significant at the first snapshot, close to zero one month later, and significant again at later snapshot through six months after the first. An analysis of the ten most-adopted models in the high-novelty, low-prior-success region shows that successful outsiders are either large firms already successful in related fields or small, skilled teams with research background, each differentiating from competitors either through wholly new architectures or by sharpening a familiar one toward a specific purpose. The paper discusses what these results mean for theories of legitimacy and novelty in innovation, and for the governance of attention on open innovation platforms.

---

## uid: `doi:10.2139/ssrn.6968998`

- title: Re-Examining the Contours of Fair Dealing and Fair Use in Copyright Infringement in the Wake of Generative Artificial Intelligence -A Comparative Analysis of UK, US and India
- authors: Arunabha Banerjee
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6968998
- keyword hits: generative ai, generative artificial intelligence, large language model, large language models, llm

### abstract

The rise of generative Artificial Intelligence ("AI") has resulted in an increased unauthorised use of copyrighted works in training Large Language Models ('LLM'). In recent years, a number of common law jurisdictions like the United States of America and United Kingdom have witnessed copyright infringement suits filed against the AI developers to injunct such unauthorised use. Proving infringement has been a challenge from the evidentiary point of view, as seen in Getty Images v. Stability AI before the UK High Court in 2025. However, even where infringement is detected by courts, the matter begs the question whether such liability can be exempted by application of the fair dealing doctrine under which the court must consider the extent of copying, purpose and character of use, effect on potential market etc. The issue becomes all the more pertinent considering the recent 2025 rulings in Richard Kadrey v. Meta Platforms and Bartz v. Anthropic where the US District Courts found in favour of the defendant on the point of fair dealing in relation to the act of training LLM's. A similar issue has also been raised in Thomson Reuters Enter. Ctr. GmbH v. Ross Intel. Inc. where Ross Intelligence has approached the Court of Appeals for the Third Circuit in an interlocutory appeal seeking the court's opinion on the question whether the unauthorized use of the Westlaw's headnotes by Ross Intelligence for creating its legal research tool can be considered as fair use under the US copyright law. This article will compare and examine the compatibility of the 'permitted use' and fair dealing under the Indian copyright law in light of this generative AI predicament, and suggest potential solutions to effectively adjudicate copyright infringement matters in these jurisdictions.

---

## uid: `arxiv:2607.14371v1`

- title: Supervised Fine-Tuning vs. In-Context Learning: An Equilibrium Analysis of LLM Personalization under Congestion
- authors: Fengzhuo Zhang, Zhuoran Yang, Dirk Bergemann
- affiliations: not stated
- posted: 2026-07-15
- source: arXiv
- link: https://arxiv.org/abs/2607.14371v1
- keyword hits: fine-tuning, in-context learning, large language model, large language models, llm, llms

### abstract

Large Language Models (LLMs) have revolutionized AI services, but a critical tension emerges: while personalization improves model performance, it consumes scarce computational resources that users must share. When should a user invest in expensive Supervised Fine-Tuning (SFT) versus lightweight In-Context Learning (ICL)? How does congestion from other users' personalization choices reshape these incentives? And what strategies should platforms adopt when offering multiple personalization algorithms? We develop a tractable framework for LLM serving that captures the statistical-economic trade-offs users face. Our analysis yields several surprising insights. First, we show that ICL and SFT dominate in different regimes, determined by an interplay between pretraining coverage and data signal-to-noise ratios, but congestion can flip these rankings. Second, equilibrium resource consumption exhibits pronounced non-monotonicity: improving pretraining precision reduces the congestion, while broader pretraining coverage and harder tasks sometimes increase it. Third, we prove that offering both personalization methods never hurts the platform's maximal profits, despite potentially increasing computational load. Experiments with GPT-2 on linear regression tasks validate our theoretical predictions about algorithm performance. Complementing these results, our review of documentation from 21 major AI platforms shows that the share offering both SFT and ICL increased from 9.5% in 2021 to 71.4% in 2025, consistent with our platform-design implications.

---

## uid: `arxiv:2607.13618v1`

- title: STOCKTAKE: Measuring the Gap Between Perception and Action in LLM Agents with a Fair Oracle
- authors: Sagar Deb, Ashwanth Krishnan
- affiliations: not stated
- posted: 2026-07-15
- source: arXiv
- link: https://arxiv.org/abs/2607.13618v1
- keyword hits: claude, deepseek, gpt-5, llm

### abstract

LLM agents are increasingly evaluated on multi-week decision tasks in which the state that drives cost is never directly observed. On such tasks the final cost cannot say why an agent failed: it may have misread the world, or read it correctly and still failed to act (the knowing-doing gap). Existing evaluations cannot separate these two failures; their reference policies either read privileged information the agent never sees, or are missing altogether. We introduce STOCKTAKE, a 26-week supply-chain replenishment benchmark built as a factored partially observable Markov decision process with six hidden factor processes, designed so that a fair reference policy is computable: an exact Bayes filter per factor drives a rollout policy on the identical observation stream the agent receives. Scoring each run between a symptom-blind base-stock floor (0) and this oracle (1) yields a skill score, and grading each week's written rationale yields a stated-belief detection lag and a knowing-doing rate, so state estimation and control are measured separately. On fifty seeds with curated stress profiles, Claude Sonnet 5, GPT-5.4, DeepSeek-V4-Pro, and Grok 4.5 detect 84-88% of hidden failures, typically within a week of onset, yet span skill scores from 0.62 to -0.23: two of the four end below the symptom-blind floor while naming factors slightly faster than the two that beat it. The failure has two faces. Where stress persists, 34-43% of correctly diagnosed stress weeks still end in stockout for every model, a rate that partly reflects the severity of the weeks models notice. That rate also runs opposite to skill: the two models under the floor stock out least on diagnosed weeks, so under-response is only one face of the gap, and their traces point to the other, responses whose cost exceeds what they protect. STOCKTAKE measures both directions of that failure.

---

## uid: `doi:10.2139/ssrn.6993619`

- title: Consumable but Not Identifiable Longitudinally: A Matched Audit of ESG Narrative Change in Japanese Listed Firms
- authors: Hiroyuki Kokubu
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6993619
- keyword hits: claude, deepseek, gemini, gpt-5

### abstract

This data note examines whether ESG narrative disclosures that are machine-consumable at a single point in time remain longitudinally identifiable-that is, whether year-over-year changes in narrative scoring can be reliably computed and interpreted under a fixed extraction and scoring protocol. We apply the disclosure-based v3.1 four-model consensus scoring system (claude-opus-4-7 / gpt-5.5 / gemini-3.1-pro-preview / deepseek-v4-pro) to a 30-firm matched panel of Japanese Prime Market companies across three reporting years (FY2022, FY2023, FY2024). Of 60 targeted prior-year firm-year cells, 29 (48%) achieved full comparability (class A: distinct artifact, ≥10 extractable spans); 31 (52%) were classified as non-comparable (class C) due to late-stage sample replacement, document unavailability, CMS-induced artifact duplication, or CDN-blocked download. Restricting analysis to class-A prior-year cells, we compute 87 axis-year ΔN observations across 15 firms and identify 5 symmetric pair-year observations where both the SBTi-anchor and matched non-SBTi firm in the same pair achieved class-A comparability. Of the 87 ΔN rows, 63 (72.4%) are stable within the inter-model dispersion threshold. Among the 24 changing rows, 16 show positive ΔN coinciding with Japan's mandatory disclosure expansion (2022-2025), classified as E-regulation-aligned candidates. Critically, the dominant source of class-C classification is sample construction timing-16 of 31 class-C prior-year cells (all in Group B) are attributable to nine replacement firms whose prior-year PDFs were not in the acquisition inventory. This is a procedural asymmetry, not a finding about firm disclosure behavior. These findings constitute the third empirical proposition in a systematization of ESG disclosure accessibility: narrative comparability does not imply longitudinal identifiability.

---

## uid: `arxiv:2607.15766v1`

- title: Before the Action: Benchmarking LLMs on Prospective Hypothesis Discovery
- authors: Tianyun Zhong, Wangyi Jiang, Wei Wang, Xuanang Chen, Yaojie Lu, Shiwei Ye, Yuzhen Shi, Boyu Yang
- affiliations: not stated
- posted: 2026-07-17
- source: arXiv
- link: https://arxiv.org/abs/2607.15766v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) excel at answering pre-specified questions, yet their ability to navigate the open-ended, pre-conclusion stage of discovery remains largely unmeasured. We introduce Prospective Hypothesis Discovery (PHD), which asks models to autonomously construct grounded, discriminative, and testable hypothesis spaces from inconclusive evidence, including anomalous observations and fragmented records, to guide subsequent investigation. To evaluate this capability, we introduce HypoArena, comprising HypoData, a benchmark of 988 cases across six scientific and analytical domains, and HypoEval, an evaluation framework for open-ended hypothesis sets. To construct HypoData at scale, we propose Retrospective Context Regression, a Forge--Audit pipeline that reconstructs pre-conclusion contexts from completed expert documents by removing explicit conclusions, target hypotheses, and retrospective causal attributions while preserving the factual substrate. Because PHD admits multiple valid outputs, HypoEval combines bidirectional pairwise judgments with Bradley--Terry--Davidson aggregation for ranking and six-dimensional rubric scoring for diagnosis. Experiments on 15 frontier LLMs reveal clear capability stratification and model-dependent effects of structured analytical skills, with gains for several lower-performing models on HypoArena but regressions for other systems, including a top-performing model. Compared with absolute rubric scoring, arena evaluation resolves finer-grained differences among models, with aggregated rankings showing strong agreement with human experts and an independent judge. Together, these results support treating PHD as a distinct target for evaluating how LLMs formulate investigative directions when final conclusions are withheld. Our code and data are publicly available at github.com/SKYLENAGE-AI/HypoArena and github.com/SKYLENAGE-AI/HypoArena.

---
