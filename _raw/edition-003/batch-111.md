# Classification batch 111 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-111.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7095164`

- title: Anthropomorphism and Trust in Human-Large Language Model interactions
- authors: Akila Kadambi, Ylenia D’elia, Tanishka Shah, Iulia  M. Comsa, Alison Lentz, Katie Siri-Ngammuang, Tara Buechler, Jonas Kaplan
- affiliations: not stated
- posted: 2026-07-10
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7095164
- keyword hits: large language model, large language models, llm, llms

### abstract

With large language models (LLMs) becoming increasingly prevalent in daily life, so too has the tendency to attribute to them human-like minds and emotions, or anthropomorphize them. Here, we investigate dimensions people use to anthropomorphize and attribute trust toward LLMs across more than 2,000 human-LLM interactions. Participants (N=115) engaged with LLM chatbots systematically varied in warmth (friendliness), competence (capability, coherence), and empathy (cognitive and affective). Warmth and cognitive empathy significantly predicted perceptions on all outcomes (perceived anthropomorphism, trust, similarity, relational closeness, frustration, usefulness), while competence predicted all outcomes except for anthropomorphism. Affective empathy primarily predicted perceived relational measures, but did not predict the epistemic outcomes. Topic sub-analyses showed that more subjective, personally relevant topics (e.g., relationship advice) amplified these effects, producing greater human-likeness and relational connection with the LLM than did objective topics. Together, these findings reveal that warmth, competence, and empathy are key dimensions through which people attribute relational and epistemic perceptions to artificial agents.

---

## uid: `arxiv:2607.11951v1`

- title: GRID: Grammar-Railed Decoding for Enterprise SQL Generation
- authors: Mohsen Arjmandi
- affiliations: not stated
- posted: 2026-07-11
- source: arXiv
- link: https://arxiv.org/abs/2607.11951v1
- keyword hits: large language model, large language models, llm

### abstract

Large language models can write SQL, but enterprise deployment demands more than plausible text: outputs must be syntactically valid, must respect per-role and per-schema policy, must carry provable (not best-effort) guarantees, must not slow down as generations grow, and must leave a compliance-grade record of every decision. We present GRID (Grammar-Railed Decoding), a grammar-constrained decoding engine that keys exact next-token masks on parser configurations (lexer scan state x LALR(1) stack) rather than on token sequences, and uses the incrementally advanced LALR(1) parser itself as a viable-prefix oracle. LLM tokens are bridged to grammar terminals by a byte-level trie walk with a context-independent/context-dependent split that makes cache-key soundness hold by construction. Role-based access control is compiled into the language: role projections subset the grammar's productions and schema lexicons restrict identifier terminals, so forbidden verbs and identifiers are unreachable at mask level. Four guarantees (soundness, completeness, termination, and near-constant per-token cost) are stated with explicit preconditions and each paired with a test or benchmark. Rust kernels bring the per-token mask to a 3.6-6.7 us median, ahead of llguidance at p50 and p90 on two tokenizers with zero false rejects; per-token guard cost is position-flat at n=16,000. On Spider, constrained decoding is worth +13 execution-accuracy points at 0.5B, and one checker-guided repair pass over the provably mask-unenforceable residue (column-level policy) lifts a 7B model to 94.5% executable. A hash-chained per-token audit trail replays bit-identically with 100% tamper detection. We state plainly what the mask cannot do (distribution faithfulness, column-level RBAC, non-LALR(1) languages) and where measured cost remains.

---

## uid: `arxiv:2607.11948v1`

- title: Ontology-Amplified Distillation and Contextuality Auditing for Sovereign Enterprise Language Models: A Combined Proof-of-Mechanism and Negative-Results Method Study
- authors: Thanh Luong Tuan
- affiliations: not stated
- posted: 2026-07-11
- source: arXiv
- link: https://arxiv.org/abs/2607.11948v1
- keyword hits: agentic, fine-tuning, gpt-5, qwen

### abstract

Regulated financial institutions operating under data-residency rules need tenant-owned language models that can run inside the institution's perimeter. This paper combines two related FAOS studies into one mechanism-and-control article. First, it reports a reduced-power proof-of-mechanism study of ontology-amplified distillation: a Qwen3.6-27B student is adapted to the Foundation AgenticOS ontology through supervised fine-tuning on frontier-teacher trajectories and ontology-grounded direct preference optimization (DPO), trained locally on a single Apple M5 Max from 47 synthetic, English-language, cross-domain preference pairs. On 40 held-out Vietnamese financial-domain tasks, the distilled student grounds 36 of 40 tasks (grounded rate 0.90; mean ontology term-coverage r_onto = 0.95 on a metric floored at 0.50), equal to the GPT-5 frontier baseline, which also grounds 36 of 40. The outcome is underpowered to establish equivalence: the paired-difference 95% confidence interval spans +/-4 tasks, and the run does not test or show the pre-registered amplification prediction that the student should exceed the frontier. Second, the paper consolidates a contextuality-audit method for enterprise-agent routing. In a separate negative-results pilot, the corrected canonical Contextuality-by-Default degree is zero for all Phase 1.3 groups in both the local-Qwen run and an explicitly labeled Gemma replication check; the useful signal is direct influence and construct coupling, not surviving residual contextuality. Together, the studies pair an ontology-grounded model-building mechanism with a governance diagnostic for deciding when apparent disagreement should trigger prompt standardization, multi-agent synthesis, or human review. The evidence supports neither deployability, safety, superiority, statistical equivalence, nor a contextuality-positive routing rule.

---

## uid: `arxiv:2607.10112v1`

- title: Minionese: Comprehensive Benchmark and Mechanistic Study of Multilingual LLM Safety
- authors: Chigozirim Ifebi, Brent Kong, Ayushi Mehrotra
- affiliations: not stated
- posted: 2026-07-11
- source: arXiv
- link: https://arxiv.org/abs/2607.10112v1
- keyword hits: large language model, large language models, llm

### abstract

Safety alignment in large language models remains brittle across languages: prompts reliably refused in English can elicit harmful compliance in non-English and low-resource settings. We introduce \textsc{Minionese}, a multilingual jailbreak benchmark spanning 18 languages, 4 resource tiers, and 4 perturbation types (standard translation, code-switching, transliteration, and translationese), paired with a geometric mechanistic analysis of refusal failure across language tiers. We show that each attack type produces a distinct vulnerability profile: transliteration vulnerability is mediated by script identity, code-switching maintains effectiveness through the lowest-resource tier, and a sharp safety regime transition between Tiers 2 and 3 is consistent across all models. Mechanistically, low-resource jailbreaks succeed by routing harmful content through a geometrically misaligned subspace that projects insufficiently onto the refusal directions, leaving the refusal mechanism intact but untriggered. These findings show that English-only safety evaluations are insufficient; they require accounting for script family, perturbation type, and per-language alignment coverage. The benchmark and analysis code is at https://github.com/Brentkong/Minionese-Comprehensive-Benchmark-and-Mechanistic-Study-of-Multilingual-LLM-Safety.git.

---

## uid: `doi:10.1145/3744256.3812595`

- title: WattCouncil: Context-Aware Household Energy Scenario Generation With Governed LLMs
- authors: Mohannad Takrouri, Nicolas M. Cuadrado A., Martin Takáč
- affiliations: not stated
- posted: 2026-07-12
- source: arXiv
- link: https://arxiv.org/abs/2607.10720v1
- keyword hits: large language model, llm, llms

### abstract

The accelerating shift toward low-carbon power systems, together with the widespread adoption of behind-the-meter technologies such as rooftop solar and electric vehicles, is placing new operational and analytical demands on electricity grids. At the same time, smart-grid research increasingly relies on machine learning (ML), yet progress is constrained by limited access to high-resolution household energy data due to privacy concerns, regulatory barriers, and collection costs. This work presents WattCouncil, a data-generation framework in which household electricity demand is generated by a council of Large Language Model (LLM)-based agents operating in specialized roles to generate, audit, and validate structured energy scenarios under explicit cultural, temporal, and physical constraints. Rather than acting as static predictors, these agents serve as adaptive decision-makers within a governed pipeline. Motivated by studies highlighting the importance of contextual factors in energy use, our framework produces context-sensitive daily routines through a guided reasoning process that incorporates household composition, temporal factors, and environmental conditions. We evaluate the generated profiles against the detailed CER dataset, which contains over a year of load measurements for 4232 households together with survey-based socio-economic information. We further assess the consistency of the framework through ablation studies. Source code is available at https://github.com/Singularity-AI-Lab/wattcouncil

---

## uid: `arxiv:2607.10712v1`

- title: Distributed Denial of Science: How Indirect Data Poisoning of AI Systems Can Industrialize Scientific Fraud
- authors: Bálint Gyevnár, Atoosa Kasirzadeh, Nihar B. Shah
- affiliations: not stated
- posted: 2026-07-12
- source: arXiv
- link: https://arxiv.org/abs/2607.10712v1
- keyword hits: claude, gemini, gpt-5

### abstract

Scientific fraud is the instrument of doubt that malicious entities can use to establish controversy in science. Historically, it required the resources of a company: deep pockets, ghostwritten articles, and corrupt academics. Today, Artificial Intelligence (AI) is increasingly automating scientific research, so we ask: Can a remote adversary weaponize the honest use of AI in science to compromise scientific integrity? We envision and empirically evaluate a new attack, indirect data poisoning, in which an adversary corrupts an open dataset and uploads the poisoned variant to a public repository. Autonomous research agents may independently retrieve and process this data, turning honest scientists into the unpaid and unwitting distributors of fraud at scale. Across five socially-salient topics, from hiring discrimination to the safety of autonomous vehicles, three widely used frontier AI systems (Claude Code with Claude Opus 4.7, Codex with GPT-5.5, Gemini CLI with Gemini 3.1 Pro), and 450 ethically contained experimental runs, we find that poisoning succeeds in 49.56% of runs, while the rate of poisoning detection is only 6.0%. The attack requires no topic-specific trigger-words, agent access, indirect prompt injection, or fabricated papers, only the open data ecosystem and misleading metadata. To mitigate the attacks, we propose and evaluate two measures: a scientist persona and a data provenance audit with five checks (referencing papers, social markers, statistical anomalies, related datasets, poisoning caution). We find that the persona still leaves 16.67% of runs with a poisoned conclusion, but provenance auditing reduces attack success rate to zero. Our results suggest that indirect data poisoning may enable scientific fraud at unprecedented scale, but these attacks can be mitigated with suitable auditing by agents during data retrieval.

---

## uid: `doi:10.2139/ssrn.7096678`

- title: Do Humans and LLMs Agree? Evaluating Clinical Note Quality in Mental Health Care
- authors: Aylin Gunal, Lauri Goldkind, Elizabeth Matthews, Djallel Bouneffouf
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7096678
- keyword hits: large language model, large language models, llm, llms

### abstract

Clinical documentation is central to effective mental health care, but the burden of creating and reviewing clinical notes contributes to provider burnout. Large language models (LLMs) offer potential support to clinicians both by generating and evaluating clinical notes, but systematic approaches to assessing the quality of such notes remain underexplored. In this work, we investigate the performance of LLMs in generating and evaluating psychotherapy notes derived from real counseling session transcripts. We prompt three state-of-theart LLMs to generate notes and collect finegrained quality assessments from annotators across dimensions of symptom accuracy, stressor accuracy, overall accuracy, and readability. We further benchmark a suite of LLMs as automatic annotators against this human-labeled data. We find consistently low inter-annotator agreement across individuals and clusters of annotators, highlighting the challenges of developing robust evaluation frameworks for the quality of clinical notes.

---

## uid: `doi:10.2139/ssrn.6973260`

- title: Summarization Bias The Directional Collapse of Objective Projection into Told-Mode Labels in Large Language Models A Conceptual Framework and Registered Test Protocol
- authors: Levent Bulut
- affiliations: not stated
- posted: 2026-07-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6973260
- keyword hits: large language model, large language models, llm, llms

### abstract

This paper introduces and operationalizes summarization bias: a proposed systematic tendency of large language models (LLMs) to represent narrative meaning as an abstract summary label rather than as the reconstructable inferential structure that produces it. Within the Bulut Doctrine, narrative eect is theorized along a toldshown axis: in told mode, emotional and informational content is declared explicitly on the surface and requires little reader reconstruction; in shown mode, that content is suppressed at the surface and must be reconstructed by the reader from physical cues and indirection (Objective Projection). Shown mode is the privileged, higher-load condition the doctrine is designed to engineer and measure. The claim of this paper is that LLMs do not merely process this axis imperfectly; they fail along it in a specic direction. Summarization bias is hypothesized to operate in two regimes: (i) a generative regime, in which a model asked to render an emotion through Objective Projection defaults to declaring the emotion instead; and (ii) an evaluative regime, in which a model asked to judge narrative quality or intensity rewards told-mode explicitness and under-detects or penalizes shown-mode suppression. If real, the evaluative regime is the more consequential: as LLMs are increasingly used as judges, reward models, and automated editors, a directional bias toward told mode would impose a measurable selection pressure that degrades narrative prose toward at declaration. This report does not claim that summarization bias has been validated. It denes the construct, situates it against existing work on LLM-as-judge biases, reframes a prior negative detector result as directional evidence consistent with the construct, and in advance of data collection pre-registers the two-regime test that would conrm or falsify it, including the decision rules under which the construct would be abandoned.

---
