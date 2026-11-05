### 3.1 Era 1 Ladder ($L_1$: 2017-06 to 2020-05) — Pre-LLM & Transfer-Learning NLP Ladder

**Era 1 Summary:** Covers the 36-month window from `2017-06` to `2020-05` (*"The Fine-Tuned Encoder Era"*), when natural language processing (NLP) shifted from hand-built keyword rules and task-specific word-sequence networks (recurrent neural networks / RNNs) to self-attention networks (Transformers) and pretrain-then-finetune language encoders (`ULMFiT`, `BERT`, `RoBERTa`). Across this era, everyday production traffic stayed anchored in Step 1 rule engines and cloud APIs (62% of active users) and Step 2 static word vectors (`Word2Vec` + `BiLSTM`, 23% of users), while Step 3 pretrained encoder fine-tuning (`BERT` via `HuggingFace`, 13% of users) and Step 4 from-scratch sequence and deep reinforcement learning (deep RL) runs (2% of users) consumed 60% of all era AI compute.

#### 3.1.1 Valid Dates & Why Old Ladders Got Outdated

**Window & Triggers:** Spans `2017-06` to `2020-05`, opened by three foundational releases that replaced isolated task training with reusable pretrained language representations and closed when OpenAI's `GPT-3` completion API (`2020-06`) introduced zero-shot and few-shot prompting.

* **Opening Breakthroughs (`2017-06` to `2018-10`):** Three research milestones launched Era 1 and retired the pre-2017 hand-crafted feature ladder:
  * **Self-Attention Architecture (`2017-06`):** Google Brain and Google Research published *"Attention Is All You Need"* (`2017-06`), introducing a network design that processes all words in a sentence in parallel by weighing how strongly each word relates to every other word (self-attention Transformer). This parallel design replaced slow step-by-step word processing (recurrent neural networks / RNNs) and cut base translation training cost to $\$930$ ($\sim 3.3 \times 10^{18}$ math operations [floating-point operations / FLOPs]).
  * **Three-Stage Transfer Learning (`2018-01`):** Jeremy Howard and Sebastian Ruder released Universal Language Model Fine-Tuning (`ULMFiT`, `2018-01`), proving that pretraining a language network on general Wikipedia text and fine-tuning it on a target task matched from-scratch accuracy using $100\times$ fewer labeled examples (100 labeled movie reviews instead of 10,000).
  * **Bidirectional Pretrained Encoders (`2018-10`):** Jacob Devlin and colleagues at Google released Bidirectional Encoder Representations from Transformers (`BERT`, `2018-10`), training a deep network to fill in masked-out words using both left and right sentence context (masked language modeling) at a cloud compute cost of $\$3,288$ ($\sim 1.9 \times 10^{20}$ FLOPs for `BERT-Large`), sweeping 11 NLP benchmarks overnight.
* **Technical Shifts:** Pre-2017 text systems relied on word-count tables (term frequency–inverse document frequency / TF-IDF) and static word lookup tables (`Word2Vec`, `GloVe`) where a polysemous word like *"bank"* held the exact same number list (vector embedding) whether describing a river bank or a financial bank. Era 1 replaced static lookups with sentence-aware word representations (contextual embeddings from `ELMo` and `BERT`) and sub-word text splitting (WordPiece and byte-pair encoding / BPE tokenization), handling rare words cleanly while fitting inside a fixed 512-subword memory limit (context window).
* **Economic Shifts:** Cloud providers packaged baseline text extraction into sub-cent utility calls — led by `AWS Comprehend` (`2017-11` launch at $\$0.0001$ per 100-character unit) and `Google Cloud Natural Language API` — while Nvidia's Tesla `V100` tensor-core GPUs (`2017-06`) and Google's Cloud `TPU v2/v3` pods brought custom `BERT-Base` fine-tuning down to $\$1.50\text{–}\$50$ per run. Meanwhile, frontier pretraining costs escalated by two orders of magnitude inside two years, jumping from $\$930$ (`Transformer` base, 2017) and $\$3,288$ (`BERT-Large`, 2018) to $\$160,018$ (`RoBERTa-Large`, `2019-07`, $\sim 4.0 \times 10^{21}$ FLOPs), concentrating from-scratch pretraining inside well-funded labs.
* **Workflow & Cultural Shifts:** Sebastian Ruder declared in `2018-07` that *"NLP's ImageNet moment has arrived,"* marking the shift from Andrej Karpathy's *Software 1.0* (`2017-11`, hand-coded rules) into *Software 2.0* (curating labeled datasets to optimize neural network weights). Across universities and industry teams, `PyTorch` overtook `TensorFlow 1.x` as the primary research library (*State of AI Report 2019*; *GitHub Octoverse 2018–2019*), while HuggingFace's `pytorch-transformers` (`2018–2019`) standardized model sharing so any engineer could download a pretrained checkpoint in three lines of Python.

#### 3.1.2 How Steps Changed in Era 1

**Four Structural Movements:** Maps how the pre-2017 landscape of manual feature engineering and standalone task networks reorganized into the four steps of Ladder $L_1$.

* **New Top & Breakthrough Steps:** Two high-complexity rungs reshaped the top half of the ladder:
  * **Step 3 Emergence (Pretrained Encoder Fine-Tuning):** `ULMFiT` (`2018-01`), `BERT` (`2018-10`), and `RoBERTa` (`2019-07`) created a brand-new Step 3 where engineers downloaded a general-purpose language encoder, attached a single linear classification layer on top (task head), and fine-tuned all weights on 1,000–50,000 labeled rows for multi-sentence question answering and search ranking.
  * **Step 4 Consolidation (From-Scratch Sequence & Deep RL Systems):** Multi-GPU sequence pretraining (`fairseq`, `tensor2tensor`, domain-specific `BioBERT` and `SciBERT`) and massive simulation-based reinforcement learning (`AlphaGo Zero`, `OpenAI Five`, `AlphaStar`) formed the top Step 4 ceiling ($10^{19}\text{–}10^{21}$ FLOPs).
* **Old Steps Sinking into Default UI & Commodity APIs:** Pre-2017 custom statistical pipelines — such as training bespoke conditional random fields (`CRF`) or support vector machines (`SVM`) for basic named-entity tagging, language detection, and sentiment polarity — sank into Step 1 one-line REST calls (`AWS Comprehend`, `Google Cloud NLP`, `Azure Text Analytics`) and fast pre-packaged local pipelines (`spaCy v2.0`, released `2017-11`).
* **Split Steps:** Neural NLP split sharply into two separate complexity tiers based on context sensitivity and hardware requirements:
  * **Step 2 (Static Vectors + Task RNNs):** Kept lightweight static embeddings (`Word2Vec`, `GloVe`, `fastText`) paired with task-specific recurrent or convolutional layers (`BiLSTM-CRF`, 1D `CNN`) for high-throughput, low-latency single-document classification and tagging.
  * **Step 3 (Contextual Encoder Fine-Tuning):** Split upward to handle context-heavy reading comprehension (`SQuAD`), natural language inference (`MNLI`), and conversational search ranking using 110M–340M parameter `BERT` models on dedicated GPUs.
* **Combined or Gone Steps:** Hand-crafted linguistic parse trees, manual part-of-speech feature templates, and domain-specific lexicon tables merged into automated sub-word tokenizers (`WordPiece`, `SentencePiece`) and neural network layers, retiring manual feature engineering from competitive NLP benchmarks.

#### 3.1.3 Step-by-Step Breakdown (Steps 1 to 4)

**Four Complexity Tiers:** Profiles each step of Era 1 ($L_1$) from bottom to top using the five-part step framework, verified against the Two-of-Three Step Split Test.

---

##### Step 1: Rule Engines, Keyword Filters & Off-the-Shelf Cloud NLP APIs

* **Name & Rank:** **Step 1 (Lowest Complexity) — Rule Engines, Keyword Filters & Off-the-Shelf Cloud NLP APIs** (*62% User Share | 15% Compute Share | 28% Spending Share*).
* **Step Boundaries:**
  * **Entry Floor (Base Step):** Represents the entry rung of Era 1 text processing, requiring zero custom training data, zero neural network design, and zero GPU infrastructure.
  * **Ceiling vs. Step 2:** Limited to fixed pattern matching and generic pre-built categories (overall positive/negative sentiment, standard person/location/organization entities); moving to custom company-specific categories or noisy domain jargon requires training a Step 2 task network on labeled company records.
* **Concrete Tool Stack:** Python regular expressions (`re`), keyword search engines (`Elasticsearch` / Apache `Lucene` BM25), classical table-based classifiers (`scikit-learn` `TfidfVectorizer` + `LogisticRegression` / `SGDClassifier`, `NLTK`), fast pre-packaged industrial pipelines (`spaCy v2.0` `en_core_web_sm` CNN tagger), and managed cloud REST APIs (`AWS Comprehend` launched `2017-11`, `Google Cloud Natural Language API`, `IBM Watson Natural Language Understanding`, `Microsoft Azure Text Analytics`, `Dialogflow` intent trees).
* **Use Cases & Context Switching:**
  * **Who & Goal:** Software engineers, business analysts, and support teams extracting structured fields (dates, invoice numbers, names), filtering profanity, routing customer support tickets, and running basic sentiment dashboards.
  * **Courses & Surveys:** Taught as the baseline comparison in *Stanford CS224N* (2017–2018 Assignment 1 baseline) and *Fast.ai Machine Learning for Coders*; reflected in the *Stack Overflow Developer Survey (2019–2020)* where general data and tabular tools (`Pandas` at 12.7% in 2019 rising to 15.5% in 2020, and `scikit-learn` at ~8%–11%) reached $3\times$ more developers than deep learning libraries (`PyTorch` at 3.3%).
  * **News Wins & Cautionary Tales:** Following the **Microsoft Tay** chatbot failure (shut down in 16 hours after Twitter users taught its adaptive learning loop offensive speech), enterprise customer service teams across 2017–2020 locked commercial chatbots (`Dialogflow`, `IBM Watson`, bank support bots) into strict Step 1 decision trees and regex blocklists to guarantee safe, predictable replies. Meanwhile, **Google Duplex** (`2018-05`) demonstrated how combining narrow task networks with tightly scripted conversation state rules could book restaurant reservations by phone.
  * **Same-Engineer Context Switching:** A production ML engineer in 2019 used **Step 1** `re` regex and `spaCy` rules to strip HTML tags, emails, and phone numbers in milliseconds, switched to **Step 2** `GloVe` + `BiLSTM` when training a fast custom product-category tagger on 50,000 catalog items, and climbed to **Step 3** `BERT-Base` fine-tuning only when building a semantic question-answering search bar where word order and prepositions changed the answer.
* **Step Resource Use:**
  * **Single-Task Cost:** Processes **0 LLM tokens** (operates on raw character strings or 100-character billing units); executes $\sim 10^7\text{ to }10^8\text{ FLOPs}$ per document on a CPU or shared cloud accelerator; costs **$\$0.0001$ per 100-character unit** on `AWS Comprehend` ($\sim \$0.0003$ per 300-character minimum API request, or $<\$0.00001$ self-hosted on `spaCy`); consumes **$\sim 0.0005\text{ Wh}$** of electricity; requires **$\sim 5\text{ min}$** of human rule configuration or API wiring vs. **$<0.01\text{ min}$ ($<0.5\text{ s}$)** of machine execution per call.
  * **Industry-Wide Share:** Accounts for **62% of active users**, **50% of human engineering hours**, **15% of era AI compute**, and **28% of era spending** (driven by high-volume enterprise cloud API billing and developer integration hours).

---

##### Step 2: Static Word Vectors + Task-Specific Neural Networks (`Word2Vec`/`GloVe` + `BiLSTM`/`CNN`)

* **Name & Rank:** **Step 2 — Static Word Vectors + Task-Specific Neural Networks (`Word2Vec`/`GloVe` + `BiLSTM`/`CNN`)** (*23% User Share | 25% Compute Share | 30% Spending Share*).
* **Step Boundaries:**
  * **Difference vs. Step 1:** Replaces rigid keyword matching and generic cloud APIs with a custom-trained neural network initialized with pretrained 100-to-300-dimensional static word vectors (`Word2Vec`, `GloVe`), capturing synonym similarity (grouping *"couch"* and *"sofa"* together) and learning custom company labels from 10,000–100,000 labeled training rows.
  * **Ceiling vs. Step 3:** Assigns a single fixed vector to each word regardless of surrounding context and processes words sequentially through recurrent gates (`LSTM`/`GRU`), losing track of long-range dependencies beyond ~50–100 words and failing on subtle multi-sentence reading comprehension that requires Step 3 `BERT` self-attention.
* **Concrete Tool Stack:** Pretrained static word vector tables (Google `Word2Vec` 300d, Stanford `GloVe` 6B/840B, Facebook `fastText` subword vectors), deep learning frameworks (`TensorFlow 1.x`, `Keras`, early `PyTorch 0.4/1.0`, `AllenNLP`), sequential and convolutional architectures (bidirectional long short-term memory networks [`BiLSTM`], `BiLSTM-CRF` sequence taggers, Kim 2014 1D text `CNN`), and single-GPU cloud instances (`AWS EC2 p2.xlarge` Nvidia `K80` or `p3.2xlarge` Nvidia `V100`).
* **Use Cases & Context Switching:**
  * **Who & Goal:** Applied ML engineers and data scientists building custom document classifiers, e-commerce product categorizers, clinical named-entity extractors (`BiLSTM-CRF`), and toxic-comment filters.
  * **Courses & Surveys:** Formed the core curriculum of *Stanford CS224N (2017–2018)* — where students coded `Word2Vec` skip-gram gradients in `NumPy`, built neural dependency parsers, and trained recurrent sequence models — and *Fast.ai Practical Deep Learning for Coders v1 (2017)*. In the *Stack Overflow Developer Survey (2019)*, `TensorFlow` reached **10.3%** of all respondents while `Torch/PyTorch` reached **3.3%** (ranking among the "Most Loved" frameworks as researchers migrated from `Keras`/`TensorFlow 1.x` graph sessions to `PyTorch` dynamic execution).
  * **News Wins & Cautionary Tales:** In **October 2018**, Reuters broke the story that **Amazon scrapped its internal AI recruiting tool** after discovering that the custom resume-ranking model — trained on 10 years of historical resumes submitted mostly by men — learned to penalize resumes containing the word *"women's"* (as in *"women's chess club captain"*) and downgraded graduates of two all-women's colleges, illustrating how task-specific models trained from scratch on historical company data amplify embedded bias.
  * **Same-Engineer Context Switching:** An ML engineer at a media or retail company used **Step 1** keyword filters for instant spam blocking, trained a **Step 2** `GloVe` + `BiLSTM` classifier when they needed 2-millisecond CPU/GPU inference across millions of daily product reviews, and moved to **Step 3** `BERT` fine-tuning when high-value legal or medical contract review demanded deep contextual accuracy over raw speed.
* **Step Resource Use:**
  * **Single-Task Cost:** Processes **0 generative LLM tokens** ($\sim 100\text{–}500$ word vectors per document); requires **$\sim 10^{15}\text{ FLOPs}$** for a multi-epoch training run on 50,000 documents ($\sim 10^9\text{ FLOPs}$ per single inference pass); costs **$\$5\text{ to }\$50$** in cloud GPU time per training run ($\sim \$0.00001$ per inference query); consumes **$\sim 30\text{ Wh}$** per training run ($\sim 0.001\text{ Wh}$ per inference pass); requires **$\sim 480\text{ min}$ ($8\text{ hr}$)** of human data cleaning, vocabulary tokenization, and hyperparameter tuning vs. **$\sim 20\text{ min}$** of GPU training runtime.
  * **Industry-Wide Share:** Accounts for **23% of active users**, **30% of human engineering hours**, **25% of era AI compute**, and **30% of era spending**.

---

##### Step 3: Pretrained Language Encoder Fine-Tuning (`ULMFiT`, `BERT`, `RoBERTa`, `HuggingFace`)

* **Name & Rank:** **Step 3 — Pretrained Language Encoder Fine-Tuning (`ULMFiT`, `BERT`, `RoBERTa`, `HuggingFace` + early `GPT-2` continuation)** (*13% User Share | 40% Compute Share | 27% Spending Share*).
* **Step Boundaries:**
  * **Difference vs. Step 2:** Replaces static word lookups and from-scratch recurrent layers with a deep 12-to-24-layer bidirectional Transformer encoder (`BERT-Base` 110M parameters, `BERT-Large` 340M parameters, `RoBERTa`) pretrained on billions of words, updating all weights for 2–4 passes (epochs) over a small labeled dataset (1,000–20,000 rows) to achieve state-of-the-art reading comprehension, entity extraction, and semantic ranking.
  * **Ceiling vs. Step 4:** Relies on existing public pretrained checkpoints capped at a 512-subword context window and requires a task-specific labeled dataset and gradient weight updates for every new task; building a brand-new architecture, pretraining on terabytes of proprietary domain text from scratch, or training multi-agent reinforcement learning systems requires climbing to Step 4.
* **Concrete Tool Stack:** Pretrained checkpoints (`ULMFiT` AWD-LSTM, Google `BERT-Base`/`Large`, Facebook `RoBERTa`, `DistilBERT`, Google `ALBERT`, `XLNet`, OpenAI `GPT-1`/`GPT-2` 117M–1.5B), model hub and training libraries (HuggingFace `pytorch-transformers` $\to$ `transformers` v2, `fastai` v1/v2 `text_classifier_learner`, Google `TensorFlow` `bert` repo), subword tokenizers (`WordPiece`, byte-level `BPE`), and cloud GPU workstations (`AWS p3.2xlarge` / `p3.8xlarge` with 1–4 Nvidia `V100` 16GB GPUs, `Google Colab` free `K80`/`T4` GPUs, `Kaggle Kernels`).
* **Use Cases & Context Switching:**
  * **Who & Goal:** NLP engineers, search-ranking teams, Kaggle competitors, and applied researchers building semantic search engines, extractive question-answering systems (`SQuAD` style), contract clause extractors, and early creative text-continuation apps.
  * **Courses & Surveys:** Anchored the **2018–2019 syllabus overhaul** across the field: *Fast.ai Lesson 4 (2018–2019)* taught 3-stage `ULMFiT` transfer learning on IMDB movie reviews, while Professor Chris Manning's *Stanford CS224N (Winter 2019 & 2020)* replaced RNN sequence dominance with self-attention, `BERT` contextual embeddings, and subword tokenization, and students completed final projects by fine-tuning `BERT` on `SQuAD 2.0`. *GitHub Octoverse (2018–2019)* ranked `PyTorch` and HuggingFace `transformers` among the fastest-growing open-source projects globally, while the *State of AI Report (2019)* documented `PyTorch` overtaking `TensorFlow` at major AI conferences (69% of CVPR/NAACL/ACL papers).
  * **News Wins & Cautionary Tales:** In **October 2019**, Google Fellow and VP of Search **Pandu Nayak** announced that Google integrated **BERT into Google Search** for **10% of all US English queries** (and featured snippets globally), calling it the biggest leap forward in search quality in five years because `BERT` understood how prepositions like *"to"* and *"for"* altered query intent (such as *"2019 brazil traveler to usa need visa"*). On the generative side, OpenAI made headlines in **February 2019** with its **staged release of `GPT-2` (1.5B)** — initially withholding the full weights due to fears of automated fake news before releasing the full model in November 2019, which college student Nick Walton fine-tuned on choose-your-own-adventure stories to launch **AI Dungeon** (`2019-12`).
  * **Same-Engineer Context Switching:** A search engineer at a tech company used **Step 1** `Elasticsearch` BM25 to retrieve the top 1,000 candidate web pages in 10 milliseconds, used a **Step 2** lightweight neural vector model to filter down to 100 candidates, and ran a **Step 3** fine-tuned `BERT` cross-encoder over the top 20 passages to rank the exact answer snippet shown to the user.
* **Step Resource Use:**
  * **Single-Task Cost:** Processes up to **$512$ subword tokens per query** ($\sim 3.8 \times 10^6$ subword tokens across a 3-epoch fine-tuning run on 10,000 examples); executes **$\sim 2.5 \times 10^{15}\text{ to }10^{17}\text{ FLOPs}$** per fine-tuning job ($\sim 1.1 \times 10^{11}\text{ FLOPs}$ per 512-token single inference pass on `BERT-Base`, $2 \times 1.1 \times 10^8 \times 512$); costs **$\$1.50\text{ to }\$200$** per cloud GPU fine-tuning run ($\sim \$0.00005$ per inference pass); consumes **$\sim 60\text{ to }500\text{ Wh}$** for fine-tuning ($\sim 0.005\text{ Wh}$ per query on an Nvidia `V100` at $\sim 5 \times 10^{10}\text{ FLOPs/J}$); requires **$\sim 240\text{ min}$ ($4\text{ hr}$)** of human dataset curation and training script setup vs. **$\sim 15\text{ to }90\text{ min}$** of GPU fine-tuning ($\sim 0.002\text{ min}$ per single query).
  * **Industry-Wide Share:** Accounts for **13% of active users**, **16% of human engineering hours**, **40% of era AI compute** (driven by heavy GPU fine-tuning and high-volume `BERT` search inference across billions of daily web queries), and **27% of era spending**.

---

##### Step 4: Custom From-Scratch Sequence & Deep RL Systems

* **Name & Rank:** **Step 4 (Highest Complexity) — Custom From-Scratch Sequence & Deep RL Systems** (*2% User Share | 20% Compute Share | 15% Spending Share*).
* **Step Boundaries:**
  * **Difference vs. Step 3:** Moves beyond fine-tuning existing public checkpoints on a single GPU to pretraining brand-new foundation encoders or encoder-decoder translation architectures from scratch across 8 to 1,024+ GPUs/TPUs on terabytes of text (`BioBERT`, `RoBERTa`, `T5`, production neural machine translation) or running distributed reinforcement learning across thousands of CPU/GPU workers (`OpenAI Five`, `AlphaStar`).
  * **Era Ceiling (Top Step of $L_1$):** Represents the maximum technical, financial, and cluster-orchestration ceiling of `2017-06` to `2020-05`, requiring distributed multi-node gradient synchronization, custom tokenizer construction, and $\$1,000\text{ to }\$160,000+$ compute budgets per training run.
* **Concrete Tool Stack:** Multi-node distributed training frameworks (Facebook `fairseq`, Google `tensor2tensor` and `mesh-tensorflow`, Uber `Horovod`, Nvidia `Megatron-LM` 2019, `OpenAI Rapid` distributed RL framework), mixed-precision math libraries (`Nvidia Apex` `FP16`), custom domain pretraining corpora (`PubMed` + `PMC` for `BioBERT`; `CommonCrawl` `C4` for `T5`; `BookCorpus` + `CC-News` for `RoBERTa`), and supercomputing clusters (Google `Cloud TPU v2/v3` 64–1,024 chip pods, Nvidia `DGX-1`/`DGX-2` clusters with `InfiniBand`).
* **Use Cases & Context Switching:**
  * **Who & Goal:** Frontier AI research labs (Google Brain, DeepMind, Facebook AI Research / FAIR, OpenAI, Allen Institute for AI / AI2) and specialized biomedical/global-translation teams pretraining domain foundation models (`BioBERT`, `ClinicalBERT`, `SciBERT`), training production neural machine translation engines (`Google Translate`, `DeepL`), and building superhuman game-playing RL systems.
  * **Courses & Reports:** Analyzed in OpenAI's landmark *"AI and Compute"* report (`2018-05` by Dario Amodei and Danny Hernandez), which documented a **$300,000\times$ increase in frontier training compute** from AlexNet (2012) to `AlphaGo Zero` (late 2017/2018) — doubling every 3.4 months and measured in **petaflop/s-days** ($1\text{ pfs-day} = 8.64 \times 10^{19}\text{ FLOPs}$). Tracked annually in the *Stanford HAI AI Index (2018–2020)* and *State of AI Reports (2018–2020)*.
  * **News Wins & Cautionary Tales:**
    * **Domain Pretraining Wins (`2019`):** Researchers at Korea University and Clova AI released **BioBERT** (`2019-01` / `Bioinformatics` `2019-09`), continuing pretraining from `BERT` on 4.5B words of `PubMed` abstracts and 13.5B words of `PMC` full-text articles across 8 Nvidia `V100` GPUs for 23 days to beat general `BERT` across biomedical entity recognition and medical question answering.
    * **Deep RL Milestones & Fragility (`2017–2019`):** DeepMind's **AlphaGo Zero / AlphaZero** (`2017-10`/`12`, $\sim 1.6 \times 10^{21}\text{ FLOPs}$) mastered Go, chess, and shogi via pure self-play; **OpenAI Five** (`2019-04`) defeated Dota 2 world champions OG after training across 256 `P100`/`V100` GPUs and 128,000 CPU cores for 10 months ($\sim 800\text{ pfs-days} \approx 6.9 \times 10^{22}\text{ FLOPs}$); and DeepMind's **AlphaStar** (`2019-10`, Nature) reached Grandmaster level in *StarCraft II*. However, when OpenAI opened `OpenAI Five` to public online play in April 2019, amateur human teams discovered unconventional unit strategies that exploited the agent's fixed training assumptions — demonstrating that massive Step 4 RL systems remained brittle outside their exact simulation rules.
  * **Same-Engineer Context Switching:** A research scientist at a biomedical institute or global tech lab used **Step 3** off-the-shelf `BERT-Base` fine-tuning to test whether a new clinical labeling dataset had clean signal in a single afternoon, then escalated to a **Step 4** multi-week, 8-to-64-GPU domain pretraining run (`BioBERT` or custom `fairseq` encoder-decoder) only when specialized medical abbreviations or low-resource languages caused standard checkpoints to plateau.
* **Step Resource Use:**
  * **Single-Task Cost:** Processes **billions to trillions of pretraining tokens** ($\sim 3.3 \times 10^9$ words for `BERT`, $\sim 1.8 \times 10^{10}$ words for `BioBERT`, or 45,000 years of simulated game play for `OpenAI Five`); executes **$\sim 10^{19}\text{ to }10^{21}\text{ FLOPs}$** per pretraining run ($\sim 3.3 \times 10^{18}\text{ FLOPs}$ for 2017 base `Transformer`, $1.9 \times 10^{20}\text{ FLOPs}$ for `BERT-Large`, $4.0 \times 10^{21}\text{ FLOPs}$ for `RoBERTa-Large`); costs **$\$1,000\text{ to }\$160,000+$** in cloud compute per language pretraining run (up to $\$1\text{M}+$ for multi-month deep RL clusters); consumes **$\sim 100,000\text{ to }5,000,000\text{ Wh}$ ($0.1\text{ to }5.0\text{ MWh}$)** per training run; requires **$\sim 12,000\text{ min}$ ($200+\text{ hr}$)** of specialist distributed-systems engineering vs. **$\sim 4,320\text{ to }43,200\text{ min}$ ($3\text{ to }30\text{ days}$)** of uninterrupted cluster runtime.
  * **Industry-Wide Share:** Accounts for **2% of active users**, **4% of human engineering hours**, **20% of era AI compute**, and **15% of era spending**.

#### 3.1.4 Era 1 Full-Ladder Resource Totals

**Era 1 Aggregate Scale (`2017-06` to `2020-05`):** Summing across all four steps over the 36-month valid window reveals an industry transitioning from CPU rule processing to first-generation GPU/TPU transfer learning, with total resource consumption several orders of magnitude below the post-2022 LLM era.

* **Total Compute ($\sim 1.5 \times 10^{23}\text{ FLOPs}$):** Combined training and inference compute across all four NLP and sequence steps over the 3-year window totaled roughly **$1.5 \times 10^{23}\text{ FLOPs}$** ($\sim 5 \times 10^{22}\text{ FLOPs/year}$) — driven by Step 3 `BERT` search inference across billions of Google and enterprise queries (40% share, $\sim 6.0 \times 10^{22}\text{ FLOPs}$), Step 2 custom `BiLSTM`/`CNN` training and production tagging (25% share, $\sim 3.8 \times 10^{22}\text{ FLOPs}$), Step 4 frontier pretraining and deep RL runs (20% share, $\sim 3.0 \times 10^{22}\text{ FLOPs}$), and Step 1 cloud NLP APIs and local `spaCy` pipelines (15% share, $\sim 2.2 \times 10^{22}\text{ FLOPs}$). Notice that the entire 3-year compute of Era 1 ($\sim 1.5 \times 10^{23}\text{ FLOPs}$) was half the compute of the single `GPT-3 175B` training run ($3.14 \times 10^{23}\text{ FLOPs}$) that opened Era 2 in `2020-06`.
* **Total Electricity ($\sim 0.95\text{ TWh}$ / $950,000\text{ MWh}$):** At era cluster efficiency ($\eta_{\text{2018}} \approx 5 \times 10^{10}\text{ FLOPs/Joule}$ across Nvidia `K80`/`P100`/`V100` GPUs and CPU servers with datacenter cooling overhead $\text{PUE} \approx 1.25$), full-ladder NLP and sequence workloads consumed approximately **$950,000\text{ MWh}$ ($0.95\text{ TWh}$)** over 36 months ($\sim 315,000\text{ MWh/year}$).
* **Total Spending ($\sim \$2.8\text{ Billion USD}$):** Cumulative enterprise and research expenditure across cloud NLP APIs (`AWS Comprehend`, `Google Cloud NLP`), cloud GPU compute (`AWS EC2 P2/P3`, `GCP TPU`), and dedicated NLP compute infrastructure totaled approximately **$\$2.8\text{B}$** over the 3-year window ($\sim \$0.93\text{B/year}$), split across Step 1 APIs and rule pipelines (28%, $\$780\text{M}$), Step 2 custom neural models (30%, $\$840\text{M}$), Step 3 `BERT` fine-tuning and inference clusters (27%, $\$760\text{M}$), and Step 4 frontier pretraining and RL clusters (15%, $\$420\text{M}$).
* **Total Token & Query Volume ($\sim 4.5 \times 10^{12}$ Subword Tokens Equivalent):** Commercial generative API token billing was not yet invented in Era 1; measured in equivalent subword/word units processed across Step 3 `BERT` search/classification inference and Step 4 pretraining runs, global volume totaled approximately **$4.5 \times 10^{12}$ subword tokens** ($4.5\text{ trillion}$ tokens across 36 months, or $\sim 1.5\text{T tokens/year}$) alongside $\sim 1.2 \times 10^{12}$ Step 1–2 API/document tagging calls.
* **Total Human Usage ($\sim 1.8\text{ Million Active Practitioners}$ | $\sim 540\text{ Million Human-Hours}$):** Active usage was concentrated entirely among software engineers, data scientists, and ML researchers (**$\sim 1.8\text{M}$ practitioners globally**, aligned with the 10.3% `TensorFlow` and 3.3% `PyTorch` shares among ~20M global developers in the *2019 Stack Overflow Survey*), who logged roughly **$540\text{M}$ cumulative engineering hours** cleaning datasets, writing regex/spaCy pipelines, and tuning neural network training scripts.

| Step Rank & Name | Task Complexity Scope | Primary Era 1 Tool Stack | Single-Task Compute & Energy | Single-Task Cost & Time (Human vs. AI) | User Share % | Human-Hours Share % | Compute Share % | Spend Share % | Cross-Era Link into Era 2 ($L_2$: `2020-06`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Step 1:** Rule Engines & Cloud NLP APIs | Single sentence / entity tag / sentiment call | `Regex`, `spaCy v2.0`, `scikit-learn`, `AWS Comprehend`, `Google Cloud NLP` | $\sim 10^8\text{ FLOPs}$ / $0.0005\text{ Wh}$ ($0\text{ LLM tokens}$) | $\$0.0001\text{–}\$0.0003$ / $5\text{ min}$ human setup vs. $<0.01\text{ min}$ AI | 62% | 50% | 15% | 28% | **Sinks / Evolves** into $L_2$ Step 1 inline autocomplete & templates |
| **Step 2:** Static Word Vectors + Task RNNs/CNNs | Single document classification / custom NER | `Word2Vec`, `GloVe`, `fastText` + `BiLSTM-CRF` / `CNN` (`Keras`, `PyTorch`) | $\sim 10^{15}\text{ FLOPs}$ train ($10^9$ infer) / $30\text{ Wh}$ train | $\$5\text{–}\$50$ train run / $480\text{ min}$ human vs. $20\text{ min}$ GPU | 23% | 30% | 25% | 30% | **Combined / Gone** — replaced by `BERT` encoders & `GPT-3` prompting |
| **Step 3:** Pretrained Encoder Fine-Tuning (`BERT`) | Multi-sentence Q&A, NLI, search ranking (512 subwords) | `ULMFiT`, `BERT`, `RoBERTa`, `GPT-2`, `HuggingFace transformers`, `fastai` | $\sim 10^{16}\text{–}10^{17}\text{ FLOPs}$ train ($10^{11}$ infer) / $60\text{–}500\text{ Wh}$ | $\$20\text{–}\$200$ train run / $240\text{ min}$ human vs. $45\text{ min}$ GPU | 13% | 16% | 40% | 27% | **Evolves & Combines** with Step 4 into $L_2$ Step 4 production fine-tuning |
| **Step 4:** From-Scratch Sequence & Deep RL Systems | Domain foundation pretraining / full NMT / game RL | `fairseq`, `tensor2tensor`, `BioBERT`, `OpenAI Five`, `AlphaStar` (`TPU`/`V100` pods) | $\sim 10^{19}\text{–}10^{21}\text{ FLOPs}$ train / $0.1\text{–}5.0\text{ MWh}$ | $\$1\text{k}\text{–}\$160\text{k}+$ run / $12,000\text{ min}$ human vs. $14,400\text{ min}$ cluster | 2% | 4% | 20% | 15% | **Combines** into $L_2$ Step 4 custom training while birthing `GPT-3` API |
| **Era 1 Total ($L_1$)** | **All 4 Steps (`2017-06` to `2020-05`, 36 mos)** | **CPU Rules $\to$ `V100`/`TPU` Transfer Learning** | **$\sim 1.5 \times 10^{23}\text{ FLOPs}$ Total / $\sim 950,000\text{ MWh}$** | **$\sim \$2.8\text{B}$ Total Spend / $\sim 540\text{M}$ Human-Hours** | **100%** ($\sim 1.8\text{M}$ devs) | **100%** ($\sim 540\text{M}$ hrs) | **100%** ($1.5 \times 10^{23}$ FLOPs) | **100%** ($\$2.8\text{B}$) | **Opens Era 2 ($L_2$) on `2020-06` (`GPT-3` API)** |

```json
{
  "era_id": "L1",
  "era_name": "Pre-LLM & Transfer-Learning NLP Ladder (The Fine-Tuned Encoder Era)",
  "valid_start": "2017-06",
  "valid_end": "2020-05",
  "duration_months": 36,
  "era_totals": {
    "total_compute_flops": 1.5e23,
    "total_electricity_mwh": 950000,
    "total_spending_usd": 2800000000,
    "total_subword_tokens_equivalent": 4.5e12,
    "total_active_practitioners": 1800000,
    "total_human_hours": 540000000
  },
  "steps": [
    {
      "step_rank": 1,
      "step_id": "L1_S1",
      "step_name": "Rule Engines, Keyword Filters & Off-the-Shelf Cloud NLP APIs",
      "task_complexity_scope": "Single sentence / tag extraction / sentiment polarity",
      "tool_stack": [
        "Python re (Regex)",
        "Elasticsearch BM25",
        "scikit-learn TfidfVectorizer",
        "spaCy v2.0",
        "AWS Comprehend",
        "Google Cloud Natural Language API",
        "Dialogflow"
      ],
      "single_task_metrics": {
        "tokens_per_task": 0,
        "subword_units_per_query": 50,
        "compute_flops_per_task": 1.0e8,
        "electricity_wh_per_task": 0.0005,
        "cost_usd_per_task": 0.0001,
        "cost_usd_range": [0.00001, 0.0003],
        "human_minutes_per_task": 5.0,
        "ai_runtime_minutes_per_task": 0.005
      },
      "industry_wide_shares": {
        "user_share_pct": 62.0,
        "human_hours_share_pct": 50.0,
        "compute_share_pct": 15.0,
        "spending_share_pct": 28.0
      },
      "cross_era_link_from_prev": "Old Step Sinking into Default UI (Pre-2017 bespoke statistical CRFs/SVMs sink into commodity cloud REST APIs and spaCy v2.0)",
      "cross_era_link_to_next": "Old Step Sinking into Default UI (Routine text/code assistance sinks into L2_S1 inline IDE ghost text and copywriting templates)"
    },
    {
      "step_rank": 2,
      "step_id": "L1_S2",
      "step_name": "Static Word Vectors + Task-Specific Neural Networks (Word2Vec/GloVe + BiLSTM/CNN)",
      "task_complexity_scope": "Single document classification / custom named-entity recognition (NER)",
      "tool_stack": [
        "Word2Vec",
        "GloVe",
        "fastText",
        "BiLSTM-CRF",
        "1D Text CNN",
        "TensorFlow 1.x / Keras",
        "PyTorch 0.4/1.0",
        "AllenNLP"
      ],
      "single_task_metrics": {
        "tokens_per_task": 0,
        "word_vectors_per_doc": 300,
        "compute_flops_train_run": 1.0e15,
        "compute_flops_per_inference": 1.0e9,
        "electricity_wh_train_run": 30.0,
        "electricity_wh_per_inference": 0.001,
        "cost_usd_train_run": 25.0,
        "cost_usd_range": [5.0, 50.0],
        "cost_usd_per_inference": 0.00001,
        "human_minutes_per_task": 480.0,
        "ai_runtime_minutes_per_task": 20.0
      },
      "industry_wide_shares": {
        "user_share_pct": 23.0,
        "human_hours_share_pct": 30.0,
        "compute_share_pct": 25.0,
        "spending_share_pct": 30.0
      },
      "cross_era_link_from_prev": "Split Step (Splits from neural NLP as lightweight static-vector sequence tier)",
      "cross_era_link_to_next": "Combined or Gone Step (Collapses in L2 as pretrained Transformer checkpoints and GPT-3 zero/few-shot completion replace static word vectors)"
    },
    {
      "step_rank": 3,
      "step_id": "L1_S3",
      "step_name": "Pretrained Language Encoder Fine-Tuning (ULMFiT, BERT, RoBERTa, HuggingFace)",
      "task_complexity_scope": "Multi-sentence reading comprehension (SQuAD), semantic search ranking, NLI, early GPT-2 text continuation",
      "tool_stack": [
        "ULMFiT (AWD-LSTM)",
        "BERT-Base / BERT-Large",
        "RoBERTa",
        "DistilBERT",
        "GPT-2 (117M-1.5B)",
        "HuggingFace pytorch-transformers / transformers",
        "fastai",
        "Nvidia V100 GPUs"
      ],
      "single_task_metrics": {
        "tokens_per_task": 512,
        "training_tokens_per_run": 3800000,
        "compute_flops_train_run": 5.0e16,
        "compute_flops_per_inference": 1.1e11,
        "electricity_wh_train_run": 200.0,
        "electricity_wh_per_inference": 0.005,
        "cost_usd_train_run": 50.0,
        "cost_usd_range": [20.0, 200.0],
        "cost_usd_per_inference": 0.00005,
        "human_minutes_per_task": 240.0,
        "ai_runtime_minutes_per_task": 45.0
      },
      "industry_wide_shares": {
        "user_share_pct": 13.0,
        "human_hours_share_pct": 16.0,
        "compute_share_pct": 40.0,
        "spending_share_pct": 27.0
      },
      "cross_era_link_from_prev": "New Breakthrough Step (Unlocked in 2018 by ULMFiT and BERT bidirectional masked language model pretraining)",
      "cross_era_link_to_next": "Evolved & Combined Step (Merges with L1_S4 into L2_S4 Task-Specific Encoder & Open-Model Fine-Tuning)"
    },
    {
      "step_rank": 4,
      "step_id": "L1_S4",
      "step_name": "Custom From-Scratch Sequence & Deep RL Systems",
      "task_complexity_scope": "Full neural machine translation (NMT) pipelines, domain foundation pretraining (BioBERT), and multi-agent game RL (OpenAI Five, AlphaStar)",
      "tool_stack": [
        "Facebook fairseq",
        "Google tensor2tensor",
        "BioBERT / SciBERT",
        "Megatron-LM",
        "OpenAI Rapid (OpenAI Five)",
        "DeepMind AlphaZero / AlphaStar",
        "Google Cloud TPU v2/v3 Pods",
        "Nvidia DGX V100 Clusters"
      ],
      "single_task_metrics": {
        "tokens_per_task": 3300000000,
        "compute_flops_train_run": 2.0e20,
        "compute_flops_range": [1.0e19, 4.0e21],
        "electricity_wh_train_run": 1200000.0,
        "cost_usd_train_run": 35000.0,
        "cost_usd_range": [1000.0, 160018.0],
        "human_minutes_per_task": 12000.0,
        "ai_runtime_minutes_per_task": 14400.0
      },
      "industry_wide_shares": {
        "user_share_pct": 2.0,
        "human_hours_share_pct": 4.0,
        "compute_share_pct": 20.0,
        "spending_share_pct": 15.0
      },
      "cross_era_link_from_prev": "New Top Step (Consolidates multi-GPU sequence pretraining and large-scale self-play RL)",
      "cross_era_link_to_next": "Combined & Split Step (Domain pretraining merges into L2_S4 while giant autoregressive pretraining births L2_S2 GPT-3 completion API)"
    }
  ]
}
```