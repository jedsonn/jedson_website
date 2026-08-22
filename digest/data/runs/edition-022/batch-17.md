# Classification batch 17 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-17.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7277079`

- title: Generative AI Governance in iSchools: A Cross-Institutional Analysis of UNESCO's AI Ethics Principles
- authors: Nosakhare Okuonghae
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7277079
- keyword hits: generative ai, generative artificial intelligence

### abstract

As universities formalize institutional responses to the use of generative artificial intelligence (AI) systems, numerous ethical frameworks have been proposed to guide their responsible use in higher education. This study adopts UNESCO's Recommendation on the Ethics of Artificial Intelligence as an analytical framework to examine which ethical principles are reflected in generative AI policies across iSchools. A qualitative content analysis of policies from 136 iSchools was conducted using six UNESCO ethical principles as the analytical framework. Responsibility and accountability (53.7%) and awareness and literacy (52.2%) were the most frequently reflected ethical principles. Fairness and non-discrimination (20.6%) and privacy and data protection (38.2%) appeared in fewer institutional AI policies. The analysis also showed that institutional AI governance extends beyond policy documents to include institutional decisions regarding approved AI tools. The findings show that institutional AI governance is characterized by the selective reflection of ethical principles in policy and operationalized through institutional support for generative AI tools.

---

## uid: `arxiv:2608.17050v2`

- title: Cross-Model Memory Transfer via Target-Side Reader Adaptation
- authors: Mingyuan Li, Guangsheng Yu, Xu Wang, Shaoxiong Ji
- affiliations: not stated
- posted: 2026-08-17
- source: arXiv
- link: https://arxiv.org/abs/2608.17050v2
- keyword hits: large language model, large language models

### abstract

Methods for improving knowledge use in large language models typically fall into two regimes. Non-parametric retrieval offers flexible access to external knowledge, but adds retrieval latency, context overhead, and only shallow integration with the backbone. Parametric adaptation is efficient at inference time, but entangles knowledge with model weights and can be hard to update, audit, or transfer. Engram-style hashed memory occupies a middle regime: it stores learned information in an external, addressable table, yet consumes that table through a small learned reader. This raises a basic question: when such a memory is moved across backbones, what matters more, the frozen memory itself or the target-side reader? We study this question through cross-model frozen-memory extraction, in which a memory trained on a source model is frozen and attached to a different target model, with only a lightweight reader trained. Ablations show that learned memory content and correct addressing both matter, but the transferred table becomes useful only through a reader aligned to the target model. In downstream question answering tasks, a dual-layer, four-branch reader nearly closes the gap between same-model and cross-model reuse, achieving an average score of 38.8 under our controlled evaluation protocol. Moreover, when the provider reader is directly compatible with the target interface, the frozen artifact can provide substantial utility without target-side training, while optional reader adaptation yields further improvement. These results suggest that Engram can serve as a reusable external knowledge artifact, provided that the target has access to a compatible reader interface; target-side adaptation can further improve alignment when direct reader reuse is insufficient.

---

## uid: `doi:10.2139/ssrn.7306318`

- title: LLM-Guided Hierarchical Learning for Zero-shot Image Classification
- authors: Na Chen, Tianyu Cheng, qun chen, Wenjie Liu, zhanhuai li
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7306318
- keyword hits: large language model, llm

### abstract

As visual recognition systems are increasingly expected to generalize beyond seen categories, zero-shot image classification, which aims to identify unseen classes based on category semantics, has become a critical research problem. Many existing approaches treat all candidate categories as a single label space and perform prediction in a flat manner. However, such a flat formulation overlooks the inherent hierarchical organization of real-world categories and requires a shared representation space to support both coarse-grained and fine-grained discrimination, thereby limiting the ability to distinguish closely related unseen classes. To alleviate this limitation, this paper presents LG-HL, LLM-Guided Hierarchical Learning, for zero-shot image classification that transforms flat categorization into coarse-to-fine hierarchical categorization. It gradually narrows candidate categories through coarse-to-fine hierarchical inference and level-wise representation refinement. Specifically, it first employs a large language model to construct a task-specific category taxonomy and generate hierarchy-aware textual descriptions through sibling differentiation and ancestral abstraction. It then uses high-confidence pseudo-labels from unlabeled test images to adapt level-specific text representations through hierarchy-aware contrastive learning, which jointly promotes local cross-modal alignment, ancestor consistency, and sibling separation. Experiments on seven benchmark datasets with two CLIP backbones show that LG-HL outperforms the corresponding CLIP baseline on all datasets and achieves the best performance among the compared methods on six of the seven datasets under both backbones, demonstrating the effectiveness of explicitly modeling hierarchical semantic structure for zero-shot visual recognition.

---

## uid: `doi:10.2139/ssrn.7283081`

- title: From Ledgers, to Options, to Latency A History of Trading, Mathematical Finance, and the Quant Profession
- authors: Paul Alexander Bilokon
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7283081
- keyword hits: large language model, large language models

### abstract

The quantitative finance profession is often narrated as a late-twentieth-century consequence of option-pricing theory, electronic markets, and the migration of mathematicians and physicists to Wall Street. That account is correct but incomplete. The modern quant is the latest expression of a much longer co-evolution among five systems: institutions of exchange, mathematical representation, information technology, organisational specialisation, and regulation. This paper develops that thesis from the prehistory of money and markets to machine learning and large language models. It treats merchant accounting, bills of exchange, bourses, joint-stock companies, organised derivatives markets, telegraphy, the stock ticker, and the formation of specialised trading desks as genuine antecedents of quantitative work rather than as decorative prehistory. It then follows the mathematical line from Bachelier through axiomatic probability, stochastic calculus, portfolio theory, asset pricing, no-arbitrage valuation, volatility modelling, market microstructure, optimal execution, and modern computational statistics. Parallel to this intellectual history, it traces the professional line from mathematically sophisticated merchants and actuaries to portfolio "quantifiers," derivatives quants, systematic hedge funds, electronic market makers, quantitative developers, risk quants, data scientists, and AI-assisted researchers. The paper also argues that the profession cannot be understood by following theory alone. Each wave of quantification depended on a matching substrate of market data, computing, communication, and institutional demand. Conversely, mathematical models reshaped the markets in which they were deployed, while crises and regulation repeatedly redirected quantitative labour toward new problems such as value-at-risk, counterparty exposure, xVA, capital, liquidity, execution quality, and model risk. The result is a history in which the quant is not a single occupation but a family of roles occupying the interface between formal models and executable decisions.

---

## uid: `doi:10.2139/ssrn.7287199`

- title: Colophon: Per-user Traitor Tracing for Chatbot Text that Survives Paraphrase
- authors: Karthik Hosur
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7287199
- keyword hits: large language model, llama, llm

### abstract

We study traitor tracing for large language model (LLM) chatbots: embedding a secret, per-user signature in a bot's answers so that a leaked conversation can be attributed to the account that produced it, while remaining legible only to the key holder. Unlike token-level watermarks, whose signal lives in exact wording and is therefore erased by paraphrasing, we place the signature in content decisions: which of several near-equivalent content "atoms" (points, tips, examples) a response includes (a channel immune to reordering) and in what order (a pairwise-coded channel). The mark is keyed by a pseudorandom function so that any text produced without the key is, to the detector, a sequence of fair coins-yielding an exact, distribution-free null and, with a positioncollapse correction, controlled false-accusation rates. Generation uses a plan-then-write pipeline; detection recovers atoms from paraphrased leaked text by sentence-embedding canonicalization and scores them with an adaptive inverse-variance channel fusion; collusion resistance uses Tardos codes. We validate on model-generated and real human content (Reddit LifeProTips), against a strong (Llama-70B) paraphrase attacker and a standard local paraphraser. The honest picture, reported with confidence intervals: verbatim and normal-paraphrase leaks are traced in essentially every resample, moderately-aggressive rewriting in ≈ 83%, and round-trip translation likewise, all with zero false accusations in our runs-a control we validate at scale by family-wise-error simulation up to 10 6 users-while a maximally-determined attacker who aggressively rewrites and reorders evades a short 12-message leak and is caught only as ≈two dozen messages accumulate. Head-to-head on identical content, the content channel strictly dominates a SemStamp-style semantic watermark and a token green-list on paraphrase robustness (retaining 0.6-1.0 of its detection power versus 0.2-0.5), and on content-preserving attacks an oracle ablation shows the residual gap is recognizer-limited, not fundamental erasure. The mark applies to ≈ 57% of instruction traffic and carries a measurable generation-quality cost that we report honestly-and show is partly reducible, with detection staying well above the accusation line, by softer generation. Its sharpest limit is that an adversary who reverse-engineers the atom pool (feasible in a handful of queries) can then erase the mark cheaply: it is a forensic layer against non-adaptive adversaries, not a guarantee against a pool-aware one. Our contribution is a systems-and-threat-model result with an honestly measured robustness boundary: individual mechanisms have prior art; the composition-content selection-and-ordering as a per-user codeword, Tardos over an LLM text channel, and the measured frontier-does not.

---

## uid: `doi:10.2139/ssrn.7303345`

- title: Evaluating LLM-Assisted Linguistic Coding across Heterogeneous Annotation Features: A Behavioral-Profile Study
- authors: Yufeng WU, Esther Asare, Meichun LIU
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7303345
- keyword hits: large language model, large language models, llm

### abstract

Large language models are increasingly used to assist linguistic coding, but their validity as research instruments may vary across the heterogeneous decisions contained in a single annotation scheme. We examine this problem using a 12-feature Behavioral Profile scheme for Chinese color-term derivatives as a heterogeneous linguistic coding testbed. A fixed committee of three locally served open-weight models evaluated 240 held-out instances after development on 60 items. For the ten features with sufficiently reliable human-human kappa estimates, the committee's kappa confidence interval lay entirely above the human-human kappa estimate for two features, overlapped it for four, and lay entirely below it for four; two further features were reported descriptively because human-human kappa was low. Majority voting improved kappa over the mean constituent model for all ten comparison features and accuracy for nine. Class-level analysis nevertheless exposed minority-role failures, especially for semantic role, and model consensus did not guarantee correctness. A development-selected rule revision reduced a recurrent word-class error on held-out data without eliminating the difference from the human-human kappa estimate. These findings show that the reliability of LLM-assisted linguistic coding is feature-specific rather than system-wide. Validation should therefore combine human-human kappa, gold agreement, class-level diagnostics, and model-consensus information, while separating development gains from held-out evidence.

---

## uid: `doi:10.2139/ssrn.7291338`

- title: Measuring In-Context Behavioral Adaptation of AI Agents Across Repeated Tasks
- authors: Sahir Maharaj
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7291338
- keyword hits: ai agent, in-context learning, large language model

### abstract

An agent that fails once and succeeds on the next attempt appears to have learned, but that appearance is surprisingly easy to mismeasure. Large language model agents can change behavior at inference time while their model weights remain fixed: they can retain a failed trajectory, receive verifier feedback, write a reflection into memory, retrieve a prior experience, or infer a reusable procedure from earlier errors. Yet a better second attempt can also arise from stochastic resampling, additional compute, easier environmental state, evaluator leakage, or literal patching that does not transfer. This paper develops an operational framework for separating these cases. We define failure-driven in-context behavioral adaptation as a causal change in an agent policy produced by failure information carried across attempts under fixed model parameters. We synthesize evidence from in-context learning, reflection, selfcorrection, experiential learning, memory-augmented agents, interactive benchmarks, and 2025-2026 work on self-evolving memory and agent transfer. The evidence supports a qualified conclusion: nonparametric adaptation is real, but it is conditional. External or environment-grounded feedback is substantially more reliable than unconstrained intrinsic self-critique; memory benefits depend on retrieval and task structure; and current automatic self-evolution methods can improve some settings while regressing in others. We introduce ICBA-RT, a repeated-task evaluation protocol that isolates same-task repair, cross-episode adaptation, procedural transfer, persistence, regression, and cost, together with ADAPT-12, a taxonomy of twelve failure-to-adaptation modes. The central methodological claim is that repeated success is not sufficient evidence of learning. Strong evidence requires matched fresh-start controls, state resets, held-out related variants, causal ablations of the feedback channel, and persistence tests. For deployment teams, the implication is practical: an agent can become behaviorally better without retraining, but only when experience is converted into trustworthy, retrievable, appropriately scoped state and when improvement is measured against the right counterfactual.

---

## uid: `doi:10.2139/ssrn.7303344`

- title: Parsing structured semantic knowledge from arbitrary text with GenAI: A tutorial
- authors: Adrielli Tina Lopes Rego, Joshua Snell, Martijn Meeter
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7303344
- keyword hits: generative ai, large language model, llm

### abstract

Frame Semantics offers a compelling framework for representing meaning as structured conceptual scenarios (frames). FrameNet operationalizes this theory as a lexical resource linking words to frames and their conceptual roles (frame elements, FEs). However, applying Frame Semantics to arbitrary text has historically required either laborious manual annotation or complex, task-specific classification pipelines that presuppose known targets and/or frames. Here we present a step-by-step tutorial for a simple, open-source method that leverages Generative AI (GenAI) to automatically parse semantic frames and their FEs from any input text, without requiring pre-specification of frames or target spans, or task-specific model training. The tool combines a retrieval step, in which candidate frames are identified via embedding-based semantic similarity, with a selection step, in which a Large Language Model (LLM) is prompted, using zero- or few-shot examples, to determine which frames are evoked, which spans trigger them, and which spans fill their FEs, returning a structured, machine-readable output. We detail installation, execution, and output interpretation, and provide a built-in evaluation module supporting exact, semantic, and graph-based matching against FrameNet's human-annotated data. This freely available tool lowers the barrier to frame-semantic analysis for researchers across linguistics, who wish to explore structured semantic content in naturalistic text, including in relation to behavioral and neural measures of language comprehension.

---
