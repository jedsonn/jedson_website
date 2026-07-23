# Classification batch 31 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-31.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6989056`

- title: Guideline-Bound or Case-Adaptive? A Guideline–Case Evidence-Balancing Framework for Clinical LLMs
- authors: Yuchen Pan, Haotian Tang, Zihan Wang, Benjamin Lev
- affiliations: not stated
- posted: 2026-06-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6989056
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

Clinical large language models (LLMs) are increasingly used to generate diagnostic and therapeutic recommendations, yet their decision knowledge is often difficult to govern. Clinical guidelines provide normative authority, standardization, and safety boundaries, whereas real-world cases capture contextual adaptation for patients with comorbidities, contraindications, and complex medication histories. This study examines how these knowledge sources can be positioned and fused for clinical decision support without reducing the system to either rigid guideline retrieval or unguided case imitation. We propose GCE-LLM, a Guideline–Case Evidence-Balancing framework for clinical LLMs in heart failure treatment decision support. The framework retains the technical strength of LLM-KG bidirectional augmentation: LLMs structure guideline knowledge into a computable clinical knowledge graph, and the graph together with a case base constrains downstream LLM generation. GCE-LLM builds a dual-source knowledge base from heart failure guidelines and 5,620 real-world patients in the HERO cohort, retrieves guideline and case evidence through hybrid semantic and keyword mechanisms, applies contraindication filtering and source-aware reranking, and generates structured treatment plans through clinically constrained prompting. We evaluated GCE-LLM against six baseline configurations using blind assessments by 50 cardiology experts, producing 2,800 expert-plan evaluations across simple and complex scenarios. GCE-LLM achieved the highest overall performance, with the clearest advantage in complex scenarios. The findings contribute to decision support systems research by showing how clinical LLMs can be designed as evidence-governed, case-adaptive, and auditable decision-support artifacts rather than as unconstrained generators.

---

## uid: `doi:10.2139/ssrn.6997075`

- title: THTB: A Cognitive-Difficulty-Aware Framework for Instruction Data Selection in Supervised Fine-Tuning of Large Language Models
- authors: Zhaoyang Shang, Sibo Wei, Jianbin Guo, Rui Zhou, Xiaobao Wang, Lifeng Dong, Yin Luo
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6997075
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

​Supervised fine-tuning (SFT) is a key step for adapting large language models (LLMs) to downstream applications, yet its effectiveness depends strongly on instruction data composition. Existing instruction data selection methods can reduce SFT data requirements, but the resulting subsets may still be less effective for downstream generalization; their criteria are often difficult to interpret or operationalize for instruction data construction; and many methods rely on black-box LLM scoring or model-dependent signals. To address these limitations, we propose THTB (The Harder The Better), a Bloom's Taxonomy-informed framework for SFT data selection and annotation guidance. THTB first filters low-quality instruction–response pairs and then ranks the remaining samples using intrinsic and extrinsic hardness. Intrinsic hardness characterizes cognitive demand and knowledge-integration requirement, while extrinsic hardness characterizes response-generation demand and distributional distinguishability within the candidate set. These explicit criteria make the selection process analyzable and provide operational guidance for domain-specific instruction data construction. Experiments on Alpaca show that THTB-selected 5% subsets achieve higher performance than full-data training and representative baselines, including AlpaGasus and IFD, on MMLU-Pro and Alpaca-Eval. Ablation results confirm the contribution of quality filtering, intrinsic hardness, and extrinsic hardness. Further validation on Magpie-Ultra-v0.1 shows that THTB remains effective on a high-quality corpus. In a Traditional Chinese Medicine application case study, a 200-sample instruction set constructed under THTB guidance outperforms a 10K-sample TCM baseline dataset. These results suggest that explicit cognitive-difficulty modeling can improve SFT efficiency with substantially fewer samples and support domain-specific instruction data construction.

---

## uid: `doi:10.2139/ssrn.7010050`

- title: Empirical Asset Pricing via Large Language Models
- authors: Anjana Yatawara
- affiliations: not stated
- posted: 2026-06-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7010050
- keyword hits: in-context learning, large language model, large language models, llm, llms

### abstract

We ask what the Gu, Kelly, and Xiu (2020) machine-learning asset-pricing framework reveals when its cross-sectional prediction function is replaced by a large language model (LLM). Holding their target, characteristics, preprocessing, and evaluation fixed, we present the whole monthly cross-section of stocks (each firm a row of characteristics ranked to [-1,1] and stripped of identity) to a panel of ten LLMs and read back one predicted next-month excess return per stock. Because an LLM that has read financial history can recall as easily as it can predict, we do not run a horse race; we make the LLM the object of measurement. On a memorization-clean post-cutoff window, zero-shot LLMs recover cross-sectional predictability: the strongest attains an out-of-sample R-squared of 0.75% and a rank information coefficient of 0.056 (t=2.9), leading a re-estimated machine-learning zoo on rank-IC and decile long-short Sharpe ratios. Mechanically, the LLM is a heavily shrunk ranker and a static factor tilt: a single fixed, momentum-aligned tilt explains 80-98% of its month-to-month rank skill, with no conditional skill beyond it. In-context learning breaks calibration rather than improving direction, capability buys calibration not cross-sectional skill, and a four-pronged audit shows the recovered skill is not memorization. Dropped into the Gu-Kelly-Xiu pipeline, an off-the-shelf LLM is a competent but radically over-shrunk cross-sectional ranker whose skill is a static, regime-contingent factor tilt.

---

## uid: `arxiv:2606.29251v2`

- title: When Summaries Distort Decisions: Information Fidelity in LLM-Compressed Financial Analysis
- authors: Hoyoung Lee, Suhwan Park, Seunghan Lee, Jun Seo, Jaehoon Lee, Sungdong Yoo, Minjae Kim, CheolWon Na
- affiliations: not stated
- posted: 2026-06-28
- source: arXiv
- link: https://arxiv.org/abs/2606.29251v2
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Financial decision-makers face more information than they can directly inspect, making context compression necessary. Yet when large language models (LLMs) compress financial source material, they can alter the investment judgment supported by the original source. We frame this problem as information fidelity: compression loses fidelity when it changes the decision induced by the source. In agentic systems, such losses may recur across intermediate steps and amplify throughout the decision process. Across financial filings and earnings-call transcripts, we find that LLM-based compression can produce fluent and factually plausible compressed contexts that nevertheless alter downstream decisions. We analyze two diagnostic patterns associated with fidelity loss: decontextualization, where salient evidence is retained but separated from the caveats and contextual qualifiers needed for correct interpretation, and model dependency, where different compressors expose different views of the same source. We then propose Agentic Context Compression, which generates multiple candidate compressions and audits their disagreements against the original source. Our results suggest that financial compression should be evaluated not only by efficiency or factuality, but also by its ability to preserve decision-relevant context.

---

## uid: `doi:10.2139/ssrn.7017518`

- title: A Practitioner's Guide to Using Large Language Models and Generative AI in Economic History
- authors: Andreas Ferrara
- affiliations: not stated
- posted: 2026-06-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7017518
- keyword hits: agentic, generative ai, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are lowering the entry barriers to working with exciting data sources that used to require strong data science skills, such as handwritten ledgers, text, images, or sound recordings. This guide provides an introduction for researchers who are new to LLMs. It sets out a step-by-step workflow for turning a research idea into working code and data, and describes the four main ways of interacting with an LLM: the chat window, editor-integrated assistants, agentic coding tools, and the API. It then works through the decisions a practitioner meets in sequence, beginning with whether an LLM is the right tool and whether the data are allowed to be sent to one, then how to select models, write prompts, manage context limits, and control costs, and finally how to validate, reproduce, document, and correct LLM-generated measures in regression settings. A review of recent research shows how these tools already extract, link, harmonize, and classify historical data at scale. Four worked examples with replication files illustrate the use of LLMs. They classify emotions in paintings, link census records without names, measure newspaper salience and sentiment around the 1882 Chinese Exclusion Act, and score the emotional delivery of Franklin D. Roosevelt's wartime speeches. The guide also condenses the workflow, the best-practice recommendations, and the preparation of replication packages into summary tables and checklists to aid applied economists. Institutional subscribers to the NBER working paper series, and residents of developing countries may download this paper without additional charge at www.nber.org .

---

## uid: `doi:10.2139/ssrn.6970459`

- title: Structuring Human Objectives: A Survey of Rubrics for Evaluation, Alignment, and Agentic AI
- authors: Hongru Xiao, Jie Li, Zhirui Li, XIang Li, Sunzhu Li, Jiale Han
- affiliations: not stated
- posted: 2026-06-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6970459
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

As large language models (LLMs) move beyond answer generation toward agentic tasks, evaluation increasingly requires more than final correctness or preference. Models are expected to plan, reason, interact, use tools, and act over multiple steps. However, conventional evaluation signals often compress these requirements into coarse outcomes. They can indicate whether an output is correct or preferred, but provide limited insight into which criteria are satisfied, which constraints are violated, or where failures arise. To address this gap, rubrics have emerged as a critical interface for structured evaluation and alignment. They translate human objectives into criterion-level judgments that can be inspected, reused, aggregated, and converted into feedback or rewards. This paper provides a comprehensive survey of rubrics for LLM evaluation and post-training. We organize the literature through a lifecycle taxonomy covering rubric construction, training integration, inference enhancement, reward hacking risks, evaluation mechanisms, and applications. Furthermore, we discuss how rubrics support scalable evaluation, reward modeling, judge calibration, and alignment, and highlight key challenges and future directions. Together, this work establishes a roadmap for developing more reliable, interpretable, and aligned agentic AI systems.

---

## uid: `doi:10.3386/w35374`

- title: A Practitioner's Guide to Using Large Language Models and Generative AI in Economic History
- authors: Andreas Ferrara
- affiliations: not stated
- posted: 2026-06-30
- source: NBER
- link: https://doi.org/10.3386/w35374
- keyword hits: agentic, generative ai, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are lowering the entry barriers to working with exciting data sources that used to require strong data science skills, such as handwritten ledgers, text, images, or sound recordings.This guide provides an introduction for researchers who are new to LLMs.It sets out a step-by-step workflow for turning a research idea into working code and data, and describes the four main ways of interacting with an LLM: the chat window, editor-integrated assistants, agentic coding tools, and the API.It then works through the decisions a practitioner meets in sequence, beginning with whether an LLM is the right tool and whether the data are allowed to be sent to one, then how to select models, write prompts, manage context limits, and control costs, and finally how to validate, reproduce, document, and correct LLM-generated measures in regression settings.A review of recent research shows how these tools already extract, link, harmonize, and classify historical data at scale.Four worked examples with replication files illustrate the use of LLMs.They classify emotions in paintings, link census records without names, measure newspaper salience and sentiment around the 1882 Chinese Exclusion Act, and score the emotional delivery of Franklin D. Roosevelt's wartime speeches.The guide also condenses the workflow, the bestpractice recommendations, and the preparation of replication packages into summary tables and checklists to aid applied economists.

---

## uid: `doi:10.2139/ssrn.7032069`

- title: Generating Symbolic Chain-of-Thoughts from Knowledge Graphs to Fine-Tune Language Models for Dataset Metadata Extraction in Scientific Publications
- authors: Yashrajsinh Chudasama, Disha Purohit, Enrique Iglesias, Ahmad Sakor, Maria-Esther Vidal
- affiliations: not stated
- posted: 2026-07-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7032069
- keyword hits: chain-of-thought, large language model, large language models, llm, llms

### abstract

Scientific progress increasingly depends on the ability to discover, understand, and reuse datasets described in scientific publications. However, dataset metadata is often embedded in unstructured text, making dataset discovery, benchmarking, and reuse labor-intensive. Although large language models (LLMs) have shown promise for metadata extraction, they primarily rely on textual evidence and frequently produce incomplete or inconsistent descriptions that are difficult to align with semantic standards and knowledge-driven discovery systems. This paper addresses the problem of extracting dataset metadata from scientific publications in a semantically grounded and interpretable manner. Given a corpus of research papers and a metadata vocabulary, the objective is to automatically identify datasets, determine the scientific tasks for which they are used, and generate structured metadata describing task–dataset relationships as standards-compliant RDF aligned with the DCAT vocabulary. We present METAMINE, a neuro-symbolic framework that integrates knowledge extraction, knowledge graph (KG) construction, semantic reasoning, and LLM adaptation. Relations among scientific tasks, datasets, methods, and publications are extracted from research papers to construct a KG. Semantic traversal algorithms identify high-confidence multi-hop paths connecting tasks and datasets, which are then transformed into symbolic Chain-of-Thoughts (CoTs) that provide explicit reasoning traces. These KG-derived CoTs are used to fine-tune an LLM, aligning neural reasoning with the relational structure encoded in the KG. By combining symbolic reasoning with neural language models, METAMINE generates semantically grounded metadata together with transparent explanations that justify dataset–task associations. The resulting metadata supports interoperability, semantic querying, FAIR dataset descriptions, and more effective dataset discovery, benchmarking, and scientific knowledge management.

---
