# Classification batch 115 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-115.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7140493`

- title: Achieving Staggered Arrivals of Bidirectional Metro Trains via LLM-Inspired Heuristic Hyper-Optimization
- authors: xuyang song, Wenfeng pang, wanlu cao, Yu Feng, Xiaowei MAO, Huaiyu Wan
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7140493
- keyword hits: large language model, llm, qwen

### abstract

Frequent simultaneous arrivals of bidirectional metro trains at high-traffic transfer stations cause severe passenger congestion and safety hazards. To address this, this paper formulates a large-scale discrete Integer Non-Linear Programming (INLP) model with two objectives: maximizing the weighted arrival-time differences across target stations (F_A) and minimizing the total number of simultaneous arrivals (F_B), subject to adjustment-bound, safety-headway, and turnaround constraints. Since the solution quality and efficiency of metaheuristic solvers depend critically on hyperparameter settings, this study proposes an LLM-inspired hyper-optimization framework. By integrating Latin Hypercube Sampling (LHS) for a high-quality initial experience pool, the framework employs a Large Language Model (Qwen3.5-27B-Instruct) as a meta-optimizer. Through a closed-loop iterative mechanism, the LLM analyzes the historical parameter-utility data, performs pattern recognition, and actively generates both optimal hyperparameter combinations and adaptive iteration counts, shifting the paradigm from passive search to active decision-making. We validate the proposed framework on the real-world timetable of Zhengzhou Metro Line 1 (30 stations, peak window 18:00-20:00) under two scenarios: a multi-station collaborative scenario (Scenario 1) and a single-station scenario (Scenario 2). Empirical results show that the proposed framework: (i) eliminates 82.4% of simultaneous arrivals on Scenario 1 and 100% on Scenario 2; (ii) achieves a 5x reduction in NSGA-II generations compared to default settings (400 vs 2000 on S1; 458 vs 2000 on S2), translating to proportional savings in local compute; and (iii) requires only 5-6 LLM API calls, half of the strongest LLM-based baseline LLaMEA (10-12 calls). Compared with LLaMEA, the proposed framework delivers 1.36x faster total wall-clock time on S1 (705 s vs 962 s) and 1.47x faster on S2 (400 s vs 587 s), while achieving higher solution quality on both scenarios. Ablation studies confirm the complementary contributions of LHS and LLM components. This research provides a computationally frugal and generalizable intelligent paradigm for urban rail transit timetable optimization.

---

## uid: `arxiv:2607.17122v1`

- title: Scope3Trace: Evidence-Based Identification and Extraction of Scope 3 GHG Emissions from Sustainability Reports
- authors: Siyuan Zheng, Yifan Duan, Chao Xue, Flora D. Salim
- affiliations: not stated
- posted: 2026-07-19
- source: arXiv
- link: https://arxiv.org/abs/2607.17122v1
- keyword hits: large language model, large language models, llm

### abstract

Scope 3 greenhouse gas (GHG) emissions account for the majority of corporate carbon footprints, yet remain difficult to analyze at scale due to sparse disclosures, heterogeneous report document formats, and limited evidence traceability. Existing approaches typically rely on large language models to extract emissions information from ESG reports, but often lack explicit evidence grounding or depend on costly manual annotation and verification to ensure extraction reliability. To address these challenges, we propose Scope3Trace, an evidence-grounded information extraction framework designed to extract interpretable and traceable Scope 3 emissions information from real-world ESG and sustainability reports. The framework integrates a document information extraction pipeline that performs PDF collection and OCR parsing, LLM-assisted page localization and table reconstruction, and hybrid rule-LLM extraction of organization- and building-level emissions disclosures with evidence-grounded verification. Building upon this framework, we further contribute a dual-level, evidence-grounded, multimodal dataset comprising organization-level Scope 3 disclosures extracted from heterogeneous sustainability reports. Scope3Trace enables reliable extraction and transparent integration of heterogeneous sustainability disclosures, achieving high accuracy in extracting Scope 1-3 totals and category-level disclosures from sustainability reports.

---

## uid: `doi:10.2139/ssrn.7145639`

- title: Measuring Corporate Governance with Large Language Models
- authors: Jens Frankenreiter
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7145639
- keyword hits: large language model, large language models, llm

### abstract

Empirical corporate governance research depends on structured data extracted from legal text, a translation exercise that has traditionally required costly and difficult-to-scale human coding. Using the DECODEM benchmarks developed in companion work, this paper asks what role LLM-based extraction can play in governance data production: whether automated extraction routines perform on par with realistic human coding workflows and whether model-human disagreement can guide audits of human-coded data. The paper's main findings are based on a blind adjudication of observations on which human coding and the automated extraction routines disagree. The analysis supports three main findings. First, for many governance variables, LLM-based extraction performs at levels at least comparable to feasible human coding workflows, at less than two percent of the marginal cost of human coding. Second, different extraction routines often make only partially overlapping errors, creating value from ensemble rules that aggregate multiple routines. In the setting studied here, labels generated through ensemble rules agree with the adjudicated labels substantially more often than initial human labels did. Third, substantial variation across variables remains, so LLM-generated governance variables should not be used for downstream research without validation against hand-collected data. The results also carry an implication for settings where fully automated coding is not appropriate: because human and model errors also overlap only weakly, flagging observations on which any of six routines disagrees with the initial human label would surface more than ninety percent of observed human coding errors while requiring review of roughly seven percent of observations. Together, the results point towards a new model of data production in which human judgment defines and validates governance variables, while LLM-based extraction supplies scalable coding and targeted quality control.

---

## uid: `arxiv:2607.19430v1`

- title: ChannelGuard: Safe Models Do Not Compose into Safe Multi-Agent Systems
- authors: Elias Hossain, Md Mehedi Hasan Nipu, Fatema Tuj Johora Faria, Tasfia Nuzhat Ornee, Maleeha Sheikh
- affiliations: not stated
- posted: 2026-07-20
- source: arXiv
- link: https://arxiv.org/abs/2607.19430v1
- keyword hits: gpt-5, llama, llm

### abstract

Multi-agent LLM applications chain a planner, worker agents, a verifier, and a synthesizer, and every hop between agents is an unmonitored channel through which an adversary can smuggle instructions. Existing defenses guard only the input boundary (IBProtector, Llama Guard, perplexity filters, SmoothLLM) or run outside the application as opaque, stochastic provider-side filters. We show this gap carries a consequence rarely measured: on a 2,100-trace evaluation across eight attack families, five defenses, and three model backends, an undefended pipeline that appears fully safe under standard reporting (attack success 0.000 on tool- and memory-poisoning) owes that safety almost entirely to the cloud provider's server-side filter (54 of 60 blocks on Azure GPT-5), and silently shifts to the agent model's own alignment on a backend without such a filter. Outcome-only reporting hides this dependence. We present ChannelGuard, a training-free defense-in-depth framework placing information-bottleneck gates on every inter-agent channel; each scores channel text against an adversarial phrase bank by embedding similarity and deterministically passes, compresses, or blocks it, adding no LLM call, while an attribution method records which layer stopped each attack. ChannelGuard's tool-output gate blocks Tool Poisoning 30 of 30 at the application layer, identically across Azure GPT-5, Anthropic Sonnet 4.5, and Anthropic Haiku 4.5, whereas the undefended pipeline shifts entirely across backends; it also lowers Prompt Injection attack success by half (0.333 to 0.167) and preserves GSM8K accuracy exactly (0.867). White-box adaptive paraphrase evades every embedding gate, where a perturb-and-vote baseline does better. An extended appendix adds baselines, ablations, sweeps, a benign-preservation analysis, and a judge audit (kappa = 0.900), at a total cost of 47.36 USD.

---

## uid: `doi:10.2139/ssrn.7069438`

- title: Stereotypes in the Machine: Gender and Racial Bias in LLM-Generated Financial Advice
- authors: Ang Li, Fujing Xue, Zixuan Zeng, Xiaofeng Zhao
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7069438
- keyword hits: large language model, large language models, llm, llms

### abstract

We conduct a large-scale controlled experiment of large language models (LLMs) acting as financial advisors. We find that LLMs systematically recommend lower equity allocations to female and Asian clients compared to otherwise identical White males. This bias persists and even intensifies for financially sophisticated clients, and the recommended portfolios are less efficientrejecting rational statistical discrimination in favor of stereotyping. While higher model intelligence mitigates these biases, model scale, standard safety alignment, and explicit debiasing prompts prove ineffective. Our results suggest that without advanced reasoning capabilities, AI advisors risk institutionalizing wealth disparities by projecting demographic stereotypes onto investment decisions.

---

## uid: `doi:10.2139/ssrn.7152490`

- title: Explainable Risk Assessment and Intelligent Maintenance for Electrochemical Energy Storage System with Large Language Model
- authors: Yijie Wang, Yujie Fu, Yi Lu, Jingbo Qu, Putai Zhang, Mian Li
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7152490
- keyword hits: large language model, llm, llms, qwen

### abstract

With large-scale deployment of Electrochemical Energy Storage System (EESS), risk assessment plays a vital role in maintaining EESS safety. However, due to the variable operation conditions and complex structure of EESS, existing risk assessment methods cannot be objective and comprehensive enough to reflect real-time risk. Besides, assessment results are difficult to directly provide clear guidance to correct the identified risk, reducing the efficiency of EESS Operation and Maintenance (O&M). With Large Language Model (LLM), this framework is proposed for EESS explainable risk assessment and intelligent maintenance. A hierarchical risk assessment is established based on real-time sensor data and expert opinions, providing an objective and comprehensive tool to reflect real-world operational risks in EESS. Furthermore, LLM is applied to bridge domain knowledge about EESS safety and hierarchical risk assessment, so that the proposed framework is able to explain why those risks are identified and how those risks propagate to further influence EESS safety by coupling relationship graph. Finally, the framework enables LLM to generate corresponding detailed suggestions for the guidance of EESS maintenance, improving the efficiency of EESS O&M. The main contribution is to construct a comprehensive and explainable risk assessment for decision-making support, bridging the gap between risk assessment and practical EESS O&M. Deployed in six in-service EESS stations, the proposed framework effectively identifies critical risk contributors in each station and has satisfactory performance in assessment explanation, generation of O&M suggestions with advanced full-scale LLMs such as Kimi-K2.6, and understanding of domain knowledge with 7B/14B-scale fine-tuned LLMs such as Qwen3-8B.

---

## uid: `doi:10.2139/ssrn.7149599`

- title: Generative AI and Idea Implementation: An Attention-Based View
- authors: Luke Rhee
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7149599
- keyword hits: chatgpt, generative ai, generative artificial intelligence

### abstract

Research on innovation has emphasized that generating ideas is insufficient for creating value; ideas must be implemented through collective effort. Although recent scholarship highlights generative artificial intelligence (AI) as a tool for ideation, little theory and evidence explain whether and how it affects idea implementation. We theorize generative AI as a communication technology that facilitates implementation through the attention it helps ideas attract. Implementation depends on whether colleagues notice and engage with an idea, and generative AI lets users express it in terms more accessible and relevant to each audience, drawing greater attention and support. We test this in a longitudinal field experiment at a software company piloting ChatGPT Enterprise. Of 287 workers, 140 were randomly assigned access and 147 served as controls. Combining two survey waves with the firm’s performance evaluations in a difference-in-differences design, we find that employees with access contributed significantly more to advancing ideas into products, services, and processes. They attracted 23.5% more attention from colleagues, and mediation analyses indicate this attention partially explains the effect, especially for employees in brokerage positions. By theorizing generative AI as a technology that aids implementation, this study reframes it as an enabler of a critical, overlooked stage of innovation.

---

## uid: `doi:10.2139/ssrn.7018978`

- title: ClinQuery: Retrieval-Augmented Clinical Question Answering from Ambulatory Visit Conversations
- authors: Abhishek Kumar
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7018978
- keyword hits: gpt-4, large language model, llm, prompting, retrieval-augmented

### abstract

Clinical Question Answering (Clinical QA) from patient-provider conversations aim to answer natural-language clinical queries directly from visit dialogues without relying on manually created documentation. This capability is essential for ambulatory care information retrieval and serves as a foundation for point-of-care clinical decision support. Despite recent advances, prior works remain limited. Generic medical QA systems and Large Language Model (LLM) prompting over complete transcripts often depend heavily on parametric knowledge or lexical matching. Therefore, they suffer from a conversational retrieval gap, where colloquial patient expressions fail to align with clinically formulated questions, preventing relevant evidence from being identified. Although Retrieval-Augmented Generation (RAG) works partially address this issue through external retrieval mechanisms, they frequently show ungrounded generation drift, producing answers that are not fully supported by the retrieved conversational evidence and may introduce inaccurate medications, dosages, or timelines. To address these challenges, we propose ClinQuery, a RAG designed specifically for clinical QA from visit conversations. ClinQuery is built on the hypothesis that biomedical semantic retrieval over conversational segments, combined with evidence-conditioned generation, can provide accurate and faithful answers grounded in the source dialogue. The framework operates in two stages: (1) biomedical semantic retrieval, which bridges the linguistic gap between colloquial and clinical language, and (2) evidencegrounded answer generation, which constrains response generation using retrieved conversational evidence. The proposed framework achieves an F1 score of 0.812 and faithfulness of 0.887 on ACI, an F1 score of 0.794 on VirtAssist, and an F1 score of 0.779 on VirtScribe. Compared with zero-shot GPT-4 and standard RAG baselines, ClinQuery improves average F1 performance by 13.6% and reduces hallucinations by 21.4%, while maintaining low-latency single-pass retrieval suitable for real-world clinical workflows.

---
