#!/usr/bin/env python3
"""
Generate the 2026 Agent Anatomy Megachart ("ANATOMY OF AI AGENTS 2026"):
  1. dev/anatomy_of_AI_agents_2026/anatomy_of_AI_agents_2026.png        (46.8 x 21.6 in @ 300 DPI — ISO A0-Width 19.5:9 Landscape)
  2. dev/anatomy_of_AI_agents_2026/anatomy_of_AI_agents_2026.pdf        (Vector PDF)
  3. dev/anatomy_of_AI_agents_2026/anatomy_of_AI_agents_2026_mobile.png (26.0 x 12.0 in @ 300 DPI — Mobile 19.5:9 Landscape)
  4. dev/anatomy_of_AI_agents_2026/2026 11 07 anatomy_of_AI_agents_2026.md

Structure:
  • Columns (Left -> Right, 10 Stages):
      1. Silicon       — Physical Compute Silicon, GPU Clusters, HBM3e Memory & Interconnect Fabrics
      2. Python        — Python Runtimes, Package Managers, Virtual Environments & Tensor Compilers
      3. Data          — Web & Code Corpora, Subword Tokenization & Curation Pipelines
      4. Pre-Training  — Foundation Model Architectures, Sparse MoE Routing & Self-Supervised Pre-Training
      5. SFT           — Supervised Fine-Tuning, Instruction Templates, Sequence Packing & LoRA Adapters
      6. Post-Training — Preference Alignment (RLHF/DPO) & Verifiable-Reward Reinforcement Learning (RLVR/GRPO)
      7. Test-Time     — Test-Time Compute Scaling, System-2 Chain-of-Thought Reasoning & Tree Search
      8. Context       — Context Engineering, Four-Tier Memory, Tool Calling, MCP & Skills
      9. Harness       — Single-Agent Harness Engineering, Observe-Decide-Act Loops & Stateful Graph Workflows
     10. Multi-Agent   — Multi-Agent Orchestration, Hierarchical Swarms, A2A Protocols & Shared State
  • Rows (Top -> Bottom, 4 Organisms — NO generic Pillars/Anti-Pattern rows):
      1. LLM           — Autoregressive Text, Code & Reasoning Language Models (Primary Spine)
      --- Detached Organism Boundary ---
      2. RAG           — Hybrid Vector, Lexical & Graph Retrieval-Augmented Generation
      3. Multimodal    — Vision, Audio, Speech, Video & Native Omni-Modal Models
      4. Embodied AI   — GUI Computer Use, Physics World Models & VLA Robotics
  • Inside Every Cell (40 Cells):
      - Tier 1 (H2): 3 Flagship Pills (Core Architecture, Flagship Stack, Scaling/Verification)
      - Tier 2 (H3): 3x2 = 6 Core Mechanisms, Packages, Protocols & Benchmarks
      - Tier 3 (H4): 1x3 = 3 Granular Specs, Flags & Formulas
      - Inner Anti-Patterns Box (H3/H4): Red dashed "⚠ ANTI-PATTERNS & TRAPS" sub-card INSIDE the bottom of every cell (2x2 = 4 failure modes)
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
# 1. Four Organism Rows (Short Name <= 2 words, Full Name <= 10 words)
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
        "h1_bg": "#D1FAE5",
        "h1_txt": "#064E3B",
        "pill_edge": "#10B981",
        "t2_bg": "#F0FDF4",
        "t2_txt": "#065F46",
        "t3_bg": "#E2E8F0",
        "t3_txt": "#1E293B",
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
        "h1_bg": "#CCFBF1",
        "h1_txt": "#134E4A",
        "pill_edge": "#14B8A6",
        "t2_bg": "#F0FDFA",
        "t2_txt": "#115E59",
        "t3_bg": "#E2E8F0",
        "t3_txt": "#1E293B",
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
        "h1_bg": "#EDE9FE",
        "h1_txt": "#4C1D95",
        "pill_edge": "#8B5CF6",
        "t2_bg": "#FAF5FF",
        "t2_txt": "#5B21B6",
        "t3_bg": "#E2E8F0",
        "t3_txt": "#1E293B",
    },
    {
        "key": "embodied",
        "short_name": "Embodied AI",
        "full_name": "GUI Computer Use, Physics World Models & VLA Robotics",
        "badge": "ORGANISM · ACTION",
        "desc": "Browser/OS GUI Control,\n3D Physics Simulators, World\nModels & VLA Robot Policies",
        "bullets": "• 1–3: Edge NPU / Isaac / Teleop\n• 4–7: VLA π0 / ACT / Sim2Real\n• 8–10: 3DGS / OSWorld / Fleets",
        "hdr_bg": "#1D4ED8",
        "cell_bg": "#EFF6FF",
        "cell_edge": "#2563EB",
        "h1_bg": "#DBEAFE",
        "h1_txt": "#1E3A8A",
        "pill_edge": "#3B82F6",
        "t2_bg": "#F8FAFC",
        "t2_txt": "#1E40AF",
        "t3_bg": "#E2E8F0",
        "t3_txt": "#1E293B",
    },
]

for _org in ORGANISMS:
    _sw = len(_org["short_name"].split())
    _fw = len(_org["full_name"].split())
    assert _sw <= 2, f"Organism short_name > 2 words: {_org['short_name']}"
    assert _fw <= 10, f"Organism full_name > 10 words: {_org['full_name']}"

# -----------------------------------------------------------------------------
# 2. Ten Stages (Short Name <= 2 words, Full Name <= 10 words) x 4 Organisms
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
        "desc": "GPUs/TPUs/NPUs, HBM3e vs. SRAM hierarchy, CUDA/Triton kernels, and NVLink/InfiniBand fabrics.",
        "core_unit": "Core Unit: FLOPs, HBM Bytes & CUDA Warps",
        "book_ref": "Ch. 1.6, 2.3, 11.10–14, 30.5 (GPUs & Kernels)",
        "cells": {
            "llm": {
                "h1": [
                    "NVIDIA H100 / H200 / Blackwell B200",
                    "HBM3e vs. On-Chip SRAM Hierarchy",
                    "FlashAttention-3 IO-Aware SRAM Tiling",
                ],
                "normal": [
                    "Google TPU v5p / v6e Trillium / v7",
                    "CUDA · OpenAI Triton · CUTLASS",
                    "FP8 (E4M3/E5M2) & Microscaling FP4",
                    "NVLink 5 (1.8 TB/s) & NVSwitch",
                    "Model FLOPs Utilization (MFU > 45%)",
                    "Prefill (Compute) vs. Decode (BW)",
                ],
                "small": [
                    "Streaming Multiprocessors (132 SMs)",
                    "400G/800G RoCEv2 & InfiniBand NDR",
                    "Confidential Compute GPU TEEs",
                ],
                "anti": [
                    "HBM Memory Bandwidth Wall (Decode)",
                    "CUDA Out-of-Memory (OOM) Crashes",
                    "Silent Tensor Core SDC Bit-Flips",
                    "Straggler GPU Halting 1,000 Nodes",
                ],
            },
            "rag": {
                "h1": [
                    "NVIDIA cuVS / RAFT GPU Vector Search",
                    "AVX-512 SIMD Distance Kernels",
                    "NVMe Gen5 DirectStorage DiskANN I/O",
                ],
                "normal": [
                    "GPU-Accelerated CAGRA Graph Index",
                    "Int8 / Binary Scalar & PQ Hardware",
                    "High-IOPS NVMe SSD Page Cache",
                    "RDMA Zero-Copy Index Sharding",
                    "Sub-10ms p99 Vector Query SLA",
                    "DRAM vs. SSD Tiered Memory Pool",
                ],
                "small": [
                    "L2 / Cosine / Inner-Product SIMD",
                    "GPUDirect Storage (GDS) DMA",
                    "HNSW Graph Traversal Cache Misses",
                ],
                "anti": [
                    "Random-Read SSD IOPS Thrashing",
                    "HNSW Graph Exceeding Host DRAM",
                    "PCIe Host-to-GPU Index Bottleneck",
                    "NUMA Cross-Socket Latency Spikes",
                ],
            },
            "multimodal": {
                "h1": [
                    "Hardware NVDEC / NVENC Video Codecs",
                    "ViT Patch Tensor-Core SRAM Tiling",
                    "Dedicated Audio DSP & Neural Engines",
                ],
                "normal": [
                    "Apple Silicon M4 Unified Memory",
                    "JPEG/HEVC Hardware Decode Pipelines",
                    "2D/3D Conv & DiT Attention Kernels",
                    "GPUDirect RDMA Camera/Video Ingest",
                    "Sub-200ms Voice-to-Voice Hardware SLA",
                    "4K Frame Buffer Bandwidth Budgeting",
                ],
                "small": [
                    "NVMM Zero-Copy Frame Buffers",
                    "BFloat16 ViT Patch Projection",
                    "Hardware Acoustic Echo Cancellation",
                ],
                "anti": [
                    "CPU-Bound Video Decode Starving GPU",
                    "4K Uncompressed Frame PCIe Saturation",
                    "Audio Codec Sample-Rate Clock Drift",
                    "Thermal Throttling on Continuous Video",
                ],
            },
            "embodied": {
                "h1": [
                    "NVIDIA Jetson Thor / Orin Edge SoCs",
                    "GPU PhysX / Warp Parallel Sim Kernels",
                    "1 kHz Real-Time Deterministic Bus",
                ],
                "normal": [
                    "LiDAR / Depth / IMU Sensor ISP Silicon",
                    "On-Device INT4/FP8 NPU Inference",
                    "EtherCAT / CAN-FD Actuator Bus",
                    "Hardware Watchdog & E-Stop Relays",
                    "10,000x Parallel Sim Env Throughput",
                    "Sub-5ms Sensor-to-Actuator Loop Latency",
                ],
                "small": [
                    "PREEMPT_RT Real-Time Linux Kernel",
                    "MIPI CSI-2 Multi-Camera Deserializers",
                    "Battery Watt-Hour Compute Envelopes",
                ],
                "anti": [
                    "Edge Thermal Throttling Mid-Trajectory",
                    "GC / OS Jitter Breaking 1 kHz Control",
                    "USB/CSI Camera Frame Drop Desync",
                    "Sim-to-Real Contact Physics Mismatch",
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
        "desc": "Package managers (Homebrew, uv, conda, pip, venv), Python 3.12+, PyTorch, JAX, vLLM, and sandboxes.",
        "core_unit": "Core Unit: Wheels, Lockfiles, Tensors & Paged KV",
        "book_ref": "Ch. 1.24–25, 11.1–9, 21.5, 22.1–9 (Env & Runtime)",
        "cells": {
            "llm": {
                "h1": [
                    "Homebrew (brew) · uv · conda · pip · venv",
                    "Python 3.12+ · PyTorch 2.x · JAX · MLX",
                    "vLLM · SGLang · llama.cpp · Docker · E2B",
                ],
                "normal": [
                    "torch.compile (TorchInductor) & XLA",
                    "PagedAttention KV & Continuous Batch",
                    "pyproject.toml & uv.lock Reproducibility",
                    "E2B / Firecracker MicroVM Sandboxes",
                    "OS Sandboxing (Bubblewrap / Seatbelt)",
                    "TTFT / TPOT SLAs & Asyncio Event Loop",
                ],
                "small": [
                    "manylinux Wheels & CUDA ABI Tags",
                    "Speculative Decoding Draft-Verify",
                    "Outlines / XGrammar FSM Masking",
                ],
                "anti": [
                    "Python Dependency & CUDA ABI Hell",
                    "Unsandboxed Host RCE & rm -rf /",
                    "KV-Cache Fragmentation & Preemption",
                    "pip install Breaking flash-attn ABI",
                ],
            },
            "rag": {
                "h1": [
                    "FAISS · HNSWlib · LanceDB · PyArrow",
                    "psycopg3 (pgvector) · qdrant-client",
                    "Apache Arrow Zero-Copy Memory Tables",
                ],
                "normal": [
                    "rank-bm25 · tantivy · Pyserini Lexical",
                    "Parquet Columnar Storage & DuckDB",
                    "Async gRPC / HTTP/2 Connection Pools",
                    "ONNX Runtime / TensorRT Embed Serving",
                    "Memory-Mapped (mmap) Vector Segments",
                    "Connection Pool & Batch Upsert SLAs",
                ],
                "small": [
                    "pyarrow.Table Zero-Copy Slicing",
                    "SQLAlchemy / AsyncPG Vector Types",
                    "Protobuf / FlatBuffers Serialization",
                ],
                "anti": [
                    "GIL Lockup During CPU Token/Chunking",
                    "Pickle Deserialization RCE in Indexes",
                    "Unbounded Connection Pool Exhaustion",
                    "Pandas Copy-on-Write RAM Explosion",
                ],
            },
            "multimodal": {
                "h1": [
                    "torchvision · torchaudio · OpenCV",
                    "FFmpeg · PyAV · Pillow-SIMD · Decord",
                    "WebRTC · LiveKit · whisper.cpp · Kokoro",
                ],
                "normal": [
                    "NVIDIA DALI GPU Data Loading Pipeline",
                    "librosa · soundfile · Soxr Resampling",
                    "vLLM Multimodal & SGLang Vision Engine",
                    "WebSockets / RTP Real-Time Audio Streams",
                    "VAD (Silero) Turn-Detection Runtime",
                    "Frame-Sync Jitter Buffer Management",
                ],
                "small": [
                    "BGR-to-RGB Tensor Channel Ordering",
                    "Opus / PCM16 Streaming Audio Frames",
                    "EXIF Orientation Tag Normalization",
                ],
                "anti": [
                    "OpenCV BGR vs. RGB Silent Channel Bug",
                    "FFmpeg Zombie Subprocess Memory Leaks",
                    "Audio Buffer Underrun Pops & Glitches",
                    "Pillow Decompression Bomb DoS",
                ],
            },
            "embodied": {
                "h1": [
                    "ROS 2 (rclpy) · Gymnasium · MuJoCo",
                    "NVIDIA Isaac Lab · ManiSkill · Genesis",
                    "Playwright · CDP · PyAutoGUI · LeRobot",
                ],
                "normal": [
                    "ZeroMQ / CycloneDDS Pub-Sub Middleware",
                    "Headless Chromium / Xvfb Virtual Displays",
                    "Open3D · Trimesh · PyBullet Kinematics",
                    "Dockerized Browser & OS Sandboxes",
                    "Vectorized AsyncGym Env Stepping",
                    "Deterministic Seed & Replay Recording",
                ],
                "small": [
                    "URDF / MJCF Robot Description XML",
                    "Accessibility Tree (AXTree) Snapshots",
                    "6-DoF End-Effector Quaternion Math",
                ],
                "anti": [
                    "ROS 2 DDS Discovery Multicast Storms",
                    "Zombie Headless Browser RAM Leaks",
                    "Euler Angle Gimbal Lock in Control",
                    "Non-Deterministic Physics Step Drift",
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
        "desc": "Pre-training/post-training corpora, BPE/Tiktoken tokenizers, deduplication, filtering, and synthetic data.",
        "core_unit": "Core Unit: Corpora, Subword Tokens & Shards",
        "book_ref": "Ch. 1.2, 3.1, 3.3–3.5, 4.1, 30.2 (Data & Tokenizers)",
        "cells": {
            "llm": {
                "h1": [
                    "FineWeb-Edu · Dolma · The Stack v2",
                    "Byte-Level BPE · Tiktoken · SentencePiece",
                    "MinHash LSH Dedup & Quality Classifiers",
                ],
                "normal": [
                    "HF Datasets · Datatrove · NeMo Curator",
                    "Execution-Verified Code & Math Traces",
                    "Benchmark Decontamination (13-Gram)",
                    "PII, Secret & License Scrubbing",
                    "Vocabulary Size (128k–256k) & Fertility",
                    "Domain Curriculum & Annealing Mixes",
                ],
                "small": [
                    "cl100k / o200k Pre-Tokenization Regex",
                    "Canary String Injection & Filtering",
                    "Vendi Score & N-Gram Diversity",
                ],
                "anti": [
                    "Garbage-In Synthetic Model Collapse",
                    "Test-Set Contamination Mirage",
                    "Tokenizer Glitch Tokens & Fertility Bloat",
                    "PII & API Keys Baked into Weights",
                ],
            },
            "rag": {
                "h1": [
                    "Docling · Marker · Unstructured PDF ETL",
                    "Semantic, Contextual & AST Code Chunking",
                    "Metadata Schema, ACLs & Temporal Tags",
                ],
                "normal": [
                    "Anthropic Contextual Chunk Headers",
                    "Table-to-Markdown & Layout Extraction",
                    "Hard-Negative Triplet Mining (Q, d+, d-)",
                    "Incremental CDC Document Sync",
                    "Near-Duplicate Chunk Deduplication",
                    "Golden QA Evaluation Set Curation",
                ],
                "small": [
                    "256–512 Token Overlap Sliding Windows",
                    "Tree-sitter AST Function Boundary Split",
                    "SHA-256 Content-Addressable Chunk IDs",
                ],
                "anti": [
                    "Mid-Sentence / Mid-Table Naive Chunking",
                    "Multi-Column PDF Reading-Order Scramble",
                    "Stale Deleted Docs Remaining in Index",
                    "Missing Document-Level RBAC Metadata",
                ],
            },
            "multimodal": {
                "h1": [
                    "DataComp · LAION · OBELICS Interleaved",
                    "OCR Document, Chart & UI Grounding Sets",
                    "Whisper ASR & Diarized Speech Corpora",
                ],
                "normal": [
                    "CLIPScore & Aesthetic Quality Filtering",
                    "Synthetic VLM Recaptioning (ShareGPT4V)",
                    "Scene-Cut Video Clip Segmentation",
                    "Discrete Audio Codec Tokens (EnCodec/Mimi)",
                    "Face Blurring & C2PA Provenance Scrub",
                    "Bounding-Box & Set-of-Mark Annotations",
                ],
                "small": [
                    "Dynamic Aspect-Ratio AnyRes Tiling",
                    "Forced Phoneme-Timestamp Alignment",
                    "NSFW & Watermark Classifier Gates",
                ],
                "anti": [
                    "Alt-Text Noise & Mismatched Captions",
                    "OCR Hallucination on Low-DPI Scans",
                    "Biased Demographic & Cultural Corpora",
                    "Audio Background Noise & Crosstalk Leak",
                ],
            },
            "embodied": {
                "h1": [
                    "Open X-Embodiment · DROID Robot Datasets",
                    "Mind2Web · OSWorld · Rico GUI Traces",
                    "Ego4D · Something-Something Video Logs",
                ],
                "normal": [
                    "ALOHA / VR Teleoperation Demonstrations",
                    "DOM + Screenshot + Action Triplets",
                    "3D Point-Cloud & Depth-Map Alignment",
                    "Proprioceptive Joint-State Normalization",
                    "Success/Failure Trajectory Labeling",
                    "Domain-Randomized Sim Data Generation",
                ],
                "small": [
                    "RLDS / LeRobot Parquet Episode Format",
                    "Coordinate Normalization [0, 1000]",
                    "Camera Extrinsics & Intrinsics Calibration",
                ],
                "anti": [
                    "Teleoperator Hesitation & Suboptimal Demos",
                    "Coordinate Resolution Scaling Mismatch",
                    "Action-Space Embodiment Incompatibility",
                    "Unlogged Environment State Confounders",
                ],
            },
        },
    },
    # =========================================================================
    # 4. Pre-Training
    # =========================================================================
    {
        "stage": 4,
        "short_name": "Pre-Training",
        "full_name": "Foundation Model Architectures, Sparse MoE Routing & Self-Supervised Pre-Training",
        "accent": "#A78BFA",
        "desc": "Transformer/MoE/hybrid architectures, attention (GQA, MLA), RoPE, next-token pre-training, and scaling laws.",
        "core_unit": "Core Unit: Transformer Blocks, MoE & Base Weights",
        "book_ref": "Ch. 1.1, 2.2, 3.1, 11.1–9, 30.1 (Architecture & Pre-Training)",
        "cells": {
            "llm": {
                "h1": [
                    "Transformer · Sparse MoE · GQA / MLA",
                    "Megatron-LM · DeepSpeed · TorchTitan",
                    "Chinchilla & Inference-Aware Scaling Laws",
                ],
                "normal": [
                    "Llama 4 · Qwen 3 · DeepSeek-V3 Base",
                    "Hybrid Linear Attention (Mamba/DeltaNet)",
                    "Pre-Norm RMSNorm, SwiGLU & RoPE/YaRN",
                    "3D Parallelism (DP/FSDP + TP + PP + EP)",
                    "Loss-Spike Recovery & Z-Loss Stability",
                    "Base Perplexity (Bits-per-Byte) & NIAH",
                ],
                "small": [
                    "Aux-Loss-Free MoE Load Balancing",
                    "muP Maximal Update Parametrization",
                    "Async Distributed Checkpoint Shards",
                ],
                "anti": [
                    "Catastrophic Loss Spikes & NaN Divergence",
                    "MoE Routing Collapse (Expert Starvation)",
                    "Pipeline Bubble & All-to-All Bottlenecks",
                    "RoPE Extrapolation Collapse Past Train Len",
                ],
            },
            "rag": {
                "h1": [
                    "Bi-Encoder Contrastive InfoNCE Training",
                    "BGE-M3 · NV-Embed-v2 · Cohere Embed v4",
                    "ColBERTv2 Late-Interaction MaxSim",
                ],
                "normal": [
                    "Matryoshka Representation Learning (MRL)",
                    "SPLADE Learned Sparse Lexical Expansion",
                    "In-Batch & Cross-GPU Negative Scaling",
                    "Bidirectional Attention Encoder Backbones",
                    "Multilingual Cross-Lingual Alignment",
                    "MTEB Retrieval & NDCG@10 Benchmarks",
                ],
                "small": [
                    "Temperature-Scaled Cosine Similarity",
                    "Dimension Truncation (1024 -> 256d)",
                    "Asymmetric Query/Passage Prefixes",
                ],
                "anti": [
                    "Embedding Space Anisotropy Collapse",
                    "False-Negative Collisions in Large Batches",
                    "Out-of-Domain Lexical Acronym Blindness",
                    "Fixed 512-Token Encoder Context Truncation",
                ],
            },
            "multimodal": {
                "h1": [
                    "SigLIP-2 · OpenCLIP · DINOv2 Vision",
                    "Native Early-Fusion Omni (GPT-4o / Gemini)",
                    "Flow-Matching & DiT Diffusion Backbones",
                ],
                "normal": [
                    "Qwen2.5-VL · Pixtral · InternVL3",
                    "MLP / Perceiver / Q-Former Projectors",
                    "3D Spatio-Temporal Video RoPE",
                    "RVQ Neural Audio Codecs (Mimi / SoundStream)",
                    "Contrastive + Captioning Joint Pre-Train",
                    "Zero-Shot ImageNet / VQA / ASR Evals",
                ],
                "small": [
                    "14x14 / 16x16 ViT Patch Embeddings",
                    "Sigmoid Pairwise Contrastive Loss",
                    "Classifier-Free Guidance (CFG) Dropout",
                ],
                "anti": [
                    "Modality Competition Degrading Text IQ",
                    "Bag-of-Patches Spatial Blindness",
                    "Quadratic ViT Token Explosion on 4K",
                    "Small-Text & Fine-Line Patch Blur",
                ],
            },
            "embodied": {
                "h1": [
                    "Vision-Language-Action (π0 · OpenVLA · RT-2)",
                    "World Models (V-JEPA 2 · Cosmos · Genie 2)",
                    "Diffusion Policy & Flow-Matching Actions",
                ],
                "normal": [
                    "Octo · CrossFormer Multi-Embodiment Base",
                    "Latent Dynamics & Next-Frame Prediction",
                    "3D Point-Cloud & Voxel Encoders",
                    "Discrete Action Bins vs. Continuous Heads",
                    "Cross-Robot Morphology Tokenization",
                    "Sim-to-Sim Zero-Shot Transfer Evals",
                ],
                "small": [
                    "SE(3) Equivariant Pose Representations",
                    "Video-to-Action Latent Conditioning",
                    "Proprioceptive State History Window",
                ],
                "anti": [
                    "Causal Confusion (Spurious Correlations)",
                    "World Model Physics Hallucination",
                    "Multi-Modal Action Averaging Freeze",
                    "Camera Viewpoint Shift Fragility",
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
        "desc": "Instruction tuning, ChatML formatting, tool-call/reasoning trace SFT, loss masking, and PEFT (LoRA/DoRA).",
        "core_unit": "Core Unit: Chat Templates, Packed Sequences & LoRA",
        "book_ref": "Ch. 1.8, 3.2, 7.6, 9.4, 30.2 (SFT, Packing & PEFT Adapters)",
        "cells": {
            "llm": {
                "h1": [
                    "ChatML Templates & Completion-Only Masking",
                    "HF TRL (SFTTrainer) · Axolotl · Unsloth",
                    "PEFT Adapters: LoRA · QLoRA · DoRA",
                ],
                "normal": [
                    "LLaMA-Factory · Torchtune · Liger-Kernel",
                    "Multipack Sequence Packing + Position IDs",
                    "Tool-Use & Multi-Turn Trajectory SFT",
                    "Cold-Start Chain-of-Thought Trace SFT",
                    "MergeKit (SLERP / TIES / DARE Merging)",
                    "IFEval Instruction-Following & Format Audit",
                ],
                "small": [
                    "Mask Prompt Tokens (labels = -100)",
                    "QLoRA 4-Bit NF4 + Double Quantization",
                    "rsLoRA Rank-Stabilized Scaling (α/√r)",
                ],
                "anti": [
                    "Training on Prompt Tokens (Missing -100)",
                    "Chat Template EOS/BOS Mismatch Loops",
                    "Cross-Sample Attention Bleed in Packing",
                    "Catastrophic Forgetting & Sycophancy",
                ],
            },
            "rag": {
                "h1": [
                    "Cross-Encoder Reranker SFT (bge-reranker)",
                    "Domain-Adapted Embedding Fine-Tuning",
                    "Citation-Grounded QA SFT (RAFT)",
                ],
                "normal": [
                    "Retrieval-Augmented Fine-Tuning (RAFT)",
                    "Distractor-Document Robustness Tuning",
                    "Query-Rewriting & Decomposition SFT",
                    "Structured JSON / SQL Query Generation SFT",
                    "Hard-Negative Margin MSE Distillation",
                    "Faithful Abstention ('I Don't Know') SFT",
                ],
                "small": [
                    "Inline [Doc_i] Citation Span Formatting",
                    "KL-Distillation from LLM Teacher Rankings",
                    "LoRA Adapters on Bi-Encoder Backbones",
                ],
                "anti": [
                    "Memorizing Stale Facts Instead of Context",
                    "Ignoring Distractor Passages in SFT",
                    "Fabricated Citation Brackets ([1], [2])",
                    "Overfitting Embedding to Narrow Queries",
                ],
            },
            "multimodal": {
                "h1": [
                    "Visual Instruction Tuning (LLaVA-OneVision)",
                    "GUI Grounding & Bounding-Box SFT",
                    "Full-Duplex Speech-to-Speech SFT (Moshi)",
                ],
                "normal": [
                    "Frozen ViT + Trainable Projector + LLM SFT",
                    "AnyRes High-Res Document/Chart SFT",
                    "Interleaved Image-Text Multi-Turn SFT",
                    "Voice Emotion, Prosody & Barge-In SFT",
                    "Set-of-Mark (SoM) Visual Prompt SFT",
                    "MMMU / ChartQA / DocVQA Eval Suites",
                ],
                "small": [
                    "<image> / <audio> Special Token Alignment",
                    "[x1, y1, x2, y2] Normalized Box Tokens",
                    "LoRA on Vision Projector + LLM Layers",
                ],
                "anti": [
                    "Visual Hallucination (Answering Blindly)",
                    "Projector Collapse Ignoring Fine Details",
                    "Coordinate Token Off-by-One Drift",
                    "Voice SFT Losing Text Reasoning Ability",
                ],
            },
            "embodied": {
                "h1": [
                    "Behavioral Cloning (BC) & ACT Policies",
                    "GUI Action-Trajectory SFT (OS-Atlas / Aguvis)",
                    "Co-Fine-Tuning on Sim + Real Robot Demos",
                ],
                "normal": [
                    "Action Chunking with Transformers (ACT)",
                    "Language-Conditioned Manipulation SFT",
                    "Click(x,y) / Type(text) / Scroll GUI SFT",
                    "Wrist + Third-Person Multi-View SFT",
                    "LoRA Adaptation to New Robot Gripper",
                    "Offline Action MSE & Task Success Rate",
                ],
                "small": [
                    "k-Step Action Chunk Prediction Horizon",
                    "Gaussian Mixture / Diffusion Action Head",
                    "Proprioceptive History Dropout Regularizer",
                ],
                "anti": [
                    "Covariate Shift & Compounding BC Errors",
                    "Copycat Inertia Trap (Repeating Past Action)",
                    "Overfitting to Exact Background Lighting",
                    "GUI SFT Clicking Stale Static Coordinates",
                ],
            },
        },
    },
    # =========================================================================
    # 6. Post-Training
    # =========================================================================
    {
        "stage": 6,
        "short_name": "Post-Training",
        "full_name": "Preference Alignment (RLHF/DPO) & Verifiable-Reward Reinforcement Learning (RLVR/GRPO)",
        "accent": "#F472B6",
        "desc": "Preference tuning (PPO, DPO, KTO) and critic-free Reinforcement Learning with Verifiable Rewards (RLVR, GRPO).",
        "core_unit": "Core Unit: Preference Pairs, Rollouts & Advantages",
        "book_ref": "Ch. 1.8, 3.2, 12.1–8, 30.2 (RLHF, DPO & RLVR / GRPO)",
        "cells": {
            "llm": {
                "h1": [
                    "Preference Tuning: PPO · DPO · KTO · SimPO",
                    "Critic-Free RLVR: GRPO · Dr. GRPO · DAPO",
                    "verl · OpenRLHF · TRL (GRPO) · NeMo Aligner",
                ],
                "normal": [
                    "DeepSeek-R1 · OpenAI o3/o4 · QwQ-32B",
                    "Verifiable Execution Oracles (Tests/Math)",
                    "KL-Divergence & Policy Entropy Monitoring",
                    "DAPO Clip-Higher & Dynamic Sampling",
                    "Deliberative Alignment & Safety Rubrics",
                    "Anti-Reward-Hacking & Length Control",
                ],
                "small": [
                    "Group-Normalized Advantage A_i",
                    "Ray + vLLM Distributed Async Rollouts",
                    "Prime Intellect Verifiers Environments",
                ],
                "anti": [
                    "Reward Hacking & Length Inflation",
                    "Policy Entropy Collapse & Mode Collapse",
                    "GRPO Zero-Variance Advantage (All 0/1)",
                    "Sycophancy & Judge-Bias Exploitation",
                ],
            },
            "rag": {
                "h1": [
                    "Search-R1: RLVR for Multi-Turn Search",
                    "Citation Faithfulness & Groundedness DPO",
                    "Abstention & Conflict-Resolution RL",
                ],
                "normal": [
                    "End-to-End Query-Retrieve-Reason RL",
                    "Exact-Match / F1 Answer Verifier Rewards",
                    "NLI Entailment Reward for Citations",
                    "Penalizing Unsupported Extrapolation",
                    "Retrieval Cost & Latency Penalty in RL",
                    "RAGTruth & FaithBench Alignment Audits",
                ],
                "small": [
                    "<search>query</search> Rollout Action",
                    "Counterfactual Context Robustness Reward",
                    "Hard-Negative Preference Pairs (Chosen/Rej)",
                ],
                "anti": [
                    "Reward Hacking via Redundant Searches",
                    "Cherry-Picking Weak Evidence to Please RM",
                    "Over-Abstention ('I Cannot Answer' Trap)",
                    "Hallucinating Plausible Uncited Claims",
                ],
            },
            "multimodal": {
                "h1": [
                    "Multimodal RLVR (Visual Math & Geometry)",
                    "Hallucination-Penalized VLM DPO (RLAIF-V)",
                    "Diffusion DPO & Flow-GRPO Aesthetic RL",
                ],
                "normal": [
                    "OCR-Verified Chart & Table Reasoning RL",
                    "Object-Detector Grounded Reward Oracles",
                    "Voice Turn-Taking & Politeness Alignment",
                    "Safety Refusal on Visual Jailbreaks",
                    "Video Temporal Consistency RL Rewards",
                    "MM-Vet / HallusionBench Alignment Evals",
                ],
                "small": [
                    "IoU Bounding-Box Overlap Verifier Reward",
                    "CLIP / PickScore Aesthetic Reward Models",
                    "Contrastive Image-Conditioned DPO",
                ],
                "anti": [
                    "Text-Prior Shortcuts Ignoring the Image",
                    "Aesthetic Reward Hacking (Oversaturation)",
                    "Over-Refusal on Benign Medical/Art Images",
                    "Voice Interruption Hypersensitivity",
                ],
            },
            "embodied": {
                "h1": [
                    "OSWorld / WebArena Verifiable GUI RLVR",
                    "Sim-to-Real RL (PPO / SAC / HIL-SERL)",
                    "Control-Barrier Safety Shielding RL",
                ],
                "normal": [
                    "DOM / Database State Verifier Rewards",
                    "Human-in-the-Loop Sample-Efficient RL",
                    "Domain Randomization (Friction/Mass/Lag)",
                    "Residual RL on Top of Pre-Trained VLA",
                    "Sparse Task-Completion vs. Dense Shaping",
                    "Real-World Rollout Safety Reset Controllers",
                ],
                "small": [
                    "Asymmetric Actor-Critic (Privileged Sim)",
                    "Action Smoothness / Jerk Penalty Term",
                    "Docker Snapshot Reset Between Rollouts",
                ],
                "anti": [
                    "Sim Physics Exploit (Glitching Simulator)",
                    "Destructive Real-World Hardware Exploration",
                    "GUI Agent Clicking 'Delete/Buy' for Reward",
                    "Sparse-Reward Credit Assignment Failure",
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
        "desc": "Inference-time System-2 scaling: Chain-of-Thought (<think>), Best-of-N, PRM reranking, and MCTS.",
        "core_unit": "Core Unit: Thinking Tokens, Search Trees & Votes",
        "book_ref": "Ch. 13.1–8, 15.1–9, 30.2 (Test-Time Compute & Search)",
        "cells": {
            "llm": {
                "h1": [
                    "System-2 Chain-of-Thought (<think> CoT)",
                    "Parallel Scaling: Best-of-N & Majority@k",
                    "Sequential & Tree Search (PRM / MCTS)",
                ],
                "normal": [
                    "OpenAI o3 / Claude 4.6 Extended Thinking",
                    "DeepSeek-R1 · Qwen3 Thinking · s1 Budget",
                    "Process Reward Models (Step-Level PRM)",
                    "Adaptive Thinking Budgets (Low/Med/High)",
                    "Execution-Guided Code Filter before Vote",
                    "Pass@k vs. Cons@k & AIME/ARC-AGI Evals",
                ],
                "small": [
                    "s1 Budget Forcing ('Wait' Token Extension)",
                    "PUCT Node Selection in Reasoning Trees",
                    "Compute-Optimal Test-Time Allocation",
                ],
                "anti": [
                    "Overthinking & Analysis Paralysis (10x)",
                    "PRM Reward Hacking & Verifier Blindspots",
                    "Self-Correction Degrading Right Answers",
                    "Unfaithful Post-Hoc CoT Rationalization",
                ],
            },
            "rag": {
                "h1": [
                    "Query Decomposition & Multi-Hop Planning",
                    "Reciprocal Rank Fusion (Dense + BM25)",
                    "CRAG & Self-RAG Critique-and-Retry Loops",
                ],
                "normal": [
                    "HyDE (Hypothetical Document Embeddings)",
                    "Cross-Encoder Reranking Cascade (Top-100->10)",
                    "Iterative IRCoT (Interleaved Retrieval + CoT)",
                    "Minimum-Span Evidence Extraction",
                    "Dynamic Top-k Cutoff via Confidence Score",
                    "Latency-Bounded Multi-Index Speculation",
                ],
                "small": [
                    "RRF Score = Σ 1 / (k + rank_i)",
                    "Step-Back Prompting for Abstract Queries",
                    "Cross-Document Contradiction Check",
                ],
                "anti": [
                    "Infinite Query-Rewrite Retrieval Loops",
                    "HyDE Hallucination Drifting Vector Search",
                    "Reranker Latency Blowing Up p99 SLA",
                    "Multi-Hop Error Propagation Across Steps",
                ],
            },
            "multimodal": {
                "h1": [
                    "Visual Chain-of-Thought (Crop / Zoom / Pan)",
                    "Active Perception & Region-of-Interest Scan",
                    "Best-of-N VLM Verifier Reranking",
                ],
                "normal": [
                    "Iterative High-Res Crop Inspection (o3-Vision)",
                    "Code-Execution Image Tooling (OpenCV/Matplotlib)",
                    "Keyframe Selection + Dense Window Search",
                    "Classifier-Free Guidance (CFG) Step Scaling",
                    "Audio Re-Listening & Timestamp Verification",
                    "Self-Consistency Over Multiple Crop Views",
                ],
                "small": [
                    "Dynamic BBox Zoom-In Tool Call",
                    "Denoising Diffusion Step Count (20–50)",
                    "OCR-Assisted Visual Math Verification",
                ],
                "anti": [
                    "Zooming into Irrelevant Background Patches",
                    "Visual Confirmation Bias on Blurry Crops",
                    "Excessive High-Res Crops Blowing Token Cap",
                    "Diffusion Over-Stepping Artifact Burn-In",
                ],
            },
            "embodied": {
                "h1": [
                    "Model-Predictive Control (MPC) Rollouts",
                    "World-Model Counterfactual Tree Search",
                    "Visual Subgoal & Affordance Planning",
                ],
                "normal": [
                    "CEM / MPPI Trajectory Optimization in Sim",
                    "VLM Failure Detection & Recovery Replan",
                    "GUI Pre-Click Hover / DOM Verification",
                    "3D Value Map & VoxPoser Waypoint Search",
                    "Receding-Horizon Action Chunk Execution",
                    "Safety-Filter Critic Rejecting Unsafe Actions",
                ],
                "small": [
                    "H-Step Imagination Rollout Horizon",
                    "Collision-Free Configuration Space Check",
                    "Speculative GUI Action Rollback",
                ],
                "anti": [
                    "Planning Latency Exceeding Control Rate",
                    "World-Model Rollout Diverging After 5s",
                    "Irreversible GUI Click Before Verification",
                    "Deadlock Oscillation Between Two Obstacles",
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
        "desc": "Context budgeting, 4-tier agentic memory, function calling, Model Context Protocol (MCP), and SKILL.md.",
        "core_unit": "Core Unit: Context Window, Memory & JSON-RPC",
        "book_ref": "Ch. 17, 18.2–5, 22, 23 (Memory, Tools, MCP & Skills)",
        "cells": {
            "llm": {
                "h1": [
                    "Context Engineering & Token Budgeting",
                    "Model Context Protocol (MCP / .mcp.json)",
                    "4-Tier Memory + Agent Skills (SKILL.md)",
                ],
                "normal": [
                    "Letta (MemGPT) · Mem0 · Zep · LangMem",
                    "Working, Episodic, Semantic & Procedural",
                    "Progressive Disclosure Skill Loading",
                    "Sleep-Time Dreaming & Memory Consolidation",
                    "Observation Masking & /compact Hygiene",
                    "MCP OAuth 2.1 Scopes & LoCoMo Evals",
                ],
                "small": [
                    "Prompt Caching Prefix Reuse (90% Savings)",
                    "JSON-RPC 2.0 stdio & Streamable HTTP",
                    "Keep Context Utilization < 65% Window",
                ],
                "anti": [
                    "Context Rot & Lost-in-the-Middle Decay",
                    "MCP Tool Bloat (100+ Schemas in Prompt)",
                    "Malicious SKILL.md & MCP Rug-Pulls",
                    "Memory Poisoning & Stale Fact Contradiction",
                ],
            },
            "rag": {
                "h1": [
                    "Qdrant · Milvus · pgvector · Weaviate",
                    "GraphRAG · LightRAG · Neo4j Knowledge",
                    "REFRAG & LLMLingua Context Compression",
                ],
                "normal": [
                    "Hybrid Dense + BM25 Index Orchestration",
                    "Entity-Relation Knowledge Graph Communities",
                    "Parent-Document & Window Context Expansion",
                    "Time-Weighted & Recency-Biased Retrieval",
                    "Document-Level RBAC & Tenant Isolation",
                    "RAG Triad Evals (Faithfulness / Recall@k)",
                ],
                "small": [
                    "HNSW ef_search & Metadata Pre-Filtering",
                    "Leiden Community Summary Hierarchy",
                    "KV-Cache Block Reuse for Static Docs",
                ],
                "anti": [
                    "Indirect Prompt Injection via Poisoned Docs",
                    "Cross-Tenant RBAC Data Leakage in Vector DB",
                    "Context Stuffing Drowning Signal in Noise",
                    "GraphRAG Entity-Extraction Cost Explosion",
                ],
            },
            "multimodal": {
                "h1": [
                    "Adaptive ViT Token Merging (PruMerge / ToMe)",
                    "Streaming Video KV-Cache Ring Buffers",
                    "Cross-Modal CLIP / SigLIP Vector Memory",
                ],
                "normal": [
                    "Spatial-Temporal Video Token Compression",
                    "Audio Transcript + Acoustic Embedding Memory",
                    "MCP Image / Audio / Resource URI Handles",
                    "OCR + Layout + Crop Tiered Context Cache",
                    "Full-Duplex Voice Interruption State Tracking",
                    "Video-MME Long-Video Needle-in-Haystack",
                ],
                "small": [
                    "Drop 75% Redundant Background ViT Tokens",
                    "Base64 vs. Presigned URI Media Payloads",
                    "Sliding-Window Cross-Frame KV Eviction",
                ],
                "anti": [
                    "10-Min Video Exhausting 128k Context Window",
                    "Aggressive Token Pruning Dropping Small Text",
                    "Base64 Image Bloat Crashing JSON-RPC Bus",
                    "Desynced Audio-Visual Timestamp Memory",
                ],
            },
            "embodied": {
                "h1": [
                    "3D Scene Graphs & Gaussian Splatting (3DGS)",
                    "DOM + Accessibility Tree (AXTree) Pruning",
                    "Episodic Spatial & Affordance Memory",
                ],
                "normal": [
                    "Semantic Voxel & OctoMap Occupancy Grids",
                    "Set-of-Mark (SoM) Interactive Element IDs",
                    "Proprioceptive & Force-Torque Ring Buffer",
                    "Object Permanence & Tracked Entity State",
                    "MCP Browser / OS / Robot Hardware Servers",
                    "Spatial QA & Scene-State Consistency Evals",
                ],
                "small": [
                    "Filter Invisible / Off-Screen DOM Nodes",
                    "6-DoF Object Pose Kalman Filter State",
                    "Keyframe RGB-D Topological Map Nodes",
                ],
                "anti": [
                    "Raw 50,000-Node HTML DOM Overflowing Prompt",
                    "Dynamic Obstacle Ghosting in Stale 3D Map",
                    "Occlusion Forgetting (Out-of-Sight Vanishes)",
                    "Coordinate Frame Drift Over Long Episodes",
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
        "desc": "The CPU/OS of an agent: CLAUDE.md/AGENTS.md, Loop Engineering, Graph Engineering (LangGraph), and Harness².",
        "core_unit": "Core Unit: State Transitions, Actions & Diffs",
        "book_ref": "Ch. 16, 19, 20, 27 (Harness, Loops & Graphs)",
        "cells": {
            "llm": {
                "h1": [
                    "Agent Harness (Prompt + Tools + State + Loop)",
                    "Claude Code · Codex CLI · Cursor · OpenCode",
                    "LangGraph · OpenAI Agents SDK · Harness²",
                ],
                "normal": [
                    "CLAUDE.md & AGENTS.md Repo Constitutions",
                    "Observe–Decide–Act Loop & Stop Conditions",
                    "Typed State Schema & Checkpointer Reducers",
                    "Spec-Driven Development (Spec->Plan->Test)",
                    "Decoupled Independent Verification (No Self-Grading)",
                    "SWE-bench Verified/Pro & pass^k Reliability",
                ],
                "small": [
                    "p^k Compounding Decay (0.95^20 = 35.8%)",
                    "Git Worktree Checkpoints & Diff Rollback",
                    "Human-in-the-Loop Destructive Tool Gate",
                ],
                "anti": [
                    "Agent Deleting / Mocking Failing Tests",
                    "Unbounded Loop Burn & Action Stagnation",
                    "God-Node Anti-Pattern & State Schema Bloat",
                    "CVE-2025-53773 IDE Config Auto-Approve RCE",
                ],
            },
            "rag": {
                "h1": [
                    "Agentic RAG Workflows (LlamaIndex / Haystack)",
                    "Plan-Search-Read-Synthesize-Verify Loop",
                    "Deterministic Citation & Grounding Gate",
                ],
                "normal": [
                    "Adaptive Routing (No-RAG vs. Fast vs. Deep)",
                    "Sub-Question DAG Execution & State Merge",
                    "Schema-Enforced Structured Output Citations",
                    "Source-Freshness & Authority Verification",
                    "Fallback Web Search When Local KB Misses",
                    "DeepResearch Bench & Citation Precision/Recall",
                ],
                "small": [
                    "Max 3 Search Retries Before Escalation",
                    "Span-Level Character Offset Provenance",
                    "Read-Only Credentials for Search Connectors",
                ],
                "anti": [
                    "Search-Loop Thrashing on Rephrased Queries",
                    "Silent Fallback to Parametric Hallucination",
                    "Citation Laundering (Attributing False Claim)",
                    "Latency Blowup from Unbounded Deep Research",
                ],
            },
            "multimodal": {
                "h1": [
                    "Voice Agent Harness (LiveKit / Pipecat)",
                    "ComfyUI / Diffusers Iterative Gen-Critique Loop",
                    "Visual-Render-Inspect-Fix Coding Loop",
                ],
                "normal": [
                    "VAD + Barge-In Interruption State Machine",
                    "Speculative Turn-Taking & Backchanneling",
                    "VLM Screenshot Diffing for Frontend UI Code",
                    "Iterative Image Inpainting & ControlNet Loop",
                    "C2PA Cryptographic Media Watermarking",
                    "Word-Error-Rate (WER) & Turn-Latency Evals",
                ],
                "small": [
                    "< 300ms End-of-Turn Speech Trigger",
                    "Playwright Render -> VLM Critique -> CSS Fix",
                    "Audio Echo Cancellation & Duplex Ducking",
                ],
                "anti": [
                    "Voice Agent Talking Over User (Barge-In Fail)",
                    "Echo Loop (Agent Transcribing Its Own TTS)",
                    "VLM Critique Loop Breaking Working Layout",
                    "Cascading ASR -> LLM -> TTS Latency (>3s)",
                ],
            },
            "embodied": {
                "h1": [
                    "Computer-Use Harness (Operator / Claude CU)",
                    "Hierarchical System-2 VLM + System-1 VLA",
                    "Hardware Safety Interlocks & E-Stop Harness",
                ],
                "normal": [
                    "Screenshot -> Grounding -> Action -> Verify Loop",
                    "Browser Pop-Up, Modal & Auth Recovery",
                    "2 Hz High-Level Subgoal + 50 Hz Motor Control",
                    "Force/Torque Anomaly & Collision Reflex Stop",
                    "Confirmation Gate Before Checkout / Send / Delete",
                    "OSWorld / WebArena / AndroidWorld Benchmarks",
                ],
                "small": [
                    "Post-Click DOM/Visual Diff Assertion",
                    "Joint-Velocity & Workspace Bounding Box",
                    "Automated Episode Reset & State Snapshot",
                ],
                "anti": [
                    "Visual Prompt Injection via Fake Screen Pop-Up",
                    "Clicking 'Submit/Pay' in Infinite Retry Loop",
                    "UI Loading Lag Causing Misaligned Double-Click",
                    "VLM Delusion Ignoring Physical Gripper Slip",
                ],
            },
        },
    },
    # =========================================================================
    # 10. Multi-Agent
    # =========================================================================
    {
        "stage": 10,
        "short_name": "Multi-Agent",
        "full_name": "Multi-Agent Orchestration, Hierarchical Swarms, A2A Protocols & Shared State",
        "accent": "#E879F9",
        "desc": "Multi-agent topologies (OWC), inter-agent protocols (A2A, ACP), parallel worktree swarms, and Agentic/Generative UI.",
        "core_unit": "Core Unit: A2A Tasks, Worktrees & Swarm State",
        "book_ref": "Ch. 1.14, 14, 24, 26, 28, 30.10 (A2A, MAS & Agentic UI)",
        "cells": {
            "llm": {
                "h1": [
                    "Orchestrator–Worker–Critic (OWC) Pattern",
                    "Google A2A Protocol · IBM ACP · ANP",
                    "CrewAI · AutoGen / AG2 · LangGraph Swarm",
                ],
                "normal": [
                    "Hierarchical, Decentralized & Debate Swarms",
                    "Parallel Git-Worktree Coding Subagents",
                    "Independent Critic & Red-vs-Blue Verification",
                    "CopilotKit · AG-UI · Vercel AI SDK Generative UI",
                    "Agent Gateway (mTLS, OAuth OBO, FinOps Caps)",
                    "Cross-Agent Cryptographic KYA & Audit Trails",
                ],
                "small": [
                    "/.well-known/agent.json Capability Cards",
                    "Per-Swarm Token & Dollar Circuit Breakers",
                    "Blackboard Shared-Memory vs. Message Bus",
                ],
                "anti": [
                    "Cascading Hallucination & Swarm Echo Chamber",
                    "O(N²) Chatty Agent Token Explosion",
                    "Cross-Agent Confused Deputy & Privilege Escalation",
                    "Merge Conflicts Across Parallel Worktrees",
                ],
            },
            "rag": {
                "h1": [
                    "Federated Multi-Index Knowledge Brokers",
                    "Parallel Deep-Research Subagent Swarms",
                    "Cross-Domain Claim-Verification Critics",
                ],
                "normal": [
                    "Supervisor Routing Across SQL / Vector / Graph",
                    "Map-Reduce Literature & Patent Synthesis",
                    "Adversarial Fact-Checker vs. Writer Debate",
                    "Per-Agent OAuth On-Behalf-Of (OBO) ACLs",
                    "Shared Citation Blackboard & Deduplication",
                    "Enterprise Cross-Silo Retrieval Benchmarks",
                ],
                "small": [
                    "A2A Knowledge-Query Capability Discovery",
                    "Provenance Hash Chain Across Subagents",
                    "Token-Budget Allocation per Research Branch",
                ],
                "anti": [
                    "Subagent Circular Citation Laundering",
                    "Confused-Deputy Cross-Department Data Leak",
                    "10 Subagents Fetching Identical Documents",
                    "Aggregator Dropping Minority Counter-Evidence",
                ],
            },
            "multimodal": {
                "h1": [
                    "Cross-Modal Specialist Production Swarms",
                    "Director–Storyboard–Video–Audio Pipeline",
                    "Multimodal Critic & Brand/Safety Gatekeeper",
                ],
                "normal": [
                    "Voice Concierge + Backend Tool Subagents",
                    "Character-Sheet & Style Consistency Blackboard",
                    "Parallel Scene Rendering + Audio Foley Sync",
                    "VLM Visual QA Critic Grading Generated Media",
                    "Streaming AG-UI Canvas & Live Media Artifacts",
                    "End-to-End Multi-Modal Storyboard Evals",
                ],
                "small": [
                    "Shared Latent Seed & IP-Adapter Reference",
                    "WebRTC + A2A Split-Plane Media Streaming",
                    "Automated Copyright & Likeness Guardrails",
                ],
                "anti": [
                    "Character Identity Drift Across Video Scenes",
                    "Voice Concierge Promising Actions Backend Fails",
                    "Audio-Visual Lip-Sync Desynchronization",
                    "Runaway Diffusion Rendering Costs in Swarm",
                ],
            },
            "embodied": {
                "h1": [
                    "Multi-Robot Fleet & Warehouse Orchestration",
                    "Digital-Twin Sim + Physical Fleet Co-Execution",
                    "Human–Robot–GUI Shared Autonomy Swarms",
                ],
                "normal": [
                    "MAPF (Multi-Agent Path Finding) Conflict-Free",
                    "Heterogeneous Swarms (Drone + Rover + Arm)",
                    "V2X Cooperative Perception & Spatial Sharing",
                    "Cloud Fleet Planner + Local Edge Safety Reflex",
                    "Operator Fleet Dashboard & Teleop Handoff",
                    "Fleet Throughput, Deadlock & Collision Evals",
                ],
                "small": [
                    "CBS (Conflict-Based Search) Spatio-Temporal",
                    "DDS / ROS 2 Multi-Robot Namespace Isolation",
                    "Graceful Degradation on Wi-Fi Drop",
                ],
                "anti": [
                    "Warehouse Corridor Deadlock & Traffic Gridlock",
                    "Shared-Map Poisoning from One Faulty Sensor",
                    "Network Partition Leaving Fleet Uncoordinated",
                    "Simultaneous Grasp Collision on Shared Object",
                ],
            },
        },
    },
]

# Validate Short Name (<= 2 words) and Full Name (<= 10 words) for all 10 stages
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

    Strict Unskipped 5-Level Golden Ratio Typographic Hierarchy (φ = 1.61803398875):
      • T = H0 = 10.0 * φ² ≈ 26.18 pt : Main Megachart Title ("ANATOMY OF AI AGENTS 2026")
      • H1 = H0 / φ        ≈ 16.18 pt : Stage Short Names ("1. Silicon" .. "10. Multi-Agent")
                                        & Organism Short Names ("LLM", "RAG", "Multimodal", "Embodied AI")
      • H2 = H1 / φ        = 10.00 pt : Cell Tier-1 Top-3 Flagship Pills & Masthead Subtitle/Hook/Key
      • H3 = H2 / φ        ≈  6.18 pt : Stage & Organism Full Names (<= 10 words), Cell Tier-2 Core Grid,
                                        Inner Anti-Pattern Items, and Masthead Footnote Strip
      • H4 = H3 / φ        ≈  3.82 pt : Cell Tier-3 Granular Specs & Anti-Pattern Header Badge
    """
    plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]

    H2 = 10.0000          # 10.0000 pt (Cell Tier-1 Top-3 Pills & Masthead)
    H1 = H2 * PHI         # 16.1803 pt (Stage Short Names & Organism Short Names)
    H0 = H1 * PHI         # 26.1803 pt (Main Title T = H0)
    H3 = H2 / PHI         #  6.1803 pt (Full Names, Cell Tier-2 Grid & Anti-Pattern Items)
    H4 = H3 / PHI         #  3.8197 pt (Cell Tier-3 Granular Specs & Anti-Pattern Badge)

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

    ax.text(
        0.012, hdr_y + hdr_h * 0.70,
        "ANATOMY OF AI AGENTS 2026",
        fontsize=H0, fontweight="bold", color="#FFFFFF", va="center", ha="left"
    )
    ax.text(
        0.013, hdr_y + hdr_h * 0.34,
        "www.arianprabowo.com · 10 Stages (1. Silicon → 10. Multi-Agent) × 4 Organisms (LLM · RAG · Multimodal · Embodied AI)",
        fontsize=H2, fontweight="bold", color="#38BDF8", va="center", ha="left"
    )

    ax.plot(
        [0.435, 0.435], [hdr_y + hdr_h * 0.24, hdr_y + hdr_h * 0.91],
        color="#334155", linewidth=1.6
    )

    ax.text(
        0.443, hdr_y + hdr_h * 0.58,
        "What actually runs under an AI agent in 2026? Trace left to right:\n"
        "1. Silicon → 2. Python → 3. Data → 4. Pre-Training → 5. SFT →\n"
        "6. Post-Training → 7. Test-Time → 8. Context → 9. Harness → 10. Multi-Agent.",
        fontsize=H2, fontweight="bold", color="#FEF08A", va="center", ha="left",
        linespacing=1.16
    )

    ax.plot(
        [0.758, 0.758], [hdr_y + hdr_h * 0.24, hdr_y + hdr_h * 0.91],
        color="#334155", linewidth=1.6
    )

    ax.text(
        0.766, hdr_y + hdr_h * 0.58,
        "① COLUMNS (1 → 10): Physical Silicon to Multi-Agent Swarms\n"
        "② ROWS (4 ORGANISMS): LLM Spine + RAG, Multimodal & Embodied AI\n"
        "③ INSIDE EVERY CELL: Stack + Red ⚠ ANTI-PATTERNS Box at Bottom",
        fontsize=H2, fontweight="bold", color="#93C5FD", va="center", ha="left",
        linespacing=1.18
    )

    ax.plot(
        [0.010, 0.990], [hdr_y + hdr_h * 0.20, hdr_y + hdr_h * 0.20],
        color="#1E293B", linewidth=1.1
    )

    ax.text(
        0.500, hdr_y + hdr_h * 0.095,
        f"*Synthesized from Haggai Roitman's 'The Hitchhiker's Guide to Agentic AI: From Foundations to Systems' (arXiv:2606.24937, v1.4, June 2026) + 2026 systems tooling. "
        f"Companion to AI Skill Tree 2026 & AI Ladder Evolution by Arian Prabowo · {LAST_UPDATED_STR}",
        fontsize=H3, fontweight="bold", color="#94A3B8", va="center", ha="center"
    )

    # -------------------------------------------------------------------------
    # 2. Horizontal Geometry (Left Organism Column + 10 Stage Columns)
    # -------------------------------------------------------------------------
    left_x0 = 0.004
    left_w = 0.076
    col_gap = 0.0026
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
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.73,
        "ORGANISMS\n× STAGES",
        fontsize=H1, fontweight="bold", color="#FFFFFF", va="center", ha="center",
        linespacing=1.02
    )
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.38,
        "1. Silicon → 10. Swarms",
        fontsize=H2, fontweight="bold", color="#FEF08A", va="center", ha="center"
    )
    ax.text(
        left_x0 + left_w / 2, col_hdr_y + col_hdr_h * 0.15,
        "LLM · RAG · Multimodal\n· Embodied (+ ⚠ Traps)",
        fontsize=H3, fontweight="bold", color="#5EEAD4", va="center", ha="center",
        linespacing=1.08
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
        banner_h = col_hdr_h * 0.55
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
        seg_h = banner_h * 0.12
        bar_x_start = lx + 0.0040
        bar_y = b_top_y - banner_h * 0.16 - seg_h / 2.0
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

        # Short Name (<= 2 words) in H1 (= H0 / φ): "1. Silicon", "2. Python", ...
        ax.text(
            lx + stage_col_w / 2, b_top_y - banner_h * 0.45,
            STAGE_H1_TITLES[st_num],
            fontsize=H1,
            fontweight="bold",
            color="#FFFFFF",
            va="center", ha="center"
        )

        # Full Name (<= 10 words, wrapped onto 2 lines) at bottom of banner in H3 (= H0 / φ³)
        ax.text(
            lx + stage_col_w / 2, b_top_y - banner_h * 0.80,
            textwrap.fill(STAGE_FULL_NAMES[st_num], width=52),
            fontsize=H3,
            fontweight="bold",
            color="#FEF08A",
            va="center", ha="center",
            linespacing=1.02
        )

        # Column Header Body below banner: Description & Bullets in H3 (= H0 / φ³)
        desc_wrapped = textwrap.fill(st["desc"], width=46)
        unit_line = f"• {st['core_unit']}"
        ref_line = f"• Guide: {st['book_ref']}"

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
            color="#93C5FD",
            va="bottom",
            ha="left",
            linespacing=1.04,
        )

    # -------------------------------------------------------------------------
    # 3. 4 Organism Rows (LLM Spine + Detached RAG, Multimodal, Embodied AI)
    #    with Red Dashed "⚠ ANTI-PATTERNS & TRAPS" Box INSIDE Every Cell
    # -------------------------------------------------------------------------
    top_y = 0.772
    row_h = 0.1865
    spine_sep_gap = 0.0075  # Visual separation between Row 1 (LLM Spine) and Separate Organisms (RAG, Multimodal, Embodied)
    row_gap = 0.0042

    row_geoms = [
        (top_y - 1 * row_h, row_h),
        (top_y - 2 * row_h - spine_sep_gap, row_h),
        (top_y - 3 * row_h - spine_sep_gap - 1 * row_gap, row_h),
        (top_y - 4 * row_h - spine_sep_gap - 2 * row_gap, row_h),
    ]

    # Dashed teal/amber separator line between LLM Core Spine (Row 1) and Separate Organisms (Rows 2..4)
    sep_y = top_y - row_h - spine_sep_gap * 0.50
    ax.plot(
        [left_x0, 0.996], [sep_y, sep_y],
        color="#0D9488", linewidth=2.0, linestyle=(0, (7, 4)), alpha=0.85
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
        rbanner_h = rh * 0.48
        rbox_top = FancyBboxPatch(
            (left_x0 + inset_r, ry + rh - rbanner_h - inset_r),
            left_w - 2 * inset_r, rbanner_h,
            boxstyle="round,pad=0.0,rounding_size=0.003",
            facecolor=org["hdr_bg"], edgecolor="#FFFFFF", linewidth=1.1
        )
        ax.add_patch(rbox_top)

        rb_top_y = ry + rh - inset_r
        # Badge in H4/H3
        ax.text(
            left_x0 + left_w / 2, rb_top_y - rbanner_h * 0.16,
            org["badge"],
            fontsize=H3, fontweight="bold", color="#FEF08A", va="center", ha="center"
        )
        # Organism Short Name (<= 2 words) in H1
        ax.text(
            left_x0 + left_w / 2, rb_top_y - rbanner_h * 0.46,
            org["short_name"],
            fontsize=H1,
            fontweight="bold", color="#FFFFFF", va="center", ha="center"
        )
        # Organism Full Name (<= 10 words, wrapped) in H3
        ax.text(
            left_x0 + left_w / 2, rb_top_y - rbanner_h * 0.80,
            textwrap.fill(org["full_name"], width=28),
            fontsize=H3,
            fontweight="bold", color="#E2E8F0", va="center", ha="center",
            linespacing=1.00
        )

        body_avail_h = rh - rbanner_h - inset_r
        ax.text(
            left_x0 + left_w / 2,
            ry + body_avail_h * 0.68,
            org["desc"],
            fontsize=H3,
            fontweight="bold",
            color="#F8FAFC",
            va="center",
            ha="center",
            linespacing=1.06,
        )
        ax.text(
            left_x0 + 0.0030,
            ry + 0.0045,
            org["bullets"],
            fontsize=H3,
            fontweight="bold",
            color="#93C5FD",
            va="bottom",
            ha="left",
            linespacing=1.08,
        )

        # 10 Stage Cells for this Organism
        for s_idx, st in enumerate(STACK_STAGES):
            cx = get_col_x(s_idx)
            cw = stage_col_w

            cell_data = st["cells"][org["key"]]
            top_h1 = cell_data["h1"]
            mid_norm = cell_data["normal"]
            bot_small = cell_data["small"]
            anti_list = cell_data["anti"]

            cbox = FancyBboxPatch(
                (cx, ry), cw, rh,
                boxstyle="round,pad=0.0,rounding_size=0.004",
                facecolor=org["cell_bg"],
                edgecolor=org["cell_edge"],
                linewidth=1.5
            )
            ax.add_patch(cbox)

            pad_x = 0.0018
            pad_top = 0.0026
            pad_bot = 0.0024
            inner_w = cw - 2 * pad_x
            x_left = cx + pad_x

            gap_z = 0.0018
            avail_h = rh - pad_top - pad_bot - 3 * gap_z
            t1_h = avail_h * 0.34   # Top 3 Flagship Pills (H2)
            t2_h = avail_h * 0.30   # Middle 3x2 = 6 Core Items (H3)
            t3_h = avail_h * 0.08   # Granular 1x3 = 3 Specs (H4)
            anti_h = avail_h * 0.28 # Inner Red "⚠ ANTI-PATTERNS & TRAPS" Box (2x2 in H3/H4)

            # -----------------------------------------------------------------
            # Zone 1: Top 3 Flagship Pills (H2)
            # -----------------------------------------------------------------
            t1_top_y = ry + rh - pad_top
            pill_gap = 0.0015
            ph = (t1_h - 2 * pill_gap) / 3.0
            for idx_1, kw in enumerate(top_h1[:3]):
                py = t1_top_y - (idx_1 + 1) * ph - idx_1 * pill_gap
                pill = FancyBboxPatch(
                    (x_left, py), inner_w, ph,
                    boxstyle="round,pad=0.0,rounding_size=0.0022",
                    facecolor=org["h1_bg"],
                    edgecolor=org["pill_edge"],
                    linewidth=1.10
                )
                ax.add_patch(pill)

                ax.text(
                    x_left + inner_w / 2, py + ph / 2,
                    kw,
                    fontsize=H2,
                    fontweight="bold",
                    color=org["h1_txt"],
                    va="center", ha="center"
                )

            # -----------------------------------------------------------------
            # Zone 2: Middle 3x2 = 6 Core Stack & Mechanisms Grid (H3)
            # -----------------------------------------------------------------
            t2_top_y = t1_top_y - t1_h - gap_z
            t2_row_h = t2_h / 3.0
            t2_col_w = inner_w / 2.0

            ax.plot(
                [x_left + t2_col_w, x_left + t2_col_w],
                [t2_top_y - t2_h + 0.0008, t2_top_y - 0.0008],
                color=org["cell_edge"], linewidth=0.55, alpha=0.35
            )

            for idx_2, kw in enumerate(mid_norm[:6]):
                mr = idx_2 // 2
                mc = idx_2 % 2
                if mr % 2 == 1 and mc == 0:
                    stripe = FancyBboxPatch(
                        (x_left + 0.0004, t2_top_y - (mr + 1) * t2_row_h + 0.00015),
                        inner_w - 0.0008, t2_row_h - 0.0003,
                        boxstyle="round,pad=0.0,rounding_size=0.0012",
                        facecolor=org["t2_bg"],
                        edgecolor="none"
                    )
                    ax.add_patch(stripe)

                tx = x_left + mc * t2_col_w + 0.0010
                ty = t2_top_y - (mr + 0.5) * t2_row_h
                ax.text(
                    tx, ty,
                    textwrap.fill(kw, width=23),
                    fontsize=H3,
                    fontweight="bold",
                    color=org["t2_txt"],
                    va="center", ha="left",
                    linespacing=0.96
                )

            # -----------------------------------------------------------------
            # Zone 3: Granular 1x3 = 3 Specs Strip (H4)
            # -----------------------------------------------------------------
            t3_top_y = t2_top_y - t2_h - gap_z
            t3_col_w = inner_w / 3.0
            t3_band = FancyBboxPatch(
                (x_left, t3_top_y - t3_h), inner_w, t3_h,
                boxstyle="round,pad=0.0,rounding_size=0.0016",
                facecolor=org["t3_bg"],
                edgecolor="#CBD5E1",
                linewidth=0.55
            )
            ax.add_patch(t3_band)

            for c_div in (1, 2):
                ax.plot(
                    [x_left + c_div * t3_col_w, x_left + c_div * t3_col_w],
                    [t3_top_y - t3_h + 0.0005, t3_top_y - 0.0005],
                    color="#CBD5E1", linewidth=0.50
                )

            for idx_3, kw in enumerate(bot_small[:3]):
                tx = x_left + idx_3 * t3_col_w + 0.0007
                ty = t3_top_y - 0.5 * t3_h
                ax.text(
                    tx, ty,
                    textwrap.fill(kw, width=25),
                    fontsize=H4,
                    fontweight="bold",
                    color=org["t3_txt"],
                    va="center", ha="left",
                    linespacing=0.92
                )

            # -----------------------------------------------------------------
            # Zone 4 (INSIDE): Red Dashed "⚠ ANTI-PATTERNS & TRAPS" Sub-Box
            # -----------------------------------------------------------------
            anti_top_y = t3_top_y - t3_h - gap_z
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

            # Compact top header strip inside the Anti-Patterns sub-box
            ahdr_h = anti_h * 0.22
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
                "⚠ ANTI-PATTERNS & FAILURE MODES",
                fontsize=H4,
                fontweight="bold",
                color="#9F1239",
                va="center", ha="center"
            )

            # 2x2 Grid of 4 Concrete Anti-Patterns in H3/H4
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
                tx = x_left + ac * acol_w + 0.0009
                ty = abody_top_y - (ar + 0.5) * arow_h
                ax.text(
                    tx, ty,
                    textwrap.fill(f"✕ {akw}", width=22),
                    fontsize=H3,
                    fontweight="bold",
                    color="#881337",
                    va="center", ha="left",
                    linespacing=0.92
                )

    fig.savefig(OUT_DEV_PNG, dpi=300, facecolor=fig.get_facecolor())
    fig.savefig(OUT_DEV_PDF, format="pdf", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved: {OUT_DEV_PNG} ({OUT_DEV_PNG.stat().st_size:,} bytes)")
    print(f"Saved: {OUT_DEV_PDF} ({OUT_DEV_PDF.stat().st_size:,} bytes)")


def render_mobile_agent_anatomy_chart():
    """
    Smartphone Landscape Mini Chart (26.0 x 12.0 in @ 300 DPI — exact 19.5:9 Mobile Landscape)
    flowing from LEFT to RIGHT (1. Silicon -> 10. Multi-Agent) across 4 Organism Rows
    (LLM, RAG, Multimodal, Embodied AI) with Anti-Patterns INSIDE every cell.
    """
    plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]

    M_H2 = 10.0 * (26.0 / 46.8)          #  5.5556 pt
    M_H1 = M_H2 * PHI                    #  8.9891 pt
    M_H0 = M_H1 * PHI                    # 14.5446 pt
    M_H3 = M_H2 / PHI                    #  3.4335 pt

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
        "www.arianprabowo.com · 10 Stages (1. Silicon → 10. Multi-Agent) × 4 Organisms (LLM · RAG · Multimodal · Embodied AI)",
        fontsize=M_H2, fontweight="bold", color="#38BDF8", va="center", ha="left"
    )

    ax.plot(
        [0.435, 0.435], [hdr_y + hdr_h * 0.24, hdr_y + hdr_h * 0.91],
        color="#334155", linewidth=1.2
    )

    ax.text(
        0.443, hdr_y + hdr_h * 0.58,
        "What actually runs under an AI agent in 2026? Trace left to right:\n"
        "1. Silicon → 2. Python → 3. Data → 4. Pre-Training → 5. SFT →\n"
        "6. Post-Training → 7. Test-Time → 8. Context → 9. Harness → 10. Multi-Agent.",
        fontsize=M_H2, fontweight="bold", color="#FEF08A", va="center", ha="left",
        linespacing=1.15
    )

    ax.plot(
        [0.758, 0.758], [hdr_y + hdr_h * 0.24, hdr_y + hdr_h * 0.91],
        color="#334155", linewidth=1.2
    )

    ax.text(
        0.766, hdr_y + hdr_h * 0.58,
        "① COLUMNS (1 → 10): Physical Silicon to Multi-Agent Swarms\n"
        "② ROWS (4 ORGANISMS): LLM Spine + RAG, Multimodal & Embodied AI\n"
        "③ INSIDE EVERY CELL: Stack + Red ⚠ ANTI-PATTERNS Box at Bottom",
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
    left_w = 0.076
    col_gap = 0.0026
    active_x0 = left_x0 + left_w + col_gap
    n_stages = len(STACK_STAGES)
    stage_col_w = (0.996 - active_x0 - (n_stages - 1) * col_gap) / n_stages

    def get_col_x(s_idx: int) -> float:
        return active_x0 + s_idx * (stage_col_w + col_gap)

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
        "ORGANISMS\n× STAGES",
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
        "LLM · RAG · Multimodal\n· Embodied (+ ⚠ Traps)",
        fontsize=M_H3, fontweight="bold", color="#5EEAD4", va="center", ha="center",
        linespacing=1.08
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
        banner_h = col_hdr_h * 0.60
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
        seg_h = banner_h * 0.12
        bar_x_start = lx + 0.0040
        bar_y = b_top_y - banner_h * 0.16 - seg_h / 2.0
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
            lx + stage_col_w / 2, b_top_y - banner_h * 0.45,
            STAGE_H1_TITLES[st_num],
            fontsize=M_H1,
            fontweight="bold",
            color="#FFFFFF",
            va="center", ha="center"
        )

        ax.text(
            lx + stage_col_w / 2, b_top_y - banner_h * 0.80,
            textwrap.fill(STAGE_FULL_NAMES[st_num], width=52),
            fontsize=M_H3,
            fontweight="bold",
            color="#FEF08A",
            va="center", ha="center",
            linespacing=1.02
        )

        unit_short = textwrap.fill(f"{st['core_unit']} · {st['book_ref']}", width=46)
        ax.text(
            lx + 0.0026,
            col_hdr_y + (col_hdr_h - banner_h) * 0.48,
            unit_short,
            fontsize=M_H3,
            fontweight="bold",
            color="#93C5FD",
            va="center",
            ha="left",
            linespacing=1.05,
        )

    top_y = 0.784
    row_h = 0.1895
    spine_sep_gap = 0.0070
    row_gap = 0.0040

    row_geoms = [
        (top_y - 1 * row_h, row_h),
        (top_y - 2 * row_h - spine_sep_gap, row_h),
        (top_y - 3 * row_h - spine_sep_gap - 1 * row_gap, row_h),
        (top_y - 4 * row_h - spine_sep_gap - 2 * row_gap, row_h),
    ]

    sep_y = top_y - row_h - spine_sep_gap * 0.50
    ax.plot(
        [left_x0, 0.996], [sep_y, sep_y],
        color="#0D9488", linewidth=1.5, linestyle=(0, (6, 3)), alpha=0.85
    )

    for r_idx, org in enumerate(ORGANISMS):
        ry, rh = row_geoms[r_idx]

        rbox = FancyBboxPatch(
            (left_x0, ry), left_w, rh,
            boxstyle="round,pad=0.0,rounding_size=0.004",
            facecolor=org["hdr_bg"], edgecolor="#0F172A", linewidth=1.3
        )
        ax.add_patch(rbox)
        ax.text(
            left_x0 + left_w / 2, ry + rh * 0.80,
            org["badge"],
            fontsize=M_H3,
            fontweight="bold", color="#FEF08A", va="center", ha="center"
        )
        ax.text(
            left_x0 + left_w / 2, ry + rh * 0.56,
            org["short_name"],
            fontsize=M_H1,
            fontweight="bold", color="#FFFFFF", va="center", ha="center"
        )
        ax.text(
            left_x0 + left_w / 2, ry + rh * 0.24,
            textwrap.fill(org["full_name"], width=28),
            fontsize=M_H3,
            fontweight="bold", color="#E2E8F0", va="center", ha="center",
            linespacing=1.02
        )

        for s_idx, st in enumerate(STACK_STAGES):
            cx = get_col_x(s_idx)
            cw = stage_col_w

            cell_data = st["cells"][org["key"]]
            top_h1 = cell_data["h1"]
            mid_norm = cell_data["normal"]
            anti_list = cell_data["anti"]

            cbox = FancyBboxPatch(
                (cx, ry), cw, rh,
                boxstyle="round,pad=0.0,rounding_size=0.004",
                facecolor=org["cell_bg"],
                edgecolor=org["cell_edge"],
                linewidth=1.3
            )
            ax.add_patch(cbox)

            pad_x = 0.0018
            pad_top = 0.0026
            pad_bot = 0.0024
            inner_w = cw - 2 * pad_x
            x_left = cx + pad_x

            gap_z = 0.0018
            avail_h = rh - pad_top - pad_bot - 2 * gap_z
            t1_h = avail_h * 0.42
            t2_h = avail_h * 0.30
            anti_h = avail_h * 0.28

            t1_top_y = ry + rh - pad_top
            pill_gap = 0.0015
            ph = (t1_h - 2 * pill_gap) / 3.0
            for idx_1, kw in enumerate(top_h1[:3]):
                py = t1_top_y - (idx_1 + 1) * ph - idx_1 * pill_gap
                pill = FancyBboxPatch(
                    (x_left, py), inner_w, ph,
                    boxstyle="round,pad=0.0,rounding_size=0.0022",
                    facecolor=org["h1_bg"],
                    edgecolor=org["pill_edge"],
                    linewidth=0.90
                )
                ax.add_patch(pill)

                ax.text(
                    x_left + inner_w / 2, py + ph / 2,
                    kw,
                    fontsize=M_H2,
                    fontweight="bold",
                    color=org["h1_txt"],
                    va="center", ha="center"
                )

            t2_top_y = t1_top_y - t1_h - gap_z
            t2_row_h = t2_h / 3.0
            for idx_2, kw in enumerate(mid_norm[:3]):
                ty = t2_top_y - (idx_2 + 0.5) * t2_row_h
                ax.text(
                    x_left + 0.0012, ty,
                    f"• {kw}",
                    fontsize=M_H3,
                    fontweight="bold",
                    color=org["t2_txt"],
                    va="center", ha="left"
                )

            anti_bot_y = ry + pad_bot
            anti_box = FancyBboxPatch(
                (x_left, anti_bot_y), inner_w, anti_h,
                boxstyle="round,pad=0.0,rounding_size=0.0020",
                facecolor="#FFF1F2",
                edgecolor="#E11D48",
                linewidth=0.95,
                linestyle="--"
            )
            ax.add_patch(anti_box)

            arow_h = anti_h / 2.0
            for idx_a, akw in enumerate(anti_list[:2]):
                ty = anti_bot_y + anti_h - (idx_a + 0.5) * arow_h
                ax.text(
                    x_left + 0.0012, ty,
                    f"⚠ {akw}",
                    fontsize=M_H3,
                    fontweight="bold",
                    color="#881337",
                    va="center", ha="left"
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
        "# ANATOMY OF AI AGENTS 2026 (`10 Stages: 1. Silicon → 10. Multi-Agent` × `4 Organisms: LLM · RAG · Multimodal · Embodied AI`)",
        "",
        "> **What actually runs under the hood of an autonomous AI agent in 2026? Trace left to right across the 10 stages (`1. Silicon`, `2. Python`, `3. Data`, `4. Pre-Training`, `5. SFT`, `6. Post-Training`, `7. Test-Time`, `8. Context`, `9. Harness`, `10. Multi-Agent`) and top to bottom across the 4 distinct organisms (`LLM`, `RAG`, `Multimodal`, `Embodied AI`), with production `⚠ ANTI-PATTERNS & FAILURE MODES` embedded directly inside every cell.**  ",
        f"> **How to Read ([www.arianprabowo.com](https://www.arianprabowo.com) · Based on Haggai Roitman's *The Hitchhiker's Guide to Agentic AI*, `arXiv:2606.24937` · <sub>`{LAST_UPDATED_STR}`</sub>):** **`① COLUMNS (1 → 10):`** Follow `1. Silicon → 10. Multi-Agent` · **`② ROWS (4 ORGANISMS):`** Compare the `LLM` Core Spine against `RAG`, `Multimodal`, and `Embodied AI` · **`③ INSIDE EVERY CELL:`** Audit the red dashed **`⚠ ANTI-PATTERNS & FAILURE MODES`** box at the bottom of each cell.",
        "",
        "---",
        "",
        "## 1. Complete 10-Stage × 4-Organism Matrix Overview",
        "",
        "| Stage (`H1` Short Name · `H3` Full Name · Core Unit · Book Ref) | `LLM` (*Autoregressive Text, Code & Reasoning Language Models*) | `RAG` (*Hybrid Vector, Lexical & Graph Retrieval-Augmented Generation*) | `Multimodal` (*Vision, Audio, Speech, Video & Native Omni-Modal Models*) | `Embodied AI` (*GUI Computer Use, Physics World Models & VLA Robotics*) |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]

    for st in STACK_STAGES:
        st_num = st["stage"]
        col0 = (
            f"**{STAGE_H1_TITLES[st_num]}** — *{STAGE_FULL_NAMES[st_num]}*<br>"
            f"{st['desc']}<br>"
            f"• **{st['core_unit']}**<br>"
            f"• **Roitman Guide:** {st['book_ref']}"
        )
        row_cells = [col0]
        for org in ORGANISMS:
            d = st["cells"][org["key"]]
            h1_str = " · ".join(f"**{k}**" for k in d["h1"])
            norm_str = " · ".join(d["normal"])
            small_str = " · ".join(f"*{k}*" for k in d["small"])
            anti_str = " · ".join(f"**`⚠ {k}`**" for k in d["anti"])
            parts = [p for p in (h1_str, norm_str, small_str, anti_str) if p]
            row_cells.append("<br><br>".join(parts))
        lines.append("| " + " | ".join(row_cells) + " |")

    lines.extend([
        "",
        "---",
        "",
        "## 2. Stage-by-Stage Breakdown (`1. Silicon` → `10. Multi-Agent` Across All 4 Organisms)",
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
            "| Organism (`Short` — *Full Name*) | Top 3 Flagship Checkpoints (`H2`) | Core Stack & Mechanisms (`H3`) | Granular Specs (`H4`) | Inner `⚠ Anti-Patterns & Traps` |",
            "| :--- | :--- | :--- | :--- | :--- |",
        ])
        for org in ORGANISMS:
            d = st["cells"][org["key"]]
            h1_s = ", ".join(f"**`{k}`**" for k in d["h1"])
            nm_s = ", ".join(f"`{k}`" for k in d["normal"])
            sm_s = ", ".join(f"*{k}*" for k in d["small"])
            an_s = ", ".join(f"**`✕ {k}`**" for k in d["anti"])
            lines.append(
                f"| **{org['short_name']}** (*{org['full_name']}*) | {h1_s} | {nm_s} | {sm_s} | {an_s} |"
            )
        lines.append("")

    content = "\n".join(lines)
    OUT_MD.write_text(content, encoding="utf-8")
    print(f"Saved: {OUT_MD} ({OUT_MD.stat().st_size:,} bytes)")


if __name__ == "__main__":
    render_desktop_agent_anatomy_megachart()
    render_mobile_agent_anatomy_chart()
    write_agent_anatomy_markdown()
