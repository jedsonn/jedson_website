# Classification batch 329 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-329.answer.json` as a JSON array.

---

## uid: `arxiv:2607.01223v4`

- title: Theoria: Rewrite-Acceptability Verification over Informal Reasoning States
- authors: Michael Saldivar, Ben Slivinski
- affiliations: not stated
- posted: 2026-07-01
- source: arXiv
- link: https://arxiv.org/abs/2607.01223v4
- keyword hits: llm

### abstract

When should an AI system's answer be trusted? Formal proof assistants offer certainty but cannot reach most of the problem distribution; scalar LLM judges offer coverage but produce opaque scores that cannot be audited after the fact and are subject to the same coherence issues as any LLM. We present Theoria, a verification architecture that closes this gap. A candidate solution is rewritten into a sequence of typed state transitions, each licensed by an explicit justification, whether that be a citation, computation, or problem-given fact, and every transition is independently auditable. The foundational invariant is completeness of change: every difference between consecutive proof states must be accounted for, so hidden premises surface as unlicensed mutations rather than passing silently. On HLE-Verified Gold (185 text-only expert problems), Theoria certifies 105 at 91.4% strict precision (Wilson 95% CI [84.5%, 95.4%]). Every certification produces a human readable proof trace in which each step can be independently challenged. Holistic LLM judges achieve comparable precision at matched coverage but fail on different problems (Jaccard 0.14-0.36), making the approaches complementary. On 95 adversarial poisoned proofs across 15 domains, structured judges catch 94.7% versus 83.2% for holistic judging (p= 0.0017). The overall 11.5 pp gap concentrates in hidden premises (90.6% vs. 62.5%, a 28 pp difference) and fabricated citations (100% vs. 90%), the error classes where the formal analysis predicts an advantage; performance is identical on arithmetic and theorem-misapplication errors, where no advantage is predicted. On GPQA Diamond (n= 65), certified precision is 97.1% (Wilson CI [85.1%, 99.5%]).

---

## uid: `arxiv:2607.00692v1`

- title: Self-GC: Self-Governing Context for Long-Horizon LLM Agents
- authors: Xubin Hao, Hongjin Meng, Xin Yin, Jiawei Zhu, Chenpeng Cao
- affiliations: not stated
- posted: 2026-07-01
- source: arXiv
- link: https://arxiv.org/abs/2607.00692v1
- keyword hits: llm

### abstract

Long-horizon LLM agents accumulate tool results, files, plans, and user constraints that are too structured to be treated as a disposable text suffix. Current systems mostly rely on in-run heuristics such as chronological pruning and tool-output masking, or on final self-summary near a context limit. Heuristics are cheap but blind to future dependencies; summaries preserve narrative state but often hide exact evidence, locators, and editable artifacts. We present Self-GC, where GC denotes self-governing context while deliberately echoing garbage collection: the system does not merely reclaim unused tokens, but governs the lifecycle of agent context objects. Self-GC turns user turns, tool spans, and skill state into indexed objects; asks a side-channel planner to propose fold, mask, and prune actions; and lets the harness enforce recoverable sidecars, safe commit boundaries, and cache-aware commit. On a 33-session Hard Set, Self-GC prunes 43.95% of prefix tokens while leaving 84.85% of future continuations unaffected, compared with no-impact rates of 54.55% to 69.70% for heuristic baselines. On a 332-session production-derived suite, three planner backbones reach no-impact rates of 91.27% to 94.58%, while baselines remain at 77.71% to 87.46%. In production, an online account-level split reduces daytime average input tokens by 10% to 15%, with peak reductions near 20%. These results point to context management as runtime lifecycle control over indexed, recoverable objects rather than post hoc text cleanup.

---

## uid: `doi:10.2139/ssrn.7044188`

- title: Spatially Resolved Investigation into the Performance and Mechanisms of Preferential Weld Corrosion Mitigation in CO2-Saturated Acetic Acid Environments Using Structurally Tailored Gemini Surfactant Inhibitors
- authors: Mohd Sofi Numin, Khairulazhar Jumbri, Kok Eng Kee, Bob Varela, Mike Yongjun Tan
- affiliations: not stated
- posted: 2026-07-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7044188
- keyword hits: gemini

### abstract

Preferential weld corrosion (PWC) remains a critical threat to the integrity of pipelines in the oil and gas industry, particularly in aggressive CO2-saturated flowline environments containing organic acids. This study introduces an integrated approach to mitigate PWC on A333 carbon steel by synthesizing and applying three novel quaternary ammonium Gemini surfactant inhibitors with varying spacer groups: 2B-Benzene, 2B-Ether, and 2B-Ketone. The chemical structures were confirmed via FTIR and NMR spectroscopy, while the performance of these inhibitors in mitigating uniform and localised corrosion was investigated using a combination of conventional electrochemical tests (LPR and ZRA) and advanced local electrochemical techniques including the Wire-Beam Electrode (WBE) method that provide spatially resolved insights into localized anodic and cathodic electrochemical activities across the weld metal (WM), heat-affected zone (HAZ), and parent metal (PM). Results show that at temperatures up to 50 °C, all synthesized inhibitors effectively reduced self-corrosion rates. However, at an elevated temperature of 70 °C, only 2B-Ether maintained superior inhibition efficiency (>90%), significantly reducing the WM corrosion rate from 3.45 mm/yr to 0.50 mm/yr. This performance is attributed to the flexible ether spacer and stable Fe–O coordination, which facilitate strong surface anchoring even under thermal stress. Localized polarization analysis (LPA) using the WBE further elucidated the inhibition mechanisms at the most active micro regions. This work demonstrates that the rational molecular design of Gemini surfactants, coupled with localized electrochemical characterization, provides a robust framework for developing targeted corrosion mitigation strategies for heterogeneous welded structures.

---

## uid: `doi:10.2139/ssrn.7038559`

- title: Adabku: A Generative AI-Based Digital Children's Storybook with Character Personalization Features
- authors: Teguh Arie Sandy
- affiliations: not stated
- posted: 2026-07-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7038559
- keyword hits: generative ai, generative artificial intelligence

### abstract

The development of Generative Artificial Intelligence (GenAI) opens opportunities for producing more contextual children's learning media, yet photo-based visual personalization also introduces risks concerning privacy, content accuracy, and dependence on model outputs. This development study created Adabku: Magic Story as a digital children's storybook that integrates the generation of adab-themed narratives with character personalization based on children's photographs. The study employed an early-stage design-based research approach, encompassing needs analysis, architectural design, prototype development, expert validation, and revision planning. The product features three main workflows: character creation, theme and story source selection, and story presentation in flipbook format. The validation instrument comprised 25 items across the aspects of adab content, pedagogical narrative, GenAI personalization, interface, data security, and practical utility. Validation by two experts yielded feasibility scores of 93.6% and 94.4%, averaging 94.0%, with 96.0% exact agreement and a quadratic weighted kappa of 0.93. These results place the product in the highly feasible category with minor revisions. This design demonstrates that personalization should not be understood merely as an aesthetic feature. Rather, it must be anchored by validated knowledge bases, adult controls, restrictions on children's photo usage, and per-page story quality evaluation. The study's primary contribution lies in its GenAI-based adab story media development framework that treats pedagogical design, content traceability, and child protection as an integrated whole.

---

## uid: `doi:10.2139/ssrn.6987839`

- title: Artificial Intelligence, Private Tutoring, and Class Reproduction A Political-Economy Hypothesis and Evidence Map Using Korea as a Case
- authors: S. Jung
- affiliations: not stated
- posted: 2026-07-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6987839
- keyword hits: generative artificial intelligence

### abstract

South Korea (hereafter Korea) exhibits internationally very high private-tutoring (shadow-education) participation and spending while simultaneously recording one of the world's lowest fertility rates, so that its school-age population is contracting rapidly. In 2025 total private-tutoring spending, the participation rate, and weekly hours all declined, yet per-participating-student spending actually rose and the income-based spending gap persisted. The fall in the aggregate therefore cannot by itself be read as a structural easing of tutoring dependence or of class inequality. It is at this moment that generative artificial intelligence (AI) enters as an educational resource. The dominant policy narrative expects AI to lower tutoring dependence and dissolve gaps; this study argues against that expectation. Its claim is the following hypothesis: AI is a complement to existing educational capital, and its learning effect will be larger the larger the capital a household already holds (a positive interaction). High-capital households combine high-cost tutoring, higher-performing AI, and parental cultural capital and convert these into a larger learning effect, whereas low-capital households, even with access to the same cheapened AI, lack the complementary inputs to convert it, so that under a no-intervention condition the gap may widen. The study joins the political economy of AI-gain capture (Acemoglu–Restrepo, Korinek–Stiglitz) to the theory of educational reproduction (Bourdieu, Chetty) at the household and private-tutoring layer, and uses Korea — a country of internationally high tutoring participation/spending and a large income gap — as an extreme diagnostic case. Because panel statistics on AI use, spending, and learning outcomes by income decile are currently absent (though class differences in adolescents' generative-AI use experience are already observed — see §4), the joint claim is presented not as an established fact but as a falsifiable hypothesis, supported by theory and adjacent data, with explicit statement of what data would confirm or refute it. The claim is not deterministic — it states a pressure toward widening under the absence of policy intervention, not a physical necessity. In the policy analysis the study shows that AI policy can narrow the conversion gap but that its effect is bounded by three constraints — prior knowledge, teacher capacity, and household capital — and that the residual passes to the problem of distribution. Finally, the study directly concedes the strongest causal evidence that AI can compress gaps in short-term task performance (Noy–Zhang 2023; Brynjolfsson et al. 2025), while defending its hypothesis on the time horizon of long-run learning formation and conversion, and distinguishing itself from adjacent prior work at the level of analysis (household, private tutoring, intergenerational reproduction).

---

## uid: `doi:10.2139/ssrn.7044647`

- title: Navigating Generative AI in Academic Writing: Perceived Appropriateness and Ethical Use Among Indian PhD Scholars
- authors: Nitin Sharma
- affiliations: not stated
- posted: 2026-07-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7044647
- keyword hits: generative ai, generative artificial intelligence

### abstract

Purpose,The swift integration of Generative Artificial Intelligence (GenAI) has significantly changed academic writing practices, presenting both new opportunities and ethical dilemmas for English for Academic Purposes (EAP). Despite this transformation, there is a scarcity of empirical research on doctoral students' views regarding the suitability of GenAI at various stages of academic writing for publication. This study aims to explore how L2 PhD students (who use English as a second language for paper writing and publications) perceive the appropriate use of GenAI.,Methodology ,A sequential mixed-methods approach was utilized. Quantitative data were collected through a survey of 63 L2 PhD students from the arts, humanities, and social sciences at universities in Punjab, India. Qualitative data were collected through semi-structured interviews with 22 of the participants. The data were analyzed using descriptive statistics and thematic analysis.,Findings,The results indicate that doctoral students differentiate between acceptable and unacceptable applications of GenAI during various stages of academic writing. Participants generally found GenAI suitable for tasks like language editing, proofreading, and providing feedback. Still, they deemed its use for creating original arguments, interpreting literature without verification, or generating publishable content as inappropriate.,Originality,This research advances existing knowledge by going beyond general attitudes towards GenAI to scrutinize doctoral students' perceptions of appropriate AI utilization during the entire academic writing process. The proposed Perceived Scholarly Ownership Framework offers a fresh perspective on ethical AI-assisted writing and provides practical advice for EAP educators.

---

## uid: `doi:10.2139/ssrn.7039079`

- title: Human-in-the-Loop Multi-Objective Manufacturing Scheduling Optimization with LLM Agents
- authors: Wei Ye, Marvin Carl May, József Váncza, Xingyu Li
- affiliations: not stated
- posted: 2026-07-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7039079
- keyword hits: llm

### abstract

In manufacturing scheduling problems, such as Job Shop Scheduling (JSP), Flow Shop Scheduling (FSP), and Flexible Job Shop Scheduling (FJSP), a single optimal solution may be insufficient to capture the full production context, as it can oversimplify the problem by ignoring its multi-objective nature and lacking contextual adaptation. Human expertise plays a critical role in addressing this issue by identifying the gap between the optimal schedule and the actual production context. However, existing methods lack an effective mechanism for actively integrating human expertise into the optimization process. To address this gap, we propose the human-in-the-loop genetic algorithm (HiLGA), which integrates a two-layer, three-agent framework for multi-objective scheduling optimization. The first layer connects the human operator with the optimization core through two agents: an Interpreter agent which translates natural-language input into structured hint vector encodings, and an Explainer agent which evaluates the Pareto schedules returned by the optimization core and provides conversational support for schedule selection. The second layer serves as the optimization core, where a Generator agent integrates these hints into a genetic algorithm and produces Pareto-optimal schedules.Experiments across JSP, FSP, and FJSP evaluate each agent and agent coupling in sequence. The Generator agent alone achieves rapid convergence and attains 3-19% optimality gaps against the MILP benchmark across the tested configurations, confirming its viability as an evolutionary search operator. When the Interpreter agent is activated, HiLGA achieves 132% mean hypervolume improvement over combined baselines, with 51.7% of Pareto solutions achieving at least 80% preference alignment. Ablation against direct LLM scheduling baselines confirms that neither component alone is sufficient: direct LLM approaches fail in 40.1-43.7% of runs due to invalid or missing schedules, while GA-only search never reaches high-alignment regions, establishing the Interpreter-Generator coupling as the key driver of preference-aware Pareto solutions. The Explainer agent closes the human-in-the-loop cycle by decomposing each Pareto schedule's preference satisfaction into machine-selection, machine-avoidance, and operation-sequence components, allowing operators to query trade-offs and select schedules conversationally over verified optimization results. Overall, HiLGA establishes that natural-language human expertise can be represented as an optimization objective, optimized through Pareto search, and explained at the component level, enabling human workers to actively guide scheduling decisions rather than passively execute algorithmic outputs.

---

## uid: `doi:10.2139/ssrn.6910839`

- title: Identity Dilution in Multi-Hop MCP Architectures: A Dual-Attestation Chain for Verified Token Delegation
- authors: Kameswara Prasad Mukkamala
- affiliations: not stated
- posted: 2026-07-02
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6910839
- keyword hits: large language model, llm

### abstract

The Model Context Protocol (MCP) has been rapidly adopted as a standard transport layer connecting large language model (LLM) agents to external resource servers. As deployments shift from local stdio environments to remote web architectures secured by OAuth 2.1, a structural identity problem surfaces at multi-hop boundaries. When an MCP client delegates tool execution to an MCP server, which in turn calls a downstream resource API, neither the raw token passthrough pattern nor the opaque proxy pattern preserves end-user identity with verifiable integrity at the resource layer. This paper formalizes this gap as the Identity Dilution Problem and characterizes its two degenerate forms: the Passthrough Anti-Pattern, in which an unscoped upstream token transits an intermediary with full privilege, and the Confused Deputy Anti-Pattern, in which an agent proxy erases user identity entirely. We ground this formalization in the first systematic empirical measurement of 119 real-world remote MCP server deployments spanning four authentication lifecycle phases. We propose a Dual-Attestation Chain (DAC) architecture in which JSON-RPC tool-call payloads carry a cryptographically linked pair of signatures alongside an audience-bound, short-lived token derived from OAuth 2.1 Resource Indicators (RFC 8707). We further define a Context-Aware Scope Degradation rule that downgrades token privileges when the execution context contains untrusted input. Together these mechanisms allow any downstream resource server to verify user identity, agent scope, and invocation legitimacy without receiving or storing a raw upstream credential.

---
