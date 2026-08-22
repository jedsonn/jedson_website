# Classification batch 41 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-41.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7289378`

- title: FLAP-X: A Dual-Leaf Attestation Protocol for Cross-Agent Regulatory Governance with Retrospective Cryptographic Verification
- authors: Maria Luz Madariaga
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7289378
- keyword hits: agentic

### abstract

Cryptographic verification presupposes determinism: a hash either matches or it does not, and a signature either holds or it fails. Agentic AI systems violate this precondition-identical inputs may produce different outputs, so there is no fixed expected value against which behaviour can be verified, and the naive application of cryptographic audit to AI fails at the first step. This paper takes a different route: separate what can be held invariant from what cannot. Credentials, delegation chains, prompt-template versions, access profiles, and controlexecution records are invariant by construction; model output is not. FLAP-X anchors the invariant set cryptographically and governs the variable residual with a calibrated tolerance, making non-deterministic multiagent systems retrospectively auditable. The dual-leaf attestation structure follows from this separation: Leaf 1 at the decision layer captures clause discharge, controls fired, and output hash; Leaf 2 at the workflow layer captures orchestration, delegation, and template version; the leaves are cross-linked and hash-bound to a principal chain rooted in a human agent owner. A four-check verification protocol operates across both surfaces. We parameterise a 15-condition test protocol in four parts-core verification (8), adversarial (3), governance lifecycle (3), and a comparative experiment (1) demonstrating two fault classes a single-surface record cannot handle: output substitution, which the single-surface record passes as a false negative, and surface attribution, which it cannot distinguish. We report honest negatives: adjacent-agent collusion producing mutually consistent false attestations passes verification, and a stolen signing key defeats signature checks; both are stated trust-boundary limitations addressed by the lifecycle layer, not the attestation layer. Effectiveness of the lifecycle controls at production scale remains future work; the author is actively seeking an empirical validation partnership.

---

## uid: `doi:10.2139/ssrn.7312718`

- title: Modelling the Transition towards Climate-Friendly Agriculture: A Simulation-Based Analysis
- authors: Anirban Sanyal
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7312718
- keyword hits: prompting

### abstract

This paper proposes a comprehensive framework to analyze sustainable transition finance in agriculture, beginning with a review of international efforts and modeling the transition using a partial equilibrium framework that incorporates firm dynamics and financing needs under different scenarios. Farmers face climate-induced productivity losses, prompting shifts to more sustainable crops that require upfront investments and cause temporary income declines, affecting loan affordability. While larger farmers can access formal credit, smaller ones depend heavily on government support. The model is then extended to a Dynamic Stochastic General Equilibrium (DSGE) framework, building on Jermann and Quadrini (2012), to capture forward-looking behavior, financial frictions, and the interactions among households, farmers, banks, and government in navigating climate shocks and policy responses. In this paper, calibration is based on empirical findings from the Making Agriculture Trade Sustainable (MATS) project, which promotes environmentally and socially sustainable agricultural trade. The MATS project provides valuable data by identifying trade policies, standards, and practices that support low-carbon, biodiversity-friendly farming while ensuring smallholder market access, thereby offering a robust basis for parameter selection in modeling sustainable agricultural transitions.

---

## uid: `doi:10.2139/ssrn.7303038`

- title: Gaze-Regularized Low-Rank Adaptation of Swin Transformers for Dental Panoramic Lesion Detection: A Rigorously Controlled Negative Result
- authors: S. M. Zain, Eram Mahamud
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7303038
- keyword hits: fine-tuning

### abstract

Background/Objective: Panoramic dental radiographs are read under time pressure, and deep learning systems proposed to assist this task are typically opaque. Expert eye-tracking data, which is available for a small number of publicly released datasets, has been proposed as a training signal that could both improve detection and anchor model attention to clinically meaningful regions. We test this hypothesis for dental lesion detection using a rigorously controlled design rather than a single-arm accuracy claim. Methods: We adapt an ImageNet-pretrained Swin-Tiny transformer with rank-8 LoRA adapters and a convolutional spatial decoder in a two-phase protocol: domain pre-training on OralXrays-9 (12,688 images, no gaze), followed by gaze-regularized fine-tuning on the Tufts Dental Database (TDD, 1,000 images with paired expert eye-tracking heat maps). A Kullback-Leibler gaze regularizer aligns the model's final-stage self-attention to normalized expert gaze density. Four experimental arms Phase-1 transfer, gaze fine-tuning (λ = 0.05), a matched λ = 0 ablation, and an external ImageNet ResNet-50 baseline are compared under identical five-fold cross-validation on a 900-image development pool, a 100-image held-out test set, and the DENTEX corpus (1,005 labeled images) as an out-of-distribution probe. Faithfulness (area over the perturbation curve, AOPC), human alignment (normalized scanpath saliency, NSS; Pearson correlation, CC), and an adapted false-positive/false-negative error taxonomy are computed for the gaze and ablation arms and compared as paired differences. matched cross-validation, an external non-gaze baseline, out-of-distribution testing, and a faithfulness/error-taxonomy audit that we argue should be a minimum standard for future gaze-supervision claims in medical imaging.

---

## uid: `doi:10.2139/ssrn.7305938`

- title: From Prompt to Organization Delegated Construction in Exploratory AI Work
- authors: Nghi Truong
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7305938
- keyword hits: ai agent

### abstract

Exploratory work cannot be fully planned in advance, yet AI agents depend heavily on written instructions. We study a sixteen-hour mathematical research run in which Shanmu Jin's one-page prompt led to a thirteenagent organization and a candidate proof of Crouzeix's conjecture. The prompt was neither a general request nor a detailed operating plan. It specified a dynamic multi-agent search: a diverse portfolio of initially independent routes, explicit tracking of approach families, grounded rules for blocking and reopening work, delayed sharing, adversarial checking, concrete reporting, and repeated synthesis by the first agent. It left the realized structure and procedures-headcount, hierarchy, assignments, timing, allocation, communication channels, and audit sequence-to that agent. Comparing the prompt with the public event record shows how these open choices were filled and how additional compatible practices appeared. We call this arrangement precise principles plus delegated construction. It is more viable when candidate components are much easier to check than to find, and less reliable when nominally separate agents share correlated errors.

---

## uid: `doi:10.2139/ssrn.7305358`

- title: Identity and Access Control for Autonomous AI Agents: Dual-Principal Authorization in Enterprise Settings
- authors: Leela Sai Krishna Udiga
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7305358
- keyword hits: ai agent

### abstract

Autonomous and semi-autonomous software agents now call tools, change records, and coordinate with other agents at machine speed. Identity and access management (IAM) in most enterprises still treats those agents as either human users with a session or as long-lived machine accounts with a shared secret. Neither treatment answers the questions that matter after an incident: which agent instance acted, on whose authority, for what task, and how that authority can be withdrawn without disabling the human. This working paper examines that gap as a problem of authorization design rather than of model safety alone. Drawing on existing protocol families (OAuth and OpenID Connect, SPIFFE, SCIM) and on recent industry and consortium writing on agent identity, I argue that privileged agent action should satisfy two principals at once: the agent as actor and the human or system as subject. Grants should also be bound to a declared purpose, a specific audience, and a short lifetime. I then set out a six-part control-plane reading of the same problem (identity, delegation, policy, enforcement, evidence, and lifecycle) and discuss how the combination behaves in common enterprise patterns, including user-delegated copilots, headless workers, tool gateways, and multi-agent chains. The paper is conceptual. It does not report a controlled experiment. Its contribution is a compact authorization rule, a mapping onto standards that organizations already run, and a statement of limits: identity controls cannot correct a purpose that was written too widely. AI disclosure: Generative writing tools were used for language editing, section organization, and typesetting of this working paper. The author reviewed the text, is responsible for the argument, and does not list any tool as a co-author.

---

## uid: `arxiv:2608.18852v1`

- title: SkillGate: Training In-Policy Skill Selection in Long-Horizon Agents
- authors: Qingyao Li, Wenxiang Jiao, Shuai Shao, Kangning Zhang, Yuan Lu, Yi Guo, Weiwen Liu, Weinan Zhang
- affiliations: not stated
- posted: 2026-08-19
- source: arXiv
- link: https://arxiv.org/abs/2608.18852v1
- keyword hits: agentic

### abstract

Agent frameworks increasingly package procedural knowledge as skills: instruction files an agent reads on demand, while public libraries now hold thousands of them. Which skill to read has thus become a decision the policy itself makes in the middle of an episode, yet no existing signal trains it. We show that the default remedy, outcome-rewarded RL over the candidate slate, cannot teach it, for a structural reason we identify and name selector credit starvation: under a broadcast, sequence-level advantage, the few tokens that name the chosen skill carry a vanishing share of the loss, and the credit they inherit is increasingly wrong-signed as trajectories lengthen. A correct choice is punished whenever the execution after it fails, even though the choice itself is among the most valuable decisions in the trajectory. Auditing a completed run's own training artifacts confirms all three properties, each worsening monotonically with horizon. SkillGate removes the failure by construction: it partitions the token support into two disjoint credit channels, outcome credit reaching only execution tokens, and a separate action-local advantage reaching exactly the skill-naming tokens, positive only when a trajectory's single read is the correct one. On five agentic benchmarks under a 16-candidate slate, SkillGate lifts a 9B policy from 40.8% to 53.2% trial success, well ahead of the identical budget spent on outcome reward alone, while cutting exposure to misleading candidates by two thirds and reading fewer skills.

---

## uid: `doi:10.2139/ssrn.7317622`

- title: Collaborative Intelligent Manufacturing System based on Large-Small Model Fusion and Retrieval-Augmented Generation
- authors: Xiao Lai, Han Wang, Zian Lu, Xiaohan Zhang, Xinyi Chen, Li Bai, Min Liu
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7317622
- keyword hits: agentic, ai agent, retrieval-augmented

### abstract

With the rapid advancement of intelligent manufacturing, industrial systems generate vast amounts of unstructured data, yet face significant challenges in data utilization, knowledge retrieval accuracy, decision-making efficiency, and human-machine collaboration. To address these issues, this paper proposes a domain knowledge-enhanced collaborative intelligent manufacturing system (CIMS) framework based on large-small model fusion and retrieval-augmented generation, which comprises three modules. First, the model of knowledge parsing and Retrieval-Augmented Generation for industrial document is introduced, featuring IndDocMaster (a high-precision unstructured data parsing model) enabling end-to-end document understanding through multi-source fusion and a data flywheel mechanism, significantly enhancing knowledge extraction quality. Second, a large-small model fusion based hierarchical industrial AI agent architecture from L1 to L4 is designed, achieving cognitive-execution synergy via large-model orchestration and small-model execution. Finally, a domain knowledge-enhanced agentic Agent-Human-Cyber-Physical System (A-HCPS) framework is established to enable autonomous, domain knowledge-enhanced collaborative decision-making process. Experimental results show that the proposed system outperforms existing methods in knowledge-enhanced industrial document parsing in the zinc oxygen-pressure leaching production processes, and near-expert-level maintenance decision-making with over 60% faster response in the high safety special equipment maintenance processes.

---

## uid: `doi:10.2139/ssrn.7285757`

- title: A Custom Artificial Intelligence Chatbot Created High Quality Health Outcome Descriptors for Rheumatoid Arthritis Treatment
- authors: Krista Dagsvik, Meghan Elliott, Wojtek Wiercioch, Anya Siddonns, Beverly  J. Shea, Annelies Boonen, Deborah  A. Marshall, Pakeezah Sadaat
- affiliations: not stated
- posted: 2026-08-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7285757
- keyword hits: chatgpt, retrieval augmented

### abstract

ObjectiveTo generate HODs for rheumatoid arthritis (RA) using a customized chatbot and evaluate their quality.MethodsWe developed a Retrieval Augmented Generation (RAG) chatbot in ChatGPT 4.0 to generate HODs for 11 RA outcomes, in standard and short formats (22 in total). The chatbot incorporated four frameworks for improving language complexity, structure, and comprehensibility, and custom, iteratively refined prompts. In a web-based survey, patients, clinicians and researchers from four international groups rated HODs across five quality attributes using Likert scale responses, with acceptable quality defined a priori as ≥70% agreement. Responses were collected in a cross-sectional web-based survey and reported following Checklist for Reporting Results of Internet E-surveys (CHERRIES) guidelines.ResultsThirty panelists completed the survey. Seven of eleven standard HODs (64%), and all eleven (100%) short HODs met the predefined acceptability threshold (≥70% agreement) across all five quality attributes. Standard HODs not meeting the acceptability threshold fell below the criterion in only one attribute, most commonly appropriateness for individuals with low health literacy, where agreement ranged from 50% to 91%. The attribute evaluating technical accuracy had an average rate of agreement of 86% for standard HODs, and 87% for short HODs. The attribute evaluating appropriateness for patients with low literacy had an average rate of agreement of 74% for standard HODs, and 89% for short HODs.ConclusionsHODs generated using a customized GPT4.0 chatbot were rated highly by experts for quality. This structured AI-assisted approach can facilitate the generation of HODs that are acceptable to clinicians and researchers, but still require human oversight and proof-reading.

---
