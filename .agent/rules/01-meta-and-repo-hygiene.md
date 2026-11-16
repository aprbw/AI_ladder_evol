# Workspace Rules Part 1: Meta-Principles, Design Philosophy & Repository Hygiene

## 1. Induce General Principles from Few-Shot Corrections (Never Just Hot-Fix)
Whenever the user gives concrete examples, critiques, or corrections:
1. **Infer the general principle**: Treat the user's examples as few-shot demonstrations of a deeper aesthetic, structural, or taxonomic rule.
2. **Apply globally**: Audit and update all cells, columns, rows, figures, and markdown tables across the entire deliverable so the rule holds universally, not only on the cited example.
3. **Fix at the design level**: If an output has recurring flaws, fix the underlying data schema, layout math, or megaprompt specification rather than patching isolated strings or leaving "scar tissue" commentary in reports.
4. **Persist the rule**: Record new or refined user preferences in `.agent/rules/` so future sessions on any machine inherit them automatically.

## 2. Repository Hygiene & Directory Boundaries
1. **Stay strictly inside the project workspace**: Never create or modify files outside the repository root unless explicitly instructed.
2. **Keep the repository root clean**:
   * The top-level root is strictly reserved for the published flagship artifacts (`AI_skill_tree_2026.png`, `AI_skill_tree_2026.pdf`, `README.md`, `LICENSE`, `.gitignore`, `.licenses/`, and hidden config folders like `.git/`, `.venv/`, `.agent/`).
   * Place all development scripts, intermediate reports, megaprompts (`mp*.md`), data caches, and sub-projects inside `dev/`.
3. **Self-contained sub-project folders**:
   * Keep all files for `Anatomy of AI Agents 2026` (including `plot_agent_anatomy_2026.py`, `.png`, `.pdf`, `_mobile.png`, and the companion `.md`) inside `dev/anatomy_of_AI_agents_2026/`.

## 3. First-Principles Design & Adversarial Red-Teaming
1. **Do not blindly inherit layouts across different chart types**:
   * Before designing a new chart or cell layout, analyze what the reader needs to distinguish at a glance.
   * Example lesson learned: Inheriting the floating 3-pill + unlabelled 6-bullet layout from `AI Skill Tree 2026` into `Anatomy of AI Agents 2026` blurred brand-agnostic categories with product names. Rethinking the cell from first principles produced the 4-zone anatomical cell (`H2` Brand-Agnostic Category Banner -> `H3` Brand-Agnostic Mechanisms -> `H4` Framed `⚙ SUB-CATEGORY ▸ PRODUCTS & OSS` Box -> `H4` Framed `⚠ ANTI-PATTERNS & TRAPS` Box).
2. **Literature-first inductive taxonomies**:
   * Never invent stage names, level names, or taxonomies up front from intuition alone. Survey canonical literature and production ecosystems first (e.g., `arXiv:2606.24937` for agentic architecture, existing industry AI ladders for `AI Ladder Evolution`), then distill the shortest canonical names.
   * When building ranked milestone or keyword pools, audit at least `2x` the candidate pool that appears on the final chart.
3. **Multi-persona red-teaming**:
   * Red-team both visual layout and content completeness from diverse viewpoints: systems engineers, ML researchers, everyday consumers, safety/alignment researchers, historians, enterprise architects, and non-US / Global South perspectives.
   * Always include real-world failure modes, anti-patterns, security exploits (e.g., RCE, prompt injection, MCP rug-pulls, supply-chain poisoning), and societal/cognitive traps (e.g., hallucinations, AI slop, sycophancy, reward hacking, overthinking token burn) alongside capabilities.

## 4. Authentic Visuals & Licensing Integrity
1. **Never use AI-generated or synthetic placeholder images for historical events**: Always use authentic archival photos, paper figures, hardware die/rack photos, or official UI captures tied directly to the milestone.
2. **Preserve aspect ratio (crop, never stretch)**: Zooming in and cropping to the focal subject of a figure or portrait is encouraged; stretching or squishing an image (`resize` with mismatched aspect ratio) is strictly forbidden.
3. **Track provenance**: Prefer Public Domain, CC0, and permissive Wikimedia Commons / arXiv figures, and document attributions in `.licenses/` and chart mastheads for Reddit and public distribution safety.
