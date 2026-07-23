# Classification batch 17 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-17.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6604379`

- title: MineTalk AI: A Novel Multi-Model Architecture and Persistent Emotional Memory Framework for Addressing Chronic Isolation
- authors: Maozhe Wang
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6604379
- keyword hits: chatgpt, claude, gemini, gpt-4, llm, llms

### abstract

Chronic isolation-defined as a sustained, pathological absence of meaningful social connection persisting across weeks or months rather than situational or transient periods-is a clinically distinct and measurable public health emergency. Across a synthesis of eleven major epidemiological studies published between 2003 and 2023 (combined N > 600,000 adults), the prevalence of clinically significant chronic isolation in the United States is estimated at approximately 22-46% of the adult population, equivalent to between 58 million and 122 million individuals experiencing meaningful disconnection on a regular basis [1-5, 10-12]. The health consequences are independently established across mortality, cognitive, immunological, and psychiatric pathways [6-9]. Existing AI conversational systems-including OpenAI's ChatGPT (GPT-4o), Anthropic's Claude, and Google's Gemini-provide within-session emotional support and retain user-provided facts across sessions; however, none were architecturally designed with persistent cross-session emotional memory, longitudinal relationship modeling, or clinically-informed proactive outreach as primary engineering goals [13, 14, 25]. This is a meaningful architectural and purposive distinction, not a general capability claim. This paper presents MineTalk AI, an emotionally intelligent companion designed for chronic isolation, and six primary technical contributions: (1) a persistent emotional memory architecture with sleep-informed consolidation over a 12-month horizon; (2) a dynamic cross-provider routing framework (ExpertRouter) synthesizing responses from three frontier LLMs in real time; (3) an emotional trajectory engine computing longitudinal baseline with trend classification; (4) a proactive memory-triggering system operationalizing perceived partner responsiveness; (5) a gender-differentiated response layer grounded in meta-analytic communication research; and (6) an algorithmic determinism constraint layer (Digital Brakes) preventing harmful outputs.

---

## uid: `doi:10.2139/ssrn.6672588`

- title: VirtualLab_CC: An LLM-Augmented Virtual Laboratory for Automated Computational Chemistry Research
- authors: Martina Kieninger, Marc  E. Segovia, Mauricio  A. Vega-Teijido, Aline Katz, Anabela Martinez, Elena Vuan, Kenneth Irving, Oscar  N. Ventura
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6672588
- keyword hits: claude, large language model, large language models, llm, llms

### abstract

Recent advances in large language models (LLMs) have opened new avenues for automating scientific research workflows. Systems like the AI Scientist [1] demonstrate fully autonomous end-to-end research pipelines for machine learning, but their applicability to domains requiring expensive high-performance computing (HPC) resources, specialized quantum chemistry software, and rigorous thermochemical accuracy remains unexplored. Here we present VirtualLab_CC, a hybrid LLM-augmented virtual laboratory for computational chemistry that integrates Claude (Anthropic) as an orchestration layer with a multi-agent architecture, gated lifecycle management, and bidirectional HPC cluster synchronization. Unlike fully autonomous systems, VirtualLab_CC enforces human-in-the-loop quality gates at every critical decision point while automating routine operations: conformer searches, input generation, job submission and monitoring, output parsing, failure diagnosis, and manuscript preparation. The system manages 21 specialized skills spanning literature review, cluster operations, result extraction, novelty verification, AI-assisted peer review, and citation validation. We demonstrate VirtualLab_CC on a prototype case study of 1,3-dipolar cycloadditions between stabilized Criegee intermediates and biogenic terpene dipolarophiles, involving 17 molecular species, 34 conformers, and over 100 SLURM jobs across multiple calculation stages. The system successfully identified and auto-corrected cluster failures, detected a methodological anomaly (a suspiciously low dioxirane barrier requiring IRC verification), and coordinated multi-method validation across three DFT functionals. VirtualLab_CC bridges the gap between fully autonomous AI research and the rigorous quality control demands of computational chemistry, providing a practical framework for LLM-augmented scientific workflows in resource-constrained HPC environments.

---

## uid: `doi:10.2139/ssrn.6647800`

- title: Tool-Augmented Large Language Model Agents for Analysis: A Focused Study
- authors: Haoran Dong
- affiliations: not stated
- posted: 2026-05-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6647800
- keyword hits: ai agent, large language model, large language models, llm, llms, retrieval-augmented

### abstract

The integration of large language models (LLMs) with external tools has catalyzed a paradigm shift in automating statistical data analysis. Unlike general-purpose AI agents, tool-augmented statistical agents must navigate the intricate interplay between probabilistic reasoning, domain-specic computing ecosystems, and rigorous reproducibility standards. This study provides a focused review of recent advances in tool-augmented LLM agents tailored for statistics and data science. We examine three core architectural paradigmscode generation, retrieval-augmented generation, and interactive tool useand analyze their respective strengths in addressing statistical inference tasks. Particular emphasis is placed on the integration of LLM agents with the R statistical ecosystem, the challenges of evaluating agents on real-world data science problems, and the emerging benchmark suites designed to measure statistical reasoning delity. We additionally propose a taxonomy that classies existing systems along the dimensions of reasoning depth, tool interface granularity, and knowledge grounding strategy, oering a structured lens through which to assess the maturity of the eld.

---

## uid: `doi:10.2139/ssrn.6648978`

- title: Code-First vs LLM-First Architectures: A Hybrid Approach for Scalable and Reliable AI Systems
- authors: Swapneswar Sundar Rray
- affiliations: not stated
- posted: 2026-05-05
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6648978
- keyword hits: agentic, large language model, large language models, llm, llms, retrieval-augmented

### abstract

The rapid adoption of Large Language Models (LLMs) in enterprise software systems has introduced a new class of architectural challenges related to reliability, scalability, interpretability, and operational control. While LLM-first approaches-where core application logic is embedded within prompt-driven model interactions-enable rapid prototyping and flexible behavior, they often degrade under increasing task complexity, resulting in higher hallucination rates, inconsistent outputs, and limited observability in production environments. This paper presents a comprehensive comparative analysis of LLM-first and code-first architectural paradigms for AI system design, grounded in practical implementation insights from enterprise-scale applications. We identify a critical limitation in LLM-first systems, referred to as "LLM cognitive load," where overloading a single model invocation with multiple responsibilities-such as validation, transformation, reasoning, and formatting-leads to degraded performance and unpredictable system behavior. To address these limitations, we propose a hybrid architectural framework that combines deterministic, code-driven control layers with modular LLM-based reasoning components. The proposed approach decomposes complex workflows into smaller, well-defined stages, including input validation, task routing, structured LLM invocation, and post-processing. This separation of concerns enables improved control flow management, reduces ambiguity in model interactions, and enhances system observability. Empirical observations from real-world deployments indicate that the hybrid architecture improves response consistency by up to 35 percent, reduces hallucination rates across multistep workflows, and significantly enhances debuggability and maintainability. Furthermore, the modular design allows for easier integration with emerging paradigms such as Retrieval-Augmented Generation (RAG) and multi-agent orchestration frameworks, supporting the evolution toward Agentic AI systems. The findings demonstrate that effective integration of LLMs requires an architecture-first approach, where models are treated as probabilistic reasoning components within a broader deterministic system. This work contributes a practical design methodology for building scalable, production-ready AI systems and provides foundational insights into the development of autonomous, self-adaptive enterprise architectures.

---

## uid: `doi:10.2139/ssrn.6731321`

- title: FGDM: Reasoning Aware Multi-Agentic Framework for Software Bug Detection using Chain of Thought and Tree of Thought Prompting
- authors: Srita Padmanabhuni, Bhargavi Karuturi, Jerusha  Karen Indupalli, Santhan  Reddy Chilla, Yelleti Vivek
- affiliations: not stated
- posted: 2026-05-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6731321
- keyword hits: agentic, chain of thought, chain-of-thought, large language model, large language models, llm, llms, prompting

### abstract

Deep Learning methods are becoming prominent in automated software bug detection; however, they lack the global understanding of the given code. Consequently, their performance tends to degrade, especially when they are applied to large interconnected code bases or complex modular programs. Recently, Large Language Models (LLMs) have proven to be effective at capturing dependencies among multiple interconnected modules in the codebase. This motivated us to propose the Flow-Graph-Driven Multi-Agent Framework (FGDM), which is composed of four agents that operate in a sequential manner. The framework converts the received code to a flow graph, identifies the erroneous segments, and further generates the repaired code. All the employed agents utilize Chain-of-Thought (COT) and Tree-of-Thoughts (TOT) prompts. Additionally, we also integrated with the FAISS vector database to retrieve similar previous bugs and their repairs. We demonstrated the efficacy of the proposed framework over 100 programs from several projects, including Ansible, Black, FastAPI, Keras, Luigi, Matplotlib, Pandas, Scrapy, SpaCy, and Tornado in both C and Python programs. Our experiments demonstrate that the FGDM outperforms the extant approaches and yielded reductions with a mean of 24.33 and 8.37 in Levenshtein distance and similarities of 0.951 and 0.974 in cosine similarity for Python and C, respectively.

---

## uid: `doi:10.2139/ssrn.6728899`

- title: The Finance Value Pyramid: A Conceptual Framework for Repositioning Value Creation in Finance in the Era of Generative AI
- authors: BAYU ISTANTORO
- affiliations: not stated
- posted: 2026-05-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6728899
- keyword hits: generative ai, large language model, large language models, llm, llms

### abstract

This paper introduces the Finance Value Pyramid a three-level conceptual framework that classifies finance function activities according to their strategic value contribution: Data Work (Level 1), Analytical Work (Level 2), and Narrative Work (Level 3). Unlike prior finance-transformation research that focuses primarily on technical efficiency, this article argues that the emergence of generative AI and large language models (LLMs) accentuates a pre-existing value asymmetry: LLMs substantially automate Data Work (Eloundou et al., 2024), augment Analytical Work while preserving human interpretive judgment (Yigitbasioglu et al., 2023), and leave Narrative Work—the highest-value domain—as the most resilient human advantage. Through critical synthesis of three literature domains—decision usefulness theory (Beaver, 1968; IASB, 2018), the evolution of management accounting toward business partnering (Lambert & Sponem, 2012; Goretzki & Messner, 2019), and AI impact on cognitive work (Frey & Osborne, 2017; Eloundou et al., 2024)—the framework derives each pyramid level analytically from decision-usefulness criteria and proposes an extension of that theory to incorporate narrative translation as an explicit dimension of actual usefulness. Three conceptual propositions are advanced together with a falsifiable empirical research agenda.

---

## uid: `doi:10.2139/ssrn.6738599`

- title: Beyond Words: The Risks of Generative Interpretation
- authors: Jonathan Scher
- affiliations: not stated
- posted: 2026-05-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6738599
- keyword hits: chatgpt, gpt-4, large language model, large language models, llm, llms

### abstract

Judges are beginning to use large language models like ChatGPT to interpret legal texts. This Note examines whether they should do so. Prior studies testing LLMs as legal interpreters use survey responses as benchmarks for performance. I offer the first study comparing LLM interpretations to real-world judicial decisions. Across eight Ninth Circuit cases, I test whether GPT-4 Turbo (a model of ChatGPT) correctly identifies legal text as ambiguous or unambiguous. I find that ChatGPT's assessments diverged from the court's determinations 50% of the time. I then advance a novel argument: judicial reliance on LLMs may constitute improper ex parte communication under current judicial ethics rules.

---

## uid: `doi:10.2139/ssrn.6705699`

- title: The Abductive Hypothesis Engine: Evolving Observational Causal Inference
- authors: Martin Trajkow
- affiliations: not stated
- posted: 2026-05-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6705699
- keyword hits: large language model, large language models, llm, llms, prompting, retrieval-augmented

### abstract

We propose the Abductive Hypothesis Engine, a structural departure from traditional Retrieval-Augmented Generation (RAG) and runtime neuro-symbolic prompting. Current Large Language Models (LLMs) struggle with real-world causal inference because they conflate hypothesis generation with verification, relying on fuzzy linguistic semantics that are highly susceptible to hallucination. To address this, our system systematically shifts the burden of causal inference away from LLM text generation and onto deterministic, offline algorithms. The LLM's role is strictly confined to that of a natural language interface (NLI), tasked only with translating formally verified proofs into human-readable text. To achieve this, the engine adapts LLM-driven evolutionary coding to evolve constructive graphtraversal algorithms over a rigorous topological graph of discrete behavioral signals. The architecture resolves the uncertainty of sparse observational data through abductive Counterfactual Simulation (injecting unobserved hypothetical phenomena to infer hidden causal links). By executing these algorithms on a formally closed substrate governed by the invariant-preserving algebra of Hyperdimensional Computing (HDC), we establish a theoretical framework for an autonomous reasoning engine designed to enforce logical auditability and structurally constrain the propagation of weak logical steps.

---
