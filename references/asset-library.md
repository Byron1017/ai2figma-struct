# Asset Library And Cutout Rules

Use this guide for photos, generated pets, mascots, thumbnails, decorative marks, and other visuals that should not be rebuilt as native UI.

When the asset comes from a larger reference board, screenshot, or generated UI image, read and follow `precise-roi-crop.md` first. This is mandatory for foundation-board asset libraries and for any task involving transparent-background cutouts, screenshot contamination, bad crop boundaries, or alpha validation.

For program-development handoff, every active image asset must be atomic: one icon/state, one photo/avatar/thumbnail, one generated subject, one decoration, one visual skin/state, one shadow/glow, or another standalone visual unit. If the file contains unrelated native UI, multiple controls, multiple cards/list rows, a whole tab bar, a whole hero area, or any region that must be cut again, reject it as `invalid-ui-region-slice` and keep it reference-only.

## Asset Status

Use `qaStatus` for usability and `scope` for reuse:

QA status:

- approved: accepted for use
- repaired-approved: repaired and accepted
- missing-repaired: generated or extracted after being missing, then accepted
- active-best-effort: closest atomic/native result after retry limit
- needs-regeneration: not ready yet
- rejected: bad crop, contaminated, wrong style, invalid granularity, or no longer needed

Scope:

- page-local: used only in the current screen
- candidate: may be reused, but not validated enough for library use
- promoted: verified and safe to reuse by default

## Asset Manifest

Record assets in this format:

```text
Asset: Corgi Hero
QA status: approved
Scope: candidate
Type: generated pet image
Handoff purpose: program-development
Asset granularity: atomic-subject
Development usable: true
Source: V3 Home reference
Source bounds: x=180 y=120 w=220 h=430
Target placement: x=340 y=180 w=300 h=500
Alpha: transparent / rectangular / masked
Includes shadow: yes/no
Exclude: card fill, text, unrelated background
Validation: checkerboard pass, dark pass, light pass
Figma: node id, imageHash, scaleMode
Decision: keep candidate until reused successfully in Remote page
```

For assets cropped from foundation boards, the manifest must include exact ROI bounds before import. Do not promote an asset that only has a rough crop or visual guess.

## Extraction Rules

- Extract only independent visual content.
- Do not extract text, cards, buttons, nav bars, tags, inputs, dividers, or page backgrounds.
- A visually non-native component skin/state may be an asset only when it is one atomic unit with explicit ownership, such as one button skin, one card skin, one tab item state, one nav container skin, or one embedded icon state. Do not extract a whole multi-item bar, list area, modal body, or mixed text/control slice.
- Use the smallest crop that contains intended pixels plus necessary soft edge or shadow.
- Preserve antialiasing, translucency, soft glow, and texture when they belong to the asset.
- Remove unrelated UI background pixels.
- If the reference asset is flat, keep it flat. Do not add 3D, bevel, gradient, or cute extra details.
- Validate transparent assets on checkerboard, dark, and light backgrounds.
- Reject crops that include foundation-board titles, filenames, status badges, card borders, asset cells, or neighboring examples unless those pixels are explicitly part of the intended asset.

## Rectangular Crops

Rectangular crops are allowed for photo-like content inside a native UI container:

- pet photos
- wallpaper thumbnails
- generated result previews
- real product/scene images

The surrounding card, labels, badges, and controls must remain native Figma layers.

## Promotion Rules

Promote an asset only when:

- it is reused across screens, or
- it is part of brand/base material, or
- the user requests a reusable asset, or
- development needs it as a standalone export

Do not promote one-off page crops. Keep them page-local.

## Demotion Rules

Demote or reject an asset when:

- background contamination is visible
- crop includes unrelated UI
- asset is a large UI-region slice instead of an atomic development unit
- color/contrast differs from reference
- it forces wrong placement in another page
- a simpler native/vector version is more editable and accurate


