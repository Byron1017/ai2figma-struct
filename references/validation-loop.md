# Validation Loop

Use validation to control quality. Do not rely on visual memory.

## Required Loop

```text
Export -> Compare -> Defect Log -> Targeted Fix -> Re-export
```

Run this loop for every rebuilt screen and for any high-risk section.

## Export Requirements

Export at the intended target size whenever possible. Record:

- reference PNG path and size
- rebuilt PNG path and size
- Figma frame id and name
- scale ratio
- export timestamp or iteration label

## Comparison Requirements

Create:

- full-page side-by-side comparison
- top/navigation crop
- primary content crop
- key card/list crop
- button/tag/control crop
- bottom navigation or fixed action crop
- complex asset crop when images are involved

Use `scripts/make_comparison_sheet.py` for side-by-side sheets when local PNGs are available.

## Defect Log Format

```text
Iteration: V3
Frame: 04 Create
Reference: v3-04-reference.png
Rebuild: v6-04-current.png

Defects:
1. Typography / Major / Header title 4px too small / Fix title style
2. Image Crop / Major / template cat images too large / replace with source crop
3. Spacing / Minor / card row gap 6px too wide / adjust x positions
4. Asset Contamination / Critical / bottom tab image includes content above / recrop asset

Decision:
- Fix critical and major now.
- Leave minor if user accepts or quality level is Development-ready.
```

## Fix Rules

- Fix the smallest local area that explains the defect.
- Do not rebuild the whole page to fix one crop, label, or card.
- Do not create new global components while fixing a page unless the defect proves an existing component needs promotion/demotion.
- If a component causes repeated drift, demote it and use page-local reconstruction.

## Stop Criteria

Stop when the requested quality level is reached and remaining defects are recorded.

For High-fidelity and Pixel-critical work, at least one full-page comparison and focused local comparisons must be produced after the final fix.


