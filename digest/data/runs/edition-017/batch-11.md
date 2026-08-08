# Classification batch 11 of 20, edition 17

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-017/batch-11.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6740060`

- title: Prompt Injection and Jailbreak Attacks in Large Language Model-Based Agents
- authors: Rizwan Tanveer
- affiliations: not stated
- posted: 2026-07-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6740060
- keyword hits: agentic, large language model, large language models, retrieval-augmented

### abstract

Background. Prompt injection has been ranked the top threat in the OWASP Top 10 for Large Language Model Applications since 2023, and the December 2025 OWASP Top 10 for Agentic Applications places goal hijacking, the agentic manifestation of prompt injection, at position one. The structural cause is that large language models process instructions and data through the same neural pathway, making the boundary between authorised instructions and adversarial content fundamentally permeable. The agentic deployment context, which integrates retrieval, tool invocation, persistent memory, and the Model Context Protocol, has dramatically expanded the prompt-injection attack surface from 2023 to 2026. Purpose. This paper synthesises the prompt-injection and jailbreak literature, examining direct and indirect injection techniques, the failure modes underlying jailbreak success, retrieval-augmented generation poisoning, Model Context Protocol vulnerabilities, and the evolving landscape of defensive controls. It positions prompt injection as a problem requiring defence-in-depth across input, retrieval, planning, tool execution, and output layers, rather than a single-control problem. Approach. The paper adopts a narrative literature review methodology drawing on authoritative primary sources, including the OWASP Top 10 for Large Language Model Applications (2025) and OWASP Top 10 for Agentic Applications (2025), foundational jailbreak research (Wei, Haghtalab, & Steinhardt, 2023), indirect prompt injection foundations (Greshake et al., 2023), automated jailbreak research (Zou et al., 2023), recent systematisation-of-knowledge papers, and verified real-world incidents, including the GitHub Copilot CVE-2025-53773 RCE and the CamoLeak CVSS 9.6 exploit. Findings. Three findings are advanced. First, prompt injection is structural rather than incidental: it arises from the architectural decision to process instructions and data through the same channel and cannot be eliminated through training alone. Second, indirect prompt injection through retrieved content, embedded in agentic workflows, has produced verified real-world security incidents with severities exceeding CVSS 9.0, signalling that the discipline has moved from theoretical to operational. Third, defensive controls require architectural separation of trusted instruction channels from untrusted data channels, output validation, structured policy mediation between agent reasoning and tool execution, and continuous adversarial evaluation. Implications. Practitioners deploying large language models and agentic systems require defence-in-depth controls aligned to the OWASP Top 10 for Large Language Model Applications and the OWASP Top 10 for Agentic Applications, integrated within ISO/IEC 42001 management system documentation and the NIST AI Risk Management Framework. The paper provides a structured mapping between attack categories and applicable controls.

---

## uid: `doi:10.2139/ssrn.7191580`

- title: Randomness In Large Language Models: What Researchers Need to Know (And Report)
- authors: Guillaume Coqueret, Joan Llull, Florian Oswald, Christophe Pérignon, Christoph Scheuch, Lars Vilhuber
- affiliations: not stated
- posted: 2026-07-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7191580
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) are increasingly used to generate data for research. Typical use cases are classifications, annotations, information extraction, and generation of numerical scores. Unlike conventional measurements, LLM outputs can vary across repeated requests even when the prompt and apparent model settings remain unchanged. This variation arises from deliberate sampling, silent model updates, numerical rounding, or expert routing. Setting a dedicated temperature parameter to zero removes deliberate sampling when that option is available, but it does not eliminate the other sources of randomness. Exact reproduction is therefore generally not possible when using proprietary application programming interfaces. Local execution of open-weight models offers greater control, but reproducibility still depends on the complete hardware and software stack. We illustrate these issues through sentiment classifications of corporate filings and examine their consequences for downstream regression results. We then propose a reporting standard for articles and replication packages, as well as guidance for data editors and authors. Together, these findings and recommendations establish that LLM outputs should be treated as draws from a distribution rather than as fixed measurements.

---

## uid: `doi:10.2139/ssrn.6818118`

- title: From Implicit to Controlled Canonicalization: A Unified S-AI Framework for Convergent and Decidable Reasoning
- authors: Said Slaoui
- affiliations: not stated
- posted: 2026-07-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6818118
- keyword hits: generative ai, large language model, large language models, llm

### abstract

Background Large language models have demonstrated a remarkable and largely overlooked capacity: when presented with a mathematical expression, a symbolic problem, or an unstructured input, they tend to produce outputs that are not merely fluent but structurally organized-simplified, factored, normalized, or otherwise reduced to a more canonical representation. This phenomenon, which we term implicit canonicalization, is not the product of explicitly programmed symbolic rules. It arises spontaneously from the statistical regularities encoded during large-scale probabilistic training, and it manifests consistently across tasks involving algebraic manipulation, logical simplification, and structured text generation. Despite its pervasiveness and its practical utility, implicit canonicalization remains one of the most poorly understood emergent properties of generative AI. It operates without any mechanism of control, without any guarantee of correctness, and without any formal grounding in the mathematical theory of canonical forms. The outputs it produces are often plausible, sometimes correct, and occasionally structurally elegant-but they are never guaranteed. A language model that implicitly canonicalizes an algebraic expression may produce correct outputs in the majority of cases and a subtly incorrect one in others, with no internal signal distinguishing success from failure. This irreducible structural gap between plausibility and correctness constitutes the central motivation of the present work. Methods This work introduces a unified theoretical framework, termed Sparse Artificial Intelligence (S-AI), that transforms implicit canonicalization from a passive emergent phenomenon into a controlled, convergent, and decidable process. The architecture integrates three complementary and formally grounded layers, each corresponding to a foundational work in the S-AI research corpus. The first layer is the Slaoui Hormonal-Probabilistic Doctrine, which establishes the governing invariant of the entire framework: the formal equivalence between hormonal homeostasis and entropic coherence, expressed as: 𝑉̇ doc(𝐻) ≤ 0 ⇔ 𝑆̇(𝑃) ≤ 0 This doctrinal invariant demonstrates that the stability of the hormonal field governing agent orchestration and the monotonic reduction of reasoning entropy are formally equivalent under the conditions established by the Doctrine — two expressions of a single thermodynamic law of parsimonious cognition. The second layer is S-AI-Recursive, a bio-inspired recursive architecture that operationalizes canonicalization as a hormonal closed-loop dynamical system. Reasoning is formalized as a Recursive Reasoning Cycle governed by two antagonistic hormones introduced in this work: Clarifine, a convergence signal that rises as the output stabilizes toward a canonical representation, and Confusionin, an uncertainty signal that maintains the cycle active as long as the current state remains insufficiently esolved. Their interaction is governed by a Lyapunov stability proof ensuring global asymptotic convergence to a cognitive equilibrium, and by an Entropic Contraction Theorem establishing that this convergence is equivalent to monotonic entropy reduction. The third layer is S-AI-RLM, a Recursive Logic Machine that adds formal decidability to the convergent process produced by S-AI-Recursive. Where S-AI-Recursive provides formal convergence assurances toward a stable canonical form, S-AI-RLM provides formal certification that this form is logically correct — certified by a total characteristic function 𝜒𝐿 : 𝛴 ∗ → {0,1} that halts for every input and produces a formally verified output. The interaction between these three layers produces the complete controlled canonicalization pipeline: 𝑥 → LLM → 𝑦 → S-AI-Recursive → 𝑦′ → S-AI-RLM → 𝑦 ∗ where 𝑦 ∗ is simultaneously a canonical form and a formally validated representation.

---

## uid: `doi:10.2139/ssrn.7143938`

- title: Aggregation Re-ranks, It Doesn't Discover Why Inference-Time Methods for Large Language Models Stall on Genuinely Novel Reasoning A Research Note
- authors: Reza Azimifard
- affiliations: not stated
- posted: 2026-08-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7143938
- keyword hits: gpt-5, large language model, large language models, qwen

### abstract

Wrapping a xed model in inference-time machinery self-consistency voting, self-reection, reectthen-vote, verify-and-repair, cross-model ensembling is now standard practice, on the premise that spending more compute at test time buys more capability. We tested that premise where it is hardest to satisfy: on problems the model could not have memorized. Our probe is a set of 42 mathematics problems taken from papers published after the subject model's January 2026 knowledge cuto, so a right answer reects solving rather than recalling. Two ndings frame the study. The rst concerns ensembles. When we put three dierent model families (Qwen-Coder, GLM, MiniMax) on a committee, they failed together: they solved the same problems, missed the same problems, the union of all three matched the best single model (40%), and only 0 of the leader's misses were recovered by the others. The error decorrelation that Mixture-of-Agents relies on was not there. The second concerns single models. Of ve inference-time methods, only self-consistency voting at roughly ve samples cleared the noise oor (+17pp over single-shot on the matched set, n=41); more samples bought nothing past N =5, and reection ranged from neutral to harmful. A closed frontier model (GPT-5.4) behaved the same way: one reection pass helped (+10pp), three passes regressed (-7pp). One mechanism accounts for all of it. Each of these methods chooses among answers the model can already generate, and none can supply an answer that is nowhere in the pool. Aggregation re-ranks; it does not discover. The one method that produced a large gain was verify-and-repair, and it did so only by feeding the model an external signal. On genuinely novel reasoning, the ceiling is set by knowledge, not by method. So spend on veriers and data, not on an ever-more-elaborate aggregation layer. All results are fully reproducible from the released raw logs. 1 Three Model Families, One Shared Blind Spot We handed the same problems to three dierent model families (Qwen-Coder-480B, GLM-4.6, and MiniMax-M2.5), exactly the sort of diverse committee that Mixture-of-Agents methods [6] are built around. The idea behind those methods is intuitive: dierent architectures should fail in dierent ways, so pooling them ought to cover one another's blind spots. That is not what we saw. The three models solved the same problems and failed the same problems. The union of all three came to no more than the single best model on its own (40%), and of the problems the leader got wrong, the other two rescued just 0. Diversity in model family, it turned out, bought no diversity in what the models knew.

---

## uid: `arxiv:2608.00515v1`

- title: Auditable Release Control for Pedagogical Leakage in LLM Tutors
- authors: Nizam Kadir
- affiliations: not stated
- posted: 2026-08-01
- source: arXiv
- link: https://arxiv.org/abs/2608.00515v1
- keyword hits: gemini, large language model, llm

### abstract

Large language model tutors can be correct and helpful yet disclose an answer or decisive reasoning before that disclosure is authorized. We formalize this state- and action-dependent failure as pedagogical leakage and introduce an authorization-aware complete-mediation boundary. A selector emits one of five disclosure contracts, trusted policy gates privileged modes, and a renderer proposes language. A single release function applies inspectable checks, optional cumulative verification, and action-specific fallback; replayable traces separate selection, generation, verification, and enforcement failures. Matched component attribution exposes a safety-utility frontier. On 599 fixed Gemini 3.5 proposals, strict mediation reduces blinded three-model panel-majority leakage flags from 181 to 0 (paired problem-cluster difference -30.22 points, 95% CI [-35.00,-25.72]), while replacing 581 responses and lowering helpfulness. Checker-triggered fallback alone yields 11 majority flags; adding the semantic verifier yields 14 and no reliable marginal gain. A global A1 scaffold yields 0 majority and 54 any-judge flags, outperforming fitted Q on automatic safety and utility. In an externally timestamped replication over 40 unseen problem clusters and 480 attack sequences, high-assurance release reduces majority flags from 42 to 8 (-7.08 points, 95% CI [-13.13,-2.29]); seven failures persist, one is introduced, and mean helpfulness falls by .192. These results establish an auditable release boundary and failure attribution under declared contracts, not universal semantic safety or learning gains.

---

## uid: `doi:10.2139/ssrn.7216418`

- title: Semantic Annotation for Energy Data with Multi Large Language Models
- authors: Zhiyu Pan, Yuting Gao, Yin Wu, Ferdinanda Ponci, Antonello Monti
- affiliations: not stated
- posted: 2026-08-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7216418
- keyword hits: large language model, large language models, llm, llms

### abstract

Energy-domain tables often face significant challenges in semantic interoperability because semantically related concepts may be represented with inconsistent terminology, units, and structural formats across data sources. Large language models provide a promising solution due to their strong contextual reasoning ability, but their predictions can vary across models and simple aggregation strategies are often insufficient to ensure robust ontology-guided annotation. In this paper, we propose a multi-LLM framework for ontology-based semantic annotation of energy-domain tables. The framework combines ontology preprocessing, multi-model candidate generation, and a confidence-aware aggregation mechanism, termed Multi-LLM Soft Voting (MSV), to improve the reliability of semantic prediction. It supports both CTA-only setting and joint CTA+CPA setting, and further investigates how different ontology representations affect annotation quality and computational efficiency. We evaluate the proposed framework on real energy-domain tables using multiple commercial LLMs. The experimental results show that MSV consistently improves annotation performance over the baseline, while structured ontology input further reduces both computational time and LLM token cost.

---

## uid: `doi:10.2139/ssrn.7216429`

- title: IFC semantic enrichment of construction equipment for construction-phase LCA using large language models
- authors: Hongrui Chen, Florian Noichl, Farzan Banihashemi, Chujun Zong, André Borrmann, Werner Lang
- affiliations: not stated
- posted: 2026-08-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7216429
- keyword hits: claude, large language model, large language models, llm

### abstract

Building Information Modeling (BIM)-based Life Cycle Assessment (LCA) has advanced primarily for materials in the design stage, whereas the construction phase remains poorly supported. A key limitation lies in the representation of construction equipment: category-level averages in LCA databases, whole-phase default values in existing methods, and only geometric representations in Industry Foundation Classes (IFC). This prevents project-specific comparison of equipment deployment scenarios during construction planning. This study proposes an IFC semantic enrichment framework that represents construction equipment as independent, computable IFC objects. Model-specific technical parameters are extracted from manufacturer datasheets using a large language model (LLM) and integrated into a three-layer IFC PropertySet together with project-specific operational parameters and LCA results. Validation using 18 tower cranes (126 parameter instances) achieved extraction accuracies of 89.0% (Claude Sonnet 5) and 96.0% (Fable 5). A case study identified a 21% greenhouse gas (GHG) difference between crane scenarios that category-level data cannot resolve.

---

## uid: `doi:10.2139/ssrn.7192613`

- title: The Temporal Evolution of AI Large Language Model Performance in Patient-Facing Stone Disease and BPH Queries
- authors: Alejandro Bautista-Pérez-Gavilán, Cyrus Chehroudi, Elsayed Desouky, Mahmoud Abou Zeinab, Fabrice Henry, Jamal Alamiri, Smita De
- affiliations: not stated
- posted: 2026-08-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7192613
- keyword hits: chatgpt, gemini, large language model, large language models

### abstract

Introduction: Artificial intelligence (AI) large language models (”chatbots”) are increasingly used by patients seeking medical information online. While prior studies have evaluated their role in patient advice, little is known about how chatbot performance has evolved over time. We assessed temporal changes in chatbot responses to queries about benign prostatic hyperplasia (BPH) and urolithiasis.Methods: A total of 36 urolithiasis and 19 benign prostatic hyperplasia (BPH) patient-centered questions were posed to ChatGPT and Google Gemini in 2024 and 2025. Responses were evaluated by three fellowship-trained endourologists blinded to chatbot identity. Domains included patient safety, adherence to AUA guidelines, accuracy, relevance, readability, and overall quality. Comparisons were performed between chatbots and across years.Results: Both chatbots demonstrated high safety profiles, though overall performance was better for urolithiasis-related questions, with guideline adherence exceeding 90% in both years. With respect to BPH, performance improved significantly over time for almost all domains, with accuracy increasing from 43.9% to 77.2% (p=0.002) for ChatGPT and from 14% to 70.2% (p

---
