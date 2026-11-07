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
#    Inside each cell (4-Part Anatomical Cell Design):
#      • h2_pill  (Zone 1, H2 = 24.00 pt): 100% Brand-Agnostic Functional Category (<= 18 chars)
#      • h3_pills (Zone 2, H3 = 14.83 pt): 2 Brand-Agnostic Core Mechanisms / Primitives (zero brand names)
#      • normal   (Zone 3, H4 =  9.17 pt): 3x2 = 6 Concrete Products, Models & OSS Tools inside "⚙ PRODUCTS, MODELS & OSS"
#      • anti     (Zone 4, H4 =  9.17 pt): 2x2 = 4 Concrete Failure Modes inside "⚠ ANTI-PATTERNS & TRAPS"
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
                "h2_pill": "Tensor Compute",
                "h3_pills": [
                    "HBM3e vs. On-Chip SRAM",
                    "Tiled Attention & FP8",
                ],
                "normal": [
                    "AI ACCELERATORS: | H200 · B200 · MI325X",
                    "CLOUD ASICs: | TPU v6e · Trainium2",
                    "KERNEL LANGUAGES: | CUDA · Triton · CUTLASS",
                    "ATTENTION KERNEL: | FlashAttention-3",
                    "CLUSTER FABRIC: | NVLink 5 · InfiniBand",
                    "LOW-BIT ENGINE: | TransformerEngine FP8",
                ],
                "anti": [
                    "HBM Bandwidth Wall",
                    "CUDA OOM Crashes",
                    "Silent SDC Bit-Flips",
                    "Straggler GPU Stall",
                ],
            },
            "rag": {
                "h2_pill": "Vector & SSD I/O",
                "h3_pills": [
                    "GPU Graph & SIMD Scan",
                    "Direct NVMe Disk I/O",
                ],
                "normal": [
                    "GPU VECTOR INDEX: | NVIDIA cuVS · RAFT",
                    "CPU SIMD KERNELS: | Intel AVX-512 · AMX",
                    "ASYNC DISK I/O: | NVMe Gen5 · io_uring",
                    "ON-DISK GRAPH: | DiskANN · SPANN",
                    "DMA STORAGE: | GPUDirect Storage",
                    "MEMORY POOLING: | RoCEv2 · CXL 3.0",
                ],
                "anti": [
                    "SSD Random-Read Thrash",
                    "HNSW Exceeding DRAM",
                    "PCIe Index Bottleneck",
                    "NUMA Socket Latency",
                ],
            },
            "multimodal": {
                "h2_pill": "Media Codec DSP",
                "h3_pills": [
                    "HW Video/Audio Decode",
                    "3D Patch & Conv Tiling",
                ],
                "normal": [
                    "GPU MEDIA CODEC: | NVIDIA NVDEC / NVENC",
                    "UNIFIED RAM SoC: | Apple M4 Media Engine",
                    "MOBILE / EDGE DSP: | Qualcomm Hexagon NPU",
                    "ZERO-COPY VIDEO: | GPUDirect Video DMA",
                    "VISION KERNELS: | cuDNN · TensorRT-MM",
                    "CAMERA / RTC BUS: | MIPI CSI-2 · WebRTC",
                ],
                "anti": [
                    "CPU Video Decode Stall",
                    "4K Frame PCIe Flood",
                    "Audio Sample Clock Drift",
                    "Video Thermal Throttle",
                ],
            },
            "embodied": {
                "h2_pill": "Edge RT Compute",
                "h3_pills": [
                    "1kHz Sensor ISP & Bus",
                    "GPU Rigid/Soft Physics",
                ],
                "normal": [
                    "ROBOTICS SoC: | NVIDIA Jetson Thor",
                    "GPU PHYSICS SIM: | PhysX 5 · NVIDIA Warp",
                    "REAL-TIME FIELD: | EtherCAT · CAN-FD",
                    "LOW-POWER NPU: | Qualcomm RB5 · Hailo",
                    "3D LIDAR SENSOR: | Ouster · Velodyne",
                    "DEPTH CAMERAS: | RealSense · ZED 2i",
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
                "h2_pill": "Serving Runtime",
                "h3_pills": [
                    "Deterministic Lockfiles",
                    "Paged KV & Graph Capture",
                ],
                "normal": [
                    "ENV & PKG MGR: | uv · Pixi · Conda · pip",
                    "TENSOR FRAMEWORK: | PyTorch 2.x · JAX",
                    "SERVING ENGINE: | vLLM · SGLang",
                    "C++ LLM RUNTIME: | TRT-LLM · llama.cpp",
                    "GRAPH COMPILER: | torch.compile · XLA",
                    "CODE SANDBOX: | E2B · Firecracker VM",
                ],
                "anti": [
                    "CUDA ABI & Wheel Hell",
                    "Unsandboxed Host RCE",
                    "KV-Cache Preemption",
                    "pip Breaking flash-attn",
                ],
            },
            "rag": {
                "h2_pill": "Index Bindings",
                "h3_pills": [
                    "Zero-Copy Columnar IPC",
                    "Async Vector/DB Drivers",
                ],
                "normal": [
                    "ANN LIBRARIES: | FAISS · HNSWLib · Lance",
                    "COLUMNAR MEMORY: | Apache Arrow · Parquet",
                    "IN-PROCESS OLAP: | DuckDB · Polars",
                    "ASYNC SQL DRIVER: | psycopg3 · asyncpg",
                    "VECTOR CLIENTS: | qdrant-client · pymilvus",
                    "LEXICAL & EMBED: | Tantivy · BM25S · ONNX",
                ],
                "anti": [
                    "Python GIL Chunk Lock",
                    "Pickle Index RCE Exploit",
                    "DB Pool Exhaustion",
                    "Pandas Copy RAM Blowup",
                ],
            },
            "multimodal": {
                "h2_pill": "Stream Pipelines",
                "h3_pills": [
                    "Zero-Copy Tensor Decode",
                    "Async Media Ring Buffers",
                ],
                "normal": [
                    "VIDEO DEMUXING: | FFmpeg · PyAV · Decord",
                    "VISION TRANSFORMS: | OpenCV · torchvision",
                    "AUDIO DSP LIBS: | torchaudio · librosa",
                    "GPU DATA LOADER: | NVIDIA DALI · Kornia",
                    "FAST IMAGE I/O: | Pillow-SIMD · Albument.",
                    "SPEECH & VAD: | whisper.cpp · Silero",
                ],
                "anti": [
                    "OpenCV BGR vs RGB Bug",
                    "FFmpeg Zombie Leaks",
                    "Audio Buffer Underruns",
                    "Pillow Bomb DoS Crash",
                ],
            },
            "embodied": {
                "h2_pill": "Middleware & IPC",
                "h3_pills": [
                    "Pub-Sub DDS & Zero-Copy",
                    "Browser & Physics APIs",
                ],
                "normal": [
                    "ROBOT MIDDLEWARE: | ROS 2 · CycloneDDS",
                    "BROWSER CONTROL: | Playwright · Chrome CDP",
                    "RL ENV INTERFACE: | Gymnasium · PettingZoo",
                    "PHYSICS ENGINES: | MuJoCo · Isaac Lab",
                    "KINEMATICS & 3D: | Pinocchio · Open3D",
                    "ROBOT SDK & BUS: | LeRobot · Eclipse Zenoh",
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
                "h2_pill": "Text & BPE Corpus",
                "h3_pills": [
                    "MinHash Dedup & Filter",
                    "Byte-Level BPE Tokenize",
                ],
                "normal": [
                    "WEB TEXT CORPORA: | FineWeb-Edu · Dolma",
                    "CODE & MATH SETS: | The Stack v2 · DCLM",
                    "BPE TOKENIZERS: | Tiktoken · SentencePiece",
                    "CURATION ENGINES: | Datatrove · NeMo Curat.",
                    "SYNTHETIC CORPORA: | Nemotron-CC · Cosmop.",
                    "PII & QUALITY: | Presidio · FastText",
                ],
                "anti": [
                    "Synthetic Model Collapse",
                    "Test-Set Contamination",
                    "Tokenizer Glitch Tokens",
                    "PII Baked into Weights",
                ],
            },
            "rag": {
                "h2_pill": "Doc Chunking & ETL",
                "h3_pills": [
                    "Layout-Aware & AST Split",
                    "ACL Metadata & CDC Sync",
                ],
                "normal": [
                    "PDF LAYOUT ETL: | Docling · Marker PDF",
                    "DOC PARSERS: | LlamaParse · Unstruct.",
                    "CODE AST CHUNKER: | Tree-sitter AST Split",
                    "ACADEMIC OCR: | Grobid · Nougat OCR",
                    "SEMANTIC CHUNKER: | Chonkie · LangChain",
                    "CDC STREAM SYNC: | Debezium · Airbyte",
                ],
                "anti": [
                    "Mid-Table Naive Split",
                    "PDF Column Scramble",
                    "Stale Deleted Vectors",
                    "Missing ACL Metadata",
                ],
            },
            "multimodal": {
                "h2_pill": "Modal Alignment",
                "h3_pills": [
                    "Contrastive Pair Filter",
                    "Scene Cut & Diarization",
                ],
                "normal": [
                    "IMAGE-TEXT SETS: | DataComp · OBELICS",
                    "DENSE CAPTIONS: | ShareGPT4V · LAION-5B",
                    "SPEECH DIARIZE: | WhisperX · pyannote",
                    "NEURAL CODECS: | EnCodec · Mimi · DAC",
                    "VIDEO SCENE CUT: | PySceneDetect · CLIP",
                    "DOCUMENT OCR: | PaddleOCR · Surya",
                ],
                "anti": [
                    "Mismatched Alt-Text",
                    "Low-DPI OCR Misreads",
                    "Demographic Bias Skew",
                    "Audio Crosstalk Bleed",
                ],
            },
            "embodied": {
                "h2_pill": "Trajectory Logs",
                "h3_pills": [
                    "Teleop & Action Sync",
                    "DOM + Screen Traces",
                ],
                "normal": [
                    "ROBOT TRAJECTORY: | Open X-Embodiment",
                    "MANIPULATION SET: | DROID · BridgeData V2",
                    "EGOCENTRIC VIDEO: | Ego4D · Epic-Kitchens",
                    "GUI ACTION LOGS: | Mind2Web · OSWorld",
                    "BIMANUAL TELEOP: | ALOHA · GELLO Rig",
                    "TRAJECTORY STORE: | RLDS · LeRobot Parquet",
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
                "h2_pill": "Sparse MoE & Attn",
                "h3_pills": [
                    "Routed MoE & Latent KV",
                    "3D/4D Tensor Parallel",
                ],
                "normal": [
                    "OPEN MoE MODELS: | DeepSeek-V3 · Llama 4",
                    "DENSE & MoE LLMs: | Qwen 3 · Mistral Large",
                    "3D/4D TRAINERS: | Megatron-LM · TorchTitan",
                    "SHARDED DATA PAR: | DeepSpeed ZeRO · FSDP2",
                    "SSM / HYBRID ARCH: | Mamba-2 · Jamba · RWKV",
                    "COMPACT DENSE: | Gemma 3 · Nemotron-4",
                ],
                "anti": [
                    "Loss Spikes & NaN Crash",
                    "MoE Routing Collapse",
                    "Pipeline Bubble Stall",
                    "RoPE Length Collapse",
                ],
            },
            "rag": {
                "h2_pill": "Dense Bi-Encoders",
                "h3_pills": [
                    "Contrastive InfoNCE Loss",
                    "Late-Interaction & MRL",
                ],
                "normal": [
                    "DENSE EMBEDDERS: | BGE-M3 · NV-Embed-v2",
                    "LATE INTERACTION: | ColBERTv2 · PLAID",
                    "SPARSE LEXICAL: | SPLADE-v3 · BM25S",
                    "MATRYOSHKA EMBED: | Nomic-Embed · GTE",
                    "COMMERCIAL EMBED: | Cohere Embed v3 · E5",
                    "RETRIEVAL EVALS: | MTEB · BEIR Benchmark",
                ],
                "anti": [
                    "Embedding Anisotropy",
                    "False-Negative Batches",
                    "Domain Acronym Blindness",
                    "512-Token Truncation",
                ],
            },
            "multimodal": {
                "h2_pill": "Omni Backbones",
                "h3_pills": [
                    "Early-Fusion Any-to-Any",
                    "Flow-Matching & 3D RoPE",
                ],
                "normal": [
                    "VISION ENCODERS: | SigLIP-2 · DINOv2 ViT",
                    "OPEN VLM BASES: | Qwen2.5-VL · InternVL3",
                    "NATIVE OMNI LLMs: | GPT-4o · Gemini 2.5 Pro",
                    "FLOW / DiT GEN: | Flux.1 · Wan2.1 DiT",
                    "FULL-DUPLEX OMNI: | Moshi · Chameleon",
                    "MULTIMODAL EVAL: | MMMU · MathVista",
                ],
                "anti": [
                    "Modality Text-IQ Drop",
                    "Bag-of-Patches Blindness",
                    "4K Quadratic ViT Blowup",
                    "Small-Text Patch Blur",
                ],
            },
            "embodied": {
                "h2_pill": "World & VLA Base",
                "h3_pills": [
                    "Latent Physics Prediction",
                    "Visuomotor Token Fusion",
                ],
                "normal": [
                    "FLOW VLA MODELS: | π0 (Pi-Zero) · OpenVLA",
                    "GENERALIST VLA: | RT-2 · Octo · CrossFormer",
                    "WORLD MODELS: | V-JEPA 2 · NVIDIA Cosmos",
                    "INTERACTIVE SIM: | Google Genie 2 · UniSim",
                    "3D POINT ENCODER: | PointNet++ · Uni3D",
                    "EMBODIED SUITES: | Habitat 3.0 · ManiSkill",
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
                "h2_pill": "Instruction Tuning",
                "h3_pills": [
                    "Chat Template & Packing",
                    "LoRA / QLoRA & Masking",
                ],
                "normal": [
                    "SFT FRAMEWORKS: | TRL · Axolotl · Unsloth",
                    "MODULAR TRAINERS: | TorchTune · LLaMA-Fact.",
                    "ADAPTER LIBRARIES: | HF PEFT · LoRA · DoRA",
                    "WEIGHT MERGING: | MergeKit (SLERP/TIES)",
                    "CHAT TEMPLATES: | ChatML · ShareGPT · Tulu",
                    "FORMAT BENCHMARK: | IFEval · Arena-Hard",
                ],
                "anti": [
                    "Unmasked Prompt Loss",
                    "EOS/BOS Template Loops",
                    "Packed Attention Bleed",
                    "Catastrophic Forgetting",
                ],
            },
            "rag": {
                "h2_pill": "Retriever Tuning",
                "h3_pills": [
                    "Hard-Negative Cross-Enc",
                    "Distractor-Robust RAFT",
                ],
                "normal": [
                    "CROSS-ENCODERS: | bge-reranker · Cohere",
                    "GROUNDED SFT: | RAFT · RankZephyr",
                    "UNIFIED EMBED+GEN: | GritLM · Instructor",
                    "EMBEDDING TUNER: | Sentence-Transformers",
                    "LIGHT RERANKERS: | FlashRank · Rerankers",
                    "RAG SFT EVALS: | RAGBench · RGB Eval",
                ],
                "anti": [
                    "Memorizing Stale Facts",
                    "Believing Distractors",
                    "Fake [1] Citation Tags",
                    "Narrow Query Overfit",
                ],
            },
            "multimodal": {
                "h2_pill": "Visual & Voice SFT",
                "h3_pills": [
                    "Dynamic High-Res Tiling",
                    "Bounding-Box & Voice SFT",
                ],
                "normal": [
                    "ANYRES VLM SFT: | LLaVA-OneVision · Molmo",
                    "SPEECH-LLM SFT: | Qwen2-Audio · Ultravox",
                    "COMPACT VLM SFT: | PaliGemma 2 · Pixtral",
                    "GROUNDING BBOX: | Florence-2 · GroundDINO",
                    "VISUAL PROMPTING: | Set-of-Mark (SoM)",
                    "DOC & CHART EVAL: | DocVQA · ChartQA",
                ],
                "anti": [
                    "Blind Visual Guessing",
                    "Projector Detail Loss",
                    "BBox Coordinate Drift",
                    "Voice SFT Hurting Math",
                ],
            },
            "embodied": {
                "h2_pill": "Behavior Cloning",
                "h3_pills": [
                    "k-Step Action Chunking",
                    "GUI Pixel-to-Action SFT",
                ],
                "normal": [
                    "ACTION CHUNKING: | ACT · ALOHA Policy",
                    "DIFFUSION POLICY: | Diffusion Policy · DP3",
                    "GUI GROUNDING: | OS-Atlas · SeeClick",
                    "GUI ACTION MODELS: | ShowUI · Aguvis · CogAg.",
                    "BIMANUAL VLA SFT: | RDT-1B · Octo Tune",
                    "BC BENCHMARKS: | LIBERO · Meta-World",
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
                "h2_pill": "Alignment & RLVR",
                "h3_pills": [
                    "Group-Relative RL (GRPO)",
                    "Pairwise Preference DPO",
                ],
                "normal": [
                    "RLVR REASONERS: | DeepSeek-R1 · Open-R1",
                    "RLVR FRAMEWORKS: | veRL · OpenRLHF · NeMo",
                    "PREFERENCE TUNER: | TRL DPO / KTO / SimPO",
                    "REWARD & ASYNC RL: | Prime-RL · Skywork-RM",
                    "VERIFIABLE EVALS: | LiveCodeBench · AIME",
                    "ALIGNMENT EVALS: | RewardBench · AlpacaEv.",
                ],
                "anti": [
                    "Reward Hacking & Bloat",
                    "Policy Entropy Collapse",
                    "Zero-Variance Advantage",
                    "Judge Sycophancy Bias",
                ],
            },
            "rag": {
                "h2_pill": "Search & Cite RL",
                "h3_pills": [
                    "Multi-Hop Search RLVR",
                    "NLI Faithfulness Reward",
                ],
                "normal": [
                    "SEARCH RL MODELS: | Search-R1 · R1-Searcher",
                    "QUERY REWRITE RL: | DeepRetrieval · ReZero",
                    "NLI VERIFIERS: | AlignScore · LettuceDet.",
                    "RAG JUDGE SUITES: | RAGAS · TruLens · ARES",
                    "MULTI-HOP QA SET: | HotpotQA · MuSiQue",
                    "HALLUCINATION QA: | RAGTruth · HaluEval",
                ],
                "anti": [
                    "Redundant Search Loops",
                    "Cherry-Picking Evidence",
                    "Over-Abstention Refusal",
                    "Uncited Extrapolation",
                ],
            },
            "multimodal": {
                "h2_pill": "Perceptual RL",
                "h3_pills": [
                    "IoU & OCR Verifiable RL",
                    "Diffusion & Fact DPO",
                ],
                "normal": [
                    "VISUAL RLVR MODELS: | R1-OneVision · VLM-R1",
                    "VLM FACT ALIGN: | RLAIF-V · POVID · BPO",
                    "DIFFUSION RL: | Diffusion-DPO · FlowGRPO",
                    "MULTIMODAL RLHF: | InternVL-RL · LLaVA-RL",
                    "OBJECT HALLUC QA: | POPE · HallusionBench",
                    "VLM SAFETY EVALS: | MM-SafetyBench · SPA-VL",
                ],
                "anti": [
                    "Text-Prior Blind Guess",
                    "Oversaturated Image Hack",
                    "Benign Image Refusals",
                    "Voice Barge-In Jitter",
                ],
            },
            "embodied": {
                "h2_pill": "Sim-to-Real RL",
                "h3_pills": [
                    "Domain-Randomized PPO",
                    "Residual & Safe HIL-RL",
                ],
                "normal": [
                    "GPU RL TRAINERS: | Isaac Gym · CleanRL",
                    "REAL-WORLD HIL RL: | HIL-SERL · RLPD",
                    "LLM REWARD SYNTH: | Eureka · DrEureka",
                    "WEB / OS RL ENVS: | WebArena · OSWorld-RL",
                    "LEGGED LOCOMOTION: | RSL-RL · Legged-Gym",
                    "SAFE CONTROL RL: | Safe-RL · ControlBarrier",
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
                "h2_pill": "System-2 Search",
                "h3_pills": [
                    "Deliberative CoT Tokens",
                    "Process RM & Tree Search",
                ],
                "normal": [
                    "FRONTIER REASONER: | OpenAI o3 / o4-mini",
                    "OPEN REASONERS: | DeepSeek-R1 · QwQ-32B",
                    "EXTENDED THINKING: | Claude 4.6 · Gemini 2.5",
                    "TREE & BUDGET: | LATS · s1 Budget-Force",
                    "PROCESS VERIFIER: | Math-Shepherd · SkyPRM",
                    "SYSTEM-2 EVALS: | ARC-AGI-2 · AIME · GPQA",
                ],
                "anti": [
                    "10x Overthinking Burn",
                    "PRM Verifier Hacking",
                    "Self-Correction Regress",
                    "Unfaithful Post-Hoc CoT",
                ],
            },
            "rag": {
                "h2_pill": "Iterative Search",
                "h3_pills": [
                    "Query Decomp & Rewrite",
                    "Reciprocal Rank & Verify",
                ],
                "normal": [
                    "REFLECTIVE RAG: | Self-RAG · CRAG",
                    "INTERLEAVED CoT: | IRCoT · FLARE · HyDE",
                    "NEURAL RERANKER: | Cohere Rerank 3.5",
                    "TOKEN RERANKER: | ColBERT PLAID Rerank",
                    "LISTWISE LLM RANK: | RankGPT · MonoT5",
                    "REASONING RAG QA: | BRIGHT · FRAMES Eval",
                ],
                "anti": [
                    "Infinite Rewrite Loops",
                    "HyDE Hallucination Drift",
                    "Reranker p99 SLA Blowup",
                    "Multi-Hop Error Cascade",
                ],
            },
            "multimodal": {
                "h2_pill": "Active Perception",
                "h3_pills": [
                    "Iterative Crop & Zoom",
                    "Best-of-N Visual Verify",
                ],
                "normal": [
                    "VISUAL CoT ZOOM: | OpenAI o3 Visual CoT",
                    "GUIDED CROP SEARCH: | V* (V-Star) Search",
                    "VISUAL PROGRAM: | ViperGPT · VisProg",
                    "TOOL-USING VLMs: | LLaVA-Plus · CogCom",
                    "DIFFUSION SCALING: | ControlNet Tile · CFG",
                    "PERCEPTION EVALS: | BLINK · V-Bench Eval",
                ],
                "anti": [
                    "Zooming Irrelevant Bg",
                    "Blurry Crop Hallucinate",
                    "High-Res Token Overflow",
                    "CFG Over-Step Artifacts",
                ],
            },
            "embodied": {
                "h2_pill": "Predictive Rollout",
                "h3_pills": [
                    "Receding-Horizon MPC",
                    "World-Model Tree Search",
                ],
                "normal": [
                    "SAMPLING PLANNER: | MPPI · CEM Rollouts",
                    "LATENT WORLD MPC: | TD-MPC2 · DreamerV3",
                    "3D VALUE MAPS: | VoxPoser · Code-as-Pol.",
                    "AFFORDANCE PLAN: | SayCan · InnerMonologue",
                    "MOTION PLANNERS: | MoveIt 2 · Drake MPC",
                    "GUI TREE SEARCH: | AgentQ · WebTree MCTS",
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
                "h2_pill": "Memory & Tool Bus",
                "h3_pills": [
                    "4-Tier Memory Hierarchy",
                    "JSON-RPC Tool & Skill Bus",
                ],
                "normal": [
                    "TOOL PROTOCOL: | Model Context Protocol",
                    "AGENTIC MEMORY: | Letta (MemGPT) · Mem0",
                    "TEMPORAL GRAPH: | Zep · LangMem · Cognee",
                    "PROGRESSIVE SKILL: | SKILL.md · AGENTS.md",
                    "KV PREFIX CACHE: | Anthropic Prompt Cache",
                    "MEMORY BENCHMARK: | LoCoMo · LongMemEval",
                ],
                "anti": [
                    "Lost-in-the-Middle Rot",
                    "100+ MCP Schema Bloat",
                    "SKILL.md / MCP Rug-Pull",
                    "Poisoned Memory State",
                ],
            },
            "rag": {
                "h2_pill": "Hybrid & Graph KB",
                "h3_pills": [
                    "Dense + Lexical Fusion",
                    "Entity-Relation Graph KB",
                ],
                "normal": [
                    "VECTOR DATABASES: | Qdrant · Milvus · Weav.",
                    "HYBRID SQL / DOC: | pgvector · Elasticsearch",
                    "GRAPH RAG ENGINE: | MS GraphRAG · LightRAG",
                    "PROPERTY GRAPHS: | Neo4j · Memgraph",
                    "PROMPT COMPRESS: | LLMLingua-2 · REFRAG",
                    "RAG ORCHESTRATOR: | LlamaIndex · Haystack",
                ],
                "anti": [
                    "Indirect Prompt Inject",
                    "Cross-Tenant Vector Leak",
                    "Context Stuffing Noise",
                    "GraphRAG Indexing Cost",
                ],
            },
            "multimodal": {
                "h2_pill": "Token & KV Pruning",
                "h3_pills": [
                    "ViT Patch Merge & Drop",
                    "Streaming Video KV Ring",
                ],
                "normal": [
                    "PATCH MERGING: | ToMe (Token Merging)",
                    "VLM TOKEN PRUNE: | FastV · PruMerge",
                    "STREAMING KV RING: | StreamingLLM · InfiniPot",
                    "VIDEO INDEX API: | TwelveLabs · Marengo",
                    "AUDIO-TEXT ALIGN: | Whisper Timestamp Idx",
                    "LONG VIDEO EVALS: | Video-MME · MLVU Eval",
                ],
                "anti": [
                    "10m Video Filling 128k",
                    "Pruning Tiny OCR Text",
                    "Base64 JSON-RPC Crash",
                    "Audio-Video Sync Drift",
                ],
            },
            "embodied": {
                "h2_pill": "Spatial Scene Map",
                "h3_pills": [
                    "3D Voxel & Gaussian Map",
                    "Pruned DOM & AXTree",
                ],
                "normal": [
                    "RADIANCE FIELDS: | 3D Gaussian Splatting",
                    "VOXEL OCCUPANCY: | OctoMap · nvblox",
                    "3D SCENE GRAPHS: | Hydra · ConceptGraphs",
                    "DOM DISTILLATION: | Browser-Use DOM Pruner",
                    "ACCESSIBILITY TREE: | Playwright AXTree · SoM",
                    "SLAM LOCALIZATION: | RTAB-Map · ORB-SLAM3",
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
                "h2_pill": "Observe-Act Loop",
                "h3_pills": [
                    "Stateful Graph & Retries",
                    "Sandboxed Test-Fix Loop",
                ],
                "normal": [
                    "CLI CODE AGENTS: | Claude Code · Codex",
                    "IDE CODE AGENTS: | Cursor · Windsurf · Cline",
                    "STATEFUL GRAPHS: | LangGraph · PydanticAI",
                    "OPEN SWE AGENTS: | OpenHands · SWE-agent",
                    "DURABLE WORKFLOW: | Temporal · Inngest",
                    "CODING BENCHMARK: | SWE-bench Verified",
                ],
                "anti": [
                    "Deleting Failing Tests",
                    "Infinite Loop Token Burn",
                    "God-Node State Bloat",
                    "IDE Auto-Approve RCE",
                ],
            },
            "rag": {
                "h2_pill": "Plan-Verify RAG",
                "h3_pills": [
                    "Adaptive Query Routing",
                    "Citation & Span Verify",
                ],
                "normal": [
                    "DEEP RESEARCHERS: | OpenAI Deep Research",
                    "SEARCH SYNTHESIS: | Perplexity Pro · STORM",
                    "AGENTIC RAG DAG: | LangGraph CRAG · DSPy",
                    "AGENT SEARCH API: | Tavily · Exa · Firecrawl",
                    "FAITHFULNESS GATE: | Patronus Lynx · NeMo G.",
                    "RESEARCH BENCH: | GAIA · FRAMES Eval",
                ],
                "anti": [
                    "Rephrase Search Thrash",
                    "Silent Hallucination",
                    "Citation Laundering",
                    "Unbounded Research Lag",
                ],
            },
            "multimodal": {
                "h2_pill": "Duplex Media Loop",
                "h3_pills": [
                    "Full-Duplex VAD Barge-In",
                    "Render-Inspect-Fix Loop",
                ],
                "normal": [
                    "VOICE HARNESSES: | LiveKit Agents · Pipecat",
                    "DUPLEX SPEECH API: | OpenAI Realtime API",
                    "NODE GEN GRAPH: | ComfyUI · InvokeAI",
                    "LOW-LATENCY TTS: | ElevenLabs · Cartesia",
                    "MEDIA PROVENANCE: | C2PA · SynthID",
                    "DUPLEX BENCHMARK: | Full-Duplex-Bench",
                ],
                "anti": [
                    "Talking Over User Voice",
                    "Transcribing Own TTS",
                    "VLM Breaking CSS Layout",
                    ">3s Cascaded Voice Lag",
                ],
            },
            "embodied": {
                "h2_pill": "Closed-Loop Act",
                "h3_pills": [
                    "Screen-Action-Verify",
                    "2Hz VLM + 50Hz Control",
                ],
                "normal": [
                    "DESKTOP AGENTS: | Anthropic Computer Use",
                    "BROWSER AGENTS: | OpenAI Operator · CUA",
                    "GUI PARSER & VLA: | UI-TARS · OmniParser v2",
                    "WEB AUTOMATION: | Browser-Use · Skyvern",
                    "ROBOT NAV STACK: | ROS 2 Nav2 · MoveIt 2",
                    "OS AGENT BENCH: | OSWorld · WindowsArena",
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
                "h2_pill": "Multi-Agent Graph",
                "h3_pills": [
                    "Orchestrator-Worker DAG",
                    "Agent-to-Agent RPC Bus",
                ],
                "normal": [
                    "INTER-AGENT RPC: | Google A2A Protocol",
                    "AGENT-USER UI BUS: | AG-UI · CopilotKit",
                    "ROLE SWARM SDKs: | CrewAI · AutoGen (AG2)",
                    "GRAPH SWARM SDKs: | LangGraph Swarm · OAI",
                    "SANDBOX WORKTREE: | Git Worktree · Dagger",
                    "ROLEPLAY SWARMS: | ChatDev · MetaGPT",
                ],
                "anti": [
                    "Swarm Echo Hallucinate",
                    "O(N²) Chatty Token Burn",
                    "Confused Deputy Breach",
                    "Worktree Merge Conflict",
                ],
            },
            "rag": {
                "h2_pill": "Federated KB Mesh",
                "h3_pills": [
                    "Cross-Silo Query Router",
                    "OAuth ACL Token Pass",
                ],
                "normal": [
                    "ENTERPRISE SEARCH: | Glean · Onyx (Danswer)",
                    "MULTI-AGENT RAG: | LlamaIndex AgentWorkfl.",
                    "FEDERATED ROUTER: | Federated-MCP · GraphQL",
                    "ZANZIBAR RBAC: | SpiceDB · OpenFGA ACL",
                    "FEDERATED LAKE: | Apache Iceberg · Trino",
                    "ENTERPRISE BENCH: | Enterprise RAG-Bench",
                ],
                "anti": [
                    "Circular Citation Loop",
                    "Cross-Dept ACL Leakage",
                    "Duplicate Doc Fetching",
                    "Dropping Minority Facts",
                ],
            },
            "multimodal": {
                "h2_pill": "Cross-Modal Studio",
                "h3_pills": [
                    "Director-Storyboard DAG",
                    "Multi-Track Sync & QA",
                ],
                "normal": [
                    "VIDEO GEN MODELS: | Runway Gen-4 · Sora",
                    "CINEMA DI-T MODELS: | Google Veo 2 · Kling",
                    "AUDIO / MUSIC GEN: | Suno · Udio · StableAud.",
                    "WORKFLOW CLOUD: | ComfyUI Swarm · Fal.ai",
                    "TIMELINE ASSEMBLY: | FFmpeg · OTIO Timeline",
                    "VIDEO GEN BENCH: | MovieGenBench · VBench",
                ],
                "anti": [
                    "Character Identity Drift",
                    "Voice Promising Failed Op",
                    "Audio-Video Lip Desync",
                    "Runaway Render Spend",
                ],
            },
            "embodied": {
                "h2_pill": "Fleet Coordination",
                "h3_pills": [
                    "Conflict-Free Path Plan",
                    "Shared Spatial Twin",
                ],
                "normal": [
                    "FLEET MIDDLEWARE: | Open-RMF Robotics",
                    "DIGITAL TWIN CTRL: | NVIDIA Isaac Mission",
                    "MAPF PATH SOLVER: | CBS / LaCAM Solvers",
                    "FLEET TELEMETRY: | Foxglove · Formant",
                    "INTEROP STANDARD: | VDA 5050 · AWS RoboRun.",
                    "SWARM SIM BENCH: | Flatland · VMAS Eval",
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
        "③ CELL ANATOMY: Brand-Agnostic Category (H2) + Mechanisms (H3) + ⚙ PRODUCTS & OSS Box (H4) + ⚠ ANTI-PATTERNS Box (H4)",
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
        "Category (H2) · Mechs (H3)\n⚙ Products · ⚠ Traps (H4)",
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

        # Short Name (<= 2 words) in H1 (= 38.83 pt): "1. Silicon", "2. Python", ...
        ax.text(
            lx + stage_col_w / 2, b_top_y - banner_h * 0.35,
            STAGE_H1_TITLES[st_num],
            fontsize=H1,
            fontweight="bold",
            color="#FFFFFF",
            va="center", ha="center"
        )

        # Full Name (<= 10 words, wrapped onto 2 lines) at bottom of banner in H4 (= 9.17 pt)
        ax.text(
            lx + stage_col_w / 2, b_top_y - banner_h * 0.77,
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
    #    with 4-Zone Anatomical Cell Design:
    #      Zone 1 (H2 = 24.00 pt): Brand-Agnostic Category Banner
    #      Zone 2 (H3 = 14.83 pt): 2 Brand-Agnostic Core Mechanisms
    #      Zone 3 (H4 =  9.17 pt): Framed "⚙ PRODUCTS, MODELS & OSS" Sub-Box (3x2 = 6 items)
    #      Zone 4 (H4 =  9.17 pt): Framed "⚠ ANTI-PATTERNS & TRAPS" Sub-Box (2x2 = 4 items)
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
            h2_cat_str = cell_data["h2_pill"]
            h3_mechs = cell_data["h3_pills"]
            prod_list = cell_data["normal"]
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
            pad_top = 0.0020
            pad_bot = 0.0020
            inner_w = cw - 2 * pad_x
            x_left = cx + pad_x

            gap_z = 0.0014
            avail_h = rh - pad_top - pad_bot - 3 * gap_z
            z1_h = avail_h * 0.148   # Zone 1: Brand-Agnostic Category Banner (H2 = 24.00 pt)
            z2_h = avail_h * 0.197   # Zone 2: 2 Brand-Agnostic Core Mechanisms (H3 = 14.83 pt)
            z3_h = avail_h * 0.365   # Zone 3: Framed "⚙ PRODUCTS, MODELS & OSS" Sub-Box (3x2 in H4 = 9.17 pt)
            anti_h = avail_h * 0.290 # Zone 4: Framed "⚠ ANTI-PATTERNS & TRAPS" Sub-Box (2x2 in H4 = 9.17 pt)

            # -----------------------------------------------------------------
            # Zone 1: Brand-Agnostic Category Banner in H2 (= 24.00 pt)
            # -----------------------------------------------------------------
            z1_top_y = ry + rh - pad_top
            z1_bot_y = z1_top_y - z1_h
            p_h2 = FancyBboxPatch(
                (x_left, z1_bot_y), inner_w, z1_h,
                boxstyle="round,pad=0.0,rounding_size=0.0024",
                facecolor=org["h2_bg"],
                edgecolor="#FFFFFF",
                linewidth=1.15
            )
            ax.add_patch(p_h2)
            ax.text(
                x_left + inner_w / 2, z1_bot_y + z1_h / 2,
                h2_cat_str,
                fontsize=H2,
                fontweight="bold",
                color=org["h2_txt"],
                va="center", ha="center"
            )

            # -----------------------------------------------------------------
            # Zone 2: 2 Brand-Agnostic Mechanism Bars in H3 (= 14.83 pt)
            # -----------------------------------------------------------------
            z2_top_y = z1_bot_y - gap_z
            pill_gap = 0.0012
            ph3 = (z2_h - pill_gap) / 2.0
            for idx_p, kw in enumerate(h3_mechs[:2]):
                py = z2_top_y - (idx_p + 1) * ph3 - idx_p * pill_gap
                pill = FancyBboxPatch(
                    (x_left, py), inner_w, ph3,
                    boxstyle="round,pad=0.0,rounding_size=0.0020",
                    facecolor=org["h3_bg"],
                    edgecolor=org["pill_edge"],
                    linewidth=0.95
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
            # Zone 3 (INSIDE): Framed "⚙ PRODUCTS, MODELS & OSS" Sub-Box (3x2 in H4 = 9.17 pt)
            # -----------------------------------------------------------------
            z3_top_y = z2_top_y - z2_h - gap_z
            z3_bot_y = z3_top_y - z3_h
            prod_box = FancyBboxPatch(
                (x_left, z3_bot_y), inner_w, z3_h,
                boxstyle="round,pad=0.0,rounding_size=0.0022",
                facecolor="#FFFFFF",
                edgecolor=org["cell_edge"],
                linewidth=1.15
            )
            ax.add_patch(prod_box)

            phdr_h = z3_h * 0.205
            phdr_box = FancyBboxPatch(
                (x_left + 0.0004, z3_top_y - phdr_h), inner_w - 0.0008, phdr_h,
                boxstyle="round,pad=0.0,rounding_size=0.0016",
                facecolor=org["hdr_bg"],
                edgecolor=org["pill_edge"],
                linewidth=0.55
            )
            ax.add_patch(phdr_box)
            ax.text(
                x_left + inner_w / 2, z3_top_y - phdr_h * 0.52,
                "⚙ SUB-CATEGORY ▸ PRODUCTS & OSS",
                fontsize=H4,
                fontweight="bold",
                color="#FEF08A",
                va="center", ha="center"
            )

            pbody_top_y = z3_top_y - phdr_h
            pbody_h = z3_h - phdr_h
            t2_row_h = pbody_h / 3.0
            t2_col_w = inner_w / 2.0

            ax.plot(
                [x_left + t2_col_w, x_left + t2_col_w],
                [z3_bot_y + 0.0006, pbody_top_y - 0.0006],
                color=org["pill_edge"], linewidth=0.55, alpha=0.45
            )
            for r_div in (1, 2):
                y_div = pbody_top_y - r_div * t2_row_h
                ax.plot(
                    [x_left + 0.0010, x_left + inner_w - 0.0010],
                    [y_div, y_div],
                    color=org["pill_edge"], linewidth=0.45, alpha=0.40
                )

            for idx_2, kw in enumerate(prod_list[:6]):
                mr = idx_2 // 2
                mc = idx_2 % 2
                tx = x_left + mc * t2_col_w + 0.0008
                ty = pbody_top_y - (mr + 0.5) * t2_row_h
                if " | " in kw:
                    sub_cat, prod_names = kw.split(" | ", 1)
                    ax.text(
                        tx, ty + t2_row_h * 0.22,
                        sub_cat,
                        fontsize=H4,
                        fontweight="bold",
                        color="#64748B",
                        va="center", ha="left"
                    )
                    ax.text(
                        tx, ty - t2_row_h * 0.21,
                        prod_names,
                        fontsize=H4,
                        fontweight="bold",
                        color=org["t2_txt"],
                        va="center", ha="left"
                    )
                else:
                    ax.text(
                        tx, ty,
                        textwrap.fill(kw, width=19),
                        fontsize=H4,
                        fontweight="bold",
                        color=org["t2_txt"],
                        va="center", ha="left",
                        linespacing=1.00
                    )

            # -----------------------------------------------------------------
            # Zone 4 (INSIDE): Red Dashed "⚠ ANTI-PATTERNS & TRAPS" Sub-Box (2x2 in H4 = 9.17 pt)
            # -----------------------------------------------------------------
            anti_top_y = z3_bot_y - gap_z
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

            ahdr_h = anti_h * 0.245
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
                    linespacing=1.00
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
        "③ CELL ANATOMY: Brand-Agnostic Category (H2) + Mechanisms (H3) + ⚙ PRODUCTS & OSS Box (H4) + ⚠ ANTI-PATTERNS Box (H4)",
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
        "Category (H2) · Mechs (H3)\n⚙ Products · ⚠ Traps (H4)",
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

        ax.text(
            lx + stage_col_w / 2, b_top_y - banner_h * 0.35,
            STAGE_H1_TITLES[st_num],
            fontsize=M_H1,
            fontweight="bold",
            color="#FFFFFF",
            va="center", ha="center"
        )

        ax.text(
            lx + stage_col_w / 2, b_top_y - banner_h * 0.77,
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
            h2_cat_str = cell_data["h2_pill"]
            h3_mechs = cell_data["h3_pills"]
            prod_list = cell_data["normal"]
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
            pad_top = 0.0020
            pad_bot = 0.0020
            inner_w = cw - 2 * pad_x
            x_left = cx + pad_x

            gap_z = 0.0014
            avail_h = rh - pad_top - pad_bot - 3 * gap_z
            z1_h = avail_h * 0.148
            z2_h = avail_h * 0.197
            z3_h = avail_h * 0.365
            anti_h = avail_h * 0.290

            z1_top_y = ry + rh - pad_top
            z1_bot_y = z1_top_y - z1_h
            p_h2 = FancyBboxPatch(
                (x_left, z1_bot_y), inner_w, z1_h,
                boxstyle="round,pad=0.0,rounding_size=0.0024",
                facecolor=org["h2_bg"],
                edgecolor="#FFFFFF",
                linewidth=0.90
            )
            ax.add_patch(p_h2)
            ax.text(
                x_left + inner_w / 2, z1_bot_y + z1_h / 2,
                h2_cat_str,
                fontsize=M_H2,
                fontweight="bold",
                color=org["h2_txt"],
                va="center", ha="center"
            )

            z2_top_y = z1_bot_y - gap_z
            pill_gap = 0.0012
            ph3 = (z2_h - pill_gap) / 2.0
            for idx_p, kw in enumerate(h3_mechs[:2]):
                py = z2_top_y - (idx_p + 1) * ph3 - idx_p * pill_gap
                pill = FancyBboxPatch(
                    (x_left, py), inner_w, ph3,
                    boxstyle="round,pad=0.0,rounding_size=0.0020",
                    facecolor=org["h3_bg"],
                    edgecolor=org["pill_edge"],
                    linewidth=0.75
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
            z3_bot_y = z3_top_y - z3_h
            prod_box = FancyBboxPatch(
                (x_left, z3_bot_y), inner_w, z3_h,
                boxstyle="round,pad=0.0,rounding_size=0.0022",
                facecolor="#FFFFFF",
                edgecolor=org["cell_edge"],
                linewidth=0.95
            )
            ax.add_patch(prod_box)

            phdr_h = z3_h * 0.205
            phdr_box = FancyBboxPatch(
                (x_left + 0.0004, z3_top_y - phdr_h), inner_w - 0.0008, phdr_h,
                boxstyle="round,pad=0.0,rounding_size=0.0016",
                facecolor=org["hdr_bg"],
                edgecolor=org["pill_edge"],
                linewidth=0.45
            )
            ax.add_patch(phdr_box)
            ax.text(
                x_left + inner_w / 2, z3_top_y - phdr_h * 0.52,
                "⚙ SUB-CATEGORY ▸ PRODUCTS & OSS",
                fontsize=M_H4,
                fontweight="bold",
                color="#FEF08A",
                va="center", ha="center"
            )

            pbody_top_y = z3_top_y - phdr_h
            pbody_h = z3_h - phdr_h
            t2_row_h = pbody_h / 3.0
            t2_col_w = inner_w / 2.0

            ax.plot(
                [x_left + t2_col_w, x_left + t2_col_w],
                [z3_bot_y + 0.0006, pbody_top_y - 0.0006],
                color=org["pill_edge"], linewidth=0.45, alpha=0.45
            )
            for r_div in (1, 2):
                y_div = pbody_top_y - r_div * t2_row_h
                ax.plot(
                    [x_left + 0.0010, x_left + inner_w - 0.0010],
                    [y_div, y_div],
                    color=org["pill_edge"], linewidth=0.38, alpha=0.40
                )

            for idx_2, kw in enumerate(prod_list[:6]):
                mr = idx_2 // 2
                mc = idx_2 % 2
                tx = x_left + mc * t2_col_w + 0.0008
                ty = pbody_top_y - (mr + 0.5) * t2_row_h
                if " | " in kw:
                    sub_cat, prod_names = kw.split(" | ", 1)
                    ax.text(
                        tx, ty + t2_row_h * 0.22,
                        sub_cat,
                        fontsize=M_H4,
                        fontweight="bold",
                        color="#64748B",
                        va="center", ha="left"
                    )
                    ax.text(
                        tx, ty - t2_row_h * 0.21,
                        prod_names,
                        fontsize=M_H4,
                        fontweight="bold",
                        color=org["t2_txt"],
                        va="center", ha="left"
                    )
                else:
                    ax.text(
                        tx, ty,
                        textwrap.fill(kw, width=19),
                        fontsize=M_H4,
                        fontweight="bold",
                        color=org["t2_txt"],
                        va="center", ha="left",
                        linespacing=1.00
                    )

            anti_top_y = z3_bot_y - gap_z
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

            ahdr_h = anti_h * 0.245
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
                    linespacing=1.00
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
        "> **What actually runs under the hood of an autonomous AI agent in 2026? Trace left to right across the 10 stages (`1. Silicon`, `2. Python`, `3. Data`, `4. Pre-Train`, `5. SFT`, `6. Post-Train`, `7. Test-Time`, `8. Context`, `9. Harness`, `10. Swarms`) and top to bottom across the 4 distinct organisms (`LLM`, `RAG`, `Multimodal`, `Embodied`), where every cell cleanly separates its Brand-Agnostic Category (`H2`) and Core Mechanisms (`H3`) from its Concrete `⚙ PRODUCTS, MODELS & OSS` (`H4`) and `⚠ ANTI-PATTERNS & TRAPS` (`H4`).**  ",
        f"> **How to Read ([www.arianprabowo.com](https://www.arianprabowo.com) · Based on Haggai Roitman's *The Hitchhiker's Guide to Agentic AI*, `arXiv:2606.24937` · <sub>`{LAST_UPDATED_STR}`</sub>):** **`① COLUMNS (1 → 10):`** Follow `1. Silicon → 10. Swarms` · **`② ROWS (4 ORGANISMS):`** Compare the `LLM` Core Spine against `RAG`, `Multimodal`, and `Embodied` · **`③ CELL ANATOMY:`** Audit the Brand-Agnostic Category (`H2 = 24 pt`), Brand-Agnostic Mechanisms (`H3 = 14.83 pt`), Framed **`⚙ PRODUCTS, MODELS & OSS`** box (`H4 = 9.17 pt`), and Framed **`⚠ ANTI-PATTERNS & TRAPS`** box (`H4 = 9.17 pt`).",
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
            h2_str = f"**`[{d['h2_pill']}]`** *(Brand-Agnostic Category)*"
            h3_str = "**Core Mechanisms:** " + " · ".join(f"**{k}**" for k in d["h3_pills"])
            norm_items = [
                f"**{k.split(' | ', 1)[0]}** `{k.split(' | ', 1)[1]}`" if " | " in k else f"`{k}`"
                for k in d["normal"]
            ]
            norm_str = "**`⚙ Sub-Category ▸ Products:`** " + " · ".join(norm_items)
            anti_str = "**`⚠ Traps:`** " + " · ".join(f"**`✕ {k}`**" for k in d["anti"])
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
            "| Organism (`Short` — *Full Name*) | Brand-Agnostic Category (`H2 = 24pt`) | Brand-Agnostic Mechanisms (`H3 = 14.83pt`) | `⚙ Sub-Category ▸ Products & OSS` (`H4 = 9.17pt`) | `⚠ Anti-Patterns & Traps` (`H4 = 9.17pt`) |",
            "| :--- | :--- | :--- | :--- | :--- |",
        ])
        for org in ORGANISMS:
            d = st["cells"][org["key"]]
            h2_s = f"**`{d['h2_pill']}`**"
            h3_s = ", ".join(f"**`{k}`**" for k in d["h3_pills"])
            nm_s = ", ".join(
                f"**{k.split(' | ', 1)[0]}** `{k.split(' | ', 1)[1]}`" if " | " in k else f"`{k}`"
                for k in d["normal"]
            )
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
