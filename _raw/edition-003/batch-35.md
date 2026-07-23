# Classification batch 35 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-35.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7013259`

- title: Selling with AI Voice Agents: Does Disclosure Still Matter?
- authors: Johannes Habel, Jan Zawadzki, Paul Freise
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7013259
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

Artificial intelligence (AI) voice agents are increasingly deployed to sell to customers on the phone, prompting legislation that requires firms to disclose when customers are interacting with AI. Prior research, based on data collected before large language models (LLMs) became widely used, concluded that such disclosure harms sales performance because customers hold prejudices against AI. We revisit this question in the contemporary AI era through three studies. A randomized field experiment (N = 1,337 customers reached) shows that disclosing an AI voice agent no longer reduces conversion rates relative to nondisclosure. A second randomized field experiment (N = 366 customers reached) demonstrates, however, that AI voice agents still substantially underperform human sales agents. This is because contemporary AI voice agents continue to struggle with sales process discipline, including stakeholder qualification, value communication, persistence, and next-step orchestration. Finally, an online experiment (N = 238) reveals that customers largely recognize AI voice agents regardless of disclosure and evaluate disclosed and nondisclosed AI similarly. Customers are less willing to continue a conversation with them because they anticipate that these agents exhibit lower empathy, are less human-like, require greater effort, and signal greater firm insincerity. In summary, our findings suggest that mandatory AI disclosure may no longer be the primary challenge facing sales operations deploying AI voice agents. Instead, managers should focus on improving AI sales-process execution and selectively deploying AI voice agents while recognizing the value of human sales agents.

---

## uid: `doi:10.2139/ssrn.7128878`

- title: In 2026, Can AI "Humanizers" Outsmart AI Text Detectors?
- authors: Roman Lesnov
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7128878
- keyword hits: claude, large language model, large language models, llm, llms, prompt engineering

### abstract

Research into AI-generated writing and its detection is growing, yet it struggles to keep pace with rapid technological advancements in AI. The rapid development of large language models (LLMs) and other AI-powered technologies, such as AI-writing detectors, demands ongoing, accelerated scholarly efforts to assess their potential and limitations. A relatively underexplored area involves text manipulation techniques that can mislead AI detectors, such as prompt engineering for human-like output and "humanizing" AI-generated text with software. Some studies have found that humanized essays greatly reduce AI detection accuracy (e.g., Taloni et al., 2023), but more research is needed on newer, more advanced detectors and humanizers. This study aims to bridge this gap by comparing how two text-manipulation methods affect AI detection accuracy: (1) prompt-based manipulation, like asking an LLM to write an essay and make it undetectable, and (2) AI humanization with an AI humanizer tool. The study used 20 AI-generated essays that were humanized via prompt in the Claude Sonnet 4.6 LLM (Anthropic, 2026). The same 20 AI-generated essays were also humanized with Undetectable AI, a paid AI humanization tool. The research question was: “How accurate are the selected AI detectors at identifying AI-humanized essays?” To answer this research question, each essay was analyzed by three subscription-based AI detectors— Originality AI , Pangram , and Winston AI —and the results were averaged for each detector. The results showed that the AI detectors did an excellent job recognizing prompt-humanized essays as machine-generated but failed to recognize essays that had been humanized via software. These findings suggest that AI detectors are not yet reliable enough to stand alone as proof in academic writing evaluations and may not effectively discourage AI use. It is, therefore, recommended that writing instructors prioritize other AI-deterring strategies, such as developing a clear AI policy, using AI-resistant assessments, and fostering AI literacy among students.

---

## uid: `doi:10.2139/ssrn.7025538`

- title: DataPrep-bench: Benchmarking LLMs as Training Data Preparators
- authors: Hao Liang, Qifeng Cai, Yibo Lin, Jianzhuo Du, Qifeng Xia, Sizhe Qiu, Linzhuang Sun, Meiyi Qiang
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7025538
- keyword hits: fine-tuning, large language model, large language models, llama, llm, llms

### abstract

The quality of training data fundamentally determines the capabilities of large language models (LLMs), yet no unified benchmark exists to measure how well LLMs, agents, and data-centric workflows actually prepare training data end to end. We view LLM-driven data preparation as comprising two complementary capabilities: data construction, which transforms raw sources into supervised training data, and data quality evaluation, which predicts the training value of candidate datasets before downstream training; throughout, “quality” refers to downstream training utility rather than surface-level textual properties. We introduce DataPrep-Bench, the first unified benchmark that jointly evaluates both capabilities under a shared downstream-grounded protocol over six domains and multiple base models. For data construction, methods consume identical raw sources and are scored by fine-tuning a base model on their outputs jointly with Dolly-15k; alongside this track we release Data-Construction-Skill, a skill-guided agent that lifts the Dolly-only baseline by nearly 20 points absolute on Llama-3.1-8B Finance and is competitive with the strongest agent- and DataFlow-based methods in knowledge-extraction-dense domains. For data quality evaluation, scoring functions are scored by Pearson correlation with downstream performance on a shared candidate pool; we release the Distributional Alignment Score (DAS), a distribution-based evaluator that uses MMD between a candidate dataset and a domain proxy. DAS attains the strongest cross-model correlation in four of six domains and is the only metric clearing r > 0.70 simultaneously in Math, Science, and Medical, outperforming existing quality-, diversity-, and heuristic-based evaluators. DataPrep-Bench provides a unified, downstream-grounded framework for measuring progress on both capabilities as co-equal targets of LLM-driven data preparation.

---

## uid: `doi:10.2139/ssrn.7158720`

- title: Agentic Digital Twins for Community Energy Management: LLM-Orchestrated Control with Physics-Informed Simulation and Carbon-Aware Planning
- authors: Rui Wang
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7158720
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Buildings account for approximately 40% of global energy consumption and associated carbonemissions. Community-level demand flexibility through coordinated battery storage dispatch offerssignificant potential for peak demand reduction and carbon mitigation, yet existing control approachesface fundamental limitations: model predictive control (MPC) requires accurate system models andstruggles with distribution shift; deep reinforcement learning (DRL) is sample-inefficient and brittleto unseen scenarios; and standalone large language models (LLMs) lack physical grounding forsafe real-time control. This paper presents an agentic digital twin framework that integrates LLM-based reasoning with physics-informed digital twin simulation and machine learning forecastingtools. The LLM serves as an orchestrator that queries the twin state, invokes forecasting models,evaluates counterfactual dispatch scenarios through twin simulation, and commits carbon-awarebattery schedules. We evaluate the proposed method against four baselines — rule-based control,MPC, proximal policy optimization (PPO), and a standalone LLM without twin access — on theCityLearn 2020 benchmark across three California climate zones (hot-humid, hot-dry, and cold) with9 buildings and 30-day episodes. Results demonstrate that the agentic twin achieves 21.5% lowerpeak demand than DRL (𝑝

---

## uid: `arxiv:2607.20270v1`

- title: Which Values Do LLMs Confuse? A Schwartz-Based Recognition Study
- authors: Andrei Chetvergov, Stepan Ukolov, Timofei Sivoraksha, Alexander Evseev, Mikhail Solovev, Valeriia Kuschenko, Maria Chistyakova, Sergey Bolovtsov
- affiliations: not stated
- posted: 2026-07-22
- source: arXiv
- link: https://arxiv.org/abs/2607.20270v1
- keyword hits: instruction-tuned, large language model, large language models, llm, llms

### abstract

Large language models are increasingly evaluated through the values they endorse, but such evaluations presuppose that models can identify the value expressed in a concrete situation. We study this prerequisite as controlled top-1 recognition over Schwartz's ten basic values. Our evaluation set contains 1,000 Russian situational texts, balanced across the ten values and independently labeled by two human annotators per item. We evaluate 21 instruction-tuned LLM runs under a fixed ranked-response protocol; 20 runs with reliable outputs form the semantic panel. Pooled Acc@1 is 0.683 and Acc@3 is 0.892, showing that models often locate the correct motivational region while ranking close alternatives unstably. Adjacent values account for 50.9% of semantic errors, compared with 24.4% under a checkpoint-specific null. Eight directed confusions recur across checkpoints and human-confirmed subsets. Several are strongly asymmetric, including Universalism to Benevolence, Tradition to Conformity, and Security to Power, whereas Stimulation-Hedonism forms a bidirectional boundary. Their severity is checkpoint-specific and can bias higher-order value profiles. The results motivate value-recognition evaluation that combines exact accuracy, ranked recovery, and directed error analysis.

---

## uid: `doi:10.2139/ssrn.4593895`

- title: A Survey of GPT-3 Family Large Language Models Including ChatGPT and GPT-4
- authors: Katikapalli Subramanyam Kalyan
- affiliations: not stated
- posted: 2023-10-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.4593895
- keyword hits: chatgpt, gpt-3, gpt-4, large language model, large language models

### abstract

NOT AVAILABLE. You have title and authors only. Set bullet_provenance to "none", return an empty bullets array, and classify field and role only if the title makes it unambiguous.

---

## uid: `doi:10.3386/w32327`

- title: Recovering Overlooked Information in Categorical Variables with LLMs: An Application to Labor Market Mismatch
- authors: Yi Chen, Hanming Fang, Yi Zhao, Zibo Zhao
- affiliations: not stated
- posted: 2024-04-15
- source: NBER
- link: https://doi.org/10.3386/w32327
- keyword hits: large language model, large language models, llm, llms

### abstract

Categorical variables have no intrinsic ordering, and researchers often adopt a fixed-effect (FE) approach in empirical analysis.However, this approach has two significant limitations: it overlooks textual labels associated with the categorical variables; and it produces unstable results when there are only limited observations in a category.In this paper, we propose a novel method that utilizes recent advances in large language models (LLMs) to recover overlooked information in categorical variables.We apply this method to investigate labor market mismatch.Specifically, we task LLMs with simulating the role of a human resources specialist to assess the suitability of an applicant with specific characteristics for a given job.Our main findings can be summarized in three parts.First, using comprehensive administrative data from an online job posting platform, we show that our new match quality measure is positively correlated with several traditional measures in the literature, and at the same time, we highlight the LLM's capability to provide additional information conditional on the traditional measures.Second, we demonstrate the broad applicability of the new method with a survey data containing significantly less information than the administrative data, which makes it impossible to compute most of the traditional match quality measures.Our LLM measure successfully replicates most of the salient patterns observed in a hard-to-access administrative dataset using easily accessible survey data.Third, we investigate the gender gap in match quality and explore whether there exists gender stereotypes in the hiring process.We simulate an audit study, examining whether revealing gender information to LLMs influences their assessment.We show that when gender information is disclosed to the GPT, the model deems females better suited for traditionally female-dominated roles.

---

## uid: `doi:10.2139/ssrn.4932769`

- title: A Comprehensive Survey of Large Language Models in Management: Applications, Challenges, and Opportunities
- authors: Hongke Zhao, Chuang Zhao, Likang Wu, Yuqing Shan, Zonghan Jin, Yuanpei Sui, Zipeng Liu, Nan Feng
- affiliations: not stated
- posted: 2024-09-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.4932769
- keyword hits: large language model, large language models, llm, llms

### abstract

This survey examines the transformative impact of Large Language Models (LLMs) and AI-driven systems across three critical and interconnected business domains: Finance, Marketing, and Supply Chain Management (SCM). As these technologies reshape business management, our analysis explores their roles in enhancing operational efficiency, fostering strategic insights, and driving economic growth. Unlike previous studies that only focus on an isolated and micro application aspect, this research integrates insights across finance, marketing, and SCM, highlighting individual advancements and these technologies' synergistic effects. In finance, LLMs revolutionize market predictions, risk assessments, regulatory compliance, fraud detection, etc. For marketing-related businesses, it enables hyper-personalized consumer engagements, optimizes resource allocation, and boosts conversion rates. SCM benefits from improved demand forecasting and more intelligent logistics optimization, ensuring agility and resilience in the LLM-driven system. This integrative approach provides a comprehensive understanding of LLM's impact and offers a robust framework for leveraging these technologies in the complex dynamics of modern business ecosystems.

---
