# Classification batch 420 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-420.answer.json` as a JSON array.

---

## uid: `arxiv:2607.17780v1`

- title: ETAS: An Effect-Typed Language for Agent Systems
- authors: Huiri Tan, Yikun Wang, Puyang Zhang, Shangyu Li, Jiasi Shen
- affiliations: not stated
- posted: 2026-07-20
- source: arXiv
- link: https://arxiv.org/abs/2607.17780v1
- keyword hits: agentic

### abstract

ETAS is a programming language for agent systems that treats model-backed agents, tool calls, prompts, typed memory, human approvals, policies, and execution traces as semantic program elements rather than library conventions. It separates deterministic computation from agentic nondeterminism and externally visible actions while preserving a direct programming style. We present the core design of ETAS. Its static semantics assigns ordinary types through spec conformance and tracks each computation with two behavioral indices: an escaping effect row and a persistent abstraction of the typed action trace it may request. Specs form a terminating compile-time constraint calculus: type specs provide evidence for polymorphism and resource facts, callable specs constrain function and stage shapes, and trace specs express allow, deny, and temporal constraints. Typing checks requested traces against compiled monitors and emits residual obligations when dynamic resources preclude a complete static proof. The dynamic semantics distinguish requested, handled, denied, and committed events; handlers interpret typed actions without making their requests invisible to authorization or audit. We formalize a core calculus and state preservation, progress, type/effect soundness, handler trace-transparency, and policy safety. We also implement ETAS in Rust with a command-line interface, typed HIR checks, effect and policy diagnostics, handler checks, and trace-aware execution hooks. ETAS provides a programming-language foundation for reasoning about authorization, nondeterminism, recovery, and audit evidence before and during agent execution.

---

## uid: `arxiv:2607.17598v1`

- title: Is Progressive Disclosure All You Need for Long-Context Agents?
- authors: Yifeng He, Yinzhe Zhao, Jicheng Wang, Hao Chen
- affiliations: not stated
- posted: 2026-07-20
- source: arXiv
- link: https://arxiv.org/abs/2607.17598v1
- keyword hits: agentic

### abstract

Long-document question answering usually forces a choice between loading the whole document into the context window and bolting on a separate retriever. Agentic AI suggests a broader option, giving the agent the document path and letting it decide how and what to read. Agent Skills, a standard for packaging expertise into folders an agent loads on demand, supply a ready mechanism: progressive disclosure, which exposes only what a query needs, from a short description down to the specific passages. Practitioners rapidly adopted this pattern for book-length understanding tasks, but the evidence to support such choices has been anecdotal. We run the first controlled study of the pattern, comparing raw-document navigation and several designs of Agent Skills packs against a classical hybrid retriever across three agent harnesses and three model families on InfiniteBench. On a single book, the gain depends on the harness, running large when the agent navigates the raw document poorly but near zero when a strong agent harness already divides and retrieves on its own. When scaling up to tasks that span many books, raw-document navigation collapses while one-level progressive disclosure degrades more slowly and pulls ahead. A second, deeper routing level never helps and sometimes breaks accuracy outright, so one level is enough. Progressive disclosure buys context, not intelligence: it is redundant while a strong agent can locate the right passages itself, and decisive once the corpus grows too large to navigate by reading.

---

## uid: `arxiv:2607.17447v1`

- title: Calibrating Semantic Uncertainty from Observable Language-Model Probabilities
- authors: Matthew F. Dixon
- affiliations: not stated
- posted: 2026-07-20
- source: arXiv
- link: https://arxiv.org/abs/2607.17447v1
- keyword hits: prompt engineering

### abstract

Language models produce probabilities over words, but professional decisions require uncertainty over meaningful states such as diagnoses, hypotheses or operational conditions. A model's printed numerical confidence does not establish reliability. We introduce a semantic map: a prespecified, testable bridge from probabilities over verbal responses to probabilities over declared states, formulated as semiparametric inference for a finite-valued latent state. A reference model defines the target posterior, the language model supplies an unrestricted conditional distribution over verbal responses, and held-out calibration connects them. We derive posterior-error bounds and conditions for existence, uniqueness, stability and sequential Bayesian updating. Crucially, language probabilities depend on the prompt's lexical form, whereas the target posterior is unchanged by information-equivalent rewording. We test the method on professional market text compiled from Federal Reserve economic and financial series and on controlled simulations with exact posteriors. Across two fitted language models, language-derived probabilities outperform printed numerical probabilities, recover held-out posteriors with valid uncertainty coverage, remain largely stable under paraphrasing, and respond appropriately to altered evidence. The broader implication is that prompt engineering optimizes a wording-dependent response, whereas scientific and professional use requires validated stability of application-relevant meaning. The semantic map turns this general concern into a testable statistical problem and, when its acceptance conditions hold, yields an auditable posterior estimate. The same principle offers a template for auditing classifications, recommendations and other fluent responses that may conceal semantic instability.

---

## uid: `doi:10.2139/ssrn.7155814`

- title: Benzo[5,6][1,4]dithiino[2,3-c][1,2,5]chalcogenadiazoles: synthesis and structural pecularities
- authors: Lidia  S. Konstantinova, Alexandra  S. Chechulina, Ekaterina  A. Knyazeva, Bin Kan, Yongsheng Chen, Rinat  R. Aysin, Oleg Rakitin
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7155814
- keyword hits: fine tuning

### abstract

A series of previously unknown fused benzodithiinochalcogenadiazoles, benzo[5,6][1,4]dithiino[2,3‑c][1,2,5]thia- and oxadiazoles, and its N-oxide, have been synthesized starting from readily available dichloroglyoxime via a key intermediate, benzo[b][1,4]dithiine-2,3‑dione dioxime. Benzo[5,6][1,4]dithiino[2,3-c][1,2,5]thiadiazole was successfully prepared using disulfur dichloride in DMF, while the corresponding [1,2,5]oxadiazole was unexpectedly obtained by dehydration of starting dioxime with selenium dioxide. Oxidation of benzo[b][1,4]dithiine-2,3‑dione dioxime with concentrated nitric acid gave the 1,2,5-oxadiazole N-oxide derivative. The molecular structures of all three compounds were unambiguously confirmed by single‑crystal X‑ray diffraction, which revealed a strong dependence of the molecular planarity on the nature of the chalcogenadiazole ring and the presence of the exocyclic N→O bond. DFT calculations using the EDDB method demonstrated that the compounds do not form a unified aromatic system. The thiadiazole ring shows the highest aromaticity, whereas the oxadiazole ring is only weakly aromatic. Electron affinity (EA) values, calculated at the DLPNO‑CCSD(T) level, are moderate for thia- and oxadiazoles, but increase substantially for 1,2,5-oxadiazole N-oxide, correlating with spin density localization in the corresponding anion radicals. These findings provide a basis for fine‑tuning the electronic and structural properties of benzodithiinochalcogenadiazoles by chalcogen variation, which may be of interest for the design of functional materials in optoelectronics and related fields.

---

## uid: `doi:10.2139/ssrn.7021838`

- title: The Trust Invariant: Toward a Cybernetic Architecture of Auditable Trust Across Interactional, Agentic, and Cryptographic Systems
- authors: Thomas Scillian
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7021838
- keyword hits: agentic

### abstract

As intelligence is distributed across human operators, autonomous agents, and cryptographic infrastructure, the recurring failure is not a failure of capability but a failure of trust: trust that is assumed rather than established, asserted rather than observed, and opaque rather than auditable. This paper proposes that trust, across otherwise unrelated domains, obeys a common invariant. In each domain, durable trust requires three properties-it must be established through an explicit process, observable as discrete events, and reconstructable after the fact-and where any of the three is absent, trust silently degrades. We frame this claim within Enterprise Cybernetic Intelligence (ECI), a cybernetic account of adaptive systems, and argue that the same trust invariant governs three layers that are usually studied in isolation: the interactional layer (how humans and AI systems maintain coherent collaboration), the agentic layer (how autonomous machine actors establish legitimacy and bounded access), and the cryptographic layer (how systems bootstrap quantumresistant trust during the post-quantum migration). We position a body of prior and concurrent work as instances of this single architecture and offer the invariant as an organizing frame and a research program, not a finished theory. The contribution is integrative: a vocabulary and a structure that connect interaction stability, agentic identity, and post-quantum trust as expressions of one cybernetic requirement.

---

## uid: `doi:10.2139/ssrn.7151169`

- title: Target-labelled adaptation of legacy raster floor plans for BEM preprocessing: source-separated evaluation and error propagation to EnergyPlus input skeletons
- authors: chunling wu, Shengqi Zhang, Jiye Li, Zhifeng Sun, Xiaofeng Li, Lingling Zhao, Zhichao Wang
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7151169
- keyword hits: fine-tuning

### abstract

Legacy floor plans often survive only as raster images, creating a preprocessing bottleneck for building energy modelling (BEM). We evaluate whether supervised fine-tuning with a small convenience-selected target set improves semantic segmentation across drawing families and audit how room-closure errors propagate into simplified EnergyPlus input skeletons. A ResNet34-U-Net trained on CubiCasa5K obtained 0.780 mIoU on 400 source test images but 0.270 on 200 zero-shot dark-background FloorPlanCAD tiles; the tested colour randomization and adaptive batch normalization did not close the gap. The target collection comprised 29 model-assisted, human-corrected masks from five uneven sources and 21 provenance-inferred building groups. Leave-one-source-out foreground mIoU increased from 0.026 ± 0.036 to 0.261 ± 0.118, but the gain was only 0.012 for the single screenshot-style source. In three seeded building-grouped re-evaluations, pooled foreground mIoU increased from 0.021 to 0.453 ± 0.014; the seed-averaged building-group gain was 0.436 (95% bootstrap CI, 0.367–0.496). Eight held-out prediction/comparator pairs entered the downstream audit. The IDFs used axis-aligned room rectangles, treated every wall as Outdoors, and contained no fenestration or inter-zone adjacency. One prediction produced no thermal zone; among seven usable pairs, median absolute deviations were 16.7% in conditioned area and 32.1% in annual ideal load. Separately written IFC2x3-labelled STEP outputs failed GUID, opening-scale, and relationship checks. These internally re-evaluated development data support adaptation within related drawing families and an error-propagation audit, not IFC exchange, calibrated energy prediction, labour saving, or automated BEM generation.

---

## uid: `doi:10.2139/ssrn.7017320`

- title: Deterministic Policy Enforcement for Healthcare RAG: A Runtime Control Pattern for Privacy, Access, and Auditability
- authors: Pradeep Chellappa Chockalingam
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7017320
- keyword hits: retrieval-augmented

### abstract

Background. Healthcare organizations are deploying retrieval-augmented generation (RAG) to surface knowledge from enterprise data across clinical, administrative, and operational functions. RAG systems introduce a class of runtime governance exposure that data-at-rest controls do not fully address: information is retrieved, assembled into context, embedded in prompts, transformed during generation, and surfaced in responses, with each stage creating distinct policy-conformance risks. In regulated healthcare environments, existing candidate enforcement mechanisms, including model alignment, prompt instructions, and post-hoc review, are structurally insufficient as the primary enforcement layer because they cannot produce perinteraction governance guarantees that are independent of probabilistic model behavior. Objective. This paper proposes a runtime control pattern for healthcare RAG that places deterministic policy enforcement in the orchestration layer surrounding the language model, external to the model and independent of its behavior. The pattern specifies how governance rules are operationalized at runtime across six deterministic gates aligned with the retrievalaugmented generation lifecycle. Key Messages. The paper introduces four contributions. First, a staged control fabric that organizes deterministic enforcement by gate, applying the lowest-cost control sufficient for the interaction's risk tier and escalating only when policy, sensitivity, or exception conditions require it. Second, a policy compilation principle that translates governance rules into executable artifacts before runtime, enabling each gate to enforce pre-approved policy decisions rather than interpret policy at runtime. Third, a six-gate runtime control pattern and associated runtime control matrix covering pre-retrieval, retrieval-time, context-assembly, prompt-construction, response-time, and post-response stages. Fourth, a failure-mode vocabulary naming enforcement leakage, boundary inversion, and verification gap as the primary architectural patterns that undermine deterministic enforcement. Conclusions. The contribution is conceptual-architectural. No empirical validation is presented. The pattern specifies a runtime enforcement layer for regulated healthcare RAG systems; runtime auditability, evidence logging, source traceability, and human attestation are treated in the next paper in this series.

---

## uid: `doi:10.2139/ssrn.7155813`

- title: Distinct omics signatures reveal functional stabilisation underlying biostimulant‐mediated drought resilience in grapevine
- authors: Iván Jauregui, Ariadna Iglesias-Sanchez, Dorra Fakhet, Angie  L. Gámez, Igor Florez-Sarasa, Diane Houdusse, Iker Aranjuelo
- affiliations: not stated
- posted: 2026-07-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7155813
- keyword hits: fine tuning

### abstract

Biostimulants are emerging as promising tools to enhance crop resilience under abiotic stress, yet their mechanisms of action in perennial species remain insufficiently characterized. This study evaluated the drought mitigating potential of two biostimulant treatments (protein hydrolysates alone and combined with seaweed; B1 and B2 respectively) applied to Vitis vinifera cv. Tempranillo under controlled greenhouse conditions. Water deficit markedly reduced foliar and stem biomass across all treatments, confirming the intrinsic sensitivity of structural growth during early vine establishment. However, growth limitation under drought contrasted with clear biostimulant‐induced improvements in physiological function. Biostimulant application significantly enhanced physiological performance, with treated plants displaying higher photosynthetic capacity and improved maintenance of photosynthesis under drought. The combined formulation conferred the strongest physiological resilience, suggesting synergistic effects among its bioactive components. Metabolomic analyses revealed targeted reconfiguration of primary metabolism under biostimulant application, including increased abundance of shikimate‐derived phenolics, osmoprotective sugars such as raffinose, and stress‐related amino acids, indicating enhanced metabolic flexibility and carbon reallocation under water limitation. In parallel, transcriptomic profiling showed that, although drought induced extensive gene expression reprogramming, biostimulant treatments under stress resulted in only limited additional differential gene expression. Nevertheless, pathway enrichment analyses identified consistent modulation of key adaptive networks, including photosynthesis‐related pathways, MAPK signalling and hormone signal transduction, indicating regulatory fine‐tuning rather than activation of novel transcriptional stress programmes. Together, these findings demonstrate that biostimulants (particularly multifunctional formulations) reinforce drought tolerance in grapevine by sustaining photosynthetic function and stabilizing metabolic and signaling pathways, offering valuable insights for climate adaptive viticulture.

---
