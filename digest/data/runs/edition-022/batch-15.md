# Classification batch 15 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-15.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7323999`

- title: Domain-Specialized Language Models for Core Medical Reasoning:Structural Refinement and Fine-tuning
- authors: Neel Khairnar, Vedant Jadhav, Bharat Kale
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7323999
- keyword hits: fine-tuning, llama, mistral, qwen

### abstract

Background and Objectives: Medical language models are evaluated primarily on benchmark ac-curacy, yet clinical deployment requires structural properties beyond correctness: machine-readableoutput formats, calibrated confidence, and verifiable evidence grounding. This study introducesthe structural alignment gap — the tension between domain knowledge gains and degradation indeployment-critical reliability — and proposes a formal framework to measure it.Methods: Four 7B–8B parameter models (Llama-3.1-8B, Qwen-2.5-7B, Med42-v2-8B,BioMistral-7B) were evaluated on 6,000 questions from MedMCQA, MedQA-USMLE, and Pub-MedQA using a five-metric framework measuring accuracy, JSON format fidelity, hallucination risk,reasoning depth, and citation fidelity. A composite Structural Alignment Index (SAI) was definedas the multiplicative product of format fidelity, inverse hallucination risk, and evidence grounding.Targeted LoRA fine-tuning (rank 16) was applied post-hoc to test structural correctability.Results: Specialist models achieved higher accuracy (Med42-v2-8B: 65.5% on MedQA-USMLE,7.7% above baseline) but lower SAI (35.6) than generalist models (Qwen-2.5-7B: 39.7; Llama-3.1-8B:39.1), due to overconfidence and weaker citation fidelity. After LoRA fine-tuning on fewer than 2,000examples, Med42-v2-8B citation fidelity increased from 58.7% to 98.5%, hallucination risk decreasedfrom 35.9% to 18.4%, and SAI rose to 68.2. All interventions completed within 15 seconds on an AMDMI300X GPU.Conclusions: Benchmark accuracy alone is insufficient to assess clinical deployment readiness.The SAI framework reveals structural gaps invisible to accuracy-only evaluation. These deficits areattributable to training procedures rather than model architecture and are correctable via lightweighttargeted alignment.

---

## uid: `doi:10.2139/ssrn.7323943`

- title: SEMAD: Semantic-Enhanced Malicious Package Detection Using LLMs and Prompt Engineering
- authors: Tuyet  A. Dang-Thi, Hoang-Ly Nguyen, Thanh  M. Truong-Le, Duc-Ly Vu
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7323943
- keyword hits: llm, llms, prompt engineering

### abstract

Context: The proliferation of malicious packages in open-source ecosystems, particularly npm, threatens software supply chains. While current detection focuses on binary classification (malicious vs. benign), the sequential stages of supply chain attack chains remain largely unexplored. Mapping this operational sequence helps software engineers conceptualize and communicate how exploits unfold.Objectives: We introduce SEMAD, an automated approach that reconstructs behavioral attack chains in malicious npm packages to evaluate supply chain threats beyond isolated binary classification indicators.Methods: SEMAD employs a hierarchical hybrid framework combining deterministic static program analysis with LLM semantic reasoning. A rule-based structural layer merges metadata heuristics with AST-based static taint tracking, followed by semantic inference to interpret intent. To mitigate false alarms, a multi-perspective verification stage applies behavioral-chain analysis and contextual legitimacy checks.Results: Evaluated on 246 npm packages (142 malicious, 104 benign) from MalnpmDB, SEMAD’s verification layer reconstructed complete, causally coherent attack chains for 98% of confirmed malicious packages (mean coherence score: 0.73). The end-to-end pipeline achieved a precision of 1.000 and a recall of 0.756 (F1 = 0.861). The initial structural triage stage alone filtered 42.3% of benign packages with zero false positives.Conclusion: Integrating deterministic static filters with semantic reasoning provides an interpretable, reliable, and reproducible paradigm for software supply chain defense, delivering actionable security insights for development teams.

---

## uid: `doi:10.2139/ssrn.7319678`

- title: Learning from Use: Test-Time Learning in Large Language Models and Agents
- authors: Weihao Xuan, Qingcheng Zeng, Jiarui Liu, Rui Yang, Yunze Xiao, Yinxi Li, Zeqi Zhou, Weiwei Sun
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7319678
- keyword hits: agentic, large language model, large language models

### abstract

Models are no longer merely trained and then used, but generate experience during use from which future behavior should improve. A deployed assistant may learn user preferences, a coding agent may encounter recurring repository conventions, and an interactive agentic system may receive corrections, tool outcomes, or environmental feedback. The question is therefore not only how to train a capable model, but how a model should keep, update, and reuse what happens during use. We use test-time learning (TTL) to describe a deployment-time learning paradigm that complements pre-training and post-training. TTL occurs when experience encountered during use updates adaptive state that causally shapes a subsequent decision, forming a deployment-time write-read loop. This formulation provides a unifying lens for a fragmented body of work on memory, adaptation, model editing, and self-evolving agents. We formalize the loop and organize qualifying forms of TTL into context-level, representation-level, and parameter-level TTL, according to where adaptive state re-enters the system. This taxonomy makes lines of work that grew up in separate communities comparable as variants of the same problem: how to turn use into durable learning. We close by reviewing how the causal contribution of learned state should be evaluated, how learning accumulates and remains stable over time, and the challenges facing trustworthy learning during deployment.

---

## uid: `doi:10.2139/ssrn.7324978`

- title: Measuring the Citation Gap: Retrieval Eligibility and Extraction Readiness on Small and Mid-Sized Business Websites Across Four Countries
- authors: Vikas K
- affiliations: not stated
- posted: 2026-08-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7324978
- keyword hits: agentic, llm, llms

### abstract

Retrieval-grounded generative systems can retrieve web sources and use them to construct answers, including answers that expose source citations. Existing measurement of web quality addresses the rendered document — accessibility audits execute JavaScript, structured-data surveys sample crawler corpora, and consent studies examine robots.txt in isolation. None measures what a retrieval client actually receives when it requests an ordinary business homepage and is not a browser. This paper specifies a protocol for that measurement and applies it to 428 small and mid-sized business websites across four countries and four sectors. Each domain is requested under up to four conditions with every attempt recorded, so refusals are reported rather than converted into missing data, and seven binary preconditions are observed with the supplying observer recorded per value. We then define the Citation Gap operationally as the set of sites that satisfy the access preconditions — reachable, permitted, indexable — but do not satisfy all four extraction-readiness preconditions specified by the protocol. Of 349 access-eligible sites, 187 (53.6%) fall below that threshold. Its structure is unexpectedly shallow: 114 of the 187 fail exactly one extraction precondition, most often a top-level heading (45 sites), structured data (38), or a meta description (31), and none fails solely on non-JavaScript content. Adoption of llms.txt, the convention introduced for this purpose, is 20% overall and is associated with sites already outside the gap (29% versus 14%). Blocking of AI crawlers in robots.txt is rare (13 of 382 measurable sites); the observed access failures occur instead at the network edge. An independent local implementation of Google's agentic accessibility-tree audit agrees with it on 55% of sites, so that measure is reported as implementation-specific. The sample is designed to exercise the protocol across heterogeneous business websites, not to estimate population prevalence. No engine behaviour is observed and no causal claim is made.

---

## uid: `doi:10.2139/ssrn.7290180`

- title: AI and Ethics: Reality or Oxymoron?
- authors: Jean Kuhn Keyser
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7290180
- keyword hits: large language model, large language models

### abstract

Contemporary debates on Artificial Intelligence (AI) ethics generally proceed as though AI already exists as an autonomous moral subject. In this article the author questions this assumption, arguing that the philosophical underpinnings of AI ethics remain conceptually unstable. Employing linguistic philosophy, critical self-reflection, and Adorno's negative dialectics, the paper examines the historical development of AI as a concept alongside contemporary ethical and regulatory frameworks. It argues that current policy dialogue frequently conflates advanced machine learning systems with Artificial Intelligence in its stronger philosophical sense, thereby attributing capacities such as reasoning, autonomy, and moral agency that have not yet been demonstrated. Applying narrative analysis, the article traces competing conceptions of AI through the Turing Test, machine ethics, functionalist and standard theories of moral agency, and contemporary debates surrounding explainability, black-box systems, and large language models. It further analyses international policy frameworks, particularly UNESCO's Recommendation on the Ethics of Artificial Intelligence, to demonstrate how conceptual ambiguity generates inconsistencies in ethical governance and legal accountability. Rather than rejecting AI ethics, the paper contends that greater conceptual precision is needed if ethical and legal frameworks are to remain coherent. The paper concludes by proposing a return to a clearer philosophical vocabulary that distinguishes Artificial Intelligence from machine learning, computational ethics, and machine ethics. Such distinctions provide a stronger foundation for future ethical inquiry while leaving open the possibility that genuinely autonomous artificial moral agents may emerge in the future. Until then, philosophical clarity remains a prerequisite for responsible governance of rapidly evolving intelligent technologies.

---

## uid: `doi:10.2139/ssrn.7289632`

- title: Adaptive Weather-Aware Home Energy Management through Large Language Model-Based Appliance Scheduling
- authors: sokipriala jonah, Queen Moses, Abiola Babatunde, Michael Ajao-Olarinoye, Daniel Bammeke
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7289632
- keyword hits: large language model, llm

### abstract

Residential flexibility can reduce electricity costs, increase local photovoltaic (PV) utilisation, and support demand-side operation, but conventional Home Energy Management Systems often require users to translate everyday preferences into technical constraints. This paper presents an adaptive, weather-aware energy-management agent that converts natural-language requirements into coordinated schedules for multiple flexible household loads. To our knowledge, it is the first autonomous LLM-based HEMS to jointly optimise appliance schedules using dynamic retail prices, weather-derived PV forecasts, household demand, self-consumption, export revenue, calendar deadlines, and household power limits within a unified net-cost objective.Five language-model controllers are evaluated against an extended mixed-integer linear programming oracle across tariff-volatility and weather regimes, forecast uncertainty, constraint conflicts, and a seven-day rolling deployment. Results show reliable multi-appliance coordination and near-optimal operating cost under dynamic tariffs. Constraint-conflict testing reveals model-specific failures under deadlines, power caps, irregular schedules, and infeasible requests, demonstrating that economic performance alone is insufficient for evaluating autonomous energy controllers.Weather-aware scheduling provides regime-dependent cost and PV self-consumption benefits by coordinating flexible demand with forecast generation. Across the seven-day evaluation, the agents capture 96.7–98.0% of the savings available between an off-peak timer and the optimisation oracle, while outperforming immediate-start and greedy policies. The findings demonstrate the potential of LLM-based residential energy control while highlighting the need for an independent deterministic feasibility layer before physical actuation.

---

## uid: `doi:10.2139/ssrn.7291663`

- title: Combining Case-Based Reasoning and Open AI Language Models for Experience-Driven Artificial Intelligence
- authors: Thacha Lawanna
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7291663
- keyword hits: large language model, large language models, llm

### abstract

Integrating Case-Based Reasoning (CBR) with large language models provides a promising foundation for artificial intelligence systems capable of learning from and adapting previous problem-solving experiences. This study proposes an experience-driven CBR–OpenAI framework combining the Retrieve–Reuse–Revise–Retain cycle with semantic understanding and generative reasoning. Publicly available CaseHOLD and CUAD datasets were adopted to support evaluation using realistic cases. The framework retrieves relevant historical experiences, adapts previous solutions to new contexts, evaluates generated responses, and retains validated outcomes for future reasoning. Performance was assessed through retrieval accuracy, solution accuracy, contextual relevance, solution adaptability, explainability, experience reuse effectiveness, and response consistency. The proposed framework demonstrated consistently strong results, achieving 94.5% retrieval accuracy, 95.1% solution accuracy, 96.0% contextual relevance, 96.4% solution adaptability, 96.2% explainability, 95.7% experience reuse effectiveness, and a best value of 96.6% for response consistency, with an overall effectiveness of 95.8%. Comparative and ablation analyses further demonstrated the complementary contributions of case retrieval, LLM-supported adaptation, revision, and experience retention. These findings indicate that combining explicit experiential memory with language-model reasoning can provide a balanced foundation for adaptive, explainable, context-aware, and continuously evolving artificial intelligence systems.

---

## uid: `arxiv:2608.15424v1`

- title: ETHOS: Towards a Modular Ethics Framework for Clinical Multi-Agent Systems
- authors: Rakesh Sharma, Sydney Pugh, Cameron Beeche, Pankhuri Singhal, Rachel Wu, Margaret Eby, Jeffrey Duda, James Gee
- affiliations: not stated
- posted: 2026-08-15
- source: arXiv
- link: https://arxiv.org/abs/2608.15424v1
- keyword hits: large language model, large language models

### abstract

The rapid adoption of large language models has enabled the development of clinical multi-agent systems (MAS) capable of integrating multimodal patient data and supporting increasingly complex clinical decision-making. However, the deployment of these systems in real-world healthcare settings raises critical ethical concerns related to safety, fairness, accountability, transparency, and patient trust. While numerous organizations, including the World Health Organization, the National Academy of Medicine, and the FUTURE-AI consortium, have proposed ethical frameworks and governance principles for healthcare AI, these efforts remain largely conceptual. To address this challenge, we present ETHOS (Ethics and Trust through Hierarchical Oversight System), a modular ethics framework designed as a governance meta-agent that can be integrated with any existing multi-agent system without requiring changes to its underlying architecture. ETHOS translates stakeholder-informed ethical requirements into executable runtime oversight through a layered governance approach consisting of deterministic checks, contextual reviews, and a final ethics critic. These components continuously evaluate intermediate reasoning steps and final outputs, enabling the system to identify ethical risks, request revisions, or suppress responses that fail predefined safety and trustworthiness criteria. We demonstrate ETHOS within a hepatology clinical decision-support MAS. Results show that ETHOS improves decision reliability by detecting incomplete, inconsistent, or out-of-scope evidence and appropriately increasing abstention when safe recommendations cannot be supported. By embedding ethical governance directly into system operation, ETHOS provides a practical and auditable mechanism for transforming high-level AI ethics principles into deployable safeguards.

---
