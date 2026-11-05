import os
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import matplotlib.gridspec as gridspec

# Import ERAS, PALETTE, and existing drawing functions from generate_visuals
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generate_visuals as gv

PALETTE = gv.PALETTE
ERAS = gv.ERAS
WORKSPACE_FIG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "figures"))
PERSONAL_FIG_DIR = "/Users/z3540725/My Drive/personal/figures"
os.makedirs(WORKSPACE_FIG_DIR, exist_ok=True)
os.makedirs(PERSONAL_FIG_DIR, exist_ok=True)

def save_both(fig, fname, dpi=220):
    p1 = os.path.join(WORKSPACE_FIG_DIR, fname)
    p2 = os.path.join(PERSONAL_FIG_DIR, fname)
    fig.savefig(p1, dpi=dpi, bbox_inches="tight", facecolor="white")
    fig.savefig(p2, dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Rendered {fname}")

def draw_card(ax, x, y, w, h, title, lines, edge_color, bg_color="#F8FAFC", badge=None):
    rect = patches.FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.015,rounding_size=0.03",
        facecolor=bg_color, edgecolor=edge_color, linewidth=1.8, zorder=2
    )
    ax.add_patch(rect)
    stripe_w = w * 0.035
    stripe = patches.FancyBboxPatch(
        (x, y), stripe_w, h, boxstyle="round,pad=0.005,rounding_size=0.02",
        facecolor=edge_color, edgecolor=edge_color, linewidth=0.5, zorder=3
    )
    ax.add_patch(stripe)
    ax.text(x + stripe_w + 0.02*w, y + h - 0.22*h, title, fontsize=8.8, fontweight="bold", color=PALETTE["TEXT"], va="center", zorder=4)
    for idx, line in enumerate(lines):
        ax.text(x + stripe_w + 0.02*w, y + h - (0.48 + idx*0.22)*h, line, fontsize=7.9, color=PALETTE["SUBTEXT"], va="center", zorder=4)
    if badge:
        ax.text(
            x + w - 0.025*w, y + h - 0.22*h, badge,
            fontsize=7.3, fontweight="bold", color=edge_color, ha="right", va="center",
            bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor=edge_color, lw=1.0), zorder=4
        )

# ==============================================================================
# 1. VISUAL ABSTRACTS (Root + Parts I, II, III, IV, V)
# ==============================================================================

def render_va0_root():
    fig = plt.figure(figsize=(18.5, 8.8), dpi=220, facecolor="white")
    gs = gridspec.GridSpec(2, 3, width_ratios=[1.35, 1.15, 0.26], height_ratios=[1.05, 0.95], wspace=0.18, hspace=0.28, left=0.045, right=0.97, top=0.86, bottom=0.08)
    fig.suptitle("Visual Abstract: Nine-Year Evolution of AI, LLM & Agentic Ladders (2017-06 to 2026-10)", fontsize=14.5, fontweight="bold", color=PALETTE["TEXT"], x=0.045, ha="left", y=0.96)
    fig.text(0.045, 0.91, "Five Empirically Locked Era Ladders (L1–L5, 23 Complexity Steps)  •  Four Governing Laws  •  2,000x Price Deflation Driving 4,000x Larger Agent Horizons", fontsize=9.5, color=PALETTE["SUBTEXT"])

    # Panel A (Top-Left): 5-Era Staircase & Downward Sinking
    ax_a = fig.add_subplot(gs[0, 0])
    ax_a.set_xlim(0, 10)
    ax_a.set_ylim(0, 6.2)
    ax_a.axis("off")
    ax_a.set_title("A. Five Chronological Era Ladders & 18-Month Downward Sinking", fontsize=10.5, fontweight="bold", color=PALETTE["TEXT"], loc="left", pad=6)

    era_boxes = [
        (0.2, 0.8, "L1: 2017–20", "Encoders (BERT)", "4 Steps | 2k tok\n1.8M Users | $2.8B", PALETTE["GONE"]),
        (2.15, 1.5, "L2: 2020–22", "Completion (GPT-3)", "4 Steps | 50k tok\n4.5M Users | $3.2B", PALETTE["SUNK"]),
        (4.1, 2.3, "L3: 2022–24", "Web Chat & RAG", "5 Steps | 180k tok\n250M Users | $10.5B", PALETTE["EVOLVED"]),
        (6.05, 3.2, "L4: 2024–25", "Multimodal, IDE & o1", "5 Steps | 1.2M tok\n480M Users | $18.5B", PALETTE["SPLIT"]),
        (8.0, 4.1, "L5: 2025–26", "CLI, MCP & Fleets", "5 Steps | 8.0M tok\n1.15B Users | $95B", PALETTE["NEW"]),
    ]
    for x, y, title, sub, stats, col in era_boxes:
        rect = patches.FancyBboxPatch((x, y), 1.75, 1.75, boxstyle="round,pad=0.03,rounding_size=0.08", facecolor="#F8FAFC", edgecolor=col, lw=2.0, zorder=3)
        ax_a.add_patch(rect)
        ax_a.text(x+0.875, y+1.42, title, ha="center", va="center", fontsize=8.5, fontweight="bold", color=col)
        ax_a.text(x+0.875, y+1.02, sub, ha="center", va="center", fontsize=8.0, fontweight="bold", color=PALETTE["TEXT"])
        ax_a.text(x+0.875, y+0.45, stats, ha="center", va="center", fontsize=7.2, color=PALETTE["SUBTEXT"])
        ax_a.annotate("", xy=(x+0.875, 0.35), xytext=(x+0.875, y-0.05), arrowprops=dict(arrowstyle="-|>", lw=1.3, color=PALETTE["SUNK"], ls="--"))

    ax_a.plot([0.2, 9.7], [0.3, 0.3], color=PALETTE["SUNK"], lw=2.2)
    ax_a.text(4.95, 0.05, "Step 1 Default UI Baseline (Absorbs Prior Era's Advanced Engineering Rungs Every 18–24 Months)", ha="center", va="center", fontsize=8.0, fontweight="bold", color=PALETTE["SUNK"])

    # Panel B (Bottom-Left): Four Governing Laws Cards
    ax_b = fig.add_subplot(gs[1, 0])
    ax_b.set_xlim(0, 10)
    ax_b.set_ylim(0, 5.2)
    ax_b.axis("off")
    ax_b.set_title("B. Four Repeating Structural & Economic Laws Across All Nine Years", fontsize=10.5, fontweight="bold", color=PALETTE["TEXT"], loc="left", pad=6)
    laws = [
        (0.1, 2.7, 4.8, 2.2, "Law 1: 18-Mo Step Sinking", ["New ladder requires >=2 simultaneous step shifts.", "L2 API prompt -> L3 Chat; L3 PDF RAG -> L4 Upload."], PALETTE["SUNK"], "Commoditization"),
        (5.1, 2.7, 4.8, 2.2, "Law 2: Jevons Token Paradox", ["2,000x price drop (USD 60 -> 0.06/1M tok) unlocked", "4,000x larger loops (2k -> 8M tok) & USD 37B+ spend."], PALETTE["ACTUAL"], "2,000x -> 4,000x"),
        (0.1, 0.2, 4.8, 2.2, "Law 3: Pareto Inversion", ["Step 1 serves 55%–68% of users at <USD 0.01/turn;", "Top 12% of users (L5 S4–S5) consume 50% of tokens."], PALETTE["NEW"], "r = 0.60 Pareto"),
        (5.1, 0.2, 4.8, 2.2, "Law 4: Labor Migration", ["Data Curator (L1) -> Prompt Crafter (L2) -> RAG", "Plumber (L3) -> Diff Reviewer (L4) -> Fleet Cmdr (L5)."], PALETTE["SPLIT"], "Human Role Shift"),
    ]
    for x, y, w, h, t, lns, c, b in laws:
        draw_card(ax_b, x, y, w, h, t, lns, c, badge=b)

    # Panel C (Right Full Height + Marginal): CITRA Timeseries of Price, Spend, Max Tokens, and User Count
    ax_c = fig.add_subplot(gs[:, 1])
    ax_cm = fig.add_subplot(gs[:, 2], sharey=ax_c)
    years = np.arange(2017, 2027)
    price = np.array([150.0, 110.0, 80.0, 60.0, 30.0, 20.0, 2.0, 0.15, 0.07, 0.04])
    spend = np.array([0.2, 0.35, 0.6, 0.9, 1.4, 2.2, 4.5, 13.8, 37.0, 62.0])
    max_tok_k = np.array([0.5, 0.512, 1.0, 2.0, 4.0, 12.0, 180.0, 1200.0, 5000.0, 8000.0])
    users_m = np.array([0.8, 1.2, 1.8, 2.5, 3.5, 4.5, 180.0, 480.0, 850.0, 1150.0])

    ax_c.set_yscale("log")
    ax_c.plot(years, price, "-o", color=PALETTE["ACTUAL"], lw=2.2, label="Baseline Price (USD / 1M Tokens)")
    ax_c.plot(years, spend, "-s", color=PALETTE["DEMAND"], lw=2.2, label="Annual Enterprise AI Spend (USD B)")
    ax_c.plot(years, max_tok_k, "--^", color=PALETTE["SUPPLY"], lw=2.2, label="Top-Step Single-Task Tokens ($10^3$ tok)")
    ax_c.plot(years, users_m, ":D", color=PALETTE["MODELLED"], lw=2.2, label="Active Monthly Practitioners/Users ($10^6$)")
    ax_c.set_xticks(years)
    ax_c.set_xticklabels([str(y) for y in years], fontsize=8.5, fontweight="bold")
    ax_c.set_ylabel("Log10 Scale (USD/1M | USD B | $10^3$ Tok | $10^6$ Users)", fontsize=9, fontweight="bold")
    ax_c.set_title("C. Empirical Macro Scaling Trajectory (2017–2026)", fontsize=10.5, fontweight="bold", color=PALETTE["TEXT"], loc="left", pad=6)
    ax_c.grid(True, which="both", linestyle="--", color=PALETTE["GRID"], alpha=0.65)
    ax_c.legend(loc="upper left", fontsize=8.0, frameon=True, facecolor="white", framealpha=0.92)

    bins = np.geomspace(0.02, 1.5e4, 14)
    ax_cm.hist(price, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["ACTUAL"])
    ax_cm.hist(spend, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["DEMAND"])
    ax_cm.hist(max_tok_k, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["SUPPLY"])
    ax_cm.hist(users_m, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["MODELLED"])
    ax_cm.set_xlabel("Years", fontsize=8.5, fontweight="bold")
    ax_cm.tick_params(labelleft=False)
    ax_cm.set_title("Marginal", fontsize=9.5, fontweight="bold", color=PALETTE["TEXT"])
    ax_cm.grid(True, which="both", linestyle=":", color=PALETTE["GRID"], alpha=0.5)

    save_both(fig, "fig_va0_root_report.png")

def render_va1_part1():
    fig = plt.figure(figsize=(18.0, 7.5), dpi=220, facecolor="white")
    gs = gridspec.GridSpec(1, 3, width_ratios=[1.25, 1.15, 0.25], wspace=0.18, left=0.045, right=0.97, top=0.83, bottom=0.10)
    fig.suptitle("Part I Visual Abstract: Executive Digest of the Five-Part Synthesis (2017–2026)", fontsize=14, fontweight="bold", color=PALETTE["TEXT"], x=0.045, ha="left", y=0.95)
    fig.text(0.045, 0.89, "Left: Four-Part Report Architecture Digest (Sections 1.1–1.4)  •  Right: Cross-Era Top-Step Cost vs. Compute Concentration Trajectory", fontsize=9.3, color=PALETTE["SUBTEXT"])

    ax_l = fig.add_subplot(gs[0])
    ax_l.set_xlim(0, 10)
    ax_l.set_ylim(0, 8.8)
    ax_l.axis("off")
    ax_l.set_title("A. Four-Pillar Executive Summary Architecture (Sections 1.1 to 1.4)", fontsize=10.5, fontweight="bold", color=PALETTE["TEXT"], loc="left", pad=6)

    cards = [
        (0.1, 6.65, 9.8, 1.9, "1.1 Literature, Evidence & Cost Digest (Part II)", ["18 published ladders (Karpathy, DeepMind, OpenAI, Anthropic, Shapiro, Huyen) + 9 yrs of HAI,", "Menlo (USD 1.7B -> 37B), OpenRouter 100T tok, CS224N & Stack Overflow data across 5 cost units."], PALETTE["DEMAND"], "18 Ladders + 5 Units"),
        (0.1, 4.45, 9.8, 1.9, "1.2 Applied Four-Rule Scientific Method (Part III)", ["Rule 1: >=2 Simultaneous Step Shifts per Era | Rule 2: Bottom-Up Usage + Top-Down Ladder Pass", "Rule 3: MECE 2-of-3 Step Split Test (Scope, Autonomy, 10x Cost) | Rule 4: 5 Lineage Categories."], PALETTE["EVOLVED"], "4 MECE Rules"),
        (0.1, 2.25, 9.8, 1.9, "1.3 Five Chronological Era Ladders L1–L5 (Part IV)", ["L1 Encoders (4 steps) -> L2 Completion/Copilot (4 steps) -> L3 ChatGPT/RAG (5 steps) ->", "L4 Multimodal/Cursor/o1 (5 steps) -> L5 CLI/Deep Research/MCP/Fleets (5 steps = 23 total)."], PALETTE["SPLIT"], "5 Eras / 23 Steps"),
        (0.1, 0.05, 9.8, 1.9, "1.4 Four Evolutionary Laws & Master Matrix (Part V)", ["18-Mo Downward Sinking | 2,000x Price -> 4,000x Token Jevons Paradox | Top 12% Users = 50%", "Compute Pareto Inversion | Human Labor Shift from CSV Curator to Parallel Fleet Commander."], PALETTE["NEW"], "4 Macro Laws"),
    ]
    for x, y, w, h, t, lns, c, b in cards:
        draw_card(ax_l, x, y, w, h, t, lns, c, badge=b)

    ax_r = fig.add_subplot(gs[1])
    ax_rm = fig.add_subplot(gs[2], sharey=ax_r)
    era_x = np.arange(1, 6)
    era_labels = ["L1\n(17–20)", "L2\n(20–22)", "L3\n(22–24)", "L4\n(24–25)", "L5\n(25–26)"]
    era_spend_b = np.array([2.8, 3.2, 10.5, 18.5, 95.0])
    era_users_m = np.array([1.8, 4.5, 250.0, 480.0, 1150.0])
    era_twh = np.array([0.95, 0.24, 0.50, 3.80, 48.0])
    top_tok_m = np.array([0.002, 0.05, 0.18, 1.2, 8.0])

    ax_r.set_yscale("log")
    ax_r.plot(era_x, era_users_m, "-o", color=PALETTE["DEMAND"], lw=2.3, label="Active Monthly Users ($10^6$)")
    ax_r.plot(era_x, era_spend_b, "-s", color=PALETTE["ACTUAL"], lw=2.3, label="Total Era Spending (USD Billions)")
    ax_r.plot(era_x, era_twh, "--^", color=PALETTE["MODELLED"], lw=2.3, label="Total Era Electricity (TWh)")
    ax_r.plot(era_x, top_tok_m, ":D", color=PALETTE["SUPPLY"], lw=2.3, label="Top-Step Single-Task Tokens ($10^6$)")
    ax_r.set_xticks(era_x)
    ax_r.set_xticklabels(era_labels, fontsize=8.5, fontweight="bold")
    ax_r.set_ylabel("Log10 Macro Scale Across Eras L1 to L5", fontsize=9, fontweight="bold")
    ax_r.set_title("B. Five-Era Macro Scaling Summary (L1 to L5)", fontsize=10.5, fontweight="bold", color=PALETTE["TEXT"], loc="left", pad=6)
    ax_r.grid(True, which="both", linestyle="--", color=PALETTE["GRID"], alpha=0.65)
    ax_r.legend(loc="upper left", fontsize=8.0, frameon=True, facecolor="white", framealpha=0.92)

    bins = np.geomspace(1e-3, 2e3, 12)
    ax_rm.hist(era_users_m, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["DEMAND"])
    ax_rm.hist(era_spend_b, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["ACTUAL"])
    ax_rm.hist(era_twh, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["MODELLED"])
    ax_rm.hist(top_tok_m, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["SUPPLY"])
    ax_rm.set_xlabel("Eras", fontsize=8.5, fontweight="bold")
    ax_rm.tick_params(labelleft=False)
    ax_rm.set_title("Marginal", fontsize=9.5, fontweight="bold", color=PALETTE["TEXT"])
    ax_rm.grid(True, which="both", linestyle=":", color=PALETTE["GRID"], alpha=0.5)

    save_both(fig, "fig_va1_part1_summary.png")

def render_va2_part2():
    fig = plt.figure(figsize=(18.0, 7.6), dpi=220, facecolor="white")
    gs = gridspec.GridSpec(1, 3, width_ratios=[1.15, 1.2, 0.25], wspace=0.18, left=0.045, right=0.97, top=0.83, bottom=0.10)
    fig.suptitle("Part II Visual Abstract: Literature Catalog (18 Ladders), Empirical Sources & Two-Level Cost System", fontsize=14, fontweight="bold", color=PALETTE["TEXT"], x=0.045, ha="left", y=0.95)
    fig.text(0.045, 0.89, "Synthesizing 18 Published Frameworks (Section 2.1), Four Empirical Evidence Pillars (Section 2.2) & Five Physical Cost Units (Section 2.3)", fontsize=9.3, color=PALETTE["SUBTEXT"])

    ax_l = fig.add_subplot(gs[0])
    ax_l.set_xlim(0, 10)
    ax_l.set_ylim(0, 8.8)
    ax_l.axis("off")
    ax_l.set_title("A. Three Published Ladder Traditions & Five Coupled Cost Units", fontsize=10.5, fontweight="bold", color=PALETTE["TEXT"], loc="left", pad=6)
    cards = [
        (0.1, 6.0, 9.8, 2.5, "Section 2.1: 18 Published Ladders Across 3 Traditions (2017–2026)", [
            "1. Lab/Academic (6): Karpathy Software 1.0–3.0 & Slider, DeepMind AGI, OpenAI L1–L5, Anthropic, CoALA",
            "2. Industry/Coding (7): Shapiro & Yegge L0–L5, LangChain, HuggingFace, a16z/Sequoia/Menlo, Gartner",
            "3. Practitioner NLP/LLM (5): Huyen, Eugene Yan 7 Patterns, OpenAI DevDay, Ruder, Liu et al."
        ], PALETTE["DEMAND"], "18 Frameworks"),
        (0.1, 3.1, 9.8, 2.5, "Section 2.2: 4 Empirical Evidence Pillars (2017–2026)", [
            "1. Macro Reports: Stanford HAI, State of AI, Epoch AI (Compute 3.3e18 -> 1e26+ FLOPs)",
            "2. Billing Logs: Menlo (USD 1.7B -> 37B), OpenRouter (100T tok), Ramp, Stripe, Cloudflare",
            "3. Courses & Surveys: CS224N/CS324, Fast.ai, DeepLearning.AI, Stack Overflow (84% AI), Octoverse"
        ], PALETTE["EVOLVED"], "4 Data Pillars"),
        (0.1, 0.2, 9.8, 2.5, "Section 2.3: Two-Level Cost System & 5 Physical Units", [
            "Level 1 Single-Task vs. Level 2 Industry Share (Sums = 100% per Era)",
            "Units: (1) Tokens, (2) FLOPs (2*N*T infer, 6*N*D train), (3) Energy Wh/MWh, (4) USD, (5) Time",
            "2,000x API Deflation: USD 60/1M (davinci 2020) -> USD 2 (3.5-turbo 2023) -> USD 0.06 (Flash 2026)"
        ], PALETTE["SUPPLY"], "5 Coupled Units"),
    ]
    for x, y, w, h, t, lns, c, b in cards:
        draw_card(ax_l, x, y, w, h, t, lns, c, badge=b)

    ax_r = fig.add_subplot(gs[1])
    ax_rm = fig.add_subplot(gs[2], sharey=ax_r)
    years = np.arange(2017, 2027)
    train_flops_e18 = np.array([3.3, 190.0, 2500.0, 3.14e5, 8.0e5, 2.5e6, 2.15e7, 5.0e7, 1.2e8, 2.5e8])
    api_price = np.array([150.0, 110.0, 80.0, 60.0, 30.0, 20.0, 2.0, 0.15, 0.07, 0.04])
    adoption_pct = np.array([20.0, 27.0, 37.0, 50.0, 56.0, 50.0, 55.0, 78.0, 84.0, 88.0])

    ax_r.set_yscale("log")
    ax_r.plot(years, train_flops_e18, "-^", color=PALETTE["SUPPLY"], lw=2.3, label="Frontier Training Compute ($10^{18}$ FLOPs)")
    ax_r.plot(years, api_price, "-o", color=PALETTE["ACTUAL"], lw=2.3, label="Baseline API Token Price (USD / 1M tok)")
    ax_r.plot(years, adoption_pct, "--s", color=PALETTE["DEMAND"], lw=2.3, label="Enterprise / Developer AI Adoption (%)")
    ax_r.set_xticks(years)
    ax_r.set_xticklabels([str(y) for y in years], fontsize=8.5, fontweight="bold")
    ax_r.set_ylabel("Log10 Scale ($10^{18}$ FLOPs | USD/1M | Adoption %)", fontsize=9, fontweight="bold")
    ax_r.set_title("B. Frontier Training Compute vs. Inference Price & Adoption (2017–2026)", fontsize=10.5, fontweight="bold", color=PALETTE["TEXT"], loc="left", pad=6)
    ax_r.grid(True, which="both", linestyle="--", color=PALETTE["GRID"], alpha=0.65)
    ax_r.legend(loc="upper left", fontsize=8.0, frameon=True, facecolor="white", framealpha=0.92)

    bins = np.geomspace(0.02, 5e8, 16)
    ax_rm.hist(train_flops_e18, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["SUPPLY"])
    ax_rm.hist(api_price, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["ACTUAL"])
    ax_rm.hist(adoption_pct, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["DEMAND"])
    ax_rm.set_xlabel("Years", fontsize=8.5, fontweight="bold")
    ax_rm.tick_params(labelleft=False)
    ax_rm.set_title("Marginal", fontsize=9.5, fontweight="bold", color=PALETTE["TEXT"])
    ax_rm.grid(True, which="both", linestyle=":", color=PALETTE["GRID"], alpha=0.5)

    save_both(fig, "fig_va2_part2_literature.png")

def render_va3_part3():
    fig = plt.figure(figsize=(18.0, 7.4), dpi=220, facecolor="white")
    gs = gridspec.GridSpec(1, 2, width_ratios=[1.25, 1.0], wspace=0.18, left=0.045, right=0.97, top=0.83, bottom=0.10)
    fig.suptitle("Part III Visual Abstract: Four-Step Applied Ladder-Building & MECE Verification Method", fontsize=14, fontweight="bold", color=PALETTE["TEXT"], x=0.045, ha="left", y=0.95)
    fig.text(0.045, 0.89, "How Raw Literature, Syllabi & Billing Logs Are Filtered into 5 Era Ladders (L1–L5) and 23 Mutually Exclusive Steps (Sections 3.1–3.4)", fontsize=9.3, color=PALETTE["SUBTEXT"])

    ax_l = fig.add_subplot(gs[0])
    ax_l.set_xlim(0, 10)
    ax_l.set_ylim(0, 8.8)
    ax_l.axis("off")
    ax_l.set_title("A. Four-Stage Methodological Funnel (Sections 3.1 to 3.4)", fontsize=10.5, fontweight="bold", color=PALETTE["TEXT"], loc="left", pad=6)
    stages = [
        (0.1, 6.65, 9.8, 1.9, "Stage 3.1: Two-Shift Era Cutoff Audit (Timeline Partitioning)", ["Requires >=2 simultaneous structural step changes (sinking, splitting, or new top step).", "Accepts 5 Era Cutoffs (2017-06, 2020-06, 2022-11, 2024-06, 2025-02); rejects 2 single upgrades."], PALETTE["DEMAND"], "5 Eras Locked"),
        (0.1, 4.45, 9.8, 1.9, "Stage 3.2: Bottom-Up Usage + Top-Down Published Reconciliation", ["Clusters real developer/enterprise workflows first, then aligns with 18 published ladders.", "Adds L1-S1 Cloud APIs & L5-S2 Deep Research; sets aside unverified OpenAI L4/L5 & ASI."], PALETTE["EVOLVED"], "Dual-Pass Filter"),
        (0.1, 2.25, 9.8, 1.9, "Stage 3.3: MECE Two-of-Three Step Split Verification Matrix", ["Adjacent steps (k -> k+1) split ONLY if >=2 of 3 axes jump: (1) Task Scope, (2) Tool/Autonomy,", "(3) 10x–100x Single-Task Cost Scale. Guarantees zero overlap and 100% era share coverage."], PALETTE["SPLIT"], "2-of-3 Split Proof"),
        (0.1, 0.05, 9.8, 1.9, "Stage 3.4: Locked Master Skeleton & Cross-Era Lineage Links", ["Every step linked across eras via 5 mechanisms: Old Step Sinking into Default UI (5),", "Evolved Workhorse (5), Split Step (5), New Breakthrough Step (6), or Combined/Gone (2)."], PALETTE["NEW"], "23 Steps Linked"),
    ]
    for x, y, w, h, t, lns, c, b in stages:
        draw_card(ax_l, x, y, w, h, t, lns, c, badge=b)

    ax_r = fig.add_subplot(gs[1])
    eras = ["L1 (17–20)", "L2 (20–22)", "L3 (22–24)", "L4 (24–25)", "L5 (25–26)"]
    sunk = np.array([1, 1, 1, 1, 1])
    evolved = np.array([1, 1, 2, 1, 1])
    split_s = np.array([0, 1, 1, 1, 2])
    new_s = np.array([1, 1, 1, 2, 1])
    gone_s = np.array([1, 0, 0, 0, 0])

    x = np.arange(len(eras))
    w = 0.55
    ax_r.bar(x, sunk, w, label="Old Step Sinking into Default Step 1 UI", color=PALETTE["SUNK"], alpha=0.9)
    ax_r.bar(x, evolved, w, bottom=sunk, label="Evolved Core Engineering Workhorse", color=PALETTE["EVOLVED"], alpha=0.9)
    ax_r.bar(x, split_s, w, bottom=sunk+evolved, label="Split & Specialized Step", color=PALETTE["SPLIT"], alpha=0.9)
    ax_r.bar(x, new_s, w, bottom=sunk+evolved+split_s, label="New Breakthrough Step", color=PALETTE["NEW"], alpha=0.9)
    ax_r.bar(x, gone_s, w, bottom=sunk+evolved+split_s+new_s, label="Legacy Step Gone in Next Era", color=PALETTE["GONE"], alpha=0.9)

    for idx, tot in enumerate([4, 4, 5, 5, 5]):
        ax_r.text(idx, tot + 0.12, f"{tot} Steps", ha="center", va="bottom", fontsize=9, fontweight="bold", color=PALETTE["TEXT"])

    ax_r.set_xticks(x)
    ax_r.set_xticklabels(eras, fontsize=9, fontweight="bold")
    ax_r.set_ylim(0, 6.2)
    ax_r.set_ylabel("Number of Verified Steps per Era Ladder", fontsize=9, fontweight="bold")
    ax_r.set_title("B. Composition of the 23 Verified Steps by Transition Mechanism", fontsize=10.5, fontweight="bold", color=PALETTE["TEXT"], loc="left", pad=6)
    ax_r.grid(True, axis="y", linestyle="--", color=PALETTE["GRID"], alpha=0.65)
    ax_r.legend(loc="upper left", fontsize=8.0, frameon=True, facecolor="white", framealpha=0.92)

    save_both(fig, "fig_va3_part3_method.png")

def render_va4_part4():
    fig = plt.figure(figsize=(18.5, 7.8), dpi=220, facecolor="white")
    gs = gridspec.GridSpec(1, 3, width_ratios=[1.15, 0.25, 1.15], wspace=0.20, left=0.045, right=0.97, top=0.83, bottom=0.10)
    fig.suptitle("Part IV Visual Abstract: Chronological Evolution & Resource Totals Across All Five Era Ladders (L1–L5)", fontsize=14, fontweight="bold", color=PALETTE["TEXT"], x=0.045, ha="left", y=0.95)
    fig.text(0.045, 0.89, "Left: Five-Era Macro Totals (Users, Tokens, FLOPs, Electricity & Spend) with Marginal Histogram  •  Right: 100% Share Shift from Step 1 to Top Agentic Rungs", fontsize=9.3, color=PALETTE["SUBTEXT"])

    ax_l = fig.add_subplot(gs[0])
    ax_lm = fig.add_subplot(gs[1], sharey=ax_l)
    era_x = np.arange(1, 6)
    era_labels = ["L1\n2017–20", "L2\n2020–22", "L3\n2022–24", "L4\n2024–25", "L5\n2025–26"]
    users_m = np.array([1.8, 4.5, 250.0, 480.0, 1150.0])
    tokens_t = np.array([4.5, 18.0, 450.0, 350.0, 180000.0])
    spend_b = np.array([2.8, 3.2, 10.5, 18.5, 95.0])
    energy_twh = np.array([0.95, 0.24, 0.50, 3.80, 48.0])

    ax_l.set_yscale("log")
    ax_l.plot(era_x, tokens_t, "-^", color=PALETTE["SUPPLY"], lw=2.3, label="Total Era Tokens ($10^{12}$ Trillions)")
    ax_l.plot(era_x, users_m, "-o", color=PALETTE["DEMAND"], lw=2.3, label="Active Monthly Users ($10^6$ Millions)")
    ax_l.plot(era_x, spend_b, "-s", color=PALETTE["ACTUAL"], lw=2.3, label="Total Era Spend (USD Billions)")
    ax_l.plot(era_x, energy_twh, "--D", color=PALETTE["MODELLED"], lw=2.3, label="Total Era Electricity (TWh)")
    ax_l.set_xticks(era_x)
    ax_l.set_xticklabels(era_labels, fontsize=8.5, fontweight="bold")
    ax_l.set_ylabel("Log10 Era Macro Totals", fontsize=9, fontweight="bold")
    ax_l.set_title("A. Era-Wide Macro Totals Across L1–L5 (Sections 4.1–4.5)", fontsize=10.5, fontweight="bold", color=PALETTE["TEXT"], loc="left", pad=6)
    ax_l.grid(True, which="both", linestyle="--", color=PALETTE["GRID"], alpha=0.65)
    ax_l.legend(loc="upper left", fontsize=8.0, frameon=True, facecolor="white", framealpha=0.92)

    bins = np.geomspace(0.1, 3e5, 14)
    ax_lm.hist(tokens_t, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["SUPPLY"])
    ax_lm.hist(users_m, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["DEMAND"])
    ax_lm.hist(spend_b, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["ACTUAL"])
    ax_lm.hist(energy_twh, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["MODELLED"])
    ax_lm.set_xlabel("Eras", fontsize=8.5, fontweight="bold")
    ax_lm.tick_params(labelleft=False)
    ax_lm.set_title("Marginal", fontsize=9.5, fontweight="bold", color=PALETTE["TEXT"])
    ax_lm.grid(True, which="both", linestyle=":", color=PALETTE["GRID"], alpha=0.5)

    # Panel B: Compute Share by Step Rank (S1 to S5) across L1..L5
    ax_r = fig.add_subplot(gs[2])
    step_colors = [PALETTE["SUNK"], PALETTE["SPLIT"], PALETTE["EVOLVED"], PALETTE["NEW"], "#7C3AED"]
    comp_matrix = np.array([
        [15, 25, 40, 20, 0],   # L1
        [18, 22, 15, 45, 0],   # L2
        [32, 28, 23, 10, 7],   # L3
        [22, 16, 34, 18, 10],  # L4
        [12, 16, 22, 30, 20],  # L5
    ])
    user_s1 = [62, 50, 68, 62, 55]
    bottom = np.zeros(5)
    for s_idx in range(5):
        vals = comp_matrix[:, s_idx]
        ax_r.bar(era_x, vals, width=0.52, bottom=bottom, color=step_colors[s_idx], alpha=0.9, label=f"Step {s_idx+1} Compute/Token Share %")
        for e_i, v in enumerate(vals):
            if v >= 10:
                ax_r.text(era_x[e_i], bottom[e_i] + v/2, f"S{s_idx+1}: {v}%", ha="center", va="center", fontsize=8.0, fontweight="bold", color="white")
        bottom += vals

    ax_r.plot(era_x, user_s1, "--o", color="#0F172A", lw=2.2, label="Step 1 User Headcount Share (%)")
    for e_i, u in enumerate(user_s1):
        ax_r.text(era_x[e_i]+0.18, u+2, f"{u}% S1 Users", fontsize=7.5, fontweight="bold", color="#0F172A")

    ax_r.set_xticks(era_x)
    ax_r.set_xticklabels(era_labels, fontsize=8.5, fontweight="bold")
    ax_r.set_ylim(0, 115)
    ax_r.set_ylabel("Share of Era Total Compute / Tokens (%)", fontsize=9, fontweight="bold")
    ax_r.set_title("B. Era Compute Share by Step (Bars) vs. Step 1 User Share (Line)", fontsize=10.5, fontweight="bold", color=PALETTE["TEXT"], loc="left", pad=6)
    ax_r.grid(True, axis="y", linestyle="--", color=PALETTE["GRID"], alpha=0.65)
    ax_r.legend(loc="upper right", fontsize=7.5, ncol=2, frameon=True, facecolor="white", framealpha=0.92)

    save_both(fig, "fig_va4_part4_eras.png")

def render_va5_part5():
    fig = plt.figure(figsize=(18.5, 7.8), dpi=220, facecolor="white")
    gs = gridspec.GridSpec(1, 3, width_ratios=[1.1, 1.15, 0.25], wspace=0.18, left=0.045, right=0.97, top=0.83, bottom=0.10)
    fig.suptitle("Part V Visual Abstract: Four Repeating Laws, Lorenz Compute Concentration & Human-to-AI Time Shift", fontsize=14, fontweight="bold", color=PALETTE["TEXT"], x=0.045, ha="left", y=0.95)
    fig.text(0.045, 0.89, "Left: Lorenz Concentration Curves Across Eras (Law 3)  •  Right: Autonomous AI Runtime vs. Human Setup Minutes Across Top Steps (Law 4)", fontsize=9.3, color=PALETTE["SUBTEXT"])

    # Panel A: Lorenz Curves of User Share vs Compute Share across Eras
    ax_l = fig.add_subplot(gs[0])
    ax_l.plot([0, 100], [0, 100], "--", color=PALETTE["GONE"], lw=1.5, label="Line of Absolute Equality (1% Users = 1% Compute)")
    era_colors = [PALETTE["GONE"], PALETTE["SUNK"], PALETTE["EVOLVED"], PALETTE["SPLIT"], PALETTE["NEW"]]
    for e_idx, era in enumerate(ERAS):
        # Sort steps from lowest compute/user intensity to highest
        steps_sorted = sorted(era["steps"], key=lambda s: s["compute_share"] / s["user_share"])
        cum_u = np.concatenate([[0], np.cumsum([s["user_share"] for s in steps_sorted])])
        cum_c = np.concatenate([[0], np.cumsum([s["compute_share"] for s in steps_sorted])])
        ax_l.plot(cum_u, cum_c, "-o", color=era_colors[e_idx], lw=2.2, label=f"{era['id']} ({era['dates'][:4]}–{era['dates'][11:15]})")

    ax_l.annotate("Era 5 Top 12% Users (S4+S5)\nConsume 50% of All Compute\n(Bottom 88% Users = 50% Compute)", xy=(88, 50), xytext=(42, 22),
                  arrowprops=dict(arrowstyle="->", lw=1.8, color=PALETTE["NEW"]), fontsize=8.5, fontweight="bold", color=PALETTE["NEW"],
                  bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFF7ED", edgecolor=PALETTE["NEW"]))
    ax_l.set_xlim(0, 100)
    ax_l.set_ylim(0, 100)
    ax_l.set_xlabel("Cumulative Percentage of Active Users (Ordered Bottom-to-Top Step)", fontsize=9, fontweight="bold")
    ax_l.set_ylabel("Cumulative Percentage of Total Era Compute & Tokens (%)", fontsize=9, fontweight="bold")
    ax_l.set_title("A. Law 3: Pareto Compute Concentration (Lorenz Curves, L1–L5)", fontsize=10.5, fontweight="bold", color=PALETTE["TEXT"], loc="left", pad=6)
    ax_l.grid(True, linestyle="--", color=PALETTE["GRID"], alpha=0.65)
    ax_l.legend(loc="upper left", fontsize=8.0, frameon=True, facecolor="white", framealpha=0.92)

    # Panel B: Law 1 & Law 4 Trajectory with Right Marginal Histogram
    ax_r = fig.add_subplot(gs[1])
    ax_rm = fig.add_subplot(gs[2], sharey=ax_r)
    era_x = np.arange(1, 6)
    era_labels = ["L1\n(BERT FT)", "L2\n(davinci)", "L3\n(RAG/GPT-4)", "L4\n(Cursor/Devin)", "L5\n(CLI Fleets)"]
    human_workhorse_min = np.array([240.0, 5.0, 6.0, 4.0, 15.0])
    ai_workhorse_min = np.array([45.0, 0.06, 0.8, 0.8, 45.0])
    s1_ai_min = np.array([0.005, 0.01, 0.03, 0.15, 0.10])
    top_ai_min = np.array([14400.0, 360.0, 15.0, 20.0, 45.0])

    ax_r.set_yscale("log")
    ax_r.plot(era_x, human_workhorse_min, "-o", color=PALETTE["DEMAND"], lw=2.3, label="Workhorse Human Steering Time (min)")
    ax_r.plot(era_x, ai_workhorse_min, "-s", color=PALETTE["SUPPLY"], lw=2.3, label="Workhorse Autonomous AI Runtime (min)")
    ax_r.plot(era_x, top_ai_min, "--^", color=PALETTE["NEW"], lw=2.1, label="Top-Step Autonomous AI Runtime (min)")
    ax_r.plot(era_x, s1_ai_min, ":D", color=PALETTE["SUNK"], lw=2.1, label="Step 1 Default UI AI Latency (min)")
    ax_r.set_xticks(era_x)
    ax_r.set_xticklabels(era_labels, fontsize=8.5, fontweight="bold")
    ax_r.set_ylabel("Wall-Clock Duration per Task (Minutes, Log10)", fontsize=9, fontweight="bold")
    ax_r.set_title("B. Law 4: Human Steering vs. Autonomous AI Runtime Across Eras", fontsize=10.5, fontweight="bold", color=PALETTE["TEXT"], loc="left", pad=6)
    ax_r.grid(True, which="both", linestyle="--", color=PALETTE["GRID"], alpha=0.65)
    ax_r.legend(loc="upper right", fontsize=7.8, frameon=True, facecolor="white", framealpha=0.92)

    bins = np.geomspace(1e-3, 2e4, 14)
    ax_rm.hist(human_workhorse_min, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["DEMAND"])
    ax_rm.hist(ai_workhorse_min, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["SUPPLY"])
    ax_rm.hist(top_ai_min, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["NEW"])
    ax_rm.hist(s1_ai_min, bins=bins, orientation="horizontal", histtype="step", lw=1.8, color=PALETTE["SUNK"])
    ax_rm.set_xlabel("Eras", fontsize=8.5, fontweight="bold")
    ax_rm.tick_params(labelleft=False)
    ax_rm.set_title("Marginal", fontsize=9.5, fontweight="bold", color=PALETTE["TEXT"])
    ax_rm.grid(True, which="both", linestyle=":", color=PALETTE["GRID"], alpha=0.5)

    save_both(fig, "fig_va5_part5_laws.png")

if __name__ == "__main__":
    render_va0_root()
    render_va1_part1()
    render_va2_part2()
    render_va3_part3()
    render_va4_part4()
    render_va5_part5()
