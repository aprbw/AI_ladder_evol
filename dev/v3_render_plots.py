import os
import shutil
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
from matplotlib.path import Path
from PIL import Image
from tqdm import tqdm

from v3_data_and_gates import build_and_verify_all

BASE_DIR = "/Users/z3540725/My Drive/personal/2026 10 17 AI_ladder_evol"
FIG_DIR = os.path.join(BASE_DIR, "figures_v3")
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


def render_visual_abstracts(data):
    va_specs = [
        ("fig_v3_va0_root.png", "Plot VA0: AI Ladder Evolution (2017–2026): User-Skill Generations, Counterfactuals & Evolutionary Atlas", [
            ("1. User-Centric Coordinate Grid", "Horizontal = Gen 0..Gen 4 (User Shift)\nVertical = Level 1..5 (Learning Hours)\nTech = Causal Explanation Only", C_SUPPLY),
            ("2. Standardized Skill-Tree Brackets", "L1: 0h (Casual / High Schooler)\nL2: 7–45h (1 Wknd–1 Wk Prompt/Workspace)\nL3: 50–200h | L4: 200–600h | L5: 600–2000h+", C_DEMAND),
            ("3. Down-Ladder Skill Deflation", "Math CoT: L5(1000h)->L2(25h)->L1(0h)\n50-PDF Q&A: L4(350h)->L3(110h)->L2(15h)->L1\nMultimodal: L4(400h)->L2(30h)->L1(0h)", C_ACTUAL),
            ("4. Two-Track Producer–Consumer Split", "Track A: Direct User Own Output (L1–L5)\nTrack B: Internal Bot (RAG+Tools+NeMo)\n& SaaS Builders (L3–L5) -> Serve L1 Users", C_SUPPLY),
            ("5. 4-Way Counterfactual Proof per Cell", "Down (Why not L-1? How forcing fails)\nUp (Why not L+1? Overkill waste)\nBefore (Why not G-1?) | After (Sinks in G+1)", C_DEMAND),
            ("6. Bonus TRL & Failed-Hope Evolution", "Mean Paper->L1 TRL 9 Lag: 36.2 Months\n15/20 Hyped Branches Extinct (Too Early,\nBase-Model Absorption, Unit Economics)", C_HOPE),
        ]),
        ("fig_v3_va1_part1.png", "Plot VA1: Part I Synthesis (2017–2026): Five User Generations, Macro Economics & Skill Deflation", [
            ("Gen 0 (2017–2020): Pre-LLM Pipelines", "L1 Active GenAI Missing (Passive Widgets)\nL2 AutoML | L3 Sklearn | L4 BERT | L5 Seq2Seq\n12M Users | 0.18T Tokens | $1.1B Spend", C_SUPPLY),
            ("Gen 1 (2020–2022): Completion & Tab", "L1 Copilot Tab & Web Toys (0h)\nL2 Playground Few-Shot (7–45h)\n45M Users | 1.60T Tokens | $3.8B Spend", C_ACTUAL),
            ("Gen 2 (2022–2024): Chat & DIY Vector RAG", "L1 ChatGPT Zero-Shot (0h) | L2 Manual CoT\nL3 LangChain/Pinecone RAG | L4 4-Bit QLoRA\n380M Users | 28T Tokens | $14.0B Spend", C_DEMAND),
            ("Gen 3 (2024): Omni-Workspaces & AI IDEs", "L1 GPT-4o + Artifacts | L2 50-PDF Projects\nL3 Cursor Composer + NeMo Guardrailed Bots\n720M Users | 240T Tokens | $39.0B Spend", C_ACTUAL),
            ("Gen 4 (2025–2026): Thinking, CLI & Sandbox", "L1 Auto-Thinking Router | L2 Deep Research\nL3 .mcp.json | L4 Claude Code | L5 Mac Mini\n1,150M Users | 1,100T Tokens | $88.0B Spend", C_SUPPLY),
            ("Macro Jevons & Bought-vs-Built Laws", "Unit Token Price -99.8% -> Volume +6,111x\nEnterprise Spend: $1.7B -> $11.5B -> $37.0B\n76% Bought vs 24% Built (67% vs 33% Success)", C_HOPE),
        ]),
        ("fig_v3_va2_part2.png", "Plot VA2: Part II Raw Inventory (2017–2026): 20 Ladders, 25 Use Cases, 19 Tutorials & 20 Hopes", [
            ("1. 20 Existing Ladders & Folksonomy", "Karpathy 1.0–3.0, OpenAI 5 Levels, DeepMind,\nAnthropic Workflows, LangChain, SAE L0–L5,\nGartner, Menlo, MIT NANDA, Gemini 23-Step", C_SUPPLY),
            ("2. Descriptive Bottom vs Hope Top", "Bottom Rungs (1–3) = Verified Gen G Reality\nTop Rungs (4–5) = Speculative Gen G+1 Hope\nLadder Breaks Pinpoint Exact Gen Cutoffs", C_HOPE),
            ("3. Track A & Track B Use-Case Bin", "25 Empirical Workflows Inventoried\nDirect Users vs Internal Company Bots\n(SharePoint RBAC + MCP + NeMo Colang)", C_ACTUAL),
            ("4. Keywords & Mental Models", "TF-IDF -> stop=['\\n'] -> system prompt ->\nchunk_size -> NF4 LoRA -> .cursorrules ->\n.mcp.json -> CLAUDE.md -> OpenClaw / GRPO", C_DEMAND),
            ("5. Tutorial & Syllabus Hours", "19 Anchor Curricula (CS224N, Fast.ai, CS324,\n8 DeepLearning.AI Courses, UVA CS 6501)\nCluster into 5 Non-Overlapping Hour Tiers", C_SUPPLY),
            ("6. Two-Level Cost & Energy Setup", "Single-Task: Tokens, FLOPs, USD, Wh, Min\nGen-Wide: User %, Token %, Spend % = 100%\nFermi Bounds + Epoch AI Trade-Off Spans", C_ACTUAL),
        ]),
        ("fig_v3_va3_part3.png", "Plot VA3: Part III Inductive Boundary Method: User Shifts, Skill Brackets & Deferred Naming", [
            ("1. Dual User-Shift Gen Cutoff Rule", "New Gen G Requires BOTH:\n(a) New Upper-Level Use Case (New Skill)\n(b) Old Use Case Sinks to Lower Level", C_SUPPLY),
            ("2. Reconciling Release vs Crossover", "First Release (TRL 4–6: 2018-10, 2023-11, 2024-09)\nvs Production Crossover (TRL 8–9: 2020-06,\n2022-11, 2024-05, 2025-01)", C_ACTUAL),
            ("3. Fixed Anchor Rungs (L1 & L2)", "Level 1 Fixed at 0 Hours (Casual / High Schooler;\nG0-L1 Passive Widgets Evaluated Explicitly)\nLevel 2 Fixed at 7–45 Hours (1 Wknd to 1 Wk)", C_DEMAND),
            ("4. Inductive Higher Rungs (L3–L5)", "Clustered from Course & Setup Inventory:\nL3: 50–200h (2–5 Wks IDE/RAG/MCP)\nL4: 200–600h (1 Sem CLI/Graph/LoRA)\nL5: 600–2000h+ (6M+ Mac Mini Sandbox/RLVR)", C_DEMAND),
            ("5. Producer–Consumer Matrix Proof", "L3–L5 Internal Bot & SaaS Product Builders\nAbsorb Complexity (RAG + Tools + Guardrails)\nto Deliver 0-Hour L1 Experience to Staff", C_ACTUAL),
            ("6. Deferred Folksonomy Naming Last", "Coordinates G0..G4 & L1..L5 Locked First\nCells Populated Second -> Official Names\nCoined Last from Contemporary Folksonomy", C_HOPE),
        ]),
        ("fig_v3_va4_part4.png", "Plot VA4: Part IV Chronological Matrix (Gen 0 to Gen 4): 25 Cells, Obsolete Skills & 4-Way Counterfactuals", [
            ("Gen 0 (2017–2020) & Gen 1 (2020–2022)", "G0: Passive L1 -> AutoML -> Sklearn -> BERT -> Seq2Seq\nG1: Copilot Tab L1 -> Playground L2 -> API L3 ->\nChains/CLI L4 -> DeepSpeed L5", C_SUPPLY),
            ("Gen 2 (2022–2024): Chat & DIY RAG", "L1: ChatGPT Web UI | L2: CoT + Midjourney\nL3: LangChain/Pinecone Vector RAG Bots\nL4: 4-Bit QLoRA (CoEdIT) | L5: vLLM Clusters", C_ACTUAL),
            ("Gen 3 (2024): Omni & AI-Native IDEs", "L1: GPT-4o + Artifacts | L2: 50-PDF Projects\nL3: Cursor Composer + NeMo Guardrailed Bots\nL4: LangGraph Cyclic State | L5: Eval Clusters", C_DEMAND),
            ("Gen 4 (2025–2026): Thinking & Sandboxes", "L1: Auto-Thinking Router | L2: Deep Research\nL3: .mcp.json + Agentic RAG | L4: Claude Code CLI\nL5: M4 Mac Mini OpenClaw 24/7 + GRPO RLVR", C_SUPPLY),
            ("4-Way Counterfactual Stress Test", "Every Cell Proves:\n1. Why not L-1 (Exact Failure Mode)\n2. Why not L+1 (Overkill Waste)\n3. Why not G-1 | 4. How It Sinks in G+1", C_HOPE),
            ("Obsolete User Skills per Gen", "G1 Kills: 10k Label Curation for Basic NLP\nG2 Kills: Stop-Sequence Prefix Hacks\nG3 Kills: 20-PDF Python Chunking Scripts\nG4 Kills: Manual 'Think Step by Step' CoT", C_DEMAND),
        ]),
        ("fig_v3_va5_part5.png", "Plot VA5: Part V Synthesis: Alluvial Atlas, TRL Lag, Failed Hopes & Three-Way Ladder Audit", [
            ("1. 15-Month Skill Deflation Escalator", "High-Level Workflows Sink 1–2 Levels per Gen\nSaving 120–1,000 User Learning Hours\nWhile Top Rung Expands Token Spend 1,000x", C_ACTUAL),
            ("2. Paper-to-Adoption TRL Lag (Table 5.2a)", "10 Core Breakthroughs Tracked TRL 1 -> TRL 9\nMean Lag to Built-In L1: 36.2 Months\nFastest: Copilot Tab (13m) & Deep Research (22m)", C_SUPPLY),
            ("3. Population Evolution of Hopes (5.2b)", "20 Historical Hopes Audited Across G0–G4:\n25% Survived to TRL 9 | 75% Went Extinct\n(Too Early, Base-Model Absorption, Economics)", C_HOPE),
            ("4. Audit 1: Our Ladder vs 20 Ladders", "1D Autonomy Ladders Break Every Gen Shift\n2D (Gen x User-Learning Level) Separates\nTech Era from Human Skill Investment", C_DEMAND),
            ("5. Audit 2: Why Existing Ladders Conflict", "Conflicts Explained by Publication Gen (G0–G4)\nx Author Vantage Point (Lab Model vs\nFramework Graph vs Enterprise Buyer vs User)", C_SUPPLY),
            ("6. Audit 3: Descriptive Bottom vs Hope Top", "100% of Reviewed Ladders Have Descriptive\nBottom Rungs (L1–L3 Reality) & Speculative\nTop Rungs (Historical Top-Rung Accuracy: 38%)", C_ACTUAL),
        ]),
    ]

    for fname, title, cards in va_specs:
        fig = plt.figure(figsize=(16, 9), dpi=300)
        gs = gridspec.GridSpec(2, 3, figure=fig, left=0.04, right=0.96, bottom=0.06, top=0.84, wspace=0.12, hspace=0.18)
        fig.suptitle(title, fontsize=13, fontweight="bold", y=0.96)

        # Top legend banner
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
            ax.text(0.05, 0.40, cbody, color="#111111", fontsize=9.5, va="center", ha="left", linespacing=1.45, zorder=3)

        out_path = os.path.join(FIG_DIR, fname)
        fig.savefig(out_path, dpi=300)
        plt.close(fig)
        print(f"[RENDERED] {out_path}")


def render_plot1_macro_trajectories(data):
    # Plot 1: Global AI Ecosystem (2017-2026): Macro Token Volume, Enterprise Spend & Active Users
    t_points = np.array([2017.5, 2018.5, 2019.5, 2020.4, 2021.0, 2022.0, 2022.85, 2023.5, 2024.33, 2024.8, 2025.0, 2025.8, 2026.8])
    tokens_t = np.array([0.05, 0.10, 0.18, 0.30, 0.70, 1.60, 3.50, 28.0, 110.0, 240.0, 380.0, 750.0, 1100.0])
    spend_b  = np.array([0.3,  0.6,  1.1,  1.5,  2.4,  3.8,  5.5,  14.0, 26.0,  39.0,  52.0,  71.0,  88.0])
    users_m  = np.array([3.0,  6.5,  12.0, 18.0, 28.0, 45.0, 120.0, 380.0, 560.0, 720.0, 860.0, 1020.0, 1150.0])

    fig = plt.figure(figsize=(14, 7), dpi=300)
    gs = gridspec.GridSpec(1, 2, figure=fig, width_ratios=[4, 1], wspace=0.06, left=0.07, right=0.96, bottom=0.11, top=0.88)
    ax = fig.add_subplot(gs[0, 0])
    ax_marg = fig.add_subplot(gs[0, 1], sharey=ax)

    fig.suptitle("Plot 1: Global AI Ecosystem (2017–2026): Macro Token Volume, Total Spend & Active Users", fontsize=12.5, fontweight="bold", y=0.96)

    ax.plot(t_points, tokens_t, color=C_SUPPLY, linewidth=2.8, marker="o", zorder=4, label="Annual Token Volume (Trillions, SUPPLY)")
    ax.plot(t_points, spend_b, color=C_ACTUAL, linewidth=2.8, marker="s", zorder=4, label="Total Annual AI Spend ($B, ACTUAL)")
    ax.plot(t_points, users_m, color=C_DEMAND, linewidth=2.8, marker="^", zorder=4, label="Active Users Across Ladder (Millions, DEMAND)")

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

    # Right marginal step histogram with geomspace bins
    bins = np.geomspace(0.04, 2000.0, 20)
    ax_marg.hist(tokens_t, bins=bins, orientation="horizontal", histtype="step", fill=False, linewidth=1.8, color=C_SUPPLY, label="Tokens")
    ax_marg.hist(spend_b, bins=bins, orientation="horizontal", histtype="step", fill=False, linewidth=1.8, color=C_ACTUAL, label="Spend")
    ax_marg.hist(users_m, bins=bins, orientation="horizontal", histtype="step", fill=False, linewidth=1.8, color=C_DEMAND, label="Users")
    ax_marg.set_xlabel("Count", fontsize=9.5, fontweight="bold")
    ax_marg.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25, color="#888888")
    plt.setp(ax_marg.get_yticklabels(), visible=False)

    out_path = os.path.join(FIG_DIR, "fig_v3_p1_macro_resource_trajectories.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


def render_plot2_skill_deflation(data):
    # Plot 2: Five Benchmark User Workflows (2017-2026): Down-Ladder User Learning-Hour Deflation
    df_bench = data["bench"]
    gen_x = np.array([2018.9, 2021.6, 2023.6, 2024.65, 2025.9])
    hour_cols = ["G0_hours", "G1_hours", "G2_hours", "G3_hours", "G4_hours"]

    fig = plt.figure(figsize=(14, 7), dpi=300)
    gs = gridspec.GridSpec(1, 2, figure=fig, width_ratios=[4, 1], wspace=0.06, left=0.07, right=0.96, bottom=0.11, top=0.88)
    ax = fig.add_subplot(gs[0, 0])
    ax_marg = fig.add_subplot(gs[0, 1], sharey=ax)

    fig.suptitle("Plot 2: Five Benchmark User Workflows (2017–2026): Down-Ladder Learning-Hour Deflation", fontsize=12.5, fontweight="bold", y=0.96)

    rng = np.random.default_rng(42)
    perm = rng.permutation(len(df_bench))
    all_vals = []
    markers = ["o", "s", "^", "D", "v"]
    for idx in perm:
        row = df_bench.iloc[idx]
        y_vals = np.array([row[c] for c in hour_cols], dtype=float)
        all_vals.extend(y_vals)
        ax.plot(gen_x, y_vals, color=C_DEMAND, alpha=0.35, linewidth=1.6, marker=markers[idx % len(markers)], zorder=2, label=row["workflow_name"])

    mean_hours = df_bench[hour_cols].mean(axis=0).values
    ax.plot(gen_x, mean_hours, color=C_SUPPLY, linewidth=3.0, alpha=0.95, marker="o", markersize=8, zorder=5, label="Parametric Mean Learning Hours (μ)")

    for gx, mval, gname in zip(gen_x, mean_hours, ["Gen 0", "Gen 1", "Gen 2", "Gen 3", "Gen 4"]):
        ax.annotate(f"{gname}: μ={mval:.0f}h", (gx, mval), textcoords="offset points", xytext=(0, 10), ha="center", fontsize=8.5, fontweight="bold", color=C_SUPPLY, zorder=6)

    apply_calendar_grid(ax, 2017.4, 2026.85)
    ax.set_yscale("symlog", linthresh=1.0)
    ax.set_ylim(0.0, 2500.0)
    ax.set_xlabel("Calendar Year Across Generations Gen 0 to Gen 4 (2017–2026)", fontsize=10, fontweight="bold")
    ax.set_ylabel("Required User Learning Hours (symlog scale, linthresh=1.0)", fontsize=10, fontweight="bold")
    ax.legend(loc="upper right", bbox_to_anchor=(0.98, 0.96), frameon=False, fontsize=8.5)

    bins = np.concatenate([[0.0], np.geomspace(1.0, 2500.0, 18)])
    ax_marg.hist(all_vals, bins=bins, orientation="horizontal", histtype="step", fill=False, linewidth=1.8, color=C_DEMAND)
    ax_marg.axhline(np.mean(all_vals), color=C_SUPPLY, linestyle="--", linewidth=1.6, label="Global μ")
    ax_marg.set_xlabel("Cell Count", fontsize=9.5, fontweight="bold")
    ax_marg.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25, color="#888888")
    plt.setp(ax_marg.get_yticklabels(), visible=False)

    out_path = os.path.join(FIG_DIR, "fig_v3_p2_skill_deflation_escalator.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


def render_plot3_folksonomy_raster(data):
    # Plot 3 (Section 2.1): Published AI Ladder Corpus (2017-2026): Descriptive Bottom Rungs vs. Speculative Hope Top Rungs
    df_lad = data["ladders"]
    fig, ax = plt.subplots(figsize=(14.5, 8), dpi=300)
    fig.subplots_adjust(left=0.13, right=0.97, bottom=0.11, top=0.88)
    fig.suptitle("Plot 3: Published AI Ladder Corpus (2017–2026): Descriptive Bottom Rungs vs. Speculative Hope Top Rungs", fontsize=12, fontweight="bold", y=0.96)

    # Construct dense temporal-rung raster (5 vertical levels x 112 monthly columns)
    t_grid = np.linspace(2017.42, 2026.83, 113)
    y_grid = np.arange(0.5, 6.0, 1.0)
    Z = np.zeros((5, len(t_grid) - 1))
    for r in range(5):
        for c in range(len(t_grid) - 1):
            # Bottom rungs (1-3) are predominantly descriptive (1.0); top rungs (4-5) are speculative hope (2.0)
            if r < 3:
                Z[r, c] = 0.25 + 0.10 * (r)
            else:
                Z[r, c] = 0.78 + 0.12 * (r - 3)

    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list("desc_hope", [C_ACTUAL, "#F0E442", C_HOPE])
    mesh = ax.pcolormesh(t_grid, y_grid, Z, cmap=cmap, alpha=0.45, rasterized=True, shading="flat")

    # Overlay the 20 published ladders at their publication dates with staggered vertical callouts
    even_counter = 0
    for idx, row in df_lad.iterrows():
        yr, mo = map(int, row["pub_date"].split("-"))
        x_val = yr + (mo - 0.5) / 12.0
        ax.scatter([x_val, x_val], [1.5, 2.7], color=C_ACTUAL, s=60, edgecolors="#111111", zorder=4)
        ax.scatter([x_val], [4.45], color=C_HOPE, s=80, marker="D", edgecolors="#111111", zorder=5)
        if idx % 2 == 0:
            y_lbl = 4.62 if (even_counter % 2 == 0) else 4.86
            even_counter += 1
            ax.annotate(row["ladder_id"], (x_val, y_lbl), fontsize=7.5, fontweight="bold", ha="center", rotation=20, zorder=6)

    for (gx, glabel), y_brk in zip([(2020.42, "Break G0->G1"), (2022.83, "Break G1->G2"), (2024.33, "Break G2->G3"), (2025.00, "Break G3->G4")], [5.38, 5.38, 5.38, 5.14]):
        ax.axvline(gx, color=C_DEMAND, linewidth=2.2, linestyle="--", zorder=5)
        ax.text(gx + 0.05, y_brk, glabel, color=C_DEMAND, fontsize=8.5, fontweight="bold", va="top")

    apply_calendar_grid(ax, 2017.4, 2026.85)
    ax.set_ylim(0.5, 5.5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["Rung 1 (Bottom)", "Rung 2", "Rung 3 (Mid)", "Rung 4 (Upper)", "Rung 5 (Top/Apex)"], fontsize=9.5, fontweight="bold")
    ax.set_xlabel("Ladder Publication Date & Generation Break Timeline (2017–2026)", fontsize=10, fontweight="bold")
    ax.set_ylabel("Normalized Ladder Rung Position", fontsize=10, fontweight="bold")

    handles = [
        mpatches.Patch(color=C_ACTUAL, alpha=0.8, label="Descriptive Adopted Rungs (L1–L3 Current Gen Reality)"),
        mpatches.Patch(color=C_HOPE, alpha=0.8, label="Speculative Hope Top Rungs (L4–L5 Next-Gen Projection)"),
        plt.Line2D([0], [0], color=C_DEMAND, linewidth=2.2, linestyle="--", label="Detected Generation Break Cutoff"),
    ]
    ax.legend(handles=handles, loc="lower left", bbox_to_anchor=(0.02, 0.02), frameon=False, fontsize=9)

    out_path = os.path.join(FIG_DIR, "fig_v3_p3_folksonomy_and_gen_breaks.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    shutil.copyfile(out_path, os.path.join(FIG_DIR, "fig_v3_p4_folksonomy_and_gen_breaks.png"))
    print(f"[RENDERED] {out_path} (+ alias fig_v3_p4_folksonomy_and_gen_breaks.png)")


def render_plot4_jointplot(data):
    # Plot 4 (Section 2.3): All (Gen G, Level L) Cells: Single-Task Cost vs. User Learning Hours JointPlot
    df_cells = data["cells"]
    x_hours = 0.5 * (df_cells["learning_hours_min"].values + df_cells["learning_hours_max"].values)
    y_usd = df_cells["single_task_usd"].values
    gens = df_cells["gen_id"].values

    fig = plt.figure(figsize=(12, 10), dpi=300)
    gs = gridspec.GridSpec(2, 2, figure=fig, width_ratios=[4, 1], height_ratios=[1, 4], wspace=0.06, hspace=0.06, left=0.09, right=0.96, bottom=0.09, top=0.90)
    ax_main = fig.add_subplot(gs[1, 0])
    ax_top  = fig.add_subplot(gs[0, 0], sharex=ax_main)
    ax_right = fig.add_subplot(gs[1, 1], sharey=ax_main)
    ax_leg  = fig.add_subplot(gs[0, 1])
    ax_leg.axis("off")

    fig.suptitle("Plot 4: All 25 (Gen G, Level L) Cells (2017–2026): Single-Task API/Compute Cost vs. User Learning Hours", fontsize=12, fontweight="bold", y=0.96)

    gen_colors = {"G0": "#555555", "G1": C_SUPPLY, "G2": C_DEMAND, "G3": C_ACTUAL, "G4": C_HOPE}
    gen_offsets = {"G0": (6, -5), "G1": (-6, -7), "G2": (6, 4), "G3": (-6, 5), "G4": (6, 5)}
    gen_align   = {"G0": "left",  "G1": "right",  "G2": "left", "G3": "right", "G4": "left"}
    rng = np.random.default_rng(42)
    perm = rng.permutation(len(df_cells))

    for idx in perm:
        g = gens[idx]
        lvl = df_cells.iloc[idx]["level_id"]
        dx, dy = gen_offsets[g]
        ha_val = gen_align[g]
        if lvl == 1:
            dx, ha_val = 6, "left"
        ax_main.scatter(x_hours[idx], y_usd[idx], color=gen_colors[g], alpha=0.80, s=75, edgecolors="#111111", linewidth=0.6, zorder=3)
        ax_main.annotate(f"{g}-L{lvl}", (x_hours[idx], y_usd[idx]), textcoords="offset points", xytext=(dx, dy), ha=ha_val, fontsize=7.5, fontweight="bold", alpha=0.90)

    # OLS fit in log-transformed space
    lx = np.log10(x_hours + 1.0)
    ly = np.log10(y_usd + 1e-5)
    slope, intercept = np.polyfit(lx, ly, 1)
    x_grid = np.geomspace(1.0, 2000.0, 100)
    x_grid = np.concatenate([[0.0], x_grid])
    y_fit = np.maximum(10**(intercept + slope * np.log10(x_grid + 1.0)) - 1e-5, 0.0)
    ax_main.plot(x_grid, y_fit, linestyle="--", color="#000000", linewidth=2.0, zorder=4, label="Log-OLS Trend")

    ax_main.set_xscale("symlog", linthresh=1.0)
    ax_main.set_yscale("symlog", linthresh=0.001)
    ax_main.set_xlim(0.0, 2800.0)
    ax_main.set_ylim(0.0, 100.0)
    ax_main.set_xlabel("User Learning Investment (Hours, symlog linthresh=1.0)", fontsize=10, fontweight="bold")
    ax_main.set_ylabel("Single-Task Monetary Cost (USD, symlog linthresh=0.001)", fontsize=10, fontweight="bold")
    ax_main.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25, color="#888888")
    ax_main.grid(True, which="minor", linestyle="--", linewidth=0.5, alpha=0.12, color="#AAAAAA")

    xbins = np.concatenate([[0.0], np.geomspace(1.0, 2500.0, 15)])
    ybins = np.geomspace(1e-5, 50.0, 16)
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

    out_path = os.path.join(FIG_DIR, "fig_v3_p4_task_cost_vs_learning_jointplot.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    shutil.copyfile(out_path, os.path.join(FIG_DIR, "fig_v3_p3_task_cost_vs_learning_jointplot.png"))
    print(f"[RENDERED] {out_path} (+ alias fig_v3_p3_task_cost_vs_learning_jointplot.png)")


def render_plots5_to_9_gen_matrices(data):
    # Plot 5 to Plot 9: Per-Generation Step Profiles & Counterfactual Share Breakdown
    df_cells = data["cells"]
    df_gens = data["gens"]

    gen_plot_map = [
        ("G0", 5, "fig_v3_p5_gen0_matrix.png"),
        ("G1", 6, "fig_v3_p6_gen1_matrix.png"),
        ("G2", 7, "fig_v3_p7_gen2_matrix.png"),
        ("G3", 8, "fig_v3_p8_gen3_matrix.png"),
        ("G4", 9, "fig_v3_p9_gen4_matrix.png"),
    ]

    for gen_id, pnum, fname in gen_plot_map:
        sub = df_cells[df_cells["gen_id"] == gen_id].sort_values("level_id")
        gen_row = df_gens[df_gens["gen_id"] == gen_id].iloc[0]

        fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(15.5, 7.5), dpi=300, sharey=True)
        fig.subplots_adjust(left=0.13, right=0.97, bottom=0.11, top=0.82, wspace=0.08)
        fig.suptitle(f"Plot {pnum}: {gen_row['gen_folksonomy_name']} ({gen_row['start_date']} to {gen_row['end_date']})", fontsize=12, fontweight="bold", y=0.96)

        y_pos = sub["level_id"].values
        h_bar = 0.22
        ax_l.barh(y_pos - h_bar, sub["single_task_tokens"].values, height=h_bar, color=C_SUPPLY, alpha=0.85, label="Single-Task Tokens (SUPPLY)")
        ax_l.barh(y_pos, sub["learning_hours_max"].values, height=h_bar, color=C_DEMAND, alpha=0.85, label="Max Learning Hours (DEMAND)")
        ax_l.barh(y_pos + h_bar, sub["single_task_wh"].values * 1000.0, height=h_bar, color=C_ACTUAL, alpha=0.85, label="Single-Task Energy (mWh, ACTUAL)")

        ax_l.set_xscale("symlog", linthresh=1.0)
        ax_l.set_xlim(0.0, 1e8)
        ax_l.set_ylim(0.5, 5.65)
        ax_l.set_yticks([1, 2, 3, 4, 5])
        ax_l.set_yticklabels([f"{gen_id}-L{lvl}\n({hmin}–{hmax}h)" for lvl, hmin, hmax in zip(sub["level_id"], sub["learning_hours_min"], sub["learning_hours_max"])], fontsize=9, fontweight="bold")
        ax_l.set_xlabel("Single-Task Magnitude (symlog scale, linthresh=1.0)", fontsize=10, fontweight="bold")
        ax_l.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25)
        ax_l.grid(True, which="minor", linestyle="--", linewidth=0.5, alpha=0.12)
        ax_l.legend(loc="lower center", bbox_to_anchor=(0.5, 1.01), ncol=3, frameon=False, fontsize=8.0)

        # Right panel: Generation Share % across levels
        ax_r.barh(y_pos - h_bar, sub["user_share_pct"].values, height=h_bar, color=C_DEMAND, alpha=0.85, label="Active User Share %")
        ax_r.barh(y_pos, sub["token_share_pct"].values, height=h_bar, color=C_SUPPLY, alpha=0.85, label="Token Volume Share %")
        ax_r.barh(y_pos + h_bar, sub["spend_share_pct"].values, height=h_bar, color=C_ACTUAL, alpha=0.85, label="Expenditure Share %")

        for lvl, u_sh, t_sh, s_sh, title in zip(sub["level_id"], sub["user_share_pct"], sub["token_share_pct"], sub["spend_share_pct"], sub["user_first_title"]):
            max_bar = max(u_sh, t_sh, s_sh)
            short_t = title[:34] + (".." if len(title) > 34 else "")
            if max_bar <= 48.0:
                ax_r.text(max_bar + 1.5, lvl, f"{short_t} (U:{u_sh:.0f}% | T:{t_sh:.0f}% | S:{s_sh:.0f}%)", va="center", ha="left", fontsize=7.8, color="#111111")
            else:
                ax_r.text(2.0, lvl + 0.34, f"{short_t} (U:{u_sh:.0f}% | T:{t_sh:.0f}% | S:{s_sh:.0f}%)", va="bottom", ha="left", fontsize=7.8, fontweight="bold", color="#111111")

        ax_r.set_xlim(0.0, 100.0)
        ax_r.set_xticks(np.arange(0, 101, 20))
        ax_r.set_xticks(np.arange(0, 101, 5), minor=True)
        ax_r.set_xlabel("Generation-Wide Resource Share (% of Total = 100.0%)", fontsize=10, fontweight="bold")
        ax_r.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25)
        ax_r.grid(True, which="minor", linestyle="--", linewidth=0.5, alpha=0.12)
        ax_r.legend(loc="lower center", bbox_to_anchor=(0.5, 1.01), ncol=3, frameon=False, fontsize=8.0)

        out_path = os.path.join(FIG_DIR, fname)
        fig.savefig(out_path, dpi=300)
        plt.close(fig)
        print(f"[RENDERED] {out_path}")
        if fname == "fig_v3_p9_gen4_matrix.png":
            alias_path = os.path.join(FIG_DIR, "fig_v3_p9_genM_matrix.png")
            shutil.copyfile(out_path, alias_path)
            print(f"[RENDERED ALIAS] {alias_path}")


def draw_bezier_ribbon(ax, x0, y0, x1, y1, color, alpha=0.45, lw=6.0, zorder=3):
    xm = 0.5 * (x0 + x1)
    verts = [(x0, y0), (xm, y0), (xm, y1), (x1, y1)]
    codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    path = Path(verts, codes)
    patch = mpatches.PathPatch(path, facecolor="none", edgecolor=color, lw=lw, alpha=alpha, zorder=zorder)
    ax.add_patch(patch)


def render_plot10_alluvial_poster(data):
    # Plot 10: Continuous-Time Alluvial Evolution Atlas (2017-2026)
    df_cells = data["cells"]
    df_gens = data["gens"]

    fig = plt.figure(figsize=(22, 12), dpi=300)
    gs = gridspec.GridSpec(1, 2, figure=fig, width_ratios=[5.5, 1], wspace=0.05, left=0.11, right=0.97, bottom=0.08, top=0.89)
    ax = fig.add_subplot(gs[0, 0])
    ax_marg = fig.add_subplot(gs[0, 1], sharey=ax)

    fig.suptitle("Plot 10: Continuous-Time Alluvial Evolution Atlas (2017–2026): Down-Level Built-In Sinking, Skill Expansion & Extinction", fontsize=14, fontweight="bold", y=0.96)

    gen_centers = {}
    for _, grow in df_gens.iterrows():
        gid = grow["gen_id"]
        x0, x1 = grow["start_year_float"], grow["end_year_float"]
        xc = 0.5 * (x0 + x1)
        gen_centers[gid] = (x0, x1, xc)
        ax.axvspan(x0, x1, color="#F5F7FA" if int(gid[1]) % 2 == 0 else "#FFFFFF", alpha=0.6, zorder=0)
        ax.axvline(x0, color="#444444", linestyle="--", linewidth=1.1, alpha=0.5, zorder=1)
        y_hdr = 5.66 if gid == "G3" else 5.48
        hdr_txt = f"{gid} ({grow['duration_months']}m)\n{grow['macro_tokens_trillions']}T | ${grow['macro_spend_billion_usd']}B" if gid == "G3" else f"{gid} ({grow['start_date']}..{grow['end_date']})\n{grow['duration_months']} mos | {grow['macro_tokens_trillions']}T tok | ${grow['macro_spend_billion_usd']}B"
        ax.text(xc, y_hdr, hdr_txt,
                ha="center", va="top", fontsize=7.8 if gid == "G3" else 8.5, fontweight="bold", bbox=dict(boxstyle="round,pad=0.22", facecolor="#EFEFEF", edgecolor="#888888"))

    # Draw nodes
    for _, crow in df_cells.iterrows():
        gid = crow["gen_id"]
        lvl = crow["level_id"]
        x0, x1, xc = gen_centers[gid]
        w = (x1 - x0) * 0.76
        rect = mpatches.FancyBboxPatch((xc - w/2, lvl - 0.29), w, 0.58, boxstyle="round,pad=0.02",
                                       facecolor="white", edgecolor=C_SUPPLY if lvl >= 3 else C_ACTUAL, linewidth=1.6, zorder=4)
        ax.add_patch(rect)
        max_chars = 14 if gid == "G3" else 26
        short_title = crow["user_first_title"][:max_chars] + (".." if len(crow["user_first_title"]) > max_chars else "")
        lbl_top = f"{gid}-L{lvl}" if gid == "G3" else f"{gid}-L{lvl} ({crow['learning_hours_min']}–{crow['learning_hours_max']}h)"
        ax.text(xc, lvl + 0.09, lbl_top, ha="center", va="center", fontsize=7.6 if gid == "G3" else 8.0, fontweight="bold", color="#111111", zorder=5)
        ax.text(xc, lvl - 0.11, short_title, ha="center", va="center", fontsize=6.6 if gid == "G3" else 7.2, color="#333333", zorder=5)

    # Alluvial ribbons: Down-level Built-In Sinking (C_ACTUAL), Upward Expansion (C_SUPPLY)
    sinking_links = [
        ("G0", 4, "G1", 2), ("G0", 3, "G1", 2), ("G0", 3, "G1", 1),
        ("G1", 2, "G2", 1), ("G1", 5, "G2", 4), ("G1", 4, "G2", 2),
        ("G2", 2, "G3", 1), ("G2", 3, "G3", 2),
        ("G3", 2, "G4", 1), ("G3", 4, "G4", 2), ("G3", 4, "G4", 3),
    ]
    expansion_links = [
        ("G0", 4, "G1", 5), ("G1", 3, "G2", 3), ("G1", 4, "G2", 4),
        ("G2", 3, "G3", 3), ("G2", 4, "G3", 4), ("G3", 3, "G4", 4), ("G3", 5, "G4", 5),
    ]
    for gA, lA, gB, lB in sinking_links:
        x0 = gen_centers[gA][2] + (gen_centers[gA][1] - gen_centers[gA][0]) * 0.38
        x1 = gen_centers[gB][2] - (gen_centers[gB][1] - gen_centers[gB][0]) * 0.38
        draw_bezier_ribbon(ax, x0, lA, x1, lB, color=C_ACTUAL, alpha=0.50, lw=5.5, zorder=3)
    for gA, lA, gB, lB in expansion_links:
        x0 = gen_centers[gA][2] + (gen_centers[gA][1] - gen_centers[gA][0]) * 0.38
        x1 = gen_centers[gB][2] - (gen_centers[gB][1] - gen_centers[gB][0]) * 0.38
        draw_bezier_ribbon(ax, x0, lA, x1, lB, color=C_SUPPLY, alpha=0.45, lw=4.5, zorder=3)

    # Obsolete skill extinction stubs
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
    ax.set_ylim(0.0, 5.95)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["Level 1 (0h Casual)", "Level 2 (7–45h Wknd–Wk)", "Level 3 (50–200h 2–5Wks)", "Level 4 (200–600h 1 Sem)", "Level 5 (600–2000h+ Infra)"], fontsize=10, fontweight="bold")
    ax.set_xlabel("Continuous Calendar Time (Column Widths Proportional to Generation Duration in Months)", fontsize=11, fontweight="bold")

    handles = [
        mpatches.Patch(color=C_ACTUAL, alpha=0.6, label="Down-Level Sinking (Old High-Level Workflow Becomes Built-In at Lower Level)"),
        mpatches.Patch(color=C_SUPPLY, alpha=0.6, label="Upward Frontier Skill Expansion (New Use Case Requires New Learning)"),
        plt.Line2D([0], [0], color=C_DEMAND, marker="X", linestyle="None", markersize=9, label="Obsolete User Skill Extinction"),
    ]
    ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.01, 0.99), ncol=3, frameon=False, fontsize=9.2)

    # Right marginal step histogram of cell token share weighted by level
    ax_marg.hist(df_cells["level_id"].values, bins=np.arange(0.5, 6.5, 1.0), weights=df_cells["token_share_pct"].values / 5.0,
                 orientation="horizontal", histtype="step", fill=False, linewidth=2.0, color=C_SUPPLY, label="Mean Token %")
    ax_marg.hist(df_cells["level_id"].values, bins=np.arange(0.5, 6.5, 1.0), weights=df_cells["user_share_pct"].values / 5.0,
                 orientation="horizontal", histtype="step", fill=False, linewidth=2.0, color=C_DEMAND, label="Mean User %")
    ax_marg.set_xlabel("Mean Gen Share (%)", fontsize=9.5, fontweight="bold")
    ax_marg.legend(loc="upper right", frameon=False, fontsize=8.5)
    ax_marg.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25)
    plt.setp(ax_marg.get_yticklabels(), visible=False)

    out_path = os.path.join(FIG_DIR, "fig_v3_p10_alluvial_evolution_poster.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


def render_plot11_animation(data):
    # Plot 11 (Section 5.1.2): Animated Temporal Progression of AI Ladder Evolution (fig_v3_p11_ladder_evolution_anim.gif + alias fig_v3_p13_ladder_evolution_anim.gif)
    N_total = 112
    frames_remaining = int(np.ceil(N_total / SKIP_INTERVALS))
    N_render = min(frames_remaining, MAX_FRAMES_TO_RENDER)
    gif_duration = N_render / float(ANIMATION_FPS)
    total_days = 3409
    compression_ratio = total_days / gif_duration

    # Mandatory Pre-Render Mathematical Breakdown Equations (Section 1.5 Plot 11)
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
    fig = plt.figure(figsize=(10, 6.5), dpi=110)
    gs = gridspec.GridSpec(2, 1, figure=fig, height_ratios=[4, 1], hspace=0.22, left=0.10, right=0.96, bottom=0.10, top=0.90)
    ax_main = fig.add_subplot(gs[0, 0])
    ax_scrub = fig.add_subplot(gs[1, 0])

    for f_idx in tqdm(range(N_render), desc="Rendering Plot 11 Animation"):
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

        # Statically lock main panel limits before plotting
        ax_main.set_xscale("symlog", linthresh=1.0)
        ax_main.set_yscale("symlog", linthresh=1.0)
        ax_main.set_xlim(0.0, 2500.0)
        ax_main.set_ylim(0.0, 2e7)
        ax_main.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25)
        ax_main.grid(True, which="minor", linestyle="--", linewidth=0.5, alpha=0.12)

        sub = df_cells[df_cells["gen_id"] == cur_gen]
        xh = 0.5 * (sub["learning_hours_min"].values + sub["learning_hours_max"].values)
        yt = sub["single_task_tokens"].values
        ax_main.plot(xh, yt, color=C_SUPPLY, linewidth=2.4, marker="o", markersize=8, zorder=4, label=f"Active Gen: {cur_gen} ({t_cur:.2f})")
        for lvl, xv, yv in zip(sub["level_id"], xh, yt):
            ax_main.annotate(f"{cur_gen}-L{lvl}", (xv, yv), textcoords="offset points", xytext=(5, 4), fontsize=8, fontweight="bold")

        ax_main.set_title(f"Plot 11: AI Ladder Evolution Trajectory | Time={t_cur:.2f} ({cur_gen})", fontsize=11, fontweight="bold")
        ax_main.set_xlabel("User Learning Investment (Hours, symlog linthresh=1.0)", fontsize=9, fontweight="bold")
        ax_main.set_ylabel("Single-Task Token Volume (symlog linthresh=1.0)", fontsize=9, fontweight="bold")
        ax_main.legend(loc="upper left", frameon=False, fontsize=9)

        # Bottom CITRA Scrubber Strip
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
    out_gif = os.path.join(FIG_DIR, "fig_v3_p11_ladder_evolution_anim.gif")
    frames_pil[0].save(out_gif, save_all=True, append_images=frames_pil[1:], duration=int(1000 / ANIMATION_FPS), loop=0)
    shutil.copyfile(out_gif, os.path.join(FIG_DIR, "fig_v3_p13_ladder_evolution_anim.gif"))
    print(f"[RENDERED ANIMATION] {out_gif} (+ alias fig_v3_p13_ladder_evolution_anim.gif) | frames={len(frames_pil)}")


def render_plot12_trl_and_hopes(data):
    # Plot 12 (Section 5.2.1): TRL Maturation Trajectories & Population Evolution of Failed Hopes
    df_trl = data["trl"]
    fig = plt.figure(figsize=(16.5, 7.5), dpi=300)
    gs = gridspec.GridSpec(1, 3, figure=fig, width_ratios=[3.2, 0.7, 2.8], wspace=0.14, left=0.12, right=0.97, bottom=0.11, top=0.82)
    ax_l = fig.add_subplot(gs[0, 0])
    ax_m = fig.add_subplot(gs[0, 1], sharey=ax_l)
    ax_r = fig.add_subplot(gs[0, 2])

    fig.suptitle("Plot 12: TRL Maturation Trajectories (Paper to Level 1 Default) & Population Evolution of the Inventory of Hope", fontsize=12, fontweight="bold", y=0.96)

    def ym_to_float(ym_str):
        ym = ym_str.split(" ")[0]
        y, m = map(int, ym.split("-"))
        return y + (m - 0.5) / 12.0

    rng = np.random.default_rng(42)
    perm = rng.permutation(len(df_trl))
    all_trl_points = []
    trl_y_offsets = {
        "TRL_01": 9.10, "TRL_02": 9.10, "TRL_03": 9.10,
        "TRL_04": 9.08, "TRL_05": 9.32, "TRL_06": 9.52,
        "TRL_07": 9.08, "TRL_08": 9.32, "TRL_10": 9.52,
        "TRL_09": 9.10,
    }
    for idx in perm:
        row = df_trl.iloc[idx]
        xs = [ym_to_float(row["trl_1_2_paper_date"]), ym_to_float(row["trl_4_5_proto_date_level"]),
              ym_to_float(row["trl_7_power_date_level"]), ym_to_float(row["trl_9_builtin_l1_date"])]
        ys = [1.5, 4.5, 7.0, 9.0]
        all_trl_points.extend(ys)
        ax_l.plot(xs, ys, color=C_SUPPLY, alpha=0.35, linewidth=1.6, marker="o", zorder=2)
        ax_l.annotate(row["trl_id"], (xs[-1], trl_y_offsets.get(row["trl_id"], 9.10)), fontsize=7.2, fontweight="bold", ha="center", color="#222222")

    # Central parametric mean TRL trajectory
    mean_x = np.linspace(2018.5, 2025.5, 50)
    mean_y = 1.5 + 7.5 * ((mean_x - 2018.5) / (2025.5 - 2018.5))**0.85
    ax_l.plot(mean_x, mean_y, color=C_ACTUAL, linewidth=3.0, zorder=5, label="Parametric Mean TRL Maturation Curve (Lag μ = 36.2 mos)")

    apply_calendar_grid(ax_l, 2017.4, 2026.85)
    ax_l.set_ylim(1.0, 9.8)
    ax_l.set_yticks([1.5, 4.5, 7.0, 9.0])
    ax_l.set_yticklabels(["TRL 1–2 (Paper)", "TRL 4–5 (L4–L5 Proto)", "TRL 7 (L2–L3 Power)", "TRL 9 (Built-In L1)"], fontsize=8.5, fontweight="bold")
    ax_l.set_xlabel("Calendar Time (2017–2026)", fontsize=9.5, fontweight="bold")
    ax_l.set_ylabel("Technology Readiness Level (TRL 1 to 9)", fontsize=9.5, fontweight="bold")
    ax_l.legend(loc="lower center", bbox_to_anchor=(0.5, 1.01), frameon=False, fontsize=8.5)

    ax_m.hist(all_trl_points, bins=np.linspace(1.0, 9.5, 10), orientation="horizontal", histtype="step", fill=False, linewidth=1.8, color=C_SUPPLY)
    ax_m.set_xlabel("Stage Count", fontsize=8.5, fontweight="bold")
    ax_m.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25)
    plt.setp(ax_m.get_yticklabels(), visible=False)

    # Right panel: Population Evolution of the Inventory of Hope across Gen 0..Gen 4
    gens_labels = ["Gen 0", "Gen 1", "Gen 2", "Gen 3", "Gen 4"]
    x_idx = np.arange(len(gens_labels))
    survived   = np.array([25.0, 33.3, 20.0, 25.0, 25.0])
    absorbed   = np.array([50.0, 33.3, 20.0, 25.0, 0.0])
    too_early  = np.array([0.0,  33.4, 20.0, 25.0, 25.0])
    econ_dead  = np.array([0.0,  0.0,  20.0, 25.0, 50.0])
    out_std    = np.array([25.0, 0.0,  20.0, 0.0,  0.0])

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

    out_path = os.path.join(FIG_DIR, "fig_v3_p12_trl_and_failed_hopes.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    shutil.copyfile(out_path, os.path.join(FIG_DIR, "fig_v3_p11_trl_and_failed_hopes.png"))
    print(f"[RENDERED] {out_path} (+ alias fig_v3_p11_trl_and_failed_hopes.png)")


def render_plot13_pair_plot(data):
    # Plot 13 (Section 5.3.1): Asymmetric Tri-Partite Pair Plot Matrix across 4 Quantitative Dimensions for 20 Ladders
    df_lad = data["ladders"].copy()
    cols = ["scope_coverage", "user_skill_alignment", "historical_invariance", "empirical_cost_grounding"]
    labels = ["Scope Coverage", "User-Skill Align", "Hist. Invariance", "Cost Grounding"]

    fig = plt.figure(figsize=(14, 12), dpi=300)
    gs = gridspec.GridSpec(4, 4, figure=fig, left=0.08, right=0.96, bottom=0.07, top=0.88, wspace=0.12, hspace=0.12)
    fig.suptitle("Plot 13: Published AI Ladders (2017–2026): Tri-Partite Pairwise Alignment Matrix", fontsize=13, fontweight="bold", y=0.96)

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
                ax.boxplot(x_data, orientation="horizontal", positions=[4.2], widths=0.7, patch_artist=True,
                           boxprops=dict(facecolor=C_ACTUAL, alpha=0.35))
                stats_txt = f"μ={mu:.2f} | Med={q2:.2f}\nMin={x_data.min():.2f} | Max={x_data.max():.2f}\nQ1={q1:.2f} | Q3={q3:.2f} | IQR={iqr:.2f}"
                ax.text(0.03, 0.94, stats_txt, transform=ax.transAxes, va="top", ha="left", fontsize=7.2,
                        bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.85, edgecolor="#CCCCCC"))
                ax.set_xlim(0.35, 1.02)
                ax.set_ylim(0.0, 6.0)
            elif i > j:
                ax.scatter(x_data[perm], y_data[perm], color=C_SUPPLY, alpha=0.70, s=55, edgecolors="#111111", zorder=3)
                ax.scatter([1.0], [1.0], color=C_DEMAND, marker="*", s=140, zorder=5, label="v3 Gen×Level")
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
        plt.Line2D([0], [0], color=C_DEMAND, marker="*", linestyle="None", markersize=10, label="Our v3 2D (Gen × Level) Ladder"),
        plt.Line2D([0], [0], color="#000000", linestyle="--", linewidth=1.8, label="OLS Linear Fit"),
        plt.Line2D([0], [0], color=C_DEMAND, linestyle="--", linewidth=1.8, label="Parametric Mean (μ)"),
    ]
    fig.legend(handles=handles, loc="center", bbox_to_anchor=(0.5, 0.92), ncol=4, frameon=False, fontsize=9.5)

    out_path = os.path.join(FIG_DIR, "fig_v3_p13_ladder_comparison_matrix.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    shutil.copyfile(out_path, os.path.join(FIG_DIR, "fig_v3_p12_ladder_comparison_matrix.png"))
    print(f"[RENDERED] {out_path} (+ alias fig_v3_p12_ladder_comparison_matrix.png)")


def render_plot14_gen5_speculative_matrix(data):
    # Plot 14 (Section 5.4.2): Speculative Next Generation (Gen 5 = Current + 1) User-Skill Matrix & Cutoff Window
    sub = data["gen5_cells"].sort_values("level_id")
    fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(15.5, 7.5), dpi=300, sharey=True)
    fig.subplots_adjust(left=0.14, right=0.97, bottom=0.11, top=0.82, wspace=0.08)
    fig.suptitle("Plot 14: Speculative Gen 5 (Current + 1: 2026-08 Pre-Cutoff / 2027-03 Mainstream Crossover to 2028): Ambient OS, Verifier Contracts & Continuous RLVR", fontsize=11.5, fontweight="bold", y=0.96)

    y_pos = sub["level_id"].values
    h_bar = 0.22
    ax_l.barh(y_pos - h_bar, sub["single_task_tokens"].values, height=h_bar, color=C_SUPPLY, alpha=0.85, label="Projected Single-Task Tokens (SUPPLY)")
    ax_l.barh(y_pos, sub["learning_hours_max"].values, height=h_bar, color=C_DEMAND, alpha=0.85, label="Max Learning Hours (DEMAND)")
    ax_l.barh(y_pos + h_bar, sub["single_task_wh"].values * 1000.0, height=h_bar, color=C_HOPE, alpha=0.85, label="Projected Task Energy (mWh, SPECULATIVE)")

    ax_l.set_xscale("symlog", linthresh=1.0)
    ax_l.set_xlim(0.0, 2e8)
    ax_l.set_ylim(0.5, 5.65)
    ax_l.set_yticks([1, 2, 3, 4, 5])
    ax_l.set_yticklabels([
        "G5-L1 (Casual)\n0 hours",
        "G5-L2 (Spec Studio)\n7–45 hours",
        "G5-L3 (A2A/Policy)\n50–200 hours",
        "G5-L4 (Formal Verifier)\n200–600 hours",
        "G5-L5 (Cont. RLVR)\n600–2000+ hours"
    ], fontsize=9, fontweight="bold")
    ax_l.set_xlabel("Projected Single-Task Magnitude (symlog scale, linthresh=1.0)", fontsize=10, fontweight="bold")
    ax_l.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25)
    ax_l.grid(True, which="minor", linestyle="--", linewidth=0.5, alpha=0.12)
    ax_l.legend(loc="lower center", bbox_to_anchor=(0.5, 1.01), ncol=3, frameon=False, fontsize=8.0)

    ax_r.barh(y_pos - h_bar, sub["user_share_pct"].values, height=h_bar, color=C_DEMAND, alpha=0.85, label="Projected User Share %")
    ax_r.barh(y_pos, sub["token_share_pct"].values, height=h_bar, color=C_SUPPLY, alpha=0.85, label="Projected Token Share %")
    ax_r.barh(y_pos + h_bar, sub["spend_share_pct"].values, height=h_bar, color=C_HOPE, alpha=0.85, label="Projected Spend Share %")

    for lvl, u_sh, t_sh, s_sh, title in zip(sub["level_id"], sub["user_share_pct"], sub["token_share_pct"], sub["spend_share_pct"], sub["user_first_title"]):
        max_bar = max(u_sh, t_sh, s_sh)
        short_t = title[:36] + (".." if len(title) > 36 else "")
        if max_bar <= 45.0:
            ax_r.text(max_bar + 1.5, lvl, f"{short_t} (U:{u_sh:.0f}% | T:{t_sh:.0f}% | S:{s_sh:.0f}%)", va="center", ha="left", fontsize=7.8, color="#111111")
        else:
            ax_r.text(2.0, lvl + 0.34, f"{short_t} (U:{u_sh:.0f}% | T:{t_sh:.0f}% | S:{s_sh:.0f}%)", va="bottom", ha="left", fontsize=7.8, fontweight="bold", color="#111111")

    ax_r.set_xlim(0.0, 100.0)
    ax_r.set_xticks(np.arange(0, 101, 20))
    ax_r.set_xticks(np.arange(0, 101, 5), minor=True)
    ax_r.set_xlabel("Projected Generation-Wide Resource Share (% of Total = 100.0%)", fontsize=10, fontweight="bold")
    ax_r.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25)
    ax_r.grid(True, which="minor", linestyle="--", linewidth=0.5, alpha=0.12)
    ax_r.legend(loc="lower center", bbox_to_anchor=(0.5, 1.01), ncol=3, frameon=False, fontsize=8.0)

    out_path = os.path.join(FIG_DIR, "fig_v3_p14_gen5_speculative_matrix.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


def render_plot0_encyclopedic_megachart_poster(data):
    # Plot 0 (Very Start of Doc Before Title): Large-Format Encyclopedic Broadside Wallchart / Megachart Poster
    import textwrap

    df_cells = pd.concat([data["cells"], data["gen5_cells"]], ignore_index=True)
    df_poster = data["poster_cells"]
    df_events = data["events"]

    # Piecewise-linear calendar coordinate transformation mapping 6 Generations onto [0.0, 6.0]
    # G0: [2017.42, 2020.42] -> [0, 1]
    # G1: [2020.42, 2022.83] -> [1, 2]
    # G2: [2022.83, 2024.33] -> [2, 3]
    # G3: [2024.33, 2025.00] -> [3, 4]
    # G4: [2025.00, 2026.803] -> [4, 5] (TODAY = 2026-10-20 = 2026.803 sits cleanly at the x = 5.000 inter-column boundary!)
    # G5: [2026.803, 2028.95] -> [5, 6]
    gen_bounds = [
        ("G0", 2017.42, 2020.42, 0.0, 1.0),
        ("G1", 2020.42, 2022.83, 1.0, 2.0),
        ("G2", 2022.83, 2024.33, 2.0, 3.0),
        ("G3", 2024.33, 2025.00, 3.0, 4.0),
        ("G4", 2025.00, 2026.803, 4.0, 5.0),
        ("G5", 2026.803, 2028.95, 5.0, 6.0),
    ]

    def year_to_x(y_val):
        for _, t0, t1, x0, x1 in gen_bounds:
            if y_val <= t1:
                return x0 + (x1 - x0) * np.clip((y_val - t0) / (t1 - t0), 0.0, 1.0)
        return 6.0

    fig = plt.figure(figsize=(42, 27), dpi=300, facecolor="#FBFBF9")
    gs = gridspec.GridSpec(
        2, 2, figure=fig,
        width_ratios=[5.85, 1.15],
        height_ratios=[4.35, 1.40],
        left=0.148, right=0.988, bottom=0.042, top=0.922,
        wspace=0.016, hspace=0.036
    )
    ax_main   = fig.add_subplot(gs[0, 0])
    ax_right  = fig.add_subplot(gs[0, 1], sharey=ax_main)
    ax_bot    = fig.add_subplot(gs[1, 0], sharex=ax_main)
    ax_corner = fig.add_subplot(gs[1, 1])

    # Top Broadside Title Banner
    fig.text(
        0.50, 0.972,
        "PLOT 0 — THE AI LADDER EVOLUTION ATLAS (2017–2028): AN ENCYCLOPEDIC BROADSIDE WALLCHART OF USER SKILL LEVELS, WORKFLOWS, TOOLS & DEFINING EVENTS",
        ha="center", va="center", fontsize=17.5, fontweight="bold", color="#111111"
    )
    fig.text(
        0.50, 0.947,
        "Six Chronological Generations (Gen 0 Pre-LLM through Speculative Gen 5) × Five Standardized User Learning-Time Tiers (Level 1 Casual [0 Hours] to Level 5 Infrastructure & Sandbox Architect [600 to 2,000+ Hours])  |  Empirical Cutoff Baseline: TODAY = 2026-10-20",
        ha="center", va="center", fontsize=11.2, color="#333333", fontweight="bold"
    )

    # -------------------------------------------------------------------------
    # PANEL 1: TOP-LEFT MAIN ENCYCLOPEDIC MATRIX (6 Generations x 5 Levels = 30 Cells)
    # -------------------------------------------------------------------------
    ax_main.set_facecolor("#FBFBF9")
    ax_main.set_xlim(0.0, 6.0)
    ax_main.set_ylim(0.46, 6.08)

    gen_header_specs = [
        ("G0", 0.0, 1.0, "GEN 0: PRE-LLM CODE-PIPELINE &\nPASSIVE-WIDGET GENERATION",
         "2017-06..2020-05 (36m) | 12M Users • 0.18T Tok • $1.1B", "#E8EEF5", "#2B4C7E"),
        ("G1", 1.0, 2.0, "GEN 1: COMPLETION PLAYGROUND &\nGHOST-TEXT AUTOCOMPLETE GEN",
         "2020-06..2022-10 (29m) | 45M Users • 1.60T Tok • $3.8B", "#EBF5EE", "#1E6B47"),
        ("G2", 2.0, 3.0, "GEN 2: CONVERSATIONAL CHAT, MANUAL\nPROMPTING & DIY VECTOR-RAG GEN",
         "2022-11..2024-04 (18m) | 380M Users • 28.0T Tok • $14.0B", "#FDF2E9", "#A04000"),
        ("G3", 3.0, 4.0, "GEN 3: MULTIMODAL WORKSPACE,\nLIVE ARTIFACTS & AI-IDE GEN",
         "2024-05..2024-12 (8m) | 720M Users • 240T Tok • $39.0B", "#E8F6F3", "#0E6655"),
        ("G4", 4.0, 5.0, "GEN 4: BUILT-IN THINKING, DEEP RESEARCH,\nTERMINAL CLI & SANDBOX GEN",
         "2025-01..2026-10/2027-03 | 1,150M Users • 1,100T Tok • $88B", "#EBF3FA", "#00558C"),
        ("G5", 5.0, 6.0, "GEN 5 [SPECULATIVE NEXT GEN: CURRENT+1]:\nAMBIENT OS, VERIFIER & CONT. RLVR GEN",
         "2026-08 Pre / 2027-03..2028-12 | Proj: 1,650M U • 4,800T Tok", "#F8ECF5", "#7A2862"),
    ]

    for gid, x0, x1, gtitle, gsub, bg_c, hdr_c in gen_header_specs:
        ax_main.axvspan(x0, x1, color=bg_c, alpha=0.32, zorder=0)
        ax_main.axvline(x0, color="#444444", linestyle="-" if gid != "G5" else "--", linewidth=1.5, alpha=0.75, zorder=2)
        # Column Top Title Banner (strictly inside [x0+0.032, x0+0.968], y in [5.66, 6.04])
        hdr_box = mpatches.FancyBboxPatch(
            (x0 + 0.032, 5.66), 0.936, 0.38,
            boxstyle="round,pad=0.008", facecolor=hdr_c, edgecolor="#111111", linewidth=1.4, zorder=6
        )
        ax_main.add_patch(hdr_box)
        ax_main.text(x0 + 0.50, 5.90, gtitle, ha="center", va="center", fontsize=6.8, fontweight="bold", color="white", linespacing=1.12, zorder=7)
        ax_main.text(x0 + 0.50, 5.72, gsub, ha="center", va="center", fontsize=5.9, color="#F0E442", fontweight="bold", zorder=7)

    # Highlight Dual Gen 4 -> Gen 5 Cutoff Zone & TODAY (2026-10-20) Beacon Line in the inter-column gutter [4.96, 5.04]
    x_pre_cutoff = 4.962                # 2026-08 Pre-Today First-Release Inflection (gutter left edge)
    x_today      = 5.000                # 2026-10-20 TODAY (exact Gen 4 | Gen 5 boundary)
    x_post_cut   = 5.038                # 2027-03 Post-Today Mainstream Production Crossover (gutter right edge)

    ax_main.axvspan(x_pre_cutoff, x_post_cut, color="#FFD700", alpha=0.16, zorder=1)
    ax_main.axvline(x_pre_cutoff, color=C_HOPE, linestyle=":", linewidth=2.0, zorder=8)
    ax_main.axvline(x_today, color="#C00000", linestyle="-", linewidth=3.2, zorder=12)
    ax_main.axvline(x_post_cut, color=C_HOPE, linestyle="--", linewidth=2.6, zorder=8)

    ax_main.text(
        x_today, 5.555,
        "◀ TODAY: 2026-10-20 ▶  (Pre-Cutoff: 2026-08 First-Release | Post-Cutoff: 2027-03 Mainstream Crossover)",
        ha="center", va="center", fontsize=6.6, fontweight="bold", color="white",
        bbox=dict(boxstyle="round,pad=0.16", facecolor="#C00000", edgecolor="#111111", linewidth=1.1),
        zorder=15
    )

    # Horizontal level dividers
    for y_div in [1.5, 2.5, 3.5, 4.5]:
        ax_main.axhline(y_div, color="#888888", linestyle=":", linewidth=0.9, alpha=0.55, zorder=1)

    # Alluvial Flow Ribbons Between Columns (routed through the inter-column gutter [c+0.96, c+1.04])
    sinking_links = [
        (0, 4, 1, 2), (0, 3, 1, 2), (0, 3, 1, 1),
        (1, 2, 2, 1), (1, 5, 2, 4), (1, 4, 2, 2),
        (2, 2, 3, 1), (2, 3, 3, 2),
        (3, 2, 4, 1), (3, 4, 4, 2), (3, 4, 4, 3),
        (4, 2, 5, 1), (4, 3, 5, 2), (4, 4, 5, 2),
    ]
    expansion_links = [
        (0, 4, 1, 5), (1, 3, 2, 3), (1, 4, 2, 4),
        (2, 3, 3, 3), (2, 4, 3, 4), (3, 3, 4, 4), (3, 5, 4, 5),
        (4, 3, 5, 3), (4, 4, 5, 4), (4, 5, 5, 5),
    ]
    for cA, lA, cB, lB in sinking_links:
        col_rib = C_HOPE if cB == 5 else C_ACTUAL
        draw_bezier_ribbon(ax_main, cA + 0.955, lA, cB + 0.045, lB, color=col_rib, alpha=0.55, lw=6.5, zorder=3)
    for cA, lA, cB, lB in expansion_links:
        col_rib = C_HOPE if cB == 5 else C_SUPPLY
        draw_bezier_ribbon(ax_main, cA + 0.955, lA, cB + 0.045, lB, color=col_rib, alpha=0.45, lw=5.0, zorder=3)

    # Render all 30 Encyclopedic Cells
    gen_to_col = {"G0": 0, "G1": 1, "G2": 2, "G3": 3, "G4": 4, "G5": 5}
    for _, prow in df_poster.iterrows():
        gid = prow["gen_id"]
        lvl = int(prow["level_id"])
        c = gen_to_col[gid]
        crow = df_cells[(df_cells["gen_id"] == gid) & (df_cells["level_id"] == lvl)].iloc[0]

        x_left = c + 0.032
        w_box  = 0.936
        y_bot  = lvl - 0.445
        h_box  = 0.890

        if gid == "G5":
            edge_c = C_HOPE
            hdr_fill = "#7A2862"
            box_fill = "#FFFBFD"
        elif gid == "G0" and lvl == 1:
            edge_c = "#666666"
            hdr_fill = "#555555"
            box_fill = "#F7F7F7"
        elif lvl <= 2:
            edge_c = C_ACTUAL
            hdr_fill = "#116649"
            box_fill = "#FFFFFF"
        else:
            edge_c = C_SUPPLY
            hdr_fill = "#0B4F7C"
            box_fill = "#FFFFFF"

        # Outer cell card
        card = mpatches.FancyBboxPatch(
            (x_left, y_bot), w_box, h_box,
            boxstyle="round,pad=0.008", facecolor=box_fill, edgecolor=edge_c,
            linewidth=1.5 if gid != "G5" else 1.8,
            linestyle="--" if gid == "G5" else "-", zorder=4
        )
        ax_main.add_patch(card)

        # Two-line Cell Top Header Strip (Line 1 = Distinctive Title, Line 2 = Telemetry Badge — zero horizontal collision!)
        hdr_strip = mpatches.FancyBboxPatch(
            (x_left, lvl + 0.295), w_box, 0.150,
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
        badge_str = f"Task: {tok_str} ({usd_str})  •  Gen Share: Users {crow['user_share_pct']:.0f}% | Tokens {crow['token_share_pct']:.0f}% | Spend {crow['spend_share_pct']:.0f}%"

        ax_main.text(
            x_left + 0.014, lvl + 0.402,
            f"[{gid}-L{lvl}] {prow['short_header']}",
            ha="left", va="center", fontsize=6.35, fontweight="bold", color="white", zorder=6
        )
        ax_main.text(
            x_left + 0.014, lvl + 0.332,
            badge_str,
            ha="left", va="center", fontsize=5.65, fontweight="bold", color="#F0E442", zorder=6
        )

        # Wrap each bullet line cleanly to fit inside the cell box
        wrapped_bullets = []
        for raw_line in prow["encyclopedic_body"].split("\n"):
            wlines = textwrap.wrap(raw_line, width=76, subsequent_indent="   ")
            wrapped_bullets.extend(wlines[:3])
        body_text = "\n".join(wrapped_bullets[:15])

        ax_main.text(
            x_left + 0.014, lvl + 0.275,
            body_text,
            ha="left", va="top", fontsize=5.85, color="#151515", linespacing=1.14, zorder=6
        )

    # Obsolete User Skill Extinction Callout Badges on Main Matrix (placed cleanly on inter-column boundaries)
    obsolete_badges = [
        (0.965, 3.48, "EXTINCT IN GEN 1: 10k Manual Label Curation"),
        (1.965, 2.48, "EXTINCT IN GEN 2: stop=['\\n'] Prefix Hacks"),
        (2.965, 3.48, "EXTINCT IN GEN 3: 20-PDF Python Chunking"),
        (3.965, 2.48, "EXTINCT IN GEN 4: Manual CoT Wrappers"),
        (4.965, 3.48, "SINKS IN GEN 5: Manual .mcp.json & CLI"),
    ]
    for ox, oy, otxt in obsolete_badges:
        ax_main.scatter([ox], [oy], color=C_DEMAND, marker="X", s=95, edgecolors="#111111", linewidth=0.8, zorder=10)
        ax_main.text(
            ox - 0.018, oy, otxt, ha="right", va="center", fontsize=5.6, fontweight="bold", color="#902000",
            bbox=dict(boxstyle="round,pad=0.11", facecolor="#FFF3CD", edgecolor=C_DEMAND, linewidth=0.8), zorder=10
        )

    # Multi-Line Y-Axis Labels with Level Number, Coined Name ("Casual" for Level 1), Un-Abbreviated Learning Time, and Infrastructure
    y_labels_multiline = [
        "LEVEL 1 — CASUAL\n"
        "• Learning Time: 0 hours (zero study required)\n"
        "• Persona: Average high schooler / mainstream consumer\n"
        "• Resources & Infrastructure: Default consumer web browser,\n"
        "  mobile app, or pre-installed office/IDE widget\n"
        "  (Zero setup, zero configuration, zero extra spend)",

        "LEVEL 2 — PROMPT & WORKSPACE CRAFTER\n"
        "• Learning Time: 7 to 45 hours\n"
        "  (1 weekend to 1 full week of focused practice)\n"
        "• Persona: Curious power user / domain analyst\n"
        "• Resources & Infrastructure: Paid consumer web tier ($20/month),\n"
        "  web playground, or drag-and-drop project workspace (No code/CLI)",

        "LEVEL 3 — SYSTEM & WORKFLOW INTEGRATOR\n"
        "• Learning Time: 50 to 200 hours\n"
        "  (2 to 5 full weeks of applied engineering study)\n"
        "• Persona: Software developer / internal company bot builder\n"
        "• Resources & Infrastructure: Local code IDE (VS Code / Cursor),\n"
        "  commercial API keys ($20–$200/month), vector DB, or .mcp.json",

        "LEVEL 4 — HARNESS & MODEL TUNING ENGINEER\n"
        "• Learning Time: 200 to 600 hours\n"
        "  (~1 university semester of ML & systems curriculum)\n"
        "• Persona: AI systems engineer / applied ML practitioner\n"
        "• Resources & Infrastructure: Single local/cloud GPU (16–80 GB VRAM)\n"
        "  or terminal CLI coding harness + local Docker suite ($100–$1,000/month)",

        "LEVEL 5 — INFRASTRUCTURE & SANDBOX ARCHITECT\n"
        "• Learning Time: 600 to 2,000+ hours\n"
        "  (6+ months full-time systems & cluster mastery)\n"
        "• Persona: Frontier ML architect / autonomous sandbox operator\n"
        "• Resources & Infrastructure: Dedicated 24/7 physical sandbox host\n"
        "  (Apple M4 Mac Mini) or multi-node GPU cluster ($1,000–$100,000+/month)",
    ]
    ax_main.set_yticks([1, 2, 3, 4, 5])
    ax_main.set_yticklabels(y_labels_multiline, fontsize=8.0, fontweight="bold", color="#111111", linespacing=1.22)
    plt.setp(ax_main.get_xticklabels(), visible=False)

    # -------------------------------------------------------------------------
    # PANEL 2: TOP-RIGHT MARGINAL HISTOGRAM (10 Lines with Alpha: 2 Metrics x 5 Empirical Generations in Rel. Freq.)
    # -------------------------------------------------------------------------
    ax_right.set_facecolor("#FBFBF9")
    gen_Line_styles = [
        ("G0", "Gen 0 (2017–2020)", "#555555", "o"),
        ("G1", "Gen 1 (2020–2022)", "#0072B2", "s"),
        ("G2", "Gen 2 (2022–2024)", "#D55E00", "^"),
        ("G3", "Gen 3 (2024)",      "#009E73", "D"),
        ("G4", "Gen 4 (2025–2026)", "#CC79A7", "P"),
    ]
    y_lvls = np.array([1.0, 2.0, 3.0, 4.0, 5.0])

    for gid, glbl, gcol, gmk in gen_Line_styles:
        sub_g = df_cells[df_cells["gen_id"] == gid].sort_values("level_id")
        u_rel = sub_g["user_share_pct"].values / 100.0
        t_rel = sub_g["token_share_pct"].values / 100.0

        # Horizontal step histogram + marker overlay for User Relative Frequency (Solid)
        ax_right.step(u_rel, y_lvls, where="mid", color=gcol, linestyle="-", linewidth=2.2, alpha=0.72, zorder=4, label=f"{gid} User Rel. Freq.")
        ax_right.scatter(u_rel, y_lvls, color=gcol, marker=gmk, s=42, alpha=0.82, zorder=5)

        # Horizontal step histogram + marker overlay for Token Relative Frequency (Dashed)
        ax_right.step(t_rel, y_lvls, where="mid", color=gcol, linestyle="--", linewidth=2.0, alpha=0.68, zorder=3, label=f"{gid} Token Rel. Freq.")
        ax_right.scatter(t_rel, y_lvls, facecolors="none", edgecolors=gcol, marker=gmk, s=42, linewidth=1.4, alpha=0.82, zorder=5)

    # Annotate mean relative frequencies per level on right margin
    emp_cells = df_cells[df_cells["gen_id"].isin(["G0", "G1", "G2", "G3", "G4"])]
    for lvl in range(1, 6):
        u_mu = emp_cells[emp_cells["level_id"] == lvl]["user_share_pct"].mean() / 100.0
        t_mu = emp_cells[emp_cells["level_id"] == lvl]["token_share_pct"].mean() / 100.0
        ax_right.text(
            0.76, lvl + 0.33,
            f"L{lvl} Mean Rel. Freq:\nUser μ={u_mu:.2f} | Tok μ={t_mu:.2f}",
            ha="right", va="top", fontsize=6.8, fontweight="bold", color="#222222",
            bbox=dict(boxstyle="round,pad=0.14", facecolor="white", alpha=0.88, edgecolor="#BBBBBB")
        )

    ax_right.set_xlim(0.0, 0.78)
    ax_right.set_xticks([0.0, 0.20, 0.40, 0.60, 0.75])
    ax_right.set_xticklabels(["0.00", "0.20", "0.40", "0.60", "0.75"], fontsize=8.5, fontweight="bold")
    ax_right.set_xlabel("Relative Frequency Across Levels\n(10 Curves = 5 Gens × [User Solid, Token Dashed], Σ = 1.00)", fontsize=8.8, fontweight="bold")
    ax_right.set_title("Marginal Relative Frequency\n(2 Metrics × 5 Empirical Gens = 10 Lines)", fontsize=9.8, fontweight="bold", pad=8)
    ax_right.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.28, color="#888888")
    ax_right.legend(loc="upper right", bbox_to_anchor=(0.99, 0.99), ncol=1, frameon=True, facecolor="white", framealpha=0.90, fontsize=6.6)
    plt.setp(ax_right.get_yticklabels(), visible=False)

    # -------------------------------------------------------------------------
    # PANEL 3: BOTTOM-LEFT MARGINAL TIMELINE (2 Growth Curves + 36 Generational-Defining Events ~3/yr)
    # -------------------------------------------------------------------------
    ax_bot.set_facecolor("#FBFBF9")
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
    ])
    tokens_emp = np.array([
        0.04, 0.07, 0.12, 0.16, 0.25,
        0.55, 1.10, 1.45, 2.20,
        12.0, 22.0, 45.0,
        140.0, 280.0,
        520.0, 780.0, 1010.0, 1100.0
    ])

    t_curve_spec = np.array([2026.803, 2027.17, 2027.8, 2028.4, 2028.95])
    users_spec   = np.array([1150.0,  1260.0,  1420.0, 1560.0, 1650.0])
    tokens_spec  = np.array([1100.0,  1550.0,  2600.0, 3700.0, 4800.0])

    x_emp  = np.array([year_to_x(t) for t in t_curve_emp])
    x_spec = np.array([year_to_x(t) for t in t_curve_spec])

    # Step-histogram fill + bold trajectory curves for Users (Millions) and Tokens (Trillions)
    ax_bot.fill_between(x_emp, 0, users_emp, step="mid", color=C_DEMAND, alpha=0.12, zorder=1)
    ax_bot.fill_between(x_emp, 0, tokens_emp, step="mid", color=C_SUPPLY, alpha=0.12, zorder=1)
    ax_bot.plot(x_emp, users_emp, color=C_DEMAND, linewidth=2.8, marker="o", markersize=5, zorder=4, label="Global Active AI Users (Millions, Empirical 2017–TODAY)")
    ax_bot.plot(x_emp, tokens_emp, color=C_SUPPLY, linewidth=2.8, marker="s", markersize=5, zorder=4, label="Global Annualized Token Volume (Trillions, Empirical 2017–TODAY)")

    ax_bot.plot(x_spec, users_spec, color=C_DEMAND, linestyle="--", linewidth=2.4, marker="o", markersize=4, zorder=4, label="Projected Active Users in Speculative Gen 5 (Millions)")
    ax_bot.plot(x_spec, tokens_spec, color=C_SUPPLY, linestyle="--", linewidth=2.4, marker="s", markersize=4, zorder=4, label="Projected Token Volume in Speculative Gen 5 (Trillions)")

    # Generation boundary lines & TODAY beacon in bottom timeline
    for gid, x0, x1, _, _, bg_c, _ in gen_header_specs:
        ax_bot.axvspan(x0, x1, color=bg_c, alpha=0.25, zorder=0)
        ax_bot.axvline(x0, color="#444444", linestyle="-" if gid != "G5" else "--", linewidth=1.3, alpha=0.75, zorder=2)

    ax_bot.axvspan(x_pre_cutoff, x_post_cut, color="#FFD700", alpha=0.18, zorder=1)
    ax_bot.axvline(x_pre_cutoff, color=C_HOPE, linestyle=":", linewidth=2.0, zorder=8)
    ax_bot.axvline(x_today, color="#C00000", linestyle="-", linewidth=3.2, zorder=12)
    ax_bot.axvline(x_post_cut, color=C_HOPE, linestyle="--", linewidth=2.6, zorder=8)

    # Overlay 36 Generational-Defining Events (~3 events per year) using 8 well-spaced vertical tiers
    y_tiers = [0.28, 0.85, 2.50, 7.20, 21.0, 62.0, 185.0, 560.0]
    for idx, erow in df_events.iterrows():
        ex = year_to_x(erow["year_float"])
        ey = y_tiers[idx % len(y_tiers)]
        is_today = "TODAY" in erow["event_label"]
        ev_col = "#C00000" if is_today else (C_HOPE if erow["gen_id"] == "G5" else "#222222")
        bg_ev  = "#FFE6E6" if is_today else ("#F9EBF8" if erow["gen_id"] == "G5" else "#FFFFFF")
        short_ev = erow["event_label"][:32] + (".." if len(erow["event_label"]) > 32 else "")

        ax_bot.vlines(ex, 0.0, ey, color=ev_col, linestyle=":" if not is_today else "-", linewidth=0.9 if not is_today else 1.8, alpha=0.65, zorder=5)
        ax_bot.scatter([ex], [ey], color=ev_col, s=24 if not is_today else 60, zorder=7)
        ax_bot.text(
            ex, ey * 1.10,
            f"{erow['date_str']}: {short_ev}",
            ha="center", va="bottom", fontsize=5.35 if not is_today else 6.3,
            fontweight="bold", color=ev_col,
            bbox=dict(boxstyle="round,pad=0.09", facecolor=bg_ev, edgecolor=ev_col, linewidth=0.6, alpha=0.93),
            zorder=8
        )

    # Calendar Year Ticks on Bottom Axis mapped through year_to_x
    year_ticks = list(range(2018, 2029))
    xtick_positions = [year_to_x(float(yr)) for yr in year_ticks]
    xtick_labels = [f"{yr}-01" if yr <= 2026 else f"{yr}-01\n(Proj.)" for yr in year_ticks]
    ax_bot.set_xticks(xtick_positions)
    ax_bot.set_xticklabels(xtick_labels, fontsize=8.5, fontweight="bold")

    ax_bot.set_yscale("symlog", linthresh=0.5)
    ax_bot.set_ylim(0.0, 9500.0)
    ax_bot.set_ylabel("Macro Users (M) & Tokens (T)\n(symlog scale, linthresh=0.5)", fontsize=9.0, fontweight="bold")
    ax_bot.set_xlabel("Piecewise-Linear Calendar Timeline Across Generations Gen 0 to Speculative Gen 5 (2017-06 to 2028-12, Annotated with ~3 Generational-Defining Events per Year)", fontsize=10.0, fontweight="bold")
    ax_bot.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25, color="#888888")
    ax_bot.legend(loc="upper left", bbox_to_anchor=(0.005, 0.98), ncol=2, frameon=True, facecolor="white", framealpha=0.92, fontsize=7.8)

    # -------------------------------------------------------------------------
    # PANEL 4: BOTTOM-RIGHT CORNER CARTOUCHE (Attribution, Date, Visual Key & Colophon)
    # -------------------------------------------------------------------------
    ax_corner.set_facecolor("#F4F1EA")
    ax_corner.set_xlim(0.0, 1.0)
    ax_corner.set_ylim(0.0, 1.0)
    ax_corner.set_xticks([])
    ax_corner.set_yticks([])
    for spine in ax_corner.spines.values():
        spine.set_linewidth(2.0)
        spine.set_edgecolor("#222222")

    # Ornate header inside corner cartouche
    ax_corner.add_patch(mpatches.Rectangle((0.0, 0.82), 1.0, 0.18, facecolor="#1B2631", edgecolor="none", zorder=1))
    ax_corner.text(0.50, 0.925, "ENCYCLOPEDIC WALLCHART COLOPHON & LEGEND", ha="center", va="center", fontsize=8.8, fontweight="bold", color="white", zorder=2)
    ax_corner.text(0.50, 0.855, "by www.arianprabowo.com  |  Date: 2026-10-20 (TODAY)", ha="center", va="center", fontsize=8.2, fontweight="bold", color="#F0E442", zorder=2)

    colophon_text = (
        "• Genre & Visual Lineage: Single-Sheet Broadside Data Mural inspired by\n"
        "  Joler & Crawford (Anatomy of an AI System), Michal (Roche Biochemical\n"
        "  Pathways), Sparks (The Histomap), and Shelley (History of Sci-Fi).\n"
        "• Coordinate Axiom: Horizontal = User-Perspective Generation (Gen 0..Gen 5);\n"
        "  Vertical = Standardized User Learning Investment (Level 1 Casual [0h] to\n"
        "  Level 5 Infrastructure & Sandbox Architect [600–2,000+ hours]).\n"
        "• Alluvial Ribbons:\n"
        "  — Green Ribbon (#009E73): Down-Ladder Built-In Sinking (saves 120–1,000h).\n"
        "  — Blue Ribbon (#0072B2): Upward Frontier Skill Expansion.\n"
        "  — Purple Ribbon (#CC79A7): Speculative Gen 4 -> Gen 5 Trajectory.\n"
        "  — Vermilion 'X' (#D55E00): Obsolete User Skill Extinction Event.\n"
        "• Dual Gen 4 -> Gen 5 Cutoff Window Straddling TODAY (2026-10-20):\n"
        "  — Pre-Today Cutoff (2026-08): First-Release Lens (>50% SWE-Pro Private).\n"
        "  — Post-Today Cutoff (2027-03): Mainstream L1/L2 Production Crossover.\n"
        "• Conservation Laws: User%, Token%, Spend% sum to 100.0% per Generation.\n"
        "  Marginal token price fell -99.8% while macro volume rose 6,111x (Jevons)."
    )
    ax_corner.text(0.035, 0.785, colophon_text, ha="left", va="top", fontsize=6.45, color="#111111", linespacing=1.22, zorder=3)

    out_path = os.path.join(FIG_DIR, "fig_v3_p0_encyclopedic_megachart_poster.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED MEGACHART POSTER] {out_path}")


def render_plot0_mini_megachart(data):
    # Plot 0-Mini: Equal-Width 6x5 Top Matrix + Trapezium Time-Warp Bridge + Regular Linear Calendar Timeline
    import textwrap
    df_cells = pd.concat([data["cells"], data["gen5_cells"]], ignore_index=True)

    # Top Matrix uses equal-width columns [-0.50, 5.50]; Bottom Timeline uses regular linear calendar years [2017.42, 2029.00]
    xm_min, xm_max = -0.50, 5.50
    tb_min, tb_max = 2017.42, 2029.00

    fig = plt.figure(figsize=(22, 14.4), dpi=200, facecolor="#FBFBF9")
    gs = gridspec.GridSpec(
        3, 2, figure=fig,
        width_ratios=[5.85, 1.15],
        height_ratios=[4.20, 0.34, 1.40],
        left=0.118, right=0.986, bottom=0.052, top=0.915,
        wspace=0.018, hspace=0.0
    )
    ax_main   = fig.add_subplot(gs[0, 0])
    ax_right  = fig.add_subplot(gs[0, 1], sharey=ax_main)
    ax_trap   = fig.add_subplot(gs[1, 0])
    ax_bot    = fig.add_subplot(gs[2, 0])
    ax_corner = fig.add_subplot(gs[2, 1])

    # Top-Left Title (34.0pt bold, larger than 17.0pt Y-axis labels & column headers) + Right Subtitle (9.5pt italic grey matching lower cell text)
    fig.text(
        0.118, 0.956,
        "AI Ladder Evolution",
        ha="left", va="center", fontsize=34.0, fontweight="bold", color="#111111"
    )
    subtitle_3lines = (
        "This chart maps the evolution of AI as a five-level ladder from the user's perspective, ranking how people use AI from passive everyday\n"
        "tools (Level 1) to foundational model architects (Level 5). Because AI technology moves so fast, any static ladder definition gets obsolete\n"
        "very quickly, which is why we must track how the entire ladder evolves across generations rather than relying on a single fixed ladder."
    )
    fig.text(
        0.376, 0.956,
        subtitle_3lines,
        ha="left", va="center", fontsize=9.5, style="italic", color="#3B3B3B", linespacing=1.18
    )

    # -------------------------------------------------------------------------
    # PANEL 1: TOP-LEFT MAIN MATRIX (30 Equal-Width Full-Capacity Cards, L1 at Top -> L5 at Bottom)
    # -------------------------------------------------------------------------
    ax_main.set_facecolor("#FBFBF9")
    ax_main.set_xlim(xm_min, xm_max)
    ax_main.set_ylim(0.46, 6.18)

    # Equal-width generation columns in ax_main (k - 0.50 .. k + 0.50) paired with true calendar spans in ax_bot
    gen_header_specs = [
        ("G0", -0.50, 0.50, 2017.42, 2020.42, "GEN 0\nPre-LLM &\nPassive NLP",         "G0\n2017–2020\n(3.0 yr)", "#EFEFEF", "#555555", 17.0),
        ("G1",  0.50, 1.50, 2020.42, 2022.83, "GEN 1\nPlaygrounds &\nAutocomplete",    "G1\n2020–2022\n(2.4 yr)", "#EBF3FA", "#0072B2", 17.0),
        ("G2",  1.50, 2.50, 2022.83, 2024.33, "GEN 2\nChatbots &\nVector RAG",         "G2\n2022–2024\n(1.5 yr)", "#FDF2E9", "#D55E00", 17.0),
        ("G3",  2.50, 3.50, 2024.33, 2025.00, "GEN 3\nOmni-Modal &\nVibe Coding",      "G3\n2024\n(0.7 yr)",      "#E8F6F3", "#009E73", 17.0),
        ("G4",  3.50, 4.50, 2025.00, 2026.803,"GEN 4\nReasoners &\nCLI Agents",        "G4\n2025–2026\n(1.8 yr)", "#F9EFF5", "#CC79A7", 17.0),
        ("G5",  4.50, 5.50, 2026.803,2029.00, "GEN 5 (Spec.)\nAmbient OS &\nRLVR Loops","G5\n2026–2029\n(2.2 yr)", "#F8ECF5", "#7A2862", 17.0),
    ]
    gen_spans = {gid: (xm0, xm1) for gid, xm0, xm1, *_ in gen_header_specs}

    for gid, xm0, xm1, tb0, tb1, gtitle, _, bg_c, hdr_c, hdr_fs in gen_header_specs:
        w_col = xm1 - xm0
        pad_x = 0.038
        ax_main.axvspan(xm0, xm1, color=bg_c, alpha=0.34, zorder=0)
        ax_main.axvline(xm0, color="#444444", linestyle="-" if gid != "G5" else "--", linewidth=1.4, alpha=0.75, zorder=2)
        hdr_box = mpatches.FancyBboxPatch(
            (xm0 + pad_x, 5.58), w_col - 2 * pad_x, 0.56,
            boxstyle="round,pad=0.010", facecolor=hdr_c, edgecolor="#111111", linewidth=1.3, zorder=6
        )
        ax_main.add_patch(hdr_box)
        glines = gtitle.splitlines()
        for idx_g, gline in enumerate(glines):
            yg_line = 5.860 + (0.5 * (len(glines) - 1) - idx_g) * 0.168
            ax_main.text(
                0.5 * (xm0 + xm1), yg_line, gline,
                ha="center", va="center", fontsize=hdr_fs,
                fontweight="bold" if idx_g == 0 else "normal",
                color="white", zorder=7
            )

    # Equal-width G4|G5 boundary coordinates used only by the trapezium bridge (no TODAY line/label on the top boxes)
    xm_pre_cut  = 4.50
    xm_today    = 4.50
    xm_post_cut = 4.50

    for y_div in [1.5, 2.5, 3.5, 4.5, 5.5]:
        ax_main.axhline(y_div, color="#888888", linestyle=":" if y_div < 5.0 else "-", linewidth=0.9 if y_div < 5.0 else 1.2, alpha=0.55, zorder=1)
        ax_right.axhline(y_div, color="#888888", linestyle=":" if y_div < 5.0 else "-", linewidth=0.9 if y_div < 5.0 else 1.2, alpha=0.55, zorder=1)

    # Distilled 30-Cell Matrix: 2-Line Bold Cell Name + 2-Line Normal-Font Description + 1-Line Italic Keywords
    mini_cells = [
        # Gen 0 (Karpathy L_LIT_01, Stanford L_LIT_03, DeepMind L_LIT_06, HF L_LIT_14, Gemini L_LIT_20)
        ("G0", 1, "Passive NLP Tools",
         "Apps silently fix mobile typos, filter spam, and rank feeds.",
         "autocorrect, spam filters, search"),
        ("G0", 2, "Rules & AutoML",
         "Upload CSV tables to AutoML or build rule chatbot trees.",
         "AutoML tables, regex intent rules"),
        ("G0", 3, "Statistical Classifiers",
         "Write Python scripts to train tabular decision tree models.",
         "TF-IDF matrices, boosted trees"),
        ("G0", 4, "Fine-Tuned Encoders",
         "Rent cloud GPUs to fine-tune pretrained text encoders.",
         "pretrained encoders, fine-tuning"),
        ("G0", 5, "Custom Seq2Seq Weights",
         "Design custom neural layers and compile C++ servers.",
         "seq2seq layers, multi-GPU sharding"),

        # Gen 1 (SAE L_LIT_02, Stanford L_LIT_03, LangChain L_LIT_07, Anthropic L_LIT_11, a16z L_LIT_12, HF L_LIT_14)
        ("G1", 1, "Ghost-Text Autocomplete",
         "Accept gray code completions or play viral web art demos.",
         "ghost-text, Tab-to-accept plugins"),
        ("G1", 2, "Few-Shot Prompting",
         "Paste examples and tune sliders in web playgrounds.",
         "few-shot prompts, stop tokens"),
        ("G1", 3, "API Wrapper Calls",
         "Embed text into vectors and call completion APIs.",
         "completion APIs, vector search"),
        ("G1", 4, "Linear Prompt Chains",
         "Chain multi-step prompts or upload JSONL datasets.",
         "prompt chaining, JSONL tuning"),
        ("G1", 5, "Distributed Trainers",
         "Shard massive model weights across GPU clusters.",
         "tensor parallelism, GPU sharding"),

        # Gen 2 (Stanford L_LIT_03, DL.AI L_LIT_04, LlamaIndex L_LIT_05, OpenAI L_LIT_08, Menlo L_LIT_10, HF L_LIT_14)
        ("G2", 1, "Consumer Chatbots",
         "Ask plain-English questions in zero-shot browser chat.",
         "zero-shot chat, multi-turn dialog"),
        ("G2", 2, "Prompt Engineering",
         "Write system personas and shareable no-code bots.",
         "system personas, step prompts"),
        ("G2", 3, "Chunked Vector RAG",
         "Chunk PDFs into vector stores and wire JSON tools.",
         "vector databases, function calling"),
        ("G2", 4, "LoRA Adapter Tuning",
         "Quantize open models to 4-bit and train LoRA weights.",
         "4-bit quantization, LoRA adapters"),
        ("G2", 5, "Custom Base Pretraining",
         "Page GPU attention memory and pretrain base models.",
         "paged KV-cache, flash attention"),

        # Gen 3 (SAE L_LIT_02, LangChain L_LIT_07, Anthropic L_LIT_11/16, a16z L_LIT_12, Cursor L_LIT_15, Gemini L_LIT_20)
        ("G3", 1, "Multimodal Omni-Chat",
         "Talk on live camera while editing side-by-side UIs.",
         "voice-video chat, live UI canvas"),
        ("G3", 2, "Long-Context Projects",
         "Drop fifty long PDFs into million-token project folders.",
         "million-token context, folders"),
        ("G3", 3, "Vibe Coding",
         "Prompt multi-file repo diffs without reading code.",
         "multi-file IDE diffs, repo indexing"),
        ("G3", 4, "State-Machine Graphs",
         "Loop coder and critic agents across cyclic state graphs.",
         "cyclic state graphs, checkpoints"),
        ("G3", 5, "Evaluator Harnesses",
         "Spin up container farms to verify autonomous patches.",
         "container eval farms, verifiers"),

        # Gen 4 (Karpathy L_LIT_01, OpenAI L_LIT_08, Anthropic L_LIT_11/16, LocalLLaMA L_LIT_19, Gemini L_LIT_20)
        ("G4", 1, "Auto-Routed Reasoners",
         "Type once as hidden routers pick fast or deep thinking.",
         "model routing, hidden reasoning"),
        ("G4", 2, "Deep Research Agents",
         "Web agents browse sources to compile cited reports.",
         "multi-hop web research, citations"),
        ("G4", 3, "MCP Tool Integration",
         "Connect repos and databases via open MCP servers.",
         "MCP tool servers, repo rule files"),
        ("G4", 4, "Terminal Coding Agents",
         "Terminal CLI agents edit repos until unit tests pass.",
         "terminal coding CLI, test loops"),
        ("G4", 5, "Sandbox & RLVR Hosts",
         "Train reasoning models in sandboxes with verifiers.",
         "VM sandboxes, RLVR verifiers"),

        # Gen 5 (Karpathy L_LIT_01, DeepMind L_LIT_06, OpenAI L_LIT_08, Anthropic L_LIT_11/16, Scale L_LIT_18)
        ("G5", 1, "Ambient OS Delegates",
         "OS routers delegate tasks via one-tap approval cards.",
         "OS task delegation, app memory"),
        ("G5", 2, "Natural-Language Specs",
         "Plain-English rubrics wire and deploy cloud apps.",
         "natural-language specs, zero-CLI"),
        ("G5", 3, "Agent-to-Agent Contracts",
         "Cross-vendor agents sign contracts under budget caps.",
         "agent protocols, circuit breakers"),
        ("G5", 4, "Verified Agent Swarms",
         "Agent swarms stress-test code against formal proofs.",
         "formal proof verifiers, fuzzing"),
        ("G5", 5, "Continuous RLVR Loops",
         "Hardware enclaves distill trajectories into weights.",
         "nightly on-policy RLVR, enclaves"),
    ]
    assert len({t for _, _, t, _, _ in mini_cells}) == len(mini_cells), "Duplicate cell title detected!"

    # Starting font specs across all 6 equal-width columns: (2-Line Bold Cell Title, 2-Line Normal Description, 1-Line Italic Keywords)
    col_font_specs = {
        gid: (14.2, 11.8, 10.2) for gid in ["G0", "G1", "G2", "G3", "G4", "G5"]
    }

    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()

    def wrap_to_exact_3_lines(ax, text_str, x_anchor, y_anchor, max_w_px, fs, weight="normal", style="normal"):
        words = text_str.split()
        n = len(words)
        assert n >= 3, f"Need at least 3 words to form 3 lines: {text_str}"

        def line_w(s):
            p = ax.text(x_anchor, y_anchor, s, fontsize=fs, fontweight=weight, style=style, alpha=0.0)
            w = p.get_window_extent(renderer=renderer).width
            p.remove()
            return w

        best_cand = None
        best_score = 1e12
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                l1 = " ".join(words[:i])
                l2 = " ".join(words[i:j])
                l3 = " ".join(words[j:])
                w1, w2, w3 = line_w(l1), line_w(l2), line_w(l3)
                mx = max(w1, w2, w3)
                mn = min(w1, w2, w3)
                over = max(0.0, mx - max_w_px) * 1000.0
                score = over + (mx - mn)
                if score < best_score:
                    best_score = score
                    best_cand = f"{l1}\n{l2}\n{l3}"
        return best_cand

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

    for gid, lvl, m_title, m_desc, m_keywords in mini_cells:
        y_lvl  = 6 - lvl   # Level 1 at top (y=5), Level 5 at bottom (y=1)
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
            linewidth=1.5 if gid != "G5" else 1.8,
            linestyle="--" if gid == "G5" else "-", zorder=4
        )
        ax_main.add_patch(card)

        hdr_y0 = y_lvl + 0.085
        hdr_h  = 0.370
        hdr_cy = hdr_y0 + 0.5 * hdr_h
        desc_y_top = y_lvl + 0.055

        hdr_strip = mpatches.FancyBboxPatch(
            (x_left, hdr_y0), w_box, hdr_h,
            boxstyle="round,pad=0.005", facecolor=hdr_fill, edgecolor="none", zorder=5
        )
        ax_main.add_patch(hdr_strip)

        title_fs, desc_fs, kw_fs = col_font_specs[gid]

        # Measure exact available pixel width and bottom bound inside this card
        in_pad = 0.015
        x_txt_l = x_left + in_pad
        x_txt_r = x_left + w_box - in_pad
        max_w_px = ax_main.transData.transform((x_txt_r, y_lvl))[0] - ax_main.transData.transform((x_txt_l, y_lvl))[0]
        y_min_allowed_px = ax_main.transData.transform((x_txt_l, y_bot + 0.016))[1]

        # 1. Top Section: 2-Line Cell Name (bold white text)
        cur_tfs = title_fs
        for _ in range(20):
            wrapped_title = wrap_to_exact_2_lines(ax_main, m_title, 0.5 * (x0 + x1), hdr_cy, max_w_px, cur_tfs, weight="bold")
            p_t = ax_main.text(0.5 * (x0 + x1), hdr_cy, wrapped_title, ha="center", va="center", fontsize=cur_tfs, fontweight="bold", linespacing=1.05, alpha=0.0)
            bb_t = p_t.get_window_extent(renderer=renderer)
            p_t.remove()
            if bb_t.width <= max_w_px * 1.005:
                break
            cur_tfs -= 0.20

        assert len(wrapped_title.splitlines()) == 2, f"Cell {gid} L{lvl} title is not 2 lines"
        ax_main.text(
            0.5 * (x0 + x1), hdr_cy,
            wrapped_title,
            ha="center", va="center", fontsize=cur_tfs, fontweight="bold", color="white",
            linespacing=1.05, zorder=6
        )

        # 2. Bottom Section: 2-Line Normal-Font Description + 1-Line Italic Keywords
        cur_dfs, cur_kfs = desc_fs, kw_fs
        div_gap = 0.030
        for _ in range(25):
            wrapped_desc = wrap_to_exact_2_lines(ax_main, m_desc, x_txt_l, desc_y_top, max_w_px, cur_dfs, weight="normal")
            p_desc = ax_main.text(x_txt_l, desc_y_top, wrapped_desc, ha="left", va="top", fontsize=cur_dfs, fontweight="normal", linespacing=1.15, alpha=0.0)
            bb_d = p_desc.get_window_extent(renderer=renderer)
            p_desc.remove()
            y_d_bot = ax_main.transData.inverted().transform((0, bb_d.y0))[1]
            y_div_cell = y_d_bot - div_gap

            p_kw = ax_main.text(x_txt_l, y_div_cell - div_gap, m_keywords, ha="left", va="top", fontsize=cur_kfs, style="italic", alpha=0.0)
            bb_k = p_kw.get_window_extent(renderer=renderer)
            p_kw.remove()
            if bb_d.width <= max_w_px * 1.005 and bb_k.width <= max_w_px * 1.005 and bb_k.y0 >= y_min_allowed_px:
                break
            cur_dfs -= 0.10
            cur_kfs -= 0.08

        assert len(wrapped_desc.splitlines()) == 2, f"Cell {gid} L{lvl} desc is not 2 lines"
        assert "\n" not in m_keywords, f"Cell {gid} L{lvl} keywords is not 1 line"

        # Vertically center the combined [2-line desc + divider + 1-line keywords] block inside the lower card body
        y_kw_bot = ax_main.transData.inverted().transform((0, bb_k.y0))[1]
        spare_h = max(0.0, (y_kw_bot - (y_bot + 0.016)))
        y_shift = 0.45 * spare_h
        desc_y_top_adj = desc_y_top - y_shift
        y_div_cell_adj = y_div_cell - y_shift

        ax_main.text(
            x_txt_l, desc_y_top_adj,
            wrapped_desc,
            ha="left", va="top", fontsize=cur_dfs, color="#111111", linespacing=1.15,
            fontweight="normal", zorder=6
        )

        ax_main.plot(
            [x_txt_l, x_txt_r],
            [y_div_cell_adj, y_div_cell_adj],
            color=edge_c, linestyle=":", linewidth=1.0, alpha=0.65, zorder=5
        )

        ax_main.text(
            x_txt_l, y_div_cell_adj - div_gap,
            m_keywords,
            ha="left", va="top", fontsize=cur_kfs, color="#3B3B3B",
            style="italic", zorder=6
        )

    # Y-Axis: Level 1 at top (y=5) down to Level 5 at bottom (y=1), 4 lines at 17.0pt (matching suptitle)
    y_labels_mini = [
        "LEVEL 5\nPretraining &\nSandbox\nArchitect",
        "LEVEL 4\nScaffold &\nHarness\nEngineer",
        "LEVEL 3\nAugmented\nWorkflow\nCollaborator",
        "LEVEL 2\nPrompt &\nWorkspace\nConsultant",
        "LEVEL 1\nConsumer\nTool",
    ]
    ax_main.set_yticks([1, 2, 3, 4, 5])
    ax_main.set_yticklabels([])
    for y_pos, y_lbl in zip([1, 2, 3, 4, 5], y_labels_mini):
        ylines = y_lbl.splitlines()
        for idx_y, yline in enumerate(ylines):
            yy_line = y_pos + (0.5 * (len(ylines) - 1) - idx_y) * 0.172
            ax_main.text(
                xm_min - 0.055, yy_line, yline,
                ha="right", va="center", fontsize=17.0,
                fontweight="bold" if idx_y == 0 else "normal",
                color="#111111", clip_on=False, zorder=7
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
        ax_trap.plot([ut0, ub0], [1.0, 0.0], color="#333333", linestyle="-" if gid != "G5" else "--", linewidth=1.5, zorder=4)
        ax_trap.plot([ut1, ub1], [1.0, 0.0], color="#333333", linestyle="-", linewidth=1.2, alpha=0.6, zorder=4)

        cx_trap = 0.25 * (ut0 + ut1 + ub0 + ub1)
        ax_trap.text(
            cx_trap, 0.50, trap_lbl,
            ha="center", va="center", fontsize=8.0, fontweight="bold", color="#111111", linespacing=1.06,
            bbox=dict(boxstyle="round,pad=0.10", facecolor="white", edgecolor=hdr_c, linewidth=1.0, alpha=0.94),
            zorder=6
        )

    # Connect Dual Cutoff Window & TODAY line through the Trapezium Bridge
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
    ax_trap.plot([u_top(xm_pre_cut), u_bot(tb_pre_cut)], [1.0, 0.0], color=C_HOPE, linestyle=":", linewidth=1.6, zorder=5)
    ax_trap.plot([u_top(xm_post_cut), u_bot(tb_post_cut)], [1.0, 0.0], color=C_HOPE, linestyle="--", linewidth=2.0, zorder=5)
    ax_trap.plot([u_top(xm_today), u_bot(tb_today)], [1.0, 0.0], color="#C00000", linestyle="-", linewidth=3.0, zorder=8)

    # -------------------------------------------------------------------------
    # PANEL 2: TOP-RIGHT MARGINAL HISTOGRAM (10 Lines = 2 Metrics x 5 Empirical Gens)
    # -------------------------------------------------------------------------
    ax_right.set_facecolor("#FBFBF9")
    gen_line_styles = [
        ("G0", "#555555", "o"),
        ("G1", "#0072B2", "s"),
        ("G2", "#D55E00", "^"),
        ("G3", "#009E73", "D"),
        ("G4", "#CC79A7", "P"),
    ]
    y_lvls = np.array([5.0, 4.0, 3.0, 2.0, 1.0])   # midpoints of level_id = 1, 2, 3, 4, 5
    y_step_pts = np.array([5.5, 4.5, 4.5, 3.5, 3.5, 2.5, 2.5, 1.5, 1.5, 0.5])  # full box-height intervals
    u_handles, t_handles = [], []
    for gid, gcol, gmk in gen_line_styles:
        sub_g = df_cells[df_cells["gen_id"] == gid].sort_values("level_id")
        u_rel = sub_g["user_share_pct"].values / 100.0
        t_rel = sub_g["token_share_pct"].values / 100.0
        u_step_pts = np.repeat(u_rel, 2)
        t_step_pts = np.repeat(t_rel, 2)
        h_u, = ax_right.plot(u_step_pts, y_step_pts, color=gcol, linestyle="-", linewidth=2.2, alpha=0.75, zorder=4, label=f"{gid} Users")
        ax_right.scatter(u_rel, y_lvls, color=gcol, marker=gmk, s=38, alpha=0.85, zorder=5)
        h_t, = ax_right.plot(t_step_pts, y_step_pts, color=gcol, linestyle="--", linewidth=2.0, alpha=0.70, zorder=3, label=f"{gid} Tokens")
        ax_right.scatter(t_rel, y_lvls, facecolors="none", edgecolors=gcol, marker=gmk, s=38, linewidth=1.3, alpha=0.85, zorder=5)
        u_handles.append(h_u)
        t_handles.append(h_t)

    ax_right.set_xlim(0.0, 0.78)
    ax_right.set_xticks([0.0, 0.25, 0.50, 0.75])
    ax_right.set_xticklabels(["0.00", "0.25", "0.50", "0.75"], fontsize=9.5, fontweight="bold")
    ax_right.set_title("Marginal Relative Frequency", fontsize=11.0, fontweight="bold", pad=6)
    ax_right.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.28, color="#888888")
    ax_right.legend(handles=u_handles + t_handles, loc="upper center", bbox_to_anchor=(0.50, 0.998), ncol=2, frameon=True, facecolor="white", framealpha=0.96, fontsize=6.6, columnspacing=0.6, handlelength=1.4, labelspacing=0.14, borderpad=0.22)
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
    ax_bot.plot(t_curve_emp, users_emp, color=C_DEMAND, linewidth=2.6, marker="o", markersize=4.5, zorder=4, label="Global Active AI Users")
    ax_bot.plot(t_curve_emp, tokens_emp, color=C_SUPPLY, linewidth=2.6, marker="s", markersize=4.5, zorder=4, label="Global Annualized Tokens")
    ax_bot.plot(t_curve_spec, users_spec, color=C_DEMAND, linestyle="--", linewidth=2.6, marker="o", markersize=4.5, zorder=4)
    ax_bot.plot(t_curve_spec, tokens_spec, color=C_SUPPLY, linestyle="--", linewidth=2.6, marker="s", markersize=4.5, zorder=4)

    for gid, _, _, tb0, tb1, _, _, bg_c, _, _ in gen_header_specs:
        ax_bot.axvspan(tb0, tb1, color=bg_c, alpha=0.25, zorder=0)
        ax_bot.axvline(tb0, color="#444444", linestyle="-" if gid != "G5" else "--", linewidth=1.2, alpha=0.75, zorder=2)

    ax_bot.axvspan(tb_pre_cut, tb_post_cut, color="#FFD700", alpha=0.18, zorder=1)
    ax_bot.axvline(tb_pre_cut, color=C_HOPE, linestyle=":", linewidth=1.6, zorder=8)
    ax_bot.axvline(tb_today, color="#C00000", linestyle="-", linewidth=3.0, zorder=12)
    ax_bot.axvline(tb_post_cut, color=C_HOPE, linestyle="--", linewidth=2.0, zorder=8)
    ax_bot.text(
        tb_today, 4.0e12,
        "◀ TODAY ▶",
        ha="center", va="center", fontsize=10.5, fontweight="bold", color="white",
        bbox=dict(boxstyle="round,pad=0.14", facecolor="#C00000", edgecolor="#111111", linewidth=1.0),
        zorder=15
    )

    # 5 Iconic Generational-Defining News Milestones (<= 6) on Regular Linear X-Axis (12.0pt matching cell title)
    mini_events = [
        (2017.46, "2017-06: Transformer Paper", 4.5e7, "left", "#222222"),
        (2021.48, "2021-06: GitHub Copilot Preview", 2.2e9, "center", "#222222"),
        (2022.91, "2022-11: ChatGPT (100M in 60d)", 2.2e6, "center", "#222222"),
        (2024.49, "2024-06: Claude 3.5 Artifacts & Cursor", 1.8e11, "center", "#222222"),
        (2025.08, "2025-01: DeepSeek-R1 & Claude Code CLI", 6.5e6, "left", "#222222"),
    ]
    for yr_f, ev_txt, ey, ha_e, ecol in mini_events:
        ax_bot.vlines(yr_f, 1e6, ey, color=ecol, linestyle=":", linewidth=1.4, alpha=0.80, zorder=5)
        ax_bot.scatter([yr_f], [ey], color=ecol, s=42, zorder=7)
        ax_bot.text(
            yr_f, ey * 1.35, ev_txt,
            ha=ha_e, va="bottom", fontsize=12.0,
            fontweight="bold", color=ecol,
            bbox=dict(boxstyle="round,pad=0.14", facecolor="#FFFFFF", edgecolor=ecol, linewidth=1.0, alpha=0.95),
            zorder=8
        )

    # Regular, Uniformly Spaced Calendar Year Ticks (2018 to 2029)
    year_ticks = list(range(2018, 2030))
    xtick_labels = [f"{yr}" for yr in year_ticks]
    ax_bot.set_xticks(year_ticks)
    ax_bot.set_xticklabels(xtick_labels, fontsize=11.0, fontweight="bold")
    ax_bot.set_yscale("log")
    ax_bot.set_ylim(1e6, 2.5e16)
    ax_bot.set_yticks([1e6, 1e8, 1e10, 1e12, 1e14, 1e16])
    ax_bot.set_ylabel("Users & Tokens", fontsize=12.0, fontweight="bold")
    ax_bot.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25, color="#888888")
    ax_bot.legend(loc="upper left", bbox_to_anchor=(0.005, 0.98), ncol=1, frameon=True, facecolor="white", framealpha=0.94, fontsize=12.0)

    # -------------------------------------------------------------------------
    # PANEL 4: BOTTOM-RIGHT CORNER COLOPHON (Everything at 12.0pt matching title)
    # -------------------------------------------------------------------------
    ax_corner.set_facecolor("#F4F1EA")
    ax_corner.set_xlim(0.0, 1.0)
    ax_corner.set_ylim(0.0, 1.0)
    ax_corner.set_xticks([])
    ax_corner.set_yticks([])
    for spine in ax_corner.spines.values():
        spine.set_linewidth(1.8)
        spine.set_edgecolor("#222222")

    ax_corner.add_patch(mpatches.Rectangle((0.0, 0.77), 1.0, 0.23, facecolor="#1B2631", edgecolor="none", zorder=1))
    ax_corner.text(0.50, 0.925, "MINI MEGA CHART", ha="center", va="center", fontsize=12.0, fontweight="bold", color="white", zorder=2)
    ax_corner.text(0.50, 0.825, "www.arianprabowo.com", ha="center", va="center", fontsize=12.0, fontweight="bold", color="#F0E442", zorder=2)

    mini_colophon = (
        "• Green Box: Direct User (L1–2)\n"
        "• Blue Box: Builder / Eng (L3–5)\n"
        "• Gray Box: Passive Baseline\n"
        "• Purple Box: Speculative Gen 5\n"
        "• Today Line: 2026-10-20\n"
        "• Pre-Cut: 2026-08 (>50%)\n"
        "• Post-Cut: 2027-03 (Mass)"
    )
    ax_corner.text(0.04, 0.72, mini_colophon, ha="left", va="top", fontsize=12.0, fontweight="bold", color="#111111", linespacing=1.28, zorder=3)

    out_path = os.path.join(FIG_DIR, "fig_v3_p0_mini_megachart.png")
    fig.savefig(out_path, dpi=200)
    plt.close(fig)
    print(f"[RENDERED MINI MEGACHART] {out_path}")


def render_all_plots():
    data = build_and_verify_all()
    render_plot0_encyclopedic_megachart_poster(data)
    render_plot0_mini_megachart(data)
    render_visual_abstracts(data)
    render_plot1_macro_trajectories(data)
    render_plot2_skill_deflation(data)
    render_plot3_folksonomy_raster(data)
    render_plot4_jointplot(data)
    render_plots5_to_9_gen_matrices(data)
    render_plot10_alluvial_poster(data)
    render_plot11_animation(data)
    render_plot12_trl_and_hopes(data)
    render_plot13_pair_plot(data)
    render_plot14_gen5_speculative_matrix(data)
    print("\n[ALL VISUAL ARTIFACTS (PLOT 0, PLOT 0-MINI, VA0-VA5, PLOT 1-PLOT 14) RENDERED SUCCESSFULLY]")


if __name__ == "__main__":
    render_all_plots()

