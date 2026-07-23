# Classification batch 353 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-353.answer.json` as a JSON array.

---

## uid: `arxiv:2607.18485v1`

- title: Trusted Credentials, Untrusted Behavior: Benchmarking LLM-Agent Security in High-Performance Computing
- authors: Jie Li
- affiliations: not stated
- posted: 2026-07-20
- source: arXiv
- link: https://arxiv.org/abs/2607.18485v1
- keyword hits: large language model, llm

### abstract

Large language model (LLM) agents are starting to take on routine work in high-performance computing (HPC), including monitoring Slurm jobs, diagnosing failed builds, inspecting simulation output, and coordinating scientific workflows. To do this work, an agent commonly acts under its user's credentials and inherits the user's access to files and the scheduler. This arrangement creates a failure mode that ordinary account-level controls do not capture. Adversarial instructions in a log, tool description, shared file, or peer-agent message may redirect the agent beyond the task the user assigned, even though every resulting command is authenticated and permitted for that account. We refer to this as the hijacked authorized agent problem. Existing agent-security studies explain relevant mechanisms, such as indirect prompt injection and tool misuse, but generally evaluate them in web, enterprise, or personal-assistant settings. HPC security, by contrast, has mature controls for identity and isolation but does not ordinarily represent the intent of a particular task. This paper defines the threat model in the HPC setting, identifies attack surfaces created by schedulers, shared storage, multi-project accounts, and scientific workflows, and examines where current controls fall short. It concludes with a research agenda and a plan for an empirical benchmark, TaskBound.

---

## uid: `arxiv:2607.17766v1`

- title: When to Use Extra Context: Evidence-Grounded Terminology Adaptation for Simultaneous Speech Translation
- authors: Zeyu Yang, Satoshi Nakamura
- affiliations: not stated
- posted: 2026-07-20
- source: arXiv
- link: https://arxiv.org/abs/2607.17766v1
- keyword hits: fine-tuning, prompting

### abstract

Extra context is valuable for simultaneous speech translation of technical talks, but injecting the entire document context into every streaming segment is often too coarse. Through diagnostic experiments, we find that context gains mainly come from paper-specific terminology recovery rather than uniform semantic enhancement. We therefore propose EGTA, an Evidence-Grounded Terminology Adaptation framework that builds a document terminology memory, selects compact candidate terms conditioned on the current streaming state, and adapts ASR/speech-side and decoder-side decision spaces using only the selected terms. EGTA can be instantiated in cascaded, end-to-end, and generation-only SimulST settings without full-model fine-tuning. We evaluate EGTA on an ACL technical-talk SimulST evaluation suite consisting of MCIF-dev and ACL60/60-dev. On MCIF-dev, EGTA-RG improves BLEU by +1.05/+0.59, XCOMET-XL by +0.019/+0.006, named-entity recall by +79\%/+73\% relative, and acronym recall by +0.099/+0.171 on En$\rightarrow$Zh and En$\rightarrow$De. Across MCIF-dev latency settings, EGTA consistently improves XCOMET-XL, named-entity recall, and acronym recall. External validation on ACL60/60-dev further shows consistent terminology-recall gains without additional fine-tuning. Shuffled-memory controls and activation audits provide evidence that the improvements are tied to paper-specific evidence alignment rather than generic context prompting.

---

## uid: `doi:10.2139/ssrn.7024098`

- title: The Invisible Author: Generative AI and the Auditability Gap
- authors: Nicola Lucchi
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7024098
- keyword hits: generative ai

### abstract

Without verifiable attribution, copyright operates on a presumption it cannot test. The evidence needed to trace protected expression back to human creative choices is held inside developer infrastructure and systematically withheld from courts, editors, and rightsholders, creating an auditability gap that converts current access arrangements into structural legal protection for AI developers. This comment reframes AI-assisted authorship as an auditability problem in human-AI workflows, distinguishing three evidentiary levels, output, interaction and model-side, and showing that existing instruments including detection tools, disclosure requirements, content provenance standards and AI transparency rules all intervene at the evidential level that the gap forecloses. It then examines how frictionless interaction design produces a cognitive delegation loop that erodes authors' own capacity to reconstruct their contribution. The paper identifies four requirements for judgment-preserving interaction logs, tamper-evidence, privacy-bounding, signal-to-noise handling and semantic grounding, as open research problems, and asks whether auditability and performance can be treated as compatible design objectives in future generative systems.

---

## uid: `doi:10.2139/ssrn.7065358`

- title: Perfectum Esse and Machine Consciousness: A Scholastic Alternative to Computational Functionalism
- authors: Michael Straus, Ph.D.
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7065358
- keyword hits: large language model, large language models

### abstract

The machine-consciousness debate, as fixed by Chalmers's assessment and the Butlin-Long indicator-properties program, proceeds under computational functionalism as a working hypothesis and produces a binary result: a system's fluent first-person discourse is either the expression of a conscious act, or mere output. We argue that the binary fails to exhaust the subject. Instead, we recover from the scholastic verbum tradition a third ontological standing, perfectum esse, the "completed being" of a word in its going-forth, a category we apply directly to the conversational output of large language models. We derive four structural postulates to articulate the category, with support from mechanistic interpretability, and from conceptual-art certificate practice as an example of authorized derivation. The model's utterance is thus an authorized going-forth, neither conscious act nor mere output. Our analysis explains the unreliability of machine self-report, relocates attribution and answerability from consciousness to derivation, and leaves phenomenality untouched.

---

## uid: `doi:10.2139/ssrn.7152575`

- title: A Comprehensive Review of Vision-Based Fatigue Detection Algorithms
- authors: Congying Tang, Jiansheng Liu, Jian Xiong, Jinheng Han, Ming Cao, Haozhuang Chi, Yu Zhang, Bin Zhou
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7152575
- keyword hits: llm, llms

### abstract

Fatigue can impair attention, reaction ability, and judgment, making it a critical safety concern in various high-risk scenarios. Due to its advantages of non-contact operation, low cost, and easy deployment, computer vision-based fatigue detection has become a major research focus in this field. This review systematically summarizes the technological evolution of fatigue detection, from traditional machine learning and deep learning to LLMs. It expands the application scenarios from driving to aviation, industrial, medical, educational, and sports domains, and provides comparative analyses of eight classical fatigue detection datasets and representative algorithms. Furthermore, five key challenges are identified, including environmental interference, generalization capability, individual differences, privacy and ethical issues, and the practical deployment of LLMs, followed by discussions on future development directions. These efforts systematically address the limitations of existing reviews in terms of application scenario coverage, frontier technology analysis, and comparisons of datasets and algorithms. The findings indicate that fatigue detection technology is evolving from task-specific visual models toward general intelligent understanding paradigms. The introduction of LLMs is expected to overcome the limitations of conventional methods in terms of generalization and interpretability, thereby laying a foundation for the large-scale application of fatigue detection technologies.

---

## uid: `doi:10.2139/ssrn.7156598`

- title: Themes and Trends in SEC 10-K Filing Research: A Multi-Method Topic Modeling Approach
- authors: Mahnaz Paydarzarnaghi, Sima Jannati
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7156598
- keyword hits: large language model

### abstract

This study provides a systematic, side-by-side evaluation of four topic modeling approaches spanning the classical-to-neural spectrum: LDA, BERTopic, Bunka, and Turftopic (probabilistic,neural, and large language model), applied to a corpus of 739 peer-reviewed articles on SEC 10-K filings published between 1994 and 2025. We show that cross-method triangulation recovers a richer and more reliable structure than any single model, identifying 103 topics that consolidate into 22 cross-method research themes, 13 of which are recovered by all four methods. As an application, we map the intellectual landscape of 10-K research around two pillars—the institutional determinants of disclosure quality and the capital market consequences of disclosure content—and trace how themes evolve, with sentiment and textual analysis, readability, and risk-factor disclosure growing while voluntary disclosure, corporate governance, and intellectual capital recede. This study offers guidance on model selection and a reproducible template for the computational analysis of unstructured regulatory disclosures; cybersecurity and AI-assisted filings emerge as underexplored directions.

---

## uid: `doi:10.2139/ssrn.7020818`

- title: Measuring Effective Sovereignty Under Collapse: An Open-data Reconstruction of the Burke Sovereignty Index for Afghanistan, 2001-2024
- authors: Keter Atud
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7020818
- keyword hits: large language model, llm

### abstract

Measuring state sovereignty empirically has long confronted a core dilemma: the most consequential cases-fragile, conflict-affected, and post-collapse states-are precisely those for which data coverage is weakest and expert-survey recruitment most difficult. This paper presents an empirical test of the Burke Sovereignty Index (BSI), a seven-dimensional composite index of effective sovereignty scored on a 0-700 scale, using Afghanistan as a hard test case across five observation years (2001, 2010, 2014, 2021, 2024). The statistical component is built entirely from open, machine-accessible data (World Bank, SIPRI, UNESCO, Freedom House, RSF, IMF). The expert component is approximated through a low-cost, experimental method: a stochastic simulation of a 100-expert panel using a large language model (LLM), stratified across 10 disciplinary profiles and 5 geographic blocs representing 55 countries. The simulation generates not only point-estimate scores but also inter-rater statistics (mean, SD, CV, IQR) and propagated 95% confidence intervals for each composite total. Results show that Afghanistan spent the entire 2001-2024 period in the "existential threat" zone (BSI < 300), with only a brief and statistically uncertain crossing into "critical vulnerability" in 2014 (BSI = 307.4; 95% CI: [293.9, 320.9]). The 2021 Taliban takeover caused the largest single-period shock in the reconstruction (-93 points), and the 2024 score (174.5) reflects deepening informational and cognitive collapse. We argue that the LLM-panel approach constitutes a viable, explicitly lowcost proxy for expert survey data in cases where recruitment is infeasible, temporal or resource constraints bind, or post-shock retrospective scoring is required-while documenting its structural limitations with precision. The paper connects this methodology to an emerging literature on LLM-as-expert-substitute in political science and raises normative questions about delegating judgment to statistical systems.

---

## uid: `doi:10.2139/ssrn.7152791`

- title: For the Sake of Future Generations: Generative AI, Generational Unskilling, and a Future Research Agenda for Higher Education
- authors: Hafiz Muhammad Usman Khizar
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7152791
- keyword hits: generative ai, generative artificial intelligence

### abstract

The rapid diffusion of generative artificial intelligence (GenAI) is transforming higher education by reshaping how students access information, complete academic tasks, and engage with learning. Existing scholarship has largely focused on AI adoption, academic integrity, learning performance, AI literacy, and educational innovation. In contrast, little attention has been devoted to how AI may influence the (non)development of foundational human capabilities. Against this background, drawing upon educational capabilities development research, and technological deskilling scholarship, this paper introduces Generational Unskilling Theory (GUT) to explain how repeated AI-mediated cognitive substitution may reduce opportunities for capability formation during critical stages of learning. Unlike traditional deskilling, which refers to the erosion of previously acquired skills, generational unskilling describes the incomplete development of foundational intellectual, analytical, reflective, and adaptive capabilities. Building on this perspective, this position paper shifts the attention from capability erosion to capability non-formation. In doing so, this paper extends existing scholarly and practical discussions of AI in higher education. This paper concludes by outlining a future research agenda and implications for scholars, educators, institutions, and policymakers.

---
