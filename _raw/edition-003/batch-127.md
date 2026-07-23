# Classification batch 127 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-127.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7108778`

- title: AI Premium
- authors: Nicola Borri, Aleh Tsyvinski, Yukun Liu
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7108778
- keyword hits: agentic, large language model, large language models

### abstract

Using 380 trillion tokens of realized AI consumption across more than four hundred large language models from the licensed proprietary OpenRouter dataset covering approximately 2 percent of current global monthly AI token consumption, we analyze how AI affects firms, markets, and workers. Leveraging the unprecedented size, scope and granularity of this data, we construct the AI Factor from growth in tokens, dollars, and users, estimate firm-level AI Betas from stock return comovement, and characterize the AI Premium. First, we build a high-frequency AI factor and decompose it into salient components. Second, we show that firms whose returns covary more positively with the AI factor—high AI beta firms—earn higher subsequent returns, and the AI premium is large and heterogeneous. A value-weighted longshort strategy earns 64.1 basis points per week, and the premium is large for loadings on the intensive, frontier-oriented margin of AI consumption—closed-source models, paying and seasoned users, and long prompts—but not on casual or open-weight use. Third, the premium reaches beyond technology firms into consumer-facing and capital-heavy parts of the economy, but is absent in emerging markets, including China. Fourth, the AI exposure is more positive in nonroutine interactive work and more negative in analytical, scientific, and operations-control skills—an occupation one standard deviation higher in interaction-and-communication content has 0.36-standard-deviation higher market-implied AI exposure. Additionally, we provide early evidence of the rise of the agentic economy. Institutional subscribers to the NBER working paper series, and residents of developing countries may download this paper without additional charge at www.nber.org .

---

## uid: `doi:10.2139/ssrn.7117519`

- title: DeFiSent: Check-Guided Repair for Financial-Semantic\\ Vulnerabilities in DeFi Smart Contracts
- authors: Yinhao Xiao, Chih-Chung Liu, Mingshu Cong, Le Yang
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7117519
- keyword hits: deepseek, llm, prompting

### abstract

DeFi smart-contract vulnerabilities often arise from protocol-level financial semantics rather than syntactic Solidity patterns. Direct LLM prompting can generate plausible patches that compile but leave oracle, vault, lending, or AMM invariants unresolved. We aim to make LLM-based smart-contract repair more reliable by separating patch generation from domain-specific judgment and requiring accepted patches to improve check-visible semantic obligations. We present DeFiSent, a check-guided repair framework. It normalizes contract code, infers protocol roles, routes vulnerability-family checks, emits structured findings and violated invariants, and prompts an LLM with this evidence. Candidate patches are accepted only after compilation, tests, interface preservation, non-increasing semantic severity, and invariant-specific gates. We evaluate DeFiSent on a coverage-aware corpus from DeFiHackLabs, EVMbench, LISA-Bench, SmartBugs Curated, and BCCC-SCsVuls-2024. The DeepSeek campaign contains 40,452 paired tasks and 80,904 model-mode runs, including a 41,332-row code-level shard. On the unified 6,000-task DeepSeek subset, check guidance improves dynamic pass rate from 54.82\% to 79.95\%, semantic-improvement rate from 40.42\% to 53.92\%, and total severity reduction from 8,733 to 24,084. On a 2,000-task SiliconFlow matrix, aggregate semantic-improvement rate increases from 27.0\% to 57.8\%. Structured findings and gate-based validation substantially improve LLM repair behavior for DeFi contracts. DeFiSent does not replace expert auditing, but it provides a reproducible path for aligning LLM-generated patches with financial-semantic proof obligations.

---

## uid: `doi:10.2139/ssrn.6968139`

- title: Human Capital, AI, and Labor Commoditization
- authors: Auyon Siddiq, Niuniu Zhang
- affiliations: not stated
- posted: 2026-07-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6968139
- keyword hits: chatgpt, generative ai, text embedding

### abstract

Has generative AI changed how labor markets value human capital? We study this question using data from Upwork, a large online labor market. Representing worker profiles with high-dimensional text embeddings, we compute the importance of human capital information and price in predicting labor demand, and incorporate these measures into a difference-in-differences design around the release of ChatGPT. We find that in more AI-exposed job categories, the importance of human capital declines and the importance of price rises, suggesting a commoditization effect of AI on labor. Two additional findings support commoditization as a mechanism: The demand premium enjoyed by workers with strong human capital declines in more AI-exposed categories, and demand reallocates toward lower-priced workers. Our results have implications for the design of online labor markets, workers' incentives to invest in human capital, and labor welfare.

---

## uid: `doi:10.2139/ssrn.7125062`

- title: SustainFed-LLM+: Carbon-Budgeted Renewable-Energy-Aware Client Selection for Energy-Efficient Federated Fine-Tuning of Large Language Models
- authors: Sunbal Iftikhar, Hassan Khan, John Breslin, Steven Davy
- affiliations: not stated
- posted: 2026-07-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7125062
- keyword hits: fine-tuning, large language model, large language models, llm

### abstract

Federated learning (FL) enables collaborative model training without centralizing data, but federated large language model (LLM) fine-tuning can amplify energy use, communication overhead, and carbon emissions when client participation ignores regional electricity conditions and device heterogeneity. Parameter-efficient fine-tuning, particularly low-rank adaptation (LoRA), reduces update size but does not determine which clients should train as renewable availability and carbon intensity vary across time and geography. This paper presents SustainFed LLM+, a carbon-budgeted extension of SustainFed-LLM. Whereas SustainFed-LLM performs fixed-size renewable-aware ranking, SustainFed-LLM+ reformulates client selection as carbon-budgeted variable client participation in which a Q-learning controller selects a per-round carbon budget, and a scheduler selects a variable-size cohort whose predicted emissions fit that budget under a carbon shadow price, an adaptive utility score, and a fairness-debt term. We evaluate SustainFed-LLM+ with LoRA-based fine-tuning across T5, OPT, GPT-2, and RoBERTa under non-IID partitions and trace-driven heterogeneity. Relative to SustainFed-LLM, SustainFed-LLM+ lowers carbon emissions by 12.6–14.3% and energy consumption by 5.6–9.2% while keeping ROUGE-L within ±0.004 of SustainFed-LLM (from −0.002 on GPT-2 to +0.004 on T5). Against random, loss-based, and cross-silo baselines it reduces emissions by 30.6–38.9%, 19.4–24.5%, and 68.0–89.1%, respectively, and reduces communication volume by 14.6–20.3% over SustainFed-LLM. It also lowers the participation Gini coefficient from 0.188 to 0.142, corresponding to a 24.5% fairness improvement among selective-participation strategies.

---

## uid: `doi:10.2139/ssrn.7060219`

- title: A Systematic Review of Agentic AI Frameworks: Architectures, Patterns, and Enterprise Applications
- authors: Malathi Marineni
- affiliations: not stated
- posted: 2026-07-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7060219
- keyword hits: agentic, large language model, large language models

### abstract

Background: Agentic AI frameworks-systems that enable large language models to reason, plan, invoke tools, and coordinate across multiple agents-have proliferated rapidly since 2022. The resulting literature, however, remains organized around isolated framework descriptions, obscuring the systematic design trade-offs that govern the field and leaving practitioners without a principled basis for framework selection. Objective: This review synthesizes the agentic AI framework literature to identify the crosscutting design dimensions that structure the field, characterize the trade-offs each dimension imposes, and map the resulting research gaps. Methodology: We systematically searched and screened papers published between 2022 and 2026, applying explicit inclusion criteria and a five-criterion, 10-point quality rubric (publication venue rigor, technical clarity, evaluation rigor, relevance to scope, and transparency of limitations) to admit both peer-reviewed publications and high-quality preprints meeting a ≥6/10 threshold. This process yielded a corpus of 114 retained papers, which we classified along five cross-cutting design dimensions-agent architecture, reasoning pattern, tool integration, memory management, and safety boundaries-derived iteratively from the extracted paper attributes. Key Findings: Safety boundaries do not appear to function as an independent design dimension; rather, the reviewed literature suggests they emerge as a downstream consequence of the other four: conservative, auditable systems in our corpus consistently combine single-pass inference with decision-support-only tool use, while expansive, autonomous systems combine iterative multi-agent reasoning with unrestricted tool invocation. Evaluation practice is correspondingly split between academic benchmarks optimized for cross-framework comparability and real-world case studies optimized for operational realism, with limited methodological transfer between the two traditions. Documented enterprise deployments cluster toward the conservative end of the autonomy spectrum, while research-oriented frameworks cluster toward the expansive end, with almost no documented middle ground; this pattern is based on a small number of enterprise case studies in the corpus and should be treated as an initial observation rather than an established trend. Contributions: This review contributes (1) a five-dimensional taxonomy for classifying agentic AI frameworks, grounded in patterns observed across the corpus; (2) a synthesis-driven comparative analysis identifying systematic trade-offs between architectural choices; (3) an evidence-based account of research gaps in evaluation standardization, enterprise deployment documentation, and graduated safety design, prioritized by tractability and dependency; and (4) practical guidance for framework selection based on task risk profile rather than capability alone.

---

## uid: `doi:10.2139/ssrn.7123579`

- title: Becoming an Agentic Enterprise: A Practitioner Methodology & Frameworks for Human-AI Governance
- authors: Bharath Yadla
- affiliations: not stated
- posted: 2026-07-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7123579
- keyword hits: agentic, large language model, large language models

### abstract

The transition from pilot projects to enterprise-scale autonomous AI systems represents one of the most significant governance challenges facing organizations today. While much attention has focused on the technical capabilities of large language models and agentic systems, comparatively little research has addressed the practical governance frameworks and methodology required to manage portfolios of agents at scale within an Enterprise. This creates a governance gap that keeps enterprises in long pilot cycles. For enterprises to confidently deploy, they need governing frameworks: Boards lack comprehensive frameworks to assess, classify, and oversee these increasingly sophisticated human-algorithm systems. Transformation leaders need a way to assess the human oversight required as agent complexity evolves. This paper introduces the “Becoming an Agentic Enterprise” methodology developed by the author (s) as a comprehensive practitioner framework, grounded in direct engagement with enterprise transformation initiatives. The methodology comprises four interlocking components: SCORE-AI for board-level governance assessment, the L1-L6 Agent Maturity Model for capability classification, the AURA framework for human oversight calibration & the extent of integration required with existing systems and processes, and the RRR transformation sequence for phased implementation. We illustrate the application of this integrated methodology through a detailed case study of an enterprise software company that uses this framework, resulting in a blueprint for ~100 agents across eight business domains spanning the spectrum of agent maturity. The paper contributes to the human-AI interaction literature by demonstrating how layered governance structures can maintain meaningful human oversight while enabling operational autonomy, and by providing a replicable blueprint for enterprise-scale agentic transformation. This paper introduces the “Becoming an Agentic Enterprise” methodology developed by the author (s) as a comprehensive practitioner framework, grounded in direct engagement with enterprise transformation initiatives. The methodology comprises four interlocking components: SCORE-AI for board-level governance assessment, the L1-L6 Agent Maturity Model for capability classification, the AURA framework for human oversight calibration & the extent of integration required with existing systems and processes, and the RRR transformation sequence for phased implementation. We illustrate the application of this integrated methodology through a detailed case study of an enterprise software company that uses this framework, resulting in a blueprint for ~100 agents across eight business domains spanning the spectrum of agent maturity. The paper contributes to the human-AI interaction literature by demonstrating how layered governance structures can maintain meaningful human oversight while enabling operational autonomy, and by providing a replicable blueprint for enterprise-scale agentic transformation. (2) Ethics: Embedding oversight through the SCORE-AI Ethics pillar and human oversight calibration at the agent level (3) AI Impact: Offering a practitioner-developed methodology for boards navigating AI governance.

---

## uid: `doi:10.2139/ssrn.7135124`

- title: ACORN: A Knowledge-Guided Hybrid Architecture for Resilient Last-Mile Logistics
- authors: Aneek Choudhury
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7135124
- keyword hits: agentic, large language model, mistral

### abstract

The application of Multi-Agent Reinforcement Learning (MARL) to industrial logistics is often limited by stochastic instability and the lack of operational interpretability. We present ACORN, a novel knowledge-guided neuro-symbolic architecture designed to enhance resilience in last-mile inventory control. Unlike "black-box" end-to-end models, ACORN implements a Cognitive Control Paradigm where a hierarchical Large Language Model (Mistral-7B) utilizes 15 explicit governance motifs to audit and refine agent actions before execution. Validated on the 9.16-million-record LaDe dataset, the system demonstrates 1.0 precision in constraint enforcement and maintains a 97.4% service level on held-out data, significantly outperforming traditional EOQ baselines (46.0%). These results confirm that integrating symbolic knowledge into agentic frameworks provides the operational robustness required for safety-critical supply chains.

---

## uid: `doi:10.2139/ssrn.6970398`

- title: The Agentic Regulator: Risks for AI in Finance and a Proposed Agent-based Framework for Governance
- authors: Eren Kurshan, Tucker Balch, David Byrd
- affiliations: not stated
- posted: 2026-07-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6970398
- keyword hits: agentic, large language model, large language models

### abstract

Generative and agentic artificial intelligence is entering financial markets faster than existing governance can adapt. Current modelrisk frameworks assume static, well-specified algorithms and onetime validations; large language models and multi-agent trading systems violate those assumptions by learning continuously, exchanging latent signals, and exhibiting emergent behavior. Drawing on complex adaptive systems theory, we model these technologies as decentralized ensembles whose risks propagate along multiple timescales. We then propose a modular governance architecture. The framework decomposes oversight into four layers of "regulatory blocks": (i) self-regulation modules embedded beside each model, (ii) firm-level governance blocks that aggregate local telemetry and enforce policy, (iii) regulator-hosted agents that monitor sector-wide indicators for collusive or destabilizing patterns, and (iv) independent audit blocks that supply third-party assurance. Eight design strategies enable the blocks to evolve as fast as the models they police. A case study on emergent spoofing in multiagent trading shows how the layered controls quarantine harmful behavior in real time while preserving innovation. The architecture remains compatible with today's model-risk rules yet closes critical observability and control gaps, providing a practical path toward resilient, adaptive AI governance in financial systems.

---
