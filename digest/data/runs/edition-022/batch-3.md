# Classification batch 3 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-3.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7315788`

- title: Knowledge-Guided Document-Level Relation Extraction with LLMs:A Benchmark-Driven Survey of Semantic, Graph-Based,Ontology-Based, and Agentic RAG
- authors: Gabriel Medeiros, Cecilia Zanni-Merk
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7315788
- keyword hits: agentic, large language model, large language models, llm, llms, prompting, retrieval-augmented

### abstract

Document-level relation extraction is a central step for transformingunstructured text into structured knowledge that can support knowledgegraphs, decision support systems, and explainable artificial intelligenceapplications. Recent large language models have made relation extractionmore flexible through zero-shot and few-shot prompting, but their predictionsoften remain weakly grounded, difficult to validate, and sensitive tohallucinations when relations depend on multi-sentence evidence or domainknowledge. In parallel, retrieval-augmented generation, knowledge graphs,ontologies, and agentic workflows have introduced new mechanisms forgrounding, semantic control, and provenance-aware prediction. However,existing surveys usually study relation extraction, retrieval-augmentedgeneration, graph-based retrieval, ontology-guided reasoning, and agenticRAG as separate research lines. This paper addresses this gap through abenchmark-driven survey of knowledge-guided document-level relationextraction with LLMs. It first proposes a taxonomy that organizes methodsinto LLM-only extraction, flat semantic retrieval, ontology-guided RAG,knowledge graph-based RAG, agentic RAG, and validation-orientedneuro-symbolic pipelines. It then introduces RAGTree, a unified benchmarkframework that adapts representative strategies from these families to acommon relation extraction protocol. Experiments are conducted withgpt-oss-20B on MAVEN-ERE, EventStoryLine, FinCausal, DocRED, andCausalBank, using micro-averaged precision, recall, and F1. The observedresults do not identify a single strategy as strongest across all datasets.Ontology-guided, knowledge graph-based, and agentic methods providecomplementary advantages under different dataset conditions, whileretrieval alignment, recall limitations, and orchestration complexityremain open challenges.

---

## uid: `doi:10.2139/ssrn.7271379`

- title: Cross-Model Generalization of Supervised Detectors for AI-Generated Scientific Abstracts
- authors: Sultan BaHammam, Ahmed BaHammam
- affiliations: not stated
- posted: 2026-08-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7271379
- keyword hits: claude, gemini, gpt-4, large language model, large language models, llama

### abstract

Text produced by large language models is difficult to distinguish from human writing by inspection, while deployed detectors usually do not know which model produced the text under review. Most supervised detectors are still trained on output from a single model. This study measures how performance changes when classifiers trained on one source model are applied, without retraining, to text from unseen generators. A balanced corpus of 3,000 arXiv paper titles was stratified across eight academic fields and split 80/20 at the prompt level. Each title prompted one abstract from GPT-4.1, the training source, and from three held-out models: Claude Sonnet 4.5, Gemini 2.5 Flash, and Llama 3.1 8B Instruct. Two detectors were trained on identical rows: a TF-IDF and Logistic Regression pipeline and a fine-tuned RoBERTa-base classifier. Both exceeded 99.7 percent in-domain accuracy. Transfer to unseen sources remained strong: mean cross-model accuracy was 96.92 percent for TF-IDF and 97.86 percent for RoBERTa; the largest observed drop was 5.58 percentage points on Llama 3.1 8B. RoBERTa had the smaller mean generalization gap, 1.97 points compared with 2.83 points for TF-IDF. Because the human subset was identical across test conditions, between-condition changes arose from predictions on the AI-generated subset. The results apply to title-conditioned research abstracts of 100 to 300 words generated with provider-default settings. They do not establish general performance on other genres, adversarially edited text, or abstracts generated from fuller source material.

---

## uid: `doi:10.2139/ssrn.7282318`

- title: Research-AI: An Intelligent Multi-Agent System for Deep Research Document Generation Using Large Language Models
- authors: Nabh Patodi, Tanmay Agarwal, Madhumitha K
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7282318
- keyword hits: gemini, large language model, large language models, llm, llms

### abstract

The rapid advancement of large language models (LLMs) has led to the rise of a new generation of autonomous deep research agents capable of multi-step information gathering and detailed document generation. Existing commercial deep research services, including OpenAI Deep Research, Google Gemini Deep Research and Perplexity Deep Research, perform iterative web search and produce reports from the retrieved information. However, these systems share a fundamental architectural limitation: they rely on a single agent following a linear research path. This makes their outputs susceptible to confirmation bias, model-specific reasoning biases, and incomplete coverage due to the lack of diverse analytical perspectives. Additionally, current systems struggle to generate and maintain complex, multi-level hierarchical document structures. This paper introduces Research-AI, a multi-agent, graph-based research platform that addresses these limitations through a novel multi-perspective synthesis approach. Research-AI orchestrates a four-stage LangGraph workflow: (1) an outline agent generates a detailed hierarchical document blueprint via vector and web search; (2) multiple expert personas with diverse professional backgrounds and ideologies orientations are generated; (3) each expert independently researches and writes the complete document section-by-section, alternating between OpenAI GPT and Google Gemini model families to mitigate model-specific bias; and (4) a synthesis agent integrates all perspectives into a coherent final document. Rolling summarisation of previously generated sections ensures coherence throughout the document. We evaluate Research-AI on DeepResearch Bench, a benchmark of 100 PhD-level research tasks across 22 distinct fields. Research-AI achieves a RACE (Reference-based Adaptive Criteria-driven Evaluation) score of 55.32, ranking first amongst all evaluated systems and outperforming the nearest competitor by 0.78 points, Google Gemini 2.5 Pro Deep Research by 5.61 points, and OpenAI Deep Research (o3) by 8.87 points. The Insight dimension most directly targeted by our approach shows the largest margin over all competitors (59.30, versus the next-best 56.43), demonstrating that architectural diversity outweighs raw model capability for comprehensive research document generation.

---

## uid: `doi:10.2139/ssrn.7309910`

- title: Closing the Loop: Structured Feedback Generation and Validationfor Short Answer Scoring with Large Language Models
- authors: Lei Chen, BoYu Gao, Zitao Liu, Tingjie Wan
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7309910
- keyword hits: gpt-4, large language model, large language models, llama, llm, llms

### abstract

Large language models (LLMs) have shown strong capability in automatic short-answer scoring and feedback generation. However, most existing assessment systems primarily focus on scoring accuracy, while feedback is often treated as an auxiliary output without verifying whether it actually helps students improve their answers. Deploying ineffective feedback may mislead students, whereas manually validating feedback quality is labor-intensive and difficult to scale. To address this, we propose Closed-loop Improvement Learning (CIL), a three-stage framework that integrates LoRA-based short-answer scoring, score-guided structured feedback generation, and automatic feedback-utility verification through simulated answer revision. Experiments on SciEntsBank show that with Llama-3.1-8B-Instruct as the scorer, CIL achieves 0.7405 accuracy on SciEntsBank and 0.6843 on Beetle, improving over the two-prompt baseline by 27.4% and 16.1%, respectively, and outperforming GPT-4o by 1.05% and 3.43% in relative accuracy. The framework generates high-confidence structured feedback with confidence scores of 0.8477 and 0.8242 and 0% format error. Importantly, our verification mechanism automatically evaluates feedback effectiveness, successfully revising up to 43.73% of initially incorrect SciEntsBank answers and 33.49\% of Beetle answers into correct ones. These results demonstrate that CIL improves scoring reliability while providing an efficient and scalable solution for validating the educational usefulness of generated feedback.

---

## uid: `doi:10.2139/ssrn.7307658`

- title: Bias, Fairness, and Inclusivity in Generative AI Systems: A Critical Examination of Algorithmic Bias, Representation Gaps, and the Challenges of Ensuring Equity in AI-Generated Outputs
- authors: Aashay Gupta
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7307658
- keyword hits: generative ai, large language model, large language models, llm, llms

### abstract

Generative AI systems such as large language models (LLMs), image synthesizers, and multimodal frameworks have transformed content creation while also exposing and amplifying systemic biases that undermine fairness and inclusivity. This study critically examines algorithmic bias in model outputs, representation gaps across marginalized demographic groups, and the efficacy of mitigation strategies using data primarily from 2023–2024 benchmark evaluations and fairness research. We draw on established datasets and benchmarks including the HolisticBias descriptor dataset, which covers hundreds of demographic axes to probe stereotyping and toxicity in language models, and demographic face datasets like FairFace designed to balance race, gender, and age representation. Holistic bias evaluations reveal measurable disparities in model behavior across gender, race, disability, and other identity dimensions, illustrating persistent stereotyping and unequal treatment in generated text and image outputs. Gendered occupational associations, for instance, remain prevalent in LLM outputs, while vision models continue to show performance gaps across underrepresented subgroups in facial analysis. Mitigation experiments — including targeted counterfactual data augmentation, bias-aware prompts, and fairness-aware training adjustments — demonstrate reductions in measurable bias, though significant gaps remain, particularly at intersections of identity. Drawing on this analysis, we propose a tripartite framework emphasizing data curation grounded in demographic coverage, systematic model auditing with established bias benchmarks, and stakeholder-informed model design to advance equity in generative AI. Overall, our work integrates empirical bias metrics with design and policy recommendations to support more inclusive and accountable generative systems.

---

## uid: `doi:10.2139/ssrn.7321294`

- title: Generative AI-Based High-Growth Potential Ranking for Portfolio Construction: Evidence from China's Optical Industry
- authors: Yiru Lin, Kaijie Xue
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7321294
- keyword hits: generative ai, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) have been applied to stock screening and portfolio construction, but whether their high-growth potential rankings contain economically valuable stock-selection information within a single industry remains insufficiently tested. This study uses 94 constituents of the Shenwan Optical and Optoelectronics Level-2 Industry as the stock universe and the corresponding Shenwan industry index as the benchmark. Using November 1, 2025 as the ranking date, the same high-growth potential ranking task is conducted through 30 independent API calls. Drawing on the intuition of the law of large numbers, the individual rankings are averaged to form a composite ranking and reduce dependence on any single model output. Based on the composite ranking, this study develops a two-parameter framework, $\tau(p,d)$. Parameter $p$ controls the stock-selection range, while parameter $d$, together with a customized exponential decay weighting function, determines the extent to which portfolio weights are concentrated among higher-ranked stocks. Portfolio performance is evaluated using cumulative return, geometric excess return, the Sharpe Ratio, and the Calmar Ratio. The results show that all LLM portfolios outperform the benchmark across the four performance measures, with portfolios formed from the highest-ranked stocks exhibiting the strongest performance. Increasing the weights assigned to highly ranked stocks further improves the performance of more concentrated portfolios. Random Equal-Weight portfolios and a conditional Monte Carlo randomization test provide further statistical evidence of economically valuable stock-selection information in the LLM ranking. The evidence demonstrates that LLM-generated high-growth potential rankings contain economically valuable cross-sectional stock-selection information within an industry. This information is concentrated toward the top of the ranking, exhibiting a Pareto-like phenomenon. The two-parameter framework and the exponential decay weighting function provide an explicit mechanism for translating LLM rankings into stock selection and portfolio weights.

---

## uid: `arxiv:2608.20320v1`

- title: An Agentic Approach for Active Data Collection, Travel Behavior Modeling, and Weather-Sensitive Demand Prediction
- authors: Narges Ahmadi, Yubo Jiao, Jônatas Augusto Manzolli, Jiangbo Yu, Luis Miranda-Moreno
- affiliations: not stated
- posted: 2026-08-20
- source: arXiv
- link: https://arxiv.org/abs/2608.20320v1
- keyword hits: agentic, large language model, large language models, llm, llms, prompting

### abstract

Travel behavior research increasingly combines digital data collection with predictive modeling, yet these stages are often developed and evaluated separately. This study proposes a three-agent workflow integrating conversational data collection, structured data processing, and behavioral prediction. A chatbot-administered, image-augmented stated-preference survey collected mode choices from student commuters across five predefined weather scenarios, yielding 454 respondent-scenario observations. Weather-related associations were analyzed using a multinomial logit model, while logistic regression and random forest provided machine-learning benchmarks. Nine locally deployed large language models (LLMs), ranging from 2 to 35 billion parameters, were evaluated across four zero-shot prompt-and-context conditions and extended through persona, few-shot, and vision-based configurations. Random forest achieved 69.6% five-class accuracy, while the best text-only zero-shot LLM reached 69.9% without task-specific fitting. Habitual travel information produced the most consistent gains, Expert framing generally outperformed Role-Play, and persona information was most useful when habitual travel information was unavailable. Few-shot prompting improved prediction for several models, with gains stabilizing after a small number of examples. Using the same weather images shown to respondents, the best vision-based configuration reached 71.5% five-class accuracy, indicating that visual context may provide additional predictive information for selected models. Overall, the study shows how conversational surveys, structured data processing, conventional behavioral modeling, machine learning, and multimodal LLM prediction can be coordinated within an auditable multi-agent workflow.

---

## uid: `doi:10.2139/ssrn.7323738`

- title: Predict, Observe, Retrain: Can a Language Model Learn to Pick A/B Test Winners from Its Own Feedback Loop?
- authors: Nathan Clark
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7323738
- keyword hits: fine-tuning, large language model, large language models, llm, llms, prompting, qwen

### abstract

Companies spend a lot of money running A/B tests on headlines, ads, and email subject lines. A model that could predict the winner before the test runs would save much of that money. Recent work suggests large language models (LLMs) can simulate human responses, but most evaluations are one-shot: the model predicts, and that is the end of it. Real deployment would be a loop. The model predicts, the real test runs anyway, the outcome comes back, and the model retrains before predicting the next batch. This paper runs that loop on real data. We take 2,599 headline A/B tests from the Upworthy Research Archive (43 million impressions of real reader behavior), sort them into ten time-ordered rounds, and require every model to predict each round's winners using only outcomes revealed in earlier rounds. We compare a frozen zero-shot LLM, a fewshot prompted LLM, a gradient-boosted trees baseline on text features, and a small LLM (Qwen2.5-3B) that is LoRA fine-tuned from scratch each round on all outcomes revealed so far. The full loop was run twice with independent random seeds. The fine-tuning loop wins clearly. It picks the winner of decisive tests 52.8% of the time on average across the two runs (53.7% and 52.0%) against a 25.6% random baseline, beating the best non-LLM baseline by 15 points in both runs and in every round. The gain arrives almost entirely with the first round of feedback and holds steady, rather than climbing round over round. Zero-shot and few-shot prompting barely beat the trees baseline, echoing prior reports that prompting alone captures little about real preferences. Two checks back the result up. A memorization probe finds the base model cannot reproduce a single archive headline verbatim (0 of 200). And the fine-tuned model transfers: trained only on Upworthy tests, it ranks 1,803 news headlines from the Microsoft MIND dataset with Spearman correlation 0.37 against real click-through rates, where the base model manages 0.04. The loop works, the gains arrive early, and what the model learns is general clickability rather than one site's quirks. But at 53% accuracy on decisive pairs, the model prunes candidate pools; it does not replace testing.

---
