"""
Standalone AI Usage Level (1-6) Self-Diagnosis Skill-Tree Chart & Report (Jan 2025 – Nov 2026)
==============================================================================================
Option 3 Action-Oriented Categories + Red-Team Visual & Safety/Alignment/Governance Architecture:
1. 4 Columns (3 Wide Action-Oriented Skill-Tree Pillars + 1 Narrower Obsolete Sidebar):
   - THINK, SEARCH & ANALYZE  (Research · Writing · Data & Docs · RAG · Reasoning & Alignment)
   - CREATE & DESIGN (MEDIA)  (Image · Video · Audio · Voice · 3D · Provenance & DiT)
   - AUTOMATE & BUILD (CODE)  (Workflows · AI IDEs · Agents · Evals, Safety & Training)
   - OBSOLETE  (Still Doing This? You're Behind — no cross bullets)
2. Safety, Alignment, Reward Hacking, Fairness, Audit Trails & Compliance Integrated at Every Level:
   - Level 1: Hallucination Fact-Check, Data Training Opt-Out, Deepfake / Watermark Spot
   - Level 2: Zero-Data-Retention (ZDR), PII Redaction, Citation & Source Verification
   - Level 3: Human-in-Loop Tool Approval, AI Code Security Scan, Spend & Rate-Limit Caps
   - Level 4: CI Evals, Audit Trails & OTel Tracing, Guardrails & PII Filters, Fairness & Bias Evals,
              EU AI Act / SOC2 Compliance Logs, Prompt Injection Red-Teaming, C2PA / SynthID
   - Level 5: DPO/ORPO Alignment, Constitutional / RLAIF Data, Activation Steering,
              Refusal Calibration, Bias/Toxicity Filtering, Machine Unlearning
   - Level 6: Scalable Oversight & Weak-to-Strong, Reward Hacking & Sycophancy Defense,
              Mechanistic Interpretability (SAEs & Circuit Tracing), Deliberative CoT Alignment,
              Scheming & Sandbagging Evals, Instruction Hierarchy, ASL / CBRN Safety Evals
"""

from datetime import datetime
from pathlib import Path
import textwrap
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

REPO_ROOT = Path("/Users/z3540725/My Drive/personal/2026 10 17 AI_ladder_evol")
ROOT = REPO_ROOT / "dev"
FIG_DIR = ROOT / "figures_v5"
FIG_DIR.mkdir(parents=True, exist_ok=True)

OUT_PNG = FIG_DIR / "fig_v5_current_gen_self_diagnosis.png"
OUT_TOP_PNG = REPO_ROOT / "AI_skill_tree_2026.png"
OUT_TOP_PDF = REPO_ROOT / "AI_skill_tree_2026.pdf"
OUT_MOBILE_PNG = FIG_DIR / "fig_v5_mini_self_diagnosis_mobile.png"
OUT_MD = ROOT / "2026 11 04 AI_usage_level_keyword_quiz.md"

plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["ps.fonttype"] = 42

_now_local = datetime.now().astimezone()
_utc_off = _now_local.strftime("%z")
_utc_off_colon = f"{_utc_off[:3]}:{_utc_off[3:]}" if len(_utc_off) == 5 else _utc_off
LAST_UPDATED_STR = f"Updated: {_now_local.strftime('%Y-%m-%d %H:%M:%S %Z')} (UTC{_utc_off_colon})"


# =============================================================================
# 4 CATEGORY COLUMNS (OPTION 3: HOW YOU USE AI + OBSOLETE SIDEBAR)
# =============================================================================
CATEGORIES = [
    {
        "key": "think_search_analyze",
        "title": "THINK, SEARCH & ANALYZE",
        "sub": "Research · Data & Docs · RAG · Reasoning & Alignment",
        "hdr_bg": "#0F766E",
        "cell_bg": "#FFFFFF",
        "t2_bg": "#F8FAFC",
        "t3_bg": "#F1F5F9",
        "cell_edge": "#0D9488",
        "h1_bg": "#CCFBF1",
        "pill_edge": "#0F766E",
        "h1_txt": "#115E59",
        "t2_txt": "#0F172A",
        "t3_txt": "#475569",
        "div_col": "#99F6E4",
    },
    {
        "key": "create_design_media",
        "title": "CREATE & DESIGN (MEDIA)",
        "sub": "Image · Video · Audio · Voice · 3D · Provenance & DiT",
        "hdr_bg": "#6D28D9",
        "cell_bg": "#FFFFFF",
        "t2_bg": "#F8FAFC",
        "t3_bg": "#F1F5F9",
        "cell_edge": "#7C3AED",
        "h1_bg": "#EDE9FE",
        "pill_edge": "#6D28D9",
        "h1_txt": "#4C1D95",
        "t2_txt": "#0F172A",
        "t3_txt": "#475569",
        "div_col": "#DDD6FE",
    },
    {
        "key": "automate_build_code",
        "title": "AUTOMATE & BUILD (CODE)",
        "sub": "Workflows · AI IDEs · Agents · Evals, Safety & Training",
        "hdr_bg": "#1D4ED8",
        "cell_bg": "#FFFFFF",
        "t2_bg": "#F8FAFC",
        "t3_bg": "#F1F5F9",
        "cell_edge": "#2563EB",
        "h1_bg": "#DBEAFE",
        "pill_edge": "#1D4ED8",
        "h1_txt": "#1E3A8A",
        "t2_txt": "#0F172A",
        "t3_txt": "#475569",
        "div_col": "#BFDBFE",
    },
    {
        "key": "obsolete",
        "title": "OBSOLETE",
        "sub": "Still Doing This? You're Behind",
        "hdr_bg": "#991B1B",
        "cell_bg": "#FFF5F5",
        "t2_bg": "#FEF2F2",
        "t3_bg": "#FEE2E2",
        "cell_edge": "#DC2626",
        "h1_bg": "#FEE2E2",
        "pill_edge": "#B91C1C",
        "h1_txt": "#7F1D1D",
        "t2_txt": "#991B1B",
        "t3_txt": "#991B1B",
        "div_col": "#FECACA",
    },
]


# =============================================================================
# 6 LEVELS x 4 COLUMNS (SAFETY, ALIGNMENT, AUDIT TRAILS & FAIRNESS INTEGRATED)
# =============================================================================
LEVEL_ROWS = [
    {
        "level": 1,
        "badge": "LEVEL 1",
        "meter": "1/6",
        "name": "EVERYDAY CONSUMER",
        "desc": "Uses default consumer AI apps as a conversational search engine, writing assistant, and instant media helper.",
        "persona": "Casual daily user & general public.",
        "surface": "Phone app, web browser & built-in OS assistant on any phone or laptop.",
        "use_cases": "Search replacement, drafting emails/texts, summarizing PDFs/videos, live voice & casual image gen.",
        "accent": "#10B981",
        "cells": {
            "think_search_analyze": {
                "h1": [
                    "ChatGPT / Claude Daily Q&A",
                    "Perplexity Cited Web Search",
                    "PDF & Article Upload Summary",
                ],
                "normal": [
                    "Google Search AI Overviews",
                    "Gemini Mobile Assistant",
                    "Web Browsing in Chat",
                    "Android Circle to Search",
                    "Apple AI Writing Tools",
                    "Meta AI in WhatsApp / IG",
                    "Hallucination Fact-Check",
                    "Draft & Rewrite Emails",
                ],
                "small": [
                    "DeepSeek Free Web / App",
                    "TLDR Thread Summarize",
                    "Grammar & Tone Polish",
                    "YouTube Video Summary",
                    "Gmail / Outlook Auto-Draft",
                    "Foreign Language Chat",
                    "Travel Itinerary Planner",
                    "Excel / Sheets Formulas",
                    "Click Cited Source Links",
                    "Memory On / Off Toggle",
                    "Data Training Opt-Out",
                    "Temporary Incognito Chat",
                ],
            },
            "create_design_media": {
                "h1": [
                    "ChatGPT Live Voice Mode",
                    "Conversational Image Gen (4o)",
                    "Phone Camera Live Vision Q&A",
                ],
                "normal": [
                    "Gemini Live Voice Chat",
                    "Google Lens Visual Q&A",
                    "Mobile OS Voice Dictation",
                    "Magic Eraser Photo Unblur",
                    "Canva Magic Media Studio",
                    "iOS Genmoji / Image Wand",
                    "Screenshot OCR Translate",
                    "Zoom / Meet AI Summaries",
                ],
                "small": [
                    "Google Imagen / ImageFX",
                    "Bing Image Creator",
                    "Auto-Captions on Video",
                    "Spotify AI Playlist DJ",
                    "1-Click BG Removal",
                    "Receipt Photo Expense",
                    "Voice Memo Transcript",
                    "Google Photos Ask-Photos",
                    "Whiteboard Photo Read",
                    "Menu Photo Translation",
                    "Spot AI / Deepfake Tells",
                    "Short-Video Auto-Clip",
                ],
            },
            # Level 1 Everyday Consumer does NOT automate or build -> Rendered as intentional N/A panel!
            "automate_build_code": {
                "h1": [],
                "normal": [],
                "small": [],
            },
            "obsolete": {
                "h1": [
                    '"Act as a..." Jailbreaks',
                    "Buying 10k Prompt PDFs",
                    "Blindly Trusting AI Claims",
                ],
                "normal": [
                    "ChatGPT w/o Web Search",
                    "Copy-Pasting 1 Para Only",
                    "ChatGPT Plugins Store",
                    "Google Bard / Bing Sydney",
                    "DALL-E mini / Craiyon",
                    "Short 3-Word Prompts",
                    "Passwords in Public Chat",
                    "AI Voice-Clone Scams",
                    "AI as Medical/Legal Fact",
                    "Ignoring Source Links",
                ],
                "small": [],
            },
        },
    },
    {
        "level": 2,
        "badge": "LEVEL 2",
        "meter": "2/6",
        "name": "WORKSPACE POWER USER",
        "desc": "Orchestrates paid reasoning models, deep-research agents, and interactive canvases across multi-file workspaces.",
        "persona": "Knowledge worker, analyst, designer & solo operator.",
        "surface": "Paid web workspaces, desktop apps, multi-source notebooks & creative studios.",
        "use_cases": "Deep research reports, multi-doc synthesis, interactive canvases & consistent media.",
        "accent": "#14B8A6",
        "cells": {
            "think_search_analyze": {
                "h1": [
                    "Multi-Step Deep Research",
                    "Extended Thinking (o3 / Claude)",
                    "Data Analysis & Chart Canvas",
                ],
                "normal": [
                    "Projects & Custom GPTs",
                    "NotebookLM 50-Source Pod",
                    "DeepSeek-R1 DeepThink",
                    "Gemini 1M–2M Token Upload",
                    "Perplexity Pro Spaces",
                    "Multi-Doc Cross-Audit",
                    "Zero-Data-Retention (ZDR)",
                    "Critique-Then-Revise Loop",
                ],
                "small": [
                    "Grok-3 DeepSearch Mode",
                    "LMSYS Chatbot Arena",
                    "Side-by-Side Model Check",
                    "Context Token Trimming",
                    "CSV / Excel Code Sandbox",
                    "PII Redaction Before Upload",
                    "Full-Book PDF Q&A",
                    "Earnings Call Synthesis",
                    "Literature Review Matrix",
                    "Rubric Self-Grading",
                    "Role-Separated Debate",
                    "Citation Source Audit",
                ],
            },
            "create_design_media": {
                "h1": [
                    "Midjourney --sref / --cref Refs",
                    "Sora 2 / Veo 2 / Runway Video",
                    "ElevenLabs Instant Voice Clone",
                ],
                "normal": [
                    "NotebookLM Audio Host",
                    "Kling / Luma Keyframes",
                    "Ideogram / 4o Text-Image",
                    "Suno v4 / Udio Song Gen",
                    "HeyGen Video Translate",
                    "Superwhisper / Wispr Flow",
                    "Adobe Firefly Gen-Fill",
                    "Live Screen-Share Vision",
                ],
                "small": [
                    "Pika Scene Ingredients",
                    "Descript Overdub & Eye",
                    "Topaz AI Video Upscale",
                    "Captions.ai Avatar",
                    "Hedra Character-2 Sync",
                    "Leonardo Phoenix Canvas",
                    "Recraft Brand Vectors",
                    "Spline AI 3D Prompts",
                    "Stem Splitter Isolation",
                    "Photoshop Gen-Expand",
                    "Commercial IP-Safe Models",
                    "Voice Consent Verification",
                ],
            },
            # Level 2 uses No-Code Canvases, Web Agents & Workspace Automations (full 23 items)
            "automate_build_code": {
                "h1": [
                    "Claude Artifacts (React / SVG)",
                    "ChatGPT Agent / Operator Mode",
                    "Zapier / Make No-Code AI Flows",
                ],
                "normal": [
                    "ChatGPT Canvas Co-Editor",
                    "Scheduled AI Tasks & Alerts",
                    "Notion AI & M365 Copilot",
                    "Raycast AI Quick Commands",
                    "Granola / Fireflies Notes",
                    "Airtable / Sheets AI Agents",
                    "Custom GPT Action Webhooks",
                    "Workspace SSO & Audit Logs",
                ],
                "small": [
                    "Apple Shortcuts AI Actions",
                    "Browser AI Sidebar Actions",
                    "Linear / Jira AI Triage",
                    "Superhuman / Gmail AI Rules",
                    "Slack AI Channel Digests",
                    "Loom AI Auto-Workflows",
                    "Tally / Typeform AI Routing",
                    "Coda AI Doc Automations",
                    "TextExpander / Alfred Snips",
                    "Readwise Reader AI Ghost",
                    "Mermaid / Whimsical AI Flow",
                    "Role-Based Access (RBAC)",
                ],
            },
            "obsolete": {
                "h1": [
                    '"Let\'s think step by step"',
                    '"Prompt Engineer" ($300k)',
                    "Uploading Client PII to Chat",
                ],
                "normal": [
                    "Tipping $200 / Threats",
                    '"6 fingers" Neg Prompts',
                    "Midjourney Discord Bot",
                    "Custom GPT Store Hype",
                    "Manual 4k Text Splits",
                    "1-Page Prompt Walls",
                    "Copy-Pasting CSV Tables",
                    "Manual Zoom Note-Taking",
                    "Fake Legal Citations",
                    "Shadow AI w/o IT SSO",
                ],
                "small": [],
            },
        },
    },
    {
        "level": 3,
        "badge": "LEVEL 3",
        "meter": "3/6",
        "name": "VIBE CODER & BUILDER",
        "desc": "Ships full-stack apps and multi-step automations by directing AI IDEs, CLI coding agents, and cloud APIs.",
        "persona": "Indie builder, automation maker & AI-native developer.",
        "surface": "AI IDEs (Cursor/Windsurf), CLI agents (Claude Code), app builders & APIs.",
        "use_cases": "Natural-language app shipping, multi-file repo refactoring, MCP/webhook flows & API media pipes.",
        "accent": "#3B82F6",
        "cells": {
            "think_search_analyze": {
                "h1": [
                    "Spec-First PRD & XML Prompts",
                    "Tavily / Exa / Firecrawl API",
                    "Repomix / Gitingest Packing",
                ],
                "normal": [
                    "System vs User Role Split",
                    "llms.txt Docs Standard",
                    "Jina Reader URL-Markdown",
                    "Context Window Budgeting",
                    "Markdown Memory Banks",
                    "Multi-Step Prompt Chains",
                    "Few-Shot JSON Examples",
                    "OpenRouter Benchmarking",
                ],
                "small": [
                    "Perplexity Sonar API",
                    "Brave Search Grounding",
                    "Unstructured PDF API",
                    "Prompt Git Versioning",
                    "Token Cost & Spend Caps",
                    "Fallback Model Retries",
                    "Streaming SSE Responses",
                    "Temp / Top-P API Tuning",
                    "Stop-Sequence Control",
                    "Needle-in-Haystack Check",
                    "Untrusted Input Delimiters",
                    "SQL / Pandas Query via AI",
                ],
            },
            "create_design_media": {
                "h1": [
                    "ComfyUI Ready Workflows",
                    "Fal.ai / Replicate Webhooks",
                    "ElevenLabs / Vapi Voice API",
                ],
                "normal": [
                    "Black Forest Flux API",
                    "Remotion Code-to-Video",
                    "Whisper + FFmpeg Subs",
                    "Sync.so Lip-Sync API",
                    "Recraft v3 Vector API",
                    "Figma-to-Code Plugins",
                    "Magnific / Krea Upscale",
                    "Luma / Meshy 3D Assets",
                ],
                "small": [
                    "Runway Act-One API",
                    "Hume Empathic Voice API",
                    "Retell Phone Webhooks",
                    "AssemblyAI Diarization",
                    "Creatomate JSON Video",
                    "Photoroom Batch API",
                    "LivePortrait Face API",
                    "Mux Video Auto-Chapters",
                    "PlayHT Low-Latency TTS",
                    "Gladia Multilingual ASR",
                    "C2PA / SynthID Metadata",
                    "NSFW Moderation API Gate",
                ],
            },
            "automate_build_code": {
                "h1": [
                    "Cursor / Windsurf Agent Mode",
                    "Claude Code CLI & CLAUDE.md",
                    "Lovable / Bolt / v0 / Replit",
                ],
                "normal": [
                    ".cursor/rules & AGENTS.md",
                    "Claude Desktop MCP & n8n",
                    "Context7 Live Docs MCP",
                    "Plan-Before-Act & Diffs",
                    "Human-in-Loop Tool Approve",
                    "Cline / Roo Code / Aider",
                    "Browser-Use / Stagehand",
                    "Vercel AI SDK & Supabase",
                ],
                "small": [
                    "Ollama / LM Studio Local",
                    "Groq / Cerebras LPU API",
                    "LiteLLM / CF AI Gateway",
                    "Together / Fireworks API",
                    "Helicone / LangSmith Logs",
                    "AI Code Security Scan",
                    "Playwright AI E2E Tests",
                    "Secret & API-Key Scrubbing",
                    "Regex / Bash / Git via AI",
                    "GitHub Actions PR Bot",
                    "Slopsquat Package Check",
                    "Stripe + Auth0 Vibe Ship",
                ],
            },
            "obsolete": {
                "h1": [
                    "AutoGPT / BabyAGI Loops",
                    "Ghost-Text Autocomplete",
                    "Blindly Running Agent rm -rf",
                ],
                "normal": [
                    "API Keys in Public Git",
                    "Copy-Pasting StackTraces",
                    "Legacy .cursorrules Dump",
                    "50-Node Flowise Chains",
                    "Manual Regex Scraping",
                    "Pasting Files to Web UI",
                    "No Git Commit Pre-Agent",
                    "Shipping AI SQL w/o Auth",
                    "No API Spend / Rate Cap",
                    "Fake Slopsquat Packages",
                ],
                "small": [],
            },
        },
    },
    {
        "level": 4,
        "badge": "LEVEL 4",
        "meter": "4/6",
        "name": "AI & AGENT ENGINEER",
        "desc": "Architects production multi-agent backends with schema-enforced tool use, hybrid RAG, guardrails, audit traces, and CI evals.",
        "persona": "Production AI software engineer & systems architect.",
        "surface": "Python/TS SDKs, custom MCP servers, state graphs, microVM sandboxes & observability stacks.",
        "use_cases": "Stateful multi-agent backends, hybrid RAG, guardrails, audit trails, compliance & CI eval gates.",
        "accent": "#6366F1",
        "cells": {
            "think_search_analyze": {
                "h1": [
                    "Pydantic / Zod Schema Outputs",
                    "Hybrid RAG + Cross-Rerankers",
                    "ColPali & Docling PDF RAG",
                ],
                "normal": [
                    "Prompt Caching (90% Saved)",
                    "Hallucination & Faithfulness",
                    "Anthropic Thinking Tokens",
                    "Contextual & GraphRAG",
                    "DSPy Prompt Optimization",
                    "BAML Typed Prompt Calls",
                    "Cohere Rerank-v3.5 Pipe",
                    "Citation Span Grounding",
                ],
                "small": [
                    "Hypothetical Embed (HyDE)",
                    "Parent-Doc Late Chunking",
                    "Reciprocal Rank Fusion",
                    "Corrective RAG (CRAG)",
                    "Semantic Intent Router",
                    "Multi-Query RAG Expand",
                    "Surya / LayoutLM Tables",
                    "Demographic Fairness Eval",
                    "PII & Bias Leakage Audits",
                    "Faithfulness Gate Check",
                    "Time-Weighted Memory",
                    "Golden Retrieval Recall",
                ],
            },
            "create_design_media": {
                "h1": [
                    "OpenAI / Gemini WebRTC API",
                    "LiveKit / Pipecat Voice AI",
                    "Programmatic ComfyUI API",
                ],
                "normal": [
                    "Deepgram Nova-3 Stream",
                    "Cartesia / Kokoro TTS",
                    "Vision-LLM UI Grounding",
                    "Barge-In VAD Interruption",
                    "Twilio SIP Call Bridging",
                    "TwelveLabs Video Search",
                    "CLIP / SigLIP Visual RAG",
                    "WebSocket PCM16 Streams",
                ],
                "small": [
                    "Frame-Accurate Video Cut",
                    "Silero VAD Turn-Taking",
                    "Daily.co WebRTC Mesh",
                    "HeyGen Streaming Avatar",
                    "WhisperX Word Timestamps",
                    "pyannote Speaker Diarize",
                    "Bounding-Box Detection",
                    "Deepfake / Spoof Detection",
                    "C2PA Cryptographic Sign",
                    "Sub-500ms Voice Loop",
                    "Audio Watermark Check",
                    "3D Gaussian Asset API",
                ],
            },
            "automate_build_code": {
                "h1": [
                    "Custom MCP Servers & OAuth",
                    "LangGraph Durable State Graphs",
                    "Promptfoo / Braintrust CI Evals",
                ],
                "normal": [
                    "E2B / Modal Sandboxes",
                    "Audit Trails & OTel Traces",
                    "Llama-Guard / NeMo Rails",
                    "LLM-as-a-Judge Rubrics",
                    "Git Worktree Subagents",
                    "OpenAI SDK / PydanticAI",
                    "Qdrant / Milvus / pgvector",
                    "SWE-bench Eval Harness",
                ],
                "small": [
                    "Prompt Injection Red-Team",
                    "EU AI Act / SOC2 Audit Logs",
                    "Firecracker MicroVMs",
                    "Human-in-Loop Interrupts",
                    "Agent Memory (Mem0/Letta)",
                    "Temporal Durable Exec",
                    "Redis Semantic Caching",
                    "Langfuse / Phoenix Spans",
                    "Cascade Model Cost Router",
                    "Canary / Shadow Deploys",
                    "RBAC Tool-Permission Gate",
                    "A2A Agent2Agent Protocol",
                ],
            },
            "obsolete": {
                "h1": [
                    "Shipping w/o Evals or Traces",
                    "Naive 500-Tok Vector RAG",
                    "Regex-Parsing LLM JSON",
                ],
                "normal": [
                    "Un-Sandboxed Code Exec",
                    "Fine-Tuning to Add Facts",
                    "LangChain LLMChain Class",
                    "Assistants API v1 Polls",
                    "text-embedding-ada-002",
                    "Pinecone Pod-Index Lock",
                    "No Injection Guardrails",
                    "No Tool Audit Logging",
                    "No Model Fallback Route",
                    "Vibe-Check Only Evals",
                ],
                "small": [],
            },
        },
    },
    {
        "level": 5,
        "badge": "LEVEL 5",
        "meter": "5/6",
        "name": "LOCAL & POST-TRAINING",
        "desc": "Serves quantized open-weight models on dedicated GPUs/Macs and aligns weights via QLoRA, DPO, GRPO, and steering.",
        "persona": "ML systems engineer, local-first builder & model post-trainer.",
        "surface": "Multi-GPU rig (RTX 3090/4090/5090), unified-memory Mac, vLLM, SGLang & Unsloth.",
        "use_cases": "High-throughput local serving, QLoRA/DPO/GRPO alignment, weight merging & air-gapped AI.",
        "accent": "#8B5CF6",
        "cells": {
            "think_search_analyze": {
                "h1": [
                    "Synthetic CoT Dataset Curation",
                    "Rejection-Sampled SFT / DPO",
                    "Grammar-Constrained GBNF / JSON",
                ],
                "normal": [
                    "Local DeepSeek-R1 & Qwen-3",
                    "Constitutional / RLAIF Data",
                    "RoPE Scaling (YaRN)",
                    "Min-P / DRY / XTC Sample",
                    "DPO Chosen/Reject Pairs",
                    "Custom ChatML Templates",
                    "Air-Gapped Hybrid RAG",
                    "Domain Eval Benchmarks",
                ],
                "small": [
                    "Refusal Boundary Tuning",
                    "Bias & Toxicity Filtering",
                    "Perplexity Quant Audit",
                    "KL-Divergence Drift Check",
                    "De-Duplicated FT Corpora",
                    "ShareGPT Multi-Turn Data",
                    "System Prompt Distill",
                    "Local BGE-Reranker",
                    "Air-Gapped Citations",
                    "CoT Trace Length Tuning",
                    "RAGAS Local Faithfulness",
                    "Data Contamination Check",
                ],
            },
            "create_design_media": {
                "h1": [
                    "ComfyUI Custom Node Pipelines",
                    "Flux.1 / Wan-2.1 Local Weights",
                    "Kohya / AI-Toolkit LoRA Train",
                ],
                "normal": [
                    "ControlNet & IP-Adapter",
                    "Whisper-v3-turbo Local",
                    "Kokoro-82M / F5-TTS Local",
                    "RVC / So-VITS Voice Clone",
                    "Florence-2 & SAM-2 Vision",
                    "GGUF FP8 Flux Offload",
                    "TensorRT Diffusion Accel",
                    "HunyuanVideo / Mochi Run",
                ],
                "small": [
                    "TeaCache / WaveSpeed",
                    "Chatterbox / Orpheus TTS",
                    "faster-whisper CTranslate",
                    "AnimateDiff Motion Nodes",
                    "Depth-Anything ControlNet",
                    "InstantID / FaceID Nodes",
                    "CosyVoice2 / Fish-Speech",
                    "Ultimate-SD Tiled VAE",
                    "SageAttention Speedup",
                    "JoyCaption VLM Tagging",
                    "Concept Erasure LoRA",
                    "Watermark-Preserving Gen",
                ],
            },
            "automate_build_code": {
                "h1": [
                    "vLLM / SGLang GPU Serving",
                    "Unsloth / Axolotl / TRL QLoRA",
                    "DPO / ORPO / Local GRPO Tune",
                ],
                "normal": [
                    "EXL2 / AWQ / GGUF / FP8",
                    "SGLang RadixAttention",
                    "Outlines / XGrammar FSM",
                    "Speculative Decode (EAGLE)",
                    "MergeKit SLERP/TIES/DARE",
                    "Activation Steering Vectors",
                    "KV-Cache FP8 / INT4 Quant",
                    "Apple MLX / Dual-4090 Rig",
                ],
                "small": [
                    "llama.cpp / KoboldCpp",
                    "LLaMA-Factory Training",
                    "vLLM Multi-LoRA Serving",
                    "Qwen-Coder-32B Local IDE",
                    "Machine Unlearning Runs",
                    "Local Stdio MCP & SQLite",
                    "Hermes-3 Local Tool Call",
                    "OmniParser GUI Grounding",
                    "Adversarial Jailbreak Eval",
                    "Prefill-Decode Disagg",
                    "lm-eval-harness Local",
                    "imatrix Importance Quant",
                ],
            },
            "obsolete": {
                "h1": [
                    "Full-Weight 7B Style FT",
                    "Automatic1111 SD 1.5 UI",
                    "SFT Without KL / Eval Checks",
                ],
                "normal": [
                    "8-bit bitsandbytes Slow",
                    "Oobabooga Text-Gen UI",
                    "Manual GPTQ Calibration",
                    "DreamBooth 40m Colab",
                    "LoRA Rank-128 Overfit",
                    "Raw Alpaca 52k SFT Set",
                    "Static RoPE Alpha Hacks",
                    "Flask Single-Batch API",
                    "Blind Frankenmerges",
                    "FT Without Safety Evals",
                ],
                "small": [],
            },
        },
    },
    {
        "level": 6,
        "badge": "LEVEL 6",
        "meter": "6/6",
        "name": "FRONTIER RESEARCHER",
        "desc": "Pre-trains foundation models, designs verifiable RL & scalable-oversight alignment, and authors custom GPU kernels.",
        "persona": "Foundation model scientist, alignment researcher & kernel author.",
        "surface": "Multi-node H100/B200/TPU clusters, InfiniBand fabrics, FSDP2/Megatron & CUDA/Triton.",
        "use_cases": "Base/MoE pre-training, RLVR/GRPO, mechanistic interpretability, scalable oversight & GPU kernels.",
        "accent": "#EC4899",
        "cells": {
            "think_search_analyze": {
                "h1": [
                    "RLVR (Verifiable Reward RL)",
                    "GRPO (Group Relative Policy)",
                    "Test-Time Compute Scaling",
                ],
                "normal": [
                    "Scalable Oversight & Debate",
                    "Reward Hacking Defense",
                    "Process Reward Model (PRM)",
                    "MCTS Tree-Search Reason",
                    "AlphaProof / Lean-4 RL",
                    "Deliberative CoT Alignment",
                    "Pass@k → Pass@1 Distill",
                    "Benchmark Decontam LSH",
                ],
                "small": [
                    "Scheming & Sandbag Evals",
                    "Weak-to-Strong Generalize",
                    "Instruction Hierarchy RL",
                    "Aha-Moment Backtracking",
                    "VinePPO / ReST-MCTS* Tree",
                    "KL-Divergence Ref Clip",
                    "Curriculum Difficulty RL",
                    "Coconut Latent Space CoT",
                    "Math-Shepherd Verifiers",
                    "CoT Monitorability Checks",
                    "Specification Gaming Fix",
                    "AlphaEvolve Search Loop",
                ],
            },
            "create_design_media": {
                "h1": [
                    "Rectified Flow Matching (DiT)",
                    "Native Early-Fusion Omni-Modal",
                    "3D Spatio-Temporal Video VAE",
                ],
                "normal": [
                    "Discrete Audio Tok (Mimi)",
                    "Consistency Flow Distill",
                    "Autoregressive Visual Tok",
                    "Interleaved Omni Attend",
                    "Chameleon / Transfusion",
                    "3D Gaussian Splatting",
                    "Full-Duplex Speech Model",
                    "JEPA / Genie-2 World Sim",
                ],
                "small": [
                    "Cross-Modal Contrastive",
                    "Rotary 3D-RoPE Video Pos",
                    "CFG Guidance Distillation",
                    "MMDiT Dual-Stream Blocks",
                    "VQ-GAN / FSQ Scalar Quant",
                    "MAR Masked Autoregressive",
                    "SoundStorm Parallel Audio",
                    "Latent Concept Erasure",
                    "Tree-Ring Latent Watermark",
                    "Spatio-Temporal Patchify",
                    "Distribution Match Distill",
                    "Physics Video Priors",
                ],
            },
            "automate_build_code": {
                "h1": [
                    "FSDP2 / Megatron 3D Parallel",
                    "Custom Triton & FlashAttention-3",
                    "DeepSeek MLA & Aux-Free MoE",
                ],
                "normal": [
                    "Mech Interp & SAE Circuits",
                    "FP8 / MXFP8 Mixed Train",
                    "Exec-Guided Code RLVR",
                    "Zero-Day Cyber Fuzzing RL",
                    "ThunderKittens / CUTLASS",
                    "torch.compile & Inductor",
                    "InfiniBand & NCCL Tuning",
                    "OpenRLHF / VeRL Clusters",
                ],
                "small": [
                    "ASL / CBRN Frontier Evals",
                    "Autonomous Replication Eval",
                    "Chinchilla / MuP Scaling",
                    "DualPipe Compute Overlap",
                    "Multi-Token Predict (MTP)",
                    "WSD Warmup-Stable-Decay",
                    "Ring-Attention 1M+ Context",
                    "FlexAttention & Pallas",
                    "NVSHMEM All-to-All MoE",
                    "Micro-Scaling NVFP4",
                    "Zero-Bubble Pipe Parallel",
                    "Differential Privacy SGD",
                ],
            },
            "obsolete": {
                "h1": [
                    "4-Model PPO RLHF Pipeline",
                    "Dense-Only 500B+ Pretrain",
                    "Unverifiable Code/Math RMs",
                ],
                "normal": [
                    "Scaling w/o Safety Evals",
                    "nn.DataParallel / DDP",
                    "Static Sinusoidal Pos",
                    "FP32 Unfused Attention",
                    "GANs for Image / Video",
                    "Dropless MoE Aux-Loss",
                    "Human-Only RL Oversight",
                    "Contaminated Benchmarks",
                    "Unmonitored Latent CoT",
                    "Length-Biased RMs",
                ],
                "small": [],
            },
        },
    },
]


def render_dense_self_diagnosis_chart():
    plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]

    # Compact 18.8-inch width x 22-inch height @ 300 DPI
    fig = plt.figure(figsize=(18.8, 22), dpi=300, facecolor="#0F172A")
    ax = fig.add_axes([0.002, 0.002, 0.996, 0.996])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Background canvas (cool slate-gray so white cards and explicit gutters pop)
    bg_canvas = FancyBboxPatch(
        (0.002, 0.002), 0.996, 0.996,
        boxstyle="round,pad=0.0,rounding_size=0.005",
        facecolor="#E2E8F0", edgecolor="#0F172A", linewidth=1.2
    )
    ax.add_patch(bg_canvas)

    # -------------------------------------------------------------------------
    # 1. Top Header Banner:
    #    - Left: 1-Line Giant Title ("WHAT IS YOUR AI USAGE LEVEL?")
    #    - Middle (to the right of title): 2-Line Hook + 3-Line Blue Key
    #    - Far Right: Website -> Valid -> Last Updated (smaller font)
    # -------------------------------------------------------------------------
    hdr_y = 0.938
    hdr_h = 0.057
    hdr_box = FancyBboxPatch(
        (0.005, hdr_y), 0.990, hdr_h,
        boxstyle="round,pad=0.0,rounding_size=0.005",
        facecolor="#0F172A", edgecolor="#1E293B", linewidth=1.6
    )
    ax.add_patch(hdr_box)

    # Zone 1 (Left): Giant 1-Line Title + Website Underneath
    ax.text(
        0.013, hdr_y + hdr_h * 0.64,
        "AI SKILL TREE 2026",
        fontsize=29.5, fontweight="bold", color="#FFFFFF", va="center", ha="left"
    )
    ax.text(
        0.014, hdr_y + hdr_h * 0.19,
        "www.arianprabowo.com",
        fontsize=11.8, fontweight="bold", color="#38BDF8", va="center", ha="left"
    )

    # Divider 1 (between Title/Website and Yellow/Blue Deck)
    ax.plot(
        [0.292, 0.292], [hdr_y + 0.007, hdr_y + hdr_h - 0.007],
        color="#334155", linewidth=2.0
    )

    # Zone 2 (Center-Left): Pure Yellow Motivating Hook (Larger Font to Fill Space)
    ax.text(
        0.300, hdr_y + hdr_h * 0.63,
        "Want to get better at AI, but don't know what you don't know?\n"
        "From daily chat (L1) to autonomous coding agents (L3–L4)\n"
        "and IMO-math / cyber-RL (L6), here is the full progression map.",
        fontsize=11.15, fontweight="bold", color="#FEF08A", va="center", ha="left",
        linespacing=1.15
    )

    # Divider 2 (between Yellow Hook and Blue 3-Step Key)
    ax.plot(
        [0.644, 0.644], [hdr_y + hdr_h * 0.27, hdr_y + hdr_h - 0.007],
        color="#334155", linewidth=2.0
    )

    # Zone 3 (Right): 3-Step How-To Key (Larger Font to Fill Space)
    ax.text(
        0.653, hdr_y + hdr_h * 0.63,
        "① DIAGNOSE: Scan down each column (L1 → L6) to find where you stop\n"
        "② LEVEL UP: Target the Top 3 pills in the row below\n"
        "③ UNLEARN: Avoid the OBSOLETE traps on the right",
        fontsize=10.65, fontweight="bold", color="#93C5FD", va="center", ha="left",
        linespacing=1.17
    )

    # Combined Footnote Strip (Definition + Fast-Changing Evolution Note + Updated Timestamp)
    ax.text(
        0.300, hdr_y + hdr_h * 0.13,
        f"*Scope: Modern LLMs, Multimodal (mmLLM) & Agentic AI across end-users, MLE & model research (not GOFAI or classic ML/DL). "
        f"Changes fast — see the AI Ladder Evolution mega-chart by Arian Prabowo · {LAST_UPDATED_STR}",
        fontsize=5.80, fontweight="bold", color="#94A3B8", va="center", ha="left"
    )

    # -------------------------------------------------------------------------
    # 2. Column Width Allocation with Explicit Non-Overlapping Gutters (pad=0.0)
    # -------------------------------------------------------------------------
    col_hdr_y = 0.8905
    col_hdr_h = 0.0430

    left_x0 = 0.0050
    left_w = 0.1360

    active_x0 = left_x0 + left_w + 0.0045
    active_col_w = 0.2155
    col_gap = 0.0040

    c1_x = active_x0
    c2_x = c1_x + active_col_w + col_gap
    c3_x = c2_x + active_col_w + col_gap

    sep_x = c3_x + active_col_w + 0.0045
    obs_x0 = sep_x + 0.0045
    obs_w = 0.9950 - obs_x0

    col_geoms = [
        (c1_x, active_col_w),
        (c2_x, active_col_w),
        (c3_x, active_col_w),
        (obs_x0, obs_w),
    ]

    # Vertical dashed divider separating the 3 active Skill-Tree columns from Obsolete
    ax.plot(
        [sep_x, sep_x], [0.005, col_hdr_y + col_hdr_h],
        color="#DC2626", linewidth=1.6, linestyle=(0, (5, 3)), alpha=0.70
    )

    # Left Column Header ("AI LEVEL")
    lhdr = FancyBboxPatch(
        (left_x0, col_hdr_y), left_w, col_hdr_h,
        boxstyle="round,pad=0.0,rounding_size=0.004",
        facecolor="#0F172A", edgecolor="#334155", linewidth=1.5
    )
    ax.add_patch(lhdr)
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.64,
        "AI LEVEL",
        fontsize=18.0, fontweight="bold", color="#FFFFFF", va="center", ha="center"
    )
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.22,
        "Overview · Persona · Surface · Use Case",
        fontsize=7.0, fontweight="bold", color="#94A3B8", va="center", ha="center"
    )

    # 4 Category Column Headers
    for c_idx, cat in enumerate(CATEGORIES):
        cx, cw = col_geoms[c_idx]
        is_obs = cat["key"] == "obsolete"
        chdr = FancyBboxPatch(
            (cx, col_hdr_y), cw, col_hdr_h,
            boxstyle="round,pad=0.0,rounding_size=0.004",
            facecolor=cat["hdr_bg"], edgecolor="#0F172A", linewidth=1.3
        )
        ax.add_patch(chdr)
        ax.text(
            cx + cw / 2, col_hdr_y + col_hdr_h * 0.64,
            cat["title"],
            fontsize=14.2 if len(cat["title"]) >= 25 else (15.0 if is_obs else 15.8),
            fontweight="bold", color="#FFFFFF", va="center", ha="center"
        )
        ax.text(
            cx + cw / 2, col_hdr_y + col_hdr_h * 0.22,
            cat["sub"],
            fontsize=6.8 if is_obs else 7.1,
            fontweight="bold", color="#FEE2E2" if is_obs else "#E2E8F0", va="center", ha="center"
        )

    # -------------------------------------------------------------------------
    # 3. 6 Level Rows x 4 Category Columns (Explicit Row Gaps & Pill Gaps)
    # -------------------------------------------------------------------------
    top_y = 0.8860
    bot_y = 0.0050
    n_levels = len(LEVEL_ROWS)
    row_gap = 0.0042
    row_h = (top_y - bot_y - (n_levels - 1) * row_gap) / n_levels

    for r_idx, lv in enumerate(LEVEL_ROWS):
        y0 = top_y - (r_idx + 1) * row_h - r_idx * row_gap

        # ---------------------------------------------------------------------
        # 1st Column (Sleek Dark-Slate Card with Inset Top Banner):
        # ---------------------------------------------------------------------
        lbox_body = FancyBboxPatch(
            (left_x0, y0), left_w, row_h,
            boxstyle="round,pad=0.0,rounding_size=0.004",
            facecolor="#0F172A", edgecolor="#334155", linewidth=1.5
        )
        ax.add_patch(lbox_body)

        inset_b = 0.0018
        banner_h = row_h * 0.285
        lbox_top = FancyBboxPatch(
            (left_x0 + inset_b, y0 + row_h - banner_h - inset_b),
            left_w - 2 * inset_b, banner_h,
            boxstyle="round,pad=0.0,rounding_size=0.003",
            facecolor="#1E293B", edgecolor=lv["accent"], linewidth=1.4
        )
        ax.add_patch(lbox_top)

        # Level badge on top-left of banner
        ax.text(
            left_x0 + 0.0055, y0 + row_h - inset_b - banner_h * 0.34,
            lv["badge"],
            fontsize=16.8, fontweight="bold", color="#FFFFFF", va="center", ha="left"
        )

        # Crisp 6-segment vector progress bar on top-right of banner
        bar_total_w = 0.050
        bar_gap = 0.0014
        seg_w = (bar_total_w - 5 * bar_gap) / 6.0
        seg_h = banner_h * 0.23
        bar_x_start = left_x0 + left_w - 0.0055 - bar_total_w
        bar_y = y0 + row_h - inset_b - banner_h * 0.34 - seg_h / 2.0
        for b_i in range(6):
            bx_i = bar_x_start + b_i * (seg_w + bar_gap)
            is_lit = b_i < lv["level"]
            seg_patch = FancyBboxPatch(
                (bx_i, bar_y), seg_w, seg_h,
                boxstyle="round,pad=0.0,rounding_size=0.001",
                facecolor=lv["accent"] if is_lit else "#334155",
                edgecolor=lv["accent"] if is_lit else "#475569",
                linewidth=0.6
            )
            ax.add_patch(seg_patch)

        ax.text(
            left_x0 + left_w / 2, y0 + row_h - inset_b - banner_h * 0.77,
            lv["name"],
            fontsize=10.6 if len(lv["name"]) >= 19 else 11.6,
            fontweight="bold", color="#FEF08A", va="center", ha="center"
        )

        # Explanation 1st (before the bullet list!), tightly wrapped
        desc_wrapped = textwrap.fill(lv["desc"], width=33)
        p_wrapped = textwrap.fill(f"• Persona: {lv['persona']}", width=33)
        s_wrapped = textwrap.fill(f"• Surface: {lv['surface']}", width=33)
        u_wrapped = textwrap.fill(f"• Use Case: {lv['use_cases']}", width=33)

        body_top_y = y0 + (row_h - banner_h - inset_b) * 0.94
        ax.text(
            left_x0 + 0.0035,
            body_top_y,
            desc_wrapped,
            fontsize=8.00,
            fontweight="bold",
            color="#F8FAFC",
            va="top",
            ha="left",
            linespacing=1.10,
        )

        bullet_body = f"{p_wrapped}\n{s_wrapped}\n{u_wrapped}"
        ax.text(
            left_x0 + 0.0035,
            body_top_y - 0.030,
            bullet_body,
            fontsize=7.75,
            fontweight="bold",
            color="#CBD5E1",
            va="top",
            ha="left",
            linespacing=1.08,
        )

        # ---------------------------------------------------------------------
        # 4 Category Columns
        # ---------------------------------------------------------------------
        for c_idx, cat in enumerate(CATEGORIES):
            cx, cw = col_geoms[c_idx]
            is_obs = cat["key"] == "obsolete"

            cell_data = lv["cells"][cat["key"]]
            top_h1 = cell_data["h1"]
            mid_norm = cell_data["normal"]
            bot_small = cell_data["small"]

            # Intentional Empty Cell (Level 1 x AUTOMATE & BUILD)
            if not top_h1 and not mid_norm and not bot_small:
                empty_box = FancyBboxPatch(
                    (cx, y0), cw, row_h,
                    boxstyle="round,pad=0.0,rounding_size=0.004",
                    facecolor="#CBD5E1",
                    edgecolor="#64748B",
                    linewidth=1.4,
                    linestyle="--"
                )
                ax.add_patch(empty_box)

                badge_w = cw * 0.88
                badge_h = row_h * 0.42
                bx = cx + (cw - badge_w) / 2
                by = y0 + (row_h - badge_h) / 2
                na_pill = FancyBboxPatch(
                    (bx, by), badge_w, badge_h,
                    boxstyle="round,pad=0.0,rounding_size=0.004",
                    facecolor="#F8FAFC",
                    edgecolor="#94A3B8",
                    linewidth=1.2
                )
                ax.add_patch(na_pill)
                ax.text(
                    cx + cw / 2, y0 + row_h * 0.56,
                    "— NO AUTOMATION / CODING AT LEVEL 1 —",
                    fontsize=10.8, fontweight="bold", color="#475569",
                    va="center", ha="center"
                )
                ax.text(
                    cx + cw / 2, y0 + row_h * 0.43,
                    "Everyday consumers use pre-built apps only.\nNo-code workflows & canvases start at Level 2 ↓",
                    fontsize=8.0, fontweight="bold", color="#64748B",
                    va="center", ha="center", linespacing=1.2
                )
                continue

            # Outer Cell Card (pad=0.0 so exact coordinates never collide)
            cbox = FancyBboxPatch(
                (cx, y0), cw, row_h,
                boxstyle="round,pad=0.0,rounding_size=0.004",
                facecolor=cat["cell_bg"],
                edgecolor=cat["cell_edge"],
                linewidth=1.5 if not is_obs else 1.6,
                linestyle="--" if is_obs else "-"
            )
            ax.add_patch(cbox)

            pad_x = 0.0028
            pad_top = 0.0026
            pad_bot = 0.0024
            inner_w = cw - 2 * pad_x
            x_left = cx + pad_x

            # =================================================================
            # CASE A: Obsolete Column (Top 3 H1 Pills + 5x2 Table Below)
            # =================================================================
            if is_obs:
                gap_t1_t2 = 0.0020
                gap_t2_t3 = 0.0016
                avail_h = row_h - pad_top - pad_bot - gap_t1_t2 - gap_t2_t3
                t1_h = avail_h * 0.390
                t2_h = avail_h * 0.610 + gap_t2_t3

                # --- TIER 1: Top 3 in 1 Column (H1 Pills with explicit pill_gap, pad=0.0) ---
                t1_top_y = y0 + row_h - pad_top
                pill_gap = 0.0018
                ph = (t1_h - 2 * pill_gap) / 3.0
                for idx_1, kw in enumerate(top_h1[:3]):
                    px = x_left
                    pw = inner_w
                    py = t1_top_y - (idx_1 + 1) * ph - idx_1 * pill_gap
                    pill = FancyBboxPatch(
                        (px, py), pw, ph,
                        boxstyle="round,pad=0.0,rounding_size=0.0025",
                        facecolor=cat["h1_bg"],
                        edgecolor=cat["pill_edge"],
                        linewidth=1.1,
                        linestyle="--"
                    )
                    ax.add_patch(pill)
                    ax.text(
                        px + pw / 2, py + ph / 2,
                        kw,
                        fontsize=12.0,
                        fontweight="bold",
                        color=cat["h1_txt"],
                        va="center", ha="center"
                    )

                # --- TIER 2: 5 Rows x 2 Columns Table (Left-Aligned, NO DOT) ---
                t2_top_y = t1_top_y - t1_h - gap_t1_t2
                t2_row_h = t2_h / 5.0
                t2_col_w = inner_w / 2.0

                ax.plot(
                    [x_left + t2_col_w, x_left + t2_col_w],
                    [y0 + pad_bot + 0.0006, t2_top_y - 0.0004],
                    color="#FCA5A5", linewidth=0.85
                )

                for r_div in range(1, 5):
                    hy = t2_top_y - r_div * t2_row_h
                    ax.plot(
                        [x_left + 0.0004, x_left + inner_w - 0.0004],
                        [hy, hy],
                        color="#FECACA", linewidth=0.55
                    )

                for idx_2, kw in enumerate(mid_norm[:10]):
                    sr = idx_2 // 2
                    sc = idx_2 % 2
                    if sc == 0 and sr % 2 == 1:
                        stripe = FancyBboxPatch(
                            (x_left, t2_top_y - (sr + 1) * t2_row_h + 0.00015),
                            inner_w, t2_row_h - 0.0003,
                            boxstyle="round,pad=0.0,rounding_size=0.001",
                            facecolor="#FEE2E2", edgecolor="none", alpha=0.60
                        )
                        ax.add_patch(stripe)
                    tx = x_left + sc * t2_col_w + 0.0016
                    ty = t2_top_y - (sr + 0.5) * t2_row_h
                    ax.text(
                        tx, ty,
                        kw,
                        fontsize=6.65,
                        fontweight="bold",
                        color=cat["t2_txt"],
                        va="center", ha="left"
                    )
                continue

            # =================================================================
            # CASE C: Full 3-Tier Active Skill-Tree Cell (pad=0.0, explicit pill_gap)
            # =================================================================
            gap_t1_t2 = 0.0020
            gap_t2_t3 = 0.0016
            avail_h = row_h - pad_top - pad_bot - gap_t1_t2 - gap_t2_t3
            t1_h = avail_h * 0.390
            t2_h = avail_h * 0.365
            t3_h = avail_h * 0.245

            # --- TIER 1: Top 3 in 1 Column (H1 Pills with explicit pill_gap, pad=0.0) ---
            t1_top_y = y0 + row_h - pad_top
            pill_gap = 0.0018
            ph = (t1_h - 2 * pill_gap) / 3.0
            for idx_1, kw in enumerate(top_h1[:3]):
                if not kw:
                    continue
                px = x_left
                pw = inner_w
                py = t1_top_y - (idx_1 + 1) * ph - idx_1 * pill_gap

                pill = FancyBboxPatch(
                    (px, py), pw, ph,
                    boxstyle="round,pad=0.0,rounding_size=0.0025",
                    facecolor=cat["h1_bg"],
                    edgecolor=cat["pill_edge"],
                    linewidth=1.15
                )
                ax.add_patch(pill)

                ax.text(
                    px + pw / 2, py + ph / 2,
                    kw,
                    fontsize=13.2,
                    fontweight="bold",
                    color=cat["h1_txt"],
                    va="center", ha="center"
                )

            # --- TIER 2: Next 8 in 2 Columns x 4 Rows (Borderless, Left-Aligned, NO DOT) ---
            t2_top_y = t1_top_y - t1_h - gap_t1_t2
            t2_row_h = t2_h / 4.0
            t2_col_w = inner_w / 2.0

            ax.plot(
                [x_left + t2_col_w, x_left + t2_col_w],
                [t2_top_y - t2_h + 0.0006, t2_top_y - 0.0006],
                color="#CBD5E1", linewidth=0.8
            )

            for idx_2, kw in enumerate(mid_norm[:8]):
                if not kw:
                    continue
                sr = idx_2 // 2
                sc = idx_2 % 2
                if sc == 0 and sr % 2 == 1:
                    stripe = FancyBboxPatch(
                        (x_left, t2_top_y - (sr + 1) * t2_row_h + 0.00015),
                        inner_w, t2_row_h - 0.0003,
                        boxstyle="round,pad=0.0,rounding_size=0.001",
                        facecolor=cat["t2_bg"], edgecolor="none"
                    )
                    ax.add_patch(stripe)

                tx = x_left + sc * t2_col_w + 0.0016
                ty = t2_top_y - (sr + 0.5) * t2_row_h
                ax.text(
                    tx, ty,
                    kw,
                    fontsize=7.35,
                    fontweight="bold",
                    color=cat["t2_txt"],
                    va="center", ha="left"
                )

            # --- TIER 3: Bottom 12 in 3 Columns x 4 Rows (Borderless Footnote Band, Left-Aligned, NO DOT) ---
            t3_top_y = t2_top_y - t2_h - gap_t2_t3
            t3_row_h = t3_h / 4.0
            t3_col_w = inner_w / 3.0

            t3_band = FancyBboxPatch(
                (x_left, y0 + pad_bot),
                inner_w, t3_h,
                boxstyle="round,pad=0.0,rounding_size=0.002",
                facecolor=cat["t3_bg"],
                edgecolor="#CBD5E1",
                linewidth=0.6
            )
            ax.add_patch(t3_band)

            for c_div in (1, 2):
                ax.plot(
                    [x_left + c_div * t3_col_w, x_left + c_div * t3_col_w],
                    [y0 + pad_bot + 0.0006, t3_top_y - 0.0006],
                    color="#CBD5E1", linewidth=0.55
                )

            for idx_3, kw in enumerate(bot_small[:12]):
                if not kw:
                    continue
                sr = idx_3 // 3
                sc = idx_3 % 3
                tx = x_left + sc * t3_col_w + 0.0012
                ty = t3_top_y - (sr + 0.5) * t3_row_h

                ax.text(
                    tx, ty,
                    kw,
                    fontsize=4.90,
                    fontweight="bold",
                    color=cat["t3_txt"],
                    va="center", ha="left"
                )

    fig.savefig(OUT_PNG, dpi=300, facecolor=fig.get_facecolor())
    fig.savefig(OUT_TOP_PNG, dpi=300, facecolor=fig.get_facecolor())
    fig.savefig(OUT_TOP_PDF, format="pdf", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved: {OUT_PNG} ({OUT_PNG.stat().st_size:,} bytes)")
    print(f"Saved: {OUT_TOP_PNG} ({OUT_TOP_PNG.stat().st_size:,} bytes)")
    print(f"Saved: {OUT_TOP_PDF} ({OUT_TOP_PDF.stat().st_size:,} bytes)")


def render_mini_self_diagnosis_mobile_chart():
    """
    Smartphone Portrait Mini Self-Diagnosis Chart (9.5 x 18.0 in @ 300 DPI, ~9:17 portrait).
    Allows multiline wrapping across masthead, column headers, Top-3 H1 pills, and core items
    so every text element is large and readable on a phone screen without pinching to zoom.
    """
    plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]

    fig = plt.figure(figsize=(9.5, 18.0), dpi=300, facecolor="#0F172A")
    ax = fig.add_axes([0.003, 0.002, 0.994, 0.996])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    bg_canvas = FancyBboxPatch(
        (0.001, 0.0005), 0.998, 0.999,
        boxstyle="round,pad=0.0,rounding_size=0.005",
        facecolor="#E2E8F0", edgecolor="#0F172A", linewidth=1.2
    )
    ax.add_patch(bg_canvas)

    # -------------------------------------------------------------------------
    # 1. Portrait Top Masthead (Title + Metadata Badge + Full-Width Hook + 3-Step Key)
    # -------------------------------------------------------------------------
    hdr_y = 0.918
    hdr_h = 0.079
    hdr_box = FancyBboxPatch(
        (0.005, hdr_y), 0.990, hdr_h,
        boxstyle="round,pad=0.0,rounding_size=0.006",
        facecolor="#0F172A", edgecolor="#1E293B", linewidth=1.6
    )
    ax.add_patch(hdr_box)

    # Top Row of Masthead: Giant 1-Line Title (Left) + Website (Right)
    ax.text(
        0.015, hdr_y + hdr_h * 0.79,
        "AI SKILL TREE 2026",
        fontsize=25.0, fontweight="bold", color="#FFFFFF", va="center", ha="left"
    )
    ax.text(
        0.985, hdr_y + hdr_h * 0.79,
        "www.arianprabowo.com",
        fontsize=11.2, fontweight="bold", color="#38BDF8", va="center", ha="right"
    )

    # Horizontal divider separating Top Row (Title + Website) from Middle Row (Yellow | Blue)
    ax.plot(
        [0.014, 0.986], [hdr_y + hdr_h * 0.60, hdr_y + hdr_h * 0.60],
        color="#334155", linewidth=1.2
    )

    # Middle-Left of masthead: Pure Yellow Hook (Larger Font)
    ax.text(
        0.014, hdr_y + hdr_h * 0.38,
        "Want to get better at AI, but don't know what you don't know?\n"
        "From daily chat (L1) to autonomous coding agents (L3–L4) and\n"
        "IMO-math / cyber-RL (L6), here is the full progression map.",
        fontsize=7.25, fontweight="bold", color="#FEF08A", va="center", ha="left",
        linespacing=1.09
    )

    # Vertical divider between Yellow (1st) and Blue (2nd)
    ax.plot(
        [0.508, 0.508], [hdr_y + hdr_h * 0.19, hdr_y + hdr_h * 0.56],
        color="#334155", linewidth=1.2
    )

    # Middle-Right of masthead: Blue 3-Step Key (Larger Font)
    ax.text(
        0.518, hdr_y + hdr_h * 0.38,
        "① DIAGNOSE: Scan down each column (L1 → L6) to find where you stop\n"
        "② LEVEL UP: Target the Top 3 pills in the row below\n"
        "③ UNLEARN: Avoid the OBSOLETE traps on the right",
        fontsize=6.95, fontweight="bold", color="#93C5FD", va="center", ha="left",
        linespacing=1.11
    )

    # Bottom Combined Footnote Strip (Scope + Fast-Changing Mega-Chart + Updated Timestamp)
    ax.text(
        0.500, hdr_y + hdr_h * 0.08,
        f"*Scope: Modern LLMs, mmLLM & Agentic AI (end-user to MLE/research; not GOFAI/classic ML/DL). "
        f"Changes fast — see AI Ladder Evolution mega-chart by Arian Prabowo · {LAST_UPDATED_STR}",
        fontsize=4.25, fontweight="bold", color="#94A3B8", va="center", ha="center"
    )

    # -------------------------------------------------------------------------
    # 2. Portrait Column Headers (Multiline 2-Line Titles, Explicit Gaps)
    # -------------------------------------------------------------------------
    col_hdr_y = 0.871
    col_hdr_h = 0.044

    left_x0 = 0.005
    left_w = 0.165

    col_gap = 0.0045
    active_x0 = left_x0 + left_w + col_gap
    active_col_w = 0.207
    sep_x = active_x0 + 3 * active_col_w + 2 * col_gap + 0.0045
    obs_x0 = sep_x + 0.0045
    obs_w = 0.995 - obs_x0

    col_geoms = [
        (active_x0 + 0 * (active_col_w + col_gap), active_col_w),
        (active_x0 + 1 * (active_col_w + col_gap), active_col_w),
        (active_x0 + 2 * (active_col_w + col_gap), active_col_w),
        (obs_x0, obs_w),
    ]

    ax.plot(
        [sep_x, sep_x], [0.004, col_hdr_y + col_hdr_h],
        color="#DC2626", linewidth=1.5, linestyle=(0, (5, 3)), alpha=0.65
    )

    lhdr = FancyBboxPatch(
        (left_x0, col_hdr_y), left_w, col_hdr_h,
        boxstyle="round,pad=0.0,rounding_size=0.005",
        facecolor="#0F172A", edgecolor="#334155", linewidth=1.4
    )
    ax.add_patch(lhdr)
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.65,
        "AI LEVEL",
        fontsize=12.4, fontweight="bold", color="#FFFFFF", va="center", ha="center"
    )
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.23,
        "Overview & Persona",
        fontsize=6.2, fontweight="bold", color="#94A3B8", va="center", ha="center"
    )

    mobile_cat_titles = {
        "think_search_analyze": ("THINK, SEARCH\n& ANALYZE", "Research · Docs · RAG · Align"),
        "create_design_media": ("CREATE & DESIGN\n(MEDIA)", "Image · Video · Voice · 3D"),
        "automate_build_code": ("AUTOMATE &\nBUILD (CODE)", "Workflows · Agents · Evals"),
        "obsolete": ("OBSOLETE\n(TRAPS)", "Still Doing This? Stop"),
    }

    for c_idx, cat in enumerate(CATEGORIES):
        cx, cw = col_geoms[c_idx]
        is_obs = cat["key"] == "obsolete"
        m_title, m_sub = mobile_cat_titles[cat["key"]]
        chdr = FancyBboxPatch(
            (cx, col_hdr_y), cw, col_hdr_h,
            boxstyle="round,pad=0.0,rounding_size=0.005",
            facecolor=cat["hdr_bg"], edgecolor="#0F172A", linewidth=1.2
        )
        ax.add_patch(chdr)
        ax.text(
            cx + cw / 2, col_hdr_y + col_hdr_h * 0.64,
            m_title,
            fontsize=9.3 if not is_obs else 9.1,
            fontweight="bold", color="#FFFFFF", va="center", ha="center",
            linespacing=0.98
        )
        ax.text(
            cx + cw / 2, col_hdr_y + col_hdr_h * 0.16,
            m_sub,
            fontsize=5.5,
            fontweight="bold", color="#FEE2E2" if is_obs else "#E2E8F0", va="center", ha="center"
        )

    # -------------------------------------------------------------------------
    # 3. 6 Level Rows x 4 Columns (Multiline Mini Self-Diagnosis, Explicit Gaps)
    # -------------------------------------------------------------------------
    top_y = 0.866
    bot_y = 0.004
    n_levels = len(LEVEL_ROWS)
    row_gap = 0.0042
    row_h = (top_y - bot_y - (n_levels - 1) * row_gap) / n_levels

    mobile_level_names = {
        1: "EVERYDAY\nCONSUMER",
        2: "WORKSPACE\nPOWER USER",
        3: "VIBE CODER\n& BUILDER",
        4: "AI & AGENT\nENGINEER",
        5: "LOCAL &\nPOST-TRAINING",
        6: "FRONTIER\nRESEARCHER",
    }

    for r_idx, lv in enumerate(LEVEL_ROWS):
        y0 = top_y - (r_idx + 1) * row_h - r_idx * row_gap

        # Left Column: AI LEVEL (Multiline Banner + Explanation First + Bullets)
        lbox_body = FancyBboxPatch(
            (left_x0, y0), left_w, row_h,
            boxstyle="round,pad=0.0,rounding_size=0.005",
            facecolor="#0F172A", edgecolor="#334155", linewidth=1.5
        )
        ax.add_patch(lbox_body)

        inset_b = 0.0020
        banner_h = row_h * 0.340
        lbox_top = FancyBboxPatch(
            (left_x0 + inset_b, y0 + row_h - banner_h - inset_b),
            left_w - 2 * inset_b, banner_h,
            boxstyle="round,pad=0.0,rounding_size=0.004",
            facecolor="#1E293B", edgecolor=lv["accent"], linewidth=1.4
        )
        ax.add_patch(lbox_top)

        b_top_y = y0 + row_h - inset_b
        ax.text(
            left_x0 + 0.006, b_top_y - banner_h * 0.22,
            lv["badge"],
            fontsize=12.0, fontweight="bold", color="#FFFFFF", va="center", ha="left"
        )

        # 6-segment vector progress bar
        bar_total_w = 0.062
        bar_gap = 0.0018
        seg_w = (bar_total_w - 5 * bar_gap) / 6.0
        seg_h = banner_h * 0.15
        bar_x_start = left_x0 + left_w - 0.006 - bar_total_w
        bar_y = b_top_y - banner_h * 0.22 - seg_h / 2.0
        for b_i in range(6):
            bx_i = bar_x_start + b_i * (seg_w + bar_gap)
            is_lit = b_i < lv["level"]
            seg_patch = FancyBboxPatch(
                (bx_i, bar_y), seg_w, seg_h,
                boxstyle="round,pad=0.0,rounding_size=0.001",
                facecolor=lv["accent"] if is_lit else "#334155",
                edgecolor=lv["accent"] if is_lit else "#475569",
                linewidth=0.5
            )
            ax.add_patch(seg_patch)

        ax.text(
            left_x0 + left_w / 2, b_top_y - banner_h * 0.72,
            mobile_level_names[lv["level"]],
            fontsize=8.3,
            fontweight="bold", color="#FEF08A", va="center", ha="center",
            linespacing=0.96
        )

        desc_wrapped = textwrap.fill(lv["desc"], width=24)
        p_wrapped = textwrap.fill(f"• Persona: {lv['persona']}", width=24)
        s_wrapped = textwrap.fill(f"• Surface: {lv['surface']}", width=24)

        body_top_y = y0 + (row_h - banner_h - inset_b) * 0.95
        ax.text(
            left_x0 + 0.005,
            body_top_y,
            desc_wrapped,
            fontsize=5.95,
            fontweight="bold",
            color="#F8FAFC",
            va="top",
            ha="left",
            linespacing=1.05,
        )

        n_desc_lines = desc_wrapped.count("\n") + 1
        bullet_body = f"{p_wrapped}\n{s_wrapped}"
        ax.text(
            left_x0 + 0.005,
            body_top_y - n_desc_lines * 0.0066 - 0.0018,
            bullet_body,
            fontsize=5.55,
            fontweight="bold",
            color="#CBD5E1",
            va="top",
            ha="left",
            linespacing=1.04,
        )

        # 4 Category Columns (Multiline Top 3 H1 Pills + 4 Multiline Core Items)
        for c_idx, cat in enumerate(CATEGORIES):
            cx, cw = col_geoms[c_idx]
            is_obs = cat["key"] == "obsolete"

            cell_data = lv["cells"][cat["key"]]
            top_h1 = cell_data["h1"]
            mid_norm = cell_data["normal"]
            bot_small = cell_data["small"]

            # Intentional Empty Cell (Level 1 x AUTOMATE & BUILD)
            if not top_h1 and not mid_norm and not bot_small:
                empty_box = FancyBboxPatch(
                    (cx, y0), cw, row_h,
                    boxstyle="round,pad=0.0,rounding_size=0.005",
                    facecolor="#CBD5E1",
                    edgecolor="#64748B",
                    linewidth=1.3,
                    linestyle="--"
                )
                ax.add_patch(empty_box)

                badge_w = cw * 0.88
                badge_h = row_h * 0.48
                bx = cx + (cw - badge_w) / 2
                by = y0 + (row_h - badge_h) / 2
                na_pill = FancyBboxPatch(
                    (bx, by), badge_w, badge_h,
                    boxstyle="round,pad=0.0,rounding_size=0.004",
                    facecolor="#F8FAFC",
                    edgecolor="#94A3B8",
                    linewidth=1.1
                )
                ax.add_patch(na_pill)
                ax.text(
                    cx + cw / 2, y0 + row_h * 0.58,
                    "— NO AUTOMATION /\nCODING AT LEVEL 1 —",
                    fontsize=8.0, fontweight="bold", color="#334155",
                    va="center", ha="center", linespacing=1.08
                )
                ax.text(
                    cx + cw / 2, y0 + row_h * 0.39,
                    "Everyday consumers use\npre-built apps only.\nStarts at Level 2 ↓",
                    fontsize=6.3, fontweight="bold", color="#475569",
                    va="center", ha="center", linespacing=1.12
                )
                continue

            cbox = FancyBboxPatch(
                (cx, y0), cw, row_h,
                boxstyle="round,pad=0.0,rounding_size=0.005",
                facecolor=cat["cell_bg"],
                edgecolor=cat["cell_edge"],
                linewidth=1.4 if not is_obs else 1.5,
                linestyle="--" if is_obs else "-"
            )
            ax.add_patch(cbox)

            pad_x = 0.0032
            pad_top = 0.0028
            pad_bot = 0.0024
            inner_w = cw - 2 * pad_x
            x_left = cx + pad_x

            gap_t1_t2 = 0.0020
            avail_h = row_h - pad_top - pad_bot - gap_t1_t2
            t1_h = avail_h * 0.54
            t2_h = avail_h * 0.46

            # --- TIER 1: Top 3 Multiline H1 Pills (Explicit Gaps Between Pills) ---
            t1_top_y = y0 + row_h - pad_top
            pill_gap = 0.0020
            ph = (t1_h - 2 * pill_gap) / 3.0
            wrap_w_h1 = 19 if is_obs else 21
            for idx_1, kw in enumerate(top_h1[:3]):
                px = x_left
                pw = inner_w
                py = t1_top_y - (idx_1 + 1) * ph - idx_1 * pill_gap
                pill = FancyBboxPatch(
                    (px, py), pw, ph,
                    boxstyle="round,pad=0.0,rounding_size=0.003",
                    facecolor=cat["h1_bg"],
                    edgecolor=cat["pill_edge"],
                    linewidth=1.1,
                    linestyle="--" if is_obs else "-"
                )
                ax.add_patch(pill)

                kw_multiline = textwrap.fill(kw, width=wrap_w_h1)
                ax.text(
                    px + pw / 2, py + ph / 2,
                    kw_multiline,
                    fontsize=8.1 if is_obs else 8.45,
                    fontweight="bold",
                    color=cat["h1_txt"],
                    va="center", ha="center",
                    linespacing=1.01
                )

            # Horizontal divider between Top 3 Pills and Core List
            div_y = t1_top_y - t1_h - gap_t1_t2 * 0.5
            ax.plot(
                [x_left + 0.001, x_left + inner_w - 0.001],
                [div_y, div_y],
                color="#FCA5A5" if is_obs else cat["div_col"],
                linewidth=0.9,
                linestyle="--" if is_obs else "-"
            )

            # --- TIER 2: 4 Core Checkpoints (Left-Aligned, No Dots, Multiline Allowed) ---
            t2_top_y = t1_top_y - t1_h - gap_t1_t2
            t2_row_h = t2_h / 4.0
            wrap_w_t2 = 25 if is_obs else 27

            for idx_2, kw in enumerate(mid_norm[:4]):
                if idx_2 % 2 == 1:
                    stripe = FancyBboxPatch(
                        (x_left + 0.0003, t2_top_y - (idx_2 + 1) * t2_row_h + 0.00015),
                        inner_w - 0.0006, t2_row_h - 0.0003,
                        boxstyle="round,pad=0.0,rounding_size=0.001",
                        facecolor="#FEE2E2" if is_obs else cat["t2_bg"],
                        edgecolor="none",
                        alpha=0.60 if is_obs else 1.0
                    )
                    ax.add_patch(stripe)

                ty = t2_top_y - (idx_2 + 0.5) * t2_row_h
                kw_t2_multiline = textwrap.fill(kw, width=wrap_w_t2)
                ax.text(
                    x_left + 0.0022, ty,
                    kw_t2_multiline,
                    fontsize=6.45 if is_obs else 6.70,
                    fontweight="bold",
                    color=cat["t2_txt"],
                    va="center", ha="left",
                    linespacing=0.98
                )

    fig.savefig(OUT_MOBILE_PNG, dpi=300, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved: {OUT_MOBILE_PNG} ({OUT_MOBILE_PNG.stat().st_size:,} bytes)")


def write_standalone_markdown_report():
    lines = [
        f"![AI Skill Tree 2026 — Full Desktop Self-Diagnosis (Jan 2025 – Nov 2026)]({OUT_PNG})",
        "",
        f"![AI Skill Tree 2026 — Mobile Portrait Mini Self-Diagnosis (Jan 2025 – Nov 2026)]({OUT_MOBILE_PNG})",
        "",
        "# AI SKILL TREE 2026",
        "",
        "> **Want to get better at AI, but don't know what you don't know? From daily chat (`L1`) to autonomous coding agents (`L3–L4`) and IMO-math / cyber-RL (`L6`), here is the full progression map.**  ",
        f"> **How to Use ([www.arianprabowo.com](https://www.arianprabowo.com) · `Valid: Jan 2025 – Nov 2026` · <sub>`{LAST_UPDATED_STR}`</sub>):** **`① DIAGNOSE:`** Scan down each column (`L1 → L6`) to find where you stop · **`② LEVEL UP:`** Target the **Top 3** pills in the row below · **`③ UNLEARN:`** Avoid the **`OBSOLETE`** traps on the right.  ",
        "> <sub>*\\*Scope: Modern LLMs, Multimodal (`mmLLM`) & Agentic AI across end-users, MLE & foundation-model research — excludes GOFAI and classic tabular ML/DL. Because AI changes rapidly, this snapshot is only valid for `Jan 2025 – Nov 2026`; to see how the ladder evolves across generations, check the **AI Ladder Evolution** mega-chart by Arian Prabowo.*</sub>",
        "",
        "---",
        "",
        "## 1. Standalone AI Skill Tree (`Levels 1–6` × `4` Columns)",
        "",
        "*Caption: Current-generation (`Jan 2025 – Nov 2026`) AI skill tree across `6` usage levels (`Rows`) and `4` columns (`Think, Search & Analyze`, `Create & Design (Media)`, `Automate & Build (Code)`, and `Obsolete`), integrating capability, reliability, audit trails, compliance, fairness, and frontier safety/alignment across every tier. Active skill-tree cells organize capabilities into `3` tiers: **Top 3 (`H1` bold)** flagship capability checkpoints, **Middle 8 (`Normal`)** core workflows, and **Bottom 12 (`Footnote` *italics*)** granular techniques. `Level 1 × Automate & Build (Code)` is intentionally empty because everyday consumers use pre-built apps only.*",
        "",
        "| AI Level (Overview · Persona · Surface · Use Case) | Think, Search & Analyze | Create & Design (Media) | Automate & Build (Code) | Obsolete |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]

    for lv in LEVEL_ROWS:
        col0 = (
            f"**{lv['badge']} ({lv['meter']}): {lv['name']}**<br>"
            f"{lv['desc']}<br>"
            f"• **Persona:** {lv['persona']}<br>"
            f"• **Surface:** {lv['surface']}<br>"
            f"• **Use Case:** {lv['use_cases']}"
        )
        row_cells = [col0]
        for cat in CATEGORIES:
            d = lv["cells"][cat["key"]]
            if not d["h1"] and not d["normal"] and not d["small"]:
                row_cells.append("*(No Automation / Coding at Level 1 — starts at Level 2)*")
                continue
            h1_str = " · ".join(f"**{k}**" for k in d["h1"])
            norm_str = " · ".join(d["normal"])
            small_str = " · ".join(f"*{k}*" for k in d["small"])
            parts = [p for p in (h1_str, norm_str, small_str) if p]
            row_cells.append("<br><br>".join(parts))
        lines.append("| " + " | ".join(row_cells) + " |")

    lines.extend([
        "",
        "---",
        "",
        "## 2. Level-by-Level Breakdown (`Level 1` → `Level 6`)",
        "",
    ])

    for lv in LEVEL_ROWS:
        lines.extend([
            f"### {lv['badge']} ({lv['meter']}) — {lv['name']}",
            "",
            f"{lv['desc']}",
            "",
            f"* **Persona:** {lv['persona']}",
            f"* **Surface & Hardware:** {lv['surface']}",
            f"* **Use Case:** {lv['use_cases']}",
            "",
            "| Category | Top 3 Flagship Checkpoints (`H1`) | Core Workflows (`Normal`) | Granular Techniques (`Footnote`) |",
            "| :--- | :--- | :--- | :--- |",
        ])
        for cat in CATEGORIES:
            d = lv["cells"][cat["key"]]
            if not d["h1"] and not d["normal"] and not d["small"]:
                lines.append(f"| **{cat['title']}** | — | — | — |")
                continue
            h1_s = ", ".join(f"**`{k}`**" for k in d["h1"]) if d["h1"] else "—"
            nm_s = ", ".join(f"`{k}`" for k in d["normal"]) if d["normal"] else "—"
            sm_s = ", ".join(f"*{k}*" for k in d["small"]) if d["small"] else "—"
            lines.append(f"| **{cat['title']}** | {h1_s} | {nm_s} | {sm_s} |")
        lines.append("")

    content = "\n".join(lines)
    OUT_MD.write_text(content, encoding="utf-8")
    print(f"Saved: {OUT_MD} ({OUT_MD.stat().st_size:,} bytes)")


if __name__ == "__main__":
    render_dense_self_diagnosis_chart()
    render_mini_self_diagnosis_mobile_chart()
    write_standalone_markdown_report()
