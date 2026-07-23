# Classification batch 102 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-102.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6869664`

- title: Comparative Analysis of Initial and Long-term Financial Commitments of Cloud-based and Onpremises Infrastructure Solutions for Large Language Models
- authors: Daniel Winnips
- affiliations: not stated
- posted: 2026-06-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6869664
- keyword hits: large language model, large language models, llm, llms

### abstract

The rapid advancements in artificial intelligence and deep learning, particularly in Large Language Models (LLMs), have significantly increased computational demands for organizations. This paper provides a comparative analysis of the initial and long-term financial commitments associated with cloud-based and on-premises infrastructure solutions for deploying LLMs across organizations of varying sizes. It examines the costefficiency, environmental impact, and required skill sets for managing these infrastructures. The study employs a mixed-methods approach, including a comprehensive literature review and a workshop involving students from a master's program in Business Information Systems. Key findings indicate that cloud-based solutions offer lower upfront costs and scalability, making them suitable for startups and small to medium-sized enterprises, while on-premises solutions provide greater control and potentially lower long-term costs, beneficial for larger organizations with specific compliance and data security needs. Additionally, the study highlights cost-reduction strategies such as transfer learning, sparse training, and optimal hyperparameter tuning. The results aim to guide organizations in aligning their infrastructure strategies with technical needs, financial constraints, and environmental responsibilities, thereby future proofing their investments in LLM deployment.

---

## uid: `doi:10.2139/ssrn.6869438`

- title: RIS-Kernel: A Model-agnostic Architecture for Long-context LLM Inference via Sparse Attention
- authors: Anderson Santos
- affiliations: not stated
- posted: 2026-06-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6869438
- keyword hits: large language model, large language models, llm, qwen

### abstract

Full self-attention in large language models scales as O(N 2), limiting long-context document analysis to 65,536 tokens and requiring costly GPU clusters. The Reduced Interaction Sampling (RIS) inference engine addresses this constraint as a model-agnostic architecture. Without modifying weights, RIS reduces self-attention complexity to O(N log N) using sparse stochastic geometry that fits within commodity memory limits. We validate RIS on Qwen2-1.5B-Instruct across two regimes. In controlled evaluations at 32,768 tokens (where native dense attention serves as the upper bound), RIS-Stochastic at 1% density and 70 ensemble seeds achieves 75.00% accuracy, outperforming the native dense baseline (71.88%), while RIS-Stochastic at 5% density and 10 seeds matches it (71.88%). This demonstrates that sparse attention acts as a regularizer: low density (1%) over multiple seeds filters out sequence-level noise, whereas higher density (5%) reintroduces distractor noise. Under the tightest budget, RIS-Structural reaches 68.75% accuracy at 1% density with just 10 seeds, recovering 75% of the contextual gap relative to the zero-context floor (59.38%). At 65,536 tokens, where dense attention triggers out-of-memory faults, RIS yields retrieval gains of up to 14.06 percentage points over the zero-context floor (51.56%). All evaluations run on commodity, unaccelerated CPU servers (16-128 GB of RAM), demonstrating that long-context LLM inference is feasible on standard academic hardware without GPU acceleration.

---

## uid: `arxiv:2606.22797v1`

- title: Measuring Behavior Portability in Large Language Models
- authors: Tianjia Dong, Nadav Kunievsky, James A. Evans
- affiliations: not stated
- posted: 2026-06-22
- source: arXiv
- link: https://arxiv.org/abs/2606.22797v1
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models are increasingly deployed as autonomous decision makers, yet the behavioral mapping they exhibit can vary substantially across decision environments that are payoff-equivalent by construction-environments that share identical payoff-relevant structure but differ in surface presentation. This sensitivity renders suite-based evaluation fragile and raises a fundamental question of behavioral portability: how well does a behavioral mapping learned in one decision environment informative on another that preserves the same underlying incentive structure? We introduce a formal framework to measure this property. Our protocol fits an interpretable behavioral model on data pooled from a set of source environments and evaluates its out-of-sample predictive performance in a held-out target environment, benchmarking against an oracle trained directly on target data. Portability is quantified via a loss-agnostic measure that delivers worst-case bounds on the performance of the induced prediction-action mapping in the target environment. In controlled experiments spanning seven canonical economic decision problems, we document substantial and systematic portability losses, suggesting that behavioral characterizations of LLMs obtained in one decision environment cannot be assumed to transfer reliably to structurally equivalent alternatives.

---

## uid: `doi:10.2139/ssrn.6985744`

- title: Leveraging Chatbots to Support Help-Seeking
- authors: James Gaskin, Eva Blondeel, Ryan Schuetzler, Rachel Serre, Jacob Steffen, David A. Wood, Taylor Bullock, Taylor Wells
- affiliations: not stated
- posted: 2026-06-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6985744
- keyword hits: chatgpt, large language model, llm

### abstract

As large language model (LLM) chatbots gain traction across education and the workplace, they are emerging as a new class of decision support tool that reshapes how individuals seek information and make learning and work decisions. This study investigates how LLM-based chatbots reduce help-seeking avoidance, particularly among introverted and underrepresented individuals who often hesitate to seek assistance due to fears of judgment or stereotype threat. Across two classroom field studies and a qualitative survey of professionals, we show that chatbots significantly encourage help-seeking behavior by offering anonymous, on-demand, and non-judgmental support. In an introductory Information Systems course, 597 students interacted with a custom chatbot, viewing it as an accessible teaching assistant. In an accounting program, 916 students reported a strong preference for ChatGPT over traditional human support. An open-ended survey of 32 working professionals confirmed and extended these findings. Evidence suggests LLM chatbots ”level the playing field” across social anxiety and introversion. We conceptualize LLM-based chatbots as socially neutral decision support agents that decouple informational access from social evaluation, reducing the social costs of help-seeking. In doing so, they extend decision support research by demonstrating that AI systems do not merely improve information access but transform the social dynamics underlying knowledge-seeking and decision-making. These findings hold implications for the design and deployment of organizational decision support agents and for institutional strategies that leverage AI to broaden equitable access to support.

---

## uid: `doi:10.2139/ssrn.6962406`

- title: Engineering Measurable Trust: A Multilayer Architecture for Safe Deployment of Large Language Models in Clinical Decision Support
- authors: Barnty Johnson
- affiliations: not stated
- posted: 2026-06-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6962406
- keyword hits: chain-of-thought, large language model, large language models, prompting

### abstract

The rapid integration of large language models into clinical workflows promises substantial gains in diagnostic support, documentation efficiency, and patient communication. Yet the gap between impressive benchmark performance and safe real world deployment remains dangerously unbridged. This paper argues that the central problem is not model accuracy per se but rather the absence of an engineering framework for measurable trust-a system property that cannot be reduced to any single metric. Drawing on a synthesis of recent empirical audits, consensus frameworks, and multi-agent architectures, we advance a novel conceptual model built on three principles: evidence traceability, human-in-the-loop supervision, and staged autonomy. We demonstrate that existing approaches, including chain-of-thought prompting and self-consistency methods, fail to address critical failure modes identified in recent studies: reasoning instability that precedes hallucination, the accountability paradox where high-quality outputs still require full physician verification, and the absence of calibrated uncertainty metrics suitable for high-stakes decisions. Our proposed multilayer architecture integrates a deterministic clinical core, a contextually bounded AI assistant, a tiered model escalation mechanism, and a human supervision layer with quantitative trust metrics derived from metrological principles. The framework provides both a design blueprint for developers and an evaluation protocol for regulators. We conclude that trustworthy clinical AI is not an intrinsic property of any model but an architectural outcome that must be engineered from first principles.

---

## uid: `doi:10.2139/ssrn.6985531`

- title: SCALE: Scalable Cross-Attention Learning with Extrapolation for Agentic Workflow Scheduling
- authors: Zhifei Xu, Jierui Lan, Zixuan Liang, Aiji Liang, Jinxi He
- affiliations: not stated
- posted: 2026-06-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6985531
- keyword hits: agentic, fine-tuning, large language model, llm

### abstract

Agentic Large Language Model (LLM) systems decompose complex tasks into workflow Directed Acyclic Graphs (DAGs) whose primitives must be scheduled on heterogeneous clusters. Existing deep reinforcement learning (DRL) schedulers are tied to a fixed cluster size and require retraining whenever the number of servers changes. We propose SCALE (Scalable Cross-Attention Learning with Extrapolation), a DRL scheduler that generalizes to unseen cluster scales without fine-tuning. SCALE employs a cross-attention pointer network where task features query against server features, so the architecture accepts any number of servers by construction. We observe, however, that permutation-invariant architecture alone does not guarantee good performance at new scales-the attention feature undergoes distribution shift as the server count grows. To counter this, we introduce Structured Representation Regularization (SRR): a decorrelation loss combined with a KL penalty toward the standard normal, which keeps feature statistics stable regardless of input size. Trained on 16 nodes and tested directly on 32 and 48 nodes, SCALE reduces average response time by 8.9% at N=48 relative to the same architecture without SRR, confirming that explicit regularization is necessary to close the scale-generalization gap.

---

## uid: `doi:10.2139/ssrn.6900538`

- title: Predicting the Pitch or Repeating the Public? Large Language Models and Sports Consensus Bias in the FIFA World Cup 2026
- authors: Nouar Aldahoul, Hezerul Abdul Karim, Myles Joshua Tan
- affiliations: not stated
- posted: 2026-06-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6900538
- keyword hits: large language model, large language models, llm, llms

### abstract

As the FIFA World Cup 2026 approaches, global excitement is peaking and everyone is focused on predicting who will lift the trophy. However, football remains difficult to forecast because human emotion, unexpected injuries, and pure pitch drama constantly defy even the most advanced statistics. This work looks at whether different Large Language Models (LLMs) give different predictions or if they all just copy each other when simulating sports tournaments. Our study was done in three phases. In the first phase, we used 30 different LLMs to predict the winners of 72 individual matches in the group stage (ignoring draws scenarios). Surprisingly, there was low variety Because all 30 models selected the same winning team in at least 94% of the matches. In the second phase, we picked eight major LLMs from different companies and gave them a harder task. Instead of just picking a match winner, we asked them to simulate an entire four-team group stage consisting of six matches' total. We instructed them to look at team quality, world rankings, and tactics, and we forced them to include realistic draws. Even with this extra complexity in the prompt, all eight models still generated the same final group standings shown in the first phase. In the third phase, with the same eight LLMs, we instructed the prompt not to use reference, or factor in FIFA rankings, Elo ratings, or any numerical team coefficients. The prompt relies entirely on LLM's intrinsic knowledge. Even with this prompt, LLMs generated at least 70% of the same rankings and 90% of the same first and last place rankings shown in previous two phases. These results indicate that today's LLMs suffer from consensus bias when looking at public sports data. The models just repeat the most popular public opinions and standard world rankings found in their training data. Since the FIFA 2026 matches have not yet been played, it is not yet possible to evaluate how accurately the LLM predictions match the actual outcomes. This evaluation will be conducted once the tournament results become available.

---

## uid: `doi:10.2139/ssrn.6986543`

- title: The Grain of Prediction: Character-Level Language Models Better Approximate Human Predictability in Chinese Reading
- authors: Jochen Laubrock, Ming Yan
- affiliations: not stated
- posted: 2026-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6986543
- keyword hits: large language model, llm, llms, qwen

### abstract

Predictability, typically measured via cloze norms, is a robust predictor of fixation durations during reading, but cloze norms are expensive to collect and available for very few corpora. Large language model (LLM) surprisal has emerged as a scalable surrogate in alphabetic scripts. It has not been tested whether this generalizes to Chinese, a logographic writing system in which each character is typically a meaningful morpheme. We computed word-level surprisal from three LLMs that differ in tokenization granularity: a character-level model (Chinese GPT-2, 102M parameters) and two BPE-tokenized models (Qwen3-8B and GLM-4-9B). Analyzing eye movements from 60 readers of the Beijing Sentence Corpus (150 sentences, 1685 words), we report four findings. First, LLM surprisal predicts fixation durations and skipping rates in Chinese, replicating the pattern from alphabetic scripts. Second, the character-level model better approximates human cloze predictability (r = .78) and yields larger improvements in eye-movement model fit than BPE models that are about 80 times larger. Third, decomposing character-level word surprisal into onset (first character) and completion (remaining characters) components reveals dissociable contributions: onset surprisal dominates first-fixation duration (FFD), while both onset and completion contribute to gaze duration (GD). Fourth, surprisal of the preceding word influences fixation duration on the current word, replicating the distributed processing pattern from alphabetic scripts. Together, these results suggest that predictive processing during Chinese reading operates at the morphemic (character) level and propagates upward to the lexical level, a dissociation made visible by the transparency of the Chinese writing system.

---
