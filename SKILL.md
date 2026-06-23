---
name: ai2figma-struct
description: Rebuild UI screenshots, generated UI images, mockups, or design images into editable Figma systems and screens. Use when the user asks to import to Figma, restore/recreate a UI, convert a screenshot into editable Figma layers, create a 100% editable UI version, analyze UI structure, extract visual tokens, identify component candidates, build or refine component/asset libraries, compare rebuilt Figma output against a UI image, or fix inaccurate Figma reconstructions including screenshot contamination, bad cutouts, background pollution, text overflow, missing assets, bitmap UI slices, wrong font size, inconsistent colors, wrong spacing, or non-pixel-matched output.
---

# AI2Figma Struct

Use this skill for high-fidelity screenshot-to-Figma reconstruction. The goal is an editable Figma system and screens that can be inspected, modified, reused, and handed to development.

Always load and follow `figma-use` before any `use_figma` call. Load `figma-generate-design` when building or updating composed Figma screens, design tokens, or reusable component structures.

## Core Model

Use a progressive foundation model, not a forced component-first model:

```text
Reference Intake
-> Foundation Discovery
-> Candidate Registry
-> Editable Screen Build
-> Visual Validation
-> Promotion to Tokens / Components / Assets
```

The long-term structure is:

```text
Design Tokens / Visual Spec
-> Component Library
-> Asset Library / Cutout Library
-> Editable Screens
```

Treat this structure as a progressive result, not a required starting point. Do not blindly create or force-use components and assets before they are validated. Wrong abstractions spread errors across every page. Build candidates first, validate them against screenshots, then promote stable patterns into the library.

Use four artifact layers:

- Visual Spec: colors, typography, spacing, radii, shadows, icons, and page-size rules discovered from accepted references.
- Component Library: only repeated, validated native UI patterns.
- Asset Library: only reusable, validated photos, mascots, generated imagery, cutouts, and complex decorations.
- Editable Screens: the actual page rebuilds; page-local layers are allowed when they match better than premature reuse.

## Source Of Truth Hierarchy

Use the highest-fidelity original UI as the visual source of truth:

1. Original/high-fidelity UI reference images or source design frames.
2. Clean exports from the original design.
3. User-accepted rebuilt pages, only as auxiliary evidence for structure or local fixes.
4. Unreviewed rebuilt pages, only as candidates.

Do not derive global colors, typography, shadows, spacing, or asset crops from rebuilt pages when an original/high-fidelity reference exists. Rebuilt pages may contain drift; using them as the standard will spread that drift into the visual spec, component library, and asset library.

## What Is Mandatory

Mandatory:

- Use clean reference images with exact bounds and size.
- Analyze UI structure before rebuilding.
- Record token, component, and asset candidates.
- Derive visual tokens from the highest-fidelity source reference, not from an unverified rebuild.
- Keep editable UI as native Figma layers or component instances.
- Keep complex visual content as independent image assets only when appropriate.
- Export rebuilt screens and compare them against the reference.
- Log defects and fix targeted local areas.

Not mandatory:

- Creating a full component library before the first page.
- Reusing an unvalidated component candidate.
- Promoting every image crop into a global asset library.
- Forcing a component when page-local editable reconstruction matches better.

Read `references/foundation-workflow.md` for the complete progressive workflow.

## Native UI Rule

Rebuild these as editable Figma layers or validated component instances:

- Text
- Cards, panels, backgrounds, dividers
- Buttons and icon buttons
- Inputs, upload zones, segmented controls
- Tabs, tab bars, navigation bars, status bars, WeChat capsules
- Tags, chips, badges
- Simple icons and icon containers
- Shadows, strokes, radii, spacing

Do not represent these UI elements with screenshot slices or image fills. Use clear layer names such as `Status Bar/Time`, `Primary Button/Label`, `Template Card/Image`, or `Tab Bar/Item Home`.

## Image Asset Rule

Use image assets for content that cannot be reliably rebuilt natively:

- Photos, avatars, product images
- Generated pets, mascots, complex illustrations
- Wallpaper and scene thumbnails
- Complex decorative marks, silhouettes, watermarks, soft glows, textures
- Fidelity-critical logo or brand imagery when vector reconstruction would drift

Image assets may be page-local, candidate assets, or promoted library assets. Do not promote an asset globally until its crop, alpha, scale, and use case are verified.

Read `references/asset-library.md` before extracting or placing assets.

## Workflow

1. Confirm target frame, target size, source reference, and quality level.
2. Create or obtain a clean reference PNG. Record pixel size, UI bounds, and any scale ratio.
3. Analyze layout hierarchy, text, UI components, image assets, icons, spacing, and fidelity risks.
4. Inspect existing Figma pages for accepted styles, existing components, variables, and reusable assets.
5. Create a candidate registry:
   - token candidates
   - component candidates
   - asset candidates
   - page-local exceptions
6. Decide what to reuse, what to rebuild page-locally, and what to extract as assets. Prefer page-local reconstruction when candidate quality is uncertain.
7. Build the editable screen section by section.
8. Export the rebuilt screen.
9. Generate full-page and local comparison sheets.
10. Classify defects with `references/defect-taxonomy.md`.
11. Apply targeted fixes only to inaccurate local areas.
12. Promote only validated repeated patterns into Design Tokens, Component Library, or Asset Library.

For the validation loop, read `references/validation-loop.md`.

## Promotion Rules

Promote a token/component/asset only when it is stable enough to reuse:

- Token: appears consistently in multiple locations or is confirmed by an accepted page/design spec.
- Component: appears in repeated UI patterns and survives at least one comparison/fix cycle.
- Asset: is reused across pages, required for development handoff, or explicitly requested by the user.

Keep uncertain items as candidates. Keep one-off or risky items page-local.

If a promoted component or asset causes visible drift, demote it to candidate status and use page-local reconstruction for that screen.

## Library Confidence Policy

Use the lightest reliable abstraction:

- Page-local: use by default for one-off patterns, uncertain crops, special cards, or pages that need exact reconstruction first.
- Candidate: use when a pattern appears reusable but has not passed comparison across contexts.
- Validated: use when a pattern has passed local comparison on the current page.
- Promoted: use as the default only after repeated evidence or explicit user approval.

Never let the existence of a component library override the screenshot. If a component instance makes the result less faithful, adjust the component variant, keep it page-local, or demote it.

## Figma Operation Discipline

Follow `figma-use` rules strictly:

- Inspect before mutating.
- Use small incremental `use_figma` calls.
- Return all created and mutated node IDs.
- Load fonts before editing text.
- Stop and read errors before retrying. Failed scripts are atomic.
- Verify screenshots after meaningful changes.
- Verify image fills by actual `imageHash`, node size, visibility, and scale mode.

## Quality Levels

Infer or ask for the target quality level:

- Draft: editable structure and rough visual direction.
- Development-ready: consistent editable UI, obvious layout errors removed.
- High-fidelity: strong local visual match, tuned typography, spacing, cards, and images.
- Pixel-critical: repeated comparison/fix cycles with explicit residual mismatch reporting.

Read `references/quality-levels.md` for stop criteria.

## Required Output

When reporting progress or completion, include:

- Reference PNG path and size.
- Target Figma frame name and size.
- Candidate registry status: tokens, components, assets, page-local exceptions.
- Promoted library items, if any.
- Native layers/components used.
- Image assets used and whether they are page-local, candidate, or promoted.
- Comparison sheet paths.
- Defect log summary.
- Remaining mismatch risk.

## References

- `references/foundation-workflow.md`: progressive tokens/components/assets/screens workflow.
- `references/rebuild-checklist.md`: screenshot analysis, extraction prompts, and common failures.
- `references/asset-library.md`: asset manifest, cutout rules, and promotion rules.
- `references/validation-loop.md`: export, compare, defect log, targeted fix loop.
- `references/defect-taxonomy.md`: defect categories and fix routing.
- `references/quality-levels.md`: acceptance levels and stop criteria.

## Scripts

- `scripts/make_comparison_sheet.py`: generate side-by-side comparison sheets from reference and rebuilt PNGs.

