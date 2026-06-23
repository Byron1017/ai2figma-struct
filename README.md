# AI2Figma Struct

AI2Figma Struct is a Codex skill for converting UI screenshots, generated mockups, and design images into editable Figma screens. It focuses on rebuilding real UI layers instead of flattening screenshots into bitmap slices.

The skill is designed for high-fidelity reconstruction workflows where the final Figma file should support editing text, buttons, cards, inputs, navigation, icons, tokens, reusable components, and asset libraries.

## What It Does

- Analyzes UI screenshots before rebuilding.
- Uses the highest-fidelity reference image as the visual source of truth.
- Rebuilds text, cards, buttons, inputs, tabs, navigation, and simple icons as native Figma layers.
- Keeps photos, avatars, generated characters, complex illustrations, wallpapers, and fidelity-critical decorative marks as image assets when needed.
- Separates work into visual tokens, component candidates, asset candidates, and editable screens.
- Avoids forcing premature components when page-local reconstruction is more accurate.
- Uses export-and-compare QA loops to find color, spacing, typography, crop, mask, and alignment defects.

## Workflow Model

```text
Reference Intake
-> Foundation Discovery
-> Candidate Registry
-> Editable Screen Build
-> Visual Validation
-> Promotion to Tokens / Components / Assets
```

The long-term Figma structure is:

```text
Design Tokens / Visual Spec
-> Component Library
-> Asset Library / Cutout Library
-> Editable Screens
```

This structure is progressive. Components and assets should be promoted only after they have been validated against the source reference.

## Directory Structure

```text
ai2figma-struct/
  SKILL.md
  agents/
    openai.yaml
  references/
    asset-library.md
    defect-taxonomy.md
    foundation-workflow.md
    quality-levels.md
    rebuild-checklist.md
    validation-loop.md
  scripts/
    make_comparison_sheet.py
```

## Installation

Copy this folder into your Codex skills directory:

```text
$CODEX_HOME/skills/ai2figma-struct
```

Then ask Codex to use the skill when working on Figma reconstruction tasks, for example:

```text
Use $ai2figma-struct to rebuild this UI screenshot into editable Figma layers.
```

## Comparison Sheet Script

The helper script creates side-by-side QA images from a reference export and a rebuilt export.

```bash
python scripts/make_comparison_sheet.py \
  --reference reference.png \
  --rebuilt rebuilt.png \
  --output comparison.png \
  --crop "header:0,0,750,180"
```

The script requires Pillow.

## Privacy Notes

This repository should contain only reusable skill instructions and helper scripts. Do not commit private Figma links, API tokens, client screenshots, generated project assets, local comparison outputs, or personal workspace paths.

## License

Add your preferred license before publishing publicly.

