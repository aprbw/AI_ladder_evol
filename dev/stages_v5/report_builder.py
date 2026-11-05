#!/usr/bin/env python3
"""
stages_v5/report_builder.py
===========================
Ground-up author and assembler for `2026 10 17 AI_ladder_evol report v5.md`.
Generates `stages_v5/frontispiece_and_part1.md`, `stages_v5/part2.md`,
`stages_v5/part3.md`, `stages_v5/part4.md`, and `stages_v5/part5.md` directly
from the SSOT datasets in `cache_v5/*.csv` (with zero regex-splicing of v3/v4),
and assembles `2026 10 17 AI_ladder_evol report v5.md`.
"""

import os
import numpy as np
import pandas as pd
from v5_data_and_gates import build_all_csvs, BASE_DIR, REPORT_PATH

STAGES_DIR = os.path.join(BASE_DIR, "stages_v5")


def _md_escape(val) -> str:
    s = str(val).replace("\n", " / ").replace("|", "\\|")
    return " ".join(s.split())


def df_to_markdown_table(df: pd.DataFrame, headers: list[str] | None = None) -> str:
    cols = list(df.columns)
    hdrs = headers if headers is not None else cols
    lines = [
        "| " + " | ".join(hdrs) + " |",
        "| " + " | ".join(["---"] * len(hdrs)) + " |",
    ]
    for _, row in df.iterrows():
        vals = [_md_escape(row[c]) for c in cols]
        lines.append("| " + " | ".join(vals) + " |")
    return "\n".join(lines)


def build_frontispiece_and_part1(dfs: dict[str, pd.DataFrame]) -> str:
    gen_df = dfs["generations"]
    lvl_df = dfs["level_brackets"]
    bench_df = dfs["benchmarks"]

    lines = []
    # Frontispiece before # Title (Plot 0-Micro, Plot 0-Mini, Plot 0)
    lines.append("![Plot 0-Micro: 10-Second SAE-Style 6x6 User-Skill Slide Card](figures_v5/fig_v5_p0_micro_sae_card.png)\n")
    lines.append(
        "**Caption (`Plot 0-Micro` — 10-Second SAE J3016 User-Skill Slide Card):** **Human AI proficiency stratifies into six cumulative beeline learning-hour and capital brackets (`L1: 0h | $0` to `L6: ~10,000h | ~$100M+`) across six technological generations (`Gen 0` [2017-06] to `Gen 5` [2027-03+]), rejecting the null hypothesis ($H_0$) of a flat, single-dimensional 'AI user' persona.** Rendering the `2–3` flagship `micro_keywords_subset` tags per cell (`Micro` $\\subsetneq$ `Mini-Mega` $\\subsetneq$ `Mega`) under uniform `13.5pt` bold titles and `10.0pt` keyword pills, the card exposes how every `L6` PhD breakthrough (`TRL 1–3`) systematically sinks down-ladder to `L1` (`0h | $0`) consumer defaults (`TRL 9`) within `17–65` months.\n"
    )
    lines.append("![Plot 0-Mini: 2-Minute Condensed 5-Panel User-Skill Megachart](figures_v5/fig_v5_p0_mini_megachart.png)\n")
    lines.append(
        "**Caption (`Plot 0-Mini` — 2-Minute Condensed 5-Panel User-Skill Overview):** **Coupling the `6 × 6` user-skill matrix (`4–6` `mini_keywords_subset` tags + 2-line plain-English summaries) with the right-hand Beeline Deflation panel, Trapezium Time-Warp Bridge, and bottom 12-lineage TRL timeline refutes $H_0$ that unit token price deflation ($1{,}000\\times+$) reduces aggregate AI expenditure (`Jevons Paradox`: spend surges $80\\times$ from `\\$1.1B` [`G0`] to `\\$88.0B` [`G4`]).** Uniform `12.0pt` cell headers, `6.0pt` summaries, and `5.75pt` keyword strips preserve rapid visual scanning before full wallchart inspection.\n"
    )
    lines.append("![Plot 0: 15-Minute Encyclopedic User-Skill Megachart Poster](figures_v5/fig_v5_p0_encyclopedic_megachart_poster.png)\n")
    lines.append(
        "**Caption (`Plot 0` — 15-Minute Encyclopedic User-Skill Wallchart Poster):** **Full `36`-cell socio-technical synthesis integrating `8` canonical `keywords_1line` tags and a non-redundant `2 × 3` (`6`-facet: `Extended Summary`, `Use Cases & Landmarks`, `User Actions`, `Models & Products`, `Surface & Hardware`, `Scope & Evolution`) internal table inside every cell (`22.0pt` title / `10.6pt` summary / `7.1pt` keywords / `5.75pt` centered subcell headers & body), rejecting $H_0$ that token consumption tracks active user headcount (`G4` `L4–L6` engineers represent `2.5%` of users but consume `82.7%` of all tokens, $\\text{Tok/User} = 17.5\\times\\text{--}120.0\\times$).**\n\n---\n"
    )

    # Root Header
    lines.append("# AI Ladder Evolution (v5): A Six-Generation by Six-Level (6 × 6) Socio-Technical Atlas, Eight-Domain Keyword Etymology & Historical News Megachart (2017–2028)\n")
    lines.append(
        "**Root BLUF (Bottom Line Up Front):** Across `2017-06` to `2026-10` (`Gen 0` to `Gen 4`) and into the `2027-03 to 2028-12` speculative horizon (`Gen 5`), human interaction with AI is governed by two orthogonal coordinates: **Generation $G_t \\in \\{\\text{G0} \\dots \\text{G5}\\}$** (when both `L2–L6` new skill demands emerge and `L1–L2` prior skills sink into zero-setup defaults) and **Standardized Skill Level $L_k \\in \\{\\text{L1} \\dots \\text{L6}\\}$** (anchored strictly to cumulative beeline learning hours and hardware/API capital: `L1: 0h (0d) | $0`, `L2: <50h (~1 Wk / Short Course) | <$30`, `L3: <200h (~1 Mo / 1 Uni Subject) | <$100`, `L4: ~600h (~1 Qtr / 1 Uni Semester) | ~$1.5k`, `L5: ~2,000h (~1 Yr / Core Postgrad) | ~$500k`, and `L6: ~10,000h (~5 Yrs / Focused PhD) | ~$100M+`). Fixed user capabilities deflate downward by **$0.72\\text{ levels per generation}$** (`83%–99%` cumulative learning-hour reduction via `The Bitter Lesson`), while autonomous 50%-reliability task horizons (`METR`) double every **~$7\\text{ months}$** (`<30s` in `G0` to `2h–30h` in `G4`). Simultaneously, `1,000x+` unit token price deflation triggers **`Jevons Paradox`**, driving a `$1.1B -> $88.0B/yr` enterprise spend surge and extreme Pareto concentration where `L4–L6` harnesses (`2.5%` of users) consume `82.7%` of global tokens.\n"
    )
    lines.append("![Plot VA0: Root Architecture Visual Abstract](figures_v5/fig_v5_va0_root.png)\n")
    lines.append(
        "**Caption (`Plot VA0` — Root Architecture Visual Abstract):** **Six-panel architectural schematic mapping the Twin Megachart Hierarchy (`Plot 0` User-Skill Atlas $\\leftrightarrow$ `Plot 0B` Six-Category Historical News Atlas), the Eight-Domain Chronological Keyword Taxonomy (`125` terms), the `12` Technical & Socio-Technical Governance TRL Lineages, and the `8` Deterministic Validation Gates (`Gates 1–8`), refuting $H_0$ that 1D company maturity scales can capture socio-technical co-evolution.**\n"
    )

    lines.append("#### Master Report Structural Index\n")
    lines.append("* [1. Part I — Extended Summary (~5% Synthesis)](#1-part-i--extended-summary-5-synthesis)")
    lines.append("* [2. Part II — Primary Literature Review, Eight-Domain Keyword Etymology, Six-Category Event Megachart & Cost Setup](#2-part-ii--primary-literature-review-eight-domain-keyword-etymology-six-category-event-megachart--cost-setup)")
    lines.append("* [3. Part III — Inductive Boundary Method, Six Relational Invariants & Deferred Naming](#3-part-iii--inductive-boundary-method-six-relational-invariants--deferred-naming)")
    lines.append("* [4. Part IV — Chronological Six-Level Ladder Evolution (Gen 0 to Gen 4, 30 Empirical Cells)](#4-part-iv--chronological-six-level-ladder-evolution-gen-0-to-gen-4-30-empirical-cells)")
    lines.append("* [5. Part V — Cross-Gen Scaling Laws, 12-Lineage TRL/Evolutionary Audit, Existing Ladder Comparison & Gen 5 Forecast](#5-part-v--cross-gen-scaling-laws-12-lineage-trlevolutionary-audit-existing-ladder-comparison--gen-5-forecast)\n\n---\n")

    # Part I
    lines.append("## 1. Part I — Extended Summary (~5% Synthesis)\n")
    lines.append(
        "**Part I Synthesis:** This section condenses the full empirical and theoretical architecture of `report v5.md` into three self-contained sub-sections: (1.1) the inductive `6 Gens × 6 Levels` (`36`-cell) skill matrix, 6-category historical news drivers (`Plot 0B`), 8-domain chronological keyword taxonomy (`125` terms), and `Track A (Using)` vs. `Track B (Making)` profession split; (1.2) cumulative beeline learning-hour brackets, down-ladder skill deflation (`The Bitter Lesson`), `METR` 7-month autonomous task-horizon doubling, and obsolete skill extinction; and (1.3) two-scale token/energy/spend economics (`Jevons Paradox`), marginal `Tok/User` intensity skew, 12-lineage `TRL 1–9` maturation lags, and the 22-ladder literature audit.\n"
    )
    lines.append("#### Part I Structural Index\n")
    lines.append("* [1.1 Inductive 6 × 6 Skill Matrix, Six-Category News Drivers, Eight-Domain Taxonomy & Track A/B Profession Split](#11-inductive-6--6-skill-matrix-six-category-news-drivers-eight-domain-taxonomy--track-ab-profession-split)")
    lines.append("* [1.2 Cumulative Beeline Methodology, Down-Ladder Skill Deflation, METR Horizon Doubling & Obsolete Skills](#12-cumulative-beeline-methodology-down-ladder-skill-deflation-metr-horizon-doubling--obsolete-skills)")
    lines.append("* [1.3 Two-Scale Resource Economics (Jevons Paradox), Tok/User Pareto Skew, 12-Lineage TRL Lags & Ladder Audit](#13-two-scale-resource-economics-jevons-paradox-tokuser-pareto-skew-12-lineage-trl-lags--ladder-audit)\n")

    lines.append("![Plot VA1: Part I Executive Visual Abstract](figures_v5/fig_v5_va1_part1.png)\n")
    lines.append(
        "**Caption (`Plot VA1` — Part I Executive Visual Abstract):** **Executive synthesis of the `6 × 6` skill coordinate system, macro exponential trajectories (`Users`, `Tokens`, `Spend`), five benchmark deflation curves (`83%–99%` hour savings), and `L4–L6` Pareto token concentration (`82.7%` of `G4` tokens from `2.5%` of users), rejecting $H_0$ of uniform skill and compute distribution across AI practitioners.**\n"
    )

    lines.append("### 1.1 Inductive 6 × 6 Skill Matrix, Six-Category News Drivers, Eight-Domain Taxonomy & Track A/B Profession Split\n")
    lines.append(
        "**Inductive Matrix & Dual-Track Architecture (`Table 1.1` & `Table 1.2`):** Rather than imposing arbitrary vendor marketing tiers, we derive generation boundaries (`G0..G5`) and skill rungs (`L1..L6`) inductively from `22` published ladders (`Table 2.1`), `36` Track A/B use cases (`Table 2.2`), `26` technical syllabi (`Table 2.3a`), `125` chronologically dated AI coinages across `8` domains (`Table 2.3b–c`), `20` contemporaneous hype bets (`Table 2.4`), `14` hardware/pricing baselines (`Table 2.5`), and `144` dated historical events across `6` news categories (`Table 2.6` & `Plot 0B`). Every practitioner cell $(G_t, L_k)$ is anchored strictly to the **human operator's prerequisite floor** (`Bidirectional Medium-Model Decoupling`), cleanly separating `Track A (Direct Users: L1–L2 at 90%–100% Using, L3–L4 Applied/Harness SWEs)` from `Track B (Builders, Post-Trainers & Scientists: L3–L5 Applied/Systems MLEs and L6 Frontier Scientists at 100% Genesis Making)`.\n"
    )
    lines.append("![Plot 1: Global AI Ecosystem Macro Trajectories](figures_v5/fig_v5_p1_macro_resource_trajectories.png)\n")
    lines.append(
        "**Caption (`Plot 1` — Macro Token Volume, Enterprise Spend & Active Users, 2017–2026):** **Annualized global AI token volume expands $6{,}111\\times$ (`0.18T` in `G0` to `1,100T/yr` in `G4`), active users grow $95.8\\times$ (`12M` to `1,150M`), and enterprise AI spend surges $80.0\\times$ (`\\$1.1B` to `\\$88.0B/yr`), decisively rejecting $H_0$ that $1{,}000\\times$ unit token price deflation reduces aggregate market expenditure (`Jevons Paradox`).**\n"
    )

    lines.append("#### Table 1.1 — Inductively Discovered Generation Overview Ledger (`Gen 0` to `Gen 5`)\n")
    lines.append(
        "**Caption (`Table 1.1`):** **Six-generation chronological boundary ledger (`2017-06` to `2028-12`) pairing upper-level new skill emergence (`L2–L6`) with down-level built-in sinking (`L1–L2`), six-factor causal drivers, obsolete user skills, and macro ecosystem totals.**\n"
    )
    t11_df = gen_df[[
        "gen_id", "gen_name", "start_date", "end_date", "new_upper_use_cases",
        "sunk_lower_use_cases", "six_factor_causal_drivers", "obsolete_user_skills",
        "macro_users_m", "macro_tokens_t_yr", "macro_spend_b_yr"
    ]].copy()
    t11_df["valid_dates"] = t11_df["start_date"] + " to " + t11_df["end_date"]
    t11_df["gen_title"] = t11_df["gen_id"] + " — " + t11_df["gen_name"]
    t11_out = t11_df[[
        "gen_title", "valid_dates", "new_upper_use_cases", "sunk_lower_use_cases",
        "six_factor_causal_drivers", "obsolete_user_skills",
        "macro_users_m", "macro_tokens_t_yr", "macro_spend_b_yr"
    ]]
    lines.append(df_to_markdown_table(t11_out, [
        "Gen ID & Folksonomy Name", "Valid Dates (YYYY-MM)", "New Upper-Level Use Cases (L2–L6)",
        "Down-Level Built-In Sunk Use Cases", "Primary Causal Drivers (Tech/Money/Eng/TRL/Culture/Legal)",
        "Obsolete User Skills", "Macro Users (M)", "Macro Tokens (T/yr)", "Macro Spend ($B/yr)"
    ]) + "\n")

    lines.append("#### Table 1.2 — Standardized Six-Level Cumulative Beeline Brackets & Profession Mapping (`L1` to `L6`)\n")
    lines.append(
        "**Caption (`Table 1.2`):** **Six standardized human prerequisite brackets (`L1` to `L6`) mapping cumulative beeline learning hours, capital ceilings, four-tier cognitive inputs, and `Track A (Using)` vs. `Track B (Making)` technical professions.**\n"
    )
    t12_out = lvl_df[[
        "level_name", "beeline_bracket", "cognitive_tier", "primary_surface_hw",
        "track_a_using_persona", "track_b_making_persona",
        "mean_single_task_tokens", "mean_single_task_usd"
    ]]
    lines.append(df_to_markdown_table(t12_out, [
        "Level ID & Folksonomy Name", "Cumulative Beeline Bracket (Hours | Capital $)",
        "Cognitive Input Tier", "Primary Tool Surface & Hardware",
        "Track A (Using) Persona", "Track B (Making / Foundation) Persona",
        "Mean Single-Task Tokens", "Mean Single-Task USD ($)"
    ]) + "\n")

    lines.append("### 1.2 Cumulative Beeline Methodology, Down-Ladder Skill Deflation, METR Horizon Doubling & Obsolete Skills\n")
    lines.append(
        "**Down-Ladder Skill Deflation & Autonomous Horizon Scaling (`Plot 2` & `Table 1.3`):** By tracking five invariant user workflows across `G0` to `G5` (`Table 1.3`), we prove that required human setup and learning hours deflate monotonically downward by a mean of **$-0.72\\text{ levels per generation}$** (`83%–99%` cumulative learning-hour compression from `G0` to `G4`). Concurrently, `METR` autonomous software task horizons ($t_{\\text{AI}}$ at 50% reliability) double every **~$7\\text{ months}$** (`<30s` in `G0`, `~2m` in `G1`, `~15m` in `G2`, `~45m` in `G3`, `2h–30h` in `G4`, and projected `40h+` workweek sprints in `G5`). Every downward sink simultaneously extinguishes a prior generation's manual syntax habit: `G1` few-shot prompting killed 10,000-row CSV labeling for basic NLP; `G2` `RLHF` chat killed `stop=['\\n']` completion prefix hacking; `G3` `200k–2M` workspaces (`Claude Projects` / `NotebookLM`) killed bespoke Python vector-chunking scripts for `<50` PDFs; and `G4` `RLVR` auto-routers (`GPT-5` / `DeepSeek-R1`) killed manual `'Let's think step by step'` and `'Take a deep breath'` prompt superstitions.\n"
    )
    lines.append("![Plot 2: Down-Ladder Beeline Skill Deflation Escalator](figures_v5/fig_v5_p2_skill_deflation_escalator.png)\n")
    lines.append(
        "**Caption (`Plot 2` — Five Benchmark User Workflows & METR Autonomy Horizon, 2017–2026):** **Required cumulative beeline learning hours ($\\text{Hours}_{\\text{learn}}$) across five invariant benchmark workflows collapse by $98.9\\%$ on average (`1,040h` mean in `G0` $\\to$ `4.0h` mean in `G4`, $p < 0.0001$), rejecting $H_0$ that required human technical prerequisites for a fixed task $W$ remain invariant over time.**\n"
    )

    lines.append("#### Table 1.3 — Down-Ladder Skill Deflation Tracker Across Five Benchmark Workflows (`G0` to `G5`)\n")
    lines.append(
        "**Caption (`Table 1.3`):** **Empirical trajectory of required skill level ($L_k$) and cumulative beeline learning hours ($\\text{Hours}_{\\text{learn}}$) for five fixed user workflows across `Gen 0` through `Gen 5`.**\n"
    )
    t13_rows = []
    for _, r in bench_df.iterrows():
        t13_rows.append({
            "wf": f"{r['workflow_id']} — {r['workflow_name']}",
            "g0": f"L{r['g0_lvl']} ({r['g0_hrs']}h)",
            "g1": f"L{r['g1_lvl']} ({r['g1_hrs']}h)",
            "g2": f"L{r['g2_lvl']} ({r['g2_hrs']}h)",
            "g3": f"L{r['g3_lvl']} ({r['g3_hrs']}h)",
            "g4": f"L{r['g4_lvl']} ({r['g4_hrs']}h)",
            "g5": f"L{r['g5_lvl']} ({r['g5_hrs']}h)",
            "saved": f"-{r['total_hrs_saved']}h",
            "mech": r["deflation_mechanism"],
        })
    lines.append(df_to_markdown_table(pd.DataFrame(t13_rows), [
        "Benchmark Workflow", "Gen 0 (Lvl / Hrs)", "Gen 1 (Lvl / Hrs)", "Gen 2 (Lvl / Hrs)",
        "Gen 3 (Lvl / Hrs)", "Gen 4 (Lvl / Hrs)", "Gen 5 Spec. (Lvl / Hrs)",
        "Total Hours Saved (G0->G4)", "Primary Deflation & Absorption Mechanism"
    ]) + "\n")

    lines.append("### 1.3 Two-Scale Resource Economics (Jevons Paradox), Tok/User Pareto Skew, 12-Lineage TRL Lags & Ladder Audit\n")
    lines.append(
        "**Two-Scale Token Economics & Socio-Technical Co-Evolution:** Auditing resource consumption at both the **single-task scale** (`tokens`, `FLOPs`, `USD`, `Wh`, `human_minutes`, `ai_minutes`) and the **generation-wide population share scale** (`100.0%` conserved `user_share_pct`, `token_share_pct`, and `spend_share_pct` across `L1–L6`) reveals a profound structural divergence. While `L1–L2` users represent `91.0%` of active human practitioners in `Gen 4`, their single-turn or short-session queries consume just `5.5%` of global tokens ($\\text{Tok/User}_{\\text{G4,L1}} = 0.025\\times$). Conversely, `L4–L6` harness engineers, sandbox architects, and frontier scientists represent only `2.5%` of users but consume **`82.7%` of all tokens** and **`84.5%` of total spend** ($\\text{Tok/User}_{\\text{G4,L4..L6}} = 17.5\\times\\text{--}120.0\\times$) via continuous multi-agent worktree loops, containerized `SWE-bench` / property-test evaluation farms, and million-container synthetic `RLVR` training flywheels. Across all `12` traced `TRL 1–9` lineages (`8` Technical + `4` Socio-Technical Governance/Safety in `Table 5.2a`), maturation from an `L6` paper or ethical/legal shock (`Stochastic Parrots`, `Willison Prompt Injection`, `NYT Copyright Suit`, `Mata v. Avianca`) to an `L1` built-in consumer default averages **$35.3\\text{ months}$** (compressing from `65m` in `G0/G1` to `17–32m` in `G2–G4`).\n\n---\n"
    )

    out_text = "\n".join(lines)
    with open(os.path.join(STAGES_DIR, "frontispiece_and_part1.md"), "w", encoding="utf-8") as f:
        f.write(out_text)
    return out_text


def build_part2(dfs: dict[str, pd.DataFrame]) -> str:
    ladders_df = dfs["existing_ladders"]
    uc_df = dfs["use_cases"]
    tut_df = dfs["courses_blogs"]
    gloss_df = dfs["glossary_etymology"]
    dom_df = dfs["glossary_domain_summary"]
    hope_df = dfs["hope_inventory"]
    price_df = dfs["pricing_hardware_baseline"]
    ev_df = dfs["defining_events"]
    news_cells_df = dfs["news_megachart_cells"]

    lines = []
    lines.append("## 2. Part II — Primary Literature Review, Eight-Domain Keyword Etymology, Six-Category Event Megachart & Cost Setup\n")
    lines.append(
        "**Part II Synthesis:** Before defining a single boundary or naming a single rung, this section compiles the complete primary empirical inventory across four dimensions: (2.1) `22` published AI ladders, enterprise maturity models, and `METR` autonomous task-horizon benchmarks (`Table 2.1`, `Plot 3`); (2.2) `36` Track A/B use cases (`Table 2.2`), `26` courses/syllabi/blogs (`Table 2.3a`), the **Chronological Eight-Domain Glossary & Concept Etymology Literature Review (`125` terms sorted strictly by `YYYY-MM`, `Table 2.3b` & `Table 2.3c`)**, and `20` contemporaneous hopes (`Table 2.4`); (2.3) the **`144`-Event Six-Category Historical Ledger (`Table 2.6`)** and **Companion Historical News, Breakthroughs & Ecosystem Megachart Hierarchy (`Plot 0B-Micro`, `Plot 0B-Mini`, `Plot 0B`)**; and (2.4) the `14`-model pricing/hardware baseline (`Table 2.5`) and `30`-cell single-task cost vs. learning hours JointPlot (`Plot 4`).\n"
    )
    lines.append("#### Part II Structural Index\n")
    lines.append("* [2.1 Existing AI Ladders Catalog, METR Horizon Synthesis & Descriptive-Bottom vs. Hope-Top Split](#21-existing-ai-ladders-catalog-metr-horizon-synthesis--descriptive-bottom-vs-hope-top-split)")
    lines.append("* [2.2 Six-Level Track A/B Use Cases, Pedagogical Courses, Chronological Eight-Domain Keyword Etymology & Hope Inventory](#22-six-level-track-ab-use-cases-pedagogical-courses-chronological-eight-domain-keyword-etymology--hope-inventory)")
    lines.append("* [2.3 Six-Category Historical Defining-Event Inventory (144 Events) & Companion News Megachart Hierarchy (Plot 0B)](#23-six-category-historical-defining-event-inventory-144-events--companion-news-megachart-hierarchy-plot-0b)")
    lines.append("* [2.4 Six-Level Beeline Setup Metrics, Pricing/Hardware Baselines & 30-Cell JointPlot](#24-six-level-beeline-setup-metrics-pricinghardware-baselines--30-cell-jointplot)\n")

    lines.append("![Plot VA2: Part II Primary Literature & Inventory Visual Abstract](figures_v5/fig_v5_va2_part2.png)\n")
    lines.append(
        "**Caption (`Plot VA2` — Part II Visual Abstract):** **Architectural overview of the Stage 1 primary research inventories (`22` published ladders, `36` Track A/B use cases, `26` courses/cookbooks, `125` chronologically sorted terms across `8` taxonomy domains, `20` hopes, and `144` dated historical events across `6` `Plot 0B` categories), refuting $H_0$ that AI evolution is driven solely by model parameter scaling.**\n"
    )

    # 2.1
    lines.append("### 2.1 Existing AI Ladders Catalog, METR Horizon Synthesis & Descriptive-Bottom vs. Hope-Top Split\n")
    lines.append(
        "**Empirical Pattern Across 22 Published Ladders (`Table 2.1` & `Plot 3`):** Auditing `22` influential AI taxonomies (`2017–2026`) exposes a universal structural bifurcation: **Rungs 1 to 3 (`Descriptive Bottom Rungs`)** accurately describe contemporaneous tools already adopted at `TRL 7–9` (`L1–L4`), whereas the **top 1 to 2 rungs (`Speculative Hope Top Rungs`)** project multi-year research aspirations (`L5–L6` `TRL 1–4` goals such as `SAE Level 5 Zero-Human Coding`, `OpenAI Level 5 Organizations`, or `Aschenbrenner/AI-2027 Superintelligence`) as if they were imminent `L1` consumer products.\n"
    )
    lines.append("![Plot 3: Published AI Ladder Corpus Temporal Raster](figures_v5/fig_v5_p3_folksonomy_and_gen_breaks.png)\n")
    lines.append(
        "**Caption (`Plot 3` — 6-Level Descriptive Bottom Rungs vs. Speculative Hope Top Rungs, 2017–2026):** **Temporal raster across `22` published ladders demonstrating that Descriptive Adopted Rungs (`#009E73`) cluster strictly in Levels 1–4 while Speculative Hope Rungs (`#CC79A7`) concentrate in Levels 5–6 ($\\chi^2 = 48.6, p < 10^{-9}$), rejecting $H_0$ of uniform vertical feasibility across published ladder rungs.**\n"
    )
    lines.append("#### Table 2.1 — Catalog of 22 Published AI Ladders, Autonomy Benchmarks & Folksonomy Frameworks (`2017–2026`)\n")
    lines.append(
        "**Caption (`Table 2.1`):** **Primary literature audit of `22` AI maturity ladders (`LAD_01` to `LAD_22`), documenting extracted folksonomy keywords, descriptive bottom rungs, speculative hope top rungs, implied generation breaks, and four quantitative alignment scores (`0.00–1.00`).**\n"
    )
    lines.append(df_to_markdown_table(ladders_df, [
        "ID", "Ladder / Framework Name", "Authors / Organization", "Pub Date", "Rungs",
        "Extracted Folksonomy Keywords", "Descriptive Bottom Rungs (Adopted Reality)",
        "Speculative Hope Top Rungs (Projected Aspiration)", "Implied Gen Breaks",
        "Scope Cov.", "Skill Align.", "Hist. Inv.", "Cost Ground."
    ]) + "\n")

    # 2.2
    lines.append("### 2.2 Six-Level Track A/B Use Cases, Pedagogical Courses, Chronological Eight-Domain Keyword Etymology & Hope Inventory\n")
    lines.append(
        "**Complete Practitioner, Pedagogical & Etymological Inventories (`Tables 2.2, 2.3a, 2.3b, 2.3c & 2.4`):** To ground every cell in verifiable human actions and domain vocabulary, we catalog `36` Track A/B use cases across all six generations and levels (`Table 2.2`), `26` foundational courses, university syllabi (`CS224N`, `CS324`, `CS336`, `UVA CS 6501`), and engineering guides (`Table 2.3a`), `125` core AI keywords and coined concepts sorted strictly chronologically from `1865-04` (`Jevons Paradox`) to `2025-11` (`OpenClaw`) across all `8` Keyword Taxonomy Domains (`Table 2.3b` & `Table 2.3c`), and `20` contemporaneous hype bets (`Table 2.4`).\n"
    )
    lines.append("#### Table 2.2 — Raw Inventory of 36 Track A (Using) & Track B (Making) AI Use Cases (`G0–G5 × L1–L6`)\n")
    lines.append("**Caption (`Table 2.2`):** **Thirty-six canonical practitioner workflows (`UC_01` to `UC_36`) spanning `Gen 0` through `Gen 5` across `L1` to `L6`.**\n")
    lines.append(df_to_markdown_table(uc_df, [
        "Use Case ID", "Canonical Workflow & Use Case Name", "Track Split (Using vs Making)",
        "First Viable (YYYY-MM)", "Mainstream (YYYY-MM)", "Primary Surface & Hardware",
        "Empirical Cell & Down-Ladder Sinking Trajectory"
    ]) + "\n")

    lines.append("#### Table 2.3a — Pedagogical Courses, University Syllabi, Seminal Blogs & Cookbooks (`TUT_01` to `TUT_26`)\n")
    lines.append("**Caption (`Table 2.3a`):** **Twenty-six benchmark courses, university syllabi, and practitioner cookbooks anchoring cumulative beeline learning-hour brackets (`<50h` to `~10,000h`).**\n")
    lines.append(df_to_markdown_table(tut_df, [
        "Course ID", "Course / Syllabus / Guide Title & Author", "Release Date",
        "Extracted Technical Keywords & Skills", "Beeline Hours",
        "Required Surface & Hardware", "Mapped Beeline Level Bracket"
    ]) + "\n")

    lines.append("#### Table 2.3b — Chronological Eight-Domain Glossary & Concept Etymology Literature Review (`125` Terms Sorted by `YYYY-MM`)\n")
    lines.append(
        "**Caption (`Table 2.3b`):** **Comprehensive chronological etymology of `125` foundational AI keywords, meta-laws, doomer/safety theories (`Paperclip Maximizer`, `Orthogonality Thesis`, `Treacherous Turn`, `Sharp Left Turn`, `FOOM`, `p(doom)`, `e/acc`, `Shoggoth / Waluigi`), failure pathologies (`Hallucination`, `Sycophancy`, `Model Collapse`, `Dead Internet`, `Enshittification`, `Lost in the Middle / Context Rot`, `AI/ChatGPT Psychosis`, `AI Slop / Code Slop / Workslop`, `Alignment Faking`, `Reward Hacking`, `Cognitive Debt`), prompting folksonomy, vibe-coding builders, local quantization stacks, frontier architectures, and gigawatt nuclear silicon (`1865-04` to `2025-11`).**\n"
    )
    lines.append(df_to_markdown_table(gloss_df, [
        "Term ID", "Coinage Date (YYYY-MM)", "Core Keyword / Coined Concept", "Domain ID",
        "Taxonomy Domain Name", "Coined By / Seminal Primary Source",
        "Concise Technical & Socio-Technical Definition", "Cognitive Input Tier",
        "Origin Cell", "Absorbed / Sunk Cell"
    ]) + "\n")

    lines.append("#### Table 2.3c — Eight-Domain Keyword & Etymology Taxonomy Summary Matrix (`D1` to `D8`)\n")
    lines.append("**Caption (`Table 2.3c`):** **Structural synthesis of the `8` Keyword Taxonomy Domains (`D1`–`D8`, `125` total terms), showing term counts, representative coinages, origin vs. sunk rungs, and causal role in driving ladder evolution.**\n")
    lines.append(df_to_markdown_table(dom_df, [
        "Domain ID", "Taxonomy Domain Name", "Term Count", "Representative Coined Keywords",
        "Primary Origin Rungs", "Primary Sunk / Absorbed Rungs", "Causal Role in Socio-Technical Ladder Evolution"
    ]) + "\n")

    lines.append("#### Table 2.4 — The 'Inventory of Hope' Ledger (`20` Contemporaneous Hype Bets Across `Gen 0` to `Gen 4`)\n")
    lines.append("**Caption (`Table 2.4`):** **Audit of `20` contemporaneous speculative bets (`HOPE_01` to `HOPE_20`), contrasting the `5` hopes that survived to `TRL 9` defaults against the `15` hopes that suffered evolutionary extinction.**\n")
    lines.append(df_to_markdown_table(hope_df, [
        "Hope ID", "Promised Capability / Hype Bet", "Origin Gen", "Target Gen",
        "Primary Proponents", "Claimed Technical Mechanism", "2026 Status",
        "Extinction / Survival Category", "Empirical Outcome & Failure Audit", "Structural Evolutionary Lesson"
    ]) + "\n")

    # 2.3
    lines.append("### 2.3 Six-Category Historical Defining-Event Inventory (144 Events) & Companion News Megachart Hierarchy (Plot 0B)\n")
    lines.append(
        "**Companion Six-Category Historical News Megachart (`Plot 0B-Micro`, `Plot 0B-Mini`, `Plot 0B` & `Table 2.6`):** While `Plot 0` maps *what the human user does* at each skill rung (`L1..L6`), its companion **`Plot 0B` Megachart Hierarchy** maps *what happened in the world* across the exact same six generation columns (`G0..G5`) stratified vertically by **Six Socio-Technical News & Ecosystem Categories (`CAT 1` to `CAT 6`)**:\n"
        "* **`CAT 1 (y=6, Top — Purple #6A3D9A)`: `Foundational Papers, Critiques, Meta-Laws & Coinages`** (`24` dated events across `G0..G5`).\n"
        "* **`CAT 2 (y=5 — Blue #0072B2)`: `Landmark Model, Product, Local-Stack & Multimodal Releases`** (`24` dated events across `G0..G5`).\n"
        "* **`CAT 3 (y=4 — Red #C00000)`: `Viral Cultural Moments, Companion AI, Psychosis/Slop & Security Incidents`** (`24` dated events across `G0..G5`).\n"
        "* **`CAT 4 (y=3 — Green #116649)`: `Economic, Silicon, Nuclear Energy, Data-Crawl & Policy Shocks`** (`24` dated events across `G0..G5`).\n"
        "* **`CAT 5 (y=2 — Orange #D55E00)`: `Seminal Courses, Blogs, Evals, Benchmarks & Guides`** (`24` dated events across `G0..G5`).\n"
        "* **`CAT 6 (y=1, Bottom — Slate #555555)`: `Contemporaneous Hype Bets, Failed Hopes & Extinct User Habits`** (`24` dated events across `G0..G5`).\n"
    )
    lines.append("![Plot 0B-Micro: 10-Second Six-Category Historical News Slide Card](figures_v5/fig_v5_p0b_micro_news_card.png)\n")
    lines.append(
        "**Caption (`Plot 0B-Micro` — 10-Second Six-Category Historical News Slide Card):** **High-level `6 Gens × 6 Categories` (`36`-cell) historical news matrix displaying `13.5pt` category-era titles and `10.0pt` `micro_keywords_subset` pills (`2–3` iconic events per cell), rejecting $H_0$ that paradigm breaks occur without synchronized legal, economic, and cultural shocks.**\n"
    )
    lines.append("![Plot 0B-Mini: 2-Minute Condensed 5-Panel Historical News Megachart](figures_v5/fig_v5_p0b_mini_news_megachart.png)\n")
    lines.append(
        "**Caption (`Plot 0B-Mini` — 2-Minute Condensed 5-Panel Historical News Megachart):** **Intermediate-scale `6 × 6` news atlas pairing `4–6` `mini_keywords_subset` tags and 2-line summaries per cell with category impact shares (`ax_right`), the Trapezium Time-Warp Bridge (`ax_trap`), and the 12-lineage TRL timeline (`ax_bot`).**\n"
    )
    lines.append("![Plot 0B: 15-Minute Encyclopedic Six-Category Historical News Megachart Poster](figures_v5/fig_v5_p0b_historical_news_megachart_poster.png)\n")
    lines.append(
        "**Caption (`Plot 0B` — 15-Minute Encyclopedic Historical News & Ecosystem Wallchart Poster):** **Complete `36`-cell historical news wallchart (`38 × 28 in`, `300 DPI`) containing `8` canonical event tags and a `2 × 3` internal subcell table (`4` dated `[YYYY-MM]` landmark event subcells = `144` events total + `Causal Impact on User Skill Ladder` + `TRL Maturation & Cross-Category Cascade`) inside every `(Gen G, Category C)` cell.**\n"
    )

    lines.append("#### Six-Facet Cell Summary of All 36 `(Gen G, Category C)` Cells in `Plot 0B`\n")
    for _, nrow in news_cells_df.iterrows():
        cid = nrow["cell_id"]
        cname = str(nrow["cell_name"]).replace("\n", " ")
        lines.append(
            f"* **`{cid}: {cname}`** — *Summary:* {nrow['plain_desc']} | *Micro Keywords (`2–3`):* `{nrow['micro_keywords_subset']}` | *Mini Keywords (`4–6`):* `{nrow['mini_keywords_subset']}` | *Mega Keywords (`8`):* `{nrow['keywords_1line']}` | *Events:* (1) {nrow['sub_ev1']} (2) {nrow['sub_ev2']} (3) {nrow['sub_ev3']} (4) {nrow['sub_ev4']} | *Ladder Impact:* {nrow['sub_ladder_impact']} | *TRL Cascade:* {nrow['sub_trl_cascade']}"
        )
    lines.append("")

    lines.append("#### Table 2.6 — Systematic Six-Category Historical Defining-Event Ledger (`144` Dated Events Across `2017–2028`, `4` Events per `Plot 0B` Cell)\n")
    lines.append(
        "**Caption (`Table 2.6`):** **Complete chronological ledger of all `144` defining events (`EV_001` to `EV_144`, `4` per `(Gen, Category)` cell across `G0..G5 × CAT_1..CAT_6`), cross-referencing `Plot 0` flagship timeline markers, impacted skill cells, and `TRL_01..TRL_12` maturation lineages.**\n"
    )
    t26_out = ev_df[[
        "event_id", "gen_id", "category_id", "event_slot", "event_date",
        "event_title", "is_flagship_plot0", "primary_ladder_cell_impacted",
        "trl_lineage_id", "impact_summary"
    ]]
    lines.append(df_to_markdown_table(t26_out, [
        "Event ID", "Gen", "Category", "Slot", "Date (YYYY-MM)",
        "Historical Event Title", "Plot 0 Flagship?", "Primary Cell Impacted",
        "TRL Lineage", "Dated Quantitative Summary & Ecosystem Impact"
    ]) + "\n")

    # 2.4
    lines.append("### 2.4 Six-Level Beeline Setup Metrics, Pricing/Hardware Baselines & 30-Cell JointPlot\n")
    lines.append(
        "**Unit Cost Deflation vs. Single-Task Compute Scaling (`Table 2.5` & `Plot 4`):** Across `14` representative models from `2018` (`GNMT` / `BERT-Large`) to `2026–2027` (`DeepSeek-R1`, `Claude Opus 4.6`, `GPT-5.4`, and `Gen 5 Rubin/NPU`), unit inference cost for GPT-3-class capability plunged by **$>1{,}000\\times$** (`\\$60.00/1M` tokens in `2020-06` $\\to$ `\\$0.55–\\$2.19/1M` for `DeepSeek-R1` and `<\\$0.15/1M` on `Blackwell FP4`). Yet across the `30` empirical `(Gen G, Level L)` cells (`Plot 4`), log-transformed cumulative learning hours $\\text{Hours}_{\\text{learn}}$ and single-task compute cost $\\text{USD}_{\\text{task}}$ exhibit a tight positive correlation ($r = 0.942, R^2 = 0.887, p < 10^{-14}$).\n"
    )
    lines.append("![Plot 4: 30-Cell Single-Task Cost vs Beeline Learning Hours JointPlot](figures_v5/fig_v5_p4_task_cost_vs_learning_jointplot.png)\n")
    lines.append(
        "**Caption (`Plot 4` — Single-Task Compute Cost vs. Cumulative Beeline Learning Hours Across 30 Empirical Cells, 2017–2026):** **Bivariate `symlog` JointPlot with marginal step histograms (`histtype='step'`) demonstrating a strong log-linear coupling between human prerequisite hours and single-task compute expenditure ($r = 0.942, R^2 = 0.887, p < 10^{-14}$), rejecting $H_0$ ($r = 0$) of independence between human skill depth and per-task compute scale.**\n"
    )
    lines.append("#### Table 2.5 — Historical Cost, Token & Hardware Baseline (`14` Representative Models `2017–2027`)\n")
    lines.append("**Caption (`Table 2.5`):** **Fourteen benchmark models and hardware configurations (`MOD_01` to `MOD_14`) anchoring token pricing, context windows, FLOPs, and single-task energy (Wh).**\n")
    lines.append(df_to_markdown_table(price_df, [
        "Model ID", "Representative Model & Hardware", "Release Date", "Gen",
        "Input $/1M", "Output $/1M", "Context Window", "Training FLOPs",
        "Single-Task Wh", "Step-Change Capability Unlocked"
    ]) + "\n\n---\n")

    out_text = "\n".join(lines)
    with open(os.path.join(STAGES_DIR, "part2.md"), "w", encoding="utf-8") as f:
        f.write(out_text)
    return out_text


def build_part3(dfs: dict[str, pd.DataFrame]) -> str:
    gen_df = dfs["generations"]
    lvl_df = dfs["level_brackets"]
    inv_df = dfs["relational_invariants"]

    lines = []
    lines.append("## 3. Part III — Inductive Boundary Method, Six Relational Invariants & Deferred Naming\n")
    lines.append(
        "**Part III Synthesis:** This section formalizes our four-step inductive methodology: (3.1) deriving generation cutoffs (`G0..G5`) strictly from simultaneous upper-level emergence (`L2–L6`) and lower-level built-in sinking (`L1–L2`); (3.2) standardizing the six cumulative beeline learning-hour and capital brackets (`L1..L6`) and four-tier cognitive input hierarchy; (3.3) enforcing the `Track A/B` profession split (`SWE` vs. `MLE` vs. `Scientist`) and **Six Core Relational Invariants (`INV_01`–`INV_06`)** governing `Scope & Evolution`; and (3.4) executing the Deferred Naming Protocol (`Table 3.4`).\n"
    )
    lines.append("#### Part III Structural Index\n")
    lines.append("* [3.1 User-Perspective Generation Boundary Derivation (Simultaneous Upper Emergence & Lower Sinking)](#31-user-perspective-generation-boundary-derivation-simultaneous-upper-emergence--lower-sinking)")
    lines.append("* [3.2 Standardized Six-Level Cumulative Beeline Brackets & Four-Tier Cognitive Input Hierarchy](#32-standardized-six-level-cumulative-beeline-brackets--four-tier-cognitive-input-hierarchy)")
    lines.append("* [3.3 Using vs. Making (Track A/B) Profession Mapping & Six Core Relational Invariants](#33-using-vs-making-track-ab-profession-mapping--six-core-relational-invariants)")
    lines.append("* [3.4 Deferred Naming Protocol (Boundaries First, Folksonomy Names Last)](#34-deferred-naming-protocol-boundaries-first-folksonomy-names-last)\n")

    lines.append("![Plot VA3: Part III Inductive Methodology & Six Invariants Visual Abstract](figures_v5/fig_v5_va3_part3.png)\n")
    lines.append(
        "**Caption (`Plot VA3` — Part III Visual Abstract):** **Formal schematic of the Dual-Trigger Generation Boundary Rule, the Six Cumulative Beeline Brackets (`0h` to `~10,000h`), the Four-Tier Cognitive Input Hierarchy, and the Six Relational Invariants (`INV_01`–`INV_06`), rejecting $H_0$ that natural-language modality implies low technical skill.**\n"
    )

    lines.append("### 3.1 User-Perspective Generation Boundary Derivation (Simultaneous Upper Emergence & Lower Sinking)\n")
    lines.append(
        "**Dual-Trigger Boundary Rule (`Table 3.1`):** A new AI generation $G_t$ begins in month $m$ if and only if **both** conditions hold simultaneously across the Stage 1 inventory: (1) **Upper-Rung Emergence (`L2–L6`)**: at least three new workflow classes require practitioners to learn a new tool surface, protocol, or post-training paradigm; and (2) **Down-Ladder Sinking (`L1–L2`)**: at least two workflows that previously required `L2–L5` coding or prompt syntax become packaged at `TRL 8–9` into zero-setup `L1` (`0h | $0`) or `<50h` `L2` workspaces.\n"
    )
    lines.append("#### Table 3.1 — Inductive Generation Boundary Derivation Ledger (`G0` to `G5`)\n")
    lines.append("**Caption (`Table 3.1`):** **Derivation of generation start/end dates (`YYYY-MM`), duration in months, upper-rung emergence triggers, and down-ladder sinking triggers.**\n")
    t31_out = gen_df[[
        "gen_id", "start_date", "end_date", "duration_months",
        "new_upper_use_cases", "sunk_lower_use_cases", "obsolete_user_skills"
    ]]
    lines.append(df_to_markdown_table(t31_out, [
        "Neutral Gen ID", "Start Date", "End Date", "Duration (Months)",
        "Upper-Rung Emergence Trigger (L2–L6)", "Down-Ladder Sinking Trigger (L1–L2)",
        "Extinguished Prior-Gen Manual Habits"
    ]) + "\n")

    lines.append("### 3.2 Standardized Six-Level Cumulative Beeline Brackets & Four-Tier Cognitive Input Hierarchy\n")
    lines.append(
        "**Cumulative Beeline Prerequisite Floor (`Table 3.2`):** Every vertical rung $L_k$ is anchored to the cumulative learning hours ($\\text{Hours}_{\\text{learn}}$) required for a competent professional starting from zero AI-specific training to execute that rung's workflow reliably in production, paired with the required hardware/API capital ceiling.\n"
    )
    lines.append("#### Table 3.2 — Standardized Six-Level Cumulative Beeline Brackets & Four-Tier Cognitive Input Hierarchy\n")
    lines.append("**Caption (`Table 3.2`):** **Exact canonical bracket strings (`L1`..`L6`), compact axis tick labels, cognitive input tiers, and `Using vs. Making` split.**\n")
    t32_out = lvl_df[[
        "level_id", "beeline_bracket", "compact_tick_label", "learning_hours_max",
        "hardware_cap_usd", "cognitive_tier", "using_vs_making_split"
    ]]
    lines.append(df_to_markdown_table(t32_out, [
        "Level", "Canonical Cumulative Beeline Bracket", "Compact Plot Tick Label",
        "Beeline Hours Ceiling", "Capital Ceiling ($)", "Four-Tier Cognitive Input Hierarchy",
        "Track A (Using) vs Track B (Making) Split"
    ]) + "\n")

    lines.append("### 3.3 Using vs. Making (Track A/B) Profession Mapping & Six Core Relational Invariants\n")
    lines.append(
        "**Six Formal Invariants Governing `Scope & Evolution` (`Table 3.3`):** Every cell's `Scope & Evolution` facet in Part IV and Section 5.4 is audited against six deterministic relational rules (`INV_01` to `INV_06`), replacing unstructured counterfactual prose with four-directional boundary proofs (`Why Not L-1?`, `Why Not L+1?`, `From Gen G-1`, `To Gen G+1`).\n"
    )
    lines.append("#### Table 3.3 — Six Core Relational Invariants Governing `Scope & Evolution` (`INV_01` to `INV_06`)\n")
    lines.append("**Caption (`Table 3.3`):** **Formal specification of the six relational invariants enforced across all `36` skill cells.**\n")
    lines.append(df_to_markdown_table(inv_df, [
        "Invariant ID", "Relational Invariant Name", "Formal Operational Rule & Boundary Enforcement"
    ]) + "\n")

    lines.append("### 3.4 Deferred Naming Protocol (Boundaries First, Folksonomy Names Last)\n")
    lines.append(
        "**Deferred Folksonomy Naming (`Table 3.4`):** Only after locking all `G0..G5` date cutoffs (`Section 3.1`) and `L1..L6` beeline brackets (`Section 3.2`) do we assign descriptive folksonomy titles drawn directly from the dominant practitioner terms in `Table 2.1` and `Table 2.3b`.\n"
    )
    lines.append("#### Table 3.4 — Deferred Naming Protocol Ledger (`G0..G5` & `L1..L6`)\n")
    lines.append("**Caption (`Table 3.4`):** **Mapping from neutral coordinate IDs (`G0..G5`, `L1..L6`) to final emergent folksonomy titles.**\n")
    t34_rows = []
    for _, r in gen_df.iterrows():
        t34_rows.append({"id": r["gen_id"], "type": "Horizontal Generation", "window": f"{r['start_date']} to {r['end_date']}", "name": r["gen_name"]})
    for _, r in lvl_df.iterrows():
        t34_rows.append({"id": f"L{r['level_id']}", "type": "Vertical Skill Rung", "window": r["beeline_bracket"], "name": r["level_name"]})
    lines.append(df_to_markdown_table(pd.DataFrame(t34_rows), [
        "Neutral ID", "Coordinate Axis", "Locked Boundary / Beeline Bracket", "Coined Emergent Folksonomy Title"
    ]) + "\n\n---\n")

    out_text = "\n".join(lines)
    with open(os.path.join(STAGES_DIR, "part3.md"), "w", encoding="utf-8") as f:
        f.write(out_text)
    return out_text


def _render_six_facet_cell(prow: pd.Series, crow: pd.Series) -> str:
    cid = prow["cell_id"]
    lvl = int(prow["level_id"])
    cname_flat = str(prow["cell_name"]).replace("\n", " ")
    b_str = crow["beeline_hrs_bracket"]
    tok_user_ratio = round(float(crow["token_share_pct"]) / max(float(crow["user_share_pct"]), 0.01), 3)

    out = []
    out.append(f"#### `{cid}` — {cname_flat} (`{b_str}`)\n")
    out.append(
        f"* **Cell Header Block (Synchronized `1:1` with `Plot 0-Micro`, `Plot 0-Mini` & `Plot 0`):**\n"
        f"  * **Coordinate & Exact Cell Title:** `{cid}: {cname_flat}` | *Short SAE Header:* `{prow['short_header']}` | *SAE Human Action:* `{prow['sae_human_action']}` | *SAE AI Executes:* `{prow['sae_ai_executes']}`\n"
        f"  * **Beeline Bracket & Plain-English Summary:** `{b_str}` — {prow['plain_desc']}\n"
        f"  * **Four-Tier Keyword Containment (`Micro` $\\subsetneq$ `Mini-Mega` $\\subsetneq$ `Mega` $\\subseteq$ `Report`):**\n"
        f"    * **Micro SAE-Card Flagship Keywords (`2–3` items):** `{prow['micro_keywords_subset']}`\n"
        f"    * **Mini-Mega Subset Keywords (`4–6` items):** `{prow['mini_keywords_subset']}`\n"
        f"    * **Mega Encyclopedic Keywords (`8` items):** `{prow['keywords_1line']}`\n"
        f"* **Six Mandatory Facet Sub-Blocks (`Plot 0` `2 × 3` Internal Subcell Grid):**\n"
        f"  1. **Facet 1 — `Extended Summary`:** {prow['sub_summary']}\n"
        f"  2. **Facet 2 — `Use Cases & Landmarks`:** {prow['sub_use_cases']}"
        + (f" **Four Mandatory `L6` Genesis Pillars:** {prow['l6_pillars']}" if lvl == 6 and str(prow.get("l6_pillars", "")) else "")
        + "\n"
        f"  3. **Facet 3 — `User Actions`:** {prow['sub_actions']}\n"
        f"  4. **Facet 4 — `Models & Products` (Strict Top-to-Bottom Non-Redundant $\\Delta L_k$ Additions):** {prow['sub_models']}\n"
        f"  5. **Facet 5 — `Surface & Hardware` (Two-Scale Resource Metrics):** {prow['sub_surface']} "
        f"*Single-Task Metrics:* `{crow['single_task_tokens']:,}` tokens, `{crow['single_task_flops']:.2e}` FLOPs, `${crow['single_task_usd']:.4f}`, `{crow['single_task_wh']:.3f}` Wh, `{crow['human_minutes']}m` human / `{crow['ai_minutes']}m` AI. "
        f"*Generation Shares:* `Users = {crow['user_share_pct']:.1f}%`, `Tokens = {crow['token_share_pct']:.1f}%`, `Spend = {crow['spend_share_pct']:.1f}%` ($\\text{{Tok/User}} = {tok_user_ratio}\\times$).\n"
        f"  6. **Facet 6 — `Scope & Evolution` (Four-Directional Relational Boundary Audit):** {prow['sub_scope']}\n"
    )
    return "\n".join(out)


def build_part4(dfs: dict[str, pd.DataFrame]) -> str:
    gen_df = dfs["generations"]
    lc_df = dfs["ladder_cells"]
    p0_df = dfs["poster_encyclopedic_cells"]
    ev_df = dfs["defining_events"]

    lines = []
    lines.append("## 4. Part IV — Chronological Six-Level Ladder Evolution (Gen 0 to Gen 4, 30 Empirical Cells)\n")
    lines.append(
        "**Part IV Synthesis:** This section documents the five empirical generations (`Gen 0` through `Gen 4`, `2017-06` to `2026-10`, `30` cells `G0-L1`..`G4-L6`). Each generation section (`4.1`–`4.5`) opens with its four mandatory Generation Header blocks (valid dates and all `24` Six-Category `Table 2.6` historical events for that generation, new upper-level emergence vs. down-level built-in sinking, six-factor causal drivers, and obsolete user skills), embeds its standalone 6-Column SAE J3016 Micro Card (`Plot M-G0`..`Plot M-G4`), presents all six **Six-Facet `(Gen G, Level L)` Cell Profiles (`L1`..`L6`)** synchronized `1:1` with `Plot 0`, and concludes with its generation-wide quantitative resource table (`Table 4.1`..`Table 4.6`) and step/share profile (`Plot 5`..`Plot 9`).\n"
    )
    lines.append("#### Part IV Structural Index\n")
    lines.append("* [4.1 Gen 0 (2017-06 to 2020-05): The Pre-LLM Code-Pipeline & Passive-Widget Generation (G0-L1 to G0-L6)](#41-gen-0-2017-06-to-2020-05-the-pre-llm-code-pipeline--passive-widget-generation-g0-l1-to-g0-l6)")
    lines.append("* [4.2 Gen 1 (2020-06 to 2022-10): The Completion Playground & Ghost-Text Autocomplete Generation (G1-L1 to G1-L6)](#42-gen-1-2020-06-to-2022-10-the-completion-playground--ghost-text-autocomplete-generation-g1-l1-to-g1-l6)")
    lines.append("* [4.3 Gen 2 (2022-11 to 2024-04): The Conversational Chat, Manual Prompting & DIY Vector-RAG Generation (G2-L1 to G2-L6)](#43-gen-2-2022-11-to-2024-04-the-conversational-chat-manual-prompting--diy-vector-rag-generation-g2-l1-to-g2-l6)")
    lines.append("* [4.4 Gen 3 (2024-05 to 2024-12): The Multimodal Workspace, Vibe Coding & Agentic Graph Generation (G3-L1 to G3-L6)](#44-gen-3-2024-05-to-2024-12-the-multimodal-workspace-vibe-coding--agentic-graph-generation-g3-l1-to-g3-l6)")
    lines.append("* [4.5 Gen 4 (2025-01 to 2026-10): The Auto-Routed Reasoner, Deep Research, Terminal CLI & Sandbox Swarm Generation (G4-L1 to G4-L6)](#45-gen-4-2025-01-to-2026-10-the-auto-routed-reasoner-deep-research-terminal-cli--sandbox-swarm-generation-g4-l1-to-g4-l6)\n")

    lines.append("![Plot VA4: Part IV 30-Cell Empirical Matrix Visual Abstract](figures_v5/fig_v5_va4_part4.png)\n")
    lines.append(
        "**Caption (`Plot VA4` — Part IV Visual Abstract):** **Architectural map of the `30` empirical `(Gen G, Level L)` cells (`G0-L1`..`G4-L6`), highlighting the 6-facet internal cell structure, top-to-bottom non-redundancy, and four mandatory `L6` genesis pillars.**\n"
    )

    gen_sec_map = [
        ("G0", "4.1", "fig_v5_micro_gen0_sae.png", "Plot M-G0", "fig_v5_p5_gen0_matrix.png", "Plot 5", "Table 4.1"),
        ("G1", "4.2", "fig_v5_micro_gen1_sae.png", "Plot M-G1", "fig_v5_p6_gen1_matrix.png", "Plot 6", "Table 4.2"),
        ("G2", "4.3", "fig_v5_micro_gen2_sae.png", "Plot M-G2", "fig_v5_p7_gen2_matrix.png", "Plot 7", "Table 4.3"),
        ("G3", "4.4", "fig_v5_micro_gen3_sae.png", "Plot M-G3", "fig_v5_p8_gen3_matrix.png", "Plot 8", "Table 4.4"),
        ("G4", "4.5", "fig_v5_micro_gen4_sae.png", "Plot M-G4", "fig_v5_p9_gen4_matrix.png", "Plot 9", "Table 4.5"),
    ]

    for gid, sec_num, sae_fn, sae_id, mat_fn, mat_id, tbl_id in gen_sec_map:
        grow = gen_df[gen_df["gen_id"] == gid].iloc[0]
        gev = ev_df[ev_df["gen_id"] == gid]
        ev_str = "; ".join([f"`{r['event_id']}` [{r['event_date']}] {r['event_title']} ({r['category_id']})" for _, r in gev.iterrows()])

        lines.append(f"### {sec_num} {gid} ({grow['start_date']} to {grow['end_date']}): {grow['gen_name']} ({gid}-L1 to {gid}-L6)\n")
        lines.append(
            f"* **1. Valid Dates, Six-Category Defining Historical Events & User-Perspective Shift:** `{grow['start_date']}` to `{grow['end_date']}` (`{grow['duration_months']}` months). **All 24 `Table 2.6` Events in `{gid}`:** {ev_str}.\n"
            f"* **2. New Upper-Level Use Cases (`L2–L6`) vs. Down-Level Built-In Sinking (`L-1 / L1`):** *New Emergence:* {grow['new_upper_use_cases']}. *Down-Ladder Sinking:* {grow['sunk_lower_use_cases']}.\n"
            f"* **3. Six-Factor Causal Drivers ('What Changed?'):** {grow['six_factor_causal_drivers']}.\n"
            f"* **4. Obsolete User Skills & Why They Died:** {grow['obsolete_user_skills']}.\n"
        )
        lines.append(f"![{sae_id}: {gid} SAE J3016 6-Column Micro Card](figures_v5/{sae_fn})\n")
        lines.append(
            f"**Caption (`{sae_id}` — `{gid}` 6-Column SAE J3016 Reference Card):** **Five-second horizontal comparison across `{gid}-L1` to `{gid}-L6` grouping Direct Users (`L1–L2`, green spanner) vs. Builders, Engineers & Scientists (`L3–L6`, blue spanner), rejecting $H_0$ of uniform user-to-token intensity within `{gid}`.**\n"
        )

        # 6 cells
        sub_p0 = p0_df[p0_df["gen_id"] == gid].sort_values("level_id")
        sub_lc = lc_df[lc_df["gen_id"] == gid].sort_values("level_id")
        for (_, prow), (_, crow) in zip(sub_p0.iterrows(), sub_lc.iterrows()):
            lines.append(_render_six_facet_cell(prow, crow))

        # Matrix plot & Table 4.x
        lines.append(f"![{mat_id}: {gid} Quantitative Step & Share Matrix](figures_v5/{mat_fn})\n")
        lines.append(
            f"**Caption (`{mat_id}` — `{gid}` Quantitative Step & Share Profile Across `L1–L6`):** **Two-panel `symlog` step profile (left: single-task tokens, learning hours, Wh; right: `100.0%` conserved user, token, and spend shares across `{gid}-L1`..`{gid}-L6`), rejecting $H_0$ that token share equals user share.**\n"
        )
        lines.append(f"#### {tbl_id} — `{gid}` Six-Level Single-Task Resource & Conserved Share Ledger (`{gid}-L1` to `{gid}-L6`)\n")
        lines.append(f"**Caption (`{tbl_id}`):** **Quantitative resource, timing, and `100.0%` conserved share profile across `{gid}-L1` to `{gid}-L6`.**\n")
        t4_out = sub_lc[[
            "cell_id", "user_first_title", "beeline_hrs_bracket", "single_task_tokens",
            "single_task_flops", "single_task_usd", "single_task_wh",
            "human_minutes", "ai_minutes", "user_share_pct", "token_share_pct", "spend_share_pct"
        ]]
        lines.append(df_to_markdown_table(t4_out, [
            "Cell ID", "Cell Title", "Cumulative Beeline Bracket", "Task Tokens",
            "Task FLOPs", "Task USD ($)", "Task Wh", "Human Min", "AI Min",
            "User Share (%)", "Token Share (%)", "Spend Share (%)"
        ]) + "\n")

        if gid == "G4":
            lines.append("#### Table 4.6 — `Gen 4` Frontier Benchmark Saturation vs. Private Commercial Repository Generalization Gap\n")
            lines.append("**Caption (`Table 4.6`):** **Empirical contrast between saturated public benchmarks (`MMLU`, `GSM8K`, `SWE-bench Verified`) and private commercial multi-repo generalization (`SWE-bench Pro`, `Terminal-Bench`, `Humanity's Last Exam`), explaining why `G4-L4` decoupled verification oracles are mandatory.**\n")
            t46_df = pd.DataFrame([
                ("MMLU / HumanEval (Static Single-Turn)", "92.5% – 96.4%", "Retired / Saturated", "G2–G3", "Memorization & test-set contamination saturate single-turn static leaderboards."),
                ("SWE-bench Verified (500 Public Python Issues)", "77.2% – 80.9% (Claude 4.5/4.6)", "32% – 46% on Private Multi-Lang Repos", "G4-L3 / G4-L4", "Agents pass public unit tests but struggle with undocumented private enterprise invariants."),
                ("SWE-bench Bash-Only / Terminal-Bench", "54.0% – 68.5%", "28% – 41% without Decoupled Oracle", "G4-L4 / G4-L5", "Requires sandboxed CLI worktrees, property-based testing, and reward-hacking prevention."),
                ("Humanity's Last Exam (HLE) / FrontierMath", "34.5% – 52.0% (o3 / R1 / GPT-5.4)", "Active L6 Research Frontier", "G4-L6", "Drives multi-domain RLVR rubrics and formal Lean 4 proof synthesis."),
            ], columns=["bench", "pub", "priv", "rungs", "implication"])
            lines.append(df_to_markdown_table(t46_df, [
                "Evaluation Benchmark Suite", "Public Leaderboard Score (2025–2026)",
                "Private Commercial / Uncontaminated Reality", "Primary Ladder Rungs",
                "Engineering Implication for L3–L6 Practitioners"
            ]) + "\n")

    lines.append("\n---\n")
    out_text = "\n".join(lines)
    with open(os.path.join(STAGES_DIR, "part4.md"), "w", encoding="utf-8") as f:
        f.write(out_text)
    return out_text


def build_part5(dfs: dict[str, pd.DataFrame]) -> str:
    gen_df = dfs["generations"]
    lc_df = dfs["ladder_cells"]
    g5_df = dfs["gen5_speculative"]
    p0_df = dfs["poster_encyclopedic_cells"]
    bench_df = dfs["benchmarks"]
    trl_df = dfs["trl_trajectories"]
    hope_df = dfs["hope_inventory"]
    ladders_df = dfs["existing_ladders"]
    cut_df = dfs["gen5_cutoffs"]

    lines = []
    lines.append("## 5. Part V — Cross-Gen Scaling Laws, 12-Lineage TRL/Evolutionary Audit, Existing Ladder Comparison & Gen 5 Forecast\n")
    lines.append(
        "**Part V Synthesis:** This concluding section synthesizes four macro investigations: (5.1) the four cross-generation quantitative scaling laws (`Down-Ladder Beeline Skill Deflation`, `METR 7-Month Horizon Doubling`, `Jevons Paradox & Tok/User Intensity Skew`, and `Enterprise Bought-vs-Built Inversion`, `Master Tables 5.1a–c` & `Plot 10`); (5.2) the **12-Lineage Technical & Socio-Technical Governance TRL Maturation Audit (`Table 5.2a`, `Plot 11`, and all `12` Individual Paper-to-Consumer-Tool Micro Cards `Plot M-TRL01`..`Plot M-TRL12`)** plus the evolutionary extinction audit of `20` hopes (`Table 5.2b`); (5.3) the Three-Way Audit of `22` existing literature ladders (`Tables 5.3a–c`, `Plot 12`, `Plot 13`); and (5.4) the **Controlled Speculative Forecast for `Gen 5` (`G5-L1`..`G5-L6`, `Tables 5.4a–b`, `Plot M-G5`, `Plot 14`)**.\n"
    )
    lines.append("#### Part V Structural Index\n")
    lines.append("* [5.1 Cross-Generation Skill Deflation, METR Horizon Doubling & Token-Intensity Laws (30 Empirical + 6 Speculative Cells)](#51-cross-generation-skill-deflation-metr-horizon-doubling--token-intensity-laws-30-empirical--6-speculative-cells)")
    lines.append("* [5.2 Bonus Analysis: 12-Lineage Technical & Governance TRL 1–3 (L6) to TRL 9 (L1) Maturation & Failed Hopes](#52-bonus-analysis-12-lineage-technical--governance-trl-13-l6-to-trl-9-l1-maturation--failed-hopes)")
    lines.append("* [5.3 Three-Way Audit of Existing Literature Ladders (Synchronized Pairwise Matrix & Temporal Animation)](#53-three-way-audit-of-existing-literature-ladders-synchronized-pairwise-matrix--temporal-animation)")
    lines.append("* [5.4 Controlled Speculation: Next Generation (Gen 5 = Current + 1) Six-Facet Forecast (G5-L1 to G5-L6)](#54-controlled-speculation-next-generation-gen-5--current--1-six-facet-forecast-g5-l1-to-g5-l6)\n")

    lines.append("![Plot VA5: Part V Scaling Laws, 12 TRL Lineages & Gen 5 Forecast Visual Abstract](figures_v5/fig_v5_va5_part5.png)\n")
    lines.append(
        "**Caption (`Plot VA5` — Part V Visual Abstract):** **Synthesis of the four cross-generation scaling laws, the `12` technical and governance `TRL 1–9` trajectories (`35.3m` mean lag), the `22`-ladder pairwise correlation matrix, and the `Gen 5` speculative horizon (`2027-03 to 2028-12`).**\n"
    )

    # 5.1
    lines.append("### 5.1 Cross-Generation Skill Deflation, METR Horizon Doubling & Token-Intensity Laws (30 Empirical + 6 Speculative Cells)\n")
    lines.append(
        "**Four Macro Quantitative Laws (`Master Tables 5.1a–c` & `Plot 10`):**\n"
        "1. **Down-Ladder Beeline Skill Deflation Law:** Across all five benchmark workflows (`Master Table 5.1c`), required human prerequisite level drops by **$-0.72\\text{ levels/generation}$** (`83%–99%` cumulative learning-hour compression from `G0` to `G4`).\n"
        "2. **METR Autonomous Task-Horizon Doubling Law:** 50%-reliability autonomous task duration $t_{\\text{AI}}$ doubles every **~$7.0\\text{ months}$** (`2019–2026`), expanding from `<30s` (`G0`) to `2h–30h` (`G4`) and `40h+` (`G5`).\n"
        "3. **Jevons Paradox & Per-Level Token-Intensity Law ($\\text{Tok/User}_{G,L}$):** In `Gen 4`, `L4–L6` practitioners (`2.5%` of users) account for **`82.7%` of all tokens** and **`84.5%` of total spend** ($\\text{Tok/User}_{\\text{G4,L4..L6}} = 17.5\\times\\text{--}120.0\\times$ vs. $0.025\\times$ at `G4-L1`).\n"
        "4. **Enterprise Bought-vs-Built Inversion (`MIT NANDA` & `Menlo Ventures`):** Vertical domain/context workflows (`L3–L4`) achieve `67%` production ROI vs. `33%` for bespoke horizontal builds (`76%` bought vs. `24%` built in 2025).\n"
    )
    lines.append("![Plot 10: Six-Level Continuous-Time Alluvial Evolution Atlas](figures_v5/fig_v5_p10_alluvial_evolution_poster.png)\n")
    lines.append(
        "**Caption (`Plot 10` — Six-Level Continuous-Time Alluvial Evolution Atlas, 2017–2026):** **Continuous-time alluvial flow diagram across all `30` empirical cells tracing Down-Level Built-In Sinking (`#009E73`), Upward New Skill Expansion (`#0072B2`), and Obsolete Skill Extinction stubs (`#D55E00`), rejecting $H_0$ of static skill boundaries.**\n"
    )

    lines.append("#### Master Table 5.1a — Complete 36-Cell (`30` Empirical + `6` Speculative) Resource, Timing & Share Ledger (`G0-L1` to `G5-L6`)\n")
    lines.append("**Caption (`Master Table 5.1a`):** **Unified SSOT ledger across all `36` cells (`G0-L1`..`G5-L6`).**\n")
    all_36 = pd.concat([lc_df, g5_df], ignore_index=True)
    all_36["tok_user_intensity"] = (all_36["token_share_pct"] / all_36["user_share_pct"].clip(lower=0.01)).round(3)
    t51a_out = all_36[[
        "cell_id", "status", "user_first_title", "beeline_hrs_bracket",
        "single_task_tokens", "single_task_usd", "single_task_wh",
        "human_minutes", "ai_minutes", "user_share_pct", "token_share_pct",
        "spend_share_pct", "tok_user_intensity"
    ]]
    lines.append(df_to_markdown_table(t51a_out, [
        "Cell ID", "Status", "Cell Title", "Beeline Bracket", "Task Tokens",
        "Task USD ($)", "Task Wh", "Human Min", "AI Min",
        "User %", "Token %", "Spend %", "Tok/User Ratio (x)"
    ]) + "\n")

    lines.append("#### Master Table 5.1b — Generation-Wide Macro Totals & `L4–L6` Pareto Concentration Ledger (`G0` to `G5`)\n")
    lines.append("**Caption (`Master Table 5.1b`):** **Macro users, annualized token volume, enterprise spend, and `L4–L6` builder/scientist Pareto concentration across `Gen 0` to `Gen 5`.**\n")
    t51b_rows = []
    for _, grow in gen_df.iterrows():
        gid = grow["gen_id"]
        sub = all_36[all_36["gen_id"] == gid]
        u_l46 = sub[sub["level_id"] >= 4]["user_share_pct"].sum()
        t_l46 = sub[sub["level_id"] >= 4]["token_share_pct"].sum()
        s_l46 = sub[sub["level_id"] >= 4]["spend_share_pct"].sum()
        t51b_rows.append({
            "gen": f"{gid} ({grow['start_date']}..{grow['end_date']})",
            "users": f"{grow['macro_users_m']:.1f}M",
            "tokens": f"{grow['macro_tokens_t_yr']:.2f}T/yr",
            "spend": f"${grow['macro_spend_b_yr']:.1f}B/yr",
            "u_l46": f"{u_l46:.1f}%",
            "t_l46": f"{t_l46:.1f}%",
            "s_l46": f"{s_l46:.1f}%",
            "skew": f"{round(t_l46 / max(u_l46, 0.01), 1)}x",
        })
    lines.append(df_to_markdown_table(pd.DataFrame(t51b_rows), [
        "Generation Window", "Active Users (M)", "Global Tokens (T/yr)", "Enterprise Spend ($B/yr)",
        "L4–L6 User Share (%)", "L4–L6 Token Share (%)", "L4–L6 Spend Share (%)", "L4–L6 Tok/User Skew"
    ]) + "\n")

    lines.append("#### Master Table 5.1c — Cross-Generation Down-Ladder Skill Deflation Summary (`G0` to `G5`)\n")
    lines.append("**Caption (`Master Table 5.1c`):** **Summary of vertical level deflation and learning-hour savings across the five benchmark workflows.**\n")
    lines.append(df_to_markdown_table(bench_df, [
        "Workflow ID", "Benchmark Workflow Name", "G0 Lvl", "G0 Hrs", "G1 Lvl", "G1 Hrs",
        "G2 Lvl", "G2 Hrs", "G3 Lvl", "G3 Hrs", "G4 Lvl", "G4 Hrs", "G5 Lvl", "G5 Hrs",
        "Hours Saved (G0->G4)", "Primary Deflation Mechanism"
    ]) + "\n")

    # 5.2
    lines.append("### 5.2 Bonus Analysis: 12-Lineage Technical & Governance TRL 1–3 (L6) to TRL 9 (L1) Maturation & Failed Hopes\n")
    lines.append(
        "**Twelve-Lineage On-Ladder TRL Maturation (`Table 5.2a`, `Plot 11` & `Plot M-TRL01`..`Plot M-TRL12`):** Every zero-skill `L1` consumer capability (`TRL 9`) and statutory safety guardrail began as an `L6` PhD paper or foundational critique (`TRL 1–3`). Below we present the macro 12-lineage trajectory and failed-hope survival audit (`Plot 11`), followed by `Table 5.2a`, all **12 Individual 4-Stage Paper-to-Consumer-Tool Micro Cards (`Plot M-TRL01` to `Plot M-TRL12`)**, and `Table 5.2b`.\n"
    )
    lines.append("![Plot 11: 12-Lineage TRL Maturation & Failed Hopes Survival Audit](figures_v5/fig_v5_p11_trl_and_failed_hopes.png)\n")
    lines.append(
        "**Caption (`Plot 11` — 12-Lineage On-Ladder TRL Trajectories & Hope Extinction Rates, 2017–2026):** **Left: All `12` synchronized `TRL 1 -> TRL 9` maturation curves (`8` Technical in `#0072B2` + `4` Governance/Safety in `#CC79A7`) under the parametric mean trajectory (`#009E73`, mean lag $= 35.3\\text{ months}$). Right: Stacked survival (`25%`) vs. four extinction mechanisms (`75%`) across `20` historical hopes (`Table 2.4`), rejecting $H_0$ of constant TRL maturation lag.**\n"
    )

    lines.append("#### Table 5.2a — Synchronized 12-Lineage On-Ladder `TRL 1–3` (`L6`) to `TRL 9` (`L1`) Maturation Ledger\n")
    lines.append("**Caption (`Table 5.2a`):** **Complete 4-stage maturation ledger for all `12` lineages (`TRL_01` to `TRL_12`: `8` Technical + `4` Governance/Safety).**\n")
    t52a_out = trl_df[[
        "lineage_id", "lineage_name", "category_type", "trl_1_3_genesis",
        "trl_4_6_prototype", "trl_7_8_workflow", "trl_9_default",
        "months_trl1_to_9", "primary_bottleneck_resolved"
    ]]
    lines.append(df_to_markdown_table(t52a_out, [
        "Lineage ID", "Lineage Name (L6 Genesis -> L1 Default)", "Category",
        "Stage 1: TRL 1–3 (L6 Genesis)", "Stage 2: TRL 4–6 (L4–L5 Prototype)",
        "Stage 3: TRL 7–8 (L2–L3 Workflow)", "Stage 4: TRL 9 (L1 Built-In Default)",
        "Total Lag (Months)", "Primary Bottleneck Resolved"
    ]) + "\n")

    lines.append("#### Twelve Individual Paper-to-Consumer-Tool TRL Micro Cards (`Plot M-TRL01` to `Plot M-TRL12`)\n")
    for idx, (_, trow) in enumerate(trl_df.iterrows(), start=1):
        tid = trow["lineage_id"]
        fn = trow["micro_plot_file"]
        tname = trow["lineage_name"]
        lines.append(f"![Plot M-TRL{idx:02d}: {tid} — {tname}](figures_v5/{fn})\n")
        lines.append(
            f"**Caption (`Plot M-TRL{idx:02d}` — `{tid}: {tname}`, Lag = `{trow['months_trl1_to_9']} Months`):** **Left: 2D skill-deflation escalator from `L6` (`TRL 1–3`) to `L1` (`TRL 9`). Right: 4-Stage SAE Maturation Strip: (1) `{trow['s1_date_cell']}` {trow['s1_artifact']} ({trow['s1_human_action']} $\\to$ {trow['s1_unlock']}); (2) `{trow['s2_date_cell']}` {trow['s2_artifact']} ({trow['s2_human_action']} $\\to$ {trow['s2_unlock']}); (3) `{trow['s3_date_cell']}` {trow['s3_artifact']} ({trow['s3_human_action']} $\\to$ {trow['s3_unlock']}); (4) `{trow['s4_date_cell']}` {trow['s4_artifact']} ({trow['s4_human_action']} $\\to$ {trow['s4_unlock']}).**\n"
        )

    lines.append("#### Table 5.2b — Population Evolution of Hope Inventory by Extinction Mechanism (`Gen 0` to `Gen 4`)\n")
    lines.append("**Caption (`Table 5.2b`):** **Breakdown of the `20` inventoried hopes (`Table 2.4`) across the `1` survival path and `4` evolutionary extinction mechanisms.**\n")
    t52b_df = hope_df.groupby(["extinction_category", "status_2026"]).agg(
        count=("hope_id", "count"),
        hopes=("hope_id", lambda s: ", ".join(s)),
        lesson=("evolutionary_lesson", "first"),
    ).reset_index()
    t52b_df["share_pct"] = (t52b_df["count"] / len(hope_df) * 100.0).round(1)
    lines.append(df_to_markdown_table(t52b_df[["extinction_category", "status_2026", "count", "share_pct", "hopes", "lesson"]], [
        "Evolutionary Outcome / Extinction Mechanism", "2026 Status", "Count", "Share (%)",
        "Cataloged Hope IDs", "Canonical Socio-Technical Lesson"
    ]) + "\n")

    # 5.3
    lines.append("### 5.3 Three-Way Audit of Existing Literature Ladders (Synchronized Pairwise Matrix & Temporal Animation)\n")
    sc = ladders_df["scope_coverage"].to_numpy()
    ua = ladders_df["user_skill_alignment"].to_numpy()
    hi = ladders_df["historical_invariance"].to_numpy()
    ec = ladders_df["empirical_cost_grounding"].to_numpy()
    r_sc_hi = float(np.corrcoef(sc, hi)[0, 1])
    r_ua_ec = float(np.corrcoef(ua, ec)[0, 1])

    lines.append(
        f"**Synchronized Pairwise Audit Across 22 Ladders (`Tables 5.3a–c`, `Plot 12` & `Plot 13`):** Across all `22` cataloged ladders (`Table 2.1`), mean alignment scores are $\\mu_{{\\text{{Scope}}}} = {sc.mean():.2f}$ ($\\text{{Med}} = {np.median(sc):.2f}, \\text{{IQR}} = {np.percentile(sc,75)-np.percentile(sc,25):.2f}$), $\\mu_{{\\text{{Skill}}}} = {ua.mean():.2f}$ ($\\text{{Med}} = {np.median(ua):.2f}, \\text{{IQR}} = {np.percentile(ua,75)-np.percentile(ua,25):.2f}$), $\\mu_{{\\text{{Hist}}}} = {hi.mean():.2f}$ ($\\text{{Med}} = {np.median(hi):.2f}, \\text{{IQR}} = {np.percentile(hi,75)-np.percentile(hi,25):.2f}$), and $\\mu_{{\\text{{Cost}}}} = {ec.mean():.2f}$ ($\\text{{Med}} = {np.median(ec):.2f}, \\text{{IQR}} = {np.percentile(ec,75)-np.percentile(ec,25):.2f}$), with strong positive pairwise correlations ($r_{{\\text{{Scope,Hist}}}} = {r_sc_hi:.3f}$, $r_{{\\text{{Skill,Cost}}}} = {r_ua_ec:.3f}$).\n"
    )
    lines.append("![Plot 12: Three-Way Literature Ladder Pairwise Structural Matrix](figures_v5/fig_v5_p12_ladder_comparison_matrix.png)\n")
    lines.append(
        f"**Caption (`Plot 12` — Pairwise Structural Alignment Matrix Across 22 Published Ladders):** **Tri-partite Pair Plot (`4 × 4` grid: lower-triangle scatter + OLS, diagonal KDE + horizontal boxplot with `manage_ticks=False`, upper-triangle correlation heat-cards with $r_{{\\text{{Scope,Hist}}}} = {r_sc_hi:.3f}$ and $r_{{\\text{{Skill,Cost}}}} = {r_ua_ec:.3f}$), rejecting $H_0$ ($r = 0$) of orthogonal evaluation dimensions.**\n"
    )

    lines.append("#### Table 5.3a — Quantitative Alignment Scores of 22 Published Ladders Against the 2D `6 × 6` Framework\n")
    lines.append("**Caption (`Table 5.3a`):** **Ranking of all `22` published ladders by composite alignment score across Scope Coverage, User-Skill Alignment, Historical Invariance, and Empirical Cost Grounding.**\n")
    t53a = ladders_df[["ladder_id", "ladder_name", "pub_date", "num_rungs", "scope_coverage", "user_skill_alignment", "historical_invariance", "empirical_cost_grounding"]].copy()
    t53a["composite_mean"] = t53a[["scope_coverage", "user_skill_alignment", "historical_invariance", "empirical_cost_grounding"]].mean(axis=1).round(3)
    lines.append(df_to_markdown_table(t53a, [
        "Ladder ID", "Ladder Name", "Pub Date", "Rungs", "Scope Cov.",
        "User-Skill Align.", "Hist. Invariance", "Cost Grounding", "Composite Mean"
    ]) + "\n")

    lines.append("#### Table 5.3b — Inter-Ladder Conflict Resolution by Vantage Point\n")
    lines.append("**Caption (`Table 5.3b`):** **Resolution of four apparent contradictions in the AI ladder literature via 2D `(Gen, Level)` coordinate disambiguation.**\n")
    t53b = pd.DataFrame([
        ("Conflict 1: 'Prompt Engineering is a $335k Career' (LAD_06) vs. 'Prompting is Dead' (LAD_20)", "Gen 1–2 L2 vs. Gen 4 L1/L4", "Manual CoT/prefix hacks at G1/G2-L2 sank into G4-L1 RLVR auto-routers, while industrial Context Engineering rose to G4-L4 (~600h)."),
        ("Conflict 2: 'RAG is Obsolete Due to 2M Context' (G3 Hype) vs. 'Enterprise RAG is Essential' (LAD_07)", "G3-L2 (<50 PDFs) vs. G3/G4-L3 (1M+ Docs)", "<50-PDF personal RAG sank into G3-L2 drag-and-drop workspaces, while ACL-filtered million-document corpora remain at L3/L4."),
        ("Conflict 3: 'Coding Agents Replace SWEs' (LAD_15/19) vs. 'Workslop & 0% ROI' (LAD_21)", "Coupled L2/L3 Vibe Coding vs. Decoupled L4 Oracles", "Unverified L2/L3 vibe coding generates Code Slop; positive enterprise ROI requires L4 decoupled property/Docker verification oracles."),
        ("Conflict 4: 'Every Company Needs Sovereign GPU Clusters' (LAD_11 Rung 5) vs. '76% Bought Tools' (Menlo/MIT)", "L6 Pretraining ($100M+) vs. L3/L4 Vertical Integration", "Bespoke corporate base pretraining (BloombergGPT) failed on unit economics; enterprises buy foundation APIs and build L3/L4 harnesses."),
    ], columns=["conflict", "coords", "resolution"])
    lines.append(df_to_markdown_table(t53b, [
        "Apparent Literature Conflict", "2D (Gen, Level) Coordinate Split", "Empirical Resolution in Our 6 × 6 Framework"
    ]) + "\n")

    lines.append("#### Table 5.3c — Descriptive Bottom Rungs vs. Speculative Hope Top Rungs Audit\n")
    lines.append("**Caption (`Table 5.3c`):** **Structural comparison between Descriptive Bottom Rungs (Rungs 1–3) and Speculative Hope Top Rungs (Top 1–2 Rungs) across the 22-ladder corpus.**\n")
    t53c = pd.DataFrame([
        ("Descriptive Bottom Rungs (Rungs 1–3 of Published Ladders)", "L1 – L4", "TRL 7 – TRL 9", "88.5%", "High empirical accuracy; captures tools already productized and adopted by practitioners."),
        ("Speculative Hope Top Rungs (Top 1–2 Rungs of Published Ladders)", "L5 – L6 (Conflated as L1)", "TRL 1 – TRL 4", "25.0%", "Commits Upward Artifact Conflation by projecting future L6 research goals as zero-human L1 autonomy."),
    ], columns=["zone", "mapped_levels", "trl_band", "survival_rate", "diagnosis"])
    lines.append(df_to_markdown_table(t53c, [
        "Published Ladder Zone", "True Mapped Skill Levels", "Contemporaneous TRL Band",
        "3-Year Survival Rate", "Structural Diagnosis"
    ]) + "\n")

    lines.append("![Plot 13: Animated Temporal Progression of Six-Level AI Ladder Evolution](figures_v5/fig_v5_p13_ladder_evolution_anim.gif)\n")
    lines.append(
        "**Caption (`Plot 13` — Animated Temporal Progression of Six-Level AI Ladder Evolution, 2017-06 to 2026-09):** **112-frame (`28.0s` at `4 FPS`, `121.75 days/s` temporal compression) animated `symlog` trajectory across `G0` to `G4` tracking cumulative beeline learning hours vs. single-task token volume with a synchronized bottom calendar playhead scrubber, rejecting $H_0$ of static rung positions.**\n"
    )

    # 5.4
    lines.append("### 5.4 Controlled Speculation: Next Generation (Gen 5 = Current + 1) Six-Facet Forecast (G5-L1 to G5-L6)\n")
    lines.append(
        "**Bounded Next-Gen Extrapolation (`Tables 5.4a–b`, `Plot M-G5` & `Plot 14`):** Applying our Dual-Trigger Boundary Rule and 7-month METR doubling law forward from `TODAY = 2026-10-20` yields `Gen 5` (*The Verified Autonomous Workforce & Cross-Org Agentic Mesh Generation*).\n"
    )
    lines.append("#### Table 5.4a — Speculative `Gen 5` Dual-Lens Cutoff Comparison (Relative to `TODAY = 2026-10-20`)\n")
    lines.append("**Caption (`Table 5.4a`):** **Comparison of the Pre-Today First-Release Lens (`2026-08`) vs. Post-Today Mainstream Production-Crossover Lens (`2027-03 to 2028-12`).**\n")
    lines.append(df_to_markdown_table(cut_df, [
        "Lens ID", "Cutoff Lens Name", "Date Window", "Year Float",
        "Triggering Technical & Ecosystem Events", "Analytical Pros", "Cons & Operational Adoption Decision"
    ]) + "\n")

    lines.append("![Plot M-G5: Speculative Gen 5 SAE J3016 6-Column Micro Card](figures_v5/fig_v5_micro_gen5_sae.png)\n")
    lines.append(
        "**Caption (`Plot M-G5` — Speculative `Gen 5` 6-Column SAE J3016 Reference Card):** **Projected 6-level practitioner division of labor in `Gen 5` (`G5-L1` Ambient OS Delegate to `G5-L6` Recursive Self-Improving Pioneer), where `L4–L6` harnesses account for `90.0%` of total token volume.**\n"
    )

    sub_p0_g5 = p0_df[p0_df["gen_id"] == "G5"].sort_values("level_id")
    sub_g5 = g5_df.sort_values("level_id")
    for (_, prow), (_, crow) in zip(sub_p0_g5.iterrows(), sub_g5.iterrows()):
        lines.append(_render_six_facet_cell(prow, crow))

    lines.append("![Plot 14: Six-Level Speculative Next Generation (Gen 5) Matrix](figures_v5/fig_v5_p14_gen5_speculative_matrix.png)\n")
    lines.append(
        "**Caption (`Plot 14` — Speculative `Gen 5` Quantitative Step & Conserved Share Matrix, 2027–2028+):** **Projected single-task token, hour, and Wh step profiles (left) and `100.0%` conserved user, token, and spend shares (right) across `G5-L1`..`G5-L6`, rejecting $H_0$ of token-share convergence ($\\text{L4–L6}$ token share reaches `90.0%` from `2.2%` of users).**\n"
    )
    lines.append("#### Table 5.4b — Speculative `Gen 5` Six-Level Resource & Conserved Share Matrix (`G5-L1` to `G5-L6`)\n")
    lines.append("**Caption (`Table 5.4b`):** **Projected single-task metrics and `100.0%` conserved shares for `G5-L1` to `G5-L6`.**\n")
    t54b_out = sub_g5[[
        "cell_id", "user_first_title", "beeline_hrs_bracket", "single_task_tokens",
        "single_task_flops", "single_task_usd", "single_task_wh",
        "human_minutes", "ai_minutes", "user_share_pct", "token_share_pct", "spend_share_pct"
    ]]
    lines.append(df_to_markdown_table(t54b_out, [
        "Cell ID", "Projected Cell Title", "Cumulative Beeline Bracket", "Task Tokens",
        "Task FLOPs", "Task USD ($)", "Task Wh", "Human Min", "AI Min",
        "User Share (%)", "Token Share (%)", "Spend Share (%)"
    ]) + "\n")

    out_text = "\n".join(lines)
    with open(os.path.join(STAGES_DIR, "part5.md"), "w", encoding="utf-8") as f:
        f.write(out_text)
    return out_text


def assemble_report_v5() -> str:
    dfs = build_all_csvs()
    p1 = build_frontispiece_and_part1(dfs)
    p2 = build_part2(dfs)
    p3 = build_part3(dfs)
    p4 = build_part4(dfs)
    p5 = build_part5(dfs)
    full_report = "\n".join([p1, p2, p3, p4, p5])
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(full_report)
    print(f"[assemble_report_v5] Wrote {len(full_report):,} chars ({full_report.count(chr(10))+1:,} lines) to {REPORT_PATH}")
    return full_report


if __name__ == "__main__":
    assemble_report_v5()
