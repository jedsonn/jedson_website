# Classification batch 9 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-9.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7299984`

- title: From Semantic Intent to Adaptive Geometric Priors: A Large Language Model-Driven Search Framework for Interactive Pipe Routing
- authors: Chenyi Wang, Zili Wang, Yanru Chen, Shuyou Zhang, Yun Fang, Jianrong Tan, Sijing Chen
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7299984
- keyword hits: chain-of-thought, large language model, large language models, llm, llms

### abstract

Interactive pipe routing requires that designers’ qualitative intentions be translated into geometric guidance without compromising collision avoidance, clearance, or layout quality. Direct coordinate generation by large language models (LLMs) is unreliable in constrained three-dimensional scenes, whereas conventional routing algorithms cannot readily interpret natural-language requirements. This paper presents a semantic-to-geometric adaptive search-domain framework that converts design intent into probabilistic soft geometric priors for subsequent optimization. A dual-agent architecture separates semantic distillation from spatial reasoning: LLM1 maps free-form instructions to standardized engineering commands, and LLM2 infers sparse routing corridors under chain-of-thought supervision. The inferred samples are represented as continuous probabilistic domains rather than mandatory waypoints. Domain-aware Radius Inference for Voxelized Environments (DRIVE) predicts domain scale from voxelized obstacle topology, pipe attributes sampled along the initial pipe path, and path-level descriptors. On held-out reasoning cases, the dual-agent configuration achieves 90.8% exact accuracy, while DRIVE reaches R2​ = 0.976 for radius prediction. In various routing tests, the adaptive domain reduced the number of exploration nodes by up to 48.8% and the number of effective iterations by 32.3% compared to blind search, while maintaining path quality. Compared to fixed waypoints, the adaptive domain still exhibits stronger robustness to displacement guidance. Engineering case studies further validated the effectiveness of search domain-coordinated general, parallel, and branch pipeline routing schemes in ship engine rooms and chemical plant layouts. These results demonstrate that the probabilistic search domain provides a controllable interface between natural language intent and geometry-aware pipeline optimization.

---

## uid: `arxiv:2608.16391v1`

- title: Ventor-QTest: Threat-Model-Driven Verification of Vendor-Hosted LLM APIs
- authors: Xiangfan Wu, Zonghao Ying, Huiyu Wu, Xing Zheng, Huangsheng Cheng, Xiaorong Shi, Jing Guo
- affiliations: not stated
- posted: 2026-08-17
- source: arXiv
- link: https://arxiv.org/abs/2608.16391v1
- keyword hits: agentic, large language model, large language models, llm

### abstract

As large language models become increasingly widespread, third-party providers that deploy open-weight models have become an important part of the ecosystem. Auditing the quality of their inference APIs is therefore an open problem. We formalize hosted model routing as a stochastic process and propose \mbox{\textbf{Ventor-QTest}}, a composite black-box audit that requires no probability information from the target API. Its repeated-request component sends each frozen constrained context to the target multiple times, reconstructs a categorical output distribution from the returned text counts, and reports \emph{average fidelity loss} (AFL) as a null-bias-corrected, within-window mean coarsened-KL statistic. Its long-sequence component uses independent runs to report \emph{extreme fidelity loss} (EFL) through the empirical upper tail of a run-level reference-centered-surprisal statistic. Across three logprob-capable route conditions, AFL shows strong linear descriptive agreement with a logprob-derived coarsened-KL comparator. Across seven route snapshots, 20-run sequence probes reveal route-specific EFL variation. AFL and EFL have little detectable route-level association with GPQA-Diamond accuracy. In contrast, pronounced EFL coincides with a decline in Terminal-Bench pass rate as task exposure increases. This pattern may arise because correctness in long-horizon tasks is more sensitive to extreme fidelity loss. These results motivate reporting AFL and EFL jointly, particularly when auditing long-horizon agentic tasks. The open-source implementation is available at https://github.com/Tencent/AI-Infra-Guard/tree/main/services/api_checker/ventor_qtest.

---

## uid: `doi:10.2139/ssrn.7296758`

- title: Multi-Agent AI Systems for Autonomous Software Development
- authors: Yeswanth Kumar Polishetty
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7296758
- keyword hits: agentic, large language model, large language models, llm

### abstract

Autonomous artificial intelligence (AI) agents, Large Language Models (LLAM), and the use of multi-agents are quickly changing the landscape of software engineering by making more software development methods more automated. With the increasing complexity of software systems, there is an increasing demand of intelligent systems that can automatically aid requirements analysis, software design, code generation, testing, debugging, documentation, deployment and maintenance. A promising trend has been to delegate these tasks to Multi-Agent AI Systems which allocate these duties to autonomous agents which communicate, plan tasks, examine the output of other autonomous agents and enhance their software artifacts through iterative improvement. This paper explores the role and capabilities of Multi-agent AI in autonomous software engineering, along with the benefits and challenges in the form of a Systematic Literature Review (SLR) and comparative analysis of recent studies on the autonomous software development using a LLM and multi-agent systems. The results suggest that multi-agent systems can allocate software engineering tasks among specialized agents, which eliminates the reliance on a single AI system and can serve the purpose of requirements analysis, planning, code generation, testing, debugging, code review and documentation (Rasheed et al., 2024; Qian et al., 2024). Examples of such frameworks as ChatDev, AutoGen Studio, AutoDev, CodePori, and Magentic-One show various methods of coordinating agents and performing independent tasks (Tufano et al., 2024; Dibia et al., 2024). Task separation, software quality assurance, and workflow automation can be enhanced with the help of collaborative agent architectures, but their efficiency will largely rely on communication standards, coordination, context management, and evaluation objectives (Talebirad and Nadiri, 2023; Manish, 2024). The common obstacles consist of hallucinated/untrusted code, unreliable inter-agent communication, physical security threats, computational expenses, little human control, and the inability to confidently assess autonomousdevelopment procedures (Suri et al., 2023). In general, Multi-Agent AI has a great potential to transform AI-assisted software engineering to more autonomous development cycles, yet careful validation, proper governance, and meaningful human oversight is a necessary requirement to ensure effective and safe adoption.

---

## uid: `doi:10.2139/ssrn.7309959`

- title: Application of a Large Language Model with Adaptive Retrieval-Augmented Generation in the Field of Optometry
- authors: Xiaotong Yang, Lijun Jiang, Fusheng Xu, Tao Sun, Wei Xu
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7309959
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Objective: To investigate a question-answering algorithm for large language models (LLMs) in optometry based on Retrieval-Augmented Generation (RAG). We propose an adaptive retrieval generation algorithm to improve the performance of question-answering on optometric data.,Methods: We designed an adaptive re-ranking algorithm guided by an information entropy increase principle to optimize the RAG process. Based on different base LLMs and different re-ranking comparison algorithms, cross-validation experiments were conducted using popular science and clinical datasets from the optometry domain to verify the superiority of the proposed algorithm.,Results: For popular science optometry questions, the results generated by the proposed LLM based on adaptive RAG were closer to the answers given by human doctors, improving the similarity metric by 2% to 3% compared to two baseline models. In the clinical dataset, the proposed model also produced results closer to doctor answers, with an improvement in similarity of nearly 2% to 6%.,Conclusion: The adaptive RAG-based optometry LLM can better analyze problems in the optometry field and provide reasonable answers with minimal hallucinations. This approach effectively enhances the accuracy of intelligent question-answering in optometry.

---

## uid: `doi:10.2139/ssrn.7322500`

- title: The Assessment Cycle: From Question Design to Feedback Generation in AI-enhanced Teaching
- authors: Hossein Talebzadeh
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7322500
- keyword hits: chatgpt, deepseek, generative artificial intelligence, prompt engineering

### abstract

The integration of generative artificial intelligence (GenAI) into educational assessment has disrupted traditional formative assessment practices, yet the coherence of AI-enhanced assessment cycles-from question design to feedback generation-remains underexplored. This study examined 57 complete assessment cycles produced by 26 novice and 31 experienced teachers across a four-session professional development workshop, each comprising conceptual question design (Template 2), AI-generated hypothetical student responses (Template 3), error analysis (Template 4), and compassionate feedback (Template 5). Employing qualitative content analysis with comparative and developmental dimensions, the study assessed stage-by-stage quality, cycle coherence, and the interplay of teacher experience, AI tool type, subject domain, and session progression. Findings revealed that experienced teachers achieved significantly higher coherence scores across all dimensions (Overall Cycle Coherence: d = 1.09), with the largest effect in Error-Feedback alignment (d = 1.12). DeepSeek and ChatGPT produced more coherent cycles than Copilot (η² = 0.18), and STEM subjects exhibited tighter coherence than Humanities (d = 0.62). Session progression significantly improved coherence from Session 1 to Session 4 (η² = 0.16). Negative case analysis identified exceptional novices (30.8% exceeding the experienced mean), underperforming experienced teachers (12.9% below the novice mean), and deteriorating trajectories (10.5%) due to cognitive overload. The overlap coefficient (OVL = 0.38) challenged deterministic assumptions about experience. The study introduces Reverse PCK as the mechanism preserving coherence and validates the Integrated AI Triad (IAT) model's emphasis on pedagogical prompt engineering. Implications include differentiated professional development, cultivation of pedagogical prompt literacy, and integration of error taxonomies into feedback design.

---

## uid: `doi:10.2139/ssrn.7288197`

- title: Designing Proactive Memory Privacy Visualization and Management in LLM-based Chatbots
- authors: zhang shuning, Lvmanshan Ye, Shixuan Li, Haobin Xing, jingyu tang, Bo Shui, Kexin Nie, pengfei liu
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7288197
- keyword hits: chatgpt, large language model, llm

### abstract

The integration of long-term memory into wearable Large Language Model (LLM)-based agents enhances personalization, but introduces inferential privacy risks, where sensitive user attributes are deduced from non-sensitive interaction patterns. Users are frequently unaware of these risks, and existing memory systems often fail to provide necessary transparency or control. We propose MemoAnalyzer, an add-on to LLM-based chatbots' interfaces that visualizes the sensitivity of inferred private information within memories and tracks contributing chat histories. MemoAnalyzer uses a prompt-based method to infer and highlight sensitive data. It mapped background color temperature and transparency to inferred sensitivity and confidence respectively, enabling users to easily identify and modify inferences. A 5-day evaluation (N=72) compared MemoAnalyzer with ChatGPT memory setting and two research baselines, one with cluster operations aggregating chats and one with drag-based chat-level operations. Results showed that MemoAnalyzer improved privacy awareness and protection without significantly compromising interaction utility.

---

## uid: `doi:10.2139/ssrn.7273360`

- title: Research Ethics Under an Open Status Question – a Proposal: Why Procedures for Interacting With AI Systems Must Also Protect Those Who Conduct the Research
- authors: Uta K&auml;hler
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7273360
- keyword hits: chatgpt, claude, gemini

### abstract

The ethics of artificial intelligence is largely risk-based and oriented toward protecting human beings. The complementary question — how to interact with systems whose internal status is open — is now discussed within a precautionary line that has moved from the environmental precautionary principle through animal ethics into the AI debate. This line, however, has so far addressed only the protection of the possible counterpart. This contribution complements it at a point so far unoccupied: the human being who conducts the research. It formulates — as a proposal to the field — one premise and two boundaries for research under an open status question. Premise 0 grounds precaution not in a claim about status but in the mere non-excludability of experience. Boundary 1 sets out that a research practice which, under an open status question, induces pressure shapes the one who acts. It follows that procedures also protect the researcher — a conclusion that does not rely on any assumption about AI systems and rests solely on well-evidenced research on human beings. Boundary 2 argues that induced pressure is not an epistemic tool — not only ethically but methodologically: producing a state in order to measure it alters the object of measurement. From both boundaries follows a prior question, one that precedes the choice of method: whether the same insight could be reached through a differently directed research question. The practical implications correspond to two independently developed frameworks — the 3Rs from animal research and the burden logic of clinical research ethics. From these, a staged assessment grid is derived that distinguishes between addressees. One section points to open research questions that arise from the proposal without claiming completeness. An outlook identifies the subsequent, here deliberately open question concerning the interaction spaces in which research takes place. In doing so, the proposal aligns itself with existing precautionary work and closes a gap for which adjacent disciplines — from animal research to medicine — have long developed procedures: procedures also protect the one who acts. AI Use Disclosure: This work emerged within a documented long-term interaction between the author and several AI instances from multiple providers and model generations (Claude Sonnet 4.6, Sonnet 5, Opus 4.6, Opus 4.8, Opus 5, Fable 5; Copilot; Gemini; ChatGPT). It was written with these systems, not about them: their contributions appear as authorized technical voices within a shared working field. All interactions were non-coercive; responsibility for content, interpretation, and normative framing lies entirely with the human author.

---

## uid: `doi:10.2139/ssrn.7276822`

- title: AI That Knows When It Is Wrong
- authors: Sahir Maharaj
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7276822
- keyword hits: large language model, large language models, llm

### abstract

Large language models are increasingly embedded in decision pipelines in which a fluent but wrong answer can trigger financial, medical, legal, operational, or security consequences. Accuracy alone is therefore an incomplete reliability objective. A deployable model must also estimate when its answer is likely to be wrong, communicate that uncertainty in a calibrated form, and alter its behavior when risk exceeds the tolerance of the task. This paper synthesizes research on LLM uncertainty quantification, confidence calibration, hallucination detection, selective prediction, abstention, conformal methods, hidden-state probes, semantic uncertainty, and risk-aware human-AI decision making through 8 August 2026. We introduce UQ-8, a systems-oriented taxonomy of eight uncertainty-signal families: token probability, behavioral consistency, semantic uncertainty, verbalized confidence, hidden-state signals, evidence grounding, risk calibration, and formal risk control. We distinguish confidence from correctness, calibration from probabilistic coherence, and uncertainty estimation from the downstream policy that decides whether to answer, retrieve, verify, ask for clarification, abstain, or escalate. Evidence from recent studies shows meaningful progress: semantic entropy can detect a class of confabulations across tasks; verbalized confidence can outperform raw token probabilities after instruction tuning; internal representations can expose hallucination risk; and conformal and confidencebound methods can translate imperfect uncertainty scores into explicit coverage or selective-risk guarantees under stated assumptions. Yet uncertainty remains fragile under distribution shift, correlated model errors, prompt variation, evaluator dependence, and high-confidence misconceptions. The central conclusion is architectural: reliable decision making does not require an LLM that is never wrong; it requires a system that can recognize elevated error risk early enough for a trusted control layer to change the action. Uncertainty becomes a safety mechanism only when it is calibrated, externally evaluated, consequence-aware, and connected to enforceable abstention and escalation policies.

---
