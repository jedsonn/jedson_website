# Classification batch 20 of 22, edition 21

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-021/batch-20.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7284980`

- title: Why Firms May Continue to Fund Scaling Despite Uncertainty About Autonomous Research
- authors: Lewis Lewin
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7284980
- keyword hits: large language model, large language models

### abstract

A companion paper argued that scale alone does not produce instructional competence: large language models trained on more data with more parameters do not thereby acquire the structure that expert-designed instruction supplies (Lewin, 2026d). This paper asks a question that argument leaves open. If the claim is correct, and if evidence for it keeps accumulating, why does the field keep betting on scale anyway? Part of the answer requires separating two things that are easy to conflate: scaling is a technical mechanism — adding data, parameters, and compute — while automation is a technical target: building a system that can set its own research agenda, run its own experiments, and judge its own results without continuing human involvement. What makes automation, rather than scale, the thing that gets financially rewarded is what automation promises to eliminate: the ongoing cost of expert-designed instructional structure. Scaling is simply the strategy the field is currently betting will get it there, and that distinction matters because it is automation's promise of not needing that structuring — not scale for its own sake — that this line of research argues is the actual bottleneck. Companies are not skipping that structuring step by accident while pursuing automation; avoiding that cost is plausibly close to the actual reason full automation is attractive in the first place — a system that runs its own research end to end is, among other things, a system that does not require paying for expert-designed instruction. Recent evidence adds to, without single-handedly settling, the underlying instructional argument. A 2026 shadow evaluation study, based on two case studies, found that frontier AI research agents, given six days and substantial compute, could accurately judge that their own work fell short of publication standards, yet could not use that accurate judgment to generate a better approach — a dissociation the study's authors term a generator-verifier gap, and this paper treats as one of the more instructive pieces of evidence so far for separating knowledge from operative competence. At the same time, a single illustrative case — Recursive Superintelligence, capitalized at more than $4 billion in 2026 — shows the automation bet continuing in spite of, not in ignorance of, this evidence, though one case cannot establish a general pattern on its own. A historical precedent from outside AI research — the 2023 suspension of Cruise's robotaxi operating permit in San Francisco — suggests the same pattern, automation pursued through a scaling strategy, may predate the current generation of language models. This paper argues that the economic attractiveness of full automation is substantially increased if expert-designed instructional structures can ultimately be eliminated or greatly reduced, whether or not that elimination is technically achievable given current evidence, and that scaling persists as the field's leading strategy for reaching that goal.

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

## uid: `doi:10.2139/ssrn.7284398`

- title: Leaving the Scene after Vehicle-Train Collisions: Factors Associated with Post-crash Flight at U.S. Highway-Rail Grade Crossings
- authors: Pouyan Saiedian, Salvador Hernandez, Rakan  Mohammad Radwan Albatayneh, SM Rahat Rahman
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7284398
- keyword hits: large language model, llm

### abstract

Objectives: This study examines factors associated with post-crash flight among surviving drivers in highway-rail grade-crossing (HRGC) crashes, with emphasis on driver impairment. This study extracts post-crash-flight and impairment indicators from Federal Railroad Administration (FRA) narratives and evaluates their associations with driver, vehicle, crossing, environmental, train, and crash characteristics. Methods: A national FRA dataset of more than 17,000 HRGC crashes from 2005-2025 was analyzed. A large language model extracted binary indicators of post-crash flight and driver impairment from crash narratives. Post-crash flight was modeled as the target variable using binary logistic regression. Findings: Descriptive results showed that 4.77% of surviving drivers left the scene after an HRGC crash. The model indicated that driver impairment was strongly associated with this behavior: impaired drivers had 2.54 times the odds of leaving the scene than other drivers. Injured drivers had 88.7% lower odds of leaving than uninjured drivers. Higher odds were also associated with younger age, male drivers, passing another vehicle before the crash, and crashes occurring in darkness. These findings show that post-crash flight is related to driver condition, risky behavior, environmental conditions, and crash context. Novelty: This study is among the first national analyses of drivers leaving the scene after vehicle-train collisions at HRGCs. It also shows how structured FRA data can be combined with LLM-derived indicators of driver impairment and post-crash flight extracted from crash narratives. Practical Applications: The findings can support targeted crossing surveillance, rapid preservation of locomotive and crossing-camera recordings, and improved coordination between railroads and local lawenforcement agencies. The model may also help insurance companies identify higher-risk claims, prioritize investigations and support fraud detection. In addition, the results support adding structured fields for postcrash flight and driver impairment to FRA reporting systems, which could improve driver identification, data quality, infrastructure-damage recovery, and safety planning.

---

## uid: `doi:10.2139/ssrn.7305334`

- title: Model-Fixable or Architecture-Fixable? A Failure Taxonomy for Model-Agnostic Clinical Entity Extraction and Ontology Coding
- authors: Hemachandran Babu, Priyadarsini K
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7305334
- keyword hits: large language model, llm

### abstract

Background and Objective: Clinical entity extraction systems built around a single large language model inherit that model's specific quirks and failure modes. Swapping the model later causes some errors to vanish while new ones appear. Existing work reports per-model accuracy without asking whether an error belongs to the model or to the surrounding system. This paper asks whether extraction failures can be systematically attributed to the model versus the architecture so that teams know what to fix.Methods: We propose a modular model-agnostic framework for clinical entity extraction and ontology coding, in which extraction, ontology coding and validation are separated into independent components communicating through a fixed schema so that the underlying LLM can be replaced without redesigning the system. Building on this we developed a failure taxonomy synthesized from failure patterns already reported across the clinical NLP and LLM extraction literature, classifying each failure mode as either model-fixable (changes when the LLM is swapped) or architecture-fixable (persists regardless of which model sits underneath).Results: The taxonomy identifies distinct failure categories and classifies them against the criteria alongside a proposed controlled validation experiment for testing these classifications empirically. As this classification is derived from literature synthesis rather than a new experiment run, the model-fixable/architecture-fixable labels are proposed classification hypotheses, meant to guide future testing and not confirmed results.Conclusion: Separating model level failures from architecture-level failures gives clinical NLP teams a systematic way to decide whether a performance problem calls for a model upgrade or a pipeline redesign rather than defaulting to the easiest option.

---
