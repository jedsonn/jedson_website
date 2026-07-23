# Classification batch 346 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-346.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7121382`

- title: The Trust Appropriability Problem in Artificial Intelligence: Why Innovators Capture Usage but Not Legitimacy. Evidence from the n-Ball Volume Peak and the Trust-Adoption Divergence Across 48,340 Respondents in 47 Countries Special Issue: "Outside In: Unconventional Pathways to Innovation"
- authors: Xuan Tran
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7121382
- keyword hits: chatgpt

### abstract

Who captures the trust surplus from artificial intelligence (AI) adoption? Teece (1986) demonstrated that innovators rarely capture full returns from technological innovations because complementary assets are controlled by others, the appropriability problem. This paper identifies a structural analogue: a trust appropriability problem in AI in which adoption and legitimacy diverge at the precise mathematical threshold predicted by the Bayesian Gamma Prior-Update Recursion (BGPR) theory ([Author], 2025). Using the n-ball volume recursion V(n) = (2π/n) × V(n−2), which peaks at n = 5 (V(5) ≈ 5.264), we show that the fifth AI paradigm generation, ChatGPT (2022), corresponds to peak adoption (66% regular usage) simultaneously with maximum trust-adoption divergence: only 46% of global respondents trust AI (Gillespie et al., 2025; N = 48,340; 47 countries), trust had declined from 63% to 56% between 2022 and 2025 as adoption doubled, expert optimism runs 50 percentage points above public trust (73% vs. 23% on job impact), and public excitement has collapsed to its lowest recorded level. This pattern, usage captures the volume peak, trust does not, is structurally predicted by the gamma convergence property of the n-ball function and cannot be explained by standard diffusion-of-innovation models. We develop four propositions: (P1) AI usage and AI trust diverge at the n-ball volume peak; (P2) the trust-adoption gap follows the gamma convergence curve, not a random walk; (P3) expert optimism and public trust constitute distinct appropriability regimes; and (P4) governance, not further capability development, is the complementary asset that determines who captures the trust surplus. The paper contributes a formal model of paradigm-level trust appropriability and a policy framework for closing the trust-adoption gap before n = 7.

---

## uid: `doi:10.2139/ssrn.7121397`

- title: The Trust Appropriability Problem in Artificial Intelligence: Why Innovators Capture Usage but Not Legitimacy. Evidence from the n-Ball Volume Peak and the Trust-Adoption Divergence Across 48,340 Respondents in 47 Countries Special Issue: "Outside In: Unconventional Pathways to Innovation"
- authors: Xuan Tran
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7121397
- keyword hits: chatgpt

### abstract

Who captures the trust surplus from artificial intelligence (AI) adoption? Teece (1986) demonstrated that innovators rarely capture full returns from technological innovations because complementary assets are controlled by others, the appropriability problem. This paper identifies a structural analogue: a trust appropriability problem in AI in which adoption and legitimacy diverge at the precise mathematical threshold predicted by the Bayesian Gamma Prior-Update Recursion (BGPR) theory ([Author], 2025). Using the n-ball volume recursion V(n) = (2π/n) × V(n−2), which peaks at n = 5 (V(5) ≈ 5.264), we show that the fifth AI paradigm generation, ChatGPT (2022), corresponds to peak adoption (66% regular usage) simultaneously with maximum trust-adoption divergence: only 46% of global respondents trust AI (Gillespie et al., 2025; N = 48,340; 47 countries), trust had declined from 63% to 56% between 2022 and 2025 as adoption doubled, expert optimism runs 50 percentage points above public trust (73% vs. 23% on job impact), and public excitement has collapsed to its lowest recorded level. This pattern, usage captures the volume peak, trust does not, is structurally predicted by the gamma convergence property of the n-ball function and cannot be explained by standard diffusion-of-innovation models. We develop four propositions: (P1) AI usage and AI trust diverge at the n-ball volume peak; (P2) the trust-adoption gap follows the gamma convergence curve, not a random walk; (P3) expert optimism and public trust constitute distinct appropriability regimes; and (P4) governance, not further capability development, is the complementary asset that determines who captures the trust surplus. The paper contributes a formal model of paradigm-level trust appropriability and a policy framework for closing the trust-adoption gap before n = 7.

---

## uid: `doi:10.2139/ssrn.7123267`

- title: E-VContract: Auditable Binary CVE Confirmation via Patch-Aware Semantic Contracts
- authors: Wei Guo, Qiang Wei, Yunfeng Wang
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7123267
- keyword hits: llm

### abstract

Known-CVE binary confirmation determines whether a target binary preserves a known vulnerable behavior or implements the corresponding repair when source-level patch context is unavailable, incomplete, or inconsistent with the deployed artifact. Existing patch checks can indicate that a binary resembles a repaired reference, but they do not prove that the relevant guard prevents the CVE-specific hazard, so they may mark an unrepaired target as safe. This paper presents E-VContract, a patch-aware semantic confirmation method for this repair-status decision that addresses this gap by treating repair status as a satisfaction question over binary evidence rather than as a similarity label. E-VContract derives a role-aware semantic contract from CVE repair knowledge, binds structured binary evidence to source, sink, guard, and constraint roles, and checks whether the observed repair condition blocks the hazard before assigning Preserved, Guarded, or Uncertainwhen evidence is insufficient. We evaluate E-VContract on an 18-entry, 72-case CVE/GHSA-entry benchmark and a 1,200-case controlled benchmark, where it achieves 72/72 and 1,200/1,200 correct decisions within the counted COPY_OOB-style scope; in contrast, LLM-Judge baselines and PS3 either make safety-critical false decisions or lack full end-to-end coverage. These results show that known-CVE binary confirmation should not infer repair from patch resemblance alone, but should require explicit evidence that the candidate repair satisfies the vulnerability-specific safety condition in the analyzed binary during known-CVE repair assessment.

---

## uid: `doi:10.2139/ssrn.7122633`

- title: IntelliVLA:Structured Task Reasoning for Speech-Driven Robotic Manipulation in Multi-Turn Human-Robot Interaction
- authors: XiaoKang Hu, Lili Han, Xiuping Liu, Yuefei Li, Le Li
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7122633
- keyword hits: foundation model, qwen

### abstract

​Instruction-following robot manipulation in real environments requires a deployed system to jointly resolve spoken intent, visual grounding, dialogue context, and reliable motion execution. We present IntelliVLA, a dialogue-grounded Vision-Language-Action framework for speech-driven robotic manipulation that couples lightweight model Qwen3-VL-2B-based multimodal task reasoning with RGB-D perception, structured action representation, and a ROS 2 execution pipeline on a UR10e manipulator. Rather than treating each command independently, IntelliVLA maintains dialogue history and scene state to resolve underspecified follow-up instructions, and explicitly separates pick and place intents to improve controllability, interpretability, and execution safety. We formalize the system as a structured mapping from multimodal observations to machine-readable action tuples and executable motion plans. Experiments on 100 real-robot instructions spanning target grasping, pick-and-place, and multi-turn interaction show 90.4% overall success, 92.8% semantic accuracy, 12.1 mm average localization error, and a dialogue coherence score of 4.3/5. On LIBERO, IntelliVLA utilizes lightweight models to consume minimal computational resources, achieves 87.8% average success across four task suites, remaining competitive with strong open baselines while preserving a transparent dialogue-grounded interface. These results suggest that structured task reasoning is a practical route for bridging multimodal foundation models and reliable embodied execution.

---

## uid: `doi:10.2139/ssrn.7121431`

- title: Privacy-enhanced co-release of trajectory and traffic flow data via LLM-guided path obfuscation and Kirchhoff-bound perturbation
- authors: Guoyang Qin, Jianhao Yang, Jian Sun
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7121431
- keyword hits: large language model, llm

### abstract

The widespread release of floating-car trajectories and aggregated traffic flow data is essential for modern intelligent transportation systems, yet it introduces profound privacy risks. Because human mobility is highly identifying, sparse spatiotemporal observations can be exploited via linkage attacks to reconstruct full paths, sensitive endpoints, and behavioral routines. Existing trajectory privacy defenses typically suppress nodes or perturb location points; however, they fundamentally preserve a modified correspondence to the underlying true trip. We show that modern deep inference models can easily bridge this residual correspondence by fusing public road-network topology with co-released link flow side channels, accurately reconstructing missing trajectory data. Here, we propose a paradigm shift that breaks correspondence entirely rather than merely increasing trip perturbation. We introduce a joint data-release framework that pairs structural-aware Large Language Model (LLM) path obfuscation with Kirchhoff-bound link flow perturbation. Instead of treating these channels independently, our framework co-optimizes obfuscated-path selection and loop-structured noise injection within a closed adversarial loop targeting deep reconstruction encoders. Evaluated on approximately 18,000 real-world trajectories from Shanghai, our approach reduces the exact-match recovery rate of state-of-the-art inference models from 70.1\% to 9.8\%$\pm$0.6\%, and successfully restricts adaptive retraining attacks to 32.5\% while maintaining robust downstream transportation utility. By simultaneously neutralizing trajectory and flow side channels, this unified adversarial framework offers a rigorous methodology for publishing highly secure yet useful urban mobility data.

---

## uid: `doi:10.2139/ssrn.7120738`

- title: Official Monetary Policy Narratives and Bond Risk Premia: Evidence from LLM-Based News Measures
- authors: Xuan Wang, Ximing Yin, Yi Liu, Keqin Li
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7120738
- keyword hits: llm

### abstract

Central bank communication and official policy narratives are critical for monetary transmission, but few studies quantify their forward-looking information in bond markets. We build an article-level Official Monetary Policy Action Score (OMPAS) via LLM semantic annotation using 1.46 million Chinese official-news articles to quantify action-oriented policy narratives. We then construct the Policy Action Signal (PAS) by linking OMPAS to future policy actions. We show that PAS significantly predicts Chinese government bond excess returns beyond yield curve factors, with stronger effects on long-maturity bonds. Its persistent component forecasts lower future yields, consistent with durable easing expectations being incorporated into the yield curve. Out-of-sample forecasts and portfolio tests show that PAS delivers tangible economic value for investors. Our paper provides an auditable LLM text measurement tool and identifies an unspanned policy narrative channel shaping bond risk premia.

---

## uid: `doi:10.2139/ssrn.7121420`

- title: The Trust Appropriability Problem in Artificial Intelligence: Why Innovators Capture Usage but Not Legitimacy. Evidence from the n-Ball Volume Peak and the Trust-Adoption Divergence Across 48,340 Respondents in 47 Countries
- authors: Xuan Tran
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7121420
- keyword hits: chatgpt

### abstract

Who captures the trust surplus from artificial intelligence (AI) adoption? Teece (1986) demonstrated that innovators rarely capture full returns from technological innovations because complementary assets are controlled by others, the appropriability problem. This paper identifies a structural analogue: a trust appropriability problem in AI in which adoption and legitimacy diverge at the precise mathematical threshold predicted by the Bayesian Gamma Prior-Update Recursion (BGPR) theory ([Author], 2025). Using the n-ball volume recursion V(n) = (2π/n) × V(n−2), which peaks at n = 5 (V(5) ≈ 5.264), we show that the fifth AI paradigm generation, ChatGPT (2022), corresponds to peak adoption (66% regular usage) simultaneously with maximum trust-adoption divergence: only 46% of global respondents trust AI (Gillespie et al., 2025; N = 48,340; 47 countries), trust had declined from 63% to 56% between 2022 and 2025 as adoption doubled, expert optimism runs 50 percentage points above public trust (73% vs. 23% on job impact), and public excitement has collapsed to its lowest recorded level. This pattern, usage captures the volume peak, trust does not, is structurally predicted by the gamma convergence property of the n-ball function and cannot be explained by standard diffusion-of-innovation models. We develop four propositions: (P1) AI usage and AI trust diverge at the n-ball volume peak; (P2) the trust-adoption gap follows the gamma convergence curve, not a random walk; (P3) expert optimism and public trust constitute distinct appropriability regimes; and (P4) governance, not further capability development, is the complementary asset that determines who captures the trust surplus. The paper contributes a formal model of paradigm-level trust appropriability and a policy framework for closing the trust-adoption gap before n = 7.

---

## uid: `doi:10.2139/ssrn.7028619`

- title: Profiting from Technological Innovation, Forty Years On
- authors: Mouhamdy Dahoud
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7028619
- keyword hits: generative artificial intelligence

### abstract

In 1986, David Teece showed that innovators rarely capture the rent from their own innovation when imitation is easy, and that the rent then accrues to the owners of specialized complementary assets rather than to the holder of the intellectual property. Forty years on, generative artificial intelligence shifts the very hinge of the model. Where Teece assumed a clean separation between the technological core and the complementary asset, user-data flows now feed the self-improving algorithm in real time: asset and innovation fuse. Absent primary empirical data, we adopt an axiomatic conceptual method, grounded in thought experiments and analytical illustration, to restate three axioms and to propose an artifact, the self-appropriability matrix, which updates Teece's (1986, p. 287) taxonomy. We mobilize a single empirical anchor, the observed compression of the interval between frontier models, to support the acceleration hypothesis, while conceding that this metric captures the market-perceived rhythm of recombination rather than fundamental innovation itself. We close with three scenarios to 2066 and one thesis: in the age of AI, rent leaves the idea and settles into compute, distribution and, at the other extreme, human originality, the one scarcity that probabilistic synthesis cannot manufacture.

---
