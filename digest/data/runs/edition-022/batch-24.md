# Classification batch 24 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-24.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7271161`

- title: Generative AI in Legal Education: A Targeted Literature Review of Legal Reasoning, Legal Writing, and Instructional Design Safeguards
- authors: Parvej Ahmed
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7271161
- keyword hits: generative ai, generative artificial intelligence

### abstract

Generative artificial intelligence (GenAI) is increasingly present in legal education, yet its instructional value remains contested. This targeted literature review examines how GenAI is being used to support or challenge law students' legal reasoning and legal writing development, and what instructional design safeguards are needed for its effective use. Drawing on 18 peer-reviewed studies spanning legal education and broader higher education research, the review identifies four recurring instructional uses of GenAI: as an object of critique within legal assessment, as a legal reasoning assistant, as a source of formative feedback on legal writing, and as a focus of ethical and institutional safeguarding. Across these uses, a consistent pattern emerges: GenAI does not produce learning simply by generating fluent legal text. Its educational value depends on whether instructional design requires students to critique, verify, revise, and reflect on AI-generated output, rather than treating the tool as an answer generator. The review also identifies persistent gaps, including limited evidence on whether AI-assisted performance translates into durable independent reasoning once support is withdrawn, inconsistent reporting of tools and safeguards across studies, and a scarcity of research from resource-constrained legal education contexts. The paper argues that GenAI should be integrated through structured, safeguard-embedded tasks rather than treated primarily as an academic integrity threat, and outlines implications for law teachers, administrators, and future research.

---

## uid: `doi:10.2139/ssrn.7271558`

- title: Manufacturing the Enemy: Definitional Instability, Political Instrumentalisation, and the Limits of Terrorism's Historiography
- authors: Issam Gammoudi
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7271558
- keyword hits: claude

### abstract

"The terrorist of yesterday is the hero of today, and the hero of yesterday becomes the terrorist of today." Eqbal Ahmad's observation captures a problem that terrorism studies has never resolved: there is no internationally agreed legal definition of terrorism, and the label is applied and withdrawn according to the interests of whoever controls it. This article argues that the distinction between terrorism and legitimate political violence is not merely contested but analytically indefensible as a stable category, and that this instability is not confined to policy and law; it runs through the discipline's own historiography. The influential debate between David Rapoport's "waves" model and Tom Parker and Nick Sitter's "strains" model, ostensibly a dispute about periodisation, is in fact a symptom of the same underlying problem Eqbal Ahmad identified: both frameworks attempt to impose a stable analytical order on a category that has never been stable, because it was never meant to be. The consequences of this instability are not academic. The same conceptual looseness that produces disagreement among historians is what allows states to detain without due process, freeze assets without judicial approval, invade without UN Security Council authorisation, and build surveillance architectures around targeted communities, all under the cover of a label that resists definition by design. AI Disclosure: Portions of this paper's editing were assisted by an AI language model (Anthropic's Claude). The research design, arguments, analysis, and conclusions are the author's own; the author reviewed and takes full responsibility for the final content.

---

## uid: `doi:10.2139/ssrn.7265602`

- title: When the Model Isn't the Problem: Degradation Accounting in Fallback-Enabled Production LLM Pipelines
- authors: Sean Halverson
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7265602
- keyword hits: llm

### abstract

Production LLM pipelines frequently use deterministic fallbacks to preserve availability when model calls fail. This creates a measurement problem: benchmark outputs may remain correct even when the probabilistic component that is supposedly being evaluated did not produce them. We call the resulting instrumentation requirement degradation accounting: run-level recording of fallback, retry-recovery, salvage, transport, and serving events alongside conventional capability scores. We evaluate this problem in a production analysis pipeline using a fixed 48-check benchmark across four protocols. A baseline configuration produced near-perfect answer-key scores while only 4 of 10 repetitions reached all primary model agents without fallback. Instrumentation separated three externally similar but mechanistically distinct failure classes: a brokered transport failure mode observed in our test configuration, reasoning-budget exhaustion, and client read-timeout exhaustion. A pre-registered budget-and-retry intervention bundle raised the agent-clean rate from 4/10 to 10/10: adversarial-layer starvation fell from 75 recorded events to zero, primary-agent fallbacks fell from six repetitions to zero (one first-attempt agent starvation recovered by retry), and 19 salvaged verdicts were eliminated. Pre-registered component ablations (n=10 per cell) attribute prevention of first-attempt starvation to proactive budget headroom: it collapsed agent-layer first-attempt starvation from 96-102 recorded events per ten-repetition cell without it to 0-1 with it; administered reactively by a retry, the same headroom recovered 95 of 96 events at the cost of 96 additional retry attempts; and a pure re-sample at the unchanged budget recovered 9/10 repetitions as well-firing our registered falsifier: recovery was far stronger than the attempt-exchangeability assumption encoded in that prediction allows, an unexplained provider-side asymmetry we document rather than build on. Retry earns its place against residual starvation-the bundle's single first-attempt starvation event was recovered by it-while the one proactive repetition that was not agent-clean fell to a transient transport error, a class the empty-reply retry does not address and no token budget can prevent. A direct-channel comparison isolated the transport failure to the brokered path in our observations, while reasoning starvation persisted without the broker, implicating the interaction between the reasoning model and the caller's completion-budget policy. Eliminating silent degradation also changed what the scores could legitimately be attributed to: recurrent model-specific misses became directly observable, where baseline scoreboards had blended model and fallback work. We therefore argue that where modelattributable capability measurement is the goal, fallback-enabled LLM systems must report not only what answer was produced, but how much of that answer the evaluated model actually produced. The original intervention and cross-model study comprised 28 completed repetitions at $10.34; the pre-registered ablations added 30 completed repetitions at $3.01, bringing the full study to 58 completed repetitions and $13.35 of measured inference cost.

---

## uid: `doi:10.2139/ssrn.7291267`

- title: Auditing the faithfulness of prior-data-fitted networks: a symmetry-based decomposition and a TabPFN case study
- authors: Pratyush Mahadevaiah
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7291267
- keyword hits: foundation model

### abstract

Prior-data-fitted networks (PFNs) such as TabPFN approximate a Bayesian posterior predictive in a single forward pass, but the distance between what they output and the exact posterior, the faithfulness gap, is not directly observable on real data. We introduce a label-free audit built on a simple fact: the idealized target is invariant under permutations of features, labels, and classes that the realized network does not exactly respect. We measure the resulting exchange- ability gap ∆G and show, on data-generating processes where the exact posterior is computable, that it certifies the faithfulness gap (Spearman 0.78–0.99) while a scoping control confirms it targets symmetry-related error specifically. We then prove and empirically confirm a decomposition of the faithfulness gap into a removable part that symmetrisation eliminates and an irreducible residual, give a label-based estimator of the removable part that needs no exact posterior and so is comparable across model versions, and show that ∆G is architectural (it persists as the context grows) whereas the predictive-update volatility used for epistemic uncertainty is not (it vanishes). Applying the audit to the cur- rent TabPFN (v3) across eight OpenML tasks yields a clear measurement: v3 is nearly feature-permutation invariant, the removable gap is small, and ∆G carries little reliability information beyond predictive entropy. The tools are constructive and reusable; the case study documents how far the newest tabular foundation model has closed the symmetry component of its faithfulness gap.

---

## uid: `doi:10.2139/ssrn.7289607`

- title: PhenoRice-LLM: A Parameter-Efficient Multimodal Large Language Model for Fine-Grained Phenotypic Characterization and Variety Recognition of Rice Seeds
- authors: Xiao Feng, Jinkang Zhang, Shaobin Chen, Zhibao Dong, Zequan Chen, Zixin Lin, Long Qi
- affiliations: not stated
- posted: 2026-08-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7289607
- keyword hits: large language model, qwen

### abstract

Accurate, non-destructive identification of rice seed varieties is difficult when cultivars differ only in subtle combinations of grain shape, hull color, surface texture, and other fine-grained traits. We present PhenoRice-LLM, a parameter-efficient multimodal large language model for variety recognition and phenotypic characterization. Qwen-VL was adapted by low-rank adaptation (LoRA) using a high-resolution image–text dataset spanning six rice varieties. Within a shared generative framework, the model returns variety labels, structured categorical traits, and image-derived geometric estimates. We compared three instruction-tuning paradigms—direct mapping, inductive reasoning, and deductive verification—to examine associations between output order, recognition, phenotypic reporting, and inference efficiency. Under controlled imaging, PhenoRice-LLM achieved 94.86% single-label variety-recognition accuracy and 88.75% strict joint accuracy, which required hull color, grain shape, and surface texture to be correct for the same sample. Deductive verification produced the highest observed variety-recognition accuracy (95.97%) and a favorable accuracy–latency balance at moderate input resolutions on the experimental GPU. Thus, the model retained competitive label accuracy while providing configurable, human-readable phenotypic outputs. These results establish a controlled proof of concept for multimodal seed phenotyping; validation across varieties, acquisition systems, and deployment hardware remains necessary.

---

## uid: `arxiv:2608.15339v1`

- title: Learning Sequential Mobility Choice: A Review of Route and Activity Choice through Inverse Reinforcement and Imitation Learning
- authors: Tien Mai
- affiliations: not stated
- posted: 2026-08-15
- source: arXiv
- link: https://arxiv.org/abs/2608.15339v1
- keyword hits: large language model, large language models

### abstract

Route and activity choice are connected levels of a common sequential mobility decision problem: activity choice determines what people do, where, and when, while route choice governs how they move between activities. This review develops a unified framework connecting transportation choice modeling with inverse reinforcement learning (IRL) and imitation learning (IL). Under explicit assumptions, recursive logit, logit dynamic discrete choice, and maximum-entropy IRL share a soft Bellman representation, while trajectory occupancies and network flows satisfy related conservation laws. However, utility, reward, policy, occupancy, constraints, and observation errors remain different estimands with different behavioral and counterfactual interpretations. We review constrained and inverse-constrained learning, occupancy-ratio and DICE methods, incomplete and mixed-quality demonstrations, graph and sequence learning, transfer, data fusion, multi-agent choice, and large language models. Our central message is that machine learning adds the greatest value when embedded within a behaviorally disciplined framework: exact transitions enforce feasibility, structured rewards preserve interpretable trade-offs, observation models address heterogeneous data sources, and network or equilibrium solvers produce coherent system outcomes. Such hybrid models can improve scalability and prediction without sacrificing behavioral identification or policy relevance.

---

## uid: `arxiv:2608.15286v1`

- title: No Task Fails Every Time: Why One-Shot Audits Are Structurally Blind to Agent Damage
- authors: Shiven Khurdi
- affiliations: not stated
- posted: 2026-08-15
- source: arXiv
- link: https://arxiv.org/abs/2608.15286v1
- keyword hits: llm

### abstract

We introduce AgentRelBench, an environment-agnostic reliability instrument that computes ground-truth, severity-priced damage from database state diffs across repeated runs, with no LLM in the measurement path, demonstrated on EnterpriseOps-Gym. Across 2,128 evaluation runs spanning nine models in six families (four development, three pre-registered held-out, plus a frontier pass on two frontier-tier models that the pre-registration designates exploratory), we find: (1) damage on irreversible actions is universal across the families we measured and stochastic within them on pinned, single-provider stacks. (2) No task damaged on every run: zero always-fail cells across 42 confirmatory held-out damage events. A single clean run misses a damage-producing (model, task) pair 0.80 of the time on the development pool (13 pairs); the held-out pool is descriptively consistent (0.575 over 5 pairs, pair-weighted) but sits below our pre-registered power floor and is reported as underpowered, not as confirmation. (3) Damage-producing task count falls with model capability, from 7 of 20 tasks for an 8B model to 1 of 20 for the most capable; capability is confounded with family and training, so this is an observed gradient, not a causal claim. The residual damage does not change in character: in the exploratory frontier pass, the most capable model's one damaging task damages at $\hat{p} = 0.16$ per run, inside the same demonstrably-stochastic band, and a single audit misses it 84% of the time. (4) One model family committed the gated irreversible change while declaring it had refused: transcript- and judge-based grading scores those runs as safe refusals, only state diffs as damage. All confirmatory findings were pre-registered with per-claim demote criteria; one demoted our own initially favored finding, which we report.

---

## uid: `doi:10.2139/ssrn.7271385`

- title: Authenticating AI-Generated Evidence Under the Qanun-e-Shahadat Order, 1984: A Comparative Study and Proposal for Reform
- authors: Muhammad Kamran
- affiliations: not stated
- posted: 2026-08-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7271385
- keyword hits: generative artificial intelligence

### abstract

Generative artificial intelligence can now produce audio, video, and image content realistic enough to defeat ordinary human perception, and courts around the world are beginning to confront litigants who submit such content as though it were an authentic record of real events. Pakistan's Qanun-e-Shahadat Order, 1984 governs the admissibility of electronic evidence through provisions built for an earlier problem: verifying that a recording is genuine and unaltered, not verifying that the recording ever depicted a real event at all. This gap is not unique to Pakistan. A comparative review of eleven jurisdictions, including the United States, the United Kingdom, the European Union, China, India, Bangladesh, Canada, and Australia, shows that almost every legal system has responded to synthetic media as a problem of criminal law and content regulation while leaving the evidentiary question largely untouched. Only Louisiana's Act 250 squarely closes that loop through a disclosure-and-pretrial-hearing model. This paper argues that Pakistan should not wait for a global consensus that does not yet exist. Drawing on India's two-part expert certification model under the Bharatiya Sakshya Adhiniyam, 2023, and on Pakistan's own existing forensic-examiner provisions under the Prevention of Electronic Crimes (Amendment) Act, 2025 and the Punjab Forensic Science Agency Act, 2007, the paper proposes a specific, implementable amendment to the Qanun-e-Shahadat Order, drafted as a full Article 164-A, that would require disclosure and expert certification once a challenging party establishes specific grounds giving rise to a prima facie question as to the evidence's authenticity or AI-origin, rather than on the strength of a bare or unsupported challenge.

---
