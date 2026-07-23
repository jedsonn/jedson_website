# Classification batch 323 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-323.answer.json` as a JSON array.

---

## uid: `arxiv:2606.29567v1`

- title: SurrogateShield: Beyond Redaction for High-Utility, Privacy-Preserving LLM Interactions
- authors: Sherwin Vishesh Jathanna
- affiliations: not stated
- posted: 2026-06-28
- source: arXiv
- link: https://arxiv.org/abs/2606.29567v1
- keyword hits: llm

### abstract

LLM-based assistants transmit user queries verbatim to third-party API endpoints that lie outside the user's audit or control. When those queries contain personally identifiable information (PII), the data persists on remote infrastructure subject to breach, subpoena, or policy change. Placeholder redaction (the prevailing mitigation) suppresses PII at the cost of semantic coherence, producing structurally degraded queries and correspondingly degraded responses. We present SurrogateShield, a client-side proxy that substitutes detected PII with locally generated, type-consistent surrogate values prior to transmission and restores originals in the response. No real PII crosses the network boundary. Detection runs through a three-stage cascade (PatternScan, EntityTrace, and ContextGuard) covering 22 PII types and quasi-identifier combinations grounded in Sweeney's k-anonymity framework. Surrogate-to-original mappings are sealed in an AES-256-GCM encrypted per-conversation ShadowMap that never leaves the device. Evaluations on a 1,124-query corpus demonstrate that the cascade reliably detects PII, achieving an overall F1 score of 98.87%. Surrogate substitution substantially outperforms placeholder redaction in semantic utility, yielding a 13.26 pp improvement in BERTScore (roberta-large), from 81.59% to 94.85%. Within this corpus, the local pipeline restricted real PII transmission across all tested query types; in a 100-query adversarial trial, a prompted LLM adversary recovered no original values from surrogate-substituted messages.

---

## uid: `arxiv:2606.29493v1`

- title: Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving
- authors: Pawan Sasanka Ammanamanchi, Siddharth Bhat, Stella Biderman
- affiliations: not stated
- posted: 2026-06-28
- source: arXiv
- link: https://arxiv.org/abs/2606.29493v1
- keyword hits: llm

### abstract

Benchmarks for LLM-assisted theorem proving in Lean are often treated as intrinsically reliable because every solved instance comes with a machine-checked proof. However, the kernel only checks that a proof establishes a \emph{formal} statement; it does not verify that the statement faithfully encodes the intended informal problem, nor that evaluation harnesses are robust to trivial or adversarial solutions. We audit five widely used Lean theorem-proving benchmarks and their forks, using corpus-scale static checkers to surface 4,833 findings, including 398 mechanically certified issues such as counterexamples, vacuous theorems, and unsound axioms. We also document semantic defects such as missing hypotheses, problem simplification, incomplete or incorrect translations, and Lean-specific specification hazards. Beyond dataset construction, we survey evaluation-time failure modes and show, on corrected subsets, that defects can both inflate and deflate reported prover scores. We propose a fault taxonomy, a suite of automated checkers and recall-oriented semantic audit prompts, and release standards to guide the creation of formal math datasets and to make evaluation more reproducible and trustworthy. Our checkers, audit prompts, and corrected dataset snapshots are available at https://github.com/Shashi456/atp-checkers.

---

## uid: `arxiv:2606.29399v1`

- title: LLM-Guided Planning for Multi-hop Reasoning over Multimodal Nuclear Regulatory Documents
- authors: Mingyu Jeon, Bokyeong Kim, Suwan Cho, Jae Young Suh, Yonggyun Yu
- affiliations: not stated
- posted: 2026-06-28
- source: arXiv
- link: https://arxiv.org/abs/2606.29399v1
- keyword hits: llm

### abstract

Reviewing nuclear regulatory documents requires multi-hop reasoning across tens of thousands of pages, where judgments depend on evidence assembled across multiple chapters. We frame this task as planning: an LLM-based agent observes the evidence collected so far, picks the next document fragment to inspect, and stops when the evidence is sufficient. The agent operates over a vectorless document tree using browse, read, and search tools, and maintains a dynamic knowledge graph (KG) as state. On a 200-question benchmark over NuScale Final Safety Analysis Report (FSAR) documents, the system reaches 81.5% accuracy with a RAGAS Faithfulness of 0.93. The dominant performance factor is planning: against PageIndex, which uses the same document tree without state-conditioned action selection, the gap is +38.0pp (43.5% to 81.5%, p<0.001). The system also outperforms LightRAG (73.0%, p<0.05), HippoRAG (70.5%, p<0.01), and GraphRAG (49.5%, p<0.001), and matches RAPTOR (75.5%, p=0.11) without offline indexing. Edge inference adds 2.8x cost without raising accuracy; we retain it as a traceability module. Of 7,391 inferred edges, 3 Violates edges (0.04%) flag scope boundaries (Q058) and partial conformance (Q176) as typed annotations that a human reviewer can audit.

---

## uid: `arxiv:2607.16259v1`

- title: Quantifying Ranking Uncertainty in LLM Benchmarks
- authors: Bitya Neuhof, Yuval Benjamini
- affiliations: not stated
- posted: 2026-06-28
- source: arXiv
- link: https://arxiv.org/abs/2607.16259v1
- keyword hits: llm, llms

### abstract

Pretrained models are typically ranked on multi-task leaderboards to assess their effectiveness across diverse tasks. Rank confidence intervals were recently introduced as a method to quantify the uncertainty in these rankings by aggregating pairwise hypothesis tests. In this work, we analyze the sources of uncertainty in the knowledge evaluation benchmark MMLU and show how hypothesis tests can be modified to account for their effects. We demonstrate that ranking variability across MMLU subjects is substantial and should be considered when comparing LLMs or identifying the top-performing models.

---

## uid: `arxiv:2606.29196v1`

- title: Representational Depth of Evaluation Awareness Shifts With Scale in Open-Weight Language Models
- authors: Archit Manek
- affiliations: not stated
- posted: 2026-06-28
- source: arXiv
- link: https://arxiv.org/abs/2606.29196v1
- keyword hits: llama, qwen

### abstract

Do language models know when they are being tested? This question matters for AI safety: a model that recognises an evaluation context could alter its behaviour strategically, making downstream benchmarks harder to interpret. Using 11 models spanning Qwen 2.5, Gemma 2, and Llama 3.2, we find a systematic size-dependent shift in representational depth: in both Qwen 2.5 and Gemma 2, the layer at which evaluation-awareness is most linearly recoverable moves from late layers in smaller models to early layers in larger ones. This suggests that scale changes not only the strength of evaluation-awareness but also where it is most linearly recoverable in the network. This depth shift helps explain why within-family scaling trajectories are non-monotonic or inverse rather than smooth and family-general, showing that a simple universal power-law account is not supported under denser within-family sampling. Finally, white-box probe signals are consistently stronger than black-box behavioural expression, and the relationship between the two varies by family in ways not predicted by probe AUROC alone.

---

## uid: `doi:10.2139/ssrn.7021144`

- title: The Paradox of Artificial Intelligence Adoption: How Artificial Intelligence Engagement Shapes Anxiety over Skill Atrophy Among Public Relations Professionals
- authors: Karen Sutherland, Puneet Vatsa, Karen J. Freberg
- affiliations: not stated
- posted: 2026-06-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7021144
- keyword hits: generative ai

### abstract

Public relations professionals face a distinctive challenge in the age of artificial intelligence (AI). Their core competencies, including relationship cultivation, ethical counsel, and authentic voice, are precisely those most difficult to automate yet most vulnerable to erosion through disuse. This study investigates how communication practitioners perceive the impact of generative AI on their skills, examining whether increased AI engagement heightens or diminishes concerns about professional capability. Drawing on an integrated framework combining Diffusion of Innovation Theory and Technology Acceptance Model 3 (TAM3), this study surveyed 400 public relations professionals across Australia, the United Kingdom, and the United States. A generalized ordered logit model examined associations between practitioner characteristics and concern about AI-induced skill atrophy. The findings reveal what we term the "engagement paradox": moderate AI users reported the least concern, while frequent users acknowledged potential risks but were significantly less likely to express extreme worry. Notably, frequency of AI use predicted concern more consistently than education, experience, industry, or firm size. These results extend TAM3 by positioning skill-atrophy concern as a novel post-adoption affective outcome and demonstrate threshold-dependent effects across the concern distribution. For practitioners and educators, the findings suggest that calibrated engagement with AI, rather than avoidance or intensive adoption, may offer a sustainable path through technological transformation.

---

## uid: `doi:10.2139/ssrn.7006287`

- title: Stop Debugging the Dreamer: A Manager’s Framework for Turning AI Hallucinations into Breakthroughs
- authors: İlbey  Kutluhan Papatya, Nurhan Papatya
- affiliations: not stated
- posted: 2026-06-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7006287
- keyword hits: generative ai

### abstract

Most organizations treat generative AI’s hallucinations as a defect to stamp out. That instinct is backwards. Discovery has always run on the same engine — abundant variation, then ruthless selection — and generative AI has made variation almost free. The binding constraint is no longer imagination but verification, and verification cost is something managers can deliberately lower. We give managers a diagnostic, the Verifiability–Stakes matrix, that says when to amplify a model’s “dreaming,” when to harness it behind a verification gate, and when to contain it. More importantly, we show a dynamic move competitors miss: by engineering verification cheaper, a firm can tip whole domains from “too risky to touch” into “too valuable to ignore.” A four-step protocol — Provoke, Filter, Capture, Bound — builds the organization that turns AI’s errors into advantage — and tells you fast, before the expensive bet, when it is not paying.

---

## uid: `doi:10.2139/ssrn.6974858`

- title: Distillation and Strategic Launches on the LLM Frontier: An Empirical Analysis
- authors: Jiaqi Shi, Zhoupeng (Jack) Zhang
- affiliations: not stated
- posted: 2026-06-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6974858
- keyword hits: large language model, llm

### abstract

We study how distillation shapes the innovation frontier in the large language model (LLM) market. A distinctive feature of this market is that launches can also become inputs into rivals’ subsequent development: Model behavior can be learned from, and open-weight releases expose reusable artifacts more directly. We build a provider-week panel from 529 model launches by 51 providers between November 2022 and June 2026, measuring both launch decisions and benchmark-based quality states. Reduced-form evidence identifies two opposing margins: While realized open-weight rival frontier raises in the same capability dimension are associated with larger subsequent quality improvements, anticipated near-term open-weight rival launches reduce current launch probabilities. Closed-weight rival activity does not exhibit similar patterns. We then estimate a structural launch model in which distillation affects both quality improvement and launch timing. Counterfactual analyses show that an all-closed-weight regime increases launch frequency but reduces quality gains per launch, whereas an all-open-weight regime tempers launch frequency but increases quality gains per launch. These opposing margins offset more strongly under all-open than under all-closed: All-open remains close to the baseline frontier, while all-closed yields greater total quality improvement through a substantially higher launch frequency. Impacts on consumers are modest and dimension-specific, with the all-open regime tending to benefit consumers more than the all-closed regime by improving the best available models. Our work highlights how distillation and model openness reshape the LLM innovation frontier through timing and magnitude.

---
