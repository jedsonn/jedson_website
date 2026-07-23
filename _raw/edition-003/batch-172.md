# Classification batch 172 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-172.answer.json` as a JSON array.

---

## uid: `arxiv:2606.29654v1`

- title: Budgeted Act-or-Defer Multi-Agent LLM Deliberation with Local Reliability Bounds
- authors: Mengdie Flora Wang, Haochen Xie, Guanghui Wang, Devin Zhang, Jae Oh Woo
- affiliations: not stated
- posted: 2026-06-28
- source: arXiv
- link: https://arxiv.org/abs/2606.29654v1
- keyword hits: llm, llms

### abstract

Multi-agent deliberation among LLMs can improve reasoning, but deployment requires deciding when the current answer is reliable enough to act on and when it should be escalated to human review. We formulate this as budgeted act-or-defer decision making. At each round, the system maps the debate prefix to a low-dimensional state, computes a $k$-nearest-neighbor lower confidence bound on state-conditional correctness using calibration data, and acts only when the bound exceeds a user-specified reliability threshold. The certificate controls wrong actions through the decomposition $β= δ+ α+ \varepsilon_{\mathrm{act}}$, separating calibration failure, residual action risk, and representation gap. The guarantee is conditional, not distribution-free: it relies on a valid local bias envelope and an action-region representation-gap bound, and each assumption is paired with falsification-style diagnostics. Because the same absolute wrong-action budget has different meanings across tasks of different difficulty, we set budgets relative to each task's final-round error using training data only, and evaluate safety by normalized budget usage $\mathrm{WA}/β$. On six benchmarks against nine baselines, the method uses 9--12% of the pre-declared budget on activated datasets, reaching up to 84% automation and 96% acted-on accuracy; on stress-test datasets, it defers rather than forcing unreliable automation. Rather than relying on per-task post-hoc threshold search, the method prospectively converts a user-declared wrong-action budget into an auditable act-or-defer operating point before deployment, under explicitly stated assumptions.

---

## uid: `arxiv:2606.29537v2`

- title: OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks
- authors: Mengqi Yuan, Zilong Zhou, Xinzhuang Xiong, Weiming Wu, Jiayang Sun, Jiamin Song, Kaiqian Cui, Bowen Wang
- affiliations: not stated
- posted: 2026-06-28
- source: arXiv
- link: https://arxiv.org/abs/2606.29537v2
- keyword hits: claude, gpt-5

### abstract

Existing computer-use benchmarks fail to capture the realism, complexity, and long-horizon demands of real-world computer use, limiting their ability to reveal the limitations of frontier agents. We introduce OSWorld 2.0, a benchmark of 108 long-horizon computer-use workflows across everyday and professional tasks, designed to capture complex and challenging real-world phenomena. Each task represents a realistic end-to-end workflow that takes human users a median of about 1.6 hours to complete and requires an average of 318 tool calls with Claude Opus 4.7 using maximum thinking, compared with about 30 in OSWorld 1.0. OSWorld 2.0 targets challenge phenomena that are common in real workflows yet underrepresented in prior benchmarks, spanning interaction-design challenges such as streaming interaction and dynamic environments, as well as agent-pattern challenges such as cross-source reasoning, implicit-state inference, and visual-spatial precision. Tasks are grounded in authentic input artifacts and cross-referenced against realistic stateful user profile data, and include separate safety reports auditing safety-sensitive execution. Under our primary binary-completion metric at 500 steps, Claude Opus 4.8 with maximum thinking and batched tool calls scores best but still completes only 20.6% of tasks at a 54.8% partial score; GPT-5.5 is far more token-efficient yet plateaus near 13%. These results show that current agents are still far from professional-level computer use: rather than stumbling on basic GUI control or coding, they lose track of constraints, miss information that arrives mid-task, guess rather than ask the user, and skip verification, struggling most when a task hinges on hidden state they must recover.

---

## uid: `doi:10.2139/ssrn.6894862`

- title: Cloud Value Chains in the Age of AI
- authors: Shi Chen, Vinayak Deshpande
- affiliations: not stated
- posted: 2026-06-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6894862
- keyword hits: foundation model, generative ai

### abstract

The rapid adoption of generative AI is transforming cloud computing from a virtualized service platform into a tightly coupled, capital-intensive value chain spanning upstream supply networks (hardware, energy, and data), midstream AI data centers, and downstream AI platform ecosystems. In this AI era, traditional cloud assumptions-predictable performance from provisioned resources, frictionless elastic scaling, and unconstrained upstream inputs-are breaking down due to heterogeneous training and inference workloads, token-based performance measurement and pricing, and two-sided information asymmetry regarding demand characteristics and providers' hidden operational controls. To address these fundamental changes, this paper proposes an end-to-end framework for analyzing AI-driven cloud value chains from a holistic operations management (OM) perspective. Using this framework, we (i) articulate how AI workloads and production pipelines differ fundamentally from those of traditional cloud computing; (ii) map the key actors and interactions across downstream platform ecosystems, midstream AI data centers, and upstream supply networks; and (iii) synthesize emerging industry practices to develop a research agenda spanning strategic (e.g., coopetition, vertical integration, and long-term capacity expansion under sustainability objectives and policy constraints), tactical (e.g., pricing, capacity reservation and allocation mechanisms, and procurement of hardware, energy, and data services), and operational (e.g., compute pipeline scheduling, congestion control, and grid contingency planning) decisions. The proposed framework helps managers and policymakers diagnose bottlenecks and incentive conflicts while identifying their underlying drivers. In particular, AI platform providers should align pricing and contracting mechanisms with output uncertainty and information asymmetry, while cloud infrastructure and foundation model providers should design capacity reservation, allocation, and real-time pipeline control policies that reflect training-inference differences and throughput-latency tradeoffs. Together, these challenges require coordinated procurement, capacity planning, and operational strategies to scale AI infrastructure efficiently, responsibly, and sustainably.

---

## uid: `doi:10.2139/ssrn.7006198`

- title: Health AI Literacy: An Emerging Social Determinant of Health in the Age of Generative AI
- authors: Jasmine Chiat Ling Ong, Kabilan Elangovan, Matthew Yu Heng Wong, Jun Jie Benjamin Seng, Iain Beehuat Tan, Lian Leng Low, Lionel  Tim-Ee Cheng, Daniel Shu Wei Ting
- affiliations: not stated
- posted: 2026-06-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7006198
- keyword hits: generative ai, generative artificial intelligence

### abstract

Generative artificial intelligence is rapidly transforming how individuals access and interpret health information. Patients have consistently accessed these artificial intelligence (AI) systems, and surveys and chat log analyses from organizations such as OpenAI and Microsoft indicate that a substantial proportion of use already involves health-related queries. More recently, product launches from major AI labs have increasingly been designed to directly target patient-facing use cases, further reinforcing this trend. Existing constructs such as health literacy and digital health literacy do not fully capture the competencies required to safely engage with AI-generated outputs. In this paper, we propose health AI literacy as a distinct construct and emerging social determinant of health, defined as the ability to critically, safely, and effectively interact with AI-enabled health technologies. We introduce a conceptual framework comprising six domains: functional AI competence, structural understanding, interpretive competence, clinical risk awareness, data and governance awareness, and social and equity awareness. We further discuss how disparities in health AI literacy may create an "AI health divide," influencing healthcare utilization, trust in digital health systems, and health outcomes at both population and global levels. Advancing measurement, education, and policy will be critical to ensure that AIenabled healthcare improves equity rather than amplifies existing disparities.

---

## uid: `doi:10.2139/ssrn.7023228`

- title: Breaking Bad Intentions: Identifying Semantic Drift in Multi-Turn Language Model Inputs
- authors: Emmanuel Amo, Mary  L. Cummings, Wanyi Chen
- affiliations: not stated
- posted: 2026-06-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7023228
- keyword hits: large language model, large language models, llm

### abstract

Multi-turn interaction fundamentally changes the safety landscape for large language models, as potentially harmful intent can be distributed across multiple individually benign queries. Existing defenses struggle to detect coordinated misuse that emerges at the level of conversational trajectories. This paper addresses this gap by framing deceptive questioning as a problem of semantic drift in embedding space. Each multi-turn user interaction is represented as a set of embedded questions anchored to a fixed reference vector, from which a compact set of geometric and similarity-based features is extracted to capture angular coverage, distance structure, linearity, and internal semantic coherence. Using these features, we trained a lightweight neural classifier to distinguish non-deceptive from deceptively coordinated question sets attepting to illicit information about developed methamphetamine in a fully black-box, transcript- only setting. The approach is evaluated across four experimental conditions. Results show strong performance across experimental settings. We also conducted a cross-model generalization analysis using an external dataset constructed around a different harmful task. Despite this shift in domain, the proposed features retain meaningful discriminative power, indicating that they capture structural properties of coordinated deceptive questioning rather than topic-specific artifacts. Detailed error analyses further reveal that false negatives arise primarily from geometric overlap near the decision boundary, while false positives remain partially sensi- tive to specific lexical cues. Together, the results demonstrate that multi-turn geometric structure provides a scalable foundation for deception detection, while underscoring the importance of jointly considering geometric and lexical effects in robust LLM safety monitoring

---

## uid: `doi:10.2139/ssrn.6835301`

- title: Investor Protection in Venture Capital: How Do Legal Systems Shape Contracting?
- authors: Chen Lin, Yu-Jane Liu, Lai Wei, Dan Wen, Yusheng Ye
- affiliations: not stated
- posted: 2026-06-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6835301
- keyword hits: large language model, llm

### abstract

This paper examines how legal systems shape contractual investor protection by using a distinctive feature of China’s venture capital (VC) market, where investments are structured either through offshore entities governed by common law or through onshore entities subject to domestic civil law. This institutional duality generates substantial within-market variation in legal origin under a shared economic environment, providing empirical leverage to study how statutory legal regimes interact with private contracting. Using granular contract-level data, we construct a novel investor protection index and document that common-law deals adopt significantly stronger protective terms than civil-law deals, consistent with complementarity between statutory and contractual investor protection. However, this relationship changes under heightened economic uncertainty. While VC contracts generally become more protective when uncertainty rises, the increase in contractual protection is significantly weaker for common-law structures, suggesting that stronger legal institutions partially substitute for explicit contractual safeguards in risky environments. The substitution effect extends to the supply side of VC investment, where common-law governance reduces reliance on investor experience in managing uncertainty, but does not replace demand-side bargaining power of entrepreneurial firms. We further corroborate our results using large language model (LLM)-based measures that provide a holistic, context-aware assessment of investor protection.

---

## uid: `arxiv:2606.30085v1`

- title: Not-quite-human tastes: the stylized omnivorousness of LLM survey surrogates
- authors: Xiangyu Ma, Mengmi Zhang, Shannon Ang, Minne Chen
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.30085v1
- keyword hits: deepseek, llm, llms

### abstract

Large-language models have proven to be remarkable if inconsistent parrots of public attitudes and opinions. The extent to which LLMs are able to produce reasonable approximations of cultural taste remains an open empirical question that becomes more urgent by the day, with market research companies already offering provisional `synthetic' survey panels and the contamination of standard survey data from LLM-generated responses. In this study, we build on past work on silicon sampling by extending considerations of its algorithmic fidelity and alignment to the domain of cultural consumption. We use large-language models from OpenAI, Anthropic, and DeepSeek to each produce 277,470 (30x9249) silicon surrogates of survey respondents from the Survey of Public Participation in the Arts (SPPA). We find these silicon surrogates' tastes to be highly stylized facsimiles of human tastes. (1) Silicon samples have a systematic postive-bias for liking, resulting in inflated ecological estimates of tastes. The individual-level bias of silicon samples are not well-explained by the WEIRD-bias often discussed in the literature. (2) The complex relationality in real taste structures is completely lost among silicon samples. (3) Finally, very little of the known cultural alignment between tastes and social space are preserved. Silicon samples attenuate age-taste associations, resurrect anachronistic class-taste associations, caricaturize gender- and race-taste associations.

---

## uid: `arxiv:2606.30852v2`

- title: When Does Learning to Stop Help? A Cost-Aware Study of Early Exits in Reasoning Models
- authors: Zhe Dong, Fang Qin, Manish Shah
- affiliations: not stated
- posted: 2026-06-29
- source: arXiv
- link: https://arxiv.org/abs/2606.30852v2
- keyword hits: deepseek, qwen

### abstract

Reasoning models spend test-time compute unevenly across instances, and a growing family of early-exit rules -- confidence thresholds, entropy monitors, answer-stability checks, and learned stoppers -- promises to reclaim the waste. These rules, however, are evaluated under heterogeneous protocols that leave the deployment question unanswered: at a fixed tolerance for losing correct answers, which policy saves more compute, and does the saving survive probe overhead? We answer this question with a controlled study across 18 task-model settings spanning GSM8K, MATH-500, MMLU-Pro, AIME-90, and GPQA on Qwen3 and DeepSeek-R1-distilled models, using LearnStop, a hidden-state-free logistic stopper over prefix-observable features, as the learned policy instrument. Under matched lost-correct risk at $α$ = 0.15, with the scalar competitor selected on calibration data from confidence, entropy, confidence-leap, and run-stability exits, the answer forms three regimes. Learned stopping wins on all four primary Qwen3 free-form math settings (+3.2 to +21.2 pp additional total-token saving); calibrated scalar exits win on multiple-choice MMLU-Pro; and small hard benchmarks (AIME-90, GPQA) admit no certifiable aggressive policy at all. A trajectory decomposition predicts the regime: learning pays where answers oscillate and correctness evidence is spread across complementary signals, while a single confidence threshold suffices where most instances are already solved at the first checkpoint. Cost accounting sharpens the picture further -- the same policy that saves 32% of tokens under KV-cache forking costs 121% extra under black-box repeated prefilling. Together, these results replace the single-method race with a decision procedure for choosing a stopping rule from the trajectory structure and serving regime of the target workload.

---
