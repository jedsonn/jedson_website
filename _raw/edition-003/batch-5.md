# Classification batch 5 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-5.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7147495`

- title: Testing Large Language Models capabilities to create Indicators of Compromise
- authors: Bartłomiej Płonkowski, Piotr Lewandowski, Grzegorz Janowski, Anna Felkner
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7147495
- keyword hits: claude, gpt-4, large language model, large language models, llama, llm, llms, qwen

### abstract

This paper investigates the capability of Large Language Models (LLMs) to generate Indicators of Compromise (IoCs) from exploits targeting devices and software. The study evaluates commercial models (Anthropic’s Claude 3.5 Sonnet, OpenAI’s GPT-4o) and locally-deployed models: two specialised in programming (Qwen2.5-Coder-7B-Instruct and Codestral) and one general (Llama 3.1 8B). The results are evaluated using strict and lenient matching methods with Nuclei rules. Additionally, the study analyses the impact of parameter combinations on performance, with results grouped by exploit programming languages and Common Vulnerabilities and Exposures (CVE) records publication years. To further test model capabilities, querying a Glastopf honeypot logs with LLM- created rules is included in the analysis. The results highlight the strengths and limitations of LLMs in cybersecurity applications, particularly in generating IoCs. While commercial models demonstrate robust performance, tested on–premise models were deemed unsuitable for the task. This work contributes to advancing AI-driven threat detection by identifying key factors impacting model effectiveness and proposing areas for future research. By bridging the gap between exploit analysis and IoC generation, this study underscores the potential of LLMs to enhance automated cybersecurity workflows while addressing current limitations in their application.

---

## uid: `arxiv:2607.17765v1`

- title: FIFA World Cup 2026 as a Contamination-Free Benchmark for LLM Forecasting Agents: Four Models, a Bookmaker, and 104 Matches
- authors: Jiacheng Ding, Cong Guo, Jason Xu
- affiliations: not stated
- posted: 2026-07-20
- source: arXiv
- link: https://arxiv.org/abs/2607.17765v1
- keyword hits: chatgpt, claude, gemini, gpt-5, large language model, large language models, llm, llms

### abstract

We introduce WC2026-Agents, a benchmark and dataset for evaluating large language models (LLMs) as autonomous forecasting agents on real, future events. For every one of the 104 matches of the 2026 FIFA World Cup, four frontier models -- Claude Opus 4.8, ChatGPT (GPT-5.5, high reasoning), Gemini 3.1 Pro, and Grok (Expert Mode) -- ran an identical search-act-reflect loop: gather evidence with a web tool, commit to a 1X2 (team-A win / draw / team-B win) distribution and a virtual 100-USD bet, and, after the match, reflect given only the final score. Because every match kicked off after the models' training cutoffs, the benchmark is contamination-free by construction. Crucially, we pair the four agents with a fifth competitor drawn from the same information environment -- the pre-match betting market -- collected as per-match 1X2 odds, giving an economically grounded baseline and letting us score not just what an agent predicts but what it does with money. The release contains 416 forecasts and 414 reflections with verbatim reasoning, ground truth (including penalty shootouts), odds, and a reproducible evaluation suite. A reference evaluation surfaces findings that raw accuracy hides: the four agents issue an identical top pick in 92% of matches and none beats the market's Brier score; indeed, a naive flat stake on the market favorite out-earns all four agents. Yet the agents diverge sharply as decision-makers: betting return-on-investment ranges from -18% to +10%, fading the market is unprofitable for all four, the share of forecasts that cite the market ranges from 12% to 100%, and self-reported error rates on wrong picks range from 36% to 86%. The benchmark thus measures calibration, decision quality, and self-knowledge -- axes on which frontier models differ even when their predictions do not. Data and code: https://github.com/graphuofm/FIFA2026LLM

---

## uid: `doi:10.2139/ssrn.6636720`

- title: Medbench V4: A Robust and Scalable Benchmark for Evaluating Chinese Medical Language Models, Multimodal Models, and Intelligent Agents ​
- authors: Jinru Ding, Simeng Wu, Lu Lu, Chao Ding, Mouxiao Bian, Jia-Yuan Chen, Wenrao Pang, Rui-Yao Chen
- affiliations: not stated
- posted: 2026-04-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6636720
- keyword hits: agentic, claude, gpt-5, large language model, large language models, llm, llms

### abstract

Background: Recent advances in medical large language models (LLMs), multimodal models, and agents demand evaluation frameworks that reflect real clinical workflows and safety constraints.Methods: We present MedBench v4, a nationwide, cloud-based benchmarking infrastructure comprising over 700,000 expert-curated tasks spanning 24 primary and 91 secondary specialties. The platform features dedicated tracks for LLMs, multimodal models, and agents. Items undergo multi-stage refinement and multi-round review by clinicians from more than 500 institutions. We evaluated 15 frontier models, using an LLM-as-a-judge approach—calibrated to human ratings—to score open-ended responses.Results: Base LLMs reached a mean overall score of 54.1/100 (best: Claude Sonnet 4.5, 62.5/100), but performance in safety and ethics remained low (18.4/100). Multimodal models performed worse overall (mean 47.5/100; best: GPT-5, 54.9/100), demonstrating solid perception yet weaker cross-modal reasoning. Conversely, agents built on the same backbones substantially improved end-to-end performance (mean 79.8/100), with Claude Sonnet 4.5–based agents achieving up to 85.3/100 overall and 88.9/100 on safety tasks.Conclusions: MedBench v4 reveals persisting gaps in multimodal reasoning and safety for base models, while showing that governance-aware agentic orchestration can markedly enhance benchmarked clinical readiness without sacrificing capability. By aligning tasks with Chinese clinical guidelines and regulatory priorities, the platform offers a practical reference for hospitals, developers, and policymakers auditing medical AI.​

---

## uid: `doi:10.2139/ssrn.6663737`

- title: Generative AI-based Agentic Framework for the Formulation of Phenomena Identification and Ranking Table for Advanced Reactor Application
- authors: Paridhi Athe, Nam Dinh
- affiliations: not stated
- posted: 2026-04-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6663737
- keyword hits: agentic, foundation model, generative ai, large language model, large language models, llm, llms, prompt engineering, retrieval augmented

### abstract

One of the preliminary steps in the design and safety analysis of nuclear reactor systems is the formulation of the Phenomena Identification and Ranking Table (PIRT). PIRT requires systematic strategy and knowledge abstraction at different levels. Counterfactual reasoning and knowledge transfer from different disciplines are also needed depending on the application. In this work, we aim to leverage the recent developments in the area of multimodal Large Language Models (LLMs) to build an AI-driven multi-agent system for the implementation of PIRT. Foundation models based on advanced LLMs (such as GPT 4o), customized and adapted by retrieval augmented generation and prompt engineering, are used as proxy experts to support knowledge abstraction, reasoning and information retrieval for PIRT formulation. The evaluation of the multiagent PIRT implementation is performed using Bayesian Belief Network (BBN). BBN helps in assimilating prior knowledge with observation and helps us in making inference under a situation of uncertainty and incomplete information (missing data). As evaluation requires processing and summarizing large volume of information, a frontier LLM (GPT 5.2) with specific input, guidance and supervision from humans was used in the systematic formulation of evaluation evidence used in the BBN. The illustration of the multiagent framework for PIRT implementation is presented using case studies on: (i) a generic sodium fast reactor with loss of coolant accident under beyond design basis accident condition and (ii) an advanced high temperature reactor with loss of coolant accident under beyond design basis accident condition.

---

## uid: `doi:10.2139/ssrn.6729618`

- title: LLM Zero-Shot Replication of SEC Comment Letter Returns: An Out-of-Sample Reproducibility Test
- authors: Hyun Ahn
- affiliations: not stated
- posted: 2026-05-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6729618
- keyword hits: claude, large language model, large language models, llama, llm, llms, prompting

### abstract

This study tests whether the post-disclosure return channel documented for U.S. Securities and Exchange Commission (SEC) comment letters by Ryans (2021, Review of Accounting Studies 26(1)) is reproducible out-of-sample under a fundamentally different extraction technology. Where Ryans trains a supervised Naïve Bayesian text classifier on cumulative-abnormal-return labels, this study extracts topic, severity, and registrant-response intent from 1,014 matched UPLOAD-CORRESP letter pairs (Russell 3000 universe, 2015-2024) using zero-shot prompting of three large language models (LLMs): Gemma 3 27B, Llama 3.3 70B, and Claude Opus 4.7 as a label oracle. A pre-registered severity-weighted long-short portfolio constructed against sector-and-size-matched non-recipient controls delivers, in the held-out 2022-2024 window, a Fama-French five-factor plus momentum residual alpha of 11.92 percent annualized (Newey-West t=2.86, p=0.007, deflated Sharpe ratio 1.00, Sharpe 1.43). Two additional Benjamini-Hochberg-FDR-survivor strata emerge from a 43-cell post-hoc grid: the non-GAAP metrics topic and the 0.5-0.8 severity band. Together with the pre-registered headline, three claims survive multiplecomparison correction. The contribution is methodological rather than channel-discovery: this study (i) demonstrates that zero-shot LLM extraction reproduces the Ryans (2021) sign direction without supervised label leakage, (ii) extends the channel with topic-and severity-stratified Benjamini-Hochberg-survivor sorts that Ryans does not perform, and (iii) supplies one-command end-to-end reproducibility from raw filings to alpha. The full pipeline, including extraction prompts, replication scripts, and a locally runnable visualization dashboard, is publicly released on GitHub.

---

## uid: `doi:10.2139/ssrn.6778404`

- title: Fuzzy-Gated Verification of LLM Agents for Industrial Fault Diagnosis: An Evolutionary-Optimized Closed-Loop Framework
- authors: Yifan Xiao, Dexuan Xu, Shijie Li, Weiping Ding, Yu Huang
- affiliations: not stated
- posted: 2026-05-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6778404
- keyword hits: ai agent, large language model, large language models, llama, llm, llms, mistral

### abstract

Intelligent fault diagnosis and machine health management are essential for reliable operation of industrial systems, yet deploying large language models (LLMs) for these tasks introduces reliability risks including hallucinated evidence, overconfident outputs, and inconsistent reasoning. We propose CL-LLMOps, a closed-loop LLMOps framework that orchestrates LLM agents through five integrated stages—from alarm normalization to regression-tested action. At the semantic verification level—where, to our knowledge, soft computing has not previously been applied—its hierarchical mechanism combines rule-based pattern checking, cross-attention evidence scoring, and Mamdani fuzzy inference gating, jointly optimized via multi-objective particle swarm optimization, to detect hallucinations and evidence contradictions before maintenance decisions. Evaluation on three public datasets spanning power quality classification, bearing fault diagnosis, and wind turbine SCADA anomaly detection—validated across two open-source LLM backbones (Llama-3-8B and Mistral-7B)—shows that CL-LLMOps achieves 98.6% diagnostic accuracy on power quality data, 99.3% on CWRU bearing data, and 95.2% on CARE wind turbine data. The framework reduces inconsistency-type hallucination from 12% to 2% relative to the fine-tuned LLM baseline while maintaining 93% action accuracy and 96% risk compliance on PQ data, with fuzzy gating specifically improving action accuracy by 5 percentage points through graded borderline handling. This work bridges LLM-powered intelligence and operational dependability for industrial deployment, offering a novel integration of established soft computing techniques—neural attention, fuzzy logic, and evolutionary optimization—at the semantic verification level for deploying trustworthy AI agents in fault diagnosis under the Industry 5.0 paradigm.

---

## uid: `doi:10.2139/ssrn.6843081`

- title: Beyond the Prompt: An Analysis of the Current State of Automated Test Generation with LLMs
- authors: Shakthi Weerasinghe, Xiaozhou Li, Md Arfan Uddin, Deuslirio Silva-Junior, Manoel  Veríssimo dos Santos Neto, Mateus  Eduardo S. Ribeiro, Hamza  Bin Mazhar, Melika Akbarsharifi
- affiliations: not stated
- posted: 2026-06-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6843081
- keyword hits: agentic, fine-tuning, generative ai, large language model, large language models, llm, llms, prompting

### abstract

Background: Large Language Models (LLMs) are transforming automated test generation, shifting the paradigm from search-based heuristics to generative AI. However, naive prompting has proven to be a brittle foundation for enterprise-grade software, spurring fragmented architectural innovations that demand systematic synthesis.Objective: This study reviews LLM-assisted test generation techniques "beyond the prompt'". We evaluate enterprise readiness and practical viability of these approaches by isolating existing capabilities, prevailing limitations, and priority areas for future investigation. Method: We screened 2,616 peer-reviewed studies published between 2015 and 2025, identifying 313 primary studies for full synthesis. Driven by four Research Questions, we examine the literature across four under-explored dimensions relevantly to automated test generation: advanced architectural and prompting strategies, the functional quality of generated tests, the scientific rigor of prevalent evaluation techniques, and the spectrum of model adaptations.Results: We highlight an architectural shift from fine-tuning to inference-time augmentations (RAG and agents) that breaks coverage ceilings, yet incurring a notable "agentic tax". The study also exposes a pervasive "syntax-versus-semantics gap", where over-reliance on superficial metrics masks a steep post-generation "repair tax". Finally, an industrial validity paradox leaves LLM efficacy for complex enterprise testing unproven, as the literature focuses overwhelmingly on isolated unit tests on algorithmic toy benchmarks.Conclusion: While LLMs exhibit strong capabilities, their transition to enterprise-grade testing is bottlenecked by brittle evaluation practices and the costs of post-generation repair. To close this gap, the field must pivot from isolated unit tests on contaminated toy benchmarks toward deterministic, contamination-free orchestration pipelines for complex, stateful architectures.

---

## uid: `doi:10.2139/ssrn.6884338`

- title: Cognitive Guardrails in Medical LLMs: Fusing Latent Routing with T-Adaptive Attention to Mitigate Aleatoric and Epistemic Uncertainty
- authors: Narendra Bayutama Wibisono
- affiliations: not stated
- posted: 2026-06-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6884338
- keyword hits: large language model, large language models, llama, llm, llms, mistral, prompting

### abstract

Clinical deployment of Large Language Models (LLMs) is fundamentally constrained by their propensity to hallucinate—generating fluent but clinically unfounded assertions that pose direct patient safety risks. This work introduces Conditional Latent Routing (CLR) , a compound inference architecture that decomposes clinical uncertainty into its aleatoric and epistemic constituents and applies distinct, mechanistically motivated interventions at each stratum. Inspired by the corollary discharge framework from computational psychiatry—wherein the healthy brain’s forward model suppresses self-generated sensory predictions, a mechanism whose dysfunction in schizophrenia produces hallucinations—we construct an analogous dual-pathway system for medical LLM inference. A fine-tuned Bio_ClinicalBERT encoder classifies input noise (aleatoric uncertainty) and routes clean inputs through a latent soft-prompting Fast Lane while directing noisy, contradictory records through a cautionary Slow Lane with explicit abstention instructions. To address epistemic uncertainty—the model’s internal confusion—we introduce a T-Adaptive Attention patch at the logits level that modulates generation temperature as an inverse function of hidden-state variance. We evaluate CLR on BioMistral-7B across 400 clinical cases (200 clean, 200 noisy) using RAGAS Faithfulness scored by Llama-4-Scout-17B-16E-Instruct via Groq API. Phase 1 (Aleatoric Routing) achieves 100% routing accuracy and 64.8% faithfulness on clean data with zero alignment tax , but reveals a critical failure: a 0% inconclusive rate on noisy inputs, indicating extreme over-helpfulness bias. Phase 2 (Epistemic T-Adaptive Patch) preserves faithfulness at 64.4% while demonstrating zero computational overhead, but the inconclusive rate remains at 0%. We formally prove this failure as The Greedy Paradox : under greedy decoding, temperature scaling of logits is mathematically nullified because for all . Phase 3 (Non-Greedy Sampling) degrades faithfulness to 58.5% while still failing to trigger abstention, confirming that over-helpfulness bias is embedded in pre-training weight distributions, not merely in the decoding surface. These results establish that single-agent, test-time interventions are fundamentally insufficient for self-uncertainty modulation in medical LLMs, providing strong empirical justification for transitioning to multi-agent systems with externalized uncertainty arbitration.

---
