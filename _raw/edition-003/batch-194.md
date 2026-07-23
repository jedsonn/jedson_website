# Classification batch 194 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-194.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6368558`

- title: AI Product Displacement Risk
- authors: Renping Li
- affiliations: not stated
- posted: 2026-03-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6368558
- keyword hits: ai agent, generative ai

### abstract

Generative AI can raise firm value by replacing workers but destroy it by replacing products. We construct AI Product Displacement Risk (AI-PDR), a firm-level measure of vulnerability to product substitution by generative AI. AI-PDR captures the demand-side threat to revenue, the opposite channel from the supply-side labor cost savings measured by existing AI-exposure indices. Event studies around four AI releases show that the displacement signal strengthens as AI advances from demonstration to targeted product substitution: early capability releases produce no within-industry return spread; a later release reveals a significant spread once correlated beta exposure is absorbed; and the 2026 launch of AI agents designed to replace specific incumbent SaaS products generates the largest repricing, with top-quintile firms underperforming bottom-quintile firms by 4.8 percentage points. Digital deliverability drives the entire effect.

---

## uid: `doi:10.2139/ssrn.6459920`

- title: An Empirical Study of Generative AI Adoption in Software Engineering
- authors: Görkem Giray, Onur Demirörs, Marcos Kalinowski, Daniel Mendez
- affiliations: not stated
- posted: 2026-03-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6459920
- keyword hits: generative ai, prompt engineering

### abstract

Objective. This study aims to provide an overview of the status of GenAI adoption in SE. It investigates the (1) status of GenAI adoption, (2) associated benefits and challenges, (3) institutionalization of tools and techniques, and (4) anticipated long-term impacts on SE professionals and the community.Method. We conducted an internationally distributed questionnaire-based survey to collect insights from SE practitioners. The survey combined closed-ended and open-ended questions to capture both quantitative trends and qualitative insights. We received 204 responses from 37 countries. Qualitative responses were analyzed using systematic coding and categorization. To cope with the random sampling limitation, we used bootstrapping and conservatively reported confidence intervals.Results. The results indicate a wide adoption of GenAI tools and that they are deeply integrated into daily SE work, particularly for implementation, verification and validation, personal assistance, and maintenance-related tasks. Practitioners report substantial benefits, most notably reduction in cycle time, enhanced support in knowledge work, perceived quality improvements and productivity gains. However, objective measurement of productivity and quality remains limited in practice. Significant challenges persist, including incorrect or unreliable outputs, prompt engineering difficulties, validation overhead, security and privacy concerns, and risks of overreliance. Institutionalization of tools and techniques seems to be common, but it varies considerably, with a strong focus on tool access and less emphasis on training and governance. Practitioners expect GenAI to redefine rather than replace their roles, while expressing moderate concern about job market contraction and skill shifts.

---

## uid: `doi:10.2139/ssrn.6392818`

- title: From Tool to Collaborator: Rethinking GIScience as GIS Becomes Agentic and Autonomous
- authors: Ali Khosravi Kazazi, Zhenlong Li
- affiliations: not stated
- posted: 2026-03-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6392818
- keyword hits: agentic, generative ai

### abstract

Geographic Information Systems (GIS) have long been positioned along Wright, Goodchild and Proctor's influential continuum of GIS as a tool, GIS as toolmaking, and GIScience, an arrangement that presumes GIS is epistemically passive and primarily executes human authored intent. This paper argues that the integration of generative AI into GIS introduces functional autonomy in goal interpretation, workflow and code generation, execution monitoring, and iterative revision, which increasingly breaks this boundary condition. Through an integrative narrative review of AI-enabled, agentic, and autonomous GIS, we trace a migration of intent from expert driven command execution toward partial delegation of planning and procedural assembly to systems operating in iterative loops. Building on this analysis, we propose the Agentic Role Entanglement (ARE) model, which replaces the tool-toolmaking-science continuum with an epistemic action loop in which tool use, toolmaking, and epistemic inquiry become dynamically coupled within a single episode. ARE model yields falsifiable implications for evaluation and peer review, motivating a shift from output checking to episode level validation. To support this shift, we outline a layered validation stack centered on provenance, reproducibility, workflow and code verification, geospatial sanity checks, and uncertainty bounded claims. We extend these requirements into a lifecycle view of distributed responsibility and ethical governance. We conclude by advocating a post instrumental GIScience that treats human-agent systems, rather than software alone, as the unit of analysis for scientific defensibility, reproducibility, and accountability.

---

## uid: `doi:10.2139/ssrn.6460573`

- title: Agentic Artificial Intelligence in Finance: A Comprehensive Survey
- authors: Irene Aldridge, Jolie An, Riley Burke, Michael Cao, Chia-Yi Chien, Kexin Deng, Ruipeng Deng, Yichen Gao
- affiliations: not stated
- posted: 2026-03-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6460573
- keyword hits: agentic, generative ai

### abstract

The emergence of agentic artificial intelligence (AI) represents a fundamental transformation in financial markets, characterized by autonomous systems capable of reasoning, planning, and adaptive decision-making with minimal human intervention. This comprehensive survey synthesizes recent advances in agentic AI across multiple dimensions of financial operations, including system architecture, market applications, regulatory frameworks, and systemic implications. We examine how agentic AI differs from traditional algorithmic trading and generative AI through its capacity for goal-oriented autonomy, continuous learning, and multi-agent coordination. Our analysis shows that while agentic AI offers substantial potential for enhanced market efficiency, liquidity provision, and risk management, it also introduces novel challenges related to market stability, regulatory compliance, interpretability, and systemic risk. Through a systematic review of foundational research, technical architectures, market applications, and governance frameworks, this survey provides scholars and practitioners with a structured understanding of how agentic AI is reshaping financial markets and identifies critical research directions for ensuring that these systems enhance both operational efficiency and market resilience.

---

## uid: `doi:10.2139/ssrn.6212818`

- title: TRACE: A Governance-First Execution Framework Providing Architectural Assurance for Autonomous AI Operations
- authors: Elias Calboreanu
- affiliations: not stated
- posted: 2026-03-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6212818
- keyword hits: ai agent, llm

### abstract

Autonomous AI agents increasingly take actions against external systems in environments where mistakes are costly and where post-hoc logs are insufficient for governance. We introduce TRACE (Trusted Runtime for Autonomous Containment and Evidence), a governance-first execution framework that treats the execution agent as untrusted and derives assurance from infrastructure mediation rather than model behavior. TRACE executes each operation under a cryptographically signed policy bundle that pinpoints tool definitions and encodes authorization boundaries, constraints, tripwire predicates, isolationtier selection, and success criteria. An Interface Gateway enforces complete mediation for all boundarycrossing actions, while independent boundary instrumentation (Y) provides telemetry that deterministic tripwires evaluate to trigger graduated containment levels (L0-L5) and fail-closed halts. TRACE produces a hash-chained, signed evidence log anchored with RFC 3161 timestamps, enabling audit reconstruction and post-incident forensics. We specify ten assurance properties, their dependencies on explicit deployment assumptions, and the corresponding proof obligations for mediation and evidence invariants. To make enforcement auditable without access to model internals, TRACE defines LLM-specific tripwire metrics for repetition (ARI), post-response divergence (PRDS), and plan-trajectory deviation (TMD), and provides an enumerable formal model of the containment finite-state machine. TRACE is presented as an architecture and specification; a research-grade skeleton reference implementation of core algorithms is released alongside this preprint, while full production implementation and empirical validation remain future work.

---

## uid: `doi:10.2139/ssrn.6465238`

- title: Agents, Inc.
- authors: Kevin Werbach
- affiliations: not stated
- posted: 2026-04-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6465238
- keyword hits: ai agent, generative ai

### abstract

AI agents—systems that plan, act, and interact in the world with limited human oversight—are proliferating across every sector of the economy. Unlike generative AI tools that produce content in response to prompts, agents can enter into contracts, execute financial transactions, communicate with third parties, and, with developments in robotics, operate machinery. This creates an accountability gap that existing tort, contract, and agency law alone cannot bridge. Important preconditions for law to function are absent when agents are the ones acting. There must be means of identifying responsible actors, tracing causation, attributing authority, and, in cases involving financial transactions or significant risks, ensuring funds and mechanisms are available for dispute resolution. This Article proposes a registration framework for AI agents, drawing on three bodies of knowledge not previously synthesized. First, it situates the accountability gap within a broader visibility problem and surveys the identification and registration systems, from corporate registration to securities identifiers to business numbering systems, that have made complex market actors legible throughout commercial history. Second, it draws on corporate law to provide the conceptual architecture, treating registration as a constitutive act that brings a new category of legal-governance object into existence, with structures calibrated to risk, limited liability as an incentive, and veil-piercing as an enforcement backstop. Third, it shows how blockchain technology provides the technical infrastructure for a dynamic, decentralized, programmable registry. The resulting regime operates on three tiers. Basic registration assigns a unique identifier, making agents visible to the legal system. Standard registration constitutes a legal-governance object with defined attributes and confers legal protections that incentivize voluntary participation. Full registration requires posting a surety bond via smart contract and adopting a Ricardian contract for dispute resolution. This regime would create the informational infrastructure that enables an AI insurance market to function, generating a self-sustaining cycle that does not depend on government mandates.

---

## uid: `doi:10.2139/ssrn.6546398`

- title: THE AI LEGAL REFERENCE MODEL (ALRM): A Ten-Factor Test for Distinguishing AI Tools from Third Parties in Privilege and Work Product Analysis with Ten Unresolved Questions for Judicial Consideration
- authors: Alexis Austin Litle, JD Morris, Deepankar Das
- affiliations: not stated
- posted: 2026-04-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6546398
- keyword hits: agentic, chatgpt

### abstract

On February 10, 2026, two federal courts issued opposing first-of-their-kind rulings on whether materials generated using publicly available artificial intelligence tools are protected from discovery. In Manhattan, Judge Jed S. Rakoff held in United States v. Heppner that thirty-one documents a criminal defendant generated using a consumer AI tool were neither privileged nor protected work product, treating the AI platform as a third party whose terms of service destroyed confidentiality. In the Eastern District of Michigan, Magistrate Judge Anthony P. Patti held in Warner v. Gilbarco, Inc. that a pro se plaintiff's ChatGPT queries and responses deserved work product protection, observing that AI programs “are tools, not persons.” Seven weeks later, in Morgan v. V2X, Inc., Magistrate Judge Maritza Dominguez Braswell split the difference, protecting AI-assisted litigation materials while imposing a contractual safeguard test requiring vendors to prohibit training on inputs and disclosure to third parties. This Article proposes the AI Legal Reference Model (ALRM): a ten-factor test organized around four analytical dimensions — attorney-agency relationship, contractual architecture, system architecture, and review mechanism — for determining when an AI system functions as a tool (preserving privilege and work product protections) and when it functions as a third party (destroying them). The framework's system-architecture dimension is grounded in three independent formal impossibility theorems establishing that hallucination cannot be eliminated from any AI system retaining a stochastic generation step. Drawing on Sequoia Capital's distinction between “copilot” and “autopilot” AI business models, the Article maps that taxonomy onto the doctrinal architecture of attorney-client privilege, the work product doctrine, and Model Rule 5.3. The Article then identifies ten unresolved questions the framework surfaces — including attorney-directed use of consumer AI, multi-agent privilege chains, AI memory contamination, and judicial use of AI — and proposes analytical directions for courts confronting each. Applying the framework to those ten questions, the Article projects that eight will resolve in favor of third-party classification, two in favor of tool classification, and two will split on the fact pattern, a directional prediction that places the framework at risk of falsification. This Article is the first in a nine-paper series, The Architecture of Legal AI. Subsequent papers extend the framework to judicial AI candor obligations (Paper 2), hallucination and the architecture of trust (Paper 3), product liability for the legal AI vendor (Paper 4), the regulatory architecture of legal AI (Paper 5), and the agentic law firm (Paper 6). The ten-factor test introduced here is the analytical spine on which each extension depends.

---

## uid: `doi:10.2139/ssrn.6641378`

- title: Control and Governance of Generative and Agentic AI: An AIS Lifecycle Framework for Privacy and Security
- authors: Sumit Sharma
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6641378
- keyword hits: agentic, generative artificial intelligence

### abstract

Generative artificial intelligence (GenAI) and agentic AI architectures are rapidly being integrated into organizational information systems and automation frameworks. While these technologies promise efficiency gains in knowledge work, automation, and decision support, their autonomy, system-level access, and coordinated actions introduce significant privacy and security risks. These risks differ from those associated with traditional software or analytics systems. From an Accounting Information Systems (AIS) perspective, these developments challenge assumptions of bounded execution, stable role-based access, and auditable transactions supported by systematic audit trails. Agentic AI systems may autonomously invoke tools, access sensitive organizational data, and interact with other agents in ways difficult to observe or constrain using conventional internal controls. This research letter proposes an AISoriented privacy and security control framework for GenAI and agentic AI systems integrating five control dimensions: identity and access control, governance and policy design, monitoring and audit mechanisms, cryptographic guardrails, and agentic resilience.

---
