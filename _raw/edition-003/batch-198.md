# Classification batch 198 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-198.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6720039`

- title: The Inference Divide: Tiered AI Subscription Models, Capability Stratification, and the Emergence of a New Form of Technological Inequality
- authors: Yim Cao, Louis Zhao
- affiliations: not stated
- posted: 2026-05-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6720039
- keyword hits: agentic, generative artificial intelligence

### abstract

Access to generative artificial intelligence in 2026 is nominally universal and substantively stratified. Major commercial providers have converged on a four-tier subscription architecture (free, entry at $8–$15/mo, standard at $20/mo, and premium at $100–$250/mo) that distributes qualitatively different AI capabilities across qualitatively different user populations. The premium tier, serving fewer than one million subscribers globally, concentrates agentic capability, extended reasoning, and long-context processing that the free tier (serving billions) does not provide. This Article names this phenomenon the Inference Divide and develops it as a distinctive legal-doctrinal category. Applying K. Sabeel Rahman's three-element infrastructural regulation test (scale, necessity, vulnerability), the Article argues that consumer AI has crossed the threshold into infrastructural status in specified domains. Martha Nussbaum's capabilities approach provides the normative bridge from infrastructural diagnosis to ethical claim. The Article then conducts comparative doctrinal analysis across four jurisdictions (the United States, the European Union, the People's Republic of China, and Hong Kong SAR), identifying a pattern of fragmented coverage. Hong Kong emerges as a revealing instance of layered exclusion at the intersection of U.S. export-control posture, Chinese regulatory influence, and common-law consumer-protection tradition. The Article addresses the most significant empirical challenge to this thesis (the equity-enhancing evidence from Noy and Zhang, Brynjolfsson, Li, and Raymond, and adjacent studies) by showing that scope limitations in the existing evidence leave the Inference Divide argument intact. Part V proposes two interventions calibrated to the post–Loper Bright environment: Mandatory Capability Disclosure anchored in existing consumer-protection doctrine, and Public AI Provisioning through state procurement and capability-floor standards. The post–Loper Bright administrative-law restructuring (Loper Bright, Corner Post, and Jarkesy as a 2024 trifecta) reinforces, rather than undermines, the procurement-route preference of the second proposal.

---

## uid: `doi:10.2139/ssrn.6721323`

- title: ScoutLLM: More than Matching, Analyzing DDoS Attacks with Human Thinking Mode
- authors: jinhao you, Mingzhe Xing, Lei Zhang, Zan Zhou, Shujie Yang, Yong Cui, Changqiao Xu
- affiliations: not stated
- posted: 2026-05-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6721323
- keyword hits: fine-tuning, large language model, llm

### abstract

With the development of artificial intelligence (AI) technology, technologies based on machine learning (ML), deep learning (DL), and transformer architecture have been widely applied to distributed denial of service (DDoS) attack detection. However, they are still difficult to apply to a wide range of diverse business scenarios. The reason is that existing technologies still rely on learning the behavioral patterns of attack traffic for matching, rather than relying on scenario-based business thinking and judgment like human experts. Fortunately, large language model (LLM) have shown amazing performance in simulating human thinking to solve problems due to their excellent reasoning capabilities. Therefore, using LLM to mimic the thinking of human experts to analyze DDoS attack seems feasible. However, applying LLM to this field still faces three specific challenges: complicated input information, unreliable output, and complex analysis tasks. To address these challenges, this paper proposes ScoutLLM, which re-encodes and maps the input information, scores the output based on the Inner activation heads of the model output, and constructs a tree of thought analysis for complex tasks, thereby overcoming the above three challenges. It is worth noting that, compared to other DDoS attack detection schemes, our ScoutLLM only requires initial projection layer training. When switching DDoS scenarios, it does not need to undergo pre-training and fine-tuning to adapt to the new DDoS attack scenario. We conducted experiments on three datasets, and the accuracy was above 98.1% in all cases. It is worth noting that, compared to other DDoS attack detection schemes, our ScoutLLM does not require pre-training and fine-tuning based on DDoS attack traffic to achieve DDoS attack detection in different scenarios.

---

## uid: `doi:10.2139/ssrn.6723679`

- title: MeVe: A Modular System for Memory Verification and Effective Context Control in Language Models
- authors: Andreas Ottem
- affiliations: not stated
- posted: 2026-05-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6723679
- keyword hits: llm, retrieval-augmented

### abstract

Retrieval-Augmented Generation (RAG) systems typically face constraints because of their inherent mechanism: a simple top-k semantic search [1]. The approach often leads to the incorporation of irrelevant or redundant information in the context, degrading performance and efficiency [10][11]. This paper presents MeVe, a novel modular architecture intended for Memory Verification and smart context composition. MeVe rethinks the RAG paradigm by proposing a five-phase modular design that distinctly breaks down the retrieval and context composition process into distinct, auditable, and independently tunable phases: initial retrieval, relevance verification, fallback retrieval, context prioritization, and token budgeting. This architecture enables fine-grained control of what knowledge is made available to an LLM, enabling task-dependent filtering and adaptation. We release a reference implementation of MeVe as a proof of concept and evaluate its performance on knowledge-heavy QA tasks spanning biomedical, legal, Wikipedia, and HotpotQA domains [22] [26] [27]. Our results demonstrate that by actively verifying and refining contextual information, MeVe achieves substantial gains in both accuracy and efficiency: Exact Match improves by around 40%, F1 by 34%, and usable context by over 40% while processing time rises only barely ( 12%). These improvements translate into large reductions in contextual redundancy (up to 57% on Wikipedia and 75% on HotpotQA) and consistent accuracy gains across all evaluated domains. Component ablation further highlights the importance of Hybrid Fallback, Coherence Filtering and Adaptive Verification in sustaining these benefits [25]. This work provides a framework for more scalable and reliable LLM applications. By refining and distilling contextual information, MeVe offers a path toward better grounding and more accurate factual support [16].

---

## uid: `doi:10.2139/ssrn.6632898`

- title: Decision-Driven Software Engineering (DDSE) for AI-Assisted Development -A New SDLC Paradigm
- authors: Mahmudur Rahman Manna
- affiliations: not stated
- posted: 2026-05-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6632898
- keyword hits: generative ai, prompting

### abstract

Modern software development faces unprecedented complexity with distributed teams, AI-assisted coding tools, and increasingly modular architectures. Yet the foundational technical decisions that shape systems are often made implicitly or lost in transient discussions, leading to misalignment and architectural drift. We propose Decision-Driven Software Engineering (DDSE), a new software development life cycle (SDLC) that centers on explicitly capturing, evolving, and operationalizing technical decisions as first-class artifacts. In DDSE, layered Technical Decision Records (TDRs) – including Architectural Decision Records (ADRs), Engineering Decision Records (EDRs), Implementation Decision Records (IDRs), Trade-off Decision Matrices (TDMs), and Major Design Decisions (MDDs) – provide a structured knowledge base of why and how key technical choices are made. We describe how DDSE integrates with AI-assisted development workflows, ensuring that generative AI coding assistants and automation tools work within the guardrails of recorded decisions rather than against them. The DDSE model is iterative and responsive like Agile, but introduces distinct control structures and alignment mechanisms focused on decision management. We position DDSE relative to Agile principles and highlight how explicit decision artifacts improve traceability, crossteam alignment, and architectural governance without reverting to big up-front design. A hypothetical workflow demonstrates DDSE in practice, incorporating emerging tools such as AI-enabled IDE assistants, continuous integration (CI) conformance checks, auto-prompting agents, and decision-aware CI/CD pipelines. We provide practical guidelines and heuristics for adopting DDSE – including roles, lightweight documentation practices, and cultural considerations – and discuss the benefits of reduced architectural drift and improved transparency alongside challenges like potential overhead and required mindset shifts. The paper concludes that DDSE offers a timely framework to harness AI’s power while maintaining technical integrity, positioning it as a candidate for the next evolution of software engineering methodology

---

## uid: `arxiv:2605.18784v2`

- title: The Insurability Frontier of AI Risk: Mapping Threats to Affirmative Coverage, Silent Exposures, and Exclusions
- authors: Alex Leung, Rex Zhang, Ervin Ling, Kentaroh Toyoda, SiewMei Loh
- affiliations: not stated
- posted: 2026-05-06
- source: arXiv
- link: https://arxiv.org/abs/2605.18784v2
- keyword hits: agentic, foundation model

### abstract

The rapid diffusion of agentic AI has created a new coverage problem for commercial insurance: some AI-mediated losses are now affirmatively insured, some create silent-AI exposure under legacy cyber, technology errors-and-omissions (E&O), directors-and-officers (D&O), employment practices liability (EPLI), crime, and media policies, and others are being actively excluded. This paper maps that emerging boundary by coding 55 AI threat classes against 26 insurance products, endorsements, and exclusion regimes using public carrier materials and OWASP/MITRE threat catalogs. We identify a four-tier insurability frontier: affirmatively insured perils, silent-AI exposures, actively excluded perils, and perils outside conventional private insurance structures. Our coding measures publicly claimed positioning rather than executed contract wording; the headline statistics describe what carriers publicly state about coverage, not what would be paid in any specific claim. Three patterns emerge. First, affirmative AI coverage is beginning to differentiate by primary risk emphasis: public materials often position Munich Re around model performance and drift, Armilla and parts of the Lloyd's market around hallucination and broader AI liability, Tokio Marine Kiln and CFC around IP and technology E&O concerns, Apollo ibott around emerging autonomous system liability, and Coalition around deepfake and AI-enabled cyber response. Second, legacy lines retain silent-AI exposure where AI is an instrumentality rather than the legal cause of loss. Third, foundation model concentration is the clearest genuinely novel insurability frontier because upstream model failure can correlate losses across many cedents at once; the relevant market design question is which insurability constraint each candidate structure relaxes, not merely which systemic risk template exists.

---

## uid: `doi:10.2139/ssrn.6728121`

- title: Breaking Down Barriers Assistant: Leveraging AI to Conduct Policy Analyses with Complex Data
- authors: Ujjwal KC, Jan Kabatek
- affiliations: not stated
- posted: 2026-05-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6728121
- keyword hits: generative ai, retrieval-augmented

### abstract

Evidence-based policy design increasingly relies on integrated administrative data, yet access to and effective use of these data remain constrained by technical and institutional barriers. This paper introduces the Breaking Down Barriers Assistant, an AI-powered analytical platform designed to democratise access to complex, linked administrative datasets for policy analysis. The system enables users to query secure, pre-aggregated Australian administrative and survey data using natural language and supports the full policy research cycle through three integrated tools: variable discovery, visual analytics, and automated reporting. Methodologically, the BDB Assistant combines Retrieval-Augmented Generation with controlled code generation and execution, ensuring that all analytical outputs are grounded in verified metadata, auditable Python code, and human-in-the-loop validation. Using benchmark comparisons with established platforms such as YouthView and the BDB Community Profiles, we demonstrate that the Assistant can accurately reproduce complex spatial and longitudinal policy analyses that traditionally require advanced technical expertise. The findings show that the system substantially reduces time-to-insight while maintaining strict standards of accuracy, transparency, and privacy. The BDB Assistant illustrates how responsibly governed generative AI can expand analytical capacity within government and the social sector, supporting more timely, rigorous, and locally targeted evidence-based policymaking.

---

## uid: `doi:10.2139/ssrn.6655539`

- title: Structured Reasoning in LLM Optimization Agents: Scaffolding, Not Regularization
- authors: Kartik Ganapati Bhat
- affiliations: not stated
- posted: 2026-05-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6655539
- keyword hits: chain-of-thought, claude, llm

### abstract

LLM-based optimization agents increasingly produce structured reasoning artifacts-hypothesis summaries, causal models, prediction logs-that persist across iterations. The assumption is that forcing articulation regularizes reasoning, as the self-explanation effect suggests it does for human learners. We test this assumption using SynthOracle, a family of synthetic multi-objective optimization oracles with known causal structure that enables separate measurement of optimization quality and reasoning quality. We pair the benchmark with a verbal regularization (VR) protocol that requires the agent to hypothesize, predict, and reconcile at each iteration via a structured summary embedded in conversation context. Through controlled ablations on two oracles and two models (Claude Opus 4.6 and Sonnet 4.6; n = 5 paired seeds per condition), we find that the forced summary is scaffolding, not regularization: it improves optimization for a less capable model (Sonnet, +26%) and a harder task (12-dimensional with noise, +14% to +35%), but hurts the most capable model on the simplest oracle (Opus,-35%, p = 0.0006). The pattern is consistent across 18 of 20 paired seeds (binomial p = 0.0002). A mechanism-isolation experiment shows that the performance penalty comes from the summary's persistence in conversation context, not from the cognitive cost of producing it: an agent that produces the summary but does not receive it back performs identically to one that never produces it (p = 0.35). We connect this finding to the architectural trend in frontier reasoning models toward ephemeral chain-of-thought traces and derive a design principle: match the rigidity of your reasoning protocol to the gap between model capability and task difficulty.

---

## uid: `doi:10.2139/ssrn.6678078`

- title: Candor and the Algorithm: Deliberative Privilege and the Structural Vulnerability of Judicial AI
- authors: Alexis Austin Litle, JD Morris, Deepankar Das
- affiliations: not stated
- posted: 2026-05-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6678078
- keyword hits: generative ai, retrieval-augmented

### abstract

In fiscal year 2025, the federal judiciary’s 677 district judges confronted 382,692 new filings, an average of 565 per judge, while carrying backlogs of approximately 800 pending matters each. With 40 Article III vacancies and no significant congressional expansion of the federal bench in decades, the structural labor shortage makes artificial intelligence (AI) adoption a practical necessity. A March 2026 Northwestern survey, the first random-sample study of federal judges and AI, found that more than 60 percent of responding judges use at least one AI tool in their judicial work, with 30 percent using AI for legal research. But the consumer AI platforms judges are most likely to use are generative AI systems prone to hallucination at rates between 69 and 88 percent on legal research tasks, and even retrieval-augmented generation (RAG) systems marketed as “hallucination-free” hallucinate between 17 and 33 percent of the time. Meanwhile, consumer platform terms of service authorize vendors to access, retain, and use judicial inputs for model improvement, compromising the deliberative privilege that protects pre-decisional judicial reasoning. This Article argues that the deliberative privilege extends to a judge’s AI research during the decisional process, but that this protection is structurally undermined when judges use personal consumer accounts. It applies the AI Legal Reference Model (ALRM) proposed in a companion article to the judicial context, identifies five doctrinal requirements any confidential judicial AI capability must satisfy under the ALRM, and predicts that the first subpoena to an AI vendor for a judge’s interaction logs is a foreseeable litigation event within eighteen months of publication. It further identifies the doctrinal protection gap: no current federal doctrine shields records of pre-decisional AI-assisted judicial analysis from compelled disclosure, and it proposes three legislative vehicles to close that gap before any institutional judicial AI capability can be safely deployed.

---
