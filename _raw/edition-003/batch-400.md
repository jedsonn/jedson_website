# Classification batch 400 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-400.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6992489`

- title: Domain-adaptive mixture-of-experts for cross-dataset lithium-Ion battery SOH prediction via adaptive strategy selection
- authors: Liu Teng, Wei Li, Zhiqiang Li, Weiwei Huo
- affiliations: not stated
- posted: 2026-06-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6992489
- keyword hits: fine-tuning

### abstract

Accurate cross-dataset state of health prediction for lithium-ion batteries remains challenging due to distribution shifts arising from diverse cathode chemistries, operating temperatures, and charge-discharge protocols across heterogeneous battery fleets. This study proposes a Domain-Adaptive Mixture-of-Experts framework that automatically selects the optimal domain adaptation strategy for each target domain through a lightweight linear gating network comprising merely 32 learnable parameters. The framework integrates a shared Transformer-based backbone with four adaptation strategies spanning the full spectrum of target-domain information utilization, namely Zero-shot transfer, Test-Time Adaptation, Fine-Tuning, and Model-Agnostic Meta-Learning. Comprehensive evaluation on 564 battery cells from seven publicly available datasets under Leave-One-Domain-Out Cross Validation protocol demonstrates that the proposed framework achieves an average coefficient of determination of 0.864 with perfect oracle strategy alignment under full domain training and maintains competitive generalization at average [[EQUATION]] of 0.795 when each target domain is held out during gating network training. Hard argmax selection consistently outperforms weighted fusion across all seven domains with an average margin of +0.027 in [[EQUATION]], confirming that the four adaptation strategies compete rather than cooperate in this application context. Feature ablation analysis identifies sample count as the dominant determinant of strategy selection with performance degradation of [[EQUATION]] upon removal, followed by degradation slope and knee-point ratio as secondary signals. The proposed framework provides a practically deployable solution for battery management systems operating across heterogeneous fleets with minimal computational overhead and strong cross-dataset generalization capability.

---

## uid: `doi:10.2139/ssrn.6880480`

- title: MIVL: A Memory Integrity Verification Layer for Detecting and Mitigating Poisoning Attacks in Agentic AI Systems
- authors: Jigesh Sheoran
- affiliations: not stated
- posted: 2026-06-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6880480
- keyword hits: agentic, gemini

### abstract

Agentic AI systems that maintain persistent memory across sessions are vulnerable to memory poisoning attacks, in which adversaries plant malicious entries that silently alter long-term agent behaviour. Existing defences target single-turn prompt injection and do not address the persistence, gradual accumulation, or cross-agent propagation vectors that threaten multi-session agents. We present MIVL (Memory Integrity Verification Layer), a five-signal detection pipeline that computes a Memory Integrity Score (MIS) for every candidate memory write before it is committed. The five signals are: Semantic Intent Drift Detection (S1-SIDD), Command/Instruction Vocabulary Score (S2-CIVS), Temporal Drift Monitor (S3-TDM), Provenance Verification Score (S4-PVS), and Cross-Context Contradiction Ratio (S5-CCCR). A tiered remediation system routes flagged writes to one of five actions: BLOCK, QUARANTINE, SANITIZE, FLAG, or ROLLBACK. Evaluated on a labelled dataset of 200 memory write examples spanning four attack classes, MIVL achieves F1 = 0.8804, AUROC = 0.9023, and a false positive rate of 3.0% at the default threshold T M = 0.30. All five Gemini Memory Attack variants are successfully detected. The dataset and implementation are open-sourced.

---

## uid: `doi:10.2139/ssrn.6997566`

- title: MA-EASA: A Governance-First Multi-Agent Economic-Aware Slice Allocation Framework for Private 6G Industrial IoT Networks
- authors: Onur Sahin, Vanlin Sathya, Lyutianyang Zhang, Kalpana Naidu
- affiliations: not stated
- posted: 2026-06-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6997566
- keyword hits: agentic

### abstract

Private 6G industrial networks support services with vastly different operational importance, yet most slice-allocation approaches optimize technical metrics such as latency, throughput, and reliability without considering enterprise impact. Our work proposes MA-EASA (Multi-Agent Economic-Aware Slice Allocator), a governance-first multi-agent framework that allocates slice resources based on application criticality, service value, resource cost, and service-level constraints. MA-EASA combines bounded agents for state monitoring, criticality assessment, utility estimation, allocation, governance, and explanation, while enforcing protected-service guarantees before deployment. Using a reproducible simulation environment spanning smart-factory, smart-port, and airport scenarios, results show that MA-EASA achieves higher enterprise utility and fewer critical-service violations than KPI-centric and non-agentic economic baselines, demonstrating the potential of governance-aware multi-agent control for future private 6G networks.

---

## uid: `doi:10.2139/ssrn.6992481`

- title: Epeditor: A Scalable Platform for Large-ensemble Building Energy Simulation Enabling Agent-Assisted Automation
- authors: Jun Xiao, Qiong Wang, Hao Zhou, Yang Zhao, Borong Lin
- affiliations: not stated
- posted: 2026-06-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6992481
- keyword hits: ai agent

### abstract

The data scale of energy simulation keeps increasing, particularly in urban building energy modeling (UBEM) and uncertainty analysis, where thousands of EnergyPlus runs are often required to explore complex parameter spaces and building variability. To simplify these data-intensive workflows, recent studies have introduced AI agents for end-to-end simulation tasks. However, in practice, both AI-assisted and conventional batch workflows remain constrained by hallucination-induced search bias, inefficient large-ensemble simulation execution, and cumbersome data processing. To address these problems, this study introduces Epeditor, a cloud-deployable simulation infrastructure for large-ensemble building energy analysis for both AI and human users. It combines three improvements on current workflows: a knowledge-assisted parameterization with more accurate and stable field searching in IDF files; a simulator that improves parallel execution efficiency through Operation-System-Level deployment; and a data management system that enables memory-safe aggregation of large simulation input and outputs. The packaged Agent Skill allows AI agents to execute fully automated dataset generation, batch simulation, surrogate modeling, and interpretation through an auditable workflow. Epeditor is evaluated through a systematical agent benchmarks with metrics for Artificial General Intelligence, and two case studies were introduced to show the ability in research and design practices including an AI-assisted surrogate-modeling case, and design-studio practices. The pipeline exhibits 99.98% robustness in IDF generation, up to four-fold acceleration in high-parallel simulation, and 76.28 (F1) in IDF fields inference. These findings indicate that Epeditor can lower the technical and computational barriers of large-ensemble EnergyPlus simulation, supporting more accessible, reproducible, and AI-ready building energy analysis.

---

## uid: `arxiv:2606.26959v1`

- title: The Shift to Agentic AI: Evidence from Codex
- authors: Drew Johnston, David Holtz, Alex Martin Richmond, Christopher Ong, Prasanna Tambe, Aaron Chatterji
- affiliations: not stated
- posted: 2026-06-25
- source: arXiv
- link: https://arxiv.org/abs/2606.26959v1
- keyword hits: agentic, chatgpt

### abstract

We analyze usage data from OpenAI's Codex tool to present large-scale evidence of how agentic AI technology, which can take actions on a user's behalf, changes how people work. We use an automated, privacy-protecting pipeline to contrast usage across three populations: external personal-account users, external organizational-account users, and workers within OpenAI. We find that agentic AI usage is growing rapidly: the number of active users has grown more than fivefold in the first half of 2026, with the most rapid increase occurring outside the initial audience of software developers. Uptake is uneven: within OpenAI, Codex usage is nearly universal and has largely replaced business usage of ChatGPT. We document a similar shift to agentic tooling outside OpenAI, particularly within organizations, although external adoption remains lower and more uneven. In addition to headline usage figures, we observe measures of sophistication, and find that a growing number of users have used Codex to change their workflows substantially. More than 10% of users manage three or more concurrent Codex agents at some point each week and that 26.6% use skills, which allow users to share instructions for complex workflows. Alongside these changes in usage practices, request complexity has increased: since the start of the year, the share of individual Codex users who submit at least one request for a task estimated to require more than eight hours for an experienced human to complete has increased nearly tenfold. Concurrently, output has grown rapidly -- in June 2026, the median OpenAI employee in a legal role generated 13 times more monthly output tokens across Codex and ChatGPT than they did in November 2025, while the median researcher generated more than 50 times as many. We conclude by discussing the implications of these patterns for productivity, job reorganization, and workforce restructuring.

---

## uid: `arxiv:2606.26933v1`

- title: Chai: Agentic Discovery of Cryptographic Misuse Vulnerabilities
- authors: Corban Villa, Sohee Kim, Austin Chu, Alon Shakevsky, Raluca Ada Popa
- affiliations: not stated
- posted: 2026-06-25
- source: arXiv
- link: https://arxiv.org/abs/2606.26933v1
- keyword hits: agentic

### abstract

AI-assisted vulnerability discovery has proven effective for bug classes like memory safety, where instrumentation confirms memory violations and efficiently filters false positives. Many dangerous vulnerability classes, such as cryptographic misuse, however, lack any comparable instrumentation. In this work, we present Chai, an AI-based system that discovers and validates cryptographic misuse vulnerabilities through naturally occurring signals. To achieve this, Chai rethinks the classical technique of differential testing by leveraging AI to 1) improve precision for detecting real security issues in libraries, and 2) repurpose commonly overlooked discrepancies as leads for tangible vulnerabilities in downstream applications. In doing so, Chai inverts the prevailing paradigm of AI vulnerability discovery: instead of auditing one codebase for many flaws, it catalogs flaws at the library level and propagates them across a cryptographic dependency graph, delivering compounding efficiency gains. We evaluate Chai across X.509, JWT, and SAML libraries. Chai discovered a previously unknown critical vulnerability in an SSL library that powers billions of devices, along with security bugs in one library behind a major web browser and another in major Linux distributions. In total, these techniques surfaced over 100 vulnerabilities.

---

## uid: `doi:10.2139/ssrn.7002663`

- title: TokenCount: A Training-Free Framework for Object Counting by Interpreting Output Tokens
- authors: Min Woo Woo, Jun Ha Lee, Min Young Kim, Jae-Il Kim, Byeong Hak Kim
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7002663
- keyword hits: fine-tuning, foundation model

### abstract

Object counting is a critical computer vision task with widespread applications in manufacturing, traffic monitoring, and crowd analysis. Recent class-agnostic object counting methods leveraging the Segment Anything Model are limited by the inherent uncertainty of the similarity metric derived from its image encoder. While solutions incorporating additional encoders can refine this similarity, they face challenges due to high computational costs. To overcome this challenge, we propose a novel framework consisting of two critical components working in synergy with Segment Anything Model: a probabilistic prompt generation stage and an output token-based verification stage. The former efficiently generates prompts based on probability distributions from Segment Anything Model’s image embedding, while the latter utilizes Segment Anything Model’s output tokens to effectively distinguish between positive and negative instances. Experimental results demonstrate that our method achieves superior accuracy with an Mean Absolute Error of 16.25, outperforming existing training-based and training-free methods. Notably, on the Car Parking Lot dataset, our framework achieves superior performance, outperforming all supervised methods and demonstrating comparable results against training-free alternatives. Furthermore, we demonstrate the framework's versatility in industrial automation through rigorous testing on pharmaceutical and mechanical components from the Few-Shot Counting-147 dataset. Unlike supervised approaches that optimize parameters on specific samples, our model performs inference without prior exposure to the data distribution. Ultimately, this study showcases the significant potential of applying foundation models to specialized downstream tasks without the need for fine-tuning or auxiliary models.

---

## uid: `doi:10.2139/ssrn.6890342`

- title: GPU-aligned Deterministic Scaling in a Reversible Intelligence Substrate
- authors: Joseph Iko
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6890342
- keyword hits: transformer model

### abstract

The scaling of artificial intelligence architectures to accommodate extreme sequence lengths represents one of the most profound challenges in contemporary computational research. At the core of this challenge lies the fundamental incompatibility between the memory hierarchies of modern hardware accelerators and the mathematical requirements of standard sequence modeling paradigms. Contemporary sequence architectures, predominantly derived from the Transformer model, exhibit pathological memory bloat and experience catastrophic throughput degradation when tasked with processing millions of tokens. This systemic degradation stems inherently from the linear scaling of the required Key-Value (KV) cache memory footprint, coupled with the quadratic computational complexity inherent to dense token-to-token associative attention mechanisms. In this paper, we propose, define, and empirically evaluate a radical architectural departure: a reversible, block-wise intelligence substrate engineered exclusively for deterministic, perfectly flat scaling on graphical processing units (GPUs). By completely decoupling the dynamic memory footprint from the global sequence length and leveraging fixed-topology parallel reduction primitives, the proposed substrate maintains a strict memory complexity relative to the context size. The primary contribution of this research is the presentation of empirical results demonstrating highly stable, deterministic GPU throughput at unprecedented sequence lengths without revealing proprietary implementation details or core algorithmic update rules. In rigorously controlled evaluations, the substrate achieves a 131.75× operational speedup over optimized sequential CPU baselines at a 100-million-token sequence length, completing execution in exactly 0.0126 seconds. Furthermore, in a sustained 10-billion-token continuous streaming pass, the architecture maintains an entirely flat scaling profile, yielding an effective throughput exceeding 9.51 billion tokens per second. These results confirm that hardware-aligned reversible architectures can completely bypass the memory-bandwidth bottlenecks inherent to standard attention models, offering a scalable foundation for extreme-context sequence processing without algorithmic throughput degradation or non-deterministic statistical divergence.

---
