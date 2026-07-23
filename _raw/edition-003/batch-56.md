# Classification batch 56 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-56.answer.json` as a JSON array.

---

## uid: `arxiv:2607.05985v1`

- title: Auto-DSM Under the Lens: A Black-Box Evaluation Framework for LLM-Based DSM Generation
- authors: Niels Potters, Theo Hofman
- affiliations: not stated
- posted: 2026-07-07
- source: arXiv
- link: https://arxiv.org/abs/2607.05985v1
- keyword hits: large language model, large language models, llm, llms

### abstract

This paper presents a black-box evaluation framework to systematically assess the ability of Large Language Models (LLMs) to generate Design Structure Matrices (DSMs) from structured technical documentation. Motivated by the closed-source nature of current Auto-DSM pipelines, the framework introduces a reproducible methodology that benchmarks generated DSMs (GEN-DSMs) against manually validated ground-truth matrices (GT-DSMs). The evaluation integrates both single-run and multi-run perspectives, combining structural metrics (Completeness, Correctness, Coupling Density), classification metrics (Selective Accuracy, Abstention Coverage), and stability measures (Entropy, Fleiss' $κ$). To synthesize these aspects, a Composite Quality Score (Q) is proposed. Controlled experiments are conducted on two datasets: a fictive abstract system and a real-world refrigerator decomposition, covering variations in phrasing, parameter-dataset alignment, and system complexity. Results show that LLMs can produce structurally plausible DSMs and achieve high reproducibility under well-structured inputs, but remain sensitive to ambiguity, inconsistent dependency definitions, and prompt formulation. The findings highlight systematic sources of hallucination and abstention failure, demonstrating both the potential and current limitations of LLM-driven DSM automation. The proposed framework provides a transparent benchmark for auditing Auto-DSM pipelines and establishes foundations for integrating LLM-based decomposition methods into model-based systems engineering (MBSE) workflows.

---

## uid: `doi:10.2139/ssrn.7053118`

- title: LLM Generated Regression Results vs. Specialized Econometric Software (STATA)
- authors: Mohd Nahar Mohd Arshad
- affiliations: not stated
- posted: 2026-07-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7053118
- keyword hits: large language model, large language models, llm, llms

### abstract

Large Language Models (LLMs) offer unprecedented assistance in economic research, yet researchers often mistakenly trust these tools to perform native statistical calculations on raw data. This paper exposes the mathematical limitations of LLMs and proposes a structured workflow for safely integrating artificial intelligence into econometric analysis. The proposed three-phase strategy enables researchers to use LLMs for conceptualization and code generation while ensuring that all final computations are executed in dedicated econometric software such as Stata. Through a detailed case study involving household income transfer data and quantile regression, this paper demonstrates that LLM-generated statistical outputs can produce fabricated coefficients that contradict empirical findings derived from authentic computation. The results confirm that while LLMs serve as effective cognitive assistants for structuring research designs and generating preliminary code, they cannot substitute for the deterministic mathematical operations required in rigorous econometric analysis. This paper contributes to the growing literature on responsible AI integration in the social sciences by offering a practical, replicable methodology that preserves scientific validity while improving the productivity gains when using AI tools.

---

## uid: `doi:10.2139/ssrn.7053778`

- title: Generative-AI Powered Inference
- authors: Junting Duan, Markus Pelger
- affiliations: not stated
- posted: 2026-07-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7053778
- keyword hits: large language model, large language models, llm, llms

### abstract

Empirical researchers increasingly use large language models (LLMs) to extract structured features, such as sentiment scores, classifications, and expectations, from unstructured data and treat these generated features as observed covariates in downstream estimation. This practice can invalidate inference when systematic, input-dependent errors in generated features, such as hallucination and look-ahead bias, distort the downstream moment conditions. Even after these moment-level distortions are corrected, generated features remain noisy proxies for the latent truth, with error profiles that differ across models and prompts. We introduce Generative-AI Powered Inference (Gen-PI), a method-of-moments framework that delivers valid and efficient inference by combining three components: (i) a moment-specific bias correction based on a small human-labeled calibration set; (ii) adaptive weights that optimally combine multiple modelprompt pairs, downweighting unreliable generators and exploiting complementary information across generated features ; and (iii) an optimal calibration-set design that concentrates costly human labels on the observations where the generated features are least reliable. We establish consistency and asymptotic normality of the Gen-PI estimator, allowing for non-random and data-adaptive labeling designs, cross-fitted LLM-pipeline tuning, and overidentified GMM. Simulations confirm that Gen-PI delivers substantial gains over naive LLM regressions and over debiasing without optimal weighting or labeling design. In an empirical study of news-based sentiment and stock returns, Gen-PI produces stable conclusions in a setting where naive analyses vary substantially across LLM and prompt choices, and its confidence interval is roughly half the length of the interval that uses the human-labeled data alone.

---

## uid: `doi:10.2139/ssrn.7082874`

- title: GraphShield: A Graph-Structured Defense Framework for Prompt Injection in RAG and Multi-Agent LLM Systems
- authors: Shreya Singh
- affiliations: not stated
- posted: 2026-07-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7082874
- keyword hits: llama, llm, llms, qwen

### abstract

GraphShield is a graph-structured defense framework for LLMs that represents system prompts, retrieved knowledge, agents, and parsed instructions as directed Trust-Knowledge Graph (TKG). Security is formalized as reachability from an instruction node to policy node in a trust-threshold subgraph, and operationally instantiated through typed instruction-violation signatures that assign zero trust to pattern-matched instructions, together with provenance filtering of retrieved and agent-supplied content; instructions that clear these checks receive a default bridge trust, so the trust threshold functions as a structural reachability gate rather than a graded per-instruction score. Evaluated on four benchmarks (PromptBench, INJECAGENT, RAGInject-Bench, MultiAgentEscape-Bench) against six defense baselines and a No-Defense reference across three victim models (Qwen2-0.5B, Gemma3-4B, Llama3.2), the full GraphShield configuration achieves block-level F1=0.791; the block-level F1 is invariant across all three victim models by construction (§5.0.1). We select the full configuration for threat-surface coverage and structural completeness against indirect and context-borne attacks rather than to maximize aggregate F1. We frame GraphShield's contribution as a unified, auditable graph representation for coordinating heterogeneous security controls across RAG and multi-agent systems.

---

## uid: `doi:10.2139/ssrn.7062098`

- title: From K-means to LLM-Augmented Pipelines: A Critical Survey and Taxonomy for Biomedical Big Data
- authors: Absalom El-Shamir Ezugwu
- affiliations: not stated
- posted: 2026-07-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7062098
- keyword hits: large language model, large language models, llm, llms

### abstract

The exponential growth of biomedical data arising from medical images, genomics, bioinformatics, and electronic health records has intensified the urgent need for more scalable, interpretable, and computationally efficient unsupervised learning approaches. Among these, the K-means clustering technique remains one of the most widely adopted clustering methods because of its conceptual, design and implementation simplicity, adaptability, and effectiveness across diverse biomedical data modalities. This paper presents a systematic and critical survey of Kmeans clustering methodologies applied to biomedical data science, with specific emphasis on scalability, robustness, and integration into modern big data ecosystems. Similarly, this study categorises and analyses classical, enhanced, and hybrid K-means variants, including initialisation strategies, distance metrics, constraint-based formulations, and distributed implementations for high-dimensional, large-scale biomedical datasets. Moreover, the survey also examines recent trends in augmented K-means workflows with large language models (LLMs), highlighting their emerging roles in data preprocessing, feature engineering, semantic annotation, and a human-in-the-loop analytical pipeline rather than in direct numerical optimisation. Lastly, open challenges related to data heterogeneity, interpretability, and scalability, as well as benchmarking practices, are discussed.

---

## uid: `doi:10.2139/ssrn.6980679`

- title: Spectral Shape Residual: A Lightweight Spec-Tral Diagnostic For Attention Weight Matrices
- authors: Fei-Yun Wang
- affiliations: not stated
- posted: 2026-07-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6980679
- keyword hits: deepseek, llama, llm, llms, qwen

### abstract

We introduce the Spectral Shape Residual (SSR), a lightweight metric computed directly from the query and key weight matrices of attention layers-no forward pass, no training data needed. SSR measures how similar the singular value distributions of W Q and W K are: when they match perfectly, SSR is zero. We study SSR across four settings organized as a 2×2 analytical framework (toy vs. production LLM; static snapshot vs. training dynamics)-a design that systematically covers the conditions under which spectral weight-space signals can arise. In toy transformers trained on modular arithmetic, SSR drops to near-machine precision after grokking, and this drop happens 200-1,900 steps before the model generalizes-making SSR an early warning signal. In production LLMs (LLaMA-3-8B (hereafter LLaMA), Gemma-4-31B-IT (hereafter Gemma)), SSR decreases systematically with layer depth, and RL-distilled models (DeepSeek-R1-Distill-Qwen-14B (hereafter R1)) show lower SSR than their base model (Qwen2.5-14B-Instruct (hereafter Qwen)) in 45 out of 48 layers. In OLMoE-1B-7B pretraining, 18.8% of attention heads show persistent monotonic decline in SSR before grokking completes, concentrated in deep layers (L10-L13); the median SSR of these heads falls 40% below its peak 582B tokens before grokking completes. SSR requires only one SVD per attention head and no evaluation data, making it deployable as a zero-overhead structural health monitor directly inside training pipelines. For both pre-training (does the model grok?) and post-training (does RL alignment shift spectral structure?), SSR provides a continuous signal without running a single forward pass.

---

## uid: `doi:10.2139/ssrn.6955198`

- title: Classification Drift in AI-Augmented Data Analytics: A New Attack Surface for PII and PCI Exposure
- authors: Venkata Manikanta Sangaraju
- affiliations: not stated
- posted: 2026-07-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6955198
- keyword hits: large language model, large language models, llm, llms

### abstract

The rapid integration of AI-assisted analytics into modern data engineering and business intelligence systems has introduced new and underexplored security risks related to the exposure of sensitive Personally Identifiable Information (PII) and Payment Card Industry (PCI) data. This paper introduces the concept of classification drift, defined as the temporal misalignment between a dataset's true sensitivity classification and the enforcement of its associated security policies. We argue that in highly automated environments-where large language models (LLMs) generate queries, traverse evolving schemas, and interface with distributed data systems-classification drift emerges as a critical attack surface that amplifies the risk of unauthorized data exposure. We further categorize drift into policy, pipeline, schema, and AI-induced semantic variations, and demonstrate how these inconsistencies propagate through data workflows modeled as Directed Acyclic Graphs (DAGs). To formally characterize drift dynamics and exposure risk, we propose a hybrid analytical framework combining DAG-based lineage modeling with Continuous-Time Markov Chains (CTMCs). A simulated enterprise analytics environment is used to evaluate drift propagation and exposure likelihood under AI-driven query generation scenarios, highlighting significantly elevated risks compared to static access control systems. Finally, we propose a drift-resilient governance architecture incorporating continuous monitoring, automated reclassification, and policy-as-code enforcement to mitigate emerging vulnerabilities in AI-augmented data ecosystems.

---

## uid: `arxiv:2607.08961v1`

- title: NL-PAC: Specification Ambiguity and Certified Minimax Risk Floors in LLM-Mediated Supervision
- authors: Berkay Anahtarci
- affiliations: not stated
- posted: 2026-07-09
- source: arXiv
- link: https://arxiv.org/abs/2607.08961v1
- keyword hits: large language model, large language models, llm, qwen

### abstract

Large language models increasingly provide labels, evaluations, and feedback for tasks specified in natural language. When a specification admits multiple readings but the supervision channel does not reveal which is operative, additional labels reduce sampling error without resolving the resulting identification problem. We introduce Natural Language PAC (NL-PAC), a framework that uses a fixed model's thresholded decoding law to define admissible labels and candidate targets. The probability that multiple labels are admissible equals the diameter of the pointwise-admissible target class, and under target-blind supervision every learner incurs worst-case risk of at least half this diameter, at every sample size; the exact randomized minimax risk over this class is attained by a data-independent strategy. Finite-sample confidence bounds make these quantities certifiable from held-out unlabeled inputs. In a frozen Qwen~2.5--3B audit, one prespecified prompt yields a positive model-relative certificate, whereas a paraphrase and exact-rule controls yield zero. A held-out bridge audit finds that supplied candidate reading clauses fail the admissibility condition needed to transfer the certificate to coherent readings. The guarantee is specific to the audited model, prompt, threshold, and input distribution; extending it to human interpretations requires external validation.

---
