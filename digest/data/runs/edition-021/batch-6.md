# Classification batch 6 of 22, edition 21

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-021/batch-6.answer.json` as a JSON array.

---

## uid: `arxiv:2608.14804v1`

- title: Generated Context versus Governed State: Functional Conditions for Accountable Longitudinal Clinical Reasoning
- authors: Augusto Bernardo Pissarra, Victor Lorena de Farias Souza
- affiliations: not stated
- posted: 2026-08-14
- source: arXiv
- link: https://arxiv.org/abs/2608.14804v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) have become the dominant interface of clinical artificial intelligence, yet the interface they expose (text in, text out, one context window at a time) maintains no explicit, persistent, governed representation of what is currently true about a patient. This paper argues that longitudinal clinical reasoning is a state-estimation problem under partial observability, and that the axis on which clinical AI succeeds or fails is not the fluency of the model reading the record but the governance of the patient state it reasons over. We distinguish generated context from governed state; separate five objects that clinical AI habitually conflates (true state, observations, evidence, belief, and simulated state); define a tiered governance standard against which any clinical AI system can be audited; and show that an operational definition of accountability decomposes into four information requirements: an immutable evidence ledger with awareness-time versioning, a belief state distinct from accumulated evidence, an observation-process model, and claim-level causal typing. We are explicit that this decomposition is analytic rather than a necessity theorem, and that its value is conceptual hygiene: it converts "accountable clinical AI" from a slogan into an audit instrument. A six-level maturity framework separates what a system makes governable from what it can compute, locating current LLM-centric practice at high capability but low maturity. The paper is fully self-contained: the four research questions the framework poses are stated in the introduction, and the conclusion records what the paper establishes toward each; future work develops the buildable core of the architecture and the research program toward full Clinical World Models. No empirical result is claimed here.

---

## uid: `doi:10.2139/ssrn.7290195`

- title: JaccardServe: Cross-Request Prefill Acceleration in LLM Serving via MinHash-LSH Token Shingling
- authors: Anmol Sureshkumar Panchal
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7290195
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented, token embedding

### abstract

Reusing computed key-value (KV) caches across requests is a highly effective optimization in serving large language models (LLMs), but the field has split into three main approaches: exact block-level prefix caching (vLLM APC), exact token-level prefix caching (SGLang RadixAttention), and approximate cosine-similarity caching on token embeddings (SemShareKV). Each method captures different types of cross-request redundancy while missing others. Exact prefix caches fail to handle templated prompts with user-specific substitutions; SemShareKV requires pairwise comparisons and GPU-level embedding computations before matching. None specifically address scenarios where many simultaneous requests share large, nearly identical token sequences differing only by minor lexical changes—a common pattern in templated chat, retrieval-augmented generation (RAG) with passage reordering, and multi-agent frameworks. This paper introduces JaccardServe, a cross-request prefill acceleration layer that uses MinHash-LSH near-duplicate detection on token shingles. The matching process operates at the API gateway on standard CPUs before any model inference, based on the Broder–Charikar MinHash banding technique, which provides a tunable precision-recall trade-off via the closed-form S-curve formula 𝑃(collision; 𝑠, 𝑏, 𝑟) = 1 − (1 − 𝑠^𝑟)^𝑏. This approach extends the author's previous MinHash–LSH banding implementation for document near-duplicate detection [Panchal, 2018] to online inference with token-level detail. In a 500-prompt templated-chat benchmark, exact block-level prefix caching achieves a 5.2% cross-request match rate, while JaccardServe at a balanced setting (b=20, r=4, 𝜏=0.5) reaches a 97.4% match rate with only 0.28 ms overhead per request at the gateway—an 18.7-fold improvement. On a 320-prompt multi-document summarization benchmark, hit rates are 19.7% for vLLM APC, 5.9% for a SemShareKV simulator, and 70.9% for JaccardServe balanced. Compared to an oracle ground truth, JaccardServe in high-recall mode achieves precision of 0.905 and recall of 0.806 (F1 = 0.853), outperforming vLLM APC’s 0.324 and SemShareKV’s 0.120. The paper follows the author’s previous review-and-extend framework [Panchal, 2018], surveying three existing cross-request reuse techniques, outlining their limitations, and presenting JaccardServe as a complementary solution. All related code, benchmarks, and figures are available in a single CPU-reproducible repository. Keywords: AI, LLM, Model Compression, Token Deduplication, LLM inference, KV cache, prefix caching, MinHash, locality-sensitive hashing, Jaccard similarity, and serving systems.​

---

## uid: `doi:10.2139/ssrn.7291671`

- title: A Neuro‐Symbolic Framework with DOF‐Based Constraint Verification for Generating Parametrically Editable Sketches from Natural Language
- authors: Pengfei Bao, Qingying Zhao, Yidan Luo
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7291671
- keyword hits: large language model, large language models, llm, llms

### abstract

The direct transformation of natural language design descriptions into editable, constraint‐based parametric CAD models remains an open challenge. While large language models (LLMs) exhibit impressive generative capabilities, their application to engineering CAD is limited by a fundamental inability to guarantee geometric consistency and parametric editability. This paper proposes a neuro‐symbolic framework that couples a fine‐tuned LLM, functioning as a structured intent parser, with a deterministic symbolic verifier grounded in rigid‐body degrees‐of‐freedom (DOF) analysis. The LLM extracts entity‐constraint graphs from free‐form text; the verifier then audits these graphs for over‐ and underconstraint, automatically repairing logical inconsistencies using a greedy heuristic rooted in kinematic invariants. The verified graph is solved by a geometric constraint solver to produce fully editable parametric sketches. Evaluated on a curated dataset of 340 industrial 2D sketch‐text pairs, our approach achieves a solver success rate of 92.4% and, critically, 100% parametric editability for all successfully solved cases—substantially outperforming end‐to‐end LLM script generation (41.2% success). Failure analyses reveal that the DOF verifier resolves 83% of LLM‐induced logical errors, underscoring the indispensable role of symbolic reasoning in translating linguistic intent into engineering‐grade digital models. This work establishes a reproducible, verification‐centric paradigm for trustworthy AI‐assisted design.

---

## uid: `doi:10.2139/ssrn.7264764`

- title: Credible Stopping Points: Focal Points, Reference Points, and Peaceful Territorial Change
- authors: Tomoyuki Matsuoka
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7264764
- keyword hits: chatgpt, claude, gemini, generative ai

### abstract

What makes peaceful territorial change possible? To answer, I integrate two usually separate literatures. Schelling’s focal-point theory treats territorial lines as resources for settlement; prospect theory’s reference-point accounts treat the same lines as definitions of loss that sustain conflict. To concede territory peacefully, the target must believe that resistance is costly and that compliance is final. These requirements create a threat–assurance tension: the same evidence that makes resistance appear costly can also make further demands after compliance seem plausible. A salient line—a potential focal point—can make a finite settlement limit mutually intelligible; yet it gives the target no reason to believe that the challenger’s exceptional willingness to bear costs declines there. The missing element is the territorial reference point: the subjective baseline from which the challenger evaluates outcomes as gains or losses. While the line it marks remains unattained, unrecovered loss sustains the challenger’s willingness to bear costs; attainment removes this loss-recovery premium, and territory beyond becomes ordinary gain. Yet the reference point is not directly observable. When it coincides with the focal line—convergence—the same line does two jobs at once: it serves as the mutually intelligible limit, and it marks the motivational break. In protracted disputes, however, several candidate baselines may coexist, some beyond the focal line, and the target must infer which one guides the challenger. Its claims, priorities, and bargaining behavior provide diagnostic evidence. Where evidence remains insufficient, the challenger’s choice between two forms of commitment can strengthen the inference. A coordination-point commitment conditions restraint on the target’s conduct; a stopping-point commitment conditions the scope of revision on the line itself and publicly forecloses farther baselines. Because such foreclosure is costlier for a challenger guided by a farther baseline, the choice itself becomes evidence of whether recovery is complete at the focal line. When the target can infer convergence, threat and assurance can become jointly credible and the line a credible stopping point; when convergence is absent or cannot be inferred, concessions may stall and disputes may escalate. I illustrate the framework with the Sino-Soviet border settlement (1964–1991) and the Egyptian–Israeli peace (1967–1982). In both cases, a long-available focal line supported settlement only after diagnostic evidence favored convergence; costly public acts foreclosing farther baselines reinforced that inference. AI Disclosure: During the preparation of this manuscript, the author used generative AI tools (ChatGPT, Codex, Claude, Claude Code, and Gemini) for drafting, translating drafts and notes into English, revising and proofreading, and identifying potentially relevant literature and sources. The author independently verified all cited sources and supporting evidence and reviewed and edited all AI-generated or AI-assisted material incorporated into the manuscript. The author developed the argument, made all final scholarly judgments concerning the interpretation and conclusions, and takes full responsibility for the content.

---

## uid: `doi:10.2139/ssrn.7269978`

- title: A Syllabus-Agnostic Reference Architecture for Free, National-Scale Socratic AI Tutoring
- authors: Muthu Rama Ganesh Srinivasan
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7269978
- keyword hits: large language model, large language models, llm, llms

### abstract

One-to-one tutoring remains the most effective known form of instruction, yet its cost has confined it to families who can afford it-the access problem Bloom framed four decades ago as the 2 Sigma Problem. Large language models (LLMs) have recently demonstrated, under randomised controlled conditions, that carefully scaffolded AI tutors can match or exceed strong classroom instruction. However, most demonstrated systems are single-purpose builds: one model, one subject, one pedagogy, one market-and their inference economics presume paying users. This paper presents a reference architecture for an AI tutor designed from first principles to be free at national scale and extensible across syllabi, teaching methods, languages, and models. The architecture makes four design commitments: (1) a strict portsand-adapters (hexagonal) decomposition in which curriculum, pedagogy, model, learner state, and gamification are independently swappable behind stable interfaces; (2) a separation of generative and deterministic responsibilitiesthe language model conducts Socratic dialogue while answer evaluation and skill progression remain deterministic code, with the worked solution always supplied to the model (mandatory grounding) so that it guides rather than derives; (3) an event-driven decoupling of motivational game mechanics from the pedagogical core; and (4) a data flywheel in which interaction telemetry is curated into training data that distils a purpose-built small language model (SLM), gated by evaluation benchmarks before deployment, driving the marginal cost of tutoring toward a level at which free nationalscale service is sustainable. We instantiate the architecture for Singapore's Primary School Leaving Examination (PSLE) mathematics syllabus, treating the syllabus entirely as data rather than code, and describe a phased build roadmap executable by a small team. The paper's contribution is architectural: a documented, reproducible design that converts recent empirical findings on LLM tutoring into an engineering blueprint for equitable access.

---

## uid: `doi:10.2139/ssrn.7291619`

- title: Beyond Accuracy: Separating Reasoning Competence from Default Reasoning Behavior in Large Language Models — A Controlled Causal-Reasoning Study in Newtonian Physics, with a Cross-Domain Probe in Deterministic Mathematics
- authors: Cheng Zuo
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7291619
- keyword hits: claude, deepseek, gpt-4, large language model, large language models

### abstract

How should an evaluation distinguish a model that can solve a causal problem from one that routinely expresses the relevant causal structure without being asked to? We use the Newton's Laws Triplet Benchmark (NLTB) to evaluate GPT-4o, Claude Opus 4.8, and DeepSeek-v4-pro on accuracy together with a five-dimensional annotation of observable reasoning behavior (object and causal-variable identification, causal-direction articulation, variable parsimony, causal-chain narration), treated as behavioral indicators rather than direct evidence of an internal causal model. All three models are highly accurate, with little accuracy degradation under surface-isomorphic reformulation where tested, yet dissociate from two default behaviors. First, all three frequently re-derive a circuit time constant that is already given or irrelevant; removing a causal-statement step leaves this unchanged, while an explicit parsimony instruction reduces it in two models but not GPT-4o. Second, with the causal-statement step removed, all three still apply the correct governing law, while explicit verbalization of causal direction falls to 55%/40%/35% for Claude/GPT-4o/DeepSeek in the paired Tier-4 analysis. Demand controls recover both behaviors, separating elicitable competence from spontaneous behavior — evidence that accuracy and reasoning behavior are separable measurement targets, not that an internal causal model is established or refuted. A small exploratory mathematics extension shows a similar pattern (not used to support the main claims). Three benchmark-generator defects found during analysis show that ground truth must be validated before attributing model failures to reasoning. The study contributes a controlled evaluation framework and evidence that reasoning competence, expression, and prompt demand are distinct measurement targets.

---

## uid: `doi:10.2139/ssrn.7292159`

- title: Cultural Sensitivity in AI-Mediated Language Instruction: A Critical Exploration of Learner Perceptions and Feedback Biases
- authors: Thomas  Abdull Jamel Asare
- affiliations: not stated
- posted: 2026-08-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7292159
- keyword hits: chatgpt, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are rapidly becoming a source of academic writing support, raising concerns about how these tools recognize and preserve culturally embedded writing in non-native varieties of English. This study aims to provide an integrated understanding of how AI-mediated feedback is perceived and culturally sensitive in a culturally diverse environment like Ghana. The study seeks to answer 2 research questions: a) How do Ghanaian ESL learners perceive the cultural sensitivity of AI-generated responses to their English texts? B) What discursive patterns of cultural bias or insensitivity to culturally embedded expressions of the participants’ texts are present in AI feedback outputs? Forty Ghanaian university students produced written texts in English based on a cultural embodiment prompt which was then evaluated by two AI tools—ChatGPT and Trinka.ai through a standardized prompt requesting constructive comments on grammar, vocabulary, sentence structure, and clarity. To answer the first research question, the participants completed quantitative data from an 8-item Cultural Sensitivity Scale and were analyzed using a linear mixed-effects model. No statistically significant difference between the tools’ perceived cultural sensitivity was revealed, with both getting mid-range evaluations. To address the second research question, AI feedback on the students’ texts was processed inductively using a Critical Discourse Analysis and Culturally Sustaining Pedagogy framework, which identified four dominant discursive patterns: cultural assumption, register mismatch, prescriptivist bias, and erasure of cultural expression. A chi-square test of independence showed that the distribution of these patterns was similar across tools, indicating that the tools have shared training-based tendencies.

---

## uid: `arxiv:2608.15893v1`

- title: Breaking and Defending LLM-Powered Social Media Bot Detection Systems
- authors: Nof Orenstein, Yoni Birman
- affiliations: not stated
- posted: 2026-08-16
- source: arXiv
- link: https://arxiv.org/abs/2608.15893v1
- keyword hits: claude, large language model, large language models, llm, llms

### abstract

The rise of social media bots poses a persistent threat, enabling misinformation, opinion manipulation, and the erosion of trust in online platforms. To combat this, machine learning systems have been developed to detect and limit bot activity, but attackers continuously adapt through techniques such as adversarial learning and behavior imitation, fueling an ongoing arms race between bots and detection tools. Recent advances in large language models (LLMs) have significantly improved bot detection by enabling deeper semantic and contextual analysis of accounts and their content. However, this shift also introduces new attack surfaces, allowing adversaries to craft exploits that directly target the reasoning and generation mechanisms of LLM-based classifiers. Industry tools such as Anthropic's Claude Code Security similarly leverage LLMs for security-critical decisions, further motivating a careful study of their attack surfaces. In this work, we investigate both the offensive and defensive aspects of LLM-powered, threat-specific cybersecurity applications. While centered on the challenge of social media bot detection, our methodology and insights generalize to a broad class of LLM-powered cybersecurity systems, including phishing detection, email classification, and fraud analysis. We introduce two novel adversarial attack strategies that systematically exploit the semantic and contextual weaknesses of LLM-based classifiers, degrading their detection accuracy by up to 48%. To counter these threats, we propose a robust multi-LLM defense architecture designed to preserve detection reliability under adaptive adversarial conditions. Our solution, LSABRE (LLM-powered Social Adversarial Bot Recognition Ensemble), is a multi-LLM framework that substantially improves robustness across a range of attacks, maintaining 86% detection accuracy even under strong, adaptive adversarial pressure.

---
