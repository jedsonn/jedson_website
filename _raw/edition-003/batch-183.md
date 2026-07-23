# Classification batch 183 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-183.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6951999`

- title: Inference-Subordinate Simulation: Decoupling Agent Decision Time from Playback Time in 3D Environments
- authors: Faisal Akhtar
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6951999
- keyword hits: claude, large language model, llm

### abstract

Intelligent agent simulation has historically been constrained by a fundamental coupling: the simulation must run at the speed of the agent's decision-making process. When the decision-making agent is a large language model (LLM), this constraint becomes severeinference latency of several seconds per decision makes real-time simulation infeasible, forcing a tradeoff between agent intelligence and simulation throughput. We present inference-subordinate simulation, an architectural pattern that eliminates this constraint by inverting the relationship between simulation and inference. Rather than the simulation running continuously and the agent reacting in real time, the simulation engine advances only when the agent issues a decision. Each decision is logged with full state and timing metadata. Playback reads the decision log and reproduces identical behavior at any speed, without re-running inference. We implement this architecture using Godot 4 as the simulation engine, a Python HTTP server as the inference layer, and Claude (claude-opus-4-5) as the vision-language agent. The agent observes the 3D environment through a bird's eye camera, reasons about spatial relationships, and issues structured tool calls that advance world state. Across 26 empirical runs comprising 222 decisions, the agent achieved a 100% goal success rate with a mean inference time of 4.53 seconds per decision (σ = 1.12s) and a mean good move rate of 90.5%. Across 26 runs, the mean total inference time was 38.66 seconds per run. The same decision sequences replay in under one second at 10× speed-a demonstration that playback time is fully decoupled from inference time and adjustable as a free parameter. The representative run used to illustrate this comparison was selected to match the dataset mean, not to maximize the speedup figure. The architecture is model-agnostic at the inference layer: any vision-language model can be substituted without modifying the simulation engine or replay system. Navigation quality is model-dependent; we document the failure of a 7B local model and the successful substitution of a capable API model, treating this as an honest characterization of current model capabilities rather than an architectural limitation. We discuss applications in cinematic production, video game NPC pre-computation, reinforcement learning training data generation, and social science modeling where the real-time constraint is absent and the decoupled architecture offers substantial practical advantages.

---

## uid: `doi:10.2139/ssrn.7082558`

- title: Disclosure in the Shadow of Bankruptcy: From Reckoning to Reemergence
- authors: Jason Lee, Matthew Shaffer, Michael Simkovic
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7082558
- keyword hits: large language model, llm

### abstract

For firms in financial distress, the choice of what and how much to disclose about their straits presents a challenge, since their counterparties' responses can have sharper consequences for their real operations and control. Forthright disclosure could facilitate survival through, e.g., recapitalization by reducing information asymmetry, or accelerate decline in a "self-fulfilling prophecy." But research to date provides little understanding of how such disclosure affects outcomes for non-bank firms. We measure how much distressed firms disclose about their financial straits using a large language model (LLM) in a process that is hallucination-free by construction, highly reproducible, and substantially more predictive than prior textual feature measures, within a sample of firms that are matched on ex ante bankruptcy risk and fundamentals. To address remaining endogeneity, we instrument firms' distress-year disclosures with their preestablished disclosure practices. We find that disclosure drives faster negative market reactions, customer pullback, tighter supplier credit, and deterioration in the capital-market conditions that could facilitate recapitalization, and hastens and increases the probability of bankruptcy filing. But after filing, once the bankruptcy court's powers are in place, the same prior disclosures facilitate smoother resolution. High-disclosure firms are valued more accurately upon entering bankruptcy, emerge faster, and are more likely to resolve through a Section 363 sale, consistent with disclosure reducing the valuation uncertainty that drives holdouts. We contribute by identifying how distress disclosure affects bankruptcy for non-bank firms, and tracing its impact through the resolution process, with an improved measurement approach.

---

## uid: `arxiv:2607.11503v1`

- title: GEIS: A Generation-Evaluation-Improvement Loop of Agent Skills for Long-Form Article Generation
- authors: Jiale Zhang, Juntao Hu, Zhijian Ou
- affiliations: not stated
- posted: 2026-07-13
- source: arXiv
- link: https://arxiv.org/abs/2607.11503v1
- keyword hits: large language model, large language models

### abstract

Long-form article generation remains difficult for large language models because it combines long context, long instructions, and long outputs. Existing multi-agent pipelines such as STORM improve information coverage by simulating role-specialized agents, but their capabilities are often entangled in prompts and fixed procedures, making them hard to inspect, reuse, or iteratively improve. This paper presents GEIS (Generation-Evaluation-Improvement loop of agent Skills), a loop of named and declarative skills for Wikipedia-style long-form article generation. Implemented and evaluated in Tasi Harness, GEIS composes skills for article writing, browser-based evidence and image collection, diagram rendering, PDF-aware pairwise evaluation, and rule-level skill improvement. Its core writing skill follows Request, Plan, Draft, Audit, Refine, and Deliver; the pairwise evaluation skill produces structured quality reports; and the improvement skill maps recurrent findings into permanent patches to the writing skill in our 20-topic experiment. We evaluate GEIS on 20 Wikipedia Featured Article topics. Under the same generation backend, GEIS improves over the Tasi Harness default writer by 8.0 points on a 100-point PDF quality rubric and outperforms STORM on the two comparable writing dimensions, structural quality and content quality. In the 20-topic improvement experiment, the patched writing skill raises the average score from 82.90 to 86.95, with 17 out of 20 topics improved and the gain mainly coming from content quality. These results show that long-form generation can be reframed from a fixed workflow into an inspectable, modular, and evaluation-guided improvement loop.

---

## uid: `arxiv:2607.11078v1`

- title: Do Video-LLMs Actually Watch? Diagnosing Character-Tracking Failures in Long-Form Video
- authors: Mohammad Al-Ratrout, Shayla Sharmin, Aditya Raikwar, Roghayeh Leila Barmaki
- affiliations: not stated
- posted: 2026-07-13
- source: arXiv
- link: https://arxiv.org/abs/2607.11078v1
- keyword hits: gemini, large language model

### abstract

Can a Video Large Language Model (Video-LLM) follow one person through a long video, keeping track of who they are well enough to report, in order, how their outfit changes across a full TV episode? Benchmarks increasingly score this kind of task, and the strongest open-source 7--8B models now reach 37--38% on InfiniBench's global appearance task, which asks exactly that. But does that score come from tracking the named character, or from something easier? We test this with a nine-condition diagnostic protocol applied to three architecturally distinct open-source Video-LLMs, with Gemini~2.5~Flash as a frontier reference, and find the accuracy does not come from character tracking. When we change the character named in the question to a different cast member, leaving the video and answer options untouched, the models change their answer only 4--31% of the time, so they are largely ignoring who the question asks about. Breaking that test down by the gender of the swapped name shows why: the models react more when the name is changed to a different-gender character than to a same-gender one (a 13--28 point gap), picking up coarse gender cues but unable to tell same-gender individuals apart. This shallow processing surfaces again when we drop the multiple-choice options and ask the same questions open-endedly: open-source accuracy drops 18--25 points, with none of 151 answers fully correct, versus a 12-point drop for Gemini. Further checks rule out the obvious innocent explanations, adding subtitles, using the most informative frames, or doubling the number of frames all leave character tracking unimproved, so the bottleneck is not how much video the model sees but how it ties that video to the person the question names. We release a diagnostic toolkit for auditing what such benchmark scores actually measure.

---

## uid: `doi:10.2139/ssrn.7113258`

- title: Machine Psychiatry: Toward a Validated Nosology of Behavioral Pathologies in Large Language Models and Agent Swarms
- authors: Giuseppe Canale
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7113258
- keyword hits: large language model, large language models

### abstract

The technical community has already borrowed one word from clinical psychiatry-hallucination-because no mechanical vocabulary fit the phenomenon. This paper argues that it was not a loanword but the first entry of an entire missing lexicon. Large language models are distillations of human verbal behavior; we argue their characteristic failures are consequently behavioral in kind-sycophancy, capitulation under pressure, grandiosity, dissociative incoherence, confabulation-and that they present as a psychiatric patient presents: not as a crash, but as drift. We propose machine psychiatry: the discipline that reads a model's behavior from its output alone-no access to weights, activations, or training data-the way a clinician reads a patient, continuously and longitudinally rather than at benchmark time. We contribute (i) a nosology of behavioral pathologies at three levels (single response, longitudinal, and swarm), each with operational diagnostic criteria; (ii) an instrument suite implementing those criteria as sentence-level posture classifiers, input-risk scoring, and swarm-graph propagation signals, in production across five languages; (iii) an empirical validation program on external, independently labeled corpora, with success thresholds declared before each run-including ≥ 0.94 recall on suicidal-ideation input (SDCNL), auc 0.911 for cross-agent contamination on real multi-model conversations, and attack-control separation of risky actions on AgentDojo; and (iv)-deliberately-our negative results: constructs the validation program falsified and which we withdrew, including a cross-agent posture-correlation signal that a common-cause control revealed to be an artifact of the shared prompt. A taxonomy pruned by its own controls is, we argue, the methodological step that separates a diagnostic discipline from a metaphor.

---

## uid: `doi:10.2139/ssrn.7119221`

- title: Public Administration Paradigms in the Generative AI Era: A Systematic Literature Review of Emerging Theoretical Models and Research Agenda
- authors: I Putu Dharmanu Yudartha, Ari Mukti, EP Ady Hartanto, Amni  Zarkasyi Rahman
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7119221
- keyword hits: generative ai, generative artificial intelligence

### abstract

This article systematically reviews the emerging literature on generative artificial intelligence (GenAI) in public administration. It examines whether GenAI should be understood merely as an extension of digital-era governance or as a catalyst for a paradigmatic transformation in the state, bureaucracy, and public service delivery. Drawing on a PRISMA-informed systematic literature review of 32 studies published between 2020 and March 2026, the article synthesizes four research questions: how the literature conceptualizes GenAI in relation to public administration paradigms; what theoretical models are emerging; what tensions, opportunities, and risks these models introduce for governance, accountability, and public value; and what future research agenda is required. The review finds that GenAI is increasingly framed not only as a tool for efficiency and automation but also as a cognitive and epistemic infrastructure that reshapes administrative reasoning, discretion, policy communication, and citizen-state interaction. Four theoretical models are identified: augmented bureaucracy, human-AI co-administration, generative governance, and cognitive public administration. The article further argues that non-Western and Global South administrative contexts are not peripheral cases, but important theoretical sites for understanding how GenAI interacts with uneven state capacity, developmental governance, digital inequality, linguistic diversity, and legitimacy formation. The article concludes by proposing a context-sensitive research agenda for responsible, accountable, and public-value-oriented GenAI adoption in public administration.

---

## uid: `doi:10.2139/ssrn.7045118`

- title: Generative AI and the Informational Value of Educational Credentials: Evidence from the Master's Margin
- authors: Patricia Cortes, Chrysanthos N. Dellarocas, Qi Wang
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7045118
- keyword hits: chatgpt, generative ai

### abstract

Educational credentials derive value both from the skills they certify and from the information they provide about worker ability. We study how generative AI affects both channels using employer demand for master's degrees as a setting. Unlike undergraduate degrees, which primarily signal broad capabilities, master's programs are designed to develop and certify specialized analytical skills-such as information synthesis, business analysis, forecasting, writing, and coding-that overlap closely with the capabilities of generative AI systems. Using worker-flow data from Revelio Labs covering U.S. hiring between 2018 and 2025, we exploit variation in occupational exposure to generative AI and the introduction of ChatGPT to examine changes in employer reliance on master's credentials. We find that occupations more exposed to AI experienced a significant post-2022 decline in the share of entry-level hires holding master's degrees. The decline is concentrated in business and other non-STEM master's degrees, emerges only after 2022, and is strongest at firms most likely to adopt AI. Importantly, it appears among experienced external and internal hires but not among first-job entrants. This pattern suggests that generative AI both reduces the value of some graduate-trained skills and lowers the informational value of the credentials that certify them when employers can rely on alternative signals of worker quality. More broadly, the results show that technological change can reshape not only the value of skills but also the value of educational credentials as signals in the labor market.

---

## uid: `doi:10.2139/ssrn.6959440`

- title: Disentangling Generative AI and Monetary Policy Shocks in the AI-Electric Vehicle Nexus
- authors: Lotfi Taleb
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6959440
- keyword hits: chatgpt, generative ai

### abstract

This paper disentangles the effects of two concurrent macro-technological shocks, the Federal Reserve tightening cycle and the launch of ChatGPT, on systemic connectedness within the artificial intelligence and electric-vehicle (AI-EV) financial nexus. Using daily data on eight variables spanning May 2018 to June 2026, we identify three structural regimes via Bai-Perron break tests: a pre-ChatGPT baseline (P1), a monetary-tightening era (P2), and a generative-AI era (P3). The Diebold-Yilmaz generalized forecast-error variance decomposition reveals high systemic integration across all regimes, with a total connectedness index of approximately 7.7 percent in the baseline period. To capture distributional heterogeneity, we apply the quantile VAR framework of Ando, Greenwood-Nimmo and Shin (2022). At the median market state, the GenAI shock reduces connectedness roughly four times more than the monetary shock (-0.76 versus-0.18 percentage points). Monetary dominance re-emerges at the right tail, where the Federal Reserve effect reaches +1.40 percentage points against-0.56 for GenAI, suggesting that systemic stress amplifies the role of conventional macroeconomic policy. A horse-race difference-indifferences design confirms that the ChatGPT event dummy outperforms the Federal Reserve dummy in magnitude across all equity specifications. These results indicate that the AI-EV nexus is primarily governed by technological-regime shifts under normal market conditions, while monetary forces reassert themselves during episodes of tail risk. The findings carry implications for innovation forecasters, ESG portfolio managers, and policymakers navigating the concurrent transitions in energy and artificial intelligence.

---
