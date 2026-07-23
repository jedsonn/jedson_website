# Classification batch 290 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-290.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6806924`

- title: Designing for Interpretive Gatekeeping: Family-Centered AI Literacy in Korean Immigrant Households
- authors: Jeongone Seo, Ryan Womack, Tawfiq Ammari
- affiliations: not stated
- posted: 2026-05-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6806924
- keyword hits: generative ai

### abstract

As generative AI enters family life, immigrant households face distinct challenges navigating tools across generations and languages. Through 20 interviews with Korean immigrant families in the U.S., we identify two design-relevant practices: interpretive gatekeeping, where parents mediate AI use through cultural values and language-aware verification; and convenient critical deferment, where teens strategically stage critique across task lifecycles. We contribute to design research by: (1) operationalizing language as epistemic infrastructure—a verification mechanism families use to assess AI quality and cultural fit; (2) reframing teen usage as temporally-distributed criticality rather than literacy deficit; and (3) translating family practices into six design patterns: bilingual inconsistency detection, parental value overlays, tone-aware modes, context-sensitive refusal, negotiation-first governance, and relational data views. These patterns reframe “workarounds” as first-class design requirements for equitable, culturally-attuned AI systems supporting intergenerational collaboration. Our work extends ongoing scholarship on child-centered AI, bilingual conversational agents, and culturally-situated technology use by centering the immigrant family (rather than individual users) as the unit of analysis for AI literacy.

---

## uid: `doi:10.2139/ssrn.6774579`

- title: Trustworthy Transaction Arena (TTA): A Governance Architecture for Multi-Actor Agentic AI Systems with Probabilistic Workflow Verification
- authors: Hiroyuki Kitajima
- affiliations: not stated
- posted: 2026-05-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6774579
- keyword hits: agentic, ai agent

### abstract

Existing multi-agent frameworks evaluate correctness only at the team outcome level: if the agent team achieves its goal, the transaction is deemed successful. This is insufficient for business and social activities, which consist of multiple interrelated tasks — involving asynchronous, time-constrained, and probabilistic behaviors — pursued toward broader goals. Without a framework that conveys objectives and authority to every actor throughout the activity, the means by which goals are achieved cannot be verified. This paper proposes the Trustworthy Transaction Arena (TTA), treating these activities as governed workflows in which every actor operates under delegated authority from a human principal, subject to continuous enforcement at every step. Its principal features — absent from all existing approaches — are: (i) a Unified Governance Layer combining static role-based and dynamic workflow-state access control in a single enforcement layer through which every actor action must pass; (ii) Non-Escalation of Delegated Authority (NEDA) — no agent can exceed the authority scope of its delegating principal — enforced transitively throughout the entire delegation chain; and (iii) a HERT probabilistic workflow engine handling asynchronous and stochastic behaviors, enabling critical path identification, bottleneck extraction, and detection of stochastic behaviors such as hallucination and capability leakage, with structural human supervision checkpoints. The architecture extends two production-validated prior works — the CBA access control model extended to cascaded AI agent delegation [Kitajima2002], and the HERT probabilistic formalism extended to stochastic workflow verification in AI environments [Kitajima1981-HERT] — and is demonstrated through an out-of-hospital cardiac arrest emergency response application.

---

## uid: `doi:10.2139/ssrn.6768758`

- title: Conditional Skill Compression: Domain Expertise and the Unequal Returns to Generative AI
- authors: Mustafa Seref Akin
- affiliations: not stated
- posted: 2026-05-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6768758
- keyword hits: generative ai, generative artificial intelligence

### abstract

Generative artificial intelligence creates a distributional paradox: AI compresses withinoccupation productivity gaps, yet aggregate inequality is not falling. This paper resolves the paradox through a formal model built around two thresholds. The Minimum Expertise Threshold (θ*) is the minimum domain knowledge required to evaluate and correct AI outputs safely; it is derived endogenously from expected AI-use payoffs. The model yields three predictions. First, the within-occupation gap between qualified and high-skill workers narrows, as medium-skill workers above the threshold fill their execution gap through AI while high-skill workers approach the productivity ceiling. Second, the gap between qualified and below-threshold workers widens, as below-threshold workers gain little by AI they cannot evaluate. Third, AI adoption also reduces demand for entry-level workers who would otherwise accumulate the domain knowledge (θ*) needed to cross the threshold, generating a training-pipeline externality: total discounted welfare can fall even when the static productivity gain is positive.

---

## uid: `doi:10.2139/ssrn.6733338`

- title: Investor DNA Scoring: A Position-Data Framework for Detecting Behavioral Risk in Retail Portfolios -Early Evidence from an AI-Native Wealth Platform
- authors: Varun Srivastava
- affiliations: not stated
- posted: 2026-05-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6733338
- keyword hits: llm

### abstract

This paper introduces the Investor DNA Score, an exploratory behavioral-risk metric that uses retail portfolio position data to identify concentration, factor-tilt, and behavioral-bias patterns without requiring broker credentials, transaction history, or investor surveys. Using 82 anonymised portfolio submissions of the NeuFin Intelligence platform between March and May 2026, the study documents an unexpected holding pattern among AIengaged Southeast Asian investors: overwhelming exposure to US-listed mega-cap equities and fixed-income ETFs, at a level that differs markedly from what conventional home bias theory would predict for a regional retail population. Apple (AAPL), Microsoft (MSFT), and JPMorgan (JPM) each appear in over 30% of portfolio submissions; no Singapore Exchange (SGX)-listed security appears among the thirty most frequently held positions. We term this pattern reverse home bias-a preference for globally recognisable brand-name equities listed in a foreign market, which we attribute to crossnational availability heuristic rather than informational advantage. This preliminary finding motivates a theoretical framework that distinguishes reverse home bias from conventional geographic overweighting, and has distinct implications for portfolio risk and investor suitability assessment in the region. The DNA scoring architecturecombining deterministic portfolio analytics with LLM-assisted interpretation across seven specialised agents-produces complete behavioral portfolio reports in under sixty seconds, establishing the operational feasibility of real-time behavioral intelligence at practitioner scale.

---

## uid: `doi:10.2139/ssrn.6814893`

- title: G-Diag: Graph-Based Bottleneck Diagnosis for Pipeline-Parallel LLM Training
- authors: Xizhi Wang, Weixing Zhang, Runze Cai
- affiliations: not stated
- posted: 2026-05-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6814893
- keyword hits: large language model, llm

### abstract

Pipeline Parallelism (PP) is essential for hyperscale Large Language Model (LLM) training, yet existing profilers, planners, and simulators either overlook PP-specific dependencies in measured executions or fail to quantify which bottlenecks are actionable and how much workload can be safely rebalanced before bottleneck migration. We propose G-Diag, a trace-driven framework for PP-aware structural bottleneck diagnosis. G-Diag reconstructs profiler traces into a Pipelined Execution Graph (PEG) and introduces Optimization Dominance, a provable metric that separates actionable bottlenecks from critical but non-dominant microsteps. Building on this formalism, G-Diag parameterizes movable workload through trace-derived computation time, respects forward--backward coupling and workload-conservation constraints, and computes feasible rebalancing directions with a Dominance-guided optimization algorithm. We evaluate G-Diag on two production clusters and models up to 236B parameters, and validate its trace-derived workload parameterization against measured PP scaling. G-Diag uncovers up to 12.26% projected optimization headroom, reveals persistent group-specific bottlenecks at scale, and supports a production MoE-32B reconfiguration whose realized makespan matches the projection within 7.80%. Additional simulation shows that the same PEG-based formulation extends from canonical 1F1B to virtual-stage schedules, providing a theoretically grounded and practical approach for diagnosing structural inefficiencies in hyperscale PP training.

---

## uid: `doi:10.2139/ssrn.6811562`

- title: The use of GenAI in team science: Exploring the role of team size, task independence and geographical dispersion
- authors: Jeongwon Choi, Anna-Lena Rüland, Yao Qu, Madita Amoneit
- affiliations: not stated
- posted: 2026-05-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6811562
- keyword hits: generative artificial intelligence

### abstract

Generative artificial intelligence (GenAI) remains contested in its adoption within scientific research. While research on team science has increased, the role of GenAI in collaborative research settings remains underexplored. Drawing on a large-scale international survey of researchers’ reported use of GenAI in scientific publications, this study examines how structural conditions of team science, task independence and geographical dispersion, and their interaction with team size is associated with GenAI use. We find that neither task independence nor geographical dispersion alone significantly predicts GenAI adoption. However, both factors interact with team size such that larger teams are more responsive to these structural conditions than smaller teams. We interpret these findings as evidence that GenAI use in team science, while still contested, is driven by coordination needs, with stronger associations in larger, more dispersed, or task-independent teams. We further discuss how GenAI adoption in research teams is closely linked to competitive pressures in science. As a policy implication, we suggest that efforts to govern GenAI in research should move beyond individual-level prescriptions and instead emphasize shared norms, collective responsibility, and team-level governance.

---

## uid: `doi:10.2139/ssrn.6773381`

- title: The Synthetic Disinformation Boom: AI and the Collapse of Trust
- authors: David Venable
- affiliations: not stated
- posted: 2026-05-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6773381
- keyword hits: generative artificial intelligence

### abstract

Generative artificial intelligence has industrialized deception, enabling influence operations that are faster, cheaper, and harder to attribute than at any prior point in the history of information warfare. This briefing documents the emergence of what ISRS terms the "synthetic disinformation boom": a new phase of information conflict defined by automation rather than ideology, in which the cost of fabrication approaches zero while the cost of verification continues to rise. Drawing on open-source intelligence monitoring across 2025 election environments and politically sensitive information spaces, including the United States and Eastern Europe, ISRS analysts identify a shift from traditional troll farm operations toward machine-accelerated psychological warfare conducted with commercial tools and minimal human oversight. The briefing introduces the concept of cognitive saturation-the systematic exhaustion of public attention and institutional credibility through high-volume synthetic content-and examines its implications for epistemic security, democratic governance, and national resilience. Policy recommendations address content authentication infrastructure, cognitive security investment, synthetic content supply chain regulation, and AI counterintelligence capability development.

---

## uid: `doi:10.2139/ssrn.6774983`

- title: A.C.E. — AI Concierge & Engine An AI-Driven Financial Intelligence Framework for U.S. SME Restaurant Resilience
- authors: Arthunya Kanoklertwongse
- affiliations: not stated
- posted: 2026-05-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6774983
- keyword hits: generative ai

### abstract

This paper introduces A.C.E. (AI Concierge & Engine), an AI-powered financial intelligence framework designed to address the "Financial Blindness" crisis afflicting U.S. small and mediumsized enterprise (SME) restaurant operators. The U.S. restaurant industry generates $1.1 trillion in annual sales and employs 15.5 million Americans, yet the SME sector operates with a structural informational disadvantage relative to large corporate chains: manual invoice processing, fragmented data systems, and reactive pricing decisions create dangerous lags in response to supply chain cost volatility. A.C.E. proposes an Intelligent Neural Network architecture integrating Generative AI and machine learning directly into existing cloud-based point-of-sale (POS) infrastructures-including Toast and Clover-to achieve zero-touch invoice processing via AIoptical character recognition, real-time dynamic menu price optimization, and predictive labor scheduling. The system targets a 100% elimination of manual invoice data entry, a reduction of 15+ administrative hours per location per week, and measurable improvement in pricing decision velocity during inflationary periods. This paper presents the problem diagnosis, system architecture, AI component design, implementation strategy, risk assessment, and ethical governance framework. A.C.E. is designed as a platform-agnostic, API-accessible service deployable across the full network of SME restaurants without dependency on any single POS vendor or employer, positioning it as a cross-sector national economic intervention rather than a single-organization tool.

---
