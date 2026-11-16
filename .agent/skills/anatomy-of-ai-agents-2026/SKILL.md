---
name: anatomy-of-ai-agents-2026
description: >-
  Complete specification, architectural rules, 10x4 matrix taxonomy, 4-zone cell anatomy,
  Golden Ratio typography (H2=24pt), and verification workflow for the "ANATOMY OF AI AGENTS 2026"
  megachart in dev/anatomy_of_AI_agents_2026/. Activate whenever editing, auditing, or regenerating
  the Anatomy of AI Agents 2026 chart, PDF, mobile chart, or companion markdown.
---

# Anatomy of AI Agents 2026: Complete Specification & Runbook

## 1. File Locations (Strictly Consolidated in `dev/anatomy_of_AI_agents_2026/`)
All files belonging to `Anatomy of AI Agents 2026` MUST remain inside `dev/anatomy_of_AI_agents_2026/`:
* **Generator Script**: `dev/anatomy_of_AI_agents_2026/plot_agent_anatomy_2026.py`
* **Desktop A0 Megachart (`46.8 x 21.6 in`, `19.5:9`, 300 DPI)**: `dev/anatomy_of_AI_agents_2026/anatomy_of_AI_agents_2026.png`
* **Vector PDF**: `dev/anatomy_of_AI_agents_2026/anatomy_of_AI_agents_2026.pdf`
* **Mobile Landscape Chart (`26.0 x 12.0 in`, `19.5:9`, 300 DPI)**: `dev/anatomy_of_AI_agents_2026/anatomy_of_AI_agents_2026_mobile.png`
* **Companion Markdown Reference**: `dev/anatomy_of_AI_agents_2026/2026 11 07 anatomy_of_AI_agents_2026.md`

## 2. Non-Negotiable Architectural & Naming Rules
1. **No `OSI` or `PDU` References**: Never mention `OSI`, `PDU`, or `"Layer X"` anywhere in the chart, code, or markdown.
2. **Left-to-Right 10-Stage Pipeline (`Columns 1 -> 10`)**:
   * Pre-training, SFT, Post-training, and Test-time compute are strictly separated into distinct columns.
   * Each stage has a **Short Name (`<= 2 words`, rendered at `H1 = 38.83 pt`)** formatted as `1. Silicon`, `2. Python`, etc., and a **Full Name (`<= 10 words`, rendered at `H4 = 9.17 pt`)** right below it inside the column header banner (with NO progress bar at the top of the column):
     1. `1. Silicon`: *Physical Compute Silicon, GPU Clusters, HBM3e Memory & Interconnect Fabrics*
     2. `2. Python`: *Python Runtimes, Package Managers, Virtual Environments & Tensor Compilers*
     3. `3. Data`: *Web & Code Corpora, Subword Tokenization & Curation Pipelines*
     4. `4. Pre-Train`: *Foundation Model Architectures, Sparse MoE Routing & Self-Supervised Pre-Training*
     5. `5. SFT`: *Supervised Fine-Tuning, Instruction Templates, Sequence Packing & LoRA Adapters*
     6. `6. Post-Train`: *Preference Alignment (RLHF/DPO) & Verifiable-Reward Reinforcement Learning (RLVR/GRPO)*
     7. `7. Test-Time`: *Test-Time Compute Scaling, System-2 Chain-of-Thought Reasoning & Tree Search*
     8. `8. Context`: *Context Engineering, Four-Tier Memory, Tool Calling, MCP & Skills*
     9. `9. Harness`: *Single-Agent Harness Engineering, Observe-Decide-Act Loops & Stateful Graph Workflows*
     10. `10. Swarms`: *Multi-Agent Orchestration, Hierarchical Swarms, A2A Protocols & Shared State*
3. **Top-to-Bottom 4-Organism Rows (`Rows 1 -> 4`)**:
   * Do not use generic "Pillar 1 / Pillar 2 / Anti-Patterns" rows.
   * `RAG`, `Multimodal`, and `Embodied` are separated out from the core `LLM` spine as distinct organisms (visually separated below the `LLM` spine by a teal dashed horizontal line):
     1. `LLM` (*Autoregressive Text, Code & Reasoning Language Models*): Core Spine (Emerald `#047857`)
     2. `RAG` (*Hybrid Vector, Lexical & Graph Retrieval-Augmented Generation*): Knowledge Organism (Teal `#0F766E`)
     3. `Multimodal` (*Vision, Audio, Speech, Video & Native Omni-Modal Models*): Sensory Organism (Violet `#6D28D9`)
     4. `Embodied` (*GUI Computer Use, Physics World Models & VLA Robotics*): Action Organism (Blue `#1D4ED8`)

## 3. 4-Zone Anatomical Cell Design (Brand-Agnostic vs. Concrete Products)
Every single one of the `40` `(Organism, Stage)` cells is divided vertically into 4 explicit zones so that **brand-agnostic categories/mechanisms** and **concrete product names** are never conflated:
1. **Zone 1 (`H2 = 24.00 pt`, Top Solid Banner): Overarching Brand-Agnostic Category**:
   * Strictly `<= 18 chars` and **100% vendor-neutral** (zero brand/product names, e.g., `Tensor Compute`, `Serving Runtime`, `Text & BPE Corpus`, `Sparse MoE & Attn`, `Instruction Tuning`, `Alignment & RLVR`, `System-2 Search`, `Memory & Tool Bus`, `Observe-Act Loop`, `Multi-Agent Graph`).
2. **Zone 2 (`H3 = 14.83 pt`, 2 Concept Bars): Brand-Agnostic Core Mechanisms**:
   * Two stacked mechanism bars (`h3_pills`) containing **100% vendor-neutral architectural primitives/algorithms** (zero brand names, e.g., `Deterministic Lockfiles` and `Paged KV & Graph Capture`).
3. **Zone 3 (`H4 = 9.17 pt`, Framed `⚙ SUB-CATEGORY ▸ PRODUCTS & OSS` Sub-Box)**:
   * Solid-bordered white sub-box with an organism-colored header bar labeled **`⚙ SUB-CATEGORY ▸ PRODUCTS & OSS`**.
   * Contains a `3x2 = 6` grid with vertical and horizontal dividers. Each item in `normal` is formatted as `"SUB-CATEGORY: | Product Names"` and rendered on 2 crisp single lines:
     * **Line 1 (`sub_cat`, bold muted slate `#64748B`)**: The brand-agnostic sub-category (e.g., `ENV & PKG MGR:`, `TENSOR FRAMEWORK:`, `SERVING ENGINE:`).
     * **Line 2 (`prod_names`, bold organism dark)**: Concrete product, model, chip, or library names (e.g., `uv · Pixi · Conda · pip`, `PyTorch 2.x · JAX`, `vLLM · SGLang`).
4. **Zone 4 (`H4 = 9.17 pt`, Framed `⚠ ANTI-PATTERNS & TRAPS` Sub-Box)**:
   * Dashed red sub-box (`#FFF1F2` fill, `#E11D48` dashed border) at the bottom of the cell with header bar **`⚠ ANTI-PATTERNS & TRAPS`** and a `2x2 = 4` grid of concrete `✕` failure modes.

## 4. Golden Ratio Typography Scale (Anchored at `H2 = 24.00 pt`)
* `T = H0 = 24.0 * φ² ≈ 62.83 pt`
* `H1 = 24.0 * φ ≈ 38.83 pt`
* `H2 = 24.00 pt`
* `H3 = 24.0 / φ ≈ 14.83 pt`
* `H4 = 24.0 / φ² ≈ 9.17 pt`
* Mobile chart (`26.0 x 12.0 in`) scales all 5 tiers proportionally by `SCALE = 26.0 / 46.8`.

## 5. Verification & Execution Commands
1. Run the generator script:
   ```bash
   .venv/bin/python dev/anatomy_of_AI_agents_2026/plot_agent_anatomy_2026.py
   ```
2. Run the Matplotlib renderer bounding-box audit (`get_window_extent`) to verify `0` overflows across all `40` `H2` banners, `80` `H3` mechanisms, `480` `H4` sub-category/product lines, and `160` `H4` anti-patterns.
3. Visually inspect `dev/anatomy_of_AI_agents_2026/anatomy_of_AI_agents_2026.png` via `read_file`.
