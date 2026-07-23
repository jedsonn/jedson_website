# Classification batch 195 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-195.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6641596`

- title: On the Role of Geometric Representations for Ultra-Fine-Grained Crop Variety Identification
- authors: Charlotte Tibi, Ilyass Moummad, Alexis Joly, Yves Caraglio, Christophe Jenny, Pierre Bonnet, Hervé Goëau
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6641596
- keyword hits: fine-tuning, foundation model

### abstract

Distinguishing plant varieties within a single species, an Ultra-Fine-Grained Visual Categorization (Ultra-FGVC) problem, remains largely unsolved under real-world agricultural conditions. While foundation models have significantly improved species-level plant identification, their ability to capture the subtle phenotypic variations that define cultivars remains unclear.In this work, we investigate which representation learning paradigm is best suited for infraspecific plant identification. We compare two approaches: (i) geometric self-supervised learning (DINOv2/v3), which learns representations by enforcing consistency across different sub-regions (patches) of the same image, and (ii) semantic alignment (BioCLIP 2), which aligns images with taxonomic textual descriptions. We further evaluate a hybrid strategy combining geometric pre-training with species-level supervised fine-tuning (Pl@ntNet), aiming to leverage the complementary strengths of both approaches. Experiments are conducted across three complementary datasets: a controlled market garden dataset (22 varieties), a participatory banana dataset (87 classes), and a grape variety dataset exhibiting a strong domain shift (34 varieties).Our results show that geometric self-supervised representations provide the most suitable foundation for ultra-fine-grained recognition, consistently outperforming semantic alignment approaches. While species-level supervision yields modest improvements, its contribution remains limited compared to the gains obtained from geometric pre-training, indicating that the discriminative signal at the varietal level is primarily morphological rather than semantic. Furthermore, domain-specific adaptation provides small but consistent gains, and naïve multi-organ aggregation can dilute discriminative signals in asymmetric taxa such as \textit{Musa} (bananas).These findings demonstrate that ultra-fine-grained crop variety identification relies primarily on geometric sensitivity, and highlight the importance of designing models and aggregation strategies that preserve fine-scale morphological information for agrobiodiversity monitoring.

---

## uid: `doi:10.2139/ssrn.6643046`

- title: Towards Data-efficient Weed Detection via Fine-Tuning Grounding DINO
- authors: Harshavardhan Subramanian, Nikita Genze, Heinz Bernhardt, Dominik G. Grimm, Florian Haselbeck
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6643046
- keyword hits: fine-tuning, foundation model

### abstract

The agricultural sector is facing the challenge of developing more sustainable plant protection methods while maintaining high productivity levels to ensure food security. Potential solutions include more targeted chemical plant protection through spot spraying and more efficient non-pesticide weed management using agricultural robots, both of which require accurate automated weed detection. While deep learning has shown strong potential for weed detection, achieving robust performance in heterogeneous real-world agricultural environments remains challenging. Moreover, training deep learning-based methods typically requires large, annotated datasets that are often lacking in agricultural settings. In this study, we focus on data efficiency, aiming to reduce the amount of data required to develop competitive deep learning-based weed detection models. To this end, we systematically analyse the performance of the pre-trained foundation model Grounding DINO under data scarcity. Using drone imagery from sorghum and maize fields, we incrementally reduce the number of samples used to fine-tune Grounding DINO and benchmark against the state-of-the-art object detectors DINO, RetinaNet and YOLO. Results on held-out testset demonstrate that Grounding DINO outperforms its comparison partners in both F1-score and Average Precision, even maintaining superior performance when fine-tuned using only one quarter of the full training data. Furthermore, we observe competitive test performance when fine-tuning Grounding DINO using samples from only a few early growth stages. In conclusion, a fine-tuned Grounding DINO model exhibits strong data efficiency behaviour, providing advantages for the development of sustainable plant protection approaches by reducing the need for labour- and time-intensive data collection.

---

## uid: `doi:10.2139/ssrn.6642164`

- title: High Level Synthesis in the Agentic Era
- authors: Zijian Ding, Yang Zou, Yizhou Sun, Jason Cong
- affiliations: not stated
- posted: 2026-04-24
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6642164
- keyword hits: agentic, large language model, llm

### abstract

High-Level Synthesis (HLS) provides a higher-level programming model for chip design, enabling implementations to be derived from algorithmic specifications, simplifying design verification. With recent advances in large language model (LLM)-based agents, there is growing interest in automating chip design directly at the RTL level, raising questions about the role of HLS in agent-driven workflows. In this work, we compare HLS- and RTL-based agentic design flows and find that HLS remains a strong abstraction, particularly for application-centric tasks. Building on this observation, we present two agent-based frameworks: AgRefactor for robust software-to-HLS refactoring using structured planning, tool integration, and self-improving memory, and ChipComposer for composing and optimizing hardware systems from tool-generated modules. Experimental results across multiple benchmarks show improvements in correctness, design quality, and optimization capability, suggesting that LLM-based agents can effectively leverage HLS abstractions to enable more scalable chip design workflows.

---

## uid: `doi:10.2139/ssrn.6436920`

- title: LegalAI: Legal Document Analysis using Clause Extract
- authors: Ashutosh Patel, Raman Kalra, Dhruv Jain, Dr. Rajni Sehgal Kaushik
- affiliations: not stated
- posted: 2026-04-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6436920
- keyword hits: fine-tuning, llama, retrieval-augmented, transformer model

### abstract

Legal document review is a me-consuming task that demands extensive domain knowledge. This paper presents LexAI, an architecture that combines a fine-tuned RoBERTabased clause extrac on model with a Retrieval-Augmented Genera on (RAG) conversa onal assistant to automate contract analysis. Users upload legal documents through a chat interface; the system extracts text, anonymizes personally iden fiable informa on using a Legal-BERT Named En ty Recogni on model, segments the text into overlapping chunks, embeds those chunks with a SentenceTransformer model, and stores the resul ng vectors in a Supabase cloud database. A locally hosted LLaMA3 model via Ollama generates answers grounded exclusively in retrieved context. In parallel, a RoBERTa Ques on-Answering model, fine-tuned on the Contract Understanding A cus Dataset (CUAD), iden fies and presents up to 41 dis nct clause types to the user separately in the interface. The backend is built on FastAPI with MySQL for rela onal data and JWT-based authen ca on. Experimental evalua ons on the CUAD dataset demonstrate clause detec on rates exceeding 80% across evaluated clause categories. This paper details the system architecture, the technologies employed, the fine-tuning methodology, and the evalua on results.

---

## uid: `doi:10.2139/ssrn.6643475`

- title: PD-CLIP: A contrastive language-image pre-training framework for zero-shot fine-grained plant disease diagnosis
- authors: Pengyao Xie, Xingjian Li, Weilong He, Inga Meadows, Lirong Xiang
- affiliations: not stated
- posted: 2026-04-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6643475
- keyword hits: fine-tuning, large language model, large language models

### abstract

Accurate plant disease characterization is pivotal for precision agriculture, yet current deep learning approaches are constrained by costly real-world annotations, data scarcity, and the inherent “closed-set” limitations of traditional classifiers. Moreover, existing systems typically struggle to simultaneously resolve local lesion details and global canopy distribution patterns under zero-shot settings. To address these challenges, we present PD-CLIP, a plant disease contrastive language-image pre-training framework. Utilizing Unreal Engine 5 3D physical simulation, we constructed a synthetic dataset encompassing 10 tomato foliar disease categories across 7 severity levels and 4 spatial spread types, which were automatically annotated with fine-grained semantic descriptions by multimodal large language models. Our model employs a dual-stream vision architecture and a parameter-efficient fine-tuning strategy via low-rank adaptation to map multi-scale visual and textual features into independent diagnostic subspaces. To overcome sim-to-real distribution shifts, we developed a composite domain adaptation module integrating Fourier transform-based domain adaptation, real-world anchor data guidance, and entropy minimization. Evaluated through a leave-one-out cross-validation strategy, PD-CLIP demonstrated strong cross-domain zero-shot capabilities. On unseen real-world field images, the domain-adapted model achieved a disease type classification accuracy of 0.575, a spread type identification accuracy of 0.992, and severity grading with a mean absolute error of 0.818. By effectively characterizing disease types, severity, and spread types without requiring explicit real-world annotations for the target pathogens, this approach bridges the sim-to-real gap, offering an open-vocabulary solution for crop health monitoring.

---

## uid: `doi:10.2139/ssrn.6437578`

- title: LegalAI: Legal Document Analysis
- authors: Ashutosh Patel, Dhruv Jain, Raman Kalra, Dr. Rajni Sehgal Kaushik
- affiliations: not stated
- posted: 2026-04-25
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6437578
- keyword hits: fine-tuning, llama, retrieval-augmented, transformer model

### abstract

Legal document review is a me-consuming task that demands extensive domain knowledge. This paper presents LexAI, an architecture that combines a fine-tuned RoBERTabased clause extrac on model with a Retrieval-Augmented Genera on (RAG) conversa onal assistant to automate contract analysis. Users upload legal documents through a chat interface; the system extracts text, anonymizes personally iden fiable informa on using a Legal-BERT Named En ty Recogni on model, segments the text into overlapping chunks, embeds those chunks with a SentenceTransformer model, and stores the resul ng vectors in a Supabase cloud database. A locally hosted LLaMA3 model via Ollama generates answers grounded exclusively in retrieved context. In parallel, a RoBERTa Ques on-Answering model, fine-tuned on the Contract Understanding A cus Dataset (CUAD), iden fies and presents up to 41 dis nct clause types to the user separately in the interface. The backend is built on FastAPI with MySQL for rela onal data and JWT-based authen ca on. Experimental evalua ons on the CUAD dataset demonstrate clause detec on rates exceeding 80% across evaluated clause categories. This paper details the system architecture, the technologies employed, the fine-tuning methodology, and the evalua on results.

---

## uid: `doi:10.2139/ssrn.6661512`

- title: An Explainable AI Partner Framework with Web Beacons and DeepSeek: Engineering Applications in Intelligent Library Services
- authors: ningxian zhu
- affiliations: not stated
- posted: 2026-04-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6661512
- keyword hits: deepseek, fine-tuning, large language model

### abstract

The inherent conflict between the need for real-time adaptation, the demand for interpretability, and the reality of sparse interaction data defines a core challenge for today's information systems. Traditional methods have problems such as lack of interpretability, low sample efficiency, and instability of long-range reasoning, which limit real-world application.We propose a new engineering architecture, which integrates web beacon real-time behavior perception, large language model prompt word generation, and OpenClaw. The core innovation is an interaction-guided prompt generation mechanism, which transforms user behavior and item attributes into structured natural language prompt words and can achieve task alignment without fine-tuning. The Model Context Protocol (MCP) connects the OpenClaw runtime with heterogeneous data sources through a unified interface, while the five-layer architecture ensures the system's robust generalizability.We validate this architecture in an intelligent library service. Experiments on 15,000 users, 6,000 resources, 689 profiles, and 600 AI partners we obtain: prompt quality 4.3/5.0; user satisfaction of +9.2% vs. deep learning baseline; CTR 24.56% and reading completion 75.10%; 4× sample efficiency and 57.99% gain in recommendation quality; higher task completion (+13.6%), lower response time (-24.5%), and +80% computational efficiency.The principal engineering contribution is to realize the efficient integration of an adaptive recommendation system through the long-term personalized agent mechanism. The code and data have been disclosed.

---

## uid: `doi:10.2139/ssrn.6660120`

- title: Can AI Agents have Rights?
- authors: Anna Su, Sue Anne Teo
- affiliations: not stated
- posted: 2026-04-27
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6660120
- keyword hits: ai agent, generative ai

### abstract

AI agents are rapidly moving from theoretical constructs to real-world deployments. This raises urgent questions about governance and, more specifically, rights. While rights for artificial agents have received some scholarly attention, the question of rights for AI agents understood through the paradigmatic shift introduced by generative AI remains underexamined. This article addresses that gap. We develop four theoretical pathways through which rights for AI agents might be recognized. The derivative argument draws on the legal and moral foundations of agency law and tests their applicability to AI agents. The diffusion argument holds that AI agents' deep embeddedness in social life creates pressure to render their actions legible within existing frameworks of responsibility and liability. The distinction argument examines whether AI agents possess capacities-including a potential role in resolving collective action problems requiring high levels of social coordination-that independently justify rights recognition. The devolution argument frames rights as a counterweight to the concentration of corporate power over AI systems. A central contribution of this analysis is decoupling the question of AI rights from moral personhood and its associated qualities, such as sentience and consciousness. We also address three objections: that AI rights would dilute human rights, generate a problematic proliferation of rights, and that regulatory goals could be achieved through legal duties alone. As AI agents become increasingly embedded in social, professional, and political life, questions about their rights will inevitably arise. This article offers a more nuanced framework for addressing them.

---
