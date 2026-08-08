# Classification batch 20 of 20, edition 17

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-017/batch-20.answer.json` as a JSON array.

---

## uid: `arxiv:2608.01181v1`

- title: Talking to Digital Twins: Selective Disclosure and Belief Measurement in Financial Social Media
- authors: Boone Bowles, Raymond Duch, Sorin Sorescu
- affiliations: not stated
- posted: 2026-08-02
- source: arXiv
- link: https://arxiv.org/abs/2608.01181v1
- keyword hits: llm, llms

### abstract

Social media affect financial markets, but public posts by financial media personas are voluntary disclosures. What is not disclosed is therefore usually unobserved. We address this measurement problem by conducting repeated, real-time interviews of "digital twins" built from monitored finfluencers' X accounts under a fixed protocol. The interviews recover stock-level public-persona belief proxies even when no public recommendation is made. Because the interviews are generated and archived before the relevant return windows, the design avoids the look-ahead bias that arises when LLMs are queried ex post. The evidence shows that information obtained from these digital-twin interviews predicts the cross section of large-cap stock returns in the expected direction. Repeated real-time interviews therefore show how selective disclosure can be turned into measurable panels of market views.

---

## uid: `arxiv:2608.01418v1`

- title: Reusing Rollouts under Policy Lag: Prefix-Normalized Policy Optimization for LLM Reinforcement Learning
- authors: Wenhao Zhang, Yibo Xie, Rui Wang, Jiahua Yang, Lei Jiang, Zibo Yang, Yawei Wang, Jiali Xu
- affiliations: not stated
- posted: 2026-08-02
- source: arXiv
- link: https://arxiv.org/abs/2608.01418v1
- keyword hits: large language model, large language models, llm

### abstract

Autoregressive rollout generation is a major computational cost in reinforcement learning for large language models. Reusing each rollout batch for additional learner updates amortizes this cost, but later updates become increasingly off-policy as the learner departs from the behavior policy. At a token position, exact off-policy correction must account for both the current action and the probability of reaching its prefix. The cumulative importance ratio provides this correction, but its product form can produce an unwieldy dynamic range. We study Prefix-Normalized Policy Optimization (PNPO), which replaces the cumulative ratio with the geometric mean of likelihood ratios along each causal prefix, preserving causal-prefix dependence at each position while compressing the log-weight scale. In controlled long-context mathematical reasoning experiments, we induce two off-policy regimes by using one or four policy-update epochs per rollout batch. PNPO does not consistently outperform GSPO with one epoch. With four epochs, it attains the highest observed Avg@32 on each benchmark; the unweighted mean of the three independently selected benchmark peaks is 50.24, 3.00 percentage points above GSPO. Under a matched 2,400-update budget, four-epoch PNPO reaches a final macro Avg@32 of 49.66 after 150 rollout batches, comparable to the 49.56 reached after 600 batches with one epoch. These results provide preliminary evidence that PNPO can be advantageous as training moves further off-policy.

---

## uid: `arxiv:2608.01388v1`

- title: Why Formal Monitors Fail: Attack Distribution Entropy as a Coverage Bound for LTL-Based LLM Agent Safety
- authors: Ruiyang Zhang
- affiliations: not stated
- posted: 2026-08-02
- source: arXiv
- link: https://arxiv.org/abs/2608.01388v1
- keyword hits: deepseek, gemini, llm

### abstract

Runtime safety monitors based on Linear Temporal Logic (LTL) and finite automata (FSA) are increasingly deployed to intercept unsafe tool-call sequences in LLM agents. Yet the same monitor achieves 68-75% attack coverage on some model architectures and near-zero on others, with no explanation from capability scores, training data, or prompt design. We provide the missing theory. We prove that the recall of any fixed-invariant FSA monitor is bounded above by the concentration of the attack distribution: the fraction of attacks covered by the k most frequent trigger-completion patterns. When attacks concentrate (low Shannon entropy), a small fixed invariant set achieves high recall; when they disperse across many structurally distinct patterns (high entropy), no fixed invariant set of tractable size can, regardless of how the invariants were derived. We validate this entropy-coverage bound across eight frontier LLM architectures. GPT-class and DeepSeek backends yield highly concentrated attacks (H ~ 0.24 bits; one pattern covers 96%), explaining 68-75% recall; Gemini variants yield high-entropy distributions (H ~ 2.81 bits; 7 clusters each <= 7%), explaining near-zero recall (6-13%), invariant to architecture-matched retraining. Entropy accounts for 76% of variance in coverage (Pearson r = -0.87, p = 0.005, 95% CI [-0.98, -0.78]), holding under leave-one-out (r in [-0.91, -0.82]). We introduce a pre-deployment entropy test that predicts monitor coverage from a small attack sample, enabling architecture-aware monitor selection before deployment. The bound and test are architecture-agnostic and apply to any FSA-based runtime monitor over discrete action sequences.

---
