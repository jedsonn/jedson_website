# Classification batch 409 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-409.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.7077603`

- title: ChatGPT Enterprise Adjustment Trajectories Through a Dynamic Job Demands-Resources Perspective
- authors: Ally St. Aubin, Camila Hazzard, Katlyn Bui, Bradley Brummel
- affiliations: not stated
- posted: 2026-07-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7077603
- keyword hits: chatgpt, prompting

### abstract

This study further develops job demands-resources (JD-R) theory using a dynamic consideration of digital job resources, digital job demands, techno-work burnout, and techno-work engagement associated with technology implementation in the workplace. Twelve employees from a ChatGPT Enterprise pilot program participated in focus groups and discussed their experiences with its implementation. Across participants’ retrospective accounts of the implementation process, experiences followed a pattern of initial learning demands gradually decreasing as participants integrated ChatGPT into their work and perceived increasing value in ChatGPT as a resource to support efficiency in both mundane and complex tasks. Across these common phases, participant descriptions of their adjustment to technology aligned with one of three change profiles: (1) Rapid Adjustment, (2) Gradual Adjustment, and (3) Minimal Adjustment. Participants provided theory-aligned descriptions of their experiences, given minimal prompting, thereby supporting JD-R theory. Findings support the application of JD-R theory to technology experiences by demonstrating how workplace AI implementation is dynamic and nonuniform across employees. Finally, we expanded techno-overload to include a monitoring burden in reviewing ChatGPT output, and expanded techno-insecurity to include concerns about deskilling. Organizations can maintain awareness of employee experiences using focus groups or questionnaires, and leverage informal and formal learning opportunities to support employees’ adjustment to technology interventions. Previous research on JD-R theory and technology has overlooked the implementation of new technologies and how perceptions of digital JD-R constructs evolve. Understanding how these changes occur over time when new workplace technologies are implemented can help organizations successfully manage the implementation process.

---

## uid: `doi:10.2139/ssrn.7078021`

- title: Automatic seismic phase picking benchmark on a local network in Central Asia: DT-SFM, PhaseNet, and EQTransformer versus a tuned STA/LTA
- authors: Suratbek Khalbayev, Javokhir Kodirov, Ming Zhao, Shi Chen, Timur Mamarozikov, Bakhodir Alimov, Timur Kurbanov, Diyorbek Yusupov
- affiliations: not stated
- posted: 2026-07-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7078021
- keyword hits: fine-tuning, foundation model

### abstract

Automatic earthquake detection and phase picking are increasingly performed with deep-learning models, yet how they behave under adverse, out-of-distribution conditions remains poorly constrained, particularly in regions absent from existing training datasets. We assemble a deliberately challenging benchmark of 846 manually reviewed events recorded by a compact local network in Central Asia, dominated by low-magnitude seismicity on noisy stations across local to regional distances, and use it to evaluate four detectors under a single protocol: the DiTing seismic foundation model (DT-SFM), the open-source PhaseNet and EQTransformer pickers, and a tuned STA/LTA detector. The deep-learning models are applied with their default configurations and without regional fine-tuning, while the STA/LTA detector is tuned to provide a strong baseline, and all are scored against the same manual reference picks. Ranked by P-phase F1, the order is DiTing (0.307), tuned STA/LTA (0.161), PhaseNet (0.127), and EQTransformer (0.077): only DiTing surpasses the classical detector, while both open-source pickers fall below it as their recall declines sharply with epicentral distance. A threshold analysis shows that the missed arrivals of PhaseNet are largely recoverable by lowering its probability threshold, so its position below the classical baseline is specific to the default operating point; those of EQTransformer are not recoverable in the same way. Timing accuracy is comparable across all methods, so detection rather than timing is the discriminating factor. The results delineate the limits of current pickers under demanding conditions and provide guidance for their use where no local training data exist.

---

## uid: `doi:10.2139/ssrn.7083233`

- title: Expert-guided progressive learning for label-efficient multi-fault diagnosis of industrial robots​
- authors: Soufiane Douimia, Abdelghani Bekrar, Abdessamad Ait El Cadi, Yassin El Hilali
- affiliations: not stated
- posted: 2026-07-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7083233
- keyword hits: fine-tuning

### abstract

Industrial robots in high-throughput manufacturing exhibit rare and mechanically coupled faults, making cycle-level diagnosis difficult under limited labels. This paper addresses the downstream artificial-intelligence problem of converting a fixed cycle-level feature interface (anomaly flags, Excess-Ratio (ER) localization profiles and encoder features from low-rate motor currents) into label-efficient multi-fault diagnosis with selective human handover. The engineering application is predictive maintenance of production-grade Kawasaki BX100S welding robots in an automotive manufacturing environment. The main artificial-intelligence contribution is a confidence- and distribution-aware selective predictor that abstains when classifier margin, ER ambiguity or out-of-distribution energy indicate unsafe autonomous diagnosis. Supporting components include cycle-phase-aware contrastive adaptation, active learning used as a label-efficiency mechanism, confidence-weighted supervised contrastive fine-tuning with normal replay, and an annotation-memory layer for auditability and case retrieval. On a controlled multi-fault campaign, the framework reaches 55.3 percent balanced accuracy over five coupled fault classes using 202 annotations (6.4 percent of the cycle pool), and 94.5 percent F1-score on a kinematically distinct brake fault; the coupled-class performance is reported as evidence that full autonomous diagnosis is unreliable under severe label scarcity, motivating the selective handover. In a cross-time deployment five months later, the handover policy reduces wrong autonomous decisions by 37 percent and selective risk by 18 percent. Historical computerized maintenance management system (CMMS) records confirm that the targeted fault axes match dominant maintenance drivers. Expert annotations are emulated by an oracle using controlled fault-injection labels; silent baseline drift remains unsolved and requires temporal monitoring.​

---

## uid: `doi:10.2139/ssrn.7077979`

- title: Automatizing Argumentative Move Analysis with Pre-trained Language Models: Variations by Proficiency and L1 Backgrounds
- authors: Weiran Wang, Wenjuan Qin
- affiliations: not stated
- posted: 2026-07-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7077979
- keyword hits: fine-tuning

### abstract

Argumentative writing is a core skill for L2 learners, but evaluating its structural components has long relied on labor-intensive manual coding, limiting scalability and generalizability. Pre-trained language models (PLMs) offer a potential solution, yet existing PLM-based studies lack diversity in corpora, struggle with rare argumentative moves, and neglect the L1 influence. This study aims to test the effectiveness of a fine-tuned BERT-based PLM in analyzing argumentative moves in L2 learners’ essays. The training data encompasses a stratified sample of 1,100 EFL argumentative essays, and human-guided feedback is incorporated in the fine-tuning process to ensure human alignment. PLM-labeled argumentative moves are used post fine-tuning to analyze by-proficiency and by-L1-background differences. Results showed the fine-tuned PLM achieved an overall high accuracy in labeling core moves (i.e., claim, data) but lower accuracy in rare moves (i.e., counterargument data, rebuttal data). Additionally, PLM-labeled moves reliably differentiated proficiency levels (advanced learners used more counterarguments and rebuttals) and L1 backgrounds (e.g., Singaporean learners included more counterarguments, while Pakistani learners focused on data). These findings confirm the PLM’s utility for scalable argumentative move analysis, provide insights into L1 influences on L2 argumentation, and inform the development of context-aware automatic writing evaluation (AWE) tools for diverse L2 learners.

---

## uid: `doi:10.2139/ssrn.7077651`

- title: Incentive-Compatible Token Design as a Signal of Venture Quality
- authors: Guillaume Andrieu
- affiliations: not stated
- posted: 2026-07-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7077651
- keyword hits: token embedding

### abstract

This paper examines whether token design can serve as a signal of venture quality in decentralized fundraising environments. We develop a simple model in which an entrepreneur privately informed about project quality chooses between a neutral token and an incentive-compatible token embedding a milestone-contingent feature. While the latter increases the likelihood of attracting external funding, it imposes a private cost on the entrepreneur.Because token design is publicly observable prior to investment, it affects investor beliefs and financing decisions. The model shows that a separating equilibrium arises only for an intermediate range of design costs. If incentive-compatible features are too inexpensive, low-quality ventures mimic high-quality ones and the signal loses credibility. If they are too costly, even high-quality entrepreneurs refrain from adopting them, leading to pooling outcomes.The paper highlights how signaling can be embedded directly in token architecture through observable design choices that constrain entrepreneurial behavior. The model also yields testable empirical implications: token structures imposing meaningful constraints on founders should attract greater investor participation, whereas nearly costless features should not predict venture quality. These predictions are consistent with emerging evidence on token-based financing.

---

## uid: `doi:10.2139/ssrn.7074138`

- title: The Evolution Of State Constitutional Enforcement
- authors: Allison Freedman, Joanna C. Schwartz
- affiliations: not stated
- posted: 2026-07-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7074138
- keyword hits: prompting

### abstract

In the wake of George Floyd’s murder, government leaders around the country called for legislative reforms to reduce police violence and increase accountability. A primary target of those reforms was qualified immunity—a Supreme Court doctrine that shields officers from damages liability, even if they have violated the Constitution, so long as they have not violated “clearly established” law. Colorado (in 2020), and New Mexico and New York City (in 2021) each passed legislation creating rights to sue for violations of state constitutional law; although each bill has a range of provisions, all prohibit qualified immunity as a defense. In New Mexico, Colorado, and New York City, have people been able to better protect their rights? Have courts in those jurisdictions been overwhelmed by frivolous, costly lawsuits? Have lawsuit payouts and insurance premiums skyrocketed? Have government employees retired in droves? Through extensive, semi-structured interviews with thirty-one people directly involved with litigation against New Mexico governments—including plaintiffs’ attorneys, defense attorneys, and risk management and insurance personnel—we have gained unparalleled insights about the impact of New Mexico’s Civil Rights Act (“NMCRA”) in the five years since its passage. Respondents’ observations varied in several regards but point toward five general conclusions about the impact of the NMCRA on the state’s civil rights ecosystem. First, there remain many unsettled questions regarding the NMCRA’s scope and application. Second, plaintiffs’ attorneys appear to be filing two categories of claims under the NMCRA. Third, the NMCRA is changing the manner in which civil rights cases are being litigated to some degree. Fourth, many interviewees report that insurance premiums and deductibles are rising in New Mexico but disagree about whether and to what extent the NMCRA is the cause. Fifth, interviewees agreed that uncertainty about the impact of the NMCRA on New Mexico’s civil rights ecosystem will resolve in the coming years. Our findings offer important insights for New Mexico stakeholders and stakeholders in other states considering government accountability legislation. Our findings show that the passage of government accountability legislation like the NMCRA can markedly change litigation dynamics without prompting a dramatic increase in filings, payouts, and insurance rates. Our findings illuminate the incremental and multi-faceted manner in which new constitutional rights evolve and suggest that uncertainties about and fluctuations in the civil rights ecosystem caused by legislation like the NMCRA will resolve over time. Finally, our findings make clear that any rush to judgment about the impact of the NMCRA or other government accountability legislation—positive or negative—would be both premature and oversimplistic. Instead, an understanding of the subtle evolution of civil rights enforcement will require repeated, nuanced study and assessment.

---

## uid: `doi:10.2139/ssrn.7076204`

- title: Product Networks as Strategic Assets: A Predictive Model for Reward-Based Crowdfunding Success in Technology Ventures
- authors: Zinat Shariati
- affiliations: not stated
- posted: 2026-07-08
- source: SSRN
- link: https://doi.org/10.2139/ssrn.7076204
- keyword hits: text embedding

### abstract

In the contemporary entrepreneurial ecosystem, securing financial capital remains a cornerstone of startup growth and viability. Accelerated by digital transformation, innovative financing mechanisms such as Reward-Based Crowdfunding (RBCF) have gained substantial traction. In this context, the "product network" emerges as a critical strategic asset capable of mitigating information asymmetry, fostering investor trust, and enhancing campaign appeal. This study aims to optimize RBCF campaigns on digital platforms by explicitly modeling the strategic role of product networks. Leveraging web scraping techniques, a dataset comprising 144 technology-oriented campaigns was extracted from Indiegogo. Product network dimensions (product attributes, value propositions, and target audiences) were vectorized and quantified via text embedding techniques, followed by rigorous preprocessing, classification, and cleaning in Python. Utilizing the embedding-derived product network, an optimized predictive model for crowdfunding success was developed and validated through a machine learning framework (train-test split). The empirical results demonstrate that the product network exerts a statistically significant impact on campaign success. Notably, the variables voluminous (funding target size), quantity_similarity (structural similarity of campaigns within the network), and owner_camp_cnt (creator's historical campaign count) emerged as the primary predictors of success. The findings reveal that product features (via novelty and attractiveness), value propositions (via transparency and competitive differentiation), and precise target audience specification (via streamlined communication) interact systematically to predict and optimize campaign outcomes. By delivering both a conceptual process model and a predictive model, this study offers robust theoretical and practical insights for crowdfunding stakeholders and proposes a foundational architecture for next-generation, intelligent crowdfunding platforms.

---

## uid: `arxiv:2607.07646v1`

- title: RL Post-Training Builds Compositional Reasoning Strategies
- authors: Azwar Abdulsalam, Nishil Patel, Andrew Saxe
- affiliations: not stated
- posted: 2026-07-08
- source: arXiv
- link: https://arxiv.org/abs/2607.07646v1
- keyword hits: fine-tuning

### abstract

Does RL post-training merely amplify primitive skills already latent in a base model, or can it compose primitive skills into new higher-level strategies? We study this question in a fully observable rewrite-grammar environment where the pretraining distribution is known and every generated rewrite can be audited. A Transformer is pretrained on primitive symbol-rewrite chains and post-trained on a Trace-based reasoning task with only a binary final-answer reward. RL solves held-out problems that remain rarely solved by the pretrained model even under much larger sampling budgets, while rejection fine-tuning improves early but plateaus. Trace analysis shows that RL reorganizes primitive competence through a phased compositional mechanism: it first strengthens primitive reductions, then discovers valid composed procedures. These include sequential compositions, which collapse ordered chains of primitive contractions, and parallel compositions, which combine independent primitive contractions in a single step. The composed procedures are not isolated samples; they are reused and consolidated into a stable repertoire. Comparing RL with rejection fine-tuning shows that the key difference is not exploration volume but selectivity: RFT produces many shortcut-like rewrites, much of them invalid, whereas RL concentrates exploration into valid reusable structure. Pretraining ablations show that the emergence of compositional strategies is gated not by primitive exposure alone, but by whether pretraining organizes primitive competence into reduction procedures that RL can later compress. The base model provides weak procedural ingredients; RL builds them into reliable higher-level strategies.

---
