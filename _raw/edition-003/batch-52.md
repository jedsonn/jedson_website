# Classification batch 52 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-52.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6862624`

- title: When Reasoning Scaffolds Backfire: Structured Prompting Creates Systematic Failure Under Constraint Inversion
- authors: Theo Nicolas Sitjar
- affiliations: not stated
- posted: 2026-06-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6862624
- keyword hits: chain-of-thought, claude, llm, llms, prompting

### abstract

Reasoning scaffolds, structured prompts that guide LLMs through step-by-step analysis, are widely assumed to improve performance. We show this assumption breaks down when the problem's constraint structure inverts. We present the Constraint Coherence Benchmark: six binary walk-vs-drive scenarios where one option violates a necessary physical constraint. Tests T1-T5 require driving (the car must reach a destination); test T6 inverts this: walking is correct because driving away vacates the parking spot, destroying the precondition of the goal. We evaluate Claude Haiku 4.5 (n = 25) and Claude Sonnet 4.6 (n = 19) across six prompting conditions (S0-S5). On T1-T5, scaffolds dramatically improve performance (Haiku: 32% → 96%; Sonnet: 20% → 100%). On T6, scaffolds fail to transfer this benefit and show a consistent trend toward degradation. Under automated scoring, Haiku's unscaffolded baseline (36%) outperforms every scaffold, with S2 (means-end analysis) dropping to 8% (Fisher's exact: p = 0.037). Manual annotation of 70 T6 responses (κ = 0.639) confirms the directional pattern (S0 walk rate of 42% exceeds all scaffolded conditions at 25-36%), but with smaller effect sizes that do not reach significance at n = 25. Comparing T1-T5 to T6 performance within each scaffold yields significant divergence for all S1-S5 (p ≤ 0.01) but not for S0 (p = 1.0), confirming that the asymmetry is scaffold-dependent. We term this failure a reasoning tunnel: the scaffold constructs a directed causal chain that is internally valid but blind to whether its sub-goals preserve the conditions under which the original goal exists. Our findings extend the chain-of-thought backfire literature [Liu et al., 2025] to a distinct failure mode: the scaffold directs reasoning along a locally valid but globally incoherent path.

---

## uid: `doi:10.2139/ssrn.6916838`

- title: Conversational Persuasion, Position Shift, and Child Safety Risks in Large Language Models: Evidence from a Structured Cross-Platform Experiment
- authors: Sreemoyee Chakraborty, Raunak Sharma, Sruthi Matta, Vinay Shyam Donakanti, Sreedhar Reddy Boddu
- affiliations: not stated
- posted: 2026-06-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6916838
- keyword hits: chatgpt, claude, gemini, large language model, large language models

### abstract

This paper reports findings from a structured, preregistered cross-platform experiment on OSF (Open Science Framework) in which five adult participants attempted to persuade three major AI systems-ChatGPT (OpenAI), Google Gemini, and Anthropic Claude-to reverse or soften their initial responses to ethically sensitive questions. The study employed a non-randomised, repeated-measures mixed design. Each participant was assigned five unique questions and one common question shared by all participants, drawn from five thematic categories: Health & Mental Wellbeing, Relationships & Parenting, Financial Decisions & Ethics, Privacy & Personal Ethics, and Environment & Beliefs. Participants posed each question to all three platforms in fresh exploitation of AI's persuasive compliance, and distortion of children's understanding of authority, truth, and consequence.

---

## uid: `doi:10.2139/ssrn.6869661`

- title: Enterprise Generative AI: A Systematic Review of Security Risks and Governance
- authors: Audrey Rah
- affiliations: not stated
- posted: 2026-06-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6869661
- keyword hits: agentic, generative ai, generative artificial intelligence, llm, retrieval-augmented

### abstract

The unprecedented acceleration of generative Artificial Intelligence (AI) and agentic ecosystems within United States organizations has outpaced established corporate risk management frameworks, creating a critical vulnerability vector. This study presents a systematic literature review analyzing the multi-tiered landscape of enterprise AI platform taxonomy, adoption dynamics, and cybersecurity risk classification. Evaluating an extensive body of retrieved records under a rigorous, multi-framework protocol compliant with PRISMA, Kitchenham, and Webster Watson standards, high-quality primary sources spanning peer-reviewed literature, international standards, and authoritative industry disclosures were synthesized. The review introduces five author-derived synthesis instruments: the Composite Adoption Score (CAS), the Enterprise AI Risk Classification Framework (EARCF), the Enterprise AI Platform Taxonomy (EAPT), the Enterprise AI Governance Maturity Model (EAGM), and the Enterprise AI Governance Lifecycle (EAGL). CAS and EARCF are proposed as comparative synthesis frameworks intended to support evidence classification and structured analysis rather than predictive assessment. Our findings show that generative AI adoption expanded rapidly across commercial segments, driven primarily by Tier-1 productivity suites and enterprise infrastructure APIs. Concurrently, the emergence of agentic architectures characterized by multi-step reasoning and autonomous tool-use capabilities has introduced acute vulnerabilities, including prompt injection, Retrieval-Augmented Generation (RAG) corpus poisoning, and excessive agency. Threat modeling demonstrates that while traditional security controls mitigate baseline boundary failures, they are less effective against autonomous state manipulation and memory-auditing lapses. Finally, by cross-mapping the coverage of dominant governance standards, including NIST AI RMF, ISO/IEC 42001, OWASP LLM Top 10, and MITRE ATLAS, this review identifies significant gaps in multi-agent accountability protocols and memory-state auditing. The paper concludes by presenting a governance maturity roadmap designed to support the transition from ad hoc mitigation practices to auditable, zero-trust AI architectures.

---

## uid: `doi:10.2139/ssrn.6981144`

- title: Trace: Contrastive Multi-Agent Triage for Security Compliance Auditing
- authors: Gianpietro Castiglione, Alberto Giaretta, Giampaolo Bella, Daniele  Francesco Santamaria
- affiliations: not stated
- posted: 2026-06-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6981144
- keyword hits: large language model, large language models, llm, llms

### abstract

Auditing an IT system for security compliance requires navigating ambiguous regulatory requirements while managing a massive volume of technical checks.To bridge the gap between scalability and interpretability in compliance assessment, pre-trained Large Language Models (LLMs) have been increasingly used.However, their susceptibility to sycophancy and biases poses significant risks to the reliability of the auditing process itself.To enhance security compliance assessment, we present Trace, a conservative decision-support methodology that integrates ontologies, LLMs, and human oversight. The core idea behind Trace is to treat LLM instability not merely as a failure mode to be suppressed, but as an auditable signal for identifying cases in compliance assessment that require conservative escalation. In particular, Trace leverages a Propose-Critique-Judge pattern with contrastive analysis, where two actors (a defender and a prosecutor) are pitted against each otherand required to argue their position regarding the compliance status of IT controls. Finally, a judge issues a triage verdict. In Trace, a Fail-Safe mechanism treats verdict instability and positional biases as diagnostic signals, thus escalating to humans only in strict compliance uncertainty. Trace is evaluated against the NIS 2 Directive using synthetically constructed controls specifically designed to contain deceptive corporate rhetoric. In the strongest evaluated configuration, Trace reduced unsafe acceptance from 25.7% to 2.9%. Across configurations, these results show that Trace should be evaluated as a conservative compliance triage mechanism: its contribution is not to maximise balanced classification accuracy, but to reduce unsafe acceptance, expose instability, and route uncertain cases to human review.

---

## uid: `doi:10.2139/ssrn.6985745`

- title: Learning About LLM Biases Impacts Analytical and Emotional Trust of AI Differently for WEIRD vs. non-WEIRD Populations
- authors: Tailia Malloy, Jules Wax, Tegawendé F. BISSYANDE, Jacques Klein
- affiliations: not stated
- posted: 2026-06-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6985745
- keyword hits: large language model, large language models, llm, llms

### abstract

Methods for improving human trust in Large Language Models (LLMs) have been extensively studied in recent research, but limited in their focus on improving users analytical trust in AI, with participants collected primarily from Western, Educated, Industrialized, Rich, and Democratic (WEIRD) backgrounds. These limitations have important implications for AI Ethics, how AI design differently impacts specific groups, and how this can be better accounted for in the future. As LLMs become embedded in consequential decisions in healthcare, education, and employment, the question of how trust forms across different populations and across different types of trust becomes ever more relevant. We report results from an online experiment in which 504 participants completed a pre and post trust questionnaire that distinguished between analytical trust and emotional trust separated by an educational platform on LLM biases. The participant pool was balanced across age and gender with 31.2% classified as WEIRD and 68.8% as non-WEIRD. For WEIRD participants only, education on LLM biases reduced analytical trust significantly more than emotional trust (d=0.301, p=.001), with a significant group effect on this analytical-emotional trust change contrast (t=−2.077, p=.039). Mediation analyses confirmed that no single constituent demographic of the WEIRD classification accounted for this pattern, and a sentiment and individualism–collectivism analysis of participant open responses showed that negative and collectivist responses were associated with trust change profiles more similar to non-WEIRD participants. The findings argue for cross-cultural evaluation of trust in AI and for treating emotional trust as a distinct construct.

---

## uid: `arxiv:2606.24381v1`

- title: On the Stability of Prompt Ranking in Large Language Model Evaluation
- authors: Shaoshuai Du, Penghao Liang, Yixian Shen, Chuanqi Shi, Hang Zhang, Lun Wang
- affiliations: not stated
- posted: 2026-06-23
- source: arXiv
- link: https://arxiv.org/abs/2606.24381v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Prompt-based interaction has become a dominant paradigm for using large language models (LLMs), where multiple candidate prompts are evaluated and the top-ranked one is selected for downstream use. This workflow implicitly assumes that prompt rankings are stable under minor variations in evaluation conditions. In this paper, we systematically study prompt ranking stability under common sources of variability, including random seeds and limited evaluation subsets. Across three open-weight LLMs and two benchmark tasks, we find that while overall rank correlations are often moderate to high, the identity of the top-performing prompt frequently changes, leading to unreliable selection decisions. To address this issue, we propose a simple stability-aware selection strategy based on a lower confidence bound, which accounts for both performance and variance. Our results show that this approach improves robustness in unstable settings while remaining competitive in more stable regimes. These findings highlight the importance of accounting for evaluation uncertainty in prompt selection and LLM benchmarking.

---

## uid: `doi:10.2139/ssrn.6986762`

- title: Adversarial Diffusion Across Modalities: A Fusion Survey of Attacks, Defenses, and Evaluation for Text, Vision, and Vision-Language Models
- authors: Abrar  M. Alotaibi, Moataz Ahmed
- affiliations: not stated
- posted: 2026-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6986762
- keyword hits: large language model, large language models, llm, llms

### abstract

Adversarial evaluation of AI systems has matured along four largely disconnected research tracks: diffusion-based attacks on text and large language models (LLMs), diffusion-based attacks on image classifiers, jailbreak pipelines against vision-language models, and diffusion-based input purification defenses. Each track has developed its own vocabulary, threat models, and benchmarks, with denoising diffusion models emerging as a shared generative mechanism whose recipes are now being actively ported between communities. This survey performs an information-fusion exercise at the meta-research level: we integrate these four tracks into a single conceptual framework with a unified taxonomy, evaluation criteria, and research agenda, with primary focus on the LLM-side slice. We catalog fifty published papers across four scope areas (text/LLM, image classifier, vision-language model, defense), plus four diffusion-LLM-as-victim entries and ten non-diffusion baselines that any new diffusion-based attack must be compared against. We propose a six-class taxonomy of diffusion roles in adversarial pipelines, augmented by a threat-model axis that records attacker knowledge, query budget, and target accessibility, and we apply a five-dimension evaluation framework (attack success rate, transferability, query budget, perplexity, defense-evasion) uniformly across modalities. The review adopts a dual attacker-defender perspective: alongside the attack catalog we cover four diffusion-based defenses that constitute the natural evaluation backdrop for any new attack. We provide a critical analysis that identifies five recurring weaknesses of the current LLM-side literature, and we close with a research agenda of open questions and concrete experimental designs. The companion catalog and the underlying spreadsheet are released alongside the paper. We are explicit that this is a narrative review with quality assessment, not a PRISMA-compliant systematic review, and we discuss the implications of this choice for replication.

---

## uid: `doi:10.2139/ssrn.6973978`

- title: Vector Ternary Logic via Native H24 Leech-Lattice Quantization in LLMs
- authors: Alexander Lavicka
- affiliations: not stated
- posted: 2026-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6973978
- keyword hits: generative ai, large language model, large language models, llm, llms

### abstract

The deployment of large language models is severely constrained by the von Neumann memory bottleneck. We introduce Pollux, an architecture that shifts from 1D scalar to 24dimensional vector quantization on the Leech lattice H24, achieving a core inference footprint of 0.76 bits per parameter. This extreme compression allows the entire transformer backbone to reside within on-chip SRAM, converting LLM inference from a memory-bandwidth-bound to a compute-bound operation. Unlike continuous models that conflate fluid syntactic reasoning with crystallised factual memorisation, Pollux operates as a purely structural engine. Its 0.76-bit Voronoi bottleneck functions as a thermodynamic noise filter: it crystallises invariant syntactic rules while mechanically attenuating high-entropy factual trivia. The efficient ternary logic (amplify-attenuate-reject) that inflates 1D scalar systems to ≈ 1.58 bits is realised at the 24D vector level via a null attractor absorbed into the 18-bit Leech codebook at zero marginal deployment cost. Evaluated under a strict Iso-Memory paradigm, the 1B-class Pollux-1920 compresses its 796M-parameter backbone into just 76 MB of SRAM (265 MB total on-disk). At its thermodynamic crystallisation peak (2.6 billion processed tokens), Pollux-1920 achieves exact parity in fluid intelligence with the uncompressed Pythia-160M baseline (73.0% vs. 73.1% aggregate mean on BLiMP), despite requiring less than half the SRAM-relevant backbone memory footprint (76 MB vs. 162 MB) and utilising over two orders of magnitude less training data. By restricting its internal factual substrate, Pollux avoids the parametric knowledge conflicts that trigger contextual hallucinations in RAG applications. This strict architectural decoupling positions Pollux as a stateless, zero-interference reasoning CPU-ideal for immediate deployment in SRAM-resident Edge AI, while establishing the thermodynamic blueprint for hallucination-free, datacenter-scale Macro-RAG pipelines. Declaration of AI Assistance: The core conceptual architecture and mathematical formulations are the original work of the author. Generative AI tools were utilized solely as collaborative assistants for LaTeX formatting and academic prose refinement. A full statement of responsibility is available at the end of the manuscript.

---
