# Classification batch 1 of 5, edition 1

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-001/batch-1.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7153923`

- title: Leveraging LLMs for Automated Requirements Quality Verification in Automotive Software: An Empirical Industrial Study
- authors: Youssef Bikouche, Hamid El Ghazi
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7153923
- keyword hits: chain-of-thought, deepseek, fine-tuning, gpt-5, large language model, large language models, llm, llms, prompt engineering, qwen

### abstract

Reviewing software requirements for quality defects is a slow and repetitive task in automotive software development. Requirements Specification Part (RSP) documents follow strict proprietary standards covering naming conventions, control flow notation, and variant applicability rules. When these rules are violated, defects propagate into later development stages and cause expensive rework. This paper studies whether Large Language Models (LLMs) can automatically detect these violations by applying a fixed set of quality rules specified entirely through prompt engineering, with no model fine-tuning. We define 25 verification rules drawn from real industrial practice and evaluate five LLMs (GPT-5-Mini, DeepSeek-V4-Flash, GPT-OSS-20B, GLM-4.7-Flash, and Qwen3-32B) across three prompt strategies (zero-shot, few-shot, and chain-of-thought) on two datasets: 80 clean and 80 defect-injected requirements taken from production automotive RSP documents, producing over 8,000 individual LLM inferences. GPT-5-Mini and DeepSeek-V4-Flash achieve a 0% false positive rate with F1 scores above 0.96 across all prompt variants. Weaker models show consistent hallucination patterns tied to specific rule families, and prompt strategy matters for these models while making no difference for strong ones. DeepSeek-V4-Flash, an open-weight model, matches the 0% false positive rate of the top tier and comes within 0.010 F1 points of GPT-5-Mini, making it a practical option for deployments where data must stay on-premise. These results show that near-production-quality requirements verification is achievable without fine-tuning for rule-based tasks of this kind, and identify a capability threshold above which model selection matters more than prompt strategy.

---

## uid: `doi:10.2139/ssrn.7119484`

- title: AI Trading: Evaluating Large Language Models for Technical Market Analysis
- authors: Geofrey Ntale
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7119484
- keyword hits: claude, fine-tuning, gemini, gpt-4, large language model, large language models, llama, llm, llms

### abstract

The convergence of artificial intelligence and financial markets has produced a fundamental shift in how trading decisions are conceived, evaluated, and executed. Large Language Models (LLMs), initially designed for natural language understanding, have emerged as a powerful class of tools capable of processing the heterogeneous information environments that characterize modern financial markets. This paper presents a systematic, comparative evaluation of five prominent LLMs, specifically GPT-4 Turbo, Claude 3 Opus, Gemini 1.5 Pro, Llama 3 70B, and the domain-specialized FinGPT, with respect to their capacity for technical market analysis. The evaluation spans four structured tasks: candlestick pattern recognition from Open-High-Low-Close-Volume (OHLCV) data, directional signal generation with BUY/SELL/HOLD classification, backtesting of signal quality through a simulated execution pipeline, and financial report comprehension measured against established benchmarks. Our experimental framework employs rigorous quantitative metrics, including Sharpe ratio, maximum drawdown, Sortino ratio, information coefficient, F1-score, and BLEU score, alongside standard confusion-matrixderived classification metrics. Findings from simulated backtesting indicate that GPT-4 Turbo achieves the highest annualized return and Sharpe ratio among general-purpose models, while FinGPT demonstrates competitive risk-adjusted performance attributed to its domain-specific fine-tuning. Both models outperform a passive S&amp;amp;P 500 benchmark under the tested conditions. The study identifies persistent failure modes across all evaluated models, including numerical hallucination, context-window limitations, and inconsistent performance in sideways market regimes. These findings suggest that while LLMs hold genuine promise as components within ai trading systems, robust deployment requires careful task decomposition, rigorous backtesting protocols, and domain-aware fine-tuning strategies. The paper concludes with a discussion of practical and ethical implications, as well as a structured agenda for future research in multimodal market intelligence and reinforcement learning-augmented trading agents.

---

## uid: `doi:10.2139/ssrn.7120478`

- title: Foundation Models and Large Language Models in Healthcare: A Narrative Review of Applications, Evidence, and Emerging Challenges
- authors: Babatola Joshua
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7120478
- keyword hits: fine-tuning, foundation model, large language model, large language models, llm, llms, prompting

### abstract

Foundation models and large language models (LLMs) have moved rapidly from generalpurpose natural language processing tools to candidate components of clinical infrastructure. Trained on broad corpora and subsequently adapted through fine-tuning, retrieval augmentation, or prompting, these systems now demonstrate competitive performance on medical licensing examinations, clinical documentation, diagnostic reasoning, and patient communication tasks. This review synthesises the technical foundations of LLMs in healthcare, traces their evolution from transformer-based architectures to multimodal clinical foundation models, and critically appraises the peer-reviewed evidence base underpinning their clinical use. Drawing on studies published predominantly between 2019 and 2025, the review examines applications across documentation, decision support, patient-facing communication, and biomedical research, and situates these applications within a broader discussion of reliability, bias, privacy, interpretability, and regulatory status. The evidence indicates that although benchmark and simulated-case performance is often impressive, prospective clinical validation remains limited, and demonstrated capability does not yet equate to demonstrated safety or effectiveness in routine care. Persistent challenges include hallucination, uneven performance across demographic subgroups, ambiguous regulatory classification, and the practical difficulty of integrating probabilistic language systems into accountable clinical workflows. The review concludes that foundation models are best conceived as adjunctive tools requiring structured human oversight, robust governance, and prospective evaluation rather than autonomous clinical agents, and it proposes priority directions for future research, including standardised evaluation frameworks, equity-focused benchmarking, and longitudinal outcome studies.

---

## uid: `doi:10.2139/ssrn.7155798`

- title: Improving cultural ecosystem service assessment from social media data using domain-adaptive large language models
- authors: Yufei Chen, Shiqin Dai, Yiming Lei, Lei Zhao, Jiabo Xie, Ruiqing Qin, Kangping Meng, Qinhua Fang
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7155798
- keyword hits: fine-tuning, gemini, large language model, large language models, llm, llms, prompting, retrieval-augmented

### abstract

Cultural ecosystem services (CES), which link ecosystems and human well-being, are increasingly assessed using social media data. As state-of-the-art natural language processing models, large language models (LLMs) represent a new paradigm for CES research. However, as a long-tailed classification task, CES classification remains challenging for general-purpose LLMs, often resulting in limited classification accuracy and reduced reliability in ecosystem assessments. In this study, we propose LACA (LLM-Augmented CES Assessment), an LLM-enhanced pipeline integrating domain-specialized prompting, fine-tuning (FT) and retrieval-augmented generation (RAG) to improve CES classification. Results demonstrate that, while general-purpose LLMs tend to underestimate long-tail CES categories, the lightweight 8B-parameter LACA consistently outperforms models up to two orders of magnitude larger. Specifically, LACA achieves notable F1-score gains on rare categories, improving by 90.26% over its base model and 37.90% over the strongest baseline, Gemini3-Flash. A case study in Xiamen, China shows that LACA corrects spatial cluster misclassification caused by overestimating mainstream CES and underestimating long-tail categories. Furthermore, it reveals a masked aesthetic-spiritual correlation (ρ= 0.569). By mitigating attribution bias and supply-demand mismatches, LACA enables accurate clustering and captures seasonal and day-night variations in CES perceptions. This study demonstrates that LACA, built on lightweight LLMs, provides a replicable method enabling cost-effective and scalable long-term CES monitoring based on social sensing data.

---

## uid: `doi:10.2139/ssrn.7167544`

- title: Large Language Models on Tabular Data Based Molecular Property Prediction (MPP) of RP-3 Kerosene
- authors: Muhammad  Hassaan Athar, Yong Hu, Wenbin Yu, Feiyang Zhao
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7167544
- keyword hits: large language model, large language models, llama, llm, llms, text embedding

### abstract

Accurate prediction of multicomponent fuel properties is a longstanding bottleneck in surrogate fuel design, where nonlinear composition property relationships limit the reliability of empirical correlations and conventional machine learning (ML). In present study we show that large language models (LLMs) pretrained on molecular and general-purpose text corpora can predict physiochemically distinct properties of RP-3 kerosene surrogates with near unity accuracy directly from SMILES strings and tabular to text embeddings. Evaluating four supervised ML model (SVM, GPR, RF and k-NN) against three transformer-based representations (ChemBERTa, MolFormer and TinyLlama (1.1B)) across the smaller and larger datasets, we found that the predictive performance is governed by an interplay between data scale and representation chemistry. At small sample size, TinyLlama yielded the most stable embeddings (R2 = 0.9962), where at scale, ChemBERTa SMILES pretraining surpasses all other models, explaining 99.95% of property variance (RMSE = 0.126, MRE = 0.18%), outperforming both MolFormer and TinyLlama, as well as supervised ML models. Notably, TinyLlama lacking any chemistry specific pretraining, still achieves R2 = 0.995 purely from serialized composition and structured prompts, demonstrating that contextual language embeddings alone encode transferable chemical information. Cosine similarity and residual analyses further confirms that the pretrained representations capture meaningful differences between aromatic and saturated hydrocarbon structures while maintain strong predictive stability. These findings demonstrate that pretrained language models can provide a scalable and chemically informed alternative to conventional composition-based regression for RP-3 kerosene fuel property prediction, with potential applications in surrogate fuel design, combustion kinetic modeling and molecular property prediction (MPP).

---

## uid: `doi:10.2139/ssrn.7158001`

- title: Generative AI Regulation, Creative Industry Disruption, and Governance Response in China's Cultural Sector
- authors: Gh U
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7158001
- keyword hits: generative ai, large language model, large language models, llm, llms

### abstract

Text generators based on large language models (LLMs), AIGC (Artificial Intelligence Generated Content), and models that transform text into images or videos have been rapidly transforming cultural industries. As GenAI platforms started to enter the market, China’s state regulators, from the Cyberspace Administration of China (CAC) to the National Press and Publication Administration (NPPA), have been working to establish a new governance architecture to deal with the emerging industrial component. This study investigates the relationship between AIGC adoption intensity in the creative sector and the governance quality of corresponding regulations. Using firm-level panel data from 2020 to 2024 covering all listed cultural enterprises engaged in film, music, publishing, and interactive media, this study adopts a difference-in-differences (DiD) identification strategy based on staggered provincial implementation of licensing enforcement by authorities at the national and provincial levels, as well as an event-study design focusing on CAC announcements related to AIGC. The results show that effective governance quality can make a significant difference in the scale and pattern of labour displacement caused by AIGC adoption. The impact varies across levels of governance quality and firm characteristics. State-affiliated platforms have enjoyed remarkable advantages in AIGC compliance, perpetuating existing structural inequalities between platform operators and independent creators. The simulation results suggest that an incremental improvement of the regulatory quality at the provincial level, up to a certain point, may help to decrease the creative workforce displacement rate by certain percentages. Building on these findings, the paper discusses the possible implications for upgrading the governance instruments and systems for AIGC in China, developing international AI cultural governance frameworks within the UNESCO and WIPO frameworks, and protecting creative labour rights in emerging cultural economies dominated by AI.This list of completed research projects on Generative and Interactive Gaming Technologies (AIGC) explores the issues concerning the interaction and control between generative AI and its governance, and its impact on creative industry and business models related to it. Some projects also focus on the cultural governance and relevant Chinese policies. The methodologies used include differential analysis, empirical studies, and critical thinking.

---

## uid: `doi:10.2139/ssrn.7073158`

- title: LLM-Assisted Proofreading A Study of the Effectiveness of 13 Free AI Detection Tools
- authors: Kariema El Touny
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7073158
- keyword hits: claude, gemini, large language model, large language models, llm, llms

### abstract

This study investigates the effectiveness of 13 free online AI-content detection tools when applied to texts edited by large language models (LLMs) at varying levels of proofreading. Seven original texts spanning academic, journalistic, fictional, and professional genres were processed through three LLMs (Copilot, Claude, and Gemini) across four editing levels, ranging from grammar correction to full rewrite. Outputs were scanned by multiple detectors, with results systematically recorded and compared. Findings reveal significant inconsistencies across tools, with some detectors returning human-written verdicts regardless of proofreading level, while others flagged original, unmodified texts as AI-generated. Most notably, detection scores were found to correlate more strongly with genre and writing style than with the degree of LLM intervention, suggesting that these tools function more as style detectors than as AI detectors. Technical limitations of the tools used in this study significantly constrained the experiment, highlighting their unreliability and limited suitability as trustworthy instruments for identifying LLM-assisted writing.

---

## uid: `doi:10.2139/ssrn.7146358`

- title: Physicians' Experiences of Generative AI-Assisted Diagnostic Reasoning and Perceived Applicability in the Kenyan Healthcare Context: A Qualitative Study from a Tertiary Teaching Hospital
- authors: Roselyter  Monchari Riang&apos;a, Soraiya Manji, Norah Obungu, See PDF
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7146358
- keyword hits: chatgpt, generative ai, generative artificial intelligence, gpt-4, large language model, llm

### abstract

Background: Generative artificial intelligence (AI), particularly large language model (LLM)-based tools, offers new opportunities to support clinical reasoning and diagnostic decision-making. However, direct experiential evidence on how frontline physicians in low- and middle-income countries engage with these tools in practice remains largely absent from Literature.&lt;br&gt;&lt;br&gt;Methods: Embedded in a wider multi-site parallel group randomized controlled trial study, we conducted a qualitative descriptive study guided by a constructivist-interpretivist paradigm anchored on the Normalisation Process Theory(May &amp;amp; Finch, 2009) framework. Semi-structured exit interviews were conducted with 19 physicians across diverse departments at a Kenyan tertiary teaching hospital immediately following structured diagnostic simulations with a generative AI chatbot (ChatGPT-4o API access). Data was analysed inductively through reflexive thematic analysis.&lt;br&gt;&lt;br&gt;Findings: Ten sub-themes emerged within two overarching domains. Perceived benefits included broadened differential diagnoses beyond initial formulation, more structured history-taking and clinical reasoning, targeted investigation planning, enriched patient education, and consolidated workflow efficiency. Contextual barriers included workflow incompatibility with high-volume clinical settings, systematic misalignment between AI outputs and local epidemiology and resource availability, physician concern that visible AI use during consultation would undermine clinical authority and patient trust — a finding rooted in the relational architecture of the African clinical encounter — interface usability limitations, and risk of overreliance with reduced critical engagement.&lt;br&gt;&lt;br&gt;Interpretation: Kenyan physicians showed strong readiness to engage with generative AI as a clinical thinking partner, but structural, epidemiological, and relational barriers prevented routine clinical enactment. These findings reframe AI implementation in African health systems from a technical deployment problem to a sociotechnical integration challenge requiring localised model training, workflow-sensitive interface design, and institutional renegotiation of AI's role in the clinical encounter.

---
