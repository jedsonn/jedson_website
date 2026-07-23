# Classification batch 206 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-206.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6913339`

- title: Inside the Odds
- authors: Nizan Geslevich Packin, Maya O Shaton, Elior Sulem, Sharon Rabinovitz
- affiliations: not stated
- posted: 2026-06-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6913339
- keyword hits: llm, prompting

### abstract

Here is the abstract trimmed to land at 5,000 characters while changing as little as possible: Prediction markets have rapidly moved from regulatory fringe to consequential financial infrastructure, yet the doctrinal and empirical foundations for governing insider trading in these markets remain underdeveloped. This Article argues that the mainstreaming of prediction markets, accelerated by shifts in administrative law and judicial decisions permitting regulated platforms to expand, has produced insider trading risks that neither securities law nor gambling law is equipped to address. Those risks became concrete in January 2026, when a Polymarket trade placed shortly before the U.S. military detention of Venezuelan President Nicolás Maduro, and later geopolitical wagers tied to escalation risks involving Iran, triggered allegations of trading on privileged information and immediate legislative scrutiny. The episode exposed the absence of a coherent legal framework governing informational trading, compounded by ongoing uncertainty over classification. Although prediction markets operate as event contracts under the Commodity Exchange Act within the jurisdiction of the Commodity Futures Trading Commission, state courts have increasingly treated them as unlicensed sports wagering, prompting the CFTC in February 2026 to announce that it would defend federally regulated platforms against state enforcement. Yet existing antifraud and material nonpublic information doctrines, developed for securities markets, do not clearly apply to trading on privileged information about real-world events. As a result, platforms such as Kalshi and Polymarket have assumed responsibility for policing insider trading through private governance, functioning as de facto regulators and increasingly formalizing insider trading prohibitions through internal rulemaking without clear statutory standards. Platform sanctions, state-level restrictions, and formal CFTC enforcement guidance in early 2026 confirm that insider trading concerns are no longer hypothetical. In June 2026, Kalshi announced mandatory employment verification for traders in high-risk markets, a six-factor risk-scoring system applied to every proposed market before listing, and platform-embedded whistleblower tools allowing users to report suspicious activity in real time, demonstrating that private governance is actively evolving in response to enforcement pressure and regulatory scrutiny. This Article presents a systematic study of whether regulators and stakeholders recognized insider trading risks in prediction markets before they materialized. It analyzes public comments submitted to the CFTC's 2024 Notice of Proposed Rulemaking using LLM analysis, computational text analysis, and multi-model validation. The findings show that neither regulators nor commenters meaningfully engaged with insider trading risks before they became controversial, revealing a systematic failure of regulatory processes to anticipate informational abuse. Regulatory discourse focused on jurisdictional classification and definitional questions while largely ignoring informational asymmetries that enable insider trading, demonstrating that regulatory frameworks are structurally reactive. The study further shows that market participants cannot be relied upon to identify insider trading risks, undermining disclosure-centered approaches that assume informed, self-policing participation. Building on these findings, the Article develops a typology of insider trading-like misconduct, including trading based on privileged institutional access, temporal informational advantages, manipulation of event probabilities, exploitation of platform design features, and self-referential trading. It situates these practices within existing antifraud and material nonpublic information doctrines and demonstrates that current law fails to clearly prohibit key forms of informational exploitation. Because prediction markets transform informational asymmetries regarding legal, political, and state action into tradable financial assets, failure to address insider trading risks threatens market integrity, institutional legitimacy, and the credibility of probabilistic forecasting as a public information tool. The Article concludes by proposing a governance framework integrating doctrinal clarification, regulatory oversight, and platform-level safeguards before these markets fully integrate into financial and legal systems.

---

## uid: `doi:10.2139/ssrn.6911557`

- title: Annotation-Efficient Adaptation of SAM3 for Thyroid Ultrasound Segmentation: A Comparative Analysis of LoRA and Full Fine-Tuning Across Label Regimes
- authors: Karima Bahmane, Alkhalil  Brahim Chaouki
- affiliations: not stated
- posted: 2026-06-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6911557
- keyword hits: fine-tuning, foundation model

### abstract

Background: Thyroid nodule segmentation in ultrasound imaging is clinically important but typically requires large volumes of expert annotations. Foundation models offer a promising approach to reducing labeled data requirements, yet the relationship between annotation budget and segmentation performance across adaptation strategies remains insufficiently characterized. Methods: We evaluated four SAM3-based adaptation strategies on TN5000 (5,000 biopsy-confirmed thyroid ultrasound images): full fine-tuning (MedSAM3), zero-shot inference (SAM3-Zero), and Low-Rank Adaptation at ranks 8 and 16 (SAM3-LoRA8, SAM3-LoRA16). All models were initialized via Masked Autoencoder pretraining on the unlabeled corpus and evaluated under four annotation regimes (10%, 25%, 50%, and 100% of labeled data) using Dice, IoU, AUC, sensitivity, specificity, and F1-score, with 95% bootstrap confidence intervals and Bonferroni-corrected significance testing. External validation was conducted on the independent DDTI dataset. Results: At full annotation budget, MedSAM3 achieved the highest internal performance (Dice = 0.815, AUC = 0.989), significantly outperforming the zero-shot baseline (Dice = 0.097, p < 0.001 across Wilcoxon, DeLong, and McNemar tests). At 25% label availability, SAM3-LoRA8 matched or exceeded MedSAM3 (Dice = 0.736 vs 0.726) while updating only 1.85% of model parameters, identifying 25% as the annotation-efficiency crossover threshold. No statistically significant difference was observed between LoRA ranks 8 and 16 on per-image Dice (Wilcoxon p = 0.704), indicating that increasing rank beyond 8 yields no measurable performance benefit for this task. External validation on the DDTI dataset preserved model ranking (MedSAM3 AUC = 0.911); a dissociation between AUC and Dice under domain shift was observed across all fine-tuned models, with implications for cross-site deployment. Conclusions: Full fine-tuning with domain-adapted initialization provides the best segmentation performance at large annotation budgets. LoRA adaptation with rank 8 offers a more annotation-efficient and parameter-efficient alternative, matching full fine-tuning at 25% label availability and requiring approximately half the training time. These findings provide a concrete decision framework for selecting adaptation strategies in annotation-constrained clinical deployments of thyroid ultrasound segmentation.

---

## uid: `doi:10.2139/ssrn.6947764`

- title: Musubito: Deterministic Execution Lineage for AI-Enabled Python Workflows
- authors: Domenico Altieri
- affiliations: not stated
- posted: 2026-06-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6947764
- keyword hits: agentic, large language model, llm

### abstract

AI-enabled software systems built around large language model (LLM) agentsincreasingly execute as pipelines of prompts, retrieval steps, tools, validators,and aggregation functions. In these settings, expensive operations are oftenrepeated even when the logical inputs and upstream dependencies have not changed.This paper presents Musubito, a Python runtime for execution lineage anddependency-aware replay. The runtime distinguishes deterministic, stochastic, andexternal-effect steps, each associated with different replay expectations. Its maininvariant is a strict node identity in which operation names, canonical input hashes, andsorted upstream node identifiers determine whether a stored artifact is admissiblefor reuse. Nodes, artifacts, and edges are stored in a relational directed acyclicgraph backed by SQLite. Replay is governed by the declared step semantics; fan-inis represented through merge contexts; and downstream staleness is propagated byrecursive SQL common table expressions (CTEs, recursive SQL queries used totraverse graphs). In this formulation, deterministic refers to node identity andreplay decision logic, not to the semantic determinism of every wrapped operation.In a reproducible five-step agentic pipeline, replay retains millisecond-scalesame-process reuse while adding cross-session persistence and durable DAG lineagefor incremental recomputation.

---

## uid: `doi:10.2139/ssrn.6860720`

- title: The Silent Ergodestruction: How Artificial Intelligence is Eroding Human Creative Thinking
- authors: Tawhidur Rahman
- affiliations: not stated
- posted: 2026-06-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6860720
- keyword hits: generative artificial intelligence, prompt engineering

### abstract

The rapid proliferation of generative artificial intelligence (AI) tools has transformed creative industries, education, and everyday problem-solving. While marketed as creativity enhancers, emerging research reveals a troubling paradox: AI is silently diminishing human creative capacity. This paper synthesizes empirical studies demonstrating that excessive AI reliance leads to cognitive atrophy, idea homogenization, design fixation, and reduced divergent thinking. MIT Media Lab research shows decreased brain activity in AI users during writing tasks, while Exeter University findings indicate AI-generated ideas cluster around common themes while humans produce more original concepts. A meta-analysis of 19 studies confirms a statistically significant homogenization effect. We argue that without deliberate intervention, society risks creating a generation more skilled at prompt engineering than original ideation, fundamentally undermining the creative spark that has driven human advancement for centuries.

---

## uid: `doi:10.2139/ssrn.6960639`

- title: Pre-Learning and Data-Driven Machine Learning Dual-Agent Strategy for Accelerated AEMWE Design
- authors: Yuhao Jiao, Linhao Fan, Zhongyao Zhang, Zhanfan Chen, Xingang Li, Ruichao Wang, Qing Du, Kui Jiao
- affiliations: not stated
- posted: 2026-06-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6960639
- keyword hits: ai agent, large language model, llm

### abstract

Hydrogen is a potential energy carrier, and anion exchange membrane water electrolysis (AEMWE) represents an important route for producing green hydrogen. Machine Learning (ML) methods are commonly adopted to predict the current density of AEMWE systems. However, conventional approaches to data collection and experimental exploration of favorable operating conditions remain relatively limited. Addressing these limitations has become a major challenge at present. In this study, we designed three learning steps to construct a Data Extraction AI agent. The Data AI agent enabled LLM (Large Language Model) to automatically acquire experimental groups from papers, thereby replacing manual efforts. Three machine learning models, including Artificial Neural Network (ANN), Support Vector Regression (SVR), and Kernel Ridge Regression (KRR), were employed to predict current density. Correlation heatmap analysis, cross-validation, hyperparameter tuning, and model optimization were conducted. Among the models examined, KRR demonstrated the highest predictive performance SHapley Additive exPlanations (SHAP) interpretability analysis identified voltage as the most influential predictor of current density. Finally, we integrated various types of information, including the originally collected data, the prediction results of the ML models, and the SHAP analysis results, into a knowledge base and constructed an Analytical AI agent based on it. The Analytical AI agent was capable of recommending promising catalysts, accurately providing favorable operating condition for specified catalysts, and offering clear and logically rigorous judgments. The methodology proposed in this study provides valuable technical support for constructing large-scale AEMWE databases and offers insights into accelerating the discovery of hidden, high-performance operating conditions under massive experimental data.

---

## uid: `doi:10.2139/ssrn.6941538`

- title: The kv4 Trade-off Is Workload-Dependent: A Depth-and Workload-Resolved Study of 4-bit KV-Cache Quantization on a 4 GB Turing GPU
- authors: Christopher Slothouber
- affiliations: not stated
- posted: 2026-06-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6941538
- keyword hits: agentic, llama, qwen

### abstract

The value of 4-bit KV-cache quantization ("turbo4"/kv4) on a 4 GB commodity GPU depends on the workload, and a single tokens/sec headline obscures that. On the NVIDIA GTX 1650 (TU117, Turing sm_75) we run a depthand workload-resolved matrix over KV-cache quantization (f16, turbo2/3/4), decode depth (0-32 768), context allocation (8 K-64 K), and workload shape-sustained decode vs RAG/coordinator (long prefill, short decode) with optional ngram (prompt-lookup) speculative decoding-under a controlled-clock, sole-tenant, L1/L2/L4-instrumented harness. The trade-off flips with workload. For sustained decode (agentic long rollouts), kv4 is a capacity lever that costs throughput: it fits 32 K-64 K context where f16 OOMs, but its dequant kernel makes decode at depth slower than f16 where f16 fits (depth 0: 75.40 vs 73.05; depth 8 192: 33.50 vs 24.53; depth 32 768: f16 OOM vs turbo4 8.14 t/s). For RAG/coordinator shapes (long prefill, short decode-our deployment shape) the decode penalty is largely hidden behind short decode while kv4's capacity is what lets the long context fit. On a realistic RAG probe (retrieval over a real document, extractive QA) we find a cost the throughput numbers miss: 4-bit KV lowers answer accuracy on every family tested directionally, and clearly so on Qwen3-1.7B (8/8 → 4/8; Wilson 95 % intervals on n=8 separate it from f16), with degenerate looping and hallucinated values rather than clean extraction. The smaller perfamily losses (-1/8 on Llama-3.2-3B and SmolLM2-1.7B; none on the 1B MiniCPM5) fall within the small-sample interval and await a larger suite. The decode penalty, by contrast, is universal (-12 % to-50 %). We further show that ngram (prompt-lookup) speculative decoding helps only when output copies input: on a pathological repeated-context prompt it manufactures a large but misleading speedup, whereas on realistic RAG its acceptance collapses (≤0.14) and it slows decode. We also surface the methodological trap that hid the depth cost-throughput measured at shallow decode depth inside a large allocated context (the source of an earlier in-house "turbo4 ≥ f16 at 32 K" reading).

---

## uid: `doi:10.2139/ssrn.6959200`

- title: Toward Neuro-Inclusive Generative AI: Cognitive Barriers, Coping Strategies, and Design Patterns in Prompt-Based Creative Tools
- authors: Amrita Amrita
- affiliations: not stated
- posted: 2026-06-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6959200
- keyword hits: generative ai, prompting

### abstract

Prompt-based creative AI systems, diffusion-based image generators in particular, open new possibilities for visual expression while also imposing cognitive demands that the literature links to exclusion for some neurodivergent users. This structured narrative review draws on scholarship from 2020 to 2026 across humancomputer interaction, cognitive accessibility, neurodiversity, and generative AI to examine how prompt-mediated interaction creates barriers for people with ADHD, autism, dyslexia, and related cognitive differences. This review proposes four barrier types grounded in convergent findings from adjacent HCI and accessibility research: working-memory overload from prompt construction and parameter management; executive-function burden during iterative refinement; sensory and language-processing friction in visually dense, text-centric interfaces; and opaque feedback and hidden prompting conventions that prevent users from diagnosing why outputs diverge from intention. Direct empirical evidence specific to diffusion tools remains thin. Each proposed barrier type warrants direct empirical testing with diffusion-tool users before the framework can be treated as validated. The paper proposes a three-layer taxonomy separating barriers users encounter, coping strategies they develop, and design patterns that future interfaces should test. Accessible creative AI, the review concludes, requires moving past compliance-based thinking toward co-designed, cognitively adaptive interfaces with progressive disclosure, multimodal input, editable prompt histories, interpretable feedback, and metrics built for the prompting workflow rather than borrowed from static interfaces.

---

## uid: `doi:10.2139/ssrn.6975018`

- title: When Better AI Hurts: Verification, Compliance, and AI-Human Handoffs in Service Systems
- authors: Guanling Yang, Cuihong Li, Ricky Roet-Green, Fasheng Xu
- affiliations: not stated
- posted: 2026-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6975018
- keyword hits: ai agent, generative ai

### abstract

Generative AI agents deployed in customer-facing services introduce a distinctive failure mode: hallucination risk , whereby AI responses appear plausible and complete yet may be incorrect, with correctness unobservable prior to human verification. We develop a game-theoretic queueing model of AI-human handoffs in which a firm sets a verification policy and strategic, delay-sensitive customers decide whether to bypass human review and exit with unverified AI answers. Our central finding is an AI improvement trap : when hallucination risk exceeds a critical threshold, improving AI accuracy can paradoxically reduce the effective throughput, which is the rate of successful service completions. The mechanism operates through equilibrium responses: more reliable AI makes customers more willing to forgo human verification, compelling the firm to change its verification policy to maintain compliance. This equilibrium adjustment expands unverified completions, and the resulting errors can outweigh the direct accuracy gains. Consumer surplus, however, always increases with AI accuracy, revealing a firm-customer incentive misalignment: firms may rationally resist AI investments that benefit customers. We further extend the model to incorporate several distinctive features of GenAI systems, including AI reasoning, feedback learning, and imperfect difficulty assessment. These extensions reveal that enhancing AI capability does not automatically improve operational performance. Instead, the benefits of better AI depend critically on how improvements reshape customer behavior and firm policies, reinforcing the central role of strategic responses in determining system outcomes.

---
