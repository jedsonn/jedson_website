# Classification batch 209 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-209.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6988699`

- title: Towards Empowering the Offline Clinician: A Method for Enhancing Dermatology Reference Material Utility through Mobile Edge AI-Based Retrieval-Augmented Generation
- authors: Maged  N. Kamel Boulos, Mohammed Ali Chherawalla
- affiliations: not stated
- posted: 2026-06-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6988699
- keyword hits: qwen, retrieval-augmented

### abstract

Background: In 2024, we demonstrated the feasibility of using retrieval-augmented generation (RAG) on local laptops to create intelligent personal clinical tutors for dermatology education. However, the rapidly evolving capabilities of mobile hardware now allow for similar localised deployments on smartphones. Objective: This study investigates the feasibility of replicating a local, offline RAG system on a contemporary midrange smartphone to provide a highly portable and secure clinical dermatology educational tool for clinicians and students. Methodology: Using a Redmi Note 15 5G (12 GB RAM, Snapdragon 6 Gen 3 processor), we deployed the 'Off Grid-Private AI Chat' app (Android). A 4-billion parameter model, Qwen 3.5 4B (Vision), was loaded on-device. A compressed PDF of a 234-page dermatology textbook was indexed into a local RAG knowledge base. All operations model execution, indexing, and query processing-were executed natively and exclusively within the app without network connectivity. Results: The system successfully generated accurate, contextually relevant answers derived from the textbook. The model listed specific source text chunks used for each response, allowing for easy verification. Comparative analysis revealed that the RAG-enabled system prevented critical clinical inaccuracies observed in unconstrained Qwen 3.5 4B output by strictly grounding generation in the verified knowledge base. We provide technical guidance to facilitate high-performance execution on mid-range and flagship smartphones. Conclusion: The experiment confirms that mid-range mobile hardware is now sufficiently advanced to support localised, offline AI dermatology tutoring. This democratises access to sophisticated study aids while maintaining absolute data privacy, copyright protection, and offline flexibility.

---

## uid: `arxiv:2606.29793v2`

- title: Fund2Persona: A Framework for Building and Refining Financial Advisor Personas from Fund Disclosure Data
- authors: Suhwan Park, Hoyoung Lee, Zhangyang Wang, Alejandro Lopez-Lira, Young Cha, Chanyeol Choi, Jaewon Choi, Yongjae Lee
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.29793v2
- keyword hits: agentic, llm

### abstract

Demand for personalized financial advising is growing, but consistent advisor expertise is difficult to obtain, scale, and encode in LLM systems. Simple persona prompts rarely specify how a financial advisor should reason and often drift toward generic recommendations. We propose Fund2Persona, a framework that grounds financial-advisor personas in fund disclosures, holdings transitions, market context, and manager commentary, then refines them through an agentic actor--scorer--patcher loop. We evaluate the resulting personas on held-out holdings-transition reconstruction and manager-commentary alignment, where they better recover portfolio decisions and grounded manager interpretation than generic baselines. We further study two downstream diagnostics: market-scenario generation, where persona retrieval broadens plausible investment views beyond repeated generic rollouts, and advisory dialogues grounded in investor profiles, where matched personas give more specific and useful advice than a generic advisor. These results suggest that fund-data-grounded financial-advisor personas can make manager-specific investment expertise portable rather than merely changing an LLM's surface style.

---

## uid: `arxiv:2606.30801v1`

- title: Using AI Agents to Automate Black-Box Audits of Personalization Algorithms at Scale
- authors: Alessandro Morosini, Sarah H. Cen, Andrew Ilyas, Hedi Driss, Aleksander Mądry, Chara Podimata
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.30801v1
- keyword hits: ai agent, generative ai

### abstract

Personalization algorithms determine what content users encounter on online platforms. Auditing these systems is difficult because independent auditors have only black-box access to the algorithms, while personalization depends on users' attributes, behavior, and evolving interaction histories. Existing auditing methods face a tradeoff: studies with real users capture realistic behavior but are costly and hard to control, whereas sock-puppet audits scale more easily but often rely on scripted behavior that limits realism. Beyond this, both approaches struggle to decouple user attributes from user behavior, limiting our ability to causally understand personalization. To address this gap, we introduce a framework for black-box audits of personalization algorithms using generative AI agents as behavioral engines for synthetic accounts. Each agent is instantiated with a fixed persona, grounded in demographic and political survey data, and interacts with a platform's content by reasoning about it and choosing actions. Because behavior is fixed within each persona while platform-visible signals such as age, gender, or location can be experimentally perturbed, our design enables counterfactual auditing of how platforms respond to user attributes. As a case study, we deploy 1,120 agents on X shortly after the 2024 U.S. election, spanning 14 personas and three counterfactual conditions, collecting over 200,000 content exposures. We find that X's algorithmic feed amplifies toxic, polarizing, political, and right-leaning content relative to the chronological feed, with amplification varying sharply by user ideology. Counterfactual analyses show that demographic signals affect content delivery in persona-dependent ways: pooled effects are largely null, while subgroup-level effects vary in direction and magnitude. Our work establishes GenAI-based agents as a new tool for algorithmic auditing.

---

## uid: `arxiv:2606.30190v1`

- title: Few-Shot Domain Incremental Learning via Continual Vision-Language Consolidation
- authors: Naeem Paeedeh, Mahardhika Pratama, Wolfgang Mayer, Mukesh Prasad, Weiping Ding, Yew-Soon Ong
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.30190v1
- keyword hits: fine-tuning, llm, llms

### abstract

Existing domain-incremental learning (DIL) strategies call for massive amounts of data to adapt to new domains and suffer from the overfitting problem in the case of data scarcity. This paper puts forward a relatively uncharted problem, namely, few-shot domain incremental learning (FSDIL), taking into account the problem of extreme data shortages in the realm of DIL. A novel algorithm, namely Continual Vision-Language Consolidation (CVLC), is proposed to address the FSDIL problem, where the key idea lies in the concept of latent space reservation in the base domain coupled with dual coalescent projection (DCP) as a parameter-efficient fine-tuning method. First, the vision prototype is calibrated while multiple templates and synonyms are generated via LLMs to induce the language prototype. The vision and language prototypes are fused. Adaptation to never-ending arrivals of new domains is done by the DCP technique, fine-tuned in such a way to prepare the model to unseen domains via latent-space reservations committed in the base domain. CVLC is structured under shared and domain-specific components to combine general knowledge and domain-specific details. The advantage of our approach is demonstrated through a range of benchmark problems and comparisons with prior arts, in which CVLC outperforms them by up to a 16% gap. Our codes are shared publicly in https://github.com/Naeem-Paeedeh/CVLC .

---

## uid: `arxiv:2606.29863v1`

- title: KbSD: Knowledge Boundary aware Self-Distillation for Behavioral Calibration in Agentic Search
- authors: Tao Feng, Xinke Jiang, Chao Wu
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.29863v1
- keyword hits: agentic, large language model, large language models

### abstract

Agentic search equips large language models with dynamic retrieval abilities, but existing reinforcement learning methods remain limited by reward sparsity in knowledge boundary calibration -- deciding when to trust parametric memory, when to rely on retrieved evidence, and when to abstain. Binary rewards can penalize undesirable outcomes, but provide little guidance on the reasoning process required to make calibrated decisions across different knowledge states. To address this, we propose KbSD (Knowledge boundary Self-Distillation), a framework that tackles this limitation through dense token-level supervision, outcome-level sparse rewards, and quadrant-adaptive optimization. KbSD constructs a hint-augmented teacher, architecturally identical to the student, that receives explicit knowledge boundary signals -- including parametric certainty, retrieval quality, and ground-truth answers -- to generate calibrated reasoning demonstrations. This information-asymmetric self-distillation enables dense supervision without requiring a larger external model. To further account for the heterogeneous reasoning distributions across knowledge states, we introduce a quadrant-adaptive distillation objective: reverse KL for concentrated integration, forward KL for diverse refusal, and Pareto-optimal bidirectional KL for asymmetric quadrants requiring both precision and coverage. Experiments on multiple benchmarks show that KbSD consistently improves both task accuracy and hallucination mitigation over strong baselines, with the largest gains appearing in the challenging quadrants where sparse rewards are least informative.

---

## uid: `doi:10.2139/ssrn.6900243`

- title: Are we Better Off Interacting with Humans or AI in Conflict and Coordination Settings? *
- authors: Richard Li, Bradley J. Ruffle, Fei Song
- affiliations: not stated
- posted: 2026-06-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6900243
- keyword hits: ai agent, llm

### abstract

As artificial intelligence (AI) increasingly acts autonomously in economic and social environments, understanding how humans and AI interact strategically has become a central scientific and societal question. We report controlled experimental evidence on how humans and autonomous AI agents behave toward one another in repeated conflict and coordination settings. Unlike prior work using pre-programmed strategies or hypothetical judgments, we embed autonomous LLM agents directly into an incentivized laboratory experiment as strategic decision-makers interacting with both humans and other AI agents. Thus, AI agents in our study independently interpreted instructions, formed expectations, made gameplay decisions, generated round-by-round reasoning for their decisions and adapted dynamically to feedback. Specifically, humans and AI agents play either a 40-round repeated Prisoner's Dilemma or Battle of the Sexes, 20 rounds against each counterpart type. We elicit both humans' and AI's earnings beliefs before and after an initial 20-round block of play against each counterpart type, and observe dynamic behavior across human-human, human-AI, and AI-AI dyads under identical laboratory conditions. Humans show no strong ex ante preference between human and AI counterparts, but exhibit more reciprocity, cooperation and accommodation toward fellow humans. In contrast, AI agents display a systematic in-group bias toward AI. AI's thought processes highlight its aim to maximize joint payoffs, establish mutual cooperation and achieve coordination. Consequently, AI-AI pairs achieve the highest payoffs in both games. Our findings show that social preferences are endogenous to counterpart identity in mixed agent systems. These counterpart-contingent social preferences generate markedly different equilibrium dynamics across dyad types.

---

## uid: `doi:10.2139/ssrn.7036766`

- title: Deploying a Course-Specific Artificial Intelligence Tutor Chatbot in Chemical Engineering Computation: A Mixed-Methods Evaluation of Student Learning Outcomes, Engagement, and Self-Efficacy
- authors: Nurhazwani Yusoff Azudin
- affiliations: not stated
- posted: 2026-07-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7036766
- keyword hits: large language model, llm, prompt engineering

### abstract

The integration of artificial intelligence (AI) in engineering education has accelerated with the availability of large language model (LLM) platforms that can be customised to domain-specific instructional content. This study reports the design, deployment, and evaluation of a course-specific AI tutor chatbot in the Chemical Engineering Computation course (KC33503) at Universiti Malaysia Sabah, Malaysia. The chatbot was built on the Poe platform and configured using the RST (Role–Structure–Task) prompt engineering framework, incorporating lecture notes, tutorial questions, and worked solutions as its knowledge base. Deployed over ten weeks (Weeks 4–14) of a single semester for 55 third-year undergraduate students in a blended learning environment, the tool was evaluated using a mixed-methods approach comprising a structured student perception survey (n = 10), self-reported confidence ratings, and qualitative thematic analysis of open-ended responses. Quantitative results revealed high mean scores across all dimensions: learning effectiveness (M = 4.93/5.00), usability (M = 4.85/5.00), content accuracy (M = 4.90/5.00), and engagement and motivation (M = 4.80/5.00). Notably, students reported a statistically meaningful improvement in self-efficacy, with mean confidence scores rising from 3.60 to 4.50 (a gain of 0.90 points, representing a 25% increase) on a five-point scale. Qualitative themes highlighted the chatbot's value in providing immediate, course-aligned feedback; supporting MATLAB and Excel problem-solving; and promoting self-directed learning. The study contributes a reproducible implementation model for AI-enhanced teaching in discipline-specific engineering education and identifies directions for future work, including formal pre-post assessment, extended cohort studies, and integration of adaptive learning pathways.

---

## uid: `doi:10.2139/ssrn.6900918`

- title: The Verifiable Context Layer: The Missing Architectural Commitment in Enterprise Intelligence for Agentic AI
- authors: Vibhuraja Bhutani
- affiliations: not stated
- posted: 2026-07-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6900918
- keyword hits: agentic, foundation model

### abstract

Enterprise AI initiatives continue to stall at the trust boundary despite the increasing maturity of foundation models and agent runtimes. The Enterprise Intelligence Layer (EIL) pattern — a layer between enterprise systems of record and agentic AI workloads — is converging across enterprise vendors under varied branding (Atlan’s Context Layer, Snowflake’s Agent Context Layer, Microsoft Foundry IQ + Purview, Salesforce Einstein Trust Layer, IBM watsonx.governance, Palantir Foundry Ontology). Across these implementations, one architectural commitment is consistently absent or under-specified: an explicit, named layer that turns enterprise context into a substrate for agentic verification. We propose the Verifiable Context Layer (VCL) as a reference architecture for this missing component. The VCL is a named architectural commitment, not a new mechanism, that organises five existing elements — semantic layer, knowledge graph, governance and policy engine, agent runtime, feedback loop — around a single loadbearing claim: that enterprise context, properly governed and instrumented, is the substrate that makes agentic AI verifiable at enterprise scale against both formal verification primitives and the regulatory obligations imposed by the EU AI Act and the NIST AI RMF Agentic Profile. We position the VCL explicitly against partial vendor implementations, illustrate it with a worked enterprise use case, map each component to specific regulatory obligations and formal verification primitives, synthesise publicly attributed industry observations from Klarna, Walmart, JPMorgan, Siemens, Schneider Electric, Notion, and Box, and propose an empirical roadmap with integration guidance for practitioners. We do not claim primary empirical validation; the contribution is a named architectural pattern defended by structural argument, illustrated by a worked example, and grounded in public evidence.

---
