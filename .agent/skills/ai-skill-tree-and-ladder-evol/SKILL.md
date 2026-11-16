---
name: ai-skill-tree-and-ladder-evol
description: >-
  Complete specification, taxonomic rules, L1-L6 user-sophistication axis, Gen 0-5 evolution grid,
  trapezoid timeline bridge, marginal histogram rules, and build pipeline for "AI SKILL TREE 2026"
  and "AI LADDER EVOLUTION (v1-v5)". Activate when editing or regenerating AI_skill_tree_2026.png/.pdf,
  dev/v5_data_and_gates.py, dev/v5_render_plots.py, or dev/2026 10 17 AI_ladder_evol report v5.md.
---

# AI Skill Tree 2026 & AI Ladder Evolution (`v1 -> v5`): Specification & Runbook

## 1. Core Taxonomic Principles

### A. Definition of the Vertical Axis ("Up" the Ladder = User Sophistication)
* **"Up" (`Level 1` -> `Level 6`) measures the sophistication, skill investment, and operational surface of the human user**, NOT the internal parameter count of the model or abstract task complexity:
  * **Level 1 (`Everyday Consumer`)**: `0 hours` training; casual web/mobile chat UI, zero-shot prompting, voice/camera consumer mode, and browser vibe-coding (`Claude Artifacts`, `ChatGPT Canvas`).
  * **Level 2 (`Power Prompt & Workspace User`)**: `Weekend / ~10h` investment; system instructions, Projects/Gems, NotebookLM document grounding, deep research, and no-code automation (`Zapier`).
  * **Level 3 (`AI-Assisted Creator & Vibe Coder`)**: `Short course / ~40h` investment; AI IDE (`Cursor`, `Windsurf`), CLI coding harnesses (`Claude Code`), local models (`Ollama`), and ComfyUI node graphs.
  * **Level 4 (`AI Application & Workflow Engineer`)**: `Bootcamp / SE degree` investment; structured outputs, hybrid RAG (`Qdrant`, `Docling`), `MCP` servers, `SKILL.md` / `AGENTS.md`, `LangGraph` stateful harnesses, and CI/CD evals.
  * **Level 5 (`Model Customization & Post-Training Engineer`)**: `ML Engineering / MSc` investment; dataset curation, `LoRA`/`QLoRA` SFT (`TRL`, `Unsloth`), `DPO` preference tuning, `RLVR`/`GRPO` (`veRL`), and `vLLM`/`SGLang` cluster serving.
  * **Level 6 (`Frontier AI Researcher & Systems Architect`)**: `PhD / Frontier Lab` investment; CUDA/Triton kernels, `3D/4D` parallelism (`Megatron-LM`, `TorchTitan`), sparse `MoE` pre-training, `System-2` tree search, and cryptographic `A2A` swarm infrastructure.
* **Key Insight on Building AI for Others**: A user who builds an internal company chatbot connected via RAG, tool calling, and policy guardrails for *other people* to use is operating at **Level 4 (`AI Application & Workflow Engineer`)**, whereas the employee asking that chatbot questions is at **Level 1**.

### B. Orientation & Visual Structure of `AI Ladder Evolution`
1. **Top-to-Bottom Level Ordering (`Level 1` at Top -> `Level 6` at Bottom)**:
   * `Level 1` sits at the top row (broadest user funnel) and `Level 6` sits at the bottom row (deepest technical foundation).
2. **Equal-Width Generation Columns (`Gen 0` -> `Gen 5`) + Trapezoid Timeline Bridge**:
   * Keep the Generation columns equal-width in the main matrix so every cell has uniform text capacity.
   * Connect the equal-width matrix columns to the true chronological X-axis of the bottom timeseries plot via a **row of trapezoids**, where each trapezoid displays `3 rows` of text: `Gen X`, `Start YYYY-MM to End YYYY-MM`, and `Duration in years` (write `"years"`, not `"yr"`, without brackets).
3. **Right-Hand Marginal Histogram (`Users` vs. `Tokens`)**:
   * Render as a horizontal bar/step chart where each flat bar aligns with the full height of its corresponding `Level` row.
   * Legend at the top: **Left column = `Users`**, **Right column = `Tokens`**, with each row corresponding to a Generation.
   * Include an analytical annotation box at the bottom explaining: (a) power-law decay of user headcount as level increases, (b) invariance of this funnel shape across generations, and (c) concentration of total token consumption in the middle/upper-middle agentic levels (`L3-L5`) where automated loops run 24/7.
4. **Bottom Timeseries & TRL Continuity**:
   * Connect foundational papers (`Chain-of-Thought`, `LoRA`, `RAG`, `ReAct`, `DPO`, `RLVR`) to production frameworks and consumer tools via directed **Technology Readiness Level (TRL)** lines.
   * Projected future segments (`Gen 5` up to `2028`) use the same color as historical series with a dashed linestyle.
5. **Non-Repetition Across Levels (Top-to-Bottom Reading Rule)**:
   * Expect the reader to scan from `Level 1` (top) down to `Level 6` (bottom); do not repeat model or product names in lower rows if they already appeared in a higher row of the same generation.

## 2. `AI SKILL TREE 2026` (`AI_skill_tree_2026.png` / `.pdf`) Rules
1. **4 Capability Pillars + 1 Obsolete Column (`Left -> Right`)**:
   * Column 1: `Chat, Search, RAG & Reasoning`
   * Column 2: `Multimodal (Vision, Audio, Video)`
   * Column 3: `Coding, Harnesses, Data & Infra`
   * Column 4: `Safety, Evals, Governance & Ops`
   * Column 5 (Red Dashed): `Obsolete / Automated-Away Trap` (also structured with `Top 3` pills + `5x2` grid, with NO cross bullet icons).
2. **Masthead Layout**:
   * **Top-Left**: Single-line title `AI SKILL TREE 2026` + `www.arianprabowo.com` directly below it.
   * **Top-Right**: 4-part numbered reading guide (`①②` in yellow `#FEF08A` for motivation & self-diagnosis rule; `③④` in blue `#38BDF8` for cell hierarchy & obsolete column).
   * **Bottom Footnote Strip inside Masthead (`grey #94A3B8`)**: Defines scope (LLM, multimodal, and agentic AI usage/engineering, excluding classical GOFAI/tabular ML), notes fast-moving validity and cross-references `AI Ladder Evolution` by Arian Prabowo, cites `arXiv:2606.24937`, and prints the exact local timestamp (`Updated: YYYY-MM-DD HH:MM:SS TZ`).

## 3. Execution Pipeline
* Run `dev/v5_ladder_pipeline.py` using `.venv/bin/python`:
  ```bash
  .venv/bin/python dev/v5_ladder_pipeline.py
  ```
  This executes `dev/v5_data_and_gates.py`, `dev/v5_render_plots.py` (which updates both `dev/figures_v5/*` and root `AI_skill_tree_2026.png` / `.pdf`), and rebuilds `dev/2026 10 17 AI_ladder_evol report v5.md`.
