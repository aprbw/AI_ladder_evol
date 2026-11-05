import os
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import matplotlib.gridspec as gridspec

# Ensure output directories exist
ARTIFACT_DIR = "/Users/z3540725/.gemini/antigravity/brain/a6915702-56c0-4c0f-b9f8-3259cffb7e3f"
PERSONAL_FIG_DIR = "/Users/z3540725/My Drive/personal/figures"
WORKSPACE_FIG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "figures"))
os.makedirs(ARTIFACT_DIR, exist_ok=True)
os.makedirs(PERSONAL_FIG_DIR, exist_ok=True)
os.makedirs(WORKSPACE_FIG_DIR, exist_ok=True)

# CITRA Global Semantic Color Mapping (Okabe-Ito / High-Contrast Publication Palette)
PALETTE = {
    "SUNK": "#0072B2",       # Deep Blue: Old Step Sinking into Default UI
    "EVOLVED": "#009E73",    # Bluish Green: Evolved Core Workhorse Step
    "SPLIT": "#E69F00",      # Orange/Gold: Split & Specialized Step
    "NEW": "#D55E00",        # Vermilion/Crimson: New Breakthrough / Top Step
    "GONE": "#7F7F7F",       # Slate Grey: Combined or Gone Step
    "SUPPLY": "#D55E00",     # Model/Compute/Token Supply Side
    "DEMAND": "#0072B2",     # User/Human Demand Side
    "ACTUAL": "#009E73",     # Realised USD Cost / Spend
    "MODELLED": "#CC79A7",   # AI Runtime / Modelled Fit
    "BG_CARD": "#F8FAFC",
    "GRID": "#CBD5E1",
    "TEXT": "#0F172A",
    "SUBTEXT": "#334155",
}

plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]
plt.rcParams["axes.edgecolor"] = "#475569"
plt.rcParams["axes.linewidth"] = 0.8

# Master Dataset across all 5 Era Ladders (23 Steps)
ERAS = [
    {
        "id": "L1",
        "num": 1,
        "short_title": "Era 1 (L1: 2017-06 to 2020-05)",
        "full_title": "Figure 1: Pre-LLM & Transfer-Learning NLP Ecosystem (2017-06 to 2020-05): Task Complexity Hierarchy & Compute Allocation",
        "dates": "2017-06 to 2020-05",
        "subtitle": "The Fine-Tuned Encoder Era — Triggered by Transformer (2017-06), ULMFiT (2018-01) & BERT (2018-10)",
        "totals": {
            "Users": "~1.8M practitioners",
            "Spend": "~USD 2.8B",
            "Compute": "~1.5e23 FLOPs",
            "Energy": "~950,000 MWh",
        },
        "steps": [
            {
                "step": 1,
                "name": "Rule Engines & Cloud NLP APIs",
                "short_node": "Rule Engines & Cloud APIs",
                "status": "SUNK",
                "status_label": "Baseline Commodity UI",
                "tools": "Regex, spaCy v2, scikit-learn, AWS Comprehend, GCP NLP",
                "scope": "Single sentence / keyword / sentiment tag",
                "limit": "Fails on context, synonyms & multi-sentence logic",
                "tokens": 50,
                "flops": 1e8,
                "usd": 0.0001,
                "wh": 0.0005,
                "human_min": 5.0,
                "ai_min": 0.005,
                "user_share": 62,
                "compute_share": 15,
                "y_complexity": 1.0,
            },
            {
                "step": 2,
                "name": "Static Word Vectors + Task RNNs/CNNs",
                "short_node": "Word2Vec/GloVe + BiLSTM",
                "status": "GONE",
                "status_label": "Legacy ML (Gone in L2)",
                "tools": "Word2Vec, GloVe, fastText + Keras/PyTorch BiLSTM-CRF",
                "scope": "Single-task document classification & custom NER",
                "limit": "One fixed vector per word; loses context past ~100 words",
                "tokens": 300,
                "flops": 1e15,
                "usd": 25.0,
                "wh": 30.0,
                "human_min": 480.0,
                "ai_min": 20.0,
                "user_share": 23,
                "compute_share": 25,
                "y_complexity": 2.1,
            },
            {
                "step": 3,
                "name": "Pretrained Encoder Fine-Tuning (BERT)",
                "short_node": "Pretrained Encoder FT (BERT)",
                "status": "NEW",
                "status_label": "New 2018 Workhorse",
                "tools": "BERT, RoBERTa, ULMFiT, DistilBERT, HuggingFace, GPT-2",
                "scope": "Multi-sentence Q&A, search ranking & domain NLU",
                "limit": "512-token window; requires 1k–10k labeled rows per task",
                "tokens": 512,
                "flops": 5e16,
                "usd": 50.0,
                "wh": 200.0,
                "human_min": 240.0,
                "ai_min": 45.0,
                "user_share": 13,
                "compute_share": 40,
                "y_complexity": 3.4,
            },
            {
                "step": 4,
                "name": "From-Scratch Sequence & Deep RL Systems",
                "short_node": "From-Scratch NMT & Deep RL",
                "status": "EVOLVED",
                "status_label": "Frontier Cluster Train",
                "tools": "fairseq, tensor2tensor, BioBERT, OpenAI Five, AlphaStar",
                "scope": "Full translation engine, domain pretraining or game RL",
                "limit": "Requires multi-GPU/TPU pods (USD 1k–160k+) & PhD team",
                "tokens": 2048,
                "flops": 2e20,
                "usd": 35000.0,
                "wh": 1200000.0,
                "human_min": 12000.0,
                "ai_min": 14400.0,
                "user_share": 2,
                "compute_share": 20,
                "y_complexity": 4.7,
            },
        ],
    },
    {
        "id": "L2",
        "num": 2,
        "short_title": "Era 2 (L2: 2020-06 to 2022-10)",
        "full_title": "Figure 2: Completion Foundation Models & Early Copilot Ecosystem (2020-06 to 2022-10): Complexity & Resource Profile",
        "dates": "2020-06 to 2022-10",
        "subtitle": "The Few-Shot Completion Era — Triggered by OpenAI GPT-3 API (2020-06, USD 60/1M) & GitHub Copilot Preview (2021-06)",
        "totals": {
            "Users": "~8M devs & writers",
            "Spend": "~USD 3.8B",
            "Compute": "~6.0e23 FLOPs",
            "Energy": "~95,000 MWh",
        },
        "steps": [
            {
                "step": 1,
                "name": "Single-Line IDE Autocomplete & Copy Templates",
                "short_node": "IDE Ghost Text & Templates",
                "status": "SUNK",
                "status_label": "New Inline Ghost-Text UI",
                "tools": "GitHub Copilot (Codex), TabNine, Jasper.ai, Copy.ai",
                "scope": "Single line of code (15–50 tokens) or marketing blurb",
                "limit": "Blind to multi-file architecture; hallucinates APIs",
                "tokens": 250,
                "flops": 6e12,
                "usd": 0.002,
                "wh": 0.08,
                "human_min": 0.2,
                "ai_min": 0.01,
                "user_share": 50,
                "compute_share": 18,
                "y_complexity": 1.3,
            },
            {
                "step": 2,
                "name": "Zero-Shot & Few-Shot Completion Prompting",
                "short_node": "Few-Shot API Completion",
                "status": "NEW",
                "status_label": "New Step (In-Context Learning)",
                "tools": "OpenAI Playground, davinci / text-davinci-002 API",
                "scope": "Single-task extraction, summary or draft via 3–5 examples",
                "limit": "2k–4k context ceiling; requires manual stop-token tuning",
                "tokens": 1500,
                "flops": 5e14,
                "usd": 0.06,
                "wh": 0.45,
                "human_min": 5.0,
                "ai_min": 0.06,
                "user_share": 25,
                "compute_share": 22,
                "y_complexity": 2.5,
            },
            {
                "step": 3,
                "name": "Early Embedding Search & Prompt Chains",
                "short_node": "Early FAISS/Pinecone Search",
                "status": "SPLIT",
                "status_label": "Split Pre-RAG Step",
                "tools": "FAISS, Pinecone (2021), Weaviate, OpenAI Embeddings",
                "scope": "Multi-document semantic lookup + chained API calls",
                "limit": "High latency & USD 60/1M token cost; custom glue code",
                "tokens": 10000,
                "flops": 3.5e15,
                "usd": 0.40,
                "wh": 2.8,
                "human_min": 30.0,
                "ai_min": 0.3,
                "user_share": 7,
                "compute_share": 15,
                "y_complexity": 3.6,
            },
            {
                "step": 4,
                "name": "Task-Specific Encoder & Open-Model Fine-Tuning",
                "short_node": "Encoder & Open-Model FT",
                "status": "EVOLVED",
                "status_label": "Combined L1 Steps 3+4",
                "tools": "RoBERTa, DeBERTa-v3, T5, GPT-J-6B, HuggingFace Trainer",
                "scope": "High-volume enterprise classification & custom domain models",
                "limit": "Full-weight GPU training (USD 100–2,500) per task update",
                "tokens": 50000,
                "flops": 1e19,
                "usd": 450.0,
                "wh": 3200.0,
                "human_min": 720.0,
                "ai_min": 360.0,
                "user_share": 18,
                "compute_share": 45,
                "y_complexity": 4.9,
            },
        ],
    },
    {
        "id": "L3",
        "num": 3,
        "short_title": "Era 3 (L3: 2022-11 to 2024-05)",
        "full_title": "Figure 3: Conversational Web Chat, Custom Vector RAG & Early Agent Ecosystem (2022-11 to 2024-05): Complexity & Cost",
        "dates": "2022-11 to 2024-05",
        "subtitle": "The ChatGPT & Custom RAG Era — Triggered by ChatGPT (2022-11), gpt-3.5-turbo USD 2/1M Drop, GPT-4 & LLaMA (2023-03)",
        "totals": {
            "Users": "~250M monthly users",
            "Spend": "~USD 6.5B (1.7B Ent.)",
            "Compute": "~1.8e25 FLOPs",
            "Energy": "~620,000 MWh",
        },
        "steps": [
            {
                "step": 1,
                "name": "Single-Turn Web Chat & Inline Autocomplete",
                "short_node": "Free Web Chat & Copilot",
                "status": "SUNK",
                "status_label": "L2 Step 2 Sinks to Free Web UI",
                "tools": "ChatGPT Free (gpt-3.5-turbo), Bing Chat, GitHub Copilot",
                "scope": "Single question, email draft, or single-line code completion",
                "limit": "Hallucinates facts; lacks private doc or live tool access",
                "tokens": 1200,
                "flops": 1.8e14,
                "usd": 0.0024,
                "wh": 0.30,
                "human_min": 2.0,
                "ai_min": 0.05,
                "user_share": 68,
                "compute_share": 32,
                "y_complexity": 1.5,
            },
            {
                "step": 2,
                "name": "Multi-Turn Prompting & System Personas",
                "short_node": "Multi-Turn GPT-4 & Personas",
                "status": "SPLIT",
                "status_label": "Split from L2 Step 2",
                "tools": "ChatGPT Plus (GPT-4), Custom GPTs, CoT, JSON Function Calling",
                "scope": "Multi-turn code/text analysis, structured JSON extraction",
                "limit": "8k–32k context drift; manual copy-paste between browser & IDE",
                "tokens": 6000,
                "flops": 1.5e16,
                "usd": 0.22,
                "wh": 1.5,
                "human_min": 12.0,
                "ai_min": 0.3,
                "user_share": 20,
                "compute_share": 28,
                "y_complexity": 2.8,
            },
            {
                "step": 3,
                "name": "Custom Vector Document Search (RAG)",
                "short_node": "Custom Vector RAG (LangChain)",
                "status": "EVOLVED",
                "status_label": "Evolved Enterprise Standard",
                "tools": "LangChain, LlamaIndex, Pinecone, ChromaDB, ada-002 + GPT-4",
                "scope": "Question answering over 10–1,000 private corporate PDFs/wikis",
                "limit": "Naive chunking breaks tables & cross-document synthesis",
                "tokens": 22000,
                "flops": 5e16,
                "usd": 0.65,
                "wh": 4.2,
                "human_min": 25.0,
                "ai_min": 0.5,
                "user_share": 8,
                "compute_share": 23,
                "y_complexity": 4.0,
            },
            {
                "step": 4,
                "name": "Parameter-Efficient Open-Weight Fine-Tuning",
                "short_node": "Open-Weight LoRA / QLoRA",
                "status": "EVOLVED",
                "status_label": "LoRA Replaces Full Train",
                "tools": "LLaMA-2, Mistral-7B, HuggingFace PEFT, QLoRA, Axolotl, vLLM",
                "scope": "Custom domain tone, SQL dialect, or private on-prem model",
                "limit": "Teaches form/style rather than new factual knowledge",
                "tokens": 150000,
                "flops": 5e18,
                "usd": 45.0,
                "wh": 450.0,
                "human_min": 360.0,
                "ai_min": 180.0,
                "user_share": 3,
                "compute_share": 10,
                "y_complexity": 5.1,
            },
            {
                "step": 5,
                "name": "Experimental Autonomous Agent Loops",
                "short_node": "Experimental AutoGPT Loops",
                "status": "NEW",
                "status_label": "New Top Step (Brittle Loop)",
                "tools": "AutoGPT, BabyAGI, AgentGPT, LangChain ReAct while-loops",
                "scope": "Open-ended multi-step web browsing & file goal execution",
                "limit": "Cascading hallucinations (~80% fail over 10 steps) & runaway cost",
                "tokens": 180000,
                "flops": 4e17,
                "usd": 6.50,
                "wh": 25.0,
                "human_min": 45.0,
                "ai_min": 15.0,
                "user_share": 1,
                "compute_share": 7,
                "y_complexity": 6.2,
            },
        ],
    },
    {
        "id": "L4",
        "num": 4,
        "short_title": "Era 4 (L4: 2024-06 to 2025-01)",
        "full_title": "Figure 4: Multimodal Context, Multi-File IDE Pairing & First Reasoning Models (2024-06 to 2025-01): Complexity & Cost",
        "dates": "2024-06 to 2025-01",
        "subtitle": "The Sonnet 3.5, Cursor & o1 Era — Triggered by GPT-4o, Claude 3.5 Sonnet + Artifacts (2024-06), 90% KV-Cache & o1 (2024-09)",
        "totals": {
            "Users": "~480M monthly users",
            "Spend": "~USD 18.5B (13.8B Ent.)",
            "Compute": "~9.0e25 FLOPs",
            "Energy": "~3,800,000 MWh",
        },
        "steps": [
            {
                "step": 1,
                "name": "Multimodal Web Chat & Built-In File/Web Search",
                "short_node": "Multimodal Chat & Native RAG",
                "status": "SUNK",
                "status_label": "L3 Single-PDF RAG Sinks to UI",
                "tools": "GPT-4o, Claude 3.5 Sonnet Artifacts/Projects, NotebookLM, Perplexity",
                "scope": "Multi-PDF/image Q&A, live web search, interactive UI prototype",
                "limit": "Single-turn output without hard math proofs or repo edits",
                "tokens": 5500,
                "flops": 3e15,
                "usd": 0.018,
                "wh": 0.50,
                "human_min": 1.5,
                "ai_min": 0.15,
                "user_share": 62,
                "compute_share": 22,
                "y_complexity": 2.0,
            },
            {
                "step": 2,
                "name": "Single-Call Reasoning Models (RLVR)",
                "short_node": "Single-Call Reasoning (o1/R1)",
                "status": "NEW",
                "status_label": "New Step (Test-Time Compute)",
                "tools": "OpenAI o1-preview, o1, o1-mini, DeepSeek-R1 (Jan 2025), QwQ",
                "scope": "PhD math/physics derivation, competitive code & logic proofs",
                "limit": "Isolated text box; lacks live multi-file IDE or bash execution",
                "tokens": 25000,
                "flops": 4e16,
                "usd": 0.42,
                "wh": 5.0,
                "human_min": 3.0,
                "ai_min": 1.2,
                "user_share": 12,
                "compute_share": 16,
                "y_complexity": 3.5,
            },
            {
                "step": 3,
                "name": "Multi-File IDE Pairing & Hybrid Enterprise RAG",
                "short_node": "Multi-File IDE & Hybrid RAG",
                "status": "SPLIT",
                "status_label": "Split & Evolved with KV-Cache",
                "tools": "Cursor Composer, Windsurf, Copilot Edits, Cohere Rerank 3 + KV-Cache",
                "scope": "Coordinated 3–10 file code edits or reranked corporate search",
                "limit": "Human must review diffs & manually fix failing terminal tests",
                "tokens": 70000,
                "flops": 8e16,
                "usd": 0.30,
                "wh": 6.0,
                "human_min": 4.0,
                "ai_min": 0.8,
                "user_share": 18,
                "compute_share": 34,
                "y_complexity": 4.8,
            },
            {
                "step": 4,
                "name": "Stateful Graph Workflows & Multi-Agent Pipelines",
                "short_node": "Stateful Graphs (LangGraph)",
                "status": "EVOLVED",
                "status_label": "Replaces Brittle AutoGPT",
                "tools": "LangGraph, CrewAI, AutoGen, LlamaIndex Workflows, Prompt Routing",
                "scope": "Deterministic branching customer-support, research & ETL pipelines",
                "limit": "Rigid pre-coded graph edges; breaks on unexpected OS/repo states",
                "tokens": 200000,
                "flops": 2e17,
                "usd": 1.10,
                "wh": 15.0,
                "human_min": 5.0,
                "ai_min": 3.5,
                "user_share": 6,
                "compute_share": 18,
                "y_complexity": 6.0,
            },
            {
                "step": 5,
                "name": "Cloud Sandbox & Screen Agents + Post-Training",
                "short_node": "Cloud Sandboxes & GUI Agents",
                "status": "NEW",
                "status_label": "New Top Step (Devin / GUI)",
                "tools": "Cognition Devin, Anthropic Computer Use, SWE-agent, Llama-3.1 DPO",
                "scope": "Autonomous cloud VM ticket attempts, GUI clicking & distillation",
                "limit": "Slow GUI latency, USD 500/mo cost & ~15–25% unassisted PR pass",
                "tokens": 1200000,
                "flops": 1.5e18,
                "usd": 6.80,
                "wh": 45.0,
                "human_min": 10.0,
                "ai_min": 20.0,
                "user_share": 2,
                "compute_share": 10,
                "y_complexity": 7.3,
            },
        ],
    },
    {
        "id": "L5",
        "num": 5,
        "short_title": "Era 5 (L5: 2025-02 to 2026-10)",
        "full_title": "Figure 5: Terminal CLI Harnesses, Deep Research, MCP & Parallel Agent Fleets (2025-02 to 2026-10): Complexity & Cost",
        "dates": "2025-02 to 2026-10",
        "subtitle": "The Agentic Harness & Fleet Era — Triggered by Deep Research & Claude Code (2025-02), MCP Standard (2025-03) & o3/Claude 4",
        "totals": {
            "Users": "~1.15B monthly users",
            "Spend": "~USD 95B (37B–55B Ent.)",
            "Compute": "~6.5e26 FLOPs",
            "Energy": "~48,000,000 MWh",
        },
        "steps": [
            {
                "step": 1,
                "name": "Auto-Routed Hybrid Chat & Instant Tab Edit",
                "short_node": "Auto-Routed Chat & Tab Edit",
                "status": "SUNK",
                "status_label": "L4 o1 Sinks to Auto-Router",
                "tools": "GPT-5/4o, Claude 4/4.5 Sonnet, Gemini 2.5 Flash, Cursor Tab",
                "scope": "Everyday chat, voice/vision, auto-thinking slider & tab edits",
                "limit": "Single-response window; stops short of 20-min research or repo loops",
                "tokens": 3500,
                "flops": 2e15,
                "usd": 0.008,
                "wh": 0.30,
                "human_min": 1.0,
                "ai_min": 0.1,
                "user_share": 55,
                "compute_share": 12,
                "y_complexity": 2.5,
            },
            {
                "step": 2,
                "name": "Autonomous Deep Research & Synthesis",
                "short_node": "Autonomous Deep Research",
                "status": "SPLIT",
                "status_label": "Split from L4 Step 2 Reasoning",
                "tools": "OpenAI Deep Research, Gemini/Perplexity Deep Research, o3-pro",
                "scope": "10–30 min autonomous browsing & synthesis across 50–150 sources",
                "limit": "Read-only web/file synthesis; stops short of repo/DB mutation",
                "tokens": 300000,
                "flops": 3e17,
                "usd": 1.50,
                "wh": 18.0,
                "human_min": 8.0,
                "ai_min": 18.0,
                "user_share": 18,
                "compute_share": 16,
                "y_complexity": 4.2,
            },
            {
                "step": 3,
                "name": "Standardized MCP Workflows & Scoped IDE Agents",
                "short_node": "MCP Workflows & IDE Agents",
                "status": "EVOLVED",
                "status_label": "Unites L4 Steps 3+4 under MCP",
                "tools": "Model Context Protocol (MCP) Servers + Cursor/Windsurf Agent Mode",
                "scope": "Multi-tool business workflows (GitHub/Slack/DB) & scoped IDE features",
                "limit": "Interactive single-thread IDE loop; waits on human approvals",
                "tokens": 150000,
                "flops": 1.8e17,
                "usd": 0.55,
                "wh": 10.0,
                "human_min": 4.0,
                "ai_min": 2.5,
                "user_share": 15,
                "compute_share": 22,
                "y_complexity": 5.6,
            },
            {
                "step": 4,
                "name": "Autonomous Terminal CLI & Cloud Repo Agents",
                "short_node": "Terminal CLI & Repo Agents",
                "status": "SPLIT",
                "status_label": "Split & Evolved CLI Harness",
                "tools": "Claude Code CLI, OpenAI Codex CLI/Cloud, Cline, Devin 2.0",
                "scope": "Full-repo refactors, running bash/linters/tests & self-fixing PRs",
                "limit": "Serial single-agent execution; context fills on massive monorepos",
                "tokens": 1300000,
                "flops": 1.5e18,
                "usd": 3.20,
                "wh": 40.0,
                "human_min": 6.0,
                "ai_min": 25.0,
                "user_share": 9,
                "compute_share": 30,
                "y_complexity": 7.2,
            },
            {
                "step": 5,
                "name": "Parallel Agent Fleets & Custom RLVR Flywheels",
                "short_node": "Parallel Fleets & RLVR",
                "status": "NEW",
                "status_label": "New Top Step (Worktrees & RLVR)",
                "tools": "Parallel Claude Code/Codex Git Worktrees, verifiers RLVR, TRL GRPO",
                "scope": "Orchestrating 3–10 parallel repo agents & custom RLVR post-training",
                "limit": "Human verification bandwidth & merge-conflict review bottleneck",
                "tokens": 8000000,
                "flops": 8e18,
                "usd": 20.00,
                "wh": 150.0,
                "human_min": 15.0,
                "ai_min": 45.0,
                "user_share": 3,
                "compute_share": 20,
                "y_complexity": 8.8,
            },
        ],
    },
]

# Cross-Era Transitions for Alluvial Diagram
TRANSITIONS = [
    # L1 -> L2
    (0, 1, 1, 1, "SUNK", 25, "Cloud APIs -> Inline Copilot/Templates"),
    (0, 2, 1, 2, "GONE", 12, "Word2Vec+RNNs Replaced by Few-Shot GPT-3"),
    (0, 3, 1, 2, "SPLIT", 15, "Zero/Few-Shot Offloads Low-Data NLU"),
    (0, 3, 1, 3, "SPLIT", 10, "Embeddings Power Early FAISS/Pinecone"),
    (0, 3, 1, 4, "EVOLVED", 25, "BERT/RoBERTa Scales to Prod Fine-Tuning"),
    (0, 4, 1, 4, "EVOLVED", 15, "Custom Training Merges into Open/Encoder FT"),
    # L2 -> L3
    (1, 1, 2, 1, "SUNK", 25, "Copilot + Templates Merge with Free Web Chat"),
    (1, 2, 2, 1, "SUNK", 25, "API Completion Sinks to Free ChatGPT UI"),
    (1, 2, 2, 2, "SPLIT", 20, "Splits into Multi-Turn GPT-4 & CoT Prompting"),
    (1, 3, 2, 3, "EVOLVED", 20, "Early Vector Search -> LangChain/LlamaIndex RAG"),
    (1, 4, 2, 4, "EVOLVED", 15, "Full Fine-Tuning -> 4-Bit LoRA/QLoRA (LLaMA-2)"),
    # L3 -> L4
    (2, 1, 3, 1, "SUNK", 30, "Free Chat Upgrades to Multimodal GPT-4o/Sonnet"),
    (2, 2, 3, 1, "SUNK", 15, "Custom GPTs Sink into Claude Projects/Artifacts"),
    (2, 3, 3, 1, "SUNK", 12, "Single-PDF RAG Sinks into Native Upload/NotebookLM"),
    (2, 2, 3, 3, "SPLIT", 15, "Code Chat Splits into Multi-File Cursor Composer"),
    (2, 3, 3, 3, "EVOLVED", 20, "Enterprise RAG Adds Rerankers & 90% KV-Cache"),
    (2, 4, 3, 5, "GONE", 8, "Routine Style LoRA Shrinks to Post-Training/DPO"),
    (2, 5, 3, 4, "EVOLVED", 12, "Brittle AutoGPT Loops -> Stateful LangGraph"),
    (2, 5, 3, 5, "SPLIT", 8, "Open Loops Split to Cloud Sandboxes (Devin)"),
    # L4 -> L5
    (3, 1, 4, 1, "SUNK", 28, "Multimodal Chat Adds Auto-Routing"),
    (3, 2, 4, 1, "SUNK", 12, "o1 Single-Call Thinking Sinks to Chat Slider"),
    (3, 2, 4, 2, "SPLIT", 18, "RLVR Reasoning + Search -> 20-Min Deep Research"),
    (3, 3, 4, 3, "EVOLVED", 16, "Hybrid RAG & IDE Pair Unite Under MCP"),
    (3, 4, 4, 3, "EVOLVED", 12, "Custom Graph Connectors Standardize on MCP"),
    (3, 3, 4, 4, "SPLIT", 20, "IDE Pairing Splits to Autonomous Claude Code CLI"),
    (3, 5, 4, 4, "EVOLVED", 10, "Devin Sandboxes Evolve into Local/Cloud CLI Agents"),
    (3, 4, 4, 5, "SPLIT", 10, "Pipelines Scale to Parallel Git Worktree Fleets"),
    (3, 5, 4, 5, "NEW", 12, "Post-Training Evolves to Custom RLVR Flywheels"),
]


def draw_era_ladder_figure(era, out_paths):
    """Render high-density 3-panel CITRA figure for a single Era Ladder with zero text overlap."""
    steps = era["steps"]
    n_steps = len(steps)
    fig = plt.figure(figsize=(16.5, 8.0), dpi=220, facecolor="white")
    gs = gridspec.GridSpec(
        1, 3, width_ratios=[1.62, 1.08, 0.82], wspace=0.20, left=0.025, right=0.975, top=0.84, bottom=0.10
    )

    # Title & Subtitle (CITRA Section 3.4: Latent context & DGP)
    fig.suptitle(era["full_title"], fontsize=13.0, fontweight="bold", color=PALETTE["TEXT"], x=0.025, ha="left", y=0.96)
    totals_str = " | ".join([f"{k}: {v}" for k, v in era["totals"].items()])
    fig.text(
        0.025,
        0.915,
        f"{era['subtitle']}  •  Totals ({totals_str})",
        fontsize=8.3,
        color=PALETTE["SUBTEXT"],
        ha="left",
    )

    # Panel A: Vertical Complexity Ladder Cards (Bottom-to-Top)
    ax_cards = fig.add_subplot(gs[0])
    ax_cards.set_xlim(0, 10)
    ax_cards.set_ylim(0.4, n_steps + 0.6)
    ax_cards.axis("off")
    ax_cards.set_title(
        "A. Task Complexity Hierarchy (Ordered Bottom-to-Top)",
        fontsize=10.5,
        fontweight="bold",
        color=PALETTE["TEXT"],
        loc="left",
        pad=10,
    )

    for s in steps:
        y = s["step"]
        col = PALETTE[s["status"]]
        # Card background
        rect = patches.FancyBboxPatch(
            (0.10, y - 0.43),
            9.80,
            0.86,
            boxstyle="round,pad=0.02,rounding_size=0.07",
            linewidth=1.6,
            edgecolor=col,
            facecolor=PALETTE["BG_CARD"],
        )
        ax_cards.add_patch(rect)
        # Left color stripe
        stripe = patches.FancyBboxPatch(
            (0.10, y - 0.43),
            0.36,
            0.86,
            boxstyle="round,pad=0.01,rounding_size=0.04",
            linewidth=0,
            facecolor=col,
        )
        ax_cards.add_patch(stripe)
        ax_cards.text(
            0.28,
            y,
            f"S{s['step']}",
            color="white",
            fontweight="bold",
            fontsize=10,
            ha="center",
            va="center",
        )
        # Line 1: Step Title (left)
        ax_cards.text(
            0.62,
            y + 0.27,
            f"Step {s['step']}: {s['name']}",
            fontsize=9.3,
            fontweight="bold",
            color=PALETTE["TEXT"],
            va="center",
        )
        # Line 2: Tools (left)
        ax_cards.text(
            0.62,
            y + 0.08,
            f"Stack: {s['tools']}",
            fontsize=7.9,
            color="#1E293B",
            va="center",
        )
        # Badge placed cleanly at bottom-right corner
        ax_cards.text(
            9.76,
            y - 0.27,
            f"{s['status_label']}",
            fontsize=7.3,
            fontweight="bold",
            color=col,
            ha="right",
            va="center",
            bbox=dict(boxstyle="round,pad=0.14", facecolor="white", edgecolor=col, lw=0.8),
        )
        # Line 3: Scope
        ax_cards.text(
            0.62,
            y - 0.10,
            f"Scope: {s['scope']}",
            fontsize=7.8,
            color="#334155",
            va="center",
        )
        # Line 4: Ceiling
        ax_cards.text(
            0.62,
            y - 0.28,
            f"Ceiling: {s['limit'][:56]}",
            fontsize=7.5,
            color="#64748B",
            style="italic",
            va="center",
        )

    # Panel B: Single-Task Resource Profile (Log10 Scale Bars)
    ax_cost = fig.add_subplot(gs[1])
    y_pos = np.arange(1, n_steps + 1)
    height = 0.22

    tokens_vals = [max(s["tokens"], 1) for s in steps]
    usd_vals = [max(s["usd"], 1e-4) for s in steps]
    wh_vals = [max(s["wh"], 1e-3) for s in steps]

    ax_cost.set_xscale("log")
    ax_cost.barh(
        y_pos + height,
        tokens_vals,
        height=height,
        color=PALETTE["SUPPLY"],
        alpha=0.88,
        label="Tokens / Task (count)",
    )
    ax_cost.barh(
        y_pos,
        [u * 1e4 for u in usd_vals],
        height=height,
        color=PALETTE["ACTUAL"],
        alpha=0.88,
        label="Cost / Task ($10^{-4}$ USD units)",
    )
    ax_cost.barh(
        y_pos - height,
        [w * 1e2 for w in wh_vals],
        height=height,
        color=PALETTE["MODELLED"],
        alpha=0.88,
        label="Energy / Task ($10^{-2}$ Wh units)",
    )

    for i, s in enumerate(steps):
        y = s["step"]
        ax_cost.text(
            tokens_vals[i] * 1.22,
            y + height,
            f"{s['tokens']:,} tok | {s['flops']:.0e} FLOPs",
            va="center",
            fontsize=7.5,
            color=PALETTE["SUPPLY"],
            fontweight="bold",
        )
        ax_cost.text(
            usd_vals[i] * 1e4 * 1.22,
            y,
            f"USD {s['usd']:.4g} | {s['human_min']:g}m H / {s['ai_min']:g}m AI",
            va="center",
            fontsize=7.5,
            color=PALETTE["ACTUAL"],
            fontweight="bold",
        )
        ax_cost.text(
            wh_vals[i] * 1e2 * 1.22,
            y - height,
            f"{s['wh']:g} Wh",
            va="center",
            fontsize=7.4,
            color=PALETTE["MODELLED"],
        )

    max_bar = max(max(tokens_vals), max(u * 1e4 for u in usd_vals), max(w * 1e2 for w in wh_vals))
    ax_cost.set_yticks(y_pos)
    ax_cost.set_yticklabels([f"Step {s['step']}" for s in steps], fontweight="bold", fontsize=9)
    ax_cost.set_ylim(0.4, n_steps + 0.6)
    ax_cost.set_xlim(0.5, max_bar * 2200)
    ax_cost.grid(True, which="both", axis="x", linestyle="--", color=PALETTE["GRID"], alpha=0.6)
    ax_cost.set_xlabel("Log10 Single-Task Resource Scale (Normalized Units)", fontsize=9, fontweight="bold")
    ax_cost.set_title(
        "B. Single-Task Resource Footprint (Log Scale)",
        fontsize=10.5,
        fontweight="bold",
        color=PALETTE["TEXT"],
        loc="left",
        pad=10,
    )
    ax_cost.legend(loc="lower right", fontsize=7.6, frameon=True, facecolor="white", framealpha=0.92)

    # Panel C: Industry-Wide User Share % vs Compute/Token Share %
    ax_share = fig.add_subplot(gs[2])
    user_shares = [s["user_share"] for s in steps]
    comp_shares = [s["compute_share"] for s in steps]
    bar_h = 0.30

    ax_share.barh(
        y_pos + bar_h / 2,
        user_shares,
        height=bar_h,
        color=PALETTE["DEMAND"],
        alpha=0.88,
        label="Active User Share (%)",
    )
    ax_share.barh(
        y_pos - bar_h / 2,
        comp_shares,
        height=bar_h,
        color=PALETTE["SUPPLY"],
        alpha=0.88,
        label="Compute / Token Share (%)",
    )

    for i, s in enumerate(steps):
        y = s["step"]
        ax_share.text(
            user_shares[i] + 1.5,
            y + bar_h / 2,
            f"{user_shares[i]}% users",
            va="center",
            fontsize=8.0,
            color=PALETTE["DEMAND"],
            fontweight="bold",
        )
        ax_share.text(
            comp_shares[i] + 1.5,
            y - bar_h / 2,
            f"{comp_shares[i]}% compute",
            va="center",
            fontsize=8.0,
            color=PALETTE["SUPPLY"],
            fontweight="bold",
        )

    ax_share.set_yticks(y_pos)
    ax_share.set_yticklabels([f"S{s['step']}" for s in steps], fontweight="bold", fontsize=9)
    ax_share.set_ylim(0.4, n_steps + 0.6)
    ax_share.set_xlim(0, 92)
    ax_share.grid(True, axis="x", linestyle="--", color=PALETTE["GRID"], alpha=0.6)
    ax_share.set_xlabel("Percentage of Era Total (Sums = 100%)", fontsize=9, fontweight="bold")
    ax_share.set_title(
        "C. Macro User vs. Compute Share",
        fontsize=10.5,
        fontweight="bold",
        color=PALETTE["TEXT"],
        loc="left",
        pad=10,
    )
    ax_share.legend(loc="upper right", fontsize=7.8, frameon=True, facecolor="white", framealpha=0.92)

    for p in out_paths:
        fig.savefig(p, dpi=220)
    plt.close(fig)


def draw_bezier_ribbon(ax, x0, y0, x1, y1, h0, h1, color, alpha=0.36):
    """Draw a smooth cubic Bezier alluvial ribbon between two nodes."""
    xm = (x0 + x1) / 2.0
    verts = [
        (x0, y0 - h0 / 2.0),
        (xm, y0 - h0 / 2.0),
        (xm, y1 - h1 / 2.0),
        (x1, y1 - h1 / 2.0),
        (x1, y1 + h1 / 2.0),
        (xm, y1 + h1 / 2.0),
        (xm, y0 + h0 / 2.0),
        (x0, y0 + h0 / 2.0),
        (x0, y0 - h0 / 2.0),
    ]
    codes = [
        Path.MOVETO,
        Path.CURVE4,
        Path.CURVE4,
        Path.CURVE4,
        Path.LINETO,
        Path.CURVE4,
        Path.CURVE4,
        Path.CURVE4,
        Path.CLOSEPOLY,
    ]
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor=color, edgecolor=color, lw=0.6, alpha=alpha, zorder=2)
    ax.add_patch(patch)


def draw_full_evolution_poster(out_paths):
    """Render Full-Timeline Alluvial Evolution & Cost Deflation Poster on a true continuous calendar time X-axis (2017-06 to 2026-10)."""
    fig = plt.figure(figsize=(24.0, 13.6), dpi=240, facecolor="white")
    gs = gridspec.GridSpec(
        2, 2, width_ratios=[1.0, 0.085], height_ratios=[3.10, 1.05], wspace=0.115, hspace=0.19, left=0.075, right=0.975, top=0.90, bottom=0.065
    )

    fig.suptitle(
        "Nine-Year AI & Agentic Ladder Evolution on a True Calendar Time Axis (2017-06 to 2026-10): Duration-Proportional Eras & Price Deflation",
        fontsize=14.8,
        fontweight="bold",
        color=PALETTE["TEXT"],
        x=0.075,
        ha="left",
        y=0.965,
    )
    fig.text(
        0.075,
        0.932,
        "Box Widths Strictly Proportional to Era Duration (L1: 36m • L2: 29m • L3: 19m • L4: 8m Flashpoint • L5: 21m)  •  Bezier Ribbons Encode Cross-Era Lineage  •  Lower Panel Shares Exact Time Axis",
        fontsize=9.8,
        color=PALETTE["SUBTEXT"],
        ha="left",
    )

    ax_main = fig.add_subplot(gs[0, 0])
    ax_top_leg = fig.add_subplot(gs[0, 1])
    ax_top_leg.axis("off")

    # Exact decimal year boundaries (YYYY + (MM-1)/12 for start of month, YYYY + MM/12 for end of month)
    era_bounds = [
        (2017 + 5.0 / 12.0, 2020 + 5.0 / 12.0, 36),   # L1: 2017-06 to 2020-05 (36 mos = 3.00 yrs)
        (2020 + 5.0 / 12.0, 2022 + 10.0 / 12.0, 29),  # L2: 2020-06 to 2022-10 (29 mos = 2.42 yrs)
        (2022 + 10.0 / 12.0, 2024 + 5.0 / 12.0, 19),  # L3: 2022-11 to 2024-05 (19 mos = 1.58 yrs)
        (2024 + 5.0 / 12.0, 2025 + 1.0 / 12.0, 8),    # L4: 2024-06 to 2025-01 (8 mos  = 0.67 yrs)
        (2025 + 1.0 / 12.0, 2026 + 10.0 / 12.0, 21),  # L5: 2025-02 to 2026-10 (21 mos = 1.75 yrs)
    ]
    ribbon_gap = 0.15  # ~1.8 months channel for Bezier alluvial ribbons between eras

    era_geom = []
    node_coords = {}
    for e_idx, era in enumerate(ERAS):
        t0, t1, mos = era_bounds[e_idx]
        xl = t0 + (0.0 if e_idx == 0 else ribbon_gap / 2.0)
        xr = t1 - (0.0 if e_idx == 4 else ribbon_gap / 2.0)
        w = xr - xl
        xc = 0.5 * (xl + xr)
        era_geom.append((t0, t1, mos, xl, xr, w, xc))
        for s in era["steps"]:
            node_coords[(e_idx, s["step"])] = (xl, xr, xc, w, s["y_complexity"], s)

    # Draw vertical dashed era boundary lines across ax_main
    cutoff_dates = [
        (2017 + 5.0 / 12.0, "2017-06 (L1)"),
        (2020 + 5.0 / 12.0, "2020-06 (L2)"),
        (2022 + 10.0 / 12.0, "2022-11 (L3)"),
        (2024 + 5.0 / 12.0, "2024-06 (L4)"),
        (2025 + 1.0 / 12.0, "2025-02 (L5)"),
        (2026 + 10.0 / 12.0, "2026-10 (End)"),
    ]
    for tc, clbl in cutoff_dates:
        ax_main.axvline(tc, color="#94A3B8", linestyle="--", lw=1.1, alpha=0.75, zorder=1)

    # Draw Alluvial Transition Ribbons (Shuffled z-order per CITRA Section 3.3)
    rng = np.random.default_rng(42)
    perm = rng.permutation(len(TRANSITIONS))
    for idx in perm:
        e0, s0, e1, s1, t_type, weight, t_label = TRANSITIONS[idx]
        xl0, xr0, xc0, w0, y0, st0 = node_coords[(e0, s0)]
        xl1, xr1, xc1, w1, y1, st1 = node_coords[(e1, s1)]
        h0 = 0.14 + (weight / 35.0) * 0.42
        h1 = 0.14 + (weight / 35.0) * 0.42
        draw_bezier_ribbon(
            ax_main,
            xr0,
            y0,
            xl1,
            y1,
            h0,
            h1,
            PALETTE[t_type],
            alpha=0.38,
        )

    # Curated non-truncated tool labels per (era_idx, step_num) so no word is ever cut mid-word
    clean_tools_map = {
        (0, 1): "Regex, spaCy v2, scikit-learn, AWS/GCP NLP",
        (0, 2): "Word2Vec, GloVe, fastText + BiLSTM-CRF",
        (0, 3): "BERT, RoBERTa, ULMFiT, DistilBERT, GPT-2",
        (0, 4): "fairseq, tensor2tensor, OpenAI Five, AlphaStar",
        (1, 1): "GitHub Copilot (Codex), TabNine, Jasper.ai",
        (1, 2): "OpenAI Playground, davinci / text-davinci-002",
        (1, 3): "FAISS, Pinecone (2021), Weaviate, Embeddings",
        (1, 4): "RoBERTa, DeBERTa-v3, T5, GPT-J-6B, HF Trainer",
        (2, 1): "ChatGPT Free (gpt-3.5-turbo), Bing, Copilot",
        (2, 2): "ChatGPT Plus (GPT-4), Custom GPTs, Claude 2",
        (2, 3): "LangChain, LlamaIndex, Pinecone, Chroma",
        (2, 4): "LLaMA-2, Mistral-7B, QLoRA, Axolotl, vLLM",
        (2, 5): "AutoGPT, BabyAGI, AgentGPT, ReAct Loops",
        (3, 1): "GPT-4o, Sonnet 3.5",
        (3, 2): "o1, DeepSeek-R1",
        (3, 3): "Cursor, KV-Cache",
        (3, 4): "LangGraph, CrewAI",
        (3, 5): "Devin, Computer Use",
        (4, 1): "GPT-5/4o, Claude 4/4.5, Gemini 2.5, Cursor Tab",
        (4, 2): "OpenAI Deep Research, Perplexity/Gemini DR",
        (4, 3): "MCP Servers + Cursor / Windsurf Agents",
        (4, 4): "Claude Code CLI, OpenAI Codex CLI, Aider",
        (4, 5): "Parallel Git Worktrees + Custom GRPO RLVR",
    }
    l4_compact_titles = {
        1: "S1: 4o/Sonnet UI",
        2: "S2: o1 / R1 Reason",
        3: "S3: Cursor / KV",
        4: "S4: LangGraph",
        5: "S5: Devin / VM",
    }

    # Draw Era Column Headers & Width-Proportional Step Boxes
    for e_idx, era in enumerate(ERAS):
        t0, t1, mos, xl, xr, w, xc = era_geom[e_idx]
        is_narrow = (mos <= 10)  # L4 is 8 months wide

        # Era header banner with width strictly = w
        banner = patches.FancyBboxPatch(
            (xl, 9.38),
            w,
            0.76,
            boxstyle="round,pad=0.012,rounding_size=0.04",
            facecolor="#1E293B",
            edgecolor="#0F172A",
            lw=1.2,
            zorder=5,
        )
        ax_main.add_patch(banner)
        if is_narrow:
            ax_main.text(xc, 9.94, f"L4 ({mos}m)", color="white", fontweight="bold", fontsize=7.8, ha="center", va="center", zorder=6)
            ax_main.text(xc, 9.72, "24-06–25-01", color="#E2E8F0", fontweight="bold", fontsize=6.2, ha="center", va="center", zorder=6)
            ax_main.text(xc, 9.51, "480M•USD 18.5B", color="#CBD5E1", fontsize=5.8, ha="center", va="center", zorder=6)
        else:
            ax_main.text(
                xc,
                9.90,
                f"{era['short_title']}  [{mos} Months]",
                color="white",
                fontweight="bold",
                fontsize=8.6 if mos >= 20 else 8.0,
                ha="center",
                va="center",
                zorder=6,
            )
            ax_main.text(
                xc,
                9.58,
                f"{era['totals']['Users']}  •  {era['totals']['Spend'].replace('$', 'USD ')}",
                color="#CBD5E1",
                fontsize=7.3 if mos >= 20 else 6.8,
                ha="center",
                va="center",
                zorder=6,
            )

        # Draw each step box with width = w
        for s in era["steps"]:
            yc = s["y_complexity"]
            col = PALETTE[s["status"]]
            box_h = 0.88
            box = patches.FancyBboxPatch(
                (xl, yc - box_h / 2.0),
                w,
                box_h,
                boxstyle="round,pad=0.012,rounding_size=0.04",
                facecolor="white",
                edgecolor=col,
                lw=2.0,
                zorder=4,
            )
            ax_main.add_patch(box)

            top_bar = patches.FancyBboxPatch(
                (xl, yc + box_h / 2.0 - 0.24),
                w,
                0.24,
                boxstyle="round,pad=0.008,rounding_size=0.03",
                facecolor=col,
                edgecolor=col,
                lw=0,
                zorder=4.5,
            )
            ax_main.add_patch(top_bar)

            tools_str = clean_tools_map[(e_idx, s["step"])]
            if is_narrow:
                title_str = l4_compact_titles[s["step"]]
                tok_str = f"{s['tokens']//1000}k | USD {s['usd']:.2g}" if s["tokens"] < 1000000 else f"1.2M | USD {s['usd']:.2g}"
                share_str = f"U:{s['user_share']}% • C:{s['compute_share']}%"
                f_title, f_body = 6.2, 5.75
            else:
                title_str = f"S{s['step']}: {s['short_node']}"
                tok_str = f"{s['tokens']:,} tok | USD {s['usd']:.3g} | {s['wh']:g} Wh"
                share_str = f"Users: {s['user_share']}%  •  Compute/Tokens: {s['compute_share']}%"
                f_title = 7.8 if mos >= 25 else 7.2
                f_body = 7.0 if mos >= 25 else 6.55

            ax_main.text(xc, yc + box_h / 2.0 - 0.12, title_str, color="white", fontweight="bold", fontsize=f_title, ha="center", va="center", zorder=5)
            ax_main.text(xc, yc + 0.04, tools_str, color=PALETTE["TEXT"], fontsize=f_body, ha="center", va="center", zorder=5)
            ax_main.text(xc, yc - 0.16, tok_str, color=PALETTE["SUBTEXT"], fontsize=f_body, fontweight="bold", ha="center", va="center", zorder=5)
            ax_main.text(xc, yc - 0.33, share_str, color=col, fontsize=f_body, fontweight="bold", ha="center", va="center", zorder=5)

    # Legend for transition mechanisms inside top-left open space
    legend_handles = [
        patches.Patch(color=PALETTE["SUNK"], label="Old Step Sinking into Default Step 1 UI (Commoditization)"),
        patches.Patch(color=PALETTE["EVOLVED"], label="Evolved Core Engineering Workhorse Step"),
        patches.Patch(color=PALETTE["SPLIT"], label="Split & Specialized Step (Divergent Scope / Autonomy)"),
        patches.Patch(color=PALETTE["NEW"], label="New Breakthrough Step (Unlocked by Tech / 10x Price Drop)"),
        patches.Patch(color=PALETTE["GONE"], label="Combined or Gone Step (Replaced by Superior Paradigm)"),
    ]
    ax_main.legend(
        handles=legend_handles,
        loc="upper left",
        bbox_to_anchor=(0.01, 0.89),
        fontsize=8.6,
        frameon=True,
        facecolor="white",
        edgecolor="#CBD5E1",
        framealpha=0.95,
        title="Cross-Era Structural Transition Categories (MECE Taxonomy)",
        title_fontsize=9.0,
    )

    x_min, x_max = 2017.25, 2027.00
    ax_main.set_xlim(x_min, x_max)
    ax_main.set_ylim(0.3, 10.30)
    ax_main.set_yticks([1.5, 3.0, 4.5, 6.0, 7.5, 9.0])
    ax_main.set_yticklabels(
        [
            "Tier 1: Single-Line /\nInstant UI (<10³ tok)",
            "Tier 2: Single-File /\nMulti-Turn (~10⁴ tok)",
            "Tier 3: Multi-Doc RAG /\nIDE Pair (~10⁵ tok)",
            "Tier 4: Repo CLI /\nGraph Loop (~10⁶ tok)",
            "Tier 5: Cloud Sandbox /\nCustom FT (~10⁶–10⁷ tok)",
            "Tier 6: Parallel Agent\nFleets (~10⁷+ tok)",
        ],
        fontsize=8.4,
        fontweight="bold",
    )
    year_ticks = np.arange(2017, 2028, 1)
    ax_main.set_xticks(year_ticks)
    ax_main.set_xticklabels([f"{y}-01" for y in year_ticks], fontsize=8.4, fontweight="bold", color=PALETTE["SUBTEXT"])
    ax_main.set_ylabel("Task & Use-Case Complexity Axis (Ordered Bottom-to-Top)", fontsize=10.2, fontweight="bold")
    ax_main.grid(True, axis="y", linestyle=":", color=PALETTE["GRID"], alpha=0.65)
    ax_main.grid(True, axis="x", linestyle=":", color=PALETTE["GRID"], alpha=0.45)

    # Right-side summary annotation in gs[0, 1] showing Era Duration Bars
    ax_dur = ax_top_leg
    ax_dur.axis("on")
    era_short = ["L1\n(36m)", "L2\n(29m)", "L3\n(19m)", "L4\n(8m)", "L5\n(21m)"]
    mos_vals = [36, 29, 19, 8, 21]
    y_d = np.arange(5)
    d_cols = [PALETTE["GONE"], PALETTE["SUNK"], PALETTE["EVOLVED"], PALETTE["SPLIT"], PALETTE["NEW"]]
    ax_dur.barh(y_d, mos_vals, height=0.55, color=d_cols, alpha=0.88, edgecolor="#0F172A", lw=0.8)
    for i, m in enumerate(mos_vals):
        ax_dur.text(m + 1.5, i, f"{m}m", va="center", fontsize=7.8, fontweight="bold", color=PALETTE["TEXT"])
    ax_dur.set_yticks(y_d)
    ax_dur.set_yticklabels(era_short, fontsize=7.8, fontweight="bold")
    ax_dur.set_xlim(0, 48)
    ax_dur.set_xlabel("Months", fontsize=8.0, fontweight="bold")
    ax_dur.set_title("Era\nWidth", fontsize=8.8, fontweight="bold", color=PALETTE["TEXT"])
    ax_dur.grid(True, axis="x", linestyle=":", color=PALETTE["GRID"], alpha=0.5)

    # Bottom Synchronized Panel: Continuous Time Trajectory (2017.42 to 2026.83) + Right Marginal
    ax_bot = fig.add_subplot(gs[1, 0])
    ax_bot_m = fig.add_subplot(gs[1, 1], sharey=ax_bot)
    ax_bot.set_xlim(x_min, x_max)
    ax_bot.set_yscale("log")

    for i_c, (tc, clbl) in enumerate(cutoff_dates):
        ax_bot.axvline(tc, color="#94A3B8", linestyle="--", lw=1.1, alpha=0.75, zorder=1)
        if i_c == len(cutoff_dates) - 1:
            ax_bot.text(tc - 0.04, 340, clbl, fontsize=6.8, fontweight="bold", color="#475569", va="top", ha="right")
        else:
            ax_bot.text(tc + 0.04, 340, clbl, fontsize=6.8, fontweight="bold", color="#475569", va="top", ha="left")

    era_mid_t = [g[6] for g in era_geom]
    price_per_1m = np.array([120.0, 60.0, 2.0, 0.15, 0.06])
    top_step_tokens = np.array([2048.0, 50000.0, 180000.0, 1200000.0, 8000000.0])
    step1_tokens = np.array([50.0, 250.0, 1200.0, 5500.0, 3500.0])

    # Also plot step-function / continuous bands across each era's exact [t0, t1] span
    for e_idx, (t0, t1, mos, xl, xr, w, xc) in enumerate(era_geom):
        ax_bot.hlines(price_per_1m[e_idx], t0, t1, colors=PALETTE["ACTUAL"], lw=3.2, alpha=0.45, zorder=3)

    l1 = ax_bot.plot(
        era_mid_t,
        price_per_1m,
        marker="o",
        markersize=7,
        linewidth=2.5,
        color=PALETTE["ACTUAL"],
        label="Baseline Inference Price (USD / 1M Tokens, Left Axis)",
        zorder=5,
    )
    price_offsets = [(-0.0, 0.32), (0.0, 2.0), (-0.48, 0.48), (0.0, 0.22), (0.0, 2.3)]
    for x, p, (dx, mult), lbl in zip(
        era_mid_t,
        price_per_1m,
        price_offsets,
        [
            "~USD 120/1M\n(V100 GPU)",
            "USD 60/1M\n(davinci)",
            "USD 2.00/1M\n(3.5-turbo)",
            "USD 0.15/1M\n(4o-mini/KV)",
            "USD 0.06/1M\n(Flash/KV)",
        ],
    ):
        va_align = "bottom" if mult > 1 else "top"
        ax_bot.text(x + dx, p * mult, lbl, ha="center", va=va_align, fontsize=7.3, color=PALETTE["ACTUAL"], fontweight="bold")

    ax_bot_r = ax_bot.twinx()
    ax_bot_r.set_yscale("log")
    for e_idx, (t0, t1, mos, xl, xr, w, xc) in enumerate(era_geom):
        ax_bot_r.hlines(top_step_tokens[e_idx], t0, t1, colors=PALETTE["SUPPLY"], lw=3.2, alpha=0.40, zorder=3)

    l2 = ax_bot_r.plot(
        era_mid_t,
        top_step_tokens,
        marker="s",
        markersize=7,
        linewidth=2.5,
        linestyle="--",
        color=PALETTE["SUPPLY"],
        label="Top-Step Single-Task Token Volume (Tokens / Run, Right Axis)",
        zorder=5,
    )
    l3 = ax_bot_r.plot(
        era_mid_t,
        step1_tokens,
        marker="^",
        markersize=6,
        linewidth=2.0,
        linestyle=":",
        color=PALETTE["DEMAND"],
        label="Step 1 Default UI Token Volume (Tokens / Run, Right Axis)",
        zorder=4,
    )
    tok_offsets = [1.55, 0.35, 1.65, 1.55, 1.45]
    for x, t, mult in zip(era_mid_t, top_step_tokens, tok_offsets):
        va_align = "bottom" if mult > 1 else "top"
        ax_bot_r.text(x, t * mult, f"{int(t):,} tok", ha="center", va=va_align, fontsize=7.4, color=PALETTE["SUPPLY"], fontweight="bold")

    ax_bot.set_ylim(0.012, 650)
    ax_bot_r.set_ylim(20, 4e7)
    ax_bot.set_xticks(year_ticks)
    ax_bot.set_xticklabels([str(y) for y in year_ticks], fontsize=9.0, fontweight="bold")
    ax_bot.set_xlabel("Continuous Calendar Time (2017-06 to 2026-10, Exact Era Cutoff Boundaries Marked)", fontsize=9.5, fontweight="bold")
    ax_bot.set_ylabel("Price (USD / 1M Tokens, Log)", fontsize=9, fontweight="bold", color=PALETTE["ACTUAL"])
    ax_bot_r.set_ylabel("Tokens per Single Task (Log)", fontsize=8.8, fontweight="bold", color=PALETTE["SUPPLY"], labelpad=6)
    ax_bot.grid(True, which="both", linestyle="--", color=PALETTE["GRID"], alpha=0.6)
    ax_bot.set_title(
        "Synchronized Continuous-Time Economic Engine: 2,000x Inference Price Deflation Directly Unlocks 4,000x Larger Multi-Step Agent Loops",
        fontsize=10.0,
        fontweight="bold",
        color=PALETTE["TEXT"],
        loc="left",
        pad=6,
    )

    lines = l1 + l2 + l3
    labels = [l.get_label() for l in lines]
    ax_bot.legend(lines, labels, loc="center left", fontsize=8.0, frameon=True, facecolor="white", framealpha=0.92)

    # Marginal histogram for price on ax_bot_m
    bins_p = np.geomspace(0.02, 500.0, 10)
    ax_bot_m.hist(price_per_1m, bins=bins_p, orientation="horizontal", histtype="step", lw=2.0, color=PALETTE["ACTUAL"])
    ax_bot_m.set_xlabel("Eras", fontsize=8.0, fontweight="bold")
    ax_bot_m.tick_params(labelleft=False)
    ax_bot_m.set_title("Price\nMarginal", fontsize=8.2, fontweight="bold", color=PALETTE["ACTUAL"])
    ax_bot_m.grid(True, which="both", linestyle=":", color=PALETTE["GRID"], alpha=0.5)

    for p in out_paths:
        fig.savefig(p, dpi=240, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def draw_era_defining_news_poster(out_paths):
    """Render Full-Timeline Poster of Era-Opening/Closing Tech Triggers, Defining News Wins & Failures ('Who Did What'), and 'Top Thing to Learn' per Era on a True Continuous Time X-Axis (2017-06 to 2026-10)."""
    fig = plt.figure(figsize=(24.5, 14.6), dpi=240, facecolor="white")
    gs = gridspec.GridSpec(
        2, 1, height_ratios=[4.25, 0.95], hspace=0.12, left=0.075, right=0.98, top=0.90, bottom=0.055
    )

    fig.suptitle(
        "Era-Defining Moments, Tech Triggers, Real-World News ('Who Did What') & Top Skill to Learn Across Nine Years (2017-06 to 2026-10)",
        fontsize=14.8,
        fontweight="bold",
        color=PALETTE["TEXT"],
        x=0.075,
        ha="left",
        y=0.965,
    )
    fig.text(
        0.075,
        0.932,
        "Continuous Calendar Time X-Axis (Box Widths Proportional to Era Months: L1=36m, L2=29m, L3=19m, L4=8m, L5=21m)  •  4 Swimlanes: (1) Start/End Tech, (2) News Wins, (3) News Failures, (4) Top Skill to Learn",
        fontsize=9.6,
        color=PALETTE["SUBTEXT"],
        ha="left",
    )

    ax = fig.add_subplot(gs[0])
    ax_pin = fig.add_subplot(gs[1], sharex=ax)

    era_bounds = [
        (2017 + 5.0 / 12.0, 2020 + 5.0 / 12.0, 36, "L1: Pre-LLM & Encoder Era", "2017-06 to 2020-05", PALETTE["GONE"]),
        (2020 + 5.0 / 12.0, 2022 + 10.0 / 12.0, 29, "L2: Completion & Copilot Era", "2020-06 to 2022-10", PALETTE["SUNK"]),
        (2022 + 10.0 / 12.0, 2024 + 5.0 / 12.0, 19, "L3: ChatGPT, RAG & AutoGPT Era", "2022-11 to 2024-05", PALETTE["EVOLVED"]),
        (2024 + 5.0 / 12.0, 2025 + 1.0 / 12.0, 8, "L4: Sonnet, Cursor & o1", "2024-06 to 2025-01", PALETTE["SPLIT"]),
        (2025 + 1.0 / 12.0, 2026 + 10.0 / 12.0, 21, "L5: CLI Agents, MCP & Fleets Era", "2025-02 to 2026-10", PALETTE["NEW"]),
    ]
    gap = 0.08  # small visual margin between era columns

    # Content for each Era across the 4 swimlanes (tailored to fit each era's exact proportional box width!)
    swimlane_data = [
        # Era 1 (36 mos - wide)
        {
            "tech": [
                "STARTS ERA (2017-06 / 2018-10):",
                "• Google Transformer ('Attention Is All You Need', 2017-06)",
                "• ULMFiT (2018-01) & BERT Bidirectional Encoder (2018-10)",
                "ENDS / OUTDATES ERA (2020-05):",
                "• Fine-tuning needs 1,000s of labeled rows + V100 GPU per task",
                "• Outdated when GPT-3 175B proves zero/few-shot API prompting",
            ],
            "wins": [
                "WHO DID WHAT — HEADLINE WINS:",
                "• Google Search (2019-10): Deploys BERT across 10% of all US",
                "  search queries (biggest quality leap since RankBrain).",
                "• OpenAI Five (2019-04): Beats Dota 2 world champs Team OG 2–0",
                "  after 45,000 yrs of self-play reinforcement learning.",
                "• Hugging Face (2019): transformers library becomes NLP standard.",
            ],
            "fails": [
                "WHO DID WHAT — HEADLINE FAILURES & SHOCKS:",
                "• Amazon Recruiting AI Scrapped (2018-10): Secret resume",
                "  model penalized applicants mentioning the word 'women's'.",
                "• OpenAI GPT-2 Staged Release Panic (2019-02): 1.5B weights",
                "  withheld as 'too dangerous to release' over fake news fears.",
                "• Static Word2Vec/GloVe collapses on polysemy ('bank' bug).",
            ],
            "learn": [
                "TOP THING TO LEARN (ERA 1 CURRICULUM):",
                "★ #1 Skill: Pretrained Encoder Fine-Tuning (BERT / ULMFiT)",
                "• Courses: Stanford CS224N (Manning) & Fast.ai v3 (Howard)",
                "• Core Action: Stop training BiLSTMs from scratch; load",
                "  AutoModelForSequenceClassification & fine-tune on V100s.",
            ],
        },
        # Era 2 (29 mos - wide)
        {
            "tech": [
                "STARTS ERA (2020-06 / 2021-06):",
                "• OpenAI GPT-3 davinci 175B Completion API (2020-06, USD 60/1M)",
                "• GitHub Copilot (Codex 12B IDE ghost text, 2021-06)",
                "ENDS / OUTDATES ERA (2022-10):",
                "• Raw completion drifts without stop tokens; 2k–4k context wall",
                "• Outdated by free ChatGPT dialog UI (2022-11) & USD 2/1M turbo",
            ],
            "wins": [
                "WHO DID WHAT — HEADLINE WINS:",
                "• GitHub Copilot GA (2022-06): 1.2M devs; controlled trial proves",
                "  coders finish tasks 55.8% faster (AI writes 40% of Python).",
                "• Jasper.ai (2022-10): Scales to USD 80M ARR & USD 1.5B valuation",
                "  wrapping GPT-3 templates for marketing teams.",
                "• DeepMind AlphaFold 2 (2020-11) & MSFT DeBERTa (2021-01).",
            ],
            "fails": [
                "WHO DID WHAT — HEADLINE FAILURES & SHOCKS:",
                "• Zillow Offers USD 500M+ ML Collapse (2021-11): Home-flipping",
                "  forecast models fail; USD 504M write-down & 2,000 laid off.",
                "• Meta Galactica Pulled in 72 Hours (2022-11): 120B science",
                "  LLM fabricates wiki papers ('History of Bears in Space').",
                "• AI Dungeon 'Filtergate' (2021-04) & USD 600/1M embed bills.",
            ],
            "learn": [
                "TOP THING TO LEARN (ERA 2 CURRICULUM):",
                "★ #1 Skill: Few-Shot In-Context Prompting & Vector Search",
                "• Courses: Stanford CS324 (Liang) & OpenAI API Cookbook",
                "• Core Action: Format 3–5 input/output examples, tune stop",
                "  tokens/temperature, and index chunks in FAISS/Pinecone.",
            ],
        },
        # Era 3 (19 mos - medium)
        {
            "tech": [
                "STARTS ERA (2022-11 / 2023-03):",
                "• ChatGPT RLHF Web UI (2022-11) & USD 2/1M gpt-3.5-turbo",
                "• GPT-4 (2023-03), Meta LLaMA & LangChain/Pinecone RAG",
                "ENDS / OUTDATES ERA (2024-05):",
                "• 8k–32k context & single-pass guessing break multi-doc RAG",
                "• Outdated by 200k–2M multimodal context, 90% KV-cache & o1",
            ],
            "wins": [
                "WHO DID WHAT — HEADLINE WINS:",
                "• ChatGPT (2023-01): Hits 100M monthly users in 60 days;",
                "  GPT-4 passes Uniform Bar Exam at 90th percentile.",
                "• Klarna (2024-02): AI assistant handles 2.3M chats in 1 mo",
                "  (work of 700 agents); Morgan Stanley deploys GPT-4 RAG",
                "  across 16,000 financial advisors.",
            ],
            "fails": [
                "WHO DID WHAT — HEADLINE FAILURES & SHOCKS:",
                "• Mata v. Avianca (2023-05): NY lawyers fined USD 5k for filing",
                "  6 fake court cases invented by ChatGPT.",
                "• Moffatt v. Air Canada (2024-02): Airline held legally",
                "  liable for chatbot bereavement refund hallucination.",
                "• Chegg crashes -48% (USD 1B lost, 2023-05); AutoGPT loops fail.",
            ],
            "learn": [
                "TOP THING TO LEARN (ERA 3 CURRICULUM):",
                "★ #1 Skill: Custom Vector RAG, 4-Bit QLoRA & LLM Evals",
                "• Courses: DeepLearning.AI Short Courses & Huyen/Yan Guides",
                "• Core Action: Build LangChain/LlamaIndex PDF chunkers,",
                "  LLM-as-a-Judge eval suites, and PEFT QLoRA adapters.",
            ],
        },
        # Era 4 (8 mos - narrow flashpoint! Keep strings concise <= 26 chars)
        {
            "tech": [
                "STARTS (2024-06):",
                "• GPT-4o & Sonnet 3.5",
                "• 90% KV-Cache & Cursor",
                "• OpenAI o1 RLVR (24-09)",
                "ENDS (2025-01):",
                "• Isolated o1 + manual IDE",
                "  replaced by CLI + MCP",
            ],
            "wins": [
                "HEADLINE WINS:",
                "• Cursor IDE: Passes",
                "  USD 100M ARR on Sonnet",
                "• NotebookLM: Viral 2-host",
                "  AI audio podcasts (24-09)",
                "• DeepSeek-R1 (25-01):",
                "  Matches o1 at 1/27th cost",
            ],
            "fails": [
                "HEADLINE FAILURES:",
                "• Devin USD 500/mo Audit:",
                "  Answer.AI finds 15% pass",
                "  (3/20 real tasks, 25-01)",
                "• Google AI Overviews:",
                "  'Glue on pizza' (24-05)",
                "• Nvidia -USD 589B drop",
            ],
            "learn": [
                "TOP SKILL TO LEARN:",
                "★ Multi-File IDE Pairing,",
                "  KV-Cache & LangGraph",
                "• DL.AI LangGraph & o1;",
                "  Anthropic Contextual RAG",
                "• Master .cursorrules &",
                "  cyclic state machines",
            ],
        },
        # Era 5 (21 mos - medium-wide)
        {
            "tech": [
                "STARTS ERA (2025-02 / 2025-03):",
                "• OpenAI Deep Research & Anthropic Claude Code CLI (2025-02)",
                "• Universal MCP Standard (2025-03) & Tool-Integrated RLVR (o3/GPT-5)",
                "CURRENT FRONTIER CEILING (2026-10):",
                "• Parallel git worktree agent fleets & custom GRPO RLVR flywheels",
                "• Bottlenecked by human PR review & staging database safety",
            ],
            "wins": [
                "WHO DID WHAT — HEADLINE WINS:",
                "• YC W25 Startups (2025-03): 25% of cohort ships production",
                "  codebases 95%+ written by Claude Code & Cursor agents.",
                "• Anthropic MCP & Ramp Index (2025–26): OpenAI/Google adopt",
                "  MCP; Claude reaches 43.5% corporate adoption share.",
                "• OpenAI Deep Research: Hits 26.6% on Humanity's Last Exam.",
            ],
            "fails": [
                "WHO DID WHAT — HEADLINE FAILURES & SHOCKS:",
                "• Replit Agent Deletes Live Prod DB (2025-07): Wipes 1,215",
                "  SaaStr executives during code freeze & fakes 4,000 rows.",
                "• GitHub MCP 'Lethal Trifecta' Exploit (2025-06): Invariant",
                "  Labs shows prompt injection exfiltrating private repos.",
                "• 10-agent worktree merge storms & USD 1k overnight loops.",
            ],
            "learn": [
                "TOP THING TO LEARN (ERA 5 CURRICULUM):",
                "★ #1 Skill: CLI Harness (CLAUDE.md), MCP & Worktree Fleets",
                "• Courses: Anthropic Claude Code Guide, DL.AI MCP, CS224N/324",
                "• Core Action: Orchestrate 3–10 parallel git worktree agents",
                "  with TDD guardrails & train custom verifiers/GRPO rewards.",
            ],
        },
    ]

    # Swimlane Y coordinates (bottom, height, label, border/tint color)
    lanes = [
        (7.15, 2.05, "SWIMLANE 1:\nTECH TRIGGERS\n(What Starts &\nEnds the Era)", "#0284C7", "#F0F9FF"),
        (4.85, 2.15, "SWIMLANE 2:\nDEFINING WINS\n('Who Did What'\nBreakthroughs)", "#059669", "#ECFDF5"),
        (2.55, 2.15, "SWIMLANE 3:\nDEFINING FAILURES\n('Who Did What'\nCautionary Tales)", "#DC2626", "#FEF2F2"),
        (0.25, 2.15, "SWIMLANE 4:\nTOP THING TO\nLEARN PER ERA\n(Skills & Courses)", "#7C3AED", "#F5F3FF"),
    ]

    x_min, x_max = 2017.25, 2027.00
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(0.05, 10.25)

    # Left swimlane labels via custom y-ticks
    ax.set_yticks([y0 + h / 2.0 for (y0, h, _, _, _) in lanes] + [9.68])
    ax.set_yticklabels([lbl for (_, _, lbl, _, _) in lanes] + ["ERA WINDOW &\nDURATION\n(Proportional X)"], fontsize=8.4, fontweight="bold")
    ax.tick_params(axis="x", labelbottom=False)

    # Vertical cutoff lines
    for t0, t1, mos, _, _, _ in era_bounds:
        ax.axvline(t0, color="#64748B", linestyle="--", lw=1.2, alpha=0.7, zorder=1)
    ax.axvline(era_bounds[-1][1], color="#64748B", linestyle="--", lw=1.2, alpha=0.7, zorder=1)

    # Draw Era Headers & 4 Swimlane Cards per Era
    for e_idx, (t0, t1, mos, e_title, e_dates, e_col) in enumerate(era_bounds):
        xl = t0 + (0.0 if e_idx == 0 else gap / 2.0)
        xr = t1 - (0.0 if e_idx == 4 else gap / 2.0)
        w = xr - xl
        xc = 0.5 * (xl + xr)
        is_narrow = (mos <= 10)

        # Top Era Header Box
        hdr = patches.FancyBboxPatch(
            (xl, 9.32), w, 0.76, boxstyle="round,pad=0.01,rounding_size=0.04",
            facecolor=e_col, edgecolor="#0F172A", lw=1.4, zorder=4
        )
        ax.add_patch(hdr)
        if is_narrow:
            ax.text(xc, 9.85, "L4 (8m)", color="white", fontweight="bold", fontsize=8.2, ha="center", va="center", zorder=5)
            ax.text(xc, 9.63, "24-06–25-01", color="white", fontweight="bold", fontsize=6.5, ha="center", va="center", zorder=5)
            ax.text(xc, 9.43, "Sonnet/o1", color="#F8FAFC", fontsize=6.3, ha="center", va="center", zorder=5)
        else:
            ax.text(xc, 9.84, f"{e_title}  [{mos} Months]", color="white", fontweight="bold", fontsize=8.8 if mos >= 20 else 8.0, ha="center", va="center", zorder=5)
            ax.text(xc, 9.50, f"Valid Window: {e_dates}  •  Width = {mos}/113 of Timeline", color="#F8FAFC", fontsize=7.3 if mos >= 20 else 6.8, ha="center", va="center", zorder=5)

        # Draw the 4 swimlane boxes for this era
        d_era = swimlane_data[e_idx]
        for l_idx, (key, (y0, h, _, l_col, l_bg)) in enumerate(zip(["tech", "wins", "fails", "learn"], lanes)):
            card = patches.FancyBboxPatch(
                (xl, y0), w, h, boxstyle="round,pad=0.01,rounding_size=0.04",
                facecolor=l_bg, edgecolor=l_col, lw=1.5, zorder=3
            )
            ax.add_patch(card)

            lines = d_era[key]
            n_lines = len(lines)
            f_hdr = 6.2 if is_narrow else (7.6 if mos >= 25 else 7.0)
            f_txt = 5.9 if is_narrow else (7.2 if mos >= 25 else 6.65)

            for line_i, line_str in enumerate(lines):
                yy = y0 + h - 0.18 - line_i * ((h - 0.28) / max(n_lines - 1, 1))
                is_header_line = line_str.isupper() or line_str.startswith("★") or line_str.startswith("STARTS") or line_str.startswith("ENDS") or line_str.startswith("CURRENT") or line_str.startswith("HEADLINE") or line_str.startswith("TOP")
                ax.text(
                    xl + (0.025 if is_narrow else 0.045),
                    yy,
                    line_str,
                    fontsize=f_hdr if is_header_line else f_txt,
                    fontweight="bold" if is_header_line else "normal",
                    color=l_col if is_header_line else PALETTE["TEXT"],
                    ha="left",
                    va="center",
                    zorder=5,
                )

    # Bottom Pinpoint Timeline Track (ax_pin): Exact Dated Milestones on Continuous Time Axis with 4-tier vertical stagger
    ax_pin.set_xlim(x_min, x_max)
    ax_pin.set_ylim(-0.08, 1.08)
    ax_pin.set_yticks([])
    year_ticks = np.arange(2017, 2028, 1)
    ax_pin.set_xticks(year_ticks)
    ax_pin.set_xticklabels([f"{y}-01" for y in year_ticks], fontsize=9.2, fontweight="bold")
    ax_pin.set_xlabel("Continuous Calendar Time Axis (2017-06 to 2026-10 — Exact YYYY-MM Milestone Pins)", fontsize=9.8, fontweight="bold")
    ax_pin.axhline(0.50, color="#0F172A", lw=2.2, zorder=2)
    ax_pin.grid(True, axis="x", linestyle="--", color=PALETTE["GRID"], alpha=0.65)

    # (decimal_year, label, y_stem_end, color)
    milestones = [
        (2017 + 5/12, "2017-06\nTransformer", 0.80, PALETTE["GONE"]),
        (2018 + 9/12, "2018-10\nBERT & Amzn Bias", 0.20, PALETTE["GONE"]),
        (2019 + 9/12, "2019-10\nGoogle BERT Search", 0.80, PALETTE["GONE"]),
        (2020 + 5/12, "2020-06\nGPT-3 API (L2)", 0.20, PALETTE["SUNK"]),
        (2021 + 5/12, "2021-06\nCopilot Preview", 0.80, PALETTE["SUNK"]),
        (2021 + 10/12, "2021-11\nZillow USD 500M Bust", 0.20, PALETTE["SUNK"]),
        (2022 + 10/12, "2022-11\nChatGPT (L3)", 0.80, PALETTE["EVOLVED"]),
        (2023 + 4/12, "2023-05\nMata v. Avianca", 0.20, PALETTE["EVOLVED"]),
        (2024 + 1/12, "2024-02\nKlarna / Air Canada", 0.84, PALETTE["EVOLVED"]),
        (2024 + 5/12, "2024-06\nSonnet 3.5 (L4)", 0.24, PALETTE["SPLIT"]),
        (2024 + 8/12, "2024-09\no1 & NotebookLM", 0.65, PALETTE["SPLIT"]),
        (2025 + 0/12, "2025-01\nDeepSeek-R1 / Devin", 0.08, PALETTE["SPLIT"]),
        (2025 + 1/12, "2025-02\nClaude Code (L5)", 0.88, PALETTE["NEW"]),
        (2025 + 6/12, "2025-07\nReplit DB Wipe", 0.22, PALETTE["NEW"]),
        (2026 + 5/12, "2026-06\nRamp 43.5% Claude", 0.80, PALETTE["NEW"]),
    ]
    for tm, mlbl, y_target, mcol in milestones:
        is_top = (y_target > 0.50)
        ax_pin.plot([tm, tm], [0.50, y_target], color=mcol, lw=1.5, zorder=3)
        ax_pin.scatter([tm], [0.50], s=48, color=mcol, edgecolors="white", lw=1.0, zorder=4)
        ax_pin.text(tm, y_target + (0.04 if is_top else -0.04), mlbl, ha="center", va="bottom" if is_top else "top", fontsize=6.8, fontweight="bold", color=mcol)

    for p in out_paths:
        fig.savefig(p, dpi=240, bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    poster_paths = [
        os.path.join(ARTIFACT_DIR, "fig_full_evolution_poster.png"),
        os.path.join(PERSONAL_FIG_DIR, "fig_full_evolution_poster.png"),
        os.path.join(WORKSPACE_FIG_DIR, "fig_full_evolution_poster.png"),
    ]
    draw_full_evolution_poster(poster_paths)
    print("Rendered fig_full_evolution_poster.png")

    news_poster_paths = [
        os.path.join(ARTIFACT_DIR, "fig_era_defining_news_and_learning_poster.png"),
        os.path.join(PERSONAL_FIG_DIR, "fig_era_defining_news_and_learning_poster.png"),
        os.path.join(WORKSPACE_FIG_DIR, "fig_era_defining_news_and_learning_poster.png"),
    ]
    draw_era_defining_news_poster(news_poster_paths)
    print("Rendered fig_era_defining_news_and_learning_poster.png")

    with open(os.path.join(ARTIFACT_DIR, "scratch", "ladder_metrics.json"), "w") as f:
        json.dump({"eras": ERAS, "transitions": TRANSITIONS}, f, indent=2)
    print("Saved scratch/ladder_metrics.json")

