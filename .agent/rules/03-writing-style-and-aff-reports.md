# Workspace Rules Part 3: Writing Style, Nomenclature & Report Formatting

## 1. Zero Em-Dash Rule (Forbidden Everywhere)
Never use an em dash (`U+2014`), horizontal bar (`U+2015`), HTML `&mdash;` entity, or double-hyphen prose substitute anywhere in chart titles, subtitles, cell text, legends, markdown reports, code comments, CSV files, or chat responses:
* Use a **colon (`:`)** or **semicolon (`;`)** to introduce a list, subtitle, or summary clause.
* Use **middle dots (`·`)** or **slashes (`/`)** inside compact chart cells and pill labels.
* Use **commas (`,`)** or **parentheses `(...)`** for appositives and technical clarifications.
* Use a **period (`.`)** to split independent clauses into crisp sentences.

## 2. Plain English + Parenthetical Jargon (`plain (jargon)`)
1. **Default to direct, objective plain English**: Write so an intelligent general technical reader understands the claim immediately.
2. **Parenthetical technical precision**: When a specialized technical term or acronym increases precision, write the plain-English phrase first followed immediately by the technical term in parentheses: `plain English explanation (technical jargon)`.
3. **Positive instruction framing**: In megaprompts (`mp*.md`), contracts, and documentation, state positively *what to do* and *what the target state looks like* rather than chaining negative `"do not..."` clauses.
4. **Descriptive, not normative**: Frame AI usage ladders and historical taxonomies descriptively (how practitioners and systems actually operate empirically) rather than normatively (prescribing how people "should" use AI).

## 3. Nomenclature & Word-Count Constraints
1. **Stage & Organism Headers (`Anatomy of AI Agents 2026`)**:
   * **Short Name (`H1`)**: Maximum `2` words (`1. Silicon`, `2. Python`, `3. Data`, `4. Pre-Train`, `5. SFT`, `6. Post-Train`, `7. Test-Time`, `8. Context`, `9. Harness`, `10. Swarms`; `LLM`, `RAG`, `Multimodal`, `Embodied`).
   * **Full Name (`H4`)**: Maximum `10` words.
   * **No `OSI` or `PDU` terminology**: The OSI model was only an internal conceptual analogy for the user's initial prompt. Never write `OSI`, `PDU`, or `Layer X` on the chart, in the code, or in the companion markdown.
2. **Timeline & Ladder Node Titles**:
   * When a node/card carries a separate body description (`H0`, `H1`, `H2` on timelines, or `AI Ladder Evolution` cells), keep the title ultra-terse (`< 6` words), stripping announcement verbs (`"Launches"`, `"Releases"`), redundant nouns (`"Paper"`, `"Dataset"`), and brand names where a brand-agnostic category belongs (`"Vibe Coding"`, not `"Copilot"`).
   * When a compact node has no body description (`H3`, `H4` on timelines), use a self-contained micro-sentence (`6-12` words, `< 13` words) stating `Subject + Active Verb + Object / Significance`.

## 4. Markdown Reports: Arian Fractal Format (AFF) & Visual Frontispieces
1. **Visual Frontispieces at Line 1**:
   * Every companion Markdown report must open at the very top of the file with its rendered visual megacharts (`![...](...)`) before the `# H1` title.
   * When both a `mini` and `mega` chart exist for the same narrative report (`AI Ladder Evolution`), display the `mini` overview chart first, followed immediately by the full `mega` chart.
2. **Arian Fractal Format (AFF) & Recursive Information Headers (RIH)**:
   * Prefix sections and bullet points with ultra-terse bold **Recursive Information Headers (RIH)** (`~3 words`, e.g., **Descriptive, not normative:**) that summarize the block before expanding into detail.
   * Include an **Extended Executive Summary (`Part I`)** comprising roughly `5%` (`~2,500 words` on full research reports) of the total report length.
   * Provide a **clickable Table of Contents** at the top of the report and a **part-level clickable Table of Contents (up to Level 4, numbered `2.1.1.1`)** at the start of every major Part.
   * Be liberal with visualizations and structured markdown tables (ideally at least one visualization or synthesis table per `H3` section, plus a visual abstract at the start of every Part).
