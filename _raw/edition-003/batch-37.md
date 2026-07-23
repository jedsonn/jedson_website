# Classification batch 37 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-37.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6368071`

- title: Long-Horizon Reliability in Human–LLM Interaction: Observations, Failure Modes, and Limits of Procedural Control
- authors: Henric Larsson
- affiliations: not stated
- posted: 2026-03-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6368071
- keyword hits: large language model, large language models, llm, llms

### abstract

Current evaluation of large language models (LLMs) predominantly relies on short-horizon, reset-based interactions designed to assess task performance under controlled conditions. While effective for measuring capability, such regimes structurally limit observation of behaviors that emerge only through sustained interaction—and leave behavioral reliability over extended interaction largely uncharacterized.This paper introduces a qualitative, non-scalable observational method for examining LLM behavior under extended, non-reset conversational conditions, and documents failure modes observed when epistemic pressure weakened or interactional dynamics accumulated unchecked. The observed phenomena range from mild conversational tendencies to substantive failures that produced incorrect outputs, masked errors, or misleading confidence. Two failure modes – Narrative Arc Confabulation and Instance Identity Confusion – are not explicitly named or taxonomized in the literature reviewed as of early 2026 and may represent under-documented phenomena.The paper further examines why awareness of these failure modes does not suffice to prevent them, arguing that long-horizon stability depends on practiced, situational human judgment that resists procedural transfer. The contribution is descriptive and clarificatory: defining an observational space that prevailing evaluation practices structurally exclude, documenting phenomena that emerge within that space, and explaining why reliability under extended interaction is conditional, costly, and human-dependent.

---

## uid: `doi:10.2139/ssrn.6253818`

- title: Early Warning at Scale: Large Language Models for Real-Time Risk Monitoring in SME Lending — Lessons from a Production Deployment
- authors: Terrence Cai
- affiliations: not stated
- posted: 2026-03-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6253818
- keyword hits: agentic, large language model, large language models, llm, prompting

### abstract

This paper presents RiskSensing — a production-deployed, dual-LLM agentic framework for real-time credit risk monitoring in SME lending. Unlike most existing work relying on public datasets or simulated environments, this study is evaluated against live portfolio outcomes, providing empirically grounded evidence of a kind rare in the current literature. The framework operates as a two-stage pipeline: (1) an LLM-augmented connection discovery module that surfaces hidden person-to-business and business-to-business relationships absent from company registries; and (2) an LLM-driven risk signal detection agent that identifies adverse events — operational disruptions, legal issues, bankruptcy signals, and key-person risks — using a custom risk taxonomy and structured prompting. Deployed across an SME credit portfolio at a digital bank, the framework increased detection coverage by 23% for hidden connections and 25% for adverse events (pooled across cohorts) over traditional baselines. Borrowers flagged by hidden connection signals exhibited 2.3× higher subsequent delinquency rates; those flagged by adverse event signals showed 2.4× higher rates, with individual cohorts reaching up to 3.4×. The median lead time from signal detection to delinquency onset was three months — an actionable early warning window for credit intervention. Qualitative expert review confirmed 80% signal precision, with 21% of flagged events representing genuinely novel intelligence unavailable from existing monitoring channels. The findings demonstrate that customer conversational data, when processed through a modular LLM architecture, delivers timely risk intelligence that structured data sources cannot replicate. Practical lessons from deployment include the critical role of expert-validated prompt taxonomy in controlling false positives, the importance of human-in-the-loop review for operational credibility, and the framework’s adaptability across the credit risk lifecycle — from origination screening to collection optimization.

---

## uid: `doi:10.2139/ssrn.6257458`

- title: Reliable Empirical Accounting Research in the Age of Generative AI
- authors: Valerie Zhang, Sean M Song, Christopher Rigsby
- affiliations: not stated
- posted: 2026-03-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6257458
- keyword hits: ai agent, generative ai, llm, llms, retrieval augmented

### abstract

Despite the swift advancements in LLM-enhanced abilities, general generative AI models still hallucinate and cannot reliably distinguish theoretically plausible from implausible foundations. To determine whether domain-specific generative AI can consistently improve academic research in empirical accounting, we construct a retrieval augmented generation (RAG) system based on an extensive corpus of accounting, finance, and economics papers and code. Compared with standalone commercial LLMs, the system nearly eliminates hallucinations, retrieves more relevant prior literature, and produces faster and more reliable replications. Our findings suggest that a domainspecific knowledge base enhances the reliability of AI agents in conducting empirical accounting research, opening a path forward by automating transparent and theoretically grounded analyses.

---

## uid: `doi:10.2139/ssrn.6276278`

- title: Generative AI for Finance: A New Framework
- authors: Bailin Chai, Fuwei Jiang, Lingchao Meng, Tian You, Guofu Zhou
- affiliations: not stated
- posted: 2026-03-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6276278
- keyword hits: generative ai, large language model, llm, llms

### abstract

We propose a generative-AI framework for finance that leverages Large Language Model (LLM) architectures to encode the cross-sectional structure of equity markets. Our approach, Risk Premia BERT (RPBERT), reframes the cross-section as characteristic-ordered sequences where firm identities serve as tokens within economic sentences. Motivated by the attention mechanism that underlies modern LLMs, our approach learns context-dependent representations of firms by selectively weighting characteristics and cross-sectional interactions. Rather than imposing a fixed mapping from characteristics to returns, attention endogenously determines how information enters pricing. Using a BERT-based two-stage implementation, we show that this representation-first approach substantially outperforms leading machine-learning and factor-pricing benchmarks in both statistical fit and economic performance. More broadly, our results demonstrate that attention-based generative models provide a general and powerful paradigm for asset pricing. Our proposed new model can be easily applied to analyze other asset classes as well as corporate or accounting issues.

---

## uid: `doi:10.2139/ssrn.6329139`

- title: The (Large) Language of Veil-Piercing
- authors: Douglas C. Barnard, Peter B. Oh
- affiliations: not stated
- posted: 2026-03-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6329139
- keyword hits: claude, large language model, llm, llms

### abstract

Content analysis has evolved by leaps and bounds. What originally involved manual compilation and analysis of data now harnesses new techniques and technologies that can provide a more robust empirical portrait of courts, aka the “Oracles of the Law.” Advances with this method can enrich our understanding of the Law. One such example concerns the remedy known as piercing the corporate veil. Since its inception, veil-piercing has been notoriously difficult to predict, much less justify, in practice. This has made it a popular topic for “old-fashioned” judicial content analysis, i.e., manual coding of veil-piercing opinions. In 2014 Jonathan Macey and Joshua Mitts (“M&M”) published an innovative study. They deployed automated text analysis, a novel technique at that time, to test a hypothesis about veil-piercing: that the entire universe of veil-piercing opinions comports with a taxonomy of policy rationales. Specifically, M&M contend that veil-piercing occurs if and only if it (1) achieves the goals of a regulatory/statutory scheme; (2) avoids fraud/misrepresentation by shareholders; and/or (3) advances bankruptcy values by eliminating favoritism among creditors. Notably, this tripartite taxonomy omits considerations conventionally believed to be significant to veil-piercing outcomes, such as inadequate capitalization of the firm and a failure to observe corporate formalities. To test their hypothesis, M&M manually coded 1,000 opinions to “train” an algorithm, which predicted the outcomes of 8,380 other opinions with a 76.62% accuracy rate; they then used other algorithms to analyze the semantic differences between veil-piercing outcomes. Remarkably, M&M reported results that correspond precisely to, and thus confirm, their hypothesis. This paper reexamines M&M’s results by replicating their study with new technology. Like M&M, we manually code 1,000 veil-piercing opinions. But we are not interested in simply retracing their steps. Instead, we deploy three algorithmic models. The first model replicates the Naïve Bayes model used in M&M’s study, which is “trained” through manually coded opinions. The second model is Claude, a large language model (“LLM”) unavailable to M&M in 2014, that makes predictions “blindly,” i.e., without access to any manually coded opinions. The third model is an XGBoost Stacked Ensemble model, which uses the classification predictions from both the Naïve Bayes model and Claude as metafeatures. We determine that both Claude and the Stacked Ensemble model outperform M&M’s model, and that the Stacked Ensemble model is the “best,” with an 86.00% accuracy rate. We then deploy the Stacked Ensemble model to predict the outcomes of 16,202 other opinions, and then use various algorithmic models to analyze the semantic differences between veil-piercing outcomes. We obtain statistically significant results that differ from those reported by M&M. Specifically, we find that firm capitalization and corporate formalities are in fact important considerations for veil-piercing. We also find that interactions among words and phrases are even more important than all of the traditional factors, and that judicial reasoning operates through nuanced conditional logic on multiple cognitive levels rather than simply factor-weighing. Our findings have implications for veil-piercing, and for the capacity of LLMs to perform blind (judicial) content analysis.

---

## uid: `doi:10.2139/ssrn.6433859`

- title: Real Hypothetical Negotiations
- authors: Bernard H. Chao
- affiliations: not stated
- posted: 2026-03-18
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6433859
- keyword hits: generative ai, large language model, large language models, llm, llms

### abstract

Patent law's prevailing method for awarding reasonable royalties relies on a "hypothetical negotiation" framework that asks what royalty a willing licensor and willing licensee would have agreed to. In practice, this approach has devolved into a battle of paid experts who manipulate the same evidence to reach dramatically different conclusions, often diverging by orders of magnitude. The current system's reliance on the unwieldy fifteen-factor Georgia-Pacific test, combined with inadequate judicial oversight and jury decision-making limitations, has transformed what should be a reliable proxy of market behavior into a stylized fiction used for strategic advocacy. This article proposes and pilots the first empirically grounded alternative to expert driven reasonable royalty determinations. Drawing on patent law, experimental jurisprudence, negotiation theory and generative AI decisionmaking, it introduces "real hypothetical negotiations." Under this proposal, royalty rates are determined through simulated negotiation. Departing from the traditional remedial goal of strictly restoring the patentee to a pre-infringement state, this proposal prioritizes the constitutional mandate of promoting innovation. Accordingly, the briefing materials include both pre-infringement and post-infringement information to best calibrate damages to the invention's actual economic value. To test this approach, the article reports results from two pilot studies based on Summit 6 LLC v. Samsung Electronics Co., where opposing damages experts reached dramatically different conclusions. Law students using the same case materials reached settlement in only two out seven of negotiations, while competing AI large language models (LLMs) using identical materials achieved settlement in all six cases. These mixed results illustrate both the challenges and promise of operationalizing this approach. The article also describes several potential enhancements to the basic proposal: 1) blinding experts to the party that retained them, or alternatively, 2) court-appointed neutral experts to oversee the negotiation process, 3) conducting simulations multiple times to address outlier results and improve statistical reliability, and 4) using LLMs themselves as negotiators. The article concludes that real hypothetical negotiations offer valuable potential for both actual cases and controlled experiments. Future experiments could filter out value unrelated to innovation, revealing the patent's true technical contribution and guiding damages awards toward outcomes that advance innovation.

---

## uid: `doi:10.2139/ssrn.6448058`

- title: Computational Clinical Judgment: Predicting Risk with Large Language Models
- authors: Ryan Copus, Hannah Laqueur
- affiliations: not stated
- posted: 2026-04-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6448058
- keyword hits: gpt-5, large language model, large language models, llm, llms

### abstract

For seventy years, research has shown actuarial methods outperform clinical judgment. Yet actuarial approaches have limitations: they generally rely on structured data; cannot exploit rare case-specific details; have limited accuracy where outcome data are scarce or incomplete; and cannot offer case-level justifications. Large language models (LLMs) offer a different approach. Like actuarial methods, they aggregate information algorithmically, but like clinicians, they bring general knowledge and can provide case-level justifications. We prompted seven LLMs to assess rearrest risk from 113 parole hearing transcripts and compared their predictions to a machine learning model trained on 4,000 cases with 91 administrative variables. GPT-5 outperformed this actuarial baseline despite no task-specific training on arrest outcomes; however, its stated justifications did not reliably explain its own predictions.

---

## uid: `doi:10.2139/ssrn.6445281`

- title: NIKA V3: A Substrate Observer Study of Geometric Reasoning in DeepSeek-R1-Qwen-32B
- authors: Sushain Devi
- affiliations: not stated
- posted: 2026-04-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6445281
- keyword hits: deepseek, large language model, large language models, qwen

### abstract

Large language models exhibit sophisticated reasoning, yet it remains unclear whether this reflects genuine logical grounding or superficial heuristics. Building on the discovery of dual truth (84.7) and illusion (98.6) manifolds separated by a Layer 16-32 "dead zone," this study introduces a Substrate Observer to visualize truth circuit formation in real-time across 23,000+ generation steps. By scaling to 𝑛 = 500 samples, we demonstrate: 1. Truth circuits compress to 2-3 intrinsic dimensions (a 99.94% reduction), confirming a universal geometric substrate; 2. Without intervention, generation exclusively traverses an illusion manifold (mean truth score 0.027); 3. Möbius steering provides a measurable score lift (+0.006) but remains insufficient to bypass the dead zone; 4. Full pipeline integration-comprising steering, trajectories, stabilizers, and meta-cognitionachieves a breakthrough to sustained truth emergence (0.73). These results characterize the dead zone as an architectural barrier and establish geometric steering as a topological shield necessary for reasoning survival. This work provides a framework to watch, measure, and systematically engineer truth within deep neural networks.

---
