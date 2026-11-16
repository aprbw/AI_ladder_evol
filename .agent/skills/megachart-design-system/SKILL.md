---
name: megachart-design-system
description: >-
  Arian Prabowo's canonical Encyclopedic Megachart Design System (combining CITRA, Golden Ratio
  typography, A0/Mobile 19.5:9 canvas geometry, Masthead & Caption archetypes, and Matplotlib
  renderer pixel-collision verification). Activate when designing a new megachart or auditing
  visual layout, font scaling, or text bounding boxes.
---

# Encyclopedic Megachart Design System (`CITRA + Golden Ratio`)

## 1. Core Philosophy of an Encyclopedic Megachart
An **Encyclopedic Megachart** (inspired by classic high-density visual references such as *The Histomap of World History*, xkcd *Radiation Dose* / *Money*, and modern systems architecture posters) maximizes information density across both macro and micro viewing distances:
1. **Macro View (Zoomed Out / Across the Room / Mobile Preview)**:
   * The `T = H0` Title, `H1` Column/Row Short Names, color-coded organism/generation bands, and `H2` Cell Category Banners form a clean, balanced grid that communicates the entire taxonomy in 3 seconds.
2. **Micro View (Zoomed In / A0 Print Inspection)**:
   * Every cell exposes structured, high-signal technical detail (`H3` Core Mechanisms + `H4` `Sub-Category -> Concrete Products` pairs + `H4` `Anti-Patterns & Traps`), with zero wasted whitespace and zero text collisions.

## 2. Canvas & Aspect Ratio Mathematics (`19.5:9`)
* **Aspect Ratio**: `19.5 : 9` (`width / height = 2.16667`, matching modern smartphone landscape screens so full-screen mobile viewing has zero letterboxing).
* **Desktop / ISO A0-Width Print Canvas**:
  * `figsize = (46.8, 21.6)` inches at `dpi = 300` (`14040 x 6480 px`).
  * Physical width: `46.8 in * 25.4 mm/in = 1188.72 mm ≈ 1189 mm` (ISO A0 landscape width).
* **Mobile Companion Canvas**:
  * `figsize = (26.0, 12.0)` inches at `dpi = 300` (`7800 x 3600 px`).
  * Scale factor from Desktop A0: `SCALE = 26.0 / 46.8 = 5 / 9 ≈ 0.5556`.

## 3. Golden Ratio Typography Ladder (`φ = 1.61803398875`)
Anchor the typography at **`H2 = 24.00 pt`** on the `46.8 x 21.6 in` canvas:
```python
PHI = (1.0 + 5.0 ** 0.5) / 2.0  # 1.618033988749895
H2 = 24.0000          # 24.00 pt (8.47 mm) : Cell Zone-1 Category Banner & Masthead Subtitle
H1 = H2 * PHI         # 38.83 pt (13.70 mm): Column & Row Short Names (<= 2 words)
H0 = H1 * PHI         # 62.83 pt (22.17 mm): Main Megachart Title (T = H0)
H3 = H2 / PHI         # 14.83 pt (5.23 mm) : Cell Zone-2 Core Mechanisms & Masthead Reading Guide
H4 = H3 / PHI         #  9.17 pt (3.23 mm) : Full Names (<= 10 words), Sub-Category/Products, Anti-Patterns, Footnote
```

## 4. Programmatic Bounding-Box Collision Gate (Mandatory)
On macOS Retina systems, `fig.dpi` can be doubled internally during canvas creation if not compared directly against the axes renderer extent. Always measure text overflows using `ax.get_window_extent(renderer=r)` as the reference frame:

```python
fig.canvas.draw()
r = fig.canvas.get_renderer()
ax_bb = ax.get_window_extent(renderer=r)
ax_w_px, ax_h_px = ax_bb.width, ax_bb.height

# Compare any text artist `t` against its normalized box (box_w_norm, box_h_norm):
bb = t.get_window_extent(renderer=r)
w_ratio = bb.width / (box_w_norm * ax_w_px)
h_ratio = bb.height / (box_h_norm * ax_h_px)
assert w_ratio <= 0.96 and h_ratio <= 0.96, f"Overflow: w={w_ratio:.2f}, h={h_ratio:.2f}"
```

## 5. Masthead Subtitle & Caption Archetype
When writing a masthead blurb for a timeline or encyclopedic megachart:
1. **Lead with what the chart depicts** (in the spirit of *The Histomap* or xkcd *Radiation Dose*), covering both positive breakthroughs and negative fallout (e.g., *"A chart of the defining moments in AI: papers, Python libraries, models, unicorns: the breakthroughs and the fallout"*).
2. **State the empirical selection & stratification methodology** (e.g., candidate pool size, impact scoring, `Generation x Category` stratification, and 5-tier Golden Ratio sizing).
3. **Keep punctuation clean**: Zero em dashes (`U+2014`) anywhere.
