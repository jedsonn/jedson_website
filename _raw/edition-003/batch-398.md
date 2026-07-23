# Classification batch 398 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-398.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6866422`

- title: Attested Governance: Runtime Integrity for Autonomous Systems
- authors: Jack Brennan
- affiliations: not stated
- posted: 2026-06-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6866422
- keyword hits: ai agent

### abstract

Autonomous AI systems face four critical governance problems: attestation of subject identity and authorized behavior, runtime enforcement of policy, generation of cryptographically meaningful evidence, and continuity verification of decision history. These four problems are coupled by design: any architecture that solves them must address all four under one trust root. The case making them actively pressing now is the rise of autonomous AI agents that manage workflows, invoke external tools, and modify state at production scale without cryptographic records that survive forensic scrutiny. We name this property inseparability. The architecture either binds all four pillars under one cryptographic chain (integrated) or it does not (composed). This commitment is made at the time of design. Composing independent provenance, policy, attestation, and logging produces parallel verification with multiple independent trust roots. Integration requires the architectural commitment to a unified receipt format and trust model from system genesis. We define Attested Governance as the integrated category and present AGA as one implementation. The category supports multiple architectural realizations; Section 3.4 reviews peer instantiations. We derive the integration property within an explicit trust boundary that names two assumptions upfront: the issuing authority and the portal are not compromised. We present AGA in detail including its primitive choices, trust model design, and operational framing. We anchor the architectural pattern in three independent regulated sectors (industrial control under ISA/IEC 62443-3-3 and NIST SP 800-82, custody transfer measurement under API MPMS Chapter 21.1, and electronic records integrity under 21 CFR Part 11) where the same four-pillar pattern has operated for decades under high consequence requirements where evidence must survive external audit. A reference implementation establishes an empirical baseline: a complete signed measurement cycle completes in approximately 4.94 ms on commodity hardware (reference implementation, v0.9.1 snapshot; see Section 4.7), with post-quantum hybrid signing adding only 0.39 ms per governance decision (Hybrid Sign + Verify mean). We propose six minimum criteria for standardization within the category, identify four open research directions, and identify three IETF working groups (SCITT, RATS, WIMSE) as standardization pathways. The proposed category is motivated by high consequence contexts demanding forensic review. We do not claim it applies to all AI governance. The architectural debt of partial governance becomes more expensive to retire as autonomous systems scale into higher consequence deployments, and the same forensic scrutiny pressure that drove regulated sectors (Section 5) toward integration applies here. Whether a coherent category with interoperable implementations emerges depends on whether the integration question is engaged structurally now.

---

## uid: `arxiv:2607.09702v1`

- title: Fundamental market design as a layer of AI-agent alignment
- authors: Omar Inverso, Emilio Tuosto, Dragisa Zunic
- affiliations: not stated
- posted: 2026-06-21
- source: arXiv
- link: https://arxiv.org/abs/2607.09702v1
- keyword hits: ai agent

### abstract

This paper argues that AI-agent alignment in markets should not be understood only as a property of agents, but also as a property of the interaction infrastructure in which agents act. In financial markets, this infrastructure is the market core: the rule system that determines how orders enter, interact, match, persist, and stabilize. If this fundamental interaction layer allows or rewards undesired behaviour, then higher-level alignment of agents may be insufficient. We propose to view fundamental market design as a layer of AI-agent alignment. Alongside the important work of computational economics in modelling agents, strategies, and learning, we focus on a complementary but more fundamental layer: the formal modelling of the market core itself. Market design, especially at the level of the core mechanism, can benefit from a rigour characteristic of theoretical computer science. This gives a transparent-box model of the market, whose core properties can be formally specified and reasoned about. It also lets us treat the trading venue not as a static order book, but as a computational process combining resident orders with incoming order flow, and ask which computational model, perhaps yet unknown, naturally lies at its core. This perspective is especially relevant for markets populated by adaptive or AI agents. Such agents may learn what the mechanism rewards, including speed, delay, liquidity provision, or manipulation. These behaviours are not only properties of individual agents, but may emerge from the agent-mechanism system. We therefore argue that transparent formal models of market cores can support incentive-oriented analysis and the design of mechanisms in which desirable behaviours are structurally favoured and undesirable behaviours are harder to sustain.

---

## uid: `doi:10.2139/ssrn.6871318`

- title: From Technologist to Business Architect: The CIO's Evolving Role as Enterprise AI Strategist and Governance Leader
- authors: Sunil Gentyala
- affiliations: not stated
- posted: 2026-06-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6871318
- keyword hits: ai agent

### abstract

Corporate hierarchies rarely reconfigure themselves overnight, yet the Chief Information Officer role has undergone precisely that kind of abrupt structural upheaval. Four independent industry surveys conducted between late 2024 and early 2026 (Foundry/CIO.com, n=1,156; Deloitte, n=622; Gartner, n=3,186; McKinsey, n=632) converge on a striking portrait: 65% of CIOs now report directly to the CEO, 36% carry profit-and-loss accountability, and 80% spearhead enterprise AI evaluation. Grounding these practitioner findings in upper echelons theory, strategic alignment theory, and established IT governance frameworks, this paper documents the metamorphosis and contends that governing autonomous AI agents constitutes the CIO's most consequential emerging obligation. We scrutinize the security vulnerabilities that the Model Context Protocol (MCP) introduces into enterprise architectures, marshaling evidence that 80% of organizations have encountered hazardous AI agent behaviors and that 41.7% of audited MCP deployments harbor exploitable weaknesses. We then propose ContextGuard, a zero-trust governance architecture purpose-built for AI context protocol security, and advance three falsifiable research propositions linking CIO strategic positioning, zerotrust governance maturity, and organizational AI value realization.

---

## uid: `doi:10.2139/ssrn.6966955`

- title: Breast Lesion Classification from Raw Ultrasound RF Signals: Lesion Level Comparison with Adapted Foundation Models
- authors: Yassine Gannoune, Sara Bakkali, Hajar Saikouk, Ahmed El Hilali Alaoui
- affiliations: not stated
- posted: 2026-06-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6966955
- keyword hits: fine tuning, foundation model

### abstract

Breast ultrasound is widely used for lesion characterization, but most deep learning systems rely on reconstructed B-mode images, where the original RF signal is transformed during image formation. Learning directly from raw radio-frequency (RF) data offers an alternative, but its value for breast lesion classification remains unclear. In this study, we proposed an RF architecture with four CNN models that use native RF patches, envelope patches, dual-stream fusion, and entropy-guided attention. Their predictions were combined in an RF ensemble. We evaluated the proposed RF architecture on OASBUD using lesion level grouping and compared it with foundation models adapted to the same dataset, including time series models trained on RF signals and ultrasound vision models trained on B-mode images. Using 100 lesions from 78 women, the highest AUC was achieved by a fully fine tuned time series foundation model at 0.939. The best image based foundation model reached an AUC of 0.903, while the proposed RF ensemble reached 0.839. These results show that useful lesion information remains accessible in RF signals before standard image formation. They also show that the foundation models we adapted to OASBUD reached the highest AUC after full fine tuning, while the proposed RF architecture achieved strong results with a much smaller model.

---

## uid: `doi:10.2139/ssrn.6981421`

- title: A Dataset Construction Method for Monocular Depth Estimation Based on Prior Diffusion Models and Multi-Dimensional Consistency Constraints
- authors: yubo song, Weibin Li, zhanlin li
- affiliations: not stated
- posted: 2026-06-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6981421
- keyword hits: fine-tuning, foundation model

### abstract

Monocular Depth Estimation plays a crucial role in fields such as autonomous driving and 3D reconstruction. However, acquiring high-precision depth datasets heavily relies on expensive sensor equipment, resulting in high data collection costs and narrow scene coverage, which limits the generalization ability of models in complex real-world scenarios. In recent years, utilizing pre-trained vision foundation models to generate pseudo-labels for knowledge distillation has emerged as an effective approach to alleviate data scarcity. Nevertheless, selecting an appropriate teacher model and ensuring the geometric structure and edge accuracy of pseudo-labels in complex scenes remain formidable challenges. To address these issues, this paper proposes a fast, low-cost method for constructing large-scale monocular depth datasets. First, a multi-criteria model quantitative evaluation system is established, encompassing mirror consistency, depth gradient error, and zero-shot generalization stability. Based on this system, the generative diffusion model, Marigold, is selected as the optimal pseudo-label teacher model. Second, to resolve sporadic noise and local artifacts during offline generation, this paper innovatively introduces mirror consistency constraints and edge consistency constraints, leveraging the equivariance of geometric transformations to filter out unstable predictions. Based on the proposed generation and dual-filtering paradigm, a large-scale monocular depth pseudo-label dataset comprising approximately 0.25M samples is successfully constructed using the COCO unlabeled image library. This dataset achieves a high level of visual fidelity and global geometric consistency, significantly reducing reliance on expensive hardware equipment and facilitating unsupervised domain adaptation pre-training and fine-tuning tasks for downstream lightweight depth estimation models.

---

## uid: `arxiv:2606.25195v1`

- title: SoK: AI Secure Code Generation: Progress, Pitfalls, and Paths Forward
- authors: Rupam Patir, Keyan Guo, Haipeng Cai, Hongxin Hu
- affiliations: not stated
- posted: 2026-06-23
- source: arXiv
- link: https://arxiv.org/abs/2606.25195v1
- keyword hits: agentic, fine-tuning, prompting

### abstract

The increasing use of AI systems for code generation raises a central security question: what can today's models and coding agents actually do to produce secure code, where do they still fail, and what would move the field forward? Existing work has explored prompting, fine-tuning, reinforcement learning, and agentic workflows for secure code generation, but the field still lacks a systematic understanding of how these techniques improve security and why substantial failures persist. In this SoK, we systematize the progress, pitfalls, and paths forward for AI secure code generation. We introduce a three-level framework that measures models' natural-language understanding of secure coding principles, their code-level actuation of those principles during generation, and the knowledge--actuation gaps between the two. We instantiate this framework across models and coding agents on benchmarks covering both isolated function-level security and full web-application security. Our results show that secure-coding-principle understanding is a statistically strong predictor of code-level outcomes, including functional correctness, security, and joint functional-security correctness. Yet substantial knowledge--actuation gaps remain: models can recognize relevant security principles but still fail to translate them into secure and functional code. These findings offer a principle-centered account of where AI secure code generation stands today and identify concrete paths forward through principle-guided generation, evaluation, benchmarking, and agentic workflows.

---

## uid: `arxiv:2606.24799v1`

- title: OrbitForge: Text-to-3D Scene Generation via Reconstruction-Anchored Video Synthesis
- authors: Chenrui Fan, Paolo Favaro
- affiliations: not stated
- posted: 2026-06-23
- source: arXiv
- link: https://arxiv.org/abs/2606.24799v1
- keyword hits: fine-tuning

### abstract

Generic text-to-video models can be used as rich open-world scene priors. Despite the high quality of today's generated videos, they do not directly yield reliable 3D assets: camera motion is difficult to control, view coverage is partial, and frames often contain inconsistencies across time. We introduce OrbitForge, an adapter built from frozen video priors and per-prompt Gaussian Splatting reconstruction optimization that converts a single text-generated video into a canonical closed-orbit 3D Gaussian Splatting scene. We use 3D reconstruction as an anchor to improve the 3D consistency of the generated video. We obtain a preliminary 3D reconstruction from a first generated video via Deformable Gaussian Splatting with a robust MedianGS proxy. We render views from a prescribed orbit to detect missing viewpoints. OrbitForge uses the text-to-video model to complete only the missing views, and reconstructs the completed orbit into a final Gaussian Splatting scene. This design requires no task-specific video or multiview fine-tuning, avoids per-prompt score-distillation optimization, and does not progressively generate views one step at a time. We further argue that this setting demands coverage-aware evaluation: local smoothness alone rewards methods that never attempt a full orbit. On a frozen 300-prompt T3Bench-derived audit, OrbitForge reconstruction attains a 359.0-degree measured median span, raises originally unsupported-bin Q10 ImageReward from 8.07 to 16.36 relative to MedianGS-only reconstruction, while remaining competitive with VideoMV on the coverage-quality.

---

## uid: `arxiv:2606.24783v1`

- title: Paying to Know: Micro-Transaction Markets for Verified Product Information in Agentic E-Commerce
- authors: Filippos Ventirozos, Matthew Shardlow
- affiliations: not stated
- posted: 2026-06-23
- source: arXiv
- link: https://arxiv.org/abs/2606.24783v1
- keyword hits: agentic

### abstract

Commercial NLP treats the shopping chatbot as a recommender or a conversion tool: its job is to match a user to a catalogue entry and close a sale. We argue that the arrival of agent-native micro-payment rails (e.g., x402, AP2) changes what is scarce. When the buyer is an autonomous agent that can investigate exhaustively, the bottleneck is no longer matching products but acquiring trustworthy, decision-relevant information about them. We envision agentic e-commerce as a micro-transaction market for verified information: buyer agents spend fractions of a cent to progressively unlock seller- and reviewer-supplied data -- service histories, third-party test reports, bills of materials, audited sales and support metrics -- paid for a la carte under a freemium model, with reviewer trust scored reputationally. We sketch the architecture of such a market and argue that it rewards genuine product quality and yields truer competition than ranking-based storefronts. We then translate the vision into concrete NLP problems -- cost-optimal information acquisition, data pricing and negotiation, real-time entity resolution, grounded value exchange, and privacy-preserving persona modelling -- and argue that these, not chat fluency, deserve the field's attention.

---
