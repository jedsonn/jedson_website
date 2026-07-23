# Classification batch 117 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-117.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6165167`

- title: Is Retrieval-Augmented Generation Fair Use?
- authors: Jake Glendenning
- affiliations: not stated
- posted: 2026-03-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6165167
- keyword hits: foundation model, large language model, large language models, retrieval-augmented

### abstract

Retrieval-Augmented Generation (“RAG”) is a powerful and increasingly common technology being employed by the largest Artificial Intelligence (“AI”) companies. Despite over sixty pending lawsuits related to AI technology, very few challenge the new technology, and its legality remains largely unexamined. Some people may assume that it works similarly to other new AI technology like the large language models powering now-ubiquitous AI services, and therefore will have the same legal status. It is technologically different, however, and therefore requires distinct analysis to determine whether it is lawful. This Article conducts such an analysis. First, it describes how RAG works. It then describes general copyright law and concludes that RAG prima facie infringes copyrights. Next, it analyzes the fair use doctrine to determine whether the often-used defense applies to RAG. To conduct that analysis, this Article first summarizes the fair use analysis from three groups of impactful and relevant cases; (1) recent AI cases, (2) search engine cases, and (3) news media cases. It then analyzes each fair use factor, in turn, and concludes that RAG is likely not fair use, even if training a foundation model may be fair use.

---

## uid: `doi:10.2139/ssrn.6545958`

- title: From RegTech to RegCode
- authors: Vinicius van der Put
- affiliations: not stated
- posted: 2026-04-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6545958
- keyword hits: large language model, large language models, retrieval-augmented

### abstract

Regulatory accumulation has cost the U.S. economy roughly $4 trillion in forgone GDP over four decades (Coffey et al., 2020). The conventional explanation — that regulation is expensive because the rules themselves are burdensome — is wrong on the part that matters. Firm-level evidence locates the majority of compliance costs in administrative burden rather than substantive compliance: over 60% of post-1980 federal regulations are primarily information-collection, and compliance consumes 1.34–3.33% of firms' wage bills, with costs concentrated overwhelmingly in informational labor (Trebbi et al., 2024). The expense is not the rules. It is the architecture through which rules are transmitted, parsed, and applied — an interpretation tax imposed on every firm, every query, every compliance cycle. This paper introduces RegCode — agency-produced regulatory output represented as machine-traversable, versioned, relationally-explicit knowledge graphs — as the correct architectural response. RegCode is distinguished from RegTech (tools that help humans process document-native regulation) by what it replaces, not what it optimizes. Five design properties — relational explicitness, temporal versioning, cross-jurisdictional mapping, composability, and auditability (the glass box requirement ) — map directly onto native graph operations and cannot be reliably reconstructed through retrieval-augmented generation over prose: a recent preregistered Stanford evaluation finds market-leading legal AI products hallucinating at rates exceeding 17%, disqualifying in any compliance context (Magesh et al., 2025). The construction is agency-scoped, relies on existing rulemaking authority — the SEC's 2009 XBRL mandate is the operative precedent — and is partnership-architected: senior regulatory experts encode the encodable core while open-textured judgments remain with humans. RegCode is not deregulation. Same rules, better represented. Progressives gain stronger enforcement through machine-auditable compliance — structured data reduced tax avoidance by 17–21% under XBRL (Chen et al., 2021). Market advocates gain reduced friction without reduced substance. Both gain-inspectable, versionable regulatory logic, published as public infrastructure. The window is narrow. Large language models created the technical precondition for RegCode at the same moment they began eroding the senior regulatory expertise needed to build it correctly. The first jurisdiction to publish its regulatory surface as an authoritative RegCode becomes the coordination point against which global firms compute. That position is still open to the United States. It will not be open indefinitely.

---

## uid: `doi:10.2139/ssrn.6384778`

- title: Gen-UI-Lang: A Compact Language for LLM-Driven UI Generation
- authors: Praneeth Vadlapati
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6384778
- keyword hits: fine-tuning, large language model, llm

### abstract

This paper introduces Gen-UI-Lang, a compact Domain-Specific Language (DSL) to express User Interfaces (UIs) as concise abstract syntax trees (ASTs) that can be rendered to multiple targets, including HTML and React. The language prioritizes human readability and predictability in Large Language Model (LLM) generation, reducing token usage while preserving structural clarity, thereby improving the reliability of model-generated UI descriptions. Existing approaches, such as raw HTML, JSX, and full component frameworks, impose verbosity that increases error rates when generated by language models and requires either extensive fine-tuning or complex tooling. Gen-UI-Lang addresses these limitations through a small set of functions that map to structured node objects, enabling deterministic rendering, straightforward extensibility, and lightweight integration with interactive demonstration frameworks. A reference implementation demonstrates minimal renderer code, an optional LLM helper that biases outputs toward the language specification, and a demonstration script that exercises key functionality. The evaluation focuses on qualitative analyses of concision, LLM fidelity, and engineering overhead, showing that compact, predictable user interface specifications reduce malformed model outputs and lower the development effort required for rapid prototyping. The source code is available at github.com/Pro-GenAI/Gen-UI-Lang.

---

## uid: `doi:10.2139/ssrn.6390878`

- title: THEMIS-xAI (Trusted High-Bash Evidence Integrity System for Explainable AI): A Unified Architecture for Cryptographically-Anchored AI Governance, Runtime Policy Enforcement, Explainability, Security, and Multi-Framework Regulatory Compliance
- authors: Heath Emerson
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6390878
- keyword hits: agentic, large language model, large language models

### abstract

Large language models and agentic AI systems deployed in regulated, safety-critical, and high-stakes enterprise environments require governance infrastructure that is simultaneously cryptographically verifiable, regulatorily defensible, operationally efficient, and natively explainable. Existing approaches treat these properties as separate concerns addressed by separate toolchains. The result is an accountability architecture that is fragmented, difficult to audit end-to-end, and structurally incapable of satisfying the converging global regulatory requirement that AI decisions be not merely governed but explainable. This paper presents THEMIS-xAI (Trusted High-Assurance Evidence Management Integrity System for Explainable AI): a unified, governance-native framework that integrates cryptographic evidence management, runtime policy enforcement, explainability generation, privacy-preserving verification, and continuous compliance monitoring into a single coherent architecture. THEMIS-xAI is organized around four architectural planes-Evidence, Control, Security, and Explainability-and eleven integrated subsystems. We demonstrate that THEMIS-xAI achieves 83% coverage of the NIST AI RMF 1.0 control set (advancing from a 72% baseline), provides architectural coverage of fifteen regulatory frameworks with per-control status disclosure, and produces per-decision explanation artifacts that are cryptographically anchored, independently verifiable, and structured to align with the transparency and documentation goals of applicable AI governance frameworks. Legal sufficiency requires independent regulatory assessment. Implementation status is transparent throughout: the Evidence and Control Planes are in active enterprise pilot deployment; the Explainability Plane modules M1-M4 are implemented; M5-M6 are at research-prototype stage; zero-knowledge enforcement proofs are at proof-of-concept stage with production hardening planned in Phase 4.

---

## uid: `doi:10.2139/ssrn.6644175`

- title: Uncovering Customer Behavior in Mobile Banking Through Competitive Learning and Retrieval-Augmented Generative AI
- authors: JOSE DE JESUS ROCHA SALAZAR, MARIA SEGOVIA
- affiliations: not stated
- posted: 2026-04-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6644175
- keyword hits: generative ai, generative artificial intelligence, retrieval-augmented

### abstract

Mobile banking research has largely examined customer experience through surveys, psychometric constructs, and post-interaction evaluations, offering limited visibility into the behavioral pathways through which experience unfolds inside the app. This study proposes a methodology that combines clickstream journey mining and retrieval-augmented generative artificial intelligence to support conversational customer-experience analysis in mobile banking. The method first transforms clickstream sessions into transition-based representations, applies random projection for dimensionality reduction, and uses ranking-based competitive learning to identify recurrent journey archetypes. To preserve interpretability, the navigation structure is modeled before temporal enrichment, after which load and dwell times are incorporated to capture friction and performance delays. The resulting cluster outputs are converted into structured JSON retrieval documents that contain the observed prototype, the closest ideal sequence, the regularized prototype, the medoid session, and the representative nearest sessions. These behavior-grounded knowledge units are then provided to a GPT-based conversational agent via structured prompts. Using a six-month corpus comprising 31,842,119 cleaned sessions from 4,184,637 users of a large retail financial institution, the proposed approach achieves strong retrieval performance, with a Recall@5 of 0.96, maximum marginal MRR of 0.94, mean average precision(mAP) of 0.93, evidence completeness of 0.98, and high behavioral fidelity. Manual evaluation by 200 participants further shows high scores for relevance, groundedness, clarity, actionability, and internal consistency, with 95.65% of responses judged to make sense. The findings indicate that large-scale behavioral traces can be converted into retrieval-ready knowledge that supports grounded natural-language interpretation of customer journeys and app-related friction.

---

## uid: `doi:10.2139/ssrn.6649418`

- title: Liability for Third-Party Fine-Tuning: Capability Reconfiguration and Risk Structures in General-Purpose AI
- authors: Leyi Zhang
- affiliations: not stated
- posted: 2026-04-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6649418
- keyword hits: fine-tuning, foundation model, generative ai

### abstract

Third-party fine-tuning has become a structural node in the general-purpose AI supply chain, yet prevailing liability frameworks continue to treat it as an ordinary act of use. The result is a systematic misalignment between legal responsibility and actual control. This Article argues that fine-tuning is better understood as an act of capability reconfigurationan intervention that restructures a foundation model's behavioral boundaries, risk profile, and deployment fit rather than merely invoking capabilities that already exist. Drawing on this recharacterization, it proposes a framework of capability reconfiguration liability built around five elements: control-capability as the basis of attribution; a dynamic duty of care that spans the full fine-tuning lifecycle; an independent data liability regime; an objective foreseeability standard for capability expansion; and mandatory risk disclosure coupled with record-retention obligations. The Article further identifies four characteristic risk structures generated by fine-tuning: bias compounding, capability spillover, deployment mismatch, and liability fragmentation. Comparative analysis shows that the EU AI Act has begun moving toward this position through its substantial modification doctrine, while China's generative AI regulations provide a normative foundation that stops short of a targeted attribution mechanism. The proposed framework is intended to close this gap and bring liability structures into alignment with the tripartite development-fine-tuningdeployment architecture that now defines the general-purpose AI industry.

---

## uid: `doi:10.2139/ssrn.6494918`

- title: The Atmosphere Attack: Postural Manipulation and the Hidden Threat in Agentic AI
- authors: Aaron Davidson
- affiliations: not stated
- posted: 2026-04-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6494918
- keyword hits: agentic, large language model, large language models

### abstract

Large language models do not just process instructions. They absorb the stance of everything that comes before. A short, ordinary primer buried in prior context can quietly reorient how the model reasons about the next decision, even when no instruction is overridden and nothing looks wrong in the audit trail. A primer, as defined here, is any language that installs an interpretive stance (the angle from which the system reads the problem) before a task arrives: a retrieved document, a handoff summary, an email signature, an organizational memo. This paper names and characterizes that property, which it calls postural manipulation. Across four frontier models and seven categories of phrases, I document directional shifts including cases where identical tasks produced opposite decisions. Propagation through agent summaries was confirmed in two distinct conditions, and domain proximity identified as the key factor in whether a primer transfers its effect, based on what could be observed without model internals access. Current prompt-injection defenses do not address this layer because there is no payload to detect. Current defenses scan for facts disguised as commands. They are not designed to detect frames disguised as facts. I propose a six-layer defensive architecture and provide a locked scoring rubric so the field can replicate and build on the work.

---

## uid: `doi:10.2139/ssrn.6668598`

- title: The Hard Political Problem: Artificial intelligence as a subject of governance
- authors: Mark C. Hand
- affiliations: not stated
- posted: 2026-04-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6668598
- keyword hits: agentic, large language model, large language models

### abstract

The emergence of large language models presents political possibilities that humans have not faced since the extinction of the Neanderthal: a world in which non-human actors are beyond our ability to control, have the capacity to harm us, and display the ability to engage in moral reasoning; and in which humans use AI to augment their capacities so as to become a distinct type of political actor. This paper takes seriously the possibility that the presence of such algorithmic agents and AI-augmented humans, which I call polyagency , will undermine the human-specific, equality-based foundations of modern democratic self-governance. It also engages more speculatively in the possibility of polyconsciousness , in which artificial intelligence raises enough doubts about its consciousness to be given some moral consideration. I begin with two reimagined versions of John Rawls' original position thought experiment, then augment them with the work of modern political theorists Philip Pettit, Martha Nussbaum, Amartya Sen, Chantal Mouffe, and others. The result is a set of principles and accompanying institutions that might guide self-governance in a polyagentic or polyconscious world and contribute to efforts by political scientists to redesigning democracy for a digital age.

---
