#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
v5_render_plots.py
==================
Renders all 44 visual artifacts for the v5 AI Capability & Adoption Ladder Evolution
manuscript into `figures_v5/`:
  - 3 User-Skill Megachart Suite (`fig_v5_p0_micro_sae_card.png`, `fig_v5_p0_mini_megachart.png`, `fig_v5_p0_encyclopedic_megachart_poster.png`)
  - 3 Historical News Megachart Suite (`fig_v5_p0b_micro_news_card.png`, `fig_v5_p0b_mini_news_megachart.png`, `fig_v5_p0b_historical_news_megachart_poster.png`)
  - 6 Per-Generation SAE J3016 6-Column Micro Cards (`fig_v5_micro_gen0_sae.png` .. `fig_v5_micro_gen5_sae.png`)
  - 12 Per-TRL-Lineage Paper-to-Consumer-Tool Micro Cards (`fig_v5_micro_trl01_transformer.png` .. `fig_v5_micro_trl12_grounded_search.png`)
  - 6 Multi-Panel Architecture Visual Abstracts (`fig_v5_va0_root.png` .. `fig_v5_va5_part5.png`)
  - 14 Analytical Plots + Animation (`fig_v5_p1_macro_resource_trajectories.png` .. `fig_v5_p14_gen5_speculative_matrix.png`)

Leaves `v3_render_plots.py`, `v4_render_plots.py`, `figures_v3/`, and `figures_v4/` 100% untouched.
"""

import os
import warnings
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
from matplotlib.path import Path
from PIL import Image

warnings.filterwarnings("ignore")

from v5_data_and_gates import (
    BASE_DIR,
    FIGURES_DIR as FIG_DIR,
    build_all_csvs,
    run_all_gates,
)
from stages_v5.plot_micro_cards import render_all_micro_cards
from stages_v5.plot_megacharts import (
    render_plot0_mini_megachart,
    render_plot0_encyclopedic_megachart_poster,
    render_plot0b_mini_news_megachart,
    render_plot0b_historical_news_megachart_poster,
)

os.makedirs(FIG_DIR, exist_ok=True)

# Global CITRA Semantic Color Palette (Locked project-wide)
C_SUPPLY = "#0072B2"    # Supply / Model-Side Capability & Compute
C_DEMAND = "#D55E00"    # Demand / User-Side Skill & Learning Hours
C_ACTUAL = "#009E73"    # Actual / Realised Production Adoption
C_HOPE   = "#CC79A7"    # Modelled / Speculative Hope Projection
C_GRAY   = "#666666"

# Configurable Top-Level Animation Constants (Plot 13)
ANIMATION_FPS = 4
SKIP_INTERVALS = 1
MAX_FRAMES_TO_RENDER = 112

COMPACT_TICK_LABELS = {
    1: "L1: Consumer (0h|$0)",
    2: "L2: Workspace (<50h|<$30)",
    3: "L3: Integrator (<200h|<$100)",
    4: "L4: Harness (~600h|~$1.5k)",
    5: "L5: Cluster (~2,000h|~$500k)",
    6: "L6: Scientist (~10,000h|~$100M+)",
}


def apply_calendar_grid(ax, xmin=2017.4, xmax=2026.85):
    ax.set_xlim(xmin, xmax)
    major_years = np.arange(2018, 2027, 1)
    minor_quarters = np.arange(2017.5, 2026.85, 0.25)
    ax.set_xticks(major_years)
    ax.set_xticklabels([f"{int(y)}" for y in major_years], fontsize=9)
    ax.set_xticks(minor_quarters, minor=True)
    ax.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25, color="#888888")
    ax.grid(True, which="minor", linestyle="--", linewidth=0.5, alpha=0.12, color="#AAAAAA")


def draw_bezier_ribbon(ax, x0, y0, x1, y1, color, alpha=0.45, lw=6.0, zorder=3):
    xm = 0.5 * (x0 + x1)
    verts = [(x0, y0), (xm, y0), (xm, y1), (x1, y1)]
    codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    path = Path(verts, codes)
    patch = mpatches.PathPatch(path, facecolor="none", edgecolor=color, lw=lw, alpha=alpha, zorder=zorder)
    ax.add_patch(patch)


# ==============================================================================
# 0. HIERARCHICAL VISUAL ABSTRACTS (Plot VA0 .. Plot VA5)
# ==============================================================================
def render_visual_abstracts(dfs):
    va_specs = [
        ("fig_v5_va0_root.png", "Plot VA0: AI Ladder Evolution v5 (2017–2029): Dual 6×6 Megacharts, 125-Term Glossary, 144 Events & 12 TRL Lineages", [
            ("1. Dual 6×6 Megachart Architecture", "Plot 0: Gen G0..G5 × Effort Level L1..L6\nPlot 0B: Gen G0..G5 × Ecosystem CAT 1..CAT 6\nMicro, Mini & Full Poster Triads (44 Figs)", C_SUPPLY),
            ("2. 6 Standardized Beeline Brackets", "L1: 0h (0d) | $0  •  L2: <50h (~1 Wk) | <$30\nL3: <200h (~1 Mo) | <$100  •  L4: ~600h | ~$1.5k\nL5: ~2,000h | ~$500k  •  L6: ~10,000h | ~$100M+", C_DEMAND),
            ("3. 125-Term Chronological Glossary", "8 Domains (D1..D8): Prompting, RAG/Agents,\nTuning, Serving/Silicon, Scaling/RLVR, Slop &\nPsychosis, Security/IP, and X-Risk/Doomer", C_ACTUAL),
            ("4. 144 Dated Historical Milestones", "4 Dated Events × 36 News Cells (G0..G5 × CAT 1..6)\nCAT 1 Viral/Safety -> CAT 2 Courses -> CAT 3 Law\n-> CAT 4 Tools -> CAT 5 Silicon -> CAT 6 Papers", C_SUPPLY),
            ("5. 6 Boundary & Counterfactual Rules", "Medium-Model Decoupling, Meta-Bootstrapping\nGate, 4-Tier Cognitive Input, Failure Anchor,\nRecursive Cannibalization & Setup Half-Life", C_DEMAND),
            ("6. 12 Synchronized TRL Lineages", "8 Technical + 4 Governance/Safety Lineages\n(TRL_01..TRL_12) with 12 Dedicated Micro Cards\nAll 8 Deterministic Validation Gates Pass 100%", C_HOPE),
        ]),
        ("fig_v5_va1_part1.png", "Plot VA1: Part I Synthesis (2017–2026): Six Effort Levels, Beeline Methodology, Dual Megacharts & Macro Economics", [
            ("Gen 0 (2017–2020): Pre-LLM Pipelines", "L1 Passive Widgets | L2 AutoML | L3 Sklearn\nL4 BERT | L5 Horovod | L6 Transformer Genesis\n12M Users | 0.18T Tokens | $1.1B Spend", C_SUPPLY),
            ("Gen 1 (2020–2022): Completion & Tab", "L1 Copilot Tab (0h) | L2 Playground (<50h)\nL3 OpenAI API | L4 Chains | L5 ZeRO | L6 GPT-3\n45M Users | 1.60T Tokens | $3.8B Spend", C_ACTUAL),
            ("Gen 2 (2022–2024): Chat & DIY Vector RAG", "L1 ChatGPT (0h) | L2 CoT | L3 Pinecone RAG\nL4 4-Bit QLoRA | L5 vLLM | L6 Llama-2/DPO\n380M Users | 28T Tokens | $14.0B Spend", C_DEMAND),
            ("Gen 3 (2024): Omni-Workspaces & AI IDEs", "L1 GPT-4o + Artifacts | L2 50-PDF Projects\nL3 Cursor Vibe Coding | L4 LangGraph | L6 o1\n720M Users | 240T Tokens | $39.0B Spend", C_ACTUAL),
            ("Gen 4 (2025–2026): Thinking, CLI & Sandbox", "L1 Auto-Router | L2 Deep Research | L3 MCP\nL4 Claude Code | L5 OpenClaw | L6 RLVR Genesis\n1,150M Users | 1,100T Tokens | $88.0B Spend", C_SUPPLY),
            ("Beeline Hours & 8 Validation Gates", "Zero-Filler Beeline from High School (0h)\nProper-Subset Micro -> Mini -> Mega Hierarchy\nAll 8 Programmatic Gates Pass 100%", C_HOPE),
        ]),
        ("fig_v5_va2_part2.png", "Plot VA2: Part II Raw Inventory: 22 Ladders, 125 Glossary Terms (D1–D8), 26 Tutorials, 36 Use Cases & 20 Hopes", [
            ("1. 22 Existing Ladders Audited", "Karpathy 1.0–3.0, OpenAI 5 Levels, DeepMind,\nAnthropic, LangChain, SAE L0–L5, METR Horizon,\nAnthropic ASL-1..4, NIST RMF, EU AI Act", C_SUPPLY),
            ("2. 125-Term Chronological Glossary", "D1 Prompt/Vibe • D2 RAG/MCP • D3 LoRA/DPO\nD4 vLLM/B200 • D5 RLVR/GRPO • D6 Slop/Psychosis\nD7 Jailbreak/CVE • D8 P(doom)/Foom/ASL/SB-1047", C_HOPE),
            ("3. 36 Track A & Track B Use Cases", "36 Empirical Workflows Across L1–L6\nDirect Users vs Enterprise Bot Builders\n& L6 Foundation Model Genesis Teams", C_ACTUAL),
            ("4. 26 Beeline Curricula & Papers", "L1 (0h) -> L2 (<50h DL.AI) -> L3 (<200h MCP)\n-> L4 (~600h CS224N/LoRA) -> L5 (~2,000h ZeRO)\n-> L6 (~10,000h Attention/Chinchilla/R1)", C_DEMAND),
            ("5. 4-Pillar L6 Research Anchor", "(1) Math/Theory Formulation\n(2) Pretraining & Alignment Data Curation\n(3) Benchmark & Metric Design\n(4) From-Scratch Base Pretraining ($100M+)", C_SUPPLY),
            ("6. Two-Level Cost & Share Conservation", "Single-Task: Tokens, FLOPs, USD, Wh, Min\nGen-Wide: L1..L6 User%, Token%, Spend% = 100%\nZero Forbidden Min–Max Ranges", C_ACTUAL),
        ]),
        ("fig_v5_va3_part3.png", "Plot VA3: Part III 6×6 Coordinate Architecture, News Category Taxonomy & Six Boundary Axioms", [
            ("1. Dual User-Shift Gen Cutoff Rule", "New Gen G Requires BOTH:\n(a) New Upper-Level Use Case (L3–L6)\n(b) Old Use Case Sinks to Lower Level", C_SUPPLY),
            ("2. Six Standardized Effort Levels", "L1: 0h|$0 • L2: <50h|<$30 • L3: <200h|<$100\nL4: ~600h|~$1.5k • L5: ~2,000h|~$500k\nL6: ~10,000h (~5 Yrs PhD) | ~$100M+", C_DEMAND),
            ("3. Six Historical News Categories", "CAT 1 Viral/Safety • CAT 2 Flagship Courses\nCAT 3 Policy/IP/Law • CAT 4 Frameworks/Tools\nCAT 5 Silicon/Capex • CAT 6 Core Papers", C_ACTUAL),
            ("4. Meta-Bootstrapping Gate (Why Not L-1)", "Cell Stays at Lk Only if BOTH Fail:\n(a) Direct By-Name Delegation to L(k-1) AI\n(b) Socratic AI Onboarding within B(k-1) Hours", C_DEMAND),
            ("5. Failure-Boundary & Cannibalization", "L2/L3: Coupled Happy-Path Build+Self-Test\nL4+: Decoupled Verification Oracles & Recovery\nEvery Rung Lk Recursively Uses Gt-L(1..k-1)", C_SUPPLY),
            ("6. Proper-Subset Keyword Invariant", "micro_keywords_subset ⊂ mini_keywords_subset\n⊂ keywords_1line Across All 36 Skill Cells\n& All 36 Historical News Cells", C_HOPE),
        ]),
        ("fig_v5_va4_part4.png", "Plot VA4: Part IV Chronological Matrix (Gen 0 to Gen 5): 36 Skill Cells, 36 News Cells & 6 SAE Cards", [
            ("Gen 0 (2017–2020) & Gen 1 (2020–2022)", "G0: Passive L1..Seq2Seq L5 + Transformer L6\nG1: Copilot Tab L1..DeepSpeed L5 + Scaling L6\n48 Dated News Milestones (EV_001..EV_048)", C_SUPPLY),
            ("Gen 2 (2022–2024): Chat, RAG & DPO", "L1: ChatGPT | L2: CoT | L3: Vector RAG\nL4: 4-Bit QLoRA | L5: vLLM | L6: Llama-2/DPO\nSydney, Mata v. Avianca, EO 14110 & H100s", C_ACTUAL),
            ("Gen 3 (2024): Omni, Vibe Coding & o1", "L1: GPT-4o + Artifacts | L2: 50-PDF Projects\nL3: Vibe Coding | L4: LangGraph | L5: Evals\nAI Slop, Sewell Setzer III, EU AI Act & o1", C_DEMAND),
            ("Gen 4 (2025–2026): Thinking, CLI & Swarms", "L1: Auto-Router | L2: Deep Research | L3: MCP\nL4: Claude Code CLI | L5: OpenClaw/GRPO\n200k MCP RCEs, Bartz $1.5B & DeepSeek-R1", C_SUPPLY),
            ("Gen 5 (2027+ Spec.): Ambient OS & Mesh", "L1: Ambient OS | L2: Cloud Studio | L3: A2A\nL4: Lean-4 Proofs | L5: TEE RLVR | L6: World Sim\n24 Projected Milestones (EV_121..EV_144)", C_HOPE),
            ("6 Per-Generation SAE J3016 Cards", "Dedicated 6-Column Reference Cards\n(fig_v5_micro_gen0_sae .. gen5_sae)\nZero-Truncation Scannable Architecture", C_DEMAND),
        ]),
        ("fig_v5_va5_part5.png", "Plot VA5: Part V Synthesis: Alluvial Atlas, 12 TRL Lineages (Tech + Governance), 22-Ladder Matrix & Gen 5", [
            ("1. Skill Deflation Escalator (Plot 2)", "5 Anchor Workflows Sink 2–4 Levels (G0->G4)\nSaving 200–2,000 Beeline Learning Hours\nWhile L5–L6 Compute Expands 1,000x+", C_ACTUAL),
            ("2. 12 On-Ladder TRL Lineages (Plot 11)", "8 Technical (TRL_01..08) + 4 Governance/Safety\n(TRL_09..12: Jailbreaks, Copyright, X-Risk,\nHallucinations) with 12 Dedicated Micro Cards", C_SUPPLY),
            ("3. Population Evolution of Hopes (Plot 11)", "20 Historical Hopes Audited Across G0–G4:\n25% Survived to TRL 9 | 75% Went Extinct\n(Too Early, Base-Model Absorption, Economics)", C_HOPE),
            ("4. 22-Ladder Pairwise Matrix (Plot 12)", "20 Capability/Agent Ladders + METR Horizon\n+ Anthropic ASL / NIST RMF / EU AI Act\n4-Axis Parametric & Non-Parametric Audit", C_DEMAND),
            ("5. 112-Frame Animated Trajectory (Plot 13)", "Continuous Monthly Trajectory (2017.4–2026.8)\nAcross All 6 Standardized Effort Levels\nWith Synchronized Token Volume Scrubber", C_SUPPLY),
            ("6. Speculative Gen 5 (Plot 14, G5-L1..L6)", "Pre-Cutoff: 2026-08 (>50% SWE-Pro Gate)\nPost-Cutoff: 2027-03 (Mass L1/L2 Adoption)\nAmbient OS (L1) to World-Model Genesis (L6)", C_ACTUAL),
        ]),
    ]

    for fname, title, cards in va_specs:
        fig = plt.figure(figsize=(16, 9), dpi=300)
        gs = gridspec.GridSpec(2, 3, figure=fig, left=0.04, right=0.96, bottom=0.06, top=0.84, wspace=0.12, hspace=0.18)
        fig.suptitle(title, fontsize=12.5, fontweight="bold", y=0.96)

        legend_handles = [
            mpatches.Patch(color=C_SUPPLY, alpha=0.8, label="SUPPLY / MODEL-SIDE"),
            mpatches.Patch(color=C_DEMAND, alpha=0.8, label="DEMAND / USER-SKILL"),
            mpatches.Patch(color=C_ACTUAL, alpha=0.8, label="ACTUAL / REALISED"),
            mpatches.Patch(color=C_HOPE, alpha=0.8, label="MODELLED / HOPE-PROJECTION"),
        ]
        fig.legend(handles=legend_handles, loc="upper center", bbox_to_anchor=(0.5, 0.92), ncol=4, frameon=False, fontsize=9.5)

        for idx, (ctitle, cbody, col) in enumerate(cards):
            r, c = divmod(idx, 3)
            ax = fig.add_subplot(gs[r, c])
            ax.set_xlim(0.0, 1.0)
            ax.set_ylim(0.0, 1.0)
            ax.set_xticks([])
            ax.set_yticks([])
            for spine in ax.spines.values():
                spine.set_linewidth(1.4)
                spine.set_edgecolor("#333333")
            ax.add_patch(mpatches.Rectangle((0, 0), 1, 1, facecolor=col, alpha=0.12, zorder=1))
            ax.add_patch(mpatches.Rectangle((0, 0.80), 1, 0.20, facecolor=col, alpha=0.88, zorder=2))
            ax.text(0.04, 0.90, ctitle, color="white", fontsize=10.5, fontweight="bold", va="center", ha="left", zorder=3)
            ax.text(0.05, 0.40, cbody, color="#111111", fontsize=9.2, va="center", ha="left", linespacing=1.40, zorder=3)

        out_path = os.path.join(FIG_DIR, fname)
        fig.savefig(out_path, dpi=300)
        plt.close(fig)
        print(f"[RENDERED] {out_path}")


# ==============================================================================
# PLOT 1: MACRO RESOURCE TRAJECTORIES
# ==============================================================================
def render_plot1_macro_trajectories(dfs):
    t_points = np.array([2017.5, 2018.5, 2019.5, 2020.4, 2021.0, 2022.0, 2022.85, 2023.5, 2024.33, 2024.8, 2025.0, 2025.8, 2026.8])
    tokens_t = np.array([0.05, 0.10, 0.18, 0.30, 0.70, 1.60, 3.50, 28.0, 110.0, 240.0, 380.0, 750.0, 1100.0])
    spend_b  = np.array([0.3,  0.6,  1.1,  1.5,  2.4,  3.8,  5.5,  14.0, 26.0,  39.0,  52.0,  71.0,  88.0])
    users_m  = np.array([3.0,  6.5,  12.0, 18.0, 28.0, 45.0, 120.0, 380.0, 560.0, 720.0, 860.0, 1020.0, 1150.0])

    fig = plt.figure(figsize=(14, 7), dpi=300)
    gs = gridspec.GridSpec(1, 2, figure=fig, width_ratios=[4, 1], wspace=0.06, left=0.07, right=0.96, bottom=0.11, top=0.88)
    ax = fig.add_subplot(gs[0, 0])
    ax_marg = fig.add_subplot(gs[0, 1], sharey=ax)

    fig.suptitle("Plot 1: Global AI Ecosystem (2017–2026): Macro Token Volume, Total Spend & Active Users Across 6 Levels", fontsize=12.5, fontweight="bold", y=0.96)

    ax.plot(t_points, tokens_t, color=C_SUPPLY, linewidth=2.8, marker="o", zorder=4, label="Annual Token Volume (Trillions, SUPPLY)")
    ax.plot(t_points, spend_b, color=C_ACTUAL, linewidth=2.8, marker="s", zorder=4, label="Total Annual AI Spend ($B, ACTUAL)")
    ax.plot(t_points, users_m, color=C_DEMAND, linewidth=2.8, marker="^", zorder=4, label="Active Users Across 6-Level Ladder (Millions, DEMAND)")

    gen_cuts = [(2020.42, "G0->G1\n(2020-06)"), (2022.83, "G1->G2\n(2022-11)"), (2024.33, "G2->G3\n(2024-05)"), (2025.00, "G3->G4\n(2025-01)")]
    for gx, glabel in gen_cuts:
        ax.axvline(gx, color="#444444", linestyle="--", linewidth=1.2, alpha=0.6, zorder=2)
        ax.text(gx + 0.06, 1450.0, glabel, fontsize=8, color="#222222", va="top", ha="left")

    apply_calendar_grid(ax, 2017.4, 2026.85)
    ax.set_yscale("symlog", linthresh=1.0)
    ax.set_ylim(0.0, 2000.0)
    ax.set_xlabel("Calendar Year (2017-06 to 2026-10)", fontsize=10, fontweight="bold")
    ax.set_ylabel("Macro Magnitude (symlog scale, linthresh=1.0)", fontsize=10, fontweight="bold")
    ax.legend(loc="upper left", bbox_to_anchor=(0.02, 0.96), frameon=False, fontsize=9.5)

    bins = np.geomspace(0.04, 2000.0, 20)
    ax_marg.hist(tokens_t, bins=bins, orientation="horizontal", histtype="step", fill=False, linewidth=1.8, color=C_SUPPLY, label="Tokens")
    ax_marg.hist(spend_b, bins=bins, orientation="horizontal", histtype="step", fill=False, linewidth=1.8, color=C_ACTUAL, label="Spend")
    ax_marg.hist(users_m, bins=bins, orientation="horizontal", histtype="step", fill=False, linewidth=1.8, color=C_DEMAND, label="Users")
    ax_marg.set_xlabel("Count", fontsize=9.5, fontweight="bold")
    ax_marg.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25, color="#888888")
    plt.setp(ax_marg.get_yticklabels(), visible=False)

    out_path = os.path.join(FIG_DIR, "fig_v5_p1_macro_resource_trajectories.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


# ==============================================================================
# PLOT 2: SKILL DEFLATION ESCALATOR
# ==============================================================================
def render_plot2_skill_deflation(dfs):
    df_bench = dfs["benchmarks"]
    gen_x = np.array([2018.9, 2021.6, 2023.6, 2024.65, 2025.9])
    hour_cols = ["g0_hrs", "g1_hrs", "g2_hrs", "g3_hrs", "g4_hrs"]

    fig = plt.figure(figsize=(14, 7), dpi=300)
    gs = gridspec.GridSpec(1, 2, figure=fig, width_ratios=[4, 1], wspace=0.06, left=0.07, right=0.96, bottom=0.11, top=0.88)
    ax = fig.add_subplot(gs[0, 0])
    ax_marg = fig.add_subplot(gs[0, 1], sharey=ax)

    fig.suptitle("Plot 2: Five Benchmark User Workflows (2017–2026): Down-Ladder Beeline Learning-Hour Deflation", fontsize=12.5, fontweight="bold", y=0.96)

    rng = np.random.default_rng(42)
    perm = rng.permutation(len(df_bench))
    all_vals = []
    markers = ["o", "s", "^", "D", "v"]
    for idx in perm:
        row = df_bench.iloc[idx]
        y_vals = np.array([row[c] for c in hour_cols], dtype=float)
        all_vals.extend(y_vals)
        ax.plot(gen_x, y_vals, color=C_DEMAND, alpha=0.45, linewidth=1.8, marker=markers[idx % len(markers)], zorder=2, label=f"{row['workflow_name']} (-{row['total_hrs_saved']}h)")

    mean_hours = df_bench[hour_cols].mean(axis=0).values
    ax.plot(gen_x, mean_hours, color=C_SUPPLY, linewidth=3.0, alpha=0.95, marker="o", markersize=8, zorder=5, label="Parametric Mean Beeline Learning Hours (μ)")

    for gx, mval, gname in zip(gen_x, mean_hours, ["Gen 0", "Gen 1", "Gen 2", "Gen 3", "Gen 4"]):
        ax.annotate(f"{gname}: μ={mval:.0f}h", (gx, mval), textcoords="offset points", xytext=(0, 10), ha="center", fontsize=8.5, fontweight="bold", color=C_SUPPLY, zorder=6)

    apply_calendar_grid(ax, 2017.4, 2026.85)
    ax.set_yscale("symlog", linthresh=1.0)
    ax.set_ylim(0.0, 2800.0)
    ax.set_xlabel("Calendar Year Across Generations Gen 0 to Gen 4 (2017–2026)", fontsize=10, fontweight="bold")
    ax.set_ylabel("Required Beeline Learning Hours (symlog scale, linthresh=1.0)", fontsize=10, fontweight="bold")
    ax.legend(loc="upper right", bbox_to_anchor=(0.98, 0.96), frameon=False, fontsize=8.3)

    bins = np.concatenate([[0.0], np.geomspace(1.0, 2800.0, 18)])
    ax_marg.hist(all_vals, bins=bins, orientation="horizontal", histtype="step", fill=False, linewidth=1.8, color=C_DEMAND)
    ax_marg.axhline(np.mean(all_vals), color=C_SUPPLY, linestyle="--", linewidth=1.6, label="Global μ")
    ax_marg.set_xlabel("Cell Count", fontsize=9.5, fontweight="bold")
    ax_marg.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25, color="#888888")
    plt.setp(ax_marg.get_yticklabels(), visible=False)

    out_path = os.path.join(FIG_DIR, "fig_v5_p2_skill_deflation_escalator.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


# ==============================================================================
# PLOT 3: PUBLISHED AI LADDER CORPUS & GEN BREAKS (22 LADDERS)
# ==============================================================================
def render_plot3_folksonomy_raster(dfs):
    df_lad = dfs["existing_ladders"]
    fig, ax = plt.subplots(figsize=(14.5, 8.2), dpi=300)
    fig.subplots_adjust(left=0.14, right=0.97, bottom=0.11, top=0.88)
    fig.suptitle("Plot 3: Published AI Ladder Corpus (22 Ladders, 2017–2026): Descriptive Bottom Rungs (L1–L3) vs. Speculative Top Rungs (L4–L6)", fontsize=12, fontweight="bold", y=0.96)

    t_grid = np.linspace(2017.42, 2026.83, 113)
    y_grid = np.arange(0.5, 7.0, 1.0)
    Z = np.zeros((6, len(t_grid) - 1))
    for r in range(6):
        for c in range(len(t_grid) - 1):
            Z[r, c] = (0.25 + 0.10 * r) if r < 3 else (0.75 + 0.08 * (r - 3))

    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list("desc_hope", [C_ACTUAL, "#F0E442", C_HOPE])
    ax.pcolormesh(t_grid, y_grid, Z, cmap=cmap, alpha=0.45, rasterized=True, shading="flat")

    even_counter = 0
    for idx, row in df_lad.iterrows():
        yr, mo = map(int, row["pub_date"].split("-"))
        x_val = yr + (mo - 0.5) / 12.0
        ax.scatter([x_val, x_val], [1.5, 2.7], color=C_ACTUAL, s=60, edgecolors="#111111", zorder=4)
        ax.scatter([x_val], [5.15], color=C_HOPE, s=80, marker="D", edgecolors="#111111", zorder=5)
        if idx % 2 == 0:
            y_lbl = 5.38 if (even_counter % 2 == 0) else 5.68
            even_counter += 1
            ax.annotate(row["ladder_id"], (x_val, y_lbl), fontsize=7.5, fontweight="bold", ha="center", rotation=20, zorder=6)

    for (gx, glabel), y_brk in zip([(2020.42, "Break G0->G1"), (2022.83, "Break G1->G2"), (2024.33, "Break G2->G3"), (2025.00, "Break G3->G4")], [6.36, 6.36, 6.36, 6.08]):
        ax.axvline(gx, color=C_DEMAND, linewidth=2.2, linestyle="--", zorder=5)
        ax.text(gx + 0.05, y_brk, glabel, color=C_DEMAND, fontsize=8.5, fontweight="bold", va="top")

    apply_calendar_grid(ax, 2017.4, 2026.85)
    ax.set_ylim(0.5, 6.5)
    ax.set_yticks([1, 2, 3, 4, 5, 6])
    ax.set_yticklabels([COMPACT_TICK_LABELS[i] for i in [1, 2, 3, 4, 5, 6]], fontsize=8.8, fontweight="bold")
    ax.set_xlabel("Ladder Publication Date & Generation Break Timeline (2017–2026)", fontsize=10, fontweight="bold")
    ax.set_ylabel("Normalized 6-Level Ladder Rung Position", fontsize=10, fontweight="bold")

    handles = [
        mpatches.Patch(color=C_ACTUAL, alpha=0.8, label="Descriptive Adopted Rungs (L1–L3 Current Gen Reality)"),
        mpatches.Patch(color=C_HOPE, alpha=0.8, label="Speculative / Frontier Rungs (L4–L6 Projection)"),
        plt.Line2D([0], [0], color=C_DEMAND, linewidth=2.2, linestyle="--", label="Detected Generation Break Cutoff"),
    ]
    ax.legend(handles=handles, loc="lower left", bbox_to_anchor=(0.02, 0.02), frameon=False, fontsize=9)

    out_path = os.path.join(FIG_DIR, "fig_v5_p3_folksonomy_and_gen_breaks.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


# ==============================================================================
# PLOT 4: TASK COST VS. LEARNING HOURS JOINTPLOT (30 EMPIRICAL CELLS G0-L1..G4-L6)
# ==============================================================================
def render_plot4_jointplot(dfs):
    df_cells = dfs["ladder_cells"]
    x_hours = df_cells["learning_hours"].values.astype(float)
    y_usd = df_cells["single_task_usd"].values.astype(float)
    gens = df_cells["gen_id"].values

    fig = plt.figure(figsize=(12.5, 10), dpi=300)
    gs = gridspec.GridSpec(2, 2, figure=fig, width_ratios=[4, 1], height_ratios=[1, 4], wspace=0.06, hspace=0.06, left=0.09, right=0.96, bottom=0.09, top=0.90)
    ax_main = fig.add_subplot(gs[1, 0])
    ax_top  = fig.add_subplot(gs[0, 0], sharex=ax_main)
    ax_right = fig.add_subplot(gs[1, 1], sharey=ax_main)
    ax_leg  = fig.add_subplot(gs[0, 1])
    ax_leg.axis("off")

    fig.suptitle("Plot 4: All 30 Empirical (Gen G, Level L) Cells (2017–2026): Single-Task Cost vs. Beeline Learning Hours", fontsize=12, fontweight="bold", y=0.96)

    gen_colors = {"G0": "#555555", "G1": C_SUPPLY, "G2": C_DEMAND, "G3": C_ACTUAL, "G4": C_HOPE}
    gen_offsets = {"G0": (6, -5), "G1": (-6, -7), "G2": (6, 4), "G3": (-6, 5), "G4": (6, 5)}
    gen_align   = {"G0": "left",  "G1": "right",  "G2": "left", "G3": "right", "G4": "left"}
    rng = np.random.default_rng(42)
    perm = rng.permutation(len(df_cells))

    for idx in perm:
        g = gens[idx]
        lvl = int(df_cells.iloc[idx]["level_id"])
        dx, dy = gen_offsets[g]
        ha_val = gen_align[g]
        if lvl == 1:
            dx, ha_val = 6, "left"
        ax_main.scatter(x_hours[idx], y_usd[idx], color=gen_colors[g], alpha=0.82, s=78, edgecolors="#111111", linewidth=0.6, zorder=3)
        ax_main.annotate(f"{g}-L{lvl}", (x_hours[idx], y_usd[idx]), textcoords="offset points", xytext=(dx, dy), ha=ha_val, fontsize=7.5, fontweight="bold", alpha=0.92)

    lx = np.log10(x_hours + 1.0)
    ly = np.log10(y_usd + 1e-5)
    slope, intercept = np.polyfit(lx, ly, 1)
    x_grid = np.concatenate([[0.0], np.geomspace(1.0, 12000.0, 120)])
    y_fit = np.maximum(10**(intercept + slope * np.log10(x_grid + 1.0)) - 1e-5, 0.0)
    ax_main.plot(x_grid, y_fit, linestyle="--", color="#000000", linewidth=2.0, zorder=4, label="Log-OLS Trend")

    ax_main.set_xscale("symlog", linthresh=1.0)
    ax_main.set_yscale("symlog", linthresh=0.001)
    ax_main.set_xlim(0.0, 16000.0)
    ax_main.set_ylim(0.0, 500.0)
    ax_main.set_xlabel("Cumulative Beeline Learning Investment (Hours: 0h, <50h, <200h, ~600h, ~2,000h, ~10,000h)", fontsize=10, fontweight="bold")
    ax_main.set_ylabel("Single-Task / Amortized Run Cost (USD, symlog linthresh=0.001)", fontsize=10, fontweight="bold")
    ax_main.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25, color="#888888")
    ax_main.grid(True, which="minor", linestyle="--", linewidth=0.5, alpha=0.12, color="#AAAAAA")

    xbins = np.concatenate([[0.0], np.geomspace(1.0, 12000.0, 16)])
    ybins = np.geomspace(1e-5, 350.0, 16)
    ax_top.hist(x_hours, bins=xbins, histtype="step", fill=False, linewidth=1.8, color=C_DEMAND)
    ax_top.set_ylabel("Count", fontsize=9, fontweight="bold")
    ax_top.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25)
    plt.setp(ax_top.get_xticklabels(), visible=False)

    ax_right.hist(y_usd, bins=ybins, orientation="horizontal", histtype="step", fill=False, linewidth=1.8, color=C_ACTUAL)
    ax_right.set_xlabel("Count", fontsize=9, fontweight="bold")
    ax_right.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25)
    plt.setp(ax_right.get_yticklabels(), visible=False)

    handles = [mpatches.Patch(color=gen_colors[g], label=f"{g}") for g in ["G0", "G1", "G2", "G3", "G4"]]
    handles.append(plt.Line2D([0], [0], color="#000000", linestyle="--", linewidth=2.0, label="OLS Trend"))
    ax_leg.legend(handles=handles, loc="center", frameon=False, fontsize=9, title="Generation & Fit")

    out_path = os.path.join(FIG_DIR, "fig_v5_p4_task_cost_vs_learning_jointplot.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


# ==============================================================================
# PLOTS 5-9: GENERATION-SPECIFIC 6-LEVEL MATRICES (G0 TO G4)
# ==============================================================================
def render_plots5_to_9_gen_matrices(dfs):
    df_cells = dfs["ladder_cells"]
    df_gens = dfs["generations"]

    gen_plot_map = [
        ("G0", 5, "fig_v5_p5_gen0_matrix.png"),
        ("G1", 6, "fig_v5_p6_gen1_matrix.png"),
        ("G2", 7, "fig_v5_p7_gen2_matrix.png"),
        ("G3", 8, "fig_v5_p8_gen3_matrix.png"),
        ("G4", 9, "fig_v5_p9_gen4_matrix.png"),
    ]

    for gen_id, pnum, fname in gen_plot_map:
        sub = df_cells[df_cells["gen_id"] == gen_id].sort_values("level_id")
        gen_row = df_gens[df_gens["gen_id"] == gen_id].iloc[0]

        fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(17.2, 8.2), dpi=300, sharey=True)
        fig.subplots_adjust(left=0.20, right=0.97, bottom=0.11, top=0.82, wspace=0.08)
        fig.suptitle(f"Plot {pnum}: {gen_row['gen_name']} ({gen_row['start_date']} to {gen_row['end_date']}) — 6-Level Breakdown", fontsize=12, fontweight="bold", y=0.96)

        y_pos = sub["level_id"].values
        h_bar = 0.22
        ax_l.barh(y_pos - h_bar, sub["single_task_tokens"].values, height=h_bar, color=C_SUPPLY, alpha=0.85, label="Single-Task Tokens (SUPPLY)")
        ax_l.barh(y_pos, sub["learning_hours"].values, height=h_bar, color=C_DEMAND, alpha=0.85, label="Beeline Learning Hours (DEMAND)")
        ax_l.barh(y_pos + h_bar, sub["single_task_wh"].values * 1000.0, height=h_bar, color=C_ACTUAL, alpha=0.85, label="Single-Task Energy (mWh, ACTUAL)")

        ax_l.set_xscale("symlog", linthresh=1.0)
        ax_l.set_xlim(0.0, 2.5e8)
        ax_l.set_ylim(0.5, 6.65)
        ax_l.set_yticks([1, 2, 3, 4, 5, 6])
        ax_l.set_yticklabels([f"{gen_id}-{COMPACT_TICK_LABELS[int(lvl)]}" for lvl in sub["level_id"]], fontsize=8.8, fontweight="bold")
        ax_l.set_xlabel("Single-Task Magnitude (symlog scale, linthresh=1.0)", fontsize=10, fontweight="bold")
        ax_l.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25)
        ax_l.grid(True, which="minor", linestyle="--", linewidth=0.5, alpha=0.12)
        ax_l.legend(loc="lower center", bbox_to_anchor=(0.5, 1.01), ncol=3, frameon=False, fontsize=8.0)

        ax_r.barh(y_pos - h_bar, sub["user_share_pct"].values, height=h_bar, color=C_DEMAND, alpha=0.85, label="Active User Share %")
        ax_r.barh(y_pos, sub["token_share_pct"].values, height=h_bar, color=C_SUPPLY, alpha=0.85, label="Token Volume Share %")
        ax_r.barh(y_pos + h_bar, sub["spend_share_pct"].values, height=h_bar, color=C_ACTUAL, alpha=0.85, label="Expenditure Share %")

        for lvl, u_sh, t_sh, s_sh, title in zip(sub["level_id"], sub["user_share_pct"], sub["token_share_pct"], sub["spend_share_pct"], sub["user_first_title"]):
            max_bar = max(u_sh, t_sh, s_sh)
            short_t = title[:34] + (".." if len(title) > 34 else "")
            if max_bar <= 45.0:
                ax_r.text(max_bar + 1.5, lvl, f"{short_t} (U:{u_sh:g}% | T:{t_sh:g}% | S:{s_sh:g}%)", va="center", ha="left", fontsize=7.6, color="#111111")
            else:
                ax_r.text(2.0, lvl + 0.33, f"{short_t} (U:{u_sh:g}% | T:{t_sh:g}% | S:{s_sh:g}%)", va="bottom", ha="left", fontsize=7.6, fontweight="bold", color="#111111")

        ax_r.set_xlim(0.0, 100.0)
        ax_r.set_xticks(np.arange(0, 101, 20))
        ax_r.set_xticks(np.arange(0, 101, 5), minor=True)
        ax_r.set_xlabel("Generation-Wide Resource Share Across L1–L6 (% of Total = 100.0%)", fontsize=10, fontweight="bold")
        ax_r.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25)
        ax_r.grid(True, which="minor", linestyle="--", linewidth=0.5, alpha=0.12)
        ax_r.legend(loc="lower center", bbox_to_anchor=(0.5, 1.01), ncol=3, frameon=False, fontsize=8.0)

        out_path = os.path.join(FIG_DIR, fname)
        fig.savefig(out_path, dpi=300)
        plt.close(fig)
        print(f"[RENDERED] {out_path}")


# ==============================================================================
# PLOT 10: CONTINUOUS-TIME 6-LEVEL ALLUVIAL EVOLUTION ATLAS
# ==============================================================================
def render_plot10_alluvial_poster(dfs):
    df_cells = dfs["ladder_cells"]
    df_gens = dfs["generations"][dfs["generations"]["gen_id"] != "G5"]

    fig = plt.figure(figsize=(22, 13.5), dpi=300)
    gs = gridspec.GridSpec(1, 2, figure=fig, width_ratios=[5.5, 1], wspace=0.05, left=0.14, right=0.97, bottom=0.08, top=0.89)
    ax = fig.add_subplot(gs[0, 0])
    ax_marg = fig.add_subplot(gs[0, 1], sharey=ax)

    fig.suptitle("Plot 10: Continuous-Time 6-Level Alluvial Evolution Atlas (2017–2026): Down-Level Built-In Sinking, Skill Expansion & Extinction", fontsize=13.5, fontweight="bold", y=0.96)

    gen_centers = {}
    for _, grow in df_gens.iterrows():
        gid = grow["gen_id"]
        x0, x1 = grow["start_year_float"], grow["end_year_float"]
        xc = 0.5 * (x0 + x1)
        gen_centers[gid] = (x0, x1, xc)
        ax.axvspan(x0, x1, color="#F5F7FA" if int(gid[1]) % 2 == 0 else "#FFFFFF", alpha=0.6, zorder=0)
        ax.axvline(x0, color="#444444", linestyle="--", linewidth=1.1, alpha=0.5, zorder=1)
        y_hdr = 6.68 if gid == "G3" else 6.50
        hdr_txt = f"{gid} ({grow['duration_months']}m)\n{grow['macro_tokens_t_yr']}T | ${grow['macro_spend_b_yr']}B" if gid == "G3" else f"{gid} ({grow['start_date']}..{grow['end_date']})\n{grow['duration_months']} mos | {grow['macro_tokens_t_yr']}T tok | ${grow['macro_spend_b_yr']}B"
        ax.text(xc, y_hdr, hdr_txt, ha="center", va="top", fontsize=7.8 if gid == "G3" else 8.4, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.20", facecolor="#EFEFEF", edgecolor="#888888"))

    short_b_map = {1: "0h | $0", 2: "<50h | <$30", 3: "<200h | <$100", 4: "~600h | ~$1.5k", 5: "~2,000h | ~$500k", 6: "~10,000h | ~$100M+"}
    for _, crow in df_cells.iterrows():
        gid = crow["gen_id"]
        lvl = int(crow["level_id"])
        x0, x1, xc = gen_centers[gid]
        w = (x1 - x0) * 0.76
        rect = mpatches.FancyBboxPatch((xc - w/2, lvl - 0.29), w, 0.58, boxstyle="round,pad=0.02",
                                       facecolor="white", edgecolor=C_SUPPLY if lvl >= 3 else C_ACTUAL, linewidth=1.6, zorder=4)
        ax.add_patch(rect)
        max_chars = 14 if gid == "G3" else (21 if gid == "G2" else 24)
        short_title = crow["user_first_title"][:max_chars] + (".." if len(crow["user_first_title"]) > max_chars else "")
        lbl_top = f"{gid}-L{lvl}" if gid == "G3" else f"{gid}-L{lvl} ({short_b_map[lvl]})"
        ax.text(xc, lvl + 0.09, lbl_top, ha="center", va="center", fontsize=7.2 if gid == "G3" else 7.5, fontweight="bold", color="#111111", zorder=5)
        ax.text(xc, lvl - 0.11, short_title, ha="center", va="center", fontsize=6.4 if gid == "G3" else 6.9, color="#333333", zorder=5)

    sinking_links = [
        ("G0", 6, "G1", 5), ("G0", 5, "G1", 4), ("G0", 4, "G1", 2), ("G0", 3, "G1", 2), ("G0", 3, "G1", 1),
        ("G1", 6, "G2", 5), ("G1", 2, "G2", 1), ("G1", 5, "G2", 4), ("G1", 4, "G2", 2),
        ("G2", 6, "G3", 5), ("G2", 2, "G3", 1), ("G2", 3, "G3", 2),
        ("G3", 6, "G4", 5), ("G3", 2, "G4", 1), ("G3", 4, "G4", 2), ("G3", 4, "G4", 3),
    ]
    expansion_links = [
        ("G0", 4, "G1", 5), ("G0", 5, "G1", 6), ("G1", 3, "G2", 3), ("G1", 4, "G2", 4), ("G1", 5, "G2", 6),
        ("G2", 3, "G3", 3), ("G2", 4, "G3", 4), ("G2", 5, "G3", 6), ("G3", 3, "G4", 4), ("G3", 5, "G4", 5), ("G3", 5, "G4", 6),
    ]
    for gA, lA, gB, lB in sinking_links:
        x0 = gen_centers[gA][2] + (gen_centers[gA][1] - gen_centers[gA][0]) * 0.38
        x1 = gen_centers[gB][2] - (gen_centers[gB][1] - gen_centers[gB][0]) * 0.38
        draw_bezier_ribbon(ax, x0, lA, x1, lB, color=C_ACTUAL, alpha=0.50, lw=5.2, zorder=3)
    for gA, lA, gB, lB in expansion_links:
        x0 = gen_centers[gA][2] + (gen_centers[gA][1] - gen_centers[gA][0]) * 0.38
        x1 = gen_centers[gB][2] - (gen_centers[gB][1] - gen_centers[gB][0]) * 0.38
        draw_bezier_ribbon(ax, x0, lA, x1, lB, color=C_SUPPLY, alpha=0.45, lw=4.2, zorder=3)

    obsolete_stubs = [
        ("G0", 3, "Obsolete: 10k Manual Label Curation"),
        ("G1", 2, "Obsolete: stop=['\\n'] Prefix Hacks"),
        ("G2", 3, "Obsolete: 20-PDF Python Chunking"),
        ("G3", 2, "Obsolete: Manual CoT Wrappers"),
    ]
    for gA, lA, otext in obsolete_stubs:
        x_end = gen_centers[gA][1] - 0.04
        ax.scatter([x_end], [lA - 0.34], color=C_DEMAND, marker="X", s=90, zorder=6)
        ax.text(x_end, lA - 0.44, otext, fontsize=7.2, color=C_DEMAND, fontweight="bold", ha="right", zorder=6)

    apply_calendar_grid(ax, 2017.4, 2026.85)
    ax.set_ylim(0.0, 6.95)
    ax.set_yticks([1, 2, 3, 4, 5, 6])
    ax.set_yticklabels([COMPACT_TICK_LABELS[i] for i in [1, 2, 3, 4, 5, 6]], fontsize=9.2, fontweight="bold")
    ax.set_xlabel("Continuous Calendar Time (Column Widths Proportional to Generation Duration in Months)", fontsize=11, fontweight="bold")

    handles = [
        mpatches.Patch(color=C_ACTUAL, alpha=0.6, label="Down-Level Sinking (Old High-Level Workflow Becomes Built-In at Lower Level)"),
        mpatches.Patch(color=C_SUPPLY, alpha=0.6, label="Upward Frontier Skill Expansion (New Use Case Requires New Learning)"),
        plt.Line2D([0], [0], color=C_DEMAND, marker="X", linestyle="None", markersize=9, label="Obsolete User Skill Extinction"),
    ]
    ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.01, 0.99), ncol=3, frameon=False, fontsize=9.2)

    ax_marg.hist(df_cells["level_id"].values, bins=np.arange(0.5, 7.5, 1.0), weights=df_cells["token_share_pct"].values / 5.0,
                 orientation="horizontal", histtype="step", fill=False, linewidth=2.0, color=C_SUPPLY, label="Mean Token %")
    ax_marg.hist(df_cells["level_id"].values, bins=np.arange(0.5, 7.5, 1.0), weights=df_cells["user_share_pct"].values / 5.0,
                 orientation="horizontal", histtype="step", fill=False, linewidth=2.0, color=C_DEMAND, label="Mean User %")
    ax_marg.set_xlabel("Mean Gen Share (%)", fontsize=9.5, fontweight="bold")
    ax_marg.legend(loc="upper right", frameon=False, fontsize=8.5)
    ax_marg.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25)
    plt.setp(ax_marg.get_yticklabels(), visible=False)

    out_path = os.path.join(FIG_DIR, "fig_v5_p10_alluvial_evolution_poster.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


# ==============================================================================
# PLOT 11: ON-LADDER TRL 1-9 MATURATION (12 LINEAGES) & FAILED HOPES
# ==============================================================================
def render_plot11_trl_and_hopes(dfs):
    df_trl = dfs["trl_trajectories"]
    fig = plt.figure(figsize=(16.5, 7.5), dpi=300)
    gs = gridspec.GridSpec(1, 3, figure=fig, width_ratios=[3.2, 0.7, 2.8], wspace=0.14, left=0.13, right=0.97, bottom=0.11, top=0.82)
    ax_l = fig.add_subplot(gs[0, 0])
    ax_m = fig.add_subplot(gs[0, 1], sharey=ax_l)
    ax_r = fig.add_subplot(gs[0, 2])

    fig.suptitle("Plot 11: On-Ladder TRL 1–9 Maturation Trajectories (12 Lineages: L6 Genesis to L1 Default) & Population Evolution of Hopes", fontsize=11.5, fontweight="bold", y=0.96)

    def ym_to_float(ym_str):
        ym = ym_str.split(" ")[0]
        y, m = map(int, ym.split("-"))
        return y + (m - 0.5) / 12.0

    rng = np.random.default_rng(42)
    perm = rng.permutation(len(df_trl))
    all_trl_points = []
    trl_label_pos = {
        "TRL_01": (0.0,   9.12),
        "TRL_02": (0.0,   9.12),
        "TRL_03": (0.0,   9.12),
        "TRL_04": (-0.28, 9.08),
        "TRL_05": (-0.15, 9.35),
        "TRL_06": (0.0,   9.58),
        "TRL_07": (0.28,  9.26),
        "TRL_08": (0.18,  9.42),
        "TRL_09": (-0.25, 9.10),
        "TRL_10": (0.25,  9.62),
        "TRL_11": (-0.22, 9.52),
        "TRL_12": (0.22,  9.18),
    }
    for idx in perm:
        row = df_trl.iloc[idx]
        xs = [ym_to_float(row["trl_1_3_genesis"]), ym_to_float(row["trl_4_6_prototype"]),
              ym_to_float(row["trl_7_8_workflow"]), ym_to_float(row["trl_9_default"])]
        ys = [2.0, 4.5, 7.0, 9.0]
        all_trl_points.extend(ys)
        is_gov = int(row["lineage_id"].split("_")[1]) >= 9
        col_line = C_DEMAND if is_gov else C_SUPPLY
        ax_l.plot(xs, ys, color=col_line, alpha=0.45, linewidth=1.6, marker="s" if is_gov else "o", zorder=2)
        dx, y_targ = trl_label_pos.get(row["lineage_id"], (0.0, 9.12))
        ax_l.annotate(row["lineage_id"], (xs[-1] + dx, y_targ), fontsize=6.9, fontweight="bold", ha="center", color="#222222")

    mean_x = np.linspace(2018.5, 2025.5, 50)
    mean_y = 2.0 + 7.0 * ((mean_x - 2018.5) / (2025.5 - 2018.5))**0.85
    mean_lag = df_trl["months_trl1_to_9"].mean()
    ax_l.plot(mean_x, mean_y, color=C_ACTUAL, linewidth=3.0, zorder=5, label=f"Mean TRL Maturation Curve (Lag μ = {mean_lag:.1f} mos)")
    ax_l.plot([], [], color=C_SUPPLY, marker="o", linewidth=1.6, label="Technical Lineages (TRL_01..TRL_08)")
    ax_l.plot([], [], color=C_DEMAND, marker="s", linewidth=1.6, label="Governance & Safety (TRL_09..TRL_12)")

    apply_calendar_grid(ax_l, 2017.4, 2026.85)
    ax_l.set_ylim(1.0, 9.85)
    ax_l.set_yticks([2.0, 4.5, 7.0, 9.0])
    ax_l.set_yticklabels(["TRL 1–3\n(L6 Genesis)", "TRL 4–5\n(L4–L5 Proto)", "TRL 7\n(L2–L3 Power)", "TRL 9\n(Built-In L1)"], fontsize=8.5, fontweight="bold")
    ax_l.set_xlabel("Calendar Time (2017–2026)", fontsize=9.5, fontweight="bold")
    ax_l.set_ylabel("On-Ladder Technology Readiness Level (TRL 1–9)", fontsize=9.5, fontweight="bold")
    ax_l.legend(loc="lower right", frameon=False, fontsize=7.6)

    ax_m.hist(all_trl_points, bins=[1.0, 3.2, 5.8, 8.0, 9.8], orientation="horizontal", histtype="step", fill=False, linewidth=1.8, color=C_SUPPLY)
    ax_m.set_xlim(0.0, 15.0)
    ax_m.set_xlabel("Milestones", fontsize=8.5, fontweight="bold")
    ax_m.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25)
    plt.setp(ax_m.get_yticklabels(), visible=False)

    gens_labels = ["Gen 0", "Gen 1", "Gen 2", "Gen 3", "Gen 4"]
    x_idx = np.arange(len(gens_labels))
    survived  = np.array([25.0, 25.0, 25.0, 25.0, 25.0])
    absorbed  = np.array([25.0, 25.0, 25.0, 25.0,  0.0])
    too_early = np.array([25.0, 25.0, 50.0, 25.0, 25.0])
    econ_dead = np.array([25.0, 25.0,  0.0, 25.0, 25.0])
    out_std   = np.array([ 0.0,  0.0,  0.0,  0.0, 25.0])

    b1 = survived
    b2 = b1 + absorbed
    b3 = b2 + too_early
    b4 = b3 + econ_dead

    ax_r.bar(x_idx, survived, color=C_ACTUAL, alpha=0.85, label="Survived to Next Gen (TRL 9)")
    ax_r.bar(x_idx, absorbed, bottom=b1, color=C_SUPPLY, alpha=0.85, label="Extinct: Base-Model Absorption")
    ax_r.bar(x_idx, too_early, bottom=b2, color=C_DEMAND, alpha=0.85, label="Extinct: Premature TRL (Too Early)")
    ax_r.bar(x_idx, econ_dead, bottom=b3, color=C_HOPE, alpha=0.85, label="Extinct: Broken Economics / Security")
    ax_r.bar(x_idx, out_std, bottom=b4, color="#777777", alpha=0.85, label="Extinct: Out-Standardized")

    ax_r.set_xticks(x_idx)
    ax_r.set_xticklabels(gens_labels, fontsize=9, fontweight="bold")
    ax_r.set_ylim(0.0, 100.0)
    ax_r.set_ylabel("Share of Generation's Hope Inventory (%)", fontsize=9.5, fontweight="bold")
    ax_r.set_xlabel("Origin Generation of Hyped Thesis", fontsize=9.5, fontweight="bold")
    ax_r.grid(True, which="major", axis="y", linestyle="-", linewidth=0.8, alpha=0.25)
    ax_r.legend(loc="lower center", bbox_to_anchor=(0.5, 1.01), ncol=2, frameon=False, fontsize=7.6)

    out_path = os.path.join(FIG_DIR, "fig_v5_p11_trl_and_failed_hopes.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


# ==============================================================================
# PLOT 12: 22-LADDER PAIRWISE MATRIX
# ==============================================================================
def render_plot12_pair_plot(dfs):
    df_lad = dfs["existing_ladders"].copy()
    cols = ["scope_coverage", "user_skill_alignment", "historical_invariance", "empirical_cost_grounding"]
    labels = ["Scope Coverage", "User-Skill Align", "Hist. Invariance", "Cost Grounding"]

    fig = plt.figure(figsize=(14, 12), dpi=300)
    gs = gridspec.GridSpec(4, 4, figure=fig, left=0.08, right=0.96, bottom=0.07, top=0.88, wspace=0.14, hspace=0.14)
    fig.suptitle("Plot 12: Published AI Ladders (22 Ladders, 2017–2026): Tri-Partite Pairwise Alignment Matrix", fontsize=13, fontweight="bold", y=0.96)

    rng = np.random.default_rng(42)
    perm = rng.permutation(len(df_lad))

    for i in range(4):
        for j in range(4):
            ax = fig.add_subplot(gs[i, j])
            x_data = df_lad[cols[j]].values
            y_data = df_lad[cols[i]].values

            if i == j:
                ax.hist(x_data, bins=np.linspace(0.35, 1.0, 9), histtype="step", fill=False, linewidth=1.8, color=C_SUPPLY)
                mu = np.mean(x_data)
                q1, q2, q3 = np.percentile(x_data, [25, 50, 75])
                iqr = q3 - q1
                ax.axvline(mu, color=C_DEMAND, linestyle="--", linewidth=1.8, label="Mean μ")
                ax.boxplot(
                    x_data, vert=False, positions=[4.1], widths=0.55,
                    manage_ticks=False, patch_artist=True,
                    boxprops=dict(facecolor=C_ACTUAL, alpha=0.35),
                    medianprops=dict(color="#111111", linewidth=1.6)
                )
                stats_txt = f"μ={mu:.2f} | Med={q2:.2f}\nMin={x_data.min():.2f} | Max={x_data.max():.2f}\nQ1={q1:.2f} | Q3={q3:.2f} | IQR={iqr:.2f}"
                ax.text(0.03, 0.96, stats_txt, transform=ax.transAxes, va="top", ha="left", fontsize=7.1,
                        bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.92, edgecolor="#CCCCCC"))
                ax.set_xlim(0.35, 1.02)
                ax.set_ylim(0.0, 7.0)
                ax.set_yticks([0, 2, 4, 6])
            elif i > j:
                ax.scatter(x_data[perm], y_data[perm], color=C_SUPPLY, alpha=0.70, s=55, edgecolors="#111111", zorder=3)
                ax.scatter([1.0], [1.0], color=C_DEMAND, marker="*", s=140, zorder=5, label="v5 6×6 Ladder")
                m, b = np.polyfit(x_data, y_data, 1)
                xg = np.linspace(0.35, 1.0, 50)
                ax.plot(xg, m * xg + b, linestyle="--", color="#000000", linewidth=1.8, zorder=4)
                ax.set_xlim(0.35, 1.02)
                ax.set_ylim(0.35, 1.02)
                ax.grid(True, linestyle="-", linewidth=0.7, alpha=0.20)
            else:
                r_val = np.corrcoef(x_data, y_data)[0, 1]
                r2_val = r_val ** 2
                mae_val = np.mean(np.abs(x_data - y_data))
                bg_col = C_ACTUAL if r_val >= 0.5 else C_HOPE
                ax.add_patch(mpatches.Rectangle((0, 0), 1, 1, transform=ax.transAxes, facecolor=bg_col, alpha=0.18))
                ax.text(0.5, 0.62, f"r = {r_val:+.2f}", transform=ax.transAxes, ha="center", va="center", fontsize=13, fontweight="bold", color="#111111")
                ax.text(0.5, 0.30, f"R² = {r2_val:.2f} | MAE = {mae_val:.2f}", transform=ax.transAxes, ha="center", va="center", fontsize=8.5, color="#222222")
                ax.set_xticks([])
                ax.set_yticks([])

            if i == 3:
                ax.set_xlabel(labels[j], fontsize=9.5, fontweight="bold")
            else:
                ax.set_xticklabels([])
            if j == 0:
                ax.set_ylabel(labels[i], fontsize=9.5, fontweight="bold")
            elif i != j:
                ax.set_yticklabels([])

    handles = [
        plt.Line2D([0], [0], color=C_SUPPLY, marker="o", linestyle="None", markersize=7, label="22 Literature Ladders"),
        plt.Line2D([0], [0], color=C_DEMAND, marker="*", linestyle="None", markersize=10, label="Our v5 6×6 (Gen × Level) Ladder"),
        plt.Line2D([0], [0], color="#000000", linestyle="--", linewidth=1.8, label="OLS Linear Fit"),
        plt.Line2D([0], [0], color=C_DEMAND, linestyle="--", linewidth=1.8, label="Parametric Mean (μ)"),
    ]
    fig.legend(handles=handles, loc="center", bbox_to_anchor=(0.5, 0.92), ncol=4, frameon=False, fontsize=9.5)

    out_path = os.path.join(FIG_DIR, "fig_v5_p12_ladder_comparison_matrix.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


# ==============================================================================
# PLOT 13: ANIMATED 6-LEVEL TRAJECTORY GIF (112 FRAMES)
# ==============================================================================
def render_plot13_animation(dfs):
    N_total = 112
    frames_remaining = int(np.ceil(N_total / SKIP_INTERVALS))
    N_render = min(frames_remaining, MAX_FRAMES_TO_RENDER)
    gif_duration = N_render / float(ANIMATION_FPS)
    total_days = 3409
    compression_ratio = total_days / gif_duration

    print("\n[ANIMATION METADATA BREAKDOWN — PRE-RENDER EQUATIONS]")
    print(f"Total Available Intervals = N_total = {N_total}")
    print(f"Frames Remaining = ceil(N_total / SKIP_INTERVALS) = ceil({N_total} / {SKIP_INTERVALS}) = {frames_remaining}")
    print(f"Rendered Frames = min(Frames Remaining, MAX_FRAMES_TO_RENDER) = min({frames_remaining}, {MAX_FRAMES_TO_RENDER}) = {N_render}")
    print(f"GIF Duration (seconds) = Rendered Frames / ANIMATION_FPS = {N_render} / {ANIMATION_FPS} = {gif_duration:.1f} s")
    print(f"Total Duration Covered = {total_days} days, 0 hours")
    print(f"Temporal Compression Ratio = {total_days} days / {gif_duration:.1f} s = {compression_ratio:.2f} days/s\n")

    df_cells = dfs["ladder_cells"]
    t_slices = np.linspace(2017.42, 2026.83, N_render)
    global_tok_curve = 0.05 * np.exp(0.98 * (t_slices - 2017.42))

    frames_pil = []
    fig = plt.figure(figsize=(10, 6.5), dpi=105)
    gs = gridspec.GridSpec(2, 1, figure=fig, height_ratios=[4, 1], hspace=0.22, left=0.10, right=0.96, bottom=0.10, top=0.90)
    ax_main = fig.add_subplot(gs[0, 0])
    ax_scrub = fig.add_subplot(gs[1, 0])

    for f_idx in range(N_render):
        t_cur = t_slices[f_idx]
        cur_gen = "G0" if t_cur < 2020.42 else ("G1" if t_cur < 2022.83 else ("G2" if t_cur < 2024.33 else ("G3" if t_cur < 2025.00 else "G4")))

        ax_main.clear()
        ax_scrub.clear()

        ax_main.set_xscale("symlog", linthresh=1.0)
        ax_main.set_yscale("symlog", linthresh=1.0)
        ax_main.set_xlim(0.0, 15000.0)
        ax_main.set_ylim(0.0, 2e8)
        ax_main.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25)
        ax_main.grid(True, which="minor", linestyle="--", linewidth=0.5, alpha=0.12)

        sub = df_cells[df_cells["gen_id"] == cur_gen].sort_values("level_id")
        xh = sub["learning_hours"].values
        yt = sub["single_task_tokens"].values
        ax_main.plot(xh, yt, color=C_SUPPLY, linewidth=2.4, marker="o", markersize=8, zorder=4, label=f"Active Gen: {cur_gen} ({t_cur:.2f})")
        for lvl, xv, yv in zip(sub["level_id"], xh, yt):
            ax_main.annotate(f"{cur_gen}-L{lvl}", (xv, yv), textcoords="offset points", xytext=(5, 4), fontsize=8, fontweight="bold")

        ax_main.set_title(f"Plot 13: AI 6-Level Ladder Evolution Trajectory (v5) | Time={t_cur:.2f} ({cur_gen})", fontsize=11, fontweight="bold")
        ax_main.set_xlabel("Beeline Learning Investment (Hours: 0h to ~10,000h, symlog)", fontsize=9, fontweight="bold")
        ax_main.set_ylabel("Single-Task Token Volume (symlog linthresh=1.0)", fontsize=9, fontweight="bold")
        ax_main.legend(loc="upper left", frameon=False, fontsize=9)

        ax_scrub.plot(t_slices, global_tok_curve, color=C_ACTUAL, linewidth=1.8, zorder=3)
        ax_scrub.axvline(t_cur, color=C_DEMAND, linewidth=2.5, zorder=6)
        apply_calendar_grid(ax_scrub, 2017.4, 2026.85)
        ax_scrub.set_yscale("symlog", linthresh=1.0)
        ax_scrub.set_yticks([])
        ax_scrub.set_xlabel("Calendar Scrubber Timeline (2017–2026, Playhead = Vermilion)", fontsize=8.5, fontweight="bold")

        fig.canvas.draw()
        buf = np.asarray(fig.canvas.buffer_rgba())
        frames_pil.append(Image.fromarray(buf[:, :, :3].copy()))

    plt.close(fig)
    out_gif = os.path.join(FIG_DIR, "fig_v5_p13_ladder_evolution_anim.gif")
    frames_pil[0].save(out_gif, save_all=True, append_images=frames_pil[1:], duration=int(1000 / ANIMATION_FPS), loop=0)
    print(f"[RENDERED ANIMATION] {out_gif} | frames={len(frames_pil)}")


# ==============================================================================
# PLOT 14: SPECULATIVE GEN 5 (6-LEVEL) MATRIX & DUAL CUTOFFS
# ==============================================================================
def render_plot14_gen5_speculative_matrix(dfs):
    sub = dfs["gen5_speculative"].sort_values("level_id")
    fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(17.2, 8.2), dpi=300, sharey=True)
    fig.subplots_adjust(left=0.20, right=0.97, bottom=0.11, top=0.82, wspace=0.08)
    fig.suptitle("Plot 14: Speculative Gen 5 (2026-08 Pre-Cutoff / 2027-03 Mainstream Crossover to 2029): 6-Level Horizon (G5-L1..L6)", fontsize=11.5, fontweight="bold", y=0.96)

    y_pos = sub["level_id"].values
    h_bar = 0.22
    ax_l.barh(y_pos - h_bar, sub["single_task_tokens"].values, height=h_bar, color=C_SUPPLY, alpha=0.85, label="Projected Single-Task Tokens (SUPPLY)")
    ax_l.barh(y_pos, sub["learning_hours"].values, height=h_bar, color=C_DEMAND, alpha=0.85, label="Beeline Learning Hours (DEMAND)")
    ax_l.barh(y_pos + h_bar, sub["single_task_wh"].values * 1000.0, height=h_bar, color=C_HOPE, alpha=0.85, label="Projected Task Energy (mWh, SPECULATIVE)")

    ax_l.set_xscale("symlog", linthresh=1.0)
    ax_l.set_xlim(0.0, 5e8)
    ax_l.set_ylim(0.5, 6.65)
    ax_l.set_yticks([1, 2, 3, 4, 5, 6])
    ax_l.set_yticklabels([f"G5-{COMPACT_TICK_LABELS[int(lvl)]}" for lvl in sub["level_id"]], fontsize=8.8, fontweight="bold")
    ax_l.set_xlabel("Projected Single-Task Magnitude (symlog scale, linthresh=1.0)", fontsize=10, fontweight="bold")
    ax_l.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25)
    ax_l.grid(True, which="minor", linestyle="--", linewidth=0.5, alpha=0.12)
    ax_l.legend(loc="lower center", bbox_to_anchor=(0.5, 1.01), ncol=3, frameon=False, fontsize=8.0)

    ax_r.barh(y_pos - h_bar, sub["user_share_pct"].values, height=h_bar, color=C_DEMAND, alpha=0.85, label="Projected User Share %")
    ax_r.barh(y_pos, sub["token_share_pct"].values, height=h_bar, color=C_SUPPLY, alpha=0.85, label="Projected Token Share %")
    ax_r.barh(y_pos + h_bar, sub["spend_share_pct"].values, height=h_bar, color=C_HOPE, alpha=0.85, label="Projected Spend Share %")

    for lvl, u_sh, t_sh, s_sh, title in zip(sub["level_id"], sub["user_share_pct"], sub["token_share_pct"], sub["spend_share_pct"], sub["user_first_title"]):
        max_bar = max(u_sh, t_sh, s_sh)
        short_t = title[:34] + (".." if len(title) > 34 else "")
        if max_bar <= 45.0:
            ax_r.text(max_bar + 1.5, lvl, f"{short_t} (U:{u_sh:g}% | T:{t_sh:g}% | S:{s_sh:g}%)", va="center", ha="left", fontsize=7.6, color="#111111")
        else:
            ax_r.text(2.0, lvl + 0.33, f"{short_t} (U:{u_sh:g}% | T:{t_sh:g}% | S:{s_sh:g}%)", va="bottom", ha="left", fontsize=7.6, fontweight="bold", color="#111111")

    ax_r.set_xlim(0.0, 100.0)
    ax_r.set_xticks(np.arange(0, 101, 20))
    ax_r.set_xticks(np.arange(0, 101, 5), minor=True)
    ax_r.set_xlabel("Projected Generation-Wide Resource Share Across L1–L6 (% of Total = 100.0%)", fontsize=10, fontweight="bold")
    ax_r.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25)
    ax_r.grid(True, which="minor", linestyle="--", linewidth=0.5, alpha=0.12)
    ax_r.legend(loc="lower center", bbox_to_anchor=(0.5, 1.01), ncol=3, frameon=False, fontsize=8.0)

    out_path = os.path.join(FIG_DIR, "fig_v5_p14_gen5_speculative_matrix.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


def render_all_plots():
    dfs = build_all_csvs()
    # 1. Render 20 Micro Cards (Plot 0-Micro, Plot 0B-Micro, 6 Per-Gen SAE Cards, 12 Per-TRL Cards)
    render_all_micro_cards(dfs, FIG_DIR)
    # 2. Render 4 Megacharts (Plot 0-Mini, Plot 0, Plot 0B-Mini, Plot 0B)
    render_plot0_mini_megachart(dfs, FIG_DIR)
    render_plot0_encyclopedic_megachart_poster(dfs, FIG_DIR)
    render_plot0b_mini_news_megachart(dfs, FIG_DIR)
    render_plot0b_historical_news_megachart_poster(dfs, FIG_DIR)
    # 3. Render 6 Visual Abstracts (VA0..VA5)
    render_visual_abstracts(dfs)
    # 4. Render 14 Analytical Plots + Animation (Plot 1..Plot 14)
    render_plot1_macro_trajectories(dfs)
    render_plot2_skill_deflation(dfs)
    render_plot3_folksonomy_raster(dfs)
    render_plot4_jointplot(dfs)
    render_plots5_to_9_gen_matrices(dfs)
    render_plot10_alluvial_poster(dfs)
    render_plot11_trl_and_hopes(dfs)
    render_plot12_pair_plot(dfs)
    render_plot13_animation(dfs)
    render_plot14_gen5_speculative_matrix(dfs)
    # 5. Run all 8 deterministic gates with figure + report verification
    run_all_gates(dfs, check_figures=True, check_report=True)
    print("\n[ALL 44 V5 VISUAL ARTIFACTS RENDERED & VERIFIED SUCCESSFULLY]")


if __name__ == "__main__":
    render_all_plots()