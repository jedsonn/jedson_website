# Classification batch 27 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-27.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7300712`

- title: BuildThermBench: An EnergyPlus-Grounded Benchmark for Building-Thermal Reasoning and Closed-Loop Control
- authors: deli liu, Penghui Cao, Yu Li, Ying Jin, Dagang Xu, Jiaxin Yu, Xiaoping Zhou
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7300712
- keyword hits: large language model, large language models

### abstract

Large language models are increasingly used as engineering assistants and supervisory controllers, but current evaluations rarely connect static reasoning and closed-loop action to one executable physical oracle. We introduce BuildThermBench, an EnergyPlus-grounded benchmark that separates thermal-state understanding, physics-grounded counterfactual reasoning, and closed-loop safe control. The benchmark uses a DOE Medium Office prototype, five Chinese cities, six frozen building and operational variables, deterministic scenario identities, and EnergyPlus 25.1. Track 1 converts annual simulations into 168-hour state-understanding tasks. Track 2 creates single-variable interventions and matched presentation-only variants, with labels and effect filters derived from paired simulations. Track 3 evaluates hourly cooling-setpoint decisions through the EnergyPlus Python Runtime API under action bounds, ramp limits, fallback rules, and a pre-registered energy–comfort–compliance–reliability score. Public development data, hidden test inputs, and internal oracle artifacts are separated to limit leakage. Version 1 contains 480 Track 1 cases, 1,436 scored Track 2 prompts, and 150 formal Track 3 episodes. Four local open-weight models and three hosted systems completed all tracks, totaling 37,268 model interactions. Across these configurations, Track 1 accuracy ranged from 24.3% to 59.7%, Track 2 accuracy from 11.3% to 56.1%, and Track 3 scores from 0.630 to 0.736. Diagnostics reveal a cumulative-energy scoring floor, intervention-dependent counterfactual difficulty, distinct energy–comfort operating points, and substantial fallback dependence for one controller. BuildThermBench therefore provides a reproducible diagnostic framework for physical reasoning and safe building control.

---

## uid: `arxiv:2608.16370v1`

- title: What Does Context Compression Cost an Agent? Interaction Costs Unrevealed by Task-Completion Metrics
- authors: Shuyu Liu
- affiliations: not stated
- posted: 2026-08-17
- source: arXiv
- link: https://arxiv.org/abs/2608.16370v1
- keyword hits: deepseek, gpt-5

### abstract

Task completion is the standard metric for evaluating context compression, yet it is incomplete: compression can increase an agent's interaction cost by forcing it to reacquire dropped state while leaving completion statistically unchanged. We introduce a controlled runtime measurement protocol for reacquisition cost in a bounded-horizon tool-using agent. The agent acts in a deterministic planning environment under a fixed 24-turn horizon. We vary compression severity, compare a dropping operator with a fact-preserving operator, restore dropped state through controlled oracle interventions, and decompose tool calls into retrieval and execution. We evaluate three models across two task regimes. Retrieval calls increase in all six model-regime comparisons and account for almost all added interaction; five of six remain significant after Holm correction. At the prespecified 5x comparison point, completion changes are not significant in any cell. DeepSeek shows a significant completion drop only at 10x compression. GPT-5.5 is the clearest case: completion changes from 80% to 85% (p = 1.0) while retrieval increases from 21.0 to 63.9 calls (p = .002). Retention interventions further separate state quantity, state type, and content validity. Random selection is comparable to an offline hindsight oracle, while replacing retained D-state with semantically irrelevant content increases retrieval by 57% (p < .001) without a significant completion change. In a second environment, ALFWorld, sliding compression produces no retrieval surge, showing that the reacquisition signature is environment-dependent rather than intrinsic to shortening context. Overall, compression can impose hidden interaction costs when execution-relevant state becomes absent and must be reacquired, while completion alone may not expose those costs.

---

## uid: `arxiv:2608.16213v1`

- title: Process-Constituted Intelligence: A Shared Criterion for Humans and Machines
- authors: Michael J. Richardson, Ayeh Alhasan, Cassandra Crone, M. Paula Diaz Monfort, Patrick Nalepka, Mark Dras, Rachel W. Kallen, David M. Kaplan
- affiliations: not stated
- posted: 2026-08-17
- source: arXiv
- link: https://arxiv.org/abs/2608.16213v1
- keyword hits: generative ai

### abstract

Intelligence is constituted by \textit{process} (iterative activity through which output emerges), not in the output itself. Generative AI (GenAI) is trained on \textit{traces} (textual and visual residues of human cognitive processes), reproducing samples from a distribution of those traces. Its outputs resemble reasoning, problem-solving, and creativity, yet the activity that produces such outputs in humans remains largely absent. Current GenAI is, therefore, weakly equivalent to the cognition it imitates, matching outputs while process stays absent or opaque. The cognitive sciences have long distinguished between weak and strong equivalence. Here, we define \textit{strong} equivalence across seven process features, assessable against human and machine cognition. Our process-based account addresses a symmetric risk: GenAI tools that outsource a person's generative processes may leave critical capacities unbuilt. We specify design principles for GenAI that instantiate more process and preserve rather than erode human judgment and creativity, and outline process audits that make strong equivalence testable.

---

## uid: `arxiv:2608.16003v1`

- title: Prior Audit-Repair Context Shifts LLM Verifier Thresholds Toward Leniency
- authors: Parsa Mazaheri, Kasra Mazaheri
- affiliations: not stated
- posted: 2026-08-17
- source: arXiv
- link: https://arxiv.org/abs/2608.16003v1
- keyword hits: llm

### abstract

Automated checking pipelines increasingly place one language model as the checker and another (or the same one) as the fixer. We ask whether that wiring changes what the checker reports. Measuring false alarms on human-verified-correct ProcessBench traces with the present task held byte-identical, we find that a completed audit -> repair episode already in the model's context lowers false alarms in 15 of 15 model x wording combinations, by 2.8 to 11.5 percentage points against a length-matched non-audit control, a 9 to 25% reduction relative to that control. The direction contradicts what the accumulated-message literature predicts: an episode whose audit reported an error lowers false alarms further still, at all five wordings on the model where that manipulation lands cleanly, though a negativity asymmetry predicts more flagging. Decomposing the episode finds repair content and audit verdict complementary: different components carry the effect on different model families. Signal-detection analysis locates the change in the threshold rather than in discrimination -- the criterion moves in 15 of 15 combinations and survives correction in 13 while d' survives in none, though the d' test is half as sensitive by construction -- and a hand audit of 50 false alarms finds 82% simply wrong, so at this operating point the shift need not be harmful. With reasoning enabled the effect keeps its relative size on both models tested, and the threshold reading holds there too.

---

## uid: `doi:10.2139/ssrn.7285899`

- title: Code is not Law: The Congruence Dilemma and the Limits of Legality in AI-based Public Administration
- authors: Craig S Wright
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7285899
- keyword hits: generative ai

### abstract

The premise that encoding a rule in software is a way of administering it now underwrites much of the digital state. Critics mainly contest it by disputing whether algorithmic systems are accurate, fair or legitimate enough to bear it, a framing that concedes the decisive ground by treating law and code as competing technologies for one task. This article argues instead that regulation and legality are different properties, and that competence at the first entails nothing about capacity for the second. Reconstructing legality through Fuller's desiderata, we locate the distinctive failure at the eighth, congruence between declared rule and official action, and specify it as a congruence dilemma. Where an external declared norm survives, the system enacts rather than states its operative rule, so divergence must be reconstructed by investigation rather than observed by comparison; where computational implementation progressively becomes the de facto specification of a delegated standard, there is nothing left for administration to be incongruent with. Crucially, the resulting failure is not an inability to detect incongruence-Robodebt was detected repeatedly and continued anyway-but the severance of detection from correction, which automation achieves by making detected incongruence cheap to perpetuate at scale. We then show that generative AI introduces a distinct failure we call the specification illusion: a natural-language system prompt can institutionally impersonate a promulgated rule while possessing none of a promulgated rule's authoritative priority over implementation. We accept that determinism, formal runtime constraint and trajectory auditing are all technically achievable, and argue that this sharpens rather than weakens the thesis, because technical conformance is neither necessary nor sufficient for legal bindingness. We conclude by specifying contestability as a four-part institutional requirement-separation (as a binding legal envelope), record, adjudicative remedy and propagation-and assess the EU, Canadian, US and Australian instruments against it.

---

## uid: `doi:10.2139/ssrn.7306280`

- title: Fast Real-World Face De-Occlusion by Style-Based GAN Prior
- authors: Honglei Li, Yiran Gong, Huan He, Yuqian He, Lihe Hu, Zhisha Xu, Minjie Liao
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7306280
- keyword hits: foundation model

### abstract

Occlusions in face images severely degrade the quality and usability of sensoracquired face data, hindering downstream tasks like biometric recognition, emotion analysis, and public safety monitoring. Existing face de-occlusion methods heavily rely on accurate occlusion detection or paired training data, leading to limitations in real scenarios. Recent multi-modal vision foundation models perform well in text-guided face editions, but suffer from slowprocessing speed and less controllability. To address these issues, we propose a novel Style-based de-occlusion model, which leverages a pre-trained StyleGAN generator and successively optimizes intermediate features under perceptual and mask detection constraints. It fully exploits the generative prior of the style-based generator for unoccluded face generation, enabling real-time face de-occlusion without pre-identifying occlusions and thus enhancing robustness in real-world scenarios. Extensive experiments confirm this model outperforms state-of-the-art methods, excelling in identity preservation, structural consistency, and practical occlusion robustness.

---

## uid: `doi:10.2139/ssrn.7303098`

- title: Contesting the Rules of the Game: Organized Groups in Election Policymaking
- authors: Joseph Loffredo
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7303098
- keyword hits: large language model, large language models

### abstract

Organized groups often pursue policy influence by lobbying policymakers and working to elect allies. Research on groups' efforts to shape who governs, especially campaign contributions, generally treats electoral rules as fixed. I argue that groups work strategically to change those rules and explain why and when they take action. Because doing so is costly and its returns uncertain, groups take positions on election policy when sufficiently motivated and proposed changes could affect who governs. I test this argument by linking 12,000 election bills across 22 states to 37,000 group positions from state lobbying and testimony records. Nearly seven in ten positions come from groups whose work lies outside election policy. These groups participate more where elections are closely contested and they have a legislative presence. Groups that repeatedly fail to advance policy goals act more only where electoral competition is high, while groups with fewer opportunities to advance priorities act more where legislative leaders tightly control the agenda. Using a human-in-the-loop procedure combining large language models with supervised machine learning, I assess how legislation changes election policy, then pair these ratings with group ideal points from state legislative activity. I find that liberal groups favor proposals that expand voter access or improve election administration, while conservative groups favor the reverse. Further, group activity signals which proposals divide policymakers and which are viable to become law. These findings broaden accounts of how groups pursue policy influence and illuminate their role in the politicization of American election policy.

---

## uid: `doi:10.2139/ssrn.7305538`

- title: CNN-LSTM-Based Groundwater Depth Forecasting Using Hydroclimatic Variables and Monitoring Data in Lahore, Pakistan
- authors: Kandeel sadaqat, Abdullah Nadeem, Muhammad Kashif Nazir, Muhammad  Atiq Ur Rehman Tariq
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7305538
- keyword hits: llama

### abstract

Groundwater depletion has become a major environmental and water security challenge in rapidly urbanizing regions, particularly in developing countries where groundwater is the primary source of domestic, industrial, and municipal water supply. Lahore, Pakistan, has experienced persistent groundwater decline driven by increasing abstraction, urban expansion, and hydroclimatic variability. This study developed a hybrid Convolutional Neural Network–Long Short-Term Memory (CNN–LSTM) model to forecast groundwater depth by integrating long-term groundwater observations with satellite-derived hydroclimatic variables.Groundwater data from 27 monitoring stations (2003–2023) were combined with precipitation (CHIRPS), temperature (MODIS/ERA5), and soil moisture (SMAP) datasets. Because groundwater measurements were available primarily during pre- and post-monsoon periods, a hybrid kriging–ARIMA framework was employed to reconstruct continuous monthly groundwater time series. Following temporal synchronization and normalization, the CNN–LSTM model was trained using a chronological data-splitting strategy and evaluated using Root Mean Square Error (RMSE), Mean Absolute Error (MAE), and the coefficient of determination (R2).The model achieved satisfactory predictive performance, with a validation RMSE of 2.31 m, MAE of 1.74 m, and R2 of 0.84, while demonstrating stable convergence and good generalization. Prediction accuracy varied spatially, with lower errors generally observed in rural and peripheral areas than in densely urbanized locations. Forecasts for 2024–2033 indicate continued groundwater depletion across Lahore, identifying Township, Garden Town, Green Town, Gulberg, and Allama Iqbal Town as future groundwater stress hotspots. These findings demonstrate the potential of hybrid deep learning for groundwater forecasting and provide a practical framework to support groundwater monitoring, sustainable resource management, and long-term water planning in data-constrained urban environments.

---
