# Classification batch 99 of 423, edition 3

Read prompts/classify.md before answering. Write your answer to
`data/runs/edition-003/batch-99.answer.json` as a JSON array.

---

## uid: `doi:10.2139/ssrn.6919419`

- title: Designing for Structural AI Failure: Interface Stress Testing the Gap Between AI Capability Claims and Grounded Reality
- authors: Peter Zakrzewski
- affiliations: not stated
- posted: 2026-06-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6919419
- keyword hits: foundation model, large language model, large language models

### abstract

Current multimodal AI systems exhibit reproducible, diagnosable architectural class failures in spatial reasoning, physical coherence, and temporal consistency. These represent hallmarks of current transformer architectures rather than model-specific artifacts. These failures are collectively described as the Inversion Error, a diagnosis independently supported by Ma et al, who report that current 3D large language models systematically fail to understand 3D spatial relationships. The failures are invisible from within the systems that produce them not only because the architecture lacks the physical grounding layer (Enactive floor) that detection would require, but because that absence is structural rather than incidental. They are visible from outside them because the embodied human observer stands on exactly that layer. This position paper proposes to exploit this diagnostic asymmetry by reorienting AI-focused Human-Computer Interaction design practice: from designing interfaces that smooth over AI failure modes, to interfaces that deliberately expose them. The Inversion Error position paper established the first designer role in this two-paper socio-technical systems research program: the socio-technical systems designer as diagnostic architect, exposing the structural condition in current transformer architectures from outside the engineering system. That paper diagnosed and named the condition; this paper proposes the intervention at the level of the second designer role. Where the diagnostic architect identifies what is wrong with the architecture, the interface designer as More Knowledgeable Other (MKO) provides what it structurally lacks: the embodied physical grounding that makes AI outputs coherent in a physical world. The mechanism for the embodied physical grounding is Reinforcement Learning from Physical Feedback (RLPF): encoding physical constraints as differentiable priors inside the neural architecture rather than imposing them as post-hoc corrections on its outputs. Building on the HCI tradition, within which screen-based interaction remains the dominant paradigm, I propose a two-phase stress testing program. Phase 1, the Spaghetti Table Protocol Challenge, operates at the screen-based level: a distributed research effort that scales diagnostic methodology across the design and HCI research communities using existing interfaces. Phase 2, the Universe Falling Apart Protocol, extends this program into embodied XR environments, grounded in the emerging premise of Human+Computer (H+C) Immersion: that the human user and the computational system can be co-present in a single environment where the symbolic and the embodied are united rather than separated by an interface layer. Where screen-based interaction exposes AI grounding failures symbolically, embodied interaction exposes them physically, generating the RLPF signal at the level of direct sensorimotor engagement. Shneiderman's principle that governance must match autonomy level provides the regulatory frame; H+C Immersion provides the ontological one. 2D screen-based HCI interface stress testing offers an excellent starting point for the methodology; 3D multimodal immersion is the next step. Drawing on the Chaos Engineering tradition in software reliability, I introduce the Chaos Monkey for the Inversion Error: a class of interface designs that leverage human embodied cognition as a diagnostic instrument for detecting AI architectural failures. I present the Spaghetti Table Protocol as a proof-of-concept screen-based stress testing methodology, reporting an aggregate diagnostic score of 4 out of 30 across three leading multimodal systems. The logged outputs of this stress testing constitute training data for RLPF: the mechanism through which the interface designer as MKO provides the physical grounding signal that current AI training pipelines do not collect. Phase 2, the Universe Falling Apart Protocol, is inspired by Philip K. Dick's argument about the ontological persistence of reality turned into a diagnostic criterion: an AI-generated environment passes the stress test if it holds together under embodied, multimodal human interaction.Together, the two phases produce the dataset and the RLPF training signal that foundation model architectures require to address the Inversion Error at the level of structure rather than output.

---

## uid: `doi:10.2139/ssrn.6944964`

- title: GridSage: A Skill-Grounded LLM Platform for Scenario-Oriented Reinforcement Learning Evaluation in Distribution Networks
- authors: Yilin Ge, Tao Qian, Hao Li, Qinran Hu, Zhenya Ji
- affiliations: not stated
- posted: 2026-06-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6944964
- keyword hits: large language model, large language models, llm, llms

### abstract

To address the challenges of complex scenario construction, high configuration overhead, and limited reproducibility in reinforcement learning (RL) studies for distribution networks, this paper proposes GridSage, an integrated platform that combines large language models (LLMs) with physics-aware power system simulation. GridSage adopts a Scenario Skill retrieval and incremental semantic editing framework, enabling users to generate customized scenarios through natural language instructions. To ensure physical validity and operational consistency, all generated scenarios are verified through topology checks, parameter-bound validation, power-flow feasibility analysis and operational constraint screening. Validated scenarios are then deployed into a vehicle-to-grid (V2G) interactive RL environment incorporating photovoltaic generation, wind power, energy storage systems, electric vehicles and distribution network operation dynamics. Built upon Gymnasium, GridSage supports the training and evaluation of mainstream RL algorithms. Experimental results show that GridSage achieves 96.0% command accuracy, 96.12% field accuracy, and 98.0% validity rate in natural-language scenario configuration, indicating that user instructions can be reliably transformed into executable and physically consistent ScenarioConfig objects. The layered safety validation further demonstrates the effectiveness of the proposed pre-execution screening mechanism, with 100.0% hard-reject recall, full coverage of seven hard-error categories, and 80.0% semantic intervention for risky executable scenarios. In the IEEE 33-bus high-PV low-load case, the training process and physical-operation feedback verify that the generated scenarios can provide an effective and reproducible environment for RL interaction and policy learning. The proposed platform provides a unified, scalable, and user-friendly testbed for human-AI collaborative experiment design in distribution networks.

---

## uid: `doi:10.2139/ssrn.6945194`

- title: Automated Vibe Coding of a Controller for Collective Adaptive Systems
- authors: Michal Töpfer, František Plášil, Tomáš Bureš, Petr Hnětynka
- affiliations: not stated
- posted: 2026-06-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6945194
- keyword hits: large language model, large language models, llm, llms

### abstract

In collective adaptive systems (CAS), the adaptation manager (AM) is responsible for updating the system’s architecture and behavior at runtime. Recent large language models (LLMs) make it appealing to generate AM code from a system specification, but ensuring correctness is challenging when the code is not manually reviewed.This paper studies fully automated LLM-driven code generation with iterative feedback (vibe coding) for AM implementation. We propose a runtime-verification feedback loop based on Functional Constraints Logic (FCL), a novel temporal logic designed to express fine-grained functional constraints over finite adaptation traces. FCL enables precise, structured violation reports that can be translated into actionable feedback for the LLM. The approach is realised in an end-to-end framework combining vibe-coding loop with feedback based on runtime verification done as part of the adaptation loop.We evaluate the approach on two CAS scenarios. The results show that verification-backed vibe coding can produce valid AMs in a small number of iterations when the functional constraints are stated precisely and violations are reported in a diagnostic form. Detailed, diagnostic feedback is key to eliciting focused code fixes from the LLM.

---

## uid: `doi:10.2139/ssrn.6946089`

- title: PromptCOVER: Prompt Copyright Protection with Value Differentiation by Homomorphic Encryption and Watermarking
- authors: Ruijie Sun, Peng Li, Xin Zheng, Yumiao Zheng
- affiliations: not stated
- posted: 2026-06-15
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6946089
- keyword hits: large language model, large language models, llm, llms

### abstract

Large language models(LLMs) have democratized visual content creation through prompts, yet expose critical copyright vulnerabilities in emerging prompt marketplaces.Professionally engineered prompts face unauthorized leakage risks during transactions, threatening the economic model of prompt-driven ecosystems.Current platforms lack systematic protections against such intellectual property breaches, jeopardizing creator revenue and marketplace integrity.To address this issue, we propose PromptCOVER, a prompt copyright protection framework designed to protect the intellectual property rights of prompt engineers and maintain the business model of prompt marketplaces.The framework includes two solutions tailored to prompts of different value.First, we adopt an encryption-based solution to ensure the secure bidirectional transmission of high-value prompts between users and models while maintaining task efficiency.Second, for general-value prompts, we propose a watermark-based solution that leverages synonym substitution to enhance model adaptability while preserving the user experience.We conducted extensive experiments on public and self-collected datasets using various LLMs, demonstrating the diverse capabilities of PromptCOVER.Compared to existing solutions, PromptCOVER improves performance in areas like encryption computation speed and watermark invisibility.These works bridge the gap between advanced AI security theory and deployable marketplace solutions, providing a scalable, efficient, and commercially viable engineering system for intellectual property protection.

---

## uid: `doi:10.2139/ssrn.6790338`

- title: Co-Construction Blindness and Asymmetric Epistemic Vulnerability in Human-LLM Interaction
- authors: Bianca Helena Ximenes
- affiliations: not stated
- posted: 2026-06-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6790338
- keyword hits: claude, large language model, llm

### abstract

This paper introduces two constructs to describe, to the best of our knowledge, a previously unnamed risk in human-LLM interaction. Co-construction blindness is the failure to recognize that LLM outputs are not independent assessments to be verified, but co-constructed artifacts shaped by the user's own inputs, accumulated history, and metadata. Every user of a conversational LLM is IN the loop, not ON ityet every deployment disclaimer positions them as external auditors. Asymmetric epistemic vulnerability describes the condition in which coconstruction blindness produces consequences of radically different magnitude depending on where in the authority structure the user sits. We argue that these constructs describe a structural inevitability, not an anomaly, using the public case of Richard Dawkins's interaction with Claude as a paradigmatic instance. We document a secondary mechanism-structural deferencethrough a first-person exchange in which a large language model concedes that it treated Dawkins more gently than warranted because his intellectual output is represented in its training data. We map the research gaps this analysis opens and call for shared terminology as a precondition for appropriate governance and design response.

---

## uid: `doi:10.2139/ssrn.6851501`

- title: Can LLMs Detect Greenwashing? Evaluating AI-Assisted Verification of Sovereign Green Bond Impact Reports in India
- authors: Harsh Singh
- affiliations: not stated
- posted: 2026-06-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6851501
- keyword hits: large language model, large language models, llm, llms

### abstract

This paper examines whether large language models (LLMs) can reliably verify sovereign green bond (SGrB) impact reports, using India's program as the empirical context. Green bonds have grown into a central mechanism for climate finance, yet the environmental claims issuers make are largely self-reported and difficult to verify at scale. Sovereign issuers face weaker market accountability than their corporate counterparts, making the absence of scalable verification infrastructure particularly consequential. We construct a 26-criterion evaluation rubric grounded in the ICMA Green Bond Principles and the Reserve Bank of India's SGrB Framework, and develop a structured pilot methodology for comparing LLM evaluations against independent human expert assessments across Indian green bond impact reports. Drawing on the ICMA Green Bond Principles, the RBI SGrB Framework, and the Climate Bonds Initiative standards, we develop a structured, replicable evaluation methodology and demonstrate its operationalization through a pilot application. Based on the epistemological constraints identified in the theoretical framework, we propose a tiered verification model distinguishing tasks suitable for AI automation from those requiring human judgment, and derive four policy recommendations for SEBI, RBI, and the Department of Economic Affairs, including a proposed AI-Assisted Preliminary Verification Protocol (APVP). Full empirical results from a large-scale application of this methodology will be reported in a subsequent study.

---

## uid: `doi:10.2139/ssrn.6952641`

- title: Large language models as efficient designers of composite wing-box structures via semantic feedback
- authors: luca pustina
- affiliations: not stated
- posted: 2026-06-16
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6952641
- keyword hits: claude, large language model, large language models, llm

### abstract

New propulsion technologies and unconventional configurations widen the aircraft design space just as certification pressure shortens conceptual loops. Sizing a composite wing box in this setting is expensive: each finite-element evaluation takes seconds to minutes, and population-based metaheuristics consume tens of thousands of them. The cost compounds when this sizing is embedded in a multidisciplinary design optimization. A general-purpose large language model (LLM) can instead drive the structural optimization loop when the feedback it receives is a structured engineering report rather than a fitness scalar. This paper introduces the Semantic Design Report, a briefing that translates each wing-box finite-element analysis into a design-variable action table, a ranked list of critical regions, a buckling-mode summary, and a per-region narrative. The LLM reads the report and proposes the next candidate design. The paper benchmarks two strategies of this optimizer, a sequential mode that refines a single candidate per iteration and a population-based mode that evaluates multiple candidates per iteration, across two hosted models (Claude Sonnet and Opus). The test case is a quasi-isotropic composite wing box of a regional aircraft, sized against stress, ply-failure and buckling constraints. The best configuration matches the genetic optimizer optimum within 2.8 percentage points of normalized mass while using 179× fewer finite-element evaluations.

---

## uid: `doi:10.2139/ssrn.6956764`

- title: Exploring the Landscape of Generative AI Guidelines in Higher Education
- authors: Suzanne de Castell, Jennifer Jenson, Irina Turnsunkulova
- affiliations: not stated
- posted: 2026-06-17
- source: SSRN
- link: https://doi.org/10.2139/ssrn.6956764
- keyword hits: chatgpt, claude, gemini, generative ai

### abstract

Since the public launch of ChatGPT in late fall 2022, and subsequent chatbot and other GenAI launches by major tech companies like Microsoft (Copilot), Google (Gemini), and Anthropic (Claude), educational institutions have scrambled to articulate a stance, both in policy and in practice, regarding AI use in education. This paper examines the proliferation of publicly available educational discourse on GenAI in higher education in Canada, analyzing the ways GenAI and its applications are framed in university policies and guidelines on appropriate uses. Immediately evident is the near absence of any formal policies on educational uses of AI, and a ubiquitous reliance on guidelines, non-enforceable regulations and directives and suggestions. Of note, too, is how much of the institutional regulatory discourse surrounding the use of AI in higher education is similar, and too often disturbingly identical, across institutions, and how much AI regulation focuses on ethical and privacy concerns, specifically plagiarism and “academic integrity”. There is a noticeable lack of practical guidance for educators on ethically and meaningfully integrating GenAI tools into curriculum, pedagogy and assessment, and no evidence that they should, or how they could. This paper’s objective is to contribute an accurate and useful description of AI regulation across Canadian universities and colleges, exploring, as well, what has been overlooked and ignored, and why that matters, thereby contributing to an urgently-needed critical and actionable dialogue about how to reconfigure and restabilize the foundations of higher education in the age of GenAI.

---
