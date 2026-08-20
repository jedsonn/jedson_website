# Classification batch 11 of 22, edition 21

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-021/batch-11.answer.json` as a JSON array.

---

## uid: `arxiv:2608.12875v1`

- title: The Embedder's Dilemma: LLMs Are Better, but at What Cost?
- authors: Adnan El Assadi, Niklas Muennighoff, Jinhyuk Lee
- affiliations: not stated
- posted: 2026-08-13
- source: arXiv
- link: https://arxiv.org/abs/2608.12875v1
- keyword hits: gemini, large language model, llm, llms

### abstract

Should you replace your text-embedding pipeline with a large language model? We answer this with a controlled, cost-aware comparison of ten LLMs across six families and 26 embedding models (118M to 14B parameters) on 37 tasks spanning classification, semantic textual similarity (STS), clustering, pair classification, and retrieval. In aggregate the two paradigms are effectively tied: the best LLM (Gemini 3.1 Pro, 77.6) and the best embedding model (77.2) differ by 0.4 points. Their strengths differ by task: LLMs lead on reasoning-heavy retrieval, embedding models lead on classification, and the two match on clustering, STS, and pair classification. Reaching that parity is expensive. An LLM costs up to 1,431x more than an embedding model of comparable quality (USD 154 vs. USD 0.11 per benchmark pass), and the open LLMs tested process tokens 2.5 to 736x more slowly on the same GPU. Reasoning tokens account for 28 to 81% of LLM inference cost; lower reasoning budgets preserve or improve retrieval quality for most models in our ablation. The Pareto frontier contains the leading embedding models and one LLM, Gemini 3.1 Pro. These results support a division of labour: use embedding models for similarity, classification, and clustering, and reserve LLMs for reasoning-intensive retrieval. Our code, datasets, and results are publicly available at https://github.com/embeddings-benchmark/embedders-dilemma.

---

## uid: `doi:10.2139/ssrn.7270413`

- title: ReaRx: Reasoning and Refinement for Safe Herbal Prescription Recommendation via Expert-Guided Reinforcement Learning
- authors: Junjie Long, Jinghao Niu, Heping Wang, Ruike Gao, Yuxin Wu, Wensheng Zhang, Jie Li
- affiliations: not stated
- posted: 2026-08-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7270413
- keyword hits: large language model, large language models, llm, llms

### abstract

Herbal prescription recommendation (HPR) in traditional Chinese medicine (TCM) is a challenging clinical decision-support task that requires fusing heterogeneous patient information, domain knowledge, and institution-specific clinical constraints. Although recent methods leveraging deep learning and large language models (LLMs) have advanced this task, their limited use of these complementary sources may constrain prescription accuracy and weaken clinical safety assurance. To address these limitations, we propose ReaRx, a novel deep learning model for personalized and safe prescription recommendation. ReaRx comprises a prescription reasoning module and a prescription refinement module, which together emulate the clinical workflow of TCM physicians. The prescription reasoning module fuses heterogeneous clinical information to enhance patient representation and generate foundational prescriptions. For the prescription refinement module, we introduce an expert-guided herbal prescription refinement framework, named EGHPR, which incorporates institution-specific guidelines into a multi-step decision-making process within a policy-based reinforcement learning framework to iteratively refine the generated prescriptions. Experimental results under five-fold cross-validation on the TCM-GCD dataset demonstrate that ReaRx achieves state-of-the-art performance. Ablation studies, parameter analysis, and case studies further validate the effectiveness and practicality of the proposed modules. EGHPR can also be seamlessly integrated into existing LLM-based prescription recommendation models, improving prescription accuracy without retraining or updating the underlying models. Overall, ReaRx closely aligns with the clinical prescription process of TCM physicians, while EGHPR further enhances the accuracy, clinical relevance, and safety of generated prescriptions, demonstrating practical value for personalized and safe prescription recommendation.

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

## uid: `doi:10.2139/ssrn.7272084`

- title: Quantifying Representational Mismatch between Narratives and Structured Reports in Near-Death Experiences
- authors: Cristian Pulido, Francisco Gómez, Prejaas K.B. Tewarie, Roxane S. Hoyer, Steven Laureys
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7272084
- keyword hits: large language model, large language models, llm, llms

### abstract

Near-death experiences (NDEs) are often studied using both structured questionnaires and narrative reports, yet these representations cannot be assumed to provide interchangeable representations of the same experience. Narratives allow flexible expression of different aspects of the experience, whereas questionnaires organize reports into predefined dimensions and retrospective evaluations. How disagreement between these formats should be quantified and interpreted remains unclear. This study operationalized this disagreement as \emph{representational mismatch} by comparing questionnaire-derived and narrative-derived labels across \NDEAnalyzed~NDE reports. Narratives were coded using 12 large language models (LLMs), complemented by human-reference annotation, a lexical baseline, external sentiment benchmarks, and preprocessing sensitivity analyses. Correspondence was evaluated across emotional tone, experiential features (NDE-C), and post-experience life changes (LCI-R). Agreement was systematic but incomplete and differed across representational domains. Experiential features showed stronger correspondence than life changes (NDE-C macro F1 =$0.62\,[0.60,0.65]$ vs. LCI-R $0.52\,[0.50,0.54]$). Narrative tone contained meaningful affective information but corresponded only partially with global self-reported valence (macro F1 =$0.43\,[0.41,0.44]$), with disagreement concentrated mainly in mixed and neutral narrative-tone assignments rather than direct polarity reversals. Standard sentiment benchmarks showed substantially higher correspondence (macro F1 $=0.78 \pm 0.16$), making a purely general model-limitation explanation less plausible. These findings support interpreting cross-format disagreement as a structured property of reporting rather than measurement or extraction error alone. Representational mismatch provides a framework for identifying where different reporting formats converge, where they cease to be interchangeable, and how the elicitation format shapes what becomes observable in research on subjective experience.

---

## uid: `doi:10.2139/ssrn.7270241`

- title: What is Collaborative Inference? Conditions for Collective Reasoning beyond Individual Inference in the Age of LLMs
- authors: Akira Funabiki
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7270241
- keyword hits: large language model, large language models, llm, llms

### abstract

This paper proposes a theoretical framework for collaborative inference in the age of large language models (LLMs). It conceptualizes individual intellectual activity as a recursive cycle of Value → Question → Reasoning → Understanding → Value Updating → New Question , and defines collaborative inference as the mutual updating of reasoning through interaction with difference. Unlike approaches that emphasize agreement or shared answers, this framework allows participants to retain divergent conclusions while transforming their own reasoning through interaction. The framework is applied to Human–LLM interaction, where LLMs are conceptualized not as answer-generating teachers but as heterogeneous inferential systems that can introduce alternative perspectives, expose assumptions, and stimulate critique and reconstruction. The paper further develops a model of self-updating education , shifting the focus of learning from acquiring fixed answers toward generating questions, revising reasoning, reconsidering values, and generating new questions. To connect the framework with empirical research, the concept of an Update Trace is proposed for examining changes in learners' reasoning over time. The central proposition is that collaborative inference is not the elimination of difference, but the continuous updating of reasoning through difference and the generation of new inquiry .

---

## uid: `doi:10.2139/ssrn.7270039`

- title: PAUSE: A Privacy-preserving Self-reflection Tool for AI-associated Cognitive Offloading
- authors: Mahbub Ul Alam
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7270039
- keyword hits: large language model, large language models, llm, llms

### abstract

Cognitive offloading is the use of external aids, such as notes, calculators, or search engines, to reduce mental effort. Large language models (LLMs) extend this to thinking itself, and by AI-associated cognitive offloading, I mean the pattern where a person routinely substitutes LLM output for their own reasoning, idea generation, learning, or communication. Recent empirical work reports associations between some patterns of LLM use and changes in critical thinking effort, neural engagement during assisted tasks, creative diversity, learning behaviour, and social dependence. Validated instruments for AI reliance, dependence, and literacy have begun to appear. I describe PAUSE (Patterns of AI Use: Self-Examination) , a privacy-by-design web tool that occupies a different niche from these. It is a lightweight, non-diagnostic reflection aid for private individual use. PAUSE is organised around how a person's own LLM use may relate to cognitive offloading across four everyday domains (reasoning & critical thinking, creativity & originality, research & learning, and social & communicative capacity). It delivers a short, free, no-login self-check, scores it entirely in the browser, and returns descriptive, domain-aware reflections. The self-check pairs reverse-scored behavioural items with a claim-evaluation reasoning probe, an alternative-uses creativity probe, and a small retrospective before-and-after block. PAUSE does not assume that AI use is harmful. It addresses the narrower case where AI substitutes for effort a person may want to preserve. The application is privacy-preserving by design: scoring is deterministic and runs client-side, no personal data is required, nothing is transmitted or stored beyond the browser session, and no LLM is involved in production. In this paper, I describe the conceptual grounding, the item design, the scoring, the architecture, and the design philosophy. PAUSE is a self-reflection tool, not a validated psychological instrument. It presents no reliability or validity evidence, and all readings should be interpreted as descriptive self-reflection rather than psychological measurement.

---
