# Classification batch 40 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-40.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7305684`

- title: FIWARE MCP Agent: A Policy-Aware Interworking Middleware for MCP-Enabled AI Agents and NGSI-Based Context Platforms
- authors: Thanh-Trung Nguyen, Dong  Nam Truong
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7305684
- keyword hits: ai agent

### abstract

AI agents increasingly access external resources and invoke tools, yet their capabilities remain weakly integrated with shared context-management platforms used by IoT systems, digital twins, and operational applications. This paper presents the FIWARE MCP Agent, a policy-aware interworking middleware that connects MCP-enabled AI agents with NGSI-based context platforms without modifying the Context Broker. The framework maps MCP resources to NGSI entities, selected prompts to workflow-template descriptors, workflow-derived runtime state to NGSI-v2 attributes or NGSI-LD Properties and Relationships, and MCP tools to governed command or action lifecycles. A version-aware mapping registry and execution layer enforce synchronization direction, policy and schema checks, acknowledgement, idempotence, error propagation, and trace reconstruction. We implemented the framework with Orion and Orion-LD and evaluated it through mapping and failure-path tests, controlled middleware workloads, deployed broker–MCP–external-tool workflows, authenticated concurrency, and selected NGSI-LD semantics. Internal middleware processing remained sub-millisecond. Across three clean deployments, all 270 serial workflows completed with 100% trace completeness; overall mean and p95 deployed software-chain latencies were 64.21 and 85.97 ms. All 360 authenticated concurrent workflows completed without errors or timeouts; throughput peaked at 13.16 workflows/s at concurrency four, and all 18 authorization-negative probes returned the expected 401/403 outcomes. The NGSI-LD evaluation completed 90/90 workflows with 100% trace completeness, while 18/18 negative probes produced the expected rejections. These results provide implementation-backed evidence that MCP-facing resources and capabilities can participate in shared NGSI context infrastructures through explicit mappings and auditable execution lifecycles, while broader multi-domain and production-scale validation remains necessary.

---

## uid: `doi:10.2139/ssrn.7303181`

- title: AgriLM: Cross Modal Visual Language Reasoning with Multi Vector Retrieval for Multimodal Knowledge Analytics
- authors: Veerababu Reddy, Bhanu Siva Prakash Boyapati, Venkata  Sai Teja Vadalasetty
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7303181
- keyword hits: qwen, retrieval augmented

### abstract

Multimodal visual reasoning in computer graphics requires integrating images, text, and structured knowledge within a unified representation. Existing approaches often rely on coarse fusion and weak grounding, limiting fine grained cross modal alignment and reliable retrieval. AgriLM, an evidence grounded multimodal visual language framework for scalable visual reasoning. Agricultural decision making increasingly relies on complex multimodal data (image, text, soil reports) emerging from scientific literature, plant disease images and soil diagnostic reports archives. The architecture combines a Vision Transformer (CLIP ViT-L/14) with a domain adapted language model (Qwen-14B) via a cross modal transformer, enabling token level interaction between visual and textual features. A multi vector representation strategy preserves entity level semantics, improving cross modal correspondence and retrieval fidelity. These representations are indexed using FAISS based approximate nearest neighbor search for efficient large scale retrieval. A retrieval augmented generation module incorporates top k evidence during inference to produce grounded and interpretable outputs. Experiments demonstrate strong performance (92.8% accuracy, 0.91 F1, 0.94 nDCG) with competitive latency. The results show that combining cross modal transformers, multi vector representations, and retrieval aware generation provides an effective framework for scalable multimodal visual reasoning in visual computing applications. AgriLM code repository is available at https://github.com/BoyapatiBhanu/AgriLM.The dataset and resources are archived on Zenodo: https://doi.org/10.5281/zenodo.19704388.

---

## uid: `doi:10.2139/ssrn.7303207`

- title: Hydrothermal performances of flexible wickless looped pulsating heat pipes with smooth and roughened boiling surfaces
- authors: Wei  Ling Cai, Zi-Yang Chen, Shyy Woei Chang
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7303207
- keyword hits: prompting

### abstract

This experimental study investigates the hydrothermal performance of flexible wickless looped pulsating heat pipes (WLPHPs) by decoupling the individual and combined effects of heating power, condenser thermal resistance, evaporator-to-condenser inclination angle, and boiling surface morphology across vertical and horizontal orientations. At pseudo-steady states within smooth serpentine evaporator channels, elongated Taylor bubbles coalesce downstream into annular regimes while undergoing severe asymmetric deformation driven by gravitational stratification. Conversely, roughened surfaces destabilize these conventional Taylor bubbles, prompting rapid breakup into annular/mist flows that expand the vapor-liquid interfacial area and significantly enhance heat transfer. This thermal enhancement is driven by the micro-cavities of the textured surface, which lower the critical wall superheat for boiling incipience, synergized with macro-looped circulation and localized slug pulsations. The textured WLPHP thereby reduces overall thermal resistance below the minimum thresholds reported in existing literature while considerably boosting effective thermal conductivity. Furthermore, a novel spectrum-thermal synergy framework is pioneered to unify macroscopic thermal metrics using a single dimensionless, frequency-weighted agitation energy derived from spectral pressure fluctuations. These findings successfully bridge micro-scale spectral instabilities with macro-scale thermal behaviors, providing a foundational strategy to establish empirical correlations and validate flexible WLPHPs for advanced thermal management.

---

## uid: `doi:10.2139/ssrn.7289458`

- title: FLAP-X: A Dual-Leaf Attestation Protocol for Cross-Agent Regulatory Governance with Retrospective Cryptographic Verification
- authors: Maria Luz Madariaga
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7289458
- keyword hits: agentic

### abstract

Cryptographic verification presupposes determinism: a hash either matches or it does not, and a signature either holds or it fails. Agentic AI systems violate this precondition-identical inputs may produce different outputs, so there is no fixed expected value against which behaviour can be verified, and the naive application of cryptographic audit to AI fails at the first step. This paper takes a different route: separate what can be held invariant from what cannot. Credentials, delegation chains, prompt-template versions, access profiles, and controlexecution records are invariant by construction; model output is not. FLAP-X anchors the invariant set cryptographically and governs the variable residual with a calibrated tolerance, making non-deterministic multiagent systems retrospectively auditable. The dual-leaf attestation structure follows from this separation: Leaf 1 at the decision layer captures clause discharge, controls fired, and output hash; Leaf 2 at the workflow layer captures orchestration, delegation, and template version; the leaves are cross-linked and hash-bound to a principal chain rooted in a human agent owner. A four-check verification protocol operates across both surfaces. We parameterise a 15-condition test protocol in four parts-core verification (8), adversarial (3), governance lifecycle (3), and a comparative experiment (1) demonstrating two fault classes a single-surface record cannot handle: output substitution, which the single-surface record passes as a false negative, and surface attribution, which it cannot distinguish. We report honest negatives: adjacent-agent collusion producing mutually consistent false attestations passes verification, and a stolen signing key defeats signature checks; both are stated trust-boundary limitations addressed by the lifecycle layer, not the attestation layer. Effectiveness of the lifecycle controls at production scale remains future work; the author is actively seeking an empirical validation partnership.

---

## uid: `doi:10.2139/ssrn.7267523`

- title: Fermented Polygonatum kingianum polysaccharide exerted enhanced anti-obesity effects by modulating the gut microbiota–GDCA-TGR5 axis
- authors: Lin Liu, Yanli Li, Xiangmin Pan, Kai Zhang, Fanghan Yang, Dahui Liu, Wensong SUN, Pan Li
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7267523
- keyword hits: prompting

### abstract

Probiotic-fermented Polygonatum kingianum polysaccharide (FPKP0) was previously confirmed to exhibit enhanced anti-adipogenic activity in 3T3-L1 cells in vitro owing to altered structural, prompting an examination of whether this modified FPKP0 exerts superior anti-obesity effects in vivo via related mechanism in high-fat diet-fed mice. Physiological results showed that FPKP0 outperformed unfermented PKP0 accounting for reducing body weight, improving blood lipids, alongside alleviating hepatic steatosis and colonic damage. Correspondingly, FPKP0 reshaped the gut microbiota by boosting beneficial genera (especially Akkermansia muciniphila) and suppressing harmful bacteria (e.g., Dubosiella, Helicobacter). Integrated metagenomic and metabolomic analyses identified Akkermansia muciniphila and Glycodeoxycholic acid (GDCA) as the key microbial and metabolic underlying the in vivo effects of FPKP0, with a strong positive correlation (ρ = 0.83), indicating that FPKP0 may promote GDCA production by enriching Akkermansia muciniphila. Further mechanistic exploration revealed that TGR5 was confirmed as the downstream receptor mediating the metabolic effects of FPKP0-induced GDCA. Molecular docking and immunoblotting displayed that GDCA binds to TGR5 and activates the Gsα-PKA-CREB-UCP1 cascade to stimulate energy expenditure. This enhanced in vivo anti-obesity effect of FPKP0 could be attributed to modulation of the gut microbiota (AKK)-bile acid (GDCA)-TGR5 axis, supporting the potential of FPKP0 as a functional food additive to combat obesity and related disorders.

---

## uid: `arxiv:2608.17744v1`

- title: Thinking in a Low-Resource Language: What SFT Builds, What RL Fixes, What Accuracy Cannot See
- authors: Ayoub Kirouane, Christos Petrocheilos
- affiliations: not stated
- posted: 2026-08-18
- source: arXiv
- link: https://arxiv.org/abs/2608.17744v1
- keyword hits: fine-tuning

### abstract

Take three frontier mixture-of-experts models (Alibaba, OpenAI, NVIDIA; 3.6-4.0B active parameters each) and fine-tune them to reason in a low-resource language. On accuracy benchmarks almost nothing happens, and the benchmark itself is noise at this scale: changing only the random seed moves the score by 7.7 points, more than every data and recipe effect we measured. That null is our first result. The real changes live where accuracy cannot see. Base models never think in Greek: 0 of 1,000 reasoning traces, even when the question is Greek, so the model answers correctly while reasoning in a form its user cannot read, audit, or correct. After supervised fine-tuning (SFT), every released checkpoint reasons in the language of the question on ~98% of items, one family at 3x fewer tokens, with judged grammaticality improving on all four models and general ability within a few points of each base: nothing was forgotten, and fluency was gained. We propose six behavioural dimensions that make such changes measurable, each gated to reject any metric that correlates with output length, and we report how our own instruments lied: six failures, each caught by a control. What SFT cannot do is fix its own defects: a quarter of answers skip the requested format, answers leak into the reasoning channel, and an explicit "think in English" is obeyed under half the time. Reinforcement learning with verifiable rewards, pre-registered before training, fixes the first two outright (fallback 24% to 2.5%, leak 3.5% to 0.0%, both against a flat random-reward control) and moves the third (+9.1pp), while the Greek reasoning habit survives an accuracy-only gradient untouched. We release five checkpoints. The instruments, the controls and the pre-registration travel to any low-resource language; Greek is the case that let us measure them.

---

## uid: `doi:10.2139/ssrn.7288898`

- title: The Language That Prevails The Paradigmatic Interpretation Rule and the Global Scholarship on the Abuse of Programming-Language Semantics in ICT-Governed Systems and Procedures: A Comparative Study of 304 Verified Works
- authors: Filip Vukov
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7288898
- keyword hits: ai agent

### abstract

Where the meanings of human legal language and the functional meanings of programming languages diverge inside ICT-governed systems and procedures, which meaning prevails? The Paradigmatic Interpretation Rule proposed by the first author answers: the human legal meaning-in use, in synergistic co-working with automated AI agents, ICT and robotic systems, and in their autonomous operation, whether or not legal supervisors are present-as a consequence of the hierarchy of legal norms of constitutional nation states; and it characterises the covert private alteration of the functional meaning of a nation state's official words in automated processes as a hostile takeover of the national official language, the privatisation of human language without legal ground. This article measures the Rule against a verified corpus of 304 works from six literatures across Europe, the United States, Canada, Australia and New Zealand, and Asia (1974-2026), classifying the stances of sixty-six leading authors on the Rule's five elements. A broad multi-regional convergence supports the Rule's conflict core and its hierarchical ground; a supervision paradox-doctrinal and technical evidence that oversight cannot detect covert semantic divergence-supports its supervision-independence; the factual premise of covert alteration is established science, while its normative synthesis is original to the Rule; and no work in the corpus asserts the ius cogens/international-crime characterisation as lex lata, which the article preserves through a three-layer derivative reading (cybercrime treaty offences in force; state responsibility for sovereignty violations; existing Rome Statute categories committed by cyber means; an autonomous offence de lege ferenda). The article further contributes the authenticitygap argument-executable code as an unofficial translation of the enacted text-a three-register taxonomy of semantic capture, and the constitutional specification tying the Rule to the rightsprotecting hierarchy from which it draws its authority.

---

## uid: `doi:10.2139/ssrn.7307799`

- title: DPACT: A Framework for Identity, Accountability, and Task-Scoped Authority in Autonomous AI Agent Systems
- authors: Sahil Agarwal
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7307799
- keyword hits: ai agent

### abstract

Autonomous AI agents are increasingly deployed as operational actors that read data, call tools, update systems, and communicate with users. Traditional identity and access management assumes that actors are either human users or deterministic service accounts. Agents violate this assumption: they act under delegated authority, compose actions at runtime, and may retain credentials beyond the task that justified them. This paper introduces DPACT, a five-dimensional framework for governing agent identity: Delegation, Policy, Audit, Context, and Time. DPACT provides a formal model of task-scoped authority, a taxonomy of identity failures, a maturity rubric, a reference architecture, an implementation profile, and an evaluation method for public incidents and representative agent patterns. The framework is mapped to deployable controls such as OAuth token exchange, capability tokens, policy decision points, short-lived workload identity, continuous authorization, structured audit logs, and revocation mechanisms. We apply DPACT to OpenClaw-style personal agents, the McHire AI hiring workflow incident, indirect prompt injection, multi-agent systems, autonomous coding agents, attended command-line coding assistants, and the Air Canada chatbot ruling. The analysis shows that agent trust is not a property of a model alone. It is an outcome of verifiable delegation, bounded policy, accountable audit evidence, contextual authorization, and time-limited authority.

---
