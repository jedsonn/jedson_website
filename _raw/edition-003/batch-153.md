# Classification batch 153 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-153.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6701739`

- title: Beyond the Cloud: Privacy-Preserving Evidence Extraction from Indian Judicial Documents via Local LLMs
- authors: Vipul Singh Parmar
- affiliations: not stated
- posted: 2026-05-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6701739
- keyword hits: large language model, llm, llms

### abstract

Indian judicial repositories contain a vast corpus of unstructured judgments that serve as primary sources for forensic data. However, systematic information extraction is frequently obstructed by the linguistic complexity of legal prose and the stringent privacy requirements governing judicial records. We introduce Forensic-LLM, a decentralized framework for the privacy-preserving extraction of forensic evidence from Indian court judgments. By integrating automated document retrieval with local, quantized Large Language Model (LLM) inference, Forensic-LLM enables structured data extraction while maintaining strict on-premises data residency. We demonstrate the framework on a pilot dataset of criminal cases, showcasing its ability to identify and structure diverse evidentiary categories on consumer-grade hardware. Our results highlight the viability of local, lightweight LLMs as a secure and scalable alternative to cloud-hosted AI services for the forensic analysis of sensitive judicial documentation.

---

## uid: `doi:10.2139/ssrn.6749423`

- title: Adaptive Edge-Cloud Routing for Cost-Effective andPrivacy-Aware Code Search
- authors: WeiDong Hou, Khairul  Azhar Kasmiran
- affiliations: not stated
- posted: 2026-05-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6749423
- keyword hits: large language model, large language models

### abstract

Context: Semantic code search backed by large language models improvesranking fidelity but inflates cloud spend and conflicts with policies that limitsending proprietary source listings to third-party inference hosts.Objective: This paper introduces UON-Code, a budget-aware edge-firstorchestration pipeline that answers most queries locally while allowing astronger remote code model only after auditable triggers indicate either thatdense retrieval omitted the correct snippet from the evaluated shortlist orthat on-device reranking outputs are untrustworthy; a configurable quotabounds how often such cloud application programming interfaces may run.Methods: The design pairs a contrastive fine-tuned UniXcoder bi-encoder(≈125 M parameters) for Top-10 candidate mining with a hosted code-orientedsmall language model that performs structured listwise reranking, plus op-tional cloud reformulation, secondary retrieval, or reranking aligned with thereproducibility logging spelled out in this article.Results: Using the six-language filtered CodeSearchNet split and the bench-marking, tracing, and budgeting assumptions packaged with this work, macro-averaged mean reciprocal rank (MRR) reaches 0.8619, whereas cloud inferenceactivates on 10.9% of queries, outperforming bi-encoder-only serving on thepooled ranking metrics reported in the empirical evaluation while avoidingan always-on cloud reranker.Conclusion: The design reduces routine cloud dependency and limits ex-posure of code snippets, offering a deployable compromise when cost andconfidentiality must be satisfied together.

---

## uid: `doi:10.2139/ssrn.6745460`

- title: Beyond Correction: A Stage-Wise Evaluation of Diagnosis-to-Remediation Systems for Language Learner Errors
- authors: Satish K C, Prashidda Thapa, Puspa Subedi, Ushana Bhattarai, Ahsaas Bajaj, Kushal Bhandari, Bhawesh Shrestha
- affiliations: not stated
- posted: 2026-05-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6745460
- keyword hits: gpt-4, llm

### abstract

Grammatical error correction systems now rewrite learner writing with near-human accuracy. Yet a silent correction teaches nothing: a learner shown "I have two brothers" in place of "I am having two brothers" still does not know the rule and will likely reproduce the error. Prior work addresses error explanation, feedback, and exercise generation as separate tasks with disjoint evaluation protocols, leaving open whether a single system can diagnose an error, explain it, and generate targeted practice that remains coherent across stages. We empirically evaluate seven diagnosis-to-remediation systems (spanning correction-only, explanation-paired, single-prompt, template, and multi-stage designs) on 1,094 single-error instances from the W&I+LOCNESS learner corpus, scoring each system on diagnostic accuracy against gold error labels, explanation quality, practice-item validity, and a cross-stage alignment metric that prior educational NLP evaluation has not systematically reported. Explicit schema constraint, not staged decomposition, is what makes diagnosis reliable. A schema-unconstrained singleprompt baseline scores macro-F1 = 0.061 over 12 error categories, but a single-prompt baseline that simply enumerates the 12-class taxonomy in its prompt reaches 0.634, essentially matching a three-stage Diagnosis-Conditioned Remediation system (DCR; 0.639). The same pattern holds on a smaller model (gpt-4.1-mini: 0.634 vs 0.638): the architectural gap is within noise at both scales. Under LLM-as-judge scoring with cross-judge reliability analysis, explanation-quality differences across architectures are also within inter-judge noise (avg. 2.97 vs. 2.93 on a 1-3 scale), and cross-stage alignment is near-perfect for both single-prompt and decomposed approaches (≥ 0.94). Practice-item difficulty calibration is the remaining bottleneck: two LLM judges disagree by up to 55 percentage points on the same items, identifying this dimension as a target for human-anchored evaluation. We report diagnostic accuracy against gold labels and use LLM-as-judge evaluation, with reliability analysis, for explanation and practice quality. The taxonomy, rubric, judge prompts, and derived annotations will be released with the public version of this manuscript so that follow-up work can build on these foundations.

---

## uid: `doi:10.2139/ssrn.6691018`

- title: Three Things Socrates Can Teach Us About Hacking
- authors: Joshua Goossen
- affiliations: not stated
- posted: 2026-05-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6691018
- keyword hits: large language model, large language models, llm

### abstract

Expert penetration testers do not simply enumerate faster than novices. They orient differently — toward targets that have not yet been identified as targets, conditions that have not yet been named as vulnerabilities, attack paths that emerge from the intersection of human decisions made in different organizational roles at different moments in a system's history. This paper argues that this orienting capacity — adversarial cognition — consists of three concurrent components that current security education underdevelops and current AI systems do not replicate: city awareness, the practitioner's working model of how role boundaries, organizational pressures, and systemic drift produce predictable blind spots in the actors who shaped a given environment; live signal reading, the empirical interpretation of system artifacts as evidence about the human decisions that produced them; and the attacker's toolbelt, a practiced repertoire of investigative moves calibrated to deploy specific techniques in response to what the concurrent reading reveals. These three components operate simultaneously rather than sequentially, and their concurrence is what distinguishes expert adversarial cognition from both procedural instruction and the pattern-matching capability that large language models currently bring to automated penetration testing. The paper grounds this framework in Socratic dialectic — where city awareness, live reading of the interlocutor, and a practiced elenchus operate in exactly this concurrent configuration — and situates the educational proposal within the history of professional education, where law and medicine resolved structurally identical gaps between declarative knowledge and professional reasoning through case-grounded, Socratic instruction. It further argues that the existing LLM penetration testing literature evaluates procedural strategy — the sequencing of known steps against known targets — and does not evaluate the prior question of how a practitioner identifies which targets warrant investigation before any documented pattern has been matched. City awareness addresses that prior question. Formalizing the three-component model creates the measurement scaffold for a richer comparison of human and AI adversarial reasoning, opening a feedback loop in which human instruction and machine development become mutually informing rather than parallel tracks.

---

## uid: `doi:10.2139/ssrn.6695678`

- title: From Words to Embeddings: Text Representation and the Information Content of Financial News
- authors: Huaye Zeng, Diego Amaya
- affiliations: not stated
- posted: 2026-05-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6695678
- keyword hits: large language model, llm

### abstract

We study how the representation of text affects the amount of return-relevant information that can be recovered from financial news. Using 135,403 Dow Jones articles, we classify news into topics using keyword matching, Latent Dirichlet Allocation (LDA), and Large Language Model (LLM) embedding-based methods, and relate these classifications to high-frequency returns on five asset-class ETFs. We find that richer text representations recover substantially more information. The share of topics significantly associated with extreme returns rises from 31.4% under keyword matching to 54.1% under LDA and 67.8% under embeddings, a 13-percentage-point increase relative to LDA. This gap indicates that a meaningful portion of return-relevant information is encoded in semantic relationships that are not captured by word co-occurrence alone. Mutual information between topics and returns confirms that information recovery rises with representational richness across horizons and peaks at the 60-second horizon, identifying the timescale of news-driven price discovery. Topic-level results further show that macroeconomic releases are most strongly associated with large price movements. Overall, our findings suggest that the way text is represented is an economically important determinant of how much information can be extracted from financial news.

---

## uid: `doi:10.2139/ssrn.6736978`

- title: Automating Incident Triage and Root Cause Intelligence Through Large Language Model-Driven Correlation of System Logs and Operational Metrics in Large-Scale Distributed Environments
- authors: Hema Latha Boddupally
- affiliations: not stated
- posted: 2026-05-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6736978
- keyword hits: large language model, large language models

### abstract

The increasing scale and complexity of distributed computing environments have intensified the difficulty of timely incident triage and accurate root cause identification, as operators must reason across high volume system logs and heterogeneous operational metrics under severe time constraints. This work addresses the research problem of how incident response can be transformed from manual, heuristic driven practices into an intelligent and automated process capable of semantic understanding and contextual reasoning. The objective is to investigate how large language model driven analysis can be systematically applied to correlate logs and metrics for reliable incident triage in production scale systems. A mixed methodological approach is adopted, combining architectural design, qualitative analysis of operational workflows, and quantitative evaluation of diagnostic efficiency across representative enterprise scenarios. The proposed framework introduces a novel correlation pipeline that leverages language model based contextual abstraction to unify unstructured log streams and structured metrics into coherent incident narratives. Empirical patterns suggest substantial reductions in triage time, improved diagnostic precision, and lower cognitive burden on reliability engineers when compared with traditional rule based and statistical techniques. The findings demonstrate that language model driven reasoning enables a shift from reactive alert handling toward proactive root cause intelligence. The primary contribution lies in articulating a principled foundation for integrating large language models into observability and incident management systems, bridging academic advances in machine intelligence with real world operational demands. The study concludes that automated, semantics aware triage represents a critical advancement for scalable reliability engineering, with significant implications for future research and enterprise operations in large scale distributed environments.

---

## uid: `doi:10.2139/ssrn.6752726`

- title: Reducing Compliance Violations in Ethereum Smart Contracts: A Multi-Agent LLM Approach to ERC Standard Auditing
- authors: MAHA AL-ZBOON, Mu’awya Al-Dala’ien
- affiliations: not stated
- posted: 2026-05-12
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6752726
- keyword hits: large language model, llm

### abstract

Ethereum is a decentralized blockchain platform that allows developers to deploy and run smart contracts, which are self-executing programs responsible for handling digital transactions without intermediaries. ERC standards define how these smart contracts are expected to behave in the Ethereum ecosystem. When these rules are not implemented correctly, contracts may contain security weaknesses that can lead to financial loss or unexpected behavior. For this reason, verifying whether a contract complies with ERC requirements is an important task during the development process. However, compliance verification is still often performed manually, which makes the process slow and dependent on expert knowledge. Most existing static analysis tools mainly detect predefined vulnerability patterns, but they may miss behavioral deviations from Ethereum Request for Comments (ERC) specifications that are not explicitly encoded as patterns. In this study, we present a multi-agent LLM framework designed to automate ERC compliance auditing. The system extracts contract-specific code fragments and evaluates them using multiple independent Large Language Model agents. Their outputs are aggregated through a confidence-weighted mechanism that aims to stabilize the final decision. Experiments on ERC-20, ERC721, and ERC-1155 contracts show that the multi-agent configuration improves recall and reduces false negatives compared to single-agent auditing.

---

## uid: `doi:10.2139/ssrn.6752619`

- title: Authorship and the Human Editor of LLM Outputs A Proposal Based on a Comparative Reading of the 2026 National Reports
- authors: Daniel J. Gervais
- affiliations: not stated
- posted: 2026-05-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6752619
- keyword hits: large language model, llm

### abstract

When a human author runs a draft through a large language model, edits the resulting text, and presents the final product as her own, is she the author? The question is old; the entity whose output she is editing is not. This contribution argues that the answer lies not in new doctrine but in the disciplined application of existing doctrine to a genuinely new set of facts. It supports that conclusion through a comparative reading of the eighteen national reports submitted to ALAI 2026 in The Hague. The reports converge to a degree unusual in comparative IP scholarship. Each affirms, on grounds variously statutory, doctrinal, and constitutional, that purely machine-generated output is not protected; none sets a numerical threshold; all treat the question as qualitative and case-by-case. The operative test tracks the same intuition across traditions: copyright attaches where free and creative choices through which a human author's personality finds expression are visible in the resulting work. Two recent German decisions, the Munich Amtsgericht judgment of 13 February 2026 and the Frankfurt Landgericht judgment of 17 December 2025, supply the substantive and procedural mechanics of the standard's application. The UK Government's announced repeal of section 9(3) CDPA and Italy's Law 132/2025 confirm, on opposite legislative routes, the same human-authorship requirement. From these materials I propose a collaborative writing standard : authorship of an LLM-edited text requires editing that displaces the machine's expressive choices rather than refining them. Three diagnostic criteria operationalise the standard: structural displacement, voice, and expressive specificity. The framework engages the Painer tension and resolves it through the Court of Justice's December 2025 elaboration in Mio and Others . The standard leaves an unprotected middle: a substantial proportion of LLM-assisted professional writing will fall outside copyright. That gap is a legislative problem, not a judicial one.

---
