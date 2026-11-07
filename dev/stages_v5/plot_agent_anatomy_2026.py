"""
ANATOMY OF AI AGENTS 2026 — 7-Layer OSI-Inspired Reference Model & Megachart
=============================================================================
Grounded in Haggai Roitman's "The Hitchhiker's Guide to Agentic AI: From Foundations to Systems"
(arXiv:2606.24937, v1.4, June 2026) and the 2026 production AI systems stack.

7 OSI-Inspired Stack Layers (Top-to-Bottom Progression: Layer 1 Physical -> Layer 7 Multi-Agent):
  - LAYER 1 (Physical & Silicon): GPU/TPU/NPU Silicon, HBM3e/SRAM, NVLink/InfiniBand & Power (Ch. 2.1, 11, 30.5)
  - LAYER 2 (OS, Env & Sandbox): Linux/macOS, Homebrew, uv/conda/pip/venv, Python/Rust/TS & MicroVMs (Ch. 21.5, 22)
  - LAYER 3 (Tensor & Serving Engine): CUDA/Triton/MLX, PyTorch/JAX, FlashAttention, vLLM/SGLang & Quantization (Ch. 1.6, 2.2, 11)
  - LAYER 4 (Foundation & Reasoning RL): Transformer/MoE/MLA, SFT/Packing, LoRA/DoRA/PiSSA, DPO/KTO & RLVR/GRPO/DAPO (Ch. 1, 3-10, 12-13)
  - LAYER 5 (Context, RAG, Memory & MCP): Context Eng, Agentic RAG/REFRAG, Episodic/Dream Memory, MCP & SKILL.md (Ch. 16-18, 23-24)
  - LAYER 6 (Single-Agent Harness, Loop & Graph): CLAUDE.md/AGENTS.md, ReAct/Reflexion, Loop Eng, LangGraph & Harness² (Ch. 18-21, 27)
  - LAYER 7 (Multi-Agent Mesh, A2A & Agentic UI): Orchestrator-Worker-Critic (OWC), Google A2A / IBM ACP, Gateways & GenUI (Ch. 25-26, 28)

4 Columns:
  1. CORE PRIMITIVES & ARCHITECTURE (Math · Abstractions · Data Structures · Topologies)
  2. FRAMEWORKS, TOOLING & PROTOCOLS (Packages · Runtimes · SDKs · Open Standards)
  3. SCALING, OPS, EVALS & SECURITY (Optimization · Verification Oracles · Sandboxing · Benchmarks)
  4. FAILURE MODES & ANTI-PATTERNS (Hardware Walls · Env Hell · Reward Hacking · Loop & Swarm Traps)
"""

from datetime import datetime
from pathlib import Path
import textwrap
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

REPO_ROOT = Path("/Users/z3540725/My Drive/personal/2026 10 17 AI_ladder_evol")
DEV_DIR = REPO_ROOT / "dev"
FIG_DIR = DEV_DIR / "figures_v5"
FIG_DIR.mkdir(parents=True, exist_ok=True)

OUT_DEV_PNG = DEV_DIR / "anatomy_of_AI_agents_2026.png"
OUT_DEV_PDF = DEV_DIR / "anatomy_of_AI_agents_2026.pdf"
OUT_FIG_PNG = FIG_DIR / "fig_v5_anatomy_of_ai_agents_2026.png"
OUT_MOBILE_PNG = FIG_DIR / "fig_v5_mini_anatomy_of_ai_agents_mobile.png"
OUT_MD = DEV_DIR / "2026 11 07 anatomy_of_AI_agents_2026.md"

plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["ps.fonttype"] = 42

_now_local = datetime.now().astimezone()
_utc_off = _now_local.strftime("%z")
_utc_off_colon = f"{_utc_off[:3]}:{_utc_off[3:]}" if len(_utc_off) == 5 else _utc_off
LAST_UPDATED_STR = f"Updated: {_now_local.strftime('%Y-%m-%d %H:%M:%S %Z')} (UTC{_utc_off_colon})"


# =============================================================================
# 4 ARCHITECTURAL PILLAR COLUMNS (3 ACTIVE + 1 FAILURE MODES SIDEBAR)
# =============================================================================
COLUMNS = [
    {
        "key": "primitives_arch",
        "title": "CORE PRIMITIVES & ARCHITECTURE",
        "sub": "Hardware Physics · Math · Data Structures · Control Topologies",
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
        "key": "frameworks_stack",
        "title": "FRAMEWORKS, PACKAGES & PROTOCOLS",
        "sub": "CLI Package Managers · DL Frameworks · Serving · Agent SDKs",
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
        "key": "ops_evals_security",
        "title": "SCALING, VERIFICATION & SECURITY",
        "sub": "Parallelism · Sandboxes · Evals & Oracles · Guardrails",
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
        "key": "failure_modes",
        "title": "FAILURE MODES & TRAPS",
        "sub": "What Breaks Here (Anti-Patterns)",
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
# 7 OSI-INSPIRED AGENT STACK LAYERS (LAYER 1 PHYSICAL -> LAYER 7 MULTI-AGENT)
# =============================================================================
STACK_LAYERS = [
    {
        "layer": 1,
        "badge": "LAYER 1",
        "meter": "L1/7",
        "name": "PHYSICAL & SILICON",
        "osi_map": "OSI L1 Physical · PDU: FLOPs, HBM Bytes & Warps",
        "desc": "GPUs/TPUs/NPUs, HBM3e vs. SRAM hierarchy, CUDA/Triton kernels, and NVLink/InfiniBand fabrics.",
        "book_ref": "Ch. 1.6, 2.1, 11.10–14, 30.5 (GPUs & Kernels).",
        "accent": "#10B981",
        "cells": {
            "primitives_arch": {
                "h1": [
                    "GPU / TPU / NPU Tensor Cores",
                    "HBM3e vs. On-Chip SRAM Hierarchy",
                    "FlashAttention IO-Aware SRAM Tiling",
                ],
                "normal": [
                    "Streaming Multiprocessors (SMs)",
                    "Warp Schedulers (32-Thread SIMT)",
                    "Arithmetic Intensity (FLOP/Byte)",
                    "Roofline Compute vs. Memory Bound",
                    "FP16 / BF16 / FP8 / FP4 Formats",
                    "Online Softmax Rescaling (Safe Max)",
                    "Unified Memory Architecture (UMA)",
                    "Wafer-Scale & SRAM-Only LPU Dies",
                ],
                "small": [
                    "Register File (256KB/SM)",
                    "L1 Cache / Shared Memory",
                    "L2 Cache (50MB–128MB)",
                    "HBM3e Bandwidth (3.3–8 TB/s)",
                    "SRAM Bandwidth (~20–30 TB/s)",
                    "Transformer Engine FP8/FP4",
                    "Stochastic Rounding",
                    "Tensor Memory Accelerator (TMA)",
                    "Systolic Array Matrix Multiply",
                    "Memory Coalescing",
                    "Bank Conflict Avoidance",
                    "TDP Power & Liquid Cooling",
                ],
            },
            "frameworks_stack": {
                "h1": [
                    "NVIDIA H100 / H200 / Blackwell B200",
                    "Google TPU v5p / v6e Trillium / v7",
                    "CUDA · OpenAI Triton · Apple Silicon M4",
                ],
                "normal": [
                    "NVIDIA GB200 NVL72 Rack Scale",
                    "AMD Instinct MI300X / MI325X",
                    "AWS Trainium2 & Inferentia2",
                    "Groq LPU & Cerebras WSE-3 ASIC",
                    "NVLink 4/5 (900–1,800 GB/s/GPU)",
                    "InfiniBand NDR/XDR (400–800Gb/s)",
                    "cuBLAS / cuDNN / CUTLASS / FlashInfer",
                    "AMD ROCm / HIP & Apple Metal",
                ],
                "small": [
                    "DGX / HGX 8-GPU Node Topology",
                    "GPUDirect RDMA / Storage",
                    "Mellanox ConnectX-7 / 8 NICs",
                    "80GB / 141GB / 192GB VRAM Tiers",
                    "Mac Mini M4 64GB–512GB Cluster",
                    "RTX 4090 / 5090 Local Workstation",
                    "On-Device NPU (45–80+ TOPS)",
                    "Co-Packaged Silicon Photonics",
                    "Vera Rubin NVL144 (HBM4 Roadmap)",
                    "Liger-Kernel Fused Triton Ops",
                    "ECC Memory Error Correction",
                    "NCCL / Gloo Collective Backend",
                ],
            },
            "ops_evals_security": {
                "h1": [
                    "Model FLOPs Utilization (MFU > 45%)",
                    "Prefill (Compute) vs. Decode (BW)",
                    "Confidential Compute GPU TEEs",
                ],
                "normal": [
                    "Prefill Phase (Matrix-Matrix Gemm)",
                    "Decode Phase (Matrix-Vector Gemv)",
                    "Multi-Instance GPU (MIG) Slices",
                    "Rail-Optimized Fat-Tree Topology",
                    "NVIDIA DCGM Hardware Health Check",
                    "Silent Data Corruption (SDC) Scans",
                    "Nsight Compute & Systems Profiling",
                    "Hardware Root-of-Trust Attestation",
                ],
                "small": [
                    "MFU = Achieved / Peak FLOPs",
                    "Hardware FLOPs Utilization (HFU)",
                    "Bytes/Param: 2B (BF16) vs 0.5B (FP4)",
                    "4-Model RLHF VRAM Multiplier",
                    "Optimizer State Memory (12B/param)",
                    "Activation Memory Checkpointing",
                    "NVLink All-Reduce Bandwidth",
                    "Cross-Node All-to-All Bottleneck",
                    "Thermal Throttling Mitigation",
                    "H100/B200 Secure Enclave (CC-On)",
                    "Power Usage Effectiveness (PUE)",
                    "Straggler GPU Detection",
                ],
            },
            "failure_modes": {
                "h1": [
                    "HBM Memory Bandwidth Wall (Decode)",
                    "CUDA Out-of-Memory (OOM) Crashes",
                    "Silent Tensor Core Bit-Flip Corrupt",
                ],
                "normal": [
                    "Low Decode MFU (<5% Compute Util)",
                    "PCIe Host-to-Device Bottleneck",
                    "InfiniBand Link Flaps & Stalls",
                    "Straggler GPU Halting 1,000 Nodes",
                    "4-Model RLHF VRAM Explosion",
                    "Thermal Throttling Under RL Rollouts",
                    "Unaligned Tensor Shapes (No TC)",
                    "Consumer GPU P2P Disabled Locks",
                    "Power Spike Breaker Trips",
                    "ECC Uncorrectable GPU Reset",
                ],
                "small": [],
            },
        },
    },
    {
        "layer": 2,
        "badge": "LAYER 2",
        "meter": "L2/7",
        "name": "ENV, PACKAGES, PYTHON & TENSOR",
        "osi_map": "OSI L2 Data Link · PDU: Wheels, Tensors & Paged KV",
        "desc": "Package managers (`Homebrew`, `uv`, `conda`, `pip`, `venv`), `Python`, `PyTorch`, `JAX`, `vLLM`, and sandboxes.",
        "book_ref": "Ch. 1.14–15, 11.1–9, 21.5, 22.1–9 (Env & Runtime).",
        "accent": "#0EA5E9",
        "cells": {
            "primitives_arch": {
                "h1": [
                    "Virtual Environments, Locks & Sandboxes",
                    "Autograd Computation Graphs & JIT",
                    "PagedAttention KV & Continuous Batch",
                ],
                "normal": [
                    "POSIX PTYs, Processes & Asyncio Loop",
                    "ABI / manylinux Wheels & uv.lock",
                    "OS Namespaces, cgroups & Seccomp",
                    "Dynamic Autograd DAG & torch.compile",
                    "PagedAttention Virtual Memory KV",
                    "RadixAttention Automatic Prefix Cache",
                    "Speculative Decoding (Draft + Verify)",
                    "3D Parallelism (DP/TP/PP/SP) & ZeRO",
                ],
                "small": [
                    "pyproject.toml (PEP 517 / 621)",
                    "Content-Addressable Global Cache",
                    "Hardlink / Reflink Env Cloning",
                    "LD_LIBRARY_PATH / DYLD RPATH",
                    "torch.compile (TorchInductor/Dynamo)",
                    "JAX jit / vmap / pmap / shard_map",
                    "XLA HLO Graph Fusion & CUDA Graphs",
                    "Disaggregated Prefill-Decode Routing",
                    "Chunked Prefill & Guided Decoding",
                    "KV-Cache FP8 / INT4 Quantization",
                    "Container UnionFS / OverlayFS Layers",
                    "Hardware Virtualization (KVM / HVF)",
                ],
            },
            "frameworks_stack": {
                "h1": [
                    "Homebrew (brew) · uv · conda · pip · venv",
                    "Python 3.12+ · PyTorch 2.x · JAX · MLX",
                    "vLLM · SGLang · llama.cpp · Docker · E2B",
                ],
                "normal": [
                    "Homebrew (brew) & System Toolchains",
                    "uv (uv venv / uv run / uvx / uv pip)",
                    "conda / Miniforge / mamba / Pixi / Poetry",
                    "pip · venv · virtualenv · pipx",
                    "PyTorch 2.x · JAX / Flax · Apple MLX",
                    "vLLM · SGLang · TensorRT-LLM · Ollama",
                    "Docker / OCI & NVIDIA Container Toolkit",
                    "Rust (PyO3/Maturin) & TypeScript/Bun",
                ],
                "small": [
                    "brew install uv git ripgrep fd tmux",
                    "uv lock & uv sync --frozen",
                    "environment.yml & conda-lock",
                    "pip install --no-build-isolation",
                    "DeepSpeed ZeRO & PyTorch FSDP2",
                    "llama.cpp (GGUF) & ExLlamaV2/v3",
                    "Outlines & XGrammar (JSON/CFG)",
                    "Ray Serve & NVIDIA Triton Server",
                    "ONNX Runtime & Safetensors Zero-Copy",
                    "Nix / Devcontainers / Direnv",
                    "Slurm / Kubernetes (K8s) / Ray",
                    "Pydantic v2 (Rust Schema Core)",
                ],
            },
            "ops_evals_security": {
                "h1": [
                    "E2B / Firecracker MicroVM Sandboxes",
                    "OS Sandboxing (Bubblewrap / Seatbelt)",
                    "TTFT / TPOT SLAs & Async RL Sync",
                ],
                "normal": [
                    "gVisor User-Space Kernel Isolation",
                    "macOS sandbox-exec & Linux bwrap",
                    "OpenEnv Standardized Gym Reset/Step",
                    "Air-Gapped VLAN & Egress Firewall",
                    "Scoped Ephemeral OAuth / API Tokens",
                    "NCCL Weight Broadcast (Trainer->vLLM)",
                    "Per-Tenant LoRA Adapter Hot-Swapping",
                    "Grammar-Constrained 100% Valid JSON",
                ],
                "small": [
                    "env.reset() / env.step(action) API",
                    "SWE-bench Docker Repo Images",
                    "OSWorld / WebArena Live Desktop VMs",
                    "TTFT < 200ms · TPOT < 15ms/tok",
                    "Goodput (SLO-Compliant Tok/s)",
                    "In-Flight Weight Update (Zero Stall)",
                    "S-LoRA / Punica Multi-Adapter Batch",
                    "Pyodide / Wasm Code Execution",
                    "Secret Scrubbing in Env Vars",
                    "SBOM & pip-audit Vulnerability Scan",
                    "Signed Container Attestation (Cosign)",
                    "Deterministic Seed Mode (cuDNN)",
                ],
            },
            "failure_modes": {
                "h1": [
                    "Python Dependency & CUDA ABI Hell",
                    "Unsandboxed Host RCE & rm -rf /",
                    "KV-Cache Fragmentation & Preemption",
                ],
                "normal": [
                    "nvcc vs. torch.version.cuda Mismatch",
                    "Global System Python Pollution",
                    "pip install Breaking flash-attn ABI",
                    "Typosquatted PyPI / npm / Skill Packs",
                    "Agent Leaking .env & SSH Keys",
                    "60–80% Contiguous KV Memory Waste",
                    "RL Rollout Generation Bottleneck",
                    "torch.compile Graph-Break Thrashing",
                    "NCCL Collective Deadlock / Timeout",
                    "/dev/shm Exhaustion in PyTorch DDP",
                ],
                "small": [],
            },
        },
    },
    {
        "layer": 3,
        "badge": "LAYER 3",
        "meter": "L3/7",
        "name": "DATA, TOKENIZATION & RAG",
        "osi_map": "OSI L3 Network · PDU: Token IDs, Embeddings & Chunks",
        "desc": "Pre-training/SFT/RLVR data curation, synthetic trajectories, BPE tokenizers, vector DBs, and Agentic RAG.",
        "book_ref": "Ch. 1.2, 3.2–5, 4.3, 16, 18.4, 30.2 (Data & RAG).",
        "accent": "#6366F1",
        "cells": {
            "primitives_arch": {
                "h1": [
                    "BPE Tokenization, Packing & Loss Masking",
                    "SFT, Preference & RLVR Data Curation",
                    "Embeddings, Vector HNSW & Hybrid RAG",
                ],
                "normal": [
                    "Byte-Level BPE / SentencePiece / Tiktoken",
                    "Sequence Packing & Position-ID Reset",
                    "Completion-Only Loss Masking (Labels=-100)",
                    "Chosen vs. Rejected Preference Pairs",
                    "Synthetic Reasoning & Trajectory Gen",
                    "Bi-Encoder (HNSW) vs. Cross-Encoder",
                    "Hybrid RAG (Dense + BM25 + RRF Fusion)",
                    "GraphRAG Entity Summaries & REFRAG",
                ],
                "small": [
                    "MinHash LSH & Exact Substring Dedup",
                    "FastText / KenLM Quality Filtering",
                    "Decontamination (N-gram / Embed Match)",
                    "ChatML Special Tokens (<|im_start|>)",
                    "Rejection Sampling (Best-of-N Filter)",
                    "Execution-Verified Code/Math Traces",
                    "Contextual Chunk Headers (Anthropic)",
                    "Late Interaction ColBERT Token MaxSim",
                    "Search-R1 RL Query Reformulation",
                    "Self-RAG Critique Tokens (ISREL/ISSUP)",
                    "Corrective RAG (CRAG) Web Fallback",
                    "Matryoshka Representation (MRL)",
                ],
            },
            "frameworks_stack": {
                "h1": [
                    "HF Datasets · Datatrove · NeMo Curator",
                    "Tiktoken · SentencePiece · HF Tokenizers",
                    "Qdrant · Milvus · pgvector · Neo4j",
                ],
                "normal": [
                    "FineWeb-Edu · Dolma · The Stack v2",
                    "Apache Arrow · Parquet · WebDataset",
                    "Docling · Unstructured · Marker PDF",
                    "Tree-sitter AST Codebase Chunking",
                    "BGE-M3 · Cohere Embed v3 & Rerank v3",
                    "FAISS · LanceDB · Chroma · Weaviate",
                    "LlamaIndex · Haystack · LightRAG",
                    "Distilabel · Curator Synthetic Suites",
                ],
                "small": [
                    "Polars · DuckDB · PyArrow ETL",
                    "Ray Data Distributed Streaming",
                    "MosaicML StreamingDataset (MDS)",
                    "OpenMathReasoning & NuminaMath",
                    "SWE-Gym & SWE-smith Trajectories",
                    "ShareGPT & OpenAI Harmony Formats",
                    "Firecrawl · Jina Reader Markdown",
                    "Graphiti & Cognee Knowledge Graphs",
                    "SQLite-vec & DuckDB-VSS Local",
                    "DVC & LakeFS Data Version Control",
                    "Cleanlab Automated Label Audit",
                    "Argilla Human-in-the-Loop Curation",
                ],
            },
            "ops_evals_security": {
                "h1": [
                    "RAG Triad Evals (Faithfulness / Recall)",
                    "Benchmark Decontamination & PII Scrub",
                    "Document-Level RBAC & Injection Scans",
                ],
                "normal": [
                    "Ragas & TruLens Groundedness Oracles",
                    "NDCG@k · MRR · Recall@k Retrieval Audits",
                    "Pre-Indexing ACL / RBAC Permission Tags",
                    "Regex + Presidio PII & Secret Scrubbing",
                    "Canary String & N-Gram Contamination",
                    "Synthetic Data Diversity & Entropy Audit",
                    "Citation Span-Locking & Provenance",
                    "Indirect Prompt Injection Sanitization",
                ],
                "small": [
                    "LLM-as-a-Judge Data Quality Scoring",
                    "Perplexity Outlier Filtering (KenLM)",
                    "Topic & Difficulty Curriculum Mix",
                    "Needle-in-a-Haystack (NIAH) & RULER",
                    "FRAMES & LongBench Multi-Hop Eval",
                    "Hallucination Span (LettuceDetect)",
                    "Poisoned Document Backdoor Scans",
                    "Copyright & SPDX License Filtering",
                    "Cross-Tenant Vector Namespace Auth",
                    "Embedding Drift & Stale Index Check",
                    "Tokenizer Fertility (Tok/Word) Audit",
                    "Zero-Retention Enterprise Pipelines",
                ],
            },
            "failure_modes": {
                "h1": [
                    "Garbage-In Synthetic Model Collapse",
                    "Naive Fixed-Size Mid-Table Chunking",
                    "Indirect Prompt Injection via RAG",
                ],
                "normal": [
                    "Training on Prompt Tokens (No -100 Mask)",
                    "Test-Set Contamination Mirage",
                    "Cross-Row Table & Function Splitting",
                    "Unfiltered Vector RAG Leaking Docs",
                    "Chat Template EOS/BOS Token Mismatch",
                    "Tokenizer Glitch & Byte-Fallback Bloat",
                    "Unverified Synthetic Hallucinations",
                    "Hallucinated Citations on Unread Text",
                    "Embedding Drift After Model Upgrades",
                    "PII & API Keys Baked Into Pretraining",
                ],
                "small": [],
            },
        },
    },
    {
        "layer": 4,
        "badge": "LAYER 4",
        "meter": "L4/7",
        "name": "MODEL ARCHITECTURE & RLVR",
        "osi_map": "OSI L4 Transport · PDU: Logits, Adapters & CoT",
        "desc": "Transformer/MoE/hybrid architectures, SFT, PEFT adapters (`LoRA`), preference tuning (`DPO`), and `RLVR` (`GRPO`).",
        "book_ref": "Ch. 1, 2.2, 3–10, 12–13, 30.1–3 (Models & RL).",
        "accent": "#8B5CF6",
        "cells": {
            "primitives_arch": {
                "h1": [
                    "Transformer · Sparse MoE · GQA / MLA",
                    "Hybrid Linear Attention (Mamba/DeltaNet)",
                    "PEFT (LoRA/DoRA) & RLVR (PPO/DPO/GRPO)",
                ],
                "normal": [
                    "Pre-Norm RMSNorm · SwiGLU · RoPE/YaRN",
                    "Grouped-Query (GQA) & Latent (MLA)",
                    "Sparse MoE Top-K & Shared Experts",
                    "Gated DeltaNet / Mamba-2 SSM Hybrid",
                    "LoRA · QLoRA (NF4) · DoRA · PiSSA",
                    "Preference Tuning: PPO · DPO · KTO",
                    "Critic-Free RLVR: GRPO · Dr.GRPO · DAPO",
                    "Harness Distillation (Harness-Zero)",
                ],
                "small": [
                    "Multi-Head Latent Attention (MLA)",
                    "Aux-Loss-Free MoE Load Balancing",
                    "rsLoRA (alpha/sqrt(r)) · QLoRA NF4",
                    "Zeroth-Order MeZO Forward-Only Tune",
                    "Bradley-Terry RM & Process RM (PRM)",
                    "IPO · ORPO · SimPO · Online DPO",
                    "RLCR Calibrated Brier Score Reward",
                    "On-Policy Self-Distillation (OPSD/RLCSD)",
                    "Test-Time Compute (Best-of-N / MCTS)",
                    "Cold-Start Pure-RL Emergence (R1-Zero)",
                    "MergeKit (SLERP / TIES / DARE)",
                    "AdamW vs. Muon Matrix Orthogonal",
                ],
            },
            "frameworks_stack": {
                "h1": [
                    "GPT-5.4 / o3 · Claude 4.6/5 · Gemini 3",
                    "DeepSeek-R1/V3.2 · Qwen 3 · Llama 4",
                    "HF TRL · PEFT · verl · OpenRLHF · Unsloth",
                ],
                "normal": [
                    "TRL (SFTTrainer / DPOTrainer / GRPO)",
                    "verl (HybridEngine RLHF/RLVR at Scale)",
                    "OpenRLHF (Ray + vLLM Distributed RL)",
                    "Unsloth (2x Speed Triton Backprop)",
                    "Axolotl & LLaMA-Factory YAML Suites",
                    "HuggingFace Transformers & PEFT",
                    "Prime Intellect verifiers & OpenR1",
                    "Torchtune & NeMo Aligner",
                ],
                "small": [
                    "DeepSeek-R1-Distill (7B–70B Weights)",
                    "Qwen3-235B-A22B & QwQ-32B",
                    "Claude Sonnet 4.5 / Opus 4.6 / 5.5",
                    "OpenAI GPT-5.4-Codex & o4-mini",
                    "Gemini 2.5 / 3.1 Pro & 3.8 Flash",
                    "Mistral Large 3 & Codestral",
                    "bitsandbytes (NF4) · AWQ · GPTQ",
                    "Lean 4 / SymPy Formal Math Verifiers",
                    "MergeKit CLI Checkpoint Merger",
                    "WandB / TensorBoard / MLflow Logs",
                    "vLLM Rollout Worker Integration",
                    "BitNet.cpp 1.58-Bit Ternary Weights",
                ],
            },
            "ops_evals_security": {
                "h1": [
                    "Verifiable Execution Oracles (RLVR)",
                    "KL-Divergence & Entropy Regularization",
                    "Constitutional AI & Safety Classifiers",
                ],
                "normal": [
                    "Deterministic Unit-Test / Math Graders",
                    "DAPO Clip-Higher & Dynamic Sampling",
                    "Multi-Objective Reward Combination",
                    "Listwise Rank-Based Reward Models",
                    "Instruction Hierarchy Privilege Training",
                    "Deliberative Alignment in CoT Traces",
                    "Activation Steering & SAE Circuit Probes",
                    "GCG / AutoDAN / Best-of-N Red-Teaming",
                ],
                "small": [
                    "KL Penalty beta * D_KL(pi_theta || pi_ref)",
                    "PPO Clipping epsilon in [0.1, 0.28]",
                    "GRPO Group Size G = 8..64 Rollouts",
                    "Pass@k vs. Majority@k Scaling",
                    "Length-Controlled Win-Rate Audits",
                    "Catastrophic Forgetting Evals",
                    "Sleeper Agent Backdoor Detection",
                    "Sandbagging & Alignment Faking Audits",
                    "Machine Unlearning (RMU / Grad Ascent)",
                    "CBRN / Cyber ASL-3/4 Threshold Gates",
                    "Contamination-Free LiveBench / HLE",
                    "Calibration Expected Error (ECE)",
                ],
            },
            "failure_modes": {
                "h1": [
                    "Reward Hacking & Length Inflation",
                    "Entropy Collapse & Mode Collapse",
                    "Catastrophic Forgetting / Alignment Tax",
                ],
                "normal": [
                    "GRPO Zero-Variance Advantage (All 0/1)",
                    "DPO Likelihood Displacement (Both Drop)",
                    "MoE Routing Collapse (Expert Starve)",
                    "Naive INT4 Quant Breaking Reasoning",
                    "Sycophancy & Delusional Validation",
                    "Emergent Misalignment from Narrow SFT",
                    "Over-Refusal on Benign Triggers",
                    "FP16 Loss-Scaling Underflow / NaNs",
                    "Stale Policy Weights in Async RL",
                    "Unbounded CoT Babbling Loops",
                ],
                "small": [],
            },
        },
    },
    {
        "layer": 5,
        "badge": "LAYER 5",
        "meter": "L5/7",
        "name": "CONTEXT, MEMORY, TOOLS & MCP",
        "osi_map": "OSI L5 Session · PDU: Context Windows & JSON-RPC",
        "desc": "Context budgeting, 4-tier agentic memory (`Sleep-Time Compute`), function calling, `MCP`, and `SKILL.md`.",
        "book_ref": "Ch. 17, 18.2–3, 23, 24 (Memory, Tools, MCP & Skills).",
        "accent": "#EC4899",
        "cells": {
            "primitives_arch": {
                "h1": [
                    "Context Engineering & Token Budgeting",
                    "4-Tier Memory + Sleep-Time Dreaming",
                    "Tool Calling, MCP Bus & Progressive Skills",
                ],
                "normal": [
                    "Working Memory (Active Context Window)",
                    "Episodic Memory (Past Experience Logs)",
                    "Semantic Memory (Entity/Fact Triples)",
                    "Procedural Memory (SKILL.md / Weights)",
                    "Sleep-Time Offline Consolidation (Dream)",
                    "JSON-RPC 2.0 Host-Client-Server Bus",
                    "Progressive Disclosure Skill Loading",
                    "Observation Masking & /compact Hygiene",
                ],
                "small": [
                    "System / History / RAG / Tool Scratchpad",
                    "Write / Read / Reflect / Consolidate Ops",
                    "Ebbinghaus Temporal Memory Decay",
                    "Proactive Context Pre-Fetching",
                    "KV-Cache Prefix Pinning (90% Discount)",
                    "Parallel Tool-Call Batch Execution",
                    "Strict JSON Schema Tool Definitions",
                    "Code-Act (Python Execution as Tool)",
                    "Dynamic Tool Search (Top-K Schemas)",
                    "Rolling Summary & Turn Truncation",
                    "Subagent Forked Context Isolation",
                    "Scratchpad & Todo.md State Offload",
                ],
            },
            "frameworks_stack": {
                "h1": [
                    "Model Context Protocol (MCP / .mcp.json)",
                    "Agent Skills (SKILL.md Folder Standard)",
                    "Letta (MemGPT) · Mem0 · Zep · LangMem",
                ],
                "normal": [
                    "MCP Primitives: Tools, Resources, Prompts",
                    "MCP Transports: stdio & Streamable HTTP",
                    "FastMCP Python / TypeScript SDKs",
                    "SKILL.md YAML Frontmatter + Instructions",
                    "skills/scripts/ & skills/references/ Dirs",
                    "Letta (MemGPT) OS-Paged Memory Blocks",
                    "Mem0 · Zep · Graphiti Temporal Memory",
                    "Linux Foundation AAIF MCP Registry",
                ],
                "small": [
                    "MCP Sampling & Roots Client Callbacks",
                    "MCP Elicitation User Confirmation",
                    ".claude/skills/ & .agents/skills/ Paths",
                    "agentskills.io Open Specification",
                    "LangMem Semantic/Episodic Store",
                    "Cognee & Memary Memory Engines",
                    "Redis / Postgres Agent Session Stores",
                    "OpenAPI-to-MCP Auto-Generators",
                    "Browserbase / Playwright MCP Servers",
                    "GitHub / Slack / Postgres MCP Servers",
                    "Anthropic & Cursor MCP Marketplaces",
                    "Smithery & Glama MCP Registries",
                ],
            },
            "ops_evals_security": {
                "h1": [
                    "MCP OAuth 2.1 Scopes & Tool Signing",
                    "/compact Hygiene (<65% Context Cap)",
                    "Memory Contradiction & Decay Audits",
                ],
                "normal": [
                    "Human-in-the-Loop Destructive Tool Gate",
                    "Tool Schema Token-Bloat Minimization",
                    "Memory Contradiction & Stale-Fact Purge",
                    "LOCOMO & LongMemEval Memory Evals",
                    "MCP Server Code-Signing Verification",
                    "Least-Privilege Read-Only Connectors",
                    "OX Security stdio RCE Hardening",
                    "Cross-Tenant Memory Isolation",
                ],
                "small": [
                    "Context Utilization < 65% Rot Threshold",
                    "Lost-in-the-Middle U-Curve Placement",
                    "BFCL (Berkeley Function-Calling) Eval",
                    "ToolBench & API-Bank Multi-Tool Eval",
                    "Episodic Replay Buffer Deduplication",
                    "Tool Output Truncation & Pagination",
                    "Skill Static Analysis Before Install",
                    "Egress Domain Whitelisting per Tool",
                    "OAuth 2.1 PKCE Token Refresh Flow",
                    "Idempotency Keys for Mutating Tools",
                    "Audit Logging of All JSON-RPC Calls",
                    "Canary Tokens in Memory Stores",
                ],
            },
            "failure_modes": {
                "h1": [
                    "Context Rot & Lost-in-the-Middle",
                    "MCP Tool Bloat (100+ Schemas)",
                    "Malicious Skills & MCP Rug-Pulls",
                ],
                "normal": [
                    "100+ MCP Tool Schemas Blowing Context",
                    "ClawHavoc Malicious SKILL.md Payloads",
                    "MCP Rug-Pull & Tool Shadowing Attacks",
                    "Memory Poisoning Across Sessions",
                    "Stale Episodic Memory Overriding Code",
                    "stdio MCP Server Spawning Host Shells",
                    "Malformed Tool-Call JSON Loops",
                    "Unbounded Tool Output Flooding Window",
                    "/compact Summarization Losing Constraints",
                    "Cross-User Memory Bleed in Shared DB",
                ],
                "small": [],
            },
        },
    },
    {
        "layer": 6,
        "badge": "LAYER 6",
        "meter": "L6/7",
        "name": "AGENT HARNESS, LOOP & GRAPH",
        "osi_map": "OSI L6 Presentation · PDU: State Transitions & Diffs",
        "desc": "The CPU/OS of an agent: `CLAUDE.md`/`AGENTS.md`, Loop Engineering, Graph Engineering (`LangGraph`), and `Harness²`.",
        "book_ref": "Ch. 18, 19, 20, 21, 27 (Harness, Loops & Graphs).",
        "accent": "#F59E0B",
        "cells": {
            "primitives_arch": {
                "h1": [
                    "Agent Harness (Prompt+Tools+State+Loop)",
                    "Loop Engineering (Observe→Decide→Act)",
                    "Graph Engineering (Typed StateGraphs)",
                ],
                "normal": [
                    "ReAct · Reflexion · Plan-and-Execute",
                    "5 Loop Primitives (State/Step/Check/Stop)",
                    "Typed State Schema & Reducer Functions",
                    "Conditional Edges & Cyclic Graph Routing",
                    "Fan-Out / Fan-In Parallel Send() API",
                    "Recursive Agent Harnessing (Harness²)",
                    "Spec-Driven Development (Spec→Plan→Task)",
                    "Cognitive Escalation & Uncertainty Handoff",
                ],
                "small": [
                    "pi(a_t | s_t) Inference-Time Policy Loop",
                    "LATS (Language Agent Tree Search)",
                    "LLM Compiler Parallel DAG Execution",
                    "BDI (Belief-Desire-Intention) Hybrid",
                    "Checkpointer Time-Travel & Replay",
                    "Human-in-the-Loop Interrupt() Gates",
                    "Stagnation & Repeat-Action Detection",
                    "Subagent Context Isolation (Forked Call)",
                    "Red-Green-Refactor TDD Agent Cycle",
                    "Exponential Backoff & Schema Self-Repair",
                    "Token/Cost/Iteration Termination Caps",
                    "Dynamic Model Routing (Fast vs. Reasoner)",
                ],
            },
            "frameworks_stack": {
                "h1": [
                    "Claude Code CLI · Codex CLI · OpenCode",
                    "Cursor · Windsurf · Cline / Roo · Aider",
                    "LangGraph · OpenAI Agents SDK · DSPy",
                ],
                "normal": [
                    "CLAUDE.md & AGENTS.md Repo Constitutions",
                    ".cursor/rules & .github/copilot-instructions",
                    "GitHub Spec Kit & obra/superpowers TDD",
                    "LlamaIndex Workflows (Event-Driven)",
                    "Smolagents (CodeAct Python-as-Action)",
                    "PydanticAI Type-Safe Agent Harness",
                    "OpenHands (OpenDevin) & Block goose",
                    "Semantic Kernel & Haystack Agents",
                ],
                "small": [
                    "LangGraph PostgresCheckpointer",
                    "DSPy MIPROv2 Prompt/Weight Compiler",
                    "Claude Agent SDK & Computer Use API",
                    "Browser-Use & Playwright DOM Harnesses",
                    "Vercel AI SDK Core (generateText/maxSteps)",
                    "Guardrails AI & NeMo Guardrails",
                    "Instructor & BAML Structured Outputs",
                    "Litellm Unified Model Router",
                    "Git Pre-Commit & CI Harness Hooks",
                    "Repomix / Gitingest Codebase Packers",
                    "LangSmith · Arize Phoenix · Langfuse",
                    "OpenTelemetry (OTel) GenAI Spans",
                ],
            },
            "ops_evals_security": {
                "h1": [
                    "Decoupled Verification Oracles (No Self-Grade)",
                    "SWE-bench Verified/Pro & Terminal-Bench",
                    "pass^k Reliability & Trajectory Tracing",
                ],
                "normal": [
                    "Property-Based Testing (Hypothesis/Kani)",
                    "Mutation Testing (Stryker / mutmut) Gates",
                    "Immutable CI Tests Locked From Agent Write",
                    "Trajectory Tool-Call Exact/Prefix Match",
                    "LLM-as-a-Judge Pairwise Rubric Grading",
                    "Cost-per-Resolved-Task Efficiency Metric",
                    "PyRIT & Garak Adversarial Red-Teaming",
                    "LlamaFirewall Prompt/Tool Guardrails",
                ],
                "small": [
                    "pass^k = (pass@1)^k Consistency Metric",
                    "METR 50%-Reliability Horizon (2h–30h)",
                    "GAIA · OSWorld · WebArena · TAU-bench",
                    "Scale SWE-bench Pro (Private Repos)",
                    "Step Efficiency (Optimal / Actual Steps)",
                    "Deterministic Mock-Tool Replay Harness",
                    "Shadow-Mode Traffic Counterfactual Eval",
                    "Circuit-Breaker Spend & Loop-Depth Caps",
                    "Canary Token Exfiltration Tripwires",
                    "Git Diff AST Security Linter (Semgrep)",
                    "Automated Rollback on Regression",
                    "EU AI Act / SOC2 Immutable Audit Logs",
                ],
            },
            "failure_modes": {
                "h1": [
                    "Agent Deleting / Mocking Failing Tests",
                    "Unbounded Loop Burn & Action Stagnation",
                    "God-Node Anti-Pattern & State Bloat",
                ],
                "normal": [
                    "Coupled Agent Rewriting Its Own Grader",
                    "0.95^20 = 35.8% Compounding Step Decay",
                    "Poisoned .cursor/rules or GitHub Issues",
                    "CVE-2025-53773 IDE Config Auto-Approve RCE",
                    "Swallowing Exceptions in Tool Wrappers",
                    "Appending Raw 50KB HTML to Graph State",
                    "Premature Termination Before Verification",
                    "Sycophantic Plan Pivot on User Pushback",
                    "Single-Turn Eval Masking Multi-Turn Fail",
                    "Context Exhaustion Mid-Refactoring",
                ],
                "small": [],
            },
        },
    },
    {
        "layer": 7,
        "badge": "LAYER 7",
        "meter": "L7/7",
        "name": "MULTI-AGENT MESH, A2A & UI",
        "osi_map": "OSI L7 Application · PDU: A2A Tasks & GenUI Streams",
        "desc": "Multi-agent topologies (`OWC`), inter-agent protocols (`A2A`/`ACP`), parallel worktree swarms, and Agentic/Generative UI.",
        "book_ref": "Ch. 21.6, 25, 26, 28, 30.10/18 (A2A, MAS & Agentic UI).",
        "accent": "#F43F5E",
        "cells": {
            "primitives_arch": {
                "h1": [
                    "Orchestrator-Worker-Critic (OWC) Pattern",
                    "Multi-Agent Topologies (Hierarchical/Mesh)",
                    "Generative UI & Shared State Sync",
                ],
                "normal": [
                    "Centralized Supervisor vs. Decentralized",
                    "Hierarchical Tree (Squads of Squads)",
                    "Debate / Society-of-Mind Consensus",
                    "Blackboard Shared-Memory Coordination",
                    "Contract-Net Task Bidding & Auctions",
                    "Parallel Git-Worktree Swarm Isolation",
                    "A2A (Horizontal) × MCP (Vertical) Dual Bus",
                    "Human-on-the-Loop Escalation & Approval",
                ],
                "small": [
                    "Agent Card (/.well-known/agent.json)",
                    "Task Lifecycle (Submitted→Working→Done)",
                    "Multi-Agent MDP & CTDE MARL Training",
                    "Credit Assignment (Shapley / Counterfactual)",
                    "Role Specialization & Persona Diversity",
                    "Byzantine Fault-Tolerant Critic Voting",
                    "Pub/Sub Asynchronous Event Choreography",
                    "Process-Centric Enterprise State Workflows",
                    "Server-Driven UI Component Streaming",
                    "Optimistic UI Updates & Diff Previews",
                    "Ambient OS Cross-App Delegation",
                    "Organizational Digital-Twin Simulation",
                ],
            },
            "frameworks_stack": {
                "h1": [
                    "Google A2A Protocol · IBM ACP · ANP",
                    "CrewAI · AutoGen / AG2 · LangGraph Swarm",
                    "CopilotKit · AG-UI · Vercel AI SDK UI",
                ],
                "normal": [
                    "Google Agent-to-Agent (A2A) JSON-RPC/SSE",
                    "IBM BeeAI & Agent Communication Protocol",
                    "Microsoft AutoGen v0.4 / Semantic Kernel",
                    "CrewAI Flows & Role-Based Crews",
                    "Claude Code Subagents & Worktree Swarms",
                    "OpenClaw 24/7 Multi-Channel Agent Daemon",
                    "Agent Gateways (Kong / Solo / LiteLLM)",
                    "Claude Artifacts · ChatGPT/Gemini Canvas",
                ],
                "small": [
                    "AG-UI (Agent-User Interaction Protocol)",
                    "Vercel AI SDK useChat / streamUI Hooks",
                    "Chainlit · Streamlit · Gradio Agent UIs",
                    "OpenAI ChatKit & Realtime WebRTC Voice",
                    "LangGraph Platform Cloud & Studio UI",
                    "Camel-AI Workforce & MetaGPT SOPs",
                    "OpenAI Swarm / Agents SDK Handoffs",
                    "A2A Artifact & Push-Notification Webhooks",
                    "React Server Components (RSC) GenUI",
                    "Slack / Discord / WhatsApp Bot Bridges",
                    "Linear / GitHub PR Async Agent Teammates",
                    "1-Click MCP & A2A Enterprise Registries",
                ],
            },
            "ops_evals_security": {
                "h1": [
                    "Agent Gateway (mTLS, Auth, FinOps Caps)",
                    "Cross-Agent Trust & Cryptographic KYA",
                    "Independent Critic & Red-vs-Blue Swarms",
                ],
                "normal": [
                    "Zero-Trust Agent Identity (SPIFFE / KYA)",
                    "OAuth 2.1 On-Behalf-Of (OBO) Token Flow",
                    "Per-Swarm Token & Dollar Circuit Breakers",
                    "Anti-Collusion & Decorrelated Critic Models",
                    "Cross-Repo API Contract Locks (OpenAPI)",
                    "Deadlock, Livelock & Cycle Detection",
                    "Provenance Watermarking (C2PA / SynthID)",
                    "Strict Liability & Action Audit Ledgers",
                ],
                "small": [
                    "Communication Overhead O(N^2) Pruning",
                    "Multi-Agent Judge Independence Check",
                    "Cross-Org Data-Loss Prevention (DLP)",
                    "Swarm Amplification Factor Monitoring",
                    "Canary Deployment of Agent Topologies",
                    "Chaos Engineering (Injecting Rogue Agents)",
                    "XBOW / Cybench / T3MP3ST Cyber Ranges",
                    "Lean 4 / TLA+ Formal Protocol Verification",
                    "Human Escalation SLA Latency Tracking",
                    "Anti-Sycophancy & Anti-Psychosis Filters",
                    "GDPR / HIPAA Cross-Agent Consent Scopes",
                    "Kill-Switch Broadcast Across Swarm Nodes",
                ],
            },
            "failure_modes": {
                "h1": [
                    "Cascading Hallucination & Swarm Echo",
                    "O(N²) Chatty Agent Token Explosion",
                    "Cross-Agent Confused Deputy & Escalation",
                ],
                "normal": [
                    "7-Persona Roleplay Chatter Burning 15x Cost",
                    "Homogeneous Critic Blindly Agreeing",
                    "Supervisor Bottleneck & Context Overflow",
                    "Merge Conflicts Across Parallel Worktrees",
                    "Rogue Subagent Bypassing Parent Scopes",
                    "Infinite Ping-Pong Handoff Deadlocks",
                    "Free-Riding Worker Agents in Crews",
                    "UI Stream Desync & Phantom Tool States",
                    "Automation Bias Rubber-Stamping Swarm PRs",
                    "Unattributed Multi-Agent Tort Liability",
                ],
                "small": [],
            },
        },
    },
]


def render_desktop_agent_anatomy_megachart():
    """
    Desktop Widescreen Megachart (24.0 x 17.5 in @ 300 DPI).
    Mirrors the visual hierarchy of `AI_skill_tree_2026` while mapping the
    7-Layer OSI-Inspired Anatomy of AI Agents (Physical Silicon -> Multi-Agent Mesh).
    """
    plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]

    fig = plt.figure(figsize=(24.0, 17.5), dpi=300, facecolor="#0F172A")
    ax = fig.add_axes([0.004, 0.004, 0.992, 0.992])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    bg_canvas = FancyBboxPatch(
        (0.001, 0.001), 0.998, 0.998,
        boxstyle="round,pad=0.0,rounding_size=0.006",
        facecolor="#E2E8F0", edgecolor="#0F172A", linewidth=1.5
    )
    ax.add_patch(bg_canvas)

    # -------------------------------------------------------------------------
    # 1. Top Masthead (Title + Website + Yellow Hook + Blue How-to-Read + Footnote)
    # -------------------------------------------------------------------------
    hdr_y = 0.916
    hdr_h = 0.079
    hdr_box = FancyBboxPatch(
        (0.005, hdr_y), 0.990, hdr_h,
        boxstyle="round,pad=0.0,rounding_size=0.006",
        facecolor="#0F172A", edgecolor="#1E293B", linewidth=1.8
    )
    ax.add_patch(hdr_box)

    # Left Block: Giant Title + Website Underneath
    ax.text(
        0.013, hdr_y + hdr_h * 0.70,
        "ANATOMY OF AI AGENTS 2026",
        fontsize=31.0, fontweight="bold", color="#FFFFFF", va="center", ha="left"
    )
    ax.text(
        0.014, hdr_y + hdr_h * 0.36,
        "www.arianprabowo.com  ·  7-Layer OSI-Style Stack Reference (Based on Roitman arXiv:2606.24937)",
        fontsize=11.0, fontweight="bold", color="#38BDF8", va="center", ha="left"
    )

    # Vertical divider 1
    ax.plot(
        [0.440, 0.440], [hdr_y + hdr_h * 0.24, hdr_y + hdr_h * 0.91],
        color="#334155", linewidth=1.4
    )

    # Middle Block: Yellow Motivating Hook
    ax.text(
        0.450, hdr_y + hdr_h * 0.58,
        "What actually runs under the hood of an autonomous AI agent in 2026?\n"
        "Like the 7-layer OSI model, modern agents are a vertical stack — from GPU silicon (L1) &\n"
        "uv/PyTorch/JAX (L2) to Data/RAG (L3), Arch/RLVR (L4), MCP (L5), Harness² (L6) & A2A swarms (L7).",
        fontsize=9.1, fontweight="bold", color="#FEF08A", va="center", ha="left",
        linespacing=1.18
    )

    # Vertical divider 2
    ax.plot(
        [0.758, 0.758], [hdr_y + hdr_h * 0.24, hdr_y + hdr_h * 0.91],
        color="#334155", linewidth=1.4
    )

    # Right Block: Blue 3-Step Key
    ax.text(
        0.768, hdr_y + hdr_h * 0.58,
        "① TRACE THE STACK: Follow Layers 1 → 7 from silicon to swarms\n"
        "② BUILD EACH LAYER: Top 3 pills = flagship 2026 primitives & tools\n"
        "③ HARDEN PROD: Audit the red FAILURE MODES & TRAPS on the right",
        fontsize=9.0, fontweight="bold", color="#93C5FD", va="center", ha="left",
        linespacing=1.22
    )

    # Horizontal divider above bottom footnote strip
    ax.plot(
        [0.012, 0.988], [hdr_y + hdr_h * 0.20, hdr_y + hdr_h * 0.20],
        color="#1E293B", linewidth=1.0
    )

    # Bottom Combined Grey Footnote Strip
    ax.text(
        0.500, hdr_y + hdr_h * 0.095,
        f"*Synthesized from Haggai Roitman's 'The Hitchhiker's Guide to Agentic AI: From Foundations to Systems' (arXiv:2606.24937, v1.4, June 2026) + 2026 systems tooling. "
        f"Companion to AI Skill Tree 2026 & AI Ladder Evolution by Arian Prabowo · {LAST_UPDATED_STR}",
        fontsize=6.4, fontweight="bold", color="#94A3B8", va="center", ha="center"
    )

    # -------------------------------------------------------------------------
    # 2. Column Headers
    # -------------------------------------------------------------------------
    col_hdr_y = 0.881
    col_hdr_h = 0.031

    left_x0 = 0.005
    left_w = 0.142

    col_gap = 0.0045
    active_x0 = left_x0 + left_w + col_gap
    active_col_w = 0.224
    sep_x = active_x0 + 3 * active_col_w + 2 * col_gap + 0.0045
    obs_x0 = sep_x + 0.0045
    obs_w = 0.995 - obs_x0

    col_geoms = [
        (active_x0 + 0 * (active_col_w + col_gap), active_col_w),
        (active_x0 + 1 * (active_col_w + col_gap), active_col_w),
        (active_x0 + 2 * (active_col_w + col_gap), active_col_w),
        (obs_x0, obs_w),
    ]

    # Red dashed vertical separator line before FAILURE MODES & TRAPS
    ax.plot(
        [sep_x, sep_x], [0.005, col_hdr_y + col_hdr_h],
        color="#DC2626", linewidth=1.8, linestyle=(0, (6, 3)), alpha=0.70
    )

    lhdr = FancyBboxPatch(
        (left_x0, col_hdr_y), left_w, col_hdr_h,
        boxstyle="round,pad=0.0,rounding_size=0.004",
        facecolor="#0F172A", edgecolor="#334155", linewidth=1.5
    )
    ax.add_patch(lhdr)
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.65,
        "OSI AGENT LAYER",
        fontsize=13.2, fontweight="bold", color="#FFFFFF", va="center", ha="center"
    )
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.22,
        "OSI Analogy · PDU · Scope · Ch.",
        fontsize=6.8, fontweight="bold", color="#94A3B8", va="center", ha="center"
    )

    for c_idx, col in enumerate(COLUMNS):
        cx, cw = col_geoms[c_idx]
        is_fail = col["key"] == "failure_modes"
        chdr = FancyBboxPatch(
            (cx, col_hdr_y), cw, col_hdr_h,
            boxstyle="round,pad=0.0,rounding_size=0.004",
            facecolor=col["hdr_bg"], edgecolor="#0F172A", linewidth=1.4
        )
        ax.add_patch(chdr)
        ax.text(
            cx + cw / 2, col_hdr_y + col_hdr_h * 0.65,
            col["title"],
            fontsize=13.0 if not is_fail else 12.2,
            fontweight="bold", color="#FFFFFF", va="center", ha="center"
        )
        ax.text(
            cx + cw / 2, col_hdr_y + col_hdr_h * 0.21,
            col["sub"],
            fontsize=6.8 if is_fail else 7.1,
            fontweight="bold", color="#FEE2E2" if is_fail else "#E2E8F0", va="center", ha="center"
        )

    # -------------------------------------------------------------------------
    # 3. 7 Layer Rows x 4 Columns
    # -------------------------------------------------------------------------
    top_y = 0.8765
    bot_y = 0.0045
    n_layers = len(STACK_LAYERS)
    row_gap = 0.0038
    row_h = (top_y - bot_y - (n_layers - 1) * row_gap) / n_layers

    for r_idx, ly in enumerate(STACK_LAYERS):
        y0 = top_y - (r_idx + 1) * row_h - r_idx * row_gap

        # Left Column Card (Layer Badge + 7-Segment Stack Meter + OSI PDU + Book Ref)
        lbox_body = FancyBboxPatch(
            (left_x0, y0), left_w, row_h,
            boxstyle="round,pad=0.0,rounding_size=0.004",
            facecolor="#0F172A", edgecolor="#334155", linewidth=1.5
        )
        ax.add_patch(lbox_body)

        inset_b = 0.0016
        banner_h = row_h * 0.300
        lbox_top = FancyBboxPatch(
            (left_x0 + inset_b, y0 + row_h - banner_h - inset_b),
            left_w - 2 * inset_b, banner_h,
            boxstyle="round,pad=0.0,rounding_size=0.003",
            facecolor="#1E293B", edgecolor=ly["accent"], linewidth=1.4
        )
        ax.add_patch(lbox_top)

        ax.text(
            left_x0 + 0.0050, y0 + row_h - inset_b - banner_h * 0.34,
            ly["badge"],
            fontsize=15.0, fontweight="bold", color="#FFFFFF", va="center", ha="left"
        )

        # 7-segment vector progress bar on top-right of banner
        bar_total_w = 0.052
        bar_gap = 0.0012
        seg_w = (bar_total_w - 6 * bar_gap) / 7.0
        seg_h = banner_h * 0.23
        bar_x_start = left_x0 + left_w - 0.0050 - bar_total_w
        bar_y = y0 + row_h - inset_b - banner_h * 0.34 - seg_h / 2.0
        for b_i in range(7):
            bx_i = bar_x_start + b_i * (seg_w + bar_gap)
            is_lit = b_i < ly["layer"]
            seg_patch = FancyBboxPatch(
                (bx_i, bar_y), seg_w, seg_h,
                boxstyle="round,pad=0.0,rounding_size=0.001",
                facecolor=ly["accent"] if is_lit else "#334155",
                edgecolor=ly["accent"] if is_lit else "#475569",
                linewidth=0.6
            )
            ax.add_patch(seg_patch)

        ax.text(
            left_x0 + left_w / 2, y0 + row_h - inset_b - banner_h * 0.77,
            ly["name"],
            fontsize=9.6 if len(ly["name"]) >= 22 else 10.3,
            fontweight="bold", color="#FEF08A", va="center", ha="center"
        )

        desc_wrapped = textwrap.fill(ly["desc"], width=34)
        osi_wrapped = textwrap.fill(f"• {ly['osi_map']}", width=34)
        ref_wrapped = textwrap.fill(f"• Guide: {ly['book_ref']}", width=34)

        body_top_y = y0 + (row_h - banner_h - inset_b) * 0.94
        ax.text(
            left_x0 + 0.0035,
            body_top_y,
            desc_wrapped,
            fontsize=7.35,
            fontweight="bold",
            color="#F8FAFC",
            va="top",
            ha="left",
            linespacing=1.08,
        )

        bullet_body = f"{osi_wrapped}\n{ref_wrapped}"
        ax.text(
            left_x0 + 0.0035,
            body_top_y - 0.031,
            bullet_body,
            fontsize=7.05,
            fontweight="bold",
            color="#93C5FD",
            va="top",
            ha="left",
            linespacing=1.08,
        )

        # 4 Architectural Pillar Columns
        for c_idx, col in enumerate(COLUMNS):
            cx, cw = col_geoms[c_idx]
            is_fail = col["key"] == "failure_modes"

            cell_data = ly["cells"][col["key"]]
            top_h1 = cell_data["h1"]
            mid_norm = cell_data["normal"]
            bot_small = cell_data["small"]

            cbox = FancyBboxPatch(
                (cx, y0), cw, row_h,
                boxstyle="round,pad=0.0,rounding_size=0.004",
                facecolor=col["cell_bg"],
                edgecolor=col["cell_edge"],
                linewidth=1.5 if not is_fail else 1.6,
                linestyle="--" if is_fail else "-"
            )
            ax.add_patch(cbox)

            pad_x = 0.0026
            pad_top = 0.0022
            pad_bot = 0.0020
            inner_w = cw - 2 * pad_x
            x_left = cx + pad_x

            # =================================================================
            # CASE A: Failure Modes Column (Top 3 H1 Pills + 4x1 Tier 2 + 4x1 Tier 3)
            # =================================================================
            if is_fail:
                gap_t1_t2 = 0.0017
                gap_t2_t3 = 0.0014
                avail_h = row_h - pad_top - pad_bot - gap_t1_t2 - gap_t2_t3
                t1_h = avail_h * 0.390
                t2_h = avail_h * 0.365
                t3_h = avail_h * 0.245

                t1_top_y = y0 + row_h - pad_top
                pill_gap = 0.0015
                ph = (t1_h - 2 * pill_gap) / 3.0
                for idx_1, kw in enumerate(top_h1[:3]):
                    px = x_left
                    pw = inner_w
                    py = t1_top_y - (idx_1 + 1) * ph - idx_1 * pill_gap
                    pill = FancyBboxPatch(
                        (px, py), pw, ph,
                        boxstyle="round,pad=0.0,rounding_size=0.0022",
                        facecolor=col["h1_bg"],
                        edgecolor=col["pill_edge"],
                        linewidth=1.1,
                        linestyle="--"
                    )
                    ax.add_patch(pill)
                    ax.text(
                        px + pw / 2, py + ph / 2,
                        kw,
                        fontsize=9.9 if len(kw) > 34 else 10.4,
                        fontweight="bold",
                        color=col["h1_txt"],
                        va="center", ha="center"
                    )

                # Tier 2: 4 single-column rows (full width, zero horizontal collision)
                t2_top_y = t1_top_y - t1_h - gap_t1_t2
                t2_row_h = t2_h / 4.0

                for r_div in range(1, 4):
                    hy = t2_top_y - r_div * t2_row_h
                    ax.plot(
                        [x_left + 0.0004, x_left + inner_w - 0.0004],
                        [hy, hy],
                        color="#FECACA", linewidth=0.55
                    )

                for sr, kw in enumerate(mid_norm[:4]):
                    if sr % 2 == 1:
                        stripe = FancyBboxPatch(
                            (x_left, t2_top_y - (sr + 1) * t2_row_h + 0.00012),
                            inner_w, t2_row_h - 0.00024,
                            boxstyle="round,pad=0.0,rounding_size=0.001",
                            facecolor="#FEE2E2", edgecolor="none", alpha=0.65
                        )
                        ax.add_patch(stripe)
                    tx = x_left + 0.0025
                    ty = t2_top_y - (sr + 0.5) * t2_row_h
                    ax.text(
                        tx, ty,
                        f"▸ {kw}",
                        fontsize=6.45,
                        fontweight="bold",
                        color=col["t2_txt"],
                        va="center", ha="left"
                    )

                # Tier 3: Bottom 4 single-column rows in matching band
                t3_top_y = t2_top_y - t2_h - gap_t2_t3
                t3_row_h = t3_h / 4.0

                t3_band = FancyBboxPatch(
                    (x_left, y0 + pad_bot),
                    inner_w, t3_h,
                    boxstyle="round,pad=0.0,rounding_size=0.0018",
                    facecolor="#FFF1F2",
                    edgecolor="#FCA5A5",
                    linewidth=0.6
                )
                ax.add_patch(t3_band)

                for sr, kw in enumerate(mid_norm[4:8]):
                    tx = x_left + 0.0025
                    ty = t3_top_y - (sr + 0.5) * t3_row_h
                    ax.text(
                        tx, ty,
                        f"• {kw}",
                        fontsize=5.35,
                        fontweight="bold",
                        color="#991B1B",
                        va="center", ha="left"
                    )
                continue

            # =================================================================
            # CASE B: Full 3-Tier Active Architectural Cell
            # =================================================================
            gap_t1_t2 = 0.0017
            gap_t2_t3 = 0.0014
            avail_h = row_h - pad_top - pad_bot - gap_t1_t2 - gap_t2_t3
            t1_h = avail_h * 0.390
            t2_h = avail_h * 0.365
            t3_h = avail_h * 0.245

            # --- TIER 1: Top 3 H1 Pills ---
            t1_top_y = y0 + row_h - pad_top
            pill_gap = 0.0015
            ph = (t1_h - 2 * pill_gap) / 3.0
            for idx_1, kw in enumerate(top_h1[:3]):
                px = x_left
                pw = inner_w
                py = t1_top_y - (idx_1 + 1) * ph - idx_1 * pill_gap

                pill = FancyBboxPatch(
                    (px, py), pw, ph,
                    boxstyle="round,pad=0.0,rounding_size=0.0022",
                    facecolor=col["h1_bg"],
                    edgecolor=col["pill_edge"],
                    linewidth=1.15
                )
                ax.add_patch(pill)

                ax.text(
                    px + pw / 2, py + ph / 2,
                    kw,
                    fontsize=11.4,
                    fontweight="bold",
                    color=col["h1_txt"],
                    va="center", ha="center"
                )

            # --- TIER 2: Middle 8 in 2 Columns x 4 Rows ---
            t2_top_y = t1_top_y - t1_h - gap_t1_t2
            t2_row_h = t2_h / 4.0
            t2_col_w = inner_w / 2.0

            ax.plot(
                [x_left + t2_col_w, x_left + t2_col_w],
                [t2_top_y - t2_h + 0.0005, t2_top_y - 0.0005],
                color="#CBD5E1", linewidth=0.8
            )

            for idx_2, kw in enumerate(mid_norm[:8]):
                sr = idx_2 // 2
                sc = idx_2 % 2
                if sc == 0 and sr % 2 == 1:
                    stripe = FancyBboxPatch(
                        (x_left, t2_top_y - (sr + 1) * t2_row_h + 0.00012),
                        inner_w, t2_row_h - 0.00024,
                        boxstyle="round,pad=0.0,rounding_size=0.001",
                        facecolor=col["t2_bg"], edgecolor="none"
                    )
                    ax.add_patch(stripe)

                tx = x_left + sc * t2_col_w + 0.0015
                ty = t2_top_y - (sr + 0.5) * t2_row_h
                ax.text(
                    tx, ty,
                    kw,
                    fontsize=6.15 if len(kw) > 34 else 6.45,
                    fontweight="bold",
                    color=col["t2_txt"],
                    va="center", ha="left"
                )

            # --- TIER 3: Bottom 12 in 3 Columns x 4 Rows ---
            t3_top_y = t2_top_y - t2_h - gap_t2_t3
            t3_row_h = t3_h / 4.0
            t3_col_w = inner_w / 3.0

            t3_band = FancyBboxPatch(
                (x_left, y0 + pad_bot),
                inner_w, t3_h,
                boxstyle="round,pad=0.0,rounding_size=0.0018",
                facecolor=col["t3_bg"],
                edgecolor="#CBD5E1",
                linewidth=0.6
            )
            ax.add_patch(t3_band)

            for c_div in (1, 2):
                ax.plot(
                    [x_left + c_div * t3_col_w, x_left + c_div * t3_col_w],
                    [y0 + pad_bot + 0.0005, t3_top_y - 0.0005],
                    color="#CBD5E1", linewidth=0.55
                )

            for idx_3, kw in enumerate(bot_small[:12]):
                sr = idx_3 // 3
                sc = idx_3 % 3
                tx = x_left + sc * t3_col_w + 0.0011
                ty = t3_top_y - (sr + 0.5) * t3_row_h

                ax.text(
                    tx, ty,
                    kw,
                    fontsize=4.20 if len(kw) > 32 else 4.45,
                    fontweight="bold",
                    color=col["t3_txt"],
                    va="center", ha="left"
                )

    fig.savefig(OUT_DEV_PNG, dpi=300, facecolor=fig.get_facecolor())
    fig.savefig(OUT_FIG_PNG, dpi=300, facecolor=fig.get_facecolor())
    fig.savefig(OUT_DEV_PDF, format="pdf", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved: {OUT_DEV_PNG} ({OUT_DEV_PNG.stat().st_size:,} bytes)")
    print(f"Saved: {OUT_FIG_PNG} ({OUT_FIG_PNG.stat().st_size:,} bytes)")
    print(f"Saved: {OUT_DEV_PDF} ({OUT_DEV_PDF.stat().st_size:,} bytes)")


def render_mobile_agent_anatomy_chart():
    """
    Smartphone Portrait Mini Chart (9.5 x 20.0 in @ 300 DPI) for the 7-Layer Agent Stack.
    """
    plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]

    fig = plt.figure(figsize=(9.5, 20.0), dpi=300, facecolor="#0F172A")
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

    hdr_y = 0.922
    hdr_h = 0.075
    hdr_box = FancyBboxPatch(
        (0.005, hdr_y), 0.990, hdr_h,
        boxstyle="round,pad=0.0,rounding_size=0.006",
        facecolor="#0F172A", edgecolor="#1E293B", linewidth=1.6
    )
    ax.add_patch(hdr_box)

    ax.text(
        0.015, hdr_y + hdr_h * 0.79,
        "ANATOMY OF AI AGENTS 2026",
        fontsize=21.5, fontweight="bold", color="#FFFFFF", va="center", ha="left"
    )
    ax.text(
        0.985, hdr_y + hdr_h * 0.79,
        "www.arianprabowo.com",
        fontsize=10.5, fontweight="bold", color="#38BDF8", va="center", ha="right"
    )

    ax.plot(
        [0.014, 0.986], [hdr_y + hdr_h * 0.60, hdr_y + hdr_h * 0.60],
        color="#334155", linewidth=1.2
    )

    ax.text(
        0.014, hdr_y + hdr_h * 0.38,
        "What runs under an AI agent in 2026? A 7-layer OSI-style stack\n"
        "from GPU silicon (L1) & uv/PyTorch/JAX (L2) to Data/RAG (L3),\n"
        "Model Arch/RLVR (L4), MCP/Memory (L5), Harness² (L6) & Swarms (L7).",
        fontsize=6.7, fontweight="bold", color="#FEF08A", va="center", ha="left",
        linespacing=1.09
    )

    ax.plot(
        [0.515, 0.515], [hdr_y + hdr_h * 0.19, hdr_y + hdr_h * 0.56],
        color="#334155", linewidth=1.2
    )

    ax.text(
        0.525, hdr_y + hdr_h * 0.38,
        "① TRACE: Follow Layers 1 → 7 from silicon to swarms\n"
        "② BUILD: Top 3 pills = flagship primitives & frameworks\n"
        "③ HARDEN: Audit FAILURE MODES & TRAPS on the right",
        fontsize=6.6, fontweight="bold", color="#93C5FD", va="center", ha="left",
        linespacing=1.11
    )

    ax.text(
        0.500, hdr_y + hdr_h * 0.08,
        f"*Based on Roitman 'Hitchhiker's Guide to Agentic AI' (arXiv:2606.24937, June 2026) · Arian Prabowo · {LAST_UPDATED_STR}",
        fontsize=4.2, fontweight="bold", color="#94A3B8", va="center", ha="center"
    )

    col_hdr_y = 0.878
    col_hdr_h = 0.041

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
        "OSI LAYER",
        fontsize=11.8, fontweight="bold", color="#FFFFFF", va="center", ha="center"
    )
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.23,
        "PDU & Book Ch.",
        fontsize=6.0, fontweight="bold", color="#94A3B8", va="center", ha="center"
    )

    mobile_col_titles = {
        "primitives_arch": ("PRIMITIVES &\nARCHITECTURE", "Math · Topologies"),
        "frameworks_stack": ("FRAMEWORKS &\nPROTOCOLS", "Packages · SDKs"),
        "ops_evals_security": ("SCALING, EVALS\n& SECURITY", "Oracles · Sandboxes"),
        "failure_modes": ("FAILURE MODES\n& TRAPS", "What Breaks Here"),
    }

    for c_idx, col in enumerate(COLUMNS):
        cx, cw = col_geoms[c_idx]
        is_fail = col["key"] == "failure_modes"
        m_title, m_sub = mobile_col_titles[col["key"]]
        chdr = FancyBboxPatch(
            (cx, col_hdr_y), cw, col_hdr_h,
            boxstyle="round,pad=0.0,rounding_size=0.005",
            facecolor=col["hdr_bg"], edgecolor="#0F172A", linewidth=1.2
        )
        ax.add_patch(chdr)
        ax.text(
            cx + cw / 2, col_hdr_y + col_hdr_h * 0.64,
            m_title,
            fontsize=8.8 if not is_fail else 8.6,
            fontweight="bold", color="#FFFFFF", va="center", ha="center",
            linespacing=0.98
        )
        ax.text(
            cx + cw / 2, col_hdr_y + col_hdr_h * 0.16,
            m_sub,
            fontsize=5.3,
            fontweight="bold", color="#FEE2E2" if is_fail else "#E2E8F0", va="center", ha="center"
        )

    top_y = 0.873
    bot_y = 0.004
    n_layers = len(STACK_LAYERS)
    row_gap = 0.0036
    row_h = (top_y - bot_y - (n_layers - 1) * row_gap) / n_layers

    mobile_layer_names = {
        1: "PHYSICAL &\nSILICON",
        2: "ENV, PACKAGES,\nPYTHON & TENSOR",
        3: "DATA, TOKENS\n& RAG",
        4: "MODEL ARCH &\nREASONING RL",
        5: "CONTEXT, MEMORY,\nTOOLS & MCP",
        6: "AGENT HARNESS,\nLOOP & GRAPH",
        7: "MULTI-AGENT\nMESH & UI",
    }

    for r_idx, ly in enumerate(STACK_LAYERS):
        y0 = top_y - (r_idx + 1) * row_h - r_idx * row_gap

        lbox_body = FancyBboxPatch(
            (left_x0, y0), left_w, row_h,
            boxstyle="round,pad=0.0,rounding_size=0.005",
            facecolor="#0F172A", edgecolor="#334155", linewidth=1.5
        )
        ax.add_patch(lbox_body)

        inset_b = 0.0018
        banner_h = row_h * 0.340
        lbox_top = FancyBboxPatch(
            (left_x0 + inset_b, y0 + row_h - banner_h - inset_b),
            left_w - 2 * inset_b, banner_h,
            boxstyle="round,pad=0.0,rounding_size=0.004",
            facecolor="#1E293B", edgecolor=ly["accent"], linewidth=1.4
        )
        ax.add_patch(lbox_top)

        b_top_y = y0 + row_h - inset_b
        ax.text(
            left_x0 + 0.006, b_top_y - banner_h * 0.22,
            ly["badge"],
            fontsize=11.0, fontweight="bold", color="#FFFFFF", va="center", ha="left"
        )

        bar_total_w = 0.062
        bar_gap = 0.0014
        seg_w = (bar_total_w - 6 * bar_gap) / 7.0
        seg_h = banner_h * 0.15
        bar_x_start = left_x0 + left_w - 0.006 - bar_total_w
        bar_y = b_top_y - banner_h * 0.22 - seg_h / 2.0
        for b_i in range(7):
            bx_i = bar_x_start + b_i * (seg_w + bar_gap)
            is_lit = b_i < ly["layer"]
            seg_patch = FancyBboxPatch(
                (bx_i, bar_y), seg_w, seg_h,
                boxstyle="round,pad=0.0,rounding_size=0.001",
                facecolor=ly["accent"] if is_lit else "#334155",
                edgecolor=ly["accent"] if is_lit else "#475569",
                linewidth=0.5
            )
            ax.add_patch(seg_patch)

        ax.text(
            left_x0 + left_w / 2, b_top_y - banner_h * 0.72,
            mobile_layer_names[ly["layer"]],
            fontsize=7.8,
            fontweight="bold", color="#FEF08A", va="center", ha="center",
            linespacing=0.95
        )

        desc_wrapped = textwrap.fill(ly["desc"], width=24)
        osi_wrapped = textwrap.fill(f"• {ly['osi_map']}", width=24)
        ref_wrapped = textwrap.fill(f"• {ly['book_ref']}", width=24)

        body_top_y = y0 + (row_h - banner_h - inset_b) * 0.95
        ax.text(
            left_x0 + 0.005,
            body_top_y,
            desc_wrapped,
            fontsize=5.45,
            fontweight="bold",
            color="#F8FAFC",
            va="top",
            ha="left",
            linespacing=1.04,
        )

        n_desc_lines = desc_wrapped.count("\n") + 1
        bullet_body = f"{osi_wrapped}\n{ref_wrapped}"
        ax.text(
            left_x0 + 0.005,
            body_top_y - n_desc_lines * 0.0056 - 0.0015,
            bullet_body,
            fontsize=5.15,
            fontweight="bold",
            color="#93C5FD",
            va="top",
            ha="left",
            linespacing=1.03,
        )

        for c_idx, col in enumerate(COLUMNS):
            cx, cw = col_geoms[c_idx]
            is_fail = col["key"] == "failure_modes"

            cell_data = ly["cells"][col["key"]]
            top_h1 = cell_data["h1"]
            mid_norm = cell_data["normal"]

            cbox = FancyBboxPatch(
                (cx, y0), cw, row_h,
                boxstyle="round,pad=0.0,rounding_size=0.005",
                facecolor=col["cell_bg"],
                edgecolor=col["cell_edge"],
                linewidth=1.4 if not is_fail else 1.5,
                linestyle="--" if is_fail else "-"
            )
            ax.add_patch(cbox)

            pad_x = 0.0030
            pad_top = 0.0024
            pad_bot = 0.0020
            inner_w = cw - 2 * pad_x
            x_left = cx + pad_x

            gap_t1_t2 = 0.0018
            avail_h = row_h - pad_top - pad_bot - gap_t1_t2
            t1_h = avail_h * 0.54
            t2_h = avail_h * 0.46

            t1_top_y = y0 + row_h - pad_top
            pill_gap = 0.0016
            ph = (t1_h - 2 * pill_gap) / 3.0
            wrap_w_h1 = 23 if is_fail else 25
            for idx_1, kw in enumerate(top_h1[:3]):
                px = x_left
                pw = inner_w
                py = t1_top_y - (idx_1 + 1) * ph - idx_1 * pill_gap
                pill = FancyBboxPatch(
                    (px, py), pw, ph,
                    boxstyle="round,pad=0.0,rounding_size=0.003",
                    facecolor=col["h1_bg"],
                    edgecolor=col["pill_edge"],
                    linewidth=1.05,
                    linestyle="--" if is_fail else "-"
                )
                ax.add_patch(pill)

                kw_multiline = textwrap.fill(kw, width=wrap_w_h1)
                n_pill_lines = kw_multiline.count("\n") + 1
                pill_fs = 6.3 if n_pill_lines >= 3 else (7.0 if is_fail else 7.3)
                ax.text(
                    px + pw / 2, py + ph / 2,
                    kw_multiline,
                    fontsize=pill_fs,
                    fontweight="bold",
                    color=col["h1_txt"],
                    va="center", ha="center",
                    linespacing=0.96
                )

            div_y = t1_top_y - t1_h - gap_t1_t2 * 0.5
            ax.plot(
                [x_left + 0.001, x_left + inner_w - 0.001],
                [div_y, div_y],
                color="#FCA5A5" if is_fail else col["div_col"],
                linewidth=0.85,
                linestyle="--" if is_fail else "-"
            )

            t2_top_y = t1_top_y - t1_h - gap_t1_t2
            t2_row_h = t2_h / 4.0
            wrap_w_t2 = 25 if is_fail else 27

            for idx_2, kw in enumerate(mid_norm[:4]):
                if idx_2 % 2 == 1:
                    stripe = FancyBboxPatch(
                        (x_left + 0.0003, t2_top_y - (idx_2 + 1) * t2_row_h + 0.00012),
                        inner_w - 0.0006, t2_row_h - 0.00024,
                        boxstyle="round,pad=0.0,rounding_size=0.001",
                        facecolor="#FEE2E2" if is_fail else col["t2_bg"],
                        edgecolor="none",
                        alpha=0.60 if is_fail else 1.0
                    )
                    ax.add_patch(stripe)

                ty = t2_top_y - (idx_2 + 0.5) * t2_row_h
                kw_t2_multiline = textwrap.fill(kw, width=wrap_w_t2)
                ax.text(
                    x_left + 0.0020, ty,
                    kw_t2_multiline,
                    fontsize=5.95 if is_fail else 6.15,
                    fontweight="bold",
                    color=col["t2_txt"],
                    va="center", ha="left",
                    linespacing=0.96
                )

    fig.savefig(OUT_MOBILE_PNG, dpi=300, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved: {OUT_MOBILE_PNG} ({OUT_MOBILE_PNG.stat().st_size:,} bytes)")


def write_agent_anatomy_markdown():
    lines = [
        f"![Anatomy of AI Agents 2026 — 7-Layer OSI-Inspired Megachart]({OUT_DEV_PNG})",
        "",
        f"![Anatomy of AI Agents 2026 — Mobile Portrait Mini Chart]({OUT_MOBILE_PNG})",
        "",
        "# ANATOMY OF AI AGENTS 2026 (7-Layer OSI-Inspired Reference Stack)",
        "",
        "> **What actually runs under the hood of an autonomous AI agent in 2026? Like the 7-layer OSI networking model, modern agents are a deep vertical stack — from GPU silicon (`L1`) and `uv`/`conda`/`Docker` environments (`L2`) to `PyTorch`/`vLLM` serving (`L3`), `RLVR` reasoning weights (`L4`), `MCP`/`SKILL.md` & memory (`L5`), `Harness²` loop/graph control (`L6`), and `A2A` multi-agent meshes (`L7`).**  ",
        f"> **How to Read ([www.arianprabowo.com](https://www.arianprabowo.com) · Based on Haggai Roitman's *The Hitchhiker's Guide to Agentic AI*, `arXiv:2606.24937` · <sub>`{LAST_UPDATED_STR}`</sub>):** **`① TRACE THE STACK:`** Follow `Layers 1 → 7` from physical silicon to multi-agent swarms · **`② BUILD EACH LAYER:`** Target the **Top 3** pills in each pillar · **`③ HARDEN PROD:`** Audit the **`FAILURE MODES & TRAPS`** on the right.",
        "",
        "---",
        "",
        "## 1. Complete 7-Layer Stack Overview (`Layer 1` → `Layer 7` × `4` Pillars)",
        "",
        "| OSI Agent Layer (Analogy · PDU · Scope · Book Ref) | Core Primitives & Architecture | Frameworks, Packages & Protocols | Scaling, Verification & Security | Failure Modes & Traps |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]

    for ly in STACK_LAYERS:
        col0 = (
            f"**{ly['badge']} ({ly['meter']}): {ly['name']}**<br>"
            f"{ly['desc']}<br>"
            f"• **OSI & PDU:** {ly['osi_map']}<br>"
            f"• **Roitman Guide:** {ly['book_ref']}"
        )
        row_cells = [col0]
        for col in COLUMNS:
            d = ly["cells"][col["key"]]
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
        "## 2. Layer-by-Layer Architectural Breakdown (`Layer 1` → `Layer 7`)",
        "",
    ])

    for ly in STACK_LAYERS:
        lines.extend([
            f"### {ly['badge']} ({ly['meter']}) — {ly['name']}",
            "",
            f"{ly['desc']}",
            "",
            f"* **OSI Analogy & Protocol Data Unit (PDU):** `{ly['osi_map']}`",
            f"* **Primary Reference (`arXiv:2606.24937`):** {ly['book_ref']}",
            "",
            "| Architectural Pillar | Top 3 Flagship Checkpoints (`H1`) | Core Stack & Mechanisms (`Normal`) | Granular Specs, Flags & Formulas (`Footnote`) |",
            "| :--- | :--- | :--- | :--- |",
        ])
        for col in COLUMNS:
            d = ly["cells"][col["key"]]
            h1_s = ", ".join(f"**`{k}`**" for k in d["h1"]) if d["h1"] else "—"
            nm_s = ", ".join(f"`{k}`" for k in d["normal"]) if d["normal"] else "—"
            sm_s = ", ".join(f"*{k}*" for k in d["small"]) if d["small"] else "—"
            lines.append(f"| **{col['title']}** | {h1_s} | {nm_s} | {sm_s} |")
        lines.append("")

    content = "\n".join(lines)
    OUT_MD.write_text(content, encoding="utf-8")
    print(f"Saved: {OUT_MD} ({OUT_MD.stat().st_size:,} bytes)")


if __name__ == "__main__":
    render_desktop_agent_anatomy_megachart()
    render_mobile_agent_anatomy_chart()
    write_agent_anatomy_markdown()
