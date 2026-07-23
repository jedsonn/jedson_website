# Classification batch 332 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-332.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6916779`

- title: The Lost Product Layer in AI A Workflow-aware Framework for Moving beyond Chatbot-first AI
- authors: Rahul Gautam
- affiliations: not stated
- posted: 2026-07-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6916779
- keyword hits: large language model, large language models

### abstract

Artificial intelligence has become one of the most powerful technological shifts in software. Large language models can write, summarize, code, classify, search, reason, automate, and assist across many domains. Yet despite this capability, the software industry still has relatively few AI-native products that users rely on deeply, repeatedly, and naturally in their everyday workflows beyond areas such as customer support, coding assistance, writing, search, and chatbot-style interaction. This paper argues that the gap is not primarily a model capability problem, but a product-experience problem. Teams often begin with model capabilities rather than user workflows, producing chatbots, dashboards, agents, summaries, and feature-heavy interfaces that impress in demos but fail to embed in daily practice. The paper introduces the idea of the "lost product layerˮ in AI the weakening of product judgment, user segmentation, interaction discipline, feedback loops, and workflow understanding in AI product development. It proposes Product-Native AI as a conceptual framework for integrating AI into products through stable user experiences, adaptive intelligence, contextual cues, subtle interaction design, product discipline, and real user behavior. The central argument is that AI-native products should not be built by adding AI features everywhere. They should be built by identifying the right user moment, placing intelligence where it naturally belongs, and gradually discovering new workflows through feedback. This paper provides a two-stage adoption pathway, Workflow Fit to Workflow Emergence, and ten operational principles for teams moving from capability-led to workflow-native AI integration.

---

## uid: `arxiv:2607.04096v1`

- title: Forethought: Verifiable Reasoning from Neurosymbolic Primitive Programming
- authors: Vishvesh Bhat, Jay Vaghasiya, Emmanuel Anaya Gonzalez
- affiliations: not stated
- posted: 2026-07-05
- source: arXiv
- link: https://arxiv.org/abs/2607.04096v1
- keyword hits: agentic, prompting

### abstract

Current agentic workflows usually involve decomposing user requests into sequences of tool calls with correctly resolved parameters, the results of which are processed through reasoning traces in the language model's context window. The prevailing route to improve such reasoning is test-time scaling, which trains models to search over long chains of thought; but the resulting capability is entangled in model weights, is not verifiable step-by-step, and is costly at inference. We present Forethought, a neurosymbolic reasoning system that instead treats reasoning as an explicit, verifiable program, that builds from a library of symbolic and neural primitives which are composed through a domain-specific language. The result are reasoning programs, which are concrete representations of the model's work, and as such can be inspected and modified before deployment. Instantiated as a tool-calling execution kernel and evaluated across five benchmarks, Forethought improves base-model accuracy by about 30% relative and outperforms vanilla prompting, reinforcement learning scaffolds, and prompt-evolution methods, enabling small models to match or exceed frontier models capabilities. In a direct comparison, a non-reasoning model augmented with Forethought competes with a dedicated reasoning model while requiring roughly three orders of magnitude less post-training investment, and remains model-agnostic and auditable.

---

## uid: `doi:10.2139/ssrn.7067738`

- title: PyPIGuard: A Lightweight, Explainable Machine Learning Tool for Pre-Install Detection of Malicious PyPI Packages
- authors: Rahat  Ahmed Jobu
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7067738
- keyword hits: llm

### abstract

Open-source package registries such as PyPI are increasingly targeted by at-tackers, yet existing detection tools report false-positive rates as high as 97%,making automated adoption impractical. PyPIGuard is an open-source, de-ployable tool that classifies PyPI packages as malicious or benign withina millisecond, using only static code, Abstract Syntax Tree (AST), andbytecode-level structural features — without relying on a large languagemodel (LLM). It is deployed as a live web application with a real-time scan-ner, a file-upload scanner, and a Jupyter notebook malware-import scanner.Trained on 9,723 real packages — the entire available malicious archive plusfreshly-sampled benign packages — it achieves 0.9993 ROC-AUC on held-outdata and 0.984 ROC-AUC on packages discovered after the training cutoff,remaining robust under adversarial evasion testing.

---

## uid: `doi:10.2139/ssrn.7042778`

- title: The Influence of Artificial Intelligence on Multiple-Choice Question Logic and Guessing Accuracy in Standardized Testing
- authors: Goutam Kanamarlapudi
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7042778
- keyword hits: chatgpt, gemini

### abstract

Multiple-choice questions are widely used because they are efficient, scalable, and easy to score. However, poorly constructed items can allow students to use structural clues instead of content knowledge. This exploratory content analysis examined whether artificial intelligence (AI)generated multiple-choice questions contained more guessing cues than human-created standardized items. A broader pool of 200 AI-generated candidate questions was produced across widely used AI tools, including ChatGPT, Perplexity, and Gemini. From this pool, the researcher randomly selected 30 AI-generated questions for detailed coding: 10 limited-prompt, 10 medium-prompt, and 10 high-prompt items. A comparison sample of 10 released National Assessment of Educational Progress (NAEP) questions was also randomly selected, producing a final coded sample of 40 questions. Each question was coded for seven cue types: unequal answer length, weak distractors, repeated wording, extreme language, grammar clues, an overly clear correct answer, and patterned answer placement. Human-created NAEP questions contained fewer cues than AI-generated items. Only 2 of 10 NAEP questions contained at least one guessing cue, compared with 8 of 10 limited-prompt AI questions, 6 of 10 medium-prompt AI questions, and 5 of 10 high-prompt AI questions. Prompt specificity improved distractor quality and answer clarity, but answer-placement patterns remained common across AI conditions. These findings suggest that AI can assist with assessment drafting, but AI-generated questions should be reviewed before use in classroom or standardized testing.

---

## uid: `doi:10.2139/ssrn.7065100`

- title: Knowledge-Guided Neural-Symbolic Framework with Post-hoc Adaptive Fusion for Sports Sentiment Analysis
- authors: Haitao Wang, Jianliang Guan, Mujuan Zhao, Mengmeng Huang, Tianchi Tong
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7065100
- keyword hits: large language model, llm

### abstract

Sentiment analysis for Chinese sports commentary remains challenging because pure neural models lack domain-specific knowledge, fixed-weight neural-symbolic methods cannot adapt to comment-level variation, and large language model (LLM)-based pipelines are often too slow, costly, and hard to deploy in real-time or privacy-sensitive applications. To address these problems, we propose SportDict-BERT, a parallel three-path neural-symbolic fusion framework. The BERT-LDA path injects a Latent Dirichlet Allocation topic prior into a fine-tuned Chinese-RoBERTa-wwm-ext encoder, the standalone BERT path serves as a topic-agnostic reference, and the Enhanced Sentiment Reasoning path performs rule-based symbolic computation with four explicit reasoning rules over a domain-specific lexicon. A post-hoc trained gating network then performs instance-conditioned fusion through an Adaptive Fusion Strategy. Experiments on the released Sports Comment Dataset-Chinese demonstrate the feasibility and superiority of the proposed method. SportDict-BERT outperforms the RoBERTa-wwm-ext baseline by 3.32% to 5.65% in F1 and consistently surpasses fixed-weight fusion and majority voting baselines, positioning the framework as a locally deployable alternative for sports analytics.

---

## uid: `doi:10.2139/ssrn.6924659`

- title: Cognitive Homophily in Human-AI ensembles: Explaining the Quality-Satisfaction Trade-off
- authors: Vivek Choudhary, Arianna Marchetti, Ella Miron-Spektor, Phanish Puranam, Yash Raj Shrestha, Nety Wu, Yuanjun Feng
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6924659
- keyword hits: gpt-4

### abstract

Human-AI ensembling is increasingly used in creative workflows, yet evidence is limited on two questions central to human behaviour: (i) how ensemble configurations shape psychological ownership and satisfaction with the creative process, and (ii) whether humans and AI evaluate creative outputs differently, thereby steering what is selected and retained through intermediate evaluation in collaborative pipelines. We address these questions in a preregistered online experiment (N = 700) using a controlled interface embedded with GPT-4o. Participants completed the same ideation task (improving Airbnb's business model alignment with the UN Sustainable Development Goals) under one of three dyadic ensemble configurations: Parallel (human and AI generate ideas independently, and their outputs are then integrated), Human-first sequential (AI builds on human-originated ideas), and AI-first sequential (humans build on AI-originated ideas). We evaluate both output quality (via independent human and AI evaluators) and participant self-reported satisfaction. We find a quality-satisfaction trade-off: the Parallel ensemble yields the highest-rated outputs on idea feasibility and alignment with the UN goals, but the human-first ensemble produces greater novelty and yields the highest human satisfaction, consistent with psychological ownership in creative work. The AI-first ensemble performs the worst on both quality and satisfaction. We also document "cognitive homophily," i.e., evaluatordependent selection in idea assessment: human and AI evaluators each preferentially rate ideas generated by their own "type," despite being blind to the generator's identity. Together, these results provide evidence that optimising human-AI team design for output quality can conflict with the human experience of collaboration, and that the evaluator's identity can systematically shape idea selection and the direction of creative work, with implications for the design and governance of human-AI workflows.

---

## uid: `doi:10.2139/ssrn.7067276`

- title: Robotic Environment Manipulation Agents (REMA): A Proactive Multi-Agent Framework for Robust
- authors: Mubashar Saeed
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7067276
- keyword hits: large language model

### abstract

Robotic manipulation is a key capability for autonomous systems, requiring flexible planning and robust execution in dynamic, unstructured environments. Existing large language model based methods primarily rely on reactive replanning after task failures, resulting in inefficiencies and error accumulation during long horizon manipulation. This paper presents Robotic Environment Manipulation Agents (REMA), a proactive multi-agent framework that divides planning, execution, and continuous semantic validation among four specialized agents to detect and incrementally correct deviations in real time. REMA integrates persistent semantic monitoring to prevent failure propagation while preserving prior planning investments through contextaware adaptations. Experimental evaluations on nine diverse RLBench tasks demonstrate that REMA achieves statistically significant improvements in success rates and robustness over state-of-the-art multi-agent baselines, confirming its efficacy for reliable autonomous manipulation.

---

## uid: `doi:10.2139/ssrn.7065101`

- title: Knowledge-Guided Neural-Symbolic Framework with Post-hoc Adaptive Fusion for Sports Sentiment Analysis
- authors: Haitao Wang, Jianliang Guan, Mujuan Zhao, Mengmeng Huang, Tianchi Tong
- affiliations: not stated
- posted: 2026-07-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7065101
- keyword hits: large language model, llm

### abstract

Sentiment analysis for Chinese sports commentary remains challenging because pure neural models lack domain-specific knowledge, fixed-weight neural-symbolic methods cannot adapt to comment-level variation, and large language model (LLM)-based pipelines are often too slow, costly, and hard to deploy in real-time or privacy-sensitive applications. To address these problems, we propose SportDict-BERT, a parallel three-path neural-symbolic fusion framework. The BERT-LDA path injects a Latent Dirichlet Allocation topic prior into a fine-tuned Chinese-RoBERTa-wwm-ext encoder, the standalone BERT path serves as a topic-agnostic reference, and the Enhanced Sentiment Reasoning path performs rule-based symbolic computation with four explicit reasoning rules over a domain-specific lexicon. A post-hoc trained gating network then performs instance-conditioned fusion through an Adaptive Fusion Strategy. Experiments on the released Sports Comment Dataset-Chinese demonstrate the feasibility and superiority of the proposed method. SportDict-BERT outperforms the RoBERTa-wwm-ext baseline by 3.32% to 5.65% in F1 and consistently surpasses fixed-weight fusion and majority voting baselines, positioning the framework as a locally deployable alternative for sports analytics.

---
