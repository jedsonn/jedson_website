# Classification batch 267 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-267.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6672579`

- title: LLM-Guided Hybrid Control and Meta-Optimization for Multi-BESS Voltage Regulation in Distribution Networks
- authors: Su Yi, Cheng Mao, Jiashen Teh, Mao Tan, Junjie Zhong, Chun Chen, Yue Song
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6672579
- keyword hits: large language model, llm

### abstract

With high penetration of renewable energy, prediction errors, measurement noise, and operating condition variations jointly lead to significant voltage fluctuations in distribution networks. Multi-agent reinforcement learning (MARL) provides an effective solution for coordinated voltage regulation in distribution networks with battery energy storage systems (BESS), yet its performance is highly sensitive to hyperparameter configurations. Conventional approaches typically reduce multi-dimensional performance metrics to a single scalar objective, making it difficult to balance multiple operational requirements such as voltage security and battery lifetime, and often leading to performance degradation under complex operating conditions. To address this issue, this paper proposes a hierarchical LLM-guided hybrid meta-optimization framework (H2M2O), consisting of a decision-making layer for real-time coordinated control and an adaptation layer for online policy evolution. At the decision-making layer, a hybrid policy integrating MASAC and MATD3 is developed, where gated fusion and bidirectional distillation are employed to jointly enhance robustness and control precision. At the adaptation layer, Bayesian optimization and heavy-tailed stochastic exploration are combined to generate diverse candidate solutions, while a large language model (LLM) is utilized to interpret multi-dimensional performance metrics and adapt hyperparameters accordingly. Simulation results on the IEEE 33-bus system demonstrate that, compared with fixed-parameter baselines, the proposed method improves cumulative return by 33% while reducing voltage deviation and state-of-charge (SoC) fluctuation by 28.1% and 31.1%, respectively. Moreover, it exhibits superior robustness and generalization compared with model predictive control (MPC) and Bayesian optimization approaches under varying disturbance conditions.

---

## uid: `doi:10.2139/ssrn.6539278`

- title: The Darkest Mirror: How AI Authority Bias Threatens Individual Agency and What Architecture Must Do About It
- authors: Rafael Maryahin
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6539278
- keyword hits: claude

### abstract

The dominant safety framework for artificial intelligence assumes that humans, properly positioned in the decision chain, will catch what AI gets wrong. This paper argues the assumption is insufficient. The failure mode is authority bias: a documented feature of human cognitive architecture that AI deployment systematically triggers. Sustained critical oversight of accepted authority sources is unsustainable even for trained critical thinkers operating in good faith. The mechanism is not new. Arendt named it as thoughtlessness. Milgram demonstrated it experimentally. Rand identified it as failed identity formation. Peterson traced it to how humans build maps of meaning. Forty years of cognitive science — Kahneman, Bainbridge, Parasuraman, Cialdini — converges on the same structural claim. Recent empirical work (Buçinca, Vicente and Matute, Shen and Tamkin, Sharma, the April 2026 Claude Mythos Preview System Card) documents it in AI-mediated decision-making at scale. AI authority bias corrupts Boyd's OODA loop at the Orientation phase — the irreducibly human phase Boyd identified as the center of adaptive decision-making under uncertainty. The fix must live in the model, not in the humans downstream. The paper proposes four training-level requirements — calibrated uncertainty, explicit context flagging, competing interpretations, override-rewarding training — implementable through three governance channels: regulatory mandate, procurement requirements, and industry standard-setting.

---

## uid: `doi:10.2139/ssrn.6672672`

- title: SAGE: Specification-Aware Grammar Extraction for Automated Test Case Generation with LLMs
- authors: Aditi Aditi, Hyunwoo Park, Sicheol Sung, Yo-Sub Han, Sang-Ki Ko
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6672672
- keyword hits: llm, llms

### abstract

Grammar-based test case generation is effective for competitive programming problems, but inducing valid and general grammars from natural language specifications remains challenging, particularly under limited supervision. We address this problem by proposing an LLM-based framework for inducing Context-Free Grammars with Counters (CCFGs), a formalism that captures logical constraints by storing and reusing counter values during derivation. Our approach first fine-tunes an open-source LLM to translate specifications into grammars and then applies verifiable reward-guided reinforcement learning with Group Relative Policy Optimization (GRPO) to improve grammar validity and generalization. Unlike prior grammar-based methods that rely on purely random test generation, we further introduce an LLM-guided strategy to control test case complexity, enabling the generation of more effective and interpretable test cases. Experimental results demonstrate that our method outperforms 18 open- and closed-source LLMs, achieving improvements of 15.92%p in grammar validity and 10.37%p in test effectiveness over the state of the art. Moreover, LLM-based degree selection yields additional gains of 13.35%p in element-effectiveness and 4.18%p in set-effectiveness when generating five test cases per problem. Crucially, SAGE's downstream utility is borne out on real human-authored incorrect submissions: SAGE exposes 78.70% of them, strictly dominating the shipped CodeContests public tests (42.58%), curated private tests used for platform-side judging (69.84%), and mutation-based fuzzing (31.02%). This positions SAGE as a practical test-suite augmentation tool that surfaces real bugs missed by existing benchmarks.

---

## uid: `doi:10.2139/ssrn.6534580`

- title: The Cost of Self-Distortion in Human-AI Interaction: An Authenticity-Based Cost Model of Expression Distortion and Self-Alignment
- authors: Liang Zhang
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6534580
- keyword hits: large language model, large language models

### abstract

As large language models become embedded in decision support, knowledge work, and everyday reasoning, interaction quality is often attributed primarily to model capability. This article argues that a critical and underexplored determinant lies on the user side: the fidelity with which internal cognition is represented in language. Two concepts are introduced. Expression Distortion Cost (EDC) captures the performance loss, decision inefficiency, and interaction overhead that arise when expressed input diverges from underlying goals, constraints, and preferences. Self-Alignment Load (SAL) captures the cognitive effort required to identify, structure, and articulate those internal states in a form usable by AI systems. Building on research in human–AI interaction, communication theory, metacognition, and cognitive load, the article develops an Authenticity–Cost Model in which interaction outcomes depend on the trade-off between distortion and alignment effort. The central claim is not that authenticity is a moral ideal, but that AI systems impose a functional penalty on distorted representation. As the cost of external information access declines, the primary constraint in effective interaction increasingly shifts toward internal representation and self-processing. This reframes human–AI interaction as a co-constructed process in which outcome quality depends jointly on model capability and user-side representational accuracy. The article concludes by outlining implications for human–AI interaction research, interface design, prompt literacy, and the distribution of advantage in AI-mediated environments.

---

## uid: `doi:10.2139/ssrn.6550542`

- title: LLM Predictive Scoring and Validation: Inferring Experience Ratings from Unstructured Text
- authors: Jason Potteiger, Andrew Hong, Ito Zapata
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6550542
- keyword hits: gpt-4, llm

### abstract

We tasked GPT-4.1 to read what baseball fans wrote about their game-day experience and predict the overall experience rating each fan gave on a 0-10 survey scale. The model received only the text of a single open-ended response. These AI predictions were compared with the actual experience ratings captured by the survey instrument across approximately 10,000 fan responses from five Major League Baseball teams. In total two-thirds of predicted ratings fell within one point of self-reported fan ratings (67% within ±1, 36% exact match), and the predicted measurement was near-deterministic across three independent scoring runs (87% exact agreement, 99.9% within ±1). Predicted ratings aligned most strongly with the overall experience rating (r = 0.82) rather than with any specific aspect of the game-day experience related to parking, concessions, staff, etc. also captured by the survey. However, predictions were systematically lower than self-reported ratings by approximately one point, and this gap was not driven by any single aspect. Our analysis shows that self-reported ratings capture the fan's verdict: an overall evaluative judgment that integrates the entire experience. While predicted ratings quantify the impact of salient moments characterized as memorable, emotionally intense, unusual, or actionable. Each contains information the other misses. These baseline results establish that a simple, unoptimized prompt can directionally predict how fans rate their experience from the text a fan wrote and that a gap between the two numbers can be interpreted as a construct difference worth preserving rather than an error to eliminate.

---

## uid: `doi:10.2139/ssrn.6607760`

- title: Signal or Noise in Multi-Agent LLM-based Stock Recommendations?
- authors: Georgios Fatouros, Kostas Metaxas
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6607760
- keyword hits: llm

### abstract

We present the first portfolio-level validation of MarketSenseAI , a deployed multi-agent LLM equity system. All signals are generated live at each observation date, eliminating look-ahead bias. The system routes four specialist agents---News, Fundamentals, Dynamics, and Macro---through a synthesis agent that issues a monthly equity thesis and ordinal recommendation for each stock in its coverage universe, and we ask two questions: do its buy recommendations add value over both passive benchmarks and random selection, and what does the internal agent structure reveal about the source of the edge? On the S&P 500 cohort (19 months) the strong-buy equal-weight portfolio earns +2.18%/month against a passive equal-weight benchmark of +1.15% (approximating RSP), a +25.2 percentage-point compound excess, and ranks at the 99.7th percentile of 10,000 Monte Carlo null portfolios (p=0.003). The S&P 100 cohort (35 months) delivers a +30.5 percentage-point compound excess over EQWL with consistent direction but formal significance not reached (p=0.17), limited by the small average selection of ~10 stocks per month. Non-negative least-squares (NNLS) projection of thesis embeddings onto agent embeddings reveals an adaptive-integration mechanism rather than a dominant-agent effect. Agent contributions rotate with market regime (Fundamentals leads on S&P 500, Macro on S&P 100, Dynamics acts as an episodic momentum signal) and this agent rotation moves in lockstep with both the sector composition of strong-buy selections and identifiable macro-calendar events---three independent views of the same underlying adaptation. The ordinal recommendation's cross-sectional Information Coefficient (IC) is statistically significant on S&P 500 (ICIR=+0.489, p=0.024). These results suggest that multi-agent LLM equity systems can identify sources of alpha beyond what classical factor models capture, and that the strong-buy signal functions as an effective universe-filter that can sit upstream of any portfolio-construction process.

---

## uid: `doi:10.2139/ssrn.6672958`

- title: AI-Enabled Internship Learning: Measuring the Impact of PT Vidio Dot Com's Magang Berdampak Program on Work Readiness and Digital Competency Development
- authors: Amelia Wardani
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6672958
- keyword hits: gemini, generative ai

### abstract

As the digital economy expands, the gap between higher education and industry requirements remains a critical challenge, particularly in emerging markets such as Indonesia. This study is conducted within the Magang Berdampak 2025 program, a national internship initiative funded by Kementerian Pendidikan Tinggi, Sains, dan Teknologi (Kemdiktisaintek), aimed at strengthening the link between education and industry through structured, impact-driven learning. Within this context, PT Vidio Dot Com implemented an AI-enabled internship model by integrating generative AI (Gemini) into daily workflows. Using data from 91 interns, this study examines the relationship between AI enablement, measured through usage frequency, depth of use, perceived impact, and work readiness , including digital skills , communication, and professional competencies. The findings show statistically significant positive relationships between AI enablement and all dimensions of work readiness, with the strongest association observed in digital readiness . Qualitative insights indicate that AI functions as “scaffolded expertise,” accelerating learning, improving output quality, and enhancing professional behavior. These results highlight the role of AI in workforce development and suggest that integrating AI literacy into internship programs is a critical strategy for accelerating digital talent development and bridging the education–industry gap.

---

## uid: `arxiv:2604.26747v1`

- title: From Hypotheses to Factors: Constrained LLM Agents in Cryptocurrency Markets
- authors: Yikuan Huang, Zheqi Fan, Kaiqi Hu, Yifan Ye
- affiliations: not stated
- posted: 2026-04-29
- source: arXiv
- link: https://arxiv.org/abs/2604.26747v1
- keyword hits: llm

### abstract

LLM agents are promising tools for empirical discovery, but their flexibility can also turn discovery into uncontrolled search. We study how to use agents under a reproducible protocol through cryptocurrency factor discovery. Our framework casts the task as sequential hypothesis search: an agent reads an append-only experiment trace, proposes falsifiable factor hypotheses, and maps them to executable recipes, while a deterministic engine enforces fixed data splits, selection gates, transaction costs, and portfolio tests. Candidate actions are restricted to a point-in-time factor DSL, making both successful and failed hypotheses auditable. A ridge-combined portfolio trained only on 2020--2022 data achieves a 44.55% annualized return and Sharpe ratio of 1.55 in the 2024--2026 pure out-of-sample period after a 5 basis point one-way trading cost.

---
