# Classification batch 15 of 22, edition 21

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-021/batch-15.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7305416`

- title: S-BEED: Sparse Bayesian Ensemble with Entropy-Calibrated Debate for Medical Multiple-Choice Question Answering
- authors: Wangyun Dan, Suyang Xi, Chenzi Guo, Ximing Ran, Zhaohui Qin
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7305416
- keyword hits: large language model, large language models, prompting

### abstract

Background and Objective: Both accuracy and reliable calibration are necessary for deploying large language models in medical question answering, where overconfident errors translate directly into clinical risk. Existing approaches, whether single-model prompting, static ensemble voting, or free-form multi-agent debate, either yield poorly calibrated confidence estimates or incur prohibitive inference costs.Methods: We introduce S-BEED, a sparse multi-agent framework that treats the group belief distribution over candidate answers, rather than a single hard label, as the primary object of inference, giving clinicians and downstream systems an interpretable uncertainty signal they can act on. For each question, a slice-aware router activates a small subset of reliable agents that revise their option-level beliefs through a structured, entropy-weighted debate, and the aggregated group belief is calibrated at the output layer.Results: Across MedQA, MMLU-Clinical, and MedMCQA-Single, S-BEED achieves the highest accuracy and the lowest expected calibration error on all three datasets while using far fewer tokens than dense and dedicated multi-agent baselines (up to roughly 94% fewer) and remaining comparable in cost to simple ensembling. In a selective-prediction analysis, deferring the least-confident predictions reduces error faster for S-BEED than for the single-best model on every dataset. A single-parameter output-layer temperature scaling further improves the calibration error, the Brier score, and the negative log-likelihood without changing accuracy, indicating that the raw group beliefs are well ranked but over-sharpened, and ablation experiments confirm that sparse routing, the structured debate protocol, entropy-aware influence weighting, and early convergence stopping each contribute to overall performance.Conclusions: Treating a sparse, calibrated group belief as the primary inference target yields medical question answering that is simultaneously more accurate, better calibrated, and more efficient than existing approaches.

---

## uid: `doi:10.2139/ssrn.7313387`

- title: Coordinating Multiple Rewards in Rank Space for Spatial Reasoning
- authors: Han Wang, Ziru Wang, Haowen Sun, Xinzhe Chen, Xingyu Chen, Zeyang Liu, Xuguang Lan
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7313387
- keyword hits: chain-of-thought, large language model, large language models

### abstract

Multimodal large language models (MLLMs) have achieved remarkable progress in vision–language tasks, but continue to struggle with spatial reasoning. Existing spatial MLLMs rely on large-scale datasets, explicit 3D inputs, architecture-specific modifications, or sparse Reinforcement Learning (RL) methods that provide insufficient guidance for spatially-grounded reasoning.Moreover, such algorithms based on sparse outcome-driven rewards often yield ``right-answer wrong-path'' false positives, where conclusions are correct but the underlying geometric logic is flawed. Although process reward models are typically introduced to provide dense intermediate supervision, combining noisy process scores with outcome rewards via standard zzz-score normalization contaminates in-group statistics and induces reward hacking. Meanwhile, on already-correct groups the vanishing outcome signal leaves flawed "right-answer wrong-path" reasoning uncorrected. Together these failure modes stall or even degrade spatial-reasoning gains. To overcome this, we propose RT-GRPO, a Rank-Transformed GRPO framework that constructs advantages in rank space rather than using raw reward values. Our framework introduces two key innovations: (i) a lexicographic advantage formulation that prioritizes format compliance as a hard gate, outcome correctness as the primary order, and process quality strictly to break ties; and (ii) a batch-level information weighting mechanism that suppresses zero-signal groups while preserving gradients for process refinement in already-correct groups. Evaluations across three complementary benchmarks (RoboBench, RoboSpatial-HOME, and 3DSRBench) demonstrate that RT-GRPO establishes a new state-of-the-art among comparably sized models. Furthermore, real-world deployment on a Franka FR3 robot confirms its superior robustness and the practical efficacy of its chain-of-thought reasoning.

---

## uid: `doi:10.2139/ssrn.7244142`

- title: Compliance By Design: GDPR, Cybersecurity, And the AI Act in Extended Reality Platforms for Industry 5.0
- authors: Marcelo Corrales Compagnucci, Harsh Manoj Shah
- affiliations: not stated
- posted: 2026-08-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7244142
- keyword hits: large language model, llm

### abstract

The rapid deployment of Extended Reality (XR) and Artificial Intelligence (AI) technologies in industrial environments raises complex legal, ethical, and regulatory challenges that organisations must navigate with care. This chapter presents the compliance-by-design framework developed within XR5.0, a Horizon Europe initiative deploying human-centric XR and AI tools across six industrial pilot cases, and demonstrates how each major requirement of that framework was concretely implemented in the XR5.0 Training Platform-a cloud-based orchestration system for immersive industrial training. The chapter analyses the EU regulatory landscape-the GDPR, NIS2 Directive, Cybersecurity Act, Cyber Resilience Act, and AI Act-alongside the ethical framework of the High-Level Expert Group (HLEG) Guidelines on Trustworthy AI and the Assessment List for Trustworthy AI (ALTAI). While the XR5.0 Training Platform is not, strictly speaking, a standalone AI system, it incorporates a number of AI-enabled functionalities-including local large language model (LLM) processing, AIassisted chat functionalities, and adaptive personalisation features-which justify a proportionate and context-sensitive application of the HLEG and ALTAI trustworthy AI principles. A central contribution is tracing how these legal and ethical instruments materialise in the platform's architecture. GDPR compliance is operationalised through data minimisation, a lawful basis grounded in contractual necessity, transparency via a structured consent workflow, and data protection by design through session token authentication and pixel streaming. Cybersecurity is ensured through TLS encryption and multi-tenant cloud isolation, while AI governance is supported by an administrator-controlled training authoring model, session audit logging, and device-agnostic Universal Design implementing the seven ALTAI requirements for trustworthy AI. The chapter argues that embedding compliance into design from the outset is both a legal obligation and a prerequisite for responsible innovation, and offers a replicable compliance-by-design model for EU-funded research projects at the intersection of XR, AI, and industrial data processing.

---

## uid: `doi:10.2139/ssrn.7249778`

- title: MAITREYI: A Pedagogical Instruction Architecture for AI Agents; Model for Artificial Intelligence Training, Reflective Education and Yielding Instructions
- authors: Ashwin Kumar Iyer
- affiliations: not stated
- posted: 2026-08-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7249778
- keyword hits: ai agent, large language model, large language models, prompt engineering

### abstract

Large language model agents are typically instructed through prompt engineering: an accumulation of ad hoc rules, examples and constraints written directly into a system prompt as failures are discovered. As agents take on more persistent, higher stakes roles, holding memory across sessions, operating across multiple underlying model providers, running for extended autonomous stretches, this mode of instruction shows predictable failure. Rules do not transfer across models, behaviour drifts over long deployments, and instruction sets accumulate maintenance costs that outpace their usefulness. A substantial and growing literature has applied instructional design theory to large language models, but almost exclusively in one direction: the AI as tutor, generating curricula, lesson plans and adaptive feedback for human learners. This paper inverts that direction. We introduce MAITREYI (Model for Artificial Intelligence Training, Reflective Education and Yielding Instructions), a framework that applies the apparatus of instructional design, curriculum sequencing, worked examples, formative assessment and spaced reflection, to the instruction set governing an AI agent’s own behaviour, treating the agent as the learner and the human operator as the instructor. MAITREYI separates an agent’s instructions into eight components: Constitution, Curriculum, Playbooks, Case Studies, Examinations, Reflection Journal, Knowledge Base and Memory Layer, organised along a single architectural distinction between material that is enduring and expected to change rarely, and material that is evolving and expected to change often. We argue that this separation, rather than any individual component, is what produces three claimed benefits: portability of behaviour across model providers, reduced maintenance cost as instruction sets grow, and reduced behavioural drift over long deployments. None of these three benefits are demonstrated empirically here. Each is stated as a claim to be argued rather than a finding to be reported, and we specify a falsifiable experimental protocol for testing all three. The paper is scoped deliberately as a work of synthesis and formalisation rather than invention. Nearly every individual component we describe, layered system prompts, principle based steering, reusable instruction modules, structured agent memory, already exists in some form in production systems or prior research. The contribution of MAITREYI is the unifying grammar across these components, the enduring/evolving distinction as an organising principle, and the proposed validation methodology.

---

## uid: `doi:10.2139/ssrn.7270443`

- title: Adoption of Generative Artificial Intelligence in Clinical Practice: An Online Survey of Physicians and Nurses in Sweden
- authors: Carolina Garcia Sanchez, Anna Kharko, Emma Brulin, Josefin Hagström, Maria Hägglund, Charlotte Blease
- affiliations: not stated
- posted: 2026-08-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7270443
- keyword hits: chatgpt, generative artificial intelligence

### abstract

Background: Generative artificial intelligence (GenAI) tools are rapidly entering clinical environments worldwide, yet little is known about their contrastive adoption among doctors and nurses. In Sweden, understanding current patterns of GenAI use is essential to inform policy, training, and regulatory frameworks. The aim of this study was to describe and contrast the prevalence and patterns of GenAI adoption among physicians and nurses in Sweden, including tools used, clinical purposes, and institutional context. Methods: ​We conducted a cross-sectional survey using stratified random sampling among physicians and nurses participating in the 2025 Longitudinal Occupational Health Survey in Health Care Sweden (LOHHCS). A total of 9,401 physicians and 9,404 nurses aged 80 years or younger and practicing in Sweden were invited to participate. The primary outcome was the prevalence of GenAI adoption for clinical work. Findings: 20.9% of physicians (633/3,025) and 9·3% of nurses (270/2,874) reported purposeful use of GenAI tools to support clinical work. ChatGPT was the most commonly used tool in both professions (physicians, 84·4%; nurses, 80·7%). The leading clinical use differed by profession, with physicians most commonly reporting use for differential diagnosis (53·9%) and nurses for treatment options (34·4%). Employer encouragement of GenAI use in the past 12 months was reported by 9·3% of physicians and 6·0% of nurses, prohibition by 1·5% and 0·7%, and training by 6·2% and 3·9%, respectively. 30·6% of physicians and 33·2% of nurses reported that AI use would reduce their sense of meaning in work. Interpretation: GenAI adoption among physicians and nurses in Sweden revealed substantial but uneven uptake, concentrated among physicians and reliant on consumer-grade tools for clinical decision support. The gap between real-world adoption and institutional governance underscores the need for structured guidance, targeted training, and regulatory clarity to support safe integration into clinical practice.

---

## uid: `doi:10.2139/ssrn.7276418`

- title: How spatial recreational activities shape cultural ecosystem benefits: Causal evidence from integrating a large language model with double machine learning
- authors: Qiqi Zhao, Jing Li, Zixiang Zhou, Manchun Li, Yanming Chen, Yubin Wu, Keshava  Pallavi Gone
- affiliations: not stated
- posted: 2026-08-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7276418
- keyword hits: large language model, llm

### abstract

Cultural ecosystem benefits (CEB) are non-material benefits that people derive from environmental spaces and are important for sustainable urban environmental management. Recreational activities provide pathways through which people experience these benefits, but how different activities shape specific CEB remains insufficiently understood. To address this gap, this study first uses a large language model (LLM) to identify CEB and spatial recreational activities from social media data, and then applies double machine learning (DML) to estimate the causal effects of recreational activities on CEB under measured-confounder assumptions. Using 85,766 Ctrip reviews from 344 scenic sites in Xi'an, we identified five CEB types and seven recreational activity types, and estimated 35 treatment-effect pairs, of which 18 were statistically significant. Results reveal pronounced differences in the intensity and direction of activity effects across CEB types: history is shaped by the widest range of activities and is more susceptible to negative effects; education derives primarily from learning activities; aesthetic and recreational benefits accrue from common recreational activities; while culture requires targeted cultural engagement. Spatial factors exert the strongest moderating effect on causal effects, followed by the site-specific factor, while temporal factors have the least influence. These findings provide a quantitative basis for matching recreational activities to site functions and targeted cultural benefits in urban environmental management.

---

## uid: `doi:10.2139/ssrn.7275148`

- title: VulTrigger: Multi-Agent LLM Generation of Downstream Vulnerability-Triggering Tests for Third-Party Libraries
- authors: Xiaolin JU, Xinhua Yu, Rongcun Wang, Chang Li, Xiang Chen
- affiliations: not stated
- posted: 2026-08-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7275148
- keyword hits: llm, llms

### abstract

Context:Modern software development's reliance on open-source components introduces security risks throughout the software supply chain. Existing Software Composition Analysis (SCA) tools mainly detect vulnerable dependencies through version matching, but such evidence alone cannot confirm whether the vulnerable behavior is reachable and triggerable in a specific downstream application, and generating executable tests for such confirmation remains challenging due to multi-layered call graphs and subtle vulnerability behaviors requiring dedicated test oracles.Objective:To address these limitations, we propose VulTrigger, a multi-agent, LLM-based framework for generating downstream vulnerability-triggering tests for third-party library vulnerabilities. VulTrigger aims to distinguish dependency-level exposure from confirmed downstream triggerability by providing executable, runtime-validated evidence.Method:VulTrigger extracts vulnerability metadata, dependency evidence, and downstream usage context from vulnerability reports, PoC examples, and downstream source code, then applies bridging-point path analysis and source-preservation reasoning to identify Reachable Triggering Paths along which vulnerability-related inputs propagate to the vulnerable library API. A blackboard-based multi-agent workflow coordinates trigger-plan construction, constrained test generation, execution-based verification, and debugger-guided iterative repair to improve the executability and effectiveness of the generated tests.Results:On 68 vulnerability–downstream application samples spanning 30 third-party dependencies and 44 downstream projects across Java and Python, VulTrigger confirms 57 samples (83.82% success rate), outperforming TRANSFER and VulEUT by 35.29 and 13.24 percentage points, respectively (both statistically significant under the exact McNemar test). Ablation and comparative analyses further show that trigger-plan construction, path analysis, source-preservation reasoning, blackboard-based coordination, multi-agent collaboration, iterative repair, and stronger LLMs each contribute to the observed effectiveness.Conclusions:These results suggest that program-analysis-guided LLM agents can provide executable evidence of the triggerability of downstream vulnerabilities under the evaluated settings. VulTrigger is intended to complement, rather than replace, dependency-level SCA alerts and static reachability analysis.

---

## uid: `doi:10.2139/ssrn.7253318`

- title: When Does Generative AI Level the Playing Field? Evidence from Crowdsourced Earnings Forecasts
- authors: Leonard Yang Liu, Musa Subasi
- affiliations: not stated
- posted: 2026-08-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7253318
- keyword hits: chatgpt, generative ai

### abstract

Whether generative AI (GenAI) levels the playing field or reinforces existing advantages depends on which constraint it relaxes. We argue that GenAI substitutes for institutionalized analytical resources while complementing human expertise. We test this distinction using crowdsourced earnings forecasts from Estimize. We find that non-professional contributors persistently underperform professionals in forecast accuracy before the release of ChatGPT; afterward, the gap is no longer present. Inferring contributors' GenAI reliance from forecasting behavior during ChatGPT service outages, we find that GPT-reliant non-professionals produce more accurate and independent earnings forecasts, while professionals are largely unaffected, consistent with GenAI relaxing institutional resource constraints. Among non-professionals, where analytical resources are relatively homogeneous, only experienced contributors improve after adopting GenAI; inexperienced adopters show no gains and may herd more. Our cross-sectional tests suggest that non-professionals benefit more when disclosures are difficult to process and, separately, when information asymmetry is low. Furthermore, stock returns around earnings announcements respond more strongly to non-professional forecast surprises in the post-GPT period. Collectively, our findings reconcile conflicting evidence on GenAI's distributional effects: the technology democratizes information production by substituting for institutionalized resources while amplifying the returns to expertise.

---
