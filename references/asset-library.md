# Asset Library And Cutout Rules

Use this guide for photos, generated pets, mascots, thumbnails, decorative marks, and other visuals that should not be rebuilt as native UI.

## Asset Status

Use one of these statuses:

- page-local: used only in the current screen
- candidate: may be reused, but not validated enough for library use
- promoted: verified and safe to reuse by default
- rejected: bad crop, contaminated, wrong style, or no longer needed

## Asset Manifest

Record assets in this format:

```text
Asset: Corgi Hero
Status: candidate
Type: generated pet image
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

## Extraction Rules

- Extract only independent visual content.
- Do not extract text, cards, buttons, nav bars, tags, inputs, dividers, or page backgrounds.
- Use the smallest crop that contains intended pixels plus necessary soft edge or shadow.
- Preserve antialiasing, translucency, soft glow, and texture when they belong to the asset.
- Remove unrelated UI background pixels.
- If the reference asset is flat, keep it flat. Do not add 3D, bevel, gradient, or cute extra details.
- Validate transparent assets on checkerboard, dark, and light backgrounds.

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
- color/contrast differs from reference
- it forces wrong placement in another page
- a simpler native/vector version is more editable and accurate


