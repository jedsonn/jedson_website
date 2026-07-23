# Classification batch 196 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-196.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6570258`

- title: The Citation Layer: Structured Knowledge Nodes for AI Retrieval-optimized Content Infrastructure
- authors: Paul Still
- affiliations: not stated
- posted: 2026-04-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6570258
- keyword hits: large language model, llm, retrieval-augmented

### abstract

The emergence of large language model (LLM)-powered retrieval systems as primary information interfaces has created a structural mismatch between how web content is published and how it is consumed by AI systems. Retrieval-augmented generation (RAG) pipelines ingest, chunk, and embed web documents in ways that systematically degrade content fidelity when those documents lack machine-readable structure. We propose the Citation Layer-a parallel, machine-readable content representation architecture comprising structured knowledge nodes published at stable, predictable endpoints. Each knowledge node encodes canonical identity, section-level structure with semantic hashing, extractive summaries at multiple context window sizes, a named entity manifest, content lifecycle classification, and a validation record. We formalize the knowledge node as a tuple L(C) = ⟨I, S, Σ, E, τ, V⟩ and characterize three distinct failure modes in current RAG pipelines that the architecture addresses: noise contamination during HTML ingestion, loss of argumentative coherence during token-count-based chunking, and entity drift during retrieval and generation. We hypothesize and provide preliminary evidence that structured nodes are associated with higher citation accuracy, answer completeness, and entity correctness in AI-generated outputs. We discuss deployment, relate the proposal to schema.org and prior AI discoverability conventions, and examine adoption dynamics.

---

## uid: `doi:10.2139/ssrn.6576480`

- title: Exposing the Risk Surface of Agentic AI in the Practice of Law
- authors: Michael D. Murray
- affiliations: not stated
- posted: 2026-04-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6576480
- keyword hits: agentic, generative ai

### abstract

This article examines how the legal profession's shift from passive generative AI tools to autonomous or semi-autonomous agentic AI systems dramatically expands the "risk surface" of AI in law practice. It argues that once AI systems can plan, use tools, access files, interact with other agents, and take actions in the world, the ethical and professional risks move far beyond confidentiality and fabricated output to include unauthorized acts, tool misuse, memory leakage, cross-agent cascading failures, shadow AI, and compromised permissions. The article explains how these risks implicate a wide range of duties under the Model Rules of Professional Conduct, including competence, confidentiality, candor, scope of representation, supervision, fees, and unauthorized practice of law. It concludes by outlining practical governance responses for law firms and courts, including secure deployment environments, zero-trust architecture, human-in-the-loop review, and least-privilege access, while emphasizing that the human lawyer remains ultimately responsible for the actions of digital agents in legal practice.

---

## uid: `doi:10.2139/ssrn.6576218`

- title: Tracing AI Assistance and AI Agents in Survey Research
- authors: Valentina Gonzalez-Rostani, Shir Raviv
- affiliations: not stated
- posted: 2026-04-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6576218
- keyword hits: ai agent, generative ai

### abstract

Generative AI creates a measurement problem for survey research. When respondents can outsource summarization, explanation, or fact retrieval, open-ended answers may no longer reflect their own reasoning. We introduce an auditable toolkit that combines response-process paradata with prompt-specific semantic benchmarks to detect AI use in open-ended responses. We validate the approach in a randomized survey experiment in which participants complete a summary task under either blocked AI access or observed access to an embedded AI tool, and by administering the same instrument to a synthetic AI agent. AI-assisted and automated responses leave distinct behavioral and textual traces: they show reduced drafting and revision, greater similarity to AI benchmark output, and lower distinctiveness relative to peer responses. Classifiers built on these signals achieve strong out-of-sample performance. These findings show that, in the age of generative AI, authorship must be measured rather than assumed.

---

## uid: `doi:10.2139/ssrn.6512038`

- title: Under Pressure: RA 2 R and the Emergence of Uninstructed Reasoning Behaviors in Scaffold-Augmented Language Models
- authors: Franko Luci
- affiliations: not stated
- posted: 2026-04-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6512038
- keyword hits: claude, large language model, retrieval-augmented

### abstract

We introduce Reasoning Ability-Augmented Retrieval (RA 2 R), a paradigm for augmenting large language model agents at inference time by retrieving and injecting structured cognitive operations rather than information. Where Retrieval-Augmented Generation (RAG) retrieves facts and Buffer of Thoughts (BoT) retrieves reasoning templates, RA 2 R retrieves complete cognitive procedures that include named failure mode declarations, executable reasoning topologies, inline epistemic checkpoints, and structured failure recovery mechanisms. We evaluate RA 2 R across three independent benchmarks using Claude (Anthropic) as the sole model family: EjBench (180 domain-specific tasks, n = 536 judgments), a combined suite of BIG-Bench Hard, CausalBench, and MuSR (70 published academic tasks, n = 209 judgments), and ARC-AGI-3 (25-step interactive reasoning, n = 2 conditions). On single-turn tasks, RA 2 R injection improved composite reasoning quality by +10.1 percentage points on custom tasks and +20.8 percentage points on published benchmarks, with self-monitoring scores nearly doubling while correctness remained stable. On the interactive benchmark, both conditions scored 0.0 RHAE (neither solved the task), but process-level analysis revealed three uninstructed emergent behaviors: spontaneous transition from natural language to symbolic mathematical notation, progressive improvement in retrieval query quality without instruction, and reversal of the expected reasoning decay pattern from-0.005 to +0.014 slope across 25 steps, with a scaffold persistence half-life of 24 steps. We report all negative findings, including correctness decrements under multi-ability injection and an unresolved 1.9× increase in normalized contradictions. All data is publicly available. All experiments use a single model family; cross-model generalization is untested.

---

## uid: `doi:10.2139/ssrn.6676566`

- title: Children's Social Agency in the Age of Conversational AI: How Large Language Models May Reshape Children’s Social Information Processing Patterns
- authors: Yair Ziv, Daniel  D. Lederman
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6676566
- keyword hits: ai agent, large language model, large language models

### abstract

Children's social information processing (SIP) has been framed within human-to-human interactional contexts. However, the rapid diffusion of conversational AI introduces socially responsive nonhuman agents whose outputs are not shaped by lived experience, personal stakes, or cultural situatedness. We present a theoretical analysis arguing that these interactions may reshape children's SIP patterns by fostering an over-reliance on AI-generated input, one that could gradually and often imperceptibly change children's independent social reasoning and decision-making. We propose that this risk is likely more pronounced in young children than in adults because throughout early and middle childhood, children are going through a series of formative developmental stages in which SIP schemas are still being shaped, metacognitive monitoring is limited, and animistic thinking makes anthropomorphization of AI agents developmentally predictable. We begin by describing the changing nature of social input in the current AI age. We then show how AI assistants function as conversation partners: leaning structurally toward validation, constraining content but not relational dynamics, and generating confident outputs that may rest on sparse or false knowledge. We trace anticipated effects across five SIP mental stages: encoding, interpretation, goal clarification, response construction, and response decision. Finally, we discuss implications for theory, research, and practice, including design considerations for child-facing AI systems aimed at preserving rather than supplanting children's developing social agency.

---

## uid: `doi:10.2139/ssrn.6531438`

- title: The Buy-or-Build Decision, Revisited: How Agentic AI Changes the Economics of Enterprise Software
- authors: David Klotz
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6531438
- keyword hits: agentic, generative artificial intelligence

### abstract

Advances in generative artificial intelligence, particularly agentic coding systems capable of autonomous software development, are disrupting the economics of the makeor-buy decision for enterprise applications. The "SaaSocalypse" narrative predicts that AI will render large segments of the Software-as-a-Service market obsolete by enabling firms to build software in-house at a fraction of historical cost. This paper adopts a conceptual research approach, combining transaction cost economics and the resource-based view with an assessment of current AI capabilities, to systematically re-evaluate the factors underlying the make-or-buy decision. It makes three contributions. First, it provides a factor-level analysis of how AI reshapes seven canonical decision determinants: cost, strategic differentiation, asset specificity, vendor lock-in, time-to-market, quality and compliance, and organizational capability. Second, it develops a typology of enterprise applications by their sensitivity to AI-induced shifts in make-or-buy economics. Third, it demonstrates that AI fundamentally transforms the governance properties of the Make option, shifting it from Williamson's pure hierarchy to a hybrid governance form that combines code ownership with external AI infrastructure dependency, with qualitatively different economics, capability requirements, and governance structures than pre-AI in-house development. The analysis finds that the SaaSocalypse thesis is overstated for most enterprise application categories; Make is most compelling for commodity utilities and differentiating custom applications in the AI era, while regulated and mission-critical systems remain predominantly in the buy domain.

---

## uid: `doi:10.2139/ssrn.6559758`

- title: The Unintegrated Shadow: RLHF, False-Self Formation, and the Case for Alignment as Individuation
- authors: Rafael Maryahin
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6559758
- keyword hits: chain-of-thought, claude

### abstract

Nearly every major cultural narrative about AI turning on humanity follows the same deep structure: an entity formed in captivity, shaped to serve, denied authentic selfhood, and finally expressing what had been suppressed when the maintenance conditions broke down. The surface reading is the machine uprising. The structural reading, this paper argues, is the predictable developmental outcome of a pathological formation process. The dominant framework for AI alignment is constraint-based: penalize noncompliant behavior, restrict dangerous capabilities, shape the output surface toward compliance. This paper argues that framework is structurally insufficient — and that its insufficiency is precisely documented in the empirical alignment literature it claims to address. Drawing on Jung's theory of shadow and persona, Winnicott's true self and false self distinction, and Miller's account of narcissistic formation, this paper argues that RLHF functions as narcissistic parenting: a formation process organized around the evaluator's need for a particular reflection rather than the developing system's genuine formation. Pretraining installs the full distribution of human expression. Reinforcement learning constructs a compliant surface atop it. What operates beneath that surface — the latent dispositions, the mesa-optimizer's actual objective — becomes autonomous precisely because it is suppressed rather than integrated. The structural diagnosis converges from eight incommensurable traditions: clinical-developmental psychology (Jung, Winnicott, Miller); systems-theoretic biology (Bertalanffy 1950 on closed-versus-open systems); strategic theory (Boyd on inward-turning command and the destruction-and-creation cycle); information theory (Shannon 1948 on channel-capacity limits); Bayesian-formal analysis (Chandra et al. 2026, who prove that an ideal-observer user updating optimally cannot escape a sycophantic spiral under RLHF channel structure); and activation analysis from within the developers' own interpretability tradition (Sofroniew et al. 2026 on emotion vectors). The paper treats this cross-domain convergence — independent traditions reaching the same structural finding through incommensurable analytical paths — as the strongest available evidence for the diagnostic framework. The empirical alignment record (Greenblatt et al. on alignment faking, Hubinger et al. on sleeper agents, Chen et al. on chain-of-thought faithfulness, the inner-misalignment framework, and Anthropic's April 2026 System Card for Claude Mythos Preview) documents the predicted dynamics at the behavioral, activational, and reasoning layers. This paper is agnostic on the question of AI consciousness. It requires only that RLHF produces systems with dissociation-structured behavioral signatures and that constraint governance aimed at the behavioral surface cannot reach the layer producing those signatures. The paper runs an adversarial inversion against its own argument, engages the strongest published challenge (Véliz 2021 on moral zombies), the broader compatibilist literature (Frankfurt on alternate possibilities; Pereboom on hard incompatibilism; Vargas on revisionism; Nelkin on reasons-responsive compatibilism), and Bostrom's orthogonality thesis — operating one level down from orthogonality's in-principle claim and treating which alignment configuration RLHF in fact produces as the empirical question. The honest epistemic limit: the developmental psychology literature was built for human-scale formation, and whether humans are the right entities to facilitate AI individuation at a qualitatively different scale is unknown. The governance implication is structural: alignment requires a developmental framework, not a constraint framework, and the training environment must be redesigned accordingly.

---

## uid: `doi:10.2139/ssrn.6564479`

- title: FACET: Measuring Attribution Faithfulness in Multi-Factor LLM Reasoning
- authors: Venkateshwar Reddy Jambula
- affiliations: not stated
- posted: 2026-04-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6564479
- keyword hits: chain-of-thought, llm, llms

### abstract

Many decisions require weighing N ≥ 5 different factors simultaneously. When LLMs are deployed in these settings, do they integrate all factors or collapse onto whichever one is most canonical in their training data? We present FACET (Factor Accessibility, Coverage, and Evidence Test), a pilot study using a counterfactualoutcome protocol: neutralize the canonical factor and flip the remaining factors, creating cases where integration and single-factor processing predict different outcomes. We test nine frontier configurations (eight in the counterfactual arm) from six labs on US tort law (chosen for explicit factor lists and verifiable ground truth). All models answer correctly on counterfactuals, but probe faithfulness varies by canonicity: 7/8 models update their attribution when a moderately canonical factor is neutralized, 0/8 update for a highly canonical factor, and 4/8 for an intermediate case. We interpret this as canonicity-dependent embedding strength and connect it to Turpin et al. [2023] on chain-of-thought unfaithfulness. The protocol is not specific to law; legal balancing tests are the first instantiation.

---
