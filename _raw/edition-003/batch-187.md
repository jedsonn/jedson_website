# Classification batch 187 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-187.answer.json` as a JSON array.

---

## uid: `arxiv:2607.16372v1`

- title: AoA: Theorem Proving Agent over Abstract Syntax Tree of Redesigned Language
- authors: Qiyuan Xu, Joshua Ong Jun Leang, Renxi Wang, Wenda Li, Haonan Li, Luke Ong, Conrad Watt
- affiliations: not stated
- posted: 2026-07-17
- source: arXiv
- link: https://arxiv.org/abs/2607.16372v1
- keyword hits: llm, llms

### abstract

Interactive theorem proving (ITP) underpins program verification and formalized mathematics, but its manual effort limits scalability. LLM-based proof agents promise to ease this effort, but their heavy token consumption and API cost remain a major obstacle. We trace this cost to a shared root: current agents operate on serialized concrete syntax, emitting proofs as source text and recovering proof states through separate, line-number-based queries, so every edit shifts later lines and forces repeated relocation of errors and states. This same dependence on concrete syntax also blocks adoption of Minilang, a recent proof language that reaches SOTA on LLM-based proving but is too new for LLMs' training corpora. We address both problems by lifting the agent off source text and onto the abstract syntax tree (AST): the model supplies proofs as JSON representations of Minilang's AST -- native to tool-calling LLMs -- and drives the prover through a tree-edit model that fuses proof operations and states into one proof tree, so each operation carries its own subgoal's state, readable directly off the tree. We realize this design in \emph{Agent over AST} (AoA). Against Amazon's Isabelle Agent on miniF2F and NTP4VC-Pearl common success sets, AoA cuts API cost by 2.3--4.7x (normalized input-cache accounting), uses 2.9--6.9x fewer tokens and 3.9--8.9x fewer tool calls, and finishes 1.4--2.0x faster -- while also solving far more problems on the harder verification benchmark.

---

## uid: `arxiv:2607.15557v3`

- title: SkillCorpus: Consolidating and Evaluating the Open Skill Ecosystem for Real-World LLM Agents
- authors: Yanze Wang, Pengfei Yao, Tianyi Sun, Chuanrui Hu, Yan Xiao, Yunyun Han, Jun Sun, Yafeng Deng
- affiliations: not stated
- posted: 2026-07-17
- source: arXiv
- link: https://arxiv.org/abs/2607.15557v3
- keyword hits: llm, qwen

### abstract

Agent skills, SKILL files that package reusable procedural knowledge for an LLM agent, are a popular mechanism for extending agent capabilities. Public repositories now host them in large and growing numbers, yet these artifacts are fragmented, redundant, and uneven in quality, and their value in practice is unclear. A core question remains open, namely how to consolidate this open-source SKILL ecosystem into a single usable corpus, and what bounds its benefit on real-world agent tasks. We present SkillCorpus, a framework that aggregates, curates, matches, and evaluates the open skill ecosystem at scale. It filters ~821,000 crawled skills through a multi-stage pipeline into 96,401 skills organised by a 16-class taxonomy and three quality facets (utility, robustness, safety), and pairs them with a fine-tuned retrieval-and-selection stack that matches task-relevant skills. We evaluate end-to-end across three benchmarks (SkillsBench, GDPVal, QwenClawBench), two harnesses, and two open backbones with a frontier robustness check. Integrating SkillCorpus yields consistent gains across all three benchmarks, largest on SkillsBench (+7.5 pp). An operational analysis traces the gains to a coverage boundary and a harness boundary. SkillCorpus is, to our knowledge, the first end-to-end account of when a curated, retrieval-served community corpus improves real agent tasks, and where it does not. The dataset, models, and code will be released upon acceptance.

---

## uid: `doi:10.2139/ssrn.7007544`

- title: Deepfakes And Identity Appropriation: Re-Examining The Limits Of Indian Criminal Law In The Age Of Generative Ai
- authors: Nandini Reddy Kunduru
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7007544
- keyword hits: generative ai, generative artificial intelligence

### abstract

Rapid advances in generative artificial intelligence have enabled the creation of highly realistic synthetic videos, audio, and images capable of imitating a person's face, voice, and likeness without consent. 1 Public discussions on deepfakes are usually about misinformation, but this paper argues the fundamental legal problem lies elsewhere: Indian criminal law which treats deepfakes as wrongful only when they produce a separate recognisable harm such as fraud, defamation, or fabricated evidence rather than recognising it as the theft of identity of an individual as an independently wrongful act. Drawing on recent Indian incidents which include Rashmika Mandanna deepfake controversy 2 , deepfake-enabled investment scams impersonating executives associated with Bombay Stock Exchange (BSE) 3 , and AI-generated political content circulated during the Tamil Nadu Assembly Election 2026, this paper examines the Information Technology Act, 2000, Bharatiya Nyaya Sanhita, 2023, and Digital Personal Data Protection Act, 2023, and finds that each statute applies only after a downstream consequence occurs. The paper then discusses Indian personality rights law, which recognises that using someone's identity without consent is independently illegal and can be enforced through civil courts. It argues that this principle should also be applied in criminal law, not just civil law. The paper further recommends creating a new law that specifically criminalises the non-consensual use of digitally created or synthetic versions of a person's identity such as deepfakes. Overall, the paper suggests that Indian law should shift from a reactive approach in which action is taken only after harm occurs to a preventive approach where unauthorized use of identity itself is treated as an offence. This paper's novel contribution lies in reframing deepfake regulation in India from a consequence-based harm model to an identity-based appropriation model, arguing that unauthorised digital replication itself should be treated as the primary criminal wrong.

---

## uid: `arxiv:2607.16716v1`

- title: RECON: Benchmarking Agent Memory for Compositional Reasoning over Long Contexts
- authors: Mihir Shriniwas Arya
- affiliations: not stated
- posted: 2026-07-18
- source: arXiv
- link: https://arxiv.org/abs/2607.16716v1
- keyword hits: large language model, large language models, llm

### abstract

Large language models and LLM-based agents are widely used as personal chat assistants, enterprise copilots, and autonomous workflow agents. In all these applications, memory (the ability to retain, access, and reason over information accumulated over long contexts and multiple interactions) plays a crucial role in determining the reliability of any agent. We introduce RECON (Reasoning over Extended Contexts with Obfuscated Narratives), a benchmark for evaluating compositional reasoning over long contexts. RECON spans 24 case files across three domains (criminal, medical, and financial), each ranging from 50k to 100k tokens, and tests agents on six memory intensive tasks: reconstructing multi-hop evidence chains, propagating cascading invalidations, resolving source conflicts, counterfactual reasoning, satisfying temporal constraints, and temporal fact retrieval. Recent memory benchmarks evaluate whether agents can retrieve scattered facts or detect if a fact has changed whereas RECON evaluates what happens after the change, whether agents can trace which downstream conclusions are affected, which survive through independent support, and how alternative timelines would have unfolded. Our evaluation reveals substantial limitations across current architectures: even the strongest non-Oracle system reaches only 22.4% Accuracy, with retrieval and reasoning each surfacing as challenges.

---

## uid: `doi:10.2139/ssrn.7014038`

- title: WindCMA：Lightweight LLM-based Multivariate SCADA Forecasting for Offshore Wind Turbine Gearbox
- authors: Yaohua Guo, Renshen Tan, Xiaowei Zhou, Peiyi Zhu, Khalil AL-Bukhaiti, Anping Wan, Xiaomin Cheng, Xiaosheng Ji
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7014038
- keyword hits: large language model, llm

### abstract

To address the problems of delayed early warning and low prediction accuracy caused by the complex environment of real-world offshore wind farms, the scarcity of gearbox fault samples, and limited edge computing resources, this paper proposes an offshore wind turbine gearbox state evolution prediction method that integrates Wavelet Packet Transform (WPT), SPCC-RF feature selection, a lightweight Large Language Model (LLM), and Dual-stream Cross-Modal Fusion. First, the method employs the Random Forest (RF) algorithm and the Pearson Correlation Coefficient (PCC) to analyze the feature importance of multi-dimensional Supervisory Control and Data Acquisition (SCADA) data from wind turbines, filtering out key feature variables correlated with gearbox oil temperature to achieve dimensionality reduction. Subsequently, the Wavelet Packet Transform is utilized to denoise the selected multi-dimensional feature sequences, thereby enhancing data quality. Breaking through the limitations of traditional time-series prediction models that rely solely on numerical features, this method innovatively introduces a lightweight LLM as a prior knowledge base. By constructing a Dual-stream Cross-Modal Fusion mechanism, multi-dimensional SCADA time-series data patches are mapped into the semantic space, achieving a deep representational fusion of industrial-grade text prompts and sensor signals. Experimental results demonstrate that the proposed method effectively improves the prediction accuracy of gearbox oil temperature. Possessing robust generalization capabilities and practical engineering value, this approach provides powerful technical support for the predictive health management (PHM) of wind turbines.

---

## uid: `doi:10.2139/ssrn.7123240`

- title: Faking Resistance of Forced-Choice and Single-Statement Personality Measures: Stress-Testing With Humans and Generative AI
- authors: Chet Robie, Justin Feeney, Sabah Rasheed, Joshua S. Bourdage, Neil Christiansen, Patrick  D. Dunlop, Kabir Daljeet
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7123240
- keyword hits: generative ai, generative artificial intelligence

### abstract

A major concern with personality assessment in high‐stakes settings is test‐takers misrepresenting (“faking”) their personalities. Although test developers have adopted difficult‐to‐fake forced‐choice (FC) formats, generative artificial intelligence (AI) now offers test‐ takers a highly sophisticated “test‐coach,” and yet it is unclear how resilient FC formats are to faking by AI‐generated response sets. This investigation examined the faking resistance of single‐statement (SS), forced‐choice IRT (FC‐IRT), and forced‐choice CTT (FC‐CTT) versions of the HEXACO inventory. 219 Accounting/Finance professionals completed the three assessments under honest and applicant conditions, the latter for a role where Honesty‐Humility and Conscientiousness were target traits. Three frontier AI models were repeatedly prompted with analogous instructions to simulate AI‐assisted faking. We found that two AI models consistently outscored human test‐takers under applicant conditions across all formats. Among the human‐generated responses, the FC‐CTT format showed less inflation than FC‐IRT for Honesty‐Humility and better rank‐order stability in applicant conditions, but this pattern did not extend to Conscientiousness. Neither FC format demonstrated clear improvements in convergent or criterion‐related validity. Findings challenge the previous assumption that FC measurement approaches can fully mitigate human‐ or AI‐assisted faking.

---

## uid: `doi:10.2139/ssrn.7147562`

- title: The Persuasion-Prediction Gap: Outcome-Grounded Auditing of LLM Judges on Market Resolved Financial and Crypto Reasoning
- authors: VASFI TATAROGLU, HASAN KURBAN
- affiliations: not stated
- posted: 2026-07-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7147562
- keyword hits: gemini, llm

### abstract

LLM-as-a-judge now underpins evaluation and decision-support pipelines, yet judges are validated against human preferences or other models, never against whether the scored reasoning was right. Both anchors reward fluent, confident rationales. We audit judges where the outcome itself supplies the label. OG-JUDGE, a label-free benchmark, pairs reasoning traces about future, market-resolved financial and cryptocurrency events with their realized outcomes: one eventually-correct and one eventually-wrong rationale per event. Two diagnostics score judges: Outcome-Discrimination Accuracy (ODA) and the Persuasion-Prediction Gap (PPG), which splits preference into persuasion and outcome channels; an identification result shows why ODA alone cannot measure judge quality. On 350 contamination-controlled events, four judges from three providers detect injected verifiable defects at 0.94 to 0.99 accuracy yet prefer the eventually-correct rationale at only 0.46 to 0.50, at or below chance and far short of a Bayes ceiling of 0.706. Outcome share of preference is near zero for every judge; one (Gemini 2.5 Flash) has a significantly negative persuasion-adjusted outcome coefficient. PPG is positive wherever reliably estimable, largest in the high-narrative crypto subdomain. Neither reasoning modes nor four outcome-agnostic mitigations restore outcome discrimination: judges reward rationales that sound right over rationales that are right. Code, data, and protocol: https://github.com/KurbanIntelligenceLab/llm-judge-finance-audit.

---

## uid: `arxiv:2607.17917v1`

- title: PEARL: Auditable Repair for Scientific Reasoning Graph Extraction
- authors: Bohan Su, Pengze Li, Yuchen Lu, Xi Chen
- affiliations: not stated
- posted: 2026-07-20
- source: arXiv
- link: https://arxiv.org/abs/2607.17917v1
- keyword hits: llm, llms

### abstract

Scientific Reasoning Graph Extraction (SRGE) aims to recover explicit links among observations, evidence, intermediate claims, and paper-level conclusions. LLMs can produce graph-like scientific explanations, but their outputs often mix malformed syntax, drifting edge labels, incorrectly oriented roots, and weak source anchors. We propose PEARL (Peircean Extraction via Abstraction and Repair Layer), a training-free framework that turns noisy LLM graph responses into auditable reasoning graphs and repairs them toward strict semantic validity. PEARL first materializes explicit graph content under a closed Peircean schema, then uses matched evidence-grounded judge feedback to repair rejected edge types, local inference steps, and terminal roots while preserving an audit trail. On five 70-paper model archives from ARCHE, a benchmark for latent reasoning-chain extraction, PEARL raises strict gate passes from 0/350 for the LLM baseline to 300/350, with average REA improving from 0.339 to 0.906. The graphs provide a reliability layer for research-agent and AI scientist workflows that need inspectable reasoning traces rather than unconstrained graph regeneration. Code and audit artifacts are available at https://github.com/BohanSu/auditable-repair-reasoning-graphs/tree/300-350_workshop .

---
