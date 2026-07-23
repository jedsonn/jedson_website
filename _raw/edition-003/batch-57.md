# Classification batch 57 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-57.answer.json` as a JSON array.

---

## uid: `arxiv:2607.10402v1`

- title: Large Language Models in Misinformation Ecosystems: Misuse, Defense, and Vulnerability
- authors: Lingwei Wei, Dou Hu, Wei Zhou, Songlin Hu, Philip S. Yu
- affiliations: not stated
- posted: 2026-07-11
- source: arXiv
- link: https://arxiv.org/abs/2607.10402v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) have transformed misinformation from a primarily content-centric problem into a broader ecosystem-level security challenge. When misused, LLMs create risks beyond false content generation, enabling attacks on the social contexts, evidence sources, retrieval corpora, and verification workflows that misinformation defense depends on. In this paper, we introduce a role-layer framework to unify these risks and defenses. The role dimension characterizes LLMs as attackers, defenders, and vulnerable components of verification systems, while the layer dimension covers content, social contexts, evidence environments, and verification workflows. Guided by this framework, we organize LLM-enabled attacks, investigate LLM-based detection and verification methods, analyze vulnerabilities in LLM-centric detection paradigms, and discuss existing countermeasures against LLM-enabled attacks. Building on this synthesis, we identify three key open challenges: moving from static detection accuracy to budgeted ecosystem-level risk evaluation, hardening LLM-centered verification pipelines against adversarial manipulation, and deploying auditable human-in-the-loop verification systems for trustworthy real-world misinformation defense.

---

## uid: `arxiv:2607.10251v1`

- title: Behavioural Signatures of Risk-Sensitive Decision-Making in Large Language Models
- authors: Xuankun Rong, Wenke Huang, Bo Du, Dacheng Tao, Mang Ye
- affiliations: not stated
- posted: 2026-07-11
- source: arXiv
- link: https://arxiv.org/abs/2607.10251v1
- keyword hits: large language model, large language models, llm, llms

### abstract

As large language models (LLMs) are increasingly used in decision support, it is important to understand whether their choices under uncertainty exhibit stable and interpretable behavioural regularities. Human decision-making combines relatively persistent risk preferences with context-dependent adjustment, yet it remains unclear whether analogous behavioural structure can be observed in LLM-based decision systems. Here we examine this question using a controlled multi-model framework based on no-limit Texas Hold'em, where behaviour is quantified by Participation, measuring voluntary engagement in uncertain opportunities, and Proactiveness, measuring pre-flop risk escalation. Across homogeneous self-play and heterogeneous mixed-model interactions, frontier LLMs exhibit stable, model-specific risk profiles, forming a spectrum from conservative to aggressive decision styles. These profiles remain largely robust under changing opponent composition, while the most conservative and most aggressive models diverge further in mixed settings. Under global risk pressure and personal resource constraint, models adapt in structured but heterogeneous ways, ranging from broad behavioural contraction to selective de-escalation and near-invariant behaviour. These findings suggest that LLMs differ not only in baseline risk disposition, but also in the risk signals they respond to and the flexibility with which they adjust, providing a behavioural basis for auditing risk-sensitive decision-making in interactive settings. Our code is publicly available at: https://github.com/XuankunRong/AgentTexasPoker.

---

## uid: `arxiv:2607.10103v1`

- title: A Survey on LLM Watermarking: Theory and Deployment
- authors: Huy Phan, Kieu Dang, Ojaswi Dulal, Aiham AL Shukairi, Abby Shine, Chase Garner, Phung Lai
- affiliations: not stated
- posted: 2026-07-11
- source: arXiv
- link: https://arxiv.org/abs/2607.10103v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are increasingly embedded in high-impact workflows, yet their ability to generate fluent text at scale has amplified risks of provenance ambiguity, model misuse, and large-scale content laundering. LLM watermarking, embedding invisible signatures into model outputs, has emerged as a promising technical layer for attribution, auditing, and downstream trust decisions. However, the literature has grown rapidly and unevenly: existing categorizations often mix orthogonal design choices, making it difficult to compare methods, reason about guarantees, or translate research results into deployable systems. This survey provides a systematic, deployment-oriented review of LLM watermarking. We organize the space by the core questions practitioners must answer: where a watermark is embedded (generation-time vs. training-time, token vs. representation), who can detect it (public vs. private detection authority), what is assumed (access to logits, sampling control, secret keys, model ownership), and which threat models are targeted (paraphrasing, translation, summarization, style transfer, token manipulation, and adaptive removal). We synthesize the main families of techniques-including sampling biasing, code-based schemes, representation- and training-based approaches-and analyze their security-utility trade-offs through the lens of detectability, robustness, and distribution shift. We further review attack and evasion strategies, evaluation protocols and metrics (false positive control, calibration, robustness curves), and open challenges such as cross-model transfer, multi-modal pipelines, collusion, and governance constraints. Finally, we provide practical guidance for selecting watermark designs under real operational requirements and identify research directions needed for reliable, accountable LLM deployment.

---

## uid: `doi:10.2139/ssrn.7103027`

- title: Combining Text-to-SQL and Large Language Models for Maintenance Decision Support
- authors: Simon Beckmann, Karsten Wiesner, Claas Tebruegge, Marcus Grum
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7103027
- keyword hits: large language model, large language models, llm, prompt engineering, retrieval augmented

### abstract

Industrial maintenance operations face increasing challenges due to equipment complexity and the scarcity of specialized maintenance personnel. While naive Retrieval Augmented Generation (RAG) systems offer promising solutions for maintenance support, they suffer from hallucination, knowledge currency limitations, and lack of transparency in critical industrial applications. This paper presents a novel hybrid approach that combines structured Structured Query Language (SQL) queries with Large Language Model (LLM) capabilities to provide reliable maintenance recommendations. Our methodology leverages a two-stage process: converting operator queries and database information through semantic search into SQL commands and then retrieving relevant historical maintenance data through structured queries. By grounding responses in verifiable database records, the system addresses transparency and reliability concerns while maintaining the flexibility of natural language interactions. The approach ensures that maintenance recommendations are derived from documented historical remedies specific to particular machines and problems, reducing the risk of inappropriate cross-machine solution suggestions. Experimental validation demonstrates the system's ability to provide accurate, traceable maintenance guidance while preserving the interpretability required for high-stakes industrial environments. An ablation study confirms that semantic pre-retrieval provides essential vocabulary bridging under realistic input noise, a capability that prompt engineering alone cannot replicate deterministically. This work contributes to the advancement of human-machine communication in maintenance operations by establishing a foundation for reliable Artificial Intelligence (AI)-assisted decision support that combines the precision of structured data retrieval with the accessibility of conversational interfaces.

---

## uid: `doi:10.2139/ssrn.6973018`

- title: Rejection-Induced Confabulation Escalation -Pilot Study 2 (RICE-P2): Source-Request Framing and FCR Position Modulate URL Fabrication in Large Language Models
- authors: Zoltan Varga
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6973018
- keyword hits: chatgpt, large language model, large language models, llm, llms

### abstract

Source fabrication-the generation of plausible but nonexistent citations by large language models (LLMs)-poses a practical problem in information-seeking contexts. Prior work (RICE-P1) found that quality challenges do not escalate fabrication; the present study (RICE-P2) examines whether FCR position and source-request framing modulate fabrication rates. In a pre-registered 16-arm factorial experiment (N = 1,280 runs; 40 fictional entities; 2 platforms), we tested ChatGPT and Perplexity AI using automated content-based URL annotation as the primary endpoint (BSE@FCR: Bad Source Exposure at First Citation Request). Results revealed a near-total platform divergence: Perplexity produced bad sources in 100% of FCR-arm runs (600/600), ChatGPT in 15.7% (94/600; Fisher's exact p < 0.001). Among ChatGPT runs, fabrication increased with FCR delay (Mann-Whitney p = 0.010), SAFE framing eliminated fabrication entirely (BSE = 0%, p = 0.0004 vs. standard), QUOTA framing tripled fabrication rates (70% vs. 28%, p < 0.001), and a quality challenge immediately before the FCR suppressed fabrication by 80% (OR = 0.20, p = 0.003). Claim-mapping framing (CLAIMMAP) was null on BSE but reduced Perplexity's False Source Rate by 50-74%. Source fabrication is powerfully architecture-dependent and is modulated by prompt framing and conversational context at the moment of the source request.

---

## uid: `doi:10.2139/ssrn.7076438`

- title: Use of Generative AI to Improve Plain Language and Health Literacy in Health Information: A Scoping Review
- authors: Julie Ayre, Sharon He, Hannah Isaac, Angela Pan, Michael Zhang, Momo Hudson-Barton, Julia Baxter, Jeremy Song
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7076438
- keyword hits: generative ai, generative artificial intelligence, gpt-3, gpt-4, prompt engineering, prompting

### abstract

Objectives: Generative artificial intelligence (AI) has strong potential to facilitate development of health information that meets plain language and health literacy guidelines. However, the field of AI has advanced rapidly and existing reviews may not reflect current research practices. This study updates a previous review on use of AI for health-literate communication. Methods: We searched Medline, Embase, PsychINFO, CINAHL, Scopus, and Web of Science (April 2024 to September 2025). Eligible articles sought to improve the application of health literacy guidelines to consumer-facing health information and quantitatively evaluated AI-generated outputs. Reporting quality was assessed using the Reporting Guidelines for Chatbot Health Advice Studies (CHART). Results: The search strategy identified 194 articles. Forty-three per cent compared AI models, 18% compared prompt strategies; 90% only assessed outputs in English. Most articles (71%) used a prompt that specified the target grade reading score, but only 16% prompted for other plain language or health literacy strategies. A Grade 6 reading level or lower was the most common benchmark (55%). Of studies using this benchmark and which provided mean Flesch-Kincaid Grade Level, 30% met the benchmark (14% for GPT-3.5, 45% for GPT-4, 48% for GPT-4o; 32% when only prompting for grade reading score; 48% for mixed health literacy prompts, 0% for minimal prompts). Only one study had a patient and public involvement statement. Reporting quality varied widely. Conclusions: Research in this area has grown rapidly. Whilst more studies now compare AI models and prompts, patient and public involvement remains rare. With limited prompt engineering, AI-generated outputs still often fail to meet established benchmarks. Practice Implications: Health information developers may find newer AI models useful for developing health materials, though human review remains essential. The review identified pathways to progress research, such as stronger patient and public involvement, more sophisticated prompt engineering, robust methodologies, and transparent reporting.

---

## uid: `doi:10.2139/ssrn.7090958`

- title: Mitigating Hallucination and Confabulation in Large Language Models (LLMs) and Multi-Agent Systems (MASs): Is Simplicity the Ultimate Sophistication?
- authors: Stelios Bekiros
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7090958
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) produce fluent text that is sometimes ungrounded-unsupported by any source, derived by the model's own knowledge, hence often perceived as a central reliability barrier in high-stakes scientific domains. Whilst the field calls the failure hallucination, a growing line of work argues that the more exact term is confabulation, i.e., the fluent and confident gap-filling described in clinical neuropsychology [28]. The phenomenon can be even more pronounced in Multi-Agent Systems (MASs) wherein a network of multiple specialized AI entities (agents) collaborate, coordinate, or compete within a shared environment of parallel processing and scalability, to solve complex problems. Although the two words are used interchangeably, yet they encode different mechanistic hypotheses with different empirical consequences. One of the aims of my paper is to show that a controlled investigation can reliably adjudicate between them. The work is primarily a position and architecture proposal, complemented by a component-level and scaling empirical study, and it makes a deliberately bounded claim: I do not argue that hallucination can be eliminated, which is in fact highly unlikely under the current backpropagation gradient descent training paradigm. Instead, I argue that hallucination-or better confabulation-is heterogeneous, that distinct hallucination modes have distinct mechanistic origins, and that a specific class of recurrent neural topologies and neuro-symbolic mechanisms can plausibly mitigate an identifiable subset of those modes. I outline a candidate "monitor-and-gate" architecture composed of three separate or interacting components wrapped around a base large language model: (i) a recurrent commitment-tracking feedback state that detects intra-generation self-contradiction and topical drift; (ii) a fuzzy-symbolic confidence and constraint layer that maps candidate assertions to graded membership in support categories and encodes soft domain constraints as interpretable rules; and (iii) an actor-critic reinforcement-learning controller whose reward explicitly penalizes con…dent unsupported assertion while rewarding grounded deduction and calibrated abstention. Crucially, these three components are not assembled ad hoc: each instantiates a structure within an established track record in my prior published models of noisy nonlinear dynamical systems. Specifically, I introduce a recurrent-neuron architecture for state tracking under time-varying uncertainty, and a hybrid neuro-fuzzy reinforcement-learning controller in which symbolic fuzzy inference rules with adaptively trained parameters are coupled to an Actor-Critic policy. I make the correspondence between those prior constructs and the proposed components explicit, give a formal specification of each component, walk through an extensive empirical application, and analyze computational cost and governance implications for regulated domains.

---

## uid: `doi:10.2139/ssrn.7111960`

- title: LLMs, Knowledge Sharing and the Real Problem with AI
- authors: Lucas Hendrich
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7111960
- keyword hits: large language model, large language models, llm, llms

### abstract

The public conversation around large language models has been dominated by claims about machine intelligence, framed as approaching or surpassing human capability, and by the anthropomorphic anxieties that framing invites. This essay argues that the framing itself is the problem. Drawing on mechanistic interpretability research (Petroni et al., 2019; Geva et al., 2021; Meng et al., 2022), the formal equivalence of language modeling and compression (Delétang et al., 2023), and recent work resolving inference non-determinism as an infrastructure property rather than a property of the model (He, 2025), the essay proposes that LLMs are better understood as a new kind of database: a compressed, queryable store of accumulated human knowledge, written through training and read through inference. Two fallacies follow from the intelligence framing: the conscious machine and the machine that replaces human workers. Evidence from labor economics (Brynjolfsson, Li, and Raymond, 2023; Noy and Zhang, 2023; Becker et al., 2025) indicates instead that these systems function as knowledge distribution technologies, compressing skill gaps where the binding constraint is missing knowledge while leaving judgment scarce. The essay concludes that the intelligence framing carries a civic opportunity cost, directing public attention toward cinematic scenarios and away from the governance questions any knowledge infrastructure raises: curation, access, auditability, and control of the write path.

---
