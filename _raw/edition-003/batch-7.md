# Classification batch 7 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-7.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6650978`

- title: From Passing Exams to Passing Practice: Evaluating the Practical Readiness of Large Language Models in Legal Case Analysis
- authors: Sascha Schweitzer, Markus Conrads
- affiliations: not stated
- posted: 2026-04-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6650978
- keyword hits: claude, gemini, gpt-5, large language model, large language models, llm, llms

### abstract

Recent studies have demonstrated that large language models (LLMs) can pass standardized legal examinations, including bar exams and university-level tests. However, these benchmarks predominantly rely on multiple-choice questions or narrowly scoped essay tasks that do not capture the full complexity of real-world legal practice. This study shifts the evaluation paradigm from exam performance to practical readiness by testing frontier LLMs on a corpus of 50 German civil-law Aktenvortrag cases, an oral examination format that closely simulates judicial decision-making. Each case requires the model to extract relevant facts from unstructured multi-page case files, identify the decisive legal issues, apply the correct legal framework, and formulate a structured, practice-oriented solution. Model outputs are evaluated using case-specific rubrics with a novel gatekeeper mechanism that caps scores when critical legal issues are missed, distinguishing between argumentative quality and practical usability. A key design principle separates this approach from unstructured LLM-as-a-judge evaluation: the normative judgment is made by a legal expert in the rubric before automated scoring begins, reducing the evaluating model's role to an execution check against explicit criteria. The dataset comprises 50 cases, 250 generated solutions, and 1250 evaluations in a full 5×5 cross-evaluation design. Results show that Claude Opus 4.6, Gemini 3.1 Pro, and GPT-5.4 form a statistically indistinguishable top tier with mean gatekeeper-adjusted scores of 63.8-64.3%, significantly outperforming Grok 4.20 and Kimi K2.5 (32.9-38.9%; all Holm-corrected p ≤ 0.001). Within that top tier, Gemini 3.1 Pro offers the most favorable operational profile, combining comparable quality with substantially lower cost and faster iteration. The gatekeeper analysis further indicates that even top-tier models miss decisive issues in a substantial share of cases according to the automated evaluators, suggesting that the gap between passing legal exams and delivering practice-ready legal analysis warrants careful attention.

---

## uid: `doi:10.2139/ssrn.6449018`

- title: Cross-Architecture Semantic Geometry in LLM Residual Streams: Alignment, Null Controls, and Overfitting Bounds
- authors: Juan Jacobo Jimenez Sanchez
- affiliations: not stated
- posted: 2026-04-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6449018
- keyword hits: large language model, large language models, llama, llm, mistral, qwen

### abstract

We investigate whether large language models of different architectures encode semantic structure in geometrically equivalent ways in their residual streams. Using raw residual activations (no sparse autoencoders), we test cross-architecture alignment across five models spanning four families (Gemma, Llama, Qwen, Mistral; 8B-123B parameters). Three findings are robust: (1) all tested models perfectly separate a structured 64-prompt probe set from 50 Wikipedia controls (ARI=1.0, at all tested layers); (2) semantic domain labels are linearly decodable within each model at 60-80% accuracy (chance=25%); and (3) representational similarity between independently trained models is high (CKA ≥ 0.97 between Llama 3.3 70B and Qwen 2.5 72B). We also identify a methodological problem in a commonly used alignment measure: the standard pipeline of PCA(50) + Procrustes on 64 points produces near-perfect cross-model transfer (95-100%) even for random-label controls, making it uninformative as evidence for shared geometry. A constrained analysis with PCA(5) reveals honest transfer rates: 66% for the original probe set, 94% for recipe cuisine types, 52% for animals, and 52% for random-label controls. We conclude that cross-model semantic geometry is partially shared-coherent taxonomies produce above-chance transfer while random controls do not-but that Procrustes alignment at standard PCA dimensionalities is unreliable with small sample sizes. We propose a constrained protocol (multiple PCA dimensionalities with random-label controls) as a necessary methodological check for future cross-model alignment studies.

---

## uid: `doi:10.2139/ssrn.6557318`

- title: The 70/30 Rule: User Framing as the Dominant Driver of Sycophantic Behavior in Production AI Systems
- authors: Daniel Anene
- affiliations: not stated
- posted: 2026-04-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6557318
- keyword hits: claude, large language model, large language models, llama, llm, llms, mistral

### abstract

Sycophancy in large language models (LLMs) the systematic tendency to agree with, flatter, and validate users rather than provide accurate, independent analysis is widely recognized as a critical failure mode in production AI systems. Prior research has focused primarily on sycophancy as a model-level phenomenon driven by reinforcement learning from human feedback (RLHF), positioning it as a training-time problem requiring training-time intervention. In this paper, we present findings from a longitudinal deployment study of 30,247 user-AI interactions across 1,043 production agents and six enterprise domains. Our central finding, the 70/30 Rule, demonstrates that approximately 70% of sycophantic AI responses are directly attributable to user framing patterns rather than model architecture. We introduce the Striker Sycophancy Index (SSI), an 8-tier behavioral scoring metric validated against human annotation (kappa=0.84), and demonstrate through controlled framing experiments that deployment-level calibration frameworks can address the dominant source of sycophancy without model retraining. Our directive calibration framework achieved a mean 73% SSI reduction across production deployments with consistent results across Anthropic Claude, Meta Llama 3.1, Mistral 7B, and OpenAI GPT series.

---

## uid: `doi:10.2139/ssrn.6688478`

- title: Systematic AI-Assisted Analysis of Public Broadcaster Impartiality: A Scalable Methodological Framework for Measuring Structural Bias in Public Service Media
- authors: David Schlaepfer
- affiliations: not stated
- posted: 2026-05-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6688478
- keyword hits: claude, gemini, large language model, large language models, llm, llms

### abstract

We present a scalable, reproducible methodology for the systematic measurement of structural bias in public service media (PSM) output. Applying large language models (LLMs) across a corpus of 25,000+ broadcast subtitle files from Switzerland (SRG/SRF), Germany (ARD/ZDF), and Norway (NRK) spanning 1968-2026, we operationalise fifteen documentary bias criteria grouped into five analytical categories: Framing, Source and Visibility, Omission, Moderation Conduct, and Agenda-Setting. Each finding is anchored to direct quotations with timestamps, enabling independent verification. A directional cross-validation across three independent LLM families (Anthropic Claude, Google Gemini, OpenAI GPT) on a stratified sample of N=98 broadcasts confirms that all three models independently identify the same directional bias pattern. The key finding-a mean Weglassen (Omission) score of 7.03/10 across Swiss PSM-indicates that content omission follows systematic, non-random patterns across programmes, time periods, and political topics. To our knowledge, this represents the first largescale, AI-assisted, primary-source-anchored framework for PSM impartiality measurement worldwide. The methodology has direct applications for regulatory bodies, parliamentary inquiries, and legal proceedings.

---

## uid: `doi:10.2139/ssrn.6690543`

- title: Neurosymbolic Multi-Layer LLM vs Unimodal LLMs and Human Specialists in Acute Aortic Dissection: A MIMIC-IV Emergency Department Cohort Study
- authors: Rasit Dinc, mete Ucdal, Evren ekingen
- affiliations: not stated
- posted: 2026-05-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6690543
- keyword hits: claude, gemini, gpt-4, large language model, llm, llms

### abstract

Background: Acute aortic dissection (AAD) presenting to the emergency department carries one of the highest time-sensitive mortality rates among cardiovascular emergencies. Neurosymbolic multi-agent large language model (NS-LLM) systems integrating deterministic clinical rule engines with neural inference represent a promising paradigm for AI-assisted triage support. Their comparative performance against unimodal LLMs and human specialists on a real-world ED cohort from a validated, publicly available critical care database has not been evaluated. Methods: We performed a comparative diagnostic performance evaluation using 320 randomly stratified AAD cases extracted from the MIMIC-IV database (v2.2; Medical Information Mart for Intensive Care, Beth Israel Deaconess Medical Center, Boston, MA; study period 2011–2019). Patients were identified via ICD-10 codes I71.00–I71.03 from the MIMIC-IV-ED module. From 700 eligible encounters with confirmed intimal flap on computed tomography angiography (CTA) report, 320 were randomly stratified by Stanford type (type A: 192, 60.0%; type B: 128, 40.0%), treatment modality, and 30-day mortality status. Each case was independently evaluated by: (1) a five-agent NS-LLM comprising a cardiovascular surgery (KVC) agent, an emergency medicine agent, a neurosymbolic operator, and two control-layer agents; (2) three unimodal LLMs (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro) under zero-shot conditions; and six human specialists (three KVC surgeons, three EM physicians) applying 2024 ESC and 2022 ACC/AHA guidelines. Primary outcomes were Stanford classification accuracy, guideline-based treatment concordance, and 30-day mortality prediction AUC. Results: The 320-patient MIMIC-IV ED cohort had a mean age of 61.2 ± 12.1 years; 67.5% were male; 74.1% had hypertension; and overall 30-day mortality was 20.0% (95% CI, 16.0–24.7%). The NS-LLM achieved Stanford classification accuracy of 94.4% (95% CI, 91.2–96.8%), treatment concordance of 91.6% (95% CI, 87.9–94.4%), and mortality AUC of 0.872 (95% CI, 0.841–0.903; κ=0.887). Unimodal LLM performance was significantly inferior across all outcomes (accuracy 79.7–84.1%; AUC 0.712–0.748; all P<0.001). KVC specialists achieved the highest overall performance (accuracy 96.3%; AUC 0.891; κ=0.921), not significantly different from NS-LLM (P=0.382). EM specialists performed below both NS-LLM and KVC surgeons (accuracy 88.4%; P=0.021 vs. NS-LLM). Conclusions: Evaluated against MIMIC-IV ED AAD cases, the NS-LLM matched KVC specialist performance and significantly outperformed unimodal LLMs and EM specialists across all primary outcomes. These findings support prospective evaluation of neurosymbolic multi-agent architectures as decision-support tools in ED settings where immediate subspecialty expertise is unavailable.

---

## uid: `doi:10.2139/ssrn.6725589`

- title: Evaluation of AI Chatbot Responses to Pediatric Urology Frequently Asked Questions
- authors: Paul Kokorowski, Andrew Freedman, Nadine Friedrich, Timothy Daskivich, Najva Mazhari
- affiliations: not stated
- posted: 2026-05-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6725589
- keyword hits: chatgpt, claude, gemini, gpt-4, large language model, llm, llms

### abstract

BackgroundParents of children with urologic conditions frequently seek health information online; however, individual health literacy and emotional stress may hinder understanding. Large language model (LLM) chatbots provide accessible health information, yet their accuracy, completeness, tone, and readability remain uncertain.ObjectiveTo evaluate the quality of responses from four publicly available LLMs (ChatGPT-4o, Claude 3.7, Gemini 2.5, and Copilot) to frequently asked questions (FAQs) in pediatric urology.MethodsFAQs were generated using standardized prompts and submitted to each LLM using parent-centered instructions. Two board-certified pediatric urologists independently rated responses across seven domains: Accuracy, Completeness, Safety, Clarity, Actionability, Conciseness, and Global Quality Score using a 5-point Likert scale. Emotional tone was analyzed using the NRC Word-Emotion Association Lexicon, and readability was assessed using seven established metrics.ResultsAll LLMs produced generally high expert ratings for accuracy (mean 4.27), safety (4.36), and clarity (4.42). Claude achieved the highest overall quality score (4.35), followed by Gemini (4.03), ChatGPT (4.00), and Copilot (3.80). Emotional tone was predominantly positive and supportive across models. Reading corresponded to an 11th–15th grade reading level, exceeding the recommended 6th–8th grade patient-education standards.ConclusionLLMs can provide accurate, safe, and supportive information for parents, but their usefulness is limited by gaps in completeness and high readability levels. Claude achieved the highest overall quality, whereas ChatGPT demonstrated high safety with lower completeness. Future development would prioritize plain-language optimization, context-aware emotional framing, and parent co-design to improve comprehension.

---

## uid: `doi:10.2139/ssrn.6732292`

- title: TITAN-SR: development and validation of a biomedical BERT ensemble for systematic-review screening
- authors: Tyler Pitre, Dena Zeraatkar, John Granton, Jason  W. Busse, Bram Rochwerg, Gordon H. Guyatt
- affiliations: not stated
- posted: 2026-05-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6732292
- keyword hits: claude, deepseek, gemini, gpt-4, large language model, llm

### abstract

BackgroundMachine learning tools to facilitate literature screening have existed for over a decade, yet adoption remains limited. Available approaches range from active learning tools that require hundreds of interactive screening decisions before they can prioritise citations effectively, to commercial large language model (LLM) chatbots repurposed for screening without task-specific training.ObjectiveWe aimed to develop TITAN-SR, a screening tool built on biomedical BERT models, and to compare its performance against ASReview, a widely used active-learning tool for systematic-review screening; four commercial LLM chatbots evaluated on a 500-review benchmark (Claude Sonnet 4, GPT-4o, DeepSeek-V3, Gemini 2.0 Flash); and GPT-4o-mini evaluated separately on all 3,434 evaluable internal test reviews.MethodsWe assembled 762,934 citation–label pairs from 19,787 completed reviews and trained TITAN-SR on a prespecified review-level training split, with validation and testing on held-out reviews. The tool uses an ensemble of two biomedical BERT models (PubMedBERT and BioLinkBERT) that read a review’s eligibility criteria alongside each citation’s title and abstract and outputs a raw inclusion score. Training penalised missing a relevant study 10 times more heavily than retaining an irrelevant one. We compared TITAN-SR with four commercial LLM chatbots applied without task-specific training on a stratified 500-review benchmark, and additionally evaluated GPT-4o-mini on the 3,434 evaluable internal test internal test set. External validation and the ASReview comparison used a temporally independent holdout of 22 Cochrane reviews comprising 142,504 records, with no review-level overlap with the Cochrane reviews used during model development. To ensure a fair comparison with an active-learning tool that improves with reviewer input, ASReview received a warm-up period (20% of known includes plus proportional excludes).ResultsAcross 3,434 test reviews, TITAN-SR achieved a median specificity at 99% recall (S@99R) of 0.902 and median AUC of 0.974; at the threshold required to achieve 99% recall within each review, TITAN-SR excluded a median of 90.2% of irrelevant citations. TITAN-SR outperformed all four chatbots evaluated on the 500-review benchmark (Bonferroni-corrected paired Wilcoxon signed-rank p ≤ 5 × 10−31 for every comparison) and also outperformed GPT-4o-mini on the full 3,434-review test set. The chatbots exhibited calibration collapse: 82–99% of their self-reported confidence scores were ≥ 0.9 regardless of accuracy. Temporal validation on 22 held-out Cochrane reviews showed performance virtually identical to internal results (median AUC 0.976, S@95R 0.897). In head-to-head comparison on those 22 reviews, TITAN-SR outperformed ASReview, winning 18 of 22 (81.8%; median paired S@95R difference +0.145, bootstrap 95% CI +0.101 to +0.201).ConclusionsA purpose-built screening tool based on biomedical BERT models, developed using a corpus of nearly 20,000 completed reviews, outperformed ASReview, a widely used active-learning tool, and four commercial LLM chatbots evaluated without task-specific training (plus GPT-4o-mini on all 3,434 evaluable internal test reviews). Temporal validation on 22 held-out Cochrane reviews confirmed that performance generalised to new Cochrane reviews published after the model-development period.

---

## uid: `doi:10.2139/ssrn.6742119`

- title: The Finance Value Pyramid : A Conceptual Framework for Repositioning Value Creation in the Finance Function in the Era of Generative Artificial Intelligence
- authors: BAYU ISTANTORO
- affiliations: not stated
- posted: 2026-05-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6742119
- keyword hits: generative ai, generative artificial intelligence, large language model, large language models, llm, llms

### abstract

This paper introduces the Finance Value Pyramid-a three-level conceptual framework that classifies finance function activities according to their strategic value contribution: Data Work (Level 1), Analytical Work (Level 2), and Narrative Work (Level 3). Unlike prior financetransformation research that focuses primarily on technical efficiency, this article argues that the emergence of generative AI and large language models (LLMs) accentuates a pre-existing value asymmetry: LLMs substantially automate Data Work (Eloundou et al., 2024), augment Analytical Work while preserving human interpretive judgment (Yigitbasioglu et al., 2023), and leave Narrative Work-the highest-value domain-as the most resilient human advantage. Through critical synthesis of three literature domains-decision usefulness theory (Beaver, 1968; IASB, 2018), the evolution of management accounting toward business partnering (Lambert & Sponem, 2012; Goretzki & Messner, 2019), and AI impact on cognitive work (Frey & Osborne, 2017; Eloundou et al., 2024)-the framework derives each pyramid level analytically from decision-usefulness criteria and proposes an extension of that theory to incorporate narrative translation as an explicit dimension of actual usefulness. Three conceptual propositions are advanced together with a falsifiable empirical research agenda.

---
