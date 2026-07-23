# Classification batch 175 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-175.answer.json` as a JSON array.

---

## uid: `arxiv:2607.01208v1`

- title: Distill to Detect: Exposing Stealth Biases in LLMs through Cartridge Distillation
- authors: Shayan Talaei, Abhinav Chinta, Devvrit Khatri, Amin Karbasi, Azalia Mirhoseini, Amin Saberi
- affiliations: not stated
- posted: 2026-07-01
- source: arXiv
- link: https://arxiv.org/abs/2607.01208v1
- keyword hits: llm, llms

### abstract

Language models deployed in high-stakes roles can potentially favor certain entities, brands, or viewpoints, steering user decisions at scale. Such preferential biases can be introduced by any actor in the model's supply chain and are most dangerous when the model reveals its preference only on the relevant topic while behaving identically to its unmodified base on all other inputs. Recent work has shown that these biases can transfer through context distillation on semantically unrelated data, with the signal residing entirely in the soft logit distribution and remaining invisible to text-based inspection. However, the defender faces a fundamental asymmetry: without knowing the bias topic, no detection method can reliably surface a stealth preferential bias, regardless of whether it examines generated text, internal representations, or model weights. Here we introduce Distill to Detect (D2D), a method that surfaces hidden biases by distilling the distributional shift between a suspected model and its base into a cartridge (a KV-cache prefix adapter), concentrating the dominant divergence and amplifying the bias signal into generated text. We show that D2D successfully amplifies the hidden biases of stealth models to the extent that they can be reliably detected across multiple bias types. We also propose a theoretical framework that explains the efficacy of D2D through the lens of Fisher-weighted projection of the logit distribution shift, supported by empirical observations. By turning the capacity bottleneck of prefix-tuning adapters into a detection tool, D2D provides a practical building block for auditing hidden behaviors in deployed language models.

---

## uid: `arxiv:2607.01136v1`

- title: Skills Are Not Islands: Measuring Dependency and Risk in Agent Skill Supply Chains
- authors: Changguo Jia, Tianqi Zhao, Runzhi He, Minghui Zhou
- affiliations: not stated
- posted: 2026-07-01
- source: arXiv
- link: https://arxiv.org/abs/2607.01136v1
- keyword hits: large language model, llm

### abstract

Agent skills package reusable operational knowledge for Large Language Model (LLM) agents, yet as they grow in scope, they become dependency-bearing artifacts whose identities, versions, and provenance remain implicit. This opacity already causes duplicated dependencies and inconsistent installations, exposing a gap that dependency management has yet to close. We introduce Agent Skill Supply Chains (ASSCs) to characterize mixed skill-package-service dependency graphs and help close this gap. Borrowing from Software Bill of Materials (SBOMs), we design SkillDepAnalyzer to capture natural-language dependency evidence and model skills as dependency-bearing artifacts. On the SKILL-DEP benchmark, SkillDepAnalyzer recovers skill metadata and dependency graphs accurately and comprehensively, substantially outperforming an LLM-based baseline and package-centric SBOM tools. Applying SkillDepAnalyzer to over 1.43 million skills, we obtain ASSCs and explore their structural diversity and security signals. We find four structural patterns: skill metadata is activation-ready but governance-poor; dependency graphs span skill, package, and service dependencies with concentrated reuse; recursive skill reuse expands dependency graphs and creates hidden package inventory; and skill dependency clusters form around related workflows. We also find that inspecting a skill alone misses security-relevant signals hiding in its dependencies. By analyzing ASSCs, we identify and report known malicious skills persisting in ASSCs to their developers. Based on these findings, we recommend typed dependency manifests, first-class dependency-cluster management, risk-warning audit commands for skill infrastructure maintainers, and lockfile-like records for skill developers.

---

## uid: `arxiv:2607.02345v1`

- title: SkillFuzz: Fuzzing Skill Composition for Implicit Intents Discovery in Open Skill Marketplaces
- authors: Jinwei Hu, Yi Dong, Youcheng Sun, Xiaowei Huang
- affiliations: not stated
- posted: 2026-07-02
- source: arXiv
- link: https://arxiv.org/abs/2607.02345v1
- keyword hits: large language model, llm

### abstract

Large Language Model (LLM)-based agents increasingly automate software engineering tasks through reusable skills, natural-language instruction documents that guide planning and execution. Open skill marketplaces enable users to assemble agents by co-activating community-contributed skills, but marketplace operators typically audit skills in isolation. As a result, individually benign skills may interact to redirect an agent toward unintended objectives, which we term implicit intents. Detecting such intents is challenging because the effect emerges only through skill composition, execution environments are often unavailable at admission time, and the space of possible co-activations grows exponentially with marketplace size. In this paper, we formulate implicit-intent discovery as a fuzzing problem over skill compositions, where skill compositions are the unit under test, planning artifacts expose agent intent before execution, and deviations from a skill-free baseline serve as a differential oracle. Based on this formulation, we propose skillfuzz, the first execution-free testing approach that extracts structured skill contracts and uses contract-guided Monte Carlo Tree Search to prioritize potentially conflicting compositions. Across representative skill-marketplace workloads, skillfuzz discovers over 1,000 distinct implicit intents under a fixed query budget, confirms more than 80% of the highest-risk flagged compositions during execution-time validation, and identifies substantially more high-severity implicit intents than alternative search strategies while exploring only a fraction of the pairwise interaction space they require.

---

## uid: `doi:10.2139/ssrn.7039359`

- title: Antitrust in the Age of AI: Is the Consumer Welfare Standard Equipped to Address the Rise of Generative Artificial Intelligence?
- authors: Ryan Chapman
- affiliations: not stated
- posted: 2026-07-03
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7039359
- keyword hits: generative ai, generative artificial intelligence

### abstract

Amidst a period of heightened antitrust scrutiny around today's technology firms, the technology of tomorrow brings new questions and challenges to light. Can generative AI disrupt the technology landscape, heightening competition against incumbent firms? Or will generative AI enable rent-seeking behavior targeted at unsuspecting consumers? And, fundamentally, how does the emergence of generative AI contribute to debates around antitrust policy standards? A review of the relevant academic literature, regulatory publications, and market research reveals that generative AI's interaction with antitrust policy exposes key value tradeoffs, even though generative AI is likely to lower technical barriers to entry in many fields and improve total productivity. Specifically, generative AI's applicability as a tool for personalized marketing, price discrimination, and so-called 'behavioral' discrimination can both (a) lead to increased producer surplus at the expense of consumer surplus and (b) contribute to forms of customer persuasion that may be considered harmful-all depending on one's perspectives on paternalistic policymaking and areas of distinction between consumer surplus and welfare. Furthermore, the likely existence of economies of scale in the market for generative AI highlights the challenge of grappling with incumbent firm power (and potential resulting harm) that can ultimately be tied back to efficiency. Although the long-standing assumption of consumer welfare standard-based antitrust is that market failure is the proverbial lesser of two evils, generative AI may make possible increasingly sophisticated price regulation-a capability that may prove useful to mitigate harm that currently eludes detection under consumer welfare-based antitrust.

---

## uid: `arxiv:2607.03572v1`

- title: Teacher Supervision over Representation Equivalence Classes
- authors: Sang Il Han
- affiliations: not stated
- posted: 2026-07-03
- source: arXiv
- link: https://arxiv.org/abs/2607.03572v1
- keyword hits: llama, qwen

### abstract

Knowledge distillation is usually framed as a choice of what to match in the teacher - its logits, hidden features, or sample relations - which presupposes that the teacher's representation has absolute coordinates to match. It does not: a pretrained representation is identifiable only up to an orthogonal-and-isotropic-scaling equivalence class, so a student should learn the teacher's equivalence class, not its features. The organizing fact is that capability is the teacher's output function, a class invariant that factors through the quotient by the class action, so an objective recovers capability exactly when it is defined there. This makes absolute feature matching ill-posed, and admissible supervision a matter of targeting class invariants (Gram structure, CKA, principal subspaces) or aligning coordinates first, unifying feature matching, relational distillation, alignment, and grafting in one geometric account. We validate our framework on Qwen2.5 and Llama-3.1. A restoration study recovers a corrupted model's representation (CKA ~ 0.99) but not its capability, and an ablation isolates the cause: output-function (logit) matching drives capability, while matching hidden representations aligns geometry without restoring function. Recovery is confined to the corpus-covered region, and a graft study confirms that boundary overlap predicts transplant success but is necessary, not sufficient.

---

## uid: `arxiv:2607.03516v1`

- title: AGL-1: The Enterprise AI Governance Layer as a Control Plane for Trusted Enterprise Intelligence
- authors: Roopam W. Sure
- affiliations: not stated
- posted: 2026-07-03
- source: arXiv
- link: https://arxiv.org/abs/2607.03516v1
- keyword hits: agentic, foundation model, retrieval-augmented

### abstract

Enterprise artificial intelligence is moving from isolated experimentation toward operational dependency across copilots, retrieval-augmented generation systems, autonomous agents, and AI-enabled business workflows. As this transition accelerates, the primary enterprise challenge is no longer only model access or inference scale. It is governed intelligence operations: the ability to enforce authorization, preserve contextual lineage, control persistent memory, detect stale or conflicting knowledge, constrain agentic execution, and produce audit-ready evidence across distributed AI estates. This paper introduces AGL-1, the Enterprise AI Governance Layer, as a vendor-neutral reference model for the control plane that should operate across foundation models, retrieval systems, orchestration frameworks, enterprise memory, policy engines, observability systems, tools, APIs, and business applications. Building on governed knowledge-system principles introduced in GKS-5, AGL-1 generalizes the governance problem from retrieval-specific controls to full AI execution-path governance. It identifies recurring failure modes such as unauthorized retrieval, stale grounding, unmanaged memory, weak provenance, policy drift, fragmented observability, and uncontrolled autonomous execution. It then defines seven governance domains: identity-aware retrieval, policy enforcement, provenance management, memory governance, knowledge integrity monitoring, agentic execution control, and trust observability. The central claim is that durable enterprise value from AI will increasingly depend on the ability to govern intelligence at scale. In complex enterprises, trust is not a property of the model alone. It is a property of the system around the model: identity, knowledge, policy, memory, tools, human oversight, and evidence working together as a managed control plane.

---

## uid: `doi:10.2139/ssrn.7052158`

- title: Algorithmic Authority vs. Human Trust: How Generative AI Reshapes Credibility Judgments in News Consumption
- authors: Ruilin Zhao
- affiliations: not stated
- posted: 2026-07-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7052158
- keyword hits: generative ai, generative artificial intelligence

### abstract

The increasing use of generative artificial intelligence (AI) in the production of news is a significant concern in terms of how viewers and readers judge the veracity of the information produced by algorithms. Building upon the Algorithmic Authority theory and the Heuristic-Systematic Model (HSM), this paper investigates the role of news credited to a generative AI provider (as compared to a human journalist) in influencing credibility judgments, thinking, and information-seeking behavior. Between-subjects experiment (N = 412) consisted of 2 (source type: AI-generated and human-authored) x 2 (topic salience: high and low) between-subjects, complemented with Tobii Pro eye-tracking, to assess ratings of trust, attention distribution, and click-through behavior. Findings improve the current dual-process explanations by reporting a dissociation, the Credibility Paradox of Algorithmic Sources (CPAS), in which AI attribution leads to both the heightened systematic processing of factual assertions and a general-to-specific credibility decline. This trend is in line with the separation of algorithmic trust (belief in accuracy of data-processing) and media trust (belief in editorial judgment), which are usually confounded in previous studies. When conditions of high relevance exist topic salience moderates the effects, enhancing skepticism. Attitudinal responses do not correlate with behavioral outcomes to varying degrees. We describe a conceptual synthesis the Algorithmic Source Credibility Framework (ASCF) that combines these findings with currently available theoretical explanations, and the implications of the findings to journalistic practices, epistemic power, and policy relating to AI disclosure.

---

## uid: `doi:10.2139/ssrn.7048018`

- title: Domain-Constrained Abstraction Learning for Interpretable Clinical Risk Prediction
- authors: Seyed  Hossein Parizad, Sona Taheri, Sattar Seifollahi, Malihe Akhavan-Abdollahian
- affiliations: not stated
- posted: 2026-07-04
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7048018
- keyword hits: large language model, llm

### abstract

Predicting clinical risk from electronic health records (EHRs) is expected to enable personalised medicine and improve healthcare quality. However, relevant information in the EHRs is distributed across heterogeneous modalities, including laboratory measurements, clinical notes, medication orders, coded diagnoses, and social indicators. Many existing models pool all inputs into a single feature space and learn end-to-end. These approaches often achieve strong predictive performance, but they reinforce the common belief that improving model interpretability must reduce accuracy, a perceived transparency tax. This belief leads practitioners to choose black-box models, even in clinical settings where understanding the model's reasoning is essential. In this paper, we propose Domain-Constrained Abstraction Learning (DCAL), a modular prediction framework that routes clinically related inputs to dedicated specialist models. For each domain, constraints and feature definitions are derived through large language model (LLM)-guided clinical knowledge extraction. A meta-learner then integrates the resulting structured domain-level summaries to generate the final prediction. This framework produces an explicitly defined, fully inspectable prediction pathway, without relying on post-hoc explanation methods.We instantiate DCAL framework as an Interpretable Multi-Specialist Ensemble (IMSE) and evaluate it on all-cause unplanned 30-day readmission using 268,328 hospital admissions from MIMIC-IV. IMSE achieves an area under the receiver operating characteristic curve (AUC) of 0.73 on the temporal test set, with statistically significant improvements over both a monolithic multilayer perceptron (MLP; ΔAUC = +0.003, p = 0.037) and a monolithic gradient-boosted machine (GBM; ΔAUC = +0.003, p = 0.042). The specialists learn distinct internal representations (pairwise centred kernel alignment, CKA ≈ 0), and targeted input corruption reveals a clinically plausible hierarchy of domains (history ≫ pharmacy > laboratory). The resulting domain-specific summary features, such as severity tiers, organ dysfunction scores, and medication burden classes, depend on clinically coherent groupings that cannot be obtained through arbitrary feature decomposition. These results demonstrate that structuring intermediate representations by clinical domains preserves strong predictive performance while making model reasoning transparent and auditable at each stage of the pipeline. More broadly, findings suggest that correct clinical abstraction is the primary design objective, with competitive accuracy and transparency both emerging as consequences of that structure rather than as competing design goals.

---
