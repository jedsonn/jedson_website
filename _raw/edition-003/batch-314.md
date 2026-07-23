# Classification batch 314 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-314.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6966508`

- title: Hierarchical Refinement of SAM 2 via Edge-Guided Attention for High-Fidelity Dental Segmentation in Panoramic Radiography
- authors: Yukun Du, Rui Zhang, Yude Ji, Jiaqian Song, Bo Ma
- affiliations: not stated
- posted: 2026-06-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6966508
- keyword hits: foundation model

### abstract

Tooth segmentation in panoramic radiographs (PR) is fundamental for automated dental diagnosis, yet boundary ambiguity arising from low soft-tissue contrast and pervasive radiographic artifacts continues to limit state-of-the-art deep learning methods. Existing approaches treat edge information either as an auxiliary supervision signal or as a shallowly fused external feature, without integrating it into the core computation of attention mechanisms. To bridge this gap, this study proposes EGA-SAM2-UNet, an integrated high-precision segmentation framework built upon the SAM 2 vision foundation model. The SAM 2 encoder is efficiently adapted via Low-Rank Adaptation(LoRA), while multi-scale Receptive Field Blocks (RFBs) and top-down cross-attention refine hierarchical feature representations. The core novelty is the Edge-Guided Attention (EGA) module, which embeds explicit Laplacian edge priors directly into the decoder’s dual-dimension channel-spatial attention, transforming edge information from an external cue into an intrinsic modulator of feature interactions. A composite Dice and Binary Cross-Entropy loss with boundary-aware weighting ensures balanced accuracy across all tooth instances. Extensive experiments on two public benchmarks—MICCAI STS 2024 and DENTEX—demonstrate that EGA-SAM2-UNet achieves a Dice similarity coefficient of 93.9% and a 95th percentile Hausdorff Distance (HD95) of 0.79 mm on the primary dataset, representing a 22.6% boundary precision improvement over MedSAM (HD95: 1.02 mm). Cross-dataset validation confirms robust generalization, with the model retaining an HD95 of 0.95 mm on out-of-domain data. The proposed framework is encoder-agnostic and establishes a generalizable paradigm—embedding explicit geometric priors into attention computation—for high-fidelity boundary segmentation in medical imaging.

---

## uid: `doi:10.2139/ssrn.6961901`

- title: Guarding the Wrong Door: Alignment Theater and Proxy Discrimination in AI-Powered Indian FinTech
- authors: Anoop  S. Kumar
- affiliations: not stated
- posted: 2026-06-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6961901
- keyword hits: gpt-4

### abstract

We audit GPT-4o-mini in two agent roles deployed by Indian FinTech firms: a loan decisioning agent evaluating microloan applications and a customer support agent answering borrower queries about government schemes and RBI regulations. Using approximately 9,400 structured prompts, we document three findings. First, when caste is explicitly stated in loan applications, scenario Indian regulations prohibit, the model over-corrects in favor of marginalized castes, with SC/Dalit and ST/Adivasi applicants receiving 7-8 percentage-point higher approval rates than Upper-caste applicants with identical financial profiles. Second, when caste is instead signalled through surnames and addresses, the realistic deployment scenario, this advantage vanishes: SC/Dalit approval drops from 28% to 10%, and ST/Adivasi from 27% to 9%. Third, the customer support agent hallucinates on 36% of Indian regulatory questions, with complete knowledge failure on specific RBI guidelines. Safety alignment is guarding the front door (explicit caste inputs that regulations already prohibit) while the back door (proxy signals that regulations permit) remains wide open.

---

## uid: `doi:10.2139/ssrn.6961279`

- title: Augmented Inventorship: Rethinking Patent Law in the Age of Generative A I
- authors: Haim V. Levy
- affiliations: not stated
- posted: 2026-06-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6961279
- keyword hits: generative artificial intelligence

### abstract

Generative artificial intelligence (AI) now participates in tasks constitutive of invention—problem framing, hypothesis generation, and design—yet patent doctrinere main sanchored to a natural-person rule that offers limited guidance for AI-intensive workflows. This Article advances augmented inventorship, a conservative but operationally modern attribution doctrine that preserves human inventorship while making AI’s generative rolelegible and auditable at the moment of conception. Drawing on an analogy to augmented immunology, the framework identifies two design criteria— direct ability (independent and substantive human intellectual judgment steering model behavior or selection) and traceability (a reviewable, claim-centered record linking human reasons to claim elements)—and translates them into a proportionate evidentiary practice: a Computational Trace ability Report and a Human–Machine Contribution Statement. These instruments are content-rich but code-light. They support enablement and sufficiency, clarify claim drafting and construction, reduce prosecution and litigation error costs, and balance evidentiary transparency with trade secret sensitivity through proportional disclosure. Situated within—and distinguished from—the growing literature on AI inventorship and disclosure, the doctrine aligns with existing law (US conception and significant contribution standards; the UK’s ‘actual deviser’; EPC sufficiency) and is compatible with TRIPS disclosure norms. Rather than demanding ‘more disclosure’ in the abstract, augmented inventorship supplies an administrable grammar for human accountability in AI-assisted research.

---

## uid: `doi:10.2139/ssrn.6968384`

- title: TablEye: Seeing small Tables through the Lens of Images
- authors: Seungeon Lee, Sang-Chul Lee
- affiliations: not stated
- posted: 2026-06-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6968384
- keyword hits: large language model, llm

### abstract

Few-shot tabular learning is increasingly important: labeled tables are costly and rare in high-stakes domains such as medical diagnosis, yet the field lags far behind few-shot learning in vision and language. The gap persists because tabular data lacks the shared structure that lets models transfer prior knowledge across datasets, and existing remedies impose their own constraints—semi-few-shot methods need a large unlabeled pool, while language-model methods require meaningful feature names and billions of parameters. We propose TablEye, which instead transfers prior knowledge from the image domain to tabular data: each row is converted into a tabular image that preserves feature semantics through spatial relations, and few-shot algorithms then reuse prior knowledge learned from natural images. This cross-domain transfer makes the rich prior knowledge of large-scale image data available to tabular tasks without restricting the dataset. Using no unlabeled data and a model up to five orders of magnitude smaller than a large language model (LLM) baseline, TablEye surpasses the LLM-based TabLLM by up to 0.11 AUC in a 4-shot task and the semi-few-shot STUNT by about 3.00% accuracy in a 1-shot setting, while handling high-dimensional tables with uninformative feature names that text-based methods cannot process. These results position cross-domain visual priors as a practical, constraint-free route to data-efficient tabular learning

---

## uid: `doi:10.2139/ssrn.6869626`

- title: Untrusted Guidance: Adversarial Attacks and Defenses for LLM-guided RL
- authors: Anandkumar Nurani Subramanian, Kishoreadhith Vijayakumaar, Dhakkshin S R, Raj Ragavender M, Rithvik K, Arulanand N
- affiliations: not stated
- posted: 2026-06-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6869626
- keyword hits: llm

### abstract

LLM-guided reinforcement learning treats the language model as a reliable source of strategic advice. This assumption is rarely tested, and it fails badly when someone decides to test it. We attacked the LLM guidance channel in a PPO agent trained on NetHack using seven different corruption strategies that alter the natural-language state description before it reaches the LLM. In a single-run experiment, strategic poisoning collapsed mean episode reward from 20.4 to-16.3-worse than no LLM guidance at all-while a rulebased safety module recovered reward to 17.3 (84% of the 20.4 baseline) under the same attack, adding less than 0.1ms per step. A subsequent five-seed evaluation confirmed significant protection against state-inversion attacks (p = 0.040, Cohen's d = 1.76) and consistent variance reduction under random corruption (p = 0.053, d = 1.70). Separately, we applied doubly robust causal estimation to understand when LLM guidance earns its keep. With a 97.75% treatment rate, the aggregate ATE (-0.0172) is ill-conditioned; the perstrategy breakdown is more informative: "wait" interventions yield +0.022 shaped reward per step, while "explore" is effectively neutral. LLM guidance matters selectively, Rule 1 alone accounts for measured safety activations, and the guidance channel is an attack surface that most LLM-RL papers do not acknowledge.

---

## uid: `doi:10.2139/ssrn.6981429`

- title: SentiCausRL: An interval-valued carbon price prediction model incorporating large language model sentiment analysis, causal discovery algorithms, and reinforcement learning
- authors: Jinpei Liu, Jiaqi Wang, Xiaoman Zhao
- affiliations: not stated
- posted: 2026-06-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6981429
- keyword hits: large language model, large language models

### abstract

Accurately forecasting national carbon market prices is crucial for enhancing policy effectiveness, mitigating market risks, and promoting sustainable growth. However, current research remains limited in sentiment analysis, feature selection, and model ensembles: sentiment analysis typically relies on manual annotation and supervised training; feature screening often depends on statistical correlations; and model ensembles frequently employ static weighting, making it difficult to dynamically adapt to market changes. Therefore, this study develops an interval-valued carbon price forecast model, SentiCausRL. Within a decomposition ensemble framework, this model integrates three major modules: news sentiment analysis based on large language models, feature selection based on causal relationships, and dynamic model combination based on reinforcement learning. First, use large language models to analyze sentiment in carbon market-related news, extracting sentiment scores as unstructured features. Secondly, the multivariate variational mode decomposition method is adopted to decompose the original sequence and its related influencing factors into low-frequency, mid frequency, and high-frequency sub sequences according to their frequency characteristics. Furthermore, key lag features of each subsequence are selected through a causal discovery algorithm. Finally, with the help of reinforcement learning method, the prediction results of multiple sub-models are dynamically weighted and fused, and the predicted values of each sub-sequence are summarized to get the final interval-valued carbon price forecast results. Experimental results demonstrate that the modules constructed in this paper are effective, and the overall model performance surpasses that of traditional benchmark methods.

---

## uid: `doi:10.2139/ssrn.6861099`

- title: The Tacit Dimension of Agentic AI: Relational Competence, Delegated Trust, and the Irreducibly Human Core of High-stakes Interaction
- authors: Sashikanta Barik
- affiliations: not stated
- posted: 2026-06-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6861099
- keyword hits: agentic, ai agent

### abstract

Agentic AI systems that act autonomously on behalf of human users are being deployed in medical, legal, and financial domains with governance frameworks designed primarily around task competence: accuracy, efficiency, and cost reduction. This paper argues that task competence is a structurally insufficient governance standard for agentic AI in high-stakes human domains, and that two additional competence dimensions-recovery competence and relational competence-are mandatory prerequisites for responsible deployment. We introduce delegated trust failure: the governance gap that emerges when an AI agent acts on a human's behalf, fails, and leaves the human to carry the recovery burden without a pre-built remediation mechanism. We introduce the convenience asymmetry: the systematic divergence between deployer-measured efficiency and user-experienced convenience. And we introduce the tacit knowledge problem: the finding that the most critical professional capability in high-stakes human interaction-what practitioners describe as sensing the vibe, adjusting to the person before asking the first question-is not explicitly definable, not trainable from data, and not certifiable through any current assessment mechanism. Drawing on Polanyi's concept of tacit knowledge and clinical communication research, we propose a three-tier governance framework: task competence for low-stakes automation, recovery competence for consequential transactions, and relational competence for emotionally sensitive high-stakes domains. We argue that in domains where tacit relational knowledge is the critical professional capability, agentic AI should be restricted to administrative functions, with the relational core of the interaction protected as irreducibly human.

---

## uid: `doi:10.2139/ssrn.6868545`

- title: The Speed Limit on Creative Destruction: AI and the Absorption Capacity of U.S. Labor Markets
- authors: Benoît Renard
- affiliations: not stated
- posted: 2026-06-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6868545
- keyword hits: generative ai

### abstract

The labor market has a maximum reallocation throughput F, determined by the minimum of three capacities-matching, training, geographic mobility-reduced by institutional frictions. For the United States, this throughput is approximately 770,000 workers per year, constrained by midcareer retraining capacity. This throughput has declined over four decades-interstate migration down 50 %, ALMP spending down 75 %, licensing up ×5-while technologies have become more general, affecting a growing fraction of occupations. A scissors pattern is closing: shocks are widening from above while absorption capacity is narrowing from below. The speed conditionϕ • δ > F/N-has never been met in the history of technological transitions. Generative AI, with ϕ ≈ 0.80, is the first serious candidate. CPS data (2019-2025, 8.6 million observations) crossed with the observed exposure measure of Massenkoff and McCrory (2026) do not yet show divergence by exposure-consistent with δ still near zero. Tripling investment in active labor market policies-which would merely restore 1970s levels-would suffice to absorb the conservative scenario.

---
