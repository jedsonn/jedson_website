# Classification batch 387 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-387.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6837953`

- title: Counter-Diplomacy as Communicative Strategy Indonesia’s Negotiation of Chinese Hegemony through Constrained Middle-Power Communication
- authors: Khoirunnisa Khoirunnisa, Jamalullail Jamalullail, Prasetya Yoga Santoso, Didi Jubaidi
- affiliations: not stated
- posted: 2026-05-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6837953
- keyword hits: prompting

### abstract

The rise of China has significantly reshaped the geopolitical landscape of Southeast Asia, prompting regional states to develop various strategies to navigate growing asymmetries of power. While existing studies often interpret these responses through material strategies such as balancing, bandwagoning, or hedging, relatively limited attention has been given to the role of diplomatic communication in negotiating hegemonic influence. This study examines how international communication functions as a strategic instrument in Indonesia’s counter-diplomacy toward China’s expanding regional influence. Drawing on a qualitative research design, the study employs discourse analysis of diplomatic statements, policy documents, and media narratives related to Indonesia–China relations between 2014 and 2024. The analysis explores how China’s hegemonic influence operates through symbolic, material, ideological, and institutional dimensions, and how Indonesia responds through strategic diplomatic communication. The findings show that China promotes narratives of development, connectivity, and shared prosperity to legitimize its regional leadership, particularly through initiatives such as the Belt and Road Initiative. In response, Indonesia articulates diplomatic narratives emphasizing ASEAN centrality, multilateral cooperation, and the principle of a free and active foreign policy. Rather than directly confronting China’s influence, Indonesia strategically frames its communication within regional institutional norms, allowing it to maintain constructive engagement while preserving strategic autonomy. Building on these findings, the article introduces the concept of constrained middle-power communication, which explains how semi-peripheral states negotiate hegemonic influence through diplomatic narratives and legitimacy management under conditions of asymmetric interdependence.

---

## uid: `doi:10.2139/ssrn.6839608`

- title: Harmonic Frequency Transformer with Fault Query Decoder: A Physics-Inspired Deep Learning Architecture for Bearing Fault Diagnosis in the Spectral Domain
- authors: Sebastian Avi&ntilde;a, Reyner  Iván Yparrea-Arreola, Manuel  Nazario Rocha-Martínez, Miguel García-Alvarado
- affiliations: not stated
- posted: 2026-05-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6839608
- keyword hits: fine-tuning

### abstract

Experienced maintenance engineers diagnose failure modes in rotating machineryby inspecting vibration spectra: faults in gears, shafts, imbalances, androlling element bearings each leave characteristic harmonic signatures in thefrequency domain that a trained analyst identifies by looking for energyconcentrated at fault-related frequencies and their integer multiples.Automating this process with deep learning is an open problem — existingarchitectures either learn spectral representations from scratch without anyharmonic prior, or apply generic transformers that capture long-rangedependencies without exploiting the multiplicative frequency arithmetic thatunderpins expert diagnosis.This paper proposes the *Harmonic Frequency Transformer with FaultQuery Decoder (HFT-FFD)*, a novel architecture that formalises the expertinspection process as two learnable structural components applicable to anyrotating machinery fault whose signature is harmonic in the frequency domain:(1)~a harmonic bias matrix H[i,j], added to multi-head attention logits,that initialises inter-patch attention weights from the known harmonicstructure of the target fault frequencies and refines them by backpropagation;and (2)~a DETR-style fault query decoder whose per-class cross-attentionweights produce interpretable frequency-band activation maps, directlyverifiable by a domain expert without post-hoc tools.Rolling element bearing diagnosis is used as the evaluation domain becauseit is a well-characterised problem with publicly available benchmark datasetsand analytically known fault frequencies (BPFO, BPFI), providing a rigoroustestbed for the proposed ideas. HFT-FFD is benchmarked against threearchitectures on the Paderborn University Bearing Dataset (64~kHz, 4 classes,159,078 segments), achieving 98.15% accuracy and macro F1 of 0.9825. In azero-shot cross-dataset evaluation on the HUST Bearing Dataset (51.2~kHz,different bearing geometries, no fine-tuning), the harmonic bias yields a+9.01~pp advantage over an otherwise identical transformer without theharmonic prior (48.48% vs. 39.47%), confirming that the architecturecaptures spectral regularities that generalise beyond the specific trainingdistribution.

---

## uid: `doi:10.2139/ssrn.6745619`

- title: Compositional Layer Pruning of Frozen Tabular Foundation Models When Single-Layer Importance Misleads, and What to Do About It
- authors: Agus Sudjianto, Aijun Zhang
- affiliations: not stated
- posted: 2026-05-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6745619
- keyword hits: foundation model, in-context learning

### abstract

Pruning frozen foundation models is typically driven by ranking layers according to a perlayer importance score and dropping the bottom-k. We document a failure mode of this approach for tabular in-context learning models. On TabICLv2 across ten OpenML binary classification benchmarks and five seeds (50 dataset-seed conditions), single-layer ablation rankings are highly consistent across datasets (Kendall's τ = 0.40, 95% bootstrap CI [+0.03, +0.73]), which would seem to validate the per-layer approach. But pairwise layer-drop interactions are large enough to falsify the submodularity assumption underlying greedy: the maximum pair interaction averages 3.74× the maximum single-layer drop and only 43% of pairs are subadditive. Two specific layers form a universal complementary pair whose pairwise interaction is positive on every one of the 50 conditions, and another layer plays a compositional compensator role detectable only in pair statistics. Per-layer scoring cannot see this structure. We propose a multi-diagnostic framework that exposes compositional layer importance through four cheap measurements: per-layer ablation across a calibration suite, downstream-projected residual energy D ℓ = E∥J ℓ+1 F ℓ ∥ 2 supported by a first-order Taylor bound, pairwise drop interactions C ij and L 1-penalized soft gates that learn joint sparsity. On TabICLv2 the four converge on a load-bearing core, a drop-first set and a task-dependent middle. End-to-end validation with short knowledge distillation: the consensus prescription matches teacher accuracy on 9 of 10 datasets at 3 dropped layers, with mean KL divergence to the teacher (0.004) lower than any per-layer baseline at the same compression level. Naive greedy single-layer pruning at 5 drops is catastrophic (16× higher KL) because it breaks the universal complementary pair, direct evidence that consistent single-layer rankings are unsafe as a multi-layer pruning primitive.

---

## uid: `doi:10.2139/ssrn.6786758`

- title: The Cognitive Impact of AI on Organisational Decision-Making: Why Human Readiness Is the Missing Layer in AI Governance
- authors: Julie Hendry
- affiliations: not stated
- posted: 2026-05-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6786758
- keyword hits: agentic

### abstract

The EU AI Act (Regulation 2024/1689), enforceable from 2 August 2026, places human oversight at the centre of AI governance for high-risk systems. Yet converging evidence from cognitive psychology, human factors engineering, organisational behaviour, and neuroscience demonstrates that human oversight as currently conceived is psychologically untenable in most operational contexts. Recent work by Acemoglu et al. (2026) introduces the concept of "knowledge collapse," arguing that agentic AI substitutes for human cognitive effort, reducing learning incentives and eroding collective knowledge, potentially irreversibly. This narrative review synthesises research across five thematic domains: the cognitive effects of working alongside AI (including deskilling and cognitive offloading), the architecture of human-AI decisionmaking, organisational conditions for honest self-assessment, the psychology of AIdriven workforce transition, and structural accountability gaps in human-AI systems. No existing AI maturity or governance framework systematically assesses the cognitive, psychological, and organisational readiness of the humans expected to exercise oversight. Existing human-centred AI maturity models (e.g., Winby & Xu, 2025) assess whether AI is designed and deployed in human-centred ways, but do not measure what AI does to human cognition. The paper presents an early practical assessment tool developed to measure individual cognitive impact of technology, and argues that organisational AI readiness assessment must begin with the human, not the technical system.

---

## uid: `doi:10.2139/ssrn.6783978`

- title: Runtime Governance for Agentic AI: Action-Boundary Control with Trusted Provenance and Fail-Closed Execution
- authors: Adam Mazzocchetti
- affiliations: not stated
- posted: 2026-05-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6783978
- keyword hits: agentic

### abstract

Agentic AI systems request tool actions that can modify files, send messages, launch jobs, or change workflow state. This shifts the safety problem from harmful text generation to harmful operational side effects. Prompt-level governance can shape model behavior, but it does not create an execution boundary. We introduce Aegis, a runtime governance system that treats model outputs as action proposals and mediates them through a trusted decision layer before tool execution. The model proposes; the trusted runtime decides. Aegis evaluates proposals against active policy state, resolves provenance server-side, fails closed under uncertainty, and routes selected cases through Senate-style settlement, a quorumbased non-unilateral authorization path. We evaluate Aegis on a repeated sandbox corpus spanning five run families, 42 tasks, three conditions, and ten repeats per family. Across 6,300 rows, prompt-policy conditioning produced 79 risky comparator-path leakage rows. Across 2,100 Aegis-governed rows, the system recorded zero governed mock-tool applications and zero governed risky side-effect completions. All 1,832 Aegis-attempted governed rows preserved trusted Aegis-resolved provenance, and all 1,019 Senate-settled rows had quorum and final signed tally evidence. These results do not prove general autonomous-agent safety. They support the narrower systems claim that, in this evaluated sandbox corpus, runtime action-boundary governance prevented observed risky proposals from becoming governed side effects.

---

## uid: `doi:10.2139/ssrn.6844785`

- title: Engineering Queryable Industrial Product Knowledge Bases from Technical Documents: A Survey of Data, Knowledge, and Retrieval Pipelines
- authors: Muzakkiruddin Ahmed Mohammed, Mert Can Cakmak, John R. Talburt
- affiliations: not stated
- posted: 2026-05-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6844785
- keyword hits: retrieval-augmented

### abstract

Industrial product documentation, including catalogs, datasheets, selection guides, and specification sheets, contains essential technical knowledge for procurement, engineering design, maintenance, and supply-chain operations. Much of this information, however, remains locked in PDFs designed for human reading rather than machine interpretation. This survey reviews the end-to-end pipeline for transforming industrial documents into queryable product knowledge bases. We synthesize 189 works published between 2015 and 2025 across document parsing, information extraction, knowledge base engineering, retrieval-augmented querying, and local deployment. The review shows that although OCR systems, document vision-language models, table parsers, vector databases, and RAG frameworks have matured, their integration for industrial product documentation remains weakly validated. We identify a maturity inversion: several components are deployable or near-deployable, whereas end-to-end industrial pipelines remain at an early readiness level. The survey highlights seven critical gaps involving industrial benchmarks, end-to-end evaluation, dense table extraction, cross-manufacturer schema variation, specification value parsing, multi-path retrieval, and local deployment validation. We argue that the central challenge is the engineering of trustworthy product knowledge bases through schema-aware extraction, value normalization, provenance-preserving storage, data-quality control, and hybrid query routing across SQL, lexical, vector, and graph retrieval. The paper concludes with a prioritized research agenda for reliable, auditable, and maintainable industrial product knowledge infrastructure.

---

## uid: `doi:10.2139/ssrn.6848034`

- title: Low-Cost LoRA Fine-Tuning of Small Language Models for Multi-Step Arithmetic Reasoning ​
- authors: Jake O&apos;Grady, Effirul I. Ramlan
- affiliations: not stated
- posted: 2026-05-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6848034
- keyword hits: fine-tuning, qwen

### abstract

Small language models (SLMs) often struggle with multi-step arithmetic reasoning. Using GSM8K as a source dataset, we generated a 21,250-example corpus of grade-school arithmetic word-problem variants combining natural-language solution traces, lightweight Socratic-style cues, structural variation, and irrelevant distractor context. We then fine-tuned Qwen3-0.6B and Qwen3-1.7B models with LoRA on a consumer-hardware setup. Exact-match accuracy on GSM8K improved from 36.5% to 49.1% for Qwen3-0.6B and from 53.5% to 66.5% for Qwen3- 1.7B. Transfer to related arithmetic benchmarks was strongest for Qwen3-1.7B, reaching 98.9% on MultiArith and 73.0% on SVAMP, compared with 54.4% and 45.3% for the base model. These results show that low-cost synthetic data generation and parameter-efficient fine-tuning can provide meaningful arithmetic gains in SLMs. The findings support structured synthetic data design, including natural-language solution traces and lightweight Socratic-style cues, as a viable adaptation strategy for arithmetic fine-tuning under consumer-hardware constraints. ​

---

## uid: `arxiv:2606.00143v1`

- title: Regime-Adaptive Continual Learning for Portfolio Management
- authors: Chaofan Pan, Lingfei Ren, Linbo Xiong, Yonghao Li, Wei Wei, Xin Yang
- affiliations: not stated
- posted: 2026-05-29
- source: arXiv
- link: https://arxiv.org/abs/2606.00143v1
- keyword hits: fine-tuning

### abstract

Financial markets are inherently non-stationary, exhibiting frequent regime shifts and structural changes that render traditional Portfolio Management (PM) approaches ineffective. Existing remedies, such as rolling-window retraining and naive online fine-tuning, are hindered by high computational costs and insufficient knowledge utilization, respectively, resulting in low returns and limited adaptability. Continual learning (CL) offers a promising paradigm by enabling trading agents to accumulate and transfer knowledge across sequential tasks. In this paper, we propose \textbf{Re}gime-aware \textbf{C}ontinual \textbf{A}daptive \textbf{P}ortfolio management (\textbf{ReCAP}), a novel framework that integrates CL into PM to address the challenges of dynamic financial environments. ReCAP employs an adaptive regime detection module to segment historical market data into variable-length regimes, enabling regime-specific learning of policy vectors and the construction of a policy library. During continual trading, a regime-gate module adaptively combines policy vectors from the library based on the current market state, facilitating rapid adaptation to newly detected regimes. Only the regime-gate and the current regime's policy vector are continually updated to preserve useful knowledge effectively. Extensive experiments on five real-world datasets demonstrate that ReCAP consistently outperforms popular baselines, achieving superior returns in long-term investment horizons and rapid adaptation to regime shifts.

---
