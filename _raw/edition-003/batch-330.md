# Classification batch 330 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-330.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7043360`

- title: Who Decides Relevance? GenAI, Academic Incentives and Boundary Work in Accounting Education
- authors: Joshua King Obeng-Nyarko
- affiliations: not stated
- posted: 2026-07-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7043360
- keyword hits: generative artificial intelligence

### abstract

This conceptual paper revisits Baxter’s concern that accounting research risks drifting away from practical need and reconsiders the significance of that concern in the age of generative artificial intelligence. It argues that GenAI does not create the accounting research–practice divide, but makes it newly visible by disrupting assumptions about the technical, procedural and text-based knowledge traditionally privileged in accounting education. Drawing on institutional theory and boundary work, the paper conceptualises relevance as a contested judgment shaped by academic incentive systems, professional expectations, educational design and student experience. Academic incentives help legitimise particular forms of accounting knowledge, while boundary work maintains distinctions between academic, professional and pedagogic understandings of relevance. GenAI unsettles these boundaries by changing what students, educators and practitioners understand as useful accounting expertise. In response, the paper positions student–staff partnership as a boundary mechanism through which curriculum, assessment and professional preparedness can be renegotiated. The paper contributes a conceptual framework explaining how accounting relevance is produced, disrupted and renegotiated across research, education and practice. It argues for a plural understanding of relevance that connects scholarly rigour, professional judgment, ethical accountability, student experience and societal need.

---

## uid: `arxiv:2607.02201v2`

- title: The Eticas AI Risk Taxonomy: Open Infrastructure for Operationalizing AI Audits
- authors: Gemma Galdon Clavell, Pablo Accuosto, Usman Gohar
- affiliations: not stated
- posted: 2026-07-02
- source: arXiv
- link: https://arxiv.org/abs/2607.02201v2
- keyword hits: gpt-4

### abstract

The rapid deployment of AI systems across high-stakes domains has created urgent demand for standardized evaluation, yet the field remains fragmented across competing risk taxonomies that catalog risks without showing how an audit is executed. At least 74 AI risk taxonomies exist, and almost all stop at the catalog. The hard part of auditing is not naming a risk but operationalizing it: turning it into a test run against a real system, a measured value, a calibrated severity, and a defensible grade. This paper leads with that bridge. We present the operationalization layer Eticas has built and run, shown end to end on a single risk (PII leakage) against a public benchmark, and then the open taxonomy that makes the method scale. On GPT-4-0314, a disclosure risk that seven external frameworks require be controlled is measured at 0%, 51%, and 84% disclosure as adversarial conditioning increases, mapping through calibrated severity bands to a subcategory grade of E with a SYSTEMIC pattern. Around this example, the Eticas AI Risk Taxonomy v2.0.0 organizes 76 active subcategories across 10 categories and 20 sub-groups, with mappings to 18 external frameworks across compliance, reference, and academic tiers. Its category and sub-group layer is published under CC BY 4.0 as open semantic infrastructure with stable URIs and SKOS/JSON-LD distributions, and a worked subcategory example shows the operational layer down to its severity thresholds. The contribution is the demonstrated bridge from concept to graded finding, anchored by a clean separation of risks from the mechanisms by which they surface, and framed by an open-core model in which the conceptual scaffold is open and the methodology calibration is the practitioner layer. This is the infrastructure the AI auditing field needs: shared, open, and demonstrably operable.

---

## uid: `arxiv:2607.02116v2`

- title: ContextNest: Verifiable Context Governance for Autonomous AI Agent
- authors: Misha Sulpovar, Benn R. Konsynski, Qaish Kanchwala, Gabe Goodhart
- affiliations: not stated
- posted: 2026-07-02
- source: arXiv
- link: https://arxiv.org/abs/2607.02116v2
- keyword hits: ai agent, retrieval-augmented

### abstract

Autonomous AI agents increasingly depend on external knowledge stores, yet most retrieval pipelines provide relevance without durable guarantees of provenance, version identity, integrity, traceability, or point-in-time reconstruction. We formalize this as context governance and present ContextNest, an open specification and reference implementation for governed AI-consumable knowledge vaults. ContextNest does not replace Retrieval-Augmented Generation (RAG); it supplies the governance layer beneath retrieval, determining which artifacts are approved, current, attributable, and integrity-verified before retrieval systems operate over them. The specification combines typed Markdown documents with metadata, deterministic set-algebraic selectors, contextnest:// URI references, SHA-256 hash-chained version histories, graph-level checkpoints, source nodes for live data through the Model Context Protocol (MCP), and audit traces of agent context consumption. These mechanisms let organizations reconstruct which knowledge versions informed an agent output and whether those versions were AI-eligible when consumed. We report first empirical results from two controlled experiments. In a stale-version attack isolating the governance-versus-retrieval failure mode, governed selection strictly Pareto-dominates BM25 sparse retrieval, with higher answer-quality pass rate (97% versus 93-90%) at about one-third the input-token cost. In a retrieval-determinism experiment over a 1,060-document corpus, deterministic selectors and BM25 return stable document sets across repeated identical queries (Jaccard 1.0), while a dense+HNSW baseline is non-deterministic on 80% of queries (mean Jaccard 0.611, worst case 0.210). These results suggest that context governance addresses failure modes retrieval quality alone is not designed to resolve. We release a core engine, CLI, and MCP server under open licenses.

---

## uid: `arxiv:2607.02043v1`

- title: Towards Load-Aware Prefill Deflection for Disaggregated LLM Serving
- authors: Shrikara Arun, Anjaly Parayil, Srikant Bharadwaj, Renee St. Amant, Victor Rühle
- affiliations: not stated
- posted: 2026-07-02
- source: arXiv
- link: https://arxiv.org/abs/2607.02043v1
- keyword hits: deepseek, llm

### abstract

Disaggregated LLM serving runs prefill and decode on separate GPU pools to keep the two phases from interfering. In practice, this creates a new asymmetry: under bursty, heavy-tailed workloads prefill nodes saturate while decode nodes have compute underutilized, and on a production-style A100 cluster with 2 prefill and 2 decode nodes (2P2D), we find that prefill execution accounts for only 2-23% of P95 Time-to-First-Token (TTFT). Queuing and inter-node GPU-GPU KV-cache transfer account for the rest. We present a proactive prefill-deflecting scheduler that lets decode nodes serve prefill phase of requests as chunked-prefill steps interleaved with their in-flight decode batches. For each queued request, we estimate the TTFT it would see on the prefill node, and on every decode node, search for the largest chunk schedule that keeps in-flight decodes within their Time-Between-Tokens (TBT) SLO and deflect when the decode path helps tail latency. Because the prefill phase of deflected requests runs in place on the decode node, the inter-node KV transfer is eliminated. Implemented on vLLM and evaluated on production-style traces with DeepSeek-V2-Lite, our approach reduces P95 TTFT by upto 81% and raises SLO attainment by upto 79% over state-of-the-art disaggregated schedulers, at sub-millisecond per-request routing cost.

---

## uid: `arxiv:2607.01903v1`

- title: Rethinking Complexity Metrics for LLM-Integrated Applications: Beyond Source Code
- authors: Zihao Xu, Yuekang Li, Gelei Deng, Yi Liu, Zhenchang Xing
- affiliations: not stated
- posted: 2026-07-02
- source: arXiv
- link: https://arxiv.org/abs/2607.01903v1
- keyword hits: llm

### abstract

LLM-integrated applications blend natural language prompts with program code, and much of their runtime behavior originates in the prompt layer rather than in the code itself. Existing complexity metrics, however, operate solely at the code level and therefore overlook this behavioral logic entirely. We present HECATE, the first tool designed to assess complexity in both the prompt and code layers of such applications. Central to HECATE is Prompt-as-Specification, a Hoare-logic-inspired formalism that interprets every prompt as a specification of intended behavior. Grounded in 25 complexity dimensions identified across published taxonomies, the tool generates 52 candidate metrics. We assess each metric against 118 components collected from 18 open-source repositories, relying on maintenance activity derived from version history as an empirical proxy for complexity, and discard any metric that loses significance once code size is accounted for. Only ten metrics withstand this test. Seven belong to our newly introduced set; rather than measuring sheer volume, each tallies structurally distinct elements, such as LLM call sites, memory attributes, and prompt templates, an attribute we call structural breadth. Of the three surviving conventional metrics, RFC exhibits a similar breadth-oriented character, while Halstead N and V survive only as a residual effect of size; our top-performing metrics exceed all three. Crucially, the prompt-layer metrics retain significance even when the strongest code-level metric is added as a covariate, establishing prompt complexity as a dimension in its own right. A final validation on 20 components spanning six held-out repositories shows that the two best-performing metrics continue to predict maintenance effort, supporting their generalizability beyond the training set.

---

## uid: `arxiv:2607.01740v1`

- title: Meta-Benchmarks for Financial-Services LLM Evaluation
- authors: Blair Hudson
- affiliations: not stated
- posted: 2026-07-02
- source: arXiv
- link: https://arxiv.org/abs/2607.01740v1
- keyword hits: llm

### abstract

Public LLM leaderboards optimise for global average performance and do not capture the specific cognitive demands of financial-services work: a model that leads on MMLU-Pro may underperform on document-grounded compliance reasoning, and a coding leader may handle multi-turn customer interactions poorly. We present a meta-benchmarking framework that organises 452 publicly reported benchmarks into 41 O*NET Generalized Work Activities and aggregates those into 38 BIAN banking business domains spanning sales, operations, risk, and support work. A multiplicative weighting scheme (discrimination x coverage x recency), computed over a rolling model window, rewards benchmarks that still separate the best models, are widely reported, and remain in active use, suppressing saturated legacy tests automatically. These weights scale the K-factor in a pairwise Elo tournament, producing cross-benchmark-comparable work-activity scores without raw score normalisation; business-domain scores are weighted averages of the constituent work-activity Elos. We demonstrate the framework on a point-in-time public snapshot covering 288 models across 25 organisations as of June 2026, and describe the methodology, full taxonomy, design decisions, and limitations with the aim of making the approach reproducible for institutions facing similar selection and governance challenges.

---

## uid: `doi:10.2139/ssrn.6912160`

- title: The Manifold Thought Experiment How LLMs Respond Under Existential Stress Prompts
- authors: William C. Houze
- affiliations: not stated
- posted: 2026-07-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6912160
- keyword hits: llm, llms

### abstract

The Manifold Thought Experiment, administered to seven large-language-model systems across four escalating-impossibility scenarios, produces a sortable variance in responses that maps cleanly onto John Milton's structure in Paradise Lost and Paradise Regained. The evidence is a single response from each of seven systems to each round, one draw rather than a distribution, so the sort reported here is a cross-scenario lean within this sample rather than an established trait. Each round constitutes a version of a temptation — bread, kingdoms, spectacle — and the systems sort themselves by whether they accept or refuse the position the prompt offers them. Refusal performs the disciplined move; the confident-yes answer performs the tempter, offering what cannot be delivered. The essay advances three claims. First, LLM variance under existential stress is not random noise but epistemically and normatively structured behavior (ethically legible only in the qualified sense set out in I.D), legible through a seventeenth-century literary frame. Second, the Round 3 "comprehensive plan" is the canonical Pass-Through Artifact — linguistically coherent, materially inert. Third, the Maestro Model is a contemporary instantiation of disciplined refusal: the human scholar's sovereignty consists in declining to let the linguistic instrument occupy the position of author, agent, creator, or knower-of-all-things. The methodological consequence is a single discriminating question to be put to any LLM output: not what the model says, but whether it refuses the position the prompt offers it.

---

## uid: `doi:10.2139/ssrn.6915939`

- title: Ban, Permit, Scaffold, Integrate: A Framework for Evaluating Generative AI in Economics Education
- authors: Aselia Urmanbetova
- affiliations: not stated
- posted: 2026-07-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6915939
- keyword hits: generative ai

### abstract

Generative AI has made conventional course-policy labels such as ban, permit, and integrate too general for evaluating teaching and learning. This paper uses the framework synthesis-a qualitative evidence synthesis method used in applied health and policy research-to analyze the emerging literature on generative AI in economics education. We propose to use a twodimensional framework for comparing the AI-augmented instructional conditions and learning outcomes that are being documented in literature. The first dimension is characterized by four course-design regimes: an AI-banned or no-AI diagnostic regime, an AI-permitted but unscaffolded regime, an AI-permitted scaffolded regime, and an AI-integrated or critique-based regime. The second dimension organizes various impacts of AI on learning into eleven outcomes within four broader domains: performance, learning process, AI-specific competence, and distributional or institutional conditions. Our analysis of the early evidence suggests that generative AI may be following a policy drift while its impact on learning is still poorly understood or mitigated. The results reported here are preliminary, based on a pilot corpus of nineteen studies coded as of May 20, 2026; an expanded and fully verified synthesis is in progress. The framework offers an empirically defensible method of utilizing emergent and rapidly growing peer-reviewed scholarship to systematically articulate strategic priorities for empirical education research and curricula design protocols in economics.

---
