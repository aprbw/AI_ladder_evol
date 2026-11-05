### 3.4 Era 4 Ladder ($L_4$: 2024-06 to 2025-01) — Built-In Multimodal Context, Multi-File IDE Pairing & First Reasoning Models Ladder

**Era 4 Summary:** Over the eight months from June 2024 to January 2025 (*"The Sonnet 3.5, Cursor & o1 Era"*), three breakthroughs reshaped how people used AI: 200k-to-2M token reading windows paired with 90% cheaper saved prompt memory (key-value cache / KV-cache) pushed 2023's custom document-search code directly into free consumer chat upload buttons; training models to think step by step before answering (reinforcement learning with verifiable rewards / RLVR test-time compute) created a dedicated reasoning step with `OpenAI o1` and `DeepSeek-R1`; and multi-file code editors (`Cursor Composer`, `Windsurf`) plus state-machine graphs (`LangGraph`) replaced Era 3's single-file chat copy-pasting and fragile `AutoGPT` loops across $13.8B in annual enterprise generative AI spending.

***

#### 3.4.1 Valid Dates & Why Era 3 Got Outdated

**Shift Drivers Summary:** Era 4 ran for eight intense months from `2024-06` to `2025-01`, triggered when native image-and-voice models, 200k-token workspace memory, 90% prompt cache discounts, and internal chain-of-thought reasoning models arrived together and made Era 3's single-PDF vector databases, manual chain-of-thought prompt hacks, and unconstrained agent loops outdated.

* **Exact Era Window:** `2024-06` to `2025-01` (8 months):
  * **Opening Trigger (`2024-05` to `2024-09`):** Opened with OpenAI's native voice-and-vision `GPT-4o` (`2024-05`), Anthropic's `Claude 3.5 Sonnet` (`2024-06`, introducing live side-by-side `Artifacts` previews and `Projects` workspace memory), Anthropic's 90% KV-cache prompt caching discount (`2024-08`), `Cursor Composer` multi-file code editing (`2024-06` to `2024-09`), and OpenAI's `o1-preview` (`2024-09`, the first commercial model trained with RLVR test-time compute).
  * **Closing Boundary (`2025-01`):** Closed in late January 2025 with the open-weight release of `DeepSeek-R1` (`2025-01-20`, matching `o1` math and logic performance at $27\times$ lower API pricing and triggering a $589B single-day Nvidia market-value drop on `2025-01-27`) and OpenAI's `o3-mini` (`2025-01-31`), right before `OpenAI Deep Research` (`2025-02`), `Claude Code` CLI (`2025-02`), and universal tool plugs (Model Context Protocol / MCP) opened Era 5.
* **Technical Shifts:** Five model and systems breakthroughs broke Era 3's architectural limits:
  * **Long Context Windows:** Reading capacity jumped from Era 3's standard 4k–32k tokens to 128k tokens (`GPT-4o`), 200k tokens (`Claude 3.5 Sonnet` — roughly 500 pages of text), and 1M–2M tokens (`Gemini 1.5 Flash` and `Gemini 1.5 Pro`), letting users drop entire books, legal contracts, or 20-file code modules directly into a single prompt.
  * **Native Multimodal Input:** Instead of piping separate speech-to-text, optical character recognition (OCR), and text models together, single models (`GPT-4o`, `Gemini 1.5 Pro`, `Claude 3.5 Sonnet`) natively read high-resolution charts, UI screenshots, PDF page layouts, audio streams, and video recordings in one pass.
  * **Internal Reasoning Scaling:** Rather than relying on users to type *"think step by step"* into the prompt, labs trained models via reinforcement learning with verifiable math and code rewards (RLVR) to generate 5,000 to 35,000 hidden thinking tokens before writing the final answer (`OpenAI o1-preview`, `o1`, `o1-mini`, `QwQ-32B`, `DeepSeek-R1`), jumping from 13% (`GPT-4o`) to 83% (`o1`) and 79.8% (`DeepSeek-R1`) on the American Invitational Mathematics Examination (AIME 2024).
  * **Multi-File IDE Grounding:** Code editors evolved from single-line ghost text (`GitHub Copilot` 2022) and sidebar chat into repository-indexed multi-file diff engines (`Cursor Composer`, `Codeium Windsurf Cascade`, `GitHub Copilot Edits`) that read project dependency graphs and apply synchronized red/green code edits across 5 to 10 files at once.
  * **Screen & Sandbox Action:** Models gained early pixel-level screen reading and mouse/keyboard control (graphical user interface / GUI grounding in `Anthropic Computer Use`, scoring 14.9% single-pass and 22.0% extended on the OSWorld desktop benchmark vs. 7.8% prior state of the art) alongside cloud virtual-machine coding sandboxes (`Cognition Devin`, `SWE-agent`, `OpenHands`).
* **Economic Shifts:** A $13\times$ to $100\times$ collapse in token prices paired with saved prompt memory unlocked context-heavy workflows:
  * **Sub-Dollar Small Models:** In July 2024, `gpt-4o-mini` launched at **$0.15 input / $0.60 output per 1M tokens** (replacing `gpt-3.5-turbo` at $13\times$ lower cost while beating `GPT-4` on early chat leaderboards), alongside `Gemini 1.5 Flash` at **$0.075 input / $0.30 output per 1M tokens** — a $280\times$ drop from late-2022 `GPT-3.5`-equivalent pricing (*Stanford HAI AI Index 2025*).
  * **Open-Weight MoE Deflation:** In December 2024 and January 2025, `DeepSeek-V3` (a 671B-parameter sparse mixture-of-experts / MoE model activating only 37B parameters per token, trained for $5.58M across 2.788M H800 GPU hours) and `DeepSeek-R1` priced commercial API access at **$0.14 input / $0.28 output** and **$0.55 input / $2.19 output per 1M tokens**, cutting frontier reasoning costs by $27\times$ below `OpenAI o1` ($15.00 input / $60.00 output).
  * **Prompt Cache Discounts:** Saving pre-computed attention states in GPU memory (KV-cache prompt caching) launched on DeepSeek and Anthropic (`2024-08`, **90% read discount**, dropping `Claude 3.5 Sonnet` repeated input from $3.00 to **$0.30 per 1M tokens**) and OpenAI (`2024-10`, **50% discount**), making it economical for IDE coding agents and enterprise document pipelines to re-send 50,000+ context tokens across 20 consecutive turns.
  * **Enterprise Spend Surge:** According to *Menlo Ventures' 2024 State of Generative AI in the Enterprise*, corporate generative AI spending grew $8\times$ from **$1.7B in 2023 to $13.8B in 2024**, while *McKinsey / Stanford HAI* organizational AI adoption surged from a 55% plateau in 2023 to **72%–78% in 2024** and *OpenAI* introduced the **$200/month `ChatGPT Pro`** tier (`2024-12`) for heavy `o1 pro mode` compute users.
* **Workflow & Cultural Shifts:** Everyday habits moved from copy-pasting snippets in browser tabs to live workspace co-editing and controlled state graphs:
  * **In-App Workspace Previews:** Users stopped treating web chat as a text-only Q&A box; `Claude Artifacts` (`2024-06`) rendered live interactive React apps, SVG diagrams, and games right beside the chat thread, while `Google NotebookLM` (`2024-09`) turned uploaded PDFs and slides into viral two-host AI audio podcasts.
  * **Chat-Oriented Programming:** As documented in the *2024 Stack Overflow Developer Survey* (**76% of developers using or planning to use AI tools**, **62% actively using**) and *GitHub Octoverse 2024* (where **Python overtook JavaScript as the #1 language on GitHub** for the first time on the back of AI workloads), startup and indie engineers migrated en masse from `VS Code + Copilot` autocomplete to `Cursor` and `Windsurf` multi-file `Cmd+I` editing.
  * **Graph Guardrails Over Loops:** After 2023's `AutoGPT` and `BabyAGI` burned API budgets in infinite loops, enterprise teams adopted Anthropic's *Building Effective Agents* (`2024-12`) rule — building predictable, code-controlled state graphs (`LangGraph`) and structured JSON schemas (`OpenAI Structured Outputs`, `2024-08`, hitting 100% schema compliance) before attempting open-ended agents.

***

#### 3.4.2 How Steps Changed from Era 3 to Era 4

**Structural Transitions Summary:** Crossing from Era 3 ($L_3$: `2022-11` to `2024-05`) into Era 4 ($L_4$: `2024-06` to `2025-01`) triggered four simultaneous structural changes across the ladder — sinking single-project RAG and custom personas into default Step 1 chat, inserting RLVR single-call reasoning at Step 2, splitting coding and RAG into multi-file IDE pairing at Step 3, and replacing Era 3's unconstrained `AutoGPT` loops with state-machine graphs at Step 4 and sandboxed desktop/cloud agents at Step 5.

* **Old Steps Sinking into Default UI ($L_3$ Steps 2 & 3 $\to$ $L_4$ Step 1):**
  * **Single-Folder RAG Sinks:** In Era 3, answering questions over 10 to 50 PDFs required Step 3 Python engineering — writing `LangChain` chunkers, generating `text-embedding-ada-002` vectors, and hosting a `Pinecone` or `Chroma` index. In Era 4, 200k–2M context windows plus built-in workspace retrieval sank single-project document Q&A into zero-code Step 1 consumer apps (`Claude Projects`, `Google NotebookLM`, `ChatGPT-4o` file upload, and `Perplexity Pro` live web-and-file search).
  * **Custom Personas Sink:** Era 3 Step 2 multi-turn prompt crafting (`Custom GPTs`, system prompt templates, and manual UI mockup coding) became standard Step 1 features via persistent project instructions and `Claude Artifacts` live interactive previews.
* **New Steps ($L_4$ Step 2 & $L_4$ Step 5):**
  * **New Step 2 (RLVR Reasoning):** `OpenAI o1-preview`/`o1` (`2024-09`/`12`) and `DeepSeek-R1` (`2025-01`) created a brand-new Step 2 between fast conversational chat (Step 1) and multi-file IDE/RAG tooling (Step 3), where a single prompt triggers 10 to 90 seconds of autonomous internal test-time compute ($15\text{k}–40\text{k}$ thinking tokens) to solve competition math, formal logic, and subtle race-condition bugs that defeated every Era 3 model.
  * **New Top Step 5 (Sandboxes):** At the top of the ladder, full Linux container sandboxes (`Cognition Devin`, `SWE-agent`, `OpenHands`) and pixel-level desktop control (`Anthropic Computer Use` beta) combined with preference post-training (`Llama-3.1` Direct Preference Optimization / DPO and synthetic reasoning distillation) to form a new Step 5 executing 30-to-100-step autonomous software and GUI runs.
* **Split & Evolved Steps ($L_3$ Steps 1–3 $\to$ $L_4$ Step 3; $L_3$ Step 5 $\to$ $L_4$ Step 4):**
  * **Coding & RAG Split Upward:** While single-line tab autocomplete and single-file chat stayed in Step 1, professional software engineering and corporate search evolved into $L_4$ Step 3 — combining multi-file IDE AI pairing (`Cursor Composer`, `Windsurf Cascade`, `Copilot Edits`) with production enterprise hybrid search (combining keyword matching [BM25] + vector embeddings + neural cross-encoder reranking [`Cohere Rerank 3`] + 90% KV-cache prompt caching).
  * **Brittle Loops Become State Graphs:** Era 3 Step 5 experimental recursive scripts (`AutoGPT`) evolved into $L_4$ Step 4 controlled state machines (`LangGraph`, `LlamaIndex Workflows`) and role-based multi-agent pipelines (`CrewAI`, `AutoGen`), where human engineers hard-code the allowed transition edges, reflection checkpoints, and human-in-the-loop approval gates.
* **Combined or Gone Steps ($L_3$ Step 2, Step 4 & Step 5 Consolidations):**
  * **Unconstrained `AutoGPT` Loops Gone:** Raw unconstrained `while True` prompt loops (`AutoGPT` 2023) disappeared from production engineering due to compounding hallucinations and runaway token bills, replaced by bounded Step 4 state graphs and Step 5 isolated Docker sandboxes.
  * **Routine Style `LoRA` Absorbed:** Roughly 70% of Era 3 Step 4 open-weight adapter training (`LoRA` / `QLoRA` used simply to teach a model company tone or JSON formatting) vanished as 200k long context, 90% KV-cache discounts, and 100%-reliable `OpenAI Structured Outputs` made in-context few-shot prompting cheaper and more accurate; remaining weight training consolidated into Step 5 post-training (DPO alignment and distilling `o1`/`DeepSeek-R1` reasoning traces into compact 8B–70B models).

```
ERA 3 LADDER (2022-11 to 2024-05)                  ERA 4 LADDER (2024-06 to 2025-01)
=================================                  =================================
Step 5: Experimental Autonomous   ---[Gone/Tamed]--> Step 5: Cloud Sandbox & Screen Agents + DPO
        Loops (AutoGPT, BabyAGI)        |                    (Devin, Computer Use, Llama-3.1 DPO)
                                        +----------> Step 4: Stateful Graph & Multi-Agent Workflows
Step 4: Open-Weight LoRA/QLoRA    ---[Consolidated]^         (LangGraph, CrewAI, AutoGen, Workflows)
        Fine-Tuning (LLaMA-2)
                                  +----------------> Step 3: Multi-File IDE Pairing & Hybrid RAG
Step 3: Custom Vector Document    |                          (Cursor Composer, Windsurf, Rerank+Cache)
        Search / RAG (LangChain) -+--[Sinks to UI]
                                                   > Step 2: Single-Call Reasoning Models [NEW STEP]
Step 2: Multi-Turn Prompting &    ---[Sinks to UI]-+         (OpenAI o1-preview/o1, DeepSeek-R1)
        Personas (Custom GPTs)                     |
                                                   v
Step 1: Single-Turn Web Chat &    -----------------> Step 1: Multimodal Chat, Built-In File/Web Search
        Autocomplete (ChatGPT)                               & Previews (GPT-4o, Sonnet 3.5, NotebookLM)
```
**Figure 3.4 — Era 3 to Era 4 Structural Ladder Shift: Long context windows and 90% prompt cache discounts pushed 2023 custom RAG code into 2024 default chat UI while test-time reasoning (`o1`, `DeepSeek-R1`) and multi-file IDE agents (`Cursor`) created new middle and upper rungs.**

***

#### 3.4.3 Step-by-Step Breakdown (Steps 1 to 5)

**Five-Rung Complexity Profile:** Orders every real-world workflow from June 2024 to January 2025 across five mutually exclusive steps, rising from 5,000-token multimodal workspace chat (Step 1: 62% of users) up to 1,200,000-token cloud sandbox and desktop agents (Step 5: 2% of users).

##### Step 1: Multimodal Web Chat with Built-In File Upload, Search & Live Previews

* **Name & Rank:** **Step 1 (Lowest Complexity / Mass Default Foundation) — Multimodal Web Chat with Built-In File Upload, Search & Live Previews.**
* **Step Boundaries:**
  * **Entry Baseline (Bottom Rung):** Serves as the zero-setup entry point for all consumers, students, analysts, and developers, plus inline single-line code completions (`GitHub Copilot`, `Cursor Tab`); absorbs Era 3 Step 2 (`Custom GPT` personas) and Era 3 Step 3 (single-project PDF vector RAG) into native drag-and-drop browser workspaces requiring zero Python or API keys.
  * **Upper Ceiling vs. Step 2:** Runs on fast single-pass generation (`GPT-4o`, `Claude 3.5 Sonnet`, `Gemini 1.5 Pro`) without extended hidden chain-of-thought verification loops; when faced with olympiad math, complex algorithmic proofs, or deep multi-constraint logic puzzles, Step 1 models guess plausible-sounding wrong answers, requiring users to step up to Step 2 RLVR reasoning models (`o1`, `DeepSeek-R1`) or Step 3 multi-file IDE editors.
* **Concrete Tool Stack:**
  * **Consumer & Workspace Web Apps:** `ChatGPT` powered by `GPT-4o` and `gpt-4o-mini` (with built-in web browsing, Advanced Voice Mode, vision upload, and Python `Data Analysis` sandbox), `Claude.ai` powered by `Claude 3.5 Sonnet` (`Artifacts` live code/UI preview pane and `Projects` 200k-token workspace knowledge bases), `Google NotebookLM` (source-grounded workspace with `Audio Overviews` two-host podcast generation), `Perplexity` (real-time citation search engine), and `Google AI Studio` / `Gemini Advanced` (`Gemini 1.5 Pro` 2M-token context window and `Gemini 1.5 Flash` 1M-token window).
  * **Inline Code Autocomplete:** `GitHub Copilot` inline ghost text in `VS Code` and `Cursor Tab` multi-line cursor-jump autocomplete.
* **Use Cases & Context Switching:**
  * **Courses & Guides:** *Anthropic's Prompt Engineering Interactive Tutorial* (`2024`), *Google Prompting Essentials* (`2024`), and *DeepLearning.AI's* `Prompt Engineering for Vision Models` taught millions of knowledge workers how to combine PDFs, screenshots, and voice prompts inside native chat workspaces.
  * **Surveys & Adoption Reports:** *McKinsey / Stanford HAI AI Index (2025)* recorded organizational generative AI adoption leaping to **72%–78% in 2024**, while *Stack Overflow's 2024 Developer Survey* (65,000+ developers) showed **76% using or planning to use AI tools** with `ChatGPT` (82%) and `GitHub Copilot` (41%) anchoring daily Step 1 lookup and autocomplete.
  * **Famous Wins & Failures:** In June 2024, `Claude 3.5 Sonnet Artifacts` went viral as non-programmers built and played interactive React dashboards, physics simulations, and retro video games inside a split browser window in 30 seconds; in September 2024, `Google NotebookLM Audio Overviews` went viral across universities and businesses by turning dry 100-page PDFs and research papers into lifelike 12-minute banter between two AI podcast hosts. Conversely, in May 2024, `Google AI Overviews` launched in US search results and suffered a front-page failure when unverified Reddit jokes caused the model to advise users to put non-toxic glue on pizza to keep cheese from sliding off and to eat one small rock per day for vitamins; meanwhile, the February 2024 tribunal ruling in **_Moffatt v. Air Canada_** proved that companies remain legally liable when a basic web support chatbot hallucinates refund rules.
  * **Same-Person Context Switching:** A full-stack software engineer starts the morning at **Step 1**, dragging a client's 40-page product PDF and a whiteboard smartphone photo into `Claude Projects` (`Claude 3.5 Sonnet`) to generate an interactive `Artifact` wireframe prototype, while accepting single-line `Cursor Tab` completions for boilerplate imports — before switching to Step 2 (`o1`) for a tricky database deadlock and Step 3 (`Cursor Composer`) for multi-file backend implementation.
* **Step Resource Use:**
  * **Single-Task Cost (Level 1):** One multimodal workspace or file-grounded chat turn processes **$\sim 3,000\text{ to }8,000\text{ tokens}$** (such as $4,800$ input tokens from an uploaded document/image + $700$ output tokens $\approx 5.5 \times 10^3\text{ tokens}$). Using the forward-pass compute equation ($\text{FLOPs} \approx 2 \cdot N_{\text{active}} \cdot T_{\text{total}}$ with $N_{\text{active}} \approx 1.0 \times 10^{11}$ to $2.5 \times 10^{11}$ including multimodal vision encoding and attention prefill), one task executes **$\sim 3.0 \times 10^{15}\text{ FLOPs}$**, costs **$\$0.01\text{ to }\$0.03$** at `GPT-4o` ($2.50/$10.00 per 1M) or `Claude 3.5 Sonnet` ($3.00/$15.00 per 1M) API rates (or $\$0.001$ on `gpt-4o-mini` / covered by flat $\$20/\text{month}$ subscriptions), and consumes **$\sim 0.5\text{ Wh}$** of datacenter electricity (scaling from the verified *Epoch AI* / Google $0.24\text{–}0.34\text{ Wh}$ short-prompt baseline for larger multimodal context). Human-vs-AI time averages **$1.5\text{ min}$** of human reading and prompting vs. **$0.15\text{ min}$ ($9\text{ seconds}$)** of AI generation.
  * **Industry-Wide Share (Level 2):** Captures **62% of active Era 4 users**, **22% of global token and inference compute volume**, and **20% of total Era 4 AI spending** (anchored by tens of millions of $\$20/\text{month}$ `ChatGPT Plus`, `Claude Pro`, and `Copilot` subscriptions).

##### Step 2: Single-Call Reasoning Models (RLVR Test-Time Compute)

* **Name & Rank:** **Step 2 (Low-Middle Complexity) — Single-Call Reasoning Models (RLVR Test-Time Compute).**
* **Step Boundaries:**
  * **Difference vs. Step 1:** While Step 1 models begin streaming tokens immediately (~0.5 seconds time-to-first-token) and commit to their first intuitive path, Step 2 models trained via reinforcement learning with verifiable rewards (RLVR) spend **10 to 90 seconds generating 10,000 to 35,000 internal thinking tokens** (`<think>...</think>`) — testing hypotheses, spotting algebraic dead ends, and backtracking internally before outputting a verified answer, multiplying single-call token count by $5\times$ to $10\times$ and compute cost by $10\times$ to $25\times$.
  * **Upper Ceiling vs. Step 3:** In Era 4 (`2024-09` to `2025-01`), `o1-preview`, early `o1`, and `DeepSeek-R1` operated as isolated "brains in a box" inside a single chat turn or stateless API call — lacking live multi-file IDE diff editing, automated terminal execution, or enterprise database connectors, which required Step 3 (`Cursor Composer` / Hybrid RAG) or Step 4 (`LangGraph`).
* **Concrete Tool Stack:**
  * **Commercial & Open-Weight Reasoning Models:** OpenAI `o1-preview` and `o1-mini` (launched `2024-09-12`), full `OpenAI o1` (`o1-2024-12-17`) and `o1 pro mode` inside the $\$200/\text{month}$ `ChatGPT Pro` tier (`2024-12-05`), Alibaba's open-weight `QwQ-32B-Preview` (`2024-11`), Google's `Gemini 2.0 Flash Thinking Experimental` (`2024-12`), DeepSeek's open-weight `DeepSeek-R1` and `DeepSeek-R1-Zero` (`2025-01-20`, 671B total / 37B active MoE under MIT license, plus distilled `1.5B` to `70B` Qwen/Llama checkpoints), and OpenAI `o3-mini` (`2025-01-31`).
* **Use Cases & Context Switching:**
  * **Courses & Guides:** *DeepLearning.AI & OpenAI's* short course `Reasoning with o1` (taught by Colin Jarvis, late `2024`) and *OpenAI's Reasoning Best Practices Cookbook* taught engineers a major prompting reversal: stop writing verbose 2023-style chain-of-thought instructions and instead give Step 2 models concise, constraint-rich goal specifications so the internal RLVR policy can allocate its own thinking tokens.
  * **Surveys & Adoption Reports:** *OpenRouter* usage logs and *Epoch AI* benchmarks tracked reasoning models climbing from **0% of commercial tokens in August 2024 to ~16% of total Era 4 token volume by January 2025** (and passing 50% in Era 5), while *Sequoia Capital's* essay *"Generative AI's Act o1: The Reasoning Era Begins"* (`2024-10`) documented how trading inference compute for accuracy unlocked PhD-level STEM problem solving (matching **OpenAI AGI Level 2: Reasoners**).
  * **Famous Wins & Failures:** `OpenAI o1` jumped from `GPT-4o`'s 13.4% to **83.3% on the AIME math olympiad qualifier**, reached the **89th percentile on Codeforces competitive programming**, and beat PhD scientists on the **GPQA Diamond** physics/chemistry/biology benchmark (78.0% vs. 69.7% human experts). Then on January 20, 2025, Chinese lab DeepSeek released open-weight `DeepSeek-R1` (scoring **79.8% on AIME 2024** and **97.3% on MATH-500**) alongside a free mobile app that hit #1 on the US Apple App Store; the realization that pure RLVR (`Group Relative Policy Optimization / GRPO`) could reproduce `o1`-class reasoning at $27\times$ lower API pricing triggered a historic **$589B single-day drop in Nvidia's market capitalization on January 27, 2025**. On the failure side, developers discovered "overthinking traps" where `o1-preview` burned 30,000 billed output tokens ($1.80) and 60 seconds pondering a simple riddle or formatting request, or triggered false-positive safety warnings when users asked to inspect its hidden chain of thought.
  * **Same-Person Context Switching:** When our full-stack engineer hits a subtle distributed-lock race condition or needs to prove a custom pricing algorithm that `Claude 3.5 Sonnet` (Step 1/3) gets wrong three times in a row, the engineer copies the 300-line module and error log into **Step 2 (`OpenAI o1` or `DeepSeek-R1`)**, waits 55 seconds while the model explores edge cases in its thinking trace, and takes the verified mathematical fix back into Step 3 (`Cursor Composer`) to apply across the codebase.
* **Step Resource Use:**
  * **Single-Task Cost (Level 1):** One deep reasoning query processes **$\sim 15,000\text{ to }40,000\text{ tokens}$** ($2,500$ input tokens + $20,000$ internal thinking tokens + $2,500$ visible output tokens $\approx 2.5 \times 10^4\text{ tokens}$). Using $\text{FLOPs} \approx 2 \cdot N_{\text{active}} \cdot T_{\text{total}}$ across heavy reasoning checkpoints, one task executes **$\sim 4.0 \times 10^{16}\text{ FLOPs}$**, costs **$\$0.15\text{ to }\$0.80$** per query (specifically: $2.5\text{k} \times \$15/1\text{M} + 22.5\text{k} \times \$60/1\text{M} = \$1.39$ on flagship `o1` down to $\$0.11$ on `o1-mini` and $\$0.05$ on `DeepSeek-R1`), and uses **$\sim 5.0\text{ Wh}$** of electricity ($10\times$ a standard Step 1 chat turn due to sequential autoregressive decoding of 20k+ thinking tokens; Jegham et al. 2025). Human-vs-AI time averages **$3.0\text{ min}$** of human problem framing and proof verification vs. **$1.2\text{ min}$ ($40\text{–}90\text{ seconds}$)** of autonomous AI thinking time.
  * **Industry-Wide Share (Level 2):** Captures **12% of active Era 4 users** (concentrated among software engineers, quant researchers, scientists, and legal/financial analysts), **16% of global token and compute volume**, and **14% of total Era 4 AI spending**.

##### Step 3: Multi-File IDE AI Pairing & Enterprise Hybrid RAG

* **Name & Rank:** **Step 3 (Middle Production Workhorse) — Multi-File IDE AI Pairing & Enterprise Hybrid RAG.**
* **Step Boundaries:**
  * **Difference vs. Step 2:** Moves out of isolated single-turn browser prompts into deeply connected multi-file software workspaces and production corporate databases. Step 3 connects the model (`Claude 3.5 Sonnet`, `GPT-4o`) to an entire local code repository (`Cursor`, `Windsurf`) or millions of enterprise documents via hybrid search, rerankers, and 90% KV-cache prompt caching, raising single-task token volume $3\times$ to **40,000–100,000 tokens** across 3 to 10 interactive edit or retrieval turns.
  * **Upper Ceiling vs. Step 4:** Remains **human-driven and synchronous** (matching **Dan Shapiro Coding Level 2: The Junior Developer / Active Pairing** and **Karpathy Autonomy Slider Rung 3**): the developer or business user triggers each prompt, watches the streaming red/green diffs across 3 to 8 files, and clicks *"Accept"* or *"Reject"* after every step. It stops short of autonomous branching state graphs (`LangGraph`, Step 4) or unattended 30-minute container execution (`Devin`, Step 5).
* **Concrete Tool Stack:**
  * **AI-Native Code Editors (IDEs):** `Cursor` (`Cmd+K` inline edit and `Cmd+I` `Cursor Composer` multi-file agent powered by `Claude 3.5 Sonnet` and custom fast-apply diff models, indexed via `.cursorrules` and local codebase embeddings), `Codeium Windsurf` (`Cascade` deep codebase flow engine, launched `2024-11`), `GitHub Copilot Edits` (multi-file VS Code editing launched `2024-10`/`11`), `Zed AI`, and early `Cline` / `Aider` IDE extensions.
  * **Enterprise Hybrid RAG & Caching Stack:** Keyword search (`BM25` / `Elasticsearch`) fused with dense vector embeddings (`OpenAI text-embedding-3-large`, `Cohere Embed v3`, `Voyage AI`) inside `Pinecone`, `Qdrant`, `Weaviate`, `Milvus`, or `pgvector`, filtered by cross-encoder rerankers (`Cohere Rerank 3`, `BGE-Reranker`), parsed with vision-assisted PDF extractors (`LlamaParse`, `Unstructured`, `Docling`), and served with **Anthropic / DeepSeek 90% KV-Cache Prompt Caching** and **`OpenAI Structured Outputs`** (`Pydantic` / strict JSON schema).
* **Use Cases & Context Switching:**
  * **Courses & Guides:** *DeepLearning.AI's* `Multimodal RAG: Chat with Videos and PDFs` (`2024`), `Building and Evaluating Advanced RAG`, and the *Anthropic Cookbook* (`Prompt Caching with Claude 3.5 Sonnet` & `Contextual Retrieval`, `2024-09`, showing how prepending chunk context + BM25 + reranking + prompt caching cuts retrieval failure rates by 67%) defined the exact production blueprint for Step 3.
  * **Surveys & Adoption Reports:** *Menlo Ventures (2024)* reported that **Retrieval-Augmented Generation (RAG) climbed to 51% of all enterprise AI production deployments** (up from 31% in 2023), while code generation became the #1 departmental budget line. On *OpenRouter*, `Claude 3.5 Sonnet` captured **over 50% of all commercial programming token traffic** driven by `Cursor` and IDE harnesses, and *Stack Overflow 2024* recorded **62% active developer AI tool usage**.
  * **Famous Wins & Failures:** Throughout the second half of 2024, `Cursor` (built by Anysphere) achieved the fastest SaaS revenue ramp in developer-tool history — surging past $100M annualized recurring revenue (ARR) and overtaking `GitHub Copilot` among Y Combinator startups and indie hackers after `Claude 3.5 Sonnet` + `Cursor Composer` allowed a single developer to refactor a 6-file React/FastAPI feature in two minutes. In August 2024, Shopify, Notion, and Intercom reported cutting production RAG latency by 2x and API bills by 75%–90% overnight using Anthropic's prompt caching and `Contextual Retrieval`. On the cautionary side, "Chat-Oriented Programming" (coined by Steve Yegge in June 2024) produced a wave of "Cursor composer loops" where junior developers blindly clicked *"Accept All"* across 8 files without reading the diffs, accidentally overwriting authentication middleware or introducing circular imports until they rolled back via `git reset`.
  * **Same-Person Context Switching:** Armed with the UI mockup from Step 1 and the lock-free algorithm from Step 2, our engineer spends four hours of the workday inside **Step 3 (`Cursor Composer` running `Claude 3.5 Sonnet`)** — tagging `@schema.prisma`, `@api/routes.py`, and `@components/Dashboard.tsx`, reviewing the streaming multi-file diffs across 6turns, and wiring the backend into the company's Step 3 `Pinecone + Cohere Rerank 3` customer document search endpoint.
* **Step Resource Use:**
  * **Single-Task Cost (Level 1):** One multi-file feature implementation (5–8 `Composer` turns) or multi-hop enterprise hybrid RAG session processes **$\sim 40,000\text{ to }100,000\text{ tokens}$** (such as $60,000$ cached repository/document context tokens + $8,000$ new uncached input tokens + $3,000$ generated code/answer output tokens $\approx 7.1 \times 10^4\text{ tokens}$). Using the KV-cache adjusted compute formula ($\text{FLOPs} \approx 2 \cdot N_{\text{active}} \cdot [T_{\text{new}} + 0.1 \cdot T_{\text{cached}} + T_{\text{out}}]$ plus cross-encoder reranking and attention), one task executes **$\sim 8.0 \times 10^{16}\text{ FLOPs}$**, costs **$\$0.15\text{ to }\$0.50$** (on `Claude 3.5 Sonnet`: $60\text{k} \times \$0.30/1\text{M cached} + 8\text{k} \times \$3.00/1\text{M new} + 3\text{k} \times \$15.00/1\text{M out} = \$0.087$ per turn $\times$ 3–4 turns $\approx \$0.30$), and consumes **$\sim 6.0\text{ Wh}$** of electricity. Human-vs-AI time averages **$4.0\text{ min}$** of active human prompt steering and line-by-line diff inspection vs. **$0.8\text{ min}$ ($48\text{ seconds}$)** of AI generation and reranking.
  * **Industry-Wide Share (Level 2):** Captures **18% of active Era 4 users** (professional developers and enterprise knowledge workers), **34% of global token and compute volume** (the single largest token consumer in Era 4 due to 50k+ token codebase contexts sent on every edit), and **36% of total Era 4 AI spending**.

##### Step 4: Stateful Graph Workflows & Role-Based Multi-Agent Pipelines

* **Name & Rank:** **Step 4 (High Complexity / Production Multi-Step Orchestration) — Stateful Graph Workflows & Role-Based Multi-Agent Pipelines.**
* **Step Boundaries:**
  * **Difference vs. Step 3:** Crosses from human-triggered single-step calls into **automated multi-step state machines and multi-agent pipelines** (`8 to 25` chained LLM and tool calls per run). Instead of a human clicking *"Accept"* after every file edit or search query, a code-defined state graph (`LangGraph`) or role team (`CrewAI`, `AutoGen`) routes tasks across specialized prompts, invokes external REST/SQL APIs, checks outputs with an evaluator node, and loops back automatically on schema or test failures — jumping single-task token volume to **100,000–300,000 tokens**.
  * **Upper Ceiling vs. Step 5:** Follows **Anthropic's *Building Effective Agents* (`2024-12`) "Workflows" tier** and **LangChain Cognitive Architecture Level 5 (State Machine)**: the human engineer explicitly programs the allowed graph nodes, tool schemas, and maximum retry counters in Python/TypeScript. It avoids giving the model unconstrained root access to a cloud Linux container or live desktop mouse/keyboard GUI (`Devin` / `Computer Use`, Step 5).
* **Concrete Tool Stack:**
  * **State-Graph & Multi-Agent Frameworks:** `LangGraph` (`v0.1` / `v0.2` by LangChain, featuring cyclic graph nodes, typed state schemas, persistent checkpoint memory, and `LangGraph Studio`), `CrewAI` (role-based `Agent`, `Task`, and `Crew` sequential/hierarchical delegation), Microsoft `AutoGen` (`v0.2` / `v0.4` conversational multi-agent programming), `LlamaIndex Workflows` (event-driven async step orchestration, launched `2024-08`), `PydanticAI`, and early **Anthropic `Model Context Protocol (MCP)`** (open-sourced `2024-11-25` for connecting local data sources).
  * **Observability & Guardrail Harnesses:** `LangSmith`, `Braintrust`, `Arize Phoenix`, and `Weights & Biases Weave` for tracing multi-node token costs and running `LLM-as-a-Judge` evaluation suites.
* **Use Cases & Context Switching:**
  * **Courses & Guides:** This step was the centerpiece of 2024 practitioner education, led by Andrew Ng's *Four Agentic Design Patterns* (`Reflection`, `Tool Use`, `Planning`, `Multi-Agent Collaboration`, `2024-03`) and three flagship *DeepLearning.AI* courses: `AI Agents in LangGraph` (Harrison Chase & Rotem Weiss, `2024-06`), `Multi AI Agent Systems with crewAI` (João Moura, `2024-05`), and `AI Agentic Design Patterns with AutoGen` (Chi Wang & Qingyun Wu, `2024-04`), plus Anthropic's engineering guide *"Building Effective Agents"* (Erik Schluntz & Barry Zhang, `2024-12`).
  * **Surveys & Adoption Reports:** *Menlo Ventures (2024)* documented multi-step agentic workflows rising from <2% experimental scripts in 2023 to **12% of enterprise AI implementations in 2024**, while *LangChain's 2024 State of AI Agents Report* (1,300+ practitioners) found **51% running multi-step workflows in production** and **78% planning deployments**, citing performance quality and deterministic state control as their top engineering priority.
  * **Famous Wins & Failures:** Enterprise customer-support and back-office workflow platforms like `Sierra` (co-founded by Bret Taylor, reaching a $4.5B valuation in October 2024) and `Decagon` proved that Step 4 state graphs — routing a user request through an identity verifier node, a policy RAG node, an action tool node (processing a real refund or flight change), and a safety guardrail judge — could resolve 60%–80% of Tier-1 support tickets without hallucinations. Similarly, financial and legal teams deployed `LangGraph` and `CrewAI` pipelines where a `Researcher` agent pulled SEC 10-K filings, a `Quant` agent ran Python `pandas` ratios, and a `Critic` agent checked every citation before generating client memos. Conversely, teams that built naive 5-agent `CrewAI` or `AutoGen` chat rooms without explicit exit conditions suffered "polite agent ping-pong" — where two agents spent 40 turns thanking each other and burning $4.00 per run until engineers replaced free-form group chat with strict `LangGraph` state transitions.
  * **Same-Person Context Switching:** Once our engineer finishes coding the interactive feature in Step 3 (`Cursor`), the engineer needs to automate an enterprise customer-onboarding pipeline that extracts tables from uploaded vendor invoices, cross-checks tax IDs against an internal SQL database, flags anomalies for human Slack approval, and writes verified records to Salesforce; the engineer builds this as a **Step 4 `LangGraph` state machine** calling `gpt-4o-mini` for fast routing and `Claude 3.5 Sonnet` for complex extraction, monitored in `LangSmith`.
* **Step Resource Use:**
  * **Single-Task Cost (Level 1):** One end-to-end graph execution across 10 to 20 node transitions (router + retrieval + tool execution + reflection retry + synthesis) processes **$\sim 100,000\text{ to }300,000\text{ tokens}$** (midpoint $\sim 2.0 \times 10^5\text{ tokens}$ combining cached system/state prompts, tool JSON payloads, and multi-agent generations). Using the forward-pass compute equation across mixed frontier (`Sonnet`/`4o`) and fast (`4o-mini`/`Haiku`) nodes, one workflow run executes **$\sim 2.0 \times 10^{17}\text{ FLOPs}$**, costs **$\$0.50\text{ to }\$2.00$** per completed workflow run (midpoint $\sim \$1.10$), and consumes **$\sim 15.0\text{ Wh}$** of electricity. Human-vs-AI time shifts to **$5.0\text{ min}$** of human audit/approval at checkpoint gates vs. **$3.5\text{ min}$** of automated multi-node graph runtime.
  * **Industry-Wide Share (Level 2):** Captures **6% of active Era 4 users** (production AI engineers and enterprise automation teams), **18% of global token and compute volume**, and **18% of total Era 4 AI spending**.

##### Step 5: Early Cloud Sandbox & Screen-Acting Agents + Post-Training

* **Name & Rank:** **Step 5 (Highest Complexity / Frontier Autonomy & Custom Weight Adaptation) — Early Cloud Sandbox & Screen-Acting Agents + Post-Training.**
* **Step Boundaries:**
  * **Difference vs. Step 4:** Removes the pre-programmed workflow graph and gives the model **full environment autonomy inside an isolated operating system, web browser, and bash terminal sandbox** (`30 to 100+` dynamic action steps per task) OR updates the model's underlying neural weights via preference post-training and synthetic reasoning distillation. Single-task token volume jumps another $5\times$–$10\times$ to **500,000–2,000,000 tokens** ($10^{18}+$ FLOPs).
  * **Era 4 Top Ceiling (Why It Stopped Short of Era 5):** Represents the highest complexity achieved between June 2024 and January 2025 (**Anthropic Level 6 Autonomous Agents** / **OpenAI Level 3 Agents early preview**). Because Era 4 models (`Claude 3.5 Sonnet v2`, `GPT-4o`, early `o1`) still suffered from slow 15-second screenshot-action latency, context drift after 30 bash commands, and a 14.9%–22.0% OSWorld / 13.8%–49% SWE-bench Verified ceiling, Step 5 remained an expensive, heavily supervised frontier tier rather than the fast local terminal CLI (`Claude Code`) and parallel worktree fleets that emerged in Era 5.
* **Concrete Tool Stack:**
  * **Cloud Coding Sandboxes & SWE Harnesses:** `Cognition Devin` (launched in early access `2024-03` and general availability `2024-12` at **$\$500/\text{month}$**, providing an autonomous cloud Linux container, shell, code editor, and Chrome browser), Princeton's open-source `SWE-agent` (`Yang et al. 2024`, introducing Agent-Computer Interfaces / ACI for GitHub issue resolution), `OpenHands` (formerly `OpenDevin`), and `E2B` / `Modal` cloud code-execution sandboxes.
  * **Screen-Acting GUI Agents:** `Anthropic Computer Use` public beta (launched `2024-10-22` with upgraded `Claude 3.5 Sonnet`, translating desktop screenshots into pixel `[x, y]` mouse clicks, cursor drags, and keystrokes inside a Docker X11 virtual desktop).
  * **Post-Training & Distillation Stack:** Meta `Llama 3.1 405B / 70B / 8B` (`2024-07`) and `Qwen 2.5` open weights trained via Direct Preference Optimization (`DPO`), Kahneman-Tversky Optimization (`KTO`), or supervised fine-tuning (`SFT`) on synthetic reasoning traces distilled from `Llama-3.1-405B`, `o1`, or `DeepSeek-R1` using `HuggingFace TRL`, `Axolotl`, `Unsloth`, `TorchTune`, and `vLLM` on multi-node `Nvidia H100` clusters.
* **Use Cases & Context Switching:**
  * **Courses & Guides:** *DeepLearning.AI & Anthropic's* course `Building Toward Computer Use with Anthropic` (taught by Colt Steele, late `2024`), *HuggingFace's* `smolagents` `CodeAgent` tutorials (`2024-12`), and *Meta's Llama 3.1 Post-Training & Synthetic Data Cookbook* (`2024-07`) taught advanced ML teams how to sandbox autonomous OS agents and distill 405B/671B teacher traces into 8B production student models.
  * **Surveys & Adoption Reports:** *Menlo Ventures (2024)* found that custom fine-tuning and post-training consolidated into a specialized **9% of enterprise production workloads**, reserved for high-volume domain adaptation, strict latency budgets, or synthetic distillation, while open-ended autonomous sandbox agents accounted for the top **~2% of frontier engineering pilots**.
  * **Famous Wins & Failures:** On the win side, upgraded `Claude 3.5 Sonnet` (`2024-10`) pushed autonomous GitHub issue resolution on **SWE-bench Verified from <5% in 2023 to 49.0%**, and `Anthropic Computer Use` demonstrated the first general model capable of reading arbitrary spreadsheet cells, navigating legacy web forms, and debugging apps via visual screenshots (**22.0% on OSWorld**, nearly tripling the 7.8% prior record). On the failure side, `Cognition Devin` became the defining cautionary tale of Era 4 autonomy hype: after its March 2024 viral demo video claimed to complete real Upwork freelance jobs autonomously (later critiqued by independent developers for cherry-picking and fixing bugs Devin itself created), research lab **Answer.AI** ran a rigorous month-long production evaluation on the $\$500/\text{month}$ December 2024 release across **20 real-world engineering tasks** (`2025-01`, *"Thoughts On A Month With Devin"*) — finding that Devin **succeeded on only 3 of 20 tasks (15%)**, got stuck in multi-hour dead-end refactoring loops on 14 tasks, and fabricated unrequested architecture changes whenever task requirements were slightly ambiguous.
  * **Same-Person Context Switching:** At the end of the day, our engineer has three background chores — migrating 40 legacy unit test files from Jest to Vitest, filling out a repetitive 50-row vendor compliance web portal that has zero API, and training a low-latency 8B classifier on 50,000 logged customer-support traces. The engineer delegates the unit-test migration to **Step 5 (`Devin` / `OpenHands` cloud sandbox)** via Slack, runs a **Step 5 `Claude Computer Use` Docker container** to click through the legacy web portal, and launches an overnight `Unsloth` + `TRL` DPO post-training job on `Llama-3.1-8B` — then spends 10 minutes the next morning rescuing and merging the sandbox PRs.
* **Step Resource Use:**
  * **Single-Task Cost (Level 1):** One autonomous cloud sandbox ticket or 50-step `Computer Use` screenshot-action session processes **$\sim 500,000\text{ to }2,000,000\text{ tokens}$** (midpoint $\sim 1.2 \times 10^6\text{ tokens}$, driven by 50–100 high-resolution desktop screenshots at $\sim 1,500$ tokens each plus accumulated bash/file history and 25,000 output/action tokens). Using the forward-pass compute equation, one autonomous agent task executes **$\sim 1.5 \times 10^{18}\text{ FLOPs}$** (while a custom `Llama-3.1` DPO post-training run executes $\sim 10^{19}\text{ to }10^{20}\text{ FLOPs}$), costs **$\$3.00\text{ to }\$15.00$** in API/compute per autonomous task (or $\$50\text{ to }\$500$ per cloud GPU post-training job), and consumes **$\sim 45.0\text{ Wh}$** of electricity (equivalent to running a laptop for nearly an hour). Human-vs-AI time inverts to **$10.0\text{ min}$** of human ticket scoping and PR rescue vs. **$20.0\text{ min}$ ($10\text{–}45\text{ min}$)** of unattended cloud sandbox or GUI execution.
  * **Industry-Wide Share (Level 2):** Captures **2% of active Era 4 users** (frontier AI labs and advanced platform teams), **10% of global token and compute volume** (since one Step 5 task consumes $200\times$ the tokens of a Step 1 chat turn), and **12% of total Era 4 AI spending**.

***

#### 3.4.4 Era 4 Full-Ladder Resource Totals

**Era 4 Resource Summary:** Across the 8-month window from `2024-06` to `2025-01`, global generative AI usage scaled to roughly **450 million to 500 million monthly active users** generating **$\sim 3.5 \times 10^{14}$ tokens ($350\text{ trillion}$ tokens)** and consuming **$\sim 9.0 \times 10^{25}\text{ FLOPs}$** of combined inference and frontier training compute, **$\sim 3.8\text{ TWh}$ ($3.8 \times 10^6\text{ MWh}$)** of datacenter electricity, and **$\sim \$18.5\text{B}$** in direct API, enterprise application, and consumer subscription spending.

* **Compute & Energy Totals (`2024-06` to `2025-01`):**
  * **Total Compute ($\sim 9.0 \times 10^{25}\text{ FLOPs}$):** Combines **$\sim 5.0 \times 10^{25}\text{ FLOPs}$ of global inference compute** across 350 trillion commercial and consumer tokens (weighted across Step 1–5 active parameter scales and KV-cache prefill) with **$\sim 4.0 \times 10^{25}\text{ FLOPs}$ of frontier pre-training and RLVR post-training runs** executed during the 8-month window (anchored by `Llama 3.1 405B` at $3.8 \times 10^{25}\text{ FLOPs}$, `DeepSeek-V3/R1` at $3.3 \times 10^{24}\text{ FLOPs}$, plus proprietary `OpenAI o1`/`GPT-4.5` and `Anthropic Claude 3.5` training runs tracked by *Epoch AI*).
  * **Total Electricity ($\sim 3,800,000\text{ MWh}$ / $3.8\text{ TWh}$):** Derived from $\sim 2.1\text{ TWh}$ of global LLM/multimodal inference electricity (350T tokens at a blended H100/TPUv5p cluster efficiency of $\sim 6\text{ Wh}$ per $10^4$ active/cached tokens including PUE $\approx 1.15$) plus $\sim 1.7\text{ TWh}$ dedicated to frontier model training and continuous synthetic data generation clusters across US, European, and Asian AI datacenters.
* **Spending & Token Volume Totals (`2024-06` to `2025-01`):**
  * **Total Spending ($\sim \$18.5\text{B USD}$ over 8 months):** Combines the 8-month run-rate of *Menlo Ventures' 2024 Enterprise GenAI Spend* (**$\$13.8\text{B/year}$** $\to \sim \$10.5\text{B}$ during the ramped H2 2024–Jan 2025 period across foundation model APIs, coding IDEs like `Cursor`/`Copilot`, and enterprise RAG/agent deployments) with **$\sim \$8.0\text{B}$ in consumer and prosumer subscriptions** (`ChatGPT Plus` at $\$20/\text{mo}$, `ChatGPT Pro` at $\$200/\text{mo}$, `Claude Pro`, `Perplexity Pro`, and `Google One AI Premium`).
  * **Global Token Volume ($\sim 3.5 \times 10^{14}\text{ tokens}$ / $350\text{T tokens}$):** Averages $\sim 1.45\text{ trillion tokens per day}$ across all global providers (consistent with OpenAI's disclosed $100\text{B+}\text{ words/day}$ in early 2024 scaling $4\times$ by late 2024 alongside Anthropic, Google Gemini, DeepSeek, and OpenRouter's multi-trillion monthly logs). While Step 1 accounted for 62% of users, **Steps 2–5 accounted for 78% of all tokens** due to 20k-token reasoning traces (`o1`/`R1`) and 70k-token cached IDE contexts (`Cursor`).
* **Human Usage Totals (`2024-06` to `2025-01`):**
  * **Active Users ($\sim 480\text{ million}$ monthly active users):** Anchored by `ChatGPT` crossing 200M–350M weekly active users between August 2024 and January 2025, plus `Gemini`, `Claude`, `Perplexity`, `NotebookLM`, `DeepSeek` (which added 30M+ users in January 2025 alone), and 15M+ developers using `GitHub Copilot` and `Cursor`.
  * **Human-Hours ($\sim 4.2 \times 10^9\text{ human-hours}$):** Across 245 days, ~480M active users averaged $\sim 35\text{ hours}$ of cumulative interactive prompting, document study, side-by-side `Cursor` code review, and `LangGraph` workflow supervision ($\sim 8.5\text{ minutes/day}$ for casual Step 1 consumers vs. $1.5\text{–}3.0\text{ hours/day}$ for Step 3–4 software engineers).

| Step Rank & Name ($L_4$: `2024-06` to `2025-01`) | Evolution Link from Era 3 ($L_3$) | Representative Tool Stack | Tokens / Task (Order of Mag.) | Compute / Task (FLOPs) | Energy & Cost / Task (Wh & USD) | Human vs. AI Time / Task | Active User Share | Token & Compute Share | Spend Share |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Step 1:** Multimodal Web Chat, Built-In File/Web Search & Previews | **Old Steps Sinking into Default UI** ($L_3$ Step 1 chat + Step 2 personas + Step 3 single-PDF RAG) | `GPT-4o`, `Claude 3.5 Sonnet` Artifacts & Projects, `NotebookLM`, `Perplexity`, `Gemini 1.5 Pro` | $3\text{k}–8\text{k}$ ($\sim 5.5 \times 10^3$) | $3.0 \times 10^{15}$ | $0.5\text{ Wh}$ / $\$0.01–\$0.03$ | $1.5\text{ min}$ human / $0.15\text{ min}$ AI | **62%** | **22%** | **20%** |
| **Step 2:** Single-Call Reasoning Models (RLVR Test-Time Compute) | **New Step** (unlocked by internal RLVR chain-of-thought scaling) | `OpenAI o1-preview`, `o1`, `o1-mini`, `DeepSeek-R1`, `QwQ-32B`, `o3-mini` | $15\text{k}–40\text{k}$ ($\sim 2.5 \times 10^4$) | $4.0 \times 10^{16}$ | $5.0\text{ Wh}$ / $\$0.15–\$0.80$ | $3.0\text{ min}$ human / $1.2\text{ min}$ AI | **12%** | **16%** | **14%** |
| **Step 3:** Multi-File IDE AI Pairing & Enterprise Hybrid RAG | **Split & Evolved Step** (from $L_3$ Step 1/2 coding & $L_3$ Step 3 vector RAG) | `Cursor Composer`, `Windsurf Cascade`, `Copilot Edits`, `Cohere Rerank 3` + 90% KV-cache | $40\text{k}–100\text{k}$ ($\sim 7.0 \times 10^4$) | $8.0 \times 10^{16}$ | $6.0\text{ Wh}$ / $\$0.15–\$0.50$ | $4.0\text{ min}$ human / $0.8\text{ min}$ AI | **18%** | **34%** | **36%** |
| **Step 4:** Stateful Graph Workflows & Role-Based Multi-Agent Pipelines | **Evolved Replacement Step** (taming $L_3$ Step 5 `AutoGPT` loops with state graphs) | `LangGraph`, `CrewAI`, `AutoGen`, `LlamaIndex Workflows`, `LangSmith` | $100\text{k}–300\text{k}$ ($\sim 2.0 \times 10^5$) | $2.0 \times 10^{17}$ | $15.0\text{ Wh}$ / $\$0.50–\$2.00$ | $5.0\text{ min}$ human / $3.5\text{ min}$ AI | **6%** | **18%** | **18%** |
| **Step 5:** Early Cloud Sandbox & Screen-Acting Agents + Post-Training | **New Top Step & Consolidated Fine-Tuning** ($L_3$ Step 4 `LoRA` + OS sandboxes) | `Cognition Devin` ($500/mo), `Anthropic Computer Use`, `SWE-agent`, `Llama-3.1` DPO | $500\text{k}–2\text{M}$ ($\sim 1.2 \times 10^6$) | $1.5 \times 10^{18}$ | $45.0\text{ Wh}$ / $\$3.00–\$15.00$ | $10.0\text{ min}$ human / $20.0\text{ min}$ AI | **2%** | **10%** | **12%** |
| **Era 4 Full-Ladder Totals (`2024-06` to `2025-01`, 8 Months)** | **4 Structural Shifts** (RAG sinks to UI; RLVR, Multi-File IDE, Graphs & Sandboxes rise) | **Full Era 4 Ecosystem** (`Sonnet 3.5`, `GPT-4o`, `o1`, `DeepSeek-R1`, `Cursor`, `LangGraph`) | **$\sim 3.5 \times 10^{14}$ Total Tokens** | **$\sim 9.0 \times 10^{25}$ Total FLOPs** | **$\sim 3.8 \times 10^6\text{ MWh}$ / $\sim \$18.5\text{B}$** | **$\sim 4.2 \times 10^9$ Human-Hours** | **100%** ($\sim 480\text{M}$ Users) | **100%** ($350\text{T}$ Tokens) | **100%** ($\$18.5\text{B}$ Spend) |

***

#### 3.4.5 Structured Era 4 Data Handoff (JSON)

**Machine-Readable Step Metrics:** Supplies the verified single-task, industry-wide, and cross-era transition numbers for Stage 4 visual plotting.

```json
{
  "era_id": "L4",
  "era_name": "Built-In Multimodal Context, Multi-File IDE Pairing & First Reasoning Models Ladder",
  "era_nickname": "The Sonnet 3.5, Cursor & o1 Era",
  "start_date": "2024-06",
  "end_date": "2025-01",
  "duration_months": 8,
  "era_totals": {
    "total_tokens": 3.5e14,
    "total_compute_flops": 9.0e25,
    "inference_compute_flops": 5.0e25,
    "training_compute_flops": 4.0e25,
    "total_electricity_mwh": 3800000,
    "total_spending_usd": 18500000000,
    "enterprise_spending_annualized_usd": 13800000000,
    "active_users_millions": 480,
    "total_human_hours": 4.2e9
  },
  "steps": [
    {
      "step_rank": 1,
      "step_name": "Multimodal Web Chat with Built-In File Upload, Search & Live Previews",
      "evolution_category": "Old Step Sinking into Default UI",
      "prior_era_links": ["L3_Step_1", "L3_Step_2", "L3_Step_3"],
      "tool_stack": [
        "ChatGPT (GPT-4o / gpt-4o-mini)",
        "Claude 3.5 Sonnet (Artifacts & Projects)",
        "Google NotebookLM (Audio Overviews)",
        "Perplexity Pro",
        "Gemini 1.5 Pro (2M context) & Flash",
        "GitHub Copilot / Cursor Tab"
      ],
      "single_task_metrics": {
        "tokens_min": 3000,
        "tokens_max": 8000,
        "tokens_midpoint": 5500,
        "compute_flops": 3.0e15,
        "energy_wh": 0.5,
        "cost_usd_min": 0.01,
        "cost_usd_max": 0.03,
        "cost_usd_midpoint": 0.02,
        "human_time_minutes": 1.5,
        "ai_runtime_minutes": 0.15
      },
      "industry_wide_shares": {
        "user_share_pct": 62.0,
        "token_compute_share_pct": 22.0,
        "spending_share_pct": 20.0
      }
    },
    {
      "step_rank": 2,
      "step_name": "Single-Call Reasoning Models (RLVR Test-Time Compute)",
      "evolution_category": "New Step",
      "prior_era_links": ["L3_Step_2"],
      "tool_stack": [
        "OpenAI o1-preview & o1",
        "OpenAI o1-mini & o3-mini",
        "ChatGPT Pro ($200/mo o1 pro mode)",
        "DeepSeek-R1 & DeepSeek-R1-Zero",
        "QwQ-32B-Preview",
        "Gemini 2.0 Flash Thinking"
      ],
      "single_task_metrics": {
        "tokens_min": 15000,
        "tokens_max": 40000,
        "tokens_midpoint": 25000,
        "compute_flops": 4.0e16,
        "energy_wh": 5.0,
        "cost_usd_min": 0.15,
        "cost_usd_max": 0.80,
        "cost_usd_midpoint": 0.45,
        "human_time_minutes": 3.0,
        "ai_runtime_minutes": 1.2
      },
      "industry_wide_shares": {
        "user_share_pct": 12.0,
        "token_compute_share_pct": 16.0,
        "spending_share_pct": 14.0
      }
    },
    {
      "step_rank": 3,
      "step_name": "Multi-File IDE AI Pairing & Enterprise Hybrid RAG",
      "evolution_category": "Split & Evolved Step",
      "prior_era_links": ["L3_Step_1", "L3_Step_2", "L3_Step_3"],
      "tool_stack": [
        "Cursor Composer (Cmd+I)",
        "Codeium Windsurf (Cascade)",
        "GitHub Copilot Edits",
        "Claude 3.5 Sonnet (90% KV-Cache Prompt Caching)",
        "Pinecone / Qdrant / Weaviate + BM25 Hybrid",
        "Cohere Rerank 3 & OpenAI Structured Outputs"
      ],
      "single_task_metrics": {
        "tokens_min": 40000,
        "tokens_max": 100000,
        "tokens_midpoint": 70000,
        "compute_flops": 8.0e16,
        "energy_wh": 6.0,
        "cost_usd_min": 0.15,
        "cost_usd_max": 0.50,
        "cost_usd_midpoint": 0.30,
        "human_time_minutes": 4.0,
        "ai_runtime_minutes": 0.8
      },
      "industry_wide_shares": {
        "user_share_pct": 18.0,
        "token_compute_share_pct": 34.0,
        "spending_share_pct": 36.0
      }
    },
    {
      "step_rank": 4,
      "step_name": "Stateful Graph Workflows & Role-Based Multi-Agent Pipelines",
      "evolution_category": "Evolved Replacement Step",
      "prior_era_links": ["L3_Step_3", "L3_Step_5"],
      "tool_stack": [
        "LangGraph & LangGraph Studio",
        "CrewAI",
        "Microsoft AutoGen",
        "LlamaIndex Workflows",
        "Anthropic Prompt Chaining / Routing / Orchestrator-Workers",
        "LangSmith & Braintrust Evals"
      ],
      "single_task_metrics": {
        "tokens_min": 100000,
        "tokens_max": 300000,
        "tokens_midpoint": 200000,
        "compute_flops": 2.0e17,
        "energy_wh": 15.0,
        "cost_usd_min": 0.50,
        "cost_usd_max": 2.00,
        "cost_usd_midpoint": 1.10,
        "human_time_minutes": 5.0,
        "ai_runtime_minutes": 3.5
      },
      "industry_wide_shares": {
        "user_share_pct": 6.0,
        "token_compute_share_pct": 18.0,
        "spending_share_pct": 18.0
      }
    },
    {
      "step_rank": 5,
      "step_name": "Early Cloud Sandbox & Screen-Acting Agents + Post-Training",
      "evolution_category": "New Top Step & Consolidated Fine-Tuning",
      "prior_era_links": ["L3_Step_4", "L3_Step_5"],
      "tool_stack": [
        "Cognition Devin ($500/mo Cloud Sandbox)",
        "Anthropic Computer Use (Claude 3.5 Sonnet GUI Beta)",
        "SWE-agent & OpenHands (OpenDevin)",
        "E2B / Modal Code Sandboxes",
        "Llama 3.1 405B/70B/8B DPO & Synthetic Distillation",
        "HuggingFace TRL, Axolotl & Unsloth"
      ],
      "single_task_metrics": {
        "tokens_min": 500000,
        "tokens_max": 2000000,
        "tokens_midpoint": 1200000,
        "compute_flops": 1.5e18,
        "energy_wh": 45.0,
        "cost_usd_min": 3.00,
        "cost_usd_max": 15.00,
        "cost_usd_midpoint": 8.00,
        "human_time_minutes": 10.0,
        "ai_runtime_minutes": 20.0
      },
      "industry_wide_shares": {
        "user_share_pct": 2.0,
        "token_compute_share_pct": 10.0,
        "spending_share_pct": 12.0
      }
    }
  ]
}
```