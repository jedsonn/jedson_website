# Classification batch 121 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-121.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6817719`

- title: Mini-JEPA Foundation Model Fleet Enables Agentic Hydrologic Intelligence
- authors: Mashrekur Rahman
- affiliations: not stated
- posted: 2026-05-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6817719
- keyword hits: agentic, claude, foundation model, llm

### abstract

Geospatial foundation models leverage multispectral observations into dense embeddings that are increasingly applied in natural-language environmental reasoning systems. A single planetary-scale model, e.g. Google AlphaEarth, handles broad characterization well but may compromise on specialized hydrologic signals. Such generalist models are also often inaccessible, expensive, and require large-scale compute. We propose a fleet of small sensor-specialized Joint Embedding Predictive Architecture (JEPA) foundation models that can be consulted by a routing agent for specialized questions. We pretrained five (22M parameter) Mini-JEPAs that share an identical Vision Transformer backbone, an identical JEPA training recipe, and a 64-dimensional output space, using images from Sentinel-2 optical, Sentinel-1 SAR, MODIS thermal, multi-temporal Sentinel-2 phenology, and a topography and soil stack. Each Mini-JEPA reconstructs the environmental variable matched to its sensor, with cross-validated R² reaching 0.97 for elevation under the topography-soil model, 0.97 for mean temperature under the thermal model, and 0.81 for precipitation under the phenology model. Across all five models, the variable each one predicts best is the variable its sensor physically observes. The five manifolds differ in geometric structure, with global participation ratios ranging from 8.9 for the SAR model to 20.2 for the thermal model, and local intrinsic dimensionalities from 2.3 to 9.0. By contrast, the joint topography-soil and phenology models add predictive value beyond AlphaEarth Foundation Model alone for soil moisture, aridity, and precipitation (ΔR² up to 0.031). A router LLM (Claude Sonnet/Opus) reads per-modality references and selects the appropriate sensors with a perfect expected-modality hit rate over a curated question set. In paired LLM-as-Judge evaluation, dual retrieval over AlphaEarth and the routed fleet outperforms AlphaEarth alone on questions whose signal matches a single sensor (Cohen's d = 1.10, p = 0.031). Aggregate gains across all question types remain modest. On the physics-matched questions, the routed fleet alone also scores comparably to AlphaEarth. Our findings suggest that locally-trained specialized Mini-JEPAs can be operationalized for hydrologic intelligence systems with modest compute, providing a complement or substitute to planetary-scale foundation models.

---

## uid: `doi:10.2139/ssrn.6833492`

- title: Sherlock Holmes vs LLMs: May LMs Deceive Brilliant Minds?
- authors: Paolo Tripicchio
- affiliations: not stated
- posted: 2026-05-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6833492
- keyword hits: llm, llms, retrieval-augmented

### abstract

This article examines the reasoning capacities of contemporary AI systems through the conceptual lens of Sherlock Holmes's investigative method. Rather than treating ``reasoning'' as a broad label for improved performance, the paper distinguishes among observation, abductive hypothesis generation, deductive testing, memory organization, and verification against external constraints. On this basis, it compares Holmesian reasoning with the mechanisms that underlie current AI systems, including attention and cross-attention, Mixture of Experts (MoE), Reinforcement Learning with Verifiable Rewards (RLVR), retrieval-augmented memory, graph-based retrieval, vector-space search, and latent world-modeling approaches such as JEPA. The analysis argues that these developments increasingly approximate important components of structured reasoning, but still fall short of the flexible, reality-grounded abductive competence associated with human inquiry. This gap becomes especially visible in logic-puzzle benchmarks, where fluent reasoning traces often coexist with failures in compositional consistency and constraint management. The paper concludes that progress toward more general intelligence will depend not only on scaling pattern recognition, but also on integrating memory, perception, inference, and verification into more unified cognitive architectures.

---

## uid: `doi:10.2139/ssrn.6748465`

- title: Epistemological Sequencing as an Architectural Principle: Structural Output Properties of Multi-regime Inference over Large Language Models
- authors: Marcelo Manucci
- affiliations: not stated
- posted: 2026-05-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6748465
- keyword hits: large language model, large language models, prompt engineering

### abstract

Background. The dominant design pattern in applied large language model systems involves a single inferential regime: one prompt, one model, one analytical pass. This structural uniformity produces a convergence across systems, models, and analytical outputs that we term epistemic monoculture — a pattern that is not primarily a limitation of model capability but an architectural consequence of single-regime processing. Objectives. To test whether epistemological sequencing — the controlled succession of distinct inferential regimes over the same analytical object — produces structural output properties not replicable by professional single-prompt engineering under controlled conditions (same generative model, same analytical case). Methods. Six analytical frameworks instantiating epistemologically distinct regimes — spanning systems complexity theory, systemic constructivism, inductive empiricism, competitive morphogenesis, cognitive neuroscience, and third-order cybernetics — were each executed under sequenced (experimental) and single-prompt (control) conditions over the same organizational case. Output structure was measured across four metrics: variable diversity (M1), relational density (M2), configurational differentiation (M3), and inferential traceability (M4). A pre-specified success criterion required ≥3/4 metrics in ≥5/6 frameworks. Three independent blind assessors evaluated anonymized output pairs. Results. The pre-specified success criterion was met in all six frameworks (≥3/4 metrics in 6/6): four frameworks achieved full 4/4 superiority, and two achieved 3/4 with a tie on M1. Relational density (M2) and inferential traceability (M4) were favorable to the sequenced condition in all six frameworks without exception — structural properties that depend on regime transitions rather than on the prescriptive content of any individual prompt. Blind assessment confirmed the structural advantage in five of six frameworks, with a majority in two and unanimity in one. One framework (NM), in which the single-prompt control was exceptionally strong, produced no majority verdict in the blind assessment and is documented and analyzed as an informative exception. Conclusions. Epistemological sequencing produces architectural output properties — particularly relational density and inferential traceability — that were not observed in the DOI 10.5281/zenodo.20121190 | 2 strong single-prompt controls used in this study and are theoretically attributable to regime transitions. The consistency across six epistemologically heterogeneous regimes supports an architecture-level interpretation of the effect. Whether the principle generalizes to structurally distinct domains — that is, whether it is domain-agnostic — requires independent instantiation and remains an open research question. Verification requires instantiation outside the strategic analysis domain studied here. The complete measurement protocol, blind evaluation rubric, control prompt generation procedure with structural summaries, scoring tables, and an anonymized execution environment instantiating the six frameworks are openly deposited and operationally accessible. Current limitations — a single organizational case, a single domain, and a study design that does not fully isolate operator-level reproducibility from model-level variation — define the scope of the present evidence and the next stage of the research program.

---

## uid: `doi:10.2139/ssrn.6843587`

- title: Acoustic Recognition of Tilapia Feeding Intensity via LoRA-Fine-Tuned Multimodal Large Language Models
- authors: Chen Yang, Shengli Fan, Peizheng He, Xinli Ma, Lang Wang, Michel Dossou, Weiming Cai
- affiliations: not stated
- posted: 2026-05-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6843587
- keyword hits: fine-tuning, large language model, large language models, qwen

### abstract

Real-time assessment of fish feeding intensity is essential for demand-based feeding in intensive aquaculture, yet existing methods rely on external spectrogram preprocessing and large annotated datasets, limiting practical deployment. This study proposes an end-to-end approach that reformulates feeding intensity recognition as an audio instruction-following task using the multimodal large language model Qwen2.5-Omni-3B. Raw audio clips and natural language prompts are taken as direct inputs, and low-rank adaptation (LoRA) is applied for parameter-efficient fine-tuning under data-scarce conditions. Experiments on 4,186 tilapia audio recordings show that the method achieves 98.21% accuracy with 200 training samples on the same test set used by a CNN baseline, and 96.96% on an independent test set of 2,000 samples. Ablation studies indicate that applying LoRA across all linear layers with rank 32 and scaling factor 256 yields a favorable performance–efficiency trade-off. The results demonstrate that coupling pre-trained multimodal models with parameter-efficient fine-tuning can effectively reduce dependence on annotated data in underwater acoustic recognition tasks, offering a scalable solution for intelligent feeding systems in aquaculture.

---

## uid: `doi:10.2139/ssrn.6828838`

- title: Prompt Injection Attacks Against Clinical LLM Agents Accessing Electronic Health Records: A Survey, Threat Model, Benchmark Specification, and Layered Defense Synthesis
- authors: Divya Pandey, Shivani Manchanda, Gangesh Pathak, Nishant Sonkar
- affiliations: not stated
- posted: 2026-05-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6828838
- keyword hits: agentic, large language model, llm, llms

### abstract

Clinical large language model (LLM) agents are entering production hospital deployments, where they read longitudinal electronic health records (EHRs), retrieve evidence from clinical knowledge bases, and assist with summarization, dosing, triage, and guideline-based decisions. The same architectural patterns that make these agents useful-instruction-following on retrieved text, tool use over patient data, and multi-turn conversation-also expose them to prompt injection attacks across heterogeneous input channels. This paper makes four contributions: (i) a structured survey of prompt injection in medical LLMs, including the MPIB benchmark, the JAMA Network Open simulation study, oncology vision-language attacks, and the broader prompt-injection literature; (ii) a threat model for EHR-accessing agents organized around five injection channels, four attacker objectives, and three cross-tenant risks, with explicit mapping to defense layers; (iii) EHR-Agent-PI, a benchmark specification extending MPIB and BIPIA along agentic, cross-channel, and outcome-aware dimensions, with specified scenarios, attack rules, disambiguated evaluation metrics (ASR, CHER, PER, TMR, FPR-H), per-cell instance counts, a reference judge prompt, a synthetic-data schema, a documented cost model, and a responsible-release plan compatible with HIPAA and GDPR constraints; and (iv) a layered six-layer defense architecture for clinical deployments, with explicit layerinteraction analysis. Empirical instantiation of EHR-Agent-PI is described as planned future work, with a small-scale pilot outlined in Section 8.5.

---

## uid: `doi:10.2139/ssrn.6844333`

- title: A Multimodal Explainable AI System for Early Prediction of 30-Day Diabetes Readmission with LLM-Generated Clinical Recommendations
- authors: Aiman Sadiev, Remudin Mekuria
- affiliations: not stated
- posted: 2026-05-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6844333
- keyword hits: large language model, llm, text embedding

### abstract

Predicting 30-day hospital readmission in diabetic patients is a key challenge in modern healthcare: readmissions within this window signal poor glycaemic management during the index admission and contribute substantially to avoidable costs. Existing machine-learning approaches rely on structured tabular data and often stop short of translating their predictions into actionable guidance for clinicians. We propose a multimodal explainable AI system that addresses both limitations. Using the Diabetes 130-US Hospitals dataset (n = 101,766), we augment structured electronic health record (EHR) features with a text modality: feature-conditioned synthetic clinical notes generated by a large language model (LLM) and encoded by Bio+ClinicalBERT into 768-dimensional dense vectors. We compare six models: Logistic Regression, Random Forest, XGBoost, a Tabular-Only Neural Network (Tab-NN), an Early Fusion Neural Network (EF-NN), and a Late Fusion Neural Network (LF-NN). A controlled ablation study isolates the contribution of the text modality by comparing EF-NN and Tab-NN, which share identical architecture and training. Our LF-NN achieves AUC-ROC of 0.9067 (95% CI: 0.8827–0.9287), and EF-NN surpasses the architecturally equivalent Tab-NN by +0.2513 AUC-ROC points, confirming that synthetic text embeddings carry complementary predictive signal beyond structured features. Model predictions are explained via SHAP, and a structured LLM-driven recommendation layer translates per-patient feature attributions into natural-language clinical guidance. SHAP analysis identifies prior inpatient admissions, polypharmacy, and glycaemic indicators as the dominant readmission drivers, consistent with established clinical knowledge. Bootstrap confidence intervals confirm that both multimodal models are statistically distinguishable from tabular-only baselines by non-overlapping CIs. Key limitations include the use of risk-label-conditioned synthetic notes, which may carry indirect target-correlated signal, and the small multimodal test subset. Our system demonstrates that combining structured and unstructured data modalities with interpretable AI and natural-language recommendations meaningfully advances both predictive performance and clinical utility.

---

## uid: `doi:10.2139/ssrn.6853414`

- title: Large Language Model Agents in the Building Energy Sector: All You Need to Know About Applications, Infrastructure, Limitation, and Best Practice
- authors: Huiwen Zhou, Liang Zhang, Sunil Khadka, Xiaoqin Fu, Han Li, Tianzhen Hong
- affiliations: not stated
- posted: 2026-06-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6853414
- keyword hits: agentic, foundation model, large language model, llm

### abstract

The paper focuses on the emerging applications of Large Language Model (LLM) agents in the building energy sector. While LLM agents have gained traction in other fields, their use in building energy research and engineering remains limited. We examine studies from both building and non-building domains to bridge the current literature gap and identify transferable methodologies from more mature AI application areas that can be adapted to the specific constraints of the built environment. We compare core concepts such as autonomous agents and agentic workflows, and summarize commonly used tools and infrastructure. Despite growing interest, significant challenges persist—including the absence of standardized validation methods, and persistent issues related to safety, bias, and hallucination. Based on our synthesis, we identify emerging opportunities—such as building-specific benchmarks, and human-in-the-loop workflows—that offer promising pathways to address these limitations. We summarize the limitations of LLM foundation models and agentic systems, define the scope of suitable applications of LLM agents in the building energy sector, and provide a checklist as practical guidance for agent design. By distilling the state-of-the-art and outlining future directions, this paper provides insights and informs the development of trustworthy and efficient LLM-based agents capable of performing diverse tasks that vary in function and complexity across real-world applications.

---

## uid: `doi:10.2139/ssrn.6865776`

- title: BearAgent: Multi-Agent Diagnosis Optimization and Uncertainty-aware Decision-Making for Bearing Health Management
- authors: Cheng Zhang, Zheyuan Lu, Dingxiao Liu, Shenyuan Ren, Yakun Li, Dongmei Li, Juanzi Li, Jie Tang
- affiliations: not stated
- posted: 2026-06-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6865776
- keyword hits: fine-tuning, llm, llms

### abstract

Reliable bearing health management is essential for industrial safety and economic efficiency. Fault diagnosis and maintenance decision-making are core tasks, yet progress is constrained by two challenges: (1) real-world fault data are severely imbalanced, and (2) LLMs-based decision systems typically treat the predicted label as ground truth, ignoring diagnostic uncertainty. To address these limitations, we propose BearAgent, a multi-agent framework that integrates diagnosis optimization with uncertainty-aware maintenance decision-making. On the diagnosis side, BearAgent employs a multi-agent diagnosis optimization module to monitor class-wise performance, schedule minority-class conditional generation, and admit only high-quality synthetic vibration signals through a two-stage screening mechanism, thereby improving minority fault recognition and exposing a calibrated probabilistic diagnosis interface. On the decision side, BearAgent first learns a policy model from labeled diagnosis--action pairs derived from real diagnostic results, then constructs an uncertainty-aware maintenance decision corpus for supervised fine-tuning, and finally employs a lightweight LLM to generate interpretable, action-consistent maintenance recommendations conditioned on diagnostic uncertainty features. Experiments under multiple class-imbalance settings show that BearAgent consistently improves diagnostic performance, enables robust action selection under unseen uncertainty patterns, and produces interpretable action-consistent maintenance recommendations.

---
