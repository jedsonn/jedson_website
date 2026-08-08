# Classification batch 12 of 20, edition 17

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-017/batch-12.answer.json` as a JSON array.

---

## uid: `arxiv:2608.00909v1`

- title: FinHardBench: Can LLMs Generate Latency-Aware Hardware for Financial Computing?
- authors: Weimin Fu, Hejia Zhang, Minghao Shao, Zeng Wang, Johann Knechtel, Ozgur Sinanoglu, Muhammad Shafique, Ramesh Karri
- affiliations: not stated
- posted: 2026-08-02
- source: arXiv
- link: https://arxiv.org/abs/2608.00909v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Can large language models generate not just correct, but fast hardware? This paper investigates the question in financial FPGA design, where 5-10 nanoseconds of latency determines competitive advantage and designs iterate continuously as protocols, strategies, and regulations evolve. FinHardBench, a benchmark of 33 financial computing tasks, is presented together with three experiments that mirror the real-world FPGA iteration cycle: generating new modules from specifications, tuning system-level configurations across a 6-stage trading pipeline, and adapting existing modules to specification changes. Evaluation of six LLMs on 1530+ experiment rounds yields three findings: (1) models achieve 19-61% functional correctness with timing degradation up to 13.7$\times$ on specific tasks; (2) in system-level design space exploration, top LLMs converge to the optimal configuration with higher reliability than random search, simulated annealing, and Bayesian optimization baselines (5/5 seeds vs. 0-4/5 at the same 24-round budget); (3) strategy-level specification changes remain unsolved for most models. Across the six models, generation and DSE rankings overlap moderately: the strongest code generator is not the fastest architecture optimizer, and the weakest code generator (MiniMax M2.7) still reaches the system optimum on 4 of 5 seeds. On the tasks in FinHardBench, difficulty tracks training data pattern availability more closely than abstraction level. FinHardBench is released as an open-source benchmark.

---

## uid: `doi:10.2139/ssrn.7157279`

- title: The Author After Artificial Intelligence: Responsibility, Intertextuality and the Limits of Machine Agency
- authors: Olga Pilate
- affiliations: not stated
- posted: 2026-08-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7157279
- keyword hits: generative ai, generative artificial intelligence, large language model, large language models

### abstract

Abstract The rapid adoption of generative artificial intelligence has transformed authorship from a predominantly theoretical concept into a practical concern for scholars, publishers, educators and legal institutions. While large language models have intensified debates about creativity and textual production, they have also reopened fundamental questions concerning responsibility, originality and intellectual agency. This article argues that the challenges posed by AI are best understood not as unprecedented disruptions but as developments anticipated by twentieth-century literary theory. Revisiting the works of Roland Barthes, Michel Foucault, Julia Kristeva, Mikhail Bakhtin and Gérard Genette, the article demonstrates that generative AI represents a technological realisation of intertextuality, producing texts through the statistical transformation of existing linguistic material rather than through autonomous creative intention. The article integrates insights from literary theory, copyright law and academic publishing ethics to examine whether artificial intelligence can meaningfully be regarded as an author. It argues that current legal doctrine and editorial standards consistently reject machine authorship because authorship is ultimately a normative institution grounded in accountability rather than linguistic production. Applying the methodological principle of Occam's razor, the article further contends that introducing AI as a new category of authorship adds unnecessary conceptual complexity, since existing theories of intertextuality, copyright and academic responsibility already provide an adequate explanatory framework for AI-assisted writing. The central claim advanced is that generative AI does not eliminate the concept of authorship but reveals its essential function more clearly than before. As the production of fluent language becomes increasingly automated, authorship can no longer be understood primarily as the origin of textual expression. Instead, it is more convincingly conceived as the capacity to formulate research questions, exercise intellectual judgement, evaluate evidence and assume responsibility for scholarly knowledge. The article concludes that the future of authorship will depend not on the technological capabilities of artificial intelligence but on the continuing relationship between agency, accountability and the institutional practices through which knowledge is created and validated.

---

## uid: `arxiv:2608.01607v1`

- title: AI Financial Advice: Supply, Demand, and Life Cycle Implications
- authors: Taha Choukhmane, Tim de Silva, Weidong Lin, Matthew Akuzawa
- affiliations: not stated
- posted: 2026-08-03
- source: arXiv
- link: https://arxiv.org/abs/2608.01607v1
- keyword hits: gpt-5, llm, llms

### abstract

We ask a representative sample to write prompts seeking spending and investing advice from LLMs, then simulate the lifetime effects of following the advice under realistic asset and labor market conditions. Applying this method to GPT-5.2, we find following the advice would move respondents toward life cycle theory: broader participation in diversified equity funds, age-declining equity shares, and larger savings buffers. Recommendations vary systematically by gender, prior AI experience, and financial literacy. For gender, two-thirds of recommended equity-share differences arise from men and women writing different prompts (demand), while one-third arise from gender labels attached to otherwise identical prompts (supply).

---

## uid: `arxiv:2608.02947v1`

- title: ATFlash: Per-RoPE-Wavelength Attention Windows for Compute/Memory-Efficient LLM Inference
- authors: Shun-ichiro Hayashi, Daichi Mukunoki, Tetsuya Hoshino, Takahiro Katagiri
- affiliations: not stated
- posted: 2026-08-03
- source: arXiv
- link: https://arxiv.org/abs/2608.02947v1
- keyword hits: llama, llm, qwen

### abstract

The attention score with rotary position embeddings (RoPE) decomposes exactly into a sum over its 2D-rotation frequency pairs, and each pair's wavelength limits how far it can discriminate position. Aligned with this structure, we propose the per-RoPE-wavelength distance window: it prunes the query--key inner-product terms beyond a wavelength-proportional distance. Unlike a sliding window, every key remains reachable, at least through the low-frequency pairs. The reduction rate is input-independent, with a closed form logarithmic in the sequence length $N$, in contrast to dynamic-sparse methods like MInference. Such token-level selection is orthogonal to our frequency-level pruning. The window can therefore be applied on top of those methods. On Qwen2.5-0.5B and Llama-3.2-3B, the window prunes 37--48\% of the query--key inner-product terms within each model's native context length. Relative to full attention, the top-1 match rate stays at 96--98\% and the mean output-distribution KL at the $10^{-3}$-nat level on LongBench-v2 contexts. We examine absolute scores on long-context benchmarks such as RULER, OpenAI-MRCR, LongCodeQA, and $\infty$Bench: they are broadly preserved. We implement the window as a slice of the query--key contraction axis, leaving the online-softmax recurrences untouched, and port it with minimal diffs into the released FlashAttention-4 prefill and FlashInfer decode. On RTX PRO 6000 with Llama, both ports outpace stock with gains growing with context length, up to $1.29\times$ at 128K. End to end on Qwen2.5-7B-1M, with 57\% of the inner-product terms pruned, the speedup reaches $1.31\times$ at a 1M-token context.

---

## uid: `doi:10.2139/ssrn.7228343`

- title: ShuoWen: A Large-Scale Synthetic Dataset for Tongjiazi Extraction in Classical Chinese
- authors: Lili Chang, Yichen Yu, Yong Wang, Chaowen Yan, Tao He
- affiliations: not stated
- posted: 2026-08-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7228343
- keyword hits: large language model, large language models, llm, llms

### abstract

In this paper, we present ShuoWen, a large-scale synthetic dataset designed for Tongjiazi (phonetic loanword) extraction in Classical Chinese, containing over 128,000 samples derived from authoritative linguistic knowledge bases. Unlike existing resources constrained by data scarcity, ShuoWen achieves full coverage of 8,009 canonical Tongjiazi-original character pairs. To address the challenges of data sparsity and homograph ambiguity, we propose a knowledge-injected synthesis framework that integrates dictionary-based expansion with a Hard Negative Mining (HNM) strategy. This approach effectively infuses latent philological expertise into the model while refining semantic boundaries to mitigate the pervasive issue of over-correction, particularly in identifying original character usage. Experimental results demonstrate that training with ShuoWen significantly enhances the model's ability to identify rare, long-tail Tongjiazi instances. Our evaluation on independent benchmarks shows that models fine-tuned with ShuoWen achieve highly competitive performance. Furthermore, we observe that integrating ShuoWen enables general-purpose Large Language Models (LLMs) to better handle the complexities of Classical Chinese, as evidenced by improved performance in high-ambiguity scenarios. We also provide a detailed qualitative analysis of persistent challenges, such as metaphorical semantic shifts and proper noun interference, establishing ShuoWen as a foundational resource for high-precision Classical Chinese NLP. The dataset and code are available at https://github.com/Heshuiao/ShuoWen-Tongjiazi.

---

## uid: `doi:10.2139/ssrn.7231715`

- title: From Runnable to Behaviorally Reliable Models: A Multi-Agent Large Language Model Framework for Automated Modelica Modeling and Repair
- authors: Shutong Feng, Jiasheng Cheng, Ganpeng He, Jianxiang Zheng, Yaoli Zhang
- affiliations: not stated
- posted: 2026-08-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7231715
- keyword hits: large language model, large language models, llm, llms

### abstract

Engineering simulation modeling is a critical engineering activity, yet constructing reliable equation-based simulation models remains labor-intensive and requires substantial domain expertise. Although large language models (LLMs) can generate simulation code from natural-language requirements, generated models may compile and execute successfully while still violating engineering requirements, physical assumptions, or control objectives.This paper proposes a multi-agent LLM framework for automated Modelica modeling, simulation, and behavioral repair. The AI contribution is a closed-loop workflow that combines Modelica code generation, OpenModelica-based execution feedback, domain-aware review, and iterative repair. The engineering application is automated equation-based simulation modeling, where natural-language requirements are transformed into executable and behaviorally reliable Modelica models.Five specialized reviewer agents evaluate parameter consistency, component semantics, equation physicality, control logic, and result behavior to identify hidden errors beyond compilation and simulation success. The framework is evaluated on 20 representative Modelica modeling tasks. Using execution-feedback-based repair alone, all generated models become runnable, but only 16 of 20 achieve correct simulation results and only 8 of 20 satisfy critical behavioral correctness requirements. After multi-agent review and iterative repair, all 20 tasks achieve correct simulation results and critical behavioral correctness. Reviewer-removal experiments further demonstrate the value of specialized reviewers for improving the reliability of AI-generated engineering simulation software.Keywords: Large language models; Multi-agent systems; Modelica; Engineering simulation modeling; Software verification and validation; Behavioral repair

---

## uid: `doi:10.2139/ssrn.7159578`

- title: A Conceptual Reference Architecture for Closed-Loop Intelligent Data Quality Governance
- authors: Hadi Fadlallah
- affiliations: not stated
- posted: 2026-08-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7159578
- keyword hits: agentic, large language model, large language models, retrieval-augmented

### abstract

Data quality assessment is essential for reliable data-driven systems, directly affecting analytics, machine learning performance, operational monitoring, and decision-making. Traditional approaches primarily rely on predefined rules, statistical profiling, and manually engineered validation workflows. Recent advances in machine learning, deep learning, large language models, retrieval-augmented generation, and agentic AI have introduced more adaptive and context-aware validation capabilities. However, existing approaches remain fragmented and typically focus on isolated tasks such as anomaly detection, rule recommendation, executable validation generation, or semantic assessment without providing a unified governance-oriented lifecycle architecture. This paper proposes the Intelligent and Automated Data Quality Assessment Control Framework (IDQACF), a conceptual reference architecture for closed-loop intelligent data quality governance. The framework conceptualizes data quality assessment as a continuous operational and governance lifecycle integrating contextual sensing, knowledge-driven planning, agentic validation, governance verification, deterministic execution, explainability, and adaptive feedback learning. Rather than presenting a production-ready implementation, the framework provides a layered conceptual model intended to guide future research, implementation, and governance standardization for autonomous AI-driven data quality ecosystems. The proposed framework extends recent research on context-aware, retrieval-augmented, and agentic data quality assessment systems. A central design principle is the explicit separation between probabilistic AI reasoning and deterministic executable validation to improve reliability, auditability, explainability, and governance in autonomous assessment workflows. The framework additionally emphasizes policy-aware orchestration, reusable organizational memory, lifecycle-oriented governance, and adaptive operational feedback as core requirements for future intelligent data quality ecosystems.

---

## uid: `doi:10.2139/ssrn.7153718`

- title: Democratizing Legal Knowledge in India Using Retrieval-Augmented Generation: A Scalable Large-Corpus Framework for Legal Question Answering
- authors: Amit Pratap Singh, Manas Pratap Singh, Madhav Sharma, Lakshay Dang, Anju Gera
- affiliations: not stated
- posted: 2026-08-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7153718
- keyword hits: gpt-4, llm, llms, retrieval-augmented, text embedding

### abstract

India’s legal system is vast, complex and fluid, and legal knowledge is difficult for lay citizens to access or interpret amid thousands of statutes, millions of judgments, and constantly evolving legislation. Although LLMs can produce elegant answers, they often hallucinate in the legal domain and are not able to cite authoritative sources reliably. We introduce a Retrieval-Augmented Generation (RAG)-based approach specifically designed for the Indian legal domain, supported by a large structured legal corpus of 45–60 million tokens and a sentence-aware chunking mechanism for creating text embeddings using Instructor-XL, integrating FAISS HNSW for retrieval and GPT-4o for grounded generation. The platform delivers natural-language legal answers with citations and context to help bring legal knowledge into the general populace and enable greater public access to justice. We present the architecture, dataset construction, retrieval pipeline, evaluation methodology, and responsible-AI aspects for robust deployment of legal-domain RAG systems in India.

---
