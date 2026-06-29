---
name: ai2figma-struct
description: Rebuild UI screenshots, generated UI images, mockups, or ai2psd-struct packages into editable Figma systems and screens for program-development handoff. Use when the user asks to import to Figma, restore/recreate a UI, convert a screenshot into editable Figma layers, create a 100% editable UI version, consume structured manifests and atomic assets, analyze UI structure, extract visual tokens, identify component candidates, build or refine component/asset libraries, extract precise transparent assets from reference boards, compare rebuilt Figma output against a UI image, or fix inaccurate Figma reconstructions including screenshot contamination, bad cutouts, background pollution, missing assets, invalid large UI bitmap slices, wrong font size, inconsistent colors, wrong spacing, or non-pixel-matched output.
---

# AI2Figma Struct

Use this skill for high-fidelity screenshot-to-Figma reconstruction. The goal is an editable Figma system and screens that can be inspected, modified, reused, and handed to development.

Always load and follow `figma-use` before any `use_figma` call. Load `figma-generate-design` when building or updating composed Figma screens, design tokens, or reusable component structures.

## Development Handoff Priority

This skill exists to produce development-usable Figma source, not a screenshot poster.

Priority order:

1. Program-development usable structure and assets.
2. Editable Figma source.
3. Pixel-level visual closeness.

Pixel closeness is a QA target, not permission to flatten the UI. Do not satisfy "100%" by placing full-screen screenshots, large UI-region slices, whole cards, whole lists, whole tab bars, mixed text/control regions, or app-shell chunks as active assets. Use native/editable Figma structure plus atomic visual assets. If a gate fails, repair or rebuild locally; after the retry limit, keep the closest development-usable atomic/native result and record the defect.

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

Conditional exception for source-file rebuild projects: when the user provides clean foundation boards or asks for a complete Figma source rebuild, use the provided foundation boards before building screens. This is conditional, not universal. If a visual spec is provided, rebuild/import the visual spec first. If a component library is provided, rebuild/import the component library first. If an asset/cutout library is provided, rebuild/import the asset library first. Do not require missing foundation boards. Do not start screen reconstruction by extracting shared UI from an individual page when the relevant shared UI is available in a provided component or asset library.

Foundation-board projects are not ordinary page rebuilds. Treat visual-spec, component-library, and asset-library images as source documents:

- Their text explains the design system. Do not casually redesign, reflow, or reinterpret it.
- Their component examples define sizes, spacing, typography, states, and shared patterns.
- Their asset examples define approved crops, boundaries, status, and usage rules.
- Rebuild native UI components from measured reference geometry, not from visual taste.
- Extract complex visuals from the clean foundation image using precise ROI crops and alpha validation, not from individual screens and not by redrawing them in Figma.

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

## AI2PSD-AI2FIGMA Shared Contract

When a source package was produced by `ai2psd-struct` or contains `04-manifest/asset-map.json` and `04-manifest/screen-map.json`, treat `ai2figma-struct` as the consumer side of a paired pipeline. Use the package contract before applying ordinary screenshot-to-Figma judgment.

Shared asset QA statuses may appear as `qaStatus` or, in older manifests, `status`. Do not confuse them with `scope` values such as `page-local` or `approved-shared`.

- `approved`: use directly after manifest preflight.
- `repaired-approved`: use directly, preserving the repair metadata.
- `missing-repaired`: use directly, preserving the repair metadata.
- `active-best-effort`: use only with visible risk reporting; do not silently promote it.
- `needs-regeneration`: run the repair asset pipeline before use when the user expects completion.
- `rejected`: do not use.

In paired-package mode, the manifest's `ownership`, `contentBBox`, `targetPlacement`, and `layerOrder` override generic native-vs-image assumptions only for atomic, development-usable assets. Native layers are still preferred for text and simple containers, but do not redraw complex visuals already owned by valid package assets.

Do not trust a manifest entry just because it says `approved`, `page-local`, or `approved-shared`. If an active asset is a large UI-region slice, mixed text/control bitmap, whole card/list/tab/hero/app-shell image, or any asset a developer would need to cut again, mark it `invalid-ui-region-slice`, demote it to reference-only for comparison, and route the affected area through native rebuild plus atomic asset repair. Do not place the large slice as the active Figma reconstruction layer.

Do not stop at a defect when the user expects the job completed. First run the repair asset pipeline or a local rebuild fix. Stop only when the user explicitly asked for audit-only work, a required external tool is unavailable, or every repair path is blocked.

## Foundation Exact Intake Gate

When the user provides clean foundation images such as a visual specification, component library, asset library, or approved UI screen set, run this gate before rebuilding pages.

This gate is mandatory for high-fidelity and pixel-critical work:

1. Place the clean foundation images in Figma as locked reference layers with their exact pixel dimensions and names such as `Reference / Visual Spec`, `Reference / Component Library`, and `Reference / Asset Library`.
2. Derive colors, typography, spacing, radii, shadows, component sizes, bottom tab styles, button states, card styles, icon containers, and asset boundaries only from these clean references.
3. Create a calibration sheet from the foundation references before building screens:
   - page size and safe area
   - navigation/status/capsule sample
   - bottom tab sample
   - primary/secondary/text/icon button states
   - chip, input, selector, switch, checkbox samples
   - pet card, upload card, template card, result card, record card samples
   - approved image assets and page-local image assets
4. Run the precise ROI crop workflow for every complex asset that must be extracted from a foundation image. Read `references/precise-roi-crop.md` before cropping or importing these assets.
5. Extract or upload clean image assets from the asset library reference when a correct crop already exists. Do not regenerate, redraw, stylize, or substitute these assets.
6. For component examples, rebuild UI structure as native editable layers, but keep the clean reference directly behind or beside it until export comparison passes.
7. Screens must be rebuilt against the source screen image or clean exported UI image, not against an agent-created approximation or a previous unreviewed rebuild.
8. If the project includes a component-library reference, rebuild or validate the component source library before rebuilding screens. Shared UI such as bottom tab bars, top navigation, status/capsule bars, primary buttons, chips, inputs, cards, toggles, and icon buttons must come from the component library or be rebuilt from that component-library reference.
9. If the project includes an asset-library reference, rebuild or validate the asset/cutout library before rebuilding screens. Brand logos, mascot images, approved pet renders, hero pets, thumbnails, waveform graphics, empty-state illustrations, and decorative marks must come from this asset library or from an approved asset extraction pass.
10. If an accepted editable page already exists in the Figma file, inspect and reuse it before rebuilding that page again. Accepted pages may be copied into the new version and then aligned to the current foundation reference.

Hard prohibitions under this gate:

- Do not invent icons, pet images, thumbnails, or waveform styles when they appear in the foundation images.
- Do not approximate brand assets, mascots, tab icons, or complex decorative elements with generic symbols.
- Do not use guessed crop bounds for assets from foundation boards. Every crop needs an ROI record, local crop screenshot, alpha/background check, and final placement check.
- Do not crop shared components such as bottom tabs, nav bars, buttons, chips, inputs, card shells, or icon containers from an individual screen when they exist in the component-library reference.
- Do not flatten foundation-board explanatory text into images when rebuilding the source library. Text that explains tokens, components, rules, status, labels, or filenames should be editable text unless the user explicitly asks for visual-only documentation.
- Do not crop UI components from foundation boards as reusable bitmaps. Native components must be rebuilt from measured reference geometry. Only photos, mascots, generated pets, complex illustrations, decorative marks, and other non-native visuals may become image assets.
- Do not rebuild an accepted editable page from scratch unless the user explicitly asks for a new reconstruction.
- Do not promote a component or token if it has not been checked against the clean foundation reference.
- Do not delete or hide the reference layer before validation is complete.

## Foundation Board Reconstruction Rules

Use these rules when rebuilding clean visual-spec, component-library, or asset-library boards:

- Treat the foundation board as a specification document and asset manifest, not as a freeform design prompt.
- Preserve the board's visible information architecture: section order, labels, filenames, status markers, and usage notes.
- Recreate explanatory text as editable Figma text with matching font size, line height, and spacing. Do not rewrite wording unless OCR is impossible or the user asks for copy changes.
- Recreate colors, spacing blocks, typography samples, radii, shadows, and UI examples from measured positions and dimensions.
- Rebuild buttons, tabs, inputs, cards, chips, switches, checkboxes, and navigation as native Figma components or editable frames.
- Extract brand marks, mascots, pet renders, thumbnails, waveforms, decorative marks, and illustrations from the relevant asset-library reference using precise ROI crop. Do not redraw these visuals with primitives unless the reference itself is vector-simple and the vector match is better.
- Keep the clean foundation image locked beside or behind the rebuild until local comparisons pass.
- If crop precision is uncertain, stop at an asset candidate with a defect note. Do not promote it into the reusable asset library.

## Structured Image Package Intake

When the source package was produced by `ai2psd-struct` or contains `04-manifest/asset-map.json` and `04-manifest/screen-map.json`, enter paired-package mode. Treat those manifests as the reconstruction contract, then verify them against the source screen before and after placement.

Intake order:

1. Read `screen-map.json` to identify screen files, target sizes, foundation references, regions, native rebuild targets, component references, asset references, page-local assets, `assetUsages[]`, and known risks.
2. Read `asset-map.json` to locate promoted, candidate, page-local, and rejected visual assets.
3. Verify that referenced files exist before building in Figma. If a referenced asset is missing and the task is not audit-only, run the repair asset pipeline instead of inventing a substitute or stopping.
4. If clean visual-spec, component-library, or asset-library images are present, rebuild those libraries first according to the Foundation Exact Intake Gate.
5. Use assets whose QA status is `approved`, `repaired-approved`, or `missing-repaired` as the default only when they visually match the source screen. Use `active-best-effort` assets only when no better repaired version is available, and keep their risk visible in the defect log.
6. Keep native rebuild targets native only when the usage ownership permits it. `screen-map.assetUsages[].ownership` is stronger than the generic native rule: assets that own skins, icons, shadows, gradients, or state visuals must not be duplicated with native drawing.
7. If a manifest conflicts with the original screen image, the highest-fidelity screen image wins. Log the conflict and fix locally through repair assets, placement correction, or native layer correction.
8. Reject any manifest active asset whose granularity is not atomic or development-usable. Use it only as a locked reference/comparison image while rebuilding the UI structure natively and repairing the missing atomic assets.

Do not force missing, rejected, or low-confidence package assets into the rebuild without repair. The manifest reduces guessing; it does not replace visual comparison. If repair still fails after the retry limit, use the best available version as `active-best-effort` and report the remaining mismatch.

### Manifest Preflight And Repair Routing

Before placing assets, preflight every asset referenced by the target screen:

- file exists and has usable dimensions;
- QA status is `approved`, `repaired-approved`, `missing-repaired`, or explicitly `active-best-effort`; if only `status: page-local` or another scope-like value exists, require `validation.approved`, `asset-quality-audit`, or a repair log to prove usability;
- `contentBBox` exists on the asset;
- a `screen-map.assetUsages[]` record exists for the target screen when the asset is visible or pixel-critical;
- the usage record has `targetPlacement`, `layerOrder`, `ownership`, and `alignBy`;
- `contentBBox` and usage `targetPlacement` aspect ratios are compatible;
- usage `ownership` is present or can be inferred safely from the reference;
- usage `layerOrder` is present or can be assigned from the default layer stack;
- usage `localPastebackStatus` is `passed`, or the asset is explicitly `active-best-effort` with a defect record.
- `handoffPurpose` is compatible with development handoff when provided;
- `assetGranularity` is `atomic` or a more specific atomic class when provided;
- `developmentUsable` is not `false`;
- the asset does not contain unrelated editable text, multiple controls, multiple cards/list rows, a whole tab bar, a whole hero area, a modal body, or other large UI-region content.

Route defects:

- missing file or missing complex visual: run the repair asset pipeline;
- rejected asset: do not use; repair or replace it;
- `needs-regeneration`: repair before use;
- aspect-ratio conflict: first retry extraction/crop from package sources or source ROI; if unavailable, generate a replacement repair asset;
- missing usage placement: measure from the source reference or package paste-back evidence, write a repair addendum, and run local paste-back; after three failed placement attempts, mark the usage `active-best-effort` and continue with a visible defect note;
- missing local paste-back: run a local paste-back check before trusting the placement; if it fails, repair placement or asset before use;
- invalid large UI-region slice: demote to reference-only, rebuild the surrounding UI natively, and repair or generate the needed atomic assets;
- non-development asset granularity: repair into atomic assets or use native/vector reconstruction;
- missing ownership: infer only once from the source reference, record `ownershipInferred: true`, and avoid duplicate drawing;
- missing layer order: assign the default stack and record `layerOrderInferred: true`.

Do not replace complex icons, 3D renders, tab states, badges, decorative marks, or button-internal visuals with circles, emoji, generic icon sets, or hand-drawn approximations.

### Repair Asset Pipeline

Use this pipeline only when the structured package is missing, rejecting, or visibly mismatching a required visual and the user expects the reconstruction to be completed.

Repair priority:

1. Re-extract, recrop, or reprocess from same-generation working sources such as asset sheets, matte sources, or approved source files under the package.
2. Extract or clean from the original UI reference ROI when that is the only available source and the screenshot-crop exception allows it.
3. Generate a replacement with `imagegen` using the UI reference ROI or same-generation source as the visual anchor.
4. Generate from text prompt only when no usable source or ROI exists.
5. After three failed attempts for the same asset issue, use the closest atomic asset, native/vector reconstruction, or unresolved atomic defect as `active-best-effort`, record the remaining defect, and continue the rebuild.

The fallback is still development-first. Never promote a large UI-region slice, whole card/list/tab/hero/app-shell bitmap, or mixed text/control screenshot as `active-best-effort`. If an atomic replacement cannot be made, rebuild the affected area with native layers, keep the bad slice as reference-only if useful, and record what visual detail remains imperfect.

Store repaired assets separately from original package assets when possible, for example under `03-transparent-assets/rebuild-repairs/<screenId>/`, and write or update a repair addendum such as `04-manifest/rebuild-repair-log.json`. The log should include source, attempts, selected version, status, and remaining mismatch.

### Simple Placement Contract

When a package provides placement metadata, use it before estimating by eye.

For each screen asset usage, look for:

- `contentBBox`: tight visible bounds inside the PNG, excluding transparent safety padding.
- `screen-map.assetUsages[].targetPlacement`: intended visual bounds on the target screen.
- `screen-map.assetUsages[].layerOrder`: relative stack order.
- `screen-map.assetUsages[].ownership`: which parts are already inside the asset and which parts should be native.
- `screen-map.assetUsages[].alignBy`: normally `contentBBox`.

`screen-map.assetUsages[]` is the canonical placement contract for paired `ai2psd-struct` packages. Legacy `asset-map.assets[].targetPlacement` may be used only when a package has no `assetUsages[]` and the asset is clearly single-use; record that fallback in the defect log.

Placement rule:

- If both `contentBBox` and usage `targetPlacement` exist, align the asset's content bounds to `targetPlacement`. Do not size the Figma node as if the full transparent PNG canvas were the visible element.
- Use uniform scaling for pixel-critical assets. Compute `scaleX = targetPlacement.width / contentBBox.width` and `scaleY = targetPlacement.height / contentBBox.height`. If they are close, use one uniform `scale`, size the PNG node to `pngWidth * scale` and `pngHeight * scale`, then position it at `targetPlacement.x - contentBBox.x * scale` and `targetPlacement.y - contentBBox.y * scale`. If they conflict, route to repair or best-effort handling; do not stretch the image to hide the mismatch.
- If only `targetPlacement` exists, place the asset there and record that transparent padding may affect scale.
- If no usage placement exists, measure from the reference image and write the estimated usage to the repair log before placing. Do not silently guess.

Ownership rule:

- `asset-only`: place the asset and do not redraw its internal icon, label, state, shadow, or decoration.
- `asset-with-native-text`: place the asset skin and overlay editable text only. Do not redraw embedded icons, stars, shadows, gradients, or state visuals.
- `native-with-asset-icon`: rebuild the container/text natively and place only the listed icon/avatar/thumbnail/decor asset.
- `native-only`: rebuild with Figma layers and do not place an image asset.

`asset-only` is valid only for one atomic visual element or one self-contained visual skin/state. It is not valid for a whole card containing multiple editable parts, a list area, a tab bar with multiple items and labels, a hero region containing title/buttons/art, a modal body, or any mixed UI slice. Those regions must become native structure plus atomic assets.

Do not duplicate one visual part across asset and native layers. If a button, chip, badge, card, or tab asset already contains an icon or selected-state skin, do not add a second native icon or a second selected-state treatment. If ownership is unclear, prefer the source reference: use the asset for complex/gradient/3D/state visuals and keep only necessary text native.

### Final Layer Order And Validation Loop

Before exporting a rebuilt screen, run a final layer-order pass:

```text
page background and native container skins
-> image assets and repaired assets
-> editable text and simple foreground vectors
-> status bars, system chrome, fixed overlays, and top controls
```

Within the image-asset layer, respect usage `layerOrder`. Native text overlays declared by `asset-with-native-text` must sit above their asset skins. Do not allow later-created native card backgrounds or container fills to cover image assets.

After ordering, export the rebuilt screen and compare it with the source reference. Fix local defects, not the whole page, unless the entire layout is wrong. Use at most three local repair passes for the same defect category. If a defect remains after three passes, keep the closest version, mark the relevant layer or asset `active-best-effort`, and include the residual mismatch in the final report.
## Conditional Source Library First Mode

Use this mode when the user asks for a full editable Figma source file, a UI version suitable for development, or explicitly says to build visual spec, component library, asset library, then pages.

This mode is conditional on available inputs. Build only the foundation libraries that the user provides or explicitly asks for. If a UI project has no visual-spec reference, no component-library reference, or no asset-library reference, do not invent or force that missing library as a hard prerequisite. Continue with the progressive page-level workflow and promote repeated patterns after validation.

Conditional order:

1. Reference boards: place any provided clean visual-spec, component-library, asset-library, and screen references in Figma as locked image layers.
2. Visual Spec source, if provided or requested: rebuild the visual specification as editable tokens/styles/docs from the clean visual-spec reference. Record page size, colors, typography, spacing, radius, shadow, navigation, and asset rules.
3. Component Library source, if provided or requested: rebuild shared components from the clean component-library reference. Public components may include status bar, WeChat capsule, top nav, bottom tab, primary/secondary/text/icon buttons, chips, segmented controls, inputs, selectors, switches, checkboxes, pet selector/card, upload card, template card, result card, record card, empty/success/failure feedback, and bottom-sheet/modal patterns.
4. Asset Library source, if provided or requested: rebuild the asset/cutout library from the clean asset-library reference. Use precise ROI crop for approved, candidate, and page-local visual assets. Store asset names, source reference, ROI bounds, imageHash values, alpha notes, validation status, and promotion status.
5. Screen assembly: create editable screens using any available source libraries. Use page-local reconstruction for missing libraries, one-off details, or unvalidated variants.
6. Validation: compare each rebuilt screen to its original screen reference and fix locally.

Screen work is blocked only by foundations that are both relevant and provided/requested. Examples:

- If visual spec, component library, and asset library are all provided, build all three before screens.
- If only screen images are provided, do not block on a missing library; rebuild pages progressively and promote repeated patterns after validation.
- If only a component library is provided, rebuild relevant shared components before screens, but do not invent a separate visual spec or asset library unless needed.
- If only an asset library is provided, use those assets before screens, but rebuild UI components page-locally until repeated patterns are validated.

Reuse policy:

- If a validated source component exists, use it or copy it. Do not redraw it ad hoc.
- If a component reference exists but the source component has not been rebuilt, rebuild that component from the component-library reference first.
- If a screen already has a user-approved editable version in an older UI version, copy that accepted frame into the new version and reconcile it with the current source libraries. Do not restart from raw screenshot extraction.

## What Is Mandatory

Mandatory:

- Use clean reference images with exact bounds and size.
- When clean foundation images exist, run the Foundation Exact Intake Gate before creating tokens, components, assets, or screens.
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

Exception for paired `ai2psd-struct` packages: manifest `ownership` overrides this generic native rule only after manifest preflight confirms the asset is atomic and development-usable. If a valid asset is `asset-only`, place it as the complete visual. If it is `asset-with-native-text`, place the visual skin/icon/shadow/gradient asset and overlay only the editable text. If it is `native-with-asset-icon`, rebuild the container/text natively and place only the listed asset. Do not redraw a visual part already owned by the asset. If the manifest asset is a large UI-region slice, ignore its ownership for active reconstruction and route it through repair/native rebuild.

## Image Asset Rule

Use image assets for content that cannot be reliably rebuilt natively:

- Photos, avatars, product images
- Generated pets, mascots, complex illustrations
- Wallpaper and scene thumbnails
- Complex decorative marks, silhouettes, watermarks, soft glows, textures
- Fidelity-critical logo or brand imagery when vector reconstruction would drift

Image assets may be page-local, candidate assets, or promoted library assets. Do not promote an asset globally until its crop, alpha, scale, and use case are verified.

For development handoff, image assets must be atomic. A valid image asset may be a single icon/state, illustration, avatar/photo/thumbnail, decorative mark, generated subject, logo, waveform, visual skin, shadow/glow, or other standalone visual unit. It must not be a large mixed UI region that includes unrelated native text, multiple controls, multiple cards/list rows, a whole navigation bar, or a full app-shell area.

Read `references/asset-library.md` before extracting or placing assets.

Read `references/precise-roi-crop.md` before cropping assets from a larger reference board, screenshot, or generated UI image. This is mandatory when a user complains about bad cutout boundaries, background contamination, inaccurate transparent assets, or foundation-library assets.

## Workflow

1. Confirm target frame, target size, source reference, and quality level.
2. Create or obtain a clean reference PNG. Record pixel size, UI bounds, and any scale ratio.
3. Analyze layout hierarchy, text, UI components, image assets, icons, spacing, and fidelity risks.
4. Inspect existing Figma pages for accepted styles, existing components, variables, and reusable assets.
5. Create a candidate registry:
   - token candidates
   - component candidates
   - asset candidates
   - precise ROI crop records for extracted assets
   - page-local exceptions
6. Decide what to reuse, what to rebuild page-locally, and what to extract as assets. Prefer page-local reconstruction when candidate quality is uncertain.
7. Build the editable screen section by section.
8. In paired-package mode, run manifest preflight before placement and route missing or invalid assets through the repair asset pipeline.
9. Run final layer ordering before export.
10. Export the rebuilt screen.
11. Generate full-page and local comparison sheets.
12. Classify defects with `references/defect-taxonomy.md`.
13. Apply targeted fixes only to inaccurate local areas, with at most three repair passes for the same defect before best-effort fallback.
14. Promote only validated repeated patterns into Design Tokens, Component Library, or Asset Library.

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
- Image assets used and whether they are page-local, candidate, or promoted. For extracted assets, include ROI bounds, alpha/background validation status, and imageHash verification.
- Repair assets created during rebuild, their sources, attempt count, selected status, and whether any are `active-best-effort`.
- Comparison sheet paths.
- Defect log summary.
- Remaining mismatch risk.

## References

- `references/foundation-workflow.md`: progressive tokens/components/assets/screens workflow.
- `references/rebuild-checklist.md`: screenshot analysis, extraction prompts, and common failures.
- `references/asset-library.md`: asset manifest, cutout rules, and promotion rules.
- `references/precise-roi-crop.md`: precise crop, transparent-background, ROI, and crop validation workflow.
- `references/validation-loop.md`: export, compare, defect log, targeted fix loop.
- `references/defect-taxonomy.md`: defect categories and fix routing.
- `references/quality-levels.md`: acceptance levels and stop criteria.

## Scripts

- `scripts/make_comparison_sheet.py`: generate side-by-side comparison sheets from reference and rebuilt PNGs.


