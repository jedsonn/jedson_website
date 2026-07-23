# Classification batch 349 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-349.answer.json` as a JSON array.

---

## uid: `arxiv:2607.16010v1`

- title: AI Watermark Evidence Fails Forensic Readiness: An Empirical Evaluation
- authors: Saifur Rahman Tamim, Amir Labib Khan
- affiliations: not stated
- posted: 2026-07-17
- source: arXiv
- link: https://arxiv.org/abs/2607.16010v1
- keyword hits: llm

### abstract

Governments are increasingly mandating that LLM-generated content carry watermarks. The EU AI Act calls for markings that are "sufficiently reliable and robust." California's SB 942 requires disclosure that is "permanent or extraordinarily difficult to remove." Both mandates rest on an untested assumption: that watermark detection yields evidence reliable enough for courts. This paper tests that assumption directly. We evaluate three representative LLM watermarking methods -- KGW, Unigram, and the MarkLLM implementation of SynthID-Text -- against the Daubert admissibility criteria and the NIST SP 800-86 digital forensic process. To structure this evaluation, we propose a Forensic Readiness Score (FRS) framework with 12 criteria, three mandatory gates, and a 60-point scoring system. We focus on meaning-preserving paraphrase as the attack vector, since it is both legally realistic and difficult to dismiss as evidence tampering. The results raise serious evidentiary concerns. Out of 846 valid paraphrase runs across 15 diverse prompts per method, every single initially-detected KGW and Unigram text lost its watermark after paraphrasing -- 100% conditional removal. SynthID fared only slightly better at 98.3%. Even before any attack, false-negative rates were already high: 70% for KGW, 83% for Unigram, 80% for SynthID. The SynthID configuration also flagged 5.4% of paraphrased human-written controls as AI-generated and showed an 18.6% paradox rate, with 80% of its own pristine watermarked output landing in the uncertainty deadband. None of the three methods satisfy more than two of five Daubert factors. We also find that the FRS point-based scoring system, despite working as designed, cannot fully capture forensic uselessness -- a limitation worth noting for future framework design. These configurations, as tested, do not meet the evidentiary bar that courts require.

---

## uid: `arxiv:2607.15781v1`

- title: AgentFAIR: A Multi-Agent Collaborative Framework for FAIRness Evaluation of Geospatial Datasets
- authors: Ming Chen, Pranav Pai
- affiliations: not stated
- posted: 2026-07-17
- source: arXiv
- link: https://arxiv.org/abs/2607.15781v1
- keyword hits: llm

### abstract

Geospatial datasets support applications from urban planning to climate modeling, yet consistent assessment of FAIR compliance is difficult. Existing evaluators use different rubrics and evidence sources and may fail on JavaScript-rendered pages or repository-specific identifiers. For 50 datasets from 10 repositories, the standard deviation of normalized scores across available tools averages 15.0 percentage points and reaches 30.3 for one dataset. Because these outputs are not equivalent measurements, we use them to characterize disagreement and failure modes, not comparative accuracy. We present AgentFAIR, a multi-agent framework combining structured metadata extraction with 13 sub-principle-specific LLM evaluators. Each produces a 0-3 maturity score, cited evidence, and recommendations; a critic checks evidence and consistency and can request targeted re-evaluation. Mean Findability, Accessibility, Interoperability, and Reusability scores are 79.7%, 70.4%, 45.3%, and 72.0%. Rank correlations with four baseline tools range from 0.31 to 0.61; the FAIR-enough comparison is not statistically significant. On a 10-dataset repeated-run subset, sub-principle agreement averages 89% (standard deviation: 3 percentage points), versus 71% without the critic. A preliminary 15-dataset expert study yields Fleiss' kappa of 0.71 and 82% alignment with expert consensus. API cost is approximately USD 0.054 per dataset. These results support auditability and feasibility, while the limited benchmark, incomplete ablations, and single-model-family validation constrain claims about accuracy and generalization.

---

## uid: `doi:10.2139/ssrn.7000618`

- title: Process Visibility in AI-Mediated Education Why the Question Is Not Who Wrote It But Who Thought It
- authors: Warner Rey Allen
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7000618
- keyword hits: generative artificial intelligence

### abstract

The deployment of generative artificial intelligence across higher education has produced a governance crisis that mirrors structural failures identified in defense, transportation, and human care. Institutions have responded to AI-capable students by deploying detection tools that produce probability scores rather than evidence, by issuing contradictory policies that change from classroom to classroom, and by signing procurement contracts without consulting the populations those contracts govern. This paper argues that the prevailing question-"did AI write this?"-is structurally incapable of producing a governed outcome. The question that governs is: "can the student reconstruct the thinking the work claims to represent?" Drawing on McCormick's process visibility framework (2026), Vygotsky's theory of inner speech as cognitive technology (1934), and empirical neuroscience demonstrating that self-directed speech physically modulates cognitive processing (Lupyan and Swingley 2012; Moser, Kross et al. 2017), this paper establishes that students who use AI as an externalized thinking partner are engaging the same cognitive mechanism that developmental psychology has documented as foundational to human learning. The paper then identifies the institutional governance failure across the California State University system as a case study in what happens when technology is deployed without governance architecture, and proposes a structural framework-grounded in the author's published governance architecture for irreversible systems (Allen 2026a)-that addresses both the classroom and the institution.

---

## uid: `doi:10.2139/ssrn.6996880`

- title: Leveraging AI to Identify Small Business Regulations at the Federal, State, and Local Levels
- authors: Patrick A. McLaughlin, Dustin Chambers
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6996880
- keyword hits: large language model, llm

### abstract

We introduce a novel database of small business exemptions at the 3-digit NAICS industry level for 48 US States in 2023. Our dataset is derived using Large Language Model (LLM) technology, which is validated using more traditional Natural Language Processing (NLP) methods. We demonstrate that this data is correlated with other measures of small business friendliness at the state level. Furthermore, we apply our LLM classifier to the US Code of Federal Regulations and show that the industry pattern of small business regulation at the state level is similar to industry patterns at the federal level. We find that industries with higher levels of small business exemptions exhibit greater economic dynamism (i.e., more establishment and job formation). Finally, we extend the same LLM-based screening approach to municipal ordinances, analyzing 3,241 jurisdictions. This municipal extension shows that local "small business" definitions are substantially more heterogeneous than those used at the state and federal levels, varying widely across jurisdictions and policy domains.

---

## uid: `doi:10.2139/ssrn.7003938`

- title: Artificial Intelligence, Evolution and Technocapitalism
- authors: Howard Covington
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7003938
- keyword hits: large language model, large language models

### abstract

This essay brings together ideas on the changes that artificial intelligence may cause in preparation for a talk in Salzburg in Summer 2026. It makes observations on how intelligent biological life evolved and how large language models could lead to the evolution of silicon-based life. It highlights the role of Austrian scholars in developing the ideas that led to technocapitalism in Silicon Valley in the 1950s. It notes that despite this major contribution, Europe has been unable to adapt to technocapitalism and risks becoming a digital vassal.

---

## uid: `doi:10.2139/ssrn.6998138`

- title: The Spatial Footprint of Artificial Intelligence: Evaluating the Friction Between Fast-Tracked Digital Infrastructure and Local Land-Use Governance in Italy
- authors: Mehrdad Afsharmajd
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6998138
- keyword hits: generative ai

### abstract

The generative AI boom has turned data centres from invisible utilities into one of the most land-, power-and water-intensive building types of the early twenty-first century. Planning theory, however, still tends to treat them through the dematerialising language of "the cloud." This paper examines the institutional friction that the AI build-out has produced in Italy, where the national state and sub-national governments moved in opposite directions within a single quarter of 2026. Law Decree 21/2026 (Article 8) created a fast-tracked single national authorisation procedure (procedimento unico nazionale) with a binding statutory deadline of ten months, extendable to thirteen. Its purpose was to capture mobile hyperscale capital before it relocated to other European markets. Within weeks, the Lombardy region reasserted territorial control through Regional Law 11/2026, which routes large projects into supra-municipal planning agreements, requires wasteheat recovery audits, and imposes equalisation and compensation levies on built surface. We read these instruments against the actual reorganisation of Italy's data-centre geography: the saturated Milan inference cluster, the brownfield conversion of the former Galileo Ferraris thermoelectric plant at Trino in Piedmont, and the subsea-cable and renewables story now unfolding as a "Data Center Valley" in Puglia. AI infrastructure, we argue, exposes a territorial blind spot in planning practice. We develop that argument through two distinctions: between the spatial logics of AI training and AI inference, and between data centres as engines of industrial requalification and as instruments of territorial extraction. The governance question is not whether to authorise these facilities. It is how to convert a highly automated, low-employment, resource-hungry industry, one that runs on accelerated corporate timelines, into durable local public value. That conversion requires a shift from reactive zoning toward proactive territorial equalisation.

---

## uid: `doi:10.2139/ssrn.6986861`

- title: A Taxonomy of Rational Handoffs for AI Agents
- authors: Shaurya Jauhari
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6986861
- keyword hits: agentic, ai agent

### abstract

As autonomous AI agents become more prevalent, the question of when they should relinquish control to a human is a critical design concern. Current approaches often rely on ad-hoc heuristics. This paper makes two contributions to establish a more principled foundation for this problem. First, and primarily, we introduce a comprehensive taxonomy of rational hand-off scenarios, moving beyond simple confidence scores to include triggers based on risk, system policies, resource optimization, causal uncertainty, and information security. Second, we present the rudimentary mathematical foundations of a framework designed to operationalize this taxonomy. We introduce the Agency-Humility Equilibrium (AHE) as a core decision-theoretic principle and the Handoff Utility Function (HUF) as a mechanism for balancing autonomous action against deferral. This work aims to provide a clear conceptual map and a preliminary formal language for designing safer and more reliable agentic systems.

---

## uid: `doi:10.2139/ssrn.7140369`

- title: When Textual Signals Lose Value: Generative AI and Scientific Attention Allocation
- authors: Zhuoxian Lin, Jiaqi Liu
- affiliations: not stated
- posted: 2026-07-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7140369
- keyword hits: chatgpt, generative ai

### abstract

Scientific attention is allocated under severe information constraints. This allocation is especially uncertain in early-stage research markets, where readers evaluate work before formal peer review. Building on signaling theory, we argue that generative AI reduces the informational value of textual signals by lowering the cost of producing polished scholarly text. Readers may therefore shift attention toward harder-to-imitate signals, such as external certification and institutional reputation. Using 286,378 papers from the Social Science Research Network (SSRN), we examine how generative AI changes the attention value of textual, certification, and reputation signals. We show that textual complexity loses its pre-ChatGPT attention premium after ChatGPT’s public release. This decline is strongest for unpublished papers and weakest for papers with stronger journal certification, while institutional reputation becomes more consequential in attracting downloads. We further find that the post-ChatGPT decline in the attention value of textual complexity is stronger for papers associated with highly reputable institutions, consistent with reputation-based signal substitution. These patterns suggest that readers substitute away from reproducible textual signals toward durable credibility signals when allocating attention under uncertainty. The study contributes to research on scientific attention, signaling, and cumulative advantage by showing that generative AI can change the relative importance of evaluative signals in science. Although AI may democratize scholarly communication, it may also reinforce existing status advantages in scientific visibility.

---
