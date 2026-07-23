# Classification batch 61 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-61.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.4395751`

- title: Using LLMs for Market Research
- authors: James Brand, Ayelet Israeli, Donald Ngwe
- affiliations: not stated
- posted: 2023-03-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.4395751
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) have rapidly gained popularity as labor-augmenting tools for programming, writing, and many other processes that benefit from quick text generation. In this paper we explore the uses and limitations of LLMs for researchers and practitioners who aim to understand consumer preferences. We focus on the distributional nature of LLM responses, and query the different LLMs to generate dozens of responses to each survey question. We offer two sets of results to illustrate and assess our approach. First, we show that estimates of willingness-to-pay for products and features derived from LLM responses are sometimes comparable to estimates from human studies, but are often inaccurate and in some cases wrong-signed. Second, we demonstrate a practical method for market researchers to enhance LLMs' responses by incorporating previous survey data from similar contexts via fine-tuning. This method improves alignment with human responses for existing and, importantly, new product features \emph{within} the same product category and population. We do not find similar improvements in the alignment for new product categories or for differences between customer segments. Taken together, our results suggest that the appropriate use case for LLMs in market research is as a supplement to---not a substitute for---human studies, with fine-tuning providing the most reliable gains when prior human survey data from the relevant category and population are already in hand.

---

## uid: `doi:10.2139/ssrn.6215938`

- title: A Survey of LLMs in Drug Discovery and Precision Medicine
- authors: Hasi Hays, William  J. Richardson
- affiliations: not stated
- posted: 2026-03-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6215938
- keyword hits: large language model, large language models, llm, llms, retrieval augmented

### abstract

The convergence of artificial intelligence and biomedical research has catalyzed transformative advances in drug discovery and precision medicine. Large language models (LLMs), originally developed for natural language processing, have emerged as powerful tools capable of processing complex biomedical data, from molecular structures to clinical records. This comprehensive review examines the state-of-the-art applications of LLMs across the drug development pipeline, spanning target identification, molecular generation, property prediction, and drug repurposing in drug discovery, as well as clinical decision support, patient stratification, treatment personalization, and genomic interpretation in precision medicine. We analyze the technical methodologies underlying these applications, including multimodal architectures, knowledge-guided approaches, and retrieval augmented generation systems. Through examination of recent advances from 2020 to 2025, we highlight key achievements such as end-to-end drug discovery pipelines, multi-agent systems for clinical simulation, and knowledge-enhanced models achieving state-of-the-art performance. We critically assess current challenges, including data privacy, model interpretability, hallucination risks, and ethical considerations. Finally, we discuss future directions, emphasizing the potential for federated learning, explainable artificial intelligence, and integrated multiscale approaches to advance the field toward more reliable, transparent, and clinically applicable systems.

---

## uid: `doi:10.2139/ssrn.6097886`

- title: Representational and Behavioral Stability of Truth in Large Language Models
- authors: Samantha Dies, Courtney Maynard, Germans Savcisens, Tina Eliassi-Rad
- affiliations: not stated
- posted: 2026-03-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6097886
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

Large language models (LLMs) are increasingly used as information sources, yet small changes in semantic framing can destabilize their truth judgments. We propose P-StaT (Perturbation Stability of Truth), an evaluation framework for testing belief stability under controlled semantic perturbations in representational and behavioral settings via probing and zero-shot prompting. Across sixteen open-source LLMs and three domains, we compare perturbations involving epistemically familiar Neither statements drawn from well-known fictional contexts (Fictional) to those involving unfamiliar Neither statements not seen in training data (Synthetic). We find a consistent stability hierarchy: Synthetic content aligns closely with factual representations and induces the largest retractions of previously held beliefs, producing up to 32.7% retractions in representational evaluations and up to 36.3% in behavioral evaluations. By contrast, Fictional content is more representationally distinct and comparatively stable. Together, these results suggest that epistemic familiarity is a robust signal across instantiations of belief stability under semantic reframing, complementing accuracy-based factuality evaluation with a notion of epistemic robustness.

---

## uid: `doi:10.2139/ssrn.6416050`

- title: A Generalizable Retrieval-Augmented LLM Framework for PRISMA-Aligned Systematic Reviews
- authors: Romeo Silvestri, Miguel Pincheira Caro, Massimo Vecchio, Fabio Antonelli
- affiliations: not stated
- posted: 2026-03-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6416050
- keyword hits: large language model, large language models, llm, llms, retrieval-augmented

### abstract

Systematic reviews and meta-analyses are essential for advancing scientific research, but they are time-consuming, labor-intensive, and prone to human error during literature selection and data extraction. This paper proposes a framework that integrates Large Language Models (LLMs) and retrieval-augmented generation (RAG) into the PRISMA 2020 workflow to automate and standardize key review tasks, enhancing transparency, completeness, and up-to-date reporting. The framework uses structured query templates to ensure reproducible bibliographic searches, an LLM-driven pipeline for title and abstract screening, and a RAG-based full-text assessment in which articles are segmented, encoded as dense vector embeddings, and retrieved for generative evaluation against inclusion and exclusion criteria. Beyond selecting relevant papers, the framework also extracts specific information from documents, such as application details or datasets, and harmonizes it into a standardized metadata schema. Automated tasks are supported by predefined fallback strategies, with human oversight reserved for borderline decisions. To evaluate our proposal, we performed an experimental validation using an existing systematic literature review as a reference. The framework achieved an article detection rate of 72.34\% and an extraction accuracy of 85.11\% for domain-specific information. Furthermore, the framework identified 25 additional data sources not reported in the original review. These results demonstrate that the proposed framework can effectively assist in both identifying relevant studies and extracting additional information, substantially accelerating systematic reviews while maintaining alignment with the PRISMA 2020 guidelines.

---

## uid: `doi:10.2139/ssrn.6426760`

- title: Protocol-Mediated Execution Governance for LLM Agent Systems
- authors: Ari Harrison
- affiliations: not stated
- posted: 2026-04-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6426760
- keyword hits: ai agent, large language model, large language models, llm

### abstract

As large language models transition from conversational assistants to autonomous agents capable of executing actions inside enterprise infrastructure, the primary security risk shifts from model hallucination to ungoverned delegation of execution authority to probabilistic systems. A fundamental architectural question emerges: how should execution authority be governed when the decision-making component is nondeterministic? This paper proposes protocol-mediated execution layers as a governance architecture for LLM agent systems. Rather than relying on prompt-based behavioral suggestions, which are probabilistic, bypassable, and unenforceable, we argue that execution governance must be implemented as structural infrastructure external to the model. We present a concrete architecture in which the LLM functions as a reasoning engine that expresses intent, while a protocol layer (instantiated here as Model Context Protocol infrastructure) enforces authorization, validates inputs against formal schemas, constrains execution to pre-defined capability boundaries, and maintains an immutable audit trail. Drawing on Zero Trust principles [13] and foundational work in capability-based security [12, 16], we establish direct architectural parallels to operating system kernels, API gateways, and container orchestration control planes, demonstrating that every generation of computing has solved the same governance problem through the same fundamental pattern. We present a production implementation, NovoMCP, a drug discovery platform managing 122 million molecular records, as an empirical case study demonstrating four governance layers: schemabased tool definitions, tiered access control, pre-execution resource accounting, and service-level isolation. We further identify an underexplored dimension of the governance problem: input-side control. While most discussions focus on constraining model outputs (what the agent can do), we argue that a complete governance envelope must also constrain model inputs (what context, tools, and data sources the agent can access). We propose admissibility gates and behavioral drift detection as complementary mechanisms, and identify drift detection across sequences of individually authorized actions as a key open problem. 1 The central thesis is a reframe: the question is not whether to trust AI agents, but what architectural controls make them trustworthy. The answer, consistent with five decades of computing history, is: trust the protocol, not the process.

---

## uid: `doi:10.2139/ssrn.6494259`

- title: Digital Legacy AI: A Proactive Framework for Posthumous Conversational Systems
- authors: Daniele Frongia
- affiliations: not stated
- posted: 2026-04-06
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6494259
- keyword hits: generative artificial intelligence, large language model, large language models, retrieval-augmented

### abstract

The rapid advancement of generative artificial intelligence has made it increasingly feasible to simulate human-like communication based on personal data. Current approaches to posthumous digital presence rely on passive data aggregation, reconstructing digital personas from emails, social media posts, and other digital traces that were never intended for such use. These reconstructions are often unstructured, unintentional, and produced without explicit consent. This paper introduces the concept of Digital Legacy AI: the intentional design of a personal artificial intelligence system during one's lifetime, aimed at enabling meaningful posthumous interaction with designated individuals. Unlike retrospective systems (commonly known as "deadbots" or "griefbots"), this approach is grounded in proactive data curation, structured identity modelling, and explicit pre-mortem authorisation. The paper proposes a multi-layered identity framework and introduces a methodology based on Retrieval-Augmented Generation (RAG), a technical approach that anchors AI responses to the individual's own documented words and values, significantly reducing the risk of the AI fabricating content. It also addresses the practical contingency of sudden or unexpected death through an iterative "Draft Legacy" design. A concrete use case, a parent creating a digital legacy for a young child, illustrates the human and emotional dimensions of the framework. The paper concludes by examining ethical and legal implications, with particular attention to the regulatory gap created by the GDPR's explicit exclusion of deceased persons, psychological risks and safeguards (including the author's position that AI systems must not intervene during the grief process, and that prior consultation with a qualified psychologist is a mandatory condition of access for heirs of all ages), and the necessity of data sovereignty. The urgency of this framework is underscored by recent industrial developments. In 2025, Meta obtained a patent for a system based on large language models capable of simulating the digital activity of a user after death, generating interactions consistent with their historical behaviour on social platforms. Although the company has stated it has no plans for implementation, the patent marks a significant step towards the industrial formalisation of so-called "griefbots" and the algorithmic management of post-mortem identity. The Digital Legacy AI framework presented in this paper moves considerably further: rather than simulating a person from the passive residue of their social media history, it proposes a proactive, consent-based, and ethically governed architecture in which the individual is the author of their own posthumous presence.

---

## uid: `doi:10.2139/ssrn.6636974`

- title: Toward Robust Legal Text Formalization into Defeasible Deontic Logic Using LLMs
- authors: Elias Horner, Cristinel Mateis, Guido Governatori, Agata Ciabattoni
- affiliations: not stated
- posted: 2026-04-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6636974
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

We present a comprehensive approach to the automated formalization of legal texts using large language models (LLMs), into Defeasible Deontic Logic (DDL). Our method employs a structured pipeline that segments complex normative language into atomic snippets, extracts DDL rules, and evaluates them for syntactic and semantic coherence. We introduce a success metric that captures the completeness of formalizations, and a novel two-stage pipeline with a dedicated refinement step to improve logical consistency and coverage. We compare results across multiple LLM configurations, including newly released models and various prompting strategies. We discuss limitations arising from gold-standard dependence and implicit legal obligations, highlighting trade-offs between textual fidelity and normative completeness.Experiments on legal norms from the Australian Telecommunications Consumer Protections Code demonstrate that, when guided effectively, LLMs can produce formalizations that align closely with expert-crafted representations, underscoring their potential for scalable legal informatics.

---

## uid: `doi:10.2139/ssrn.6536159`

- title: The Moral Machine? Ideological AI Partially Simulates Human Responses to Moral Framing
- authors: Xingman Wu, Xiaoli Nan
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6536159
- keyword hits: ai agent, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are increasingly explored as tools for simulating human responses in social and behavioral research, yet their capacity to reproduce theory-driven persuasion effects remains unclear. This research tests whether an LLM can simulate human responses in moral framing experiments grounded in moral foundations theory, using politicized COVID-19 mask communication as a stringent test case. Two participant-level simulation studies replicated experiments originally conducted with human participants, assigning AI agents political identities and exposing them to care/fairness, loyalty/purity, or nonmoral messages. Across simulations, the LLM reproduced several key effects: politically liberal agents expressed more favorable attitudes toward mask wearing and tended to perceive care/fairness frames as more persuasive than loyalty/purity frames, whereas conservative agents evaluated the frames similarly or showed modest preference for loyalty/purity appeals. These patterns are consistent with evidence that LLMs approximate broad, socially patterned associations in ideology, moral language, and health attitudes. However, the simulations did not reliably reproduce ideology by message interaction effects central to moral reframing theory. The findings position LLMs as promising but partial analogues of human participants, clarifying both the potential and boundaries of AI-based "silicon samples" for theory testing in communication research.

---
