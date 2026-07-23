# Classification batch 385 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-385.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6811568`

- title: Learning-Driven Autonomy in Traffic Flow: A multi-modal perception, forecasting and planning
- authors: Lakshman Mahto
- affiliations: not stated
- posted: 2026-05-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6811568
- keyword hits: text embedding

### abstract

Urban traffic management increasingly requires closed-loop autonomy rather than isolatedestimation, forecasting, or local signal timing. This article develops a learning-drivenautonomy framework for traffic flow management in which traffic evolves through a recurrentbelief–forecast–control loop. The framework integrates: (i) a multimodal belief space thatfuses traffic, infrastructure, temporal, and contextual signals into compact latent statesummaries; (ii) a structured control context encoding current actions, inertia, feasibility, anddwell-time persistence; (iii) an action-aware conditional variational autoencoder (CVAE)that predicts future traffic states under uncertainty; and (iv) a chance-constrained modelpredictive control (MPC) layer that manages congestion risk, queue spillback, and operationalfeasibility. In the present implementation, the multimodal conditioning is instantiated as a104-dimensional vector composed of a 64D context embedding, a 32D control embedding, andan 8D plan embedding. The empirical pipeline compares 10 forecasting variants, performsmulti-seed statistical evaluation, calibrates predictive uncertainty, and studies closed-loopcontrol behavior using the benchmark traffic workflow. The resulting formulation positionstraffic flow management as a problem of learning-driven autonomy under uncertainty ratherthan deterministic traffic prediction alone.

---

## uid: `doi:10.2139/ssrn.6811369`

- title: When a Safe Prompt Produces an Unsafe Feeling: The Context-Ambiguity Gap in Child-Facing Generative AI Storytelling
- authors: Wenlin Han
- affiliations: not stated
- posted: 2026-05-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6811369
- keyword hits: generative ai, prompting

### abstract

Child-facing generative AI systems are increasingly used in libraries, schools, and family learning settings, yet safety practices often focus on prohibited prompts, explicit content, and privacy while giving less attention to how young children interpret emotionally ambiguous outputs. This design case analyzes a public library AI literacy activity in which a benign story prompt involving familiar children's characters led to an AI-generated image that a child reportedly interpreted as a character being dead. The case is examined through local event documents, a parent follow-up draft, an incident email, the activity handout, the volunteer guide, and screenshots embedded in the feedback record. The analysis identifies a context-ambiguity gap: an output can be semantically related to a safe prompt while lacking the emotional cues that help a child understand the scene as playful, temporary, or harmless. Drawing on early-childhood technology guidance, child-centered AI policy, AI literacy frameworks, and research on children's context-sensitive interpretation of pictures, the paper proposes Developmental Interpretation Safety as a design requirement for child-facing AI storytelling. The resulting protocol combines constrained prompting, adult preview, visual ambiguity checks, positive-ending defaults, and facilitator repair language.

---

## uid: `doi:10.2139/ssrn.6777058`

- title: Context Objects: A Temporal, Provenance-aware Memory Primitive for Enterprise AI Agents
- authors: Madhu Chamarty
- affiliations: not stated
- posted: 2026-05-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6777058
- keyword hits: ai agent

### abstract

We propose the Context Object , a storage primitive designed for enterprise AI agent systems. Unlike logs, documents, vector embeddings, or knowledge graph nodes, a Context Object treats temporal validity, epistemic confidence, provenance lineage, organizational weight, and agent-use feedback as first-class retrieval properties rather than application-layer annotations. We define the formal schema, specify retrieval semantics, and describe the Context Bank : a sovereign, enterprise-owned memory layer built on this primitive. We evaluate the primitive against a four-condition ablation study conducted in a controlled simulation environment (Acme Advisory), calibrated from two real-world datasets: 1,595,911 events from the BPI Challenge 2019 Purchase-to-Pay process logs (van Dongen, 2019) for structured exhaust, and 332,557 emails from the CMU Enron corpus (Klimt and Yang, 2004) for behavioral exhaust. The full primitive stack achieves 80.0% accuracy on correct routing of procurement, staffing, billing, and proposal scenarios against seeded ground truth institutional memory objects, compared to 53.3% for a Global RAG baseline, a 26.7 percentage point advantage attributable to synthesis, confidence tracking, and decay management. The central empirical finding is a Partial Sophistication Trap : the SILOED_ADVANCED condition, which partially implements context retrieval without the complete primitive stack, achieves 26.7% accuracy, 46.6 points worse than SILOED_TYPICAL (73.3%), which makes no retrieval attempt. The failure modes of partial retrieval compound multiplicatively. In our experiments, partial implementations produced sharply degraded performance, suggesting strong interdependence among components of the primitive stack. More broadly, our results suggest that retrieval performance is not monotonic with retrieval sophistication: adding partial context retrieval capability can produce worse outcomes than no retrieval at all.

---

## uid: `doi:10.2139/ssrn.6816398`

- title: AI Augmented Shipping Automation in ERP Systems:,Architecture, Algorithms, and Production Evaluation
- authors: Manish Kumar
- affiliations: not stated
- posted: 2026-05-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6816398
- keyword hits: llm, retrieval-augmented

### abstract

Shipping label generation sits at the operational heart of order fulfilment in warehouse environments, yet in many Oracle ERP deployments it still depends on warehouse staff manually re-entering shipment data into carrier portals—a practice that is slow, error-prone, and increasingly incompatible with the throughput demands of modern e-commerce. This paper describes ShipSync-AI, an architecture we developed and deployed in a production Oracle E-Business Suite environment to eliminate that manual step and, beyond it, to embed genuine intelligence into the shipping decision process. The system has two layers. The first is a seven-component integration pipeline that automates end-to-end label generation through direct carrier API communication, with formal treatment of idempotent reprint handling, hierarchical printer resolution, return label support, and exponential-backoff error recovery. The second is an AI Intelligence Layer comprising six modules—a fine-tuned BERT address validator, an LSTM + gradient-boosted ETA predictor, a Deep Q-Network carrier selection agent, an Isolation Forest anomaly detector, a retrieval-augmented LLM exception handler, and a Temporal Fusion Transformer demand forecaster—each formally specified and individually benchmarked. The complete system was evaluated across 187,432 production shipments over 90 days. Manual processing effort fell by 82%, label accuracy reached 99.7%, throughput increased from 45 to 380 labels per hour, and P99 end-to-end latency measured 2.8 seconds. We also document the practical engineering challenges—ZPL resolution mismatches, API versioning transitions, concurrent staging table contention—that sit between a well-specified architecture and a working production deployment.

---

## uid: `doi:10.2139/ssrn.6816152`

- title: How Patient Capital Supports AI-Native Entrepreneurship: An Empirical Study of OPC Incubation by China’s Government Guidance Funds
- authors: Yifan Zhang, shuai ye
- affiliations: not stated
- posted: 2026-05-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6816152
- keyword hits: ai agent

### abstract

Driven by AI Agent technology, China’s OPC (One-Person Company) entrepreneurship model has undergone disruptive transformation and emerged as the mainstream form in the local innovation ecosystem. However, it presents a significant structural mismatch with traditional capital support systems and incubation governance models. This typical Chinese industrial phenomenon highlights the urgent need for government guidance fund–based patient capital to adapt to AI-native entrepreneurship. Grounded in China’s institutional characteristics and the realities of AI entrepreneurship, this study adopts actor-network theory and defines OPC for the first time as a hybrid actor composed of natural persons and AI agents, breaking away from traditional governance frameworks centered on legal or natural persons. Taking AI Agent development platforms such as Open Claw as research entry points, the paper reveals their dual role in productivity empowerment and institutional embedding in OPC incubation, and constructs a four-dimensional nested institutional model covering intelligent project screening, OPC–AI empowerment, China–US computing power sharing, and legal protection. Based on survey data from 327 AI-native OPC projects in Jiangsu Province, a logistic regression model embedded with legal boundaries is developed to quantify compliance requirements and identify high-quality projects precisely. Using Suzhou Industrial Park as an empirical case, the study verifies the practical feasibility and governance effectiveness of the four-dimensional model. This research extends the connotation of patient capital from the temporal dimension to technological and governance dimensions, innovates the human–machine coupling analytical unit and the nested innovation governance framework. It not only provides a systematic institutional design for China’s government guidance funds to build professional OPC incubation platforms, but also offers a valuable local paradigm for global innovation governance in the digital era.

---

## uid: `doi:10.2139/ssrn.6819075`

- title: Focusing on Object Relations in Scenes: A Multi-collaborative Graph-structured Framework for Infrared and Visible Image Fusion
- authors: Jiawei Li, Hongwei Yu, Xinlong Ding, Enlong Wang, Qiankun Liu, Jinyuan Liu, Huimin Ma, Jiansheng Chen
- affiliations: not stated
- posted: 2026-05-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6819075
- keyword hits: fine-tuning

### abstract

Infrared and visible image fusion (IVIF) technology can overcome the limitations of single-modality imaging by integrating the complementary information from different source images into a fused image. Existing methods are capable not only of extracting image features from inputs, but also of leveraging descriptions to enrich the representation of fusion results in the text domain. However, they focus solely on texture details or specific targets, while neglecting the relative spatial relationships and scene understanding capacity of images. To address this issue, we propose a novel graph-structured framework with text–image–relation collaborative representation, referred as GraTIR. Specifically, we employ a pre-trained scene graph generation (SGG) module to extract scene-aligned attention maps and triplet descriptions. Then, they are fed into a relation-to-graph (R2G) module to construct relation graph features, which help the fusion network learn the relative positional relationships among objects. Global Adaptive Decoder (GAD) decodes visual and semantic features in a hierarchical manner, aiming to enhance the effective representation of different feature types. In addition, the SGG module also serves as the fine-tuning model under the scene graph loss supervision. We conduct fusion and down-stream (i:e:, detection and segmentation) experiments on the M3FD and MSRS datasets. To evaluate the scene understanding ability of fusion images, we establish the IVIF-SG dataset and, for the first time, introduce SGG as a down-stream task of IVIF. Extensive experiments confirm that our GraTIR achieves outstanding fusion quality while improving performance on down-stream tasks.

---

## uid: `doi:10.2139/ssrn.6819943`

- title: Predicting Public Building Energy Consumption in the Early Design Stage Using a Multi-Agent LLM for Occupant Behavior Simulation
- authors: Rui Dai, guoqiang zhang, Linhu Wang, Liuchang yang, Ge Bai
- affiliations: not stated
- posted: 2026-05-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6819943
- keyword hits: ai agent, llm

### abstract

Accurate building energy prediction at the early design stage is essential for low-carbon design decisions, but its reliability is often limited by incomplete design information and simplified assumptions about occupant behavior. This study proposes a design-stage energy prediction framework for hospital outpatient buildings that integrates BIM-based layout information, scenario-based environmental variables, AI agent-generated occupant behavior data, and data-driven prediction models. Three outpatient campuses in Wuhan, China, were used as case studies. A multi-agent simulation process was developed to generate occupant behavior logs under outpatient service scenarios, from which temporal, spatial, service-process, interaction, and energy-related behavior variables were extracted. Four benchmark models selected from representative recent building energy prediction studies, namely multiple linear regression, TLBO-ANN, Transformer, and temporal fusion transformer, were then compared under a unified evaluation setting. The results show that the temporal fusion transformer achieved the best overall performance, with an MSE of 69,400, an MAE of 181, a MAAPE of 0.052, and an R^2 of 0.933. Incorporating AI agent-generated behavior variables improved all benchmark models, reducing MSE by 19.1--19.8% and increasing R^2 by 1.97--3.53%. Ablation and sensitivity analyses further indicate that temporal occupancy features, HVAC usage duration, zone-level occupancy, and service-process variables are key drivers of prediction performance. The proposed framework provides a practical way to incorporate simulated occupant behavior into early-stage energy prediction and offers decision support for low-carbon hospital outpatient building design.

---

## uid: `doi:10.2139/ssrn.6788658`

- title: A Bitter Lesson for Retail Demand Forecasting: Evidence from Fine-Tuning Foundation Models
- authors: Yi Sui, Chenjie Xiao, Linwei Xin, Donghai Huang, Lei Cao
- affiliations: not stated
- posted: 2026-05-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6788658
- keyword hits: fine-tuning, foundation model

### abstract

Recent advances have driven growing interest in using pretrained foundation models for time-series forecasting, marking a shift from task-specific forecasting models toward general-purpose forecasting systems. Although a growing body of literature highlights their promise across benchmark settings, the practical value of time-series foundation models (TSFMs), including Amazon's widely adopted Chronos-2, remains debated. In particular, there is limited independent evidence on how well TSFMs perform in real-world industrial settings beyond controlled benchmark evaluations. This paper provides the first systematic and independent empirical evaluation of Chronos-2, together with two other TSFMs, using large-scale retail data from Alibaba. Our results reveal a striking finding: despite the strong performance of Alibaba’s existing deep learning-based production forecasting system, Chronos-2 substantially outperforms this baseline, improving forecasting performance by 3.5% for domestic products and 5.4% for international products. Moreover, these improvements are highly consistent across temporal dimensions and product segments, as well as in both zero-shot and fine-tuned settings. Our results point to a potentially disruptive paradigm shift in demand forecasting, echoing Sutton's "bitter lesson'': in the long run, the largest improvements may come less from increasingly sophisticated handcrafted forecasting systems and more from scalable pretrained foundation models. Beyond forecasting accuracy, our findings also suggest that TSFMs can serve as simulators for operations, generating synthetic demand trajectories to support downstream tasks such as inventory optimization and pricing. This opens an exciting new research frontier on how to utilize TSFM-generated synthetic data to improve downstream decision-making.

---
