# Classification batch 154 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-154.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6727899`

- title: Enriched Fine-Tuning Pipeline with LLM-as-a-Judge Evaluation: A Novel Framework for Teaching Reasoning Strategies to Small Language Models
- authors: Hari Prasad Sampatirao
- affiliations: not stated
- posted: 2026-05-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6727899
- keyword hits: chain-of-thought, fine-tuning, llama, llm

### abstract

Standard parameter-efficient fine-tuning of small language models (SLMs) trains exclusively on extractive domain summariesteaching a model what the domain says, but not how to reason about it. This paper introduces the Enriched Fine-Tuning Pipeline with LLM-as-a-Judge Evaluation (EFTP-J): a novel integrated framework that couples enriched multi-trace training data with a hardware-portable semantic evaluation protocol. The training pipeline synthesises four complementary trace types from raw PDF corpora without any teacher model: (1) extractive knowledge summaries, (2) Chain-of-Thought (CoT) decomposition traces, (3) Knowledge Graph (KG) concept-linking traversal traces, and (4) selfcritique traces in which the model evaluates a draft answer against a four-criterion rubric and refines it. The evaluation pipeline employs an LLM-as-a-Judge protocol with a deterministic rule-based fallback that operates on any hardwareeliminating the GPU dependency of prior judge implementations. Applied to TinyLlama-1.1B-Chat-v1.0 on a ten-document academic corpus (136 content chunks, 349 enriched training samples), EFTP-J is evaluated alongside six baseline augmentation strategies in a sevenway empirical comparison. The EFTP-J trained model (FT-v2) achieves a perfect LLM-judge score of 1.00 on structured methodological questions, and 0.75 on recommendation synthesis tasks on CPU hardwaredemonstrating that reasoning capability baked into model weights at training time produces qualitatively superior outputs on structured question types compared to extraction-only fine-tuning. The dual-mode judge (LLM + rule-based fallback) successfully evaluates all 42 answer-question pairs without failure, resolving the JSON-generation fragility that prevents pure LLM judges from operating reliably on sub-2B parameter models. Together, EFTP-J constitutes the first published framework to jointly address the training-data reasoning gap and the evaluation robustness gap for small language model deployment.

---

## uid: `doi:10.2139/ssrn.6558838`

- title: Philosophy Portability in AI Systems: The Cognitive System Package Framework as Architecture for Cross-Model Epistemic Deployment
- authors: Kwaku Adu Gyamfi
- affiliations: not stated
- posted: 2026-05-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6558838
- keyword hits: claude, large language model, large language models

### abstract

Large language models are widely understood to carry philosophical commitments embedded in their training. These commitments are generally treated as inseparable from the model itself. This paper challenges that assumption. Drawing on the Cognitive System Package (CSP) framework and the metacognitive gap literature, we argue that an AI system's philosophical orientation can be separated from its generative architecture and redeployed as a designed prompt architecture that instantiates that philosophy's epistemic commitments in any sufficiently capable frontier model. We term this capacity philosophy portability. We demonstrate the concept through the design and specification of two Cognitive System Packages: the Grok Cognitive System (GCS), which instantiates xAI's first-principles, truth-seeking philosophy (xAI, 2023; Musk, 2023), and the Claude Cognitive System (CCS), which instantiates Anthropic' s commitments to epistemic humility and genuine helpfulness (Anthropic, 2024; Bai et al., 2022). We posit that both systems may be deployed on models other than their originating platform, producing philosophy-specific epistemic behavior that is architecturally determined rather than model-determined. We examine the implications for AI evaluation methodology, AI system design, and the comparative study of AI epistemic architectures. Altogether, we posit that philosophy portability constitutes a new unit of analysis for AI research, one that separates what a model produces from what a cognitive system surrounding that model is designed to instantiate.

---

## uid: `doi:10.2139/ssrn.6707258`

- title: AI Search Impact Assessment- The ASIA Framework
- authors: Avinash Tripathi
- affiliations: not stated
- posted: 2026-05-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6707258
- keyword hits: chatgpt, claude

### abstract

Purpose: AI-powered search platforms—including Google AI Overviews, ChatGPT, Perplexity, and Claude—are fundamentally restructuring how B2B buyers discover software solutions, yet no sector-specific framework exists for measuring their impact on SaaS business performance. This inaugural Annual AI Search Impact Assessment presents the first comprehensive, data-driven analysis of how AI search is reshaping organic discovery, pipeline generation, and revenue for B2B software companies. Design/Methodology: The ASIA (AI Search Impact Assessment) Framework was applied across 143 B2B SaaS client properties over a twelve-month study period (June 2024–June 2025). The framework employs an exploratory sequential mixed-methods design combining quantitative analysis of search analytics data with multiple embedded case studies. Four proprietary metrics—Click Efficiency Ratio (CER), Traffic-Visibility Gap (TVG), Impression Productivity (IP), and Revenue Efficiency (RE)—were calculated for each property and validated against observed revenue outcomes. Key Findings: By 2027, B2B SaaS companies face an estimated risk where 23% of their organic revenue is exposed to be impacted by AI search shifts. The sample median CER was 0.78 (indicating 22% fewer clicks per impression than baseline) with a median TVG of −12.4% (traffic declining 12.4 percentage points faster than visibility). In 68% of assessed properties, organic traffic had been declining for 60+ days before internal detection. B2B SaaS companies now derive 37% of their organic pipeline from AI-vulnerable content categories, up from 18% one year prior. Among companies cited by AI platforms, 73% experienced the “Citation Paradox”—rising AI mentions paired with declining organic traffic. Despite 61% of properties showing measurable AI search impact, only 9% have implemented any AI search optimization. Implications: The findings establish B2B SaaS as a sector experiencing moderate-to-high AI search impact, with informational and educational content most affected while transactional and brand queries remain relatively protected. The assessment provides practitioners with sector-specific benchmarks, a diagnostic pattern taxonomy, and financial projection models. For marketing scholars, this paper extends information foraging theory into AI-mediated search environments and proposes the first formative measurement index for AI search impact in B2B contexts.

---

## uid: `doi:10.2139/ssrn.6741387`

- title: Beyond Blocking: A Privacy-Preserving Local AI System for Empathic Game Coaching in Children​
- authors: Byoung Ha Kim, Ki  Sung Kang, Dong-Wook Kim
- affiliations: not stated
- posted: 2026-05-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6741387
- keyword hits: llm, llms

### abstract

Children's game over-immersion is a growing public health concern, yet existing interventions are limited to restrictive blocking or clinical therapy—neither scalable nor privacy-preserving. Cloud-based AI coaching transmits children's biometric data externally, conflicting with COPPA/GDPR and blocking parental adoption.We present a privacy-preserving hybrid AI coaching system replacing blocking with empathic dialogue. A local LLM on the home PC delivers real-time conversational coaching while all biometric data (facial images, voice, behavioral signals) are processed locally and discarded after each session. Only anonymized aggregate statistics cross the network boundary.Systematic evaluation of eight LLMs across six child-interaction scenarios identified five essential selection criteria; only 25% met all criteria. The system implements four adaptive coaching strategies: game-specific dialogue, self-planned time negotiation, history-based persuasion, and multi-user face-recognition switching.Phase I feasibility demonstration on consumer-grade hardware (8 GB GPU, ~USD 1/month) confirmed simultaneous game-and-coaching operation without frame-rate degradation. Observational testing revealed reflexive posture correction without gameplay interruption—a compliance mechanism blocking cannot achieve.We position this as Phase I formative feasibility; controlled efficacy evaluation (Phase II RCT, n≥20, IRB-approved) is reserved for follow-up. To our knowledge, this is the first system providing privacy-preserving local AI coaching, empathic LLM dialogue, and systematic model selection for child-facing applications.

---

## uid: `doi:10.2139/ssrn.6767137`

- title: How Digital Intelligence Drives Corporate Green Innovation: Evidence from China
- authors: Tong Feng, Xiaomin Wang, Tianxin Wang, Qun Li, Lei Guo
- affiliations: not stated
- posted: 2026-05-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6767137
- keyword hits: large language model, large language models

### abstract

Corporate green innovation is vital for sustainable development but is often hindered by technological risk, resource constraints, and information asymmetry. As a transformative production paradigm shaped by artificial intelligence, cloud computing, and big data, digital intelligence (DI) may help overcome these barriers. This study examines the causal effect of DI on corporate green innovation. We construct a semantic-rich DI index using large language models and adopt a double machine learning framework with a shift-share instrumental variable for identification. Using data on Chinese listed firms from 2007 to 2023, we find that DI significantly promotes green innovation, especially substantive green invention patents rather than utility models, suggesting limited greenwashing concerns. Mechanism analyses show that DI works by easing financing constraints, improving resource allocation efficiency, and strengthening knowledge absorptive capacity. The effect is stronger for firms with better disclosure quality and in regions with superior digital infrastructure and innovation capacity.

---

## uid: `doi:10.2139/ssrn.6749481`

- title: AI Exposure and Housing Markets
- authors: Cayman Seagraves, Stace Sirmans
- affiliations: not stated
- posted: 2026-05-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6749481
- keyword hits: generative ai, llm

### abstract

Generative AI arrived just as the pandemic had pushed housing demand away from expensive, supply constrained metros. We ask whether the period after Chat-GPT extended that dispersion or reversed it. Using a quarterly panel of 211 U.S. metros from 2017Q1 to 2025Q4, we relate Zillow and FHFA house price growth to AI Geography Exposure weighted by 2019 population, with the 2020 remote work break timed separately. AI exposed metros grow faster after 2023: a one standard deviation increase in AIGE is associated with 3.6% higher cumulative ZHVI growth, about $9,400 at the sample median 2023 home value. The premium also appears in FHFA prices and rents, concentrates in supply inelastic metros, and is reproduced by a predetermined LLM task suitability index. A pandemic WFH placebo has the opposite sign. IRS migration data show reduced outmigration from exposed metros, and Revelio LinkedIn data show rising AI hiring there. The early generative AI period appears to have reinforced the residential value of dense, supply constrained high skill labor markets, reversing the spatial direction of the pandemic.

---

## uid: `doi:10.2139/ssrn.6770779`

- title: Unpacking Social Exposure
- authors: Mingyang Liu, Zacharias Sautner, Laurence van Lent, Ruishen Zhang
- affiliations: not stated
- posted: 2026-05-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6770779
- keyword hits: large language model, large language models

### abstract

We develop a method to measure firms' exposures to social issues from earningscall transcripts. The method applies large language models and decomposes social exposure into five domains: Employee Welfare, DEI, Stakeholder Outreach, Ethical Commitments, and Crisis Response. The measures cover over 15,000 firms across 93 countries from 2003 to 2024. The five domains exhibit distinct, sometimes opposing, associations with labor outcomes, productivity, and ESG ratings. Aggregating domains of differing sign attenuates estimated effects, consistent with the weak findings reported for composite social scores. Domains correlate with labor-market outcomes and productivity in different directions; the aggregate averages these correlations toward zero. Exploiting the Dobbs decision, which tightened abortion regulation, as a labor-supply shock, we find that firms with higher pre-Dobbs DEI exposure experienced a lower worker outflow than non-exposed firms in the same state and month.

---

## uid: `doi:10.2139/ssrn.6757178`

- title: Pathways to Judicial Justice in Legal Large Language Model-assisted Sentencing: A Legal Realist Perspective
- authors: Liu Bingni
- affiliations: not stated
- posted: 2026-05-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6757178
- keyword hits: large language model, llm

### abstract

The legitimate boundaries of legal large language model (LLM)-assisted sentencing essentially delineate the equilibrium between technical rationality and judicial rationality, as well as between legal realist practice and normative ideals. Although LLM-assisted sentencing ostensibly aligns with the legal formalist pursuit of rule deduction and legal certainty, its datadriven nature reveals a distinctly legal realist orientation. This orientation, in turn, engenders a dual crisis of judicial justice: a legitimacy crisis concerning fact-finding, and, at a deeper level, a normative crisis regarding rule application. Addressing these intertwined crises necessitates the establishment of virtue-centred human-machine collaborative accountability rules, an algorithmic governance framework that incorporates broad participation from the legal professional community, and a paradigm shift in judicial decision-making from an efficiencyfirst approach to one guided by virtue. This article seeks to provide jurisprudential support and institutional principles for the reform of sentencing standardisation in the digital age.

---
