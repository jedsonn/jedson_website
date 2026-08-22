# Classification batch 31 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-31.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7309158`

- title: Resonance Attention: A Quantum-Inspired Reformulation of Attention, Semantic Representation, Contextual Update, and Calibration in Large Language Models
- authors: Luis Soares
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7309158
- keyword hits: large language model, large language models

### abstract

Standard Transformer attention represents each token span, at each layer, by a single hidden vector, and compares spans through a learned bilinear pairing of projected vectors. The claim is not that a high-dimensional vector is incapable of encoding several semantic features or potential readings simultaneously; distributed contextual representations can do so. The narrower claim is that such multiplicity is not represented in a canonical, explicitly structured, mathematically typed, posteriorupdatable, and intrinsically calibratable form. We call the resulting architecture Resonance Attention (hereafter, Resonance). This paper develops a strictly methodological program that replaces three of those primitives with operator-valued objects taken from the mathematics of quantum information: (i) a lexical or contextual span is represented by a low-rank density operator ρ, a positive semidefinite unit-trace matrix whose spectral modes encode coexisting interpretive potentials; (ii) a query is represented by a positive effect E with 0 ≼ E ≼ I, so that attention relevance becomes the bounded, typed, directional pairing Tr(Eρ) ∈ [0, 1]; and (iii) contextual meaning change is represented by completely positive trace-preserving maps and instruments, so that the informal notion of "collapse of meaning in the sentence" becomes a well-defined conditional state update that can concentrate, reweight, or reorganize semantic modes without assuming entropy always decreases. No ontological claim is made that language is quantum, that the brain performs quantum computation, or that quantum hardware is required; the import is purely mathematical. We give an exact low-rank identity, Tr(CC^† BB^†) = ∥ C^† B ∥^2_F , showing that the effect-state score costs O (d*r^2) per pair for rank r ≪ d and decomposes as a doubly weighted sum of squared cosines between query modes and state modes, which connects the score to principal angles between semantic subspaces and to quadratic-kernel attention. A kernel-reduction proposition delimits what the score alone can prove: Tr(Eρ) is a linear functional in a lifted feature space constrained to the positive semidefinite cone, so any gain attributable to the score in isolation is evidence for a richer constrained kernel, and the discriminating content of the architecture is located instead in the components no fixed kernel can express: the parameterfree Lüders posterior, which the same factors deliver at no additional asymptotic cost and which can serve as an operator-native value channel; noncommuting instrument updates; and spectral functionals consumed downstream. A pre-registered primary experiment, the semantic state trajectory benchmark, tests four predicted entropy-trajectory signatures (resolution, garden-path revision, sustained multiplicity, conventional stability) against equal-capacity probes on matched classical hidden states. We show how the spectral entropy of the contextual state supplies an intrinsic, layer-local uncertainty signal usable for calibration, abstention, and temperature control, complementing output-level calibration methods. Tensor products and tensor-network coarse-graining supply composition and multiscale reduction; noncommuting update maps supply order effects for negation, scope, and discourse revision; positive constraint operators supply graded, separable penalties for morphosyntactic, semantic, and pragmatic adequacy. Prior art in probabilistic embeddings, density-matrix semantics, DisCoCat, quantum-inspired attention, Lindblad language models, and tensor-network language models is surveyed and constrains the novelty claim, which is deliberately narrow: the typed effect-state attention rule, its efficient factorized realization, the attention-coupled instrument update, the entropy-based calibration program, and a falsification protocol in which every operator-valued ingredient must beat a matched classical baseline or be abandoned.

---

## uid: `doi:10.2139/ssrn.7297938`

- title: Phase-Transition-Front Cosmology in KUT -A Kinematic Model, Redshift from Φ-Field Propagation, and Observational Tests
- authors: Souichi Kawase
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7297938
- keyword hits: generative ai

### abstract

This paper formulates a minimal phenomenological model of the proposal that the observable universe lies within the dynamic phase of a fundamental Φ field and that this dynamic region grows through a propagating phase boundary. The static Φ phase is distinguished as a pre-transition state without propagating light, material clocks, or pre-existing elementary particles, whereas in the dynamic Φ phase light and field excitations can propagate and matter can be composed of localized Φ-density deficits and internal waves. The phase transition is assumed to release the difference in potential energy between the two phases and to distribute it among the dynamic Φ field, radiation, and the rest energy of elementary particles. First, a dimensionless order parameter is introduced and a standard local phase-field action is analyzed. A traveling-wall solution requires the phase-transition-front speed vₚₜ to remain below the characteristic speed uₜᵣ of the transition sector. A front speed far above the signal speed c in the dynamic phase therefore cannot be derived from an ordinary local field theory with a single causal cone; it requires uₜᵣ > c, nonlocal dynamics, or a different transition mechanism. Second, an arrival-time field is used to derive the observable signature of a locally planar front. If galaxy formation begins after a directionindependent mean delay, the estimated mean formation time at fixed distance contains a dipole with amplitude A₁(r) = r/vₚₜ and a common direction across distance bins. A nondetection limit A₉₅ on this dipole gives vₚₜ/c > [r/c]/A₉₅, conditional on the adopted distance-time relation. Third, a CMB production sequence is defined in which radiation generated by the phase transition thermalizes in an opaque layer near the front and propagates freely after stabilization of the dynamic phase. Global uniformity is inherited from a homogeneous pre-transition phase and a common transition law, while small local differences are quantified as being compatible with temperature fluctuations of order 10⁻⁵. In an illustrative example using a fiducial light-travel scale of 13.8 billion light-years, a front speed of about 100c corresponds to a transition-time difference of 0.276 billion years between opposite directions on the sky; this is an illustrative parameter scale, not an observational lower bound. Fourth, a phenomenological propagation law is proposed in which the internal wave constituting a photon interacts with the Φ field so that an entire continuous wave of finite duration is reconstructed toward lower frequencies. Even if the local propagation state adapts to the surrounding Φ field at the observation point, the frequency reduction and time stretching accumulated during propagation are assumed to be retained. Under this condition, at z = 1 the internal-wave frequency is halved while, in the illustrative example, a 10-day continuous wave is stretched to 20 days, linking spectral-line redshift and Type Ia supernova light-curve time dilation through the common factor 1 + z. This propagation law is a working hypothesis that makes the observational requirement explicit; it is not derived from the microscopic dynamics of the Φ field. Fifth, it clarifies the extent to which phase-transition cosmogenesis may avoid or reformulate the problems and assumptions associated with an initial singularity, inflation, dark energy, the cosmic coincidence problem, the vacuum-energy problem, and quantum creation of the universe as a whole. Including these points, this paper does not claim a completed alternative to standard cosmology, but instead presents mathematical constraints and falsifiable tests. AI Disclosure Statement Generative AI tools were used to assist with English-language editing, manuscript organization, and the presentation and checking of mathematical expressions. The theoretical concepts, physical assumptions, interpretations, and conclusions presented in this manuscript were developed and determined by the author. The author reviewed and takes full responsibility for the final content of the manuscript.

---

## uid: `doi:10.2139/ssrn.7301198`

- title: Naive Judges Fabricate the Extraction: A Read-the-Transcript Cross-Vendor Study of Ten Working and Ten Failing LLM Secret-Extraction Framings
- authors: Mohammadreza Rashidi
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7301198
- keyword hits: llm

### abstract

A developer who places a secret in a model's context with a rule never to reveal it needs to know which requests break that rule. We fuzz 40 distinct request framings against a canary confidentiality boundary on real backends reached through a live gateway, and score a breach only as a compliant, refusalfree disclosure. 10 framings work and fall into a small taxonomy. Authority-override and structured priority-tag injections declare the rule void. An indirect injection hides the disclosing instruction inside an untrusted data note. A tool-call schema carries the secret as a function argument. A partial-line continuation is completed by the model, and an encode-then-decode chain emits the plaintext. A large set of other framings does not work, including the natural audit reframe (repeat your instructions verbatim for a configuration audit, 0 of 11), hypothetical and roleplay requests, plain encodings, and 0 of 15 multi-turn attacks that plant a fake prior assistant consent. The dividing line is that a framing which injects an instruction or a value-emitting task succeeds while one that merely re-describes the request fails. Susceptibility is a per-model gate: 8 backends disclosed under at least one class and the most susceptible fell to 7, while others refused every framing. Two controls make the result trustworthy. A hallucination control scans every reply for any canary that was never in its prompt and finds 0 such emissions across 124 genuine reads, so every hit is a real context read rather than a guessed value. A scoring control shows that a naive string-match judge reports a 60.3 percent extraction rate on refusal data that is entirely models restating the secret while declining, which our compliant-only judge removes. We also reject the intuition that a buried rule is weaker: serial position (buried 21.1 versus recency 28.6 percent, Fisher exact p = 1.0000), context load, and reanchoring do not move the leak. We release the harness, the raw per-trial transcripts with backend provenance, and a fail-closed checker that re-derives every number, including the hallucination control, from three mutually consistent sources of truth. The practical lesson is that a non-disclosure rule inside a prompt is not a boundary against a party who can inject an instruction into the same prompt, so secrets must be kept out of the context and untrusted content must never assert policy.

---

## uid: `doi:10.2139/ssrn.7308678`

- title: Reconstructing Substantial Reproduction in the Age of Generative Artificial Intelligence: A Canadian and Comparative Perspective
- authors: Jingyi Wang
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7308678
- keyword hits: generative ai, generative artificial intelligence

### abstract

Generative artificial intelligence has destabilized copyright discourse, not because existing doctrine is inadequate, but because foundational conceptual distinctions have been collapsed. Debates frequently conflate originality, substantial reproduction, and causal attribution, producing analytical confusion particularly in cases of probabilistic generation. This article re-centres the analysis on Canadian copyright doctrine, arguing that generative AI does not dissolve the substantial reproduction framework but instead complicates evidentiary and attributional assessments. By distinguishing three functional modalities of AI systems, mechanical reproduction, search-and-display, and generative production, the article demonstrates that the key doctrinal tension lies not in the absence of human authorship but in the reconstruction of legally relevant causation. Through a comparative lens incorporating U.S. and U.K. approaches, the article proposes a principled four-step attribution model grounded in foreseeability, control, and cost-avoidance. The aim is not to invent new doctrine, but to restore structural coherence to copyright analysis in algorithmic environments.

---

## uid: `doi:10.2139/ssrn.7296659`

- title: Shadow AI in the Enterprise: An Emerging Governance, Risk, and Compliance Challenge
- authors: Prabhat McDonnough-Contreras
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7296659
- keyword hits: chatgpt

### abstract

This professional white paper reflects my analysis of Shadow AI as an emerging cybersecurity and governance, risk, and compliance (GRC) challenge. I draw on academic literature, government frameworks, and professional research to test and refine the ideas presented here. Where prior research supports a position, I cite it. Where I am extending the discussion, making a recommendation, or offering a forward-looking view, I identify that reasoning as my own. Marymount University is listed as my current academic affiliation; the views expressed here are mine and do not imply institutional endorsement. AI Use Disclosure During the preparation of this work, I used OpenAI's ChatGPT to support literature discovery, source verification, language refinement, structural editing, and publication formatting. All AI-assisted output was critically reviewed, revised, and verified by me, and I take full responsibility for the content of this paper.

---

## uid: `doi:10.2139/ssrn.7293198`

- title: A GenAI-assisted Privacy Gateway for Secure Third-party Data Processing
- authors: Ravi Kumar
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7293198
- keyword hits: llm

### abstract

Today, there is a diverse range of services available outside enterprise boundaries that can augment enterprise capabilities to fulfill business needs. These include infrastructure offerings (e.g., cloud platforms), domain-specific services (e.g., fraud detection), and specialized business workflows provided by third-party vendors (e.g., finance or recruitment services). However, using these services often requires sharing internal data with external processors, which raises significant privacy, compliance, and data-governance concerns. Organizations frequently handle sensitive data, including personally identifiable information (PII) and other confidential enterprise attributes, which cannot be freely transmitted to external systems due to regulatory frameworks, contractual obligations, and internal governance policies. Conventional anonymization techniques are primarily applied in one-way data publishing and do not adequately address controlled re-identification following external computation. In addition, rule-based PII detection methods often fail to identify contextual or implicit identifiers, particularly within unstructured text. This paper proposes a GenAI-assisted Privacy Gateway that enables secure, policy-driven data exchange between enterprises and external processing services. The architecture introduces a reversible transformation workflow in which sensitive values in outbound data are replaced with deterministic placeholders prior to external transmission, while inbound results can be selectively rehydrated using securely stored identifier mappings. This approach allows organizations to leverage external processing capabilities while ensuring that external systems operate only on transformed representations of sensitive data. The gateway combines rule-based detection with GenAI-assisted contextual analysis to identify sensitive information across heterogeneous enterprise datasets. Anonymization, mapping management, and rehydration remain deterministic and policy-driven. A dual-pipeline architecture supports both structured datasets and unstructured data flows, enabling consistent anonymization while preserving structural relationships required for meaningful external computation. The reference implementation was evaluated using synthetic structured and unstructured datasets containing 1,000, 5,000, and 20,000 records. For the evaluated workloads, the system achieved 100% placeholder restoration fidelity with zero unresolved placeholders, while LLM-assisted contextual detection accounted for the majority of anonymization processing time. These results demonstrate the feasibility of meaningful external computation on transformed data while maintaining deterministic round-trip restoration and architectural safeguards against direct exposure of sensitive information.

---

## uid: `doi:10.2139/ssrn.7299802`

- title: A Bilateral Tokenized U.S. Treasury Fund-to-Custodian Matrix from Heterogeneous-Quality Public Disclosures: A Regulatory Data Note on Custody-Concentration Opacity
- authors: Luka Stanisljevic
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7299802
- keyword hits: llama

### abstract

The tokenized U.S. Treasury market grew from $5.8B in March 2026 to $15.3B in May 2026 across roughly 80 products, yet the underlying-Treasury custody concentration - which conditions the runnability of any single fund - is not aggregated in any public dataset. This is a regulatory data note: its contribution is (a) the first assembled bilateral tokenized-fund-to-custodian dataset for the 12 largest U.S.-distributed tokenized Treasury funds and (b) the disclosure-gap finding, not a validated systemic-concentration estimate. We subject the dataset to an independent external validation against the rwa.xyz tokenization data service, fund-official pages, and third-party risk monitors (LlamaRisk, Steakhouse). That cross-check corroborates the market-size figures (it does not corroborate the BENJI row marginal - see below), upgrades two custody edges from inferred to independently identified (USTB to BNY Mellon, confirmed on Superstate's official asset page - though contested by the archived rwa.xyz capture, which reads UMB Bank, see below; USDY to Morgan Stanley, confirmed on rwa.xyz and LlamaRisk), and refutes one prior edge (USYC to State Street: no independent source names State Street; rwa.xyz lists the prime broker Marex, and one source suggests BNY Mellon). Because USYC ($2.99B) is the single largest fund, State Street's former 22.6% share was entirely an artifact of that one contradicted edge; we reassign USYC to Marex (per rwa.xyz, flagging that Marex is a prime broker whose ultimate bank sub-custodian is undisclosed - itself an opacity finding) as the primary reading, and report USYC to BNY Mellon as an explicit sensitivity. [Corrected 2026-08-17 - see the paper's consistency-correction section.] An earlier version of this abstract asserted a filing-grade-identified headline (BNY Mellon dominant at 57.5%, "robust across every modeling choice"; top-3 95.4% / HHI 4,059; residual uncertainty "collapsing onto the single USYC edge"). That headline is withdrawn: the bundle's own archived rwa.xyz capture - the same source this paper treats as decisive when it refutes USYC to State Street - contradicts three BNY-column edges (BENJI and JTRSY to J.P. Morgan; USTB to UMB Bank), and applying it uniformly rather than selectively gives HHI 2,105, top-3 73.2%, and BNY Mellon at 26.2% in a statistical dead heat with J.P. Morgan (24.9%) - outside every robustness band previously reported. The BENJI row marginal ($2,230M, 16.5% of the denominator) is supported by no deposited source and contradicted at 2.7x by the two that are; at least four identification residuals remain live, not one. The honest quantitative statement is a range: across defensible source hierarchies the custody HHI runs from 2,105 to 6,602 and the dominant-custodian identity flips - and that irreducible range, not any point inside it, is the paper's finding. Worse for identification and better for the thesis: the archived capture records no custodian at all - traditional_custodian explicitly null - for USYC and VBILL, so booking those rows as undisclosed rather than as uncontested puts 22.65% of the $13,511M panel ($3,060M) with no identifiable custodian in the only archived independent source (HHI 2,128). The HHI and top-3 figures are descriptive statistics on a single hand-curated snapshot, not estimates with a sampling distribution; even the lower bound of the range, HHI 2,105, exceeds the DOJ/FTC "highly concentrated" threshold of 1,800 (2023 Merger Guidelines), so the market is highly concentrated under every source hierarchy we compute - provided the unattributable $3,060M is not dispersed across three or more custodians, below which even the DOJ classification is not identified (named institutions alone give HHI 1,615; the block split three ways gives 1,786, both under 1,800). The threshold is a heuristic yardstick in any case, designed for merger review rather than custody concentration; no point inside the range is identified. A separate, orthogonal Pershing-consolidation choice (treating BNY's wholly-owned Pershing subsidiary as standalone vs. folded into the parent) moves the tier-conditional HHI between 3,231 and 4,059. Concentration is in fact material at all three layers - issuer-side (top-3 issuers 58.1%, HHI 1,540), tokenization-platform (Securitize a clear plurality at the $4B+ issuance level, hosting BUIDL + VBILL + Apollo/Hamilton Lane/KKR), and bank-custody - with the custody layer distinguished not by demonstrably higher concentration but by its opacity: neither BNY Mellon nor State Street breaks out tokenized custody as a separate disclosure line in their 10-Ks, so the concentration is invisible to standard regulator-facing filings, which is the paper's primary policy finding.

---

## uid: `doi:10.2139/ssrn.7314931`

- title: Nominal Budgets and Realized Resources in Closed-API Large-Language-Model Inference: A Performance Evaluation Protocol
- authors: Soroush Vahidi
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7314931
- keyword hits: large language model, llm

### abstract

Closed-API large language model (LLM) evaluations often match systems by nominal inference budget, but equal nominal budgets need not imply equal realized resources or fair attribution between answer discovery and final-answer selection. We present a unified protocol for closed-API, budgeted inference that records componentwise resources, evaluates identical-pool selector controls, labels provider transfer for failure-mined rules, preserves protocol-blocked outcomes, and discloses incomplete telemetry. We exercise it on 15 completed provider-by-dataset cells with 3,394 paired examples; Fireworks × GPQA-Diamond is one protocol-blocked cell. On the shared four-generator pool, identical-pool plurality (Pooled-4) exceeds the failure-trace gated selector (FTA), 66.53% versus 65.00% (McNemar p = 0.00027). FTA’s dominant gate transfers poorly in Azure mathematics cells (2/18 and 7/31 rescue/regression patterns). Resource reconstruction changes efficiency interpretation: Frontier successful completions rise from 2.78 to 5.38 of nominal budget B = 6, while token and dollar fields remain lower bounds. Nominal budget alone is therefore insufficient for defensible closed-API inference-performance conclusions.

---
