# Classification batch 384 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-384.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6766758`

- title: From Connectivity to Commerce: Digital Infrastructure, Rural Entrepreneurship, and the AI Inflection Point A Comparative Study of India, China, and Southeast Asia
- authors: Sai Chand Bollu
- affiliations: not stated
- posted: 2026-05-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6766758
- keyword hits: ai agent, generative ai

### abstract

Digital infrastructure-internet connectivity, mobile penetration, and now artificial intelligence-is widely cited as a catalyst for rural entrepreneurship in developing economies. Yet the empirical record is sharply heterogeneous: China's Taobao Villages converted rural internet access into a documented ecommerce entrepreneurship phenomenon at massive scale (7,780 villages by 2022), while Southeast Asian economies converted mobile penetration into gig economy participation through super-app platforms. India, despite achieving near-universal mobile broadband affordability (data costs falling from 269/GB in 2014 ₹ to 9.18/GB in 2024) and a stated policy commitment to rural digital empowerment, has not yet produced a ₹ comparable structural transformation of rural entrepreneurial outcomes. This paper introduces the Connectivity-Capability-Commerce (C3) Framework to explain this divergence. The C3 Framework posits that digital infrastructure generates rural entrepreneurial outcomes only when entrepreneurs successfully traverse three sequential layers: Connectivity (access to digital infrastructure), Capability (ability to leverage digital tools for productive economic activity), and Commerce (capacity to generate sustained revenue through digital channels). We argue that the binding constraint on rural entrepreneurship is not the Connectivity layer-which India has largely addressed-but the Capability-to-Commerce transition, which requires platform ecosystems, financial infrastructure, trust mechanisms, and language-accessible tools that have developed differently across the three regions. We further introduce the concept of AI Compression-the mechanism through which generative AI and voice-based AI agents may collapse the Capability layer, enabling a direct Connectivity-to-Commerce transition for rural entrepreneurs who currently lack the digital literacy to traverse Capability independently. Drawing on data from World Bank, TRAI, Alibaba Research Institute, ASEAN Startup White Paper 2024, and Government of India Digital India reports, we provide the most comprehensive comparative analysis to date of how digital infrastructure translates-or fails to translate-into rural entrepreneurial activity across these three regions. The implications are direct for policymakers designing rural development programs, platform companies seeking rural market expansion, and researchers studying the digital economy's distributional effects.

---

## uid: `doi:10.2139/ssrn.6770624`

- title: Coherence as an Extension of the Organizational Design Canon
- authors: Anil Prakash Singh
- affiliations: not stated
- posted: 2026-05-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6770624
- keyword hits: ai agent

### abstract

This research note positions the Living Enterprise framework (Singh, 2026) within the organizational design canon. The framework is offered not as a replacement of Mintzberg, Galbraith, or Laloux, but as an extension of these traditions to a specific design problem: what organizational architecture is appropriate when AI agents perform most of the operational work, governance is continuous and runtime rather than periodic, and human judgment is concentrated at named coherence points rather than distributed across functional hierarchies. The note has three contributions. First, it specifies the intellectual lineage of the framework, identifying where it extends Mintzberg's configurations, Galbraith's Star Model, and Laloux's evolutionary purpose. Second, it presents the Spotify Model as a structured counter-case, showing how the documented failure modes of cargo-cult adoption inform the framework's design choices. Third, it names four empirical conditions under which the framework would predict its own failure, converting it from a closed system into a testable proposition. A research agenda for cross-industry validation is proposed.

---

## uid: `doi:10.2139/ssrn.6814922`

- title: Captioning Daily Activity Images in Early Childhood Education: Benchmark and Algorithm
- authors: sixing li, Zhibin Gu, Ziqi Zhang, Weiguo Pan, Bing Li, ying Wang, Hongzhe Liu
- affiliations: not stated
- posted: 2026-05-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6814922
- keyword hits: fine-tuning, large language model

### abstract

Image captioning for Early Childhood Education (ECE) is essential for automated activity understanding and educational assessment. However, existing methods face two key challenges. First, the lack of large-scale, domain-specific datasets limits the model’s ability to capture fine-grained semantic concepts unique to ECE scenarios, resulting in generic and imprecise descriptions. Second, conventional training paradigms exhibit limitations in enhancing professional object description capability, as supervised learning tends to favor high-frequency expressions, while reinforcement learning may suffer from unstable optimization on difficult samples.To address these limitations, we introduce ECAC, a large-scale benchmark for ECE daily activity image captioning, comprising 256,121 real-world images annotated with expert-level captions and fine-grained labels. ECAC is further equipped with a domain-oriented evaluation protocol, the Teaching Toy Recognition Score (TTS), to explicitly measure professional object naming accuracy. Furthermore, we propose RSRS (Reward-Conditional Switch of Reinforcement Learning and Supervised Fine-Tuning), a hybrid training framework that dynamically alternates between RL and supervised optimization. By rerouting hard samples with zero rewards to supervised fine-tuning, RSRS effectively mitigates advantage collapse and enables stable optimization for fine-grained recognition. Leveraging ECAC and RSRS, we develop KinderMM-Cap-3B, a domain-adapted multimodal large language model. Extensive experiments demonstrate that our model achieves a TTS of 51.06, substantially outperforming state-of-the-art baselines while maintaining superior caption quality, highlighting its potential for specialized educational applications. The code and data are available at https://github.com/SixingLI030/KinderMM-Cap.

---

## uid: `doi:10.2139/ssrn.6775598`

- title: Zero-Trust Architecture for Multi-Tenant SaaS Platforms on AWS:A Practitioner Framework for Authentication, Authorisation, and KYC in Regulated Financial Services
- authors: Alan Terriaga
- affiliations: not stated
- posted: 2026-05-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6775598
- keyword hits: agentic

### abstract

Multi-tenant Software-as-a-Service (SaaS) platforms operating in regulated financial services face a unique intersection of security, compliance, and operational challenges that traditional perimeter-based architectures cannot adequately address. This paper presents a practitioner framework for implementing Zero-Trust Architecture (ZTA) across all layers of an AWS-hosted SaaS application deployed on Amazon Web Services (AWS), with particular focus on the authentication, authorisation, and Know Your Customer (KYC) verification pipelines that underpin financial compliance obligations. Drawing on direct delivery experience leading engineering teams responsible for identity and access management (IAM) in regulated multi-tenant environments, we describe concrete implementation patterns across seven architectural layers: edge security, identity and authentication, fine-grained authorisation, service-to-service machine identity, data protection, continuous monitoring, and developer access governance. We identify key failure modes, trade-off decisions, and compliance constraints that shape real-world ZTA deployments-aspects absent from theoretical frameworks but critical to practitioners building production systems. Our framework aligns with the US Cybersecurity and Infrastructure Security Agency (CISA) Zero Trust Maturity Model and Executive Order 14028 requirements, offering a reusable reference architecture validated in a production environment serving multiple regulated financial institution tenants. The platform operates in a regulated sector managing pension and retirement contribution obligations for member organisations and their employees, subject to oversight by national financial regulatory authorities. Individual user identities span concurrent organisational affiliations with distinct role assignments and mandatory KYC verification requirements per organisational context-a cross-tenant identity model that introduces authorisation complexity beyond conventional single-tenant frameworks. This compliance burden is significant at industry scale: financial institutions in the United States and Canada alone spend an estimated $61 billion annually on AML and KYC compliance [10], with global AML system spend projected to reach $51.7 billion by 2028 [11], and average per-firm AML/KYC operational spend now standing at $72.9 million annually [12]. Authorisation rules are expressed as policy-as-code using the Cedar language, enabling fine-grained, auditable, per-request access decisions. We conclude with discussion of emerging challenges introduced by agentic AI workloads and the extension of KYC principles to non-human identities.

---

## uid: `doi:10.2139/ssrn.6811533`

- title: DANTE: A Lightweight Hybrid CNN‐Transformer Network for Efficient Image Classification
- authors: Miguel Sanchez-Brito
- affiliations: not stated
- posted: 2026-05-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6811533
- keyword hits: transformer model

### abstract

Abstract.,Vision Transformers (ViTs) have achieved remarkable accuracy but suffer from high computational and memory costs, typically relying on large‐scale pre‐training. Hybrid CNN‐Transformer models attempt to combine local feature extraction with global attention, yet most suffer from redundant fusion, parameter inefficiency, or dependence on pre‐trained backbones. We propose DANTE_Optimized, a lightweight hybrid architecture designed to be trained from scratch on small‐to‐medium datasets. DANTE introduces: (i) a three‐stage convolutional stem that aggressively downsamples spatial resolution while expanding channels, producing a compact token sequence; (ii) a multi‐head self‐attention module with learnable relative positional bias (DanteAttention) that generalises across input sizes; and (iii) a hierarchy of Transformer blocks with pre‐LayerNorm, gated MLP, and residual connections, using only 7.1 M parameters. Without any pre‐training or external data, DANTE is evaluated on five benchmarks (CIFAR‐10, CIFAR‐100, Tiny ImageNet, STL‐10, SVHN) against ResNet50, EfficientNet‐B0, MobileNetV3, and ConvNeXt‐Tiny under identical training protocols. DANTE achieves the highest top‐1 accuracy on CIFAR‐100 (67.26%, +5.0 pp over ResNet50) and SVHN (96.14%), while using 3‐4× fewer parameters. On CIFAR‐10 it matches ResNet50 (87.68% vs 88.26%) with a 3.3× parameter reduction. Ablation studies confirm that the convolutional stem is critical (removing it drops accuracy by 13 pp) and that depth=6 offers a better efficiency‐accuracy trade‐off. Although DANTE has higher FLOPs than pure CNNs (0.44 G vs 0.08 G on 32×32 inputs), its parameter efficiency makes it ideal for memory‐constrained deployment. Code and benchmark are open‐source and reproducible on Apple Silicon.

---

## uid: `doi:10.2139/ssrn.6775102`

- title: Context Objects: A Temporal, Provenance-Aware Memory Primitive for Enterprise AI Agents
- authors: Madhu Chamarty
- affiliations: not stated
- posted: 2026-05-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6775102
- keyword hits: ai agent

### abstract

We propose the Context Object, a storage primitive designed for enterprise AI agent systems. Unlike logs, documents, vector embeddings, or knowledge graph nodes, a Context Object treats temporal validity, epistemic confidence, provenance lineage, organizational weight, and agent-use feedback as first-class retrieval properties rather than application-layer annotations. We define the formal schema, specify retrieval semantics, and describe the Context Bank: a sovereign, enterprise-owned memory layer built on this primitive. We evaluate the primitive against a four-condition ablation study conducted in a controlled simulation environment (Acme Advisory), calibrated from two real-world datasets: 1,595,911 events from the BPI Challenge 2019 Purchase-to-Pay process logs (van Dongen, 2019) for structured exhaust, and 332,557 emails from the CMU Enron corpus (Klimt and Yang, 2004) for behavioral exhaust. The full primitive stack achieves 80.0% accuracy on correct routing of procurement, staffing, billing, and proposal scenarios against seeded ground truth institutional memory objects, compared to 53.3% for a Global RAG baseline, a 26.7 percentage point advantage attributable to synthesis, confidence tracking, and decay management. The central empirical finding is a Partial Sophistication Trap : the SILOED_ADVANCED condition, which partially implements context retrieval without the complete primitive stack, achieves 26.7% accuracy, 46.6 points worse than SILOED_TYPICAL (73.3%), which makes no retrieval attempt. The failure modes of partial retrieval compound multiplicatively. In our experiments, partial implementations produced sharply degraded performance, suggesting strong interdependence among components of the primitive stack. More broadly, our results suggest that retrieval performance is not monotonic with retrieval sophistication: adding partial context retrieval capability can produce worse outcomes than no retrieval at all.

---

## uid: `doi:10.2139/ssrn.6797302`

- title: 3D Point Cloud Deep Learning for Mammalian Bone Classification in Natural History Collections
- authors: Zakaria Doubabi, Youcef Sklab, Hanane Ariouat, Pauline Provini, Eric Chenin, Jean-Daniel Zucker, Christophe Denis, Jihad Zahir
- affiliations: not stated
- posted: 2026-05-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6797302
- keyword hits: fine-tuning

### abstract

3D point clouds capture rich geometric information, but remain largely unexplored in biodiversity research due to their irregular structure and the high morphological variability of biological specimens. This study reports the first large-scale application of state-of-the-art 3D point cloud deep learning architectures to digitized natural history collections for mammalian bone classification. A dataset of 5,318 digitized bones spanning diverse mammalian taxa and fourteen anatomical categories was assembled, introducing substantial intra-class variability. Thirteen point cloud architectures were evaluated, including traditional supervised models and self-supervised learning (SSL) architectures. Supervised models were trained exclusively under supervision, while SSL architectures were assessed both when trained from scratch and when using self-supervised pre-training followed by supervised fine-tuning. Classification performance varied markedly across architectures, with overall accuracies ranging from approximately 54.8% to 97.6% and macro F1-scores from 50.7% to nearly 96.6%. Several architectures achieved near-optimal performance without pre-training, whereas others benefited substantially from self-supervised learning, while some exhibited limited or negative transfer. These results demonstrate that architectural design, rather than training strategy alone, is the primary determinant of performance in 3D mammalian bone classification. The study highlights both the potential and the limitations of applying point cloud deep learning methods to complex biological morphology.

---

## uid: `doi:10.2139/ssrn.6809940`

- title: Reflexively Stabilized Adaptive Cognitive Runtime Systems: Toward Continuity-Constrained Human-Governed Agentic Intelligence
- authors: Varun Gupta
- affiliations: not stated
- posted: 2026-05-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6809940
- keyword hits: agentic

### abstract

Contemporary artificial intelligence systems increasingly demonstrate advanced generative and adaptive reasoning capability but remain vulnerable to instability during prolonged runtime execution. Emerging challenges include recursive escalation, hallucination amplification, governance inconsistency, excessive cognitive activation, context contamination, and degradation of operational coherence across extended adaptive interaction. Current research predominantly optimizes either capability expansion or alignment enforcement, while comparatively limited attention has been directed toward continuity preservation, bounded cognition, and long-term operational survivability under sustained runtime conditions. This paper proposes a conceptual architecture for adaptive cognitive runtime systems centered on reflexive stabilization, selective cognitive activation, continuity-constrained reasoning, governance-adaptive execution, and bounded human-governed autonomy. Rather than conceptualizing intelligence as permanently maximized cognition, the proposed framework treats adaptive reasoning as a selectively activated process operating under persistent continuity-preserving constraints inspired by stabilization principles observed in biological and cybernetic systems. The framework advances a stability-centered runtime philosophy emphasizing pre-escalation stabilization, operational admissibility, adaptive governance regulation, transition integrity, and sustainable cognitive economy. The proposed direction prioritizes boundedness, runtime coherence, and operational survivability over unrestricted autonomous expansion. This paper presents the conceptual foundations, architectural motivations, research positioning, and future directions for continuity-centered adaptive cognitive runtime systems while preserving abstraction around implementation-specific orchestration mechanisms.

---
