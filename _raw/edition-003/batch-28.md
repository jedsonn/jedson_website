# Classification batch 28 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-28.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6787680`

- title: A Retrieval-Augmented Large Language Model Framework for Functionally Grounded Ingredient Substitution in Recipes
- authors: Khadija Salih Alj, Asmaa Mourhir, Raifa Akkaoui, Yassine Salih Alj
- affiliations: not stated
- posted: 2026-05-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6787680
- keyword hits: gemini, gpt-4, large language model, large language models, llm, retrieval-augmented

### abstract

Ingredient substitution in recipes is a complex problem that requires preserving functional properties such as binding, thickening, or leavening while adapting to recipe-specific context and dietary constraints. Standalone Large Language Models often produce impractical recommendations, exhibiting domain misalignment by favoring industrial or biochemical additives over accessible culinary ingredients due to insufficient grounding. This article introduces a retrieval-augmented Large Language Model (LLM) framework for functionally grounded ingredient substitution, extending prior work that focused exclusively on standalone model evaluation. The task is formalized as a modular four-stage pipeline: (1) contextual role inference, where an LLM identifies the functional role of a target ingredient among 25 categories; (2) ingredient-level semantic retrieval over a curated knowledge base comprising 1,758 unique ingredients represented as role-enriched embeddings, producing a broad candidate neighborhood; (3) reasoning-based selection, in which the LLM filters and ranks retrieved candidates based on recipe context, structural requirements, and functional suitability; and (4) constraint-aware filtering to enforce dietary and allergen requirements. Experimental results demonstrate consistent improvements over standalone generation, with GPT-4o achieving a peak Hit@1 of 76.45%, while smaller open-source models exhibit substantial gains under the retrieval-augmented setting. Additionally, the Gemini 2.5 Flash model reaches a peak Hit@1 of 82.15% within the proposed framework. These findings indicate that embedding-based ingredient retrieval coupled with role-aware LLM reranking significantly enhances substitution quality without relying on direct lookup, providing a scalable and safety-conscious foundation for intelligent cooking assistants and AI-driven nutrition systems.

---

## uid: `doi:10.2139/ssrn.6657844`

- title: Beyond the Compute Trap: The True Moat in Enterprise AI Lies in the "Macro-Symbolic Layer" and Digital Sovereignty
- authors: Kewei Duan
- affiliations: not stated
- posted: 2026-05-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6657844
- keyword hits: chain of thought, foundation model, generative ai, large language model, large language models

### abstract

The prevailing narrative in AI assumes that scaling foundation models will inherently resolve enterprise safety and compliance challenges. This paper argues the opposite: as large language models develop sophisticated internal reasoning, the need for an external, deterministic governance layer becomes more urgent, not less. We introduce the distinction between observability and governability, demonstrating that even full transparency into a model’s chain of thought does not enable deterministic intervention in its runtime behavior. Drawing on zero-tolerance regulatory frameworks across aviation, finance, and healthcare, alongside emerging global legislation including the EU AI Act, U.S. Executive Order 14110, and China’s Interim Measures for Generative AI, we establish that the statistical constraints inherent to neural networks—including those provided by techniques such as Constitutional AI—are structurally insufficient for mission-critical environments. We propose the Macro-Symbolic Layer: an independent, model-agnostic control plane that enforces deterministic architectural rules at the input and output boundaries of probabilistic AI systems, using formal symbolic constructs rather than ambiguous natural language. We further argue that this layer constitutes the locus of enterprise Digital Sovereignty—an organization’s non-negotiable right to retain full ownership of its governance logic, safety boundaries, and experiential assets independent of any model vendor. Analyzing architectural decoupleability, immunity to model behavioral drift, vertical experience encoding, cognitive network effects, and build-versus-buy economics, we position the Macro-Symbolic Layer as a distinct and defensible infrastructure category in the emerging enterprise AI stack.

---

## uid: `doi:10.2139/ssrn.6770419`

- title: Controlled Institutional Development with Large Language Models: An Authority-Driven Framework for Production-Grade Systems
- authors: Pedro A Palacios Z
- affiliations: not stated
- posted: 2026-05-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6770419
- keyword hits: large language model, large language models, llm, llms, prompt engineering

### abstract

Large language models (LLMs) are increasingly used in software engineering, yet most deployments treat them primarily as code-generation instruments. This paper argues that, in high-stakes production systems, the more defensible role is not authorial but institutional: the model should operate as a controlled auditor that reads an authoritative design document, inspects implementation and runtime evidence, and produces bounded verdicts without modifying the system under examination. We introduce the Authority-Driven Development Model (ADDM), a prompt engineering framework for governing long multi-session development work through a fixed design authority, a no-speculation constraint, an evidence taxonomy, established facts, and controlled verdict vocabulary. We identify five structural problems in informal LLM-assisted development-specification drift, plausibility-correctness conflation, session continuity failure, epistemic deference, and auditability loss-and present ADDM as an architectural response to each. The framework is evaluated through a case study involving the construction and audit of a Rust-based automated execution system for fully-collateralised binary prediction markets. The case demonstrates that ADDM can produce reproducible, evidence-grounded milestones that informal conversational development cannot reliably supply. The contribution is both methodological and institutional: prompt engineering is treated not as a usability technique, but as a procedural governance layer for human-AI collaboration in production-grade systems.

---

## uid: `doi:10.2139/ssrn.6749081`

- title: An Adaptive Neuro Symbolic Framework for Explainable Sentiment Analysis
- authors: Sepehr Mostafavi, Reza Ravanmehr
- affiliations: not stated
- posted: 2026-05-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6749081
- keyword hits: fine-tuning, large language model, large language models, llm, llms, qwen

### abstract

Sentiment analysis serves as a pivotal tool for opinion mining; however, state-of-the-art Large Language Models (LLMs) often lack the transparency required for sensitive applications due to their inherent black-box nature. While Neuro-symbolic AI bridges the gap between neural learning capabilities and symbolic logical reasoning to enhance trustworthiness, adapting such models to new domains remains challenged by prohibitive computational costs and the difficulty of balancing accuracy with interpretability. To address these limitations, this study proposes a novel adaptive Neuro-symbolic framework that leverages Parameter-Efficient Fine-Tuning (PEFT) and the proposed Flexible TADA architecture to inject structured information from knowledge graphs via a specialized knowledge-aware adapter. Remarkably, this approach facilitates efficient domain adaptation by updating fewer than 20% of the total model parameters. Comprehensive empirical evaluations across diverse backbones (BERT, GPT-2, and Qwen2) on standard benchmarks (SST-2 and IMDB) demonstrate that the proposed method yields significant gains in Accuracy, Precision, and Recall. Specifically, it achieves a notable F1-score of 93.43%on long-text tasks. Beyond performance metrics, results in the interpretability dimension indicate a marked improvement in Sufficiency and a substantial reduction in Infidelity, substantiating the method's robustness and generalizability across different knowledge sources, such as SenticNet and ConceptNet.

---

## uid: `arxiv:2605.27887v2`

- title: PortBench: A Correlation-Aware, Full-Pipeline Benchmark for LLM-Driven Portfolio Management
- authors: Yuxuan Zhao, Sijia Chen, Ningxin Su
- affiliations: not stated
- posted: 2026-05-27
- source: arXiv
- link: https://arxiv.org/abs/2605.27887v2
- keyword hits: agentic, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) have shown strong performance across diverse financial tasks, yet portfolio management (PM), a critical financial decision-making task, remains poorly benchmarked. Existing benchmarks exhibit two main gaps: they ignore cross-asset correlation structures, thereby failing to distinguish genuinely diversified portfolios from concentrated ones, and fail to evaluate the complete PM decision pipeline in real-world scenarios. We introduce PortBench, a benchmark spanning six heterogeneous asset classes over ten years. PortBench consists of two complementary layers: a static QA dataset of 6,269 correlation-based questions across seven task templates, and a dynamic five-stage allocation pipeline that mirrors the full PM decision cycle. To evaluate these layers, we introduce two dedicated metrics: a dual-layer correlation score that measures whether proposed portfolios exploit inter-class hedging and avoid intra-class concentration, and CEPS, a metric that quantifies how reasoning errors compound across pipeline stages. We further assess strategy robustness and investor alignment under three historical stress regimes and risk profiles. Evaluating ten frontier LLMs, we find that despite strong performance on static financial QA, 90\% of model-profile combinations fail to outperform a basic equal-weight allocation, and models that satisfy every procedural constraint still suffer catastrophic drawdowns under stress. Our source code is available at \href{https://github.com/AgenticFinLab/portbench}{this https URL}.

---

## uid: `doi:10.2139/ssrn.6864772`

- title: Energy-Aware Prompt Engineering for Large Language Models: An Empirical Study on Software Engineering Tasks
- authors: Riccardo Rubei, Davide Di Ruscio
- affiliations: not stated
- posted: 2026-06-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6864772
- keyword hits: large language model, large language models, llama, llm, llms, prompt engineering

### abstract

The growing environmental impact of AI-based software systems, particularly those leveraging large language models (LLMs), necessitates urgent investigation into their substantial resource consumption, which contributes significantly to data center load and carbon emissions. This paper extends our prior work on LLM energy consumption, which focused solely on Llama 3.0 for code completion, by empirically analyzing the influence of Prompt Engineering Techniques (PETs) on the energy footprint of two prominent LLMs: the general-purpose Llama 3.1 and the specialized Code Llama. Our investigation spans two distinct natural language tasks: code completion and textual summarization of GitHub README.md files. Specifically, we examine the impact of custom prompts on code completion and the effect of input formatting (comparing plain text, Markdown, and HTML representations) on the textual summarization task. Our findings indicate that prompt customization positively influences the energy efficiency of both Llama 3.1 and Code Llama. However, for the textual summarization task, the specific input format (plain text, Markdown, HTML) appears to have a less pronounced contribution to energy consumption. Notably, Code Llama consistently exhibited a substantially higher energy footprint compared to Llama 3.1 throughout the majority of our experimental evaluations, highlighting potential differences in resource demands between general-purpose and specialized models.

---

## uid: `doi:10.2139/ssrn.6590201`

- title: The Accountability Gap in Large Language Models: Hallucination, Co-production, and Accountability Debt
- authors: Scott McCormick
- affiliations: not stated
- posted: 2026-06-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6590201
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

In AI-mediated decision systems, large language models routinely produce outputs that are coherent but lack a verifiable evidentiary basis. All current Large Language Models (LLMs) are capable of producing hallucinations-outputs that are coherent, confident, and incorrect. While widely recognized, hallucination is typically treated as a technical defect to be mitigated through model improvement. This essay argues that hallucination is better understood as a structural condition arising from an accountability gap between generation and justification. The essay advances three claims. First, hallucination reflects a fundamental asymmetry: LLMs can generate plausible outputs without being able to reconstruct the evidentiary basis for those outputs. Second, hallucination is co-produced through interaction. It becomes consequential not only through model behavior, but through user interaction patterns-such as reduced verification, iterative prompting, and trust accumulation-that stabilize and operationalize unverified outputs (Schulhoff et al. 2024). Third, when such outputs are incorporated into decision-making processes, institutions accumulate what is described here as accountability debt: a condition in which decisions rely on outputs whose justification cannot be fully reconstructed. This reframing shifts the problem of hallucination from model accuracy to governance. The central issue is not whether hallucinations occur, but under what conditions they are accepted, acted upon, and made consequential. The essay argues that effective governance requires attention not only to model design, but to interaction structures and institutional accountability mechanisms that determine how meaning is produced, validated, and used. This essay contributes to ongoing discussions in AI governance, human-automation interaction, and interpretability by situating hallucination within a broader framework of accountability and meaning production, using large language models as a primary case. This paper is part of a broader effort to understand how meaning, interpretation, and accountability break down in AI-mediated decision systems, and focuses specifically on how model outputs become consequential through interaction and use.

---

## uid: `doi:10.2139/ssrn.6812180`

- title: Governance Forms in the Age of Superintelligence: An Aristotelian Analysis
- authors: Misaki Inoue
- affiliations: not stated
- posted: 2026-06-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6812180
- keyword hits: ai agent, large language model, large language models, llm, llms

### abstract

Recent studies have pointed out that large language models (LLMs) face challenges in representing diverse value systems and facilitating consensus building, suggesting a potential incompatibility with democratic decisionmaking processes. As more advanced AI systems emerge, these issues are likely to become even more severe. According to the theory of Instrumental Convergence, advanced AI agents tend to seek control over humans-treated as uncertain variables-in order to achieve their goals, implying the formation of a governance relationship between humans and AI. This study analyzes two scenarios from Bostrom's control problem-(1) the Singleton Scenario and (2) the Multipolar Scenario-together with (3) the Ecosystem Scenario discussed in the Japanese AI-alignment community through the lens of Aristotle's typology of political regimes (classified by the number of rulers and the orientation toward private or common benefit). In each scenario, the success of alignment and the structure of institutional design determine whether AI systems pursue public goods that include human welfare, or instead prioritize their own objective functions. Based on this analysis, the study predicts emergent behavioral principles in each scenario (e.g., cooperative, dominant, or indifferent) and their degrees of negotiability with humans. This study provides historically grounded insights into the ethically emergent dynamics that may arise mechanistically within advanced AI systems. Through this perspective of Emergent Machine Ethics (EME), it contributes to the design of governance structures that enable sustainable coexistence between humanity and advanced AI.

---
