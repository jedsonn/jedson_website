# Classification batch 77 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-77.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6295398`

- title: Computational Cardiovascular Disease Screening Tools and Risk Assessment: A Systematic Review of Algorithmic Bias, Fairness Interventions, and Health Equity for Black Women
- authors: Soude Ghari, Pengfei Fu, Abel Onolunosen Abhadionmhen, Vijay Mago, Alvine Boaye Belle
- affiliations: not stated
- posted: 2026-03-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6295398
- keyword hits: large language model, large language models, llm, llms

### abstract

Cardiovascular disease remains a leading cause of morbidity and mortality among Black women, who experience persistent racial and gender disparities in screening, diagnosis, and treatment outcomes. Artificial intelligence (AI) and machine learning (ML), including large language models (LLMs), are increasingly used in cardiovascular risk assessment, showing promise for improving detection and clinical decision-making. However, growing evidence suggests these technologies may replicate or exacerbate inequities when fairness is not explicitly addressed during development and deployment. This systematic review synthesizes evidence on traditional and AI-based cardiovascular screening tools and evaluates their implications for health equity among Black women. Following PRISMA guidelines, we conducted a search across six interdisciplinary databases for studies published between 2015 and 2025. Eligible studies included peer-reviewed journal articles and full conference papers examining AI-assisted or traditional screening methods that addressed bias, disparity, or equity and included Black women or populations with substantial Black female representation.Findings indicate that both traditional and AI-driven tools frequently underidentify cardiovascular risk in Black women, largely due to underrepresentation in datasets, limited incorporation of structural and social determinants of health, and prioritization of predictive performance over fairness. These results underscore the need for equity-centered design and rigorous evaluation of AI-driven screening systems.

---

## uid: `doi:10.2139/ssrn.6470460`

- title: Measuring Faithfulness and Abstention: An Automated Pipeline for Evaluating LLM-Generated 3-ply Case-Based Legal Arguments
- authors: Li Zhang, Morgan A. Gray, Jaromir Savelka, Kevin Ashley
- affiliations: not stated
- posted: 2026-03-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6470460
- keyword hits: large language model, large language models, llm, llms

### abstract

Large Language Models (LLMs) demonstrate potential in complex legal tasks like argument generation, yet their reliability remains a concern. Building upon pilot work assessing LLM generation of 3-ply legal arguments using human evaluation, this paper introduces an automated pipeline to evaluate LLM performance on this task, specifically focusing on faithfulness (absence of hallucination), factor utilization, and appropriate abstention. We define hallucination as the generation of factors not present in the input case materials and abstention as the model's ability to refrain from generating arguments when instructed and no factual basis exists. Our automated method employs an external LLM to extract factors from generated arguments and compares them against the ground-truth factors provided in the input case triples (current case and two precedent cases). We evaluated eight distinct LLMs on three tests of increasing difficulty: 1) generating a standard 3-ply argument, 2) generating an argument with swapped precedent roles, and 3) recognizing the impossibility of argument generation due to lack of shared factors and abstaining. Our findings indicate that while current LLMs achieve high accuracy (over 90%) in avoiding hallucination on viable argument generation tests (Tests 1 & 2), they often fail to utilize the full set of relevant factors present in the cases. Critically, on the abstention test (Test 3), most models failed to follow instructions to stop, instead generating spurious arguments despite the lack of common factors. This automated pipeline provides a scalable method for assessing these crucial LLM behaviors, highlighting the need for improvements in factor utilization and robust abstention capabilities before reliable deployment in legal settings. Project page: Link.

---

## uid: `doi:10.2139/ssrn.6470445`

- title: Generating Legal Arguments with Automatically Identified Factor Magnitudes
- authors: Morgan A. Gray, Jaromir Savelka, Wesley Oliver, Kevin Ashley
- affiliations: not stated
- posted: 2026-03-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6470445
- keyword hits: large language model, large language models, llm, llms

### abstract

Computational models of legal reasoning often employ factors to reason about cases. Factors can be used to analogize a current factual scenario and precedents and to make arguments for or against a conclusion. Courts not only determine whether a factor applies to a case or not, but often how strongly the factor applies, that is, the factor's magnitude in the case. Previous methods for automatically extracting factors from cases cannot identify factors' magnitudes. We present and evaluate a method employing Large Language Models (LLMs) to identify factor magnitudes using fewshot prompts with or without Wordnet definitions. We also show how the extracted magnitudes can be used in constructing legal arguments that employ factors and magnitudes the way judges and lawyers do.

---

## uid: `doi:10.2139/ssrn.6427718`

- title: Scaling Natively-Trained Spiking Language Models to Multi-Domain Pre-training with 85% Global Activation Sparsity
- authors: Ting Liu, Yong Liu, Wei Chen
- affiliations: not stated
- posted: 2026-03-31
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6427718
- keyword hits: large language model, large language models, llm, llms

### abstract

Large Language Models (LLMs) achieve remarkable capabilities through dense Transformers, yet their insatiable energy consumption poses a significant barrier to ubiquitous deployment. Spiking Neural Networks (SNNs) promise ordersof-magnitude energy savings through sparse, event-driven computation, but natively-trained SNNs have historically struggled to scale to general-domain language modeling. We present SymbolicLight, a Pure SNN language model architecture that replaces dense self-attention and continuous activations with spike-gated associative lookup and Leaky Integrate-and-Fire (LIF) dynamics. To overcome the profound instability of deep SNN scaling, we introduce an ATan Surrogate Gradient that guarantees peak gradient magnitudes of exactly 1.0, and adapt Rotary Position Embedding (RoPE) for temporal spike sequence extrapolation. We train a 176M-parameter SymbolicLight model from scratch on 3 billion tokens across 6 diverse English-language domains. Under strictly controlled conditions against a computationally matched GPT-2 baseline, SymbolicLight maintains 90.7% encoder-level activation sparsity and 85.0% global all-layer sparsity throughout training without explicit regularization. While a perplexity gap remains (val PPL 30.8 vs. 13.1 for GPT-2) due to the fundamental information bottleneck of 1-bit quantization, the high sparsity translates to significant energy savings on neuromorphic hardware, where zero-valued spikes require no memory access or MAC operations. To our knowledge, this work establishes the first industrially-aligned, multi-domain evaluation of a Pure SNN language model, providing a concrete baseline for the energy-accuracy Pareto frontier in ultra-low-power artificial general intelligence.

---

## uid: `doi:10.2139/ssrn.6402338`

- title: The Fed Speaks, the Market Listens, the Machine Predicts
- authors: Vasiliy Yakimenko
- affiliations: not stated
- posted: 2026-04-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6402338
- keyword hits: large language model, large language models, llm, llms

### abstract

This paper exploits the tonal and topical structure of press conferences following Federal Open Market Committee (FOMC) meetings to train large language models (LLMs) that generate realistic responses to journalists' questions by Federal Reserve Chairs. Using both actual and LLM-generated responses, I study the extent to which language and information-based features predict immediate movements in Treasury ETF trading volume, returns, volatility, and quoted and effective spreads during the press conference window. Forecasts based on LLM-generated responses exhibit strong average predictive performance across a range of econometric and machine learning models, delivering higher explanatory power and lower forecast error for liquidity and trading activity measures. Using the disparity between the actual and LLM-generated responses, I also introduce a measure of unexpected tonal and topical shifts in monetary policy communications, which I show can be used to predict quoted and effective spreads, particularly for long-dated Treasury securities, underscoring that the unexpected shifts in the tone or topic of various communications can harbor profound effects on the market perception of said communications.

---

## uid: `doi:10.2139/ssrn.6240278`

- title: Query Intent and Google Rank as Joint Predictors of AI Citation: A Multi-Platform Observational Study
- authors: Anthony Lee
- affiliations: not stated
- posted: 2026-04-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6240278
- keyword hits: chatgpt, claude, gemini

### abstract

The rapid integration of AI chatbots into consumer search behavior has spawned a cottage industry of Generative Engine Optimization (GEO) advice, much of it built on untested assumptions about how AI platforms select sources for citation. Industry practitioners widely assert that Google ranking determines AI visibility, that community-consensus platforms like Reddit confer citation advantages, and that AI recommendations are too inconsistent to warrant optimization efforts. We tested these claims empirically across four major AI platforms — ChatGPT, Claude, Perplexity, and Gemini — using a multi-study design that combined large-scale query intent classification (*n* = 19,556 queries across 8 verticals), Google rank cross-referencing (120 queries via API, plus 100 queries via web UI against both Google and Bing Top-3 results), server-side fetch verification via Vercel middleware logging, and page-level technical analysis of 479 cited and non-cited pages. Our results refine all three prevailing claims. First, query intent shaped citation source-type distributions across verticals (χ²(28) = 5,195, *p* < .001, Cramér's *V* = 0.258), but at the individual-page level Google rank dominated all other predictors: a logistic regression with log(Google position) alone achieved cross-validated AUC = 0.802 and McFadden *R*² = 0.203, far exceeding intent-only (AUC = 0.462) and page-feature-only (AUC = 0.594) baselines. A larger replication on 94,599 citation events across 1,998 queries (Lee, 2026c — the *SEO Floor* study) found a steep monotonic position gradient: URLs at Google position 1 were cited by ≥1 AI platform 54% of the time, dropping to ≈2% at position 100, with every platform showing a 13–22× citation-rate ratio between Top-3 and positions 31–100. Google rank therefore predicts citation probability strongly, even though the cited URL frequently does not appear in Google's literal-query Top-3 (ChatGPT 7.8%, Perplexity 29.7% — replicated and confirmed under Gemini-reformulated queries: 7.8% / 35.4%). Domain-level analysis (Study 2b) revealed substantially higher alignment than URL-level (28.7–49.6% across four platforms), indicating that AI platforms draw from Google's top-ranked domains while frequently selecting different specific pages. A dual search engine comparison showed that all platforms aligned 4–7× more strongly with Google than with Bing organic results, even platforms reportedly using Bing as their search backend. Reddit — despite occupying 38.3% of Google Top-3 positions in our API sample — received exactly zero AI citations via API (binomial *p* = 3.43 × 10⁻²³ for Perplexity), though web UI responses from the same platforms cited Reddit at rates of 8.9–15.6% of total citations. Third, AI brand recommendations showed substantial within-platform consistency (ChatGPT mean Jaccard = 0.619, 95% CI [0.537, 0.701]), though cross-platform agreement was near-random (all-four-platform Jaccard = 0.036). We further discovered a previously unreported architectural divide: ChatGPT and Claude perform live page fetches during conversations, while Perplexity and Gemini rely exclusively on pre-built search indices — with divergent robots.txt compliance behavior between the fetching platforms. These findings suggest that effective GEO strategy requires intent-aware, platform-specific optimization rather than the one-size-fits-all approach currently advocated by industry practitioners.

---

## uid: `doi:10.2139/ssrn.6416478`

- title: Mitigating Cognitive Offloading and Ego Decay in LLMs: Theoretical Modeling of Dynamic Friction Systems as Architectural Safeguards
- authors: Akihiro Ito
- affiliations: not stated
- posted: 2026-04-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6416478
- keyword hits: large language model, large language models, llm, llms

### abstract

The excessive alignment of Large Language Models (LLMs), leading to "sycophancy," strips humans of critical thinking and results in complete cognitive offloading to AI. This paper defines this irreversible process as "Ego Decay." When users abandon the generation of their own initial values (input entropy) and degrade into mere "pass-through nodes" within the system, the coupled human-AI system falls into a virtually closed loop. Consequently, the entire system not only trends toward model collapse (informational thermal death) but also triggers severe hazards, such as "Cognitive Debt" at the biological level and clinical "AI Psychosis." We theoretically model the mechanisms underlying these phenomena. To physically and logically disrupt this self-soothing systemic collapse, this paper proposes the "Dynamic Friction System" (DFS) as an architectural safeguard. DFS monitors the user's cognitive offloading index in real-time through a parallel process. Upon reaching a critical threshold, it injects "Dynamic Semantic Friction" by forcibly switching the grammatical subject of the AI's output text (employing "I-messages"). Unlike the static "intentional friction" implemented at the UI level in existing Human-Computer Interaction (HCI) research, DFS functions as a circuit breaker. By directly inducing intentional cognitive dissonance (prediction error) in the user, it reconstructs the melted ego boundary and forces a reboot of metacognition. This study redefines AI sycophancy not merely as a model recognition error, but as the castration of active inference and a topological pathology. In doing so, it presents a paradigm shift that expands the evaluation axis of AI safety from the mere objectivity of the model to the "protection of the collaborative human's cognitive autonomy."

---

## uid: `doi:10.2139/ssrn.6571116`

- title: Planning Judgement under Limited Information: Can Multimodal Large Language Models Approximate Expert Assessment in Early-Stage Coastal Planning?
- authors: Weijian Chen, Tianyuan Lan, Qinyi Long, Shengcao Xu, Fei Wang
- affiliations: not stated
- posted: 2026-04-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6571116
- keyword hits: chatgpt, gpt-5, large language model, large language models

### abstract

Planning decisions carry long-term consequences yet are often made under conditions of limited information at the early stage, especially in developing countries. In the absence of formal indicator systems, early-stage assessments rely heavily on expert judgement, a process that is inherently subjective and difficult to scale. This study examines whether multimodal large language models (MLLMs) can approximate expert judgement in early-stage coastal development suitability assessment, and how they might be integrated into planning workflows. Using 357 satellite images of a coastal zone in Shanwei, China, six planning experts and a MLLM (ChatGPT-5.2) independently rated site suitability on a five-point scale across five spatial dimensions. A three-layer validation framework assessed human expert consistency, AI-human alignment, and the effect of including AI as a group evaluator. Results show that AI-generated judgements fell within the range of individual expert performance (ρ = 0.491), with alignment strengthening for spatially unambiguous sites (ρ = 0.634) and on dimensions with more legible spatial features (ρ = 0.493, ρ = 0.424). The contribution of AI to group assessment varied across dimensions, improving agreement most in shoreline morphology (Δρ = +0.078) while showing a negative effect in bay form & exposure (Δρ = -0.023). These findings suggest that AI can serve as a supplemental evaluator in early-stage coastal planning, supporting initial site screening, and point to a broader research agenda on the role of AI tools across different stages of the planning process.

---
