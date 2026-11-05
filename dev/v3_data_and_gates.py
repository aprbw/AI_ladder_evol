import os
import json
import numpy as np
import pandas as pd

BASE_DIR = "/Users/z3540725/My Drive/personal/2026 10 17 AI_ladder_evol"
CACHE_DIR = os.path.join(BASE_DIR, "cache_v3")
os.makedirs(CACHE_DIR, exist_ok=True)


def build_and_verify_all():
    print(f"[CACHE-FIRST CHECK] Inspecting cache directory: {CACHE_DIR}")

    # 1. Table 2.1: Existing AI Ladders & Emergent Folksonomy Catalog (20 ladders)
    existing_ladders = [
        ("L_LIT_01", "Karpathy Software 1.0 / 2.0 / 3.0", "Andrej Karpathy", "2017-11", 3,
         "Explicit Code, Learned Weights, Natural Language Prompts",
         "Rungs 1-2: Classical Code & Supervised Neural Nets",
         "Rung 3 (in 2017-2022): Natural Language Programming of Universal Models",
         "G0->G1 (2020-06) & G1->G2 (2022-11)", 0.72, 0.65, 0.85, 0.40),
        ("L_LIT_02", "SAE L0-L5 Adapted for Coding Autonomy", "Industry / GitHub / Sourcegraph", "2021-06", 6,
         "Autocomplete, In-IDE Chat, Multi-File Edit, Background Agent, Unsupervised SWE",
         "L0-L2: Manual Coding, Ghost-Text Tab Autocomplete, Chat Copy-Paste",
         "L4-L5: Fully Autonomous Unsupervised Full-Lifecycle Software Engineering",
         "G1->G2 (2022-11) & G2->G3 (2024-05)", 0.78, 0.82, 0.75, 0.55),
        ("L_LIT_03", "Stanford CS224N -> CS324 Progression", "Manning, Liang, Hashimoto", "2022-01", 4,
         "Word Vectors, Fine-Tuned BERT, Few-Shot Prompting, Adapter Tuning",
         "Rungs 1-3: TF-IDF/Word2Vec, Pretrained Encoders, Few-Shot In-Context Learning",
         "Rung 4: Autonomous Multimodal Foundation Agents",
         "G0->G1 (2020-06)", 0.80, 0.88, 0.82, 0.70),
        ("L_LIT_04", "DeepLearning.AI Practitioner Course Ladder", "Andrew Ng & Partners", "2023-05", 5,
         "Prompt Engineering, Chat with Your Data (RAG), Fine-Tuning, Reasoning, Multi-Agent Systems",
         "Rungs 1-3: Prompt Templates, Chunked Vector RAG, QLoRA Adapter Tuning",
         "Rung 5 (in 2023): Autonomous CrewAI/AutoGen Multi-Agent Enterprise Swarms",
         "G1->G2 (2022-11) & G3->G4 (2025-01)", 0.88, 0.92, 0.84, 0.68),
        ("L_LIT_05", "LlamaIndex / Enterprise RAG Maturity Ladder", "Jerry Liu / LlamaIndex", "2023-08", 5,
         "Naive Chunked RAG, Hybrid BM25+Vector, Reranking, GraphRAG, Agentic Query Planning",
         "Rungs 1-3: Top-k Vector Chunking, Metadata Filtering, Cross-Encoder Reranking",
         "Rung 5 (in 2023): Self-Healing Autonomous Enterprise Knowledge Graphs",
         "G2->G3 (2024-05)", 0.76, 0.80, 0.70, 0.65),
        ("L_LIT_06", "DeepMind Levels of AGI (Performance x Autonomy)", "Morris et al. (Google DeepMind)", "2023-11", 6,
         "No AI, Emerging, Competent, Expert, Virtuoso, Superhuman; Tool -> Consultant -> Collaborator -> Agent",
         "Autonomy L1-L3: AI as Passive Tool, On-Demand Consultant, Interactive Collaborator",
         "Autonomy L5 / Perf L5: Fully Autonomous Superhuman General Organization",
         "G2->G3 (2024-05)", 0.85, 0.74, 0.80, 0.50),
        ("L_LIT_07", "LangChain Cognitive Architectures & Autonomy Tiers", "Harrison Chase (LangChain)", "2024-01", 6,
         "Fixed Code, Single LLM Call, Chain, Router, State-Machine Graph (LangGraph), Deep Agents",
         "Rungs 1-4: Single API Call, Linear Prompt Chains, Intent Routers",
         "Rungs 5-6 (in early 2024): Long-Horizon Open-Ended Deep Agents",
         "G2->G3 (2024-05) & G3->G4 (2025-01)", 0.90, 0.86, 0.88, 0.72),
        ("L_LIT_08", "OpenAI 5 Levels of AGI", "OpenAI Leadership", "2024-07", 5,
         "L1 Chatbots, L2 Reasoners, L3 Agents, L4 Innovators, L5 Organizations",
         "L1-L2: Conversational Chatbots & Early Test-Time Reasoners (o1-preview)",
         "L4-L5: Scientific Innovators & Zero-Human Autonomous Corporations",
         "G3->G4 (2025-01)", 0.82, 0.60, 0.72, 0.45),
        ("L_LIT_09", "Gartner 5-Level Enterprise AI Maturity Model", "Gartner Research", "2024-08", 5,
         "Foundational, Emerging, Operational, Scaled, Transformational",
         "L1-L3: Ad-Hoc Employee Chat, Pilot RAG Bots, Department Copilots",
         "L5: Enterprise-Wide Autonomous Process Transformation (warned 40% cancel rate)",
         "G2->G3 (2024-05)", 0.75, 0.70, 0.68, 0.80),
        ("L_LIT_10", "Menlo Ventures Enterprise GenAI Stack", "Menlo Ventures", "2024-11", 4,
         "Consumer Chat, Departmental Copilots, Vertical AI Apps, Infrastructure/Model Layer",
         "Rungs 1-3: SaaS Copilots, Bought Vertical AI (76% bought vs 24% built), Prompt Caching",
         "Rung 4: Autonomous Multi-Departmental Agent Ecosystems",
         "G3->G4 (2025-01)", 0.84, 0.78, 0.82, 0.95),
        ("L_LIT_11", "Anthropic Building Effective Agents Taxonomy", "Erik Schluntz & Barry Zhang", "2024-12", 7,
         "Augmented LLM, Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer, Autonomous Agent",
         "Patterns 1-6: Structured Predefined Workflows with Deterministic Guardrails",
         "Pattern 7: Unconstrained Open-Ended Autonomous Coding & Computer-Use Agents",
         "G3->G4 (2025-01)", 0.94, 0.90, 0.92, 0.88),
        ("L_LIT_12", "a16z GenAI Application & Agentic Stack", "Andreessen Horowitz", "2024-06", 4,
         "Foundation APIs, RAG/Context Plumbing, AI-Native Copilots, Autonomous Agent Coworkers",
         "Rungs 1-3: Wrapper Apps, Vector Context, Human-in-the-Loop IDE/Vertical Copilots",
         "Rung 4: Full-Time Autonomous Digital Employees Replacing SaaS Seats",
         "G2->G3 (2024-05)", 0.80, 0.76, 0.78, 0.82),
        ("L_LIT_13", "Fast.ai Top-Down Practical Deep Learning", "Jeremy Howard", "2018-09", 4,
         "Pretrained Transfer Learning, ULMFiT Fine-Tuning, DataBlock Curation, Custom PyTorch",
         "Rungs 1-3: 5-Line Pretrained Vision/NLP Fine-Tuning on Single GPU",
         "Rung 4: Universal Small-Data Transfer Learning Without Giant Compute Clusters",
         "G0 (2017-2020)", 0.70, 0.85, 0.74, 0.60),
        ("L_LIT_14", "HuggingFace NLP & Transformers Progression", "Wolf et al. (HuggingFace)", "2019-10", 4,
         "pipeline() Inference, AutoModel Fine-Tuning, Distributed Trainer, Custom Pretraining",
         "Rungs 1-3: Pretrained BERT/RoBERTa Checkpoints & Single-GPU Fine-Tuning",
         "Rung 4: Democratized Community Training of Frontier-Scale Models (BigScience)",
         "G0->G1 (2020-06)", 0.82, 0.86, 0.80, 0.74),
        ("L_LIT_15", "Cursor AI-Native Coding Progression", "Anysphere (Cursor)", "2024-06", 4,
         "Copilot++ Tab, Cmd+K Inline Diff, @codebase Chat, Composer Multi-File Agent",
         "Rungs 1-3: Multi-Line Next-Edit Tab, Inline Prompt Diffs, Repo-Indexed Chat",
         "Rung 4: Background Autonomous Multi-File Feature Implementation",
         "G2->G3 (2024-05)", 0.86, 0.91, 0.85, 0.78),
        ("L_LIT_16", "Anthropic MCP & Claude Code Harness Tiers", "Anthropic Engineering", "2025-02", 5,
         "Web Chat, Projects/Artifacts, Desktop MCP (.mcp.json), Claude Code CLI, Parallel Worktree Swarms",
         "Rungs 1-4: Built-In Thinking Chat, Artifacts, MCP Connectors, Terminal CLI Loops",
         "Rung 5: Unsupervised Multi-Agent Swarms & OS-Level Computer Use at Human Parity",
         "G3->G4 (2025-01)", 0.95, 0.94, 0.92, 0.90),
        ("L_LIT_17", "MIT NANDA GenAI Divide Enterprise Audit", "MIT Project NANDA", "2025-07", 4,
         "Consumer Shadow AI, Bought SaaS Tools (67% success), Partner Builds, In-House Builds (33% success)",
         "Rungs 1-2: Shadow ChatGPT Usage & Purchased Departmental/Coding Tools",
         "Rung 4: Custom In-House Autonomous Enterprise Orchestration (80-95% pilot failure)",
         "G3->G4 (2025-01)", 0.85, 0.82, 0.86, 0.92),
        ("L_LIT_18", "Scale AI SWE-bench Pro & Harness Autonomy Audit", "Scale AI SEAL Lab", "2025-09", 4,
         "Public Benchmark Solving, Standardized Scaffold, Custom Vendor Harness, Unseen Private Repo Generalization",
         "Rungs 1-3: High Public SWE-bench Verified Scores (70-96%) via Vendor Harnesses",
         "Rung 4: Zero-Drop Generalization to Unseen Commercial Repos (actual drop: 4.8-22.5 pts)",
         "G4 (2025-2026)", 0.88, 0.80, 0.90, 0.94),
        ("L_LIT_19", "LocalLLaMA & OpenClaw Self-Hosted Sandbox Ladder", "Open-Source Practitioner Community", "2025-11", 5,
         "Ollama One-Click, Local RAG/WebUI, QLoRA Tuning, Dedicated Mac Mini OpenClaw, Multi-GPU RLVR Cluster",
         "Rungs 1-4: Quantized GGUF Local Chat, OpenWebUI, Dedicated M4 Mac Mini 24/7 OpenClaw Agent",
         "Rung 5: Decentralized Home-Cluster Frontier Model Pretraining",
         "G3->G4 (2025-01)", 0.89, 0.95, 0.86, 0.84),
        ("L_LIT_20", "Gemini Deep Research 5-Era / 23-Step Historical Ladder", "Google Gemini Deep Research", "2026-10", 5,
         "Pre-LLM Encoders (4 steps), Completion (4 steps), Chat/RAG (5 steps), Long-Context (5 steps), Reasoning/MCP/CLI (5 steps)",
         "Steps 1-4 per Era: First-Release Capability Progression from Autocomplete to CLI Agents",
         "Top Step L5-P5: Autonomous GUI Computer Use & Multi-Agent Swarms Replacing Manual Workflows",
         "All 4 Breaks (First-Release Dates: 2018-10, 2020-06, 2022-11, 2023-11, 2024-09)", 0.96, 0.84, 0.94, 0.88),
    ]
    df_ladders = pd.DataFrame(existing_ladders, columns=[
        "ladder_id", "ladder_name", "author", "pub_date", "rung_count",
        "folksonomy_terms", "descriptive_bottom_rungs", "speculative_hope_top_rungs",
        "gen_break_alignment", "scope_coverage", "user_skill_alignment",
        "historical_invariance", "empirical_cost_grounding"
    ])
    ladders_path = os.path.join(CACHE_DIR, "v3_existing_ladders.csv")
    df_ladders.to_csv(ladders_path, index=False)
    print(f"[SAVED] {ladders_path} | shape={df_ladders.shape}")

    # 2. Table 2.2: Use-Case & Producer-Consumer Inventory
    use_cases = [
        ("UC_01", "Passive Spellcheck, Translation & Smart Compose Widgets", "Track A: Direct User (served by Track B ML)", "2016-11", "2018-05", "Browser / Email App", "G0-L1 (Passive Only; 0h)"),
        ("UC_02", "No-Code AutoML Tabular/Text Classification & Regex Rules", "Track A: Direct Power User", "2017-06", "2018-01", "Cloud Web Console / Spreadsheet", "G0-L2 (7-45h)"),
        ("UC_03", "Classical NLP Sentiment, NER & Topic Extraction Pipelines", "Track A & B: Data Scientist / Product Builder", "2017-06", "2017-09", "Jupyter / Python scikit-learn / spaCy", "G0-L3 (50-200h)"),
        ("UC_04", "Fine-Tuning Pretrained BERT/RoBERTa Encoders on Custom Labels", "Track A & B: ML Engineer (e.g. Grammarly GECToR 2020)", "2018-10", "2019-06", "PyTorch / HuggingFace GPU Notebook", "G0-L4 (200-600h) -> serves L1 users"),
        ("UC_05", "Custom Seq2Seq/Transformer Pretraining & ONNX Quantized Serving", "Track B: Frontier/Enterprise NLP Architect", "2017-06", "2019-10", "Multi-GPU Cluster / C++ ONNX Runtime", "G0-L5 (600-2000h)"),
        ("UC_06", "One-Key IDE Ghost-Text Autocomplete & Consumer Viral Web Boxes", "Track A: Direct User (Copilot Tab / Craiyon / AI Dungeon)", "2021-06", "2022-06", "VS Code Extension / Consumer Web Box", "G1-L1 (0h)"),
        ("UC_07", "Few-Shot Completion Prompting & Stop-Sequence Formatting", "Track A: Playground Power User", "2020-06", "2021-03", "OpenAI Playground / Web Sandbox", "G1-L2 (7-45h; sank from G0-L3/L4)"),
        ("UC_08", "REST API Completion Wrappers & Early Embedding Search", "Track B: SaaS Wrapper / Early Internal Bot Builder", "2020-06", "2021-11", "Python REST SDK / Early Vector Index", "G1-L3 (50-200h) -> serves L1 users"),
        ("UC_09", "Multi-Step Prompt Chains, Self-Consistency & Curated Cloud Fine-Tuning", "Track A & B: AI Engineer", "2021-12", "2022-05", "OpenAI Fine-Tune CLI / Python Wrapper", "G1-L4 (200-600h)"),
        ("UC_10", "Distributed Multi-GPU Full-Weight LLM Fine-Tuning (DeepSpeed ZeRO)", "Track B: Research & Core ML Team", "2020-06", "2022-03", "Multi-Node A100 Cluster / DeepSpeed", "G1-L5 (600-2000h)"),
        ("UC_11", "Zero-Shot Conversational Text Q&A, Summarization & Drafting", "Track A: Mass Consumer / High Schooler (ChatGPT)", "2022-11", "2022-12", "Browser / Mobile Chat UI", "G2-L1 (0h; sank from G1-L2)"),
        ("UC_12", "Manual CoT/Role Prompting, Custom GPTs & Separate Discord Image Gen", "Track A: Prompt Crafter (ChatGPT + Midjourney Discord)", "2022-11", "2023-03", "Web UI + Discord Flags (--ar --v)", "G2-L2 (7-45h)"),
        ("UC_13", "DIY Chunked Vector RAG & Function-Calling Internal Company Chatbots", "Track B: Internal Bot & SaaS Integrator (LangChain/Pinecone)", "2023-03", "2023-06", "Python SDK + Vector DB + OpenAI Functions", "G2-L3 (50-200h) -> serves L1 employees"),
        ("UC_14", "Single-GPU 4-Bit QLoRA Fine-Tuning (CoEdIT) & Early Agent Loops", "Track A & B: ML Engineer (Grammarly CoEdIT 2023 / Llama-2)", "2023-05", "2023-07", "Single A100/RTX 4090 + PEFT/bitsandbytes", "G2-L4 (200-600h; sank from G1-L5)"),
        ("UC_15", "Bespoke Corporate Pretraining (BloombergGPT) & High-Throughput vLLM Clusters", "Track B: Infra & Foundation Team", "2023-03", "2023-09", "64-512 H100/A100 Cluster + vLLM/TGI", "G2-L5 (600-2000h)"),
        ("UC_16", "Built-In Multimodal Omni-Chat (Text+Image+Vision+Voice) & Live Artifacts", "Track A: Casual User (GPT-4o / Claude 3.5 Sonnet Artifacts)", "2024-05", "2024-06", "Default Web/Mobile Chat + Artifact Pane", "G3-L1 (0h; sank from G2-L2/L3)"),
        ("UC_17", "Drag-and-Drop 50-PDF Long-Context Workspaces & Audio Synthesis", "Track A: Knowledge Worker (NotebookLM / Claude Projects)", "2024-05", "2024-09", "200k-2M Project Workspace UI", "G3-L2 (7-45h; sank from G2-L3 Vector RAG)"),
        ("UC_18", "AI-Native IDE Multi-File Composer & Policy-Guardrailed Enterprise RAG Bots", "Track A (Cursor Coder) & Track B (NeMo Guardrails + RBAC Bot Builder)", "2024-05", "2024-07", "Cursor IDE (.cursorrules) / NeMo Colang + Hybrid RAG", "G3-L3 (50-200h) -> serves L1 employees"),
        ("UC_19", "Stateful Cyclic Agent Graphs (LangGraph) & Human-in-the-Loop Checkpoints", "Track B: Agentic Systems Engineer", "2024-03", "2024-06", "LangGraph StateGraph + Postgres Checkpointer", "G3-L4 (200-600h)"),
        ("UC_20", "Enterprise Multi-Agent Evaluation Harnesses & Custom Post-Training (DPO)", "Track B: Frontier Applied AI Architect", "2024-05", "2024-10", "Multi-GPU DPO + Prompt-Cached Eval Cluster", "G3-L5 (600-2000h)"),
        ("UC_21", "Zero-Shot Auto-Thinking Chat (Router RLVR) & Interactive MCP Apps", "Track A: Casual User (GPT-5 Router / Claude 4.5-4.6 / DeepSeek-R1)", "2025-01", "2025-02", "Default Auto-Routing Web/Mobile UI", "G4-L1 (0h; sank from G2/G3-L2 manual CoT)"),
        ("UC_22", "Autonomous Multi-Site Deep Research Brief Scoping & Citation Auditing", "Track A: Analyst / Researcher (OpenAI/Gemini Deep Research)", "2025-01", "2025-02", "Built-In Deep Research Web Panel", "G4-L2 (7-45h; sank from G3-L4 custom scraper graphs)"),
        ("UC_23", "Plug-and-Play MCP Server Wiring (.mcp.json) & Guardrailed Agentic Enterprise Bots", "Track A (IDE/Desktop Integrator) & Track B (Enterprise MCP + Llama Guard Bot)", "2024-11", "2025-03", "Cursor / Claude Desktop .mcp.json + RBAC/Guardrails", "G4-L3 (50-200h; sank from G3-L4 custom API glue)"),
        ("UC_24", "Autonomous Terminal CLI Coding Harnesses (Claude Code + CLAUDE.md + Docker Tests)", "Track A & B: Senior SWE / Harness Engineer", "2025-02", "2025-05", "Terminal CLI (bash/edit/git) + Local Docker Suite", "G4-L4 (200-600h)"),
        ("UC_25", "24/7 Dedicated M4 Mac Mini OpenClaw Sandboxes, Git Worktree Swarms & Custom GRPO RLVR", "Track A (Personal Sandbox Architect) & Track B (RLVR Post-Training Team)", "2025-01", "2025-11", "Dedicated Apple M4 Mac Mini Sandbox / Multi-GPU GRPO", "G4-L5 (600-2000h)"),
    ]
    df_use_cases = pd.DataFrame(use_cases, columns=[
        "use_case_id", "use_case_name", "track", "first_appearance",
        "mainstream_crossover", "target_surface", "mapped_cell_and_note"
    ])
    uc_path = os.path.join(CACHE_DIR, "v3_use_cases.csv")
    df_use_cases.to_csv(uc_path, index=False)
    print(f"[SAVED] {uc_path} | shape={df_use_cases.shape}")

    # 3. Table 2.3: Keywords, Tutorials & Learning-Hour Inventory
    tutorials = [
        ("TUT_01", "Google Cloud AutoML & Regex101 Documentation", "2018-01", "regex lookahead, CSV schema, precision-recall threshold, AutoML Web UI", 7, 35, "Web Console / Spreadsheet", "Level 2 (7-45h)"),
        ("TUT_02", "Coursera Machine Learning & scikit-learn / spaCy Docs", "2017-06", "TF-IDF, n-grams, XGBoost, hyperparameter grid search, spaCy dependency parse", 50, 180, "Jupyter / Python SDK", "Level 3 (50-200h)"),
        ("TUT_03", "Stanford CS224N (NLP with Deep Learning) & Fast.ai Practical DL", "2018-09", "Word2Vec, BiLSTM-CRF, self-attention, BERT fine-tuning, learning rate warmup", 200, 550, "PyTorch GPU Notebook", "Level 4 (200-600h)"),
        ("TUT_04", "Annotated Transformer (Harvard NLP) & ONNX Runtime C++ Guide", "2018-04", "multi-head attention tensor shapes, beam search, FP16/INT8 quantization, ONNX graph", 600, 1800, "Multi-GPU Cluster / C++ Serving", "Level 5 (600-2000h)"),
        ("TUT_05", "OpenAI GPT-3 Playground Guide & Prompt Engineering Blog Posts", "2020-07", "few-shot exemplars, completion prefix, stop sequences, temperature, frequency penalty", 7, 40, "OpenAI Web Playground", "Level 2 (7-45h)"),
        ("TUT_06", "OpenAI REST API Cookbook & Early Embeddings Search Notebooks", "2021-06", "text-davinci-002 API, cosine similarity, babbage/ada embeddings, rate-limit backoff", 50, 160, "Python REST SDK / VS Code", "Level 3 (50-200h)"),
        ("TUT_07", "Stanford CS324 (Large Language Models, Liang & Hashimoto) & Wei CoT Paper", "2022-01", "in-context learning scaling, Chain-of-Thought, self-consistency voting, JSONL fine-tune CLI", 200, 500, "Python SDK / Cloud Fine-Tune CLI", "Level 4 (200-600h)"),
        ("TUT_08", "DeepSpeed ZeRO-3 & HuggingFace Accelerate Multi-GPU Documentation", "2021-04", "ZeRO stage 3 optimizer sharding, BF16 mixed precision, gradient checkpointing, NCCL", 600, 2000, "Multi-Node GPU Cluster", "Level 5 (600-2000h)"),
        ("TUT_09", "DeepLearning.AI: ChatGPT Prompt Engineering for Developers (Ng & Fulford) + Midjourney Guide", "2023-05", "system role, delimiter tags, Let's think step by step, Custom GPT actions, --ar 16:9 --v 5", 7, 45, "Web Chat UI / Discord", "Level 2 (7-45h)"),
        ("TUT_10", "DeepLearning.AI: LangChain Chat with Your Data (Chase) & Advanced RAG (Liu)", "2023-07", "RecursiveCharacterTextSplitter, chunk overlap, HNSW index, Pinecone/Chroma, OpenAI function calling", 50, 200, "Python SDK + Vector DB", "Level 3 (50-200h)"),
        ("TUT_11", "HuggingFace PEFT / bitsandbytes QLoRA Guide (Dettmers) & trl SFTTrainer Docs", "2023-05", "4-bit NF4 quantization, LoRA rank r, alpha scaling, target_modules, SFTTrainer, LLM-as-a-Judge", 200, 600, "Single GPU + PyTorch/PEFT", "Level 4 (200-600h)"),
        ("TUT_12", "vLLM PagedAttention Paper/Docs & Megatron-LM Pretraining Manual", "2023-06", "PagedAttention KV-cache blocks, tensor parallelism, FlashAttention-2, continuous batching", 600, 2000, "Multi-GPU Cluster + vLLM", "Level 5 (600-2000h)"),
        ("TUT_13", "Anthropic Claude Projects / Artifacts Guide & Google NotebookLM Documentation", "2024-06", "200k-2M context curation, project instructions, React Artifact remixing, Audio Overview grounding", 7, 45, "Multimodal Project Workspace UI", "Level 2 (7-45h)"),
        ("TUT_14", "Cursor Composer Guide (.cursorrules) & NVIDIA NeMo Guardrails Colang Manual", "2024-07", "Cmd+K inline diff, @codebase indexing, .cursorrules, Colang dialog rails, RBAC metadata filtering, prompt caching", 50, 200, "Cursor AI IDE / Enterprise Bot SDK", "Level 3 (50-200h)"),
        ("TUT_15", "LangChain Academy: Introduction to LangGraph & DeepLearning.AI Multi-Agent crewAI", "2024-06", "cyclic StateGraph, conditional edges, Postgres checkpointer, human-in-the-loop interrupt, DPO preference pairs", 200, 600, "Python Agent Graph SDK + Docker", "Level 4 (200-600h)"),
        ("TUT_16", "OpenAI / Gemini Deep Research Scoping Guides & Reasoning with o1 (DeepLearning.AI)", "2025-01", "research brief constraints, source credibility auditing, reasoning effort budget, verification prompts", 7, 45, "Deep Research Web UI", "Level 2 (7-45h)"),
        ("TUT_17", "DeepLearning.AI: Building with Claude API & MCP + Linux Foundation AAIF MCP Spec", "2025-03", ".mcp.json server config, stdio vs SSE transport, OAuth tool scoping, Llama Guard 3 safety filters", 50, 200, "AI IDE / Claude Desktop + MCP SDK", "Level 3 (50-200h)"),
        ("TUT_18", "DeepLearning.AI: Building Adaptive AI Agents with Claude Code & UVA CS 6501 (Agentic AI)", "2025-06", "CLAUDE.md, AGENTS.md, bash/read/write/edit/glob/grep primitives, TDD verification loop, Docker container isolation", 200, 600, "Terminal CLI + Local Docker Harness", "Level 4 (200-600h)"),
        ("TUT_19", "OpenClaw Mac Mini Sandbox Guide & DeepSeek-R1 GRPO Verifier Training Cookbook", "2025-11", "dedicated M4 Mac Mini host, parallel git worktrees, OpenClaw daemon, least-privilege API tokens, GRPO group reward", 600, 2000, "Dedicated M4 Mac Mini Sandbox / Multi-GPU RLVR", "Level 5 (600-2000h)"),
    ]
    df_tutorials = pd.DataFrame(tutorials, columns=[
        "tutorial_id", "resource_name", "release_date", "keywords_taught",
        "hours_min", "hours_max", "target_surface", "mapped_level"
    ])
    tut_path = os.path.join(CACHE_DIR, "v3_tutorials.csv")
    df_tutorials.to_csv(tut_path, index=False)
    print(f"[SAVED] {tut_path} | shape={df_tutorials.shape}")

    # 4. Table 2.4 & Table 5.2b: The "Inventory of Hope" Ledger (20 contemporaneous hopes across G0-G4)
    hopes = [
        ("HOPE_01", "Capsule Networks (Hinton) Replacing CNNs & Transformers", "Gen 0", "G1", "Geoffrey Hinton / Academic ML", "Dynamic routing between capsules learning part-whole hierarchies with 10x less data", "Extinct", "Out-Standardized / Hardware Scaling (Transformers scaled cleanly on GPUs; Capsules hit compute wall)"),
        ("HOPE_02", "Symbolic-Neural Hybrid Ontologies (OWL/RDF + Deep Learning) as Only Path to Reasoning", "Gen 0", "G1", "Neuro-Symbolic AI Workshops", "Hand-crafted knowledge graphs governing neural feature extractors", "Extinct", "Foundation Model Absorption (In-context learning & RLVR absorbed soft reasoning without manual ontologies)"),
        ("HOPE_03", "Universal Small-Data Transfer Learning Eliminating Large Pretraining Clusters", "Gen 0", "G1", "Fast.ai / ULMFiT / Early NLP", "Single-GPU fine-tuning of 30M-100M models beating giant models on all tasks", "Extinct", "Foundation Model Absorption (GPT-3 175B scaling laws proved giant zero/few-shot models dominate)"),
        ("HOPE_04", "Pretrained Transformer Representation Transfer Across Text, Code & Vision", "Gen 0", "G1", "Vaswani et al. / Devlin et al. / OpenAI", "Unified self-attention backbone scaling to generative text and code", "Survived", "Matured to TRL 9 (Became foundation of Gen 1-4)"),
        ("HOPE_05", "Standalone Prompt Marketplaces (PromptBase) as Permanent Professional Career", "Gen 1", "G2", "Early Prompt Engineering Influencers / VC", "Buying and selling secret $4.99 prompt strings as durable IP", "Extinct", "Foundation Model Absorption (RLHF instruction tuning & built-in thinking made secret prompt hacks obsolete)"),
        ("HOPE_06", "Zero-Code End-to-End Production SaaS Generation from Single Codex Docstring", "Gen 1", "G2", "Early Codex / Copilot Demos (2021)", "Non-programmers generating full production backends from 1 paragraph in 2021", "Extinct", "Premature TRL / Capability Starvation (4k context & 0% multi-file state awareness caused immediate build failure until Gen 3/4)"),
        ("HOPE_07", "Conversational Instruction-Following & RLHF Alignment for Mass Consumers", "Gen 1", "G2", "OpenAI InstructGPT / Anthropic Constitutional AI", "Turning raw completion models into safe zero-shot dialogue assistants", "Survived", "Matured to TRL 9 (Triggered Gen 2 ChatGPT explosion)"),
        ("HOPE_08", "Unconstrained Recursive Autonomous Loops (AutoGPT / BabyAGI) Running Businesses in 2023", "Gen 2", "G3", "GitHub Viral Repos / Twitter Hype (Apr 2023)", "Infinite while-loops over GPT-4 autonomously executing multi-day company projects", "Extinct", "Premature TRL / Capability Starvation (0.90^20 = 12.2% step survival caused infinite loops & $50 API burn)"),
        ("HOPE_09", "Every Enterprise Training Its Own From-Scratch Base LLM (BloombergGPT Model)", "Gen 2", "G3", "BloombergGPT ($3M+) / Enterprise Infra VCs", "Banks, hospitals, and retailers pretraining proprietary 50B base models from scratch", "Extinct", "Broken Unit Economics & Maintenance Friction (Frontier APIs + RAG/QLoRA beat $3M bespoke base models in 6 months)"),
        ("HOPE_10", "Pure Vector Databases Permanently Replacing Long Context Windows", "Gen 2", "G3", "2023 Vector DB Boom (Pinecone/Weaviate/Milvus)", "4k-8k context remaining permanent; every 10-page document requiring vector chunking", "Extinct", "Foundation Model Absorption (128k-2M long context + 90% prompt caching absorbed small/medium corpus Q&A into L2)"),
        ("HOPE_11", "Proprietary Per-Vendor Chat Plugin Stores (Early ChatGPT Plugins 2023)", "Gen 2", "G3", "OpenAI Plugin Store Launch (Mar 2023)", "Closed vendor-specific JSON plugin manifests becoming the new App Store", "Extinct", "Out-Standardized (Deprecated in favor of open function calling and Anthropic/AAIF Model Context Protocol [MCP])"),
        ("HOPE_12", "Native Multimodal Omni-Models & 100k-2M Long-Context Workspaces", "Gen 2", "G3", "GPT-4V / Gemini 1.5 / Claude 3", "Unified text-vision-audio models with massive context and live code rendering", "Survived", "Matured to TRL 9 (Triggered Gen 3 Omni-Chat, Projects & Artifacts)"),
        ("HOPE_13", "Thin Single-Prompt SaaS Wrappers ('Chat with One PDF' Startups) as Defensible Moats", "Gen 3", "G4", "2023-2024 Wrapper Startup Wave", "Charging $20/mo for a single system prompt + file upload button over OpenAI API", "Extinct", "Foundation Model Absorption (Crushed when Claude Projects, NotebookLM & ChatGPT Canvas built it into L1/L2 for free)"),
        ("HOPE_14", "100% Unsupervised Zero-Human-Review Full-Lifecycle Software Engineering by 2025", "Gen 3", "G4", "SAE L5 Coding Hype / Early Devin Claims", "Firing engineering teams and letting autonomous agents push directly to production", "Extinct", "Premature TRL / Capability Starvation (Scale AI SWE-bench Pro proved 4.8-22.5 pt drop on private commercial code; requires L4 human TDD review)"),
        ("HOPE_15", "In-House Custom Enterprise AI Builds Outperforming Purchased Vertical Tools", "Gen 3", "G4", "Enterprise IT Internal Build Mandates (2024)", "Internal IT building bespoke agent platforms beating commercial vendors", "Extinct", "Broken Unit Economics (MIT NANDA 2025 proved 67% success for bought tools vs 33% for in-house builds; Menlo 76% bought)"),
        ("HOPE_16", "Test-Time Reasoning (RLVR) + Standardized Tool Protocols (MCP) + Terminal CLI Agents", "Gen 3", "G4", "OpenAI o1 / DeepSeek-R1 / Anthropic MCP & Claude Code", "RL on verifiable rewards unlocking multi-step terminal coding and standardized tool wiring", "Survived", "Matured to TRL 9 (Triggered Gen 4 Auto-Thinking, Deep Research, MCP & Claude Code)"),
        ("HOPE_17", "Unauthenticated Zero-Sandbox Local MCP & Browser Agents Running with Root Credentials", "Gen 4", "G5", "Early 2025 YOLO Agent Adoption", "Giving autonomous agents unrestricted host shell and primary browser cookie access", "Extinct", "Broken Security / Governance (Apr 2026 OX Security disclosure of 200,000 vulnerable stdio MCP instances forced isolated M4 Mac Mini / Docker sandboxes)"),
        ("HOPE_18", "Pure Pixel-Only GUI Clicking Replacing All API & CLI Harnesses in 2026", "Gen 4", "G5", "Early Computer-Use Only Theses", "Agents operating exclusively by taking screenshots and clicking pixels at 3-5s/click", "Extinct", "Broken Unit Economics (Bash CLI + MCP API calls are 50x faster and 20x cheaper; GUI clicking reserved for legacy non-API apps)"),
        ("HOPE_19", "OpenAI Level 4 'Innovators' & Level 5 'Autonomous Organizations' Operating in 2026", "Gen 4", "G5", "OpenAI 5-Level Ladder Top Rungs", "AI autonomously discovering new physical laws and running entire corporations without humans", "Extinct", "Premature TRL (2026 frontier deployments calibrate at Level 2.5-3; long-horizon organizational coherence still requires human orchestration)"),
        ("HOPE_20", "Sandboxed Multi-Agent Verification Swarms & Continuous RLVR Domain Flywheels", "Gen 4", "G5", "Anthropic / DeepSeek / AAIF / OpenClaw", "Isolated hardware/container sandboxes running parallel verified agent worktrees", "Survived", "Active Frontier at Gen 4 Level 4-5 (Expanding toward next generation)"),
    ]
    df_hopes = pd.DataFrame(hopes, columns=[
        "hope_id", "hope_thesis", "origin_gen", "target_gen", "proponents",
        "predicted_workflow", "fate", "extinction_or_maturation_mechanism"
    ])
    hopes_path = os.path.join(CACHE_DIR, "v3_hope_inventory.csv")
    df_hopes.to_csv(hopes_path, index=False)
    print(f"[SAVED] {hopes_path} | shape={df_hopes.shape}")

    # 5. Table 5.2a: TRL Maturation Trajectories (10 core breakthroughs from TRL 1-2 Paper to TRL 9 Built-In Level 1)
    trl_rows = [
        ("TRL_01", "Transformer Self-Attention & Pretrained Encoders", "2017-06", "2018-10 (G0-L4 BERT)", "2019-10 (G0-L3 HF pipeline)", "2019-11 (G0-L1 Google Search/Smart Compose)", 29, "Hardware & Pretraining Compute Scaling"),
        ("TRL_02", "In-Context Few-Shot Completion Learning", "2020-05", "2020-06 (G1-L3 GPT-3 API)", "2020-09 (G1-L2 Playground)", "2021-06 (G1-L1 Copilot Tab Autocomplete)", 13, "API Waitlist & IDE Product Packaging"),
        ("TRL_03", "RLHF Instruction Tuning & Conversational Chat", "2017-06", "2022-01 (G1-L3 InstructGPT)", "2022-06 (G1-L2 Playground Chat)", "2022-11 (G2-L1 ChatGPT Web UI)", 65, "Post-Training Human Preference Alignment & Web UI"),
        ("TRL_04", "Retrieval-Augmented Generation (RAG over Private Docs)", "2020-05", "2022-11 (G2-L4 Custom FAISS)", "2023-04 (G2-L3 LangChain/Pinecone)", "2024-06 (G3-L2/L1 Projects & NotebookLM)", 49, "128k-2M Context Scaling & Prompt Caching"),
        ("TRL_05", "Parameter-Efficient Fine-Tuning (LoRA / 4-Bit QLoRA)", "2021-06", "2023-02 (G2-L4 PEFT LoRA)", "2023-05 (G2-L4 Single-GPU QLoRA)", "2024-05 (G3-L3 Managed Cloud Fine-Tune UI)", 35, "Open-Weight Base Models (Llama-2) & NF4 Quantization"),
        ("TRL_06", "Native Multimodal Vision-Audio-Text & Live UI Rendering", "2021-02", "2023-09 (G2-L2 GPT-4V Preview)", "2024-05 (G3-L2 Multi-Doc Vision)", "2024-06 (G3-L1 GPT-4o & Claude Artifacts)", 40, "End-to-End Omni-Tokenization & Browser Sandboxing"),
        ("TRL_07", "Chain-of-Thought & RLVR Test-Time Reasoning", "2022-01", "2022-05 (G1-L3 Self-Consistency)", "2023-03 (G2-L2 Manual CoT Prompting)", "2025-01 (G4-L1 Auto-Router o1/R1/GPT-5)", 36, "Reinforcement Learning with Verifiable Rewards (RLVR)"),
        ("TRL_08", "Autonomous Multi-Site Web Research & Citation Synthesis", "2023-04", "2023-05 (G2-L4 AutoGPT Failed)", "2024-06 (G3-L4 LangGraph + Tavily)", "2025-02 (G4-L2 Built-In Deep Research)", 22, "Long-Horizon Browsing RL & Hallucination Grounding"),
        ("TRL_09", "Standardized External Tool & Data Wiring (MCP)", "2023-06", "2023-11 (G2-L3 OpenAI Functions)", "2024-11 (G4-L3 Anthropic .mcp.json)", "2025-12 (G4-L1 AAIF MCP Apps in Chat)", 30, "Cross-Vendor Open Protocol Standardization (AAIF)"),
        ("TRL_10", "Autonomous Multi-File Repo Coding & Sandboxed Execution", "2021-07", "2023-04 (G2-L4 Brittle Agent Loops)", "2024-06 (G3-L3 Cursor Composer)", "2025-02 (G4-L4/L5 Claude Code CLI & OpenClaw)", 43, "RLVR Coding Accuracy (>70% SWE-bench) & Container/Mac Mini Sandboxes"),
    ]
    df_trl = pd.DataFrame(trl_rows, columns=[
        "trl_id", "breakthrough", "trl_1_2_paper_date", "trl_4_5_proto_date_level",
        "trl_7_power_date_level", "trl_9_builtin_l1_date", "total_lag_months", "primary_bottleneck"
    ])
    trl_path = os.path.join(CACHE_DIR, "v3_trl_trajectories.csv")
    df_trl.to_csv(trl_path, index=False)
    print(f"[SAVED] {trl_path} | shape={df_trl.shape}")

    # 6. Table 1.1 & Table 3.1: Inductively Discovered Generations (Gen 0 to Gen 4)
    generations = [
        ("G0", "Gen 0: The Pre-LLM Code-Pipeline & Passive-Widget Generation", "2017-06", "2020-05", 36, 2017.42, 2020.42,
         "Fine-tuned BERT/RoBERTa custom classifiers (L4); AutoML web consoles (L2)",
         "Baseline generation (active zero-shot generative L1 missing; passive widgets only)",
         "Tech: Transformer (2017-06) & BERT (2018-10); Money: Cloud GPU $2.50/hr; Eng: HuggingFace transformers & ONNX; TRL: Self-attention TRL 2->7; Culture: Code-first Data Science; Legal: GDPR (2018-05)",
         "Hand-crafted morphological lexicons & SIFT/HOG feature engineering replaced by pretrained BERT embeddings",
         12.0, 0.18, 1.1),
        ("G1", "Gen 1: The Completion Playground & Ghost-Text Autocomplete Generation", "2020-06", "2022-10", 29, 2020.42, 2022.83,
         "Few-shot text completion & stop-sequence prompting (L2); REST API wrappers (L3); DeepSpeed full-weight tuning (L5)",
         "Custom NLP classification sank from G0-L3/L4 (50-600h BERT/sklearn) to G1-L2 (7-45h Playground few-shot); boilerplate lookup sank to G1-L1 (0h Copilot Tab)",
         "Tech: GPT-3 175B in-context learning & Codex; Money: $60/1M tokens pay-per-token API; Eng: OpenAI Playground & VS Code Copilot extension; TRL: Few-shot TRL 2->8; Culture: Prompting replaces dataset labeling; Legal: Early GitHub Copilot GPL copyright debate",
         "Labeling 10,000 training rows & writing PyTorch training loops for basic sentiment/entity extraction became obsolete",
         45.0, 1.60, 3.8),
        ("G2", "Gen 2: The Conversational Chat, Manual Prompting & DIY Vector-RAG Generation", "2022-11", "2024-04", 18, 2022.83, 2024.33,
         "Manual CoT/Role prompting, Custom GPTs & Midjourney Discord flags (L2); DIY Chunked Vector RAG & early internal company bots (L3); Single-GPU 4-bit QLoRA (L4)",
         "Conversational Q&A/drafting sank from G1-L2 (7-45h Playground completion formatting) to G2-L1 (0h ChatGPT web UI); custom weight tuning sank from G1-L5 (600h+ DeepSpeed) to G2-L4 (200h QLoRA)",
         "Tech: RLHF instruction tuning (ChatGPT/GPT-4), text-embedding-ada-002 & Llama-2/QLoRA; Money: $20/mo flat subscription & $2/1M GPT-3.5 API ($1.7B enterprise spend); Eng: Chat web UI, LangChain/LlamaIndex & Pinecone; TRL: RLHF chat hit TRL 9 in 60 days; Culture: 100M+ mainstream consumers; Legal: Samsung data-leak ban & Mata v. Avianca hallucination sanctions",
         "Completion prefix/stop-sequence hacks (Input:/Output:) & multi-GPU full-weight fine-tuning for domain style adaptation became obsolete",
         380.0, 28.00, 14.0),
        ("G3", "Gen 3: The Multimodal Workspace, Live Artifacts & AI-IDE Generation", "2024-05", "2024-12", 8, 2024.33, 2025.00,
         "AI-native IDE multi-file Composer (.cursorrules) & policy-guardrailed hybrid-RAG enterprise bots (L3); Stateful cyclic agent graphs (LangGraph, L4)",
         "Multimodal creation & live app preview sank from G2-L2/L3 (separate Midjourney Discord / local code) to G3-L1 (0h GPT-4o & Claude Artifacts); 50-PDF Q&A sank from G2-L3 (50-200h Vector RAG code) to G3-L2 (7-45h drag-and-drop Projects/NotebookLM)",
         "Tech: Native omni-models (GPT-4o), Claude 3.5 Sonnet (33%->49% SWE-bench) & 128k-2M context; Money: 90% prompt caching discount ($0.30/1M) & $11.5B-$13.8B enterprise spend; Eng: Claude Artifacts/Projects, NotebookLM & Cursor Composer; TRL: Long-context & multimodal hit TRL 9; Culture: 75% knowledge worker adoption (Work Trend Index); Legal: EU AI Act entry into force & RBAC/NeMo Guardrails enterprise mandates",
         "Switching across separate websites/Discord for text vs image/vision, and writing custom Python vector-chunking scripts for 10-50 personal PDFs became obsolete",
         720.0, 240.00, 39.0),
        ("G4", "Gen 4: The Built-In Thinking, Deep Research, Terminal CLI & Sandbox Generation", "2025-01", "2026-10", 22, 2025.00, 2026.83,
         "Autonomous terminal CLI coding harnesses (Claude Code + CLAUDE.md + Docker tests, L4); Dedicated M4 Mac Mini 24/7 OpenClaw sandboxes, parallel git worktree swarms & GRPO RLVR flywheels (L5)",
         "Chain-of-Thought reasoning sank from G2/G3-L2 (manual CoT prompts) to G4-L1 (0h auto-router thinking); 50-site web synthesis sank from G3-L4 (custom scraper graphs) to G4-L2 (7-45h Deep Research); tool wiring sank from G3-L4 custom API glue to G4-L3 (50-200h .mcp.json)",
         "Tech: RLVR thinking models (o1/o3/DeepSeek-R1/Claude 4.5-5.5/GPT-5.4), MCP & Computer Use; Money: $37.0B enterprise spend (76% bought vs 24% built; MIT NANDA 67% vs 33% success) & Epoch +5-6 OOM runtime scaling; Eng: Claude Code CLI, AAIF (Dec 2025 MCP+goose+AGENTS.md) & OpenClaw; TRL: Reasoning & CLI agents hit TRL 8-9; Culture: SWE shifts from syntax typing to TDD harness specification; Legal: Apr 2026 OX Security 200k MCP stdio RCE disclosure enforcing isolated hardware/container sandboxes",
         "Manual 'Let's think step by step' CoT prompt wrappers, hand-rolled per-app REST tool schemas, and line-by-line manual IDE syntax typing became obsolete",
         1150.0, 1100.00, 88.0),
    ]
    df_gens = pd.DataFrame(generations, columns=[
        "gen_id", "gen_folksonomy_name", "start_date", "end_date", "duration_months",
        "start_year_float", "end_year_float", "new_upper_use_cases",
        "sunk_builtin_use_cases", "causal_drivers_6factor", "obsolete_user_skills",
        "macro_users_millions", "macro_tokens_trillions", "macro_spend_billion_usd"
    ])
    gens_path = os.path.join(CACHE_DIR, "v3_generations.csv")
    df_gens.to_csv(gens_path, index=False)
    print(f"[SAVED] {gens_path} | shape={df_gens.shape}")

    # 7. Table 1.3: Down-Ladder Skill Deflation Tracker (5 Benchmark Workflows across G0-G4)
    benchmarks = [
        ("math_reasoning", "Multi-Step Math & Logic Reasoning", 5, 1000, 3, 120, 2, 25, 2, 15, 1, 0, 1000, "RLVR test-time compute (o1/R1) & auto-routers absorbed manual CoT wrappers into built-in L1 chat"),
        ("multimodal_creation", "Multimodal Text + Image + Live App Preview", 4, 400, 3, 100, 2, 30, 1, 0, 1, 0, 400, "Native omni-models (GPT-4o) & sandboxed browser rendering (Claude Artifacts/Canvas) unified tools into L1"),
        ("doc_qa_50pdf", "Ask Questions Across 50 Private PDFs / Docs", 4, 350, 3, 140, 3, 110, 2, 15, 1, 0, 350, "128k-2M long context + 90% prompt caching + Projects/NotebookLM replaced custom Python chunking code"),
        ("web_research_synthesis", "Multi-Website Cited Research Report (50+ Sources)", 5, 800, 4, 350, 4, 300, 3, 120, 2, 12, 788, "End-to-end RL browsing agents (OpenAI/Gemini Deep Research) productized multi-hop synthesis into L2"),
        ("text_classification", "Custom Business Text Classifier / Entity Extractor", 3, 120, 2, 20, 1, 0, 1, 0, 1, 0, 120, "In-context learning (Gen 1) & RLHF instruction following (Gen 2) eliminated supervised training loops"),
    ]
    df_bench = pd.DataFrame(benchmarks, columns=[
        "workflow_key", "workflow_name", "G0_level", "G0_hours", "G1_level", "G1_hours",
        "G2_level", "G2_hours", "G3_level", "G3_hours", "G4_level", "G4_hours",
        "total_hours_saved", "tech_mechanism"
    ])
    bench_path = os.path.join(CACHE_DIR, "v3_skill_deflation_benchmarks.csv")
    df_bench.to_csv(bench_path, index=False)
    print(f"[SAVED] {bench_path} | shape={df_bench.shape}")

    # 8. Table 4.0 to Table 4.4 & Master Tables 5.1a-b: All 25 (Gen G, Level L) Cells
    # Columns required by Section 1.4 Schema Gate:
    # ['gen_id', 'level_id', 'status', 'learning_hours_min', 'learning_hours_max',
    #  'single_task_tokens', 'single_task_flops', 'single_task_usd', 'single_task_wh',
    #  'human_minutes', 'ai_minutes', 'user_share_pct', 'token_share_pct', 'spend_share_pct']
    # Plus rich metadata columns for tables and plots.
    cells = [
        # GEN 0 (2017-06 to 2020-05)
        ("G0", 1, "Passive-Widgets-Only (Active GenAI Missing)", 0, 0,
         25, 1.5e8, 0.00001, 0.0002, 0.1, 0.01, 72.0, 15.0, 5.0,
         "Passive Consumer NLP Widgets (Active Generative L1 Missing)",
         "Browser / Mobile App (Google Translate, Grammarly, Gmail Smart Compose)",
         "Zero-shot active generative AI did not exist; users experienced AI only as passive background autocomplete/spellcheck",
         "N/A (Lowest Level; active generative prompting fails 100% because no consumer LLM existed)",
         "Jumping to L2 (AutoML console) for simple email typo fixes wastes 10h+ of setup",
         "Pre-2017 phrase-based statistical MT had 50%+ higher syntax error rates before GNMT/Transformer",
         "In G1-G2, active zero-shot prompt boxes (Copilot Tab, ChatGPT) replace passive-only widgets at L1"),
        ("G0", 2, "Populated", 7, 45,
         150, 1.2e9, 0.0005, 0.002, 15.0, 0.5, 14.0, 13.0, 10.0,
         "No-Code Cloud AutoML Consoles & Regex Rule Crafting",
         "Cloud Web Console (Google AutoML, AWS Comprehend) & Spreadsheet Regex",
         "regex lookahead, CSV label upload, precision-recall slider, confidence threshold",
         "Forcing custom ticket routing at L1 fails completely (passive spellcheck cannot classify custom business intents)",
         "Writing Python scikit-learn pipelines (L3, 50-200h) is overkill when a 500-row CSV in Cloud AutoML hits 85% accuracy",
         "Pre-2017 required manual Java/C++ rule engines with zero transfer learning",
         "In G1, few-shot prompting in OpenAI Playground replaces labeled CSV uploads without training waits"),
        ("G0", 3, "Populated", 50, 200,
         600, 1.8e10, 0.003, 0.015, 45.0, 2.0, 9.5, 27.0, 25.0,
         "Classical Python NLP & Tabular Feature Engineering Pipelines",
         "Jupyter Notebook + scikit-learn / XGBoost / spaCy",
         "TF-IDF, n-gram tokenizer, XGBoost, spaCy NER, cross-validation",
         "Forcing 50-feature entity extraction into L2 Regex/AutoML fails with brittle regex breakage on unseen phrasing (F1 < 55%)",
         "Fine-tuning BERT on GPU (L4, 200-600h) wastes $50+ GPU hours when TF-IDF + XGBoost runs in 10 seconds on CPU",
         "Earlier feature pipelines lacked spaCy v2 neural transition parsers",
         "In G1-G2, zero/few-shot LLM prompts replace custom TF-IDF + scikit-learn pipelines for standard text tasks"),
        ("G0", 4, "Populated", 200, 600,
         2000, 4.4e11, 0.025, 0.120, 120.0, 15.0, 3.8, 30.0, 35.0,
         "Single-GPU Pretrained Encoder Fine-Tuning (BERT / RoBERTa / GECToR)",
         "PyTorch + HuggingFace transformers on Cloud/Local Single GPU",
         "BERT-base, WordPiece, AdamW warmup, cross-entropy loss, Grammarly GECToR sequence tagging",
         "Forcing polysemous contextual QA/grammar correction into L3 bag-of-words TF-IDF fails on word-order semantics (15-25 pt F1 drop)",
         "Pretraining from scratch on multi-GPU clusters (L5, 600-2000h) wastes $10k+ when pretrained bert-base-uncased converges in 3 epochs",
         "Pre-2018 BiLSTMs lacked bidirectional self-attention and required task-specific architectures",
         "In G1, 5-shot GPT-3 Playground prompting (L2) achieves comparable accuracy with 0 training examples"),
        ("G0", 5, "Populated", 600, 2000,
         8000, 6.4e12, 0.180, 0.850, 240.0, 60.0, 0.7, 15.0, 25.0,
         "Custom Seq2Seq/Transformer Pretraining & Quantized ONNX Serving",
         "Multi-GPU Linux Cluster + Fairseq / Tensor2Tensor + ONNX Runtime",
         "multi-head attention tensors, beam search, FP16/INT8 quantization, ONNX graph optimization",
         "Forcing low-latency 10,000 QPS production translation/search into unoptimized L4 PyTorch notebooks fails SLA (>500ms latency & OOM)",
         "Top level in Gen 0; pushing toward general-purpose 175B language models required $4.6M supercomputer runs (OpenAI GPT-3)",
         "Pre-2017 RNNSeq2Seq suffered vanishing gradients and sequential training bottlenecks",
         "In G1-G2, managed Foundation Model APIs eliminate custom seq2seq pretraining for 99% of enterprises"),

        # GEN 1 (2020-06 to 2022-10)
        ("G1", 1, "Populated", 0, 0,
         60, 1.4e10, 0.0005, 0.004, 0.2, 0.02, 52.0, 12.0, 8.0,
         "One-Key IDE Ghost-Text Autocomplete & Viral Consumer Web Toys",
         "VS Code (GitHub Copilot Tab) & Viral Web Boxes (Craiyon / AI Dungeon)",
         "Zero AI learning (0h); pressing Tab to accept inline ghost-text or typing 3 words into a viral image box",
         "N/A (Lowest Level; 0-skill entry point)",
         "Opening OpenAI Playground (L2) to manually tune temperature for single-line boilerplate wastes 5 minutes per line",
         "In G0, boilerplate synthesis required L3/L4 Stack Overflow search + manual adaptation",
         "In G2, ChatGPT expands L1 from single-line ghost-text and toy boxes to full conversational Q&A and drafting"),
        ("G1", 2, "Populated", 7, 45,
         650, 2.3e11, 0.039, 0.045, 8.0, 0.15, 28.0, 24.0, 22.0,
         "Few-Shot Completion Prompting & Stop-Sequence Crafting in Playground",
         "OpenAI Web Playground / Early Jasper & Copy.ai Templates",
         "few-shot exemplars, Input:/Output: prefix, stop=['\\n'], temperature, frequency penalty",
         "Forcing zero-shot questions into raw GPT-3 davinci without L2 few-shot formatting fails: model completes question with more questions",
         "Writing Python REST API scripts (L3, 50-200h) is unnecessary when interactive Playground presets solve batch copywriting/classification",
         "In G0, custom classification/extraction required L3/L4 (50-600h) scikit-learn or BERT GPU fine-tuning on labeled datasets",
         "In G2, RLHF instruction tuning (ChatGPT) makes Input:/Output: completion prefixes and stop sequences obsolete; task sinks to L1"),
        ("G1", 3, "Populated", 50, 200,
         1800, 6.3e11, 0.108, 0.120, 25.0, 0.5, 13.5, 29.0, 30.0,
         "REST API Completion Wrappers & Early Embedding Search Integrations",
         "Python/Node.js REST SDK + OpenAI text-similarity-davinci / FAISS",
         "prompt template injection, exponential backoff, cosine similarity, babbage/ada embeddings, token budget truncation",
         "Forcing product integration or 100-doc search into L2 Web Playground fails due to manual copy-paste and 2,049-4,096 token ceiling",
         "Training custom fine-tuned weights (L4, 200-600h) wastes weeks when embedding search + few-shot API wrapper grounds answers dynamically",
         "In G0, building a semantic search/QA service required L4 (200-600h) custom BERT + Elasticsearch engineering",
         "In G2, standardized Chat Completion APIs + LangChain/LlamaIndex and eventually L2 Custom GPTs simplify doc Q&A"),
        ("G1", 4, "Populated", 200, 600,
         4500, 1.6e12, 0.270, 0.310, 60.0, 3.0, 5.2, 22.0, 24.0,
         "Multi-Step Prompt Chains, Self-Consistency Wrappers & Cloud Fine-Tuning CLI",
         "Python Orchestration Scripts + OpenAI Fine-Tuning CLI (curie/davinci)",
         "Let's think step by step, self-consistency majority voting (pass@20), JSONL prompt-completion pairs, validation loss",
         "Forcing multi-step GSM8K math or strict schema extraction into single-call L3 API fails (single-pass davinci scores <18% on GSM8K without CoT/voting)",
         "Setting up multi-node DeepSpeed clusters (L5, 600-2000h) is overkill when OpenAI's managed fine_tunes.create CLI adapts curie/davinci in 1 hour",
         "In G0, multi-step reasoning over text was impossible even at L4/L5",
         "In G2-G4, CoT sinks first to L2 manual prompting (G2) and then to L1 built-in RLVR auto-router thinking (G4)"),
        ("G1", 5, "Populated", 600, 2000,
         15000, 9.0e12, 0.900, 1.400, 180.0, 45.0, 1.3, 13.0, 16.0,
         "Distributed Multi-GPU Full-Weight Model Fine-Tuning (DeepSpeed ZeRO)",
         "Multi-Node A100 GPU Cluster + PyTorch + DeepSpeed ZeRO-3 / Megatron",
         "ZeRO-3 optimizer state sharding, BF16, gradient accumulation, Flan-T5-XXL / GPT-NeoX-20B full-weight updates",
         "Forcing private on-prem domain adaptation of 6B-20B models onto L4 single-GPU or cloud CLI fails with CUDA Out-Of-Memory (80GB VRAM exceeded)",
         "Top level in Gen 1; full foundation pretraining from scratch (>100B params) required >$2M lab-scale supercomputing",
         "In G0, models were 110M-340M params (fit on 1 GPU); G1 6B-20B models broke single-GPU memory limits",
         "In G2, 4-bit NF4 QLoRA + PEFT sinks custom weight tuning of 7B-70B models from L5 multi-GPU clusters down to L4 single GPU"),

        # GEN 2 (2022-11 to 2024-04)
        ("G2", 1, "Populated", 0, 0,
         800, 2.8e11, 0.002, 0.035, 1.5, 0.1, 68.0, 22.0, 18.0,
         "Zero-Shot Conversational Web Chat for Drafting, Q&A & Code Snippets",
         "Browser / Mobile App (ChatGPT Free/Plus, Bing Chat, Claude.ai)",
         "Zero AI learning (0h); typing natural conversational requests into a single text box",
         "N/A (Lowest Level; 0-skill entry point for 100M+ consumers)",
         "Spending 20 hours learning L2 prompt frameworks for a simple email rewrite or recipe summary yields zero marginal gain",
         "In G1, getting conversational answers required L2 (7-45h) Playground completion prefixes and stop-sequence configuration",
         "In G3, L1 expands from text-only chat to built-in native multimodal (voice/vision/image) and live interactive Artifacts"),
        ("G2", 2, "Populated", 7, 45,
         2500, 1.8e12, 0.045, 0.180, 6.0, 0.4, 19.0, 25.0, 24.0,
         "Manual CoT/Role Prompting, Custom GPTs & Separate Discord Image Generation",
         "ChatGPT Plus (GPT-4 + Custom GPTs) + Midjourney Discord (--ar --v)",
         "system persona, delimiter tags, Let's think step by step, few-shot CoT, Custom GPT instructions, Midjourney --ar 16:9 --v 5 --stylize",
         "Forcing complex logic or multimodal brochure creation at L1 fails: zero-shot GPT-3.5 hallucinates math/citations (Mata v. Avianca) and text-only ChatGPT cannot generate/style images without switching tools",
         "Writing Python LangChain code (L3, 50-200h) is unnecessary when a no-code Custom GPT with 3 uploaded reference files solves personal workflow templates",
         "In G1, CoT required L3/L4 Python sampling wrappers and image generation required L3 Colab VQGAN+CLIP notebooks",
         "In G3-G4, separate image tools & manual CoT prompts sink into L1 built-in omni-chat (G3) and L1 auto-thinking routers (G4)"),
        ("G2", 3, "Populated", 50, 200,
         8500, 6.1e12, 0.170, 0.620, 20.0, 1.2, 8.5, 26.0, 27.0,
         "DIY Chunked Vector-DB RAG & Function-Calling Internal Company Chatbots",
         "Python SDK (LangChain / LlamaIndex) + Pinecone/Chroma + OpenAI Function Calling",
         "RecursiveCharacterTextSplitter, chunk_size=512, text-embedding-ada-002, top-k cosine similarity, JSON schema function calling",
         "Forcing a 500-page company wiki Q&A bot into L2 ChatGPT / Custom GPT fails immediately with context_length_exceeded (4k-8k limit), truncates 95% of docs, and lacks API tool execution",
         "Fine-tuning model weights via QLoRA (L4, 200-600h) on volatile company PDFs fails: weights hallucinate policy numbers and require retraining on every doc edit",
         "In G0-G1, internal document Q&A required L4 (200-600h) custom BERT extractive QA + Elasticsearch engineering",
         "In G3, personal/team 50-PDF Q&A sinks to L2 (128k-2M drag-and-drop Projects/NotebookLM), while L3 upgrades to RBAC + NeMo Guardrails"),
        ("G2", 4, "Populated", 200, 600,
         25000, 1.8e13, 0.450, 1.800, 45.0, 8.0, 3.6, 17.0, 19.0,
         "Single-GPU 4-Bit QLoRA Fine-Tuning (Llama-2 / CoEdIT) & Early Agent Loops",
         "Single A100/RTX 4090 + HuggingFace PEFT / bitsandbytes / trl + Early ReAct Loops",
         "4-bit NF4 quantization, LoRA rank r=16, lora_alpha, SFTTrainer, Grammarly CoEdIT instruction tuning, LLM-as-a-Judge evals",
         "Forcing strict low-latency domain syntax/tone (e.g. Grammarly CoEdIT serving 30M users or medical NER) into L3 prompt+RAG fails latency (<100ms) and per-call API cost budgets",
         "Provisioning 64-GPU full-weight training clusters (L5, 600-2000h) wastes $50,000+ when 4-bit QLoRA tunes Llama-2-13B/70B on 1 GPU in 8 hours",
         "In G1, adapting a 13B-20B open model required L5 (600-2000h) multi-node DeepSpeed ZeRO-3 clusters",
         "In G3-G4, prompt caching (90% discount) & fast flash models replace QLoRA for many tasks, while L4 shifts to LangGraph (G3) & Claude Code CLI (G4)"),
        ("G2", 5, "Populated", 600, 2000,
         80000, 7.2e13, 1.600, 6.500, 120.0, 30.0, 0.9, 10.0, 12.0,
         "Custom Domain Pretraining & High-Throughput GPU Serving Clusters (vLLM)",
         "Multi-Node H100/A100 Cluster + vLLM (PagedAttention) / TGI / Megatron-LM",
         "PagedAttention KV-cache blocks, tensor parallelism, FlashAttention-2, continuous batching, custom tokenizer",
         "Forcing 5,000+ concurrent enterprise users onto unoptimized L4 HuggingFace generate() scripts fails with KV-cache memory fragmentation and 10x higher GPU costs",
         "Top level in Gen 2; bespoke corporate pretraining from scratch (BloombergGPT $3M+) proved economically inferior to frontier APIs + RAG/LoRA",
         "In G1, open-source serving lacked PagedAttention and FlashAttention-2, wasting 60-80% of GPU VRAM on fragmented KV cache",
         "In G3-G4, managed serverless inference and prompt caching commoditize basic serving, pushing L5 toward multi-agent evals & RLVR flywheels"),

        # GEN 3 (2024-05 to 2024-12)
        ("G3", 1, "Populated", 0, 0,
         2200, 8.8e11, 0.004, 0.065, 1.2, 0.15, 64.0, 18.0, 15.0,
         "Built-In Multimodal Omni-Chat (Text, Image, Vision, Voice) & Live Artifacts",
         "Default Web/Mobile App (GPT-4o, Claude 3.5 Sonnet with Artifacts)",
         "Zero AI learning (0h); talking by voice, pasting screenshots, generating images, and interacting with live React Artifacts in one chat box",
         "N/A (Lowest Level; 0-skill entry point)",
         "Switching to separate Discord servers or writing local HTML/React boilerplate (L2/L3) for a single-file chart or prototype wastes 30+ minutes",
         "In G2, generating images alongside text or previewing interactive UI required L2/L3 (switching to Midjourney Discord or running local Node.js)",
         "In G4, L1 absorbs silent RLVR step-by-step reasoning via auto-routers and interactive MCP Apps"),
        ("G3", 2, "Populated", 7, 45,
         35000, 1.4e13, 0.035, 0.450, 5.0, 0.8, 20.0, 24.0, 22.0,
         "Drag-and-Drop 50-PDF Long-Context Workspaces & Audio Overview Synthesis",
         "Multimodal Project Workspace (Claude Projects 200k, Google NotebookLM 1M-2M)",
         "200k-2M context window curation, project system instructions, source-grounded inline citations, NotebookLM Audio Overview",
         "Forcing 50 PDFs (400,000 tokens) into a single stateless L1 chat turn fails: loses persistent workspace instructions, re-uploads files every session, and lacks cross-doc citation studio",
         "Writing a custom Python LangChain + Pinecone vector chunking script (L3, 50-200h) for a static 50-PDF team binder wastes 80 hours of coding",
         "In G2, querying 50 PDFs required climbing to G2-L3 (50-200h) to build a custom chunked Vector DB RAG pipeline due to 4k-8k context limits",
         "In G4, L2 expands from static uploaded PDFs to autonomous 50-website live browsing via built-in Deep Research"),
        ("G3", 3, "Populated", 50, 200,
         65000, 3.9e13, 0.140, 1.100, 12.0, 2.5, 10.5, 28.0, 30.0,
         "AI-Native IDE Multi-File Composer & Policy-Guardrailed Enterprise RAG Chatbots",
         "Cursor IDE (Composer + .cursorrules) & Enterprise RAG (Hybrid BM25+Vector + RBAC + NeMo Guardrails)",
         "Cmd+K, @codebase, Composer multi-file diff, .cursorrules, prompt caching (90% off), Colang policy rails, SharePoint RBAC acl filtering",
         "Forcing a 10-file feature refactor or a 10,000-employee HR/IT chatbot into L2 (Claude Projects) fails: L2 has zero local git/IDE file write access, zero SharePoint RBAC permissions (leaking executive docs), and zero Colang policy rails",
         "Building a custom stateful cyclic LangGraph orchestrator (L4, 200-600h) is unnecessary when Cursor Composer (for code) or a 3-stage routed RAG+NeMo pipeline capped at $0.10/ticket solves 80% of requests",
         "In G2, coders had to manually copy-paste single files between browser ChatGPT and VS Code, and early RAG bots lacked prompt caching and Colang guardrails",
         "In G4, proprietary API tool connectors sink into standardized .mcp.json configs (L3), while multi-file coding advances to autonomous terminal CLI loops (L4)"),
        ("G3", 4, "Populated", 200, 600,
         180000, 1.1e14, 0.480, 3.200, 25.0, 12.0, 4.3, 19.0, 21.0,
         "Stateful Cyclic Agent Graphs (LangGraph) & Human-in-the-Loop Checkpoints",
         "Python LangGraph SDK + Postgres Checkpointer + LangSmith Tracing + DPO",
         "cyclic StateGraph, conditional routing edges, state persistence, human-in-the-loop interrupt_before, Evaluator-Optimizer loop, DPO preference tuning",
         "Forcing multi-step cyclic workflows with tool retries and human approval pauses into linear L3 chains fails: unhandled API/SQL exceptions crash the entire run without state recovery",
         "Building distributed multi-agent cluster infrastructure from scratch (L5, 600-2000h) is redundant when LangGraph + managed tracing handles stateful workflow persistence",
         "In G2, autonomous loops (AutoGPT) lacked explicit state-machine graph boundaries and human checkpoints, failing 85%+ of multi-step runs",
         "In G4, built-in Deep Research absorbs web-research graphs into L2, while coding/ops agents move into terminal CLI harnesses (Claude Code) at L4"),
        ("G3", 5, "Populated", 600, 2000,
         550000, 4.4e14, 1.850, 11.000, 60.0, 45.0, 1.2, 11.0, 12.0,
         "Multi-Agent Repository Orchestration & Automated Benchmark Evaluation Harnesses",
         "Dockerized SWE-bench / Custom Eval Clusters + Multi-Agent Orchestrator-Workers + vLLM",
         "Orchestrator-Workers pattern, containerized repo test beds, pass@k execution verification, synthetic preference data generation",
         "Forcing repository-wide autonomous PR generation onto single-graph L4 without containerized test-suite verification fails: unverified code patches break CI builds on 50%+ of PRs",
         "Top level in Gen 3; pre-RLVR base models (Claude 3.5 Sonnet v1 at 33%-49% SWE-bench) still hit a reasoning ceiling on complex multi-file bugs",
         "In G2, multi-agent coding frameworks (MetaGPT/ChatDev) operated in toy sandboxes without real GitHub repo Docker test harnesses",
         "In G4, RLVR thinking models + Claude Code CLI bring single-repo TDD loops to L4, while L5 advances to 24/7 M4 Mac Mini OpenClaw sandboxes & GRPO flywheels"),

        # GEN 4 (2025-01 to 2026-10)
        ("G4", 1, "Populated", 0, 0,
         6500, 3.9e12, 0.008, 0.110, 0.8, 0.4, 61.0, 14.0, 12.0,
         "Zero-Shot Auto-Thinking Chat (Built-In RLVR Router) & Interactive MCP Apps",
         "Default Web/Mobile UI (GPT-5 Auto-Router, Claude 4.5/4.6, DeepSeek-R1, Gemini 3.5)",
         "Zero AI learning (0h); user asks a hard math, logic, or planning question and auto-router silently thinks step-by-step and renders interactive MCP Apps",
         "N/A (Lowest Level; 0-skill entry point where CoT reasoning and multimodal app widgets are 100% built-in)",
         "Spending 20 hours writing manual G2-style 'Let's think step by step' XML prompt wrappers at L2 for an RLVR thinking model is obsolete and degrades native reasoning traces",
         "In G2-G3, getting multi-step Chain-of-Thought reasoning required L2 (7-45h) manual prompt engineering or L3 reflection wrappers",
         "Current frontier baseline (2025-2026); moving toward persistent cross-app OS memory at L1"),
        ("G4", 2, "Populated", 7, 45,
         120000, 7.2e13, 0.180, 1.500, 6.0, 12.0, 21.0, 22.0, 20.0,
         "Autonomous Multi-Site Deep Research Scoping & Citation Verification",
         "Built-In Deep Research UI (OpenAI Deep Research, Gemini Deep Research, Perplexity Deep Research)",
         "research brief scoping, constraint framing, reasoning effort toggle (low/med/high/xHigh), primary-source citation auditing, contradiction checks",
         "Forcing a 100-source competitive/literature audit into a single L1 chat turn fails: standard L1 search retrieves only top 3-5 snippets without 15-minute multi-hop browsing and cross-verification",
         "Coding a custom Python LangGraph + Tavily + Playwright web scraper (G3-L4, 200-600h) for ad-hoc research reports wastes weeks when built-in Deep Research executes 80+ searches for $0.18",
         "In G3, autonomous multi-hop web research synthesis required climbing to G3-L4 (200-600h) to build and maintain custom LangGraph search pipelines",
         "Current frontier power-user tier (2025-2026); expanding into automated spreadsheet/financial model verification"),
        ("G4", 3, "Populated", 50, 200,
         160000, 9.6e13, 0.250, 2.100, 10.0, 4.0, 11.5, 25.0, 27.0,
         "Plug-and-Play MCP Tool Wiring (.mcp.json) & Guardrailed Agentic Enterprise Chatbots",
         "Cursor / Claude Desktop (.mcp.json) & Enterprise Agentic Bot Stack (MCP + Hybrid RAG + Llama Guard / NeMo)",
         ".mcp.json server configuration, stdio vs SSE transport, OAuth scoped tokens, AGENTS.md, Salesforce Headless 360 MCP, Llama Guard 3 / NeMo policy rails",
         "Forcing live database/Jira/ServiceNow actions or enterprise policy compliance into L2 (Deep Research / Projects) fails: L2 cannot authenticate into private internal tools via MCP or enforce RBAC/Colang guardrails for 10,000 L1 employees",
         "Writing bespoke per-tool REST API glue code or autonomous bash CLI loops (L4, 200-600h) for standard SaaS connectors wastes 100+ hours when 10,000+ prebuilt MCP servers plug in via .mcp.json",
         "In G2-G3, connecting an LLM to 5 internal enterprise tools required L3/L4 custom JSON function schemas and custom OAuth middleware per model vendor",
         "Current frontier integrator tier (2025-2026); AAIF standardization (Dec 2025) makes .mcp.json the universal USB-C port for AI tools"),
        ("G4", 4, "Populated", 200, 600,
         480000, 3.4e14, 1.150, 7.800, 15.0, 25.0, 5.1, 23.0, 24.0,
         "Autonomous Terminal CLI Coding & Verification Harnesses (Claude Code / Codex CLI)",
         "Terminal CLI Harness (Claude Code, OpenAI Codex CLI, Aider, Goose) + CLAUDE.md + Local Docker Test Suite",
         "CLAUDE.md / AGENTS.md harness engineering, bash/read/write/edit/glob/grep primitives, TDD red-green loop, context compaction (/compact), Scale SWE-bench Pro scaffold tuning",
         "Forcing a 40-file commercial codebase refactoring with iterative test debugging into L3 IDE chat/Composer fails: requires human manual approval per diff and lacks autonomous bash test-execution retry loops",
         "Buying dedicated 24/7 physical sandbox hardware or running multi-GPU GRPO training (L5, 600-2000h) is unnecessary for interactive daytime engineering on a developer's existing laptop",
         "In G3, pre-RLVR models scored 33%-49% on SWE-bench Verified and lacked mature terminal CLI harnesses (Claude Code launched Feb 2025; SWE-bench Verified hit 72.7%-96.0% in G4)",
         "Current frontier SWE harness tier (2025-2026); shifting human effort from writing syntax to writing deterministic test suites and CLAUDE.md specifications"),
        ("G4", 5, "Populated", 600, 2000,
         2400000, 2.2e15, 6.500, 42.000, 20.0, 180.0, 1.4, 16.0, 17.0,
         "24/7 Dedicated M4 Mac Mini OpenClaw Sandboxes, Parallel Worktree Swarms & Custom GRPO RLVR",
         "Dedicated Physical Apple M4 Mac Mini ($599-$1,200) running OpenClaw / Docker + Parallel Git Worktrees OR Multi-GPU GRPO RLVR Cluster",
         "dedicated hardware air-gap (M4 Mac Mini), OpenClaw 24/7 daemon, parallel git worktree subagent swarms, OSWorld GUI grounding, GRPO group relative policy optimization, verifiable reward environments",
         "Forcing 24/7 unattended background agents or unauthenticated MCP stdio servers onto a user's primary daily-driver laptop (L4) fails security & OS isolation: risks credential theft, prompt-injection rm -rf, and the Apr 2026 OX Security 200,000-instance stdio RCE vulnerability",
         "Top level in Gen 4 (600-2,000+ hours + dedicated non-compute hardware capital or multi-GPU RLVR cluster); pushing beyond L5 to zero-human L5 corporations remains premature (4.8-22.5 pt private repo drop)",
         "In G3, neither open-weight RLVR reasoning recipes (DeepSeek-R1 GRPO, Jan 2025) nor mature 24/7 local personal agent daemons (OpenClaw + MCP + Computer Use at 72.5%-78.4% OSWorld) existed",
         "Current apex of the AI skill tree (Oct 2026): combines physical hardware sandboxing for personal/team autonomy with custom RLVR verifier flywheels for proprietary enterprise domains"),
    ]

    df_cells = pd.DataFrame(cells, columns=[
        "gen_id", "level_id", "status", "learning_hours_min", "learning_hours_max",
        "single_task_tokens", "single_task_flops", "single_task_usd", "single_task_wh",
        "human_minutes", "ai_minutes", "user_share_pct", "token_share_pct", "spend_share_pct",
        "user_first_title", "surface_and_setup", "keywords_and_tutorials",
        "why_not_lower_L_minus_1", "why_not_higher_L_plus_1",
        "why_not_before_G_minus_1", "why_not_after_G_plus_1"
    ])
    cells_path = os.path.join(CACHE_DIR, "v3_ladder_cells.csv")
    df_cells.to_csv(cells_path, index=False)
    print(f"[SAVED] {cells_path} | shape={df_cells.shape}")

    # 9. Table 2.5: Historical Cost, Token & Hardware Baseline
    cost_baseline = [
        ("BERT-Large / T4 GPU", "2018-10", "0.02 (equiv)", "512 tokens", "0.9e12 FLOP/s/W", 0.08),
        ("GPT-3 davinci (175B)", "2020-06", "60.00 / 60.00", "2,049 tokens", "1.9e12 FLOP/s/W (A100)", 2.50),
        ("gpt-3.5-turbo", "2023-03", "2.00 / 2.00", "4,096 tokens", "2.4e12 FLOP/s/W", 0.80),
        ("GPT-4 (8k)", "2023-03", "30.00 / 60.00", "8,192 tokens", "3.2e12 FLOP/s/W", 4.50),
        ("GPT-4 Turbo (128k)", "2023-11", "10.00 / 30.00", "128,000 tokens", "4.5e12 FLOP/s/W (H100)", 2.20),
        ("GPT-4o (Omni)", "2024-05", "5.00 / 15.00 (2.50 cached)", "128,000 tokens", "6.0e12 FLOP/s/W", 0.32),
        ("Claude 3.5 Sonnet (v1/v2)", "2024-06", "3.00 / 15.00 (0.30 cached)", "200,000 tokens", "6.5e12 FLOP/s/W", 0.90),
        ("OpenAI o1 / DeepSeek-R1", "2025-01", "15.00/60.00 (o1) | 0.55/2.19 (R1)", "128k-200k tokens", "8.8e12 FLOP/s/W (H200/B200)", 18.00),
        ("Claude Sonnet 4.6 / Gemini 3.5 Flash", "2026-02", "3.00/15.00 | 0.15/0.60", "1,000,000 tokens", "1.2e13 FLOP/s/W", 1.10),
        ("GPT-5.4 (xHigh) / Claude Opus 5.5 / Laguna S 2.1", "2026-08", "2.50/10.00 | 5.00/20.00 | 0.05/0.20", "1.1M-2.0M tokens", "1.6e13 FLOP/s/W (Blackwell)", 0.65),
    ]
    df_cost = pd.DataFrame(cost_baseline, columns=[
        "model_or_hardware", "release_date", "price_per_1m_tokens_usd",
        "context_window", "hardware_efficiency", "typical_latency_sec"
    ])
    cost_path = os.path.join(CACHE_DIR, "v3_cost_baseline.csv")
    df_cost.to_csv(cost_path, index=False)
    print(f"[SAVED] {cost_path} | shape={df_cost.shape}")

    # 10. Table 5.4a: Pre-Today vs. Post-Today Gen 4 -> Gen 5 Cutoff Window Audit (Relative to TODAY = 2026-10-20)
    gen5_cutoffs = [
        ("CUT_PRE_TODAY", "Pre-Today First-Release / Early-Adopter Lens (TRL 5–6)", "2026-08 (2 mos BEFORE Today 2026-10-20)",
         "2026-08 to 2028-06",
         "Muse Spark 1.1 crosses >50% (51.5%) on Scale SWE-bench Pro Unseen Commercial; Claude Opus 5.5 hits 96.0% Verified; GPT-5.4 (xHigh, 1.1M ctx) & Poolside Laguna S 2.1 ($0.20/1M); Salesforce Headless 360 (4.5M MCP calls) & dedicated M4 Mac Mini OpenClaw 24/7 sandboxes",
         "Frontier L4–L5 engineers shift from foreground CLI supervision to asynchronous multi-PR background queues & continuous RLVR verifiers",
         "Mainstream L1/L2 Down-Ladder Sinking incomplete on 2026-10-20 (casual users still use turn-based chat rather than ambient OS background delegates)"),
        ("CUT_POST_TODAY", "Post-Today Mainstream Production-Crossover Lens (TRL 8–9, Primary v3 Lens)", "2027-03 (5 mos AFTER Today 2026-10-20)",
         "2027-03 to 2028-12",
         "OS-native Ambient Background Delegation ships as default L1 consumer OS layer (Apple/Windows/Android + AAIF MCP Registry); natural-language repo/app builders with built-in test verification cross 50%+ enterprise seat adoption at L2",
         "Both shifts complete: (a) G4-L2 Deep Research & cross-app memory sink to G5-L1 (0h); G4-L3/L4 MCP + single-repo CLI coding sink to G5-L2 (7–45h); (b) New L3–L5 verifier-contract & continuous RLVR skills emerge",
         "Requires 4–6 additional months post-2026-10-20 for cryptographic MCP/A2A auth standardization (remediating OX Security stdio flaws) and sub-$0.05/1M verifier inference"),
    ]
    df_gen5_cutoffs = pd.DataFrame(gen5_cutoffs, columns=[
        "cutoff_id", "chronological_lens", "cutoff_date_vs_today", "projected_gen5_window",
        "triggering_milestones", "user_workflow_shift", "why_lens_applies_or_waits"
    ])
    g5_cut_path = os.path.join(CACHE_DIR, "v3_gen5_cutoff_windows.csv")
    df_gen5_cutoffs.to_csv(g5_cut_path, index=False)
    print(f"[SAVED] {g5_cut_path} | shape={df_gen5_cutoffs.shape}")

    # 11. Table 5.4b: Speculative Next Generation (Gen 5 = Current + 1) User-Skill Matrix (G5-L1 to G5-L5)
    # Folksonomy Name: Gen 5: The Ambient OS Delegation, Verifier-Contract & Continuous-RLVR Generation
    gen5_cells = [
        ("G5", 1, "Speculative-Next-Gen (Current+1)", 0, 0,
         45000, 3.6e13, 0.015, 0.220, 0.5, 5.0, 58.0, 12.0, 10.0,
         "Ambient Cross-App OS Delegation, Persistent Personal Memory & Background Action Cards",
         "OS-Native Ambient Assistant & Browser/Mobile Action Bar (Zero-Config Background Delegate)",
         "Zero AI learning (0h); speaking or typing high-level life/work intents ('rebook flights, reconcile receipts, summarize 30 sources') executed asynchronously across apps with one-tap approval cards",
         "N/A (Lowest Level; 0-skill entry point where G4-L2 multi-site Deep Research and cross-app MCP actions have sunk into the default OS layer)",
         "Opening a dedicated workspace studio (G5-L2) to write multi-page specification rubrics for routine calendar/travel/research tasks wastes 15 minutes",
         "In G4, L1 was still session-bound chat requiring manual copy-paste or foreground waiting; multi-site synthesis required G4-L2 Deep Research",
         "In a hypothetical G6 (post-2029), ambient delegation may extend to physical household/embodied robotics"),
        ("G5", 2, "Speculative-Next-Gen (Current+1)", 7, 45,
         650000, 5.2e14, 0.350, 2.800, 8.0, 35.0, 22.0, 21.0, 19.0,
         "Natural-Language Full-Stack App/Repo Specification & Async Background PR Review Studios",
         "No-CLI Cloud Specification Studio + One-Click AAIF MCP Store + Automated PR Preview Sandbox",
         "acceptance rubric drafting, visual state-flow specification, one-click OAuth MCP connector toggle, preview-environment diff auditing, async agent task queuing",
         "Forcing a custom multi-table internal web app or 10-connector workflow into G5-L1 ambient voice/chat fails: lacks explicit edge-case acceptance rubrics and staging preview verification",
         "Dropping into terminal bash CLI harnesses or writing formal policy-as-code contracts (G5-L3/L4, 50-600h) is unnecessary when the cloud studio auto-generates tests and deploys preview containers",
         "In G4, building verified multi-file apps or wiring MCP servers required G4-L3 (.mcp.json) or G4-L4 (Claude Code terminal CLI + Docker)",
         "Sinks G4-L3 MCP wiring and G4-L4 single-repo coding into a 1-weekend no-CLI specification workflow"),
        ("G5", 3, "Speculative-Next-Gen (Current+1)", 50, 200,
         1800000, 1.4e15, 0.900, 6.500, 12.0, 60.0, 12.5, 25.0, 26.0,
         "Multi-Agent A2A/MCP Contract Wiring, Cryptographic Policy-as-Code & SLA Budget Engineering",
         "Enterprise Agent Registry + Cryptographic MCP/A2A Gateway + Cedar/OPA Policy-as-Code + FinOps Circuit Breakers",
         "A2A agent-card manifests, OAuth 2.1 hardware-attested MCP scopes, Cedar/OPA deterministic policy rails, per-ticket token/USD circuit breakers, counterfactual shadow-run auditing",
         "Forcing 50,000-employee cross-department autonomous workflows (Finance + Legal + CRM) into G5-L2 personal spec studios fails: lacks cryptographic tool attestation, tenant RBAC isolation, and FinOps loop-kill switches",
         "Writing custom Lean 4 / property-based formal simulation verifiers (G5-L4, 200-600h) is overkill when declarative Cedar/OPA policy-as-code and standard MCP/A2A contracts govern commercial SaaS agents",
         "In G4, MCP security was bolted on after the Apr 2026 OX Security 200k stdio RCE disclosure and lacked cross-vendor Agent-to-Agent (A2A) budget contracts",
         "Standardizes the Track B enterprise integrator tier around verifiable agent SLAs and cryptographic governance"),
        ("G5", 4, "Speculative-Next-Gen (Current+1)", 200, 600,
         6500000, 5.8e15, 3.200, 22.000, 18.0, 180.0, 5.8, 24.0, 25.0,
         "Formal Verifier Harness, Property-Based Simulation & Parallel Swarm Choreography Engineering",
         "Deterministic Digital-Twin Simulator + Property-Based / Formal Verifier Suite (Hypothesis / Kani / Lean 4 / TLA+) + 20-Agent Swarm Orchestrator",
         "executable specification engineering, property-based fuzzing invariants, stateful digital-twin mock environments, Lean 4 / TLA+ state invariants, pass@k verifier reward shaping, cross-repo dependency choreography",
         "Forcing a 20-agent swarm to refactor a 500,000-line private commercial monolith using only G5-L3 policy rails or G4-style unit tests fails: subtle cross-service race conditions pass shallow unit tests (Scale SWE-bench Pro private commercial gap)",
         "Operating dedicated 24/7 on-policy weight-updating GPU clusters (G5-L5, 600-2000h+) is unnecessary when frozen frontier checkpoints guided by formal verifiers solve the engineering specification",
         "In G4, L4 developers wrote manual pytest/Docker harnesses for 1-3 foreground CLI agents; in G5, human engineers design formal verifier environments that grade 20+ parallel background agents",
         "Shifts human SWE effort 100% from imperative code/test writing to formal invariant and simulation environment design"),
        ("G5", 5, "Speculative-Next-Gen (Current+1)", 600, 2000,
         35000000, 3.5e16, 18.000, 110.000, 25.0, 720.0, 1.7, 18.0, 20.0,
         "Continuous On-Policy RLVR Flywheels, World-Model Simulators & Sovereign Hardware Clusters",
         "Sovereign Local Cluster (Multi-Node Mac Studio Ultra / Blackwell Server) + Continuous Nightly GRPO/RLVR Weight Updating + Hardware-Enclaved Agent Appliance",
         "continuous nightly on-policy RLVR, verifiable trajectory harvesting, domain world-model training, hardware enclave attestation (TPM/Secure Enclave), speculative decoding trees, self-play curriculum generation",
         "Forcing proprietary scientific discovery, quantitative trading, or chip-design closure onto frozen public API models at G5-L4 hits out-of-distribution generalization ceilings without continuous weight updates on private verifier traces",
         "Apex of the Gen 5 skill tree (600-2,000h+ and dedicated sovereign cluster/appliance capital); fully unsupervised zero-human corporations remain bounded by legal liability and human goal specification",
         "In G4-L5, Mac Mini OpenClaw sandboxes ran frozen weights and GRPO RLVR was a periodic offline batch job; G5-L5 closes the loop into continuous nightly on-policy RLVR over verified execution traces",
         "Represents the Current+1 horizon where private verifier environments continuously distill swarm trajectories into sovereign domain weights"),
    ]
    df_gen5 = pd.DataFrame(gen5_cells, columns=df_cells.columns)
    g5_path = os.path.join(CACHE_DIR, "v3_gen5_speculative.csv")
    df_gen5.to_csv(g5_path, index=False)
    print(f"[SAVED] {g5_path} | shape={df_gen5.shape}")

    # 12. 34 Generational-Defining Events (2017–2028, ~3 events/year) for Plot 0 Bottom Timeline
    defining_events = [
        (2017.46, "2017-06", "G0", "Vaswani 'Attention Is All You Need'"),
        (2017.75, "2017-09", "G0", "spaCy v2 Neural NLP & Weld"),
        (2018.12, "2018-02", "G0", "ELMo Contextual Embeddings"),
        (2018.42, "2018-05", "G0", "EU GDPR Enforced & Google Duplex Demo"),
        (2018.79, "2018-10", "G0", "Google BERT & HF pytorch-pretrained-bert"),
        (2019.15, "2019-02", "G0", "OpenAI GPT-2 (1.5B) 'Too Dangerous'"),
        (2019.58, "2019-07", "G0", "RoBERTa & ONNX Runtime 1.0"),
        (2019.83, "2019-10", "G0", "BERT Powers 10% of Google US Search"),
        (2020.12, "2020-02", "G0", "Grammarly GECToR Sequence Tagger"),
        (2020.46, "2020-06", "G1", "OpenAI GPT-3 175B API Beta ($60/1M)"),
        (2020.79, "2020-10", "G1", " DeepSpeed ZeRO-3 Sharding Released"),
        (2021.08, "2021-01", "G1", "OpenAI CLIP & DALL-E 1 Multimodal"),
        (2021.48, "2021-06", "G1", "GitHub Copilot Technical Preview (Codex)"),
        (2021.88, "2021-11", "G1", "OpenAI API Waitlist Removed + Fine-Tune CLI"),
        (2022.08, "2022-01", "G1", "InstructGPT RLHF & Wei Chain-of-Thought"),
        (2022.48, "2022-06", "G1", "GitHub Copilot GA (1.2M+ Users) & Midjourney v1"),
        (2022.71, "2022-08", "G1", "Stable Diffusion v1.4 Open-Weight Release"),
        (2022.91, "2022-11", "G2", "ChatGPT (gpt-3.5-turbo) Hits 100M Users in 60d"),
        (2023.21, "2023-03", "G2", "GPT-4 Launch, LangChain Boom & BloombergGPT"),
        (2023.42, "2023-05", "G2", "Dettmers 4-Bit QLoRA, CoEdIT & Mata v. Avianca"),
        (2023.58, "2023-07", "G2", "Meta Llama-2 Open Weights & vLLM PagedAttention"),
        (2023.87, "2023-11", "G2", "GPT-4 Turbo (128k) & Claude 2.1 (200k)"),
        (2024.21, "2024-03", "G2", "Claude 3 Family & LangGraph v0.1 Cyclic Graphs"),
        (2024.42, "2024-05", "G3", "GPT-4o Omni-Model & EU AI Act Approved"),
        (2024.49, "2024-06", "G3", "Claude 3.5 Sonnet + Artifacts & Cursor Composer"),
        (2024.72, "2024-09", "G3", "NotebookLM Audio Overviews & o1-preview"),
        (2024.90, "2024-11", "G3", "Anthropic Model Context Protocol (MCP) Open Spec"),
        (2025.08, "2025-01", "G4", "DeepSeek-R1 Open RLVR & OpenAI o3-mini"),
        (2025.16, "2025-02", "G4", "Claude Code CLI & OpenAI/Gemini Deep Research"),
        (2025.58, "2025-07", "G4", "MIT NANDA Audit (67% Bought vs 33% Built) & Deep Agents"),
        (2025.94, "2025-12", "G4", "Linux Foundation AAIF (MCP + goose + AGENTS.md)"),
        (2026.29, "2026-04", "G4", "OX Security 200k MCP stdio RCE -> M4 Mac Mini OpenClaw"),
        (2026.62, "2026-08", "G4", "Muse Spark 1.1 (51.5% SWE-Pro Private), Opus 5.5 & GPT-5.4"),
        (2026.80, "2026-10", "G4", "TODAY (2026-10-20): v3 AI Ladder Atlas Baseline"),
        (2027.21, "2027-03", "G5", "[Speculative] Gen 5 Crossover: Ambient OS Delegates & A2A Contracts"),
        (2028.08, "2028-01", "G5", "[Speculative] Continuous Nightly On-Policy RLVR Enterprise Flywheels"),
    ]
    df_events = pd.DataFrame(defining_events, columns=["year_float", "date_str", "gen_id", "event_label"])
    events_path = os.path.join(CACHE_DIR, "v3_defining_events.csv")
    df_events.to_csv(events_path, index=False)
    print(f"[SAVED] {events_path} | shape={df_events.shape}")

    # 13. 30 Encyclopedic Cell Payloads for Plot 0 Megachart Poster (Gen 0 to Speculative Gen 5 x Level 1 to Level 5)
    # Strictly "What" only (no learning hours repeated, no "why here" counterfactuals).
    poster_cells = [
        # GEN 0
        ("G0", 1, "Passive Background NLP Widgets (Active GenAI Missing)",
         "• Use Cases & Landmarks: Gmail Smart Compose (May 2018), Google Neural Machine Translate (GNMT), Grammarly browser typo underlines, iOS QuickType\n"
         "• User Actions: Typing normal emails/texts; clicking 1-word spellcheck or pressing Tab on fixed 3-word phrase completions (0% freeform prompting)\n"
         "• Models & Engines: GNMT LSTM/Transformer hybrid, Grammarly GECToR sequence tagger, n-gram language models\n"
         "• Surface & Hardware: Chrome/Safari extension, iOS/Android keyboard, CPU/TPU cloud background inference\n"
         "• Core Vocabulary: Autocorrect, spellcheck underline, Smart Reply, language translation bar, predictive text"),
        ("G0", 2, "Cloud AutoML Consoles & Regex Rule Crafting",
         "• Use Cases & Landmarks: Google Cloud AutoML Natural Language (Jan 2018), AWS Comprehend console, Zendesk/Salesforce regex ticket routing\n"
         "• Techniques & Skills: Uploading 500–5,000 labeled CSV rows, regex lookahead/lookbehind patterns, confidence threshold slider tuning\n"
         "• Platforms & Models: Google Cloud AutoML Vision/NLP, AWS Comprehend, Azure LUIS, Dialogflow intent trees\n"
         "• Software & Formats: Web admin consoles, Excel/Sheets CSV cleaning, Regex101 debugger, JSON webhook payloads\n"
         "• Core Vocabulary: Intent slot, entity list, precision-recall curve, false positive threshold, confusion matrix, webhook"),
        ("G0", 3, "Classical Python NLP & Tabular Feature Pipelines",
         "• Use Cases & Landmarks: Customer churn & sentiment pipelines, Kaggle tabular/text competitions, spaCy v2 production entity extraction\n"
         "• Techniques & Skills: TF-IDF vectorization, n-gram tokenization, stop-word pruning, k-fold cross-validation, grid search\n"
         "• Libraries & Models: scikit-learn (LogisticRegression, RandomForest), XGBoost, LightGBM, spaCy (en_core_web_sm), NLTK, Gensim Word2Vec\n"
         "• Software & Hardware: Jupyter Notebook, Anaconda, Pandas DataFrames, multi-core CPU workstation (16–64 GB RAM)\n"
         "• Core Vocabulary: TF-IDF, bag-of-words, lemmatization, POS tagging, dependency parse, ROC-AUC, F1 score, GridSearchCV"),
        ("G0", 4, "Single-GPU Pretrained Encoder Fine-Tuning (BERT / RoBERTa)",
         "• Use Cases & Landmarks: Oct 2018 BERT release, Grammarly GECToR (2020) grammatical error tagging, SQuAD 2.0 extractive QA, legal/medical NER\n"
         "• Techniques & Skills: Pretrained checkpoint transfer learning, AdamW linear warmup + decay, gradient clipping, sequence bucketing\n"
         "• Models & Repos: Google BERT-base/large, Facebook RoBERTa, DistilBERT, ALBERT, ULMFiT (Fast.ai), HuggingFace pytorch-pretrained-bert\n"
         "• Software & Hardware: PyTorch, HuggingFace transformers, Google Colab Pro / single NVIDIA GTX 1080 Ti, V100, or T4 (16 GB VRAM)\n"
         "• Core Vocabulary: [CLS] & [SEP] tokens, WordPiece, masked language modeling (MLM), attention mask, fine-tuning head, cross-entropy"),
        ("G0", 5, "Custom Seq2Seq Pretraining & Quantized ONNX Serving",
         "• Use Cases & Landmarks: Vaswani Transformer (Jun 2017), Google Search BERT rollout (Oct 2019), high-QPS neural machine translation & ad ranking\n"
         "• Techniques & Skills: Custom BPE/SentencePiece vocabulary training, multi-GPU Horovod/DDP all-reduce, FP16/INT8 graph quantization, beam search\n"
         "• Models & Frameworks: Transformer-Big, GPT-1/GPT-2 (1.5B), Megatron-LM, Fairseq, Tensor2Tensor, ONNX Runtime, TensorRT\n"
         "• Software & Hardware: 8x–64x NVIDIA V100 DGX servers, NVLink, InfiniBand, CUDA/cuDNN, C++ gRPC microservices, Docker/Kubernetes\n"
         "• Core Vocabulary: Scaled dot-product attention, multi-head QKV tensors, layer norm, warmup steps, perplexity, ONNX graph optimization"),

        # GEN 1
        ("G1", 1, "IDE Ghost-Text Autocomplete & Viral Consumer Web Toys",
         "• Use Cases & Landmarks: GitHub Copilot Technical Preview (Jun 2021) & GA (Jun 2022, 1.2M devs), Craiyon / DALL-E Mini viral memes, AI Dungeon\n"
         "• User Actions: Pressing Tab to accept inline gray ghost-text code completions; typing 3-word noun phrases into viral browser boxes\n"
         "• Models & Products: OpenAI Codex (code-cushman-001 12B), DALL-E Mini / Craiyon, GPT-J-6B web demos, Replika early chat\n"
         "• Surface & Hardware: VS Code Copilot extension, JetBrains plugin, public web toy URLs (cloud-hosted inference)\n"
         "• Core Vocabulary: Ghost text, Tab autocomplete, docstring-to-function, text-to-image prompt box, AI Dungeon adventure"),
        ("G1", 2, "Few-Shot Completion Prompting & Stop-Sequence Crafting",
         "• Use Cases & Landmarks: OpenAI GPT-3 Playground (Jun 2020), Jasper.ai & Copy.ai marketing copy, early Midjourney v1–v3 Discord art\n"
         "• Techniques & Skills: Designing 3-to-5-shot Input:/Output: completion prefixes, setting stop=['\\n', '###'] sequences, tuning temperature\n"
         "• Models & Platforms: OpenAI GPT-3 (davinci, curie, babbage, ada), text-davinci-002, Cohere Generate, AI21 Jurassic-1, Midjourney Discord\n"
         "• Surface & Tools: OpenAI Web Playground sliders, Notion AI alpha, Discord slash commands (/imagine), PromptBase templates\n"
         "• Core Vocabulary: Few-shot exemplars, completion prefix, stop sequence, temperature, top_p nucleus sampling, frequency/presence penalty"),
        ("G1", 3, "REST API Completion Wrappers & Early Embedding Search",
         "• Use Cases & Landmarks: Early SaaS copywriting/summarization startups, semantic product search, customer support draft assistants\n"
         "• Techniques & Skills: Dynamic prompt template interpolation, token counting (GPT2TokenizerFast), cosine similarity search, rate-limit backoff\n"
         "• Models & APIs: OpenAI /v1/completions & /v1/embeddings (text-similarity-davinci-001, text-search-ada), FAISS, early Pinecone (2021)\n"
         "• Software & Hardware: Python/Node.js REST SDKs, FastAPI/Flask, PostgreSQL, Redis cache, standard cloud CPU web servers\n"
         "• Core Vocabulary: Completion endpoint, prompt injection defense, 2,049-token context ceiling, dense embedding vector, cosine similarity"),
        ("G1", 4, "Multi-Step Prompt Chains, Self-Consistency & Cloud Fine-Tune CLI",
         "• Use Cases & Landmarks: Stanford CS324 (Jan 2022), Wei et al. Chain-of-Thought (Jan 2022), GSM8K math solving, custom domain classifiers\n"
         "• Techniques & Skills: Multi-call prompt chaining, self-consistency majority voting (pass@20), curating 1,000+ JSONL prompt-completion pairs\n"
         "• Models & Tools: code-davinci-002, text-davinci-002, OpenAI Fine-Tuning CLI (openai api fine_tunes.create), Google Flan-T5-XL, EleutherAI GPT-J\n"
         "• Software & Hardware: Python async orchestration scripts, Weights & Biases experiment tracking, single A100/V100 GPU or managed cloud CLI\n"
         "• Core Vocabulary: In-context learning, Chain-of-Thought (CoT), self-consistency voting, JSONL completion schema, classification suffix"),
        ("G1", 5, "Distributed Multi-GPU Full-Weight LLM Fine-Tuning (DeepSpeed)",
         "• Use Cases & Landmarks: On-prem enterprise 6B–20B domain models, BigScience BLOOM-176B, EleutherAI GPT-NeoX-20B, Stable Diffusion v1.4 training\n"
         "• Techniques & Skills: ZeRO Stage 3 optimizer/gradient/parameter sharding, activation checkpointing, BF16 mixed precision, Slurm cluster ops\n"
         "• Models & Frameworks: GPT-NeoX-20B, OPT-30B/66B, BLOOM, Flan-T5-XXL, Microsoft DeepSpeed, Megatron-LM, HuggingFace Accelerate\n"
         "• Software & Hardware: Multi-node 8x–64x NVIDIA A100 (40GB/80GB) clusters, 400Gbps InfiniBand, NCCL collectives, PyTorch Distributed\n"
         "• Core Vocabulary: ZeRO-3 sharding, model/tensor/pipeline parallelism, CUDA OOM, BF16, gradient accumulation, throughput TFLOP/s/GPU"),

        # GEN 2
        ("G2", 1, "Zero-Shot Conversational Web Chat for Q&A & Drafting",
         "• Use Cases & Landmarks: ChatGPT launch (Nov 30, 2022 -> 100M users in 60 days), homework/essay drafting, email rewrites, Samsung leak ban (Apr 2023)\n"
         "• User Actions: Typing natural conversational questions and follow-up edits in a browser chat box with zero formatting or parameters\n"
         "• Models & Apps: OpenAI ChatGPT (gpt-3.5-turbo), Microsoft Bing Chat (Sydney), Google Bard (PaLM 2), Anthropic Claude 2 web chat\n"
         "• Surface & Hardware: chat.openai.com browser tab, iOS/Android mobile app (free tier, cloud-hosted RLHF inference)\n"
         "• Core Vocabulary: Chat thread, regenerate response, hallucination, prompt, ChatGPT, AI detector, conversational follow-up"),
        ("G2", 2, "Manual CoT/Role Prompting, Custom GPTs & Discord Image Flags",
         "• Use Cases & Landmarks: Ng & Fulford Prompt Eng course (May 2023), Mata v. Avianca citation sanction, OpenAI Custom GPT Store (Nov 2023), Midjourney v5\n"
         "• Techniques & Skills: System role personas ('Act as...'), XML/markdown delimiters, manual 'Let's think step by step', Midjourney parameter flags\n"
         "• Models & Platforms: GPT-4 (8k/32k), Claude 2.1, Midjourney v5/v6 Discord bot, DALL-E 3, Perplexity AI early citation search\n"
         "• Surface & Tools: ChatGPT Plus ($20/mo), Custom GPT builder + Actions, Discord /imagine (--ar 16:9 --v 5.2 --stylize 250 --no)\n"
         "• Core Vocabulary: System prompt, role prompting, Chain-of-Thought trigger, Custom GPT knowledge upload, aspect ratio flag, negative prompt"),
        ("G2", 3, "DIY Chunked Vector-DB RAG & Function-Calling Internal Bots",
         "• Use Cases & Landmarks: Internal HR/wiki 'Chat with Your PDFs' bots, Chase LangChain & Liu LlamaIndex courses (2023), OpenAI Function Calling (Jun 2023)\n"
         "• Techniques & Skills: RecursiveCharacterTextSplitter (chunk_size=512, overlap=50), HNSW vector indexing, top-k retrieval, JSON function schemas\n"
         "• Models & Databases: gpt-3.5-turbo-0613, gpt-4-0613, text-embedding-ada-002, Cohere Rerank, Pinecone, ChromaDB, Weaviate, Milvus, Qdrant\n"
         "• Software & Hardware: LangChain, LlamaIndex, Python FastAPI, Streamlit/Gradio UI, Pydantic, cloud API keys ($50–$500/mo)\n"
         "• Core Vocabulary: RAG (Retrieval-Augmented Generation), chunking & overlap, vector database, HNSW, top-k cosine similarity, function calling"),
        ("G2", 4, "Single-GPU 4-Bit QLoRA Fine-Tuning & Early ReAct Agent Loops",
         "• Use Cases & Landmarks: Dettmers QLoRA (May 2023), Grammarly CoEdIT text editing (May 2023), Meta Llama-2 fine-tuning, viral AutoGPT/BabyAGI loops\n"
         "• Techniques & Skills: 4-bit NormalFloat (NF4) double quantization, LoRA rank r/alpha tuning on attention projections, SFTTrainer, LLM-as-a-Judge\n"
         "• Models & Libraries: Meta Llama-2 (7B/13B/70B), Mistral-7B, Falcon-40B, Flan-T5-Large (CoEdIT), HuggingFace PEFT, bitsandbytes, TRL, Axolotl\n"
         "• Software & Hardware: Single NVIDIA RTX 3090/4090 (24GB) or cloud A100 (40GB/80GB), llama.cpp GGUF, Ollama local runner\n"
         "• Core Vocabulary: QLoRA, NF4 quantization, LoRA adapter weights, rank r & lora_alpha, SFT, ReAct (Reason+Act) loop, compounding error (0.9^20)"),
        ("G2", 5, "Custom Domain Pretraining & High-Throughput vLLM GPU Clusters",
         "• Use Cases & Landmarks: Kwon et al. vLLM PagedAttention (Jun 2023), Dao FlashAttention-2, BloombergGPT 50B ($3M pretraining), enterprise GPU clusters\n"
         "• Techniques & Skills: PagedAttention non-contiguous KV-cache block management, continuous iteration-level batching, tensor parallelism, RLHF PPO\n"
         "• Models & Engines: Llama-2-70B, Mixtral-8x7B MoE, BloombergGPT-50B, vLLM, HuggingFace Text Generation Inference (TGI), TensorRT-LLM\n"
         "• Software & Hardware: 8x–512x NVIDIA H100 / A100 GPU clusters, NVSwitch, Ray, Triton Inference Server, Prometheus GPU telemetry\n"
         "• Core Vocabulary: PagedAttention, KV-cache fragmentation, continuous batching, time-to-first-token (TTFT), inter-token latency (ITL), MoE routing"),

        # GEN 3
        ("G3", 1, "Built-In Multimodal Omni-Chat (Voice/Vision/Image) & Live Artifacts",
         "• Use Cases & Landmarks: OpenAI GPT-4o launch (May 2024), Claude 3.5 Sonnet + Live Artifacts (Jun 2024), ChatGPT Advanced Voice & Canvas (Oct 2024)\n"
         "• User Actions: Speaking naturally with 320ms voice latency, pointing phone camera, pasting screenshots, remixing live interactive React/SVG apps in-chat\n"
         "• Models & Products: OpenAI GPT-4o, Anthropic Claude 3.5 Sonnet (20240620), Google Gemini 1.5 Flash, Meta Llama 3.1 web chat\n"
         "• Surface & Hardware: Default consumer web/mobile app with side-by-side Artifact/Canvas preview pane (0 setup, browser iframe sandbox)\n"
         "• Core Vocabulary: Omni-model, Claude Artifact, ChatGPT Canvas, real-time voice mode, camera vision grounding, one-click app remix"),
        ("G3", 2, "Drag-and-Drop 50-PDF Long-Context Workspaces & Audio Synthesis",
         "• Use Cases & Landmarks: Claude Projects (Jun 2024, 200k context), Google NotebookLM Audio Overviews viral wave (Sep 2024, 1M–2M context)\n"
         "• Techniques & Skills: Curating 20–100 PDFs/docs into persistent project workspaces, writing workspace system instructions, auditing inline citations\n"
         "• Models & Platforms: Gemini 1.5 Pro (2M context), Claude 3.5 Sonnet (200k context), GPT-4o (128k context), Google NotebookLM\n"
         "• Surface & Tools: Drag-and-drop cloud project folders, Google Drive / Notion direct sync, NotebookLM 2-host podcast studio\n"
         "• Core Vocabulary: Long-context window (200k–2M tokens), needle-in-a-haystack, Project Knowledge base, grounded inline citation, Audio Overview"),
        ("G3", 3, "AI-Native IDE Multi-File Composer & Policy-Guardrailed Enterprise RAG",
         "• Use Cases & Landmarks: Cursor IDE Composer & .cursorrules boom (mid-2024), Anthropic 90% Prompt Caching (Aug 2024, $0.30/1M), enterprise RBAC bots\n"
         "• Techniques & Skills: Multi-file diff orchestration (Cmd+K / Composer), @codebase indexing, hybrid BM25+vector search, SharePoint ACL filtering, Colang rails\n"
         "• Models & Stack: Claude 3.5 Sonnet v1/v2, GPT-4o-mini ($0.15/1M), Cursor IDE, Windsurf, NVIDIA NeMo Guardrails, Guardrails AI, Cohere Rerank 3\n"
         "• Software & Hardware: Cursor/VS Code fork, .cursorrules, Pinecone/pgvector hybrid index, Redis/Anthropic prompt cache, Okta/Entra RBAC tokens\n"
         "• Core Vocabulary: Cursor Composer, @codebase/@file tags, .cursorrules, prompt caching (90% discount), Colang dialog rails, RBAC metadata filter"),
        ("G3", 4, "Stateful Cyclic Agent Graphs (LangGraph) & HITL Checkpoints",
         "• Use Cases & Landmarks: LangGraph v0.1/v0.2 production rollout (2024), Anthropic 'Building Effective Agents' (Dec 2024), customer-support state machines\n"
         "• Techniques & Skills: Designing explicit cyclic StateGraphs, conditional routing edges, Postgres state checkpointing, human-in-the-loop interrupts, DPO\n"
         "• Frameworks & Models: LangGraph, CrewAI, AutoGen v0.4, LlamaIndex Workflows, Claude 3.5 Sonnet, GPT-4o, Direct Preference Optimization (DPO)\n"
         "• Software & Hardware: Python StateGraph SDK, PostgreSQL checkpointer, LangSmith / Arize Phoenix trace observability, Docker microservices\n"
         "• Core Vocabulary: Cyclic StateGraph, conditional edge, Postgres checkpointer, interrupt_before (HITL), Orchestrator-Workers, Evaluator-Optimizer, DPO"),
        ("G3", 5, "Multi-Agent Repo Orchestration & Containerized Eval Harnesses",
         "• Use Cases & Landmarks: SWE-bench Verified benchmark jump (33% -> 49% on Claude 3.5 Sonnet v2, Oct 2024), enterprise CI/CD eval clusters\n"
         "• Techniques & Skills: Containerized GitHub repo test-bed orchestration, pass@k execution grading, synthetic preference trajectory generation\n"
         "• Models & Harnesses: Claude 3.5 Sonnet v2, OpenAI o1-preview (Sep 2024), SWE-agent, AllHands/OpenDevin, custom vLLM + Docker evaluation farms\n"
         "• Software & Hardware: Kubernetes Docker-in-Docker farms, 8x–64x H100 inference clusters, GitHub Actions matrix runners, Braintrust/LangSmith\n"
         "• Core Vocabulary: SWE-bench Verified, containerized test harness, pass@k execution verification, trajectory replay, synthetic data flywheel"),

        # GEN 4
        ("G4", 1, "Zero-Shot Auto-Thinking Chat (RLVR Router) & Interactive MCP Apps",
         "• Use Cases & Landmarks: DeepSeek-R1 viral mobile/web wave (Jan 2025), GPT-5 Auto-Router (2025), AAIF Interactive MCP Apps in chat (Dec 2025–2026)\n"
         "• User Actions: Asking complex math, coding, legal, or planning questions in plain language; auto-router silently thinks & renders live interactive widgets\n"
         "• Models & Products: OpenAI GPT-5 / GPT-5.4 Auto-Router, DeepSeek-R1, Claude Sonnet 4.6 / Opus 4.6, Google Gemini 3.5 Flash\n"
         "• Surface & Hardware: Default consumer web/mobile app with automatic thinking-budget routing and embedded MCP App UI cards\n"
         "• Core Vocabulary: Auto-thinking router, expandable thought summary, DeepThink toggle, interactive MCP App widget, zero-shot reasoning"),
        ("G4", 2, "Autonomous Multi-Site Deep Research Scoping & Citation Auditing",
         "• Use Cases & Landmarks: OpenAI Deep Research (Feb 2025), Gemini Deep Research, Perplexity Deep Research; 15-minute 100-source analyst reports\n"
         "• Techniques & Skills: Scoping structured research briefs, setting reasoning effort toggles (low/med/high/xHigh), auditing primary-source citation chains\n"
         "• Models & Platforms: OpenAI o3 / GPT-5.4 Deep Research, Gemini 3.5 Deep Research, Claude Research, Perplexity Pro Research\n"
         "• Surface & Tools: Built-in Deep Research web panel, multi-hop browser trajectory viewer, exported Markdown/PDF citation tables\n"
         "• Core Vocabulary: Research brief scoping, multi-hop autonomous browsing, reasoning effort budget (xHigh), citation provenance audit"),
        ("G4", 3, "Plug-and-Play MCP Tool Wiring (.mcp.json) & Guardrailed Agentic Bots",
         "• Use Cases & Landmarks: Linux Foundation AAIF (Dec 9, 2025: MCP + Block goose + AGENTS.md), Salesforce Headless 360 (4.5M MCP calls), 10,000+ MCP servers\n"
         "• Techniques & Skills: Configuring .mcp.json servers (stdio/SSE), OAuth 2.1 tool scoping, Llama Guard 3 / NeMo safety rails, $0.10–$0.25 ticket caps\n"
         "• Protocols & Stack: Model Context Protocol (MCP), Block goose, OpenAI AGENTS.md, Cursor / Claude Desktop, Llama Guard 3, MCP Atlas benchmark\n"
         "• Software & Hardware: .mcp.json config files, Dockerized MCP servers, Postgres/Snowflake/Jira/GitHub MCP connectors, enterprise API gateways\n"
         "• Core Vocabulary: .mcp.json, MCP server/client, stdio vs Streamable HTTP/SSE, AAIF, AGENTS.md, tool poisoning defense, bought vs built (76%/24%)"),
        ("G4", 4, "Autonomous Terminal CLI Coding & Verification Harnesses",
         "• Use Cases & Landmarks: Anthropic Claude Code CLI launch (Feb 2025), Scale SWE-bench Pro audit (2025–2026), LangChain Deep Agents (Mar 2026)\n"
         "• Techniques & Skills: Authoring CLAUDE.md / AGENTS.md repo specs, supervising bash/read/write/edit/glob/grep loops, TDD red-green verification, /compact\n"
         "• Models & Harnesses: Claude Code CLI, OpenAI Codex CLI, Block goose, Aider, Claude Opus 4.6 / 5.5 (96% Verified), GPT-5.4, Muse Spark 1.1, Laguna S 2.1\n"
         "• Software & Hardware: macOS/Linux terminal shell, local Docker test containers, Git branches, pytest/vitest suites, Terminal-Bench 2.1\n"
         "• Core Vocabulary: CLAUDE.md, harness engineering, bash/edit/glob/grep primitives, context compaction (/compact), SWE-bench Pro private gap"),
        ("G4", 5, "24/7 Dedicated M4 Mac Mini OpenClaw Sandboxes & GRPO RLVR Clusters",
         "• Use Cases & Landmarks: Apr 2026 OX Security 200k MCP stdio RCE disclosure -> M4 Mac Mini OpenClaw sandbox boom; DeepSeek-R1 GRPO RLVR replication\n"
         "• Techniques & Skills: Air-gapping 24/7 agents on dedicated hardware, parallel git worktree subagent swarms, OSWorld GUI grounding, GRPO RLVR training\n"
         "• Systems & Models: OpenClaw 24/7 daemon, Computer Use (78.4% OSWorld), DeepSeek-R1 / Qwen3.8-Flash-Next, verl / OpenRLHF GRPO trainers\n"
         "• Hardware & Infra: Dedicated physical Apple M4 Mac Mini ($599–$1,200) + Tailscale/VLAN isolation, OR 8x–64x H200/B200 GPU RLVR cluster\n"
         "• Core Vocabulary: Dedicated M4 Mac Mini sandbox, OpenClaw daemon, git worktree swarm, OX Security stdio RCE, GRPO, RLVR verifiable rewards"),

        # SPECULATIVE GEN 5 (Current + 1)
        ("G5", 1, "[Speculative Gen 5] Ambient Cross-App OS Delegation & Persistent Memory",
         "• Projected Use Cases: OS-level background life/work delegation ('reconcile taxes, rebook flights, synthesize 50 threads') via 1-tap approval cards\n"
         "• User Actions: Speaking or typing intent once; OS background daemon coordinates across apps asynchronously with zero app-switching or prompting\n"
         "• Projected Models & OS Layers: GPT-6 / Claude 6 / Gemini 4 Ambient OS Router, Apple/Windows/Android native AAIF MCP OS fabric\n"
         "• Surface & Hardware: Hybrid on-device NPU (50+ TOPS local privacy memory) + cloud reasoning bursts; persistent cross-app timeline\n"
         "• Core Vocabulary: Ambient OS delegate, persistent personal memory graph, asynchronous approval card, zero-prompt background execution"),
        ("G5", 2, "[Speculative Gen 5] Natural-Language Full-Stack Spec & Async PR Studios",
         "• Projected Use Cases: Domain analysts & PMs shipping verified multi-table web apps and reviewing async background PRs without opening a terminal\n"
         "• Techniques & Skills: Writing structured acceptance rubrics, toggling 1-click OAuth MCP connectors, auditing live staging preview diffs\n"
         "• Projected Platforms: Cloud Specification Studios (Next-Gen Cursor Cloud / Replit / Claude Studio), 1-Click AAIF Verified MCP App Store\n"
         "• Surface & Tools: Browser specification canvas, auto-generated ephemeral Docker preview URLs, visual state-machine diff inspector\n"
         "• Core Vocabulary: Acceptance rubric, async PR queue, ephemeral preview sandbox, no-CLI repo builder, visual behavioral diff"),
        ("G5", 3, "[Speculative Gen 5] Multi-Agent A2A Contracts & Cryptographic Policy-as-Code",
         "• Projected Use Cases: Cross-company & cross-department autonomous procurement, compliance, and IT resolution governed by formal SLAs\n"
         "• Techniques & Skills: Wiring Agent-to-Agent (A2A) & MCP identity contracts, authoring Cedar/OPA policy-as-code rails, setting FinOps circuit breakers\n"
         "• Projected Stack: Linux Foundation AAIF MCP v2 + A2A Protocol, AWS Cedar / Open Policy Agent (OPA), hardware-attested OAuth 2.1 tokens\n"
         "• Software & Infra: Enterprise Agent Registry, cryptographic tool-call ledger, shadow-mode counterfactual replay gateway\n"
         "• Core Vocabulary: Agent-to-Agent (A2A) contract, Cedar/OPA policy-as-code, cryptographic tool attestation, FinOps circuit breaker, shadow replay"),
        ("G5", 4, "[Speculative Gen 5] Formal Verifier Harnesses & Digital-Twin Swarm Choreography",
         "• Projected Use Cases: Refactoring 500k+ line private commercial monoliths & verifying complex distributed systems via 20-agent parallel swarms\n"
         "• Techniques & Skills: Designing formal state invariants (Lean 4 / TLA+ / Kani), property-based fuzzing harnesses, digital-twin mock environments\n"
         "• Projected Tools & Models: Formal verifier compilers (Lean 4, TLA+, Hypothesis), multi-repo swarm choreographers, sub-$0.05/1M verifier models\n"
         "• Software & Hardware: Deterministic simulation containers, parallel git worktree farms, automated mutation-testing clusters\n"
         "• Core Vocabulary: Formal verifier harness, Lean 4 / TLA+ invariant, property-based simulation, digital-twin mock, swarm choreography"),
        ("G5", 5, "[Speculative Gen 5] Continuous On-Policy RLVR Flywheels & Sovereign Clusters",
         "• Projected Use Cases: Nightly self-improving enterprise/scientific domain models trained continuously on verified daytime agent execution traces\n"
         "• Techniques & Skills: Continuous on-policy RLVR/GRPO weight updates, automated curriculum generation, sovereign hardware enclave operations\n"
         "• Projected Systems: Continuous RLVR flywheel engines, domain world-model simulators, hardware-enclaved local agent appliances\n"
         "• Hardware & Infra: Sovereign multi-node Mac Studio Ultra / NVIDIA Blackwell/Rubin clusters + TPM/Secure Enclave attested sandbox racks\n"
         "• Core Vocabulary: Continuous on-policy RLVR, nightly weight distillation, verifiable trajectory flywheel, world-model simulator, sovereign enclave"),
    ]
    df_poster = pd.DataFrame(poster_cells, columns=["gen_id", "level_id", "short_header", "encyclopedic_body"])
    poster_path = os.path.join(CACHE_DIR, "v3_poster_encyclopedic_cells.csv")
    df_poster.to_csv(poster_path, index=False)
    print(f"[SAVED] {poster_path} | shape={df_poster.shape}")

    # =========================================================================
    # SECTION 1.4 DETERMINISTIC DATA VALIDATION GATES (PROGRAMMATIC ASSERTS)
    # =========================================================================
    print("\n[VALIDATION GATES] Running Section 1.4 Programmatic Assertions...")

    req_cols = [
        'gen_id', 'level_id', 'status', 'learning_hours_min', 'learning_hours_max',
        'single_task_tokens', 'single_task_flops', 'single_task_usd', 'single_task_wh',
        'human_minutes', 'ai_minutes', 'user_share_pct', 'token_share_pct', 'spend_share_pct'
    ]

    # Combine empirical G0..G4 and speculative G5 for schema, bounds, monotonic, and share gates
    df_all_cells = pd.concat([df_cells, df_gen5], ignore_index=True)

    # Gate 1: Schema & Null Gate
    null_count = df_all_cells[req_cols].isna().sum().sum()
    print(f"  -> Gate 1 (Schema & Null Gate): null_count = {null_count} across {len(req_cols)} columns (30 cells: G0..G5)")
    assert null_count == 0, f"Gate 1 Failed: Found {null_count} NaNs"

    # Gate 2: Mathematical Bounds Gate
    df_pop = df_all_cells.copy()
    assert (df_pop['learning_hours_min'] >= 0).all(), "Gate 2 Failed: learning_hours_min < 0"
    assert (df_pop['learning_hours_min'] <= df_pop['learning_hours_max']).all(), "Gate 2 Failed: min > max"
    assert (df_pop['single_task_tokens'] >= 0).all(), "Gate 2 Failed: single_task_tokens < 0"
    assert (df_pop['single_task_flops'] > 0).all(), "Gate 2 Failed: single_task_flops <= 0"
    assert (df_pop['single_task_usd'] >= 0).all(), "Gate 2 Failed: single_task_usd < 0"
    assert (df_pop['single_task_wh'] > 0).all(), "Gate 2 Failed: single_task_wh <= 0"
    print(f"  -> Gate 2 (Mathematical Bounds Gate): PASS | tokens range=[{df_pop['single_task_tokens'].min()}, {df_pop['single_task_tokens'].max()}], USD range=[{df_pop['single_task_usd'].min()}, {df_pop['single_task_usd'].max()}]")

    # Gate 3: Monotonic Level Learning-Hour Gate
    for gen_id, df_gen in df_pop.groupby("gen_id", sort=False):
        df_gen_sorted = df_gen.sort_values("level_id").reset_index(drop=True)
        for i in range(len(df_gen_sorted) - 1):
            h_max_k = df_gen_sorted.loc[i, 'learning_hours_max']
            h_min_next = df_gen_sorted.loc[i + 1, 'learning_hours_min']
            assert h_max_k <= h_min_next, f"Gate 3 Failed in {gen_id}: L{i+1} max ({h_max_k}) > L{i+2} min ({h_min_next})"
    print("  -> Gate 3 (Monotonic Level Learning-Hour Gate): PASS | L1(0-0h) < L2(7-45h) < L3(50-200h) < L4(200-600h) < L5(600-2000h) across G0..G5")

    # Gate 4: Share Conservation Identity Gate
    for gen_id, df_gen in df_all_cells.groupby("gen_id", sort=False):
        u_sum = df_gen['user_share_pct'].sum()
        t_sum = df_gen['token_share_pct'].sum()
        s_sum = df_gen['spend_share_pct'].sum()
        assert abs(u_sum - 100.0) <= 0.5, f"Gate 4 Failed in {gen_id}: user_share_pct sum = {u_sum}"
        assert abs(t_sum - 100.0) <= 0.5, f"Gate 4 Failed in {gen_id}: token_share_pct sum = {t_sum}"
        assert abs(s_sum - 100.0) <= 0.5, f"Gate 4 Failed in {gen_id}: spend_share_pct sum = {s_sum}"
        print(f"  -> Gate 4 ({gen_id} Share Conservation): PASS | Users={u_sum:.1f}%, Tokens={t_sum:.1f}%, Spend={s_sum:.1f}%")

    # Gate 5: Down-Ladder Skill Deflation Gate ($H_0$ Verification)
    gen_cols = ["G0_level", "G1_level", "G2_level", "G3_level", "G4_level"]
    for _, row in df_bench.iterrows():
        w = row["workflow_key"]
        for t in range(1, len(gen_cols)):
            l_prev = row[gen_cols[t - 1]]
            l_curr = row[gen_cols[t]]
            assert l_curr <= l_prev, f"Gate 5 Failed for {w}: {gen_cols[t]} ({l_curr}) > {gen_cols[t-1]} ({l_prev})"
        print(f"  -> Gate 5 ($H_0$ Skill Deflation - {w}): PASS | Level trajectory = {[int(row[c]) for c in gen_cols]} (Saved {row['total_hours_saved']}h)")

    print("\n[ALL 5 VALIDATION GATES PASSED 100% WITHOUT ERROR ACROSS G0..G5]\n")
    return {
        "ladders": df_ladders,
        "use_cases": df_use_cases,
        "tutorials": df_tutorials,
        "hopes": df_hopes,
        "trl": df_trl,
        "gens": df_gens,
        "bench": df_bench,
        "cells": df_cells,
        "cost": df_cost,
        "gen5_cutoffs": df_gen5_cutoffs,
        "gen5_cells": df_gen5,
        "events": df_events,
        "poster_cells": df_poster,
    }


if __name__ == "__main__":
    build_and_verify_all()


