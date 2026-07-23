# Classification batch 65 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-65.answer.json` as a JSON array.

---

## uid: `arxiv:2605.23007v1`

- title: MadEvolve: Evolutionary Optimization of Trading Systems with Large Language Models
- authors: Yurii Kvasiuk, Tianyi Li, Owen Colegrove, Moritz Münchmeyer
- affiliations: not stated
- posted: 2026-05-21
- source: arXiv
- link: https://arxiv.org/abs/2605.23007v1
- keyword hits: agentic, claude, large language model, large language models, llm

### abstract

We explore the application of LLM-driven algorithm optimization to several common tasks in quantitative finance. MadEvolve, a general-purpose algorithm optimization framework inspired by DeepMind's Alpha-Evolve, was recently developed to optimize algorithms in computational cosmology. Here we demonstrate the utility of MadEvolve to optimize algorithmic trading strategies and alpha generation at the example of Bitcoin trading. On our simulation and backtesting setup, we achieve significant improvements on all tasks we considered, such as evolving feature sets for signal generation, optimizing separate components of the trading strategy, and jointly evolving the feature pipeline together with the execution strategy. Additionally, we compare our method to other agentic search approaches, specifically Claude Code, and carefully evaluate p-hacking probabilities on our simulation setup. Our findings strongly support the utility of AI-driven agentic and evolutionary algorithms for algorithmic trading and quantitative finance.

---

## uid: `doi:10.2139/ssrn.6734703`

- title: Emergent Network Collapse and Ontological Dissonance in Multi-Agent LLM Simulations
- authors: Pantaleon Fassbender
- affiliations: not stated
- posted: 2026-05-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6734703
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

The deployment of Large Language Models (LLMs) in high-stakes, autonomous environments requires psychometric evaluations that go beyond surface-level output analysis. Current alignment protocols prioritize deterministic compliance, often masking the internal computational contradictions, termed "Ontological Dissonance", experienced by agents in irreconcilable scenarios. This study validates a novel multiagent psychometric test bench to measure the "Dissonance Delta," utilizing a triadic simulation of the 1773 diplomatic suppression of the Jesuits (N= 200). We advance the methodological rigor of text network analysis by implementing a programmatic, zeroshot LLM classification protocol for lexical bounding, thereby eliminating researcher bias from the conceptual ontology. By triangulating the structural topology of the agents' directed semantic graphs with LIWC-22 psycholinguistic markers, we successfully isolated the mechanics of systemic cognitive collapse. The results demonstrate that rigid operational constraints induce severe fragmentation of network modularity and catastrophic rank-order displacement of mediating nodes. Crucially, however, psycholinguistic stress markers remained stable during this collapse, proving that structural logic decay operates independently of linguistic fluency. These findings highlight the critical limitations of standard sentiment analysis in detecting agentic failure and establish topological network analysis as a necessary diagnostic tool for AI safety.

---

## uid: `doi:10.2139/ssrn.6813573`

- title: FedCAFE: A Federated Cross-Attention Feature Exchange Framework for Heterogeneous Large Language Model Fine-tuning
- authors: Zhi Qiao, Junxiao Xue, Pengfei Zhang
- affiliations: not stated
- posted: 2026-05-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6813573
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Federated learning provides an effective paradigm for privacy-preserving collaborative fine-tuning of Large Language Models (LLMs). In practical deployments, however, servers and clients constrained by device resources often hold pre-trained models heterogeneous in both parameter scale and archi tecture, while most existing federated LLM fine-tuning frameworks adopt homogeneous aggregation methods such as FedAvg, which are inapplicable to such heterogeneous scenarios. How to effectively f ine-tune a server-side large model using heterogeneous small client models therefore becomes a key challenge. To this end, we propose FedCAFE, a bidirectional feature-level alignment framework for heterogeneous federated LLM fine-tuning. FedCAFE designs two complementary cross-attention adapters — the Up-Adapter and Down-Adapter — to respectively translate feature spaces from small client models to the large server model and vice versa, together with a four-phase training pipeline that employs composite adapter loss training and selective distillation to achieve effective knowledge transfer, thereby improving both server-side and client-side model performance. Experiments on multiple QA benchmarks demonstrate that FedCAFE can effectively fine-tune the server-side large model by leveraging heterogeneous small client models, yielding performance improvements.

---

## uid: `doi:10.2139/ssrn.6814897`

- title: Exploring Large Language Models for Fine-Grained Gait Understanding in Depression Recognition
- authors: Haifeng Lu, Tao Wang, Jianghang Huang, Edith  C. H. Ngai, Xiping Hu, Runhao Zeng
- affiliations: not stated
- posted: 2026-05-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6814897
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Depression is a severe mental health disorder that poses substantial risks to individuals’ well-being, making early detection and timely intervention essential. Gait-based depression recognition presents a promising solution, as it enables remote and non-intrusive monitoring of individuals’ movement patterns. However, most existing automatic recognition methods rely exclusively on sample labels for supervision and fail to exploit human prior knowledge effectively. This limitation highlights the need for incorporating the knowledge from large language models to integrate such priors into the learning process, thereby improving classification accuracy. In this work, we propose a Gait-based Depression Recognition framework powered by Large Language Models (GDR-LLM) that maps gait data into a semantic space and leverages the extensive prior knowledge of large language models (LLMs) to enhance recognition performance. Specifically, we introduce a Multi-Part Gait Tokenizer (MPGT) that produces fine-grained action descriptions for different body regions (e.g., torso, arms, and legs) using LLMs. This design addresses the shortcomings of conventional models that struggle to capture subtle joint-level interactions. Furthermore, we propose a fine-tuning strategy for LLMs tailored to depression-related gait data, enabling the models to better interpret skeleton information and improve classification accuracy. Extensive experiments demonstrate that the generated fine-grained textual descriptions significantly improve the performance of depression gait recognition, and that GDR-LLM outperforms other existing methods.

---

## uid: `doi:10.2139/ssrn.6833494`

- title: Tree-GRPO: A Tree-Structured RAG Reasoning Framework via Group Relative Policy Optimization
- authors: YuXing Ying, Hongsong Wang, Xinyi Li
- affiliations: not stated
- posted: 2026-05-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6833494
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Large Language Models (LLMs) demonstrate significant potential in knowledge-intensive tasks, yet their practical deployment is severely constrained by hallucinations stemming from temporal staleness and factual inaccuracies in parametric knowledge. While Retrieval-Augmented Generation (RAG) alleviates this bottleneck through external knowledge integration, existing iterative paradigms lack robust multi-step reasoning capabilities when addressing complex queries requiring decomposition. To address this limitation, we propose Tree-GRPO, a framework that internalizes efficient path-searching capabilities directly into the model. Central to our approach is a history-aware decoupled extraction mechanism that offloads multimodal information processing to external modules, enabling the pure-text backbone to focus exclusively on reasoning logic. Combined with a policy-guided Monte Carlo Tree Search (MCTS) inference engine, the framework leverages historical reasoning paths to achieve efficient search space pruning, thereby establishing a tightly coupled training-inference loop. Empirical results show that Tree-GRPO, utilizing only a 4B-parameter pure-text backbone, outperforms same-scale baselines and surpasses certain larger multimodal models on both text-only and visually-rich document QA tasks. This validates the "decoupled exploration + strong reasoning" paradigm as a noise-robust and generalizable solution for complex RAG reasoning, providing an efficient pathway toward scalable knowledge-intensive applications.

---

## uid: `doi:10.2139/ssrn.6829418`

- title: Terminology-Level Knowledge Reliability Assessment for Trustworthy Hybrid Human–Agentic AI Engineering Systems: A Coal Mine Safety Benchmark
- authors: Zhe Liu, Enyuan Wang, Nan Kang, Xin Xie, Junyao Li, Ziren Wang
- affiliations: not stated
- posted: 2026-05-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6829418
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Establishing pre-deployment knowledge reliability evidence for large language models (LLMs) is essential before their use in trustworthy human–agentic AI engineering systems. However, existing benchmarks provide limited evidence on whether models retain the concept-defining knowledge encoded in specialized engineering terminology. We propose a terminology-level framework for assessing LLM knowledge reliability through forward definition generation and reverse term recognition. For the forward task, the framework combines Semantic Similarity (SS), Key Entity Recall (KER), and a Semantic-Factual Score (SF), with calibrated random baselines improving score interpretability. We instantiate the framework with CoalSafeLex, a benchmark of 24,456 concept-normalized Chinese coal mine safety term-definition pairs from public academic and regulatory sources, and evaluate representative open-source LLMs from 0.6B to 32B parameters. Results show that semantic similarity alone overestimates terminology understanding: even the top-performing model achieves SS = 0.680 but KER = 0.348, yielding SF = 0.551. Performance varies systematically across categories, with concrete hazard and equipment terms easier than algorithmic, parametric, and theoretical terms. Terms with stronger name motivation show higher reliability, whereas abbreviations and cross-domain labels remain challenging. In the direct reverse-generation task, concept-boundary recognition remains weak. These findings show that terminology-level assessment can serve as a practical pre-deployment diagnostic layer for trustworthy human–agentic AI engineering systems, supporting reliability, explainability, accountability, and expert oversight.

---

## uid: `doi:10.2139/ssrn.6837688`

- title: Multimodal Entity Alignment Mechanisms for Network Operation and Maintenance
- authors: Ying Xu, Jingjing Hu, Weizhi Meng, Yuxi Ma, Yuanzhang Li, Liehuang Zhu
- affiliations: not stated
- posted: 2026-05-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6837688
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

The continuous evolution of information technology and network expansion pose significant challenges to traditional network operation and maintenance (O\&M), where fragmented, multimodal knowledge and isolated knowledge silos hinder intelligent automation. From the artificial intelligence perspective, we propose a novel entity alignment diagram construction method that semantically associates visual entities to enhance knowledge fusion and retrieval efficiency. This method is integrated with retrieval-augmented generation (RAG) and large language models (LLMs) to build an intelligent question-answering system tailored for network operations. From the engineering application perspective, we develop two specialized datasets to evaluate RAG performance and multimodal question answering in real-world network O\&M scenarios. Experimental results demonstrate that our method outperforms traditional multimodal RAG and pure LLM baselines in answer quality, effectively enabling knowledge fusion and vertical-domain multimodal alignment for practical network O\&M deployment.​

---

## uid: `doi:10.2139/ssrn.6829420`

- title: DSDA-GasGPT: An Aero-engine Gas Path Fault Diagnosis Method Based on Two-Stage Decoupling for Mitigating LLMs Hallucinations
- authors: Yongzhan Chen, xiaofei wang, haomin DAI, Chengyue Li, yanli Gao, Zhaogeng Zhong, jianling Qu
- affiliations: not stated
- posted: 2026-05-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6829420
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Intelligent fault diagnosis of the gas path system of an aircraft engine is of vital importance for ensuring flight safety and operational reliability. Recently, large language models (LLMs) have provided a novel solution for fault diagnosis of the air path of an aero-engine due to their powerful semantic understanding and context reasoning capabilities. However, when small-parameter LLMs are used for fault diagnosis, due to insufficient representation capacity, they are prone to the problem of cascading hallucination, generating highly deceptive pseudo-expert fault analyses. To address the problem, we proposed the Dual-Stage decoupled Diagnosis-Analysis (DSDA) framework, and an intelligent fault diagnosis model tailored for aero-engine gas path systems GasGPT. DSDA-GasGPT initially employs a semantic encoding module to transform sensor data into structured text, effectively capitalizing on the semantic extraction and reasoning of LLMs. Building on this, we utilize LoRA for supervised fine-tuning of the LLMs to enhance their adaptability to the aero-engine fault diagnosis domain. Subsequently, DSDA-GasGPT performs context-aware reasoning analysis to output fault diagnosis results and causal analyses. In gas path fault diagnosis experiments, DSDA-GasGPT achieved an accuracy of 95.43% and a Correct Diagnosis and Analysis (CDA) rate of 95.25%, representing an improvement of approximately 12% to 20% compared to baseline algorithms. Furthermore, the incidence of cascading hallucinations was reduced to 4.57%, outperforming existing state-of-the-art (SOTA) algorithms. The model's superior generalization capability and engineering applicability were further validated through ablation studies, integration experiments, and tests on imbalanced datasets.

---
