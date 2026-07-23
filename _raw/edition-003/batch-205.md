# Classification batch 205 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-205.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6901711`

- title: AMESA: Adaptive Mixture-of-Experts Service Architecture for Efficient LLM Serving
- authors: Doaa Shawky
- affiliations: not stated
- posted: 2026-06-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6901711
- keyword hits: large language model, llm, retrieval-augmented

### abstract

Large Language Model (LLM)-enabled services are increasingly deployed as application backends, where the LLM replaces oraugments traditional backend logic to handle structured, recurring requests such as customer support queries, dashboard assistants,API orchestration, and retrieval-augmented generation pipelines. Unlike open-ended conversational settings, these deploymentcontexts naturally exhibit high request repetition, popularity skew, and bursty concurrency patterns, since prompts are frequentlygenerated from structured templates or recurring user workflows. Despite this, large-scale deployment remains challenging due tohigh inference latency, limited throughput, and substantial operational cost — challenges that are further amplified by redundantbackend invocations caused by repeated and concurrently duplicated requests. Existing optimization techniques, such as caching,batching, and request coalescing, are typically applied independently and lack adaptability to dynamic workload conditions. Thispaper presents Adaptive Mixture-of-Experts Service Architecture (AMESA), a service-level architecture that integrates multiple ex-ecution strategies into a unified adaptive framework. AMESA models execution paths — including exact and semantic cache reuse,in-flight request coalescing, batching, and exact model inference — as specialized execution experts and employs a lightweightrule-based routing mechanism to dynamically select efficient execution paths according to runtime workload conditions. Unliketraditional neural mixture-of-experts approaches, AMESA operates entirely at the service layer and does not require model retrain-ing.A comprehensive experimental evaluation is conducted using controlled workloads with varying request distributions and con-currency levels. The results demonstrate that AMESA substantially improves system efficiency, achieving up to 2.5× higherthroughput and reducing average latency by 4–6× under highly repetitive workloads. Under more realistic skewed workloads,AMESA reduces p95 latency by 3–5× and improves throughput by up to 2× compared with direct backend execution. Furthermore,AMESA reduces backend invocations leading to proportional reductions in estimated operational cost. The results demonstrate ef-fectiveness in LLM-as-backend deployments, where structured and recurring request patterns create substantial opportunities foradaptive execution-path selection

---

## uid: `doi:10.2139/ssrn.6828339`

- title: Redesigning AI Regulatory Sandboxes for Generative AI: Beyond Traditional for-Profit Innovation
- authors: Bhargavi Ganesh, Jose A. Guridi, Thiago Moraes
- affiliations: not stated
- posted: 2026-06-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6828339
- keyword hits: ai agent, generative ai

### abstract

Regulatory sandboxes have become a central instrument for governing artificial intelligence (AI), with data protection authorities and AI regulations frameworks increasingly relying on them to enable regulatory learning and promote innovation. However, in this paper, we argue that current sandbox frameworks do not adequately account for AI innovation occurring outside of the for-profit space. As vibe coding, AI agents, and zero-code platforms have lowered the technical thresholds for building and deploying AI applications, public sector institutions, civil society organizations, and non-institutional innovators are increasingly in roles that data protection and AI regulations have traditionally assigned to firms. Yet in conducting a scoping review of AI-related sandboxes across jurisdictions in Europe, Latin America, Asia, Africa, and the Middle East, we find several barriers to participation by these actors. In addition to often explicitly limiting sandbox participation to private sector actors, eligibility criteria and participant recruitment processes place implicit barriers as they assume organisational capacity that public sector, civil society, and individual innovators typically do not possess. Drawing from literature in innovation studies, data protection and AI law, and experimental governance, we argue that this bias against non-market actors limits the capacity for socially beneficial innovations to emerge. To go beyond market-driven approaches to regulatory learning and innovation, we conclude by proposing three main pathways for more inclusive sandbox design, including low-friction entry points, intermediated participation, and eligibility criteria oriented toward societal value.

---

## uid: `doi:10.2139/ssrn.6894079`

- title: From Data moats to Context moats: A Utility Law for Applied AI
- authors: Gaston Besanson, Jean Luc Chatelain
- affiliations: not stated
- posted: 2026-06-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6894079
- keyword hits: foundation model, retrieval-augmented

### abstract

The dominant heuristic in enterprise AI holds that better performance follows from owning and continuously retraining on the largest proprietary corpus. As foundation models with long context windows, retrieval-augmented generation, and native tool use become widely available, this heuristic no longer fully describes where competitive advantage accumulates. This paper advances a central claim: for a broad class of applied AI tasks with high prior substitutability, advantage is migrating from proprietary corpus ownership to governed inference-time context orchestration, and this migration can be expressed as a quantitative utility law and tested empirically. We formalize context moats as the utility advantage arising from governed control of a thin, high-signal layer of context at inference time. We introduce three core constructs: (i) a Context Utility Law that decomposes enterprise AI value into performance, hallucination, cost, and governance risk; (ii) a Context Dominance Condition that specifies when marginal gains in context quality and governance dominate marginal gains in proprietary data volume; and (iii) a Context Moat Vector that turns context quality, memory-state fidelity, and governance into measurable indices. The framework is informed by recent empirical literature on RAG performance, long-context inference, and data governance, yielding falsifiable predictions for distinguishing data-moat from context-moat regimes. Finally, we situate the thesis against the emerging world-models paradigm and identify the architectural horizon beyond which the context-moat era may end. In applied AI, advantage is migrating from corpus ownership to context control.

---

## uid: `doi:10.2139/ssrn.6830898`

- title: Beyond Retrieval vs Context: A Unified Evaluation Framework for External Information Management in LLM Agents
- authors: Alessio Rocchi
- affiliations: not stated
- posted: 2026-06-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6830898
- keyword hits: llm, retrieval-augmented

### abstract

Recent advances in language-model context windows past one million tokens have reopened the debate over whether retrieval-augmented generation remains necessary. We argue that the debate is misframed: long-context inference, retrieval-augmented generation (RAG), and agent memory systems are not paradigms in competition but three architectural realisations of a single information-management policy. We introduce a five-axis framework-accuracy, cost, latency, freshness, traceability-that scores any policy under a workload distribution and a price schedule. A four-operator canonical form (ingest, consolidate, forget, working-tier maintenance) reduces memory-augmented generation to RAG composed with three or four additions, and a precise retrieval-equivalence relation identifies the conditions under which a deployed memory system collapses to RAG observationally. We exhibit this collapse empirically on the open-source Mem0 2.x release. An engineering map of six surveyed conversationalmemory systems (Mem0, Letta, Zep, A-MEM, Cognee, Generative Agents) documents four cross-system patterns: forgetting is uniformly absent or opt-in, consolidation is heterogeneous in scheduling, papervs-code divergence runs in both directions, and the cognitive memory taxonomy lives in documentation rather than in schemas. A controlled empirical protocol (§6) is preregistered at horizons of 10 2 , 10 3 , and 10 4 turns under an explicit and frozen cost function; the present draft executes the 10 2-turn pilot on all six configurations and a long-horizon C1 trajectory terminating at 𝑁 = 2,992 turns. The longhorizon C1 measurements are consistent with §3.6's a-priori prediction that long-context cumulative cost diverges from retrieval and memory baselines, with empirical local slopes accelerating from ≈ 1.76 to ≈ 1.97 as the horizon grows. Full multi-configuration 10 3-and 10 4-turn runs, three-seed replication on the accuracy axes, the customer-support Scenario B, and the cross-vendor simulator cross-check are preregistered as deferred future work.

---

## uid: `doi:10.2139/ssrn.6910198`

- title: RAG-Based Retrieval Systems for Enterprise Mainframe Operations: Accelerating Incident Response and Mitigating Operational Risk Through AI-Driven Knowledge Access
- authors: Rohit Kumar Shaw
- affiliations: not stated
- posted: 2026-06-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6910198
- keyword hits: llm, retrieval augmented

### abstract

Since the introduction of mainframe computers, large amounts of data have been produced in these systems, yet operators rely on manual searching of fragmented documentation for troubleshooting incident resolution. In this paper, we explore the application of the Retrieval Augmented Generation (RAG) model to accelerating incident response in enterprise mainframe operations. Specifically, how well can a retrieval-based system speed up responses without adversely impacting the veracity, security, governance, and usability of enterprise mainframe systems? We combine key themes from RAG research, AIOps, information retrieval, and enterprise security standards to form a model RAG architecture to accelerate incident response in an enterprise mainframe operating environment. Our analysis showed that hybrid retrieval systems, blending BM25 and dense passage retrieval with cross encoder reranking, provide the most effective setup for using RAG on the varied content of mainframe information systems. As part of our research, we created a metrics system that measures retrieval, the accuracy of answers generated using these answers (or faithfulness), and how fast the system can fix problems. Though there are no existing performance benchmarks specifically for using RAG for analyzing mainframe data, there are analytical comparisons that can be made to performance benchmarks for other AI-based incident management approaches, yielding potential incident response time improvements in the 25 to 40% range. For financial institutions that depend on mainframes to conduct the bulk of their financial transactions, like banks, this offers efficiency improvements while simultaneously lowering operational risk. A risk category global banks are required to maintain capital against under the Basel III framework and subject to heightened regulatory attention. Issues around how systems can be manipulated (hallucinations, knowledge corpus poisoning, and prompt injection attacks) or have data privacy and government regulations (such as the NIST AI Risk Management Framework and the OWASP LLM Top 10 for Security) are discussed in the context of these potential gains. The paper concludes that RAG systems offer an attractive solution for speeding up troubleshooting of mainframe incidents as long as they incorporate human oversight and countermeasures against attack and ensure that provenance and data lineage can be established and audited for accountability.

---

## uid: `doi:10.2139/ssrn.6910258`

- title: RETRIEVAL AUGMENTED GENERATION FOR PEDIATRIC EHR DATA INTEGRATION: EVALUATING RETRIEVAL FIDELITY AND OUTPUT ACCURACY ON SYNTHETIC CLINICAL RECORDS
- authors: VINOD RUFUS MOTANI
- affiliations: not stated
- posted: 2026-06-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6910258
- keyword hits: large language model, large language models, retrieval augmented

### abstract

The increased usage of EHRs has created an enormous amount of information generated from structured clinical and unstructured data in pediatric healthcare. Analyzing and efficiently integrating the EHRs for effective clinical decision support remains a challenge and thus require advanced AI techniques. RAG is becoming a new state-of-the-art AI technology that embeds information retrieval techniques to enhance large language models with more context (or knowledge). This paper outlines a RAG-based architecture for extracting and integrating information from pediatric patient electronic health records. To validate the framework experimentally, we have generated synthetic clinical records of patients that replicate different pediatric health scenarios encompassing symptoms, history, and diagnostic findings. The frame work extracts patient specific information from a clinical knowledge base and an integrated trained generative model for generating integrated clinical records and treatment/diagnostic recommendations. This paper assesses how well the integrated framework performs in terms of retrieval correctness generation accuracy, contextual consistency and information fidelity. A comprehensive evaluation of the implemented architecture is carried out using synthetic clinical EHRs of pediatric-related diseases. The experimental results indicate that RAG improves factual accuracy and reduces hallucination compared with generative transformer-based language models alone.

---

## uid: `doi:10.2139/ssrn.6922045`

- title: AIDE-LLM: Agentic Artificial Intelligence for Explainable Electrochemical Screening of Aflatoxin M1 and Atrazine in Agricultural Food Matrices
- authors: Kundan  Kumar Mishra, Akanksha Paul, Sriram Muthukumar, Shalini Prasad
- affiliations: not stated
- posted: 2026-06-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6922045
- keyword hits: agentic, large language model, llm

### abstract

Rapid screening of food contaminants is increasingly important for intelligent agriculture and supply-chain safety, yet current portable sensing systems often stop at numerical prediction and provide limited support for uncertainty handling, matrix effects, and field-level decision-making. Here, we introduce AIDE-LLM, an agentic artificial intelligence framework that transforms electrochemical sensor outputs into explainable, uncertainty-aware, and action-oriented food-safety decisions. Unlike conventional machine-learning pipelines that only classify sensor signals, AIDE-LLM combines electrochemical feature extraction, machine-learning prediction, replicate-consensus reasoning, matrix-aware interpretation, and large language model–guided report generation within a unified decision workflow. The framework was demonstrated for agricultural food-contaminant screening of Aflatoxin M1 and Atrazine in socked corn, corn flour, and plant-based protein matrices. Electrochemical outputs were converted into structured feature representations and classified into Low, Mid, and High risk categories. Across 195 samples, the base classifier achieved 93.33% accuracy, 93.38% weighted F1-score, and AUC = 0.985, with comparable performance across both contaminants. Error analysis revealed that misclassifications were concentrated near decision boundaries, including Low-to-Mid, Mid-to-High, and High-to-Mid shifts. To address this limitation, the LLM-agent layer identified discordant replicate groups, flagged uncertain cases, recommended retesting, and generated human-readable food-safety interpretations. This agentic triage strategy flagged 12 of 65 replicate groups and captured all 13 observed classification errors for review, while preserving automated acceptance for most samples. Stress testing under leave-one-matrix and leave-one-chip conditions further highlighted the need for intelligent deployment guardrails in agricultural sensing. This work establishes an AI-first framework for converting portable sensor data into reliable, explainable, and field-deployable decision intelligence for precision food-safety monitoring.

---

## uid: `doi:10.2139/ssrn.6920309`

- title: LLM-Driven Optimization of Cooperative Computation Offloading in Space-Ground Integrated Satellite Relay Networks
- authors: Peng Deng, Hao Chen, Ziyi Zhao
- affiliations: not stated
- posted: 2026-06-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6920309
- keyword hits: large language model, llm, retrieval-augmented

### abstract

The space-ground integrated network breaks the limitations of geographical isolation. The method of space-ground integrated network with mobile edge computing facilitates the wide-area distribution of computing resources, enabling users in remote areas to access services, without the need to backhaul data to distant cloud centers. To solve the problem of degraded service continuity across regions caused by dynamic network topologies and complex channel conditions in satellite relay networks, a Large Language Model (LLM)-driven optimization method for intelligent collaborative computation offloading is proposed in this paper. Retrieval-Augmented Generation (RAG) technology is employed to acquire expertise in satellite digital modeling. Through a prompt tuning strategy, the patterns of high-performing strategies are automatically analyzed. New, superior problem-solving instructions and offloading schemes are generated.This method adapts to dynamic environments without requiring extensive retraining. Simulation results show that the proposed LLM-driven optimization scheme outperforms baseline methods in minimizing the average completion time of computational tasks.

---
