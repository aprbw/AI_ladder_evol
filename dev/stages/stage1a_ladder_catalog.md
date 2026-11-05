# Catalog of Published & Informal AI, LLM & Agentic Ladders (2017–2026)

**Complete Ladder Survey:** Catalogs 18 foundational AI, large language model (LLM), and action-taking AI (agentic AI) ladders published between `2017-11` and `2026-01` across research labs, venture capital firms, software companies, and engineering communities, documenting exact publication dates (`YYYY-MM`), authors, web sources, ordering axes, and step-by-step definitions.

### Structural Index
1. Academic & AI Lab Ladders
   1. Karpathy Software Eras & Autonomy Slider (`2017-11` to `2025-06`)
   2. Google DeepMind Levels of AGI Matrix (`2023-11`)
   3. OpenAI Five Levels of AGI & Optimization Matrix (`2023-11` to `2025-01`)
   4. Anthropic Building Effective Agents Hierarchy (`2024-12`)
   5. Academic Language Agent Architectures (`2023-06` to `2024-03`)
2. Industry, Enterprise & Autonomy Ladders
   1. Self-Driving Style AI Coding Ladders (`2021-06` to `2026-01`)
   2. LangChain & Hugging Face Cognitive Architectures (`2023-11` to `2025-01`)
   3. Venture Capital Market & Stack Ladders (`2022-09` to `2026-01`)
   4. Gartner Enterprise AI Maturity Model (`2020-01` to `2025-06`)
3. Developer & Practitioner Informal Ladders
   1. Practitioner LLM Intervention Hierarchy (`2023-04` to `2025-01`)
   2. Eugene Yan Seven Production LLM Patterns (`2023-07`)
   3. Pre-LLM & Early Transformer NLP Ladders (`2017-06` to `2021-07`)
4. Cross-Ladder Synthesis for Stage 2 Schema Lock

***

## 1. Academic & AI Lab Ladders

**Lab Frameworks Summary:** Leading AI research labs classify AI progress along two distinct axes — broad human-skill replacement benchmarks from Google DeepMind and OpenAI, and practical code-control hierarchies from Andrej Karpathy, Anthropic, and academic agent researchers.

### 1.1 Karpathy Software Eras & Autonomy Slider (`2017-11` to `2025-06`)

**Three Software Eras:** Andrej Karpathy maps the history of computer programming across three shifts in how humans instruct machines, paired with a continuous dial controlling how much independence the AI gets (autonomy slider).

* **Authors & Sources:** Andrej Karpathy (Founding Member of OpenAI, Former Director of AI at Tesla); published in *"Software 2.0"* on Medium (`2017-11`, `karpathy.medium.com/software-2-0-a64152b37c35`) and expanded in *"Software in the Era of AI / Software Is Changing (Again)"* at Y Combinator AI Startup School (`2025-06`, `youtube.com/watch?v=LCEmiRjPEtQ`).
* **Ordering Axis:** Programming abstraction level (from explicit human-written rules to learned math weights to natural English prompts) paired with human-in-the-loop verification speed along an autonomy slider.
* **Step 1 — Software 1.0 (`Pre-2017` Baseline):** Engineers write explicit step-by-step logic in traditional programming languages like Python, C++, and Java where every behavior is hand-coded line by line.
* **Step 2 — Software 2.0 (`2017-11` Shift):** Engineers curate training datasets and define a goal score (objective function), letting math optimization (gradient descent backpropagation) compile data directly into neural network numbers (model weights) across image recognition, voice translation, and Tesla Autopilot vision.
* **Step 3 — Software 3.0 (`2025-06` Shift):** Engineers program computers in plain English where natural language prompts act as the code, large language models act as the central processor (CPU), and the amount of text the model holds in active memory (context window) acts as working memory (RAM).
* **Autonomy Slider Tiers:** Inspired by Tesla Autopilot Levels 1 to 5, Karpathy pairs Software 3.0 with a product design slider where successful apps act as human-amplifying "Iron Man suits" with fast visual diff checks:
  * **Slider Rung 1 — Manual Tab Completion:** Developer writes code while the model predicts the next few lines inline (GitHub Copilot tab autocomplete).
  * **Slider Rung 2 — Scoped File Edits:** Developer highlights a code block or single file and instructs the model to modify it (`Cmd+K` in Cursor).
  * **Slider Rung 3 — Multi-File Repo Changes:** Developer prompts an editor agent to edit multiple files across a project (`Cmd+I` Composer in Cursor) and audits the red/green change highlights (code diffs).
  * **Slider Rung 4 — Independent Agent Loops:** Model runs background tasks across codebases, terminals, and browsers with periodic human review checkpoints.

### 1.2 Google DeepMind Levels of AGI Matrix (`2023-11`)

**Skill-by-Autonomy Grid:** Google DeepMind separates raw model skill percentile from task breadth and human-interaction independence in a two-part grading grid.

* **Authors & Sources:** Meredith Ringel Morris, Jascha Sohl-Dickstein, Noah Fiedel, Tris Warkentin, Allan Dafoe, Aleksandra Faust, Clement Farabet, and Shane Legg (Google DeepMind); published in *"Levels of AGI for Operationalizing Progress on the Path to AGI"* (`2023-11`, updated `2024-06` for ICML 2024, `arxiv.org/abs/2311.02462`).
* **Ordering Axis:** Two-dimensional capability matrix comparing human skill percentile (Depth: Levels 0–5) against task scope (Breadth: Narrow vs. General), paired with a six-level independence scale (Autonomy Levels 0–5).
* **Performance Tier 0 — No AI:** Humans perform 100% of the task using standard non-AI software tools (calculators, compilers, spreadsheets).
* **Performance Tier 1 — Emerging:** AI matches or slightly beats an unskilled human adult (~1st–20th percentile); Narrow examples include simple rule-based systems, while General examples include 2023 chat models (`ChatGPT`, `Bard`, `Llama 2`).
* **Performance Tier 2 — Competent:** AI reaches at least the 50th percentile of skilled adults; Narrow examples include voice assistants (`Siri`) and coding/writing tasks in `GPT-4`, while General Competent AGI remains unachieved as of 2023.
* **Performance Tier 3 — Expert:** AI reaches at least the 90th percentile of skilled adults; Narrow examples include grammar checkers (`Grammarly`) and image generators (`DALL-E 2`, `Midjourney`), while General Expert AGI remains unachieved.
* **Performance Tier 4 — Virtuoso / Exceptional:** AI reaches at least the 99th percentile of skilled adults; Narrow examples include championship game engines (`DeepBlue`, `AlphaZero`), while General Virtuoso AGI remains unachieved.
* **Performance Tier 5 — Superhuman:** AI beats 100% of all humans across tasks; Narrow examples include 3D protein folding prediction (`AlphaFold`) and superhuman board-game play (`AlphaGo`), while General Superhuman AI (Artificial Superintelligence / ASI) remains theoretical.
* **DeepMind Autonomy Levels (0–5):** Separate scale measuring how humans delegate work to the model:
  * **Autonomy Level 0 — No AI:** Human executes every step manually.
  * **Autonomy Level 1 — AI as Tool:** Human fully controls the task and invokes AI for immediate single-step commands (search query, spellcheck).
  * **Autonomy Level 2 — AI as Consultant:** Human drives the workflow but asks the AI for advice, summaries, or draft options when requested.
  * **Autonomy Level 3 — AI as Collaborator:** Human and AI share equal back-and-forth initiative, co-editing documents or pair-programming interactively.
  * **Autonomy Level 4 — AI as Expert:** AI drives task execution independently while human provides high-level feedback and handles rare edge cases.
  * **Autonomy Level 5 — AI as Agent:** AI operates with full autonomy, creating sub-goals, calling external software, and finishing end-to-end tasks without human intervention.

### 1.3 OpenAI Five Levels of AGI & Optimization Matrix (`2023-11` to `2025-01`)

**Five Capability Rungs:** OpenAI tracks its internal product roadmap across five ascending tiers of problem-solving depth and multi-day independence, supplemented by developer guides for customizing models and building agents.

* **Authors & Sources:** OpenAI Leadership (Sam Altman, Mira Murati, Bob McGrew), reported by Rachel Metz at Bloomberg in *"OpenAI Scale Ranks Progress Toward 'Human-Level' Problem Solving"* (`2024-07`, July 11, 2024, `bloomberg.com`); paired with Colin Jarvis and John Allard's OpenAI DevDay breakout *"A Survey of Techniques for Maximizing LLM Performance"* (`2023-11`, `youtube.com/watch?v=ahnGLM-RC1Y`) and OpenAI's *"A Practical Guide to Building Agents"* (`2025-01`, `cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf`).
* **Ordering Axis:** Autonomous problem-solving duration and cognitive scope (from single-turn conversation to internal reasoning, multi-step tool action, scientific discovery, and full corporate operation).
* **Level 1 — Chatbots (`2022-11` Baseline):** AI interacts in fluent conversational language to answer questions, summarize text, and draft short content (`ChatGPT`, `GPT-3.5`, base `GPT-4`).
* **Level 2 — Reasoners (`2024-09` Rollout):** AI solves complex logic, math, and coding problems at the level of a human with a doctorate (PhD-level problem solving) by training models to think step by step before answering (reinforcement learning with verifiable rewards / RLVR test-time compute in `OpenAI o1` and `o3`).
* **Level 3 — Agents (`2025-01` Frontier):** AI systems take multi-step actions across web browsers, terminals, and software APIs over hours or days on a user's behalf (`OpenAI Operator`, `Deep Research`, `Codex CLI`).
* **Level 4 — Innovators (Speculative Tier):** AI systems generate original scientific hypotheses, invent novel engineering designs, and make creative breakthroughs beyond existing human knowledge.
* **Level 5 — Organizations (Speculative Tier):** AI systems coordinate strategy, execution, and operations across an entire company to perform the full work of a human organization.
* **OpenAI DevDay Optimization Ladder (`2023-11`):** Orders developer customization along two perpendicular needs — adding external facts (Context Optimization) vs. changing model habits (LLM Behavior Optimization):
  * **Rung 1 — Prompt Engineering:** Write clear instructions, split complex tasks into smaller steps, and give the model time to think (`Chain-of-Thought`).
  * **Rung 2 — Retrieval-Augmented Generation (RAG):** Connect the model to private search indexes to supply missing facts at question time.
  * **Rung 3 — Function Calling / Tool Use:** Connect the model to live software interfaces (APIs) and structured data schemas (`JSON Mode`).
  * **Rung 4 — Fine-Tuning:** Train model weights on thousands of examples to lock in consistent tone, formatting, or compact model speed (`GPT-3.5-Turbo` fine-tuning).

### 1.4 Anthropic Building Effective Agents Hierarchy (`2024-12`)

**Workflows Before Agents:** Anthropic orders multi-step AI architectures from a single augmented model call through five predictable code-driven workflows up to open-ended autonomous agents.

* **Authors & Sources:** Erik Schluntz and Barry Zhang (Anthropic Applied AI); published in *"Building Effective Agents"* (`2024-12`, December 19, 2024, `anthropic.com/research/building-effective-agents`).
* **Ordering Axis:** Runtime control and execution predictability — moving from developer-coded step sequences (Workflows) to model-directed dynamic loops (Agents), with increasing token cost and latency at each step.
* **Step 0 — Single Augmented LLM:** Base model call enhanced with document lookup (retrieval), external software plugs (tools via Model Context Protocol / MCP), and short/long-term scratchpads (memory).
* **Step 1 — Prompt Chaining Workflow:** Fixed code pipeline that splits a task into sequential model calls where each step checks or transforms the previous output (such as generating marketing copy in English, verifying tone in code, then translating into five languages).
* **Step 2 — Routing Workflow:** Classifier call that inspects an incoming request and sends it to a specialized downstream prompt, toolset, or model tier (such as sending easy questions to `Claude 3.5 Haiku` and hard coding bugs to `Claude 3.5 Sonnet`).
* **Step 3 — Parallelization Workflow:** Code harness running multiple model calls at the same time via two patterns — **Sectioning** (splitting a task into independent parallel parts like checking code vs. checking safety guardrails) or **Voting** (running the same check multiple times to reach majority consensus).
* **Step 4 — Orchestrator-Workers Workflow:** Central planner model (Orchestrator) that dynamically breaks an unpredictable task (such as editing an unknown number of files in a software repository) into sub-tasks, delegates them to parallel worker models, and merges their results.
* **Step 5 — Evaluator-Optimizer Workflow:** Two-model feedback loop where one model generates a draft and a second judge model critiques it against rubrics until quality passes (analogous to iterative human writing or search refinement).
* **Step 6 — Autonomous Agents:** Open-ended loop where an LLM independently plans steps, executes tools or computer clicks (`Claude Computer Use`), reads environment feedback (compiler errors, terminal logs), and iterates over dozens of turns until task completion or a stopping guardrail.

### 1.5 Academic Language Agent Architectures (`2023-06` to `2024-03`)

**Agent Component Taxonomies:** Academic researchers at OpenAI, Princeton, and Stanford formalized how language models evolve into autonomous agents by adding reasoning loops, memory stores, and multi-agent teamwork.

* **Lilian Weng's Autonomous Agent Triad (`2023-06`):** Published by Lilian Weng (OpenAI) in *"LLM Powered Autonomous Agents"* (`2023-06`, June 23, 2023, `lilianweng.github.io/posts/2023-06-23-agent/`), defining an agent as **LLM + Planning + Memory + Tool Use**:
  * **Component 1 — Planning:** Subgoal decomposition (`Chain of Thought`, `Tree of Thoughts`) plus self-reflection (`ReAct`, `Reflexion`).
  * **Component 2 — Memory:** Sensory input embeddings, short-term working memory (in-context window), and long-term external vector memory (fast approximate nearest-neighbor search / MIPS via `FAISS`, `HNSW`).
  * **Component 3 — Tool Use:** External API execution (`MRKL`, `Toolformer`, `HuggingGPT`, `ChatGPT Plugins`).
* **CoALA Cognitive Architecture Framework (`2023-09`):** Published by Theodore R. Sumers, Shunyu Yao, Karthik Narasimhan, and Thomas L. Griffiths (Princeton University) in *"Cognitive Architectures for Language Agents (CoALA)"* (`2023-09`, `arxiv.org/abs/2309.02427`), ordering language systems along three progressive tiers:
  * **Tier 1 — Text-Only Prompted LLM:** Stateless input-to-output text transformation with zero external memory or environment action.
  * **Tier 2 — Action-Taking Language Agent (`ReAct`):** Model alternates between internal reasoning traces (Thought) and external tool actions (Act) plus environment readouts (Observation), originally introduced by Shunyu Yao et al. in *"ReAct: Synergizing Reasoning and Acting in Language Models"* (`2022-10`, `arxiv.org/abs/2210.03629`).
  * **Tier 3 — Full Cognitive Language Agent (`CoALA`):** Structured agent combining working memory, long-term episodic/semantic/procedural memory, internal cognitive actions (retrieval, reasoning, learning), and external grounding actions in a continuous decision loop (`Voyager`, `Generative Agents`).
* **Andrew Ng's Four Agentic Design Patterns (`2024-03`):** Presented by Andrew Ng (DeepLearning.AI / Stanford) at Sequoia Capital's AI Ascent (`2024-03`, March 26, 2024, `deeplearning.ai/the-batch`), ordering agent capabilities by rising reliability and autonomy:
  * **Pattern 1 — Reflection:** Prompting a model to critique and rewrite its own code or text output in a self-check loop.
  * **Pattern 2 — Tool Use:** Giving the model access to web search, code execution, and API functions.
  * **Pattern 3 — Planning:** Having the model generate and update a multi-step action plan before executing tasks.
  * **Pattern 4 — Multi-Agent Collaboration:** Splitting complex workflows across multiple role-specialized agents (such as a coder agent and a tester agent in `AutoGen` or `CrewAI`).

***

## 2. Industry, Enterprise & Autonomy Ladders

**Enterprise & Autonomy Summary:** Software companies and venture capital firms adapt the Society of Automotive Engineers self-driving car scale (SAE Levels 0–5) to measure how much human labor is replaced by AI coding assistants, state-machine orchestration graphs, and enterprise applications.

### 2.1 Self-Driving Style AI Coding Ladders (`2021-06` to `2026-01`)

**SAE L0–L5 Coding Scales:** Engineering leaders at Sourcegraph, Glowforge, Cognition, and Latent Space classify AI software engineering by how far the human programmer steps back from typing individual lines of code to supervising parallel agent fleets.

* **Dan Shapiro's Five Levels of AI Coding (`2026-01`):** Published by Dan Shapiro (CEO of Glowforge, Wharton Fellow) in *"The 5 Levels of AI Coding"* (`2026-01`, modelled directly on SAE J3016 self-driving tiers L0–L5):
  * **Level 0 — Spicy Autocomplete (Manual):** Programmer writes every line and accepts or rejects single-line ghost text completions (`GitHub Copilot` 2021–2022 baseline).
  * **Level 1 — The Coding Intern (Task Offloading):** Programmer designs the software and delegates isolated tasks like writing unit tests, docstrings, or single helper functions via chat (`ChatGPT`, `Copilot Chat`).
  * **Level 2 — The Junior Developer (Active Pairing):** Programmer pairs side-by-side in an AI code editor (`Cursor`, `Windsurf`) that edits multiple files and navigates project imports while the human still reads and approves every line of code.
  * **Level 3 — The Manager (AI Collaborator):** AI writes the majority of code across background tasks (`Claude Code`, `Cursor Agent`) while the human shifts from writing code to reviewing pull-request diffs and setting test constraints.
  * **Level 4 — The Product Team (Orchestration):** Human hands off full product specifications (PRDs) to parallel fleets of agents (`Devin`, multi-instance `Claude Code`), validating only at integration test and pull-request merge stages.
  * **Level 5 — The Dark Factory (Full Autonomy):** End-to-end automated software production where product specifications go in and tested production deployments come out without humans reading the source code.
* **Steve Yegge & Sourcegraph's Eight Coding Levels (`2024-06` to `2026-01`):** Formulated by Steve Yegge (Former Head of Engineering at Sourcegraph) across *"The Death of the Junior Developer"* (`2024-06`, `sourcegraph.com/blog`, coining Chat-Oriented Programming / CHOP) and *"Welcome to Gas Town"* (`2026-01`, January 1, 2026, `steve-yegge.medium.com`), popularized by Shawn "swyx" Wang on *Latent Space*:
  * **Level 1 — Near-Zero AI:** Manual coding supplemented by tab autocomplete and copy-pasting errors into web chat.
  * **Level 2 — Agent in IDE (Permissions On):** Agent inside the code editor (`Sourcegraph Cody`, `Cursor`, `Cline`) reads files and runs terminal commands, pausing for human approval on every action.
  * **Level 3 — YOLO Mode (Auto-Approve):** Developer disables permission prompts and lets the in-editor agent execute multi-file edits and test runs uninterrupted.
  * **Level 4 — Wide Agent (Diffs Fade):** Developer stops inspecting line-by-line code diffs and evaluates the agent by whether tests pass and the app runs.
  * **Level 5 — Agent-First, IDE Later:** Developer works primarily inside a command-line or chat agent (`Claude Code`, `Amp`) and opens the code editor only as a secondary viewer.
  * **Level 6 — Agent Multiplexing:** Developer runs 3 to 5 parallel agent sessions simultaneously across terminal tabs to avoid waiting on single-agent thinking time.
  * **Level 7 — Manual Fleet Management (10+ Agents):** Developer coordinates a dozen concurrent agents by hand, hitting human attention and merge-conflict limits.
  * **Level 8 — Custom Agent Orchestrator ("Gas Town"):** Developer builds automated supervisor software that spawns, routes, merges, and checks worker agents programmatically.

### 2.2 LangChain & Hugging Face Cognitive Architectures (`2023-11` to `2025-01`)

**Six Orchestration Tiers:** Application framework creators Harrison Chase (LangChain) and Hugging Face (`smolagents`) order AI software architectures by how much control the language model exercises over program control flow (`if/else` branches and `while` loops).

* **LangChain Six Levels of Cognitive Architectures (`2024-07`):** Published by Harrison Chase (CEO of LangChain) in *"What is a 'cognitive architecture'?"* (`2024-07`, `blog.langchain.dev/what-is-a-cognitive-architecture/`, building on his `2023-11` essay *"OpenAI's Bet on a Cognitive Architecture"*):
  * **Level 1 — Pure Code:** Deterministic human-written software with zero language model calls.
  * **Level 2 — Single LLM Call:** Code formats data into a prompt, makes one stateless model call, and parses the output (simple summarization or classification).
  * **Level 3 — Chain of LLM Calls:** Predetermined sequence of multiple model calls (`LangChain LCEL`), such as generating a search query in call one and synthesizing retrieved documents in call two.
  * **Level 4 — Router:** Model makes a single dynamic branching decision (`if/else`), selecting which downstream chain, index, or tool to call next while keeping execution bounded to one pass.
  * **Level 5 — State Machine (`LangGraph`):** Combines LLM routing with explicit code-constrained loops (`while` loops with defined state schemas, nodes, and transition edges), letting the system iterate until a check passes while preventing runaway actions.
  * **Level 6 — Autonomous Agent:** Unconstrained loop where the model dynamically selects tools, invents its own sub-steps, and decides when to stop without fixed graph boundaries (`AutoGPT`, open-ended agent harnesses).
* **Hugging Face `smolagents` Agency Spectrum (`2024-12` to `2025-01`):** Published by Aymeric Roucher and the Hugging Face team in *"Introducing smolagents: simple agents that write actions in code"* (`2024-12`, December 31, 2024, `huggingface.co/blog/smolagents`):
  * **Agency Level 0 (☆☆☆) — Simple Processor:** LLM output has zero effect on program control flow.
  * **Agency Level 1 (★☆☆) — Router:** LLM output selects a single conditional branch (`if/else` switch).
  * **Agency Level 2 (★★☆) — Tool-Calling Agent (`ToolCallingAgent`):** LLM decides which external functions to run and generates structured `JSON` arguments inside a loop.
  * **Agency Level 3 (★★★) — Multi-Step Code Agent & Multi-Agent (`CodeAgent`):** LLM writes executable Python code snippets directly to compose tools, loops, and variables inside a secure sandbox (`E2B`, `Modal`, `Docker`) or delegates to subordinate agents.

### 2.3 Venture Capital Market & Stack Ladders (`2022-09` to `2026-01`)

**VC Adoption Horizons:** Sequoia Capital, Menlo Ventures, and Andreessen Horowitz (a16z) map how commercial AI products evolved from novelty text generators to human-paired copilots, enterprise RAG stacks, and outcome-billed autonomous agents.

* **Sequoia Capital's Generative AI Acts 1–3 (`2022-09` to `2026-01`):** Authored by Sonya Huang, Pat Grady, and Stephanie Zhan at Sequoia Capital (`sequoiacap.com`):
  * **Act 1 — Technology-Out Demos (`2022-09`):** Published in *"Generative AI: A Creative New World"* (`2022-09`, September 19, 2022); foundation models unlock fast text, image, and code generation, producing thin chat wrappers and single-turn copywriting apps (`Jasper`, `Copy.ai`, `Midjourney`).
  * **Act 2 — Customer-Back Copilots & Systems (`2023-09`):** Published in *"Generative AI's Act Two"* (`2023-09`, September 20, 2023); products add company context (`RAG`), workflow interfaces, and human-in-the-loop editing to assist professionals (`Harvey`, `Glean`, `Cursor`).
  * **Act 3 / Act o1 — Reasoning Agents & Service-as-a-Software (`2024-10` to `2026-01`):** Published in *"Generative AI's Act o1: The Reasoning Era Begins"* (`2024-10`, October 9, 2024) and *"2026: This is AGI"* (`2026-01`); inference-time reasoning (`OpenAI o1`) shifts products from selling software tools to selling completed work outcomes (**Service-as-a-Software** — autonomous customer support agents like `Sierra`, AI software engineers like `Devin`, and AI accounting/legal associates).
* **Menlo Ventures Enterprise GenAI Architecture Ladder (`2023-11` to `2025-11`):** Published by Matt Murphy, Tim Tully, Joff Redfern, and Deedy Das in *"The State of Generative AI in the Enterprise"* (`2023-11`, `2024-11`, `2025-11`, `menlovc.com/perspective/2024-the-state-of-generative-ai-in-the-enterprise/`), ranking production enterprise usage shares across complexity tiers:
  * **Rung 1 — Fixed Prompting & Routing:** Single model calls and deterministic prompt chains handling summarization, drafting, and classification.
  * **Rung 2 — Retrieval-Augmented Generation (RAG):** Connecting models to enterprise databases (`Snowflake`, `Databricks`, `Pinecone`) via vector embeddings and rerankers (representing the majority — 51% in 2024 — of production enterprise architectures).
  * **Rung 3 — Fine-Tuning & Context Caching:** Customizing open-weight or commercial models (`Llama 3`, `GPT-4o`) on proprietary domain data (~9% of production implementations in 2024).
  * **Rung 4 — Multi-Step Agentic Workflows:** Autonomous planning, tool-calling, and self-correcting execution loops (growing from ~12% experimental pilots in 2024 to the primary enterprise growth driver in 2025).
* **Andreessen Horowitz (a16z) LLM Application Stack (`2023-06` to `2024-03`):** Published by Matt Bornstein, Guido Appenzeller, and Martin Casado in *"Emerging Architectures for LLM Applications"* (`2023-06`, June 20, 2023, `a16z.com/emerging-architectures-for-llm-applications/`), defining the progressive architectural buildout:
  * **Tier 1 — In-Context Learning Foundation:** Calling closed API models (`GPT-4`, `Claude`) or self-hosted open models (`Llama`) with prompt templates.
  * **Tier 2 — Contextual Data Pipeline (RAG):** Adding document loaders (`Unstructured`, `LlamaIndex`), embedding models, and vector databases (`Pinecone`, `Weaviate`, `Chroma`).
  * **Tier 3 — Orchestration & Tool Execution:** Chaining calls and connecting external APIs via orchestration libraries (`LangChain`) and agent loops (`AutoGPT`).
  * **Tier 4 — Validation, Guardrails & Observability:** Wrapping outputs in programmatic validators (`Guardrails AI`, `Rebuff`), caching, and logging (`Weights & Biases`, `Arize`, `Braintrust`).

### 2.4 Gartner Enterprise AI Maturity Model (`2020-01` to `2025-06`)

**Organizational Readiness Tiers:** Gartner scores corporate AI adoption across five organizational stages from early executive curiosity to enterprise-wide autonomous workflows.

* **Authors & Sources:** Gartner Research (`gartner.com`, originally introduced `2020-01` for enterprise ML and updated `2023-08` through `2025-06` for Generative and Agentic AI).
* **Ordering Axis:** Organizational integration depth, governance standardization, and production business impact across company departments.
* **Level 1 — Awareness:** Company leadership discusses AI possibilities with ad-hoc employee experimentation (`Shadow AI` web chat usage) and zero formal projects or infrastructure.
* **Level 2 — Active:** Isolated engineering teams run sandboxed proofs-of-concept (PoCs) and vendor API trials without standardized governance or ROI metrics.
* **Level 3 — Operational:** At least one AI project runs in daily production with dedicated ML/AI engineers, established data pipelines, budget tracking, and measurable business outputs.
* **Level 4 — Systemic:** AI capabilities integrate across multiple departments (`HR`, `Legal`, `Engineering`, `Support`) sharing a unified data platform, model registry, evaluation suite, and security guardrails.
* **Level 5 — Transformational:** AI forms the core operating model of the business, autonomously driving products, supply chains, and customer service with continuous automated retraining and evaluation.

***

## 3. Developer & Practitioner Informal Ladders

**Practitioner Ladders Summary:** Working AI engineers order techniques by engineering effort, cost, and maintenance burden — insisting teams exhaust simple prompting and evaluation tests before adding document search (RAG), tool loops, or custom weight training (fine-tuning).

### 3.1 Practitioner LLM Intervention Hierarchy (`2023-04` to `2025-01`)

**Cost-vs-Complexity Intervention Ladder:** Leading practitioners Chip Huyen, Hamel Husain, Simon Willison, and Shawn "swyx" Wang codified a strict six-rung engineering ladder governing how developers build and optimize LLM applications.

* **Authors & Sources:** Chip Huyen in *"Building LLM applications for production"* (`2023-04`, April 11, 2023, `huyenchip.com/2023/04/11/llm-engineering.html`) and O'Reilly book *"AI Engineering"* (`2025-01`); Shawn "swyx" Wang in *"The Rise of the AI Engineer"* (`2023-06`, June 29, 2023, `latent.space/p/ai-engineer`); Hamel Husain in *"Your AI Product Needs Evals"* (`2024-03`, `hamel.dev/blog/posts/evals/`); and Simon Willison (`simonwillison.net`, `2023–2025`).
* **Ordering Axis:** Implementation cost, infrastructure complexity, data preparation overhead, and runtime latency/risk (always starting at the lowest rung that passes automated evaluation tests).
* **Rung 1 — Zero-Shot Prompting & System Instructions:** Write clear system prompts, role instructions, and output schemas (`JSON` or Markdown) in a single API call with zero external infrastructure.
* **Rung 2 — Few-Shot Examples, Chain-of-Thought & Evals:** Add 3 to 10 curated input-output examples inside the prompt (`In-Context Learning`), instruct the model to write out intermediate reasoning steps (`Chain-of-Thought`), and build an automated test suite (`Evals` using code assertions and `LLM-as-a-Judge`) to measure accuracy before climbing higher.
* **Rung 3 — Retrieval-Augmented Generation (RAG):** When the model needs private or fresh facts, chunk documents, index them via keyword search (`BM25`) plus semantic vector embeddings, rerank top matches, and inject them into the prompt window.
* **Rung 4 — Tool Use & Function Calling:** Give the model structured schemas to invoke deterministic external tools (calculators, SQL database queries, Python interpreters, REST APIs) so the model offloads math and live actions to code.
* **Rung 5 — Agentic Loops & Multi-Step Control Flows:** Wrap tool calls in iterative execution loops (`ReAct`, reflection retries, state graphs) where the model inspects tool outputs or compiler errors and takes follow-up steps.
* **Rung 6 — Fine-Tuning & Reinforcement Learning (`SFT` / `LoRA` / `RL`):** After prompt engineering and RAG plateau, collect thousands of verified production traces to update model weights via parameter-efficient fine-tuning (`LoRA`, `QLoRA`) or reinforcement learning (`DPO`, `RLVR`) to lock in formatting, domain syntax, or smaller-model cost savings.

### 3.2 Eugene Yan Seven Production LLM Patterns (`2023-07`)

**Seven Production Patterns:** Amazon Senior Applied Scientist Eugene Yan organized practical LLM engineering into seven progressive system design patterns moving from quality measurement to continuous data flywheels.

* **Authors & Sources:** Eugene Yan; published in *"Patterns for Building LLM-based Systems & Products"* (`2023-07`, July 31, 2023, `eugeneyan.com/writing/llm-patterns/`).
* **Ordering Axis:** Production system maturity and defensive reliability around an unreliable base model.
* **Pattern 1 — Evals (To Measure Performance):** Benchmark datasets, reference-based metrics (`ROUGE`, `BERTScore`), and reference-free model judges (`G-Eval`, `LLM-as-a-Judge`) to quantify every change.
* **Pattern 2 — RAG (To Add Recent/External Knowledge):** Fetching verified external text snippets at runtime so the model grounds answers in real sources instead of guessing from frozen training weights.
* **Pattern 3 — Fine-Tuning (To Get Better at Specific Tasks):** Adapting pre-trained models (`LoRA`, instruction tuning, distillation) to master narrow task structures, reduce prompt token counts, and lower latency.
* **Pattern 4 — Caching (To Reduce Latency and Cost):** Storing exact or semantically similar prompt-response pairs in memory/vector stores (`Redis`) to serve repeat queries instantly.
* **Pattern 5 — Guardrails (To Ensure Output Quality):** Validating model inputs and outputs via syntactic schema parsers (`Pydantic`, `Guidance`), toxicity filters, and factual consistency checks against retrieved context.
* **Pattern 6 — Defensive UX (To Anticipate Error Gracefully):** Designing user interfaces with confidence indicators, source citations, autocomplete previews, and human correction controls to handle model mistakes smoothly.
* **Pattern 7 — Collect User Feedback (To Build Data Flywheels):** Capturing explicit user ratings (thumbs up/down) and implicit behavior (whether a user edits or accepts an AI draft) to automatically build evaluation and fine-tuning datasets.

### 3.3 Pre-LLM & Early Transformer NLP Ladders (`2017-06` to `2021-07`)

**Four NLP Paradigms:** Prior to chat LLMs, natural language processing (NLP) researchers mapped a four-step historical ladder from hand-crafted rules and static word vectors to fine-tuned `BERT` classifiers and zero/few-shot `GPT-3` prompting.

* **Authors & Sources:** Pengfei Liu, Weizhe Yuan, Jinlan Fu, Zhengbao Jiang, Hiroaki Hayashi, and Graham Neubig (Carnegie Mellon University) in *"Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing"* (`2021-07`, July 28, 2021, `arxiv.org/abs/2107.13586`, ACM Computing Surveys); paired with Sebastian Ruder's *"NLP's ImageNet moment has arrived"* (`2018-07`, July 8, 2018, `thegradient.pub/nlp-imagenet/`).
* **Ordering Axis:** How human engineers adapt a system to a text task — shifting from manual feature extraction to neural network architecture design, self-supervised pre-training + task fine-tuning, and finally natural-language prompting.
* **Step 1 — Non-Neural Feature Engineering (`Pre-2013` Baseline, still widespread in `2017`):** Engineers write regular expressions (`Regex`), part-of-speech rules, and word-count tables (`Bag-of-Words`, `TF-IDF`) fed into classical algorithms (`Logistic Regression`, `Support Vector Machines / SVM`, `CRF`).
* **Step 2 — Pretrained Word Embeddings + Task Neural Networks (`2013–2018` Architecture Engineering):** Engineers initialize models with static word vectors (`Word2Vec`, `GloVe`, `fastText` — where a word like *"bank"* has the exact same vector regardless of sentence context) and train recurrent or convolutional networks (`BiLSTM`, `CNN`) plus attention mechanisms from scratch for each task.
* **Step 3 — Pre-train and Fine-Tune (`2018-05` to `2020-05` Objective Engineering / "NLP's ImageNet Moment"):** Engineers take a deep contextual model pre-trained on massive unlabeled text corpora (`ELMo` `2018-02`, `ULMFiT` `2018-05`, `OpenAI GPT-1` `2018-06`, `BERT` `2018-10`, `RoBERTa` `2019-07`, `T5` `2019-10`), attach a task-specific classification layer on top, and update the model's weights on thousands of labeled examples via Hugging Face `transformers`.
* **Step 4 — Pre-train, Prompt, and Predict (`2020-05`+ Prompt Engineering):** Introduced at scale with `GPT-3` (`2020-05`, Brown et al., `arxiv.org/abs/2005.14165`); engineers keep the massive language model's weights completely frozen and reframe classification, translation, and extraction tasks as text completion prompts using zero examples (`Zero-Shot`) or a handful of examples in the prompt (`Few-Shot In-Context Learning`).

***

## 4. Cross-Ladder Synthesis for Stage 2 Schema Lock

**Master Timeline Alignment:** Comparing all 18 published ladders against the pipeline's rules (Section 3 of `AI_ladder_evol mp.md`) reveals four structural rules for locking the chronological Era Ladders ($L_1 \dots L_n$):

* **Published Axes vs. Pipeline Axis:** Published ladders order steps along four different dimensions — **Capability Percentile** (DeepMind, OpenAI L1–L5), **Control Flow Autonomy** (Anthropic, LangChain, Hugging Face, SAE Coding L0–L5), **Engineering Effort** (Huyen, Yan, OpenAI DevDay), and **Historical Training Paradigm** (Karpathy, Liu et al., Ruder). Our master pipeline unifies these along a single bottom-to-top **Task / Use-Case Complexity Axis** measured by task scope, technical setup, autonomy, and single-task compute/token cost.
* **Speculative Top Rungs Set Aside:** Following Section 3 (`Pass 2 — Top-Down Ladder Cross-Check: set aside speculative published steps until an era where real usage data backs them`), the master era ladders set aside unrealized theoretical tiers — specifically **OpenAI Level 4 (Innovators)** and **Level 5 (Organizations)**, **DeepMind General Levels 3–5 (Expert/Virtuoso/Superhuman AGI)**, and **Dan Shapiro Level 5 (The Dark Factory)** — while retaining every step backed by real empirical usage up through multi-file/repo coding agents and parallel agent orchestration.
* **The Fine-Tuning Rank Inversion Across Eras:** Comparing Pre-LLM ladders (Liu et al., Ruder) against Post-ChatGPT practitioner ladders (Huyen, Yan, Menlo Ventures) exposes a major historical inversion:
  * **In 2018–2020 (`BERT` Era):** Custom model fine-tuning (`BERT` / `RoBERTa` classification) was the **standard middle step** required for everyday business NLP tasks because base models lacked instruction-following and zero-shot capabilities.
  * **In 2023–2026 (`GPT-4` / `Claude 3.5` / `o1` Era):** Zero-shot prompting, long context windows, and RAG absorbed 90%+ of tasks that once required fine-tuning, pushing custom weight training (`LoRA` / `SFT` / `RLVR`) to the **top specialized rung** reserved for high-volume latency/cost optimization or frontier model post-training.
* **Four Clear Structural Era Boundaries (`2017`–`2026`):** Cross-referencing the publication dates and structural step shifts across all cataloged ladders points to five distinct historical eras where at least two structural step changes occurred simultaneously:
  1. **Era 1 (`2017-06` to `2020-05`) — Pre-LLM & Transfer Learning NLP Ladder:** Dominated by feature engineering, static embeddings (`Word2Vec`/`GloVe` + `BiLSTM`), and `BERT` fine-tuning (`NLP's ImageNet Moment`).
  2. **Era 2 (`2020-06` to `2022-10`) — Completion Foundation Models & Early Copilot Ladder:** Triggered by `GPT-3` (`2020-05`/`06` API) and `GitHub Copilot` (`2021-06`), introducing zero/few-shot completion prompting and inline code autocomplete while `BERT` fine-tuning remained the production workhorse.
  3. **Era 3 (`2022-11` to `2024-08`) — Chat UI, Custom RAG Stacks & Early Agent Wrappers Ladder:** Triggered by `ChatGPT` (`2022-11`) and `GPT-4` (`2023-03`), sinking zero-shot completion into consumer Web Chat (Step 1), birthing the custom Python + Vector DB (`LangChain`/`LlamaIndex` + `Pinecone`) RAG explosion, and spawning brittle first-wave autonomous loops (`AutoGPT`).
  4. **Era 4 (`2024-09` to `2025-05`) — Reasoning Models, Built-In Chat RAG & IDE Multi-File Agents Ladder:** Triggered by `OpenAI o1-preview` (`2024-09`), `Claude 3.5 Sonnet` (`2024-06`/`10` Computer Use + Artifacts), and `Cursor Composer` — sinking custom 2023 RAG pipelines into default chat file-uploads, introducing test-time reasoning (`RLVR`), and splitting coding into tab autocomplete vs. multi-file IDE agents.
  5. **Era 5 (`2025-06` to `2026-10`) — Terminal CLI Harnesses, MCP Tool Standards & Parallel Agent Fleets Ladder:** Triggered by `Claude Code` / `Codex CLI`, `Model Context Protocol (MCP)` standardization, `Deep Research`, and `o3`/`Claude 4` long-horizon execution — elevating terminal/cloud background agents and multi-agent fleet supervision (`Level 3–4 Manager/Orchestrator`) into mainstream production workflows.