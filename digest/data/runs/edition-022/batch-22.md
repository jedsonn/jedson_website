# Classification batch 22 of 60, edition 22

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-022/batch-22.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7292747`

- title: FedPOD-LoRA: Federated Fine-Tuning Based on Proximal Optimization and Dual-LoRA Collaboration
- authors: Yanan Li, Mengyang Guo, Yimeng Wang, Aming Wu, Yun Xin, Yongliang Yuan, Jianji Ren
- affiliations: not stated
- posted: 2026-08-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7292747
- keyword hits: fine-tuning, large language model, large language models

### abstract

Fine-tuning methods that combine federated learning with low-rank adaptation (LoRA) enable efficient collaborative training of large language models under resource constraints. Existing approaches widely adopt single-LoRA or multi-LoRA architectures. However, non-IID client data contain both global and personalized knowledge. Single-LoRA architectures tend to entangle them, while, multi-LoRA architectures lack persistent constraints between the global and private branches, causing the progressive discrepancy between local knowledge and aggregation knowledge. To address these limitations, this paper proposes FedPOD-LoRA, a federated fine-tuning method based on proximal optimization and dual-LoRA collaboration. First, we introduce a targeted proximal constraint on the global LoRA matrix B at the client side to reduce representation divergence between LoRA branches, thereby mitigating knowledge drift and fusion conflicts under non-IID data. Second, we further optimize the aggregated global Bmatrix using public data at the server side to enhance its global knowledge representation capability. Compared with five state-of-the-art (SOTA) methods, FedPOD-LoRA achieves better understanding performance, faster convergence. Across five natural language understanding tasks, including MNLI, SST-2, QNLI, QQP, and RTE, it improves accuracy by up to 2.5% and reduces the communication rounds required to reach the target performance on RTE and QNLI by 25.6% and 63.9%.

---

## uid: `doi:10.2139/ssrn.7292902`

- title: Trust-weighted distributionally robust maintenance scheduling under adversarial uncertainty in AI-generated diagnostic signals
- authors: Chunting Liu, Jian Zhang
- affiliations: not stated
- posted: 2026-08-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7292902
- keyword hits: deepseek, retrieval-augmented

### abstract

AI-augmented industrial decision-support systems, such as retrieval-augmented diagnosis engines and small-language-model monitors, now report an internal reliability signal alongside every inference. No maintenance optimization model uses that signal as an uncertainty parameter, and none hedges against its adversarial corruption. We treat an AI-generated diagnostic signal’s trustworthiness as a first-class, potentially adversarial variable. We introduce a trust-weighted contamination ambiguity set, a Wasserstein ball whose radius scales with the reported reliability, mixed with a budgeted adversarial component, which generalizes both Huber contamination and Wasserstein ambiguity sets. Embedding it in a two-stage distributionally robust maintenance model with priced verification recourse, we obtain a closed-form worst-case cost, a polynomial-size mixed-integer linear program, and a verification policy that thresholds the reliability score. We validate on the NASA C-MAPSS turbofan dataset with a real prognostic model whose confidence predicts its error (Spearman -0.70), under real false-data-injection, poisoning, and noise attacks. Naive trust is cheapest but leaves 7 to 14 critical engines unserviced per run, while the proposed policy attains near-complete failure prevention at a third to a half of blanket-verification cost. Crucially, among policies deployable under an unknown attack regime, no fixed verification heuristic matches its missed-failure rate for less than 44 percent additional cost; only an oracle that knows the attack can equal it. The premise generalizes to a second dataset (XJTU-SY bearings, Spearman -0.89). A language-model case study (retrieval-augmented deepseek-chat) confirms that prompt injection and corpus poisoning corrupt the signal while its faithfulness stays blind, so the contamination hedge supplies the protection.

---

## uid: `arxiv:2608.18167v1`

- title: Adversarial Review: Structured Disagreement for Grounded Agentic Code Review
- authors: Eric S. Qiu, Joyce Gill
- affiliations: not stated
- posted: 2026-08-16
- source: arXiv
- link: https://arxiv.org/abs/2608.18167v1
- keyword hits: agentic, llm

### abstract

Early multi-agent LLM systems often used role-separated teams, yet scaling agent count yields diminishing returns on repository-level coding tasks. Recent alternatives treat agents as passive tools (subagents), yet this removes the benefits of agent interaction entirely. We study whether a subagent paradigm can support a middle ground: minimal agentic cooperation without the overhead of large multi-agent teams. We introduce Adversarial Review (AR), a minimal cooperative code-review protocol in which a main coding agent works with a reviewer and a critic agent. The reviewer evaluates code, while the critic audits the review through structured disagreement before the main agent edits. On LiveCodeBench, AR achieves the highest pass rate among tested methods, outperforming a five-agent baseline while using only three agents. On SWE-PRBench, naive AR exposes a false-consensus failure mode, where agents converge on agreement without sufficient evidence, but a single prompt iteration that adds disagreement explicitly achieves the highest F1 among tested methods. On SWE-bench Verified, AR also shows improvements over the baselines on repository-level coding tasks. Together, AR demonstrates that cooperative code review does not require many agents or complex communication structures: it requires that disagreement be minimal, structured, and evidence-grounded.

---

## uid: `arxiv:2608.15877v1`

- title: Dear Algo: A Precision-First Agentic Intent Layer for Unified Search and Recommendation
- authors: Rui Wang, Jiazhou Wang, Zheng Wei, Chenglin Lu, Fangcheng Sun, Ivy Sun, Jin Sun, Hui Geng
- affiliations: not stated
- posted: 2026-08-16
- source: arXiv
- link: https://arxiv.org/abs/2608.15877v1
- keyword hits: agentic, llm

### abstract

Search and recommendation serve a shared discovery objective but encode intent differently. We study this boundary through Dear Algo on Threads, a deployed product where open-ended requests such as \emph{more NBA news} or \emph{less politics} steer subsequent feed recommendations rather than return a one-shot result list. Its agentic intent layer compiles explicit, inferred, negative, and compound intent into a grounded executable plan, then invokes conventional retrieval and optional semantic or multimodal reranking. The layer shares an intent-to-retrieval contract without requiring one model or serving path across search-like and recommendation-like modes. We evaluate Dear Algo under a precision-first objective. In a blinded audit of 300 public request-item pairs (296 evaluable), a strict categorical LLM-as-a-judge gate achieved 94.4\% exact-Relevant precision [88.8\%, 98.9\%]. Across 72 normalized request clusters, the full configuration produced 7.73 judge-qualified candidates per 20 slots versus 6.61 for an LLM-derived-query baseline, a gain of 1.11 [0.12, 2.12]. In a candidate-randomized serving-path study restricted to the reranker path's first 72 eligible hours, the user-weighted judge-Irrelevant share among judged admissions was 2.80\% versus 4.78\% off (-1.97 points [-3.02, -0.94]), while Exact-Relevant share was 2.24 points higher [0.08, 4.41]. Together, these studies show how explicit natural-language intent can be carried into feed recommendation under a precision-first evaluation framework

---

## uid: `doi:10.2139/ssrn.7301504`

- title: An LLM-Assisted Multimodal Materials-Informatics Pipeline for Predicting Remanence and Intrinsic Coercivity in Sintered Nd–Fe–B Magnets
- authors: Chunghee Nam
- affiliations: not stated
- posted: 2026-08-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7301504
- keyword hits: llm, llms, text embedding

### abstract

Reducing the use of heavy rare earth elements, particularly Dy and Tb, in sintered Nd–Fe–B magnets while maintaining high coercivity requires reliable prediction of magnetic properties from composition, processing, and microstructure. Although such information is abundant in the literature, much of it remains embedded in unstructured text. Here, we present an LLM assisted multimodal materials informatics pipeline that extracts a structured dataset of sintered Nd–Fe–B base magnets from the literature and predicts remanence (Br) and intrinsic coercivity (Hcj). The framework integrates composition and processing descriptors with fixed MatSciBERT representations derived from experimental and microstructure related text. The pretrained encoder is used only as a feature extractor and is not further pretrained or fine-tuned on the Nd–Fe–B corpus. From 839 Elsevier full text articles published between 1990 and 2026, the pipeline extracted 706 sample records, 658 of which contained usable property data. An independent extraction of the same corpus using a different LLM showed close agreement with the primary workflow in the per article median magnetic properties, with Pearson (r = 0.91–0.98), supporting the reproducibility of the structured dataset across LLMs. Under repeated random five-fold cross validation, tree ensemble models achieved R2 values of approximately 0.71 for Hcj and 0.56 for Br. The multimodal representation combining numerical descriptors with MatSciBERT derived text embeddings achieved the highest overall predictive performance, although its improvement over the numerical representation was modest and remained within the variability observed across repeated cross validation. The feature importance analysis was physically consistent: Hcj was governed primarily by Dy and Tb content and their fraction within the rare earth component, with an additional contribution from powder particle size, whereas Br was dominated by Fe content and the Ce fraction. Finally, a target driven literature retrieval tool provides direct access to citable, experimentally reported magnets that satisfy user defined property constraints. The proposed framework provides a physically grounded, reproducible, and openly accessible basis for the data driven development of magnets with reduced dependence on heavy rare earth elements.

---

## uid: `arxiv:2608.16795v1`

- title: Historical Backtesting for Scientific Question Discovery: A Protocol and Astronomy Pilot
- authors: Hui Mao
- affiliations: not stated
- posted: 2026-08-17
- source: arXiv
- link: https://arxiv.org/abs/2608.16795v1
- keyword hits: llm, prompting

### abstract

Systems that generate scientific research questions are evaluated today by expert scores, LLM-as-judge ratings, or curated case studies -- all subjective, none falsifiable. We formalize historical backtesting as an alternative: a system generates questions from a corpus frozen at a historical cutoff, the questions are frozen before any access to later literature, and a temporally isolated future corpus then determines whether each question was subsequently answered, partially addressed, independently posed, or ignored, and whether its underlying premise was supported or refuted. The protocol is model-agnostic: any system that emits frozen questions can be scored. We release reproducible astronomy instances with temporally isolated corpora, frozen questions, auditable labels, four reference baselines, and a submission interface. Two findings result. First, evidence-structure-first generation outperforms LLM-only prompting: across a generator decomposition crossed with a four-cutoff stress test (2010-2024, 798 judged questions) whose last window postdates model training, LLM-only generation shows memorized relevance without specific foresight, while a generator using no model weights at all finds questions whose premises the future refutes in every era. Second, a seven-rater agreement study (two blinded human annotators, five judge models, 90 items) indicts the outcome taxonomy rather than the judge: two careful humans agree at kappa = 0.17, every judge model agrees with the professional annotator as well or better (0.17-0.26), and frontier models agree with one another at 0.60 -- certifying an LLM judge by model-model agreement would have overstated its reliability threefold. A prospective instance -- 200 questions frozen 2026-08-17, scored 2027-2030 -- is released so the central claims become contamination-free tests that time itself will grade.

---

## uid: `arxiv:2608.16402v1`

- title: A Policy Algebra for Trust-Preserving Agentic AI Execution
- authors: Bhaskar Tripathi, Anurag Kumar, Ramendra Kumar, Bhavesh Gadhe
- affiliations: not stated
- posted: 2026-08-17
- source: arXiv
- link: https://arxiv.org/abs/2608.16402v1
- keyword hits: agentic, large language model

### abstract

Large language model-based agentic frameworks primarily optimize capability: whether an agent can reason, retrieve information, call tools, delegate work, and complete a goal. Enterprise execution requires a stronger property. A successful result is not reliable if it was produced through unauthorized data access, widened delegated authority, unapproved side effects, unrecoverable budget consumption, or incomplete evidence. This paper defines reliable capability as a path property: an agent is reliably capable only when it completes a task through action events that remain admissible under identity, profile, tool, data, memory, budget, artifact, approval, and audit constraints. We propose a policy algebra that defines the reliability envelope within which agent capability may be exercised. Security profiles and runtime obligations compose through joins, intersections, budget narrowing, approval inheritance, and evidence accumulation; the resulting composition is both trust-preserving and the least restrictive state satisfying all governing inputs. The algebra also propagates restrictions across multi-agent calls and introduces cost-aware artifact materialization, which redirects open-ended execution toward a recoverable outcome as budget exposure grows. The evaluation is interpreted as a reliability-capability trade-off rather than a capability benchmark: the policy-algebra runtime intervenes on 94.8% of policy-violating events while retaining an 86.9% task-completion rate, eliminates the observed profile-monotonicity and zero-artifact-exhaustion violations, and increases audit completeness to 98.6%. The method provides researchers and practitioners with formal correctness conditions, executable decision semantics, and trace evidence for building agents that are not only capable, but reliably capable.

---

## uid: `doi:10.2139/ssrn.7303184`

- title: Instance-level spatiotemporal identity mapping of tomato fruits and trusses via intra-period tracking and inter-period re-identification
- authors: Pengyao Xie, Weilong He, Xingjian Li, Nicholas Kaczmar, Neil Mattson, Lirong Xiang
- affiliations: not stated
- posted: 2026-08-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7303184
- keyword hits: gpt-5, prompting

### abstract

Longitudinal phenotyping requires observations of the same biological instance to be linked across views and growth periods. However, growth and ripening, viewpoint variation, and intermittent occlusion make cross-view and cross-period instance association unstable in dense tomato scenes. This study developed an instance-level spatiotemporal identity mapping pipeline for tomato fruits in field scenarios and tomato trusses in greenhouse scenarios. The pipeline combines few-shot YOLOv11-seg or zero-shot Segment Anything Model 3 (SAM3) perception, automatically linked keyframes with SAM3 mask propagation, DINOv2 feature-based dynamic time warping (DTW) for inter-period frame alignment, and set-of-mark (SoM) prompting with GPT-5.5 for candidate-level re-identification (Re-ID). The evaluation included 3,295 RGB frames and 2,053 local fruit tracks from five periods, and 3,485 RGB frames and 10,154 local truss tracks from eight periods. The proposed tracking strategy achieved track correctness of 93.5% for tomato fruit and 93.7% for tomato truss. DINOv2-DTW achieved within-one-frame alignment accuracies of 97.0% for fruits and 94.0% for trusses. GPT-5.5 SoM Re-ID achieved 73.4% and 79.5% query-level accuracies, outperforming rule-based, handcrafted, frozen-feature, graph-based, and spatiotemporal baselines and performing comparably to the strongest fine-tuned DINOv2 models. This framework provides an auditable route from image sequences to persistent fruit and truss identities under sparse annotation. By transforming repeated image observations into persistent biological identities, the framework enables longitudinal characterization of size, shape, and color-related traits and provides a scalable foundation for identity-aware crop phenotyping and precision management.

---
