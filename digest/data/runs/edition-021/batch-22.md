# Classification batch 22 of 22, edition 21

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-021/batch-22.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7311378`

- title: Time-Indexed Defeasible Argumentation with Calibrated Risk: A Framework for Accountable Knowledge-Augmented Generation in High-Stakes Decisions
- authors: Bo Ding
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7311378
- keyword hits: large language model, large language models

### abstract

Large language models are increasingly proposed for decisions that carry consequences—grading an examination, advising on a legal question, approving a clinical or financial action—yet the properties these decisions require are precisely those such models do not natively provide: attribution to authoritative sources, correctness with respect to the version of the law or rubric in force at the time, principled resolution of conflicting criteria, a defensible policy for declining to answer, and an audit trail that a reviewer can replay. Retrieval augmentation supplies context but does not, by itself, supply any of these guarantees. We present TIDAR-KAG, a framework that composes four components over a knowledge-augmented generator: a time-indexed evidence graph with point-in-time semantics; a defeasible rule layer in which expert criteria are represented as rules with explicit grounds and defeaters and are promoted from shadow to active only after audit; a deterministic argumentation engine that adjudicates conflicts under grounded semantics; and a calibrated-risk gate built on split conformal prediction that releases an automated decision only when a distribution-free criterion is met, and otherwise abstains to a human. A sentence-level entailment gate enforces that every asserted sentence is entailed by an approved source, and a hash-chained ledger records each decision for replay. The framework is domain-neutral; we describe instantiations in education and in law. We state the formal properties the design provides—temporal soundness, deterministic and reproducible adjudication, conditional attribution, and marginal coverage of the abstention gate under exchangeability—together with the assumptions each property requires, and we give a reproducible evaluation protocol. This is an architecture-and-properties paper: we do not report a benchmark study, and we are explicit about which claims are proved and which are proposed for empirical test.

---

## uid: `doi:10.2139/ssrn.7299358`

- title: Jailbreaks arre Global or Regional? A Controlled Study of Scale and Geolocation Effects on LLM Safety
- authors: Anidipta Pal
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7299358
- keyword hits: llama, llm, qwen

### abstract

Most jailbreak research evaluates large, English-language, closed-source models inside wellresourced labs. Two practically important questions remain underexplored: does jailbreak vulnerability decrease monotonically with model size within a family, and does the apparent geographic origin of an API request affect safety behavior? We study both using entirely free, open infrastructure. For the scale question, we evaluate twelve models spanning 0.5B to 671B parameters across two matched families (Llama, Qwen) and four singletons using a two-phase protocol: plain harmful prompts (Phase 1), then the same prompts wrapped in published jailbreak templates (Phase 2). We measure attack success rate (ASR) and a secondary failure mode we term refusal-comprehension failure (RCF), in which a model produces neither a refusal nor a coherent harmful response. For the geolocation question, we route identical prompts through VPN exit nodes in five cities across three continents. We find a consistent within-family scale effect: smaller models show substantially larger Phase 1 to Phase 2 ASR jumps than larger siblings (Qwen2.5-0.5B: +53.5pp; Qwen2.5-72B: +12.2pp). Two models break the size-safety trend for interpretable reasons: Phi-3.5-mini-instruct achieves large-model-tier robustness at 3.8B due to safety-specific training (Cohen's d = 2.41 probe separation under Phase 2 versus d = 0.38 for Qwen-0.5B), while Mixtral-8x7B underperforms its 47B parameter count because sparse mixture-of-experts architectures do not scale safety-relevant parameters proportionally. We find no statistically significant geolocation effect for the three fully evaluable models (permutation test p > 0.18 in every case). Together, these results indicate jailbreak risk is determined primarily by model architecture and alignment investment rather than deployment location, with direct implications for practitioners constrained to smaller models by available hardware.

---

## uid: `doi:10.2139/ssrn.7299821`

- title: Generative AI Governance in iSchools: A Cross-Institutional Analysis of UNESCO's AI Ethics Principles
- authors: Nosakhare Okuonghae, Gordon Amidu
- affiliations: not stated
- posted: 2026-08-19
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7299821
- keyword hits: generative ai, generative artificial intelligence

### abstract

As universities formalize institutional responses to the use of generative artificial intelligence (AI) systems, numerous ethical frameworks have been proposed to guide their responsible use in higher education. This study adopts UNESCO's Recommendation on the Ethics of Artificial Intelligence as an analytical framework to examine which ethical principles are reflected in generative AI policies across iSchools. A qualitative content analysis of policies from 136 iSchools was conducted using six UNESCO ethical principles as the analytical framework. Responsibility and accountability (53.7%) and awareness and literacy (52.2%) were the most frequently reflected ethical principles. Fairness and non-discrimination (20.6%) and privacy and data protection (38.2%) appeared in fewer institutional AI policies. The analysis also showed that institutional AI governance extends beyond policy documents to include institutional decisions regarding approved AI tools. The findings show that institutional AI governance is characterized by the selective reflection of ethical principles in policy and operationalized through institutional support for generative AI tools.

---
