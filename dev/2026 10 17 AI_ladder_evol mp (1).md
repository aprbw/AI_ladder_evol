# AI Ladder Evolution

**Multi-Agent History & Cost of AI Ladders:** Orchestrate a multi-agent research pipeline to produce a thorough historical and data-driven report mapping how people have used AI, large language models (LLMs), and action-taking AI (agentic AI) across different eras, ordered bottom-to-top by task and use-case complexity, measured by both single-task and industry-wide resource use, and illustrated with clear in-section and summary visuals.

### Structural Index
1. Agent Contract & Scope
2. Literature & Cost Survey
   1. Existing AI Ladders
   2. Annual Reports & News Milestones
   3. Single-Task vs. Industry-Wide Metrics
3. How to Build the Ladders
4. Ladder Evolution
   1. Era Dates & Why Old Ladders Get Outdated
   2. How Steps Change Between Eras
   3. Full-Ladder Resource Totals
5. Steps in a Ladder
6. Multi-Agent Execution Pipeline
7. Output Report Blueprint

***

## Agent Contract & Scope

**Role, Rules & Scope:** Defines the lead orchestrator and subagent team, input sources, writing and drawing rules, and scope boundaries.

* **Role & Multi-Agent Team:** Lead Research Orchestrator coordinating specialized subagents:
  * **Core Job:** Coordinate a staged team of subagents to map how AI, large language models (LLMs), and action-taking AI (agentic AI) ladders have evolved over time — why old ladders become outdated after new breakthroughs, how individual steps change from era to era, and how much resource each step uses.
  * **Subagent Division of Labor:** Follow `Multi-Agent Execution Pipeline` (Section 6) so literature discovery, timeline locking, per-era deep dives (one subagent per era ladder $L_t$), and code-driven visual generation each get dedicated search depth and output space.
  * **Input Sources & Search Precision:** Use this markdown prompt plus thorough web search across published AI ladders, research papers, annual AI reports, paid model traffic logs (API usage data), developer surveys, educational resources (courses, university syllabi, code cookbooks, tutorials), and news archives. Every agent runs search queries using exact technical terms (`RLVR`, `FLOPs`, `KV-cache`, `MCP`, `LoRA`, `RAG`, `pass@k`) to pull primary technical sources, then translates findings into plain English when writing.
* **Output Deliverable:** Comprehensive written research report with clear visuals:
  * **Report Structure:** Follow `Output Report Blueprint` (Section 7) so each era's ladder is presented together with its steps and visuals.
  * **Writing Style:** Clear, high-density prose governed by 5 rules:
    * **Arian Fractal Format:** Recursive summary-first structure:
      * **Bottom-Line Summaries:** Start the report and every section with $\ge 3$ items with a brief summary at the top (bottom-line up front / BLUF).
      * **Table of Contents:** Place a nested numbered table of contents (`Structural Index`) right under the main summary.
      * **Bold Lead-In Labels:** Start every bullet and paragraph with a bold 2–3 word label (run-in heading / RIH).
    * **Plain Layman English:** Write in plain, direct English for a smart general reader outside the AI field. Use everyday tech words (`prompt`, `chat`, `model`, `autocomplete`, `database`, `code editor`) plainly with zero brackets, and replace empty academic words (`methodology`, `taxonomy`, `paradigm`, `obsolescence`, `telemetry`) with simple everyday words (`method`, `ordering`, `shift`, `getting outdated`, `usage logs`).
    * **Bracketed Technical Jargon:** When a real, established AI or engineering term exists and improves accuracy, write the plain meaning first and append the technical term in parentheses as `plain English (technical term)` on first use in a section, then use the short term cleanly after — for example, write *"training models to think step by step before answering (RLVR test-time compute)"* rather than raw jargon *"RLVR test-time compute scaling"* or vague *"making AI think harder"*.
    * **Caveman Compression:** Keep high information density using short, direct sentences and positive instructions stating what to do.
    * **Concrete Specificity:** Name exact models, software libraries, websites, tools, and data sources.
  * **Drawing Style:** High-density visual rules for why, when, and how to decide what to draw, plus how to draw it:
    * **Why to Draw:** Draw a visual whenever a multi-step hierarchy, cross-era structural shift, or multi-order-of-magnitude cost gap is faster and clearer to grasp spatially than in prose.
    * **When to Draw:** Place focused visuals right inside each section where a new ladder or trade-off is introduced, and place an overall summary visual at the end where all eras and trends are compared together.
    * **Deciding What to Draw:** Match the chart type to the relationship being shown — vertical tiers for ordered complexity steps, connecting flow bands (alluvial diagrams) for steps splitting/merging/sinking across eras, and multi-scale charts for single-task cost vs. industry-wide share.
    * **How to Draw:** Pack high information density into every figure (combining structure, number scales, and concrete tool/example callouts in one view using the richest visual format available in your environment) and pair every visual with a standalone caption that opens with a bold conclusion sentence stating the main takeaway (such as *"Falling token prices pushed 2023 custom RAG code into 2024 default chat UI"*).
* **Scope & Ordering Rules:** Domain boundaries and how steps are ordered:
  * **Domain Scope:** AI, LLMs, and agentic AI across text, code, step-by-step reasoning, and tool use, including image/video models (computer vision / CV) and audio models where connected to LLM workflows (screen-reading models [vision-language models / VLMs], image-and-text document search [multimodal RAG], reading text from images [OCR-to-LLM]).
  * **Real Usage Only:** Build a factual classification of how people actually used AI in the past (positive taxonomy) rather than a theory of how people should use AI or future predictions (normative ontology). Base every step on real historical usage.
  * **Task-Complexity Axis:** Order steps bottom-to-top by **Task / Use-Case Complexity** — from simple one-line tasks, to single-document questions, to multi-step workflows, up to large system-wide engineering and research projects. Note the required technical setup — web chat (Web UI), writing instructions (prompting), connecting software or private documents (API / retrieval-augmented generation [RAG]), or custom model training (fine-tuning) — and the level of AI independence at each step.

***

## Literature & Cost Survey

**Ladders, Evidence & Cost Metrics:** Reviews all existing AI ladders first, gathers annual AI reports, educational materials, surveys, and yearly news to populate the use cases of each step within each era's ladder, and defines single-task and industry-wide resource measurements.

### Existing AI Ladders

**All Published & Informal Ladders:** Catalogs and reviews all existing AI, LLM, and agentic ladders across research, industry, and developer communities.

* **Academic & AI Lab Ladders:** Review ladders from research papers and leading AI companies (frontier labs) — Karpathy Software 1.0/2.0/3.0, OpenAI 5 Levels of AGI (Chatbots, Reasoners, Agents, Innovators, Organizations), DeepMind Levels of AGI (Morris et al.), and Anthropic Workflows vs. Agents.
* **Industry & Enterprise Ladders:** Review business, venture capital (VC), and autonomy frameworks — self-driving car levels (SAE L0–L5) adapted for coding and agents, Gartner AI maturity models, a16z, Menlo Ventures, and LangChain agent tiers.
* **Developer & Practitioner Ladders:** Review informal and community ladders from engineering blogs, tutorials, code cookbooks, and developer post-mortems across eras.

### Annual Reports & News Milestones

**Step Use-Case Sources:** Gathers annual AI reports, API usage data, educational courses/cookbooks, developer surveys, and major news stories so these items go directly into the **Use Cases** and resource estimates of each step within each era's ladder.

* **Annual AI Reports:** Pull yearly adoption, compute, and cost trends from *Stanford HAI AI Index Report*, *State of AI Report* (Benaich & Hogarth), and *Epoch AI* datasets for each era's steps.
* **API Usage Data:** Gather workflow and text-chunk (token) usage breakdowns from *Menlo Ventures Enterprise GenAI Report*, *OpenRouter* rankings, *Stripe* AI billing data, and *Cloudflare* AI radar to map real usage per step.
* **Educational Resources:** Review courses, university syllabi, code cookbooks, and popular tutorials from each era (Fast.ai, DeepLearning.AI, Stanford CS224N/CS324, OpenAI/Anthropic cookbooks, popular YouTube/GitHub guides) to populate the concrete use cases taught and practiced at each step.
* **Surveys & News:** Check *Stack Overflow Developer Survey*, *GitHub Octoverse*, and all major AI use cases that made the news each year to place concrete examples into their matching ladder step.

### Single-Task vs. Industry-Wide Metrics

**Two-Level Cost Metrics:** Compares candidate measurement units (Energy, Money, Tokens, Compute, Human-Hours) and measures resource use at both the single-task level and the whole-industry level.

* **Unit Trade-Offs:** Compare candidate units — text chunks processed by the model (tokens: absent before 2020, jumps 1000x with reasoning and agent loops), electricity in watt-hours (Wh/MWh) and math operations (floating-point operations / FLOPs: reported for whole datacenters, rarely split by step), money in USD (mixes training costs, per-token API bills, and flat monthly subscriptions), and Human-Hours (shows human effort saved or spent, relies on surveys).
* **Single-Task Cost:** Estimate resource use for one single task run at Step $k$:
  * **Tokens & Compute:** Typical tokens and compute operations (FLOPs) per task ($10^2$ tokens for code autocomplete, $10^3$ for one chat turn, $10^6+$ for deep research or coding agent).
  * **Money & Energy:** Estimated USD cost and watt-hours (Wh) of electricity per task.
  * **Human-vs-AI Time:** Minutes of active human prompting/checking vs. minutes of independent AI runtime per task.
* **Industry-Wide Share:** Estimate the percentage share or rough scale of total AI spending, API token traffic, and active users at Step $k$ compared to the rest of the ladder during that era.
* **Data Fallback & Rough Math:** Follow a strict 3-step sequence for every metric: (1) use direct figures from published reports or papers when available, (2) use developer survey or API traffic proxies when direct figures are missing, and (3) calculate transparent back-of-the-envelope estimates showing the formula (such as typical tokens per task $\times$ era token price or watt-hours per token) and order-of-magnitude range ($10^2$ vs. $10^5$).

***

## How to Build the Ladders

**From Literature to Ladders:** Explains the step-by-step method for turning the literature review, usage data, courses, and news into a chronological series of ladders and steps.

* **Two-Shift Era Threshold:** Place all collected ladders, annual reports, courses, and news milestones onto a single timeline, and start a new Era Ladder ($L_t$) only when a breakthrough or $10\times$ cost drop causes **at least 2 structural step changes at once** — such as an old advanced step sinking into default Step 1 chat UI while a brand-new top step appears or an existing step splits (keeping era boundaries tied to major structural shifts rather than minor model updates).
* **Bottom-Up & Top-Down Pass:** Build each era's steps in two passes (empirical-to-conceptual followed by conceptual-to-empirical):
  * **Pass 1 — Bottom-Up Usage Clustering:** First, group the real workflows found in that era's courses, cookbooks, developer surveys, API logs, and news stories into natural clusters based on what people actually built and used.
  * **Pass 2 — Top-Down Ladder Cross-Check:** Next, compare those bottom-up clusters against the era's published ladders to adopt clear standard names where they match, keep practical steps that corporate ladders missed, and set aside speculative published steps (like "Autonomous Organizations") until an era where real usage data backs them.
* **No-Overlap & No-Gaps Rule:** Test every step in the ladder so the set of steps has no overlap and no gaps (mutually exclusive and collectively exhaustive / MECE):
  * **Two-of-Three Step Split Test:** Separate two workflows into distinct steps only when moving from Step $k$ to Step $k+1$ changes **at least 2 of 3 variables**: (1) **Task / Use-Case Complexity** (such as single line $\to$ single file $\to$ whole repository), (2) **Tool & Autonomy Setup** (such as single prompt $\to$ document search [RAG] $\to$ multi-step tool loop), and (3) **Single-Task Cost Scale** ($10\times$–$100\times$ jump in tokens, compute, or runtime); combine workflows that share the same scope, setup, and cost scale into a single step.
  * **Full Usage Coverage:** Ensure every major real-world workflow from that era's surveys, courses, and reports fits cleanly into one step on that era's ladder.
* **Cross-Era Links & Convergence Check:** Link every step in ladder $L_t$ to its matching step(s) in ladder $L_{t-1}$ using the change categories in Section 4.2, assign that era's reports, courses, surveys, and news stories into each step's **Use Cases** and **Step Resource Use**, and lock the master ladder skeleton once every step passes the no-overlap and no-gaps checks.

***

## Ladder Evolution

**Eras, Drivers & Step Changes:** Uses the method above to present the timeline of ladders, documenting each ladder's valid dates, why the old ladder became outdated, how steps changed, and total resources used.

### Era Dates & Why Old Ladders Get Outdated

**Tech, Cost & Habit Shifts:** Explains when each ladder was valid and the technical, economic, and workflow shifts that made the previous ladder outdated.

* **Evidence-Based Ladder List:** Determine the chronological list of ladders, their names, and their exact valid dates (`YYYY-MM` to `YYYY-MM`) from the literature and news review.
* **Technical Changes:** Detail breakthroughs that broke old limits — how much text a model can read at once (context window), training models to think step by step before answering (reinforcement learning with verifiable rewards / RLVR and test-time compute), built-in tool use, reading and clicking computer screens (GUI grounding), standard plugs for external tools and data (Model Context Protocol / MCP), and faster generation speeds.
* **Economic Changes:** Track drops in token prices (10x–100x cheaper per year) that made multi-step agent retries affordable, plus shifts from pay-per-token API bills to flat monthly subscriptions.
* **Workflow & Cultural Changes:** Track changes in user trust, moving from browser chat tabs into code editors and command-line terminals (IDE and CLI agent harnesses), free downloadable AI models (open-weight models), and everyday workplace habits.

### How Steps Change Between Eras

**New, Combined, Split & Gone Steps:** Tracks what happened to the steps when a new ladder replaced an old one.

* **New Top Steps:** Identify brand-new high-complexity steps at the top of the ladder and what technical or cost change made them possible.
* **Old Steps Sinking into Default UI:** Trace advanced technical steps from an older ladder that became simple built-in features of Step 1 in the next ladder (such as custom Python + Pinecone document search [RAG] becoming a single "Upload File" button in standard chat).
* **Split Steps:** Trace a single step splitting into multiple specialized steps (such as "AI Coding" splitting into instant line autocomplete, multi-file code editor chat, and background pull-request agents).
* **Combined or Gone Steps:** Document old steps that merged together or disappeared completely and explain why (such as standalone prompt marketplaces, brittle 2023 AutoGPT loops, or training custom small models to sort text [BERT fine-tuning]).

### Full-Ladder Resource Totals

**Era-Wide Resource Totals:** Estimates total resources used across the entire ladder during its valid time window.

* **Compute & Energy:** Total training and usage compute (FLOPs) and electricity (MWh) used across all steps of the ladder.
* **Spending & Tokens:** Total USD spent (API bills + subscriptions) and global token volume during the era.
* **Human Usage:** Total active users and human-hours spent across the full ladder.

***

## Steps in a Ladder

**Five-Part Step Profile:** Describes every individual step inside each ladder using the same 5 details.

* **Name & Rank:** Number steps from bottom (lowest task/use-case complexity) to top (highest task/use-case complexity) with a clear name.
* **Step Boundaries:** Explain how this step differs from the step below it (difference vs. Step $k-1$: what extra task complexity, context, or setup is needed) and the step above it (difference vs. Step $k+1$: what limit or failure stops it from handling harder tasks).
* **Concrete Tool Stack:** Name the exact models, software libraries, websites, tools, and setups people needed at Step $k$ during that era — such as early completion models (`text-davinci-003`), model hubs (HuggingFace `transformers`), document-search databases (FAISS, Pinecone) and orchestration libraries (LangChain, LlamaIndex), early agent loops (AutoGPT, BabyAGI), consumer web apps (ChatGPT Plus, Claude Artifacts), AI code editors and terminal agents (Cursor Composer, Claude Code), tool standards (MCP), fast model-serving engines (vLLM), and custom training tools (LoRA/QLoRA, DeepSpeed).
* **Use Cases & Context Switching:** Explain who uses AI at Step $k$, in what setting, and for what goal — populating each step's use cases with concrete examples from that era's annual AI reports, educational courses/cookbooks, developer surveys, and major news stories. Show how the **same person** switches between steps depending on the task (such as a developer using Step 1 autocomplete for single lines, Step 2 web chat for quick questions, and Step 4 terminal agent for multi-file changes), including famous real-world wins and failures.
* **Step Resource Use:** Estimate both single-task cost (tokens, USD, Wh, human minutes vs. AI runtime) and era-wide share (% of users, human-hours, and compute/tokens used at Step $k$), returning both prose and a structured data row (CSV/JSON) for visual plotting.

***

## Multi-Agent Execution Pipeline

**Four-Stage Agent Workflow:** Splits the research, era synthesis, deep-dive writing, and visual plotting across 4 coordinated stages so every era and step gets dedicated web search depth and output space.

* **Stage 1 — Parallel Literature Subagents (Section 2):** Spawn 2 research subagents in parallel to gather the raw evidence:
  * **Subagent 1A (Ladder Catalog):** Searches and reviews all published and informal AI, LLM, and agentic ladders across research papers, AI labs, enterprise frameworks, and developer blogs (Section 2.1).
  * **Subagent 1B (Yearly Evidence & Cost Setup):** Searches annual AI reports, API traffic logs, educational courses/cookbooks, developer surveys, and yearly news stories across all years, and compiles the historical token/compute/energy pricing baseline (Sections 2.2–2.3).
* **Stage 2 — Orchestrator Timeline & Schema Lock (Section 3):** The Lead Orchestrator combines Subagent 1A and 1B's findings using `How to Build the Ladders` (Section 3) to lock a single shared master skeleton before any era writing begins:
  * **Locked Era List:** Exact chronological list of Era Ladders ($L_1, L_2, \dots, L_n$) with valid `YYYY-MM` start and end dates.
  * **Locked Step Names & Links:** Verified step names ordered bottom-to-top inside each ladder $L_t$, plus the exact cross-era links showing how each step in $L_t$ evolved from $L_{t-1}$ (`New Top Step`, `Old Step Sinking into Default UI`, `Split Step`, `Combined or Gone Step`).
* **Stage 3 — Parallel Per-Era Subagents (Sections 4 & 5):** Spawn **one dedicated subagent per Era Ladder $L_t$** in parallel, passing each subagent the locked master skeleton and the Stage 1 evidence for its time window:
  * **Dedicated Era Deep Dive:** Each Era Subagent spends 100% of its search budget and output space on its single ladder $L_t$ — writing the era's valid dates and why the old ladder got outdated (Section 4.1), how its steps changed from $L_{t-1}$ (Section 4.2), the full 5-part profile for every step $1 \dots N$ populated with that era's courses, cookbooks, surveys, news stories, and 2-level cost math (Section 5), and full-ladder resource totals (Section 4.3).
  * **Structured Data Handoff:** Each Era Subagent also outputs a clean machine-readable table (CSV/JSON) of its steps' single-task and industry-wide numbers plus cross-era links.
* **Stage 4 — Visual Generation & Final Assembly (Section 7):** Combine all subagent outputs into the finished report:
  * **Visual & Synthesis Subagent:** Collects the structured CSV/JSON tables from all Era Subagents, runs code (Python `matplotlib` / SVG / HTML or the richest visual tool available) to render the in-section ladder diagrams and full-timeline summary visuals following `Drawing Style`, and drafts Part IV (`Overall Patterns & Summary Visuals`).
  * **Lead Orchestrator Assembly:** Merges Parts I–IV into one seamless document following `Output Report Blueprint` (Section 7) and runs the `Final Verification Checks` to confirm uniform style, matching cross-era links, and verified numbers.

***

## Output Report Blueprint

**Combined Report Structure:** Organize the final research report into 5 parts where each era's ladder section includes its own step-by-step breakdown and in-section visuals:

1. **Title, Summary & Index:** Report title, bottom-line summary (BLUF), and nested numbered table of contents (`Structural Index`).
2. **Part I — Literature & Cost Survey:**
   * **Ladder Literature Review:** Comprehensive review of all published and informal AI, LLM, and agentic ladders across research papers, AI labs, industry frameworks, educational guides, and developer communities.
   * **Step Use-Case Sources:** Overview of annual AI reports, educational courses/cookbooks, developer surveys, and yearly news stories gathered to populate the **Use Cases** of each step within each era's ladder.
   * **Resource Metrics:** Comparison of resource units, 3-step fallback and rough-math rules, and setup of the two-level measurement system (single-task cost vs. industry-wide share).
3. **Part II — Applied Ladder-Building Method:** Short standalone section documenting the concrete decisions made when running this research — which specific breakthroughs and usage shifts set the chosen era cutoff dates, which published ladder steps were combined or set aside as speculative, and how specific workflows from courses and surveys were grouped into steps.
4. **Part III — Chronological Ladder Evolution (One Section per Era's Ladder):** For each historical ladder $L_t$ in time order, present the ladder, its steps, and any in-section visuals together in one section:
   * **Valid Dates & Why Old Ladder Got Outdated:** Valid time window (`YYYY-MM` to `YYYY-MM`) and the technical, economic, and workflow changes that created $L_t$ and made $L_{t-1}$ outdated.
   * **How Steps Changed:** What changed compared to $L_{t-1}$ — new top steps, old steps sinking into default UI, split steps, and combined or gone steps.
   * **Step-by-Step Breakdown (Step $1 \dots N$):** Full 5-part profile for every step in $L_t$ (Name & Rank, Step Boundaries, Concrete Tool Stack, Use Cases & Context Switching — populated with that era's annual AI reports, courses/cookbooks, developer surveys, and news stories — and Step Resource Use), accompanied by in-section visuals where helpful.
   * **Full-Ladder Resource Totals:** Total compute, electricity, spending, token volume, and human usage across $L_t$.
5. **Part IV — Overall Patterns & Summary Visuals:**
   * **Long-Term Patterns:** Summary of repeating patterns across eras — how fast advanced steps sink into default consumer UI, how falling token prices unlock longer agent loops, and how human work shifts.
   * **Cross-Era Comparison & Visual Summary:** Summary comparison across all ladders (tables and full-timeline visuals) showing how steps, complexity, and resource use connect over time.

* **Final Verification Checks:** Before finishing the report, verify that: (1) every section and bullet uses bold 2–3 word lead-in labels (`**RIH:**`) and plain layman English with `plain meaning (technical term)` on first use, (2) every era ladder has exact `YYYY-MM` start and end dates, (3) every step includes all 5 profile parts plus both single-task and industry-wide resource estimates, (4) industry-wide user and token share percentages across the steps of each ladder add up to roughly 100%, and (5) every visual includes a standalone caption opening with a bold conclusion sentence.

