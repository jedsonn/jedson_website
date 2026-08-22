# Classification batch 4 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-4.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7294110`

- title: Parameter-Efficient and Quantized LLM Fine-Tuning for Predictive Process Monitoring
- authors: Rafael Oyamada, Jari Peeperkorn, Jochen De Weerdt, Johannes De Smedt
- affiliations: not stated
- posted: 2026-08-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7294110
- keyword hits: fine-tuning, foundation model, large language model, large language models, llm, llms

### abstract

Large language models have shown strong results in predictive process monitoring, but their computational cost raises questions about their practical value compared with smaller sequence models trained from scratch. This paper studies whether parameter-efficient fine-tuning (PEFT) and quantization can provide a suitable balance between predictive performance and computational cost in multi-task predictive process monitoring. We evaluate recurrent networks, Transformers, PEFT-based LLMs, and a process-specific foundation model across six real-world event logs and three tasks: next-activity, next-resource, and remaining-time prediction. We assess predictive performance, hyperparameter sensitivity, peak GPU memory usage, and the total runtime of different model-selection procedures. The results show that PEFT-based LLMs are mainly sensitive to the learning rate, whereas LoRA rank, target modules, numerical precision, and most backbone choices have smaller effects. This supports replacing broad PEFT searches with a focused learning-rate search. Quantization reduces peak GPU memory usage by up to 70.9\% with limited predictive loss in most settings. A focused PEFT procedure can also be competitive in total runtime with broad hyperparameter searches over models trained from scratch. Finally, task-level results show that aggregate scores in multi-task may hide effects related to class imbalance and resource-label structure. Overall, quantized PEFT offers a practical and competitive approach for adapting pretrained LLMs to multi-task predictive process monitoring.

---

## uid: `doi:10.2139/ssrn.7273098`

- title: Breaking the Memory Wall: A Survey of Key-Value (KV) Cache Compression for Efficient Large Language Model (LLM) Inference
- authors: Manpreet Singh, Yash Jajoo, Rohith Reddy Bellibatlu
- affiliations: not stated
- posted: 2026-08-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7273098
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

The deployment of large language models (LLMs) at long context lengths is increasingly limited by memory rather than compute. During autoregressive decoding, the key-value (KV) cache stores the key and value activations of processed tokens, grows linearly with sequence length and batch size, and must often be streamed for each generated token. In long-context and high-throughput settings, this makes decoding memory-bandwidthbound and exposes the memory wall. This survey gives a unified, hardware-aware treatment of techniques that mitigate this bottleneck. We formalise it through the roofline model and a VRAM-footprint analysis separating compute-bound prefill from memorybound decoding, then organise the literature into four complementary layers: algorithmic compression (quantization, eviction and sparsification, and token, low-rank, or learned merging); architectural redesign (multi-query and grouped-query attention, low-rank latent attention, and recurrent or hybrid state-space models); system-level management (paged memory, prefix sharing, cross-request transport, and tiered offloading); and hardware acceleration (decoding kernels, fusion, and processing-in-memory). For each we give the governing mechanism, achievable memory reduction, and accuracy-latency trade-offs. Distinct from prior surveys, we (a) unify the four layers under a co-design and Pareto-frontier framework, (b) consolidate the evidence on multi-tenant KV cache security and side-channel leakage, and (c) analyse cache degradation in long-horizon agentic loops. To make this gap actionable, we propose Matched-Budget Evaluation (MBE), a lightweight reporting protocol and accompanying pilot harness for describing KV-cache results at fixed memory budgets. We present MBE as a standardization proposal, not a fully validated benchmark. It targets researchers and engineers combining KV cache optimisations under deployment constraints.

---

## uid: `doi:10.2139/ssrn.7299978`

- title: How Far Can Training-Free Text-to-SQL Go? An Empirical Study on Corrected BIRD
- authors: Ruihan Cao, Yifang Luo, Fan Zhang
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7299978
- keyword hits: fine-tuning, large language model, large language models, llm, llms, qwen

### abstract

Text-to-SQL remains a demanding benchmark for large language models (LLMs), requiring joint understanding of natural language, relational schemas, and SQL semantics. State-of-the-art BIRD systems typically rely on closed-source frontier models, large-scale fine-tuning, or multi-agent pipelines. We ask how far a simple, training-free baseline can go: a mid-sized open-weight model (Qwen3-14B, 4-bit quantized) wrapped in five lightweight inference-time stages: (i) a DDL-based schema representation with adaptive example budgeting, (ii) a structured prompt with error-analysis-derived instructions, (iii) N-best sampling with result-based voting, (iv) post-generation fuzzy matching, and (v) execution-driven self-correction. Evaluating on the corrected BIRD subset of Jin et al. (2026), we report three findings. First, this baseline reaches 80.4 ± 1.1% (five seeds) on the corrected 100-set, comparable to the two strongest agents re-evaluated there, CHESS and GenaSQL (both 81%, on proprietary frontier backbones). Second, five-seed ablations show that self-correction and fuzzy matching compose super-additively: worth +0.8 and +1.4 pp individually, their joint removal costs 3.6 pp and nearly quadruples the cross-seed standard deviation (σ: 1.14 → 4.38). Third, our strongest LoRA fine-tuning baseline (Qwen2.5-Coder-14B) does not outperform the training-free pipeline (60.82% vs. 60.95% on full BIRD dev), though differing base models make this a best-effort rather than controlled comparison. A strict held-out evaluation on the 1,394-example BIRD-dev complement (61.69%) rules out prompt overfitting, and cross-model transfer lifts a frontier-tier checkpoint from 71% to 81% (fuzzy matching disabled).

---

## uid: `arxiv:2608.17220v1`

- title: PACE: Policy-Attested Contract Execution for Safe AI Agents in Decentralized Finance
- authors: Rabimba Karanjai, Yang Lu, Richard Williamson, Hemanth Hm, Prakhar Mehrotra, Lei Xu, Weidong, Shi
- affiliations: not stated
- posted: 2026-08-18
- source: arXiv
- link: https://arxiv.org/abs/2608.17220v1
- keyword hits: ai agent, large language model, large language models, llm, llms

### abstract

Autonomous AI agents are emerging as interfaces for decentralized finance (DeFi) actions such as swaps, lending operations, and yield management. Because these agents rely on large language models (LLMs) to plan transactions, they inherit the LLM's susceptibility to prompt injection and lack of mechanisms to bind a verifier's approval to the exact transaction ultimately submitted on-chain. We present PACE (Policy-Attested Contract Execution), a transaction-level authorization framework that interposes between an LLM-based agent and on-chain execution. PACE introduces typed transaction intents, a deterministic policy verifier, and signed Policy Decision Records (PDRs) that cryptographically bind the approved intent, policy, and simulation report to the exact execution bytes, with replay and expiration protection. A Solidity smart account enforces PDR signatures on-chain with a measured overhead of 29,826-31,822 gas. We evaluate PACE against six baselines on 40 tasks spanning four attack categories plus benign utility (2,800 trials, 10 seeds). In our deterministic sandbox, PACE achieves a 0.00 unsafe execution rate and 0.00 false-positive rate on benign tasks, compared to 0.80 for the unguarded baseline. Ablation studies identify permissive policy settings (+57.5 pp) and the touched-contract allowlist (+12.5 pp) as the dominant safety components. To test whether the same deterministic floor holds for real model outputs, the artifact additionally provides a three-model live-LLM evaluation over the full task suite with repeated runs. A mainnet-fork harness is included for archive-RPC deployments, but fork results are reported only when the corresponding artifacts are generated. These auxiliary studies are separate from, and never substitute for, the deterministic benchmark. We frame our claims as logic-level safety within a reproducible benchmark rather than deployment-ready DeFi security.

---

## uid: `doi:10.2139/ssrn.7299799`

- title: A Taxonomy of Large Language Model Hallucination Detection Methods: Approaches, Evaluation Strategies, Challenges, and Open Research Problems
- authors: Aritrik Ghosh
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7299799
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Large language models (LLMs) routinely produce fluent text that is factually incorrect, internally inconsistent, or unsupported by any verifiable source, a phenomenon widely termed hallucination. As LLMs are deployed in information-seeking, retrieval-augmented, and decision-support settings, the ability to detect hallucinated content after or during generation has become a central concern for trustworthy AI. This paper presents a structured survey and taxonomy of LLM hallucination detection methods, built around a multidimensional comparison framework – detection signal, model-access requirements, external-knowledge dependence, detection granularity, computational cost, and structural failure modes – applied consistently across the literature rather than a formal, PRISMA-style systematic review. Rather than proposing or validating a new detector, the paper’s contribution is organizational and analytical: it synthesizes a substantial body of peer-reviewed and preprint literature into a structured taxonomy spanning intrinsic (uncertainty- and representation-based), sampling-based, semantic-consistency-based, knowledge-based, retrieval-based, reference-based, LLM-as-a-judge and verifier-based, multi-agent, and hybrid detection families. For each family, the survey identifies the underlying detection signal, the assumption that links the signal to hallucination, the method’s dependence on model access and external knowledge, and its principal failure modes. The survey further catalogues commonly used benchmarks and datasets, reviews evaluation metrics appropriate for imbalanced detection tasks, and distinguishes hallucination-detection evaluation from hallucination-generation evaluation. A comparative synthesis across method families is used to surface recurring limitations, including inconsistent operational definitions of hallucination, reliance on English-centric and short-form benchmarks, weak treatment of long-context and reasoning-induced errors, and the circularity risk of using one LLM to judge another. Building on this synthesis, the paper proposes a research agenda organized into short-, medium-, and long-term problems, covering domain-general and multilingual detection, low-cost real-time detection, detection for reasoning and multimodal models, and calibrated confidence estimation. The survey is intended as a reference point for researchers in natural language processing, retrieval-augmented generation, and AI safety who need a structured map of an otherwise fast-moving and fragmented literature.

---

## uid: `arxiv:2608.19025v1`

- title: Self-prompting and cross-model consensus enable reproducible data extraction from scientific literature with large language models
- authors: Valentin Romanov, Monique Bax, Steven Niederer
- affiliations: not stated
- posted: 2026-08-19
- source: arXiv
- link: https://arxiv.org/abs/2608.19025v1
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

Accurately extracting nuanced, contextualized data from research articles is laborious and time intensive. Here, we investigate the performance of frontier, browser-based large language models (LLMs) to extract highly contextualized information. We demonstrate four escalating workflows, 1) given an expert curated prompt and research articles, most frontier LLMs perform well at data extraction, however can struggle with interpreting scientific context and nuance, 2) given simple instructions, LLMs can author their own prompts which were almost as eNective as expert-written prompts, 3) autonomous discovery of research literature was diNicult, agents either missed or hallucinated references, and 4) LLMs can create new datasets from published guidelines that closely match human-expert judges, but still require a human-in-the-loop. Together, these findings define an auditable division of labour in which experts specify the evidence standard, models cross-check repeated extractions and researchers resolve disputed cases, providing a practical route to scaling scientific data curation without relinquishing expert oversight.

---

## uid: `arxiv:2608.19526v1`

- title: Automated Summarization of Financial News Using Large Language Models and Retrieval-Augmented Generation: An Early Empirical Study (Fall 2023)
- authors: Pranav Chandaliya
- affiliations: not stated
- posted: 2026-08-20
- source: arXiv
- link: https://arxiv.org/abs/2608.19526v1
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Stock market analysts and investors face a daily challenge: too much financial news, too little time. Manually reading and synthesizing hundreds of company-specific articles is impractical, yet missing key information can directly affect investment decisions. This project, conducted at George Washington University in Fall 2023, explores whether Large Language Models can automate this process reliably. We built a pipeline that pulls news articles from the News API, company background from Wikipedia, and stock price data from Yahoo Finance for ten major companies (AAPL, MSFT, GOOGL, AMZN, META, TSLA, JPM, NVDA, WMT, DIS). Because LLMs cannot directly process numerical tables, we developed a simple but effective template that converts stock data into natural language narratives. We then tested two summarization approaches (Summarize Chains and Retrieval-Augmented Generation with FAISS) across three open-source models (Falcon-7B-Instruct, DistilBART-CNN-12-6, BART-Large-XSum) for news, and GPT (text-davinci-003) for stock summaries. Falcon-7B with Summarize Chains gave the best results, covering all news events accurately and coherently. RAG, while promising in theory, caused severe repetition in Falcon and hallucinated facts in BART-Large when k was large. Both LLM-based approaches outperformed a simple Lead-3 baseline on ROUGE-1. We also built a Streamlit dashboard for interactive stock visualization. The work was done in Fall 2023, before RAG-based financial tools became widespread, and the failure modes we document, particularly hallucination under RAG in smaller models, remain relevant today.

---

## uid: `doi:10.2139/ssrn.7304462`

- title: Same Patient, Different Words, Different Diagnosis? Evaluating Semantic Stability inClinical LLMs
- authors: mahdi alkaeed, Adnan Qayyum, Nabeel Abo Kashreef, Muhammad Bilal, Junaid Qadir
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7304462
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Large Language Models (LLMs) are increasingly used in clinical applications; however, their behavior remains highly sensitive to subtle linguistic variations, such as rephrasing or syntactic variation. This sensitivity poses risks in safety-critical healthcare settings, where semantically equivalent inputs should produce consistent predictions. However, a key challenge is to ensure that prompt variations truly preserve clinical meaning, as embedding-based similarity metrics often fail to capture distinctions involving negation, temporality, or severity. To address this limitation, we propose a semantic verification framework based on Natural Language Inference (NLI) to filter meaning-preserving prompt variations, which are further refined using an LLM-as-a-judge andaudited by a clinical expert. In addition, we introduce three metrics to quantify model sensitivity: Meaning-Preserving Variation Sensitivity (MVS), confidence variation (ΔC), andWorst-Case Instability (WCI).We evaluate 16 open-source general-purpose (GP) and medical LLMs within the same model families and parameter scales, using reformulated prompts derived from the DiagnosisQA and MedQA datasets. Our results demonstrate that robustness differences between domain-specific (DS) models are mixed and highly model-dependent, i.e., domain specialization does not consistently improve or reduce robustness to meaning-preserving prompt reformulations. Several DS models rank among the most robust (when compared with GP counterparts), and strong GP baselines remain competitive as well. We also find that confidence variation is only weakly associated with prediction instability, while overall confidence is only weakly aligned with model accuracy; many models remain overconfident despite reduced robustness or relatively low performance. This suggests that medical fine-tuning alone does not reliably guarantee stable behavior undernatural prompt variations, thereby highlighting the need for explicit robustness evaluation prior to clinical deployment.

---
