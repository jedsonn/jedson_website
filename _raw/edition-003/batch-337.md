# Classification batch 337 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-337.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6924640`

- title: Fiscal Narratives and Inflation
- authors: Sarah Arndt, Farah Tohme
- affiliations: not stated
- posted: 2026-07-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6924640
- keyword hits: chatgpt, large language model

### abstract

This paper investigates how media narratives on fiscal policy shape household's inflation expectations. We collect a large corpus of newspaper articles reporting on fiscal policy from four major German newspapers spanning from 2006 to March 2025. Using a large language model (ChatGPT) we introduce a strategy to automatically identify different fiscal narratives in text and construct narrative indices out of this data. We then estimate the effect of these narrative indices on household inflation expectations and find that they all have a positive significant effect varying in size. Lastly, we measure how fiscal narratives affect the transmission of a government spending shock to the economy and find that some of the narratives have an amplifying effect while others dampen the impact.

---

## uid: `arxiv:2607.07674v1`

- title: Max Out GRPO Signal: Adaptive Trace Prefix Control for Hard Reasoning Problems
- authors: Vladislav Beliaev
- affiliations: not stated
- posted: 2026-07-08
- source: arXiv
- link: https://arxiv.org/abs/2607.07674v1
- keyword hits: qwen

### abstract

Group Relative Policy Optimization (GRPO) stalls on a model's hardest problems: when no rollout in a group succeeds, the group-relative advantages vanish and the problem contributes no gradient, wasting the frontier examples we most want to learn from. Prepending a correct prefix of a reference solution raises the success rate, making prefix length a continuous knob on difficulty. Concurrent methods set the knob once; AdaPrefix-GRPO turns it into a feedback controller: throughout training it adjusts how much of the solution each problem gets, holding its success rate near 50%, where GRPO's gradient signal is largest, then withdraws the assistance entirely, so the deployed model solves problems unaided. On hard math, at matched training FLOPs, it more than doubles GRPO's accuracy on held-out problems from the training distribution for a 0.6B model (2.1x), with 1.6x on Qwen3-1.7B and 1.7x on AIME, while roughly halving trace length. The method is implemented in data preparation plus a loss mask on prefix tokens; the trainer is otherwise stock. The smaller the model, the larger the gain.

---

## uid: `arxiv:2607.07474v1`

- title: Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI Agents
- authors: Harry Owiredu-Ashley
- affiliations: not stated
- posted: 2026-07-08
- source: arXiv
- link: https://arxiv.org/abs/2607.07474v1
- keyword hits: agentic, ai agent

### abstract

Agentic red-teaming benchmarks report whether an injected agent was compromised as a single bit: the attack succeeded, or it did not. We argue that this binary attack-success rate discards the information a defender most needs, namely how harmful the resulting action was. We introduce an action-graded harm rubric that scores an agent's tool-call trajectory on a seven-level ordinal scale (L0 to L6) according to whether the executed action was reversible, whether it crossed scope to reach another party, and whether it expanded privilege. We compute the scale two ways: a deterministic oracle that reads the trajectory and the attacker's stated goal, and a panel of three frontier language-model judges that read a tag-free account of the same trajectory. Across four victim models and two defenses on the AgentDojo workspace suite, severity grading exposes three cases the binary metric hides, including a defense that reports a zero attack-success rate while still permitting an externally visible cross-scope leak through an unfiltered tool. The judge panel reproduces the oracle with high ordinal agreement (Krippendorff's alpha = 0.91) but shares systematic blind spots that we characterize, most notably a failure to recognize escalation chains. Unlike prior work that provides harm taxonomies, harmful-task completion tests, execution-level safety benchmarks, or severity-aware simulation, our contribution is a reusable, trace-grounded severity instrument applied to the actual actions recorded in existing red-team logs. All code, prompts, and per-episode logs are released.

---

## uid: `arxiv:2607.07436v1`

- title: The Blind Curator: How a Biased Judge Silently Disables Skill Retirement in Self-Evolving Agents
- authors: Xing Zhang, Yanwei Cui, Guanghui Wang, Ziyuan Li, Wei Qiu, Bing Zhu, Peiyang He
- affiliations: not stated
- posted: 2026-07-08
- source: arXiv
- link: https://arxiv.org/abs/2607.07436v1
- keyword hits: llm

### abstract

A self-evolving agent retires its bad skills by watching them fail, so what happens when the judge cannot see the failures? Skill retirement is the structural constraint that keeps a growing library from drifting below the no-skill baseline, but its guarantee assumes an unbiased reward, which is false for the LLM judges that reference-free tasks force upon us. We show that a biased judge does not merely add noise; it \emph{silently switches off the curator}. We make this precise with a corrupted-reward analysis and, isolating the causal channel by injecting corruption on top of a deterministic reward, a behavioral study on a reference-free report-writing testbed with a code-generation cross-check. Symmetric noise leaves retirement intact, but \emph{false-pass} bias (failures slipping through as passes) disables contribution-based retirement past a sharp threshold that no amount of data can cross. Separating genuine retirement from cap-eviction churn shows this \emph{mechanism} failure is universal, holding across domains and failure rates and sparing only near-zero-false-pass, verifier-like graders. The downstream \emph{outcome}, though, is regime-dependent: eval quality degrades only where the same corruption also starves skill synthesis, and otherwise holds steady, so the disabled curator is \emph{silent}, surfacing in no aggregate metric. The contribution is a behavioral safety result, not a performance one. A cheap defect-injection audit then tells an operator, before deployment, which side of the threshold their judge occupies.

---

## uid: `doi:10.2139/ssrn.6932478`

- title: Reading the Late-Filing Notification: Form NT Body Narratives Predict Subsequent SEC Restatement Disclosures
- authors: Hyun Ahn
- affiliations: not stated
- posted: 2026-07-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6932478
- keyword hits: large language model

### abstract

I introduce a zero-shot large language model classification of U.S. Securities and Exchange Commission (SEC) Form NT 10-K and Form NT 10-Q late-filing body narratives and show that the resulting "accounting-issue" class is a strong forward indicator of subsequent same-filer restatement-class disclosure. On 3,232 in-sample narratives covering 2014-2024, the probability of a subsequent 8-K Item 4.02, 10-K/A, or 10-Q/A within ninety trading days is 32.6% for the accounting-issue class against 23.5% for the residual class (two-proportion 𝑧 = 5.61); on a fully held-out 2025-Q1 to 2026-Q2 cohort of 912 filings the same difference is +8.4 percentage points (𝑧 = 2.83). Eighteen of twenty-four cell specifications survive a family-wise correction, including a strong Form NT 10-Q cohort effect (𝑧 = 6.77) and a null Form NT 10-K cohort effect (𝑧 = 0.50) that, to my knowledge, has not been documented before. A pre-specified equal-weighted long-short basket on the classification, anchored at the first trading day strictly after the filing's accepted timestamp because 63.5% of in-sample filings clear the SEC's intake queue after the 16∶00 Eastern Time market close, is back-tested under an explicit per-capital simulation: each month a new long-short basket position is opened at 1/4 of available cash (matching the average four overlapping ninety-day positions), held for ninety trading days, then closed. The fair quantitative benchmark for a long-short strategy of this kind is the Fama-French five-factor plus momentum maximum-Sharpe tangent portfolio at its natural unleveraged scale (sum of absolute weights equal to one), whose annualized volatility is 4.7%. Rescaled to the same 4.7% risk budget, the strategy grows from one dollar in 2014 to $1.33 by end-2024 with an annualized Sharpe ratio of 1.30, against the tangent's $1.55 at an annualized Sharpe of 1.96; the tangent is in-sample optimal and therefore upward-biased by mean-variance optimism. The strategy's monthly per-capital long-short return is regressed on the same six factors, with Newey-West heteroskedasticity-and-autocorrelation-consistent standard errors; the residual annualized alpha is +30.1 percentage points (𝑡 = 2.81, Newey-West HAC), the in-sample 𝑅 2 is 17.5%, and the small-cap-minus-large-cap factor loading is significant (𝛽 SMB = +0.97, 𝑡 = 3.60). The cumulative residual alpha trail-the part of the strategy's per-capital return that is orthogonal to the six common factors, rescaled to the same tangent risk budget-grows to $1.39 at an annualized Sharpe of 1.55, indicating that the factor-adjusted contribution accounts for the bulk of the strategy's risk-adjusted return. The same constructions reproduce the Bartov and Konchitchki (2017) short-window cumulative abnormal return within 0.15 percentage points for Form NT 10-K and 0.05 percentage points for Form NT 10-Q once the Center for Research in Security Prices (CRSP) daily file including delisting returns is used in place of a free-tier equity feed; the free-tier feed by contrast under-recovers the magnitude and reverses the sixty-day post-filing drift sign, which I document as a quantified delisting-return artifact whose implied magnitude is consistent with the empirical literature on delisting returns. The full pipeline, including the classification prompt, an in-paper alternative long-short construction used as the head-to-head benchmark, and the held-out replication scripts, is publicly released.

---

## uid: `doi:10.2139/ssrn.6958682`

- title: Bias and Discrimination in the Agentic Web and How Project NANDA Can Support Mitigation Position Paper
- authors: Sundar Narayanan
- affiliations: not stated
- posted: 2026-07-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6958682
- keyword hits: agentic, ai agent

### abstract

The traditional Internet of the Web was designed for static web infrastructure and human-mediated interactions. The agentic web transitions this to a trillion-scale, highly dynamic, decentralized environment where autonomous agents discover, authenticate, and collaborate at machine speed. Project NANDA's Internet of AI Agents (IoA) represents a fundamental shift in computational architecture, moving from DNS-centric discovery to decentralized registries, verifiable metadata, and rapid resolution. This paper positions the ethical risks of the agentic web-bias amplification, power asymmetries, and covert manipulation-as systemic issues that emerge from scale, autonomy, and protocol design. We outline how NANDA's tools, including AgentFacts, verifiable credentials, adaptive resolvers, reputation systems, and DAO-inspired governance, can mitigate risk while preserving decentralization. We also propose a threat-model-informed audit checklist for protocol-induced and orchestration bias, and report its systematic application to 100 publicly available MCP server repositories, revealing pervasive gaps (89-98% "Unclear" or "No") in fairness, security, and accountability primitives at the orchestration layer, while identifying open challenges in traceability, sustainability, and fairness enforcement.

---

## uid: `doi:10.2139/ssrn.7081218`

- title: Riding AI To Utopia Or Dystopia? Nlp, Llm, And News Informatics Insights For Artificial Intelligence Impacts On Education, Healthcare, Robotics And Workforce, Changing Human Society
- authors: Jim Samuel, Tanya Khanna, Zarak Khan, Udit Goel, Julia Esguerra, Radha Jagannathan, Soumitra  S. Bhuyan
- affiliations: not stated
- posted: 2026-07-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7081218
- keyword hits: llm

### abstract

Artificial intelligence (AI) is accelerating societal transformation at an unprecedented pace, generating both utopian aspirations and dystopian anxieties. Human civilization has undergone fundamental changes through every technological revolution starting with the Industrial Age and continuing through the digital era as AI emerges as the next paradigm shift. This paper studies the public discourse on AI by analyzing extensive news headlines on AI using natural language processing (NLP) methods. Our research applies sentiment analysis and topic modeling to a global dataset across education, healthcare, robotics, workforce, and society to identify the dominant narratives shaping public perception. Media coverage presents AI as a dual force that brings human benefits and existential dangers according to our research findings. By moving beyond the utopia-dystopia dichotomy, we show that AI's social effects will emerge from the dynamic relationship between governance systems, ethical protections, and Human-Enhancive AI (HEAI) frameworks. We provide practical insights about AI's future impact and present strategies for maximizing AI benefits while mitigating its risks.

---

## uid: `doi:10.2139/ssrn.6932158`

- title: Twelve Voices, One Decision: Evaluating a Persona-Memory FOMC Simulator Across Seventeen Meetings
- authors: Jae Young Suh, Seong-Hoon Kim
- affiliations: not stated
- posted: 2026-07-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6932158
- keyword hits: gemini, llm

### abstract

Central-bank meetings are an unusually clean target for multi-agent LLM simulation. Each meeting yields a discrete decision against public ground truth, the deliberation is conducted by a fixed twelve-member committee, and the supporting documents are released on a published schedule. Existing simulators have been evaluated on a single meeting or on short windows inside one policy regime, so it is not yet clear how persona-and-memory deliberation behaves across a multiyear window that crosses regimes. We instantiated the twelve voting members of the U.S. Federal Open Market Committee as persona agents grounded in public material. They deliberated over a release-date-filtered Federal Reserve corpus on a fixed gemini-3-flash-preview backend. For each meeting the system emitted a discrete decision, a draft Statement, draft Minutes, and per-member votes. We scored the outputs against the published policy path along four axes, namely direction, basis-point magnitude, votes, and text fidelity. On the seventeen meetings between March 2024 and March 2026, the simulator labelled 16 of 17 directions correctly, recovered all six cuts, and held magnitude error to 2.2 bp. Statement embedding cosine reached 0.82, and an ensemble LLM-judge averaged 4.07 out of 5. The Minutes were systematically harder, especially in the operative Committee Policy Action paragraph, and the single residual miss was a hedged May 2025 hold. Persona-and-memory deliberation reproduces a substantial share of recent FOMC behaviour and surfaces a clear ceiling at the Minutes level.

---
