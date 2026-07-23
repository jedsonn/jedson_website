# Classification batch 1 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-1.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6887539`

- title: The Evolution, Capabilities, Limitations, and Future of Large Language Models (2026): A Comprehensive Review
- authors: Divyansh Shukla
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6887539
- keyword hits: agentic, chain-of-thought, claude, deepseek, gemini, large language model, large language models, llama, llm, llms, prompting, qwen, retrieval-augmented

### abstract

Large language models (LLMs) have emerged as one of the most transformative technological developments of the twenty-first century. Originating from statistical language modelling and neural network research, these systems have grown from modest n-gram models into massively parameterised, multi-trillion-token-trained architectures capable of complex reasoning, code synthesis, scientific hypothesis generation, and open-ended conversation. This review surveys the trajectory of LLM development from foundational language-modelling research through the seminal Transformer architecture (Vaswani et al., 2017) to contemporary frontier models released in 2025–2026, including the GPT, Claude, Gemini, Llama, Qwen, and DeepSeek families. We systematically examine the core technical innovations that have driven progress: the self-attention mechanism, Reinforcement Learning from Human Feedback (RLHF), Constitutional AI, Chain-of-Thought prompting, Mixture-of-Experts (MoE) routing, Retrieval-Augmented Generation (RAG), and emerging agentic paradigms. Benchmark comparisons across MMLU, HumanEval, GSM8K, MATH, and GPQA are presented to contextualise the relative capabilities of major model families. We further analyse domain-specific applications in education, enterprise software, and scientific research, before turning to the critical limitations that temper optimism: hallucination, factual inconsistency, social bias, adversarial fragility, privacy risks, intellectual property concerns, and the substantial environmental footprint of large-scale training. The paper closes with an examination of ethical and societal implications, emerging governance frameworks at national and supranational levels, and a forward-looking synthesis of research directions likely to define the next generation of AI systems, including reasoning-specialised models, embodied agents, neuromorphic integration, and interpretability science. The review is intended as a comprehensive reference for researchers, practitioners, and policy-makers navigating the rapidly evolving LLM landscape in 2026.

---

## uid: `doi:10.2139/ssrn.6734906`

- title: SecCodeAgent: Secure Code Generation from High-Level Natural Language Prompts via an Iterative Multi-Agent Pipeline
- authors: Shigang Liu, Bushra Sabir, Seung  Ick Jang, Yuval Kansal, Yansong Gao, kristen mo, Alsharif Abuadbba, Surya Nepal
- affiliations: not stated
- posted: 2026-05-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6734906
- keyword hits: agentic, chain-of-thought, deepseek, fine-tuning, gpt-3, gpt-4, large language model, large language models, llama, llm, llms, prompting

### abstract

Large language models (LLMs) can generate functional code from natural language prompts, but they often introduce security vulnerabilities. Existing defenses, including fine-tuning and prompt-based methods, are usually evaluated on code-anchored inputs, rely on narrow datasets, or address only part of the secure coding workflow. As a result, their effectiveness on realistic high-level natural language requests remains unclear. This paper presents SecCodeAgent, a multi-stage agentic pipeline for secure code generation from high-level natural language prompts. SecCodeAgent coordinates three specialized agents for code generation, vulnerability detection, and vulnerability patching, and integrates static-analysis-based cross-verification to identify residual flaws. The pipeline operates iteratively through Encouragement Prompting (EP), a structured feedback mechanism that uses rewards, penalties, and vulnerability-specific guidance to improve remediation across rounds. Experiments on LEval, SecEval, and Holmes with GPT-3.5, GPT-4, GPT-4o, DeepSeek, and LLaMA show that iterative EP raises fix success rates from about 0.25--0.30 in early rounds to 0.85--0.95 after refinement, with the largest gains on weaker models. SecCodeAgent also outperforms baseline prompting strategies, including Chain-of-Thought and Chain-of-Code, and achieves near-complete remediation on some open models. Results across Python and C++ further show strong cross-language effectiveness, although C++ remains slightly harder because of static-analysis limitations. Overall, the results show that multi-agent collaboration with iterative prompting and static verification provides an effective framework for secure code generation.

---

## uid: `doi:10.2139/ssrn.6968361`

- title: A Comparative Security Evaluation of AI-Generated Code Across Large Language Models and Programming Languages
- authors: Deniz Aydın, Serif Bahtiyar
- affiliations: not stated
- posted: 2026-06-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6968361
- keyword hits: claude, deepseek, gemini, gpt-5, large language model, large language models, llama, llm, llms, mistral

### abstract

Large Language Models (LLMs) have been widely used in software development, yet the security of AI-generated code remains a critical concern. This research examines security vulnerabilities in code generated by seven LLMs, which are GPT-5, Claude Sonnet 4.5, DeepSeek R1 70B, Gemini 3 Flash, Llama 3.1 405B, Mistral Large 2, and Nova Pro, across four programming languages, which are JavaScript, Python, C++, and Java. We propose a new approach using 100 complex prompts per language identical across the LLMs. We analyzed the most frequent Common Weakness Enumeration (CWE) categories across different LLMs and programming languages. Each snippet was analyzed via a hybrid pipeline that combines three Static Application Security Testing (SAST) tools, which are Semgrep, Snyk and SonarCloud, with manual review. Findings were classified by Common Vulnerability Scoring System (CVSS) severity. The results show that 936 of the 2,800 snippets contain vulnerabilities, and we identified 1,703 vulnerabilities from 36 CWEs, unevenly distributed across languages (JavaScript: 695, Python: 398, Java: 348, C++: 262). Although all LLMs introduce vulnerabilities, their CWE and severity distributions vary significantly across both LLMs and programming languages, with the same model concentrating on different CWE subsets depending on the language. Because raw vulnerabilities ignore differences in code size and vulnerability severity, we introduce two new metrics for a fair comparison, namely Vulnerabilities per Line of Code (V/LoC) and Weighted Security Risk per Line of Code (WSR/LoC). Our research highlights the need for language aware and model aware security measures to mitigate risks in AI-generated code.

---

## uid: `doi:10.2139/ssrn.7140345`

- title: From Synthetic to Real: A Systematic Comparison of Seven Large Language Models for Turkish Emotion Data Generation
- authors: Haydar Tuna, Taymaz Akan
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7140345
- keyword hits: claude, deepseek, gemini, large language model, large language models, llama, llm, llms, mistral

### abstract

Supervised emotion classification for Turkish is limited by a scarcity of large, balanced, human-annotated corpora. Large language models (LLMs) can generate labeled sentences on demand; however, data quality varies across providers, and few studies compare multiple LLMs under a leakage-free design. To address this gap, this study compares seven LLMs as synthetic-data sources for Turkish emotion classification: Claude Opus 4.8, DeepSeek 3.2, Gemini 3.5 Flash, GPT 5.4, Grok 4.3, Llama 4 Scout, and Mistral Large 3. Each model generated approximately 2,000 sentences for each of six emotion categories: happiness, fear, sadness, disgust, surprise, and anger. For each corpus, a BERTurk classifier was fine-tuned and evaluated on a balanced, held-out subset of the human-annotated TREMO corpus. Each corpus was characterized using lexical diversity and self-similarity metrics and compared against TREMO on inter-emotion vocabulary overlap.Grok 4.3 produced the most diverse and least repetitive sentences, while TREMO retained the highest lexical diversity without the highest inter-emotion overlap. On the TREMO test set, macro-F1 ranged from 0.749 for Mistral Large 3 to 0.813 for Claude Opus 4.8. Classification performance did not track corpus diversity: Grok 4.3, the most diverse source, produced the sixth-best classifier, while DeepSeek 3.2, a repetitive source, produced the second-best. Every model over-predicted disgust, and most under-recalled sadness; statistical tests confirmed significant differences between most model pairs.These results indicate that diversity metrics are not a reliable guide for selecting a generator LLM. A small, human-labeled sample, validated against each candidate LLM before full-scale generation, offers a direct alternative.

---

## uid: `doi:10.2139/ssrn.6210099`

- title: Stochastic Parrots or Singing in Harmony? Testing Five Leading LLMs for their Ability to Replicate a Human Survey with Synthetic Data
- authors: Jason Miklian, Kristian Hoelscher, John Katsos
- affiliations: not stated
- posted: 2026-03-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6210099
- keyword hits: ai agent, chatgpt, claude, deepseek, gemini, generative ai, large language model, large language models, llm, llms

### abstract

How well can AI-derived synthetic research data replicate the responses of human participants? An emerging literature has begun to engage with this question, which carries deep implications for organizational research practice. This article presents a comparison between a humanrespondent survey of 420 Silicon Valley coders and developers and "synthetic" survey data designed to simulate real organizational survey takers generated by five leading Generative AI Large Language Models (LLMs): ChatGPT Thinking 5 Pro, Claude Sonnet 4.5 Pro plus Claude Code / CoWork 1.123, Gemini Advanced 2.5 Pro, Incredible 1.0, and DeepSeek 3.2. Our findings reveal that while AI agents produced technically plausible results that lean more towards replicability and harmonization than typically assumed, none of the LLMs were able to capture the counterintuitive insights that made the human survey valuable. Moreover, deviations grouped together for all models, leaving the real data as the outlier. Our key methodological finding is that while leading LLMs are increasingly being used to scale, replicate and replace human survey responses in organizational research, these advances only illustrate an increased capacity to parrot conventional wisdom in harmony with each other rather than revealing novel findings. If synthetic respondents are used in future research, we need more replicable validation protocols and reporting standards for when and where synthetic survey data can be used responsibly in organizational research, a gap that this paper helps fill. Our results suggest that synthetic survey responses cannot meaningfully model real human social beliefs within organizations, particularly in contexts lacking previously documented evidence. We conclude that synthetic survey-based research should be cast not as a substitute for rigorous survey methods, but as an increasingly reliable pre-or post-fieldwork instrument for identifying societal assumptions, conventional wisdoms, and other expectations about research populations within organizations.

---

## uid: `doi:10.2139/ssrn.6644227`

- title: Stochastic Parrots or Singing in Harmony? Testing Five Leading LLMs for their Ability to Replicate a Human Survey with Synthetic Data
- authors: Jason Miklian, Kristian Hoelscher, John Katsos
- affiliations: not stated
- posted: 2026-04-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6644227
- keyword hits: ai agent, chatgpt, claude, deepseek, gemini, generative ai, large language model, large language models, llm, llms

### abstract

How well can AI-derived synthetic research data replicate the responses of human participants? This article presents a comparison between a human-respondent survey of 420 Silicon Valley coders and developers and "synthetic" survey data designed to simulate real organizational survey takers generated by five leading Generative AI Large Language Models (LLMs): ChatGPT Thinking 5 Pro, Claude Sonnet 4.5 Pro plus Claude Code / CoWork 1.123, Gemini Advanced 2.5 Pro, Incredible 1.0, and DeepSeek 3.2. An emerging literature has begun to engage with this question, which carries deep implications for innovation and science policy research practice. Our findings reveal that while AI agents produced technically plausible results that lean more towards replicability and harmonization than typically assumed, none of the LLMs were able to capture the counterintuitive insights of the human survey. Moreover, this pattern was repeated across different prompt formations, such that deviations in synthetic data grouped together for all models, leaving the real data as the apparent ‘outlier’. Our key methodological finding is that while leading LLMs are increasingly being used to scale, replicate and replace human survey responses in innovation and science policy research, these advances only illustrate an increased capacity to parrot conventional wisdom in harmony with each other rather than revealing novel findings. If synthetic respondents are used in future research, we need more replicable validation protocols and reporting standards for when and where synthetic survey data can be used responsibly in innovation and science policy research, a gap that this paper helps fill. Our results suggest that synthetic survey responses cannot meaningfully model real human social beliefs, particularly in contexts lacking previously documented evidence. We conclude that synthetic survey-based research should be cast not as a substitute for rigorous survey methods, but as an increasingly reliable data collection instrument for identifying societal assumptions, conventional wisdoms, and other expectations about research populations within organizations.

---

## uid: `doi:10.2139/ssrn.6541280`

- title: Using Large Language Models to Interpret Central Bank Speak
- authors: Andrea Stragiotti, Maeve Tsivanidis, Paul Henderson, Ronald Kahn, Simona Paravani-Mellinghoff
- affiliations: not stated
- posted: 2026-04-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6541280
- keyword hits: deepseek, gpt-4, gpt-5, large language model, large language models, llama, llm, llms

### abstract

Central bank communications move financial markets, but assessing policy stance at scale remains manual and time-intensive. Investors and policymakers need rapid, consistent judgments of whether minutes signal tighter (hawkish) or looser (dovish) policy, yet technical language and institutional nuance make automation difficult. We evaluate whether large language models (LLMs) can reliably classify monetarypolicy stance in central bank communications, benchmarking against expert labels from BlackRock macro specialists. We extend the existing literature by moving from single-institution studies to a cross-institution benchmark: we analyze 1,722 sentences from the Federal Reserve, European Central Bank, and Bank of England under a unified methodology, which allows us to distinguish model behavior that is consistent across institutions from patterns driven by institution-specific communication styles. Overall, LLM predictions closely track expert judgments, with disagreements largely confined to adjacent classes rather than polarity reversals. Models systematically under-use extreme categories relative to humans. Performance is highest for the Bank of England, consistent with experts assigning fewer extreme labels to BoE communications, which reduces the penalty from under-using extremes. As a robustness check, collapsing the five-class taxonomy to three classes (Dovish/Neutral/Hawkish) increases agreement while leaving the overall pattern of model performance similar; under this mapping, LLaMA-70B achieves 66% accuracy against expert labels. Under the five-class taxonomy, GPT-5 and LLaMA-70B perform best on the pooled sample across central banks, while another open-weight alternative, DeepSeek-R1, performs competitively with GPT-4o-supporting reproducible, scalable, near-real-time stance measurement without relying solely on closed models.

---

## uid: `doi:10.2139/ssrn.6608038`

- title: Open-Source Edge LLMs for Forecasting Stock Returns via News Headline Sentiment Analysis
- authors: Colin Arndt
- affiliations: not stated
- posted: 2026-05-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6608038
- keyword hits: deepseek, gpt-3, gpt-4, large language model, large language models, llama, llm, llms

### abstract

This research investigates the capability of open-source Large Language Models (LLMs) to forecast stock returns using news headline sentiment analysis, focusing on edge models deployable on consumer-grade hardware. The Llama3-8B family, including quantized versions and a fine-tuned FinGPT variant, was evaluated against benchmark models (FinBERT, GPT-3.5, GPT-4o mini, DeepSeek V3) and existing LLM solutions. Using a Kaggle dataset of US financial headlines from 2018–2019, edge LLMs were shown to outperform some larger, generalized models in classification and portfolio performance. Llama3-8B with INT8 quantization achieved 42.4% annualized returns and a 1.55 Sharpe ratio - competitive with existing FinLLMs and significantly outperforming the S&P 500 - while running within 10GB of RAM on an M2 MacBook Pro. These findings highlight the potential of resource-efficient open-source LLMs to democratize access to advanced trading strategies, while also demonstrating that the field requires more consistent study design, metric transparency, and peer review.

---
