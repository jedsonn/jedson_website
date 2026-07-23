# Classification batch 107 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-107.answer.json` as a JSON array.

---

## uid: `arxiv:2607.00738v2`

- title: Phantom References: Hallucinated Citations That Survive Peer Review at Top-Tier Conferences
- authors: Mark Russinovich, Ram Shankar Siva Kumar, Ahmed Salem
- affiliations: not stated
- posted: 2026-07-01
- source: arXiv
- link: https://arxiv.org/abs/2607.00738v2
- keyword hits: chatgpt, large language model, large language models

### abstract

Large language models can generate polished scientific text that includes unsupported claims, allowing hallucinations to enter the archival record. Assessing this risk via technical statements is difficult and often requires expert judgment, but citations provide a more auditable surface: a reference either resolves to a real scholarly work with compatible authorship, or it does not. We measure citation hallucination in peer-reviewed proceedings using a conservative definition limited to identity-level failures: non-existent works and substantial author-list mismatches. We explicitly exclude ordinary bibliographic drift (e.g., venue/year differences, publication-status updates, minor name variants). To audit citations at scale, we build RefChecker, a verification pipeline that resolves bibliography entries against multiple bibliographic sources and escalates unresolved cases to web-search re-verification. We apply RefChecker to accepted camera-ready papers from ICLR, ICML, NeurIPS, and USENIX Security. Hallucinated citations have entered the archival record. While reference-level rates are usually below 1%, proceedings are large enough that paper-level failures are visible: in 2025, roughly one in twenty NeurIPS and USENIX Security papers contains at least two likely hallucinated academic-paper-like references under our strict definition. We also observe post-ChatGPT increases in several venues, including a tail of papers with 5+ failures in a single bibliography, and likely hallucinated citations even among award-winning papers. These results suggest peer review alone does not reliably enforce citation integrity, yet auditing is tractable (about 0.04$ per paper in one venue-scale scan). We open-source RefChecker for routine, reproducible citation verification before publication (https://github.com/markrussinovich/refchecker).

---

## uid: `arxiv:2607.00368v1`

- title: Beyond Perplexity: A Behavioral Evaluation Framework for Deployment-Memory Claims in LLM Test-Time Training
- authors: Xiangchen Song, Zhenhao Chen, Lingjing Kong, Shaoan Xie, Xinshuai Dong, Guangyi Chen, Kun Zhang
- affiliations: not stated
- posted: 2026-07-01
- source: arXiv
- link: https://arxiv.org/abs/2607.00368v1
- keyword hits: large language model, llm, qwen

### abstract

Large language model test-time training (TTT) is often evaluated through local proxy metrics: models are updated on recent tokens, retrieved context, target-domain data, or verifiable task attempts, and then judged by perplexity, future-token loss, long-context performance, or reward. These metrics are well matched to claims about stream adaptation, domain adaptation, context compression, and reward-backed test-time improvement. They are weaker evidence, however, for a capability that TTT results are increasingly used to motivate: deployed assistant memory, personalization, or sparse post-deployment learning, which instead requires behavioral evidence such as later recall, paraphrase robustness, retention, locality, conflict handling, and use in downstream actions after the original support context is removed. We introduce a behavioral evaluation framework that calibrates TTT memory claims to the evidence that supports them. It has two components: a claim-calibrated evidence ladder that separates stream/domain adaptation, bridge internalization, and deployment-time behavioral learning; and an evaluation protocol with matched explicit-memory baselines and mutually exclusive failure categories. We validate the framework by auditing recent TTT and memory-adjacent work and by instantiating it as a controlled diagnostic in which, in a sparse nonce-fact setting, one-step LoRA updates lower support and answer loss across three Qwen3 model scales while generated free-form recall stays at zero, exposing a measurable gap between proxy improvement and deployment behavior. The framework gives authors and evaluators a concrete standard for aligning TTT memory claims with the evidence actually reported.

---

## uid: `doi:10.2139/ssrn.6908358`

- title: CyberTrust AI: An LLM-Based Framework for Automated Smart Contract Vulnerability Detection, Classification, and Remediation
- authors: Yash Mandaviya
- affiliations: not stated
- posted: 2026-07-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6908358
- keyword hits: claude, large language model, llm

### abstract

Smart contract vulnerabilities have caused documented financial losses exceeding $6 billion across decentralized finance (DeFi) ecosystems between 2020 and 2024. Existing automated security toolsincluding Slither, Mythril, and Manticoreemploy rule-based static analysis that systematically fails to detect contextual, indirect, and semantically complex vulnerability patterns that are commonly exploited in production attacks. This paper presents CyberTrust AI, a production-deployed security analysis framework that applies large language model (LLM) inference via Anthropic's Claude Sonnet to perform contextual, semantic vulnerability analysis of Solidity smart contracts. The system identifies critical vulnerability classes including reentrancy attacks, integer overflow and underflow, unprotected self-destruct, unchecked external call return values, tx.origin authentication abuse, timestamp manipulation, and access control logic flawsgenerating severity-classified structured findings, natural language attack vector explanations, automated Solidity remediation code, and cryptographically verifiable onchain NFT trust scores. The complete system has been deployed at cybersheild-sooty.vercel.app and implements seven production capabilities: multi-mode audit analysis (security audit, threat simulation, gas optimization), realtime streaming analysis output, batch multi-file contract auditing, side-by-side contract diff comparison, conversational AI chat assistance for vulnerability Q&A, and a public trust score leaderboard. We conducted preliminary evaluation on 35 annotated Solidity contracts covering five canonical vulnerability types, demonstrating that LLM-based contextual analysis successfully detects all vulnerability instances while conventional static analysis tools miss approximately 13% of contextual casesparticularly indirect reentrancy patterns and access control logic errors requiring cross-function semantic reasoning. A full quantitative comparative evaluation is in progress.

---

## uid: `arxiv:2607.01854v1`

- title: Has This Checkpoint Been Abliterated? A Two-Signal Audit and Its Failure Map
- authors: Gabriel Hurtado
- affiliations: not stated
- posted: 2026-07-02
- source: arXiv
- link: https://arxiv.org/abs/2607.01854v1
- keyword hits: deepseek, llama, qwen

### abstract

Can a platform tell, before deployment, whether an open-weight checkpoint has had its refusal mechanism stripped? Runtime guards cannot: they score generations, not the artifact. We combine two cheap internal signals, a reference-anchored activation refusal-gap and a weight-recovery energy of the base-to-candidate weight difference, into a threshold-free checkpoint audit. The two are negatively correlated and label-complementary: the gap supplies refusal-specificity and the weight energy supplies recall. On a 273-checkpoint registry spanning Qwen, DeepSeek-distilled Qwen, Llama, and Gemma, their z-sum separates 57 public abliterations from 37 benign fine-tunes, merges, and instruction-tunes at AUROC 0.95, significantly above either signal alone (0.84, 0.90), and a Youden-calibrated threshold transfers to held-out families at balanced accuracy 0.89 (FPR 0.11), missing only 4 of 57. We then map two failures, in order of severity: a spoofed reference evades both axes with no training (ΔW=0, \r{ho}=1 by construction), and a white-box owner trains a checkpoint past the threshold while it stays guard-unsafe and coherent. The audit is effective triage, not tamper-proofing: it presumes an attested reference, and its claims are bounded by the registry we evaluate it on.

---

## uid: `arxiv:2607.01612v1`

- title: Scaling with Confidence: Calibrating Confidence of LLMs for Adaptive Test Time Scaling
- authors: Xuqing Yang, Yi Yuan, Shanzhe Lei, Xuhong Wang
- affiliations: not stated
- posted: 2026-07-02
- source: arXiv
- link: https://arxiv.org/abs/2607.01612v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Training large language models (LLMs) with reinforcement learning (RL) has significantly advanced their performance on reasoning and question-answering tasks. However, prevailing RL reward designs typically prioritize response correctness, neglecting to incentivize models to express their confidence accurately. This leads to a critical problem: performance gains are often accompanied by poor calibration between confidence and accuracy, misleading models to overconfidently hallucinate when uncertain. To address this limitation, we propose $\textbf{C}$orrectness and $\textbf{C}$onfidence $\textbf{C}$alibration $\textbf{R}$einforcement $\textbf{L}$earning ($\textbf{C3RL}$), a novel RL algorithm integrating correctness, calibration and dataset-informed reference accuracy rewards together. Comprehensive evaluation across 8 text and multimodal datasets demonstrates that C3RL enhances calibration without sacrificing accuracy, outperforming the current state-of-the-art method in both performance and calibration metrics. Utilizing the well-calibrated verbalized confidence from C3RL, we further introduce $\textbf{C}$onfidence-based $\textbf{A}$daptive Test Time $\textbf{S}$caling ($\textbf{CAS}$), an adjustable inference-time strategy that allocates computational resources based on response confidence. Experiments show that CAS surpasses majority voting on both in-domain and out-of-domain datasets while reducing the inference budget by up to 12.33 times. We believe the synergy of C3RL and CAS paves the way for deploying more reliable and resource-efficient LLMs. The code, data and models will be released.

---

## uid: `doi:10.2139/ssrn.7051224`

- title: LLM as a Forensic Reasoner: Expert-Guided Video Deepfake Detection Across Modalities
- authors: Jiaxin Liu, Jia Wang, Saihui Hou, Min Ren, Huijia Wu, Long Ma, Zhaofeng He
- affiliations: not stated
- posted: 2026-07-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7051224
- keyword hits: large language model, large language models, llm, llms

### abstract

The proliferation of sophisticated deepfakes presents a critical challenge that transcends mere visual artifact detection. Current methods, often operating as black boxes, exhibit poor generalization to forgery techniques and lack the interpretability required for trusted, real-world deployment. This limitation stems from treating detection as a pattern recognition task rather than a forensic reasoning problem. To bridge this gap, we propose a paradigm shift with FALCON, a framework that re-conceptualizes the role of Large Language Models (LLMs) in deepfake detection. Instead of being a low-level data processor, the LLM in FALCON acts as a central forensic reasoner. It synthesizes low-dimensional, symbolic evidence extracted by a committee of specialized expert modules. This hierarchical design elegantly circumvents the computational costs and lack of forensic priors inherent in direct LLM video analysis. Crucially, we introduce a three-stage, human-in-the-loop training paradigm to generate and certify high-quality forensic rationales, ensuring the LLM’s reasoning is both reliable and explainable. Extensive experiments show that FALCON not only achieves state-of-the-art performance, particularly on challenging difusion-based forgeries, but also demonstrates superior cross-domain generalization, validating it as a robust and interpretable forensic reasoning system.

---

## uid: `doi:10.2139/ssrn.7049101`

- title: When Some Investors Have Superior AI: Evidence from China's Stock Connect Programs
- authors: Hongyi Qu, Yuhang Qiu, Cheng Xiang, Qingbo Yuan
- affiliations: not stated
- posted: 2026-07-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7049101
- keyword hits: chatgpt, deepseek, generative ai

### abstract

We examine whether unequal access to generative AI (GenAI) widens information disparities among investors. Using a difference-in-differences design, we find that informed trading, measured by VPIN, for Chinese Stock Connect constituent firms tradable by foreign investors increases significantly after the launch of ChatGPT relative to non-constituent firms, which are predominantly traded by domestic investors with limited GenAI access before 2025. This effect is stronger for firms with higher foreign trading intensity or information-processing costs, suggesting that the increase is driven by foreign investors’ GenAI-enabled information-processing advantages. Consistent with this, the predictive power of foreign investors’ trades on future stock returns increases significantly after ChatGPT’s launch. Finally, the relative VPIN gap between Connect-constituent and non-constituent firms disappears following the release of DeepSeek in 2025, when domestic investors gained access to more comparable GenAI tools. Our findings suggest that the uneven diffusion of GenAI can widen informational inequality in financial markets.

---

## uid: `doi:10.2139/ssrn.7044979`

- title: Enhancing System Design Knowledge: A Comparative Study of Natural Language Processing (NLP) approaches for extracting Axiomatic Design theory
- authors: Marc Losanno, Vito Giordano, Fantoni Gualtiero
- affiliations: not stated
- posted: 2026-07-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7044979
- keyword hits: large language model, large language models, llm, llms

### abstract

Patent documents constitute one of the most important sources of engineering knowledge. Extracting this knowledge from large patent collections has become increasingly valuable for supporting engineering design and research activities. To achieve this, NLP techniques are widely applied to identify engineering concepts of design theories in such technical documents. An important design theory for improving the engineering design process is Axiomatic Design (AD), which maps the relationships between functional requirements and design parameters for analysing the design of systems. However, identifying AD concepts in patent texts using NLP remains complex and relatively underexplored. This paper investigates the extraction of AD concepts from patent texts, comparing three NLP approaches: a rule-based expert system, supervised machine learning models, and prompt-based Large Language Models (LLMs). We developed a benchmarking dataset of 6,000 USPTO patent sentences annotated for Named Entity Recognition and Joint Entity and Relation Extraction, capturing functional requirements, design parameters, and axiomatic relations. Results show that supervised machine learning models outperform rule-based and prompt-based LLM approaches in extracting entities and relations. While functional requirements and design parameters are extracted with high accuracy, the axiomatic relations remain challenging due to their abstract nature, implicit description, and rarity. A case study on 729 protective face mask patents demonstrates that AD concepts are embedded in patent documents, supporting engineers in mapping functional requirements-design parameters relationships. This work provides a standardized annotated dataset, a unified comparative evaluation framework, and empirical evidence that integrating AD theory with NLP can enable knowledge-based systems for design analysis and decision-making.

---
