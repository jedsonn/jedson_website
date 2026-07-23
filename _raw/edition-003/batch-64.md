# Classification batch 64 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-64.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6756299`

- title: A Hybrid Statistical–Machine Learning Framework for Analyzing the Impact of Prompt Engineering and User Behavior in Large Language Models
- authors: Kareem  Abbas Dawood, Osman  Sharif Osman, Shan Khazendar, Muayad Jajo
- affiliations: not stated
- posted: 2026-05-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6756299
- keyword hits: large language model, large language models, llm, llms, prompt engineering

### abstract

Large language models (LLMs) have transformed human-computer interaction (HCI) by enabling users to communicate with them in natural language. Although the quality of the output is influenced by the structure of the prompt and user behavior, many studies still examine prompt structure and user behavior separately rather than analyze both together quantitatively. This study proposed a hybrid statistical-machine learning framework for analyzing the impact of prompt engineering and user behavior on the quality of response in LLMs. The study compiled a dataset of 1200 prompt response pairs covering unstructured, structured, and multimodal prompts. Then the study evaluated how the structure of the prompt, the clarity of instruction, and interaction constraints affected response quality using ANOVA and correlation analyses. To extend the analysis, the authors trained a neural network classifier to recommend effective prompt strategies from the prompt features. The results showed that the structure prompts improved performance by 27% over unstructured prompts, while multimodal prompts improved performance by 18% in a visually demanding task. As evidenced by the robust ROC curve, precision–recall curve, and confusion matrix, the classifier scored 91.6 accuracy. The finding shows how prompt design and user interaction affect the quality of LLM responses, thereby providing a framework for more reliable human-AI interaction.

---

## uid: `doi:10.2139/ssrn.6759124`

- title: LKE-MVQA: A Large Language Model Knowledge-Enhanced Method for Medical Visual Question Answering
- authors: siyuan tang, Siriguleng Wang, Gang Xiang, Hongda pang, Gu Yu, Jinliang Zhao, yuxin wang
- affiliations: not stated
- posted: 2026-05-13
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6759124
- keyword hits: fine-tuning, large language model, large language models, llama

### abstract

Medical Visual Question Answering (Med-VQA) generates answers from medical images and associated questions, aiding computer-aided diagnosis and clinical decision support. Existing methods face limitations, such as overreliance on statistical correlations, underuse of external medical knowledge, poor cross-modal alignment, and unreliable answers. This paper introduces LKE-MVQA, a knowledge-enhanced approach leveraging large language models for Med-VQA. It employs a dynamic knowledge routing mechanism, combining image descriptions from BiomedCLIP with question semantics to select relevant medical knowledge from the UMLS knowledge graph, improving accuracy and reducing noise. A knowledge-infused dual-attention module enhances image and question features, aligning multimodal semantics. The Llama-3.2-3B model is fine-tuned using prompt tuning, Low-Rank Adaptation (LoRA), and feed-forward adapters, along with an answer consistency verification loss to ensure reliability. Experimental results on the VQA-RAD, SLAKE, and PathVQA datasets demonstrate that LKE-MVQA outperforms state-of-the-art methods. Ablation studies and Grad-CAM visualizations confirm the effectiveness of key components, such as dynamic knowledge routing, multimodal fusion, and fine-tuning strategies. This work offers a new pathway for building interpretable, reasoning-oriented medical visual question answering systems.

---

## uid: `doi:10.2139/ssrn.6767310`

- title: Fine-Tuning Small Language Models for Solution-Oriented Windows Event Log Analysis
- authors: Siraaj Akhtar, Saad Khan, Simon Parkinson
- affiliations: not stated
- posted: 2026-05-14
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6767310
- keyword hits: fine-tuning, large language model, large language models, llm, llms

### abstract

Large language models (LLMs) have shown promise for event log analysis, but their high computational requirements, reliance on cloud infrastructure, and security concerns limit practical deployment. In addition, most existing approaches focus only on the identification of the problem and do not provide actionable remediation. Small language models (SLMs) present a lightweight alternative that can be fine-tuned for a specific purpose and hosted locally. This paper investigates whether SLMs, when fine-tuned for a specific task, can serve as a practical alternative for event log analysis while also generating solutions. We first create a large-scale synthetic Windows event log dataset that contains remediation actions using a high-performing LLM. We then fine-tune multiple SLMs and LLMs using the LoRA parameter-efficient fine-tuning technique and evaluate their performance by comparing with expert assessment. The results show that the dataset accurately reflects real-world scenarios and that fine-tuned SLMs consistently outperform LLMs in identifying issues and providing relevant remediation, while requiring fewer computational resources.

---

## uid: `doi:10.2139/ssrn.6752998`

- title: Sex, Drugs, and LLMs: Social Desirability Bias in Language Models
- authors: Sophia Kazinnik, Jos&eacute; Ram&oacute;n Enr&iacute;quez, Jacy Anthis, David Nguyen, Jiaxin Pei
- affiliations: not stated
- posted: 2026-05-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6752998
- keyword hits: large language model, large language models, llm, llms, prompting

### abstract

When surveys ask about sensitive topics, respondents often shift their answers toward what seems socially acceptable, underreporting behaviors such as drug use or infidelity and overreporting behaviors such as voting, exercise, or charitable giving. We show that large language models (LLMs) often exhibit the same pattern. This cannot be explained solely by safety-related refusals: although some models decline to answer the most sensitive questions, across 13 models and 15 case studies, responses were generally closer to biased human self-reports than to the best available behavioral benchmarks. Using an open weights LLM, we show that information about actual behavior remains present in the model's internal representations, even when its final answer is pulled toward the socially desirable response. Steering those activations moves responses closer to actual behavior in 13 of 15 case studies. Prompting is less effective: providing the true base rate improves accuracy somewhat, while instructing the model to ignore social norms or warning that its answers will be checked has little effect. We interpret these results as evidence of a gap between internal representation and reported output in LLMs. Social desirability bias therefore provides a useful setting for studying this mismatch. At the same time, because accuracy can be substantially improved, LLM-based social simulations should not be written off.

---

## uid: `doi:10.2139/ssrn.6777479`

- title: Language-Based Screening for Alexithymia in Veterans with PTSD Using a Large Language Model
- authors: Tomas Meaney, Vijay Yadav, Isaac Galatzer-Levy, Richard Bryant
- affiliations: not stated
- posted: 2026-05-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6777479
- keyword hits: large language model, llm, llms, mistral, transformer model

### abstract

Alexithymia refers to challenges with the identification and description of emotional states. Prior research has shown that alexithymia negatively affects the course, symptom severity and treatment of clinical psychological conditions, including posttraumatic stress disorder (PTSD). The measurement of alexithymia currently relies heavily on self-report measures, which is problematic given that these measures require emotional awareness that those with alexithymia may not have. In the present study, the capacity of a Large Language Model (LLM) to accurately classify individuals with and without alexithymia was evaluated based on its capacity to make these classifications using speech extracts derived from recordings of war veterans with probable PTSD (N = 96) describing traumatic events. These speech extracts were also analyzed by a sentence embedding model (MPNet) combined with a machine learning classification algorithm. The accuracy of the models’ classifications was assessed relative to participants levels of alexithymia on the Toronto Alexithymia Scale (TAS-20). The LLM (Mistral Nemo Instruct 2407) achieved a good level of classification accuracy (F1-score = 0.73, Precision = 0.69, Recall = 0.77), that was better than the performance of the sentence transformer model (F1-score = 0.68, Precision = 0.76, Recall = 0.63), despite producing a higher rate of false positives. These results suggest that the analysis of text extracts with LLMs could assist in screening for alexithymia in veterans with PTSD, and subsequently contribute to the delivery of more tailored and effective treatment for these individuals. However, further research is required to improve the performance of this approach.

---

## uid: `doi:10.2139/ssrn.6732238`

- title: Preregistration for Experiments with AI Agents
- authors: Michelle Vaccaro
- affiliations: not stated
- posted: 2026-05-20
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6732238
- keyword hits: ai agent, large language model, large language models, llm, llms

### abstract

The proliferation of large language models (LLMs) and autonomous AI agents has given rise to a rapidly growing methodological paradigm: "in silico" behavioral experiments. Originally conceived as a way to use AI agents as proxies for human participants in studies of cognition, decision-making, and social dynamics, this approach has taken on new significance—as AI agents increasingly negotiate, transact, and make consequential decisions on behalf of people and organizations, understanding their behavior has become a research priority in its own right. While these experiments with AI agents offer unprecedented advantages in terms of scalability, cost efficiency, and experimental control, they also inherit, and in some cases amplify, methodological vulnerabilities that have long plagued human subjects research. To address these issues, this paper argues that preregistration practices—central to improving the credibility of human subjects experiments—should now be extended to experiments with AI agents. We systematically catalog the researcher degrees of freedom that experiments with AI agents introduce—model selection, prompt wording, settings, and outcome-contingent redesign, for example—and show how the low cost of iteration and lack of reporting norms make these choices both easy to exploit and difficult to detect. We propose a preregistration template tailored to experiments with AI agents and call on conferences, journals, and funding agencies to make preregistration standard practice for this emerging research paradigm.

---

## uid: `doi:10.2139/ssrn.6806427`

- title: Adaptation and Evaluation of a Retrieval-Augmented Generation QA Model for Water Environment Management in Tidal River Networks
- authors: Junkai Huang, Jing Liu, Ming Huang, Min chen, Siyuan Liu, Sheng Jiang, Qihua Ran, Saiyu Yuan
- affiliations: not stated
- posted: 2026-05-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6806427
- keyword hits: large language model, large language models, qwen, retrieval-augmented

### abstract

Hydraulic regulation and water environment management in tidal river networks are constrained by coupled river–tide dynamics, complex water quality responses, pollution source tracing difficulties, and delayed regulatory knowledge access. Thus, enhancing the efficiency of knowledge acquisition and information integration in regulatory decision-making is urgently needed. To address this issue, this study uses the Wennan tidal river network in Shanghai as a case study to construct a retrieval-augmented generation (RAG) question-answering framework integrating document vector retrieval with structured river network data querying. We propose a method to evaluate large language model response performance using citation omission and error rates. We quantitatively analyze the performance of six mainstream open-source large language models in RAG-based question answering for river network water environment management. The main conclusions are as follows: (1) Results indicate that Qwen3.5-9B achieved the best overall performance. Under the RAG framework, Qwen3.5-9B's question-answering accuracy improved significantly across all knowledge tasks compared to direct answering, with a 21.7 percentage point increase for water quality-related questions. (2) The hybrid attention architecture demonstrated superior adaptability in multi-evidence association and complex-context tasks. Knowledge distillation enhanced content generation quality and reasoning organization, though its impact on structured citation behavior remained limited. Reasoning improvements did not synchronously enhance citation standardization. While MoE architectures expand knowledge coverage, their advantage in breadth does not directly translate to stable reasoning and citation capabilities in complex multi-evidence scenarios. (3) Differences in structured citation generation among large language models stem from the combined effects of pretraining corpora, training strategies, and architectural characteristics. (4) The RAG system deployed in Shanghai's Intelligent System for Hydrodynamic Reconstruction and Water Environment Improvement of the Wennan Area verified the feasibility of locally deploying Qwen3.5-9B for intelligent knowledge services in water environment management. These findings offer quantitative benchmarks and practical guidance for applying large language models to digital twins of tidal river networks, intelligent water environment management, and regulatory decision-making.

---

## uid: `doi:10.2139/ssrn.6734262`

- title: A Validation Layer for AI-to-Unix Execution
- authors: Sean T. Gilley
- affiliations: not stated
- posted: 2026-05-21
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6734262
- keyword hits: ai agent, claude, large language model, large language models

### abstract

Large language models are increasingly used to generate Unix shell commands in operational and development environments. Their output is probabilistic; Unix execution is deterministic and irreversible. This structural mismatch creates a missing layer between AI suggestion and system execution. AIShell-Gate addresses that gap with a deterministic policy engine and execution gateway implemented in portable C with no external dependencies. Every proposed command is evaluated against a configurable, layered policy before execution; the policy engine and executor are separated into distinct processes across a hard OS boundary so that neither can subvert the other. The system enforces argument-level access controls, path restrictions, network target rules, and risk-scored confirmation escalation, and produces a tamper-evident HMAC-SHA256 audit chain of every decision. AIShell-Gate serves two distinct user populations from a single unified policy engine: AI agents submitting JSON execution plans, and human operators working interactively at a terminal.The same gate, the same policy, and the same audit chain apply to both.For human operators, the system functions simultaneously as a safety net, a teaching tool — every flag assessment carries documented reasoning explaining why a command is categorized as it is, not merely what the decision is — and a disciplined workflow enforcing confirmation gates and audit trail on operator-generated commands. A novel threat class addressed by version 1.02 is Model Sub-Delegation — an AI agent consulting a second inference system to influence a policy decision without the operator's knowledge. The specific mechanism is Self-Referential API Access: the agent contacts inference endpoints — local, remote, or its own model's public API — from within a gated execution session. The practice is not inherently prohibited; AIShell-Gate's gate ensures the operator is aware it is occurring and explicitly approves it, converting an invisible action into a conscious decision. Version 1.0 Beta covers the local-inference variant through the 108-entry port catalog and loopback-alias normalization; a hostname catalog covering remote and same-model variants — 21 named commercial inference endpoints across all major providers — is introduced in v1.03 and described in full in §11. The architecture is intended to occupy the specific gap between unrestricted AI shell access and no AI integration at all, providing a practical, auditable execution boundary for organizations introducing AI into Unix workflows. Version 1.02 introduces an MCP (Model Context Protocol) server — aishell- gate-mcp — that exposes two tools to AI coding environments such as Claude Code and Cursor: evaluate_plan for policy-gated plan inspection without execution, and execute_plan for live execution. Every MCP tool response includes a protocol version block, making the full wire interface versioned and forward-compatible. The flag catalog has expanded to 2,088 entries covering ansible, ansible-playbook, az (Azure CLI), extended kubectl, terraform, and helm flags, kernel operations (insmod, kexec, rmmod), disk partitioning tools, debugfs, socat, nftables, and the full LVM suite. Network policy enforcement has been formalized: net_default_deny — decoupled from command default-deny — requires explicit allow rules for any detected network target in ops_safe, read_only, and dev_sandbox presets, while CI presets allow unrestricted network access for package registry and artifact store access. New operator tools include --dry-run- json , which produces a machine-readable JSON document describing what a plan would execute without executing it, and --test-plan , a policy testing mode that evaluates a JSON file of test cases against the active policy and reports PASS/FAIL, suitable for committing alongside policy files and running in CI. This paper introduces a formal glossary of terminology coined for the AI execution security domain, including Model Sub-Delegation, Self-Referential API Access, Command-Coded Confirmation, Zero-Effect Fail-Closed, Declared and Injected Source Identity, Epistemic Honesty, Execution Posture, Net Default-Deny, and Broker Seam. See §18.

---
