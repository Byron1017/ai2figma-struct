# AI2Figma Struct Checklist

Use this checklist when rebuilding a UI screenshot or generated UI image into editable Figma layers.

## Reference Capture Prompt

Use before analysis when the UI source may include browser chrome, Codex chat UI, editor panels, desktop background, surrounding whitespace, or other unrelated content:

```text
Create a clean UI reference PNG before rebuilding.

Requirements:
- Do not use a hand-drawn screen-region screenshot if an element, frame, viewport, canvas, or source image export is available.
- Capture only the target UI, not the browser frame, Codex/chat UI, Figma sidebars, DevTools, desktop, or neighboring content.
- Keep the UI at a fixed, known size.
- If the available screenshot is larger than the UI, crop it deterministically to the UI boundary.
- Preserve intended internal blank margins, but remove unrelated outside margins.
- Preserve the real UI background and surfaces; do not make the whole UI reference transparent.
- Save the cleaned PNG separately and report its exact pixel width and height.
- Do not start the Figma rebuild until the reference PNG contains only the intended UI.
```

Preferred capture order:

1. Export the original design/image file directly.
2. Capture the browser element or app container.
3. Capture the fixed viewport when the whole viewport is the UI.
4. Capture a larger screenshot, then crop by known target size or detected UI bounds.
5. Ask for a cleaner source only when the target boundary cannot be determined.

## Analysis Prompt

Before rebuilding, confirm the UI structure:

```text
Analyze the UI image first. Do not rebuild yet.

Output a layer and asset reconstruction checklist:
1. Confirm the reference image is clean and list its exact pixel size.
2. Page size.
3. Overall background.
4. Top navigation/status area.
5. Main content sections.
6. Text, buttons, icons, cards, images, tags, inputs, and tabs in each section.
7. Approximate size, position, spacing, and alignment relationships.
8. Elements that must be rebuilt as native Figma layers: text, cards, buttons, inputs, tabs, tags, nav bars, dividers, simple shapes, backgrounds, shadows, strokes, and spacing.
9. Elements that should be rebuilt as vector/icon candidates.
10. Elements that may remain image assets: photos, avatars, product renders, complex illustrations, irregular decoration, watermarks, or generated imagery.
11. Transparent PNG extraction targets, with local crop bounds and why each one should not be rebuilt natively.
12. Source-reference to target-Figma scale ratio, if sizes differ.
13. Candidate registry:
   - token candidates
   - component candidates
   - asset candidates
   - page-local exceptions
14. Likely fidelity risks.

Do not use bitmap UI slices for text, cards, buttons, navigation, tags, or inputs.
Do not extract transparent PNG assets until after this checklist is complete.
```

## Candidate Registry Prompt

Use after analysis and before rebuilding:

```text
Create a candidate registry before editing Figma.

For each candidate, list:
1. Name.
2. Type: token, component, asset, or page-local exception.
3. Evidence: which page/section/crop shows it.
4. Shared traits.
5. Known variants or uncertainty.
6. Risk if reused too early.
7. Decision: promoted, validated, candidate, page-local, or rejected.

Rules:
- Do not promote anything only because it appears once.
- Do not force a candidate component into the page if native page-local reconstruction is more faithful.
- Do not store screenshot slices of UI controls as assets.
- Keep uncertain items as candidates until export comparison validates them.
```

## Asset Extraction Prompt

Use only after the clean full-UI reference has been analyzed and the extraction targets are listed:

```text
Before extracting PNGs, create an asset extraction table.

For each asset, list:
1. Asset name.
2. Asset type: photo, avatar, product render, illustration, decoration, watermark, generated image, or other.
3. Why this asset should be a PNG instead of native Figma layers.
4. Source bounds: x, y, width, height in reference-image pixels.
5. Visible asset boundary: what pixels belong to the asset.
6. Exclude: surrounding background, card fill, text, button, icon container, divider, or unrelated UI that must not be captured.
7. Edge/alpha treatment: hard edge, antialiased edge, soft edge, shadow, glow, blur, translucency, texture.
8. Padding: exact pixels to include around the visible asset, and why.
9. Whether shadow/glow stays in the PNG or should be rebuilt as a native Figma effect.
10. Target Figma placement: x, y, width, height after applying the scale ratio.

After the table is complete, extract only the approved independent image/decorative assets from the clean UI reference.

Requirements:
- Do not extract text, buttons, inputs, cards, tabs, tags, nav bars, dividers, simple icons, or page backgrounds as PNG assets.
- Output transparent PNGs only for visual assets that are not practical to rebuild natively.
- Use the smallest crop that contains the asset's intended visible pixels plus intentional padding.
- Preserve each asset's visible bounds, opacity, softness, color temperature, edge antialiasing, and local crop.
- Remove unrelated UI background pixels from the transparent area.
- Record each asset's original x/y/width/height in source-reference pixels.
- If the target Figma frame size differs from the source reference, compute the scale ratio and provide scaled x/y/width/height.
- Place each asset over native Figma layers, not as a replacement for native UI structure.
```

## PNG Boundary Validation Prompt

Use after extracting each transparent PNG and before placing it in Figma:

```text
Validate each extracted transparent PNG before using it.

For each PNG:
1. Inspect it on a checkerboard background.
2. Inspect it on a dark solid background.
3. Inspect it on a light solid background.
4. Check whether the transparent area contains leftover UI background color.
5. Check whether a rectangular crop edge is visible.
6. Check whether antialiasing, soft edges, translucency, shadow, glow, or texture were accidentally removed.
7. Check whether unrelated text, card fill, button, icon container, divider, or whitespace was included.
8. If any issue appears, redo the extraction from the original clean UI reference instead of hiding the issue in Figma.

Report for each PNG:
- pass/fail
- PNG dimensions
- source bounds
- target Figma placement
- whether shadow/glow is included in PNG or rebuilt in Figma
- remaining edge risk, if any
```

## Rebuild Prompt

```text
Rebuild this UI image into Figma as an editable page.

Requirements:
- Create the frame at the exact source image size.
- Use native Figma Text for all text.
- Use native Frame/Rectangle/Text/Vector/Auto Layout for cards, buttons, inputs, nav bars, tags, tabs, icon containers, dividers, and backgrounds.
- Only photos, avatars, complex illustrations, generated pet/product images, and subtle decorative assets may remain images.
- Use vector icons when practical; do not crop UI icons out of screenshots unless the icon is unusually complex.
- Name layers clearly.
- Use Auto Layout for page, sections, rows, columns, cards, and buttons.
- Calibrate font size, weight, and line height before judging layout spacing.
- Preserve image crop, card radius, shadow, fill, stroke, opacity, and local alignment.
- Do not use full-page screenshots or large UI-area image slices.
- If the target Figma frame size differs from the source reference, apply the same scale ratio to element positions, sizes, spacing, and extracted PNG placement.
```

## Validation Prompt

```text
Export the rebuilt Figma frame and compare it against the original UI image.

Do not only inspect the whole page. Also create local comparison crops for:
1. Top navigation.
2. Main visual/action area.
3. Core cards.
4. Buttons and tags.
5. Bottom navigation.
6. Complex images and decorative assets.

Check text size, weight, line height, overflow, card sizes, radius, shadow, icon size, image crop, decorative asset opacity, missing assets, unwanted 3D effects, and alignment.

Fix only the inaccurate local area, then export and compare again.
```

## Decorative Asset Prompt

Use when a small complex element cannot be rebuilt cleanly with Figma primitives:

```text
Use the provided original UI crop as visual reference.
Redraw or extract only the target decorative element.
Ignore text, cards, buttons, icon containers, background, and unrelated UI.

Output a transparent PNG.
Match the reference shape, opacity, color temperature, and visual weight.
If the reference is flat, keep it flat.
No 3D, no bevel, no highlight, no material, no extra shadow, no gradient, no cute extra details.
If it is a watermark, keep it low contrast.
If it is a silhouette, keep it as a silhouette.
If it is a light patch, keep it broad, soft, and low contrast.
```

## Common Failure Patterns

- Manually dragging a screenshot region and accidentally including browser chrome, chat UI, Figma panels, desktop background, or unrelated whitespace.
- Rebuilding from an uncropped reference whose outer bounds do not match the intended Figma frame.
- Cropping away intentional internal blank margin because outside margin and UI padding were not distinguished.
- Making the whole UI background transparent instead of preserving the page background and extracting only independent assets.
- Extracting transparent PNGs before classifying which elements should be native Figma layers.
- Using transparent PNGs for text, cards, buttons, inputs, navigation, or other editable UI structure.
- Screenshotting a rectangular asset crop and leaving the original UI background visible around the object.
- Omitting soft antialiasing or semi-transparent edge pixels, causing jagged cutout edges.
- Including both PNG shadows and native Figma shadows, making the asset look heavier than the source.
- Forgetting to validate PNGs on checkerboard, dark, and light backgrounds before placing them in Figma.
- Forgetting to apply the source-to-Figma scale ratio to extracted asset placement.
- Starting with the wrong font size, causing the whole layout to become cramped or oversized.
- Using bitmap slices for UI regions, making the design unusable for development.
- Replacing subtle flat decorations with 3D-looking generated assets.
- Drawing complex animal silhouettes with Figma circles/rectangles instead of extracting a real local asset.
- Inspecting only the full page, where small errors are hidden.
- Trusting upload success without checking whether the Figma node actually received the intended `imageHash`.
- Rebuilding the whole page to fix one local asset, which introduces new drift.

## Acceptance Rule

A rebuilt page is acceptable only when the user can edit text, cards, buttons, colors, spacing, and radii independently, while the exported screenshot visually matches the source image at full-page and local-crop levels.

