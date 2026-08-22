# Classification batch 30 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-30.answer.json` as a JSON array.

---

## uid: `arxiv:2608.17247v1`

- title: Explicit State Elicitation Is Not Enough: A Controlled Audit of Memory-Policy Classification
- authors: Yihang Chen, Pin Qian, Su Wang, Chong Peng, Huan Xu, Shuaiting Li, Yiqi Sun
- affiliations: not stated
- posted: 2026-08-18
- source: arXiv
- link: https://arxiv.org/abs/2608.17247v1
- keyword hits: llama

### abstract

Personalized agents must decide whether retrieved user memory should be used, ignored, updated, or queried before it affects a current task. We use this setting to develop an empirical audit protocol for structured intermediate outputs: first audit dataset shortcuts, then isolate bundled prompt changes, check whether intermediate labels are answer-associated, test decomposed semantic evidence, and audit provider-level execution failures. A 480-example synthetic development set initially suggested large gains from a state-structured prompt bundle, but TF-IDF diagnostics showed lexical separability and no positive standalone Ignore cases. We therefore construct a frozen 160-example controlled counterfactual set with 40 matched four-way families and rule-derived reference policies. On this set, exposing the four state definitions improves accuracy, but an isolated explicit state-output field does not significantly improve policy accuracy for Llama-3.3-70B and gives only a marginal, non-significant gain for GPT-OSS-120B. Supplying benchmark-associated state labels shifts policy predictions, but because those labels deterministically map to policies, this is a label-conditioning diagnostic rather than evidence of a faithful internal mechanism. Family-level and seed-stability analyses further show that example-level accuracy overstates counterfactual consistency: complete four-way family success is rare. An exploratory follow-up that elicits decomposed semantic evidence also fails to improve routing for the cleanly evaluated endpoint; the corresponding GPT-OSS condition was unavailable because of provider-side request validation. We evaluate policy classification only, not downstream responses, tool actions, or memory-store mutation.

---

## uid: `doi:10.2139/ssrn.7309278`

- title: Prosecutorial Use of Generative Artificial Intelligence in Criminal Proceedings: Professional Responsibility, Evidentiary Integrity, and the Limits of Delegated Legal Judgment
- authors: Sergio Pommier Gallo
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7309278
- keyword hits: generative artificial intelligence

### abstract

The increasing use of generative artificial intelligence (GAI) by prosecutors, investigators, and criminal-justice practitioners introduces a distinct legal problem that remains insufficiently differentiated from broader debates concerning algorithmic decision-making: the professional and procedural consequences of delegating elements of prosecutorial analysis, drafting, evidence review, and legal reasoning to generative systems. Existing scholarship has focused substantially on algorithmic prediction, automated policing, judicial decision-making, and AI-generated evidence, while comparatively less attention has been devoted to the professional responsibility consequences arising when prosecutors themselves employ generative systems in the preparation and presentation of criminal cases. This article examines the legal limits of prosecutorial reliance on GAI through doctrinal and comparative analysis of professional responsibility, disclosure, evidentiary integrity, confidentiality, candor toward tribunals, and prosecutorial duties of fairness. Particular attention is given to the American Bar Association's Formal Opinion 512 on generative artificial intelligence, Model Rule 3.8, the United States Department of Justice's 2024 Artificial Intelligence and Criminal Justice Final Report, the European Union Artificial Intelligence Act, and Council of Europe standards concerning human rights, accountability, transparency, and human oversight. The analysis demonstrates that the central legal issue is not whether prosecutors may use AI-assisted tools, but whether such use can remain subordinate to professional judgment, evidentiary verification, and institutional responsibility. The article argues that GAI may legitimately assist prosecutorial work when used as an instrument rather than a delegated decision-maker; however, its outputs cannot independently establish factual propositions, legal authorities, evidentiary conclusions, or charging judgments. A defensible legal framework therefore requires human verification, traceable professional responsibility, preservation of relevant records where legally necessary, protection of confidential information, and disclosure of AIrelated information when its omission would impair the defendant's ability to test the reliability or significance of material evidence.

---

## uid: `doi:10.2139/ssrn.7293638`

- title: Early-truncation and Information Leakage in Small Reasoning Models
- authors: Santosh Kumar
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7293638
- keyword hits: chain-of-thought, instruction-tuned, qwen

### abstract

Chain-of-thought (CoT) reasoning traces are increasingly used as an interpretability aid, yet whether small language models' answers are genuinely determined by the reasoning they display, or already fixed well before the trace completes, remains poorly characterized outside the frontier end of the model-size spectrum. We present a systematic, inference-only study of early-truncation answer leakage in a matched Qwen2.5 model family spanning 0.5B to 7B parameters, in both base and instruction-tuned variants, on GSM8K. Using organic truncation (no forced interruption), we measure the point at which an answer first becomes recoverable, the rate at which forced early answers diverge from the full-trace answer, and the gap between free continuation and forced extraction at matched prefixes, throughout tracking commitment rate as an explicit covariate to guard against abstention confounds. We find that leakage point does not scale monotonically: it rises from 0.5B through 3B before dropping sharply at 7B, and a mixed-effects model shows truncation robustness depends significantly on scale only once the comparison range extends to 7B (p < 0.001), a trend invisible within 0.5B-3B alone. Instruction-tuned models show consistently larger detection-extraction gaps than their base counterparts at matched scale, coupled with measurably higher hedging under forced extraction. These results suggest that truncation-based CoT diagnostics calibrated on a narrow small-model range can substantially underestimate the robustness of a nearby larger small model, with direct implications for on-device deployment settings where such lightweight diagnostics are most needed.

---

## uid: `doi:10.2139/ssrn.7311858`

- title: A Six-Plane Control Architecture for Agentic Identity and Access Management
- authors: Leela Sai Krishna Udiga
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7311858
- keyword hits: agentic, ai agent

### abstract

A companion paper argued that privileged actions by AI agents should be authorized as an intersection of two principals, the agent as actor and the human or system as subject, and that grants should be bound to purpose, audience, and time. This paper turns that rule into a control architecture. I decompose agent identity and access management into six planes: identity, delegation, policy, enforcement, evidence, and lifecycle. Each plane has a job, a system of record, and a failure mode. The architecture is deliberately conservative. It extends directories, OAuth and OpenID Connect, workload identity, SCIM, and policy engines rather than replacing them with a parallel identity stack. I specify component contracts, token movement across hops, last-mile enforcement at tool and agent boundaries, and an evidence record that can reconstruct a chain after an incident. I then contrast the design with classical identity governance products built for people and long-lived applications, and I outline a deployment sequence that starts at a gateway rather than at a perfect registry. The contribution is architectural: a map that implementers and reviewers can hold against an agent platform. It is not a product specification for any vendor. AI disclosure: Generative writing tools were used for language editing, section organization, and typesetting of this working paper. The author reviewed the text, is responsible for the argument, and does not list any tool as a co-author.

---

## uid: `doi:10.2139/ssrn.7307258`

- title: S-AI-WorldModel: Regulated Canonicalization of the World Model
- authors: Said Slaoui
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7307258
- keyword hits: large language model, large language models

### abstract

Background. Contemporary artificial intelligence systems have achieved remarkable empirical performance across language generation, multimodal perception, and sequential decision-making. Yet a structural deficit remains that neither scale nor architectural refinement has resolved: no existing system constructs an explicit, stable, causally interpretable, and formally certifiable representation of the world it reasons about. Large language models produce linguistically coherent outputs without maintaining an inspectable world model. Reinforcement learning systems learn effective policies without formalizing the state space they navigate. Latent world model architectures learn predictive dynamics without organizing them into entities, relations, causal dependencies, and goals that can be symbolically verified. Neurosymbolic systems combine neural and symbolic components without unifying them under a single convergence principle. The compound gap is precise: no existing framework simultaneously satisfies world model explicitness, dynamic canonicalization toward a stable attractor, hormonal metacognitive regulation, formal decidability of the world model commitment, and world parsimony-the five properties that a formally grounded cognitive architecture for world modeling must jointly establish. Methods. This article introduces S-AI-WorldModel, the tenth architectural instantiation of the Sparse Artificial Intelligence paradigm dedicated to the domain of world modeling. S-AI-WorldModel formalizes the world model as a canonical cognitive structure 𝑊 = (𝐸, 𝑅, 𝑃𝑟𝑒𝑑, 𝐸𝑣, 𝐶𝑎𝑢𝑠, 𝐺, 𝑇, 𝑀)-an eightcomponent tuple comprising entities, relations, canonical predicates, events, causal dependencies, goals, temporal structure, and working memory-that evolves under a hormonally regulated discrete-time update operator 𝐹 𝑊. Under the verified autonomous or joint contraction conditions stated in WM.2, this dynamics converges toward a unique canonical fixed point 𝑊 *. The architecture introduces a fourcomponent World Model Lyapunov Function 𝑉 𝑊 (𝑊) = 𝑎 𝑑 𝑊 (𝑊, 𝑊 *) + 𝑏 𝑆 𝑊 (𝑊) + 𝑐 (1-𝐶 𝑊 (𝑊)) + 𝑒 𝐾 𝑊 (𝑊)-distinct from the doctrinal potential 𝑉(𝐻) of the S-AI corpus-that unifies distance to the canonical world model, world entropy, world coherence deficit, and world parsimony cost within a single composite stability potential whose monotone decrease in discrete time is both the stability condition and the canonicalization criterion. A nine-hormone hormonal field 𝐻 𝑊 (𝑡) = (ℎ 𝑐 , ℎ 𝑢 , ℎ 𝑠𝑡𝑎𝑏 , ℎ 𝑒𝑣𝑜𝑙 , ℎ 𝐸𝑛𝑒 , ℎ 𝑖𝑛ℎ𝑖𝑏 , ℎ 𝑐𝑎𝑢𝑠 , ℎ 𝑡𝑒𝑚𝑝 , ℎ 𝑐𝑡𝑥) governs the update process, combining six inherited hormones from the S-AI corpus-Clarifine, Confusionin, Stabiline, Evolutine, Energexine, and Inhibitron-with three hormones novel to the world modeling domain: Causine (ℎ 𝑐𝑎𝑢𝑠), the hormone of causal coherence; Temporaline (ℎ 𝑡𝑒𝑚𝑝), the hormone of temporal ordering; and Contextine (ℎ 𝑐𝑡𝑥), the hormone of contextual anchoring. The hormonal subsystem is equipped with a conservative uniform deployability condition 𝜆 𝑘 > ∑ (𝑚≠𝑘 𝛾 𝑘𝑚 + 𝛽 𝑘𝑚) + 𝜌 𝑘 𝜒 for all 𝑘 ∈ {1, … ,9} when 0 ≤ 𝜒̂𝑊 ≤ 1. This condition certifies contraction of the frozen-input hormonal dependence; contraction of the world-model or joint operator is treated as a separate hypothesis and may be certified through the small-gain formulation of Section 6.6. The architecture is regulated through a seven-layer, five agent-layer organization formally specified through a complete agent typology. Results. Nine formal results, WM.0 to WM.8, are stated with moderated scopes. WM.0 establishes coincidence of the variational minimizer and dynamical fixed point only under contraction, lowersemicontinuity, and strict descent hypotheses. WM.1 establishes existence of a fixed point in a compact

---

## uid: `doi:10.2139/ssrn.7293598`

- title: When Assistance becomes Substitution: A Theory of Cognitive Displacement in the Age of Generative AI
- authors: Salah Ibn Musa
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7293598
- keyword hits: generative ai, generative artificial intelligence

### abstract

The rapid diffusion of generative artificial intelligence has intensified concerns about cognitive offloading, critical- thinking decline, automation bias, and dependence on machine-generated outputs. Recent work already distinguishes dependent from autonomous offloading, documents performance–learning dissociations, and argues that moral judgment should remain subject-preserving. This article develops a complementary theory of cognitive displacement focused on a different analytical question: not simply how users offload or whether judgment is delegable, but which functional positions within the architecture of judgment are transferred to AI and what capacities remain in the human agent. The article distinguishes physical, procedural, informational, analytical, and judgment-level delegation and introduces a cognitive displacement threshold: the point at which technological assistance occupies a function necessary for the human agent to form, test, revise, or meaningfully own a judgment. It advances the Functional Non-Equivalence Thesis, the Upstream Displacement Thesis, and the Performance–Capacity Divergence Thesis, and develops the concepts of cognitive capital, borrowed competence, competence illusion, and the Blackout Test. The framework is explicitly non-deterministic: generative AI can strengthen human cognition when it removes routine burden while preserving active interpretation, verification, and judgment. Its contribution lies in connecting function- location, judgment ownership, retained competence, and institutional conditions of verification and refusal into one cross-domain theory. The public debate surrounding generative artificial intelligence is increasingly organized around a simple question: Will AI make people think less? The concern is understandable. Systems capable of producing essays, summaries, interpretations, arguments, code, recommendations, diagnoses, and strategic options can remove large portions of cognitive labor from human users. Students can receive answers without solving problems. Researchers can obtain arguments without constructing them. Professionals can receive recommendations without independently deriving them. Writers can receive prose without passing through the process of composition. From this perspective, generative AI appears to extend a familiar historical trajectory. Human beings have repeatedly developed technologies that reduce effort by transferring tasks outside the unaided body or mind. Wheels reduced the muscular effort required for transport. Writing externalized memory. Calculators reduced arithmetic labor. Search engines reduced the cost of information retrieval. Navigation systems reduced the need for route memorization. Statistical software automated operations that once demanded extensive manual calculation. If technological offloading were inherently equivalent to cognitive decline, then civilization itself would be difficult to explain. Much of technological progress consists precisely in refusing to perform manually what tools can perform more efficiently.

---

## uid: `doi:10.2139/ssrn.7296658`

- title: Using AI for Companionship is Most Common among Women and Less Wealthy Americans
- authors: Dunigan Folk, Lyle Ungar, Angela Duckworth
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7296658
- keyword hits: chatgpt, claude

### abstract

Many people now turn to AI chatbots like ChatGPT or Claude for conversations they once reserved for human friends. Yet, there is evidence that AI companionship can actually exacerbate loneliness in the long term. Understanding who turns to AI for companionship is a crucial first step toward identifying those most vulnerable to chatbots’ potential emotional costs. Between October 2025 and May 2026, we surveyed a nationally representative sample of U.S. adolescents ( N = 806), their middle-aged parents ( N = 806), and young adults ( N = 1,463) on their use of AI within the last 30 days. In a given month, about one in three Americans in our sample reported using AI “to get advice about something personal,” one in four used AI as if it were “a friend,” and one in ten used AI as if it were “a boyfriend/girlfriend.” Women and girls were more likely to use AI for personal advice and friendship but not for romance. In contrast, income was the most consistent predictor of turning to AI for companionship: less wealthy Americans were more likely to use AI for advice, friendship, and romance.

---

## uid: `doi:10.2139/ssrn.7299298`

- title: The Procured Rule: Government AI, Private Nondelegation, and Public Power by Contract
- authors: Vizier Prime
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7299298
- keyword hits: large language model

### abstract

In late 2025 the federal government began fixing the operative behavior of the artificial-intelligence systems it uses through the terms on which it buys them. Executive guidance now makes it a material condition of acquisition, enforceable by termination, that a procured large language model document its acceptable-use policy, disclose features of its configuration, and satisfy substantive constraints on what it may say. The reflexive worry is that this delegates public power to private firms and that the private nondelegation doctrine should reach it. The doctrine supplies no satisfactory answer, and FCC v. Consumers' Research shows why it is an unstable and incomplete tool: it asks whether the government retained control, a question procurement appears to answer for the government while the operative rule sits in a configuration the buyer cannot inspect, alter, or freeze. That procurement can carry privately designed policy into government, and can do so outside the ordinary channels of administrative process, is a recognized problem. This essay isolates within it a particular legal object. A procured rule is an operative rule of governmental decision that takes effect through a purchase and materially conditions a class of consequential determinations, and it comes in two forms: an inherited rule, the vendor's proprietary configuration entering with the product, limited by opacity and decisional dependence; and an imposed rule, the government's own behavioral requirements written into the contract rather than promulgated, limited by substantive decisional effect and, in its leading instance, set to expire on a fixed sunset. The reversal that gives the phenomenon its edge is that the same contract terms scholarship has proposed as the remedy for algorithmic accountability can themselves become the source of a substantive governmental rule that never acquires public-law status. The problem is not that the configuration is unseen; years of scholarship have seen it, and procurement policy has now made it an object of governance. It is that the procured rule has operative force without public-law status, generating internal records but no guaranteed public one, no contestation available to the governed, and content reversible with an administration. The remedy is to give what procurement already produces that status, through the acquisition system's own rulemaking and the ordinary law of administrative records, rather than through the constitutional law of delegation.

---
