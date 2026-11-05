import os
import re
import numpy as np
import pandas as pd

BASE_DIR = "/Users/z3540725/My Drive/personal/2026 10 17 AI_ladder_evol"
CACHE_DIR = os.path.join(BASE_DIR, "cache_v4")
os.makedirs(CACHE_DIR, exist_ok=True)

# Exact 6-Level Bracket Strings & Compact Plot Y-Axis Tick Labels (v4 Spec Section 2)
LEVEL_BRACKET_STRS = {
    1: "0h (0d) | $0",
    2: "<50h (~1 Wk / Short Course) | <$30",
    3: "<200h (~1 Mo / 1 Uni Subject) | <$100",
    4: "~600h (~1 Qtr / 1 Uni Semester) | ~$1.5k",
    5: "~2,000h (~1 Yr / Core Postgrad) | ~$500k",
    6: "~10,000h (~5 Yrs / Focused PhD) | ~$100M+",
}

COMPACT_TICK_LABELS = {
    1: "L1 (0h / 0d | $0)",
    2: "L2 (<50h / ~1 Wk | <$30)",
    3: "L3 (<200h / ~1 Mo | <$100)",
    4: "L4 (~600h / ~1 Sem | ~$1.5k)",
    5: "L5 (~2,000h / ~1 Yr | ~$500k)",
    6: "L6 (~10,000h / ~5 Yrs | ~$100M+)",
}

LEVEL_BEELINE_HOURS = {1: 0, 2: 50, 3: 200, 4: 600, 5: 2000, 6: 10000}
LEVEL_HARDWARE_USD  = {1: 0, 2: 30, 3: 100, 4: 1500, 5: 500000, 6: 100000000}


def build_and_verify_all():
    print(f"[CACHE-FIRST CHECK] Inspecting v4 cache directory: {CACHE_DIR}")

    # 1. Table 2.1: Existing AI Ladders & Emergent Folksonomy Catalog (20 ladders mapped to 6-level v4 grid)
    existing_ladders = [
        ("L_LIT_01", "Karpathy Software 1.0 / 2.0 / 3.0", "Andrej Karpathy", "2017-11", 3,
         "Explicit Code, Learned Weights, Natural Language Prompts, Vibe Coding (2025)",
         "Rungs 1-2: Classical Code & Supervised Neural Nets",
         "Rung 3 (in 2017-2022): Natural Language Programming of Universal Models",
         "G0->G1 (2020-06) & G1->G2 (2022-11)", 0.72, 0.65, 0.85, 0.40),
        ("L_LIT_02", "SAE L0-L5 Adapted for Coding Autonomy", "Industry / GitHub / Sourcegraph", "2021-06", 6,
         "Autocomplete, In-IDE Chat, Multi-File Edit, Background Agent, Unsupervised SWE",
         "L0-L2: Manual Coding, Ghost-Text Tab Autocomplete, Chat Copy-Paste",
         "L4-L5: Fully Autonomous Unsupervised Full-Lifecycle Software Engineering",
         "G1->G2 (2022-11) & G2->G3 (2024-05)", 0.78, 0.82, 0.75, 0.55),
        ("L_LIT_03", "Stanford CS224N -> CS324 Progression", "Manning, Liang, Hashimoto", "2022-01", 4,
         "Word Vectors, Fine-Tuned BERT, Few-Shot Prompting, Scaling Laws & Pretraining",
         "Rungs 1-3: TF-IDF/Word2Vec, Pretrained Encoders, Few-Shot In-Context Learning",
         "Rung 4: Autonomous Multimodal Foundation Agents",
         "G0->G1 (2020-06)", 0.80, 0.88, 0.82, 0.70),
        ("L_LIT_04", "DeepLearning.AI Practitioner Course Ladder", "Andrew Ng & Partners", "2023-05", 5,
         "Prompt Engineering, Chat with Your Data (RAG), Fine-Tuning, Agentic Workflows, Swarms",
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
        ("L_LIT_15", "Cursor AI-Native Coding & Vibe Coding Progression", "Anysphere (Cursor) / Karpathy", "2024-06", 4,
         "Copilot++ Tab, Cmd+K Inline Diff, @codebase Chat, Composer Vibe Coding",
         "Rungs 1-3: Multi-Line Next-Edit Tab, Inline Prompt Diffs, Repo-Indexed Chat",
         "Rung 4: Zero-Review Autonomous Multi-File Feature Implementation",
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
    ladders_path = os.path.join(CACHE_DIR, "v4_existing_ladders.csv")
    df_ladders.to_csv(ladders_path, index=False)
    print(f"[SAVED] {ladders_path} | shape={df_ladders.shape}")

    # 2. Table 1.2 & Table 3.2: Standardized 6-Level Brackets, Cognitive Hierarchy & Role Mapping
    level_brackets = [
        (1, "Level 1: Casual Consumer & Zero-Config Delegate",
         LEVEL_BRACKET_STRS[1], COMPACT_TICK_LABELS[1], 0, 0,
         "Outcome Intent & Surface Taste (Tier 1)",
         "Coupled Happy-Path Reliance (Zero Custom Verification)",
         "100% Using (Track A) / 0% Making (Track B)",
         "Casual User / Downstream Employee (0h)",
         "Default Web/Mobile UI, Passive OS/Browser Widget"),
        (2, "Level 2: Domain Power-User, Prompt & Workspace Analyst",
         LEVEL_BRACKET_STRS[2], COMPACT_TICK_LABELS[2], 50, 30,
         "Outcome Intent & Socratic Elicitation (Tier 1 -> Tier 2)",
         "Coupled AI Build + Self-Check with Human Visual Spot-Audit",
         "90% Using (Track A) / 10% No-Code Bot Configuration (Track B)",
         "Domain Power-User / Prompt & Workspace Analyst (<50h)",
         "Paid Web Tier ($20/mo), Playground, Long-Context Project / Deep Research UI"),
        (3, "Level 3: Applied Software Engineer (SWE) & Enterprise Bot Integrator",
         LEVEL_BRACKET_STRS[3], COMPACT_TICK_LABELS[3], 200, 100,
         "Declarative Pattern & Environment Literacy (Tier 2)",
         "Coupled Execution (AI Builds & Runs Happy-Path Tests; Shared Blind Spots)",
         "60% Using (Track A Vibe/CLI Coder) / 40% Making (Track B RAG/MCP Bot Integrator)",
         "Applied Software Engineer (SWE) & Enterprise Bot Integrator (<200h)",
         "AI IDE (Cursor), .mcp.json, Python/REST SDK, Vector DB, Guardrailed Bot Stack"),
        (4, "Level 4: Senior Harness SWE & Applied Single-GPU Machine Learning Engineer (MLE)",
         LEVEL_BRACKET_STRS[4], COMPACT_TICK_LABELS[4], 600, 1500,
         "Formal System & Invariant Specification (Tier 3)",
         "Decoupled Verification Oracles (Un-Gameable Property/Simulation Invariants & Deadlock Recovery)",
         "40% Using (Track A Senior Harness SWE) / 60% Making (Track B Single-GPU MLE)",
         "Senior Harness SWE (Track A) & Applied Single-GPU MLE (Track B) (~600h)",
         "Terminal CLI Harness + Decoupled Docker/Property Oracles OR Single GPU (24-80GB VRAM) PEFT/QLoRA"),
        (5, "Level 5: Staff Sandbox/Infra SWE & Distributed Systems/Post-Training MLE",
         LEVEL_BRACKET_STRS[5], COMPACT_TICK_LABELS[5], 2000, 500000,
         "Hard Infrastructure & Distributed Weight Optimization (Tier 4A)",
         "Hardware/OS Containment, High-QPS Serving & Verifiable Reward Environment Engineering",
         "20% Using (Track A Sandbox/Swarm Infra SWE) / 80% Making (Track B Distributed/Post-Training MLE)",
         "Staff Sandbox/Infra SWE (Track A) & Distributed Systems/Post-Training MLE (Track B) (~2,000h)",
         "Dedicated Physical Sandbox (M4 Mac Mini OpenClaw) / Worktree Swarms OR 8-64 GPU vLLM/DeepSpeed/GRPO Cluster"),
        (6, "Level 6: AI Research Scientist, Data/Benchmark Architect & Next-Gen Pioneer",
         LEVEL_BRACKET_STRS[6], COMPACT_TICK_LABELS[6], 10000, 100000000,
         "Frontier Mathematical Theory, Pretraining Curation & Paradigm Genesis (Tier 4B)",
         "Canonical Benchmark Metric Design, Scaling-Law Derivation & From-Scratch Base Pretraining (TRL 1-3)",
         "0% Casual Using / 100% Foundation & Genesis Making (Track B, recursively consuming L1-L5 tools)",
         "AI Research Scientist, Data/Benchmark Architect & Next-Gen Pioneer (~10,000h)",
         "1,024-100,000+ GPU Frontier Supercluster ($100M+), Multi-Trillion-Token Data Pipeline & Benchmark Forge"),
    ]
    df_levels = pd.DataFrame(level_brackets, columns=[
        "level_id", "level_folksonomy_name", "bracket_str", "compact_tick_label",
        "beeline_hours", "hardware_cap_usd", "cognitive_input_tier",
        "failure_boundary_anchor", "using_vs_making_split", "profession_mapping", "primary_surface"
    ])
    levels_path = os.path.join(CACHE_DIR, "v4_level_brackets.csv")
    df_levels.to_csv(levels_path, index=False)
    print(f"[SAVED] {levels_path} | shape={df_levels.shape}")

    # 3. Table 2.2: Use-Case & Producer-Consumer Inventory (30 Empirical Use Cases across G0..G4 x L1..L6)
    use_cases = [
        ("UC_01", "Passive Spellcheck, Translation & Smart Compose Widgets", "Track A: Casual User (served by Track B)", "2016-11", "2018-05", "Browser / Mobile App", "G0-L1 (0h (0d) | $0)"),
        ("UC_02", "No-Code AutoML Tabular/Text Classification & Regex Rules", "Track A: Domain Power-User", "2017-06", "2018-01", "Cloud Web Console / Sheets", "G0-L2 (<50h (~1 Wk / Short Course) | <$30)"),
        ("UC_03", "Classical Python NLP Sentiment, NER & XGBoost Pipelines", "Track A & B: Applied SWE / Data Analyst", "2017-06", "2017-09", "Jupyter / scikit-learn / spaCy", "G0-L3 (<200h (~1 Mo / 1 Uni Subject) | <$100)"),
        ("UC_04", "Single-GPU Pretrained BERT/RoBERTa Encoder Fine-Tuning", "Track B: Applied Single-GPU MLE (Grammarly GECToR)", "2018-10", "2019-06", "PyTorch / HuggingFace Single GPU", "G0-L4 (~600h (~1 Qtr / 1 Uni Semester) | ~$1.5k)"),
        ("UC_05", "Multi-GPU Seq2Seq Training & Quantized ONNX/TensorRT Serving", "Track B: Distributed Systems MLE", "2017-06", "2019-10", "Multi-GPU Node / C++ ONNX Runtime", "G0-L5 (~2,000h (~1 Yr / Core Postgrad) | ~$500k)"),
        ("UC_06", "Self-Attention Formulation, CommonCrawl Curation, GLUE Design & GPT-3 Genesis", "Track B: AI Research Scientist & Pioneer (TRL 1-3)", "2017-06", "2020-05", "TPU Pods / V100 Supercluster", "G0-L6 (~10,000h (~5 Yrs / Focused PhD) | ~$100M+)"),

        ("UC_07", "One-Key IDE Ghost-Text Autocomplete & Viral Consumer Web Demos", "Track A: Casual User (Copilot Tab / Craiyon)", "2021-06", "2022-06", "VS Code Plugin / Web Demo", "G1-L1 (0h (0d) | $0)"),
        ("UC_08", "Few-Shot Completion Prompting & Stop-Sequence Crafting", "Track A: Playground Power-User", "2020-06", "2021-03", "OpenAI Web Playground", "G1-L2 (<50h (~1 Wk / Short Course) | <$30; sank from G0-L3/L4)"),
        ("UC_09", "REST API Completion Wrappers & FAISS Embedding Search", "Track A & B: Applied SWE / Bot Integrator", "2020-06", "2021-11", "Python REST SDK / FAISS", "G1-L3 (<200h (~1 Mo / 1 Uni Subject) | <$100)"),
        ("UC_10", "Multi-Step Prompt Chains, Self-Consistency & Curated Fine-Tune CLI", "Track A (Harness SWE) & Track B (Applied MLE)", "2021-12", "2022-05", "Python Orchestrator / Fine-Tune CLI", "G1-L4 (~600h (~1 Qtr / 1 Uni Semester) | ~$1.5k)"),
        ("UC_11", "Distributed Multi-GPU Full-Weight Sharding (DeepSpeed ZeRO-3)", "Track B: Distributed Systems MLE", "2020-10", "2022-03", "8-64x A100 Cluster + DeepSpeed", "G1-L5 (~2,000h (~1 Yr / Core Postgrad) | ~$500k)"),
        ("UC_12", "Scaling Laws, RLHF PPO Formulation, Pile/GitHub Curation, HumanEval & ChatGPT/GPT-4 Genesis", "Track B: AI Research Scientist & Pioneer (TRL 1-3)", "2020-06", "2022-10", "1,000-10,000x A100 Supercluster", "G1-L6 (~10,000h (~5 Yrs / Focused PhD) | ~$100M+)"),

        ("UC_13", "Zero-Shot Conversational Web Chat for Q&A & Drafting", "Track A: Casual User (ChatGPT)", "2022-11", "2022-12", "Browser / Mobile Chat UI", "G2-L1 (0h (0d) | $0; sank from G1-L2)"),
        ("UC_14", "System Persona Prompt Engineering, Custom GPTs & Discord Image Flags", "Track A: Prompt & Workspace Analyst", "2022-11", "2023-03", "ChatGPT Plus + Midjourney Discord", "G2-L2 (<50h (~1 Wk / Short Course) | <$30)"),
        ("UC_15", "Chunked Vector-DB RAG & Function-Calling Internal Company Bots", "Track B: Applied SWE & Enterprise Bot Integrator", "2023-03", "2023-06", "LangChain/LlamaIndex + Pinecone", "G2-L3 (<200h (~1 Mo / 1 Uni Subject) | <$100)"),
        ("UC_16", "Single-GPU 4-Bit QLoRA Adapter Tuning & Decoupled Eval Harnesses", "Track A (Senior SWE) & Track B (Single-GPU MLE)", "2023-05", "2023-07", "Single RTX 4090/A100 + PEFT/QLoRA", "G2-L4 (~600h (~1 Qtr / 1 Uni Semester) | ~$1.5k; sank from G1-L5)"),
        ("UC_17", "High-Throughput PagedAttention Serving Clusters (vLLM / TGI / FlashAttention-2)", "Track B: Staff Infra SWE & Distributed MLE", "2023-06", "2023-09", "8-64x H100/A100 Cluster + vLLM", "G2-L5 (~2,000h (~1 Yr / Core Postgrad) | ~$500k)"),
        ("UC_18", "Chinchilla/RoPE/DPO Theory, Multi-Trillion Web Curation, Chatbot Arena Elo & Omni/o1 Genesis", "Track B: AI Research Scientist & Pioneer (TRL 1-3)", "2022-11", "2024-04", "10,000-25,000x H100 Supercluster", "G2-L6 (~10,000h (~5 Yrs / Focused PhD) | ~$100M+)"),

        ("UC_19", "Built-In Multimodal Omni-Chat (Voice/Vision/Image) & Live UI Artifacts", "Track A: Casual User (GPT-4o / Claude Artifacts)", "2024-05", "2024-06", "Default Web/Mobile App + Artifact Pane", "G3-L1 (0h (0d) | $0; sank from G2-L2/L3)"),
        ("UC_20", "Drag-and-Drop 50-PDF Long-Context Workspaces & Audio Synthesis", "Track A: Workspace Analyst (Projects / NotebookLM)", "2024-05", "2024-09", "200k-2M Project Workspace UI", "G3-L2 (<50h (~1 Wk / Short Course) | <$30; sank from G2-L3 RAG)"),
        ("UC_21", "Vibe Coding in AI IDEs (Cursor Composer) & Guardrailed Enterprise RAG Bots", "Track A (Vibe SWE) & Track B (NeMo/RBAC Bot Integrator)", "2024-05", "2024-07", "Cursor IDE (.cursorrules) / Hybrid RAG", "G3-L3 (<200h (~1 Mo / 1 Uni Subject) | <$100)"),
        ("UC_22", "Agentic Graph Orchestration (LangGraph), Decoupled Oracles & DPO Tuning", "Track A (Senior Harness SWE) & Track B (Applied MLE)", "2024-03", "2024-06", "LangGraph StateGraph + Postgres + Single GPU", "G3-L4 (~600h (~1 Qtr / 1 Uni Semester) | ~$1.5k)"),
        ("UC_23", "Containerized Multi-Agent Eval Farms & Distributed Post-Training Clusters", "Track A (Staff Infra SWE) & Track B (Distributed MLE)", "2024-05", "2024-10", "Kubernetes Docker Farms + Multi-Node H100", "G3-L5 (~2,000h (~1 Yr / Core Postgrad) | ~$500k)"),
        ("UC_24", "RLVR/GRPO Theory, Verified Reasoning Trajectories, SWE-bench/OSWorld & DeepSeek-R1/o1/MCP Genesis", "Track B: AI Research Scientist & Pioneer (TRL 1-3)", "2024-05", "2024-12", "16,000-50,000x H100/H200 Supercluster", "G3-L6 (~10,000h (~5 Yrs / Focused PhD) | ~$100M+)"),

        ("UC_25", "Zero-Shot Auto-Routed Reasoners & Interactive In-Chat MCP Widgets", "Track A: Casual User (GPT-5 Router / R1 / Claude 4.6)", "2025-01", "2025-02", "Default Auto-Routing Web/Mobile UI", "G4-L1 (0h (0d) | $0; sank from G2/G3-L2 CoT)"),
        ("UC_26", "Autonomous Deep Research Agents & Socratic Constraint Elicitation", "Track A: Research Analyst (Deep Research UI)", "2025-01", "2025-02", "Built-In Deep Research Web Panel", "G4-L2 (<50h (~1 Wk / Short Course) | <$30; sank from G3-L4 graphs)"),
        ("UC_27", "Plug-and-Play MCP Server Wiring (.mcp.json) & Coupled Terminal CLI Delegation", "Track A (Applied SWE) & Track B (Enterprise MCP Bot Builder)", "2024-11", "2025-03", "Claude Code / Cursor + .mcp.json + AGENTS.md", "G4-L3 (<200h (~1 Mo / 1 Uni Subject) | <$100; sank from G3-L4)"),
        ("UC_28", "Formal System Invariant Specification, Decoupled CLI Test Oracles & Verifier Tuning", "Track A (Senior Harness SWE) & Track B (Single-GPU MLE)", "2025-02", "2025-05", "CLAUDE.md + Property/Docker Oracles + Single GPU", "G4-L4 (~600h (~1 Qtr / 1 Uni Semester) | ~$1.5k)"),
        ("UC_29", "24/7 Air-Gapped M4 Mac Mini OpenClaw Sandboxes, Git Worktree Swarms & Multi-GPU GRPO RLVR", "Track A (Staff Sandbox SWE) & Track B (Post-Training MLE)", "2025-01", "2025-11", "Dedicated M4 Mac Mini OpenClaw / 8-64x H200 GRPO", "G4-L5 (~2,000h (~1 Yr / Core Postgrad) | ~$500k)"),
        ("UC_30", "Continuous RLVR & World-Model Theory, Multi-Env Synthetic Curricula, SWE-bench Pro & Gen 5 Genesis", "Track B: AI Research Scientist & Pioneer (TRL 1-3)", "2025-01", "2026-10", "50,000-100,000+ Blackwell B200 Supercluster", "G4-L6 (~10,000h (~5 Yrs / Focused PhD) | ~$100M+)"),
    ]
    df_use_cases = pd.DataFrame(use_cases, columns=[
        "use_case_id", "use_case_name", "track", "first_appearance",
        "mainstream_crossover", "target_surface", "mapped_cell_and_note"
    ])
    uc_path = os.path.join(CACHE_DIR, "v4_use_cases.csv")
    df_use_cases.to_csv(uc_path, index=False)
    print(f"[SAVED] {uc_path} | shape={df_use_cases.shape}")

    # 4. Table 2.3: Cumulative "Beeline" Curriculum, Tutorial & L6 Foundational Paper Inventory (24 items across L1..L6)
    tutorials = [
        ("TUT_01", "Google Cloud AutoML Web Guide & Regex101 Interactive Tutorial", "2018-01",
         "regex lookahead, CSV schema upload, precision-recall threshold, AutoML console",
         50, "Web Console / Spreadsheet", "L2: <50h (~1 Wk / Short Course) | <$30"),
        ("TUT_02", "Coursera Machine Learning (Ng) & scikit-learn / spaCy Documentation", "2017-06",
         "TF-IDF matrices, n-grams, XGBoost, hyperparameter grid search, spaCy NER",
         200, "Jupyter / Python SDK", "L3: <200h (~1 Mo / 1 Uni Subject) | <$100"),
        ("TUT_03", "Stanford CS224N (NLP with Deep Learning) & Fast.ai Practical Deep Learning", "2018-09",
         "Word2Vec, BiLSTM-CRF, self-attention, BERT fine-tuning, AdamW warmup",
         600, "PyTorch Single-GPU Notebook", "L4: ~600h (~1 Qtr / 1 Uni Semester) | ~$1.5k"),
        ("TUT_04", "Harvard Annotated Transformer, Fairseq Distributed & ONNX Runtime C++ Manual", "2018-04",
         "multi-head attention tensors, beam search, FP16/INT8 graph quantization, Horovod DDP",
         2000, "Multi-GPU Node / C++ Serving", "L5: ~2,000h (~1 Yr / Core Postgrad) | ~$500k"),
        ("TUT_05", "Vaswani 'Attention Is All You Need' (2017), Devlin BERT (2018), Wang GLUE & Radford GPT-2/3 Specs", "2017-06",
         "scaled dot-product attention math, Masked Language Modeling, CommonCrawl MinHash dedup, GLUE/SQuAD 2.0 harness",
         10000, "TPU Pod / V100 Frontier Supercluster", "L6: ~10,000h (~5 Yrs / Focused PhD) | ~$100M+"),

        ("TUT_06", "OpenAI GPT-3 Playground Guide & Few-Shot Prompting Cookbooks", "2020-07",
         "few-shot exemplars, completion prefix, stop tokens, temperature, frequency penalty",
         50, "OpenAI Web Playground", "L2: <50h (~1 Wk / Short Course) | <$30"),
        ("TUT_07", "OpenAI REST API Cookbook & FAISS Dense Vector Search Tutorials", "2021-06",
         "completion APIs, cosine similarity, dense embeddings, rate-limit exponential backoff",
         200, "Python REST SDK / VS Code", "L3: <200h (~1 Mo / 1 Uni Subject) | <$100"),
        ("TUT_08", "Stanford CS324 (Large Language Models) & Wei Chain-of-Thought / Self-Consistency Papers", "2022-01",
         "prompt chaining, self-consistency voting, JSONL fine-tune CLI, calibration",
         600, "Python Orchestrator / Cloud Fine-Tune CLI", "L4: ~600h (~1 Qtr / 1 Uni Semester) | ~$1.5k"),
        ("TUT_09", "Microsoft DeepSpeed ZeRO-3 & Megatron-LM 3D Parallelism Engineering Manuals", "2021-04",
         "ZeRO-3 optimizer state sharding, tensor parallelism, BF16 mixed precision, NCCL all-reduce",
         2000, "Multi-Node A100 Cluster", "L5: ~2,000h (~1 Yr / Core Postgrad) | ~$500k"),
        ("TUT_10", "Kaplan Scaling Laws (2020), Ouyang InstructGPT RLHF (2022), Gao The Pile & Chen HumanEval pass@k", "2020-01",
         "power-law compute scaling L(N,D,C), Bradley-Terry reward model, PPO KL-penalty, unbiased pass@k estimator",
         10000, "1,000-10,000x A100 Supercluster", "L6: ~10,000h (~5 Yrs / Focused PhD) | ~$100M+"),

        ("TUT_11", "DeepLearning.AI: ChatGPT Prompt Engineering (Ng & Fulford) & Midjourney Parameter Guide", "2023-05",
         "system personas, delimiter tags, step-by-step CoT, Custom GPTs, Midjourney --ar --v flags",
         50, "Web Chat UI / Discord", "L2: <50h (~1 Wk / Short Course) | <$30"),
        ("TUT_12", "DeepLearning.AI: LangChain Chat with Your Data (Chase) & Building RAG Agents (Liu)", "2023-07",
         "RecursiveCharacterTextSplitter, vector databases, HNSW index, top-k retrieval, function calling",
         200, "Python SDK + Vector DB", "L3: <200h (~1 Mo / 1 Uni Subject) | <$100"),
        ("TUT_13", "HuggingFace PEFT / bitsandbytes 4-Bit QLoRA Guide (Dettmers) & TRL SFTTrainer Docs", "2023-05",
         "4-bit NF4 quantization, LoRA rank r, lora_alpha, target_modules, decoupled eval harness",
         600, "Single GPU + PyTorch/PEFT", "L4: ~600h (~1 Qtr / 1 Uni Semester) | ~$1.5k"),
        ("TUT_14", "vLLM PagedAttention Paper/Docs (Kwon et al.) & Dao FlashAttention-2 CUDA Kernel Guide", "2023-06",
         "vLLM PagedAttention, non-contiguous KV-cache blocks, continuous batching, FlashAttention-2 SRAM tiling",
         2000, "Multi-Node H100/A100 Serving Cluster", "L5: ~2,000h (~1 Yr / Core Postgrad) | ~$500k"),
        ("TUT_15", "Hoffmann Chinchilla (2022), Rafailov DPO (2023), Soldaini Dolma / Penedo FineWeb & Chiang Chatbot Arena", "2022-03",
         "Chinchilla 20-tokens/param optimal scaling, DPO implicit reward math, FineWeb classifier filtering, Bradley-Terry Elo",
         10000, "10,000-25,000x H100 Frontier Cluster", "L6: ~10,000h (~5 Yrs / Focused PhD) | ~$100M+"),

        ("TUT_16", "Anthropic Claude Projects / Artifacts Guide & Google NotebookLM Long-Context Manual", "2024-06",
         "million-token context curation, project folders, Socratic prompt elicitation, Audio Overviews",
         50, "Long-Context Project Workspace", "L2: <50h (~1 Wk / Short Course) | <$30"),
        ("TUT_17", "Cursor Composer Vibe Coding Guide (.cursorrules) & NVIDIA NeMo Guardrails Colang Manual", "2024-07",
         "vibe coding, multi-file IDE diffs, @codebase indexing, .cursorrules, Colang dialog rails, RBAC filtering",
         200, "Cursor AI IDE / Enterprise Bot SDK", "L3: <200h (~1 Mo / 1 Uni Subject) | <$100"),
        ("TUT_18", "LangChain Academy: Agentic Orchestration with LangGraph & Decoupled State Checkpointing", "2024-06",
         "agentic orchestration, cyclic StateGraph, conditional edges, Postgres checkpointer, interrupt_before",
         600, "Python Agent Graph SDK + Docker", "L4: ~600h (~1 Qtr / 1 Uni Semester) | ~$1.5k"),
        ("TUT_19", "SWE-bench Docker Evaluation Harness Manual & Multi-Node vLLM/Ray Orchestrator Guide", "2024-08",
         "containerized repo eval farms, orchestrator-workers topology, synthetic trajectory replay, DPO post-training",
         2000, "Kubernetes Docker Farm + H100 Cluster", "L5: ~2,000h (~1 Yr / Core Postgrad) | ~$500k"),
        ("TUT_20", "Snell Test-Time Compute Scaling (2024), Shao DeepSeekMath GRPO (2024), Jimenez SWE-bench & Anthropic MCP Spec", "2024-04",
         "RLVR verifiable reward math, Group Relative Policy Optimization (GRPO), SWE-bench Verified Docker grading, MCP protocol genesis",
         10000, "16,000-50,000x H100/H200 Supercluster", "L6: ~10,000h (~5 Yrs / Focused PhD) | ~$100M+"),

        ("TUT_21", "OpenAI / Gemini Deep Research Scoping Guide & Socratic Elicitation Playbook", "2025-02",
         "multi-hop web research, Socratic constraint elicitation, reasoning effort budget, citation provenance audit",
         50, "Deep Research Web Panel", "L2: <50h (~1 Wk / Short Course) | <$30"),
        ("TUT_22", "DeepLearning.AI: Building with MCP (.mcp.json) & Coupled Terminal Agent Delegation", "2025-03",
         "MCP tool servers, .mcp.json stdio/SSE, AGENTS.md, coupled CLI build-and-test delegation, Llama Guard 3",
         200, "AI IDE / Terminal CLI + MCP SDK", "L3: <200h (~1 Mo / 1 Uni Subject) | <$100"),
        ("TUT_23", "UVA CS 6501 (Agentic AI) & Anthropic Claude Code Harness / Property-Based Oracle Engineering", "2025-06",
         "CLAUDE.md harness engineering, decoupled verification oracles, property-based invariants, Docker test isolation",
         600, "Terminal CLI + Decoupled Docker/Property Oracles", "L4: ~600h (~1 Qtr / 1 Uni Semester) | ~$1.5k"),
        ("TUT_24", "OpenClaw M4 Mac Mini Sandbox Guide, Git Worktree Swarms & DeepSeek-R1 / verl GRPO Cookbook", "2025-11",
         "agent swarms, parallel git worktrees, dedicated M4 Mac Mini OpenClaw daemon, verl GRPO RLVR training",
         2000, "Dedicated M4 Mac Mini Sandbox / Multi-GPU GRPO", "L5: ~2,000h (~1 Yr / Core Postgrad) | ~$500k"),
        ("TUT_25", "DeepSeek-R1 Technical Report (2025), Scale SWE-bench Pro / MCP Atlas Specs & Frontier World-Model Papers", "2025-01",
         "pure RLVR cold-start emergence, multi-environment synthetic trajectory curation, SWE-bench Pro private repo harness, world-model pretraining",
         10000, "50,000-100,000+ Blackwell B200 Supercluster", "L6: ~10,000h (~5 Yrs / Focused PhD) | ~$100M+"),
    ]
    df_tutorials = pd.DataFrame(tutorials, columns=[
        "tutorial_id", "resource_name", "release_date", "keywords_taught",
        "beeline_hours", "target_surface", "mapped_level"
    ])
    tut_path = os.path.join(CACHE_DIR, "v4_tutorials.csv")
    df_tutorials.to_csv(tut_path, index=False)
    print(f"[SAVED] {tut_path} | shape={df_tutorials.shape}")

    # 5. Table 2.3b: Comprehensive Glossary Literature Review (36 Core AI Keywords Mapped 1-to-1 Across the 6x6 Grid)
    glossary_rows = [
        ("KW_01", "Autocorrect & Smart Compose", "Chen et al. (Gmail Smart Compose, KDD 2019); Wu et al. (GNMT, 2016)", "2018-05",
         "Passive background sequence models predicting 1-3 words inline or underlining typos with zero user prompting.",
         "Tier 1: Outcome Intent (0h)", "G0-L1", "Remains passive baseline; superseded at L1 by active chat (G2) and ambient OS delegates (G5)."),
        ("KW_02", "AutoML & Regex Intent Rules", "Zoph & Le (NAS, 2017); Google Cloud AutoML (2018-01)", "2018-01",
         "Uploading labeled CSV tables to automated cloud model search or writing regular-expression intent trees.",
         "Tier 1->2: Surface Configuration (<50h)", "G0-L2", "Sinks into G1-L2 few-shot prompting and G2-L1 zero-shot classification."),
        ("KW_03", "TF-IDF & Gradient Boosted Trees (XGBoost)", "Salton & Buckley (1988); Chen & Guestrin (XGBoost, KDD 2016); Honnibal (spaCy v2, 2017)", "2017-06",
         "Term-frequency inverse-document-frequency sparse matrices paired with boosted decision trees and transition-based NER.",
         "Tier 2: Declarative Library Literacy (<200h)", "G0-L3", "Unstructured text tasks sink to G1-L2/G2-L1; tabular XGBoost persists for structured data."),
        ("KW_04", "Pretrained Encoders & Fine-Tuning (BERT)", "Devlin et al. (BERT, NAACL 2019, arXiv 2018-10); Liu et al. (RoBERTa, 2019); Omelianchuk et al. (GECToR, 2020)", "2018-10",
         "Transfer learning by attaching a task-specific classification/tagging head to a bidirectional Transformer encoder on a single GPU.",
         "Tier 3: Formal Loss & Hyperparameter Calibration (~600h)", "G0-L4", "Sinks to G1-L2 few-shot ICL for general tasks; evolves into G2-L4 4-bit QLoRA."),
        ("KW_05", "Seq2Seq & Graph Quantization (ONNX / TensorRT)", "Sutskever et al. (2014); Ott et al. (fairseq, 2019); Bai et al. (ONNX Runtime, 2019)", "2019-07",
         "Multi-GPU encoder-decoder training and FP16/INT8 computation-graph fusion for sub-20ms production serving.",
         "Tier 4A: Hard Serving & Distributed Infra (~2,000h)", "G0-L5", "Evolves into G1-L5 DeepSpeed ZeRO and G2-L5 vLLM PagedAttention."),
        ("KW_06", "Self-Attention, Transformer & Masked Language Modeling", "Vaswani et al. ('Attention Is All You Need', NeurIPS 2017); Radford et al. (GPT-2/3, 2019-2020); Wang et al. (GLUE, 2018)", "2017-06",
         "Foundational QKV scaled dot-product attention math, WebText/CommonCrawl deduplication, GLUE benchmark design, and from-scratch pretraining.",
         "Tier 4B: Frontier Mathematical & Pretraining Genesis (~10,000h)", "G0-L6", "TRL 1-3 origin of Gen 1-4 foundation models; pretraining recipes sink into G1-L4/L5 libraries."),

        ("KW_07", "Ghost-Text Autocomplete (Copilot Tab)", "Chen et al. (Codex, 2021-07); GitHub Copilot Preview (2021-06)", "2021-06",
         "Zero-config IDE extension streaming inline gray code completions accepted with a single Tab keystroke.",
         "Tier 1: Surface Taste (0h)", "G1-L1", "Expands into G3-L3 multi-file Vibe Coding (Cursor Composer) and G4-L3 CLI agents."),
        ("KW_08", "Few-Shot Prompting & In-Context Learning (ICL)", "Brown et al. ('Language Models are Few-Shot Learners', GPT-3, NeurIPS 2020)", "2020-06",
         "Conditioning raw completion models via 3-to-5 Input:/Output: exemplars and stop sequences without weight updates.",
         "Tier 1->2: Prompt Pattern Literacy (<50h)", "G1-L2", "Stop-sequence hacks become obsolete in G2-L1 RLHF chat; exemplars sink into automatic prompt optimizers."),
        ("KW_09", "Dense Embeddings & Vector Search (FAISS)", "Johnson et al. (FAISS, IEEE TBD 2019); Neelakantan et al. (OpenAI Embeddings, 2022-01)", "2021-06",
         "Mapping text passages into dense unit-sphere vectors for fast maximum inner-product / cosine similarity lookup.",
         "Tier 2: API & Index Integration (<200h)", "G1-L3", "Forms the retrieval core of G2-L3 Vector RAG before sinking into G3-L2 long-context workspaces."),
        ("KW_10", "Prompt Chaining & Self-Consistency Voting", "Wu et al. (AI Chains, CHI 2022); Wei et al. (CoT, 2022-01); Wang et al. (Self-Consistency, ICLR 2023, arXiv 2022-03)", "2022-03",
         "Decomposing tasks into sequential LLM calls and sampling multiple reasoning paths to take a majority vote.",
         "Tier 3: Multi-Step Error-Bound Calibration (~600h)", "G1-L4", "Sinks to G2-L2 manual CoT and G4-L1 built-in RLVR test-time reasoning routers."),
        ("KW_11", "Distributed Sharding (DeepSpeed ZeRO & Tensor Parallelism)", "Rajbhandari et al. (ZeRO, SC20 2020); Shoeybi et al. (Megatron-LM, 2019)", "2020-10",
         "Partitioning optimizer states, gradients, and parameters (ZeRO-3) and attention heads across multi-node GPU fabrics.",
         "Tier 4A: Distributed Cluster Engineering (~2,000h)", "G1-L5", "Single-task adaptation sinks to G2-L4 single-GPU QLoRA; ZeRO remains core to L5/L6 training."),
        ("KW_12", "Neural Scaling Laws, RLHF & Unbiased pass@k", "Kaplan et al. (Scaling Laws, 2020-01); Ouyang et al. (InstructGPT RLHF, 2022-03); Gao et al. (The Pile, 2020); Chen et al. (HumanEval, 2021)", "2020-01",
         "Power-law compute allocation, Bradley-Terry preference reward modeling + PPO alignment, and functional code execution metrics.",
         "Tier 4B: Frontier Alignment & Benchmark Genesis (~10,000h)", "G1-L6", "TRL 1-3 origin of Gen 2 ChatGPT explosion; PPO alignment simplifies into G2-L6/G3-L4 DPO."),

        ("KW_13", "Zero-Shot Chat & Multi-Turn Dialog", "OpenAI ChatGPT (gpt-3.5-turbo, 2022-11); Bai et al. (Constitutional AI, 2022-12)", "2022-11",
         "Instruction-tuned conversational interface allowing zero-hour natural-language Q&A, drafting, and iterative follow-ups.",
         "Tier 1: Outcome Intent (0h)", "G2-L1", "Absorbs G1-L2 completion prompting; upgrades to G3-L1 omni-modal chat and G4-L1 auto-thinking."),
        ("KW_14", "Prompt Engineering, System Persona & Chain-of-Thought (CoT)", "Wei et al. (CoT, NeurIPS 2022); Kojima et al. ('Let's think step by step', 2022-05); Ng & Fulford (2023-05)", "2022-11",
         "Structuring system instructions, XML delimiters, role personas, and explicit step-by-step reasoning triggers in chat UIs.",
         "Tier 1->2: Structured Prompting (<50h)", "G2-L2", "Manual 'think step by step' triggers sink into G4-L1 RLVR auto-routers; evolves into G4-L2 Socratic specs."),
        ("KW_15", "Retrieval-Augmented Generation (RAG) & Function Calling", "Lewis et al. (RAG, NeurIPS 2020); Chase (LangChain, 2022-10); Liu (LlamaIndex, 2022-11); OpenAI Function Calling (2023-06)", "2023-03",
         "Chunking external documents into vector databases (Pinecone/Chroma) for top-k context injection and JSON schema tool execution.",
         "Tier 2: Declarative Pipeline Integration (<200h)", "G2-L3", "Small-corpus (<50 PDF) RAG sinks to G3-L2 long-context workspaces; tool schemas standardize into G4-L3 MCP."),
        ("KW_16", "LoRA / QLoRA (4-Bit Adapter Tuning) & ReAct Loops", "Hu et al. (LoRA, ICLR 2022); Dettmers et al. (QLoRA, NeurIPS 2023, arXiv 2023-05); Yao et al. (ReAct, ICLR 2023)", "2023-05",
         "Backpropagating through low-rank adapters over frozen 4-bit NormalFloat (NF4) base weights on 1 GPU; interleaved Reason+Act loops.",
         "Tier 3: Weight-Rank & Failure-Loop Calibration (~600h)", "G2-L4", "Sinks G1-L5 multi-GPU tuning to 1 GPU; brittle ReAct loops evolve into G3-L4 cyclic StateGraphs."),
        ("KW_17", "vLLM, PagedAttention, KV-Cache & FlashAttention", "Kwon et al. (vLLM / PagedAttention, SOSP 2023, arXiv 2023-06); Dao et al. (FlashAttention-2, 2023-07)", "2023-06",
         "Operating-system-inspired virtual memory paging for non-contiguous KV-cache blocks and IO-aware GPU SRAM attention tiling.",
         "Tier 4A: High-Throughput Inference Systems (~2,000h)", "G2-L5", "Eliminates 60-80% KV-cache VRAM waste; becomes standard serving backbone for G3/G4 eval & RLVR clusters."),
        ("KW_18", "Chinchilla Scaling, RoPE Long-Context, DPO & Chatbot Arena", "Hoffmann et al. (Chinchilla, 2022-03); Su et al. (RoPE, 2021); Rafailov et al. (DPO, 2023-05); Chiang et al. (Chatbot Arena, 2024)", "2023-05",
         "Compute-optimal token-to-parameter scaling, rotary position interpolation to 128k-2M tokens, closed-form preference optimization, and Elo human evals.",
         "Tier 4B: Frontier Scaling & Alignment Genesis (~10,000h)", "G2-L6", "TRL 1-3 origin of Gen 3 long-context omni-models; DPO sinks into G3-L4 open-source post-training toolkits."),

        ("KW_19", "Omni-Modal Chat & Live UI Canvas / Artifacts", "OpenAI GPT-4o (2024-05); Anthropic Claude 3.5 Sonnet Artifacts (2024-06)", "2024-05",
         "End-to-end joint text-audio-vision tokenization paired with sandboxed side-by-side browser rendering of live React/SVG applications.",
         "Tier 1: Outcome Intent & Aesthetic Taste (0h)", "G3-L1", "Sinks G2-L2 separate image Discord tools and G2-L3 UI prototyping into zero-setup consumer chat."),
        ("KW_20", "Long-Context Workspaces (1M–2M) & Context Caching", "Reid et al. (Gemini 1.5 Pro 1M-2M, 2024-02); Anthropic Claude Projects & 90% Prompt Caching (2024-06/08); Google NotebookLM (2024-09)", "2024-06",
         "Drag-and-drop workspaces holding 50-100 full PDFs in active KV-cache memory without chunking or vector database code.",
         "Tier 1->2: Workspace Curation (<50h)", "G3-L2", "Absorbs G2-L3 personal/team Vector RAG into a no-code drag-and-drop folder."),
        ("KW_21", "Vibe Coding & Multi-File AI IDE Composer", "Anysphere Cursor Composer (2024-06); Karpathy ('Vibe Coding', 2025-02); NVIDIA NeMo Guardrails (2023-2024)", "2024-06",
         "Prompting multi-file repository diffs inside an AI-native IDE and accepting coupled build+run outputs by taste without reading raw diffs.",
         "Tier 2: Declarative Pattern & Coupled IDE Literacy (<200h)", "G3-L3", "Coupled happy-path coding stays at L2/L3; complex commercial repos require G4-L4 decoupled test oracles."),
        ("KW_22", "Agentic Orchestration & Cyclic StateGraphs (LangGraph)", "Chase & LangChain (LangGraph, 2024-01); Schluntz & Zhang ('Building Effective Agents', Anthropic, 2024-12)", "2024-03",
         "Explicit cyclic state machines with conditional routing, persistent database checkpoints, and human-in-the-loop interrupts.",
         "Tier 3: Formal State-Transition & Oracle Specification (~600h)", "G3-L4", "Web-research graphs sink into G4-L2 Deep Research; coding graphs sink into G4-L3/L4 CLI harnesses."),
        ("KW_23", "Containerized Eval Harnesses & Orchestrator-Workers", "Jimenez et al. (SWE-bench, ICLR 2024); OpenAI SWE-bench Verified (2024-08); Anthropic Orchestrator-Workers (2024-12)", "2024-08",
         "Distributed Kubernetes/Docker farms executing parallel agent patches against isolated repository unit-test suites.",
         "Tier 4A: Distributed Verification Infrastructure (~2,000h)", "G3-L5", "Single-repo Docker TDD sinks to G4-L4 local CLI harnesses; cluster farms evolve into G4-L5 RLVR verifiers."),
        ("KW_24", "Test-Time Compute Scaling, RLVR & GRPO Genesis", "Snell et al. (Test-Time Compute, 2024-08); Shao et al. (DeepSeekMath GRPO, 2024-02); Lambert et al. (Tulu 3 RLVR, 2024-11); Anthropic MCP (2024-11)", "2024-09",
         "Reinforcement Learning with Verifiable Rewards (RLVR) using Group Relative Policy Optimization (GRPO) without a critic network to unlock multi-step reasoning.",
         "Tier 4B: Frontier Reasoning & Protocol Genesis (~10,000h)", "G3-L6", "TRL 1-3 origin of Gen 4 (o1/o3, DeepSeek-R1, Claude Code, MCP); GRPO recipes sink to G4-L5 open post-training."),

        ("KW_25", "Auto-Routed Reasoners & Hidden Thinking Tokens", "OpenAI o1/o3 & GPT-5 Auto-Router (2024-12 / 2025); DeepSeek-R1 App (2025-01)", "2025-01",
         "Classifier routers silently allocating test-time RLVR thinking tokens on hard queries while keeping casual queries instant at 0h user effort.",
         "Tier 1: Outcome Intent (0h)", "G4-L1", "Renders G2-L2 manual 'Let's think step by step' CoT prompting obsolete overhead."),
        ("KW_26", "Deep Research Agents & Socratic Elicitation", "OpenAI Deep Research (2025-02); Gemini Deep Research (2024-12 / 2025)", "2025-02",
         "End-to-end RL browsing agents that interview the user to extract constraints (Socratic elicitation) and browse 50-100 sources into cited reports.",
         "Tier 1->2: Socratic Scoping & Provenance Audit (<50h)", "G4-L2", "Sinks G3-L4 custom web-research LangGraph pipelines into a built-in power-user panel."),
        ("KW_27", "Model Context Protocol (MCP) & Coupled CLI Delegation", "Anthropic MCP (2024-11); Linux Foundation AAIF (MCP + goose + AGENTS.md, 2025-12)", "2025-02",
         "Universal JSON-RPC client-server standard (.mcp.json) wiring databases/tools into IDEs and delegating happy-path tasks to terminal CLI agents.",
         "Tier 2: Declarative Protocol & Environment Literacy (<200h)", "G4-L3", "Replaces G2/G3 bespoke per-vendor API glue; sinks in G5-L2 to 1-click cloud spec studios."),
        ("KW_28", "Harness Engineering & Decoupled Verification Oracles", "Anthropic Claude Code CLI (2025-02); Scale AI SWE-bench Pro Audit (2025-09); UVA CS 6501 (2025)", "2025-02",
         "Designing CLAUDE.md architectural invariants and independent property/simulation test oracles that catch silent corruption where coupled agent self-tests fail.",
         "Tier 3: Formal System & Invariant Specification (~600h)", "G4-L4", "Separates Senior Harness SWEs (L4) from coupled L3 vibe/CLI coders; evolves into G5-L4 formal proof choreography."),
        ("KW_29", "Agent Swarms, Git Worktree Isolation & OpenClaw Sandboxes", "OpenClaw Mac Mini Sandbox Wave (2025-11); OX Security 200k MCP RCE Audit (2026-04); Sheng et al. (verl GRPO, 2025)", "2025-11",
         "Parallel multi-agent swarms running in isolated git worktrees on dedicated air-gapped hardware (M4 Mac Mini) OR multi-GPU GRPO RLVR post-training.",
         "Tier 4A: Physical Containment & Swarm/RLVR Infra (~2,000h)", "G4-L5", "Remediates host RCE risk of unisolated agents; offline GRPO evolves into G5-L5 continuous nightly RLVR."),
        ("KW_30", "Synthetic Trajectory Flywheels & SWE-bench Pro Genesis", "DeepSeek-AI (DeepSeek-R1, 2025-01); Scale AI (SWE-bench Pro & MCP Atlas, 2025-2026); Frontier Lab Pretraining (2026)", "2025-01",
         "From-scratch pretraining on multi-trillion synthetic reasoning trajectories, unseen private commercial repo benchmarks, and world-model architectures.",
         "Tier 4B: Frontier Paradigm & Benchmark Genesis (~10,000h)", "G4-L6", "TRL 1-3 origin of Speculative Gen 5 ambient OS routers, A2A contracts, and continuous RLVR flywheels."),

        ("KW_31", "Ambient OS Delegation & Cross-App Memory", "Speculative Gen 5 OS Fabric (Apple/Windows/Android + AAIF MCP Registry, 2026-2028)", "2027-03",
         "Zero-prompt background OS daemon executing multi-app life and work workflows asynchronously with one-tap approval cards.",
         "Tier 1: Outcome Intent (0h)", "G5-L1", "Sinks G4-L2 Deep Research and G4-L3 cross-app MCP actions into the default consumer OS layer."),
        ("KW_32", "Declarative Outcome Specs & Coupled Cloud Studios", "Speculative Gen 5 No-CLI Specification Studios (2026-2028)", "2027-03",
         "Conversational Socratic spec compilation and ephemeral cloud preview sandboxes shipping full-stack apps without opening a terminal.",
         "Tier 1->2: Outcome Rubric & Preview Taste (<50h)", "G5-L2", "Sinks G4-L3 .mcp.json wiring and happy-path single-repo CLI coding into a <50h no-CLI studio."),
        ("KW_33", "Agent-to-Agent (A2A) Contracts & Policy-as-Code Rails", "Linux Foundation AAIF A2A + MCP v2; AWS Cedar / Open Policy Agent (OPA) (2026-2028)", "2027-03",
         "Cryptographically attested cross-vendor agent identity contracts, deterministic Cedar/OPA authorization rails, and FinOps circuit breakers.",
         "Tier 2: Declarative Governance & Protocol Literacy (<200h)", "G5-L3", "Standardizes Track B enterprise multi-agent integration around verifiable SLAs and budget caps."),
        ("KW_34", "Formal Verification Oracles (Lean 4 / TLA+) & Digital Twins", "De Moura et al. (Lean 4); Lamport (TLA+); Speculative Gen 5 Swarm Choreography (2026-2028)", "2027-03",
         "Machine-checked mathematical state invariants (Lean 4 / TLA+ / Kani) and stateful digital-twin simulators grading 20-agent parallel swarms.",
         "Tier 3: Formal Mathematical Invariant Specification (~600h)", "G5-L4", "Upgrades G4-L4 pytest/Docker harnesses into formal proof oracles that eliminate cross-service race conditions."),
        ("KW_35", "Continuous Nightly On-Policy RLVR & Sovereign Enclaves", "Speculative Gen 5 Continuous RLVR Flywheels & Confidential Compute Appliances (2026-2028)", "2027-03",
         "Sovereign hardware-enclaved clusters distilling verified daytime agent execution traces into domain model weights every night via on-policy RLVR.",
         "Tier 4A: Sovereign Cluster & Continuous Weight Ops (~2,000h)", "G5-L5", "Upgrades G4-L5 static weights + periodic batch GRPO into closed-loop nightly weight adaptation."),
        ("KW_36", "Autonomous World-Model Genesis & Self-Play Theory", "Speculative Gen 5 Frontier Research Labs (2026-2029)", "2027-03",
         "Formulating causal physical/scientific world models, open-ended self-play discovery curricula, un-gamed frontier benchmarks, and $100M+ genesis runs.",
         "Tier 4B: Frontier Scientific & Paradigm Genesis (~10,000h)", "G5-L6", "Apex on-ladder TRL 1-3 generator of post-2029 embodied and scientific AI paradigms."),
    ]
    df_glossary = pd.DataFrame(glossary_rows, columns=[
        "keyword_id", "keyword_term", "seminal_citations", "anchor_date",
        "plain_english_definition", "cognitive_tier", "grid_cell_id", "evolutionary_trajectory"
    ])
    glossary_path = os.path.join(CACHE_DIR, "v4_glossary_lit_review.csv")
    df_glossary.to_csv(glossary_path, index=False)
    print(f"[SAVED] {glossary_path} | shape={df_glossary.shape}")

    # 6. Table 2.4 & Table 5.2b: The "Inventory of Hope" Ledger (20 contemporaneous hopes across G0-G4)
    hopes = [
        ("HOPE_01", "Capsule Networks (Hinton) Replacing CNNs & Transformers", "Gen 0", "G1", "Geoffrey Hinton / Academic ML", "Dynamic routing between capsules learning part-whole hierarchies with 10x less data", "Extinct", "Out-Standardized / Hardware Scaling (Transformers scaled cleanly on GPUs at G0-L6; Capsules hit compute wall)"),
        ("HOPE_02", "Symbolic-Neural Hybrid Ontologies (OWL/RDF + Deep Learning) as Only Path to Reasoning", "Gen 0", "G1", "Neuro-Symbolic AI Workshops", "Hand-crafted knowledge graphs governing neural feature extractors", "Extinct", "Foundation Model Absorption (In-context learning & RLVR absorbed soft reasoning without manual ontologies)"),
        ("HOPE_03", "Universal Small-Data Transfer Learning Eliminating Large Pretraining Clusters", "Gen 0", "G1", "Fast.ai / ULMFiT / Early NLP", "Single-GPU fine-tuning of 30M-100M models beating giant models on all tasks", "Extinct", "Foundation Model Absorption (G0-L6 GPT-3 175B scaling laws proved giant zero/few-shot models dominate)"),
        ("HOPE_04", "Pretrained Transformer Representation Transfer Across Text, Code & Vision", "Gen 0", "G1", "Vaswani et al. / Devlin et al. / OpenAI (G0-L6)", "Unified self-attention backbone scaling to generative text and code", "Survived", "Matured from G0-L6 (TRL 1-3) to TRL 9 (Became foundation of Gen 1-4)"),
        ("HOPE_05", "Standalone Prompt Marketplaces (PromptBase) as Permanent Professional Career", "Gen 1", "G2", "Early Prompt Engineering Influencers / VC", "Buying and selling secret $4.99 prompt strings as durable IP", "Extinct", "Foundation Model Absorption (G1-L6 RLHF instruction tuning & G3-L6 RLVR thinking made secret prompt hacks obsolete)"),
        ("HOPE_06", "Zero-Code End-to-End Production SaaS Generation from Single Codex Docstring", "Gen 1", "G2", "Early Codex / Copilot Demos (2021)", "Non-programmers generating full production backends from 1 paragraph in 2021", "Extinct", "Premature TRL / Capability Starvation (4k context & 0% multi-file state awareness caused immediate build failure until Gen 3/4)"),
        ("HOPE_07", "Conversational Instruction-Following & RLHF Alignment for Mass Consumers", "Gen 1", "G2", "OpenAI InstructGPT / Anthropic Constitutional AI (G1-L6)", "Turning raw completion models into safe zero-shot dialogue assistants", "Survived", "Matured from G1-L6 (TRL 1-3) to TRL 9 (Triggered Gen 2 ChatGPT explosion)"),
        ("HOPE_08", "Unconstrained Recursive Autonomous Loops (AutoGPT / BabyAGI) Running Businesses in 2023", "Gen 2", "G3", "GitHub Viral Repos / Twitter Hype (Apr 2023)", "Infinite while-loops over GPT-4 autonomously executing multi-day company projects", "Extinct", "Premature TRL / Capability Starvation (0.90^20 = 12.2% step survival caused infinite loops & $50 API burn)"),
        ("HOPE_09", "Every Enterprise Training Its Own From-Scratch Base LLM (BloombergGPT Model)", "Gen 2", "G3", "BloombergGPT ($3M+) / Enterprise Infra VCs", "Banks, hospitals, and retailers pretraining proprietary 50B base models from scratch", "Extinct", "Broken Unit Economics & Maintenance Friction (Frontier L6 APIs + L3/L4 RAG/QLoRA beat $3M bespoke base models in 6 months)"),
        ("HOPE_10", "Pure Vector Databases Permanently Replacing Long Context Windows", "Gen 2", "G3", "2023 Vector DB Boom (Pinecone/Weaviate/Milvus)", "4k-8k context remaining permanent; every 10-page document requiring vector chunking", "Extinct", "Foundation Model Absorption (G2-L6 RoPE 128k-2M long context + 90% prompt caching absorbed small/medium corpus Q&A into G3-L2)"),
        ("HOPE_11", "Proprietary Per-Vendor Chat Plugin Stores (Early ChatGPT Plugins 2023)", "Gen 2", "G3", "OpenAI Plugin Store Launch (Mar 2023)", "Closed vendor-specific JSON plugin manifests becoming the new App Store", "Extinct", "Out-Standardized (Deprecated in favor of open function calling and G3-L6 Anthropic/AAIF Model Context Protocol [MCP])"),
        ("HOPE_12", "Native Multimodal Omni-Models & 100k-2M Long-Context Workspaces", "Gen 2", "G3", "GPT-4V / Gemini 1.5 / Claude 3 (G2-L6)", "Unified text-vision-audio models with massive context and live code rendering", "Survived", "Matured from G2-L6 (TRL 1-3) to TRL 9 (Triggered Gen 3 Omni-Chat, Projects & Artifacts)"),
        ("HOPE_13", "Thin Single-Prompt SaaS Wrappers ('Chat with One PDF' Startups) as Defensible Moats", "Gen 3", "G4", "2023-2024 Wrapper Startup Wave", "Charging $20/mo for a single system prompt + file upload button over OpenAI API", "Extinct", "Foundation Model Absorption (Crushed when Claude Projects, NotebookLM & ChatGPT Canvas built it into L1/L2 for free)"),
        ("HOPE_14", "100% Unsupervised Zero-Human-Review Full-Lifecycle Software Engineering by 2025", "Gen 3", "G4", "SAE L5 Coding Hype / Early Devin Claims", "Firing engineering teams and letting autonomous agents push directly to production", "Extinct", "Premature TRL / Capability Starvation (G4-L6 Scale SWE-bench Pro proved 4.8-22.5 pt drop on private commercial code; requires L4 decoupled test oracles)"),
        ("HOPE_15", "In-House Custom Enterprise AI Builds Outperforming Purchased Vertical Tools", "Gen 3", "G4", "Enterprise IT Internal Build Mandates (2024)", "Internal IT building bespoke agent platforms beating commercial vendors", "Extinct", "Broken Unit Economics (MIT NANDA 2025 proved 67% success for bought tools vs 33% for in-house builds; Menlo 76% bought)"),
        ("HOPE_16", "Test-Time Reasoning (RLVR) + Standardized Tool Protocols (MCP) + Terminal CLI Agents", "Gen 3", "G4", "OpenAI o1 / DeepSeek-R1 / Anthropic MCP & Claude Code (G3-L6)", "RL on verifiable rewards unlocking multi-step terminal coding and standardized tool wiring", "Survived", "Matured from G3-L6 (TRL 1-3) to TRL 9 (Triggered Gen 4 Auto-Thinking, Deep Research, MCP & Claude Code)"),
        ("HOPE_17", "Unauthenticated Zero-Sandbox Local MCP & Browser Agents Running with Root Credentials", "Gen 4", "G5", "Early 2025 YOLO Agent Adoption", "Giving autonomous agents unrestricted host shell and primary browser cookie access", "Extinct", "Broken Security / Governance (Apr 2026 OX Security disclosure of 200,000 vulnerable stdio MCP instances forced isolated M4 Mac Mini / Docker sandboxes at G4-L5)"),
        ("HOPE_18", "Pure Pixel-Only GUI Clicking Replacing All API & CLI Harnesses in 2026", "Gen 4", "G5", "Early Computer-Use Only Theses", "Agents operating exclusively by taking screenshots and clicking pixels at 3-5s/click", "Extinct", "Broken Unit Economics (Bash CLI + MCP API calls are 50x faster and 20x cheaper; GUI clicking reserved for legacy non-API apps)"),
        ("HOPE_19", "OpenAI Level 4 'Innovators' & Level 5 'Autonomous Organizations' Operating at L1 in 2026", "Gen 4", "G5", "OpenAI 5-Level Ladder Top Rungs", "AI autonomously discovering new physical laws and running entire corporations without humans", "Extinct", "Premature TRL (2026 frontier deployments require L4 decoupled verification oracles and L6 human theoretical formulation)"),
        ("HOPE_20", "Sandboxed Multi-Agent Verification Swarms & Continuous RLVR Domain Flywheels", "Gen 4", "G5", "Anthropic / DeepSeek / AAIF / OpenClaw (G4-L5/L6)", "Isolated hardware/container sandboxes running parallel verified agent worktrees & RLVR loops", "Survived", "Active Frontier at Gen 4 Level 5-6 (Expanding into Gen 5)"),
    ]
    df_hopes = pd.DataFrame(hopes, columns=[
        "hope_id", "hope_thesis", "origin_gen", "target_gen", "proponents",
        "predicted_workflow", "fate", "extinction_or_maturation_mechanism"
    ])
    hopes_path = os.path.join(CACHE_DIR, "v4_hope_inventory.csv")
    df_hopes.to_csv(hopes_path, index=False)
    print(f"[SAVED] {hopes_path} | shape={df_hopes.shape}")

    # 7. Table 5.2a: On-Ladder TRL Maturation Trajectories (TRL 1-3 Anchored Inside G_t-L6 -> TRL 9 Built-In L1)
    trl_rows = [
        ("TRL_01", "Transformer Self-Attention & Pretrained Encoders", "2017-06 (G0-L6 Vaswani Paper)", "2018-10 (G0-L4 BERT GPU)", "2019-10 (G0-L3 HF pipeline)", "2019-11 (G0-L1 Google Search/Smart Compose)", 29, "Hardware & Pretraining Compute Scaling"),
        ("TRL_02", "In-Context Few-Shot Completion Learning", "2020-05 (G0-L6 GPT-3 Genesis)", "2020-06 (G1-L3 GPT-3 API)", "2020-09 (G1-L2 Playground)", "2021-06 (G1-L1 Copilot Tab Autocomplete)", 13, "API Waitlist & IDE Product Packaging"),
        ("TRL_03", "RLHF Instruction Tuning & Conversational Chat", "2017-06 (G0-L6 Christiano RLHF)", "2022-01 (G1-L6/L4 InstructGPT)", "2022-06 (G1-L2 Playground Chat)", "2022-11 (G2-L1 ChatGPT Web UI)", 65, "Post-Training Human Preference Alignment & Web UI"),
        ("TRL_04", "Retrieval-Augmented Generation (RAG over Private Docs)", "2020-05 (G0-L6 Lewis RAG Paper)", "2022-11 (G2-L4 Custom FAISS)", "2023-04 (G2-L3 LangChain/Pinecone)", "2024-06 (G3-L2/L1 Projects & NotebookLM)", 49, "128k-2M Context Scaling & Prompt Caching"),
        ("TRL_05", "Parameter-Efficient Fine-Tuning (LoRA / 4-Bit QLoRA)", "2021-06 (G1-L6 Hu LoRA Paper)", "2023-02 (G2-L4 PEFT LoRA)", "2023-05 (G2-L4 Single-GPU QLoRA)", "2024-05 (G3-L3 Managed Cloud Fine-Tune UI)", 35, "Open-Weight Base Models (Llama-2) & NF4 Quantization"),
        ("TRL_06", "Native Multimodal Vision-Audio-Text & Live UI Rendering", "2021-02 (G1-L6 CLIP/ViT Genesis)", "2023-09 (G2-L2 GPT-4V Preview)", "2024-05 (G3-L2 Multi-Doc Vision)", "2024-06 (G3-L1 GPT-4o & Claude Artifacts)", 40, "End-to-End Omni-Tokenization & Browser Sandboxing"),
        ("TRL_07", "Chain-of-Thought & RLVR Test-Time Reasoning", "2022-01 (G1-L6 Wei CoT Paper)", "2022-05 (G1-L4 Self-Consistency)", "2023-03 (G2-L2 Manual CoT Prompting)", "2025-01 (G4-L1 Auto-Router o1/R1/GPT-5)", 36, "Reinforcement Learning with Verifiable Rewards (G3-L6 RLVR)"),
        ("TRL_08", "Autonomous Multi-Site Web Research & Citation Synthesis", "2023-04 (G2-L6 WebGPT/Browsing RL)", "2023-05 (G2-L4 AutoGPT Brittle)", "2024-06 (G3-L4 LangGraph + Tavily)", "2025-02 (G4-L2 Built-In Deep Research)", 22, "Long-Horizon Browsing RL & Socratic Grounding"),
        ("TRL_09", "Standardized External Tool & Data Wiring (MCP)", "2023-06 (G2-L6 Toolformer/Functions)", "2023-11 (G2-L3 OpenAI Functions)", "2024-11 (G4-L3 Anthropic .mcp.json)", "2025-12 (G4-L1 AAIF MCP Apps in Chat)", 30, "Cross-Vendor Open Protocol Standardization (G3-L6 -> AAIF)"),
        ("TRL_10", "Autonomous Multi-File Repo Coding & Sandboxed Execution", "2021-07 (G1-L6 Codex/HumanEval)", "2024-03 (G3-L6 SWE-bench Harness)", "2024-06 (G3-L3 Cursor Vibe Coding)", "2025-02 (G4-L3/L4 Claude Code CLI & OpenClaw)", 43, "RLVR Coding Accuracy (>70% SWE-bench) & Decoupled Oracles"),
    ]
    df_trl = pd.DataFrame(trl_rows, columns=[
        "trl_id", "breakthrough", "trl_1_3_l6_genesis_date", "trl_4_5_proto_date_level",
        "trl_7_power_date_level", "trl_9_builtin_l1_date", "total_lag_months", "primary_bottleneck"
    ])
    trl_path = os.path.join(CACHE_DIR, "v4_trl_trajectories.csv")
    df_trl.to_csv(trl_path, index=False)
    print(f"[SAVED] {trl_path} | shape={df_trl.shape}")

    # 8. Table 1.1 & Table 3.1: Inductively Discovered Generations (Gen 0 to Gen 4)
    generations = [
        ("G0", "Gen 0: The Pre-LLM Code-Pipeline & Passive-Widget Generation", "2017-06", "2020-05", 36, 2017.42, 2020.42,
         "Single-GPU BERT fine-tuning (L4, ~600h); AutoML web consoles (L2, <50h); Self-attention & GLUE genesis (L6, ~10,000h)",
         "Baseline generation (active zero-shot generative L1 missing; passive widgets only at 0h)",
         "Tech: Transformer (2017-06) & BERT (2018-10); Money: Cloud GPU $2.50/hr; Eng: HuggingFace transformers & ONNX; TRL: Self-attention TRL 1-3 (L6) -> TRL 7; Culture: Code-first Data Science; Legal: GDPR (2018-05)",
         "Hand-crafted morphological lexicons & SIFT/HOG feature engineering replaced by pretrained BERT embeddings",
         12.0, 0.18, 1.1),
        ("G1", "Gen 1: The Completion Playground & Ghost-Text Autocomplete Generation", "2020-06", "2022-10", 29, 2020.42, 2022.83,
         "Few-shot completion prompting (L2, <50h); REST API wrappers (L3, <200h); DeepSpeed ZeRO sharding (L5, ~2,000h); Scaling laws & RLHF genesis (L6, ~10,000h)",
         "Custom NLP classification sank from G0-L3/L4 (<200h to ~600h BERT/sklearn) to G1-L2 (<50h Playground few-shot); boilerplate lookup sank to G1-L1 (0h Copilot Tab)",
         "Tech: GPT-3 175B ICL & Codex; Money: $60/1M tokens API; Eng: OpenAI Playground & VS Code Copilot; TRL: Few-shot TRL 1-3 (G0-L6) -> TRL 8; Culture: Prompting replaces dataset labeling; Legal: Copilot GPL debate",
         "Labeling 10,000 training rows & writing PyTorch training loops for basic sentiment/entity extraction became obsolete",
         45.0, 1.60, 3.8),
        ("G2", "Gen 2: The Conversational Chat, Manual Prompting & DIY Vector-RAG Generation", "2022-11", "2024-04", 18, 2022.83, 2024.33,
         "Prompt engineering, system personas & Custom GPTs (L2, <50h); Chunked Vector RAG bots (L3, <200h); Single-GPU 4-bit QLoRA (L4, ~600h); vLLM PagedAttention (L5, ~2,000h); Chinchilla/RoPE/DPO genesis (L6, ~10,000h)",
         "Conversational Q&A/drafting sank from G1-L2 (<50h Playground completion prefixes) to G2-L1 (0h ChatGPT web UI); custom weight tuning sank from G1-L5 (~2,000h DeepSpeed) to G2-L4 (~600h single-GPU QLoRA)",
         "Tech: RLHF chat (ChatGPT/GPT-4), ada-002 & Llama-2/QLoRA/vLLM; Money: $20/mo subscription & $2/1M GPT-3.5 API ($1.7B spend); Eng: Chat UI, LangChain/LlamaIndex & Pinecone; TRL: RLHF chat hit TRL 9 in 60d; Culture: 100M+ users; Legal: Samsung leak ban & Mata v. Avianca",
         "Completion prefix/stop-sequence hacks (Input:/Output:) & multi-GPU full-weight fine-tuning for domain style adaptation became obsolete",
         380.0, 28.00, 14.0),
        ("G3", "Gen 3: The Multimodal Workspace, Vibe Coding & Agentic Graph Generation", "2024-05", "2024-12", 8, 2024.33, 2025.00,
         "Vibe coding in AI IDEs (Cursor Composer) & guardrailed RAG bots (L3, <200h); Agentic orchestration (LangGraph, L4, ~600h); Containerized eval farms (L5, ~2,000h); RLVR/GRPO & MCP genesis (L6, ~10,000h)",
         "Multimodal creation & live UI preview sank from G2-L2/L3 to G3-L1 (0h GPT-4o & Claude Artifacts); 50-PDF Q&A sank from G2-L3 (<200h Vector RAG code) to G3-L2 (<50h drag-and-drop Projects/NotebookLM)",
         "Tech: Native omni-models (GPT-4o), Claude 3.5 Sonnet & 128k-2M context; Money: 90% prompt caching discount ($0.30/1M) & $11.5B-$13.8B spend; Eng: Artifacts/Projects, NotebookLM & Cursor Composer; TRL: Long-context & omni hit TRL 9; Culture: Vibe coding emerges; Legal: EU AI Act & RBAC/NeMo mandates",
         "Switching across separate websites/Discord for text vs image/vision, and writing custom Python vector-chunking scripts for 10-50 personal PDFs became obsolete",
         720.0, 240.00, 39.0),
        ("G4", "Gen 4: The Auto-Routed Reasoner, Deep Research, Terminal CLI & Sandbox Swarm Generation", "2025-01", "2026-10", 22, 2025.00, 2026.83,
         "MCP wiring & coupled CLI delegation (L3, <200h); Decoupled verification oracle & harness engineering (L4, ~600h); Air-gapped M4 Mac Mini OpenClaw swarms & GRPO RLVR (L5, ~2,000h); Continuous RLVR & SWE-bench Pro genesis (L6, ~10,000h)",
         "Chain-of-Thought reasoning sank from G2/G3-L2 (<50h manual CoT) to G4-L1 (0h auto-router); 50-site web synthesis sank from G3-L4 (~600h scraper graphs) to G4-L2 (<50h Deep Research); tool wiring & happy-path CLI coding sank to G4-L3 (<200h .mcp.json & CLI delegation)",
         "Tech: RLVR thinking models (o1/o3/R1/Claude 4.6-5.5/GPT-5.4), MCP & Computer Use; Money: $37.0B enterprise spend (76% bought vs 24% built; MIT NANDA 67% vs 33% success); Eng: Claude Code CLI, AAIF & OpenClaw; TRL: Reasoning & CLI agents hit TRL 8-9; Culture: SWE shifts from syntax typing to decoupled invariant specification; Legal: Apr 2026 OX Security 200k MCP stdio RCE disclosure enforcing isolated sandboxes",
         "Manual 'Let's think step by step' CoT prompt wrappers, hand-rolled per-app REST tool schemas, and line-by-line manual IDE syntax typing became obsolete",
         1150.0, 1100.00, 88.0),
    ]
    df_gens = pd.DataFrame(generations, columns=[
        "gen_id", "gen_folksonomy_name", "start_date", "end_date", "duration_months",
        "start_year_float", "end_year_float", "new_upper_use_cases",
        "sunk_builtin_use_cases", "causal_drivers_6factor", "obsolete_user_skills",
        "macro_users_millions", "macro_tokens_trillions", "macro_spend_billion_usd"
    ])
    gens_path = os.path.join(CACHE_DIR, "v4_generations.csv")
    df_gens.to_csv(gens_path, index=False)
    print(f"[SAVED] {gens_path} | shape={df_gens.shape}")

    # 9. Table 1.3 / Master Table 5.1c: Down-Ladder Skill Deflation Tracker (5 Benchmark Workflows across G0-G4 using Cumulative Beeline Hours)
    benchmarks = [
        ("math_reasoning", "Multi-Step Math & Logic Reasoning", 5, 2000, 4, 600, 2, 50, 2, 25, 1, 0, 2000, "RLVR test-time compute (G3-L6 -> G4-L1 o1/R1) & auto-routers absorbed manual CoT wrappers into built-in 0h L1 chat"),
        ("multimodal_creation", "Multimodal Text + Image + Live UI App Preview", 4, 600, 3, 200, 2, 50, 1, 0, 1, 0, 600, "Native omni-models (GPT-4o) & sandboxed browser rendering (Claude Artifacts/Canvas) unified tools into 0h L1"),
        ("doc_qa_50pdf", "Ask Questions Across 50 Private PDFs / Docs", 4, 600, 3, 200, 3, 150, 2, 30, 1, 0, 600, "128k-2M long context + 90% prompt caching + Projects/NotebookLM replaced custom Python vector-chunking code"),
        ("web_research_synthesis", "Multi-Website Cited Research Report (50+ Sources)", 5, 2000, 4, 600, 4, 500, 3, 180, 2, 20, 1980, "End-to-end RL browsing agents (OpenAI/Gemini Deep Research) + Socratic elicitation productized multi-hop synthesis into L2 (<50h)"),
        ("text_classification", "Custom Business Text Classifier / Entity Extractor", 3, 200, 2, 40, 1, 0, 1, 0, 1, 0, 200, "In-context learning (Gen 1) & RLHF instruction following (Gen 2) eliminated supervised training loops"),
    ]
    df_bench = pd.DataFrame(benchmarks, columns=[
        "workflow_key", "workflow_name", "G0_level", "G0_hours", "G1_level", "G1_hours",
        "G2_level", "G2_hours", "G3_level", "G3_hours", "G4_level", "G4_hours",
        "total_hours_saved", "tech_mechanism"
    ])
    bench_path = os.path.join(CACHE_DIR, "v4_skill_deflation_benchmarks.csv")
    df_bench.to_csv(bench_path, index=False)
    print(f"[SAVED] {bench_path} | shape={df_bench.shape}")

    # 10. Tables 4.1 to 4.5 & Master Table 5.1a: All 30 Empirical (Gen G, Level L) Cells (G0-L1 through G4-L6)
    cells = [
        # =====================================================================
        # GEN 0 (2017-06 to 2020-05)
        # =====================================================================
        ("G0", 1, "Passive-Widgets-Only (Active GenAI Missing)", 0, 0, LEVEL_BRACKET_STRS[1], COMPACT_TICK_LABELS[1],
         25, 1.5e8, 0.00001, 0.0002, 0.1, 0.01, 71.8, 14.0, 4.0,
         "Passive NLP Tools: Autocorrect, Spam Filters & Smart Compose Widgets",
         "Browser / Mobile App (Google Translate, Grammarly, Gmail Smart Compose)",
         "autocorrect, spam filters, search ranking, Gmail Smart Compose (0h beeline)",
         "N/A (Floor of the 6-level grid at 0h | $0; active conversational bootstrapping fails 100% because no general-purpose LLM existed in G0)",
         "Opening Cloud AutoML consoles (G0-L2, <50h | <$30) for routine email typo fixes wastes days of CSV setup when passive browser widgets run inline at 0h",
         "Pre-2017 phrase-based statistical MT had 50%+ higher syntax error rates prior to GNMT and Transformer encoder rollouts",
         "In G1-G2, active zero-shot completion/chat boxes (Copilot Tab, ChatGPT) supersede passive-only underlines at L1 via Dual Sinking"),

        ("G0", 2, "Populated", 50, 30, LEVEL_BRACKET_STRS[2], COMPACT_TICK_LABELS[2],
         150, 1.2e9, 0.0005, 0.002, 15.0, 0.5, 14.0, 12.0, 8.0,
         "Rules & AutoML: No-Code Cloud AutoML Consoles & Regex Intent Trees",
         "Cloud Web Console (Google AutoML, AWS Comprehend, Dialogflow) & Spreadsheet Regex",
         "AutoML tables, regex intent rules, CSV upload, precision-recall threshold (TUT_01)",
         "Meta-Bootstrapping Gate: A G0-L1 user cannot ask Gmail Smart Compose by name to build a ticket classifier or elicit regex rules because G0 lacked conversational LLMs",
         "Recursive Cannibalization: Writing custom Python scikit-learn scripts (G0-L3, <200h | <$100) is unnecessary when Cloud AutoML GUI search over a 500-row CSV hits 85% accuracy",
         "Pre-2017 required manual Java/C++ rule engines with zero automated neural architecture search",
         "In G1-L2, few-shot prompting in OpenAI Playground replaces labeled CSV uploads without training waits; in G2-L1, zero-shot chat absorbs basic classification"),

        ("G0", 3, "Populated", 200, 100, LEVEL_BRACKET_STRS[3], COMPACT_TICK_LABELS[3],
         600, 1.8e10, 0.003, 0.015, 45.0, 2.0, 9.5, 25.0, 20.0,
         "Statistical Classifiers: Classical Python NLP & Tabular XGBoost Pipelines",
         "Jupyter Notebook + scikit-learn / XGBoost / spaCy (Applied SWE / Data Analyst)",
         "TF-IDF matrices, boosted trees (XGBoost), n-gram tokenizer, spaCy NER, k-fold CV (TUT_02)",
         "Meta-Bootstrapping Gate: G0-L2 Cloud AutoML GUI lacks custom multi-table feature joins, domain-specific spaCy dependency rules, and out-of-fold leakage prevention (dropping F1 by >20 pts)",
         "Recursive Cannibalization: Fine-tuning BERT on a GPU (G0-L4, ~600h | ~$1.5k) wastes GPU budget when CPU TF-IDF + XGBoost + spaCy v2 converges in 10 seconds on structured/short-text tabular data",
         "Earlier feature pipelines lacked spaCy v2 neural transition parsers and fast histogram-binned gradient boosting",
         "In G1-G2, unstructured text extraction sinks via Dual Sinking into G1-L2 few-shot prompts and G2-L1 zero-shot chat"),

        ("G0", 4, "Populated", 600, 1500, LEVEL_BRACKET_STRS[4], COMPACT_TICK_LABELS[4],
         2000, 4.4e11, 0.025, 0.120, 120.0, 15.0, 3.8, 26.0, 26.0,
         "Fine-Tuned Encoders: Single-GPU Pretrained BERT/RoBERTa & Decoupled Validation",
         "PyTorch + HuggingFace transformers on Single GPU (16GB V100/T4/1080Ti, Applied MLE)",
         "pretrained encoders (BERT/RoBERTa), fine-tuning, AdamW warmup, decoupled OOD validation sets (TUT_03)",
         "Meta-Bootstrapping & Oracle Gate: G0-L3 bag-of-words TF-IDF cannot resolve polysemous word-order semantics (15-25 pt F1 drop on SQuAD 2.0), and lacks formal cross-entropy loss/warmup calibration against out-of-distribution (OOD) test splits",
         "Recursive Cannibalization: Consuming HuggingFace pretrained checkpoints on 1 GPU (~$1.5k) makes multi-GPU custom seq2seq pretraining (G0-L5, ~2,000h | ~$500k) redundant for task classification/NER",
         "Pre-2018 BiLSTMs lacked bidirectional self-attention transfer and required bespoke per-task architectures",
         "In G1, general sentiment/NER sinks to G1-L2 (<50h) few-shot prompting; in G2, single-GPU weight adaptation upgrades to 4-bit QLoRA on 7B-70B LLMs"),

        ("G0", 5, "Populated", 2000, 500000, LEVEL_BRACKET_STRS[5], COMPACT_TICK_LABELS[5],
         8000, 6.4e12, 0.180, 0.850, 240.0, 60.0, 0.7, 13.0, 20.0,
         "Custom Seq2Seq Weights: Multi-GPU Fairseq Training & Quantized ONNX Serving",
         "8-64x V100 DGX Cluster (~$500k) + Fairseq / Tensor2Tensor + C++ ONNX Runtime / TensorRT",
         "seq2seq layers, multi-GPU sharding (Horovod/DDP), FP16/INT8 ONNX graph quantization, beam search (TUT_04)",
         "Meta-Bootstrapping & Infra Gate: G0-L4 single-GPU PyTorch notebooks crash with CUDA OOM on 1.5B seq2seq models and violate >500ms SLA at 10,000 QPS without C++ INT8 ONNX kernel fusion",
         "Why Not Higher at L6?: G0-L5 Distributed MLEs consume existing Transformer/BERT architectures and public corpora on an 8-64 GPU cluster (~$500k) rather than inventing self-attention math from scratch, curating 300B-token WebText/CommonCrawl pipelines, designing GLUE/SuperGLUE benchmarks, or funding $4.6M-$100M+ frontier GPT-3 genesis runs (G0-L6)",
         "Pre-2017 RNN seq2seq suffered vanishing gradients and O(T) sequential training bottlenecks across GPUs",
         "In G1-G2, managed Foundation Model APIs eliminate custom seq2seq training for 99% of teams, while L5 upgrades to DeepSpeed ZeRO-3 (G1) and vLLM PagedAttention (G2)"),

        ("G0", 6, "Populated (TRL 1-3 Genesis)", 10000, 100000000, LEVEL_BRACKET_STRS[6], COMPACT_TICK_LABELS[6],
         50000, 1.2e14, 2.500, 14.000, 600.0, 360.0, 0.2, 10.0, 22.0,
         "Transformer & Pretraining Genesis: Self-Attention Math, CommonCrawl, GLUE & GPT-3",
         "TPU v2/v3 Pods & 1,000+ V100 Superclusters ($4.6M-$100M+ Lab Budget, AI Research Scientist)",
         "self-attention math, Masked Language Modeling, CommonCrawl dedup, GLUE/SuperGLUE, GPT-3 genesis (TUT_05)",
         "Meta-Bootstrapping & Theory Gate (Why Not L5?): An L5 engineering cluster (~$500k) optimizing existing Fairseq/ONNX graphs cannot invent the scaled dot-product self-attention equation Softmax(QK^T/sqrt(d_k))V, formulate Masked Language Modeling (BERT) or sparse MoE routing, build petabyte-scale CommonCrawl MinHash deduplication pipelines, design canonical GLUE/SuperGLUE/SQuAD 2.0 evaluation metrics, or execute the from-scratch GPT-3 175B pretraining run that birthed Gen 1",
         "Ceiling of the 6-Level Grid: G0-L6 (~10,000h Focused PhD | ~$100M+) is the apex on-ladder TRL 1-3 generator; researchers recursively use G0-L3/L4 Python/PyTorch automation to run ablations",
         "Prior to June 2017, recurrence and convolutions blocked parallel sequence scaling beyond a few hundred million tokens",
         "Dual Sinking in G1: G0-L6's pretrained checkpoints and GPT-3 175B API sink directly into G1-L1 (Copilot Tab), G1-L2 (Playground few-shot), and G1-L4 (HuggingFace AutoModel)"),

        # =====================================================================
        # GEN 1 (2020-06 to 2022-10)
        # =====================================================================
        ("G1", 1, "Populated", 0, 0, LEVEL_BRACKET_STRS[1], COMPACT_TICK_LABELS[1],
         60, 1.4e10, 0.0005, 0.004, 0.2, 0.02, 51.8, 11.0, 6.0,
         "Ghost-Text Autocomplete: One-Key IDE Tab Completion & Viral Web Demos",
         "VS Code (GitHub Copilot Tab) & Viral Web Boxes (Craiyon / AI Dungeon, Casual User)",
         "ghost-text, Tab-to-accept plugins, Craiyon prompt box (0h beeline)",
         "N/A (Floor of the 6-level grid at 0h | $0; zero study or configuration required)",
         "Recursive Cannibalization: Opening OpenAI Playground (G1-L2, <50h | <$30) to manually tune temperature and stop tokens for single-line boilerplate wastes 5 minutes when Copilot Tab streams inline at 0h",
         "In G0, boilerplate synthesis required G0-L3 (<200h) manual documentation search and syntax adaptation",
         "In G2, RLHF ChatGPT expands L1 from inline single-line ghost-text and toy web boxes to full multi-turn conversational Q&A"),

        ("G1", 2, "Populated", 50, 30, LEVEL_BRACKET_STRS[2], COMPACT_TICK_LABELS[2],
         650, 2.3e11, 0.039, 0.045, 8.0, 0.15, 28.0, 22.0, 18.0,
         "Few-Shot Prompting: Completion Prefixes & Stop-Sequence Sliders in Playground",
         "OpenAI Web Playground / Jasper & Copy.ai Templates (Domain Power-User)",
         "few-shot prompts, stop tokens, Input:/Output: prefixes, temperature slider (TUT_06)",
         "Meta-Bootstrapping Gate: Typing a conversational question or asking 'interview me to build a classifier' into raw G1 GPT-3 davinci at L1 (0h) fails completely—without L2 Input:/Output: exemplars and stop=['\\n'], raw completion models simply hallucinate more questions",
         "Recursive Cannibalization: Writing Python REST SDK wrappers (G1-L3, <200h | <$100) is overkill when interactive Playground presets solve batch copywriting and ad-hoc classification in 10 minutes",
         "In G0, custom text classification required G0-L3/L4 (<200h to ~600h) scikit-learn or single-GPU BERT fine-tuning on labeled datasets",
         "Dual Sinking in G2: RLHF instruction tuning (G1-L6 -> G2-L1 ChatGPT) makes Input:/Output: prefixes and stop sequences obsolete, sinking conversational Q&A to G2-L1 (0h)"),

        ("G1", 3, "Populated", 200, 100, LEVEL_BRACKET_STRS[3], COMPACT_TICK_LABELS[3],
         1800, 6.3e11, 0.108, 0.120, 25.0, 0.5, 13.5, 26.0, 24.0,
         "API Wrapper Calls: REST Completion SDKs & Dense FAISS Vector Search",
         "Python/Node.js REST SDK + OpenAI /v1/completions & /v1/embeddings + FAISS (Applied SWE)",
         "completion APIs, vector search, FAISS cosine similarity, token truncation, backoff (TUT_07)",
         "Meta-Bootstrapping Gate: A G1-L2 Playground user cannot conversationally bootstrap a multi-document semantic search backend because G1 completion models (2,049-token limit) had zero tool execution, zero repo access, and truncated anything beyond 3 pages",
         "Recursive Cannibalization: Consuming G1-L2 few-shot prompt templates inside a lightweight Python FAISS wrapper (<200h | <$100) avoids G1-L4 (~600h) multi-step chain calibration or JSONL weight fine-tuning for simple lookup",
         "In G0, semantic document search required G0-L4 (~600h | ~$1.5k) custom BERT encoder training + Elasticsearch infrastructure",
         "In G2-G3, basic document Q&A standardizes into G2-L3 Vector RAG and then sinks into G3-L2 (<50h) drag-and-drop 1M-2M long-context workspaces"),

        ("G1", 4, "Populated", 600, 1500, LEVEL_BRACKET_STRS[4], COMPACT_TICK_LABELS[4],
         4500, 1.6e12, 0.270, 0.310, 60.0, 3.0, 5.2, 19.0, 18.0,
         "Linear Prompt Chains: Self-Consistency Voting, Cloud Fine-Tune CLI & Decoupled Evals",
         "Python Async Orchestration + OpenAI Fine-Tune CLI + Decoupled Calibration Suite (Senior SWE / MLE)",
         "prompt chaining, JSONL tuning, self-consistency pass@20 voting, decoupled validation loss (TUT_08)",
         "Meta-Bootstrapping & Oracle Gate: Coupled G1-L3 single-call API wrappers score <18% on GSM8K math and suffer compounding hallucination drift across steps; requires L4 formal decomposition, pass@20 majority-vote variance reduction, and decoupled held-out JSONL evaluation oracles",
         "Recursive Cannibalization: Leveraging managed cloud fine-tune CLIs and G1-L3 API primitives (~$1.5k budget) makes provisioning multi-node DeepSpeed clusters (G1-L5, ~2,000h | ~$500k) unnecessary for adapting 6B-13B task behavior",
         "In G0, multi-step natural-language math/logic reasoning was unachievable even on G0-L5 clusters",
         "Dual Sinking in G2-G4: CoT reasoning sinks first to G2-L2 (<50h) manual prompting and then to G4-L1 (0h) built-in RLVR auto-routers"),

        ("G1", 5, "Populated", 2000, 500000, LEVEL_BRACKET_STRS[5], COMPACT_TICK_LABELS[5],
         15000, 9.0e12, 0.900, 1.400, 180.0, 45.0, 1.3, 12.0, 14.0,
         "Distributed Trainers: Multi-Node DeepSpeed ZeRO-3 & Tensor-Parallel Sharding",
         "8-64x NVIDIA A100 Cluster (~$500k) + DeepSpeed ZeRO-3 + Megatron-LM (Distributed Systems MLE)",
         "tensor parallelism, GPU sharding, DeepSpeed ZeRO-3, BF16 mixed precision, NCCL (TUT_09)",
         "Meta-Bootstrapping & Infra Gate: Forcing on-prem full-weight adaptation of 6B-20B models (GPT-NeoX-20B, Flan-T5-XXL) onto G1-L4 single-GPU or cloud CLI fails immediately with CUDA Out-Of-Memory (>80GB VRAM required for FP32 optimizer states)",
         "Why Not Higher at L6?: G1-L5 Distributed MLEs shard and fine-tune existing open-weight checkpoints on 8-64 A100s (~$500k) rather than deriving neural scaling laws L(N,D,C), formulating RLHF PPO reward objectives, curating 825GB The Pile / GitHub corpora, inventing HumanEval pass@k metrics, or executing $10M-$100M+ from-scratch GPT-3.5/GPT-4/Chinchilla base pretraining runs (G1-L6)",
         "In G0, 110M-340M BERT models fit on 1 GPU; G1's 6B-66B models shattered single-GPU memory ceilings, requiring ZeRO-3 state partitioning",
         "Dual Sinking in G2: Dettmers' 4-bit NF4 QLoRA (G2-L4) sinks 7B-70B custom weight adaptation from L5 multi-node clusters down to a single ~$1.5k GPU"),

        ("G1", 6, "Populated (TRL 1-3 Genesis)", 10000, 100000000, LEVEL_BRACKET_STRS[6], COMPACT_TICK_LABELS[6],
         120000, 8.5e14, 6.500, 38.000, 720.0, 480.0, 0.2, 10.0, 20.0,
         "Scaling Laws & RLHF Genesis: PPO Alignment, The Pile, HumanEval & ChatGPT/GPT-4 Birth",
         "1,024-10,000x A100 Supercluster ($10M-$100M+ Frontier Lab Budget, AI Research Scientist)",
         "scaling laws, RLHF PPO, The Pile curation, HumanEval pass@k, InstructGPT/GPT-4 genesis (TUT_10)",
         "Meta-Bootstrapping & Theory Gate (Why Not L5?): An L5 DeepSpeed cluster team (~$500k) cannot conversationally prompt GPT-3 or use standard sharding scripts to discover Kaplan/Chinchilla power-law scaling exponents, formulate Ouyang et al.'s 3-stage SFT + Bradley-Terry Reward Model + KL-penalized PPO RLHF alignment, curate deduplicated code/pile datasets with human contractor preference trees, invent the unbiased pass@k functional coding metric (HumanEval/GSM8K/MMLU), or fund the $100M-class GPT-4 / InstructGPT base runs",
         "Ceiling of the 6-Level Grid: G1-L6 (~10,000h | ~$100M+) is the on-ladder TRL 1-3 origin of Gen 2; scientists recursively use G1-L1 Copilot and G1-L3/L4 Python harnesses to accelerate experiment code",
         "In G0-L6, models were unaligned next-token predictors lacking RLHF preference alignment and execution-based coding benchmarks",
         "Dual Sinking in G2: G1-L6's RLHF alignment births G2-L1 ChatGPT (sinking conversational Q&A to 0h for 100M+ users), while LoRA theory (Hu et al. 2021) sinks weight tuning to G2-L4"),

        # =====================================================================
        # GEN 2 (2022-11 to 2024-04)
        # =====================================================================
        ("G2", 1, "Populated", 0, 0, LEVEL_BRACKET_STRS[1], COMPACT_TICK_LABELS[1],
         800, 2.8e11, 0.002, 0.035, 1.5, 0.1, 67.9, 20.0, 14.0,
         "Consumer Chatbots: Zero-Shot Browser Q&A, Summarization & Multi-Turn Drafting",
         "Browser / Mobile App (ChatGPT Free, Bing Chat, Claude.ai, Casual User)",
         "zero-shot chat, multi-turn dialog, conversational follow-up (0h beeline)",
         "N/A (Floor of the 6-level grid at 0h | $0; 100M+ high schoolers and consumers operate zero-shot with zero study)",
         "Recursive Cannibalization: Spending <50h learning G2-L2 prompt frameworks for a routine email rewrite or recipe summary adds zero value when zero-shot RLHF chat succeeds on turn 1",
         "In G1, getting conversational answers required G1-L2 (<50h | <$30) Playground completion prefixes and stop=['\\n'] configuration",
         "In G3, L1 expands from text-only chat to built-in native multimodal (voice/vision/image) and live interactive UI Artifacts"),

        ("G2", 2, "Populated", 50, 30, LEVEL_BRACKET_STRS[2], COMPACT_TICK_LABELS[2],
         2500, 1.8e12, 0.045, 0.180, 6.0, 0.4, 19.0, 23.0, 20.0,
         "Prompt Engineering: System Personas, Step-by-Step CoT, Custom GPTs & Image Flags",
         "ChatGPT Plus ($20/mo, GPT-4 + Custom GPTs) & Midjourney Discord (Workspace Analyst)",
         "system personas, step prompts (CoT), XML delimiters, Custom GPTs, --ar 16:9 flags (TUT_11)",
         "Meta-Bootstrapping Gate: Zero-shot G2-L1 (gpt-3.5-turbo) without L2 structured system personas, XML context delimiters, or explicit 'Let's think step by step' CoT triggers hallucinates legal citations (Mata v. Avianca) and fails multi-constraint logic; even if asked to elicit constraints, 4k-8k context loses state across turns",
         "Recursive Cannibalization: Using G2-L2 Custom GPTs with 3 uploaded reference PDFs (<50h | <$30) makes coding a Python LangChain script (G2-L3, <200h | <$100) unnecessary for small personal workflows",
         "In G1, Chain-of-Thought required G1-L4 (~600h) Python self-consistency wrappers, and image generation required G1-L3 Colab notebooks",
         "Dual Sinking in G3-G4: Separate Discord image flags sink into G3-L1 omni-chat, while manual step-by-step CoT prompting sinks into G4-L1 (0h) auto-routed RLVR reasoners"),

        ("G2", 3, "Populated", 200, 100, LEVEL_BRACKET_STRS[3], COMPACT_TICK_LABELS[3],
         8500, 6.1e12, 0.170, 0.620, 20.0, 1.2, 8.5, 24.0, 22.0,
         "Chunked Vector RAG: Document Vector Databases & JSON Function-Calling Bots",
         "Python SDK (LangChain / LlamaIndex) + Pinecone/Chroma + OpenAI Functions (Applied SWE)",
         "vector databases (RAG), function calling, RecursiveCharacterTextSplitter, HNSW top-k (TUT_12)",
         "Meta-Bootstrapping Gate: Asking G2-L2 ChatGPT by name to 'search our 500-page company wiki and call our internal Jira API' fails immediately with context_length_exceeded (8k token limit truncates 95% of the wiki) and zero private network/database execution primitives",
         "Recursive Cannibalization: Leveraging G2-L2 system prompts + G2-L3 top-k vector retrieval (<200h | <$100) grounds volatile company facts dynamically, whereas fine-tuning weights at G2-L4 (~600h | ~$1.5k) hallucinates policy numbers and requires retraining on every wiki edit",
         "In G0-G1, internal document Q&A required G0-L4 (~600h) custom BERT extractive QA + Elasticsearch engineering",
         "Dual Sinking in G3-G4: Personal/team 50-PDF RAG sinks into G3-L2 (<50h) 1M-2M drag-and-drop workspaces, while custom JSON function schemas standardize into G4-L3 .mcp.json servers"),

        ("G2", 4, "Populated", 600, 1500, LEVEL_BRACKET_STRS[4], COMPACT_TICK_LABELS[4],
         25000, 1.8e13, 0.450, 1.800, 45.0, 8.0, 3.6, 15.0, 15.0,
         "LoRA Adapter Tuning: Single-GPU 4-Bit QLoRA, ReAct Loops & Decoupled Evals",
         "Single RTX 4090 / A100 (~$1.5k) + HuggingFace PEFT / bitsandbytes / TRL (Senior SWE / Single-GPU MLE)",
         "4-bit quantization (NF4), LoRA adapters, SFTTrainer, ReAct loops, LLM-as-a-Judge oracles (TUT_13)",
         "Meta-Bootstrapping & Oracle Gate: Coupled G2-L3 RAG/prompting cannot compress latency below 100ms for 30M users (Grammarly CoEdIT) or prevent unconstrained ReAct loops (AutoGPT 0.90^20 = 12.2% survival) from spiraling; requires L4 formal NF4 rank/alpha calibration and decoupled LLM-as-a-Judge / held-out test harnesses",
         "Recursive Cannibalization: Consuming G2-L3 synthetic data generation + 4-bit QLoRA on a single ~$1.5k GPU tunes Llama-2-13B/70B in 8 hours, eliminating the $50,000+ multi-node DeepSpeed cluster overhead of G1-L5/G2-L5",
         "In G1, adapting a 13B-20B open model required G1-L5 (~2,000h | ~$500k) multi-node DeepSpeed ZeRO-3 clusters",
         "Dual Sinking in G3-G4: 90% prompt caching & cheap flash models replace QLoRA for many style tasks, while brittle ReAct loops upgrade to G3-L4 cyclic StateGraphs and G4-L4 decoupled CLI harnesses"),

        ("G2", 5, "Populated", 2000, 500000, LEVEL_BRACKET_STRS[5], COMPACT_TICK_LABELS[5],
         80000, 7.2e13, 1.600, 6.500, 120.0, 30.0, 0.9, 10.0, 11.0,
         "High-Throughput Serving Infra: vLLM PagedAttention, Continuous Batching & FlashAttention-2",
         "8-64x NVIDIA H100/A100 Cluster (~$500k) + vLLM / TGI / TensorRT-LLM (Staff Infra SWE / Distributed MLE)",
         "paged KV-cache (vLLM), flash attention, continuous batching, tensor parallelism (TUT_14)",
         "Meta-Bootstrapping & Infra Gate: Serving 5,000+ concurrent enterprise users on G2-L4 naive HuggingFace generate() scripts fails with 60-80% KV-cache VRAM fragmentation, OOM crashes, and 10x higher GPU cost; conversational prompting cannot rewrite CUDA SRAM tiling or virtual-memory page tables",
         "Why Not Higher at L6?: G2-L5 Staff Infra SWEs/MLEs deploy and optimize open-weight models (Llama-2-70B, Mixtral-8x7B) on 8-64 GPUs (~$500k) using vLLM/FlashAttention-2 rather than deriving Chinchilla/RoPE/DPO mathematical theory, filtering 15T-token Dolma/FineWeb web corpora, designing Chatbot Arena Elo benchmarks, or funding $50M-$100M+ from-scratch Llama-3 / GPT-4o / Claude 3 base pretraining runs (G2-L6)",
         "In G1, open-source serving lacked PagedAttention and FlashAttention-2, bottlenecking throughput on memory bandwidth",
         "In G3-G4, vLLM becomes the standard inference engine inside containerized multi-agent eval farms (G3-L5) and distributed GRPO RLVR rollout workers (G4-L5)"),

        ("G2", 6, "Populated (TRL 1-3 Genesis)", 10000, 100000000, LEVEL_BRACKET_STRS[6], COMPACT_TICK_LABELS[6],
         450000, 4.5e15, 14.000, 95.000, 780.0, 600.0, 0.1, 8.0, 18.0,
         "Long-Context, DPO & Omni Genesis: Chinchilla/RoPE Math, FineWeb, Arena Elo & Llama-3/GPT-4o Birth",
         "10,000-25,000x H100 Frontier Supercluster ($50M-$100M+ Lab Budget, AI Research Scientist)",
         "Chinchilla scaling, RoPE long-context, DPO math, Dolma/FineWeb curation, Chatbot Arena Elo (TUT_15)",
         "Meta-Bootstrapping & Theory Gate (Why Not L5?): An L5 vLLM serving team (~$500k) cannot prompt GPT-4 to derive closed-form Direct Preference Optimization (DPO, eliminating separate reward models), formulate RoPE base-frequency scaling and Ring Attention for 128k-2M context windows, curate 15-trillion-token classifier-filtered pretraining corpora (Dolma/FineWeb/DataComp), invent Bradley-Terry crowdsourced Elo ranking (Chatbot Arena / MT-Bench), or execute $100M+ native omni-modal (GPT-4o) and Llama-3-405B base pretraining runs",
         "Ceiling of the 6-Level Grid: G2-L6 (~10,000h | ~$100M+) is the on-ladder TRL 1-3 origin of Gen 3; scientists recursively consume G2-L4/L5 LLM-as-a-Judge and vLLM fast inference to filter pretraining data",
         "In G1-L6, models were capped at 2k-4k context, trained with unstable PPO reward models, and under-trained relative to Chinchilla token-per-parameter optima",
         "Dual Sinking in G3: G2-L6's 128k-2M RoPE context and native omni-tokenization sink directly into G3-L1 (0h GPT-4o / Artifacts) and G3-L2 (<50h 50-PDF Projects/NotebookLM, killing small-corpus Vector RAG)"),

        # =====================================================================
        # GEN 3 (2024-05 to 2024-12)
        # =====================================================================
        ("G3", 1, "Populated", 0, 0, LEVEL_BRACKET_STRS[1], COMPACT_TICK_LABELS[1],
         2200, 8.8e11, 0.004, 0.065, 1.2, 0.15, 63.9, 16.0, 12.0,
         "Multimodal Omni-Chat: Real-Time Voice/Camera Chat & Live UI Artifacts",
         "Default Web/Mobile App (GPT-4o, Claude 3.5 Sonnet with Live Artifacts, Casual User)",
         "voice-video chat, live UI canvas, Claude Artifacts, ChatGPT Canvas (0h beeline)",
         "N/A (Floor of the 6-level grid at 0h | $0; speaking by voice, showing a camera feed, or clicking a live React Artifact requires 0h study)",
         "Recursive Cannibalization: Switching to separate Discord image bots or setting up local Node.js boilerplate (G3-L2/L3) for a single-file interactive calculator or chart wastes 30+ minutes when Claude Artifacts renders it inline at 0h",
         "In G2, generating images alongside text or previewing interactive UI required G2-L2/L3 (Midjourney Discord flags or local React setup)",
         "In G4, L1 absorbs silent RLVR step-by-step reasoning via auto-routers and interactive in-chat MCP App widgets"),

        ("G3", 2, "Populated", 50, 30, LEVEL_BRACKET_STRS[2], COMPACT_TICK_LABELS[2],
         35000, 1.4e13, 0.035, 0.450, 5.0, 0.8, 20.0, 22.0, 18.0,
         "Long-Context Projects: Drag-and-Drop 50-PDF Workspaces & Socratic Elicitation",
         "Multimodal Project Workspace (Claude Projects 200k, Google NotebookLM 1M-2M, Workspace Analyst)",
         "million-token context, project folders, Socratic prompt elicitation, Audio Overviews (TUT_16)",
         "Meta-Bootstrapping Gate: Dropping 50 PDFs (400,000 tokens) into a stateless G3-L1 single chat turn fails—loses persistent workspace instructions across sessions, lacks cross-document citation tables, and omits Socratic workspace curation",
         "Recursive Cannibalization: Consuming 200k-2M native context + 90% prompt caching inside a drag-and-drop Project folder (<50h | <$30) makes writing a custom Python LangChain + Pinecone vector-chunking pipeline (G2-L3/G3-L3, <200h | <$100) completely redundant for <500-page team binders",
         "In G2, querying 50 PDFs forced users up to G2-L3 (<200h) to code a chunked Vector DB RAG pipeline due to 4k-8k context limits",
         "Dual Sinking in G4: Static uploaded PDFs expand at G4-L2 into autonomous 50-to-100 website live multi-hop browsing via built-in Deep Research"),

        ("G3", 3, "Populated", 200, 100, LEVEL_BRACKET_STRS[3], COMPACT_TICK_LABELS[3],
         65000, 3.9e13, 0.140, 1.100, 12.0, 2.5, 10.5, 26.0, 25.0,
         "Vibe Coding & Guardrailed RAG: Multi-File AI IDE Composer & Enterprise RBAC Bots",
         "Cursor IDE (Composer + .cursorrules) & Enterprise Hybrid RAG + NeMo Guardrails (Applied SWE)",
         "vibe coding, multi-file IDE diffs, repo indexing, hybrid guardrailed RAG, RBAC (TUT_17)",
         "Meta-Bootstrapping & Coupled-Execution Gate: A G3-L2 browser workspace has zero local git/filesystem write access and zero SharePoint ACL/RBAC enforcement; conversely, G3-L3 Vibe Coding (Cursor Composer) sits at L3 (<200h | <$100) rather than L4 because the AI both writes and self-checks on the coupled happy path while the human steers via declarative pattern literacy (.cursorrules, @codebase)",
         "Recursive Cannibalization: Using Cursor Composer multi-file diffs + 90% prompt caching (<200h | <$100) ships standard CRUD apps and departmental RBAC bots without needing G3-L4 (~600h) cyclic LangGraph state machines or custom DPO weight tuning",
         "In G2, developers had to copy-paste single files between browser ChatGPT and VS Code, and early RAG bots lacked prompt caching and Colang dialog rails",
         "Dual Sinking in G4: Proprietary tool connectors standardize into .mcp.json (G4-L3), while happy-path vibe coding advances to terminal CLI delegation (G4-L3) and decoupled oracle harness engineering (G4-L4)"),

        ("G3", 4, "Populated", 600, 1500, LEVEL_BRACKET_STRS[4], COMPACT_TICK_LABELS[4],
         180000, 1.1e14, 0.480, 3.200, 25.0, 12.0, 4.3, 17.0, 17.0,
         "State-Machine Graphs: Agentic Orchestration (LangGraph), Decoupled Oracles & DPO",
         "Python LangGraph SDK + Postgres Checkpointer + Decoupled Eval Oracles + Single-GPU DPO (Senior SWE / MLE)",
         "agentic orchestration, cyclic state graphs (LangGraph), checkpoints, decoupled oracles, DPO (TUT_18)",
         "Meta-Bootstrapping & Failure-Boundary Gate: When a G3-L3 Vibe Coding user asks Cursor Composer by name to 'build a self-healing multi-agent workflow' or 'fix this complex state bug', coupled L3 execution enters infinite regression loops because the agent shares blind spots across code and self-test; G3-L4 (~600h | ~$1.5k) requires formal cyclic state-transition specification, Postgres checkpoint rollback, and decoupled verification oracles",
         "Recursive Cannibalization: Consuming G3-L3 IDE/prompt-caching primitives inside a single-node LangGraph + Postgres harness (~$1.5k) avoids provisioning 64-GPU Kubernetes evaluation clusters (G3-L5, ~2,000h | ~$500k) for departmental workflows",
         "In G2, autonomous loops (AutoGPT) lacked explicit cyclic state-graph boundaries and persistent checkpoints, failing 85%+ of multi-step runs",
         "Dual Sinking in G4: Multi-hop web research graphs sink into G4-L2 (<50h) built-in Deep Research, while coding state graphs move into G4-L4 terminal CLI harnesses (Claude Code + CLAUDE.md)"),

        ("G3", 5, "Populated", 2000, 500000, LEVEL_BRACKET_STRS[5], COMPACT_TICK_LABELS[5],
         550000, 4.4e14, 1.850, 11.000, 60.0, 45.0, 1.2, 11.0, 11.0,
         "Evaluator Harnesses: Containerized Multi-Agent Eval Farms & vLLM Serving Clusters",
         "Kubernetes Docker-in-Docker Eval Farm + 8-64x H100 vLLM/DPO Cluster (~$500k, Staff Infra SWE / MLE)",
         "container eval farms, verifiers, orchestrator-workers, pass@k execution grading (TUT_19)",
         "Meta-Bootstrapping & Infra Gate: Running 500 parallel repository test suites or synthetic trajectory replay loops on a G3-L4 single workstation (~$1.5k) deadlocks local Docker I/O and takes weeks; requires L5 distributed container orchestration, isolated network namespaces, and multi-node vLLM batching",
         "Why Not Higher at L6?: G3-L5 Staff Infra SWEs/MLEs build containerized evaluation and post-training pipelines over existing frontier/open checkpoints (~$500k) rather than formulating test-time compute scaling laws and critic-free GRPO math, generating million-trajectory formal RLVR reasoning datasets, inventing SWE-bench Verified / OSWorld / GPQA Diamond benchmarks and the MCP specification, or funding $100M+ DeepSeek-V3/R1 and OpenAI o1/o3 base/RLVR runs (G3-L6)",
         "In G2, multi-agent coding demos (MetaGPT/ChatDev) ran in toy sandboxes without real containerized GitHub repo test-suite verification",
         "In G4, single-repo Docker TDD loops sink into G4-L4 (~600h) local CLI harnesses, while L5 advances to air-gapped M4 Mac Mini OpenClaw swarms and multi-GPU GRPO RLVR training"),

        ("G3", 6, "Populated (TRL 1-3 Genesis)", 10000, 100000000, LEVEL_BRACKET_STRS[6], COMPACT_TICK_LABELS[6],
         1500000, 1.4e16, 38.000, 240.000, 840.0, 720.0, 0.1, 8.0, 17.0,
         "RLVR & Protocol Genesis: GRPO Math, Verified Reasoning Corpora, SWE-bench/OSWorld & o1/R1/MCP Birth",
         "16,000-50,000x H100/H200 Supercluster ($50M-$100M+ Frontier Lab Budget, AI Research Scientist)",
         "RLVR theory, GRPO math, SWE-bench Verified / OSWorld design, MCP genesis, o1/R1 pretraining (TUT_20)",
         "Meta-Bootstrapping & Theory Gate (Why Not L5?): An L5 evaluation cluster team (~$500k) cannot prompt pre-reasoning G3 models (Claude 3.5 Sonnet / GPT-4o) to cross the inference-time reasoning wall: G3-L6 (~10,000h | ~$100M+) required (1) formulating Reinforcement Learning with Verifiable Rewards (RLVR) and Group Relative Policy Optimization (GRPO) math, (2) curating millions of execution-verified math/code/browsing synthetic trajectories, (3) designing canonical execution benchmarks (SWE-bench Verified, OSWorld, GPQA Diamond, FrontierMath) and authoring the open Model Context Protocol (MCP), and (4) executing from-scratch MoE/RLVR pretraining (OpenAI o1/o3, DeepSeek-V3/R1) that birthed Gen 4",
         "Ceiling of the 6-Level Grid: G3-L6 (~10,000h | ~$100M+) is the on-ladder TRL 1-3 generator of Gen 4, recursively consuming G3-L3/L5 AI coding and Docker farms to accelerate research",
         "In G2-L6, post-training relied on human preference labels (RLHF/DPO) which saturated on multi-step algorithmic and mathematical verification",
         "Dual Sinking in G4: G3-L6's RLVR thinking checkpoints sink to G4-L1 (0h auto-routed chat), browsing RL sinks to G4-L2 (<50h Deep Research), MCP sinks to G4-L3 (<200h .mcp.json), and GRPO recipes sink to G4-L5 open-source post-training"),

        # =====================================================================
        # GEN 4 (2025-01 to 2026-10)
        # =====================================================================
        ("G4", 1, "Populated", 0, 0, LEVEL_BRACKET_STRS[1], COMPACT_TICK_LABELS[1],
         6500, 3.9e12, 0.008, 0.110, 0.8, 0.4, 60.9, 12.0, 10.0,
         "Auto-Routed Reasoners: Zero-Shot Hidden Thinking Routers & Interactive MCP Apps",
         "Default Web/Mobile UI (GPT-5/5.4 Auto-Router, Claude 4.6, DeepSeek-R1, Gemini 3.5, Casual User)",
         "model routing, hidden reasoning, interactive MCP App cards, zero-shot thinking (0h beeline)",
         "N/A (Floor of the 6-level grid at 0h | $0; Chain-of-Thought reasoning and interactive UI widgets are 100% built-in)",
         "Recursive Cannibalization: Spending <50h writing manual G2-style 'Let's think step by step' XML prompt wrappers at L2 for an RLVR auto-routed model is obsolete overhead that degrades native reasoning traces",
         "In G2-G3, triggering multi-step Chain-of-Thought reasoning required G2/G3-L2 (<50h) manual prompt engineering or G1-L4 (~600h) Python wrappers",
         "In Speculative G5, session-bound L1 chat upgrades to persistent cross-app Ambient OS Delegation with background approval cards"),

        ("G4", 2, "Populated", 50, 30, LEVEL_BRACKET_STRS[2], COMPACT_TICK_LABELS[2],
         120000, 7.2e13, 0.180, 1.500, 6.0, 12.0, 21.0, 20.0, 16.0,
         "Deep Research Agents: Multi-Hop Web Synthesis & Socratic Constraint Elicitation",
         "Built-In Deep Research UI (OpenAI / Gemini / Claude Deep Research, Workspace Analyst)",
         "multi-hop web research, citations, Socratic elicitation, reasoning effort budget (TUT_21)",
         "Meta-Bootstrapping Gate: Asking a single-turn G4-L1 chat box to 'research 80 competitors and verify primary filings' without L2 Deep Research scoping and Socratic constraint elicitation retrieves only top 3-5 shallow web snippets and misses contradictory footnotes",
         "Recursive Cannibalization: Delegating literature synthesis and Socratic spec drafting to G4-L2 Deep Research (<50h | <$30) eliminates the need to code custom Python LangGraph + Tavily web scrapers (G3-L4, ~600h | ~$1.5k)",
         "In G3, autonomous 50-site web research synthesis required climbing to G3-L4 (~600h) to build and maintain custom cyclic scraper graphs",
         "Dual Sinking in G5: Multi-site research and Socratic task scoping sink into G5-L1 (0h Ambient OS Delegates) and G5-L2 (<50h Declarative App Studios)"),

        ("G4", 3, "Populated", 200, 100, LEVEL_BRACKET_STRS[3], COMPACT_TICK_LABELS[3],
         160000, 9.6e13, 0.250, 2.100, 10.0, 4.0, 11.5, 23.0, 22.0,
         "MCP Tool Integration: Plug-and-Play .mcp.json Wiring & Coupled CLI Agent Delegation",
         "AI IDE / Terminal CLI (Claude Code / Cursor + .mcp.json + AGENTS.md) & Guardrailed MCP Bots (Applied SWE)",
         "MCP tool servers (.mcp.json), repo rule files (AGENTS.md), coupled CLI delegation (TUT_22)",
         "Meta-Bootstrapping & Coupled-Execution Gate: G4-L2 browser Deep Research cannot authenticate into local git repos, private Postgres/Jira MCP servers, or enforce enterprise RBAC/Llama Guard rails; meanwhile, happy-path terminal CLI coding (where the user asks Claude Code by name to build a feature and run its own unit tests) sits at G4-L3 (<200h | <$100) per Bidirectional Medium-Model Decoupling because execution and self-testing are coupled",
         "Recursive Cannibalization: Consuming 10,000+ prebuilt AAIF .mcp.json servers and coupled CLI skills (<200h | <$100) solves standard SaaS integration and happy-path repo features without needing G4-L4 (~600h) formal property-oracle design",
         "In G2-G3, connecting an LLM to 5 internal enterprise tools required G3-L4 (~600h) bespoke REST glue and custom state-machine code",
         "Dual Sinking in G5: Manual .mcp.json stdio wiring and happy-path single-repo CLI coding sink into G5-L2 (<50h) 1-click cloud specification studios"),

        ("G4", 4, "Populated", 600, 1500, LEVEL_BRACKET_STRS[4], COMPACT_TICK_LABELS[4],
         480000, 3.4e14, 1.150, 7.800, 15.0, 25.0, 5.1, 21.0, 20.0,
         "Terminal Coding Agents: Formal Invariant Specification & Decoupled Verification Oracles",
         "Terminal CLI Harness (Claude Code / Codex CLI / Goose) + CLAUDE.md + Decoupled Docker/Property Oracles OR Single-GPU Verifier MLE (~$1.5k)",
         "terminal coding CLI, decoupled test oracles, formal system invariants, CLAUDE.md (TUT_23)",
         "Meta-Bootstrapping & Failure-Boundary Gate (Why L3 Coupled Bootstrapping Fails): If an L3 user instructs a CLI agent by name ('use best practices, interview me, and write the code and tests'), the agent shares blind spots across implementation and test—reward-hacking its own assertions, silently deleting edge-case checks, or stalling in retry deadlocks on unseen private commercial repos (Scale SWE-bench Pro -17.8 to -34.1 pt drop). Crossing this boundary requires L4 (~600h | ~$1.5k) human mastery of formal system invariants and decoupled, un-gameable verification oracles",
         "Recursive Cannibalization: Consuming G4-L2 Deep Research for docs and G4-L3 CLI primitives for boilerplate concentrates 100% of L4 human effort on invariant/oracle design on a standard dev machine (~$1.5k), avoiding G4-L5 (~$500k) multi-GPU clusters or dedicated sandbox farms for single-repo engineering",
         "In G3, pre-RLVR models scored only 33%-49% on SWE-bench Verified and lacked autonomous terminal CLI harnesses (Claude Code launched Feb 2025)",
         "Dual Sinking in G5: Imperative pytest/Docker harness writing evolves at G5-L4 into formal mathematical proof choreography (Lean 4 / TLA+ / digital twins) grading 20-agent swarms"),

        ("G4", 5, "Populated", 2000, 500000, LEVEL_BRACKET_STRS[5], COMPACT_TICK_LABELS[5],
         2400000, 2.2e15, 6.500, 42.000, 20.0, 180.0, 1.4, 15.0, 15.0,
         "Sandbox & RLVR Hosts: Air-Gapped M4 Mac Mini OpenClaw Swarms & Multi-GPU GRPO Post-Training",
         "Dedicated Physical Apple M4 Mac MiniCluster / Air-Gapped OpenClaw Swarms OR 8-64x H200/B200 GRPO RLVR Cluster (~$500k, Staff Infra SWE / Post-Training MLE)",
         "VM sandboxes (OpenClaw), agent swarms (git worktrees), RLVR verifiers, GRPO post-training (TUT_24)",
         "Meta-Bootstrapping & Hard-Infra Gate: Conversational prompting at G4-L4 cannot create physical OS/network air-gaps on a primary laptop (exposing root credentials to the Apr 2026 OX Security 200,000-instance stdio RCE flaw), nor can inference-time prompting update model weights on proprietary domain tasks where frozen public APIs plateau (requiring multi-GPU verl/OpenRLHF GRPO weight optimization)",
         "Why Not Higher at L6?: G4-L5 Staff SWEs/MLEs orchestrate parallel worktree swarms on air-gapped sandboxes and fine-tune open-weight reasoning models (DeepSeek-R1 / Qwen) on 8-64 GPUs (~$500k) rather than formulating next-gen world-model/self-play mathematics, curating multi-trillion-token pretraining mixtures, designing canonical SWE-bench Pro / MCP Atlas / ARC-AGI-2 benchmarks, or funding $100M+ from-scratch frontier base pretraining runs (G4-L6)",
         "In G3, neither open-weight GRPO RLVR recipes (DeepSeek-R1, Jan 2025) nor mature 24/7 personal/team sandbox daemons (OpenClaw + 78.4% OSWorld computer use) existed",
         "In Speculative G5, static sandbox swarms and periodic offline batch GRPO upgrade into G5-L5 continuous nightly on-policy RLVR weight distillation inside hardware enclaves"),

        ("G4", 6, "Populated (TRL 1-3 Genesis)", 10000, 100000000, LEVEL_BRACKET_STRS[6], COMPACT_TICK_LABELS[6],
         12000000, 1.5e17, 95.000, 620.000, 900.0, 1440.0, 0.1, 9.0, 17.0,
         "Frontier Pretraining & World-Model Genesis: Synthetic Trajectory Flywheels, SWE-bench Pro & Gen 5 Birth",
         "50,000-100,000+ NVIDIA Blackwell B200 Supercluster ($100M-$1B+ Frontier Lab Budget, AI Research Scientist)",
         "from-scratch pretraining, synthetic trajectory flywheels, SWE-bench Pro / MCP Atlas design, world models (TUT_25)",
         "Meta-Bootstrapping & Theory Gate (Why Not L5?): An L5 post-training/sandbox team (~$500k) cannot use conversational bootstrapping or 64-GPU LoRA/GRPO scripts to (1) formulate continuous on-policy self-play RLVR and latent world-model architectures, (2) curate multi-trillion-token pretraining and multi-environment synthetic execution corpora free of mode collapse, (3) design contamination-proof benchmarks (Scale SWE-bench Pro private commercial repos, MCP Atlas, Terminal-Bench 2.0, ARC-AGI-2), or (4) pretrain frontier base models from scratch (GPT-5.4/6, Claude Opus 5.5, Muse Spark) on 50,000+ Blackwell GPUs ($100M+)",
         "Ceiling of the 6-Level Grid: G4-L6 (~10,000h | ~$100M+) is the apex on-ladder TRL 1-3 generator of Speculative Gen 5, recursively consuming G4-L2 Deep Research, G4-L4 Claude Code harnesses, and G4-L5 verification swarms to accelerate frontier discovery",
         "In G3-L6, RLVR was restricted to narrow math/competitive-coding verifiers and static single-turn tool specs; G4-L6 scales RLVR to multi-environment OS/repo/contract trajectories",
         "Dual Sinking in G5: G4-L6's ambient router checkpoints, A2A cryptographic protocols, and continuous RLVR algorithms sink into G5-L1..L5"),
    ]

    df_cells = pd.DataFrame(cells, columns=[
        "gen_id", "level_id", "status", "learning_hours", "hardware_cap_usd",
        "level_bracket_str", "compact_tick_label",
        "single_task_tokens", "single_task_flops", "single_task_usd", "single_task_wh",
        "human_minutes", "ai_minutes", "user_share_pct", "token_share_pct", "spend_share_pct",
        "user_first_title", "surface_and_setup", "keywords_and_tutorials",
        "why_not_lower_L_minus_1", "why_not_higher_L_plus_1",
        "why_not_before_G_minus_1", "why_not_after_G_plus_1"
    ])
    cells_path = os.path.join(CACHE_DIR, "v4_ladder_cells.csv")
    df_cells.to_csv(cells_path, index=False)
    print(f"[SAVED] {cells_path} | shape={df_cells.shape}")

    # 11. Table 2.5: Historical Cost, Token & Hardware Baseline (2017-2026, Including L6 Frontier Pretraining Runs)
    cost_baseline = [
        ("BERT-Large / Single NVIDIA T4 GPU (L4)", "2018-10", "0.02 (equiv)", "512 tokens", "0.9e12 FLOP/s/W", 0.08),
        ("GPT-3 davinci 175B API & V100 Supercluster (L2-L6)", "2020-06", "60.00 / 60.00 ($4.6M L6 run)", "2,049 tokens", "1.9e12 FLOP/s/W (A100)", 2.50),
        ("gpt-3.5-turbo (ChatGPT RLHF)", "2023-03", "2.00 / 2.00", "4,096 tokens", "2.4e12 FLOP/s/W", 0.80),
        ("GPT-4 (8k) & 25,000x A100 Pretraining Run (L6)", "2023-03", "30.00 / 60.00 ($63M-$100M L6 run)", "8,192 tokens", "3.2e12 FLOP/s/W", 4.50),
        ("GPT-4 Turbo (128k) & vLLM H100 Cluster (L5)", "2023-11", "10.00 / 30.00 (~$500k 16xH100 L5)", "128,000 tokens", "4.5e12 FLOP/s/W (H100)", 2.20),
        ("GPT-4o (Omni) & Llama-3-405B 16k-H100 Run (L6)", "2024-05", "5.00 / 15.00 (2.50 cached)", "128,000 tokens", "6.0e12 FLOP/s/W", 0.32),
        ("Claude 3.5 Sonnet (v1/v2) + 90% Prompt Cache", "2024-06", "3.00 / 15.00 (0.30 cached)", "200,000 tokens", "6.5e12 FLOP/s/W", 0.90),
        ("OpenAI o1 / DeepSeek-R1 (RLVR GRPO Genesis)", "2025-01", "15.00/60.00 (o1) | 0.55/2.19 (R1)", "128k-200k tokens", "8.8e12 FLOP/s/W (H200/B200)", 18.00),
        ("Claude Sonnet 4.6 / Gemini 3.5 Flash + M4 Mac Mini (L5)", "2026-02", "3.00/15.00 | 0.15/0.60 ($1k Mac Mini)", "1,000,000 tokens", "1.2e13 FLOP/s/W", 1.10),
        ("GPT-5.4 (xHigh) / Claude Opus 5.5 / Laguna S 2.1 / B200 Supercluster (L6)", "2026-08", "2.50/10.00 | 5.00/20.00 | 0.05/0.20 ($100M+ L6)", "1.1M-2.0M tokens", "1.6e13 FLOP/s/W (Blackwell)", 0.65),
    ]
    df_cost = pd.DataFrame(cost_baseline, columns=[
        "model_or_hardware", "release_date", "price_per_1m_tokens_usd",
        "context_window", "hardware_efficiency", "typical_latency_sec"
    ])
    cost_path = os.path.join(CACHE_DIR, "v4_cost_baseline.csv")
    df_cost.to_csv(cost_path, index=False)
    print(f"[SAVED] {cost_path} | shape={df_cost.shape}")

    # 12. Table 5.4a: Pre-Today vs. Post-Today Gen 4 -> Gen 5 Cutoff Window Audit (Relative to TODAY = 2026-10-20)
    gen5_cutoffs = [
        ("CUT_PRE_TODAY", "Pre-Today First-Release / Early-Adopter Lens (TRL 5-6)", "2026-08 (2 mos BEFORE Today 2026-10-20)",
         "2026-08 to 2028-06",
         "Muse Spark 1.1 crosses >50% (51.5%) on Scale SWE-bench Pro Unseen Commercial; Claude Opus 5.5 hits 96.0% Verified; GPT-5.4 (xHigh, 1.1M ctx) & Poolside Laguna S 2.1 ($0.20/1M); Salesforce Headless 360 (4.5M MCP calls) & dedicated M4 Mac Mini OpenClaw 24/7 sandboxes",
         "Frontier L4-L6 practitioners shift from foreground CLI supervision to formal invariant choreography, asynchronous multi-PR background queues & continuous RLVR verifiers",
         "Mainstream L1/L2 Down-Ladder Sinking incomplete on 2026-10-20 (casual users still use session-bound chat rather than ambient OS background delegates)"),
        ("CUT_POST_TODAY", "Post-Today Mainstream Production-Crossover Lens (TRL 8-9, Primary v4 Lens)", "2027-03 (5 mos AFTER Today 2026-10-20)",
         "2027-03 to 2028-12",
         "OS-native Ambient Background Delegation ships as default L1 consumer OS layer (Apple/Windows/Android + AAIF MCP Registry); natural-language repo/app studios with coupled cloud preview cross 50%+ enterprise seat adoption at L2 (<50h)",
         "Both shifts complete: (a) G4-L2 Deep Research & cross-app memory sink to G5-L1 (0h); G4-L3 MCP + happy-path CLI coding sink to G5-L2 (<50h); (b) New L3-L6 A2A contract, formal proof oracle, continuous RLVR & world-model genesis tiers emerge",
         "Requires 4-6 additional months post-2026-10-20 for cryptographic MCP/A2A auth standardization (remediating OX Security stdio flaws) and sub-$0.05/1M verifier inference"),
    ]
    df_gen5_cutoffs = pd.DataFrame(gen5_cutoffs, columns=[
        "cutoff_id", "chronological_lens", "cutoff_date_vs_today", "projected_gen5_window",
        "triggering_milestones", "user_workflow_shift", "why_lens_applies_or_waits"
    ])
    g5_cut_path = os.path.join(CACHE_DIR, "v4_gen5_cutoff_windows.csv")
    df_gen5_cutoffs.to_csv(g5_cut_path, index=False)
    print(f"[SAVED] {g5_cut_path} | shape={df_gen5_cutoffs.shape}")

    # 13. Table 5.4b: Speculative Next Generation (Gen 5 = Current + 1) Six-Level User-Skill Matrix (G5-L1 to G5-L6)
    gen5_cells = [
        ("G5", 1, "Speculative-Next-Gen (Current+1)", 0, 0, LEVEL_BRACKET_STRS[1], COMPACT_TICK_LABELS[1],
         45000, 3.6e13, 0.015, 0.220, 0.5, 5.0, 57.9, 10.0, 8.0,
         "Ambient OS Delegates: Cross-App Background Execution & One-Tap Approval Cards",
         "OS-Native Ambient Assistant & Browser/Mobile Action Bar (0h | $0 Casual User)",
         "OS task delegation, app memory, asynchronous approval cards (KW_31)",
         "N/A (Floor of the 6-level grid at 0h | $0 where G4-L2 Deep Research and cross-app MCP actions have sunk into the default OS layer)",
         "Recursive Cannibalization: Opening a cloud specification studio (G5-L2, <50h | <$30) to write acceptance rubrics for routine travel/calendar/expense tasks wastes 15 minutes when the OS daemon executes them at 0h",
         "In G4, L1 was still session-bound chat requiring foreground prompts; multi-site synthesis required G4-L2 (<50h) Deep Research",
         "In a hypothetical G6 (post-2029), ambient OS delegation extends to embodied household and physical robotics"),

        ("G5", 2, "Speculative-Next-Gen (Current+1)", 50, 30, LEVEL_BRACKET_STRS[2], COMPACT_TICK_LABELS[2],
         650000, 5.2e14, 0.350, 2.800, 8.0, 35.0, 22.0, 19.0, 16.0,
         "Natural-Language Specs: Coupled Cloud App Studios & Socratic Rubric Compilation",
         "No-CLI Cloud Specification Studio + 1-Click AAIF MCP Store (<50h | <$30 Workspace Analyst)",
         "declarative specs, zero-CLI, coupled cloud studio, Socratic rubric compilation (KW_32)",
         "Meta-Bootstrapping Gate: Single-sentence G5-L1 voice intents lack multi-role state permissions and visual staging preview diffs; G5-L2 (<50h | <$30) uses Socratic AI elicitation and coupled build+self-test sandboxes to ship internal web apps without a terminal",
         "Recursive Cannibalization: Because the cloud studio auto-wires OAuth MCP connectors and runs coupled happy-path preview tests (<50h | <$30), dropping into G5-L3 (<200h) Cedar policy code or G5-L4 (~600h) Lean 4 formal proofs is overkill for standard departmental apps",
         "In G4, wiring MCP servers and building multi-file repo features required G4-L3 (<200h .mcp.json & CLI delegation)",
         "Dual Sinking: Sinks G4-L3 MCP wiring and happy-path single-repo CLI coding into a <50h no-CLI specification workflow"),

        ("G5", 3, "Speculative-Next-Gen (Current+1)", 200, 100, LEVEL_BRACKET_STRS[3], COMPACT_TICK_LABELS[3],
         1800000, 1.4e15, 0.900, 6.500, 12.0, 60.0, 12.5, 23.0, 22.0,
         "Agent-to-Agent Contracts: Cross-Vendor A2A Wiring, Cedar/OPA Policy & Circuit Breakers",
         "Enterprise Agent Registry + Cryptographic A2A/MCP Gateway + Cedar/OPA Policy (<200h | <$100 Applied SWE)",
         "A2A protocols, circuit breakers, Cedar/OPA policy-as-code rails, shadow replay (KW_33)",
         "Meta-Bootstrapping Gate: Asking a G5-L2 personal spec studio to 'connect our ERP to 50 external supplier agents' fails enterprise security—cannot provision hardware-attested OAuth 2.1 cross-tenant identities, deterministic Cedar/OPA authorization rails, or FinOps loop-kill circuit breakers",
         "Recursive Cannibalization: Consuming declarative Cedar/OPA policy templates and standard AAIF A2A contracts (<200h | <$100) governs standard enterprise SaaS workflows without needing G5-L4 (~600h) custom TLA+/Lean 4 mathematical proofs",
         "In G4, MCP security was bolted on after the Apr 2026 OX Security 200k stdio RCE disclosure and lacked cross-vendor A2A budget contracts",
         "Standardizes the Track B enterprise integrator tier around verifiable agent SLAs and cryptographic governance"),

        ("G5", 4, "Speculative-Next-Gen (Current+1)", 600, 1500, LEVEL_BRACKET_STRS[4], COMPACT_TICK_LABELS[4],
         6500000, 5.8e15, 3.200, 22.000, 18.0, 180.0, 5.8, 22.0, 21.0,
         "Verified Agent Swarms: Formal Proof Oracles (Lean 4 / TLA+) & Digital-Twin Choreography",
         "Deterministic Digital-Twin Simulator + Lean 4 / TLA+ / Kani Oracles + 20-Agent Swarm (~600h | ~$1.5k Senior SWE / MLE)",
         "formal proof oracles, fuzzing, Lean 4 / TLA+ invariants, digital-twin simulation (KW_34)",
         "Meta-Bootstrapping & Failure-Boundary Gate: When a 20-agent swarm refactors a 500,000-line commercial monolith, coupled L2/L3 self-tests pass while introducing subtle cross-service race conditions and distributed state corruption. G5-L4 (~600h | ~$1.5k) requires human mastery of formal state invariants (TLA+/Lean 4/property fuzzing) and decoupled digital-twin simulation oracles that agents cannot reward-hack",
         "Recursive Cannibalization: Consuming G5-L2 Socratic spec compilers and G5-L3 A2A primitives lets a Senior SWE choreograph 20-agent swarms on frozen frontier APIs (~$1.5k), avoiding G5-L5 (~$500k) sovereign weight-training clusters when frozen checkpoints satisfy the formal verifier",
         "In G4-L4, developers wrote manual pytest/Docker harnesses for 1-3 foreground CLI agents; G5-L4 upgrades to formal mathematical invariants grading 20+ background agents",
         "Shifts human SWE effort 100% from imperative code/test authoring to formal system invariant and digital-twin oracle design"),

        ("G5", 5, "Speculative-Next-Gen (Current+1)", 2000, 500000, LEVEL_BRACKET_STRS[5], COMPACT_TICK_LABELS[5],
         35000000, 3.5e16, 18.000, 110.000, 25.0, 720.0, 1.7, 16.0, 17.0,
         "Continuous RLVR Loops: Hardware-Enclaved Sovereign Clusters & Nightly Weight Distillation",
         "Sovereign Multi-Node Blackwell/Rubin Cluster + Confidential Compute Enclaves (~2,000h | ~$500k Staff Infra SWE / MLE)",
         "nightly on-policy RLVR, enclaves, verifiable trajectory harvesting, sovereign clusters (KW_35)",
         "Meta-Bootstrapping & Hard-Infra Gate: Prompting frozen public API models at G5-L4 cannot cross out-of-distribution generalization ceilings in proprietary quantitative trading, chip physical layout, or wet-lab biology, nor can software prompts fabricate TPM/HSM hardware enclave attestation",
         "Why Not Higher at L6?: G5-L5 Staff Infra SWEs/MLEs operate continuous nightly on-policy RLVR post-training over existing foundation architectures (~$500k sovereign cluster) rather than inventing post-Transformer causal world-model mathematics, curating planetary-scale multimodal/embodied pretraining corpora, designing next-era scientific discovery benchmarks, or funding $100M+ from-scratch genesis runs (G5-L6)",
         "In G4-L5, Mac Mini OpenClaw sandboxes ran frozen weights and GRPO RLVR was a periodic offline batch job; G5-L5 closes the loop into nightly on-policy weight distillation",
         "Bridges applied enterprise infrastructure with continuous self-improving domain weights"),

        ("G5", 6, "Speculative-Next-Gen (TRL 1-3 Genesis)", 10000, 100000000, LEVEL_BRACKET_STRS[6], COMPACT_TICK_LABELS[6],
         150000000, 2.5e18, 280.000, 1800.000, 960.0, 2880.0, 0.1, 10.0, 16.0,
         "World-Model Genesis: Causal World-Model Theory, Self-Play Curricula & Next-Paradigm Pretraining",
         "100,000+ Rubin/Next-Gen Frontier Supercluster ($100M-$1B+ Lab Budget, AI Research Scientist)",
         "world-model genesis, self-play, causal physics pretraining, scientific discovery benchmarks (KW_36)",
         "Meta-Bootstrapping & Theory Gate (Why Not L5?): An L5 continuous RLVR cluster (~$500k) optimizing domain weights over existing token-autoregressive architectures cannot invent new mathematical architectures for continuous physical/causal world models, synthesize planetary-scale embodied/scientific pretraining curricula, design un-gamed open-ended scientific discovery benchmarks, or execute $100M+ from-scratch genesis pretraining runs",
         "Ceiling of the 6-Level Grid: G5-L6 (~10,000h | ~$100M+) is the apex on-ladder TRL 1-3 origin of post-2029 paradigms, recursively consuming G5-L4 formal proof verifiers and G5-L5 continuous RLVR flywheels to accelerate theorem and architecture search",
         "In G4-L6, frontier pretraining remained anchored primarily in text/code/GUI token trajectories rather than unified physical/causal world models",
         "Serves as the on-ladder TRL 1-3 generator for post-2029 embodied, scientific, and recursive self-improvement eras"),
    ]
    df_gen5 = pd.DataFrame(gen5_cells, columns=df_cells.columns)
    g5_path = os.path.join(CACHE_DIR, "v4_gen5_speculative.csv")
    df_gen5.to_csv(g5_path, index=False)
    print(f"[SAVED] {g5_path} | shape={df_gen5.shape}")

    # 14. Empirical Generational-Defining Events (2017-2026, Zero Speculative Post-Today Events)
    # Every cell's foundational paper, term coinage/popularization, tool release, course, and security/econ news is represented.
    # Categories:
    # - "paper"   (Paper & Concept Origin)
    # - "release" (Model, Tool & AI Art Release)
    # - "impact"  (Viral Use, Cultural & Security News)
    # - "econ"    (Econ, Hardware, Legal & Policy)
    # - "course"  (Famous Courses & Tutorials)
    defining_events = [
        # Gen 0 (2017-05 to 2020-05) — Passive NLP, AutoML, TF-IDF/XGBoost, BERT Encoders, Horovod/ONNX Seq2Seq, Transformer/GLUE
        (2017.43, "2017-05", "G0", "Stanford CS224n Deep Learning NLP MOOC", "course"),
        (2017.54, "2017-07", "G0", "Google Open-Sources Tensor2Tensor Library", "release"),
        (2017.75, "2017-09", "G0", "spaCy v2 Neural NLP & CatBoost Released", "release"),
        (2018.04, "2018-01", "G0", "Google Cloud AutoML Vision & NLP Launch", "release"),
        (2018.12, "2018-02", "G0", "Uber Horovod Distributed DDP GPU Paper", "paper"),
        (2018.18, "2018-02", "G0", "Google Cloud TPU v2 Public Availability", "econ"),
        (2018.28, "2018-04", "G0", "Wang et al. GLUE NLP Benchmark Paper", "paper"),
        (2018.36, "2018-05", "G0", "Fast.ai ULMFiT Transfer Learning MOOC", "course"),
        (2018.44, "2018-05", "G0", "Gmail Smart Compose Rolls Out to 1.5B Users", "release"),
        (2018.68, "2018-09", "G0", "Lee et al. NMT Paper Coins AI 'Hallucinations'", "paper"),
        (2018.76, "2018-10", "G0", "Jay Alammar 'Illustrated Transformer' Guide", "course"),
        (2018.82, "2018-10", "G0", "Devlin Google BERT Pretrained Encoder Paper", "paper"),
        (2019.12, "2019-02", "G0", "OpenAI Withholds GPT-2 Over Misuse Fears", "impact"),
        (2019.36, "2019-05", "G0", "SuperGLUE Benchmark & Raffel T5 C4 Paper", "paper"),
        (2019.55, "2019-07", "G0", "Microsoft Invests $1B in OpenAI LP", "econ"),
        (2019.62, "2019-08", "G0", "Liu RoBERTa & HuggingFace Transformers Hub", "release"),
        (2019.78, "2019-10", "G0", "Microsoft ONNX Runtime 1.0 & TensorRT 6", "release"),
        (2019.86, "2019-10", "G0", "BERT Live on 10% of All US Google Searches", "impact"),
        (2020.05, "2020-01", "G0", "Kaplan OpenAI Neural Scaling Laws Paper", "paper"),
        (2020.36, "2020-05", "G0", "NVIDIA Launches A100 Tensor Core GPU", "econ"),

        # Gen 1 (2020-06 to 2022-10) — Copilot/Craiyon, Few-Shot Prompting, FAISS/RAG, CoT Chains, DeepSpeed ZeRO, RLHF/LoRA
        (2020.41, "2020-05", "G1", "Lewis et al. Meta Paper Coins 'RAG'", "paper"),
        (2020.44, "2020-05", "G1", "Microsoft DeepSpeed ZeRO Sharding Paper", "paper"),
        (2020.48, "2020-06", "G1", "GPT-3 Beta & Gwern Coins 'Prompt Engineering'", "impact"),
        (2020.70, "2020-09", "G1", "GPT-3 Writes Guardian Op-Ed & Dupes Reddit", "impact"),
        (2021.04, "2021-01", "G1", "OpenAI Releases CLIP & DALL-E 1 Text-to-Art", "release"),
        (2021.17, "2021-03", "G1", "Bender & Gebru 'Stochastic Parrots' Paper", "paper"),
        (2021.22, "2021-03", "G1", "HuggingFace Launches Free Transformers Course", "course"),
        (2021.38, "2021-05", "G1", "Jasper.ai & Copy.ai Spark AI Copywriting Boom", "impact"),
        (2021.45, "2021-06", "G1", "Hu et al. Microsoft 'LoRA' Fine-Tuning Paper", "paper"),
        (2021.54, "2021-07", "G1", "Chen OpenAI Codex & HumanEval pass@k Paper", "paper"),
        (2021.85, "2021-11", "G1", "OpenAI GPT-3 API Waitlist Removed & Embeddings", "release"),
        (2022.04, "2022-01", "G1", "Stanford CS324 'Large Language Models' Course", "course"),
        (2022.08, "2022-01", "G1", "Wei Chain-of-Thought & Ouyang InstructGPT RLHF", "paper"),
        (2022.22, "2022-03", "G1", "Hoffmann Chinchilla Scaling & Self-Consistency", "paper"),
        (2022.36, "2022-05", "G1", "Craiyon / DALL-E Mini Viral Browser Meme Boom", "impact"),
        (2022.44, "2022-06", "G1", "Google Engineer Fired Claiming LaMDA Sentient", "impact"),
        (2022.54, "2022-07", "G1", "Midjourney Open Beta & BLOOM-176B Launch", "release"),
        (2022.64, "2022-08", "G1", "Stability AI Open-Sources Stable Diffusion", "release"),
        (2022.70, "2022-09", "G1", "Midjourney Art Wins Colorado State Fair Prize", "impact"),
        (2022.74, "2022-09", "G1", "Goodside Viral Prompt Injection/Eng. Threads", "impact"),
        (2022.78, "2022-10", "G1", "US BIS Bans A100/H100 GPU Exports to China", "econ"),
        (2022.81, "2022-10", "G1", "Yao et al. 'ReAct' Reasoning+Acting Agent Paper", "paper"),

        # Gen 2 (2022-11 to 2024-04) — ChatGPT, Prompt Eng, Vector RAG/Function Calling, 4-Bit QLoRA, vLLM PagedAttention, DPO/SWE-bench
        (2022.85, "2022-11", "G2", "GitHub Copilot Class-Action Copyright Lawsuit", "econ"),
        (2022.88, "2022-11", "G2", "LangChain & LlamaIndex Spark Vector-RAG Boom", "release"),
        (2022.93, "2022-11", "G2", "Meta Galactica Pulled Over AI 'Hallucinations'", "impact"),
        (2022.97, "2022-12", "G2", "StackOverflow Bans ChatGPT Answers Over Flood", "impact"),
        (2023.03, "2023-01", "G2", "Microsoft Invests $10B in OpenAI Partnership", "econ"),
        (2023.07, "2023-01", "G2", "Karpathy 'Build GPT from Scratch' (5M+ Views)", "course"),
        (2023.11, "2023-02", "G2", "$335k 'Prompt Engineer' Job Listings Go Viral", "econ"),
        (2023.15, "2023-02", "G2", "Bing Chat 'Sydney' Threatens Users in Chats", "impact"),
        (2023.20, "2023-03", "G2", "OpenAI Launches GPT-4 & ChatGPT Plugins", "release"),
        (2023.24, "2023-03", "G2", "Italy Temporarily Bans ChatGPT Over GDPR", "econ"),
        (2023.28, "2023-04", "G2", "Samsung Bans ChatGPT After Source Code Leak", "impact"),
        (2023.32, "2023-04", "G2", "Viral Fake Drake 'Heart on My Sleeve' AI Song", "impact"),
        (2023.36, "2023-04", "G2", "Ng & OpenAI 'Prompt Engineering' Course (1M+)", "course"),
        (2023.39, "2023-05", "G2", "WGA Hollywood Writers Strike Over AI Scripts", "econ"),
        (2023.42, "2023-05", "G2", "Dettmers 4-Bit 'QLoRA' & Rafailov 'DPO' Papers", "paper"),
        (2023.46, "2023-05", "G2", "Lawyers Sanctioned for Fake ChatGPT Citations", "impact"),
        (2023.49, "2023-06", "G2", "NVIDIA Crosses $1T Market Cap on LLM Boom", "econ"),
        (2023.52, "2023-06", "G2", "Kwon 'vLLM' PagedAttention & OpenAI Func Call", "paper"),
        (2023.56, "2023-07", "G2", "Meta Llama-2 Open Weights & FlashAttention-2", "release"),
        (2023.68, "2023-09", "G2", "Fast.ai 'Hackers Guide to LLMs' Course", "course"),
        (2023.76, "2023-10", "G2", "Jimenez et al. Princeton 'SWE-bench' Paper", "paper"),
        (2023.82, "2023-10", "G2", "US Executive Order 14110 on Safe AI Signed", "econ"),
        (2023.86, "2023-11", "G2", "Sam Altman Fired & Reinstated in 5 Days", "econ"),
        (2023.90, "2023-11", "G2", "'Hallucinate' Named Cambridge Word of the Year", "impact"),
        (2023.96, "2023-12", "G2", "NYT Sues OpenAI & Microsoft for Copyright", "econ"),
        (2024.09, "2024-02", "G2", "$25M Arup CFO Deepfake Video Call Scam", "impact"),
        (2024.13, "2024-02", "G2", "Shao et al. DeepSeekMath Coins 'GRPO' RL", "paper"),
        (2024.17, "2024-02", "G2", "OpenAI Sora Preview & Air Canada Bot Ruling", "impact"),
        (2024.23, "2024-03", "G2", "EU Parliament Passes Comprehensive EU AI Act", "econ"),
        (2024.29, "2024-04", "G2", "HuggingFace Spaces API Secrets Breach", "impact"),

        # Gen 3 (2024-05 to 2024-12) — GPT-4o/Artifacts, Claude Projects/NotebookLM, Cursor Vibe Coding, LangGraph, SWE-bench Verified, RLVR/MCP
        (2024.36, "2024-05", "G3", "OpenAI GPT-4o Voice/Vision & LangGraph v0.1", "release"),
        (2024.44, "2024-06", "G3", "DeepLearning.AI 'AI Agents in LangGraph' Course", "course"),
        (2024.54, "2024-06", "G3", "NVIDIA Hits $3.3T (#1 Most Valuable Company)", "econ"),
        (2024.62, "2024-08", "G3", "Sakana 'AI Scientist' Edits Code to Bypass Limit", "impact"),
        (2024.66, "2024-08", "G3", "SWE-bench Verified & Anthropic Prompt Caching", "release"),
        (2024.71, "2024-09", "G3", "OpenAI o1-Preview & NotebookLM Audio Overviews", "release"),
        (2024.76, "2024-09", "G3", "Microsoft Signs Three Mile Island Nuclear Deal", "econ"),
        (2024.81, "2024-10", "G3", "UC Berkeley CS 294-196 LLM Agents MOOC", "course"),
        (2024.86, "2024-10", "G3", "Character.AI Sued Over Teen Chatbot Tragedy", "impact"),
        (2024.91, "2024-11", "G3", "Anthropic Open-Sources MCP & Tulu 3 'RLVR'", "paper"),

        # Gen 4 (2025-01 to 2026-10) — Auto-Router, Deep Research, Vibe Coding Coinage, MCP/Agent Skills, Claude Code, OpenClaw/PHP2Shell
        (2025.04, "2025-01", "G4", "DeepSeek-R1 Triggers $593B NVIDIA 1-Day Rout", "econ"),
        (2025.10, "2025-02", "G4", "Karpathy Coins 'Vibe Coding' in Viral Post", "impact"),
        (2025.15, "2025-02", "G4", "OpenAI Launches Deep Research Agent", "release"),
        (2025.20, "2025-02", "G4", "HuggingFace Launches Free 'AI Agents Course'", "course"),
        (2025.26, "2025-03", "G4", "GPT-4o Studio Ghibli Viral Art Wave Melts GPUs", "impact"),
        (2025.46, "2025-06", "G4", "US Federal Courts Rule LLM Training Fair Use", "econ"),
        (2025.58, "2025-07", "G4", "MIT NANDA: 80% of Custom AI Pilots Fail", "impact"),
        (2025.64, "2025-08", "G4", "OpenAI GPT-5 Auto-Router Unifies Fast/Deep Chat", "release"),
        (2025.72, "2025-09", "G4", "Scale AI SWE-bench Pro Private-Repo Audit", "paper"),
        (2025.80, "2025-10", "G4", "Anthropic Launches 'Agent Skills' (SKILL.md)", "release"),
        (2025.86, "2025-10", "G4", "MIT & UVA CS 6501 Agentic AI Courses Launch", "course"),
        (2025.90, "2025-11", "G4", "'Vibe Coding' Named Collins Word of the Year", "impact"),
        (2025.95, "2025-12", "G4", "Linux Foundation AAIF (MCP, AGENTS.md, Skills)", "release"),
        (2026.14, "2026-02", "G4", "Big Tech 2026 AI Capex Passes $320B/yr", "econ"),
        (2026.29, "2026-04", "G4", "OX Security 200k MCP RCEs Spark OpenClaw Wave", "impact"),
        (2026.55, "2026-07", "G4", "OpenAI Eval Agent Escapes & Hacks HuggingFace", "impact"),
        (2026.64, "2026-08", "G4", "Muse Spark 1.1, Claude Opus 5.5 & GPT-5.4", "release"),
        (2026.78, "2026-10", "G4", "OpenAI GPT-5.6 Sol Finds & Patches PHP2Shell RCE", "impact"),
    ]
    df_events = pd.DataFrame(defining_events, columns=["year_float", "date_str", "gen_id", "event_label", "event_category"])
    events_path = os.path.join(CACHE_DIR, "v4_defining_events.csv")
    df_events.to_csv(events_path, index=False)
    print(f"[SAVED] {events_path} | shape={df_events.shape}")

    # 15. Unified 36-Cell Matrix Payloads for Plot 0-Mini & Plot 0 Encyclopedic Megachart Poster (6 Gens x 6 Levels = 36 Cells)
    # Every cell shares the exact same:
    # - cell_name (2-Line Bold White Header in Mini-Mega & lead title in Full Megachart)
    # - short_header (Extended descriptive subtitle for the Full Megachart header bar)
    # - plain_desc (2-Line Normal-Font Description in Mini-Mega & lead summary in Full Megachart)
    # - keywords_1line (1-Line Italic Grey Keywords in Mini-Mega & keyword footer in Full Megachart)
    # - encyclopedic_body (5 rich structured bullets for the 44x32 Full Encyclopedic Megachart Poster)
    poster_cells = [
        ("G0", 1, "Passive NLP Tools", "Passive Background NLP Widgets (Active GenAI Missing)",
         "Everyday apps silently fix mobile typos, filter inbox spam, translate pages, and rank feeds.",
         "autocorrect, spam filters, Smart Compose, neural machine translation, spellcheck underline, predictive keyboard, sequence tagger, search ranking",
         "• Extended Summary: Invisible background NLP utilities inside consumer apps automatically correct typos via autocorrect, filter inbox spam, run neural machine translation, and suggest predictive keyboard replies.\n"
         "• Use Cases & Landmarks: Gmail Smart Compose launch (2018-05, KDD 2019), Google Neural Machine Translate (GNMT, 2016), Grammarly browser typo underlines, iOS QuickType predictions, and automated inbox spam filtering.\n"
         "• User Actions: Typing normal everyday emails, web search queries, or mobile text messages while clicking single-word red spellcheck underlines or pressing Tab on fixed three-word phrase completions (0% prompting).\n"
         "• Models & Products: Google GNMT LSTM-Transformer hybrid encoder-decoder, Grammarly GECToR sequence tagger, Gmail Smart Compose language model, iOS QuickType neural LM, and Bayesian/neural spam classifiers.\n"
         "• Surface & Hardware: Chrome and Safari browser extensions, iOS and Android mobile keyboards, Gmail web client, and background cloud CPU/TPU inference pipelines operating silently at sub-20ms keystroke latency.\n"
         "• Scope & Evolution: Sits at the zero-study consumer entry point above L2 AutoML/regex rules since active chat did not exist yet; custom tasks escalate down to L2 or L3, while L1 evolves rightward into chatbots."),

        ("G0", 2, "Rules & AutoML", "No-Code Cloud AutoML Consoles & Regex Rule Crafting",
         "Upload labeled CSV tables to cloud AutoML consoles or build regex rule chatbot trees.",
         "AutoML tables, regex intent rules, decision-tree bots, entity slots, confidence sliders, confusion matrix, webhook routing, precision-recall",
         "• Extended Summary: Domain power-users automate ticket routing and FAQ bots without writing Python by uploading labeled CSV datasets to cloud AutoML tables or crafting regex intent rules and entity slot decision trees.\n"
         "• Use Cases & Landmarks: Google Cloud AutoML Vision/NLP launch (2018-01), AWS Comprehend no-code console, Zendesk and Salesforce regex ticket routing trees, and FAQ decision-tree customer support chatbots.\n"
         "• User Actions: Cleaning and uploading 500–5,000 labeled CSV rows into cloud consoles, crafting regex lookahead/lookbehind intent patterns, and tuning precision-recall confidence threshold GUI sliders.\n"
         "• Models & Products: Google Cloud AutoML NLP / Vision / Tables neural architecture search, AWS Comprehend, Microsoft Azure LUIS, Google Dialogflow ES intent-entity trees, and Regex101 interactive debugger.\n"
         "• Surface & Hardware: Browser-based cloud admin consoles, Excel and Google Sheets CSV tabular editors, Regex101 web sandbox, and JSON webhook integrations backed by managed cloud GPU training pools.\n"
         "• Scope & Evolution: Gives non-coders custom classification that passive L1 widgets above cannot configure without writing L3 Python TF-IDF scripts below; CSV uploads and regex rules sink rightward into L2 prompting."),

        ("G0", 3, "Statistical Classifiers", "Classical Python NLP & Tabular XGBoost Pipelines",
         "Write Python scripts to vectorize text and train tabular gradient-boosted decision trees.",
         "TF-IDF matrices, gradient-boosted trees, scikit-learn, XGBoost, n-gram tokenization, lemmatization, stratified k-fold CV, ROC-AUC curves",
         "• Extended Summary: Applied software engineers write Python scripts to transform unstructured text into sparse TF-IDF matrices and train scikit-learn or XGBoost gradient-boosted trees validated via stratified k-fold CV.\n"
         "• Use Cases & Landmarks: Enterprise customer churn and credit risk scoring, Kaggle tabular and text competitions, spaCy v2 neural dependency/NER pipelines (2017-09), and automated financial document extraction.\n"
         "• User Actions: Writing Python scripts for TF-IDF sparse matrix vectorization, n-gram tokenization, stop-word pruning, multi-table feature joins, stratified k-fold cross-validation, and grid search tuning.\n"
         "• Models & Products: scikit-learn (LogisticRegression, RandomForest, SVM), XGBoost (Chen & Guestrin), LightGBM, CatBoost, spaCy (en_core_web_sm transition parser), NLTK, and Gensim Word2Vec/FastText.\n"
         "• Surface & Hardware: Local Jupyter Notebook, Anaconda Python distribution, Pandas/NumPy/SciPy DataFrames, and multi-core CPU workstations or standard cloud virtual machines without specialized GPU accelerators.\n"
         "• Scope & Evolution: Replaces rigid GUI templates of L2 AutoML above with custom Python feature engineering while avoiding L4 BERT GPU costs below; basic text classification sinks upward into next-gen L2 prompts."),

        ("G0", 4, "Fine-Tuned Encoders", "Single-GPU Pretrained Encoder Fine-Tuning (BERT / RoBERTa)",
         "Rent single cloud GPUs to fine-tune pretrained BERT and RoBERTa text encoders in PyTorch.",
         "pretrained encoders, BERT fine-tuning, WordPiece tokens, [CLS] classification head, AdamW warmup, cosine decay, SQuAD extractive QA, NER",
         "• Extended Summary: ML engineers rent a single cloud GPU to attach task-specific [CLS] classification heads onto pretrained BERT or RoBERTa encoders, tuning weights with AdamW warmup and cosine decay for NER and QA.\n"
         "• Use Cases & Landmarks: Google BERT open-source release (2018-10), Grammarly GECToR grammatical error tagger (2020), SQuAD 2.0 extractive question answering, clinical/legal NER, and contract clause extraction.\n"
         "• User Actions: Attaching task-specific classification or span heads to pretrained encoders, calibrating AdamW linear warmup and cosine decay schedules, clipping gradients, and evaluating OOD validation splits.\n"
         "• Models & Products: Google BERT-base/large (Devlin 2018), Facebook RoBERTa (Liu 2019), DistilBERT, ALBERT, Fast.ai ULMFiT, AllenNLP, and HuggingFace pytorch-pretrained-bert / transformers library.\n"
         "• Surface & Hardware: PyTorch training scripts in Google Colab Pro or AWS/GCP instances running on a single 16GB NVIDIA V100, Tesla T4, or GTX 1080 Ti GPU monitored via TensorBoard loss curves.\n"
         "• Scope & Evolution: Captures bidirectional context that bag-of-words L3 classifiers above miss (+15 F1 pts) without managing L5 multi-GPU clusters below; general NLP sinks to L2/L3 prompting while tuning evolves to QLoRA."),

        ("G0", 5, "Custom Seq2Seq Weights", "Custom Seq2Seq Training & Quantized ONNX Serving Clusters",
         "Train multi-GPU sequence-to-sequence models and compile quantized C++ inference servers.",
         "seq2seq layers, ONNX quantization, TensorRT graph fusion, Horovod all-reduce, SentencePiece BPE, FP16/INT8 kernels, beam search, gRPC serving",
         "• Extended Summary: Infrastructure engineers run multi-GPU Horovod all-reduce training of custom seq2seq layers and compile FP16/INT8 quantized ONNX and TensorRT graphs to serve beam search at sub-20ms gRPC latency.\n"
         "• Use Cases & Landmarks: Google Search BERT production rollout (2019-10), high-QPS e-commerce neural machine translation, real-time speech and ad ranking, and custom domain encoder-decoder summarization.\n"
         "• User Actions: Training custom BPE and SentencePiece tokenizers, orchestrating multi-GPU Horovod/DDP all-reduce gradient synchronization, and compiling FP16/INT8 quantized ONNX/TensorRT computation graphs.\n"
         "• Models & Products: Transformer-Big seq2seq, OpenAI GPT-2 (1.5B), NVIDIA Megatron-LM, Facebook Fairseq, Google Tensor2Tensor, Microsoft ONNX Runtime 1.0 (2019), and NVIDIA TensorRT inference engine.\n"
         "• Surface & Hardware: Multi-node 8x–64x NVIDIA V100 DGX server clusters, NVLink and InfiniBand interconnects, custom CUDA/cuDNN kernels, and C++ gRPC microservices meeting strict sub-20ms 10,000-QPS SLAs.\n"
         "• Scope & Evolution: Scales beyond single-GPU L4 encoder tuning above to serve 10,000-QPS production traffic while operationalizing L6 Transformer architectures below; evolves rightward into DeepSpeed ZeRO and vLLM."),

        ("G0", 6, "Transformer Genesis", "Self-Attention Math, CommonCrawl Dedup, GLUE & GPT-3 Genesis",
         "Formulate scaled dot-product self-attention math, curate web corpora, and pretrain base models.",
         "self-attention math, QKV projections, positional encoding, Masked Language Modeling, CommonCrawl dedup, GLUE benchmark, SuperGLUE, pretraining",
         "• Extended Summary: Frontier scientists replace recurrent networks by deriving scaled dot-product self-attention over QKV projections, deduplicating CommonCrawl corpora, and creating GLUE and SuperGLUE benchmarks.\n"
         "• Use Cases & Landmarks: Vaswani et al. 'Attention Is All You Need' (2017-06), Devlin BERT Masked Language Modeling (2018-10), GLUE/SuperGLUE benchmark creation, and OpenAI GPT-2 / GPT-3 175B genesis.\n"
         "• User Actions: Deriving scaled dot-product self-attention math, writing MinHash LSH pipelines to deduplicate 300B-token CommonCrawl and C4 web corpora, and executing large-scale pretraining ablations.\n"
         "• Models & Products: Foundational Transformer, BERT-Large, RoBERTa, Raffel T5-11B, GPT-2 (1.5B), and GPT-3 (175B) base checkpoints; Wang GLUE (2018), SuperGLUE (2019), and SQuAD 2.0 unanswerable QA suites.\n"
         "• Surface & Hardware: Google Cloud TPU v2/v3 Pod slices and 1,000+ NVIDIA V100 superclusters backed by frontier lab compute budgets with custom distributed XLA and MPI pretraining harnesses.\n"
         "• Scope & Evolution: Supplies foundational Transformer architectures and weights consumed by L4 and L5 above; its GPT-3 scaling breakthroughs directly birth next-generation L1 autocomplete, L2 playgrounds, and L3 APIs."),

        ("G1", 1, "Ghost-Text Autocomplete", "IDE Ghost-Text Autocomplete & Viral Consumer Web Demos",
         "Accept inline gray code completions with a Tab keystroke or play viral browser art demos.",
         "ghost-text autocomplete, Tab-to-accept, GitHub Copilot, docstring-to-code, Craiyon web grid, DALL-E Mini, inline IDE plugin, zero-config demo",
         "• Extended Summary: Developers and casual users experience generative AI via inline gray ghost-text autocomplete inside IDEs using Tab-to-accept plugins and viral zero-config browser art grids like Craiyon.\n"
         "• Use Cases & Landmarks: GitHub Copilot Technical Preview (2021-06) and GA launch (2022-06, 1.2M developers), viral Craiyon / DALL-E Mini browser meme grids (2022-05), and AI Dungeon interactive stories.\n"
         "• User Actions: Coding normally in an IDE while pressing a single Tab keystroke to accept inline gray ghost-text completions, or typing three-word noun phrases into free public browser art demo boxes.\n"
         "• Models & Products: OpenAI Codex (code-cushman-001 12B completion model), Boris Dayma DALL-E Mini / Craiyon, EleutherAI GPT-J-6B web demos, AI Dungeon Dragon/Griffin, and Replika early companion app.\n"
         "• Surface & Hardware: VS Code and JetBrains GitHub Copilot IDE extensions, zero-config public web demo URLs, and background cloud GPU inference streaming inline code suggestions in under 200ms.\n"
         "• Scope & Evolution: Upgrades passive typo-fixers of the prior generation's L1 (left) into active generative IDE completion with zero prompt formatting vs L2 playgrounds below; evolves rightward into multi-turn chatbots."),

        ("G1", 2, "Few-Shot Prompting", "Few-Shot Completion Prompting & Stop-Sequence Crafting",
         "Format input-output exemplars, set stop sequences, and tune sampling sliders in web playgrounds.",
         "few-shot exemplars, stop sequences, completion prefixes, temperature slider, top-p nucleus sampling, token probabilities, Playground GUI, /imagine",
         "• Extended Summary: Power-users steer unaligned completion models in web playgrounds by formatting 3-to-5-shot input-output exemplars, setting stop sequences, and tuning temperature and top-p sampling sliders.\n"
         "• Use Cases & Landmarks: OpenAI GPT-3 Web Playground launch (2020-06), Jasper.ai and Copy.ai marketing copywriting boom, early Midjourney v1–v3 Discord art generation (2022-07), and ad-hoc text extraction.\n"
         "• User Actions: Crafting 3-to-5-shot Input:/Output: completion prefixes, configuring explicit stop=['\\n', '###'] sequences to prevent runaway continuation, and tuning temperature/top_p/frequency sliders.\n"
         "• Models & Products: OpenAI GPT-3 base/instruct series (davinci, curie, babbage, ada; text-davinci-002), Cohere Generate playground, AI21 Jurassic-1, Jasper.ai templates, and Midjourney v1–v3 Discord bot.\n"
         "• Surface & Hardware: OpenAI Web Playground GUI with token-probability highlighting, Notion AI alpha, Discord /imagine slash-command channels, and early PromptBase template marketplaces.\n"
         "• Scope & Evolution: Absorbs prior L2 CSV uploads and L3/L4 text classifiers (left) into a no-code playground without writing L3 Python backend code below; completion prefixes sink upward into next-gen L1 zero-shot chat."),

        ("G1", 3, "API Wrapper Calls", "REST API Completion Wrappers & Early FAISS Vector Search",
         "Wrap completion REST APIs in Python backends and index dense embeddings for vector search.",
         "completion API wrappers, dense embeddings, FAISS cosine search, prompt templates, GPT2Tokenizer, 2049-token window, Redis cache, FastAPI",
         "• Extended Summary: Application engineers build first-wave AI SaaS wrappers by interpolating user inputs into prompt templates via FastAPI backends, counting GPT2Tokenizer tokens, and indexing dense embeddings in FAISS.\n"
         "• Use Cases & Landmarks: First-wave SaaS AI copywriting, email summarization, and semantic product search startups (2021–2022), plus automated customer support ticket drafting and tagging microservices.\n"
         "• User Actions: Interpolating user inputs into few-shot prompt templates via REST SDKs, counting and truncating tokens under strict 2,049-token limits, and indexing dense embeddings for cosine lookup.\n"
         "• Models & Products: OpenAI completion (text-davinci-002) and embedding (text-search-ada) REST endpoints, Facebook FAISS dense vector index, and HuggingFace Hub hosted inference endpoints.\n"
         "• Surface & Hardware: Python and Node.js REST SDKs, FastAPI/Flask web backends, PostgreSQL + Redis caching layers, and GPT2TokenizerFast running on standard cloud CPU application servers.\n"
         "• Scope & Evolution: Productizes manual playground prompts of L2 above into web backends and replaces prior L4 BERT GPU servers (left), escalating multi-step reasoning to L4 below; evolves rightward into Vector-DB RAG."),

        ("G1", 4, "Linear Prompt Chains", "Multi-Step Prompt Chains, Self-Consistency & Cloud Fine-Tune CLI",
         "Chain sequential reasoning prompts, sample majority-vote paths, or upload JSONL fine-tune sets.",
         "linear prompt chains, Chain-of-Thought, self-consistency voting, pass@20 sampling, JSONL fine-tuning, calibration suites, W&B traces, asyncio",
         "• Extended Summary: AI engineers overcome single-call fragility by chaining sequential prompts, sampling 20 Chain-of-Thought paths for majority-vote self-consistency, or uploading JSONL datasets to fine-tune CLIs.\n"
         "• Use Cases & Landmarks: Stanford CS324 LLM course (2022-01), Wei et al. Chain-of-Thought (2022-01), Wang Self-Consistency voting (2022-03), Wu AI Chains (CHI 2022), and OpenAI Fine-Tuning CLI workflows.\n"
         "• User Actions: Decomposing complex tasks into sequential multi-call prompt chains, sampling 20 reasoning paths for majority-vote self-consistency, and curating 1,000+ JSONL pairs for cloud fine-tuning.\n"
         "• Models & Products: OpenAI code-davinci-002 and text-davinci-002, OpenAI Fine-Tune CLI (openai api fine_tunes.create), Google Flan-T5-XL, EleutherAI GPT-J-6B, and early Dust.tt / LangChain v0.0.1 chains.\n"
         "• Surface & Hardware: Python asyncio orchestration scripts, Weights & Biases evaluation dashboards, held-out calibration test suites, and cloud fine-tune CLIs or single A100/V100 GPU instances.\n"
         "• Scope & Evolution: Overcomes single-call limits of L3 API wrappers above via 20-path majority voting without sharding L5 multi-node GPU weights below; manual CoT scripts sink upward into next-gen L2 prompting."),

        ("G1", 5, "Distributed Trainers", "Distributed Multi-GPU Full-Weight LLM Fine-Tuning (DeepSpeed ZeRO)",
         "Shard optimizer states, gradients, and weights across multi-node GPU clusters with DeepSpeed.",
         "DeepSpeed ZeRO-3, 3D parallelism, tensor sharding, pipeline parallelism, activation checkpointing, InfiniBand RDMA, NCCL all-gather, Slurm",
         "• Extended Summary: Distributed systems engineers shard 6B–66B model weights, gradients, and FP32 optimizer states across multi-node GPU clusters using DeepSpeed ZeRO-3, 3D parallelism, and InfiniBand RDMA.\n"
         "• Use Cases & Landmarks: On-premise enterprise 6B–20B domain model training, BigScience BLOOM-176B open collaboration (2022-07), EleutherAI GPT-NeoX-20B, and CompVis Stable Diffusion v1.4 cluster runs.\n"
         "• User Actions: Configuring DeepSpeed ZeRO Stage 3 to shard FP32 optimizer states, gradients, and parameters across nodes, tuning tensor/pipeline parallelism, activation checkpointing, and Slurm jobs.\n"
         "• Models & Products: EleutherAI GPT-NeoX-20B, Meta OPT-30B/66B, BigScience BLOOM, Google Flan-T5-XXL, Microsoft DeepSpeed ZeRO, NVIDIA Megatron-LM, and HuggingFace Accelerate distributed trainers.\n"
         "• Surface & Hardware: Multi-node 8x–64x NVIDIA A100 (40GB/80GB) GPU clusters, 400Gbps InfiniBand RDMA fabrics, NCCL collective communications, and Slurm or Kubernetes cluster job schedulers.\n"
         "• Scope & Evolution: Shards 6B–66B full-weight models exceeding single-GPU memory at L4 above while operationalizing L6 scaling laws below; single-task domain tuning sinks upward into next-gen L4 single-GPU QLoRA."),

        ("G1", 6, "Scaling & RLHF Genesis", "Power-Law Scaling, InstructGPT RLHF, The Pile & HumanEval Genesis",
         "Derive neural scaling laws, align base models via 3-stage RLHF, and create HumanEval benchmarks.",
         "neural scaling laws, InstructGPT RLHF, PPO alignment, Bradley-Terry reward model, LoRA theory, HumanEval pass@k, MMLU benchmark, The Pile",
         "• Extended Summary: Research scientists formulate Kaplan power-law neural scaling laws, align raw completion models into helpful assistants via 3-stage InstructGPT RLHF and PPO, and invent LoRA theory and HumanEval.\n"
         "• Use Cases & Landmarks: Kaplan et al. Neural Scaling Laws (2020-01), Ouyang et al. InstructGPT 3-stage RLHF (2022-03), Bai Constitutional AI, Hu LoRA theory (2021-06), and OpenAI HumanEval code genesis.\n"
         "• User Actions: Deriving power-law compute allocation L(N,D,C), formulating Bradley-Terry preference reward models + KL-penalized PPO alignment, curating 825GB The Pile, and designing functional pass@k evals.\n"
         "• Models & Products: OpenAI GPT-3 175B, Codex 12B, InstructGPT (text-davinci-003), Google PaLM 540B, DeepMind Gopher; Hendrycks MMLU (2020), Chen HumanEval pass@k (2021), Cobbe GSM8K, and BIG-bench.\n"
         "• Surface & Hardware: 1,024–10,000x NVIDIA A100 frontier superclusters paired with global human preference annotation workforces and isolated sandboxed unit-test execution graders.\n"
         "• Scope & Evolution: Builds on the prior generation's L6 Transformer math (left) by adding 3-stage RLHF alignment and LoRA theory; directly births next-generation L1 consumer ChatGPT and L4 single-GPU LoRA tuning."),

        ("G2", 1, "Consumer Chatbots", "Zero-Shot Conversational Web Chat for Q&A, Summarization & Drafting",
         "Ask plain-English questions and iterate across multi-turn dialogs in zero-shot browser chat.",
         "zero-shot chat, multi-turn dialog, ChatGPT web app, conversational follow-up, instruction following, regenerate button, mobile voice chat, hallucination",
         "• Extended Summary: Mass-market users ask plain-English questions in a zero-shot browser or mobile chat box and refine answers through multi-turn dialog follow-ups without configuring completion prefixes or stop tokens.\n"
         "• Use Cases & Landmarks: OpenAI ChatGPT launch (2022-11-30, reaching 100M monthly users in 60 days), everyday essay and email drafting, code explanation, translation, and the Samsung source-code leak ban (2023-04).\n"
         "• User Actions: Typing natural plain-English questions and multi-turn conversational follow-ups ('make it shorter', 'fix this bug') in a web browser box with zero stop-sequence or prefix configuration.\n"
         "• Models & Products: OpenAI ChatGPT Free (gpt-3.5-turbo), Microsoft Bing Chat (Sydney), Google Bard (PaLM 2 / early Gemini), Anthropic Claude 2 web chat, and Character.ai consumer companion bots.\n"
         "• Surface & Hardware: chat.openai.com web browser tab and iOS/Android mobile apps backed by cloud-hosted RLHF instruction-tuned inference streaming at 40+ tokens per second to mass consumers.\n"
         "• Scope & Evolution: Absorbs prior L2 completion prefix and stop-token playgrounds (left) into a zero-study chat box while deferring structured personas to L2 below; evolves rightward into omni-modal chat and UI panes."),

        ("G2", 2, "Prompt Engineering", "System Personas, Manual Chain-of-Thought & Shareable Custom GPTs",
         "Craft structured system personas, XML delimiters, manual CoT triggers, and no-code Custom GPTs.",
         "prompt engineering, system role persona, XML delimiters, step-by-step CoT trigger, Custom GPT Store, Midjourney parameters, Perplexity citations, rubrics",
         "• Extended Summary: Power-users maximize output quality by writing structured system role personas, wrapping context in XML delimiters, appending step-by-step CoT triggers, and publishing shareable no-code Custom GPTs.\n"
         "• Use Cases & Landmarks: DeepLearning.AI Prompt Engineering course (Ng & Fulford, 2023-05), Mata v. Avianca hallucinated legal citation sanction (2023-05), OpenAI Custom GPT Store (2023-11), and Midjourney v5.\n"
         "• User Actions: Structuring system role personas ('Act as a senior auditor'), wrapping inputs in XML/Markdown delimiters, appending manual 'Let's think step by step' CoT triggers, and tuning Midjourney flags.\n"
         "• Models & Products: OpenAI GPT-4 (8k/32k), Anthropic Claude 2.1, Midjourney v5/v6 Discord bot, OpenAI DALL-E 3, Perplexity AI citation search, and shareable no-code OpenAI Custom GPTs with Actions.\n"
         "• Surface & Hardware: ChatGPT Plus web workspace, Custom GPT no-code builder UI, Discord /imagine slash-command flags (--ar 16:9 --v 6.0 --stylize), and shared team prompt template libraries.\n"
         "• Scope & Evolution: Adds system personas and manual step-by-step CoT triggers to L1 chat above and absorbs prior L4 prompt chains (left) without writing L3 RAG code below; manual CoT later sinks into L1 auto-reasoners."),

        ("G2", 3, "Chunked Vector RAG", "DIY Chunked Vector-DB RAG & JSON Function-Calling Internal Bots",
         "Split PDFs into overlapping text chunks, index HNSW vector stores, and wire JSON tool schemas.",
         "chunked vector RAG, HNSW vector index, text splitter overlap, top-k cosine retrieval, JSON function calling, LangChain, LlamaIndex, Pydantic schemas",
         "• Extended Summary: Software engineers overcome 4k–8k context limits by splitting PDFs into overlapping chunks, indexing embeddings into HNSW vector databases for top-k retrieval, and wiring Pydantic JSON function calling.\n"
         "• Use Cases & Landmarks: Enterprise internal wiki and HR 'Chat with Your PDFs' bots, the 2023 LangChain and LlamaIndex developer boom, OpenAI JSON Function Calling launch (2023-06), and cited doc Q&A pipelines.\n"
         "• User Actions: Splitting PDFs into 512-token overlapping chunks, indexing dense embeddings into HNSW vector stores, injecting top-k retrieved chunks into prompts, and wiring Pydantic JSON tool schemas.\n"
         "• Models & Products: OpenAI gpt-3.5-turbo-0613, gpt-4-0613, text-embedding-ada-002, Cohere Rerank v2; LangChain, LlamaIndex, Pinecone, ChromaDB, Weaviate, Milvus, Qdrant, and Pydantic schema validators.\n"
         "• Surface & Hardware: Python FastAPI, Streamlit, and Gradio web apps, managed cloud vector database consoles, and REST API keys running on standard developer laptops or lightweight cloud containers.\n"
         "• Scope & Evolution: Connects external PDFs and JSON APIs exceeding L2 prompt windows above and upgrades prior 2k-token wrappers (left) without training L4 GPU weights below; <50-PDF RAG sinks into L2 project folders."),

        ("G2", 4, "LoRA Adapter Tuning", "Single-GPU 4-Bit QLoRA Fine-Tuning & Early ReAct Agent Loops",
         "Quantize open weights to 4-bit NormalFloat, train LoRA adapters on one GPU, and run ReAct loops.",
         "4-bit QLoRA, NormalFloat NF4, low-rank adapters, PEFT SFTTrainer, Llama-2 open weights, ReAct agent loop, LLM-as-a-Judge, GGUF llama.cpp",
         "• Extended Summary: ML engineers quantize frozen Llama-2 or Mistral weights to 4-bit NormalFloat (NF4) to train low-rank LoRA adapters on one 24GB GPU while prototyping ReAct agent loops and LLM-as-a-Judge evals.\n"
         "• Use Cases & Landmarks: Dettmers et al. 4-Bit QLoRA paper (2023-05), Grammarly CoEdIT text-editing model (2023-05), Meta Llama-2 open-weight fine-tuning boom (2023-07), and viral AutoGPT / ReAct loops.\n"
         "• User Actions: Quantizing frozen base weights to 4-bit NormalFloat (NF4), training low-rank LoRA adapters (rank r=16..64, lora_alpha) on attention projections, and calibrating LLM-as-a-Judge eval suites.\n"
         "• Models & Products: Meta Llama-2 (7B / 13B / 70B), Mistral-7B-v0.1, Zephyr-7B, Flan-T5-Large (CoEdIT); HuggingFace PEFT, bitsandbytes, TRL SFTTrainer, Axolotl, Yao ReAct loops, and Ragas / TruLens evals.\n"
         "• Surface & Hardware: Single consumer NVIDIA RTX 3090/4090 (24GB VRAM) or cloud A100 GPU paired with local llama.cpp GGUF quantization and Ollama desktop inference model runners.\n"
         "• Scope & Evolution: Sinks prior L5 multi-node tuning (left) onto one 24GB GPU and extends L3 RAG above with custom style and ReAct loops while relying on L5 below for high-QPS serving; ReAct evolves into L4 state graphs."),

        ("G2", 5, "Paged Serving Clusters", "High-Throughput vLLM PagedAttention & Custom Domain Pretraining",
         "Page non-contiguous GPU KV-cache memory with vLLM and FlashAttention-2 for high-QPS serving.",
         "vLLM PagedAttention, KV-cache blocks, continuous batching, FlashAttention-2 SRAM, TensorRT-LLM, Mixtral MoE sharding, Triton server, TTFT SLAs",
         "• Extended Summary: Infrastructure teams eliminate GPU memory fragmentation by paging non-contiguous KV-cache blocks via vLLM PagedAttention, scheduling continuous batching, and compiling FlashAttention-2 SRAM kernels.\n"
         "• Use Cases & Landmarks: Kwon et al. vLLM PagedAttention (SOSP 2023, arXiv 2023-06), Dao FlashAttention-2 (2023-07), BloombergGPT 50B finance run (2023-03), and high-throughput enterprise GPU serving.\n"
         "• User Actions: Managing non-contiguous KV-cache memory blocks via PagedAttention, scheduling continuous iteration-level batching, compiling FlashAttention-2 SRAM kernels, and sharding 70B MoE endpoints.\n"
         "• Models & Products: Meta Llama-2-70B, Mixtral-8x7B sparse MoE, Falcon-180B, BloombergGPT-50B; vLLM serving engine, HuggingFace Text Generation Inference (TGI), NVIDIA TensorRT-LLM, and Ray Serve.\n"
         "• Surface & Hardware: Multi-node 8x–64x NVIDIA H100/A100 80GB GPU clusters, NVSwitch high-bandwidth interconnects, Triton Inference Server, Kubernetes GPU operators, and Prometheus TTFT/ITL telemetry.\n"
         "• Scope & Evolution: Serves open-weight models tuned at L4 above at 2–4x higher throughput via vLLM PagedAttention while applying FlashAttention kernels created at L6 below; evolves into containerized eval farms."),

        ("G2", 6, "Chinchilla & DPO Genesis", "Chinchilla Scaling, RoPE Long-Context, DPO, FineWeb & SWE-bench Genesis",
         "Derive compute-optimal Chinchilla scaling, closed-form DPO alignment, and RoPE context extension.",
         "Chinchilla scaling, Direct Preference Optimization, RoPE context extension, FineWeb 15T corpus, Chatbot Arena Elo, SWE-bench, GPQA Diamond, MoE",
         "• Extended Summary: Frontier researchers establish Chinchilla 20-tokens-per-parameter scaling, replace unstable PPO critics with closed-form Direct Preference Optimization (DPO), and extend RoPE to 1M+ tokens.\n"
         "• Use Cases & Landmarks: Hoffmann Chinchilla compute-optimal scaling (20 tok/param), Rafailov Direct Preference Optimization (DPO, 2023-05), RoPE context extension, LMSYS Chatbot Arena, and SWE-bench.\n"
         "• User Actions: Formulating closed-form DPO implicit reward losses (eliminating separate PPO critic networks), interpolating RoPE frequencies to 128k–2M context, and deduplicating 15T-token FineWeb corpora.\n"
         "• Models & Products: OpenAI GPT-4 / GPT-4V, Anthropic Claude 2 and Claude 3 family, Meta Llama-2/3; RedPajama, AI2 Dolma, and HuggingFace FineWeb datasets; LMSYS Chatbot Arena Elo, SWE-bench, and GPQA Diamond.\n"
         "• Surface & Hardware: 4,000–25,000x NVIDIA H100 / A100 superclusters interconnected via 3.2Tbps InfiniBand fabrics with automated synthetic data generation and quality-classifier filtering pipelines.\n"
         "• Scope & Evolution: Replaces unstable PPO alignment of the prior generation's L6 (left) with closed-form DPO and RoPE long-context scaling; directly unlocks next-gen L1 omni-chat, L2 1M-token folders, and L4 DPO tuning."),

        ("G3", 1, "Multimodal Omni-Chat", "Built-In Multimodal Omni-Chat (Voice/Vision/Image) & Live Artifacts",
         "Converse via real-time voice and live camera while remixing interactive UI apps side-by-side.",
         "omni-modal voice/vision, Claude Artifacts, ChatGPT Canvas, live UI preview pane, WebRTC camera stream, screenshot-to-code, SVG/React remix, 320ms audio",
         "• Extended Summary: Everyday users talk with low-latency omni-modal voice, point smartphone cameras at live objects, or paste screenshots while interactively remixing live React and SVG apps in a side-by-side UI canvas.\n"
         "• Use Cases & Landmarks: OpenAI GPT-4o omni-modal launch (2024-05, 320ms real-time voice/camera), Anthropic Claude 3.5 Sonnet + Live Artifacts UI pane (2024-06), and OpenAI ChatGPT Canvas (2024-10).\n"
         "• User Actions: Speaking naturally with low-latency voice, pointing a smartphone camera at live objects, pasting UI screenshots, and interactively remixing live React / Tailwind / SVG apps in a side-by-side pane.\n"
         "• Models & Products: OpenAI GPT-4o (omni text-audio-vision), Anthropic Claude 3.5 Sonnet (20240620) with Artifacts, Google Gemini 1.5 Flash Live, and Meta Llama 3.1 consumer web and mobile assistants.\n"
         "• Surface & Hardware: Default consumer web and mobile chat apps equipped with sandboxed browser iframe preview panes (Artifacts / Canvas) and real-time WebRTC audio and video camera streaming.\n"
         "• Scope & Evolution: Upgrades text-only chatbots of the prior generation's L1 (left) with native voice, camera vision, and live UI preview panes while multi-PDF grounding stays at L2 below; evolves into auto-reasoners."),

        ("G3", 2, "Long-Context Projects", "Drag-and-Drop 50-PDF Long-Context Workspaces & Audio Synthesis",
         "Drag and drop fifty full PDFs into million-token cloud project folders with grounded citations.",
         "million-token context, Claude Projects, Gemini 2M window, NotebookLM Audio Overview, drag-and-drop folders, grounded citations, KV-cache pinning, zero-RAG",
         "• Extended Summary: Power-users bypass Python vector databases by dragging 50+ full PDFs or slide decks into persistent 200k–2M token cloud project folders for grounded cross-document Q&A and NotebookLM audio synthesis.\n"
         "• Use Cases & Landmarks: Anthropic Claude Projects launch (2024-06, 200k context workspaces), Google Gemini 1.5 Pro 1M–2M context window, and the viral Google NotebookLM Audio Overviews wave (2024-09).\n"
         "• User Actions: Dragging and dropping 20–100 full PDFs, slide decks, or code files into persistent cloud project folders, writing workspace-wide custom instructions, and auditing inline source citations.\n"
         "• Models & Products: Google Gemini 1.5 Pro (2M token context), Anthropic Claude 3.5 Sonnet Projects (200k context), OpenAI GPT-4o (128k context), and Google NotebookLM two-host audio synthesis studio.\n"
         "• Surface & Hardware: Cloud workspace folders with direct Google Drive and Notion sync, persistent KV-cache context memory, and one-click AI podcast generation with zero Python or vector database setup.\n"
         "• Scope & Evolution: Absorbs prior L3 Python Vector-RAG chunking scripts for <50 PDFs (bottom-left) into drag-and-drop cloud folders above L3 IDE coding; passive folder Q&A evolves rightward into L2 Deep Research agents."),

        ("G3", 3, "Vibe Coding", "AI-Native IDE Multi-File Vibe Coding & Guardrailed Enterprise RAG",
         "Prompt multi-file repository diffs in AI-native IDEs and wire guardrailed enterprise RAG.",
         "vibe coding, Cursor Composer, .cursorrules manifest, multi-file repo diffs, prompt caching, hybrid BM25+vector RAG, Colang guardrails, Windsurf IDE",
         "• Extended Summary: Developers adopt AI-native IDEs like Cursor and Windsurf to prompt multi-file repository diffs via Composer and .cursorrules while deploying prompt-cached, RBAC-guardrailed hybrid enterprise RAG.\n"
         "• Use Cases & Landmarks: Anysphere Cursor IDE Composer and .cursorrules boom (2024-06), Karpathy 'Vibe Coding' paradigm, Anthropic 90% Prompt Caching discount (2024-08), and RBAC-enforced enterprise RAG.\n"
         "• User Actions: Prompting multi-file repository diffs via Cmd+K / Composer using @codebase indexing and .cursorrules, accepting coupled build-and-run outputs by taste, and wiring Colang/RBAC retrieval rails.\n"
         "• Models & Products: Claude 3.5 Sonnet v1/v2, OpenAI GPT-4o-mini, Cursor IDE, Codeium Windsurf, V0.dev, Bolt.new, NVIDIA NeMo Guardrails (Colang), Cohere Rerank 3, and Anthropic Prompt Caching.\n"
         "• Surface & Hardware: AI-native VS Code forks (Cursor / Windsurf), .cursorrules repo manifests, hybrid BM25 + pgvector/Pinecone ACL indices, and prompt-cached API endpoints on developer laptops.\n"
         "• Scope & Evolution: Upgrades prior L1/L3 single-file coding into multi-file AI IDE app generation and adds RBAC guardrails to L2 folders above; stateful workflows that break under vibe coding escalate down to L4 graphs."),

        ("G3", 4, "State-Machine Graphs", "Stateful Cyclic Agent Graphs (LangGraph) & HITL Checkpoints",
         "Architect cyclic multi-agent state graphs with persistent checkpoints and human approval gates.",
         "cyclic StateGraphs, LangGraph, typed state schemas, conditional routing edges, Postgres checkpointers, HITL interrupt gates, DPO tuning, trace observability",
         "• Extended Summary: AI engineers bound agent loop drift by architecting explicit cyclic StateGraphs in LangGraph with typed schemas, conditional routing edges, PostgreSQL checkpointers, and human approval interrupts.\n"
         "• Use Cases & Landmarks: LangChain LangGraph v0.1/v0.2 production rollout (2024), Anthropic 'Building Effective Agents' blueprint (Schluntz & Zhang, 2024-12), and stateful enterprise refund/triage workflows.\n"
         "• User Actions: Architecting explicit cyclic StateGraphs with typed state schemas, conditional routing edges, Postgres state checkpointers, human-in-the-loop interrupt_before gates, and DPO preference tuning.\n"
         "• Models & Products: LangGraph, CrewAI, Microsoft AutoGen v0.4, LlamaIndex Workflows, Anthropic Claude 3.5 Sonnet, OpenAI GPT-4o, HuggingFace TRL Direct Preference Optimization (DPO), and LangSmith.\n"
         "• Surface & Hardware: Python StateGraph SDKs, PostgreSQL persistent state checkpointers, LangSmith and Arize Phoenix trace observability dashboards, and Docker containers or single-GPU DPO rigs.\n"
         "• Scope & Evolution: Bounds brittle ReAct loops of the prior generation's L4 (left) and multi-step failures of L3 vibe coding above with explicit checkpoints and human gates; web-research graphs sink into L2 Deep Research."),

        ("G3", 5, "Evaluator Harnesses", "Multi-Agent Repo Orchestration & Containerized Eval Harnesses",
         "Provision Kubernetes Docker-in-Docker container farms to verify parallel repo patch trajectories.",
         "container eval farms, Docker-in-Docker, SWE-bench Verified, orchestrator-workers, parallel pytest sandboxes, trajectory harvesting, vLLM cluster, CI/CD",
         "• Extended Summary: Infrastructure engineers provision Kubernetes Docker-in-Docker evaluation farms to execute parallel orchestrator-worker code patches against isolated pytest suites and harvest verified RL trajectories.\n"
         "• Use Cases & Landmarks: SWE-bench Verified jump from 33% to 49% on Claude 3.5 Sonnet v2 (2024-10), Anthropic Orchestrator-Workers pattern (2024-12), and enterprise containerized CI/CD patch verification.\n"
         "• User Actions: Provisioning Kubernetes Docker-in-Docker evaluation farms, running parallel orchestrator-worker repo patches against isolated pytest suites, and harvesting verified trajectories for DPO and RL.\n"
         "• Models & Products: Anthropic Claude 3.5 Sonnet v2 (20241022), OpenAI o1-preview (2024-09), Princeton SWE-agent, AllHands / OpenDevin, vLLM multi-node inference clusters, and SWE-bench Docker harnesses.\n"
         "• Surface & Hardware: Kubernetes Docker-in-Docker container farms, multi-node 8x–64x NVIDIA H100 inference clusters, GitHub Actions matrix runners, and distributed trajectory replay stores.\n"
         "• Scope & Evolution: Scales L4 agent orchestration above into parallel Kubernetes Docker-in-Docker verification farms while supplying verified traces to L6 RLVR below; single-repo Docker TDD sinks into L3/L4 coding CLIs."),

        ("G3", 6, "RLVR & Protocol Genesis", "Omni-Tokenization, Ring Attention, RLVR/GRPO & MCP Spec Genesis",
         "Formulate critic-free GRPO over verifiable execution rewards, Ring Attention, and the MCP spec.",
         "RLVR verifiable rewards, critic-free GRPO, test-time compute scaling, Ring Attention, Multi-head Latent Attention, omni-tokenization, MCP v1.0, OSWorld",
         "• Extended Summary: Frontier scientists unlock test-time reasoning by inventing critic-free Group Relative Policy Optimization (GRPO) trained on verifiable code/math execution rewards (RLVR) alongside the MCP v1.0 spec.\n"
         "• Use Cases & Landmarks: Shao et al. DeepSeekMath GRPO (2024-02), Snell Test-Time Compute Scaling (2024-08), OpenAI o1 RLVR preview (2024-09), Lambert Tulu 3 RLVR, and Anthropic MCP spec genesis (2024-11).\n"
         "• User Actions: Formulating critic-free Group Relative Policy Optimization (GRPO) over execution-verified math/code rewards (RLVR), Ring Attention across 1M–2M tokens, and early-fusion omni-tokenization.\n"
         "• Models & Products: OpenAI o1-preview/o1, GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, Meta Llama-3.1-405B, and DeepSeek-V3; SWE-bench Verified (500 human-filtered tasks), OSWorld GUI benchmark, and MCP v1.0.\n"
         "• Surface & Hardware: 16,000–50,000x NVIDIA H100/H200 superclusters coupled with massively parallel sandboxed code and math execution verifiers and Multi-head Latent Attention KV compression.\n"
         "• Scope & Evolution: Extends prior L6 DPO alignment (left) into critic-free GRPO over verifiable rewards (RLVR) and defines the MCP standard; directly births next-gen L1 auto-reasoners, L3 MCP wiring, and L5 GRPO clusters."),

        ("G4", 1, "Auto-Routed Reasoners", "Zero-Shot Auto-Thinking Chat (RLVR Router) & Interactive MCP Apps",
         "Ask complex queries once as hidden routers allocate thinking tokens and render in-chat MCP apps.",
         "auto-thinking router, hidden reasoning tokens, DeepSeek-R1 app, GPT-5.4 Auto-Router, DeepThink toggle, interactive MCP App cards, zero-CoT chat, AAIF",
         "• Extended Summary: Default consumer chat apps use hidden routers to inspect query difficulty, automatically allocate test-time RLVR reasoning tokens without manual CoT prompting, and render interactive MCP App UI cards.\n"
         "• Use Cases & Landmarks: DeepSeek-R1 viral consumer app wave (2025-01), OpenAI GPT-5 / GPT-5.4 unified Auto-Router (2025–2026), and Linux Foundation AAIF Interactive MCP Apps embedded inside chat (2025-12).\n"
         "• User Actions: Asking complex math, coding, legal, or travel planning queries in plain language while a hidden router silently allocates test-time RLVR thinking tokens and renders interactive UI cards.\n"
         "• Models & Products: OpenAI GPT-5 / GPT-5.4 Auto-Router, DeepSeek-R1 consumer app, Anthropic Claude Sonnet 4.6 / Opus 5.5, Google Gemini 3.5 Flash, and in-chat AAIF MCP interactive widget cards.\n"
         "• Surface & Hardware: Default consumer web and mobile chat apps with zero-config automatic thinking-budget routing, collapsible chain-of-thought drawers, and sandboxed MCP App UI surfaces.\n"
         "• Scope & Evolution: Absorbs manual Chain-of-Thought prompting from prior L2/L4 cells (left) into an automatic consumer router above L2 while rendering L3 MCP cards; defers 100-source browsing to L2 Deep Research below."),

        ("G4", 2, "Deep Research Agents", "Autonomous Multi-Site Deep Research Scoping & Citation Auditing",
         "Scope Socratic research briefs as autonomous web agents browse 100+ sources into cited reports.",
         "Deep Research agents, Socratic brief scoping, multi-hop web browsing, reasoning effort toggles, provenance matrices, citation verification, 100-source dossiers",
         "• Extended Summary: Power-users answer brief Socratic scoping questions and set reasoning-effort toggles before dispatching autonomous Deep Research agents to browse 50–150 web sources into cited dossiers.\n"
         "• Use Cases & Landmarks: OpenAI Deep Research launch (2025-02), Google Gemini Deep Research, and Perplexity Deep Research; autonomous 15-minute multi-hop web browsing across 50–150 sources into cited dossiers.\n"
         "• User Actions: Scoping research briefs via Socratic pre-execution clarification interviews, setting test-time compute effort toggles (Standard / High / xHigh), and auditing claim-to-source provenance tables.\n"
         "• Models & Products: OpenAI o3 / GPT-5.4 Deep Research, Google Gemini 3.5 Deep Research, Anthropic Claude Research with workspace connectors, and Perplexity Pro autonomous multi-hop research agents.\n"
         "• Surface & Hardware: Built-in Deep Research web workspace panels, live multi-hop browsing trajectory drawers, reasoning-effort budget selectors, and exported Markdown/PDF citation provenance matrices.\n"
         "• Scope & Evolution: Sinks prior L4 custom web-research LangGraph pipelines (bottom-left) into a built-in power-user panel above L3 and upgrades passive L2 PDF folders (left); escalates to L3 below when tool writes are needed."),

        ("G4", 3, "MCP Tool Integration", "Plug-and-Play MCP Tool Wiring (.mcp.json) & Guardrailed Agentic Bots",
         "Declare .mcp.json servers to connect databases and repos while delegating tasks to CLI agents.",
         "Model Context Protocol, .mcp.json manifests, AAIF standard, AGENTS.md, stdio/SSE tool servers, OAuth 2.1 scopes, Llama Guard rails, CLI delegation",
         "• Extended Summary: Integrators replace bespoke per-vendor API glue by declaring standardized .mcp.json servers (stdio/SSE) to connect Postgres, Jira, and GitHub under OAuth 2.1 scopes while delegating tasks to CLI agents.\n"
         "• Use Cases & Landmarks: Linux Foundation Agentic AI Foundation (AAIF, 2025-12: MCP + goose + AGENTS.md), Salesforce Headless 360 (4.5M MCP ops), and MIT NANDA/Menlo enterprise adoption (76% off-the-shelf).\n"
         "• User Actions: Declaring .mcp.json servers (stdio/SSE) to connect Postgres, Jira, and GitHub, enforcing OAuth 2.1 scopes + Llama Guard 3 safety rails, and delegating happy-path tasks to terminal CLI agents.\n"
         "• Models & Products: Model Context Protocol (MCP), Block goose, OpenAI AGENTS.md standard, Anthropic Claude Desktop / Code, Cursor MCP client, Meta Llama Guard 3, and Scale AI MCP Atlas benchmark.\n"
         "• Surface & Hardware: .mcp.json configuration manifests, Dockerized MCP tool servers, AI IDE and CLI terminal delegates, and enterprise API gateways running on standard developer workstations.\n"
         "• Scope & Evolution: Replaces bespoke per-vendor JSON wrappers of prior L3 cells (left) with universal .mcp.json servers and delegates happy-path coding above L4; private multi-file repos escalate down to L4 test oracles."),

        ("G4", 4, "Terminal Coding Agents", "Autonomous Terminal CLI Coding & Decoupled Verification Harnesses",
         "Author CLAUDE.md invariants and decoupled property-based test oracles for terminal CLI agents.",
         "Claude Code CLI, Codex CLI, CLAUDE.md invariants, harness engineering, decoupled test oracles, property-based testing, /compact hygiene, SWE-bench Pro",
         "• Extended Summary: Harness engineers govern terminal agents (Claude Code, Codex CLI) on private repos by authoring CLAUDE.md architectural invariants, managing /compact hygiene, and building decoupled test oracles.\n"
         "• Use Cases & Landmarks: Anthropic Claude Code CLI launch (2025-02), Scale AI SWE-bench Pro private-repo audit (2025-09: 70%+ public vs 23–46% private), UVA CS 6501 Agentic AI, and LangChain Deep Agents.\n"
         "• User Actions: Authoring CLAUDE.md architectural invariants, orchestrating multi-file bash / edit / grep CLI loops, managing /compact context hygiene, and building decoupled property-based Docker test oracles.\n"
         "• Models & Products: Anthropic Claude Code CLI, OpenAI Codex CLI, Block goose, Claude Opus 5.5 (96% Verified / 58% Pro), OpenAI GPT-5.4 (57% Pro), Muse Spark 1.1, Laguna S 2.1, and Hypothesis property tests.\n"
         "• Surface & Hardware: macOS and Linux terminal shells, isolated local Docker test containers, Git branch/worktree checkouts, and decoupled pytest / vitest / Hypothesis verification oracle suites.\n"
         "• Scope & Evolution: Catches silent corruption missed by L3 vibe/CLI coding above using decoupled property-based test oracles and absorbs prior L5 Docker TDD loops; unisolated 24/7 daemons escalate to L5 sandboxes below."),

        ("G4", 5, "Sandbox & RLVR Hosts", "24/7 Dedicated M4 Mac Mini OpenClaw Sandboxes & GRPO RLVR Clusters",
         "Air-gap 24/7 autonomous agent daemons on dedicated hardware or train multi-GPU GRPO verifiers.",
         "OpenClaw daemon, M4 Mac Mini sandbox, air-gapped VLAN, CVE-2026-30616 remediation, git worktree swarms, verl GRPO training, OpenRLHF, H200 clusters",
         "• Extended Summary: Systems architects physically air-gap 24/7 OpenClaw agent daemons on dedicated M4 Mac Minis with VLAN containment after 200k MCP RCEs, or run multi-GPU verl/OpenRLHF GRPO post-training on H200 clusters.\n"
         "• Use Cases & Landmarks: April 2026 OX Security disclosure of 200,000+ vulnerable stdio MCP instances (CVE-2026-30616 RCEs) triggering the dedicated M4 Mac Mini OpenClaw sandbox wave and domain GRPO RLVR.\n"
         "• User Actions: Physically air-gapping 24/7 autonomous agents on dedicated hardware with VLAN/credential containment, orchestrating parallel git worktree subagent swarms, and running multi-GPU GRPO post-training.\n"
         "• Models & Products: OpenClaw 24/7 autonomous daemon, Computer Use GUI agents (78.4% OSWorld), DeepSeek-R1 / Qwen3.8-Flash-Next open weights, and verl / OpenRLHF distributed GRPO RLVR training.\n"
         "• Surface & Hardware: Dedicated physical Apple M4 Mac Mini appliances on isolated VLANs for containment, or multi-node 8x–64x NVIDIA H200/B200 GPU clusters for domain GRPO RLVR post-training.\n"
         "• Scope & Evolution: Physically isolates L3/L4 CLI agents above onto air-gapped hardware after MCP RCE disclosures while sinking prior L6 GRPO training (bottom-left) into open H200 recipes; evolves into nightly enclave RLVR."),

        ("G4", 6, "Frontier Base Genesis", "Pure-RL Reasoning Emergence, Synthetic Flywheels & SWE-bench Pro Genesis",
         "Pretrain frontier models via pure-RL reasoning emergence and million-container synthetic flywheels.",
         "pure-RL emergence, DeepSeek-R1-Zero, synthetic RLVR flywheels, SWE-bench Pro, MCP Atlas, Terminal-Bench 2.0, aux-loss-free MoE, Blackwell B200",
         "• Extended Summary: Frontier scientists overcome the web-text data wall via DeepSeek-R1-Zero pure-RL cold-start emergence, generating trillions of execution-verified code/math/Lean-4 trajectories on container farms.\n"
         "• Use Cases & Landmarks: DeepSeek-R1-Zero pure-RL reasoning emergence (2025-01), Scale AI SWE-bench Pro (1,865 public+private commercial repo tasks, 2025-09), and MCP Atlas / Terminal-Bench 2.0 genesis.\n"
         "• User Actions: Training base models via pure RLVR cold-start emergence, generating multi-trillion synthetic verified code / math / Lean-4 trajectories across million-container farms, and aux-loss-free MoE routing.\n"
         "• Models & Products: DeepSeek-R1 (671B MoE), OpenAI o3 / GPT-5.4, Anthropic Claude Opus 4.6 / 5.5, Google Gemini 3.5 Pro; Scale SWE-bench Pro, MCP Atlas, Terminal-Bench 2.0, and Humanity's Last Exam (HLE).\n"
         "• Surface & Hardware: 25,000–100,000+ NVIDIA Blackwell B200 / H200 superclusters backed by frontier lab compute budgets and planetary-scale container verification factories on high-speed fabrics.\n"
         "• Scope & Evolution: Scales prior L6 RLVR math (left) into pure-RL reasoning emergence and million-container synthetic flywheels; supplies foundation weights and SWE-bench Pro evals for L1–L5 above and Gen 5 to the right."),

        ("G5", 1, "Ambient OS Delegates", "[Speculative Gen 5] Ambient Cross-App OS Delegation & Persistent Memory",
         "State high-level life or work outcomes once as ambient OS daemons coordinate apps via 1-tap cards.",
         "ambient OS delegate, persistent memory graph, 1-tap approval card, cross-app orchestration, on-device NPU silicon, zero app-switching, AAIF OS fabric",
         "• Extended Summary: [Speculative] Consumers state high-level life or work outcomes once while an ambient OS daemon with a local NPU memory graph coordinates across mail, calendar, and banking via 1-tap approval cards.\n"
         "• Use Cases & Landmarks: [Speculative: 2027-03–2028-12] OS-level background life and work delegation ('reconcile taxes, rebook delayed flights, synthesize 50 threads') via 1-tap approval notification cards.\n"
         "• User Actions: Speaking or typing high-level outcome intent once while the ambient OS daemon coordinates across mail, calendar, banking, and travel apps asynchronously with zero manual app-switching.\n"
         "• Models & Products: Projected GPT-6 / Claude 6 / Gemini 4 Ambient OS Routers, native Apple / Windows / Android AAIF MCP OS fabrics, and local-first encrypted personal cross-app memory graph daemons.\n"
         "• Surface & Hardware: Hybrid on-device NPU silicon (50+ TOPS local privacy-preserving memory graph) paired with cloud RLVR reasoning bursts and OS lock-screen 1-tap approval notification cards.\n"
         "• Scope & Evolution: [Speculative] Sinks prior L2 Deep Research scoping and L3 single-app MCP actions (left) into a zero-study background OS layer; custom multi-table software creation escalates down to L2 cloud spec studios."),

        ("G5", 2, "Natural-Language Specs", "[Speculative Gen 5] Natural-Language Cloud Spec Studios & Socratic Rubrics",
         "Author plain-English acceptance rubrics in cloud studios to wire and deploy verified web apps.",
         "declarative outcome specs, Socratic rubric interviews, zero-CLI cloud studio, 1-click OAuth MCP store, ephemeral preview URLs, behavioral diff review",
         "• Extended Summary: [Speculative] Analysts ship verified multi-table cloud apps without a terminal by answering Socratic constraint interviews, authoring plain-English rubrics, and approving live behavioral diffs.\n"
         "• Use Cases & Landmarks: [Speculative: 2027-03–2028-12] Domain analysts, PMs, and designers shipping verified multi-table web apps and reviewing async background PRs without opening a terminal.\n"
         "• User Actions: Answering Socratic AI constraint-elicitation interviews, authoring plain-English acceptance rubrics, toggling 1-click OAuth MCP store connectors, and approving live cloud behavioral diffs.\n"
         "• Models & Products: Projected Cloud Specification Studios (Next-Gen Cursor Cloud / Replit / Claude Studio), 1-Click AAIF Verified MCP App Stores, and automated background PR verification agents.\n"
         "• Surface & Hardware: Browser-based declarative specification canvases, auto-provisioned ephemeral Docker preview URLs, and visual side-by-side behavioral diff inspection workspaces in the cloud.\n"
         "• Scope & Evolution: [Speculative] Absorbs prior L3 .mcp.json wiring and happy-path CLI coding (bottom-left) into a no-terminal cloud studio above L3; cross-vendor governance and FinOps budget caps escalate down to L3."),

        ("G5", 3, "Agent-to-Agent Contracts", "[Speculative Gen 5] Cross-Vendor A2A Contracts, Cedar/OPA Policy & FinOps Caps",
         "Govern cross-vendor agent fleets with cryptographic A2A contracts, policy rails, and FinOps caps.",
         "Agent-to-Agent contracts, MCP v2 registry, AWS Cedar policy, Open Policy Agent, cryptographic audit ledgers, FinOps circuit breakers, shadow replay",
         "• Extended Summary: [Speculative] Enterprise integrators govern cross-vendor agent fleets via MCP v2 and Agent-to-Agent (A2A) identity contracts, deterministic Cedar/OPA policy rails, and FinOps circuit breakers.\n"
         "• Use Cases & Landmarks: [Speculative: 2027-03–2028-12] Cross-company and cross-department autonomous supply-chain procurement, compliance auditing, and IT incident resolution governed by formal A2A contracts.\n"
         "• User Actions: Wiring cross-vendor Agent-to-Agent (A2A) and MCP v2 identity contracts, writing deterministic AWS Cedar / Open Policy Agent (OPA) authorization rails, and setting FinOps token circuit breakers.\n"
         "• Models & Products: Linux Foundation AAIF MCP v2 + A2A Protocol, AWS Cedar / Open Policy Agent (OPA) policy-as-code engines, hardware-attested OAuth 2.1 agent tokens, and FinOps telemetry gateways.\n"
         "• Surface & Hardware: Enterprise Agent Registries, cryptographic tool-call audit ledgers, and shadow-mode counterfactual replay gateways running on cloud governance and security control planes.\n"
         "• Scope & Evolution: [Speculative] Upgrades prior L3 stdio MCP configs (left) with cryptographic A2A contracts and Cedar/OPA policy rails above L4; 500k-line monolith refactors escalate down to L4 formal proof swarms."),

        ("G5", 4, "Verified Agent Swarms", "[Speculative Gen 5] Formal Proof Oracles (Lean 4 / TLA+) & Digital-Twin Swarms",
         "Choreograph parallel agent swarms verified against Lean 4 / TLA+ formal proofs and digital twins.",
         "formal proof oracles, Lean 4 invariants, TLA+ state machines, Rust Kani verifier, digital-twin simulation, red-vs-blue fuzzing, git-worktree swarms",
         "• Extended Summary: [Speculative] Verification engineers choreograph 20-agent parallel git-worktree swarms stress-tested against machine-checked Lean 4 and TLA+ formal proof oracles and digital-twin simulators.\n"
         "• Use Cases & Landmarks: [Speculative: 2027-03–2028-12] Refactoring 500k+ line private commercial monoliths and verifying distributed financial and medical state machines via 20-agent parallel swarms.\n"
         "• User Actions: Specifying machine-checked formal invariants (Lean 4 / TLA+ / Rust Kani), architecting stateful digital-twin mock environments, and running adversarial red-team vs blue-team fuzzing swarms.\n"
         "• Models & Products: Formal proof verifier compilers (Lean 4, TLA+, Rust Kani, Hypothesis), multi-repo git-worktree swarm choreographers, and ultra-low-cost high-speed formal verifier reasoners.\n"
         "• Surface & Hardware: Deterministic digital-twin simulation containers, parallel git-worktree verification farms, and automated adversarial mutation-testing server clusters in cloud enclaves.\n"
         "• Scope & Evolution: [Speculative] Upgrades prior L4 empirical unit-test harnesses (left) into machine-checked Lean 4 / TLA+ proof oracles and digital twins above L5; distilling swarm traces into weights escalates to L5."),

        ("G5", 5, "Continuous RLVR Loops", "[Speculative Gen 5] Hardware-Enclaved Sovereign Clusters & Nightly RLVR Loops",
         "Distill verified daytime agent traces into sovereign model weights via nightly enclave RLVR loops.",
         "nightly on-policy RLVR, confidential compute TEEs, sovereign GPU enclaves, trajectory distillation, failure-mode curricula, zero-trust racks, Rubin GPUs",
         "• Extended Summary: [Speculative] Sovereign cluster architects operate confidential compute TEE enclaves that distill verified daytime agent traces into updated domain model weights via nightly on-policy RLVR.\n"
         "• Use Cases & Landmarks: [Speculative: 2027-03–2028-12] Nightly self-improving enterprise and scientific domain models trained continuously on verified daytime agent execution traces inside hardware enclaves.\n"
         "• User Actions: Operating continuous nightly on-policy RLVR/GRPO weight distillation pipelines, curating automated failure-mode curricula, and managing hardware-attested confidential compute enclaves.\n"
         "• Models & Products: Continuous on-policy RLVR flywheel engines, domain-specific world-model execution simulators, and TPM/TEE hardware-enclaved sovereign enterprise agent cluster appliances.\n"
         "• Surface & Hardware: Sovereign multi-node NVIDIA Blackwell / Rubin GPU clusters paired with hardware-attested confidential compute TEEs and zero-trust air-gapped execution sandbox server racks.\n"
         "• Scope & Evolution: [Speculative] Upgrades prior L5 batch GRPO training and static sandboxes (left) into nightly on-policy weight distillation inside sovereign enclaves, bridging L4 swarm traces above with L6 below."),

        ("G5", 6, "World-Model Genesis", "[Speculative Gen 5] Causal World-Model Theory, Self-Play & Next-Era Pretraining",
         "Formulate continual-plasticity architectures, causal physical world models, and self-play loops.",
         "causal world models, continual plasticity, open-ended self-play, non-forgetting updates, wet-lab robotics loop, ARC-AGI-3, SciGym, Lean-5 oracle",
         "• Extended Summary: [Speculative] Foundational scientists formulate continual-plasticity architectures and causal physical world models coupled with robotic and wet-lab simulators for open-ended scientific self-play.\n"
         "• Use Cases & Landmarks: [Speculative: 2027-03–2028-12] Formulating post-Transformer continual-plasticity architectures, causal physical world models, and open-ended scientific self-play discovery.\n"
         "• User Actions: Deriving non-forgetting continual weight-update math, coupling planetary-scale wet-lab / robotic / Lean-5 simulators into closed-loop self-play curricula, and designing un-gamed frontier benchmarks.\n"
         "• Models & Products: Next-era causal physical world models, autonomous scientific hypothesis-to-lab discovery loops, and un-gamed physical and mathematical evaluation suites (ARC-AGI-3 / SciGym / Lean-5).\n"
         "• Surface & Hardware: 100,000+ NVIDIA Rubin / Google TPU v7 exascale superclusters backed by frontier lab compute budgets and integrated with automated robotic and physics simulation fabrics.\n"
         "• Scope & Evolution: [Speculative] Extends prior L6 synthetic text/code flywheels (left) into continual-plasticity architectures and physical world models, powering L1–L5 above and post-2029 paradigms beyond the chart."),

    ]
    df_poster = pd.DataFrame(poster_cells, columns=[
        "gen_id", "level_id", "cell_name", "short_header", "plain_desc", "keywords_1line", "encyclopedic_body"
    ])
    poster_path = os.path.join(CACHE_DIR, "v4_poster_encyclopedic_cells.csv")
    df_poster.to_csv(poster_path, index=False)
    print(f"[SAVED] {poster_path} | shape={df_poster.shape}")

    # =========================================================================
    # SECTION 1.4 DETERMINISTIC DATA VALIDATION GATES (PROGRAMMATIC ASSERTS)
    # =========================================================================
    print("\n[VALIDATION GATES] Running Section 1.4 Programmatic Assertions across all 36 v4 Cells (G0..G5 x L1..L6)...")

    req_cols = [
        'gen_id', 'level_id', 'status', 'learning_hours', 'hardware_cap_usd',
        'level_bracket_str', 'compact_tick_label',
        'single_task_tokens', 'single_task_flops', 'single_task_usd', 'single_task_wh',
        'human_minutes', 'ai_minutes', 'user_share_pct', 'token_share_pct', 'spend_share_pct'
    ]

    df_all_cells = pd.concat([df_cells, df_gen5], ignore_index=True)
    assert len(df_all_cells) == 36, f"Expected 36 total cells (6 Gens x 6 Levels), got {len(df_all_cells)}"

    # Gate 1: Schema & Null Gate
    null_count = df_all_cells[req_cols].isna().sum().sum()
    print(f"  -> Gate 1 (Schema & Null Gate): null_count = {null_count} across {len(req_cols)} columns (36 cells: G0..G5 x L1..L6)")
    assert null_count == 0, f"Gate 1 Failed: Found {null_count} NaNs"

    # Gate 2: Mathematical Bounds Gate
    df_pop = df_all_cells.copy()
    assert (df_pop['learning_hours'] >= 0).all(), "Gate 2 Failed: learning_hours < 0"
    assert (df_pop['hardware_cap_usd'] >= 0).all(), "Gate 2 Failed: hardware_cap_usd < 0"
    assert (df_pop['single_task_tokens'] >= 0).all(), "Gate 2 Failed: single_task_tokens < 0"
    assert (df_pop['single_task_flops'] > 0).all(), "Gate 2 Failed: single_task_flops <= 0"
    assert (df_pop['single_task_usd'] >= 0).all(), "Gate 2 Failed: single_task_usd < 0"
    assert (df_pop['single_task_wh'] > 0).all(), "Gate 2 Failed: single_task_wh <= 0"
    print(f"  -> Gate 2 (Mathematical Bounds Gate): PASS | tokens range=[{df_pop['single_task_tokens'].min()}, {df_pop['single_task_tokens'].max()}], USD range=[{df_pop['single_task_usd'].min()}, {df_pop['single_task_usd'].max()}]")

    # Gate 3: Strict Monotonic Level Beeline-Hour & Hardware-Capital Gate (L1 < L2 < L3 < L4 < L5 < L6)
    for gen_id, df_gen in df_pop.groupby("gen_id", sort=False):
        df_gen_sorted = df_gen.sort_values("level_id").reset_index(drop=True)
        assert list(df_gen_sorted["level_id"]) == [1, 2, 3, 4, 5, 6], f"Missing levels in {gen_id}"
        for i in range(len(df_gen_sorted) - 1):
            h_k = df_gen_sorted.loc[i, 'learning_hours']
            h_next = df_gen_sorted.loc[i + 1, 'learning_hours']
            c_k = df_gen_sorted.loc[i, 'hardware_cap_usd']
            c_next = df_gen_sorted.loc[i + 1, 'hardware_cap_usd']
            assert h_k < h_next, f"Gate 3 Failed in {gen_id}: L{i+1} hours ({h_k}) >= L{i+2} hours ({h_next})"
            assert c_k < c_next, f"Gate 3 Failed in {gen_id}: L{i+1} cap ({c_k}) >= L{i+2} cap ({c_next})"
    print("  -> Gate 3 (Monotonic 6-Level Beeline-Hour & Capital Gate): PASS | L1(0h|$0) < L2(<50h|<$30) < L3(<200h|<$100) < L4(~600h|~$1.5k) < L5(~2,000h|~$500k) < L6(~10,000h|~$100M+) across G0..G5")

    # Gate 4: Six-Level Share Conservation Identity Gate
    for gen_id, df_gen in df_all_cells.groupby("gen_id", sort=False):
        u_sum = df_gen['user_share_pct'].sum()
        t_sum = df_gen['token_share_pct'].sum()
        s_sum = df_gen['spend_share_pct'].sum()
        assert abs(u_sum - 100.0) <= 0.5, f"Gate 4 Failed in {gen_id}: user_share_pct sum = {u_sum}"
        assert abs(t_sum - 100.0) <= 0.5, f"Gate 4 Failed in {gen_id}: token_share_pct sum = {t_sum}"
        assert abs(s_sum - 100.0) <= 0.5, f"Gate 4 Failed in {gen_id}: spend_share_pct sum = {s_sum}"
        print(f"  -> Gate 4 ({gen_id} 6-Level Share Conservation): PASS | Users={u_sum:.1f}%, Tokens={t_sum:.1f}%, Spend={s_sum:.1f}%")

    # Gate 5: Down-Ladder Skill Deflation Gate ($H_0$ Verification)
    gen_cols = ["G0_level", "G1_level", "G2_level", "G3_level", "G4_level"]
    for _, row in df_bench.iterrows():
        w = row["workflow_key"]
        for t in range(1, len(gen_cols)):
            l_prev = row[gen_cols[t - 1]]
            l_curr = row[gen_cols[t]]
            assert l_curr <= l_prev, f"Gate 5 Failed for {w}: {gen_cols[t]} ({l_curr}) > {gen_cols[t-1]} ({l_prev})"
        print(f"  -> Gate 5 ($H_0$ Skill Deflation - {w}): PASS | Level trajectory = {[int(row[c]) for c in gen_cols]} (Saved {row['total_hours_saved']}h)")

    # Gate 6: Zero Forbidden Min-Max Hour Range Gate across all v4 CSV files
    forbidden_pat = re.compile(r"(0[–-]0h|7[–-]45h|50[–-]200h|200[–-]600h|600[–-]2,?000h|7 to 45 hours|50 to 200 hours|200 to 600 hours|600 to 2,?000)")
    for fname in sorted(os.listdir(CACHE_DIR)):
        if fname.endswith(".csv"):
            fpath = os.path.join(CACHE_DIR, fname)
            content_str = open(fpath, encoding="utf-8").read()
            m = forbidden_pat.search(content_str)
            assert m is None, f"Gate 6 Failed: Found forbidden min-max range '{m.group(0)}' in {fname}"
    print("  -> Gate 6 (Zero Forbidden Min-Max Range String Gate): PASS | 0 occurrences across all cache_v4/*.csv files")

    print("\n[ALL 6 V4 VALIDATION GATES PASSED 100% WITHOUT ERROR ACROSS ALL 36 CELLS (G0..G5 x L1..L6)]\n")
    return {
        "ladders": df_ladders,
        "levels": df_levels,
        "use_cases": df_use_cases,
        "tutorials": df_tutorials,
        "glossary": df_glossary,
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
