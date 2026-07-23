# Classification batch 405 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-405.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7042053`

- title: HIERARCHRAG: A Three-Layer Hierarchical Knowledge Graph for Provenance-Aware Retrieval-Augmented Generation
- authors: Luigi Barbato, Francesco Gargiulo
- affiliations: not stated
- posted: 2026-07-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7042053
- keyword hits: llm, retrieval-augmented

### abstract

Retrieval-Augmented Generation systems built on flat knowledge graphs irrecoverably discard provenance during entity aggregation, silently collapsing contradictory evidence from heterogeneous corpora into a single canonical node. This structural deficiency undermines reliability in high-stakes domains where conflicting evidence is common and claim-level traceability is a prerequisite for safe deployment. We present HierarchRAG, a RAG architecture whose core design principle is preserve, do not collapse: rather than merging observations of an entity into one representation, every extracted concept is materialised as an autonomous node permanently anchored to the exact document, page, and paragraph from which it was drawn. This principle is realised through a three-layer hierarchical knowledge graph. The first layer (L_1) retains the canonical entity representation compatible with existing graph-based retrieval pipelines. The second layer (L_2) represents each LLM-extracted concept as an independent node, interconnected via co-occurrence, semantic similarity, and contradiction edges. The third layer (L_3) anchors every concept to its physical origin in the source corpus. These additional layers enable two orthogonal capabilities: (i) fine-grained provenance tracking, whereby every claim in a generated answer is traceable to a precise location in the reference corpus; and (ii) automatic cross-document contradiction detection, whereby conflicting concepts of the same entity are systematically flagged at the L_2 layer and propagated to the parent L_1 entity node at ingestion time. Pairwise LLM-as-judge evaluation over 20 domain-specific questions against five competitive baselines on a biomedical corpus (2,349 text blocks; 5,711 entities; 23,711 concept vectors) demonstrates consistent retrieval quality improvements across all evaluated dimensions, with a global rank score of 75.4%.

---

## uid: `doi:10.2139/ssrn.7042057`

- title: HIERARCHRAG: A Three-Layer Hierarchical Knowledge Graph for Provenance-Aware Retrieval-Augmented Generation
- authors: Luigi Barbato, Francesco Gargiulo
- affiliations: not stated
- posted: 2026-07-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7042057
- keyword hits: llm, retrieval-augmented

### abstract

Retrieval-Augmented Generation systems built on flat knowledge graphs irrecoverably discard provenance during entity aggregation, silently collapsing contradictory evidence from heterogeneous corpora into a single canonical node. This structural deficiency undermines reliability in high-stakes domains where conflicting evidence is common and claim-level traceability is a prerequisite for safe deployment. We present HierarchRAG, a RAG architecture whose core design principle is preserve, do not collapse: rather than merging observations of an entity into one representation, every extracted concept is materialised as an autonomous node permanently anchored to the exact document, page, and paragraph from which it was drawn. This principle is realised through a three-layer hierarchical knowledge graph. The first layer (L_1) retains the canonical entity representation compatible with existing graph-based retrieval pipelines. The second layer (L_2) represents each LLM-extracted concept as an independent node, interconnected via co-occurrence, semantic similarity, and contradiction edges. The third layer (L_3) anchors every concept to its physical origin in the source corpus. These additional layers enable two orthogonal capabilities: (i) fine-grained provenance tracking, whereby every claim in a generated answer is traceable to a precise location in the reference corpus; and (ii) automatic cross-document contradiction detection, whereby conflicting concepts of the same entity are systematically flagged at the L_2 layer and propagated to the parent L_1 entity node at ingestion time. Pairwise LLM-as-judge evaluation over 20 domain-specific questions against five competitive baselines on a biomedical corpus (2,349 text blocks; 5,711 entities; 23,711 concept vectors) demonstrates consistent retrieval quality improvements across all evaluated dimensions, with a global rank score of 75.4%.

---

## uid: `arxiv:2607.01919v1`

- title: ElephantAgent: Contextual State Continuity in Agentic Systems
- authors: Jiankai Jin, Xiangzheng Zhang, Zhao Liu, Wenzhuo Xu, Dongdong Yang, Deyue Zhang, Quanchen Zou
- affiliations: not stated
- posted: 2026-07-02
- source: arXiv
- link: https://arxiv.org/abs/2607.01919v1
- keyword hits: agentic

### abstract

Agentic systems enhance their capabilities by invoking external tools and maintaining persistent memory. However, these external dependencies introduce novel attack surfaces. Recent tool and memory poisoning attacks show that maliciously crafted tool descriptors and poisoned memory can covertly bias agent behavior. These threats reflect a deeper issue: the lack of verifiable continuity in the agent's contextual state for planning and execution. We present ElephantAgent, a protocol that enforces Contextual State Continuity to defend against contextual state poisoning. Inspired by prior state-continuity mechanisms (e.g., Nimble), ElephantAgent extends this protection to the evolving contextual state of agentic systems. We define the contextual state as the bounded, security-critical subset of the agent's entire context (e.g., tool state and memory). Before processing each query, ElephantAgent recomputes the digest of the local contextual state and verifies it against the latest authorized digest. Using replicated trusted hardware, ElephantAgent maintains a linearizable ledger of authorized contextual state transitions and detects out-of-band state tampering. To handle in-band semantic abuse, ElephantAgent additionally provides Historical Traceability, enabling conditional post-hoc audit and recovery to a known-good prior state.

---

## uid: `arxiv:2607.01639v1`

- title: Autonomous discovery of traffic laws with AI traffic scientists
- authors: Xingyuan Dai, Yue Liu, Xiaoyan Gong, Qinghai Miao, Junyou Shang, Yutong Wang, Chao Guo, Yonglin Tian
- affiliations: not stated
- posted: 2026-07-02
- source: arXiv
- link: https://arxiv.org/abs/2607.01639v1
- keyword hits: agentic

### abstract

Universal traffic laws describe recurrent patterns in congestion, mobility and driving behavior across cities, providing a scientific basis for transportation planning, management and control. Their discovery, however, remains expert-driven, requiring candidate regularities to be identified from heterogeneous observational evidence or validated through intervention experiments. Although autonomous artificial intelligence (AI) systems have advanced scientific discovery in controlled laboratory settings, extending them to complex transportation domains remains a challenge. Here we present TrafficSci, an agentic AI system that formulates traffic-law discovery as an iterative, auditable workflow integrating evidence scoping, critic-judge hypothesis induction, and observational-interventional validation. Across four case studies spanning population, network, control and trajectory scales, TrafficSci autonomously rediscovers three established traffic laws and identifies an unreported intrinsic temporal memory scale in urban driving behavior, statistically consistent across eight cities and two trajectory datasets. TrafficSci provides a route for extending AI-driven scientific discovery from controlled domains to complex urban systems.

---

## uid: `doi:10.2139/ssrn.7044988`

- title: ACE: Adversarial Cross-domain Enhancement for Domain Generalization
- authors: Chaoyi Liu, Libo Huang, Zhulin An, Chuanguang Yang, Junlong Guo, Yongjun Xu
- affiliations: not stated
- posted: 2026-07-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7044988
- keyword hits: fine-tuning

### abstract

While deep neural networks have achieved remarkable success across visual recognition tasks, their efficacy relies on the foundational assumption that training and testing data are independent and identically distributed. In real-world deployment, this assumption is frequently violated by distributional shifts, where the target domain diverges from the source in terms of style, texture, or environmental conditions. Domain generalization (DG) addresses this challenge by learning models that generalize to unseen domains. Existing DG methodologies generally fall into regularization and data-centric strategies. Recent DG comprehensive evaluations reveal that data-centric augmentation can match or even surpass elaborate regularization methods, underscoring the critical importance of data-centric diversity. Data-centric DG approaches grounded in vicinal risk minimization (VRM) primarily operate via linear interpolation in pixel space, yielding unnatural artifacts and failing to provide non-linear semantic transitions. We propose \textbf{Adversarial Cross-domain Enhancement (ACE)}, a plug-and-play framework that redefines data augmentation through the lens of generative vicinal risk minimization (Generative VRM). Rather than interpolating pixels, ACE leverages the rich semantic prior of a pre-trained Latent Diffusion Model to traverse the geodesic manifold between source domains. By fine-tuning the LDM with a novel Maximum Entropy Domain Regularization adversarial optimization strategy, ACE synthesizes high-quality ``bridge'' samples that populate the undefined intermediate regions of the domain space. Distinct from static generative augmentation, ACE dynamically adjusts generated resultsconditioned on the classification network's training progress, compelling the generator to produce samples aligned with the ``blind spots'' of a domain discriminator. Experiments on PACS, Office-Home, and VLCS benchmarks confirm that ACE significantly improves deep neural network performance under distributional shifts, establishing a new state-of-the-art DG baseline. Meanwhile, as a plug-and-play framework, ACE can be seamlessly integrated into various architectures, including ResNet and vision-language models, to enable them to achieve DG performance.

---

## uid: `arxiv:2607.03640v1`

- title: Revealing Hidden Model Behaviors with Task-Specific Self-Reports
- authors: Taras Kutsyk, Bartosz Zieliński
- affiliations: not stated
- posted: 2026-07-03
- source: arXiv
- link: https://arxiv.org/abs/2607.03640v1
- keyword hits: fine-tuning

### abstract

Fine-tuning can give a language model a hidden behavior--it may give false answers under a narrow condition, or give harmful advice only when a prompt touches a particular topic. We introduce the Stabilized Adapter for self-Report (SAR), a lightweight LoRA adapter that makes a fine-tuned model describe its own hidden behavior in plain language, using only the model and the dataset it was trained on. Across seven implanted behaviors (plus a no-behavior control), SAR detects the hidden behavior in every one--even when the model has generalized into broad misalignment that the training data alone does not predict. Introspection Adapters (IA), the closest existing baseline, detects some behaviors from our suite but misses others entirely--and where it misses, it hallucinates, consistently reporting wrong behaviors. SAR retains positive signal on every setting where IA fails and halves the rate of hallucinations. This makes it much easier for practitioners to audit their models and obtain reliable answers to "what did my model actually learn?" type of questions.

---

## uid: `arxiv:2607.09744v1`

- title: A Theory of Least Autonomy in AI
- authors: Christophe Parisel
- affiliations: not stated
- posted: 2026-07-03
- source: arXiv
- link: https://arxiv.org/abs/2607.09744v1
- keyword hits: agentic

### abstract

Least privilege, the principle that an identity should hold only the permissions strictly required for its task, has been a foundational primitive of access control for decades. We argue that this principle is insufficient for agentic AI systems, which do not merely hold permissions but can combine, approve, and amplify them across workflows and system boundaries. We propose least autonomy as an appropriate generalization and develop a formal theory. First, we define a compositional blast radius d(a,b) that measures structural separation between actions in an enterprise hierarchy, combining an ultrametric tree with lattice-valued confidentiality, integrity, and control-context labels. Second, we define a directed agent influence graph G(theta). An arc from U to V requires a directed shared-resource write-to-read meeting or a conservative undirected agent-to-agent (A2A) communication meeting, and a meeting-conditioned influence potential at or above an externally selected policy threshold theta. A catalogue-radius profile supports calibration and audit of theta. Finally, we define a collusion predicate over graph reachability that detects authorization composition, decision manipulation, and cross-domain capability composition.

---

## uid: `arxiv:2607.02995v1`

- title: VISTA: Auditing Semantic Divergence in Vision-Language Models
- authors: Junchi Liao, Jiawen Deng, Fuji Ren
- affiliations: not stated
- posted: 2026-07-03
- source: arXiv
- link: https://arxiv.org/abs/2607.02995v1
- keyword hits: fine-tuning

### abstract

Vision-language models can exhibit visual concept-conditioned divergence: given images containing demographic features, corporate logos, or ideological symbols, some models produce unusually uniform responses that differ from what peer models say about the same input. These behaviors evade text-only audits because visual concepts cannot be isolated or substituted the way text tokens can. We present VISTA (Visual Inconsistency Screening Through Analysis), a black-box cross-model audit that couples semantic entropy with distribution-based divergence to flag model-specific anomalies. In a controlled study, we implant concept-conditioned stances in three VLMs via fine-tuning on small biased datasets and confirm that VISTA detects them. Auditing six VLMs across 19 topics, VISTA surfaces 142 high-suspicion cases (1.2%) and identifies selective refusal as a previously unreported divergence pattern, where models refuse demographic queries at rates varying from 0 to 65% across groups.

---
