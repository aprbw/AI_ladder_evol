"""
ANATOMY OF AI AGENTS 2026 — 7-Layer AI Agent Stack Reference Model & Megachart
=============================================================================
Grounded in Haggai Roitman's "The Hitchhiker's Guide to Agentic AI: From Foundations to Systems"
(arXiv:2606.24937, v1.4, June 2026) and the 2026 production AI systems stack.

7 Agent Stack Layers (Left-to-Right Progression: Layer 1 Physical -> Layer 7 Multi-Agent):
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

ANATOMY_DIR = Path(__file__).resolve().parent
ANATOMY_DIR.mkdir(parents=True, exist_ok=True)

OUT_DEV_PNG = ANATOMY_DIR / "anatomy_of_AI_agents_2026.png"
OUT_DEV_PDF = ANATOMY_DIR / "anatomy_of_AI_agents_2026.pdf"
OUT_MOBILE_PNG = ANATOMY_DIR / "anatomy_of_AI_agents_2026_mobile.png"
OUT_MD = ANATOMY_DIR / "2026 11 07 anatomy_of_AI_agents_2026.md"

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
# 7 AGENT STACK LAYERS (LAYER 1 PHYSICAL -> LAYER 7 MULTI-AGENT)
# =============================================================================
STACK_LAYERS = [
    {
        "layer": 1,
        "badge": "LAYER 1",
        "meter": "L1/7",
        "name": "PHYSICAL & SILICON",
        "core_unit": "Core Unit: FLOPs, HBM Bytes & CUDA Warps",
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
        "core_unit": "Core Unit: Wheels, Lockfiles, Tensors & Paged KV",
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
        "core_unit": "Core Unit: Token IDs, Embeddings & Chunks",
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
        "core_unit": "Core Unit: Logits, LoRA Adapters & CoT Traces",
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
        "core_unit": "Core Unit: Context Windows & JSON-RPC Calls",
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
        "core_unit": "Core Unit: State Transitions, Actions & Diffs",
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
        "core_unit": "Core Unit: A2A Tasks, Worktrees & GenUI Streams",
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
    Landscape Widescreen Megachart (29.25 x 13.5 in @ 300 DPI — 19.5:9 Mobile-Landscape Aspect Ratio).
    The 7 Agent Stack Layers flow horizontally from LEFT to RIGHT (Columns 1..7),
    while the 4 Architectural Pillars form the horizontal rows (Rows 1..4).
    """
    plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]

    fig = plt.figure(figsize=(29.25, 13.5), dpi=300, facecolor="#0F172A")
    ax = fig.add_axes([0.003, 0.004, 0.994, 0.992])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    bg_canvas = FancyBboxPatch(
        (0.001, 0.001), 0.998, 0.998,
        boxstyle="round,pad=0.0,rounding_size=0.005",
        facecolor="#E2E8F0", edgecolor="#0F172A", linewidth=1.5
    )
    ax.add_patch(bg_canvas)

    # -------------------------------------------------------------------------
    # 1. Top Masthead (Title + Website + Yellow Hook + Blue How-to-Read + Footnote)
    # -------------------------------------------------------------------------
    hdr_y = 0.908
    hdr_h = 0.086
    hdr_box = FancyBboxPatch(
        (0.004, hdr_y), 0.992, hdr_h,
        boxstyle="round,pad=0.0,rounding_size=0.005",
        facecolor="#0F172A", edgecolor="#1E293B", linewidth=1.8
    )
    ax.add_patch(hdr_box)

    # Left Block: Giant Title + Website Underneath
    ax.text(
        0.012, hdr_y + hdr_h * 0.70,
        "ANATOMY OF AI AGENTS 2026",
        fontsize=31.5, fontweight="bold", color="#FFFFFF", va="center", ha="left"
    )
    ax.text(
        0.013, hdr_y + hdr_h * 0.35,
        "www.arianprabowo.com  ·  7-Layer AI Agent Stack Reference (Based on Roitman arXiv:2606.24937)",
        fontsize=11.2, fontweight="bold", color="#38BDF8", va="center", ha="left"
    )

    # Vertical divider 1
    ax.plot(
        [0.418, 0.418], [hdr_y + hdr_h * 0.24, hdr_y + hdr_h * 0.91],
        color="#334155", linewidth=1.4
    )

    # Middle Block: Yellow Motivating Hook
    ax.text(
        0.428, hdr_y + hdr_h * 0.58,
        "What actually runs under the hood of an autonomous AI agent in 2026?\n"
        "Modern AI agents form a 7-layer left-to-right stack — from GPU silicon (L1) &\n"
        "uv/PyTorch/JAX (L2) to Data/RAG (L3), Arch/RLVR (L4), MCP (L5), Harness² (L6) & A2A swarms (L7).",
        fontsize=9.6, fontweight="bold", color="#FEF08A", va="center", ha="left",
        linespacing=1.18
    )

    # Vertical divider 2
    ax.plot(
        [0.735, 0.735], [hdr_y + hdr_h * 0.24, hdr_y + hdr_h * 0.91],
        color="#334155", linewidth=1.4
    )

    # Right Block: Blue 3-Step Key
    ax.text(
        0.745, hdr_y + hdr_h * 0.58,
        "① TRACE LEFT → RIGHT: Follow Layers 1 → 7 from silicon to swarms\n"
        "② BUILD EACH LAYER: Top 3 pills = flagship 2026 primitives & tools\n"
        "③ HARDEN PROD: Audit the red FAILURE MODES & TRAPS row at bottom",
        fontsize=9.4, fontweight="bold", color="#93C5FD", va="center", ha="left",
        linespacing=1.22
    )

    # Horizontal divider above bottom footnote strip
    ax.plot(
        [0.010, 0.990], [hdr_y + hdr_h * 0.20, hdr_y + hdr_h * 0.20],
        color="#1E293B", linewidth=1.0
    )

    # Bottom Combined Grey Footnote Strip
    ax.text(
        0.500, hdr_y + hdr_h * 0.095,
        f"*Synthesized from Haggai Roitman's 'The Hitchhiker's Guide to Agentic AI: From Foundations to Systems' (arXiv:2606.24937, v1.4, June 2026) + 2026 systems tooling. "
        f"Companion to AI Skill Tree 2026 & AI Ladder Evolution by Arian Prabowo · {LAST_UPDATED_STR}",
        fontsize=6.8, fontweight="bold", color="#94A3B8", va="center", ha="center"
    )

    # -------------------------------------------------------------------------
    # 2. Horizontal Geometry (Left Pillar Column + 7 Agent Layer Columns Left->Right)
    # -------------------------------------------------------------------------
    left_x0 = 0.004
    left_w = 0.094
    col_gap = 0.0032
    active_x0 = left_x0 + left_w + col_gap
    n_layers = len(STACK_LAYERS)
    layer_col_w = (0.996 - active_x0 - (n_layers - 1) * col_gap) / n_layers

    col_hdr_y = 0.788
    col_hdr_h = 0.114

    # Top-Left Corner Card
    corner_box = FancyBboxPatch(
        (left_x0, col_hdr_y), left_w, col_hdr_h,
        boxstyle="round,pad=0.0,rounding_size=0.004",
        facecolor="#0F172A", edgecolor="#334155", linewidth=1.5
    )
    ax.add_patch(corner_box)
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.72,
        "AI AGENT STACK",
        fontsize=11.8, fontweight="bold", color="#FFFFFF", va="center", ha="center"
    )
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.45,
        "LAYER 1 → LAYER 7",
        fontsize=9.4, fontweight="bold", color="#FEF08A", va="center", ha="center"
    )
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.19,
        "Left-to-Right Pipeline\n× 4 Architectural Rows",
        fontsize=6.6, fontweight="bold", color="#94A3B8", va="center", ha="center",
        linespacing=1.12
    )

    # 7 Layer Column Headers (Left to Right: Layer 1 -> Layer 7)
    for l_idx, ly in enumerate(STACK_LAYERS):
        lx = active_x0 + l_idx * (layer_col_w + col_gap)

        lbox_body = FancyBboxPatch(
            (lx, col_hdr_y), layer_col_w, col_hdr_h,
            boxstyle="round,pad=0.0,rounding_size=0.004",
            facecolor="#0F172A", edgecolor="#334155", linewidth=1.5
        )
        ax.add_patch(lbox_body)

        inset_b = 0.0014
        banner_h = col_hdr_h * 0.39
        lbox_top = FancyBboxPatch(
            (lx + inset_b, col_hdr_y + col_hdr_h - banner_h - inset_b),
            layer_col_w - 2 * inset_b, banner_h,
            boxstyle="round,pad=0.0,rounding_size=0.003",
            facecolor="#1E293B", edgecolor=ly["accent"], linewidth=1.4
        )
        ax.add_patch(lbox_top)

        b_top_y = col_hdr_y + col_hdr_h - inset_b
        badge_label = f"{ly['badge']} →" if l_idx < n_layers - 1 else f"{ly['badge']} ★"
        ax.text(
            lx + 0.0045, b_top_y - banner_h * 0.33,
            badge_label,
            fontsize=12.4, fontweight="bold", color="#FFFFFF", va="center", ha="left"
        )

        # 7-segment progress bar on top-right of banner
        bar_total_w = 0.044
        bar_gap = 0.0010
        seg_w = (bar_total_w - 6 * bar_gap) / 7.0
        seg_h = banner_h * 0.22
        bar_x_start = lx + layer_col_w - 0.0045 - bar_total_w
        bar_y = b_top_y - banner_h * 0.33 - seg_h / 2.0
        for b_i in range(7):
            bx_i = bar_x_start + b_i * (seg_w + bar_gap)
            is_lit = b_i < ly["layer"]
            seg_patch = FancyBboxPatch(
                (bx_i, bar_y), seg_w, seg_h,
                boxstyle="round,pad=0.0,rounding_size=0.001",
                facecolor=ly["accent"] if is_lit else "#334155",
                edgecolor=ly["accent"] if is_lit else "#475569",
                linewidth=0.55
            )
            ax.add_patch(seg_patch)

        ax.text(
            lx + layer_col_w / 2, b_top_y - banner_h * 0.76,
            ly["name"],
            fontsize=8.0 if len(ly["name"]) >= 25 else 8.6,
            fontweight="bold", color="#FEF08A", va="center", ha="center"
        )

        desc_wrapped = textwrap.fill(ly["desc"], width=48)
        unit_line = f"• {ly['core_unit']}"
        ref_line = f"• Guide: {ly['book_ref']}"

        body_top_y = col_hdr_y + (col_hdr_h - banner_h - inset_b) * 0.93
        ax.text(
            lx + 0.0035,
            body_top_y,
            desc_wrapped,
            fontsize=5.45,
            fontweight="bold",
            color="#F8FAFC",
            va="top",
            ha="left",
            linespacing=1.05,
        )

        bullet_body = f"{unit_line}\n{ref_line}"
        ax.text(
            lx + 0.0035,
            col_hdr_y + 0.0040,
            bullet_body,
            fontsize=5.05,
            fontweight="bold",
            color="#93C5FD",
            va="bottom",
            ha="left",
            linespacing=1.08,
        )

    # -------------------------------------------------------------------------
    # 3. 4 Architectural Pillar Rows x 7 Layer Columns (Left to Right)
    # -------------------------------------------------------------------------
    top_y = 0.782
    active_row_h = 0.202
    fail_row_h = 0.152
    row_gap = 0.0040
    fail_sep_gap = 0.0080

    row_geoms = [
        (top_y - 1 * active_row_h - 0 * row_gap, active_row_h),
        (top_y - 2 * active_row_h - 1 * row_gap, active_row_h),
        (top_y - 3 * active_row_h - 2 * row_gap, active_row_h),
        (top_y - 3 * active_row_h - 2 * row_gap - fail_sep_gap - fail_row_h, fail_row_h),
    ]

    # Red dashed horizontal separator line above FAILURE MODES & TRAPS row
    sep_y = top_y - 3 * active_row_h - 2 * row_gap - fail_sep_gap * 0.5
    ax.plot(
        [left_x0, 0.996], [sep_y, sep_y],
        color="#DC2626", linewidth=1.8, linestyle=(0, (6, 3)), alpha=0.75
    )

    row_side_titles = {
        "primitives_arch": (
            "PILLAR 1",
            "CORE PRIMITIVES\n& ARCHITECTURE",
            "Hardware Physics,\nMathematical Ops,\nData Structures &\nControl Topologies",
            "• Layer 1–2: Silicon/Kernels\n• Layer 3–4: Data/Model Math\n• Layer 5–7: Memory/Loops/MAS",
        ),
        "frameworks_stack": (
            "PILLAR 2",
            "FRAMEWORKS, PKGS\n& PROTOCOLS",
            "CLI Package Managers,\nDL/Serving Frameworks,\nModel Checkpoints &\nAgent SDKs/Protocols",
            "• brew · uv · conda · pip · venv\n• PyTorch · JAX · vLLM · TRL\n• MCP · SKILL.md · LangGraph · A2A",
        ),
        "ops_evals_security": (
            "PILLAR 3",
            "SCALING, EVALS\n& SECURITY",
            "Throughput SLAs,\nMicroVM Sandboxes,\nVerification Oracles &\nZero-Trust Guardrails",
            "• MFU · E2B/bwrap · RAG Triad\n• RLVR Graders · MCP OAuth 2.1\n• SWE-bench · pass^k · KYA",
        ),
        "failure_modes": (
            "ANTI-PATTERNS",
            "FAILURE MODES\n& TRAPS",
            "What Breaks in Prod:\nBottlenecks, Collapses,\nInjections & Swarm\nEcho Chambers",
            "• OOM & CUDA ABI Hell\n• Model Collapse & Reward Hack\n• Context Rot & O(N²) Chatter",
        ),
    }

    for r_idx, col in enumerate(COLUMNS):
        ry, rh = row_geoms[r_idx]
        is_fail = col["key"] == "failure_modes"
        p_badge, p_title, p_desc, p_bullets = row_side_titles[col["key"]]

        # Left Row-Header Card
        rbox_body = FancyBboxPatch(
            (left_x0, ry), left_w, rh,
            boxstyle="round,pad=0.0,rounding_size=0.004",
            facecolor="#0F172A", edgecolor=col["cell_edge"], linewidth=1.5
        )
        ax.add_patch(rbox_body)

        inset_r = 0.0016
        rbanner_h = rh * (0.42 if is_fail else 0.36)
        rbox_top = FancyBboxPatch(
            (left_x0 + inset_r, ry + rh - rbanner_h - inset_r),
            left_w - 2 * inset_r, rbanner_h,
            boxstyle="round,pad=0.0,rounding_size=0.003",
            facecolor=col["hdr_bg"], edgecolor="#FFFFFF", linewidth=1.0
        )
        ax.add_patch(rbox_top)

        ax.text(
            left_x0 + left_w / 2, ry + rh - inset_r - rbanner_h * 0.24,
            p_badge,
            fontsize=8.0, fontweight="bold", color="#FEF08A", va="center", ha="center"
        )
        ax.text(
            left_x0 + left_w / 2, ry + rh - inset_r - rbanner_h * 0.67,
            p_title,
            fontsize=8.8 if not is_fail else 8.6,
            fontweight="bold", color="#FFFFFF", va="center", ha="center",
            linespacing=1.02
        )

        body_avail_h = rh - rbanner_h - inset_r
        ax.text(
            left_x0 + left_w / 2,
            ry + body_avail_h * 0.66,
            p_desc,
            fontsize=6.8 if not is_fail else 6.4,
            fontweight="bold",
            color="#F8FAFC",
            va="center",
            ha="center",
            linespacing=1.10,
        )
        ax.text(
            left_x0 + 0.0035,
            ry + 0.006,
            p_bullets,
            fontsize=5.65 if not is_fail else 5.45,
            fontweight="bold",
            color="#FCA5A5" if is_fail else "#93C5FD",
            va="bottom",
            ha="left",
            linespacing=1.10,
        )

        # 7 Layer Cells across this Row (Left to Right)
        for l_idx, ly in enumerate(STACK_LAYERS):
            cx = active_x0 + l_idx * (layer_col_w + col_gap)
            cw = layer_col_w

            cell_data = ly["cells"][col["key"]]
            top_h1 = cell_data["h1"]
            mid_norm = cell_data["normal"]
            bot_small = cell_data["small"]

            cbox = FancyBboxPatch(
                (cx, ry), cw, rh,
                boxstyle="round,pad=0.0,rounding_size=0.004",
                facecolor=col["cell_bg"],
                edgecolor=col["cell_edge"],
                linewidth=1.5 if not is_fail else 1.6,
                linestyle="--" if is_fail else "-"
            )
            ax.add_patch(cbox)

            pad_x = 0.0022
            pad_top = 0.0028
            pad_bot = 0.0024
            inner_w = cw - 2 * pad_x
            x_left = cx + pad_x

            # =================================================================
            # CASE A: Failure Modes Row (Top 3 H1 Pills + 4x1 Tier 2 + 4x1 Tier 3)
            # =================================================================
            if is_fail:
                gap_t1_t2 = 0.0020
                gap_t2_t3 = 0.0016
                avail_h = rh - pad_top - pad_bot - gap_t1_t2 - gap_t2_t3
                t1_h = avail_h * 0.410
                t2_h = avail_h * 0.340
                t3_h = avail_h * 0.250

                t1_top_y = ry + rh - pad_top
                pill_gap = 0.0016
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
                        linewidth=1.05,
                        linestyle="--"
                    )
                    ax.add_patch(pill)
                    ax.text(
                        px + pw / 2, py + ph / 2,
                        kw,
                        fontsize=7.9 if len(kw) > 34 else 8.3,
                        fontweight="bold",
                        color=col["h1_txt"],
                        va="center", ha="center"
                    )

                # Tier 2: 4 single-column rows
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
                    tx = x_left + 0.0020
                    ty = t2_top_y - (sr + 0.5) * t2_row_h
                    ax.text(
                        tx, ty,
                        f"▸ {kw}",
                        fontsize=6.15,
                        fontweight="bold",
                        color=col["t2_txt"],
                        va="center", ha="left"
                    )

                # Tier 3: Bottom 4 in 2x2 grid inside bottom band
                t3_top_y = t2_top_y - t2_h - gap_t2_t3
                t3_row_h = t3_h / 2.0
                t3_col_w = inner_w / 2.0

                t3_band = FancyBboxPatch(
                    (x_left, ry + pad_bot),
                    inner_w, t3_h,
                    boxstyle="round,pad=0.0,rounding_size=0.0018",
                    facecolor="#FFF1F2",
                    edgecolor="#FCA5A5",
                    linewidth=0.6
                )
                ax.add_patch(t3_band)

                ax.plot(
                    [x_left + t3_col_w, x_left + t3_col_w],
                    [ry + pad_bot + 0.0006, t3_top_y - 0.0006],
                    color="#FCA5A5", linewidth=0.55
                )

                for idx_3, kw in enumerate(mid_norm[4:8]):
                    sr = idx_3 // 2
                    sc = idx_3 % 2
                    tx = x_left + sc * t3_col_w + 0.0012
                    ty = t3_top_y - (sr + 0.5) * t3_row_h
                    fs_fail_t3 = 4.10 if len(kw) > 36 else (4.40 if len(kw) > 31 else 4.65)
                    ax.text(
                        tx, ty,
                        kw,
                        fontsize=fs_fail_t3,
                        fontweight="bold",
                        color="#991B1B",
                        va="center", ha="left"
                    )
                continue

            # =================================================================
            # CASE B: Full 3-Tier Active Architectural Cell
            # =================================================================
            gap_t1_t2 = 0.0022
            gap_t2_t3 = 0.0018
            avail_h = rh - pad_top - pad_bot - gap_t1_t2 - gap_t2_t3
            t1_h = avail_h * 0.380
            t2_h = avail_h * 0.365
            t3_h = avail_h * 0.255

            # --- TIER 1: Top 3 H1 Pills ---
            t1_top_y = ry + rh - pad_top
            pill_gap = 0.0018
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
                    linewidth=1.10
                )
                ax.add_patch(pill)

                ax.text(
                    px + pw / 2, py + ph / 2,
                    kw,
                    fontsize=8.2 if len(kw) > 36 else 8.7,
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
                [t2_top_y - t2_h + 0.0006, t2_top_y - 0.0006],
                color="#CBD5E1", linewidth=0.75
            )

            for idx_2, kw in enumerate(mid_norm[:8]):
                sr = idx_2 // 2
                sc = idx_2 % 2
                if sc == 0 and sr % 2 == 1:
                    stripe = FancyBboxPatch(
                        (x_left, t2_top_y - (sr + 1) * t2_row_h + 0.00015),
                        inner_w, t2_row_h - 0.00030,
                        boxstyle="round,pad=0.0,rounding_size=0.001",
                        facecolor=col["t2_bg"], edgecolor="none"
                    )
                    ax.add_patch(stripe)

                tx = x_left + sc * t2_col_w + 0.0011
                ty = t2_top_y - (sr + 0.5) * t2_row_h
                fs_t2 = 4.15 if len(kw) > 37 else (4.45 if len(kw) > 33 else (4.75 if len(kw) > 29 else 5.05))
                ax.text(
                    tx, ty,
                    kw,
                    fontsize=fs_t2,
                    fontweight="bold",
                    color=col["t2_txt"],
                    va="center", ha="left"
                )

            # --- TIER 3: Bottom 12 in 3 Columns x 4 Rows ---
            t3_top_y = t2_top_y - t2_h - gap_t2_t3
            t3_row_h = t3_h / 4.0
            t3_col_w = inner_w / 3.0

            t3_band = FancyBboxPatch(
                (x_left, ry + pad_bot),
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
                    [ry + pad_bot + 0.0006, t3_top_y - 0.0006],
                    color="#CBD5E1", linewidth=0.50
                )

            for idx_3, kw in enumerate(bot_small[:12]):
                sr = idx_3 // 3
                sc = idx_3 % 3
                tx = x_left + sc * t3_col_w + 0.0008
                ty = t3_top_y - (sr + 0.5) * t3_row_h
                fs_t3 = 2.65 if len(kw) > 36 else (2.85 if len(kw) > 31 else (3.10 if len(kw) > 26 else 3.40))

                ax.text(
                    tx, ty,
                    kw,
                    fontsize=fs_t3,
                    fontweight="bold",
                    color=col["t3_txt"],
                    va="center", ha="left"
                )

    fig.savefig(OUT_DEV_PNG, dpi=300, facecolor=fig.get_facecolor())
    fig.savefig(OUT_DEV_PDF, format="pdf", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved: {OUT_DEV_PNG} ({OUT_DEV_PNG.stat().st_size:,} bytes)")
    print(f"Saved: {OUT_DEV_PDF} ({OUT_DEV_PDF.stat().st_size:,} bytes)")


def render_mobile_agent_anatomy_chart():
    """
    Smartphone Landscape Mini Chart (19.5 x 9.0 in @ 300 DPI — 19.5:9 Mobile Landscape)
    flowing from LEFT to RIGHT (Layers 1 -> 7) with simplified 2-tier cells for mobile screens.
    """
    plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]

    fig = plt.figure(figsize=(19.5, 9.0), dpi=300, facecolor="#0F172A")
    ax = fig.add_axes([0.003, 0.004, 0.994, 0.992])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    bg_canvas = FancyBboxPatch(
        (0.001, 0.001), 0.998, 0.998,
        boxstyle="round,pad=0.0,rounding_size=0.005",
        facecolor="#E2E8F0", edgecolor="#0F172A", linewidth=1.2
    )
    ax.add_patch(bg_canvas)

    hdr_y = 0.908
    hdr_h = 0.086
    hdr_box = FancyBboxPatch(
        (0.004, hdr_y), 0.992, hdr_h,
        boxstyle="round,pad=0.0,rounding_size=0.005",
        facecolor="#0F172A", edgecolor="#1E293B", linewidth=1.5
    )
    ax.add_patch(hdr_box)

    ax.text(
        0.012, hdr_y + hdr_h * 0.70,
        "ANATOMY OF AI AGENTS 2026",
        fontsize=21.0, fontweight="bold", color="#FFFFFF", va="center", ha="left"
    )
    ax.text(
        0.013, hdr_y + hdr_h * 0.35,
        "www.arianprabowo.com  ·  7-Layer AI Agent Stack (Roitman arXiv:2606.24937)",
        fontsize=7.6, fontweight="bold", color="#38BDF8", va="center", ha="left"
    )

    ax.plot(
        [0.418, 0.418], [hdr_y + hdr_h * 0.24, hdr_y + hdr_h * 0.91],
        color="#334155", linewidth=1.2
    )

    ax.text(
        0.428, hdr_y + hdr_h * 0.58,
        "What runs under an AI agent in 2026? A 7-layer left-to-right stack:\n"
        "GPU silicon (L1) → uv/PyTorch/JAX (L2) → Data/RAG (L3) →\n"
        "Arch/RLVR (L4) → MCP/Memory (L5) → Harness² (L6) → Swarms (L7).",
        fontsize=6.5, fontweight="bold", color="#FEF08A", va="center", ha="left",
        linespacing=1.15
    )

    ax.plot(
        [0.735, 0.735], [hdr_y + hdr_h * 0.24, hdr_y + hdr_h * 0.91],
        color="#334155", linewidth=1.2
    )

    ax.text(
        0.745, hdr_y + hdr_h * 0.58,
        "① TRACE LEFT → RIGHT: Follow Layers 1 → 7 across columns\n"
        "② BUILD: Top 3 pills = flagship primitives & frameworks\n"
        "③ HARDEN: Audit FAILURE MODES & TRAPS on bottom row",
        fontsize=6.3, fontweight="bold", color="#93C5FD", va="center", ha="left",
        linespacing=1.18
    )

    ax.plot(
        [0.010, 0.990], [hdr_y + hdr_h * 0.20, hdr_y + hdr_h * 0.20],
        color="#1E293B", linewidth=0.9
    )

    ax.text(
        0.500, hdr_y + hdr_h * 0.095,
        f"*Based on Roitman 'The Hitchhiker's Guide to Agentic AI' (arXiv:2606.24937, June 2026) · Arian Prabowo · {LAST_UPDATED_STR}",
        fontsize=4.6, fontweight="bold", color="#94A3B8", va="center", ha="center"
    )

    left_x0 = 0.004
    left_w = 0.090
    col_gap = 0.0032
    active_x0 = left_x0 + left_w + col_gap
    n_layers = len(STACK_LAYERS)
    layer_col_w = (0.996 - active_x0 - (n_layers - 1) * col_gap) / n_layers

    col_hdr_y = 0.802
    col_hdr_h = 0.100

    corner_box = FancyBboxPatch(
        (left_x0, col_hdr_y), left_w, col_hdr_h,
        boxstyle="round,pad=0.0,rounding_size=0.004",
        facecolor="#0F172A", edgecolor="#334155", linewidth=1.3
    )
    ax.add_patch(corner_box)
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.68,
        "AGENT STACK",
        fontsize=8.6, fontweight="bold", color="#FFFFFF", va="center", ha="center"
    )
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.32,
        "L1 → L7\n(Left to Right)",
        fontsize=6.2, fontweight="bold", color="#FEF08A", va="center", ha="center",
        linespacing=1.08
    )

    for l_idx, ly in enumerate(STACK_LAYERS):
        lx = active_x0 + l_idx * (layer_col_w + col_gap)

        lbox_body = FancyBboxPatch(
            (lx, col_hdr_y), layer_col_w, col_hdr_h,
            boxstyle="round,pad=0.0,rounding_size=0.004",
            facecolor="#0F172A", edgecolor="#334155", linewidth=1.3
        )
        ax.add_patch(lbox_body)

        inset_b = 0.0014
        banner_h = col_hdr_h * 0.48
        lbox_top = FancyBboxPatch(
            (lx + inset_b, col_hdr_y + col_hdr_h - banner_h - inset_b),
            layer_col_w - 2 * inset_b, banner_h,
            boxstyle="round,pad=0.0,rounding_size=0.003",
            facecolor="#1E293B", edgecolor=ly["accent"], linewidth=1.2
        )
        ax.add_patch(lbox_top)

        b_top_y = col_hdr_y + col_hdr_h - inset_b
        badge_label = f"{ly['badge']} →" if l_idx < n_layers - 1 else f"{ly['badge']} ★"
        ax.text(
            lx + 0.004, b_top_y - banner_h * 0.33,
            badge_label,
            fontsize=8.6, fontweight="bold", color="#FFFFFF", va="center", ha="left"
        )

        bar_total_w = 0.042
        bar_gap = 0.0010
        seg_w = (bar_total_w - 6 * bar_gap) / 7.0
        seg_h = banner_h * 0.22
        bar_x_start = lx + layer_col_w - 0.004 - bar_total_w
        bar_y = b_top_y - banner_h * 0.33 - seg_h / 2.0
        for b_i in range(7):
            bx_i = bar_x_start + b_i * (seg_w + bar_gap)
            is_lit = b_i < ly["layer"]
            seg_patch = FancyBboxPatch(
                (bx_i, bar_y), seg_w, seg_h,
                boxstyle="round,pad=0.0,rounding_size=0.001",
                facecolor=ly["accent"] if is_lit else "#334155",
                edgecolor=ly["accent"] if is_lit else "#475569",
                linewidth=0.45
            )
            ax.add_patch(seg_patch)

        ax.text(
            lx + layer_col_w / 2, b_top_y - banner_h * 0.77,
            ly["name"],
            fontsize=5.5 if len(ly["name"]) >= 25 else 5.9,
            fontweight="bold", color="#FEF08A", va="center", ha="center"
        )

        unit_short = textwrap.fill(f"{ly['core_unit']} · {ly['book_ref']}", width=38)
        ax.text(
            lx + 0.0035,
            col_hdr_y + (col_hdr_h - banner_h) * 0.50,
            unit_short,
            fontsize=4.4,
            fontweight="bold",
            color="#93C5FD",
            va="center",
            ha="left",
            linespacing=1.08,
        )

    top_y = 0.796
    active_row_h = 0.205
    fail_row_h = 0.160
    row_gap = 0.0040
    fail_sep_gap = 0.0070

    row_geoms = [
        (top_y - 1 * active_row_h - 0 * row_gap, active_row_h),
        (top_y - 2 * active_row_h - 1 * row_gap, active_row_h),
        (top_y - 3 * active_row_h - 2 * row_gap, active_row_h),
        (top_y - 3 * active_row_h - 2 * row_gap - fail_sep_gap - fail_row_h, fail_row_h),
    ]

    sep_y = top_y - 3 * active_row_h - 2 * row_gap - fail_sep_gap * 0.5
    ax.plot(
        [left_x0, 0.996], [sep_y, sep_y],
        color="#DC2626", linewidth=1.4, linestyle=(0, (5, 3)), alpha=0.75
    )

    mobile_row_titles = {
        "primitives_arch": ("PRIMITIVES &\nARCHITECTURE", "Math · Topologies"),
        "frameworks_stack": ("FRAMEWORKS &\nPROTOCOLS", "Packages · SDKs"),
        "ops_evals_security": ("SCALING, EVALS\n& SECURITY", "Oracles · Sandboxes"),
        "failure_modes": ("FAILURE MODES\n& TRAPS", "What Breaks Here"),
    }

    for r_idx, col in enumerate(COLUMNS):
        ry, rh = row_geoms[r_idx]
        is_fail = col["key"] == "failure_modes"
        m_title, m_sub = mobile_row_titles[col["key"]]

        rbox = FancyBboxPatch(
            (left_x0, ry), left_w, rh,
            boxstyle="round,pad=0.0,rounding_size=0.004",
            facecolor=col["hdr_bg"], edgecolor="#0F172A", linewidth=1.3
        )
        ax.add_patch(rbox)
        ax.text(
            left_x0 + left_w / 2, ry + rh * 0.60,
            m_title,
            fontsize=6.5,
            fontweight="bold", color="#FFFFFF", va="center", ha="center",
            linespacing=1.05
        )
        ax.text(
            left_x0 + left_w / 2, ry + rh * 0.25,
            m_sub,
            fontsize=4.8,
            fontweight="bold", color="#FEE2E2" if is_fail else "#E2E8F0", va="center", ha="center"
        )

        for l_idx, ly in enumerate(STACK_LAYERS):
            cx = active_x0 + l_idx * (layer_col_w + col_gap)
            cw = layer_col_w

            cell_data = ly["cells"][col["key"]]
            top_h1 = cell_data["h1"]
            mid_norm = cell_data["normal"]

            cbox = FancyBboxPatch(
                (cx, ry), cw, rh,
                boxstyle="round,pad=0.0,rounding_size=0.004",
                facecolor=col["cell_bg"],
                edgecolor=col["cell_edge"],
                linewidth=1.3 if not is_fail else 1.4,
                linestyle="--" if is_fail else "-"
            )
            ax.add_patch(cbox)

            pad_x = 0.0022
            pad_top = 0.0028
            pad_bot = 0.0024
            inner_w = cw - 2 * pad_x
            x_left = cx + pad_x

            gap_t1_t2 = 0.0020
            avail_h = rh - pad_top - pad_bot - gap_t1_t2
            t1_h = avail_h * 0.54
            t2_h = avail_h * 0.46

            t1_top_y = ry + rh - pad_top
            pill_gap = 0.0018
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
                    linewidth=0.95,
                    linestyle="--" if is_fail else "-"
                )
                ax.add_patch(pill)

                ax.text(
                    px + pw / 2, py + ph / 2,
                    kw,
                    fontsize=5.3 if len(kw) > 35 else 5.6,
                    fontweight="bold",
                    color=col["h1_txt"],
                    va="center", ha="center"
                )

            t2_top_y = t1_top_y - t1_h - gap_t1_t2
            t2_row_h = t2_h / 4.0

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
                ax.text(
                    x_left + 0.0018, ty,
                    f"• {kw}",
                    fontsize=4.55,
                    fontweight="bold",
                    color=col["t2_txt"],
                    va="center", ha="left"
                )

    fig.savefig(OUT_MOBILE_PNG, dpi=300, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved: {OUT_MOBILE_PNG} ({OUT_MOBILE_PNG.stat().st_size:,} bytes)")


def write_agent_anatomy_markdown():
    lines = [
        f"![Anatomy of AI Agents 2026 — 7-Layer AI Agent Stack Megachart]({OUT_DEV_PNG.name})",
        "",
        f"![Anatomy of AI Agents 2026 — Mobile Landscape Mini Chart]({OUT_MOBILE_PNG.name})",
        "",
        "# ANATOMY OF AI AGENTS 2026 (7-Layer AI Agent Reference Stack)",
        "",
        "> **What actually runs under the hood of an autonomous AI agent in 2026? Modern AI agents form a 7-layer left-to-right stack — from GPU silicon (`L1`) and `Homebrew`/`uv`/`conda`/`PyTorch`/`JAX` (`L2`) to Data/Tokenization/RAG (`L3`), Model Architecture & `RLVR` (`L4`), `MCP`/`SKILL.md` & Memory (`L5`), `Harness²` Loop/Graph Control (`L6`), and `A2A` Multi-Agent Swarms (`L7`).**  ",
        f"> **How to Read ([www.arianprabowo.com](https://www.arianprabowo.com) · Based on Haggai Roitman's *The Hitchhiker's Guide to Agentic AI*, `arXiv:2606.24937` · <sub>`{LAST_UPDATED_STR}`</sub>):** **`① TRACE LEFT → RIGHT:`** Follow `Layers 1 → 7` from physical silicon to multi-agent swarms · **`② BUILD EACH LAYER:`** Target the **Top 3** pills in each pillar · **`③ HARDEN PROD:`** Audit the **`FAILURE MODES & TRAPS`** row at the bottom.",
        "",
        "---",
        "",
        "## 1. Complete 7-Layer Stack Overview (`Layer 1` → `Layer 7` × `4` Pillars)",
        "",
        "| AI Agent Layer (Scope · Core Unit · Book Ref) | Core Primitives & Architecture | Frameworks, Packages & Protocols | Scaling, Verification & Security | Failure Modes & Traps |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]

    for ly in STACK_LAYERS:
        col0 = (
            f"**{ly['badge']} ({ly['meter']}): {ly['name']}**<br>"
            f"{ly['desc']}<br>"
            f"• **{ly['core_unit']}**<br>"
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
            f"* **Core Unit of Compute / State:** `{ly['core_unit']}`",
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
