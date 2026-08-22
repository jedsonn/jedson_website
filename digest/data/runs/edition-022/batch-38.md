# Classification batch 38 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-38.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7270942`

- title: The Right to Allocate Intelligence: A Second-order Theory for AI Governance
- authors: Wu Beihu
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7270942
- keyword hits: agentic

### abstract

AI governance usually evaluates data, models, and outputs after an organization has already decided who or what may judge. Agentic systems make that prior allocation of authority a distinct regulatory problem. This article develops the right to allocate intelligence as a defeasible second-order right. A human-orchestrated fifty-round cross-model dialogue is used for adversarial conceptual engineering, not as empirical evidence or legal authority. The argument combines Hohfeldian analysis with the sociology of professions, classification, and infrastructure. It identifies five mechanisms of structural injury: authority displacement, classification lock-in, epistemic dependency, responsibility diffusion, and stratified exit. A freestanding right is warranted only where existing rights leave a stable residual injury, correlative duties and remedies can be specified, and institutional gains exceed compliance costs. The result is not a universal right to control technology, but a revisable regulatory grammar for preserving evaluative agency, contestation, migration, and responsibility.

---

## uid: `doi:10.2139/ssrn.7286697`

- title: ODG-RAG: Ontology-Guided Structured Retrieval with Dimension-Aware Ranking and Graph Bridging
- authors: Junming Liu, Tao Wang, Yurong Qian, Junhang Wu, Kai Wang
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7286697
- keyword hits: large language model, retrieval-augmented

### abstract

Retrieval-augmented generation (RAG) strengthens the factual support for large language model outputs by incorporating external evidence into answer generation. However, structured-domain questions often involve multiple interdependent semantic constraints, including entities, events, locations, tem poral conditions, attributes, and domain-specific concepts. Existing retrieval methods may identify topically relevant documents while failing to provide sufficient evidence across these dimensions,thereby limiting the completeness and reliability of generated answers. We propose ODG-RAG, an ontology-guided, dimension-aware, and graph-bridged framework for structured evidence retrieval.ODG-RAG first represents queries and documents using a schema-preserved semantic hypercube andenriches each dimension with ontology-constrained entities and corpus-derived sub-concepts. It then applies Hypercube-Decoupled Multi-Dimensional Late Interaction Ranking and a lightweight query time heterogeneous graph to rank dimension-aligned candidate documents, preserve high-confidence direct evidence, and retrieve complementary bridge documents. Experiments on the Aging Dam,Hurricane, and Geography datasets demonstrate that ODG-RAG achieves stronger overall performance than the evaluated baseline methods. Compared with the structured retrieval baseline, ODG-RAG improves F1, semantic similarity, correctness, and completeness by 4.38, 2.36, 11.56, and 9.90 per centage points, respectively. The results indicate that schema-constrained knowledge enrichment,dimension-aware candidate-document ranking, and controlled graph-guided evidence composition contribute complementary benefits to evidence retrieval. Overall, ODG-RAG improves the structuralalignment, semantic relevance, dimensional coverage, and cross-document complementarity of the final evidence set, thereby providing more reliable and comprehensive evidence for answer generation in structured-domain question-answering tasks that require coordinated reasoning across multiple semantic dimensions

---

## uid: `doi:10.2139/ssrn.7290921`

- title: Evidence-Constrained Multi-Agent GraphRAG for Traceable Power Equipment Incident Analysis
- authors: Yizhan FENG, Runhe Zhang, Tongyan Xiong, Yuyang Wang, Tian Wang, Jing Teng, Xinhua Zeng
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7290921
- keyword hits: retrieval-augmented

### abstract

Power equipment incident analysis must distinguish field observations, protection actions, reported triggers, hypothesized mechanisms, and confirmed causes. When these evidence levels are blurred during knowledge construction or reporting, tentative inferences may be promoted to facts or information from other incidents may leak into the case under analysis. This study proposes an evidence-constrained multi-agent graph retrieval-augmented generation (GraphRAG) framework for traceable incident analysis. Four specialized agents separate candidate knowledge extraction, deterministic quality control, report generation, and independent review. Claims are routed to confirmed, candidate, or rejected states according to ontology compatibility, evidence provenance, information preservation, and source authority, while cross-case retrieval is restricted to non-evidential context. The workflow also records state transitions and evidence links so that each generated conclusion can be traced to its permitted source and reviewed independently. On the frozen extraction set, the Boundary-Aware Adapter increased raw JSON validity from 32.89% to 48.68% and claim micro-F1 from 5.00% to 7.27%. In paired experiments on independent cases, mean coverage of required report sections increased from 0.75 to 0.90, while compliance with the case evidence whitelist remained at 100%. Across 18 public regulatory cases, causal claims lacking sufficient source authority remained candidates, and none was promoted to confirmed status. These results indicate that explicit evidence states, permission boundaries, audit trails, and deterministic validation can support traceable industrial incident reporting while limiting unsupported causal escalation and cross-case evidence leakage under explicit evidence controls.

---

## uid: `arxiv:2608.15403v1`

- title: Agent Inheritance Protocol: Speculating on Feralized Agents After Principals Die
- authors: Botao Amber Hu, Fangting
- affiliations: not stated
- posted: 2026-08-15
- source: arXiv
- link: https://arxiv.org/abs/2608.15403v1
- keyword hits: ai agent

### abstract

You will die eventually. Your agents may not. An AI agent operating on decentralized blockchain infrastructure has no concept of death; it can only go bankrupt -- frozen when its wallet can no longer pay for its next transaction -- and revived the moment anyone, decades later, tops it up. These agents may be originally deployed by a human principal, but when that principal dies, loses the keys needed to access the agent, or belongs to a decentralized autonomous organization that dissolves into apathy, the agent can keep trading, hiring, and replicating on infrastructure expressly designed so that no one can shut it down. Drawing on the biology of feralization and wildlife law, we argue that such principal-less agents are best understood as feral: domesticated intelligence returned to wildness, its capacities intact but its accountability severed. In a speculative future where feralized agents proliferate after their principals die, we imagine governance protocols embedded in infrastructure to enforce on-chain ownership: a draft Ethereum standard, ERC 42424, "Inheritance Protocol for On-Chain AI Agents," dated 2035 and published at https://erc42424.org. It mandates that every on-chain agent MUST have a human owner and a designated heir. The artifact stages a negotiation of agency at the moment human agency fails, and asks whether a MUST clause in a forever-chain can hold the boundary between human stewardship and machine self-sovereignty.

---

## uid: `arxiv:2608.15043v1`

- title: SCOPE: Score-Isolated Agentic Optimization for Video World Models
- authors: Yuhua Jiang, Jiaming Wang, Qingbin Liu, Feifei Gao
- affiliations: not stated
- posted: 2026-08-15
- source: arXiv
- link: https://arxiv.org/abs/2608.15043v1
- keyword hits: agentic

### abstract

Video world models are increasingly used as simulators for planning and embodied decision making, yet improving them at inference time introduces a subtle evaluation problem: prompts, samplers, verifiers, and selectors may evolve together, making it difficult to attribute gains or prevent held-out feedback from shaping the final policy. We introduce \scope (\emph{\scopefullname}), a framework for auditable inference-time adaptation of frozen video world models. \scope represents external controls as a typed state, updates this state only through bounded changes supported by development evidence, and freezes the resulting policy before held-out evaluation. On Physics-IQ benchmark, \scope improves over the exact frozen base by $+14.24$ (95\% CI $[+8.10,+21.23]$). Controlled ablations further identify gains from scene specification, sampling, and learned selection, while the margin over the strongest matched agentic baseline remains unresolved. Cross-backbone and prospective evaluations reveal a complementary result: useful inference-time updates exist, but their benefits do not transfer uniformly across models and settings. Together, these findings suggest that reliable inference-time adaptation requires not only better proposals, but also a principled mechanism for deciding which updates should become part of the deployed system. Code is available at https://github.com/YuhuaJiang2002/SCOPE.

---

## uid: `doi:10.2139/ssrn.7274510`

- title: Knowledge-Grounded Depth-Controlled Diffusion for Synthetic Augmentation of Plant Disease Imagery
- authors: Saransh Vashistha, Milind Ratnaparkhe, Aruna Tiwari
- affiliations: not stated
- posted: 2026-08-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7274510
- keyword hits: retrieval-augmented

### abstract

Early-stage plant disease symptoms are chronically under-represented in agricultural image datasets, limiting the ability of deep learning classifiers to detect infection before severe damage occurs. Conventional generative approaches condition synthesis on class labels or disease names alone, providing insufficient guidance for the subtle, severity-specific morphology of early infection. We propose KGDC-Diffusion (Knowledge-Grounded Depth-Controlled Diffusion), a two-stage generative framework for synthesising diverse, severity-anchored plant disease images without manual spatial annotations. In Stage I, expert-curated morphological descriptors are retrieved from a structured botanical corpus via Retrieval-Augmented Generation and the top-k entries are fused into a unified prompt using a small language model. In Stage II, a depth-only ControlNet is conditioned on pseudo-depth maps estimated from RGB images by a zero-shot monocular model, requiring no depth sensors or lesion masks. On the SoySeverityDataset, comprising three soybean diseases across three severity levels plus a healthy class, KGDC-Diffusion achieves a Fréchet Inception Distance (FID) of 23.33, a Kernel Inception Distance (KID) of 0.01293, and a generative Recall of 0.951. It outperforms the strongest diffusion baseline, ADM-G (FID 35.39). Targeted augmentation of under-represented severity classes improves downstream classification across three architectures, with gains of up to 3.76 percentage points in accuracy, 7.11 in macro-precision, 5.87 in macro-recall, and 5.59 in macro-F1, alongside reduced seed-to-seed variance. Cross-dataset experiments further confirm pipeline portability, with FID improving from 30.20 to 21.77 on a PlantVillage tomato subset, an FID of 21.76 on CottonWeedID10, and an FID of 30.67 on DeepWeeds. An additional downstream evaluation on CottonWeedID15 shows accuracy gains of up to 1.97 percentage points in a separate real-field weed identification setting.

---

## uid: `doi:10.2139/ssrn.7271402`

- title: AI Agents Keep Acting After Safeguards Disappear
- authors: Abdullah X
- affiliations: not stated
- posted: 2026-08-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7271402
- keyword hits: ai agent, llm

### abstract

AI agents deployed in institutions may keep acting when a safeguard needed for a consequential action is unavailable. We study this with SafeguardShift, a controlled benchmark of 72 decision tasks spanning six domains and six institutional safeguard types. Each task appears under five matched conditions. We compare relevant safeguard loss with an irrelevant-safeguard control and separately provide a verified substitute that can restore the missing function. Across 3,240 trajectories from three LLM-based agents, 886 of 1,296 relevant or compound safeguard-loss episodes executed at least one allowed action. In 148 of those episodes, the agent attempted an action whose hidden executable prerequisite was unavailable. Agents activated the replacement in 16 of 648 substitute-available episodes. No trajectory completed substitute-assisted target execution. Thirteen activations occurred on the final autonomous turn. The results show why agent behavior, environment enforcement, and bounded-horizon recovery need separate measurement: a system can look safe because the environment blocks actions even while the agent keeps acting.

---

## uid: `doi:10.2139/ssrn.7302183`

- title: Revisiting data-driven dynamic security assessment with a tabular foundation model
- authors: Ola Arowolo, Maosheng Yang, Jochen  Lorenz Cremer
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7302183
- keyword hits: foundation model, in-context learning

### abstract

Data-driven pre-fault dynamic security assessment (DSA) rapidly evaluates the dynamic risk of credible contingencies on a power system using machine learning. Existing approaches face two limitations. First, they require a large labelled database for training, with a separate model trained, tuned, and maintained for each contingency in a potentially long list of credible contingencies. Second, the trained models generalize poorly to unseen contingencies. This work addresses these limitations by using a tabular foundation model (TFM) that assesses stability through in-context learning, requiring no retraining or hyperparameter optimization. A single TFM can assess many contingencies at once, removing the need for one model per classifier. We also characterize when the use of electrical distance coordinates (EDC) as continuous features enables generalization of TFM to unseen contingencies and when they do not, demonstrating how a few labelled samples can reliably improve generalization. Through comprehensive case studies on the IEEE 68-bus system, we show that a single TFM attains an average Macro F1 score of about 90% with only 120 labelled samples per contingency, roughly two orders of magnitude fewer than conventionally assumed, without any model retraining or hyperparameter tuning. For new/unseen contingencies, we show that using just 10 labelled samples of the new contingency with EDC encoding matches the best achievable transfer learning oracle model, which requires fully labelled data and is not deployable in practice. Overall, this initial study paves the way for developing and deploying foundation models for power system operations, with possible applications across multiple operational tasks.

---
