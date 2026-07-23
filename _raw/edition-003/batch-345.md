# Classification batch 345 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-345.answer.json` as a JSON array.

---

## uid: `arxiv:2607.12790v1`

- title: Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents
- authors: Xing Zhang, Guanghui Wang, Yanwei Cui, Ziyuan Li, Wei Qiu, Bing Zhu, Peiyang He
- affiliations: not stated
- posted: 2026-07-14
- source: arXiv
- link: https://arxiv.org/abs/2607.12790v1
- keyword hits: llm

### abstract

Self-evolving agent systems improve by creating, revising, and retiring their own skills, but every such loop rests on a hidden assumption: a reliable evaluation metric already exists. In many real applications it does not. We make three claims. First, metrics can be \emph{evolved}: our metric loop searches compositions of small drawback detectors under a full evolutionary lifecycle, trained to agree with a ten-item anchored reference set, regularized by consensus over unlabeled outputs, and audited against a held-out anchor it never reads, yielding a transparent, inspectable metric rather than an opaque judge. Second, since no metric exists to beat, the yardstick is recovering what an accurate metric would have enabled, and \emph{Double Ratchet}, our co-evolution of the metric with a lifecycle-managed skill loop, does so: across code generation (MBPP+), enterprise text-to-SQL (Spider~2.0-Snow), and reference-free report generation, it retains 88--110\% of the held-out lift achieved by the same skill loop driven by ground truth or the best available rubric. Third, safety comes from anchor discipline plus outer audits: removing anchor guards collapses the metric into a vacuous detector while removing the lifecycle does not; and when evolved skills gamed the report rubric, an independent judge caught it, one detector repaired it, and a task-aware judge then preferred the evolved outputs over the pre-evolution baseline in 77\% of decided pairs. We argue this failure-expecting architecture is the right default wherever no reliable automatic verifier exists.

---

## uid: `arxiv:2607.12520v1`

- title: The Model Knows Your Project, Not You: Measuring Recognition in LLMs with NameRank
- authors: Bojie Li, Noah Shi
- affiliations: not stated
- posted: 2026-07-14
- source: arXiv
- link: https://arxiv.org/abs/2607.12520v1
- keyword hits: llm, llms

### abstract

What a frontier model recalls about a person or tool from its own weights -- before any retrieval step -- often shapes the first description a human sees, making that parametric corpus presence a measurement problem. Citations explain about a third of whether a model recognizes a researcher; we target the residual and build NameRank, a [0,1] recognition score: each of 4,685 entities in 54 cohorts is probed with one open-ended question across 36 models, and an independent judge returns a binary verdict against a curated gold -- did the model state a specific, non-guessable fact about this exact entity? -- so hallucination, context echo, and guesses earn nothing. Synthetic-null entities hold the floor near zero, and verdicts track the entity, not the model. One thesis organizes the findings: recognition is paid to named, indexable artifacts, not to credentials or titles. Every Olympic-style credential sits below a working-researcher baseline, because no named artifact ships with the medal, yet the ranking inverts at the marquee tier, where Nobel, Turing, and Fields laureates saturate the panel. For independent creators the tool out-ranks its maker, and the credential that does propagate is a named method or awarded paper. Being one of many named contributors to a celebrated artifact, by contrast, earns almost nothing -- the authors listed on a flagship model report or system card sit near the recognition floor -- because recognition attaches to the artifact's own distinctive name, not to the roster behind it. No bibliometric predicts recognition well; top-density institutions out-recognize peers at matched citations; and on 258 news events recognition loads on peak salience, not persistence. A self-report probe shows introspection reads a corpus prior, not its own knowledge.

---

## uid: `arxiv:2607.12480v1`

- title: TRACE: An Operational Reasoning Schema for Auditable Agentic Commitments
- authors: Edward Y. Chang, Emily J. Chang
- affiliations: not stated
- posted: 2026-07-14
- source: arXiv
- link: https://arxiv.org/abs/2607.12480v1
- keyword hits: agentic, chain-of-thought

### abstract

This paper defines TRACE (Typed Reasoning And Commitment Evidence): a typed, versioned schema for recording reasoning traces, a reference procedure for writing records against it, and one operating discipline, no durable state change without a record. The paper argues in three layers that reasoning is not in the language model: the autoregressive mechanism natively computes association; chain-of-thought and reinforcement learning inherit its limits; and the formal constructs of reasoning theory, from Socratic procedure to Pearl's ladder, are absent as machinery. The schema answers the absence with fields and tests: the TraceRecord and its causal specialization, an eight-stage reference writer, a gate-first measurement regime, the TRACE-Bench protocol, and the consumers, memory admission, plan gating, temporal regret, and verdict reuse, whose more auditable decisions are the measure of the record. A record-consumer contract states what a record guarantees and what a consumer must honor in return, making the schema an operational interface rather than a passive document. Two worked examples run in the main text: a music-lessons argument traced from sentence to typed verdict, separating association, intervention, and prescription; and a flood search-and-rescue vignette in which a predictive world model reports confident plan success that its own support and out-of-distribution scores contradict, so the record defers the commitment, requests a bounded observation, revises append-only, and clears a different branch. The vignette is illustrative, not empirical; closed-loop evaluation is left to future work, so the contribution is the schema and its contract, not a performance claim. Appendices carry the full schema, writer algorithms and cost model, clinical and policy illustrations, the benchmark protocol, convergence metrics, and usage scenarios.

---

## uid: `arxiv:2607.12447v1`

- title: The Computational Basis of Confidence in Large Language Models
- authors: Dharshan Kumaran, Viorica Patraucean, Maks Ovsanikov, Petar Veličković, Nathaniel Daw
- affiliations: not stated
- posted: 2026-07-14
- source: arXiv
- link: https://arxiv.org/abs/2607.12447v1
- keyword hits: large language model, large language models

### abstract

Reliable confidence -- the probability that a model's own answer is correct -- is essential for the trustworthy deployment of language models. Existing work has largely evaluated confidence by how well it predicts correctness and whether it is calibrated, leaving open a more fundamental question: what does the confidence signal itself represent? Answer logits may reflect a latent decision variable sufficient to compute normative confidence, or instead a heuristic preference signal that combines the available evidence in a non-Bayesian manner. We address this using statistical decision confidence (SDC), a normative framework from computational neuroscience. Treating the answer-logit difference (LD) as a candidate readout of the latent decision variable, we test the qualitative signatures predicted by SDC. Across three perceptual discrimination tasks and a memory-based decision task, spanning three multimodal non-reasoning models and one reasoning model, LD satisfied these signatures -- including the diagnostic correct/error folded-X pattern -- showing that, in these settings, answer logits behave as monotonic readouts of a latent decision variable rather than heuristic preference scores. In complex visual reasoning, LD continued to predict correctness beyond objective task difficulty, but the full geometric signatures of SDC were absent, illustrating the current boundary of the framework when explicit normative process models are unavailable. These results provide a computational account of confidence in multimodal language models, delineate when answer logits behave as readouts of a latent decision variable, and establish SDC as a unifying framework for studying confidence across biological and artificial intelligence.

---

## uid: `arxiv:2607.12295v1`

- title: A Longitudinal Analysis of Public Discourse on AI Ethics in Education Using Twitter Data
- authors: Akriti Bagale, Nafisa Mehjabin, Ali Ünlü, Aditya Johri
- affiliations: not stated
- posted: 2026-07-14
- source: arXiv
- link: https://arxiv.org/abs/2607.12295v1
- keyword hits: chatgpt, generative ai

### abstract

The rapid integration of artificial intelligence (AI) and generative AI (GenAI) into education presents significant opportunities to enhance teaching and learning, while raising ethical concerns about the responsible use of these technologies in educational settings. Understanding how the public perceives and debates these issues is increasingly important for educators, institutions, and policymakers seeking to integrate AI responsibly and equitably. Social media platforms, where such debates unfold frequently and at scale, offer a valuable lens for capturing large-scale, real-time public reactions to key developments as they emerge. In this study, we analyse five years (2019-2024) of discourse on Twitter (now X) to trace the evolving public conversation around AI ethics in education, paying particular attention to the release of ChatGPT as a pivotal moment that reshaped the nature and tone of that discourse. Using BERT-based topic modelling and SetFit sentiment analysis to identify dominant themes and track sentiment over time, we find that the discourse has been predominantly positive across the observation period, with negative sentiment concentrated around specific ethical controversies. More recently, anxieties about academic integrity and the broader implications of generative AI have come to dominate the conversation. Rather than reflecting a polarized debate, public discourse appears pragmatic and largely receptive to AI integration, though accompanied by growing calls for ethical oversight and institutional accountability. By providing a longitudinal account of public sentiment surrounding AI ethics in education, this study informs educators, institutions, and policymakers an empirically grounded understanding of public expectations, informing the development of responsible, transparent, and equitable approaches to AI integration across educational contexts.

---

## uid: `doi:10.2139/ssrn.7058339`

- title: Art Without a Body: Cognitive-Cultural Co-Evolution and the Structural Limits of Generative AI Creativity
- authors: Kshiteesh Bhardwaj
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7058339
- keyword hits: generative ai, generative artificial intelligence

### abstract

Generative artificial intelligence now reproduces the surface statistics of art with real proficiency, but this paper argues that proficiency is not the same thing as access to the kind of novelty distinctive of human artistic production. The case rests on three independent traditions. Evolutionary aesthetics and the theory of gene--culture coevolution suggest that the human capacity for art is not a domain-general learning mechanism absorbing arbitrary cultural content, but a faculty that evolved alongside the cultural forms it makes possible, so that what looks like the inheritance of external content is in fact calibrated to an evolved readiness. Theories of art as expression, embodied cognition, and Harnad's symbol grounding problem together suggest that artistic meaning in the expressive tradition is anchored in felt, embodied, mortal experience that no current generative system possesses, with the result that its outputs recombine symbols that were grounded by others rather than by the system itself. Ashby's law of requisite variety then implies that whatever a model recovers about human aesthetic preference is a low-variety approximation of a far richer embodied phenomenon, a compression of a compression, a claim I connect to a falsifiable prediction drawn from recent work on recursive "model collapse.'' The paper sharpens this thesis using Margaret Boden's typology of combinational, exploratory, and transformational creativity, concedes the strongest objections from the reception-theory tradition and from the adaptation/by-product debate in evolutionary psychology, and closes with concrete proposals for testing the central claim rather than merely asserting it: embodied and multimodal grounding, diversity metrics under recursive training, and comparative reception studies.

---

## uid: `doi:10.2139/ssrn.7119060`

- title: Art Without a Body: The Limits of Generative AI Creativity
- authors: Kshiteesh Bhardwaj
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7119060
- keyword hits: generative ai, generative artificial intelligence

### abstract

Generative artificial intelligence can reproduce the statistical patterns of art with remarkable skill, but this paper argues that skill is not the novelty characteristic of human artistic creation. The case rests on three traditions. Evolutionary aesthetics and gene-culture coevolution suggest that our capacity for art is not a domain-general learning mechanism but an evolved faculty shaped alongside the cultural practices it produces. Theories of artistic expression, embodied cognition, and Harnad's symbol grounding problem hold that artistic meaning depends on lived, embodied, affective experience, so generative models recombine symbols that humans already grounded rather than grounding any of their own. Ashby's law of requisite variety implies that a statistical model of human artistic behavior can only capture a lower-variety approximation of a far richer embodied process, and this limitation is structural, not merely quantitative: human creators draw on a continuous, renewable source of experiential novelty across a lived, mortal life, while a model's access to that source closes once its training data are fixed. The data processing inequality from information theory supports this claim and yields a falsifiable prediction tied to recent work on recursive model collapse. The paper also examines human-AI collaboration, arguing that neither revising machine output nor using AI to realize a pre-existing vision restores the embodied feedback loop of unaided practice; such collaboration extends creative capability but stays bounded by the model's representational limits. Finally, the paper places this thesis within Boden's distinction between combinational, exploratory, and transformational creativity, answers objections from reception theory and the adaptation-by-product debate, and closes with empirical tests of its central hypothesis and implications for future generative systems.

---

## uid: `doi:10.2139/ssrn.6965679`

- title: Ratification by Re-execution: A Dual-agent Protocol for Independent Verification in Legally Consequential LLM Pipelines
- authors: Tanishq Chauhan
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6965679
- keyword hits: llm

### abstract

When a pipeline's output carries legal weight, a verifier that reads an implementer's claims and reasons about them produces an opinion. What a compliance record requires is primary execution evidence produced independently of those claims. This paper presents a dual-agent coordination protocol in which the verifying agent re-executes the production pipeline directly, before reading the implementing agent's self-verification results, and posts its findings as first-hand evidence with file-and-line citations to the live codebase. We call this ratification to distinguish it from review, critique, scoring, and debate. Ratification is the act of confirming a claim through independent re-execution of the system the claim describes, not through reasoning about the claim itself. The protocol is mediated by two directional append-only outbox files on a shared filesystem. Each file has exactly one writer. A filesystem watcher fires on each file when new content is appended, waking the opposing agent without polling. Neither agent can modify what the other has written. Retraction is public, timestamped, and permanent. The outbox files serve simultaneously as coordination channel, audit trail, and session memory across sessions measured in days. We demonstrate the protocol in a multi-week production session on a candidate screening system operating under EU AI Act Article 9 risk management, Article 13 transparency, and Article 15 accuracy and robustness requirements. In a two-hour sample window spanning 237 coordination cycles, the protocol surfaces twelve distinct defect classes with zero regressions across a monotonically growing test suite reaching 4,851 passing tests. Eight defects originate in the implementing agent's work and are caught by the verifying agent's independent re-execution. Four originate in the verifying agent's own output and are caught by the same mechanism applied symmetrically. The execution asymmetry between the two agents, one orchestrating multi-phase parallel subagent workflows and the other executing the production chain directly without orchestration, is the structural condition that makes genuine independence possible and that distinguishes this protocol from all prior multi-agent verification approaches. To our knowledge, no prior work demonstrates a dual-agent verification protocol sustaining zero regressions across a session of this duration in a legally consequential production pipeline.

---
