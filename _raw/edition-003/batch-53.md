# Classification batch 53 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-53.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6986775`

- title: Large Language Models, Supervision, and Labor Demand: Evidence from Online Recruitment Data
- authors: Chenyang Wei, Nalinjie Jia
- affiliations: not stated
- posted: 2026-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6986775
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are rapidly diffusing into text and information intensive work. However, their impacts on labor market may differ from traditional automation because LLM outputs are stochastic and require human supervision. Theoretically, this paper incorporates endogenous supervision into canonical task-based model and empirically tests its effect on firm-level labor demand, using a large-scale panel of Chinese online recruitment data. Results indicate that higher LLM exposure is associated with lower hiring, especially for cognitive labor. However, this displacement effect is moderated by an occupation’s supervision requirements; the interaction between LLM and supervision exposure is robustly positive, and can even drive net hiring expansion in certain settings. Heterogeneity analyses reveal significant organizational and institutional complementarities. Large firms exhibit stronger cognitive displacement, while the supervisionmoderation effect is more pronounced in regions with robust legal and market institutions. Consequently, our findings suggest that steering LLM diffusion toward inclusive labor augmentation requires complementary investments in operational supervision skills and supportive institutional infrastructure.

---

## uid: `arxiv:2606.25442v1`

- title: PolicyAlign: Direct Policy-Based Safety Alignment for Large Language Models
- authors: Chang Wu, Junfeng Fang, Houcheng Jiang, Kai Tang, Pengyu Cheng, Xiaoxi Jiang, Guanjun Jiang, Xiang Wang
- affiliations: not stated
- posted: 2026-06-24
- source: arXiv
- link: https://arxiv.org/abs/2606.25442v1
- keyword hits: large language model, large language models, llm, llms, qwen

### abstract

Safety alignment of large language models (LLMs) typically depends on high-quality supervision data, such as safe demonstrations or preference pairs. However, in real-world deployment, emerging safety requirements are often specified as natural-language policies, while corresponding supervision data may be costly, delayed, or unavailable. This creates a mismatch between rapidly evolving safety policies and conventional data-driven alignment methods. To address this, we propose PolicyAlign, a simple yet effective framework for directly aligning LLMs with safety policies. Given a safety policy, PolicyAlign first synthesizes policy-violating instructions and then performs on-policy self-distillation to internalize policy-guided behavior. To improve training stability and data efficiency, we further introduce Policy-Sensitive Filtering, which selects instructions where the policy induces the largest behavioral shift. Experiments across multiple models show that PolicyAlign consistently improves safety while maintaining low over-refusal and preserving general capabilities. PolicyAlign also generalizes to medical, legal, and financial safety scenarios, highlighting its potential as a scalable and maintainable approach to policy-based LLM safety alignment. The code is released at https://github.com/Qwen-Applications/PolicyAlign.

---

## uid: `doi:10.2139/ssrn.6997673`

- title: Mechanistic Interpretability of Cognitive Complexity in LLMs via Linear Probing using Bloom’s Taxonomy
- authors: Bianca Raimondi, Maurizio Gabbrielli
- affiliations: not stated
- posted: 2026-06-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6997673
- keyword hits: large language model, large language models, llm, llms

### abstract

The black-box nature of Large Language Models necessitates novel evaluation frameworks that transcend surface-level performance metrics. This study investigates the internal neural representations of cognitive complexity using Bloom's Taxonomy as a hierarchical lens. By analyzing high-dimensional activation vectors from different LLMs, we probe whether different cognitive levels, ranging from basic recall (Remember) to abstract synthesis (Create), are linearly separable within the model's residual streams. Our results demonstrate that linear classifiers achieve high accuracy across all Bloom levels, providing evidence that cognitive level is encoded in a linearly accessible subspace of the model's representations. These findings provide evidence that the model organizes representations according to cognitive difficulty early in the forward pass, with representations becoming increasingly separable across layers.

---

## uid: `arxiv:2606.27446v1`

- title: Causal Connections: Leveraging Multilingual Fine-Tuning for Financial QA@FinCausal 2026
- authors: Akash Kumar Gautam, Serhii Hamotskyi, Christian Hänig
- affiliations: not stated
- posted: 2026-06-25
- source: arXiv
- link: https://arxiv.org/abs/2606.27446v1
- keyword hits: fine-tuning, gpt-4, llama, llm, llms, prompting

### abstract

This paper describes team HSA_CORAL's submission to the FinCausal 2026 shared task on extracting cause-effect relations from financial narratives via extractive question answering in English and Spanish. We compare three modeling families: (i) encoder-only token tagging with multilingual BERT, (ii) encoder-decoder generation with multilingual BART, and (iii) decoder-only LLMs (Llama 3.1 and GPT variants) using prompt refinement, few-shot demonstrations, and supervised fine-tuning. Across settings, prompting and few-shot examples yield competitive performance, while supervised fine-tuning provides the largest gains. Our best system, GPT-4.1 Mini fine-tuned on combined English and Spanish training data, achieves a tied highest score on the English subtask (score 4.8140) and ranks third on Spanish (score 4.7753) under the shared task's LLM-as-a-judge metric. Overall, the results highlight the value of task-specific adaptation and multilingual fine-tuning for cross-lingual transfer in financial causality QA.

---

## uid: `doi:10.2139/ssrn.7002953`

- title: Bridging Cybersecurity Expertise Gaps through Human–LLM Collaboration: Trust, Reliance, and Design Imperatives from a Mixed-Methods Study
- authors: Shahroz Tariq, Ronal Singh, Mohan Baruwal Chhetri, Surya Nepal, Cecile Paris
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7002953
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are increasingly being integrated into cybersecurity workflows as potential support for expertise-constrained triage, but their operational value depends not only on model accuracy but also on how humans interpret, question, trust, and rely on AI-generated advice. We present an exploratory mixed-methods study of human--LLM collaboration in two controlled cybersecurity triage tasks: phishing email triage (text-based, cue-transparent) and intrusion triage over network records (tabular, cue-opaque). Across 58 participants, collaboration was associated with modest gains in phishing triage and larger gains in intrusion triage. Beyond these outcome changes, the results reveal a task-dependent reliance asymmetry: in cue-transparent phishing, participants could verify visible cues and remained stronger arbiters of final decisions, whereas in cue-opaque intrusion triage, definitive LLM responses carried greater influence because independent verification was harder. We therefore treat both tasks as controlled proxy settings for studying collaboration dynamics, not as end-to-end detection benchmarks. Combining qualitative coding of interaction logs with quantitative paired analyses, we show how definitiveness, evidence-linked explanations, and question framing shape reliance, decision revision, and short-term learning. We translate these findings into design imperatives for trustworthy cybersecurity assistants, including calibrated confidence, evidence-linked and contrastive explanations, progressive disclosure, and task-adaptive interaction scaffolds to support calibrated reliance and mitigate automation bias.

---

## uid: `doi:10.2139/ssrn.7002057`

- title: A Reasoning-Enhanced LLM-based Multi-Role Simulation Model for Vertiport Location Selection
- authors: Ming Cheng, Can Li, Wei Liu, Zhongming Jin, Wanjing Ma
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7002057
- keyword hits: generative ai, large language model, large language models, llm, llms

### abstract

As a disruptive transportation mode, the successful deployment of Urban Air Mobility (UAM) hinges on public acceptance, necessitating inclusive stakeholder representation to mitigate community resistance (e.g., the Not In My Back Yard effect) regarding vertiport location selection. However, traditional Stated Preference (SP) surveys struggle to capture public alignment with such unfamiliar technologies. The rigid structure of standard questionnaires fails to accommodate the intricate, multi-dimensional cognitive trade-offs (e.g., balancing operational convenience against safety anxieties) inherent in human decision-making. To capture these social and psychological dynamics, Large Language Models (LLMs) present a paradigm-shifting alternative through their latent capacity for unstructured, common-sense reasoning and heterogeneous role-playing. Standard generative models frequently exhibit homogeneous behavioral patterns and lack deliberate, multi-step reasoning, failing to reliably replicate the profound cognitive friction of real-world stakeholders, a Reasoning-Enhanced Multi-role Simulation (REMS) model was proposed. REMS integrated a "reasoning-before-responding" logic and implemented Proximal Policy Optimization (PPO) as an alignment bridge to distill human preferences into the reasoning paths of the model. Furthermore, a Fuzzy Analytic Hierarchy Process (Fuzzy-AHP) was subsequently employed to transform these simulated reasoning processes into quantitative decision weights, systematically integrating multidimensional criteria such as operational accessibility, safety perceptions, and environmental impacts. Results demonstrate that REMS significantly outperforms non-reasoning baselines in behavioral authenticity and decision consistency. By effectively rectifying cognitive biases inherent in human surveys, REMS successfully replicates the intricate deliberative logic of diverse stakeholders. Ultimately, this study transforms generative AI into a specialized sociological tool, providing an actionable, mathematically robust, and cost-effective decision-support paradigm for the inclusive infrastructure planning of the low-altitude economy.

---

## uid: `doi:10.2139/ssrn.6893079`

- title: Examining Risk Preferences of Econs, KaTs, Humans and LLMs
- authors: Arun Muralidhar
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6893079
- keyword hits: large language model, large language models, llm, llms

### abstract

For decades, the wealth management industry has rested upon the assumption that investors follow predictable, age-based risk trajectories ("Econs"). Behavioral finance opened the door to a different risk preference paradigm ("KaTs). These theories led to the creation of "automatic" default products like Target Date Funds (TDFs) that are finding global acceptance. A variation of the Kahneman-Tversky approach, Risktyle, has shown dramatic heterogeneity among global respondents ("Humans"), and that TDFs are based on an assumption not seen in actual human risk preference. More recently, as Large Language Models (LLMs) begin to serve in a supportive role for financial advice, a new critical requirement emerges-Know Your LLM (KYL). This paper details an experiment that tests the risk preferences of eight prominent LLMs against a 15-question behavioral survey based on Risktyle that was also applied to global respondents. The results indicate that "LLMs" are statistically "off-the-ranch" compared to both academic theories and actual human populations. By comparing these digital personas to global and regional human data, this study illustrates that: (a) academic risk preference personas (Econs and KaTs) do not capture reality of how Humans appear to respond to risky gamble; (b) TDFs are not based on observable global risk preferences (i.e., that risk aversion increases with age); and (c) LLMs cannot be blindly use for investment advice without a better understanding of underlying algorithmic biases.

---

## uid: `doi:10.2139/ssrn.6893379`

- title: Towards AI-Native ERP Systems: Identifying Limitations in Contemporary Enterprise Platforms and Proposing an Intelligent Workflow-Oriented Architecture - A Conceptual Position Paper
- authors: Harsh Bhaveshkumar Trivedi
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6893379
- keyword hits: large language model, large language models, llm, llms

### abstract

Enterprise Resource Planning (ERP) systems have become fundamental components of modern organisations, enabling the integrated management of finance, human resources, procurement, customer relations, and operational processes. Leading platforms such as SAP S/4HANA and Oracle Fusion Cloud have advanced enterprise operations through cloud adoption, real-time analytics, and process standardisation. However, despite these advancements, contemporary ERP systems remain fundamentally process-centric, requiring users to navigate complex interfaces, interpret predefined workflows, and manually interact with multiple modules. Research consistently identifies user training burden, interaction complexity, and limited adaptability as persistent shortcomings of market-leading ERP solutions (AlMuhayfith and Shaiti, 2020; Garg and Khurana, 2017). Simultaneously, the emergence of Large Language Models (LLMs) and intelligent automation has introduced new opportunities for intent-driven, conversational enterprise architectures (Schnepf et al., 2024; Wornow et al., 2024). This paper argues that existing ERP systems have not fully leveraged AI as a primary interaction layer and continue to rely heavily on traditional workflow paradigms. Through a structured comparative analysis of SAP S/4HANA and Oracle Fusion Cloud against an AI-native design framework, this study identifies key architectural limitations and proposes an AI-native ERP model centred on intelligent workflow orchestration, conversational interaction, and autonomous task execution. The feasibility of this architecture is demonstrated through Trifusion Foundry, an AIpowered enterprise platform developed by the author, integrating HRMS, ITSM, role-based security, and intelligent workflow automation. It is acknowledged that, as both researcher and developer of Trifusion Foundry, a potential conflict of interest exists; the platform is therefore presented strictly as a proof-of-concept implementation rather than a comparative benchmark. Findings suggest that AI-native ERP architectures hold significant potential to reduce operational complexity, lower training dependency, and transform enterprise software from process-driven tools into intent-driven organisational platforms. This is a conceptual position paper: it advances and structures the architectural argument through analytical synthesis of existing literature, and explicitly identifies empirical validation, including controlled user studies and benchmark experiments, as essential future work rather than a contribution of this paper.

---
