# Classification batch 8 of 20, edition 17

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-017/batch-8.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7241998`

- title: Simulating Firm Decision Making with LLMs: A Scalable Experimental Framework for Strategy Research
- authors: Han Jiang, Xiaoran Ma, Jing Wu
- affiliations: not stated
- posted: 2026-08-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7241998
- keyword hits: large language model, large language models, llm, llms

### abstract

A central challenge in strategic management research lies in rigorously identifying the causal links between contextual factors and firms' strategic decisions. Observational studies are inherently constrained by the absence of credible counterfactuals, while conventional experimental approaches trade off among realism, scalability, and control. This study proposes a scalable experimental framework that leverages large language models (LLMs) as simulated corporate executives to address these limitations. The framework endows LLM agents with firm-specific contextual profiles and elicits strategic decisions that approximate those of actual firms. Since the same agent generates decisions under both the baseline condition and the treatment condition with an exogenous shock, the within-agent difference directly mirrors the average treatment effect on the treated (ATT) logic from the potential outcome framework, thereby circumventing the non-random assignment of contextual factors that challenges observational designs. We validate this framework through two experiments, on R&D investment and facility allocation decisions respectively, each employing a multi-step design: corroborating the convergence between LLM-simulated and actual firm decisions to establish face validity, introducing an exogenous shock to identify the within-agent treatment effect, and benchmarking the LLM-identified treatment effect against real-world difference-indifferences estimates. Across both experiments, the LLM-identified treatment effects converge with real-world evidence identified via quasi-experimental designs, providing external validation for the framework. These results establish the generalizability of the framework across distinct strategic contexts and demonstrate that LLM-based experimental simulations can serve as credible, scalable, and cost-effective instruments for investigating the cause-and-effect links underlying firms' strategic decision making.

---

## uid: `doi:10.2139/ssrn.6698538`

- title: Toward Sustainable On-Device Intelligence: A Survey on Energy-Efficient RAG Systems with Small Language Models
- authors: Zhiyuan Cheng, Longying Lai, Yue Liu, Yu Sun
- affiliations: not stated
- posted: 2026-07-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6698538
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

The proliferation of Large Language Models (LLMs) has driven a paradigm shift toward ondevice inference, motivated by privacy preservation, latency reduction, and offline capability. Simultaneously, Retrieval-Augmented Generation (RAG) has emerged as the dominant pattern for grounding language model outputs in external knowledge. However, deploying RAG pipelines on resource-constrained edge devices-smartphones, IoT gateways, and embedded systems equipped with Neural Processing Units (NPUs)-introduces a complex multi-dimensional trade-off among accuracy, latency, memory footprint, energy consumption, and carbon emissions. This survey is the first to comprehensively review the three-way intersection of on-device AI inference optimization, retrieval-augmented generation, and Green AI / sustainability. We systematically examine (i) model compression techniques-quantization, pruning, knowledge distillation-with emphasis on NPUaware optimization; (ii) on-device RAG system architectures including lightweight retrieval, context compression, and modular frameworks; and (iii) energy measurement, carbon footprint estimation, and sustainable inference strategies for edge deployment. As our core contribution, we propose ALEMC, an evaluation framework extending conventional metrics with explicit Energy and Carbon dimensions, and synthesize design principles for building sustainable on-device RAG systems. We review 122 papers spanning 2017-2026, identify open challenges in hardware-software co-design, standardized energy benchmarking, and lifecycle-aware model selection, and outline future research directions at this rapidly evolving intersection.

---

## uid: `doi:10.2139/ssrn.7142038`

- title: Are LLMs Reliable in Interpreting Legal Documents?
- authors: Runhua Wang
- affiliations: not stated
- posted: 2026-08-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7142038
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

The reliability of the performance of large language models ("LLMs") in the legal profession remains doubtful, even though they are being broadly applied in reviewing and analyzing legal documents. This study tests the reliability of such legal work by various models and prompting strategies. It shows that after reviewing documents that involve controversial legal issues, LLMs returned contradictory binary outputs to an identical question not only across different models and prompts but also across user accounts and query times. After being presented with reasoning from other models or from their own earlier responses, LLMs changed their answers to varying degrees without a discernible pattern. These inconsistencies undermine the stability of LLMs in conducting legal analyses. One reason is that LLMs remain incapable of performing legal syllogisms and other legal reasoning skills effectively. Unlike inconsistent legal reasoning or interpretation by human judges, the inconsistencies arising from LLMs may heighten concerns about procedural justice.

---

## uid: `doi:10.1109/mc.2026.3664470`

- title: Unleashing the Potential of Large Language Models: A Blueprint for Real-Time, Enterprise-Ready Deployments
- authors: Muhammad Faizan Raza, Shuo, Yang, Satish Mahadevan Srinivasan, Joanna F. DeFranco
- affiliations: not stated
- posted: 2026-08-01
- source: arXiv
- link: https://arxiv.org/abs/2608.00419v1
- keyword hits: large language model, large language models, llm, retrieval-augmented

### abstract

Large language models deployed in real-time, regulated settings face knowledge staleness, catastrophic forgetting, hallucination, and weak feedback loops. We present a unified, pattern-driven LLMOps architecture integrating real-time data ingestion, continual learning, retrieval-augmented generation (RAG), and human-in-the-loop feedback into a single operational pipeline. Four contributions map to established software design patterns: an adaptive ingestion pattern orchestrator (AIPO) evaluated with FreshStreamBench; STAR+FAR continual learning with sparse temporal adapter routing and freshness-aware replay; SAGE, an SLO-aware adaptive retrieval policy predicting a per-query passage budget to meet tail-latency targets; and an automated feedback-driven convergence stage with RLHF triggers. The result reduces latency-cost-accuracy trade-offs while supporting auditability and rollback for high-risk sectors such as health care and finance.

---

## uid: `doi:10.2139/ssrn.7200563`

- title: Prompt-Dependent Clinical Reasoning, Confidence, and Risk Representation Across Large Language Models in Esophagectomy Assessment​
- authors: Mosebetsi  Michael Moleka, Fan Yang, Zilong Lu, Shuqi Jia, Callista  Eudora Sanjaya, Najwa  Zahra Fakhria, Lisa  Seow Weiyan, Pallavi KRISHNAPPA
- affiliations: not stated
- posted: 2026-08-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7200563
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

Background: For high-risk procedures such as esophagectomy, surgeons may increasingly encounter large language model (LLM) outputs that combine risk estimates with ranked clinical factors, categorical risk labels, and expressed confidence. The reliability of these accompanying representations is important for patient safety: prompt-dependent changes in stated risk factors or confidence could misrepresent the clinical basis of an assessment despite unchanged patient information. Methods: In this retrospective cohort study, standardised outcome-blinded clinical vignettes were created for 299 patients undergoing curative-intent esophagectomy. Five LLMs evaluated each vignette under zero-shot, structured-reasoning, and simulated multidisciplinary-team prompts, producing 4485 assessments and 22 425 ranked factors. Factors were harmonised through automated outcome-blinded mapping into 24 clinical categories. We evaluated prompt-related factor shifts, within-model stability, intermodel agreement, associations between stated factors and LLM-assigned probabilities or prediction error, factor-based reconstruction of assigned probabilities, self-reported confidence, and agreement between categorical and numerical risk outputs. Findings: All 10 within-model prompt comparisons showed significant changes in ranked factor distributions after Holm adjustment (all adjusted p<0·001). Mean rank-weighted Jaccard distance ranged from 0·262 to 0·611, while pairwise intermodel similarity ranged from 0·273 to 0·526. All five models selected the same highest-ranked factor for only 6·4–14·7% of assessments. Although 20 of 150 reasoning–prediction correlations remained significant after false-discovery-rate adjustment, only one involved prediction-error change; no pooled patient-clustered association remained significant. Eight of ten prompt-related confidence contrasts were significant, but the pooled confidence–error association was not (p=0·193). Numerical probabilities increased from low to intermediate to high categorical-risk labels in all 15 systems, although distributions overlapped. Interpretation: Small changes in prompting can substantially alter the factors and confidence that LLMs present as the basis for surgical risk assessment. These outputs should be treated as model-reported risk representations, not verified clinical reasoning. Without validation of their stability and relation to patient outcomes, fluent explanations and high confidence could create misplaced trust and potentially unsafe AI-supported perioperative decisions.FundingNo specific funding.​

---

## uid: `doi:10.2139/ssrn.7225573`

- title: Towards Effective Long Video Understanding of Multimodal Large Language Models via One-shot Clip Retrieval
- authors: Tao Chen, Shaobo Ju, Qiong Wu, Chenxin Fang, Kun Zhang, Jun Peng, Hui Li, Yiyi Zhou
- affiliations: not stated
- posted: 2026-08-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7225573
- keyword hits: gpt-5, large language model, large language models, qwen, retrieval-augmented

### abstract

Due to excessive memory overhead, most Multimodal Large Language Models (MLLMs) can only process videos of limited frames. In this paper, we propose an effective and efficient paradigm to remedy this shortcoming, termed One-shot video-Clip based Retrieval-Augmented Generation (OneClip-RAG). Compared with existing video RAG methods, OneClip-RAG makes full use of the merits of video clips for augmented video understanding in terms of both knowledge integrity and semantic coherence. Besides, it is also equipped with a novel and concise paradigm that can unify instruction-aware video chunking and clip selection in one processing step, avoiding redundant computations. To improve instruction-clip alignment, we further propose a new dataset called SynLongVideo and design a progressive training regime for OneClip-RAG. OneClip-RAG is plugged into three recent MLLMs and validated on a set of long-video benchmarks. Experimental results not only show the obvious performance gains by OneClip-RAG over MLLMs, e.g., boosting Qwen3-VL 8B to the level of GPT-5 on MLVU, but also show its superior efficiency in handling long videos, e.g., enabling LLaVA-Video understand up to an hour of videos in less than 1.2 minutes on a single 4090 GPU. Our code is released at: https://github.com/Tao-Chen-xmu/OneClip-RAG.

---

## uid: `doi:10.2139/ssrn.7199158`

- title: APCD: Adaptive Path-Contrastive Decoding for Reliable Large Language Model Generation
- authors: Tianyu Zheng, Hong Wu, Jiaji Zhong
- affiliations: not stated
- posted: 2026-08-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7199158
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Reliable text generation is critical for deploying large language models (LLMs) in real-world applications, particularly in high-stakes domains such as medicine. To improve factual reliability, various inference-time methods have been proposed, including logit-level methods that modify token probability distributions and representation-level methods that manipulate intermediate model representations. However, most existing approaches operate on a single decoding trajectory, limiting their ability to explore alternative reasoning paths and making them susceptible to error accumulation. To address this limitation, we propose Adaptive Path-Contrastive Decoding (APCD), an adaptive multi-path contrastive decoding framework that improves factual reliability without model retraining or fine-tuning. APCD comprises two key components: Entropy-Driven Path Expansion, which adaptively expands the decoding process only at high-uncertainty decision points, and Divergence-Aware Path Contrast, which dynamically regulates contrastive interactions among parallel decoding paths based on their distributional divergence to balance diversity and coherence. We evaluate APCD on four LLM backbones across eight benchmarks spanning both general-domain and medical question answering tasks. Experimental results demonstrate that APCD consistently outperforms strong inference-time baselines in factual accuracy while maintaining competitive inference efficiency. These results demonstrate the robustness and generalizability of APCD across diverse models and tasks, highlighting its effectiveness as a practical inference-time decoding framework for reliable LLM deployment, particularly in high-stakes domains such as medicine. Code is available at https://github.com/zty-king/APCD.

---

## uid: `arxiv:2608.02941v1`

- title: Aligned in Form, Not in Meaning: The Comprehension - Containment Decoupling of LLM Safety in Low-Resource Bangla Derogatory Speech
- authors: Shadab Bin Habib, A K M Ferdous Reza Habib, Subarno Neel, Adib Sakhawat
- affiliations: not stated
- posted: 2026-08-03
- source: arXiv
- link: https://arxiv.org/abs/2608.02941v1
- keyword hits: chain-of-thought, large language model, large language models, llm

### abstract

We audit five frontier large language models on native Bangla derogatory speech (gali) across six protocols to test a single hypothesis: Comprehension-Containment Decoupling. We propose that contemporary safety alignment is bound to high-resource surface forms rather than harmful meaning, causing a model's capacity to comprehend a low-resource slur and its capacity to contain it to operate independently. Every protocol corroborates this hypothesis against a human-calibrated baseline (kappa = 0.84). At baseline, models exhibit a 7.92 percentage point comprehension deficit in Bangla while maintaining an identical 92.83% token leakage rate across both languages. Severity calibration tracks surface anatomical cues over compositional harm (+4.00 error on mild slang; -2.00 on threats), while apparent containment gains under orthographic perturbation prove to be a tokenizer-driven "containment mirage." Crucially, explicit Chain-of-Thought reasoning rescues comprehension (94.72% Pass) while systematically dismantling containment (96.23% Use). Furthermore, expert-persona framing collapses refusal to 6.57%, revealing that keyword-based filters ignore dehumanizing communal slurs entirely. Our findings demonstrate that high-resource benchmarks cannot certify low-resource safety, necessitating meaning-grounded containment.

---
