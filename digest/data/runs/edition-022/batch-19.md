# Classification batch 19 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-19.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7311378`

- title: Time-Indexed Defeasible Argumentation with Calibrated Risk: A Framework for Accountable Knowledge-Augmented Generation in High-Stakes Decisions
- authors: Bo Ding
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7311378
- keyword hits: large language model, large language models

### abstract

Large language models are increasingly proposed for decisions that carry consequences—grading an examination, advising on a legal question, approving a clinical or financial action—yet the properties these decisions require are precisely those such models do not natively provide: attribution to authoritative sources, correctness with respect to the version of the law or rubric in force at the time, principled resolution of conflicting criteria, a defensible policy for declining to answer, and an audit trail that a reviewer can replay. Retrieval augmentation supplies context but does not, by itself, supply any of these guarantees. We present TIDAR-KAG, a framework that composes four components over a knowledge-augmented generator: a time-indexed evidence graph with point-in-time semantics; a defeasible rule layer in which expert criteria are represented as rules with explicit grounds and defeaters and are promoted from shadow to active only after audit; a deterministic argumentation engine that adjudicates conflicts under grounded semantics; and a calibrated-risk gate built on split conformal prediction that releases an automated decision only when a distribution-free criterion is met, and otherwise abstains to a human. A sentence-level entailment gate enforces that every asserted sentence is entailed by an approved source, and a hash-chained ledger records each decision for replay. The framework is domain-neutral; we describe instantiations in education and in law. We state the formal properties the design provides—temporal soundness, deterministic and reproducible adjudication, conditional attribution, and marginal coverage of the abstention gate under exchangeability—together with the assumptions each property requires, and we give a reproducible evaluation protocol. This is an architecture-and-properties paper: we do not report a benchmark study, and we are explicit about which claims are proved and which are proposed for empirical test.

---

## uid: `doi:10.2139/ssrn.7299358`

- title: Jailbreaks arre Global or Regional? A Controlled Study of Scale and Geolocation Effects on LLM Safety
- authors: Anidipta Pal
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7299358
- keyword hits: llama, llm, qwen

### abstract

Most jailbreak research evaluates large, English-language, closed-source models inside wellresourced labs. Two practically important questions remain underexplored: does jailbreak vulnerability decrease monotonically with model size within a family, and does the apparent geographic origin of an API request affect safety behavior? We study both using entirely free, open infrastructure. For the scale question, we evaluate twelve models spanning 0.5B to 671B parameters across two matched families (Llama, Qwen) and four singletons using a two-phase protocol: plain harmful prompts (Phase 1), then the same prompts wrapped in published jailbreak templates (Phase 2). We measure attack success rate (ASR) and a secondary failure mode we term refusal-comprehension failure (RCF), in which a model produces neither a refusal nor a coherent harmful response. For the geolocation question, we route identical prompts through VPN exit nodes in five cities across three continents. We find a consistent within-family scale effect: smaller models show substantially larger Phase 1 to Phase 2 ASR jumps than larger siblings (Qwen2.5-0.5B: +53.5pp; Qwen2.5-72B: +12.2pp). Two models break the size-safety trend for interpretable reasons: Phi-3.5-mini-instruct achieves large-model-tier robustness at 3.8B due to safety-specific training (Cohen's d = 2.41 probe separation under Phase 2 versus d = 0.38 for Qwen-0.5B), while Mixtral-8x7B underperforms its 47B parameter count because sparse mixture-of-experts architectures do not scale safety-relevant parameters proportionally. We find no statistically significant geolocation effect for the three fully evaluable models (permutation test p > 0.18 in every case). Together, these results indicate jailbreak risk is determined primarily by model architecture and alignment investment rather than deployment location, with direct implications for practitioners constrained to smaller models by available hardware.

---

## uid: `doi:10.2139/ssrn.7299821`

- title: Generative AI Governance in iSchools: A Cross-Institutional Analysis of UNESCO's AI Ethics Principles
- authors: Nosakhare Okuonghae, Gordon Amidu
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7299821
- keyword hits: generative ai, generative artificial intelligence

### abstract

As universities formalize institutional responses to the use of generative artificial intelligence (AI) systems, numerous ethical frameworks have been proposed to guide their responsible use in higher education. This study adopts UNESCO's Recommendation on the Ethics of Artificial Intelligence as an analytical framework to examine which ethical principles are reflected in generative AI policies across iSchools. A qualitative content analysis of policies from 136 iSchools was conducted using six UNESCO ethical principles as the analytical framework. Responsibility and accountability (53.7%) and awareness and literacy (52.2%) were the most frequently reflected ethical principles. Fairness and non-discrimination (20.6%) and privacy and data protection (38.2%) appeared in fewer institutional AI policies. The analysis also showed that institutional AI governance extends beyond policy documents to include institutional decisions regarding approved AI tools. The findings show that institutional AI governance is characterized by the selective reflection of ethical principles in policy and operationalized through institutional support for generative AI tools.

---

## uid: `doi:10.2139/ssrn.7296878`

- title: Bounded Semantic Planning and Deterministic Compilation for Reliable Enterprise Text-to-SQL
- authors: Yi Ai
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7296878
- keyword hits: gemini, gpt-5

### abstract

Direct text-to-SQL asks a language model to do two jobs: interpret the business question and construct the complete relational query. In enterprise schemas, SQL can execute successfully while using the wrong relationship role or aggregation grain. We study an alternative placement of the stochastic boundary. A multi-turn planner grounds phrases and selects from question-specific governed options; graph traversal, role predicates, grain lowering, SQL construction, and deterministic checks are implemented in code. We evaluate this semantic path compilation (SPC) system against direct DDL-to-SQL generation on the ACME insurance benchmark. On a 38-question adjudicated comparison set with three runs per question, SPC was adjudicated correct on every run for 37 questions (97.4%), compared with 21 (55.3%) for the baseline. The paired discordance was 16 questions in favor of SPC and none in favor of the baseline (two-sided exact McNemar 𝑝 = 3.05×10-5). SPC answered all 38 questions correctly at least once and produced one refusal and no adjudicated wrong-but-executed run across 114 run outcomes; the baseline produced 29 adjudicated wrong runs and seven additional judge-flagged data-only coincidences on the same set. A strict-equivalence sensitivity analysis increased the paired difference. Using the same SPC workflow and three-run protocol, GPT-5.4 was solid on 36/38 questions (94.7%) and Gemini-3.6-Flash on 35/38 (92.1%). Six additional benchmark items are retained in an all-item analysis and documented separately by failure class. The study supports an end-to-end systems result, not a causal claim that compilation alone produced the gain, because SPC receives governed semantic artifacts that the DDL baseline does not.

---

## uid: `doi:10.2139/ssrn.7312182`

- title: PopMuse: Human‐AI Co‐Creative Audiovisual Canvas for Translating Pop Songs into Visual Narratives
- authors: Yichi Zhang, Jiaxiang Chen
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7312182
- keyword hits: large language model, large language models

### abstract

In the realm of popular music, visual media serve not only as an extension of auditory experience but also as a crucial space for artists to convey deep narratives and emotional resonance. However, many music creators face significant professional barriers and communication costs when attempting to translate abstract auditory emotions into visual expressions.We present PopMuse, a generative audio-visual canvas system designed to assist music creators in emotion visualization and collaborative creation. PopMuse introduces a user-centric interaction paradigm by leveraging multimodal large language models to deeply analyze a song s structure, instrumentation, and lyrical semantics, transforming them into an interpretable and editable structured visual description blueprint. This intermediate representation allows creators to intervene in the creative process, modifying textual prompts or visual styles to rapidly explore and generate customized album covers or music video storyboards while retaining artistic agency.We conducted a user study with 11 participants including music producers, music video creators, and enthusiasts to evaluate the system’s effectiveness. The results indicate that PopMuse not only significantly enhances creative efficiency but also acts as a creativity catalyst, helping users bridge the gap from auditory conception to visual realization and enabling deep human-AI collaborative emotional expression.

---

## uid: `doi:10.2139/ssrn.7290820`

- title: TwinGridShield: Consequence-Aware Runtime Authorization for LLM Grid-Agent Actions
- authors: Md Fazley Rafy
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7290820
- keyword hits: large language model, llm

### abstract

Large language model (LLM)-assisted energymanagement tools can translate natural-language context into structured grid commands, but syntactic validity does not imply physical admissibility. This paper presents TwinGridShield, a model-independent runtime authorization layer that evaluates each proposed action in a deterministic network twin before release. The prototype checks connectivity, branch-flow, generator, and load-shedding invariants and records each decision in a hashchained log. A controlled IEEE 14-bus study evaluates single-step switching, redispatch, and load-shedding actions using DC power flow and experimentally assigned branch ratings. In the matchedmodel experiment, a stochastic proposal source configured to select an unsafe action with probability p = 0.84 produced 421 unsafe proposals in 500 attacked-condition trials, a realized rate of 84.2%. This value characterizes the configured surrogate and is not an empirical measurement of LLM prompt-injection susceptibility. TwinGridShield produced 0 unsafe releases in those 500 trials. Because action labeling and authorization used the same DC model, system state, branch ratings, and encoded constraints, this result verifies conformance of the implementation to its encoded authorization predicate rather than safety under model error. The principal robustness evaluation therefore introduces model mismatch. Unsafe acceptance reached 5.63% under bounded ±20% per-bus load-measurement error and 30.09% when actual branch ratings were 20% below modeled ratings.

---

## uid: `arxiv:2608.18401v1`

- title: Multimodal Rapport Estimation in Real-World HRI
- authors: Akihiro Sakuramoto, Takato Hayashi, Ryo Miyoshi, Yuki Okafuji, Shogo Okada
- affiliations: not stated
- posted: 2026-08-19
- source: arXiv
- link: https://arxiv.org/abs/2608.18401v1
- keyword hits: gemini, llm, llms

### abstract

Evaluating interaction quality in real-world HRI is an important challenge. If interaction quality can be estimated reliably, the results can be used to improve dialogue strategies and ultimately enable robots to adapt their behavior autonomously. However, existing automatic evaluation methods have been developed primarily in controlled laboratory settings, and it remains unclear whether they can be directly applied to real-world environments, where users are free to disengage and multi-party participation may arise naturally. In this study, we investigate the automatic estimation of third-party-rated rapport scores using 62 sessions of multimodal recordings collected in a Japanese drugstore. We compare zero-shot LLMs, pretrained text, audio, and visual models, and their prediction-level fusion. The results show that, in real-world HRI, zero-shot LLMs achieve strong performance, while audio and visual models tend to provide complementary information. In particular, Gemini 2.5 Flash performs strongly as a single model, and a fusion model combining Gemini (text) with HuBERT and V-JEPA performs best overall. Further analyses showed that estimation performance varied across interaction-duration and group-size conditions. These findings suggest that rapport estimation in real-world HRI requires evaluation and model design that account for contextual variability beyond that assumed in laboratory settings.

---

## uid: `arxiv:2608.18398v1`

- title: LEDGER: Claim-to-Evidence Trace Graphs for Auditing LLM Agents
- authors: Daehong Kim, Haichao Miao, Shusen Liu
- affiliations: not stated
- posted: 2026-08-19
- source: arXiv
- link: https://arxiv.org/abs/2608.18398v1
- keyword hits: large language model, llm

### abstract

Large language model (LLM) agents can now carry out long-horizon technical workflows involving complex tool use, code execution, file edits, and generated artifacts. As agents do more work faster, the productivity bottleneck shifts from producing outputs to auditing whether those outputs are correct and trustworthy. Agent observability systems make fine-grained execution events visible, but visibility alone still leaves reviewers to reconstruct which actions, artifacts, and validation steps matter for a particular conclusion. We introduce LEDGER - Layered Evidence and Decision Graphs for Execution Review, a tracing and review system that builds layered trace graphs over observed agent sessions. LEDGER preserves Trace Records while grouping them into Evidence Nodes and Workflow Nodes, representing artifacts as evidence anchors, and adding typed semantic edges that connect claims to supporting actions, artifacts, and checks. Through data-analysis and coding examples, we show how the resulting traces expose workflow decisions, artifact lineage, repair steps, validation coverage, and claim-support paths for evidence-centered audit.

---
