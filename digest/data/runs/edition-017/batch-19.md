# Classification batch 19 of 20, edition 17

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-017/batch-19.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7214044`

- title: Carbon-intensity scheduling delivers greater climate benefit thanincremental code-level energy reductions
- authors: Michael Bane
- affiliations: not stated
- posted: 2026-08-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7214044
- keyword hits: generative ai, large language model, large language models

### abstract

Climate change is upon us and it is imperative to take action to reduce carbon emissions. Computing, and particularly generative AI, is a key contributor with its emission rate soaring due to training large language models and the ubiquitous integration of AI. Advocates such as the Green Software Foundation highlight how computing is part of the climate problem, and suggest ways to reduce its carbon footprint. This includes reducing the energy of a task, with people looking at CPU and GPU clock frequencies and reducing the precision of arithmetic. A second approach is to reduce the carbon for a given workload via ”shifting”. Since some electricity is greener, depending on the renewable-to-fossilmix, it is possible to reduce emissions by shifting in time and space. The amount of carbon emissions a unit of electricity is responsible for is its carbon intensity, which we show to be a key factor in sustainable computing.This work examines reducing the carbon footprint of computational matrix operations. We examine choices of compiler optimisations, computing languages, and numerical libraries. We compare these with savings due to the dynamic nature of CI via scheduling of where and when computation is undertaken. We find that careful choice of Implementation and Deployment yields an energy saving factor of 51, whereas shifting yields a further carbon saving factor of 354x. Our real case example illustrates carbon savings of over 7750x compared to a given baseline, and we provide key insights and recommendations for code developers, users, and policy makers.

---

## uid: `doi:10.2139/ssrn.7212519`

- title: Talking to Digital Twins: Selective Disclosure and Belief Measurement in Financial Social Media
- authors: Boone Bowles, Raymond M. Duch, Sorin M. Sorescu
- affiliations: not stated
- posted: 2026-08-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7212519
- keyword hits: llm, llms

### abstract

Social media affect financial markets, but public posts by financial media personas are voluntary disclosures. What is not disclosed is therefore usually unobserved. We address this measurement problem by conducting repeated, real-time interviews of "digital twins" built from monitored finfluencers' X accounts under a fixed protocol. The interviews recover stocklevel public-persona belief proxies even when no public recommendation is made. Because the interviews are generated and archived before the relevant return windows, the design avoids the look-ahead bias that arises when LLMs are queried ex post. The evidence shows that information obtained from these digital-twin interviews predicts the cross section of large-cap stock returns in the expected direction. Repeated real-time interviews therefore show how selective disclosure can be turned into measurable panels of market views.

---

## uid: `doi:10.2139/ssrn.7134419`

- title: The Adaptive Sovereign Balance Framework Under Transfer: A Second Pilot Application to Chile, 2005–2023
- authors: Orken Dinassilov
- affiliations: not stated
- posted: 2026-08-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7134419
- keyword hits: claude, large language model, large language models

### abstract

This paper tests whether the Adaptive Sovereign Balance Framework (ASBF) — introduced as a diagnostic of the sovereign balance's functional configuration in a companion paper on Kazakhstan (2005-2023) — reproduces under transfer to a second commodity-dependent economy, Chile (2005-2023). The five-contour architecture, the F/V/D/R operationalisation chain, and the two-index diagnostic plane (SVI^S , SVI^P) carry over structurally unchanged. Three lines of evidence are assessed. Statistical discrimination of SVI^P between stress and calm years does not reach significance at the available sample size (Mann-Whitney p=0.368; Fisher exact p=0.758; permutation p=0.195; n=16) — a result attributed to a smaller and more heterogeneous shock sample than Kazakhstan's, not to a failure of the diagnostic object itself. Lag-time comparison against IMF Article IV assessments across three episodes shows SVI^P registering positive pressure ahead of each crisis, including a signal-year value (+1.16, 2007) closely matching Kazakhstan's (+1.020). Robustness checks — an honest out-of-sample test (5 of 5 years, 2019-2023) and a crosscountry panel check (14 of 16 years) — probe distinct vulnerabilities of the weighting construction and both return negative for overfitting. The paper also identifies an unresolved methodological fork: Chile's and Kazakhstan's contour weights are computed by different normalisation formulas, which leaves one of Article 1's central predictions untestable until comparability is established. The transfer is read as necessary but not sufficient evidence for generalisability, bounded to the class of small open economies with a sovereign fund of comparable function. Large language models (Claude, Anthropic) were used to assist with drafting, language editing, and calculation cross-checking, while the research design, theoretical framework, and all substantive conclusions are the author’s own.

---

## uid: `arxiv:2608.00761v1`

- title: AI and Exchange Rate Predictability
- authors: Amin Izadyar
- affiliations: not stated
- posted: 2026-08-01
- source: arXiv
- link: https://arxiv.org/abs/2608.00761v1
- keyword hits: chatgpt, deepseek, generative artificial intelligence

### abstract

I revisit the exchange rate disconnect puzzle, first documented by Meese and Rogoff (1983), using generative artificial intelligence (AI) to forecast currency returns based on economic fundamentals. Using ChatGPT and DeepSeek, I analyze a comprehensive dataset of economic data releases for major currency pairs and measure the fundamental strength of each currency. These AI-powered fundamentals exhibit significant cross-sectional predictive power. A simple trading strategy that goes long currencies with strong fundamentals and short currencies with weak fundamentals generates a Sharpe ratio exceeding 0.7 per annum. The excess returns of this strategy remain significant after controlling for traditional currency factors. To mitigate concerns of look-ahead bias, I run multiple exercises to ensure that predictability stems from AI reasoning rather than memorization. Finally, I explore the potential sources of predictability and find evidence that the Taylor rule framework, generally used by central banks to set interest rates, is a key mechanism connecting exchange rates to economic fundamentals.

---

## uid: `arxiv:2608.00711v1`

- title: Tracing the Cascade: A Topology-Aware Evaluation Framework for Scientific Agent Hallucinations
- authors: Xinshun Feng, Ziqi Miao, Lijun Li, Jing Shao
- affiliations: not stated
- posted: 2026-08-01
- source: arXiv
- link: https://arxiv.org/abs/2608.00711v1
- keyword hits: large language model, llm

### abstract

Large language model (LLM) agents are increasingly deployed in scientific research, where reliability is critical and the underlying knowledge is densely interconnected. In such settings, hallucinations are particularly damaging: a single erroneous claim on a foundational concept can propagate through multi-step reasoning and corrupt entire trajectories. Existing hallucination benchmarks largely operate at the surface level, treating facts in isolation and relying on uniform accuracy metrics that ignore this topological structure. We address this gap with SCHEMA, the first evidence-grounded, topology-aware evaluation framework for hallucinations in scientific agents. SCHEMA automatically constructs scientific concept graphs from benchmark seeds and literature evidence, synthesizes graph-grounded tasks spanning claim verification, multi-hop reasoning, open-ended explanation, and experimental code generation, and evaluates agents with two complementary diagnostics. A trajectory hallucination pipeline audits intermediate reasoning at scale via a topology-weighted severity score, while a multi-agent counterfactual attribution module pinpoints the causal mechanism behind selected failures. SCHEMA reveals that hallucinations concentrate at a small set of highly connected knowledge hubs, and that final-answer accuracy decouples from trajectory honesty; models often reach correct conclusions through structurally flawed reasoning. These results indicate that for high-stakes scientific applications, terminal accuracy alone is an insufficient signal of agent reliability, motivating mechanism-level evaluation grounded in knowledge topology. Code is available at https://github.com/circles-post/SCHEMA.

---

## uid: `arxiv:2608.00473v1`

- title: CrossProjection: Geometric Grounding Beyond Viewpoint Change in Architectural Drawings
- authors: Kaho Li, Pengyu Zeng, Yuqin Dai, Jun Yin, Tianjing Feng, Shuai Lu
- affiliations: not stated
- posted: 2026-08-01
- source: arXiv
- link: https://arxiv.org/abs/2608.00473v1
- keyword hits: gpt-5, qwen

### abstract

Architectural drawings violate the usual assumption behind multi-view reasoning: plans and sections are cuts, while elevations are facade projections, so corresponding components change appearance in ways camera motion cannot explain. We introduce CrossProjection, an anchor-grounded diagnostic of whether vision-language models preserve component identity and externalize geometry across heterogeneous architectural views. It evaluates Matching, Registration, and Geometric Grounding through categorical judgments, candidate selection, and free point, line, and region localization. Across 23 real drawing sets and 1,954 categorical conditions per model, GPT-5.5 scores 82.4%, Qwen3-VL-32B-Instruct 62.2%, and GLM-4.5V 57.2%. A matched 200-target study crosses natural and vector-text-suppressed drawings with closed-candidate and free-geometry outputs. Candidate-supported performance is often higher, but free localization remains fragile: on natural drawings, point/region PCK@.05 is 54-76% for GPT, 8-10% for Qwen, and 14-36% for GLM; line endpoint PCK@.05 is 22%, 4%, and 0%. A coordinate grid recovers some GPT point/region precision but not lines. Three architecture-trained participants reach 87.3-93.3% categorical accuracy and 76-92% GT-region hit, supporting task feasibility rather than a population-level human ceiling. Because the categorical families do not form a same-item Matching-Registration contrast and interface controls alter multiple burdens, we avoid mechanistic claims. The supported conclusion is narrower: closed-choice or marked-element success does not entail reliable explicit geometric grounding. For drawing-guided CAD/BIM systems, categorical correctness should not be treated as evidence of candidate-free spatial reliability. Reusable on-sheet anchors, fixed-denominator scoring, and hash-locked artifacts establish an audit trail for this gap.

---

## uid: `doi:10.2139/ssrn.7216428`

- title: Constraint-Faithful Floor Plan Generation Framework Based on Domain-Specific Tokens and Reinforcement Learning with Verifiable Rewards
- authors: Jonghwa Shim, Eunbeen Kim, Eenjun Hwang
- affiliations: not stated
- posted: 2026-08-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7216428
- keyword hits: large language model, llm

### abstract

Conditional floor plan generation must satisfy constraints comprising user-specified input conditions and design rules. Existing large language model (LLM)-based methods encode floor plans with general text tokens not optimized for this task or apply reinforcement learning (RL) with only one or two coarse sequence-level rewards, failing to generate constraint-faithful floor plans. This work proposes FloorplanLLM, a framework based on domain-specific tokens and RL with verifiable rewards. Floor plan-specific custom tokens are incorporated into the pretrained LLM vocabulary, and floor plans are represented as sequences of these tokens to reduce reliance on general text tokens. Verifiable reward functions evaluate constraint satisfaction in generated floor plans, aligning the LLM to diverse constraints during RL. Token-level credit assignment differentiates reward signals across tokens according to their contribution. Comparative experiments demonstrate approximately 70% higher floor plan quality and more realistic, constraint-faithful plans than existing methods. Ablation studies confirm the contributions of each component.

---

## uid: `doi:10.2139/ssrn.7192452`

- title: Variational Autoencoders for Pose Estimation and Emotion Recognition: A Survey and Healthcare Perspectives
- authors: Huilin Ren, Lei Chen, Dan Wu, Bochao Su, Dongjun Zhang, Qianghua Liao, Minzhi Deng, Xing Zhang
- affiliations: not stated
- posted: 2026-08-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7192452
- keyword hits: large language model, large language models

### abstract

Human pose estimation and emotion recognition are two fundamental tasks in human-centric sensing, with broad applications in intelligent surveillance, human–computer interaction, and healthcare. Among deep generative models, the Variational Autoencoder (VAE) stands out for its principled probabilistic framework, interpretable latent space, and flexible generative capability. These properties make it well suited to shared challenges in both domains, including inherent ambiguity, data scarcity, and cross-domain generalization. However, existing surveys address these domains in isolation—reviewing either pose estimation methods or emotion recognition methods without a VAE-specific lens—thereby overlooking the structural parallels in how VAE is exploited across both fields and their shared healthcare implications. This paper addresses this gap with a comprehensive, VAE-centric survey spanning both fields. We construct a unified taxonomy of VAE variants, review their applications across diverse pose estimation and emotion recognition sub-tasks, and distill a key finding: despite the apparent disparity between the two domains, VAE serves structurally analogous roles in both—representation learning, data augmentation, factor disentanglement, and domain adaptation. This methodological unity naturally extends toward healthcare, where VAE-enabled pose analysis and affective computing converge to support clinical assessment and mental health monitoring. We further chart a future roadmap positioning VAE as an enduring component for continuous health monitoring and large-scale medical applications, through integration with diffusion models, large language models, and federated learning.

---
