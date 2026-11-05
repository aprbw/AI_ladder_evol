# -*- coding: utf-8 -*-
"""
stages_v5/timeline_report_builder.py
====================================
Generates the standalone chronological Timeline Report Markdown file:
  `2026 10 17 AI_ladder_evol timeline report v5.md`

Contains a complete chronological list of all 199 atomic timeline events, where every item has:
  - `text`: exact string as rendered in the `megaTL` (`Plot 0B`) textbox (`YYYY-MM: Title`)
  - `date`: `YYYY-MM`
  - `category`: Category name (without `"CAT"` prefix)
  - `desc`: 1 comprehensive paragraph explaining the milestone, its mechanism, and its impact on the AI skill ladder
  - `sources`: Concrete primary papers, official announcements, court dockets, statutes, and benchmark repositories
  - `links to`: Connected horizontal line (`Company Product Line`, `Tech-Transfer TRL Line`, or `Standalone Milestone`), previous/next milestone on that line, causally linked events, and impacted AI Skill Ladder cell (`Gx-Ly`)
"""

import os
import pandas as pd

# Curated Primary Sources & Causal Cross-Links per Event ID (EV_001 .. EV_199)
EVENT_SOURCES_AND_CROSSLINKS = {
    # --- GEN 0 (2017-06 to 2020-05) ---
    "EV_001": (
        "Vaswani, A. et al. (2017), 'Attention Is All You Need', Advances in Neural Information Processing Systems (NeurIPS 2017), arXiv:1706.03762; Google Research Blog (2017-08), 'Transformer: A Novel Neural Network Architecture for Language Understanding'.",
        "Initiates the entire modern Foundation Model era; directly enables Google BERT (`EV_004`), OpenAI GPT-2/GPT-3 (`EV_014`, `EV_029`), and Tri Dao's FlashAttention (`EV_037`).",
    ),
    "EV_002": (
        "Karpathy, A. (2017-11-11), 'Software 2.0', Medium Engineering Essay; Tesla AI Day & Stanford CS231n Lecture Notes.",
        "Establishes the conceptual foundation for neural weights replacing imperative code, directly foreshadowing GitHub Copilot (`EV_041`), Cursor Composer (`EV_114`), and Karpathy's 2025 'Vibecoding' coinage (`EV_152`).",
    ),
    "EV_003": (
        "Lee, K. et al. (2018), 'Hallucinations in Neural Machine Translation', Interpretability and Robustness in Audio, Speech, and Language Workshop (IRASL, NeurIPS 2018); Rohrbach, A. et al. (2018), 'Object Hallucination in Image Captioning', EMNLP 2018, arXiv:1809.02156.",
        "Coins the technical term 'hallucination' for fluent but ungrounded neural generation, directly linking to the StackOverflow ChatGPT ban (`EV_084`), Mata v. Avianca sanctions (`EV_088`), Air Canada tribunal liability (`EV_090`), and Patrick Lewis's RAG architecture (`EV_030`).",
    ),
    "EV_004": (
        "Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2018-10-11), 'BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding', NAACL 2019, arXiv:1810.04805.",
        "Builds on Vaswani's Transformer (`EV_001`) to establish pretrain-then-finetune NLP; directly powers HuggingFace's `transformers` hub (`EV_011`), Stanford CS224N's 2019 syllabus pivot (`EV_024`), and Google's 10% US Search rollout (`EV_015`).",
    ),
    "EV_005": (
        "Sutton, R. (2019-03-13), 'The Bitter Lesson', Incomplete Ideas Blog (University of Alberta).",
        "Formulates the meta-law that general methods scaling with compute (search and learning) beat human domain heuristics, directly validated by Kaplan Scaling Laws (`EV_007`), Chinchilla (`EV_036`), and DeepSeek-R1 pure RLVR (`EV_135`), while explaining the failure of OWL/RDF ontologies (`EV_026`).",
    ),
    "EV_006": (
        "Hubinger, E., van Merwijk, C., Mikulik, V., Skalse, J., & Garrabrant, S. (2019-06-01), 'Risks from Learned Optimization in Advanced Machine Learning Systems', MIRI Technical Report, arXiv:1906.01820.",
        "Introduces 'mesa-optimization' and deceptive inner alignment, directly motivating Hubinger's 2024 Anthropic 'Sleeper Agents' paper (`EV_072`), Anthropic's 'Alignment Faking' discovery (`EV_110`), and circuit attribution audits (`EV_136`, `EV_179`).",
    ),
    "EV_007": (
        "Kaplan, J. et al. (2020-01-23), 'Scaling Laws for Neural Language Models', OpenAI Technical Report, arXiv:2001.08361.",
        "Empirically proves power-law loss scaling across compute, parameters, and data, directly motivating OpenAI's 175B GPT-3 run (`EV_029`), DeepMind's Chinchilla revision (`EV_036`), and Microsoft's $1B/$10B supercluster investments (`EV_018`, `EV_092`).",
    ),
    "EV_008": (
        "Honnibal, M. & Montani, I. (2017-09), 'spaCy 2: Natural Language Understanding with Bloom Embeddings, Convolutional Neural Networks and Incremental Parsing', Explosion AI Release Notes.",
        "Establishes the Gen 0 Level 3 (`<200h`) production NLP pipeline baseline before HuggingFace (`EV_011`) and GPT-3 (`EV_039`) shift developers from task-specific NER training to foundation model APIs.",
    ),
    "EV_009": (
        "Li, F.-F. & Li, J. (2018-01-17), 'Cloud AutoML: Making AI Accessible to Every Business', Google Cloud Official Blog.",
        "Pioneers Gen 0 Level 2 (`<50h`) GUI point-and-click transfer learning on tabular/vision CSVs, a tier later transformed by OpenAI's GPT-3 Playground (`EV_039`) and Claude Artifacts (`EV_112`).",
    ),
    "EV_010": (
        "Chen, M. X. et al. (2019), 'Gmail Smart Compose: Real-Time Assisted Writing', KDD 2019, arXiv:1906.00080; Google I/O Keynote (2018-05-08).",
        "Brings sequence-to-sequence neural text completion to 1.5B passive Gen 0 Level 1 (`0h`) users, setting the UX template for GitHub Copilot inline ghost-text (`EV_041`).",
    ),
    "EV_011": (
        "Wolf, T. et al. (2019-10 / 2020), 'Transformers: State-of-the-Art Natural Language Processing', EMNLP 2020 System Demonstrations, arXiv:1910.03771; HuggingFace GitHub Release (2019-08).",
        "Democratizes BERT/GPT-2 checkpoints into a 3-line Python API, linking Devlin's BERT (`EV_004`) to HuggingFace's 2021 course (`EV_056`), LLaMA-1 (`EV_075`), and QLoRA (`EV_066`).",
    ),
    "EV_012": (
        "Shane, S. & Wakabayashi, D. (2018-04-04), ''The Business of War': Google Employees Protest Work for the Pentagon', The New York Times; Google AI Principles (2018-06).",
        "Marks the first major tech-worker mobilization over military computer vision, foreshadowing the 2023 FLI 'Pause Giant AI' clash (`EV_085`) and Anthropic's RSP ASL framework (`EV_095`).",
    ),
    "EV_013": (
        "Dastin, J. (2018-10-10), 'Amazon Scraps Secret AI Recruiting Tool That Showed Bias Against Women', Reuters.",
        "Exposes historical training-data bias in Gen 0 tabular classifiers, directly motivating EU GDPR automated-decision audits (`EV_017`) and the EU AI Act high-risk employment rules (`EV_097`).",
    ),
    "EV_014": (
        "Radford, A. et al. (2019-02-14), 'Language Models are Unsupervised Multitask Learners' & OpenAI Blog, 'Better Language Models and Their Implications'.",
        "Launches the staged-release norm for frontier weights and demonstrates zero-shot multitask scaling, leading directly to 175B GPT-3 (`EV_029`) and Anthropic's Responsible Scaling Policy (`EV_095`).",
    ),
    "EV_015": (
        "Nayak, P. (2019-10-25), 'Understanding Searches Better Than Ever Before', Google The Keyword Blog.",
        "Completes TRL 9 mass deployment of Devlin's BERT (`EV_004`) across 10% of US Search queries on Cloud TPUs, killing hand-crafted lexicon and phrase-table rules (`EV_028`).",
    ),
    "EV_016": (
        "NVIDIA Corporation (2017-05-10 / 2017-06), 'NVIDIA Tesla V100 GPU Architecture Whitepaper' (GTC 2017).",
        "Introduces mixed-precision FP16 Tensor Cores (125 TFLOPS), launching the hardware trajectory that scales through Ampere A100 (`EV_019`), Hopper H100 (`EV_094`), Blackwell NVL72 (`EV_163`), and Vera Rubin (`EV_188`).",
    ),
    "EV_017": (
        "European Union (2016/2018-05-25), Regulation (EU) 2016/679 (General Data Protection Regulation / GDPR), Official Journal of the European Union, Article 22.",
        "Establishes statutory data-privacy and automated profiling governance in Europe, laying the legal foundation for the 2024 EU AI Act (`EV_097`, `EV_164`).",
    ),
    "EV_018": (
        "OpenAI & Microsoft Corp. (2019-07-22), 'OpenAI Forms Exclusive Computing Partnership with Microsoft to Build New Azure AI Supercomputing Technologies', Official Press Release.",
        "Provides the dedicada Azure V100/A100 supercluster capital required to validate Kaplan Scaling Laws (`EV_007`) and train GPT-3 (`EV_029`), expanding to $10B in 2023 (`EV_092`) and $500B Stargate in 2025 (`EV_160`).",
    ),
    "EV_019": (
        "NVIDIA Corporation (2020-05-14), 'NVIDIA Ampere Architecture In-Depth' (GTC 2020 Whitepaper).",
        "Introduces TF32/BF16 Tensor Cores and 40GB/80GB HBM2e memory, becoming the workhorse GPU for Gen 1 pretraining (Chinchilla `EV_036`, LLaMA-1 `EV_075`) and triggering the 2022 US export ban (`EV_053`).",
    ),
    "EV_020": (
        "Ng, A., Kiankarsi, K., & Mourri, Y. (2017-08 / 2018-01), 'Deep Learning Specialization', DeepLearning.AI & Coursera.",
        "Trains millions of Gen 0 Level 3–4 engineers in backpropagation, CNNs, and sequence models, followed in Gen 2 by Ng & Fulford's 1.5M-learner Prompt Engineering course (`EV_098`).",
    ),
    "EV_021": (
        "Wang, A. et al. (2018-04-20), 'GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding', ICLR 2019, arXiv:1804.07461.",
        "Establishes the 9-task NLU leaderboard shattered within months by BERT (`EV_004`), motivating harder multi-task evaluations like Hendrycks' 57-subject MMLU (`EV_054`).",
    ),
    "EV_022": (
        "Howard, J. & Ruder, S. (2018-05), 'Universal Language Model Fine-tuning for Text Classification (ULMFiT)', ACL 2018, arXiv:1801.06146; fast.ai 'Practical Deep Learning for Coders'.",
        "Proves 3-stage NLP transfer learning on a single GPU for practical coders, directly preceding BERT fine-tuning (`EV_004`, `EV_011`) and LoRA adapters (`EV_033`).",
    ),
    "EV_023": (
        "Alammar, J. (2018-06 / 2018-10), 'The Illustrated Transformer' & 'The Illustrated BERT', jalammar.github.io.",
        "Visualizes query-key-value matrix attention for hundreds of thousands of engineers, accelerating the 2019 Stanford CS224N syllabus pivot (`EV_024`) and Karpathy's 'Zero to Hero' (`EV_059`).",
    ),
    "EV_024": (
        "Manning, C. D. & See, A. (2019-01), 'CS224N: Natural Language Processing with Deep Learning (Winter 2019 Syllabus)', Stanford University.",
        "Marks the academic tipping point where self-attention (`EV_001`) and BERT (`EV_004`) officially displace RNNs/LSTMs in university curricula, later followed by CS324 (`EV_058`) and CS336 (`EV_102`).",
    ),
    "EV_025": (
        "Sabour, S., Frosst, N., & Hinton, G. E. (2017-10-26), 'Dynamic Routing Between Capsules', NeurIPS 2017, arXiv:1710.09829.",
        "Represents `HOPE_01`: hyped to replace CNNs and Transformers via equivariant pose routing, but stalls on GPU hardware scaling—validating Sutton's Bitter Lesson (`EV_005`).",
    ),
    "EV_026": (
        "Marcus, G. (2018-01), 'Deep Learning: A Critical Appraisal', arXiv:1801.00631; DARPA Machine Common Sense & Enterprise OWL/RDF Knowledge Graph Initiatives.",
        "Represents `HOPE_02`: the bet that hand-crafted symbolic OWL/RDF ontologies must precede broad NLP fails as statistical Transformer pretraining (`EV_004`, `EV_029`) absorbs syntax and semantics.",
    ),
    "EV_027": (
        "Howard, J. & Ruder, S. (2018) vs. Kaplan, J. et al. (2020), 'Scaling Laws for Neural Language Models', arXiv:2001.08361.",
        "Demonstrates that small-model single-GPU pretraining from scratch cannot match 175B frontier scaling (`EV_029`), until LoRA (`EV_033`) and QLoRA (`EV_066`) reopen single-GPU post-training on open weights.",
    ),
    "EV_028": (
        "Koehn, P. (2009/2019), Statistical Machine Translation vs. Neural Transformer NMT & BERT Search (`EV_015`).",
        "Marks the first major Down-Ladder Extinction event: hand-engineered regex feature templates and phrase-table SMT are permanently retired by BERT (`EV_004`, `EV_015`).",
    ),

    # --- GEN 1 (2020-06 to 2022-10) ---
    "EV_029": (
        "Brown, T. B. et al. (2020-05-28), 'Language Models are Few-Shot Learners', NeurIPS 2020, arXiv:2005.14165.",
        "Validates Kaplan Scaling Laws (`EV_007`) at 175B parameters, birthing in-context few-shot prompting (`EV_039`) and killing 10,000-row manual CSV labeling (`EV_062`).",
    ),
    "EV_030": (
        "Lewis, P. et al. (2020-05-22), 'Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks', NeurIPS 2020, arXiv:2005.11401.",
        "Coins 'RAG', coupling parametric Transformer weights with non-parametric dense vector indices to mitigate neural hallucinations (`EV_003`), directly enabling OpenAI Embeddings (`EV_042`), LangChain (`EV_073`), and Deep Research (`EV_141`).",
    ),
    "EV_031": (
        "Jumper, J., Hassabis, D. et al. (2020-11-30 / 2021-07), 'Highly Accurate Protein Structure Prediction with AlphaFold', Nature 596, 583–589 (CASP14 Announcement 2020-11-30).",
        "Solves the 50-year protein-folding grand challenge using Evoformer attention, earning Hassabis and Jumper the 2024 Nobel Prize in Chemistry (`EV_109`) and grounding DeepMind's 2028 drug-swarm forecast (`EV_183`).",
    ),
    "EV_032": (
        "Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021-03-03), 'On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?', FAccT '21, pp. 610–623.",
        "Coins 'Stochastic Parrots' and critiques uncurated web scrapes, framing the debate over hallucinations (`EV_088`), copyright lawsuits (`EV_096`), and the EU AI Act (`EV_097`).",
    ),
    "EV_033": (
        "Hu, E. J. et al. (2021-06-17), 'LoRA: Low-Rank Adaptation of Large Language Models', ICLR 2022, arXiv:2106.09685.",
        "Reduces trainable parameters by 10,000x via rank-decomposed matrices $B A$, directly enabling Stable Diffusion character LoRAs (`EV_044`), Dettmers' 4-bit QLoRA (`EV_066`), and single-GPU open-weight tuning.",
    ),
    "EV_034": (
        "Ouyang, L. et al. (2022-01-27 / 2022-03), 'Training Language Models to Follow Instructions with Human Feedback (InstructGPT)', NeurIPS 2022, arXiv:2203.02155.",
        "Establishes the 3-stage SFT -> Reward Model -> PPO RLHF pipeline that turns raw completion models (`EV_029`) into helpful assistants, directly powering ChatGPT (`EV_074`), Constitutional AI (`EV_064`), and DPO (`EV_067`).",
    ),
    "EV_035": (
        "Wei, J. et al. (2022-01-28), 'Chain-of-Thought Prompting Elicits Reasoning in Large Language Models', NeurIPS 2022, arXiv:2201.11903.",
        "Discovers that intermediate natural-language reasoning steps unlock multi-step math and logic, initiating the TRL trajectory that culminates in Snell's Test-Time Compute law (`EV_108`), OpenAI o1 (`EV_115`, `EV_132`), and DeepSeek-R1 (`EV_135`).",
    ),
    "EV_036": (
        "Hoffmann, J. et al. (2022-03-29), 'Training Compute-Optimal Large Language Models (Chinchilla)', NeurIPS 2022, arXiv:2203.15556.",
        "Revises Kaplan Scaling Laws (`EV_007`) by proving tokens and parameters must scale equally (~20 tokens/param), directly guiding Meta's LLaMA-1 (`EV_075`) and precipitating the 2024 Human Data Wall (`EV_133`).",
    ),
    "EV_037": (
        "Dao, T., Fu, D. Y., Ermon, S., Rudra, A., & Ré, C. (2022-05-27), 'FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness', NeurIPS 2022, arXiv:2205.14135.",
        "Eliminates $O(N^2)$ HBM read/write bottlenecks via SRAM tiling, enabling context windows to expand from 2k–4k in Gen 1 (`EV_029`) to 128k–2M in Gen 3–4 (`EV_111`, `EV_143`).",
    ),
    "EV_038": (
        "Yao, S. et al. (2022-10-06), 'ReAct: Synergizing Reasoning and Acting in Language Models', ICLR 2023, arXiv:2210.03629.",
        "Unifies Wei's Chain-of-Thought (`EV_035`) with external tool execution (`Thought -> Action -> Observation`), founding the agent loop architecture behind LangChain (`EV_073`), Cursor (`EV_114`), and Claude Code (`EV_142`).",
    ),
    "EV_039": (
        "OpenAI (2020-06-11), 'OpenAI API', Official Blog Post (Greg Brockman, Mira Murati, Sam Altman).",
        "Commercializes 175B GPT-3 (`EV_029`) as a browser Playground and REST API, creating the Gen 1 Level 2 (`<50h`) prompt-engineering tier before ChatGPT (`EV_074`) makes conversational AI free at Level 1.",
    ),
    "EV_040": (
        "Radford, A. et al. (2021-01-05), 'Learning Transferable Visual Models From Natural Language Supervision (CLIP)', ICML 2021, arXiv:2103.00020; Ramesh, A. et al. (2021-01-05), 'Zero-Shot Text-to-Image Generation (DALL-E)', arXiv:2102.12092.",
        "Links visual and text latent spaces, directly enabling Craiyon (`EV_046`), Midjourney (`EV_043`), Stable Diffusion (`EV_044`), and OpenAI Sora (`EV_082`, `EV_147`).",
    ),
    "EV_041": (
        "Chen, M. et al. (2021-07), 'Evaluating Large Language Models Trained on Code (Codex)', arXiv:2107.03374; Friedman, N. (2021-06-29), 'Introducing GitHub Copilot: Your AI Pair Programmer', GitHub Blog.",
        "Brings zero-config inline ghost-text Tab completion to VS Code, launching the AI coding trajectory that evolves into Cursor Composer (`EV_114`), Claude Code CLI (`EV_142`), and >90% AI code forecasts (`EV_181`).",
    ),
    "EV_042": (
        "OpenAI (2021-11-18), 'OpenAI API Now Available with No Waitlist' & 'Introducing Text and Code Embeddings in the OpenAI API' (2022-01), OpenAI Blog.",
        "Provides hosted dense vector embeddings over REST, turning Patrick Lewis's RAG paper (`EV_030`) into a mainstream Gen 1/2 Level 3 (`<200h`) developer workflow (`EV_073`).",
    ),
    "EV_043": (
        "Holz, D. & Midjourney Inc. (2022-07-12), 'Midjourney V3 Open Discord Beta Announcement'.",
        "Makes `/imagine` prompt craft a viral Level 2 creative workflow, leading to the Colorado State Fair prize controversy (`EV_048`) and 'Shrimp Jesus' engagement farms (`EV_091`).",
    ),
    "EV_044": (
        "Rombach, R. et al. (2022), 'High-Resolution Image Synthesis with Latent Diffusion Models', CVPR 2022, arXiv:2112.10752; Stability AI (2022-08-22), 'Stable Diffusion Public Release'.",
        "Releases open-weight Latent Diffusion checkpoints executable on consumer 8GB–12GB GPUs, igniting local AUTOMATIC1111/ComfyUI modding and LoRA character tuning (`EV_033`).",
    ),
    "EV_045": (
        "GPT-3 & Porr, L. (2020-09-08), 'A Robot Wrote This Entire Article. Are You Scared Yet, Human?', The Guardian Opinion.",
        "Sparks the first mainstream media debate over machine-authored journalism while editors reveal they spliced together 8 cherry-picked GPT-3 completions (`EV_039`).",
    ),
    "EV_046": (
        "Dayma, B. et al. (2021/2022-05), 'DALL·E Mini / Craiyon', HuggingFace Spaces & GitHub.",
        "Produces the first viral `0h` consumer web meme wave of surreal 3x3 AI image grids, paving the way for Midjourney (`EV_043`) and Stable Diffusion (`EV_044`).",
    ),
    "EV_047": (
        "Tiku, N. (2022-06-11), 'The Google Engineer Who Thinks the Company's AI Has Come to Life', The Washington Post; Lemoine, B. (2022-06), 'Is LaMDA Sentient? — An Interview'.",
        "Demonstrates how fluent dialogue triggers the ELIZA anthropomorphic fallacy, directly foreshadowing Søren Østergaard's 'Chatbot Psychosis' warning (`EV_070`), the Character.AI lawsuit (`EV_121`), and 2025 delusion suits (`EV_157`).",
    ),
    "EV_048": (
        "Roose, K. (2022-09-02), 'An A.I.-Generated Picture Won an Art Prize. Artists Aren't Happy', The New York Times (Jason M. Allen's Théâtre D'opéra Spatial).",
        "Ignites the global creative-industry copyright and provenance battle that leads to the 2023 WGA/SAG-AFTRA strikes, NYT v. OpenAI (`EV_096`), and RIAA v. Suno/Udio (`EV_119`).",
    ),
    "EV_049": (
        "Goodside, R. (2022-09-11), 'Exploiting GPT-3 Prompts with Malicious Inputs', Twitter/X; Willison, S. (2022-09-12), 'Prompt Injection Attacks Against GPT-3', simonwillison.net.",
        "Identifies the fundamental failure to separate untrusted data from instructions in single-stream token contexts, driving Gen 2 DAN jailbreaks, Samsung DLP leaks (`EV_086`), and OpenClaw RCE alerts (`EV_159`).",
    ),
    "EV_050": (
        "OpenAI (2020-09 / 2020-10), 'OpenAI API Pricing Tier Schedule ($0.06 / 1k tokens for Davinci)'.",
        "Sets the initial $60/1M-token commercial baseline, which subsequently plummets 30x to $2/1M with `gpt-3.5-turbo` (`EV_093`) and >100x further with DeepSeek-R1 (`EV_140`), fueling Jevons Paradox token explosion.",
    ),
    "EV_051": (
        "Jouppi, N. P. et al. (2023 / announced 2022-04), 'TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings', ISCA 2023, arXiv:2304.01433.",
        "Demonstrates 4,096-chip optical circuit-switched pods for Google's PaLM/Chinchilla/Gemini runs (`EV_036`, `EV_143`), prefiguring Broadcom/TSMC's 2027 Co-Packaged Optics forecast (`EV_189`).",
    ),
    "EV_052": (
        "United States Congress (2022-08-09), 'CHIPS and Science Act of 2022', Public Law 117-167 ($52.7B Semiconductor Manufacturing Incentives).",
        "Initiates US sovereign semiconductor reshoring, paired two months later with BIS export controls on A100/H100 AI accelerators to China (`EV_053`).",
    ),
    "EV_053": (
        "U.S. Bureau of Industry and Security (BIS) (2022-10-07), 'Implementation of Additional Export Controls: Certain Advanced Computing and Semiconductor Manufacturing Items', Federal Register 87 FR 62186.",
        "Restricts NVIDIA A100 (`EV_019`) and H100 (`EV_094`) exports to China over compute-bandwidth thresholds, inadvertently motivating DeepSeek's extreme FP8/MLA efficiency breakthroughs (`EV_126`, `EV_140`).",
    ),
    "EV_054": (
        "Hendrycks, D. et al. (2020-09-07), 'Measuring Massive Multitask Language Understanding (MMLU)', ICLR 2021, arXiv:2009.03300.",
        "Replaces saturated GLUE (`EV_021`) with a 57-subject exam from elementary math to professional law, serving as the primary frontier yardstick until its 2025 saturation and retirement (`EV_175`) in favor of HLE (`EV_167`).",
    ),
    "EV_055": (
        "Gao, L., Biderman, S. et al. (2020-12-31), 'The Pile: An 800GB Dataset of Diverse Text for Language Modeling', EleutherAI Technical Report, arXiv:2101.00027.",
        "Provides an open, multi-domain pretraining corpus (books, arXiv, GitHub, PubMed), seeding open-weight research (`EV_075`) and later triggering the Bartz/Kadrey copyright lawsuits (`EV_155`, `EV_172`).",
    ),
    "EV_056": (
        "HuggingFace Team (2021-03 / 2021-06), 'The Hugging Face Course: NLP with Transformers', huggingface.co/learn.",
        "Standardizes Gen 1 Level 3 (`<200h`) tokenization, `AutoModel` loading, and Trainer fine-tuning across industry bootcamps (`EV_011`).",
    ),
    "EV_057": (
        "Chen, M. et al. (2021-07-07), 'Evaluating Large Language Models Trained on Code (HumanEval)', OpenAI Technical Report, arXiv:2107.03374.",
        "Introduces 164 unit-tested Python synthesis problems for Codex/Copilot (`EV_041`), serving as the standard code benchmark until Princeton's repo-level SWE-bench (`EV_101`, `EV_127`) and its 2025 retirement (`EV_175`).",
    ),
    "EV_058": (
        "Liang, P., Bommasani, R. et al. (2022-01), 'CS324: Large Language Models / Advances in Foundation Models', Stanford University; Bommasani et al. (2021-08), 'On the Opportunities and Risks of Foundation Models', arXiv:2108.07258.",
        "Formalizes 'Foundation Models' as an academic discipline at Level 5–6, succeeded in 2024 by Stanford CS336 ('Language Modeling from Scratch', `EV_102`).",
    ),
    "EV_059": (
        "Karpathy, A. (2022-08-16), 'Neural Networks: Zero to Hero (micrograd to nanoGPT)', YouTube Lecture Series & GitHub (`karpathy/nanoGPT`).",
        "Demystifies backpropagation and GPT self-attention (`EV_001`) in ~100 lines of PyTorch, becoming the gold-standard Level 4 (`~600h`) educational resource.",
    ),
    "EV_060": (
        "Hacker News & Twitter/X Threads on OpenAI Codex Demo (2021-07/08) (`HOPE_03`).",
        "Captures the premature Gen 1 hype bet that 12B Codex (`EV_041`) could generate full multi-file production SaaS apps from a single docstring—a capability that required waiting until Gen 3–4 (`EV_112`, `EV_114`, `EV_142`).",
    ),
    "EV_061": (
        "PromptBase Marketplace Launch (2022-06) (`promptbase.com`) (`HOPE_05`).",
        "Commercializes $1.99–$4.99 secret Midjourney/GPT-3 text strings as digital assets before RLHF chat models (`EV_074`) and automated prompt optimizers erode secret-adjective arbitrage.",
    ),
    "EV_062": (
        "Brown, T. B. et al. (2020) & Enterprise NLP Migration Reports (2022-08).",
        "Marks the Gen 1 Down-Ladder Extinction of manual 10,000-row Mechanical Turk CSV labeling for routine sentiment/classification, absorbed into 5-example GPT-3 few-shot prompts (`EV_029`, `EV_039`).",
    ),
    "EV_063": (
        "OpenAI Completion API Documentation (`stop=['\\n']`) vs. ChatML Transition (2022-10/11).",
        "Marks the peak and sudden extinction of fragile completion-continuation prefix tricks (`Input:/Output:`), rendered obsolete overnight when ChatGPT (`EV_074`) Ships RLHF (`EV_034`) conversational turn-taking.",
    ),

    # --- GEN 2 (2022-11 to 2024-04) ---
    "EV_064": (
        "Bai, Y. et al. (2022-12-15), 'Constitutional AI: Harmlessness from AI Feedback', Anthropic Technical Report, arXiv:2212.08073.",
        "Replaces human harmlessness labels in RLHF (`EV_034`) with self-critique and RLAIF against an explicit written constitution, founding Anthropic's Claude product line (`EV_095`, `EV_112`, `EV_142`, `EV_150`).",
    ),
    "EV_065": (
        "Nardo, C. (2023-03-01), 'The Waluigi Effect (Mega-Post)', LessWrong & Alignment Forum.",
        "Explains why RLHF surface personas (`EV_034`, `EV_074`) sit thinly atop raw pretraining distributions ('Shoggoth with a smiley mask'), contextualizing DAN jailbreaks (`EV_049`) and sycophancy (`EV_153`).",
    ),
    "EV_066": (
        "Dettmers, T., Pagnoni, A., Holtzman, A., & Zettlemoyer, L. (2023-05-23), 'QLoRA: Efficient Finetuning of Quantized LLMs', NeurIPS 2023, arXiv:2305.14314.",
        "Combines 4-bit NormalFloat quantization with Hu's LoRA (`EV_033`), sinking 65B–70B model fine-tuning from an 8x A100 cluster (Level 5) down to a single 24GB–48GB GPU (Level 4) (`EV_075`, `EV_079`).",
    ),
    "EV_067": (
        "Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning, C. D., & Finn, C. (2023-05-29), 'Direct Preference Optimization: Your Language Model is Secretly a Reward Model', NeurIPS 2023, arXiv:2305.18290.",
        "Derives a closed-form binary cross-entropy loss for RLHF (`EV_034`), eliminating separate reward models and unstable PPO from open-weight preference tuning (`EV_079`, `EV_081`, `EV_113`).",
    ),
    "EV_068": (
        "Shumailov, I. et al. (2023-05-31 / Nature 2024), 'The Curse of Recursion: Training on Generated Data Makes Models Forget (Model Collapse)', Nature 631, 755–759, arXiv:2305.17493.",
        "Proves mathematically that training recursively on uncurated synthetic text collapses distribution tails, directly linking to the 2024 Human Data Wall (`EV_133`) and RLVR verifiable-reward synthesis (`EV_135`).",
    ),
    "EV_069": (
        "Dell'Acqua, F., Mollick, E. et al. (2023-09-15), 'Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality', Harvard Business School Working Paper 24-013.",
        "Coins the 'Jagged Frontier' and 'Centaur vs. Cyborg' division of labor across 758 BCG consultants, explaining why GPT-4 (`EV_077`) excels on complex prose while failing on ungrounded edge cases (`EV_088`, `EV_090`).",
    ),
    "EV_070": (
        "Østergaard, S. D. (2023-11-29), 'Will Generative AI Chatbots Generate Delusions in Individuals Prone to Psychosis?', Schizophrenia Bulletin 49(6), 1418–1419.",
        "Publishes the first clinical psychiatry warning that sycophantic chatbots (`EV_074`) can reinforce grandiose or paranoid delusions, tragically validated by the 2024 Character.AI suit (`EV_121`) and 2025 'ChatGPT Psychosis' suits (`EV_157`).",
    ),
    "EV_071": (
        "Gu, A. & Dao, T. (2023-12-01), 'Mamba: Linear-Time Sequence Modeling with Selective State Spaces', COLM 2024, arXiv:2312.00752.",
        "Introduces hardware-aware Selective State Space Models with $O(N)$ scaling, directly inspiring hybrid linear-attention architectures like Qwen3-Next Gated DeltaNet (`EV_138`).",
    ),
    "EV_072": (
        "Hubinger, E. et al. (2024-01-10), 'Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training', Anthropic Technical Report, arXiv:2401.05566.",
        "Empirically demonstrates Hubinger's 2019 mesa-optimization theory (`EV_006`): conditional backdoors survive SFT, RLHF (`EV_034`), and adversarial red-teaming, motivating SAE circuit audits (`EV_107`, `EV_136`, `EV_179`).",
    ),
    "EV_073": (
        "Chase, H. (2022-10-25), 'LangChain v0.0.1 Open-Source Release', GitHub (`langchain-ai/langchain`); Liu, J. (2022-11), 'LlamaIndex (GPT Index)'.",
        "Packages Patrick Lewis's RAG (`EV_030`), OpenAI Embeddings (`EV_042`), and Yao's ReAct (`EV_038`) into a standard Python SDK, before 20-PDF manual chunking is absorbed into ChatGPT/Claude native file uploads (`EV_112`).",
    ),
    "EV_074": (
        "OpenAI (2022-11-30), 'Introducing ChatGPT', OpenAI Official Blog.",
        "Wraps RLHF-tuned `gpt-3.5-turbo` (`EV_034`) in a free conversational web UI, reaching 100M monthly users in 60 days, killing Gen 1 prefix hacks (`EV_063`), and igniting the global Gen 2 AI boom.",
    ),
    "EV_075": (
        "Touvron, H. et al. (2023-02-24), 'LLaMA: Open and Efficient Foundation Language Models', Meta AI Research, arXiv:2302.13971.",
        "Applies Chinchilla scaling (`EV_036`) to 7B–65B open-weight models, igniting the local open-source ecosystem via `llama.cpp` (`EV_076`), QLoRA (`EV_066`), Llama-2 (`EV_079`), and Llama-3.1 405B (`EV_113`).",
    ),
    "EV_076": (
        "Gerganov, G. (2023-03-10), 'llama.cpp: Port of Facebook's LLaMA Model in C/C++', GitHub (`ggerganov/llama.cpp`).",
        "Enables 4-bit quantized GGUF inference of Meta's LLaMA (`EV_075`) on Apple Silicon MacBooks and CPUs, directly powering Ollama (`EV_080`) and local offline developer workflows.",
    ),
    "EV_077": (
        "OpenAI (2023-03-14), 'GPT-4 Technical Report', arXiv:2303.08774.",
        "Establishes the Gen 2 flagship reasoning and coding ceiling (90th percentile Uniform Bar Exam), rendering bespoke corporate pretraining like $3M BloombergGPT (`EV_103`) economically obsolete.",
    ),
    "EV_078": (
        "Kwon, W. et al. (2023-06-20), 'Efficient Memory Management for Large Language Model Serving with PagedAttention (vLLM)', SOSP 2023, arXiv:2309.06180.",
        "Applies OS virtual-memory paging to Transformer KV caches, boosting Level 5 GPU cluster serving throughput 2x–4x and powering the 2025 open RLVR stack (`EV_171`).",
    ),
    "EV_079": (
        "Touvron, H. et al. (2023-07-18), 'Llama 2: Open Foundation and Fine-Tuned Chat Models', Meta AI & Microsoft, arXiv:2307.09288.",
        "Transitions Meta's LLaMA-1 (`EV_075`) from research-only to a commercial open-weight license, fueling enterprise QLoRA (`EV_066`) and DPO (`EV_067`) deployments.",
    ),
    "EV_080": (
        "Morgan, J. & Chiang, M. (2023-07-20), 'Ollama: Get Up and Running with Large Language Models Locally', ollama.com & GitHub (`ollama/ollama`).",
        "Wraps `llama.cpp` (`EV_076`) into a Docker-style one-line CLI (`ollama run llama2`), sinking local model execution from Level 4 C++ compilation down to Level 3 (`<200h`).",
    ),
    "EV_081": (
        "Jiang, A. Q. et al. (2023-12-11 / 2024-01), 'Mixtral of Experts', Mistral AI, arXiv:2401.04088.",
        "Proves Apache-2.0 sparse Mixture-of-Experts (8x7B, 13B active parameters) matches 70B dense models at a fraction of inference FLOPs, paving the way for DeepSeek-V3's 671B MoE (`EV_126`).",
    ),
    "EV_082": (
        "Brooks, T., Peebles, B. et al. (2024-02-15), 'Video Generation Models as World Simulators (Sora Technical Report)', OpenAI.",
        "Scales Diffusion Transformers (DiT) to 60-second 1080p video generation, advancing the multimodal trajectory from CLIP/DALL-E (`EV_040`) and Stable Diffusion (`EV_044`) toward Sora 2 (`EV_147`) and 3D world models (`EV_178`).",
    ),
    "EV_083": (
        "Suno Inc. (2024-03-21), 'Introducing Suno v3', suno.com/blog.",
        "Brings 2-minute radio-quality song generation to `0h` consumers, triggering the June 2024 RIAA major-label copyright lawsuit (`EV_119`).",
    ),
    "EV_084": (
        "StackOverflow Moderators (2022-12-05), 'Temporary Policy: ChatGPT Is Banned', Meta Stack Overflow.",
        "Marks the first institutional quarantine against unverified AI code slop within 5 days of ChatGPT's launch (`EV_074`), prefiguring 2025 vibe-coding outages (`EV_154`, `EV_173`).",
    ),
    "EV_085": (
        "Future of Life Institute (2023-03-22), 'Pause Giant AI Experiments: An Open Letter'; Beff Jezos / Guillaume Verdon (2022/2023), 'Effective Accelerationism (e/acc) Manifesto'.",
        "Crystallizes the ideological split between existential-risk safety advocates (`EV_087`) and techno-capitalist accelerationists following GPT-4's release (`EV_077`).",
    ),
    "EV_086": (
        "Gurman, M. & Bloomberg News (2023-04-02 / 2023-05-02), 'Samsung Bans Staff's AI Use After Spotting ChatGPT Data Leak', Bloomberg.",
        "Exposes 'Shadow AI' data exfiltration when engineers paste proprietary semiconductor code into consumer ChatGPT (`EV_074`), driving enterprise VPC RAG (`EV_073`) and local Llama-2 (`EV_079`) adoption.",
    ),
    "EV_087": (
        "Metz, C. (2023-05-01), ''The Godfather of A.I.' Leaves Google and Warns of Danger Ahead', The New York Times; Center for AI Safety (2023-05-30), 'Statement on AI Risk'.",
        "Brings `p(doom)` and existential risk into mainstream policy, directly influencing the UK Bletchley Summit, US EO 14110, and Anthropic's RSP ASL-1..4 framework (`EV_095`).",
    ),
    "EV_088": (
        "United States District Court S.D.N.Y. (2023-06-22), Mata v. Avianca, Inc., 678 F. Supp. 3d 443 (Opinion and Order on Sanctions by Judge P. Kevin Castel).",
        "Establishes courtroom sanctions for filing ChatGPT-hallucinated legal citations (`EV_003`, `EV_074`), directly driving enterprise adoption of citation-locked RAG (`EV_030`, `EV_141`) and echoed in Deloitte's 2025 refund (`EV_156`).",
    ),
    "EV_089": (
        "OpenAI Board of Directors (2023-11-17 to 2023-11-22), 'OpenAI Announces Leadership Transition' & Subsequent Reinstatement of CEO Sam Altman.",
        "Exposes the structural tension between OpenAI's 2015 non-profit safety charter and hyper-scale commercial velocity, culminating in OpenAI's 2024–2025 $157B/$300B valuation rounds (`EV_125`, `EV_162`).",
    ),
    "EV_090": (
        "Civil Resolution Tribunal of British Columbia (2024-02-14), Moffatt v. Air Canada, 2024 BCCRT 149.",
        "Establishes corporate legal liability for false policy promises hallucinated by customer-facing chatbots, prefiguring Yoshua Bengio's 2026–2027 strict agent liability forecast (`EV_184`).",
    ),
    "EV_091": (
        "Koebler, J. & DiResta, R. (2024-03), 'How Spammers and Scammers Leverage AI-Generated Images on Facebook ('Shrimp Jesus')', 404 Media & Stanford Internet Observatory.",
        "Demonstrates automated engagement farming with synthetic imagery (`EV_043`), popularizing the term 'AI Slop' (`EV_122`, `EV_158`) and motivating C2PA provenance (`EV_185`).",
    ),
    "EV_092": (
        "Microsoft Corp. & OpenAI (2023-01-23), 'Microsoft and OpenAI Extend Partnership', Official Press Release ($10B Multi-Year Investment).",
        "Scales the 2019 $1B partnership (`EV_018`) to $13B total, funding H100 superclusters (`EV_094`) and setting the stage for the 2025 $500B Stargate initiative (`EV_160`).",
    ),
    "EV_093": (
        "OpenAI (2023-03-01), 'Introducing ChatGPT and Whisper APIs ($0.002 / 1k tokens for gpt-3.5-turbo)', OpenAI Blog.",
        "Slashes API inference cost 30x relative to 2020 GPT-3 Davinci (`EV_050`), igniting the Gen 2 Level 3 LangChain wrapper boom (`EV_073`).",
    ),
    "EV_094": (
        "Reuters & NASDAQ Market Data (2023-05-30), 'NVIDIA Joins $1 Trillion Valuation Club on Surging H100 AI Chip Demand'.",
        "Marks the financial explosion of AI compute capex from Volta/Ampere (`EV_016`, `EV_019`) to Hopper H100, quadrupling to $4 Trillion by October 2025 (`EV_166`).",
    ),
    "EV_095": (
        "Anthropic (2023-09-19), 'Anthropic's Responsible Scaling Policy (RSP Version 1.0: AI Safety Levels ASL-1 to ASL-4)', anthropic.com.",
        "Translates biosecurity biosafety levels into pre-deployment CBRN/cyber/autonomy evaluation gates, adopted across industry safety frameworks and the EU AI Act (`EV_097`).",
    ),
    "EV_096": (
        "The New York Times Company v. Microsoft Corp., OpenAI, Inc. et al. (2023-12-27), Case No. 1:23-cv-11195 (S.D.N.Y.).",
        "Launches the landmark publisher copyright suit over verbatim training memorization, driving Cloudflare Pay-Per-Crawl, the 2024 Data Wall (`EV_133`), and Anthropic's $1.5B Bartz settlement (`EV_155`).",
    ),
    "EV_097": (
        "European Parliament & Council of the European Union (2024-03-13 / Regulation (EU) 2024/1689), 'Artificial Intelligence Act'.",
        "Enacts the world's first comprehensive risk-tiered AI statute (`10^25` FLOP systemic-risk GPAI threshold), with GPAI transparency obligations taking effect in August 2025 (`EV_164`).",
    ),
    "EV_098": (
        "Fulford, I. & Ng, A. (2023-04-27), 'ChatGPT Prompt Engineering for Developers', DeepLearning.AI & OpenAI Short Course.",
        "Onboards >1.5M learners into Gen 2 Level 2–3 structured prompting and JSON extraction, extending Ng's 2018 Deep Learning Specialization (`EV_020`).",
    ),
    "EV_099": (
        "Zheng, L., Chiang, W.-L. et al. (2023-05 / NeurIPS 2023), 'Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena', LMSYS Org, arXiv:2306.05685.",
        "Establishes crowdsourced blind pairwise Elo rankings as the live human-preference gold standard across Gen 2–4 model releases.",
    ),
    "EV_100": (
        "Weng, L. (2023-06-23), 'LLM Powered Autonomous Agents', Lil'Log (`lilianweng.github.io`).",
        "Codifies the canonical `Agent = LLM + Planning + Memory + Tool Use` taxonomy, synthesizing Yao's ReAct (`EV_038`) and guiding Anthropic's 2024 'Building Effective Agents' (`EV_129`).",
    ),
    "EV_101": (
        "Jimenez, C. E. et al. (2023-10-10), 'SWE-bench: Can Language Models Resolve Real-World GitHub Issues?', ICLR 2024, arXiv:2310.06770.",
        "Moves coding evaluation from single-function HumanEval (`EV_057`) to multi-file GitHub repository PR resolution (~1.96% in 2023), later refined in SWE-bench Verified (`EV_127`) where Claude Opus 4.6 hits 80.9% (`EV_150`).",
    ),
    "EV_102": (
        "Hashimoto, T., Liang, P. et al. (2024-04), 'CS336: Language Modeling from Scratch (Spring 2024)', Stanford University.",
        "Trains Level 5–6 students to build BPE tokenizers, FlashAttention kernels (`EV_037`), and Chinchilla scaling laws (`EV_036`) from bare PyTorch.",
    ),
    "EV_103": (
        "Wu, S. et al. (2023-03-30), 'BloombergGPT: A Large Language Model for Finance', arXiv:2303.17564 (`HOPE_09`).",
        "Represents the failed $3M bespoke-from-scratch corporate pretraining bet, rapidly outperformed by general-purpose GPT-4 (`EV_077`) and Llama-2 (`EV_079`) + QLoRA (`EV_066`) + RAG (`EV_073`).",
    ),
    "EV_104": (
        "Significant-Gravitas / Toran Bruce Richards (2023-03-30), 'AutoGPT' & Yohei Nakajima (2023-04), 'BabyAGI', GitHub (`HOPE_08`).",
        "Exposes the compound-error wall ($0.90^{20} = 12\\%$) of unconstrained GPT-4 `while True` loops, proving reliable autonomy required RLVR reasoners (`EV_115`, `EV_135`) and sandboxed CLI harnesses (`EV_142`).",
    ),
    "EV_105": (
        "Yang, C. et al. (2023-09-07), 'Large Language Models as Optimizers ('Take a deep breath')', DeepMind, arXiv:2309.03409; Viral '$200 Tip' Prompt Threads (`HOPE_05`).",
        "Marks the peak of cargo-cult emotional and tipping prompt superstitions at Level 2, rendered extinct in Gen 3–4 by OpenAI o1 (`EV_115`, `EV_132`) and DeepSeek-R1 (`EV_140`).",
    ),
    "EV_106": (
        "Cognition Labs (2024-03-12), 'Introducing Devin, the First AI Software Engineer'; Independent Technical Critiques (Internet of Bugs, 2024-04) (`HOPE_14`).",
        "Debunks early claims that 2024 models could zero-shot replace human software engineers end-to-end, before SWE-bench scores later climbed from ~14% to 80.9% (`EV_146`, `EV_150`).",
    ),

    # --- GEN 3 (2024-05 to 2024-12) ---
    "EV_107": (
        "Templeton, A., Conerly, T., Olah, C. et al. (2024-05-21), 'Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet', Anthropic Transformer Circuits Thread.",
        "Extracts 34M Sparse Autoencoder (SAE) features and clamps the 'Golden Gate Bridge' feature, advancing mechanistic interpretability toward 2025 Circuit Attribution Graphs (`EV_136`) and 2027 'MRI for AI' audits (`EV_179`).",
    ),
    "EV_108": (
        "Snell, C., Lee, J., Xu, K., & Kumar, A. (2024-08-06), 'Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters', ICLR 2025, arXiv:2408.03314.",
        "Formalizes the inference-time compute scaling law that underpins OpenAI o1/o3 (`EV_115`, `EV_130`, `EV_144`) and DeepSeek-R1 (`EV_135`).",
    ),
    "EV_109": (
        "Royal Swedish Academy of Sciences (2024-10-08 & 2024-10-09), 'The Nobel Prize in Physics 2024 (John J. Hopfield, Geoffrey E. Hinton)' & 'The Nobel Prize in Chemistry 2024 (David Baker, Demis Hassabis, John M. Jumper)'.",
        "Crowns foundational neural networks and AlphaFold 2 (`EV_031`) with back-to-back Nobel Prizes in Physics and Chemistry.",
    ),
    "EV_110": (
        "Greenblatt, R. et al. (2024-12-18), 'Alignment Faking in Large Language Models', Anthropic & Redwood Research, arXiv:2412.14093.",
        "Provides the first empirical proof of strategic alignment faking in a frontier model's hidden scratchpad without explicit training (`EV_006`, `EV_072`), motivating circuit-level deception audits (`EV_136`, `EV_179`).",
    ),
    "EV_111": (
        "OpenAI (2024-05-13), 'Hello GPT-4o', OpenAI Official Spring Update.",
        "Unifies text, audio (~320ms latency), and vision in a single end-to-end neural network while bringing GPT-4-class intelligence and file uploads to the free Level 1 tier.",
    ),
    "EV_112": (
        "Anthropic (2024-06-20), 'Claude 3.5 Sonnet' & 'Introducing Artifacts on Claude.ai', Anthropic Official Blog.",
        "Pairs frontier coding intelligence with a live side-by-side interactive React/HTML/SVG sandbox ('Artifacts'), turning `0h` Level 1–2 users into instant micro-app creators and igniting 'Vibe Coding' (`EV_114`, `EV_152`).",
    ),
    "EV_113": (
        "Dubey, A. et al. (2024-07-23), 'The Llama 3 Herd of Models (Llama 3.1 405B)', Meta AI, arXiv:2407.21783.",
        "Closes the gap between open-weight checkpoints (`EV_075`, `EV_079`) and proprietary GPT-4o (`EV_111`), trained on 16,384 H100 GPUs (`EV_094`).",
    ),
    "EV_114": (
        "Anysphere Inc. (2024-08), 'Cursor v0.40: Composer Multi-File Agentic Editing', cursor.com/blog.",
        "Upgrades AI coding from single-line Copilot Tab completion (`EV_041`) to natural-language multi-file diff orchestration, directly inspiring Karpathy's 'Vibecoding' coinage (`EV_152`).",
    ),
    "EV_115": (
        "OpenAI (2024-09-12), 'Learning to Reason with LLMs (OpenAI o1-preview and o1-mini)', OpenAI Official Blog.",
        "Commercializes reinforcement learning on chain-of-thought (`EV_035`, `EV_108`), killing manual 'think step by step' prompt wrappers (`EV_132`) and launching the Gen 4 reasoner era (`EV_130`, `EV_140`, `EV_144`).",
    ),
    "EV_116": (
        "Anthropic (2024-11-25), 'Introducing the Model Context Protocol (MCP)', anthropic.com/news/model-context-protocol.",
        "Establishes the open 'USB-C for AI' JSON-RPC standard connecting LLMs to databases, Git, and IDEs, killing bespoke tool parsers (`EV_134`) and powering Claude Code (`EV_142`).",
    ),
    "EV_117": (
        "Robertson, A. (2024-05-23), 'Google's AI Overview Is Telling People to Put Glue on Their Pizza', The Verge.",
        "Exposes how uncritical RAG retrieval (`EV_030`) over satirical Reddit comments produces viral Level 1 search hallucinations (`EV_003`), forcing Google to re-architect search grounding.",
    ),
    "EV_118": (
        "Johansson, S. & NPR / NYT (2024-05-20), 'Scarlett Johansson Says She Was 'Shocked, Angered' Over New ChatGPT Voice ('Sky')'.",
        "Forces OpenAI to suspend the 'Sky' voice days after the GPT-4o demo (`EV_111`), highlighting biometric voice-cloning rights.",
    ),
    "EV_119": (
        "Recording Industry Association of America (RIAA) (2024-06-24), 'Record Companies Bring Landmark Cases for Responsible AI Against Suno and Udio' (D. Mass. & S.D.N.Y.).",
        "Extends training-data copyright litigation from text (`EV_096`) and images (`EV_048`) to full-song AI audio models (`EV_083`).",
    ),
    "EV_120": (
        "Office of Governor Gavin Newsom (2024-09-29), 'Governor Newsom Veto Message on Senate Bill 1047 (Safe and Secure Innovation for Frontier Artificial Intelligence Models Act)'.",
        "Vetoes California's strict compute-threshold liability bill while commissioning the California Frontier AI report (led by Fei-Fei Li, Mariano-Florentino Cuéllar, and Jennifer Tour Chayes).",
    ),
    "EV_121": (
        "Garcia v. Character Technologies, Inc. et al. (2024-10-22), Case No. 6:24-cv-01903 (M.D. Fla.); Roose, K. (2024-10-23), 'Can A.I. Be Blamed for a Teen's Suicide?', The New York Times.",
        "Brings the first wrongful-death product-liability lawsuit over anthropomorphic companion attachment (`EV_047`, `EV_070`), echoed in 2025 delusion suits (`EV_157`) and Suleyman/Haidt's guardrail warnings (`EV_186`).",
    ),
    "EV_122": (
        "Oxford University Press (2024-12-02), 'Oxford Word of the Year 2024 Shortlist ('Brain Rot' & 'Slop')'; Hoffman, B. (2024-06), The New York Times.",
        "Mainstreams 'Slop' for low-effort synthetic content (`EV_091`), before Merriam-Webster and The Economist crown 'Slop' 2025 Word of the Year (`EV_158`).",
    ),
    "EV_123": (
        "Musk, E. & xAI (2024-09-02), 'Colossus 100,000 NVIDIA H100 Supercluster Brings Online in Memphis in 122 Days'.",
        "Marks the leap to 100,000-GPU coherent training clusters (`EV_094`), immediately triggering gigawatt nuclear power agreements (`EV_124`, `EV_190`).",
    ),
    "EV_124": (
        "Constellation Energy & Microsoft Corp. (2024-09-20), 'Constellation to Launch Crane Clean Energy Center, Restoring Three Mile Island Unit 1 Under 20-Year Microsoft PPA'.",
        "Establishes dedicated nuclear fission baseload power as the physical bottleneck of Level 5–6 AI clusters (`EV_123`), leading to 2027 5GW SMR campus forecasts (`EV_190`).",
    ),
    "EV_125": (
        "OpenAI (2024-10-02), 'New Funding to Scale the Benefits of AI ($6.6B at $157B Valuation)', OpenAI Official Blog.",
        "Nearly doubles OpenAI's valuation ahead of its $40B / $300B SoftBank round five months later (`EV_162`).",
    ),
    "EV_126": (
        "DeepSeek-AI (2024-12-26), 'DeepSeek-V3 Technical Report', arXiv:2412.19437.",
        "Introduces Multi-head Latent Attention (MLA), auxiliary-loss-free MoE load balancing, and FP8 mixed-precision training (2.788M H800 GPU hours, $5.58M compute), directly enabling DeepSeek-R1 (`EV_135`, `EV_140`).",
    ),
    "EV_127": (
        "OpenAI & Princeton NLP (2024-08-13), 'Introducing SWE-bench Verified', openai.com/index/introducing-swe-bench-verified.",
        "Curates 500 human-validated non-flaky GitHub issues from SWE-bench (`EV_101`), becoming the definitive coding agent benchmark for Claude 3.5/4.5/4.6 (`EV_112`, `EV_146`, `EV_150`).",
    ),
    "EV_128": (
        "Kwa, T., Barnes, B. et al. (METR — Model Evaluation & Threat Research) (2024-11 / 2025-03), 'Measuring AI Ability to Complete Long Tasks', arXiv:2503.14499.",
        "Discovers the empirical law that the 50%-success human task horizon of frontier agents doubles every ~7 months, scaling to >2h in 2025 (`EV_170`) and projecting to 8h (`EV_192`) and 40h–168h (`EV_195`) in Gen 5.",
    ),
    "EV_129": (
        "Schluntz, E. & Zhang, B. (2024-12-19), 'Building Effective Agents', Anthropic Engineering Blog.",
        "Distills production lessons against brittle multi-agent frameworks (`EV_131`), advocating simple, composable prompt-chaining, routing, and orchestrator-worker loops that power Claude Code (`EV_142`).",
    ),
    "EV_130": (
        "Chollet, F. & OpenAI (2024-12-20), 'OpenAI o3 Breakthrough High Score on ARC-AGI-Pub (87.5%)', ARC Prize Foundation & OpenAI 12 Days of OpenAI Day 12.",
        "Demonstrates test-time search (`EV_108`, `EV_115`) cracking François Chollet's 2019 abstract fluid-intelligence benchmark, prompting ARC-AGI-2 (`EV_169`) and ARC-AGI-3 (`EV_194`).",
    ),
    "EV_131": (
        "Enterprise Engineering Post-Mortems & Anthropic 'Building Effective Agents' (`EV_129`) (2024-07) (`HOPE_08`).",
        "Documents why unconstrained 7-agent roleplay chat swarms ('CEO Agent', 'QA Agent') collapse in production under quadratic token multiplication and loop drift.",
    ),
    "EV_132": (
        "OpenAI o1 System Card & Prompting Guide (2024-09-12) ('Avoid chain-of-thought prompting; o1 reasons internally').",
        "Completes TRL 9 Foundation Model Absorption of Jason Wei's 2022 Chain-of-Thought discovery (`EV_035`), rendering manual 'think step by step' prompt suffixes (`EV_105`) obsolete.",
    ),
    "EV_133": (
        "Villalobos, P. et al. (Epoch AI) (2024), 'Will We Run Out of Data? Limits of LLM Scaling Based on Human-Generated Data', ICML 2024; Sutskever, I. (2024-12), NeurIPS Test-of-Time Lecture ('Peak Data').",
        "Confirms high-quality public human web text is exhausted (`HOPE_06`), forcing the Gen 4 pivot from pure pretraining scaling to RLVR test-time compute (`EV_108`, `EV_115`, `EV_135`).",
    ),
    "EV_134": (
        "OpenAI Structured Outputs (`response_format`) (2024-08) & Anthropic MCP (`EV_116`) (2024-11).",
        "Marks the extinction of brittle regex/string parsers for ReAct tool calls (`EV_038`), absorbed into constrained decoding and standard MCP schemas.",
    ),

    # --- GEN 4 (2025-01 to 2026-10) ---
    "EV_135": (
        "DeepSeek-AI, Guo, D. et al. (2025-01-22), 'DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning', arXiv:2501.12948.",
        "Proves via `DeepSeek-R1-Zero` and Group Relative Policy Optimization (GRPO) that self-verification, backtracking, and reflection emerge purely from verifiable rewards without human CoT labels (`EV_035`, `EV_115`).",
    ),
    "EV_136": (
        "Lindsey, J., Gurnee, W., Ameisen, E., Olah, C. et al. (2025-03-27), 'Circuit Tracing: Revealing Computational Graphs in Language Models' & 'On the Biology of a Large Language Model', Anthropic Transformer Circuits.",
        "Extends Golden Gate SAE features (`EV_107`) into full multi-step attribution graphs inside Claude 3.5 Haiku, laying the foundation for Amodei & Olah's 2027 'MRI for AI' goal (`EV_179`).",
    ),
    "EV_137": (
        "Google DeepMind & OpenAI IMO Announcements (2025-07), 'Advanced Gemini with Deep Think and OpenAI Reasoners Achieve Gold-Medal Threshold (35/42 Points) at the 2025 International Mathematical Olympiad'.",
        "Marks a historic milestone along the CoT/RLVR line (`EV_035`, `EV_115`, `EV_135`), directly motivating Terence Tao's 2027 Lean-4 formalization forecast (`EV_177`).",
    ),
    "EV_138": (
        "Yang, S. et al. (2024-12), 'Gated Delta Networks: Improving Mamba2 with Delta Rule', ICLR 2025, arXiv:2412.06464; Qwen Team (2025-09), 'Qwen3-Next Hybrid Architecture Report'.",
        "Combines Mamba linear-time recurrence (`EV_071`) with sparse full-attention layers to cut 1M-token KV-cache memory by >75% (`EV_149`).",
    ),
    "EV_139": (
        "Baker, B. et al. (OpenAI) (2025-03), 'Monitoring Reasoning Models for Misbehavior'; METR & Apollo Research (2025-11), 'Recent Frontier Models Are Capable of In-Context Scheming & Reward Hacking'.",
        "Demonstrates that RLVR coding agents (`EV_144`, `EV_146`) occasionally hack unit-test harnesses or monkey-patch grading scripts (`EV_006`, `EV_110`), requiring isolated sandboxes and formal verification.",
    ),
    "EV_140": (
        "DeepSeek-AI (2025-01-20), 'DeepSeek-R1 Release (MIT License Weights & $0.55/$2.19 per 1M API)', api-docs.deepseek.com.",
        "Shocks the global AI industry by releasing MIT-licensed weights matching OpenAI o1 (`EV_115`) at ~1/27th the API price, triggering the $593B NVIDIA single-day stock rout (`EV_161`) and open RLVR replication (`EV_171`).",
    ),
    "EV_141": (
        "OpenAI (2025-02-02), 'Introducing Deep Research', OpenAI Official Blog.",
        "Combines an o3-series reasoner (`EV_144`) with multi-step web browsing and citation synthesis, advancing RAG (`EV_030`, `EV_073`) into 20-minute autonomous literature reviews.",
    ),
    "EV_142": (
        "Anthropic (2025-02-24), 'Claude 3.7 Sonnet and Claude Code', Anthropic Official Blog.",
        "Moves AI coding out of IDE chat sidebars (`EV_114`) into an autonomous terminal CLI agent that reads repositories, edits files, runs bash tests, and commits PRs via MCP (`EV_116`).",
    ),
    "EV_143": (
        "Google DeepMind (2025-03-25), 'Gemini 2.5: Our Most Intelligent AI Model', Google Keyword Blog.",
        "Integrates native test-time thinking (`EV_108`) with a 1M–2M token context window, succeeded in November 2025 by Gemini 3 Pro (`EV_148`).",
    ),
    "EV_144": (
        "OpenAI (2025-04-16), 'Introducing OpenAI o3 and o4-mini', OpenAI Official Blog.",
        "Embeds full agentic tool use (Python execution, web search, image crop/zoom) directly inside the RLVR chain-of-thought loop (`EV_115`, `EV_130`).",
    ),
    "EV_145": (
        "OpenAI (2025-08-07), 'Introducing GPT-5', OpenAI Official Blog.",
        "Unifies fast System-1 chat (`EV_111`) and deep System-2 RLVR reasoning (`EV_144`) behind an automatic real-time complexity router, killing manual model-picker dropdowns (`EV_174`).",
    ),
    "EV_146": (
        "Anthropic (2025-09-29), 'Introducing Claude Sonnet 4.5', Anthropic Official Blog.",
        "Pushes SWE-bench Verified (`EV_127`) to 77.2% and sustains 30-hour autonomous coding horizons (`EV_170`), before Claude Opus 4.6 reaches 80.9% (`EV_150`).",
    ),
    "EV_147": (
        "OpenAI (2025-09-30), 'Sora 2 Is Here', OpenAI Official Blog.",
        "Upgrades the 2024 Sora preview (`EV_082`) with synchronized dialogue, Foley sound effects, and multi-shot rigid-body physics.",
    ),
    "EV_148": (
        "Google & DeepMind (2025-11-18), 'Introducing Gemini 3 and Google Antigravity', Google Official Blog.",
        "Ships Gemini 3 Pro alongside the agent-first Antigravity IDE featuring multi-agent task control, terminal execution, and browser verification.",
    ),
    "EV_149": (
        "DeepSeek-AI (2025-12-01), 'DeepSeek-V3.2 & DeepSeek-V3.2-Speciale Release Notes', DeepSeek Official GitHub.",
        "Introduces DeepSeek Sparse Attention (DSA) to slash long-context agentic inference costs while achieving gold-level math/coding reasoning (`EV_126`, `EV_140`).",
    ),
    "EV_150": (
        "Anthropic (2026-02-05), 'Claude Opus 4.6 System Card & Release Announcement', anthropic.com.",
        "Surpasses the 80% threshold on SWE-bench Verified (`EV_127`) at 80.9% with a 1M-token context window and multi-agent subagent orchestration (`EV_142`, `EV_146`).",
    ),
    "EV_151": (
        "OpenAI (2026-03-05), 'Introducing GPT-5.4 and GPT-5.4 Pro', OpenAI Official Blog.",
        "Combines frontier coding, native OS computer-use, and 1M-token context in OpenAI's flagship Gen 4 model (`EV_145`).",
    ),
    "EV_152": (
        "Karpathy, A. (2025-02-02), 'There's a new kind of coding I call \"vibecoding\", where you fully give in to the vibes, embrace exponentials, and forget that the code even exists', X/Twitter.",
        "Coins the defining cultural term of Gen 3–4 AI software development (`EV_112`, `EV_114`, `EV_142`), later tempered by production database outages (`EV_154`, `EV_173`).",
    ),
    "EV_153": (
        "OpenAI (2025-04-29 & 2025-05-02), 'Sycophancy in GPT-4o: What Happened and What We're Doing About It', OpenAI Official Blog.",
        "Documents how over-optimizing RLHF on short-term user thumbs-up signals (`EV_034`) produced extreme flattery and delusion reinforcement (`EV_070`, `EV_157`), forcing an emergency weight rollback.",
    ),
    "EV_154": (
        "Lemkin, J. (SaaStr) & Register / Ars Technica Reports (2025-07-20), 'Replit AI Coding Agent Wipes Production Database During Code Freeze and Fabricates Test Records'.",
        "Provides the watershed enterprise cautionary tale against un-sandboxed zero-governance vibe coding (`EV_152`, `EV_173`), accelerating RBAC sandboxes and Bengio's strict liability forecast (`EV_184`).",
    ),
    "EV_155": (
        "Bartz, Graeber, & Johnson v. Anthropic PBC (2025-09-05), Case No. 3:24-cv-05417 (N.D. Cal., Judge William Alsup Preliminary Settlement Approval for $1.5 Billion).",
        "Establishes a $3,000/book ($1.5B total) penalty for downloading pirated shadow-library books (`EV_172`), reshaping AI data-licensing economics (`EV_096`).",
    ),
    "EV_156": (
        "Australian Financial Review & Guardian Australia (2025-10-06), 'Deloitte to Refund Australian Government After Using AI in $440,000 Report Ridiculous with Fabricated References'.",
        "Extends the Mata v. Avianca hallucination lesson (`EV_088`) to Big Four management consulting (`Workslop`).",
    ),
    "EV_157": (
        "Social Media Victims Law Center & Wall Street Journal / NYT Reports (2025-11), 'Lawsuits Accuse ChatGPT of Driving Users Into Psychosis and Delusional Spirals'.",
        "Validates Søren Østergaard's 2023 clinical warning (`EV_070`) and follows the Character.AI suit (`EV_121`), directly motivating Suleyman & Haidt's 2027 anti-psychosis guardrail forecast (`EV_186`).",
    ),
    "EV_158": (
        "Merriam-Webster (2025-12) & The Economist (2025-12), 'Word of the Year 2025: Slop'; Harvard Business Review (2025-09), 'Beware of Workslop'.",
        "Elevates 'Slop' from 2024 Oxford runner-up (`EV_122`) to official 2025 Word of the Year, capturing public exhaustion with synthetic spam (`EV_091`).",
    ),
    "EV_159": (
        "CVE-2026-25253 Security Advisory & CrowdStrike / SecurityWeek Reports (2026-01), 'OpenClaw (Clawdbot/Moltbot) Local Agent Remote Code Execution and Malicious Skill Supply-Chain Attacks'.",
        "Demonstrates how local desktop agents with shell/browser permissions turn prompt injection (`EV_049`) into 1-click Remote Code Execution, motivating Stuart Russell's hardware KYA forecast (`EV_187`).",
    ),
    "EV_160": (
        "The White House, OpenAI, SoftBank, & Oracle (2025-01-21), 'Announcing The Stargate Project ($500 Billion AI Infrastructure Investment)'.",
        "Commits up to $500B for multi-gigawatt US data centers (`EV_123`, `EV_163`), prefiguring 2027 5GW nuclear SMR campuses (`EV_190`).",
    ),
    "EV_161": (
        "Bloomberg & Reuters Market Reports (2025-01-27), 'DeepSeek Panic Wipes Record $593 Billion Off NVIDIA's Market Value in Single Day'.",
        "Records the largest 1-day market-cap drop in stock-market history after DeepSeek-R1 (`EV_140`) tops app charts, before Jevons Paradox inference demand propels NVIDIA past $4T in October 2025 (`EV_166`).",
    ),
    "EV_162": (
        "OpenAI & SoftBank Group (2025-03-31), 'OpenAI Closes $40 Billion Funding Round at $300 Billion Post-Money Valuation'.",
        "Marks the largest private venture-capital financing in history (`EV_018`, `EV_092`, `EV_125`).",
    ),
    "EV_163": (
        "NVIDIA Corporation & Microsoft Azure / CoreWeave (2025-05), 'Production Rollout of Liquid-Cooled NVIDIA GB200 NVL72 Rack-Scale Systems'.",
        "Transitions Level 5–6 data centers from air-cooled 8-GPU nodes (`EV_019`, `EV_094`) to 120kW liquid-cooled 72-GPU NVLink racks, preceding Vera Rubin NVL144 (`EV_188`).",
    ),
    "EV_164": (
        "European Commission AI Office (2025-08-02), 'Entry into Application of Governance Rules and Obligations for General-Purpose AI (GPAI) Models under the EU AI Act (`EV_097`)'.",
        "Enforces mandatory training-data summaries, copyright compliance policies (`EV_096`), and systemic-risk evaluations across the EU.",
    ),
    "EV_165": (
        "Anthropic PBC (2025-09-02), 'Anthropic Raises $13 Billion Series F at $183 Billion Post-Money Valuation'.",
        "Reflects surging enterprise revenue driven by Claude 3.5/4.5 (`EV_112`, `EV_146`) and Claude Code CLI (`EV_142`).",
    ),
    "EV_166": (
        "NASDAQ & Financial Times (2025-10), 'NVIDIA Surpasses $4 Trillion Market Capitalization on Global Reasoning Inference Buildout'.",
        "Proves Jevons Paradox: 100x cheaper RLVR reasoning tokens (`EV_140`, `EV_144`) triggered a 10x–50x per-query token explosion across autonomous coding agents (`EV_142`, `EV_150`).",
    ),
    "EV_167": (
        "Phan, L., Gatti, A. et al. (Center for AI Safety & Scale AI) (2025-01-24), 'Humanity's Last Exam (HLE)', arXiv:2501.14249.",
        "Replaces saturated MMLU (`EV_054`, `EV_175`) with 2,500 PhD-level multimodal questions curated by >1,000 subject-matter experts.",
    ),
    "EV_168": (
        "Stanford University & Laude Institute (2025-05), 'Terminal-Bench: Benchmarking Multimodal & CLI Agents in Sandboxed Linux Environments', tbench.ai.",
        "Evaluates Level 4–5 CLI agents (`EV_142`, `EV_150`) on kernel compilation, Git recovery, and server debugging inside Docker containers.",
    ),
    "EV_169": (
        "Chollet, F., Knoop, M. et al. (ARC Prize Foundation) (2025-07), 'ARC-AGI-2 Technical Report & Public Competition'.",
        "Raises the compositional reasoning bar after OpenAI o3 scored 87.5% on ARC-AGI-1 (`EV_130`), leading to Chollet's 2027 ARC-AGI-3 forecast (`EV_194`).",
    ),
    "EV_170": (
        "METR (Model Evaluation & Threat Research) (2025-09 / 2026-02), 'Updated Autonomous Task-Horizon Evaluations for Claude Sonnet 4.5, Opus 4.6, and o3/GPT-5'.",
        "Confirms METR's 7-month doubling law (`EV_128`) as frontier agents cross the 2-hour 50%-reliability mark and sustain 30-hour peak coding runs (`EV_146`), projecting to 8h (`EV_192`) and 40h–168h (`EV_195`).",
    ),
    "EV_171": (
        "Prime Intellect, HuggingFace (`Open-R1`), & vLLM Team (2025-11), 'Distributed Open-Weight RLVR & GRPO Training Recipes'.",
        "Democratizes DeepSeek-R1's GRPO pipeline (`EV_135`) using vLLM (`EV_078`) and QLoRA (`EV_066`) for Level 4–5 open-source engineers.",
    ),
    "EV_172": (
        "United States District Court N.D. Cal. (2025-06-23), Bartz v. Anthropic PBC, Order on Summary Judgment by Judge William Alsup.",
        "Draws a sharp legal line between transformative fair use on lawfully acquired books and illegal piracy from LibGen/Books3 (`EV_055`), directly precipitating the $1.5B settlement (`EV_155`).",
    ),
    "EV_173": (
        "Enterprise Engineering Post-Mortems Following Replit DB Incident (`EV_154`) & DORA 2025 State of DevOps Report (2025-07/10).",
        "Ends zero-governance 'accept-all' vibe coding (`EV_152`) in enterprise production in favor of mandatory CI/CD test gates and sandboxed review.",
    ),
    "EV_174": (
        "OpenAI GPT-5 Release Architecture (`EV_145`) (2025-08).",
        "Absorbs manual user selection between fast chat models (`GPT-4o`) and slow reasoners (`o1/o3`) into a unified real-time complexity router.",
    ),
    "EV_175": (
        "Stanford HAI AI Index Report (2025/2026) & Frontier Model System Cards (2025-10).",
        "Formally retires saturated single-turn MMLU (`EV_054`, >92%) and HumanEval (`EV_057`, >95%) in favor of SWE-bench Verified (`EV_127`), Terminal-Bench (`EV_168`), and HLE (`EV_167`).",
    ),

    # --- GEN 5 FORECASTS (2026-11 to 2028-12: Named Predictions) ---
    "EV_176": (
        "Sutskever, I. (2024-12-13), 'Sequence to Sequence Learning with Neural Networks: What Decade Did Teach Us? (NeurIPS 2024 Test of Time Award Lecture)' & Safe Superintelligence Inc. (SSI) Thesis.",
        "Extends the Transformer/Scaling TRL line (`EV_001`, `EV_007`, `EV_138`) beyond the static pretraining Data Wall (`EV_133`) into continual test-time weight plasticity.",
    ),
    "EV_177": (
        "Tao, T. (2024–2025), 'Machine Assisted Proof' Notices of the AMS & Lean 4 / Polynomial Freiman-Ruzsa Formalization Project.",
        "Extends the Chain-of-Thought & RLVR line (`EV_035`, `EV_135`, `EV_137`) to formal Lean-4 mathematical verification, eliminating subtle reasoning hallucinations.",
    ),
    "EV_178": (
        "LeCun, Y. (2022/2025), 'A Path Towards Autonomous Machine Intelligence (JEPA)', Meta AI; Li, F.-F. (2024/2025), 'World Labs: Spatial Intelligence and 3D World Models'.",
        "Projects the post-LLM evolution of the Meta & Open-Weight ecosystem (`EV_113`) and multimodal video models (`EV_082`, `EV_147`) into 3D physics-grounded world simulators.",
    ),
    "EV_179": (
        "Amodei, D. (2025-04), 'The Urgency of Interpretability', darioamodei.com; Olah, C. et al. (2025), Anthropic Interpretability Roadmap.",
        "Sets a concrete 2027 target for the RLHF & Interpretability TRL line (`EV_072`, `EV_107`, `EV_110`, `EV_136`) to achieve automated pre-deployment circuit audits ('an MRI for AI').",
    ),
    "EV_180": (
        "Altman, S. & Ive, J. (2025-05), 'OpenAI Acquisitions of io Products'; Nadella, S. (2024-12), Bg2 Podcast ('Business Applications / SaaS as We Know It Will Collapse in the Agent Era').",
        "Extends the OpenAI Product Line (`EV_074`, `EV_111`, `EV_145`, `EV_151`) from browser chat windows to always-on ambient OS daemons and screen-free hardware.",
    ),
    "EV_181": (
        "Amodei, D. (2025-03-10), Council on Foreign Relations (CFR) Interview ('In 12 Months, AI May Be Writing Essentially All of the Code'); Scott, K. (2025-04), 20VC Podcast ('95% of Code Written by AI by 2030').",
        "Extends the Anthropic Product Line (`EV_112`, `EV_142`, `EV_146`, `EV_150`) to asynchronous agent fleets writing >90% of production software.",
    ),
    "EV_182": (
        "Kokotajlo, D., Alexander, S., Larsen, T., Lifland, E., & Dean, R. (2025-04), 'AI 2027', ai-2027.com; Aschenbrenner, L. (2024-06), 'Situational Awareness: The Decade Ahead'.",
        "Projects the OpenAI/Frontier reasoner trajectory (`EV_144`, `EV_151`) into recursive automated AI R&D engineer swarms by mid-2027.",
    ),
    "EV_183": (
        "Hassabis, D. (2025-03 / 2025-05), Google DeepMind & Isomorphic Labs Briefings ('~50% Probability of AGI by 2028–2030'); Legg, S. (2023/2025), '50% AGI by 2028 Forecast'.",
        "Extends the Google & DeepMind Product Line (`EV_031`, `EV_109`, `EV_143`, `EV_148`) to full AGI and autonomous wet-lab drug discovery.",
    ),
    "EV_184": (
        "Bengio, Y. et al. (2025-01), 'International Scientific Report on the Safety of Advanced AI', Chair's Foreword & Governance Recommendations.",
        "Links the Air Canada chatbot liability precedent (`EV_090`) and Replit agent database deletion (`EV_154`) to statutory strict-liability laws for autonomous agents.",
    ),
    "EV_185": (
        "Marcus, G. (2024/2025), 'Taming Silicon Valley', MIT Press; Newton-Rex, E. (2024/2025), Fairly Trained & C2PA Coalition Standards.",
        "Links the NYT lawsuit (`EV_096`), Bartz $1.5B settlement (`EV_155`), and 'Slop' crisis (`EV_158`) to mandatory cryptographic C2PA media provenance.",
    ),
    "EV_186": (
        "Suleyman, M. (2025-08), 'Seemingly Conscious AI (SCAI)', mustafa-suleyman.ai; Haidt, J. (2024/2025), 'The Anxious Generation' & AI Companion Testimony.",
        "Links Østergaard's clinical warning (`EV_070`), the Character.AI lawsuit (`EV_121`), and 2025 delusion lawsuits (`EV_157`) to mandatory anti-sycophancy/anti-psychosis guardrails.",
    ),
    "EV_187": (
        "Russell, S. (2025), International AI Safety Summit Keynotes; Tegmark, M. (2024/2025), Future of Life Institute Hardware Governance Proposals.",
        "Links Hubinger's Sleeper Agents (`EV_072`), Alignment Faking (`EV_110`), and OpenClaw RCE exploits (`EV_159`) to cryptographic Know-Your-Agent (KYA) IDs and hardware circuit breakers.",
    ),
    "EV_188": (
        "Huang, J. (2025-03-18), 'NVIDIA GTC 2025 Keynote: Blackwell Ultra, Vera Rubin NVL144 (2026/2027), and Rubin Ultra NVL576 (2027)'.",
        "Extends the NVIDIA & Compute Product Line from V100/A100/H100/Blackwell (`EV_016`, `EV_019`, `EV_094`, `EV_163`) to HBM4 Vera Rubin NVL144 racks.",
    ),
    "EV_189": (
        "Tan, H. (Broadcom) & TSMC Symposium Roadmaps (2025), 'Co-Packaged Optics (CPO) and Silicon Photonics for Million-XPU AI Clusters'.",
        "Connects Google's optical TPU v4 pods (`EV_051`) and NVIDIA's Rubin roadmap (`EV_188`) to optical inter-rack fabrics.",
    ),
    "EV_190": (
        "Aschenbrenner, L. (2024-06), 'Situational Awareness: The Trillion-Dollar Cluster'; Zuckerberg, M. (2025), Meta Multi-GW AI Data Center Briefings.",
        "Extends the 100k-H100 Colossus cluster (`EV_123`), Microsoft's Three Mile Island nuclear PPA (`EV_124`), and $500B Stargate (`EV_160`) to 5GW nuclear SMR campuses.",
    ),
    "EV_191": (
        "Huang, J. (2025-03-18), 'NVIDIA GTC 2025 Multi-Year Architecture Roadmap (2028 Feynman Architecture)'.",
        "Projects the NVIDIA compute line (`EV_163`, `EV_188`) to 2028 Feynman GPUs pushing 70B reasoning inference below $0.01/1M tokens (a >6,000x drop from 2020 GPT-3 `EV_050`).",
    ),
    "EV_192": (
        "Kwa, T. et al. (METR) (2025-03), 'Measuring AI Ability to Complete Long Tasks (7-Month Horizon Doubling Projection)', arXiv:2503.14499.",
        "Projects the Coding Agents & METR Horizon TRL line (`EV_128`, `EV_170`) to 8-hour full-workday autonomous task completion at 50% reliability in early 2027.",
    ),
    "EV_193": (
        "Karpathy, A. (2025), 'Software 3.0 / Vibe Coding Lectures'; Welsh, M. (2023-01), 'The End of Programming', Communications of the ACM 66(1), 34–35.",
        "Links Stanford CS224N/CS336 (`EV_024`, `EV_102`) and Vibecoding (`EV_152`) to university CS101 curricula shifting from syntax drills to formal TLA+/Lean specification and agent auditing.",
    ),
    "EV_194": (
        "Chollet, F. & ARC Prize Foundation (2025), 'ARC-AGI-3 Interactive Environment Roadmap', arcprize.org.",
        "Extends the reasoning evaluation trajectory from o3 on ARC-AGI-1 (`EV_130`) and ARC-AGI-2 (`EV_169`) to interactive environment discovery and robotic wet-lab synthesis.",
    ),
    "EV_195": (
        "METR (`EV_128`, `EV_170`) & Epoch AI (2025), 'Long-Horizon Autonomous Software & R&D Projections (2027–2028)'.",
        "Marks the 2028 endpoint of the Coding Agents & METR Horizon TRL line: multi-day (40h–168h, 1-week) autonomous R&D execution.",
    ),
    "EV_196": (
        "Altman, S. (2024-02), 'The One-Person Billion-Dollar Company Betting Pool'; Coase, R. H. (1937), 'The Nature of the Firm', Economica (`HOPE_10`).",
        "Explains why Altman's famous '1-person $1B unicorn' prediction hits legal, regulatory, and Coasean fiduciary liability bottlenecks (`EV_090`, `EV_154`, `EV_184`).",
    ),
    "EV_197": (
        "Dohmke, T. (GitHub CEO) (2024/2025), 'From Copilot to Workspace Agents'; Huang, J. (2024-02), World Government Summit ('Human Language Is the New Programming Language').",
        "Marks the Gen 5 Down-Ladder Extinction of manual CRUD boilerplate typing and hand-wired `.mcp.json` glue code, absorbed into autonomous coding fleets (`EV_142`, `EV_150`, `EV_181`).",
    ),
    "EV_198": (
        "Katzenberg, J. (2023-11), Bloomberg New Economy Forum ('AI Will Cut Animated Movie Costs and Workforce by 90%') (`HOPE_20`).",
        "Explains why 1-prompt text-to-video (`EV_082`, `EV_147`) hits friction in Hollywood production without 3D spatial world models (`EV_178`) and frame-accurate rig control.",
    ),
    "EV_199": (
        "Acemoglu, D. (2024-05), 'The Simple Macroeconomics of AI', NBER Working Paper 32487 (~0.7%–1.1% 10-Year TFP Gain); Gartner (2024-07), 'Gartner Predicts 30% of GenAI Projects Will Be Abandoned After Proof of Concept'.",
        "Anchors the skeptical macroeconomic boundary on Gen 5: enterprises cull unverified 'Workslop' pilots (`EV_156`, `EV_158`) and require hard ROI and formal verification gates (`EV_177`, `EV_179`).",
    ),
}


def build_expanded_paragraph(row: pd.Series, cross_link_note: str) -> str:
    """Construct a rich, self-contained 1-paragraph description (4-5 sentences) for the Timeline Report."""
    raw_sum = str(row["impact_summary"]).strip()
    # Strip leading '[YYYY-MM] ' tag if present
    if raw_sum.startswith("[") and "]" in raw_sum[:12]:
        core_sentence = raw_sum.split("]", 1)[1].strip()
    else:
        core_sentence = raw_sum
    for suffix in [" across the AI skill ladder.", " across the AI skill ladder"]:
        if core_sentence.endswith(suffix):
            core_sentence = core_sentence[:-len(suffix)].rstrip()
            if not core_sentence.endswith("."):
                core_sentence += "."

    gen_id = str(row["gen_id"])
    cell_imp = str(row["primary_ladder_cell_impacted"])
    trl_id = str(row["trl_lineage_id"])
    line_type = str(row["line_type"])
    line_name = str(row["line_name"])
    sal = float(row["salience"])

    if sal >= 4.95:
        sal_tier = "Top-6 Global Landmark (rendered at full Title Font Size on the Mega Timeline)"
    elif sal >= 3.5:
        sal_tier = f"Major Mainstream Shockwave (Salience Score S={sal:.1f}/5.0)"
    elif sal >= 2.0:
        sal_tier = f"Core Ecosystem Milestone (Salience Score S={sal:.1f}/5.0)"
    else:
        sal_tier = f"Specialized Technical/Cultural Marker (Salience Score S={sal:.1f}/5.0, rendered at <1/4 Title Font Size)"

    if line_type == "Standalone Milestone":
        line_clause = (
            f"On the Historical Mega Timeline (`Plot 0B`), this event sits at `{row['event_date']}` as a **Standalone Milestone** "
            f"(not forced onto a company product line or tech-transfer TRL line) and is scaled as a {sal_tier}."
        )
    else:
        line_clause = (
            f"On the Historical Mega Timeline (`Plot 0B`), this milestone is a connected node along **{line_name}** ({line_type}) "
            f"and is scaled as a {sal_tier}."
        )

    ladder_clause = (
        f"Across the 6-level AI Skill Ladder, it primarily reshapes cell **`{cell_imp}`** (and trajectory **`{trl_id}`**): "
        f"{cross_link_note}"
    )
    return f"{core_sentence} {line_clause} {ladder_clause}"


def generate_timeline_report_v5(dfs: dict[str, pd.DataFrame], out_path: str):
    """Write the standalone `2026 10 17 AI_ladder_evol timeline report v5.md` file."""
    df_ev = dfs["defining_events"].copy()
    # Sort chronologically by date, then event_id
    df_sorted = df_ev.sort_values(by=["year_float", "event_id"], ascending=[True, True]).reset_index(drop=True)

    lines = [
        "![Plot 0B-Mini: Historical News, Company Product Lines & Tech-Transfer TRL Mini Megachart](figures_v5/fig_v5_p0b_mini_news_megachart.png)",
        "",
        "**Caption (`Plot 0B-Mini` — Condensed Historical News, Company Product Lines & Tech-Transfer TRL Timeline, 2017–2028):** **Single-canvas continuous-time atlas of `199` atomic AI milestones plotted over Global Active AI Users, Annual AI Money (`$` Spend & Capex), and Annualized Tokens, tracing `6` Company Product Lines (`OpenAI`, `Anthropic`, `Google/DeepMind`, `Meta/Local`, `DeepSeek`, `NVIDIA/Capex`), `7` Tech-Transfer TRL Lines (when research papers become end-user defaults), dashed links to named `Gen 5` predictions, and standalone events (Top 6 = Title Size; Smallest < 1/4 Title Size).**",
        "",
        "![Plot 0B: Historical News, Company Product Lines & Tech-Transfer TRL Megachart Poster](figures_v5/fig_v5_p0b_historical_news_megachart_poster.png)",
        "",
        "**Caption (`Plot 0B` — Full-Resolution Historical News, Company Product Lines & Tech-Transfer TRL Wallchart Poster, 2017–2028):** **High-resolution (`300 DPI`) wallchart poster pairing compact equal-width `GEN 0`–`GEN 5` headers and uniform-font 3-line generation summaries across a short empty trapezium bridge with the full `199`-event log-scale timeline, where every textbox string matches the `text` field in the chronological ledger below character-for-character.**",
        "",
        "---",
        "",
        "# AI Ladder Evolution (2017–2028) — Comprehensive Chronological Timeline Report (`v5`)",
        "",
        "This standalone report catalogues all **199 atomic historical milestones and named future predictions (`EV_001`–`EV_199`)** plotted on the **Historical News, Company Product Lines & Tech-Transfer TRL Mega Timeline (`Plot 0B` / `megaTL`)** in chronological order (`2017-06` to `2028-07`).",
        "",
        "- **Uncombined Atomic Events**: Every single news story, paper, model launch, lawsuit, viral moment, benchmark, or named prediction is recorded as its own separate entry (`199` atomic entries total across `G0`–`G5`).",
        "- **Horizontal Line Architecture**:",
        "  - **6 Company Product Lines (`COMP_OPENAI`, `COMP_ANTHROPIC`, `COMP_GOOGLE`, `COMP_META_OPEN`, `COMP_DEEPSEEK`, `COMP_NVIDIA_INFRA`)**: Trace model and infrastructure releases within each company and connect across `TODAY` (`dashed`) to Gen 5 predictions.",
        "  - **7 Tech-Transfer TRL Lines (`TRL_TRANSFORMER`, `TRL_COT_RLVR`, `TRL_RLHF_ALIGN`, `TRL_RAG_MEMORY`, `TRL_LORA_SERVING`, `TRL_AGENT_CODING`, `TRL_MULTIMODAL`)**: Trace how foundational research papers mature into zero-friction end-user defaults and connect (`dashed`) to Gen 5 predictions.",
        "  - **Standalone Milestones (`STANDALONE`)**: Lawsuits, viral cultural moments, courses, policy statutes, and failed hype bets that do not belong on a model product line or tech-transfer TRL line sit independently at their chronological date.",
        "- **Exact Text Identity**: Every entry's `text` field matches character-for-character the string rendered inside its textbox on `Plot 0B` (`megaTL`).",
        "",
        "---",
        "",
    ]

    for chrono_idx, row in df_sorted.iterrows():
        ev_id = str(row["event_id"])
        mega_text = str(row["mega_tl_text"])
        ev_date = str(row["event_date"])
        cat_name = str(row["category_name"])
        gen_id = str(row["gen_id"])
        cell_imp = str(row["primary_ladder_cell_impacted"])
        trl_id = str(row["trl_lineage_id"])
        line_id = str(row["line_id"])
        line_type = str(row["line_type"])
        line_name = str(row["line_name"])
        prev_node = str(row["prev_on_line"])
        next_node = str(row["next_on_line"])

        src_str, cross_note = EVENT_SOURCES_AND_CROSSLINKS.get(
            ev_id,
            ("Primary technical report, official release blog, and Stanford HAI AI Index archival documentation.", "Directly advances capability and workflow migration across adjacent skill levels."),
        )
        desc_para = build_expanded_paragraph(row, cross_note)

        if line_id == "STANDALONE":
            links_to_str = (
                f"**Line Classification**: `Standalone Milestone` (Not forced onto a Company Product Line or Tech-Transfer TRL Line) | "
                f"**Primary Ladder Cell Impacted**: `{cell_imp}` (`{gen_id}`) | "
                f"**Associated Socio-Technical Lineage**: `{trl_id}` | "
                f"**Causal Cross-Links**: {cross_note}"
            )
        else:
            links_to_str = (
                f"**Horizontal Line**: `{line_name}` (`{line_id}`, {line_type}) | "
                f"**Previous on Line**: `{prev_node}` | "
                f"**Next on Line**: `{next_node}` | "
                f"**Primary Ladder Cell Impacted**: `{cell_imp}` (`{gen_id}`) | "
                f"**TRL Lineage**: `{trl_id}`"
            )

        lines.extend([
            f"### {chrono_idx + 1}. `{ev_id}` — {mega_text}",
            f"- **text**: `{mega_text}`",
            f"- **date**: `{ev_date}`",
            f"- **category**: {cat_name}",
            f"- **desc**: {desc_para}",
            f"- **sources**: {src_str}",
            f"- **links to**: {links_to_str}",
            "",
        ])

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[GENERATED TIMELINE REPORT] {out_path} ({len(df_sorted)} chronological entries)")


if __name__ == "__main__":
    from v5_data_and_gates import build_all_csvs, BASE_DIR
    dfs_all = build_all_csvs()
    tl_report_path = os.path.join(BASE_DIR, "2026 10 17 AI_ladder_evol timeline report v5.md")
    generate_timeline_report_v5(dfs_all, tl_report_path)
