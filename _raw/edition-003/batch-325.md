# Classification batch 325 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-325.answer.json` as a JSON array.

---

## uid: `arxiv:2606.30306v1`

- title: Always-OnAgents:A Survey of Persistent Memory, State, and Governance in LLMAgents
- authors: Tianyu Ding, Aditya Nannapaneni, Bingfan Liu, Ling Zhang
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.30306v1
- keyword hits: llm

### abstract

Always-on agents are systems whose future behavior depends on durable state accumulated across earlier interactions. We treat them as persistent-state systems: the operative system includes retrievable memories, but also task ledgers, permissions, credentials, commitments, provenance and audit records, shared state, trigger conditions, and externally committed effects linked to those records. The survey reads the literature through six diagnostic axes for each state item, authority, scope, mutability, provenance, recoverability, and actionability, and through a lifecycle in which state is written, validated, organized, retrieved, acted upon, updated, forgotten, audited, and sometimes rolled back. Across a 435-work coded corpus, treated as a scoped map rather than an exhaustive census, the literature concentrates more heavily on accumulating and retrieving state than on governing, recovering, or relinquishing it. We therefore introduce the Always-On Evaluation Protocol (AOEP-v0), a pilot evaluation contract that makes these governance requirements concrete by scoring state mutation and recovery obligations rather than answer quality alone. The resulting agenda connects always-on agents to databases, distributed systems, formal methods, capability security, and machine unlearning.

---

## uid: `arxiv:2606.30219v3`

- title: EvalSafetyGap: A Hybrid Survey and Conceptual Framework for LLM Evaluation-Safety Failures
- authors: Buğra Alperen Uluırmak, Rifat Kurban
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.30219v3
- keyword hits: llm

### abstract

LLM evaluation and AI safety face a shared measurement problem: benchmark scores, reward-model signals, and reported safety metrics can improve while the latent properties they are meant to represent remain difficult to verify. This paper combines a hybrid survey - a systematic search paired with narrative synthesis and separately tracked grey evidence - with a conceptual framework and a structured ten-model audit. The synthesis spans eight evidence streams: benchmark validity, dynamic evaluation, LLM-as-judge reliability, safety evaluation, jailbreak/refusal robustness, reward hacking, mechanistic interpretability, and governance/auditability, covering 2018-2026 evaluation-safety measurement work. We introduce EvalSafetyGap as an organizing hypothesis for comparing evaluation-side and alignment-side proxy failures under optimization pressure, using Goodhart's Law together with two constructs we develop here - an Instability Decomposition and an Alignment Trilemma - as tools for generating testable comparisons. The audit shows how conclusions shift when capability, behavioral safety, and governance are measured separately. In this sample ($n = 10$), the association between capability and sustained adversarial robustness is statistically indeterminate using the displayed Table 3 inputs (Pearson $r = +0.232$, $p = 0.520$), and the apparent open-closed safety gap is modest, driven mainly by governance and disclosure rather than behavioral robustness, and sensitive to how a single borderline model is classified; attempt-budget results are protocol dependent. Because the public evidence uses heterogeneous protocols, the audit is diagnostic rather than rank-generating. The contribution is a shared vocabulary and evidence map to support dynamic evaluation, transparent source reporting, multi-attempt safety measurement, and auditable alignment practice.

---

## uid: `arxiv:2606.30128v1`

- title: Does Verbose Chain-of-Thought Really Help? In-Distribution Evidence that Content, Not Length, Matters
- authors: Wenlong Wang, Fergal Reid
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.30128v1
- keyword hits: chain-of-thought, llm, prompting

### abstract

Chain-of-thought (CoT) prompting improves LLM reasoning, but the source is contested: do the intermediate steps help because they carry useful semantic content, or because conditioning on more tokens buys extra computation before the model commits to an answer? We bring two lines of evidence to bear. First, in distribution: we repeatedly sample each model on the same question and pair a shorter with a longer of its own natural generations that follow the same reasoning plan, so nothing is rewritten and both traces are genuinely in-distribution. Across 25 models the extra tokens leave accuracy essentially unchanged for every independently-trained reasoner, and a blind analysis of the surplus tokens shows that what gain exists elsewhere tracks validation- and checking-content, not verbosity per se. Second, as a controlled intervention, we ask whether two traces expressing the same semantic content (the same facts, operations, and intermediate values, verified through directed acyclic graph equivalence) produce different outcomes when one is more verbose, using a dual-validator design across four targets and eight benchmarks with number-redacted completion and stratified bootstrap confidence intervals. Verbose traces do improve accuracy (25 of 32 benchmark-target cells are positive under at least one validator), but the effects are modest (typically 1-4 points) and depend on the quality of the verbose prose, not merely its length. Under maximum numerical redaction the effect is amplified (median 3.24x across four arithmetic benchmarks), and length-matched non-reasoning filler recovers none of it. Both lines converge: what matters is what the extra tokens do (the reasoning and validation content they carry), not how many there are, a picture neither a pure forward-pass-compute nor a pure semantic-content account fully explains.

---

## uid: `doi:10.1145/3770855.3818984`

- title: Redefining Maritime Anomaly Detection via Equation-Grounded Synthetic Anomalies
- authors: Youngseok Hwang, Sungho Bae, Dohun Lee, Jaeeun Seo, Jeehong Kim, Wonhee Lee, Hyunwoo Park
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.29721v1
- keyword hits: llm

### abstract

Maritime anomaly detection is essential for ensuring maritime safety, security, and efficient traffic management at sea, with Automatic Identification System (AIS) data serving as a primary data source. Despite its importance, most publicly available AIS datasets lack predefined anomaly labels, forcing prior studies to rely on either distribution-based rarity or domain rule/expert-assisted labeling. These approaches, however, face fundamental limitations: statistical rarity often fails to reflect practically critical events, while expert-based labeling is costly, subjective, and difficult to scale. Moreover, both paradigms tend to overlook interaction-driven hazards such as near-miss approaches between vessels. To address these challenges, we propose an equation-grounded anomaly taxonomy that is implementable under a limited AIS observation schema and extensible to other AIS datasets. Specifically, the taxonomy defines three anomaly types: unexpected AIS activity (A1), route deviation (A2), and close approach (A3), covering both single-vessel and inter-vessel anomalies. Building on this taxonomy, we introduce a unified score-synthesize-label pipeline that produces LLM-guided plausibility scores, uses them to synthesize anomalies, and assigns timestamp-level labels. To rigorously assess detection performance, we further design benchmark evaluation settings that account for variations in temporal-window length and anomaly-type composition, and evaluate a broad range of time-series models and anomaly detection models. Together, these contributions provide a systematic basis for evaluating maritime anomaly detection methods across different anomaly types. Our code is available at https://github.com/snudial/open-maritime-anomaly-detection.

---

## uid: `doi:10.2139/ssrn.6892522`

- title: Platform Governance in Generative Search: A Theory of Authority, Relevance, and Welfare
- authors: Xing Hu
- affiliations: not stated
- posted: 2026-06-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6892522
- keyword hits: generative ai

### abstract

Generative AI search transforms search platforms into governors of answer inclusion. As user attention concentrates in synthesized answers, the platform's sourcing rule determines which firms are allowed to appear in the commercially salient part of search. We develop a game-theoretic model in which a platform chooses, before latent relevance is observed, how much weight to place on authority relative to query-specific evidence. A high-authority incumbent and a low-authority specialist then invest in generative engine optimization (GEO) to make pre-existing relevance legible. We show that generative search creates conditional contestability rather than either uniform entrenchment or automatic democratization: by setting the authority weight, the platform determines how much legible evidence a lower-authority specialist must produce before its relevance is allowed to count. In broad queries, that barrier protects incumbents and concentrates answer-layer visibility; in niche queries, su!ciently strong specialist fit can clear it and flip the answer layer. Crucially, we identify a private-governance wedge: private screening can exclude socially valuable specialists and impose a robust proof-burden distortion by forcing even the displayed winner to bear socially wasteful proof costs through excessive GEO spending. We then show how to narrow that wedge. Better platform-side verification mainly cuts wasteful proof expenditure unless its gains are passed through into less authority-heavy sourcing, while stronger market incentives to reward relevance reduce exclusionary screening more directly. The paper identifies the authority weight as a central market-design lever shaping answer inclusion, market structure, and welfare.

---

## uid: `doi:10.2139/ssrn.7026193`

- title: Fifteen years of graphene optoelectronics: an LLM-assisted, dual-source landscape and taxonomy of device innovation
- authors: Renan Silva Santos
- affiliations: not stated
- posted: 2026-06-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7026193
- keyword hits: llm

### abstract

Graphene was isolated barely two decades ago, yet the literature on its optoelectronic devices already spans tens of thousands of papers and patents, too many for any narrative review to map. We address two problems at once: a practical one (what does the graphene-optoelectronics innovation landscape look like, and how is it organized?) and a methodological one (how can such a landscape be built reproducibly and ported to other domains?). We assemble a dual-source corpus of open scholarly and patent metadata — 43,190 journal articles indexed in OpenAlex over 2010–2025, plus a patent layer — and process it through a transparent pipeline that pairs unsupervised theme discovery with generative large-language-model (LLM) taxonomy induction. The result is a five-facet taxonomy of graphene optoelectronic innovations (device class, material architecture, operating mechanism, application domain, and maturity stage) and a quantitative landscape of how innovation has moved across it. Scholarly output follows a clear technology-life-cycle signature: an exponential phase to about 2017 (≈32% compound annual growth) then a plateau (≈1% per year), strongly concentrated in China (34.6% of publications), with a 2024–2025 resurgence tied to van der Waals heterostructures and graphene–perovskite hybrids. We find a pronounced translational asymmetry (fundamental device physics and material/process work dominate, while markers of system integration and commercialization are scarce), which we read against technology-life-cycle and innovation-systems theory. We release the full pipeline so the method can be re-pointed at another domain by editing a single configuration file.

---

## uid: `doi:10.2139/ssrn.6993698`

- title: Do Ai Advocates Dream Of Phantom Precedent? Designing A Reliable Legal Ai Assistant To Narrow The Justice Gap
- authors: Mengyuan Yang
- affiliations: not stated
- posted: 2026-06-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6993698
- keyword hits: large language model

### abstract

This article examines whether current AI legal assistance tools are sufficiently reliable for direct use by self-represented and low-income users in high-stakes civil matters. It argues that large language model-based systems, despite their fluency and apparent usefulness, retain a persistent risk of hallucination, doctrinal mismatch, and other legally consequential errors that such users are often poorly positioned to detect or correct. The article further argues that commonly proposed safeguards, including retrieval, citation, and staged review, reduce but do not remove this residual risk. It then develops an alternative design framework based on a Legal World Model approach, in which case state is represented explicitly, outputs are constrained by governing authority, and the system abstains where reliable action is not possible. On that basis, the article proposes a governance framework for consumer-facing legal AI combining consumer protection, state authorization, and entity-level professional accountability.

---

## uid: `doi:10.2139/ssrn.7025344`

- title: GARE-Skill：Group-wise Attribution and Regression-Gated Evolution of Search Skills for Agentic RAG
- authors: Songjie Li, Zhiqiang Gao, Wenting Cheng, Weitong Ji, Chen Yuan, Xinli Zhu
- affiliations: not stated
- posted: 2026-06-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7025344
- keyword hits: agentic, qwen, retrieval-augmented

### abstract

Open-domain question answering agents rely on external search skills to control query construction, evidence assessment, and stopping decisions during retrieval-augmented generation. Existing hand-crafted skills, however, cannot adapt to historical execution failures. Directly rewriting a global skill from failed trajectories is also risky, because heterogeneous errors in question understanding, search planning, query rewriting, and evidence control may be mixed into broad rules that repair a few cases while damaging previously correct behavior. To address these limitations, we introduce GARE-Skill, a training-free framework for group-wise attribution and regression-gated evolution of Search Skills. GARE-Skill attributes failed agentic RAG trajectories to functional groups, generates local candidate patches, and retains only patches that provide sufficient repair benefit with controlled degradation risk, while keeping both the language model and retriever frozen. Experiments on five open-domain QA benchmarks show that skills evolved from 2Wiki failures improve over a strong Base Skill and generalize to PopQA, NQ, HotpotQA, and MuSiQue. For Qwen3.5-397B-A17B, the out-of-domain average improves by +3.2 pp (EM) and +3.5 pp (F1) over the Base Skill; for Qwen3.5-35B-A3B, the gains are +2.5 pp (EM) and +2.6 pp (F1). Behavior diagnostics show that these improvements are accompanied by more stable execution and fewer max-turn failures, reducing such cases by 68.3\% on PopQA and 65.5\% on MuSiQue. Ablation and transfer analyses validate the necessity of group-wise evolution and regression gating, while showing that search stopping remains sensitive to the target model's own search and stop priors.

---
