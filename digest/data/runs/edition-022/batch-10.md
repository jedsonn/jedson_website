# Classification batch 10 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-10.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7272084`

- title: Quantifying Representational Mismatch between Narratives and Structured Reports in Near-Death Experiences
- authors: Cristian Pulido, Francisco Gómez, Prejaas K.B. Tewarie, Roxane S. Hoyer, Steven Laureys
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7272084
- keyword hits: large language model, large language models, llm, llms

### abstract

Near-death experiences (NDEs) are often studied using both structured questionnaires and narrative reports, yet these representations cannot be assumed to provide interchangeable representations of the same experience. Narratives allow flexible expression of different aspects of the experience, whereas questionnaires organize reports into predefined dimensions and retrospective evaluations. How disagreement between these formats should be quantified and interpreted remains unclear. This study operationalized this disagreement as \emph{representational mismatch} by comparing questionnaire-derived and narrative-derived labels across \NDEAnalyzed~NDE reports. Narratives were coded using 12 large language models (LLMs), complemented by human-reference annotation, a lexical baseline, external sentiment benchmarks, and preprocessing sensitivity analyses. Correspondence was evaluated across emotional tone, experiential features (NDE-C), and post-experience life changes (LCI-R). Agreement was systematic but incomplete and differed across representational domains. Experiential features showed stronger correspondence than life changes (NDE-C macro F1 =$0.62\,[0.60,0.65]$ vs. LCI-R $0.52\,[0.50,0.54]$). Narrative tone contained meaningful affective information but corresponded only partially with global self-reported valence (macro F1 =$0.43\,[0.41,0.44]$), with disagreement concentrated mainly in mixed and neutral narrative-tone assignments rather than direct polarity reversals. Standard sentiment benchmarks showed substantially higher correspondence (macro F1 $=0.78 \pm 0.16$), making a purely general model-limitation explanation less plausible. These findings support interpreting cross-format disagreement as a structured property of reporting rather than measurement or extraction error alone. Representational mismatch provides a framework for identifying where different reporting formats converge, where they cease to be interchangeable, and how the elicitation format shapes what becomes observable in research on subjective experience.

---

## uid: `doi:10.2139/ssrn.7270241`

- title: What is Collaborative Inference? Conditions for Collective Reasoning beyond Individual Inference in the Age of LLMs
- authors: Akira Funabiki
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7270241
- keyword hits: large language model, large language models, llm, llms

### abstract

This paper proposes a theoretical framework for collaborative inference in the age of large language models (LLMs). It conceptualizes individual intellectual activity as a recursive cycle of Value → Question → Reasoning → Understanding → Value Updating → New Question , and defines collaborative inference as the mutual updating of reasoning through interaction with difference. Unlike approaches that emphasize agreement or shared answers, this framework allows participants to retain divergent conclusions while transforming their own reasoning through interaction. The framework is applied to Human–LLM interaction, where LLMs are conceptualized not as answer-generating teachers but as heterogeneous inferential systems that can introduce alternative perspectives, expose assumptions, and stimulate critique and reconstruction. The paper further develops a model of self-updating education , shifting the focus of learning from acquiring fixed answers toward generating questions, revising reasoning, reconsidering values, and generating new questions. To connect the framework with empirical research, the concept of an Update Trace is proposed for examining changes in learners' reasoning over time. The central proposition is that collaborative inference is not the elimination of difference, but the continuous updating of reasoning through difference and the generation of new inquiry .

---

## uid: `doi:10.2139/ssrn.7270039`

- title: PAUSE: A Privacy-preserving Self-reflection Tool for AI-associated Cognitive Offloading
- authors: Mahbub Ul Alam
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7270039
- keyword hits: large language model, large language models, llm, llms

### abstract

Cognitive offloading is the use of external aids, such as notes, calculators, or search engines, to reduce mental effort. Large language models (LLMs) extend this to thinking itself, and by AI-associated cognitive offloading, I mean the pattern where a person routinely substitutes LLM output for their own reasoning, idea generation, learning, or communication. Recent empirical work reports associations between some patterns of LLM use and changes in critical thinking effort, neural engagement during assisted tasks, creative diversity, learning behaviour, and social dependence. Validated instruments for AI reliance, dependence, and literacy have begun to appear. I describe PAUSE (Patterns of AI Use: Self-Examination) , a privacy-by-design web tool that occupies a different niche from these. It is a lightweight, non-diagnostic reflection aid for private individual use. PAUSE is organised around how a person's own LLM use may relate to cognitive offloading across four everyday domains (reasoning & critical thinking, creativity & originality, research & learning, and social & communicative capacity). It delivers a short, free, no-login self-check, scores it entirely in the browser, and returns descriptive, domain-aware reflections. The self-check pairs reverse-scored behavioural items with a claim-evaluation reasoning probe, an alternative-uses creativity probe, and a small retrospective before-and-after block. PAUSE does not assume that AI use is harmful. It addresses the narrower case where AI substitutes for effort a person may want to preserve. The application is privacy-preserving by design: scoring is deterministic and runs client-side, no personal data is required, nothing is transmitted or stored beyond the browser session, and no LLM is involved in production. In this paper, I describe the conceptual grounding, the item design, the scoring, the architecture, and the design philosophy. PAUSE is a self-reflection tool, not a validated psychological instrument. It presents no reliability or validity evidence, and all readings should be interpreted as descriptive self-reflection rather than psychological measurement.

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
