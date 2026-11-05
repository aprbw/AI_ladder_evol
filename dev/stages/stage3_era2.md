### 3.2 Era 2 Ladder ($L_2$: 2020-06 to 2022-10) — Completion Foundation Models & Early Copilot Ladder

**Era 2 Summary:** Between June 2020 and October 2022 ("The Few-Shot Completion Era"), OpenAI's 175-billion-parameter `GPT-3` (`davinci`) API and `GitHub Copilot` (`Codex`) transformed AI from a custom model-training discipline into a cloud API and inline autocomplete ecosystem, splitting everyday workflows into four distinct steps spanning 4.5 million active users, 18 trillion processed text chunks (tokens), $3.2 billion in total spending, and $3.5 \times 10^{25}$ math operations (floating-point operations / FLOPs).

* **Structural Era Shift:** Pretrained foundation models allowed software engineers and marketers to solve text and coding tasks by writing plain-English examples inside an API call (in-context few-shot learning) rather than training custom neural networks from scratch.
* **Bifurcated Production Reality:** While `GitHub Copilot` ghost text and `GPT-3` copywriting wrappers (`Jasper`, `Copy.ai`) captured 75% of active users across Steps 1 and 2, high-volume enterprise workloads still relied on cloud GPU custom weight training (fine-tuning) of bidirectional encoders (`RoBERTa`, `DeBERTa`, `T5`) and early open-weight decoders (`GPT-J-6B`) at Step 4, which consumed 45% of all era compute.
* **Context & Alignment Ceilings:** Tiny active memory limits (context windows of 2,048 to 4,097 tokens), high API prices ($20 to $60 per 1 million tokens), and raw next-word prediction instability forced engineers building multi-document apps to invent early vector search and prompt-chaining scripts at Step 3 (`FAISS`, `Pinecone`).

***

#### 3.2.1 Valid Dates & Why Era 1 Got Outdated

**Tech, Cost & Habit Shifts:** Era 2 ($L_2$) ran for 29 months from `2020-06` to `2022-10`, opening when OpenAI launched its commercial `GPT-3` (`davinci`) completion API (`2020-06`) followed by the `GitHub Copilot` technical preview (`2021-06`), and closing right before OpenAI released the free `ChatGPT` web interface (`2022-11`).

* **Scaling Laws Breakthrough:** OpenAI's May 2020 paper *"Language Models are Few-Shot Learners"* (`Brown et al.`) and June 2020 commercial API release scaled unidirectional transformer decoders to 175 billion parameters (`GPT-3` `davinci`), trained across $3.14 \times 10^{23}$ FLOPs (a $78\times$ compute jump over 2019 `RoBERTa-Large`). At this scale, a single frozen model learned to perform translation, classification, and text generation purely from a few input-output examples pasted into the prompt string (in-context few-shot learning) with zero gradient weight updates.
* **Code Generation Specialization:** In June 2021, OpenAI and GitHub trained `Codex` (a 12-billion-parameter `GPT-3` descendant fine-tuned on 159 GB of public GitHub Python and multi-language code) and embedded it directly into `Visual Studio Code` as `GitHub Copilot`. This technical shift moved AI from offline batch data processing into real-time, sub-second keystroke prediction inside the developer's code editor (integrated development environment / IDE).
* **Instruction Tuning Alignment:** Raw `GPT-3` (`davinci`) simply predicted likely next words on the internet, frequently answering a question by generating more questions or drifting into fabricated stories (hallucinations). In January and March 2022, OpenAI deployed `InstructGPT` (`text-davinci-001` and `text-davinci-002`), training models to follow direct human instructions using human preference ratings (reinforcement learning from human feedback / RLHF) and doubling the active memory limit (context window) from 2,048 tokens to 4,097 tokens.
* **API Pay-Per-Token Economics:** Era 1 ($L_1$) required engineering teams to rent dedicated cloud GPUs (`Nvidia V100` instances on `AWS EC2` or `SageMaker`) and curate thousands of labeled rows before serving a single query. Era 2 replaced upfront GPU cluster setup with metered cloud API billing — launching at **$60.00 per 1 million tokens** ($0.06 per 1k tokens) for `davinci` in June 2020 and dropping $3\times$ to **$20.00 per 1 million tokens** ($0.02 per 1k tokens) with `text-davinci-002` in 2022 — alongside flat monthly software-as-a-service (SaaS) subscriptions (**$10/month** for `GitHub Copilot` at June 2022 general availability and **$29 to $80/month** for `Jasper` and `Copy.ai`).
* **Foundation Model Habit Shift:** Coined by Percy Liang and the Stanford Center for Research on Foundation Models (CRFM) in August 2021 (*"On the Opportunities and Risks of Foundation Models"*) and taught in Stanford's landmark Winter 2022 course `CS324: Large Language Models`, industry practice shifted from designing task-specific neural network layers to adapting a handful of massive cloud models via browser sandboxes (`OpenAI Playground`), IDE plugins, and Python wrapper scripts.

***

#### 3.2.2 How Steps Changed from Era 1 to Era 2

**Four Structural Step Transitions:** Applying the Two-Shift Era Threshold to the `2020-06` transition reveals four simultaneous structural changes that retired the Era 1 transfer-learning ladder ($L_1$) and established the four-step Era 2 completion ladder ($L_2$).

* **New Steps Emerging:**
  * **Step 1 (Single-Line IDE Code Autocomplete & AI Copywriting Templates):** Emerged as a brand-new entry rung as `GitHub Copilot` (`2021-06` preview, `2022-06` GA), `TabNine`, `Jasper` (originally launched in early 2021 as `Conversion.ai`, renamed `Jarvis`, then `Jasper` in January 2022), and `Copy.ai` wrapped `Codex` and `davinci` API calls behind zero-setup IDE ghost text and fill-in-the-blank web forms.
  * **Step 2 (Zero-Shot & Few-Shot Text Completion Prompting):** Emerged as a new middle step unlocked by `GPT-3` in-context learning, enabling developers and analysts in `OpenAI Playground` or single-call REST APIs to build classifiers, extractors, and creative writing tools (`AI Dungeon`) using 3 to 5 text examples instead of GPU training runs.
  * **Step 3 (Early Vector Embedding Search & Multi-Call Prompt Chains):** Emerged between single-call prompting and full weight training because `GPT-3`'s strict 2,048-to-4,097 token context window could only hold 3 to 6 pages of text. Engineers bypassed this ceiling by converting documents into numerical meaning lists (vector embeddings via `OpenAI Embeddings` and `sentence-transformers`), indexing them in newly launched vector databases (`Pinecone` founded 2021, `Weaviate`, `Milvus`, `FAISS`), and chaining multiple `davinci` calls in Python (`deepset Haystack`, `Dust.tt`, and the October 2022 initial release of `LangChain`).
* **Old Steps Sinking into Default UI:**
  * **$L_1$ Step 1 Sinking:** Era 1's bottom rung (Rule Engines, Keyword Filters & Off-the-Shelf Cloud NLP APIs like `AWS Comprehend` and `spaCy` regex pipelines) sank into invisible backend plumbing, while routine human-facing drafting and single-line code lookup moved into $L_2$ Step 1 inline IDE ghost text and SaaS copywriting templates.
* **Split Steps:**
  * **Completion API Splitting into Steps 2 and 3:** Foundation model API usage split by architectural scope and token cost into **Step 2** (stateless, single-call zero/few-shot completion averaging $1,000\text{–}2,000$ tokens and $\$0.04\text{–}\$0.12$ per task) versus **Step 3** (stateful vector database retrieval plus multi-call sequential prompt chains averaging $8,000\text{–}15,000$ tokens and $\$0.25\text{–}\$0.60$ per task).
* **Combined or Gone Steps:**
  * **$L_1$ Step 2 Gone (`Word2Vec`/`GloVe` + `BiLSTM`/`CNN`):** Static word embeddings paired with task-specific recurrent neural networks collapsed and vanished from both university syllabi (`Stanford CS224N`, `Fast.ai` v4) and greenfield production projects, outclassed on accuracy by pretrained transformers and on setup speed by `davinci` prompting.
  * **$L_1$ Steps 3 & 4 Combined into $L_2$ Step 4 (Task-Specific Encoder & Open-Model Fine-Tuning):** Era 1 Step 3 (`BERT` encoder fine-tuning) and Era 1 Step 4 (custom domain sequence training) merged into $L_2$ Step 4. Because `davinci` cost $20–$60 per 1M tokens with multi-second latency, high-volume enterprise production systems combined encoder fine-tuning (`RoBERTa`, Microsoft `DeBERTa`, Google `T5`) with early open-weight decoder fine-tuning (EleutherAI `GPT-J-6B` released June 2021, `GPT-NeoX-20B` released February 2022, Meta `OPT-175B` May 2022, BigScience `BLOOM-176B` July 2022) at the top complexity rung of the ladder.

```
ERA 1 (2017-06 to 2020-05)                         ERA 2 (2020-06 to 2022-10)
+------------------------------------------+       +------------------------------------------+
| Step 4: From-Scratch Sequence & RL       |------>| Step 4: Task-Specific Encoder &          |
| (Custom Transformer MT, BioBERT, RL)     |   +-->| Open-Model Fine-Tuning (RoBERTa,         |
+------------------------------------------+   |   | DeBERTa, T5, GPT-J-6B on V100/A100)      |
| Step 3: Pretrained Encoder Fine-Tuning   |---+   +------------------------------------------+
| (ULMFiT, BERT, RoBERTa, HuggingFace)     |       | Step 3: Early Vector Embedding Search &  |
+------------------------------------------+   +-->| Multi-Call Prompt Chains (FAISS,         |
| Step 2: Static Word Vectors + BiLSTM     |   |   | Pinecone 2021, Haystack, LangChain Oct22)|
| [GONE / COLLAPSED in 2020]               |   |   +------------------------------------------+
+------------------------------------------+   +-->| Step 2: Zero-Shot & Few-Shot Completion  |
| Step 1: Rule Engines & Cloud NLP APIs    |---+   | Prompting (OpenAI Playground, davinci)   |
| (Regex, spaCy, AWS Comprehend)           |       +------------------------------------------+
+------------------------------------------+------>| Step 1: Single-Line IDE Autocomplete &   |
                                                   | Copywriting Templates (Copilot, Jasper)  |
                                                   +------------------------------------------+
```
**Figure 3.2 — Era 1 to Era 2 Ladder Transition (`2020-06`):** **Cloud completion APIs and inline IDE autocomplete inserted three prompting rungs below custom GPU model fine-tuning while wiping out static word vectors.** Era 1's separate encoder fine-tuning (Step 3) and custom sequence training (Step 4) consolidated into Era 2's top production workhorse (Step 4, 45% of compute), while `Codex` and `GPT-3` `davinci` created Steps 1, 2, and 3 for single-line autocomplete, few-shot prompting, and early vector-search prompt chains.

***

#### 3.2.3 Step-by-Step Breakdown (Steps 1 to 4)

**Four-Rung MECE Profile:** Orders every real-world workflow from `2020-06` to `2022-10` bottom-to-top by task complexity, technical setup, autonomy, and single-task resource cost, showing how practitioners moved across steps.

##### Step 1: Single-Line IDE Code Autocomplete & AI Copywriting Templates

* **Name & Rank:** **Step 1 (Lowest Complexity Rung) — Single-Line IDE Code Autocomplete & AI Copywriting Templates.** Occupies the bottom entry rung of $L_2$, serving **50% of active era users** while consuming **18% of industry compute/tokens** and **20% of spending**.
* **Step Boundaries:**
  * **Floor (Entry Threshold):** Requires zero machine learning knowledge, zero API key management, and zero prompt engineering; users either press `Tab` to accept gray ghost-text code suggestions inside an IDE or type product keywords into fixed web form boxes (such as `Product Name`, `Tone of Voice`, and `Target Audience`).
  * **Difference vs. Step 2 (Ceiling):** Capped at stateless, single-line or single-blurb generation ($10\text{–}100$ output tokens) using hardcoded vendor prompt wrappers. Whenever a user needs custom task logic, multi-example formatting, or direct control over sampling parameters (`temperature`, `stop sequences`), they must climb to Step 2 (`OpenAI Playground` / raw `davinci` API).
* **Concrete Tool Stack:**
  * **Coding Autocomplete:** `GitHub Copilot` extension for `VS Code`, `Neovim`, and `JetBrains` powered by OpenAI `Codex` (`cushman-codex` / `davinci-codex` 12B); `TabNine` (local/cloud `GPT-2` autocomplete); `Kite` (sunset late 2022); `Amazon CodeWhisperer` preview (`2022-06`).
  * **Copywriting & Creative SaaS Wrappers:** `Jasper.ai` (launched 2021 as `Conversion.ai` $\to$ `Jarvis.ai` $\to$ `Jasper` in Jan 2022, featuring 40+ AIDA/PAS marketing templates and "Boss Mode"); `Copy.ai` (90+ form-based copywriting tools); `Writesonic`; `Rytr`; and early visual prompt companions (`DALL-E 2` web UI `2022-04`, `Midjourney` Discord bot `2022-07`, `Stable Diffusion` DreamStudio `2022-08`).
* **Use Cases & Context Switching:**
  * **Who & Goal:** Software engineers autocompleting boilerplate functions, unit test assertions, regex strings, and SQL queries inside `VS Code`; digital marketers, SEO agencies, and e-commerce founders generating Facebook ad variations, Amazon product bullets, and blog introductions.
  * **Courses & Tutorials:** `GitHub Copilot` onboarding labs (2021–2022); `Jasper Bootcamp` and *AI Content Dojo* template guides (2021–2022); *Fast.ai* *"From Deep Learning Foundations to Stable Diffusion"* (`2022`, Jeremy Howard).
  * **Surveys & Annual Reports:** GitHub's landmark controlled study by Sida Peng, Eirini Kalliamvakou et al. (`2022-09`, testing 95 professional programmers between May and June 2022 building an HTTP server in JavaScript) proved that developers with `GitHub Copilot` completed the task **55.8% faster** (`1 hour 11 minutes` vs. `2 hours 41 minutes` for the control group). By its June 21, 2022 general availability launch ($10/month), `Copilot` had onboarded **1.2 million technical preview users** and generated **27% to 40% of code** in enabled files (up to 40% in Python). In venture capital reports, *Sequoia Capital's* *"Generative AI: A Creative New World"* (`2022-09`, Act 1) highlighted `Jasper`'s explosive growth to **$42.5M ARR in 2021** and **$80M ARR in 2022** (raising $125M at a **$1.5B valuation** in October 2022).
  * **News Wins & Failures:** *Wins:* `GitHub Copilot` GA (`2022-06`) and `Stable Diffusion` open-weight release (`2022-08`, cited in *State of AI Report 2022* as the fastest-growing repository in GitHub history). *Failures/Controversies:* Free Software Foundation and open-source maintainers launched legal challenges against `GitHub Copilot` (`2021–2022`, culminating in the November 2022 Doe v. GitHub class-action filing) after demonstrating that `Copilot` occasionally regurgitated verbatim copyrighted code (such as the `Quake III` fast inverse square root function complete with original license comments).
  * **Context Switching by the Same Practitioner:** A full-stack engineer kept `GitHub Copilot` (Step 1) turned on all day inside `VS Code` to tab-complete repetitive Python dictionary mappings and unit tests in 0.3 seconds; when `Copilot` failed to design a complex multi-label text parser, the same engineer switched to a browser tab running `OpenAI Playground` (Step 2) to craft a 5-example `text-davinci-002` completion prompt.
* **Step Resource Use:**
  * **Single-Task Cost:**
    * **Tokens & Compute:** $\sim 150\text{–}300\text{ tokens}$ per autocomplete trigger or template generation ($\sim 200\text{ input context} + 30\text{–}80\text{ output tokens}$); $\text{FLOPs}_{\text{task}} \approx 2 \times (1.2 \times 10^{10}\text{ params}) \times 250\text{ tokens} \approx \mathbf{6.0 \times 10^{12}\text{ FLOPs}}$ on `Codex` 12B (up to $1.0 \times 10^{14}\text{ FLOPs}$ on `davinci` 175B copywriting calls).
    * **Money & Electricity:** $\text{USD}_{\text{task}} \approx \mathbf{\$0.002}$ marginal cloud/API cost (covered by flat $\$10/\text{mo}$ `Copilot` or $\$49\text{–}\$80/\text{mo}$ `Jasper` subscription); $\text{Wh}_{\text{task}} \approx \frac{6 \times 10^{12}}{8 \times 10^{10} \times 3600} \times 1.2 \approx \mathbf{0.025\text{ to }0.05\text{ Wh}}$ per completion.
    * **Human-vs-AI Time:** $\mathbf{0.05\text{ min}}$ ($3\text{ seconds}$) human reading/pressing `Tab` vs. $\mathbf{0.005\text{ min}}$ ($0.3\text{ seconds}$) AI inference latency for code autocomplete ($\sim 1.0\text{ min}$ human form filling vs. $0.03\text{ min}$ AI generation for copywriting templates).
  * **Industry-Wide Share ($L_2$):** **50% of active users** ($\sim 2.25\text{M}$ users), **35% of human-hours** ($\sim 228\text{M}$ hours), **18% of era compute & tokens** ($\sim 3.2 \times 10^{12}$ tokens; $\sim 6.3 \times 10^{24}$ FLOPs), and **20% of era spending** ($\sim \$640\text{M}$).

##### Step 2: Zero-Shot & Few-Shot Text Completion Prompting

* **Name & Rank:** **Step 2 (Low-Middle Complexity Rung) — Zero-Shot & Few-Shot Text Completion Prompting.** Sits above fixed SaaS templates as the direct prompt-engineering tier, used by **25% of active era users** and accounting for **22% of industry compute/tokens** and **18% of spending**.
* **Step Boundaries:**
  * **Difference vs. Step 1 (Floor):** Moves from fixed vendor buttons and single-line ghost text to writing raw text completion prompts with explicit instructions, custom delimiters (`###`, `Q:`, `A:`), 3 to 5 formatted input-output demonstrations (few-shot in-context learning), and manual tuning of decoding dials (`temperature=0.0`, `top_p`, `frequency_penalty`, and custom `stop` tokens) inside `OpenAI Playground` or single-call Python/Node.js REST scripts.
  * **Difference vs. Step 3 (Ceiling):** Restricted to a single stateless API call fitting inside the 2,048-token (`davinci` 2020) or 4,097-token (`text-davinci-002` 2022) context window with zero external database lookup. When a task requires searching across hundreds of pages of private company PDFs or chaining multiple reasoning/verification steps across separate prompts, the developer must step up to Step 3.
* **Concrete Tool Stack:**
  * **Commercial Completion Models & Sandboxes:** OpenAI `GPT-3` base engines (`davinci` 175B, `curie` 6.7B, `babbage` 1.3B, `ada` 350M launched `2020-06`); RLHF instruction-tuned `InstructGPT` models (`text-davinci-001` `2022-01`, `text-davinci-002` `2022-03`); `OpenAI Playground` web console; AI21 Labs `Jurassic-1` (`J1-Jumbo` 178B launched `2021-08`); `Cohere` Generation API (`2021–2022`); Anthropic early closed beta (`2022`).
  * **Consumer Completion Apps & Prompt Libraries:** Latitude `AI Dungeon` (`Dragon` model powered by `GPT-3` `davinci` in 2020–2021); `PromptBase` marketplace (`2022-06`); BigScience `PromptSource` template repository (`2021–2022`).
* **Use Cases & Context Switching:**
  * **Who & Goal:** Startup developers, data analysts, product managers, and interactive fiction writers prototyping customer support email drafters, natural-language-to-SQL converters, resume entity extractors, sentiment classifiers, and interactive roleplay adventures via single completion calls.
  * **Courses & Cookbooks:** *OpenAI API Beta Documentation & Examples* (`2020–2021`, teaching the `Prompt:` $\to$ `Completion:` pattern with stop sequences); *Stanford CS324: Large Language Models* (`Winter 2022`, Percy Liang, Tatsunori Hashimoto, and Christopher Ré, Modules on In-Context Learning and Prompting); *Prompt Engineering Guide* (`dair-ai`, 2022); and *Chain-of-Thought Prompting* tutorials following Jason Wei et al. (`2022-01`, *"Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"*) and Takeshi Kojima et al. (`2022-05`, *"Large Language Models are Zero-Shot Reasoners"*, introducing *"Let's think step by step"*).
  * **Surveys & Annual Reports:** *Stanford HAI AI Index (2022)* and *State of AI Report (2021/2022)* documented how `InstructGPT` (`text-davinci-002`) allowed a 1.3B-parameter instruction-tuned model to beat a raw 175B `GPT-3` model on human preference ratings, shifting developer workflows toward direct zero-shot instruction prompts. Pengfei Liu et al.'s landmark ACM survey *"Pre-train, Prompt, and Predict"* (`2021-07`) formally codified this tier as NLP's "Fourth Paradigm".
  * **News Wins & Failures:** *Wins:* OpenAI's `GPT-3` beta (`2020-06`) went viral across tech news as demos translated English into React/JSX code and SQL queries from 3 examples, generating over 4.5 billion words per day across 300+ apps within nine months (`2021-03` OpenAI report). *Failures:* **Latitude's `AI Dungeon` "Filtergate" Crisis (`2021-04`)** — when raw `GPT-3` completion prompts generated unsafe content in private single-player stories, OpenAI enforced abrupt automated filters and human moderation reviews, sparking a massive user privacy revolt and forcing Latitude to migrate off OpenAI to `AI21 Jurassic-1` and open-source `GPT-J-6B`. In **November 2022**, Meta released **Galactica** (a 120B scientific completion LLM), which was **pulled offline after just 3 days** because users prompted it to generate authoritative-sounding, completely fabricated wiki articles on the history of bears in space and fake scientific citations.
  * **Context Switching by the Same Practitioner:** After prototyping a legal contract clause extractor in `OpenAI Playground` (Step 2) using 4 few-shot examples inside a 2,000-token `text-davinci-002` prompt, an ML engineer hit the 4,097-token wall when a client uploaded a 120-page PDF master services agreement — forcing the engineer to switch to Step 3 and write a Python script that chunked the PDF, embedded paragraphs via `OpenAI Embeddings`, and retrieved the top 5 chunks from `FAISS`.
* **Step Resource Use:**
  * **Single-Task Cost:**
    * **Tokens & Compute:** $\sim 1,000\text{–}2,000\text{ tokens}$ per task ($1,200\text{ input tokens}$ holding instructions + 4 few-shot examples + $300\text{ output tokens}$); $\text{FLOPs}_{\text{task}} \approx 2 \times (1.75 \times 10^{11}\text{ params}) \times 1,500\text{ tokens} \approx \mathbf{5.25 \times 10^{14}\text{ FLOPs}}$.
    * **Money & Electricity:** At `davinci` launch pricing ($60/1M tokens), $1,500\text{ tokens} = \mathbf{\$0.090\text{ USD}}$ ($\sim \$0.04\text{–}\$0.12$ range); at `text-davinci-002` pricing ($20/1M tokens), $1,500\text{ tokens} = \mathbf{\$0.030\text{ USD}}$. Electricity on an A100/V100 cluster ($\eta \approx 1.0 \times 10^{11}\text{ FLOPs/J}$, $\text{PUE}=1.2$): $\text{Wh}_{\text{task}} \approx \frac{5.25 \times 10^{14}}{1.0 \times 10^{11} \times 3600} \times 1.2 \approx \mathbf{1.75\text{ Wh}}$.
    * **Human-vs-AI Time:** $\mathbf{3.0\text{ min}}$ active human prompt crafting, example formatting, and output checking vs. $\mathbf{0.05\text{ min}}$ ($3\text{ seconds}$) AI generation time.
  * **Industry-Wide Share ($L_2$):** **25% of active users** ($\sim 1.12\text{M}$ users), **25% of human-hours** ($\sim 162\text{M}$ hours), **22% of era compute & tokens** ($\sim 4.0 \times 10^{12}$ tokens; $\sim 7.7 \times 10^{24}$ FLOPs), and **18% of era spending** ($\sim \$580\text{M}$).

##### Step 3: Early Vector Embedding Search & Multi-Call Prompt Chains

* **Name & Rank:** **Step 3 (High-Middle Complexity Rung) — Early Vector Embedding Search & Multi-Call Prompt Chains.** Represents the custom application architecture tier built by early AI engineers, used by **7% of active era users** while consuming **15% of industry compute/tokens** and **12% of spending**.
* **Step Boundaries:**
  * **Difference vs. Step 2 (Floor):** Crosses from a single stateless prompt into custom Python software orchestration — splitting long documents into 500-token chunks, calling an embedding model to convert text into dense numerical vectors (768 to 12,288 floating-point numbers), running mathematical similarity searches (cosine similarity / dot-product lookup) in a vector index, and chaining 3 to 8 sequential `text-davinci-002` API calls where output from Call 1 feeds into Call 2.
  * **Difference vs. Step 4 (Ceiling):** Keeps all foundation model weights 100% frozen behind cloud APIs (`OpenAI`) or pre-built embedding libraries (`sentence-transformers`). When an enterprise requires sub-20ms inference latency across 50 million daily classification calls, strict on-premise data residency, or specialized domain weights that prompting cannot achieve, engineers must escalate to Step 4 GPU fine-tuning.
* **Concrete Tool Stack:**
  * **Vector Databases & Search Libraries:** Meta `FAISS` (local C++/Python dense vector index); `Pinecone` (launched in `2021` by Edo Liberty as the first fully managed cloud vector database); `Weaviate`; `Milvus`; `Qdrant` (`2021`); and `Elasticsearch` dense vector plugin.
  * **Embedding Models:** `sentence-transformers` (`SBERT` / `all-MiniLM-L6-v2` on HuggingFace); OpenAI first-generation Embeddings API (`2022-01`: `text-similarity-davinci-001` and `text-search-davinci-doc-001` initially priced at an expensive **$600/1M tokens** [$\$0.60/1\text{k}$] before dropping to **$200/1M tokens** [$\$0.20/1\text{k}$] in September 2022, alongside cheaper `text-search-ada-doc-001` at **$4/1M tokens**).
  * **Early Chaining & Search Frameworks:** `deepset Haystack` (`2020–2022` modular neural search and extractive/generative QA pipelines); `Dust.tt` (`2022` visual prompt chaining); `LangChain` (initial open-source release by Harrison Chase in **October 2022** at the very close of Era 2); and custom Python `asyncio` / `requests` map-reduce summarization scripts.
* **Use Cases & Context Switching:**
  * **Who & Goal:** Backend Python engineers and applied ML teams building semantic search over internal company wikis, customer support ticket routing + draft-reply pipelines, long-document map-reduce summarizers (summarizing 10 chunks separately, then summarizing the summaries), and early retrieval-grounded question answering (formalized by Patrick Lewis et al. at Meta AI in *"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"*, `2020-05`).
  * **Courses & Cookbooks:** *OpenAI Cookbook* (`2022`, `github.com/openai/openai-cookbook`, featuring canonical Jupyter notebooks for `Question_answering_using_embeddings.ipynb` with `text-search-davinci` and `Pinecone`/`FAISS`); *Pinecone Learning Center* tutorials (`2021–2022`, James Briggs on semantic search and `SBERT`); *Stanford CS324* (`Winter 2022`, retrieval-augmented language models); and early academic reasoning-and-action papers (`MRKL Systems` by AI21 Labs `2022-05`, `WebGPT` by OpenAI `2021-12`, and `ReAct` by Shunyu Yao et al. `2022-10`).
  * **Surveys & Annual Reports:** *State of AI Report (2021/2022)* and *Gartner Enterprise AI Maturity (2021–2022)* tracked the rise of vector search infrastructure startups (`Pinecone`, `Weaviate`, `Zilliz/Milvus`) raising over $150M in 2021–2022 as enterprises sought ways to ground `GPT-3` on private corporate documents without paying $100k+ to retrain model weights.
  * **News Wins & Failures:** *Wins:* OpenAI's `WebGPT` (`2021-12`) proved that combining `GPT-3` with live search query generation and source snippet retrieval beat raw `davinci` factual accuracy and human demonstrators on truth benchmarks (`TruthfulQA`). *Failures:* **The $600/1M-Token `davinci` Embedding Bill Shock (`2022-01` to `2022-09`)** — engineering teams who naively indexed 10,000 corporate PDFs using OpenAI's top `text-similarity-davinci-001` endpoint ($0.60 per 1k tokens) racked up **$3,000+ indexing bills in a single afternoon**, forcing most Step 3 builders in 2021–2022 to run local open-source `sentence-transformers` (`all-MiniLM-L6-v2`) on CPU/GPU for embeddings and reserve `text-davinci-002` solely for the final synthesis call.
  * **Context Switching by the Same Practitioner:** An applied AI engineer used Step 3 (`FAISS` + `sentence-transformers` + a 4-call `text-davinci-002` Python script) to build an internal employee handbook Q&A bot serving 200 queries a day; however, when the company needed to classify 5 million incoming e-commerce product reviews every night at under $50/day, the engineer switched to Step 4 to fine-tune a `DeBERTa-v3` classifier on an `AWS p3.2xlarge` GPU.
* **Step Resource Use:**
  * **Single-Task Cost:**
    * **Tokens & Compute:** $\sim 8,000\text{–}15,000\text{ tokens}$ per multi-step task (embedding query + retrieving 5–10 document chunks + 3 to 5 chained `text-davinci-002` map/reduce or verification calls averaging $10,000\text{ input} + 1,500\text{ output tokens}$); $\text{FLOPs}_{\text{task}} \approx 2 \times (1.75 \times 10^{11}) \times 11,500 \approx \mathbf{4.0 \times 10^{15}\text{ FLOPs}}$.
    * **Money & Electricity:** At 2022 `text-davinci-002` pricing ($20/1M tokens) plus vector lookup/embedding overhead, $\text{USD}_{\text{task}} \approx \frac{11,500 \times 20}{10^6} + \$0.05\text{–}\$0.30\text{ embed/DB} \approx \mathbf{\$0.25\text{ to }\$0.60\text{ USD}}$. Electricity: $\text{Wh}_{\text{task}} \approx \frac{4.0 \times 10^{15}}{1.0 \times 10^{11} \times 3600} \times 1.2 \approx \mathbf{13.3\text{ Wh}}$ ($\sim 10\text{–}15\text{ Wh}$ range).
    * **Human-vs-AI Time:** $\mathbf{5.0\text{ min}}$ active human Python script orchestration, chunk inspection, and pipeline debugging vs. $\mathbf{0.25\text{ min}}$ ($15\text{ seconds}$) sequential multi-call AI runtime.
  * **Industry-Wide Share ($L_2$):** **7% of active users** ($\sim 315\text{k}$ users), **10% of human-hours** ($\sim 65\text{M}$ hours), **15% of era compute & tokens** ($\sim 2.7 \times 10^{12}$ tokens; $\sim 5.25 \times 10^{24}$ FLOPs), and **12% of era spending** ($\sim \$380\text{M}$).

##### Step 4: Task-Specific Encoder & Open-Model Fine-Tuning

* **Name & Rank:** **Step 4 (Top Complexity Rung) — Task-Specific Encoder & Open-Model Fine-Tuning.** Occupies the highest complexity rung of $L_2$ — merging Era 1's encoder fine-tuning and custom domain training into the primary enterprise production workhorse used by **18% of active era users** while consuming **45% of all industry compute/tokens** and **50% of total era spending**.
* **Step Boundaries:**
  * **Difference vs. Step 3 (Floor):** Moves from calling frozen models via API to preparing labeled datasets (1,000 to 1,000,000+ examples), provisioning dedicated single- or multi-GPU cloud servers (`Nvidia V100` 16/32GB or `A100` 40/80GB), running full-parameter gradient descent weight updates (`PyTorch`, `HuggingFace Trainer`, `DeepSpeed`), and deploying custom model checkpoints behind production inference servers (`TorchServe`, `ONNX Runtime`, `NVIDIA Triton`).
  * **Ceiling (Era 2 Upper Limit):** Represents the maximum practical complexity of Era 2; autonomous multi-step coding agents and RLVR reasoning loops were absent because 2020–2022 models lacked reliable multi-turn tool calling, had narrow 2k–4k context windows, and cost too much per token for recursive trial-and-error loops.
* **Concrete Tool Stack:**
  * **Encoder & Seq2Seq Workhorses:** `RoBERTa-Large`, `DistilBERT`, Microsoft `DeBERTa` / `DeBERTa-v3` (`2020–2021`), Google `T5` / `FLAN-T5` (`2020–2022`), `BART`, and domain encoders (`BioBERT`, `FinBERT`, `LegalBERT`).
  * **Early Open-Weight Decoder Models & Cloud Fine-Tuning:** EleutherAI `GPT-Neo` (1.3B/2.7B, `2021-03`), `GPT-J-6B` (`2021-06`), and `GPT-NeoX-20B` (`2022-02`); Meta `OPT-175B` (`2022-05`); BigScience `BLOOM-176B` (`2022-07`); plus OpenAI's commercial fine-tuning API (`curie` / `babbage` / `ada` fine-tuning endpoints).
  * **Training & Serving Infrastructure:** HuggingFace `transformers`, `datasets`, `tokenizers`, and `Accelerate`; `PyTorch 1.7–1.12`; `TensorFlow 2.x`; `DeepSpeed` ZeRO stages 1–3; `Weights & Biases` (`wandb`) experiment tracking; `AWS SageMaker`, `Google Cloud Vertex AI`, `Lambda Labs` V100/A100 GPU clusters; `ONNX Runtime` and `NVIDIA TensorRT` for sub-10ms production quantization.
* **Use Cases & Context Switching:**
  * **Who & Goal:** Enterprise ML engineers, Kaggle competitors, search ranking teams, and healthcare/finance data scientists training high-throughput production classifiers (fraud detection, content moderation, clinical note ICD-10 coding, e-commerce search relevance) that ran millions of times per day at $100\times$ lower unit cost and $50\times$ lower latency than `GPT-3` `davinci`, or training open-weight `GPT-J-6B` models on sensitive private data that corporate compliance barred from leaving the company firewall.
  * **Courses & Syllabi:** *The Hugging Face Course* (launched `2021`, teaching `AutoModelForSequenceClassification`, `Trainer`, and Hub deployment); *Stanford CS224N: NLP with Deep Learning* (`2021–2022`, Chris Manning, covering `BERT`/`T5` pretraining and fine-tuning); *Fast.ai Practical Deep Learning for Coders v4* (`2020–2022`, Jeremy Howard & Sylvain Gugger with `fastai2` and `blurr` HuggingFace integration).
  * **Surveys & Annual Reports:** In the *Stack Overflow Developer Survey (2021 & 2022)* across 73,000–80,000 developers, traditional ML/DL training frameworks remained the backbone of professional AI work — **TensorFlow (12.95%)**, **scikit-learn (~12%)**, and **PyTorch (8.6%–8.7%)** dominated developer usage logs. *Stanford HAI AI Index (2022)* documented that **BERT-Large training costs had fallen to ~$3,288** while **RoBERTa-Large cost ~$160,018**, making fine-tuning existing checkpoints on $100–$2,500 cloud GPU budgets the standard enterprise deployment path while McKinsey recorded organizational AI adoption plateauing at **50%–56%** due to the high ML engineering skill required at Step 4.
  * **News Wins & Failures:** *Wins:* In **January 2021**, Microsoft's **DeBERTa** (1.5B parameters with disentangled attention) **surpassed the human baseline on the SuperGLUE benchmark** for the first time (scoring 89.9 vs. 89.8 human baseline); in **November 2020**, DeepMind's custom attention network **AlphaFold 2** solved the 50-year protein-folding grand challenge at CASP14; and in **June 2021**, EleutherAI released **GPT-J-6B**, giving the open-source community its first free 6B model matching OpenAI's `curie`. *Failures:* **Zillow Offers Collapse (`2021-11`)** — Zillow shut down its automated home-buying ("iBuying") division, taking a **$304M to $500M+ inventory write-down** and laying off 25% of its workforce (2,000 employees) after its custom-trained pricing and demand forecasting ML models failed to adapt to rapid 2021 housing market shifts, illustrating the fragility of expensive custom-trained production models when underlying data distributions shift.
  * **Context Switching by the Same Practitioner:** A senior ML engineer at a fintech company used `GitHub Copilot` (Step 1) to write PyTorch data-loader boilerplate, used a 3-shot `text-davinci-002` script (Step 2) to automatically label 10,000 raw customer support tickets ("silver labels"), and then fed those 10,000 GPT-3-labeled rows into a 6-hour `DeBERTa-v3` fine-tuning job on 4 `Nvidia A100` GPUs (Step 4) so the final production model could classify 20 million transactions a day at 4 milliseconds per query without paying OpenAI API fees.
* **Step Resource Use:**
  * **Single-Task Cost (1 Full Fine-Tuning Job + Production Validation):**
    * **Tokens & Compute:** $\sim 5 \times 10^6\text{ to }5 \times 10^8\text{ training tokens}$ across 3–5 epochs (e.g., 50k–500k examples $\times 512$ tokens; plus $512\text{ tokens}$ per downstream inference call); $\text{FLOPs}_{\text{task}} \approx 6 \cdot N_{\text{params}} \cdot D_{\text{train\_tokens}} \approx \mathbf{1.0 \times 10^{18}\text{ to }1.0 \times 10^{20}\text{ training FLOPs}}$ (and $10^{11}\text{ to }10^{13}\text{ FLOPs}$ per single inference call).
    * **Money & Electricity:** $\text{USD}_{\text{task}} \approx \mathbf{\$100\text{ to }\$2,500\text{ USD}}$ per cloud GPU fine-tuning & hyperparameter sweep run on `AWS p3.8xlarge` (4xV100 at ~$12/hr) or `p4d.24xlarge` (8xA100 at ~$32/hr), yielding a marginal serving cost of $\sim \$0.00002$ per inference query; Electricity: $\text{Wh}_{\text{task}} \approx \mathbf{15,000\text{ to }120,000\text{ Wh}}$ ($15\text{–}120\text{ kWh}$ per multi-GPU training run, or $0.005\text{–}0.05\text{ Wh}$ per inference query).
    * **Human-vs-AI Time:** $\mathbf{480\text{ min}}$ ($8\text{ hours}$ of active human dataset cleaning, training script configuration, and evaluation metric auditing) vs. $\mathbf{240\text{ to }2,880\text{ min}}$ ($4\text{ to }48\text{ hours}$ of unattended GPU training and evaluation runtime).
  * **Industry-Wide Share ($L_2$):** **18% of active users** ($\sim 810\text{k}$ ML engineers/data scientists), **30% of human-hours** ($\sim 195\text{M}$ hours), **45% of era compute & tokens** ($\sim 8.1 \times 10^{12}$ tokens equivalent; $\sim 1.58 \times 10^{25}$ FLOPs), and **50% of era spending** ($\sim \$1.60\text{B}$ in cloud GPU training and production inference clusters).

***

#### 3.2.4 Era 2 Full-Ladder Resource Totals

**29-Month Era Resource Aggregate (`2020-06` to `2022-10`):** Summing single-task physics and commercial billing across all four steps over the 29-month window of Era 2 ($L_2$) shows an industry in transition — where lightweight autocomplete and prompting captured 75% of users at the bottom of the ladder, while heavy GPU fine-tuning and high-volume production encoders still consumed nearly half of all compute and dollars at the top.

* **Total Compute (FLOPs):** **$\sim 3.5 \times 10^{25}\text{ FLOPs}$** executed across the 29-month era. Roughly $1.2 \times 10^{25}\text{ FLOPs}$ went into frontier and open-weight foundation model pretraining runs (`GPT-3` at $3.14 \times 10^{23}$, `Gopher`, `Chinchilla`, `Megatron-Turing 530B` at $5.3 \times 10^{23}$, `PaLM 540B` at $2.53 \times 10^{24}$, `OPT-175B`, `BLOOM-176B`, `GPT-J-6B`, `GPT-NeoX-20B`), while $\sim 2.3 \times 10^{25}\text{ FLOPs}$ powered Step 4 enterprise fine-tuning/serving ($45\%$ total share) and Steps 1–3 commercial `Codex`/`davinci` API inference ($55\%$ combined share).
* **Total Electricity (MWh):** **$\sim 240,000\text{ MWh}$ ($0.24\text{ TWh}$)** of datacenter electricity, calculated from $3.5 \times 10^{25}\text{ FLOPs}$ running on `Nvidia V100` and early `A100` clusters averaging realized cluster efficiency $\eta_{\text{era}} \approx 8.0 \times 10^{10}\text{ FLOPs/Joule}$ with datacenter cooling overhead $\text{PUE} \approx 1.20$ ($\text{MWh} = \frac{3.5 \times 10^{25}}{8.0 \times 10^{10} \times 3.6 \times 10^9} \times 1.20 \approx 145,833\text{ MWh}$ active GPU + host/storage/idle cluster overhead $\approx 240,000\text{ MWh}$).
* **Total Spending (USD):** **$\sim \$3.20\text{ Billion USD}$** across all steps — comprising $\sim \$1.60\text{B}$ (50%) in Step 4 cloud GPU fine-tuning and enterprise encoder serving (`AWS SageMaker`, `GCP`, `Azure`), $\sim \$640\text{M}$ (20%) in Step 1 SaaS subscriptions (`Jasper` scaling to $\$80\text{M}$ ARR, `Copy.ai`, `GitHub Copilot` $\$10/\text{mo}$ tier, and IDE plugins), $\sim \$580\text{M}$ (18%) in Step 2 commercial completion API bills (`OpenAI davinci`/`InstructGPT`, `AI21`, `Cohere`), and $\sim \$380\text{M}$ (12%) in Step 3 managed vector databases (`Pinecone`, `Weaviate`, `Milvus`) and multi-call API pipelines.
* **Total Token Volume:** **$\sim 1.8 \times 10^{13}\text{ tokens}$ ($18.0\text{ Trillion tokens}$)** processed across all four steps — spanning $3.2\text{T}$ tokens in Step 1 (`Copilot` inline completions and copywriting templates), $4.0\text{T}$ tokens in Step 2 (`davinci` and `Playground` completion calls, rising from OpenAI's reported 4.5B words/day in early 2021 to 20B+ tokens/day by autumn 2022), $2.7\text{T}$ tokens in Step 3 (embedding indexing + multi-call prompt chains), and $8.1\text{T}$ tokens equivalent in Step 4 (custom training epochs + high-volume production encoder inference).
* **Total Human Usage:** **$\sim 4.5\text{ Million active practitioners and creators}$** logging **$\sim 650\text{ Million human-hours}$** across `2020-06` to `2022-10` — led by 2.25M developers and marketers at Step 1 (1.2M+ on `GitHub Copilot` and 1M+ on `Jasper`/`Copy.ai`), 1.12M prompt builders and creators at Step 2 (`OpenAI Playground`, `AI Dungeon`), 315k applied search/chaining engineers at Step 3 (`FAISS`, `Pinecone`, `Haystack`), and 810k ML engineers and data scientists at Step 4 (`HuggingFace`, `PyTorch`, `TensorFlow`).

| Step Rank & Name | Cross-Era Evolution Link (from $L_1$) | Primary Tool Stack (`2020-06` to `2022-10`) | Single-Task Tokens | Single-Task Compute (FLOPs) | Single-Task Cost (USD) | Single-Task Energy (Wh) | Human vs. AI Time (min) | User Share % | Human-Hours Share % | Compute / Token Share % | Spend Share % |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Step 4:** Task-Specific Encoder & Open-Model Fine-Tuning | **Evolved & Combined Step** (Merges $L_1$ Step 3 `BERT` & Step 4 Custom Models) | `RoBERTa`, `DeBERTa`, `T5`, `GPT-J-6B`, `HuggingFace Trainer`, `PyTorch` on V100/A100 | $5 \times 10^6\text{–}5 \times 10^8$ train ($512$ infer) | $10^{18}\text{–}10^{20}$ train ($10^{11}$ infer) | $\$100\text{–}\$2,500$ run ($\$0.00002$ infer) | $15\text{k–}120\text{k Wh}$ ($0.01\text{ Wh}$ infer) | $480\text{m}$ human vs. $240\text{–}2880\text{m}$ AI | 18% | 30% | 45% | 50% |
| **Step 3:** Early Vector Embedding Search & Multi-Call Prompt Chains | **Split / New Step** (Emerges between single-call prompt & GPU training) | `FAISS`, `Pinecone` (2021), `Weaviate`, `Haystack`, `OpenAI Embeddings`, `LangChain` (Oct 2022) | $8,000\text{–}15,000$ | $4.0 \times 10^{15}$ | $\$0.25\text{–}\$0.60$ | $13.3\text{ Wh}$ | $5.0\text{m}$ human vs. $0.25\text{m}$ AI | 7% | 10% | 15% | 12% |
| **Step 2:** Zero-Shot & Few-Shot Text Completion Prompting | **New Step** (Unlocked by `GPT-3` in-context learning & `InstructGPT` RLHF) | `OpenAI Playground`, `davinci`, `text-davinci-002`, `AI21 Jurassic-1`, `AI Dungeon` | $1,000\text{–}2,000$ | $5.25 \times 10^{14}$ | $\$0.04\text{–}\$0.12$ ($\$0.03$ on `002`) | $1.75\text{ Wh}$ | $3.0\text{m}$ human vs. $0.05\text{m}$ AI | 25% | 25% | 22% | 18% |
| **Step 1:** Single-Line IDE Code Autocomplete & AI Copywriting Templates | **Old Step Sinking into Default UI** (Supersedes $L_1$ Step 1 rules with inline ghost text) | `GitHub Copilot` (`Codex`), `TabNine`, `Jasper.ai` (`Jarvis`), `Copy.ai` | $150\text{–}300$ | $6.0 \times 10^{12}$ | $\$0.002$ ($\$10\text{–}\$80/\text{mo}$ flat) | $0.03\text{ Wh}$ | $0.05\text{m}$ human vs. $0.005\text{m}$ AI | 50% | 35% | 18% | 20% |
| **Era 2 ($L_2$) Total / Aggregate** | **$L_1$ Step 2 (`Word2Vec`+`BiLSTM`) Gone; 3 New Prompt/Vector Steps Added** | **Hybrid Completion API (`davinci`/`Codex`) + Fine-Tuned Encoder (`DeBERTa`) Ecosystem** | **$1.8 \times 10^{13}$ Total Era Tokens** | **$3.5 \times 10^{25}$ Total Era FLOPs** | **$\$3.20\text{B}$ Total Era Spend** | **$240,000\text{ MWh}$ ($0.24\text{ TWh}$)** | **$4.5\text{M}$ Users / $650\text{M}$ Human-Hrs** | **100%** | **100%** | **100%** | **100%** |

```json
{
  "era_id": "L2",
  "era_name": "Completion Foundation Models & Early Copilot Ladder (The Few-Shot Completion Era)",
  "start_date": "2020-06",
  "end_date": "2022-10",
  "duration_months": 29,
  "era_totals": {
    "total_compute_flops": 3.5e25,
    "total_electricity_mwh": 240000,
    "total_spending_usd": 3200000000,
    "total_tokens": 1.8e13,
    "active_users": 4500000,
    "total_human_hours": 650000000
  },
  "collapsed_from_previous_era": [
    {
      "previous_step": "L1_Step_2",
      "previous_name": "Static Word Vectors + Task-Specific Neural Networks (Word2Vec/GloVe + BiLSTM/CNN)",
      "transition_type": "Combined or Gone Step",
      "reason": "Completely replaced by pretrained transformer encoders (RoBERTa/DeBERTa) and zero/few-shot API completion (GPT-3 davinci)."
    }
  ],
  "steps": [
    {
      "step_rank": 1,
      "step_id": "L2_Step_1",
      "step_name": "Single-Line IDE Code Autocomplete & AI Copywriting Templates",
      "cross_era_link_from_L1": {
        "transition_type": "Old Step Sinking into Default UI",
        "source_steps": ["L1_Step_1"],
        "description": "Absorbs L1 Step 1 routine text/code assistance into zero-setup inline IDE ghost text (GitHub Copilot) and form-based SaaS copywriting wrappers (Jasper, Copy.ai)."
      },
      "task_complexity_scope": "Single line of code (10-50 tokens) or short marketing ad blurb via fixed form template",
      "tool_stack": [
        "GitHub Copilot (OpenAI Codex 12B)",
        "TabNine",
        "Jasper.ai (Conversion.ai / Jarvis)",
        "Copy.ai",
        "Writesonic"
      ],
      "single_task_cost": {
        "tokens_min": 150,
        "tokens_max": 300,
        "tokens_typical": 250,
        "compute_flops": 6.0e12,
        "cost_usd_typical": 0.002,
        "subscription_usd_monthly": "10.00-80.00",
        "electricity_wh": 0.03,
        "human_time_minutes": 0.05,
        "ai_runtime_minutes": 0.005
      },
      "industry_wide_share": {
        "user_share_pct": 50.0,
        "human_hours_share_pct": 35.0,
        "compute_token_share_pct": 18.0,
        "spending_share_pct": 20.0,
        "era_tokens_step": 3.24e12,
        "era_compute_flops_step": 6.3e24,
        "era_spending_usd_step": 640000000
      }
    },
    {
      "step_rank": 2,
      "step_id": "L2_Step_2",
      "step_name": "Zero-Shot & Few-Shot Text Completion Prompting",
      "cross_era_link_from_L1": {
        "transition_type": "New Step",
        "source_steps": [],
        "description": "Unlocked by GPT-3 (davinci) 175B in-context learning and InstructGPT (text-davinci-002) RLHF instruction tuning without gradient weight updates."
      },
      "task_complexity_scope": "Single paragraph generation, classification, SQL translation, or entity extraction via 3-5 in-prompt examples within 2,048-4,097 token context window",
      "tool_stack": [
        "OpenAI Playground",
        "GPT-3 davinci / curie API",
        "InstructGPT (text-davinci-001 / text-davinci-002)",
        "AI21 Jurassic-1",
        "Cohere API",
        "AI Dungeon (Dragon)"
      ],
      "single_task_cost": {
        "tokens_min": 1000,
        "tokens_max": 2000,
        "tokens_typical": 1500,
        "compute_flops": 5.25e14,
        "cost_usd_min": 0.03,
        "cost_usd_max": 0.12,
        "cost_usd_typical": 0.06,
        "electricity_wh": 1.75,
        "human_time_minutes": 3.0,
        "ai_runtime_minutes": 0.05
      },
      "industry_wide_share": {
        "user_share_pct": 25.0,
        "human_hours_share_pct": 25.0,
        "compute_token_share_pct": 22.0,
        "spending_share_pct": 18.0,
        "era_tokens_step": 3.96e12,
        "era_compute_flops_step": 7.7e24,
        "era_spending_usd_step": 580000000
      }
    },
    {
      "step_rank": 3,
      "step_id": "L2_Step_3",
      "step_name": "Early Vector Embedding Search & Multi-Call Prompt Chains",
      "cross_era_link_from_L1": {
        "transition_type": "Split / New Step",
        "source_steps": ["L1_Step_3"],
        "description": "Emerges between single-prompt completion and full GPU fine-tuning to bypass the 2k-4k token context limit using vector databases and sequential Python prompt scripts."
      },
      "task_complexity_scope": "Multi-document semantic lookup and 3-8 chained completion calls for long-document QA and summarization",
      "tool_stack": [
        "FAISS",
        "Pinecone (2021 launch)",
        "Weaviate",
        "Milvus",
        "sentence-transformers (SBERT)",
        "OpenAI Embeddings (text-similarity-davinci-001 / text-search-ada-doc-001)",
        "deepset Haystack",
        "Dust.tt",
        "LangChain (Oct 2022 initial release)"
      ],
      "single_task_cost": {
        "tokens_min": 8000,
        "tokens_max": 15000,
        "tokens_typical": 11500,
        "compute_flops": 4.0e15,
        "cost_usd_min": 0.25,
        "cost_usd_max": 0.60,
        "cost_usd_typical": 0.40,
        "electricity_wh": 13.3,
        "human_time_minutes": 5.0,
        "ai_runtime_minutes": 0.25
      },
      "industry_wide_share": {
        "user_share_pct": 7.0,
        "human_hours_share_pct": 10.0,
        "compute_token_share_pct": 15.0,
        "spending_share_pct": 12.0,
        "era_tokens_step": 2.7e12,
        "era_compute_flops_step": 5.25e24,
        "era_spending_usd_step": 380000000
      }
    },
    {
      "step_rank": 4,
      "step_id": "L2_Step_4",
      "step_name": "Task-Specific Encoder & Open-Model Fine-Tuning",
      "cross_era_link_from_L1": {
        "transition_type": "Evolved & Combined Step",
        "source_steps": ["L1_Step_3", "L1_Step_4"],
        "description": "Merges L1 Step 3 (BERT fine-tuning) and L1 Step 4 (custom domain sequence models) into the high-volume enterprise production workhorse at the top of L2."
      },
      "task_complexity_scope": "Full-weight cloud GPU fine-tuning and high-throughput low-latency production serving on custom domain datasets",
      "tool_stack": [
        "RoBERTa-Large",
        "Microsoft DeBERTa / DeBERTa-v3",
        "Google T5",
        "EleutherAI GPT-J-6B / GPT-NeoX-20B",
        "Meta OPT-175B / BigScience BLOOM-176B",
        "HuggingFace transformers & Trainer",
        "PyTorch / DeepSpeed",
        "AWS SageMaker / Nvidia V100 & A100 GPUs"
      ],
      "single_task_cost": {
        "tokens_min": 5000000,
        "tokens_max": 500000000,
        "tokens_typical": 50000000,
        "inference_tokens_per_call": 512,
        "compute_flops_train_min": 1.0e18,
        "compute_flops_train_max": 1.0e20,
        "compute_flops_train_typical": 1.0e19,
        "compute_flops_infer_per_call": 1.0e11,
        "cost_usd_train_min": 100.0,
        "cost_usd_train_max": 2500.0,
        "cost_usd_train_typical": 600.0,
        "cost_usd_infer_per_call": 0.00002,
        "electricity_wh_train_min": 15000.0,
        "electricity_wh_train_max": 120000.0,
        "electricity_wh_train_typical": 45000.0,
        "human_time_minutes": 480.0,
        "ai_runtime_minutes": 720.0
      },
      "industry_wide_share": {
        "user_share_pct": 18.0,
        "human_hours_share_pct": 30.0,
        "compute_token_share_pct": 45.0,
        "spending_share_pct": 50.0,
        "era_tokens_step": 8.1e12,
        "era_compute_flops_step": 1.575e25,
        "era_spending_usd_step": 1600000000
      }
    }
  ]
}
```