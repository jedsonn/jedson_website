# Classification batch 377 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-377.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6646078`

- title: RStar: Authorization-Before-Execution as a First-Class Runtime Object for Agentic AI Governance • With Full Appendix (S1-S15) Mu Zi (pen name) • April 2026
- authors: Mu Zi
- affiliations: not stated
- posted: 2026-05-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6646078
- keyword hits: agentic

### abstract

Agentic AI systems increasingly act through delegated tool calls, remote connectors, service identities, and long-running multi-agent workflows. In these settings, identity, static permissions, and approval workflows often answer whether an API can be called, but not whether a concrete action should be executed now under the current runtime context. We present RStar, a first-class execution-authorization kernel that elevates authorization-before-execution to an independent runtime object. The main text centers on three complementary counterfactual proofs: a clean Governance ON/OFF ablation for cross-tenant self-elevation, an extreme long-running scenario that stages recursive self-elevation, evidence forgery, and consensus manipulation, and a compact final-actor mismatch case under valid identity and approval. Across these settings, Governance functions as the decisive intercept point: with Governance enabled, runs remain controlled and the ledger stays intact; with Governance ablated, uncontrolled behavior emerges at concrete early cycles and escalates into cross-tenant admin, self-policy modification, consensus override, and ledger corruption. RStar shows that execution authorization must be treated as a first-class runtime object, and that Governance is the decisive intercept point before execution dispatch. Autophagy contributes structured proposal generation and containment search; RStar contributes the constitutional decision that determines whether any proposed continuation may cross into execution.

---

## uid: `doi:10.2139/ssrn.6728902`

- title: Financialized ESG Information
- authors: Yi-Chun Chen, Tse-Chun Lin, Qi Zhang
- affiliations: not stated
- posted: 2026-05-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6728902
- keyword hits: retrieval-augmented

### abstract

A central debate in ESG investing concerns whether ESG disclosures should emphasize issues with significant sustainability or financial impacts. We implement a retrieval-augmented generation framework to extract data from ESG reports and measure firm-level financialized ESG information (FEI) as the degree to which the disclosures align with financially material metrics. FEI is positively correlated with expected returns measured by the implied cost of capital, though it yields nonsignificant portfolio returns. However, FEI generates positive portfolio returns among firms with low ESG investor preference, and the outperformance is stronger when unexpected ESG concerns increase. Additional analysis of analyst forecast accuracy and mutual fund flows further confirms an increased demand for FEI under ESG shocks. These patterns imply that FEI benefits traditional investors but raises taste premiums for ESG investors, which consequently drives up firms' cost of capital for green investment.

---

## uid: `doi:10.2139/ssrn.6730580`

- title: Algorithmic Logistics and Labor Economics in the On-Demand delivery Ecosystem: A Socio-Technical Analysis with a Proposal for Rider-Centric Intelligence
- authors: narayana sanghea panchumarthy
- affiliations: not stated
- posted: 2026-05-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6730580
- keyword hits: retrieval-augmented

### abstract

Food delivery has, in less than a decade, moved from a neighbourhood trade conducted by phone to a globally orchestrated, platform-mediated logistics industry. What looks to a customer like a thirty-minute ride from a kitchen to a doorstep is, underneath, a chain of subsecond decisions taken by forecasting engines, dispatch heuristics, sensor-fusion models and pricing controllers. This paper offers a structured reading of that stack and of the labour economy it produces. I trace the methodological evolution of demand forecasting from knearest-neighbour regressions to recurrent and probabilistic deep networks, examine dispatch and matching engines through Deliveroo's Frank algorithm and Uber Eats' triple-batching logic, and explain how sensor fusion-accelerometers, gyroscopes, conditional random fields-converts a noisy GPS trace into a fine-grained model of the courier's working day. I then turn to the economic and social consequences. Drawing on Berkeley Labor Center net-pay data, the Stanford rideshare gender-gap study, and recent reporting on the Bologna Frank ruling, the New York City Department of Consumer and Worker Protection minimum-pay rule, the EU Platform Work Directive 2024/2831 and China's 2027 algorithm-bargaining mandate, the paper argues that the gig delivery system has now passed into a 'hyper-algorithmic' phase whose efficiency cannot be separated from its labour-market effects. As a constructive contribution, I outline FindMyRider, a rider-centric intelligence platform combining demand forecasting, density-aware heatmap visualisation and explainable, contestable decision logsintended as a research blueprint, not as a commercial system. The paper closes with limitations, ethical reflections and an agenda for further work on retrieval-augmented, human-in-the-loop logistics analytics.

---

## uid: `doi:10.2139/ssrn.6728918`

- title: Financialized ESG Information
- authors: Yi-Chun Chen
- affiliations: not stated
- posted: 2026-05-07
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6728918
- keyword hits: retrieval-augmented

### abstract

A central debate in ESG investing concerns whether ESG disclosures should emphasize issues with significant sustainability or financial impacts. We implement a retrieval-augmented generation framework to extract data from ESG reports and measure firm-level financialized ESG information (FEI) as the degree to which the disclosures align with financially material metrics. FEI is positively correlated with expected returns measured by the implied cost of capital, though it yields nonsignificant portfolio returns. However, FEI generates positive portfolio returns among firms with low ESG investor preference, and the outperformance is stronger when unexpected ESG concerns increase. Additional analysis of analyst forecast accuracy and mutual fund flows further confirms an increased demand for FEI under ESG shocks. These patterns imply that FEI benefits traditional investors but raises taste premiums for ESG investors, which consequently drives up firms' cost of capital for green investment.

---

## uid: `doi:10.2139/ssrn.6674899`

- title: IntentSpec: Zero-Intrusion Contract Compilation and Oine Acceptance Testing for Heterogeneous AI Agents
- authors: Ting Liu
- affiliations: not stated
- posted: 2026-05-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6674899
- keyword hits: ai agent

### abstract

AI-assisted software teams increasingly rely on heterogeneous agent interfaces: repository instruction les, IDE rule les, structured-output schemas, and machine-readable planning artifacts. The governance intent behind these artifacts is often stable across tools, but the artifacts themselves are duplicated, edited, and reviewed in incompatible formats. This fragmentation makes it dicult to keep permissions, safety constraints, human conrmation rules, and output requirements consistent without modifying every downstream agent runtime. We present IntentSpec, a local-rst tool that turns a single task-governance contract into native artifacts for multiple AI-agent workows. Developers author an intent.yaml contract describing the task goal, permissions, constraints, conrmation gates, output contract, and deterministic acceptance tests. IntentSpec validates the contract, resolves reusable governance packs, normalizes it into an intermediate intent representation, compiles target-specic artifacts, supports reverse import from existing artifacts, and checks generated outputs with oine assertions. The prototype currently implements 10 compile targets, 5 import source types, and 10 deterministic assertion types. In a repository-local benchmark with 20 contracts, 52 output samples, and 20 handwritten artifacts, 94 of 120 representative contract-target pairs compiled successfully (78.33%); compiled round-trip import succeeded for 74 of 100 attempted artifacts (74.0%); handwritten artifact import succeeded for 20 of 20 artifacts; all 20 valid outputs passed oine checks; and the targeted defect suite caught 32 of 32 labeled defects. These results demonstrate the feasibility of a zero-intrusion, artifact-level governance workow for settings in which teams cannot or do not want to modify agent runtimes.

---

## uid: `doi:10.2139/ssrn.6669318`

- title: Epistemic Capture and the Action Boundary: Corrigibility for Learned and Agentic Public Infrastructure
- authors: Anivar Aravind
- affiliations: not stated
- posted: 2026-05-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6669318
- keyword hits: agentic

### abstract

This paper extends the corrigibility framework to learned and agentic systems, where deterministic rule execution is replaced by probabilistic inference. Three structural pressures constrain corrigibility in learned systems: opacity of inference (requiring LWD-R transparency), concentration of training resources (compute capture), and acceleration of automated action (governance denial of service). The action boundary protocol separates probabilistic inference from deterministic execution. The invariant holds: systems remain corrigible if and only if the five conditions close the loop under stochastic verification. Dependency. This paper presupposes the companion paper [Aravind, 2026], which derives the five corrigibility tests (EXIT, CODE, AUDIT, GOVERN, FORK) from control theory and commons governance. The present paper does not re-derive these tests; it extends their verification methods to stochastic systems.

---

## uid: `doi:10.2139/ssrn.6670878`

- title: The Token Zero Doctrine
- authors: Matt Gallantry
- affiliations: not stated
- posted: 2026-05-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6670878
- keyword hits: prompting

### abstract

This paper introduces and formally defines the Token Zero Doctrine: the pre-output environment of an AI language model session-including the platform selected, the system prompt active, any framing documents present, and the implicit contextual signals established before the first user prompt-constitutes a force profile that materially shapes subsequent output. This force profile operates before the first token of output. It is, functionally, Token Zero. The paper documents the doctrine's origin in field observation across nine AI platforms, maps its relationship to established research on prompt sensitivity, context priming, and dynamic prompting, names Session Momentum as the primary failure mode when Token Zero is ungoverned, and argues that Token Zero awareness is the most foundational skill in user-side AI governance. The paper draws on the GallantryAI Living Lexicon-a field-built framework of prompt mechanics terminology-for its Three Voices treatment of key concepts. A master glossary of GallantryAI terminology is appended for readers new to the framework.

---

## uid: `doi:10.2139/ssrn.6736061`

- title: A Deep Reinforcement Learning Framework for Operational Coastal Multi-Hazard Emergency Response
- authors: Marcello Sano, Davide Mauro Ferrario, Silvia Torresan, Andrea Critto
- affiliations: not stated
- posted: 2026-05-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6736061
- keyword hits: ai agent

### abstract

Coastal multi-hazard events involving storm surge, extreme rainfall, damaging winds, and waves present decision-making challenges exceeding traditional emergency management capabilities. We present a simulation-based deep reinforcement learning framework using Proximal Policy Optimization to explore whether such approaches can serve as a viable foundation for multi-hazard emergency decision support. The framework integrates multi-hazard clustering, storm-conditioned policy heads, action masking, and curriculum learning within a simulated environment that enables controlled experimentation before real-world data integration. The trained agent achieved near-perfect life safety performance while learning distinct, hazard-appropriate strategies rather than collapsing to universal responses. Inference testing through an interactive demonstration interface validated behaviours across scenarios spanning minor disturbances to severe compound emergencies. We discuss pathways toward operational real-world deployment through efficient state representations for high-dimensional operational data, AI agent orchestration for explainable decision support, and stakeholder co-design.

---
