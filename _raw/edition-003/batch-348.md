# Classification batch 348 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-348.answer.json` as a JSON array.

---

## uid: `arxiv:2607.14491v1`

- title: Manufactured Divisiveness: Decomposing the Hostile Content of Seven Social Media Influence Operations
- authors: Emilio Ferrara
- affiliations: not stated
- posted: 2026-07-16
- source: arXiv
- link: https://arxiv.org/abs/2607.14491v1
- keyword hits: llm

### abstract

State-backed influence operations are routinely measured as high-prevalence sources of ``hate'' and ``toxicity.'' We argue those rates rest on a measurement error: the detectors behind them are validated to catch a broader definition inclusive of hostility or divisiveness aimed at an out-group, and so over-attribute hate to content better described as partisan or geopolitical invective. Across 25.08M tweets from seven government-attributed campaigns in the Twitter Information Operations archive (8,275 accounts), we separate hate from the other forms of divisiveness. We first validate a two-prompt LLM-based detector, matching human labels at Cohen's $κ=0.82$, to identify the broader hostility; we then develop an auditable rule, agreeing with an expert at $κ=0.52$, to further classify this content (5,457 posts) into three sub-categories. About 50.1% are identity-based attacks on people, whereas 30.4% are partisan attacks and 19.5% invective against states and their foreign policy. Reporting all of it as hate therefore overstates hate roughly twofold; only 18.7% is both identity-based and dehumanizing or inciting. Six of seven campaigns sort into three regimes that a single ``hate'' rate flattens, namely identity hate (RU-op and IRA, both Russia-attributed), geopolitical invective (both Iran operations), and partisan divisiveness (both Venezuela operations). We call the shared product $manufactured divisiveness$. The line to separate these constructs itself remains unsettled: on the hardest cases three independent human experts agree only moderately (pairwise $κ=0.37$--$0.50$), and the best of nineteen LLM models tops out at $κ=0.601$ against the experts' majority. Our findings can help redefine the study of hate in the context of influence campaigns and broader online discourse.

---

## uid: `arxiv:2607.14443v1`

- title: Tactile: Giving Computer-Using Agents Hands and Feet
- authors: Yong Liu, Zhenyi Zhong, Zhanpeng Shi
- affiliations: not stated
- posted: 2026-07-16
- source: arXiv
- link: https://arxiv.org/abs/2607.14443v1
- keyword hits: claude

### abstract

Computer-use agents are becoming capable software operators, but their interface to desktop applications is still often a brittle motor layer: they look at screenshots, predict coordinates, click, and hope that the visible state changed as intended. This collapses target grounding, action execution, and outcome verification into a single ambiguous operation. We present Tactile, an open-source tool layer that gives agents a more reliable "hands and feet" for desktop use. Tactile converts heterogeneous UI evidence--operating-system accessibility semantics, OCR-grounded text, and visual fallback regions--into action-grounded interface states: compact target candidates with source labels, roles or text, state, geometry, executable affordances, and verification cues. Agents operate through an observe-ground-act-verify loop that prefers native semantic actions when available, falls back to OCR-grounded coordinates when visible text is the best evidence, and keeps full provenance for replay and failure attribution. On macOSWorld-style tasks, adding Tactile improves Codex Success@100 from 41.1% to 50.0% overall and from 45.2% to 55.3% on accessibility-adapted tasks; a 96-task cross-agent subset shows consistent gains across Codex, Claude Code, OpenCode, and Goose. These results suggest that reliable computer use requires not only stronger models, but also a reusable execution substrate that exposes software actions as semantic, verifiable, and auditable objects rather than anonymous screen coordinates.

---

## uid: `doi:10.2139/ssrn.7062598`

- title: Towards a Rigorous Framework for Human-Supervised GenAI-Assisted Qualitative Policy Document Analysis
- authors: Pedro Fidelman
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7062598
- keyword hits: generative artificial intelligence

### abstract

Generative artificial intelligence (GenAI) is increasingly being incorporated into qualitative research workflows, creating new opportunities for coding, classification, synthesis, and analysis of large textual datasets. While a growing methodological literature has examined the use of GenAI in qualitative research, relatively little attention has been given to its application in qualitative policy document analysis. This is a significant gap because policy documents constitute a distinctive form of qualitative research material, and analytical tasks vary substantially in their interpretive complexity and suitability for GenAI assistance. This paper develops a methodological framework for rigorous human-supervised GenAIassisted qualitative policy document analysis. The framework is based on the principle of bounded delegation, whereby the suitability of GenAI assistance varies according to the interpretive demands of the analytical task. The paper distinguishes among extraction and retrieval; structured deductive analysis; semi-deductive interpretive analysis; and interpretive or abductive analysis, and proposes corresponding boundaries for GenAI involvement. It further develops a human-supervised analytical workflow and a set of rigour principles centred on transparency, auditability, reflexivity, validation, and process traceability. This paper argues that GenAI is best understood not as a replacement for qualitative policy inquiry, but as a selectively deployable extension of computer-assisted qualitative data analysis traditions embedded within human-supervised inquiry. By developing a bounded delegation framework, a human-supervised analytical workflow, and associated rigour principles, the paper offers a methodological foundation for conducting and reporting GenAIassisted policy document analysis. In doing so, it contributes to emerging methodological debates concerning the rigorous integration of artificial intelligence into policy research and qualitative inquiry.

---

## uid: `doi:10.2139/ssrn.6980618`

- title: From Manual Outreach to Autonomous Pipelines: A Conceptual Framework for Conversational, MCP-Orchestrated B2B Sales Prospecting
- authors: Deepak Amirtha Raj
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6980618
- keyword hits: generative ai

### abstract

Business-to-business (B2B) sales development has long depended on manual prospecting, in which sales development representatives (SDRs) research prospects individually on professional networks such as LinkedIn, compose outreach by hand, and track activity in spreadsheets. While artificial intelligence (AI) has been shown to enhance sales efficiency across the B2B funnel (Paschen et al., 2020; Syam & Sharma, 2018), its adoption remains uneven, and a recent estimate found that only 21% of business and sales leaders reported fully adopting generative AI in their B2B sales (Yee et al., 2024). This paper proposes a conceptual framework in which the prospecting workflow is reconceived as an autonomous, agentorchestrated pipeline exposed to the operator through a conversational interface. The framework integrates data-enrichment providers and Model Context Protocol (MCP) servers-exemplified by platforms such as Clay, Apollo.io, and ZoomInfo-to identify target accounts, resolve decision-maker contacts, and assemble a multi-dimensional research profile for each prospect. Beyond conventional firmographics, the enrichment schema captures technographic indicators (for instance, whether an account operates HubSpot or Salesforce, or has deployed a particular live-chat technology) and trust-andcompliance signals (for instance, SOC 2 attestation or ISO/IEC 27001 certification). These signals populate a structured research table that conditions a personalization layer, whose output is dispatched and sequenced through platforms such as Instantly or Smartlead. The entire workflow is governed through a chatbot, collapsing a fragmented multi-tool process into a single conversational control plane. Drawing on the AI-and-sales literature and on documented industry practice, the paper articulates the framework's component architecture, situates it against prior work, and discusses implications for throughput, personalization quality, deliverability governance, and the ethics of automated outreach at scale.

---

## uid: `doi:10.2139/ssrn.6979203`

- title: Data Architecture and Governance in the Agentic Era: Paradigm shifts from 2026 Databricks DAIS
- authors: Idilio Moncivais
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6979203
- keyword hits: agentic, ai agent

### abstract

Enterprise data infrastructure has historically separated transactional application stores (OLTP) from analytical systems (OLAP), bridging the two with brittle Change Data Capture (CDC) and Extract-Transform-Load (ETL) pipelines. While functional for humanengineered workflows, this layout has been exposed as a bottleneck by the operational loop speeds of autonomous AI agents. This paper synthesizes the structural breakthroughs announced at the 2026 Databricks Data + AI Summit (June 15-18, 2026, San Francisco) and contextualizes them within the established literature on data architecture, governance, and AI security. We analyze five interconnected paradigm shifts: (1) the unification of transactional and analytical processing under a single Lake Transactional/Analytical Processing (LTAP) architecture built on Lakebase, Lakehouse, and the Reyden engine; (2) the evolution of Unity Catalog from a passive system of record into an active runtime decision-making engine through the Unity AI Gateway, with native Model Context Protocol (MCP) interception and an open cybersecurity ecosystem spanning ten security and four identity partners; (3) the construction of a governed semantic bridge through Unity Catalog Business Semantics and contributions to the Open Semantic Interchange (OSI) initiative; (4) ecosystem openness through the Omnigent meta-harness framework and the contribution of the OpenSharing protocol to the Linux Foundation; and (5) the transition from interactive analytics to autonomous operations through scheduled agent tasks and ZeroOps. The contribution is interpretive: the paper organizes a coherent vendor paradigm around four analytical pillars (Context, Cost, Control, Choice) and maps it against established normative frameworks (NIST AI Risk Management Framework, ISO/IEC 42001, EU AI Act, NIST SP 800-207 Zero Trust Architecture). The paper closes by identifying open challenges, including real-time synchronization limits at scale, compliance alignment across volatile international frameworks, the compute requirements of scaling execution guardrails, and the need for independent empirical evaluation of vendor capability claims.

---

## uid: `doi:10.2139/ssrn.7129019`

- title: Multi-Agent Artificial Intelligence for Autonomous Enterprise Automation
- authors: Parikshit Rohit Pravin Srivastav
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7129019
- keyword hits: agentic, ai agent

### abstract

Today's fast-paced digital transformation has dramatically changed the way that businesses operate, driving an unprecedented need to leverage intelligent automation in cloud computing, enterprise resource planning (ERP), customer relationship management (CRM), DevOps, cybersecurity, business process management and enterprise service management. In the same vein, traditional Artificial Intelligence (AI) and robotic process automation (RPA) have enhanced operational efficiency but have been confined due to their narrow autonomy, isolated use of decision making power and low adaptability in dynamic enterprise settings. Agentic Artificial Intelligence (Agentic AI) and Multi-Agent Artificial Intelligence (MAAI) are groundbreaking developments in enterprise automation, empowering multiple intelligent agents to engage in autonomous thinking, joint problem-solving, distributed AI, adaptive learning, and orchestrating workflows and processes. In this study, Agentic AI and Multi-Agent AI are examined in the context of the systematic literature review (SLR), followed by a comparative analysis of the latest academic and industrial research to explore the changing role of AI in the intelligent enterprise automation. The review summarizes the latest advancements, deployment strategies, architectural designs, advantages, and future challenges of enterprise-wide collaborative AI agent deployment. The results show that Multi-Agent AI significantly boosts enterprise automation, yielding benefits in terms of efficiency, scalability, resilience, resource optimization, and cross-functional coordination. Moreover, Agentic AI provides autonomy for planning, ongoing learning, contextual reasoning, and real-time decision-making in intricate enterprise workflows, and multi-agent orchestration boosts cloud operations, DevOps automation, cybersecurity, business process management and enterprise service delivery. Still, there are serious issues of governance, interoperability, explain ability, trust, cyber security, privacy protection, and ethics in the use of AI that must be addressed on the road to broad implementation. The review also points to the growing reliance on enterprise ecosystems in the future, where collaboration-driven AI agents will play a key role, highlighting the need for secure, transparent and well-governed autonomous architectures that will evolve alongside business ecosystems and business priorities. In conclusion, Multi-Agent AI is the future of intelligent enterprise automation, presenting unprecedented opportunities for organizational transformation, yet it comes with its own set of challenges, including the need for robust governance frameworks, standardized orchestration mechanisms, and responsible use of AI in enterprises, to ensure sustainable, secure, and trustworthy adoption (

---

## uid: `doi:10.2139/ssrn.6971038`

- title: Fully Homomorphic Compression (FHC)
- authors: Mohammad Raeini
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6971038
- keyword hits: llm, llms

### abstract

Compression algorithms and functions have been extensively utilized in various applications, e.g., in digital storage and communication. In recent years and with the popularity of machine learning applications, researchers have utilized compression techniques for addressing key problems in machine learning, e.g., for compressing artificial neural networks or for optimizing KV-cache memory in LLMs. Due to extensive applications of compression algorithms in different domains, a whole new era of innovations and applications for data compression algorithms can be envisioned. In this article, we discuss that compression functions with interesting properties, e.g., fully homomorphic compression (FHC) algorithms, can have applications beyond compressing data. FHC algorithms can potentially enable performing computation on compressed (and encrypted) data. Thus, fully homomorphic compression techniques can be used for reducing the computational and communication costs of compute and communication-intensive workloads, such as fully homomorphic encryption (FHE) & zero-knowledge proof (ZKP) applications, (secure) vector databases (VDBs and SVDBs), blockchain-based technologies, image and video processing, privacy-preserving or private LLMs, and LLM & AI inference, etc.

---

## uid: `doi:10.2139/ssrn.7036119`

- title: From Population Genomics to Biological Intelligence: Governing the Next Strategic Infrastructure
- authors: Ernest Jedrzejewski
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7036119
- keyword hits: foundation model

### abstract

The release of one of the world's largest integrated genomic repositories by the U.S. National Institutes of Health marks a transition in population genomics from large-scale data collection to routine computational analysis. This shift fundamentally changes the governance problem. While discussion has traditionally focused on participant privacy, integrated repositories combining whole-genome sequencing with longitudinal clinical, behavioural and environmental data increasingly enable the creation of biological intelligence through artificial intelligence and emerging biological foundation models. As the inferential reach of genomic repositories extends beyond enrolled participants through kinship and cross-dataset integration, governance can no longer be understood solely in terms of protecting individual records. This Commentary argues that population-scale genomic repositories increasingly exhibit characteristics traditionally associated with strategic scientific infrastructure and proposes a governance framework that shifts from protecting biological data towards governing the creation and stewardship of biological intelligence while preserving scientific openness, privacy, innovation, cybersecurity and long-term societal resilience.

---
