# AI Ladder Evolution Megaprompt v2 (MP2)

**Multi-Agent History, User Skill-Tree Progression, Resource Economics & Visual Atlas of AI Ladders:** Orchestrate a multi-agent research and visualization pipeline to produce a comprehensive ~50,000+-word historical and data-driven report (including a standalone ~2,500-word / ~5% Extended Summary in Part I) mapping how people have used artificial intelligence (AI), large language models (LLMs), and action-taking AI (agentic AI) across eras (`2017-06` to `2026-10`), ordered bottom-to-top strictly by **User-Side Sophistication & Skill-Tree Complexity** (complexity from the perspective of the human user — what skills the user must learn, what specialized tools like IDEs or terminal CLIs they must install instead of a web browser, and what non-compute environment or hardware resources like isolated sandboxes or a dedicated Mac Mini they must set up to operate at a higher rung), measured by both single-task and industry-wide resource use, compared against existing literature ladders in a dedicated post-synthesis section at the end (`Section 5.3`, only after building our five-era ladder evolution list in `Part IV`), navigated via clickable multi-level tables of contents (Root ToC plus Per-Part ToCs up to Level 4 using part-prefixed numbering), and illustrated with liberal visual density (a Root Visual Abstract, a Visual Abstract at the start of every Part, at least one visualization and one structured table in every `### H3` section, and two continuous-time, duration-proportional full-timeline posters covering structural evolution and era-defining tech triggers, "who did what" news wins/failures, and the "top thing to learn" per era).

### Structural Index
* [1. Agent Contract, Style & Visual Density Rules](#1-agent-contract-style--visual-density-rules)
  * [1.1 Role, Multi-Agent Team & Search Precision](#11-role-multi-agent-team--search-precision)
  * [1.2 Writing Style, Fractal ToCs & Word-Count Targets](#12-writing-style-fractal-tocs--word-count-targets)
  * [1.3 Liberal Visual Density, Visual Abstracts & Continuous-Time Posters](#13-liberal-visual-density-visual-abstracts--continuous-time-posters)
  * [1.4 Domain Scope & User Skill-Tree Ordering Rules ("What Up Means")](#14-domain-scope--user-skill-tree-ordering-rules-what-up-means)
* [2. Literature, News & Cost Survey Directives](#2-literature-news--cost-survey-directives)
  * [2.1 Review of Existing Published & Informal AI Ladders (Pure Literature Survey)](#21-review-of-existing-published--informal-ai-ladders-pure-literature-survey)
  * [2.2 Step Use-Case Sources: Reports, Traffic Logs, Courses, Surveys & News](#22-step-use-case-sources-reports-traffic-logs-courses-surveys--news)
  * [2.3 Single-Task vs. Industry-Wide Resource Metrics & Fallback Math](#23-single-task-vs-industry-wide-resource-metrics--fallback-math)
* [3. How to Build the Ladders (Four-Rule Protocol)](#3-how-to-build-the-ladders-four-rule-protocol)
  * [3.1 Rule 1: Two-Shift Era Cutoff Threshold](#31-rule-1-two-shift-era-cutoff-threshold)
  * [3.2 Rule 2: Bottom-Up & Top-Down Usage Reconciliation](#32-rule-2-bottom-up--top-down-usage-reconciliation)
  * [3.3 Rule 3: No-Overlap & No-Gaps (MECE) Two-of-Three User Skill-Tree Split Test](#33-rule-3-no-overlap--no-gaps-mece-two-of-three-user-skill-tree-split-test)
  * [3.4 Rule 4: Cross-Era Linkage & Convergence Lock](#34-rule-4-cross-era-linkage--convergence-lock)
* [4. Ladder Evolution Directives (Per-Era Architecture)](#4-ladder-evolution-directives-per-era-architecture)
  * [4.1 Era Dates & Why Old Ladders Get Outdated (Tech, Cost & Habit Shifts)](#41-era-dates--why-old-ladders-get-outdated-tech-cost--habit-shifts)
  * [4.2 How Steps Change Between Eras (Sunk, Evolved, Split, New & Gone)](#42-how-steps-change-between-eras-sunk-evolved-split-new--gone)
  * [4.3 Era-Defining Moments: Tech Triggers, News ("Who Did What") & Top Skill to Learn](#43-era-defining-moments-tech-triggers-news-who-did-what--top-skill-to-learn)
  * [4.4 Full-Ladder Era Resource Totals & Conservation Checks](#44-full-ladder-era-resource-totals--conservation-checks)
* [5. Steps in a Ladder (Five-Part User Skill-Tree Step Profile)](#5-steps-in-a-ladder-five-part-user-skill-tree-step-profile)
  * [5.1 Step Name, Rank & User Skill-Tree Boundaries](#51-step-name-rank--user-skill-tree-boundaries)
  * [5.2 Concrete Tool Stack, Use Cases & Same-User Context Switching](#52-concrete-tool-stack-use-cases--same-user-context-switching)
  * [5.3 Two-Level Step Resource Accounting & Machine-Readable Row](#53-two-level-step-resource-accounting--machine-readable-row)
* [6. Multi-Agent Execution & Visual Verification Pipeline](#6-multi-agent-execution--visual-verification-pipeline)
  * [6.1 Stage 1: Parallel Literature, News & Cost Subagents](#61-stage-1-parallel-literature-news--cost-subagents)
  * [6.2 Stage 2: Orchestrator Timeline & Master Skeleton Lock](#62-stage-2-orchestrator-timeline--master-skeleton-lock)
  * [6.3 Stage 3: Parallel Per-Era Deep-Dive & Post-Synthesis Comparison Subagents](#63-stage-3-parallel-per-era-deep-dive--post-synthesis-comparison-subagents)
  * [6.4 Stage 4: Code-Driven Visual Rendering, Inspection Loop & Report Assembly](#64-stage-4-code-driven-visual-rendering-inspection-loop--report-assembly)
* [7. Five-Part Output Report Blueprint & Final Verification Gates](#7-five-part-output-report-blueprint--final-verification-gates)
  * [7.1 Five-Part Report Structure (Including Part I ~5% Extended Summary & Section 5.3 Post-Synthesis Comparison)](#71-five-part-report-structure-including-part-i-5-extended-summary--section-53-post-synthesis-comparison)
  * [7.2 Mandatory Visual & Table Inventory Across All Sections](#72-mandatory-visual--table-inventory-across-all-sections)
  * [7.3 Six-Point Final Verification & Word-Count Audit Checklist](#73-six-point-final-verification--word-count-audit-checklist)

***

## 1. Agent Contract, Style & Visual Density Rules

**Section 1 Overview:** Defines the lead orchestrator and subagent division of labor, enforces Arian Fractal Format with clickable Root and Per-Part tables of contents up to Level 4 (`H4`), sets the ~5% (~2,500-word) Part I Extended Summary target, mandates liberal visual and tabular coverage across every section, and establishes the **User-Sophistication & Skill-Tree Definition of "Up the Ladder"**.

#### Section 1 Structural Index
* [1.1 Role, Multi-Agent Team & Search Precision](#11-role-multi-agent-team--search-precision)
  * [1.1.1 Lead Orchestrator & Subagent Specialization](#111-lead-orchestrator--subagent-specialization)
  * [1.1.2 Primary Input Sources & Technical Search Queries](#112-primary-input-sources--technical-search-queries)
* [1.2 Writing Style, Fractal ToCs & Word-Count Targets](#12-writing-style-fractal-tocs--word-count-targets)
  * [1.2.1 Arian Fractal Format (BLUF, RIH & Clickable Multi-Level ToCs)](#121-arian-fractal-format-bluf-rih--clickable-multi-level-tocs)
  * [1.2.2 Part-Numbered Per-Part ToC Rule (Up to Level 4 / H4)](#122-part-numbered-per-part-toc-rule-up-to-level-4--h4)
  * [1.2.3 Plain Layman English, Bracketed Technical Jargon & Caveman Density](#123-plain-layman-english-bracketed-technical-jargon--caveman-density)
  * [1.2.4 Part I Extended Summary (~5% / ~2.5k Words) & Word-Count Breakdown](#124-part-i-extended-summary-5--25k-words--word-count-breakdown)
* [1.3 Liberal Visual Density, Visual Abstracts & Continuous-Time Posters](#13-liberal-visual-density-visual-abstracts--continuous-time-posters)
  * [1.3.1 Root Visual Abstract & Per-Part Visual Abstracts (Parts I–V)](#131-root-visual-abstract--per-part-visual-abstracts-parts-iv)
  * [1.3.2 Every-H3 Visualization & Structured Table Mandate](#132-every-h3-visualization--structured-table-mandate)
  * [1.3.3 Poster 1: Continuous-Time Alluvial Evolution Poster (`fig_full_evolution_poster.png`)](#133-poster-1-continuous-time-alluvial-evolution-poster-fig_full_evolution_posterpng)
  * [1.3.4 Poster 2: Continuous-Time Era-Defining News, Tech & Top Skill Poster (`fig_era_defining_news_and_learning_poster.png`)](#134-poster-2-continuous-time-era-defining-news-tech--top-skill-poster-fig_era_defining_news_and_learning_posterpng)
  * [1.3.5 Deterministic Plotting (`matplotlib`) & Mandatory Visual Inspection Loop](#135-deterministic-plotting-matplotlib--mandatory-visual-inspection-loop)
* [1.4 Domain Scope & User Skill-Tree Ordering Rules ("What Up Means")](#14-domain-scope--user-skill-tree-ordering-rules-what-up-means)
  * [1.4.1 Empirical Positive Taxonomy vs. Speculative Claims](#141-empirical-positive-taxonomy-vs-speculative-claims)
  * [1.4.2 Bottom-to-Top User-Sophistication & Skill-Tree Complexity Axis ("What Up Means")](#142-bottom-to-top-user-sophistication--skill-tree-complexity-axis-what-up-means)

### 1.1 Role, Multi-Agent Team & Search Precision

**Orchestration & Grounding:** Coordinates specialized research and plotting subagents using technical search queries translated into clear prose.

#### 1.1.1 Lead Orchestrator & Subagent Specialization

* **Core Job:** Coordinate a staged team of subagents to map how AI, large language models (LLMs), and action-taking AI (agentic AI) ladders have evolved from `2017-06` to `2026-10` — why old ladders become outdated after new breakthroughs, how individual steps change from era to era along a **User Sophistication Skill Tree**, what news milestones ("who did what") and top skills define each era, how much resource each step uses, and how our completed five-era ladder compares against all existing ladders found in the literature review (`Section 5.3`).
* **Subagent Division of Labor:** Follow `Multi-Agent Execution & Visual Verification Pipeline` ([Section 6](#6-multi-agent-execution--visual-verification-pipeline)) so literature discovery, timeline locking, per-era deep dives (one subagent per era ladder $L_t$), post-synthesis literature comparison, extended summary synthesis, and code-driven visual generation each get dedicated search depth and output space.

#### 1.1.2 Primary Input Sources & Technical Search Queries

* **Input Sources:** Use this markdown prompt plus thorough web search across published AI ladders, research papers, annual AI reports, paid model traffic logs (API usage data), developer surveys, educational resources (courses, university syllabi, code cookbooks, tutorials), and front-page news archives.
* **Search Precision:** Every agent runs search queries using exact technical terms (`RLVR`, `GRPO`, `FLOPs`, `KV-cache`, `MCP`, `LoRA`, `QLoRA`, `RAG`, `pass@k`, `SWE-bench`, `git worktree`, `OpenClaw`, `Mac Mini agent server`) to pull primary technical sources, then translates findings into plain English when writing.

### 1.2 Writing Style, Fractal ToCs & Word-Count Targets

**Fractal Structure & Navigation:** Enforces recursive bottom-line summaries, clickable multi-level tables of contents using strict part-prefixed numbering up to Level 4 (`H4`), plain layman English with bracketed technical terms, and a ~5% (~2,500-word) Extended Summary in Part I.

#### 1.2.1 Arian Fractal Format (BLUF, RIH & Clickable Multi-Level ToCs)

* **Bottom-Line Summaries (BLUF):** Start the entire report, every Part (`## H2`), every Section (`### H3`), and every Subsection (`#### H4`) containing $\ge 3$ child items with a concise, high-density summary paragraph at the top stating the core outcome and numbers up front.
* **Clickable Root Table of Contents (`### Structural Index`):** Place a nested table of contents right under the root Executive Summary and Root Visual Abstract listing all 5 Parts (`## 1.` to `## 5.`) and all 20 H3 sections (`### 1.1` to `### 5.4`), where **every entry is a clickable GitHub-Flavored Markdown anchor link** (e.g., ``* [1.1 Section Title](#11-section-title)``).
* **Bold Lead-In Labels (`**RIH:**`):** Start every bullet and paragraph with a bold 2–4 word run-in heading summarizing the concrete claim or metric of that block.

#### 1.2.2 Part-Numbered Per-Part ToC Rule (Up to Level 4 / H4)

* **Mandatory Per-Part ToC After Every Part Overview:** Because the report has deep hierarchical nesting (`H2 -> H3 -> H4 -> H5`), **every Part (`Part I` through `Part V`) MUST include its own dedicated clickable Table of Contents (`#### Part X Structural Index`) immediately after its Part Overview and Part Visual Abstract**, expanding all the way down to **Level 4 (`#### H4`)**.
* **Strict Part-Prefixed Hierarchical Numbering:** Every heading and every ToC entry inside Part $X$ MUST use Part $X$'s number as its prefix (`X.Y` for `### H3`, `X.Y.Z` for `#### H4`, and `X.Y.Z.W` for `##### H5`):
  * **Part I ToC:** Every entry starts with `1.` (``* [1.1 ...](#11-...)``, ``  * [1.1.1 ...](#111-...)``, ``* [1.2 ...](#12-...)``, etc., through ``  * [1.4.3 ...](#143-...)``).
  * **Part II ToC:** Every entry starts with `2.` (``* [2.1 ...](#21-...)``, ``  * [2.1.1 ...](#211-...)``, ``  * [2.1.2 ...](#212-...)``, ``* [2.2 ...](#22-...)``, ``  * [2.2.1 ...](#221-...)``, ``* [2.3 ...](#23-...)``, ``  * [2.3.1 ...](#231-...)``, etc.).
  * **Part III ToC:** Every entry starts with `3.` (``* [3.1 ...](#31-...)``, ``  * [3.1.1 ...](#311-...)``, ``* [3.2 ...](#32-...)``, etc.).
  * **Part IV ToC:** Every entry starts with `4.` (``* [4.1 ...](#41-...)``, ``  * [4.1.1 ...](#411-...)`` through ``  * [4.5.4 ...](#454-...)``).
  * **Part V ToC:** Every entry starts with `5.` (``* [5.1 ...](#51-...)``, ``* [5.2 ...](#52-...)``, ``  * [5.2.1 ...](#521-...)``, ``  * [5.2.2 ...](#522-...)``, ``  * [5.2.3 ...](#523-...)``, ``* [5.3 ...](#53-...)``, ``  * [5.3.1 ...](#531-...)``..``[5.3.4 ...](#534-...)``, ``* [5.4 ...](#54-...)``).
* **Zero Broken Anchor Links:** Generate GitHub Markdown anchor slugs deterministically (lowercase heading text, strip punctuation except hyphens and spaces, replace spaces with `-`) and run an automated Python link-verification pass confirming 100% of Root and Per-Part ToC links resolve to an exact heading in the document.

#### 1.2.3 Plain Layman English, Bracketed Technical Jargon & Caveman Density

* **Plain Layman English:** Write in plain, direct English for a smart general reader outside the AI field. Use everyday tech words (`prompt`, `chat`, `model`, `autocomplete`, `database`, `code editor`) plainly with zero brackets, and replace empty academic words (`methodology`, `taxonomy`, `paradigm`, `obsolescence`, `telemetry`) with simple everyday words (`method`, `ordering`/`classification`, `shift`, `getting outdated`, `usage logs`).
* **Bracketed Technical Jargon:** When a real, established AI or engineering term exists and improves accuracy, write the plain meaning first and append the technical term in parentheses as `plain English (technical term)` on first use in a section, then use the short term cleanly after — for example, write *"training models to think step by step before answering (RLVR test-time compute)"* rather than raw jargon *"RLVR test-time compute scaling"* or vague *"making AI think harder"*.
* **Caveman Compression & Concrete Specificity:** Keep high information density using short, direct sentences and positive instructions stating what to do. Name exact models, software libraries, websites, tools, release dates (`YYYY-MM`), and data sources.

#### 1.2.4 Part I Extended Summary (~5% / ~2.5k Words) & Word-Count Breakdown

* **Part I Extended Summary Mandate:** Include a dedicated **Part I — Extended Summary** (`## 1. Part I — Extended Summary`) right after the Root ToC that synthesizes the entire report (`Parts II–V`) into a standalone executive digest of **approximately 2,500–3,000 words (~5% of the full report)**.
* **Word-Count Accounting Per Part:** Track and report the exact word count and percentage share of the total report for the Root Frontmatter and each of the five Parts (`Part I` through `Part V`), verifying that Part I stays tightly centered around `~5%`.

### 1.3 Liberal Visual Density, Visual Abstracts & Continuous-Time Posters

**Maximum Visual Density Rules:** Mandates a Root Visual Abstract, a dedicated Visual Abstract at the start of every Part (Parts I–V), at least one publication-grade visualization and one structured table in every `### H3` section, and two synchronized continuous-time full-timeline posters with duration-proportional era box widths.

#### 1.3.1 Root Visual Abstract & Per-Part Visual Abstracts (Parts I–V)

* **Root Visual Abstract (`figures/fig_va0_root_report.png`):** Place a high-density multi-panel Visual Abstract at the very top of the report (immediately below the Root Executive Summary BLUF and above the Root `Structural Index`) summarizing: (Panel A) the 5 chronological Era Ladders ($L_1 \dots L_5$) and the 18-Month Downward Sinking Law, (Panel B) the 4 repeating structural and economic laws, and (Panel C) the 10-year log-scale trajectory (`2017–2026`) of inference price, enterprise spend, top-step task tokens, and active users with a right-hand unfilled step marginal histogram.
* **Per-Part Visual Abstracts (`figures/fig_va1_part1_summary.png` through `figures/fig_va5_part5_laws.png`):** Place a dedicated 2-panel Visual Abstract at the beginning of **every single Part (`Part I` through `Part V`)**, immediately below the `Part Overview` and above the `Part Structural Index`.

#### 1.3.2 Every-H3 Visualization & Structured Table Mandate

* **Liberal Visual & Tabular Coverage Across Every `### H3` Section:** Every single `### H3` section in the report (`### 1.1` through `### 5.4`, all 20 H3 sections) MUST contain **at least one dedicated visualization (numbered Figure `Figure 1`..`Figure 23` and/or Mermaid structural flowchart)** AND **at least one structured Markdown comparison table**.
* **Standalone Declarative Captions:** Pair every Visual Abstract and numbered Figure with a standalone caption opening with a **bold declarative conclusion sentence** stating the primary quantitative finding (`**Figure N — [Declarative Takeaway Sentence with Key Numbers].** [Panel-by-panel breakdown, variables, units, and context]`).

#### 1.3.3 Poster 1: Continuous-Time Alluvial Evolution Poster (`fig_full_evolution_poster.png`)

* **True Continuous Calendar Time X-Axis (`2017-06` to `2026-10`):** Plot the X-axis of `figures/fig_full_evolution_poster.png` on continuous decimal calendar years (`2017.25` to `2027.00`, with exact `YYYY-MM` vertical dashed era boundary lines at `2017-06`, `2020-06`, `2022-11`, `2024-06`, `2025-02`, and `2026-10`).
* **Duration-Proportional Era Box Widths ($w_t \propto \text{Months}_t$):** Adjust the horizontal width of every Era column header and every step box strictly in proportion to that era's true duration in months out of the 113-month timeline (`L1 = 36m [31.9%]`, `L2 = 29m [25.7%]`, `L3 = 19m [16.8%]`, `L4 = 8m [7.1%]`, `L5 = 21m [18.6%]`).
* **Synchronized Multi-Panel Layout:** Pair the upper alluvial diagram (23 user skill-tree steps ordered bottom-to-top, connected by shuffled-z-order cubic Bezier ribbons color-coded by transition mechanism, plus a right-hand `Era Width (Months)` horizontal bar chart) with a lower economic panel sharing the exact continuous time X-axis.

#### 1.3.4 Poster 2: Continuous-Time Era-Defining News, Tech & Top Skill Poster (`fig_era_defining_news_and_learning_poster.png`)

* **Shared Continuous Calendar Time X-Axis & Duration-Proportional Boxes:** Render a second full-timeline poster (`figures/fig_era_defining_news_and_learning_poster.png`) on the exact same continuous calendar time X-axis (`2017-06` to `2026-10`) with era box widths strictly proportional to duration (`36m`, `29m`, `19m`, `8m`, `21m`), organized into **4 horizontal domain swimlanes + 1 bottom pinpoint milestone track**: (1) **Tech Triggers (Starts vs. Ends Era)**, (2) **Defining Wins ("Who Did What" Breakthroughs)**, (3) **Defining Failures ("Who Did What" Cautionary Tales & Shocks)**, and (4) **"Top Thing to Learn" Per Era (User Skill-Tree Milestone & Flagship Curricula)**.

#### 1.3.5 Deterministic Plotting (`matplotlib`) & Mandatory Visual Inspection Loop

* **Pure `matplotlib` Execution & `view_file` Inspection:** Render all charts natively using Python `matplotlib` (Okabe-Ito colorblind-safe palette, `dpi=220–300`). Never use `seaborn`. Never place two literal `$` signs inside a single `matplotlib` text string; write `USD ` in plot strings and `\$` outside math mode in Markdown prose. Inspect every `.png` via `view_file` to verify zero text clipping or overlaps.

### 1.4 Domain Scope & User Skill-Tree Ordering Rules ("What Up Means")

**Empirical Boundaries & User-Centric Ordering Axis:** Restricts ladder rungs to verified historical usage and orders all steps bottom-to-top strictly by **Complexity from the Perspective of the User (The User AI Skill Tree)**.

#### 1.4.1 Empirical Positive Taxonomy vs. Speculative Claims

* **Domain Scope:** AI, LLMs, and agentic AI across text, code, step-by-step reasoning, and tool use, including image/video models (computer vision / CV) and audio models where connected to LLM workflows (screen-reading models [vision-language models / VLMs], image-and-text document search [multimodal RAG], reading text from images [OCR-to-LLM], and native audio synthesis [`NotebookLM`]).
* **Real Usage Only (Positive Taxonomy):** Build a factual classification of how people actually used AI in each historical era rather than a speculative theory of future AGI. Set aside unverified corporate rungs (such as OpenAI *Level 4 Innovators* / *Level 5 Organizations* or Shapiro *Level 5 Dark Factory*) until an era where empirical usage logs back them.

#### 1.4.2 Bottom-to-Top User-Sophistication & Skill-Tree Complexity Axis ("What Up Means")

* **Core Definition of "Up" (User Sophistication, NOT Model/Task/Backend Complexity):** Moving **up** the ladder from `Step 1` (bottom rung) to `Step N` (top rung) within any Era Ladder is defined **strictly from the perspective of the human user** — **NOT** by how complex the task is in the abstract, nor by how large or smart the AI model is internally, nor by how complex a vendor's hidden backend workflow is. **Going "up" means the human user is more sophisticated in their AI usage, climbing a Practitioner Skill Tree**:
  1. **Learning & Applying More AI-Specific Skills ($\Delta\text{Skill}$):** A user at a higher rung must learn and actively apply specialized AI knowledge — progressing from *zero AI training (typing a plain sentence or pressing `Tab`)* $\to$ *deliberate prompt engineering (few-shot demonstrations, stop tokens, system personas, chain-of-thought, structured research briefs)* $\to$ *context, guardrail & protocol engineering (chunking, vector indexing, `.cursorrules`, `NeMo Guardrails` policy rails, `MCP` JSON configs, `SKILL.md` playbooks)* $\to$ *specification & verification harness architecture (`CLAUDE.md`, `AGENTS.md`, fast `pytest` suites, `LangGraph` state machines, `QLoRA` training scripts)* $\to$ *multi-agent swarm orchestration & RLVR reward engineering*.
  2. **Opening, Installing & Operating Specialized Tools Beyond the Web Browser ($\Delta\text{Surface}$):** A user at a lower rung works inside a zero-install **web browser** or built-in default box (`ChatGPT` web, `Claude.ai`, one-click `Tab`), whereas climbing up the ladder requires installing, configuring, and operating progressively more specialized software surfaces: **Web Browser / Embedded Product UI** (`Step 1`) $\to$ **Browser Playground / Curated Project Workspace / API Wrapper** (`Step 2`: `OpenAI Playground`, `Claude Projects`, `Deep Research`) $\to$ **Specialized AI-Native IDE or Local RAG/MCP/Guardrail SDK Stack** (`Step 3`: `Cursor`, `Windsurf`, `LangChain`/`LlamaIndex` + vector DB + `NeMo Guardrails`, local `MCP` hosts) $\to$ **Command-Line Terminal (`CLI`) & Programmatic State/Eval Harnesses** (`Step 4`: `Claude Code` CLI, `Codex CLI`, `LangGraph`, `Braintrust`/`Promptfoo` CI evals, `PEFT` CLI) $\to$ **Multi-Branch `git worktree` Swarms & 24/7 Self-Hosted Agent Daemons** (`Step 5`: `OpenClaw`, parallel `Claude Code` fleets, `TRL`/`GRPO` clusters).
  3. **Investing More Setup Time & Non-Compute Resources / Hardware ($\Delta\text{Setup}$):** Ideally, for a user at a lower rung to operate at a higher rung, they must **spend more setup/configuration time** or **acquire/configure non-compute physical or environment resources** — such as provisioning isolated Docker/devcontainer/VM sandboxes (so an autonomous CLI agent with `--dangerously-skip-permissions` cannot destroy their primary work laptop), configuring local `Tailscale` mesh networks and OAuth 2.1 `MCP` servers, buying a **dedicated local GPU workstation (`RTX 3090/4090`)**, or **buying a dedicated Apple M4 / M4 Pro Mac Mini** to run 24/7 headless `OpenClaw` and `Claude Code` agent sandboxes!
* **The Two-Track User Skill Tree & The Producer–Consumer Asymmetry (Internal Company Chatbots & AI-Integrated Products Like `Grammarly`):** Every rung of the User Skill Tree simultaneously accommodates two distinct practitioner tracks that are linked by a fundamental **Producer–Consumer Asymmetry**:
  * **Track A — Direct Personal-Output Users (*AI-as-Co-Worker*):** Practitioners who climb `Steps 1` $\to$ `5` to generate their *own* personal work output (writing emails, researching reports, coding features, running personal `Claude Code` or `OpenClaw` agent fleets).
  * **Track B — AI Product & Internal Platform Builders (*AI-as-Product-Component / Compound AI Builders*):** Engineers and platform teams who climb **`Steps 2` $\to$ `5`** not to get a one-off personal answer, but to **embed AI/LLMs inside an internal company chatbot** (connected via private company RAG, specific tool/API calls, role-based access control [RBAC], and prompt/guardrail engineering to comply with corporate policy) or **inside an external AI-integrated SaaS product** (such as `Grammarly`, `Notion AI`, `Klarna Assistant`, or `Harvey`):
    * **At `Step 2` (*API Wrapper & System-Prompt Policy Builder*):** Wrapping a single model API call behind a product UI with hidden system prompts, policy instructions, structured JSON schemas, and input/output moderation (`Custom GPTs`, early `Jasper` wrappers).
    * **At `Step 3` (*Internal Company RAG + Tool-Calling + Policy Guardrail Chatbot Builder*):** Wiring internal corporate documents (`SharePoint`, `Confluence` via `LangChain`/`LlamaIndex` + `Pinecone` hybrid RAG with RBAC permissions) + specific authorized tools/APIs (`ServiceNow`, `Workday`, `Salesforce` via function-calling or `MCP` servers) + programmable policy and safety guardrails (`NVIDIA NeMo Guardrails`, `Meta Llama Guard`, `Guardrails AI` for PII redaction and topical compliance) into an internal employee chatbot (e.g., *Morgan Stanley's* advisor assistant, *Walmart's* `MyAssistant`) or SaaS feature.
    * **At `Step 4` (*Stateful Multi-Step Product Backend, Custom Fine-Tuned Product Model & Eval-Driven CI/CD Engineer*):** Building deterministic state-machine product backends (`LangGraph`, Anthropic Predefined Workflows with hard refund/policy gates at `L4-S4`), fine-tuning custom low-latency product models (**Grammarly's** `GECToR` encoder tagger at `L1-S3`/`L2-S4` and `CoEdIT` instruction-tuned `Flan-T5` editor at `L3-S4`), and engineering automated CI/CD evaluation & policy red-teaming suites (`Braintrust`, `Promptfoo`, `LangSmith`, Shankar & Husain's *Eval-Driven Development*) so the deployed chatbot cannot violate company policy in production.
    * **At `Step 5` (*Product Telemetry Flywheel, Custom RLVR / Distillation & Autonomous Platform Architect*):** Harvesting millions of production user interaction traces (accept/reject clicks in `Grammarly` or `Cursor`, verified ticket resolutions) to run custom `DPO` (`L4-S5`) or `GRPO` RLVR post-training and student-model distillation flywheels (`L5-S5`), serving custom 7B–32B product models on `vLLM`/`TensorRT-LLM` at $1/20\text{th}$ the cost.
  * **Where the End-Users of Internal Company Chatbots & AI-Integrated Products (`Grammarly`) Fit $\to$ Strictly at `Step 1` (`Zero-Setup Default UI`):** Crucially, while the **Builders** of `Grammarly`, `Notion AI`, or an internal company RAG + Tool + Policy chatbot operate at **`Steps 3, 4, and 5`**, the **End-Users (Consumers) of those products** (the 40M+ writers clicking a `Grammarly` underline, the 16,000 Morgan Stanley advisors querying the internal bot, or the 2.3M Klarna customers chatting with support) sit strictly at **`Step 1`**! From the end-user's perspective, asking the internal company Slack bot a question or clicking `Grammarly` requires **zero AI skill ($\Delta\text{Skill}=0$)**, **zero specialized tool installation ($\Delta\text{Surface}=0$)**, and **zero setup time ($\Delta\text{Setup}=0$)**. This **Producer–Consumer Step-Compression Bridge** (where `Step 3–5` builders package RAG, tools, and policy guardrails into a `Step 1` interface for millions of end-users) is the exact human mechanism that powers **Law 1 (The Downward Sinking Law)**.

***

## 2. Literature, News & Cost Survey Directives

**Section 2 Overview:** Reviews all published and informal AI ladders (`2017–2026`, including the *Gemini Deep Research 23-Step Historical AI Ladder* and *Berkeley BAIR's Compound AI Systems & Guardrailed Product Architecture*) purely as existing literature (`Section 2.1`, reserving the head-to-head comparison against our own ladder for `Section 5.3` at the end of the report), gathers annual AI reports, paid API billing logs, courses/syllabi, developer surveys, and front-page news milestones ("who did what") (`Section 2.2`), and defines the five-unit, two-level cost accounting framework (`Section 2.3`).

#### Section 2 Structural Index
* [2.1 Review of Existing Published & Informal AI Ladders (Pure Literature Survey)](#21-review-of-existing-published--informal-ai-ladders-pure-literature-survey)
  * [2.1.1 Academic & AI Lab Ladders](#211-academic--ai-lab-ladders)
  * [2.1.2 Industry, Enterprise & Self-Driving Coding Ladders (Including Gemini Historical Ladder)](#212-industry-enterprise--self-driving-coding-ladders-including-gemini-historical-ladder)
  * [2.1.3 Developer, Practitioner & Compound AI Product Hierarchies](#213-developer-practitioner--compound-ai-product-hierarchies)
* [2.2 Step Use-Case Sources: Reports, Traffic Logs, Courses, Surveys & News](#22-step-use-case-sources-reports-traffic-logs-courses-surveys--news)
  * [2.2.1 Annual Macro AI Reports (Stanford HAI, State of AI, Epoch AI)](#221-annual-macro-ai-reports-stanford-hai-state-of-ai-epoch-ai)
  * [2.2.2 Paid API Traffic & Enterprise Billing Logs (Menlo, OpenRouter, Ramp)](#222-paid-api-traffic--enterprise-billing-logs-menlo-openrouter-ramp)
  * [2.2.3 Educational Curricula, University Syllabi & Code Cookbooks](#223-educational-curricula-university-syllabi--code-cookbooks)
  * [2.2.4 Developer Surveys & Yearly News Milestones ("Who Did What")](#224-developer-surveys--yearly-news-milestones-who-did-what)
* [2.3 Single-Task vs. Industry-Wide Resource Metrics & Fallback Math](#23-single-task-vs-industry-wide-resource-metrics--fallback-math)
  * [2.3.1 Five Candidate Measurement Units & Trade-Offs](#231-five-candidate-measurement-units--trade-offs)
  * [2.3.2 Historical API Token Pricing & Prompt Caching Baseline (2020–2026)](#232-historical-api-token-pricing--prompt-caching-baseline-20202026)
  * [2.3.3 Two-Level Cost System & Three-Step Rough-Math Fallback Protocol](#233-two-level-cost-system--three-step-rough-math-fallback-protocol)

### 2.1 Review of Existing Published & Informal AI Ladders (Pure Literature Survey)

**Cataloging 20 Existing Frameworks as Pure Literature:** Catalogs and reviews all 20 influential AI, LLM, agentic, and compound-product ladders across research labs, industry/VC, practitioner communities, and prior historical syntheses (`Table 2.1` and `Figure 5`). **Important Sequencing Rule:** Do NOT prematurely compare these existing ladders against our own ladder in `Section 2.1`; first construct our own 5-Era, 23-Step User Skill-Tree Ladder in `Parts III–IV`, and then perform the comprehensive cross-walk and head-to-head comparison in **`Section 5.3` (`Part V`)** at the end of the report.

#### 2.1.1 Academic & AI Lab Ladders

* **Frontier Lab & Research Hierarchies:** Review ladders from research papers and leading AI labs — Andrej Karpathy's *Software 1.0/2.0/3.0 & Autonomy Slider* (`2017-11` to `2025-06`), Google DeepMind's *Levels of AGI* (`2023-11`, Morris et al. 2D Performance $\times$ Autonomy matrix), OpenAI's *5 Levels of AGI* (`2024-07`: Chatbots, Reasoners, Agents, Innovators, Organizations — calibrated at Level 2.5 in 2026), Anthropic's *Building Effective Agents* (`2024-12`: Single Augmented LLM, 5 Predefined Workflows, Open-Ended Autonomous Agents), and academic cognitive architectures (*Lilian Weng* `2023-06`, Princeton *CoALA* `2023-09`, *Andrew Ng's 4 Agentic Design Patterns* `2024-03`).

#### 2.1.2 Industry, Enterprise & Self-Driving Coding Ladders (Including Gemini Historical Ladder)

* **Coding Autonomy, Enterprise Maturity & Prior Historical Scales:** Review self-driving car scales (SAE Levels 0–5) adapted for AI coding and enterprise agents — Dan Shapiro's *Five Levels of AI Coding* (`2026-01`, L0 Manual to L5 Dark Factory), Steve Yegge's *8-Rung Coding Agent Evolution / Gas Town* (`2025-02` to `2026-01`), Harrison Chase / *LangChain Cognitive Architectures & Deep Agents* (`2023-11` to `2026-03`), *Hugging Face `smolagents` Agency Levels* (`2024-12`), venture capital frameworks (*a16z*, *Sequoia*, *Menlo Ventures*), *Gartner 5-Level AI Maturity Model* (`2019–2026`), and the *Gemini Deep Research 5-Era / 23-Step Historical AI Ladder* ($L_1^{\text{Gem}}\dots L_5^{\text{Gem}}$, `2018-10` to `2026-10`) treated explicitly as an existing literature ladder.

#### 2.1.3 Developer, Practitioner & Compound AI Product Hierarchies

* **Cost-vs-Control Engineering, Compound AI Systems, Guardrails & Embedded Product Ladders:** Review practitioner hierarchies governing how engineers integrate AI/LLMs into internal company chatbots and commercial products:
  * **Transfer Learning & Prompt-RAG-FineTune Ladders:** Sebastian Ruder's *NLP Transfer Learning Hierarchy* (`2018-07`), Pre-train/Prompt/Predict (*Liu et al.* `2021-07`), and the *Prompt Engineering $\to$ Evals $\to$ RAG $\to$ Fine-Tuning Intervention Hierarchy* (*Chip Huyen* `2023–2025` *AI Engineering*, *Eugene Yan* `2023-08`, *OpenAI DevDay* `2023-11` by John Allard & Colin Jarvis).
  * **Compound AI Systems, Programmable Policy Guardrails & Embedded Product ML (`BAIR`, `NeMo Guardrails`, `Grammarly`):** Review UC Berkeley BAIR's *The Shift from Models to Compound AI Systems* (*Zaharia, Khattab, Chen, et al.* `2024-02`, defining how production AI apps combine retrievers, tools, routers, and verifiers), **Programmable Conversational & Policy Guardrails** (*Rebedea et al.* `2023-10` **`NVIDIA NeMo Guardrails`** [`arXiv:2310.10501` — input, retrieval, execution/tool, and output/topical policy rails], *Inan et al.* `2023-12` **`Meta Llama Guard`**, **`Guardrails AI`**, and **`OWASP Top 10 for LLMs`**), **Application-Centric Eval Engineering** (*Shankar, Husain, et al.* `2024-04` *Who Validates the Validators?* [`arXiv:2404.12272`]), and **Embedded SaaS Product ML** (**Grammarly's** `GECToR` [`Omelianchuk et al. 2020`, `BERT`/`RoBERTa` sequence tagging] and `CoEdIT` [`Raheja et al. 2023`, instruction-tuned `Flan-T5` text editing], alongside enterprise internal assistants at *Morgan Stanley*, *Walmart*, and *Klarna*).

### 2.2 Step Use-Case Sources: Reports, Traffic Logs, Courses, Surveys & News

**Empirical Grounding Sources:** Gathers nine years of macro reports, billing logs, courses, developer surveys, and news stories to populate the concrete use cases and cost profiles of every step.

#### 2.2.1 Annual Macro AI Reports (Stanford HAI, State of AI, Epoch AI)

* **Macro Compute & Adoption Datasets:** Pull yearly training compute (FLOPs), training cost (USD), model parameter counts, hardware epochs (`P100/V100` $\to$ `A100` $\to$ `H100/B200`), and organizational adoption rates from *Stanford HAI AI Index Report* (`2018–2026`), *State of AI Report* (Benaich & Hogarth `2018–2025`), *Epoch AI*, and *IEA Datacenter Energy Reports*.

#### 2.2.2 Paid API Traffic & Enterprise Billing Logs (Menlo, OpenRouter, Ramp)

* **Production Spend & Token Distribution:** Gather real enterprise spending and token routing shares across workflows (direct prompting vs. custom RAG vs. fine-tuning vs. MCP/agent loops) from *Menlo Ventures Enterprise GenAI Reports* (`2023–2025`), *OpenRouter State of AI 100T-Token Study* (`2025–2026`), *Ramp AI Index*, *Stripe* AI billing reports, and *Cloudflare Radar*.

#### 2.2.3 Educational Curricula, University Syllabi & Code Cookbooks

* **What Practitioners Learned Each Year ("Top Thing to Learn"):** Track the flagship courses, university syllabi, and code cookbooks from each year (`2017–2026`) — *Stanford CS224N* (Manning), *Stanford CS324* (Liang & Hashimoto), *Fast.ai Practical Deep Learning* (Howard), *Hugging Face NLP & Agents Courses*, *DeepLearning.AI Short Courses* (Ng, Fulford, Chase, Moura, Schoppik), *OpenAI Cookbook*, and *Anthropic Prompt Engineering / MCP / Claude Code Best Practices Guides* — identifying the **#1 Top Skill to Learn** in every era.

#### 2.2.4 Developer Surveys & Yearly News Milestones ("Who Did What")

* **Developer Habits & Front-Page Wins/Failures:** Combine annual *Stack Overflow Developer Surveys* (`2017–2025`) and *GitHub Octoverse* reports with every year's headline real-world AI wins and cautionary failures ("who did what") so every ladder step and the dedicated News & Learning Poster (`fig_era_defining_news_and_learning_poster.png`) are anchored in concrete historical events.

### 2.3 Single-Task vs. Industry-Wide Resource Metrics & Fallback Math

**Two-Level Five-Unit Cost System:** Evaluates five coupled measurement units across single-task execution (Level 1) and whole-era industry share (Level 2).

#### 2.3.1 Five Candidate Measurement Units & Trade-Offs

* **Five Mandatory Units:** Measure every step across all five units to eliminate single-unit blind spots:
  1. **Text Chunks (`Tokens`):** Input context + cached reads + output + internal thinking tokens ($\approx 0.75$ words/token; $10^2$ for autocomplete to $10^7+$ for parallel agent fleets).
  2. **Math Operations (`FLOPs`):** Forward-pass inference math ($\approx 2 N_{\text{active}} T_{\text{task}}$) plus custom training math ($\approx 6 N_{\text{params}} D_{\text{tokens}}$).
  3. **Electricity (`Wh` per task / `MWh` or `TWh` per era):** Grounded in verified hardware benchmarks ($0.24–0.34\text{ Wh}$ per short chat turn in 2025 [OpenAI / Google / Epoch AI] vs. $18–150\text{ Wh}$ per deep research or multi-agent coding run).
  4. **Money (`USD`):** Marginal per-task API/GPU cost and era-wide enterprise + consumer expenditure.
  5. **Human-vs-AI Time (`Minutes` per task / `Hours` per era):** Active human framing, prompting, and PR verification time vs. autonomous AI execution runtime.

#### 2.3.2 Historical API Token Pricing & Prompt Caching Baseline (2020–2026)

* **Six-Year Price Deflation Baseline:** Compile exact per-1M-token input, cached input (KV-cache hit, 50%–90% discount introduced in mid-2024), and output prices from `2020-06` `GPT-3 davinci` ($\$60.00/1\text{M}$) and `2023-03` `gpt-3.5-turbo` ($\$2.00/1\text{M}$) down to `2024–2026` `Claude 3.5/4.5 Sonnet` ($\$3.00$ input / $\$0.30$ cached), `gpt-4o-mini` ($\$0.15/1\text{M}$), `DeepSeek-V3/R1` ($\$0.14–\$0.55/1\text{M}$), `o1`/`o3`, and `Gemini 1.5/2.5 Flash` ($\$0.075–\$0.15$ input, $\$0.018–\$0.0375$ cached).

#### 2.3.3 Two-Level Cost System & Three-Step Rough-Math Fallback Protocol

* **Three-Step Estimation Sequence:** For every step metric, follow a strict 3-step sequence: (1) use direct published figures from primary reports when available, (2) apply survey and API traffic proxies (*Stack Overflow*, *Menlo Ventures*, *OpenRouter*) when step-level splits are omitted, and (3) compute transparent back-of-the-envelope equations verifying that **industry-wide User Share %, Human-Hour Share %, Compute/Token Share %, and USD Spend Share % each sum to exactly $100.0\%$ within every Era Ladder**:
  $$\sum_{k=1}^{K_t} s_{\text{users}}(k,t) = 100\%, \quad \sum_{k=1}^{K_t} s_{\text{tokens}}(k,t) = 100\%, \quad \sum_{k=1}^{K_t} s_{\text{USD}}(k,t) = 100\%$$

***

## 3. How to Build the Ladders (Four-Rule Protocol)

**Section 3 Overview:** Establishes the four deterministic rules for locking era cutoff dates (`YYYY-MM`), reconciling bottom-up user workflows against published ladders, verifying mutually exclusive and collectively exhaustive (MECE) step boundaries along the **Three User Skill-Tree Axes**, and linking steps across eras.

#### Section 3 Structural Index
* [3.1 Rule 1: Two-Shift Era Cutoff Threshold](#31-rule-1-two-shift-era-cutoff-threshold)
  * [3.1.1 Simultaneous Two-Step Structural Shift Equation](#311-simultaneous-two-step-structural-shift-equation)
  * [3.1.2 Candidate Cutoff Audit (Accepted vs. Rejected Milestones)](#312-candidate-cutoff-audit-accepted-vs-rejected-milestones)
* [3.2 Rule 2: Bottom-Up & Top-Down Usage Reconciliation](#32-rule-2-bottom-up--top-down-usage-reconciliation)
  * [3.2.1 Pass 1: Bottom-Up Empirical Workflow Clustering](#321-pass-1-bottom-up-empirical-workflow-clustering)
  * [3.2.2 Pass 2: Top-Down Published Ladder Cross-Check](#322-pass-2-top-down-published-ladder-cross-check)
* [3.3 Rule 3: No-Overlap & No-Gaps (MECE) Two-of-Three User Skill-Tree Split Test](#33-rule-3-no-overlap--no-gaps-mece-two-of-three-user-skill-tree-split-test)
  * [3.3.1 Three User Skill-Tree Separation Axes (Learned Skill, Tool Surface, Setup/Hardware)](#331-three-user-skill-tree-separation-axes-learned-skill-tool-surface-setuphardware)
  * [3.3.2 Full Adjacency Verification Matrix Across All Era Ladders](#332-full-adjacency-verification-matrix-across-all-era-ladders)
* [3.4 Rule 4: Cross-Era Linkage & Convergence Lock](#34-rule-4-cross-era-linkage--convergence-lock)
  * [3.4.1 Five Cross-Era Transition Categories](#341-five-cross-era-transition-categories)
  * [3.4.2 Locked Master Skeleton Table & Mermaid Flowchart](#342-locked-master-skeleton-table--mermaid-flowchart)

### 3.1 Rule 1: Two-Shift Era Cutoff Threshold

**Locking Era Boundaries:** Prevents single-model hype from fragmenting the timeline by requiring at least two simultaneous structural step changes on the User Skill Tree to open a new Era Ladder.

#### 3.1.1 Simultaneous Two-Step Structural Shift Equation

* **Two-Shift Cutoff Criterion:** Open a new Era Ladder $L_t$ at month $\tau$ only when a technical breakthrough or $\ge 10\times$ unit price drop causes at least two structural step transitions at once on the User Skill Tree:
  $$\Delta_{\text{structural}}(\tau) = \mathbb{I}(\text{Old Higher Skill-Tree Step Sinks to Zero-Setup Step 1}) + \mathbb{I}(\text{Existing Step Splits/Combines}) + \mathbb{I}(\text{New Top User Skill-Tree Step Emerges}) \ge 2$$

#### 3.1.2 Candidate Cutoff Audit (Accepted vs. Rejected Milestones)

* **Audit Table & Visual:** Document both the accepted production-crossover era cutoffs (`2017-06` $L_1$, `2020-06` $L_2$, `2022-11` $L_3$, `2024-06` $L_4$, `2025-02` $L_5$), their precursor release bridges (`2018-10` BERT, `2023-11` GPT-4 Turbo 128k / Claude 2.1 200k, `2024-09` OpenAI o1-preview), and rejected single-step milestones (`2019-02` `GPT-2` staged release, `2024-03` `Claude 3` release).

### 3.2 Rule 2: Bottom-Up & Top-Down Usage Reconciliation

**Dual-Pass Step Discovery:** Combines empirical user-habit clustering with published ladder cross-checks.

#### 3.2.1 Pass 1: Bottom-Up Empirical Workflow Clustering

* **User-Sophistication Grouping:** Cluster real user practices found in each era's courses, cookbooks, developer surveys, API billing logs, and news stories into natural **User Skill-Tree tiers** based on what skills users actually had to learn, what tools they had to install (browser vs. IDE vs. CLI), and what environments/hardware they had to set up.

#### 3.2.2 Pass 2: Top-Down Published Ladder Cross-Check

* **Cross-Check Decisions:** Reconcile Pass 1 clusters against the 19 published ladders to: (1) adopt clear standard names where they match, (2) retain practical high-volume user steps that model-centric corporate ladders missed (such as $L_1$ Step 1 turnkey cloud NLP APIs, $L_2$ Step 1 one-keystroke Copilot `Tab`, and $L_5$ Step 2 structured `Deep Research` specification), and (3) exclude speculative unverified rungs.

### 3.3 Rule 3: No-Overlap & No-Gaps (MECE) Two-of-Three User Skill-Tree Split Test

**Within-Era User Skill-Tree Separation:** Enforces strict mutually exclusive and collectively exhaustive (MECE) step boundaries inside every Era Ladder based on **complexity from the perspective of the user**.

#### 3.3.1 Three User Skill-Tree Separation Axes (Learned Skill, Tool Surface, Setup/Hardware)

* **Two-of-Three User Skill-Tree Split Equation:** Separate two usage patterns into distinct steps ($k$ vs. $k+1$) only when moving up from Step $k$ to Step $k+1$ requires the human user to advance on **at least 2 of 3 User Skill-Tree variables**:
  $$\text{SplitScore}(S_k \to S_{k+1}) = \mathbb{I}(\Delta\text{Skill} = 1) + \mathbb{I}(\Delta\text{Surface} = 1) + \mathbb{I}(\Delta\text{Setup} = 1) \ge 2$$
  1. **Axis 1 — Learned AI-Specific Skill & Technique ($\Delta\text{Skill} = 1$):** The user must learn and apply a new tier of AI-specific knowledge — e.g., moving from *zero AI training (natural chat or `Tab`)* $\to$ *deliberate prompt engineering (few-shot examples, stop sequences, system personas, research-brief specification)* $\to$ *context, retrieval & protocol wiring (`.cursorrules`, RAG chunking/reranking, `MCP` server configuration, `SKILL.md`)* $\to$ *specification & verification harness architecture (`CLAUDE.md`, `AGENTS.md`, `pytest` verifiers, `LangGraph` state graphs, `QLoRA` scripts)* $\to$ *parallel multi-agent swarm orchestration & custom RLVR post-training*.
  2. **Axis 2 — Specialized Tool & Environment Surface ($\Delta\text{Surface} = 1$):** The user must leave the simpler interface and install/open a more specialized software environment — e.g., moving from *Zero-Install Web Browser / Default Plugin* $\to$ *Browser API Playground / Curated Project Workspace* $\to$ *Specialized AI-Native IDE (`Cursor`, `Windsurf`) or Local Python SDK* $\to$ *Terminal CLI (`Claude Code`, `Codex CLI`) or Programmatic State Graph* $\to$ *Parallel Multi-Branch `git worktree` Terminals or 24/7 Self-Hosted Agent Daemons (`OpenClaw`)*.
  3. **Axis 3 — Upfront User Setup Time & Non-Compute Hardware/Sandbox Commitment ($\Delta\text{Setup} = 1$):** The user must invest substantially more setup time or acquire/configure **non-compute physical or environment resources** — e.g., moving from *zero setup ($0\text{ min}$)* $\to$ *multi-minute prompt/document curation* $\to$ *local IDE, vector database (`FAISS`/`Pinecone`), or `.mcp.json` server installation* $\to$ *isolated Docker/VM/devcontainer test-sandbox provisioning or single-GPU (`RTX 3090/4090`) rig setup* $\to$ *buying a **dedicated Apple M4 / M4 Pro Mac Mini** (with an isolated user account and `Tailscale` mesh network to run 24/7 `--dangerously-skip-permissions` `OpenClaw` / `Claude Code` agent sandboxes safely off one's main laptop) or provisioning multi-worktree/multi-GPU cluster infrastructure*.

#### 3.3.2 Full Adjacency Verification Matrix Across All Era Ladders

* **18-Boundary Audit Table:** Test every adjacent step pair ($S_k \to S_{k+1}$) across all five Era Ladders in a complete verification table and heatmap confirming $\text{SplitScore} \ge 2/3$ across $\Delta\text{Skill}$, $\Delta\text{Surface}$, and $\Delta\text{Setup}$ on every boundary.

### 3.4 Rule 4: Cross-Era Linkage & Convergence Lock

**Cross-Era Lineage:** Connects every step in $L_t$ to its precursor(s) in $L_{t-1}$.

#### 3.4.1 Five Cross-Era Transition Categories

* **Transition Taxonomy:** Classify every step's cross-era origin into one of five categories: (1) **Old Higher Skill-Tree Step Sinking into Zero-Setup Default Step 1 UI** (vendor absorbs the user setup/skill friction), (2) **Evolved Core Workhorse Step**, (3) **Split & Specialized Step**, (4) **New Breakthrough Top Skill-Tree Step**, or (5) **Combined or Gone Step**.

#### 3.4.2 Locked Master Skeleton Table & Mermaid Flowchart

* **Master Skeleton Lock:** Present the locked 5-era, 23-step master table, a full-timeline Mermaid structural lineage diagram, and a cross-era trajectory figure before beginning the Part IV per-era deep dives.

***

## 4. Ladder Evolution Directives (Per-Era Architecture)

**Section 4 Overview:** Specifies the required analysis for each chronological Era Ladder ($L_1 \dots L_5$) — covering exact valid dates (`YYYY-MM`), why the old ladder got outdated, how user skill-tree steps changed, era-defining news ("who did what") and top skills to learn, and full-ladder resource totals.

#### Section 4 Structural Index
* [4.1 Era Dates & Why Old Ladders Get Outdated (Tech, Cost & Habit Shifts)](#41-era-dates--why-old-ladders-get-outdated-tech-cost--habit-shifts)
  * [4.1.1 Exact Valid Window (`YYYY-MM` to `YYYY-MM`) & Duration in Months](#411-exact-valid-window-yyyy-mm-to-yyyy-mm--duration-in-months)
  * [4.1.2 Technical, Economic & Workflow Shifts Breaking the Old Ladder](#412-technical-economic--workflow-shifts-breaking-the-old-ladder)
* [4.2 How Steps Change Between Eras (Sunk, Evolved, Split, New & Gone)](#42-how-steps-change-between-eras-sunk-evolved-split-new--gone)
  * [4.2.1 Step-by-Step Transition Analysis ($L_{t-1} \to L_t$)](#421-step-by-step-transition-analysis-l_t-1-to-l_t)
  * [4.2.2 In-Section ASCII / Visual Ladder Transition Diagram](#422-in-section-ascii--visual-ladder-transition-diagram)
* [4.3 Era-Defining Moments: Tech Triggers, News ("Who Did What") & Top Skill to Learn](#43-era-defining-moments-tech-triggers-news-who-did-what--top-skill-to-learn)
  * [4.3.1 Tech That Starts vs. Ends the Era](#431-tech-that-starts-vs-ends-the-era)
  * [4.3.2 Headline Real-World Wins & Cautionary Failures ("Who Did What")](#432-headline-real-world-wins--cautionary-failures-who-did-what)
  * [4.3.3 Top Thing to Learn Per Era (#1 Skill & Flagship Courses)](#433-top-thing-to-learn-per-era-1-skill--flagship-courses)
* [4.4 Full-Ladder Era Resource Totals & Conservation Checks](#44-full-ladder-era-resource-totals--conservation-checks)
  * [4.4.1 Aggregate Compute, Electricity, Spending, Tokens & Human-Hours](#441-aggregate-compute-electricity-spending-tokens--human-hours)
  * [4.4.2 Era Summary Table & 3-Panel Era Ladder Figure](#442-era-summary-table--3-panel-era-ladder-figure)

### 4.1 Era Dates & Why Old Ladders Get Outdated (Tech, Cost & Habit Shifts)

**Drivers of Era Transitions:** Documents each ladder's exact valid dates and the technical, economic, and user-habit shifts that made the prior skill tree outdated.

#### 4.1.1 Exact Valid Window (`YYYY-MM` to `YYYY-MM`) & Duration in Months

* **Evidence-Based Era List:** Lock the exact valid window and duration in months for each Era Ladder:
  * **Era 1 ($L_1$):** `2017-06` to `2020-05` (**36 months**) — *Pre-LLM & Transfer-Learning NLP Skill-Tree Ladder*.
  * **Era 2 ($L_2$):** `2020-06` to `2022-10` (**29 months**) — *Completion Playgrounds & Early Copilot Skill-Tree Ladder*.
  * **Era 3 ($L_3$):** `2022-11` to `2024-05` (**19 months**) — *Conversational Web Chat, Custom Vector RAG & Early Agent Sandboxes Skill-Tree Ladder*.
  * **Era 4 ($L_4$):** `2024-06` to `2025-01` (**8 months**) — *Built-In Multimodal Context, Specialized AI IDEs (`Cursor`) & State-Graph Skill-Tree Ladder*.
  * **Era 5 ($L_5$):** `2025-02` to `2026-10` (**21 months**) — *Auto-Routed Chat, `MCP` Ecosystems, Terminal CLI Agents (`Claude Code`) & Dedicated Hardware/Worktree Swarms (`Mac Mini` / `OpenClaw`) Skill-Tree Ladder*.

#### 4.1.2 Technical, Economic & Workflow Shifts Breaking the Old Ladder

* **Three Shift Pillars:** For each era, detail: (1) **Technical Changes** (attention/encoders, zero/few-shot scaling, RLHF chat, 200k–2M multimodal context, 90% KV-cache, RLVR test-time compute, tool-integrated RLVR, `MCP`, CLI harnesses), (2) **Economic Changes** ($10\times–100\times$ token price drops, flat subscriptions, KV-cache billing), and (3) **User Skill-Tree & Surface Shifts** (how old engineering skills sank into default browser UIs while new upper rungs demanded specialized IDEs, terminal CLIs, isolated Docker sandboxes, or dedicated M4 Mac Mini home servers).

### 4.2 How Steps Change Between Eras (Sunk, Evolved, Split, New & Gone)

**Cross-Era Step Mechanics:** Traces every structural transition between $L_{t-1}$ and $L_t$.

#### 4.2.1 Step-by-Step Transition Analysis ($L_{t-1} \to L_t$)

* **Four Transition Mechanics:** Explicitly trace: (1) **Old Steps Sinking into Default Step 1 Browser UI** (vendor eliminates the prior user skill/setup requirement), (2) **Evolved Core Workhorse Steps**, (3) **Split Steps** (diverging by tool surface or setup requirement), and (4) **New Top Skill-Tree Steps** or **Combined/Gone Steps**.

#### 4.2.2 In-Section ASCII / Visual Ladder Transition Diagram

* **Side-by-Side Mapping:** Include a clear side-by-side structural transition diagram mapping every step of $L_{t-1}$ to $L_t$ at the start of each era's step-change subsection.

### 4.3 Era-Defining Moments: Tech Triggers, News ("Who Did What") & Top Skill to Learn

**Historical & Educational Anchors:** Captures the era-defining moments that ground both the per-era prose and the full-timeline News & Learning Poster (`fig_era_defining_news_and_learning_poster.png`).

#### 4.3.1 Tech That Starts vs. Ends the Era

* **Opening & Closing Tech:** Document the exact architectural/API launch that starts the era and the exact structural bottleneck + successor breakthrough that ends/outdates it.

#### 4.3.2 Headline Real-World Wins & Cautionary Failures ("Who Did What")

* **Who Did What (Wins vs. Failures):** Document the era's most famous front-page real-world wins (company, date `YYYY-MM`, quantitative outcome) and most famous cautionary failures, legal sanctions, or market shocks.

#### 4.3.3 Top Thing to Learn Per Era (#1 Skill & Flagship Courses)

* **Era Curriculum Anchor:** Identify the single most important practical skill a user or developer needed to unlock on the era's skill tree (`#1 Skill`), the flagship courses teaching it, and the concrete daily workflow action.

### 4.4 Full-Ladder Era Resource Totals & Conservation Checks

**Macro Era Accounting:** Compiles whole-era resource totals and verifies 100% MECE share conservation.

#### 4.4.1 Aggregate Compute, Electricity, Spending, Tokens & Human-Hours

* **Era-Wide Totals:** Estimate total training + inference compute (`FLOPs`), datacenter electricity (`MWh` / `TWh`), cumulative expenditure (`USD`), global token volume (`Tokens`), and active users + human-hours across the era's valid window.

#### 4.4.2 Era Summary Table & 3-Panel Era Ladder Figure

* **Per-Era Table & Figure (`fig_era1_ladder.png` to `fig_era5_ladder.png`):** Close each era section (`4.1` to `4.5`) with: (1) a complete 12-column Markdown summary table across all steps of $L_t$ (verifying that User %, Human-Hour %, Compute/Token %, and Spend % each sum to `100%`), and (2) a dedicated 3-panel `matplotlib` Era Ladder figure.

***

## 5. Steps in a Ladder (Five-Part User Skill-Tree Step Profile)

**Section 5 Overview:** Mandates a uniform five-part analytical profile for every individual user skill-tree step (`Step 1` through `Step N`) across all five Era Ladders (23 total steps).

#### Section 5 Structural Index
* [5.1 Step Name, Rank & User Skill-Tree Boundaries](#51-step-name-rank--user-skill-tree-boundaries)
  * [5.1.1 Bottom-to-Top User Sophistication Rank & Descriptive Name](#511-bottom-to-top-user-sophistication-rank--descriptive-name)
  * [5.1.2 Skill-Tree Entry Floor (vs. Step $k-1$) & Upper Ceiling (vs. Step $k+1$)](#512-skill-tree-entry-floor-vs-step-k-1--upper-ceiling-vs-step-k1)
* [5.2 Concrete Tool Stack, Use Cases & Same-User Context Switching](#52-concrete-tool-stack-use-cases--same-user-context-switching)
  * [5.2.1 Exact Era Models, Specialized Interfaces (Browser/IDE/CLI) & Setup Hardware](#521-exact-era-models-specialized-interfaces-browseridecli--setup-hardware)
  * [5.2.2 Grounded Use Cases (Reports, Courses, Surveys, Wins & Failures)](#522-grounded-use-cases-reports-courses-surveys-wins--failures)
  * [5.2.3 Same-Persona Multi-Step Context Switching Along the Skill Tree](#523-same-persona-multi-step-context-switching-along-the-skill-tree)
* [5.3 Two-Level Step Resource Accounting & Machine-Readable Row](#53-two-level-step-resource-accounting--machine-readable-row)
  * [5.3.1 Level 1: Single-Task Resource Footprint (5 Units)](#531-level-1-single-task-resource-footprint-5-units)
  * [5.3.2 Level 2: Industry-Wide Era Share Percentages (Summing to 100%)](#532-level-2-industry-wide-era-share-percentages-summing-to-100)

### 5.1 Step Name, Rank & User Skill-Tree Boundaries

**User Skill-Tree Positioning:** Defines each step's bottom-to-top user-sophistication rank and exact skill, tool-surface, and setup/hardware boundaries.

#### 5.1.1 Bottom-to-Top User Sophistication Rank & Descriptive Name

* **Name & Rank:** Number steps from `Step 1` (lowest user-side complexity: zero-install web browser or default 1-click surface requiring zero AI-specific training or setup) at the bottom up to `Step N` (highest user-side complexity: maximum learned AI skill, specialized IDE/CLI/daemon surfaces, and dedicated sandbox or physical hardware setup such as a dedicated Mac Mini or GPU rig) at the top.

#### 5.1.2 Skill-Tree Entry Floor (vs. Step $k-1$) & Upper Ceiling (vs. Step $k+1$)

* **User Skill-Tree Step Boundaries:** Explicitly state: (1) **What a User at Step $k-1$ Must Learn, Install, or Buy/Configure to Climb to Step $k$ (`Entry Floor`)** across learned AI skill ($\Delta\text{Skill}$), specialized software surface ($\Delta\text{Surface}$: e.g., moving from web browser to `Cursor` IDE or `Claude Code` terminal CLI), and non-compute setup/hardware commitment ($\Delta\text{Setup}$: e.g., configuring `.mcp.json`, provisioning Docker/VM sandboxes, or buying a dedicated M4 Mac Mini / RTX 4090 box); and (2) **What Skill or Setup Barrier Separates Step $k$ from Step $k+1$ Above It (`Upper Ceiling`)**.

### 5.2 Concrete Tool Stack, Use Cases & Same-User Context Switching

**Tools & Real-World Practice:** Populates every step with exact software/hardware stacks, historical evidence, and same-user skill-tree switching.

#### 5.2.1 Exact Era Models, Specialized Interfaces (Browser/IDE/CLI) & Setup Hardware

* **Concrete Tool & Setup Stack:** Name the exact models (`BERT`, `davinci`, `gpt-3.5-turbo`, `GPT-4`, `Claude 3.5/4.6 Sonnet`, `o1`/`o3`, `DeepSeek-R1`, `GPT-5.4`), user interfaces and libraries (`Web Browser`, `OpenAI Playground`, `Cursor Composer`, `Windsurf`, `LangChain`, `LlamaIndex`, `LangGraph`, `PEFT`/`QLoRA`, `Claude Code` CLI, `OpenClaw`), and non-compute setup/hardware environments (`Docker`/`devcontainer` sandboxes, `git worktree` repos, `Tailscale` mesh networks, local `RTX 3090/4090` rigs, and dedicated **Apple M4 / M4 Pro Mac Mini** 24/7 agent servers) used at Step $k$.

#### 5.2.2 Grounded Use Cases (Reports, Courses, Surveys, Wins & Failures)

* **Evidence-Backed Use Cases:** Populate every step with: (1) who operates at Step $k$ and what user skill they exercise, (2) specific courses/cookbooks teaching Step $k$, (3) survey and API log metrics (*Stack Overflow*, *Menlo Ventures*, *OpenRouter*), and (4) famous real-world news wins and failures at Step $k$.

#### 5.2.3 Same-Persona Multi-Step Context Switching Along the Skill Tree

* **Persona Skill-Tree Switch:** Show concretely how a **high-skill practitioner** (who has already unlocked Rungs 1 through 5 of the skill tree) dynamically dials their active rung up or down on the same day depending on how much setup friction a task warrants (e.g., using Rung 1 web chat/`Tab` for a quick lookup, Rung 2 `Deep Research` for a cited brief, Rung 3 `Cursor` + `MCP` for an interactive 4-file edit, Rung 4 `Claude Code` CLI in a Docker sandbox for a 30-file refactor, and Rung 5 parallel `git worktree` swarms / `OpenClaw` on a dedicated Mac Mini for overnight multi-PR execution).

### 5.3 Two-Level Step Resource Accounting & Machine-Readable Row

**Step Cost Profile:** Quantifies both single-task cost and industry-wide share on every step.

#### 5.3.1 Level 1: Single-Task Resource Footprint (5 Units)

* **Single-Task Cost:** Report typical tokens per task ($T_{\text{task}}$), math operations ($\text{FLOPs}_{\text{task}}$), electricity ($\text{Wh}_{\text{task}}$), money ($\text{USD}_{\text{task}}$), and human setup/steering minutes vs. autonomous AI runtime minutes per task.

#### 5.3.2 Level 2: Industry-Wide Era Share Percentages (Summing to 100%)

* **Industry-Wide Share:** Report percentage share of active users, human-hours, total compute/tokens, and total USD spend at Step $k$ across that era.

***

## 6. Multi-Agent Execution & Visual Verification Pipeline

**Section 6 Overview:** Splits research, timeline locking, per-era writing, post-synthesis literature comparison, extended-summary compression, and `matplotlib` visual generation/inspection across four coordinated stages.

#### Section 6 Structural Index
* [6.1 Stage 1: Parallel Literature, News & Cost Subagents](#61-stage-1-parallel-literature-news--cost-subagents)
  * [6.1.1 Subagent 1A: Published & Informal Ladder Catalog](#611-subagent-1a-published--informal-ladder-catalog)
  * [6.1.2 Subagent 1B: Yearly Reports, Courses, News ("Who Did What") & Cost Baseline](#612-subagent-1b-yearly-reports-courses-news-who-did-what--cost-baseline)
* [6.2 Stage 2: Orchestrator Timeline & Master Skeleton Lock](#62-stage-2-orchestrator-timeline--master-skeleton-lock)
  * [6.2.1 Locking the 5 Era Windows (`YYYY-MM`) & Duration Proportions](#621-locking-the-5-era-windows-yyyy-mm--duration-proportions)
  * [6.2.2 Locking All 23 User Skill-Tree Steps, Cross-Era Transitions & JSON Schema](#622-locking-all-23-user-skill-tree-steps-cross-era-transitions--json-schema)
* [6.3 Stage 3: Parallel Per-Era Deep-Dive & Post-Synthesis Comparison Subagents](#63-stage-3-parallel-per-era-deep-dive--post-synthesis-comparison-subagents)
  * [6.3.1 Dedicated Per-Era Subagents ($L_1$ through $L_5$)](#631-dedicated-per-era-subagents-l_1-through-l_5)
  * [6.3.2 Post-Synthesis Literature Comparison (`Section 5.3`) & Part I Extended Summary Pass](#632-post-synthesis-literature-comparison-section-53--part-i-extended-summary-pass)
* [6.4 Stage 4: Code-Driven Visual Rendering, Inspection Loop & Report Assembly](#64-stage-4-code-driven-visual-rendering-inspection-loop--report-assembly)
  * [6.4.1 Rendering All 6 Visual Abstracts, 23 Section Figures & 2 Continuous-Time Posters](#641-rendering-all-6-visual-abstracts-23-section-figures--2-continuous-time-posters)
  * [6.4.2 Mandatory `view_file` Visual Inspection & Self-Correction Loop](#642-mandatory-view_file-visual-inspection--self-correction-loop)
  * [6.4.3 Final Report Assembly, Anchor Link Verification & Word-Count Audit](#643-final-report-assembly-anchor-link-verification--word-count-audit)

### 6.1 Stage 1: Parallel Literature, News & Cost Subagents

**Parallel Evidence Gathering:** Spawns two research subagents concurrently to build the empirical foundation.

#### 6.1.1 Subagent 1A: Published & Informal Ladder Catalog

* **Catalog Scope:** Searches and reviews all 19 published and informal AI, LLM, and agentic ladders across research papers, AI labs, enterprise/VC frameworks, practitioner blogs, and the Gemini Deep Research historical ladder (`stages/stage1a_ladder_catalog.md`).

#### 6.1.2 Subagent 1B: Yearly Reports, Courses, News ("Who Did What") & Cost Baseline

* **Evidence & Pricing Scope:** Searches annual AI reports (*HAI*, *State of AI*, *Epoch*), paid API logs (*Menlo*, *OpenRouter*, *MIT NANDA*), courses/syllabi (*CS224N*, *CS324*, *Fast.ai*, *DeepLearning.AI*), developer surveys (*Stack Overflow*, *Octoverse*), and yearly headline news wins/failures ("who did what"), and compiles the 2020–2026 API pricing and Wh/FLOPs baseline (`stages/stage1b_yearly_evidence_cost.md`).

### 6.2 Stage 2: Orchestrator Timeline & Master Skeleton Lock

**Master Schema Lock:** Applies Rules 1–4 ([Section 3](#3-how-to-build-the-ladders-four-rule-protocol)) to lock the timeline and user skill-tree hierarchy before per-era drafting begins.

#### 6.2.1 Locking the 5 Era Windows (`YYYY-MM`) & Duration Proportions

* **Locked Era Windows:** Lock the 5 chronological Era Ladders ($L_1$: `2017-06` to `2020-05` [36m]; $L_2$: `2020-06` to `2022-10` [29m]; $L_3$: `2022-11` to `2024-05` [19m]; $L_4$: `2024-06` to `2025-01` [8m]; $L_5$: `2025-02` to `2026-10` [21m]) and verify their Two-Shift scores ($\Delta_{\text{structural}} \ge 2$).

#### 6.2.2 Locking All 23 User Skill-Tree Steps, Cross-Era Transitions & JSON Schema

* **Locked Step Skeleton:** Lock all 23 user skill-tree step names, 18 within-era MECE split scores across $\Delta\text{Skill}$, $\Delta\text{Surface}$, and $\Delta\text{Setup}$, and 28 cross-era alluvial transitions in `stages/stage2_locked_skeleton.md` and `stages/ladder_metrics.json`.

### 6.3 Stage 3: Parallel Per-Era Deep-Dive & Post-Synthesis Comparison Subagents

**Parallel Era Drafting:** Spawns dedicated Era Subagents ($L_1 \dots L_5$) followed by the post-synthesis literature comparison (`Section 5.3`) and Part I Extended Summary pass.

#### 6.3.1 Dedicated Per-Era Subagents ($L_1$ through $L_5$)

* **One Subagent Per Era Ladder:** Each Era Subagent writes its Era Ladder section (`4.1` through `4.5`), covering valid dates, why the old ladder got outdated, step transitions, the full 5-part User Skill-Tree profile for every step $1 \dots N$, and full-ladder resource totals.

#### 6.3.2 Post-Synthesis Literature Comparison (`Section 5.3`) & Part I Extended Summary Pass

* **Post-Ladder Literature Comparison & 5% Executive Digest:** Only after all 5 Era Ladders ($L_1 \dots L_5$) and 23 steps are built in `Part IV`, write **`Section 5.3` (`Post-Synthesis Comparison: Our Five-Era User Skill-Tree Ladder vs. Existing Literature Ladders`)** comparing our completed ladder against all 19 literature frameworks (`Table 5.3a`, `Table 5.3b`, `Figure 22`), and synthesize **Part I — Extended Summary** (~5% of the full report).

### 6.4 Stage 4: Code-Driven Visual Rendering, Inspection Loop & Report Assembly

**Visual Generation & Assembly:** Renders all 29 PNG visuals via Python `matplotlib`, visually inspects every image, and assembles the verified report.

#### 6.4.1 Rendering All 6 Visual Abstracts, 23 Section Figures & 2 Continuous-Time Posters

* **Automated `matplotlib` Scripts:** Execute `uv run --with numpy --with matplotlib python3` scripts in `stages/` to generate all **6 Visual Abstracts** (`fig_va0_root_report.png` + `fig_va1`..`fig_va5`) and **23 numbered H3 figures** (`Figure 1` through `Figure 23`), including both continuous-time, duration-proportional full-timeline posters (`fig_full_evolution_poster.png` and `fig_era_defining_news_and_learning_poster.png`) and the post-synthesis literature comparison chart (`fig_s5_3_literature_ladder_comparison.png`).

#### 6.4.2 Mandatory `view_file` Visual Inspection & Self-Correction Loop

* **Visual Quality Gate:** Call `view_file` on every generated `.png` figure to inspect text padding, legend placement, and axis labels and re-render until zero overlaps exist.

#### 6.4.3 Final Report Assembly, Anchor Link Verification & Word-Count Audit

* **Assembly & Programmatic Audits:** Merge all Parts inside the project workspace directory and run programmatic Python verification checks confirming: (1) 0 broken ToC anchor links across the Root ToC and all 5 Per-Part ToCs, (2) 100% visual + table presence in every `### H3` section (`20/20` H3 sections), (3) 100.0% sum conservation on all era share vectors, and (4) exact word-count breakdown per Part.

***

## 7. Five-Part Output Report Blueprint & Final Verification Gates

**Section 7 Overview:** Defines the exact 5-Part structure of the finished report (`2026 10 17 AI_ladder_evol report v2.md`), maps the mandatory visual and table inventory across every Part and H3 section, and lists the six-point final verification checklist.

#### Section 7 Structural Index
* [7.1 Five-Part Report Structure (Including Part I ~5% Extended Summary & Section 5.3 Post-Synthesis Comparison)](#71-five-part-report-structure-including-part-i-5-extended-summary--section-53-post-synthesis-comparison)
  * [7.1.1 Root Frontmatter: Title, BLUF, Root Visual Abstract & Clickable Root ToC](#711-root-frontmatter-title-bluf-root-visual-abstract--clickable-root-toc)
  * [7.1.2 Part I — Extended Summary (~5% of Report)](#712-part-i--extended-summary-5-of-report)
  * [7.1.3 Part II — Literature & Cost Survey](#713-part-ii--literature--cost-survey)
  * [7.1.4 Part III — Applied Ladder-Building Method (User Skill-Tree Protocol)](#714-part-iii--applied-ladder-building-method-user-skill-tree-protocol)
  * [7.1.5 Part IV — Chronological Ladder Evolution (L1 to L5, 2017–2026)](#715-part-iv--chronological-ladder-evolution-l1-to-l5-20172026)
  * [7.1.6 Part V — Overall Patterns, Literature Ladder Comparison & Summary Visuals](#716-part-v--overall-patterns-literature-ladder-comparison--summary-visuals)
* [7.2 Mandatory Visual & Table Inventory Across All Sections](#72-mandatory-visual--table-inventory-across-all-sections)
  * [7.2.1 Complete Section-by-Section Visual & Table Mapping Matrix](#721-complete-section-by-section-visual--table-mapping-matrix)
* [7.3 Six-Point Final Verification & Word-Count Audit Checklist](#73-six-point-final-verification--word-count-audit-checklist)
  * [7.3.1 Six Programmatic Verification Gates](#731-six-programmatic-verification-gates)

### 7.1 Five-Part Report Structure (Including Part I ~5% Extended Summary & Section 5.3 Post-Synthesis Comparison)

**Master Blueprint:** Organizes the final report into Root Frontmatter plus 5 numbered Parts (`Part I` to `Part V`), where every Part opens with a `Part Overview`, a dedicated `Part Visual Abstract`, and a clickable `Part Structural Index` expanding up to Level 4 (`H4`) using that Part's number prefix (`1.x`, `2.x`, `3.x`, `4.x`, `5.x`).

#### 7.1.1 Root Frontmatter: Title, BLUF, Root Visual Abstract & Clickable Root ToC

* **Root Header Block:** Report title (`# H1`), `**Executive Summary (BLUF):**`, embedded **Root Visual Abstract** (`figures/fig_va0_root_report.png`) with standalone declarative caption, and clickable **Root `### Structural Index`** linking to all 5 Parts and 20 H3 sections (`### 1.1` through `### 5.4`).

#### 7.1.2 Part I — Extended Summary (~5% of Report)

* **Part I Architecture (`## 1. Part I — Extended Summary`):** Opens with `**Part I Overview:**`, **Part I Visual Abstract** (`figures/fig_va1_part1_extended_summary.png`), and clickable **`#### Part I Structural Index`** (`1.1`..`1.4.3`), followed by:
  * **`### 1.1 Literature, Evidence & Cost Synthesis (Part II Digest)`:** H4s `1.1.1` (19 Published Ladders), `1.1.2` (Nine Years of Evidence), `1.1.3` (Two-Level Cost System & 2,000x Price Deflation) + `Table 1.1` + **Figure 1** (`fig_s1_1_literature_cost_digest.png`).
  * **`### 1.2 Applied Ladder-Building Method (Part III Digest)`:** H4s `1.2.1` (Rule 1 Two-Shift & Rule 2 Dual-Pass), `1.2.2` (Rule 3 MECE 2-of-3 User Skill-Tree Split & Rule 4 Lineage) + `Table 1.2` + Mermaid Flowchart + **Figure 2** (`fig_s1_2_methodology_digest.png`).
  * **`### 1.3 Five Chronological Era Ladders (L1 to L5, 2017–2026) (Part IV Digest)`:** H4s `1.3.1` ($L_1$) through `1.3.5` ($L_5$) + `Table 1.3` + **Figure 3** (`fig_s1_3_five_eras_digest.png`).
  * **`### 1.4 Evolutionary Laws, Literature Comparison & Executive Matrix (Part V Digest)`:** H4s `1.4.1` (Four Repeating Laws & Three Capital Rules), `1.4.2` (Condensed Five-Era Macro & 23-Step Executive Summary `Table 1.4`), `1.4.3` (Post-Synthesis Comparison Against the 19 Existing Literature Ladders `Table 1.4b`) + **Figure 4** (`fig_s1_4_four_laws_digest.png`).

#### 7.1.3 Part II — Literature & Cost Survey

* **Part II Architecture (`## 2. Part II — Literature & Cost Survey`):** Opens with `**Part II Overview:**`, **Part II Visual Abstract** (`figures/fig_va2_part2_literature_and_cost.png`), and clickable **`#### Part II Structural Index`** (`2.1`..`2.3.5`), followed by:
  * **`### 2.1 Review of Published & Informal AI, LLM & Agentic Ladders (2017–2026)`:** H4s `2.1.1` (Academic & AI Lab Ladders), `2.1.2` (Industry, Enterprise & Autonomy Ladders, including the Gemini Deep Research Ladder reviewed purely as literature), `2.1.3` (Developer & Practitioner Ladders), `2.1.4` (Master Comparison `Table 2.1` of 19 Ladders) + **Figure 5** (`fig_s2_1_published_ladders_map.png`).
  * **`### 2.2 Step Use-Case Sources: Reports, Traffic Logs, Courses, Surveys & News (2017–2026)`:** H4s `2.2.1`..`2.2.4` + `Tables 2.2–2.5` + **Figure 6** (`fig_s2_2_empirical_telemetry.png`).
  * **`### 2.3 Single-Task vs. Industry-Wide Resource Metrics & Fallback Math`:** H4s `2.3.1`..`2.3.5` + `Tables 2.6–2.8` + **Figure 7** (`fig_s2_3_resource_pricing_scaling.png`).

#### 7.1.4 Part III — Applied Ladder-Building Method (User Skill-Tree Protocol)

* **Part III Architecture (`## 3. Part III — Applied Ladder-Building Method`):** Opens with `**Part III Overview:**`, **Part III Visual Abstract** (`figures/fig_va3_part3_method.png`), and clickable **`#### Part III Structural Index`** (`3.1`..`3.4.2`), followed by:
  * **`### 3.1 Two-Shift Era Threshold Audit (2017–2026 Cutoff Decisions)`:** H4s `3.1.1`..`3.1.2` + Cutoff Audit Table + **Figure 8** (`fig_s3_1_era_cutoff_audit.png`).
  * **`### 3.2 Bottom-Up & Top-Down Reconciliation Against Published Ladders`:** H4s `3.2.1`..`3.2.3` + Reconciliation Table + **Figure 9** (`fig_s3_2_reconciliation_map.png`).
  * **`### 3.3 No-Overlap & No-Gaps (MECE) Two-of-Three User Skill-Tree Split Verification Matrix`:** H4s `3.3.1`..`3.3.2` + 18-Boundary MECE User Skill-Tree Table + **Figure 10** (`fig_s3_3_mece_split_heatmap.png`).
  * **`### 3.4 Locked Master Skeleton (L1 to L5 Dates, Steps & Cross-Era Links)`:** H4s `3.4.1`..`3.4.2` + 23-Step Master Skeleton Table + Cross-Era Mermaid Flowchart + **Figure 11** (`fig_s3_4_master_skeleton_flow.png`).

#### 7.1.5 Part IV — Chronological Ladder Evolution (L1 to L5, 2017–2026)

* **Part IV Architecture (`## 4. Part IV — Chronological Ladder Evolution (L1 to L5, 2017–2026)`):** Opens with `**Part IV Overview:**`, **Part IV Visual Abstract** (`figures/fig_va4_part4_eras.png`), and clickable **`#### Part IV Structural Index`** (`4.1`..`4.5.4`), followed by one H3 section per Era Ladder (`### 4.1` $L_1$, `### 4.2` $L_2$, `### 4.3` $L_3$, `### 4.4` $L_4$, `### 4.5` $L_5$), each containing `4.t.1` (Valid Dates & Why Previous Skill-Tree Ladder Got Outdated), `4.t.2` (How User Skill-Tree Steps Changed), `4.t.3` (Step-by-Step Breakdown of Steps 1 to N along the User Skill Tree), and `4.t.4` (Era Full-Ladder Resource Totals + 12-Column Summary Table + **Figures 12–16**).

#### 7.1.6 Part V — Overall Patterns, Literature Ladder Comparison & Summary Visuals

* **Part V Architecture (`## 5. Part V — Overall Patterns, Literature Ladder Comparison & Summary Visuals`):** Opens with `**Part V Overview:**`, **Part V Visual Abstract** (`figures/fig_va5_part5_laws.png`), and clickable **`#### Part V Structural Index`** (`5.1`..`5.4.2`), followed by:
  * **`### 5.1 Four Repeating Structural & Economic Laws Across Eras`:** Detailed analysis (`5.1.1`–`5.1.5`) + Summary `Table 5.1` + **Figure 17** (`fig_s5_1_four_laws_deep_dive.png`).
  * **`### 5.2 Cross-Era Master Comparison Tables & Full-Timeline Visual Synthesis`:** **Figures 18, 19, 20, 21** (`fig_full_evolution_poster.png`, `fig_era_defining_news_and_learning_poster.png`, `fig_cross_era_metrics.png`, `fig_s5_2_citra_pairplot.png`) + **`Master Tables 5.1, 5.2 & 5.3`** (`5.2.1`–`5.2.3`).
  * **`### 5.3 Post-Synthesis Comparison: Our Five-Era User Skill-Tree Ladder vs. Existing Literature Ladders`:** Placed strictly AFTER our 5-Era / 23-Step ladder evolution list is built in Part IV! Contains:
    * **`#### 5.3.1 Why Our User Skill-Tree Axis Differs from Lab Capability & Backend Workflow Ladders`:** Explains why model-capability scales (*OpenAI 5 Levels*, *DeepMind Performance Tiers*) and backend code-topology scales (*Anthropic Predefined Workflows*, *LangChain*) place auto-routed `o3`/`GPT-5.4` or backend RAG high on their scales, whereas our User Skill-Tree axis places zero-setup browser tools at **Step 1** and reserves **Steps 3–5** for users who install specialized IDEs (`Cursor`), master terminal CLIs (`Claude Code`), or set up isolated Docker sandboxes and dedicated **M4 Mac Mini** agent servers.
    * **`#### 5.3.2 Cross-Walk Against Coding Autonomy, Practitioner Evals & Enterprise Maturity Ladders`:** Maps *SAE L0–L5 Coding*, *Yegge/Shapiro Gas Town*, *Karpathy Software 1.0–3.0*, *Huyen/Husain/Willison Evals*, *Sequoia Acts 1–3*, and *Gartner L1–L5* onto our 23 steps.
    * **`#### 5.3.3 Head-to-Head Structural, Chronological & Quantitative Audit: Our v2 Ladder vs. the Gemini Deep Research Ladder`:** Compares our `v2` User Skill-Tree / Production-Crossover ladder against the *Gemini Deep Research 23-Step First-Release Cutoff Ladder* ($L_1^{\text{Gem}}\dots L_5^{\text{Gem}}$).
    * **`#### 5.3.4 Complete 19-Ladder Cross-Walk Matrix, Head-to-Head Reconciliation Table & Comparative Visual Synthesis`:** Presents **`Table 5.3a`** (19-Framework Cross-Walk Matrix), **`Table 5.3b`** (Head-to-Head Fact-Check vs. Gemini Deep Research Ladder), and **Figure 22** (`figures/fig_s5_3_literature_ladder_comparison.png`).
  * **`### 5.4 Final Verification Audit Checklist`:** Six-point verification audit (`5.4.1`–`5.4.2`) + Verification Scorecard **`Table 5.4`** + **Figure 23** (`figures/fig_s5_3_verification_audit.png`).

### 7.2 Mandatory Visual & Table Inventory Across All Sections

**Complete Visual & Tabular Coverage Matrix:** Enforces at least one visualization and one structured table in every `### H3` section (`20/20` H3 sections) plus 6 Visual Abstracts (`va0`..`va5`).

#### 7.2.1 Complete Section-by-Section Visual & Table Mapping Matrix

| Report Section (`H1` / `H2` / `H3`) | Mandatory Visualization File(s) & Diagram(s) | Mandatory Structured Table(s) | Primary Visual Architecture & User Skill-Tree / Time Axis |
| :--- | :--- | :--- | :--- |
| **Root Header (`# H1`)** | `figures/fig_va0_root_visual_abstract.png` (Root Visual Abstract) | Root Clickable `Structural Index` | 3-panel synthesis: Era timeline + 4 Laws + 10-yr log scaling with marginal |
| **Part I Header (`## 1.`)** | `figures/fig_va1_part1_extended_summary.png` (Part I Visual Abstract) | Clickable `Part I Structural Index` (`1.1`..`1.4.3`) | 2-panel digest map + 5-era macro trajectory with marginal |
| **`### 1.1` Part II Digest** | **Figure 1:** `figures/fig_s1_1_literature_cost_digest.png` | `Table 1.1` (5-Pillar Evidence Summary) | 19-ladder tradition bars + enterprise workload flip (`2020–2026`) |
| **`### 1.2` Part III Digest** | **Figure 2:** `figures/fig_s1_2_methodology_digest.png` + Mermaid | `Table 1.2` (4-Rule User Skill-Tree Audit) | Two-Shift cutoff verification + 18-boundary MECE split distribution |
| **`### 1.3` Part IV Digest** | **Figure 3:** `figures/fig_s1_3_five_eras_digest.png` | `Table 1.3` (5-Era User Skill-Tree Digest) | Single-task cost scaling (`L1–L5`) + step transition composition |
| **`### 1.4` Part V Digest** | **Figure 4:** `figures/fig_s1_4_four_laws_digest.png` | `Table 1.4` (23-Step Matrix) & `Table 1.4b` (19-Ladder Cross-Walk) | 18-month sinking cost drop + Step 1 vs. Top-Step Pareto inversion |
| **Part II Header (`## 2.`)** | `figures/fig_va2_part2_literature_and_cost.png` (Part II Visual Abstract) | Clickable `Part II Structural Index` (`2.1`..`2.3.5`) | 19-ladder axis breakdown + API price deflation (`2020–2026`) with marginal |
| **`### 2.1` Published Ladders** | **Figure 5:** `figures/fig_s2_1_published_ladders_map.png` | `Table 2.1` (Master Catalog of 19 Literature Ladders) | Rung count per framework ($n=19$) + publication timeline scatter |
| **`### 2.2` Empirical Sources** | **Figure 6:** `figures/fig_s2_2_empirical_telemetry.png` | `Tables 2.2–2.5` (Macro, Telemetry, Courses, News) | 10-yr training FLOPs/spend with marginal + survey/syllabus shift |
| **`### 2.3` Resource Metrics** | **Figure 7:** `figures/fig_s2_3_resource_pricing_scaling.png` | `Tables 2.6–2.8` (5 Units, API Prices/OOMs, Archetypes) | Log-log Tokens-vs-Wh physics + 5-unit normalized profile across archetypes |
| **Part III Header (`## 3.`)** | `figures/fig_va3_part3_method.png` (Part III Visual Abstract) | Clickable `Part III Structural Index` (`3.1`..`3.4.2`) | 4-rule MECE construction funnel + 23-step transition mechanism bars |
| **`### 3.1` Cutoff Audit** | **Figure 8:** `figures/fig_s3_1_era_cutoff_audit.png` | `Table 3.1` (Candidate Cutoff Audit) | Candidate cutoffs (`Accepted >=2` vs. `Rejected <2`) + price-drop multiplier |
| **`### 3.2` Reconciliation** | **Figure 9:** `figures/fig_s3_2_reconciliation_map.png` | `Table 3.2` (Published-to-Empirical Reconciliation) | Reconciliation fate across ladders + Step 1 vs. Workhorse user/token split |
| **`### 3.3` MECE Split Matrix** | **Figure 10:** `figures/fig_s3_3_mece_split_heatmap.png` | `Table 3.3` (18-Boundary User Skill-Tree Split Matrix) | 18-boundary 3-axis heatmap ($\Delta\text{Skill}, \Delta\text{Surface}, \Delta\text{Setup}$) |
| **`### 3.4` Master Skeleton** | **Figure 11:** `figures/fig_s3_4_master_skeleton_flow.png` + Mermaid | `Table 3.4` (Locked 23-Step Master Skeleton) | User Skill-Tree tier trajectory (`L1–L5`) + single-task USD dispersion |
| **Part IV Header (`## 4.`)** | `figures/fig_va4_part4_eras.png` (Part IV Visual Abstract) | Clickable `Part IV Structural Index` (`4.1`..`4.5.4`) | 100% stacked user vs. compute shares + 5-era macro scaling with marginal |
| **`### 4.1` Era 1 ($L_1$)** | **Figure 12:** `figures/fig_era1_ladder.png` + ASCII Transition | `Table 4.1` (Era 1 4-Step Skill-Tree & Share Table) | 3-panel CITRA ladder card + log single-task bars + macro user/compute % |
| **`### 4.2` Era 2 ($L_2$)** | **Figure 13:** `figures/fig_era2_ladder.png` + ASCII Transition | `Table 4.2` (Era 2 4-Step Skill-Tree & Share Table) | 3-panel CITRA ladder card + log single-task bars + macro user/compute % |
| **`### 4.3` Era 3 ($L_3$)** | **Figure 14:** `figures/fig_era3_ladder.png` + ASCII Transition | `Table 4.3` (Era 3 5-Step Skill-Tree & Share Table) | 3-panel CITRA ladder card + log single-task bars + macro user/compute % |
| **`### 4.4` Era 4 ($L_4$)** | **Figure 15:** `figures/fig_era4_ladder.png` + ASCII Transition | `Table 4.4` (Era 4 5-Step Skill-Tree & Share Table) | 3-panel CITRA ladder card + log single-task bars + macro user/compute % |
| **`### 4.5` Era 5 ($L_5$)** | **Figure 16:** `figures/fig_era5_ladder.png` + ASCII Transition | `Table 4.5` & `Table 4.5b` (`SWE-bench Pro` Audit) | 3-panel CITRA ladder card + log single-task bars + macro user/compute % |
| **Part V Header (`## 5.`)** | `figures/fig_va5_part5_laws.png` (Part V Visual Abstract) | Clickable `Part V Structural Index` (`5.1`..`5.4.2`) | Lorenz compute concentration curves + human-vs-AI runtime inversion |
| **`### 5.1` Four Laws** | **Figure 17:** `figures/fig_s5_1_four_laws_deep_dive.png` | `Table 5.1` (4-Law Quantitative Summary) | 4-panel proof: Sinking friction + Jevons loop + Pareto ratio + AI/Human time |
| **`### 5.2` Master Synthesis** | **Figures 18, 19, 20, 21:** `fig_full_evolution_poster.png`, `fig_era_defining_news_and_learning_poster.png`, `fig_cross_era_metrics.png`, `fig_s5_2_citra_pairplot.png` | **`Master Tables 5.1, 5.2 & 5.3`** (Macro Totals, 23-Step Matrix, Era-Defining Tech/News/Skills) | Two continuous-time duration-proportional posters (`36m/29m/19m/8m/21m`) + Pareto jointplot + 23-step CITRA tri-partite pairplot |
| **`### 5.3` Literature Comparison** | **Figure 22:** `figures/fig_s5_3_literature_ladder_comparison.png` | **`Table 5.3a`** (19-Ladder Cross-Walk) & **`Table 5.3b`** (Head-to-Head vs. Gemini Ladder) | 3-panel cross-walk of existing literature ladders onto our 23 steps + macro token fact-check + cutoff lag timeline |
| **`### 5.4` Final Audit** | **Figure 23:** `figures/fig_s5_3_verification_audit.png` | **`Table 5.4`** (Verification Scorecard & Word-Count Audit) | 15 stacked 100% MECE conservation bars + verification compliance scorecard |

### 7.3 Six-Point Final Verification & Word-Count Audit Checklist

**Autonomous Quality Gates:** Before completing the task, run programmatic verification checks confirming 100% compliance across all six requirements.

#### 7.3.1 Six Programmatic Verification Gates

* **Gate 1 — Fractal Formatting, Clickable Root + Per-Part ToCs (Part-Prefixed up to Level 4) & Plain Layman English:** Verify that every section with $\ge 3$ items opens with a bottom-line summary (BLUF), every bullet and paragraph begins with a bold 2–4 word lead-in label (`**RIH:**`), real technical terms appear as `plain meaning (technical term)` on first use, the Root ToC has clickable links, and **every Part (`Part I` to `Part V`) has its own clickable ToC right after its overview/visual abstract expanding up to Level 4 (`H4`) where every item under Part $X$'s ToC starts with `X.` (`1.1`..`1.4.3`, `2.1`..`2.3.5`, `3.1`..`3.4.2`, `4.1`..`4.5.4`, `5.1`..`5.4.2`) with 0 broken anchor links**.
* **Gate 2 — User-Sophistication / Skill-Tree Definition of "Up" & Post-Synthesis Literature Comparison (`Section 5.3`):** Verify that every Era Ladder orders steps strictly by **User-Side Sophistication & Skill-Tree Complexity** ($\Delta\text{Skill}$, $\Delta\text{Surface}$ [browser $\to$ IDE $\to$ CLI $\to$ daemon], and $\Delta\text{Setup}$ [non-compute sandboxes, local GPUs, dedicated Mac Mini servers]), and that the comparison against the 19 existing literature ladders appears in `Section 5.3` (`Part V`) after our 23-step ladder evolution is constructed in `Part IV`.
* **Gate 3 — Exact `YYYY-MM` Era Dates & Duration-Proportional Continuous-Time Posters:** Verify that all 5 Era Ladders have exact `YYYY-MM` start and end dates (`2017-06` to `2020-05` [36m], `2020-06` to `2022-10` [29m], `2022-11` to `2024-05` [19m], `2024-06` to `2025-01` [8m], `2025-02` to `2026-10` [21m]) and that both `fig_full_evolution_poster.png` and `fig_era_defining_news_and_learning_poster.png` plot a continuous calendar time X-axis with box widths strictly proportional to era duration.
* **Gate 4 — Complete 5-Part User Skill-Tree Step Profiles & Era-Defining News/Skills Coverage:** Verify that all 23 steps include all 5 profile parts (`Name & Rank`, `Skill-Tree Step Boundaries`, `Concrete Tool & Setup Stack`, `Use Cases & Context Switching`, `Step Resource Use`) and that both `fig_era_defining_news_and_learning_poster.png` and `Master Table 5.3` document each era's starting/ending tech triggers, headline news wins and failures ("who did what"), and `#1 Top Skill to Learn`.
* **Gate 5 — 100% MECE Resource Share Conservation Across All 5 Eras:** Verify programmatically that across the steps of every Era Ladder ($L_1 \dots L_5$), industry-wide User Share %, Human-Hour Share %, Compute/Token Share %, and USD Spend Share % each sum to exactly $100.0\%$.
* **Gate 6 — Liberal Visual Density (Root VA + 5 Part VAs + Every-H3 Viz & Table) & Visual Inspection:** Verify that the Root Visual Abstract, all 5 Part Visual Abstracts, all 23 numbered H3 figures, all 2 Mermaid flowcharts, and all 30+ structured tables are embedded in the report, every `### H3` section (`20/20`) contains $\ge 1$ visual and $\ge 1$ table, every figure has a standalone caption starting with a bold takeaway sentence, and every `.png` image has been visually inspected via `view_file` to guarantee zero overlapping text.
