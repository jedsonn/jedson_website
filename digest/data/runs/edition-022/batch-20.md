# Classification batch 20 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-20.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7321995`

- title: Leakage-Controlled Seriousness Triage of Spontaneous Adverse-Event Reports: A Behavioral Leakage Audit, Temporal Validation Framework, and Large Language Model Comparison on Novel First-in-Class Drugs
- authors: Shakil Mahmud
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7321995
- keyword hits: large language model, llm

### abstract

Highlights• A behavioral ablation audit flags proxy leaks missed by standard blacklists.• A model with no clinical features reached AUROC 0.879 via reporting proxy leaks.• Temporal, novel-drug validation exposes a cold-start gap hidden by random splits.• Stable AUROCs can mask threshold-induced triage recall disparities by subgroup.• LLM drug knowledge improves triage accuracy during novel drug cold-starts.

---

## uid: `doi:10.2139/ssrn.7316382`

- title: Trust, Delegation, and Alignment in Human-AI Decision Making
- authors: Erik O. Kimbrough, Brennan McDavid, Diba Vazirian
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7316382
- keyword hits: chatgpt, gpt-4, gpt-5

### abstract

This paper studies delegation to artificial intelligence in a setting where human principals retain the consequences of delegated choices. Participants wrote prompts instructing ChatGPT-4o mini how to choose on their behalf in three canonical economic domains: risky choice, intertemporal choice, and social allocation. We then elicited the compensation participants required to let the AI's choices count for payment and compared participants' own choices to choices generated from their prompts. The design produces two central empirical objects: a revealed measure of reluctance to delegate, captured by willingness to accept compensation for AI delegation, and a behavioral measure of alignment, captured by the share of decisions on which the participant and AI made the same choice. We supplement the original experiment with two benchmarks: a human-agent follow-up in which other participants attempted to implement the same prompts, and an ex post robustness exercise using GPT-5.5. The results show substantial reluctance to delegate despite moderate-to-high alignment, and they suggest that misalignment reflects not only model limitations but also the difficulty of communicating delegable preferences through short natural-language prompts.

---

## uid: `doi:10.2139/ssrn.7317146`

- title: Leveraging Generative Artificial Intelligence for Supply Chain Resilience and Economic Performance within Industry 5.0
- authors: Wahib Elayah, Abdullah ALOQAB, SULEMAN BAWA
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7317146
- keyword hits: generative ai, generative artificial intelligence

### abstract

Purpose: This study examines how Generative AI (GenAI) enhances supply chain resilience and economic performance within the Industry 5.0 context. It focuses on how firms move beyond reactive responses to disruptions toward more anticipatory and adaptive capabilities, and how these improvements contribute to broader economic stability.,Design/methodology/approach: Drawing on a longitudinal panel of manufacturing and logistics firms across multiple economies, the study employs structural equation modeling alongside dynamic panel estimation techniques. This combined approach enables the analysis of both mediating and moderating relationships while accounting for endogeneity and temporal dynamics in AI adoption and performance outcomes.,Findings: The results show that GenAI adoption significantly improves supply chain resilience, which in turn enhances firm-level economic performance. Approximately half of the performance gains associated with GenAI are transmitted through resilience. The effects are stronger in contexts with higher levels of digital infrastructure and in firms that effectively integrate human expertise with AI systems. At the macro level, improvements in firm performance contribute to more stable production and trade patterns.,Originality: This study reframes GenAI as a driver of resilience rather than merely efficiency. It offers a multi-level perspective linking firm capabilities to macroeconomic outcomes and highlights the central role of human–AI integration in realizing value from emerging technologies.

---

## uid: `doi:10.2139/ssrn.7292338`

- title: Beyond Transformers: Limitations of Sequence Models in Real-World Intelligence Systems
- authors: Harsh Singh
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7292338
- keyword hits: large language model, large language models

### abstract

Transformer-based large language models have achieved remarkable performance across diverse benchmarks, yet their deployment in domains demanding persistent reasoning, causal inference, and verifiable decision-making reveals systematic inadequacies. This paper introduces the Real-World Intelligence Requirements (RWIR) framework, a formal specification of five capability dimensions essential for general-purpose intelligence: persistent adaptive memory, causal-interventional reasoning, output verifiability, modular compositional coordination, and integrated neuro-symbolic inference. We define three foundational limitation constructs, Context-Bounded Reasoning, Stateless Inference Limitation, and the Non-Verifiable Output Problem, and develop a structured taxonomy of twelve failure modes organized across four categories. Through conceptual experiments and hypothetical long-horizon scenarios, we demonstrate that these failures are architectural rather than scale-dependent, and argue that overcoming them is unlikely to be achieved solely through scaling existing paradigms.

---

## uid: `arxiv:2608.19760v1`

- title: Credit Without Ground Truth: Auditing Step-Level Credit Assignment in LLM Agents Against Executed Replay
- authors: Haiyue Zhang
- affiliations: not stated
- posted: 2026-08-20
- source: arXiv
- link: https://arxiv.org/abs/2608.19760v1
- keyword hits: llm, qwen

### abstract

Audited against causal ground truth from executed replay in a single-agent tool environment (ALFWorld), none of the step-level credit signals used to train LLM agents -- LLM-judge scores, outcome-conditioned logprob ratios, or the policy's own confidence -- identifies which steps causally matter better than chance. Existing evaluations grade these signals against annotated step *correctness*; we audit them against step *contribution* -- what re-sampling the policy's own alternatives at each decision point and rolling forward actually changes about the outcome -- and the two come apart. The ground truth itself is structured: causal contribution is sparse (30.5% of decision points where ground truth is defined carry measurable effect), and measurability is model-dependent -- the fraction of points with no policy-supported counterfactual differs by a factor of two (13.1% vs. 26.8%) between two similar-scale policies. The failure mode is identifiable: implicit credit echoes the policy's fluency (median rank correlation +0.75, replicating at +0.70 in a second family under a corrected instrument), while conditioning on the outcome adds no causal information (partial correlation -0.004, Qwen). A confidence-only router recovers pivotal steps at chance level, but cuts judge cost by 13.1% per turn (14.0% per trajectory). In a seven-arm pre-registered training experiment, no arm reliably outperforms the untrained policy, and the checkpoints' apparent instrument signature is fully explained by training dose -- sparser credit retains fewer examples, an order-of-magnitude spread in optimizer steps -- not credit content. Comparisons of credit rules must therefore match effective sample size, or they measure dose, not credit.

---

## uid: `doi:10.2139/ssrn.7323260`

- title: Consent-Aware Data Pipelines: Tracking Training Data Provenance for Generative AI Compliance
- authors: jagan ankam
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7323260
- keyword hits: generative ai, generative artificial intelligence

### abstract

Training-data provenance refers to the systematic management of information concerning the origin, ownership, consent conditions, and processing history of data throughout its lifecycle. This has become increasingly important in Generative Artificial Intelligence (GenAI), where large and heterogeneous training corpora require reliable mechanisms for traceability, accountability, and compliance. However, large-scale data ingestion approaches commonly depend on source metadata, dataset manifests, and processing logs to reconstruct data histories. Such mechanisms can result in incomplete provenance traceability when source identity, ownership information, consent attributes, and transformation events become disconnected during distributed data processing. Recent approaches based on metadata governance and data-lineage tracking improve visibility into these processes, but compliance verification remains challenging when consent information is missing, inconsistently propagated, or difficult to validate against downstream policies. To address these limitations, we propose the Consent-Aware Data Pipeline (CADP) framework. CADP consists of two stages: (i) Provenance and Consent Capture, which records source, ownership, consent, and transformation information during data ingestion and processing, and (ii) Policy Validation and Compliance Auditing, which evaluates the preserved information against predefined governance requirements. Experimental evaluation on The Pile and Common Crawl demonstrates that CADP achieves 96.4% provenance traceability, 98.1% metadata preservation, and 94.7% compliance verification accuracy, while introducing only 8.6% processing overhead.

---

## uid: `doi:10.2139/ssrn.7322182`

- title: GSA Regulation 552.239-7001: Safeguarding Data in LLMs -A Commenter Discourse Analysis
- authors: Cari Miller
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7322182
- keyword hits: llm, llms

### abstract

The General Services Administration's (GSA) proposed GSAR clause 552.239-7001 represents a foundational effort to standardize data protection, intellectual property rights, and ethical artificial intelligence (AI) development within federal procurement. This paper presents a qualitative thematic discourse analysis of 77 public comments submitted in response to Notice MVAC-2026-01, synthesizing perspectives from factions of stakeholders throughout the AI value chain to identify critical fault lines between government safeguarding requirements and commercial technical realities. Commenter discourse is categorized into scope challenges, near-consensus technical defects, divergent policy beliefs, and comprehensive solutions, which subsequently demonstrate that the locus of control for each AI actor responsible for addressing risks and implementing governance actions is misaligned with the proposed regulatory requirements. To resolve these structural frictions, this research recommends a harmonized procurement roadmap for senior procurement professionals, IT executives, and GSA leaders to consider. By advocating for a multi-layered policy approach that differentiates between foundational model baselines and solution-specific requirements, the paper illustrates how integrating industry standards and advanced frameworks can successfully operationalize compliance, balance risk mitigation with technical truths, and establish realistic governance expectations for modern AI procurement.

---

## uid: `doi:10.2139/ssrn.7322018`

- title: Materials Design for Data Center Thermal Management and Waste Heat Recovery: Dielectric Fluids, Gallium Liquid Metals, and Embedded Two-Phase Cooling
- authors: Michael Bustamante, Kristina Lilova
- affiliations: not stated
- posted: 2026-08-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7322018
- keyword hits: large language model, llm

### abstract

Artificial intelligence (AI) and large language model (LLM) data centers are projected to consume more than 1,000 TWh of electricity annually by 2026, with nearly all of this energy ultimately rejected as heat. This work reframes data center thermal management as a materials design problem in which coolant selection governs the thermal pathway, determines the achievable coolant outlet temperature, and consequently defines the quality and recoverability of waste heat. Three generations of cooling technologies are evaluated. Dielectric immersion fluids deliver outlet temperatures of 65-75 °C, enabling direct integration with district heating networks without heat pumps while eliminating cooling water consumption. Gallium-based liquid metal coolants provide thermal conductivities 200-600 times higher than dielectric fluids and reduce transient temperature rise by 60-68%, enabling higher operating temperatures and improved heat recovery. Embedded two-phase microfluidic cooling further advances thermal performance by transferring phase change directly to the chip surface, sustaining heat fluxes approaching 1 kW cm⁻² while maximizing recoverable thermal energy. Across these cooling generations, coolant composition-and therefore the melting range-should be regarded as a design variable rather than a fixed material property, allowing liquid metal coolants to be engineered for different operating conditions. The results demonstrate that coolant materials selection is not solely a thermal management decision but also an energy systems design choice that directly influences waste heat utilization, water consumption, and carbon emissions.

---
