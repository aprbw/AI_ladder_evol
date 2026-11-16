# Workspace Rules Part 2: Megachart Typography, Golden Ratio & Layout Conventions

## 1. Strict Golden Ratio Typography Hierarchy (`T=H0 -> H1 -> H2 -> H3 -> H4`)
All megacharts obey a strict 5-tier Golden Ratio ($\varphi = \frac{1 + \sqrt{5}}{2} \approx 1.61803398875$) font hierarchy without skipping levels:
$$\text{H}_{k-1} = \text{H}_{k} \times \varphi, \qquad \text{H}_{k+1} = \text{H}_{k} / \varphi$$

* **Standard A0 Landscape Megachart Scale (Anchored at `H2 = 24.00 pt` on `46.8 x 21.6 in` @ `300 DPI`)**:
  * **`T = H0 = H2 * φ² ≈ 62.83 pt`** (`22.17 mm`): Main Megachart Title (single line, top-left of masthead).
  * **`H1 = H2 * φ ≈ 38.83 pt`** (`13.70 mm`): Column Stage Short Names (`1. Silicon` .. `10. Swarms`), Row Organism / Level Short Names (`LLM`, `RAG`, `Multimodal`, `Embodied`, or `Level 1` .. `Level 6`), and Top-Left Corner Card Title.
  * **`H2 = 24.00 pt`** (`8.47 mm`): Cell Zone-1 Top Category Banner, Masthead Subtitle (`www.arianprabowo.com · ...`), and Corner Card Subtitle.
  * **`H3 = H2 / φ ≈ 14.83 pt`** (`5.23 mm`): Cell Zone-2 Core Mechanism Bars (`2` per cell) and Masthead Reading Guide (`① ... ② ... ③ ...`).
  * **`H4 = H3 / φ ≈ 9.17 pt`** (`3.23 mm`): Stage & Organism Full Names (`<= 10 words`), Cell Zone-3 `⚙ SUB-CATEGORY ▸ PRODUCTS & OSS` (`3x2` pairs + header bar), Cell Zone-4 `⚠ ANTI-PATTERNS & TRAPS` (`2x2` items + header bar), Column/Row metadata bullets, and Masthead Footnote Strip.
* **Uniformity Within Every Tier**:
  * Every element in the same semantic tier across the entire chart MUST use the exact same font size.
  * **Never shrink a single header or cell's font size to force long text to fit.** Instead, tighten the wording so all peers stay at the exact same `H_k` size.

## 2. Aspect Ratio & Dual-Resolution (`Mega` + `Mobile/Mini`) Deliverables
1. **Preserve the `19.5:9` Smartphone Landscape Aspect Ratio (`width / height = 2.1667`)**:
   * **Desktop / A0 Print Megachart**: `46.8 x 21.6 inches` @ `300 DPI` (`14040 x 6480 px`, where `46.8 in = 1188.7 mm ≈ 1189 mm` ISO A0 width) exported as both `.png` and searchable vector `.pdf`.
   * **Mobile Companion Chart**: `26.0 x 12.0 inches` @ `300 DPI` (exact `19.5:9` aspect ratio, with all `H0..H4` font sizes scaled proportionally by `26.0 / 46.8 = 5/9`), or `9:19.5` portrait when specifically designed for vertical phone scrolling (`fig_v5_current_gen_self_diagnosis_mobile.png`).
   * **Do not alter the aspect ratio** when updating font sizes or cell layouts unless explicitly requested.
2. **Role of `Mini` vs. `Mega` Charts**:
   * `Mini` / `Mobile` charts must be legible on a mobile screen without zooming in (or present a curated subset of the `Mega` chart's keywords/events while preserving the macro visual hierarchy).

## 3. Masthead & Header Banner Conventions
1. **Masthead Structure**:
   * **Top-Left**: Single-line `T = H0` Title (`AI SKILL TREE 2026`, `ANATOMY OF AI AGENTS 2026`, `AI LADDER EVOL`) + `www.arianprabowo.com` subtitle in `H2` (or top-right `H1` on timeline charts).
   * **Top-Right**: Structured Reading Guide in `H3` (`① COLUMNS ... ② ROWS ... ③ CELL ANATOMY ...`).
   * **Bottom Footnote Strip (`H4`, muted grey `#94A3B8`)**: Keep the motivating hook separate from the scope disclaimer. Place the scope definition (e.g., what "AI" means in this chart), temporal validity note, cross-reference to companion charts by Arian Prabowo, primary academic citation, and exact local timestamp (`Updated: YYYY-MM-DD HH:MM:SS TZ (UTC+XX:XX)`) in the bottom footnote strip.
2. **Column & Row Header Rules**:
   * **Numbered Short Names (`<= 2 words`, `H1`)**: Format stage headers as `1. Silicon`, `2. Python`, `3. Data`, etc. Never write `"Layer 1. Silicon"` or `"CAT:"`.
   * **Full Names (`<= 10 words`, `H4`)**: Place the descriptive full name (`<= 10 words`) directly beneath the `H1` short name inside the header banner.
   * **No Column Progress Bars**: Do not draw segmented progress bars at the top of column headers.
   * **No Redundant Axis / Cell Labels**: Omit axis titles when the ticks make the axis obvious (e.g., chronological years), omit `GxLx` coordinates inside cells when row/column headers already specify them, and do not repeat metadata in column headers if it already appears in the trapezoid bridge below.

## 4. Cell Design: Strict Separation of Brand-Agnostic Categories vs. Product Names
1. **Never mix brand-agnostic concepts with concrete product/vendor names in the same visual tier**:
   * **Zone 1 (`H2` Top Banner)**: 100% **Brand-Agnostic Functional Category** (`<= 18 chars`, zero brand names, e.g., `Tensor Compute`, `Serving Runtime`, `Instruction Tuning`, `Observe-Act Loop`).
   * **Zone 2 (`H3` Concept Bars)**: 2 **Brand-Agnostic Core Mechanisms / Algorithms** (zero brand names, e.g., `Deterministic Lockfiles`, `Paged KV & Graph Capture`).
   * **Zone 3 (`H4` Framed `⚙ SUB-CATEGORY ▸ PRODUCTS & OSS` Sub-Box)**: A framed box with header bar `⚙ SUB-CATEGORY ▸ PRODUCTS & OSS` and a `3x2` grid where every cell pairs **Line 1: `BRAND-AGNOSTIC SUB-CATEGORY:`** (muted slate `#64748B`) with **Line 2: `Concrete Product Names`** (bold organism accent).
   * **Zone 4 (`H4` Framed `⚠ ANTI-PATTERNS & TRAPS` Sub-Box)**: A dashed red sub-box at the bottom of every cell with header bar `⚠ ANTI-PATTERNS & TRAPS` and a `2x2` grid of `✕` failure modes.

## 5. Programmatic Pixel Bounding-Box Verification (`get_window_extent`)
Before finalizing any chart render:
1. Measure every rendered text artist with `t.get_window_extent(renderer=r)` against its container patch's `ax.get_window_extent(renderer=r)` in Matplotlib pixel coordinates.
2. Verify **zero horizontal or vertical overflows** across 100% of cells and headers.
3. Visually inspect the saved `.png` using `read_file` to confirm alignment, whitespace balance, and legibility.
