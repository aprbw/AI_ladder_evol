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
# # AI Ladder Evolution (v3): Data Cache, Validation Gates & CITRA Visual Atlas Verification
#
# This notebook executes the complete verification and visualization pipeline mandated by `/Users/z3540725/My Drive/personal/2026 10 17 AI_ladder_evol/2026 10 17 AI_ladder_evol mp3.md`:
# 1. **Cache-First Provenance Check**: Loads or builds all 13 verified CSV datasets inside `cache_v3/` (covering `Gen 0` to `Gen 4`, Speculative `Gen 5`, 36 Generational-Defining Events, and 30 Encyclopedic Poster Cells).
# 2. **Programmatic Validation Gates (Section 1.4)**: Asserts zero nulls, mathematical bounds, monotonic level learning hours (`L1 < L2 < L3 < L4 < L5`), `100.0%` generation share conservation across `G0`–`G5`, and $H_0$ skill deflation across all 5 benchmark workflows.
# 3. **CITRA Visual Atlas Generation (Section 1.5)**: Renders all 21 publication-grade visual artifacts (`Plot 0` Encyclopedic Broadside Wallchart, `Plot VA0`–`Plot VA5`, and `Plot 1`–`Plot 14`, including `fig_v3_p11_ladder_evolution_anim.gif`) inside `figures_v3/` and verifies their existence and non-zero byte sizes.

# %%
import os
import sys

VENV_SITE = "/Users/z3540725/My Drive/personal/2026 10 17 AI_ladder_evol/.venv/lib/python3.14/site-packages"
if VENV_SITE not in sys.path:
    sys.path.insert(0, VENV_SITE)

from v3_data_and_gates import build_and_verify_all, CACHE_DIR
from v3_render_plots import render_all_plots, FIG_DIR

# %% [markdown]
# ## 1. Execute Data Pipeline & Programmatic Validation Gates

# %%
data_bundle = build_and_verify_all()
for key, df in data_bundle.items():
    print(f"Dataset [{key}]: rows={len(df)}, cols={len(df.columns)}")

# %% [markdown]
# ## 2. Render & Verify All 21 Visual Artifacts (`Plot 0`, `Plot VA0`–`VA5`, `Plot 1`–`Plot 14`)

# %%
render_all_plots()

expected_figures = [
    "fig_v3_p0_encyclopedic_megachart_poster.png",
    "fig_v3_va0_root.png",
    "fig_v3_va1_part1.png",
    "fig_v3_va2_part2.png",
    "fig_v3_va3_part3.png",
    "fig_v3_va4_part4.png",
    "fig_v3_va5_part5.png",
    "fig_v3_p1_macro_resource_trajectories.png",
    "fig_v3_p2_skill_deflation_escalator.png",
    "fig_v3_p3_folksonomy_and_gen_breaks.png",
    "fig_v3_p4_task_cost_vs_learning_jointplot.png",
    "fig_v3_p5_gen0_matrix.png",
    "fig_v3_p6_gen1_matrix.png",
    "fig_v3_p7_gen2_matrix.png",
    "fig_v3_p8_gen3_matrix.png",
    "fig_v3_p9_gen4_matrix.png",
    "fig_v3_p9_genM_matrix.png",
    "fig_v3_p10_alluvial_evolution_poster.png",
    "fig_v3_p11_ladder_evolution_anim.gif",
    "fig_v3_p12_trl_and_failed_hopes.png",
    "fig_v3_p13_ladder_comparison_matrix.png",
    "fig_v3_p14_gen5_speculative_matrix.png",
]

for fname in expected_figures:
    fpath = os.path.join(FIG_DIR, fname)
    assert os.path.exists(fpath) and os.path.getsize(fpath) > 1024, f"Missing or empty figure: {fpath}"
    print(f"[VERIFIED FIGURE] {fname} ({os.path.getsize(fpath) / 1024:.1f} KB)")

print("\n[SUCCESS] All v3 data caches, programmatic assert gates, and 21 visual artifacts verified!")


