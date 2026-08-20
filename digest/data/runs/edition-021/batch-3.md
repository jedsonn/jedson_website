# Classification batch 3 of 22, edition 21

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-021/batch-3.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7276704`

- title: HMARL-Pentest: Towards Autonomous Web Application Penetration Testing via LLM-Guided Multi-Agent Reinforcement Learning and Semantic Attack Memory
- authors: ilias CHARCHAOUI, Abdelhamid Zouhair, Ikram Ben Abdel Ouahab
- affiliations: not stated
- posted: 2026-08-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7276704
- keyword hits: ai agent, deepseek, gemini, gpt-4, large language model, llm, retrieval augmented

### abstract

Existing automated penetration testing frameworks commit exclusively to either reinforcement learning without contextual reasoning, simple AI agents, or large language model-driven pipelines without learned execution policies that improve through experience, leaving a critical gap in the capacity to autonomously assess heterogeneous web application environments. This paper presents HMARL-Pentest, a hierarchical multi-agent reinforcement learning framework for autonomous web application penetration testing, integrating trained RL specialist agents, LLM based strategic orchestration, and a retrieval augmented generation semantic memory layer. The framework introduces LLM Guided Policy Optimization, a novel interaction paradigm in which the LLM intervenes selectively when RL policy entropy exceeds a principled confidence threshold, acting as a curriculum teacher that recedes as agent competence increases. Six specialist PPO agents were trained under a multi target curriculum spanning PHP, Java, and Node.js architectures and deployed against three intentionally vulnerable web applications: DVWA, OWASP WebGoat, and OWASP Juice Shop. Across 45 experimental episodes, the framework achieves 100% exploitation success on all three targets, while exclusively generating MITRE ATT&CK-mapped semantic intelligence inaccessible to random and RL-only baselines. A diversity aware evaluation across three LLM backbones: GPT-4o-mini, DeepSeek-R1, and Gemini 2.5 Flash-Lite reveals that reasoning model depth positively correlates with hint follow rate, with DeepSeek-R1 achieving 21% agent adoption and the highest exploitation reward on structurally complex targets. An emergent self regulating property is identified: LLM guidance contribution scales with target architectural novelty, providing empirical support for the curriculum teacher hypothesis.

---

## uid: `doi:10.2139/ssrn.7245280`

- title: Towards an Agentic Era of AI
- authors: Tianyu Liu, Dingyuan Dai, Weihao Xuan, Jialin Chen, Qingcheng Zeng, Rui Yang, Ada Fang, Zhen Yang
- affiliations: not stated
- posted: 2026-08-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7245280
- keyword hits: agentic, ai agent, large language model, large language models, llm, llms

### abstract

Agents developed using large language models (LLMs) and multimodal large language models (MLLMs) have brought about revolutionary changes across multiple fields, significantly boost ing productivity and enthusiasm for artificial intelligence (AI). The design of effective AI agents has traditionally been treated as an engineering-centered problem, with most approaches relying heavily on human expertise and empirical trial and error. However, a systematic examination of high-performing AI agents reveals recurring design patterns from which generalizable principles for building agentic systems can be derived. Motivated by this observation, we trace the evo lution of AI agent design, review major categories and applications, identify recurring patterns among prominent AI agents, and synthesize their core architectural components into four func tional contracts: memory and state management, observation-action interface, reasoning, and runtime control. Furthermore, we propose a better agentic AI framework by following five prin ciples: grounding, autonomy, modularity, efficiency, and robustness. Our framework covers the most critical components of the agentic AI ecosystem design and provides advanced guidance for the healthy operation of agents. We conclude by discussing emerging directions and offering recommendations for the development and deployment of future AI agents. In summary, the design of AI agents requires not only engineering ingenuity but also scientific guidance.

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

## uid: `doi:10.2139/ssrn.7257138`

- title: Mapping Research Preparedness in Higher Education in the Age of Artificial Intelligence: A Bibliometric Analysis
- authors: Stephen Naul, Nancy Francisco
- affiliations: not stated
- posted: 2026-08-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7257138
- keyword hits: chatgpt, generative ai, generative artificial intelligence, large language model, large language models, prompt engineering

### abstract

Although studies have examined artificial intelligence, generative AI, and related educational applications, the literature relevant to research preparedness in higher education remains conceptually dispersed across interconnected areas of inquiry. This study mapped the scientific landscape of research preparedness in higher education in the age of artificial intelligence through a bibliometric analysis of Scopus-indexed publications. Using a PRISMA-guided bibliometric workflow, an initial set of 4,960 records was refined through systematic database filtering, data cleaning, relevance screening, and keyword harmonization, resulting in a final dataset of 1,604 journal articles published from 2017 to 2025. Performance analysis and science mapping were conducted using Bibliometrix through the Biblioshiny interface in R, supported by VOSviewer for co-authorship and keyword co-occurrence visualization. The findings reveal a sharp increase in publications, particularly from 2023 to 2025, reflecting the rapid scholarly response to generative artificial intelligence, ChatGPT, large language models, and AI-supported academic tools. The United States, China, the United Kingdom, Australia, Indonesia, and Hong Kong emerged as major contributors, while leading institutions and journals showed the interdisciplinary nature of the retrieved literature across education, educational technology, sustainability, and digital learning. Highly cited documents focused on generative AI, student perceptions, assessment, AI policy, academic integrity, and ethical risks. Collaboration patterns showed growing international engagement, although knowledge production remains concentrated among major research-producing countries. Thematic and keyword analyses identified key clusters related to AI and ChatGPT in higher education, technology acceptance, digital literacy, prompt engineering, academic integrity, curriculum innovation, and institutional preparedness. Overall, the study shows that research at the intersection of research preparedness, artificial intelligence, and higher education is rapidly expanding and thematically interconnected, although the conceptual structure of the literature remains dispersed and is still consolidating. These findings provide an evidence-based foundation for greater theoretical and methodological integration and for institutional decision-making aimed at strengthening research preparedness in AI-enabled higher education.

---

## uid: `doi:10.2139/ssrn.7277231`

- title: HECTOR: A Framework for Detecting and Mitigating Context- Conflicting Hallucinations in LLM–Based Java-C++ Code Translation
- authors: Srinuvasa  Rao Maddila, Umamaheswara Sharma B
- affiliations: not stated
- posted: 2026-08-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7277231
- keyword hits: fine-tuning, large language model, large language models, llama, llm, llms

### abstract

Large Language Models (LLMs) are widely used for code generation and translation. However, they often produce context-related errors such as repetition, dead code, inconsistencies, and missing logic, which reduce code quality. To mitigate this problem, we designed a translation-detection-generation framework that first translates the source code into the target language, detects context-conflicting hallucinations using machine learning, and refines the translated code using a fine-tuned LLM and code analysis techniques. Our work also employs context-aware hallucination injection for training data generation, followed by fine-tuning StarCoder2-15B, CodeLLaMA-7B, and CodeGen-2B-Multi models using LoRA (Low-Rank Adaptation) for both translation and correction (generation) tasks. The performances are measured using the AST-based similarity metric, Pass@k, and CodeBLEU metrics across various translation models. The proposed framework demonstrates improvements in hallucination detection and mitigation across multiple code translation scenarios. The SVM-based classifier achieved approximately 73.2% accuracy using extracted code metrics. Evaluation using AST similarity, Pass@k, and CodeBLEU on 83 program samples shows improvements of up to 8.9%, 7.6%, and 6.7%, respectively, when the StarCoder2-15B model is employed in the proposed framework, compared with other fine-tuned models.

---
