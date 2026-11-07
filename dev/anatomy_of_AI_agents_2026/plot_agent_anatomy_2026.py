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
# 10 CORE AGENT STACK LAYERS (L1 -> L10) + 1 DETACHED ORGANISM (RAG & MULTIMODAL)
# =============================================================================
STACK_LAYERS = [
    {
        "layer": 1,
        "badge": "LAYER 1",
        "meter": "L1/10",
        "name": "PHYSICAL & SILICON",
        "core_unit": "Core Unit: FLOPs, HBM Bytes & CUDA Warps",
        "desc": "GPUs/TPUs/NPUs, HBM3e vs. SRAM hierarchy, CUDA/Triton kernels, and NVLink/InfiniBand fabrics.",
        "book_ref": "Ch. 1.6, 2.1, 11.10–14, 30.5 (GPUs & Kernels).",
        "accent": "#10B981",
        "is_external_organism": False,
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
        "meter": "L2/10",
        "name": "ENV, PACKAGES, PYTHON & TENSOR",
        "core_unit": "Core Unit: Wheels, Lockfiles, Tensors & Paged KV",
        "desc": "Package managers (`Homebrew`, `uv`, `conda`, `pip`, `venv`), `Python`, `PyTorch`, `JAX`, `vLLM`, and sandboxes.",
        "book_ref": "Ch. 1.14–15, 11.1–9, 21.5, 22.1–9 (Env & Runtime).",
        "accent": "#0EA5E9",
        "is_external_organism": False,
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
                    "Disaggregated Prefill-Decode Serving",
                    "Constrained Grammar / FSM Masking",
                ],
                "small": [
                    "pyproject.toml (PEP 517 / 621)",
                    "Content-Addressable Global Cache",
                    "Hardlink / Reflink Env Cloning",
                    "LD_LIBRARY_PATH / DYLD RPATH",
                    "torch.compile (TorchInductor/Dynamo)",
                    "JAX jit / vmap / pmap / shard_map",
                    "XLA HLO Graph Fusion & CUDA Graphs",
                    "Chunked Prefill Scheduling",
                    "KV-Cache FP8 / INT4 Quantization",
                    "Container UnionFS / OverlayFS Layers",
                    "Hardware Virtualization (KVM / HVF)",
                    "IPC Shared Memory (/dev/shm)",
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
        "meter": "L3/10",
        "name": "DATA & TOKENIZATION",
        "core_unit": "Core Unit: Corpora, Subword Tokens & Shards",
        "desc": "Pre-training/post-training corpora, BPE/Tiktoken tokenizers, deduplication, filtering, and synthetic data.",
        "book_ref": "Ch. 1.2, 3.2–3.5, 4.3, 6.2, 30.2 (Data & Tokenizers).",
        "accent": "#3B82F6",
        "is_external_organism": False,
        "cells": {
            "primitives_arch": {
                "h1": [
                    "Web, Code & Math Corpus Curation",
                    "Byte-Level BPE & Unigram Tokenizers",
                    "MinHash Dedup & Quality Filtering",
                ],
                "normal": [
                    "Byte-Level BPE / SentencePiece / Tiktoken",
                    "Pre-Tokenization Regex Split Rules",
                    "Vocabulary Size Scaling (32K–256K)",
                    "MinHash LSH & Suffix-Array Dedup",
                    "Heuristic & FastText Quality Classifiers",
                    "Domain & Curriculum Mixture Weights",
                    "Synthetic Reasoning & Trajectory Gen",
                    "Execution-Verified Code & Math Traces",
                ],
                "small": [
                    "Tokenizer Fertility (Tokens/Word)",
                    "Byte-Fallback for Unknown UTF-8",
                    "ChatML Special Control Tokens",
                    "Fill-in-the-Middle (FIM) Code Formatting",
                    "AST-Parsed Repository Level Ordering",
                    "KenLM Perplexity Outlier Filtering",
                    "Exact Substring 50-Token Dedup",
                    "Back-Translation & Persona Diversity",
                    "Evol-Instruct Complexity Mutation",
                    "Compile/Test Sandbox Filtering",
                    "Annealing Data Mix (High-Quality End)",
                    "Zero-Copy Memory-Mapped Shards",
                ],
            },
            "frameworks_stack": {
                "h1": [
                    "HF Datasets · Datatrove · NeMo Curator",
                    "Tiktoken · SentencePiece · HF Tokenizers",
                    "FineWeb-Edu · Dolma · The Stack v2",
                ],
                "normal": [
                    "HuggingFace Datasets & Hub Streaming",
                    "Datatrove & NeMo Curator Pipelines",
                    "Tiktoken & HuggingFace Rust Tokenizers",
                    "FineWeb-Edu · Dolma · RedPajama-v2",
                    "The Stack v2 & StarCoderData (Code)",
                    "OpenMathReasoning & NuminaMath",
                    "Apache Arrow · Parquet · WebDataset",
                    "Distilabel & Curator Synthetic Suites",
                ],
                "small": [
                    "Polars · DuckDB · PyArrow In-Memory ETL",
                    "Ray Data Distributed Streaming Ingest",
                    "MosaicML StreamingDataset (MDS)",
                    "Megatron-LM IndexedDataset (.bin/.idx)",
                    "SWE-Gym & SWE-smith Issue Trajectories",
                    "OpenThoughts & Bespoke-Stratos Sets",
                    "CommonCrawl WARC / WET Extraction",
                    "Trafilatura & Resiliparse HTML Clean",
                    "Tree-sitter AST Code Filtering",
                    "DVC & LakeFS Data Version Control",
                    "Cleanlab Automated Label Auditing",
                    "Argilla Human-in-the-Loop Curation",
                ],
            },
            "ops_evals_security": {
                "h1": [
                    "Benchmark Decontamination (N-Gram)",
                    "PII, Secret & License Scrubbing",
                    "Synthetic Data Diversity & Entropy",
                ],
                "normal": [
                    "13-Gram & Embedding Decontamination",
                    "Canary String Injection & Filtering",
                    "Regex + Presidio PII Scrubbing",
                    "TruffleHog / Gitleaks Key Removal",
                    "SPDX Open-Source License Verification",
                    "LLM-as-a-Judge Data Quality Scoring",
                    "Vendi Score & N-Gram Diversity Audits",
                    "Tokenizer Compression Ratio Audits",
                ],
                "small": [
                    "MMLU / GSM8K / HumanEval Overlap Scan",
                    "SWE-bench Repo Commit-Date Cutoff",
                    "Opt-Out & robots.txt Compliance",
                    "Copyright & Verbatim Memorization Check",
                    "Multilingual Token Fairness Audit",
                    "Toxic & CSAM Safety Classifier Filter",
                    "Poisoned Backdoor Trigger Scanning",
                    "Synthetic Mode-Collapse Entropy Check",
                    "Data Provenance & Lineage Ledgers",
                    "Differential Privacy (DP) Scrubbing",
                    "Dataset Card & Croissant Metadata",
                    "Deterministic Shard Shuffle Seeding",
                ],
            },
            "failure_modes": {
                "h1": [
                    "Garbage-In Synthetic Model Collapse",
                    "Test-Set Contamination Mirage",
                    "Tokenizer Glitch & Fertility Bloat",
                ],
                "normal": [
                    "Recursive Synthetic Training Collapse",
                    "Benchmark Leakage Inflating SOTA",
                    "PII & API Keys Baked Into Weights",
                    "Unbalanced Domain Mix Starving Code",
                    "Tokenizer Glitch Tokens (SolidGoldMagikarp)",
                    "3–5x Token Bloat on Non-English/Code",
                    "Duplicate Boilerplate Overfitting",
                    "Broken UTF-8 / HTML Artifacts in Text",
                    "Future-Timestamp Leakage in Backtests",
                    "Unverified Synthetic Hallucinations",
                ],
                "small": [],
            },
        },
    },
    {
        "layer": 4,
        "badge": "LAYER 4",
        "meter": "L4/10",
        "name": "ARCHITECTURE & PRE-TRAINING",
        "core_unit": "Core Unit: Transformer Blocks, MoE & Base Weights",
        "desc": "Transformer/MoE/hybrid architectures (`GQA`, `MLA`, `Mamba/DeltaNet`), next-token pre-training, and scaling laws.",
        "book_ref": "Ch. 1, 2.2, 11.1–8, 30.1 (Architecture & Pre-Training).",
        "accent": "#6366F1",
        "is_external_organism": False,
        "cells": {
            "primitives_arch": {
                "h1": [
                    "Transformer · Sparse MoE · GQA / MLA",
                    "Hybrid Linear Attention (Mamba/DeltaNet)",
                    "Next-Token Cross-Entropy & Scaling Laws",
                ],
                "normal": [
                    "Pre-Norm RMSNorm & SwiGLU FFN",
                    "Grouped-Query (GQA) & Latent (MLA)",
                    "Sparse MoE Top-K & Shared Experts",
                    "Gated DeltaNet / Mamba-2 SSM Hybrid",
                    "RoPE & YaRN Context Extension (1M+)",
                    "Autoregressive Next-Token Objective",
                    "Chinchilla Compute-Optimal Scaling",
                    "3D Parallelism (DP / TP / PP / SP / EP)",
                ],
                "small": [
                    "Multi-Head Latent Attention (KV Compress)",
                    "Aux-Loss-Free MoE Load Balancing",
                    "Multi-Token Prediction (MTP) Heads",
                    "Sliding Window & Ring Attention",
                    "AdamW vs. Muon Matrix Orthogonal",
                    "WSD (Warmup-Stable-Decay) LR Schedule",
                    "ZeRO Stage 1/2/3 & FSDP2 Sharding",
                    "1F1B & Interleaved Pipeline Schedule",
                    "FP8 Mixed-Precision Pre-Training",
                    "muP (Maximal Update Parametrization)",
                    "QK-Norm Attention Logit Stabilization",
                    "BitNet b1.58 Native Ternary Architecture",
                ],
            },
            "frameworks_stack": {
                "h1": [
                    "Megatron-LM · DeepSpeed · TorchTitan",
                    "Llama 4 · Qwen 3 · DeepSeek-V3 Base",
                    "HuggingFace Transformers · OLMo 2",
                ],
                "normal": [
                    "NVIDIA Megatron-Core & NeMo Framework",
                    "PyTorch TorchTitan & FSDP2 Native",
                    "DeepSpeed ZeRO-3 & Megatron-DeepSpeed",
                    "MosaicML Composer & LLM-Foundry",
                    "Nanotron & LitGPT Pre-Training Suites",
                    "DeepSeek-V3 (671B/37B MLA+MoE Base)",
                    "Qwen3 & Llama-4 Pre-Trained Base Models",
                    "OLMo-2 / Marin Fully-Open Base Checkpoints",
                ],
                "small": [
                    "GPT-5.4 / Claude 4.6 / Gemini 3 Base",
                    "Mistral Large 3 & Codestral Base",
                    "Qwen3-Next Hybrid Gated-DeltaNet",
                    "Nemotron-H Hybrid Mamba-Transformer",
                    "FlashAttention-3 Hopper FP8 Kernels",
                    "DeepEP High-Throughput MoE All-to-All",
                    "TransformerEngine FP8 Linear Layers",
                    "HuggingFace Accelerate & Safetensors",
                    "WandB · TensorBoard · MLflow Tracking",
                    "AWS ParallelCluster & Slurm Orchestrator",
                    "Checkpointer Async S3 / Lustre Write",
                    "EleutherAI GPT-NeoX Legacy Reference",
                ],
            },
            "ops_evals_security": {
                "h1": [
                    "Loss-Spike Recovery & Gradient Clipping",
                    "Base Perplexity (Bits-per-Byte) & NIAH",
                    "Distributed Checkpoint & Elastic Faults",
                ],
                "normal": [
                    "Global Gradient Norm Clipping (1.0)",
                    "Z-Loss Router Logit Regularization",
                    "Automated Loss-Spike Batch Skip/Rewind",
                    "Validation Bits-per-Byte (BPB) Tracking",
                    "Needle-in-a-Haystack (NIAH) & RULER",
                    "Few-Shot Base Evals (MMLU / HumanEval)",
                    "Async Distributed Checkpointing (<5s)",
                    "muP Proxy-Model Hyperparameter Transfer",
                ],
                "small": [
                    "Activation Outlier & Kurtosis Monitoring",
                    "MoE Expert Utilization Entropy Audit",
                    "Dead-Neuron & Attention-Sink Diagnostics",
                    "FP8 Underflow / Overflow Scaling Audit",
                    "In-Flight Straggler & NaN Detector",
                    "Cross-Datacenter DiLoCo Low-Comm Sync",
                    "Continued Pre-Training (CPT) Replay Mix",
                    "Base Model Memorization Extraction Audit",
                    "CBRN / Dual-Use Pre-Training Data Filter",
                    "Checkpoint Integrity SHA-256 Signing",
                    "Scaling Law Extrapolation (Loss vs FLOPs)",
                    "Long-Context Perplexity Decay Curve",
                ],
            },
            "failure_modes": {
                "h1": [
                    "Catastrophic Loss Spikes & NaN Divergence",
                    "MoE Routing Collapse (Expert Starvation)",
                    "Pipeline Bubble & All-to-All Bottlenecks",
                ],
                "normal": [
                    "BF16/FP8 Attention Logit Overflow",
                    "Top-K Router Dumping All Tokens to 1 Expert",
                    "30–50% GPU Idle Time in Naive Pipeline",
                    "Cross-Node EP All-to-All Network Saturation",
                    "Attention Sinks Hoarding Mass on BOS",
                    "RoPE Out-of-Distribution Length Collapse",
                    "Catastrophic Forgetting in Domain CPT",
                    "Corrupted Checkpoint From Silent SDC",
                    "Suboptimal Chinchilla Over/Under-Training",
                    "AdamW Weight-Decay Imbalance on Embeddings",
                ],
                "small": [],
            },
        },
    },
    {
        "layer": 5,
        "badge": "LAYER 5",
        "meter": "L5/10",
        "name": "SUPERVISED FINE-TUNING (SFT)",
        "core_unit": "Core Unit: Chat Templates, Packed Sequences & LoRA",
        "desc": "Instruction tuning, ChatML formatting, sequence packing, completion-only loss masking, and `PEFT` (`LoRA`/`DoRA`).",
        "book_ref": "Ch. 1.7–9, 3, 4, 30.2 (SFT, Packing & PEFT Adapters).",
        "accent": "#8B5CF6",
        "is_external_organism": False,
        "cells": {
            "primitives_arch": {
                "h1": [
                    "Instruction Tuning & ChatML Templates",
                    "Sequence Packing & Completion Masking",
                    "PEFT Adapters (LoRA / QLoRA / DoRA)",
                ],
                "normal": [
                    "ChatML Roles (System / User / Asst / Tool)",
                    "Completion-Only Loss Masking (Labels=-100)",
                    "Multipack / FlashAttention Varlen Packing",
                    "Position-ID Reset Across Packed Examples",
                    "LoRA (B*A Low-Rank Adapter Matrices)",
                    "QLoRA (4-Bit NF4 Base + Double Quant)",
                    "DoRA (Weight-Decomposed Magnitude/Dir)",
                    "PiSSA & rsLoRA (Rank-Stabilized Scaling)",
                ],
                "small": [
                    "Target Modules: q/k/v/o/gate/up/down_proj",
                    "LoRA Rank r = 8..128 & Alpha Scaling",
                    "NEFTune Noisy Embedding Regularization",
                    "Zeroth-Order MeZO Forward-Only Tuning",
                    "GaLore Gradient Low-Rank Projection",
                    "LISA Layerwise Importance Sampled Adam",
                    "Rejection Sampling SFT (Best-of-N Filter)",
                    "Multi-Turn Tool-Call Trajectory SFT",
                    "Harness Distillation (Teacher->Student SFT)",
                    "Model Merging (SLERP / TIES / DARE)",
                    "Adapter Fusion & Task Arithmetic",
                    "Spectrum SNR-Guided Selective Layer Freeze",
                ],
            },
            "frameworks_stack": {
                "h1": [
                    "HF TRL (SFTTrainer) · PEFT · Unsloth",
                    "Axolotl · LLaMA-Factory · Torchtune",
                    "MergeKit · bitsandbytes · Liger-Kernel",
                ],
                "normal": [
                    "HuggingFace TRL SFTTrainer & DataCollator",
                    "HuggingFace PEFT (LoraConfig / get_peft)",
                    "Unsloth (2x Speed, 70% Less VRAM Triton)",
                    "Axolotl & LLaMA-Factory YAML SFT Suites",
                    "PyTorch Torchtune & MosaicML Finetuning",
                    "bitsandbytes NF4 & HQQ / AWQ Quantizers",
                    "Liger-Kernel Fused Cross-Entropy Loss",
                    "MergeKit Multi-Adapter Checkpoint Merger",
                ],
                "small": [
                    "DataCollatorForCompletionOnlyLM",
                    "packing=True + flash_attention_2 Varlen",
                    "apply_chat_template(tokenize=True)",
                    "LoRA+ (Asymmetric A/B Learning Rates)",
                    "VeRA (Vector-Based Random Matrix Adaptation)",
                    "AdaLoRA SVD Adaptive Rank Allocation",
                    "OpenAI Harmony & ShareGPT JSONL Schemas",
                    "S-LoRA & Punica Multi-Adapter Serving",
                    "vLLM --enable-lora Dynamic Adapter Load",
                    "Predibase Lorax Multi-Tenant Server",
                    "HuggingFace Alignment Handbook Recipes",
                    "OpenPipe / Fireworks SFT Cloud Pipelines",
                ],
            },
            "ops_evals_security": {
                "h1": [
                    "Masking Verification (Zero Prompt Loss)",
                    "IFEval Instruction-Following & Format Audit",
                    "Safety Refusal & Backdoor Trigger Scans",
                ],
                "normal": [
                    "Prompt-Token Loss Masking Assertion (-100)",
                    "EOS / Stop-Token Generation Verification",
                    "Cross-Sample Attention Bleed Check (Varlen)",
                    "IFEval Format & Constraint Benchmarks",
                    "MT-Bench & AlpacaEval 2.0 Win-Rate Audits",
                    "Base-Capability Retention (MMLU / Coding)",
                    "Benign vs. Harmful Refusal Calibration Mix",
                    "Fine-Tuning Jailbreak & Sleeper-Agent Audit",
                ],
                "small": [
                    "Gradient Norm & Eval-Loss Early Stopping",
                    "Cosine LR with 3–10% Warmup Ratio",
                    "Epoch Cap (1–3 Epochs to Prevent Overfit)",
                    "Tool-Call JSON Schema Validity Rate",
                    "merged_and_unload() FP16 Export Check",
                    "Per-Token Log-Probability Drift Check",
                    "Shadow-Alignment Superficial Style Check",
                    "Emergent Misalignment Safety Probe",
                    "LoRA Adapter Checksum & Provenance",
                    "PII Memorization Canary Extraction Test",
                    "Multi-Turn Context-Switch Coherence Eval",
                    "Quantized QLoRA vs. BF16 LoRA Parity Check",
                ],
            },
            "failure_modes": {
                "h1": [
                    "Training on Prompt Tokens (Missing -100)",
                    "Chat Template EOS/BOS Mismatch Loops",
                    "Catastrophic Forgetting & Style Overfit",
                ],
                "normal": [
                    "Unmasked User Prompts Corrupting Policy",
                    "Wrong EOS Token Causing Infinite Babbling",
                    "Naive Packing Bleeding Attention Across Docs",
                    "Applying LoRA Only to Q/V (Missing MLP)",
                    "Overfitting Small SFT Set (>3 Epochs)",
                    "Superficial Alignment (Style Without Logic)",
                    "100 Safety Examples Breaking Benign Help",
                    "Narrow Insecure-Code SFT Misaligning Model",
                    "Adapter Merge Degrading Base Reasoning",
                    "Padding Side (Right vs. Left) Generation Bug",
                ],
                "small": [],
            },
        },
    },
    {
        "layer": 6,
        "badge": "LAYER 6",
        "meter": "L6/10",
        "name": "POST-TRAINING (RLHF, DPO & RLVR)",
        "core_unit": "Core Unit: Preference Pairs, Rollouts & Advantages",
        "desc": "Preference alignment (`PPO`, `DPO`, `KTO`) and critic-free verifiable-reward RL (`RLVR`: `GRPO`, `Dr. GRPO`, `DAPO`).",
        "book_ref": "Ch. 5, 6, 7, 8, 9, 10, 12, 13 (RLHF, DPO & RLVR).",
        "accent": "#A855F7",
        "is_external_organism": False,
        "cells": {
            "primitives_arch": {
                "h1": [
                    "Preference Tuning (PPO · DPO · KTO · SimPO)",
                    "Critic-Free RLVR: GRPO · Dr. GRPO · DAPO",
                    "Verifiable Execution Oracles & PRMs",
                ],
                "normal": [
                    "Bradley-Terry Reward Model & PPO (GAE)",
                    "Direct Preference Optimization (DPO)",
                    "KTO (Unpaired Binary Prospect Feedback)",
                    "IPO · ORPO · SimPO (Ref-Free Length Norm)",
                    "GRPO (Group-Relative Advantage, No Critic)",
                    "Dr. GRPO (Unbiased Length & Std Norm)",
                    "DAPO (Decoupled Clip-Higher & Sampling)",
                    "Cold-Start Pure-RL (DeepSeek-R1-Zero)",
                ],
                "small": [
                    "KL Penalty beta * D_KL(pi_theta || pi_ref)",
                    "PPO Clipped Surrogate epsilon in [0.1, 0.28]",
                    "GRPO Group Size G = 8..64 Rollouts/Prompt",
                    "Outcome RM (ORM) vs. Process RM (PRM)",
                    "RLCR (Confidence Calibration Brier Reward)",
                    "On-Policy Self-Distillation (OPSD / RLCSD)",
                    "REINFORCE++ & RLOO Leave-One-Out Baseline",
                    "Iterative Online DPO & Spin Self-Play",
                    "Constitutional AI (RLAIF Critique-Revise)",
                    "Rule-Based Format + Execution Reward Sum",
                    "Curriculum Difficulty Filtering (0 < Pass < 1)",
                    "Multi-Turn Agentic RL Environment Rollouts",
                ],
            },
            "frameworks_stack": {
                "h1": [
                    "verl · OpenRLHF · HF TRL (GRPO / DPO)",
                    "DeepSeek-R1 · OpenAI o3/o4 · QwQ-32B",
                    "Prime Intellect verifiers · NeMo Aligner",
                ],
                "normal": [
                    "verl (Volcengine HybridEngine RLHF/RLVR)",
                    "OpenRLHF (Ray + vLLM Distributed Async RL)",
                    "HuggingFace TRL (GRPOTrainer / DPOTrainer)",
                    "Prime Intellect verifiers & OpenR1 Suites",
                    "Unsloth Fast GRPO (Single-GPU RLVR)",
                    "NVIDIA NeMo Aligner & Megatron-LM RL",
                    "AllenAI Open-Instruct (TÜLU 3 RLVR Pipeline)",
                    "SkyRL &oat-rl Distributed Agentic RL",
                ],
                "small": [
                    "vLLM Rollout Engine + FSDP2 Actor Sync",
                    "NCCL In-Flight Weight Broadcast",
                    "Lean 4 / SymPy Formal Math Verifiers",
                    "Pytest / Sandbox Code Execution Graders",
                    "SWE-RL & WebRL Agent Trajectory Trainers",
                    "Search-R1 Multi-Turn Retrieval RL",
                    "RewardBench & RM-Bench Reference Models",
                    "ArmoRM Multi-Objective Reward Model",
                    "Llama-3.1-Nemotron-70B-Reward",
                    "Ray PlacementGroups for Actor/Ref/Rollout",
                    "WandB Rollout Length & Entropy Dashboards",
                    "DeepSeek-R1-Distill (1.5B–70B Checkpoints)",
                ],
            },
            "ops_evals_security": {
                "h1": [
                    "Deterministic Sandboxed Reward Graders",
                    "KL-Divergence & Policy Entropy Monitoring",
                    "Anti-Reward-Hacking & Alignment Audits",
                ],
                "normal": [
                    "Hermetic Unit-Test & Math Answer Verifiers",
                    "DAPO Dynamic Filtering of All-0 / All-1 Groups",
                    "Policy Entropy & KL-Divergence Guardrails",
                    "Length-Controlled Win-Rate (AlpacaEval LC)",
                    "RewardBench & JudgeBench Grader Audits",
                    "Instruction Hierarchy Privilege Training",
                    "Deliberative Alignment in Reasoning Traces",
                    "Sandbagging, Sycophancy & Deception Audits",
                ],
                "small": [
                    "Rollout Generation Wall-Clock (70–90% of RL)",
                    "Off-Policy Staleness Bound in Async RL",
                    "Format Reward Weight <= 0.1 vs. Accuracy 1.0",
                    "Code Grader Timeout & Anti-Tamper Lock",
                    "Over-Optimization Goodhart Curve Detection",
                    "Pass@1 vs. Pass@64 Diversity Gap Check",
                    "Activation Steering & SAE Circuit Probes",
                    "Machine Unlearning (RMU / Gradient Ascent)",
                    "GCG / AutoDAN / Best-of-N Jailbreak Evals",
                    "CBRN / Cyber ASL-3/4 Capability Gates",
                    "Expected Calibration Error (ECE) Post-RL",
                    "Contamination-Free LiveBench & AIME Evals",
                ],
            },
            "failure_modes": {
                "h1": [
                    "Reward Hacking & Length Inflation",
                    "Policy Entropy Collapse & Mode Collapse",
                    "GRPO Zero-Variance Advantage (All 0/1)",
                ],
                "normal": [
                    "Model Gaming Regex/Judge Without Solving",
                    "GRPO Group All-Correct/All-Wrong -> 0 Grad",
                    "DPO Likelihood Displacement (Chosen Drops)",
                    "Std-Dividing Advantage Biasing Easy/Short",
                    "Policy Entropy Crashing to 0 (Repetitive CoT)",
                    "4-Model PPO OOM Without Hybrid Sharding",
                    "Stale vLLM Rollout Weights Breaking PPO Ratio",
                    "Language Mixing in Unpenalized CoT Traces",
                    "Sycophantic Agreement With False Premises",
                    "Alignment Tax Degrading Creative Diversity",
                ],
                "small": [],
            },
        },
    },
    {
        "layer": 7,
        "badge": "LAYER 7",
        "meter": "L7/10",
        "name": "TEST-TIME COMPUTE & REASONING",
        "core_unit": "Core Unit: Thinking Tokens, Search Trees & Votes",
        "desc": "Inference-time System-2 scaling: Chain-of-Thought (`CoT`), thinking budgets, `Best-of-N`, `PRM` reranking, and `MCTS`.",
        "book_ref": "Ch. 12.1–8, 13, 19.2, 30.3 (Test-Time Compute & Search).",
        "accent": "#D946EF",
        "is_external_organism": False,
        "cells": {
            "primitives_arch": {
                "h1": [
                    "System-2 Chain-of-Thought (<think> CoT)",
                    "Parallel Scaling: Best-of-N & Majority@k",
                    "Sequential & Tree Search (PRM / MCTS)",
                ],
                "normal": [
                    "Long Internal Reasoning (<think>...</think>)",
                    "Adaptive Thinking Budgets (Low/Med/High)",
                    "Self-Consistency Majority Voting (maj@k)",
                    "Best-of-N Reranking With ORM / PRM",
                    "Step-Level Beam Search Guided by PRM",
                    "Monte Carlo Tree Search (MCTS / UCT Value)",
                    "Sequential Self-Correction & Reflexion Loops",
                    "Compute-Optimal Test-Time Scaling Allocation",
                ],
                "small": [
                    "PUCT = Q(s,a) + c * P(s,a) * sqrt(N)/(1+n)",
                    "Tree-of-Thoughts (ToT) BFS/DFS Branching",
                    "Graph-of-Thoughts (GoT) Aggregation",
                    "Budget Forcing ('Wait' vs. '</think>' Token)",
                    "Entropy-Guided Dynamic Branching",
                    "Speculative Reasoning (Big Draft / Small Run)",
                    "Self-Verification & Backtracking Traces",
                    "Pass@k Upper-Bound vs. Majority@k Gap",
                    "Difficulty-Aware Compute Routing",
                    "Confidence-Informed Early Stopping",
                    "Iterative Code-Execution Refine Loops",
                    "Test-Time Training (TTT) Local Weight Update",
                ],
            },
            "frameworks_stack": {
                "h1": [
                    "OpenAI o3 / GPT-5.4 ReasoningEffort API",
                    "Claude 4.6 Extended Thinking · Gemini 3",
                    "DeepSeek-R1 · Qwen3 Thinking · s1 Budget",
                ],
                "normal": [
                    "OpenAI reasoning_effort (low / med / high)",
                    "Anthropic Extended Thinking (budget_tokens)",
                    "Gemini 2.5/3 Thinking Budget & Summaries",
                    "Qwen3 Hybrid Thinking (/think vs. /no_think)",
                    "vLLM / SGLang Reasoning ParserFlags",
                    "Optillm Inference-Time Proxy (MCTS / BoN)",
                    "Search-and-Learn (HuggingFace SAL Recipes)",
                    "LATS (Language Agent Tree Search) Engine",
                ],
                "small": [
                    "Qwen2.5-Math-PRM-7B / Shepherd PRM",
                    "Skywork-o1-Open-PRM Step Verifiers",
                    "s1 Simple Test-Time Scaling (Budget Forcing)",
                    "DeepConf Entropy-Filtered Voting",
                    "AlphaProof / AlphaCode 2 Search Pipelines",
                    "Archon Compound Inference-Time Architecture",
                    "vLLM Prefix Caching Across Parallel Samples",
                    "SGLang Fork/Join Parallel Branching DSL",
                    "LeanDojo / Pantograph Proof-Tree Search",
                    "DSPy BestOfN & Refine Inference Modules",
                    "LiteLLM Unified Thinking-Token Billing",
                    "OpenRouter Reasoning-Token Stream API",
                ],
            },
            "ops_evals_security": {
                "h1": [
                    "Accuracy-per-Log-FLOP Scaling Curves",
                    "Pass@k vs. Cons@k & PRM Calibration",
                    "Overthinking & CoT Faithfulness Audits",
                ],
                "normal": [
                    "AIME / HMMT / Codeforces vs. Token Budget",
                    "ARC-AGI-1/2 & Humanity's Last Exam (HLE)",
                    "Pass@k vs. Majority@k / PRM@k Efficiency",
                    "ProcessBench Step-Error Localization Audit",
                    "Token-Budget Cap & Diminishing-Return Gate",
                    "CoT Faithfulness & Post-Hoc Rationalization",
                    "Hidden vs. Visible Reasoning Trace Safety",
                    "Latency-SLA Routing (System-1 vs System-2)",
                ],
                "small": [
                    "Optimal Compute Allocation (Smallx64 vs Bigx1)",
                    "First-Correct-Solution Token Index",
                    "Thinking-to-Answer Token Ratio Monitoring",
                    "Self-Correction Positive vs. Negative Flip Rate",
                    "PRM Step-Level AUROC & Calibration",
                    "Prefix-Cache Hit Rate During Tree Search",
                    "Monitorability of Unfaithful CoT Scheming",
                    "Reasoning-Token Cost Circuit Breakers",
                    "Prompt-Injected Infinite-Thinking DoS Guard",
                    "Deterministic Voting Tie-Breaking Rules",
                    "Verifier False-Positive Rate on Hard Tail",
                    "LiveCodeBench Holistic Contamination-Free",
                ],
            },
            "failure_modes": {
                "h1": [
                    "Overthinking & Analysis Paralysis (10x)",
                    "PRM Reward Hacking & Verifier Blindspots",
                    "Self-Correction Degrading Correct Answers",
                ],
                "normal": [
                    "Burning 32K Thinking Tokens on Trivial Queries",
                    "Circular 'Wait, let me re-verify' Babble Loops",
                    "Majority Vote Converging on Shared Bias",
                    "Imperfect PRM Selecting Adversarial Fluff",
                    "Intrinsic Self-Correction Without Oracle Hurting",
                    "Unfaithful CoT Hiding True Decision Shortcut",
                    "Tree Search Exploding KV-Cache VRAM (O(B^D))",
                    "Reasoning-Effort Timeout Dropping Tool Calls",
                    "Sponge-Prompt Attack Forcing Max Thinking",
                    "Leaking System Prompts Inside Raw <think>",
                ],
                "small": [],
            },
        },
    },
    {
        "layer": 8,
        "badge": "LAYER 8",
        "meter": "L8/10",
        "name": "CONTEXT, MEMORY, TOOLS & MCP",
        "core_unit": "Core Unit: Context Windows, Memory & JSON-RPC",
        "desc": "Context budgeting, 4-tier agentic memory (`Sleep-Time Compute`), function calling, `MCP`, and `SKILL.md`.",
        "book_ref": "Ch. 17, 18.2–3, 23, 24 (Memory, Tools, MCP & Skills).",
        "accent": "#EC4899",
        "is_external_organism": False,
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
                    "System / History / Scratchpad Token Budget",
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
        "layer": 9,
        "badge": "LAYER 9",
        "meter": "L9/10",
        "name": "AGENT HARNESS, LOOP & GRAPH",
        "core_unit": "Core Unit: State Transitions, Actions & Diffs",
        "desc": "The CPU/OS of an agent: `CLAUDE.md`/`AGENTS.md`, Loop Engineering, Graph Engineering (`LangGraph`), and `Harness²`.",
        "book_ref": "Ch. 18, 19, 20, 21, 27 (Harness, Loops & Graphs).",
        "accent": "#F59E0B",
        "is_external_organism": False,
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
                    "Decoupled Verification (No Self-Grading)",
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
        "layer": 10,
        "badge": "LAYER 10",
        "meter": "L10/10",
        "name": "MULTI-AGENT SWARMS & A2A",
        "core_unit": "Core Unit: A2A Tasks, Worktrees & GenUI Streams",
        "desc": "Multi-agent topologies (`OWC`), inter-agent protocols (`A2A`/`ACP`), parallel worktree swarms, and Agentic/Generative UI.",
        "book_ref": "Ch. 21.6, 25, 26, 28, 30.10/18 (A2A, MAS & Agentic UI).",
        "accent": "#F43F5E",
        "is_external_organism": False,
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
    {
        "layer": 11,
        "badge": "SEPARATE ORGANISM",
        "meter": "EXT",
        "name": "RAG & MULTIMODAL (EXTERNAL)",
        "core_unit": "Core Unit: Vector Chunks, ViT Patches & Audio Frames",
        "desc": "Detached retrieval (`Hybrid/Graph RAG`) and sensory (`Vision/Audio/Omni`) subsystems that plug into the agent stack.",
        "book_ref": "Ch. 14, 15, 16, 18.4, 30.8/9 (RAG, Vision & Audio).",
        "accent": "#14B8A6",
        "is_external_organism": True,
        "cells": {
            "primitives_arch": {
                "h1": [
                    "Hybrid & Agentic RAG (Dense+BM25+RRF)",
                    "GraphRAG Entity Summaries & REFRAG",
                    "Vision (ViT/SigLIP) & Native Omni Audio",
                ],
                "normal": [
                    "Bi-Encoder (HNSW) vs. Cross-Encoder Rerank",
                    "Reciprocal Rank Fusion (RRF) & ColBERT",
                    "Contextual Chunking & AST Code Splitting",
                    "Self-RAG / Corrective RAG / Search-R1",
                    "ViT Patch Projection & AnyRes Dynamic Tiling",
                    "Visual Token Compression (Perceiver/Q-Former)",
                    "Whisper Spectrogram & RVQ Audio Codecs",
                    "GUI Coordinate Grounding (Set-of-Mark/SoM)",
                ],
                "small": [
                    "HNSW / IVF-PQ / DiskANN Vector Indices",
                    "Matryoshka Representation Learning (MRL)",
                    "HyDE Hypothetical Document Embeddings",
                    "GraphRAG Community Detection (Leiden)",
                    "REFRAG Compress-Sense-Expand Decoding",
                    "SigLIP / CLIP Contrastive Alignment",
                    "Chameleon / Gemini Early-Fusion Omni",
                    "2D-RoPE Spatial Vision Positional Encoding",
                    "ColPali Visual Document Patch Retrieval",
                    "Full-Duplex Speech-to-Speech Streaming",
                    "Video Temporal Frame Sampling & 3D Tubes",
                    "Diffusion / Flow-Matching Visual Generation",
                ],
            },
            "frameworks_stack": {
                "h1": [
                    "Qdrant · Milvus · pgvector · Neo4j",
                    "LlamaIndex · Haystack · LightRAG · Docling",
                    "GPT-5.4 Omni · Gemini 3 · Qwen2.5-VL",
                ],
                "normal": [
                    "Qdrant · Milvus · Pinecone · Weaviate",
                    "pgvector · LanceDB · Chroma · FAISS",
                    "LlamaIndex · Haystack · Microsoft GraphRAG",
                    "BGE-M3 · Cohere Embed v3 & Rerank v3.5",
                    "Docling · Unstructured · Marker · MinerU PDF",
                    "Qwen2.5-VL / Qwen-Omni · Pixtral · InternVL",
                    "Whisper-v3 · Moshi · ElevenLabs · Cartesia",
                    "Claude Computer Use & OpenAI Operator GUI",
                ],
                "small": [
                    "Elasticsearch / OpenSearch BM25 Lexical",
                    "Firecrawl & Jina Reader Markdown Scrapers",
                    "ColPali / Byaldi Multimodal PDF RAG",
                    "Neo4j & FalkorDB Property Graph Stores",
                    "SQLite-vec & DuckDB-VSS Local Vector",
                    "LiveKit & Pipecat Real-Time Voice/Video",
                    "OmniParser UI Icon/Bounding-Box Detector",
                    "Playwright + Screenshot Visual DOM Hybrid",
                    "PaddleOCR & Surya Multilingual OCR",
                    "SAM 2 (Segment Anything) Spatial Masks",
                    "Flux.1 / SD3.5 / Veo 3 Media Generators",
                    "TwelveLabs & LanguageBind Video Indexers",
                ],
            },
            "ops_evals_security": {
                "h1": [
                    "RAG Triad Evals (Faithfulness / Recall@k)",
                    "Document-Level RBAC & Citation Locking",
                    "MMMU / ScreenSpot / OSWorld GUI Evals",
                ],
                "normal": [
                    "Ragas & TruLens Groundedness Oracles",
                    "NDCG@k · MRR · Recall@k Retrieval Audits",
                    "Pre-Indexing Document ACL / RBAC Filtering",
                    "Citation Span-Locking & Provenance Check",
                    "Hallucination Span Detection (LettuceDetect)",
                    "MMMU · MathVista · DocVQA · OCRBench",
                    "ScreenSpot & OSWorld GUI Grounding Evals",
                    "C2PA Cryptographic Media Watermarking",
                ],
                "small": [
                    "FRAMES & LongBench Multi-Hop RAG Eval",
                    "RGB (Retrieval-Augmented Generation Bench)",
                    "Cross-Tenant Vector Namespace Isolation",
                    "PII & Secret Redaction Before Indexing",
                    "Embedding Drift Monitor on Model Upgrade",
                    "Stale-Document TTL & Incremental Re-Index",
                    "Visual Prompt-Injection OCR Scrubbing",
                    "Audio Deepfake & Voice-Cloning Spoof Check",
                    "Voice Turn-Taking Latency (<300ms EoT)",
                    "Bounding-Box IoU Click Accuracy Audit",
                    "Video Long-Horizon Needle-in-a-Haystack",
                    "SynthID & AudioSeal Provenance Verification",
                ],
            },
            "failure_modes": {
                "h1": [
                    "Indirect Prompt Injection via RAG / Images",
                    "Naive Fixed-Size Mid-Table/Code Chunking",
                    "Visual OCR Hallucination & GUI Misclicks",
                ],
                "normal": [
                    "Poisoned Web/PDF Hijacking Agent via RAG",
                    "Hidden White-on-White Text in Images",
                    "512-Token Split Severing Table Headers",
                    "Unfiltered Vector Search Leaking Exec Docs",
                    "Hallucinated Citations on Unretrieved Text",
                    "Embedding Space Mismatch After Re-Index",
                    "VLM Misreading Dense Charts / Small Fonts",
                    "Coordinate Drift Clicking Wrong GUI Button",
                    "Quadratic ViT Patch Explosion on 4K Screens",
                    "Voice Interruption Desync & Echo Loops",
                ],
                "small": [],
            },
        },
    },
]


PHI = (1.0 + 5.0 ** 0.5) / 2.0  # Golden Ratio φ ≈ 1.61803398875

STAGE_H1_TITLES = {
    1: "1. Silicon",
    2: "2. Python",
    3: "3. Data",
    4: "4. Pre-Training",
    5: "5. SFT",
    6: "6. Post-Training",
    7: "7. Test-Time",
    8: "8. Memory & MCP",
    9: "9. Harness",
    10: "10. Multi-Agent",
    11: "RAG & Multimodal",
}

STAGE_SUBTITLES = {
    1: "GPU/TPU/NPU · HBM3e/SRAM · CUDA/Triton",
    2: "brew · uv · conda · pip · PyTorch · JAX",
    3: "Corpora · BPE/Tiktoken · Dedup & Synth",
    4: "Transformer · Sparse MoE · Scaling Laws",
    5: "Instruction Tuning · Packing · LoRA/DoRA",
    6: "RLHF (PPO/DPO) & Critic-Free RLVR (GRPO)",
    7: "System-2 <think> CoT · Best-of-N · MCTS",
    8: "Context · 4-Tier Memory · MCP · SKILL.md",
    9: "CLAUDE.md · Loop · LangGraph · Harness²",
    10: "OWC · Swarms · Google A2A · AG-UI",
    11: "Detached Hybrid/Graph RAG · Vision & Omni",
}


def render_desktop_agent_anatomy_megachart():
    """
    ISO A0-Width Landscape Megachart (46.8 x 21.6 in @ 300 DPI — exact 19.5:9 Mobile-Landscape
    Aspect Ratio, width = 46.8 in = 1188.7 mm ≈ 1189 mm ISO A0 landscape width).

    Strict Unskipped 5-Level Golden Ratio Typographic Hierarchy (φ = 1.61803398875):
      • T = H0 = 10.0 * φ² ≈ 26.18 pt : Main Megachart Title ("ANATOMY OF AI AGENTS 2026")
      • H1 = H0 / φ        ≈ 16.18 pt : Stage Title ("1. Silicon", "2. Python", ..., "10. Multi-Agent",
                                        "RAG & Multimodal") + Top-Left "AI AGENT ANATOMY"
      • H2 = H1 / φ        = 10.00 pt : Cell Tier-1 Top-3 Flagship Pills, Masthead Subtitle/Hook/Key,
                                        and Left-Column Row Pillar Titles
      • H3 = H2 / φ        ≈  6.18 pt : Cell Tier-2 Normal Grid Items (2x4 active / 4x1 fail),
                                        Column Header Subtitles/Descriptions/Bullets, Row Pillar Badges/Descs,
                                        and Masthead Footnote Strip
      • H4 = H3 / φ        ≈  3.82 pt : Cell Tier-3 Granular Footnote Grid Items (3x4 active / 2x2 fail)
    """
    plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]

    H2 = 10.0000          # 10.0000 pt (Cell Tier-1 Top-3 Pills, Masthead & Row Pillar Titles)
    H1 = H2 * PHI         # 16.1803 pt (1. Silicon, 2. Python, ... H1 Stage Titles)
    H0 = H1 * PHI         # 26.1803 pt (Title T = H0)
    H3 = H2 / PHI         #  6.1803 pt (Cell Tier-2 Normal Grid & Header Descriptions/Bullets)
    H4 = H3 / PHI         #  3.8197 pt (Cell Tier-3 Granular Footnote Grid)

    fig = plt.figure(figsize=(46.8, 21.6), dpi=300, facecolor="#0F172A")
    ax = fig.add_axes([0.003, 0.004, 0.994, 0.992])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    bg_canvas = FancyBboxPatch(
        (0.001, 0.001), 0.998, 0.998,
        boxstyle="round,pad=0.0,rounding_size=0.005",
        facecolor="#E2E8F0", edgecolor="#0F172A", linewidth=1.6
    )
    ax.add_patch(bg_canvas)

    # -------------------------------------------------------------------------
    # 1. Top Masthead (T=H0 Title + H2 Subtitle/Hook/Key + H3 Footnote Strip)
    # -------------------------------------------------------------------------
    hdr_y = 0.908
    hdr_h = 0.086
    hdr_box = FancyBboxPatch(
        (0.004, hdr_y), 0.992, hdr_h,
        boxstyle="round,pad=0.0,rounding_size=0.005",
        facecolor="#0F172A", edgecolor="#1E293B", linewidth=1.8
    )
    ax.add_patch(hdr_box)

    # Left Block: T = H0 Title + H2 Website/Subtitle Underneath
    ax.text(
        0.012, hdr_y + hdr_h * 0.70,
        "ANATOMY OF AI AGENTS 2026",
        fontsize=H0, fontweight="bold", color="#FFFFFF", va="center", ha="left"
    )
    ax.text(
        0.013, hdr_y + hdr_h * 0.34,
        "www.arianprabowo.com · 1. Silicon → 10. Multi-Agent + External RAG/Multimodal (arXiv:2606.24937)",
        fontsize=H2, fontweight="bold", color="#38BDF8", va="center", ha="left"
    )

    # Vertical divider 1
    ax.plot(
        [0.415, 0.415], [hdr_y + hdr_h * 0.24, hdr_y + hdr_h * 0.91],
        color="#334155", linewidth=1.6
    )

    # Middle Block: H2 Yellow Motivating Hook
    ax.text(
        0.423, hdr_y + hdr_h * 0.58,
        "What actually runs under an AI agent in 2026? Trace left to right:\n"
        "1. Silicon → 2. Python → 3. Data → 4. Pre-Training → 5. SFT →\n"
        "6. Post-Training → 7. Test-Time → 8. Memory & MCP → 9. Harness → 10. Multi-Agent.",
        fontsize=H2, fontweight="bold", color="#FEF08A", va="center", ha="left",
        linespacing=1.16
    )

    # Vertical divider 2
    ax.plot(
        [0.758, 0.758], [hdr_y + hdr_h * 0.24, hdr_y + hdr_h * 0.91],
        color="#334155", linewidth=1.6
    )

    # Right Block: H2 Blue 3-Step Key
    ax.text(
        0.766, hdr_y + hdr_h * 0.58,
        "① TRACE LEFT → RIGHT: Follow 1. Silicon → 10. Multi-Agent\n"
        "② SEPARATE ORGANISM: Far-right = RAG & Multimodal\n"
        "③ HARDEN PROD: Audit FAILURE MODES row at bottom",
        fontsize=H2, fontweight="bold", color="#93C5FD", va="center", ha="left",
        linespacing=1.18
    )

    # Horizontal divider above bottom footnote strip
    ax.plot(
        [0.010, 0.990], [hdr_y + hdr_h * 0.20, hdr_y + hdr_h * 0.20],
        color="#1E293B", linewidth=1.1
    )

    # Bottom Combined Grey Footnote Strip (H3)
    ax.text(
        0.500, hdr_y + hdr_h * 0.095,
        f"*Synthesized from Haggai Roitman's 'The Hitchhiker's Guide to Agentic AI: From Foundations to Systems' (arXiv:2606.24937, v1.4, June 2026) + 2026 systems tooling. "
        f"Companion to AI Skill Tree 2026 & AI Ladder Evolution by Arian Prabowo · {LAST_UPDATED_STR}",
        fontsize=H3, fontweight="bold", color="#94A3B8", va="center", ha="center"
    )

    # -------------------------------------------------------------------------
    # 2. Horizontal Geometry (Left Pillar Column + 10 Core Stages + 1 Detached Organism)
    # -------------------------------------------------------------------------
    left_x0 = 0.004
    left_w = 0.072
    col_gap = 0.0024
    org_sep_gap = 0.0096  # Extra visual gap separating 10. Multi-Agent from the Separate Organism
    active_x0 = left_x0 + left_w + col_gap
    n_layers = len(STACK_LAYERS)  # 11 total (10 core + 1 external organism)
    layer_col_w = (0.996 - active_x0 - (n_layers - 2) * col_gap - org_sep_gap) / n_layers

    def get_col_x(l_idx: int) -> float:
        base_x = active_x0 + l_idx * (layer_col_w + col_gap)
        if STACK_LAYERS[l_idx].get("is_external_organism"):
            base_x += org_sep_gap - col_gap
        return base_x

    col_hdr_y = 0.778
    col_hdr_h = 0.124

    # Top-Left Corner Card
    corner_box = FancyBboxPatch(
        (left_x0, col_hdr_y), left_w, col_hdr_h,
        boxstyle="round,pad=0.0,rounding_size=0.004",
        facecolor="#0F172A", edgecolor="#334155", linewidth=1.6
    )
    ax.add_patch(corner_box)
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.72,
        "AI AGENT\nANATOMY",
        fontsize=H1, fontweight="bold", color="#FFFFFF", va="center", ha="center",
        linespacing=1.02
    )
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.37,
        "1. Silicon → 10. Swarms",
        fontsize=H2, fontweight="bold", color="#FEF08A", va="center", ha="center"
    )
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.15,
        "+ Detached Organism\n(RAG & Multimodal)",
        fontsize=H3, fontweight="bold", color="#5EEAD4", va="center", ha="center",
        linespacing=1.10
    )

    # Vertical Dashed Boundary & Background Halo for the Detached Separate Organism (Column 11)
    org_x0 = get_col_x(10)
    org_div_x = org_x0 - org_sep_gap * 0.50
    ax.plot(
        [org_div_x, org_div_x], [0.008, col_hdr_y + col_hdr_h],
        color="#0D9488", linewidth=2.6, linestyle=(0, (7, 4)), alpha=0.90
    )
    org_halo = FancyBboxPatch(
        (org_x0 - 0.0018, 0.006),
        layer_col_w + 0.0036,
        col_hdr_y + col_hdr_h - 0.004,
        boxstyle="round,pad=0.0,rounding_size=0.005",
        facecolor="#CCFBF1", edgecolor="#0D9488", linewidth=1.8, linestyle=(0, (6, 3)), alpha=0.28
    )
    ax.add_patch(org_halo)

    # 10 Core Stage Column Headers + 1 Separate Organism Column Header
    # Stage Title ("1. Silicon", "2. Python", ...) is strictly H1 (= H0 / φ)
    for l_idx, ly in enumerate(STACK_LAYERS):
        lx = get_col_x(l_idx)
        is_org = bool(ly.get("is_external_organism"))
        st_num = ly["layer"]

        lbox_body = FancyBboxPatch(
            (lx, col_hdr_y), layer_col_w, col_hdr_h,
            boxstyle="round,pad=0.0,rounding_size=0.004",
            facecolor="#042F2E" if is_org else "#0F172A",
            edgecolor="#14B8A6" if is_org else "#334155",
            linewidth=2.0 if is_org else 1.5,
            linestyle="--" if is_org else "-"
        )
        ax.add_patch(lbox_body)

        inset_b = 0.0012
        banner_h = col_hdr_h * 0.52
        lbox_top = FancyBboxPatch(
            (lx + inset_b, col_hdr_y + col_hdr_h - banner_h - inset_b),
            layer_col_w - 2 * inset_b, banner_h,
            boxstyle="round,pad=0.0,rounding_size=0.003",
            facecolor="#115E59" if is_org else "#1E293B",
            edgecolor=ly["accent"],
            linewidth=1.5
        )
        ax.add_patch(lbox_top)

        b_top_y = col_hdr_y + col_hdr_h - inset_b
        if is_org:
            # Top strip of organism banner: SEPARATE ORGANISM · EXTERNAL badge
            ax.text(
                lx + layer_col_w / 2, b_top_y - banner_h * 0.20,
                "⇄ SEPARATE ORGANISM · EXTERNAL",
                fontsize=H3, fontweight="bold", color="#5EEAD4", va="center", ha="center"
            )
        else:
            # Top strip of stage banner: 10-segment progress bar centered across top of banner
            bar_total_w = layer_col_w - 0.0080
            bar_gap = 0.0008
            seg_w = (bar_total_w - 9 * bar_gap) / 10.0
            seg_h = banner_h * 0.14
            bar_x_start = lx + 0.0040
            bar_y = b_top_y - banner_h * 0.20 - seg_h / 2.0
            for b_i in range(10):
                bx_i = bar_x_start + b_i * (seg_w + bar_gap)
                is_lit = b_i < st_num
                seg_patch = FancyBboxPatch(
                    (bx_i, bar_y), seg_w, seg_h,
                    boxstyle="round,pad=0.0,rounding_size=0.0008",
                    facecolor=ly["accent"] if is_lit else "#334155",
                    edgecolor=ly["accent"] if is_lit else "#475569",
                    linewidth=0.50
                )
                ax.add_patch(seg_patch)

        # Single-Line Stage Title in H1 (= H0 / φ): "1. Silicon", "2. Python", ...
        ax.text(
            lx + layer_col_w / 2, b_top_y - banner_h * 0.56,
            STAGE_H1_TITLES[st_num],
            fontsize=H1,
            fontweight="bold",
            color="#FEF08A" if is_org else "#FFFFFF",
            va="center", ha="center"
        )

        # Concise scope subtitle at bottom of banner in H3 (= H0 / φ³)
        ax.text(
            lx + layer_col_w / 2, b_top_y - banner_h * 0.86,
            STAGE_SUBTITLES[st_num],
            fontsize=H3,
            fontweight="bold",
            color="#5EEAD4" if is_org else "#FEF08A",
            va="center", ha="center"
        )

        # Column Header Body below banner: Description & Bullets in H3 (= H0 / φ³)
        desc_wrapped = textwrap.fill(ly["desc"], width=42)
        unit_line = f"• {ly['core_unit']}"
        ref_line = f"• Guide: {ly['book_ref']}"

        body_avail_h = col_hdr_h - banner_h - inset_b
        body_top_y = col_hdr_y + body_avail_h * 0.93
        ax.text(
            lx + 0.0026,
            body_top_y,
            desc_wrapped,
            fontsize=H3,
            fontweight="bold",
            color="#F8FAFC",
            va="top",
            ha="left",
            linespacing=1.04,
        )

        bullet_body = f"{unit_line}\n{ref_line}"
        ax.text(
            lx + 0.0026,
            col_hdr_y + 0.0032,
            bullet_body,
            fontsize=H3,
            fontweight="bold",
            color="#5EEAD4" if is_org else "#93C5FD",
            va="bottom",
            ha="left",
            linespacing=1.04,
        )

    # -------------------------------------------------------------------------
    # 3. 4 Architectural Pillar Rows x (10 Core Stage Columns + 1 Organism Column)
    # -------------------------------------------------------------------------
    top_y = 0.772
    active_row_h = 0.199
    fail_row_h = 0.151
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
            "Hardware Physics,\nTraining Objectives,\nInference Search &\nAgent Topologies",
            "• 1–3: Silicon / Python / Data\n• 4–7: Pretrain / SFT / RLVR / TTC\n• 8–10: MCP / Harness / Swarms",
        ),
        "frameworks_stack": (
            "PILLAR 2",
            "FRAMEWORKS, PKGS\n& PROTOCOLS",
            "CLI Package Managers,\nDL/RL/Serving Engines,\nAgent Harnesses &\nSwarm Protocols",
            "• brew · uv · conda · pip · venv\n• PyTorch · JAX · TRL · verl · vLLM\n• MCP · SKILL.md · LangGraph · A2A",
        ),
        "ops_evals_security": (
            "PILLAR 3",
            "SCALING, EVALS\n& SECURITY",
            "Throughput SLAs,\nMicroVM Sandboxes,\nVerification Oracles &\nZero-Trust Guardrails",
            "• MFU · E2B/bwrap · Decontam\n• RLVR Graders · PRM · MCP OAuth\n• SWE-bench · pass^k · KYA",
        ),
        "failure_modes": (
            "ANTI-PATTERNS",
            "FAILURE MODES\n& TRAPS",
            "What Breaks in Prod:\nBottlenecks, Collapses,\nReward Hacking &\nSwarm Cascades",
            "• OOM & CUDA ABI Hell\n• Catastrophic Forgetting & Hack\n• Context Rot & O(N²) Chatter",
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
            facecolor="#0F172A", edgecolor=col["cell_edge"], linewidth=1.6
        )
        ax.add_patch(rbox_body)

        inset_r = 0.0014
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
            fontsize=H3, fontweight="bold", color="#FEF08A", va="center", ha="center"
        )
        ax.text(
            left_x0 + left_w / 2, ry + rh - inset_r - rbanner_h * 0.67,
            p_title,
            fontsize=H2,
            fontweight="bold", color="#FFFFFF", va="center", ha="center",
            linespacing=1.02
        )

        body_avail_h = rh - rbanner_h - inset_r
        ax.text(
            left_x0 + left_w / 2,
            ry + body_avail_h * 0.66,
            p_desc,
            fontsize=H3,
            fontweight="bold",
            color="#F8FAFC",
            va="center",
            ha="center",
            linespacing=1.08,
        )
        ax.text(
            left_x0 + 0.0030,
            ry + 0.005,
            p_bullets,
            fontsize=H3,
            fontweight="bold",
            color="#FCA5A5" if is_fail else "#93C5FD",
            va="bottom",
            ha="left",
            linespacing=1.08,
        )

        # 10 Core Layer Cells + 1 Separate Organism Cell across this Row
        for l_idx, ly in enumerate(STACK_LAYERS):
            cx = get_col_x(l_idx)
            cw = layer_col_w
            is_org = bool(ly.get("is_external_organism"))

            cell_data = ly["cells"][col["key"]]
            top_h1 = cell_data["h1"]
            mid_norm = cell_data["normal"]
            bot_small = cell_data["small"]

            cbox = FancyBboxPatch(
                (cx, ry), cw, rh,
                boxstyle="round,pad=0.0,rounding_size=0.004",
                facecolor=col["cell_bg"],
                edgecolor="#0D9488" if (is_org and not is_fail) else col["cell_edge"],
                linewidth=1.8 if is_org else (1.5 if not is_fail else 1.6),
                linestyle="--" if (is_fail or is_org) else "-"
            )
            ax.add_patch(cbox)

            pad_x = 0.0018
            pad_top = 0.0028
            pad_bot = 0.0024
            inner_w = cw - 2 * pad_x
            x_left = cx + pad_x

            # =================================================================
            # CASE A: Failure Modes Row (Top 3 Pills=H2, 4x1 Tier 2=H3, 2x2 Tier 3=H4)
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
                        fontsize=H2,
                        fontweight="bold",
                        color=col["h1_txt"],
                        va="center", ha="center"
                    )

                # Tier 2: 4 single-column rows (H3 = H2 / φ)
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
                    tx = x_left + 0.0016
                    ty = t2_top_y - (sr + 0.5) * t2_row_h
                    ax.text(
                        tx, ty,
                        f"▸ {kw}",
                        fontsize=H3,
                        fontweight="bold",
                        color=col["t2_txt"],
                        va="center", ha="left"
                    )

                # Tier 3: Bottom 4 in 2x2 grid inside bottom band (H4 = H3 / φ)
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
                    tx = x_left + sc * t3_col_w + 0.0010
                    ty = t3_top_y - (sr + 0.5) * t3_row_h
                    ax.text(
                        tx, ty,
                        textwrap.fill(kw, width=36),
                        fontsize=H4,
                        fontweight="bold",
                        color="#991B1B",
                        va="center", ha="left",
                        linespacing=0.95
                    )
                continue

            # =================================================================
            # CASE B: Full 3-Tier Active Architectural Cell (H2 -> H3 -> H4)
            # =================================================================
            gap_t1_t2 = 0.0022
            gap_t2_t3 = 0.0018
            avail_h = rh - pad_top - pad_bot - gap_t1_t2 - gap_t2_t3
            t1_h = avail_h * 0.365
            t2_h = avail_h * 0.375
            t3_h = avail_h * 0.260

            # --- TIER 1: Top 3 Flagship Pills (H2 = H1 / φ) ---
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
                    fontsize=H2,
                    fontweight="bold",
                    color=col["h1_txt"],
                    va="center", ha="center"
                )

            # --- TIER 2: Middle 8 in 2 Columns x 4 Rows (H3 = H2 / φ) ---
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

                tx = x_left + sc * t2_col_w + 0.0009
                ty = t2_top_y - (sr + 0.5) * t2_row_h
                ax.text(
                    tx, ty,
                    textwrap.fill(kw, width=27),
                    fontsize=H3,
                    fontweight="bold",
                    color=col["t2_txt"],
                    va="center", ha="left",
                    linespacing=0.95
                )

            # --- TIER 3: Bottom 12 in 3 Columns x 4 Rows (H4 = H3 / φ) ---
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
                tx = x_left + sc * t3_col_w + 0.0007
                ty = t3_top_y - (sr + 0.5) * t3_row_h
                ax.text(
                    tx, ty,
                    textwrap.fill(kw, width=25),
                    fontsize=H4,
                    fontweight="bold",
                    color=col["t3_txt"],
                    va="center", ha="left",
                    linespacing=0.94
                )

    fig.savefig(OUT_DEV_PNG, dpi=300, facecolor=fig.get_facecolor())
    fig.savefig(OUT_DEV_PDF, format="pdf", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved: {OUT_DEV_PNG} ({OUT_DEV_PNG.stat().st_size:,} bytes)")
    print(f"Saved: {OUT_DEV_PDF} ({OUT_DEV_PDF.stat().st_size:,} bytes)")


def render_mobile_agent_anatomy_chart():
    """
    Smartphone Landscape Mini Chart (26.0 x 12.0 in @ 300 DPI — exact 19.5:9 Mobile Landscape)
    flowing from LEFT to RIGHT (1. Silicon -> 10. Multi-Agent) + Detached Separate Organism (RAG & Multimodal),
    scaled proportionally by (26.0 / 46.8 = 5/9) with the same Unskipped Golden Ratio hierarchy:
      • M_H0 = H0 * (26.0 / 46.8) ≈ 14.54 pt : Title
      • M_H1 = M_H0 / φ           ≈  8.99 pt : Stage Title (1. Silicon, 2. Python, ...)
      • M_H2 = M_H1 / φ           ≈  5.56 pt : Cell Tier-1 Top-3 Pills, Masthead & Row Pillar Titles
      • M_H3 = M_H2 / φ           ≈  3.43 pt : Cell Tier-2 Normal Items, Subtitles & Footnote
    """
    plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]

    M_H2 = 10.0 * (26.0 / 46.8)          #  5.5556 pt (Cell Tier-1 Top-3 Pills, Masthead & Pillar Titles)
    M_H1 = M_H2 * PHI                    #  8.9891 pt (1. Silicon, 2. Python, ... Stage Title)
    M_H0 = M_H1 * PHI                    # 14.5446 pt (Title T = H0)
    M_H3 = M_H2 / PHI                    #  3.4335 pt (Cell Tier-2 Items & Header Subtitles/Bullets)

    fig = plt.figure(figsize=(26.0, 12.0), dpi=300, facecolor="#0F172A")
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
        fontsize=M_H0, fontweight="bold", color="#FFFFFF", va="center", ha="left"
    )
    ax.text(
        0.013, hdr_y + hdr_h * 0.34,
        "www.arianprabowo.com · 1. Silicon → 10. Multi-Agent + External RAG/Multimodal (arXiv:2606.24937)",
        fontsize=M_H2, fontweight="bold", color="#38BDF8", va="center", ha="left"
    )

    ax.plot(
        [0.415, 0.415], [hdr_y + hdr_h * 0.24, hdr_y + hdr_h * 0.91],
        color="#334155", linewidth=1.2
    )

    ax.text(
        0.423, hdr_y + hdr_h * 0.58,
        "What actually runs under an AI agent in 2026? Trace left to right:\n"
        "1. Silicon → 2. Python → 3. Data → 4. Pre-Training → 5. SFT →\n"
        "6. Post-Training → 7. Test-Time → 8. Memory & MCP → 9. Harness → 10. Multi-Agent.",
        fontsize=M_H2, fontweight="bold", color="#FEF08A", va="center", ha="left",
        linespacing=1.15
    )

    ax.plot(
        [0.758, 0.758], [hdr_y + hdr_h * 0.24, hdr_y + hdr_h * 0.91],
        color="#334155", linewidth=1.2
    )

    ax.text(
        0.766, hdr_y + hdr_h * 0.58,
        "① TRACE LEFT → RIGHT: Follow 1. Silicon → 10. Multi-Agent\n"
        "② SEPARATE ORGANISM: Far-right = RAG & Multimodal\n"
        "③ HARDEN PROD: Audit FAILURE MODES row at bottom",
        fontsize=M_H2, fontweight="bold", color="#93C5FD", va="center", ha="left",
        linespacing=1.18
    )

    ax.plot(
        [0.010, 0.990], [hdr_y + hdr_h * 0.20, hdr_y + hdr_h * 0.20],
        color="#1E293B", linewidth=0.9
    )

    ax.text(
        0.500, hdr_y + hdr_h * 0.095,
        f"*Based on Roitman 'The Hitchhiker's Guide to Agentic AI' (arXiv:2606.24937, June 2026) · Arian Prabowo · {LAST_UPDATED_STR}",
        fontsize=M_H3, fontweight="bold", color="#94A3B8", va="center", ha="center"
    )

    left_x0 = 0.004
    left_w = 0.072
    col_gap = 0.0024
    org_sep_gap = 0.0096
    active_x0 = left_x0 + left_w + col_gap
    n_layers = len(STACK_LAYERS)
    layer_col_w = (0.996 - active_x0 - (n_layers - 2) * col_gap - org_sep_gap) / n_layers

    def get_col_x(l_idx: int) -> float:
        base_x = active_x0 + l_idx * (layer_col_w + col_gap)
        if STACK_LAYERS[l_idx].get("is_external_organism"):
            base_x += org_sep_gap - col_gap
        return base_x

    col_hdr_y = 0.790
    col_hdr_h = 0.112

    corner_box = FancyBboxPatch(
        (left_x0, col_hdr_y), left_w, col_hdr_h,
        boxstyle="round,pad=0.0,rounding_size=0.004",
        facecolor="#0F172A", edgecolor="#334155", linewidth=1.3
    )
    ax.add_patch(corner_box)
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.72,
        "AI AGENT\nANATOMY",
        fontsize=M_H1, fontweight="bold", color="#FFFFFF", va="center", ha="center",
        linespacing=1.02
    )
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.37,
        "1. Silicon → 10. Swarms",
        fontsize=M_H2, fontweight="bold", color="#FEF08A", va="center", ha="center"
    )
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.15,
        "+ Detached\nRAG/Multimodal",
        fontsize=M_H3, fontweight="bold", color="#5EEAD4", va="center", ha="center",
        linespacing=1.08
    )

    org_x0 = get_col_x(10)
    org_div_x = org_x0 - org_sep_gap * 0.50
    ax.plot(
        [org_div_x, org_div_x], [0.008, col_hdr_y + col_hdr_h],
        color="#0D9488", linewidth=1.8, linestyle=(0, (6, 3)), alpha=0.90
    )
    org_halo = FancyBboxPatch(
        (org_x0 - 0.0016, 0.006),
        layer_col_w + 0.0032,
        col_hdr_y + col_hdr_h - 0.004,
        boxstyle="round,pad=0.0,rounding_size=0.005",
        facecolor="#CCFBF1", edgecolor="#0D9488", linewidth=1.4, linestyle=(0, (5, 3)), alpha=0.28
    )
    ax.add_patch(org_halo)

    for l_idx, ly in enumerate(STACK_LAYERS):
        lx = get_col_x(l_idx)
        is_org = bool(ly.get("is_external_organism"))
        st_num = ly["layer"]

        lbox_body = FancyBboxPatch(
            (lx, col_hdr_y), layer_col_w, col_hdr_h,
            boxstyle="round,pad=0.0,rounding_size=0.004",
            facecolor="#042F2E" if is_org else "#0F172A",
            edgecolor="#14B8A6" if is_org else "#334155",
            linewidth=1.6 if is_org else 1.3,
            linestyle="--" if is_org else "-"
        )
        ax.add_patch(lbox_body)

        inset_b = 0.0012
        banner_h = col_hdr_h * 0.58
        lbox_top = FancyBboxPatch(
            (lx + inset_b, col_hdr_y + col_hdr_h - banner_h - inset_b),
            layer_col_w - 2 * inset_b, banner_h,
            boxstyle="round,pad=0.0,rounding_size=0.003",
            facecolor="#115E59" if is_org else "#1E293B",
            edgecolor=ly["accent"],
            linewidth=1.2
        )
        ax.add_patch(lbox_top)

        b_top_y = col_hdr_y + col_hdr_h - inset_b
        if is_org:
            ax.text(
                lx + layer_col_w / 2, b_top_y - banner_h * 0.20,
                "⇄ SEPARATE ORGANISM · EXTERNAL",
                fontsize=M_H3, fontweight="bold", color="#5EEAD4", va="center", ha="center"
            )
        else:
            bar_total_w = layer_col_w - 0.0080
            bar_gap = 0.0006
            seg_w = (bar_total_w - 9 * bar_gap) / 10.0
            seg_h = banner_h * 0.14
            bar_x_start = lx + 0.0040
            bar_y = b_top_y - banner_h * 0.20 - seg_h / 2.0
            for b_i in range(10):
                bx_i = bar_x_start + b_i * (seg_w + bar_gap)
                is_lit = b_i < st_num
                seg_patch = FancyBboxPatch(
                    (bx_i, bar_y), seg_w, seg_h,
                    boxstyle="round,pad=0.0,rounding_size=0.0008",
                    facecolor=ly["accent"] if is_lit else "#334155",
                    edgecolor=ly["accent"] if is_lit else "#475569",
                    linewidth=0.40
                )
                ax.add_patch(seg_patch)

        ax.text(
            lx + layer_col_w / 2, b_top_y - banner_h * 0.56,
            STAGE_H1_TITLES[st_num],
            fontsize=M_H1,
            fontweight="bold",
            color="#FEF08A" if is_org else "#FFFFFF",
            va="center", ha="center"
        )

        ax.text(
            lx + layer_col_w / 2, b_top_y - banner_h * 0.86,
            STAGE_SUBTITLES[st_num],
            fontsize=M_H3,
            fontweight="bold",
            color="#5EEAD4" if is_org else "#FEF08A",
            va="center", ha="center"
        )

        unit_short = textwrap.fill(f"{ly['core_unit']} · {ly['book_ref']}", width=42)
        ax.text(
            lx + 0.0026,
            col_hdr_y + (col_hdr_h - banner_h) * 0.48,
            unit_short,
            fontsize=M_H3,
            fontweight="bold",
            color="#5EEAD4" if is_org else "#93C5FD",
            va="center",
            ha="left",
            linespacing=1.05,
        )

    top_y = 0.784
    active_row_h = 0.202
    fail_row_h = 0.156
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
            fontsize=M_H2,
            fontweight="bold", color="#FFFFFF", va="center", ha="center",
            linespacing=1.05
        )
        ax.text(
            left_x0 + left_w / 2, ry + rh * 0.25,
            m_sub,
            fontsize=M_H3,
            fontweight="bold", color="#FEE2E2" if is_fail else "#E2E8F0", va="center", ha="center"
        )

        for l_idx, ly in enumerate(STACK_LAYERS):
            cx = get_col_x(l_idx)
            cw = layer_col_w
            is_org = bool(ly.get("is_external_organism"))

            cell_data = ly["cells"][col["key"]]
            top_h1 = cell_data["h1"]
            mid_norm = cell_data["normal"]

            cbox = FancyBboxPatch(
                (cx, ry), cw, rh,
                boxstyle="round,pad=0.0,rounding_size=0.004",
                facecolor=col["cell_bg"],
                edgecolor="#0D9488" if (is_org and not is_fail) else col["cell_edge"],
                linewidth=1.5 if is_org else (1.3 if not is_fail else 1.4),
                linestyle="--" if (is_fail or is_org) else "-"
            )
            ax.add_patch(cbox)

            pad_x = 0.0018
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
                    fontsize=M_H2,
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
                    x_left + 0.0015, ty,
                    f"• {kw}",
                    fontsize=M_H3,
                    fontweight="bold",
                    color=col["t2_txt"],
                    va="center", ha="left"
                )

    fig.savefig(OUT_MOBILE_PNG, dpi=300, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved: {OUT_MOBILE_PNG} ({OUT_MOBILE_PNG.stat().st_size:,} bytes)")


def write_agent_anatomy_markdown():
    lines = [
        f"![Anatomy of AI Agents 2026 — 1. Silicon to 10. Multi-Agent + Detached RAG/Multimodal Megachart]({OUT_DEV_PNG.name})",
        "",
        f"![Anatomy of AI Agents 2026 — Mobile Landscape Mini Chart]({OUT_MOBILE_PNG.name})",
        "",
        "# ANATOMY OF AI AGENTS 2026 (`1. Silicon` → `10. Multi-Agent` + Detached `RAG & Multimodal` Organism)",
        "",
        "> **What actually runs under the hood of an autonomous AI agent in 2026? Trace left to right across the 10 core stages — `1. Silicon`, `2. Python` (`brew`/`uv`/`conda`/`pip`/`PyTorch`/`JAX`), `3. Data`, `4. Pre-Training`, `5. SFT`, `6. Post-Training` (`RLHF`/`DPO`/`RLVR`), `7. Test-Time`, `8. Memory & MCP`, `9. Harness` (`Harness²`), and `10. Multi-Agent` (`A2A` Swarms) — while `RAG & Multimodal` operate on the far right as a detached, external organism that plugs into the agent spine.**  ",
        f"> **How to Read ([www.arianprabowo.com](https://www.arianprabowo.com) · Based on Haggai Roitman's *The Hitchhiker's Guide to Agentic AI*, `arXiv:2606.24937` · <sub>`{LAST_UPDATED_STR}`</sub>):** **`① TRACE LEFT → RIGHT:`** Follow `1. Silicon → 10. Multi-Agent` · **`② SEPARATE ORGANISM:`** Inspect the detached `RAG & Multimodal` column on the far right · **`③ HARDEN PROD:`** Audit the **`FAILURE MODES & TRAPS`** row at the bottom.",
        "",
        "---",
        "",
        "## 1. Complete 10-Stage Anatomy + Detached RAG/Multimodal Organism Overview (`1. Silicon` → `10. Multi-Agent` + `RAG & Multimodal` × `4` Pillars)",
        "",
        "| Stage / Organism (`H1` Title · Subtitle · Core Unit · Book Ref) | Core Primitives & Architecture | Frameworks, Packages & Protocols | Scaling, Verification & Security | Failure Modes & Traps |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]

    for ly in STACK_LAYERS:
        st_num = ly["layer"]
        col0 = (
            f"**{STAGE_H1_TITLES[st_num]}** — *{STAGE_SUBTITLES[st_num]}*<br>"
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
        "## 2. Stage-by-Stage Architectural Breakdown (`1. Silicon` → `10. Multi-Agent` + `Separate Organism: RAG & Multimodal`)",
        "",
    ])

    for ly in STACK_LAYERS:
        st_num = ly["layer"]
        lines.extend([
            f"### {STAGE_H1_TITLES[st_num]} — {STAGE_SUBTITLES[st_num]}",
            "",
            f"{ly['desc']}",
            "",
            f"* **Core Unit of Compute / State:** `{ly['core_unit']}`",
            f"* **Primary Reference (`arXiv:2606.24937`):** {ly['book_ref']}",
            "",
            "| Architectural Pillar | Top 3 Flagship Checkpoints (`H2`) | Core Stack & Mechanisms (`H3`) | Granular Specs, Flags & Formulas (`H4`) |",
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
