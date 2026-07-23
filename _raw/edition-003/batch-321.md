# Classification batch 321 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-321.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6885378`

- title: Does Generative AI Enhance Liquidity of Cryptocurrency Markets? Theory and Evidence from ChatGPT Outages
- authors: Charles Cao, Wei Wang, Deli Yang
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6885378
- keyword hits: chatgpt, generative ai

### abstract

This study examines the impact of ChatGPT on trading volume, return volatility, and market liquidity in cryptocurrency markets. We analyze a key trade-off: while ChatGPT enhances information quality for individual traders, it impairs collective information production by introducing correlated noise. We develop a model and show that ChatGPT adoption enhances market liquidity but reduces trading volume and return volatility. Using ChatGPT outages as exogenous shocks and data from 70 cryptocurrency pairs, we find significant increases in trading volume (24%) and return volatility (19%), and significant deterioration in liquidity-book depth declines by 8% and price impact increases by 12% during outages. These results suggest that the adoption of ChatGPT reduces disagreement between traders and the market maker and mitigates adverse selection. The absence of significant changes in order imbalance is consistent with a correlated-noise channel and rules out alternative mechanisms that predict a dominant directional trading shift.

---

## uid: `doi:10.2139/ssrn.7003865`

- title: Measuring the DeFi Control Layer: Governance, Liquidations, and Lending Flows
- authors: Jasper Pan, Lebathong Dong
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7003865
- keyword hits: llama

### abstract

Decentralized finance (DeFi) is often defended as software rather than regulated intermediation. We examine whether functional control over DeFi applications can be measured directly by tracking address-level concentration in the channels through which sophisticated actors capture rents: governance over risk parameters, liquidations, lending flows, supplier spreads, MEV, and routing. From prior work on AMMs, MEV, lending, and DAO governance, we derive three predictions about how concentration should vary across channels, protocols, and applications. We test the predictions using six data sources: 1,142 risk-tagged Snapshot proposals across 15 governance spaces, $2.05 billion in liquidations across five lending markets, $569.4 billion in actor-level lending flows, DefiLlama rent series, a Uniswap v3 LP sample, and 250 Aave forum risk topics. The evidence supports all three predictions. Discretionary channels concentrate sharply but with protocol-level heterogeneity: the median top-five voting-power share across risk proposals is 96.0 percent, with Aave at 91.2 percent, Uniswap at 84.3 percent, and Radiant at 57.7 percent. Lending markets concentrate more than exchanges in governance, and Compound V3’s top liquidator captures 55.8 percent of volume while Aave V3 has 868 active liquidators. Within lending markets, the deposit base is broad while borrowing is narrow: the Aave V3 top-five borrow share is 84.8 percent against a 17.8 percent deposit share. We treat the evidence as channel-specific screening inputs rather than entity-level control findings, and discuss disclosure, registration, and safe-harbor implications.

---

## uid: `doi:10.2139/ssrn.7004505`

- title: Beyond AI Adoption: How Curiosity and Reflection Shape Innovative Behavior in Technology-Enabled Workplaces
- authors: Muhammad  Awais Khan
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7004505
- keyword hits: generative artificial intelligence

### abstract

Generative Artificial Intelligence (GenAI) is transforming contemporary workplaces, yet employees vary considerably in their ability to convert AI use into innovative outcomes. Addressing this gap, this study examines the psychological mechanism and boundary condition underlying the relationship between GenAI use and employee innovative behavior. Drawing on the Stimulus–Organism–Response framework and information-gap theory, we propose that work-related curiosity mediates the effect of GenAI use on innovation, while individual reflection strengthens this process. The proposed moderated mediation model was tested using multi-source supervisor–employee dyadic data from 315 employees and 72 supervisors working in project-based technology firms in an emerging economy. Covariance-based structural equation modeling and bootstrapping analyses revealed that GenAI use positively predicts both work-related curiosity and innovative behavior. Work-related curiosity partially mediates the relationship between GenAI use and innovation, indicating that GenAI stimulates innovation by fostering employees’ intrinsic motivation to explore, learn, and experiment. Furthermore, individual reflection positively moderates the effect of GenAI use on curiosity, such that the indirect effect of GenAI on innovative behavior is significantly stronger among highly reflective employees. By identifying curiosity as a critical motivational mechanism and reflection as an important dispositional boundary condition, this study advances understanding of how and when GenAI contributes to employee innovation. The findings extend AI-at-work research beyond instrumental explanations of technology use and provide evidence from an underexamined emerging-economy context. Practically, organizations can enhance innovation outcomes by promoting curiosity-oriented GenAI use and embedding reflective work practices.

---

## uid: `doi:10.2139/ssrn.6886378`

- title: Variance Geometry is Not Functional Geometry in Transformer Residual Streams
- authors: Ahmed Ghazouani
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6886378
- keyword hits: mistral

### abstract

\A common assumption in representation analysis is that the directions a transformer’s residual stream varies in most are the directions most important to its predictions. We show this fails geometrically. Measuring two operators on the same per-token activations in the same basis—the activation covariance CL (the object underlying PCA) and the empirical Fisher FˆL (a local output-sensitivity operator)—we find that where the top-5 subspaces of both are independently stable under sequence-level split-half bootstrap, all but one of their principal angles exceed 56◦ : the variance geometry and the sensitivity geometry are nearly orthogonal even when both are well-defined. A stricter, pre-specified resampling analysis that selects, per cell, the maximal subspace dimension at which both operators are reproducible extends this comparison to seven (model, layer) cells across all three architectures and reaches the same conclusion: every stable covariance–Fisher comparison has minimum principal angle above 56◦ . Variance rank is not functional rank, and the directions PCA recovers are not the directions perturbations propagate through. This orthogonality is supported by two further measurements across three architectures spanning 124M–7B parameters (Pythia-160M, GPT-2-small, Mistral-7B). First, a dimensionality mismatch on the same activations: activation covariance collapses to effective rank as low as 1.0 in mid-network layers, while the empirical Fisher remains broadly distributed at effective ranks of several hundred to over a thousand. Second, a direct perturbation test: at matched norm, residual-stream perturbations along the dominant Fisher direction cause 15–100× more KL divergence than perturbations along the dominant covariance direction, flipping the predicted next token 44% (Mistral-7B L31) to 96% (Pythia-160M L11) of the time versus 8–13% for covariance directions. A pre-specified rank-1 null hypothesis—that the dominant variance direction lies in the unembedding’s softmax-invariant subspace—is decisively refuted (pooled Spearman ρ = 0.02, n = 196). The low-rank side of this asymmetry, the covariance collapse, is the compression-valley phenomenon recently proved to follow from position-0 massive activations (Arroyo et al., 2025); we confirm it on the covariance operator and use it as the mechanistic account of the variance side, rather than claiming it as new. The high-rank side complements, rather than contradicts, the low effective dimensionality of the pointwise pullback-Fisher steering metric (Wang and Zhao, 2026): the population empirical Fisher, summed over tokens, occupies far more directions than either a single-point sensitivity metric or the activation covariance. The contribution we isolate is the relationship between the two operators— that variance-dominant and sensitivity-dominant geometry are reproducibly, measurably misaligned on the same residual stream.

---

## uid: `doi:10.2139/ssrn.6989978`

- title: Postulación de los prelados / Postulation of prelates (DCH)
- authors: Anna Clara Lehmann Martins
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6989978
- keyword hits: llama

### abstract

Spanish abstract: ¿Cómo se proveían los beneficios eclesiásticos en la América hispana y en las Filipinas durante la temprana modernidad? ¿Cómo se convertía en prelado un simple sacerdote? La postulación y la elección por órganos colegiados eran las formas típicas de provisión de prelaturas, según el Corpus iuris canonici . No obstante, en los territorios bajo el patronato regio español, el prelado no era elegido por un cabildo, sino presentado por el monarca. Esta artículo sigue de cerca las intrigantes modulaciones entre el derecho común y el derecho propio, en lo que atañe a la provisión de prelaturas (sobre todo los obispados) y otros beneficios en las Indias. Inicialmente se describen las principales características de la postulación y la elección, incluyendo los requisitos canónicos para elegir y ser elegido. A continuación, se expone en detalle el proceso de elección y confirmación episcopal según el derecho común, comparándolo con el de los superiores locales de las órdenes religiosas masculinas y femeninas. En el contexto de la América hispana y las Filipinas, se observa que, según el patronato real, la provisión de obispados se realizaba mediante un acto del monarca, la presentación, seguida de la institución del candidato, a encargo del pontífice, y su consagración. Lógica semejante se aplicaba a la provisión de canonjías y parroquias. En este último caso, una cuestión ampliamente debatida fue el acceso de mestizos e indígenas a beneficios con cura de almas. También se hacen consideraciones sobre la institución en cuanto libre colación, modalidad excepcional de llamamiento a beneficios en Indias. Finalmente se expone el paso de la investidura, mediante la cual se tomaba posesión del beneficio al que se había sido presentado e instituido. El artículo cierra un balance historiográfico. English abstract: How were ecclesiastical benefices filled in Hispanic America and the Philippines during the early modern period? How did an ordinary priest become a prelate? Postulation and election by collegiate bodies were the typical methods of filling prelates’ posts, according to the Corpus iuris canonici. However, in territories under Spanish royal patronage, the prelate was not elected by a chapter, but appointed by the monarch. This article closely examines the intriguing interplay between ius commune and ius proprium regarding the provision of prelacies (particularly bishoprics) and other benefices in the Indies. The article begins by describing the main characteristics of postulation and election, including the canonical requirements for electing and being elected. It then sets out in detail the process of episcopal election and confirmation under the ius commune , comparing it with that of the local superiors of male and female religious orders. In the context of Hispanic America and the Philippines, it is observed that the provision of bishoprics under royal patronage was carried out through an act of the monarch, the presentation, followed by the institution of the candidate, at the behest of the pontiff, and his consecration. A similar logic applied to the appointment of cathedral canons and parish priests. In the latter case, a widely debated issue was the access of mestizos and indigenous people to benefices involving the cure of souls. Consideration is also given to institution as free collation, an exceptional method of appointment to benefices in the Indies. Finally, the article outlines the investiture ceremony, through which the beneficiary took possession of the benefice to which he had been presented and instituted. The article concludes with a historiographical assessment.

---

## uid: `doi:10.2139/ssrn.7003669`

- title: Digital Divide or Digital Equaliser? Economic Status and the Access to ChatGPT Among Higher Education Students Worldwide
- authors: Sajjad Mahdavivand Fard
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7003669
- keyword hits: chatgpt, generative artificial intelligence

### abstract

The rapid uptake of generative artificial intelligence tools in higher education has reignited debate about whether emerging technologies narrow or widen socioeconomic inequalities. This study examines whether a student's economic background shapes how they access and benefit from ChatGPT and draws on data from 22,963 higher education students across 155 countries and territories. Three dimensions of AI-related inequality including version access (free vs. paid), usage intensity, and perceived educational benefit are examined. Self-reported economic status, financial aid receipt, and residential setting serve as the primary socioeconomic indicators. Findings from chi-square tests, One-way ANOVA, hierarchical regression, and bootstrapped mediation analysis show that economically advantaged students are more likely to hold paid subscriptions, use ChatGPT more intensively, and report greater perceived educational benefit. Version access partially mediates the relationship between economic status and perceived benefit. The interaction between economic status and residential setting on usage intensity was not statistically significant, indicating that the economic gradient in AI use operates consistently across geographic contexts. The results challenge the assumption that low-cost AI tools automatically democratise educational opportunity and point to version-tiered access as a structural mechanism of inequality that policy interventions in higher education have yet to address.

---

## uid: `arxiv:2607.19375v1`

- title: Economic Evaluations of Language Models
- authors: Alexander Wan, Stephane Hatgis-Kessell, Tomás Aguirre, Percy Liang, Rishi Bommasani
- affiliations: not stated
- posted: 2026-06-26
- source: arXiv
- link: https://arxiv.org/abs/2607.19375v1
- keyword hits: claude

### abstract

Language models perform economically valuable work, yet they are not currently assessed for how well they perform every economically valuable task. We introduce EconEvals as an open-source evaluation suite to measure capabilities relevant to tasks, work activities, and occupations in the US labor economy. We ground the evaluation suite in real user queries to language models where possible, and supplement these with synthetic data. Our evaluations improve coverage over OpenAI's GDPval benchmark, which is the existing state-of-the-art that covers 5% of US occupations, at 500x lower cost. Alongside benchmarks, we also introduce a simulation-based exposure measure to estimate how much time current language model capabilities could save across all tasks belonging to all US occupations, with detailed accounting for each estimate. Our estimates indicate that current models could save workers substantial time on at least half of their tasks in 47% of occupations. However, for 79% of tasks where we predict substantial time savings, observed Claude usage is low, suggesting that existing usage lags potential. Beyond inherent constraints of language model chatbots, our data identifies privacy and proprietary systems as the principal bottlenecks limiting further time savings from AI. Overall, we introduce adaptable infrastructure that grounds inferences about language models' labor-market impact in their current capabilities, which can be continually updated as capabilities improve.

---

## uid: `arxiv:2606.28471v1`

- title: Data and Evaluation Closed-Loop for Model Capability Enhancement
- authors: Zhixuan Li, Jiangan Yuan, Han Xu
- affiliations: not stated
- posted: 2026-06-26
- source: arXiv
- link: https://arxiv.org/abs/2606.28471v1
- keyword hits: llm

### abstract

Model capability is the central variable in LLM pre-training, yet is never observed directly: data shapes it prospectively, while evaluation reveals it only retrospectively, compressing samples, prompts, decoding, and scoring rules into one noisy score. Practical optimization runs this backward: a failure is observed first, and the engineer must infer the corpus fix. The two sides speak incompatible vocabularies -- benchmark names and per-sample correctness versus data sources, domains, and quality labels -- so this inference is usually intuition, not method. We close this gap with the \emph{capability slice}: a group of evaluation samples sharing background condition, task type, solving operation, and output constraint -- precise enough to localize a single weakness yet stable enough to survive aggregation, unlike a benchmark name, too coarse, or a single sample, too noisy. Built around this unit, an evaluation taxonomy, a non-instruction data taxonomy, and mapping rules form a closed loop turning a benchmark-level failure into a targeted, testable data intervention. We test this loop on two case studies pulling in opposite directions. First, the loop rules the data out: continued pre-training drives BBH down by $-46.82\%$, but diagnosis traces this to a single masked \texttt{\textless EOS\textgreater} loss rather than weakened reasoning; restoring it recovers BBH to $66.44$, above the original checkpoint, without changing the data. Second, the loop rules the data in: a persistent math-reasoning weakness is decomposed by solving operation into specific failing combinations, and a weakness-targeted sampling procedure built from it lifts AIME2025/AIME2026 Pass@128 from $6.67$/$0.00$ to $26.67$ each. The same unmodified loop reaches opposite, correct verdicts in both cases, showing the evaluation-to-data inference can be routine, auditable, and experimentally validated rather than intuitive.

---
