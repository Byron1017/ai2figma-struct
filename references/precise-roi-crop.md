# Precise ROI Crop Workflow

Use this workflow when extracting logos, mascots, pet renders, thumbnails, waveforms, decorative marks, empty-state illustrations, or other complex visuals from a larger UI reference image or foundation board.

This workflow exists because rough cropping spreads defects into every screen: dirty white boxes, clipped shadows, missing alpha, wrong scale, wrong focal point, and screenshot contamination.

## 1. Decide Whether To Crop

Crop only visuals that should remain image assets:

- brand marks when vector reconstruction would drift
- mascots and generated pet renders
- photos, avatar previews, wallpaper previews, thumbnails
- waveforms when the exact shape matters
- complex decorative marks, soft glows, orbital lines, empty-state illustrations
- atomic visually non-native component skins or states from a structured package, when the manifest says the asset owns the skin/state and native layers will not duplicate it

Do not crop these as reusable images:

- text labels, filenames, rules, or explanatory copy
- whole buttons with editable labels, whole cards, inputs, tabs, chips, switches, checkboxes, nav bars, status bars
- component containers, UI backgrounds, dividers, badges, or icon containers
- whole lists, whole tab bars, whole hero sections, modal bodies, app-shell regions, or mixed text/control regions

If a visual is a simple icon or UI primitive, rebuild it as native vector/native UI instead of cropping.

## 2. Create An ROI Manifest Before Import

Record every crop before placing it in Figma:

```text
Asset: brand-mascot-corgi.png
Source: ASSET-LIBRARY-v3.png
Source size: 1536 x 1024
ROI: x=194 y=164 w=128 h=128
Target use: Asset Library / Approved Brand Assets
Expected alpha: transparent / rectangular / masked
Keep shadow: yes/no
Exclude: title text, filename text, card border, white asset cell, neighboring assets
Status: candidate
Validation: pending
```

Never use an unrecorded or guessed crop for a promoted asset.

## 3. Crop The Smallest Correct Visual

Use the cleanest available source in this order:

1. original standalone asset file, if available
2. clean asset-library/foundation board
3. clean exported UI screen
4. user-accepted repaired crop

Crop rules:

- Include the whole intended visual and its intended soft edge or shadow.
- Exclude card containers, labels, filenames, badges, reference grid lines, and neighboring assets.
- Exclude unrelated editable text and neighboring controls. If the target is a component skin, crop only that single skin/state and record whether native text should be overlaid.
- Preserve original aspect ratio unless the board explicitly shows a masked container.
- For rectangular preview images, crop only image content; rebuild the surrounding card natively.
- For transparent assets, leave 1-4 px breathing room if antialiasing or shadow needs it.
- For flat/vector-like assets, do not add bevel, 3D, glow, or cute styling.

## 4. Transparent Background Pass

Only make an asset transparent when the visual should be independent of its board cell.

Use transparency for:

- pet renders and mascots
- paw marks and brand marks
- orbit lines, stars, dots, small decorations
- upload cloud icons, empty-state illustrations
- waveform graphics when used outside a native card

Do not make transparency for:

- screenshots of UI components
- full card previews where the background is part of the content
- wallpaper or avatar result images that are intentionally rectangular/masked

After transparency processing, validate on three backgrounds:

- white
- black or dark gray
- checkerboard

Reject or recrop when any of these appear:

- white/gray box around the asset
- dirty fringe or semi-transparent rectangle
- clipped ear, paw, shadow, line, waveform, or glow
- title, filename, badge, card border, or neighboring UI included
- wrong scale caused by too much empty margin

## 5. Figma Import And Verification

When importing or applying the crop in Figma:

- Place it in a named image container such as `Asset / brand-mascot-corgi.png`.
- Keep the source reference or crop note nearby until validation passes.
- Verify the actual node fill, `imageHash`, `scaleMode`, dimensions, clipping, and visibility.
- Do not assume an upload response means the intended node received the image.
- Store asset status in the node name or nearby manifest text: `promoted`, `candidate`, `page-local`, or `rejected`.

Use `FILL` only when the asset is a rectangular preview image inside a native mask. Use `FIT` or a transparent PNG container for independent cutouts.

## 6. Local Comparison Loop

For every promoted or reused asset, run a local comparison:

1. screenshot the source reference crop area
2. screenshot the rebuilt/imported asset area
3. compare boundary, scale, focal point, alpha, shadow, and color
4. log defects using `defect-taxonomy.md`
5. fix only the crop/container, not the surrounding library

Minimum checks:

- bounding box matches the reference use case
- no extra background pixels
- no clipped content
- transparent asset passes white/dark/checkerboard
- Figma image hash is recorded
- asset name and status match the asset-library reference

## 7. Promotion Rules For Crops

Promote an extracted crop only after:

- ROI manifest exists
- crop boundary is inspected
- alpha/background validation passes
- Figma placement and imageHash are verified
- source and target naming are consistent
- user or comparison loop accepts the visual

If any condition fails, keep the crop as `candidate` or `page-local`. Do not use a questionable crop as a shared library asset.
