# Classification batch 116 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-116.answer.json` as a JSON array.

---

## uid: `arxiv:2607.19259v1`

- title: Benchmarking Generalization in Financial Statement Fraud Detection: robust evaluation and novel tasks
- authors: Guy Stephane Waffo Dzuyo, Gaël Guibon, Christophe Cerisara, Luis Belmar-Letelier
- affiliations: not stated
- posted: 2026-07-21
- source: arXiv
- link: https://arxiv.org/abs/2607.19259v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Financial statement fraud detection (FSFD) is crucial for market integrity but faces challenges from increasingly sophisticated schemes and under-utilized textual data in financial reports. Existing methods often rely on random data splits, leading to overoptimistic performance estimates that do not reflect real-world generalization to new companies or future periods. To address this recurring problem with the state of the art, we propose a robust FSFD framework leveraging Large Language Models (LLMs) to integrate both structured financial data and unstructured textual information from financial reports. We provide a more realistic evaluation through a novel and challenging benchmark task called Company-Isolated FSFD (CI-FSFD). We construct and make publicly available a comprehensive U.S. company dataset combining financial statements, summarized MD&A text, and fraud labels. Our approach achieves the best performance on the challenging CI-FSFD task, demonstrating the critical value of textual data and robust evaluation for reliable financial fraud detection.

---

## uid: `doi:10.2139/ssrn.7162473`

- title: Augmenting Large Language Models with Climate Indicator Computation for Next-Generation Climate Services
- authors: Jacopo Grassi, Dmitrii Pantiukhin, Kuznetsov Ivan, Nikolay Koldunov, Massimo Dragan, Jost von Hardenberg
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7162473
- keyword hits: large language model, large language models, llm, llms

### abstract

Climate services aim to transform climate data and scientific knowledge into information that is usable, credible, and relevant for adaptation decision-making. Large Language Models (LLMs) offer new opportunities in this domain, as they can translate technical evidence into user-oriented explanations and contextualized narratives. However, standard LLMs cannot independently perform scientific computations, limiting their ability to generate tailored and quantitatively grounded outputs. Here, we examine how different forms of LLM augmentation affect the quality of AI-mediated climate information, with a specific focus on computational augmentation: the ability of an LLM-based system to compute climate indicators rather than only retrieve, summarize, or rephrase existing information. To this end, we develop XCLIM-AI, a proof-of-concept system that connects an LLM with xclim, an open-source framework for climate indicator computation. XCLIM-AI interprets user queries, selects and parameterizes relevant indicators, computes them from climate model data, and incorporates the resulting evidence into structured responses. We compare XCLIM-AI with a plain LLM, ClimSight, and a combined ClimSight-XCLIM system, representing different strategies for augmenting LLMs with climate information, contextual analysis, and scientific computation. Using both human expert assessment and LLM-as-a-judge evaluation, we score outputs across relevance, credibility, uncertainty communication, and actionability. Results show that augmentation generally improves relevance and actionability, while credibility depends on the type of augmentation. Systems including climate indicator computation achieve more consistent improvements in credibility and uncertainty communication than systems based primarily on expanded contextual information.

---

## uid: `doi:10.2139/ssrn.7160538`

- title: The Double-Edged Sword of AI Hallucinations: Experimental Evidence on Creativity Across Idea Generation and Refinement
- authors: Li Fanshu, Siddharth Bhattacharya, Bowen Lou
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7160538
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are increasingly used to support creative work, yet little empirical evidence exists regarding how AI hallucinations influence creativity. Prior research has largely treated hallucinations as errors that undermine accuracy and reliability, leaving their role in creative tasks underexplored. In this study, we conduct an experiment in which participants use LLM assistance to generate, select, and refine product ideas based on real-world patents under varying levels of AI hallucination. Our findings reveal that the creative consequences of AI hallucinations depend on both hallucination severity and the stage of the creative process. During idea generation (divergent thinking), moderate and high levels of hallucination enhance originality, diversity, and elaboration, whereas during idea refinement (convergent thinking), higher levels of hallucination improve originality but come at the expense of feasibility. We further identify AI hallucination-induced recombinant search as a key mechanism through which AI hallucinations enhance creativity, whereby hallucinated AI outputs enable the discovery and recombination of previously disconnected knowledge elements, providing empirical support for the creative potential of AI hallucinations. Overall, this study provides one of the first empirical investigations of the creative consequences of AI hallucinations, offering a more nuanced understanding of hallucinations as barriers and enablers of creativity. More broadly, our findings suggest that the value of AI hallucinations depends on the cognitive demands of the creative process and provide practical insights for designing more effective human-AI creative workflows.

---

## uid: `arxiv:2607.19794v1`

- title: TriAgent: Divergence-Aware Multi-Agent Committees for Cost-Efficient Financial Sentiment Analysis
- authors: Isabel Xu, Cynthia Xu, Rachel Ren, Cong Guo, Jiacheng Ding
- affiliations: not stated
- posted: 2026-07-22
- source: arXiv
- link: https://arxiv.org/abs/2607.19794v1
- keyword hits: gpt-4, llm, mistral, qwen

### abstract

Production LLM-based financial sentiment analysis faces a structural cost trap: most queries are trivially classifiable, yet expensive cloud reasoners process them all, and the bill scales linearly with user count. We present TriAgent, a multi-agent committee stratified by contextual granularity -- a word-level lexicon (VADER), a sentence-level domain transformer (FinBERT), and a cross-sentence reasoner (Qwen2.5, 0.5B-14B-4bit, with Mistral-7B and Phi-3.5-mini cross-family checks). A three-way Semantic Divergence Index (SDI) measures pairwise disagreement across granularities and routes each query accordingly. Our central finding is the critic plateau: when the LLM is re-tasked as a critic over the smaller agents' outputs, F1 plateaus at ~0.87 across 1.5B-7B Qwen (bootstrap 95% CIs overlap), while a same-size 3-persona vote drops to F1=0.66, which is driven by granularity-stratified diversity. Three corollaries follow from the same SDI signal: (i) a Shared Consensus Dictionary on multilingual sentence-BERT answers 95% of Chinese queries from an English cache at F1=0.99 -- cross-border canonicalization at zero marginal cost; (ii) SDI doubles as a post-hoc LLM-hallucination detector at AUC=0.90; (iii) the SDI single-stage strategy attains the best risk-adjusted return (Sharpe=3.50) on a 20-ticker back-test, dominating both always-FinBERT (1.36) and always-LLM (0.11). At 10M-user scale, TriAgent saves $9.3M/year vs. a GPT-4o-mini baseline. Code, lexicons, and the SCD are released.

---

## uid: `doi:10.2139/ssrn.7167442`

- title: Enhancing New Product Recommendation in E-Commerce Platforms through Semantic Intelligence: An Integrated Approach Using Large Language Models and Graph Learning
- authors: Yen-Liang Chen, Hui-Chun Hung, Chu-Yun Chang
- affiliations: not stated
- posted: 2026-07-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7167442
- keyword hits: large language model, large language models, llm, llms

### abstract

The rapid introduction of new products on e-commerce platforms poses a significant challenge for recommender systems because newly listed items lack sufficient interaction histories and therefore cannot be effectively represented by conventional ID-based recommendation models. To address this problem, this study proposes an integrated semantic intelligence framework that combines large language models (LLMs) with graph learning to enhance new product recommendation. The proposed framework adopts a two-stage training strategy. In the first stage, an LLM extracts concise semantic anchors from product metadata, such as titles and descriptions information, to generate informative initial representations for new products. A hybrid item–item graph is then constructed by integrating behavioral transition edges with selectively injected semantic edges, enabling new products to connect with semantically relevant existing items despite the absence of historical interactions. Graph contrastive pre-training is further employed to align semantic representations with collaborative structural signals and to alleviate representation collapse. In the second stage, a dual-path preference aggregation mechanism dynamically integrates graph-based structural representations and LLM-derived semantic features. Masked mean pooling is subsequently applied to aggregate users’ historical preferences and generate personalized recommendation scores. Experiments conducted on the Amazon Reviews 2023 dataset demonstrate that the proposed framework substantially reduces isolated new-product nodes, maintains competitive recommendation accuracy for existing products, and consistently outperforms representative baselines in terms of HR, NDCG, and MRR for new-product recommendation. These findings indicate that integrating LLM-based semantic intelligence with graph learning provides an effective solution for bridging semantic product understanding and collaborative user behavior, thereby improving the visibility and recommendation quality of newly introduced products on e-commerce platforms.

---

## uid: `doi:10.2139/ssrn.7046318`

- title: Transformative Use, the Black Box Problem, and the Unfinished Architecture of AI Copyright Law
- authors: Akshit Mathur
- affiliations: not stated
- posted: 2026-07-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7046318
- keyword hits: generative ai, large language model, large language models

### abstract

The doctrine of transformative fair use has served as copyright law's principal mechanism for accommodating technological change. From the photocopier to the internet, courts have repeatedly held that repurposing copyrighted material for a fundamentally different function can excuse what would otherwise constitute infringement. Authors Guild, Inc. v. Google Inc. (2d Cir. 2015) represented the high-water mark of this approach: mass digitization of millions of books was deemed transformative because courts could inspect, measure, and verify the scope of Google's use through its snippet-display interface. A decade later, Bartz v. Anthropic PBC (N.D. Cal. 2025) asked whether the same logic could extend to large language models trained on millions of copyrighted works-and the answer revealed a doctrinal fault line that Authors Guild had papered over. This article argues that the two cases, read together, expose a structural vulnerability in the fair use framework: the doctrine can only function as intended when courts can empirically verify that a claimed transformation is genuine rather than merely asserted. In the age of opaque generative AI, that verification has become impossible. The article proceeds in three parts. Part I analyses the Authors Guild precedent and argues that its reasoning rested, implicitly, on the inspectability of Google's use. Part II examines how Bartz both extended and strained that precedent, with particular attention to the 'black box problem'-the inability of courts, authors, or even developers to trace how copyrighted material shapes model behaviour. Part III proposes a governance framework centred on mandatory dataset disclosure, third-party auditing, and collective licensing, arguing that these mechanisms are not merely desirable policy supplements but necessary prerequisites for the fair use doctrine to operate coherently in the context of generative AI.

---

## uid: `doi:10.2139/ssrn.7167441`

- title: Enhancing New Product Recommendation in E-Commerce Platforms through Semantic Intelligence: An Integrated Approach Using Large Language Models and Graph Learning
- authors: Yen-Liang Chen, Hui-Chun Hung, Chu-Yun Chang
- affiliations: not stated
- posted: 2026-07-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7167441
- keyword hits: large language model, large language models, llm, llms

### abstract

The rapid introduction of new products on e-commerce platforms poses a significant challenge for recommender systems because newly listed items lack sufficient interaction histories and therefore cannot be effectively represented by conventional ID-based recommendation models. To address this problem, this study proposes an integrated semantic intelligence framework that combines large language models (LLMs) with graph learning to enhance new product recommendation. The proposed framework adopts a two-stage training strategy. In the first stage, an LLM extracts concise semantic anchors from product metadata, such as titles and descriptions information, to generate informative initial representations for new products. A hybrid item–item graph is then constructed by integrating behavioral transition edges with selectively injected semantic edges, enabling new products to connect with semantically relevant existing items despite the absence of historical interactions. Graph contrastive pre-training is further employed to align semantic representations with collaborative structural signals and to alleviate representation collapse. In the second stage, a dual-path preference aggregation mechanism dynamically integrates graph-based structural representations and LLM-derived semantic features. Masked mean pooling is subsequently applied to aggregate users’ historical preferences and generate personalized recommendation scores. Experiments conducted on the Amazon Reviews 2023 dataset demonstrate that the proposed framework substantially reduces isolated new-product nodes, maintains competitive recommendation accuracy for existing products, and consistently outperforms representative baselines in terms of HR, NDCG, and MRR for new-product recommendation. These findings indicate that integrating LLM-based semantic intelligence with graph learning provides an effective solution for bridging semantic product understanding and collaborative user behavior, thereby improving the visibility and recommendation quality of newly introduced products on e-commerce platforms.

---

## uid: `doi:10.2139/ssrn.6168735`

- title: The Efficiency Paradox in Agentic AI Workflows: When Optimization Increases the Electricity Bill
- authors: Joren Gijsbrechts, Willem van Jaarsveld
- affiliations: not stated
- posted: 2026-03-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6168735
- keyword hits: agentic, large language model, llm

### abstract

Problem definition: Firms deploying agentic AI workflows at scale face fundamental trade-offs between cost, speed, and quality of Large Language Model (LLM) calls. While individual queries are inexpensive, the cumulative cost of automated workflows quickly becomes substantial. Organizations can optimize LLM usage through two approaches: internal optimization (aggregating tasks and caching instructions to reduce computational costs) or external optimization (providing time flexibility to providers who offer substantial price discounts in exchange for processing delays). Methodology/results: We characterize the optimal strategy based on workload intensity and delay sensitivity, revealing clear decision rules for when each approach dominates. Including model selection uncovers an efficiency paradox: when firms can jointly optimize workflow strategies and model capability, cost and energy savings are offset-and can be more than offset-by selection of more capable, energy-intensive models, so that increased operational flexibility leads to higher energy consumption. Managerial implications: Operational optimization alone cannot deliver environmental benefits when model choice is endogenous. Efficiency improvements are neutralized by capability upgrades that consume the same total resources or more, so efficiency strategies may not reduce the electricity bill when firms can select model capability.

---
