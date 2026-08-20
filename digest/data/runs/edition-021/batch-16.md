# Classification batch 16 of 22, edition 21

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-021/batch-16.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7254218`

- title: Automatic Techniques for Security Bug Report Identification: A Systematic Mapping Study
- authors: Muhammad Laiq, Usman Nasir
- affiliations: not stated
- posted: 2026-08-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7254218
- keyword hits: large language model, large language models

### abstract

Several studies have investigated the use of automated techniques to help practitioners identify security bug reports early in the defect management process. However, currently there is no comprehensive overview of this research area. Such an overview will help identify future research directions and consolidate the potentially relevant existing solutions. This study aims to provide a comprehensive overview of automated techniques for identifying security bug reports. To achieve this, we conducted a systematic mapping study and identified 28 primary studies. The study's findings show that the literature has evaluated various automatic techniques for identifying security bug reports, including traditional machine learning, deep learning, and more advanced large language models. The two main challenges identified are the lack of labeled data and data imbalance. Furthermore, we observe that existing studies lack evaluations in real industrial settings and rely mostly on archival data from open-source repositories. The most commonly used data sources in these studies include Wicket, Ambari, Camel, and Derby. Overall, the literature appears fragmented, highlighting the need for future work to focus on comprehensive evaluations of the most promising techniques.

---

## uid: `doi:10.2139/ssrn.7270442`

- title: Vision and Language Models for Classifying Maxillary Sinus Disease on Cone-Beam Computed Tomography: A Transparent Multimodal Benchmark
- authors: Seba Al-Hebshi, Hanadi Khalifa, Tuan Pham
- affiliations: not stated
- posted: 2026-08-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7270442
- keyword hits: chatgpt, large language model

### abstract

Background: Cone-beam computed tomography (CBCT) frequently captures the maxillary sinuses incidentally, and reliable automated detection of sinus abnormality is clinically relevant. Unlike most vision–language benchmarks in medical imaging, which pair images with pre-existing, human-authored clinical reports, findings text can also be generated directly by a large language model from the image itself—raising the question of how much diagnostic value such AI-derived text carries, and whether that value depends on independent verification. Multimodal artificial intelligence (AI) benchmarks risk overstating performance if the provenance of each input—image, raw AI-generated text, or radiologist-verified text—is not clearly separated and reported. Methods: We used 300 mid-sagittal CBCT slices from the MMDental dataset. ChatGPT generated findings text and a provisional normal/abnormal label for every slice (majority vote, three independent readings from the image alone); primary classification performance was assessed on this full, unfiltered set (n=300). A radiologist then independently reviewed each case’s image together with ChatGPT’s description, producing their own diagnosis; three cases were excluded as insufficient, yielding 297 confirmed cases. On this subset, every model was retrained and re-evaluated under identical 10-fold cross-validation on both the provisional ChatGPT-only labels (“pre”) and the radiologist-confirmed labels (“post”), isolating the effect of label provenance from image or architecture. Eight vision architectures, seven language classifiers, and five VLMs were evaluated throughout; three generative models performed exploratory note-drafting. Findings: Raw ChatGPT-generated text produced the highest performance of any modality or condition: language models reached near-ceiling AUC (0·992 to 1·000, n=300), exceeding every vision model (AUC 0·799 to 0·880) and every VLM image-only probe (AUC 0·63 to 0·69). On the 297-case pre/post analysis, this advantage depended heavily on label source: language and text-derived VLM performance fell substantially from ChatGPT-only to radiologist-confirmed labels (e.g. BERT-base AUC 0·999 to 0·837), while vision-model performance was stable or modestly improved (e.g. DenseNet-121 0·867 to 0·891). The radiologist reclassified 62 of 297 cases (21%) relative to ChatGPT’s provisional read, and a meaningful proportion of raw ChatGPT text was clinically uninterpretable or unsupported by the imaging. Interpretation: As shown here for the first time, raw, image-derived AI-generated text yields the highest apparent classification performance in this benchmark, but this reflects the text’s alignment with its own self-generated labels rather than verified diagnostic content, and a substantial share of that text is not clinically explainable. Radiologist-confirmed text and labels give a lower but trustworthy estimate of true performance, on which convolutional neural network (CNN) vision models remain a stable, comparatively inexpensive baseline. Multimodal dental AI should report performance separately by modality and label provenance rather than pooling headline metrics.

---

## uid: `doi:10.2139/ssrn.7257164`

- title: Research State: A Candidate Semantic Abstraction for Knowledge Continuity in AI-Native Research Operating Systems
- authors: Agus Sutrisno, Anang Lastriyanto
- affiliations: not stated
- posted: 2026-08-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7257164
- keyword hits: large language model, large language models

### abstract

The increasing use of large language models, research agents, scientific knowledge graphs, and workflow automation is transforming how scientific investigations are conducted. These technologies provide capable mechanisms for memory, provenance, knowledge representation, workflow execution, and agent interaction. Yet these mechanisms remain distributed across different system abstractions. Persistent agent-state research addresses durable operational state and governance (Ding et al., 2026); workflow-provenance systems represent execution and data lineage (Souza et al., 2025); scientific knowledge-orchestration systems represent entities, claims, evidence, methodological relations, and increasingly, research-agent workflows and executable tool interfaces (Cao et al., 2026); and knowledge-continuity frameworks address the preservation of actionable knowledge across organizational transitions (Türüc, 2026). What remains insufficiently specified is a common abstraction for the evolving semantic condition of a scientific investigation itself-an abstraction that explicitly integrates the multiple dimensions of research continuity within a single, model-agnostic construct. This paper proposes Research State as a candidate semantic abstraction for AI-native Research Operating Systems. Drawing on design theory (Gregor & Jones, 2007; Walls et al., 1992), Research State is defined as a persistent, research-semantic, and model-agnostic representation of the evolving condition of a scientific investigation. The construct explicitly integrates eight dimensions—identity, knowledge, evidence, governance, workflow, execution, interaction, and recovery—within a single abstraction designed to preserve coherence across the entire research lifecycle. Following the principle of separation of concerns (Dijkstra, 1982) and the tradition of abstract data types (Liskov & Zilles, 1974), we distinguish Research State as a conceptual construct from Research State Object (RSO) as one possible concrete representation. The construct is developed through a targeted construct-boundary mapping across four adjacent domains. The resulting analysis identifies integration, purpose, semantic, explicitness, and independence gaps within the reviewed corpus. We formulate three candidate system-level properties—cross-dimensional consistency, model-agnostic resumability, and research-lifecycle coherence—as testable design propositions rather than empirical findings. Two analytical walkthroughs, following the analytical evaluation tradition in design science (Hevner et al., 2004), illustrate how these propositions can be evaluated after implementation. The contribution of this paper is a design-theoretical proposal. Within the reviewed corpus, we did not identify a construct that explicitly defines all eight dimensions as an integrated, research-semantic state abstraction whose persistent unit is the scientific investigation and whose semantic interpretation is intended to remain independent of a particular reasoning model. This work builds on two prior contributions: KAMDOL Academic OS (Sutrisno & Lastriyanto, 2026a), which validated a research risk intelligence capability, and KamiOS (Sutrisno & Lastriyanto, 2026b), which proposed the Research Operating System architecture. The present paper formalizes the candidate semantic state abstraction that such a Research Operating System manages—a contribution that is conceptual and definitional rather than architectural or capability-specific.

---

## uid: `doi:10.2139/ssrn.7274519`

- title: Mind the (Wage) Gap: The Large Firm-SME Divide and Delayed Labor Market Entry for Young Adults in South Korea
- authors: Soon-hong Min
- affiliations: not stated
- posted: 2026-08-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7274519
- keyword hits: claude, large language model

### abstract

This study examines the relationship between South Korea’s dual labor market, the divide between large firms and small and medium-sized enterprises (SMEs), and the increasingly delayed entry of young people into the labor market. As the working-age population shrinks and mismatch widens, the inefficient use of available labor has become a long-term social concern. Delayed entry into the workforce gives workers less time to accumulate skills and experience, eroding human capital and, in aggregate, the skill level of the entire workforce. Drawing on recent administrative data, the analysis shows that large firms have steadily accounted for about 12 percent of all regular wage workers (excluding temporary workers and day laborers), while the SME share now sits around 39 percent. Although on aggregate, the ratio of average SME wages to average wages at large firms has improved over the past ten years, climbing from 0.43 in 2015 to 0.49 in 2024, in nominal terms the monthly wage gap grew from KRW 2.98 million to KRW 3.65 million3), so workers are likely to perceive the gap as having widened, rather than narrowed. The labor market has also grown more rigid: workers are likely to stay in their current positions, entries and exits have declined, and moving from an SME to a large firm is almost unheard of; at most, just five to six percent of workers in their twenties (the most mobile cohort) do so. Empirical results indicate that the widening of the wage gap between large firms and SMEs is associated with delayed entry into workforce, and that the effect of the rigid, dual structure of the market on the supply of young adults’ labor supply carries a lag. Given the current wage gap, four-year university graduates are estimated to defer graduation by about one month, and labor market entry by about 3.6 months. Because the structure of the labor market appears to be a quasi-permanent feature of the Korean economy, this study argues for the introduction and continuous, permanent operation of support policies that raise the real wages of young SME workers through direct support to individuals, rather than to firms. The author argues that the permanence of such programs would incentivize long-term employing planning by both young workers and firms. This paper was translated from the original Korean using the Claude Opus 5 large language model (max effort). The text was reviewed by an editor and the author prior to publication.

---

## uid: `doi:10.2139/ssrn.7275101`

- title: From Rider Voices to Route-Level Evidence: A Traceable LLM Framework for Transit Co-Planning
- authors: Ruize Qin, Ali Mansouri, Dongyang Zhen, Qingbin Cui, Abdolmajid Erfani
- affiliations: not stated
- posted: 2026-08-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7275101
- keyword hits: large language model, llm

### abstract

Large-scale public comments provide valuable knowledge about how proposed transit changes affect riders, but their unstructured, multi-issue, and multi-route nature makes them difficult to incorporate into route-level planning review. Existing manual and computational approaches can classify or summarize public feedback but provide limited support for aggregating concerns by planning object while preserving links to the underlying comments. To address this gap, this study develops a traceable large language model (LLM) framework that transforms public comments into structured, route-level evidence for transit network co-planning. The framework first uses a fine-tuned multi-label LLM to represent each comment across six planning-action dimensions: frequency, routing, stop addition, stop retention, stop removal, and transfer concerns. It then links the resulting semantic signals to referenced routes, aggregates them into route-dimension evidence scores, and separates dominant aggregate evidence from repeated non-dominant concerns. Third, a source-bounded general-purpose LLM organizes surfaced evidence subpackages into route-level planner-reviewable evidence objects with separate Track A consensus evidence and Track B minority-awareness sections. The framework was evaluated using comments from the Washington Metropolitan Area Transit Authority Better Bus Network Redesign project. The results demonstrate semantic validity, route-level evidence governance, sentence-span traceability, and planner-facing evidence organization. The framework offers a controlled alternative to direct black-box LLM summarization for LLM-enabled transit co-planning.

---

## uid: `doi:10.2139/ssrn.7254322`

- title: ECHO-7: A Local-first Personal AI Architecture with 7-Day Rolling Memory Synchronization and user-controlled Memory Consolidation
- authors: Manish Kumar Singh
- affiliations: not stated
- posted: 2026-08-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7254322
- keyword hits: large language model, llama, llm

### abstract

Personal Artificial Intelligence (AI) systems have become ubiquitous, yet they face a fundamental tension: cloud-based solutions offer seamless cross-device memory continuity but raise significant privacy concerns, while local-first systems preserve user privacy but fragment the user experience across devices. This paper presents ECHO-7, a novel local-first personal AI architecture that reconciles these competing objectives through a principled four-tier memory hierarchy-Working, Recent, Important, and Archive. ECHO-7 employs local Large Language Model (LLM) inference via llama.cpp to ensure complete privacy, while enabling cross-device synchronization through encrypted delta updates stored temporarily in a lightweight cloud layer with a 7-day rolling retention policy. After 7 days, memories undergo automated consolidation-extraction of salient information, deduplication, and permanent archival to the user's local drive-ensuring long-term data ownership and minimal cloud exposure. We evaluate ECHO-7 across four dimensions: (1) memory retrieval accuracy, achieving 100% accuracy over 10 test queries; (2) synchronization efficiency, demonstrating 60.26% faster delta synchronization compared to full-sync baselines; (3) cloud exposure, showing bounded storage (5936 bytes) independent of conversation length via 7-day retention; and (4) consolidation quality, achieving 100% preservation of important information. ECHO-7 provides a practical, privacy-preserving solution for personal AI that does not compromise on user experience or data ownership.

---

## uid: `arxiv:2608.13547v1`

- title: QuoteBench: How Matched Scores Can Hide Command-Path Failures
- authors: Shangao Li, Yao Zhang, Volker Tresp, Yuanyuan Yang
- affiliations: not stated
- posted: 2026-08-13
- source: arXiv
- link: https://arxiv.org/abs/2608.13547v1
- keyword hits: gpt-5, llm

### abstract

LLM coding agents issue Bash commands through interfaces that may serialize, wrap, and reparse model output. Matched execution scores alone cannot distinguish command-generation errors from failures introduced after generation. QuoteBench measures this boundary with exact final-state validation on 56 one-shot tasks from 14 incident-derived families, crossing the generation contract with the execution transport around one deliberately unescaped added parser. Escaping at the interpolation point reproduces each replayed reply's raw-path outcome, so any recovery under a disclosed boundary must come from the model changing its generation. Across eight same-window configurations, replaying the same reply through the added parser lowers success by 55.4 to 73.2 percentage points; disclosure recovers 30.4 to 60.7 points for six configurations, and zero or slightly negative for the other two. Raw generation is nearly saturated at the frontier; boundary adaptation is what still separates models. GPT-5.6-sol's matched gap of -3.6 points hides -64.3 points of damage and +60.7 points of compensation. The deployment configuration reorders models: one reversal among 26 comparable pairs is unambiguous and four more sit on single-task margins. Evaluations of command-issuing agents should report the model configuration, generation contract, execution path, operating point, and final-state validator rather than treat a matched score as an intrinsic model property.

---

## uid: `doi:10.2139/ssrn.7259758`

- title: The Devaluation of the Publication Signal: A Secondary-Data Analysis of AI's Impact on Academic Credentialing, 2022 to 2026, with Projections to 2036
- authors: Elijah Adeyeye
- affiliations: not stated
- posted: 2026-08-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7259758
- keyword hits: generative artificial intelligence, large language model, large language models

### abstract

For decades, the number of peer-reviewed publications a researcher holds has functioned as a trusted signal of scholarly seriousness, guiding decisions by scholarship committees, hiring panels, and funding bodies. This signal has worked precisely because producing it convincingly has been costly, requiring years of methodological training and sustained effort. This paper asks whether that signal can survive the next five to ten years, given that generative artificial intelligence has sharply lowered the cost of producing something that resembles a publication without a corresponding increase in genuine scholarly effort. Applying signaling theory (Spence, 1973) to secondary data from 2022 to 2026, this paper finds that submission volume to academic journals has risen substantially since the release of accessible large language models, that writing quality has declined over the same period, and that a documented integrity crisis, including the retraction of more than 11,300 papers from a single major publisher, has already made the credential harder to trust at face value. At the same time, institutions have begun building alternatives, including Open Science badges and verified researcher identity systems, that attach credibility to a checkable process rather than a finished document alone. The paper concludes that publication count is unlikely to disappear as a credential by 2036, but is likely to stop functioning sufficiently on its own, gradually supplemented by harder-to-fake, processbased markers. The paper closes by considering what this shift means for early-career researchers and for institutions in the Global South, where the cost of producing a credible publication has always been higher than average, and where the transition to a new credentialing system could either narrow or widen existing gaps depending on how deliberately the supporting infrastructure is built.

---
