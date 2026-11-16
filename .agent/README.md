# `.agent` Knowledge Base: AI Ladder Evolution, AI Skill Tree 2026 & Anatomy of AI Agents 2026

This `.agent/` directory distills the complete institutional memory, architectural context, lessons learned, design philosophy, and user preferences of **Arian Prabowo** (`www.arianprabowo.com`) accumulated across all conversation histories of the `AI_ladder_evol` project (`a6915702`, `ad3ebaf3`, `0e7e3c65`, `2c55a8c5`).

It is structured according to the **Antigravity Customization System** so that any new machine or fresh agent session cloning this repository automatically inherits all project rules and runbooks without needing access to local chat logs.

---

## 1. Directory Structure Inside `.agent/`

```text
.agent/
├── README.md                                      # Master project overview, repository map & historical context
├── rules/                                         # Always-on workspace rules (auto-loaded by Antigravity)
│   ├── 01-meta-and-repo-hygiene.md                # Meta-learning, design-level fixes, repo hygiene & red-teaming
│   ├── 02-megachart-typography-and-layout.md      # Golden Ratio (H0..H4), 19.5:9 A0/mobile geometry, masthead & cell rules
│   └── 03-writing-style-and-aff-reports.md        # Zero em-dashes, plain English + (jargon), Short/Full names, AFF/RIH
└── skills/                                        # On-demand project runbooks (progressive disclosure)
    ├── anatomy-of-ai-agents-2026/
    │   └── SKILL.md                               # Runbook & 4-zone cell spec for Anatomy of AI Agents 2026
    ├── ai-skill-tree-and-ladder-evol/
    │   └── SKILL.md                               # Runbook & L1-L6 x Gen 0-5 spec for AI Skill Tree & Ladder Evolution
    └── megachart-design-system/
        └── SKILL.md                               # End-to-end engineering & Matplotlib verification guide for Megacharts
```

---

## 2. Project Ecosystem & Repository Map

This repository (`https://github.com/aprbw/AI_ladder_evol.git`) hosts three closely linked visual research deliverables and one spun-out timeline project:

### A. Root Flagship Deliverable: `AI SKILL TREE 2026`
* **Published Root Files (Keep Top-Level Clean)**:
  * `AI_skill_tree_2026.png`: High-resolution desktop self-diagnosis megachart (`Level 1 Everyday Consumer` to `Level 6 Frontier AI Builder` across `4 Pillars` + `Obsolete / Automated-Away Trap`).
  * `AI_skill_tree_2026.pdf`: Searchable vector PDF companion.
  * `README.md` & `LICENSE` (`CC BY 4.0`).
* **Source & Companions in `dev/`**:
  * Generator: `dev/v5_render_plots.py` (`render_current_gen_self_diagnosis_card()`)
  * Mobile portrait version: `dev/figures_v5/fig_v5_current_gen_self_diagnosis_mobile.png`
  * Markdown guide: `dev/2026 11 04 AI_usage_level_keyword_quiz.md`

### B. Longitudinal Matrix & Report: `AI LADDER EVOLUTION (v1 -> v5)`
* **Core Thesis**: AI technology moves so rapidly that any static "AI usage ladder" becomes obsolete within months. `AI Ladder Evolution` maps the co-evolution of **Generations (`Gen 0` to `Gen 5`, X-axis)** against **User Sophistication Levels (`Level 1` at top to `Level 6` at bottom, Y-axis)**, bridged to an empirical bottom timeseries via a row of duration trapezoids and paired with a right-hand marginal histogram of **Users vs. Tokens**.
* **Source & Outputs in `dev/`**:
  * Megaprompt specification: `dev/2026 10 17 AI_ladder_evol mp5.md`
  * Data & validation gates: `dev/v5_data_and_gates.py` -> `dev/cache_v5/*.csv`
  * Plot renderer: `dev/v5_render_plots.py` -> `dev/figures_v5/*.png`
  * Pipeline & report: `dev/v5_ladder_pipeline.py` -> `dev/2026 10 17 AI_ladder_evol report v5.md`

### C. Systems Architecture Megachart: `ANATOMY OF AI AGENTS 2026`
* **Core Thesis**: A `10 Stages (Left -> Right) x 4 Organisms (Top -> Bottom)` architectural blueprint synthesized from Haggai Roitman's *The Hitchhiker's Guide to Agentic AI: From Foundations to Systems* (`arXiv:2606.24937`, v1.4, June 2026) and 2026 production systems tooling.
* **Self-Contained Directory (`dev/anatomy_of_AI_agents_2026/`)**:
  * Generator script: `dev/anatomy_of_AI_agents_2026/plot_agent_anatomy_2026.py`
  * A0 landscape megachart (`46.8 x 21.6 in`, `19.5:9`, 300 DPI): `dev/anatomy_of_AI_agents_2026/anatomy_of_AI_agents_2026.png` & `.pdf`
  * Mobile landscape chart (`26.0 x 12.0 in`, `19.5:9`, 300 DPI): `dev/anatomy_of_AI_agents_2026/anatomy_of_AI_agents_2026_mobile.png`
  * Markdown companion: `dev/anatomy_of_AI_agents_2026/2026 11 07 anatomy_of_AI_agents_2026.md`

### D. Companion Historical Project: `AI 1950-2027 TIMELINE`
* Initial prototype files reside in `dev/2026 11 04 AI_timeline mp.md`, `dev/2026 11 04 AI_timeline report.md`, `dev/figures_timeline/`, and `cache_timeline/`.
* Active development of the 1950-2027 log-time historical chart was spun out into a dedicated sibling repository (`2026 11 04 AI keywords timeline`).

---

## 3. Environment & Execution Quickstart

* **Python Virtual Environment**: Use `.venv/bin/python` at the repository root.
* **Regenerate `ANATOMY OF AI AGENTS 2026`**:
  ```bash
  .venv/bin/python dev/anatomy_of_AI_agents_2026/plot_agent_anatomy_2026.py
  ```
* **Regenerate `AI LADDER EVOLUTION v5` & `AI SKILL TREE 2026`**:
  ```bash
  .venv/bin/python dev/v5_ladder_pipeline.py
  ```
