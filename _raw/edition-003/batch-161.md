# Classification batch 161 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-161.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6854679`

- title: Antitrust Regulation of Generative AI Foundation Models: Antitrust Risks, Regulatory Frameworks and Policy Recommendations
- authors: Zhishan Deng, Jiani Wu
- affiliations: not stated
- posted: 2026-05-31
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6854679
- keyword hits: foundation model, generative ai

### abstract

The rapid integration of GenAI into corporate, legal, and economic paradigms has elevated foundation models from specialized technical tools to fundamental economic infrastructure. Positioned at the bedrock of a distinct three-tier pyramid structure, these models dictate the viability and evolutionary trajectory of all downstream vertical applications. However, this market layer is vulnerable to structural consolidation. This study constructs an integrated analytical framework—coordinating Gatekeeper Theory, Hierarchy-Based Value Chain Theory, and Ecosystem Theory—to diagnose the antitrust risks inherent to the GenAI foundation model landscape. The analysis reveals that market incumbents consolidate market power and restrict ecosystem competition through upstream data privatization, the deployment of proprietary APIs, and complementary partnerships. Furthermore, this paper evaluates the prevailing policy responses across key jurisdictions and uncovers structural regulatory limitations. This study further advocates for a paradigm shift toward an agile, dual framework of exante governance. Policy recommendations include implementing progressive data-sharing mandates, formulating common pre-training data standards, establishing quantifiable metrics for hierarchical open-source compliance, reinforcing risk identification for interface power, and adapting merger control to scrutinize non-traditional resource- and talent-based acquisitions.

---

## uid: `doi:10.2139/ssrn.6854700`

- title: Weight-Only Quantization Does Not Always Save Energy: An Empirical Study of LLM Inference Across NVIDIA GPU Platforms
- authors: Hongping Zhang
- affiliations: not stated
- posted: 2026-05-31
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6854700
- keyword hits: large language model, llm

### abstract

Low-precision weight-only quantization, such as NF4 and mixed-precision INT8, is widely used to reduce the memory footprint of large language model (LLM) inference, and it is often assumed to reduce energy consumption as well. This assumption does not always hold because runtime quantization can introduce dequantization and mixed-precision overheads whose energy cost depends on model scale and hardware platform. We measure quantized LLM inference energy using direct NVIDIA Management Library (NVML) power sampling across 270 configurations, excluding supplementary Tesla T4 runs, covering six decoder-only model families, three precision formats including the FP16 baseline (FP16, NF4, INT8), three directly measured NVIDIA GPU platforms (RTX 4090D, RTX 5090, and A800), and five batch sizes. The main result is a model-size-dependent sign reversal: under the evaluated bitsandbytes implementation, NF4 increases energy by approximately 25--45% for 1.1--1.5B models, but saves about 23% for 6B--9B models. INT8 shows a larger small-model overhead of approximately 33--55%, consistent with dynamic outlier-handling pathways, and saves about 15% for larger models. We interpret this pattern through an analytical framework that balances runtime dequantization overhead against memory-bandwidth savings. The crossover values are operational reference bounds rather than exact hardware constants, and the INT8 behavior is specific to the evaluated mixed-precision implementation. Supplementary Tesla T4 measurements near the 3B region provide qualitative evidence that the small-model penalty persists inside the 1.5B--6B interval. These findings show that weight-only quantization is not a universal energy-saving strategy: precision selection should be guided by model scale, hardware, and quantization backend.

---

## uid: `doi:10.2139/ssrn.6854625`

- title: Voluntary Sustainability Reporting and LLM-Based ESG Disclosure Quality: Evidence from Korea
- authors: Je Hyun BAE, JaeHo Lee, Eun-Chong Kim, Jaehee Jang
- affiliations: not stated
- posted: 2026-05-31
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6854625
- keyword hits: gemini, llm

### abstract

This study examines the role of voluntary sustainability reporting in firms’ ESG information environments during prolonged transition toward mandatory ESG disclosure. Using Korean-language sustainability reports and conventional ESG ratings, we construct report-level measures of disclosure quality with Gemini 3 Flash. We find that voluntary reporters have higher conventional ESG ratings than non-reporters, and that among reporting firms, textual quality, clarity, and reporting continuity are associated with subsequent external ESG assessments. Furthermore, voluntary sustainability reporting is positively associated with subsequent conventional ESG ratings. The evidence suggests that voluntary sustainability reports convey ESG-relevant information before mandatory reporting requirements. LLM-based measures help capture the quality of this information channel in a non-English reporting environment.

---

## uid: `doi:10.2139/ssrn.6864773`

- title: Quality Assurance of Large Language Model-based Software: A Systematic Literature Review
- authors: Jonathan O&apos;Berry, Dr. Upulee Kanewala
- affiliations: not stated
- posted: 2026-06-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6864773
- keyword hits: large language model, llm

### abstract

Large Language Model (LLM) based software has become increasingly utilized, including in critical and high-risk fields. Given the increasing use of LLM-based software, it is more important than ever to evaluate its quality. This study presents a systematic literature review (SLR) of quality assurance methods for LLM-based software, synthesizing evidence from 19 primary studies selected through a structured protocol across major digital libraries.This study finds that the evaluation of LLM-based software is primarily split into manual and automated evaluation, each with trade-offs between semantic depth and scalability. Additionally, this work categorizes key challenges in evaluating LLM-based software, including limited availability of domain-specific datasets, high human effort in manual evaluation, difficulty in assessing functional correctness (e.g., for code generation), model non-determinism and evolution, and substantial computational costs. Furthermore, it also finds that researchers are actively creating new evaluation systems and frameworks, alongside a lack of standardization in metrics and methodologies. This study contributes (1) the first structured synthesis of QA practices for LLM-based software systems, (2) a comprehensive taxonomy of evaluation methods, metrics, and challenges, and (3) the identification of critical research gaps, including the need for standardized and hybrid evaluation approaches. By consolidating dispersed knowledge, this SLR provides a foundation for advancing systematic, scalable, and context-aware quality assurance of LLM-based software.​

---

## uid: `doi:10.2139/ssrn.6809844`

- title: Risk Factor Disclosure Summaries
- authors: James Blann, James Moon, Yuxiao Wang
- affiliations: not stated
- posted: 2026-06-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6809844
- keyword hits: large language model, llm

### abstract

Since 2005, the SEC has mandated that firms include Risk Factor Disclosures (RFDs) in annual 10-K filings. In 2020, this mandate was “modernized” and now requires the inclusion of a two-page summary section for RFDs longer than 15 pages. On the one hand, the SEC contends that this summary requirement should benefit investors, especially those who have less time to review and analyze registrants’ disclosure. On the other hand, firms may not include all material risks in a summary, and, if some investors fixate on summaries, gaps in understanding risks may widen among investors. We use summaries generated by a large language model (LLM) as a benchmark to examine the information content of firm-disclosed summaries. Our evidence suggests that, relative to the LLM-generated summaries, firm-disclosed summaries are more positively toned, less specific, easier to read, and more likely to omit firm-idiosyncratic risks such as strategic, legal, and human-capital risks. Our results also suggest that summaries that deviate more from the LLM benchmark are associated with higher information asymmetry, uncertainty, and disagreement around the 10-K filing date. These effects do not appear to be explained by changes in risks disclosed in the full RFD surrounding the Modernization or lookahead bias in our benchmark summary generation. Overall, our results suggest that the summary requirement in the SEC’s 2020 Modernization may have led to unintended negative consequences, at least over the initial years that are covered by our sample.

---

## uid: `doi:10.2139/ssrn.6806138`

- title: Generative AI in Capital Markets: Information Production, Dissemination, and Processing
- authors: Sean S. Cao, Wilbur Chen, Guang Ma, Suraj Srinivasan
- affiliations: not stated
- posted: 2026-06-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6806138
- keyword hits: generative ai, generative artificial intelligence

### abstract

We synthesize evidence from six papers presented at the 2025 Journal of Accounting Research Conference on how generative artificial intelligence (GenAI) is reshaping capital-market information flows. Our discussion is organized around an economic framework with three layers: information production by firms and accounting professionals, information dissemination through intermediaries, and information processing by investors. Across these layers, the conference papers show that GenAI can lower preparation costs, improve intermediary productivity, and reduce investors’ processing costs. At the same time, they point to a common constraint: whether GenAI improves the information environment depends critically on information verification costs. We also highlight gaps in current evidence and outline future research opportunities within and across the three layers.

---

## uid: `doi:10.2139/ssrn.6866863`

- title: Artificial Intelligence Governance in Higher Education: A Comparative Study of Generative AI Strategies and Policy Frameworks in North American and Chinese Universities
- authors: Chengyuan Liang, Yan Shvartzshnaider, Kean Birch
- affiliations: not stated
- posted: 2026-06-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6866863
- keyword hits: deepseek, generative ai

### abstract

Generative AI (GenAI) services are being embedded in university teaching, research, and administrative systems, raising a range of governance questions about service access, data use, and institutional responsibility – amongst other issues. To understand how GenAI services are being embedded, we analysed the policy and guidance frameworks of 101 top universities defined by the 2025 Times Higher Education World University Rankings in the US, Canada, mainland China, and Hong Kong to compare their approach to GenAI governance. We use this analysis to identify different university GenAI governance approaches across jurisdictions: in the US and Canada, GenAI policy or guidance frameworks are mainly constituted at the unit level; whereas, mainland China had a diverse mix of university-wide policy, external policy and guidance, and gaps in coverage for certain policy categories; and last, Hong Kong universities had a mix of both university-wide and unit-level policy and guidance frameworks. Our analysis also showed that North American universities more often distinguish between institutionally licensed, third-party, and restricted services, with a focus on specific data-handling practices. By contrast, mainland China and Hong Kong universities more frequently provide approved services through campus-integrated platforms or self-hosted systems. To illustrate these differences in governance approaches in more depth, we analysed how universities treat DeepSeek. GenAI-related policies and guidance frameworks usually identify basic service statuses and data-entry limits, while more detailed conditions on retention, model training, onward sharing, deletion, storage location, and provider responsibility are often contained in separate and commercial provider terms and agreements.

---

## uid: `doi:10.2139/ssrn.6867203`

- title: Epistemically Bounded Rationality: Generative Artificial Intelligence, the Weight of Arguments, and the Reconfiguration of Decision-Making Constraints
- authors: Milton  Freitas Chagas
- affiliations: not stated
- posted: 2026-06-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6867203
- keyword hits: generative ai, generative artificial intelligence

### abstract

Generative AI has sharply reduced the cost of searching for information and generating alternatives, but it has not proportionally improved the capacity to evaluate the evidential robustness of those outputs. This asymmetry reconfigures the classical bottleneck of organizational decision-making: from informational scarcity to evidential validation under conditions of informational abundance. Existing frameworks explain this shift only partially. Bounded rationality models decisional constraints primarily in terms of limited information-processing capacity; automation bias explains excessive reliance on automated systems without fully accounting for its structural persistence; and explainable AI approaches treat opacity mainly as a property of system design rather than as a limitation associated with dominant optimization architectures. Drawing on Keynesian uncertainty, March’s exploration–exploitation framework, and recent work on epistemic uncertainty in machine learning, this paper’s primary contribution is the construct of epistemically bounded rationality. To explain the mechanism underlying this condition, the paper additionally develops the concept of exploratory inflation and situates it within the industrial stabilization of the transformer-based dominant design. Epistemically bounded rationality is proposed as a reconfiguration of bounded rationality in which the binding constraint on decision quality shifts from information generation toward the evaluation of evidential weight. Under these conditions, agents may become increasingly confident despite declining evidential robustness. The paper further argues that this limitation is reinforced by the industrial stabilization of the transformer-based dominant design of generative AI systems. Implications for organizational decision-making, AI governance, and human–machine interface design are discussed.

---
