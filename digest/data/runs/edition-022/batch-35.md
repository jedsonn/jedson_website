# Classification batch 35 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-35.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7313419`

- title: The Risk of Ignoring Risk in Anti-Money Laundering Research: A Scientometric and AI-assisted Review
- authors: Andréa Alves Corrêa, Danielle Montenegro Salamone Nunes, Sérgio Ricardo Miranda Nazaré
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7313419
- keyword hits: generative ai

### abstract

Objective: This study examines whether international anti-money laundering research adequately reflects the centrality and geographic distribution of money laundering risk in financial institutions. Method: A scientometric review was conducted using the Theory of the Consolidated Meta-Analytic Approach, with data from Web of Science, Scopus, and Google Scholar. Bibliometric and network analyses were applied to 4,220 publications. The TEMAC-selected corpus was complemented by an AI-assisted thematic audit and researcher-led validation. Originality/Relevance: The study advances AML literature by treating money laundering risk not only as a regulatory requirement, but as an analytical category that should structure scientific research. It also proposes a hybrid review strategy combining scientometric rigor, generative AI auditing, and human validation. Results: The AI-assisted audit identified 48 academic records, of which 37 unique studies remained after validation and deduplication; 35 were not present in the original TEMAC corpus. The consolidated geographic analysis resulted in 184 country-publication allocations across 42 countries. The correlation between scientific production and Basel AML Index scores was weak, negative, and statistically non-significant, indicating that the mismatch is better understood as concentration and underrepresentation rather than as a linear relationship. Theoretical/Methodological Contributions: The article shows that AML risk remains conceptually fragmented in academic research and demonstrates how AI can expand the semantic perimeter of scientometric reviews when its outputs are treated as auditable hypotheses. Social/Managerial Contributions: The findings support regulators, financial institutions, compliance professionals, and researchers by highlighting the need for stronger empirical models of AML risk determinants.

---

## uid: `doi:10.2139/ssrn.7321289`

- title: DCAKD-LLM: A Temporal-Textual Dual-Branch Cross-Modal Alignment Anomaly Detection Framework Integrating Knowledge Distillation and Large Language Model
- authors: YUXUAN TANG, Dongheng Zeng, Lun Tang
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7321289
- keyword hits: large language model, llm

### abstract

The surge in Internet of Things (IoT) applications driven by 5G has brought severe security and reliability challenges, necessitating efficient anomaly detection. However, existing methods face issues such as insufficient multimodal fusion, difficulty in capturing multi-scale time dependencies, weak suppression of irrelevant context, and privacy leakage in centralized training. To address these, this paper proposes a temporal-textual dual-branch cross-modal alignment anomaly detection framework integrating knowledge distillation and large language model (DCAKD-LLM). The temporal branch employs a multi-hop GCN to capture inter-node relationships, multi-scale dilated convolutions (MSDC) for local multi-scale dependencies, and differential attention for long-term global dependencies, forming hierarchical temporal features. The text prompt branch provides prior knowledge for cross-modal alignment, guiding the temporal branch to focus on anomaly-related features. A cross-attention mechanism aligns the two branches, enabling dynamic focus on anomaly-related time windows. The LLM further enhances sequence feature representations, and an MLP reconstructs sequences with reconstruction error as the anomaly score. For privacy and edge deployment, a VAE-based privacy-preserving distillation scheme is introduced: the teacher model is trained on anonymized data, while a lightweight student model learns temporal representations through knowledge distillation. Simulation results show that DCAKD-LLM outperforms baselines in precision, recall, and F1 score.

---

## uid: `arxiv:2608.20304v1`

- title: Calibration-Induced Degeneracy in LLM Financial Forecasting: An Audit-Trailed Case Study on Next-Day Market Risk
- authors: Arin Mohanty
- affiliations: not stated
- posted: 2026-08-20
- source: arXiv
- link: https://arxiv.org/abs/2608.20304v1
- keyword hits: llm

### abstract

Costly LLM features matter only if calibration lets them affect the forecast. We document a failure of this link in a next-day risk study of two broad-market funds. Full-history scoring preceded the 2022 calibration. Calibration then set all four LLM weights to zero. The 856 later scores therefore could not affect the evaluation. We call this calibration-induced degeneracy. Allowing signed weights reactivated all four mappings. None improved forecasts after familywise correction. By contrast, a near-zero-cost headline count reduced SPY variance-forecast loss by 0.001720 (95 percent familywise interval: [0.000719, 0.002830]). The cheap baseline is therefore a critical diagnostic. We propose a calibration-viability checkpoint. Fit the mapping, perturb the feature over prespecified calibration values, and require a meaningful forecast response before acquiring holdout features. The check uses no holdout outcomes. Here, it would have stopped the paid full-history inference phase.

---

## uid: `arxiv:2608.20290v1`

- title: Phantom Gains: Auditing Self-Improvement Against a Measured Null
- authors: Cheng Xu, Nan Yan, Liming Chen, M-Tahar Kechadi
- affiliations: not stated
- posted: 2026-08-20
- source: arXiv
- link: https://arxiv.org/abs/2608.20290v1
- keyword hits: qwen

### abstract

Whether a language model has improved itself is increasingly judged not by mean accuracy but by which individual problems it gains and loses. Tracking these transitions means differencing two noisy estimates, leaving them vulnerable to measurement artifacts. Auditing three rounds of rank-$32$ LoRA self-training on Qwen3-8B against a frozen control pushed through the identical pipeline, we identify seven measurement failures, each of which inverts a reported finding when its control is absent. Several are standard practice. A ledger built on a single greedy decode manufactures capability changes on an untrained model, largely an artifact of inference batching; the expansion statistic separating acquisition from sharpening assigns that same model a rate of $0.280$. The natural threshold repair does not survive replication: estimated across the frozen comparisons such a design already contains, its null stays non-zero. We replace it with a per-problem exact test against a pooled baseline under false-discovery-rate control, which detects nothing on any held-out replicate and is unchanged under the multiple-testing rule, error rate and pool size. Applied to a ladder of arms matched in stream, volume and evaluation, the audit finds that external distillation improves problems the base model rarely reaches while three forms of self-training do not; a regression rejects this asymmetry as a by-product of distillation's larger overall gain ($p < 10^{-8}$). On the far smaller set of problems the base model never reaches, the evidence is inconclusive, while self-training corrupts problems solved at baseline at rates well above the measured floor. Transition-level auditing therefore requires a separately measured null for every statistic it reports: nulls that cost no new experiments, built from baseline replicates a multi-arm study already owns, though not from as few as most possess.

---

## uid: `arxiv:2608.20169v1`

- title: Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selection
- authors: Atsuyuki Miyai, Kiyoharu Aizawa, Toshihiko Yamasaki
- affiliations: not stated
- posted: 2026-08-20
- source: arXiv
- link: https://arxiv.org/abs/2608.20169v1
- keyword hits: llm

### abstract

We present a novel approach to efficient LLM agent harness optimization through adaptive validation task selection. Harness optimization iteratively rewrites the harness code based on validation performance, enabling substantial performance gains without updating the underlying model weights. Existing approaches, however, evaluate a fixed validation set in full at every iteration, incurring substantial evaluation costs even on tasks that become less discriminative as the harness evolves. We propose $\textbf{Task-CoEvolve}$, which co-evolves the validation tasks with the harness by addressing two challenges: selecting informative tasks and estimating full-set performance from partial evaluations. Task-CoEvolve builds on the observation that tasks on which candidate harnesses disagree are more informative for distinguishing among them than tasks that are consistently solved or failed. It uses variance-weighted sampling based on past outcomes to focus evaluation on tasks near the agent's capability frontier, with the sampling distribution adapting as the harness evolves. It then estimates full-set scores from the sampled tasks by accounting for their sampling probabilities, enabling consistent comparisons across iterations despite evaluating different subsets. Experiments on online text classification and Terminal-Bench 2.1 show that Task-CoEvolve consistently outperforms fixed-subset baselines and matches the final performance of full-set search while reducing the number of evaluations during optimization by 80%. Code will be released at https://github.com/Agent4Science-UTokyo/Task-CoEvolve.

---

## uid: `arxiv:2608.19889v1`

- title: Write Once, Run Everywhere: The Axon DSL for Shape-Safe and Framework-Agnostic LLM Architectures
- authors: Jacob Nielsen, Danial Namazifard, Lukas Galke Poech, Peter Schneider-Kamp
- affiliations: not stated
- posted: 2026-08-20
- source: arXiv
- link: https://arxiv.org/abs/2608.19889v1
- keyword hits: llm

### abstract

The entire ecosystem of open-source language models effectively relies on a single platform. What if this platform was forced to shut down tomorrow? Implementing and maintaining efficient model definitions and translating them between different training and inference regimes is a resource-heavy task that severely limits model efficiency and portability, hindering both scaling and deployment. Here, we present Axon, a strongly typed domain-specific language with Haskell-like syntax, that enables a write-once, run everywhere paradigm for LLM architectures. By basing collaboration on a language specification rather than a specific framework's vision, Axon fosters open cooperation and empowers researchers to implement highly specialized architectures without giving up optimization infrastructure or accepting deployment lock-in. Axon allows for concise, auditable specifications that can be automatically compiled to standalone implementations for leading frameworks: PyTorch, PyTorch with Triton, JAX, MLX and vLLM. In 467 inference benchmarking experiments on models ranging from 135M to 32B parameters, we demonstrate median speedups of 7% on PyTorch, 12% on PyTorch with Triton, 91% on JAX, and 107% on MLX, compared to the reference implementations from Transformers. When deployed as native vLLM architectures with PagedAttention and KV-cache, Axon models achieve a 58% median speedup over Transformers implementations.

---

## uid: `arxiv:2608.19802v1`

- title: Stopping and Routing LLM Judge Panels
- authors: Bin Zhu, Yi Xie, Yanghui Rao
- affiliations: not stated
- posted: 2026-08-20
- source: arXiv
- link: https://arxiv.org/abs/2608.19802v1
- keyword hits: llm

### abstract

LLM evaluation pipelines often have many candidate judges: general LLM-as-a-judge prompts, reward models, safety classifiers, confidence variants, and task-specific verifiers. The deployment question is not only which judge is best, but which judges should be called, on which examples, and when panel construction should stop. We formulate judge-panel design as a role-conditioned allocation problem. From a small labeled audit set, declared slices, and judge costs, the method estimates target-relative roles: copies add no conditional information, complements improve the global panel, and specialists help only on slices. These roles induce a policy: drop copies, add complements globally, route specialists conditionally, and stop when validation gain falls below a threshold. Across reasoning, code, safety, preference, reward-model, summarization, and math audits, the method is compared with single judges, flat panels, matched diversity heuristics, full-call stacking, reliability juries, and frugal cascades. The result is a regime map for judge calls: route specialists on deployable slices, stop in saturated verifier regimes, keep broad ensembles when their risk benefit is worth the cost, and ignore conditional copies. The output is a reusable, auditable call plan for the next evaluation batch.

---

## uid: `doi:10.2139/ssrn.7324332`

- title: Section-Aware Hybrid Summarization for Scientific Abstract Generation: Integrating LightGBM Extraction with Transformer-Based Generation
- authors: Pei-Ju Lee, Jia-Fu Hsiao
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7324332
- keyword hits: large language model, llama

### abstract

Generating structured abstracts for scientific articles remains challenging due to the length and complex organization of scholarly texts. This study proposes a hybrid extractive–abstractive framework for generating IMRD-structured summaries from biomedical research articles. The method first employs a Light Gradient Boosting Machine (LGBM) classifier with syntactic features and transformer-based sentence embeddings to identify salient sentences within each section of an article. The selected sentences are then used as input to a BioBART abstractive model to generate coherent section summaries. Experiments are conducted on research articles from the PubMed Open Access Subset, and several SBERT variants are evaluated for sentence representation. The extractive classifier achieves approximately 70% recall in identifying abstract-related sentences. When generating full abstracts, the proposed hybrid framework of LGBM+BioBART achieves the best performance out of all experimental settings, reaching Rouge-1 = 0.5642, outperforming standalone extractive and abstractive baselines, LEAD, as well as a lightweight large language model baseline (Llama3.2:3b). The results indicate that combining extractive filtering with domain-adapted abstractive generation effectively preserves key information while improving summary coherence, demonstrating the potential of hybrid summarization for large-scale scientific literature processing.

---
