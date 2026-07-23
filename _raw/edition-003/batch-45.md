# Classification batch 45 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-45.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6799068`

- title: LLM-Native Applications as a Paradigm for AI-Driven Software Architecture: Taxonomy, Application Families, and Architecting Practices
- authors: Paulo Henrique Mendes Maia, Alan  Portela Bandeira, Gabriel de Oliveira, Nabor Mendonça, Carlos Aderaldo
- affiliations: not stated
- posted: 2026-05-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6799068
- keyword hits: large language model, large language models, llm, llms

### abstract

Large Language Models (LLMs) are increasingly shaping the design of modern software systems, moving beyond their role as auxiliary tools toward becoming central components that drive system behavior. However, existing approaches to LLM-enabled applications are often ad hoc and lack architectural foundations that account for emerging concerns such as orchestration, tool integration, knowledge grounding, memory, governance, and observability. In this paper, we introduce the concept of LLM-native applications, a class of systems whose architecture is fundamentally organized around LLM-based reasoning and behavior orchestration. To systematically characterize this emerging class, we propose an architecture-driven taxonomy defined by eight dimensions that capture key architectural and operational concerns. Based on this taxonomy, we identify six recurring application families that represent distinct architectural emphasis profiles. We further present a conceptual architecture that operationalizes these dimensions and illustrate its applicability through a concrete instantiation in a real-world application. Finally, we discuss architectural trade-offs and implications for practitioners and researchers. By providing a structured design space and a shared vocabulary, this work contributes toward the systematic engineering of LLM-native applications and advances the architectural foundations of AI-driven software systems.

---

## uid: `doi:10.2139/ssrn.6786136`

- title: Are Multimodal LLMs Ready for Clinical Dermatology? A Real-World Evaluation in Dermatology
- authors: Ruoyi Jiang, Hyunjae Kim, Zhenyue Qin, Morten Lee, Margaret MacGibeny, Ailish Hanly, Angela Sadlowski, Shanin Chowdhury
- affiliations: not stated
- posted: 2026-05-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6786136
- keyword hits: gpt-4, large language model, large language models, llm, llms

### abstract

Background: Multimodal large language models (MLLMs) have demonstrated promise on publicly available dermatology benchmarks. However, benchmark performance may not generalize to real-world dermatologic decision-making. Most prior evaluations rely on curated image-only tasks, often using dermoscopic or single-lesion or rash images obtained under standardized conditions. In contrast, real-world dermatology consultations commonly involve photographs captured in primary care or emergency department settings. Consultations are accompanied by brief requests with context written by referring clinicians; cases are reviewed by dermatologists, who triage patients for possible urgent evaluation based on likely differential diagnoses. We evaluated MLLM performance under conditions designed to reflect real-world dermatology consultation workflows. Methods: We evaluated four open-weight MLLMs (InternVL-Chat v1.5, LLaVA-Med v1.5, SkinGPT4 and MedGemma-4B-Instruct) and one commercial MLLM (GPT-4.1) across three publicly available dermatology datasets and a retrospective multi-site hospital-based dermatology consultation cohort comprising 5,811 cases and 46,405 clinical images. The real-world cohort paired clinical photographs with referring clinician consultation notes and dermatologist-authored differential diagnoses. Models were evaluated on two clinically relevant tasks: free-text differential diagnosis generation and severity-based triage of urgent dermatologic conditions. Diagnostic performance was assessed using BERTScore, LLM-based adjudication, and independent review by board-certified or board-eligible dermatologists for clinical intent, factuality, and specificity. Findings: Diagnostic performance was modest on public datasets and declined substantially in the real-world hospital consultation cohort. On public benchmarks, top-3 diagnostic accuracy reached 26.55% for the best open-weight model and 42.25% for GPT-4.1. On real-world consultation cases using images alone, top-3 diagnostic accuracy declined to 1.50-13.35% among open-weight models and 24.65% for GPT-4.1. Incorporating clinical context from referring clinician requests improved performance across all models, increasing top-3 diagnostic accuracy up to 28.75% among open-weight models and 38.93% for GPT-4.1. However, model outputs were highly sensitive to incomplete or erroneous consultation context, leading to substantial diagnostic variability across evaluation settings. For severity-based triage of dermatologic conditions, models achieved moderate sensitivity (generally exceeding 60%), suggesting potential utility for screening but insufficient reliability for clinical deployment overall. Interpretation: Current dermatology MLLMs showed lower performance under real-world consultation conditions than on public benchmark datasets. These findings suggest that limitations in visual grounding and context integration contribute substantially to current MLLM performance limitations. Future evaluation frameworks should prioritize workflow realism and deployment-oriented assessment rather than benchmark performance alone.

---

## uid: `doi:10.2139/ssrn.6762100`

- title: Prompt Injection in Court Filings: Generative AI in the Brazilian Judiciary, Algorithmic Procedural Bad Faith, and the Limits of Legal Sanction
- authors: Victor Habib Lantyer
- affiliations: not stated
- posted: 2026-05-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6762100
- keyword hits: generative ai, generative artificial intelligence, large language model, large language models

### abstract

The institutional adoption of generative artificial intelligence by Brazilian courts has pushed the judicial process into a new risk zone. Court filings once written primarily for human readers are now also processed as computational inputs by systems that assist with case management, summarization, and the drafting of decisions. That shift opens a specific attack surface: the insertion of hidden commands into pleadings, a technique known as prompt injection. This article examines a recent judgment from the 3rd Labor Court of Parauapebas, in the Eighth Regional Labor Court (TRT-8), case ATOrd No. 0001062-55.2025.5.08.0130. The judge identified a hidden instruction in the complaint, in white text on a white background, designed to nudge an AI system into producing a perfunctory defense and into refusing to challenge the attached documents. The research question is whether such conduct amounts to a procedural offense, a disciplinary infraction, or a crime, and what the limits of judicial sanction are in light of Article 77, paragraph 6, of the Brazilian Code of Civil Procedure. The methodology is qualitative, combining doctrinal legal analysis, regulatory review, and a case study, informed by the technical literature on the security of large language models. The article argues that judicial prompt injection amounts to a serious breach of procedural good faith and professional loyalty, and that the court's choice to fine the attorneys directly, although doctrinally bold under Article 77, paragraph 6, of the CPC, is defensible on a teleological reading of the provision: section 6 was designed to protect the exercise of advocacy, not the covert manipulation of the technical infrastructure that sustains the judiciary. The reading remains vulnerable on appeal, particularly because the judgment does not evidence the prior warning required by Article 77, paragraph 1. On the criminal side, fraud, procedural fraud, ideological falsity, and computer crimes all face significant obstacles of statutory fit.

---

## uid: `doi:10.2139/ssrn.6793998`

- title: UG-CPPO: Uncertainty-Gated LLM Infusion for Risk-Sensitive Reinforcement Learning Trading Agents
- authors: Grace Esther DONG
- affiliations: not stated
- posted: 2026-05-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6793998
- keyword hits: deepseek, gpt-4, large language model, llm

### abstract

Recent work on hybrid Reinforcement Learning-Large Language Model (RL-LLM) trading agents, notably FinRL-DeepSeek [Benhenda, 2025], has revealed a counterintuitive empirical finding: increasing LLM signal infusion strength systematically degrades agent performance, even at perturbation magnitudes as small as 0.1%. We hypothesize that a key factor in this degradation is the absence of epistemic uncertainty estimation on LLM outputs: the agent has no mechanism to distinguish a high-confidence financial signal from an unreliable hallucination. Drawing inspiration from Monte Carlo Dropout techniques in medical imaging uncertainty quantification [Gal and Ghahramani, 2016], we propose UG-CPPO (Uncertainty-Gated CVaR-PPO), a novel architecture that dynamically gates LLM signal infusion based on prompt-ensemble-derived uncertainty. We query the LLM with N =5 semantically diverse prompts per news article and compute the standard deviation σ across responses; when σ exceeds a threshold τ , the gate closes and the signal is suppressed. We apply this gating mechanism to both the action modifier S f (PPO action perturbation) and the risk modifier R f (CVaR penalty). We evaluate the framework on the FNSPID dataset [Dong et al., 2024] with 28,502 (ticker, date) signals computed via OpenAI gpt-4o-mini, using 10seed evaluation on Nasdaq trading 2019-2023. The gating mechanism achieves the predicted activation rate (34.2% ± 0%, exactly within target [30-40%]) and we demonstrate that LLM uncertainty σ is structurally higher in bear markets (2022: 0.614) than in bull periods (2019: 0.525). However, at our computeconstrained scale (500,000 training steps, 10 stocks), UG-CPPO does not show statistically significant performance improvement over baselines on aggregate metrics (Wilcoxon p > 0.05): cumulative return 36.0% ± 38.7% versus 62.0% ± 37.6% for CPPO and 43.9% ± 32.2% for PPO. We document the methodology, release 30 trained agents and 55,360 LLM uncertainty signals, and identify training scale as the principal direction for future validation. Our contribution is a reusable uncertainty-gating mechanism with rigorous multi-seed empirical characterizationrare in this application domain.

---

## uid: `doi:10.2139/ssrn.6804059`

- title: Between Perceived Fairness and Resignation: Examining Machine Heuristics, Privacy Cynicism and Self-Disclosure in Generative AI
- authors: Fan Liang, Christoph Lutz
- affiliations: not stated
- posted: 2026-05-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6804059
- keyword hits: chatgpt, deepseek, generative ai, generative artificial intelligence

### abstract

Generative artificial intelligence (AI) systems such as ChatGPT and DeepSeek require users to disclose nuanced prompts that may reveal highly sensitive personal information. Existing studies on privacy risks in generative AI are fragmented and rarely grounded in established privacy theories or comparative frameworks. To advance knowledge on generative AI privacy, a multi-stage model of privacy decision-making is proposed that integrates machine heuristics, privacy concerns, privacy cynicism and self-disclosure. Drawing on two online surveys in China and the US (N = 1632), we examine how machine heuristic perceptions relate to privacy concerns, how concerns translate into privacy cynicism, and how cynicism is associated with self-disclosure. Chinese respondents reported higher self-disclosure, whereas US participants expressed greater privacy concerns, mistrust and uncertainty, but also higher self-efficacy and use frequency. The findings suggest that perceptions of AI as fair, accurate, and having expertise are associated with lower privacy concerns, that concerns are positively linked to cynicism dimensions, and that cynicism exhibits divergent associations with self-disclosure. These results are discussed and contextualized in relation to privacy scholarship and policy and design recommendation.

---

## uid: `doi:10.2139/ssrn.6804466`

- title: The Price of Fiscal Confusion: Evidence from U.S. Treasury Communication
- authors: Yiting Guo, Zeju Zhu
- affiliations: not stated
- posted: 2026-05-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6804466
- keyword hits: large language model, large language models, llm, llms

### abstract

While the macroeconomic transmission of central bank forward guidance is well documented, the operational footprint of sovereign fiscal communication remains largely a black box. Does the macroeconomic penalty for erratic fiscal signaling change when the fundamental institutional anchor shifts? We answer this by applying large language models (LLMs) to 11,691 U.S. Department of the Treasury press releases from 1996 to 2026, extracting a high-frequency, multidimensional history of U.S. fiscal posture. Utilizing a state-dependent local projections (SDLP) framework, augmented by novel historical decompositions, we identify a clear structural break in how the macroeconomy absorbs fiscal uncertainty. We demonstrate that during the global financial crisis (GFC) and zero lower bound (ZLB) era, fiscal erraticism operated primarily as a real-economy friction, suppressing industrial production and employment while nominal prices remained anchored. However, in the high-debted COVID epoch, this transmission mechanism fundamentally fractured. Fiscal confusion now bypasses the real economy, transmitting directly into acute inflationary unmooring and compressions of the sovereign term premium. These findings confirm that in the modern era of elevated sovereign debt, fiscal forward guidance is no longer mere political noise; it is a primary driver of financial instability and nominal risk pricing.

---

## uid: `doi:10.2139/ssrn.6734481`

- title: MIRF: Mahjong-inspired Reasoning Framework for Large Language Models
- authors: Jaehwan Kim
- affiliations: not stated
- posted: 2026-05-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6734481
- keyword hits: large language model, large language models, llm, llms, qwen

### abstract

Large Language Models (LLMs) fundamentally operate in a binary manner, either generating an output or not. Due to this limitation, hallucinations often occur where the model outputs incorrect information with high confidence. In this paper, we discovered that the gameplay of Mahjong and the reasoning methods of LLM are very similar, and we propose MIRF (Mahjong-Inspired Reasoning Framework for Large Language Models), a reasoning framework for large language models inspired by the game of Mahjong. MIRF consists of four core pipelines. First, we formally define Tenpai in LLM reasoning. Tenpai represents an intermediate state where a solution can be reached structurally, but one cannot be perfectly certain. Second, we introduce a new reasoning state called Yakunashi. Yakunashi represents a situation where the model is in a Tenpai state but cannot determine an output because certain preconditions are not met. This is similar to a situation where one possesses a structurally perfect Mahjong set but lacks valid tile combinations, making it impossible to declare victory. Third, we define Beta-Ori as the primary defensive output strategy and distinguish between a principle-based safety-first fold and a final state where all tiles are drawn. Fourth, we propose a MIRF-weighted RLHF reward function that imposes a multiplicatively higher penalty than the standard error on confident hallucinations (Noten's Riichi). We empirically evaluate MIRF on local LLM (qwen3.5:0.6b and gemma4:e4b) for 21 pairs of QAs across 5 question categories. The experimental results show that the Deal-in rate was 0% in all experimental runs, and the Yakunashi state emerged naturally through the interaction of Tenpai and Noten. This is a state discovered through experimentation, not an intentionally designed state. In this study, we propose new evaluation indicators including the Deal-in ratio, Tenpai declaration rate, Betaori precision, and Yakunashi ratio, which better represent the reliability of LLM that cannot be captured by accuracy alone.

---

## uid: `doi:10.2139/ssrn.6813758`

- title: Data Overlap, Not Creative Reasoning: Understanding AI Competency in Accounting Education through the CICPA Examination
- authors: Mengmeng Yu, Jianning Xu, Jiading Zhu
- affiliations: not stated
- posted: 2026-05-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6813758
- keyword hits: large language model, large language models, llm, llms

### abstract

The rapid advancement of large language models (LLMs) presents profound implications for both accounting practice and accounting education, yet the fundamental sources of AI competency in this domain remain poorly understood. This ambiguity matters for educators: whether AI proficiency stems from genuine creative reasoning or from the structural similarity between training data and novel tasks has direct consequences for how institutions should design curricula, assess student competencies, and prepare graduates for human-AI collaboration. Utilizing the Chinese Institute of Certified Public Accountants (CICPA) examination as an empirical setting, this study tests two competing hypotheses, namely the creative reasoning effect and the overlapping effect, as the dominant source of AI advantage. Drawing on panel data regression methods, the results indicate that data overlap rather than creative reasoning constitutes the primary driver of current AI proficiency in accounting-related tasks considering tasks complexity. These findings carry significant implications for accounting education. Rather than treating AI proficiency as a generalized capability, educators and students should develop the judgment to identify task characteristics and select appropriate AI tools accordingly, a judgment that depends not on familiarity with any particular tool, but on understanding the conditions under which different AI systems are and are not reliable.

---
