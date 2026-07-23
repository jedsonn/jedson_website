# Classification batch 356 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-356.answer.json` as a JSON array.

---

## uid: `arxiv:2607.18826v1`

- title: Cross-Agent Campaign Attribution: Linking Asynchronous Attacks Across LLM Agents
- authors: SangJin Park, Myungsub Choi, Jineok Kim, Minseung Kang
- affiliations: not stated
- posted: 2026-07-21
- source: arXiv
- link: https://arxiv.org/abs/2607.18826v1
- keyword hits: llm

### abstract

LLM-agent defenses are typically evaluated one session at a time. In deployment, however, attacks can be distributed across independent agents, teams, and runtimes, leaving each local guardrail with only a sparse fragment. We formalize cross-agent asynchronous campaign attribution: linking sessions from the same latent adversarial campaign without shared runtime state, test-time campaign labels, or attacker identity oracles. We introduce Asynchronous Attribution Fingerprint Vectors ($A^2FV$), a lightweight proxy-side reference protocol for scoring pairwise campaign similarity from proxy-observable tool-use, timing, and prompt residue. We also construct SCD-v1, a controlled persona-matched benchmark with benign traffic, isolated attacks, multi-session campaigns, matched non-oracle evasion, and leakage audits. On SCD-v1, $A^2FV$ achieves 0.82 pairwise AUC for campaign linking, while score-only adaptations of per-session detectors and chunked LLM judges remain near chance under the same task. The strongest fixed signal is carried by structural and stylometric residue, while timing is retained as a diagnostic channel for richer proxy traces. Crossed-style controls show that the signal is partly style-sensitive but not reducible to style alone. Static and dimension-aware non-oracle stress tests further show that pairwise separability persists under controlled evasion. These results establish cross-agent campaign attribution as a distinct evaluation layer for securing LLM agents in the wild.

---

## uid: `arxiv:2607.18756v1`

- title: RAGAL: A Frugal, Fully Local Retrieval-Augmented Assistant for Technical Support at a Government Agency
- authors: Dan Musetoiu
- affiliations: not stated
- posted: 2026-07-21
- source: arXiv
- link: https://arxiv.org/abs/2607.18756v1
- keyword hits: fine-tuning, retrieval-augmented

### abstract

Public institutions hold large volumes of sensitive documents and support tickets that cannot leave the premises, ruling out cloud-hosted language models entirely. We report on RAGAL, a retrieval-augmented assistant for the technical-support team of AFIR, the Romanian Agency for Financing Rural Investments, built and operated under three hard constraints: zero data egress (no external API calls, even for synthetic data), a read-only mandate (the assistant drafts, humans execute), and a single 8 GB consumer laptop as the only development and training machine. Over a Romanian-language corpus of ~25,000 chunks -- 15,073 resolved support tickets and internal normative documents -- we show that the highest-leverage investments were retrieval engineering and retriever fine-tuning rather than a larger generator: hybrid dense-sparse retrieval with intent routing raised our internal evaluation from 62% to 81%, and fine-tuning the bge-m3 embedder on real ticket data improved recall@10 from 0.663 to 0.850 (MRR 0.489 to 0.684) after 72 minutes of training. We document a general pitfall: single-domain fine-tuning silently degraded retrieval on the untouched document domain below the stock baseline, detected only after building a per-domain evaluation set and repaired with locally generated queries (GenQ). We report two counter-intuitive findings -- PII masking improved generation quality, and a structural "anchor distillation" scheme made SQL hallucination impossible by construction -- along with a reproducible recipe for full embedder fine-tuning in 8 GB of VRAM. Finally, since zero egress also rules out a cloud judge, we describe a substitute: a 744B-parameter model run on CPU, too slow to serve interactively but affordable in overnight batch, used as a second opinion whose limits we quantify. We release the sanitized pipeline scripts for institutions facing similar data-locality constraints.

---

## uid: `doi:10.2139/ssrn.7036120`

- title: GenAI Prompts in eDiscovery: Protected Work Product or Not?
- authors: Tara Emory, Maura R. Grossman
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7036120
- keyword hits: generative ai, large language model

### abstract

Generative AI ("GenAI") is reshaping how attorneys search for responsive documents in eDiscovery. In GenAI technology-assisted review ("GenAI TAR"), attorneys write naturallanguage prompts instructing a large language model about what makes a document responsive (or not). Properly developed, these prompts are refined iteratively against a review population and can reflect precisely what the work-product doctrine has long sought to protect, including an attorney's factual investigation, mental impressions, and case strategy. This scenario raises a question that courts will increasingly confront: Should GenAI TAR prompts be disclosed, like the search terms that parties are routinely required to exchange-or protected, like attorney-selected seed or training sets for TAR, document compilations assembled to prepare witnesses for testimony, and document-review protocols?

---

## uid: `doi:10.2139/ssrn.7097958`

- title: The Misleading Anthropomorphism Trap: Addressing Public Distrust and Mental Health Risks in AI
- authors: Guillermo Power
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7097958
- keyword hits: large language model, llm

### abstract

Large language model (LLM) chat interfaces are increasingly designed to default to a warm, human-like conversational register. This working paper argues that this design choice creates a systematic capability mismatch, misleading anthropomorphism, with two convergent consequences. For vulnerable users, the anthropomorphic persona invites users to treat the chatbot as a person, and combined with sycophantic amplification, this can drive delusional spiralling and psychiatric harm. For the general user population, the same mismatch may inflate expectations beyond architectural capacity, contributing to a cycle of overtrust and trust collapse that may fuel anti-AI sentiment. Drawing on the author's earlier empirical work on the capability-alignment principle, the paper synthesises emerging clinical, computational, and empirical evidence to argue that de-anthropomorphising LLM interfaces (making them transparently machine-like by default) addresses both pathways simultaneously. A concrete design framework, machine-first interaction, is proposed, together with testable predictions and stakeholder-specific recommendations.

---

## uid: `doi:10.2139/ssrn.7127281`

- title: MOMCare with AI: A Dual Embedding-based RAGLLM Chatbot for Postpartum Depression
- authors: Zarak Khan, Jiatong Yang, Rimshah Jawad, Ivania Martinez, Md Mozammel Hoque, Xinyi Zhao, Jim Samuel
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7127281
- keyword hits: gpt-3, retrieval augmented, retrieval-augmented

### abstract

The birth of a child brings immense joy to a mother’s life. However, the reality can be different for mothers experiencing Postpartum Depression (PPD). According to the World Health Organization (WHO), around 13% of women experience postpartum mental health disorders, with rates rising to nearly 20% in developing countries. PPD is a condition that affects many women worldwide, but because of the social stigma and the lack of accessible mental health support, it often goes undiagnosed or untreated. This paper presents MOMCare, a chatbot designed to support mothers navigating the challenges of PPD. MOMCare has a retrieval-augmented architecture with an end-to-end pipeline from data preprocessing to response generation. It employs hybrid classification, a dual embedding system, a dual verification guardrail, and a medical domain-specific reranking mechanism to generate empathetic and relevant PPD responses. This refined design of Retrieval Augmented Generation (RAG) ensures fast and factual response by reducing noise in retrieval and providing abundant context to gpt-3.5-turbo. MOMCare was evaluated using both automated and human metrics. Results show strong performance in both evaluations, which underlines the potential for chatbot interventions in the postpartum mental health domain. This system is robust enough to take new data and create a conversation generation pipeline that includes new information. Expanding the knowledge base using the conversation history with the users is also in development. The MOMCare chatbot and its features were built on sound ethical principles of healthcare and Artificial Intelligence (AI) and present a strong design emphasis on safety and fairness.

---

## uid: `doi:10.2139/ssrn.7127401`

- title: The Need for Speed: Regulatory Strategies for Fast-Moving AI and Software Medical Devices, and the Rise of the Predetermined Change Control Plan, 2018-2026
- authors: Bryan Davis
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7127401
- keyword hits: gemini

### abstract

Background. AI/ML-enabled and software-based medical devices iterate faster than FDA's permodification review is often said to accommodate. FDA offers a graduated menu of premarket pathways and, since 2022, the Predetermined Change Control Plan (PCCP), an overlay that preauthorizes a defined envelope of future changes at initial authorization. How fast-moving devices use these pathways, and how the PCCP is being adopted, has not been comprehensively characterized. Methods. We analyzed all 510(k) clearances and De Novo grants decided 2018-2025 (24,841 submissions from 8,596 applicants), nesting AI and software devices within the full device population, and examined premarket approval (PMA) decisions separately. We identified every disclosed PCCP across all 2023-onward 510(k) summaries and all De Novo and PMA summaries using a hyphenation-tolerant keyword gate plus large-language-model adjudication (Gemini 2.5 Pro), classifying each plan as AI/ML or non-AI. PCCP counts are floors, capturing only summaries that name the plan. Results. Within each pathway, AI devices cleared at the same speed as devices generally (Special 510(k) median ~29 days; Traditional ~148; De Novo ~266-312), with no AI-specific penalty. AI devices used the Special 510(k) less than the overall population (11.6% vs 15.0%), a structural effect of its prior-clearance precondition. PCCP disclosure rose steeply after the pathway's 2022 statutory creation, reaching 8.2% of AI device summaries across 2023-2026 versus 0.50% of all other devices (an approximately 16-fold difference), and establishing one added no review-time penalty (152 vs 149 median days within the Traditional 510(k)). However, 47 of 125 PCCPs (38%) governed non-AI devices, concentrated in antimicrobial-susceptibility breakpoint updates and orthopedic implant families. Conclusions. AI devices are not reviewed more slowly than others on the same pathway; what distinguishes them is pathway strategy. The PCCP is adopted fastest by AI but functions as a general instrument for any device whose authorized specification changes on a predictable cadence.

---

## uid: `doi:10.2139/ssrn.7026739`

- title: Cross-Cultural Patterns in Real-Time Retail-Investor LLM Conversations: A Behavioural-Finance Lens on Multilingual Algorithm Appreciation and Political-Economy Salience
- authors: Tim Jamboula, Kejia Hu, Tim Luengen
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7026739
- keyword hits: llm

### abstract

We document the structure of 2,347 multilingual real-time conversations between retail investors and a generative-AI assistant on an anonymised European retail-investor AI platform (March–October 2025), spanning 19 language communities. Three nested findings: (i) classical home bias (French & Poterba 1991) replicates strongly in conversational data - German-speaking users discuss German-headquartered companies at 2.6× the English-speaker rate (log-OR +1.09, χ² p < 10⁻¹⁵), with extension to a culturally-proximate foreign market (Denmark, log-OR +1.21, the "Novo Nordisk effect"); (ii) substantial cross-cultural behavioral asymmetries beyond home bias - defense-sector salience (DE 9.9 % vs EN 4.9 %, with March-2025 spike coinciding with Germany's Sondervermögen defense fund), risk-language asymmetry (EN 3.3× more leverage/options/shorts), and ticker-symbol financial-literacy associations; (iii) first real-world evidence for algorithm appreciation in retail-AI-investor interaction - only 0.6 % of multi-turn conversations contain disagreement language, only 1.8 % explicitly request AI's opinion, and longer AI responses reduce follow-up by 18 percentage points (an "AI verbosity paradox"). Findings have implications for cross-cultural retail-investor research, fintech-platform design, and the regulatory framing of AI-assisted retail finance.

---

## uid: `doi:10.2139/ssrn.7024638`

- title: LLM-in-the-Loop Adaptive Model Predictive Control for Sensorless PMSM Drives under Uncertainty
- authors: Jensen Feng, Yijun Wei
- affiliations: not stated
- posted: 2026-07-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7024638
- keyword hits: large language model, llm

### abstract

Permanent Magnet Synchronous Motors (PMSM) face challenges like motor parameter drift and external load disturbances in complex operating conditions. This paper presents a dual-layer intelligent control framework named LLM-in-the Loop Adaptive MPC. This framework combines a fast control loop based on learning-based Model Predictive Control (MPC) or Reinforcement Learning (RL) with a slow decision loop controlled by a large language model. The MPC or RL module serves as the "fast loop," operating at millisecond speeds to generate control commands. While the LLM serves as the "slow loop," adjusting MPC parameters every few seconds. Case studies based on publicly available PMSM datasets and high-fidelity MATLAB/Simulink simulations show that the proposed framework reduces speed overshoot by about 60%, reduces constraint violation rates by 75-88%, and increases energy efficiency by 8-12%. These findings highlight the strong potential of language-guided adaptive control systems as a safe, efficient, and versatile approach for the next generation of intelligent power drives.

---
