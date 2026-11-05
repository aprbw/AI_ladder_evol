#!/usr/bin/env python3
"""
v5_data_and_gates.py
====================
Single-Source-of-Truth (SSOT) data compiler and 8-Gate Deterministic Validator for
`2026 10 17 AI_ladder_evol mp5.md` (v5).
"""

import os
import re
import sys
import pandas as pd

from stages_v5.data_part2 import (
    LEVEL_BRACKET_STRS,
    COMPACT_TICK_LABELS,
    LADDERS_DATA,
    LEVELS_DATA,
    USE_CASES_DATA,
    COURSES_BLOGS_DATA,
    GLOSSARY_DATA,
    GLOSSARY_DOMAIN_SUMMARY,
    HOPES_DATA,
    PRICING_HW_DATA,
    TRL_DATA,
    GENERATIONS_DATA,
    BENCHMARKS_DATA,
    RELATIONAL_INVARIANTS_DATA,
    GEN5_CUTOFFS_DATA,
)
from stages_v5.data_cells import build_skill_cells_dataframes
from stages_v5.data_news_cells import build_news_cells_dataframes

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(BASE_DIR, "cache_v5")
FIGURES_DIR = os.path.join(BASE_DIR, "figures_v5")
REPORT_PATH = os.path.join(BASE_DIR, "2026 10 17 AI_ladder_evol report v5.md")


def build_all_csvs() -> dict[str, pd.DataFrame]:
    """Compile and save all SSOT CSV datasets in cache_v5/."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    dfs = {}

    # 1. Existing Ladders (Table 2.1)
    ladders_cols = [
        "ladder_id", "ladder_name", "authors_org", "pub_date", "num_rungs",
        "extracted_folksonomy_keywords", "descriptive_bottom_rungs", "speculative_hope_top_rungs",
        "implied_generation_breaks", "scope_coverage", "user_skill_alignment",
        "historical_invariance", "empirical_cost_grounding",
    ]
    dfs["existing_ladders"] = pd.DataFrame(LADDERS_DATA, columns=ladders_cols)
    dfs["existing_ladders"].to_csv(os.path.join(CACHE_DIR, "v5_existing_ladders.csv"), index=False)

    # 2. Level Brackets (Table 1.2 & Table 3.2)
    levels_cols = [
        "level_id", "level_name", "beeline_bracket", "compact_tick_label",
        "learning_hours_max", "hardware_cap_usd", "cognitive_tier",
        "primary_surface_hw", "track_a_using_persona", "track_b_making_persona",
        "using_vs_making_split", "mean_single_task_tokens", "mean_single_task_usd",
    ]
    dfs["level_brackets"] = pd.DataFrame(LEVELS_DATA, columns=levels_cols)
    dfs["level_brackets"].to_csv(os.path.join(CACHE_DIR, "v5_level_brackets.csv"), index=False)

    # 3. Use Cases (Table 2.2)
    uc_cols = [
        "use_case_id", "use_case_name", "track_split", "first_viable_date",
        "mainstream_date", "primary_surface_hw", "sinking_trajectory",
    ]
    dfs["use_cases"] = pd.DataFrame(USE_CASES_DATA, columns=uc_cols)
    dfs["use_cases"].to_csv(os.path.join(CACHE_DIR, "v5_use_cases.csv"), index=False)

    # 4. Courses & Blogs (Table 2.3a)
    tut_cols = [
        "course_id", "title_author_venue", "release_date", "extracted_keywords",
        "beeline_hours", "required_surface_hw", "mapped_level_bracket",
    ]
    dfs["courses_blogs"] = pd.DataFrame(COURSES_BLOGS_DATA, columns=tut_cols)
    dfs["courses_blogs"].to_csv(os.path.join(CACHE_DIR, "v5_courses_blogs.csv"), index=False)

    # 5. Chronological Glossary & Etymology (Table 2.3b & Table 2.3c)
    gloss_cols = [
        "term_id", "coinage_date", "term_keyword", "domain_id", "domain_name",
        "coined_by_source", "concise_definition", "cognitive_tier",
        "origin_cell", "absorbed_cell",
    ]
    dfs["glossary_etymology"] = pd.DataFrame(GLOSSARY_DATA, columns=gloss_cols)
    dfs["glossary_etymology"].to_csv(os.path.join(CACHE_DIR, "v5_glossary_etymology.csv"), index=False)

    dom_cols = [
        "domain_id", "domain_name", "term_count", "representative_terms",
        "origin_rungs", "sunk_rungs", "structural_role",
    ]
    dfs["glossary_domain_summary"] = pd.DataFrame(GLOSSARY_DOMAIN_SUMMARY, columns=dom_cols)
    dfs["glossary_domain_summary"].to_csv(os.path.join(CACHE_DIR, "v5_glossary_domain_summary.csv"), index=False)

    # 6. Hope Inventory (Table 2.4 & Table 5.2b)
    hope_cols = [
        "hope_id", "promised_capability", "origin_gen", "target_gen", "proponents",
        "technical_mechanism", "status_2026", "extinction_category",
        "outcome_explanation", "evolutionary_lesson",
    ]
    dfs["hope_inventory"] = pd.DataFrame(HOPES_DATA, columns=hope_cols)
    dfs["hope_inventory"].to_csv(os.path.join(CACHE_DIR, "v5_hope_inventory.csv"), index=False)

    # 7. Pricing & Hardware Baseline (Table 2.5)
    price_cols = [
        "model_id", "model_hw_name", "release_date", "gen_id",
        "input_usd_per_1m", "output_usd_per_1m", "context_window",
        "training_flops_or_vram", "single_task_wh", "step_change_capability",
    ]
    dfs["pricing_hardware_baseline"] = pd.DataFrame(PRICING_HW_DATA, columns=price_cols)
    dfs["pricing_hardware_baseline"].to_csv(os.path.join(CACHE_DIR, "v5_pricing_hardware_baseline.csv"), index=False)

    # 8. Synchronized 12-Lineage TRL Trajectories (Table 5.2a)
    trl_cols = [
        "lineage_id", "micro_plot_file", "lineage_name", "category_type",
        "trl_1_3_genesis", "trl_4_6_prototype", "trl_7_8_workflow", "trl_9_default",
        "months_trl1_to_9", "primary_bottleneck_resolved",
        "s1_date_cell", "s1_artifact", "s1_human_action", "s1_unlock",
        "s2_date_cell", "s2_artifact", "s2_human_action", "s2_unlock",
        "s3_date_cell", "s3_artifact", "s3_human_action", "s3_unlock",
        "s4_date_cell", "s4_artifact", "s4_human_action", "s4_unlock",
    ]
    dfs["trl_trajectories"] = pd.DataFrame(TRL_DATA, columns=trl_cols)
    dfs["trl_trajectories"].to_csv(os.path.join(CACHE_DIR, "v5_trl_trajectories.csv"), index=False)

    # 9. Generations, Benchmarks, Relational Invariants, Gen 5 Cutoffs
    gen_cols = [
        "gen_id", "gen_name", "start_date", "end_date", "duration_months",
        "start_year_float", "end_year_float", "new_upper_use_cases",
        "sunk_lower_use_cases", "six_factor_causal_drivers", "obsolete_user_skills",
        "macro_users_m", "macro_tokens_t_yr", "macro_spend_b_yr",
    ]
    dfs["generations"] = pd.DataFrame(GENERATIONS_DATA, columns=gen_cols)
    dfs["generations"].to_csv(os.path.join(CACHE_DIR, "v5_generations.csv"), index=False)

    bench_cols = [
        "workflow_id", "workflow_name",
        "g0_lvl", "g0_hrs", "g1_lvl", "g1_hrs", "g2_lvl", "g2_hrs",
        "g3_lvl", "g3_hrs", "g4_lvl", "g4_hrs", "g5_lvl", "g5_hrs",
        "total_hrs_saved", "deflation_mechanism",
    ]
    dfs["benchmarks"] = pd.DataFrame(BENCHMARKS_DATA, columns=bench_cols)
    dfs["benchmarks"].to_csv(os.path.join(CACHE_DIR, "v5_benchmarks.csv"), index=False)

    inv_cols = ["invariant_id", "invariant_name", "formal_rule"]
    dfs["relational_invariants"] = pd.DataFrame(RELATIONAL_INVARIANTS_DATA, columns=inv_cols)
    dfs["relational_invariants"].to_csv(os.path.join(CACHE_DIR, "v5_relational_invariants.csv"), index=False)

    cut_cols = ["lens_id", "lens_name", "cutoff_window", "year_float", "trigger_events", "pros", "cons_adoption_decision"]
    dfs["gen5_cutoffs"] = pd.DataFrame(GEN5_CUTOFFS_DATA, columns=cut_cols)
    dfs["gen5_cutoffs"].to_csv(os.path.join(CACHE_DIR, "v5_gen5_cutoffs.csv"), index=False)

    # 10. Skill Cells: v5_ladder_cells.csv (30 rows), v5_gen5_speculative.csv (6 rows), v5_poster_encyclopedic_cells.csv (36 rows)
    df_emp, df_gen5, df_poster = build_skill_cells_dataframes()
    dfs["ladder_cells"] = df_emp
    dfs["ladder_cells"].to_csv(os.path.join(CACHE_DIR, "v5_ladder_cells.csv"), index=False)

    dfs["gen5_speculative"] = df_gen5
    dfs["gen5_speculative"].to_csv(os.path.join(CACHE_DIR, "v5_gen5_speculative.csv"), index=False)

    dfs["poster_encyclopedic_cells"] = df_poster
    dfs["poster_encyclopedic_cells"].to_csv(os.path.join(CACHE_DIR, "v5_poster_encyclopedic_cells.csv"), index=False)

    # 11. News Cells: v5_defining_events.csv (144 rows), v5_news_megachart_cells.csv (36 rows)
    events_rows, news_cells_rows = build_news_cells_dataframes()
    dfs["defining_events"] = pd.DataFrame(events_rows)
    dfs["defining_events"].to_csv(os.path.join(CACHE_DIR, "v5_defining_events.csv"), index=False)

    dfs["news_megachart_cells"] = pd.DataFrame(news_cells_rows)
    dfs["news_megachart_cells"].to_csv(os.path.join(CACHE_DIR, "v5_news_megachart_cells.csv"), index=False)

    return dfs


# =============================================================================
# DETERMINISTIC VALIDATION GATES (GATES 1-8)
# =============================================================================

MANDATORY_GLOSSARY_SUBSTRINGS = [
    # D1 Paradigm Coinages, Meta-Laws & Doomer/x-risk Theory
    "Software 2.0", "Bitter Lesson", "Jevons Paradox", "Moravec's Paradox",
    "Stochastic Parrots", "Foundation Models", "Shoggoth", "Waluigi",
    "Jagged Frontier", "Centaur", "Compound AI", "Agentic Workflows",
    "Vibe Coding", "Context Engineering", "Paperclip", "Instrumental Convergence",
    "Orthogonality", "Treacherous Turn", "p(doom)", "e/acc", "FOOM",
    # D2 Failure Modes, Pathologies, Deceptive Alignment, Psychosis & Slop
    "Hallucination", "Catastrophic Forgetting", "Goodhart's Law", "Reward Hacking",
    "ELIZA Effect", "Sycophancy", "Model Collapse", "Dead Internet",
    "Lost in the Middle", "Context Rot", "AI Slop", "Code Slop", "Workslop",
    "Enshittification", "Mesa-Optimization", "Alignment Faking", "Psychosis",
    # D3 Adversarial Security, Catastrophic ASL/RSP, Data Wall & Governance
    "Prompt Injection", "Jailbreaking", "Shadow AI", "Glaze", "Nightshade",
    "SynthID", "C2PA", "Sleeper Agents", "Data Wall", "Pay-Per-Crawl",
    "Guardrails", "Instruction Hierarchy", "Superalignment", "ASL", "EU AI Act",
    # D4 Prompting Folksonomy, Multimodal & Workspace
    "Few-Shot", "Prompt Engineering", "Chain-of-Thought", "Take a Deep Breath",
    "EmotionPrompt", "Sora", "Veo", "Flux", "ElevenLabs", "NotebookLM",
    "Prompt", "Caching", "Artifacts", "Canvas", "Deep Research",
    # D5 Vibe-Coding Builders, Agentic Harnesses, Protocols & Evals
    "RAG", "ReAct", "Function Calling", "Structured Outputs", "v0", "Bolt.new",
    "Lovable", "Cursor", "Windsurf", "Aider", "Cline", "OpenHands",
    "Claude Code CLI", "Model Context Protocol", "A2A", "OpenClaw",
    "Chatbot Arena", "ARC-AGI", "GAIA", "SWE-bench", "LangGraph", "GraphRAG",
    # D6 Local Inference, Quantization & Open Fine-Tuning Stack
    "LoRA", "QLoRA", "llama.cpp", "GGUF", "Ollama", "LM Studio", "MLX",
    "Unsloth", "BitNet",
    # D7 Frontier Architectures, Test-Time Compute, Corpora & AI4Science
    "Transformer", "BERT", "Mixture of Experts", "GQA", "MLA", "Constitutional AI",
    "Speculative Decoding", "Test-Time Compute", "DPO", "RLVR", "GRPO",
    "Phi", "FineWeb", "The Pile", "LAION-5B", "AlphaFold", "AlphaEvolve",
    "FlashAttention", "PagedAttention", "Mamba",
    # D8 Silicon, Cluster Networking & Gigawatt Nuclear Energy
    "CUDA Moat", "NVLink", "InfiniBand", "DeepSpeed ZeRO", "TPU",
    "Groq LPU", "Cerebras", "Three Mile Island",
]


def run_gate_1(dfs: dict[str, pd.DataFrame]) -> dict:
    """Gate 1: Chronological Keyword & Etymology Inventory Completeness."""
    df = dfs["glossary_etymology"]
    assert len(df) >= 85, f"Gate 1 Failed: Expected >= 85 glossary terms, got {len(df)}"
    dates = df["coinage_date"].tolist()
    assert dates == sorted(dates), "Gate 1 Failed: coinage_date is not strictly sorted ascending YYYY-MM!"
    for d in dates:
        assert re.match(r"^\d{4}-\d{2}$", str(d)), f"Gate 1 Failed: Invalid YYYY-MM date {d}"

    domain_counts = df["domain_id"].value_counts().to_dict()
    for dom in [f"D{i}" for i in range(1, 9)]:
        cnt = domain_counts.get(dom, 0)
        assert cnt >= 8, f"Gate 1 Failed: Domain {dom} has {cnt} < 8 terms!"

    all_terms_blob = " || ".join(
        (df["term_keyword"].astype(str) + " " + df["coined_by_source"].astype(str) + " " + df["concise_definition"].astype(str)).tolist()
    ).lower()
    missing = [s for s in MANDATORY_GLOSSARY_SUBSTRINGS if s.lower() not in all_terms_blob]
    assert not missing, f"Gate 1 Failed: Missing mandatory glossary substrings: {missing}"

    return {
        "gate": "Gate 1",
        "total_terms": len(df),
        "domain_counts": domain_counts,
        "chronological_sorted": True,
        "mandatory_substrings_verified": len(MANDATORY_GLOSSARY_SUBSTRINGS),
    }


def run_gate_2(dfs: dict[str, pd.DataFrame]) -> dict:
    """Gate 2: Six-Category Historical News Megachart Completeness."""
    ev_df = dfs["defining_events"]
    nc_df = dfs["news_megachart_cells"]
    assert len(nc_df) == 36, f"Gate 2 Failed: Expected 36 news cells, got {len(nc_df)}"
    assert len(ev_df) >= 144, f"Gate 2 Failed: Expected >= 144 defining events, got {len(ev_df)}"

    cell_counts = ev_df.groupby(["gen_id", "cat_idx"]).size().to_dict()
    for g in ["G0", "G1", "G2", "G3", "G4", "G5"]:
        for c in range(1, 7):
            cnt = cell_counts.get((g, c), 0)
            assert cnt >= 4, f"Gate 2 Failed: Cell ({g}, C{c}) has {cnt} < 4 events!"

    for _, row in ev_df.iterrows():
        assert re.match(r"^\d{4}-\d{2}$", str(row["event_date"])), f"Invalid event_date {row['event_date']}"
        assert str(row["impact_summary"]).startswith(f"[{row['event_date']}]"), (
            f"Event {row['event_id']} summary does not start with [{row['event_date']}]"
        )

    return {
        "gate": "Gate 2",
        "news_cells": len(nc_df),
        "defining_events": len(ev_df),
        "min_events_per_cell": min(cell_counts.values()),
    }


def run_gate_3(dfs: dict[str, pd.DataFrame]) -> dict:
    """Gate 3: Synchronized 12-Lineage TRL 1-9 Trajectory Completeness."""
    trl_df = dfs["trl_trajectories"]
    assert len(trl_df) == 12, f"Gate 3 Failed: Expected 12 TRL lineages, got {len(trl_df)}"
    tech_cnt = (trl_df["category_type"] == "Technical").sum()
    gov_cnt = (trl_df["category_type"].isin(["Governance/Safety", "Socio-Technical Governance"])).sum()
    assert tech_cnt == 8 and gov_cnt == 4, f"Gate 3 Failed: Expected 8 Technical + 4 Governance, got {tech_cnt}/{gov_cnt}"

    required_cols = [
        "s1_date_cell", "s1_artifact", "s1_human_action", "s1_unlock",
        "s2_date_cell", "s2_artifact", "s2_human_action", "s2_unlock",
        "s3_date_cell", "s3_artifact", "s3_human_action", "s3_unlock",
        "s4_date_cell", "s4_artifact", "s4_human_action", "s4_unlock",
    ]
    for col in required_cols:
        assert col in trl_df.columns, f"Gate 3 Failed: Missing column {col}"
        assert trl_df[col].notna().all() and (trl_df[col].astype(str).str.len() > 0).all(), (
            f"Gate 3 Failed: Empty values in {col}"
        )

    return {
        "gate": "Gate 3",
        "total_lineages": len(trl_df),
        "technical_lineages": int(tech_cnt),
        "governance_lineages": int(gov_cnt),
    }


def run_gate_4(dfs: dict[str, pd.DataFrame]) -> dict:
    """Gate 4: Top-to-Bottom Subcell Non-Redundancy & Character-Budget Audit."""
    p0_df = dfs["poster_encyclopedic_cells"]
    p0b_df = dfs["news_megachart_cells"]
    assert len(p0_df) == 36, f"Expected 36 skill cells, got {len(p0_df)}"
    assert len(p0b_df) == 36, f"Expected 36 news cells, got {len(p0b_df)}"

    p0_subcols = ["sub_summary", "sub_use_cases", "sub_actions", "sub_models", "sub_surface", "sub_scope"]
    for _, row in p0_df.iterrows():
        cid = row["cell_id"]
        plen = len(str(row["plain_desc"]))
        assert 80 <= plen <= 105, f"Gate 4 Failed: {cid} plain_desc len {plen} not in [80, 105]"
        for sc in p0_subcols:
            slen = len(str(row[sc]))
            assert 170 <= slen <= 200, f"Gate 4 Failed: {cid} {sc} len {slen} not in [170, 200]"

    for g in ["G0", "G1", "G2", "G3", "G4", "G5"]:
        sub = p0_df[p0_df["gen_id"] == g]
        assert sub["sub_models"].nunique() == 6, f"Gate 4 Failed: Duplicate sub_models in {g}"
        assert sub["sub_surface"].nunique() == 6, f"Gate 4 Failed: Duplicate sub_surface in {g}"

    p0b_subcols = ["sub_ev1", "sub_ev2", "sub_ev3", "sub_ev4", "sub_ladder_impact", "sub_trl_cascade"]
    for _, row in p0b_df.iterrows():
        cid = row["cell_id"]
        plen = len(str(row["plain_desc"]))
        assert 80 <= plen <= 105, f"Gate 4 Failed: {cid} plain_desc len {plen} not in [80, 105]"
        for sc in p0b_subcols:
            slen = len(str(row[sc]))
            assert 170 <= slen <= 200, f"Gate 4 Failed: {cid} {sc} len {slen} not in [170, 200]"

    return {
        "gate": "Gate 4",
        "p0_cells_verified": 36,
        "p0b_cells_verified": 36,
        "plain_desc_bounds": "[80, 105]",
        "subcell_bounds": "[170, 200]",
    }


def run_gate_5(dfs: dict[str, pd.DataFrame]) -> dict:
    """Gate 5: Cumulative Beeline Bracket Consistency & Share Conservation."""
    lb_df = dfs["level_brackets"]
    lc_df = dfs["ladder_cells"]
    g5_df = dfs["gen5_speculative"]

    expected_brackets = list(LEVEL_BRACKET_STRS.values())
    assert lb_df["beeline_bracket"].tolist() == expected_brackets
    for b in lc_df["beeline_hrs_bracket"].unique():
        assert b in expected_brackets, f"Gate 5 Failed: Unexpected bracket {b} in ladder_cells"
    for b in g5_df["beeline_hrs_bracket"].unique():
        assert b in expected_brackets, f"Gate 5 Failed: Unexpected bracket {b} in gen5_speculative"

    # Check 100.0% share conservation per generation across L1..L6
    all_cells = pd.concat([lc_df, g5_df], ignore_index=True)
    for g in ["G0", "G1", "G2", "G3", "G4", "G5"]:
        sub = all_cells[all_cells["gen_id"] == g]
        for col in ["user_share_pct", "token_share_pct", "spend_share_pct"]:
            tot = sub[col].sum()
            assert abs(tot - 100.0) <= 0.5, f"Gate 5 Failed: {g} {col} sum = {tot} != 100.0"

    return {
        "gate": "Gate 5",
        "canonical_brackets": expected_brackets,
        "share_conservation_verified": "G0..G5 (100.0% +/- 0.5%)",
    }


def run_gate_6(dfs: dict[str, pd.DataFrame]) -> dict:
    """Gate 6: Multi-Scale Keyword Subset Hierarchy (Micro subsetneq Mini subsetneq Mega)."""
    for name in ["poster_encyclopedic_cells", "news_megachart_cells"]:
        df = dfs[name]
        for _, row in df.iterrows():
            cid = row["cell_id"]
            mega = [x.strip() for x in str(row["keywords_1line"]).split(",") if x.strip()]
            mini = [x.strip() for x in str(row["mini_keywords_subset"]).split(",") if x.strip()]
            micro = [x.strip() for x in str(row["micro_keywords_subset"]).split("·") if x.strip()]
            assert len(mega) == 8, f"Gate 6 Failed ({name} {cid}): mega len {len(mega)} != 8"
            assert 4 <= len(mini) <= 6, f"Gate 6 Failed ({name} {cid}): mini len {len(mini)} not in [4, 6]"
            assert 2 <= len(micro) <= 3, f"Gate 6 Failed ({name} {cid}): micro len {len(micro)} not in [2, 3]"
            assert set(micro).issubset(set(mini)) and len(micro) < len(mini), (
                f"Gate 6 Failed ({name} {cid}): micro {micro} not proper subset of mini {mini}"
            )
            assert set(mini).issubset(set(mega)) and len(mini) < len(mega), (
                f"Gate 6 Failed ({name} {cid}): mini {mini} not proper subset of mega {mega}"
            )

    return {
        "gate": "Gate 6",
        "p0_hierarchy_verified": 36,
        "p0b_hierarchy_verified": 36,
    }


def run_gate_8(dfs: dict[str, pd.DataFrame]) -> dict:
    """Gate 8: Empirical Dataset & Table Completeness."""
    assert len(dfs["existing_ladders"]) >= 22, "Expected >= 22 existing ladders"
    assert len(dfs["use_cases"]) == 36, "Expected 36 Track A/B use cases"
    assert len(dfs["courses_blogs"]) >= 26, "Expected >= 26 courses/blogs"
    assert len(dfs["hope_inventory"]) == 20, "Expected 20 hopes"
    assert len(dfs["pricing_hardware_baseline"]) >= 14, "Expected >= 14 pricing/hardware baselines"
    assert len(dfs["ladder_cells"]) == 30, "Expected 30 G0-G4 ladder cells"
    assert len(dfs["gen5_speculative"]) == 6, "Expected 6 G5 speculative cells"

    return {
        "gate": "Gate 8",
        "existing_ladders": len(dfs["existing_ladders"]),
        "use_cases": len(dfs["use_cases"]),
        "courses_blogs": len(dfs["courses_blogs"]),
        "hope_inventory": len(dfs["hope_inventory"]),
        "pricing_hardware": len(dfs["pricing_hardware_baseline"]),
    }


EXPECTED_44_FIGURES = [
    # 3 User-Skill Megacharts
    "fig_v5_p0_micro_sae_card.png",
    "fig_v5_p0_mini_megachart.png",
    "fig_v5_p0_encyclopedic_megachart_poster.png",
    # 3 Historical News Megacharts
    "fig_v5_p0b_micro_news_card.png",
    "fig_v5_p0b_mini_news_megachart.png",
    "fig_v5_p0b_historical_news_megachart_poster.png",
    # 6 Per-Generation SAE Micro Cards
    "fig_v5_micro_gen0_sae.png",
    "fig_v5_micro_gen1_sae.png",
    "fig_v5_micro_gen2_sae.png",
    "fig_v5_micro_gen3_sae.png",
    "fig_v5_micro_gen4_sae.png",
    "fig_v5_micro_gen5_sae.png",
    # 12 Per-TRL-Lineage Micro Cards (exact filenames from TRL_DATA)
    "fig_v5_micro_trl01_transformer.png",
    "fig_v5_micro_trl02_rlhf.png",
    "fig_v5_micro_trl03_rag.png",
    "fig_v5_micro_trl04_diffusion.png",
    "fig_v5_micro_trl05_cot_rlvr.png",
    "fig_v5_micro_trl06_flash_kv.png",
    "fig_v5_micro_trl07_lora_qlora.png",
    "fig_v5_micro_trl08_react_mcp.png",
    "fig_v5_micro_trl09_ethics_eu_ai_act.png",
    "fig_v5_micro_trl10_injection_hierarchy.png",
    "fig_v5_micro_trl11_copyright_optout.png",
    "fig_v5_micro_trl12_grounded_search.png",
    # 6 Visual Abstracts
    "fig_v5_va0_root.png",
    "fig_v5_va1_part1.png",
    "fig_v5_va2_part2.png",
    "fig_v5_va3_part3.png",
    "fig_v5_va4_part4.png",
    "fig_v5_va5_part5.png",
    # 14 Analytical Plots + GIF
    "fig_v5_p1_macro_resource_trajectories.png",
    "fig_v5_p2_skill_deflation_escalator.png",
    "fig_v5_p3_folksonomy_and_gen_breaks.png",
    "fig_v5_p4_task_cost_vs_learning_jointplot.png",
    "fig_v5_p5_gen0_matrix.png",
    "fig_v5_p6_gen1_matrix.png",
    "fig_v5_p7_gen2_matrix.png",
    "fig_v5_p8_gen3_matrix.png",
    "fig_v5_p9_gen4_matrix.png",
    "fig_v5_p10_alluvial_evolution_poster.png",
    "fig_v5_p11_trl_and_failed_hopes.png",
    "fig_v5_p12_ladder_comparison_matrix.png",
    "fig_v5_p13_ladder_evolution_anim.gif",
    "fig_v5_p14_gen5_speculative_matrix.png",
]


def run_gate_7(dfs: dict[str, pd.DataFrame], check_figures: bool = True, check_report: bool = True) -> dict:
    """Gate 7: Visual Suite & Report Cross-Verification."""
    result = {"gate": "Gate 7", "expected_figures": len(EXPECTED_44_FIGURES)}
    if check_figures:
        missing_figs = []
        for fn in EXPECTED_44_FIGURES:
            fpath = os.path.join(FIGURES_DIR, fn)
            if not os.path.exists(fpath) or os.path.getsize(fpath) == 0:
                missing_figs.append(fn)
        assert not missing_figs, f"Gate 7 Failed: Missing or empty figures in figures_v5/: {missing_figs}"
        result["figures_verified_on_disk"] = len(EXPECTED_44_FIGURES)

    if check_report:
        assert os.path.exists(REPORT_PATH), f"Gate 7 Failed: Report {REPORT_PATH} does not exist!"
        with open(REPORT_PATH, "r", encoding="utf-8") as f:
            rep = f.read()

        unembedded = [fn for fn in EXPECTED_44_FIGURES if f"figures_v5/{fn}" not in rep]
        assert not unembedded, f"Gate 7 Failed: Figures not embedded in report v5.md: {unembedded}"

        for term in dfs["glossary_etymology"]["term_keyword"]:
            assert term in rep, f"Gate 7 Failed: Glossary term '{term}' missing from report v5.md!"

        for eid in dfs["defining_events"]["event_id"]:
            assert eid in rep, f"Gate 7 Failed: Event ID '{eid}' missing from report v5.md!"

        for tid in dfs["trl_trajectories"]["lineage_id"]:
            assert tid in rep, f"Gate 7 Failed: TRL ID '{tid}' missing from report v5.md!"

        for bad in ["(`~50h`)", "(`~200h`)", "(`~500h`)", "(`~2,000h`)"]:
            assert bad not in rep, f"Gate 7 Failed: Prohibited non-cumulative label {bad} found in report!"

        result["report_chars"] = len(rep)
        result["report_lines"] = rep.count("\n") + 1
        result["all_44_figures_embedded"] = True
        result["all_glossary_terms_in_report"] = len(dfs["glossary_etymology"])
        result["all_144_events_in_report"] = len(dfs["defining_events"])

    return result


def run_all_gates(check_figures: bool = False, check_report: bool = False) -> list[dict]:
    """Compile CSVs and execute Gates 1-8."""
    dfs = build_all_csvs()
    results = [
        run_gate_1(dfs),
        run_gate_2(dfs),
        run_gate_3(dfs),
        run_gate_4(dfs),
        run_gate_5(dfs),
        run_gate_6(dfs),
        run_gate_8(dfs),
    ]
    if check_figures or check_report:
        results.insert(6, run_gate_7(dfs, check_figures=check_figures, check_report=check_report))
    return results


if __name__ == "__main__":
    verify_rep = "--verify-report" in sys.argv
    verify_figs = "--verify-figures" in sys.argv
    res = run_all_gates(check_figures=verify_figs, check_report=verify_rep)
    print("==================================================================")
    print("v5_data_and_gates.py: ALL REQUESTED DETERMINISTIC GATES PASSED!")
    print("==================================================================")
    for r in res:
        print(f"  [PASS] {r['gate']}: {r}")
