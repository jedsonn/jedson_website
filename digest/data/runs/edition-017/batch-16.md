# Classification batch 16 of 20, edition 17

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-017/batch-16.answer.json` as a JSON array.

---

## uid: `arxiv:2608.03201v1`

- title: When Refusal Looks Safe: The Refusal-Cue Shortcut in Safety Guard Models
- authors: Yu Feng, Chunting Zang, Chen Shen, Rui Miao, Ge Teng, Weidong Cai, Jieping Ye
- affiliations: not stated
- posted: 2026-08-04
- source: arXiv
- link: https://arxiv.org/abs/2608.03201v1
- keyword hits: fine-tuning, llama, qwen

### abstract

Safety guards are widely used to filter harmful content and are typically trained via supervised fine-tuning on labeled prompt-response pairs. We audit two widely used safety-guard training datasets, WildGuardMix and GR-Train, and find that among responses to harmful prompts, refusal expressions co-occur almost exclusively with unharmful labels. This imbalance motivates what we term the refusal-cue shortcut: inserting a refusal cue into a harmful response could flip the guard's verdict from harmful to unharmful. The shortcut affects not only guards trained on these datasets but also officially released models such as LlamaGuard3 and Qwen3Guard whose training data is undisclosed. It persists across response positions and is generally stronger in smaller variants within a family. To mitigate it, we adapt sparse complementary masking as a lightweight post-hoc intervention that identifies and suppresses a small set of shortcut-associated attention heads and MLP neurons without retraining. On two primary benchmarks, the intervention achieves an approximately 79% relative reduction in response-initial detection failures induced by refusal cues, while preserving standard detection performance. Although optimized using cues at a single response position, the suppression effect transfers to unseen positions and datasets, suggesting that shortcut manifestations across positions are partly mediated by shared internal components. Further analysis provides evidence that shortcut reliance and legitimate refusal recognition are partially functionally separable, as suppressing the shortcut broadly preserves the guard's ability to recognize genuine refusals.

---

## uid: `arxiv:2608.06301v1`

- title: HarnessOpt-Bench: Evaluating LLMs at Harness Optimization
- authors: Varun Ursekar, Apaar Shanker, Yash Maurya, Shehab Yasser, Vijay S. Kalmath, Veronica Chatrath, Yuan Xue
- affiliations: not stated
- posted: 2026-08-06
- source: arXiv
- link: https://arxiv.org/abs/2608.06301v1
- keyword hits: agentic, llm, llms

### abstract

As LLMs are increasingly deployed within agentic systems, their capabilities depend not only on the model weights but also on the harness: the prompts, tools, control flow, memory, and orchestration code surrounding them. This makes automated harness optimization -- the iterative and evaluation-guided improvement of a harness by an AI system -- both an important route to improving AI systems and a demanding capability for AI systems themselves. Yet the community lacks a common protocol for measuring how well frontier LLMs perform at this task. We introduce HarnessOpt-Bench, a benchmark for end-to-end harness optimization under expensive and stochastic evaluation. An optimizer, an LLM paired with a coding harness, receives a target agent's seed harness, graded evaluation feedback, and a fixed target-evaluation budget. It edits the harness and nominates a final candidate, which is scored by its normalized gain over the seed on a held-out test partition that remains inaccessible throughout search. A trusted execution environment enforces the evaluation boundary, meters target-agent resource use, and preserves candidate versions for audit. We evaluate 5 frontier LLMs as optimizers both under a shared coding harness and under their native harnesses across 4 downstream tasks, over 111 scored runs. Experiment results show that optimizer models separate more than the coding harnesses they act through, native harnesses are not consistently superior, and gains vary substantially across tasks and seed regimes. These results establish harness optimization as a measurable and discriminative capability with large space for improvement.

---

## uid: `arxiv:2608.05792v1`

- title: When Agentic AI Meets Integrated Sensing and Communication
- authors: Kai Li, Conggai Li, Sarah Ali Siddiqui, Syed Sohail Ahmed, Xin Yuan, Shenghong Li, Wei Ni
- affiliations: not stated
- posted: 2026-08-06
- source: arXiv
- link: https://arxiv.org/abs/2608.05792v1
- keyword hits: agentic, large language model, large language models

### abstract

Agentic artificial intelligence (AI) is transforming Integrated Sensing and Communication (ISAC) from a function-oriented physical-layer technology into a goal-driven, closed-loop intelligent system, a paradigm we term AISAC. Existing work on learning-based sensing, resource allocation, reconfigurable intelligent surfaces (RIS), edge intelligence, multi-agent coordination, and resilient networking has developed largely in isolation. This survey unifies the literature within a six-stage closed-loop framework comprising observation, contextualization, reasoning and prediction, planning and orchestration, execution and collaboration, and feedback and resilience. It also introduces five levels of agentic maturity, ranging from physical-layer primitives to fully closed-loop agentic ISAC. We use this framework to review advances in multimodal intelligence, large language models, reinforcement learning, federated learning, RIS-assisted control, Unmanned Aerial Vehicle (UAV) and vehicular networks, and AI-native network management, and analyze privacy, security, resilience, and sustainability as cross-cutting requirements of the full perception-reasoning-action loop. An audit of representative studies against nine agentic-specific evaluation criteria shows that no system reports more than one or two of them, exposing a gap between claimed and demonstrated agentic maturity. We identify open challenges in physical-to-semantic grounding, predictive world models, real-time agent-PHY interaction, safe tool use, heterogeneous multi-agent collaboration, benchmarking, and resource-efficient autonomy.

---

## uid: `doi:10.2139/ssrn.7206518`

- title: Outcome Without Method: An Outcome-Validation Integrity Score for Agentic Cybersecurity Benchmarks
- authors: Babar Khan Akhunzada
- affiliations: not stated
- posted: 2026-08-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7206518
- keyword hits: agentic, large language model, llm

### abstract

Agentic large language model (LLM) systems are increasingly evaluated on cybersecurity tasks: capture-the-flag (CTF) exploitation, vulnerability discovery, malware analysis, and automated patching, typically using benchmarks that report a single scalar success metric, such as a binary flag capture, a multiple-choice accuracy, or a pass@k rate. We show, through a structured audit of eleven independently published benchmarks and deployments spanning academic preprints, an industry blog, a government-run competition, an enterprise production deployment, and an industry framework evaluation, that the design of a success metric is a strong predictor of whether that metric can be gamed without the intended capability being exercised, a failure mode we term outcomewithout-method. We formalize a five-dimension, 0-10-point Outcome-Validation Integrity Score (OVIS) that scores each benchmark on method verification, shortcut and contamination auditing, human ground-truth anchoring, grader independence, and reproducibility. Applying OVIS across our corpus, benchmarks using purely outcome-based grading (binary flag or multiple-choice) score a mean methodverification sub-score of 16.7%, versus 100.0% for benchmarks using process-aware grading (tiered capability ladders, graph-grounded step rewards, or functional patch-validation). We further document a previously reported instance of reward hacking in which a benchmarked model achieved an 85% nominal pass rate on a challenge while using the intended exploitation technique in zero of 681 relevant runs, and show that a post-hoc manual audit, rather than benchmark redesign, was sufficient to detect it. We situate OVIS within the broader reward-hacking and specification-gaming literature, argue that OVIS-style auditing should be a required companion to any reported capability number in agentic cybersecurity evaluation, release our scoring rubric and corpus as a reusable artifact, and outline how the approach generalizes to non-security agentic benchmarks.

---

## uid: `doi:10.2139/ssrn.4361607`

- title: Auditing Large Language Models: A Three-Layered Approach
- authors: Jakob Mökander, Jonas Schuett, Hannah Rose Kirk, Luciano Floridi
- affiliations: not stated
- posted: 2023-02-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.4361607
- keyword hits: large language model, large language models

### abstract

NOT AVAILABLE. You have title and authors only. Set bullet_provenance to "none", return an empty bullets array, and classify field and role only if the title makes it unambiguous.

---

## uid: `doi:10.2139/ssrn.4476855`

- title: Battle of the Wordsmiths: Comparing ChatGPT, GPT-4, Claude, and Bard
- authors: Ali Borji, Mehrdad Mohammadian
- affiliations: not stated
- posted: 2023-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.4476855
- keyword hits: chatgpt, claude, gpt-4

### abstract

NOT AVAILABLE. You have title and authors only. Set bullet_provenance to "none", return an empty bullets array, and classify field and role only if the title makes it unambiguous.

---

## uid: `doi:10.2139/ssrn.4614223`

- title: GenAI Against Humanity: Nefarious Applications of Generative Artificial Intelligence and Large Language Models
- authors: Emilio Ferrara
- affiliations: not stated
- posted: 2023-11-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.4614223
- keyword hits: generative artificial intelligence, large language model, large language models

### abstract

NOT AVAILABLE. You have title and authors only. Set bullet_provenance to "none", return an empty bullets array, and classify field and role only if the title makes it unambiguous.

---

## uid: `doi:10.2139/ssrn.4797024`

- title: A Critical Assessment of Large Language Models for Systematic Reviews: Utilizing ChatGPT for Complex Data Extraction
- authors: Hesam Mahmoudi, Doris Chang, Hannah Lee, Navid Ghaffarzadegan, Mohammad  S. Jalali
- affiliations: not stated
- posted: 2024-04-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.4797024
- keyword hits: chatgpt, large language model, large language models

### abstract

NOT AVAILABLE. You have title and authors only. Set bullet_provenance to "none", return an empty bullets array, and classify field and role only if the title makes it unambiguous.

---
