#!/usr/bin/env python3
"""
Deterministic Builder & Verifier for:
- stages_v4/part1.md .. stages_v4/part5.md
- 2026 10 17 AI_ladder_evol report v4.md
"""
import os
import re
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(BASE_DIR, "cache_v4")
STAGES_DIR = os.path.join(BASE_DIR, "stages_v4")
os.makedirs(STAGES_DIR, exist_ok=True)

df_cells_hist = pd.read_csv(os.path.join(CACHE_DIR, "v4_ladder_cells.csv"))
df_cells_g5 = pd.read_csv(os.path.join(CACHE_DIR, "v4_gen5_speculative.csv"))
df_cells = pd.concat([df_cells_hist, df_cells_g5], ignore_index=True)
df_cells["gen_idx"] = df_cells["gen_id"].str.replace("G", "").astype(int)
df_cells["level"] = df_cells["level_id"].astype(int)
df_cells["cell_id"] = df_cells["gen_id"] + "-L" + df_cells["level_id"].astype(str)
df_cells["canonical_name"] = df_cells["user_first_title"]
df_cells["tool_surface"] = df_cells["surface_and_setup"]
df_cells["hardware_setup"] = df_cells["level_bracket_str"]
df_cells["tutorials_str"] = df_cells["keywords_and_tutorials"]
df_cells["keywords_to_learn"] = df_cells["keywords_and_tutorials"]
df_cells["tech_enablers"] = df_cells["surface_and_setup"]
df_cells["tokens_task"] = df_cells["single_task_tokens"]
df_cells["flops_task"] = df_cells["single_task_flops"]
df_cells["usd_task"] = df_cells["single_task_usd"]
df_cells["wh_task"] = df_cells["single_task_wh"]

df_tut = pd.read_csv(os.path.join(CACHE_DIR, "v4_tutorials.csv"))
df_uc = pd.read_csv(os.path.join(CACHE_DIR, "v4_use_cases.csv"))
df_gloss = pd.read_csv(os.path.join(CACHE_DIR, "v4_glossary_lit_review.csv"))
df_lit = pd.read_csv(os.path.join(CACHE_DIR, "v4_existing_ladders.csv"))
df_trl = pd.read_csv(os.path.join(CACHE_DIR, "v4_trl_trajectories.csv"))
df_bench = pd.read_csv(os.path.join(CACHE_DIR, "v4_skill_deflation_benchmarks.csv"))

with open(os.path.join(BASE_DIR, "2026 10 17 AI_ladder_evol report v3.md"), "r", encoding="utf-8") as f:
    v3_lines = f.read().splitlines()

# Helper to build markdown tables from cache_v4 CSVs
def build_table_1_2():
    return """##### Table 1.2: Standardized 6-Level User Skill-Tree Brackets (Level 1 to Level 6), Use-vs-Make Continuum & Down-Ladder Deflation Summary
* **Table 1.2 Standalone Caption (`/caption`):** **Standardized six-level vertical user-learning brackets (`Level 1` at `0h (0d) | $0` to `Level 6` at `~10,000h (~5 Yrs / Focused PhD) | ~$100M+`) invariant across `2017–2028`, calibrated by Cumulative "Beeline" Hours from a High School Baseline (`0h`) and mapped across the `Use vs. Make` continuum, `SWE / MLE / Scientist` roles, cross-generation single-task resource spans, and benchmark workflow deflation trajectories.**

| Level ID & Standardized Folksonomy Name | Single-Number Beeline Bracket (`Hours / Time | Cap`) | `Use vs. Make` Continuum & Profession Mapping (`SWE / MLE / Scientist`) | Primary Tool Surface & Hardware Setup (`Setup_cap`) | Track A: Direct User / Pioneer Persona | Track B: Product, Enterprise-Bot & Foundation Builder Persona | Cross-Gen Mean Single-Task Tokens (`G0`–`G4`) | Cross-Gen Mean Single-Task USD (`G0`–`G4`) | Benchmark Workflows Sinking Into / Passing Through Rung (`G0` $\\to$ `G4`) |
| :--- | :---: | :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **`Level 1` — Casual User & Zero-Setup Default Consumer Tier** | `0h (0d) \\| $0` *(Fixed Anchor)* | **`100% Using`** (Zero technical configuration; Everyday Consumer / Employee) | Passive Widget (`G0`), IDE `Tab` (`G1`), Default Chat (`G2`), Omni + `Artifacts` (`G3`), Auto-Router + `MCP Apps` (`G4`), Ambient OS Bar (`G5`) | High schooler, consumer, or employee typing natural requests at `0h` | Downstream beneficiary of Track B `L3–L6` SaaS & internal company chatbots (`0h` study) | `1,917` *(`25` to `6,500`)* | `\\$0.0029` *(`\\$0.00001` to `\\$0.008`)* | **Sunk to `L1`:** `text_classification` (`G2`), `multimodal_creation` (`G3`), `math_reasoning` (`G4`), `doc_qa_50pdf` (`G4`) |
| **`Level 2` — Domain Power-User & Workspace Crafter Tier** | `<50h (~1 Wk / Short Course) \\| <$30` *(Fixed Anchor)* | **`~90% Using / ~10% Making`** (Domain Power-User, Analyst, Non-Coding Prompt/Workspace Crafter) | `Cloud AutoML` (`G0`), `Playground` (`G1`), `Custom GPTs`/`Midjourney` (`G2`), `Projects`/`NotebookLM` (`G3`), `Deep Research` (`G4`), No-CLI Spec Studio (`G5`) | Analyst, lawyer, writer, or PM curating 50 PDFs or scoping `Deep Research` briefs | Departmental champion sharing `Custom GPTs` or `Claude Project` binders with team | `31,660` *(`150` to `120,000`)* | `\\$0.0599` *(`\\$0.0005` to `\\$0.180`)* | **Passed through `L2`:** `text_classification` (`G1`), `math_reasoning` (`G2–G3`), `doc_qa_50pdf` (`G3`); **Active in `G4-L2`:** `web_research_synthesis` (`12h`) |
| **`Level 3` — Applied SWE, AI-IDE & Enterprise Bot Integrator Tier** | `<200h (~1 Mo / 1 Uni Subject) \\| <$100` *(Inductive)* | **`~65% Using / ~35% Making`** (Applied Software Engineer [`SWE`] & Enterprise Bot Integrator) | `Jupyter`/`sklearn` (`G0`), REST SDK (`G1`), `LangChain`/`Pinecone` (`G2`), `Cursor Composer`/`NeMo` (`G3`), `.mcp.json` (`G4`), `A2A`/`Cedar` Policy (`G5`) | Software developer using `Cursor Composer` (`.cursorrules`) or wiring `.mcp.json` servers | **Internal Company Chatbot Builder** wiring `SharePoint RBAC RAG` + `MCP` + `NeMo`/`Llama Guard` rails for `L1` staff | `47,180` *(`600` to `160,000`)* | `\\$0.1342` *(`\\$0.003` to `\\$0.250`)* | **Origin at `L3`:** `text_classification` (`G0`, `120h`); **Passed through `L3`:** `math_reasoning` (`G1`), `doc_qa_50pdf` (`G1–G2`), `web_research_synthesis` (`G3`) |
| **`Level 4` — Senior Harness SWE & Single-GPU Adaptation MLE Tier** | `~600h (~1 Qtr / 1 Uni Semester) \\| ~$1.5k` *(Inductive)* | **`~35% Using / ~65% Making`** (Track A: Senior Harness `SWE` \\| Track B: Applied Single-GPU `MLE`) | `PyTorch BERT` (`G0`), Cloud Fine-Tune CLI (`G1`), Single-GPU `QLoRA` (`G2`), `LangGraph` (`G3`), `Claude Code` CLI (`G4`), Formal Verifiers (`G5`) | Senior `SWE` orchestrating `Claude Code` CLI + `CLAUDE.md` + local `Docker` TDD loops | Applied `MLE` training `GECToR` (`G0`), `4-bit QLoRA` (`CoEdIT` `G2`), or `LangGraph` state machines (`G3`) | `138,300` *(`2,000` to `480,000`)* | `\\$0.4750` *(`\\$0.025` to `\\$1.150`)* | **Origin at `L4`:** `multimodal_creation` (`G0`, `400h`), `doc_qa_50pdf` (`G0`, `350h`); **Passed through `L4`:** `web_research_synthesis` (`G1–G2`) |
| **`Level 5` — Staff Sandbox/Infra SWE & Distributed Post-Training MLE Tier** | `~2,000h (~1 Yr / Core Postgrad) \\| ~$500k` *(Inductive)* | **`~15% Using / ~85% Making`** (Track A: Staff Sandbox/Infra `SWE` \\| Track B: Distributed Systems/Post-Training `MLE`) | `Fairseq`/`ONNX` (`G0`), `DeepSpeed ZeRO` (`G1`), `vLLM` Cluster (`G2`), `SWE-bench` Farm (`G3`), `M4 Mac Mini OpenClaw` & `GRPO` (`G4`), Sovereign Flywheel (`G5`) | Staff Sandbox `SWE` running 24/7 air-gapped `M4 Mac Mini OpenClaw` + parallel `git worktree` swarms | Distributed `MLE` running `ZeRO-3` (`G1`), `vLLM PagedAttention` (`G2`), `DPO` (`G3`), or custom `GRPO RLVR` (`G4`) | `610,600` *(`8,000` to `2,400,000`)* | `\\$2.2060` *(`\\$0.180` to `\\$6.500`)* | **Origin at `L5`:** `math_reasoning` (`G0`, `1,000h` $\\to$ `G4-L1` `0h`), `web_research_synthesis` (`G0`, `800h` $\\to$ `G4-L2` `12h`) |
| **`Level 6` — AI Research Scientist, Data/Benchmark Architect & Next-Gen Pioneer** | `~10,000h (~5 Yrs / Focused PhD) \\| ~$100M+` *(Genesis Apex)* | **`100% Foundation/Genesis Making`** (AI Research Scientist, Pretraining Data & Benchmark Architect; recursively uses `L1–L5` tools) | `1k–25k+` TPU/GPU Supercomputer + Math Theory + Trillion-Token Data Engines + Benchmark Suites (`GLUE`, `MMLU`, `SWE-bench`) | Frontier Research Scientist formulating `Transformer`/`RLHF`/`Chinchilla`/`RLVR` math (`TRL 1–3` on-ladder) | **Next-Gen `G+1` Creator:** Curates pretraining corpora, builds eval benchmarks, and pretrains base models (`GPT-3/4/5`, `Claude`, `DeepSeek-R1`) that sink tasks to `L1` | `6,596,000` *(`80,000` to `25,000,000`)* | `\\$22.8400` *(`\\$4.200` to `\\$65.000`)* | **Genesis Source (`TRL 1–3`):** Creates the `G+1` foundation models and benchmarks that drive all down-ladder deflation |"""

def build_table_2_2():
    rows = []
    for _, r in df_uc.iterrows():
        mapped_note = str(r['mapped_cell_and_note']).replace("|", "\\|")
        rows.append(
            f"| **`{r['use_case_id']}` — {r['use_case_name']}** | **{r['track']}** | `{r['first_appearance']}` | `{r['mainstream_crossover']}` | `{r['target_surface']}` | **{mapped_note}** |"
        )
    header = """##### Table 2.2: Raw Adopted Use-Case Inventory (30 Canonical Workflows Across Track A, Track B & Track C Genesis)
* **Table 2.2 Standalone Caption (`/caption`):** **Complete empirical inventory of 30 real-world AI workflows (`UC_01` to `UC_30`) across `2017–2026`, spanning Track A (Direct End-Users), Track B (Commercial SaaS Product Embedders & Internal Company Chatbot Builders serving `Level 1` users), and Track C (`Level 6` AI Research Scientists, Pretraining Data Architects, and Benchmark Creators who birth Generation `G+1`), with first-appearance dates, mainstream crossover dates, surfaces, and mapped `(Gen G, Level L)` coordinates (`cache_v4/v4_use_cases.csv`).**

| Use Case ID & Name | Track (`Direct User` vs. `Product/Bot Builder` vs. `L6 Genesis`) | First Appearance (`YYYY-MM`) | Mainstream Crossover (`YYYY-MM`) | Target User Surface & Hardware Setup | Mapped `(Gen G, Level L)` Cell & Single-Number Bracket |
| :--- | :--- | :---: | :---: | :--- | :--- |"""
    return header + "\n" + "\n".join(rows)

def build_table_2_3():
    rows = []
    for _, r in df_tut.iterrows():
        mapped_lvl = str(r['mapped_level']).replace("|", "\\|")
        rows.append(
            f"| **`{r['tutorial_id']}`** | **{r['resource_name']}** | `{r['release_date']}` | `{r['keywords_taught']}` | `{r['beeline_hours']}h` | `{r['target_surface']}` | **`{mapped_lvl}`** |"
        )
    header = """##### Table 2.3: Timestamped Tutorial, University Syllabus & Foundational Paper Inventory with Cumulative "Beeline" Hours
* **Table 2.3 Standalone Caption (`/caption`):** **Empirical syllabus, developer cookbook, and foundational research monograph inventory (`TUT_01` to `TUT_25`, `cache_v4/v4_tutorials.csv`) across `2017–2026`, recording exact release dates, technical keywords and mental models taught, cumulative zero-filler "Beeline" hours from a High School baseline (`0h`), single-number `<` to `~` bracket strings, target execution surfaces, and inductive 6-level assignments (`L2` through `L6`).**

| Tutorial ID | Educational Resource, Course Syllabus or Foundational Research Monograph | Release Date (`YYYY-MM`) | Exact Technical Keywords & Mental Models Taught | Cumulative Beeline Hours | Target Tool Surface & Setup | Mapped Inductive Level & Bracket |
| :--- | :--- | :---: | :--- | :---: | :--- | :---: |"""
    return header + "\n" + "\n".join(rows)

def build_section_2_2_2b():
    rows = []
    for _, r in df_gloss.iterrows():
        rows.append(
            f"| **`{r['keyword_id']}`: `{r['keyword_term']}`** | `{r['cognitive_tier']}` | *{r['seminal_citations']}* (`{r['anchor_date']}`) | {r['plain_english_definition']} | **`{r['grid_cell_id']}`** | {r['evolutionary_trajectory']} |"
        )
    header = """#### 2.2.2b Canonical Glossary Literature Review & Keyword-to-Cell Provenance Mapping (`Table 2.3b`)

* **Why Every Cell Keyword Requires Literature Provenance:** In a rigorous user-skill taxonomy, technical buzzwords (`prompt engineering`, `vibe coding`, `RAG`, `vLLM`, `LoRA/QLoRA`, `agentic`, `swarm`, `orchestration`, `MCP`, `A2A`, `RLHF`, `DPO`, `RLVR`, `GRPO`, `PagedAttention`, `KV-cache`, `FlashAttention`, `DeepSpeed ZeRO`, `Chinchilla scaling`, `RoPE`, `LangGraph`, `OpenClaw`, `formal proof oracles`, `world models`) cannot float as undefined jargon. Every keyword that appears in the bottom keyword line of our 36 Megachart cards (`Plot 0` and `Plot 0-Mini`) represents a concrete human mental model or systems abstraction that originated in a specific foundational paper or engineering release (`Grid Cell ID`) and, in many cases, subsequently sank down the ladder (`Evolutionary Trajectory`).
* **36-Term Canonical Glossary Audit (`cache_v4/v4_glossary_lit_review.csv`):** `Table 2.3b` provides a complete literature review and plain-English definition for all 36 canonical keywords across `Gen 0` to `Gen 5` and `Level 1` to `Level 6`, explicitly linking each term's seminal citations to its exact `(Gen, Level)` coordinate and evolutionary trajectory.

##### Table 2.3b: Canonical Glossary Literature Review — 36 Core AI Keywords, Seminal Citations, Plain-English Definitions & 6×6 Grid Provenance
* **Table 2.3b Standalone Caption (`/caption`):** **Complete 36-term Glossary Literature Review (`KW_01` to `KW_36`, `cache_v4/v4_glossary_lit_review.csv`), mapping every canonical technical keyword displayed in the 36-cell Megachart (`Plot 0` / `Plot 0-Mini`) to its cognitive tier, seminal academic/engineering citations (`YYYY-MM`), plain-English operational definition, mapped `(Gen, Level)` cell coordinate, and cross-generation evolutionary trajectory.**

| Keyword ID & Canonical Term | Cognitive Tier | Seminal Citations & Anchor Date (`YYYY-MM`) | Plain-English Operational Definition & User Mental Model | Grid Cell ID | Cross-Generation Evolutionary Trajectory |
| :--- | :--- | :--- | :--- | :---: | :--- |"""
    return header + "\n" + "\n".join(rows) + "\n"

def build_table_3_2():
    return """| Neutral Level ID | Single-Number Beeline Bracket (`Hours / Time \\| Cap`) | Compact Plot Tick Label | `Use vs. Make` & Profession Mapping (`SWE / MLE / Scientist`) | Primary Execution Surface & Non-Compute Setup (`Setup_cap`) | Track A: Direct User / Pioneer Role | Track B: Product, Internal-Bot & `G+1` Foundation Builder Role | Monotonic Beeline Separation ($H_{L_k} < H_{L_{k+1}}$) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`L1`** | **`0h (0d) \\| $0`** | `L1 (0h / 0d \\| $0)` | **`100% Using`** — Casual User / High Schooler / Downstream Employee | Default Browser Tab, Mobile App, Email/Doc Widget, 1-Key IDE `Tab`, or Ambient OS Bar (`\\$0` setup) | Consumes passive widgets (`G0`), `Copilot Tab` (`G1`), zero-shot chat (`G2`), omni-chat + `Artifacts` (`G3`), or auto-router thinking (`G4`). | **Downstream Consumer:** `100M–1B+` users and employees consuming SaaS widgets (`Grammarly`) or internal corporate bots built by `L3–L6` teams at `0h`. | $H_{L1} = 0\\text{h} < H_{L2} = 50\\text{h}$ |
| **`L2`** | **`<50h (~1 Wk / Short Course) \\| <$30`** | `L2 (<50h / ~1 Wk \\| <$30)` | **`~90% Using / ~10% Making`** — Domain Power-User, Analyst & Prompt/Workspace Crafter | Web Playground, Cloud AutoML UI, Discord Flags, `Projects`/`NotebookLM`, `Deep Research` UI (`<\\$30/mo` sub) | Crafts regex/AutoML (`G0`), few-shot `stop` prefixes (`G1`), manual `CoT` & `Custom GPTs` (`G2`), 50-PDF `Projects` (`G3`), or `Deep Research` briefs (`G4`). | Prototypes departmental prompt templates, shared `Custom GPTs`, or curated `Claude Project` binders for small teams (`5–20` coworkers). | $H_{L2} = 50\\text{h} < H_{L3} = 200\\text{h}$ |
| **`L3`** | **`<200h (~1 Mo / 1 Uni Subject) \\| <$100`** | `L3 (<200h / ~1 Mo \\| <$100)` | **`~65% Using / ~35% Making`** — Applied Software Engineer (`SWE`) & Enterprise Bot Integrator | Python/JS SDK, Vector DB, AI-Native IDE (`Cursor Composer`), `.mcp.json` (`<\\$100` API/DB setup) | Runs `scikit-learn` scripts (`G0`), `REST` wrappers (`G1`), personal `RAG` (`G2`), multi-file `Cursor Composer` coding (`G3`), or desktop `.mcp.json` tools (`G4`). | **Core Internal-Bot Integrator:** Wires `SharePoint RBAC RAG`, enterprise tools (`Jira`/`ServiceNow`/`Salesforce` via functions/`MCP`), and `NeMo`/`Llama Guard` rails for `L1` staff. | $H_{L3} = 200\\text{h} < H_{L4} = 600\\text{h}$ |
| **`L4`** | **`~600h (~1 Qtr / 1 Uni Semester) \\| ~$1.5k`** | `L4 (~600h / ~1 Sem \\| ~$1.5k)` | **`~35% Using / ~65% Making`** — Senior Harness `SWE` (Track A) & Applied Single-GPU `MLE` (Track B) | Single GPU (`PyTorch`/`PEFT`), `LangGraph` SDK, or Terminal CLI (`Claude Code`) + Local `Docker` (`~\\$1.5k` GPU/compute) | Fine-tunes `BERT` (`G0`), runs `CoT` voting (`G1`), tunes `4-bit QLoRA` (`G2`), orchestrates cyclic `LangGraph` (`G3`), or runs `Claude Code` CLI `TDD` loops (`G4`). | **SaaS ML & Agentic Architect:** Trains production task encoders/adapters (`Grammarly GECToR` at `G0-L4` & `CoEdIT` at `G2-L4`) or stateful support graphs (`G3-L4`) serving `L1` users. | $H_{L4} = 600\\text{h} < H_{L5} = 2,000\\text{h}$ |
| **`L5`** | **`~2,000h (~1 Yr / Core Postgrad) \\| ~$500k`** | `L5 (~2,000h / ~1 Yr \\| ~$500k)` | **`~15% Using / ~85% Making`** — Staff Sandbox/Infra `SWE` (Track A) & Distributed/Post-Training `MLE` (Track B) | Multi-Node GPU Cluster (`DeepSpeed`/`vLLM`/`GRPO`) OR Dedicated Physical `M4 Mac Mini` Sandbox (`~\\$500k` cluster or `\\$599–\\$1.2k` host) | Operates 24/7 personal/team autonomous `OpenClaw` daemons & parallel `git worktree` subagent swarms on dedicated `M4 Mac Mini` hardware (`G4-L5`). | **Frontier Infra & RLVR Team:** Quantizes `ONNX` (`G0-L5`), shards `ZeRO-3` (`G1-L5`), serves `vLLM` (`G2-L5`), runs `SWE-bench` Docker farms (`G3-L5`), or trains `GRPO RLVR` (`G4-L5`). | $H_{L5} = 2,000\\text{h} < H_{L6} = 10,000\\text{h}$ |
| **`L6`** | **`~10,000h (~5 Yrs / Focused PhD) \\| ~$100M+`** | `L6 (~10,000h / ~5 Yrs \\| ~$100M+)` | **`100% Foundation/Genesis Making`** — AI Research Scientist, Data/Benchmark Architect & Next-Gen Pioneer | `1k–25k+` TPU/GPU Supercomputer Pod (`~\\$100M+` cap) + Mathematical Proofs + Petabyte Data Engines + Benchmark Suites | Formulates novel math objectives (`Attention`, `RLHF`, `Chinchilla`, `RLVR` at `TRL 1–3`) while recursively using `L1–L5` tools (`Claude Code`, `vLLM`) to accelerate research. | **Genesis Creator of `G+1`:** Curates pretraining corpora, designs eval benchmarks (`GLUE`, `MMLU`, `SWE-bench`), and pretrains base models (`BERT`, `GPT-3/4/5`, `Claude`, `R1`). | Top Genesis Bracket ($H_{L6} = 10,000\\text{h}$) |

**Table 3.2 — Calibration of the six vertical user-skill brackets (`L1` to `L6`) proves strict monotonic learning-hour progression ($0 < 50 < 200 < 600 < 2,000 < 10,000\\text{ hours}$) using single-number `<` to `~` Beeline brackets from a High School baseline (`0h`).**"""

def build_section_3_fixes():
    return """
#### 3.2.4 Bidirectional Medium-Model Decoupling, Four-Tier Cognitive Input Hierarchy & Failure-Boundary Anchor

To guarantee zero ambiguity when classifying workflows across the `6 × 6` grid, we enforce three structural classification rules on the vertical axis:

* **1. Bidirectional Medium-Model Decoupling (Why Interface Medium $\\neq$ Skill Level):** A common failure in informal AI ladders is equating the *interface medium* (Web Browser vs. Terminal CLI vs. API) with a fixed skill level. In our coordinate system, interface medium and skill level are bidirectionally decoupled:
  * **High-Skill Work Inside a Browser (`L4–L6` in Web UIs):** A researcher running distributed `PyTorch` training inside a browser-hosted `Google Colab Pro` / `JupyterHub` notebook (`G0-L4`, `G2-L4`) or inspecting `Weights & Biases` pretraining loss curves (`L6`) is operating at `L4–L6`, not `L1`.
  * **Low-Skill Work Inside a Terminal or Local App (`L1–L2` One-Liners):** Conversely, a hobbyist pasting a single copy-pasted install command (`ollama run llama3` or a one-click desktop installer) to chat locally without configuring `.mcp.json` schemas, writing Python, or managing `Docker` test suites is operating at `L1/L2`, not `L4`. Classification is governed strictly by the **Four-Tier Cognitive Input Hierarchy** and **Failure-Boundary Anchor** below.
* **2. Four-Tier Cognitive Input Hierarchy (`Natural Intent` $\\to$ `Structured Context` $\\to$ `Imperative Code/Config` $\\to$ `Systems/Math Invariants`):** Every human input to an AI system belongs to one of four discrete cognitive complexity tiers:
  1. **Tier I — Natural-Language Intent (`L1`, `0h`):** Unstructured conversational requests, voice commands, screenshot drops, or single-key `Tab` acceptances requiring zero syntax or parameter knowledge.
  2. **Tier II — Structured Context & Parameter Curation (`L2`, `<50h`):** Multi-shot exemplars, delimiter templates, `200k–2M` document binder curation, `Deep Research` scope constraints, and UI/Discord flag tuning (`--ar`, `temperature`) without imperative programming.
  3. **Tier III — Imperative Code, Schema & Protocol Wiring (`L3–L4`, `<200h` to `~600h`):** Writing executable `Python`/`TypeScript` SDK pipelines, `.cursorrules`, `.mcp.json` server schemas, `RBAC` metadata filters, `LangGraph` state machines, `CLAUDE.md` harness specifications, and automated `pytest`/`Docker` verification loops.
  4. **Tier IV — Distributed Systems, Formal Verifier & Mathematical Objective Design (`L5–L6`, `~2,000h` to `~10,000h`):** Sharding multi-node GPU memory (`ZeRO-3`, `PagedAttention`), isolating physical hardware sandboxes (`M4 Mac Mini OpenClaw`), engineering `GRPO` reward verifiers (`L5`), and formulating novel loss functions, pretraining data mixtures, and evaluation benchmarks (`L6`).
* **3. The Failure-Boundary Anchor (Classification by Debugging & Verification Ceiling):** Whenever a workflow appears to straddle two rungs, its true level $L_k$ is determined by **what the human operator must do when the AI fails on a non-trivial edge case**:
  * If the user can only re-roll or rephrase in plain English, they are at **`L1` (`0h`)**.
  * If the user debugs by pruning noisy PDFs from the project context window, adjusting few-shot exemplars, or auditing primary-source citation links, they are at **`L2` (`<50h`)**.
  * If the user debugs by inspecting JSON tool schemas, adjusting vector chunk overlap, editing `.mcp.json` OAuth scopes, or tuning `NeMo Colang` guardrails, they are at **`L3` (`<200h`)**.
  * If the user debugs by reading stack traces in `Claude Code`, writing reproduction unit tests in `Docker`, or tuning `LoRA` rank/learning-rate schedules on a GPU, they are at **`L4` (`~600h`)**.
  * If the user debugs by fixing `NCCL` InfiniBand hangs, tuning `vLLM` KV-cache block tables, isolating `git worktree` race conditions on a dedicated `M4 Mac Mini`, or shaping `GRPO` reward penalties, they are at **`L5` (`~2,000h`)**.
  * If the user debugs by deriving a new mathematical attention/optimization bound, re-weighting a `15-trillion-token` pretraining data mixture to fix capability collapse, or designing a new contamination-proof benchmark (`SWE-bench`), they are at **`L6` (`~10,000h`)**.
"""

def build_section_3_3_4():
    return """
#### 3.3.4 Meta-Bootstrapping Gate, Recursive Cannibalization Rule & Setup Half-Life Dual Sinking Check

To complete our counterfactual verification protocol across all 36 cells (`G0-L1` to `G5-L6`), we enforce three additional boundary gates that resolve self-referential AI usage and cross-generation sinking:

* **1. The Meta-Bootstrapping Gate (`Why Not L-1 by Asking L1 Chat to Write the L3/L4 Code?`):** A frequent counterfactual objection is: *"Why does `L3` (`<200h`) or `L4` (`~600h`) require weeks or months of study if a casual user can just ask `L1` ChatGPT/Claude to write the Python code or `.mcp.json` config for them?"* The **Meta-Bootstrapping Gate** proves why asking `L1` to generate `L3/L4` artifacts does **not** collapse `L3/L4` into `L1`:
  * While an `L1` model can emit a 100-line Python script or `Dockerfile` in `5 seconds`, **executing, authenticating, debugging, and verifying** that artifact against a live private environment hits an immediate wall at `L1`: when the generated script throws a `CUDA out of memory` error, an `OAuth 401 redirect_uri_mismatch`, a `SharePoint RBAC` permission leak, or a subtle commercial race condition (*Scale AI SWE-bench Pro* `17.8–34.1 pt` private-repo drop), a `0h` user cannot diagnose whether the bug lies in the code, the environment variables, the network firewall, or the data schema. The human learning hours at `L3` (`<200h`) and `L4` (`~600h`) measure the **minimum Beeline competence required to specify, wire, debug, and verify the execution harness when the zero-shot output fails**.
* **2. The Recursive Cannibalization Rule (How `L6` Pioneers & `L4–L5` Builders Recursively Consume `L1–L5` Tools):** Moving up the ladder to `L5` (`~2,000h`) or `L6` (`~10,000h`) never means abandoning lower-level tools; rather, **upper rungs recursively cannibalize and orchestrate all lower rungs**:
  * In `Gen 4`, an **`L6` AI Research Scientist (`~10,000h`)** formulating a novel `RLVR` mathematical objective or pretraining `Claude Opus 5.5` / `GPT-5.4` uses **`G4-L1` (`0h`)** auto-thinking chat on their phone during their morning commute, **`G4-L2` (`<50h`)** *Deep Research* to survey 100 related `arXiv` papers, **`G4-L3` (`<200h`)** `.mcp.json` connectors to query internal experiment databases, **`G4-L4` (`~600h`)** *Claude Code* terminal CLI harnesses to refactor distributed `TorchTitan` training kernels, and **`G4-L5` (`~2,000h`)** `vLLM` + `GRPO` clusters to run verifier rollouts — all in service of an **`L6` Genesis task** (producing the `Gen 5` foundation model). A workflow is classified by the **highest rung required to close its verification loop**, while explicitly logging its recursive consumption of `L1–L5`.
* **3. The Setup Half-Life Dual Sinking Check (`Cognitive Hours` + `Setup Capital` Deflation):** Under our horizontal `Why Not G+1?` counterfactual, a workflow is declared to have **sunk** from `(G_{t-1}, L_k)` to `(G_t, L_{k-m})` if and only if **both** its required human Beeline study hours $\\text{Hours}_{\\text{learn}}$ **and** its non-compute setup/maintenance friction $\\text{Setup}_{\\text{cap}}$ drop into the lower bracket's envelope (e.g., 50-PDF retrieval dropping from `G2-L3` `<200h | <$100` Python `LangChain` + `Pinecone` server maintenance to `G3-L2` `<50h | <$30` zero-code drag-and-drop `Claude Projects` / `NotebookLM`, and then to `G4-L1` `0h | $0` default chat upload).
"""

def build_gen_table(gen_idx, table_num, gen_title, window_str, users_str, tok_str, spend_str):
    sub = df_cells[df_cells["gen_idx"] == gen_idx].sort_values("level")
    rows = []
    for _, r in sub.iterrows():
        cid = r["cell_id"]
        lvl = r["level"]
        b_str = r["level_bracket_str"].replace("|", "\\|")
        name = r["canonical_name"]
        surf = r["tool_surface"]
        tut = r["tutorials_str"]
        tok = f"{int(r['tokens_task']):,}"
        flops = f"{r['flops_task']:.1e}"
        usd = f"\\${r['usd_task']:.5f}".rstrip("0").rstrip(".") if r["usd_task"] < 0.01 else f"\\${r['usd_task']:.4f}"
        wh = f"{r['wh_task']:.4f} Wh" if r["wh_task"] < 0.01 else f"{r['wh_task']:.3f} Wh"
        t_str = f"{r['human_minutes']}m / {r['ai_minutes']}m"
        s_str = f"{r['user_share_pct']:.1f}% / {r['token_share_pct']:.1f}% / {r['spend_share_pct']:.1f}%"
        rows.append(
            f"| **`{cid}`** | **`L{lvl}` (`{b_str}`)** | **{name}** | `{surf}` | `{tut}` | `{tok}` | `{flops}` | `{usd}` | `{wh}` | `{t_str}` | `{s_str}` |"
        )
    header = f"""| Cell ID | Level & Beeline Bracket | `Gen {gen_idx}` Canonical Cell Name | Dominant User Surface & Setup | Canonical Tutorial (`ID`) | Single-Task Tokens ($T$) | Single-Task FLOPs | Single-Task Cost (`USD`) | Single-Task Energy (`Wh`) | Time (`Hum / AI min`) | Gen Shares (`U% / T% / S%`) |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |"""
    footer = f"| **Total** | **`Gen {gen_idx}` Macro (`L1–L6`)** | **{window_str}** | **{users_str} Active Users** | **{tok_str} Tokens/Yr** | — | — | **{spend_str}/Yr** | — | — | **`100.0% / 100.0% / 100.0%`** |\n\n**Table {table_num} (`Table {table_num}` — `/caption` Verification):** **Complete 6-level (`L1` to `L6`) taxonomy and resource matrix for `{gen_title}` (`{window_str}`), verified against `cache_v4/v4_ladder_cells.csv` and `cache_v4/v4_tutorials.csv` (`100.0%` share conservation across `L1–L6`).**"
    return header + "\n" + "\n".join(rows) + "\n" + footer

def build_l6_profile(gen_idx):
    r = df_cells[(df_cells["gen_idx"] == gen_idx) & (df_cells["level"] == 6)].iloc[0]
    sec_num = f"4.{gen_idx+1}.7"
    cid = r["cell_id"]
    title = r["canonical_name"]
    tok = f"{int(r['tokens_task']):,}"
    flops = f"{r['flops_task']:.2e}"
    usd = f"\\${r['usd_task']:.2f}"
    wh = f"{r['wh_task']:.1f} Wh"
    hm = r["human_minutes"]
    aim = r["ai_minutes"]
    u_pct = r["user_share_pct"]
    t_pct = r["token_share_pct"]
    s_pct = r["spend_share_pct"]

    pillars_map = {
        0: (
            "**1. Foundational Math & Theory Formulation (`TRL 1–3` On-Ladder):** Derived scaled dot-product self-attention ($\\text{Attention}(Q,K,V)=\\text{softmax}(QK^T/\\sqrt{d_k})V$, Vaswani et al. `2017-06`), deep bidirectional masked language modeling (`BERT`, Devlin et al. `2018-10`), and dynamic tree-based autograd (`PyTorch`, Paszke et al. `2019`), replacing sequential `LSTM` recurrence with parallelizable matrix multiplications.",
            "**2. Pretraining & Alignment Dataset Curation (`Data Engineering`):** Curated, deduplicated, and subword-tokenized (`WordPiece`/`BPE`/`SentencePiece`) massive unlabeled text corpora including `BookCorpus` + English Wikipedia (`3.3B` words for `BERT`), `OpenWebText` / `WebText` (`40GB` Reddit-filtered links for `GPT-2`), and `Colossal Clean Crawled Corpus (C4)` (`750GB` cleaned CommonCrawl for `T5`, Raffel et al. `2019-10`).",
            "**3. Benchmark & Evaluation Metric Design (`Eval Architecture`):** Designed multi-task natural-language understanding suites **`GLUE`** (Wang et al. `2018`) and **`SuperGLUE`** (`2019`) alongside **`SQuAD 2.0`** unanswerable extractive QA (Rajpurkar et al. `2018`), establishing the quantitative leaderboards that guided all `Gen 0` representation learning.",
            "**4. From-Scratch Base Model Pretraining & `Gen 1` Genesis:** Executed multi-week distributed pretraining across `64–512` `Google Cloud TPU v2/v3` or `NVIDIA V100` pods (`BERT-Large`, `RoBERTa`, `T5-11B`, `GPT-2 1.5B`) and initiated scaling-law runs that directly birthed **`Gen 1` (`GPT-3 175B`, `2020-06`)**."
        ),
        1: (
            "**1. Foundational Math & Theory Formulation (`TRL 1–3` On-Ladder):** Formulated neural power-law scaling laws ($L(N,D,C)$ across six orders of magnitude, Kaplan et al. `2020-01`), emergent in-context few-shot learning (`GPT-3`, Brown et al. `2020-05`), and proximal policy optimization from human preferences (`InstructGPT` `RLHF`, Ouyang et al. `2022-03`).",
            "**2. Pretraining & Alignment Dataset Curation (`Data Engineering`):** Built `300B–800B` token quality-filtered pretraining mixtures (`filtered CommonCrawl`, `WebText2`, `Books1/2`, `Wikipedia`, plus `825GB` open-source **`The Pile`** by Gao et al. `2020-12` and `159GB` GitHub Python code for `Codex`) alongside the first contractor-written `SFT` demonstration and pairwise `RLHF` comparison datasets.",
            "**3. Benchmark & Evaluation Metric Design (`Eval Architecture`):** Created **`MMLU`** (`57-subject` Massive Multitask Language Understanding, Hendrycks et al. `2020-09`), **`HumanEval`** functional Python unit-test synthesis (`pass@k`, Chen et al. `2021-07`), **`BIG-bench`** (`200+` tasks, Srivastava et al. `2022`), **`GSM8K`** grade-school math (Cobbe et al. `2021`), and **`TruthfulQA`** (Lin et al. `2021`).",
            "**4. From-Scratch Base Model Pretraining & `Gen 2` Genesis:** Trained `GPT-3 175B` (`10,000` `V100` GPUs), `Codex 12B`, `Gopher 280B`, `PaLM 540B`, and `InstructGPT`, directly birthing **`Gen 2` (`ChatGPT`, `2022-11`)**."
        ),
        2: (
            "**1. Foundational Math & Theory Formulation (`TRL 1–3` On-Ladder):** Derived compute-optimal **`Chinchilla` scaling laws** ($20$ tokens per parameter, Hoffmann et al. `2022-03`), **Direct Preference Optimization (`DPO`)** closed-form policy alignment (Rafailov et al. `2023-05`), **`Constitutional AI` (`RLAIF`)** (Bai et al. `2022-12`), **Rotary Position Embeddings (`RoPE`)** long-context scaling, and Sparse Mixture-of-Experts (`MoE`) routing (`GPT-4`, `Mixtral 8x7B`).",
            "**2. Pretraining & Alignment Dataset Curation (`Data Engineering`):** Scaled clean deduplicated pretraining corpora to `2T–15T` tokens (`RedPajama`, `Dolma`, `RefinedWeb`, `FineWeb` with `MinHash LSH` deduplication and classifier quality filtering) paired with million-turn multimodal instruction and safety red-team datasets.",
            "**3. Benchmark & Evaluation Metric Design (`Eval Architecture`):** Built **`MT-Bench` & `Chatbot Arena`** crowd-sourced Elo pairwise human evaluation (Zheng et al. `2023-06`), **`SWE-bench`** real-world GitHub issue resolution in Docker (Jimenez et al. `2023-10`), **`GPQA`** PhD-level 'Google-proof' science QA (Rein et al. `2023-11`), and **`MATH`** competition problem suites.",
            "**4. From-Scratch Base Model Pretraining & `Gen 3` Genesis:** Pretrained **`GPT-4`** (`2023-03`), **`Claude 2 / Claude 3`**, and open-weight **`Llama-1 / Llama-2 / Llama-3`** across `2,000–16,000` `A100/H100` GPUs, directly birthing **`Gen 3` (`GPT-4o` & `Claude 3.5 Sonnet`, `2024-05/06`)**."
        ),
        3: (
            "**1. Foundational Math & Theory Formulation (`TRL 1–3` On-Ladder):** Formulated native multimodal early-fusion omni-tokenization (jointly modeling text, audio waveforms, and visual patches in a single transformer), **Ring Attention** blockwise long-context transformers (`1M–2M` context, Liu et al. `2023-10`), **Multi-head Latent Attention (`MLA`)**, and **Reinforcement Learning with Verifiable Rewards (`RLVR` / `GRPO`)** test-time scaling laws.",
            "**2. Pretraining & Alignment Dataset Curation (`Data Engineering`):** Constructed `15T+` token multilingual/code/multimodal corpora (`Llama-3.1 405B`, `DeepSeek-V3 14.8T` tokens) and synthetic execution-verified math, competitive programming, and multi-step tool/reasoning trajectories used to bootstrap `o1` and `DeepSeek-R1`.",
            "**3. Benchmark & Evaluation Metric Design (`Eval Architecture`):** Engineered **`SWE-bench Verified`** (`500` human-validated non-flaky GitHub issues, OpenAI `2024-08`), **`OSWorld`** real desktop GUI operating system evaluation (Xie et al. `2024-04`), **`MMMU`** multimodal understanding, **`LiveCodeBench`** contamination-free coding, and **`AIME 2024`** competition math leaderboards.",
            "**4. From-Scratch Base Model Pretraining & `Gen 4` Genesis:** Pretrained **`GPT-4o`**, **`Claude 3.5 Sonnet v1/v2`**, **`Gemini 1.5 Pro (2M)`**, **`Llama-3.1-405B`** (`16,384` `H100` GPUs), and **`OpenAI o1`**, directly birthing **`Gen 4` (`DeepSeek-R1`, `o3`, and `Claude Code`, `2025-01/02`)**."
        ),
        4: (
            "**1. Foundational Math & Theory Formulation (`TRL 1–3` On-Ladder):** Formulated large-scale pure-RL reasoning emergence (**`DeepSeek-R1-Zero` & `DeepSeek-R1` `GRPO`**, `2025-01`), hybrid instant/extended test-time compute routing, auxiliary-loss-free MoE load balancing, and multi-step computer-use / terminal environment reinforcement learning.",
            "**2. Pretraining & Alignment Dataset Curation (`Data Engineering`):** Built **synthetic verifiable reasoning & environment trajectory factories** — running millions of parallel Dockerized code compilers, `Lean 4` proof checkers, and browser/OS episodes to generate trillions of verified `<think>` and tool-use tokens overcoming the human internet text wall.",
            "**3. Benchmark & Evaluation Metric Design (`Eval Architecture`):** Created contamination-resistant commercial & multi-server benchmarks: **`Scale AI SWE-bench Pro`** (`1,865` tasks across public GPL and unseen private commercial repositories, `2025-09`), **`Terminal-Bench 2.0`**, **`OSWorld-Verified`**, **`Scale MCP Atlas`** (`1,000` multi-server tool tasks), **`ARC-AGI-2`**, and **`Humanity's Last Exam (HLE)`**.",
            "**4. From-Scratch Base Model Pretraining & `Gen 5` Genesis:** Pretrained and post-trained **`DeepSeek-R1` (`671B MoE`)**, **`OpenAI o3 / GPT-5 / GPT-5.4 (xHigh)`**, **`Anthropic Claude 4.5 / 4.6 / Opus 5.5`**, and **`Gemini 3.5 Pro`** on `25,000–100,000` `NVIDIA H200 / Blackwell B200` GPUs (`~$100M–$1B+` clusters), directly birthing **`Gen 5` (`2026-08` first-release / `2027-03` crossover)**."
        ),
    }[gen_idx]

    return f"""
#### {sec_num} Level 6 (~10,000h / ~5 Yrs Focused PhD | ~$100M+) — {title}

**The Foundation Genesis & Benchmark Architect Apex (`{cid}`):** Operating at the `Level 6` root of `Gen {gen_idx}` (`~10,000h` cumulative Beeline mastery — equivalent to a focused 5-year AI PhD — paired with `~$100M+` in supercomputer cluster capital and petabyte-scale data pipelines), `{cid}` represents **`{u_pct:.1f}%` of active users**, **`{t_pct:.1f}%` of generation token volume**, and **`{s_pct:.1f}%` of total expenditure**. Rather than treating foundational research (`TRL 1–3`), dataset curation, and benchmark creation as "off-ladder" externalities, `Level 6` integrates the **AI Research Scientists, Pretraining Data Architects, and Evaluation Benchmark Creators** whose breakthroughs in `Gen {gen_idx}` directly created the base models and built-in capabilities of `Gen {gen_idx+1}`. Crucially, under the **Recursive Cannibalization Rule (`Section 3.3.4`)**, `{cid}` scientists recursively use every `L1–L5` tool available in `Gen {gen_idx}` to accelerate their research, while their defining work spans **four mandatory `L6` pillars**:

* **1. Four Mandatory `Level 6` Pillars (`Theory + Data + Benchmarks + Pretraining`) & Track C Genesis Role:**
  * {pillars_map[0]}
  * {pillars_map[1]}
  * {pillars_map[2]}
  * {pillars_map[3]}
* **2. Keywords to Learn, Tutorials & Cumulative Beeline Hours:**
  * **Cumulative Beeline Hours:** $\\text{{Hours}}_{{\\text{{learn}}}} \\approx 10,000\\text{{ h}}$ (`~10,000h (~5 Yrs / Focused PhD) | ~$100M+` bracket).
  * **Keywords to Learn:** `{r['keywords_to_learn']}`.
  * **Foundational Monographs & Curricula:** `{r['tutorials_str']}` (`Table 2.3` & `Table 2.3b`).
* **3. Underlying Technology & Six-Factor Enablers:**
  * **Execution Surface & Setup:** `{r['tool_surface']}` (`{r['hardware_setup']}`).
  * **Causal Enablers:** `{r['tech_enablers']}`.
* **4. Single-Task & Generation-Share Resource Economics:**
  * **Single-Task Operational Metrics:** A single `{cid}` foundation pretraining checkpoint evaluation, scaling-law ablation sweep, or synthetic data/benchmark validation pass processes $T_{{\\text{{task}}}} = {tok}\\text{{ tokens}}$, executes $\\text{{FLOPs}}_{{\\text{{task}}}} = {flops}\\text{{ FLOPs}}$, costs $\\text{{USD}}_{{\\text{{task}}}} = {usd}$, consumes $\\text{{Wh}}_{{\\text{{task}}}} = {wh}$, and pairs $t_{{\\text{{human}}}} = {hm}\\text{{ min}}$ of mathematical/data/benchmark architecture with $t_{{\\text{{AI}}}} = {aim}\\text{{ min}}$ of supercomputer execution.
  * **Generation-Wide Share Metrics:** Active Users $= {u_pct:.1f}\\%$; Token Volume $= {t_pct:.1f}\\%$; Expenditure $= {s_pct:.1f}\\%$.
* **5. Four-Way Counterfactual Boundary Proof:**
  * **Why Not Lower (`L-1` at `G{gen_idx}-L5` — Failure Mode):** `{r['why_not_lower_L_minus_1']}` While `G{gen_idx}-L5` (`~2,000h | ~$500k`) engineers excel at distributed serving, post-training adaptation, and sandbox orchestration of *existing* architectures, they do not formulate new mathematical attention/RL objectives (`TRL 1–3`), curate multi-trillion-token pretraining mixtures from raw web crawls, or pretrain frontier base models from random weight initialization.
  * **Why Not Higher (`L+1` — Genesis Ceiling):** `{r['why_not_higher_L_plus_1']}`
  * **Why Not Before (`G-1` — Prior-Gen Barrier):** `{r['why_not_before_G_minus_1']}`
  * **Why Not After (`G+1` — Next-Gen Built-In Sinking & Genesis Impact):** `{r['why_not_after_G_plus_1']}`
"""

def build_master_table_5_1a():
    sub = df_cells[df_cells["gen_idx"] <= 4].sort_values(["gen_idx", "level"])
    gen_totals = {
        0: (12.0, 0.18, 1.1),
        1: (45.0, 1.60, 3.8),
        2: (380.0, 28.00, 14.0),
        3: (720.0, 240.00, 39.0),
        4: (1150.0, 1100.00, 88.0),
    }
    rows = []
    for _, r in sub.iterrows():
        g = int(r["gen_idx"])
        u_tot, t_tot, s_tot = gen_totals[g]
        u_abs = u_tot * r["user_share_pct"] / 100.0
        t_abs = t_tot * r["token_share_pct"] / 100.0
        s_abs = s_tot * r["spend_share_pct"] / 100.0
        b_str = r["level_bracket_str"].replace("|", "\\|")
        tok = f"{int(r['tokens_task']):,}"
        flops = f"\\${r['flops_task']:.2e}$".replace("e+", "\\times 10^{") + "}"
        flops = f"${r['flops_task']:.2e}$"
        usd = f"\\${r['usd_task']:.5f}"
        wh = f"{r['wh_task']:.4f} Wh"
        hm_ai = f"`{r['human_minutes']}m` / `{r['ai_minutes']}m`"
        rows.append(
            f"| **`{r['cell_id']}`** | *{r['status']}:* {r['canonical_name']} | `{b_str}` | `{tok}` | {flops} | `{usd}` | `{wh}` | {hm_ai} | `{r['user_share_pct']:.1f}%` (`{u_abs:.2f}M`) | `{r['token_share_pct']:.1f}%` (`{t_abs:.3f}T`) | `{r['spend_share_pct']:.1f}%` (`\\${s_abs:.3f}B`) |"
        )
    header = """**Master Table 5.1a (`Master Table 5.1a` — `/caption` Verification):** **Complete 30-Cell Historical & Contemporary Master Verification Ledger (`Gen 0`–`Gen 4` $\\times$ `Level 1`–`Level 6`; `36` cells total including `Gen 5` in `Table 5.4b`), combining single-number Beeline brackets, single-task compute/cost/energy/time metrics, and generation-wide user, token, and expenditure shares (`2017–2026`, `cache_v4/v4_ladder_cells.csv`).** Across all `30` historical cells (`G0-L1` to `G4-L6`), Pearson correlation between log user learning hours and log single-task USD cost within each generation exceeds $r = +0.96$ ($p < 0.0001$), while every generation sums to exactly `100.0%` across User Share, Token Share, and Spend Share across all `6` levels (`L1` to `L6`).

| Cell ID | Status & User-First Title | Single-Number Beeline Bracket (`Hours \\| Cap`) | Single-Task Tokens | Single-Task FLOPs | Single-Task USD | Single-Task Wh | Human vs AI Min | User Share % (Abs Users) | Token Share % (Abs Tokens/yr) | Spend Share % (Abs Spend/yr) |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |"""
    footer = "| **30-Cell Historical Summary (`G0–G4 × L1–L6`)** | **30 Verified Coordinates (+6 `Gen 5` = 36 Total)** | **6 Standardized Brackets (`0h` to `~10,000h`)** | **Span: `25` to `25,000,000` tok** | **Span: $1.5\\times 10^8$ to $3.8\\times 10^{16}$** | **Span: `\\$0.00001` to `\\$65.00`** | **Span: `0.0002` to `480 Wh`** | **Inversion at `G4-L2/L4/L5/L6`** | **Peak: `1,150.0M` Users (`G4`)** | **Cumul Rate: `1,369.8T/yr`** | **Cumul Rate: `\\$145.9B/yr`** |"
    return header + "\n" + "\n".join(rows) + "\n" + footer

def build_table_5_2a():
    rows = []
    for _, r in df_trl.iterrows():
        rows.append(
            f"| **`{r['trl_id']}`: {r['breakthrough']}** | `{r['trl_1_3_l6_genesis_date']}` | `{r['trl_4_5_proto_date_level']}` | `{r['trl_7_power_date_level']}` | `{r['trl_9_builtin_l1_date']}` | **`{int(r['total_lag_months'])} mos`** | {r['primary_bottleneck']} |"
        )
    header = """**Table 5.2a (`Table 5.2a` — `/caption` Verification):** **On-Ladder Technology Readiness Level (`TRL 1` to `TRL 9`) Maturation Ledger across `10` Core AI Capabilities (`2017–2026`, `cache_v4/v4_trl_trajectories.csv`), proving that every breakthrough originates on-ladder at `Level 6 (L6)` (`TRL 1–3` mathematical formulation, dataset/benchmark design, and initial base-model pretraining) before descending through `L4–L5` (`TRL 4–5`) and `L2–L3` (`TRL 7`) into `L1/L2` built-in defaults (`TRL 9`) with a mean maturation lag of $\\mu = 36.2\\text{ months}$ (median $= 35.5\\text{ months}$, $\\text{IQR} = 18.0\\text{ months}$).**

| TRL ID & Core AI Breakthrough | `TRL 1–3` On-Ladder Genesis Date, **`L6` Cell** & Anchor Citation | `TRL 4–5` Prototype Date & Initial Builder Cell (`L3–L4`) | `TRL 7` Power-User Date & Intermediate Cell (`L2–L4`) | `TRL 9` Built-In `Level 1/2` Default Date & Target Cell | Total `L6` $\\to$ `L1` Lag (Months) | Primary Causal Bottleneck Governing Down-Ladder Maturation |
| :--- | :--- | :--- | :--- | :--- | :---: | :--- |"""
    footer = "| **Summary Statistics Across 10 Core Breakthroughs (`TRL_01`–`TRL_10`)** | **100% Originate On-Ladder at `G0-L6`..`G3-L6` (`TRL 1–3`)** | **Descends to `L3–L4` (`+12.4 mos` mean delay from `L6` paper)** | **Reaches `L2–L3` Power Users (`+22.8 mos` mean delay)** | **Reaches `TRL 9` `L1/L2` Default (`2019-11` to `2025-12`)** | **Mean $\\mu = 36.2\\text{ mos}$ \\| Median $= 35.5\\text{ mos}$ \\| $\\text{IQR} = 18.0\\text{ mos}$ (`Min=13m, Max=65m`)** | **Dominant Bottlenecks: `L6` Post-Training Alignment (`RLHF`/`RLVR`), Context/Caching Economics, and Open Protocol/UI Packaging** |"
    return header + "\n" + "\n".join(rows) + "\n" + footer

def build_table_5_4b_and_g5_l6():
    sub = df_cells[df_cells["gen_idx"] == 5].sort_values("level")
    rows = []
    for _, r in sub.iterrows():
        cid = r["cell_id"]
        lvl = int(r["level"])
        b_str = r["level_bracket_str"].replace("|", "\\|")
        u_abs = 1650.0 * r["user_share_pct"] / 100.0
        t_abs = 4800.0 * r["token_share_pct"] / 100.0
        rows.append(
            f"| **`{cid}`** (`Level {lvl}`) | **{r['canonical_name']}** | `{b_str}` | `{r['tool_surface']}` | `{int(r['tokens_task']):,}` tok (`{r['flops_task']:.1e}` FLOPs) | `\\${r['usd_task']:.3f}` | `{r['wh_task']:.3f} Wh` | `{r['human_minutes']}m` hum / `{r['ai_minutes']}m` AI | **`{r['user_share_pct']:.1f}%`** (`{u_abs:.2f}M`) | **`{r['token_share_pct']:.1f}%`** (`{t_abs:.1f}T`) | **`{r['spend_share_pct']:.1f}%`** |"
        )
    r6 = sub[sub["level"] == 6].iloc[0]
    header = """**Table 5.4b (`Table 5.4b` — `/caption` Verification):** **`Gen 5` (`Current + 1`: `2026-08` First-Release / `2027-03` Mainstream Crossover to `2028-12`) Speculative 6-Level User-Skill Matrix, Single-Task Resource Physics & Conservation Shares (`G5-L1` to `G5-L6`, `cache_v4/v4_gen5_speculative.csv`).** Every cell obeys strict 6-level share conservation ($\\sum_{L=1}^6 \\text{UserShare} = 100.0\\%$, $\\sum_{L=1}^6 \\text{TokenShare} = 100.0\\%$, $\\sum_{L=1}^6 \\text{SpendShare} = 100.0\\%$) and is bounded against the four historical extinction traps (`Section 5.2.3`).

| Cell ID & Level | User-Centric Workflow Title | Single-Number Beeline Bracket (`Hours \\| Cap`) | Tool Surface & Setup Friction (`Setup_cap`) | Single-Task Tokens ($T_{\\text{task}}$) | Single-Task Cost ($\\text{USD}_{\\text{task}}$) | Single-Task Energy ($\\text{Wh}_{\\text{task}}$) | Human / AI Time ($t_{\\text{hum}} / t_{\\text{AI}}$) | User Share (`%` of `1,650M`) | Token Share (`%` of `4,800T`) | Spend Share (`%` of `\\$195B`) |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |"""
    footer = """| **`Gen 5` Total / Conservation Check (`L1–L6`)** | **All `6` Standardized User-Skill Rungs (`G5-L1` to `G5-L6`)** | **Monotonic Single-Number Brackets (`0h` to `~10,000h`)** | **OS-Native Ambient Layer (`L1`) to Exascale Genesis Pod (`L6`)** | **`2,667x` Span (`45k` to `120M` tok)** | **`16,667x` Span (`\\$0.015` to `\\$250.00`)** | **`6,364x` Span (`0.22` to `1,400 Wh`)** | **Autonomous Ratio $t_{\\text{AI}}/t_{\\text{hum}} = 4.4\\times\\text{ to }48.0\\times$** | **`100.0%`** (`1,650.0M` users) | **`100.0%`** (`4,800.0T` tok/yr) | **`100.0%`** (`\\$195.0B/yr`) |"""
    g5_l6_profile = f"""

##### `G5-L6` — `Level 6` (`~10,000h (~5 Yrs / Focused PhD) | ~$100M+`): {r6['canonical_name']}

**`G5-L6` Cell BLUF:** At the `Level 6` Genesis apex of `Gen 5` (`~10,000h` Focused PhD mastery paired with `~$100M–$1B+` exascale compute pods), `G5-L6` AI Research Scientists, Synthetic Data Architects, and Formal Benchmark Creators (`0.1%` of users = `1.65M` researchers, `9.0%` of tokens = `432.0T` tokens/yr, `11.0%` of spend = `\\$21.45B/yr`) design the post-Transformer continuous-learning architectures, autonomous laboratory simulators, and formal mathematical proof oracles (`Lean 5`) that birth `Gen 6` (`post-2029`), consuming `120,000,000` tokens (`1.4e17` FLOPs, `\\$250.00`, `1,400.0 Wh`, and `2,880.0 min` [`48.0h`] of supercomputer runtime per `60.0 min` human theoretical specification).

* **1. Four Mandatory `Level 6` Pillars (`Theory + Data + Benchmarks + Pretraining`) & Recursive Tool Use:**
  * **Pillar 1 — Foundational Math & Post-Transformer Theory Formulation (`TRL 1–3` On-Ladder):** Formulating sub-quadratic / test-time plasticity architectures (continual weight-updating state-space/attention hybrids with zero catastrophic forgetting) and self-evolving mathematical discovery curricula.
  * **Pillar 2 — Pretraining & Closed-Loop Synthetic Dataset Curation:** Engineering self-play synthetic data engines coupled to physical/wet-lab robotic simulators and formal mathematical proof kernels (`Lean 5`), generating trillions of verified out-of-distribution scientific trajectories beyond human text.
  * **Pillar 3 — Benchmark & Formal Oracle Evaluation Design:** Creating `Gen 5/6` evaluation suites where open-ended scientific theorems, chip layouts, and systems architectures are graded automatically by formal mathematical proof oracles (`Lean 5` / `TLA+`) and closed-loop physical simulation benchmarks (`ARC-AGI-3` / `SciGym`).
  * **Pillar 4 — From-Scratch Next-Gen Foundation Pretraining & `Gen 6` Genesis:** Pretraining unified multimodal + embodied world-model foundation architectures across `100,000+` `NVIDIA Vera Rubin` / `TPU v7` accelerators while recursively using `G5-L1` ambient OS delegates, `G5-L4` formal verifier swarms, and `G5-L5` nightly `RLVR` flywheels.
* **2. Keywords to Learn, Tutorials & Cumulative Beeline Hours:** **`~10,000h (~5 Yrs / Focused PhD) | ~$100M+`**. Keywords: `{r6['keywords_to_learn']}` (`TUT_25`).
* **3. Underlying Technology & Six-Factor Enablers:** Powered by `{r6['tool_surface']}` (`{r6['hardware_setup']}`) and `{r6['tech_enablers']}`.
* **4. Single-Task & Generation-Share Resource Economics:** Consumes **`120,000,000` tokens** (`1.4e17` FLOPs, **`\\$250.000`**, **`1,400.000 Wh`**, `60.0 min` human / `2,880.0 min` [`48.0h`] AI). Across `Gen 5`, `G5-L6` accounts for **`0.1%` of users** (`1.65M`), **`9.0%` of tokens** (`432.0T` tokens/yr), and **`11.0%` of spend** (`\\$21.45B/yr`).
* **5. Four-Way Counterfactual Boundary Proof:**
  * **Why Not Lower (`L-1` — Failure Mode at `G5-L5`):** `{r6['why_not_lower_L_minus_1']}`
  * **Why Not Higher (`L+1` — Genesis Ceiling):** `{r6['why_not_higher_L_plus_1']}`
  * **Why Not Before (`G-1` — Prior-Gen Barrier in `Gen 4`):** `{r6['why_not_before_G_minus_1']}`
  * **Why Not After (`G+1` — Next-Gen Built-In Sinking in `Gen 6`):** `{r6['why_not_after_G_plus_1']}`
"""
    return header + "\n" + "\n".join(rows) + "\n" + footer, g5_l6_profile

# Let's assemble the full v4 text by transforming v3_lines and injecting all v4 tables and sections
text = "\n".join(v3_lines)

# 1. Replace Frontispiece & Title block (lines 1 to 20) — Mini-Mega FIRST before the full Mega!
new_frontispiece = """![Plot 0-Mini: The AI Ladder Evolution Atlas (2017–2028) — Distilled Executive Mini-Megachart](figures_v4/fig_v4_p0_mini_megachart.png)

![Plot 0: The AI Ladder Evolution Atlas (2017–2028) — Encyclopedic Broadside Wallchart](figures_v4/fig_v4_p0_encyclopedic_megachart_poster.png)

* **Frontispiece Broadside Wallcharts (`Plot 0-Mini` Distilled Executive Edition First, Followed by `Plot 0` Full Encyclopedic Poster — `/caption` & `/citra` Verification):** **Across six chronological generations (`Gen 0` to `Gen 5`, `2017–2028`) and six standardized user-learning brackets (`Level 1` at `0h (0d) | $0` placed at the top row `y=6` down to `Level 6` at `~10,000h (~5 Yrs / Focused PhD) | ~$100M+` placed at the bottom foundation row `y=1`), every generation boundary is governed by a `1 to 2` level downward skill-deflation escalator ($\\mu = 534.0\\text{h} \\to 2.4\\text{h} \\to 0.9\\text{h}$) coupled with a $26,667\\times$ expansion in global annual token volume ($0.18\\text{T} \\to 4,800\\text{T}\\text{ tokens/yr}$) and a $137.5\\times$ expansion in active AI users ($12\\text{M} \\to 1,650\\text{M}$).** Placed at the very start of this document before the main title — with the rapid-inspection executive edition (`Plot 0-Mini`, `figsize=(22, 16.5), dpi=200`) presented first, followed immediately by the full encyclopedic broadside poster (`Plot 0`, `figsize=(44, 32), dpi=300`) — both wallcharts share the same five-panel `GridSpec(3, 2)` geometry (`ax_main`, `ax_right`, `ax_trap`, `ax_bot`, `ax_corner`):
  * **Top-Left Title & Plain-English Subtitle Banner (No Em Dash):** Anchored at top-left in bold display typography (`"AI Ladder Evolution"`) paired on the right with the exact 3-line plain-English italic (`#3B3B3B`) subtitle: *"This is an AI ladder from the user perspective, mapping how much time and money a person must invest to use or build AI across different eras. AI technology moves very quickly, so any static ladder definition gets obsolete very quickly, which is why we need this evolution rather than a single ladder. Each column is a new generation of AI, and each row is a user skill level from zero-study everyday use at the top to frontier research at the bottom."*
  * **Top-Left Main Panel (`6-Generation × 6-Level Matrix`, `36` Zero-Clutter 3-Part Cards):** Maps all `30` historical and contemporary adopted cells (`Gen 0` to `Gen 4`, `2017-06` to `2026-10`) in solid multi-hue borders alongside the `6` controlled speculative `Gen 5` (`Current + 1`, `2026-08` first-release / `2027-03` production-crossover to `2028-12`) forecast cells in dashed violet (`#CC79A7`) borders. To maximize readability, zero alluvial ribbons or `X` badges cross over the cards. Every column header (`GEN 0`..`GEN 5`) is color-synchronized with its corresponding step-histogram curve in the right marginal panel, with **only `GEN X` and `LEVEL X` bolded** while generation names and single-number Beeline brackets (`0h (0d) | $0`, `<50h (~1 Wk / Short Course) | <$30`, `<200h (~1 Mo / 1 Uni Subject) | <$100`, `~600h (~1 Qtr / 1 Uni Semester) | ~$1.5k`, `~2,000h (~1 Yr / Core Postgrad) | ~$500k`, `~10,000h (~5 Yrs / Focused PhD) | ~$100M+`) appear in clean normal font weight. Inside each of the 36 cells, the card is divided into three clean visual zones: (1) a **2-line bold white Cell Name** in the colored header band, (2) a **2-line normal-font Description** in the upper body, and (3) a subtle dotted divider followed by **1 line of italic `#3B3B3B` Keywords** (all 36 keywords formally defined and cited in `Section 2.2.2b` and `Table 2.3b`).
  * **Top-Right Marginal Panel (`10-Line Relative-Frequency Distribution`, Share-Aligned with `Level 1–6` Rows):** Displays `10` distinct step-histogram curves with alpha transparency (`5` solid lines for `User Relative Frequency` and `5` dashed lines for `Token Relative Frequency` across `Gen 0` through `Gen 4`, $\\sum_{L=1}^6 = 1.00$), paired with per-level mean callout boxes proving that while `Level 1` (`0h`) captures $\\mu = 0.63$ of users, `Levels 2–6` consume $\\mu = 0.84$ of global token volume.
  * **Middle Trapezium Time-Warp Bridge (`ax_trap` Connecting Non-Linear Generation Columns to Linear Calendar Time):** Explicitly renders 6 semi-transparent color-matched polygons connecting the equal-width column boundaries of `Gen 0`–`Gen 5` above to their true calendar-duration spans (`36m`, `29m`, `18m`, `8m`, `22m`, `21m`) on the linear `2017.4–2028.9` timeline below, visually proving why generation durations compressed from `36 months` (`Gen 0`) to `8 months` (`Gen 3`) before stabilizing at `22 months` (`Gen 4`).
  * **Bottom-Left Temporal Panel (`2 Macro Growth Curves + 12 Headline Milestones`) & Bottom-Right Legend Cartouche:** Plots **Global Active AI Users (`Millions`, `#D55E00`, $12\\text{M} \\to 1,150\\text{M} \\to 1,650\\text{M}$)** and **Global Annualized Token Volume (`Trillions`, `#0072B2`, $0.18\\text{T} \\to 1,100\\text{T} \\to 4,800\\text{T}\\text{ tokens/yr}$)** across `2017–2028`, anchored by the vertical crimson `TODAY = 2026-10-20` beacon and the bottom-right legend cartouche.

***

# AI Ladder Evolution (v4): A Six-Generation × Six-Level (36-Cell) User-Skill Taxonomy, Counterfactual Boundary Proof & Evolutionary Audit of AI Workflows (2017–2028)"""

old_frontispiece_end = text.find("**Bottom-Line Executive Synthesis:**")
text = new_frontispiece + "\n\n" + text[old_frontispiece_end:]

# 2. Update figures_v3 -> figures_v4, cache_v3 -> cache_v4, v3_ -> v4_
text = text.replace("figures_v3/fig_v3_", "figures_v4/fig_v4_")
text = text.replace("cache_v3/v3_", "cache_v4/v4_")
text = text.replace("v3_data_and_gates.py", "v4_data_and_gates.py")
text = text.replace("v3_ladder_cells.csv", "v4_ladder_cells.csv")
text = text.replace("v3_skill_deflation_benchmarks.csv", "v4_skill_deflation_benchmarks.csv")
text = text.replace("v3_existing_ladders.csv", "v4_existing_ladders.csv")
text = text.replace("v3_gen5_cutoff_windows.csv", "v4_gen5_cutoff_windows.csv")
text = text.replace("v3_gen5_speculative.csv", "v4_gen5_speculative.csv")

# 3. Synchronize Plot 11, Plot 12, Plot 13 numbering in Part II and Part V
text = text.replace(
    "![Plot 11: Animated AI Ladder Evolution Trajectory (2017–2026)](figures_v4/fig_v4_p11_ladder_evolution_anim.gif)",
    "![Plot 13: Animated AI Ladder Evolution Trajectory (2017–2026)](figures_v4/fig_v4_p13_ladder_evolution_anim.gif)"
)
text = text.replace("Figure 5.1b (`Plot 11`", "Figure 5.1b (`Plot 13`")
text = text.replace("(`Plot 10` & `Plot 13`)", "(`Plot 10` & `Plot 13`)")
text = text.replace(
    "![Plot 12: TRL Maturation Trajectories & Population Evolution of the Inventory of Hope](figures_v4/fig_v4_p12_trl_and_failed_hopes.png)",
    "![Plot 11: On-Ladder L6 (TRL 1–3) to L1 (TRL 9) Maturation Trajectories & Population Evolution of the Inventory of Hope](figures_v4/fig_v4_p11_trl_and_failed_hopes.png)"
)
text = text.replace("Figure 5.2 (`Plot 12`", "Figure 5.2 (`Plot 11`")
text = text.replace("Synthesizing `Table 5.2b` and `Plot 12`", "Synthesizing `Table 5.2b` and `Plot 11`")
text = text.replace(
    "![Plot 13: Published AI Ladders (2017–2026) Tri-Partite Pairwise Alignment Matrix](figures_v4/fig_v4_p13_ladder_comparison_matrix.png)",
    "![Plot 12: Published AI Ladders (2017–2026) Tri-Partite Pairwise Alignment Matrix](figures_v4/fig_v4_p12_ladder_comparison_matrix.png)"
)
text = text.replace("Figure 5.3 (`Plot 13`", "Figure 5.3 (`Plot 12`")
text = text.replace("(`Plot 13` & `Table 5.3a`)", "(`Plot 12` & `Table 5.3a`)")

# 4. Synchronize Section 5.3.1 & Table 5.3a stats with exact Plot 12 values
text = text.replace(
    "1. **`Scope Coverage` ($\\mu = 0.83$, $\\text{Med} = 0.83$, $\\text{IQR} = 0.10$, $\\text{Min} = 0.70$, $\\text{Max} = 0.96$):**",
    "1. **`Scope Coverage` ($\\mu = 0.84$, $\\text{Med} = 0.84$, $\\text{IQR} = 0.09$, $\\text{Min} = 0.70$, $\\text{Max} = 0.96$):**"
)
text = text.replace(
    "2. **`User-Skill Alignment` ($\\mu = 0.82$, $\\text{Med} = 0.83$, $\\text{IQR} = 0.12$, $\\text{Min} = 0.60$, $\\text{Max} = 0.95$):**",
    "2. **`User-Skill Alignment` ($\\mu = 0.82$, $\\text{Med} = 0.83$, $\\text{IQR} = 0.11$, $\\text{Min} = 0.60$, $\\text{Max} = 0.95$):**"
)
text = text.replace(
    "3. **`Historical Invariance` ($\\mu = 0.82$, $\\text{Med} = 0.83$, $\\text{IQR} = 0.11$, $\\text{Min} = 0.68$, $\\text{Max} = 0.94$):**",
    "3. **`Historical Invariance` ($\\mu = 0.82$, $\\text{Med} = 0.83$, $\\text{IQR} = 0.09$, $\\text{Min} = 0.68$, $\\text{Max} = 0.94$):**"
)
text = text.replace(
    "proving that `Scope Coverage` and `Historical Invariance` correlate strongly ($r = +0.76, R^2 = 0.58, \\text{MAE} = 0.04$), whereas `User-Skill Alignment` and `Empirical Cost Grounding` exhibit weaker coupling ($r = +0.43, R^2 = 0.19, \\text{MAE} = 0.12$)",
    "proving that `Scope Coverage` and `Historical Invariance` correlate strongly ($r = +0.80, R^2 = 0.64, \\text{MAE} = 0.04$), whereas `User-Skill Alignment` and `Empirical Cost Grounding` exhibit moderate coupling ($r = +0.52, R^2 = 0.27, \\text{MAE} = 0.14$)"
)
text = text.replace(
    "| **Mean / Median / IQR Across 20 Literature Ladders (`L_LIT_01`–`L_LIT_20`)** | **1 to 5 Gens** | **Partial Vertical Slices** | **$\\mu=0.83$** (`IQR=0.10`) | **$\\mu=0.82$** (`IQR=0.12`) | **$\\mu=0.82$** (`IQR=0.11`) | **$\\mu=0.74$** (`IQR=0.24`) | **1D Ladders Conflate Tech Era (`Gen`) with User Learning (`Level`); Mean Composite Score $= 0.801$** |",
    "| **Mean / Median / IQR Across 20 Literature Ladders (`L_LIT_01`–`L_LIT_20`)** | **1 to 5 Gens** | **Partial Vertical Slices** | **$\\mu=0.84, \\text{Med}=0.84$** (`IQR=0.09`) | **$\\mu=0.82, \\text{Med}=0.83$** (`IQR=0.11`) | **$\\mu=0.82, \\text{Med}=0.83$** (`IQR=0.09`) | **$\\mu=0.74, \\text{Med}=0.76$** (`IQR=0.24`) | **1D Ladders Conflate Tech Era (`Gen`) with User Learning (`Level`); Scope vs. Hist $r=+0.80, R^2=0.64, \\text{MAE}=0.04$; Skill vs. Cost $r=+0.52, R^2=0.27, \\text{MAE}=0.14$** |"
)

# 5. Replace Table 1.2
t12_start = text.find("##### Table 1.2:")
t12_end = text.find("---", t12_start)
text = text[:t12_start] + build_table_1_2() + "\n\n" + text[t12_end:]

# 6. Replace Table 2.2
t22_start = text.find("##### Table 2.2:")
t22_end = text.find("#### 2.2.2 Timestamped Tutorials", t22_start)
text = text[:t22_start] + build_table_2_2() + "\n\n" + text[t22_end:]

# 7. Replace Table 2.3 and append Section 2.2.2b + Table 2.3b
t23_start = text.find("##### Table 2.3:")
t23_end = text.find("#### 2.2.3 The Inventory of Hope", t23_start)
text = text[:t23_start] + build_table_2_3() + "\n\n" + build_section_2_2_2b() + "\n" + text[t23_end:]

# 8. Replace Table 3.2 and append Section 3.2.4
t32_start = text.find("| Neutral Level ID | Learning-Hour Bracket")
t32_end = text.find("#### 3.2.2 Track A", t32_start)
text = text[:t32_start] + build_table_3_2() + "\n\n" + text[t32_end:]

s323_end = text.find("### 3.3 Four-Way Counterfactual Cell Verification Protocol")
text = text[:s323_end] + build_section_3_fixes() + "\n***\n\n" + text[s323_end:]

s333_end = text.find("### 3.4 Deferred Folksonomy Naming Protocol")
text = text[:s333_end] + build_section_3_3_4() + "\n***\n\n" + text[s333_end:]

# 9. Add L6 row to Table 3.4
text = text.replace(
    "| **`L5`** | `600–2,000h+` (`6+ Mos` + Infra) | `Distributed Systems/Pretraining Architect`, `vLLM Cluster Ops`, `RLVR GRPO Trainer`, `OpenClaw Sandbox Host` | **Level 5 (600–2,000h+ 6+ Months & Dedicated Infra): Cluster, RLVR & Dedicated Sandbox Apex** | Top human investment tier requiring either multi-node GPU clusters (`Fairseq`, `DeepSpeed`, `vLLM`, `GRPO`) or dedicated physical air-gapped hardware (`M4 Mac Mini` `OpenClaw`). |",
    "| **`L5`** | `~2,000h (~1 Yr / Core Postgrad) \\| ~$500k` | `Staff Sandbox/Infra SWE`, `vLLM Cluster Ops`, `RLVR GRPO Trainer`, `OpenClaw M4 Mac Mini Sandbox` | **Level 5 (~2,000h / ~1 Yr Core Postgrad \\| ~$500k): Staff Sandbox/Infra SWE & Distributed Post-Training MLE** | Staff systems & post-training tier requiring multi-node GPU clusters (`Fairseq`, `DeepSpeed`, `vLLM`, `GRPO`) or dedicated air-gapped hardware (`M4 Mac Mini` `OpenClaw`). |\n| **`L6`** | `~10,000h (~5 Yrs / Focused PhD) \\| ~$100M+` | `AI Research Scientist`, `Pretraining Data Architect`, `Benchmark Creator (GLUE/MMLU/SWE-bench)`, `Foundation Pretrainer` | **Level 6 (~10,000h / ~5 Yrs Focused PhD \\| ~$100M+): AI Research Scientist, Data/Benchmark Architect & Next-Gen Pioneer** | Foundation genesis tier (`TRL 1–3` on-ladder): formulates novel math theory, curates trillion-token corpora, designs eval benchmarks, and pretrains `G+1` base models (`~$100M+`). |"
)

# 10. Replace Table 4.1, 4.2, 4.3, 4.4, 4.5 with 6-level tables and append G0-L6..G4-L6 sections
# Table 4.1
t41_start = text.find("| Cell ID & User-First Title | Learning Hours")
t41_end = text.find("#### Section 4.1 Structural Index", t41_start)
text = text[:t41_start] + build_gen_table(0, "4.1", "Gen 0: The Pre-LLM Code-Pipeline & Passive-Widget Generation", "36 Months (2017-06 to 2020-05)", "12.0M", "0.18T", "\\$1.10B") + "\n\n" + text[t41_end:]

# Append G0-L6 before ### 4.2
g1_header_pos = text.find("### 4.2 Gen 1")
text = text[:g1_header_pos] + build_l6_profile(0) + "\n---\n\n" + text[g1_header_pos:]

# Table 4.2
t42_start = text.find("| Cell ID | Level (`Hours`) | `Gen 1` Canonical Cell Name |")
t42_end = text.find("#### 4.2.2 Level 1", t42_start)
text = text[:t42_start] + build_gen_table(1, "4.2", "Gen 1: The Playground Completion & Few-Shot Craft Generation", "29 Months (2020-06 to 2022-10)", "45.0M", "1.60T", "\\$3.80B") + "\n\n" + text[t42_end:]

# Append G1-L6 before ### 4.3
g2_header_pos = text.find("### 4.3 Gen 2")
text = text[:g2_header_pos] + build_l6_profile(1) + "\n---\n\n" + text[g2_header_pos:]

# Table 4.3
t43_start = text.find("| Cell ID | Level (`Hours`) | `Gen 2` Canonical Cell Name |")
t43_end = text.find("#### 4.3.2 Level 1", t43_start)
text = text[:t43_start] + build_gen_table(2, "4.3", "Gen 2: The Conversational Chatbot & DIY RAG Generation", "18 Months (2022-11 to 2024-04)", "380.0M", "28.00T", "\\$14.00B") + "\n\n" + text[t43_end:]

# Append G2-L6 before ### 4.4
g3_header_pos = text.find("### 4.4 Gen 3")
text = text[:g3_header_pos] + build_l6_profile(2) + "\n---\n\n" + text[g3_header_pos:]

# Table 4.4
t44_start = text.find("**Table 4.4 (`Table 4.4`")
t44_end = text.find("#### 4.4.1 Six-Factor Causal Drivers", t44_start)
text = text[:t44_start] + build_gen_table(3, "4.4", "Gen 3: The Long-Context Omni-Workspace & Stateful Graph Generation", "8 Months (2024-05 to 2024-12)", "720.0M", "240.00T", "\\$39.00B") + "\n\n" + text[t44_end:]

# Append G3-L6 before ### 4.5
g4_header_pos = text.find("### 4.5 Gen 4")
text = text[:g4_header_pos] + build_l6_profile(3) + "\n---\n\n" + text[g4_header_pos:]

# Table 4.5
t45_start = text.find("**Table 4.5 (`Table 4.5`")
t45_end = text.find("**Table 4.6 (`Table 4.6`", t45_start)
text = text[:t45_start] + build_gen_table(4, "4.5", "Gen 4: The Reasoning Agent, CLI/MCP & Always-On Sandbox Generation", "22 Months (2025-01 to 2026-10)", "1,150.0M", "1,100.00T", "\\$88.00B") + "\n\n" + text[t45_end:]

# Append G4-L6 before ## 5. Part V
p5_header_pos = text.find("## 5. Part V — Cross-Gen Synthesis")
text = text[:p5_header_pos] + build_l6_profile(4) + "\n***\n\n" + text[p5_header_pos:]

# 11. Replace Master Table 5.1a
t51a_start = text.find("**Master Table 5.1a (`Master Table 5.1a`")
t51a_end = text.find("**Master Table 5.1b (`Master Table 5.1b`", t51a_start)
text = text[:t51a_start] + build_master_table_5_1a() + "\n\n" + text[t51a_end:]

# 12. Update Section 5.2.1 TRL 1-3 On-Ladder L6 Integration & Replace Table 5.2a
old_trl_bullet = "* **`TRL 1–2` (Theoretical Formulation & `arXiv` Preprint — Pre-Ladder Research):** An algorithm is formulated mathematically and demonstrated on synthetic or academic toy benchmarks (`Vaswani et al. 2017-06`, `Christiano et al. RLHF 2017-06`, `Lewis et al. RAG 2020-05`, `Hu et al. LoRA 2021-06`, `Wei et al. CoT 2022-01`). Zero mainstream user workflows exist."
new_trl_bullet = "* **`TRL 1–3` (Theoretical Formulation, Dataset/Benchmark Design & `arXiv` Preprint — On-Ladder Genesis at `Level 6 [L6]`, `~10,000h (~5 Yrs / Focused PhD) | ~$100M+`):** Rather than treating foundational research as off-ladder, `TRL 1–3` sits directly on-ladder at **`Level 6` (`G0-L6` through `G4-L6`)**, where AI Research Scientists, Pretraining Data Architects, and Benchmark Creators formulate novel mathematical objectives (`Vaswani et al. 2017-06` at `G0-L6`, `Christiano et al. RLHF` / `Brown et al. GPT-3` at `G0/G1-L6`, `Hu et al. LoRA` / `Wei et al. CoT` at `G1-L6`, `Rafailov et al. DPO` / `Hoffmann et al. Chinchilla` at `G2-L6`, `DeepSeek-R1 GRPO` at `G3/G4-L6`), curate multi-trillion-token corpora, and design the evaluation benchmarks (`GLUE`, `MMLU`, `SWE-bench`) that birth `Gen G+1`."
text = text.replace(old_trl_bullet, new_trl_bullet)

t52a_start = text.find("**Table 5.2a (`Table 5.2a`")
t52a_end = text.find("#### 5.2.2 Population Evolution", t52a_start)
text = text[:t52a_start] + build_table_5_2a() + "\n\n" + text[t52a_end:]

# 13. Replace Table 5.4b and append G5-L6 at the end of Part V
t54b_start = text.find("**Table 5.4b (`Table 5.4b`")
t54b_end = text.find("##### `G5-L1`", t54b_start)
t54b_md, g5_l6_md = build_table_5_4b_and_g5_l6()
text = text[:t54b_start] + t54b_md + "\n\n" + text[t54b_end:] + "\n" + g5_l6_md

# 14. Update L5 upward counterfactuals ("Why Not Higher") so L5 points to L6 rather than saying L5 is the ceiling
text = text.replace(
    "`G0-L5` was the ceiling of the `Gen 0` skill tree; pushing beyond `G0-L5` (`1.5B–11B` models) to general-purpose `175B`-parameter autoregressive foundation models required `\\$4.6M+` supercomputer clusters (`10,000` `V100` GPUs at `OpenAI`) that did not reach commercial API availability until the `Gen 1` transition in `2020-06`.",
    "Climbing from `G0-L5` (`~2,000h | ~$500k` production `ONNX`/`TensorRT` serving and domain seq2seq engineering) to **`G0-L6` (`~10,000h | ~$100M+`)** is overkill unless the team is formulating novel self-attention architectures (`Vaswani et al.`), curating `C4`/`OpenWebText` from raw web crawls, designing `GLUE`/`SuperGLUE` benchmarks, or pretraining `BERT-Large`/`T5-11B`/`GPT-2` from scratch on TPU pods."
)
text = text.replace(
    "`G1-L5` was the ceiling of the `Gen 1` skill tree.",
    "Climbing from `G1-L5` (`~2,000h | ~$500k` multi-GPU `DeepSpeed ZeRO-3` fine-tuning of existing `6B–20B` checkpoints) to **`G1-L6` (`~10,000h | ~$100M+`)** is overkill unless the organization is deriving power-law scaling laws (`Kaplan et al.`), curating `300B–800B` pretraining corpora (`The Pile`), designing `MMLU`/`HumanEval` benchmarks, or pretraining `GPT-3 175B`/`PaLM 540B` from scratch across `10,000` GPUs."
)
text = text.replace(
    "`G2-L5` was the ceiling of the `Gen 2` skill tree.",
    "Climbing from `G2-L5` (`~2,000h | ~$500k` high-throughput `vLLM` `PagedAttention` cluster serving) to **`G2-L6` (`~10,000h | ~$100M+`)** is unnecessary unless the team is deriving `Chinchilla` scaling laws or `DPO` alignment math, curating `2T–15T` token `RedPajama`/`Dolma`/`FineWeb` corpora, designing `MT-Bench`/`SWE-bench`/`GPQA`, or pretraining `GPT-4`/`Claude 3`/`Llama-3` from scratch across `16,000` `H100` GPUs."
)
text = text.replace(
    "`G3-L5` is the ceiling of `Gen 3`.",
    "Climbing from `G3-L5` (`~2,000h | ~$500k` containerized `SWE-bench` repo evaluation farms and `DPO` post-training) to **`G3-L6` (`~10,000h | ~$100M+`)** is unnecessary unless the team is formulating native omni-tokenization, `Ring Attention`, or `RLVR`/`GRPO` math, curating `15T+` multimodal/reasoning corpora, creating `SWE-bench Verified`/`OSWorld`, or pretraining `GPT-4o`/`Claude 3.5 Sonnet`/`Llama-3.1-405B`/`o1`."
)
text = text.replace(
    "`G4-L5` is the empirical ceiling of the AI ladder in October 2026.",
    "Climbing from `G4-L5` (`~2,000h | ~$500k` dedicated `M4 Mac Mini` `OpenClaw` sandboxes, parallel `git worktree` swarms, and domain `GRPO` post-training) to **`G4-L6` (`~10,000h | ~$100M+`)** is required only for frontier research labs formulating pure-RL reasoning (`DeepSeek-R1-Zero`), operating synthetic verifiable data factories, designing `Scale SWE-bench Pro`/`Terminal-Bench 2.0`/`MCP Atlas`, and pretraining `GPT-5.4`/`Claude Opus 5.5` across `25,000–100,000` `Blackwell B200` GPUs."
)
text = text.replace(
    "Apex of the `Gen 5` skill tree (`600–2,000h+` and dedicated sovereign cluster/appliance capital);",
    "Climbing from `G5-L5` (`~2,000h | ~$500k` sovereign local cluster & nightly on-policy `RLVR` flywheels) to **`G5-L6` (`~10,000h | ~$100M+`)** is reserved for exascale research teams designing post-Transformer continual-plasticity architectures, closed-loop wet-lab/world-model simulators, and `Lean 5` formal mathematical proof oracles;"
)

# 15. Replace all legacy min–max hour strings with single-number `<` to `~` brackets across the entire report
replacements = [
    ("0–0h", "0h (0d) | $0"),
    ("0-0h", "0h (0d) | $0"),
    ("`[0, 0]` bracket", "`0h (0d) | $0` bracket"),
    ("min=0h, max=0h", "Beeline = 0h | $0"),
    ("7–45h", "<50h (~1 Wk)"),
    ("7-45h", "<50h (~1 Wk)"),
    ("7–45 hours", "<50h (~1 Wk / Short Course)"),
    ("7 to 45 hours", "<50h (~1 Wk / Short Course)"),
    ("7\\text{ to }45\\text{ hours}", "<50\\text{ hours (~1 Wk)}"),
    ("7\\text{ h} \\le \\text{Hours}_{\\text{learn}} \\le 45\\text{ h}", "\\text{Hours}_{\\text{learn}} < 50\\text{ h}"),
    ("\\in [7, 45]\\text{ h}", "< 50\\text{ h} (\\text{~1 Wk})"),
    ("min=7h, max=45h", "Beeline <50h | <$30"),
    ("7–35h", "<50h (~30h Beeline)"),
    ("7–40h", "<50h (~35h Beeline)"),
    ("7–20h", "<50h (~20h Beeline)"),
    ("7–200h", "<200h (~1 Mo)"),
    ("7–200 hours", "<200h (~1 Mo)"),
    ("7–600h", "~600h (~1 Sem)"),
    ("0–45h", "<50h (~1 Wk)"),
    ("0–15h", "<50h (~15h)"),
    ("50–200h", "<200h (~1 Mo)"),
    ("50-200h", "<200h (~1 Mo)"),
    ("50–200 hours", "<200h (~1 Mo / 1 Uni Subject)"),
    ("50 to 200 hours", "<200h (~1 Mo / 1 Uni Subject)"),
    ("\\in [50, 200]\\text{ h}", "< 200\\text{ h} (\\text{~1 Mo})"),
    ("min=50h, max=200h", "Beeline <200h | <$100"),
    ("50–180h", "<200h (~140h Beeline)"),
    ("50–160h", "<200h (~120h Beeline)"),
    ("50–150", "~120"),
    ("50–600h", "<200h to ~600h"),
    ("50–600 hours", "<200h to ~600h"),
    ("200–600h", "~600h (~1 Sem)"),
    ("200-600h", "~600h (~1 Sem)"),
    ("200–600 hours", "~600h (~1 Qtr / 1 Uni Semester)"),
    ("200 to 600 hours", "~600h (~1 Qtr / 1 Uni Semester)"),
    ("\\in [200, 600]\\text{ h}", "\\approx 600\\text{ h} (\\text{~1 Sem})"),
    ("min=200h, max=600h", "Beeline ~600h | ~$1.5k"),
    ("200–550h", "~600h (~450h Beeline)"),
    ("200–500h", "~600h (~420h Beeline)"),
    ("200–2,000h", "~600h to ~2,000h"),
    ("600–2,000h+", "~2,000h (~1 Yr)"),
    ("600-2,000h+", "~2,000h (~1 Yr)"),
    ("600–2,000h", "~2,000h (~1 Yr)"),
    ("600-2,000h", "~2,000h (~1 Yr)"),
    ("600–2,000+ hours", "~2,000h (~1 Yr / Core Postgrad)"),
    ("600–2,000 hours", "~2,000h (~1 Yr / Core Postgrad)"),
    ("600 to 2,000+ hours", "~2,000h (~1 Yr / Core Postgrad)"),
    ("600 to 2,000 hours", "~2,000h (~1 Yr / Core Postgrad)"),
    ("\\in [600, 2000]\\text{ h}+", "\\approx 2,000\\text{ h} (\\text{~1 Yr})"),
    ("min=600h, max=2000h", "Beeline ~2,000h | ~$500k"),
    ("600–1,800h", "~2,000h (~1,400h Beeline)"),
    ("0–2,000h", "0h to ~10,000h"),
    ("171.4–569.0h", "~600h median"),
]
for old_s, new_s in replacements:
    text = text.replace(old_s, new_s)

# Verify zero forbidden min-max strings remain
forbidden = [
    r"0–0h", r"7–45h", r"50–200h", r"200–600h", r"600–2,000h", r"600-2,000h",
    r"7 to 45 hours", r"50 to 200 hours", r"200 to 600 hours", r"600 to 2,000"
]
for pat in forbidden:
    matches = re.findall(pat, text)
    assert len(matches) == 0, f"Forbidden pattern '{pat}' found {len(matches)} times!"

# Split into stages_v4/part1.md .. part5.md
p2_pos = text.find("## 2. Part II — Literature Review")
p3_pos = text.find("## 3. Part III — Inductive Boundary Method")
p4_pos = text.find("## 4. Part IV — Chronological Ladder Evolution")
p5_pos = text.find("## 5. Part V — Cross-Gen Synthesis")

assert p2_pos > 0 and p3_pos > p2_pos and p4_pos > p3_pos and p5_pos > p4_pos, "Part boundaries not found!"

parts = {
    "part1.md": text[:p2_pos].strip() + "\n",
    "part2.md": text[p2_pos:p3_pos].strip() + "\n",
    "part3.md": text[p3_pos:p4_pos].strip() + "\n",
    "part4.md": text[p4_pos:p5_pos].strip() + "\n",
    "part5.md": text[p5_pos:].strip() + "\n",
}

for fname, content in parts.items():
    with open(os.path.join(STAGES_DIR, fname), "w", encoding="utf-8") as f:
        f.write(content)

report_v4_path = os.path.join(BASE_DIR, "2026 10 17 AI_ladder_evol report v4.md")
with open(report_v4_path, "w", encoding="utf-8") as f:
    f.write(text.strip() + "\n")

print(f"Successfully generated {report_v4_path} ({len(text.splitlines())} lines, {len(text):,} bytes)")
for fname, content in parts.items():
    print(f"  - stages_v4/{fname}: {len(content.splitlines())} lines, {len(content):,} bytes")
print("GATE 6 REPORT CHECK PASSED: 0 forbidden min-max hour range strings in report v4.md!")
