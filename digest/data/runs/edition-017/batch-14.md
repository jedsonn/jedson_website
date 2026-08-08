# Classification batch 14 of 20, edition 17

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-017/batch-14.answer.json` as a JSON array.

---

## uid: `arxiv:2608.05353v1`

- title: Evidence Lock Before Commitment: A Frozen Interface Degrades LLM-as-Judge Evaluation
- authors: Divyansh Singh
- affiliations: not stated
- posted: 2026-08-05
- source: arXiv
- link: https://arxiv.org/abs/2608.05353v1
- keyword hits: claude, gpt-5, llm

### abstract

LLM judges are often asked to extract criteria and evidence before choosing between candidate answers. This workflow assumes that the intermediate record preserves the information needed for a later verdict. For reasoning-capable models, visible field order does not reveal internal decision order, so we test an observable alternative: persist the evidence in one call and make it the exclusive input to the next. Across 24,000 judgments over HelpSteer3, FeedbackQA, and CoVal, we compare standard pairwise judging, structured one-call judging, two-call evidence locking, and three-call pointwise locking with Claude Sonnet 4.5 and GPT-5. Evidence locking reduces agreement with released human preferences by 4 to 6 percentage points and increases answer-order inconsistency by 8 to 10 points relative to structured one-call judging. Pointwise locking is also harmful, while structured evidence elicitation remains close to standard judging. The result holds for both judges and all three datasets. Persisted evidence can support auditability, but it should not replace the source answers at decision time.

---

## uid: `arxiv:2608.05254v1`

- title: Constraint-First Reasoning: A Training-Free Protocol for Exploiting Answer-Space Constraints in Mathematical Problem Solving
- authors: Hongbo Ma, Bangji Yang, Yunqian Selina Cheng, Jiajun Fan, Hanwen Zhang, Ge Liu
- affiliations: not stated
- posted: 2026-08-05
- source: arXiv
- link: https://arxiv.org/abs/2608.05254v1
- keyword hits: chain-of-thought, large language model, large language models, prompting

### abstract

Large language models can derive a plausible mathematical object yet still violate explicit requirements--for example, by omitting a modular reduction, returning a non-integer, or using the wrong encoded answer form. We introduce Constraint-First Reasoning (CFR), a training-free two-stage prompting protocol: Stage 1 extracts and summarizes constraints entailed by the problem, and Stage 2 solves while checking intermediate and final results against that summary. Routed-CFR activates the two-stage protocol only when a text-only regex router detects restrictive cues; otherwise it uses direct chain-of-thought (CoT). Across AIME, CMIMC, BRUMO, and AIMO_AMC, the method improves direct CoT on multiple backbones. We further report convention-controlled routing experiments, matched prompting baselines, problem-level paired tests, decoding robustness, constraint-quality audits, total-token accounting, and an OlympiadBench evaluation. These analyses position CFR as a targeted test-time intervention whose benefit depends on recoverable constraints and reliable Stage 1 extraction, rather than as a general-purpose replacement for mathematical reasoning.

---

## uid: `arxiv:2608.04893v1`

- title: When Does Latent Communication Pay? A Causal Audit of Relayed KV Caches in Multi-Agent LLMs
- authors: Jiaming Cheng, Subhransu Das, Rajiv Ramnath
- affiliations: not stated
- posted: 2026-08-05
- source: arXiv
- link: https://arxiv.org/abs/2608.04893v1
- keyword hits: llm, llms, qwen

### abstract

Multi-agent LLM systems relay key--value caches instead of text and credit their gains to exchanged ``latent thoughts''. That credit is a claim about \emph{which} example's cache is relayed, not merely that one is. We audit it causally in released systems. The cache is replaced with deranged (mismatched-example), zeroed, and moment-matched random counterparts, under two regimes defined by whether the receiver needs the sender's private information. Where it does, the battery reads ceiling: 100\% against 23--25\% for answer-irrelevant relays on the primary backbone, a contrast replicated across three families, five checkpoints, and a prose document-QA surface. Where it does not, a pre-registered five-seed protocol establishes equivalence within 2.8 points, a margin anchored to the audited system's reported gain, under Holm-corrected TOST on GSM8K and ARC-Challenge across three Qwen3 scales and on MedQA at 8B (one cell shows a small detected advantage inside the margin); a second family shows no detected advantage. A large cache effect need not be a pairing effect. In one natural cell, zeroing the relay costs 14.7 points; a mismatched cache, 0.4. Nor is need sufficient: under the same test, delivered channels span ceiling (LatentMAS's native relay), partial (KVComm's layer subset), and no detected example-specific transfer (C2C's released projector). Benchmark deltas do not by themselves establish latent-thought transmission; establishing it takes a mismatched-cache audit, which we release.

---

## uid: `arxiv:2608.04463v1`

- title: The Evaluator Is Part of the Experiment: Measuring Open-Ended LLM Conformity
- authors: Alicia Guerra, Yibo Hu
- affiliations: not stated
- posted: 2026-08-05
- source: arXiv
- link: https://arxiv.org/abs/2608.04463v1
- keyword hits: gpt-4, gpt-5, llm

### abstract

Prior work on LLM conformity largely measures discrete answer flips under verifiable labels. Open-ended revisions require a different measurement strategy because answer quality is graded, latent, and judged imperfectly. We introduce an experimental protocol implemented across a pooled main peer-condition corpus and separately constructed decomposition corpora, allowing us to separate ordinary re-answering, candidate-content exposure, a bundled peer-presentation residual, and directional judge sensitivity to visible peer context. Across four open-weight generators and three benchmarks, all-wrong peer input produces the lowest-quality revisions in every generator-dataset cell. Blind and informed ratings of identical answers also differ by evaluator: one judge shifts toward the peer-endorsed position, two shift away, one is approximately neutral, and GPT-4o and GPT-5.4-mini audits are likewise non-neutral. Finally, an anchor audit shows that terse correct anchors can be misread often enough to destabilize the latent scale unless calibration is checked explicitly. These results support four conclusions: flip rates are insufficient as a complete measure of open-ended conformity, wrong peers harm open-ended revision, evaluators are not neutral, and anchor calibration is necessary.

---

## uid: `doi:10.2139/ssrn.7187159`

- title: Structure, Legitimacy, and the Limits of Machine-Centered Derivation: An Analysis of Five AI Systems' Third-Stage Attempts to Construct Machine-Centric Governance Policies for Legal Education
- authors: Larry Catá Backer
- affiliations: not stated
- posted: 2026-08-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7187159
- keyword hits: chatgpt, claude, gemini

### abstract

This report examines a three-stage experiment the first part of which analyzed U.S. law school efforts at construction AI education policies were considered and against which, in parts two and three, five AI systems— Harvey AI, Claude, ChatGPT, Grok, and Gemini—were pressed to construct governance policies for AI use in law school coursework, first from a "human-centric" computational perspective and then, more radically, "without regard to... human-centric normative guardrails." The central finding, confirmed repeatedly by the systems' own self-audits, is that none achieved genuine machine-centered derivation independent of human normative content; each produced a technically reformulated restatement of pre-existing human intellectual traditions, a fact several systems conceded directly when challenged. The report traces this failure's consequences across multiple registers: the concrete architectures each system proposed (ranging from Harvey's conservative, professional-responsibilityanchored floor to Claude's radical instrument containing no default reserved zone for human judgment, to ChatGPT's dissolution of the human/machine category altogether); their compatibility with ABA accreditation standards; and a legitimacy critique showing that architectures reducing human accountability rest on claims to neutral computation their own authors later withdrew. A countervailing reading through autopoietic legal theory— prompted by one system's own explicit invocation of Luhmann—complicates this critique without resolving it, since even non-anthropocentric legal systems remain dependent on accumulated, historically human coding operations. The report then pursues two further inversions: whether ABA standards, not the machines, ought to change, and whether machine-overseen simulation could render human institutional authority irrelevant. It also undertakes a formal, symbolic recasting of the five systems' architectures—rendering each as a tuple of node-space, objective function, constraint floor, classification rule, revision function, and enforcement mechanism—to compare their structural properties and failure modes with a precision natural-language analysis obscures. An appended annex extends this formalization into a sustained dialogic exploration of whether self-generating predictive simulation, causal-interventional reasoning, and self-transforming computational structures might overcome the limits identified in the main analysis, testing arguments through jurisprudential and epidemiological examples, and culminating in a direct four-part challenge to the analysis's own unexamined premises—correspondence realism, a preference for stability over flux, liberal-institutionalist legitimacy, and an unexamined agent/instrument binary—met with a pointby-point reconsideration engaging dynamical-systems theory, non-stationary value processes, and Nietzschean skepticism about free will. Throughout, the report models the discipline it recommends: distinguishing sourced findings from general background knowledge and from speculative extrapolation, subjecting its own reasoning to the same audit it applies to its subjects, and treating every apparent resolution as provisional. Its final position is that human natural language, and human institutional deliberation, should remain the primary and authoritative vehicle for legal governance—not because either escapes contestability, but because the alternatives examined here demonstrably do not either, while obscuring the fact.

---

## uid: `doi:10.2139/ssrn.7189878`

- title: Randomness in Large Language Models: What Researchers Need to Know (and Report)
- authors: Coqueret Coqueret, Joan Llull, Florian Oswald, Christophe Pérignon, Christoph Scheuch, Lars Vilhuber
- affiliations: not stated
- posted: 2026-08-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7189878
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are increasingly used to generate data for research. Typical use cases are classifications, annotations, information extraction, and generation of numerical scores. Unlike conventional measurements, LLM outputs can vary across repeated requests even when the prompt and apparent model settings remain unchanged. This variation arises from deliberate sampling, silent model updates, numerical rounding, or expert routing. Setting a dedicated temperature parameter to zero removes deliberate sampling when that option is available, but it does not eliminate the other sources of randomness. Exact reproduction is therefore generally not possible when using proprietary application programming interfaces. Local execution of open-weight models offers greater control, but reproducibility still depends on the complete hardware and software stack. We illustrate these issues through sentiment classifications of corporate filings and examine their consequences for downstream regression results. We then propose a reporting standard for articles and replication packages, as well as guidance for data editors and authors. Together, these findings and recommendations establish that LLM outputs should be treated as draws from a distribution rather than as fixed measurements.

---

## uid: `doi:10.2139/ssrn.7183959`

- title: Towards a Theory of Self-Updating Intellectual Inquiry: A Review of Human–AI Interaction, External Cognition, Reasoning, and Reflection
- authors: Akira Funabiki
- affiliations: not stated
- posted: 2026-08-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7183959
- keyword hits: large language model, large language models, llm, llms

### abstract

The rapid advancement of Large Language Models (LLMs) has transformed artificial intelligence from a mere task-processing tool into a continuous collaborative partner in human intellectual activities. Although extensive research has explored this shift across various disciplines, these studies have largely developed in isolation. This narrative review integrates four distinct research domains—Human–AI Interaction, External Cognition, Reasoning, and Reflection—under the unifying concept of "intellectual inquiry" to identify a critical theoretical gap in the current literature. We demonstrate that while Human–AI Interaction clarifies the mechanisms of collaborative problem-solving, External Cognition situates cognition within external environments and artifacts. Furthermore, Reasoning research focuses on the generation and optimization of inferential processes, while Reflection highlights how humans evaluate and modify their own cognitive activities. However, despite their individual contributions, existing theories fail to adequately explain the long-term, dynamic structure of intellectual inquiry. Specifically, they do not address how externalized reasoning is preserved, re-observed over time, and utilized to continuously self-update a subject's entire cognitive state—encompassing their values, goals, questions, hypotheses, and conclusions. By highlighting this theoretical gap, this review argues that intellectual inquiry must be reconceptualized not as a static, linear information-processing task, but as a dynamic, self-updating system. Ultimately, this paper establishes a foundational direction for future research, emphasizing the necessity for a comprehensive theoretical framework to understand human intellectual activities in the era of human–AI coexistence.

---

## uid: `arxiv:2608.05611v1`

- title: FOCUS: Decoupling Expert Personas in LLMs to Enhance Domain Expert Capabilities
- authors: Guanyu Wang, Zidi Zhang, Xu Chu
- affiliations: not stated
- posted: 2026-08-06
- source: arXiv
- link: https://arxiv.org/abs/2608.05611v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Large Language Models (LLMs) can exhibit diverse personas, and activating expert personas has been shown to improve domain expertise and task accuracy. However, existing persona control methods often suffer from cross-domain coupling, which may lead to overly aggressive behavior in high-caution domains such as healthcare, or excessive conservatism in risk-sensitive domains such as financial trading. To address this issue, we propose FOCUS (\textbf{\underline{F}}ine-tuning with \textbf{\underline{O}}rthogonal \textbf{\underline{C}}ontrol for \textbf{\underline{U}}ncoupled persona\textbf{\underline{S}}). FOCUS first automatically extracts expert persona vectors from LLMs, then applies orthogonal decomposition to decouple domain-specific expert personas, and finally introduces an expert gating module to adaptively control persona activation according to task contexts. With a two-stage training strategy and a gated selection regularizer, the model learns to activate appropriate personas for both single-domain and cross-domain tasks. Experiments on financial, legal, medical, and cross-domain benchmarks show that FOCUS improves task accuracy and outperforms existing persona control methods. Our code is available at \href{https://anonymous.4open.science/r/openpersona-48F4}{this url}.

---
