## 1. Part I — Extended Summary

**Part I Overview:** Condenses the nine-year historical, structural, and resource-cost synthesis (`2017-06` to `2026-10`) into a standalone 2,500-word executive digest (~5% of the full report). Summarizes the 18 published ladders and nine-year evidence base (Part II), the four-rule ladder construction method (Part III), the step-by-step evolution and resource economics of all five Era Ladders $L_1 \dots L_5$ across 23 complexity steps (Part IV), and the four macro evolutionary laws governing capability diffusion and compute concentration (Part V).

#### Part I Structural Index
1. [1.1 Literature, Evidence & Cost Synthesis (Part II Digest)](#11-literature-evidence--cost-synthesis-part-ii-digest)
   1. [1.1.1 Eighteen Published Ladders Across Labs, Industry & Practitioners](#111-eighteen-published-ladders-across-labs-industry--practitioners)
   2. [1.1.2 Nine Years of Evidence: Reports, Token Logs, Courses & Surveys](#112-nine-years-of-evidence-reports-token-logs-courses--surveys)
   3. [1.1.3 Single-Task vs. Industry-Wide Cost System & Price Deflation](#113-single-task-vs-industry-wide-cost-system--price-deflation)
2. [1.2 Applied Ladder-Building Method (Part III Digest)](#12-applied-ladder-building-method-part-iii-digest)
   1. [1.2.1 Two-Shift Era Threshold & Dual-Pass Usage Reconciliation](#121-two-shift-era-threshold--dual-pass-usage-reconciliation)
   2. [1.2.2 Two-of-Three Step Split Test & Cross-Era Linkage Rules](#122-two-of-three-step-split-test--cross-era-linkage-rules)
3. [1.3 Five Chronological Era Ladders (L1 to L5, 2017–2026) (Part IV Digest)](#13-five-chronological-era-ladders-l1-to-l5-20172026-part-iv-digest)
   1. [1.3.1 Era 1 (L1: 2017-06–2020-05) — Pre-LLM & Encoder NLP Ladder](#131-era-1-l1-2017-062020-05--pre-llm--encoder-nlp-ladder)
   2. [1.3.2 Era 2 (L2: 2020-06–2022-10) — Completion Models & Copilot Ladder](#132-era-2-l2-2020-062022-10--completion-models--copilot-ladder)
   3. [1.3.3 Era 3 (L3: 2022-11–2024-05) — Web Chat, Vector RAG & Early Agents Ladder](#133-era-3-l3-2022-112024-05--web-chat-vector-rag--early-agents-ladder)
   4. [1.3.4 Era 4 (L4: 2024-06–2025-01) — Multimodal Context, IDE Pairing & o1 Ladder](#134-era-4-l4-2024-062025-01--multimodal-context-ide-pairing--o1-ladder)
   5. [1.3.5 Era 5 (L5: 2025-02–2026-10) — Terminal CLI, Deep Research, MCP & Fleets Ladder](#135-era-5-l5-2025-022026-10--terminal-cli-deep-research-mcp--fleets-ladder)
4. [1.4 Evolutionary Laws & Executive Matrix (Part V Digest)](#14-evolutionary-laws--executive-matrix-part-v-digest)
   1. [1.4.1 Four Repeating Structural & Economic Laws (2017–2026)](#141-four-repeating-structural--economic-laws-20172026)
   2. [1.4.2 Condensed Five-Era Macro & 23-Step Executive Summary Table](#142-condensed-five-era-macro--23-step-executive-summary-table)

### 1.1 Literature, Evidence & Cost Synthesis (Part II Digest)

**Evidence Base Summary:** Unites 18 published hierarchies with nine years of usage logs, syllabi, and compute accounting across artificial intelligence (AI), large language models (LLMs), and action-taking AI (agentic AI).

#### 1.1.1 Eighteen Published Ladders Across Labs, Industry & Practitioners

**Published Framework Convergence:** Eighteen frameworks (`2017-11`–`2026-01`) divide into three traditions:

* **Academic & AI Lab Ladders:** Karpathy's *Software 1.0/2.0/3.0* (`2017-11`–`2025-06`) tracks programming shifting from code (*1.0*), to neural weights (*2.0*), to English prompts where active reading memory (context window) acts as RAM (*3.0*), paired with an *Autonomy Slider* from tab autocomplete to multi-file diffs and background agents. DeepMind's *Levels of AGI* (`2023-11`) separates skill percentile (L0–L5) from autonomy (L0–L5), while OpenAI's *Five Levels* (`2024-07`) orders *Chatbots (L1)*, *Reasoners (L2)*, *Agents (L3)*, *Innovators (L4)*, and *Organizations (L5)*. Anthropic's *Building Effective Agents* (`2024-12`) and *CoALA* (`2023-09`) separate fixed pipelines (*Workflows*) from model-driven tool loops (*Autonomous Agents*).
* **Industry, Venture & Coding Ladders:** Dan Shapiro (`2026-01`) and Steve Yegge (`2025-02`) adapt self-driving tiers (SAE L0–L5) to coding — from manual code (L0) and ghost text (`GitHub Copilot`, L1), to multi-file IDE pairing (`Cursor Composer`, L2–L3), terminal repo agents (`Claude Code`, L4), and parallel code-branch fleets (`git worktree` swarms, L5). LangChain (`2023-11`–`2024-06`), Hugging Face (`2024-02`–`2025-01`), venture firms (*a16z*, *Sequoia*, *Menlo Ventures*), and *Gartner* (`2020–2025`) map enterprise progression from chatbots to state graphs (`LangGraph`) and multi-agent coworkers.
* **Practitioner Intervention Hierarchies:** Applied guides (*Chip Huyen* `2023-04`, *Eugene Yan* `2023-07`, *OpenAI DevDay* `2023-11`, *Ruder* `2018-07`, *Liu et al.* `2021-07`) order interventions by cost: start with zero/few-shot prompting, add private document lookup (retrieval-augmented generation / RAG) for external facts, and reserve custom weight training (fine-tuning via `BERT` or `LoRA`) for latency or domain tone.

#### 1.1.2 Nine Years of Evidence: Reports, Token Logs, Courses & Surveys

**Four Empirical Grounding Pillars:** Populates every step from four historical data sources:

* **Annual Macro AI Reports:** *Stanford HAI AI Index* (`2018–2026`), *State of AI* (`2018–2025`), and *Epoch AI* track frontier training compute growing $4\times–5\times$ yearly — from $3.3\text{e}18$ math operations (floating-point operations / FLOPs, $\$930$) for 2017 `Transformer` and $1.9\text{e}20$ FLOPs ($\$3.3\text{k}$) for 2018 `BERT-Large`, to $3.14\text{e}23$ FLOPs ($\$4.3\text{M}$) for 2020 `GPT-3`, $2.15\text{e}25$ FLOPs ($\$78.4\text{M}$) for 2023 `GPT-4`, and $10^{26}+$ FLOPs in 2025–2026 — while organizational adoption rose from 20% (2017) to 78%–85%+ (2024–2026).
* **Paid API Traffic & Billing Logs:** *Menlo Ventures* (`2023–2025`), *OpenRouter* 100T-token logs, *Ramp*, and *Stripe* show enterprise GenAI spend surging from $\$1.7\text{B}$ (2023) to $\$13.8\text{B}$ (2024) and $\$37.0\text{B}$ (2025), while architectures flipped from fine-tuning (>60% in 2020–2022 to <9% in 2024) to custom RAG (51% in 2024) and then to 2M-token contexts, standard tool plugs (Model Context Protocol / `MCP`), and coding/agentic loops (>50% of commercial tokens in 2025–2026).
* **Syllabi, Surveys & News:** *Stanford CS224N/CS324*, *Fast.ai*, *DeepLearning.AI*, *Stack Overflow Surveys* (`2017–2025`, 84% AI tool adoption by 2025), *GitHub Octoverse*, and front-page wins/failures (*Mata v. Avianca*, `AutoGPT`, *Air Canada*, `Devin`, `DeepSeek-R1`, `Claude Code`) anchor each step.

#### 1.1.3 Single-Task vs. Industry-Wide Cost System & Price Deflation

**Two-Level Resource Accounting:** Measures every step at **Level 1 Single-Task Cost** and **Level 2 Industry-Wide Share** (summing to 100% per era):

* **Five Coupled Units:** (1) **Tokens** ($10^2$ autocomplete to $10^7$ fleets), (2) **FLOPs** ($C_{\text{infer}}\approx 2N_{\text{active}}T_{\text{task}}$; $C_{\text{train}}\approx 6N_{\text{params}}D_{\text{tokens}}$), (3) **Electricity in Wh/MWh** ($0.30\text{ Wh}$ chat vs. $40–150\text{ Wh}$ agent task), (4) **Money in USD**, and (5) **Human-vs-AI Time**.
* **The $2,000\times$ Price Deflation:** Baseline inference pricing fell from $\$60.00/1\text{M}$ tokens (`GPT-3 davinci`, `2020-06`) and $\$20.00/1\text{M}$ (`text-davinci-003`), down to $\$2.00/1\text{M}$ (`gpt-3.5-turbo`, `2023-03`), $\$0.15/1\text{M}$ (`gpt-4o-mini`, `2024-07`), and $\$0.03–\$0.06/1\text{M}$ on 2025–2026 flash and 90% KV-cached models.

### 1.2 Applied Ladder-Building Method (Part III Digest)

**Four-Rule Scientific Protocol:** Converts raw evidence into five Era Ladders ($L_1 \dots L_5$) with no overlap and no gaps (mutually exclusive and collectively exhaustive / MECE).

#### 1.2.1 Two-Shift Era Threshold & Dual-Pass Usage Reconciliation

**Timeline & Step Filtering:** Locks era cutoff dates and reconciles real usage against corporate frameworks:

* **Rule 1 — Two-Shift Era Threshold:** Opens a new Era Ladder ($L_t$) only when a breakthrough or $10\times$ price drop triggers **at least two simultaneous structural step changes**, keeping single-model upgrades (`GPT-2` `2019-02`, `GPT-4 Turbo` `2023-11`) inside existing eras.
* **Rule 2 — Bottom-Up + Top-Down Reconciliation:** Groups empirical workflows bottom-up first, then cross-checks against published ladders — adding practical steps missed by corporate charts ($L_1$ Step 1 cloud NLP APIs, $L_5$ Step 2 Deep Research) while setting aside unverified speculative rungs (OpenAI *L4/L5*, DeepMind *L5 ASI*).

#### 1.2.2 Two-of-Three Step Split Test & Cross-Era Linkage Rules

**Step Boundary & Lineage Rules:** Enforces strict step separation within each era and continuous lineage across eras:

* **Rule 3 — Two-of-Three Step Split Test:** Separates adjacent steps ($k\to k+1$) only when moving up changes **at least two of three variables**: (1) **Task Complexity Scope**, (2) **Tool & Autonomy Setup**, and (3) **Single-Task Cost Scale** ($10\times–100\times$ jump).
* **Rule 4 — Five Cross-Era Transition Categories:** Links every step in $L_t$ to $L_{t-1}$ as **Old Step Sinking into Default UI**, **Evolved Core Workhorse**, **Split & Specialized Step**, **New Breakthrough Top Step**, or **Combined / Gone Step**.

### 1.3 Five Chronological Era Ladders (L1 to L5, 2017–2026) (Part IV Digest)

**Nine-Year Chronological Synthesis:** Tracks all five Era Ladders and 23 complexity steps from `2017-06` to `2026-10`.

#### 1.3.1 Era 1 (L1: 2017-06–2020-05) — Pre-LLM & Encoder NLP Ladder

**Fine-Tuned Encoder Era (36 Months, 4 Steps):** Opened by `Transformer` (`2017-06`), `ULMFiT` (`2018-01`), and `BERT` (`2018-10`), spanning $1.8\text{M}$ users, $4.5\text{T}$ subwords, $1.5\text{e}23\text{ FLOPs}$, $0.95\text{ TWh}$, and $\$2.80\text{B}$:

* **$L_1$ Step 1 — Rule Engines & Cloud NLP APIs (62% Users, 15% Compute, 28% Spend):** `Regex`, `spaCy v2`, `scikit-learn`, and `AWS Comprehend`/`Google Cloud NLP` calls ($10^8\text{ FLOPs}$, $0.0005\text{ Wh}$, $\$0.0001$).
* **$L_1$ Step 2 — Static Word Vectors + Task RNNs/CNNs (23% Users, 25% Compute, 30% Spend):** `Word2Vec`/`GloVe` + `BiLSTM-CRF`/`CNN` classifiers ($10^{15}\text{ train FLOPs}$, $30\text{ Wh}$, $\$25/\text{run}$).
* **$L_1$ Step 3 — Pretrained Encoder Fine-Tuning (13% Users, 40% Compute, 27% Spend):** `BERT` and `RoBERTa` fine-tuned via `HuggingFace` on `V100` GPUs ($5\text{e}16\text{ train FLOPs}$, $200\text{ Wh}$, $\$50/\text{run}$).
* **$L_1$ Step 4 — From-Scratch Sequence & Deep RL (2% Users, 20% Compute, 15% Spend):** Multi-node `fairseq`, `tensor2tensor`, `BioBERT`, `GPT-2`, and `OpenAI Five` runs ($2\text{e}20\text{ FLOPs}$, $1.2\text{ MWh}$, $\$35,000+$).

#### 1.3.2 Era 2 (L2: 2020-06–2022-10) — Completion Models & Copilot Ladder

**Few-Shot Completion Era (29 Months, 4 Steps):** Triggered by `GPT-3 davinci` (`2020-06`) and `GitHub Copilot` (`2021-06`), eliminating $L_1$ Step 2 (`Word2Vec`+`BiLSTM`) across $4.5\text{M}$ users, $18\text{T}$ tokens, $3.5\text{e}25\text{ FLOPs}$, $0.24\text{ TWh}$, and $\$3.20\text{B}$:

* **$L_2$ Step 1 — Single-Line Autocomplete & Templates (50% Users, 18% Compute, 20% Spend):** `GitHub Copilot` (`Codex`), `TabNine`, and `Jasper.ai` ($250\text{ tok}$, $6\text{e}12\text{ FLOPs}$, $0.03\text{ Wh}$, $\$0.002$).
* **$L_2$ Step 2 — Zero/Few-Shot Completion Prompting (25% Users, 22% Compute, 18% Spend):** 3–5 example prompts in `OpenAI Playground` and `davinci` ($1,500\text{ tok}$, $5.25\text{e}14\text{ FLOPs}$, $1.75\text{ Wh}$, $\$0.06$).
* **$L_2$ Step 3 — Early Embedding Search & Chains (7% Users, 15% Compute, 12% Spend):** `FAISS`, `Pinecone` (`2021`), and `Haystack` bypassing 2k–4k context limits ($11,500\text{ tok}$, $4\text{e}15\text{ FLOPs}$, $13.3\text{ Wh}$, $\$0.40$).
* **$L_2$ Step 4 — Encoder & Open-Model Fine-Tuning (18% Users, 45% Compute, 50% Spend):** Production `RoBERTa`, `DeBERTa-v3`, `T5`, and `GPT-J-6B` fine-tuning on `A100` GPUs ($10^{19}\text{ train FLOPs}$, $3.2\text{ kWh}$, $\$450/\text{run}$).

#### 1.3.3 Era 3 (L3: 2022-11–2024-05) — Web Chat, Vector RAG & Early Agents Ladder

**ChatGPT & Custom RAG Era (19 Months, 5 Steps):** Ignited by `ChatGPT` (`2022-11`), `gpt-3.5-turbo` at $\$2/1\text{M}$ (`2023-03`), `GPT-4`, and `LLaMA`, reaching $250\text{M}$ users, $450\text{T}$ tokens, $1.8\text{e}26\text{ FLOPs}$, $0.50\text{ TWh}$, and $\$10.5\text{B}$ ($\$1.7\text{B}$ enterprise):

* **$L_3$ Step 1 — Single-Turn Chat & Autocomplete (68% Users, 32% Compute, 28% Spend):** Conversational RLHF sank $L_2$ Step 2 prompting into free `ChatGPT`, `Bing Chat`, and `Copilot` ($1,200\text{ tok}$, $2\text{e}14\text{ FLOPs}$, $0.30\text{ Wh}$, $\$0.002$).
* **$L_3$ Step 2 — Multi-Turn Prompting & Personas (20% Users, 28% Compute, 35% Spend):** `ChatGPT Plus` (`GPT-4`), `Claude 2` 100k, `Custom GPTs`, CoT, and JSON mode ($6,000\text{ tok}$, $1.5\text{e}16\text{ FLOPs}$, $1.50\text{ Wh}$, $\$0.21$).
* **$L_3$ Step 3 — Custom Vector Document Search (RAG) (8% Users, 23% Compute, 24% Spend):** `LangChain`/`LlamaIndex` + `Pinecone`/`ChromaDB` over corporate PDFs ($20,000\text{ tok}$, $5\text{e}16\text{ FLOPs}$, $4.0\text{ Wh}$, $\$0.65$).
* **$L_3$ Step 4 — Parameter-Efficient Fine-Tuning (3% Users, 10% Compute, 8% Spend):** `LLaMA-2` and `Mistral-7B` tuned via 4-bit `LoRA`/`QLoRA` on `vLLM` ($5\text{e}18\text{ train FLOPs}$, $6.0\text{ kWh}$, $\$45/\text{run}$).
* **$L_3$ Step 5 — Experimental Agent Loops (1% Users, 7% Compute, 5% Spend):** Recursive `AutoGPT` and `BabyAGI` loops ($180,000\text{ tok}$, $4\text{e}17\text{ FLOPs}$, $25\text{ Wh}$, $\$6.00$), suffering $>90\%$ failure.

#### 1.3.4 Era 4 (L4: 2024-06–2025-01) — Multimodal Context, IDE Pairing & o1 Ladder

**Sonnet 3.5, Cursor & o1 Era (8 Months, 5 Steps):** Triggered by `GPT-4o`, `Claude 3.5 Sonnet` + `Artifacts` (`2024-06`), 90% KV-cache discounts, `Cursor Composer`, and `OpenAI o1` (`2024-09`), spanning $480\text{M}$ users, $350\text{T}$ tokens, $9.0\text{e}25\text{ FLOPs}$, $3.80\text{ TWh}$, and $\$18.5\text{B}$ ($\$13.8\text{B/yr}$ enterprise):

* **$L_4$ Step 1 — Multimodal Chat + Built-In Upload (62% Users, 22% Compute, 20% Spend):** 200k–2M contexts sank $L_3$ Step 3 single-PDF RAG into `Claude Projects`, `NotebookLM`, `Artifacts`, and `GPT-4o` upload ($5,500\text{ tok}$, $3\text{e}15\text{ FLOPs}$, $0.50\text{ Wh}$, $\$0.018$).
* **$L_4$ Step 2 — Single-Call Reasoning via RLVR (12% Users, 16% Compute, 14% Spend):** `OpenAI o1` and `DeepSeek-R1` spending 5k–30k hidden thinking tokens on math, logic, and architecture ($25,000\text{ tok}$, $4\text{e}16\text{ FLOPs}$, $5.0\text{ Wh}$, $\$0.42$).
* **$L_4$ Step 3 — Multi-File IDE Pairing & Hybrid RAG (18% Users, 34% Compute, 36% Spend):** `Cursor Composer`, `Windsurf`, and reranked RAG with 90% KV-cache discounts ($70,000\text{ tok}$, $8\text{e}16\text{ FLOPs}$, $6.0\text{ Wh}$, $\$0.30$).
* **$L_4$ Step 4 — Stateful Graph Workflows (6% Users, 18% Compute, 18% Spend):** `LangGraph`, `CrewAI`, and `AutoGen` cyclic state machines replacing `AutoGPT` ($200,000\text{ tok}$, $2\text{e}17\text{ FLOPs}$, $15\text{ Wh}$, $\$1.10$).
* **$L_4$ Step 5 — Cloud Sandbox & Screen Agents + DPO (2% Users, 10% Compute, 12% Spend):** `Cognition Devin`, `Anthropic Computer Use`, and `Llama-3.1` `DPO` ($1,200,000\text{ tok}$, $1.5\text{e}18\text{ FLOPs}$, $45\text{ Wh}$, $\$6.80$).

#### 1.3.5 Era 5 (L5: 2025-02–2026-10) — Terminal CLI, Deep Research, MCP & Fleets Ladder

**Agentic Harness & Fleet Era (21 Months, 5 Steps):** Opened by `OpenAI Deep Research` & `Claude Code` (`2025-02`), universal `MCP` (`2025-03`), and tool-integrated RLVR (`o3`, `Claude 4`, `GPT-5`), spanning $1.15\text{B}$ users, $180\text{Q}$ tokens, $6.5\text{e}26\text{ FLOPs}$, $48.0\text{ TWh}$, and $\$95.0\text{B}$ ($\$37\text{B}–\$55\text{B/yr}$ enterprise):

* **$L_5$ Step 1 — Auto-Routed Hybrid Chat & Tab Edit (55% Users, 12% Compute, 20% Spend):** $L_4$ Step 2 reasoning sank into auto-routers inside `GPT-5`, `Claude 4 Sonnet`, `Gemini 2.5 Flash`, and `Cursor Tab` ($3,500\text{ tok}$, $2\text{e}15\text{ FLOPs}$, $0.30\text{ Wh}$, $\$0.008$).
* **$L_5$ Step 2 — Autonomous Deep Research & Synthesis (18% Users, 16% Compute, 18% Spend):** `OpenAI`, `Gemini`, and `Perplexity Deep Research` running 10–30 minute multi-source synthesis ($300,000\text{ tok}$, $3\text{e}17\text{ FLOPs}$, $18\text{ Wh}$, $\$1.50$).
* **$L_5$ Step 3 — Standardized `MCP` Workflows & Scoped IDE (15% Users, 22% Compute, 25% Spend):** Universal `MCP` servers paired with `Cursor`/`Windsurf` Agent Mode ($150,000\text{ tok}$, $1.8\text{e}17\text{ FLOPs}$, $10\text{ Wh}$, $\$0.55$).
* **$L_5$ Step 4 — Autonomous Terminal CLI & Repo Agents (9% Users, 30% Compute, 22% Spend):** `Claude Code` CLI, `OpenAI Codex CLI`/Cloud, and `Cline` running bash, tests, and PRs ($1,300,000\text{ tok}$, $1.5\text{e}18\text{ FLOPs}$, $40\text{ Wh}$, $\$3.20$).
* **$L_5$ Step 5 — Parallel Agent Fleets & RLVR Flywheels (3% Users, 20% Compute, 15% Spend):** 3–10 concurrent `Claude Code`/`Codex` `git worktree` agents and custom `GRPO` RLVR post-training ($8,000,000\text{ tok}$, $8\text{e}18\text{ FLOPs}$, $150\text{ Wh}$, $\$20.00$).

### 1.4 Evolutionary Laws & Executive Matrix (Part V Digest)

**Macro Laws & Master Matrix:** Distills the nine-year empirical record into four governing laws and a unified five-era reference table.

#### 1.4.1 Four Repeating Structural & Economic Laws (2017–2026)

**Four Empirical Invariants:** Across every transition from $L_1$ to $L_5$, four quantitative rules held without exception:

* **Law 1 — The 18-Month Downward Sinking Law:** Every 18–24 months, an advanced workflow at Step 2 or Step 3 sinks into the zero-setup **Step 1 Default UI** of the next era (`GPT-3` API prompting $\to$ free `ChatGPT`; custom single-PDF `Pinecone` RAG $\to$ native file upload; standalone `o1` reasoning $\to$ `GPT-5`/`Claude 4` auto-routed chat).
* **Law 2 — The Price-to-Horizon Jevons Paradox:** A $2,000\times$ drop in unit token price ($\$60/1\text{M}\to\$0.06/1\text{M}$) triggered a $4,000\times$ surge in top-step task tokens ($2\text{k}\to 8\text{M}$ tokens) and a $22\times$ surge in annual enterprise GenAI spending ($\$1.7\text{B}\to\$37.0\text{B}+$).
* **Law 3 — The Pareto Compute & Token Inversion:** While Step 1 serves 50%–68% of users at sub-cent cost, the top 12% of users in Era 5 (Steps 4 and 5) consume **50% of all global tokens and datacenter electricity** ($r=0.60$ power-law concentration).
* **Law 4 — Upward Migration of Human Engineering Labor:** Human bottlenecks shifted from *Dataset Curator* ($L_1$) $\to$ *Few-Shot Crafter* ($L_2$) $\to$ *RAG Plumber* ($L_3$) $\to$ *Multi-File Diff Reviewer* ($L_4$) $\to$ *Parallel Fleet Commander & Verifier Architect* ($L_5$).

#### 1.4.2 Condensed Five-Era Macro & 23-Step Executive Summary Table

**Complete Era-and-Step Digest:** Summarizes valid dates, macro totals, step hierarchies, single-task scales, and user/compute/spend shares across $L_1 \dots L_5$.

| Era & Window | Macro Totals | Ordered Steps ($S_1 \dots S_N$) | Single-Task Scale ($S_1 \to S_N$) | User/Compute/Spend % |
| :--- | :--- | :--- | :--- | :--- |
| **$L_1$** (`2017-06`–`2020-05`) | $1.8\text{M}\cdot 4.5\text{T}\cdot 1.5\text{e}23\cdot 0.95\text{TWh}\cdot\$2.8\text{B}$ | **S1:**Regex/API·**S2:**`Word2Vec`·**S3:**`BERT`·**S4:**Scratch/RL | $50\to 2\text{k}$ tok·$10^8\to 2\text{e}20$ FLOPs·$\$0.0001\to\$35\text{k}$ | 62/23/13/2%·15/25/40/20%·28/30/27/15% |
| **$L_2$** (`2020-06`–`2022-10`) | $4.5\text{M}\cdot 18\text{T}\cdot 3.5\text{e}25\cdot 0.24\text{TWh}\cdot\$3.2\text{B}$ | **S1:**`Copilot`·**S2:**`GPT-3`·**S3:**`FAISS`·**S4:**`RoBERTa` FT | $250\to 50\text{k}$ tok·$6\text{e}12\to 10^{19}$ FLOPs·$\$0.002\to\$450$ | 50/25/7/18%·18/22/15/45%·20/18/12/50% |
| **$L_3$** (`2022-11`–`2024-05`) | $250\text{M}\cdot 450\text{T}\cdot 1.8\text{e}26\cdot 0.50\text{TWh}\cdot\$10.5\text{B}$ | **S1:**Chat·**S2:**`GPT-4`·**S3:**RAG·**S4:**`QLoRA`·**S5:**`AutoGPT` | $1.2\text{k}\to 180\text{k}$ tok·$2\text{e}14\to 4\text{e}17$ FLOPs·$\$0.002\to\$6$ | 68/20/8/3/1%·32/28/23/10/7%·28/35/24/8/5% |
| **$L_4$** (`2024-06`–`2025-01`) | $480\text{M}\cdot 350\text{T}\cdot 9.0\text{e}25\cdot 3.80\text{TWh}\cdot\$18.5\text{B}$ | **S1:**Multimodal·**S2:**`o1`/`R1`·**S3:**`Cursor`·**S4:**`LangGraph`·**S5:**`Devin` | $5.5\text{k}\to 1.2\text{M}$ tok·$3\text{e}15\to 1.5\text{e}18$ FLOPs·$\$0.018\to\$6.80$ | 62/12/18/6/2%·22/16/34/18/10%·20/14/36/18/12% |
| **$L_5$** (`2025-02`–`2026-10`) | $1.15\text{B}\cdot 180\text{Q}\cdot 6.5\text{e}26\cdot 48.0\text{TWh}\cdot\$95.0\text{B}$ | **S1:**Auto-Chat·**S2:**`Deep Research`·**S3:**`MCP`·**S4:**`Claude Code`·**S5:**Fleets | $3.5\text{k}\to 8\text{M}$ tok·$2\text{e}15\to 8\text{e}18$ FLOPs·$\$0.008\to\$20$ | 55/18/15/9/3%·12/16/22/30/20%·20/18/25/22/15% |

***
