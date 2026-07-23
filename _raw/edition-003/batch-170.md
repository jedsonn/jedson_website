# Classification batch 170 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-170.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6989320`

- title: A Human-Centered Framework for Urban Park Quality Assessment: Integrating Sentinel-2 Remote Sensing, Large Language Model Perception Mining, and Ensemble Deep Learning
- authors: Jing Fan, Longdi Xian
- affiliations: not stated
- posted: 2026-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6989320
- keyword hits: deepseek, large language model, llm

### abstract

Urban parks are key components of urban green infrastructure, providing ecological, recreational, and social benefits. However, comprehensive park quality assessment still rarely integrates objective environmental conditions with human perceptual factors systematically. To address this gap, this research proposes an artificial intelligence (AI)-driven multisource data fusion framework to evaluate urban park quality in Xi’an, a rapidly urbanizing city in China. A total of 101 parks with complete spatial boundary, remote sensing, and user review data were selected for analysis. Spatial boundaries were extracted from OpenStreetMap, while Sentinel-2 Level-2A multispectral imagery was used to derive five environmental indicators: the Normalized Difference Vegetation Index (NDVI), the Normalized Difference Water Index (NDWI), the Normalized Difference Built-up Index (NDBI), the Normalized Difference Moisture Index (NDMI), and approximate Land Surface Temperature (LST; a proxy derived from NDVI). In addition, 103,263 user ratings and 4,548 textual reviews were collected from Dianping. The DeepSeek large language model (LLM) was employed to extract five perceptual dimensions from the reviews: thermal comfort, vegetation quality, water presence, recreational facilities, and vegetation vitality. Deep learning models—including a Convolutional Neural Network (CNN), Residual Network (ResNet), Long Short-Term Memory (LSTM), Bidirectional LSTM (BiLSTM), Mixture-of-Experts (MoE), Liquid Neural Network (LiquidNN), and Vision Transformer (ViT)—were trained on environmental index images. ResNet achieved the highest F1-scores for NDVI (0.75), NDWI (0.73), and LST proxy (0.71), while CNN performed best on NDBI and NDMI (F1 = 0.74). Ensemble fusion improved performance further, with weighted and mean ensembles reaching 0.81 and 0.80, respectively. For perception prediction, MoE achieved F1 = 0.96 for thermal comfort and 0.84–0.85 for water presence and vegetation vitality. These findings demonstrate a robust and human-centered framework for park quality assessment and planning.

---

## uid: `doi:10.2139/ssrn.6990087`

- title: Fat-Cat: Document-Driven Metacognitive Multi-Agent System for Complex Reasoning
- authors: Tong Yang, Aming Wu, Yemin Wang, Jingzhe Kang, Yanan Li, Jianji Ren, Yun Xin, Yongliang Yuan
- affiliations: not stated
- posted: 2026-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6990087
- keyword hits: large language model, llm

### abstract

The efficacy of Large Language Model (LLM) agents is often constrained by the inefficiency of context utilization during runtime. Traditional ”log-centric” frameworks rely on syntax-heavy state representations like nested JSON, which impose a syntactic tax that diverts finite attention from semantic reasoning to structural parsing, leading to context dilution in long-horizon tasks. We propose Fat-Cat, a document-driven metacognitive architecture that transitions agent state management from passive logging to active semantic orchestration. Fat-Cat introduces two synergistic mechanisms: (1) Document-Driven State Modeling. By utilizing a markdown-based global workspace aligned with pre-training priors, we achieve representational alignment that collapses context growth from a quadratic 𝑂(𝑇 2) trajectory into a linear 𝑂(𝑇 ) one. (2) Closed-Loop Semantic Watcher. An independent auditor performs pre-commit verification to detect invalid state transitions and prevent error cascades. Additionally, a textual strategy evolution module facilitates parameter-free learning through methodological distillation. Extensive benchmarking suggests that document-driven state orchestration improves the reliability and context efficiency of LLM agents across multiple backbone models, especially in long-horizon reasoning and domain-grounded verification tasks.

---

## uid: `doi:10.2139/ssrn.6967839`

- title: Bridging the Gap Between AI Adoption and Policy Readiness in Regulated Industries
- authors: Elizabeth Harrison
- affiliations: not stated
- posted: 2026-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6967839
- keyword hits: generative ai, generative artificial intelligence

### abstract

The rapid proliferation of generative artificial intelligence (AI) within regulated industriessuch as finance, healthcare, and legal services-has introduced a critical governance paradox: while organizations aggressively pursue digital transformation to gain competitive advantage, their internal policy frameworks and compliance infrastructures remain significantly underdeveloped. This research investigates the widening chasm between AI adoption rates and organizational policy readiness, a gap exacerbated by the "shadow AI" phenomenon, wherein over half of employees utilize generative AI tools without formal employer sanction or oversight. Drawing upon a mixed-methods approach that combines regulatory analysis, industry case studies, and compliance audits, this study examines the operational vulnerabilities created by ad-hoc AI integration, including data privacy breaches, algorithmic bias, and the circumvention of established regulatory mandates. It critically evaluates the inadequacy of existing governance models-such as voluntary ethical charters and fragmented sectoral guidelines-in addressing the systemic risks of AI deployed within high-stakes environments. Furthermore, the research proposes a dynamic, tiered policy readiness framework designed to be both agile enough to accommodate technological evolution and robust enough to satisfy the stringent requirements of sectoral regulators. By bridging the theoretical discourse on AI ethics with the practical realities of compliance execution, this study offers a strategic roadmap for regulated entities seeking to align innovation imperatives with fiduciary duties, thereby transforming AI governance from a reactive compliance burden into a proactive enabler of sustainable digital transformation.

---

## uid: `doi:10.2139/ssrn.6925818`

- title: Cost and Information Asymmetries in the AI Era: Implications for Commercial and Government Sovereignty
- authors: Mauricio Aristizabal
- affiliations: not stated
- posted: 2026-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6925818
- keyword hits: large language model, large language models

### abstract

The widespread adoption of large language models has enabled a new class of AI platforms and created structural cost and information asymmetries in digital service access. AI platforms can interpret intent expressed in natural language at low cognitive cost, but lack the ability to execute transactions or provide authoritative service delivery. Service providers, including commercial firms and government agencies, possess execution authority but impose significantly higher costs on users who must translate intent into service-specific graphical user interfaces (GUI). We formalize these cost and information asymmetries and characterize an intermediation equilibrium in which users route intent based on net utility, with AI platforms capturing intent flows through advantages in both cost and perceived value despite their inability to execute transactions. This routing creates a consequent information asymmetry: AI platforms not only intercept intent, but intent in natural language enables unbounded expression of goals and preferences, while service providers observe only behavior through GUIs, which constrains observable intent to finite control permutations. This information gap compounds over time, creating knowledge asymmetry where platforms develop comprehensive customer understanding while service providers remain informationally limited. Contrasting this equilibrium (E1) with the pre-LLM search engine baseline (E0) reveals the magnitude and recency of this shift: service providers lost an estimated 70% of operational intents (queries specifically about their own services, policies, and procedures) as AI platforms shifted from referral intermediation to synthesis intermediation. This equilibrium produces multi-dimensional sovereignty losses for service providers. Commercial firms lose intelligence sovereignty by remaining blind to customer intent during discovery, relationship sovereignty by being reduced to fulfillment endpoints, and potentially economic sovereignty if AI platforms monetize intent that providers cannot observe. In addition, both commercial firms and government agencies experience a loss of voice sovereignty: their canonical, authoritative articulation of products, services, rules, and obligations is increasingly mediated, summarized, or reinterpreted by AI platforms rather than communicated directly by the originating organization. Government agencies face a structurally deeper loss: as authoritative executors of public services, the mediation of voice is particularly damaging because it displaces the official framing, explanation, and interpretation of rights, obligations, and procedures away from the public authority, while, in many cases, foreign AI platforms become the primary interfaces through which intent is expressed, interpreted, and contextualized. We analyze a counterfactual equilibrium in which service providers deploy intent-resolution capabilities and accept natural-language intent directly while retaining exclusive execution authority. Although this does not eliminate AI platforms or their aggregation advantages for multi-provider contexts, it restores cost parity for single-provider navigational, learning, and issue-resolution intents, halts compounding informational divergence, and realigns intent routing with execution responsibility. We also examine intermediate policy interventions, including transparency mandates requiring platforms to disclose aggregated intent statistics, demonstrating why such measures provide transitional relief but cannot substitute for direct intent-resolution capabilities. The analysis has implications for market design, competition policy, digital inclusion, and public-sector sovereignty in the AI era.

---

## uid: `arxiv:2606.26429v1`

- title: DualEval: Joint Model-Item Calibration for Unified LLM Evaluation
- authors: Aaron J. Li, Hao Huang, Youngmin Park, Yitong Ma, Wei-Lin Chiang, Li Chen, Cho-Jui Hsieh, Bin Yu
- affiliations: not stated
- posted: 2026-06-24
- source: arXiv
- link: https://arxiv.org/abs/2606.26429v1
- keyword hits: llm, llms

### abstract

Current LLM evaluation relies on two complementary but often disconnected signals: static benchmarks with objective correctness labels and arena-style preference data that better reflect open-ended user interactions. We introduce DualEval, a latent model-item calibration framework that represents models and evaluation items in a shared space, jointly estimating model ability together with item difficulty and sharpness. We apply DualEval across four domains: coding, math, miscellaneous domain-knowledge tasks, and generic everyday user queries. Our evaluation uses 18 frontier LLMs, static benchmark labels, and reward-model scores validated against held-out human preferences for open-ended model responses. Empirically, our framework produces reliable and balanced model rankings, and its learned item-level profiles support downstream applications such as benchmark compression for sample-efficient evaluation and anomaly detection for contamination or outlier analysis. Overall, DualEval unifies static and arena-style evaluation through joint model-item calibration, producing model rankings and item-level diagnostics that support more sample-efficient, interpretable, and auditable evaluation pipelines.

---

## uid: `doi:10.2139/ssrn.6993643`

- title: How Generative AI Drives Innovation Performance: Evidence on the Mediating Role of Knowledge Integration
- authors: Jianhua Zhang, Wahab  Afolabi Azeez, Habib Isiaq, Shadrack  Notob Dackyirekpa, Yanhong Bai, Abdulahi  Oluwadamilare Issa, Emmanuel  Damilare Shittu
- affiliations: not stated
- posted: 2026-06-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6993643
- keyword hits: generative ai, generative artificial intelligence

### abstract

Generative artificial intelligence (GenAI) is transforming innovation, yet how firms translate its adoption into tangible outcomes remains unclear. Drawing on the knowledge-based view, this study examines whether GenAI adoption enhances innovation performance and whether knowledge integration mediates this relationship. Using text-mining of annual reports from 50 Chinese listed manufacturing firms (2022–2025, 200 firm-years) and Baron-Kenny mediation analysis with invention patent data, we find that GenAI adoption significantly increases innovation output, with knowledge integration mediating approximately 30% of the total effect. These findings identify knowledge integration as a critical organizational mechanism converting AI capabilities into innovation.

---

## uid: `doi:10.2139/ssrn.6879105`

- title: Autonomous CI/CD Quality Assurance Using LangGraph Multi-Agent Orchestration and Risk-Proportionate HITL Control
- authors: Kavita Jadhav
- affiliations: not stated
- posted: 2026-06-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6879105
- keyword hits: agentic, ai agent, llm

### abstract

Modern software delivery requires quality assurance that scales with development velocity. Manual test coordination, sequential test execution, and static risk assessment create bottlenecks that constrain release frequency and accumulate quality debt. This paper presents the K11tech Agentic AI QA System, a LangGraph-orchestrated multi-agent framework that automates the full CI/CD quality gate-from pull request analysis to defect filing-without requiring manual QA intervention for routine changes. The system orchestrates 14 specialist AI agents across four pipeline phases, decouples agent logic from external tools via seven Model Context Protocol (MCP) servers, and incorporates a risk-proportionate human-in-the-loop gate for high-risk changes. A self-evaluation layer using DeepEval and RAGAS continuously audits the quality of the system's own LLM-generated outputs. Experimental evaluation on 120 pull requests across three open-source repositories demonstrates a mean pipeline execution time of 8.3 minutes (σ = 1.9 min), an 87% reduction in Phase 2 execution time through parallel dispatch, a defect detection rate of 91.2% against a manually validated ground truth, and zero false-negative escapes to production during the evaluation period. The system is fully open source and deployable via a single Docker Compose command.

---

## uid: `doi:10.2139/ssrn.6881318`

- title: InvEvolve: Evolving White-box Inventory Policies via Large Language Models with Performance Guarantees
- authors: Chenyu Huang, Jianghao Lin, Zhengyang Tang, Bo Jiang, Ruoqing Jiang, Benyou Wang, Lai Wei
- affiliations: not stated
- posted: 2026-06-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6881318
- keyword hits: large language model, large language models, llm

### abstract

We study how large language models can be used to generate inventory policies in online settings with non-stationary demand. Our work is motivated by recent advances in LLM-based evolutionary search, such as AlphaEvolve, which demonstrates strong performance on static and highly structured problems such as mathematical discovery, but is not directly suited to dynamic inventory settings with online updates. We propose InvEvolve, an end-to-end inventory policy evolution and inference framework grounded in confidenceinterval-based certification. Built on a large language model trained via reinforcement learning, InvEvolve can process demand data together with additional numerical and textual features, and generates white-box inventory policies with statistical safety guarantees for future deployment. We further introduce a unified framework with theoretical guarantees that connects training, inference, and deployment. This allows us to derive a lower bound on the probability that InvEvolve evolves a statistically safe and improved policy, and to characterize the multi-period performance gap relative to the oracle-safe benchmark. Tested on both synthetic data and real-world retail data, InvEvolve outperforms classical inventory policies and deep-learning-based methods. In canonical inventory settings, it generates new policies that outperform existing benchmarks.

---
