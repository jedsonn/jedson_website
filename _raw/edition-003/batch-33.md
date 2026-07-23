# Classification batch 33 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-33.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7090112`

- title: Retrieval-Augmented Generative AI for Analyzing Entrepreneurship in Africa
- authors: Roy  Ngu Esibe, Muhammad Aliyu, Jesse Thornburg, Erik Stam, João Barros
- affiliations: not stated
- posted: 2026-07-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7090112
- keyword hits: generative ai, large language model, large language models, llm, llms, retrieval-augmented

### abstract

Systematic knowledge about entrepreneurship in Africa and other emerging economies is constrained by a structural lack of data. However, the processes through which founders build high-growth ventures are richly documented in informal digital sources, including YouTube interviews, podcasts, and recorded conference appearances. These digital sources have been unanalyzable at scale until now. This paper presents a validated, scalable methodology based on retrieval-augmented generation (RAG) and large language models (LLMs) for reconstructing entrepreneurial journeys from fragmented multimodal content. We apply the methodology to the 16 founders of Africa’s six unicorn ventures as of 2024, processing over 1,000 YouTube videos and 9 hours of podcast audio into more than 30,000 embedded text chunks. The pipeline integrates multi-query expansion, semantic retrieval, structured narrative generation, and a refinement stage that iteratively improves factual grounding and removes unsupported claims. It is evaluated using precision, recall, F1, and faithfulness. We introduce the Context Completeness Score (CCS), a novel metric that assesses the causal and thematic depth of generated narratives beyond standard faithfulness measures. Results demonstrate high-fidelity narratives with faithfulness scores of 0.94 to 0.99. A key finding is that narrative quality depends more on thematic diversity than on data volume: reliable narratives are achievable with 800 to 1,200 well-curated text chunks. The methodology enables systematic analysis of entrepreneurial journeys in data-sparse contexts, opening a new empirical pathway for entrepreneurship research in Africa and other emerging economies.

---

## uid: `arxiv:2607.08395v1`

- title: Token-Flow Firewall: Semantic Runtime Auditing for Persistent AI Agents
- authors: Puji Wang, Yingchen Zhang, Ruqing Zhang, Jiafeng Guo, Xueqi Cheng
- affiliations: not stated
- posted: 2026-07-09
- source: arXiv
- link: https://arxiv.org/abs/2607.08395v1
- keyword hits: ai agent, large language model, large language models, llm, llms

### abstract

Persistent AI agents extend large language models (LLMs) beyond single-turn interaction into long-lived software systems. Unlike traditional chat assistants, unsafe content in these agents can propagate through persistent state, reusable skills, and tool-mediated interactions, creating a substantially larger semantic attack surface. We observe that most security-critical interactions in such agents are transmitted through natural-language token flows, including memory updates, tool arguments, retrieved files, and inter-component communications. This observation enables a new security formulation: unsafe behavior can be intercepted as risky semantic flows before reaching privileged runtime sinks. Based on this insight, we propose TokenWall, a runtime defense framework that acts as a semantic firewall over agent token flows. TokenWall performs boundary-aware semantic auditing over these flows, constructing structured source-sink audit records, applying lightweight local inspection before execution, and selectively escalating ambiguous high-risk cases to stronger arbitration modules. Unlike prior approaches that rely on sparse auditing or remote large-model oversight, TokenWall enables full-coverage pre-execution mediation while reducing remote arbitration and latency. Experiments on CIK-Bench show that TokenWall reduces attack success rate to 12.5% while maintaining a 97.4% benign executable pass rate without human confirmation. TokenWall further introduces only 0.69 seconds of additional latency on benign cases, demonstrating that semantic runtime containment can achieve a practical security-utility trade-off for persistent AI agents.

---

## uid: `arxiv:2607.13069v1`

- title: Interventional Grounding Audits: Black-Box Premise-Dependency Tests for LLM Chain-of-Thought via Predicate Substitution
- authors: Hironao Nakamura
- affiliations: not stated
- posted: 2026-07-11
- source: arXiv
- link: https://arxiv.org/abs/2607.13069v1
- keyword hits: chain-of-thought, gpt-4, large language model, large language models, llm

### abstract

Large language models produce chain-of-thought (CoT) reasoning that appears logically sound yet may not genuinely depend on its stated premises. We introduce interventional grounding audits, a black-box, step-level test of premise dependency: we intervene on a single premise by substituting its target predicate with a fresh symbol, re-run the model, and check whether each reasoning step's normalized conclusion (canonical predicate form) changes. We evaluate on ProntoQA, a synthetic multi-hop deductive reasoning benchmark with gold proof trees, where step-level premise dependencies are known. Applied to 50 ProntoQA problems with GPT-4o, our method achieves F1 = 0.806 on detecting proof-tree dependencies (F1 = 0.885 on predicate-determining dependencies; Recall = 100%), significantly outperforming a self-consistency baseline (F1 = 0.343; 95% bootstrap CIs non-overlapping). We further identify that 66% of correctly-solved problems contain at least one aligned step insensitive to a direct proof-tree dependency under consistent substitution -- all involving entity-introduction premises, a documented blind spot of the consistent-substitution evaluator -- a "right answer, wrong reasoning" signal invisible to passive methods. All audit certificates, raw outputs, and reproduction scripts are available in a public GitHub repository, and we discuss scope limits beyond formal, parsable benchmarks.

---

## uid: `doi:10.2139/ssrn.7113411`

- title: Stripping Away the Façade: Fake Review Detection in Turkish E-Commerce via Multi-Source Synthetic Data
- authors: Arzu Karataş, Ramin Abbaszadi
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7113411
- keyword hits: instruction-tuned, large language model, large language models, llama, mistral, qwen

### abstract

This study investigates fake review detection in Turkish e-commerce through a large-scale, multi-source synthetic data framework. A balanced corpus of 450,000 samples was constructed, comprising 225,000 authentic product reviews from Hepsiburada and 225,000 synthetic fake reviews. The synthetic reviews were generated using seven methods across five families: Markov chains, Frankenstein recombination, back-translation, fine-tuned GPT-2, and instruction-tuned large language models(Qwen2,LLaMA-3,Mistral).SixTurkishtransformermodels—ElecTRa, BERTurk, BERTurk-128k, ConvBERTurk, ConvBERTurk-mC4, and DistilBERTurk—were evaluated under a statistically rigorous protocol employing five independent random seeds, McNemar’s tests, and Fisher’s combination method. ElecTRa demonstrated the highest in distribution performance (F1 = 0.9940 ± 0.0006), while BERTurk-128k achieved the best results on the external held-out evaluation set (Accuracy = 0.9426 ± 0.0074). The observed divergence between in-distribution and out-of-distribution performance underscores important considerations for production system design. Controlled ablation experiments established that multi-source synthetic diversity is a substantive methodological requirement, with performance consistently improving as generation variety increased. The dataset and code are publicly available

---

## uid: `doi:10.2139/ssrn.6956641`

- title: Secure Prompt Engineering: A Practical Framework for Mitigating Prompt Injection and Data Leakage in LLM-based Systems
- authors: Gustavo Viana
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6956641
- keyword hits: large language model, large language models, llama, llm, llms, prompt engineering

### abstract

Large Language Models (LLMs) are increasingly deployed in production systems, yet their prompt-based interaction paradigm introduces a novel attack surface encompassing prompt injection, instruction hijacking, and sensitive data leakage. This paper proposes and empirically evaluates the Secure Prompt Engineering Framework (SPEF), a four-layer, application-level defensive architecture designed to operate under black-box API conditions without requiring access to model weights or training pipelines. We conducted a controlled experiment using Llama-3.3-70B (via Groq API) with a standardized adversarial corpus of 85 test cases across six attack categories, totaling 170 model interactions (85 per condition). Results demonstrate that full SPEF deployment reduces the overall Attack Success Rate (ASR) from 17.6% to 2.4%-an 86.4% relative reduction-achieving complete mitigation (0.0% ASR) in the Indirect Injection and Role Reassignment categories. Critically, this paper documents both a failed initial implementation and the corrected version, providing a methodologically transparent account of how framework design errors were diagnosed and resolved. We further identify scorer validity as a primary methodological concern in adversarial LLM evaluation, demonstrating that naive keyword-based scoring introduces substantial false-positive contamination. All code, corpus, and raw results are released as open-source artifacts at github.com/gugacyber/spef_experiment.

---

## uid: `doi:10.2139/ssrn.7089478`

- title: Generating Stack Overflow Post Edits with LLMs: A Taxonomy-Driven Evaluation
- authors: Mehedi Hasan Shanto, Muhammad Asaduzzaman, Md Ahsanuzzaman, Alioune Ngom
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7089478
- keyword hits: chain-of-thought, fine-tuning, foundation model, llm, llms, prompting

### abstract

Background. Stack Overflow (SO) relies on community editing to maintain post quality. Prior work on automated SO post editing either focuses narrowly on grammatical error fixing [1] or requires an external signal such as a comment to trigger edit generation [2]. No study has investigated how effectively foundation models and fine-tuning techniques generate SO post edits across different edit types without any external signal. Objective. We will investigate the effectiveness of foundation models and fine-tuning techniques in generating SO post edits across different edit types, using a data-driven edit benchmark as the primary evaluation criterion. Method. We will collect accepted SO post edits from posts tagged with the top-5 programming languages (Python, JavaScript, Java, C#, and C++) with at least one positive vote, using the Posts, PostHistory, and Votes tables from the January 2025 Stack Overflow Data Dump. We will randomly sample 5,000 edits and perform manual open card sorting, in which two annotators will inductively construct a taxonomy of SO edit types. Single-line change instances will be documented as atomic representatives of each category. Each edit instance will then be assigned to a taxonomy category, enabling a benchmark analysis of model performance. We evaluate foundation models under zero-shot, few-shot, and chain-of-thought prompting strategies across different edit types. We then compare different fine-tuning techniques adopted from Lin et al. [3] against the best foundation model strategy, measuring per-category resolution rates alongside automated metrics (BLEU, ROUGE-L, BERTScore, GLEU). Finally, we conduct a human study to assess the quality of the edits generated by the best-performing model.

---

## uid: `doi:10.2139/ssrn.7102064`

- title: Structured Knowledge Transfer in Language Model Distillation: A Graph-Guided Framework for Verifiable Compression
- authors: Miguel Feles, German Combariza
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7102064
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Knowledge graphs are structured, auditable repositories of relational facts that can serve as verification signals in machine learning pipelines. We exploit this property to address a structural blind spot in knowledge distillation, the dominant paradigm for compressing large language models (LLMs) into compact deployable students. Classical distillation optimizes fidelity to a teacher's output distribution without reference to external truth: when the teacher hallucinates with high confidence, the student treats these factual errors as patterns to replicate. We introduce a graph-guided distillation framework in which a Wikidata knowledge graph (KG) acts as a symbolic verification layer over the compression pipeline. Candidate teacher responses are reranked by their consistency with verified Wikidata triples, so that the preference signal driving the student is grounded in auditable relational facts rather than the teacher's unverified token probabilities. This KG-guided preference learning constitutes the core contribution, layered on top of standard supervised fine-tuning and Direct Preference Optimization (DPO).We instantiate the framework by compressing a 31-billion-parameter teacher into a 700-million-parameter student (~42:1 ratio), using a curated subgraph. Evaluation on 500 held-out queries under three controlled conditions shows that KG-guided DPO achieves a statistically significant KG-Recall improvement of +0.039 (+12.9% relative; p

---

## uid: `doi:10.2139/ssrn.7102846`

- title: Bridging Consumer Sentiment and Advertising Content Generation: A Retrieval-Augmented Pipeline for Aspect-Grounded Advertising
- authors: Nouha Hajji
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7102846
- keyword hits: gemini, large language model, large language models, llm, llms, retrieval-augmented

### abstract

E-commerce platforms accumulate vast volumes of consumer reviews that encode fine-grained,aspect-specific opinions rarely exploited by existing marketing-automation systems. Currentadvertising content generation approaches either collapse this richness into a single document-level polarity label or prompt large language models (LLMs) without any grounding mechanism,producing fluent but consumer-disconnected copy. This paper proposes and evaluates anautomated pipeline that converts consumer product reviews into two complementary marketingoutputs, a targeted advertisement and a structured five-section marketing strategy report, byintegrating four analytical components. A DeBERTa-v3 model fine-tuned on SemEval Aspect-Based Sentiment Analysis (ABSA) benchmarks extracts aspect-sentiment pairs from 1,000verified Amazon reviews through a novel hybrid lexical-semantic detection gate, achieving a45.4% aspect-detection rate and recovering 33.4% of all detected aspects through semanticmatching alone, that is, from reviews containing no literal keyword match. Zero-shot BART-large-MNLI intent classification assigns a communicative intent to every review and derives adataset-level tone signal. A FAISS-based aspect-aware retrieval mechanism filters candidateevidence by identified aspect and sentiment polarity before semantic ranking, in contrastto standard Retrieval-Augmented Generation (RAG), which ranks by topic similarity alone.Marketing content is generated with Gemini 2.5 Flash and evaluated with an LLM-as-judgeprotocol across six quality, specificity, and alignment dimensions in a single-run pilot evaluationspanning three product categories. The proposed pipeline (Model C) substantially outperformsa no-analysis LLM baseline (Model A) and a standard semantic-RAG baseline (Model B)on every metric in this pilot: mean groundedness 7.33/10 versus 1.33/10 for both baselines,reassurance quality 9.33 versus 3.67 and 4.33, hallucination avoidance 8.33 versus 1.00 and1.33, and specificity 7.33 versus 2.00 and 1.33. Notably, the two baselines obtain numericallyidentical groundedness scores in this sample, suggesting that unfiltered semantic retrieval mayprovide no practical benefit over no retrieval at all for targeted complaint resolution, a patternconsistent across all three categories though not yet tested for statistical significance given thesmall sample. The pipeline generalises to an out-of-domain Yelp corpus with a comparable,if lower, detection rate, supporting its cross-domain applicability. These preliminary findingssuggest that aspect-aware retrieval, rather than retrieval per se, may be a necessary ingredient forconsumer-grounded marketing-content generation; we present this as a pilot study motivatinglarger-scale, statistically powered follow-up evaluation

---
