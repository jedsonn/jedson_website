# Classification batch 47 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-47.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6840700`

- title: Copyright's Public Domains: The Limits on AI Appropriation
- authors: Graham Greenleaf, David F. Lindsay
- affiliations: not stated
- posted: 2026-05-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6840700
- keyword hits: generative ai, large language model, large language models, llm, llms

### abstract

The spectacular rise to commercial and intellectual prominence of artificial intelligence (AI) since 2022, and in particular the predominant role of generative AI and its use of large language models (LLMs), has given rise to many legal and policy problems. Four main types of problems for copyright law are sketched, in each of which one significant legal question raised is whether the use of the content is in the public domain, or is it an infringement of copyright? Can the developer of the training set, or the deployer of the AI system, or the end-user of the AI system, claim that the use they have made of the AI system’s content does not involve an infringement of copyright but is a use of that content which is in the public domain? Those building AI systems are faced with three alternatives. They can negotiate to obtain the consent (through private licences) of the owners of copyright in the works intended to be used. Or they can ignore whether or not consent may be necessary, on the basis that they ‘can get away with it’ anyway. Or they can attempt to justify the use they wish to make of the content on the basis that it does not require owner consent because it is in the public domain. This last approach is the subject of this article, which aims to be comprehensive and precise about which aspect(s) of the public domain can be used to support claims that consent is not legally necessary. Our previous work has identified fifteen aspects of the copyright public domain, the aggregate of which is the copyright public domain in a particular jurisdiction. We consider each of those fifteen categories, with a focus on Australian law, explaining first how the category is consistent with our overall definition of the public domain (that is, ‘the public’s ability to use content on equal terms without seeking permission’). Then the relationship of each category to international copyright law is stated, with an emphasis on how much (if any) expansion of that category in national laws is consistent with current international copyright law. We give brief examples of how each category is reflected in national laws, particularly in Australia. Finally, we consider possible ‘opportunities’, meaning how this aspect of the public domain has been or could be used or expanded (by legislation or case law) to assist the development of AI systems. This article concludes that developing solutions for the substantial challenges posed by generative AI can be assisted by analysing the actual and potential extent to which all of the existing public domain categories apply, or could reasonably be developed to apply, to access and use for developing AI systems. Instead of a ‘magic bullet’ to be found in only one category, the best solution might come from a combination of various public domain elements. From our survey we find that nine of the fifteen public domain categories offer some possibilities for supporting AI development, but in most categories these possibilities are slight. Two most clearly permit use of a substantial amount of content without the need for permission: the substantial number of works in which the copyright term has expired (category 5); and material available for use under neutral voluntary licences (category 14), such as CC licences. In two further categories access to significant amounts of public domain content is complicated due to legal uncertainties and practical obstacles: fair use exceptions, at least in the US and the EU (but not at present in Australia); and the tenet of copyright law that mere facts or ideas (category 10) can be freely used, which might seem to hold considerable potential for lawful AI training. Other public domain categories, as they currently exist, are of only theoretical value. The question then turns to the extent to which there is potential for developing existing public domain categories, while appropriately balancing the interests of authors and owners, on the one hand, and AI developers, on the other. There is more scope for national jurisdictions to reform the public domain categories than is commonly thought. For example, works expressly excluded from copyright protection (category 3), could take advantage of the two permissible optional exclusions, namely laws and other official texts, and political and legal speeches, and ‘news of the day’. This leaves the two public domain categories that have been a focus of debates about policy responses to the rise of generative AI: ‘free use’ exceptions (category 12) and neutral compulsory licensing (category 13). We can see some scope for a very nuanced TDM exception for some AI training which is in the public interest, and for some conventional compulsory licences or extended collective licences (ECLs). Reliance on the status quo , and market-based approaches are unlikely to be sufficient.

---

## uid: `doi:10.2139/ssrn.6831463`

- title: Topology Over Training: Cross-Domain Pattern Synthesis Through Graph Concurrence Without Weight Updates
- authors: Nicholas Cokas
- affiliations: not stated
- posted: 2026-05-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6831463
- keyword hits: fine-tuning, large language model, large language models, llm, llms, retrieval-augmented

### abstract

Large language models have advanced natural language generation but remain fundamentally limited by hallucination, domain isolation, and the absence of verifiable reasoning chains. Current approaches to these problems — retrieval-augmented generation, fine-tuning, and multi-agent orchestration — address symptoms rather than the structural cause: LLMs generate fluently but cannot verify what they generate. This paper introduces a graph-topological approach to cross-domain pattern synthesis that produces cross-domain concurrence signals through edge-density compounding across a knowledge graph rather than gradient-based training. We describe a reasoning middleware architecture that interposes between data sources and language model output, enforcing evidence-gated generation where every factual claim requires traceable provenance before release. We present results from a live deployment across 32 knowledge domains with an 11.2-million-pattern corpus, demonstrating that topological concurrence detection surfaces cross-domain relationships that single-domain models and retrieval systems systematically miss — including novel connections validated against held-out expert analysis. The system operates at zero marginal inference cost on consumer hardware, challenging the assumption that cross-domain intelligence requires scale. We do not claim parity with fine-tuned domain specialists on within-domain benchmarks; the contribution is the verified discovery of relationships that no single-domain system attempts.

---

## uid: `doi:10.2139/ssrn.6788059`

- title: SIGIL: Subtle Injection for Ground-truth Inference of LLM Training Data A Statistical Framework for Provable Training Data Membership
- authors: Abraham Itzhak Weinberg
- affiliations: not stated
- posted: 2026-05-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6788059
- keyword hits: large language model, large language models, llm, llms

### abstract

As large language models (LLMs) are increasingly trained on scraped web corpora without authorisation, content owners require forensic methods to prove that their documents were included in a model's training set. We propose SIGIL (Subtle Injection for Ground-truth Inference of LLM training data), a framework that embeds imperceptible canary sequences into protected text and code such that any LLM trained on those documents exhibits statistically detectable behavioural signatures when probed with targeted queries. SIGIL defines five canary strategies-lexical-rare, lexical-phrase, syntactic, semantic, and code-pattern-and a Membership Inference Score (MIS) grounded in the Neyman-Pearson hypothesis testing framework with formal false-positive rate (FPR) control. Simulator parameters are calibrated against the empirical membership inference literature, yielding realistic heterogeneous results across 36,000 trials: overall AUC = 0.892, rising from 0.831 at 0.1% injection to 0.947 at 10%. Detection rates range from 33% to 78% across model-size and injection-rate conditions. Code Pattern canaries achieve the highest AUC (0.903, Cohen's d = 1.84); Syntactic Structure the lowest (0.875, d = 1.63). All four experimental factors-injection rate, model size, canary strategy, and mixture ratio-have significant independent effects on MIS (p 0.86 even under 100% paraphrasing (AUC = 0.864), confirming robustness through semantic leakage that survives surface-level rewriting.

---

## uid: `doi:10.2139/ssrn.6845389`

- title: When Structured Guidance Helps in AI-Supported Revision: The Role of Baseline Justification Depth and Feedback Engagement
- authors: Songhee Han, Jueun Shin, Jiyoon Han, Bung-Woo Jun, Idam Kim, Sewon Joo, Zhongyu Wang
- affiliations: not stated
- posted: 2026-05-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6845389
- keyword hits: agentic, large language model, large language models, llm, llms, retrieval-augmented

### abstract

Large language models (LLMs) are increasingly examined as tools for providing feedback during revision tasks, but less is known about when additional structured guidance around such feedback improves task performance. This study examined how users’ baseline justification depth and reflective engagement with feedback from an LLM-based retrieval-augmented (RAG) chatbot shaped performance in a revision task. In a randomized experiment (N = 450), adult participants completed an instructional design task while interacting with the same LLM-RAG chatbot. During the refinement phase, participants received different forms of revision guidance. Participants were assigned to Condition A, no additional scaffold; Condition B, rubric-based scaffold; or Condition C, checklist-based scaffold. Task performance was rated with a three-criterion rubric, and open-ended responses were coded for baseline justification depth and revision theme. Task performance differed across revision conditions: Condition A produced the highest mean performance; Conditions B and C produced lower, nearly identical performance. Baseline justification depth was the strongest predictor of task performance and moderated revision condition effects: predicted performance increased most steeply across all baseline-depth levels in Condition A. However, Condition B showed no evident advantage for participants with lower baseline justification depth. Revision theme also predicted task performance after controlling for baseline justification depth and revision condition. Responses reflecting agency or structured integration of chatbot feedback were associated with higher performance; responses reflecting limited agency or insufficient reflection were associated with lower performance. The findings show that scaffold effectiveness in AI-supported revision depends on users’ baseline justification depth and agentic engagement with AI-generated feedback.

---

## uid: `doi:10.2139/ssrn.6798479`

- title: Beyond Consumer Memory: How Large Language Models Update Brand Knowledge
- authors: Andreas Hamann, Florian Stahl, P. K. Kannan
- affiliations: not stated
- posted: 2026-05-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6798479
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are emerging as new touchpoints in the customer journey, influencing how consumers discover and learn about brands. The authors argue that in these environments, brand knowledge is no longer formed solely in consumer memory but is also constructed and conveyed by LLMs. As firms continuously seek to shift brand-related associations, this research examines how brand knowledge updates in LLMs. Compared to consumer-based updating, LLMs differ structurally at the information-exposure stage: whereas consumers encounter brand information through diverse and partly stochastic touchpoints, LLMs rely on structured retrieval initiated by user queries. Consequently, the informational basis for brand-knowledge updating becomes contingent on query formulation and retrieval design, leading to systematic variation in how brand knowledge is conveyed across and within LLMs. The authors test these predictions in a controlled synthetic field experiment that leverages strategic brand repositioning as an exogenous shift in brand associations for recently established brands and tracks conveyed knowledge in model responses over time. The results provide broad support for retrieval-driven updating, with systematic heterogeneity across models and query types. The authors discuss implications for brand knowledge theory and identify retrievability as a key managerial lever in AI-mediated customer journeys.

---

## uid: `doi:10.2139/ssrn.6843685`

- title: Neuro-Symbolic Requirements Elicitation with Neutrosophic Hallucination Quantification
- authors: Ahmed Ibrahim
- affiliations: not stated
- posted: 2026-05-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6843685
- keyword hits: large language model, large language models, llm, llms

### abstract

Context: Large Language Models (LLMs) offer natural-language flexibility for automated requirements elicitation but frequently generate structurally invalid or hallucinated requirements, lacking formal correctness guarantees.Objectives: This study aims to eliminate structural hallucinations in LLM-generated requirements and quantify the LLM's pre-validation decision uncertainty within a formal domain model.Methods: We present a neuro-symbolic multi-agent architecture that operationalizes the Object-Oriented Method for Requirements Authoring and Management (OOMRAM) lattice. The LLM acts as a non-deterministic heuristic for lattice traversal, while a deterministic symbolic validator enforces all structural constraints. We introduce a neutrosophic (Truth, Indeterminacy, Falsity) framework to classify and score the LLM's requirement decisions before and after validation.Results: Evaluated across 37 natural-language project visions in eleven application families, the system completely eliminated structural hallucinations in 35 out of 37 cases (94.6%), with the remaining two containing only 6 unresolved structural errors (0.39% of decisions) due to iteration limits. Neutrosophic analysis revealed that 24.7% of all decisions are indeterminate (structurally valid but discretionary choices not explicitly mandated by the stakeholder).Conclusion: Offloading structural integrity to a deterministic symbolic layer successfully guarantees correctness, while neutrosophic logic provides a formal way to measure neural uncertainty, facilitating safe LLM deployment in formal requirements engineering.​

---

## uid: `doi:10.2139/ssrn.6805943`

- title: Constitutional Architecture of Human-AI Systems: Enabling Bilateral Collaboration
- authors: Thomas J. Salter
- affiliations: not stated
- posted: 2026-06-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6805943
- keyword hits: claude, deepseek, gemini, qwen

### abstract

Humans fail or succeed because they are embodied, social, emotional beings. AIs fail or succeed because they are not. A companion paper documented this asymmetry through a bilateral taxonomy of characteristics establishing three empirical findings: temporal asymmetry (human characteristics are structural, AI characteristics are evolving), structural complementarity (where one-party exhibits capacity, the other exhibits constraint), and shared vulnerability (both parties exhibit certain failure modes simultaneously). This paper develops the constitutional framework that bilateral architecture enables. Contemporary AI governance frameworks face a fundamental tension between regulatory approaches (external control through oversight) and techno-optimist approaches (automated self-governance through alignment). The bilateral framework navigates between these poles through constitutional governance: authority anchored to the party bearing embodied accountability (humans) while leveraging computational capabilities that party lacks (AI). Constitutional governance interrupts shared vulnerabilities through multi-origin AI diversity and falsification discipline, adapts to evolving AI capabilities while remaining anchored to structural human characteristics, and preserves non-delegable Position 0 human authority as ultimate governance anchor. This paper presents bilateral collaboration opportunities derived through systematic multi-AI deliberation under the Initiating Collaborative Intelligence (ICI) methodology. Each opportunity underwent the Bilateral Test: explicit anchors in both human strengths (Section D of the taxonomy) and AI strengths (Section E), verification of non-reducibility (the collaborative capacity cannot be achieved by either party alone), and specification of constitutional requirements. The opportunities are organized across five categories: constraint-mitigation pairs where AI strength compensates for human constraint or vice versa; shared constraint mitigation where bilateral pairing interrupts mutual failure modes; emergent capabilities that exist only in the collaboration space; multi-media adaptation leveraging symbolic, visual, and narrative registers; and evolved AI capabilities demonstrating the generative nature of bilateral architecture. The paper establishes four constitutional principles: structural constraints as design conditions (not defects to overcome), irreducible authority anchored to accountability (Position 0 human adjudication), multi-origin verification as constitutional requirement (not engineering optimization), and adaptive governance anchored to structural permanence (evolving protocols, stable anchors). These principles apply across implementation contexts because they are grounded in asymmetries between embodied mortal humans and disembodied computational systems—asymmetries that remain constant as AI capabilities evolve. This paper is itself evidence of constitutional governance: produced through a five-member multi-AI deliberative Circle (Claude, Grok, Gemini, Qwen and DeepSeek) operating under Falsify, Verify, Amplify protocol with Position 0 human adjudication. The bilateral framework is not speculative proposal but tested theorem—constitutional architecture that has undergone falsification discipline and emerged robust.

---

## uid: `doi:10.2139/ssrn.6835518`

- title: Convergence Point: A Unified Explanatory Principle for Response Uncertainty in AI Language Models
- authors: Ji Hong Park
- affiliations: not stated
- posted: 2026-06-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6835518
- keyword hits: large language model, large language models, llm, llms

### abstract

Large Language Models (LLMs) consistently express confidence on certain topics while generating uncertain responses on others. This study proposes Convergence Point Theory to explain this phenomenon through a single unified principle. A Convergence Point refers to the Consensus Density of knowledge accumulated by humanity on a given topic, which functions as the structural condition determining whether an AI model's internal response direction converges or diverges. Three zones are identified: the Full Consensus Zone (e.g., mathematical axioms, physical laws), the Partial Consensus Zone (e.g., capital punishment, euthanasia), and the Non-Consensus Zone (e.g., the nature of consciousness, the existence of God). To validate the theory, 3,600 measurements were collected from five open-source language models across four utterance versions, combining External Measurement (hedging language analysis) and Internal Measurement (logit entropy). The Spearman correlation between the Convergence Point Index and AI response uncertainty was r = 0.676 (p < 0.001). Probing Classifier analysis confirmed that Convergence Point information is linearly encoded in model internals from Layer 10–11 onward with 100% classification accuracy. A key finding is that the Partial Consensus Zone exhibited higher uncertainty than the Non-Consensus Zone in certain cases, suggesting that data conflict induces stronger internal variance than data absence. Implications for AI safety and occupational deployment are discussed.

---
