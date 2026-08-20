# Classification batch 12 of 22, edition 21

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-021/batch-12.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7294111`

- title: Capability-Boundary-Aware Memory Routing for Cost-Efficient Log Anomaly Detection
- authors: chao wang, Hongwei Zhou, Yucheng Zhang, Hao Hu, Jinhui Yuan
- affiliations: not stated
- posted: 2026-08-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7294111
- keyword hits: large language model, large language models, llm, llms

### abstract

Context: Log anomaly detection is essential for ensuring the reliable operation of softwaresystems. However, existing lightweight models remain fragile under complex log patterns anddistribution shifts, while directly employing large language models (LLMs) incurs high inference costs and latency.Objective: This paper aims to design a log anomaly detection framework that balances detection performance and inference efficiency, enabling a small language model (SLM) to efficiently handle the majority of samples while leveraging an LLM for auxiliary inference when necessary.Method: We propose CAMELog, a capability-boundary-aware memory routing frameworkfor cost-efficient log anomaly detection. CAMELog jointly characterizes the normal affinity,anomaly affinity, and novelty of each sample in a ternary deviation space, explicitly modelingthe reliable processing boundary of the SLM. Samples falling outside the SLM’s clear capabilityregion are routed to the LLM, whereas a memory-augmented reclaim mechanism conservatively returns borderline samples to the SLM when strong historical evidence exists. CAMELog further exploits error-case memory and example memory to construct prompt context, enhancing the LLM’s judgment on hard samples.Results: Experiments on three real-world log datasets, namely BGL, Thunderbird, and HDFS,show that, compared with the strongest baseline on each dataset, CAMELog improves F1-score by 10.2%, 8.9%, and 7.2%, respectively, while substantially reducing the LLM call ratio and token consumption, achieving a more favorable trade-off between detection effectiveness and inference cost.Conclusion: CAMELog offers a practical collaborative inference solution for large-scale loganomaly detection, preserving detection performance while effectively reducing reliance oncostly LLM inference.

---

## uid: `doi:10.2139/ssrn.7292749`

- title: OQTOPUS: Optimal Query-Time Optimization for Probabilistic Utility Search inLarge Language Model Reasoning Trees — A Controlled Branching ProcessFramework with Phase-Transition Guarantees
- authors: Soumyapriya Goswami, Raj  Ganesh Jayaraman, Partha  Sarathi Banerjee, Amruutha Chandrasekar Rao
- affiliations: not stated
- posted: 2026-08-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7292749
- keyword hits: large language model, large language models, llm, llms

### abstract

Inference-time reasoning in Large Language Models (LLMs) is increasingly implemented through tree-based exploration of in-termediate reasoning trajectories. Existing reasoning frameworks typically determine branching factor, search depth, beam width,and stopping policies through empirical tuning, lacking a principled theoretical foundation for compute allocation. This paper intro-duces OQTOPUS (Optimal Query-Time Optimization for Probabilistic Utility Search), an operations-research-inspired frameworkthat formulates inference-time reasoning as a finite-horizon Markov Decision Process (MDP). The proposed Controlled BranchingProcess with Absorbing Reward States (CBPARS) models each reasoning state using search depth, branching width, confidencescore, verifier reliability, and remaining computational budget.By embedding a Galton–Watson branching process into the decision framework, we derive a sharp phase-transition characterizedby the effective reasoning indexR= bpv,where b denotes branching factor, p is the probability of generating a useful reasoning continuation, and v represents verifieraccuracy. The analysis establishes closed-form bounds on the minimum computational budget required to attain a desired reasoningsuccess probability and rigorously characterizes diminishing returns beyond the critical compute threshold. Furthermore, we derivean adaptive branching policy together with an optimal stopping strategy that jointly maximize expected reasoning utility whileminimizing computational expenditure.Extensive simulation studies over 10,000 reasoning trajectories validate the theoretical analysis, demonstrating excellent agree-ment between theory and empirical performance. The results further indicate that several state-of-the-art reasoning systems allocatesubstantially more inference compute than required by the theoretical optimum, suggesting significant opportunities for principledcompute-efficient reasoning.

---

## uid: `doi:10.2139/ssrn.7295519`

- title: Passive Acoustic Monitoring for Iberian Orca Conservation and Maritime Safety: Managed Coexistence in the Strait of Gibraltar
- authors: Hans J Scholl
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7295519
- keyword hits: chatgpt, claude, gemini

### abstract

The Iberian orca subpopulation (Orcinus orca) is Critically Endangered, with approximately 40 individuals exposed to cumulative anthropogenic pressures. Since May 2020, some individuals within this subpopulation have repeatedly interacted with sailing vessels in the western Strait of Gibraltar and Gulf of Cádiz, causing seven confirmed vessel sinkings through October 2025 but no human fatalities to date. Existing information systems including citizen-science reporting, traffic-light risk maps, official monitoring, and research campaigns remain valuable but discontinuous, reactive, and fragmented across institutional boundaries. This policy perspective argues that continuous passive acoustic monitoring (PAM), implemented through a phased edge-AI network in the Strait, could provide the missing independent detection layer needed for both orca conservation and maritime safety. Rather than treating these aims as competing priorities, the article frames PAM as shared infrastructure: A basis for behavioral monitoring, non-invasive data collection, vessel-targeted risk awareness, and a cross-jurisdictional Common Operating Picture. The required hardware and edge-AI architecture are already available, but operational warning use would require Iberian-orca-specific model validation, local propagation testing, regulatory approval, and staged field trials. The central challenge is therefore not only technical but institutional: building a governance framework that integrates marine scientists, public authorities, sailors, fishermen, whale-watch operators, and conservation stakeholders into a common system for managed coexistence. AI Use Disclosure: During preparation and editing the author used Claude (Anthropic) as a writing assistant on some portions of this manuscript. Gemini (Google) and ChatGPT (OpenAI) were used for post-completion fact and consistency checking. All intellectual content, arguments, and conclusions were developed by the author.

---

## uid: `doi:10.2139/ssrn.7269600`

- title: What Is Understanding? Toward a Theory of Understanding as the Reorganization of Knowledge Relations
- authors: Akira Funabiki
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7269600
- keyword hits: large language model, large language models, llm, llms

### abstract

This study proposes a theoretical model of understanding based on the idea that understanding is the reorganization of relationships among knowledge . Rather than treating understanding as the acquisition of information, the study conceptualizes it as a dynamic cognitive process in which questions initiate reasoning, reasoning reorganizes knowledge structures, and newly formed understanding transforms worldviews and values. These updated values, in turn, generate new questions, forming a recursive cycle of understanding and self-updating. Based on this model, the study examines its implications for education and large language models (LLMs). Education is reconceptualized not as knowledge transmission but as the cultivation of learners who can continuously generate questions, revise their understanding, and update their values. LLMs, meanwhile, are positioned not as autonomous understanding subjects but as intellectual systems that support human reasoning and the reorganization of knowledge relationships. The study therefore proposes understanding as a self-updating cognitive cycle and identifies the human as an understanding subject who continuously generates new understanding through questioning, reasoning, and value updating.

---

## uid: `doi:10.2139/ssrn.7278638`

- title: AI and the Doctrine of Speakerless Speech
- authors: Margot E. Kaminski, Andrew D. Selbst
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7278638
- keyword hits: generative ai, generative artificial intelligence, large language model, large language models

### abstract

What makes speech “speech” for purposes of the First Amendment? Although the Supreme Court has developed elaborate doctrines governing when speech may be regulated, it has never squarely confronted a more fundamental question: whether constitutional speech requires the existence of a human speaker. That question has become unavoidable with the rise of generative artificial intelligence. Large language models routinely produce text, images, and videos that resemble ordinary expression while lacking any obvious connection to a human communicative act. The resulting debate has focused mostly on whether these outputs should receive First Amendment protection. This Article argues that the prior question is one of constitutional coverage. This Article identifies and reconstructs what we call the doctrine of speakerless speech—a previously unrecognized strand of First Amendment doctrine that becomes visible once courts confront expression lacking a connection to a human speaker. Examining the First Amendment’s coverage doctrine alongside Citizens United v. FEC, Moody v. NetChoice , and related cases, we show that disputes over corporations, algorithmic curation, expressive conduct, and now generative AI all confront the same underlying constitutional problem: if expression appears without a connection to a human speaker, what makes it speech for First Amendment purposes? Read together, these cases reveal that the Court has increasingly understood First Amendment coverage to turn not simply on the presence of words, images, or familiar expressive media, but on their connection to human communicative intent. This account changes the terms of the debate over AI and the First Amendment. Existing scholarship has divided over whether AI outputs should receive First Amendment coverage. Some scholars argue that outputs resembling traditional speech should be categorically covered; others contend that machine-generated outputs cannot be speech because machines neither speak nor possess constitutional rights. We argue that both approaches miss the central doctrinal development. The Supreme Court’s recent cases neither compel categorical protection nor categorical exclusion. Instead, they point toward a factual inquiry into the relationship between a particular AI output and a human’s intent to communicate. The Article makes three contributions. First, it identifies and reconstructs the doctrine of speakerless speech across cases that have never before been understood as part of a common body of law. Second, it offers the first sustained account of Moody v. NetChoice as a foundational decision about the constitutional boundaries of speech itself, rather than merely a case about social media platforms. Third, it provides a framework for evaluating the growing body of litigation involving generative AI and other algorithmic systems, showing why constitutional protection should turn on the nexus between AI outputs and human expressive intent rather than on categorical assumptions about either machines or media. In doing so, the Article offers a unified account of First Amendment coverage at precisely the moment that artificial intelligence has made the concept of a human speaker no longer inevitable.

---

## uid: `doi:10.2139/ssrn.7278438`

- title: Before "How to Use It": Locating Generative AI in the Teaching-Learning Structure
- authors: Meng-Han Lee, Feng-Jihu Lee
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7278438
- keyword hits: generative ai, large language model, large language models

### abstract

The debate over generative AI in education has oscillated between prohibition and instruction, in some jurisdictions more than once. Recent work traces this instability to a prior question about educational aims; what remains unspecified is the relocation that would make these concerns instances of one problem. Large language models can substitute not merely for tasks but for the processes that form capabilities: where an activity is constitutive of a capability, substituting for it substitutes for part of that formation. This yields an operational criterion for the individual use: does what the system returns still leave the learner a seam to cross before it becomes a solution to their problem? Because the same system affords both seam-closing and seam-preserving use, "AI use" cannot be the unit of educational judgment. Read through Kant's four stages of education, the displacement hollows cultivation's productive dimension, leaving load-bearing the capacity by which a learner answers for what they produce; in Freire's terms, narrowing the affordance to substitution alone hinders self-affirmation as a responsible person-and someone does the narrowing. The paper prescribes no method. It supplies a criterion for judging a particular use, and the coordinate on which positions now in circulation can be compared.

---

## uid: `arxiv:2608.16447v1`

- title: HaReCAP: Habitual-action Grounding for Recursive Large Language Model Agents
- authors: Shen Liu, Zhenguo Xu, Shaopu Wang, Yike Gao, Chunlei Wang
- affiliations: not stated
- posted: 2026-08-17
- source: arXiv
- link: https://arxiv.org/abs/2608.16447v1
- keyword hits: large language model, llm, qwen

### abstract

Long-horizon embodied tasks require LLM agents to iteratively decompose high-level goals, revise plans in response to environmental feedback, and ground leaf-level subgoals into valid executable actions. Recursive context-management methods such as ReCAP improve planning stability through multi-level task decomposition and parent-node refinement, but still repeatedly invoke the LLM at leaf nodes to ground atomic subtasks into exact valid actions. We refer to this final grounding step as last-mile grounding redundancy, which accumulates into substantial LLM-call and token overhead during long-horizon execution. To mitigate this issue, we propose HaReCAP (Habitual-action Grounded ReCAP), a low-intrusion leaf grounding extension for ReCAP. HaReCAP extracts frequent leaf decisions from successful trajectories and compiles them offline into auditable and abstainable one-step leaf-reflex rules. At runtime, it skips the leaf LLM call only when a rule can uniquely determine a legal action in the current valid-action set; otherwise, it falls back to the original ReCAP. This design avoids repeatedly carrying the full recursive context into the LLM for routine leaf action grounding, while preserving the original recursive control flow. We evaluate HaReCAP on Robotouille and ALFWorld with Qwen3.5-27B as the main model. On tasks solved by both ReCAP and HaReCAP, HaReCAP reduces token consumption by 14.67%, 17.93%, and 20.08% on Robotouille synchronous, Robotouille asynchronous, and ALFWorld, respectively. The results show that HaReCAP can serve as a low-intrusion extension to ReCAP-style recursive context-management frameworks, reducing last-mile grounding redundancy across environments and models on commonly successful trajectories.

---

## uid: `doi:10.2139/ssrn.7294618`

- title: The C2S Reliability Framework
- authors: Sheyene Gerardi
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7294618
- keyword hits: foundation model, large language model, large language models

### abstract

security, healthcare, finance, and public administration. As these systems assume increasingly consequential advisory roles, the central challenge is no longer computational capability alone, but institutional trust. Decisions affecting human lives, national security, and strategic infrastructure require analytical systems that are not only accurate, but also transparent, explainable, and scientifically accountable. This monograph introduces the C2S Reliability Framework , a conceptual model proposing that causal artificial intelligence can strengthen personnel reliability in high-consequence domains by supporting—rather than replacing—human institutional judgment. Building upon the principles established in SynsID and The Survival Blueprint , the framework argues that artificial intelligence should function as an evidence-integration system capable of organizing complex behavioral, developmental, physiological, and operational information into transparent decision-support models. Particular attention is given to the emergence of foundation models capable of interpreting biological information, including the Cell2Sentence (C2S-Scale) family developed by Yale University, Google Research, and Google DeepMind. These technologies demonstrate the growing capacity of large language models to analyze complex biological systems. Their significance within this monograph, however, lies not in direct behavioral prediction but in illustrating how future multimodal AI systems may contribute to broader institutional evaluation frameworks. The C2S Reliability Framework therefore rejects both biological determinism and fully autonomous decision-making. Instead, it proposes a human-centered model in which explainable causal AI assists qualified professionals by integrating multiple independent sources of objective evidence while preserving accountability, transparency, ethical safeguards, and due process. This framework is presented as a conceptual contribution intended to stimulate interdisciplinary discussion regarding the future relationship between artificial intelligence, institutional governance, and human reliability in environments where individual decisions may carry irreversible consequences.

---
