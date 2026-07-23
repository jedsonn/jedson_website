# Classification batch 169 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-169.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6968038`

- title: Toward Explainable Traffic Crash Liability Analysis via Neural-Symbolic Multimodal Reasoning: Integrating Visual Perception with Legal Knowledge Graphs
- authors: Jingyun Xu, Yuzhi Chen, Xiaoxi Hu, Yuanchang Xie, Xinyu Zhang, Jialun Yin, Chen Wang
- affiliations: not stated
- posted: 2026-06-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6968038
- keyword hits: large language model, large language models

### abstract

Determining traffic crash liability relies on rigorous on-site evidence and legal provisions and involves substantial manual intervention and potential human error. However, intelligent traffic monitoring systems focus on detection and tracking and cannot provide legally admissible crash analysis and liability adjudication. Moreover, emerging multimodal large language models (MLLMs) suffer from object hallucination that distorts or omits physical evidence, and their opaque reasoning cannot produce auditable evidence-to-law chains, resulting in a mismatch with judicial requirements for interpretable and verifiable liability facts. This paper proposes a neural-symbolic law-driven (CrashLex) framework that integrates visual perception with legal knowledge graph reasoning to align multimodal inference with judicial standards. Within CrashLex, a dual-query vision-language architecture employs parallel semantic and symbolic streams to mitigate object hallucination, utilizing Scene Queries for global context modeling and Perception Queries for fine-grained atomic feature extraction, respectively. Integrating these atomic facts, a domain-specific legal knowledge graph establishes the rigorous evidentiary basis, mapping observable physical conditions into statutory legal elements. A logic-driven aggregation protocol then imposes explicit constraints derived from verified facts and statutory provisions onto the inference process, thereby ensuring fully traceable and interpretable liability adjudication. Experimental results on the DeepAccident dataset demonstrate that CrashLex achieves 94.0% liability adjudication accuracy and suppresses object hallucination to 2.8%, yielding an 84% reduction in object hallucination rate compared with the best-performing MLLM baseline. CrashLex grounds legal judgments in deterministic legal rules rather than relying solely on unconstrained probabilistic generation, delivering auditable reasoning chains that satisfy judicial interpretability requirements.

---

## uid: `doi:10.2139/ssrn.6944058`

- title: Deep Neural Newsvendor Optimization with Fractile Adjustment and LLM-Based Feature Discovery
- authors: Zhe FU, Frank (Youhua) Chen, Mengzhuo Guo, Shaochong Lin, Jindou LUO
- affiliations: not stated
- posted: 2026-06-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6944058
- keyword hits: llm, llms

### abstract

Retail data encompasses numerical variables and semantic labels (e.g., store locations, product names, and temporal data) that capture external demand drivers but are traditionally reduced to opaque categorical codes. The problem is twofold: we convert these semantic labels into informative features, then optimize data-driven newsvendor decisions. We propose a Deep Fractile Newsvendor framework integrating an LLM-based semantic-to-source mapper with decision-focused neural learning. The LLM identifies verifiable external data sources from semantic labels; numerical features are then retrieved and retained if they enhance profit. For ordering, we use the empirical mixture distribution (EMD) and the cost-implied critical fractile as priors; the model learns only a bounded, dimensionless fractile adjustment and maps it through the EMD to the order quantity. Across three real-world datasets, external-feature integration significantly improves out-of-sample profits in two cases; gains are marginal in the third because managers already captured key external drivers. Overall, the proposed fractile policy matches or outperforms established benchmarks. By utilizing LLMs to discover verifiable data sources---rather than generating demand forecasts or ordering decisions---this framework enables managers to enrich sparse operational data while maintaining transparent, stable, and auditable inventory policies.

---

## uid: `doi:10.2139/ssrn.6965066`

- title: Artificial Intelligence-Based Risk Calculator for Endometriosis Surgery
- authors: Liron Bar-El, Fernanda  Walsh Fernandes, Adeline Chin, Sushasree  VS. Kumar, Samuel Ockunzzi, Patrick  L. Handwork, Cara  R. King, Samer Albahra
- affiliations: not stated
- posted: 2026-06-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6965066
- keyword hits: large language model, llm

### abstract

Background: Endometriosis excision surgery carries complication rates up to 16% in tertiary centers, yet no preoperative risk prediction tools exist to account for disease-specific factors in this low-comorbidity population. We aimed to develop and validate a machine learning–based model to predict perioperative complications. Methods: We conducted a retrospective cohort study of adults (≥18 years) who underwent endometriosis excision surgery within the Cleveland Clinic health system (Ohio and Florida) from 2017–2023. Preoperative predictors were derived from electronic medical records, including structured fields, clinical notes, radiology reports, and medication data, while postoperative documentation, laboratory results, and imaging reports were used to ascertain outcomes. Unstructured text was converted to discrete variables using an internally developed, AI-based large language model (LLM)‑assisted abstraction workflow. An automated machine-learning framework was used to train four binary complication classifiers corresponding to major, minor, colorectal, and genitourinary complications. An independent audit review by three clinicians was performed to validate outcome labeling and key extracted variables. Findings: The cohort included 1,667 surgical episodes among 1,622 patients. Major complications occurred in 19·6% of surgical episodes, minor complications in 10·9%, colorectal adverse events in 4·3%, and genitourinary adverse events in 13·7%. Colorectal and genitourinary adverse events were predominantly functional rather than structural. Model performance varied by outcome, with area under the receiver operating characteristic curve (AUROC) of 0·60 for major complications, 0·67 for minor complications, 0·82 for colorectal adverse events, and 0·63 for genitourinary adverse events. Interpretation: We developed and internally validated an AI-assisted, preoperative risk prediction model for perioperative complications following endometriosis excision surgery. Model discrimination was modest for aggregated outcomes and strongest for colorectal adverse events, likely reflecting limited power for rare events and a single-center cohort. Future work will focus on incorporating multi-institutional cohorts to improve power, enhance generalizability, and support further model refinement and clinical implementation.

---

## uid: `doi:10.2139/ssrn.6981707`

- title: Mitigating Think-Answer Mismatch in Large Language Model Reasoning Through Noise-Aware Advantage Reweighting
- authors: Peijun Shen, Si Shen, Wenhua Zhao, Danhao Zhu
- affiliations: not stated
- posted: 2026-06-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6981707
- keyword hits: large language model, llama, qwen

### abstract

Group-Relative Policy Optimization (GRPO) is a key technique for training large reasoning models, yet it suffers from a potential challenge: the Think-Answer Mismatch, where noisy reward signals corrupt the learning process. This problem is most severe in unbalanced response groups, paradoxically degrading the signal precisely when it should be most informative. To address this challenge, we propose Stable Group-Relative Policy Optimization (S-GRPO), a principled enhancement that derives optimal, noise-aware advantage weights to stabilize training. Our comprehensive experiments on mathematical reasoning benchmarks demonstrate S-GRPO's effectiveness and robustness. On various models, S-GRPO significantly outperforms DR. GRPO, achieving performance gains of +2.5% on Qwen-Math-7B-Base, +2.2% on Llama-3.2-3B-Base, and +2.4% on Qwen-Math-1.5B-Instruct. Most critically, while standard GRPO fails to learn under 20% synthetic reward noise, S-GRPO maintains stable learning progress. These results highlight S-GRPO's potential for more robust and effective training of large-scale reasoning models.

---

## uid: `doi:10.2139/ssrn.6872799`

- title: The Role of Generative Artificial Intelligence in Enhancing Instructional Material Development: A Qualitative Inquiry Among Elementary School Teachers
- authors: Jexille Santiago
- affiliations: not stated
- posted: 2026-06-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6872799
- keyword hits: chatgpt, gemini, generative artificial intelligence

### abstract

This qualitative study explored the lived experiences of ten (10) veteran elementary school teachers at Pio V. Corpus Central School in utilizing Generative Artificial Intelligence (GenAI) for instructional material development. Using a phenomenological research design and "Kuwentuhanstyle" semi-structured interviews, the study investigated how tools like Canva, ChatGPT, and Gemini assist educators in aligning with the MATATAG Agenda. Thematic analysis, following the Braun and Clarke framework, revealed three core themes: (1) The Digital Hurdle and Cognitive Load, characterized by initial technical overwhelm; (2) Efficiency vs. Pedagogical Authenticity, highlighting the balance between AI speed and teacher judgment; and (3) Aesthetic Enhancement and Student Engagement, noting significant improvements in visual quality. Findings indicate that while GenAI significantly reduces administrative fatigue and enhances material quality, the "human-in-the-loop" remains essential for pedagogical integrity. The study recommends localized mentoring through "Buddy Systems" in School Learning Action Cells (SLAC) to support veteran teachers in their digital transition.

---

## uid: `doi:10.2139/ssrn.6533458`

- title: Assessing AI-Mediated Interviewing Quality: A Theory-Grounded Comparative Study of Leading Models in Evaluation Contexts
- authors: Ali Safarnejad, Hippolyte Lefebvre
- affiliations: not stated
- posted: 2026-06-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6533458
- keyword hits: generative ai, large language model, large language models

### abstract

As large language models are increasingly used in evaluative settings for their conversational potential in interviews, systematic frameworks for assessing their methodological quality are still lacking. Drawing on evaluation, qualitative interviewing, and validity theories, this study develops a theory-grounded framework for evaluating the quality of AI-mediated interviewing in evaluation contexts. This framework is then operationalized into eight assessment measures and applied in a convergent mixed-methods design to compare six generative AI models (five prompted-only and one fine-tuned) across two realistic evaluation interview scenarios. Findings reveal that AI models reliably detected and probed incomplete or irrelevant responses, and the fine-tuned model matched human performance on nearly 70% of quality measures. However, performance was contextdependent, and models struggled with neutrality and clarification probing. The study contributes a replicable assessment framework, an empirical benchmark for AI interviewing performance, and guidance on appropriate deployment conditions and essential human oversight mechanisms.

---

## uid: `doi:10.2139/ssrn.6968541`

- title: Assessing the Accuracy and Performance of Vision and Language Models in Dermatological Classification of Benign Skin Lesions, BCC, SCC, and Melanoma
- authors: Natalie Vidal
- affiliations: not stated
- posted: 2026-06-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6968541
- keyword hits: claude, gemini

### abstract

We investigate the performance of four Vision and Language Models (VLMs) in classifying human skin-lesion images. We curated a set of 800 pathology-confirmed skinlesion photographs, evenly divided among four groups: 200 benign lesions, 200 Basal Cell Carcinomas (BCC), 200 Squamous Cell Carcinomas (SCC), and 200 melanomas. Each image was presented individually to OpenAI's GPT 5.5 Thinking, Google's Gemini Flash 3.5, Anthropic's Claude Opus 4.8, and Grok 4.3 Expert. Each VLM was asked first to classify the lesion as benign or non-benign, and then, where applicable, to identify the non-benign subtype. The results showed that Gemini Flash 3.5 achieved the highest binary accuracy at 79.38%, followed closely by Claude Opus 4.8 at 78.38%, GPT 5.5 Thinking at 73.13%, and Grok 4.3 Expert at 64.88%. For exact four-class classification, GPT 5.5 Thinking achieved the highest accuracy at 55.13%, followed by Gemini Flash 3.5 at 51.00%, Claude Opus 4.8 at 49.75%, and Grok 4.3 Expert at 41.50%. Our findings underscore both the promise and the limitations of contemporary VLMs in skinlesion assessment, suggesting that none can yet provide reliable standalone guidance for unsupervised layperson self-triage.

---

## uid: `arxiv:2606.24245v3`

- title: AutoSpec: Safety Rule Evolution for LLM Agents via Inductive Logic Programming
- authors: Pingchuan Ma, Zhaoyu Wang, Zimo Ji, Yuguang Zhou, Zhantong Xue, Zongjie Li, Shuai Wang, Xiaoqin Zhang
- affiliations: not stated
- posted: 2026-06-23
- source: arXiv
- link: https://arxiv.org/abs/2606.24245v3
- keyword hits: large language model, llm

### abstract

Large language model (LLM) agents increasingly automate complex tasks by integrating language models with external tools and environments. However, their autonomy poses significant safety risks: agents may execute destructive commands, leak sensitive data, or violate domain constraints. Existing safety approaches face a fundamental tradeoff: hand-crafted rules are interpretable but brittle, with overly conservative rules blocking safe operations (high false positives) while permissive rules miss unsafe behaviors (high false negatives). Neural classifiers lack the interpretability required for safety-critical deployments. We present AutoSpec, a framework that automatically evolves deployed expert-designed safety rules from user safe/unsafe annotations through counterexample-guided inductive synthesis (CEGIS) guided by inductive logic programming (ILP). Starting from the expert rules and a stream of annotated traces, AutoSpec iteratively evaluates rules, mines false-positive and false-negative counterexamples, uses ILP to learn which predicates discriminate them, generates candidate rule edits, and verifies candidates to select the best revision. The key insight is that ILP efficiently identifies predicates that appear frequently in false negatives but rarely in false positives (or vice versa), dramatically pruning the exponential search space of rule edits. This continues until convergence, producing interpretable rules that balance precision and recall. We evaluate AutoSpec on 291 execution traces spanning code execution and embodied agent domains. AutoSpec raises rule F1 to 0.98 and 0.93 across the two domains, achieving up to 94% false positive reduction while maintaining high recall, and converges within 4-5 iterations. The ILP-guided approach achieves up to 4.8x higher F1 than heuristic CEGIS. The learned rules are human-readable, auditable, and generalize to unseen scenarios.

---
