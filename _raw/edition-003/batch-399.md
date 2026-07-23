# Classification batch 399 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-399.answer.json` as a JSON array.

---

## uid: `arxiv:2606.24414v1`

- title: Cycle-Consistent Neural Explanation of Formal Verification Certificates
- authors: Andoni Rodriguez, Alberto Pozanco, Daniel Borrajo
- affiliations: not stated
- posted: 2026-06-23
- source: arXiv
- link: https://arxiv.org/abs/2606.24414v1
- keyword hits: llm, prompting

### abstract

Formal verification produces machine-checkable certificates that attest to the satisfaction or violation of temporal properties, yet these certificates remain opaque to non-specialist stakeholders. We propose a cycle-consistent neural architecture that generates faithful natural language explanations of verification certificates. A forward network NN1 maps certificates to explanations, and an inverse network NN2 reconstructs certificates from explanations; a symbolic verifier closes the loop, providing a differentiable faithfulness proxy. A pointer-generator mechanism ensures lexical grounding by copying state names directly from the certificate. We evaluate on 420 test certificates spanning six verification methods (bounded proof, k-induction, inductive invariant, lasso, reachability, witness pair) in both YES and NO verdict variants, drawn from a financial compliance domain with 207 named states. Our trained architecture, combined with a hybrid inference-time routing strategy, achieves 90.0% cycle-verified soundness, surpassing a multi- LLM few-shot baseline (76.1% for the best of 16 LLM combinations across four frontier models) by 13.9 percentage points. The neural model wins on 10 of 12 verdict/kind categories, with three categories reaching 100% soundness. The architecture offers 860x faster inference (185 ms vs. 160 s per certificate for the full multi-LLM baseline), offline operation, deterministic outputs, and zero per-inference cost. These results demonstrate that trained specialization outperforms general-purpose LLM prompting for structured certificate explanation, while eliminating the deployment constraints of cloud-based inference.

---

## uid: `doi:10.2139/ssrn.6992810`

- title: Do mutual funds transmit trade policy uncertainty risk?
- authors: Ruqin Chen
- affiliations: not stated
- posted: 2026-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6992810
- keyword hits: prompting

### abstract

This paper shows that mutual funds transmit trade policy shocks to firms without direct trade exposure. Exploiting the 2018–2019 U.S.–China trade war as an exogenous shock, I find that non-exposed firms heavily owned by trade-war-affected funds experience lower returns, higher volatility, and stronger co-movement with exposed firms. This spillover arises because losses on exposed holdings trigger redemptions, prompting funds to fire‐sell non‐exposed holdings and depress their prices. Post-trade-war return reversals indicate that the price impact is temporary, and robustness tests rule out supplychain and geopolitical risk channels. These findings reveal how ownership linkage can amplify trade policy shocks into broader financial markets.

---

## uid: `doi:10.2139/ssrn.6981769`

- title: Hyperkalemia-Associated GDMT De-optimization and Clinical Outcomes in Heart Failure: A Systematic Review and Dose-Response Meta-analysis
- authors: Hasan  A. Farhan, Hussein  Hamdan Alkenzawi, Sumaya  Zuhair Fadhil, Abbas Zuhair Marouf
- affiliations: not stated
- posted: 2026-06-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6981769
- keyword hits: prompting

### abstract

Background: Hyperkalemia complicates guideline-directed medical therapy (GDMT) in heart failure (HF), frequently prompting RAAS inhibitor discontinuation or dose reduction. Whether hyperkalemia primarily mediates harm through therapy discontinuation or serves as a disease severity marker remains debated. We evaluated the association between hyperkalemia and GDMT de-optimization, mortality, and hospitalization across HF phenotypes. Methods: We searched MEDLINE, Embase, Cochrane, and Web of Science from inception to January 2025. Primary analysis pooled adjusted hazard ratios (HRs) from 28 studies with REML and Hartung-Knapp adjustment. Sensitivity analyses included odds ratios separately, DerSimonian-Laird, and Bayesian random-effects models. Risk of bias was assessed with ROBINS-I and RoB2. Dose-response was modeled using restricted cubic splines (Greenland-Longnecker method). Publication bias was assessed with contour-enhanced funnel plots, Egger test, Begg test, Doi plot, and trim-and-fill analysis. Results: Forty-two studies (523,847 patients) were identified. The primary analysis yielded HR 2.78 (95% CI 2.41-3.21; I-squared=71.3%; 95% prediction interval 1.67-4.62). Publication bias was detected (Egger p=0.005; Begg p=0.021; Doi plot LFK index 2.84, major asymmetry); trim-and-fill adjusted HR 2.56 (2.18-3.01), approximately 8% attenuation. The dose-response gradient began at 5.0 mmol/L with progressive risk escalation. Spironolactone showed the highest association (HR 4.21); SGLT2 inhibitors showed non-significant association (HR 1.38). HFrEF-only analysis confirmed results. GRADE certainty was low for all outcomes. Conclusions: In this meta-analysis of predominantly observational data with Low GRADE certainty, hyperkalemia is associated with GDMT de-optimization in HF with a dose-dependent gradient from 5.0 mmol/L, although the estimate may be modestly inflated by publication bias. The marker-versus-mediator question requires individual patient data to resolve. Closer monitoring from potassium 5.0 mmol/L may be considered, particularly for patients on MRAs with renal impairment. SGLT2 inhibitors may be associated with better GDMT persistence. HFpEF findings are hypothesis-generating and require dedicated investigation.

---

## uid: `arxiv:2606.26449v1`

- title: ProvenAI: Provenance-Native Traces of Evidence in Generated Answers
- authors: Mohammad Faizan, Dalal Alharthi
- affiliations: not stated
- posted: 2026-06-24
- source: arXiv
- link: https://arxiv.org/abs/2606.26449v1
- keyword hits: retrieval-augmented

### abstract

Retrieval-augmented systems routinely present citations alongside generated answers, yet a citation does not confirm that the corresponding source meaningfully shaped the output. This paper introduces ProvenAI, a framework that decomposes transparency in multi-hop question answering into three independently measurable layers: answer correctness, citation fidelity against benchmark supporting evidence, and per-document influence under leave-one-resource-out intervention. Targeting the HotpotQA distractor benchmark through a seven-stage pipeline covering data normalisation, retrieval indexing, citation-aware answer generation, attribution auditing, ablation-based influence estimation, batch evaluation, and interactive inspection, ProvenAI evaluates 7,405 validation examples drawn from a canonical corpus of 509,300 passages. The system achieves 53.53% answer accuracy alongside a mean citation-fidelity score of 71.55%, and a worked example surfaces what we call the citation-influence gap: a clean citation audit co-occurring with a profile in which one cited source registers only weak influence while seven uncited sources demonstrably shift the output. We formalise the relationship between the implemented surface proxy and a token-level KL-divergence target through a stated faithfulness condition, ground the framework in causal-mediation analysis and database-provenance theory, and discuss how the three measurement layers compose with cryptographic provenance architectures emerging in autonomous scientific discovery. ProvenAI establishes that meaningful transparency in retrieval-grounded QA requires traceable links across retrieved, cited, and behaviourally influential evidence as three distinct, independently measured layers.

---

## uid: `arxiv:2606.26400v1`

- title: When Agents Meet Electric Bus Fleet Operations: Pricing Behavior, Trade-offs, and Policy Implications in an Aggregator Framework
- authors: Jônatas Augusto Manzolli, Ali Eslami, Luis Miranda-Moreno, Jiangbo Yu
- affiliations: not stated
- posted: 2026-06-24
- source: arXiv
- link: https://arxiv.org/abs/2606.26400v1
- keyword hits: agentic

### abstract

Agentic systems are changing how complex operational tasks are coordinated, introducing a new paradigm for connecting heterogeneous data sources and automating processes. Electric bus fleets provide a relevant test case. Their operation requires continuous coordination between service reliability, battery state-of-charge, charger availability, electricity prices, route-energy uncertainty, and vehicle-to-grid (V2G) opportunities. This paper proposes an agentic aggregator framework that streamlines this decision environment by coupling an optimization-based electric bus scheduling model with supervisory agents for disturbance detection, tariff adaptation, and schedule evaluation. The optimization core enforces physical feasibility across routes, chargers, batteries, and V2G exchanges, while the agentic layer interprets changing operating conditions, triggers real-time re-optimization when needed, and defines how flexibility value is allocated between the aggregator and the public transport operator (PTO). A realistic depot case study evaluates day-ahead and real-time operations under profit-based and operation-based coordination modes, considering service delays, route-energy deviations, electricity price shocks, and combined disturbances. The results show that agentic aggregation can support adaptive fleet-grid coordination by maintaining feasible schedules, activating re-optimization selectively, and improving the use of charging and V2G flexibility. However, they also reveal a critical trade-off: the same agentic capability that reduces operational complexity can extract value from the PTO when configured around profit-oriented pricing. These findings suggest that agentic aggregators can become useful for managing electric bus V2G operations, but their deployment in public-fleet contexts requires transparent coordination modes, auditable tariff-setting, and explicit value-sharing rules.

---

## uid: `arxiv:2606.26205v1`

- title: Knowledge-augmented Agentic AI for Mental Health Medication Information Seeking
- authors: Huizi Yu, Jian Liu, Wenkong Wang, Lingyao Li, Jiayan Zhou, Zhaoqian Xue, Xiang Li, Xinxin Lin
- affiliations: not stated
- posted: 2026-06-24
- source: arXiv
- link: https://arxiv.org/abs/2606.26205v1
- keyword hits: agentic

### abstract

Patients increasingly seek medication information online, yet safety knowledge for psychiatric drugs is split between regulatory adverse-event records, which are authoritative but abstract, and patient narratives, which are experience-near but unvalidated. Integrating them without conflating evidence and anecdote is especially consequential in psychiatry, where poorly contextualised information can amplify fear, nocebo responses, and non-adherence. Here we develop a provenance-aware, knowledge-graph-based multi-agent framework unifying 466,525 Reddit posts, 60,782 WebMD reviews, and twenty years of U.S. FDA Adverse Event Reporting System records for nine antidepressants. A large-language-model entity-recognition pipeline benchmarked against physician annotations reached highest F1 scores of 0.969 for medications and 0.973 for conditions. The two community platforms were far more concordant with each other (overlap up to a Jaccard similarity of 0.905) than with regulatory reports, indicating that patient-generated data form a partly independent safety signal. For sertraline, many adverse events appeared in community sources hundreds of days before the corresponding FDA date. A Neo4j knowledge graph grounded in ATC-N, ICD-10, and MedDRA vocabularies preserves provenance, keeping every claim traceable and regulatory facts distinct from patient experience. These results establish source-aware integration as a route to more auditable psychiatric medication information, with usefulness and patient benefit to be tested prospectively.

---

## uid: `arxiv:2606.25894v1`

- title: Enhancing Brain MRI Anomaly Detection and Reasoning with ROI Rethink and Synthetic Data
- authors: Shangkun Li, Jie Xu, Yi Guo, Zeju Li, Yuanyuan Wang
- affiliations: not stated
- posted: 2026-06-24
- source: arXiv
- link: https://arxiv.org/abs/2606.25894v1
- keyword hits: fine-tuning

### abstract

Medical vision-language models typically generate diagnoses through single-pass inference without indicating which image regions support their conclusions. This lack of spatial grounding limits clinical utility: outputs cannot be audited, and models may hallucinate findings on normal scans. We present BrReMark (Brain Rethink via ROI Marking), a framework that introduces explicit region marking into brain MRI diagnosis. The model first generates hypotheses about potential abnormalities and grounds them through explicit bounding box marking, then verifies conclusions by re-examining the marked evidence. Training combines supervised fine-tuning on structured reasoning trajectories with reinforcement learning using a composite reward over localization accuracy and diagnostic reasoning. Furthermore, we integrate a domain randomization-based pathology synthesis augmentation strategy to improve the model's generalizability to out-of-distribution (OOD) data. On internal benchmark, BrReMark improves mAP50 from 0.74% to 37.54% compared to the base model, while achieving 21.57% Clinical F1 and 45.26% diagnostic accuracy. On NOVA OOD benchmark, it also achieves competitive overall performance with a 45.7% reduction in false positives compared to the state-of-the-art, indicating reduced hallucination on rare pathologies. These findings suggest that explicit hypothesis-verification grounding is a practical path toward trustworthy open-ended brain MRI diagnosis across both in-distribution and OOD settings.

---

## uid: `doi:10.2139/ssrn.6878119`

- title: CAIRN: Cost-Aware Information Routing for Underwriting
- authors: John Christiansen
- affiliations: not stated
- posted: 2026-06-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6878119
- keyword hits: agentic

### abstract

A lending decision is a sequence of purchases of information. Each external source-a business register, a credit bureau, an open-banking feed, an asset valuation-carries a price and buys a quantum of certainty about a borrower. Production engines acquire a fixed waterfall of these sources for every applicant. We introduce CAIRN (Cost-Aware Information Routing for uNderwriting), an agentic engine that instead treats each acquisition as a Pandora's box in the sense of Weitzman and opens the next box only while its value of information exceeds its cost. The central contribution is a dual-currency cost: every source is priced as a vendor fee plus the monetised cost of the large-language-model tokens burned to ingest and reason over it. We cast the full intake-to-settlement workflow as a partially observable Markov decision process whose belief state is coupled to IFRS 9 PD, LGD, EAD and SICR models, so the value of information is expressed in expected-loss pounds and scales with exposure. Across a synthetic UK loan-book of 1,200 applications under realistic vendor fees, CAIRN reduces cost per decision by 38.7% (from £33.54 to £20.57) while achieving lower regret against a perfect-information oracle-of order £1.3m a year at one hundred thousand applications. We are deliberately honest about where the saving arises: at current vendor pricing it is driven by fee avoidance and the token term is second-order, yet the token term is the correct general model, is the entire cost of nominally free open-data sources and becomes first-order as reasoning models grow more token-hungry. The engine ring-fences mandatory compliance checks, audits every decision to the individual acquisition event, and attaches a plain-English rationale.

---
