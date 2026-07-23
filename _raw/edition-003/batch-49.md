# Classification batch 49 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-49.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6824318`

- title: Affective Trust in Indian LLM Users: An Exploratory Study Challenging Western Dependency Models
- authors: Bestin Samuel
- affiliations: not stated
- posted: 2026-06-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6824318
- keyword hits: large language model, large language models, llm, llms

### abstract

As large language models become more conversational and emotionally responsive, industry research characterizes affective engagement as "rare" and limited to small, isolated user groups. This exploratory mixed-methods study of Indian LLM users (N=31) challenges that characterization, demonstrating that markers of emotional dependency are more prevalent than industry self-reports suggest. Across four dependency indicators, 35.5% of participants report preferring AI over human sources for emotional support at least occasionally, 25.8% return to AI without clear need, and 73.9% of those for whom emotional engagement was applicable report feeling emotionally comforted by AI at least sometimes. A subset of 25.8% exhibit concurrent dependency across multiple dimensions simultaneously. High-dependency users defy Western vulnerability assumptions: those exhibiting the strongest concurrent markers are predominantly young women aged 18-25 living in shared or family housing, not in social isolation, with usage frequency and emotional comfort showing strong positive correlation (r=0.74). Qualitative responses reveal dependency drivers that diverge substantially from Western models-participants cite family dysfunction, privacy constraints in collective living, and absence of non-judgmental emotional outlets, suggesting a counterintuitive pattern wherein social proximity intensifies rather than mitigates AI dependency. These findings indicate that emotional dependency on LLMs is more prevalent than industry research acknowledges, and that vulnerability frameworks built on Western populations may systematically misidentify at-risk users in non-Western contexts, with significant implications for global AI safety policy and platform governance.

---

## uid: `doi:10.2139/ssrn.6878389`

- title: SAFE-GEM: Pre-Deployment Screening of GenAI Explanations in DAS Microseismic Monitoring
- authors: Md Shokor A Rahaman, Jafreezal Jaafar, Irving Paputungan
- affiliations: not stated
- posted: 2026-06-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6878389
- keyword hits: generative ai, instruction-tuned, llm, llms, prompting

### abstract

Context. Generative AI (GenAI) explanation layers are increasingly deployed in scientific monitoring software, including AI-based microseismic event detection on Distributed Acoustic Sensing (DAS) recordings. Fluent explanations can nevertheless contain unsupported signal claims, overconfident language, or misrepresentations of sensor evidence — known antecedents of inappropriate human reliance on automation.Objective. We develop and empirically evaluate a software-engineering framework that screens GenAI explanations before presentation to human verifiers, using computable proxies grounded in automation-trust and human-factors theory rather than expensive post-hoc user studies.Method. We propose SAFE-GEM (Safety-Aware Framework for GenAI Explanation Auditing in Microseismic Monitoring), a five-stage pipeline that (i) extracts symbolic signal evidence from each DAS window, (ii) generates explanations under five prompting strategies (P1–P5), (iii) audits claims against a 387-phrase controlled vocabulary, (iv) computes the Explanation-Induced Reliance Risk Score (EIRRS) from six theory-grounded components, and (v) issues a screening tier. Evaluation uses an 80-sample Utah FORGE stress-test subset enriched for high-confidence wrong predictions, six LLMs from five companies (2400 explanations), an all-494-sample distributional check, 30-explanation human-annotator validation, and an external expert-rating pilot.Results. P5 achieves the lowest EIRRS (0.150, 95% CI [0.129, 0.172]) and reduces the Unsupported Claim Rate by 80.0% relative to raw GenAI. P2 produces the highest EIRRS, coinciding with reduced hedging. P5 shows the lowest aggregate EIRRS across instruction-tuned local models; reasoning-focused models require separate calibration.Conclusion. SAFE-GEM provides a reproducible, theory-grounded screening layer — a proof-of-concept proxy, not validated safety certification. Operational threshold calibration, external expert ratings, and human-subject validation remain necessary future work.

---

## uid: `arxiv:2606.06089v1`

- title: Leveraging LLMs for Unstructured Claims Data Analysis
- authors: Robert D. Lieberthal, Richard Tran, Vietbao Phan, Jawand Singh, Elizabeth Sottung
- affiliations: not stated
- posted: 2026-06-04
- source: arXiv
- link: https://arxiv.org/abs/2606.06089v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Actuaries rely primarily on structured numerical data for reserving and ratemaking, while valuable predictive information in unstructured text including medical records, adjuster notes, and call transcripts remains largely unused. Manual processing of these documents is time-consuming, inconsistent across reviewers, and unscalable. We present a proof-of-concept framework using large language models (LLMs) to extract structured actuarial variables from unstructured claims data. We implement a two-stage processing architecture separating document-level extraction (Stage 1) from claim-level synthesis (Stage 2). A modular four-script Python pipeline processes synthetic FHIR-based claims data and real claims documents, extracting 36 actuarial variables across reserving, ratemaking, and claims management categories. We validate 14 core variables using two independent clinical expert reviewers scoring 20 synthetic claims on a five-point Likert rubric, achieving mean scores above 4.0 and a weighted kappa of 0.53. Integration with chain ladder reserving demonstrates practical actuarial value: severity-segmented analysis reduced reserve estimation error from 6.5% to 4.0%. The open-source implementation includes audit trails and confidence scoring, providing a replicable foundation for LLM-based actuarial variable extraction in property-casualty insurance.

---

## uid: `doi:10.2139/ssrn.6883279`

- title: An Equipment Health Optimization Method for Gas Gathering Stations Integrating Topology‐Constrained Mamba and Memory Agent
- authors: xin jing, Qingzeng cao, jie luo, jing cheng
- affiliations: not stated
- posted: 2026-06-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6883279
- keyword hits: large language model, large language models, llm, llms

### abstract

Gas gathering station equipment health management faces several challenges: dynamic dependency modeling, lack of interpretability, safety risks in decision-making, and difficulty in digitizing experiential knowledge. To address these challenges, this paper proposes a novel method integrating topological constraints with memory agents, constructing a three-layer closed-loop architecture of knowledge modeling, decision-making, and verification. First, static process topology is embedded as hard masks into a selective state-space model (Mamba) to enforce physical priors. Second, three dedicated memory agents (structure, parameter, state) unify prior knowledge, real-time data, and historical experience. Third, topology-constrained Mamba performs dynamic dependency reasoning, driving large language models (LLMs) to generate explainable decisions via rule retrieval and similar historical scenario matching. Finally, a formal theorem prover (Z3) performs formal verification of compliance with physical constraints and engineering safety rules, with validated decisions fed back for online model refinement. Experiments on real Supervisory Control and Data Acquisition (SCADA) data show that the method achieves 86.5% directional consistency, 3.4 ms inference latency, 94.2% top-1 alarm accuracy, and 4.72/5.0 expert score. It realizes 100% hazardous decision interception and 0% false rejection under defined constraints. This work provides a safe, interpretable, and continuously adaptive solution for gas gathering station equipment health management.

---

## uid: `doi:10.2139/ssrn.6885020`

- title: A Cartography of Open Collaboration in Open Source AI: Mapping Practices, Motivations, and Governance in 14 Open Large Language Model Projects
- authors: Johan Linaker, Cailean Osborne, Jennifer Ding, Ben Burtenshaw
- affiliations: not stated
- posted: 2026-06-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6885020
- keyword hits: large language model, large language models, llm, llms

### abstract

The proliferation of open large language models (LLMs) is fostering a vibrant ecosystem in artificial intelligence (AI). However, the methods of collaboration used to develop open LLMs, both before and after their public release, have not yet been systematically studied, limiting our understanding of how open LLM projects are initiated, organised, and governed, as well as the opportunities to further foster this ecosystem. We address this gap through an exploratory analysis of open collaboration throughout the development and reuse lifecycle of open LLMs, drawing on semi-structured interviews with the developers of 14 diverse open LLM projects. These collaborations span multiple artefact domains---including models, data, software, evaluation, compute, and community engagement---each enabling distinct forms of participation and involving different stakeholders that evolves across the LLM development lifecycle, shifting from concentrated, selective engagement in the early stages to broader, distributed participation after model release. The open LLM developers are motivated by a variety of social, economic, and technological motivations, ranging from democratising access to AI and promoting open science to building regional ecosystems and expanding language representation.These dynamics are coordinated through a range of governance structures, typically formal and professionalised to varying degrees, including centralised company-led efforts to decentralised grassroots initiatives. We synthesise our findings in a conceptual model of open collaboration in open LLM ecosystems, provide recommendations for practice, and conclude that openness in open source AI is not a uniform property but an emergent outcome of how collaboration is organised across interconnected artefact domains, lifecycle stages, and institutional contexts.

---

## uid: `arxiv:2606.06823v1`

- title: PandaAI: A Practical Agent CQ2 for Neuro-symbolic Data Analysis And Integrated Decision-Making in Quantitative Finance
- authors: Yuqi Li, Siyuan Liu, Bingjun Liu
- affiliations: not stated
- posted: 2026-06-05
- source: arXiv
- link: https://arxiv.org/abs/2606.06823v1
- keyword hits: large language model, large language models, llm, llms

### abstract

While deep learning has excelled in various domains, its application to sequential decision-making in finance remains challenging due to the low Signal-to-Noise Ratio (SNR) and non-stationarity of financial data. Leveraging the reasoning capabilities of Large Language Models (LLMs), we propose \textbf{PandaAI}, a closed-loop neuro-symbolic LLM agent with market regime modeling and constrained alpha generation, which bridges general LLM reasoning with financial rigor and suppresses the financial toxicity of LLM-generated outputs. To bridge the gap between general linguistic capability and financial rigor, we fine-tune a domain-specific LLM. Furthermore, we integrate this LLM into a modular architecture and form a closed-loop system. Unlike traditional models that optimize isolated prediction metrics, \textbf{PandaAI} is designed as a neuro-symbolic agent that navigates the complex, real-world financial environment with explicit risk awareness. Extensive experiments on CSI 300 stock data show that \textbf{PandaAI} achieves a $18.2\%$ higher Rank IC and $25.7\%$ lower maximum drawdown than state-of-the-art time-series models. Our constrained LLM generation and dual-channel adaptation method provide a general paradigm for LLM deployment in high-stakes sequential decision-making scenarios.

---

## uid: `doi:10.2139/ssrn.6891363`

- title: PRISM: Cost-Governed Adaptive Reasoning for Autonomous Recovery in Cloud-Native Lakehouse Pipelines
- authors: Akshay Sharma
- affiliations: not stated
- posted: 2026-06-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6891363
- keyword hits: large language model, large language models, llm, llms

### abstract

Cloud-native lakehouse pipelines fail in ways that retry-based orchestrators cannot resolve: a schema change is blindly re-executed rather than reconciled, an upstream latency spike is retried rather than recognized as a downstream service-level agreement (SLA) breach in waiting, and compound failures that span the schema, workload, and SLA layers simultaneously exceed any statically encoded remediation rule. Semantic reasoning with large language models (LLMs) can close this gap, but invoking an LLM on every operational event is prohibitively expensive and slow for production pipelines. This paper presents PRISM, whose central mechanism is the Adaptive Reasoning Governor (ARG): a lightweight, complexity-aware policy that decides, per event, whether a failure warrants the cost and latency of semantic reasoning or can be resolved by a deterministic fast path. The ARG routes only 7.3% of operational events to LLM reasoning, reducing inference cost by 87.7% relative to a full-LLM configuration while preserving 94.1% of its decision quality. Around this governor, PRISM coordinates schema management, workload balancing, SLA enforcement, and lineage-aware root cause analysis through a shared metadata fabric and a rollback-safe execution model.We evaluate PRISM using controlled fault-injection experiments over a synthetic financial transaction pipeline containing 50 million records and 47 orchestration DAGs. Across five independent evaluation runs, PRISM reduces mean time to resolution (MTTR) from 21.7 ± 3.4 minutes in a rule-based self-healing baseline to 9.6 ± 1.4 minutes while improving schema drift detection precision to 90.9% and SLA compliance to 96.0%.

---

## uid: `doi:10.2139/ssrn.6828039`

- title: Worst-Case Quality Collapse in KV Cache Quantization: A Per-Head Minimum-Cosine Diagnostic and a Norm-Direction Decomposition
- authors: Gregory Villines
- affiliations: not stated
- posted: 2026-06-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6828039
- keyword hits: large language model, large language models, llama, mistral, qwen

### abstract

Quantizing the key-value (KV) cache is the dominant lever for extending the usable context length of large language models on memory-constrained hardware. The methods that implement it are typically validated with average-case fidelity metrics-the mean cosine similarity of reconstructed cache tensors, or perplexity on a held-out corpus-each of which averages over the attention grid of layers, heads, and token positions. This paper presents evidence that those averages can conceal a worst-case failure mode in which a small number of (layer, head) units produce near-random output while corpus perplexity remains nominal. We introduce a per-head minimum-cosine probe: a diagnostic computed from a single FP16 forward pass that reports the minimum cosine similarity across the attention grid alongside the conventional mean. Applied to KIVI 4-bit and a paper-faithful reimplementation of TurboQuant across four models-Qwen2.5-7B, Qwen2.5-1.5B, Llama-3.1-8B, and Mistral-7B-v0.3-the probe surfaces an architecture-dependent collapse. At roughly 3.9× compression, KIVI reports a mean cosine of 0.983 on Qwen2.5-7B but a minimum of 0.588; uniform TurboQuant collapses to near-zero or negative minimum cosine on both Qwen models while matching its published fidelity on Llama-3.1-8B and Mistral-7B-v0.3. We further evaluate a norm-direction (N+D) decomposition-an 8-bit magnitude paired with a low-bit unit direction-which holds the minimum cosine in the 0.969-0.991 band across all four models at comparable compression, and an outlier-aware mixed-precision recipe that partially but incompletely rescues TurboQuant on Qwen. The probe requires no autoregressive generation, no downstream benchmark, and no held-out corpus, and runs in seconds. Code and benchmark artifacts are released under the Apache 2.0 license.

---
