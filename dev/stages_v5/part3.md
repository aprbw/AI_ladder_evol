## 3. Part III — Inductive Boundary Method, Six Relational Invariants & Deferred Naming

**Part III Synthesis:** This section formalizes our four-step inductive methodology: (3.1) deriving generation cutoffs (`G0..G5`) strictly from simultaneous upper-level emergence (`L2–L6`) and lower-level built-in sinking (`L1–L2`); (3.2) standardizing the six cumulative beeline learning-hour and capital brackets (`L1..L6`) and four-tier cognitive input hierarchy; (3.3) enforcing the `Track A/B` profession split (`SWE` vs. `MLE` vs. `Scientist`) and **Six Core Relational Invariants (`INV_01`–`INV_06`)** governing `Scope & Evolution`; and (3.4) executing the Deferred Naming Protocol (`Table 3.4`).

#### Part III Structural Index

* [3.1 User-Perspective Generation Boundary Derivation (Simultaneous Upper Emergence & Lower Sinking)](#31-user-perspective-generation-boundary-derivation-simultaneous-upper-emergence--lower-sinking)
* [3.2 Standardized Six-Level Cumulative Beeline Brackets & Four-Tier Cognitive Input Hierarchy](#32-standardized-six-level-cumulative-beeline-brackets--four-tier-cognitive-input-hierarchy)
* [3.3 Using vs. Making (Track A/B) Profession Mapping & Six Core Relational Invariants](#33-using-vs-making-track-ab-profession-mapping--six-core-relational-invariants)
* [3.4 Deferred Naming Protocol (Boundaries First, Folksonomy Names Last)](#34-deferred-naming-protocol-boundaries-first-folksonomy-names-last)

![Plot VA3: Part III Inductive Methodology & Six Invariants Visual Abstract](figures_v5/fig_v5_va3_part3.png)

**Caption (`Plot VA3` — Part III Visual Abstract):** **Formal schematic of the Dual-Trigger Generation Boundary Rule, the Six Cumulative Beeline Brackets (`0h` to `~10,000h`), the Four-Tier Cognitive Input Hierarchy, and the Six Relational Invariants (`INV_01`–`INV_06`), rejecting $H_0$ that natural-language modality implies low technical skill.**

### 3.1 User-Perspective Generation Boundary Derivation (Simultaneous Upper Emergence & Lower Sinking)

**Dual-Trigger Boundary Rule (`Table 3.1`):** A new AI generation $G_t$ begins in month $m$ if and only if **both** conditions hold simultaneously across the Stage 1 inventory: (1) **Upper-Rung Emergence (`L2–L6`)**: at least three new workflow classes require practitioners to learn a new tool surface, protocol, or post-training paradigm; and (2) **Down-Ladder Sinking (`L1–L2`)**: at least two workflows that previously required `L2–L5` coding or prompt syntax become packaged at `TRL 8–9` into zero-setup `L1` (`0h | $0`) or `<50h` `L2` workspaces.

#### Table 3.1 — Inductive Generation Boundary Derivation Ledger (`G0` to `G5`)

**Caption (`Table 3.1`):** **Derivation of generation start/end dates (`YYYY-MM`), duration in months, upper-rung emergence triggers, and down-ladder sinking triggers.**

| Neutral Gen ID | Start Date | End Date | Duration (Months) | Upper-Rung Emergence Trigger (L2–L6) | Down-Ladder Sinking Trigger (L1–L2) | Extinguished Prior-Gen Manual Habits |
| --- | --- | --- | --- | --- | --- | --- |
| G0 | 2017-06 | 2020-05 | 36 | Single-GPU BERT fine-tuning (L4, ~600h); AutoML web consoles (L2, <50h); Self-attention & GLUE genesis (L6, ~10,000h) | Baseline generation (active zero-shot generative L1 missing; passive widgets only at 0h) | Hand-crafted morphological lexicons & SIFT/HOG feature engineering replaced by pretrained BERT embeddings |
| G1 | 2020-06 | 2022-10 | 29 | Few-shot completion prompting (L2, <50h); REST API wrappers (L3, <200h); DeepSpeed ZeRO sharding (L5, ~2,000h); Scaling laws, AlphaFold 2 & RLHF genesis (L6, ~10,000h) | Custom NLP classification sank from G0-L3/L4 (<200h to ~600h BERT/sklearn) to G1-L2 (<50h Playground few-shot); boilerplate lookup sank to G1-L1 (0h Copilot Tab) | Labeling 10,000 training rows & writing PyTorch training loops for basic sentiment/entity extraction became obsolete |
| G2 | 2022-11 | 2024-04 | 18 | Prompt engineering, system personas & Custom GPTs (L2, <50h); Chunked Vector RAG bots (L3, <200h); Single-GPU 4-bit QLoRA & llama.cpp (L4, ~600h); vLLM PagedAttention (L5, ~2,000h); Chinchilla/RoPE/DPO genesis (L6, ~10,000h) | Conversational Q&A/drafting sank from G1-L2 (<50h Playground completion prefixes) to G2-L1 (0h ChatGPT web UI); custom weight tuning sank from G1-L5 (~2,000h DeepSpeed) to G2-L4 (~600h single-GPU QLoRA) | Completion prefix/stop-sequence hacks (Input:/Output:) & multi-GPU full-weight fine-tuning for domain style adaptation became obsolete |
| G3 | 2024-05 | 2024-12 | 8 | Browser vibe builders (v0/Bolt) & 50-PDF workspaces (L2, <50h); AI IDE Vibe Coding (Cursor/Windsurf, L3, <200h); LangGraph orchestration (L4, ~600h); Containerized eval farms (L5, ~2,000h); RLVR/GRPO, Data Wall & MCP genesis (L6, ~10,000h) | Multimodal creation & live UI preview sank from G2-L2/L3 to G3-L1 (0h GPT-4o & Claude Artifacts); <50-PDF Q&A sank from G2-L3 (<200h Vector RAG code) to G3-L2 (<50h drag-and-drop Projects/NotebookLM) | Switching across separate websites/Discord for text vs image/vision, and writing custom Python vector-chunking scripts for 10-50 personal PDFs became obsolete |
| G4 | 2025-01 | 2026-10 | 22 | Deep Research scoping (L2, <50h); MCP wiring & coupled CLI delegation (L3, <200h); Context/Harness engineering & decoupled oracles (L4, ~600h); Air-gapped M4 Mac Mini OpenClaw swarms & GRPO RLVR (L5, ~2,000h); Pure-RL flywheels & SWE-bench Pro genesis (L6, ~10,000h) | Chain-of-Thought reasoning sank from G2/G3-L2 (<50h manual CoT) to G4-L1 (0h auto-router); 50-site web synthesis sank from G3-L4 (~600h scraper graphs) to G4-L2 (<50h Deep Research); tool wiring & happy-path CLI coding sank to G4-L3 (<200h .mcp.json & CLI delegation) | Manual 'Let's think step by step' / 'Take a deep breath' / 'Tip $200' prompt hacks, hand-rolled per-app REST tool schemas, and line-by-line manual IDE syntax typing became obsolete |
| G5 | 2026-11 | 2028-12 | 26 | [Speculative] Cloud Spec Studios (L2, <50h); Cross-org A2A/Cedar policy contracts (L3, <200h); Lean 4 / TLA+ formal proof swarms (L4, ~600h); Nightly enclave RLVR loops (L5, ~2,000h); Continual-plasticity & causal world-model genesis (L6, ~10,000h) | [Speculative] Deep Research scoping & single-app MCP actions sink to G5-L1 (0h ambient OS daemon); .mcp.json wiring & happy-path single-repo CLI coding sink to G5-L2 (<50h zero-CLI cloud specification studios) | [Speculative] Manual .mcp.json file editing, single-repo terminal CLI babysitting, and static un-distilled enterprise weights sink into cloud spec studios and nightly RLVR loops |

### 3.2 Standardized Six-Level Cumulative Beeline Brackets & Four-Tier Cognitive Input Hierarchy

**Cumulative Beeline Prerequisite Floor (`Table 3.2`):** Every vertical rung $L_k$ is anchored to the cumulative learning hours ($\text{Hours}_{\text{learn}}$) required for a competent professional starting from zero AI-specific training to execute that rung's workflow reliably in production, paired with the required hardware/API capital ceiling.

#### Table 3.2 — Standardized Six-Level Cumulative Beeline Brackets & Four-Tier Cognitive Input Hierarchy

**Caption (`Table 3.2`):** **Exact canonical bracket strings (`L1`..`L6`), compact axis tick labels, cognitive input tiers, and `Using vs. Making` split.**

| Level | Canonical Cumulative Beeline Bracket | Compact Plot Tick Label | Beeline Hours Ceiling | Capital Ceiling ($) | Four-Tier Cognitive Input Hierarchy | Track A (Using) vs Track B (Making) Split |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | L1: 0h (0d) \| $0 | L1 (0h / 0d \| $0) | 0 | 0 | Tier 1: Outcome Intent & Surface Taste | 100% Using / 0% Making |
| 2 | L2: <50h (~1 Wk / Short Course) \| <$30 | L2 (<50h / ~1 Wk \| <$30) | 50 | 30 | Tier 1->2: Structured Prompting, Multimodal Flags & Workspace Curation | 90% Using / 10% Making |
| 3 | L3: <200h (~1 Mo / 1 Uni Subject) \| <$100 | L3 (<200h / ~1 Mo \| <$100) | 200 | 100 | Tier 2: Declarative Pattern, API/SDK & Coupled Environment Literacy | 65% Using / 35% Making |
| 4 | L4: ~600h (~1 Qtr / 1 Uni Semester) \| ~$1.5k | L4 (~600h / ~1 Sem \| ~$1.5k) | 600 | 1500 | Tier 3: Formal System, Context Architecture, Decoupled Oracle & Loss Calibration | 35% Using / 65% Making |
| 5 | L5: ~2,000h (~1 Yr / Core Postgrad) \| ~$500k | L5 (~2,000h / ~1 Yr \| ~$500k) | 2000 | 500000 | Tier 4A: Hard Distributed Infrastructure, Sandbox Kernel & Weight Post-Training | 15% Using / 85% Making |
| 6 | L6: ~10,000h (~5 Yrs / Focused PhD) \| ~$100M+ | L6 (~10,000h / ~5 Yrs \| ~$100M+) | 10000 | 100000000 | Tier 4B: Frontier Mathematical Formulation, Data/Benchmark Genesis & Pretraining | 0% Routine / 100% Genesis Making |

### 3.3 Using vs. Making (Track A/B) Profession Mapping & Six Core Relational Invariants

**Six Formal Invariants Governing `Scope & Evolution` (`Table 3.3`):** Every cell's `Scope & Evolution` facet in Part IV and Section 5.4 is audited against six deterministic relational rules (`INV_01` to `INV_06`), replacing unstructured counterfactual prose with four-directional boundary proofs (`Why Not L-1?`, `Why Not L+1?`, `From Gen G-1`, `To Gen G+1`).

#### Table 3.3 — Six Core Relational Invariants Governing `Scope & Evolution` (`INV_01` to `INV_06`)

**Caption (`Table 3.3`):** **Formal specification of the six relational invariants enforced across all `36` skill cells.**

| Invariant ID | Relational Invariant Name | Formal Operational Rule & Boundary Enforcement |
| --- | --- | --- |
| INV_01 | Bidirectional Medium-Model Decoupling | Anchor every cell strictly to the human practitioner's prerequisite floor (Hours_learn & Capital); forbid conflating L1/L2 consumer usage with the L6 cluster cost that pretrained the model, and forbid downgrading formal L4+ mathematical/system invariants merely because they are typed in English. |
| INV_02 | The Meta-Bootstrapping Gate ('Why Not Level L-1?') | A workflow belongs at Level L only if an L-1 user fails even when attempting (a) By-Name Delegation ('Use library X') or (b) Research-and-Elicit Socratic Synthesis ('Interview me to build X'), due to context rot, hallucination, unverified state corruption, or security boundary violation. |
| INV_03 | Four-Tier Cognitive Input Hierarchy | Enforce strict cognitive progression across rungs: Tier 1 Outcome Intent & Surface Taste (L1, 0h) -> Tier 1-2 Structured Prompting & Workspace Curation (L2, <50h) -> Tier 2 Declarative Pattern, API & Coupled IDE/CLI Literacy (L3, <200h) -> Tier 3 Formal System, Context & Decoupled Oracle Specification (L4, ~600h) -> Tier 4A/4B Distributed Infra, Post-Training & Frontier Theory (L5-L6, ~2,000h-10,000h). |
| INV_04 | Failure-Boundary Anchor (Coupled Execution vs. Decoupled Oracles) | Coupled happy-path generation + self-authored unit testing belongs at L2/L3 (Vibe Coding / Coupled CLI), whereas designing independent property-based, simulation, or formal verification oracles that prevent Reward Hacking and Code Slop belongs strictly at L4+. |
| INV_05 | Recursive Cannibalization Rule ('Why Not Level L+1?') | Every rung L_k in Generation G_t recursively consumes automation from G_t-L_{1..k-1} to eliminate boilerplate toil; prove why L_k's own AI delegation makes escalating to L+1 unnecessary capital/hour waste for that scope. |
| INV_06 | Setup Half-Life & Dual Sinking Check ('From Gen G-1 / To Gen G+1') | Audit both vendor GUI productization (Supply-Side Sinking) and intra-generational conversational bootstrapping (Demand-Side Sinking) explaining why a G-1 higher-rung skill sinks 1-to-3 rungs downward in G_t and G+1. |

### 3.4 Deferred Naming Protocol (Boundaries First, Folksonomy Names Last)

**Deferred Folksonomy Naming (`Table 3.4`):** Only after locking all `G0..G5` date cutoffs (`Section 3.1`) and `L1..L6` beeline brackets (`Section 3.2`) do we assign descriptive folksonomy titles drawn directly from the dominant practitioner terms in `Table 2.1` and `Table 2.3b`.

#### Table 3.4 — Deferred Naming Protocol Ledger (`G0..G5` & `L1..L6`)

**Caption (`Table 3.4`):** **Mapping from neutral coordinate IDs (`G0..G5`, `L1..L6`) to final emergent folksonomy titles.**

| Neutral ID | Coordinate Axis | Locked Boundary / Beeline Bracket | Coined Emergent Folksonomy Title |
| --- | --- | --- | --- |
| G0 | Horizontal Generation | 2017-06 to 2020-05 | Gen 0: The Pre-LLM Code-Pipeline & Passive-Widget Generation |
| G1 | Horizontal Generation | 2020-06 to 2022-10 | Gen 1: The Completion Playground & Ghost-Text Autocomplete Generation |
| G2 | Horizontal Generation | 2022-11 to 2024-04 | Gen 2: The Conversational Chat, Manual Prompting & DIY Vector-RAG Generation |
| G3 | Horizontal Generation | 2024-05 to 2024-12 | Gen 3: The Multimodal Workspace, Vibe Coding & Agentic Graph Generation |
| G4 | Horizontal Generation | 2025-01 to 2026-10 | Gen 4: The Auto-Routed Reasoner, Deep Research, Terminal CLI & Sandbox Swarm Generation |
| G5 | Horizontal Generation | 2026-11 to 2028-12 | Gen 5 (Spec.): The Verified Autonomous Workforce & Cross-Org Agentic Mesh Generation |
| L1 | Vertical Skill Rung | L1: 0h (0d) \| $0 | Level 1: Consumer Tool User |
| L2 | Vertical Skill Rung | L2: <50h (~1 Wk / Short Course) \| <$30 | Level 2: Prompt, Workspace & Spec Power-User |
| L3 | Vertical Skill Rung | L3: <200h (~1 Mo / 1 Uni Subject) \| <$100 | Level 3: Applied Workflow, IDE & MCP Integrator |
| L4 | Vertical Skill Rung | L4: ~600h (~1 Qtr / 1 Uni Semester) \| ~$1.5k | Level 4: Harness, Verification Oracle & Single-GPU Tuning Engineer |
| L5 | Vertical Skill Rung | L5: ~2,000h (~1 Yr / Core Postgrad) \| ~$500k | Level 5: Distributed Cluster, Post-Training & Sandbox Architect |
| L6 | Vertical Skill Rung | L6: ~10,000h (~5 Yrs / Focused PhD) \| ~$100M+ | Level 6: AI Research Scientist, Data/Benchmark Architect & Next-Gen Pioneer |

---
