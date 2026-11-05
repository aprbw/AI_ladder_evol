#!/usr/bin/env python3
"""
v4_render_plots.py
Renders all 22 visual artifacts for the v4 AI Capability & Adoption Ladder Evolution
manuscript into `figures_v4/`:
  - Plot 0: 6x6 Encyclopedic Megachart Poster (`fig_v4_p0_encyclopedic_megachart_poster.png`)
  - Plot 0-Mini: 6x6 Mini Megachart (`fig_v4_p0_mini_megachart.png`)
    * Both Plot 0 and Plot 0-Mini apply the exact Mini-Mega 5-panel GridSpec(3, 2) +
      Trapezium Time-Warp Bridge architecture, top-left "AI Ladder Evolution" title +
      right-side 3-line plain-English italic subtitle, matching G0..G5 column header colors,
      bold-only GEN X / LEVEL X labels, L1 at top (y=6) down to L6 at bottom (y=1),
      and 3-part cell cards (Bold White Cell Name Header + Normal-Font Description +
      Dotted Divider + Italic Grey Keywords).
  - Plot VA0..VA5: 6 Hierarchical Visual Abstracts (`fig_v4_va0_root.png` .. `fig_v4_va5_part5.png`)
  - Plot 1: Macro Resource Trajectories (`fig_v4_p1_macro_resource_trajectories.png`)
  - Plot 2: The Skill Deflation Escalator (`fig_v4_p2_skill_deflation_escalator.png`)
  - Plot 3: Published AI Ladder Corpus & Gen Breaks (`fig_v4_p3_folksonomy_and_gen_breaks.png`)
  - Plot 4: All 30 Empirical Cells Task Cost vs. Learning Hours (`fig_v4_p4_task_cost_vs_learning_jointplot.png`)
  - Plots 5-9: Generation-Specific 6-Level Breakdown Matrices (`fig_v4_p5_gen0_matrix.png` .. `fig_v4_p9_gen4_matrix.png`)
  - Plot 10: Continuous-Time 6-Level Alluvial Evolution Atlas (`fig_v4_p10_alluvial_evolution_poster.png`)
  - Plot 11: On-Ladder TRL 1-9 Maturation Trajectories & Failed Hopes (`fig_v4_p11_trl_and_failed_hopes.png`)
  - Plot 12: 20-Ladder Pairwise Comparison Matrix (`fig_v4_p12_ladder_comparison_matrix.png`)
  - Plot 13: Animated Trajectory of the 6-Level AI Ladder (`fig_v4_p13_ladder_evolution_anim.gif`)
  - Plot 14: Speculative Gen 5 (6-Level) Matrix & Dual Cutoffs (`fig_v4_p14_gen5_speculative_matrix.png`)

Leaves `v3_render_plots.py` and `figures_v3/` 100% untouched.
"""

import os
import shutil
import textwrap
import warnings
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.path import Path
from PIL import Image

warnings.filterwarnings("ignore")

from v4_data_and_gates import (
    BASE_DIR,
    COMPACT_TICK_LABELS,
    LEVEL_BRACKET_STRS,
    build_and_verify_all,
)

FIG_DIR = os.path.join(BASE_DIR, "figures_v4")
os.makedirs(FIG_DIR, exist_ok=True)

# Global CITRA Semantic Color Palette (Locked project-wide)
C_SUPPLY = "#0072B2"    # Supply / Model-Side Capability & Compute
C_DEMAND = "#D55E00"    # Demand / User-Side Skill & Learning Hours
C_ACTUAL = "#009E73"    # Actual / Realised Production Adoption
C_HOPE   = "#CC79A7"    # Modelled / Speculative Hope Projection
C_GRAY   = "#666666"

# Configurable Top-Level Animation Constants (Section 1.5 Plot 13)
ANIMATION_FPS = 4
SKIP_INTERVALS = 1
MAX_FRAMES_TO_RENDER = 112


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
def render_visual_abstracts(data):
    va_specs = [
        ("fig_v4_va0_root.png", "Plot VA0: AI Ladder Evolution v4 (2017–2029): 6×6 User-Skill Matrix, Beeline Hours & Evolutionary Atlas", [
            ("1. 6×6 User-Centric Coordinate Grid", "Horizontal = Gen 0..Gen 5 (User Shift)\nVertical = Level 1..6 (Beeline Hours & $)\n30 Empirical + 6 Speculative = 36 Cells", C_SUPPLY),
            ("2. 6 Standardized Beeline Brackets", "L1: 0h (0d) | $0  •  L2: <50h (~1 Wk) | <$30\nL3: <200h (~1 Mo) | <$100  •  L4: ~600h | ~$1.5k\nL5: ~2,000h | ~$500k  •  L6: ~10,000h | ~$100M+", C_DEMAND),
            ("3. Down-Ladder Skill Deflation", "Math CoT: L5(2,000h)->L2(50h)->L1(0h)\n50-PDF Q&A: L4(600h)->L3(200h)->L2->L1(0h)\nMultimodal: L4(600h)->L2(50h)->L1(0h)", C_ACTUAL),
            ("4. Use vs. Make & Role Mapping", "L1: 100% Using (Casual User)\nL2–L5: Hybrid SWE & Applied/Systems MLE\nL6: 100% Genesis Making (AI Scientist, PhD)", C_SUPPLY),
            ("5. 6 Boundary & Counterfactual Rules", "Medium-Model Decoupling, Meta-Bootstrapping\nGate, 4-Tier Cognitive Input, Failure Anchor,\nRecursive Cannibalization & Setup Half-Life", C_DEMAND),
            ("6. On-Ladder TRL 1–9 & Hopes Audit", "TRL 1–3 Integrated Directly at L6 Genesis\nMean L6->L1 TRL 9 Lag: 36.2 Months\n20 Historical Hopes & 36 Glossary Terms", C_HOPE),
        ]),
        ("fig_v4_va1_part1.png", "Plot VA1: Part I Synthesis (2017–2026): Six Effort Levels, Beeline Methodology & Macro Economics", [
            ("Gen 0 (2017–2020): Pre-LLM Pipelines", "L1 Passive Widgets | L2 AutoML | L3 Sklearn\nL4 BERT | L5 Horovod | L6 Transformer Genesis\n12M Users | 0.18T Tokens | $1.1B Spend", C_SUPPLY),
            ("Gen 1 (2020–2022): Completion & Tab", "L1 Copilot Tab (0h) | L2 Playground (<50h)\nL3 OpenAI API | L4 Chains | L5 ZeRO | L6 GPT-3\n45M Users | 1.60T Tokens | $3.8B Spend", C_ACTUAL),
            ("Gen 2 (2022–2024): Chat & DIY Vector RAG", "L1 ChatGPT (0h) | L2 CoT | L3 Pinecone RAG\nL4 4-Bit QLoRA | L5 vLLM | L6 Llama-2/DPO\n380M Users | 28T Tokens | $14.0B Spend", C_DEMAND),
            ("Gen 3 (2024): Omni-Workspaces & AI IDEs", "L1 GPT-4o + Artifacts | L2 50-PDF Projects\nL3 Cursor Vibe Coding | L4 LangGraph | L6 o1\n720M Users | 240T Tokens | $39.0B Spend", C_ACTUAL),
            ("Gen 4 (2025–2026): Thinking, CLI & Sandbox", "L1 Auto-Router | L2 Deep Research | L3 MCP\nL4 Claude Code | L5 OpenClaw | L6 RLVR Genesis\n1,150M Users | 1,100T Tokens | $88.0B Spend", C_SUPPLY),
            ("Beeline Hours & 6 Validation Gates", "Zero-Filler Beeline from High School (0h)\nEliminates Gen-Ed Overhead & Min-Max Ranges\nAll 6 Programmatic Gates Pass 100%", C_HOPE),
        ]),
        ("fig_v4_va2_part2.png", "Plot VA2: Part II Raw Inventory: 20 Ladders, 36 Glossary Terms, 25 Tutorials, 30 Use Cases & 20 Hopes", [
            ("1. 20 Existing Ladders Audited", "Karpathy 1.0–3.0, OpenAI 5 Levels, DeepMind,\nAnthropic Workflows, LangChain, SAE L0–L5,\nGartner, Menlo, MIT NANDA, Gemini 23-Step", C_SUPPLY),
            ("2. 36-Term Glossary Lit Review (2.3b)", "Prompting, Vibe Coding, RAG, MCP, A2A,\nLoRA/QLoRA, vLLM, PagedAttention, FlashAttn,\nZeRO, RLHF, DPO, RLVR, GRPO, Chinchilla", C_HOPE),
            ("3. 30 Track A & Track B Use Cases", "30 Empirical Workflows Across L1–L6\nDirect Users vs Enterprise Bot Builders\n& L6 Foundation Model Genesis Teams", C_ACTUAL),
            ("4. 25 Beeline Curricula & Papers", "L1 (0h) -> L2 (<50h DL.AI) -> L3 (<200h MCP)\n-> L4 (~600h CS224N/LoRA) -> L5 (~2,000h ZeRO)\n-> L6 (~10,000h Attention/Chinchilla/R1)", C_DEMAND),
            ("5. 4-Pillar L6 Research Anchor", "(1) Math/Theory Formulation\n(2) Pretraining & Alignment Data Curation\n(3) Benchmark & Metric Design\n(4) From-Scratch Base Pretraining ($100M+)", C_SUPPLY),
            ("6. Two-Level Cost & Share Conservation", "Single-Task: Tokens, FLOPs, USD, Wh, Min\nGen-Wide: L1..L6 User%, Token%, Spend% = 100%\nZero Forbidden Min–Max Ranges", C_ACTUAL),
        ]),
        ("fig_v4_va3_part3.png", "Plot VA3: Part III 6×6 Coordinate Architecture & Six Classification Boundary Axioms", [
            ("1. Dual User-Shift Gen Cutoff Rule", "New Gen G Requires BOTH:\n(a) New Upper-Level Use Case (L3–L6)\n(b) Old Use Case Sinks to Lower Level", C_SUPPLY),
            ("2. Six Standardized Effort Levels", "L1: 0h|$0 • L2: <50h|<$30 • L3: <200h|<$100\nL4: ~600h|~$1.5k • L5: ~2,000h|~$500k\nL6: ~10,000h (~5 Yrs PhD) | ~$100M+", C_DEMAND),
            ("3. Bidirectional Medium-Model Decoupling", "No Upward Artifact Conflation (JSON/Code != L3)\nNo Downward Modality Conflation (Chat != L2)\nClassified Strictly by Cognitive Input Tier", C_ACTUAL),
            ("4. Meta-Bootstrapping Gate (Why Not L-1)", "Cell Stays at Lk Only if BOTH Fail:\n(a) Direct By-Name Delegation to L(k-1) AI\n(b) Socratic AI Onboarding within B(k-1) Hours", C_DEMAND),
            ("5. Failure-Boundary & Cannibalization", "L2/L3: Coupled Happy-Path Build+Self-Test\nL4+: Decoupled Verification Oracles & Recovery\nEvery Rung Lk Recursively Uses Gt-L(1..k-1)", C_SUPPLY),
            ("6. Setup Half-Life Dual Sinking", "Workflows Sink Lk -> L(k-1) via:\n(a) Vendor GUI Packaging, OR\n(b) Conversational AI Socratic Bootstrapping", C_HOPE),
        ]),
        ("fig_v4_va4_part4.png", "Plot VA4: Part IV Chronological Matrix (Gen 0 to Gen 4): 30 Empirical Cells & 4-Way Counterfactuals", [
            ("Gen 0 (2017–2020) & Gen 1 (2020–2022)", "G0: Passive L1..Seq2Seq L5 + Transformer L6\nG1: Copilot Tab L1..DeepSpeed L5 + Scaling L6\nFull 6-Level Resource Conservation", C_SUPPLY),
            ("Gen 2 (2022–2024): Chat, RAG & DPO", "L1: ChatGPT | L2: CoT | L3: Vector RAG\nL4: 4-Bit QLoRA | L5: vLLM Clusters\nL6: DPO, FlashAttn-2 & Llama-2 Pretraining", C_ACTUAL),
            ("Gen 3 (2024): Omni, Vibe Coding & o1", "L1: GPT-4o + Artifacts | L2: 50-PDF Projects\nL3: Vibe Coding | L4: LangGraph | L5: Evals\nL6: Test-Time RLVR & ARC-AGI/SWE-Verified", C_DEMAND),
            ("Gen 4 (2025–2026): Thinking, CLI & Swarms", "L1: Auto-Router | L2: Deep Research | L3: MCP\nL4: Claude Code CLI | L5: OpenClaw/GRPO\nL6: On-Policy RLVR & SWE-bench Pro Genesis", C_SUPPLY),
            ("4-Pillar L6 & Upward L5->L6 Gate", "L5 (~2,000h | ~$500k) Optimizes Existing\nArchitectures; L6 (~10,000h | ~$100M+)\nInvents Next-Gen Math, Corpora & Benchmarks", C_HOPE),
            ("Obsolete User Skills per Gen", "G1 Kills: 10k Label Curation for Basic NLP\nG2 Kills: Stop-Sequence Prefix Hacks\nG3 Kills: 20-PDF Python Chunking Scripts\nG4 Kills: Manual 'Think Step by Step' CoT", C_DEMAND),
        ]),
        ("fig_v4_va5_part5.png", "Plot VA5: Part V Synthesis: Alluvial Atlas, On-Ladder TRL 1–9, 20-Ladder Matrix & Speculative Gen 5", [
            ("1. Skill Deflation Escalator (Plot 2)", "5 Anchor Workflows Sink 2–4 Levels (G0->G4)\nSaving 200–2,000 Beeline Learning Hours\nWhile L5–L6 Compute Expands 1,000x+", C_ACTUAL),
            ("2. On-Ladder TRL 1–9 Cascade (Plot 11)", "TRL 1–3 Directly Integrated at L6 Genesis\nTRL 4–5 at L4–L5 | TRL 7 at L2–L3 | TRL 9 at L1\nMean L6-to-L1 Maturation Lag: 36.2 Months", C_SUPPLY),
            ("3. Population Evolution of Hopes (Plot 11)", "20 Historical Hopes Audited Across G0–G4:\n25% Survived to TRL 9 | 75% Went Extinct\n(Too Early, Base-Model Absorption, Economics)", C_HOPE),
            ("4. 20-Ladder Pairwise Matrix (Plot 12)", "Scope μ=0.84 | Skill μ=0.82 | Hist μ=0.82\nCost Grounding μ=0.74 (IQR=0.24)\nScope vs Hist r=+0.80 | Skill vs Cost r=+0.52", C_DEMAND),
            ("5. 112-Frame Animated Trajectory (Plot 13)", "Continuous Monthly Trajectory (2017.4–2026.8)\nAcross All 6 Standardized Effort Levels\nWith Synchronized Token Volume Scrubber", C_SUPPLY),
            ("6. Speculative Gen 5 (Plot 14, G5-L1..L6)", "Pre-Cutoff: 2026-08 (>50% SWE-Pro Gate)\nPost-Cutoff: 2027-03 (Mass L1/L2 Adoption)\nAmbient OS (L1) to World-Model Genesis (L6)", C_ACTUAL),
        ]),
    ]

    for fname, title, cards in va_specs:
        fig = plt.figure(figsize=(16, 9), dpi=300)
        gs = gridspec.GridSpec(2, 3, figure=fig, left=0.04, right=0.96, bottom=0.06, top=0.84, wspace=0.12, hspace=0.18)
        fig.suptitle(title, fontsize=13, fontweight="bold", y=0.96)

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
            ax.text(0.05, 0.40, cbody, color="#111111", fontsize=9.3, va="center", ha="left", linespacing=1.42, zorder=3)

        out_path = os.path.join(FIG_DIR, fname)
        fig.savefig(out_path, dpi=300)
        plt.close(fig)
        print(f"[RENDERED] {out_path}")


# ==============================================================================
# 0B. UNIFIED MINI-MEGA & FULL MEGACHART RENDERER (Plot 0-Mini & Plot 0)
# ==============================================================================
def _render_megachart_common(data, is_full_poster=False):
    """
    Renders either:
      - `fig_v4_p0_mini_megachart.png` (when `is_full_poster=False`), OR
      - `fig_v4_p0_encyclopedic_megachart_poster.png` (when `is_full_poster=True`)
    by applying EVERY visual and structural principle from the Mini Megachart
    in the exact same way across all 36 cells (6 Generations G0..G5 x 6 Levels L1..L6).
    """
    df_cells = pd.concat([data["cells"], data["gen5_cells"]], ignore_index=True)
    df_poster = data["poster_cells"]

    xm_min, xm_max = -0.50, 5.50
    tb_min, tb_max = 2017.42, 2029.00

    fig = plt.figure(figsize=(22, 16.5), dpi=300 if is_full_poster else 200, facecolor="#FBFBF9")
    scale = 1.0

    gs = gridspec.GridSpec(
        3, 2, figure=fig,
        width_ratios=[5.85, 1.15],
        height_ratios=[4.95, 0.34, 1.38],
        left=0.128, right=0.986, bottom=0.048, top=0.915,
        wspace=0.018, hspace=0.0
    )
    ax_main   = fig.add_subplot(gs[0, 0])
    ax_right  = fig.add_subplot(gs[0, 1], sharey=ax_main)
    ax_trap   = fig.add_subplot(gs[1, 0])
    ax_bot    = fig.add_subplot(gs[2, 0])
    ax_corner = fig.add_subplot(gs[2, 1])

    # Top-Left Title + Right-Side 3-Line Plain-English Subtitle (no em dash, italic #3B3B3B)
    fig.text(
        0.128, 0.958,
        "AI Ladder Evolution",
        ha="left", va="center", fontsize=34.0, fontweight="bold", color="#111111"
    )
    subtitle_3lines = (
        "This chart maps the evolution of AI as a six-level ladder from the user's perspective, ranking how people use AI from passive everyday\n"
        "tools (Level 1) to foundational research scientists (Level 6). Because AI technology moves so fast, any static ladder definition gets obsolete\n"
        "very quickly, which is why we must track how the entire ladder evolves across generations rather than relying on a single fixed ladder."
    )
    fig.text(
        0.386, 0.958,
        subtitle_3lines,
        ha="left", va="center", fontsize=9.5, style="italic", color="#3B3B3B", linespacing=1.18
    )

    # -------------------------------------------------------------------------
    # PANEL 1: TOP-LEFT MAIN MATRIX (36 Equal-Width Cards, L1 at Top y=6 -> L6 at Bottom y=1)
    # -------------------------------------------------------------------------
    ax_main.set_facecolor("#FBFBF9")
    ax_main.set_xlim(xm_min, xm_max)
    ax_main.set_ylim(0.46, 7.22)

    gen_header_specs = [
        ("G0", -0.50, 0.50, 2017.42, 2020.42, "GEN 0\nPre-LLM &\nPassive NLP",          "2017-06–2020-05\n3.0 years", "#EFEFEF", "#555555", 16.0 * scale),
        ("G1",  0.50, 1.50, 2020.42, 2022.83, "GEN 1\nPlaygrounds &\nAutocomplete",     "2020-06–2022-10\n2.4 years", "#EBF3FA", "#0072B2", 16.0 * scale),
        ("G2",  1.50, 2.50, 2022.83, 2024.33, "GEN 2\nChatbots &\nVector RAG",          "2022-11–2024-04\n1.5 years", "#FDF2E9", "#D55E00", 16.0 * scale),
        ("G3",  2.50, 3.50, 2024.33, 2025.00, "GEN 3\nOmni-Modal &\nVibe Coding",       "2024-05–2024-12\n0.7 years", "#E8F6F3", "#009E73", 16.0 * scale),
        ("G4",  3.50, 4.50, 2025.00, 2026.803,"GEN 4\nReasoners &\nCLI Agents",         "2025-01–2026-10\n1.8 years", "#F9EFF5", "#CC79A7", 16.0 * scale),
        ("G5",  4.50, 5.50, 2026.803,2029.00, "GEN 5 (Spec.)\nAmbient OS &\nWorld Sim", "2026-11–2028-12\n2.2 years", "#F8ECF5", "#7A2862", 16.0 * scale),
    ]
    gen_spans = {gid: (xm0, xm1) for gid, xm0, xm1, *_ in gen_header_specs}

    for gid, xm0, xm1, tb0, tb1, gtitle, _, bg_c, hdr_c, hdr_fs in gen_header_specs:
        w_col = xm1 - xm0
        pad_x = 0.036
        ax_main.axvspan(xm0, xm1, color=bg_c, alpha=0.34, zorder=0)
        ax_main.axvline(xm0, color="#444444", linestyle="-" if gid != "G5" else "--", linewidth=1.4 * scale, alpha=0.75, zorder=2)
        hdr_box = mpatches.FancyBboxPatch(
            (xm0 + pad_x, 6.58), w_col - 2 * pad_x, 0.58,
            boxstyle="round,pad=0.010", facecolor=hdr_c, edgecolor="#111111", linewidth=1.3 * scale, zorder=6
        )
        ax_main.add_patch(hdr_box)
        glines = gtitle.splitlines()
        for idx_g, gline in enumerate(glines):
            yg_line = 6.870 + (0.5 * (len(glines) - 1) - idx_g) * 0.172
            ax_main.text(
                0.5 * (xm0 + xm1), yg_line, gline,
                ha="center", va="center", fontsize=hdr_fs,
                fontweight="bold" if idx_g == 0 else "normal",
                color="white", zorder=7
            )

    xm_pre_cut  = 4.50
    xm_today    = 4.50
    xm_post_cut = 4.50

    for y_div in [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]:
        ax_main.axhline(y_div, color="#888888", linestyle=":" if y_div < 6.0 else "-", linewidth=(0.9 if y_div < 6.0 else 1.2) * scale, alpha=0.55, zorder=1)
        ax_right.axhline(y_div, color="#888888", linestyle=":" if y_div < 6.0 else "-", linewidth=(0.9 if y_div < 6.0 else 1.2) * scale, alpha=0.55, zorder=1)

    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()

    def wrap_to_exact_2_lines(ax, text_str, x_anchor, y_anchor, max_w_px, fs, weight="normal", style="normal"):
        words = text_str.split()
        n = len(words)
        assert n >= 2, f"Need at least 2 words to form 2 lines: {text_str}"

        def line_w(s):
            p = ax.text(x_anchor, y_anchor, s, fontsize=fs, fontweight=weight, style=style, alpha=0.0)
            w = p.get_window_extent(renderer=renderer).width
            p.remove()
            return w

        best_cand = None
        best_score = 1e12
        for i in range(1, n):
            l1 = " ".join(words[:i])
            l2 = " ".join(words[i:])
            w1, w2 = line_w(l1), line_w(l2)
            mx = max(w1, w2)
            mn = min(w1, w2)
            over = max(0.0, mx - max_w_px) * 1000.0
            score = over + mx + 0.20 * (mx - mn)
            if score < best_score:
                best_score = score
                best_cand = f"{l1}\n{l2}"
        return best_cand

    mini_keywords_subset_map = {
        ("G0", 1): "autocorrect, spam filters, Smart Compose, neural machine translation, sequence tagger",
        ("G0", 2): "AutoML tables, regex intent rules, confidence sliders, confusion matrix, precision-recall",
        ("G0", 3): "TF-IDF matrices, gradient-boosted trees, n-gram tokenization, lemmatization, stratified k-fold CV",
        ("G0", 4): "pretrained encoders, BERT fine-tuning, [CLS] classification head, SQuAD extractive QA, NER",
        ("G0", 5): "seq2seq layers, ONNX quantization, TensorRT graph fusion, Horovod all-reduce, beam search",
        ("G0", 6): "self-attention math, QKV projections, Masked Language Modeling, GLUE benchmark, SuperGLUE",
        ("G1", 1): "ghost-text autocomplete, Tab-to-accept, GitHub Copilot, docstring-to-code, inline IDE plugin",
        ("G1", 2): "few-shot exemplars, stop sequences, completion prefixes, token probabilities, Playground GUI",
        ("G1", 3): "completion API wrappers, dense embeddings, FAISS cosine search, GPT2Tokenizer, 2049-token window",
        ("G1", 4): "linear prompt chains, Chain-of-Thought, pass@20 sampling, JSONL fine-tuning, calibration suites",
        ("G1", 5): "DeepSpeed ZeRO-3, 3D parallelism, pipeline parallelism, activation checkpointing, Slurm",
        ("G1", 6): "neural scaling laws, InstructGPT RLHF, PPO alignment, HumanEval pass@k, MMLU benchmark",
        ("G2", 1): "zero-shot chat, multi-turn dialog, ChatGPT web app, instruction following, regenerate button",
        ("G2", 2): "prompt engineering, system role persona, XML delimiters, step-by-step CoT trigger, rubrics",
        ("G2", 3): "chunked vector RAG, HNSW vector index, top-k cosine retrieval, LangChain, Pydantic schemas",
        ("G2", 4): "4-bit QLoRA, NormalFloat NF4, low-rank adapters, ReAct agent loop, LLM-as-a-Judge, GGUF llama.cpp",
        ("G2", 5): "vLLM PagedAttention, KV-cache blocks, continuous batching, TensorRT-LLM, Triton server, TTFT SLAs",
        ("G2", 6): "Chinchilla scaling, Direct Preference Optimization, SWE-bench, GPQA Diamond, MoE",
        ("G3", 1): "omni-modal voice/vision, Claude Artifacts, live UI preview pane, screenshot-to-code, 320ms audio",
        ("G3", 2): "million-token context, Claude Projects, Gemini 2M window, NotebookLM Audio Overview, zero-RAG",
        ("G3", 3): "vibe coding, Cursor Composer, multi-file repo diffs, prompt caching, hybrid BM25+vector RAG",
        ("G3", 4): "cyclic StateGraphs, LangGraph, typed state schemas, conditional routing edges, DPO tuning",
        ("G3", 5): "container eval farms, Docker-in-Docker, SWE-bench Verified, parallel pytest sandboxes, vLLM cluster",
        ("G3", 6): "RLVR verifiable rewards, critic-free GRPO, Ring Attention, Multi-head Latent Attention, OSWorld",
        ("G4", 1): "auto-thinking router, hidden reasoning tokens, interactive MCP App cards, zero-CoT chat, AAIF",
        ("G4", 2): "Deep Research agents, Socratic brief scoping, multi-hop web browsing, citation verification",
        ("G4", 3): "Model Context Protocol, .mcp.json manifests, AGENTS.md, OAuth 2.1 scopes, Llama Guard rails",
        ("G4", 4): "Claude Code CLI, Codex CLI, harness engineering, decoupled test oracles, property-based testing",
        ("G4", 5): "OpenClaw daemon, M4 Mac Mini sandbox, air-gapped VLAN, CVE-2026-30616 remediation, H200 clusters",
        ("G4", 6): "pure-RL emergence, DeepSeek-R1-Zero, synthetic RLVR flywheels, SWE-bench Pro, Blackwell B200",
        ("G5", 1): "ambient OS delegate, persistent memory graph, cross-app orchestration, on-device NPU silicon",
        ("G5", 2): "declarative outcome specs, zero-CLI cloud studio, 1-click OAuth MCP store, behavioral diff review",
        ("G5", 3): "Agent-to-Agent contracts, MCP v2 registry, AWS Cedar policy, Open Policy Agent, shadow replay",
        ("G5", 4): "formal proof oracles, Lean 4 invariants, TLA+ state machines, digital-twin simulation",
        ("G5", 5): "nightly on-policy RLVR, confidential compute TEEs, sovereign GPU enclaves, zero-trust racks",
        ("G5", 6): "causal world models, continual plasticity, open-ended self-play, ARC-AGI-3, Lean-5 oracle",
    }

    for _, prow in df_poster.iterrows():
        gid = prow["gen_id"]
        lvl = int(prow["level_id"])
        m_title = prow["cell_name"]
        m_desc = prow["plain_desc"]
        mega_kw_set = {k.strip() for k in prow["keywords_1line"].split(",")}
        m_keywords = mini_keywords_subset_map[(gid, lvl)]
        for mk in [k.strip() for k in m_keywords.split(",")]:
            assert mk in mega_kw_set, f"Mini-Mega keyword '{mk}' not in Mega keywords for {gid}-L{lvl}"
        m_enc_body = prow["encyclopedic_body"]
        crow = df_cells[(df_cells["gen_id"] == gid) & (df_cells["level_id"] == lvl)].iloc[0]

        y_lvl  = 7 - lvl   # Level 1 at top (y=6), Level 6 at bottom (y=1)
        x0, x1 = gen_spans[gid]
        w_col  = x1 - x0
        pad_x  = 0.028
        x_left = x0 + pad_x
        w_box  = w_col - 2 * pad_x
        y_bot  = y_lvl - 0.455
        h_box  = 0.910

        if gid == "G5":
            edge_c, hdr_fill, box_fill = C_HOPE, "#7A2862", "#FFFBFD"
        elif gid == "G0" and lvl == 1:
            edge_c, hdr_fill, box_fill = "#666666", "#555555", "#F7F7F7"
        elif lvl <= 2:
            edge_c, hdr_fill, box_fill = C_ACTUAL, "#116649", "#FFFFFF"
        else:
            edge_c, hdr_fill, box_fill = C_SUPPLY, "#0B4F7C", "#FFFFFF"

        card = mpatches.FancyBboxPatch(
            (x_left, y_bot), w_box, h_box,
            boxstyle="round,pad=0.010", facecolor=box_fill, edgecolor=edge_c,
            linewidth=(1.5 if gid != "G5" else 1.8) * scale,
            linestyle="--" if gid == "G5" else "-", zorder=4
        )
        ax_main.add_patch(card)

        # MINI-MEGA 3-SECTION CELL LAYOUT (Uniform fixed font sizes across all 36 cells):
        # 1. Top Header Strip: 2-line bold white Cell Name (12.0pt)
        # 2. Middle Body: 2-line normal-font Description (6.8pt)
        # 3. Dotted Divider + Bottom 2-line italic grey (#3B3B3B) Subset Keywords (6.0pt)
        hdr_y0 = y_lvl + 0.085
        hdr_h  = 0.370
        hdr_cy = hdr_y0 + 0.5 * hdr_h
        desc_y_top = y_lvl + 0.055

        hdr_strip = mpatches.FancyBboxPatch(
            (x_left, hdr_y0), w_box, hdr_h,
            boxstyle="round,pad=0.005", facecolor=hdr_fill, edgecolor="none", zorder=5
        )
        ax_main.add_patch(hdr_strip)

        cur_tfs, cur_dfs, cur_kfs = (12.0, 6.0, 5.75)
        in_pad = 0.022
        x_txt_l = x_left + in_pad
        x_txt_r = x_left + w_box - in_pad
        max_w_px = ax_main.transData.transform((x_txt_r, y_lvl))[0] - ax_main.transData.transform((x_txt_l, y_lvl))[0]

        wrapped_title = wrap_to_exact_2_lines(ax_main, m_title, 0.5 * (x0 + x1), hdr_cy, max_w_px, cur_tfs, weight="bold")
        ax_main.text(
            0.5 * (x0 + x1), hdr_cy,
            wrapped_title,
            ha="center", va="center", fontsize=cur_tfs, fontweight="bold", color="white",
            linespacing=1.05, zorder=6
        )

        div_gap = 0.032
        wrapped_desc = wrap_to_exact_2_lines(ax_main, m_desc, x_txt_l, desc_y_top, max_w_px, cur_dfs, weight="normal")
        p_desc = ax_main.text(x_txt_l, desc_y_top, wrapped_desc, ha="left", va="top", fontsize=cur_dfs, fontweight="normal", linespacing=1.14, alpha=0.0)
        bb_d = p_desc.get_window_extent(renderer=renderer)
        p_desc.remove()
        y_d_bot = ax_main.transData.inverted().transform((0, bb_d.y0))[1]
        y_div_cell = y_d_bot - div_gap

        wrapped_kw = wrap_to_exact_2_lines(ax_main, m_keywords, x_txt_l, y_div_cell - div_gap, max_w_px, cur_kfs, style="italic")
        p_kw = ax_main.text(x_txt_l, y_div_cell - div_gap, wrapped_kw, ha="left", va="top", fontsize=cur_kfs, style="italic", linespacing=1.12, alpha=0.0)
        bb_k = p_kw.get_window_extent(renderer=renderer)
        p_kw.remove()

        y_kw_bot = ax_main.transData.inverted().transform((0, bb_k.y0))[1]
        spare_h = max(0.0, (y_kw_bot - (y_bot + 0.020)))
        y_shift = 0.45 * spare_h
        desc_y_top_adj = desc_y_top - y_shift
        y_div_cell_adj = y_div_cell - y_shift

        ax_main.text(
            x_txt_l, desc_y_top_adj,
            wrapped_desc,
            ha="left", va="top", fontsize=cur_dfs, color="#111111", linespacing=1.14,
            fontweight="normal", zorder=6
        )
        ax_main.plot(
            [x_txt_l, x_txt_r],
            [y_div_cell_adj, y_div_cell_adj],
            color=edge_c, linestyle=":", linewidth=1.0, alpha=0.65, zorder=5
        )
        ax_main.text(
            x_txt_l, y_div_cell_adj - div_gap,
            wrapped_kw,
            ha="left", va="top", fontsize=cur_kfs, color="#3B3B3B",
            style="italic", linespacing=1.12, zorder=6
        )

    # Y-Axis: Level 1 at top (y=6) down to Level 6 at bottom (y=1); ONLY "LEVEL X" bolded!
    if is_full_poster:
        y_labels_6 = [
            (1, "LEVEL 6\nAI Research\nScientist\n(~10,000h | ~$100M+)"),
            (2, "LEVEL 5\nSandbox &\nCluster Arch.\n(~2,000h | ~$500k)"),
            (3, "LEVEL 4\nHarness &\nTuning Eng.\n(~600h | ~$1.5k)"),
            (4, "LEVEL 3\nWorkflow &\nIntegrator\n(<200h | <$100)"),
            (5, "LEVEL 2\nPrompt &\nWorkspace\n(<50h | <$30)"),
            (6, "LEVEL 1\nConsumer\nTool\n(0h / 0d | $0)"),
        ]
    else:
        y_labels_6 = [
            (1, "LEVEL 6\nAI Research\nScientist"),
            (2, "LEVEL 5\nSandbox &\nCluster Arch."),
            (3, "LEVEL 4\nHarness &\nTuning Eng."),
            (4, "LEVEL 3\nWorkflow &\nIntegrator"),
            (5, "LEVEL 2\nPrompt &\nWorkspace"),
            (6, "LEVEL 1\nConsumer\nTool"),
        ]
    ax_main.set_yticks([1, 2, 3, 4, 5, 6])
    ax_main.set_yticklabels([])
    y_fs_main = 15.0 * scale
    line_step_y = 0.175 if is_full_poster else 0.195
    for y_pos, y_lbl in y_labels_6:
        ylines = y_lbl.splitlines()
        for idx_y, yline in enumerate(ylines):
            yy_line = y_pos + (0.5 * (len(ylines) - 1) - idx_y) * line_step_y
            f_sz = y_fs_main if idx_y < 3 else (12.2 * scale)
            ax_main.text(
                xm_min - 0.055, yy_line, yline,
                ha="right", va="center", fontsize=f_sz,
                fontweight="bold" if idx_y == 0 else "normal",
                color="#111111" if idx_y < 3 else "#3B3B3B",
                clip_on=False, zorder=7
            )
    ax_main.set_xticks([])

    # -------------------------------------------------------------------------
    # PANEL 1B: TRAPEZIUM TIME-WARP BRIDGE (Connects Equal-Width Grid to Linear Calendar Timeline)
    # -------------------------------------------------------------------------
    ax_trap.set_facecolor("#F4F3EF")
    ax_trap.set_xlim(0.0, 1.0)
    ax_trap.set_ylim(0.0, 1.0)
    ax_trap.set_xticks([])
    ax_trap.set_yticks([])

    def u_top(xm):
        return (xm - xm_min) / (xm_max - xm_min)

    def u_bot(tb):
        return (tb - tb_min) / (tb_max - tb_min)

    for gid, xm0, xm1, tb0, tb1, _, trap_lbl, bg_c, hdr_c, _ in gen_header_specs:
        ut0, ut1 = u_top(xm0), u_top(xm1)
        ub0, ub1 = u_bot(tb0), u_bot(tb1)
        verts = [(ut0, 1.0), (ut1, 1.0), (ub1, 0.0), (ub0, 0.0)]
        poly_bg = mpatches.Polygon(verts, closed=True, facecolor=bg_c, edgecolor="none", alpha=0.85, zorder=1)
        poly_fg = mpatches.Polygon(verts, closed=True, facecolor=hdr_c, edgecolor="none", alpha=0.22, zorder=2)
        ax_trap.add_patch(poly_bg)
        ax_trap.add_patch(poly_fg)
        ax_trap.plot([ut0, ub0], [1.0, 0.0], color="#333333", linestyle="-" if gid != "G5" else "--", linewidth=1.5 * scale, zorder=4)
        ax_trap.plot([ut1, ub1], [1.0, 0.0], color="#333333", linestyle="-", linewidth=1.2 * scale, alpha=0.6, zorder=4)

        cx_trap = 0.25 * (ut0 + ut1 + ub0 + ub1)
        ax_trap.text(
            cx_trap, 0.50, trap_lbl,
            ha="center", va="center", fontsize=8.0 * scale, fontweight="bold", color="#111111", linespacing=1.06,
            bbox=dict(boxstyle="round,pad=0.10", facecolor="white", edgecolor=hdr_c, linewidth=1.0 * scale, alpha=0.94),
            zorder=6
        )

    tb_pre_cut  = 2026.62
    tb_today    = 2026.803
    tb_post_cut = 2027.17

    cut_verts = [
        (u_top(xm_pre_cut), 1.0),
        (u_top(xm_post_cut), 1.0),
        (u_bot(tb_post_cut), 0.0),
        (u_bot(tb_pre_cut), 0.0),
    ]
    ax_trap.add_patch(mpatches.Polygon(cut_verts, closed=True, facecolor="#FFD700", edgecolor="none", alpha=0.28, zorder=3))
    ax_trap.plot([u_top(xm_pre_cut), u_bot(tb_pre_cut)], [1.0, 0.0], color=C_HOPE, linestyle=":", linewidth=1.6 * scale, zorder=5)
    ax_trap.plot([u_top(xm_post_cut), u_bot(tb_post_cut)], [1.0, 0.0], color=C_HOPE, linestyle="--", linewidth=2.0 * scale, zorder=5)
    ax_trap.plot([u_top(xm_today), u_bot(tb_today)], [1.0, 0.0], color="#C00000", linestyle="-", linewidth=3.0 * scale, zorder=8)

    # -------------------------------------------------------------------------
    # PANEL 2: TOP-RIGHT MARGINAL HISTOGRAM (10 Lines = 2 Metrics x 5 Empirical Gens across 6 Levels)
    # -------------------------------------------------------------------------
    ax_right.set_facecolor("#FBFBF9")
    gen_line_styles = [
        ("G0", "#555555", "o"),
        ("G1", "#0072B2", "s"),
        ("G2", "#D55E00", "^"),
        ("G3", "#009E73", "D"),
        ("G4", "#CC79A7", "P"),
    ]
    y_lvls = np.array([6.0, 5.0, 4.0, 3.0, 2.0, 1.0])   # midpoints of level_id = 1..6 (L1 at y=6 down to L6 at y=1)
    y_step_pts = np.array([6.5, 6.5, 5.5, 5.5, 4.5, 4.5, 3.5, 3.5, 2.5, 2.5, 1.5, 1.5, 0.5, 0.5])  # closed horizontal-bar step intervals aligned with cells
    u_handles, t_handles = [], []
    for gid, gcol, gmk in gen_line_styles:
        sub_g = df_cells[df_cells["gen_id"] == gid].sort_values("level_id")
        u_rel = sub_g["user_share_pct"].values / 100.0
        t_rel = sub_g["token_share_pct"].values / 100.0
        u_step_pts = np.concatenate([[0.0], np.repeat(u_rel, 2), [0.0]])
        t_step_pts = np.concatenate([[0.0], np.repeat(t_rel, 2), [0.0]])
        h_u, = ax_right.plot(u_step_pts, y_step_pts, color=gcol, linestyle="-", linewidth=2.2 * scale, alpha=0.75, zorder=4, label=f"{gid} Users")
        ax_right.scatter(u_rel, y_lvls, color=gcol, marker=gmk, s=38 * scale, alpha=0.85, zorder=5)
        h_t, = ax_right.plot(t_step_pts, y_step_pts, color=gcol, linestyle="--", linewidth=2.0 * scale, alpha=0.70, zorder=3, label=f"{gid} Tokens")
        ax_right.scatter(t_rel, y_lvls, facecolors="none", edgecolors=gcol, marker=gmk, s=38 * scale, linewidth=1.3 * scale, alpha=0.85, zorder=5)
        u_handles.append(h_u)
        t_handles.append(h_t)

    ax_right.set_xlim(0.0, 0.78)
    ax_right.set_xticks([0.0, 0.25, 0.50, 0.75])
    ax_right.set_xticklabels(["0.00", "0.25", "0.50", "0.75"], fontsize=9.5 * scale, fontweight="bold")
    ax_right.set_xlabel("Relative Frequency", fontsize=11.0 * scale, fontweight="bold", labelpad=4 * scale)
    ax_right.set_title("Users & Tokens Distribution", fontsize=11.0 * scale, fontweight="bold", pad=6 * scale)
    ax_right.grid(True, which="major", linestyle="-", linewidth=0.8 * scale, alpha=0.28, color="#888888")
    ax_right.legend(
        handles=u_handles + t_handles, loc="upper center", bbox_to_anchor=(0.50, 0.998),
        ncol=2, frameon=True, facecolor="white", framealpha=0.96,
        fontsize=13.0 * scale, columnspacing=0.55, handlelength=1.25, handletextpad=0.38, labelspacing=0.14, borderpad=0.20
    )
    plt.setp(ax_right.get_yticklabels(), visible=False)

    # -------------------------------------------------------------------------
    # PANEL 3: BOTTOM-LEFT TIMELINE (True Linear Calendar X-Axis + 5 News Milestones)
    # -------------------------------------------------------------------------
    ax_bot.set_facecolor("#FBFBF9")
    ax_bot.set_xlim(tb_min, tb_max)
    t_curve_emp = np.array([
        2017.42, 2018.0, 2018.8, 2019.5, 2020.42,
        2021.0,  2021.8, 2022.5, 2022.83,
        2023.3,  2023.8, 2024.33,
        2024.6,  2025.00,
        2025.5,  2026.0, 2026.62, 2026.803
    ])
    users_emp = np.array([
        2.5, 4.5, 8.0, 11.0, 15.0,
        24.0, 34.0, 42.0, 65.0,
        210.0, 320.0, 480.0,
        640.0, 780.0,
        920.0, 1040.0, 1120.0, 1150.0
    ]) * 1e6
    tokens_emp = np.array([
        0.04, 0.07, 0.12, 0.16, 0.25,
        0.55, 1.10, 1.45, 2.20,
        12.0, 22.0, 45.0,
        140.0, 280.0,
        520.0, 780.0, 1010.0, 1100.0
    ]) * 1e12
    t_curve_spec = np.array([2026.803, 2027.17, 2027.8, 2028.4, 2029.00])
    users_spec   = np.array([1150.0,  1260.0,  1420.0, 1560.0, 1650.0]) * 1e6
    tokens_spec  = np.array([1100.0,  1550.0,  2600.0, 3700.0, 4800.0]) * 1e12

    ax_bot.fill_between(t_curve_emp, 1e6, users_emp, step="mid", color=C_DEMAND, alpha=0.12, zorder=1)
    ax_bot.fill_between(t_curve_emp, 1e6, tokens_emp, step="mid", color=C_SUPPLY, alpha=0.10, zorder=1)
    ax_bot.plot(t_curve_emp, users_emp, color=C_DEMAND, linewidth=2.6 * scale, marker="o", markersize=4.5 * scale, zorder=4, label="Global Active AI Users")
    ax_bot.plot(t_curve_emp, tokens_emp, color=C_SUPPLY, linewidth=2.6 * scale, marker="s", markersize=4.5 * scale, zorder=4, label="Global Annualized Tokens")
    ax_bot.plot(t_curve_spec, users_spec, color=C_DEMAND, linestyle="--", linewidth=2.6 * scale, marker="o", markersize=4.5 * scale, zorder=4)
    ax_bot.plot(t_curve_spec, tokens_spec, color=C_SUPPLY, linestyle="--", linewidth=2.6 * scale, marker="s", markersize=4.5 * scale, zorder=4)

    for gid, _, _, tb0, tb1, _, _, bg_c, _, _ in gen_header_specs:
        ax_bot.axvspan(tb0, tb1, color=bg_c, alpha=0.25, zorder=0)
        ax_bot.axvline(tb0, color="#444444", linestyle="-" if gid != "G5" else "--", linewidth=1.2 * scale, alpha=0.75, zorder=2)

    ax_bot.axvspan(tb_pre_cut, tb_post_cut, color="#FFD700", alpha=0.18, zorder=1)
    ax_bot.axvline(tb_pre_cut, color=C_HOPE, linestyle=":", linewidth=1.6 * scale, zorder=8)
    ax_bot.axvline(tb_today, color="#C00000", linestyle="-", linewidth=3.0 * scale, zorder=12)
    ax_bot.axvline(tb_post_cut, color=C_HOPE, linestyle="--", linewidth=2.0 * scale, zorder=8)
    ax_bot.text(
        tb_today, 4.0e12,
        "◀ TODAY ▶",
        ha="center", va="center", fontsize=10.5 * scale, fontweight="bold", color="white",
        bbox=dict(boxstyle="round,pad=0.14", facecolor="#C00000", edgecolor="#111111", linewidth=1.0 * scale),
        zorder=15
    )

    ev_cat_styles = {
        "paper":   ("#005A9C", "#EAF3FB", "#003B66", "Paper & Concept Origin"),
        "release": ("#007958", "#E8F7F2", "#004430", "Model, Tool & AI Art Release"),
        "impact":  ("#B83B00", "#FFF0E5", "#5E1D00", "Viral Use, Cultural & Security News"),
        "econ":    ("#6C287A", "#F4ECF7", "#3D1247", "Econ, Hardware, Legal & Policy"),
        "course":  ("#8C5D00", "#FEF9E7", "#5C3D00", "Famous Courses & Tutorials"),
    }
    mini_events = [
        (2017.46, "2017-06:\nTransformer Paper", 4.5e7, "left", "paper"),
        (2021.48, "2021-06: GitHub\nCopilot Preview", 2.2e9, "center", "release"),
        (2022.91, "2022-11: ChatGPT\n(100M in 60d)", 2.2e6, "center", "impact"),
        (2024.49, "2024-06: Claude 3.5\nArtifacts & Cursor", 1.8e11, "center", "release"),
        (2025.08, "2025-01: DeepSeek-R1\n& Claude Code CLI", 6.5e6, "left", "release"),
    ]
    for yr_f, ev_txt, ey, ha_e, ecat in mini_events:
        edge_ev, bg_ev, txt_ev, _ = ev_cat_styles[ecat]
        ax_bot.vlines(yr_f, 1e6, ey, color=edge_ev, linestyle=":", linewidth=1.4 * scale, alpha=0.80, zorder=5)
        ax_bot.scatter([yr_f], [ey], color=edge_ev, s=42 * scale, zorder=7)
        ax_bot.text(
            yr_f, ey * 1.35, ev_txt,
            ha=ha_e, va="bottom", fontsize=11.0 * scale,
            fontweight="bold", color=txt_ev, linespacing=1.08,
            bbox=dict(boxstyle="round,pad=0.14", facecolor=bg_ev, edgecolor=edge_ev, linewidth=1.2 * scale, alpha=0.96),
            zorder=8
        )

    year_ticks = list(range(2018, 2030))
    xtick_labels = [f"{yr}" for yr in year_ticks]
    ax_bot.set_xticks(year_ticks)
    ax_bot.set_xticklabels(xtick_labels, fontsize=11.0 * scale, fontweight="bold")
    ax_bot.set_yscale("log")
    ax_bot.set_ylim(1e6, 2.5e16)
    ax_bot.set_yticks([1e6, 1e8, 1e10, 1e12, 1e14, 1e16])
    ax_bot.tick_params(axis="y", labelsize=9.5 * scale)
    ax_bot.set_ylabel("Users & Tokens", fontsize=12.0 * scale, fontweight="bold")
    ax_bot.grid(True, which="major", linestyle="-", linewidth=0.8 * scale, alpha=0.25, color="#888888")

    h_lines, _ = ax_bot.get_legend_handles_labels()
    cat_patches = [
        mpatches.Patch(facecolor=bg_c, edgecolor=ed_c, linewidth=1.2, label=lbl_c)
        for ed_c, bg_c, _, lbl_c in ev_cat_styles.values()
    ]
    ax_bot.legend(
        handles=h_lines + cat_patches, loc="upper left", bbox_to_anchor=(0.004, 0.988),
        ncol=2, frameon=True, facecolor="white", framealpha=0.95, fontsize=8.8 * scale,
        columnspacing=0.85, handletextpad=0.45, labelspacing=0.18
    )

    # -------------------------------------------------------------------------
    # PANEL 4: BOTTOM-RIGHT CORNER COLOPHON
    # -------------------------------------------------------------------------
    ax_corner.set_facecolor("#F4F1EA")
    ax_corner.set_xlim(0.0, 1.0)
    ax_corner.set_ylim(0.0, 1.0)
    ax_corner.set_xticks([])
    ax_corner.set_yticks([])
    for spine in ax_corner.spines.values():
        spine.set_linewidth(1.8 * scale)
        spine.set_edgecolor("#222222")

    ax_corner.add_patch(mpatches.Rectangle((0.0, 0.77), 1.0, 0.23, facecolor="#1B2631", edgecolor="none", zorder=1))
    ax_corner.text(
        0.50, 0.925,
        "MEGA CHART KEY" if is_full_poster else "MINI MEGA CHART",
        ha="center", va="center", fontsize=12.0 * scale, fontweight="bold", color="white", zorder=2
    )
    ax_corner.text(0.50, 0.825, "www.arianprabowo.com", ha="center", va="center", fontsize=11.5 * scale, fontweight="bold", color="#F0E442", zorder=2)

    mini_colophon = (
        "• Green Box: Direct User (L1–2)\n"
        "• Blue Box: Builder / Eng (L3–6)\n"
        "• Gray Box: Passive Baseline\n"
        "• Purple Box: Speculative Gen 5\n"
        "• Today Line: 2026-10-20\n"
        "• Pre-Cut: 2026-08 (>50%)\n"
        "• Post-Cut: 2027-03 (Mass)"
    )
    ax_corner.text(0.04, 0.73, mini_colophon, ha="left", va="top", fontsize=11.0 * scale, fontweight="bold", color="#111111", linespacing=1.20, zorder=3)

    fname = "fig_v4_p0_encyclopedic_megachart_poster.png" if is_full_poster else "fig_v4_p0_mini_megachart.png"
    out_path = os.path.join(FIG_DIR, fname)
    fig.savefig(out_path, dpi=300 if is_full_poster else 200)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


def render_plot0_encyclopedic_megachart_poster(data):
    """
    Renders `fig_v4_p0_encyclopedic_megachart_poster.png` (figsize=(44, 32), dpi=300):
    Contains 100% of the structural and textual elements of the Mini-Mega chart:
      - Top-Left "AI Ladder Evolution" title + right-side 3-line plain-English subtitle
      - Inverted 6-Level vertical axis (Level 1 at top y=6 down to Level 6 at bottom y=1)
      - Synchronized GEN 0..GEN 5 header colors matching the 10-line marginal panel
      - Middle Trapezium Time-Warp Bridge (`ax_trap`) connecting equal-width columns to linear calendar time
      - Every cell's `cell_name`, `plain_desc`, and `keywords_1line`
    PLUS all the encyclopedic richness of the v3 Mega Wallchart across all 36 cells:
      - Extended column sub-headers with exact date windows, durations, and macro Users/Tokens/Spend
      - Multi-line Y-axis Level specifications with Hours & Money brackets, Use-vs-Make Persona, and Surface/Hardware
      - Alluvial Down-Ladder Sinking & Upward Expansion Ribbons + Obsolete User Skill ('X') Extinction Badges
      - 2-line Cell Header Strip (`[Gx-Ly] Cell Name — Full Descriptive Header` + Gold Telemetry/Share Badge)
      - Tinted Sub-Header Strip with the Mini-Mega `plain_desc` summary
      - 5 Full Structured Encyclopedic Bullets per cell (`Use Cases & Landmarks`, `Techniques/Pillars`, `Models`, `Surface/Hardware`, `Counterfactual & Vocab`)
      - Bottom Dotted Divider + Italic Grey Keywords (`keywords_1line` + Beeline Bracket)
      - 6 Per-Level Mean Relative Frequency Callout Boxes in the Top-Right Marginal Panel
      - All 36 Generational-Defining Events (~3/yr across 2017–2028) on the Bottom Timeline
      - Full Encyclopedic Wallchart Colophon & Legend Cartouche
    """
    df_cells = pd.concat([data["cells"], data["gen5_cells"]], ignore_index=True)
    df_poster = data["poster_cells"]
    df_events = data["events"]

    xm_min, xm_max = -0.50, 5.50
    tb_min, tb_max = 2017.42, 2029.00

    # Exact 2.0x linear scale of Mini-Mega (44x33 vs 22x16.5) so all top-level elements have identical relative height %!
    fig = plt.figure(figsize=(44, 33), dpi=300, facecolor="#FBFBF9")
    gs = gridspec.GridSpec(
        3, 2, figure=fig,
        width_ratios=[5.85, 1.15],
        height_ratios=[4.95, 0.34, 1.38],
        left=0.082, right=0.986, bottom=0.048, top=0.915,
        wspace=0.018, hspace=0.0
    )
    ax_main   = fig.add_subplot(gs[0, 0])
    ax_right  = fig.add_subplot(gs[0, 1], sharey=ax_main)
    ax_trap   = fig.add_subplot(gs[1, 0])
    ax_bot    = fig.add_subplot(gs[2, 0])
    ax_corner = fig.add_subplot(gs[2, 1])

    # Top-Left Title (68pt = 2.0x Mini-Mega's 34pt) + Right-Side 3-Line Subtitle (19pt = 2.0x Mini-Mega's 9.5pt) at exact same y=0.958!
    fig.text(
        0.082, 0.958,
        "AI Ladder Evolution",
        ha="left", va="center", fontsize=68.0, fontweight="bold", color="#111111"
    )
    subtitle_3lines = (
        "This chart maps the evolution of AI as a six-level ladder from the user's perspective, ranking how people use AI from passive everyday\n"
        "tools (Level 1) to foundational research scientists (Level 6). Because AI technology moves so fast, any static ladder definition gets obsolete\n"
        "very quickly, which is why we must track how the entire ladder evolves across generations rather than relying on a single fixed ladder."
    )
    fig.text(
        0.340, 0.958,
        subtitle_3lines,
        ha="left", va="center", fontsize=19.0, style="italic", color="#3B3B3B", linespacing=1.18
    )

    # -------------------------------------------------------------------------
    # PANEL 1: TOP-LEFT MAIN ENCYCLOPEDIC MATRIX (36 Cells, L1 at Top y=6 -> L6 at Bottom y=1)
    # -------------------------------------------------------------------------
    ax_main.set_facecolor("#FBFBF9")
    ax_main.set_xlim(xm_min, xm_max)
    ax_main.set_ylim(0.46, 7.36)

    gen_header_specs = [
        ("G0", -0.50, 0.50, 2017.42, 2020.42,
         "GEN 0\nPre-LLM &\nPassive NLP",
         "12M Users • 0.18T Tok • $1.1B",
         "2017-06–2020-05\n3.0 years", "#EFEFEF", "#555555"),
        ("G1",  0.50, 1.50, 2020.42, 2022.83,
         "GEN 1\nPlaygrounds &\nAutocomplete",
         "45M Users • 1.60T Tok • $3.8B",
         "2020-06–2022-10\n2.4 years", "#EBF3FA", "#0072B2"),
        ("G2",  1.50, 2.50, 2022.83, 2024.33,
         "GEN 2\nChatbots &\nVector RAG",
         "380M Users • 28.0T Tok • $14.0B",
         "2022-11–2024-04\n1.5 years", "#FDF2E9", "#D55E00"),
        ("G3",  2.50, 3.50, 2024.33, 2025.00,
         "GEN 3\nOmni-Modal &\nVibe Coding",
         "720M Users • 240T Tok • $39.0B",
         "2024-05–2024-12\n0.7 years", "#E8F6F3", "#009E73"),
        ("G4",  3.50, 4.50, 2025.00, 2026.803,
         "GEN 4\nReasoners &\nCLI Agents",
         "1,150M Users • 1,100T Tok • $88B",
         "2025-01–2026-10\n1.8 years", "#F9EFF5", "#CC79A7"),
        ("G5",  4.50, 5.50, 2026.803, 2029.00,
         "GEN 5 (Spec.)\nAmbient OS &\nWorld Sim",
         "Proj: 1,650M Users • 4,800T Tok • $210B",
         "2026-11–2028-12\n2.2 years", "#F8ECF5", "#7A2862"),
    ]
    gen_spans = {gid: (xm0, xm1) for gid, xm0, xm1, *_ in gen_header_specs}

    for gid, xm0, xm1, tb0, tb1, gtitle, gsub, _, bg_c, hdr_c in gen_header_specs:
        w_col = xm1 - xm0
        pad_x = 0.032
        ax_main.axvspan(xm0, xm1, color=bg_c, alpha=0.34, zorder=0)
        ax_main.axvline(xm0, color="#444444", linestyle="-" if gid != "G5" else "--", linewidth=2.4, alpha=0.75, zorder=2)
        hdr_box = mpatches.FancyBboxPatch(
            (xm0 + pad_x, 6.58), w_col - 2 * pad_x, 0.72,
            boxstyle="round,pad=0.010", facecolor=hdr_c, edgecolor="#111111", linewidth=2.2, zorder=6
        )
        ax_main.add_patch(hdr_box)
        glines = gtitle.splitlines()
        # Top-level GEN X (32pt bold = 2.0x Mini-Mega's 16pt) + 2-line Gen Name (32pt normal = 2.0x Mini-Mega's 16pt) + small macro line (9.5pt)
        ax_main.text(0.5 * (xm0 + xm1), 7.17, glines[0], ha="center", va="center", fontsize=32.0, fontweight="bold", color="white", zorder=7)
        ax_main.text(0.5 * (xm0 + xm1), 6.97, glines[1], ha="center", va="center", fontsize=32.0, fontweight="normal", color="white", zorder=7)
        ax_main.text(0.5 * (xm0 + xm1), 6.78, glines[2], ha="center", va="center", fontsize=32.0, fontweight="normal", color="white", zorder=7)
        ax_main.text(0.5 * (xm0 + xm1), 6.625, gsub, ha="center", va="center", fontsize=9.5, fontweight="bold", color="#F0E442", zorder=7)

    # Highlight Dual Gen 4 -> Gen 5 Cutoff Zone & TODAY (2026-10-20) Beacon Line in the inter-column gutter around x = 4.50
    x_pre_cutoff = 4.468
    x_today      = 4.500
    x_post_cut   = 4.532

    ax_main.axvspan(x_pre_cutoff, x_post_cut, color="#FFD700", alpha=0.18, zorder=1)
    ax_main.axvline(x_pre_cutoff, color=C_HOPE, linestyle=":", linewidth=2.2, zorder=8)
    ax_main.axvline(x_today, color="#C00000", linestyle="-", linewidth=3.6, zorder=12)
    ax_main.axvline(x_post_cut, color=C_HOPE, linestyle="--", linewidth=2.6, zorder=8)

    ax_main.text(
        x_today, 6.515,
        "◀ TODAY: 2026-10-20 ▶  (Pre-Cutoff: 2026-08 First-Release | Post-Cutoff: 2027-03 Mainstream Crossover)",
        ha="center", va="center", fontsize=8.5, fontweight="bold", color="white",
        bbox=dict(boxstyle="round,pad=0.16", facecolor="#C00000", edgecolor="#111111", linewidth=1.2),
        zorder=15
    )

    for y_div in [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]:
        ax_main.axhline(y_div, color="#888888", linestyle=":" if y_div < 6.0 else "-", linewidth=1.2 if y_div < 6.0 else 1.8, alpha=0.55, zorder=1)
        ax_right.axhline(y_div, color="#888888", linestyle=":" if y_div < 6.0 else "-", linewidth=1.2 if y_div < 6.0 else 1.8, alpha=0.55, zorder=1)

    # Alluvial Flow Ribbons in the Inter-Column Gutters (Note: y_lvl = 7 - lvl, so sinking to L1 flows UPWARD toward y=6!)
    sinking_links = [
        (0, 4, 1, 2), (0, 3, 1, 2), (0, 3, 1, 1), (0, 6, 1, 4),
        (1, 2, 2, 1), (1, 5, 2, 4), (1, 4, 2, 2), (1, 6, 2, 4),
        (2, 2, 3, 1), (2, 3, 3, 2), (2, 6, 3, 3),
        (3, 2, 4, 1), (3, 4, 4, 2), (3, 4, 4, 3), (3, 6, 4, 1),
        (4, 2, 5, 1), (4, 3, 5, 2), (4, 4, 5, 2),
    ]
    expansion_links = [
        (0, 4, 1, 5), (0, 5, 1, 6), (1, 3, 2, 3), (1, 4, 2, 4), (1, 5, 2, 6),
        (2, 3, 3, 3), (2, 4, 3, 4), (2, 5, 3, 6), (3, 3, 4, 4), (3, 5, 4, 5),
        (4, 3, 5, 3), (4, 4, 5, 4), (4, 5, 5, 5), (4, 6, 5, 6),
    ]
    for cA, lA, cB, lB in sinking_links:
        col_rib = C_HOPE if cB == 5 else C_ACTUAL
        yA, yB = 7 - lA, 7 - lB
        draw_bezier_ribbon(ax_main, (cA - 0.50) + 0.970, yA, (cB - 0.50) + 0.030, yB, color=col_rib, alpha=0.55, lw=7.0, zorder=3)
    for cA, lA, cB, lB in expansion_links:
        col_rib = C_HOPE if cB == 5 else C_SUPPLY
        yA, yB = 7 - lA, 7 - lB
        draw_bezier_ribbon(ax_main, (cA - 0.50) + 0.970, yA, (cB - 0.50) + 0.030, yB, color=col_rib, alpha=0.45, lw=5.5, zorder=3)

    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()

    def wrap_to_exact_2_lines(ax, text_str, x_anchor, y_anchor, max_w_px, fs, weight="normal", style="normal"):
        words = text_str.split()
        n = len(words)
        assert n >= 2, f"Need at least 2 words to form 2 lines: {text_str}"

        def line_w(s):
            p = ax.text(x_anchor, y_anchor, s, fontsize=fs, fontweight=weight, style=style, alpha=0.0)
            w = p.get_window_extent(renderer=renderer).width
            p.remove()
            return w

        best_cand = None
        best_score = 1e12
        for i in range(1, n):
            l1 = " ".join(words[:i])
            l2 = " ".join(words[i:])
            w1, w2 = line_w(l1), line_w(l2)
            mx = max(w1, w2)
            mn = min(w1, w2)
            over = max(0.0, mx - max_w_px) * 1000.0
            score = over + (mx - mn)
            if score < best_score:
                best_score = score
                best_cand = f"{l1}\n{l2}"
        return best_cand

    def wrap_to_n_lines_balanced(ax, text_str, n_lines, fs, weight="normal", style="normal"):
        words = text_str.split()
        p = ax.text(0, 0, "", fontsize=fs, fontweight=weight, style=style, alpha=0.0)
        p.set_text(text_str)
        tot_w = p.get_window_extent(renderer=renderer).width
        low_w = tot_w / (n_lines + 0.8)
        high_w = tot_w
        best_lines = [text_str]
        for _ in range(20):
            mid_w = 0.5 * (low_w + high_w)
            lines = []
            cur = []
            for w in words:
                cand = " ".join(cur + [w])
                p.set_text(cand)
                if p.get_window_extent(renderer=renderer).width <= mid_w or not cur:
                    cur.append(w)
                else:
                    lines.append(" ".join(cur))
                    cur = [w]
            if cur:
                lines.append(" ".join(cur))
            if len(lines) <= n_lines:
                best_lines = lines
                high_w = mid_w
            else:
                low_w = mid_w
        p.remove()
        return "\n".join(best_lines)

    def wrap_by_pixel_width(ax, text_str, fs, max_w_px, weight="normal", style="normal"):
        words = text_str.split()
        p = ax.text(0, 0, "", fontsize=fs, fontweight=weight, style=style, alpha=0.0)
        lines = []
        cur = []
        for w in words:
            cand = " ".join(cur + [w])
            p.set_text(cand)
            if p.get_window_extent(renderer=renderer).width <= max_w_px or not cur:
                cur.append(w)
            else:
                lines.append(" ".join(cur))
                cur = [w]
        if cur:
            lines.append(" ".join(cur))
        p.remove()
        return "\n".join(lines)

    # Render all 36 Encyclopedic + Mini-Mega Unified Cells
    for _, prow in df_poster.iterrows():
        gid = prow["gen_id"]
        lvl = int(prow["level_id"])
        m_title = prow["cell_name"]
        m_short_hdr = prow["short_header"]
        m_desc = prow["plain_desc"]
        m_keywords = prow["keywords_1line"]
        m_enc_body = prow["encyclopedic_body"]
        crow = df_cells[(df_cells["gen_id"] == gid) & (df_cells["level_id"] == lvl)].iloc[0]

        y_lvl  = 7 - lvl   # Level 1 at top (y=6), Level 6 at bottom (y=1)
        x0, x1 = gen_spans[gid]
        w_col  = x1 - x0
        pad_x  = 0.028
        x_left = x0 + pad_x
        w_box  = w_col - 2 * pad_x
        y_bot  = y_lvl - 0.458
        h_box  = 0.916

        if gid == "G5":
            edge_c, hdr_fill, box_fill, sum_fill, tbl_hdr_fill, tbl_edge = C_HOPE, "#7A2862", "#FFFBFD", "#F9EFF6", "#F0DFEC", "#C9A8C0"
        elif gid == "G0" and lvl == 1:
            edge_c, hdr_fill, box_fill, sum_fill, tbl_hdr_fill, tbl_edge = "#666666", "#555555", "#F7F7F7", "#EAEAEA", "#E0E0E0", "#B8B8B8"
        elif lvl <= 2:
            edge_c, hdr_fill, box_fill, sum_fill, tbl_hdr_fill, tbl_edge = C_ACTUAL, "#116649", "#FFFFFF", "#EAF6F1", "#DCECE5", "#B0C8BE"
        else:
            edge_c, hdr_fill, box_fill, sum_fill, tbl_hdr_fill, tbl_edge = C_SUPPLY, "#0B4F7C", "#FFFFFF", "#EBF3FA", "#DCE9F5", "#B0C4D8"

        card = mpatches.FancyBboxPatch(
            (x_left, y_bot), w_box, h_box,
            boxstyle="round,pad=0.008", facecolor=box_fill, edgecolor=edge_c,
            linewidth=2.4 if gid != "G5" else 2.8,
            linestyle="--" if gid == "G5" else "-", zorder=4
        )
        ax_main.add_patch(card)

        # 1. Zone 1: Top Colored Header Strip (`y_lvl + 0.208` to `y_lvl + 0.458`, height = 0.250)
        y_hdr_bot = y_lvl + 0.208
        hdr_strip = mpatches.FancyBboxPatch(
            (x_left, y_hdr_bot), w_box, 0.250,
            boxstyle="round,pad=0.004", facecolor=hdr_fill, edgecolor="none", zorder=5
        )
        ax_main.add_patch(hdr_strip)

        tok_v = crow["single_task_tokens"]
        if tok_v >= 1e6:
            tok_str = f"{tok_v/1e6:.1f}M tok"
        elif tok_v >= 1e3:
            tok_str = f"{tok_v/1e3:.1f}k tok"
        else:
            tok_str = f"{int(tok_v)} tok"

        usd_v = crow["single_task_usd"]
        usd_str = f"${usd_v:.4f}" if usd_v < 0.01 else (f"${usd_v:.3f}" if usd_v < 0.1 else f"${usd_v:.2f}")
        wh_v = crow["single_task_wh"]
        wh_str = f"{wh_v:.3f}Wh" if wh_v < 0.1 else f"{wh_v:.1f}Wh"
        hm_v, ai_v = crow["human_minutes"], crow["ai_minutes"]
        badge_str = (
            f"Task: {tok_str} ({usd_str}, {wh_str}) • {hm_v:g}m human / {ai_v:g}m AI • "
            f"Share: U {crow['user_share_pct']:.1f}% | T {crow['token_share_pct']:.0f}% | S {crow['spend_share_pct']:.0f}%"
        )

        in_pad = 0.026
        x_txt_l = x_left + in_pad
        x_txt_r = x_left + w_box - in_pad
        max_w_px = ax_main.transData.transform((x_txt_r, y_lvl))[0] - ax_main.transData.transform((x_txt_l, y_lvl))[0]
        hdr_cy = y_hdr_bot + 0.146
        wrapped_title = wrap_to_exact_2_lines(ax_main, m_title, 0.5 * (x0 + x1), hdr_cy, max_w_px, 22.0, weight="bold")
        ax_main.text(
            0.5 * (x0 + x1), hdr_cy,
            wrapped_title,
            ha="center", va="center", fontsize=22.0, fontweight="bold", color="white", linespacing=0.98, zorder=6
        )
        ax_main.text(
            0.5 * (x0 + x1), y_hdr_bot + 0.024,
            badge_str,
            ha="center", va="center", fontsize=5.8, fontweight="bold", color="#F0E442", zorder=6
        )

        # 2. Zone 2: Sub-Header Summary Band (`y_lvl + 0.082` to `y_lvl + 0.208`, height = 0.126) with generous margins
        y_sum_bot = y_hdr_bot - 0.126
        sum_strip = mpatches.Rectangle(
            (x_left + 0.004, y_sum_bot), w_box - 0.008, 0.126,
            facecolor=sum_fill, edgecolor="none", zorder=4.5
        )
        ax_main.add_patch(sum_strip)
        sum_cy = y_sum_bot + 0.063
        wrapped_desc = wrap_to_n_lines_balanced(ax_main, m_desc, 2, 10.6, weight="bold")
        ax_main.text(
            x_txt_l, sum_cy,
            wrapped_desc,
            ha="left", va="center", fontsize=10.6, fontweight="bold", color="#111111", linespacing=1.08, zorder=6
        )

        # 3. Zone 4: Bottom Dotted Divider + 2-Line Italic Keywords Footer (`y_bot` to `y_bot + 0.100`, height = 0.100)
        y_kw_top = y_bot + 0.100
        ax_main.plot(
            [x_left + 0.010, x_left + w_box - 0.010],
            [y_kw_top, y_kw_top],
            color=edge_c, linestyle=":", linewidth=1.2, alpha=0.75, zorder=5
        )
        kw_cy = y_bot + 0.050
        wrapped_kw = wrap_to_n_lines_balanced(ax_main, m_keywords, 2, 7.1, weight="bold", style="italic")
        ax_main.text(
            x_txt_l, kw_cy,
            wrapped_kw,
            ha="left", va="center", fontsize=7.1, color="#3B3B3B", style="italic", fontweight="bold", linespacing=1.12, zorder=6
        )

        # 4. Zone 3: Interior 3x2 Structured Table (`y_kw_top + 0.004` to `y_sum_bot - 0.002`)
        subcell_titles = [
            "Extended Summary",
            "Use Cases & Landmarks",
            "User Actions",
            "Models & Products",
            "Surface & Hardware",
            "Scope & Evolution",
        ]
        raw_lines = m_enc_body.split("\n")[:6]
        y_tbl_bot = y_kw_top + 0.004
        y_tbl_top = y_sum_bot - 0.002
        w_tbl = w_box - 0.016
        h_tbl = y_tbl_top - y_tbl_bot
        x_tbl = x_left + 0.008
        ncol_t, nrow_t = 3, 2
        cw_t = w_tbl / ncol_t
        ch_t = h_tbl / nrow_t
        sh_h = 0.030
        FIXED_SUBCELL_FS = 5.75

        for idx_s, stitle in enumerate(subcell_titles):
            r_i = idx_s // ncol_t
            c_i = idx_s % ncol_t
            sx = x_tbl + c_i * cw_t
            sy = y_tbl_top - (r_i + 1) * ch_t
            raw_s = raw_lines[idx_s] if idx_s < len(raw_lines) else ""
            sbody = raw_s.split(":", 1)[1].strip() if ":" in raw_s else raw_s.strip()

            s_rect = mpatches.Rectangle(
                (sx, sy), cw_t, ch_t,
                facecolor="#F9FBFA" if (r_i + c_i) % 2 == 0 else "#FFFFFF",
                edgecolor=tbl_edge, linewidth=0.9, zorder=4.6
            )
            ax_main.add_patch(s_rect)
            sh_rect = mpatches.Rectangle(
                (sx, sy + ch_t - sh_h), cw_t, sh_h,
                facecolor=tbl_hdr_fill, edgecolor="none", zorder=4.7
            )
            ax_main.add_patch(sh_rect)
            ax_main.text(
                sx + 0.5 * cw_t, sy + ch_t - 0.5 * sh_h, stitle,
                ha="center", va="center", fontsize=FIXED_SUBCELL_FS, fontweight="bold", color="#111111", zorder=6
            )

            sc_pad_x = 0.008
            max_sc_w_px = ax_main.transData.transform((sx + cw_t - sc_pad_x, sy))[0] - ax_main.transData.transform((sx + sc_pad_x, sy))[0]
            wrapped_b = wrap_by_pixel_width(ax_main, sbody, FIXED_SUBCELL_FS, max_sc_w_px * 0.96)
            ax_main.text(
                sx + sc_pad_x, sy + 0.5 * (ch_t - sh_h),
                wrapped_b,
                ha="left", va="center", fontsize=FIXED_SUBCELL_FS, color="#151515", linespacing=1.05, zorder=6
            )

    # Obsolete User Skill Extinction Callout Badges on Inter-Column Boundaries (with y_lvl = 7 - lvl)
    obsolete_badges = [
        (0.468, 4.48, "EXTINCT IN GEN 1: 10k Manual Label Curation"),
        (1.468, 5.48, "EXTINCT IN GEN 2: stop=['\\n'] Prefix Hacks"),
        (2.468, 4.48, "EXTINCT IN GEN 3: 20-PDF Python Chunking"),
        (3.468, 5.48, "EXTINCT IN GEN 4: Manual CoT Wrappers"),
        (4.468, 4.48, "SINKS IN GEN 5: Manual .mcp.json & CLI"),
    ]
    for ox, oy, otxt in obsolete_badges:
        ax_main.scatter([ox], [oy], color=C_DEMAND, marker="X", s=110, edgecolors="#111111", linewidth=0.9, zorder=10)
        ax_main.text(
            ox - 0.016, oy, otxt, ha="right", va="center", fontsize=6.0, fontweight="bold", color="#902000",
            bbox=dict(boxstyle="round,pad=0.11", facecolor="#FFF3CD", edgecolor=C_DEMAND, linewidth=0.9), zorder=10
        )

    # Multi-Line Y-Axis Level Labels (Level 1 at top y=6 down to Level 6 at bottom y=1):
    # Top-level LEVEL X (30pt bold = 2.0x Mini-Mega's 15pt) + 2-line Role Name (30pt normal = 2.0x Mini-Mega's 15pt)!
    # Below that, concise 3-line details (Hours & Equivalent, $ & Hardware, Persona/Split) in 9.5pt (< 1/3 of LEVEL X) without repeating prefix labels!
    y_mega_specs = [
        (6, "LEVEL 1\nConsumer\nTool",
         "0h (0 days) | Zero Study Required\n"
         "$0 | Free Web / Mobile App\n"
         "Casual User (100% Using)"),
        (5, "LEVEL 2\nPrompt &\nWorkspace",
         "<50h (~1 wk) | Weekend / Short Course\n"
         "<$30/mo | Paid Web Tier / Projects\n"
         "Power-User (~90% Use / 10% Make)"),
        (4, "LEVEL 3\nWorkflow &\nIntegrator",
         "<200h (~1 mo) | Boot Camp / 1 Uni Subject\n"
         "<$100/mo | AI IDE, API & Vector DB\n"
         "Applied SWE (~65% Use / 35% Make)"),
        (3, "LEVEL 4\nHarness &\nTuning Eng.",
         "~600h (~1 qtr) | 1 Full Uni Semester\n"
         "~$1.5k | 1× GPU or CLI + Docker\n"
         "Senior SWE / MLE (~35% Use / 65% Make)"),
        (2, "LEVEL 5\nSandbox &\nCluster Arch.",
         "~2,000h (~1 yr) | Core Master's / Postgrad\n"
         "~$500k | 8–64× GPU Cluster / Enclave\n"
         "Staff Infra / MLE (~15% Use / 85% Make)"),
        (1, "LEVEL 6\nAI Research\nScientist",
         "~10,000h (~5 yrs) | Focused AI PhD\n"
         "~$100M+ | 1k–100k+ GPU Supercluster\n"
         "AI Scientist (100% Genesis)"),
    ]
    ax_main.set_yticks([1, 2, 3, 4, 5, 6])
    ax_main.set_yticklabels([])

    # "HOW TO READ THE Y-AXIS" positioned directly above LEVEL 1 (y = 6.58..7.30), right-aligned at xm_min - 0.050
    # with no box or outline (part of the Y-axis), slightly narrower than L3/L4/L5 descriptions and shorter than the GEN 0 header box!
    ax_main.text(
        xm_min - 0.050, 7.22, "HOW TO READ THE Y-AXIS",
        ha="right", va="top", fontsize=12.5, fontweight="bold", color="#111111",
        clip_on=False, zorder=8
    )
    y_axis_guide_body = (
        "Ranks AI usage by three thresholds:\n"
        "Hours & Equivalent: Cumulative\n"
        "\"beeline\" study hours from High\n"
        "School (0h) via the shortest direct\n"
        "path, plus course/degree equivalent.\n"
        "Money & Infra ($): Monthly software\n"
        "or hardware capital required.\n"
        "Persona (% Use / Make): Role and\n"
        "effort split from Using AI (100% L1)\n"
        "to Making AI systems (100% L6)."
    )
    ax_main.text(
        xm_min - 0.050, 7.11, y_axis_guide_body,
        ha="right", va="top", fontsize=8.8, fontweight="normal", color="#2B2B2B", linespacing=1.15,
        clip_on=False, zorder=8
    )

    for y_pos, y_top_3lines, lvl_bullets in y_mega_specs:
        ylines = y_top_3lines.splitlines()
        for idx_y, yline in enumerate(ylines):
            yy_line = y_pos + 0.34 - idx_y * 0.175
            ax_main.text(
                xm_min - 0.050, yy_line, yline,
                ha="right", va="center", fontsize=30.0,
                fontweight="bold" if idx_y == 0 else "normal",
                color="#111111", clip_on=False, zorder=7
            )
        ax_main.text(
            xm_min - 0.050, y_pos - 0.25, lvl_bullets,
            ha="right", va="center", fontsize=9.2, fontweight="normal", color="#2B2B2B", linespacing=1.20, clip_on=False, zorder=7
        )
    ax_main.set_xticks([])

    # -------------------------------------------------------------------------
    # PANEL 1B: TRAPEZIUM TIME-WARP BRIDGE (Connects Equal-Width Grid to Linear Calendar Timeline)
    # -------------------------------------------------------------------------
    ax_trap.set_facecolor("#F4F3EF")
    ax_trap.set_xlim(0.0, 1.0)
    ax_trap.set_ylim(0.0, 1.0)
    ax_trap.set_xticks([])
    ax_trap.set_yticks([])

    def u_top(xm):
        return (xm - xm_min) / (xm_max - xm_min)

    def u_bot(tb):
        return (tb - tb_min) / (tb_max - tb_min)

    for gid, xm0, xm1, tb0, tb1, _, _, trap_lbl, bg_c, hdr_c in gen_header_specs:
        ut0, ut1 = u_top(xm0), u_top(xm1)
        ub0, ub1 = u_bot(tb0), u_bot(tb1)
        poly = mpatches.Polygon(
            [[ut0, 1.0], [ut1, 1.0], [ub1, 0.0], [ub0, 0.0]],
            closed=True, facecolor=bg_c, edgecolor="#444444",
            linestyle="-" if gid != "G5" else "--", linewidth=2.2, alpha=0.88, zorder=2
        )
        ax_trap.add_patch(poly)
        ucx = 0.25 * (ut0 + ut1 + ub0 + ub1)
        ax_trap.text(
            ucx, 0.50, trap_lbl,
            ha="center", va="center", fontsize=16.0, fontweight="bold", color="#111111", linespacing=1.06,
            bbox=dict(boxstyle="round,pad=0.12", facecolor="white", edgecolor=hdr_c, linewidth=1.8, alpha=0.94),
            zorder=5
        )

    tb_pre_cut  = 2026.62
    tb_today    = 2026.803
    tb_post_cut = 2027.21
    ax_trap.plot([u_top(4.50), u_bot(tb_today)], [1.0, 0.0], color="#C00000", linewidth=5.0, zorder=10)
    ax_trap.plot([u_top(4.50), u_bot(tb_pre_cut)], [1.0, 0.0], color=C_HOPE, linestyle=":", linewidth=2.8, zorder=8)
    ax_trap.plot([u_top(4.50), u_bot(tb_post_cut)], [1.0, 0.0], color=C_HOPE, linestyle="--", linewidth=3.4, zorder=8)

    # -------------------------------------------------------------------------
    # PANEL 2: TOP-RIGHT MARGINAL HISTOGRAM (10 Lines + 6 Per-Level Mean Callout Boxes)
    # -------------------------------------------------------------------------
    ax_right.set_facecolor("#FBFBF9")
    gen_line_styles = [
        ("G0", "#555555", "o"),
        ("G1", "#0072B2", "s"),
        ("G2", "#D55E00", "^"),
        ("G3", "#009E73", "D"),
        ("G4", "#CC79A7", "P"),
    ]
    y_lvls = np.array([6.0, 5.0, 4.0, 3.0, 2.0, 1.0])
    y_step_pts = np.array([6.5, 6.5, 5.5, 5.5, 4.5, 4.5, 3.5, 3.5, 2.5, 2.5, 1.5, 1.5, 0.5, 0.5])
    u_handles, t_handles = [], []

    for gid, gcol, gmk in gen_line_styles:
        sub_g = df_cells[df_cells["gen_id"] == gid].sort_values("level_id")
        u_rel = sub_g["user_share_pct"].values / 100.0
        t_rel = sub_g["token_share_pct"].values / 100.0
        u_step_pts = np.concatenate([[0.0], np.repeat(u_rel, 2), [0.0]])
        t_step_pts = np.concatenate([[0.0], np.repeat(t_rel, 2), [0.0]])
        h_u, = ax_right.plot(u_step_pts, y_step_pts, color=gcol, linestyle="-", linewidth=3.4, alpha=0.78, zorder=4, label=f"{gid} Users")
        ax_right.scatter(u_rel, y_lvls, color=gcol, marker=gmk, s=70, alpha=0.88, zorder=5)
        h_t, = ax_right.plot(t_step_pts, y_step_pts, color=gcol, linestyle="--", linewidth=2.8, alpha=0.72, zorder=3, label=f"{gid} Tokens")
        ax_right.scatter(t_rel, y_lvls, facecolors="none", edgecolors=gcol, marker=gmk, s=70, linewidth=2.0, alpha=0.88, zorder=5)
        u_handles.append(h_u)
        t_handles.append(h_t)

    emp_cells = df_cells[df_cells["gen_id"].isin(["G0", "G1", "G2", "G3", "G4"])]
    for lvl in range(1, 7):
        y_pos = 7 - lvl
        sub_l = emp_cells[emp_cells["level_id"] == lvl]
        u_mu = sub_l["user_share_pct"].mean() / 100.0
        t_mu = sub_l["token_share_pct"].mean() / 100.0
        tu_ratio = (sub_l["token_share_pct"] / sub_l["user_share_pct"]).mean()
        u_str = f"{u_mu:.3f}" if u_mu < 0.005 else f"{u_mu:.2f}"
        tu_str = f"{tu_ratio:.2f}×" if tu_ratio < 10.0 else f"{tu_ratio:.1f}×"
        ax_right.text(
            0.764, y_pos + 0.45,
            f"L{lvl} Mean Rel. Freq:\nUser μ={u_str} | Tok μ={t_mu:.2f}\nTok/User: {tu_str} mean",
            ha="right", va="top", fontsize=10.2, fontweight="bold", color="#1B2631", linespacing=1.12,
            bbox=dict(boxstyle="round,pad=0.16", facecolor="white", alpha=0.94, edgecolor="#888888", linewidth=1.2),
            zorder=8
        )

    dist_commentary = (
        "DISTRIBUTION & TOKEN/USER SCALING INSIGHTS\n"
        "• Exponential User Decay: As study hours (0h→10,000h) and\n"
        "  capital ($0→$100M+) rise, user share drops sharply each\n"
        "  level: 63% (L1) → 20% (L2) → 11% (L3) → 4% (L4) → 1% (L5)\n"
        "  → 0.1% (L6).\n"
        "• Generational Shape Invariance: Despite 100× user growth\n"
        "  and 6,000× token growth (G0–G4), the relative curve shape\n"
        "  stays invariant as Down-Ladder Sinking continually refills\n"
        "  lower tiers while frontier tasks open at the top.\n"
        "• Center-Level Token Bulge (L2–L4): Unlike users (peaking\n"
        "  at L1), 64% of all tokens are consumed in the middle tiers\n"
        "  (peaking at L3, μ=0.25) via APIs, RAG, IDEs & agent loops.\n"
        "• 300× Tok/User Surge: Per-user token intensity climbs from\n"
        "  0.23× (L1 casual chat) and 0.98× (L2) to 2.37×–4.55× (L3–L4\n"
        "  agents), 11.8× (L5 clusters), and 70.0× (L6 pretraining)."
    )
    ax_right.text(
        0.155, 0.50,
        dist_commentary,
        ha="left", va="bottom", fontsize=9.2, fontweight="normal", color="#1B2631", linespacing=1.15,
        bbox=dict(boxstyle="round,pad=0.22", facecolor="#F4F1EA", alpha=0.96, edgecolor="#555555", linewidth=1.6),
        zorder=9
    )

    ax_right.set_xlim(0.0, 0.78)
    ax_right.set_xticks([0.0, 0.25, 0.50, 0.75])
    ax_right.set_xticklabels(["0.00", "0.25", "0.50", "0.75"], fontsize=19.0, fontweight="bold")
    ax_right.set_xlabel("Relative Frequency", fontsize=22.0, fontweight="bold", labelpad=8)
    ax_right.set_title("Users & Tokens Distribution", fontsize=22.0, fontweight="bold", pad=12)
    ax_right.grid(True, which="major", linestyle="-", linewidth=1.2, alpha=0.28, color="#888888")
    ax_right.legend(
        handles=u_handles + t_handles, loc="upper center", bbox_to_anchor=(0.50, 0.998),
        ncol=2, frameon=True, facecolor="white", framealpha=0.96,
        fontsize=26.0, columnspacing=0.55, handlelength=1.25, handletextpad=0.38, labelspacing=0.14, borderpad=0.20
    )
    plt.setp(ax_right.get_yticklabels(), visible=False)

    # -------------------------------------------------------------------------
    # PANEL 3: BOTTOM-LEFT LINEAR CALENDAR TIMELINE (2 Growth Curves + All 36 Generational-Defining Events)
    # -------------------------------------------------------------------------
    ax_bot.set_facecolor("#FBFBF9")
    ax_bot.set_xlim(tb_min, tb_max)

    t_curve_emp = np.array([
        2017.42, 2018.0, 2018.8, 2019.5, 2020.42,
        2021.0,  2021.8, 2022.5, 2022.83,
        2023.3,  2023.8, 2024.33,
        2024.6,  2025.00,
        2025.5,  2026.0, 2026.62, 2026.803
    ])
    users_emp = np.array([
        2.5, 4.5, 8.0, 11.0, 15.0,
        24.0, 34.0, 42.0, 65.0,
        210.0, 320.0, 480.0,
        640.0, 780.0,
        920.0, 1040.0, 1120.0, 1150.0
    ]) * 1e6
    tokens_emp = np.array([
        0.04, 0.07, 0.12, 0.16, 0.25,
        0.55, 1.10, 1.45, 2.20,
        12.0, 22.0, 45.0,
        140.0, 280.0,
        520.0, 780.0, 1010.0, 1100.0
    ]) * 1e12

    t_curve_spec = np.array([2026.803, 2027.21, 2027.8, 2028.4, 2029.00])
    users_spec   = np.array([1150.0,  1260.0,  1420.0, 1560.0, 1650.0]) * 1e6
    tokens_spec  = np.array([1100.0,  1550.0,  2600.0, 3700.0, 4800.0]) * 1e12

    ax_bot.fill_between(t_curve_emp, 1e6, users_emp, color=C_DEMAND, alpha=0.10, zorder=1)
    ax_bot.fill_between(t_curve_emp, 1e6, tokens_emp, color=C_SUPPLY, alpha=0.10, zorder=1)
    ax_bot.plot(t_curve_emp, users_emp, color=C_DEMAND, linewidth=4.8, marker="o", markersize=8.5, zorder=4, label="Global Active AI Users")
    ax_bot.plot(t_curve_emp, tokens_emp, color=C_SUPPLY, linewidth=4.8, marker="s", markersize=8.5, zorder=4, label="Global Annualized Tokens")
    ax_bot.plot(t_curve_spec, users_spec, color=C_DEMAND, linestyle="--", linewidth=4.2, marker="o", markersize=7.5, zorder=4)
    ax_bot.plot(t_curve_spec, tokens_spec, color=C_SUPPLY, linestyle="--", linewidth=4.2, marker="s", markersize=7.5, zorder=4)

    for gid, _, _, tb0, tb1, _, _, _, bg_c, _ in gen_header_specs:
        ax_bot.axvspan(tb0, tb1, color=bg_c, alpha=0.25, zorder=0)
        ax_bot.axvline(tb0, color="#444444", linestyle="-" if gid != "G5" else "--", linewidth=2.2, alpha=0.75, zorder=2)

    ax_bot.axvspan(tb_pre_cut, tb_post_cut, color="#FFD700", alpha=0.18, zorder=1)
    ax_bot.axvline(tb_pre_cut, color=C_HOPE, linestyle=":", linewidth=2.8, zorder=8)
    ax_bot.axvline(tb_today, color="#C00000", linestyle="-", linewidth=5.0, zorder=12)
    ax_bot.axvline(tb_post_cut, color=C_HOPE, linestyle="--", linewidth=3.4, zorder=8)

    year_ticks = list(range(2018, 2030))
    xtick_labels = [f"{yr}" for yr in year_ticks]
    ax_bot.set_xticks(year_ticks)
    ax_bot.set_xticklabels(xtick_labels, fontsize=22.0, fontweight="bold")
    ax_bot.set_yscale("log")
    ax_bot.set_ylim(1e6, 2.5e16)
    ax_bot.set_yticks([1e6, 1e8, 1e10, 1e12, 1e14, 1e16])
    ax_bot.tick_params(axis="y", labelsize=19.0)
    ax_bot.set_ylabel("Users & Tokens", fontsize=24.0, fontweight="bold")
    ax_bot.grid(True, which="major", linestyle="-", linewidth=1.2, alpha=0.25, color="#888888")

    ev_cat_styles = {
        "paper":   ("#005A9C", "#EAF3FB", "#003B66", "Paper & Concept Origin"),
        "release": ("#007958", "#E8F7F2", "#004430", "Model, Tool & AI Art Release"),
        "impact":  ("#B83B00", "#FFF0E5", "#5E1D00", "Viral Use, Cultural & Security News"),
        "econ":    ("#6C287A", "#F4ECF7", "#3D1247", "Econ, Hardware, Legal & Policy"),
        "course":  ("#8C5D00", "#FEF9E7", "#5C3D00", "Famous Courses & Tutorials"),
    }
    h_lines, _ = ax_bot.get_legend_handles_labels()
    cat_patches = [
        mpatches.Patch(facecolor=bg_c, edgecolor=ed_c, linewidth=2.0, label=lbl_c)
        for ed_c, bg_c, _, lbl_c in ev_cat_styles.values()
    ]
    trl_leg_line = mlines.Line2D(
        [], [], color="#005A9C", linestyle="-", linewidth=2.6,
        marker=">", markersize=11, label="TRL Lineage (Origin → Tool)"
    )
    leg_bot = ax_bot.legend(
        handles=h_lines + cat_patches + [trl_leg_line], loc="upper left", bbox_to_anchor=(0.004, 0.990),
        ncol=2, frameon=True, facecolor="white", framealpha=0.95, fontsize=16.5,
        columnspacing=0.85, handletextpad=0.45, labelspacing=0.18
    )

    # 1. Render the exact 5 Top-Level News Items + TODAY badge from Mini-Mega at 2.0x font size (21.0pt bold)
    t_today_box = ax_bot.text(
        tb_today, 4.0e12,
        "◀ TODAY ▶",
        ha="center", va="center", fontsize=21.0, fontweight="bold", color="white",
        bbox=dict(boxstyle="round,pad=0.14", facecolor="#C00000", edgecolor="#111111", linewidth=2.0),
        zorder=25
    )

    mini_events = [
        (2017.46, "2017-06:\nTransformer Paper", 4.5e7, "left", "paper"),
        (2021.48, "2021-06: GitHub\nCopilot Preview", 2.2e9, "center", "release"),
        (2022.91, "2022-11: ChatGPT\n(100M in 60d)", 2.2e6, "center", "impact"),
        (2024.49, "2024-06: Claude 3.5\nArtifacts & Cursor", 1.8e11, "center", "release"),
        (2025.08, "2025-01: DeepSeek-R1\n& Claude Code CLI", 6.5e6, "left", "release"),
    ]
    big_texts = [t_today_box]
    placed_boxes_by_label = {}
    for yr_f, ev_txt, ey, ha_e, ecat in mini_events:
        edge_ev, bg_ev, txt_ev, _ = ev_cat_styles[ecat]
        ax_bot.vlines(yr_f, 1e6, ey, color=edge_ev, linestyle=":", linewidth=2.8, alpha=0.85, zorder=18)
        ax_bot.scatter([yr_f], [ey], color=edge_ev, s=90, zorder=19)
        t_b = ax_bot.text(
            yr_f, ey * 1.35, ev_txt,
            ha=ha_e, va="bottom", fontsize=21.0,
            fontweight="bold", color=txt_ev, linespacing=1.08,
            bbox=dict(boxstyle="round,pad=0.14", facecolor=bg_ev, edgecolor=edge_ev, linewidth=2.2, alpha=0.97),
            zorder=22
        )
        big_texts.append(t_b)
        placed_boxes_by_label[ev_txt.replace("\n", " ")] = t_b

    fig.canvas.draw()
    occupied_bboxes = [t.get_window_extent(renderer=renderer).expanded(1.04, 1.12) for t in big_texts]
    occupied_bboxes.append(t_today_box.get_window_extent(renderer=renderer).expanded(1.08, 1.22))
    occupied_bboxes.append(leg_bot.get_window_extent(renderer=renderer).expanded(1.02, 1.05))
    x_min_px = ax_bot.transData.transform((tb_min + 0.02, 1e6))[0]
    x_today_px = ax_bot.transData.transform((tb_today - 0.02, 1e6))[0]

    # Define TRL Maturation & Lineage Chains (Origin Paper -> Frameworks/Models -> Consumer Tool / Impact)
    trl_chains = [
        ("TRL: CoT → Auto-Reasoners", "#005A9C", [
            ("Wei Chain-of-Thought", 2.2e11),
            ("Chinchilla Scaling & Self-Consistency", 5.5e11),
            ("DeepSeekMath Coins 'GRPO'", 1.8e12),
            ("o1-Preview & NotebookLM", 8.5e12),
            ("Open-Sources MCP & Tulu 3 'RLVR'", 3.5e13),
            ("DeepSeek-R1 Triggers", 1.5e14),
            ("GPT-5 Auto-Router Unifies", 1.6e15),
            ("Muse Spark 1.1, Claude Opus 5.5", 2.8e15),
        ]),
        ("TRL: RAG → Deep Research", "#00838F", [
            ("Meta Paper Coins 'RAG'", 2.5e12),
            ("API Waitlist Removed & Embeddings", 4.5e12),
            ("LangChain & LlamaIndex Spark Vector-RAG", 7.5e12),
            ("SWE-bench Verified & Anthropic Prompt Caching", 5.0e12),
            ("o1-Preview & NotebookLM", 8.5e12),
            ("OpenAI Launches Deep Research Agent", 3.5e13),
        ]),
        ("TRL: Copilot → Vibe Coding & Skills", "#007958", [
            ("2021-06: GitHub Copilot Preview", 2.2e9),
            ("Codex & HumanEval pass@k", 6.0e9),
            ("Yao et al. 'ReAct'", 1.8e10),
            ("Princeton 'SWE-bench' Paper", 5.0e10),
            ("GPT-4o Voice/Vision & LangGraph", 1.0e11),
            ("2024-06: Claude 3.5 Artifacts & Cursor", 1.8e11),
            ("Karpathy Coins 'Vibe Coding'", 2.8e11),
            ("Scale AI SWE-bench Pro", 4.2e11),
            ("Anthropic Launches 'Agent Skills'", 6.5e11),
            ("'Vibe Coding' Named Collins Word", 1.1e12),
            ("Linux Foundation AAIF", 1.8e12),
        ]),
        ("TRL: ZeRO/LoRA → vLLM & Open Weights", "#6C287A", [
            ("Uber Horovod Distributed DDP", 1.2e9),
            ("ONNX Runtime 1.0 & TensorRT", 1.6e9),
            ("DeepSpeed ZeRO Sharding", 2.0e9),
            ("Microsoft 'LoRA' Fine-Tuning", 7.5e8),
            ("4-Bit 'QLoRA' & Rafailov 'DPO'", 1.2e9),
            ("Kwon 'vLLM' PagedAttention", 2.0e9),
            ("Meta Llama-2 Open Weights & FlashAttention-2", 3.8e9),
        ]),
        ("TRL: Transformer → Prompt Eng & ChatGPT", "#D35400", [
            ("2017-06: Transformer Paper", 4.5e7),
            ("GLUE NLP Benchmark", 6.5e7),
            ("Devlin Google BERT", 1.0e8),
            ("SuperGLUE Benchmark & Raffel T5", 1.6e8),
            ("Liu RoBERTa & HuggingFace", 2.2e8),
            ("BERT Live on 10% of All US Google", 3.5e8),
            ("Kaplan OpenAI Neural Scaling Laws", 2.0e8),
            ("GPT-3 Beta & Gwern Coins 'Prompt Engineering'", 1.4e8),
            ("Goodside Viral Prompt Injection/Eng.", 6.0e7),
            ("2022-11: ChatGPT (100M in 60d)", 2.2e6),
            ("$335k 'Prompt Engineer' Job", 2.5e7),
            ("OpenAI Launches GPT-4 & ChatGPT Plugins", 6.5e7),
            ("Ng & OpenAI 'Prompt Engineering' Course", 1.4e8),
        ]),
        ("TRL: CLIP/DALL-E → Omni & AI Art", "#AD1457", [
            ("CLIP & DALL-E 1 Text-to-Art", 9.0e14),
            ("Craiyon / DALL-E Mini", 1.4e15),
            ("Midjourney Open Beta", 2.2e15),
            ("Stability AI Open-Sources Stable Diffusion", 3.8e15),
            ("Midjourney Art Wins Colorado", 1.8e15),
            ("OpenAI Sora Preview", 2.5e15),
            ("GPT-4o Studio Ghibli Viral Art", 3.6e15),
        ]),
        ("TRL: Hallucinations & Grounding", "#A93226", [
            ("Lee et al. NMT Paper Coins AI 'Hallucinations'", 4.5e12),
            ("Bender & Gebru 'Stochastic Parrots'", 9.0e12),
            ("Google Engineer Fired Claiming LaMDA Sentient", 1.3e13),
            ("Meta Galactica Pulled Over AI 'Hallucinations'", 2.2e13),
            ("Lawyers Sanctioned for Fake ChatGPT Citations", 4.5e13),
            ("'Hallucinate' Named Cambridge Word", 9.5e13),
        ]),
        ("TRL: CLI Agents, Escapes & Patching", "#2C3E50", [
            ("Samsung Bans ChatGPT After Source Code Leak", 1.2e7),
            ("HuggingFace Spaces API Secrets Breach", 2.2e7),
            ("Sakana 'AI Scientist' Edits Code", 4.0e7),
            ("2025-01: DeepSeek-R1 & Claude Code CLI", 6.5e6),
            ("OX Security 200k MCP RCEs Spark OpenClaw", 4.5e7),
            ("OpenAI Eval Agent Escapes & Hacks HuggingFace", 1.4e8),
            ("OpenAI GPT-5.6 Sol Finds & Patches PHP2Shell", 4.5e8),
        ]),
        ("TRL: Compute, Hardware & Capex", "#7D6608", [
            ("Google Cloud TPU v2", 1.4e13),
            ("Microsoft Invests $1B in OpenAI", 2.5e13),
            ("NVIDIA Launches A100 Tensor Core", 5.0e13),
            ("US BIS Bans A100/H100 GPU Exports", 1.8e14),
            ("Microsoft Invests $10B in OpenAI", 3.2e14),
            ("NVIDIA Crosses $1T Market Cap", 5.0e14),
            ("NVIDIA Hits $3.3T", 8.0e14),
            ("Microsoft Signs Three Mile Island", 5.5e14),
            ("Big Tech 2026 AI Capex Passes $320B/yr", 8.5e14),
        ]),
        ("TRL: Flagship AI & Agent Courses", "#8C5D00", [
            ("Stanford CS224n Deep Learning", 2.0e6),
            ("Fast.ai ULMFiT Transfer Learning", 2.5e6),
            ("Jay Alammar 'Illustrated Transformer'", 4.5e6),
            ("HuggingFace Launches Free Transformers Course", 3.5e6),
            ("Stanford CS324 'Large Language Models'", 4.5e6),
            ("Karpathy 'Build GPT from Scratch'", 8.0e6),
            ("Fast.ai 'Hackers Guide to LLMs'", 5.0e6),
            ("DeepLearning.AI 'AI Agents in LangGraph'", 8.0e6),
            ("UC Berkeley CS 294-196 LLM Agents", 4.5e6),
            ("MIT & UVA CS 6501 Agentic AI Courses", 2.0e6),
        ]),
    ]

    # Map each event row to its target_ey if it belongs to a TRL chain
    target_ey_map = {}
    chain_priority_indices = []
    for _, _, c_nodes in trl_chains:
        for substr_k, t_ey in c_nodes:
            for idx, erow in df_events.iterrows():
                if substr_k in erow["event_label"] and idx not in target_ey_map:
                    target_ey_map[idx] = t_ey
                    chain_priority_indices.append(idx)

    all_indices = [idx for idx in df_events.index if idx in target_ey_map] + [idx for idx in df_events.index if idx not in target_ey_map]

    # 2. Overlay all Secondary Historical Events (Zero Speculative G5 Events) colored by category
    candidate_tiers = list(np.geomspace(4.8e15, 1.3e6, 32))
    candidate_dxs = [0.0, -0.03, 0.03, -0.06, 0.06, -0.09, 0.09, -0.12, 0.12, -0.15, 0.15, -0.19, 0.19, -0.23, 0.23, -0.27, 0.27, -0.32, 0.32]
    placed_count = 0
    for idx in all_indices:
        erow = df_events.loc[idx]
        if erow["gen_id"] == "G5" or float(erow["year_float"]) > tb_today:
            continue
        ex = float(erow["year_float"])
        ecat = erow.get("event_category", "release")
        ev_col, bg_ev, txt_ev, _ = ev_cat_styles.get(ecat, ev_cat_styles["release"])
        lbl_str = textwrap.fill(f"{erow['date_str']}: {erow['event_label']}", width=21)

        chosen_ey = None
        chosen_bx = ex
        chosen_artist = None
        if idx in target_ey_map:
            t_ey = target_ey_map[idx]
            log_t = np.log10(t_ey)
            cand_pairs = sorted(
                [(cand_ey, dx) for cand_ey in candidate_tiers for dx in candidate_dxs],
                key=lambda p: abs(np.log10(p[0]) - log_t) + 5.5 * abs(p[1])
            )
        else:
            rot_tiers = candidate_tiers[(idx * 7) % len(candidate_tiers):] + candidate_tiers[:(idx * 7) % len(candidate_tiers)]
            cand_pairs = [(cand_ey, dx) for dx in candidate_dxs for cand_ey in rot_tiers]

        for cand_ey, dx in cand_pairs:
            bx = np.clip(ex + dx, tb_min + 0.12, tb_today - 0.14)
            t_test = ax_bot.text(
                bx, cand_ey * 1.08, lbl_str,
                ha="center", va="bottom", fontsize=5.0, fontweight="bold", linespacing=1.03,
                bbox=dict(boxstyle="round,pad=0.06", facecolor=bg_ev, edgecolor=ev_col, linewidth=0.75),
                alpha=0.0
            )
            bb_test = t_test.get_window_extent(renderer=renderer).expanded(1.015, 1.035)
            t_test.remove()
            if bb_test.x0 >= x_min_px and bb_test.x1 <= x_today_px and not any(bb_test.overlaps(occ) for occ in occupied_bboxes):
                chosen_ey = cand_ey
                chosen_bx = bx
                occupied_bboxes.append(bb_test)
                break

        if chosen_ey is not None:
            placed_count += 1
            ax_bot.plot([ex, ex, chosen_bx], [1e6, chosen_ey * 0.84, chosen_ey], color=ev_col, linestyle=":", linewidth=0.85, alpha=0.45, zorder=5)
            ax_bot.scatter([ex], [chosen_ey * 0.84 if abs(chosen_bx - ex) > 1e-3 else chosen_ey], color=ev_col, s=16, alpha=0.72, zorder=6)
            chosen_artist = ax_bot.text(
                chosen_bx, chosen_ey * 1.08, lbl_str,
                ha="center", va="bottom", fontsize=5.0,
                fontweight="bold", color=txt_ev, linespacing=1.03,
                bbox=dict(boxstyle="round,pad=0.06", facecolor=bg_ev, edgecolor=ev_col, linewidth=0.75, alpha=0.95),
                zorder=8
            )
            placed_boxes_by_label[f"{erow['date_str']}: {erow['event_label']}"] = chosen_artist
    print(f"  -> Placed {placed_count}/{len(df_events)} small historical news events on bottom timeline without overlap")

    # 3. Draw TRL Maturation & Lineage Connecting Lines with Single-Shaft Display-Straight Arrows
    fig.canvas.draw()
    inv_data = ax_bot.transData.inverted()

    def _find_placed_artist(substr_q):
        for full_k, art in placed_boxes_by_label.items():
            if substr_q in full_k:
                return art
        return None

    def _ray_rect_exit_t(p1, p2, bb, pad_px=2.0):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        x0, y0, x1, y1 = bb.x0 - pad_px, bb.y0 - pad_px, bb.x1 + pad_px, bb.y1 + pad_px
        tx = ((x1 - p1[0]) / dx if dx > 0 else (x0 - p1[0]) / dx) if abs(dx) > 1e-6 else float("inf")
        ty = ((y1 - p1[1]) / dy if dy > 0 else (y0 - p1[1]) / dy) if abs(dy) > 1e-6 else float("inf")
        return max(0.0, min(1.0, min(tx, ty)))

    for chain_name, chain_col, c_nodes in trl_chains:
        chain_artists = []
        for substr_k, _ in c_nodes:
            art = _find_placed_artist(substr_k)
            if art is not None:
                chain_artists.append(art)
        if len(chain_artists) < 2:
            continue

        bboxes_px = [art.get_window_extent(renderer=renderer) for art in chain_artists]

        for i in range(len(bboxes_px) - 1):
            bb1, bb2 = bboxes_px[i], bboxes_px[i + 1]
            p1 = np.array([0.5 * (bb1.x0 + bb1.x1), 0.5 * (bb1.y0 + bb1.y1)])
            p2 = np.array([0.5 * (bb2.x0 + bb2.x1), 0.5 * (bb2.y0 + bb2.y1)])
            t_exit1 = _ray_rect_exit_t(p1, p2, bb1, pad_px=1.5)
            t_exit2_rev = _ray_rect_exit_t(p2, p1, bb2, pad_px=2.5)
            t_enter2 = 1.0 - t_exit2_rev

            if t_enter2 > t_exit1 + 0.03:
                p_start = p1 + t_exit1 * (p2 - p1)
                p_end = p1 + t_enter2 * (p2 - p1)
            else:
                p_start = p1
                p_end = p2

            # Sample 24 points linearly in display space so segment is perfectly straight on log-Y axis
            ts_lin = np.linspace(0.0, 1.0, 24)
            pts_px = np.outer(1.0 - ts_lin, p_start) + np.outer(ts_lin, p_end)
            pts_data = inv_data.transform(pts_px)
            ax_bot.plot(pts_data[:, 0], pts_data[:, 1], color="white", linestyle="-", linewidth=3.4, alpha=0.85, zorder=7.1)
            ax_bot.plot(pts_data[:, 0], pts_data[:, 1], color=chain_col, linestyle="-", linewidth=1.85, alpha=0.88, zorder=7.3)

            if t_enter2 > t_exit1 + 0.03:
                d_tail = pts_data[-3]
                d_head = pts_data[-1]
                arr_patch = mpatches.FancyArrowPatch(
                    d_tail, d_head,
                    arrowstyle="-|>,head_length=5.5,head_width=3.5",
                    color=chain_col, linewidth=1.85, alpha=0.95, zorder=9.2
                )
                ax_bot.add_patch(arr_patch)

    # -------------------------------------------------------------------------
    # PANEL 4: BOTTOM-RIGHT CELL ANATOMY & FIELD GUIDE
    # -------------------------------------------------------------------------
    ax_corner.set_facecolor("#F4F1EA")
    ax_corner.set_xlim(0.0, 1.0)
    ax_corner.set_ylim(0.0, 1.0)
    ax_corner.set_xticks([])
    ax_corner.set_yticks([])
    for spine in ax_corner.spines.values():
        spine.set_linewidth(2.0)
        spine.set_edgecolor("#222222")

    ax_corner.add_patch(mpatches.Rectangle((0.0, 0.84), 1.0, 0.16, facecolor="#1B2631", edgecolor="none", zorder=1))
    ax_corner.text(0.50, 0.94, "HOW TO READ EACH CELL", ha="center", va="center", fontsize=18.5, fontweight="bold", color="white", zorder=2)
    ax_corner.text(0.50, 0.872, "www.arianprabowo.com", ha="center", va="center", fontsize=13.0, fontweight="bold", color="#F0E442", zorder=2)

    cell_guide_text = (
        "Each cell maps AI usage at one Generation and Skill Level.\n"
        "Below the title, telemetry bar (task tokens, cost $, energy\n"
        "Wh, human/AI time, and User/Token/Spend % share), and\n"
        "2-line summary sits a 3x2 table above a 2-line keyword footer:\n"
        "• Extended Summary: Expands on the 2-line summary by weaving\n"
        "  in and defining the cell's core vocabulary in context.\n"
        "• Use Cases & Landmarks: Practical tasks solved alongside\n"
        "  historic launches, papers, demos, or incidents.\n"
        "• User Actions: Hands-on steps taken by the human—from\n"
        "  clicks and prompts (L1) to coding, tuning & math (L2–L6).\n"
        "• Models & Products: Neural weights and engines paired\n"
        "  with commercial apps, APIs, SDKs, and benchmarks.\n"
        "• Surface & Hardware: The workspace interface (browser,\n"
        "  IDE, CLI) and the device or GPU cluster running it.\n"
        "• Scope & Evolution: How this cell connects to adjacent\n"
        "  cells—what it absorbed (left), when to step down a\n"
        "  level (below), and what sinks to a simpler level (right)."
    )
    ax_corner.text(0.032, 0.818, cell_guide_text, ha="left", va="top", fontsize=11.7, color="#111111", linespacing=1.21, zorder=3)

    out_path = os.path.join(FIG_DIR, "fig_v4_p0_encyclopedic_megachart_poster.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED MEGACHART POSTER] {out_path}")


def render_plot0_mini_megachart(data):
    _render_megachart_common(data, is_full_poster=False)


# ==============================================================================
# PLOT 1: MACRO RESOURCE TRAJECTORIES
# ==============================================================================
def render_plot1_macro_trajectories(data):
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

    out_path = os.path.join(FIG_DIR, "fig_v4_p1_macro_resource_trajectories.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


# ==============================================================================
# PLOT 2: SKILL DEFLATION ESCALATOR
# ==============================================================================
def render_plot2_skill_deflation(data):
    df_bench = data["bench"]
    gen_x = np.array([2018.9, 2021.6, 2023.6, 2024.65, 2025.9])
    hour_cols = ["G0_hours", "G1_hours", "G2_hours", "G3_hours", "G4_hours"]

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
        ax.plot(gen_x, y_vals, color=C_DEMAND, alpha=0.45, linewidth=1.8, marker=markers[idx % len(markers)], zorder=2, label=f"{row['workflow_name']} (-{row['total_hours_saved']}h)")

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

    out_path = os.path.join(FIG_DIR, "fig_v4_p2_skill_deflation_escalator.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


# ==============================================================================
# PLOT 3: PUBLISHED AI LADDER CORPUS & GEN BREAKS (6-LEVEL RASTER)
# ==============================================================================
def render_plot3_folksonomy_raster(data):
    df_lad = data["ladders"]
    fig, ax = plt.subplots(figsize=(14.5, 8.2), dpi=300)
    fig.subplots_adjust(left=0.14, right=0.97, bottom=0.11, top=0.88)
    fig.suptitle("Plot 3: Published AI Ladder Corpus (2017–2026): Descriptive Bottom Rungs (L1–L3) vs. Speculative Top Rungs (L4–L6)", fontsize=12, fontweight="bold", y=0.96)

    t_grid = np.linspace(2017.42, 2026.83, 113)
    y_grid = np.arange(0.5, 7.0, 1.0)
    Z = np.zeros((6, len(t_grid) - 1))
    for r in range(6):
        for c in range(len(t_grid) - 1):
            if r < 3:
                Z[r, c] = 0.25 + 0.10 * r
            else:
                Z[r, c] = 0.75 + 0.08 * (r - 3)

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

    out_path = os.path.join(FIG_DIR, "fig_v4_p3_folksonomy_and_gen_breaks.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


# ==============================================================================
# PLOT 4: TASK COST VS. LEARNING HOURS JOINTPLOT (30 EMPIRICAL CELLS G0-L1..G4-L6)
# ==============================================================================
def render_plot4_jointplot(data):
    df_cells = data["cells"]
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

    out_path = os.path.join(FIG_DIR, "fig_v4_p4_task_cost_vs_learning_jointplot.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


# ==============================================================================
# PLOTS 5-9: GENERATION-SPECIFIC 6-LEVEL MATRICES (G0 TO G4)
# ==============================================================================
def render_plots5_to_9_gen_matrices(data):
    df_cells = data["cells"]
    df_gens = data["gens"]

    gen_plot_map = [
        ("G0", 5, "fig_v4_p5_gen0_matrix.png"),
        ("G1", 6, "fig_v4_p6_gen1_matrix.png"),
        ("G2", 7, "fig_v4_p7_gen2_matrix.png"),
        ("G3", 8, "fig_v4_p8_gen3_matrix.png"),
        ("G4", 9, "fig_v4_p9_gen4_matrix.png"),
    ]

    for gen_id, pnum, fname in gen_plot_map:
        sub = df_cells[df_cells["gen_id"] == gen_id].sort_values("level_id")
        gen_row = df_gens[df_gens["gen_id"] == gen_id].iloc[0]

        fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(17.2, 8.2), dpi=300, sharey=True)
        fig.subplots_adjust(left=0.20, right=0.97, bottom=0.11, top=0.82, wspace=0.08)
        fig.suptitle(f"Plot {pnum}: {gen_row['gen_folksonomy_name']} ({gen_row['start_date']} to {gen_row['end_date']}) — 6-Level Breakdown", fontsize=12, fontweight="bold", y=0.96)

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
def render_plot10_alluvial_poster(data):
    df_cells = data["cells"]
    df_gens = data["gens"]

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
        hdr_txt = f"{gid} ({grow['duration_months']}m)\n{grow['macro_tokens_trillions']}T | ${grow['macro_spend_billion_usd']}B" if gid == "G3" else f"{gid} ({grow['start_date']}..{grow['end_date']})\n{grow['duration_months']} mos | {grow['macro_tokens_trillions']}T tok | ${grow['macro_spend_billion_usd']}B"
        ax.text(xc, y_hdr, hdr_txt, ha="center", va="top", fontsize=7.8 if gid == "G3" else 8.4, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.20", facecolor="#EFEFEF", edgecolor="#888888"))

    short_b_map = {
        1: "0h | $0",
        2: "<50h | <$30",
        3: "<200h | <$100",
        4: "~600h | ~$1.5k",
        5: "~2,000h | ~$500k",
        6: "~10,000h | ~$100M+",
    }
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

    out_path = os.path.join(FIG_DIR, "fig_v4_p10_alluvial_evolution_poster.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


# ==============================================================================
# PLOT 11: ON-LADDER TRL 1-9 MATURATION & FAILED HOPES (ZERO TRL_04/TRL_07 COLLISION)
# ==============================================================================
def render_plot11_trl_and_hopes(data):
    df_trl = data["trl"]
    fig = plt.figure(figsize=(16.5, 7.5), dpi=300)
    gs = gridspec.GridSpec(1, 3, figure=fig, width_ratios=[3.2, 0.7, 2.8], wspace=0.14, left=0.13, right=0.97, bottom=0.11, top=0.82)
    ax_l = fig.add_subplot(gs[0, 0])
    ax_m = fig.add_subplot(gs[0, 1], sharey=ax_l)
    ax_r = fig.add_subplot(gs[0, 2])

    fig.suptitle("Plot 11: On-Ladder TRL 1–9 Maturation Trajectories (L6 Genesis to L1 Default) & Population Evolution of Hopes", fontsize=12, fontweight="bold", y=0.96)

    def ym_to_float(ym_str):
        ym = ym_str.split(" ")[0]
        y, m = map(int, ym.split("-"))
        return y + (m - 0.5) / 12.0

    rng = np.random.default_rng(42)
    perm = rng.permutation(len(df_trl))
    all_trl_points = []
    # Distinct vertical & horizontal offsets so TRL_04 (2024-05) and TRL_07 (2024-06) NEVER collide!
    trl_label_pos = {
        "TRL_01": (0.0,  9.12),
        "TRL_02": (0.0,  9.12),
        "TRL_03": (0.0,  9.12),
        "TRL_04": (-0.28, 9.08),
        "TRL_05": (0.0,  9.35),
        "TRL_06": (0.0,  9.58),
        "TRL_07": (0.28, 9.26),
        "TRL_08": (0.0,  9.42),
        "TRL_09": (-0.22, 9.10),
        "TRL_10": (0.22, 9.58),
    }
    for idx in perm:
        row = df_trl.iloc[idx]
        xs = [ym_to_float(row["trl_1_3_l6_genesis_date"]), ym_to_float(row["trl_4_5_proto_date_level"]),
              ym_to_float(row["trl_7_power_date_level"]), ym_to_float(row["trl_9_builtin_l1_date"])]
        ys = [2.0, 4.5, 7.0, 9.0]
        all_trl_points.extend(ys)
        ax_l.plot(xs, ys, color=C_SUPPLY, alpha=0.38, linewidth=1.6, marker="o", zorder=2)
        dx, y_targ = trl_label_pos.get(row["trl_id"], (0.0, 9.12))
        ax_l.annotate(
            row["trl_id"], (xs[-1] + dx, y_targ),
            fontsize=7.2, fontweight="bold", ha="center", color="#222222"
        )

    mean_x = np.linspace(2018.5, 2025.5, 50)
    mean_y = 2.0 + 7.0 * ((mean_x - 2018.5) / (2025.5 - 2018.5))**0.85
    ax_l.plot(mean_x, mean_y, color=C_ACTUAL, linewidth=3.0, zorder=5, label="Parametric Mean TRL Maturation Curve (Lag μ = 36.2 mos)")

    apply_calendar_grid(ax_l, 2017.4, 2026.85)
    ax_l.set_ylim(1.0, 9.85)
    ax_l.set_yticks([2.0, 4.5, 7.0, 9.0])
    ax_l.set_yticklabels(["TRL 1–3\n(L6 Genesis)", "TRL 4–5\n(L4–L5 Proto)", "TRL 7\n(L2–L3 Power)", "TRL 9\n(Built-In L1)"], fontsize=8.5, fontweight="bold")
    ax_l.set_xlabel("Calendar Time (2017–2026)", fontsize=9.5, fontweight="bold")
    ax_l.set_ylabel("On-Ladder Technology Readiness Level (TRL 1–9)", fontsize=9.5, fontweight="bold")
    ax_l.legend(loc="lower right", frameon=False, fontsize=8.0)

    ax_m.hist(all_trl_points, bins=[1.0, 3.2, 5.8, 8.0, 9.8], orientation="horizontal", histtype="step", fill=False, linewidth=1.8, color=C_SUPPLY)
    ax_m.set_xlim(0.0, 13.0)
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

    out_path = os.path.join(FIG_DIR, "fig_v4_p11_trl_and_failed_hopes.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


# ==============================================================================
# PLOT 12: 20-LADDER PAIRWISE MATRIX (ZERO OVERLAP, NO STRAY 4.2 TICK)
# ==============================================================================
def render_plot12_pair_plot(data):
    df_lad = data["ladders"].copy()
    cols = ["scope_coverage", "user_skill_alignment", "historical_invariance", "empirical_cost_grounding"]
    labels = ["Scope Coverage", "User-Skill Align", "Hist. Invariance", "Cost Grounding"]

    fig = plt.figure(figsize=(14, 12), dpi=300)
    gs = gridspec.GridSpec(4, 4, figure=fig, left=0.08, right=0.96, bottom=0.07, top=0.88, wspace=0.14, hspace=0.14)
    fig.suptitle("Plot 12: Published AI Ladders (2017–2026): Tri-Partite Pairwise Alignment Matrix", fontsize=13, fontweight="bold", y=0.96)

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
                # Placed at y=3.75 with manage_ticks=False so there is NO stray 4.2 tick and ZERO overlap with upper-left stats box!
                ax.boxplot(
                    x_data, vert=False, positions=[3.75], widths=0.55,
                    manage_ticks=False, patch_artist=True,
                    boxprops=dict(facecolor=C_ACTUAL, alpha=0.35),
                    medianprops=dict(color="#111111", linewidth=1.6)
                )
                stats_txt = f"μ={mu:.2f} | Med={q2:.2f}\nMin={x_data.min():.2f} | Max={x_data.max():.2f}\nQ1={q1:.2f} | Q3={q3:.2f} | IQR={iqr:.2f}"
                ax.text(
                    0.03, 0.96, stats_txt, transform=ax.transAxes, va="top", ha="left", fontsize=7.1,
                    bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.92, edgecolor="#CCCCCC")
                )
                ax.set_xlim(0.35, 1.02)
                ax.set_ylim(0.0, 6.4)
                ax.set_yticks([0, 2, 4, 6])
            elif i > j:
                ax.scatter(x_data[perm], y_data[perm], color=C_SUPPLY, alpha=0.70, s=55, edgecolors="#111111", zorder=3)
                ax.scatter([1.0], [1.0], color=C_DEMAND, marker="*", s=140, zorder=5, label="v4 6×6 Ladder")
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
        plt.Line2D([0], [0], color=C_SUPPLY, marker="o", linestyle="None", markersize=7, label="20 Literature Ladders"),
        plt.Line2D([0], [0], color=C_DEMAND, marker="*", linestyle="None", markersize=10, label="Our v4 6×6 (Gen × Level) Ladder"),
        plt.Line2D([0], [0], color="#000000", linestyle="--", linewidth=1.8, label="OLS Linear Fit"),
        plt.Line2D([0], [0], color=C_DEMAND, linestyle="--", linewidth=1.8, label="Parametric Mean (μ)"),
    ]
    fig.legend(handles=handles, loc="center", bbox_to_anchor=(0.5, 0.92), ncol=4, frameon=False, fontsize=9.5)

    out_path = os.path.join(FIG_DIR, "fig_v4_p12_ladder_comparison_matrix.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


# ==============================================================================
# PLOT 13: ANIMATED 6-LEVEL TRAJECTORY GIF (112 FRAMES)
# ==============================================================================
def render_plot13_animation(data):
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

    df_cells = data["cells"]
    t_slices = np.linspace(2017.42, 2026.83, N_render)
    global_tok_curve = 0.05 * np.exp(0.98 * (t_slices - 2017.42))

    frames_pil = []
    fig = plt.figure(figsize=(10, 6.5), dpi=105)
    gs = gridspec.GridSpec(2, 1, figure=fig, height_ratios=[4, 1], hspace=0.22, left=0.10, right=0.96, bottom=0.10, top=0.90)
    ax_main = fig.add_subplot(gs[0, 0])
    ax_scrub = fig.add_subplot(gs[1, 0])

    for f_idx in range(N_render):
        t_cur = t_slices[f_idx]
        if t_cur < 2020.42:
            cur_gen = "G0"
        elif t_cur < 2022.83:
            cur_gen = "G1"
        elif t_cur < 2024.33:
            cur_gen = "G2"
        elif t_cur < 2025.00:
            cur_gen = "G3"
        else:
            cur_gen = "G4"

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

        ax_main.set_title(f"Plot 13: AI 6-Level Ladder Evolution Trajectory | Time={t_cur:.2f} ({cur_gen})", fontsize=11, fontweight="bold")
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
    out_gif = os.path.join(FIG_DIR, "fig_v4_p13_ladder_evolution_anim.gif")
    frames_pil[0].save(out_gif, save_all=True, append_images=frames_pil[1:], duration=int(1000 / ANIMATION_FPS), loop=0)
    print(f"[RENDERED ANIMATION] {out_gif} | frames={len(frames_pil)}")


# ==============================================================================
# PLOT 14: SPECULATIVE GEN 5 (6-LEVEL) MATRIX & DUAL CUTOFFS
# ==============================================================================
def render_plot14_gen5_speculative_matrix(data):
    sub = data["gen5_cells"].sort_values("level_id")
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

    out_path = os.path.join(FIG_DIR, "fig_v4_p14_gen5_speculative_matrix.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


def render_all_plots():
    data = build_and_verify_all()
    render_plot0_mini_megachart(data)
    render_plot0_encyclopedic_megachart_poster(data)
    render_visual_abstracts(data)
    render_plot1_macro_trajectories(data)
    render_plot2_skill_deflation(data)
    render_plot3_folksonomy_raster(data)
    render_plot4_jointplot(data)
    render_plots5_to_9_gen_matrices(data)
    render_plot10_alluvial_poster(data)
    render_plot11_trl_and_hopes(data)
    render_plot12_pair_plot(data)
    render_plot13_animation(data)
    render_plot14_gen5_speculative_matrix(data)
    print("\n[ALL V4 VISUAL ARTIFACTS (PLOT 0, PLOT 0-MINI, VA0-VA5, PLOT 1-PLOT 14) RENDERED SUCCESSFULLY]")


if __name__ == "__main__":
    render_all_plots()
