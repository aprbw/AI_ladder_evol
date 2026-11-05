# -*- coding: utf-8 -*-
"""
stages_v5/plot_micro_cards.py
=============================
Renders the 20 high-readability Micro Cards for v5:
  1. `fig_v5_p0_micro_sae_card.png` (Plot 0-Micro: 6x6 User-Skill SAE Slide Card)
  2. `fig_v5_p0b_micro_news_card.png` (Plot 0B-Micro: 6x6 Historical News Slide Card)
  3. `fig_v5_micro_gen0_sae.png` .. `fig_v5_micro_gen5_sae.png` (6 Per-Generation 6-Column SAE Cards)
  4. `fig_v5_micro_trl01_transformer.png` .. `fig_v5_micro_trl12_grounded_search.png` (12 4-Stage TRL Cards)
"""

import os
import textwrap
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches


def _two_line_split(text_val: str) -> str:
    """Split a string into at most 2 balanced lines without truncating any words."""
    s = str(text_val).strip()
    if "\n" in s:
        lines = [line.strip() for line in s.splitlines() if line.strip()]
        if len(lines) == 2:
            return "\n".join(lines)
        s = " ".join(lines)
    words = s.split()
    if len(words) <= 2:
        return s
    best_idx = 1
    best_diff = 10**9
    for idx in range(1, len(words)):
        l1 = " ".join(words[:idx])
        l2 = " ".join(words[idx:])
        diff = abs(len(l1) - len(l2))
        if diff < best_diff:
            best_diff = diff
            best_idx = idx
    return " ".join(words[:best_idx]) + "\n" + " ".join(words[best_idx:])


def render_plot0_micro_sae_card(dfs: dict[str, pd.DataFrame], fig_dir: str):
    """Render Plot 0-Micro (`fig_v5_p0_micro_sae_card.png`, figsize=(16, 10), dpi=300)."""
    old_pm = plt.rcParams.get("text.parse_math", True)
    plt.rcParams["text.parse_math"] = False
    p0_df = dfs["poster_encyclopedic_cells"]
    fig, ax = plt.subplots(figsize=(16, 10), dpi=300, facecolor="#FBFBF9")
    fig.subplots_adjust(left=0.135, right=0.985, bottom=0.055, top=0.865)

    fig.text(0.135, 0.945, "AI Ladder Evolution (v5) — 6×6 User-Skill SAE Reference Card",
             fontsize=20.0, fontweight="bold", color="#111111", ha="left", va="center")
    fig.text(0.135, 0.905,
             "Six Cumulative Beeline Effort Rungs (L1: 0h | $0 at Top → L6: ~10,000h | ~$100M+ at Bottom) Across Six Generations (Gen 0 [2017] → Gen 5 [2027+])",
             fontsize=10.5, style="italic", color="#3B3B3B", ha="left", va="center")

    ax.set_facecolor("#FBFBF9")
    ax.set_xlim(-0.5, 5.5)
    ax.set_ylim(0.45, 6.95)
    ax.set_xticks([])
    ax.set_yticks([])

    gen_hdrs = [
        ("G0", 0, "GEN 0 (2017–2020)\nPre-LLM Pipelines", "#555555", "#EFEFEF"),
        ("G1", 1, "GEN 1 (2020–2022)\nPlaygrounds & Tab", "#0072B2", "#EBF3FA"),
        ("G2", 2, "GEN 2 (2022–2024)\nChatbots & RAG", "#D55E00", "#FDF2E9"),
        ("G3", 3, "GEN 3 (2024)\nOmni & Vibe Coding", "#009E73", "#E8F6F3"),
        ("G4", 4, "GEN 4 (2025–2026)\nReasoners & CLI", "#CC79A7", "#F9EFF5"),
        ("G5", 5, "GEN 5 (2027+ Spec.)\nAmbient OS & Mesh", "#7A2862", "#F8ECF5"),
    ]
    for gid, cx, gtitle, hcol, bgcol in gen_hdrs:
        ax.axvspan(cx - 0.5, cx + 0.5, color=bgcol, alpha=0.35, zorder=0)
        hdr = mpatches.FancyBboxPatch((cx - 0.46, 6.48), 0.92, 0.42, boxstyle="round,pad=0.01",
                                      facecolor=hcol, edgecolor="#111111", linewidth=1.2, zorder=5)
        ax.add_patch(hdr)
        ax.text(cx, 6.69, gtitle, ha="center", va="center", fontsize=10.5, fontweight="bold", color="white", linespacing=1.08, zorder=6)

    y_labels = [
        (6, "LEVEL 1\nConsumer Tool\n0h (0d) | $0", "#116649"),
        (5, "LEVEL 2\nWorkspace User\n<50h | <$30", "#116649"),
        (4, "LEVEL 3\nIDE & Integrator\n<200h | <$100", "#0B4F7C"),
        (3, "LEVEL 4\nHarness & Tuning\n~600h | ~$1.5k", "#0B4F7C"),
        (2, "LEVEL 5\nCluster & Sandbox\n~2,000h | ~$500k", "#0B4F7C"),
        (1, "LEVEL 6\nAI Scientist (PhD)\n~10,000h | ~$100M+", "#0B4F7C"),
    ]
    for ypos, ytxt, ycol in y_labels:
        ax.text(-0.56, ypos, ytxt, ha="right", va="center", fontsize=10.5, fontweight="bold", color=ycol, linespacing=1.12, clip_on=False)

    gen_to_x = {g[0]: g[1] for g in gen_hdrs}
    for _, row in p0_df.iterrows():
        gid = row["gen_id"]
        lvl = int(row["level_id"])
        cx = gen_to_x[gid]
        cy = 7 - lvl
        hdr_c = "#7A2862" if gid == "G5" else ("#555555" if (gid == "G0" and lvl == 1) else ("#116649" if lvl <= 2 else "#0B4F7C"))
        card = mpatches.FancyBboxPatch((cx - 0.46, cy - 0.44), 0.92, 0.88, boxstyle="round,pad=0.01",
                                       facecolor="white", edgecolor=hdr_c, linewidth=1.4,
                                       linestyle="--" if gid == "G5" else "-", zorder=3)
        ax.add_patch(card)
        top_bar = mpatches.FancyBboxPatch((cx - 0.46, cy + 0.04), 0.92, 0.40, boxstyle="round,pad=0.005",
                                          facecolor=hdr_c, edgecolor="none", zorder=4)
        ax.add_patch(top_bar)
        title_2l = _two_line_split(row["cell_name"])
        ax.text(cx, cy + 0.24, title_2l, ha="center", va="center", fontsize=8.8, fontweight="bold", color="white", linespacing=1.05, zorder=5)
        micro_kw = textwrap.fill(str(row["micro_keywords_subset"]), width=26)
        ax.text(cx, cy - 0.19, micro_kw, ha="center", va="center", fontsize=7.8, fontweight="bold", color="#222222", linespacing=1.12, zorder=5)

    out_path = os.path.join(fig_dir, "fig_v5_p0_micro_sae_card.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    plt.rcParams["text.parse_math"] = old_pm
    print(f"[RENDERED] {out_path}")


def render_plot0b_micro_news_card(dfs: dict[str, pd.DataFrame], fig_dir: str):
    """Render Plot 0B-Micro (`fig_v5_p0b_micro_news_card.png`, figsize=(16, 10), dpi=300)."""
    old_pm = plt.rcParams.get("text.parse_math", True)
    plt.rcParams["text.parse_math"] = False
    nc_df = dfs["news_megachart_cells"]
    fig, ax = plt.subplots(figsize=(16, 10), dpi=300, facecolor="#FBFBF9")
    fig.subplots_adjust(left=0.145, right=0.985, bottom=0.055, top=0.865)

    fig.text(0.145, 0.945, "AI Historical News & Ecosystem Atlas (v5) — 6×6 Category Slide Card",
             fontsize=20.0, fontweight="bold", color="#111111", ha="left", va="center")
    fig.text(0.145, 0.905,
             "Six Socio-Technical News Categories (CAT 1 Papers at Top → CAT 6 Failed Hopes at Bottom) Across Six Generations (144 Dated Landmarks, 2017–2028)",
             fontsize=10.5, style="italic", color="#3B3B3B", ha="left", va="center")

    ax.set_facecolor("#FBFBF9")
    ax.set_xlim(-0.5, 5.5)
    ax.set_ylim(0.45, 6.95)
    ax.set_xticks([])
    ax.set_yticks([])

    gen_hdrs = [
        ("G0", 0, "GEN 0 (2017–2020)\nTransformer & BERT", "#555555", "#EFEFEF"),
        ("G1", 1, "GEN 1 (2020–2022)\nGPT-3 & Copilot", "#0072B2", "#EBF3FA"),
        ("G2", 2, "GEN 2 (2022–2024)\nChatGPT & Llama-2", "#D55E00", "#FDF2E9"),
        ("G3", 3, "GEN 3 (2024)\nGPT-4o, o1 & R1", "#009E73", "#E8F6F3"),
        ("G4", 4, "GEN 4 (2025–2026)\nGPT-5, CLI & Bartz", "#CC79A7", "#F9EFF5"),
        ("G5", 5, "GEN 5 (2027+ Spec.)\nRubin & Proof Mesh", "#7A2862", "#F8ECF5"),
    ]
    for gid, cx, gtitle, hcol, bgcol in gen_hdrs:
        ax.axvspan(cx - 0.5, cx + 0.5, color=bgcol, alpha=0.35, zorder=0)
        hdr = mpatches.FancyBboxPatch((cx - 0.46, 6.48), 0.92, 0.42, boxstyle="round,pad=0.01",
                                      facecolor=hcol, edgecolor="#111111", linewidth=1.2, zorder=5)
        ax.add_patch(hdr)
        ax.text(cx, 6.69, gtitle, ha="center", va="center", fontsize=10.5, fontweight="bold", color="white", linespacing=1.08, zorder=6)

    cat_labels = [
        (6, "CAT 1: Papers,\nMeta-Laws &\nCoinages", "#6A3D9A"),
        (5, "CAT 2: Model,\nProduct & Local\nReleases", "#0072B2"),
        (4, "CAT 3: Viral,\nPsychosis/Slop &\nSecurity News", "#C00000"),
        (3, "CAT 4: Econ,\nSilicon, Nuclear\n& AI Policy", "#116649"),
        (2, "CAT 5: Courses,\nBenchmarks &\nEval Guides", "#D55E00"),
        (1, "CAT 6: Hype Bets,\nFailed Hopes &\nExtinct Habits", "#555555"),
    ]
    for ypos, ytxt, ycol in cat_labels:
        ax.text(-0.56, ypos, ytxt, ha="right", va="center", fontsize=10.2, fontweight="bold", color=ycol, linespacing=1.12, clip_on=False)

    gen_to_x = {g[0]: g[1] for g in gen_hdrs}
    for _, row in nc_df.iterrows():
        gid = row["gen_id"]
        cidx = int(row["cat_idx"])
        cx = gen_to_x[gid]
        cy = 7 - cidx
        hdr_c = row["category_color"]
        card = mpatches.FancyBboxPatch((cx - 0.46, cy - 0.44), 0.92, 0.88, boxstyle="round,pad=0.01",
                                       facecolor="white", edgecolor=hdr_c, linewidth=1.4,
                                       linestyle="--" if gid == "G5" else "-", zorder=3)
        ax.add_patch(card)
        top_bar = mpatches.FancyBboxPatch((cx - 0.46, cy + 0.04), 0.92, 0.40, boxstyle="round,pad=0.005",
                                          facecolor=hdr_c, edgecolor="none", zorder=4)
        ax.add_patch(top_bar)
        title_2l = _two_line_split(row["cell_name"])
        max_len = max(len(l) for l in title_2l.splitlines())
        t_fs = 6.4 if max_len >= 34 else (6.9 if max_len >= 29 else 7.4)
        ax.text(cx, cy + 0.24, title_2l, ha="center", va="center", fontsize=t_fs, fontweight="bold", color="white", linespacing=1.05, zorder=5)
        micro_kw = textwrap.fill(str(row["micro_keywords_subset"]), width=28)
        ax.text(cx, cy - 0.19, micro_kw, ha="center", va="center", fontsize=7.2, fontweight="bold", color="#222222", linespacing=1.10, zorder=5)

    out_path = os.path.join(fig_dir, "fig_v5_p0b_micro_news_card.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    plt.rcParams["text.parse_math"] = old_pm
    print(f"[RENDERED] {out_path}")


def render_per_gen_sae_cards(dfs: dict[str, pd.DataFrame], fig_dir: str):
    """Render Plot M-G0..M-G5 (`fig_v5_micro_gen0_sae.png` .. `fig_v5_micro_gen5_sae.png`, figsize=(16, 6.5), dpi=300)."""
    old_pm = plt.rcParams.get("text.parse_math", True)
    plt.rcParams["text.parse_math"] = False
    p0_df = dfs["poster_encyclopedic_cells"]
    all_cells = pd.concat([dfs["ladder_cells"], dfs["gen5_speculative"]], ignore_index=True)
    gen_df = dfs["generations"]

    for idx_g, (_, grow) in enumerate(gen_df.iterrows()):
        gid = grow["gen_id"]
        sub_p0 = p0_df[p0_df["gen_id"] == gid].sort_values("level_id")
        sub_c = all_cells[all_cells["gen_id"] == gid].sort_values("level_id")

        fig, ax = plt.subplots(figsize=(16, 6.5), dpi=300, facecolor="#FBFBF9")
        fig.subplots_adjust(left=0.02, right=0.98, bottom=0.04, top=0.82)
        fig.suptitle(f"Plot M-{gid}: {grow['gen_name']} ({grow['start_date']} to {grow['end_date']}) — 6-Column SAE J3016 Reference Card",
                     fontsize=13.5, fontweight="bold", y=0.94, color="#111111")

        ax.set_xlim(0.0, 6.0)
        ax.set_ylim(0.0, 5.65)
        ax.axis("off")

        # Top Spanners: L1-L2 Direct User (#116649) vs L3-L6 Builder/Engineer/Scientist (#0B4F7C)
        sp1 = mpatches.FancyBboxPatch((0.04, 5.05), 1.92, 0.50, boxstyle="round,pad=0.02", facecolor="#116649", edgecolor="#111111", linewidth=1.2)
        sp2 = mpatches.FancyBboxPatch((2.04, 5.05), 3.92, 0.50, boxstyle="round,pad=0.02", facecolor="#0B4F7C", edgecolor="#111111", linewidth=1.2)
        ax.add_patch(sp1)
        ax.add_patch(sp2)
        ax.text(1.00, 5.30, "DIRECT USER — Using AI Without Coding (L1–L2: 0h to <50h | $0 to <$30)",
                ha="center", va="center", fontsize=9.8, fontweight="bold", color="white")
        ax.text(4.00, 5.30, "BUILDER, ENGINEER & SCIENTIST — Making, Training & Inventing AI (L3–L6: <200h to ~10,000h | <$100 to ~$100M+)",
                ha="center", va="center", fontsize=9.8, fontweight="bold", color="white")

        for (_, prow), (_, crow) in zip(sub_p0.iterrows(), sub_c.iterrows()):
            lvl = int(prow["level_id"])
            x0 = lvl - 1.0 + 0.04
            w = 0.92
            col_c = "#116649" if lvl <= 2 else "#0B4F7C"
            if gid == "G5":
                col_c = "#7A2862"
            card = mpatches.FancyBboxPatch((x0, 0.08), w, 4.86, boxstyle="round,pad=0.02",
                                           facecolor="white", edgecolor=col_c, linewidth=1.5)
            ax.add_patch(card)
            hdr = mpatches.FancyBboxPatch((x0, 4.02), w, 0.92, boxstyle="round,pad=0.01",
                                          facecolor=col_c, edgecolor="none")
            ax.add_patch(hdr)
            cx = x0 + 0.5 * w
            t_str = _two_line_split(f"{gid}-L{lvl}: {prow['cell_name']}")
            ax.text(cx, 4.60, t_str, ha="center", va="center", fontsize=8.5, fontweight="bold", color="white", linespacing=1.05)
            ax.text(cx, 4.16, crow["compact_tick_label"], ha="center", va="center", fontsize=7.6, fontweight="bold", color="#F0E442")

            rows_spec = [
                (3.45, "WHAT HUMAN DOES", prow["sae_human_action"], "#EAF6F1" if lvl <= 2 else "#EBF3FA"),
                (2.45, "WHAT AI EXECUTES", prow["sae_ai_executes"], "#FFFFFF"),
                (1.42, "FLAGSHIP TOOLS & MODELS", prow["micro_keywords_subset"], "#F9FBFA"),
            ]
            for ry, rlbl, rval, rbg in rows_spec:
                ax.add_patch(mpatches.Rectangle((x0 + 0.02, ry - 0.42), w - 0.04, 0.92, facecolor=rbg, edgecolor="#DDDDDD", linewidth=0.7))
                ax.text(cx, ry + 0.34, rlbl, ha="center", va="center", fontsize=7.2, fontweight="bold", color=col_c)
                ax.text(cx, ry - 0.05, textwrap.fill(str(rval), width=25), ha="center", va="center", fontsize=7.8, fontweight="bold", color="#151515", linespacing=1.08)

            tu_ratio = round(float(crow["token_share_pct"]) / max(float(crow["user_share_pct"]), 0.01), 2)
            share_txt = f"Users: {crow['user_share_pct']:.1f}% | Tok: {crow['token_share_pct']:.1f}%\nTok/User Intensity: {tu_ratio:g}×"
            ax.add_patch(mpatches.Rectangle((x0 + 0.02, 0.12), w - 0.04, 0.82, facecolor="#1B2631", edgecolor="none"))
            ax.text(cx, 0.53, share_txt, ha="center", va="center", fontsize=7.8, fontweight="bold", color="#F0E442", linespacing=1.18)

        out_path = os.path.join(fig_dir, f"fig_v5_micro_gen{idx_g}_sae.png")
        fig.savefig(out_path, dpi=300)
        plt.close(fig)
        print(f"[RENDERED] {out_path}")
    plt.rcParams["text.parse_math"] = old_pm


def render_per_trl_micro_cards(dfs: dict[str, pd.DataFrame], fig_dir: str):
    """Render Plot M-TRL01..TRL12 (`fig_v5_micro_trl01_transformer.png` .. `fig_v5_micro_trl12_grounded_search.png`)."""
    old_pm = plt.rcParams.get("text.parse_math", True)
    plt.rcParams["text.parse_math"] = False
    trl_df = dfs["trl_trajectories"]

    def _parse_ym_lvl(date_cell_str: str) -> tuple[float, int]:
        parts = str(date_cell_str).split("|")
        ym = parts[0].strip()
        y, m = map(int, ym.split("-"))
        yf = y + (m - 0.5) / 12.0
        cell_part = parts[1].strip() if len(parts) > 1 else "G0-L6"
        lvl = int(cell_part.split("-L")[-1][0]) if "-L" in cell_part else 6
        return yf, lvl

    for idx_t, (_, row) in enumerate(trl_df.iterrows(), start=1):
        fname = row["micro_plot_file"]
        is_tech = row["category_type"] == "Technical"
        main_col = "#0072B2" if is_tech else "#6A3D9A"

        fig = plt.figure(figsize=(16, 5.2), dpi=300, facecolor="#FBFBF9")
        gs = gridspec.GridSpec(1, 2, figure=fig, width_ratios=[1.25, 3.75], wspace=0.06, left=0.055, right=0.985, bottom=0.12, top=0.80)
        ax_l = fig.add_subplot(gs[0, 0])
        ax_r = fig.add_subplot(gs[0, 1])

        fig.suptitle(
            f"Plot M-TRL{idx_t:02d} ({row['lineage_id']} — {row['category_type']}): {row['lineage_name']} (Total Lag: {row['months_trl1_to_9']} Months)",
            fontsize=12.8, fontweight="bold", y=0.93, color="#111111"
        )
        fig.text(0.5, 0.855, f"Primary Bottleneck Resolved: {row['primary_bottleneck_resolved']}",
                 ha="center", va="center", fontsize=9.8, style="italic", color="#333333")

        # Left Panel: 2D Skill-Deflation & TRL Escalator
        stages_dc = [row["s1_date_cell"], row["s2_date_cell"], row["s3_date_cell"], row["s4_date_cell"]]
        pts = [_parse_ym_lvl(dc) for dc in stages_dc]
        xs = [p[0] for p in pts]
        ys = [7 - p[1] for p in pts]  # L6 at bottom (y=1) up to L1 at top (y=6)

        ax_l.set_facecolor("#FFFFFF")
        ax_l.plot(xs, ys, color=main_col, linewidth=3.0, marker="o", markersize=9, zorder=4)
        for s_i, (xv, yv, dc) in enumerate(zip(xs, ys, stages_dc), start=1):
            ax_l.annotate(f"S{s_i}: {dc.split('|')[0].strip()}", (xv, yv), textcoords="offset points",
                          xytext=(4, 6 if s_i < 4 else -12), fontsize=7.8, fontweight="bold", color=main_col)
        ax_l.set_xlim(2017.0, 2026.5)
        ax_l.set_ylim(0.5, 6.6)
        ax_l.set_yticks([1, 2, 3, 4, 5, 6])
        ax_l.set_yticklabels(["L6 (TRL 1–2)", "L5 (TRL 4)", "L4 (TRL 5–6)", "L3 (TRL 7)", "L2 (TRL 8)", "L1 (TRL 9)"],
                             fontsize=8.0, fontweight="bold")
        ax_l.set_xlabel("Calendar Year (2017–2026)", fontsize=8.8, fontweight="bold")
        ax_l.set_title("L6 Paper → L1 Consumer Escalator", fontsize=9.5, fontweight="bold")
        ax_l.grid(True, linestyle="--", alpha=0.35)

        # Right Panel: 4-Column SAE Maturation Strip
        ax_r.set_xlim(0.0, 4.0)
        ax_r.set_ylim(0.0, 4.2)
        ax_r.axis("off")

        stage_specs = [
            (0, "STAGE 1: TRL 1–3 GENESIS\nL6 (~10,000h | PhD Paper)", "#555555", row["s1_date_cell"], row["s1_artifact"], row["s1_human_action"], row["s1_unlock"]),
            (1, "STAGE 2: TRL 4–6 PROTOTYPE\nL4–L5 (~600–2,000h | GPU/Cluster)", "#0072B2", row["s2_date_cell"], row["s2_artifact"], row["s2_human_action"], row["s2_unlock"]),
            (2, "STAGE 3: TRL 7–8 WORKFLOW\nL2–L3 (<50–200h | Prompt/API)", "#D55E00", row["s3_date_cell"], row["s3_artifact"], row["s3_human_action"], row["s3_unlock"]),
            (3, "STAGE 4: TRL 9 DEFAULT\nL1 (0h | $0 Built-In UI)", "#009E73", row["s4_date_cell"], row["s4_artifact"], row["s4_human_action"], row["s4_unlock"]),
        ]
        for c_i, stitle, scol, sdc, sart, sact, sunl in stage_specs:
            x0 = c_i + 0.03
            w = 0.94
            cx = x0 + 0.5 * w
            card = mpatches.FancyBboxPatch((x0, 0.05), w, 4.08, boxstyle="round,pad=0.02", facecolor="white", edgecolor=scol, linewidth=1.6)
            ax_r.add_patch(card)
            hdr = mpatches.FancyBboxPatch((x0, 3.30), w, 0.83, boxstyle="round,pad=0.01", facecolor=scol, edgecolor="none")
            ax_r.add_patch(hdr)
            ax_r.text(cx, 3.72, stitle, ha="center", va="center", fontsize=8.5, fontweight="bold", color="white", linespacing=1.08)

            sub_boxes = [
                (2.92, "DATE & COORDINATE", sdc, "#F4F6F8"),
                (2.14, "LANDMARK PAPER / PRODUCT", sart, "#FFFFFF"),
                (1.22, "WHAT HUMAN USER HAD TO DO", sact, "#F4F6F8"),
                (0.32, "PACKAGING UNLOCK → NEXT STAGE", sunl, "#EAF6F1"),
            ]
            for by, blbl, bval, bbg in sub_boxes:
                bh = 0.72 if by < 2.5 else 0.58
                ax_r.add_patch(mpatches.Rectangle((x0 + 0.02, by - 0.22), w - 0.04, bh, facecolor=bbg, edgecolor="#DDDDDD", linewidth=0.6))
                ax_r.text(cx, by + bh - 0.34, blbl, ha="center", va="center", fontsize=6.8, fontweight="bold", color=scol)
                ax_r.text(cx, by + 0.04, textwrap.fill(str(bval), width=28), ha="center", va="center", fontsize=7.6, fontweight="bold", color="#151515", linespacing=1.06)

        out_path = os.path.join(fig_dir, fname)
        fig.savefig(out_path, dpi=300)
        plt.close(fig)
        print(f"[RENDERED] {out_path}")
    plt.rcParams["text.parse_math"] = old_pm



def render_all_micro_cards(dfs: dict[str, pd.DataFrame], fig_dir: str):
    """Render all 20 Micro Cards into fig_dir."""
    render_plot0_micro_sae_card(dfs, fig_dir)
    render_plot0b_micro_news_card(dfs, fig_dir)
    render_per_gen_sae_cards(dfs, fig_dir)
    render_per_trl_micro_cards(dfs, fig_dir)