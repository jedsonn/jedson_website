# Classification batch 340 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-340.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6944358`

- title: Can Automation Offset Population Decline? Occupational Imbalances in a Shrinking Workforce
- authors: Donghyun Suh, Soo Jung Chang
- affiliations: not stated
- posted: 2026-07-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6944358
- keyword hits: large language model, llm

### abstract

This paper studies whether automation can mitigate the labor-market effects of population decline and how this mitigation differs across occupations. Korea's working-age population is projected to fall by about 11 percent between 2024 and 2034. Holding current occupational demand fixed, we first project occupation-level labor-supply imbalances using Korean population projections and age-by-occupation employment data. We then estimate occupation-level automation probabilities by applying a large language model (LLM) to O*NET task statements and mapping the resulting task-level measures to Korean occupations. Automation can substantially reduce the aggregate labor shortfall, but it does not eliminate occupational imbalance because automation potential is only weakly aligned with projected demographic shortages. The main implication is therefore compositional: population decline changes the distribution of labor scarcity, while automation changes where shortages persist and where surplus pressure emerges. With sufficiently rapid AI progress, the same framework implies that the policy problem may shift from aggregate labor shortage to the distribution of labor surplus across occupations.

---

## uid: `doi:10.2139/ssrn.6950742`

- title: Agentic Proxies: Governance, Accountability, and the Architecture of a Trustworthy AI Economy
- authors: Geoff Lundholm
- affiliations: not stated
- posted: 2026-07-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6950742
- keyword hits: agentic, ai agent

### abstract

Three claims organise this paper. First: the emerging accountability problem in AI is not human-to-AI interaction. It is AI-to-AI delegation-the transfer of authority, mandate, and responsibility across chains of autonomous agents that act at machine speed, across vendor boundaries, without continuous human involvement. Existing governance frameworks-identity systems, observability platforms, compliance APIs-establish who an agent claims to be and what it did. None establish whether a delegated action remained continuously authorised across a multi-agent workflow. That is the gap this paper addresses. Second: bounded delegation is the preferable design philosophy for AI systems acting consequentially on behalf of humans-not as a temporary concession to present-day limitations, but as an enduring principle. An AI agent operating under explicit, bounded, verifiable delegation is not a constrained version of a fully autonomous agent. It is a different and more trustworthy class of actor: one whose actions are attributable, whose authority is traceable, and whose failures are governable. We term this class the agentic proxy. Third: insurability emerges from accountability, not from model capability. Fully autonomous agents are structurally uninsurable because they satisfy none of the three conditions underwriters require-identifiable exposure, attributable causation, and verifiable governance. Agentic proxies satisfy all three by design. This creates the foundation for a viable AI insurance market, and makes the governance architecture described in this paper not merely a design preference but a commercial and regulatory requirement. The paper introduces a working definition of agentic proxies, establishes their six core properties, and distinguishes them from adjacent concepts. It presents the CTX Envelope as the architectural primitive for preserving accountability across agent handoffs, and argues that the attestation layer verifying these chains must be structurally independent of the entities producing them-for the same reason that audit firms, certificate authorities, and inter-bank messaging systems are independent. Through case studies spanning healthcare, financial services, legal workflows, and manufacturing, the framework is tested against real deployment challenges. The paper concludes by situating the agentic proxy model within the broader history of trust infrastructure-SWIFT, ACORD, TLS, SOC 2-arguing that AI requires the same institutional foundations that commerce, banking, payments, and the internet eventually required.

---

## uid: `doi:10.2139/ssrn.6947058`

- title: ANNEX: An Ethical AI-Enhanced Open Source Intelligence (OSINT) Framework for Data Analysis and Identity Resolution Week 3: Entity Extraction, Identity Resolution Matrix Design, and Relationship Mapping
- authors: Maia Fichtenholtz Sek
- affiliations: not stated
- posted: 2026-07-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6947058
- keyword hits: gemini

### abstract

This paper documents the third week of the ANNEX project, covering the development of the system's core intelligence layers: Entity Extraction, Identity Resolution, and Relationship Mapping. The five working days between June 8 and June 12, 2026 moved the ANNEX pipeline from a validated collection and normalization prototype into a system capable of extracting named entities from raw legal documents, resolving fragmented identity records into structured profiles, and mapping relational connections across resolved entities. Monday opened with a scheduled review of the Entity Extraction layer, assessing the accuracy of Gemini 1.5 Flash in identifying names, addresses, and case identifiers from raw legal PDFs, and documenting false positive rates and accuracy metrics before beginning the Framework Architecture section draft. Tuesday developed the Neural Processing Core, configuring NLP pipelines to scan documents for people, organizations, and digital identifiers, and testing entity extraction on sample legal documents. Wednesday designed the Identity Resolution Matrix, configuring AI deduplication and entity matching logic, defining the probability scoring system, and setting up manual verification flags for high-stakes matches. Thursday created system workflow diagrams and architecture visuals mapping the full pipeline from raw data to structured identity graphs. Friday closed the week with a scheduled review of probability scores for identity matching, an assessment of the first visual graph drafts using React Force Graph, and an analysis of the Relationship Mapping layer covering nodes, edges, affiliations, ownerships, and geographic links. The results confirm that the ethical constraints built into the ANNEX architecture in Weeks 1 and 2 hold under the more demanding conditions of the intelligence-producing layers.

---

## uid: `doi:10.2139/ssrn.6946258`

- title: Frontier Safety for Powerful Open Models
- authors: Spencer E. Amdur
- affiliations: not stated
- posted: 2026-07-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6946258
- keyword hits: claude

### abstract

What happens when open models reach the capabilities of Claude Mythos and beyond? Estimates suggest that open models may lag 6 to 18 months behind their closed frontier counterparts. That means that, this year or next, open-weight models could become capable of materially facilitating cyberattacks on critical infrastructure and IT systems. Soon after, they could become capable of meaningful CBRN uplift. Because open-weight safeguards can often be removed, public release of such models may make it impossible to prevent a wide range of actors from accessing dangerous capabilities. This paper examines how governments, labs, and the open-source community should approach open model governance as these risks become more concrete. The issue has changed substantially since the open-versus-closed debates of 2024. The importance of the open ecosystem has become clearer; frontier models have begun to reach specific dangerous capabilities; mitigation and testing methods have advanced unevenly; and open-weight governance has become an international issue with the rise of Chinese open labs. At the same time, AI policy has barely begun to address the distinct issues raised by powerful open models. This paper first explains the problem, then surveys the landscape of open model development, summarizes the state of open-model mitigation and capability testing, and proposes governance steps that can preserve the benefits of openness while addressing serious risks. The paper's central conclusions are that (1) capability testing must be the primary input for open-release decisions because open-weight mitigation remains unreliable; (2) there is a significant testing gap between open and closed labs; and (3) the most urgent task is to improve testing resources for open models so that labs and governments can identify models that are too dangerous for unrestricted release. There are a number of actions that governments, labs, and researchers can take, starting now, to address these risks and preserve the many benefits of openness. Open-model developers should devote more resources to capability testing, seek third-party testing where possible, and test helpful-only checkpoints to measure underlying capabilities after safeguards are removed. Closed-model developers should share advances in capability testing, either publicly or directly with open labs. CAISI, AISI, and other safety institutes should offer testing services to open labs. The executive branch should treat open-weight governance as a central part of U.S.-China AI engagement, including through technical assistance to CnAISDA. State and EU regulators supervising transparency laws and independent verification organizations should focus on open-model capability testing. Finally, the open-source community should begin designing licensing, data-security, and know-your-customer approaches for securing powerful open models before release.

---

## uid: `arxiv:2607.10198v1`

- title: Equal Accuracy, Unequal Evidence: Search APIs as Decision Surfaces for Tool-Using Agents
- authors: Sriram Selvam, Anneswa Ghosh
- affiliations: not stated
- posted: 2026-07-11
- source: arXiv
- link: https://arxiv.org/abs/2607.10198v1
- keyword hits: gpt-5

### abstract

Search APIs are the fundamental retrieval layer for many agents and are often their most frequently used tool. Traditional search APIs provide URLs, titles, and snippets that preview website contents. Because full-page retrieval is token-intensive, agent retrieval architectures increasingly use progressive disclosure: the agent first sees snippets and then chooses whether to fetch full pages. In such systems, search API performance is often evaluated primarily by answer accuracy. We argue that a commercial search API is better understood as a decision surface: the ranked snippets, URLs, and metadata that determine whether an agent answers immediately, searches again, or spends tokens opening pages. We test this claim with one frozen GPT-5.4 agent, two tools (search_web and fetch_page), and 100 questions from SEALQA-HARD, varying only the search provider (Brave, Tavily, Firecrawl). A Kimi-K2.6 oracle labels every content element visible to the agent (URL, title, snippet, and fetched page, when fetched), producing 6,869 valid per-URL judgments. We use an audited correct-answer label, semantic match, which preserves exact matches while accepting harmless formatting and naming variants. Under this measure, the providers remain close (25, 25, 26 / 100), but their evidence economies differ sharply: Brave offers gold-answer-rich snippets, Tavily concentrates gold-supporting URLs at rank 1, and Firecrawl is associated with broader exploration under this fixed agent policy. We also introduce a surface contradiction-to-gold URL ratio, which varies from 0.92 to 2.59. Provider choice is therefore a retrieval-budget and policy decision, not merely a recall decision.

---

## uid: `arxiv:2607.10113v1`

- title: Dynamic Agent Skills: A Lifecycle Survey and Taxonomy of Evolving Skill Libraries
- authors: Yubo Li
- affiliations: not stated
- posted: 2026-07-11
- source: arXiv
- link: https://arxiv.org/abs/2607.10113v1
- keyword hits: large language model

### abstract

Large language model agents increasingly store reusable procedures outside the model. These reusable procedures are often called \emph{skills}: they may be code functions, natural-language instructions, SKILL.md packages, workflow graphs, or learned adapters that a future agent can retrieve and invoke. This taxonomy-driven survey asks how such skill libraries change over time. Across a $124$-paper $2023$--$2026$ audit set, we synthesize dynamic skill systems as \emph{lifecycle-managed, verified, evolving artifact stores}: agents collect evidence from interaction, propose skill updates, verify and admit candidates, organize them for retrieval and composition, repair or prune stale entries, and govern sharing through provenance and rollback. We organize the literature around three survey tools. First, a $\text{six}$-sense taxonomy distinguishes the structurally different artifacts called ``skills'' in current papers. Second, an $\text{eight}$-stage lifecycle architecture identifies the recurring design decisions behind evidence acquisition, proposal, verification/admission, storage, retrieval/composition, maintenance, distillation/portability, and governance. Third, a lightweight skill-record schema and $\text{ten}$-operator vocabulary provide common terms for comparing library updates without elevating them into a separate method contribution. Using this structure, we synthesize evidence-graded patterns with explicit caveats: admission and repair are repeatedly important, verifier quality materially affects skill-aware RL, flat retrieval can degrade as libraries grow, and current benchmarks still under-report library trajectories, usage--utility gaps, and safety surfaces. We close with concrete reporting standards and open problems for evaluating dynamic skills as changing libraries rather than static prompt or tool collections.

---

## uid: `arxiv:2607.10814v1`

- title: Auditing Belief-Conditioned LLM Agents in Hidden-Information Social Deduction Games
- authors: Yuan Gao, Jiangyi Yang, Yao Zhao, Yichi Zhang
- affiliations: not stated
- posted: 2026-07-12
- source: arXiv
- link: https://arxiv.org/abs/2607.10814v1
- keyword hits: llm

### abstract

Evaluating LLM agents in hidden-information multi-agent settings is hard: final outcomes are high-variance and rarely reveal why an agent decided as it did. We study this in a 9-player Werewolf environment where agents act under strict, code-level information isolation, and we build an auditable framework that maintains an external belief state over hidden roles, logs belief updates and belief-action deviations as structured evidence, and supports a defensive offline improvement loop that reviews bad cases before any strategy change. Across 1,080 frozen games spanning belief-disabled, active-belief, kernel-ablation, camp-restricted, consumption-policy, and high-load arms, and including a seed-paired A0/A1 comparison, the active-belief condition is associated with substantially better good-side outcomes: in the 200-seed A0/A1 comparison the good-side win rate rises from 0.205 to 0.390 (paired McNemar $χ^2 = 16.4$, $p < 0.001$), with fewer irreversible witch-poison errors. We do not, however, attribute this shift to belief content. Direct action-belief consistency is low ($\approx 0.21$), and giving belief only to the werewolves helps the good side more than giving it only to the good side, which argues against a simple holder-benefit account; we therefore report the effect as an association and treat its mechanism as unresolved. The contribution is the audit framework itself: it makes the effect measurable, exposes low direct action-belief consistency, rejects an unreliable forced-consumption intervention with evidence, and separates strategy effects from load confounds. We accordingly position external belief in high-noise hidden-information games primarily as an auditable cognitive baseline that also carries decision-relevant signal, turning opaque agent behavior into replayable evidence for safer, controlled iteration.

---

## uid: `doi:10.2139/ssrn.6951718`

- title: When AI Agents Spend Your Money: Card Rails, Stablecoins, and the Coming Lock-In of Agentic Commerce
- authors: David Krause
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6951718
- keyword hits: agentic, ai agent

### abstract

Agentic commerce, in which autonomous AI software purchases goods on behalf of consumers, is emerging faster than the academic literature has documented. Two competing payment architectures have materialized. Tokenized card networks, led by Visa and Mastercard, offer reversibility and dispute resolution. Stablecoin protocols, led by Coinbase's x402, offer finality and microtransaction viability. This paper argues that these are not mere technical variants but incompatible economic and legal logics. The card model embeds consumer protection through ex post reversibility. The stablecoin model embeds efficiency through ex ante cryptographic finality. Through a synthesis of recent academic literature and industry developments, we show that neither architecture can fully incorporate the other's core logic. We further argue that payment preferences exhibit strong path dependence and switching costs, making early consumer delegation decisions prone to lock-in. The paper concludes by identifying open research questions at the intersection of payments economics, consumer protection law, and agentic system design.

---
