# Classification batch 1 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-1.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7315339`

- title: The Collective Rationality Trap: Algorithmic Herding, Sentiment Synchronicity, and the Erosion of Market Depth
- authors: Jitendra Singh Jadav
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7315339
- keyword hits: deepseek, gemini, large language model, large language models, llama, llm, llms, prompting, qwen

### abstract

This paper investigates whether the mass adoption of Large Language Models (LLMs) among retail and institutional investors homogenizes financial sentiment in ways that introduce systemic market fragility. We formalize the Collective Rationality Trap (CRT)-a market regime in which individually rational, AI-assisted decisionmaking inadvertently synchronizes capital flows and erodes counterparty liquidity. To eliminate context-leakage bias present in early single-prompt studies, we execute an isolated, single-ticker prompting protocol across N = 200 S&P 500 equities. We elicit sentiment scores from a 4-model research suite combining frontier commercial APIs and local GPU-accelerated open-weights reasoning models: Google Gemini 3.6 Flash, Meta Llama-3.2 3B, DeepSeek-R1 Qwen 1.5B (Chinese open reasoning model), and Microsoft Phi-3.5 Mini. We document an empirical cross-model sentiment agreement framework across a 7-day longitudinal dataset (N = 1,400 evaluations across 7 trading days), demonstrating that model synchronicity is highly sector-structured and temporally stable: speculative and high-beta equities exhibit high cross-model sentiment dispersion (σ = 0.284), while core defensive, healthcare, and industrial sectors show grounded fundamental alignment. We address potential counterarguments regarding high-frequency liquidity arbitrage, demonstrating that market maker inventory constraints prevent arbitrageurs from absorbing synchronized sell shocks once AI adoption exceeds a critical threshold (λ c ≈ 70%). We complement the empirical analysis with an agent-based market simulation (n = 1,000 agents across 500 Monte Carlo runs), introduce the Synchronicity Exposure Index (SEI) as a portfolio-level risk metric, and propose regulatory circuit breakers aligned with BIS, FSB, and IMF systemic risk frameworks.

---

## uid: `doi:10.2139/ssrn.7295938`

- title: Who Audits the Reviewers? A Multi-Model Consensus Framework for Characterizing Failures in LLM-Assisted Peer Review
- authors: Olalekan J. Akintande
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7295938
- keyword hits: gemini, gpt-4, large language model, large language models, llama, llm, llms, prompting

### abstract

Large Language Models (LLMs) are increasingly used to assist with academic peer review, yet their outputs remain prone to systematic errors often presented with high confidence. This paper presents a comprehensive empirical characterization of failure modes in LLM-assisted academic review through a controlled experiment involving 15 papers, 5 LLMs, 3 prompt conditions, and 672 independent judge-review evaluations across 11 error types. We find that Unsupported Claims is the most prevalent error (mean frequency 3.02 per review), followed by Plausible Reasoning Gaps (2.86) and Confirmation Bias (2.19). Llama 3.1 70B consistently outperforms commercial alternatives, including GPT-4o (overall error mean 3.23 vs. 3.53), challenging assumptions regarding the superiority of proprietary architectures. Structured prompting reduces error frequency by approximately 35%, while self-correction reduces errors by 44% on average; however, self-correction efficacy is highly architecture-dependent, ranging from a 50.73% reduction in GPT-4o to negligible improvements in Gemini 3.5 Flash. Inter-judge agreement is poor (mean Fleiss' Kappa:-0.013), with a 2.6-fold stringency differential between judges, mirroring human peer review variability. A counterintuitive "Self-Correction Paradox" emerges wherein higher-quality reviews generate both increased consensus and specific points of heightened disagreement. Logistic regression confirms that model choice, prompt condition, and domain, particularly in Medicine, are significant predictors of error prevalence. Novice reviewers miss 2.5% of errors on average. We propose a robust failure taxonomy and offer practical recommendations for journals, emphasizing that while LLMs offer promising structural support, rigorous human oversight remains indispensable.

---

## uid: `doi:10.2139/ssrn.7321818`

- title: The Heuristic Paradox: When Structured Prompts Hurt LLM Performance on Competitive Programming
- authors: Muhammad Ali Hassan Ahmad, Moira MacNeil
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7321818
- keyword hits: claude, gemini, gpt-5, large language model, large language models, llama, llm, llms, prompt engineering

### abstract

Large Language Models (LLMs) are increasingly used for automated code generation, yet their ability to solve complex algorithmic problems under competitive programming constraints remains poorly understood. This study investigates whether structured, heuristic-based prompt engineering can improve the correctness, efficiency, and robustness of LLM-generated C++ solutions for competition-level algorithmic problems. We evaluate five widely accessible LLMs: GPT-5, Gemini 2.5 Flash, Claude Sonnet 4.5, Grok 4.1, and Llama 3.2 (3B), across 12 problems from the USACO 2025 US Open Contest spanning four difficulty tiers (Bronze, Silver, Gold, Platinum). We test each model under two conditions: a zero-shot baseline with a single retry opportunity and a heuristic-guided prompt that incorporates constraint analysis, algorithm selection, and non-retry protocols. We measure pass rate, execution time, peak memory usage, immediate executability, and asymptotic complexity. Our results reveal a counterintuitive Heuristic Paradox: heuristic prompts decreased average pass rates for four of the five models while simultaneously improving code quality along other dimensions, most notably a reduction in execution time ranging from 34% to 91% and universal 100% immediate executability for all compilable code. The paradox is most severe at the Bronze (easiest) tier, where average pass rates dropped from 48.7% to 24.0%, suggesting that structured algorithmic guidance causes models to overthink simple problems by selecting overly complex algorithms. Only Grok 4.1 consistently benefited from heuristics, improving from 38.8% to 43.1% overall. These findings challenge the prevailing assumption that more detailed prompts uniformly improve LLM performance and highlight a fundamental tension between algorithmic sophistication in prompt design and solution correctness.

---

## uid: `doi:10.2139/ssrn.7319081`

- title: Auditing LLM-based Synthetic Expert Panels for AHP: A Preregistered Benchmark and Prospective Order-randomization Test
- authors: Howard Kim, Keuntae Cho
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7319081
- keyword hits: claude, gemini, gpt-5, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are increasingly used as inexpensive synthetic experts in structured decision support, but their judgments are rarely validated against published human targets. We benchmark six LLMs on a source-audited corpus of 27 published Analytic Hierarchy Process (AHP) studies in English and Korean, with a preregistered holdout of 22 studies and 21 reference-weight tasks. A preregistered phase evaluated Gemini 3.5 Flash, GPT-5-mini, and K-EXAONE; a prospectively frozen, locally time-stamped extension evaluated Gemini 3.6 Flash, Claude Sonnet 5, and HCX-007 under the same experimental design and repetition protocol, together retaining 28,783 valid responses. Holdout rank replication was modest and model-dependent, and only HCX-007 clearly beat uniform weights on absolute error. A diagnostic then showed that the rank metric is confounded with criterion presentation order: reference vectors largely follow source listing order, a model-free descending-order rule reaches a mean correlation of 0.735 and outscores every model, and HCX-007 is the only model of six that strongly tracks presentation order. A prospective randomized-order experiment reversed the point-estimate pattern: HCX-007 was the only model whose accuracy declined, only the Claude Sonnet 5 improvement survived Holm correction, and a direct-recall probe found no verbatim reproduction of published weights. Persona conditioning was model-dependent and often weaker than repeated-draw variability, and individual human matrices were too sparse to assess human-likeness. Synthetic panels can support piloting and stress-testing of decision pipelines, but replay benchmarks must randomize presentation order before rank accuracy can be read as reconstructed expert judgment.

---

## uid: `doi:10.2139/ssrn.7320118`

- title: Auditing LLM-Based Synthetic Expert Panels for AHP: A Preregistered Benchmark and Prospective Order-Randomization Test
- authors: Howard Kim, Keuntae Cho
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7320118
- keyword hits: claude, gemini, gpt-5, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are increasingly used as inexpensive synthetic experts in structured decision support, but their judgments are rarely validated against published human targets. We benchmark six LLMs on a source-audited corpus of 27 published Analytic Hierarchy Process (AHP) studies in English and Korean, with a preregistered holdout of 22 studies and 21 reference-weight tasks. A preregistered phase evaluated Gemini 3.5 Flash, GPT-5-mini, and K-EXAONE; a prospectively frozen, locally time-stamped extension evaluated Gemini 3.6 Flash, Claude Sonnet 5, and HCX-007 under the same experimental design and repetition protocol, together retaining 28,783 valid responses. Holdout rank replication was modest and model-dependent, and only HCX-007 clearly beat uniform weights on absolute error. A diagnostic then showed that the rank metric is confounded with criterion presentation order: reference vectors largely follow source listing order, a model-free descending-order rule reaches a mean correlation of 0.735 and outscores every model, and HCX-007 is the only model of six that strongly tracks presentation order. A prospective randomized-order experiment reversed the point-estimate pattern: HCX-007 was the only model whose accuracy declined, only the Claude Sonnet 5 improvement survived Holm correction, and a direct-recall probe found no verbatim reproduction of published weights. Persona conditioning was model-dependent and often weaker than repeated-draw variability, and individual human matrices were too sparse to assess human-likeness. Synthetic panels can support piloting and stress-testing of decision pipelines, but replay benchmarks must randomize presentation order before rank accuracy can be read as reconstructed expert judgment.

---

## uid: `doi:10.2139/ssrn.7279498`

- title: AIgentXR: Generative AI Agents and Extended Reality for Teleoperation of Unmanned Aerial Vehicles
- authors: Alhassan Mumuni, Fuseini Mumuni, Masha Ahoba Buah
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7279498
- keyword hits: agentic, ai agent, generative ai, generative artificial intelligence, large language model, large language models, llm, llms

### abstract

Unmanned Aerial Vehicles (UAVs), or drones, are increasingly deployed in complex and safety-critical environments, where human-machine interaction and collaboration is often critical to achieving mission objectives. Yet their operation still relies heavily on ground control stations (GCS) based on traditional 2D graphical user interfaces (GUIs). These interfaces permit very limited interaction with the human operator. They also limit situational awareness, increase cognitive load, and, thereby, constrain overall mission effectiveness. Recent advances in generative artificial intelligence (AI), especially Large Language Models (LLMs), and Extended Reality (XR) present new opportunities to overcome these limitations. This work explores the integration of LLM-based intelligent agents with XR to create immersive and intuitive user interfaces (UIs) for teleoperating UAVs. We develop a proof-of-concept UI, AIgentXR, based on these techniques and conduct practical studies on the use of agentic AI and XR to improve the teleoperation of UAVs. The focus is on improving mission execution efficiency, increasing interaction intuitiveness, reducing cognitive load on operators, and enhancing situational awareness. We performed extensive quantitative evaluation of our approach using predictive human-computer interaction (HCI) models and also conduct benchmark comparisons with approaches based on conventional ground control stations.The results suggest that XR-assisted agentic interaction may provide a promising direction for future human-centered UAV control systems, particularly in complex missions requiring rapid situational understanding and intuitive supervisory control.

---

## uid: `doi:10.2139/ssrn.7276907`

- title: Beyond Superficial Similarity: A Psychometric Fidelity Framework (PFF) for Validating AI Digital Twins in Mental Health Research
- authors: Susanna Joo, Myeong-Sook Yoon
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7276907
- keyword hits: claude, gemini, gpt-5, large language model, llm, llms

### abstract

Despite the growing potential of Large Language Model (LLM)-based psychobehavioral digital twins in mental health research, standardized protocols for verifying their empirical and psychometric validity are lacking. Existing evaluations often rely on descriptive-level comparisons or AUC, failing to assess whether AI-generated synthetic data preserves the underlying psychological structures of human respondents. This study proposes the Psychometric Fidelity Framework (PFF), an evaluation protocol across four tiers: distributional, structural, network, and clinical fidelity. We analyzed an integrated dataset (N = 2,256) comprising empirical survey data from South Korean university students (n = 756) and synthetic datasets generated by GPT-5.5, Gemini 3.5 Flash, and Claude 3.6 Sonnet (n = 500 each). Three validated instruments were employed: the Patient Health Questionnaire–9 (PHQ-9), UCLA Loneliness Scale–6 (UCLA-6), and Alcohol Use Disorders Identification Test–K (AUDIT-K). Results revealed systematic psychometric failures across all PFF tiers. LLMs failed to replicate the characteristic positive skewness of empirical mental health distributions. Furthermore, Cronbach’s alpha and confirmatory factor analysis revealed psychometric discrepancies between most LLMs and survey data. The theoretically expected correlations were absent or inconsistent. Crucially, the dissociation between indistinguishable AUCs and distorted prevalence, and between distinguishable AUCs and similar prevalence, highlights that descriptive or AUC-based comparisons are insufficient for validation. The PFF provides a systematic standard for validating AI-generated data and establishes the necessary boundary conditions for integrating psychobehavioral digital twins into mental health research and evidence-based practice.

---

## uid: `doi:10.2139/ssrn.7312181`

- title: Beyond Human-like Responses: Evaluating the Implicit Personality Alignment of Large Language Models
- authors: Qinyi Hu, Fei Xie, Zhen Li, Xucong Hu, Meng Zhang, Mowei Shen, Jifan Zhou
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7312181
- keyword hits: chatgpt, claude, gpt-4, large language model, large language models, llm, llms

### abstract

Despite widespread adoption of large language models (LLMs), our understanding of these competent assistants remains limited. Since personality serves as a key predictor of behavioral patterns, this study investigates whether LLMs have implicitly learned to display personality through a rigorous psychometric approach. We employed role-playing prompts to assess the "personality" of 100 fictional characters enacted by ChatGPT-4o and Claude Haiku 3.5 using two validated personality measures: a self-evaluation scale (NEO-FFI-R) and a situational judgment test (SJT). Performance was benchmarked against human participants (N = 113). Results revealed limitations in LLMs' personality coherence: both LLMs demonstrated inferior test-retest reliability to human participants, especially in terms of behavioral tendencies which showed particularly pronounced instability. More critically, construct validity analysis revealed false inference and inconsistencies between self-evaluated personality and behavioral tendencies. These discrepancies demonstrate that current LLMs are responding based on personality-related knowledge to pretend they have specific personality, rather than having a stable and consistent inner personality as humans.

---
