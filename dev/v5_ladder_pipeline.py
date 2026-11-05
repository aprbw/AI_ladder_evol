# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # AI Ladder Evolution (v5): Dual-Megachart 6×6 Data Cache, 8 Validation Gates & 44-Figure CITRA Visual Atlas Verification
#
# This notebook executes the complete verification and visualization pipeline mandated by `/Users/z3540725/My Drive/personal/2026 10 17 AI_ladder_evol/2026 10 17 AI_ladder_evol mp5.md`:
# 1. **Cache-First Provenance Check**: Loads or compiles all 16 verified Single-Source-of-Truth (SSOT) CSV datasets inside `cache_v5/` (covering `Gen 0` to `Gen 4`, Speculative `Gen 5`, 6 Levels `L1`–`L6`, 22 Existing Ladders, 125 Chronological Glossary Entries across 8 Domains `D1`–`D8`, 26 Beeline Curricula/Papers, 36 Track A/B Use Cases, 20 Historical Hopes, 12 Synchronized TRL Lineages `TRL_01`–`TRL_12`, 144 Dated Historical Milestones across `CAT 1`–`CAT 6`, 36 Skill Poster Cells, and 36 News Megachart Cells).
# 2. **Programmatic Validation Gates (`Gate 1`–`Gate 8`)**: Asserts zero nulls, mathematical bounds, monotonic 6-level beeline learning hours and hardware capital (`L1 < L2 < L3 < L4 < L5 < L6`), `100.0%` generation share conservation across `G0`–`G5`, $H_0$ skill deflation across all 5 benchmark workflows, zero forbidden min–max range strings (`7–45h`, `50–200h`, `200–600h`, `600–2,000h`), proper-subset keyword hierarchy (`micro_keywords_subset ⊂ mini_keywords_subset ⊂ keywords_1line`), 125-term chronological glossary coverage (`>= 8` terms per domain `D1..D8`), 144 dated events (`4` per News cell), 12 TRL lineages (`8` Technical + `4` Governance/Safety), and full ground-up report synchronization (`2026 10 17 AI_ladder_evol report v5.md`).
# 3. **CITRA Visual Atlas Verification (`44` Figures in `figures_v5/`)**: Verifies all 44 publication-grade visual artifacts (`3` User-Skill Megacharts, `3` Historical News Megacharts, `6` Per-Generation SAE J3016 Cards, `12` Per-TRL-Lineage Cards, `6` Visual Abstracts `VA0`–`VA5`, and `14` Analytical Plots + Animation `Plot 1`–`Plot 14`, including `fig_v5_p13_ladder_evolution_anim.gif`).

# %%
import os
import sys

VENV_SITE = "/Users/z3540725/My Drive/personal/2026 10 17 AI_ladder_evol/.venv/lib/python3.14/site-packages"
if VENV_SITE not in sys.path:
    sys.path.insert(0, VENV_SITE)

from v5_data_and_gates import (
    build_all_csvs,
    run_all_gates,
    CACHE_DIR,
    FIGURES_DIR as FIG_DIR,
    EXPECTED_44_FIGURES,
    REPORT_PATH,
)
from v5_render_plots import render_all_plots

# %% [markdown]
# ## 1. Compile SSOT Data Cache (`cache_v5/*.csv`) & Inspect Dataset Shapes

# %%
dfs = build_all_csvs()
for key, df in dfs.items():
    print(f"Dataset [{key}]: rows={len(df)}, cols={len(df.columns)}")

# %% [markdown]
# ## 2. Render (if needed) & Verify All 44 Visual Artifacts in `figures_v5/` and Execute Gates 1–8

# %%
if not all(os.path.exists(os.path.join(FIG_DIR, f)) for f in EXPECTED_44_FIGURES):
    render_all_plots()

for fname in EXPECTED_44_FIGURES:
    fpath = os.path.join(FIG_DIR, fname)
    assert os.path.exists(fpath) and os.path.getsize(fpath) > 1024, f"Missing or empty figure: {fpath}"
    print(f"[VERIFIED FIGURE] {fname} ({os.path.getsize(fpath) / 1024:.1f} KB)")

run_all_gates(check_figures=True, check_report=True)
print(f"\n[SUCCESS] Report verified: {os.path.basename(REPORT_PATH)} ({os.path.getsize(REPORT_PATH):,} bytes)")
print("[SUCCESS] All 16 v5 SSOT CSV caches, 8 programmatic assert gates, and 44 visual artifacts verified!")

