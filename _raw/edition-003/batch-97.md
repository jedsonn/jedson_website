# Classification batch 97 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-97.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6869019`

- title: FinSupplyKG: Directed Knowledge Graph Traversal for Multi-Hop Supply Chain Contagion Analysis in SEC Filings
- authors: Naga Sai Anirudh Kodali, Faezeh Aghajani, Sri Surya Abhyuday Kodali
- affiliations: not stated
- posted: 2026-06-09
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6869019
- keyword hits: agentic, deepseek, llm, retrieval-augmented

### abstract

Supply chain analysis is a core task for equity analysts. When a disruption event affects one company, analysts need to determine which other firms in the network are exposed, how significant that exposure is, and whether the impact is positive or negative for each bystander. This requires tracing multi-hop dependency relationships across company filings. Standard retrieval-augmented generation (RAG) systems are poorly suited to this because cross-company dependency links rarely appear in a single retrievable passage. We present FinSupplyKG, a system that constructs a directed Knowledge Graph (KG) from SEC 10-K and 20-F filings for 13 semiconductor companies and uses it to identify and explain indirect supply chain exposures systematically. We build a 43-question adversarial benchmark covering 2-to 3-hop contagion scenarios and compare six systems, from a zero-shot LLM to our DCG-RAG (Directed Contagion Graph RAG). Across three independent runs judged by DeepSeek-R1, DCG-RAG (Tuned) scores 2.9x higher than the best agentic baseline. It does so using 77% fewer tokens. We also introduce a three-tier grading protocol combining automated judging, programmatic corpus verification, and human adjudication, which reveals systematic biases in LLM-based evaluation.

---

## uid: `doi:10.2139/ssrn.6910509`

- title: Creativity Is Not an Outcome: A Process-Based Framework for Mapping Individual Creative Contributions in Human–LLM Collaboration
- authors: Nishthaa Lekhi, Trevor Patten, Prakash Patil, Mengyao Li, Areen Alsaid
- affiliations: not stated
- posted: 2026-06-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6910509
- keyword hits: large language model, large language models, llm, llms

### abstract

If large language models (LLMs) are reshaping creative contributions in collaboration, the dominance of outcome-based creativity evaluation may obscure these changes by capturing only the final product. This makes it hard to determine whether LLMs support or displace human creative effort. To address this, we introduce a computational framework for tracking human creative contributions during live brainstorming dialogues. Using Observable Creative Sense-Making (OCSM), we operationalize participation, novelty, and appropriateness via computational semantic and linguistic measures evaluated against expert ratings. These enable turn-by-turn analysis of how contributions evolve, offering granularity that static benchmarks lack. In a between-subjects design, we compare creative behavior, subjective experience, and emotional trajectories of participants brainstorming with a human or an LLM. Results show LLM collaboration leads to greater idea divergence and exploration but lower participation and appropriateness. Human–human collaboration demonstrates stronger participation, contextual grounding, and cumulative idea development. Participants collaborating with an LLM also reported less positive experiences and lower confidence in collaborative outcomes. These findings reveal that different partners support different creativity dimensions - tradeoffs invisible to outcome-based assessments. By showing how creative contributions emerge and evolve, our framework helps identify where human creative effort is amplified, redistributed, or diminished. This visibility enables the design of conversational AI systems that strengthen human creative engagement instead of shifting effort away from human collaborators. More broadly, our framework provides a foundation for benchmarking creative contributions, identifying gaps in human–AI collaboration, and evaluating how AI technologies shape human creative potential over time.

---

## uid: `doi:10.2139/ssrn.6912480`

- title: Literature-Derived Knowledge Graphs Powered by Large Language Models for Mechanism-Informed Membrane Design
- authors: Meiqi Yang, Siyan Liu, Rabab Ward, Xiaoxiao Li, Menachem Elimelech
- affiliations: not stated
- posted: 2026-06-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6912480
- keyword hits: large language model, large language models, llm, llms

### abstract

Global challenges in water scarcity, environmental pollution, and industrial decarbonization demand faster materials innovation than conventional trial-and-error method. Membrane technologies are central to these solutions, enabling energy-efficient separations for water treatment, chemical recovery, and resource extraction. However, their data-driven design remains limited because critical synthesis–structure–performance knowledge is often embedded in unstructured literature rather than structured datasets. Here we present an automated and interpretable framework that integrates large language models (LLMs) with knowledge graphs (KGs) to unlock latent procedural knowledge. Using pervaporation membranes as a representative example, we construct Pervaporation KGs from 342 peer-reviewed articles, comprising 796 nodes and 282 relationships that encode synthesis, structure, and performance dependencies typically lost during manual curation. Combining graph-derived features with expert-curated descriptors improves prediction of separation factor and total flux. Shapley-based interpretation identifies synthesis parameters, including crosslinker ratio, drying temperature, and polymerization degree, as key performance drivers overlooked in standard datasets. Independent validation shows that model-identified high-impact features appear three times more frequently in emerging literature than low-impact features (P = 0.0001). We further develop an interactive web platform for real-time KG exploration and on-demand publication analysis, establishing a scalable paradigm for literature-driven materials discovery.

---

## uid: `doi:10.2139/ssrn.6834298`

- title: AIAS Presence Index v0.23: Premium Spirits Recognition Ceiling, Recall-driven Regime Classification, and the Conglomerate Ownership Hypothesis across 24 Brands and Six Large Language Models
- authors: Pablo Ulpiano Gonzalez Castro
- affiliations: not stated
- posted: 2026-06-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6834298
- keyword hits: large language model, large language models, llm, llms

### abstract

This paper reports AIAS Presence Index v0.23, measuring AI Presence for 24 premium spirits brands across six large language models under Protocol v1.6. Premium spirits is the seventh substrate family in the AIAS measurement program and the first to exhibit a universal recognition ceiling: all 144 Phase A probes return R3 (rich recognition), eliminating recognition variance from the composite entirely. The Presence distribu- tion is driven exclusively by Recall — which brands AI systems recommend, not which they can describe. Composite scores range from 40.0 (perfect recognition, zero recall) to 71.19, distributing evenly across four regimes (6 Dominant, 6 Established, 6 Emerging, 6 Absent). Six brands that LLMs characterize in expert detail — Bombay Sapphire, The Balvenie, Casamigos, Compass Box, Fernet-Branca, and Jameson — are never or rarely surfaced in recommendation contexts, exposing a recognition–recall gap invisible to tra- ditional brand-tracking methods. The substrate-specific hypothesis H_ConglomeratePortfolio is falsified: conglomerate-owned brands (n = 14) average 60.75 on the Presence composite versus 58.05 for indepen- dents (n = 10), a non-significant 4.6% lift (t = 0.59, p = 0.28). The two-channel recall architecture (editorial- authority, cultural-cult) yields an overlap coefficient of 0.80, the highest across seven substrates, indicating channel convergence in high-familiarity categories. Pre-registration, data, and scoring code are deposited at OSF (osf.io/ec6wh/v23/).

---

## uid: `doi:10.2139/ssrn.6908584`

- title: What LLM and 6.3 billion words tell us about sentiment?
- authors: Konpanas Dumrongwong, Suwongrat Papangkorn
- affiliations: not stated
- posted: 2026-06-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6908584
- keyword hits: large language model, llm, llms

### abstract

The study develops a novel sentiment index, called the Financial Optimism Index (FOI), alongside a finance-specialized large language model (LLM), named ModFinBERT. The model was trained on 6.3 billion words corpora to facilitate comprehension of the complex financial sentences contained in the news articles.The FOI is created by utilizing ModFinBERT on premier financial news outlets: Thomson Reuters, the Wall Street Journal, and the New York Times. ModFinBERT outperforms similar LLMs and dictionary-based techniques for sentiment extraction. Furthermore, consistent with behavioral finance literacy, the study discovered that FOI has a bidirectional relationship with stock index returns during non-COVID periods.

---

## uid: `doi:10.2139/ssrn.6837300`

- title: CogniGraph: Governed Graph-of-Agents Reasoning over Knowledge Graph Topologies with Semantic SHACL Validation and Constrained F1 Evaluation
- authors: Harish Kumar
- affiliations: not stated
- posted: 2026-06-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6837300
- keyword hits: claude, large language model, llm

### abstract

Multi-agent large language model (LLM) systems are increasingly deployed for regulatory and high-stakes reasoning, yet none of the prevailing flat-topology frameworks-AutoGen, CrewAI, LangGraph-enforce semantic governance over what each agent may say, in whose name, and within which scope. The result is what we term ungoverned creativity at scale: plausible-sounding answers that mix regulatory provisions, misattribute framework requirements, or drift beyond an agent's intended boundary. We ask: can a knowledge graph itself act as the coordination substrate of a multi-agent reasoning system, and can semantic validation gates supply the governance guarantees that the EU AI Act mandates? We present CogniGraph, a Graph-of-Agents framework in which each activated node of a domain knowledge graph hosts an autonomous LLM agent, communication follows the graph's typed edge topology via convergent message passing, and a SemanticSHACLGate enforces three-layer semantic validation-framework fidelity, scope boundary, and cross-reference integrity-on every agent output. A Prize-Collecting Steiner Tree (PCST) sub-graph activation step bounds per-query reasoning cost at O(|V * |•R) independently of |V |; a zero-inference-cost MasterObserver provides complete provenance traces; and the system is evaluated using a new joint quality-governance metric, Constrained F1. On MultiGov-30, a 30-question multi-regulation EU governance benchmark spanning the AI Act, GDPR, DORA, and NIS2, CogniGraph (Semantic-SHACL) achieves Constrained F1 of 0.756 against 0.328 for an ungoverned single-agent Claude Sonnet 4.6 baseline (+130%), with governance accuracy of 99.4% (framework fidelity 100%, scope adherence 100%, cross-reference integrity 98.3%). The transition from format-based to semantic SHACL validation independently lifted token F1 by 18% (0.437 → 0.517) by eliminating 49% false-rejection of correct answers. CogniGraph is distributed as the open-source GraQle SDK (pip install graqle, CLI graq); the MultiGov-30 benchmark, the SemanticSHACLGate specification, and the full reference implementation are released under Apache 2.0 to enable independent replication. 1

---

## uid: `doi:10.2139/ssrn.6906929`

- title: Capitalizing on Short-Term Rigidities: An ML Forecasting Solution for Small and Family Run Businesses
- authors: Aditya Mehta
- affiliations: not stated
- posted: 2026-06-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6906929
- keyword hits: large language model, llama, llm

### abstract

In markets across the globe, small and medium enterprises (SMEs) and family-run businesses are always playing catch-up to larger, more established firms with dominance in trust, pricing, distribution, and production. SMEs and family-run businesses need weapons that will level the playing field. In this paper, we propose a six-week Machine Learning (ML) and Large Language Model (LLM) based forecasting pipeline, with the aim of providing short-term opportunities for SMEs and family-run businesses to capitalize on the rigidity of larger corporations. Tested on the Dutch Tulip Sector from June 13th to July 24th, 2025, we forecasted industry-related consumer sentiment, macroeconomic time series, and ecological indicators with robust ML models like an Extreme Gradient-Boosting Regressor (XGBoost), a Long Short-Term Memory Neural Network (LSTM), and a Random Forest (RF) respectively, interpreting forecasts with Meta’s Llama 3 8B Instruct into an six-week action plan. Very promising quantitative results were produced, including testing Root Mean Square Errors (RMSEs) of ~7.3884 average humidity (%), ~1.5382 for average temperature (ºC), and ~1.4658 for PM2.5 air pollutant levels (µg/m3). The practical results demonstrate the effectiveness of ML forecasting with LLM interpretation for exploiting short-term windows, taking market share away from larger companies. These results are important because on-target predictions of consumer-sentiment, ecological, and macroeconomic shifts in the short-term reveal when larger corporations are to have pain points in their operations

---

## uid: `doi:10.2139/ssrn.6838543`

- title: Agentic Licensing for the Large Language Model Commons: MCP and NFT-Linked Rights Objects
- authors: Christos Makridis
- affiliations: not stated
- posted: 2026-06-11
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6838543
- keyword hits: agentic, ai agent, large language model, large language models

### abstract

Large language models have intensified a growing property-rights challenge in digital markets: protected works can be copied, retrieved, transformed, and recombined at low marginal cost, while ownership, licensing authority, attribution, and remuneration remain costly to verify. First, I introduce the Model Context Protocol (MCP) as an interoperability layer between AI agents and intellectual-property institutions. MCP does not define rights or settle disputes; it gives agents a standardized way to query registries, invoke licensing tools, execute payments, record usage, and preserve audit trails. Second, I develop a stylized transaction-cost model of agentic licensing and derive comparative statics for when lawful exchange expands. Lower search, verification, contracting, payment, and monitoring costs can move marginal uses from avoidance, substitution, or unauthorized use into licensed exchange, especially when rights records are reliable, license terms are standardized, and interface costs are large relative to the price of the license. Third, I explain how non-fungible tokens (NFTs) can complement MCP when they operate not as collectibles, but as machine-readable rights objects linked to work identifiers, ownership claims, license scope, payment rules, provenance records, audit obligations, and dispute forums. Music licensing is illustrative because rights are fragmented across compositions, recordings, labels, publishers, performers, territories, and use types. MCP and NFT-linked rights records can support ex ante licensing when paired with verified title, enforceable contracts, bounded delegation, human review, and off-chain legal remedies.

---
