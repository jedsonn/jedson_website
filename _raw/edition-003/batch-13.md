# Classification batch 13 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-13.answer.json` as a JSON array.

---

## uid: `arxiv:2606.29254v1`

- title: Travel-Oriented Reasoning Large Language Model via Domain-Specific Knowledge Graphs
- authors: Vignesh Ram Nithin Kappagantula, Shayan Hassantabar, Samuel Simpson, Golnaz Moallem
- affiliations: not stated
- posted: 2026-06-28
- source: arXiv
- link: https://arxiv.org/abs/2606.29254v1
- keyword hits: fine-tuning, large language model, large language models, llm, llms, qwen

### abstract

Large language models (LLMs) demonstrate broad reasoning abilities but struggle with accuracy and reliability in specialized domains such as travel, where reasoning depends on precise definitions, rules, and expert-defined conceptual frameworks, and where confident but unfounded outputs arise from a reasoning failure in which the model has not internalized the underlying domain graph rather than from missing domain knowledge alone. We propose a modular pipeline for building a travel-domain reasoning LLM grounded in an expert-designed knowledge graph (KG). Our pipeline integrates a travel KG that encodes domain entities and their relationships, a bottom-up construction procedure that walks the KG to produce multi-hop question answer (QA) pairs, a supervised fine-tuning stage that embeds the domain knowledge into a reasoning-capable LLM using the generated QA pairs as auditable reasoning traces, and a travel-domain benchmark dataset that measures the fine-tuned model's accuracy and calibration. We evaluate our approach using Qwen3-4B with LoRA adaptation. Our reasoning model achieves an $82.4\%$ exact match on the benchmark. This performance significantly outperforms the pretrained Qwen3-4B baseline at $22.4\%$. A calibration analysis decomposes the residual $17.57\%$ of errors into two distinct failure modes: an over-confident multi-label decoder that predicts both correct answers plus one spurious option on most dual-answer mistakes, and a smaller reasoning failure on single-answer questions where the supporting facts are present in the KG but the model fails to reconstruct the correct multi-hop path. This split confirms that explicit KG-grounded reasoning substantially improves the accuracy and uncertainty interpretation of LLMs in specialized domains, and isolates per-option calibration and trace-length-aware decoding as the next axes of improvement.

---

## uid: `arxiv:2607.09121v1`

- title: Augmenting Fundamental Analysis with Large Language Models: A RAG-Based System for Generating Investor Briefs
- authors: Bartosz Ziółko, Kacper Dobrzeniewski
- affiliations: not stated
- posted: 2026-07-10
- source: arXiv
- link: https://arxiv.org/abs/2607.09121v1
- keyword hits: gpt-4, large language model, large language models, llm, llms, retrieval-augmented

### abstract

In this study, we examine the opportunities brought by Large Language Models (LLMs) to various aspects of fundamental analysis of companies based on their reports as well as data and documents describing macroeconomic situation like GDP and inflation changes as well as documents filled to the U.S. Securities and Exchange Commission (SEC) which can be found in EDGAR. We were preprocessing those data and than sending via API to gpt-4o model in a Retrieval-Augmented Generation (RAG) like regime. We prepared as well a document describing an exemplar investor knowledge based on Kitchin cycles. We were scanning data important for analysis of 9 companies for 4 weeks. Using LLM we were producing automatic briefs about them. They were sent to nine participants who are individual investors to evaluate usefulness of such approach to data analysis.

---

## uid: `doi:10.2139/ssrn.7102067`

- title: Belief at Risk: Quantifying Agentic AI Model Risk with LLM-Inferred Bayesian State Filters
- authors: Matthew Francis Dixon
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7102067
- keyword hits: agentic, foundation model, large language model, large language models, llm, llms

### abstract

Agentic AI systems operate under uncertainty: they observe heterogeneous information, infer latent states of the environment, and take actions based on uncertain beliefs. This paper develops a probabilistic framework for quantifying and validating uncertainty in agentic AI by combining large language models (LLMs) with Bayesian state estimation. The central idea is to treat an LLM as a semantic observation model that converts high-dimensional evidence into a probability distribution over latent operating regimes. A Bayesian filter then combines this semantic evidence with a transition prior to produce temporally coherent and auditable belief states. The resulting framework separates uncertainty quantification from decision making and introduces diagnostics based on posterior entropy, belief-state drift, calibration error, and consequence-sensitive loss measures.A variational characterization of the Bayesian update is developed, providing a principled mechanism for integrating foundation models into probabilistic reasoning systems. The framework supports uncertainty monitoring, calibration analysis, residual-risk assessment, and governance controls for agentic AI. An empirical case study and ablation study demonstrate that Bayesian filtering substantially reduces posterior instability and uncertainty while improving regime-classification accuracy and reducing downstream risk measures. More broadly, the proposed approach provides a bridge between probabilistic reasoning, Bayesian filtering, uncertainty quantification, and the validation of agentic AI systems operating in high-consequence decision environments.

---

## uid: `arxiv:2607.14385v2`

- title: MamaBench: Benchmarking LLM Robustness in Maternal and Child Health Diagnosis through Counterfactual Clinical Perturbation
- authors: Thanni Adewuyi, Anuoluwa Sotome, Samuel Okoko, Angel Ezendu, Oluwafunke Akinbuwa, Oluwaseun Odunsi, Oluwasegun Oguntuase, Ifeoma Nwabueze
- affiliations: not stated
- posted: 2026-07-15
- source: arXiv
- link: https://arxiv.org/abs/2607.14385v2
- keyword hits: claude, large language model, large language models, llm, llms, retrieval-augmented

### abstract

Large language models achieve strong scores on medical benchmarks, yet these benchmarks evaluate each question in isolation, providing no measure of whether a system can distinguish clinically similar presentations requiring different interventions. We introduce MamaBench, the first counterfactual benchmark for maternal and paediatric AI: 434 expert-authored clinical narratives in 217 pairs across 371 pathologies, evaluated via the Bias Trap Rate (BTR), the conditional probability that a model fails the counterfactual given success on the base case. We propose Evidence-Anchored RAG (EA-RAG), a three-stage retrieval method that replaces aggregate similarity with an evidence coverage objective through clinical parameter extraction, coverage auditing, and contrastive sub-queries. Across eight configurations of four frontier LLMs, base accuracy overstates robust accuracy by 16-28 percentage points in every model. EA-RAG achieves 20.3% BTR and 65.0% robust accuracy on Claude Sonnet 4.6, a 5.5 percentage point BTR reduction without degrading base accuracy. The residual 20% BTR confirms that counterfactual robustness in clinical AI remains an open challenge. Keywords: counterfactual evaluation, clinical AI, maternal healthcare, retrieval-augmented generation, diagnostic robustness

---

## uid: `doi:10.2139/ssrn.6977604`

- title: Fine-Tuning DeepSeek-R1-Distill-Qwen-1.5B for Financial Sentiment Analysis with LoRA
- authors: Daniela Sameny, Georges Lissoko
- affiliations: not stated
- posted: 2026-07-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6977604
- keyword hits: deepseek, fine-tuning, large language model, large language models, llm, llms, qwen

### abstract

Financial sentiment analysis is a critical component of automated trading systems, news monitoring, and quantitative research, but it requires models that understand domain-specific terminology and tone. General-purpose large language models (LLMs) are not directly suitable for this task in a zero-shot setting. We present a parameter-efficient fine-tuning study of DeepSeek-R1-Distill-Qwen-1.5B, the opensource distillation of DeepSeek-R1, on the Financial PhraseBank corpus [6]. Using Low-Rank Adaptation (LoRA) [4] combined with 4-bit quantization (QLoRA) [3], we adapt the model on a single consumer-grade GPU. Evaluated on a held-out test subset of 300 expert-annotated sentences, our fine-tuned model reaches an accuracy of 84.33% and a weighted F1 of 84.17%, compared to 54.00% accuracy and 45.32% F1 for the zero-shot base model. This corresponds to an absolute improvement of +30.33 accuracy points and +38.85 F1 points (relative gains of +56.2% and +85.7% respectively). Our results show that lightweight LoRA fine-tuning on a small, well-curated domain dataset is sufficient to dramatically specialize a general-purpose distilled LLM for financial sentiment, while remaining accessible to researchers without dedicated compute infrastructure.

---

## uid: `doi:10.2139/ssrn.7155798`

- title: Improving cultural ecosystem service assessment from social media data using domain-adaptive large language models
- authors: Yufei Chen, Shiqin Dai, Yiming Lei, Lei Zhao, Jiabo Xie, Ruiqing Qin, Kangping Meng, Qinhua Fang
- affiliations: not stated
- posted: 2026-07-21
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
- posted: 2026-07-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7167544
- keyword hits: large language model, large language models, llama, llm, llms, text embedding

### abstract

Accurate prediction of multicomponent fuel properties is a longstanding bottleneck in surrogate fuel design, where nonlinear composition property relationships limit the reliability of empirical correlations and conventional machine learning (ML). In present study we show that large language models (LLMs) pretrained on molecular and general-purpose text corpora can predict physiochemically distinct properties of RP-3 kerosene surrogates with near unity accuracy directly from SMILES strings and tabular to text embeddings. Evaluating four supervised ML model (SVM, GPR, RF and k-NN) against three transformer-based representations (ChemBERTa, MolFormer and TinyLlama (1.1B)) across the smaller and larger datasets, we found that the predictive performance is governed by an interplay between data scale and representation chemistry. At small sample size, TinyLlama yielded the most stable embeddings (R2 = 0.9962), where at scale, ChemBERTa SMILES pretraining surpasses all other models, explaining 99.95% of property variance (RMSE = 0.126, MRE = 0.18%), outperforming both MolFormer and TinyLlama, as well as supervised ML models. Notably, TinyLlama lacking any chemistry specific pretraining, still achieves R2 = 0.995 purely from serialized composition and structured prompts, demonstrating that contextual language embeddings alone encode transferable chemical information. Cosine similarity and residual analyses further confirms that the pretrained representations capture meaningful differences between aromatic and saturated hydrocarbon structures while maintain strong predictive stability. These findings demonstrate that pretrained language models can provide a scalable and chemically informed alternative to conventional composition-based regression for RP-3 kerosene fuel property prediction, with potential applications in surrogate fuel design, combustion kinetic modeling and molecular property prediction (MPP).

---

## uid: `doi:10.2139/ssrn.4448938`

- title: Can ChatGPT Kill User-Generated Q&A Platforms?
- authors: Junzhi Xue, Lizheng Wang, Jinyang Zheng, Yongjun Li, Yong Tan
- affiliations: not stated
- posted: 2023-05-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.4448938
- keyword hits: chatgpt, large language model, large language models, llm, llms

### abstract

Large Language Models (LLMs) such as ChatGPT are expected to significantly reshape learning, skill acquisition, and knowledge creation. Their impact on user-generated knowledge-sharing (Q&A) platforms has important implications for the comparative value and future co-evolution of Q&A platforms and LLMs, as well as for the future learning of LLMs. Using multiple empirical designs, we estimate that the launch of ChatGPT led to an average 14.09% reduction in the number of questions posted on Stack Overflow, an effect that intensifies over time and reaches a 27.88\% decline by May 2023. Intriguingly, this decrease in quantity is accompanied by a substantial increase in the average quality of the remaining questions. Further analysis shows that these quantity and quality changes can be explained by two mechanisms: (1) uneven substitution by ChatGPT, where simpler and mid-to-low-quality questions are more likely to disappear; and (2) direct quality improvement, after accounting for the quantity reduction, suggesting positive spillovers from the time and search cost savings provided by ChatGPT assistance to improvements in question quality. Additional heterogeneity analyses reveal stronger effects on both question quantity and quality among inexperienced users, significant declines in both user retention and new user acquisition, and systematic variation across topics characterized by tenure, broadness, and depth. These findings delineate the coexistence boundary between LLMs and Q&A platforms, suggesting an evolution toward smaller but more specialized, high-expertise Q&A communities alongside growing welfare gains and value transfer to LLMs. They also offer actionable insights for platform managers and LLM developers on sustaining the value of user-generated content ecosystems while supporting long-run model improvement.

---
