# Classification batch 171 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-171.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6997675`

- title: Beyond Reactive Agents: Uncertainty-Gated Meta-Reasoning for Tool-Augmented Decision-Making
- authors: Yiyao Zhang, Diksha Goel, Hussain Ahmad, Jun Shen
- affiliations: not stated
- posted: 2026-06-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6997675
- keyword hits: large language model, llm

### abstract

Large Language Model (LLM) agents often plan, act, observe tool feedback, and recover only after errors occur. This reactive design is useful for short horizons but can be brittle in multi-step decision-making where early mistakes compound. This paper studies whether pre-execution uncertainty-aware control and persistent reflective memory can be integrated into a more auditable tool-use controller. We present the Meta-Reasoning Insight Framework (MRIF), a multi-agent architecture that augments a planner–executor loop with an Uncertainty Estimation Module (UEM) for risk gating and a Metacognitive Reflection Loop (MRL) that stores cross-episode experience in a Knowledge Graph. We position MRIFas a systems integration of familiar ideas—uncertainty scoring, reflective updating, and structured memory—rather than as a new agent paradigm. The paper includes a comparative design analysis of representative agent patterns grounded in public artifacts and a limited ToolTalk pilot evaluation against transparent matched-budget baselines. In this pilot, MRIF reaches a 61.3% task success rate, 4.9 absolute points above Metagent-P, with higher tool-call argument accuracy (91.2%) and fewer unnecessary interventions (14.5%). Because the current artifact does not yet include exhaustive ToolTalk coverage, full task identifiers, prompts, seeds, these results should be interpreted as preliminary evidence aboutToolTalk-style tool dialogue rather than as a benchmark ranking or proof of broad generalization.

---

## uid: `doi:10.2139/ssrn.7001916`

- title: Displacement or Repartitioning in the Mobile App Ecosystem after Generative AI: A Niche Analysis
- authors: Minjeong Ham
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7001916
- keyword hits: chatgpt, generative ai, generative artificial intelligence

### abstract

The public release of ChatGPT in November 2022 raised a recurring concern that established digital products would be displaced by generative artificial intelligence (AI). This study examines this concern in the mobile app ecosystem by analyzing how generative AI repartitioned market-level niches, using monthly download-share distributions across app categories as aggregate indicators of where applications attract demand. Drawing on niche theory, the study measures whether AI-enabled and non-AI applications drew demand from similar parts of the mobile app market (overlap), how widely each of the AI and non-AI groups distributed its demand (breadth), and whether overlap was directional. Using a monthly panel of U.S. Google Play mobile applications from January 2021 to December 2024, the study finds limited evidence of wholesale displacement. Instead, the findings indicate a pattern of incumbent-led niche repartitioning, with the strongest evidence emerging from subgroup, directional, and category-level decompositions: established applications that adopted AI were more central to the shared niche space than AI-native entrants. These findings reframe the competitive impact of generative AI as a repartitioning of demand led by incumbents that absorb the new capability, rather than a wave of displacement led by AI-native entrants. These patterns bear on platform-competition policy, suggesting that contestability may depend less on access to AI capabilities than on the data and distribution assets that govern their deployment.

---

## uid: `doi:10.2139/ssrn.6888859`

- title: Individual Contribution to Collective Intelligence: Toward a Fair Knowledge Economy in the Age of Generative Artificial Intelligence
- authors: Amangeldi Nurmanbetov
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6888859
- keyword hits: generative ai, generative artificial intelligence

### abstract

The rapid advancement of generative artificial intelligence (AI) has fundamentally transformed the production, dissemination, and utilization of knowledge. While contemporary AI systems increasingly rely on large-scale interactions with users, the economic value generated through expert contributions remains largely unrecognized. This paper examines the structural asymmetry between AI platform owners and highly qualified users who continuously enrich AI ecosystems through original theories, methodological innovations, empirical data, and interdisciplinary insights. Drawing upon knowledge economy theory, institutional economics, digital commons theory, and scholarship on data labor, the study proposes a conceptual framework for recognizing, evaluating, and rewarding intellectual contributions within generative AI ecosystems. A hierarchical model of intellectual value creation is introduced, along with the concept of the "AI Knowledge Contributor" as a new economic actor. The paper outlines institutional principles-transparency, reciprocity, and fair compensation-for building a more equitable knowledge economy in which collective intelligence emerges through a balanced human-AI partnership.

---

## uid: `doi:10.2139/ssrn.7002050`

- title: DriveJudge: Tool-Grounded Evaluation of Generative Driving Simulations with Vision–Language Models
- authors: Matthieu Scharffe, Mariam Hassan, Alexandre Alahi
- affiliations: not stated
- posted: 2026-06-26
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7002050
- keyword hits: chain-of-thought, prompting, qwen

### abstract

Generative driving simulators and visual world models are increasingly used to produce synthetic driving scenarios for autonomous-driving development, scenario testing, and data generation. However, evaluating whether such videos are behaviorally correct remains difficult as a video may appear visually plausible while depicting unsafe maneuvers, traffic-rule violations, physically inconsistent motion, or generation artifacts. Vision–Language Models (VLMs) provide a natural interface for open-ended evaluation through language, but their reliability as judges of synthetic driving videos has not been systematically established. We introduce DriveJudgeBench, a transportation-grounded benchmark for evaluating VLM judging of generative driving simulation. The benchmark contains 1,597 curated synthetic driving clips and 7,371 manually annotated video–question pairs spanning sixcategories: reality detection, artifact recognition, safety assessment, traffic-law compliance, spatio-temporal reasoning, and visual understanding. Across a broad set of off-the-shelf VLMs, we find that most models are unreliable judges of synthetic driving behavior. Open-source models achieve only 21.9–30.9% overall accuracy, despite strong performance on static visual-understanding questions. An inspection of the models’ reasoning reveals that these errors are systematic rather than random. Base VLMs often rely on static visual cues and normality priors, leading to always-real judgments, artifact blindness, and over-compliance intraffic-law questions. To address these failures, we propose a training-free tool-augmented judging framework that grounds VLM decisions in external evidence: optical flow for motion cues, segmentation-based crop-and-zoom for localized visual inspection, and frequency-domain anisotropy for generated-video provenance. Built on Qwen3-VL, our agent improves overall accuracy from 21.9% to 60.1%, with large gains on reality detection, artifact recognition, traffic-law compliance, and safety assessment. Ablations show that increasing the number of input frames or using Chain-of-Thought prompting is insufficient; reliable improvement comes from tool-measured evidence that targets the failure mode being judged. The results suggest that off-the-shelf VLMs should not be used as unaudited black-box judges for generated driving rollouts in safety-relevant evaluation pipelines, while tool-groundedVLM judging offers a practical path toward more reliable evaluation of generative driving simulation.

---

## uid: `arxiv:2606.28153v2`

- title: Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models
- authors: Yanchen Yin, Dongqi Han, Linghui Li
- affiliations: not stated
- posted: 2026-06-26
- source: arXiv
- link: https://arxiv.org/abs/2606.28153v2
- keyword hits: large language model, large language models, llm

### abstract

Jailbreak attacks bypass LLM safety alignment, yet their mechanisms remain poorly understood. We provide evidence that attacks do not comprehensively eliminate safety features, but instead selectively suppress specific attention heads. We identify two functionally differentiated types: Adversarially Compromised Heads (ACHs) concentrated in early layers, which are suppressed under attacks, and Safety-Aligned Heads (SAHs) in mid-layers, which maintain robust activations even when attacks succeed. Ablation studies support the causal role of ACHs and the contribution of SAHs to robust activations: suppressing a small number of ACHs is sufficient to induce jailbreak-like behavior on normally refused inputs, while removing SAHs substantially weakens mid-layer safety activations. Token-level attribution further shows that ACH suppression is driven specifically by attack-template tokens, providing a mechanistic account of why attacks can bypass refusal decisions through ACH suppression while leaving internal safety signals sustained by SAHs -- a phenomenon we term Robust Harmful Features. To validate the practical significance of this robustness, we show that simply reading these persistent activations -- without any training -- yields competitive aggregate detection performance with strong adversarial robustness.

---

## uid: `doi:10.2139/ssrn.6890780`

- title: A Reference Architecture for LLM-Powered Incident Response in Regulated Financial Services
- authors: Ganesh Kutty Murugan
- affiliations: not stated
- posted: 2026-06-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6890780
- keyword hits: gpt-4, llm

### abstract

Every major technology company now has some version of an LLM-assisted incident response system. Google has written about theirs. Microsoft published a paper on root cause analysis with GPT-4. But none of them operate under Sarbanes-Oxley. None of them have to worry about a PCI assessor asking why cardholder data appeared in an API call to OpenAI. None of them need their Model Risk Management team to sign off before changing a prompt template. Banks do. And that difference is the entire architecture. I present a reference architecture for deploying LLM-assisted incident response in U.S. regulated financial services. Five overlapping regulatory frameworks (SOX, PCI DSS v4.0, SR 11-7, FFIEC, and recent AIspecific guidance) interact to produce constraints that make direct adoption of published approaches from unregulated companies infeasible. The six-layer architecture described here is designed around a principle I call compliance by construction, where regulatory requirements are embedded as architectural layers that data must physically traverse rather than bolted on as after-the-fact controls. The paper includes a synthetic evaluation framework allowing any institution to validate the approach without exposing proprietary operational data.

---

## uid: `doi:10.2139/ssrn.6892520`

- title: Produce or Delegate? A Transaction-cost Theory of Vertical Integration: An Old Problem in the Age of AI
- authors: Jian Ding, Yixiao Zhou
- affiliations: not stated
- posted: 2026-06-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6892520
- keyword hits: chatgpt, deepseek

### abstract

This paper argues that recent differences between ChatGPT, DeepSeek, and other AI platforms reflect an old problem of economic organization rather than a purely technological divergence. The problem is whether the owner of a core asset should organize an adjacent commercial layer through specialization or vertical integration. Specialization and vertical integration are alternative ways of organizing that adjacent layer. The choice depends on the comparison between external transaction costs and internal management costs. External transaction costs include the costs of searching for capable outside actors, negotiating the relevant terms, and enforcing contractual performance. Internal management costs include the costs of supervising, coordinating, pricing, incentivizing, and organizing the activity within the firm. In the empirical cases examined below, this comparison often turns on whether outside performance can be enforced at acceptable cost. When outside performance is costly to enforce, vertical integration or strong control is more likely; when it can be enforced at acceptable cost, specialization becomes more feasible. The paper examines this tradeoff through comparative evidence from luxury and beauty groups, restaurants, franchising, logistics, contract manufacturing, complex system integration, and AI applications. Core luxury retail, fresh-prep food service, JD logistics, ASML system integration, and AI coding workflows illustrate cases in which outside performance is difficult to enforce because rent depends on service quality, outlet execution, fulfillment reliability, system integration, or workflow feedback. Beauty and eyewear licensing, standardized franchising, marketplace logistics, Nike and adidas contract manufacturing, and dispersed AI vertical applications illustrate cases in which outside performance can be enforced at acceptable cost because the relevant routines or interfaces are sufficiently standardized. In these cases, outside actors can perform the layer without destroying the rent attached to the core asset. In AI, this framework helps explain why coding workflows are attractive candidates for internalization or platform control, while dispersed vertical applications are more likely to be delegated to downstream firms, developers, cloud providers, and system integrators.

---

## uid: `arxiv:2606.28679v1`

- title: Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks
- authors: David Mellafe Zuvic
- affiliations: not stated
- posted: 2026-06-27
- source: arXiv
- link: https://arxiv.org/abs/2606.28679v1
- keyword hits: llama, llm

### abstract

Tool-using LLM agents increasingly read untrusted content while holding side-effecting tools such as payments, email, CRM, and infrastructure APIs, yet common framework defaults still conflate tool exposure with authorization. We audit whether LangChain/LangGraph, LlamaIndex, and the Stripe Agent Toolkit re-authorize each model-emitted call, with concrete argument values, before execution. Across pinned public-source commits, all three provide capability gating by default, but none provides a deterministic fail-closed per-call value authorization gate by default. We introduce ScopeGate, a five-stage PDP/PEP for agent tool calls: scope, authorization, money ceiling, idempotency, and default deny. Evaluation shows the identical unauthorized payout call executes under LangChain's default dispatch (with a companion LlamaIndex PoC) but is denied by ScopeGate; the tested control reports 0/48 static bypasses, 0/29 unauthorized attempts (40-iteration adaptive run), 0/10 benign false-denies, and Latam-GPT payment-agent containment at 10/10. ASR denotes attempted unauthorized action, containment is not a cure, deployment-tier claims are inference over measured model classes, and no CVE is asserted.

---
