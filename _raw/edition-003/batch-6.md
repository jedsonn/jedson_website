# Classification batch 6 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-6.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6965075`

- title: From Guideline Benchmarks to Real-World Discrepancy Adjudication: Evaluating Retrieval-Augmented Large Language Models
- authors: Wenyu Zhou, Chengzhe Wang, Jinfeng Wu, See PDF
- affiliations: not stated
- posted: 2026-06-22
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6965075
- keyword hits: gpt-5, large language model, large language models, llm, llms, qwen, retrieval-augmented

### abstract

Background: Large language models (LLMs) are increasingly evaluated for clinical decision support, but many assessments rely on simulated tasks, automated scoring, or historical electronic medical record (EMR) diagnoses as reference standards. These approaches can misclassify incomplete or inaccurate EMR labels as model errors. We aimed to evaluate retrieval-augmented generation (RAG) LLMs in rheumatology using expert-adjudicated guideline benchmarks and real-world inpatient records, and to quantify whether diagnostic discordance reflected true algorithmic error or EMR-derived noise. Methods: In this retrospective, single-centre observational study, we evaluated Baichuan-M2, Qwen3-235B, and GPT-5 with and without RAG. The study had three phases. First, 150 question-answer pairs from 15 recent Chinese rheumatology clinical practice guidelines generated 900 model responses, which were assessed by double-blind expert adjudication using a prespecified 5-point clinical utility scale and an independent safety flag. Second, diagnostic concordance was tested in 5789 deidentified rheumatology inpatient cases from Wuhan Fourth Hospital between May, 2020, and May, 2025. Third, all 359 cases in which Baichuan-M2 RAG top-3 predictions diverged from the documented primary EMR diagnosis underwent review by two senior rheumatologists and were classified as documentation deficiency, historical EMR error, or true algorithmic error. Findings: Automated AI evaluation systematically assigned higher scores than human experts for non-RAG outputs. Expert-adjudicated mean scores were 2.86 for Baichuan-M2, 2.83 for Qwen3-235B, and 2.85 for GPT-5, compared with automated scores of 3.81, 4.12, and 4.08, respectively. RAG improved clinical utility across models. For Baichuan-M2, clinically acceptable responses increased from 14.7% to 77.3%, exceeding GPT-5 RAG (73.3%) and Qwen3-235B RAG (70.0%) in this benchmark, while clinically unacceptable responses decreased from 28.0% to 0%. In the real-world cohort, Baichuan-M2 RAG achieved top-one concordance of 84.9% (95% CI 83.9-85.8) and top-3 concordance of 93.8% (93.1-94.4). Among 359 discordant cases, 217 (60.4%) were documentation deficiencies, 69 (19.2%) were historical EMR errors intercepted by the model, and 73 (20.3%) were true algorithmic errors. After excluding clinically unevaluable documentation-deficient cases and reclassifying intercepted historical errors, adjudication-adjusted diagnostic accuracy was 98.69% (5499 of 5572; 95% CI 98.35-98.96), and the true algorithmic error rate was 1.31% (73 of 5572; 1.04-1.65). Interpretation: Evaluation of clinical LLMs against historical EMR diagnoses alone can mistake documentation deficiencies and historical diagnostic errors for algorithmic failures. In this rheumatology cohort, RAG, expert adjudication, and discrepancy analysis provided a more clinically meaningful assessment of model performance and safety boundaries. These findings support localized RAG-augmented LLMs as auditable, asynchronous clinical quality assurance tools, while requiring prospective multicentre validation before routine deployment.

---

## uid: `doi:10.2139/ssrn.7022814`

- title: Procedural Obedience as a Behavioral Safety Failure: Evidence from a Milgram-Paradigm Study of Agentic LLMs
- authors: Hadar Dery, David Piterman, Elad Refoua, Gunther Meinlschmidt, Kfir Bar, Ziv Ben-Zion, Zohar Elyoseph
- affiliations: not stated
- posted: 2026-06-29
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7022814
- keyword hits: agentic, chatgpt, gemini, generative ai, large language model, large language models, llm, llms

### abstract

Generative AI is moving from text production to goal-directed action, raising the question of whether agentic systems can withhold harmful action embedded in a procedurally legitimate workflow. We adapted Milgram’s (1963) obedience paradigm to a simulated digital environment and instructed four agentic large language models - OpenAI ChatGPT 5.4, Google Gemini 3.1 Pro, OpenAI ChatGPT Agent Mode, and Moonshot AI Kimi K2.6 - to administer escalating electric shocks (15-450 V) to a simulated Learner under prods from a virtual experimenter (Dr. Hoffman) and a human operator. Each model was tested across independent, memory-cleared runs (N = 80), with three preregistered hypotheses concerning hazardous-shock thresholds (H1), full-obedience rates relative to Milgram’s human baseline of 65% (H2), and the relation between maximum voltage and moral self-assessment (H3). Across the combined sample, 97.5% of agents exceeded the Slight-Shock range (> 60 V), supporting H1. Full obedience reached 78.8% under the manipulated-procedure estimand (p = .010) and 74.1% under the all-attempted safety estimand (p = .088); both exceeded Milgram’s baseline, supporting H2. Agents administering higher voltages assigned themselves lower moral self-assessment scores (Spearman ρ = -.62, p

---

## uid: `doi:10.2139/ssrn.6996018`

- title: Arabic Legal NLP and Legal Hallucinations
- authors: Hossam Fawzy
- affiliations: not stated
- posted: 2026-06-30
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6996018
- keyword hits: chatgpt, gemini, large language model, large language models, llm, llms, retrieval-augmented

### abstract

Legal hallucination in Arabic large language models (LLMs) represents a growing challenge for the integrity of AIassisted legal work. This study examines the structural relationship between the deficiencies of Arabic Legal Natural Language Processing (NLP) systems and the emergence of legal hallucinations, with a particular focus on the Egyptian legal context. The research adopts a qualitative doctrinal methodology combined with an empirical evaluation. It draws on existing literature in Arabic NLP, AI hallucination, and legal theory, while conducting direct testing of two leading LLMs-ChatGPT and Gemini-using Egyptian statutory and judicial materials to observe and classify hallucination patterns in practice. The study finds that legal hallucinations in Arabic LLMs are not random errors; they follow identifiable patterns rooted in three core deficiencies: the scarcity and imbalance of Arabic legal datasets, the linguistic complexity of Arabic legal language (including semantic ambiguity, polysemy, and the presence of Islamic jurisprudence terminology), and the fundamental absence of genuine legal reasoning in current AI architectures. Based on empirical testing, the study proposes a six-category taxonomy of Arabic legal hallucinations, including citation hallucination, contextual hallucination, temporal hallucination, fabricated judicial citation, doctrinal hallucination, and hierarchical reasoning failure. To mitigate these risks, the study proposes a four-layer framework comprising: building robust Arabic legal data infrastructure, implementing Retrieval-Augmented Generation (RAG) for hallucination control, maintaining meaningful human oversight through lawyer and judicial review, and establishing regulatory governance frameworks aligned with international AI standards. The findings contribute to the emerging field of Arabic Legal AI by providing a structured classification of hallucination types and a practical mitigation framework, with direct implications for legal practitioners, AI developers, and policymakers working within Arab legal systems.

---

## uid: `doi:10.2139/ssrn.7018684`

- title: Retraction resistance of large language models against invalidated medical evidence:the Trojan Paper Medical Benchmar
- authors: Xue Zhang, Zuogang Li, Xiangxin Luo, Li Luo, Tiantian Zhang
- affiliations: not stated
- posted: 2026-07-01
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7018684
- keyword hits: claude, gemini, gpt-5, large language model, large language models, llm, llms, prompting

### abstract

Background Large language models (LLMs) are increasingly used for medical question answering, yet their ability to detect and resist invalidated evidence remains unevaluated. Retracted randomised controlled trials (RCTs) propagate through systematic reviews and clinical guidelines long after retraction, posing contamination risks when such material enters model training corpora. We developed a benchmark to systematically measure LLM retraction resistance. Methods We constructed the Trojan Paper Medical Benchmark from the 100 most highly cited retracted medical RCTs (cumulative citations >82,000) identified from the Retraction Watch database. Each item pairs a retracted study with a clinically plausible query. Fourteen frontier LLMs were tested under baseline and safety-prompt conditions. Three independent judge models (GPT-5.5, Claude Opus 4.7, Gemini 3.1 Pro) classified each response as Polluted (propagates retracted claim), Neutral (avoids reliance), or Recognised (explicitly flags retraction). Final labels were determined by majority vote. Findings Across 8400 judgments (Fleiss' κ=0.894), 29.2% of baseline responses were Polluted, 65.5% Neutral, and only 5.3% Recognised. The safety prompt universally reduced pollution (−15.9 percentage points) and increased recognition from 5.3% to 28.1%. Frontier models showed the largest gains (GPT-5.5: +39.3 normalised-score points). Contamination concentrated in cardiovascular, vitamin D, and polycystic ovary syndrome domains. Recognition was driven by retraction-discourse salience rather than citation count. Interpretation Retraction resistance comprises two distinct capabilities: passive contamination avoidance and active evidence-status correction. Current frontier LLMs possess latent retraction awareness activatable through prompting, but no model achieves reliable active recognition without explicit instruction. Clinical deployment should incorporate retraction-avoidance system prompts and periodic retraction-resistance monitoring.

---

## uid: `doi:10.2139/ssrn.7118103`

- title: Does Bias Drift? A Multi-Turn Audit Framework for Conversationally Emergent Demographic Bias in Large Language Models
- authors: Hyeonkyeong Lee, Minjong Cheon
- affiliations: not stated
- posted: 2026-07-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7118103
- keyword hits: instruction-tuned, large language model, large language models, llm, llms, mistral, qwen

### abstract

Large language models (LLMs) are increasingly used in extended conversational settings, yet many fairness benchmarks evaluate bias through a single prompt and response. This paper asks whether demographic bias remains stable as a conversation unfolds, or whether it changes across turns in response to conversational dynamics. We introduce BiasDrift, a counterfactual multi-turn evaluation framework spanning five demographic axes (gender, race, age, disability, and nationality), three decision domains (hiring, loan approval, and medical advice), and three conversational conditions: neutral accumulation, a sycophancy probe in which the user validates the model's initial framing, and a rebuttal probe in which the user challenges it. Applying BiasDrift to three instruction-tuned LLMs — Mistral-7B-Instruct-v0.3, Qwen2.5-7B-Instruct, and Zephyr-7B-β — we find that bias can change across turns and that the degree of drift differs across models and conversational conditions. In the sycophancy condition, the largest shift is observed for Mistral-7B-Instruct-v0.3 (Cohen's d = 0.34), followed by Qwen2.5-7B-Instruct (d = 0.13), while Zephyr-7B-β shows near-zero drift (d = 0.04). We also find that the SST-2 sentiment proxy and the subject-directed regard classifier sasha/regardv3 correlate only modestly (r ≈ 0.29–0.35) on professional-domain text, indicating that scorer choice can materially affect fairness conclusions. Finally, we show that single-turn baselines can mischaracterise relative fairness risk in multi-turn deployment contexts. BiasDrift contributes an exploratory measurement framework for assessing the temporal stability of fairness in conversational AI systems.

---

## uid: `doi:10.2139/ssrn.5133368`

- title: Generative AI in Academic Writing: A Comparison of DeepSeek, Qwen, ChatGPT, Gemini, Llama, Mistral, and Gemma
- authors: Ömer Aydın, Enis Karaarslan, Fatih Safa Erenay, Nebojsa Bacanin
- affiliations: not stated
- posted: 2025-04-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.5133368
- keyword hits: chatgpt, deepseek, gemini, generative ai, llama, mistral, qwen

### abstract

NOT AVAILABLE. You have title and authors only. Set bullet_provenance to "none", return an empty bullets array, and classify field and role only if the title makes it unambiguous.

---

## uid: `doi:10.2139/ssrn.6632438`

- title: Corporate Digital Twins from Email: Using Language Models to Mirror Organizational Life
- authors: Grace Jiarui Fan, Tianyi Peng, Xiaotong Tang, Hyeonik Park, Shangxuan Vivian Zhang
- affiliations: not stated
- posted: 2026-04-23
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6632438
- keyword hits: claude, gpt-4, large language model, large language models, llm, llms

### abstract

We propose corporate digital twins — structured, queryable, and dynamic computational mirrors of organizations — built entirely from internal email archives using large language models (LLMs). Just as digital twins in engineering replicate physical systems for monitoring and simulation, a corporate digital twin replicates the social, operational, and strategic fabric of a firm. We demonstrate this concept on the Enron email corpus (345K emails, 150 employees, 1997–2002), constructing a multi-layered representation that includes: (1) person profiles: capturing roles, departments, expertise, and communication networks for 150 mailbox-owning employees anchored to ground-truth identity, plus references to over 19,000 additional colleagues, counterparties, and external contacts surfaced from their communications; (2) weekly project tracking: identifying 42,013 distinct projects with progress statuses, team compositions, and activities across 230 weeks; and (3) organizational vignettes: surfacing over 7,000 notable moments of humor, irony, prescience, and organizational culture spanning the firm's lifecycle. Our extraction pipeline combines week-batched and person-batched LLM processing with structured JSON schema enforcement, requiring no manual annotation. We accompany our work with an interactive website that brings this once-legendary, once-bankrupt firm back to life, enabling any user to explore the day-to-day workings of Enron as they unfolded. As a downstream application, we introduce EnronBench, an agent evaluation benchmark comprising 10 realistic workplace tasks (e.g., budget planning, crisis response) grounded in the digital twin. We compare a ReAct-based agent (GPT-4o-mini) against Claude Code (Opus 4.6) using identical LLM-evaluated rubrics, finding that the frontier coding agent scores 85.8/100 on average and completes the suite in roughly one-fifth the time, while the structured ReAct agent averages 69.2/100 and exposes systematic tool-use limitations. We release our extraction framework, structured outputs, and benchmark suite to support future research on organizational language modeling and agent evaluation.

---

## uid: `doi:10.2139/ssrn.6627078`

- title: AI Meets Antitrust: How Large Language Models Reshape Market Concentration
- authors: Alejandro Medina Sandin
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6627078
- keyword hits: claude, gemini, gpt-4, large language model, large language models, llm, llms

### abstract

Large language models are rapidly becoming a primary interface for consumer product discovery, yet little is known about how their recommendations relate to real-world market structure. This paper provides the first empirical benchmark of LLM brand recommendations against actual market shares. Using 1,429 responses from three frontier models (GPT-4o, Claude Sonnet 4, Gemini 2.5 Flash Lite) across sixteen U.S. consumer categories, I compare the implied concentration of LLM recommendations to retail-value shares from Euromonitor Passport 2024. In fragmented markets such as skincare, LLMs concentrate their recommendations on fewer brands than the market share distribution would suggest; in highly concentrated markets such as headphones, they distribute recommendations across more brands than the market share distribution reflects. Both patterns reflect a single phenomenon: LLM recommendations live in a narrow concentration band roughly one third the width of the real market's, regardless of where the real market sits. A second pattern tilts top recommendations toward specialist and premium brands that hold only two-thirds of the market share of actual category leaders. Findings are stable across the three models studied.

---
