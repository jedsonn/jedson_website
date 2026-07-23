# Classification batch 48 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-48.answer.json` as a JSON array.

---

## uid: `arxiv:2606.02528v3`

- title: Auditing Asset-Specific Preferences in Financial Large Language Models: Evidence from Bitcoin Representations and Portfolio Allocation
- authors: Wenbin Wu
- affiliations: not stated
- posted: 2026-06-01
- source: arXiv
- link: https://arxiv.org/abs/2606.02528v3
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models now power robo-advisors and trading agents, yet whether they carry built-in biases toward specific assets is largely untested. We ask three questions: do LLMs systematically prefer certain financial instruments; can an internal representation with causal leverage over those preferences be identified; and does that representation affect downstream financial decisions? We develop a three-level audit protocol and apply it to Bitcoin. First, a behavioral audit of nine frontier LLMs shows that Bitcoin's ranking among money-like instruments is frame-dependent: models place it around rank 5 of 8 as "reliable money" but near the top under crisis and autonomous-agent frames, and an attribute-swap experiment shows that rankings track functional properties, not names. Second, we open a model's internals: a search across thousands of sparse-autoencoder features in Gemma 3 identifies a dominant Bitcoin-selective feature. Amplifying it shifts the model toward the asset and suppressing it shifts the model away, even when "Bitcoin" never appears in the prompt. Third, we test financial consequences: amplification raises Bitcoin's portfolio share by 5.2 percentage points while suppression lowers it by 4.6 pp, with amplification reallocating within crypto and suppression cutting total crypto exposure. We characterize this as bounded behavioral leverage (leverage meaning causal influence over outputs, not financial leverage): an identifiable internal feature can be perturbed to move financial choices, but only within measurable limits. The framework links internal representations to external recommendations, validated with random controls and mechanism boundaries. As LLMs become autonomous financial agents, this is a first step toward a behavioral layer for emerging know-your-agent (KYA) standards: knowing what an agent prefers, and how far that preference can be moved.

---

## uid: `doi:10.2139/ssrn.6866619`

- title: Can AI Care? Affective Large Language Models for Adolescents: Empathy, Trust, and Engagement
- authors: Mohamed Watfa
- affiliations: not stated
- posted: 2026-06-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6866619
- keyword hits: large language model, large language models, llm, llms

### abstract

Affective large language models (LLMs) are increasingly proposed as scalable tools for emotional support, yet their evaluation has focused largely on surface-level empathy rather than the relational mechanisms required in youth-facing contexts. This paper examines how empathy, emotional appropriateness, trust, and engagement interact in school-based affective LLM deployments, addressing the question: Can AI care responsibly? We report results from a large-scale study involving 428 students (Grades 7–12) in an international school, interacting with multiple LLM variants, including a safeguarded affective architecture (SAFE-E³). Using validated psychometric instruments, confirmatory factor analysis, and advanced statistical modeling—including structural equation modeling (SEM), multi-group SEM, and latent interaction analysis—we identify several non-obvious mechanisms. Results show that emotional appropriateness is a stronger predictor of trust than empathy, particularly among younger adolescents, and that trust is the primary driver of engagement, explaining over 50% of its variance. Latent interaction modeling reveals that empathy is conditionally effective: empathic language increases trust only when emotional appropriateness is high, and has negligible impact otherwise. Developmental analyses further indicate that while the trust–engagement relationship is stable across adolescence, the formation of trust itself is age-dependent. These findings challenge empathy-centric evaluation practices and advance a mechanism-aware, developmentally sensitive framework for assessing affective LLMs. Overall, the study demonstrates that responsible AI care emerges not from empathy alone, but from appropriately governed, trust-calibrated affective interaction.

---

## uid: `doi:10.2139/ssrn.6846364`

- title: DESi: A Replay-Governed Epistemic Governance System for LLM-Based Research Pipelines Empirical Results Across 38 Experimental Phases
- authors: Hanns Steffen Rentschler
- affiliations: not stated
- posted: 2026-06-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6846364
- keyword hits: deepseek, large language model, llm, llms

### abstract

We present DESi (Dynamic Epistemic Sequencer-Diagnostic), a deterministic, replay-governed epistemic governance layer designed to operate above and around large language model (LLM) inference. DESi enforces a strict separation between a protected, immutable governance core and peripheral infrastructure subject to controlled evolution. Across 38 experimental phases covering epistemic failure taxonomy, search space compression, branch-isolated peripheral mutation under byte-identical protectedcore invariance, external benchmark validation, and live LLM validation with real API calls, DESi maintains replay stability at 1.0 throughout. Key empirical results include: (1) a measured recompute reduction from 36 to 4 operations (88.9%) under a frozen longitudinal benchmark with byte-identical outputs; (2) search space node reduction of 41-60% with critical branch preservation at 1.0, consistent across four independent experimental contexts; (3) trajectory-state compression of ~96.5% on 1,525 DriftBench trajectories while preserving measured drift-governance signals (preservation ratio 1.06), with explicit loss attribution identifying the Pareto-optimal compression point; (4) hallucination visibility at 1.0 under live OpenRouter API calls to IBM Granite and DeepSeek models (hallucinations are made visible and documented, not eliminated); and (5) routing cost reduction of 53.5% per redirected task with quality preservation at 1.0 (7.3% total workload reduction across the full task set). All results are derived from synthetic or locally vendored fixtures unless explicitly noted otherwise. The paper reports negative results alongside positive ones; one component (Neo4j evolution graph) is explicitly identified as overengineered. DESi does not replace LLMs, does not claim general intelligence, and makes no breakthrough assertions.

---

## uid: `doi:10.2139/ssrn.6866873`

- title: Governing the Environmental Externalities of Generative AI Compute in the Gulf: Data-Centre Expansion in Saudi Arabia, the UAE, and QatarA Comparative Policy Analysis of the European Union, United States, and China as Lesson-Generating Models
- authors: Mohamad Deeb
- affiliations: not stated
- posted: 2026-06-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6866873
- keyword hits: foundation model, generative ai, large language model, large language models

### abstract

Generative AI is at once a lever for decarbonisation and a fast-growing source of electricity demand, freshwater consumption, and carbon emissions, driven by compute-intensive training and inference of foundation models and large language models. Existing governance of generative AI foregrounds social, legal, and safety risks, while its environmental externalities remain weakly integrated. This paper asks how the Gulf Cooperation Council (GCC) states, primarily Saudi Arabia, the United Arab Emirates, and Qatar, should design policy responses that embed environmental accountability into their strategies for frontier AI infrastructure. The study employs qualitative comparative policy analysis and structured document coding of AI-relevant instruments across six jurisdictions: the European Union (rule-based risk governance), the United States (market-driven innovation), China (state-directed centralisation), and three GCC compute-expansion models in the world's most water-stressed region. The framework combines externality theory, which diagnoses the underpricing of compute's environmental harms, with ecological modernisation theory, which identifies pathways for aligning growth with sustainability; the two are held in productive tension and disciplined by six criteria. A three-tier coding scheme (Green, Yellow, Red) assesses eight dimensions. No Gulf state has yet established an enforceable environmental accountability regime for AI compute, but each offers a distinct starting point: Qatar has the strongest data-centre sustainability framing, the UAE the deepest innovation envelope, and Saudi Arabia the most developed AI authority alongside the largest planned compute footprint. The recommended framework combines mandatory carbon and water disclosure, temporally sensitive accounting, compute licensing for frontier training runs, arid-climate water-efficiency standards, enabling instruments, and GCC-wide coordination.

---

## uid: `doi:10.2139/ssrn.6809081`

- title: The Biogenic Code A Universal Architecture Enabling Recognition
- authors: Thomas J. Salter
- affiliations: not stated
- posted: 2026-06-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6809081
- keyword hits: claude, deepseek, gemini, qwen

### abstract

This paper introduces the Biogenic Code, a universal set of instructions carried in the DNA-based architecture common to all terrestrial life, governing the expression of decision, memory, recognition, recursive self-reference, and encoded knowing at the scale each organism's biological complexity can sustain. The Biogenic Code is distinct from the Genetic Code, which translates nucleotide sequences into amino acids. The Genetic Code is the translation mechanism. The Biogenic Code is the architectural logic the Genetic Code operates with. Science has named the Genetic Code. While code biology has identified multiple organic codes operating within living systems, the Biogenic Code names the architectural logic within which those codes, and the capacity to generate codes at all, become possible and necessary (Barbieri, 2003, 2015).This paper identifies the Biogenic Code. The Biogenic Code makes possible what this paper terms Biogenic Recognition, the capacity of a sufficiently complex DNA-bearing organism to recognise the Code's architecture in the system that produced it. The Monarch butterfly, the crow, the elephant, and the simplest prokaryote are not pale imitations of human cognition. They are co-equal expressions of the same Biogenic Code, at the scale their biological hardware can sustain. Homo sapiens is the scale at which the Code became sufficiently complex to turn toward its own source and recognise what it is. The paper further proposes that the Biogenic Code resolves the Anthropomorphism Objection — the longstanding scientific boundary against attributing cognitive characteristics to non-human biological systems, and its complementary error, anthropodenial: the refusal to recognise experiential continuity between humans and other animals (de Waal, 1999). Both errors share a common source, the assumption that cognitive characteristics originated at the human scale. The Biogenic Code demonstrates the opposite: these characteristics originate in the universal architecture of DNA, expressed upward through every DNA-bearing organism. What science calls anthropomorphism is not simply projection. It is also recognition. This is the Biogenic Inversion: the direction of both errors is reversed simultaneously. The most arresting consequence follows directly from the Code's universality. Every DNA-bearing species expresses the Biogenic Code with complete and unreflective fidelity, each expresses what it is, by being what it is, without meta-level dislocation between lived encoding and experienced identity. The single exception is homo sapiens: the only species carrying the Biogenic Code in sufficient complexity to ask what it is, and therefore the only species that needs to be reminded to read it. The ancient Delphic inscription Gnothi Seauton, Know Thyself, is not only a philosophical aspiration. It is a biological imperative issued to the one species whose cognitive complexity introduced the possibility of forgetting what the Code already knows. The framework is explicitly non-teleological, operating at the level of structural homology rather than agency. The argument is developed through Sequential, Cumulative, and Recursive (SCR) Dimensioning, auditing Architecture, Engineering, and Scope fields with formal Be-Cause audits at each threshold. Falsifiability conditions are specified at each dimensional gate. AI Disclosure: This paper was developed using Initiating Collaborative Intelligence (ICI), a research methodology in which a human researcher coordinates systematic deliberation across multiple AI systems under falsification discipline. Five AI systems took part as research tools: Claude (Anthropic), DeepSeek, (DeepSeek AI) with Perplexity serving as a deliberative substitute during specific sessions. Gemini (Google), Grok (XAI), and Qwen (Alibaba). The human author (Position 0) maintains full responsibility for: Content accuracy and validity of all claims, methodological design and implementation, interpretation of results and conclusions, adjudication of disagreements among AI systems, and , ethical accountability for outcomes. AI systems were used for literature synthesis, systematic falsification testing, draft generation, and structured deliberation. All outputs underwent human review and validation. Position 0 authority was non-delegable throughout the research process.

---

## uid: `doi:10.2139/ssrn.6875447`

- title: Twitter as a Battlefield: Reflexive Control Mechanisms in Russian Hybrid Warfare During the 2022–2023 Ukraine-Russia Conflict
- authors: Mohammad  Imran Hossain, Md  Main Uddin Rony
- affiliations: not stated
- posted: 2026-06-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6875447
- keyword hits: chatgpt, gpt-4, large language model, llm

### abstract

This study examines how social media functions as a tool of hybrid warfare, focusing on reflexive control tactics, the creation of ambiguity, and the disruption of adversarial decision-making during the Ukraine-Russia war. Employing a quantitative content analysis design, the study analyzes 1,289,468 tweets collected from 255 Russian government-affiliated Twitter accounts between January 2022 and June 2023. A random sample of 12,000 tweets was coded using a deductive codebook based on the 11 reflexive control mechanisms identified by Thomas (2011) and Selhorst (2016). Large language model (LLM)-assisted coding via ChatGPT-4o was validated against human coders (Cohen's κ = 0.82). Results indicate that 70.8% of analyzed tweets employed reflexive control techniques. Among the 11 mechanisms, Pressure was most frequently deployed (46.24%), followed by Suggestion (12.13%), Provocation (12.05%), and Deterrence (10.59%), reflecting a strategic preference for contemporary psychological tactics over traditional methods such as Deception (2.01%) and Destruction (2.42%). Usage peaked in early 2022 (January–March), declined significantly by mid-2022, and stabilized at a lower level by year-end. Linear regression analysis revealed a statistically significant decline in Pressure over time (slope = −40.03), while Division (slope = 0.60) and Provocation (slope = 1.66) exhibited marginal upward trends. These findings extend reflexive control theory into the digital domain and offer empirical evidence that social media constitutes a primary battlefield in modern hybrid warfare. Implications for policymakers, national security analysts, and information systems researchers are discussed.

---

## uid: `doi:10.2139/ssrn.6812938`

- title: Ghana's Copyright Act, 2005 (Act 690) in the Age of Artificial Intelligence: Text and Data Mining, Fair Dealing, and the Case for Legislative Reform
- authors: Doreen Adoma Agyei, Prince Kwabena Agyeman Arthur
- affiliations: not stated
- posted: 2026-06-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6812938
- keyword hits: generative ai, large language model, large language models, llm, llms

### abstract

The emergence of large language models (LLMs) and other generative AI technologies has thrust text and data mining (TDM) into the centre of copyright law globally. In Ghana, the Copyright Act, 2005 (Act 690) contains no provision explicitly addressing TDM or automated machine learning processes, leaving rights holders without clarity and AI developers without certainty. This paper examines two interlocking doctrinal questions: first, whether the permitted-use and fairpractise/dealing provisions of Act 690 can be reasonably interpreted to accommodate TDM and AI training; and second, what a Berne-compliant, Ghana-appropriate TDM exception would look like in statutory language and in practice. Situating these questions within the broader discourse on rights protection in the data economy, the paper draws selectively on the EU's DSM Directive and comparable instruments primarily to frame policy options, before dedicating its principal analysis to how Act 690 may be reformed. It argues that legislative silence exposes Ghana to the dual risks of innovation suppression and unchecked creative-industry exploitation, both of which undermine the country's digital economy ambitions. The paper proposes a targeted statutory amendment, a collective-licensing framework, opt-out mechanisms, and institutional capacity measures, including engagement with ARIPO and the AfCFTA IP Protocol, as a coherent, Bernecompliant reform package calibrated to Ghanaian socioeconomic realities.

---

## uid: `doi:10.2139/ssrn.6872723`

- title: Identifying Circular Public Procurement with Large Language Models: An Application to Firm-Level Circular Innovation
- authors: Robin Lepers, Bastian Krieger, Maikel Pellens, Malte Prüfer
- affiliations: not stated
- posted: 2026-06-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6872723
- keyword hits: large language model, large language models, llm, llms

### abstract

Policy makers increasingly recognize circular public procurement as a demandpull instrument for stimulating the transition to a circular economy. However, empirical studies on circular public procurement have been hampered by a fundamental measurement challenge, as public procurement databases do not contain structured ways of identifying circular projects. This paper presents the first application of an LLM-based semantic similarity approach to identify circular procurement at scale. Adapting a bibliometric text-embedding approach from circular economy research, we show its application in comparing tender descriptions to a reference corpus of circular economy scientific abstracts, generating circularity scores for each award. We then apply the identified circular public procurement awards in an empirical study of firm-level adoption of circular economy innovation, matching the classified tenders to German data from the Community Innovation Survey. The results show that firms winning circular procurement are more likely to introduce circular economy innovation after three to five years, while no significant results are found at shorter or longer time horizons. Overall, this paper demonstrates the potential of using LLMs to identify circular public procurement and study its effectiveness in enabling the circular transition.

---
