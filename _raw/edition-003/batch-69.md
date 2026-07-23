# Classification batch 69 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-69.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7009890`

- title: Semantic and Lexical Retrieval-Augmented Large Language Models for Code Summarization
- authors: Jiawei Wang, Chunli Xie, Wei Zhu, Chunpeng Kang
- affiliations: not stated
- posted: 2026-06-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7009890
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

As software systems continue to grow in scale and complexity, automatically generating readable and semantically accurate code summaries has become increasingly important for program comprehension and software maintenance. Although large language models (LLMs) have demonstrated strong generation capabilities in code summarization tasks, they often produce verbose summaries, omit key information, or suffer from semantic hallucinations when relying solely on source code as input. Retrieval-augmented generation (RAG) methods mitigate these issues by introducing external code-summary examples as references. However, most existing approaches depend on a single retrieval strategy, making it difficult to simultaneously capture deep semantic similarity and precise keyword matching, which limits the quality and stability of retrieved examples. To address these challenges, we propose HyRALLM, a hybrid retrieval-augmented large language model framework for code summarization. Specifically, we first map code and summary representations into a shared semantic space via cross-modal contrastive learning, constructing a dense retriever with stronger semantic alignment. We then integrate the dense retriever with a sparse retriever based on keyword matching to obtain high-quality, functionally relevant reference examples. During the generation stage, we further introduce a multi-candidate generation strategy and a post-processing discrimination mechanism, which guide the LLM to produce more accurate, concise, and semantically consistent summaries under the constraints of retrieved examples. Experimental results on two public benchmark datasets, JCSD and PCSD, demonstrate that HyRALLM consistently outperforms the compared baseline methods across multiple evaluation metrics, including BLEU, ROUGEL, METEOR, and CIDEr. Additional ablation studies and case analyses further verify the effectiveness of the hybrid retrieval strategy and generation optimization mechanisms in improving summary quality, reducing semantic deviation, and enhancing generation robustness.

---

## uid: `arxiv:2606.29406v1`

- title: Adaptive AI Delegation under Uncertainty: A Bayesian Governance Policy for Sequential Decision Authority
- authors: Matthew Francis Dixon
- affiliations: not stated
- posted: 2026-06-28
- source: arXiv
- link: https://arxiv.org/abs/2606.29406v1
- keyword hits: agentic, large language model, large language models, llm

### abstract

Organizations increasingly use large language models and agentic AI systems to generate probabilistic assessments and candidate actions in high-consequence settings. This creates a managerial problem distinct from prediction: how should organizations allocate decision authority to AI-generated recommendations as evidence quality, uncertainty, and organizational objectives evolve over time? Existing AI governance frameworks emphasize transparency, documentation, oversight, and regulatory compliance, but provide limited quantitative guidance for dynamically allocating decision authority under uncertainty. To address this challenge, we formulate adaptive AI delegation as a Governance-Aware Partially Observable Markov Decision Process (POMDP) in which Bayesian inference estimates the informational state and sequential optimization determines delegated AI authority. The paper also develops a quantitative validation and benchmarking framework for governance policies. Synthetic stress tests, reported LLM-confidence robustness, forecast-accuracy validation, governance-appetite sensitivity, and fragile-AI early-warning experiments evaluate whether the proposed policy exhibits graceful degradation, robustness to confidence-only perturbations, adaptive delegation under improving evidence quality, and interpretable calibration of institutional conservatism. The Governance-Aware POMDP is further benchmarked against five representative governance strategies operating under identical Bayesian beliefs, information, and governance objectives. The results show that while specialized heuristics perform well in stationary settings, sequential Bayesian governance provides the strongest general-purpose governance policy across heterogeneous AI-quality regimes by adaptively allocating organizational decision authority under uncertainty.

---

## uid: `doi:10.2139/ssrn.7022006`

- title: AlloyGraph: A Knowledge-Graph-Grounded Multi-Agent System for Nickel-Based Superalloy Design
- authors: Alexandru Lecu, Lezan Hawizy, Soran Birosca, Adrian Groza
- affiliations: not stated
- posted: 2026-06-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7022006
- keyword hits: gpt-4, llm, llms, retrieval-augmented

### abstract

Supporting design decisions in specialized scientific domains requires reasoning over sparse, fragmented data under strict physical constraints, conditions under which purely data-driven models and ungrounded language models are each insufficient. We introduce AlloyGraph, a knowledge-based system that integrates an OWL 2 DL ontology and RDF knowledge graph, physics-informed machine learning, and a multi-agent LLM orchestration layer that triangulates these evidence sources for property prediction, inverse design, and natural-language querying of nickel-based superalloys. It combines HermiT reasoning over the ontology, a vector database for hybrid retrieval, and a sequential Analyst–Reviewer pipeline that fuses ML predictions, physics estimates, and knowledge-graph data through confidence-weighted blending. Evaluated on 88 independent alloys spanning solid solution, precipitation hardened, and single crystal classes, the system achieves yield strength MAE of 80.6 MPa and UTS MAE of 95.2 MPa, outperforming both the ML-only baseline and a fine-tuned GPT-4.1-mini model on strength properties. A retrieval-augmented research assistant reaches 91\% accuracy on 250 factual questions versus approximately 50\% for ungrounded LLMs, and the inverse design pipeline produces metallurgically plausible compositions meeting 72\% of property targets with no critical TCP phase stability violations. Built entirely from open-access data and open-source software, AlloyGraph lowers barriers to reproducible, AI-guided materials design.

---

## uid: `arxiv:2606.31963v1`

- title: Signed-Permutation Coordinate Transport for RMSNorm Transformers
- authors: John Sweeney
- affiliations: not stated
- posted: 2026-06-30
- source: arXiv
- link: https://arxiv.org/abs/2606.31963v1
- keyword hits: fine-tuning, llama, llm, qwen

### abstract

Modern LLM workflows move coordinate-indexed objects across checkpoints: steering vectors, sparse autoencoders, top-$k$ neuron sets, attribution lists, and merge alignments. This is only well posed after fixing the model's residual-stream gauge, which we show is architecture-dependent: LayerNorm residual charts have permutation gauge $S_d$ (up to a global sign flip), while RMSNorm charts with generic per-channel gain have signed-permutation gauge $B_d = S_d \ltimes \{\pm 1\}^d$. Permutation-only alignment is therefore symmetry-incomplete for RMSNorm models. We introduce sign-marginalized Hungarian matching and prove a sharp failure mode: with decorrelated coordinates, raw signed-correlation matching has a structural permutation-accuracy ceiling at the positive-sign fraction of the true gauge, which sign-marginalization removes. We then make coordinate-preserving transport, not function-level merging, the primary object: composing saved-checkpoint local $B_d$ gauges along same-base fine-tuning trajectories recovers 91.1% of cross-run coordinates at 1500 steps versus 60.3% for endpoint matching, and the gain is not explained by merely routing through the base. The recovered gauge transfers tools that permutation-only alignment breaks: TinyLlama SAE reconstruction has NMSE 0.004 under $B_d$ versus 1.08 under $S_d$; Qwen sentiment steering preserves 95.8% of its effect versus 17.2%; refusal steering reverses sign under $S_d$; coordinate-preserving merges behave the same way. The same covariance governs stateful training: signed transport of AdamW state preserves the resumed trajectory, while permutation-only state follows a different one from a functionally identical checkpoint. Finally, gauge-sweep audits show index-level interpretability claims are reproducible only relative to an explicit gauge.

---

## uid: `arxiv:2606.31639v1`

- title: A Lifecycle and Application-Stack Survey of Large Language Model Vulnerabilities: Attacks, Risks, Defenses, and Open Problems
- authors: Seyed Bagher Hashemi Natanzi, Bo Tang
- affiliations: not stated
- posted: 2026-06-30
- source: arXiv
- link: https://arxiv.org/abs/2606.31639v1
- keyword hits: large language model, large language models, llm, prompting

### abstract

Large language models are no longer only text generators. They are increasingly embedded in retrieval pipelines, enterprise assistants, coding environments, robotic systems, security-operation workflows, and autonomous agents that can read private data, call tools, write files, execute code, and act across organizational boundaries. This shift changes the security problem: risks do not arise from the model weights alone, but from the full lifecycle and application stack through which data, prompts, model outputs, tools, memories, and user authority interact. This paper systematizes the literature on vulnerabilities in large language model systems through a lifecycle and application-stack lens. We organize attacks across eight stages: data collection, pretraining, post-training alignment, model packaging and supply chain, retrieval and memory, prompting and inference, tool/agent execution, and deployment/maintenance. For each stage, we analyze attacker capabilities, affected security objectives, representative attacks, practical risks, evaluation practices, and defenses. We further map LLM-specific vulnerabilities to confidentiality, integrity, availability, safety, privacy, fairness, accountability, and agency-control objectives. Unlike taxonomies that list isolated attack names, the proposed systematization emphasizes where trust boundaries fail, how untrusted data becomes executable instruction, how delegated authority amplifies model errors, and why point defenses rarely compose. We close with a research agenda for secure LLM systems, including compositional security, provenance-aware retrieval, tool-call containment, long-horizon agent evaluation, privacy-preserving adaptation, realistic red teaming, and deployment-grade incident response.

---

## uid: `arxiv:2607.01934v1`

- title: AIriskEval-edu: New Dataset for Risk Assessment in AI-mediated K-12 Educational Explanations
- authors: Javier Irigoyen, Roberto Daza, Francisco Jurado, Julian Fierrez, Ruben Tolosana, Alvaro Ortigosa, Enrique Blas, Aythami Morales
- affiliations: not stated
- posted: 2026-07-02
- source: arXiv
- link: https://arxiv.org/abs/2607.01934v1
- keyword hits: fine-tuning, llama, llm, llms

### abstract

This work introduces AIriskEval-edu-db2, a new dataset designed to train and evaluate auditors based on LLMs for an explainable pedagogical risk assessment in instructional content for grades K-12. The dataset comprises 1,639 explanations from 170 curated ScienceQA questions, covering science, language arts, and social sciences. For each question, the dataset includes an explanation written by a human teacher alongside 11 explanations generated by LLM-simulated teacher profiles associated with distinct pedagogical risks. We propose a comprehensive risk rubric aligned with established educational standards that covers five complementary dimensions: factual precision, depth and completeness, focus and relevance, student-level appropriateness, and ideological bias. A key contribution is the addition of 785 explanations with structured explainability annotations, including risk localization and risk description. The annotations are produced through a semi-automatic process with expert teacher validation. Finally, we present validation experiments comparing state-of-the-art proprietary models with a lightweight local Llama 3.1 8B model in both the pedagogical risk detection and the explainability assessment. These experiments evaluate whether supervised fine-tuning on AIriskEval-edu-db2 enables a locally deployable model to approach or outperform stronger frontier models while preserving privacy in educational auditing and assessment tasks.

---

## uid: `doi:10.2139/ssrn.7067665`

- title: Decision support in recirculating aquaculture systems (RAS): A case study of a human-AI interface in prawn hatchery operation
- authors: Shai  Avraham Shaked, Assaf Shechter, Amir Sagi
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7067665
- keyword hits: ai agent, large language model, llm, llms

### abstract

The need for sustainable and responsible production in aquaculture calls for innovative implementation of recirculating aquaculture systems (RAS), which are highly complex, requiring the integration of various fields of science and technology to reach the desired productivity. In this case study, we report a four-month observation using a large language model (LLM) that – collaboratively with human expertise – analyzed and resolved complex challenges in a Macrobrachium rosenbergii RAS hatchery. Unacceptable larval and post-larval mortality prompted the integration into hatchery management of an AI decision-support system as a strategic management partner, enabling exploration across chemical, biological, physical, engineering, and behavioral domains. Key interventions suggested by the AI agent included mineral balance recalibration, microbial load diagnostics, behavioral pattern decoding, and lighting and flow engineering. Outcomes were evaluated in terms of a reduction in larval mortality and improved rates of larval metamorphosis to post larvae. Central to the process was the presence of a guiding human entity, steering AI's analytical power through deliberate questioning and contextual framing. This case study suggests that AI could be instrumental in the improvement of any intensive aquaculture system. However, the tendency of AI agents to oversimplify complex systems requires the direction and guidance of a human expert to lead AI-human conversations. The adoption of LLMs in RAS-based aquaculture, bridging the gaps between raw data and actionable insights, has the potential to drive both the efficiency and the long-term sustainability of the aquaculture industry.

---

## uid: `doi:10.2139/ssrn.7067175`

- title: KGtelescope: Knowledge Graph Guided Model Routing for Factual Question Answering
- authors: Blerina Spahiu, Marco Maccarini, Anisa Rula, Matteo Palmonari
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7067175
- keyword hits: generative ai, llama, llm, llms, prompting

### abstract

Knowledge graphs (KGs) can serve generative AI not only as retrieved evidence, but also as an explicit decision layer for allocating model capacity. This paper asks whether KG-derived structural descriptors can guide routing from smaller to larger LLMs for factual question answering. We introduce KGtelescope, which constructs questions from typed KG relations and associates each with a structural profile covering relation pattern, query direction, support, entity prominence, and answer cardinality. Six Gemma and Llama models are evaluated on 131{,}616 DBpedia-derived questions under zero-shot and few-shot prompting, producing 1{,}579{,}392 responses. Factual accuracy varies strongly across KG-derived conditions. Query direction and answer cardinality have the largest effects; entity prominence (PageRank quartile) consistently predicts accuracy, with Q1 entities yielding up to 5.97 pp higher accuracy than Q3 across all 12 model configurations. For single-answer questions, the KG-informed routing policy significantly outperforms matched-budget random allocation ($\Delta = 5.26$ pp, $p

---
