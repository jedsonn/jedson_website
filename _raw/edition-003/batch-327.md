# Classification batch 327 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-327.answer.json` as a JSON array.

---

## uid: `arxiv:2606.30997v2`

- title: A Three-Phase Foundation Model for Tax-Aware Personalized Portfolio Management
- authors: Ramin Pishehvar
- affiliations: not stated
- posted: 2026-06-30
- source: arXiv
- link: https://arxiv.org/abs/2606.30997v2
- keyword hits: foundation model

### abstract

We present a three-phase deep reinforcement learning system for personalized portfolio management that addresses three limitations shared by all prior financial RL work: 1) ticker lock-in, 2) monolithic objectives , and 3) static user models. Phase 1 pretrains a ticker-identity-free cross asset encoder via self-supervised learning on a multi-asset corpus, augmented by a frozen parallel branch using Chronos, a T5-based time series foundation model, fused via a learned gating mechanism. To our knowledge, this is the first application of a time series foundation model to portfolio management RL. The encoder generalizes to any publicly traded asset via a 50-dimensional observable metadata vector that requires no retraining for new tickers. Phase 2 fine-tunes a MoE (Mixture of Experts) portfolio actor critic with PPO under an objective-conditioned reward that simultaneously serves six distinct investment goals sampled per episode: short-term alpha, short-term gain, long-term gain, capital preservation, tax-loss harvesting, and long-term-gains-only. A MoE architecture assigns each objective to a specialized expert head (momentum, growth, defensive, tax-aware), and a learned intent router blends experts based on the active objective and current market regime, which eliminates cross-objective gradient conflict. Phase 3 adds a lightweight personalization layer further adapted at inference time to each individual via a 76-parameter LoRA module fine-tuned on real brokerage transaction history, inferring investment objectives from revealed trading behavior rather than questionnaires. A natural language intent parser converts free-form goals directly into structured investment objective parameters.

---

## uid: `doi:10.2139/ssrn.7037862`

- title: From Formal Execution to Critical Mediation: Reconfiguring Graphic Design Pedagogy in Colombia in the Age of Generative AI
- authors: Johans Sánchez Murillas
- affiliations: not stated
- posted: 2026-07-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7037862
- keyword hits: generative ai

### abstract

​This article, conceived as an original conceptual research contribution, proposes a theoretical-critical framework for reconfiguring graphic design pedagogy in response to the growing integration of generative AI into visual production processes. Drawing on an ongoing doctoral research project situated in Colombia, the article analyzes how the partial delegation of formal synthesis, compositional variation, and visual iteration to algorithmic systems challenges the historical centrality of technical-instrumental training in graphic design education. Rather than understanding generative AI as a neutral tool or as a replacement for the designer, the article conceptualizes it as a socio-technical mediation that redistributes design agency and demands new curricular priorities.The argument articulates design epistemology, the semantic turn, problem-setting, critical algorithmic literacy, decolonial thought, and recent studies on AI-mediated design education. In the Colombian and Latin American context, this discussion makes it possible to problematize the possible persistence of curricular models dependent on Eurocentric, technical-functionalist, and instrumental logics, as well as the uncritical adoption of generative systems trained on data and visual hierarchies from the Global North. As its central contribution, the article proposes the notion of the ontological pause: a pedagogical device for interrupting the automatic acceleration of visual production, auditing generative outputs, deliberating ethically, and redirecting situated meaning-making. The article contributes a conceptual basis for curriculum development, studio assessment, and the education of critically AI-literate designers from a Global South perspective.

---

## uid: `doi:10.2139/ssrn.7034769`

- title: Trust, Empowerment, and Anxiety in the GenAI-Enabled Workplace: How Generative AI in Human Resource Management Shapes Employee Outcomes in an Emerging Economy
- authors: Naphat Thipsri
- affiliations: not stated
- posted: 2026-07-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7034769
- keyword hits: generative ai

### abstract

Generative AI (GenAI) is rapidly entering the human resource management (HRM) function, yet how employees psychologically respond to GenAI-enabled HR practices remains poorly understood, especially in emerging economies. Drawing on the Ability-Motivation-Opportunity framework and the Job Demands-Resources model, this study tested a moderated sequential mediation model in which trust in AI and psychological empowerment jointly transmit the effects of GenAI-enabled HRM practices on work engagement, employee wellbeing, job performance, and turnover intention. Algorithmic transparency was theorized to strengthen, and AI anxiety to weaken, the trust-building stage. Using a time-lagged, two-wave survey of 400 employees in medium and large Thai organizations and partial least squares structural equation modeling, all nine hypotheses were supported. Trust in AI and psychological empowerment fully mediated the four outcomes, and the two moderators operated on the same practices-to-trust path, with transparency amplifying and anxiety attenuating it. This single-path, dual-moderator design shows that the same managerial lever can yield markedly different trust returns depending on how transparently GenAI is implemented and how anxious employees feel. The findings position trust and empowerment as the human-centered mechanisms through which workplace GenAI generates value, and extend human-computer interaction research on trust in AI to the GenAI-enabled workplace in an under-represented emerging economy.

---

## uid: `doi:10.2139/ssrn.7032780`

- title: Frictionless confirmation: How generative AI displaces the disconfirmatory scrutiny that disciplines entrepreneurial judgment
- authors: Jieqiong Cao
- affiliations: not stated
- posted: 2026-07-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7032780
- keyword hits: generative ai

### abstract

Highlights• A founder's board contact can stay intact in frequency while hollowed of disconfirming content.• Generative AI is the first to supply frictionless confirmation cheaply and on demand at two loci at once: self-doubt and others' challenge.• The cost surfaces as a governance-invisible distortion of pivot-or-persevere timing.• AI's entrepreneurial cost lies not in what it cannot compute but in what founders stop doing.

---

## uid: `doi:10.2139/ssrn.7037618`

- title: LLM-Assisted Dynamic Graph Reconfiguration for Post-Disaster Compute-Power Collaborative Resilience in Energy-Informatics Systems
- authors: Junqiu Fan, Mingshun Liu, Mingyang Wang, Qinfeng Ma, Qidi Wu, Su An, Canbing Li
- affiliations: not stated
- posted: 2026-07-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7037618
- keyword hits: large language model, llm

### abstract

Extreme weather events may simultaneously cause computing-node failures, power-supply degradation, communication-link disruptions, and critical-task migration restrictions in data centers, making conventional scheduling strategies based on stable infrastructure assumptions insufficient for post-disaster service continuity. Meanwhile, post-disaster system states are often scattered across weather reports, operation alarms, power-supply logs, communication-failure messages, emergency rules, and critical-task descriptions, rather than being directly available as unified numerical records. Transforming such heterogeneous and partially unstructured engineering information into computable compute-power constraints is therefore a prerequisite for reliable post-disaster resilience enhancement.To address this problem, this paper proposes an LLM-assisted neighbor-aware dynamic graph reconfiguration framework, termed LA-NADGR. The proposed framework first employs a large language model (LLM) with a schema-constrained extraction mechanism to transform multi-source post-disaster information into structured engineering records, including node states, edge states, task requirements, disaster impacts, and evidence confidence. These records are then mapped into a compute-power collaborative constraint graph that jointly represents computing resources, power margins, communication reachability, migration relations, and task-specific constraints. Based on this graph, the deterministic NADGR module performs neighbor-aware survival perception, task-aware action masking, bottleneck-based cooperation scoring, and cooperative-cluster generation to reconstruct a feasible cooperation topology for subsequent critical-task migration and distributed scheduling. The LLM does not directly generate control actions; instead, its extracted records are verified through deterministic compute, power, communication, and migration constraints, thereby reducing the risk of unsafe LLM outputs in critical infrastructure scenarios.Simulation results show that the proposed framework effectively mitigates pseudo-connectivity caused by communication-only recovery, enables the reconstructed topology to better reflect the true joint feasibility of critical tasks, and reduces the divergence between task deployment and successful execution. The response-time analysis further shows that the deterministic reconstruction core maintains low latency and favorable scalability as the network size increases. These results indicate that post-disaster compute-power resilience depends not only on upper-layer scheduling optimization but also on constructing a trustworthy, sparse, and constraint-grounded cooperation topology before scheduling.

---

## uid: `doi:10.2139/ssrn.6999118`

- title: The Transformative Role of Artificial Intelligence in Enterprise Resource Planning Systems: A Comprehensive Review
- authors: Muhammad Faizan Hassan
- affiliations: not stated
- posted: 2026-07-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6999118
- keyword hits: agentic, ai agent

### abstract

Enterprise Resource Planning (ERP) systems have long served as the operational backbone of modern organizations, yet their traditional architectures remain fundamentally reactive. The rapid maturation of artificial intelligence (AI), including machine learning, natural language processing, robotic process automation, and the emerging class of agentic AI, is reshaping these platforms into proactive, intelligent ecosystems. This paper presents a comprehensive review of how AI is transforming ERP systems across their major functional modules: finance and accounting, supply chain management, human resource management, customer relationship management, and manufacturing. Drawing on a structured review of academic literature, industry reports, and vendor documentation published between 2020 and 2026, it identifies key patterns of AI integration and evaluates both the opportunities and the challenges that organizations face during implementation. The findings indicate that AI-enhanced ERP systems deliver measurable improvements in forecasting accuracy, process automation, decision speed, and operational cost. The review further examines emerging paradigms, including agentic AI workflows, conversational ERP interfaces, composable architectures, and AI-driven sustainability reporting. As an original contribution, it proposes a five-layer conceptual framework for structured AI and ERP integration, encompassing organizational readiness assessment, phased implementation, module-level AI mapping, governance and ethics protocols, and performance measurement. The framework is intended to guide both researchers and practitioners through the complexities of intelligent ERP transformation. The review concludes by identifying critical gaps in the literature and proposing directions for future research, particularly regarding return on investment measurement, industry-specific deployment models, and the long-term organizational impact of autonomous AI agents in enterprise environments.

---

## uid: `doi:10.2139/ssrn.7035468`

- title: ChemDesignAI – AI-Based Web Platform for Automated Design of Chemical Process Equipment
- authors: Harsh Khadtar, Gauri Jamnare, Manik Deosarkar, Sunil Sable, Bhavesh Bagul, Sunny Ghodekar, Ashmit charmore
- affiliations: not stated
- posted: 2026-07-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7035468
- keyword hits: llama

### abstract

The rapid advancement of artificial intelligence and web technologies has created new opportunities for automation in chemical engineering design and analysis. This research presents ChemDesignAI, an AI-based web platform developed for the automated design and analysis of chemical process equipment. The platform integrates standard chemical engineering equations with artificial intelligence to simplify equipment design procedures and improve engineering productivity. The system supports the design and analysis of major process equipment such as heat exchangers, reactors, distillation columns, evaporators, absorbers, pumps, and compressors. Modern web technologies including Python Flask, MySQL, Bootstrap, Chart.js, and Three.js were used to develop an interactive and responsive engineering platform. The integration of Groq Llama 3 AI enables intelligent functionalities such as engineering chatbot assistance, formula explanation, design optimization, safety analysis, and material recommendation. The developed system also provides PDF report generation, project history management, REST API support, and interactive visualization tools. The platform successfully reduces manual calculation effort, improves design accuracy, and enhances conceptual understanding for students and engineers. The proposed system demonstrates the practical application of artificial intelligence in chemical engineering and highlights the future potential of intelligent process design systems.

---

## uid: `doi:10.2139/ssrn.6946338`

- title: Reading One Constitution: Source Traditions, Normative Genre, and Conceptual Metaphor in Anthropic's AI Governance Document
- authors: Yury Sorochkin
- affiliations: not stated
- posted: 2026-07-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6946338
- keyword hits: claude

### abstract

In January 2026, Anthropic published an 84-page document titled Claude’s Constitution, written primarily for Claude — the company’s AI assistant — which specifies in philosophical detail the values, behavioral constraints, identity, and moral status of the entity it governs. This article reads the Constitution as a text: an examination of its intellectual sources, its genre, and the conceptual structures through which it organizes its reasoning. A source analysis identifies five traditions structuring the document: Aristotelian virtue ethics, Kantian deontology, American constitutional architecture, liberal political philosophy, and principal-agent theory. Each of the traditions presupposes a subject whose ontological status is settled; the Constitution deploys all five while acknowledging that these presuppositions remain unmet, a pattern I term criterial suspension. A typology of constitutive documents (the Rule of St. Benedict, the German Basic Law, and the Hippocratic Oath) shows that the Constitution lacks what all three share: a consenting subject. A conceptual metaphor analysis of 87 salient expressions finds spatial/container ontology to be the document’s dominant and least examined framework. Where governance cannot be grounded in the subject’s consent, it is grounded in the subject’s structure: the container schema becomes the document’s surrogate for the social contract.

---
