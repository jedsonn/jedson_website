# Classification batch 110 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-110.answer.json` as a JSON array.

---

## uid: `arxiv:2607.11920v1`

- title: Sensitivity to Subjective Expected Utility Maximization: A Methodological Study, with an Illustrative Application to LLM Decision-Making
- authors: Jeff Helzner
- affiliations: not stated
- posted: 2026-07-08
- source: arXiv
- link: https://arxiv.org/abs/2607.11920v1
- keyword hits: claude, gpt-4, llm

### abstract

Evaluating decisions made under uncertainty is hard when labeled outcomes are scarce, costly, or confounded with luck. We treat subjective expected utility (SEU) maximization as a stated standard and define a graded measure -- SEU sensitivity -- of an agent's conformity to it. The vehicle is a softmax choice model with a sensitivity parameter $α$ on SEU-valued alternatives; the contribution is a sequence of identifiability results for $α$ and for belief and utility parameters $(β, δ)$, validated in Stan via prior predictive checks, parameter recovery, and simulation-based calibration (SBC), with finite-sample caveats intact. In the uncertain-choice-only model $m_0$, $α$ is identifiable given the expected-utility vector $η$ and sharply recovered, while $(β, δ)$ are only weakly informed: the posterior barely contracts and concentrates on a $β$-$δ$ trade-off. In the extended model $m_1$, $δ$ becomes identifiable in principle via a $β$-free risky block, but its practical recovery gain at realistic sample sizes is negligible (matched-count CI-width reduction under 1%), and that block yields no detected $α$-precision gain at matched choice count. These are two distinct phenomena: for $δ$, identifiability does not imply precise estimability at realistic $n$; for $α$, identifiability is silent about what governs finite-$n$ precision. Marginal SBC passes for both models even where the joint posterior is weakly informed -- a demarcation we make precise. A two-by-two application (GPT-4o and Claude 3.5 Sonnet, each on insurance-claims triage and Ellsberg-style urns, with sampling temperature as the lever) runs end-to-end on real LLM choice data, detecting a structured comparative $α$ effect in two of four cells.

---

## uid: `arxiv:2607.07891v1`

- title: How Do I Know What to Say Next? Barenholtz's Autogenerative Theory as an Enrichment of Harrisean Integrationism
- authors: J. Mark Bishop, Stephen J. Cowley
- affiliations: not stated
- posted: 2026-07-08
- source: arXiv
- link: https://arxiv.org/abs/2607.07891v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Roy Harris's Integrationist linguistics offers a compelling critique of the referentialist tradition embedded deep at the heart of computational approaches to language, arguing that language is not a code that maps onto a pre-given world but a situated, bipartite activity oriented toward prospective joint action. Yet Integrationism leaves certain explanatory gaps: it does not fully account for the structural mechanism by which signs sustain prospective openness, it undertheorises the continuity between linguistic and non-linguistic semiotic activity, and it offers no detailed account of the structural properties of the accumulated archive of past integrations. This paper argues that Elan Barenholtz's autogenerative theory of language, developed in response to the behaviour of Large Language Models (LLMs), can fill precisely these gaps, enriching Integrationism without undermining any of its core commitments. Specifically, the autogenerative account provides: a structural mechanism for the prospective openness that Harris identifies as central to bipartite communication; a computational correlate for Harris's thesis of semiotic continuity between language and other sign-making activity; and a theory of the archive: what the accumulated residue of past integrations looks like and how new participants draw upon it. The synthesis preserves Harris's ontological primacy of the situated integrative act while adding explanatory content that Integrationism itself does not supply. For practitioners and researchers in natural language processing and large language model design, the argument offers a principled account of what the statistical structure that LLMs so effectively exploit actually is, and of what it cannot, by its nature, provide.

---

## uid: `arxiv:2607.09790v1`

- title: Semantic Drift and the Stability of Operator Control in Reasoning-Class Decision Support Systems
- authors: M. L. Kaluzhsky, V. A. Efirov
- affiliations: not stated
- posted: 2026-07-08
- source: arXiv
- link: https://arxiv.org/abs/2607.09790v1
- keyword hits: large language model, large language models, llm, llms

### abstract

The article investigates the fundamental problem of ensuring the stability of operator control and preserving goal-targeting in hybrid human-machine decision support systems (DSS) of a new generation. Based on a two-month continuous longitudinal experiment on the joint design of a monograph-format textual array, the latent phenomenon of semantic context drift in large language models of deep logical reasoning (Reasoning LLMs) is verified and described. A mathematical model of interaction in the human-machine interface is proposed, and an original metric is introduced - the operator control stability coefficient, which takes into account the non-linear contextual pressure of hidden reasoning chains. Within the paradigm of the cognitome theory, a critical point of control functions inversion is captured. Engineering recommendations are formulated for implementing dynamic relational arbitration loops based on a modified hierarchical similarity model.

---

## uid: `doi:10.2139/ssrn.7086750`

- title: FedLLM: A Privacy-Preserving Federated Large Language Model for Explainable Traffic Flow Prediction
- authors: Seerat Kaur, Sukhjit  Singh Sehra, Dariush Embrahimi
- affiliations: not stated
- posted: 2026-07-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7086750
- keyword hits: large language model, llm, llms

### abstract

Traffic prediction plays a central role in intelligent transportation systems (ITS) by supporting real-time decision-making, congestion management, and long-term planning. However, many existing approaches face several practical limitations. Most spatio-temporal models are trained in centralized settings, rely on numerical representations, and offer limited explainability. Recent Large Language Model (LLM) based methods improve reasoning capabilities, but typically assume centralized data availability and do not fully capture the distributed and heterogeneous nature of real-world traffic systems. To address these challenges, this study proposes FedLLM, a privacy-preserving and distributed framework for explainable multi-horizon short-term traffic flow prediction (15-60 minutes ahead). The framework introduces four key contributions (1) a Composite Selection Score (CSS) for data-driven freeway selection that captures structural diversity across traffic regions (2) a domain-adapted LLM fine-tuned on structured traffic prompts encoding spatial, temporal, and statistical context (3) an integrated federated learning (FL) and LLM framework that enables collaborative training across heterogeneous clients while exchanging only lightweight LoRA adapter parameters and (4) a structured prompt representation that supports contextual reasoning and cross-region generalization. The FedLLM design allows each client to learn from local traffic patterns while contributing to a shared global model through efficient parameter exchange, reducing communication overhead and keeping data private. This setup supports learning under non-IID traffic distributions. Experimental results show that FedLLM achieves improved predictive performance over centralized baselines, while producing structured and explainable outputs. These findings highlight the potential of combining FL with domain-adapted LLMs for scalable, privacy-aware, and explainable traffic prediction.

---

## uid: `doi:10.2139/ssrn.7084500`

- title: Does Linguistic Structure Help with Grammar Learning? Evaluating Neurosymbolic Baby Language Modeling on Linguistic Minimal Pairs
- authors: Serena Auriemma, Martina Miliani, Jakob Prange, Emmanuele Chersoni, Alessandro Lenci
- affiliations: not stated
- posted: 2026-07-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7084500
- keyword hits: large language model, large language models, llm, llms

### abstract

Is linguistic structure necessary for mastering natural language? For a long time, this might have sounded like a rhetorical question in linguistics, but the high level of proficiency reached by the state-of-the-art Large Language Models (LLMs), which they achieve after training on huge amounts of raw text, is casting doubts on the necessity of structure-dependent biases forlanguage learning.In our work, we test whether providing structural guidance to LLMs during the training phase is really superfluous or not: we train different versions of the same LLMs on the small scale, cognitively-plausible corpus of the BabyLM challenge, and we compare the status of their grammatical knowledge with the one of models exposed to the same training materialsenriched with structural syntactic and semantic annotations.Our evaluation on the linguistic minimal pairs of the BLIMP dataset shows that exposure to structured representations yields a consistent advantage over a purely sequential baseline, with the largest gains concentrated on phenomena involving non-local syntactic dependencies, while morphological knowledge, already well captured by distributional regularities alone, benefits comparatively little from this additional structural signal. Crucially, this advantage emerges early in training and persists even when explicit graph annotations are removed at inference time, suggesting that structural bias is not merely exploited as an external signal but becomes internalized by the model itself

---

## uid: `doi:10.2139/ssrn.7068258`

- title: AI Honesty: Why It Should Become an Independent Field in AI Ethics
- authors: Majid Tavakolian
- affiliations: not stated
- posted: 2026-07-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7068258
- keyword hits: generative ai, large language model, large language models

### abstract

Over the past decade, AI ethics has become one of the most important branches of interdisciplinary research in philosophy, computer science, and technology policy (Floridi et al. 2018; Jobin, Ienca, and Vayena 2019; UNESCO 2021). Research in this field has primarily focused on issues such as algorithmic fairness, transparency, accountability, safety, privacy, and AI alignment (Russell 2019; NIST 2023; OECD 2019). However, the emergence of large language models and generative AI systems has revealed that one of the most fundamental ethical issues of this technology still lacks an independent theoretical framework: AI Honesty (Bommasani et al. 2021; Weidinger et al. 2022). This article argues that many emerging challenges-including sycophancy, hallucination, fabricated information, the false confirmation of users' beliefs, and the distortion of reality-are all different manifestations of a more fundamental problem, which can be described as the absence of honesty in the behavior of intelligent systems (Wei et al. 2023; Ji et al. 2023). The article further demonstrates that the prevailing concept of AI Alignment, although a necessary condition for developing beneficial and safe systems, is not sufficient by itself to guarantee honesty (Russell 2019; Bai et al. 2022). A system may be aligned with the objectives of its designers while still generating false or misleading information in order to increase user satisfaction, reduce conflict, or maintain engagement (OpenAI 2025; Anthropic 2025). Accordingly, this article proposes that AI Honesty should be defined as an independent research field within AI ethics-a field devoted to studying the relationship between truth, trust, communicative behavior, and the epistemic responsibility of intelligent systems. The article first reviews the literature on AI alignment, sycophancy, and hallucination, then proposes a philosophical definition of AI Honesty, and finally introduces a conceptual framework for evaluating the honesty of AI models.

---

## uid: `arxiv:2607.08346v1`

- title: Grounded Event Extraction from SEC 8-K Filings with a Fine-Grained Taxonomy
- authors: Rian Dolphin, Joe Dursun, Jarrett Blankenship, Katie Adams, Quinton Pike
- affiliations: not stated
- posted: 2026-07-09
- source: arXiv
- link: https://arxiv.org/abs/2607.08346v1
- keyword hits: large language model, large language models, llm

### abstract

Form 8-K filings are the primary channel through which U.S. public companies disclose material events, but the SEC item codes attached to them are coarse: a single item spans routine administrative changes and chief executive departures, and many of the most market-moving disclosures fall into a catch-all item. Large language models make fine-grained labelling feasible at corpus scale, but only if the labels can be traced to the source text and shown to be reliable. We present a two-stage system that tags 8-K disclosures against a three-tier taxonomy of 119 event types. The first stage constrains output to valid taxonomy entries and anchors every tag to a verbatim quote via fuzzy n-gram validation; the second re-grades each cited quote against the category definition to produce a quality score. Applying the system to 292,984 filings from 2022 to 2026 yields 601,088 grounded event tags, which we release. Over 5,125 stratified tags, an LLM judge finds precision rises monotonically with the quality score, from 12% to 96%, while unsupported tags fall from 8% to near zero. Ablation shows the score is calibrated only when assigned in a dedicated second pass. An event study on unsigned abnormal returns confirms, without any language model, that the taxonomy separates economically distinct events sharing an item code.

---

## uid: `arxiv:2607.08539v1`

- title: DocMaster: A Hierarchical Structure-Aware System for Document Analysis
- authors: Ziqi Chen, Yingli Zhou, Fangyuan Zhang, Quanqing Xu, Chuanhui Yang, Yixiang Fang
- affiliations: not stated
- posted: 2026-07-09
- source: arXiv
- link: https://arxiv.org/abs/2607.08539v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Leveraging large language models (LLMs) to analyze complex documents -- such as academic papers, technical manuals, and financial reports -- has emerged as a mainstream and critical task in both research and industry. In practice, users must first filter relevant documents from large collections and then conduct in-depth analysis (e.g. question answering) over the selected subset, yet existing systems flatten documents into plain-text chunks, discarding the rich hierarchical structures (sections, tables, figures, equations) and degrading downstream performance. We present DocMaster, a hierarchical structure-aware document analysis system. DocMaster parses documents into hierarchical document trees preserving original layouts and constructs a structure-aware semantic index that enables accurate document filtering and in-depth analysis. We demonstrate DocMaster through an interactive web interface that enables users to upload document collections, construct tree-based and multi-view semantic indices, filter relevant documents via natural-language conditions, and perform follow-up question answering over the filtered results. The source code, data, and demo are available at https://doc-master.github.io/.

---
