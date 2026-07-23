# Classification batch 407 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-407.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6943498`

- title: Digital Leapfrogging: Leveraging Techno-Intercultural Synergy Theory (TIST) to Democratize Global Higher Education Ecosystems
- authors: Mary Ragui
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6943498
- keyword hits: agentic, generative artificial intelligence

### abstract

Traditional frameworks for Collaborative Online International Learning (COIL) treat digital tools as passive background infrastructure, inadvertently penalizing Global South institutions due to baseline readiness and preparedness gaps. This policy brief challenges the status quo by operationalizing Techno-Intercultural Synergy Theory (TIST)-a paradigm shifting Generative Artificial Intelligence (AI) from a utility to an agentic collaborative partner. Based on rigorous structural equation modeling (R² = .480, Cohen's d = 1.14), this brief demonstrates that AI integration serves a vital dual purpose: minimizing human intercultural friction while independently engineering standalone professional self-efficacy. Actionable macro-level policies are proposed to leverage AI as an equity multiplier, closing the systemic North-South developmental divide without high-carbon physical mobility budgets.

---

## uid: `doi:10.2139/ssrn.6983540`

- title: Legitimacy Debt, Neuro-Sovereignty, and Friction Rights: Reconstructing the Social Contract for AI-Mediated Governance
- authors: David Galipeau
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6983540
- keyword hits: agentic

### abstract

Public institutions are adopting AI decision systems at the same time that public trust in those institutions is eroding, and the standard remedy-greater transparency-no longer suffices. This paper develops a theory of legitimacy for AI-mediated governance and proposes institutional mechanisms to defend it. It formalizes legitimacy debt as the accumulated, unrepaired violation of procedural justice-fair process, voice, and equal respect-in AI-mediated systems, and distinguishes three layers: economic, symbolic, and neurological. It then introduces Neuro-Sovereignty, a governance-level right to mental self-authorship in the face of predictive, affective, and attention-shaping systems, and argues that it is distinct from privacy, data protection, freedom of thought, and the individual neurorights now entering constitutional law. To operationalize procedural justice inside automated environments, the paper develops Friction Rights-a guarantee of slow, contestable moments in high-stakes automated flows-and Verification Pauses, specifying who may invoke them, what must be logged, what explanation is owed, and how override works. It connects these to emerging oversight frameworks for agentic AI through a four-pillar governance pattern and positions Friction Rights as a minimum legitimacy condition. The paper closes with a normative and empirical research agenda, including candidate measures for legitimacy debt and Neuro-Sovereignty and testable hypotheses linking genuine friction to perceived legitimacy.

---

## uid: `doi:10.2139/ssrn.7068292`

- title: Regulation-Grounded Graph Retrieval and Reasoning for Elevator Fault Diagnosis
- authors: Ziyu Zhao, Feiyu Liao, Haodong DENG, Yuqing Gao, Qiang ZHENG, Yongpeng LUO
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7068292
- keyword hits: retrieval-augmented

### abstract

Building elevator diagnosis requires high reliability, interpretability, and alignment with regulatory standards, which remains challenging for retrieval-augmented generation (RAG) methods that mainly rely on unstructured text retrieval. To address this limitation, this study develops an Adaptive GraphRAG Framework for evidence-driven elevator diagnosis, grounded in a domain knowledge graph constructed from relational inspection records and short-text inspection narratives. The methodological novelty lies in casting regulation-aware diagnosis as executable graph retrieval: regulatory clauses, inspection items, component states, and fault evidence are modeled in a unified graph schema, and natural-language questions are translated into Cypher queries through a training-free prompt-template-guided pipeline. To support this process, we curate a dataset of 500 Question--Cypher pairs spanning 13 intent categories for prompt construction and benchmark evaluation, rather than supervised parameter training. Experimental results show that the Question2Cypher pipeline combined with graph retrieval achieves higher execution reliability and interpretability than direct Question2Answer generation under the same model setting. These findings indicate that graph-structured, execution-verifiable retrieval can improve auditable diagnostic decision support in safety-critical civil infrastructure scenarios. Overall, the proposed framework provides a transparent and scalable foundation for trustworthy AI-assisted elevator inspection and diagnosis.

---

## uid: `arxiv:2607.04958v1`

- title: Look-Ahead-Freedom as Temporal Non-Interference: A Verifiable Correctness Property for Backtesting and Agentic Trading Pipelines
- authors: Xavier Fonseca
- affiliations: not stated
- posted: 2026-07-06
- source: arXiv
- link: https://arxiv.org/abs/2607.04958v1
- keyword hits: agentic

### abstract

Look-ahead bias (using information from after a decision epoch to make the decision at that epoch) is the dominant way a backtest or a machine-learning evaluation flatters a system that will disappoint in deployment. The field manages it with construct-specific recipes and empirical detectors, which are sound only channel by channel and certify nothing by their silence. We show that look-ahead-freedom is a formal property in disguise: fixing an epoch, the demand that the future not influence the present is temporal non-interference over a time-indexed information lattice. From this identification we develop a pipeline calculus separating a datum's availability from its reference time, and settle the problem's boundary. Where availability may depend on data values, look-ahead-freedom is undecidable (indeed Pi-0-1-hard): leakage is recursively enumerable but freedom is not. On the value-independent fragment (covering windowing, resampling, joins, point-in-time and vintage reads, and agentic retrieval) we give a type-and-effect system that is sound and decidable in linear time. An artifact confirms the theory: the check scales linearly, an independent oracle witnesses no leak in any accepted pipeline, and the checker catches every planted leak that differential and tiling detectors miss.

---

## uid: `arxiv:2607.05666v1`

- title: What Do AI Agents Actually Change? An Empirical Taxonomy of Mutation Patterns in Performance-Improving Pull Requests
- authors: Illia Dovhoshliubnyi, Nima Soroush, Ashkan Sami, Alexander Brownlee
- affiliations: not stated
- posted: 2026-07-06
- source: arXiv
- link: https://arxiv.org/abs/2607.05666v1
- keyword hits: ai agent

### abstract

AI coding agents are black boxes: we cannot inspect how they generate code, but we can inspect what they change. This distinction matters for search-based software engineering (SBSE), where techniques such as genetic improvement (in the performance-optimisation application we study) depend on mutation operators that reflect how code is actually transformed. Fewer than 1% of the 33,596 agent PRs in AIDev-pop target performance, making each case a rare window into otherwise opaque agent behaviour. We classify 1,254 performance-relevant diff hunks from 216 of these PRs, spanning five agent systems, against the 18-category syntactic mutation taxonomy of Even-Mendoza et al. (2025) using a dual-LLM intersection pipeline. Three categories dominate: name modification (37.0%), object creation (26.4%), and type change (22.7%), a profile markedly different from prior GI corpora where no change accounted for 84%. Each agent's deployed system commits to a distinctive mutation vocabulary, and each performance strategy activates a largely disjoint category subset. Agent identity and target strategy are therefore informative priors that narrow the effective SBSE operator space. Replication package: https://github.com/5uper6rain/ssbse-challenge-2026

---

## uid: `arxiv:2607.05518v1`

- title: aiAuthZ: Off-Host, Identity-Bound Authorization for AI Agents
- authors: Sai Varun Kodathala
- affiliations: not stated
- posted: 2026-07-06
- source: arXiv
- link: https://arxiv.org/abs/2607.05518v1
- keyword hits: ai agent

### abstract

AI agents issue tool calls on the basis of text they cannot verify, so any party who controls part of the context can forge the appearance of authority. I evaluate 15 contemporary language models against eight attack scenarios derived from a published corpus of real agent incidents and find that refusal varies from 100% down to 38% across fully evaluated models; the most expensive model refused only half of the attacks despite a twentyfold price spread. I present aiAuthZ, an authorization gateway that moves the safety decision off the agent's host. Before a tool call executes, the gateway verifies caller identity with a per-message HMAC-SHA256 signature bound to a single-use nonce and a timestamp window, and it evaluates a role-based and argument-level policy that the agent can neither read nor modify. Every decision joins a SHA-256 hash-chained audit log, and each accepted message yields an HMAC-authenticated QR receipt that achieves 94% mean verification across eight transmission channels, with zero forgeries accepted in 25 wrong-key trials. With the gateway in place, residual attack success falls to 0% for all 15 models at no more than 0.03 ms of added decision latency. On the AgentDojo banking suite, aiAuthZ blocks all seven attacker-directed tool calls the evaluated agents emit, at the cost of one legitimate first-time payment, while a spotlighting baseline allows two injections to succeed. Across nine in-scope case studies from the same incident corpus, aiAuthZ blocks nine of nine, against four of nine for a policy baseline without identity binding. The gateway does not prevent a model from being deceived; it prevents a deceived model from acting beyond the verified user's authority on every call routed through it. The implementation and all experiments are released at https://github.com/Sports-Vision-Inc/aiAuthZ.

---

## uid: `arxiv:2607.04729v1`

- title: RustMizan: A Compilable, Contamination-Aware Benchmarking Framework for Rust Vulnerabilities
- authors: Tarek Elsayed, Shiping Yang, Eunsong Koh, Sanika Goyal, Vincent Huang, Paul Ngo, Nathan Young, Mohammad Omidvar Tehrani
- affiliations: not stated
- posted: 2026-07-06
- source: arXiv
- link: https://arxiv.org/abs/2607.04729v1
- keyword hits: agentic, llm

### abstract

LLM agents are increasingly applied to vulnerability analysis, but existing benchmarks have not kept pace. They typically rely on small non-compilable snippets, focus on binary classification (vulnerable or not), and do not account for the risk that publicly-released datasets are part of model training corpora. We introduce RustMizan, a benchmarking framework for Rust vulnerability analysis that addresses these gaps. RustMizan contains compilable code variants at the crate, file, and function levels, with annotations for binary vulnerability detection, CWE classification, and function- and line-level localization. A paired mutation framework produces semantics-preserving code mutants for contamination testing and robustness probing. Across four frontier models in an agentic setup with command-line access, binary classification sits in the 56-65% range, but line localization F1 stays near 20%, and adversarial cues drop line F1 by about 27%.

---

## uid: `doi:10.2139/ssrn.7063360`

- title: Tax Incentives and Venture Capital Risk-Taking: Evidence from the QSBS Program
- authors: Murillo Campello, Guilherme Junqueira
- affiliations: not stated
- posted: 2026-07-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7063360
- keyword hits: prompting

### abstract

Do tax subsidies prompt investors to take on risk? We address this question by looking at investors' responses to changes to the Qualified Small Business Stock (QSBS) program, which reduces capital gains taxes on startup investing. We do so under a framework in which some startup investors — venture capitalists (VCs) — combine outside funding with incentive-based compensation, while others invest their own funds. Using bunching, triple-differences, and matching designs that exploit industry eligibility, investment vintage, and holding-period requirements, we analyze data from 158 thousand investor–firm pairings over two decades. We identify strategic investment timing, with subsidies prompting bunching at tax-eligible holding-period thresholds. Most notably, when and where tax subsidies apply, VCs shift their project selection toward riskier ventures: they invest more in pre-commercial stage startups, become more likely to provide startups with their initial capital, and invest more in startups with pre-existing debt, while becoming less likely to co-syndicate their investments. Tax-subsidized VC-backed ventures show higher failure rates, but on the flip side, attain higher valuations at exit and are more likely to reach "unicorn status." None of these patterns are observed for comparable non-VC investors in startups exposed to the same tax subsidies. Our tests further show that tax incentives lead to reallocation toward more innovative industries, yielding more impactful patents. Our study is the first to show that tax policy can shift entrepreneurial financing toward riskier, more innovative, and valuable startups. Institutional subscribers to the NBER working paper series, and residents of developing countries may download this paper without additional charge at www.nber.org .

---
