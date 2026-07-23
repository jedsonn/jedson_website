# Classification batch 5 of 5, edition 1

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-001/batch-5.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7127378`

- title: Generative and Agentic AI Through the Lens of Model Risk Management: A Multisector Framework for Identifying Opportunities and Circumventing Risks
- authors: Advaith Nila Narayanan
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7127378
- keyword hits: agentic, generative artificial intelligence, llm, llms

### abstract

The rapid ascent of Generative Artificial Intelligence (GenAI) and its more autonomous successor, agentic AI, represents a watershed moment for organizations in virtually every sector, including healthcare, insurance, law, energy, and finance. For risk management professionals, these technologies are simultaneously the ultimate tool and the ultimate threat. We argue that while the non-deterministic nature and autonomy of these models introduce novel failure modes—such as hallucination, prompt injection, and execution drift, the core principles of model risk management (MRM), namely, Meaningful Challenge, Conceptual Soundness, and Ongoing Monitoring, remain the most robust defense. Although MRM matured as a formal discipline within quantitatively intensive industries, its principles are fundamentally sector-agnostic: any organization that uses a model to inform consequential decisions faces model risk and benefits from a disciplined framework for controlling it. This study provides a detailed account of what traditional MRM is, why it is needed, and how its components can be adapted, and offers a strategic roadmap for risk professionals in any industry to extend existing governance structures to the unique risks of LLMs and autonomous agents. We also discuss the critical question: What opportunities and risks do new technologies pose for risk professionals? using MRM principles as a foundational framework, appropriately adapted to the unique challenges posed by GenAI. We explore how the principles of meaningful challenge, conceptual soundness, and rigorous governance apply to non-deterministic, billion-parameter models, and we develop sector-specific analyses of GenAI model risk in healthcare, insurance, and legal services, together with an examination of numerical, computational, and energy-related risks unique to large-scale AI systems.

---

## uid: `doi:10.2139/ssrn.6097886`

- title: Representational and Behavioral Stability of Truth in Large Language Models
- authors: Samantha Dies, Courtney Maynard, Germans Savcisens, Tina Eliassi-Rad
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6097886
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

Large language models (LLMs) are increasingly used as information sources, yet small changes in semantic framing can destabilize their truth judgments. We propose P-StaT (Perturbation Stability of Truth), an evaluation framework for testing belief stability under controlled semantic perturbations in representational and behavioral settings via probing and zero-shot prompting. Across sixteen open-source LLMs and three domains, we compare perturbations involving epistemically familiar Neither statements drawn from well-known fictional contexts (Fictional) to those involving unfamiliar Neither statements not seen in training data (Synthetic). We find a consistent stability hierarchy: Synthetic content aligns closely with factual representations and induces the largest retractions of previously held beliefs, producing up to 32.7% retractions in representational evaluations and up to 36.3% in behavioral evaluations. By contrast, Fictional content is more representationally distinct and comparatively stable. Together, these results suggest that epistemic familiarity is a robust signal across instantiations of belief stability under semantic reframing, complementing accuracy-based factuality evaluation with a notion of epistemic robustness.

---

## uid: `doi:10.2139/ssrn.4675409`

- title: Generative AI and Simulation Modeling: How Should You (Not) Use Large Language Models Like ChatGPT
- authors: Ali Akhavan, Mohammad  S. Jalali
- affiliations: not stated
- posted: 2023-12-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.4675409
- keyword hits: chatgpt, generative ai, large language model, large language models

### abstract

interpolation of historical data

---

## uid: `doi:10.2139/ssrn.7162473`

- title: Augmenting Large Language Models with Climate Indicator Computation for Next-Generation Climate Services
- authors: Jacopo Grassi, Dmitrii Pantiukhin, Kuznetsov Ivan, Nikolay Koldunov, Massimo Dragan, Jost von Hardenberg
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7162473
- keyword hits: large language model, large language models, llm, llms

### abstract

Climate services aim to transform climate data and scientific knowledge into information that is usable, credible, and relevant for adaptation decision-making. Large Language Models (LLMs) offer new opportunities in this domain, as they can translate technical evidence into user-oriented explanations and contextualized narratives. However, standard LLMs cannot independently perform scientific computations, limiting their ability to generate tailored and quantitatively grounded outputs. Here, we examine how different forms of LLM augmentation affect the quality of AI-mediated climate information, with a specific focus on computational augmentation: the ability of an LLM-based system to compute climate indicators rather than only retrieve, summarize, or rephrase existing information. To this end, we develop XCLIM-AI, a proof-of-concept system that connects an LLM with xclim, an open-source framework for climate indicator computation. XCLIM-AI interprets user queries, selects and parameterizes relevant indicators, computes them from climate model data, and incorporates the resulting evidence into structured responses. We compare XCLIM-AI with a plain LLM, ClimSight, and a combined ClimSight-XCLIM system, representing different strategies for augmenting LLMs with climate information, contextual analysis, and scientific computation. Using both human expert assessment and LLM-as-a-judge evaluation, we score outputs across relevance, credibility, uncertainty communication, and actionability. Results show that augmentation generally improves relevance and actionability, while credibility depends on the type of augmentation. Systems including climate indicator computation achieve more consistent improvements in credibility and uncertainty communication than systems based primarily on expanded contextual information.

---

## uid: `doi:10.2139/ssrn.7167442`

- title: Enhancing New Product Recommendation in E-Commerce Platforms through Semantic Intelligence: An Integrated Approach Using Large Language Models and Graph Learning
- authors: Yen-Liang Chen, Hui-Chun Hung, Chu-Yun Chang
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7167442
- keyword hits: large language model, large language models, llm, llms

### abstract

The rapid introduction of new products on e-commerce platforms poses a significant challenge for recommender systems because newly listed items lack sufficient interaction histories and therefore cannot be effectively represented by conventional ID-based recommendation models. To address this problem, this study proposes an integrated semantic intelligence framework that combines large language models (LLMs) with graph learning to enhance new product recommendation. The proposed framework adopts a two-stage training strategy. In the first stage, an LLM extracts concise semantic anchors from product metadata, such as titles and descriptions information, to generate informative initial representations for new products. A hybrid item–item graph is then constructed by integrating behavioral transition edges with selectively injected semantic edges, enabling new products to connect with semantically relevant existing items despite the absence of historical interactions. Graph contrastive pre-training is further employed to align semantic representations with collaborative structural signals and to alleviate representation collapse. In the second stage, a dual-path preference aggregation mechanism dynamically integrates graph-based structural representations and LLM-derived semantic features. Masked mean pooling is subsequently applied to aggregate users’ historical preferences and generate personalized recommendation scores. Experiments conducted on the Amazon Reviews 2023 dataset demonstrate that the proposed framework substantially reduces isolated new-product nodes, maintains competitive recommendation accuracy for existing products, and consistently outperforms representative baselines in terms of HR, NDCG, and MRR for new-product recommendation. These findings indicate that integrating LLM-based semantic intelligence with graph learning provides an effective solution for bridging semantic product understanding and collaborative user behavior, thereby improving the visibility and recommendation quality of newly introduced products on e-commerce platforms.

---

## uid: `doi:10.2139/ssrn.7069438`

- title: Stereotypes in the Machine: Gender and Racial Bias in LLM-Generated Financial Advice
- authors: Ang Li, Fujing Xue, Zixuan Zeng, Xiaofeng Zhao
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7069438
- keyword hits: large language model, large language models, llm, llms

### abstract

We conduct a large-scale controlled experiment of large language models (LLMs) acting as financial advisors. We find that LLMs systematically recommend lower equity allocations to female and Asian clients compared to otherwise identical White males. This bias persists and even intensifies for financially sophisticated clients, and the recommended portfolios are less efficientrejecting rational statistical discrimination in favor of stereotyping. While higher model intelligence mitigates these biases, model scale, standard safety alignment, and explicit debiasing prompts prove ineffective. Our results suggest that without advanced reasoning capabilities, AI advisors risk institutionalizing wealth disparities by projecting demographic stereotypes onto investment decisions.

---

## uid: `doi:10.2139/ssrn.7152490`

- title: Explainable Risk Assessment and Intelligent Maintenance for Electrochemical Energy Storage System with Large Language Model
- authors: Yijie Wang, Yujie Fu, Yi Lu, Jingbo Qu, Putai Zhang, Mian Li
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7152490
- keyword hits: large language model, llm, llms, qwen

### abstract

With large-scale deployment of Electrochemical Energy Storage System (EESS), risk assessment plays a vital role in maintaining EESS safety. However, due to the variable operation conditions and complex structure of EESS, existing risk assessment methods cannot be objective and comprehensive enough to reflect real-time risk. Besides, assessment results are difficult to directly provide clear guidance to correct the identified risk, reducing the efficiency of EESS Operation and Maintenance (O&amp;M). With Large Language Model (LLM), this framework is proposed for EESS explainable risk assessment and intelligent maintenance. A hierarchical risk assessment is established based on real-time sensor data and expert opinions, providing an objective and comprehensive tool to reflect real-world operational risks in EESS. Furthermore, LLM is applied to bridge domain knowledge about EESS safety and hierarchical risk assessment, so that the proposed framework is able to explain why those risks are identified and how those risks propagate to further influence EESS safety by coupling relationship graph. Finally, the framework enables LLM to generate corresponding detailed suggestions for the guidance of EESS maintenance, improving the efficiency of EESS O&amp;M. The main contribution is to construct a comprehensive and explainable risk assessment for decision-making support, bridging the gap between risk assessment and practical EESS O&amp;M. Deployed in six in-service EESS stations, the proposed framework effectively identifies critical risk contributors in each station and has satisfactory performance in assessment explanation, generation of O&amp;M suggestions with advanced full-scale LLMs such as Kimi-K2.6, and understanding of domain knowledge with 7B/14B-scale fine-tuned LLMs such as Qwen3-8B.

---

## uid: `doi:10.2139/ssrn.6206500`

- title: From Humans to Algorithms: How Financial Advice Differs Across Professionals, Peers, and LLMs
- authors: Matthias Rumpf, Michael Haliassos, Tetyana Kosyakova, Thomas Otter
- affiliations: not stated
- posted: 2026-01-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6206500
- keyword hits: large language model, llm, llms

### abstract

This study compares belief-driven financial advice across professional advisors, financially literate peers, and a large language model using a vignette-based experiment. This eliminates matching problems and allows belief elicitation without incentive confounds. Repeated identical LLM prompts yield a variety of risky portfolio share recommendations, shown to result from changes in implicit rules. The resulting distribution is compared to those of professional and peer advice. A Bayesian hierarchical Tobit model captures observed and unobserved heterogeneity in recommendations. Professional and lay advisors respond to vignette characteristics consistently with theory but are influenced by their own risk preferences and characteristics. Professional advice differs from peer advice also in how it responds to client characteristics. The LLM produces advice with smaller variance but very sensitive to declared risk tolerance. Peers particularly discourage equity investment among younger, lower-income investors with limited access to professional advice, but use of AI can help mitigate or reverse this pattern.&amp;nbsp;

---
