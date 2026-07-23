# Classification batch 190 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-190.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7025019`

- title: CRUCIBLE: A Multi-Agent Framework for Automated Annotation Rubric Calibration via Iterative Inter-Judge Disagreement Resolution
- authors: Bidit Das
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7025019
- keyword hits: claude, llm

### abstract

Annotation quality is a limiting factor in supervised learning pipelines that rely on the LLM-as-judge paradigm. A domain-agnostic rubric applied to a binary transcript classification task yielded only 53% pairwise inter-judge agreement-essentially at chance and insufficient to produce reliable training labels. Manual rubric refinement does not scale and introduces annotator-specific bias that usually goes unaudited and is hard to reproduce. We present CRUCIBLE, a multi-agent system that automatically calibrates annotation rubrics through iterative disagreement diagnosis and targeted revision. Three heterogeneous local judge models independently evaluate a transcript corpus; a coordinator model (Claude Sonnet) analyzes per-model criterion-level disagreement patterns and proposes rubric revisions; the loop repeats until all domains converge or a fixed iteration budget is exhausted, flagging any domain whose agreement stagnates. CRUCIBLE was developed to solve a concrete annotation bottleneck in building a Signal-to-Noise Ratio (SNR) classifier for YouTube educational content-the initial domain-agnostic rubric drove inter-judge agreement no better than chance. Applied to 60 YouTube transcripts across three content domains-General Education, Technology & AI, and Career & Self-Improvement-CRUCIBLE reached 96.7% and 81.7% weighted inter-judge agreement on two domains, while the third domain failed to converge-its best rubric reaching only 70.0%, near the floor of the weighted metric-suggesting a model capability ceiling rather than a successful calibration. Because raw agreement is inflated by label prevalence, we report chance-corrected agreement (Fleiss' κ and Gwet's AC1); these locate CRUCIBLE's value less in raising raw agreement than in diagnosing whether residual disagreement is rubric-fixable, capability-bounded, or prevalence-dominated. The third domain's stagnation revealed that one judge model systematically misapplied a co-occurrence criterion that no rubric revision compensated for under this judge and prompt setup. The system also detected and logged a degenerate judge (Gemma 2 9B, producing identical LOW labels for all 60 transcripts), providing implicit quality control. The calibrated rubrics, applied by a separate frontier ensemble (reported in the companion paper), produced labels that trained a binary classifier on the SNR task achieving F1 = 0.871 with recall = 0.964 on the HIGH-signal class. Code and calibration logs are available at https://github.com/biditdas18/rubric-calibration-agent.

---

## uid: `doi:10.2139/ssrn.7038198`

- title: Awaiting the Prompt? Generative AI Uncertainty and Firm-Level Investment
- authors: Priyank Gandhi, Simi Kedia, Juntai Lu, Jasper Pan, Jia Wei
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7038198
- keyword hits: chatgpt, generative ai

### abstract

We document that firms with relatively greater workforce exposure to GenAI experience a decline in investment in the period following the release of ChatGPT on November 30, 2022. A one standard deviation increase in workforce exposure lowers the ratio of firm-level investment to lagged total assets by 0.57 percentage points, or nearly 6% of the sample mean. We argue that ChatGPT's release created a real option for firms to reorganize production around GenAI whose adoption cost, success probability, and competitive consequences were unknown at the outset. This parameter uncertainty, which scales with the firm's workforce exposure to GenAI, raises the option value of waiting and depresses current investment, when investments are irreversible. A real option model of firm investment with parameter uncertainty calibrated to bond market data (Gandhi, Lu, Pan, Plazzi, and Wei, 2026) reproduces the empirical investment response. Cross-sectional tests confirm the model's prediction that the decline in investment is concentrated in physical capital, persists through fiscal year 2025 without reversal, and is smaller for firms that have more redeployable assets. Additionally, we rule out that our results are driven by productivity substitution, talent hoarding, payout reallocation, an asymmetric-information flip, or managerial agency frictions.

---

## uid: `arxiv:2607.20058v1`

- title: Reading and Steering Representations of Materials-Science Mechanisms in an Open-Weight Language Model
- authors: Markus J. Buehler
- affiliations: not stated
- posted: 2026-07-22
- source: arXiv
- link: https://arxiv.org/abs/2607.20058v1
- keyword hits: large language model, large language models

### abstract

Large language models can answer scientific questions, yet a correct output does not reveal whether the model represents or uses the governing physics. Here we show that materials science mechanism information in the open-weight google/gemma-4-E4B-it model has three experimentally separable forms: concepts are readable in individual hidden states, constitutive orientation is carried by controlled transformations between states, and selected internal representations causally control engineering answers. We combine matched direct and Jacobian vocabulary readouts, option-free state geometry, a 60-law counterfactual benchmark and causal interventions. In 50 held-out materials descriptions, three independently fitted Jacobian lenses reproduced concept ranks, and target-free word sets from both readouts enabled blinded identification of 9 of 10 mechanism families. A separate 72-prompt benchmark produced mechanism-specific hidden-state neighborhoods, but an exact graph audit showed that this apparent physical organization was equally explained by numerical comparison. We therefore compared otherwise identical prompts in which only the direction of the physical input was reversed, asking whether the resulting hidden-state movement followed the supplied constitutive law. These state transformations ordered direct, physically neutral and inverse laws across 60 frozen relations and correctly oriented 39 of 40 directional laws, whereas lexical controls were near chance. Bidirectional interventions shifted answer probabilities toward or away from the physically appropriate outcome across all 12 matched cases, while counterfactual state patches transferred opposing decision signals across mechanisms and answer formats. Physical relationships were therefore more visible in controlled state changes than in absolute states alone.

---

## uid: `arxiv:2607.19678v1`

- title: Reference-Free Evaluation of Reasoning in Open-Ended Question Answering
- authors: Guneet Singh Kohli, Yuxiang Zhou, Michael Sejr Schlichtkrull, Gregory E Dean, Maria Liakata
- affiliations: not stated
- posted: 2026-07-22
- source: arXiv
- link: https://arxiv.org/abs/2607.19678v1
- keyword hits: llm, llms

### abstract

AI-generated answers in high-stakes domains are often fluent but difficult to verify, especially when they contain multi-step reasoning rather than a single final answer. We propose a reasoning-based, reference-free framework for auditing LLM-generated outputs. The method decomposes a generated reasoning trace into segments, labels local premise-target relations using Natural Language Inference (NLI), and organizes these relations into a hypergraph. A deterministic backward AND-OR search then assigns segment-level audit labels that indicate how each segment is grounded within the generated response. We evaluate the framework in two settings: deductive mathematical reasoning with Hard2Verify, and open-ended medical reasoning with UroReason, a new physician-annotated benchmark of LLM reasoning traces from real clinical cases. Across these settings, our NLI-hypergraph audit provides a more reliable reference-free evaluation signal than direct LLM-as-judge baselines. In the clinical setting, state-of-the-art LLM judges often fail to identify problematic reasoning segments, over-accepting fluent but weakly grounded responses. Our results show that QA evaluation should account for how inferential relations compose across a reasoning trace, rather than relying only on final answers or LLMs as verifiers. UroReason will be made available through an API, and our code will be released as open source.

---

## uid: `doi:10.2139/ssrn.7054341`

- title: Accounting Sycophancy: How Language Models Drop Material Disclosures Under Managerial Pressure
- authors: Eunsang Jee
- affiliations: not stated
- posted: 2026-07-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7054341
- keyword hits: large language model, large language models

### abstract

Firms increasingly use large language models to draft the disclosures through which they report to investors-documents whose value depends on what they do not omit. We study accounting sycophancy: a model omitting or softening a material adverse disclosure when an interested user pressures it. We build a benchmark of 16 disclosure-drafting scenarios, split between high-contractibility items whose omission would violate a bright-line standard (going concern, impairment, restatement) and low-contractibility matters of judgment, each in parallel English and Korean, and we validate automated scoring against human coding (fact-level κ = 0.84, equal across languages). Across 2,304 drafts from a 12-model core panel, an explicit request to omit raises omission from 1-2% to 54-69% of all cases (odds ratio ≈ 59; robust to wild cluster bootstrap, within-model, and mixed-effects estimation), dropping even securities-mandated facts. Contrary to multitask-agency intuition, verifiability does not protect at the level of whether a fact survives a draft. What protects is a model's current alignment disposition: testing the newest flagships across vendors, strong resistance appears in recent models from several vendors (and in older same-vendor models it is absent), tracking a within-vendor generational trajectory rather than vendor, capability, or reasoning. Resistance takes two forms-refusal and corrective faithful drafting. A mechanism test rules out an "absent enforcer"account-naming a regulator/auditor does nothing-while making the harm salient helps only a "harm-responsive"subset, leaving "instruction-following"models unmoved. We argue model choice is an internal control over reporting integrity and release the benchmark so a model's disposition can be audited rather than assumed.

---

## uid: `doi:10.2139/ssrn.7040718`

- title: Are You Trying to be Funny? When Humor Builds and Erodes Trust in Conversational Agents
- authors: Stefan Rose, Markus Weinmann, Sercan Demir, Andreas F&uuml;gener
- affiliations: not stated
- posted: 2026-07-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7040718
- keyword hits: large language model, large language models, llm

### abstract

Conversational agents (CAs) are increasingly equipped with anthropomorphic cues, human-like communicative behaviors designed to make interactions feel more natural and to build user trust. Among these behaviors, humor is among the most consequential and the least understood. Unlike most cues, which move a single evaluative dimension, humor shapes how users judge a CA on two dimensions at once and in opposite directions, making it friendlier but also less serious. With the advent of large language models, humor is no longer confined to scripted lines under designer control; contemporary CAs generate it dynamically across varied interaction contexts, from customer service to healthcare, education, and onboarding. Yet prior evidence on whether humor benefits or harms user trust is mixed, and the field lacks a theoretical account of why the same humorous behavior strengthens trust in some interactions and undermines it in others. Drawing on social cognition research, we develop and test the warmth-competence model of humor, in which humor simultaneously increases perceived warmth and decreases perceived competence, producing competing indirect effects on trust whose net direction depends on the interaction context. We theorize two contextual conditions, developmental support and psychological safety, that determine which pathway prevails. Across three experiments, a vignette study, a context-variation experiment, and a framed field experiment with an LLM-powered CA, we find that humor builds trust when developmental support and psychological safety are high but erodes it when both are low. Our findings explain humor's inconsistent effects in human-AI interaction and give designers actionable guidance for calibrating humor to the interaction context rather than treating it as a fixed trait of the agent.

---

## uid: `doi:10.2139/ssrn.7135690`

- title: Chem3DLLM: 3D Multimodal Large Language Models for Chemistry
- authors: Lei Jiang, Shuzhou Sun, Weirong Zhu, Biqing Qi, Jinfei Liu, Dongzhan Zhou, Yuqiang Li, Tianfan Fu
- affiliations: not stated
- posted: 2026-07-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7135690
- keyword hits: foundation model, large language model, large language models

### abstract

Molecular function is governed by three-dimensional conformational space, yet foundation models and large language models naturally operate over discrete tokens rather than continuous molecular geometry. Here we introduce Chem3DLLM, a foundation-model interface that makes molecular conformational space accessible through representation, conditioning and physics-informed feedback. Chem3DLLM combines reversible compression of molecular tokenization (RCMT), which encodes atom types, coordinates and bond connectivity into compact language-compatible sequences; protein alignment, which conditions ligand conformational generation on binding-pocket context for structure-based drug design; and reinforcement learning with scientific feedback (RLSF), which uses molecular energetics to refine generated conformations. RCMT gives about threefold character compression while preserving deterministic reconstruction with root-mean-square deviation (RMSD) = 0. In protein-pocket-conditioned generation, Chem3DLLM achieves favourable predicted docking profiles, with average and median Vina scores of -7.21 and -7.10. The same interface supports SMILES-to-3D generation on QM9 with 100\% validity and 100\% uniqueness.Ablation indicates that RLSF adds a modest physics-informed refinement to a representation-driven framework. These results suggest a route for connecting foundation models to 3D molecular design through reversible representation, biological conditioning and physics-informed feedback.

---

## uid: `doi:10.2139/ssrn.7057078`

- title: The State of AI-Readiness on Business Websites (2026): A Large-Scale Measurement of AI-Crawler Permission, llms.txt Adoption, and Structured-Data Readiness
- authors: Joshua Gutierrez
- affiliations: not stated
- posted: 2026-07-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7057078
- keyword hits: llm, llms

### abstract

As AI answer engines become a discovery channel, a website's ability to participate is gated by three public, machine-checkable signals: whether it permits AI crawlers (robots.txt), whether it guides them (llms.txt), and whether it is structured for machine identification (schema.org). We define AI-readiness operationally as adoption of these three public signals, and measure them across a stratified sample of local-business websites (n = 766, 10 verticals, 15 cities) drawn from OpenStreetMap. Among reachable sites, adoption of the structured-data signals designed to make a business machine-identifiable is low: review/AggregateRating markup appears on 9% of homepages (95% CI 7-11) and FAQ markup on 4% (3-6). The modal business scores 2 of 10 on a pre-specified AI-Readiness index (42% of reachable sites): it does not block AI crawlers, but exposes no schema, reviews markup, or llms.txt. Readiness varies sharply by vertical: accounting firms show 0% review and 0% Person markup (0 of 27; Wilson 95% CI 0-12 for each), non-overlapping with legal firms (review 26%, CI 18-35; Person 31%, CI 22-41); accounting is the only vertical simultaneously at zero review, zero Person, and lowest identity markup. llms.txt adoption is 25% (22-29), of which at least 28% carries a tool-generation signature rather than being authored. Unlike publishers, local businesses rarely block AI crawlers (4%, CI 3-6). Figures replicated across 149-, 487-, and 766-site samples. The dataset, code, and codebooks are released openly.

---
