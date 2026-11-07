#!/usr/bin/env python3
"""
Generate the 2026 Agent Anatomy Megachart ("ANATOMY OF AI AGENTS 2026"):
  1. dev/anatomy_of_AI_agents_2026/anatomy_of_AI_agents_2026.png        (46.8 x 21.6 in @ 300 DPI — ISO A0-Width 19.5:9 Landscape)
  2. dev/anatomy_of_AI_agents_2026/anatomy_of_AI_agents_2026.pdf        (Vector PDF)
  3. dev/anatomy_of_AI_agents_2026/anatomy_of_AI_agents_2026_mobile.png (26.0 x 12.0 in @ 300 DPI — Mobile 19.5:9 Landscape)
  4. dev/anatomy_of_AI_agents_2026/2026 11 07 anatomy_of_AI_agents_2026.md

Strict Golden Ratio Typography Rule anchored at H2 = 24.00 pt (φ = 1.61803398875):
  • T = H0 = H2 * φ² ≈ 62.83 pt : Main Megachart Title ("ANATOMY OF AI AGENTS 2026")
  • H1 = H2 * φ      ≈ 38.83 pt : Stage Short Names ("1. Silicon" .. "10. Swarms")
                                  & Organism Short Names ("LLM", "RAG", "Multimodal", "Embodied")
  • H2               = 24.00 pt : Cell Top Flagship Pill, Masthead Subtitle & Corner Subtitle
  • H3 = H2 / φ      ≈ 14.83 pt : Cell Secondary Checkpoint Pills (2 pills) & Masthead Reading Guide
  • H4 = H3 / φ      ≈  9.17 pt : Stage & Organism Full Names (<= 10 words), Cell 3x2 Core Stack Grid,
                                  Inner Red "⚠ ANTI-PATTERNS & TRAPS" Box (2x2), and Footnote Strip
"""

from datetime import datetime
from pathlib import Path
import textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

SCRIPT_DIR = Path(__file__).resolve().parent
OUT_DEV_PNG = SCRIPT_DIR / "anatomy_of_AI_agents_2026.png"
OUT_DEV_PDF = SCRIPT_DIR / "anatomy_of_AI_agents_2026.pdf"
OUT_MOBILE_PNG = SCRIPT_DIR / "anatomy_of_AI_agents_2026_mobile.png"
OUT_MD = SCRIPT_DIR / "2026 11 07 anatomy_of_AI_agents_2026.md"

LAST_UPDATED_STR = f"Updated: {datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %Z (UTC%:z)')}"

PHI = (1.0 + 5.0 ** 0.5) / 2.0  # Golden Ratio φ ≈ 1.61803398875

# -----------------------------------------------------------------------------
# 1. Four Organism Rows (Short Name <= 2 words at H1, Full Name <= 10 words at H4)
# -----------------------------------------------------------------------------
ORGANISMS = [
    {
        "key": "llm",
        "short_name": "LLM",
        "full_name": "Autoregressive Text, Code & Reasoning Language Models",
        "badge": "CORE SPINE",
        "desc": "Token-by-Token Language,\nSymbolic Math, Code Gen &\nAutonomous Agent Loops",
        "bullets": "• 1–3: GPU / PyTorch / BPE\n• 4–7: MoE / SFT / RLVR / CoT\n• 8–10: MCP / Harness² / A2A",
        "hdr_bg": "#047857",
        "cell_bg": "#ECFDF5",
        "cell_edge": "#059669",
        "h2_bg": "#065F46",
        "h2_txt": "#FFFFFF",
        "h3_bg": "#D1FAE5",
        "h3_txt": "#064E3B",
        "pill_edge": "#10B981",
        "t2_bg": "#F0FDF4",
        "t2_txt": "#065F46",
    },
    {
        "key": "rag",
        "short_name": "RAG",
        "full_name": "Hybrid Vector, Lexical & Graph Retrieval-Augmented Generation",
        "badge": "ORGANISM · KNOWLEDGE",
        "desc": "External Grounding, Dense +\nBM25 Search, GraphRAG &\nCitation Verification",
        "bullets": "• 1–3: SIMD / FAISS / Docling\n• 4–7: BGE-M3 / Rerank / HyDE\n• 8–10: Qdrant / Agentic RAG",
        "hdr_bg": "#0F766E",
        "cell_bg": "#F0FDFA",
        "cell_edge": "#0D9488",
        "h2_bg": "#115E59",
        "h2_txt": "#FFFFFF",
        "h3_bg": "#CCFBF1",
        "h3_txt": "#134E4A",
        "pill_edge": "#14B8A6",
        "t2_bg": "#F0FDFA",
        "t2_txt": "#115E59",
    },
    {
        "key": "multimodal",
        "short_name": "Multimodal",
        "full_name": "Vision, Audio, Speech, Video & Native Omni-Modal Models",
        "badge": "ORGANISM · SENSORY",
        "desc": "ViT Patch Perception, Native\nSpeech Codecs, Spatio-Temporal\nVideo & Cross-Modal Omni",
        "bullets": "• 1–3: NVDEC / FFmpeg / Pairs\n• 4–7: SigLIP / LLaVA / Visual CoT\n• 8–10: Token Merge / LiveKit",
        "hdr_bg": "#6D28D9",
        "cell_bg": "#F5F3FF",
        "cell_edge": "#7C3AED",
        "h2_bg": "#5B21B6",
        "h2_txt": "#FFFFFF",
        "h3_bg": "#EDE9FE",
        "h3_txt": "#4C1D95",
        "pill_edge": "#8B5CF6",
        "t2_bg": "#FAF5FF",
        "t2_txt": "#5B21B6",
    },
    {
        "key": "embodied",
        "short_name": "Embodied",
        "full_name": "GUI Computer Use, Physics World Models & VLA Robotics",
        "badge": "ORGANISM · ACTION",
        "desc": "Browser/OS GUI Control,\n3D Physics Simulators, World\nModels & VLA Robot Policies",
        "bullets": "• 1–3: Edge NPU / Isaac / Teleop\n• 4–7: VLA π0 / ACT / Sim2Real\n• 8–10: 3DGS / OSWorld / Fleets",
        "hdr_bg": "#1D4ED8",
        "cell_bg": "#EFF6FF",
        "cell_edge": "#2563EB",
        "h2_bg": "#1E40AF",
        "h2_txt": "#FFFFFF",
        "h3_bg": "#DBEAFE",
        "h3_txt": "#1E3A8A",
        "pill_edge": "#3B82F6",
        "t2_bg": "#F8FAFC",
        "t2_txt": "#1E40AF",
    },
]

for _org in ORGANISMS:
    assert len(_org["short_name"].split()) <= 2, f"Organism short_name > 2 words: {_org['short_name']}"
    assert len(_org["full_name"].split()) <= 10, f"Organism full_name > 10 words: {_org['full_name']}"

# -----------------------------------------------------------------------------
# 2. Ten Stages (Short Name <= 2 words at H1, Full Name <= 10 words at H4)
#    Inside each cell:
#      • h2_pill (1 flagship pill in H2 = 24.00 pt, <= 17 chars)
#      • h3_pills (2 checkpoint pills in H3 = 14.83 pt, <= 27 chars)
#      • normal (3x2 = 6 core stack items in H4 = 9.17 pt)
#      • anti (2x2 = 4 failure modes in H4 = 9.17 pt inside red dashed box)
# -----------------------------------------------------------------------------
STACK_STAGES = [
    # =========================================================================
    # 1. Silicon
    # =========================================================================
    {
        "stage": 1,
        "short_name": "Silicon",
        "full_name": "Physical Compute Silicon, GPU Clusters, HBM3e Memory & Interconnect Fabrics",
        "accent": "#38BDF8",
        "desc": "GPUs/TPUs/NPUs, HBM3e vs. SRAM hierarchy, CUDA/Triton kernels & NVLink/InfiniBand.",
        "core_unit": "Unit: FLOPs, HBM Bytes & Warps",
        "book_ref": "Guide: Ch. 1.6, 2.3, 11.10–14, 30.5",
        "cells": {
            "llm": {
                "h2_pill": "H100 / B200 · CUDA",
                "h3_pills": [
                    "HBM3e vs. On-Chip SRAM",
                    "FlashAttention-3 Tiling",
                ],
                "normal": [
                    "CUDA · OpenAI Triton",
                    "FP8 & Microscaling FP4",
                    "NVLink 5 & InfiniBand",
                    "MFU > 45% Utilization",
                    "Prefill vs. Decode BW",
                    "Confidential GPU TEEs",
                ],
                "anti": [
                    "HBM Bandwidth Wall",
                    "CUDA OOM Crashes",
                    "Silent SDC Bit-Flips",
                    "Straggler GPU Stall",
                ],
            },
            "rag": {
                "h2_pill": "cuVS · SIMD · NVMe",
                "h3_pills": [
                    "NVIDIA cuVS / RAFT GPU",
                    "AVX-512 Distance SIMD",
                ],
                "normal": [
                    "CAGRA GPU Graph Index",
                    "NVMe Gen5 DiskANN I/O",
                    "Int8 / Binary PQ Codes",
                    "RDMA Index Sharding",
                    "Sub-10ms p99 Vector SLA",
                    "DRAM + SSD Tiered Pool",
                ],
                "anti": [
                    "SSD Random-Read Thrash",
                    "HNSW Exceeding DRAM",
                    "PCIe Index Bottleneck",
                    "NUMA Socket Latency",
                ],
            },
            "multimodal": {
                "h2_pill": "NVDEC · ViT · DSP",
                "h3_pills": [
                    "Hardware NVDEC / NVENC",
                    "ViT Patch SRAM Tiling",
                ],
                "normal": [
                    "Apple M4 Unified RAM",
                    "JPEG/HEVC HW Decode",
                    "2D/3D DiT Conv Kernels",
                    "GPUDirect Video Ingest",
                    "Sub-200ms Voice DSP",
                    "4K Frame BW Budgeting",
                ],
                "anti": [
                    "CPU Video Decode Stall",
                    "4K Frame PCIe Flood",
                    "Audio Sample Clock Drift",
                    "Video Thermal Throttle",
                ],
            },
            "embodied": {
                "h2_pill": "Jetson Thor · PhysX",
                "h3_pills": [
                    "Edge NPU & Sensor ISP",
                    "GPU PhysX / Warp Sim",
                ],
                "normal": [
                    "1 kHz Real-Time Bus",
                    "LiDAR / IMU Hardware",
                    "EtherCAT / CAN-FD Bus",
                    "INT4/FP8 Edge NPU",
                    "10,000x Parallel Sim",
                    "Hardware E-Stop Relay",
                ],
                "anti": [
                    "Edge Thermal Throttle",
                    "OS Jitter Breaking 1kHz",
                    "CSI Camera Frame Drop",
                    "Sim Contact Mismatch",
                ],
            },
        },
    },
    # =========================================================================
    # 2. Python
    # =========================================================================
    {
        "stage": 2,
        "short_name": "Python",
        "full_name": "Python Runtimes, Package Managers, Virtual Environments & Tensor Compilers",
        "accent": "#60A5FA",
        "desc": "Package managers (brew, uv, conda, pip, venv), PyTorch, JAX, vLLM & sandboxes.",
        "core_unit": "Unit: Wheels, Tensors & Paged KV",
        "book_ref": "Guide: Ch. 1.24–25, 11.1–9, 21.5, 22.1",
        "cells": {
            "llm": {
                "h2_pill": "uv · PyTorch · vLLM",
                "h3_pills": [
                    "brew · uv · conda · pip · venv",
                    "PyTorch 2.x · JAX · SGLang",
                ],
                "normal": [
                    "torch.compile & XLA",
                    "PagedAttention KV Cache",
                    "uv.lock Reproducibility",
                    "E2B / Firecracker VM",
                    "Bubblewrap / Seatbelt",
                    "TTFT / TPOT Async SLAs",
                ],
                "anti": [
                    "CUDA ABI & Wheel Hell",
                    "Unsandboxed Host RCE",
                    "KV-Cache Preemption",
                    "pip Breaking flash-attn",
                ],
            },
            "rag": {
                "h2_pill": "FAISS · Arrow · PQ",
                "h3_pills": [
                    "FAISS · HNSWlib · LanceDB",
                    "psycopg3 · qdrant-client",
                ],
                "normal": [
                    "PyArrow Zero-Copy RAM",
                    "BM25 · Tantivy · DuckDB",
                    "Parquet Columnar Store",
                    "Async gRPC / HTTP Pools",
                    "ONNX / TRT Embed Serve",
                    "mmap Vector Segments",
                ],
                "anti": [
                    "Python GIL Chunk Lock",
                    "Pickle Index RCE Exploit",
                    "DB Pool Exhaustion",
                    "Pandas Copy RAM Blowup",
                ],
            },
            "multimodal": {
                "h2_pill": "FFmpeg · OpenCV",
                "h3_pills": [
                    "torchvision · torchaudio",
                    "LiveKit · whisper.cpp",
                ],
                "normal": [
                    "FFmpeg · PyAV · Decord",
                    "NVIDIA DALI GPU Loader",
                    "Pillow-SIMD · librosa",
                    "vLLM Multimodal Serve",
                    "Silero VAD Turn Runtime",
                    "WebRTC Jitter Buffers",
                ],
                "anti": [
                    "OpenCV BGR vs RGB Bug",
                    "FFmpeg Zombie Leaks",
                    "Audio Buffer Underruns",
                    "Pillow Bomb DoS Crash",
                ],
            },
            "embodied": {
                "h2_pill": "ROS 2 · Isaac · CDP",
                "h3_pills": [
                    "ROS 2 · Gymnasium · MuJoCo",
                    "Playwright · LeRobot",
                ],
                "normal": [
                    "NVIDIA Isaac Lab / Gym",
                    "CycloneDDS Middleware",
                    "Headless Chromium Xvfb",
                    "Open3D · Pinocchio IK",
                    "Async Vectorized Envs",
                    "Deterministic Replays",
                ],
                "anti": [
                    "ROS 2 Multicast Storms",
                    "Zombie Browser Leaks",
                    "Euler Gimbal Lock Bug",
                    "Sim Step Drift Desync",
                ],
            },
        },
    },
    # =========================================================================
    # 3. Data
    # =========================================================================
    {
        "stage": 3,
        "short_name": "Data",
        "full_name": "Web & Code Corpora, Subword Tokenization & Curation Pipelines",
        "accent": "#818CF8",
        "desc": "Pre/post-training corpora, BPE/Tiktoken tokenizers, deduplication & synthetic data.",
        "core_unit": "Unit: Corpora, Subwords & Shards",
        "book_ref": "Guide: Ch. 1.2, 3.1, 3.3–3.5, 4.1, 30.2",
        "cells": {
            "llm": {
                "h2_pill": "FineWeb · Byte-BPE",
                "h3_pills": [
                    "FineWeb-Edu · Dolma · Stack",
                    "Byte-BPE · Tiktoken · Dedup",
                ],
                "normal": [
                    "Datatrove · NeMo Curator",
                    "Verified Code/Math Synth",
                    "13-Gram Decontamination",
                    "PII & Secret Scrubbing",
                    "128k–256k Vocab Size",
                    "Curriculum Annealing",
                ],
                "anti": [
                    "Synthetic Model Collapse",
                    "Test-Set Contamination",
                    "Tokenizer Glitch Tokens",
                    "PII Baked into Weights",
                ],
            },
            "rag": {
                "h2_pill": "Docling · Chunking",
                "h3_pills": [
                    "Docling · Marker PDF ETL",
                    "Contextual & AST Chunking",
                ],
                "normal": [
                    "Anthropic Chunk Headers",
                    "Table-to-Markdown Parse",
                    "Hard-Negative Mining",
                    "Metadata & RBAC Tags",
                    "CDC Incremental Sync",
                    "Golden QA Eval Sets",
                ],
                "anti": [
                    "Mid-Table Naive Split",
                    "PDF Column Scramble",
                    "Stale Deleted Vectors",
                    "Missing ACL Metadata",
                ],
            },
            "multimodal": {
                "h2_pill": "DataComp · OCR",
                "h3_pills": [
                    "DataComp · OBELICS Pairs",
                    "OCR, Chart & Speech Sets",
                ],
                "normal": [
                    "CLIPScore Aesthetic Gate",
                    "ShareGPT4V Recaptioning",
                    "Scene-Cut Video Clips",
                    "EnCodec / Mimi Tokens",
                    "Face Blur & C2PA Scrub",
                    "Set-of-Mark BBox Labels",
                ],
                "anti": [
                    "Mismatched Alt-Text",
                    "Low-DPI OCR Misreads",
                    "Demographic Bias Skew",
                    "Audio Crosstalk Bleed",
                ],
            },
            "embodied": {
                "h2_pill": "Open-X · GUI Traces",
                "h3_pills": [
                    "Open X-Embodiment · DROID",
                    "Mind2Web · OSWorld · Ego4D",
                ],
                "normal": [
                    "ALOHA / VR Teleop Demos",
                    "DOM + Screen + Action",
                    "3D Point-Cloud Align",
                    "Joint-State Normalize",
                    "RLDS / LeRobot Parquet",
                    "Sim Domain Randomize",
                ],
                "anti": [
                    "Teleop Hesitation Noise",
                    "Screen Resolution Drift",
                    "Action-Space Mismatch",
                    "Unlogged Confounders",
                ],
            },
        },
    },
    # =========================================================================
    # 4. Pre-Training
    # =========================================================================
    {
        "stage": 4,
        "short_name": "Pre-Train",
        "full_name": "Foundation Model Architectures, Sparse MoE Routing & Self-Supervised Pre-Training",
        "accent": "#A78BFA",
        "desc": "Transformer/MoE/hybrid architectures, GQA/MLA, RoPE, next-token pre-training & scaling.",
        "core_unit": "Unit: Transformer Blocks & MoE",
        "book_ref": "Guide: Ch. 1.1, 2.2, 3.1, 11.1–9, 30.1",
        "cells": {
            "llm": {
                "h2_pill": "Sparse MoE · MLA",
                "h3_pills": [
                    "Sparse MoE · GQA / MLA",
                    "Megatron-LM · TorchTitan",
                ],
                "normal": [
                    "Llama 4 · Qwen 3 · V3",
                    "Mamba / DeltaNet Hybrid",
                    "RMSNorm, SwiGLU & RoPE",
                    "3D Parallel (DP/TP/PP/EP)",
                    "Chinchilla Scaling Laws",
                    "Perplexity (BPB) & NIAH",
                ],
                "anti": [
                    "Loss Spikes & NaN Crash",
                    "MoE Routing Collapse",
                    "Pipeline Bubble Stall",
                    "RoPE Length Collapse",
                ],
            },
            "rag": {
                "h2_pill": "BGE-M3 · ColBERTv2",
                "h3_pills": [
                    "Bi-Encoder InfoNCE Loss",
                    "BGE-M3 · NV-Embed · ColBERT",
                ],
                "normal": [
                    "Matryoshka (MRL) Dims",
                    "SPLADE Sparse Lexical",
                    "Cross-GPU In-Batch Negs",
                    "Bidirectional Encoders",
                    "Multilingual Alignment",
                    "MTEB & NDCG@10 Evals",
                ],
                "anti": [
                    "Embedding Anisotropy",
                    "False-Negative Batches",
                    "Domain Acronym Blindness",
                    "512-Token Truncation",
                ],
            },
            "multimodal": {
                "h2_pill": "SigLIP · Omni · DiT",
                "h3_pills": [
                    "SigLIP-2 · DINOv2 Vision",
                    "Early-Fusion Omni & DiT",
                ],
                "normal": [
                    "Qwen2.5-VL · InternVL3",
                    "MLP / Q-Former Projector",
                    "3D Video RoPE Position",
                    "RVQ Audio Codecs (Mimi)",
                    "Flow-Matching Backbones",
                    "Zero-Shot VQA & ASR",
                ],
                "anti": [
                    "Modality Text-IQ Drop",
                    "Bag-of-Patches Blindness",
                    "4K Quadratic ViT Blowup",
                    "Small-Text Patch Blur",
                ],
            },
            "embodied": {
                "h2_pill": "VLA π0 · V-JEPA 2",
                "h3_pills": [
                    "VLA (π0 · OpenVLA · RT-2)",
                    "World Models (V-JEPA / Genie)",
                ],
                "normal": [
                    "Diffusion Action Policy",
                    "Octo Multi-Embodiment",
                    "Latent Next-Frame Pred",
                    "3D Point-Cloud Encoder",
                    "SE(3) Equivariant Pose",
                    "Zero-Shot Sim Transfer",
                ],
                "anti": [
                    "Spurious Causal Confusion",
                    "World Physics Delusion",
                    "Mode-Averaging Freeze",
                    "Camera Viewpoint Fragile",
                ],
            },
        },
    },
    # =========================================================================
    # 5. SFT
    # =========================================================================
    {
        "stage": 5,
        "short_name": "SFT",
        "full_name": "Supervised Fine-Tuning, Instruction Templates, Sequence Packing & LoRA Adapters",
        "accent": "#C084FC",
        "desc": "Instruction tuning, ChatML formatting, sequence packing, loss masking & PEFT (LoRA/DoRA).",
        "core_unit": "Unit: ChatML, Packing & LoRA",
        "book_ref": "Guide: Ch. 1.8, 3.2, 7.6, 9.4, 30.2",
        "cells": {
            "llm": {
                "h2_pill": "ChatML · TRL · LoRA",
                "h3_pills": [
                    "TRL · Axolotl · Unsloth",
                    "LoRA · QLoRA · DoRA PEFT",
                ],
                "normal": [
                    "Completion Loss Masking",
                    "Multipack + Position IDs",
                    "Tool & Trajectory SFT",
                    "Cold-Start CoT Traces",
                    "MergeKit (SLERP / DARE)",
                    "IFEval Format Audits",
                ],
                "anti": [
                    "Unmasked Prompt Loss",
                    "EOS/BOS Template Loops",
                    "Packed Attention Bleed",
                    "Catastrophic Forgetting",
                ],
            },
            "rag": {
                "h2_pill": "Rerank · RAFT SFT",
                "h3_pills": [
                    "Cross-Encoder bge-reranker",
                    "Citation-Grounded RAFT SFT",
                ],
                "normal": [
                    "Domain Embed Fine-Tune",
                    "Distractor Doc Immunity",
                    "Query-Rewrite SFT",
                    "Text-to-SQL / JSON SFT",
                    "Margin-MSE Distillation",
                    "'I Don't Know' Abstain",
                ],
                "anti": [
                    "Memorizing Stale Facts",
                    "Believing Distractors",
                    "Fake [1] Citation Tags",
                    "Narrow Query Overfit",
                ],
            },
            "multimodal": {
                "h2_pill": "LLaVA · AnyRes SFT",
                "h3_pills": [
                    "Visual SFT (LLaVA / AnyRes)",
                    "GUI BBox & Duplex Voice SFT",
                ],
                "normal": [
                    "Projector + LLM Stage-2",
                    "High-Res Chart/Doc SFT",
                    "Interleaved Multi-Turn",
                    "Set-of-Mark Visual SFT",
                    "Moshi Full-Duplex SFT",
                    "MMMU & ChartQA Evals",
                ],
                "anti": [
                    "Blind Visual Guessing",
                    "Projector Detail Loss",
                    "BBox Coordinate Drift",
                    "Voice SFT Hurting Math",
                ],
            },
            "embodied": {
                "h2_pill": "ACT · BC · OS-Atlas",
                "h3_pills": [
                    "Behavioral Cloning & ACT",
                    "GUI Action SFT (OS-Atlas)",
                ],
                "normal": [
                    "k-Step Action Chunking",
                    "Language-Conditioned BC",
                    "Click / Type / Scroll SFT",
                    "Wrist + 3rd-Person View",
                    "New-Gripper LoRA Tune",
                    "Offline Action MSE Eval",
                ],
                "anti": [
                    "Compounding BC Drift",
                    "Copycat Action Inertia",
                    "Lighting Overfitting",
                    "Static Coordinate Click",
                ],
            },
        },
    },
    # =========================================================================
    # 6. Post-Training
    # =========================================================================
    {
        "stage": 6,
        "short_name": "Post-Train",
        "full_name": "Preference Alignment (RLHF/DPO) & Verifiable-Reward Reinforcement Learning (RLVR/GRPO)",
        "accent": "#F472B6",
        "desc": "Preference tuning (PPO, DPO, KTO) and critic-free RL with Verifiable Rewards (RLVR, GRPO).",
        "core_unit": "Unit: Pairs, Rollouts & Advantages",
        "book_ref": "Guide: Ch. 1.8, 3.2, 12.1–8, 30.2",
        "cells": {
            "llm": {
                "h2_pill": "PPO · DPO · GRPO",
                "h3_pills": [
                    "PPO · DPO · KTO · SimPO",
                    "RLVR: GRPO · DAPO · verl",
                ],
                "normal": [
                    "DeepSeek-R1 · o3 · QwQ",
                    "Code/Math Test Oracles",
                    "OpenRLHF · NeMo Aligner",
                    "KL & Entropy Monitoring",
                    "Deliberative Alignment",
                    "Length-Controlled Win",
                ],
                "anti": [
                    "Reward Hacking & Bloat",
                    "Policy Entropy Collapse",
                    "Zero-Variance Advantage",
                    "Judge Sycophancy Bias",
                ],
            },
            "rag": {
                "h2_pill": "Search-R1 · DPO",
                "h3_pills": [
                    "Search-R1 Multi-Hop RLVR",
                    "Citation Faithfulness DPO",
                ],
                "normal": [
                    "Query-Retrieve-Reason RL",
                    "Exact-Match / F1 Oracles",
                    "NLI Entailment Rewards",
                    "Conflict Resolution RL",
                    "Search Cost Penalty RL",
                    "RAGTruth & FaithBench",
                ],
                "anti": [
                    "Redundant Search Loops",
                    "Cherry-Picking Evidence",
                    "Over-Abstention Refusal",
                    "Uncited Extrapolation",
                ],
            },
            "multimodal": {
                "h2_pill": "VLM RLVR · RLAIF-V",
                "h3_pills": [
                    "Visual Math & OCR RLVR",
                    "RLAIF-V & Diffusion DPO",
                ],
                "normal": [
                    "IoU BBox Reward Oracles",
                    "Chart/Table Verifier RL",
                    "Flow-GRPO Aesthetic RL",
                    "Voice Turn-Taking RLHF",
                    "Visual Safety Alignment",
                    "HallusionBench Audits",
                ],
                "anti": [
                    "Text-Prior Blind Guess",
                    "Oversaturated Image Hack",
                    "Benign Image Refusals",
                    "Voice Barge-In Jitter",
                ],
            },
            "embodied": {
                "h2_pill": "Sim2Real · RLVR",
                "h3_pills": [
                    "OSWorld / WebArena RLVR",
                    "Sim-to-Real PPO & HIL-SERL",
                ],
                "normal": [
                    "DOM / DB State Oracles",
                    "Human-in-Loop SERL RL",
                    "Friction/Mass Randomize",
                    "Residual VLA Policy RL",
                    "Control-Barrier Shield",
                    "Docker Rollout Resets",
                ],
                "anti": [
                    "Simulator Physics Exploit",
                    "Hardware Damage in RL",
                    "Reward-Hacking 'Buy' Btn",
                    "Sparse Credit Stall",
                ],
            },
        },
    },
    # =========================================================================
    # 7. Test-Time
    # =========================================================================
    {
        "stage": 7,
        "short_name": "Test-Time",
        "full_name": "Test-Time Compute Scaling, System-2 Chain-of-Thought Reasoning & Tree Search",
        "accent": "#FBBF24",
        "desc": "Inference-time System-2 scaling: <think> CoT, Best-of-N, Process Reward Models & MCTS.",
        "core_unit": "Unit: <think> Tokens, PRM & Trees",
        "book_ref": "Guide: Ch. 13.1–8, 15.1–9, 30.2",
        "cells": {
            "llm": {
                "h2_pill": "<think> CoT · MCTS",
                "h3_pills": [
                    "System-2 <think> CoT",
                    "Best-of-N · PRM · MCTS",
                ],
                "normal": [
                    "o3 · Claude 4.6 · R1",
                    "Step-Level Process RM",
                    "Adaptive Budget Forcing",
                    "Exec-Filter Before Vote",
                    "Pass@k vs. Majority@k",
                    "AIME & ARC-AGI-2 Evals",
                ],
                "anti": [
                    "10x Overthinking Burn",
                    "PRM Verifier Hacking",
                    "Self-Correction Regress",
                    "Unfaithful Post-Hoc CoT",
                ],
            },
            "rag": {
                "h2_pill": "RRF · CRAG · HyDE",
                "h3_pills": [
                    "Hybrid RRF + Reranking",
                    "IRCoT · CRAG · Self-RAG",
                ],
                "normal": [
                    "Query Decomposition",
                    "HyDE Hypothetical Docs",
                    "Top-100 -> 10 Reranker",
                    "Interleaved Search + CoT",
                    "Minimum-Span Extraction",
                    "Dynamic Score Cutoffs",
                ],
                "anti": [
                    "Infinite Rewrite Loops",
                    "HyDE Hallucination Drift",
                    "Reranker p99 SLA Blowup",
                    "Multi-Hop Error Cascade",
                ],
            },
            "multimodal": {
                "h2_pill": "Visual CoT · Zoom",
                "h3_pills": [
                    "Iterative Crop/Zoom CoT",
                    "Active ROI Scan & Verify",
                ],
                "normal": [
                    "o3-Vision Crop Inspect",
                    "OpenCV Code-Exec Zoom",
                    "Video Keyframe Search",
                    "Diffusion CFG Scaling",
                    "Audio Re-Listen Verify",
                    "Multi-Crop Voting",
                ],
                "anti": [
                    "Zooming Irrelevant Bg",
                    "Blurry Crop Hallucinate",
                    "High-Res Token Overflow",
                    "CFG Over-Step Artifacts",
                ],
            },
            "embodied": {
                "h2_pill": "MPC · Tree Rollout",
                "h3_pills": [
                    "Model-Predictive Control",
                    "World-Model Tree Search",
                ],
                "normal": [
                    "CEM / MPPI Sim Rollouts",
                    "VLM Failure Replanning",
                    "Pre-Click Hover Verify",
                    "VoxPoser 3D Value Maps",
                    "Receding-Horizon Exec",
                    "Safety-Filter Critic",
                ],
                "anti": [
                    "Planning Lag > 1kHz Loop",
                    "5s Rollout Physics Drift",
                    "Unverified Destructive Click",
                    "Obstacle Deadlock Loop",
                ],
            },
        },
    },
    # =========================================================================
    # 8. Context
    # =========================================================================
    {
        "stage": 8,
        "short_name": "Context",
        "full_name": "Context Engineering, Four-Tier Memory, Tool Calling, MCP & Skills",
        "accent": "#F97316",
        "desc": "Context budgeting, 4-tier agentic memory, function calling, MCP, and SKILL.md.",
        "core_unit": "Unit: Context, Memory & JSON-RPC",
        "book_ref": "Guide: Ch. 17, 18.2–5, 22, 23",
        "cells": {
            "llm": {
                "h2_pill": "MCP · 4-Tier Mem",
                "h3_pills": [
                    "Model Context Protocol",
                    "4-Tier Memory & SKILL.md",
                ],
                "normal": [
                    "Letta · Mem0 · Zep",
                    "Episodic & Semantic Mem",
                    "Progressive Skill Load",
                    "Sleep-Time Consolidation",
                    "/compact (<65% Window)",
                    "MCP OAuth 2.1 & LoCoMo",
                ],
                "anti": [
                    "Lost-in-the-Middle Rot",
                    "100+ MCP Schema Bloat",
                    "SKILL.md / MCP Rug-Pull",
                    "Poisoned Memory State",
                ],
            },
            "rag": {
                "h2_pill": "Qdrant · GraphRAG",
                "h3_pills": [
                    "Qdrant · Milvus · pgvector",
                    "GraphRAG · LightRAG · Neo4j",
                ],
                "normal": [
                    "REFRAG / LLMLingua Comp",
                    "Dense + BM25 Hybrid DB",
                    "Leiden Graph Communities",
                    "Parent-Doc Expansion",
                    "Tenant RBAC Pre-Filter",
                    "RAG Triad Faithfulness",
                ],
                "anti": [
                    "Indirect Prompt Inject",
                    "Cross-Tenant Vector Leak",
                    "Context Stuffing Noise",
                    "GraphRAG Indexing Cost",
                ],
            },
            "multimodal": {
                "h2_pill": "ToMe · Video KV",
                "h3_pills": [
                    "ViT Token Merge (PruMerge)",
                    "Streaming Video KV Buffer",
                ],
                "normal": [
                    "Drop 75% Bg ViT Tokens",
                    "Cross-Modal CLIP Memory",
                    "Audio + Text Dual Index",
                    "MCP Presigned Media URI",
                    "Duplex Barge-In State",
                    "Video-MME Long Context",
                ],
                "anti": [
                    "10m Video Filling 128k",
                    "Pruning Tiny OCR Text",
                    "Base64 JSON-RPC Crash",
                    "Audio-Video Sync Drift",
                ],
            },
            "embodied": {
                "h2_pill": "3DGS · DOM AXTree",
                "h3_pills": [
                    "3D Scene Graphs & 3DGS",
                    "DOM & AXTree Pruning",
                ],
                "normal": [
                    "OctoMap Occupancy Grid",
                    "Set-of-Mark Element IDs",
                    "Proprioceptive Ring Buf",
                    "Kalman 6-DoF Object Track",
                    "MCP Robot/Browser Bus",
                    "Spatial Consistency QA",
                ],
                "anti": [
                    "50k-Node Raw DOM Flood",
                    "Dynamic Obstacle Ghosts",
                    "Out-of-Sight Forgetting",
                    "Odometry Frame Drift",
                ],
            },
        },
    },
    # =========================================================================
    # 9. Harness
    # =========================================================================
    {
        "stage": 9,
        "short_name": "Harness",
        "full_name": "Single-Agent Harness Engineering, Observe-Decide-Act Loops & Stateful Graph Workflows",
        "accent": "#F43F5E",
        "desc": "The CPU/OS of an agent: CLAUDE.md, Loop Engineering, LangGraph & Harness² verification.",
        "core_unit": "Unit: State, Actions & Git Diffs",
        "book_ref": "Guide: Ch. 16, 19, 20, 27",
        "cells": {
            "llm": {
                "h2_pill": "Claude Code · Loop",
                "h3_pills": [
                    "Claude Code · Codex · Cursor",
                    "LangGraph · Harness² Loop",
                ],
                "normal": [
                    "CLAUDE.md / AGENTS.md",
                    "Observe–Decide–Act Loop",
                    "Typed State & Checkpoints",
                    "Spec->Plan->Test->Verify",
                    "Independent Test Grader",
                    "SWE-bench & pass^k SLA",
                ],
                "anti": [
                    "Deleting Failing Tests",
                    "Infinite Loop Token Burn",
                    "God-Node State Bloat",
                    "IDE Auto-Approve RCE",
                ],
            },
            "rag": {
                "h2_pill": "Agentic RAG Loop",
                "h3_pills": [
                    "Agentic RAG Workflows",
                    "Plan–Search–Read–Verify",
                ],
                "normal": [
                    "Adaptive Router Gate",
                    "Sub-Question DAG Merge",
                    "Span-Level Citation Gate",
                    "Source Freshness Check",
                    "Web Fallback on KB Miss",
                    "DeepResearch Benchmark",
                ],
                "anti": [
                    "Rephrase Search Thrash",
                    "Silent Hallucination",
                    "Citation Laundering",
                    "Unbounded Research Lag",
                ],
            },
            "multimodal": {
                "h2_pill": "LiveKit · Pipecat",
                "h3_pills": [
                    "LiveKit / Pipecat Voice",
                    "Render–Inspect–Fix Loop",
                ],
                "normal": [
                    "VAD + Barge-In Machine",
                    "VLM UI Screenshot Diff",
                    "ComfyUI Gen-Critique",
                    "ControlNet Inpaint Loop",
                    "C2PA Media Provenance",
                    "WER & Turn-Latency SLA",
                ],
                "anti": [
                    "Talking Over User Voice",
                    "Transcribing Own TTS",
                    "VLM Breaking CSS Layout",
                    ">3s Cascaded Voice Lag",
                ],
            },
            "embodied": {
                "h2_pill": "Computer Use Loop",
                "h3_pills": [
                    "Operator / Claude CU Loop",
                    "System-2 VLM + System-1 VLA",
                ],
                "normal": [
                    "Screen -> Action -> Verify",
                    "Pop-Up & Auth Recovery",
                    "2Hz Planner + 50Hz Motor",
                    "Force/Torque Reflex Stop",
                    "Checkout/Delete Gate",
                    "OSWorld / WebArena Eval",
                ],
                "anti": [
                    "Fake Pop-Up Injection",
                    "Infinite 'Pay' Clicks",
                    "UI Lag Misaligned Click",
                    "Ignoring Gripper Slip",
                ],
            },
        },
    },
    # =========================================================================
    # 10. Multi-Agent
    # =========================================================================
    {
        "stage": 10,
        "short_name": "Swarms",
        "full_name": "Multi-Agent Orchestration, Hierarchical Swarms, A2A Protocols & Shared State",
        "accent": "#E879F9",
        "desc": "Multi-agent topologies (OWC), inter-agent protocols (A2A, ACP), worktree swarms & AG-UI.",
        "core_unit": "Unit: A2A Tasks & Swarm State",
        "book_ref": "Guide: Ch. 1.14, 14, 24, 26, 28, 30.10",
        "cells": {
            "llm": {
                "h2_pill": "A2A · OWC · AG-UI",
                "h3_pills": [
                    "Orchestrator–Worker–Critic",
                    "Google A2A · CrewAI · AG2",
                ],
                "normal": [
                    "Parallel Git Worktrees",
                    "Red-vs-Blue Independent",
                    "CopilotKit · AG-UI",
                    "Agent Gateway & FinOps",
                    "Cryptographic Agent KYA",
                    "/.well-known/agent.json",
                ],
                "anti": [
                    "Swarm Echo Hallucinate",
                    "O(N²) Chatty Token Burn",
                    "Confused Deputy Breach",
                    "Worktree Merge Conflict",
                ],
            },
            "rag": {
                "h2_pill": "Federated RAG MAS",
                "h3_pills": [
                    "Federated Knowledge Broker",
                    "Parallel Deep-Research MAS",
                ],
                "normal": [
                    "SQL + Vector + Graph Bus",
                    "Map-Reduce Lit Synthesis",
                    "Fact-Checker vs. Writer",
                    "OAuth On-Behalf-Of ACLs",
                    "Shared Citation Board",
                    "Cross-Silo Recall Evals",
                ],
                "anti": [
                    "Circular Citation Loop",
                    "Cross-Dept ACL Leakage",
                    "Duplicate Doc Fetching",
                    "Dropping Minority Facts",
                ],
            },
            "multimodal": {
                "h2_pill": "Multi-Modal Swarm",
                "h3_pills": [
                    "Cross-Modal Media Swarm",
                    "Director–Video–Audio MAS",
                ],
                "normal": [
                    "Voice + Tool Subagents",
                    "Character Style Board",
                    "Scene + Foley Sync Gen",
                    "VLM Visual QA Gatekeeper",
                    "Streaming AG-UI Canvas",
                    "Copyright & Brand Gate",
                ],
                "anti": [
                    "Character Identity Drift",
                    "Voice Promising Failed Op",
                    "Audio-Video Lip Desync",
                    "Runaway Render Spend",
                ],
            },
            "embodied": {
                "h2_pill": "Fleet MAPF Swarm",
                "h3_pills": [
                    "Multi-Robot Fleet Control",
                    "Digital-Twin + Physical MAS",
                ],
                "normal": [
                    "Conflict-Free MAPF Path",
                    "Drone + Rover + Arm MAS",
                    "V2X Spatial Perception",
                    "Cloud Plan + Edge Reflex",
                    "Human Teleop Handoff",
                    "Fleet Deadlock Evals",
                ],
                "anti": [
                    "Corridor Traffic Gridlock",
                    "Faulty Sensor Map Poison",
                    "Wi-Fi Drop Fleet Split",
                    "Dual-Arm Grasp Collision",
                ],
            },
        },
    },
]

STAGE_SHORT_NAMES = {}
STAGE_H1_TITLES = {}
STAGE_FULL_NAMES = {}

for _st in STACK_STAGES:
    _idx = _st["stage"]
    _sname = _st["short_name"]
    _fname = _st["full_name"]
    assert len(_sname.split()) <= 2 and len(_sname.replace("-", " ").split()) <= 2, f"Stage short_name > 2 words: {_sname}"
    assert len(_fname.split()) <= 10, f"Stage full_name > 10 words: {_fname}"
    STAGE_SHORT_NAMES[_idx] = _sname
    STAGE_H1_TITLES[_idx] = f"{_idx}. {_sname}"
    STAGE_FULL_NAMES[_idx] = _fname


def render_desktop_agent_anatomy_megachart():
    """
    ISO A0-Width Landscape Megachart (46.8 x 21.6 in @ 300 DPI — exact 19.5:9 Mobile-Landscape
    Aspect Ratio, width = 46.8 in = 1188.7 mm ≈ 1189 mm ISO A0 landscape width).

    Strict Unskipped 5-Level Golden Ratio Typographic Hierarchy anchored at H2 = 24.00 pt:
      • T = H0 = H2 * φ² ≈ 62.83 pt : Main Megachart Title ("ANATOMY OF AI AGENTS 2026")
      • H1 = H2 * φ      ≈ 38.83 pt : Stage Short Names ("1. Silicon" .. "10. Swarms")
                                      & Organism Short Names ("LLM", "RAG", "Multimodal", "Embodied")
      • H2               = 24.00 pt : Cell Top Flagship Pill, Masthead Subtitle & Corner Subtitle
      • H3 = H2 / φ      ≈ 14.83 pt : Cell Secondary Checkpoint Pills (2 pills) & Masthead Reading Guide
      • H4 = H3 / φ      ≈  9.17 pt : Stage & Organism Full Names (<= 10 words), Cell 3x2 Core Stack Grid,
                                      Inner Red "⚠ ANTI-PATTERNS & TRAPS" Box (2x2), and Footnote Strip
    """
    plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]

    H2 = 24.0000          # 24.0000 pt (Cell Top Flagship Pill & Masthead Subtitle)
    H1 = H2 * PHI         # 38.8328 pt (Stage Short Names & Organism Short Names)
    H0 = H1 * PHI         # 62.8328 pt (Main Title T = H0)
    H3 = H2 / PHI         # 14.8328 pt (Cell Secondary Checkpoint Pills & Masthead Guide)
    H4 = H3 / PHI         #  9.1672 pt (Full Names, Cell 3x2 Core Grid, Inner 2x2 Anti-Patterns & Footnote)

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
    # 1. Top Masthead (T=H0 Title + H2 Subtitle + H3 Reading Guide + H4 Footnote)
    # -------------------------------------------------------------------------
    hdr_y = 0.908
    hdr_h = 0.086
    hdr_box = FancyBboxPatch(
        (0.004, hdr_y), 0.992, hdr_h,
        boxstyle="round,pad=0.0,rounding_size=0.005",
        facecolor="#0F172A", edgecolor="#1E293B", linewidth=1.8
    )
    ax.add_patch(hdr_box)

    ax.text(
        0.012, hdr_y + hdr_h * 0.67,
        "ANATOMY OF AI AGENTS 2026",
        fontsize=H0, fontweight="bold", color="#FFFFFF", va="center", ha="left"
    )
    ax.text(
        0.013, hdr_y + hdr_h * 0.28,
        "www.arianprabowo.com · 1. Silicon → 10. Swarms × 4 Organisms",
        fontsize=H2, fontweight="bold", color="#38BDF8", va="center", ha="left"
    )

    ax.plot(
        [0.488, 0.488], [hdr_y + hdr_h * 0.20, hdr_y + hdr_h * 0.92],
        color="#334155", linewidth=1.6
    )

    ax.text(
        0.496, hdr_y + hdr_h * 0.56,
        "① COLUMNS (1 → 10): 1. Silicon → 2. Python → 3. Data → 4. Pre-Train → 5. SFT → 6. Post-Train → 7. Test-Time → 8. Context → 9. Harness → 10. Swarms\n"
        "② ROWS (4 ORGANISMS): Core LLM Spine + Separated RAG, Multimodal & Embodied Organisms\n"
        "③ INSIDE EVERY CELL: Flagship Pill (H2) + Checkpoints (H3) + Core Stack & Red ⚠ ANTI-PATTERNS Box (H4)",
        fontsize=H3, fontweight="bold", color="#FEF08A", va="center", ha="left",
        linespacing=1.18
    )

    ax.plot(
        [0.010, 0.990], [hdr_y + hdr_h * 0.16, hdr_y + hdr_h * 0.16],
        color="#1E293B", linewidth=1.1
    )

    ax.text(
        0.500, hdr_y + hdr_h * 0.075,
        f"*Synthesized from Haggai Roitman's 'The Hitchhiker's Guide to Agentic AI: From Foundations to Systems' (arXiv:2606.24937, v1.4, June 2026) + 2026 systems tooling · "
        f"Companion to AI Skill Tree 2026 & AI Ladder Evolution by Arian Prabowo · {LAST_UPDATED_STR}",
        fontsize=H4, fontweight="bold", color="#94A3B8", va="center", ha="center"
    )

    # -------------------------------------------------------------------------
    # 2. Horizontal Geometry (Left Organism Column + 10 Stage Columns)
    # -------------------------------------------------------------------------
    left_x0 = 0.004
    left_w = 0.080
    col_gap = 0.0024
    active_x0 = left_x0 + left_w + col_gap
    n_stages = len(STACK_STAGES)  # 10 stages
    stage_col_w = (0.996 - active_x0 - (n_stages - 1) * col_gap) / n_stages

    def get_col_x(s_idx: int) -> float:
        return active_x0 + s_idx * (stage_col_w + col_gap)

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
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.74,
        "ANATOMY",
        fontsize=H1, fontweight="bold", color="#FFFFFF", va="center", ha="center"
    )
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.43,
        "1 → 10 Stages",
        fontsize=H2, fontweight="bold", color="#FEF08A", va="center", ha="center"
    )
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.16,
        "LLM · RAG · Multimodal\n· Embodied (+ ⚠ Traps)",
        fontsize=H4, fontweight="bold", color="#5EEAD4", va="center", ha="center",
        linespacing=1.06
    )

    # 10 Stage Column Headers
    for s_idx, st in enumerate(STACK_STAGES):
        lx = get_col_x(s_idx)
        st_num = st["stage"]

        lbox_body = FancyBboxPatch(
            (lx, col_hdr_y), stage_col_w, col_hdr_h,
            boxstyle="round,pad=0.0,rounding_size=0.004",
            facecolor="#0F172A",
            edgecolor="#334155",
            linewidth=1.5
        )
        ax.add_patch(lbox_body)

        inset_b = 0.0012
        banner_h = col_hdr_h * 0.64
        lbox_top = FancyBboxPatch(
            (lx + inset_b, col_hdr_y + col_hdr_h - banner_h - inset_b),
            stage_col_w - 2 * inset_b, banner_h,
            boxstyle="round,pad=0.0,rounding_size=0.003",
            facecolor="#1E293B",
            edgecolor=st["accent"],
            linewidth=1.5
        )
        ax.add_patch(lbox_top)

        b_top_y = col_hdr_y + col_hdr_h - inset_b

        # 10-segment progress bar centered across top of banner
        bar_total_w = stage_col_w - 0.0080
        bar_gap = 0.0008
        seg_w = (bar_total_w - 9 * bar_gap) / 10.0
        seg_h = banner_h * 0.09
        bar_x_start = lx + 0.0040
        bar_y = b_top_y - banner_h * 0.11 - seg_h / 2.0
        for b_i in range(10):
            bx_i = bar_x_start + b_i * (seg_w + bar_gap)
            is_lit = b_i < st_num
            seg_patch = FancyBboxPatch(
                (bx_i, bar_y), seg_w, seg_h,
                boxstyle="round,pad=0.0,rounding_size=0.0008",
                facecolor=st["accent"] if is_lit else "#334155",
                edgecolor=st["accent"] if is_lit else "#475569",
                linewidth=0.50
            )
            ax.add_patch(seg_patch)

        # Short Name (<= 2 words) in H1 (= 38.83 pt): "1. Silicon", "2. Python", ...
        ax.text(
            lx + stage_col_w / 2, b_top_y - banner_h * 0.43,
            STAGE_H1_TITLES[st_num],
            fontsize=H1,
            fontweight="bold",
            color="#FFFFFF",
            va="center", ha="center"
        )

        # Full Name (<= 10 words, wrapped onto 2 lines) at bottom of banner in H4 (= 9.17 pt)
        ax.text(
            lx + stage_col_w / 2, b_top_y - banner_h * 0.81,
            textwrap.fill(STAGE_FULL_NAMES[st_num], width=36),
            fontsize=H4,
            fontweight="bold",
            color="#FEF08A",
            va="center", ha="center",
            linespacing=1.00
        )

        # Column Header Body below banner: Core Unit & Book Reference in H4 (= 9.17 pt)
        body_avail_h = col_hdr_h - banner_h - inset_b
        bullet_body = f"• {st['core_unit']}\n• {st['book_ref']}"
        ax.text(
            lx + stage_col_w / 2,
            col_hdr_y + body_avail_h * 0.50,
            bullet_body,
            fontsize=H4,
            fontweight="bold",
            color="#93C5FD",
            va="center",
            ha="center",
            linespacing=1.08,
        )

    # -------------------------------------------------------------------------
    # 3. 4 Organism Rows (LLM Spine + Detached RAG, Multimodal, Embodied)
    #    with Red Dashed "⚠ ANTI-PATTERNS & TRAPS" Box INSIDE Every Cell
    # -------------------------------------------------------------------------
    top_y = 0.772
    row_h = 0.1865
    spine_sep_gap = 0.0075
    row_gap = 0.0042

    row_geoms = [
        (top_y - 1 * row_h, row_h),
        (top_y - 2 * row_h - spine_sep_gap, row_h),
        (top_y - 3 * row_h - spine_sep_gap - 1 * row_gap, row_h),
        (top_y - 4 * row_h - spine_sep_gap - 2 * row_gap, row_h),
    ]

    sep_y = top_y - row_h - spine_sep_gap * 0.50
    ax.plot(
        [left_x0, 0.996], [sep_y, sep_y],
        color="#0D9488", linewidth=2.2, linestyle=(0, (7, 4)), alpha=0.85
    )

    for r_idx, org in enumerate(ORGANISMS):
        ry, rh = row_geoms[r_idx]

        # Left Organism Row-Header Card
        rbox_body = FancyBboxPatch(
            (left_x0, ry), left_w, rh,
            boxstyle="round,pad=0.0,rounding_size=0.004",
            facecolor="#0F172A", edgecolor=org["cell_edge"], linewidth=1.8
        )
        ax.add_patch(rbox_body)

        inset_r = 0.0014
        rbanner_h = rh * 0.54
        rbox_top = FancyBboxPatch(
            (left_x0 + inset_r, ry + rh - rbanner_h - inset_r),
            left_w - 2 * inset_r, rbanner_h,
            boxstyle="round,pad=0.0,rounding_size=0.003",
            facecolor=org["hdr_bg"], edgecolor="#FFFFFF", linewidth=1.1
        )
        ax.add_patch(rbox_top)

        rb_top_y = ry + rh - inset_r
        ax.text(
            left_x0 + left_w / 2, rb_top_y - rbanner_h * 0.13,
            org["badge"],
            fontsize=H4, fontweight="bold", color="#FEF08A", va="center", ha="center"
        )
        ax.text(
            left_x0 + left_w / 2, rb_top_y - rbanner_h * 0.44,
            org["short_name"],
            fontsize=H1,
            fontweight="bold", color="#FFFFFF", va="center", ha="center"
        )
        ax.text(
            left_x0 + left_w / 2, rb_top_y - rbanner_h * 0.80,
            textwrap.fill(org["full_name"], width=24),
            fontsize=H4,
            fontweight="bold", color="#E2E8F0", va="center", ha="center",
            linespacing=0.98
        )

        body_avail_h = rh - rbanner_h - inset_r
        ax.text(
            left_x0 + left_w / 2,
            ry + body_avail_h * 0.68,
            org["desc"],
            fontsize=H4,
            fontweight="bold",
            color="#F8FAFC",
            va="center",
            ha="center",
            linespacing=1.04,
        )
        ax.text(
            left_x0 + left_w / 2,
            ry + body_avail_h * 0.22,
            org["bullets"],
            fontsize=H4,
            fontweight="bold",
            color="#93C5FD",
            va="center",
            ha="center",
            linespacing=1.04,
        )

        # 10 Stage Cells for this Organism
        for s_idx, st in enumerate(STACK_STAGES):
            cx = get_col_x(s_idx)
            cw = stage_col_w

            cell_data = st["cells"][org["key"]]
            h2_pill_str = cell_data["h2_pill"]
            h3_pills = cell_data["h3_pills"]
            mid_norm = cell_data["normal"]
            anti_list = cell_data["anti"]

            cbox = FancyBboxPatch(
                (cx, ry), cw, rh,
                boxstyle="round,pad=0.0,rounding_size=0.004",
                facecolor=org["cell_bg"],
                edgecolor=org["cell_edge"],
                linewidth=1.5
            )
            ax.add_patch(cbox)

            pad_x = 0.0016
            pad_top = 0.0024
            pad_bot = 0.0022
            inner_w = cw - 2 * pad_x
            x_left = cx + pad_x

            gap_z = 0.0016
            avail_h = rh - pad_top - pad_bot - 3 * gap_z
            z1_h = avail_h * 0.16   # Zone 1: Top Flagship Banner Pill (H2 = 24.00 pt)
            z2_h = avail_h * 0.22   # Zone 2: 2 Secondary Checkpoint Pills (H3 = 14.83 pt)
            z3_h = avail_h * 0.31   # Zone 3: 3x2 = 6 Core Stack Grid (H4 = 9.17 pt)
            anti_h = avail_h * 0.31 # Zone 4: Inner Red "⚠ ANTI-PATTERNS & TRAPS" Box (2x2 in H4 = 9.17 pt)

            # -----------------------------------------------------------------
            # Zone 1: Top Flagship Pill in H2 (= 24.00 pt)
            # -----------------------------------------------------------------
            z1_top_y = ry + rh - pad_top
            z1_bot_y = z1_top_y - z1_h
            p_h2 = FancyBboxPatch(
                (x_left, z1_bot_y), inner_w, z1_h,
                boxstyle="round,pad=0.0,rounding_size=0.0024",
                facecolor=org["h2_bg"],
                edgecolor=org["pill_edge"],
                linewidth=1.2
            )
            ax.add_patch(p_h2)
            ax.text(
                x_left + inner_w / 2, z1_bot_y + z1_h / 2,
                h2_pill_str,
                fontsize=H2,
                fontweight="bold",
                color=org["h2_txt"],
                va="center", ha="center"
            )

            # -----------------------------------------------------------------
            # Zone 2: 2 Secondary Checkpoint Pills in H3 (= 14.83 pt)
            # -----------------------------------------------------------------
            z2_top_y = z1_bot_y - gap_z
            pill_gap = 0.0014
            ph3 = (z2_h - pill_gap) / 2.0
            for idx_p, kw in enumerate(h3_pills[:2]):
                py = z2_top_y - (idx_p + 1) * ph3 - idx_p * pill_gap
                pill = FancyBboxPatch(
                    (x_left, py), inner_w, ph3,
                    boxstyle="round,pad=0.0,rounding_size=0.0020",
                    facecolor=org["h3_bg"],
                    edgecolor=org["pill_edge"],
                    linewidth=1.0
                )
                ax.add_patch(pill)
                ax.text(
                    x_left + inner_w / 2, py + ph3 / 2,
                    kw,
                    fontsize=H3,
                    fontweight="bold",
                    color=org["h3_txt"],
                    va="center", ha="center"
                )

            # -----------------------------------------------------------------
            # Zone 3: Middle 3x2 = 6 Core Stack & Mechanisms Grid in H4 (= 9.17 pt)
            # -----------------------------------------------------------------
            z3_top_y = z2_top_y - z2_h - gap_z
            t2_row_h = z3_h / 3.0
            t2_col_w = inner_w / 2.0

            ax.plot(
                [x_left + t2_col_w, x_left + t2_col_w],
                [z3_top_y - z3_h + 0.0006, z3_top_y - 0.0006],
                color=org["cell_edge"], linewidth=0.60, alpha=0.35
            )

            for idx_2, kw in enumerate(mid_norm[:6]):
                mr = idx_2 // 2
                mc = idx_2 % 2
                if mr % 2 == 1 and mc == 0:
                    stripe = FancyBboxPatch(
                        (x_left + 0.0004, z3_top_y - (mr + 1) * t2_row_h + 0.00015),
                        inner_w - 0.0008, t2_row_h - 0.0003,
                        boxstyle="round,pad=0.0,rounding_size=0.0012",
                        facecolor=org["t2_bg"],
                        edgecolor="none"
                    )
                    ax.add_patch(stripe)

                tx = x_left + mc * t2_col_w + 0.0009
                ty = z3_top_y - (mr + 0.5) * t2_row_h
                ax.text(
                    tx, ty,
                    textwrap.fill(kw, width=19),
                    fontsize=H4,
                    fontweight="bold",
                    color=org["t2_txt"],
                    va="center", ha="left",
                    linespacing=1.02
                )

            # -----------------------------------------------------------------
            # Zone 4 (INSIDE): Red Dashed "⚠ ANTI-PATTERNS & TRAPS" Sub-Box (H4 = 9.17 pt)
            # -----------------------------------------------------------------
            anti_top_y = z3_top_y - z3_h - gap_z
            anti_bot_y = ry + pad_bot
            anti_box = FancyBboxPatch(
                (x_left, anti_bot_y), inner_w, anti_h,
                boxstyle="round,pad=0.0,rounding_size=0.0022",
                facecolor="#FFF1F2",
                edgecolor="#E11D48",
                linewidth=1.15,
                linestyle="--"
            )
            ax.add_patch(anti_box)

            ahdr_h = anti_h * 0.24
            ahdr_box = FancyBboxPatch(
                (x_left + 0.0004, anti_top_y - ahdr_h), inner_w - 0.0008, ahdr_h,
                boxstyle="round,pad=0.0,rounding_size=0.0016",
                facecolor="#FFE4E6",
                edgecolor="#FECDD3",
                linewidth=0.50
            )
            ax.add_patch(ahdr_box)
            ax.text(
                x_left + inner_w / 2, anti_top_y - ahdr_h * 0.52,
                "⚠ ANTI-PATTERNS & TRAPS",
                fontsize=H4,
                fontweight="bold",
                color="#9F1239",
                va="center", ha="center"
            )

            abody_top_y = anti_top_y - ahdr_h
            abody_h = anti_h - ahdr_h
            arow_h = abody_h / 2.0
            acol_w = inner_w / 2.0

            ax.plot(
                [x_left + acol_w, x_left + acol_w],
                [anti_bot_y + 0.0006, abody_top_y - 0.0006],
                color="#FDA4AF", linewidth=0.55
            )
            ax.plot(
                [x_left + 0.0010, x_left + inner_w - 0.0010],
                [anti_bot_y + arow_h, anti_bot_y + arow_h],
                color="#FDA4AF", linewidth=0.50
            )

            for idx_a, akw in enumerate(anti_list[:4]):
                ar = idx_a // 2
                ac = idx_a % 2
                tx = x_left + ac * acol_w + 0.0008
                ty = abody_top_y - (ar + 0.5) * arow_h
                ax.text(
                    tx, ty,
                    textwrap.fill(f"✕ {akw}", width=19),
                    fontsize=H4,
                    fontweight="bold",
                    color="#881337",
                    va="center", ha="left",
                    linespacing=1.02
                )

    fig.savefig(OUT_DEV_PNG, dpi=300, facecolor=fig.get_facecolor())
    fig.savefig(OUT_DEV_PDF, format="pdf", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved: {OUT_DEV_PNG} ({OUT_DEV_PNG.stat().st_size:,} bytes)")
    print(f"Saved: {OUT_DEV_PDF} ({OUT_DEV_PDF.stat().st_size:,} bytes)")


def render_mobile_agent_anatomy_chart():
    """
    Smartphone Landscape Mini Chart (26.0 x 12.0 in @ 300 DPI — exact 19.5:9 Mobile Landscape)
    scaled proportionally by (26.0 / 46.8 = 5/9) from the H2 = 24.00 pt Golden Ratio hierarchy:
      • M_H0 = H0 * (26.0 / 46.8) ≈ 34.91 pt
      • M_H1 = H1 * (26.0 / 46.8) ≈ 21.57 pt
      • M_H2 = H2 * (26.0 / 46.8) ≈ 13.33 pt
      • M_H3 = H3 * (26.0 / 46.8) ≈  8.24 pt
      • M_H4 = H4 * (26.0 / 46.8) ≈  5.09 pt
    """
    plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]

    SCALE = 26.0 / 46.8
    M_H2 = 24.0 * SCALE
    M_H1 = M_H2 * PHI
    M_H0 = M_H1 * PHI
    M_H3 = M_H2 / PHI
    M_H4 = M_H3 / PHI

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
        0.012, hdr_y + hdr_h * 0.67,
        "ANATOMY OF AI AGENTS 2026",
        fontsize=M_H0, fontweight="bold", color="#FFFFFF", va="center", ha="left"
    )
    ax.text(
        0.013, hdr_y + hdr_h * 0.28,
        "www.arianprabowo.com · 1. Silicon → 10. Swarms × 4 Organisms",
        fontsize=M_H2, fontweight="bold", color="#38BDF8", va="center", ha="left"
    )

    ax.plot(
        [0.488, 0.488], [hdr_y + hdr_h * 0.20, hdr_y + hdr_h * 0.92],
        color="#334155", linewidth=1.2
    )

    ax.text(
        0.496, hdr_y + hdr_h * 0.56,
        "① COLUMNS (1 → 10): 1. Silicon → 2. Python → 3. Data → 4. Pre-Train → 5. SFT → 6. Post-Train → 7. Test-Time → 8. Context → 9. Harness → 10. Swarms\n"
        "② ROWS (4 ORGANISMS): Core LLM Spine + Separated RAG, Multimodal & Embodied Organisms\n"
        "③ INSIDE EVERY CELL: Flagship Pill (H2) + Checkpoints (H3) + Core Stack & Red ⚠ ANTI-PATTERNS Box (H4)",
        fontsize=M_H3, fontweight="bold", color="#FEF08A", va="center", ha="left",
        linespacing=1.18
    )

    ax.plot(
        [0.010, 0.990], [hdr_y + hdr_h * 0.16, hdr_y + hdr_h * 0.16],
        color="#1E293B", linewidth=0.9
    )

    ax.text(
        0.500, hdr_y + hdr_h * 0.075,
        f"*Based on Roitman 'The Hitchhiker's Guide to Agentic AI' (arXiv:2606.24937, June 2026) · Arian Prabowo · {LAST_UPDATED_STR}",
        fontsize=M_H4, fontweight="bold", color="#94A3B8", va="center", ha="center"
    )

    left_x0 = 0.004
    left_w = 0.080
    col_gap = 0.0024
    active_x0 = left_x0 + left_w + col_gap
    n_stages = len(STACK_STAGES)
    stage_col_w = (0.996 - active_x0 - (n_stages - 1) * col_gap) / n_stages

    def get_col_x(s_idx: int) -> float:
        return active_x0 + s_idx * (stage_col_w + col_gap)

    col_hdr_y = 0.778
    col_hdr_h = 0.124

    corner_box = FancyBboxPatch(
        (left_x0, col_hdr_y), left_w, col_hdr_h,
        boxstyle="round,pad=0.0,rounding_size=0.004",
        facecolor="#0F172A", edgecolor="#334155", linewidth=1.3
    )
    ax.add_patch(corner_box)
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.74,
        "ANATOMY",
        fontsize=M_H1, fontweight="bold", color="#FFFFFF", va="center", ha="center"
    )
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.43,
        "1 → 10 Stages",
        fontsize=M_H2, fontweight="bold", color="#FEF08A", va="center", ha="center"
    )
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.16,
        "LLM · RAG · Multimodal\n· Embodied (+ ⚠ Traps)",
        fontsize=M_H4, fontweight="bold", color="#5EEAD4", va="center", ha="center",
        linespacing=1.06
    )

    for s_idx, st in enumerate(STACK_STAGES):
        lx = get_col_x(s_idx)
        st_num = st["stage"]

        lbox_body = FancyBboxPatch(
            (lx, col_hdr_y), stage_col_w, col_hdr_h,
            boxstyle="round,pad=0.0,rounding_size=0.004",
            facecolor="#0F172A",
            edgecolor="#334155",
            linewidth=1.3
        )
        ax.add_patch(lbox_body)

        inset_b = 0.0012
        banner_h = col_hdr_h * 0.64
        lbox_top = FancyBboxPatch(
            (lx + inset_b, col_hdr_y + col_hdr_h - banner_h - inset_b),
            stage_col_w - 2 * inset_b, banner_h,
            boxstyle="round,pad=0.0,rounding_size=0.003",
            facecolor="#1E293B",
            edgecolor=st["accent"],
            linewidth=1.2
        )
        ax.add_patch(lbox_top)

        b_top_y = col_hdr_y + col_hdr_h - inset_b
        bar_total_w = stage_col_w - 0.0080
        bar_gap = 0.0006
        seg_w = (bar_total_w - 9 * bar_gap) / 10.0
        seg_h = banner_h * 0.09
        bar_x_start = lx + 0.0040
        bar_y = b_top_y - banner_h * 0.11 - seg_h / 2.0
        for b_i in range(10):
            bx_i = bar_x_start + b_i * (seg_w + bar_gap)
            is_lit = b_i < st_num
            seg_patch = FancyBboxPatch(
                (bx_i, bar_y), seg_w, seg_h,
                boxstyle="round,pad=0.0,rounding_size=0.0008",
                facecolor=st["accent"] if is_lit else "#334155",
                edgecolor=st["accent"] if is_lit else "#475569",
                linewidth=0.40
            )
            ax.add_patch(seg_patch)

        ax.text(
            lx + stage_col_w / 2, b_top_y - banner_h * 0.43,
            STAGE_H1_TITLES[st_num],
            fontsize=M_H1,
            fontweight="bold",
            color="#FFFFFF",
            va="center", ha="center"
        )

        ax.text(
            lx + stage_col_w / 2, b_top_y - banner_h * 0.81,
            textwrap.fill(STAGE_FULL_NAMES[st_num], width=36),
            fontsize=M_H4,
            fontweight="bold",
            color="#FEF08A",
            va="center", ha="center",
            linespacing=1.00
        )

        body_avail_h = col_hdr_h - banner_h - inset_b
        bullet_body = f"• {st['core_unit']}\n• {st['book_ref']}"
        ax.text(
            lx + stage_col_w / 2,
            col_hdr_y + body_avail_h * 0.50,
            bullet_body,
            fontsize=M_H4,
            fontweight="bold",
            color="#93C5FD",
            va="center",
            ha="center",
            linespacing=1.08,
        )

    top_y = 0.772
    row_h = 0.1865
    spine_sep_gap = 0.0075
    row_gap = 0.0042

    row_geoms = [
        (top_y - 1 * row_h, row_h),
        (top_y - 2 * row_h - spine_sep_gap, row_h),
        (top_y - 3 * row_h - spine_sep_gap - 1 * row_gap, row_h),
        (top_y - 4 * row_h - spine_sep_gap - 2 * row_gap, row_h),
    ]

    sep_y = top_y - row_h - spine_sep_gap * 0.50
    ax.plot(
        [left_x0, 0.996], [sep_y, sep_y],
        color="#0D9488", linewidth=1.6, linestyle=(0, (6, 3)), alpha=0.85
    )

    for r_idx, org in enumerate(ORGANISMS):
        ry, rh = row_geoms[r_idx]

        rbox_body = FancyBboxPatch(
            (left_x0, ry), left_w, rh,
            boxstyle="round,pad=0.0,rounding_size=0.004",
            facecolor="#0F172A", edgecolor=org["cell_edge"], linewidth=1.4
        )
        ax.add_patch(rbox_body)

        inset_r = 0.0014
        rbanner_h = rh * 0.54
        rbox_top = FancyBboxPatch(
            (left_x0 + inset_r, ry + rh - rbanner_h - inset_r),
            left_w - 2 * inset_r, rbanner_h,
            boxstyle="round,pad=0.0,rounding_size=0.003",
            facecolor=org["hdr_bg"], edgecolor="#FFFFFF", linewidth=0.9
        )
        ax.add_patch(rbox_top)

        rb_top_y = ry + rh - inset_r
        ax.text(
            left_x0 + left_w / 2, rb_top_y - rbanner_h * 0.13,
            org["badge"],
            fontsize=M_H4, fontweight="bold", color="#FEF08A", va="center", ha="center"
        )
        ax.text(
            left_x0 + left_w / 2, rb_top_y - rbanner_h * 0.44,
            org["short_name"],
            fontsize=M_H1,
            fontweight="bold", color="#FFFFFF", va="center", ha="center"
        )
        ax.text(
            left_x0 + left_w / 2, rb_top_y - rbanner_h * 0.80,
            textwrap.fill(org["full_name"], width=24),
            fontsize=M_H4,
            fontweight="bold", color="#E2E8F0", va="center", ha="center",
            linespacing=0.98
        )

        body_avail_h = rh - rbanner_h - inset_r
        ax.text(
            left_x0 + left_w / 2,
            ry + body_avail_h * 0.68,
            org["desc"],
            fontsize=M_H4,
            fontweight="bold",
            color="#F8FAFC",
            va="center",
            ha="center",
            linespacing=1.04,
        )
        ax.text(
            left_x0 + left_w / 2,
            ry + body_avail_h * 0.22,
            org["bullets"],
            fontsize=M_H4,
            fontweight="bold",
            color="#93C5FD",
            va="center",
            ha="center",
            linespacing=1.04,
        )

        for s_idx, st in enumerate(STACK_STAGES):
            cx = get_col_x(s_idx)
            cw = stage_col_w

            cell_data = st["cells"][org["key"]]
            h2_pill_str = cell_data["h2_pill"]
            h3_pills = cell_data["h3_pills"]
            mid_norm = cell_data["normal"]
            anti_list = cell_data["anti"]

            cbox = FancyBboxPatch(
                (cx, ry), cw, rh,
                boxstyle="round,pad=0.0,rounding_size=0.004",
                facecolor=org["cell_bg"],
                edgecolor=org["cell_edge"],
                linewidth=1.2
            )
            ax.add_patch(cbox)

            pad_x = 0.0016
            pad_top = 0.0024
            pad_bot = 0.0022
            inner_w = cw - 2 * pad_x
            x_left = cx + pad_x

            gap_z = 0.0016
            avail_h = rh - pad_top - pad_bot - 3 * gap_z
            z1_h = avail_h * 0.16
            z2_h = avail_h * 0.22
            z3_h = avail_h * 0.31
            anti_h = avail_h * 0.31

            z1_top_y = ry + rh - pad_top
            z1_bot_y = z1_top_y - z1_h
            p_h2 = FancyBboxPatch(
                (x_left, z1_bot_y), inner_w, z1_h,
                boxstyle="round,pad=0.0,rounding_size=0.0024",
                facecolor=org["h2_bg"],
                edgecolor=org["pill_edge"],
                linewidth=0.95
            )
            ax.add_patch(p_h2)
            ax.text(
                x_left + inner_w / 2, z1_bot_y + z1_h / 2,
                h2_pill_str,
                fontsize=M_H2,
                fontweight="bold",
                color=org["h2_txt"],
                va="center", ha="center"
            )

            z2_top_y = z1_bot_y - gap_z
            pill_gap = 0.0014
            ph3 = (z2_h - pill_gap) / 2.0
            for idx_p, kw in enumerate(h3_pills[:2]):
                py = z2_top_y - (idx_p + 1) * ph3 - idx_p * pill_gap
                pill = FancyBboxPatch(
                    (x_left, py), inner_w, ph3,
                    boxstyle="round,pad=0.0,rounding_size=0.0020",
                    facecolor=org["h3_bg"],
                    edgecolor=org["pill_edge"],
                    linewidth=0.80
                )
                ax.add_patch(pill)
                ax.text(
                    x_left + inner_w / 2, py + ph3 / 2,
                    kw,
                    fontsize=M_H3,
                    fontweight="bold",
                    color=org["h3_txt"],
                    va="center", ha="center"
                )

            z3_top_y = z2_top_y - z2_h - gap_z
            t2_row_h = z3_h / 3.0
            t2_col_w = inner_w / 2.0

            ax.plot(
                [x_left + t2_col_w, x_left + t2_col_w],
                [z3_top_y - z3_h + 0.0006, z3_top_y - 0.0006],
                color=org["cell_edge"], linewidth=0.50, alpha=0.35
            )

            for idx_2, kw in enumerate(mid_norm[:6]):
                mr = idx_2 // 2
                mc = idx_2 % 2
                tx = x_left + mc * t2_col_w + 0.0009
                ty = z3_top_y - (mr + 0.5) * t2_row_h
                ax.text(
                    tx, ty,
                    textwrap.fill(kw, width=19),
                    fontsize=M_H4,
                    fontweight="bold",
                    color=org["t2_txt"],
                    va="center", ha="left",
                    linespacing=1.02
                )

            anti_top_y = z3_top_y - z3_h - gap_z
            anti_bot_y = ry + pad_bot
            anti_box = FancyBboxPatch(
                (x_left, anti_bot_y), inner_w, anti_h,
                boxstyle="round,pad=0.0,rounding_size=0.0022",
                facecolor="#FFF1F2",
                edgecolor="#E11D48",
                linewidth=0.95,
                linestyle="--"
            )
            ax.add_patch(anti_box)

            ahdr_h = anti_h * 0.24
            ahdr_box = FancyBboxPatch(
                (x_left + 0.0004, anti_top_y - ahdr_h), inner_w - 0.0008, ahdr_h,
                boxstyle="round,pad=0.0,rounding_size=0.0016",
                facecolor="#FFE4E6",
                edgecolor="#FECDD3",
                linewidth=0.40
            )
            ax.add_patch(ahdr_box)
            ax.text(
                x_left + inner_w / 2, anti_top_y - ahdr_h * 0.52,
                "⚠ ANTI-PATTERNS & TRAPS",
                fontsize=M_H4,
                fontweight="bold",
                color="#9F1239",
                va="center", ha="center"
            )

            abody_top_y = anti_top_y - ahdr_h
            abody_h = anti_h - ahdr_h
            arow_h = abody_h / 2.0
            acol_w = inner_w / 2.0

            ax.plot(
                [x_left + acol_w, x_left + acol_w],
                [anti_bot_y + 0.0006, abody_top_y - 0.0006],
                color="#FDA4AF", linewidth=0.45
            )
            ax.plot(
                [x_left + 0.0010, x_left + inner_w - 0.0010],
                [anti_bot_y + arow_h, anti_bot_y + arow_h],
                color="#FDA4AF", linewidth=0.40
            )

            for idx_a, akw in enumerate(anti_list[:4]):
                ar = idx_a // 2
                ac = idx_a % 2
                tx = x_left + ac * acol_w + 0.0008
                ty = abody_top_y - (ar + 0.5) * arow_h
                ax.text(
                    tx, ty,
                    textwrap.fill(f"✕ {akw}", width=19),
                    fontsize=M_H4,
                    fontweight="bold",
                    color="#881337",
                    va="center", ha="left",
                    linespacing=1.02
                )

    fig.savefig(OUT_MOBILE_PNG, dpi=300, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved: {OUT_MOBILE_PNG} ({OUT_MOBILE_PNG.stat().st_size:,} bytes)")


def write_agent_anatomy_markdown():
    lines = [
        f"![Anatomy of AI Agents 2026 — 10 Stages x 4 Organisms Megachart]({OUT_DEV_PNG.name})",
        "",
        f"![Anatomy of AI Agents 2026 — Mobile Landscape Mini Chart]({OUT_MOBILE_PNG.name})",
        "",
        "# ANATOMY OF AI AGENTS 2026 (`10 Stages: 1. Silicon → 10. Swarms` × `4 Organisms: LLM · RAG · Multimodal · Embodied`)",
        "",
        "> **What actually runs under the hood of an autonomous AI agent in 2026? Trace left to right across the 10 stages (`1. Silicon`, `2. Python`, `3. Data`, `4. Pre-Train`, `5. SFT`, `6. Post-Train`, `7. Test-Time`, `8. Context`, `9. Harness`, `10. Swarms`) and top to bottom across the 4 distinct organisms (`LLM`, `RAG`, `Multimodal`, `Embodied`), with production `⚠ ANTI-PATTERNS & TRAPS` embedded directly inside every cell.**  ",
        f"> **How to Read ([www.arianprabowo.com](https://www.arianprabowo.com) · Based on Haggai Roitman's *The Hitchhiker's Guide to Agentic AI*, `arXiv:2606.24937` · <sub>`{LAST_UPDATED_STR}`</sub>):** **`① COLUMNS (1 → 10):`** Follow `1. Silicon → 10. Swarms` · **`② ROWS (4 ORGANISMS):`** Compare the `LLM` Core Spine against `RAG`, `Multimodal`, and `Embodied` · **`③ INSIDE EVERY CELL:`** Audit the Flagship Banner (`H2 = 24 pt`), Checkpoints (`H3 = 14.83 pt`), Core Stack (`H4 = 9.17 pt`), and Red **`⚠ ANTI-PATTERNS & TRAPS`** box (`H4 = 9.17 pt`).",
        "",
        "---",
        "",
        "## 1. Complete 10-Stage × 4-Organism Matrix Overview",
        "",
        "| Stage (`H1` Short Name · `H4` Full Name · Core Unit · Book Ref) | `LLM` (*Autoregressive Text, Code & Reasoning Language Models*) | `RAG` (*Hybrid Vector, Lexical & Graph Retrieval-Augmented Generation*) | `Multimodal` (*Vision, Audio, Speech, Video & Native Omni-Modal Models*) | `Embodied` (*GUI Computer Use, Physics World Models & VLA Robotics*) |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]

    for st in STACK_STAGES:
        st_num = st["stage"]
        col0 = (
            f"**{STAGE_H1_TITLES[st_num]}** — *{STAGE_FULL_NAMES[st_num]}*<br>"
            f"{st['desc']}<br>"
            f"• **{st['core_unit']}**<br>"
            f"• **{st['book_ref']}**"
        )
        row_cells = [col0]
        for org in ORGANISMS:
            d = st["cells"][org["key"]]
            h2_str = f"**`[{d['h2_pill']}]`**"
            h3_str = " · ".join(f"**{k}**" for k in d["h3_pills"])
            norm_str = " · ".join(d["normal"])
            anti_str = " · ".join(f"**`⚠ {k}`**" for k in d["anti"])
            parts = [p for p in (h2_str, h3_str, norm_str, anti_str) if p]
            row_cells.append("<br><br>".join(parts))
        lines.append("| " + " | ".join(row_cells) + " |")

    lines.extend([
        "",
        "---",
        "",
        "## 2. Stage-by-Stage Breakdown (`1. Silicon` → `10. Swarms` Across All 4 Organisms)",
        "",
    ])

    for st in STACK_STAGES:
        st_num = st["stage"]
        lines.extend([
            f"### {STAGE_H1_TITLES[st_num]} — {STAGE_FULL_NAMES[st_num]}",
            "",
            f"{st['desc']}",
            "",
            f"* **Core Unit of Compute / State:** `{st['core_unit']}`",
            f"* **Primary Reference (`arXiv:2606.24937`):** {st['book_ref']}",
            "",
            "| Organism (`Short` — *Full Name*) | Flagship Banner (`H2 = 24pt`) | Checkpoints (`H3 = 14.83pt`) | Core Stack (`H4 = 9.17pt`) | Inner `⚠ Anti-Patterns & Traps` (`H4 = 9.17pt`) |",
            "| :--- | :--- | :--- | :--- | :--- |",
        ])
        for org in ORGANISMS:
            d = st["cells"][org["key"]]
            h2_s = f"**`{d['h2_pill']}`**"
            h3_s = ", ".join(f"**`{k}`**" for k in d["h3_pills"])
            nm_s = ", ".join(f"`{k}`" for k in d["normal"])
            an_s = ", ".join(f"**`✕ {k}`**" for k in d["anti"])
            lines.append(
                f"| **{org['short_name']}** (*{org['full_name']}*) | {h2_s} | {h3_s} | {nm_s} | {an_s} |"
            )
        lines.append("")

    content = "\n".join(lines)
    OUT_MD.write_text(content, encoding="utf-8")
    print(f"Saved: {OUT_MD} ({OUT_MD.stat().st_size:,} bytes)")


if __name__ == "__main__":
    render_desktop_agent_anatomy_megachart()
    render_mobile_agent_anatomy_chart()
    write_agent_anatomy_markdown()
