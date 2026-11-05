# -*- coding: utf-8 -*-
"""
stages_v5/plot_megacharts.py
============================
Renders the 4 Dual-Megachart Posters & Mini-Megacharts for v5:
  1. `fig_v5_p0_mini_megachart.png` (Plot 0-Mini: 6x6 User-Skill Mini Megachart)
  2. `fig_v5_p0_encyclopedic_megachart_poster.png` (Plot 0: 6x6 Encyclopedic User-Skill Megachart Poster)
  3. `fig_v5_p0b_mini_news_megachart.png` (Plot 0B-Mini: Historical News, Product Lines & TRL Mini Megachart)
  4. `fig_v5_p0b_historical_news_megachart_poster.png` (Plot 0B: Historical News, Product Lines & TRL Megachart Poster)
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
import matplotlib.lines as mlines
from matplotlib.path import Path

from stages_v5.news_lines_metadata import HORIZONTAL_LINES_SPEC

plt.rcParams["text.parse_math"] = False

C_SUPPLY = "#0072B2"
C_DEMAND = "#D55E00"
C_ACTUAL = "#009E73"
C_HOPE   = "#CC79A7"
C_GRAY   = "#666666"


def draw_bezier_ribbon(ax, x0, y0, x1, y1, color, alpha=0.45, lw=6.0, zorder=3):
    xm = 0.5 * (x0 + x1)
    verts = [(x0, y0), (xm, y0), (xm, y1), (x1, y1)]
    codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    path = Path(verts, codes)
    patch = mpatches.PathPatch(path, facecolor="none", edgecolor=color, lw=lw, alpha=alpha, zorder=zorder)
    ax.add_patch(patch)


def _wrap_to_exact_2_lines(ax, renderer, text_str, x_anchor, y_anchor, max_w_px, fs, weight="normal", style="normal"):
    words = str(text_str).replace("\n", " ").split()
    if len(words) < 2:
        return str(text_str)

    def line_w(s):
        p = ax.text(x_anchor, y_anchor, s, fontsize=fs, fontweight=weight, style=style, alpha=0.0)
        w = p.get_window_extent(renderer=renderer).width
        p.remove()
        return w

    best_cand = f"{words[0]}\n{' '.join(words[1:])}"
    best_score = 1e12
    for i in range(1, len(words)):
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


def _wrap_to_n_lines_balanced(ax, renderer, text_str, n_lines, fs, weight="normal", style="normal"):
    words = str(text_str).replace("\n", " ").split()
    p = ax.text(0, 0, "", fontsize=fs, fontweight=weight, style=style, alpha=0.0)
    p.set_text(" ".join(words))
    tot_w = p.get_window_extent(renderer=renderer).width
    low_w = tot_w / (n_lines + 0.8)
    high_w = tot_w
    best_lines = [" ".join(words)]
    for _ in range(18):
        mid_w = 0.5 * (low_w + high_w)
        lines, cur = [], []
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


def _wrap_by_pixel_width(ax, renderer, text_str, fs, max_w_px, weight="normal", style="normal"):
    words = str(text_str).replace("\n", " ").split()
    p = ax.text(0, 0, "", fontsize=fs, fontweight=weight, style=style, alpha=0.0)
    lines, cur = [], []
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


def render_plot0_mini_megachart(dfs: dict[str, pd.DataFrame], fig_dir: str):
    """Render Plot 0-Mini (`fig_v5_p0_mini_megachart.png`, figsize=(22, 16.5), dpi=200)."""
    df_cells = pd.concat([dfs["ladder_cells"], dfs["gen5_speculative"]], ignore_index=True)
    df_poster = dfs["poster_encyclopedic_cells"]

    xm_min, xm_max = -0.50, 5.50
    tb_min, tb_max = 2017.42, 2028.00

    fig = plt.figure(figsize=(22, 16.5), dpi=200, facecolor="#FBFBF9")
    gs = gridspec.GridSpec(
        3, 2, figure=fig,
        width_ratios=[5.85, 1.15],
        height_ratios=[5.06, 0.16, 1.45],
        left=0.128, right=0.986, bottom=0.048, top=0.915,
        wspace=0.018, hspace=0.0
    )
    ax_main   = fig.add_subplot(gs[0, 0])
    ax_right  = fig.add_subplot(gs[0, 1], sharey=ax_main)
    ax_trap   = fig.add_subplot(gs[1, 0])
    ax_bot    = fig.add_subplot(gs[2, 0])
    ax_corner = fig.add_subplot(gs[2, 1])

    fig.text(0.128, 0.958, "AI Ladder Evolution", ha="left", va="center", fontsize=34.0, fontweight="bold", color="#111111")
    subtitle_3lines = (
        "This chart maps the evolution of AI as a six-level ladder from the user's perspective, ranking how people use AI from passive everyday\n"
        "tools (Level 1) to foundational research scientists (Level 6). Because AI technology moves so fast, any static ladder definition gets obsolete\n"
        "very quickly, which is why we must track how the entire ladder evolves across generations rather than relying on a single fixed ladder."
    )
    fig.text(0.386, 0.958, subtitle_3lines, ha="left", va="center", fontsize=9.5, style="italic", color="#3B3B3B", linespacing=1.18)

    ax_main.set_facecolor("#FBFBF9")
    ax_main.set_xlim(xm_min, xm_max)
    ax_main.set_ylim(0.46, 7.36)

    gen_expl_map = {
        "G0": "Task-specific neural NLP (BERT, spaCy) & XGBoost on labeled CSVs; users meet AI passively via search rankers & Smart Compose.",
        "G1": "Few-shot pretraining (GPT-3, Chinchilla) unlocks API playgrounds, diffusion art (DALL-E 2, Midjourney) & Copilot ghost-text.",
        "G2": "RLHF & ChatGPT make conversational bots universal alongside GPT-4, open-weight LLaMA/QLoRA tuning & LangChain Vector RAG.",
        "G3": "Omni-modal chat (GPT-4o, Claude 3.5), live UI sandboxes (Artifacts, v0) & Cursor multi-file IDEs birth natural-language 'Vibe Coding'.",
        "G4": "RLVR test-time reasoners (o1/o3, DeepSeek-R1) & terminal CLI agents (Claude Code, MCP) run multi-hour loops amid 'AI Slop'.",
        "G5": "Named forecasts: Altman/Ive & Nadella (ambient OS), Amodei (>90% AI code & circuit MRI), LeCun/Fei-Fei Li (3D worlds) & Hassabis (AGI).",
    }

    gen_header_specs = [
        ("G0", -0.50, 0.50, 2017.42, 2020.42, "GEN 0\nPre-LLM &\nPassive NLP",              "#EFEFEF", "#555555", 13.5),
        ("G1",  0.50, 1.50, 2020.42, 2022.83, "GEN 1\nPlaygrounds &\nAutocomplete",         "#EBF3FA", "#0072B2", 13.5),
        ("G2",  1.50, 2.50, 2022.83, 2024.33, "GEN 2\nChatbots &\nVector RAG",              "#FDF2E9", "#D55E00", 13.5),
        ("G3",  2.50, 3.50, 2024.33, 2025.00, "GEN 3\nOmni-Modal &\nVibe Coding",           "#E8F6F3", "#009E73", 13.5),
        ("G4",  3.50, 4.50, 2025.00, 2026.803,"GEN 4\nReasoners &\nCLI Agents",             "#F9EFF5", "#CC79A7", 13.5),
        ("G5",  4.50, 5.50, 2026.803,2028.00, "GEN 5 (Forecasts)\nAmbient OS &\nWorld Sim", "#F8ECF5", "#7A2862", 13.5),
    ]
    gen_spans = {gid: (xm0, xm1) for gid, xm0, xm1, *_ in gen_header_specs}

    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()

    UNIFORM_DESC_FS_MINI = 5.8
    for gid, xm0, xm1, tb0, tb1, gtitle, bg_c, hdr_c, hdr_fs in gen_header_specs:
        w_col = xm1 - xm0
        pad_x = 0.036
        ax_main.axvspan(xm0, xm1, color=bg_c, alpha=0.34, zorder=0)
        ax_main.axvline(xm0, color="#444444", linestyle="-" if gid != "G5" else "--", linewidth=1.4, alpha=0.75, zorder=2)
        hdr_box = mpatches.FancyBboxPatch((xm0 + pad_x, 6.84), w_col - 2 * pad_x, 0.46, boxstyle="round,pad=0.008",
                                          facecolor=hdr_c, edgecolor="#111111", linewidth=1.3, zorder=6)
        ax_main.add_patch(hdr_box)
        glines = gtitle.splitlines()
        for idx_g, gline in enumerate(glines):
            yg_line = 7.070 + (0.5 * (len(glines) - 1) - idx_g) * 0.138
            ax_main.text(0.5 * (xm0 + xm1), yg_line, gline, ha="center", va="center", fontsize=hdr_fs,
                         fontweight="bold" if idx_g == 0 else "normal", color="white", zorder=7)

        expl_box = mpatches.FancyBboxPatch((xm0 + pad_x, 6.53), w_col - 2 * pad_x, 0.28, boxstyle="round,pad=0.006",
                                           facecolor="#FFFFFF", edgecolor=hdr_c, linewidth=1.2, alpha=0.97, zorder=6)
        ax_main.add_patch(expl_box)
        wrapped_gexpl = _wrap_to_n_lines_balanced(ax_main, renderer, gen_expl_map[gid], 3, UNIFORM_DESC_FS_MINI, weight="normal")
        ax_main.text(0.5 * (xm0 + xm1), 6.67, wrapped_gexpl, ha="center", va="center", fontsize=UNIFORM_DESC_FS_MINI, color="#1B2631", linespacing=1.06, zorder=7)

    for y_div in [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]:
        ax_main.axhline(y_div, color="#888888", linestyle=":" if y_div < 6.0 else "-", linewidth=(0.9 if y_div < 6.0 else 1.2), alpha=0.55, zorder=1)
        ax_right.axhline(y_div, color="#888888", linestyle=":" if y_div < 6.0 else "-", linewidth=(0.9 if y_div < 6.0 else 1.2), alpha=0.55, zorder=1)

    for _, prow in df_poster.iterrows():
        gid = prow["gen_id"]
        lvl = int(prow["level_id"])
        m_title = prow["cell_name"]
        m_desc = prow["plain_desc"]
        m_keywords = prow["mini_keywords_subset"]

        y_lvl  = 7 - lvl
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

        card = mpatches.FancyBboxPatch((x_left, y_bot), w_box, h_box, boxstyle="round,pad=0.010",
                                       facecolor=box_fill, edgecolor=edge_c,
                                       linewidth=1.5 if gid != "G5" else 1.8,
                                       linestyle="--" if gid == "G5" else "-", zorder=4)
        ax_main.add_patch(card)

        hdr_y0 = y_lvl + 0.085
        hdr_h  = 0.370
        hdr_cy = hdr_y0 + 0.5 * hdr_h
        desc_y_top = y_lvl + 0.055

        hdr_strip = mpatches.FancyBboxPatch((x_left, hdr_y0), w_box, hdr_h, boxstyle="round,pad=0.005",
                                            facecolor=hdr_fill, edgecolor="none", zorder=5)
        ax_main.add_patch(hdr_strip)

        cur_tfs, cur_dfs, cur_kfs = (12.0, 6.0, 5.75)
        in_pad = 0.022
        x_txt_l = x_left + in_pad
        x_txt_r = x_left + w_box - in_pad
        max_w_px = ax_main.transData.transform((x_txt_r, y_lvl))[0] - ax_main.transData.transform((x_txt_l, y_lvl))[0]

        wrapped_title = _wrap_to_exact_2_lines(ax_main, renderer, m_title, 0.5 * (x0 + x1), hdr_cy, max_w_px, cur_tfs, weight="bold")
        ax_main.text(0.5 * (x0 + x1), hdr_cy, wrapped_title, ha="center", va="center", fontsize=cur_tfs, fontweight="bold", color="white", linespacing=1.05, zorder=6)

        div_gap = 0.032
        wrapped_desc = _wrap_to_exact_2_lines(ax_main, renderer, m_desc, x_txt_l, desc_y_top, max_w_px, cur_dfs, weight="normal")
        p_desc = ax_main.text(x_txt_l, desc_y_top, wrapped_desc, ha="left", va="top", fontsize=cur_dfs, fontweight="normal", linespacing=1.14, alpha=0.0)
        bb_d = p_desc.get_window_extent(renderer=renderer)
        p_desc.remove()
        y_d_bot = ax_main.transData.inverted().transform((0, bb_d.y0))[1]
        y_div_cell = y_d_bot - div_gap

        wrapped_kw = _wrap_to_exact_2_lines(ax_main, renderer, m_keywords, x_txt_l, y_div_cell - div_gap, max_w_px, cur_kfs, style="italic")
        p_kw = ax_main.text(x_txt_l, y_div_cell - div_gap, wrapped_kw, ha="left", va="top", fontsize=cur_kfs, style="italic", linespacing=1.12, alpha=0.0)
        bb_k = p_kw.get_window_extent(renderer=renderer)
        p_kw.remove()

        y_kw_bot = ax_main.transData.inverted().transform((0, bb_k.y0))[1]
        spare_h = max(0.0, (y_kw_bot - (y_bot + 0.020)))
        y_shift = 0.45 * spare_h
        desc_y_top_adj = desc_y_top - y_shift
        y_div_cell_adj = y_div_cell - y_shift

        ax_main.text(x_txt_l, desc_y_top_adj, wrapped_desc, ha="left", va="top", fontsize=cur_dfs, color="#111111", linespacing=1.14, zorder=6)
        ax_main.plot([x_txt_l, x_txt_r], [y_div_cell_adj, y_div_cell_adj], color=edge_c, linestyle=":", linewidth=1.0, alpha=0.65, zorder=5)
        ax_main.text(x_txt_l, y_div_cell_adj - div_gap, wrapped_kw, ha="left", va="top", fontsize=cur_kfs, color="#3B3B3B", style="italic", linespacing=1.12, zorder=6)

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
    for y_pos, y_lbl in y_labels_6:
        ylines = y_lbl.splitlines()
        for idx_y, yline in enumerate(ylines):
            yy_line = y_pos + (0.5 * (len(ylines) - 1) - idx_y) * 0.195
            ax_main.text(xm_min - 0.055, yy_line, yline, ha="right", va="center", fontsize=15.0,
                         fontweight="bold" if idx_y == 0 else "normal", color="#111111", clip_on=False, zorder=7)
    ax_main.set_xticks([])

    # Short & Empty Trapezium Bridge
    ax_trap.set_facecolor("#F4F3EF")
    ax_trap.set_xlim(0.0, 1.0)
    ax_trap.set_ylim(0.0, 1.0)
    ax_trap.set_xticks([])
    ax_trap.set_yticks([])
    u_top = lambda xm: (xm - xm_min) / (xm_max - xm_min)
    u_bot = lambda tb: (tb - tb_min) / (tb_max - tb_min)

    for gid, xm0, xm1, tb0, tb1, _, bg_c, hdr_c, _ in gen_header_specs:
        ut0, ut1 = u_top(xm0), u_top(xm1)
        ub0, ub1 = u_bot(tb0), u_bot(tb1)
        verts = [(ut0, 1.0), (ut1, 1.0), (ub1, 0.0), (ub0, 0.0)]
        ax_trap.add_patch(mpatches.Polygon(verts, closed=True, facecolor=bg_c, edgecolor="none", alpha=0.85, zorder=1))
        ax_trap.add_patch(mpatches.Polygon(verts, closed=True, facecolor=hdr_c, edgecolor="none", alpha=0.22, zorder=2))
        ax_trap.plot([ut0, ub0], [1.0, 0.0], color="#333333", linestyle="-" if gid != "G5" else "--", linewidth=1.5, zorder=4)
        ax_trap.plot([ut1, ub1], [1.0, 0.0], color="#333333", linestyle="-", linewidth=1.2, alpha=0.6, zorder=4)

    tb_pre_cut, tb_today, tb_post_cut = 2026.62, 2026.803, 2027.17
    ax_trap.plot([u_top(4.50), u_bot(tb_pre_cut)], [1.0, 0.0], color=C_HOPE, linestyle=":", linewidth=1.6, zorder=5)
    ax_trap.plot([u_top(4.50), u_bot(tb_post_cut)], [1.0, 0.0], color=C_HOPE, linestyle="--", linewidth=2.0, zorder=5)
    ax_trap.plot([u_top(4.50), u_bot(tb_today)], [1.0, 0.0], color="#C00000", linestyle="-", linewidth=3.0, zorder=8)

    # Top-Right Marginal Histogram
    ax_right.set_facecolor("#FBFBF9")
    gen_line_styles = [("G0", "#555555", "o"), ("G1", "#0072B2", "s"), ("G2", "#D55E00", "^"), ("G3", "#009E73", "D"), ("G4", "#CC79A7", "P")]
    y_lvls = np.array([6.0, 5.0, 4.0, 3.0, 2.0, 1.0])
    y_step_pts = np.array([6.5, 6.5, 5.5, 5.5, 4.5, 4.5, 3.5, 3.5, 2.5, 2.5, 1.5, 1.5, 0.5, 0.5])
    u_handles, t_handles = [], []
    for gid, gcol, gmk in gen_line_styles:
        sub_g = df_cells[df_cells["gen_id"] == gid].sort_values("level_id")
        u_rel = sub_g["user_share_pct"].values / 100.0
        t_rel = sub_g["token_share_pct"].values / 100.0
        u_step_pts = np.concatenate([[0.0], np.repeat(u_rel, 2), [0.0]])
        t_step_pts = np.concatenate([[0.0], np.repeat(t_rel, 2), [0.0]])
        h_u, = ax_right.plot(u_step_pts, y_step_pts, color=gcol, linestyle="-", linewidth=2.2, alpha=0.75, zorder=4, label=f"{gid} Users")
        ax_right.scatter(u_rel, y_lvls, color=gcol, marker=gmk, s=38, alpha=0.85, zorder=5)
        h_t, = ax_right.plot(t_step_pts, y_step_pts, color=gcol, linestyle="--", linewidth=2.0, alpha=0.70, zorder=3, label=f"{gid} Tokens")
        ax_right.scatter(t_rel, y_lvls, facecolors="none", edgecolors=gcol, marker=gmk, s=38, linewidth=1.3, alpha=0.85, zorder=5)
        u_handles.append(h_u)
        t_handles.append(h_t)

    ax_right.set_xlim(0.0, 0.78)
    ax_right.set_xticks([0.0, 0.25, 0.50, 0.75])
    ax_right.set_xticklabels(["0.00", "0.25", "0.50", "0.75"], fontsize=9.5, fontweight="bold")
    ax_right.tick_params(axis="x", pad=1)
    ax_right.set_xlabel("")
    ax_right.set_title("Users & Tokens Distribution (Rel. Freq.)", fontsize=10.5, fontweight="bold", pad=6)
    ax_right.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.28, color="#888888")
    ax_right.legend(handles=u_handles + t_handles, loc="upper center", bbox_to_anchor=(0.50, 0.998),
                    ncol=2, frameon=True, facecolor="white", framealpha=0.96,
                    fontsize=12.5, columnspacing=0.55, handlelength=1.25, handletextpad=0.38, labelspacing=0.14, borderpad=0.20)
    plt.setp(ax_right.get_yticklabels(), visible=False)

    # Bottom Timeline
    ax_bot.set_facecolor("#FBFBF9")
    ax_bot.set_xlim(tb_min, tb_max)
    t_curve_emp = np.array([2017.42, 2018.0, 2018.8, 2019.5, 2020.42, 2021.0, 2021.8, 2022.5, 2022.83, 2023.3, 2023.8, 2024.33, 2024.6, 2025.00, 2025.5, 2026.0, 2026.62, 2026.803])
    users_emp   = np.array([2.5, 4.5, 8.0, 11.0, 15.0, 24.0, 34.0, 42.0, 65.0, 210.0, 320.0, 480.0, 640.0, 780.0, 920.0, 1040.0, 1120.0, 1150.0]) * 1e6
    money_emp   = np.array([1.8, 2.8, 4.2, 6.5, 11.0, 18.0, 28.0, 38.0, 48.0, 95.0, 145.0, 210.0, 265.0, 340.0, 430.0, 520.0, 610.0, 650.0]) * 1e9
    tokens_emp  = np.array([0.04, 0.07, 0.12, 0.16, 0.25, 0.55, 1.10, 1.45, 2.20, 12.0, 22.0, 45.0, 140.0, 280.0, 520.0, 780.0, 1010.0, 1100.0]) * 1e12
    t_curve_spec = np.array([2026.803, 2027.17, 2027.45, 2027.72, 2028.00])
    users_spec   = np.array([1150.0, 1260.0, 1420.0, 1560.0, 1650.0]) * 1e6
    money_spec   = np.array([650.0, 820.0, 1050.0, 1300.0, 1550.0]) * 1e9
    tokens_spec  = np.array([1100.0, 1550.0, 2600.0, 3700.0, 4800.0]) * 1e12

    ax_bot.fill_between(t_curve_emp, 1e6, users_emp, step="mid", color=C_DEMAND, alpha=0.10, zorder=1)
    ax_bot.fill_between(t_curve_emp, 1e6, money_emp, step="mid", color=C_ACTUAL, alpha=0.09, zorder=1)
    ax_bot.fill_between(t_curve_emp, 1e6, tokens_emp, step="mid", color=C_SUPPLY, alpha=0.09, zorder=1)
    ax_bot.plot(t_curve_emp, users_emp, color=C_DEMAND, linewidth=2.6, marker="o", markersize=4.5, zorder=4, label="Global Active AI Users")
    ax_bot.plot(t_curve_emp, money_emp, color=C_ACTUAL, linewidth=2.6, marker="D", markersize=4.5, zorder=4, label="Global AI Money: Spend & Capex ($)")
    ax_bot.plot(t_curve_emp, tokens_emp, color=C_SUPPLY, linewidth=2.6, marker="s", markersize=4.5, zorder=4, label="Global Annualized Tokens")
    ax_bot.plot(t_curve_spec, users_spec, color=C_DEMAND, linestyle="--", linewidth=2.6, marker="o", markersize=4.5, zorder=4)
    ax_bot.plot(t_curve_spec, money_spec, color=C_ACTUAL, linestyle="--", linewidth=2.6, marker="D", markersize=4.5, zorder=4)
    ax_bot.plot(t_curve_spec, tokens_spec, color=C_SUPPLY, linestyle="--", linewidth=2.6, marker="s", markersize=4.5, zorder=4)

    for gid, _, _, tb0, tb1, _, bg_c, _, _ in gen_header_specs:
        ax_bot.axvspan(tb0, tb1, color=bg_c, alpha=0.25, zorder=0)
        ax_bot.axvline(tb0, color="#444444", linestyle="-" if gid != "G5" else "--", linewidth=1.2, alpha=0.75, zorder=2)

    ax_bot.axvspan(tb_pre_cut, tb_post_cut, color="#FFD700", alpha=0.18, zorder=1)
    ax_bot.axvline(tb_pre_cut, color=C_HOPE, linestyle=":", linewidth=1.6, zorder=8)
    ax_bot.axvline(tb_today, color="#C00000", linestyle="-", linewidth=3.0, zorder=12)
    ax_bot.axvline(tb_post_cut, color=C_HOPE, linestyle="--", linewidth=2.0, zorder=8)
    ax_bot.text(tb_today, 4.0e12, "◀ TODAY ▶", ha="center", va="center", fontsize=10.5, fontweight="bold", color="white",
                bbox=dict(boxstyle="round,pad=0.14", facecolor="#C00000", edgecolor="#111111", linewidth=1.0), zorder=15)

    mini_events = [
        (2017.46, "2017-06:\nTransformer Paper", 4.5e7, "left", "#005A9C", "#EAF3FB", "#003B66"),
        (2021.48, "2021-06: GitHub\nCopilot Preview", 2.2e9, "center", "#007958", "#E8F7F2", "#004430"),
        (2022.91, "2022-11: ChatGPT\n(100M in 60d)", 2.2e6, "center", "#B83B00", "#FFF0E5", "#5E1D00"),
        (2024.49, "2024-06: Claude 3.5\nSonnet & Artifacts", 1.8e11, "center", "#007958", "#E8F7F2", "#004430"),
        (2025.08, "2025-01: DeepSeek-R1\nOpen Reasoner", 6.5e6, "left", "#007958", "#E8F7F2", "#004430"),
    ]
    for yr_f, ev_txt, ey, ha_e, edge_ev, bg_ev, txt_ev in mini_events:
        ax_bot.vlines(yr_f, 1e6, ey, color=edge_ev, linestyle=":", linewidth=1.4, alpha=0.80, zorder=5)
        ax_bot.scatter([yr_f], [ey], color=edge_ev, s=42, zorder=7)
        ax_bot.text(yr_f, ey * 1.35, ev_txt, ha=ha_e, va="bottom", fontsize=11.0, fontweight="bold", color=txt_ev, linespacing=1.08,
                    bbox=dict(boxstyle="round,pad=0.14", facecolor=bg_ev, edgecolor=edge_ev, linewidth=1.2, alpha=0.96), zorder=8)

    year_ticks = list(range(2018, 2029))
    ax_bot.set_xticks(year_ticks)
    ax_bot.set_xticklabels([f"{yr}" for yr in year_ticks], fontsize=11.0, fontweight="bold")
    ax_bot.set_yscale("log")
    ax_bot.set_ylim(1e6, 2.5e16)
    ax_bot.set_yticks([1e6, 1e8, 1e10, 1e12, 1e14, 1e16])
    ax_bot.set_yticklabels([r"$10^{6}$", r"$10^{8}$", r"$10^{10}$", r"$10^{12}$", r"$10^{14}$", r"$10^{16}$"], parse_math=True)
    ax_bot.tick_params(axis="y", labelsize=9.5)
    ax_bot.set_xlabel("")
    ax_bot.set_ylabel("")
    ax_bot.grid(True, which="major", linestyle="-", linewidth=0.8, alpha=0.25, color="#888888")
    ax_bot.legend(loc="upper left", bbox_to_anchor=(0.004, 0.988), ncol=3, frameon=True, facecolor="white", framealpha=0.95, fontsize=8.4)

    # Bottom-Right Colophon
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
    ax_corner.text(0.50, 0.825, "www.arianprabowo.com", ha="center", va="center", fontsize=11.5, fontweight="bold", color="#F0E442", zorder=2)
    mini_colophon = (
        "• Green Box: Direct User (L1–2)\n"
        "• Blue Box: Builder / Eng (L3–6)\n"
        "• Gray Box: Passive Baseline\n"
        "• Purple Box: Speculative Gen 5\n"
        "• Today Line: 2026-10-20\n"
        "• Pre-Cut: 2026-08 (>50%)\n"
        "• Post-Cut: 2027-03 (Mass)"
    )
    ax_corner.text(0.04, 0.73, mini_colophon, ha="left", va="top", fontsize=11.0, fontweight="bold", color="#111111", linespacing=1.20, zorder=3)

    out_path = os.path.join(fig_dir, "fig_v5_p0_mini_megachart.png")
    fig.savefig(out_path, dpi=200)
    plt.close(fig)
    print(f"[RENDERED] {out_path}")


def render_plot0_encyclopedic_megachart_poster(dfs: dict[str, pd.DataFrame], fig_dir: str):
    """Render Plot 0 (`fig_v5_p0_encyclopedic_megachart_poster.png`, figsize=(44, 33), dpi=300)."""
    df_cells = pd.concat([dfs["ladder_cells"], dfs["gen5_speculative"]], ignore_index=True)
    df_poster = dfs["poster_encyclopedic_cells"]
    df_events = dfs["defining_events"]

    xm_min, xm_max = -0.50, 5.50
    tb_min, tb_max = 2017.42, 2028.00

    fig = plt.figure(figsize=(44, 33), dpi=300, facecolor="#FBFBF9")
    gs = gridspec.GridSpec(
        3, 2, figure=fig,
        width_ratios=[5.85, 1.15],
        height_ratios=[5.06, 0.16, 1.45],
        left=0.082, right=0.986, bottom=0.048, top=0.915,
        wspace=0.018, hspace=0.0
    )
    ax_main   = fig.add_subplot(gs[0, 0])
    ax_right  = fig.add_subplot(gs[0, 1], sharey=ax_main)
    ax_trap   = fig.add_subplot(gs[1, 0])
    ax_bot    = fig.add_subplot(gs[2, 0])
    ax_corner = fig.add_subplot(gs[2, 1])

    fig.text(0.082, 0.958, "AI Ladder Evolution", ha="left", va="center", fontsize=68.0, fontweight="bold", color="#111111")
    subtitle_3lines = (
        "This chart maps the evolution of AI as a six-level ladder from the user's perspective, ranking how people use AI from passive everyday\n"
        "tools (Level 1) to foundational research scientists (Level 6). Because AI technology moves so fast, any static ladder definition gets obsolete\n"
        "very quickly, which is why we must track how the entire ladder evolves across generations rather than relying on a single fixed ladder."
    )
    fig.text(0.340, 0.958, subtitle_3lines, ha="left", va="center", fontsize=19.0, style="italic", color="#3B3B3B", linespacing=1.18)

    ax_main.set_facecolor("#FBFBF9")
    ax_main.set_xlim(xm_min, xm_max)
    ax_main.set_ylim(0.46, 7.46)

    gen_expl_map_poster = {
        "G0": "Task-specific neural NLP (BERT, spaCy) & XGBoost trained on labeled CSVs; users only meet AI passively via search rankers & Smart Compose.",
        "G1": "Few-shot pretraining (GPT-3, Chinchilla) unlocks API playgrounds, diffusion art (DALL-E 2, Midjourney) & Copilot IDE ghost-text.",
        "G2": "RLHF & ChatGPT make conversational bots universal alongside GPT-4, open-weight LLaMA/QLoRA fine-tuning & LangChain Vector RAG.",
        "G3": "Omni-modal chat (GPT-4o, Claude 3.5), live UI sandboxes (Artifacts, v0) & Cursor multi-file IDEs birth natural-language 'Vibe Coding'.",
        "G4": "RLVR test-time reasoners (o1/o3, DeepSeek-R1) & terminal CLI agents (Claude Code, MCP) run multi-hour loops amid 'AI Slop' & GW capex.",
        "G5": "Named forecasts: Altman/Ive & Nadella (ambient OS), Amodei (>90% AI code & circuit MRI), LeCun/Fei-Fei Li (3D worlds) & Hassabis (2028 AGI).",
    }

    gen_header_specs = [
        ("G0", -0.50, 0.50, 2017.42, 2020.42, "GEN 0\nPre-LLM &\nPassive NLP",              "#EFEFEF", "#555555"),
        ("G1",  0.50, 1.50, 2020.42, 2022.83, "GEN 1\nPlaygrounds &\nAutocomplete",         "#EBF3FA", "#0072B2"),
        ("G2",  1.50, 2.50, 2022.83, 2024.33, "GEN 2\nChatbots &\nVector RAG",              "#FDF2E9", "#D55E00"),
        ("G3",  2.50, 3.50, 2024.33, 2025.00, "GEN 3\nOmni-Modal &\nVibe Coding",           "#E8F6F3", "#009E73"),
        ("G4",  3.50, 4.50, 2025.00, 2026.803, "GEN 4\nReasoners &\nCLI Agents",            "#F9EFF5", "#CC79A7"),
        ("G5",  4.50, 5.50, 2026.803, 2028.00, "GEN 5 (Forecasts)\nAmbient OS &\nWorld Sim", "#F8ECF5", "#7A2862"),
    ]
    gen_spans = {gid: (xm0, xm1) for gid, xm0, xm1, *_ in gen_header_specs}

    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()

    UNIFORM_DESC_FS_POSTER = 10.6
    for gid, xm0, xm1, tb0, tb1, gtitle, bg_c, hdr_c in gen_header_specs:
        w_col = xm1 - xm0
        pad_x = 0.032
        ax_main.axvspan(xm0, xm1, color=bg_c, alpha=0.34, zorder=0)
        ax_main.axvline(xm0, color="#444444", linestyle="-" if gid != "G5" else "--", linewidth=2.4, alpha=0.75, zorder=2)
        hdr_box = mpatches.FancyBboxPatch((xm0 + pad_x, 6.88), w_col - 2 * pad_x, 0.52, boxstyle="round,pad=0.008",
                                          facecolor=hdr_c, edgecolor="#111111", linewidth=2.2, zorder=6)
        ax_main.add_patch(hdr_box)
        glines = gtitle.splitlines()
        ax_main.text(0.5 * (xm0 + xm1), 7.29, glines[0], ha="center", va="center", fontsize=26.0, fontweight="bold", color="white", zorder=7)
        ax_main.text(0.5 * (xm0 + xm1), 7.14, glines[1], ha="center", va="center", fontsize=26.0, fontweight="normal", color="white", zorder=7)
        ax_main.text(0.5 * (xm0 + xm1), 6.99, glines[2], ha="center", va="center", fontsize=26.0, fontweight="normal", color="white", zorder=7)

        expl_box = mpatches.FancyBboxPatch((xm0 + pad_x, 6.54), w_col - 2 * pad_x, 0.31, boxstyle="round,pad=0.006",
                                           facecolor="#FFFFFF", edgecolor=hdr_c, linewidth=2.0, alpha=0.97, zorder=6)
        ax_main.add_patch(expl_box)
        wrapped_gexpl = _wrap_to_n_lines_balanced(ax_main, renderer, gen_expl_map_poster[gid], 3, UNIFORM_DESC_FS_POSTER, weight="normal")
        ax_main.text(0.5 * (xm0 + xm1), 6.695, wrapped_gexpl, ha="center", va="center", fontsize=UNIFORM_DESC_FS_POSTER, color="#1B2631", linespacing=1.08, zorder=7)

    x_pre_cutoff, x_today, x_post_cut = 4.468, 4.500, 4.532
    ax_main.axvspan(x_pre_cutoff, x_post_cut, color="#FFD700", alpha=0.18, zorder=1)
    ax_main.axvline(x_pre_cutoff, color=C_HOPE, linestyle=":", linewidth=2.2, zorder=8)
    ax_main.axvline(x_today, color="#C00000", linestyle="-", linewidth=3.6, zorder=12)
    ax_main.axvline(x_post_cut, color=C_HOPE, linestyle="--", linewidth=2.6, zorder=8)
    ax_main.text(x_today, 6.505, "◀ TODAY: 2026-10-20 ▶  (Pre-Cutoff: 2026-08 First-Release | Post-Cutoff: 2027-03 Mainstream Crossover)",
                 ha="center", va="center", fontsize=8.5, fontweight="bold", color="white",
                 bbox=dict(boxstyle="round,pad=0.16", facecolor="#C00000", edgecolor="#111111", linewidth=1.2), zorder=15)

    for y_div in [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]:
        ax_main.axhline(y_div, color="#888888", linestyle=":" if y_div < 6.0 else "-", linewidth=1.2 if y_div < 6.0 else 1.8, alpha=0.55, zorder=1)
        ax_right.axhline(y_div, color="#888888", linestyle=":" if y_div < 6.0 else "-", linewidth=1.2 if y_div < 6.0 else 1.8, alpha=0.55, zorder=1)

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
        draw_bezier_ribbon(ax_main, (cA - 0.50) + 0.970, 7 - lA, (cB - 0.50) + 0.030, 7 - lB, color=col_rib, alpha=0.55, lw=7.0, zorder=3)
    for cA, lA, cB, lB in expansion_links:
        col_rib = C_HOPE if cB == 5 else C_SUPPLY
        draw_bezier_ribbon(ax_main, (cA - 0.50) + 0.970, 7 - lA, (cB - 0.50) + 0.030, 7 - lB, color=col_rib, alpha=0.45, lw=5.5, zorder=3)

    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()

    for _, prow in df_poster.iterrows():
        gid = prow["gen_id"]
        lvl = int(prow["level_id"])
        m_title = prow["cell_name"]
        m_desc = prow["plain_desc"]
        m_keywords = prow["keywords_1line"]
        m_enc_body = prow["encyclopedic_body"]
        crow = df_cells[(df_cells["gen_id"] == gid) & (df_cells["level_id"] == lvl)].iloc[0]

        y_lvl  = 7 - lvl
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

        card = mpatches.FancyBboxPatch((x_left, y_bot), w_box, h_box, boxstyle="round,pad=0.008",
                                       facecolor=box_fill, edgecolor=edge_c,
                                       linewidth=2.4 if gid != "G5" else 2.8,
                                       linestyle="--" if gid == "G5" else "-", zorder=4)
        ax_main.add_patch(card)

        y_hdr_bot = y_lvl + 0.208
        hdr_strip = mpatches.FancyBboxPatch((x_left, y_hdr_bot), w_box, 0.250, boxstyle="round,pad=0.004",
                                            facecolor=hdr_fill, edgecolor="none", zorder=5)
        ax_main.add_patch(hdr_strip)

        tok_v = crow["single_task_tokens"]
        tok_str = f"{tok_v/1e6:.1f}M tok" if tok_v >= 1e6 else (f"{tok_v/1e3:.1f}k tok" if tok_v >= 1e3 else f"{int(tok_v)} tok")
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
        wrapped_title = _wrap_to_exact_2_lines(ax_main, renderer, m_title, 0.5 * (x0 + x1), hdr_cy, max_w_px, 22.0, weight="bold")
        ax_main.text(0.5 * (x0 + x1), hdr_cy, wrapped_title, ha="center", va="center", fontsize=22.0, fontweight="bold", color="white", linespacing=0.98, zorder=6)
        ax_main.text(0.5 * (x0 + x1), y_hdr_bot + 0.024, badge_str, ha="center", va="center", fontsize=5.8, fontweight="bold", color="#F0E442", zorder=6)

        y_sum_bot = y_hdr_bot - 0.126
        sum_strip = mpatches.Rectangle((x_left + 0.004, y_sum_bot), w_box - 0.008, 0.126, facecolor=sum_fill, edgecolor="none", zorder=4.5)
        ax_main.add_patch(sum_strip)
        wrapped_desc = _wrap_to_n_lines_balanced(ax_main, renderer, m_desc, 2, 10.6, weight="bold")
        ax_main.text(x_txt_l, y_sum_bot + 0.063, wrapped_desc, ha="left", va="center", fontsize=10.6, fontweight="bold", color="#111111", linespacing=1.08, zorder=6)

        y_kw_top = y_bot + 0.100
        ax_main.plot([x_left + 0.010, x_left + w_box - 0.010], [y_kw_top, y_kw_top], color=edge_c, linestyle=":", linewidth=1.2, alpha=0.75, zorder=5)
        wrapped_kw = _wrap_to_n_lines_balanced(ax_main, renderer, m_keywords, 2, 7.1, weight="bold", style="italic")
        ax_main.text(x_txt_l, y_bot + 0.050, wrapped_kw, ha="left", va="center", fontsize=7.1, color="#3B3B3B", style="italic", fontweight="bold", linespacing=1.12, zorder=6)

        subcell_titles = ["Extended Summary", "Use Cases & Landmarks", "User Actions", "Models & Products", "Surface & Hardware", "Scope & Evolution"]
        raw_lines = m_enc_body.split("\n")[:6]
        y_tbl_bot = y_kw_top + 0.004
        y_tbl_top = y_sum_bot - 0.002
        w_tbl = w_box - 0.016
        h_tbl = y_tbl_top - y_tbl_bot
        x_tbl = x_left + 0.008
        ncol_t, nrow_t = 3, 2
        cw_t, ch_t = w_tbl / ncol_t, h_tbl / nrow_t
        sh_h = 0.030
        FIXED_SUBCELL_FS = 5.75

        for idx_s, stitle in enumerate(subcell_titles):
            r_i, c_i = divmod(idx_s, ncol_t)
            sx = x_tbl + c_i * cw_t
            sy = y_tbl_top - (r_i + 1) * ch_t
            raw_s = raw_lines[idx_s] if idx_s < len(raw_lines) else ""
            sbody = raw_s.split(":", 1)[1].strip() if ":" in raw_s else raw_s.strip()

            ax_main.add_patch(mpatches.Rectangle((sx, sy), cw_t, ch_t, facecolor="#F9FBFA" if (r_i + c_i) % 2 == 0 else "#FFFFFF", edgecolor=tbl_edge, linewidth=0.9, zorder=4.6))
            ax_main.add_patch(mpatches.Rectangle((sx, sy + ch_t - sh_h), cw_t, sh_h, facecolor=tbl_hdr_fill, edgecolor="none", zorder=4.7))
            ax_main.text(sx + 0.5 * cw_t, sy + ch_t - 0.5 * sh_h, stitle, ha="center", va="center", fontsize=FIXED_SUBCELL_FS, fontweight="bold", color="#111111", zorder=6)

            sc_pad_x = 0.008
            max_sc_w_px = ax_main.transData.transform((sx + cw_t - sc_pad_x, sy))[0] - ax_main.transData.transform((sx + sc_pad_x, sy))[0]
            wrapped_b = _wrap_by_pixel_width(ax_main, renderer, sbody, FIXED_SUBCELL_FS, max_sc_w_px * 0.96)
            ax_main.text(sx + sc_pad_x, sy + 0.5 * (ch_t - sh_h), wrapped_b, ha="left", va="center", fontsize=FIXED_SUBCELL_FS, color="#151515", linespacing=1.05, zorder=6)

    obsolete_badges = [
        (0.468, 4.48, "EXTINCT IN GEN 1: 10k Manual Label Curation"),
        (1.468, 5.48, "EXTINCT IN GEN 2: stop=['\\n'] Prefix Hacks"),
        (2.468, 4.48, "EXTINCT IN GEN 3: 20-PDF Python Chunking"),
        (3.468, 5.48, "EXTINCT IN GEN 4: Manual CoT Wrappers"),
        (4.468, 4.48, "SINKS IN GEN 5: Manual .mcp.json & CLI"),
    ]
    for ox, oy, otxt in obsolete_badges:
        ax_main.scatter([ox], [oy], color=C_DEMAND, marker="X", s=110, edgecolors="#111111", linewidth=0.9, zorder=10)
        ax_main.text(ox - 0.016, oy, otxt, ha="right", va="center", fontsize=6.0, fontweight="bold", color="#902000",
                     bbox=dict(boxstyle="round,pad=0.11", facecolor="#FFF3CD", edgecolor=C_DEMAND, linewidth=0.9), zorder=10)

    y_mega_specs = [
        (6, "LEVEL 1\nConsumer\nTool", "0h (0 days) | Zero Study Required\n$0 | Free Web / Mobile App\nCasual User (100% Using)"),
        (5, "LEVEL 2\nPrompt &\nWorkspace", "<50h (~1 wk) | Weekend / Short Course\n<$30/mo | Paid Web Tier / Projects\nPower-User (~90% Use / 10% Make)"),
        (4, "LEVEL 3\nWorkflow &\nIntegrator", "<200h (~1 mo) | Boot Camp / 1 Uni Subject\n<$100/mo | AI IDE, API & Vector DB\nApplied SWE (~65% Use / 35% Make)"),
        (3, "LEVEL 4\nHarness &\nTuning Eng.", "~600h (~1 qtr) | 1 Full Uni Semester\n~$1.5k | 1× GPU or CLI + Docker\nSenior SWE / MLE (~35% Use / 65% Make)"),
        (2, "LEVEL 5\nSandbox &\nCluster Arch.", "~2,000h (~1 yr) | Core Master's / Postgrad\n~$500k | 8–64× GPU Cluster / Enclave\nStaff Infra / MLE (~15% Use / 85% Make)"),
        (1, "LEVEL 6\nAI Research\nScientist", "~10,000h (~5 yrs) | Focused AI PhD\n~$100M+ | 1k–100k+ GPU Supercluster\nAI Scientist (100% Genesis)"),
    ]
    ax_main.set_yticks([1, 2, 3, 4, 5, 6])
    ax_main.set_yticklabels([])
    ax_main.text(xm_min - 0.050, 7.22, "HOW TO READ THE Y-AXIS", ha="right", va="top", fontsize=12.5, fontweight="bold", color="#111111", clip_on=False, zorder=8)
    y_axis_guide_body = (
        "Ranks AI usage by three thresholds:\n"
        "Hours & Equivalent: Cumulative\n\"beeline\" study hours from High\nSchool (0h) via the shortest direct\npath, plus course/degree equivalent.\n"
        "Money & Infra ($): Monthly software\nor hardware capital required.\n"
        "Persona (% Use / Make): Role and\neffort split from Using AI (100% L1)\nto Making AI systems (100% L6)."
    )
    ax_main.text(xm_min - 0.050, 7.11, y_axis_guide_body, ha="right", va="top", fontsize=8.8, color="#2B2B2B", linespacing=1.15, clip_on=False, zorder=8)
    for y_pos, y_top_3lines, lvl_bullets in y_mega_specs:
        ylines = y_top_3lines.splitlines()
        for idx_y, yline in enumerate(ylines):
            yy_line = y_pos + 0.34 - idx_y * 0.175
            ax_main.text(xm_min - 0.050, yy_line, yline, ha="right", va="center", fontsize=30.0,
                         fontweight="bold" if idx_y == 0 else "normal", color="#111111", clip_on=False, zorder=7)
        ax_main.text(xm_min - 0.050, y_pos - 0.25, lvl_bullets, ha="right", va="center", fontsize=9.2, color="#2B2B2B", linespacing=1.20, clip_on=False, zorder=7)
    ax_main.set_xticks([])

    # Short & Empty Trapezium Bridge
    ax_trap.set_facecolor("#F4F3EF")
    ax_trap.set_xlim(0.0, 1.0)
    ax_trap.set_ylim(0.0, 1.0)
    ax_trap.set_xticks([])
    ax_trap.set_yticks([])
    u_top = lambda xm: (xm - xm_min) / (xm_max - xm_min)
    u_bot = lambda tb: (tb - tb_min) / (tb_max - tb_min)
    for gid, xm0, xm1, tb0, tb1, _, bg_c, hdr_c in gen_header_specs:
        ut0, ut1 = u_top(xm0), u_top(xm1)
        ub0, ub1 = u_bot(tb0), u_bot(tb1)
        poly = mpatches.Polygon([[ut0, 1.0], [ut1, 1.0], [ub1, 0.0], [ub0, 0.0]], closed=True, facecolor=bg_c, edgecolor="#444444",
                                linestyle="-" if gid != "G5" else "--", linewidth=2.2, alpha=0.88, zorder=2)
        ax_trap.add_patch(poly)
        ax_trap.add_patch(mpatches.Polygon([[ut0, 1.0], [ut1, 1.0], [ub1, 0.0], [ub0, 0.0]], closed=True, facecolor=hdr_c, edgecolor="none", alpha=0.20, zorder=2.5))

    tb_pre_cut, tb_today, tb_post_cut = 2026.62, 2026.803, 2027.21
    ax_trap.plot([u_top(4.50), u_bot(tb_today)], [1.0, 0.0], color="#C00000", linewidth=5.0, zorder=10)
    ax_trap.plot([u_top(4.50), u_bot(tb_pre_cut)], [1.0, 0.0], color=C_HOPE, linestyle=":", linewidth=2.8, zorder=8)
    ax_trap.plot([u_top(4.50), u_bot(tb_post_cut)], [1.0, 0.0], color=C_HOPE, linestyle="--", linewidth=3.4, zorder=8)

    # Top-Right Marginal Histogram
    ax_right.set_facecolor("#FBFBF9")
    gen_line_styles = [("G0", "#555555", "o"), ("G1", "#0072B2", "s"), ("G2", "#D55E00", "^"), ("G3", "#009E73", "D"), ("G4", "#CC79A7", "P")]
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
        ax_right.text(0.764, y_pos + 0.45, f"L{lvl} Mean Rel. Freq:\nUser μ={u_str} | Tok μ={t_mu:.2f}\nTok/User: {tu_str} mean",
                      ha="right", va="top", fontsize=10.2, fontweight="bold", color="#1B2631", linespacing=1.12,
                      bbox=dict(boxstyle="round,pad=0.16", facecolor="white", alpha=0.94, edgecolor="#888888", linewidth=1.2), zorder=8)

    dist_commentary = (
        "DISTRIBUTION & TOKEN/USER SCALING INSIGHTS\n"
        "• Exponential User Decay: As study hours (0h→10,000h) and\n  capital ($0→$100M+) rise, user share drops sharply each\n  level: 63% (L1) → 20% (L2) → 11% (L3) → 4% (L4) → 1% (L5)\n  → 0.1% (L6).\n"
        "• Generational Shape Invariance: Despite 100× user growth\n  and 6,000× token growth (G0–G4), the relative curve shape\n  stays invariant as Down-Ladder Sinking continually refills\n  lower tiers while frontier tasks open at the top.\n"
        "• Center-Level Token Bulge (L2–L4): Unlike users (peaking\n  at L1), 64% of all tokens are consumed in the middle tiers\n  (peaking at L3, μ=0.25) via APIs, RAG, IDEs & agent loops.\n"
        "• 300× Tok/User Surge: Per-user token intensity climbs from\n  0.23× (L1 casual chat) and 0.98× (L2) to 2.37×–4.55× (L3–L4\n  agents), 11.8× (L5 clusters), and 70.0× (L6 pretraining)."
    )
    ax_right.text(0.155, 0.50, dist_commentary, ha="left", va="bottom", fontsize=9.2, color="#1B2631", linespacing=1.15,
                  bbox=dict(boxstyle="round,pad=0.22", facecolor="#F4F1EA", alpha=0.96, edgecolor="#555555", linewidth=1.6), zorder=9)

    ax_right.set_xlim(0.0, 0.78)
    ax_right.set_xticks([0.0, 0.25, 0.50, 0.75])
    ax_right.set_xticklabels(["0.00", "0.25", "0.50", "0.75"], fontsize=19.0, fontweight="bold")
    ax_right.tick_params(axis="x", pad=2)
    ax_right.set_xlabel("")
    ax_right.set_title("Users & Tokens Distribution (Rel. Freq.)", fontsize=21.0, fontweight="bold", pad=12)
    ax_right.grid(True, which="major", linestyle="-", linewidth=1.2, alpha=0.28, color="#888888")
    ax_right.legend(handles=u_handles + t_handles, loc="upper center", bbox_to_anchor=(0.50, 0.998),
                    ncol=2, frameon=True, facecolor="white", framealpha=0.96,
                    fontsize=25.0, columnspacing=0.55, handlelength=1.25, handletextpad=0.38, labelspacing=0.14, borderpad=0.20)
    plt.setp(ax_right.get_yticklabels(), visible=False)

    # Bottom Timeline
    ax_bot.set_facecolor("#FBFBF9")
    ax_bot.set_xlim(tb_min, tb_max)
    t_curve_emp = np.array([2017.42, 2018.0, 2018.8, 2019.5, 2020.42, 2021.0, 2021.8, 2022.5, 2022.83, 2023.3, 2023.8, 2024.33, 2024.6, 2025.00, 2025.5, 2026.0, 2026.62, 2026.803])
    users_emp   = np.array([2.5, 4.5, 8.0, 11.0, 15.0, 24.0, 34.0, 42.0, 65.0, 210.0, 320.0, 480.0, 640.0, 780.0, 920.0, 1040.0, 1120.0, 1150.0]) * 1e6
    money_emp   = np.array([1.8, 2.8, 4.2, 6.5, 11.0, 18.0, 28.0, 38.0, 48.0, 95.0, 145.0, 210.0, 265.0, 340.0, 430.0, 520.0, 610.0, 650.0]) * 1e9
    tokens_emp  = np.array([0.04, 0.07, 0.12, 0.16, 0.25, 0.55, 1.10, 1.45, 2.20, 12.0, 22.0, 45.0, 140.0, 280.0, 520.0, 780.0, 1010.0, 1100.0]) * 1e12
    t_curve_spec = np.array([2026.803, 2027.21, 2027.48, 2027.74, 2028.00])
    users_spec   = np.array([1150.0, 1260.0, 1420.0, 1560.0, 1650.0]) * 1e6
    money_spec   = np.array([650.0, 820.0, 1050.0, 1300.0, 1550.0]) * 1e9
    tokens_spec  = np.array([1100.0, 1550.0, 2600.0, 3700.0, 4800.0]) * 1e12

    ax_bot.fill_between(t_curve_emp, 1e6, users_emp, color=C_DEMAND, alpha=0.09, zorder=1)
    ax_bot.fill_between(t_curve_emp, 1e6, money_emp, color=C_ACTUAL, alpha=0.08, zorder=1)
    ax_bot.fill_between(t_curve_emp, 1e6, tokens_emp, color=C_SUPPLY, alpha=0.09, zorder=1)
    ax_bot.plot(t_curve_emp, users_emp, color=C_DEMAND, linewidth=4.8, marker="o", markersize=8.5, zorder=4, label="Global Active AI Users")
    ax_bot.plot(t_curve_emp, money_emp, color=C_ACTUAL, linewidth=4.8, marker="D", markersize=8.0, zorder=4, label="Global AI Money: Spend & Capex ($)")
    ax_bot.plot(t_curve_emp, tokens_emp, color=C_SUPPLY, linewidth=4.8, marker="s", markersize=8.5, zorder=4, label="Global Annualized Tokens")
    ax_bot.plot(t_curve_spec, users_spec, color=C_DEMAND, linestyle="--", linewidth=4.2, marker="o", markersize=7.5, zorder=4)
    ax_bot.plot(t_curve_spec, money_spec, color=C_ACTUAL, linestyle="--", linewidth=4.2, marker="D", markersize=7.0, zorder=4)
    ax_bot.plot(t_curve_spec, tokens_spec, color=C_SUPPLY, linestyle="--", linewidth=4.2, marker="s", markersize=7.5, zorder=4)

    for gid, _, _, tb0, tb1, _, bg_c, _ in gen_header_specs:
        ax_bot.axvspan(tb0, tb1, color=bg_c, alpha=0.25, zorder=0)
        ax_bot.axvline(tb0, color="#444444", linestyle="-" if gid != "G5" else "--", linewidth=2.2, alpha=0.75, zorder=2)

    ax_bot.axvspan(tb_pre_cut, tb_post_cut, color="#FFD700", alpha=0.18, zorder=1)
    ax_bot.axvline(tb_pre_cut, color=C_HOPE, linestyle=":", linewidth=2.8, zorder=8)
    ax_bot.axvline(tb_today, color="#C00000", linestyle="-", linewidth=5.0, zorder=12)
    ax_bot.axvline(tb_post_cut, color=C_HOPE, linestyle="--", linewidth=3.4, zorder=8)

    year_ticks = list(range(2018, 2029))
    ax_bot.set_xticks(year_ticks)
    ax_bot.set_xticklabels([f"{yr}" for yr in year_ticks], fontsize=22.0, fontweight="bold")
    ax_bot.set_yscale("log")
    ax_bot.set_ylim(1e6, 2.5e16)
    ax_bot.set_yticks([1e6, 1e8, 1e10, 1e12, 1e14, 1e16])
    ax_bot.set_yticklabels([r"$10^{6}$", r"$10^{8}$", r"$10^{10}$", r"$10^{12}$", r"$10^{14}$", r"$10^{16}$"], parse_math=True)
    ax_bot.tick_params(axis="y", labelsize=19.0)
    ax_bot.set_xlabel("")
    ax_bot.set_ylabel("")
    ax_bot.grid(True, which="major", linestyle="-", linewidth=1.2, alpha=0.25, color="#888888")

    cat_styles = {
        "CAT_1": ("#6A3D9A", "#F4ECF7", "#3D1247", "Papers, Meta-Laws & Coinages"),
        "CAT_2": ("#0072B2", "#EAF3FB", "#003B66", "Model, Product & Local Releases"),
        "CAT_3": ("#C00000", "#FFF0E5", "#5E1D00", "Viral, Psychosis/Slop & Security"),
        "CAT_4": ("#116649", "#E8F7F2", "#004430", "Econ, Silicon, Nuclear & Policy"),
        "CAT_5": ("#D55E00", "#FEF9E7", "#5C3D00", "Courses, Benchmarks & Eval Guides"),
        "CAT_6": ("#555555", "#EAECEE", "#1B2631", "Hype Bets & Extinct Habits"),
    }
    h_lines, _ = ax_bot.get_legend_handles_labels()
    cat_patches = [mpatches.Patch(facecolor=bg_c, edgecolor=ed_c, linewidth=2.0, label=lbl_c) for ed_c, bg_c, _, lbl_c in cat_styles.values()]
    leg_bot = ax_bot.legend(handles=h_lines + cat_patches, loc="upper left", bbox_to_anchor=(0.004, 0.990),
                            ncol=2, frameon=True, facecolor="white", framealpha=0.95, fontsize=15.0,
                            columnspacing=0.85, handletextpad=0.45, labelspacing=0.18)

    t_today_box = ax_bot.text(tb_today, 4.0e12, "◀ TODAY ▶", ha="center", va="center", fontsize=21.0, fontweight="bold", color="white",
                              bbox=dict(boxstyle="round,pad=0.14", facecolor="#C00000", edgecolor="#111111", linewidth=2.0), zorder=25)

    mini_events = [
        (2017.46, "2017-06:\nTransformer Paper", 4.5e7, "left", "CAT_1"),
        (2021.48, "2021-06: GitHub\nCopilot Preview", 2.2e9, "center", "CAT_2"),
        (2022.91, "2022-11: ChatGPT\n(100M in 60d)", 2.2e6, "center", "CAT_3"),
        (2024.49, "2024-06: Claude 3.5\nSonnet & Artifacts", 1.8e11, "center", "CAT_2"),
        (2025.08, "2025-01: DeepSeek-R1\nOpen Reasoner", 6.5e6, "left", "CAT_1"),
    ]
    big_texts = [t_today_box]
    for yr_f, ev_txt, ey, ha_e, ecat in mini_events:
        edge_ev, bg_ev, txt_ev, _ = cat_styles[ecat]
        ax_bot.vlines(yr_f, 1e6, ey, color=edge_ev, linestyle=":", linewidth=2.8, alpha=0.85, zorder=18)
        ax_bot.scatter([yr_f], [ey], color=edge_ev, s=90, zorder=19)
        t_b = ax_bot.text(yr_f, ey * 1.35, ev_txt, ha=ha_e, va="bottom", fontsize=21.0, fontweight="bold", color=txt_ev, linespacing=1.08,
                          bbox=dict(boxstyle="round,pad=0.14", facecolor=bg_ev, edgecolor=edge_ev, linewidth=2.2, alpha=0.97), zorder=22)
        big_texts.append(t_b)

    fig.canvas.draw()
    occupied_bboxes = [t.get_window_extent(renderer=renderer).expanded(1.04, 1.12) for t in big_texts]
    occupied_bboxes.append(leg_bot.get_window_extent(renderer=renderer).expanded(1.02, 1.05))
    x_min_px = ax_bot.transData.transform((tb_min + 0.02, 1e6))[0]
    x_today_px = ax_bot.transData.transform((tb_today - 0.02, 1e6))[0]

    candidate_tiers = list(np.geomspace(4.8e15, 1.3e6, 28))
    candidate_dxs = [0.0, -0.04, 0.04, -0.08, 0.08, -0.13, 0.13, -0.18, 0.18]
    emp_events = df_events[df_events["gen_id"] != "G5"].iloc[::2]
    for idx, erow in emp_events.iterrows():
        ex = float(erow["year_float"])
        if ex > tb_today:
            continue
        ecat = erow["category_id"]
        ev_col, bg_ev, txt_ev, _ = cat_styles.get(ecat, cat_styles["CAT_4"])
        lbl_str = textwrap.fill(str(erow["mega_tl_text"]), width=22)
        rot_tiers = candidate_tiers[(idx * 5) % len(candidate_tiers):] + candidate_tiers[:(idx * 5) % len(candidate_tiers)]
        for dx in candidate_dxs:
            found = False
            for cand_ey in rot_tiers:
                bx = np.clip(ex + dx, tb_min + 0.12, tb_today - 0.14)
                t_test = ax_bot.text(bx, cand_ey * 1.08, lbl_str, ha="center", va="bottom", fontsize=5.2, fontweight="bold", linespacing=1.03,
                                     bbox=dict(boxstyle="round,pad=0.06", facecolor=bg_ev, edgecolor=ev_col, linewidth=0.75), alpha=0.0)
                bb_test = t_test.get_window_extent(renderer=renderer).expanded(1.02, 1.04)
                t_test.remove()
                if bb_test.x0 >= x_min_px and bb_test.x1 <= x_today_px and not any(bb_test.overlaps(occ) for occ in occupied_bboxes):
                    occupied_bboxes.append(bb_test)
                    ax_bot.plot([ex, ex, bx], [1e6, cand_ey * 0.84, cand_ey], color=ev_col, linestyle=":", linewidth=0.85, alpha=0.45, zorder=5)
                    ax_bot.scatter([ex], [cand_ey * 0.84 if abs(bx - ex) > 1e-3 else cand_ey], color=ev_col, s=16, alpha=0.72, zorder=6)
                    ax_bot.text(bx, cand_ey * 1.08, lbl_str, ha="center", va="bottom", fontsize=5.2, fontweight="bold", color=txt_ev, linespacing=1.03,
                                bbox=dict(boxstyle="round,pad=0.06", facecolor=bg_ev, edgecolor=ev_col, linewidth=0.75, alpha=0.95), zorder=8)
                    found = True
                    break
            if found:
                break

    # Bottom-Right Field Guide
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
        "• Extended Summary: Expands on the 2-line summary by weaving\n  in and defining the cell's core vocabulary in context.\n"
        "• Use Cases & Landmarks: Practical tasks solved alongside\n  historic launches, papers, demos, or incidents.\n"
        "• User Actions: Hands-on steps taken by the human—from\n  clicks and prompts (L1) to coding, tuning & math (L2–L6).\n"
        "• Models & Products: Neural weights and engines paired\n  with commercial apps, APIs, SDKs, and benchmarks.\n"
        "• Surface & Hardware: The workspace interface (browser,\n  IDE, CLI) and the device or GPU cluster running it.\n"
        "• Scope & Evolution: How this cell connects to adjacent\n  cells—what it absorbed (left), when to step down a\n  level (below), and what sinks to a simpler level (right)."
    )
    ax_corner.text(0.032, 0.818, cell_guide_text, ha="left", va="top", fontsize=11.7, color="#111111", linespacing=1.21, zorder=3)

    out_path = os.path.join(fig_dir, "fig_v5_p0_encyclopedic_megachart_poster.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print(f"[RENDERED MEGACHART POSTER] {out_path}")


def _render_single_panel_news_timeseries(dfs: dict[str, pd.DataFrame], out_path: str, is_poster: bool = False):
    """
    Render Plot 0B / Plot 0B-Mini (`megaTL`):
      - Top Row (`ax_gen`): Compact equal-width GEN 0..GEN 5 header & 3-line description boxes (all descriptions at exact same font size)
      - Middle Row (`ax_trap`): Short and empty trapezium bridge mapping equal-width GEN boxes to true calendar-year generation boundaries
      - Bottom Row (`ax`): Continuous-time log-scale timeline with:
          * 6 Company Product Lines (OpenAI, Anthropic, Google/DeepMind, Meta/Local, DeepSeek, NVIDIA/Capex)
          * 7 Tech-Transfer TRL Lines (Transformer, CoT->RLVR, RLHF/DPO/SAE, RAG/Memory, LoRA/QLoRA/vLLM, Coding Agents/METR, Multimodal Diffusion/Video)
          * Dashed prediction extensions into Gen 5
          * Standalone events not forced onto a horizontal line
          * X and Y tick labels at exact `title_fs`
          * Top 6 events at exact `title_fs`; smallest events at `< 0.25 * title_fs`
          * No X-axis label and no Y-axis label
          * All legend items placed on the right (bottom-right)
    """
    df_events = dfs["defining_events"].copy()

    xm_min, xm_max = -0.50, 5.50
    tb_min, tb_max = 2017.42, 2028.00
    tb_pre_cut  = 2026 + (8 - 1 + 15 / 31.0) / 12.0   # 2026-08-15
    tb_today    = 2026.803                             # 2026-10-20
    tb_post_cut = 2027 + (3 - 1 + 15 / 31.0) / 12.0   # 2027-03-15

    spec_mask = df_events["year_float"] > tb_today
    if spec_mask.any():
        s_min = tb_today
        s_max = float(df_events.loc[spec_mask, "year_float"].max())
        if s_max > s_min:
            df_events.loc[spec_mask, "year_float"] = tb_today + (
                (df_events.loc[spec_mask, "year_float"] - s_min) / (s_max - s_min)
            ) * (tb_max - 0.08 - tb_today)

    if is_poster:
        fig_w, fig_h, dpi = 44.0, 28.0, 300
        title_fs = 21.0              # Title font size = 21.0 pt
        tick_fs = title_fs           # x and y tick labels at exact title_fs (21.0 pt)
        fs_top6_news = title_fs      # Top 6 biggest events at exact title_fs (21.0 pt)
        fs_tier2_max = 11.2          # Tier 2 headline events up to 11.2 pt
        fs_min_news = 4.8            # Smallest events at 4.8 pt (< 0.25 * 21.0 = 5.25 pt)
        sub_fs = 11.5
        gen_hdr_fs = 15.0
        gen_desc_fs = 11.0           # Identical font size across all 6 GEN descriptions
        leg_fs = 11.2
        today_fs = 15.0
        track_lbl_fs = 8.4
        lw_min_news, lw_max_news = 0.80, 2.50
        curve_lw = 4.6
        marker_sz = 8.2
    else:
        fig_w, fig_h, dpi = 24.0, 15.5, 200
        title_fs = 13.5              # Title font size = 13.5 pt
        tick_fs = title_fs           # x and y tick labels at exact title_fs (13.5 pt)
        fs_top6_news = title_fs      # Top 6 biggest events at exact title_fs (13.5 pt)
        fs_tier2_max = 7.0           # Tier 2 headline events up to 7.0 pt
        fs_min_news = 3.1            # Smallest events at 3.1 pt (< 0.25 * 13.5 = 3.375 pt)
        sub_fs = 6.8
        gen_hdr_fs = 9.0
        gen_desc_fs = 6.2            # Identical font size across all 6 GEN descriptions
        leg_fs = 6.8
        today_fs = 9.2
        track_lbl_fs = 5.0
        lw_min_news, lw_max_news = 0.50, 1.65
        curve_lw = 2.8
        marker_sz = 5.2

    fig = plt.figure(figsize=(fig_w, fig_h), dpi=dpi, facecolor="#FBFBF9")
    gs = gridspec.GridSpec(
        3, 1, figure=fig,
        height_ratios=[0.33, 0.13, 5.54],
        left=0.056, right=0.988, bottom=0.052, top=0.924,
        hspace=0.0
    )
    ax_gen  = fig.add_subplot(gs[0, 0])
    ax_trap = fig.add_subplot(gs[1, 0])
    ax      = fig.add_subplot(gs[2, 0])

    # Top Title & Subtitle
    fig.text(
        0.056, 0.962,
        "AI News, Company Product Lines & Tech-Transfer TRL Timeline (2017–2028)",
        ha="left", va="center", fontsize=title_fs, fontweight="bold", color="#111111"
    )
    subtitle_2lines = (
        "Continuous-time atlas of 199 atomic AI milestones (2017–2028): 6 Company Product Lines (OpenAI, Anthropic, Google/DeepMind, Meta/Local, DeepSeek, NVIDIA), 7 Tech-Transfer\n"
        "TRL Lines (paper → end-user default), dashed links to named Gen 5 predictions & standalone events. Font size ∝ news impact (Top 6 = Title Size; Smallest < ¼ Title Size)."
    )
    fig.text(
        0.988, 0.962,
        subtitle_2lines,
        ha="right", va="center", fontsize=sub_fs, style="italic", color="#3B3B3B", linespacing=1.15
    )

    gen_header_specs = [
        (
            "G0", -0.50, 0.50, 2017.42, 2020.42,
            "GEN 0: Pre-LLM & Passive NLP",
            "#EFEFEF", "#555555",
            "Task-specific neural NLP (BERT, spaCy) & XGBoost on labeled CSVs; users meet AI passively via search rankers & Smart Compose."
        ),
        (
            "G1", 0.50, 1.50, 2020.42, 2022.83,
            "GEN 1: Playgrounds & Autocomplete",
            "#EBF3FA", "#0072B2",
            "Few-shot pretraining (GPT-3, Chinchilla) unlocks API playgrounds, diffusion art (DALL-E 2, Midjourney) & Copilot IDE ghost-text."
        ),
        (
            "G2", 1.50, 2.50, 2022.83, 2024.33,
            "GEN 2: Chatbots & Vector RAG",
            "#FDF2E9", "#D55E00",
            "RLHF & ChatGPT make conversational bots universal alongside GPT-4, open-weight LLaMA/QLoRA tuning & LangChain Vector RAG."
        ),
        (
            "G3", 2.50, 3.50, 2024.33, 2025.00,
            "GEN 3: Omni-Modal & Vibe Coding",
            "#E8F6F3", "#009E73",
            "Omni-modal chat (GPT-4o, Claude 3.5), live UI sandboxes (Artifacts, v0) & Cursor multi-file IDEs birth natural-language 'Vibe Coding'."
        ),
        (
            "G4", 3.50, 4.50, 2025.00, 2026.803,
            "GEN 4: Reasoners & CLI Agents",
            "#F9EFF5", "#CC79A7",
            "RLVR test-time reasoners (o1/o3, DeepSeek-R1) & terminal CLI agents (Claude Code, MCP) run multi-hour loops amid 'AI Slop'."
        ),
        (
            "G5", 4.50, 5.50, 2026.803, 2028.00,
            "GEN 5 (Forecasts): Ambient OS & World Sim",
            "#F8ECF5", "#7A2862",
            "Named forecasts: Altman/Ive & Nadella (ambient OS), Amodei (>90% AI code & circuit MRI), LeCun/Fei-Fei Li (3D worlds) & Hassabis (AGI)."
        ),
    ]

    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()

    # 1. Top Compact Equal-Width GEN Header + 3-Line Description Strip (`ax_gen`)
    ax_gen.set_facecolor("#FBFBF9")
    ax_gen.set_xlim(xm_min, xm_max)
    ax_gen.set_ylim(0.0, 1.0)
    ax_gen.set_xticks([])
    ax_gen.set_yticks([])
    for spine in ax_gen.spines.values():
        spine.set_visible(False)

    for gid, xm0, xm1, tb0, tb1, gtitle, bg_c, hdr_c, gexpl in gen_header_specs:
        w_col = xm1 - xm0
        pad_x = 0.022
        ax_gen.axvspan(xm0, xm1, color=bg_c, alpha=0.35, zorder=0)
        hdr_rect = mpatches.FancyBboxPatch(
            (xm0 + pad_x, 0.59), w_col - 2 * pad_x, 0.37,
            boxstyle="round,pad=0.005", facecolor=hdr_c, edgecolor="#111111",
            linewidth=1.8 if is_poster else 1.1, zorder=4
        )
        ax_gen.add_patch(hdr_rect)
        ax_gen.text(
            0.5 * (xm0 + xm1), 0.775, gtitle,
            ha="center", va="center", fontsize=gen_hdr_fs, fontweight="bold", color="white", zorder=5
        )

        expl_rect = mpatches.FancyBboxPatch(
            (xm0 + pad_x, 0.04), w_col - 2 * pad_x, 0.51,
            boxstyle="round,pad=0.005", facecolor="#FFFFFF", edgecolor=hdr_c,
            linewidth=1.6 if is_poster else 1.0, alpha=0.98, zorder=4
        )
        ax_gen.add_patch(expl_rect)
        wrapped_expl = _wrap_to_n_lines_balanced(ax_gen, renderer, gexpl, 3, gen_desc_fs, weight="normal")
        ax_gen.text(
            0.5 * (xm0 + xm1), 0.295, wrapped_expl,
            ha="center", va="center", fontsize=gen_desc_fs, color="#1B2631",
            linespacing=1.06, zorder=5
        )

    # 2. Short & Empty Trapezium Bridge (`ax_trap`)
    ax_trap.set_facecolor("#F4F3EF")
    ax_trap.set_xlim(0.0, 1.0)
    ax_trap.set_ylim(0.0, 1.0)
    ax_trap.set_xticks([])
    ax_trap.set_yticks([])
    for spine in ax_trap.spines.values():
        spine.set_linewidth(1.5 if is_poster else 1.0)
        spine.set_edgecolor("#333333")

    u_top = lambda xm: (xm - xm_min) / (xm_max - xm_min)
    u_bot = lambda tb: (tb - tb_min) / (tb_max - tb_min)

    for gid, xm0, xm1, tb0, tb1, _, bg_c, hdr_c, _ in gen_header_specs:
        ut0, ut1 = u_top(xm0), u_top(xm1)
        ub0, ub1 = u_bot(tb0), u_bot(tb1)
        verts = [(ut0, 1.0), (ut1, 1.0), (ub1, 0.0), (ub0, 0.0)]
        ax_trap.add_patch(mpatches.Polygon(verts, closed=True, facecolor=bg_c, edgecolor="none", alpha=0.88, zorder=1))
        ax_trap.add_patch(mpatches.Polygon(verts, closed=True, facecolor=hdr_c, edgecolor="none", alpha=0.22, zorder=2))
        ax_trap.plot([ut0, ub0], [1.0, 0.0], color="#333333", linestyle="-" if gid != "G5" else "--", linewidth=2.0 if is_poster else 1.3, zorder=4)
        ax_trap.plot([ut1, ub1], [1.0, 0.0], color="#333333", linestyle="-", linewidth=1.4 if is_poster else 0.9, alpha=0.65, zorder=4)

    ax_trap.plot([u_top(4.50), u_bot(tb_pre_cut)], [1.0, 0.0], color=C_HOPE, linestyle=":", linewidth=2.2 if is_poster else 1.4, zorder=5)
    ax_trap.plot([u_top(4.50), u_bot(tb_post_cut)], [1.0, 0.0], color=C_HOPE, linestyle="--", linewidth=2.6 if is_poster else 1.7, zorder=5)
    ax_trap.plot([u_top(4.50), u_bot(tb_today)], [1.0, 0.0], color="#C00000", linestyle="-", linewidth=4.2 if is_poster else 2.8, zorder=8)

    # 3. Main Continuous-Time Log-Scale Timeline (`ax`)
    ax.set_facecolor("#FBFBF9")
    ax.set_xlim(tb_min, tb_max)
    ax.set_yscale("log")
    ax.set_ylim(1e6, 3.2e16)

    for spine in ax.spines.values():
        spine.set_linewidth(2.2 if is_poster else 1.5)
        spine.set_edgecolor("#222222")

    for gid, _, _, tb0, tb1, _, bg_c, _, _ in gen_header_specs:
        ax.axvspan(tb0, tb1, color=bg_c, alpha=0.26, zorder=0)
        ax.axvline(tb0, color="#444444", linestyle="-" if gid != "G5" else "--", linewidth=2.2 if is_poster else 1.4, alpha=0.75, zorder=2)

    # Macro Telemetry Curves (Users, Money $ USD & Annualized Tokens)
    t_curve_emp = np.array([2017.42, 2018.0, 2018.8, 2019.5, 2020.42, 2021.0, 2021.8, 2022.5, 2022.83, 2023.3, 2023.8, 2024.33, 2024.6, 2025.00, 2025.5, 2026.0, 2026.62, 2026.803])
    users_emp   = np.array([2.5, 4.5, 8.0, 11.0, 15.0, 24.0, 34.0, 42.0, 65.0, 210.0, 320.0, 480.0, 640.0, 780.0, 920.0, 1040.0, 1120.0, 1150.0]) * 1e6
    money_emp   = np.array([1.8, 2.8, 4.2, 6.5, 11.0, 18.0, 28.0, 38.0, 48.0, 95.0, 145.0, 210.0, 265.0, 340.0, 430.0, 520.0, 610.0, 650.0]) * 1e9
    tokens_emp  = np.array([0.04, 0.07, 0.12, 0.16, 0.25, 0.55, 1.10, 1.45, 2.20, 12.0, 22.0, 45.0, 140.0, 280.0, 520.0, 780.0, 1010.0, 1100.0]) * 1e12
    t_curve_spec = np.array([2026.803, 2027.21, 2027.48, 2027.74, 2028.00])
    users_spec   = np.array([1150.0, 1260.0, 1420.0, 1560.0, 1650.0]) * 1e6
    money_spec   = np.array([650.0, 820.0, 1050.0, 1300.0, 1550.0]) * 1e9
    tokens_spec  = np.array([1100.0, 1550.0, 2600.0, 3700.0, 4800.0]) * 1e12

    ax.fill_between(t_curve_emp, 1e6, users_emp, color=C_DEMAND, alpha=0.06, zorder=1)
    ax.fill_between(t_curve_emp, 1e6, money_emp, color=C_ACTUAL, alpha=0.06, zorder=1)
    ax.fill_between(t_curve_emp, 1e6, tokens_emp, color=C_SUPPLY, alpha=0.06, zorder=1)
    ax.plot(t_curve_emp, users_emp, color=C_DEMAND, linewidth=curve_lw, marker="o", markersize=marker_sz, alpha=0.82, zorder=3, label="Global Active AI Users")
    ax.plot(t_curve_emp, money_emp, color=C_ACTUAL, linewidth=curve_lw, marker="D", markersize=marker_sz * 0.95, alpha=0.84, zorder=3, label="Global AI Money: Spend & Capex ($ USD)")
    ax.plot(t_curve_emp, tokens_emp, color=C_SUPPLY, linewidth=curve_lw, marker="s", markersize=marker_sz, alpha=0.82, zorder=3, label="Global Annualized Tokens")
    ax.plot(t_curve_spec, users_spec, color=C_DEMAND, linestyle="--", linewidth=curve_lw * 0.85, marker="o", markersize=marker_sz * 0.85, alpha=0.82, zorder=3)
    ax.plot(t_curve_spec, money_spec, color=C_ACTUAL, linestyle="--", linewidth=curve_lw * 0.85, marker="D", markersize=marker_sz * 0.82, alpha=0.84, zorder=3)
    ax.plot(t_curve_spec, tokens_spec, color=C_SUPPLY, linestyle="--", linewidth=curve_lw * 0.85, marker="s", markersize=marker_sz * 0.85, alpha=0.82, zorder=3)

    # Cutoff lines and TODAY marker
    ax.axvspan(tb_pre_cut, tb_post_cut, color="#FFD700", alpha=0.14, zorder=1)
    ax.axvline(tb_pre_cut, color=C_HOPE, linestyle=":", linewidth=2.4 if is_poster else 1.6, zorder=8)
    ax.axvline(tb_today, color="#C00000", linestyle="-", linewidth=4.8 if is_poster else 3.2, zorder=12)
    ax.axvline(tb_post_cut, color=C_HOPE, linestyle="--", linewidth=2.8 if is_poster else 1.8, zorder=8)

    # X and Y tick labels at exact `title_fs`; no X or Y axis labels!
    year_ticks = list(range(2018, 2029))
    ax.set_xticks(year_ticks)
    ax.set_xticklabels([f"{yr}" for yr in year_ticks], fontsize=tick_fs, fontweight="bold")
    ax.set_xlabel("")

    ax.set_yticks([1e6, 1e8, 1e10, 1e12, 1e14, 1e16])
    ax.set_yticklabels([r"$10^{6}$", r"$10^{8}$", r"$10^{10}$", r"$10^{12}$", r"$10^{14}$", r"$10^{16}$"], parse_math=True)
    ax.tick_params(axis="y", labelsize=tick_fs)
    ax.set_ylabel("")
    ax.grid(True, which="major", linestyle="-", linewidth=1.1 if is_poster else 0.7, alpha=0.22, color="#888888")

    # 13 Connected Horizontal Lines (6 Company Product Lines + 7 Tech-Transfer TRL Lines)
    line_id_to_idx = {lid: idx for idx, (lid, *_) in enumerate(HORIZONTAL_LINES_SPEC)}
    track_ys = np.geomspace(1.35e16, 2.2e6, len(HORIZONTAL_LINES_SPEC))

    track_badge_texts = []
    for t_idx, (lid, ltype, lshort, lfull, tcol, _) in enumerate(HORIZONTAL_LINES_SPEC):
        y_tr = track_ys[t_idx]
        sub_df = df_events[df_events["line_id"] == lid].sort_values(by="year_float")
        if sub_df.empty:
            continue
        xs = sub_df["year_float"].to_numpy(dtype=float)
        sals = sub_df["salience"].to_numpy(dtype=float)

        emp_xs = [x for x in xs if x <= tb_today]
        spec_xs = [x for x in xs if x > tb_today]

        # Subtle background lane guide across the chart
        ax.axhline(y_tr, color=tcol, linestyle=":", linewidth=0.8 if is_poster else 0.5, alpha=0.20, zorder=3)

        # Solid line connecting empirical milestones (<= TODAY)
        if len(emp_xs) >= 2:
            ax.plot(
                [emp_xs[0], emp_xs[-1]], [y_tr, y_tr],
                color=tcol, linestyle="-",
                linewidth=3.8 if is_poster else 2.4, alpha=0.72, zorder=5
            )
            for i_pt in range(len(emp_xs) - 1):
                x_a, x_b = float(emp_xs[i_pt]), float(emp_xs[i_pt + 1])
                if (x_b - x_a) > 0.35:
                    x_mid_arrow = 0.5 * (x_a + x_b)
                    ax.annotate(
                        "", xy=(x_mid_arrow + 0.06, y_tr), xytext=(x_mid_arrow - 0.06, y_tr),
                        arrowprops=dict(arrowstyle="-|>", color=tcol, lw=2.2 if is_poster else 1.4, mutation_scale=15 if is_poster else 9.5),
                        zorder=6
                    )

        # Dashed line connecting into Gen 5 predictions (> TODAY)
        if spec_xs:
            x_from = emp_xs[-1] if emp_xs else spec_xs[0]
            x_to = spec_xs[-1]
            ax.plot(
                [x_from, x_to], [y_tr, y_tr],
                color=tcol, linestyle="--",
                linewidth=3.2 if is_poster else 2.0, alpha=0.78, zorder=5
            )
            x_mid_spec = 0.5 * (max(x_from, tb_today) + x_to)
            ax.annotate(
                "", xy=(x_mid_spec + 0.06, y_tr), xytext=(x_mid_spec - 0.06, y_tr),
                arrowprops=dict(arrowstyle="-|>", color=tcol, lw=2.0 if is_poster else 1.2, ls="--", mutation_scale=14 if is_poster else 9.0),
                zorder=6
            )

        # Node markers directly on the horizontal line
        node_sizes = [((28 + 30 * (s - 1.0)) if is_poster else (12 + 15 * (s - 1.0))) for s in sals]
        ax.scatter(xs, [y_tr] * len(xs), color=tcol, edgecolor="white", linewidth=1.2 if is_poster else 0.75, s=node_sizes, alpha=0.95, zorder=8)

        # Left-anchored Horizontal Line Header Badge
        lbl_x = tb_min + 0.035
        prefix_sym = "◆" if ltype == "Company Product Line" else "━▶"
        t_badge = ax.text(
            lbl_x, y_tr * 1.28, f"{prefix_sym} {lshort}",
            ha="left", va="bottom", fontsize=track_lbl_fs, fontweight="bold", color="white",
            bbox=dict(boxstyle="round,pad=0.10", facecolor=tcol, edgecolor="#111111", linewidth=1.2 if is_poster else 0.8, alpha=0.94),
            zorder=26
        )
        track_badge_texts.append(t_badge)

    # All Legend Items Placed on the Right (Bottom-Right)
    cat_styles = {
        "CAT_1": ("#6A3D9A", "#F4ECF7", "#3D1247", "Papers, Meta-Laws & Coinages"),
        "CAT_2": ("#0072B2", "#EAF3FB", "#003B66", "Model, Product & Local Releases"),
        "CAT_3": ("#C00000", "#FFF0E5", "#5E1D00", "Viral, Psychosis/Slop & Security"),
        "CAT_4": ("#116649", "#E8F7F2", "#004430", "Econ, Silicon, Nuclear & Policy"),
        "CAT_5": ("#D55E00", "#FEF9E7", "#5C3D00", "Courses, Benchmarks & Eval Guides"),
        "CAT_6": ("#555555", "#EAECEE", "#1B2631", "Hype Bets & Extinct Habits"),
    }
    h_lines, _ = ax.get_legend_handles_labels()
    line_type_handles = [
        mlines.Line2D([], [], color="#5B2C6F", linestyle="-", linewidth=3.2 if is_poster else 2.0, marker="o", markersize=6, label="Company Product Line (OpenAI, Anthropic, Google, Meta, DeepSeek, NVIDIA)"),
        mlines.Line2D([], [], color="#2874A6", linestyle="-", linewidth=3.2 if is_poster else 2.0, marker="s", markersize=6, label="Tech-Transfer TRL Line (Paper → End-User Default)"),
        mlines.Line2D([], [], color="#7A2862", linestyle="--", linewidth=2.8 if is_poster else 1.8, marker=">", markersize=6, label="Prediction Link (Connects Across TODAY to Named Gen 5 Forecasts)"),
        mlines.Line2D([], [], color="#666666", linestyle="none", marker="d", markersize=6, label="Standalone Milestone (Not Forced Onto a Horizontal Line)"),
    ]
    cat_patches = [mpatches.Patch(facecolor=bg_c, edgecolor=ed_c, linewidth=1.8 if is_poster else 1.2, label=lbl_c) for ed_c, bg_c, _, lbl_c in cat_styles.values()]
    size_patch = mpatches.Patch(
        facecolor="#FFFFFF", edgecolor="#222222", linewidth=1.6 if is_poster else 1.0,
        label="Font Size ∝ News Impact (Top 6 = Title Size; Smallest < ¼ Title Size)"
    )
    leg = ax.legend(
        handles=h_lines[:3] + line_type_handles + cat_patches + [size_patch],
        loc="lower right", bbox_to_anchor=(0.996, 0.010),
        ncol=2, frameon=True, facecolor="white", framealpha=0.97, edgecolor="#222222",
        fontsize=leg_fs, columnspacing=0.80, handletextpad=0.40, labelspacing=0.20, borderpad=0.35
    )
    leg.set_zorder(30)

    t_today_box = ax.text(
        tb_today, 2.0e16, "◀ TODAY: 2026-10-20 ▶",
        ha="center", va="center", fontsize=today_fs, fontweight="bold", color="white",
        bbox=dict(boxstyle="round,pad=0.16", facecolor="#C00000", edgecolor="#111111", linewidth=2.2 if is_poster else 1.5),
        zorder=29
    )

    fig.canvas.draw()
    occupied_bboxes = [t_today_box.get_window_extent(renderer=renderer).expanded(1.02, 1.06)]
    occupied_bboxes.append(leg.get_window_extent(renderer=renderer).expanded(1.02, 1.04))
    for tb_txt in track_badge_texts:
        occupied_bboxes.append(tb_txt.get_window_extent(renderer=renderer).expanded(1.01, 1.02))

    x_min_px   = ax.transData.transform((tb_min + 0.015, 1e6))[0]
    x_today_px = ax.transData.transform((tb_today - 0.015, 1e6))[0]
    x_post_px  = ax.transData.transform((tb_today + 0.015, 1e6))[0]
    x_max_px   = ax.transData.transform((tb_max - 0.015, 1e6))[0]
    y_top_px   = ax.transData.transform((tb_min, 2.85e16))[1]
    y_bot_px   = ax.transData.transform((tb_min, 1.08e6))[1]

    local_y_mults = [
        1.00, 0.78, 1.28, 0.60, 1.65, 0.46, 2.15, 0.35, 2.80, 0.27, 3.60, 0.20
    ]
    global_fallback_tiers = list(np.geomspace(2.4e16, 1.25e6, 84))
    candidate_dxs = [
        0.0, -0.035, 0.035, -0.075, 0.075, -0.12, 0.12, -0.17, 0.17,
        -0.23, 0.23, -0.30, 0.30, -0.38, 0.38, -0.47, 0.47, -0.57, 0.57,
        -0.68, 0.68, -0.80, 0.80, -0.95, 0.95
    ]

    # Sort so Top 6 (S == 5.0) get placed first, then connected line events by salience, then standalone events by salience
    df_events["is_connected"] = df_events["line_id"] != "STANDALONE"
    df_sorted = df_events.sort_values(
        by=["salience", "is_connected", "is_flagship_plot0", "year_float"],
        ascending=[False, False, False, True]
    ).reset_index(drop=True)

    placed_count = 0
    for idx, erow in df_sorted.iterrows():
        ex = float(erow["year_float"])
        lid = str(erow["line_id"])
        sal = float(erow["salience"])
        ecat = str(erow["category_id"])
        ev_col, bg_ev, txt_ev, _ = cat_styles.get(ecat, cat_styles["CAT_4"])

        # Font size rule:
        #   - Top 6 events (sal >= 4.95): exact `title_fs` (fs_top6_news)
        #   - Smallest events (sal <= 1.05): `fs_min_news` (< 0.25 * title_fs)
        #   - Intermediate events: convex scaling between fs_min_news and fs_tier2_max
        if sal >= 4.95:
            ev_fs = fs_top6_news
            frac_s = 1.0
        else:
            u_sal = np.clip((sal - 1.0) / 3.2, 0.0, 1.0) ** 1.35
            ev_fs = fs_min_news + u_sal * (fs_tier2_max - fs_min_news)
            frac_s = 0.75 * u_sal

        ev_lw = lw_min_news + frac_s * (lw_max_news - lw_min_news)
        pad_b = 0.04 + 0.08 * frac_s

        # Exact text as in the Timeline Report (`YYYY-MM: Event Title`)
        raw_lbl = str(erow["mega_tl_text"])
        if sal >= 4.95:
            w_chars = 22
        elif sal >= 3.5:
            w_chars = 25
        else:
            w_chars = 28
        lbl_str = textwrap.fill(raw_lbl, width=w_chars)

        is_spec = (erow["gen_id"] == "G5") or (ex > tb_today)

        if lid != "STANDALONE" and lid in line_id_to_idx:
            t_idx = line_id_to_idx[lid]
            y_tr = track_ys[t_idx]
            cand_ys = [y_tr * m for m in local_y_mults if 1.18e6 <= (y_tr * m) <= 2.5e16] + global_fallback_tiers
        else:
            y_tr = None
            rot = (idx * 11) % len(global_fallback_tiers)
            cand_ys = global_fallback_tiers[rot:] + global_fallback_tiers[:rot]

        placed_this = False
        for pass_relax in [0, 1]:
            exp_x = 1.015 if pass_relax == 0 else 1.002
            exp_y = 1.035 if pass_relax == 0 else 1.005
            for cand_ey in cand_ys:
                for dx in candidate_dxs:
                    if is_spec:
                        bx = np.clip(ex + dx, tb_today + 0.08, tb_max - 0.10)
                    else:
                        bx = np.clip(ex + dx, tb_min + 0.08, tb_today - 0.10)

                    t_test = ax.text(
                        bx, cand_ey, lbl_str,
                        ha="center", va="center", fontsize=ev_fs, fontweight="bold", linespacing=1.02,
                        bbox=dict(boxstyle=f"round,pad={pad_b:.2f}", facecolor=bg_ev, edgecolor=ev_col, linewidth=ev_lw),
                        alpha=0.0
                    )
                    bb_test = t_test.get_window_extent(renderer=renderer).expanded(exp_x, exp_y)
                    t_test.remove()

                    if is_spec:
                        in_bounds = (bb_test.x0 >= x_post_px) and (bb_test.x1 <= x_max_px)
                    else:
                        in_bounds = (bb_test.x0 >= x_min_px) and (bb_test.x1 <= x_today_px)

                    if in_bounds and (bb_test.y1 <= y_top_px) and (bb_test.y0 >= y_bot_px):
                        if not any(bb_test.overlaps(occ) for occ in occupied_bboxes):
                            occupied_bboxes.append(bb_test)
                            if y_tr is not None:
                                # Connected to a Company Product Line or Tech-Transfer TRL Line
                                ax.plot(
                                    [ex, bx], [y_tr, cand_ey],
                                    color=ev_col, linestyle="-" if frac_s >= 0.55 else ":",
                                    linewidth=(1.8 if is_poster else 1.1) if frac_s >= 0.55 else (1.0 if is_poster else 0.65),
                                    alpha=0.72, zorder=7
                                )
                            else:
                                # Standalone Milestone: subtle date anchor dot & short stem without forcing onto a line
                                ax.scatter([ex], [cand_ey], color=ev_col, marker="d", s=18 if is_poster else 9, alpha=0.70, zorder=7)
                                if abs(bx - ex) > 1e-3:
                                    ax.plot([ex, bx], [cand_ey, cand_ey], color=ev_col, linestyle=":", linewidth=0.8 if is_poster else 0.5, alpha=0.55, zorder=6)

                            z_box = int(14 + round(12 * frac_s))
                            ax.text(
                                bx, cand_ey, lbl_str,
                                ha="center", va="center", fontsize=ev_fs, fontweight="bold", color=txt_ev, linespacing=1.02,
                                bbox=dict(boxstyle=f"round,pad={pad_b:.2f}", facecolor=bg_ev, edgecolor=ev_col, linewidth=ev_lw, alpha=0.97),
                                zorder=z_box
                            )
                            placed_count += 1
                            placed_this = True
                            break
                if placed_this:
                    break
            if placed_this:
                break

    fig.savefig(out_path, dpi=dpi)
    plt.close(fig)
    tag = "NEWS MEGACHART POSTER" if is_poster else "MINI NEWS MEGACHART"
    print(f"[RENDERED {tag}] {out_path} (placed {placed_count}/{len(df_sorted)} atomic event textboxes)")


def render_plot0b_mini_news_megachart(dfs: dict[str, pd.DataFrame], fig_dir: str):
    """Render Plot 0B-Mini (`fig_v5_p0b_mini_news_megachart.png`, figsize=(24, 15.5), dpi=200)."""
    out_path = os.path.join(fig_dir, "fig_v5_p0b_mini_news_megachart.png")
    _render_single_panel_news_timeseries(dfs, out_path, is_poster=False)


def render_plot0b_historical_news_megachart_poster(dfs: dict[str, pd.DataFrame], fig_dir: str):
    """Render Plot 0B Poster (`fig_v5_p0b_historical_news_megachart_poster.png`, figsize=(44, 28), dpi=300)."""
    out_path = os.path.join(fig_dir, "fig_v5_p0b_historical_news_megachart_poster.png")
    _render_single_panel_news_timeseries(dfs, out_path, is_poster=True)
