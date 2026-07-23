# Classification batch 40 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-40.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6663280`

- title: FedDualFix: Hierarchical Federated Learning for Adaptive Multi-Agent Program Repair via Dual-Modality Modeling
- authors: Xiaolin JU, Qingyun Liu, Chang Li, Haocheng Wang, Heling Cao, Xiang Chen
- affiliations: not stated
- posted: 2026-04-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6663280
- keyword hits: gpt-4, large language model, large language models, llm, llms

### abstract

Recent advances in large language models (LLMs) have improved automated program repair (APR) by interpreting failures, generating context-aware patches, and refining fixes iteratively, improving repair accuracy and coverage. However, existing methods still face three key limitations: they often rely on centralized training on sensitive codebases; their pipelines are rigid, one-pass processes that cannot adapt to the complexity of a defect; and they do not fully exploit auxiliary semantic signals, such as bug reports or documentation. To address these challenges, we propose FedDualFix, a federated multi-agent repair framework that improves repair accuracy, efficiency, and semantic coherence in heterogeneous and data-locality-constrained environments. FedDualFix decomposes the repair process into specialized agents for (i) context modeling, (ii) semantic slicing, (iii) fault localization, (iv) patch generation, and (v) cross-modal alignment. A hierarchical control controller with confidence-guided scheduling enables early exits for simple defects and triggers deeper, structure-aware reasoning for complex or ambiguous cases. Dual-modality alignment further associates code-level edits with natural-language descriptions to enhance semantic plausibility. Experiments on Defects4J using several LLMs—including GPT-4o—show that FedDualFix produces 58 correct repairs and achieves 52.1% Top-1 precision, outperforming state-of-the-art baselines such as Recoder (43%) and CodeT5 (38%). The adaptive scheduling mechanism reduces inference time by more than 25%, and ablation studies demonstrate the contribution of hierarchical control, multi-agent design, and dual-modality integration. These results highlight the potential of combining federated coordination with adaptive multi-agent reasoning to support accurate and scalable APR in real-world software maintenance settings.

---

## uid: `doi:10.2139/ssrn.6499098`

- title: Threshold-Convergent Systems: The Shared Mathematical Structure Governing Quantum Error Correction and Oracle Consensus for Physical Asset Verification and Collateralisation Under Basel IV
- authors: Robert Stillwell
- affiliations: not stated
- posted: 2026-04-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6499098
- keyword hits: claude, gemini, gpt-4, llama

### abstract

This paper identifies and formally characterises a class of distributed information systems — threshold-convergent systems — in which individual participants are unreliable, but a mathematically definable critical threshold exists such that when participant error rates fall below it, adding more participants produces exponential improvement in system-level reliability. Above the threshold, scale amplifies noise. Below it, scale suppresses noise exponentially. We establish four axiomatic properties that define the class: component unreliability, threshold existence as a phase boundary, emergent composability of reliable outputs from unreliable inputs, and adversarial resistance up to formally bounded fractions. We demonstrate that this threshold phenomenon governs two independently developed systems operating in entirely different physical domains: quantum error correction, as demonstrated by Google Quantum AI's Willow processor achieving below-threshold surface code performance in December 2024, and oracle consensus for physical asset verification, as implemented in the CVR Protocol's reputation-weighted Bayesian fusion with Markov Chain Monte Carlo convergence guarantees. We derive the formal structural mapping between these two systems, establishing that the error suppression factor Λ in quantum surface codes corresponds to the posterior credible interval narrowing rate in MCMC-convergent oracle networks, that qubit code distance scaling corresponds to oracle network scaling, and that the surface code error threshold corresponds to the oracle deviation threshold. We further connect the phase transition structure to the 2D random-bond Ising model mapping established by Dennis et al. for quantum error correction, and show that the MCMC ergodic regime transition in oracle consensus is governed by the same class of mathematical theorems about when distributed, noisy, stochastic processes produce reliable collective outputs. We then demonstrate that this shared mathematical structure has direct regulatory implications: the threshold-convergent property of the CVR Protocol's oracle network is the precise mechanism that satisfies the Basel Committee on Banking Supervision's SCO60 'ongoing basis' classification requirement for Group 1a tokenized physical assets. The dynamic verification discount derived from the MCMC posterior credible interval provides continuously updating capital relief calculable from the threshold-convergent mathematics, and the framework enables a principled three-class regulatory taxonomy distinguishing threshold-convergent verification from non-convergent continuous monitoring and periodic audits. Builds on: https://ethresear.ch/t/23577 · https://ethresear.ch/t/23609 · MCMC Basel SCO60 Paper (March 2026) AI DISCLOSURE: AI tools (Claude, GPT-4, Gemini, Ollama) were used for drafting assistance, mathematical notation formatting, and literature review. All research claims, mathematical proofs, structural correspondences, and regulatory analysis were authored and verified by the human authors.

---

## uid: `doi:10.2139/ssrn.6669973`

- title: Saying More Than They Know: A Framework for Quantifying Epistemic-Rhetorical Miscalibration in Large Language Models
- authors: Asim  Dilawar Bakhshi
- affiliations: not stated
- posted: 2026-04-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6669973
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models (LLMs) exhibit systematic miscalibration with rhetorical intensity not proportionate to epistemic grounding. This study tests this hypothesis and proposes a framework for quantifying this decoupling by designing a triadic epistemic-rhetorical marker (ERM) taxonomy. The taxonomy is operationalized through composite metrics of form-meaning divergence (FMD), genuine-to-performed epistemic ratio (GPR), and rhetorical devicedistribution entropy (RDDE). Applied to 225 argumentative texts spanning approximately 0.6 Million tokens across human expert, human non-expert, and LLM-generated sub-corpora, the framework identifies a consistent, model agnostic LLM epistemic signature. LLM-generated texts produce tricolon at nearly twice the expert rate (∆ = 0.95), while human authors produceerotema at more than twice the LLM rate. Performed hesitancy markers appear at twice the human density in LLM output. FMD is significantly elevated in LLM texts relative to both human groups (p

---

## uid: `doi:10.2139/ssrn.6670534`

- title: Artificial Intelligence Techniques for Legacy Software: A Systematic Literature Review
- authors: Andrey Justo, Jefferson Seide Molléri, Luiz  Eduardo Galvão Martins
- affiliations: not stated
- posted: 2026-04-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6670534
- keyword hits: fine-tuning, large language model, large language models, llm, llms, prompt engineering

### abstract

Context: Legacy software systems remain critical to modern organizations, but face challenges to evolve due tooutdated technologies, poor documentation, and accumulated technical debt. Recent advances in Artificial Intelli-gence (AI), particularly Large Language Models (LLMs), have introduced new opportunities for automating softwareengineering tasks, including code generation and system modernization. However, their applicability and effectivenessin legacy contexts are not yet fully understood.Objective: This study aims to systematically analyze how AI techniques are applied to support code generationand modernization of legacy software systems, identifying current approaches, benefits, limitations, and researchgaps.Method: Our study conducted a Systematic Literature Review (SLR) with total of 1,349 studies retrieved frommajor digital libraries, and 52 primary studies selected through rigorous inclusion and exclusion criteria. Data extrac-tion and quality assessment were performed to analyze AI techniques, tools, and application contexts.Results: The analysis identified four main categories of AI techniques: Prompt Engineering, Fine-Tuning, DeepLearning, and Traditional Machine Learning. Transformer-based models dominate recent approaches, particularly ingenerative tasks. The findings indicate improvements in developer productivity, maintainability, and support for legacysystem modernization. However, significant challenges remain, including trust, reliability, semantic inaccuracies, lackof explainability, and integration with developer’s ecosystem.Conclusion: AI techniques, especially prompt-based approaches, show a strong potential support for legacy soft-ware evolution. However, effective adoption requires human oversight, iterative validation, and context-aware design.Key research gaps persist in reliability, trustworthiness and long-term quality assurance, indicating the need for furtherempirical studies to enable robust AI-driven modernization of legacy systems.

---

## uid: `doi:10.2139/ssrn.6595298`

- title: Knowledge, LLMs, and the Information Ladder: From Shannon to Kolmogorov
- authors: Alec Litowitz, Nick Polson, Vadim Sokolov
- affiliations: not stated
- posted: 2026-04-28
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6595298
- keyword hits: large language model, large language models, llm, llms

### abstract

We develop a unified framework for understanding knowledge in large language models (LLMs), tracing an arc from Shannon's theory of communication to Kolmogorov's theory of complexity. LLMs are Shannon machines at the physical layer, converting photons to tokens at thermodynamic cost, yet they aspire to be Kolmogorov machines at the semantic layer, compressing world knowledge into parametric representations. We organize this duality as an information ladder: five questions ranging from Shannon's "can the message be transmitted?" through Cover's "how much information does it contain?" and Kolmogorov's "what does it mean?" to Good's "can the system improve itself?" and Hayek's "which questions are worth asking?" Drawing on the token economics of Litowitz et al. [2026b,a], the Kolmogorov-GAM architecture of Polson and Sokolov [2025], Good's ultraintelligent machines [Good, 1965], Hayek's dispersed knowledge [Hayek, 1945], and Cover's entropy measurements [Cover and King, 1978, Leung-Yan-Cheong and Cover, 1978], we identify model collapse as a central threat to the Kolmogorov frontier and ask what this framework implies for knowledge representation by 2100.

---

## uid: `doi:10.2139/ssrn.6540820`

- title: The Larynx Problem: Why Large Language Models Are Not Artificial Intelligence
- authors: Björn Wikström
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6540820
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models have achieved remarkable fluency in producing human-like text, leading many to conflate linguistic competence with intelligence. This paper argues that this conflation is a category error with deep historical roots-analogous to mistaking the larynx for the brain. We term this the Larynx Problem: LLMs are trained on the output channel of human intelligence-language-not on intelligence itself. The brain does not think in words; it processes information as distributed activation patterns across functionally specialized regions, producing language only at the terminal encoding stage. We trace how this error arose from a 1969 substitution in AI research goals-from how does intelligence emerge? to how do we program intelligent behavior?-a substitution that the Transformer era made invisible by achieving unprecedented performance on its own terms. We then describe an alternative grounded in the FNC Framework and the Free Energy Principle, instantiated as the Bisociation Engine: a cognitive architecture in which language generation is one module among many, specialist knowledge domains compete in a global workspace, and creativity is operationalized as bisociation-the productive collision of structurally separated frames of reference. Empirical comparison shows that the Engine's domainpair rankings are negatively correlated with those of a leading LLM (Spearman ρ =-0.25), confirming that the two systems optimize for structurally different properties. The destination the Dartmouth pioneers set in 1956-machines that think, not machines that describe thought-remains the right one. The path needs correcting.

---

## uid: `doi:10.2139/ssrn.6677949`

- title: Portfolio Selection Using Artificial Intelligence:From Genetic Algorithms to Deep Reinforcement Learning, Graph Neural Networks, and Large Language ModelsA Revised and Extended Framework
- authors: Mohamed Benbouziane, Abdelhadi Benghalem
- affiliations: not stated
- posted: 2026-04-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6677949
- keyword hits: large language model, large language models, llm, llms

### abstract

More than a decade has passed since the genetic algorithm was first applied to the portfolio selection problem in Sefiane and Benbouziane (2012). That paper showed that arithmetic crossover could reliably identify efficient weight allocations in a constrained multi-objective setting. Much has changed since then. This paper revisits that earlier work not to replace it, but to situate it within the far richer methodological landscape that artificial intelligence now offers to quantitative finance. Three modern paradigms are integrated — deep reinforcement learning (DRL), graph neural networks (GNN), and large language models (LLMs) — alongside the original genetic algorithm (GA) framework, and a unified Hybrid AI (HAI) architecture is proposed. Two empirical illustrations are developed: the original five-asset dataset retained for direct comparability, and a ten-asset BRICS-inspired stylized portfolio spanning 2015 to 2024, calibrated to reflect elevated volatility, contagion dynamics, and regime breaks characteristic of emerging market investing. Seven figures accompany the analysis. Results confirm that GA-arithmetic crossover remains a strong interpretable baseline, while HAI dominates all benchmarks, improving the Sharpe ratio by 31 percent over GA on the original dataset and by 23 percent on the BRICS universe. The paper concludes with a targeted research agenda for the Algerian and MENA context, covering Arabic-language LLMs for regional financial sentiment, oil-price regime DRL, and Maghreb cross-border GNN construction.

---

## uid: `doi:10.2139/ssrn.6687198`

- title: The Blind Spot of the Twin Transition: Regulating the Environmental Footprint Of Large Language Models in the UK and EU
- authors: Syed Shaharyar Ahmed
- affiliations: not stated
- posted: 2026-05-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6687198
- keyword hits: generative ai, large language model, large language models, llm, llms

### abstract

The European Union and the United Kingdom are simultaneously pursuing a Twin Transition towards digital transformation and climate neutrality, predicated on the assumption that these goals are synergistic. However, the exponential rise of Large Language Models (LLMs) exposes a critical tension in this narrative: the massive energy, water, and carbon demands of compute threaten to undermine net-zero targets. This article provides a comparative doctrinal analysis of the emerging regulatory landscapes, specifically juxtaposing the EU's AI Act and Ecodesign frameworks against the UK's proinnovation White Paper approach and Environment Act 2021. It argues that a regulatory blind spot persists in both jurisdictions. Traditional environmental law remains fixated on physical industrial pollution, while nascent digital regulation prioritizes safety, bias, and privacy over sustainability. Consequently, the material environmental footprint of generative AI remains largely externalized. The article concludes that current procedural transparency mandates are insufficient to mitigate this growing impact. To resolve the Twin Transition paradox, legal frameworks must evolve to substantively integrate compute intensity into Environmental Impact Assessments and public procurement standards, treating digital infrastructure as a critical resource challenge rather than a purely virtual service.

---
