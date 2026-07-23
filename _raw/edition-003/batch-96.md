# Classification batch 96 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-96.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6889905`

- title: Listening to the Workforce: Measuring Construction Worker Safety Attitudes from Social Media Discourse Using LLMs
- authors: Farouq Sammour, Yuxin Zhang, Zhenyu Zhang
- affiliations: not stated
- posted: 2026-06-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6889905
- keyword hits: large language model, llm, llms

### abstract

Worker safety attitudes are key determinants of whether protective practices are applied or bypassed on construction sites. Yet measuring them at scale has remained out of reach. Safety attitudes are multidimensional, vary across topics, and surface most candidly in workers' own conversations. This study created and validated the Construction Safety Attitude Framework (CSAF), which integrates two components: a theory-grounded structure that characterizes safety attitudes along eight dimensions, and an operational codebook for measuring them in worker naturalistic discourse. Applying CSAF to 250 posts and comments from the r/Construction community on Reddit, trained coders reached strong agreement (Krippendorff's α = 0.85). Pairwise lift and conditional probability confirmed that the eight dimensions are related yet distinct. To apply the framework across large volumes of discourse, CSAF was operationalized through a large language model (LLM) classifier. On 450 r/Construction contributions, the classifier reproduced expert human coding (Cohen's κ = 0.90, precision = 0.98, recall = 0.98), and on 400 contributions from r/Roofing it retained that accuracy after transfer to a different trade community (κ = 0.89, precision = 0.98, recall = 0.97). A proof-of-value case study then applied the validated classifier to 10,346 contributions from r/Roofing, demonstrating that CSAF can distinguish multidimensional attitudes by safety topic, track how they shift over time, and trace the reasoning behind unfavorable ones. The study therefore provides a theoretically grounded, empirically vetted instrument for examining safety attitudes, offering a basis for targeted interventions that address the attitudes underlying unsafe practices.

---

## uid: `arxiv:2606.08283v1`

- title: Macro Economists in the Machine: A Multi-Agent LLM Framework for Commodity-Related ETF Portfolio Construction
- authors: Yiqing Wang, Dehao Dai, Ding Ma, Kerui Geng
- affiliations: not stated
- posted: 2026-06-06
- source: arXiv
- link: https://arxiv.org/abs/2606.08283v1
- keyword hits: large language model, large language models, llm, llms

### abstract

We test whether large language models (LLMs) add value in commodity portfolio construction when the information set and implementation rules are held fixed across strategies. A Hawkish Agent (inflation-tightening prior), a Dovish Agent (growth-easing prior), a Debate Agent, and a deterministic z-score Rule Agent each receive identical FRED macro z-scores and route their tilt signals through the same portfolio engine. Across 124 weekly rebalancing dates spanning the 2023 U.S. rate peak and the 2024-2025 soft landing, all three LLM strategies outperform the Rule Agent in Sharpe terms; the Hawkish and Debate Agents record the largest gains (ΔSharpe = +0.044 and +0.040, both p < 0.10 under a block bootstrap) and preserve a net-of-cost advantage over the passive inverse-volatility benchmark at one-way trading costs up to 30 basis points, while the Rule Agent's thin margin over passive disappears at approximately 5 basis points.The Debate Agent does not outperform the best single agent (ΔSharpe = -0.004, p = 0.769); its contribution is bias correction -- averaging out the Dovish Agent's miscalibrated prior -- rather than deliberation-generated return. The performance advantage is concentrated in the soft-landing sub-period, the evaluation window spans a single rate cycle, and the reported $p$-values are unadjusted for multiple comparisons. Within these limits, the results suggest that an LLM acting as a constrained macro-interpretation function can add modest but economically meaningful value over a transparent rule layer, though the margin is small and its persistence beyond this sample is unknown.

---

## uid: `doi:10.2139/ssrn.6897784`

- title: Guideline-grounded Agentic AI Enables Reliable Report-level Diagnostic Reasoning in Oncologic Pathology
- authors: Xilin Shen, Rui Kong, Yong Wang, Yiping Xiang, Meilin Sun, Manlin Yang, Kexin Chen, Xiangchun Li
- affiliations: not stated
- posted: 2026-06-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6897784
- keyword hits: agentic, large language model, llm, retrieval-augmented

### abstract

Background: Accurate oncologic pathology diagnosis remains cognitively demanding, requiring synthesis of heterogeneous evidence within complex guidelines. Although artificial intelligence has shown promise in pathology, most existing systems are image-centric, whereas large language model (LLM)-based approaches for report-level diagnosis remain limited by hallucination, weak guideline grounding, and insufficient entity-level reasoning. Methods: We developed SAGE-Path (Self-reflective Agentic Guideline-grounded Engine for text-based pathology diagnostic assistance), a framework that integrates retrieval-augmented generation with iterative self-reflective reasoning. The system was grounded in a WHO-derived pathology knowledge base comprising 1,811 tumour entities organized into 48,396 retrievable text units. SAGE-Path was evaluated across multiple pathology tasks, including TNM staging, tumour regression grading, rare-tumour diagnosis, metastatic primary-site inference, and complex diagnostic reasoning. Performance was compared with LLM-only baselines and pathologists. Assisted-reader studies were conducted to assess clinical utility. Findings: SAGE-Path achieved 90.3% accuracy in TNM staging and 99.1% accuracy in tumour regression grading, surpassing junior and senior pathologists in these tasks. In rare-tumour diagnosis and metastatic primary-site inference, SAGE-Path improved diagnostic accuracy by approximately 5–6 percentage points compared with LLM-only baselines and reduced diagnostic errors by about 40%. Mechanistically, retrieval and reflection were complementary: together they eliminated correct-to-error transitions observed with reflection alone, producing evidence-grounded reasoning and actionable recommendations. In assisted-reader evaluations, SAGE-Path improved pathologist performance and reduced completion time. Interpretation: By combining authoritative guideline retrieval with structured self-reflective reasoning, SAGE-Path enables reliable and auditable report-level diagnostic reasoning in oncologic pathology. This framework extends computational pathology beyond image-centric analysis and provides a practical approach for supporting complex diagnostic decision-making in routine pathology practice.

---

## uid: `doi:10.2139/ssrn.6906932`

- title: Federated User Behavior Modeling for Privacy-Preserving LLM Recommendation
- authors: Hongyun Yang, Shicheng Wang, Xinhua Wang, Xinchang Zhang, Hui Liu, Lei Guo
- affiliations: not stated
- posted: 2026-06-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6906932
- keyword hits: large language model, large language models, llm, llms

### abstract

Large Language Models (LLMs) have shown great success in recommender systems. However, the limited and sparse nature of user data often restricts the LLM's ability to effectively model behavior patterns. To address this, existing studies have explored cross-domain solutions by conducting Cross-Domain Recommendation (CDR) tasks. But previous methods typically assume domains are overlapped and can be accessed readily. None of the LLM methods address the privacy-preserving issues in the CDR settings, that is, Privacy-Preserving Cross-Domain Recommendation (PPCDR). Conducting non-overlapping PPCDR with LLM is challenging since: 1) The inability to share user identity or behavioral data across domains impedes effective cross-domain alignment. 2) The heterogeneity of data modalities (e.g., textual vs. ID-based features) across domains complicates knowledge integration. 3) Fusing collaborative filtering signals from traditional recommendation models with LLMs is difficult, as they operate within distinct feature spaces. To address the above issues, we propose SF-UBM, a Semantic-enhanced Federated User Behavior Modeling method as our solution. Specifically, to deal with Challenge 1, we leverage natural language as a universal bridge to connect disjoint domains via a semantic-enhanced federated architecture. Here, text-based item representations are encrypted and shared, while user-specific data remains local. To handle Challenge 2, we design a Fact-counter Knowledge Distillation (FKD) module to integrate domain-agnostic knowledge with domain-specific knowledge, across different data modalities.To tackle Challenge 3, we project pre-learned user preferences and cross-domain item representations into the soft prompt space, aligning behavioral and semantic spaces for effective LLM learning. We conduct extensive experiments on three pairs of real-world domains, and the experimental results demonstrate the effectiveness of SF-UBM compared to the recent SOTA methods. Our code will be publicly available at: https://github.com/Nexus-Yang/SF-UBM\_master.

---

## uid: `doi:10.2139/ssrn.6906371`

- title: AI use in Swedish University Theses: a Corpus-Level Analysis of Bachelor and Master Theses, 2020--2025
- authors: Arend Hintze
- affiliations: not stated
- posted: 2026-06-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6906371
- keyword hits: chatgpt, generative ai, gpt-4, llm

### abstract

Surveys document widespread student use of generative AI, but corpus-level analysis of post-ChatGPT student thesis writing remains scarce. We analyse 17{,}007 Swedish bachelor and master theses from six universities across the ChatGPT release boundary (2020--2025), using OpenAI's \texttt{gpt-4o-mini} as a five-dimensional Likert rater, sentence-transformer paragraph-coherence statistics, and $K$-means abstract clustering into six topical groups. Four findings emerge. (i)~Grammar, vocabulary, academic quality, and wordiness all show statistically significant post-2022 distribution shifts (Cohen's $d \approx 0.3$); total-variation distance between pre- and post-period score distributions reaches approximately 13\%, providing a population upper bound on the affected post-period fraction. (ii)~The shift is present and significant in every cluster. (iii)~The disciplinary magnitude ranking is inverted relative to the published-research literature: Sustainability and Society theses show the largest shift, Informatics and Engineering the smallest. (iv)~The LLM rater's direct AI-likelihood judgment is structurally anti-correlated (Spearman $\rho \approx -0.25$; PC1 loading $\approx -0.4$) with its own language-quality judgments in both periods. The rater reads polished writing as \emph{less} likely to be AI, opposite to what the AI-text-detection literature predicts. AI-influenced writing is detectable in Swedish thesis prose across disciplines, but the LLM rater designed to detect it is structurally miscalibrated; analyses should use linguistic-symptom dimensions rather than the diagnostic dimension.

---

## uid: `doi:10.2139/ssrn.6906940`

- title: Beyond Conceptual Path Bias: A Unified Hierarchical Framework for Learning Path Recommendation in Online Educational Systems
- authors: Xiangyu Zeng, Guan Yuan, Guixian Zhang, Yanmei Zhang, Shang Liu
- affiliations: not stated
- posted: 2026-06-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6906940
- keyword hits: large language model, large language models, llm, llms

### abstract

Learning Path Recommendation (LPR) aims to generate personalized sequences of concepts and exercises that improve learner mastery in online educational systems. Since effective learning path recommendation depends on modeling prerequisite relations among concepts, existing methods usually infer knowledge structures from learner interaction logs and restrict recommendation to the current target concept. As a result, they may confound observed learning transitions with true prerequisite relations, leading to \textit{Conceptual Path Bias}, and may also cause prolonged stagnation when learners fail to progress on the current concept. To address these limitations, we propose \textbf{UniSys-LPR}, a framework for structure-aware and adaptively recoverable learning path recommendation. UniSys-LPR first constructs prerequisite and semantic similarity graphs with the assistance of Large Language Models (LLMs), and models directional dependencies using Directed Graph Neural Networks (DGCNs) to provide concept-level structural priors. It then tracks the evolution of learner proficiency with a bidirectional Mamba-based sequence encoder. Building on these components, we introduce a Dual-Pool Adaptive Selection (DPAS) mechanism that expands the candidate space from the current target concept to related concepts when progress stalls. In this way, UniSys-LPR couples concept planning and exercise recommendation through shared structural and learner-state representations, supporting both prerequisite-consistent progression and adaptive detours. Experiments on three real-world datasets show that UniSys-LPR consistently outperforms strong baselines in learning gain.

---

## uid: `doi:10.2139/ssrn.6885430`

- title: Large Language Model Use, Performance Anxiety, and Objective Medical Literature Retrieval Performance among Health Care Professionals: A Nationwide Cross-sectional Study
- authors: Xianya Huang, Zhizhuang Zhao, Jing Wang, Jingxuan Zhao, Junling Wu, Hanwen Zhang, Yi Chen, Linwei Zhang
- affiliations: not stated
- posted: 2026-06-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6885430
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are increasingly used for medical literature retrieval, but whether this use is associated with actual performance loss or altered self-perception remains unclear. This nationwide cross-sectional study surveyed 607 health care professionals and trainees from medical institutions, medical schools, and research institutes across 27 regions of China in October 2025. The survey assessed LLM use, attitudes toward artificial intelligence, perceived competence, and objective performance in medical literature retrieval and application. LLM use was highly prevalent: 582 participants (95.9%) had used LLMs for literature-related tasks, mainly retrieval, interpretation, and critical appraisal of scholarly medical literature. Participants reported moderate perceived capability degradation (median [interquartile range], 12 [10-15.25] of 30), but this perception was not associated with objective performance or AI dependency. Perceived degradation was associated with lower AI trust, lower satisfaction, and lower self-efficacy. Objective performance was independently associated with greater research experience, critical AI reflection, AI proficiency, and AI exposure. A dual-path model showed that critical AI reflection was linked to both higher objective performance and lower capability anxiety. These findings suggest that in LLM-assisted medical literature work, perceived competence and objective performance are dissociated. Concern about capability decline may reflect cognitive adaptation and reduced confidence rather than measurable skill loss, highlighting the need for medical AI training that strengthens verification, reflection, and independent literature appraisal.

---

## uid: `doi:10.2139/ssrn.6903678`

- title: Mapping Artificial Intelligence in Audit: A Pre-LLM / LLM-Era Taxonomy, the Practitioner–Academic Gap, and the Emerging Regulatory Layer
- authors: Natan Tzidkani
- affiliations: not stated
- posted: 2026-06-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6903678
- keyword hits: agentic, generative ai, llm, retrieval-augmented

### abstract

Generative AI's post-2023 inflection has produced a thirty-month gap between Big-4 production deployment and peer-reviewed coverage of those deployments. This paper develops a structural mapping of the AI-in-audit era that integrates three analytical axes: a pre-LLM versus LLM-era taxonomy of audit-AI application classes; a practitioner–academic gap analysis comparing what firms deploy with what the academic literature has studied; and a regulatory overlay across the EU AI Act (Regulation 2024/1689), the PCAOB July 2024 Spotlight, the NIST AI Risk Management Framework and its Generative AI Profile, and ISO/IEC 42001:2023. The three axes converge into a single ten-row mapping that combines application-class era, deployment maturity, academic-coverage depth, primary regulatory locus, and evidence-quality concern. Two findings carry the contribution. First, the maturity column inverts the academic-coverage column across the diagonal: where Big-4 deployment is most active — LLM-augmented working-paper drafting, retrieval-augmented generation over methodology corpora, multimodal evidence review, and agentic workflows — peer-reviewed evaluation is thinnest. Second, hallucination is best framed not as a generic AI-safety problem but as an ISA-500 structural failure: LLM-generated narrative satisfies relevance while undermining reliability, and the four horizontal regulatory frameworks under-cover the audit-specific evidence-quality dimension. A layered governance stack situates the analysis: ISO/IEC 42001 and NIST AI 100-1 supply an operating-system layer; ISO/IEC 42005:2025 and NIST AI 600-1 supply an application layer; runtime governance over generative-output reliability and agentic audit-trail integrity remains the third, not-yet-anchored, layer. The paper sits within Stratopoulos and Wang's (2025) AI-Centric / Traditional-Methods quadrant and offers a supplementation-not-revision standard-setting brief for ISA 500.

---
