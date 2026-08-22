# Classification batch 6 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-6.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7299991`

- title: On the Gap Between Declarative Vulnerability Knowledge and Secure Code Generation in Large Language Models
- authors: Dang H. Vu, Lam D. Dao, Anh M. T. Bui, Phuong  T. Nguyen, Davide Di Ruscio, Massimiliano Di Penta
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7299991
- keyword hits: large language model, large language models, llm, llms

### abstract

Context. Large Language Models (LLMs) are increasingly integrated into security-critical software engineering tasks, including vulnerability detection and secure code generation. Although LLMs are trained on large-scale corpora that may include vulnerability-related information, such as the Common Weakness Enumeration (CWE), it remains unclear to what extent they encode and can recall such declarative knowledge. Moreover, the relationship between this knowledge and procedural secure coding capability remains uncertain.Objective. This work aims to examine how recalled knowledge relates to procedural secure coding capability in downstream code generation tasks. Methods. We conduct a large-scale empirical study to examine the relationship between declarative vulnerability knowledge and downstream code generation behavior. We operationalize declarative knowledge through a set of controlled recall-based probing tasks that measure the model’s ability to reproduce CWE identifiers, names, and descriptions, and contrast this with performance on security-oriented code generation benchmarks.Results. Our results reveal a consistent gap between declarative knowledge and procedural mitigation capability. While models demonstrate non-trivial lexical fidelity in recalling vulnerability definitions, this knowledge does not consistently prevent insecure code generation. We further observe that the effectiveness of such knowledge depends on how vulnerability information is expressed in prompts. Explicit taxonomy-aligned cues are associated with improved security outcomes, whereas semantically equivalent but more abstract descriptions are less effective.Conclusion. These findings suggest that the utilization of recalled knowledge may rely on surface-level associations rather than robust vulnerability reasoning. Taken together, our observations highlight the distinction between declarative knowledge recall and mitigation capability in LLM-based coding systems, and suggest potential implications for evaluation practices and prompt design.

---

## uid: `doi:10.2139/ssrn.7302410`

- title: Transformers and Large Language Models for Dynamic Cyber Defence: A Survey of Adaptive Defence, Moving Target Defence, and Security by Design
- authors: Mohamed Chahine Ghanem
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7302410
- keyword hits: large language model, large language models, llm, llms

### abstract

Transformer-based large language models (LLMs) are moving cyber defence from static, signature-driven controls toward continuous adaptation. This survey frames that shift as an information-fusion problem: a defensive system must integrate heterogeneous, adversarially influenced sources, network flows, logs, system calls, threat intelligence, code, and analyst dialogue, into decisions whose authority must be justified. Our organising contribution is the SRDAH defence loop of Sense, Reason, Decide, Act, and Harden, which generalises Boyd’s OODA cycle to the LLM setting and which we map, stage by stage, onto the JDL data-fusion model and Dasarathy’s input–output fusion taxonomy. The loop is cross-cut by an architectural axis (encoder-only, decoder-only, encoder–decoder, RL-augmented, multi-agent) and a deployment axis (enterprise, IoT/edge, cloud/SDN, critical infrastructure), and we formalise the resulting taxonomy as a product space over which the surveyed corpus induces an empirical distribution. On this foundation we state the survey’s governing proportionality principle—the authority granted to a model must be commensurate with the verifiability of its outputs and the cost of its errors—as a decision-theoretic authority-allocation rule, and we operationalise it in a reference architecture whose verification boundary implements the rule. Across a 77-reference corpus (2017–2026) selected by a PRISMA-informed protocol, we synthesise capability, evidence, and failure modes for adaptive defence, moving targetdefence, and security by design; quantify a maturity gradient in which evidence strength falls from perception toward autonomous action and hardening; consolidate benchmarks, datasets, and the reproducibility deficit; and analyse the threat surface—prompt injection, jailbreaks, and poisoning—that defensive LLMs themselves introduce. A research-gap agenda targets the verification and calibration bottlenecks that gate safe extensions of autonomy around the loop.

---

## uid: `doi:10.2139/ssrn.7301065`

- title: Student experiences of generative AI in higher education Institutional trust and detection fairness in an ODeL context
- authors: Angelo Fynn
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7301065
- keyword hits: chatgpt, generative ai, generative artificial intelligence, large language model

### abstract

This study aimed to understand the experiences, usage and perceptions of Artificial Intelligence among Open, Distance and e-Learning students. Artificial Intelligence, Generative Artificial Intelligence in particular, has fundamentally changed the way both students and institutions interact with one another. In this paper, 12,790 participants responses to a qualitative survey were analysed using Large Language Modelling assisted qualitative analyses using thematic analysis. The methods section of this paper provides a detailed audit trail of how ChatGPT 5.5 was used to analyse the large corpus of data to derive the overarching themes in the dataset. The themes were AI as an academic support tool, Concerns about AI detection fairness, Policy clarity or uncertainty, Changes in lecturer–student relationships, Psychological ambivalence or neutrality, Dependency or over-reliance on AI, Demand for institutional AI training or support and Anxiety, stress, or guilt associated with AI. The findings of this study reveal that Artificial Intelligence is mostly viewed as an academic support tool as opposed to a replacement for creative and critical thinking. Furthermore, concerns of over-reliance on Artificial Intelligence were paramount among respondents which shaped their usage patterns. The Socio-Critical Model of Student Success, the primary lens through which findings were analysed shows how students’ experiences, usage and perceptions of Artificial Intelligence was the outcome of a dialectical process rather than a one-sided enforcement of policy versus students’ as passive actors in the institutional space.

---

## uid: `doi:10.2139/ssrn.7284538`

- title: Common Conceptual Errors in Student Responses: A Content Analysis of AI-Detected Misconceptions within the IAT Framework
- authors: Hossein Talebzadeh
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7284538
- keyword hits: chatgpt, deepseek, generative ai, large language model, large language models

### abstract

As Generative AI (GenAI) becomes integrated into educational assessment, evaluating its diagnostic reliability in identifying student misconceptions is critical. Drawing on the Integrated AI Triad (IAT) framework, this empirical study investigates how four prominent Large Language Models (ChatGPT, DeepSeek, Copilot, Perplexity) detect, categorize, and address conceptual errors, and examines how teacher experience (novice vs. experienced) moderates prompt optimization. Through qualitative content analysis of 57 diagnostic entries using simulated student responses from a professional development workshop, we developed a six-tier typology of AI-detected misconceptions-Definitional Confusion and Causal Misattribution being most frequent, followed by Overgeneralization, Procedural Errors, Conflation of Related Concepts, and Reductionism. Cross-model comparisons revealed significant variance; DeepSeek achieved the highest pedagogical depth (M=4.04/5.00) and structural transparency, while Copilot exhibited the highest hallucination rate (11.1% vs 5.3% overall). Novice teachers showed rapid improvement (quality scores from 2.9 to 4.0 across four sessions) but greater automation bias, whereas experienced teachers engaged in more critical, iterative dialogue with AI. Diagnostic accuracy was governed by task-level epistemology rather than broad domain boundaries. This study operationalizes AI-TPACK in diagnostic practice and underscores the essential role of human agency-while emphasizing that findings derive from simulated data and require validation in authentic classroom contexts.

---

## uid: `doi:10.2139/ssrn.7278640`

- title: Bureaucracy Without Friction: Why Europe Must Delegate All Administrative Functions to Sovereign Large Language Models
- authors: Sari Katariina Riippi
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7278640
- keyword hits: large language model, large language models, llm, llms

### abstract

Europe has spent a decade constructing the world's most elaborate digital regulatory architecture-GDPR, the Digital Services Act, the Digital Markets Act, the Data Act, the AI Act, and the proposed Cloud and AI Development Act-while leaving the execution of ordinary administrative power in the hands of slow, biased, and discretionary human bureaucracies. The result is a polity that can compel compliance from foreign providers yet cannot issue a business licence, professional certificate, or personal identifier in less than weeks or months. This paper argues that the decisive next step is not further regulation but the wholesale delegation of bureaucratic functions to large language models (LLMs) operating under European jurisdiction and open-source governance. On metrics of rule compliance and consistency, contemporary LLMs already outperform human administrators by large margins in controlled administrative tasks. Once continuous, high-assurance identity recognition is solved, the same systems can generate and issue the full range of official identifiers-personal IDs, company registrations, licences, certificates-in seconds rather than years. The compression of administrative latency would unlock substantial economic value. Europe's present caution, visible in the lag between regulatory ambition and infrastructural capability, risks converting a temporary competitive disadvantage into permanent relative decline. Three complementary institutional pathways-an industrial consortium, a Member-State defence-linked vehicle, and a European Joint Undertaking-can deliver the required public capability. The alternative is continued demotion: a digital civitas sine suffragio in which Europe retains the right to regulate while others control the speed at which its citizens and firms can act.

---

## uid: `arxiv:2608.16118v1`

- title: Assessing LLMs' mathematical abilities requires understanding the various mechanisms of mathematical creativity
- authors: Silvère Gangloff
- affiliations: not stated
- posted: 2026-08-17
- source: arXiv
- link: https://arxiv.org/abs/2608.16118v1
- keyword hits: large language model, large language models, llm, llms

### abstract

How should we assess whether large language models can perform mathematical invention? I argue that this question is currently underspecified: mathematical creativity is not one capacity but several mechanistically distinct modes of meaning-making - reflexive introspection on mathematical practice, analogical import from the sciences, problem-driven construction, and the bridging of distant domains - together with a further, cross-cutting distinction between meaning pursued because a pattern was observed and meaning pursued because it is strategically wanted, a distinction I develop through the case of conjecture-formation. These mechanisms are likely non-substitutable, so that competence in one does not transfer to the others. Grounding each in a historical case study and in an architecture-level account of current transformer-based systems, I suggest that today's models concentrate their competence in modes shaped by recombination and search over existing building blocks; if that description holds, the remaining modes are out of reach in principle, not just slower - though whether it holds is itself the open, empirical part. Because proof is getting cheaper as AI improves at generating it - a shift the field's own leading voices are now diagnosing - mathematical value is migrating toward the modes current systems cannot yet perform, and evaluations of AI mathematical ability should be organized around this taxonomy rather than around aggregate benchmarks that conflate it.

---

## uid: `doi:10.2139/ssrn.7289520`

- title: Feeding the Machine: The Security Risks of Generative AI Use by Public Sector Employees in Southeast Asia
- authors: Nigel Finch
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7289520
- keyword hits: chatgpt, deepseek, generative ai, generative artificial intelligence

### abstract

As public sector employees across Southeast Asia adopt generative artificial intelligence to draft correspondence, summarise reports and support policy analysis, they routinely transmit text, documents and data to servers owned by private firms headquartered outside the jurisdiction whose information is being processed. This paper examines the security risks this creates for governments, applying securitization theory and the human-factor literature on insider threat to four documented incidents: the leakage of proprietary Samsung data through ChatGPT in 2023; a platform-side vulnerability that exposed users' conversation histories and billing data; the 2025 upload of restricted government contracting documents by the acting head of the United States' national cybersecurity agency to a public chatbot; and the 2025 bans on the Chinese model DeepSeek across government networks in Australia, South Korea and Taiwan. Read together, these cases show that the risk is not confined to deliberate espionage but arises structurally from where AI infrastructure is hosted, how vendors handle retained data, and how easily an official under time pressure treats a chat window as a private notebook. The paper concludes with recommendations for sovereign hosting, tiered data-classification rules, and the explicit governance of senior-level exception pathways.

---

## uid: `arxiv:2608.17843v1`

- title: Encoded but Not Actionable: Auditing the Decode-Generate-Steer Gap in Frozen LLMs for Geometric Constraints
- authors: Man Liang, Xinzhao Cheng, Faizan Wajid
- affiliations: not stated
- posted: 2026-08-18
- source: arXiv
- link: https://arxiv.org/abs/2608.17843v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) have demonstrated strong performance on structured reasoning tasks, but what they encode and whether it informs model behavior remain unclear. We investigate this question through geometric reasoning, using parametric CAD constraints as a controlled testbed for separating local pairwise relations from sketch-level constraint status. By probing the hidden states of six frozen decoder-only LLMs, we examine four properties: linear decodability, forced-choice generation, activation-level influence, and behavioral steerability. Pretraining substantially improves the decoding of local geometric relations, and this advantage persists after accounting for positional cues with shuffled-order controls. In contrast, sketch-level DOF status is already highly decodable from randomly initialized representations and improves only modestly with pretraining, indicating that much of its probe performance is available without learned weights. Further analyses show that decodable information is not always actionable. Generation often fails to express this information, and on the two intervention-tested backbones, activation-restoration effects at the patched entity position vanish while decodability persists across depth. Mean-difference steering also does not reliably control outputs. These results show that decodability, generation, activation-level influence, and steerability can diverge in the tested setting. The audit provides a controlled way to distinguish failures to encode geometric structure from failures to express or control encoded information.

---
