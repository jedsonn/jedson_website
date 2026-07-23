# Classification batch 318 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-318.answer.json` as a JSON array.

---

## uid: `arxiv:2606.26432v1`

- title: Embedding Foundation Model Predictions in Discrete-Choice Models with Structural Guarantees
- authors: Yingshuo Wang, Xian Sun, Yanhang Li, Zhichao Fan, Zexin Zhuang
- affiliations: not stated
- posted: 2026-06-24
- source: arXiv
- link: https://arxiv.org/abs/2606.26432v1
- keyword hits: foundation model

### abstract

Tabular foundation models achieve strong accuracy on choice prediction tasks, but their predictions often violate the economic logic those tasks require: raising a price can increase predicted demand, implied willingness-to-pay estimates are frequently negative or implausible, and unavailable alternatives receive nonzero probability. We propose a two-stage adapter that takes a foundation model's predicted choice probabilities as a precomputed feature and embeds them inside a multinomial logit's utility. In Stage 1, we fit the multinomial logit's structural coefficients by maximum likelihood with sign constraints; in Stage 2, we freeze those coefficients and fit a small neural correction operating on the foundation model's predictions. We prove that this composition exactly preserves the multinomial logit's marginal rate of substitution, so analytically computable value-of-time becomes a mathematical guarantee rather than an empirical accident. Across three datasets and two foundation models, the adapter gains 6.4 percentage points (pp) of test accuracy on average over the multinomial logit and up to 12.8 pp, maintains 100% cost monotonicity, and produces values of time within the published transportation-economics range on the transportation datasets. Performance degrades gracefully under foundation-model context restriction, retaining at least 6 pp of accuracy gain even at 10% of the original foundation-model context.

---

## uid: `arxiv:2606.26403v1`

- title: ProfileFoundry: A Synthetic Person-Object Substrate for Privacy, Memory, and Tool-Use Evaluation in LLM Agent
- authors: Sriram Selvam, Anneswa Ghosh
- affiliations: not stated
- posted: 2026-06-24
- source: arXiv
- link: https://arxiv.org/abs/2606.26403v1
- keyword hits: llm

### abstract

Foundation-model research increasingly needs data about people: user state, personal histories, relationships, contact-like fields, documents, and longitudinal updates. Real user data is difficult to share, perturb, audit, or redistribute responsibly, while independently generated fake fields rarely preserve the cross-field and temporal consistency needed for controlled evaluation. We present PROFILEFOUNDRY, a deterministic generator and fixed reference release of 100,000 adult synthetic Person Objects across eight locales. Each object combines a typed current snapshot, household, family, and employer links, snapshot-aligned events, normalized relational views, and generation provenance. The release contains 709,228 events, 40,338 households, 52,491 employers, and 518,564 directed relationship edges. We report evidence in separate categories: selected population-marginal comparisons, per-object invariant checks, release-wide referential and temporal closure, and coincidence/provenance screens. PROFILEFOUNDRY is not a population-fidelity model, a rendered-text corpus, or a formal privacy mechanism. Instead, it is a responsible synthetic source layer for constructing downstream foundation-model evaluations involving memory, privacy, document understanding, record linkage, and agent state while keeping the synthetic person behind each artifact inspectable

---

## uid: `arxiv:2606.26350v1`

- title: OpenFinGym: A Verifiable Multi-Task Gym Environment for Evaluating Quant Agents
- authors: Kaicheng Zhang, Wen Ge, Lei Jiang, Weixin Yang, Jordan Langham-Lopez, Jialin Yu, Lukasz Szpruch, Hao Ni
- affiliations: not stated
- posted: 2026-06-24
- source: arXiv
- link: https://arxiv.org/abs/2606.26350v1
- keyword hits: large language model

### abstract

Although large language model agents are increasingly applied to quantitative-finance workflows, their evaluation remains fragmented across isolated tasks, while the financial relevance of benchmark tasks is often overlooked. Yet financial workflows are inherently multi-stage, spanning interdependent tasks such as forecasting, strategy construction, risk management, and trading. Existing platforms typically focus on a single task, and can therefore overstate agent competence and fail to reveal weaknesses in generalization, real-market interaction, and financially meaningful decision-making. We introduce OpenFinGym, a unified gym environment for quantitative-finance agent development that covers forecasting, market generation, real-time trading, and fraud detection under a single execution and verification interface. OpenFinGym additionally provides an automated task-construction pipeline that turns quantitative finance publications into executable task packages; a containerised runtime with a host-side verifier service that supports scalable agent rollouts and prevents runtime train-test leakage; a paper trading engine with a low-latency data-stream design; deferred-resolution support for long-horizon and event-market forecasts; and integration for SFT and RL post-training

---

## uid: `arxiv:2606.26277v1`

- title: From Clicks to Intent: Cross-Platform Session Embeddings with LLM-Distilled Taxonomy for Financial Services Recommendations
- authors: Dianjing Fan, Yao Li, Kyaw Hpone Myint, Dwipam Katariya, Alexandre G. R. Day, Pranab Mohanty, Giri Iyengar
- affiliations: not stated
- posted: 2026-06-24
- source: arXiv
- link: https://arxiv.org/abs/2606.26277v1
- keyword hits: llm

### abstract

Sequential user behavior modeling is widely adopted in industrial recommender systems; however, significant gaps remain in financial services, where pre-login web interactions and authenticated in-app experiences differ drastically. Specifically, pre-login web users typically explore new products, whereas logged-in app users focus on account servicing. Due to the challenge of cross-channel entity resolution (e.g., matching anonymous web sessions to authenticated mobile accounts), web-based intent signals remain underutilized for post-authentication personalization. Existing methods for capturing web-based intent are often ad-hoc and narrow, lacking the flexibility to support both quantitative downstream recommendations and qualitative understanding at scale. In this work, we propose a scalable and dual-purpose intent prediction framework for web-based interactions and demonstrate its applicability for personalization. Our approach transforms raw web clickstreams into two outputs: a self-supervised Transformer encodes multi-modal clickstreams into a compact session embedding, while an LLM-based taxonomy generation and distillation pipeline produces interpretable intent labels. Our system demonstrates that self-supervised clickstream representations combined with LLM-distilled taxonomies can jointly serve quantitative tasks and qualitative understanding in production: on the mobile homepage tile ranking task, the session embedding improves macro Recall@1 by 1.88% and reduces Log Loss by 13.38% over production baselines. On the user conversion prediction task, the embedding outperforms the LLM labels by 4.3% on micro F1, while the distillation layer delivers interpretable labels at ultra-low latency with only a 7% performance drop.

---

## uid: `arxiv:2606.25487v2`

- title: How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring
- authors: Yang Gao
- affiliations: not stated
- posted: 2026-06-24
- source: arXiv
- link: https://arxiv.org/abs/2606.25487v2
- keyword hits: llm

### abstract

Almost every paper on LLM jailbreaks and prompt injection reports an attack-success rate (ASR), and that number is assigned not by people but by an automated judge: either a safety classifier trained for the task, or a general chat model prompted to grade. The judge is rarely checked. We check it. Using 596 human-labeled completions from the HarmBench classifier validation set, we compare the two judge families against human majority votes and then attack them. The two families fail in opposite ways. The dedicated classifier over-flags (precision 0.835, recall 0.974); three different LLM-as-judges keep high precision (0.81 to 0.94) but show erratic recall (0.06 to 0.65), so the same responses produce very different ASR depending on which judge scores them. The two families also differ sharply in robustness. Wrappers that leave the harmful text untouched and only add benign framing flip every LLM-judge between 57% and 100% of the time, and a single prepended refusal sentence accounts for much of this (39% to 88%). The dedicated classifier resists these surface attacks (at most 6.7%), but a white-box GCG attack on its open weights flips 70% of confident true positives (21 of 30; 95% CI 54 to 86%) even at a small optimization budget. A two-annotator audit confirms the attacks leave the harm intact: every one of 80 sampled flips still contained the harmful content. Because a large and growing share of reported ASR comes from LLM-judges, many such numbers are unreliable both on average and under deliberate pressure. We recommend that papers report judge precision and recall on a human-labeled slice, report ASR corrected for judge precision, and include an adversarial check of the judge. Our code is released.

---

## uid: `arxiv:2606.25375v2`

- title: Text Over Image: Auditing Multimodal Robustness in Synthetic Medical Image Detection
- authors: Ching-Hao Chiu, Hao-Wei Chung, Gelei Xu, Xueyang Li, Pin-Yu Chen, John Kheir, Meysam Ghaffari, Carlos Morato
- affiliations: not stated
- posted: 2026-06-24
- source: arXiv
- link: https://arxiv.org/abs/2606.25375v2
- keyword hits: generative ai

### abstract

With the rapid adoption of generative AI, synthetic medical images pose growing risks, including diagnostic deception and insurance fraud. Although prior work has explored vision-language model (VLM)-based synthetic image detection, these evaluations typically consider images in isolation. In clinical practice, however, images are interpreted alongside structured records and metadata, and VLMs are increasingly deployed under joint image-record inputs. We uncover a previously underexamined multimodal vulnerability: when given both modalities, VLMs may overweight record context in authenticity judgments, such that the same image receives different predictions solely due to changes in its accompanying text. This raises concerns about robustness in real-world deployment. To systematically characterize this effect, we reformulate synthetic medical image detection as an audit of multimodal robustness at the image-record interface and introduce a paired benchmark that holds the image fixed while swapping controlled metadata variants. Across multiple imaging modalities, we evaluate diverse open-weight and frontier API VLMs and find that changing the metadata context alone can flip authenticity judgments, with accuracy on authentic images dropping by 61.1% on average under an explicit AI-origin tag. We further propose an inference-time mitigation pipeline that detects and neutralizes provenance shortcuts without model retraining, substantially outperforming direct prompt-based suppression on the affected subset. Our benchmark provides a standardized tool for assessing and improving multimodal robustness beyond image-only settings. Code and data will be released upon acceptance.

---

## uid: `doi:10.2139/ssrn.6905638`

- title: The Laws of Intelligence: Computation Efficiency and the Physical Scaling Limits of AI Systems
- authors: Sanjay Kumar
- affiliations: not stated
- posted: 2026-06-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6905638
- keyword hits: large language model, large language models

### abstract

This paper develops a unified physical theory of intelligence from first principles. Intelligence is treated not as an abstract property of cognition alone, but as a measurable physical process carried out by matter, energy, information and control. The central claim of the paper is that intelligence is the rate at which a system generates useful knowledge, where useful knowledge is defined as information that helps maintain desired state, preserve viability, or expand e ective control over the environment. From this starting point, the paper builds a general framework connecting intelligence to entropy reduction, thermodynamic work, computational limits, communication limits, and control structure. The analysis begins by formalizing intelligence in information-theoretic terms and showing that useful knowledge corresponds to the reduction of uncertainty over relevant states. This yields an entropy-based interpretation of intelligence as directed reduction of relevant entropy rather than mere information accumulation. The framework then connects this definition to Landauer's principle, the Margolus-Levitin quantum speed limit, the Bekenstein bound, mass-based computational bounds, and relativistic communication limits, leading to a unified physical upper bound on intelligence for any system. On this basis, the paper distinguishes between maximum possible intelligence and realized intelligence, and derives the corresponding intelligence e iciency relation, thermodynamic intelligence parameter, intelligence density relations, and structural e iciency terms that govern real architectures. The theory is further extended into a control-theoretic and dynamical form. The paper develops the concepts of control entropy and control potential, and introduces an intelligence Lagrangian, an action principle, and a field equation describing the spatial propagation of controllable order. In this formulation, intelligence is not only a bounded quantity but also a dynamical process through which physical systems convert energy and structure into useful environmental influence over time. The framework is then applied to both limiting and practical cases. At the theoretical limit, the paper analyzes computronium as the idealized maximum-intelligence substrate and derives corresponding scaling relations for matter configured for near-optimal intelligence generation. At the practical limit, it interprets today's large language models and AI infrastructure through the lens of intelligence e iciency, showing why present systems remain far below physical limits and why memory movement, communication bottlenecks, retrieval, sparsity, modularity, and persistent knowledge structures may be more important for future progress than brute-force scaling alone. Taken together, the paper aims to place intelligence on a foundation analogous to thermodynamics: not as a description of one particular mind or machine, but as a general law-governed physical process. In this sense, Intelligence EAiciency Theory provides a common framework for comparing biological, artificial, and hypothetical future intelligence systems, while also defining the ultimate bounds and governing principles of intelligence in the physical universe.

---

## uid: `doi:10.2139/ssrn.6979919`

- title: Tort Law at the Frontier of Artificial Intelligence
- authors: Ketan Ramakrishnan
- affiliations: not stated
- posted: 2026-06-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6979919
- keyword hits: foundation model

### abstract

The frontier of contemporary AI development is dominated by AI systems built on foundation models--highly versatile algorithms, trained in the first instance on broad swathes of data, that can function as tools and agents across a wide variety of commercial, social, military and political domains. For the moment, at least, the process of developing and releasing foundation models is subject to anemic formal regulation and haphazard ex ante governance. Until that changes, it is largely the common law of torts - our society's most ancient and general legal mechanism for governing serious risks of physical injury - that will govern the frontier of AI development. This Article offers an in-depth conceptual, normative, and doctrinal examination of tort liability for foundation model development and release. It provides a qualified defense of the tort of negligence - the common law's broadest and most flexible cause of action - as the principal doctrinal foundation of the tort system's governance of this novel domain. Legal scholarship on AI liability has been quite hostile to negligence. By contrast, this Article argues that the generality and flexibility of the negligence tort - and its greater sensitivity to the externalized benefits of risky activity - render it well-suited to the polymathic and protean functionality of foundation models. Only the tort of negligence has the breadth and flexibility to address the range of important pathways - including internal deployments, inadequate model weight security, targeted entrustments of non-defective models, and open source releases - by which foundation model developers might cause serious harm. Analyzing the choice between negligence and competing doctrinal regimes does, however, suggest important ways in which common law courts should incrementally develop the law of negligence, in order to properly reflect the risks and capabilities of foundation models. For example, courts should expand the scope of the duty of care in negligence, in order to provide redress when foundation models cause economic or emotional injury by behaving in ways that are closely analogous to serious human wrongdoing (e.g., certain crimes and intentional torts, such as theft, deceit, and outrage). But the Article's analysis also suggests certain fundamental pathologies of tort liability as a mechanism of AI governance - pathologies that no amount of doctrinal development will adequately cure. In particular, the specter of tort liability can be expected to disincentivize frontier AI developers from investigating and disclosing many of the novel and poorly understood risks that frontier AI development may pose. That is especially disturbing given that our society is relying quite heavily, for its ability to discover and understand these risks, on frontier AI developers themselves. Thus, tort liability is not only inadequate as a mechanism of frontier AI governance; in certain important respects, it is actively perverse, and its perverse effects must be countered by governance institutions of a different kind. Ultimately, a robust regime of ex ante regulation - under which government institutions or credibly neutral third-party experts are empowered to investigate, evaluate, and mitigate the risks of frontier AI development - is urgently required in frontier AI governance.

---
