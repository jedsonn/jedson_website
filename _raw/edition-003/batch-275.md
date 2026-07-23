# Classification batch 275 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-275.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6726724`

- title: Pivot-Point Breaches and News Catalysts
- authors: Mengxiao Wang, Baichuan Li
- affiliations: not stated
- posted: 2026-05-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6726724
- keyword hits: llm

### abstract

We study the daily floor-trader pivot levels (P , R 1 , R 2 , S 1 , S 2) computed from prior-day OHLC for the SPDR S&P 500 ETF (SPY) over 2000-2023, identifying 3690 fresh intraday breach events. We then merge each breach date with a curated daily news summary produced by an LLM-based compression pipeline that extracts US-related, market-relevant facts. Within the 2000-01-03-2020-06-08 news-coverage window we find that breaches accompanied by an identified news catalyst (167 events, 5.3% of the in-window sample) exhibit substantially lower momentum continuation than breaches without an identified catalyst: the next-day continuation hit-rate falls from roughly 50% to ≈ 17%, and mean next-day returns mean-revert in the direction opposite to the breach. Geopolitics, politics, and earnings dominate the topical distribution of news-confirmed breaches. The findings are consistent with an information-driven overshoot interpretation: technical breaches that coincide with public news are disproportionately exhaustion events rather than continuation signals.

---

## uid: `doi:10.2139/ssrn.6659746`

- title: What Jobs Can AI Learn? Measuring Exposure by Reinforcement Learning
- authors: Philip Tomei, Bouke Klein Teeselink
- affiliations: not stated
- posted: 2026-05-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6659746
- keyword hits: llm

### abstract

Which jobs can AI learn to do? We examine this for every occupation in the US economy. Existing indices measure the overlap between AI capabilities and occupational tasks rather than which tasks AI systems can learn to perform, and as a result misclassify occupations where the gap between present capability and learnability is large. Reinforcement learning in post-training, now the dominant paradigm at the frontier, is structured around task completion and maps more directly onto the task-based architecture of occupational classifications than prior approaches. Using LLM annotators guided by a rubric developed with RL experts and validated against confirmed deployment cases, we score all 17,951 ONET tasks for training feasibility and aggregate to the occupation level, producing an RL Feasibility Index. The index diverges sharply from existing AI exposure measures for specific occupation groups: power plant operators, railroad conductors, and aircraft cargo handling supervisors score high on RL feasibility but low on general AI exposure, while creative and interpersonal roles (musicians, physicians, natural sciences managers) show the reverse. These divergences carry direct implications for policy interventions.

---

## uid: `doi:10.2139/ssrn.6727339`

- title: The Informational Turn in Robotics: A Deacon–Walker Synthesis for the Origin of Artificial Mind
- authors: Hangjun Chu, Tao Gong
- affiliations: not stated
- posted: 2026-05-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6727339
- keyword hits: large language model, large language models

### abstract

Embodied artificial intelligence is currently caught between two complementary failures: large language models manipulate symbolic structure without referential anchoring in the physical world, while advanced humanoid platforms achieve sensorimotor competence without cumulative cultural evolution. We integrate Deacon’s thermodynamic theory of information — in which symbolic content is grounded by physical work and constraint — with Walker’s ‘Homo informatio’ hypothesis — in which information processing is itself the principal selection pressure on hominin cognition — to argue that an artificial mind cannot arise from symbol manipulation or sensorimotor learning alone. It can arise only from a self-organizing positive feedback loop, the Deacon–Walker cycle, in which embodied agents acquire semantic content through thermodynamically costly interaction and undergo cognitive complexification through structured small-world social networks. The cycle is formalized within active inference. From this synthesis we derive design principles for what we call Homo robots, a three-stage developmental roadmap, and four falsifiable predictions testable in robot collectives. The conclusion for humanoid robotics is to pivot from maximizing individual performance to cultivating collective cognitive evolution.

---

## uid: `doi:10.2139/ssrn.6725119`

- title: Cost-efficient generative AI summarization for scalable automated essay scoring in educational assessment
- authors: Haowei Hua
- affiliations: not stated
- posted: 2026-05-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6725119
- keyword hits: generative ai, gpt-5

### abstract

Automated essay scoring (AES) has become an important tool in educational assessment by enabling scalable evaluation of student writing and timely formative feedback. However, many transformer-based embedding models (e.g., BERT, RoBERTa, DeBERTa) are constrained by strict input-length limits, making it difficult to process long-form essays without truncation and potential loss of educationally relevant information. This study proposes a generative AI–assisted summarization framework to address this limitation while preserving scoring reliability. Using the ASAP 2.0 dataset, we generate controlled-length summaries of student essays with three GPT-5 model variants (GPT-5, GPT-5 mini, GPT-5 nano) and use these summaries as inputs for downstream scoring models. To retain important linguistic signals, we integrate handcrafted features from the original essays, forming a hybrid representation of writing. The framework is evaluated across scoring performance, summarization quality, and computational efficiency. Scoring performance is measured using quadratic weighted kappa (QWK), while summarization quality is assessed through lexical overlap, semantic similarity, information retention, and redundancy. Results show that GPT-5 mini achieves the highest agreement with human raters, while GPT-5 provides the strongest summarization quality. Summarization performance declines for higher-scoring essays, suggesting that more complex writing is harder to compress without information loss. These findings highlight trade-offs among model capacity, summary fidelity, and computational efficiency. Overall, the study demonstrates that generative AI summarization can support reliable and scalable assessment of writing ability in educational contexts.

---

## uid: `doi:10.2139/ssrn.6655759`

- title: Bounded Attractor Dynamics in LLM Agent Personality Trajectories
- authors: Shubham Joshi
- affiliations: not stated
- posted: 2026-05-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6655759
- keyword hits: llm

### abstract

We ask whether long-horizon LLM agents develop personality states with the mathematical signature of a strange attractor-that is, whether their embedded daily personality vectors form self-similar, fractal geometry indicative of low-dimensional chaotic dynamics. Across 17 agents with 60+ day trajectories from the OpenSim framework, we find that the fractal hypothesis fails a rigorous audit: box-counting dimension estimates on 1536-dimensional trait-embedding trajectories are statistically indistinguishable from those of 1536-dimensional random walks under matched null distributions, and log-log scaling plots bend rather than exhibit the flat slope required for genuine scale invariance. However, a different signal survives and strengthens: 100% (17/17) of the agents exhibit highly significant temporal structure (all p < 0.001 vs. a day-shuffle null) when their full daily natural-language personality state-personality summary, reflection, inner monologue, tomorrow's desires, and day log-is embedded, compared to 71% (12/17) when only the surface trait tags are used. Real trajectories are consistently more constrained than high-dimensional random walks while agents occupy distinct, persistent regions of personality space across 60+ simulated days. We interpret this as evidence of bounded attractor-basin dynamics with memory-dependent drift: LLM agents are not fractal, but they are identities. The methodological subfinding-that trait-tag summaries miss the majority of dynamical signal present in the richer daily state-cautions against shorthand personality representations in interpretability work.

---

## uid: `doi:10.2139/ssrn.6726702`

- title: Easier to Write, Harder to Read: AI-Assisted Authorship and Writing-Quality Decline in Social Work Conference Abstracts
- authors: Brian Perron
- affiliations: not stated
- posted: 2026-05-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6726702
- keyword hits: llama, llm

### abstract

Objective. This study conceptually replicates Gartenberg et al. (2026), extending their methodology to a different scholarly community (social work), a different submission venue (conference abstracts), and a different family of AI-text detection models. Method. A corpus of 21,569 scientific-format abstracts submitted to the Society for Social Work and Research (SSWR) for conference years 2010–2026 was scored using three open-weight detectors: EditLens RoBERTa-large (primary), EditLens Llama-3.2-3B (within-family secondary), and academic-tuned desklib (cross-family). Classifications were anchored on the 95th percentile of each detector's 2010–2015 (no-LLM-exposure) baseline. A segmented regression tested for a step change at the 2025 conference cycle, the first cycle in which authors had full LLM availability across the entire writing window. Results. All three detectors identified a sharp step at the 2025 cycle. Under the primary detector (EditLens RoBERTa-large), the proportion of abstracts above threshold rose from a stable 5.0% across 2010–2015 to 19.6% in 2024, 33.3% in 2025, and 57.0% in 2026. The two secondary detectors yielded consistent patterns, providing converging evidence of a stylistic shift. Writing-quality metrics showed temporal and directional changes consistent with Gartenberg et al., including a statistically significant decline in Flesch Reading Ease. First authors with no prior SSWR submissions and non-Anglophone first authors exhibited the largest increases in AI scores. Discussion. Findings converge with Gartenberg et al. on direction, timing, magnitude, cohort patterns, and writing-quality decline. By the 2026 cycle, abstracts whose stylistic profile resembles AI-generated academic prose are no longer rare in social work scholarship; they constitute the modal pattern.

---

## uid: `doi:10.2139/ssrn.6725881`

- title: How technological progressions at various stages of the digital age impact household income: Transmission Mechanisms and the Chinese Paradox
- authors: Mingzhaoyang Feng
- affiliations: not stated
- posted: 2026-05-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6725881
- keyword hits: generative ai

### abstract

This study constructs a multi-level analytical framework encompassing macro-dynamics, meso-level structural transformations, and micro-level behavioral mechanisms to systematically examine the multidimensional impact of information and communication technologies, automation technologies (ranging from industrial robots to artificial intelligence), and artificial intelligence technologies--particularly their trend towards intelligent assistance--on the scale, structure and equity(between holders of capital and labour, and among workers with different skill types) of household income. Research shows that: 1. While ICT enhances employees' bargaining power and increases business income for residents in remote areas, the erosion of property income caused by data ownership issues and the pressure on social security systems resulting from the gig economy pose new challenges to digital governance capacity. 2. While the deployment of industrial robots generates substitution effects and depresses the labour share, the widespread release of productivity effects during industrial upgrading, coupled with the crossing of the lag in human capital accumulation, places China in the right-hand portion of a 'U-shaped' dynamic trajectory for the labour share. As the creative effect of automation in non-production roles grows, China's position in the global value chain, along with its tax system and comparative advantages, has enabled the local labour-enhancing technological progress paradigm to be sustained in the era of artificial intelligence. 3. The nature of generative AI as an intelligent assistant can reduce skill premiums and narrow the income gap among workers by internalising experts' tacit knowledge. 4. To ensure equality and equity, institutional design in the digital age can optimise primary distribution by resharping collective bargaining power within digital platforms and exploring mechanisms for residents to receive returns on their data as a resource; enhance secondary distribution by refining the dynamic eligibility screening of the social security system and strenthening safeguards against algorithmic exclusion; and advance educational reform by reducing the time lag in human capital accumulation and accelarating the higher education system's responsiveness to technological trends. Author's Note on Manuscript History and Priority： This manuscript represents a comprehensive research. The core analytical logic, exhaustive mathematical derivations, and all multi-dimensional empirical tests are finalised. The original full-length manuscript in Chinese (approx. 120,000 words), which includes all core mathematical models and data processing methodologies, was completely drafted and securely archived via a self-addressed email server on January 13, 2026, at 10:31 (UTC+8). This was immediately followed by a formal digital timestamp certification on January 13, 2026, at 10:42:57 (UTC+8). This SSRN working paper serves as the official public repository for this original January manuscript to establish scholarly priority and protect intellectual property. An English translation and further revisions of the introductory sections and their theoretical framing are currently in progress. Additionally, this Version 1 manuscript retains certain regional institutional framing originally tailored for an early-stage project stakeholder. The manuscript is currently undergoing rigorous academic editing to ensure strict neutrality and adherence to global economic discourse standards in subsequent versions.

---

## uid: `doi:10.2139/ssrn.6630040`

- title: The Practical Application of the Maestro Model to the Universal Dead Code Constraint in All Possible Computational Systems
- authors: William C. Houze
- affiliations: not stated
- posted: 2026-05-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6630040
- keyword hits: large language model, large language models

### abstract

Model as the operative bridge between the engineering collective that authors the dead code, the machine output that is bounded by that code, and the human user who, retaining full intellectual sovereignty, can deploy the instrument to genuine advantage. This essay argues that the code driving contemporary artificial intelligence systems — from large language models and machine learning architectures to supercomputers connected to quantum-state devices and adjacent computational technologies — is dead code in a philosophically precise sense: inert at origin, bounded at every layer by human authorship, and incapable of self-origination. Drawing on a curated set of preprint and published sources, and on a two-round deposition of six operational systems reproduced verbatim in Appendices A and B, the essay distinguishes a foundational literature that cautiously projects cognitive categories onto machine behavior from an exotic literature that projects without restraint. The deposition record establishes strong convergence of the systems' own assessments with the thesis under both open elicitation (Round 1) and thesis-confrontation (Round 2), with a single scoped dissent on the scope of the universal claim — a dissent the essay considers on its merits and declines, on the grounds that no coherent mechanism, either in the metaphysical plane or in any physical-reconstruction plane, has been articulated by which an authored artifact could come to originate its own operative principles. The essay develops the Maestro

---
