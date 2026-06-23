# Progressive Foundation Workflow

Use this workflow when rebuilding one or more UI screenshots into editable Figma screens.

The foundation is progressive:

```text
Discovery -> Candidate -> Validated -> Promoted
```

Do not treat first-pass AI analysis as a finished design system. Components, tokens, and assets become reusable only after comparison-based validation.

## 1. Reference Intake

Before any Figma edit, record:

- source reference path or Figma node id
- clean reference PNG path
- reference width and height
- UI bounds inside the source image
- target Figma frame id
- target width and height
- scale ratio, if source and target differ
- quality level: Draft, Development-ready, High-fidelity, or Pixel-critical
- source-of-truth level: original reference, clean export, accepted rebuild auxiliary, or unreviewed rebuild candidate

Reject references that include unrelated UI, neighboring frames, Figma panels, chat UI, browser chrome, desktop background, or accidental whitespace.

When a high-fidelity/original UI reference exists, use it as the only authority for visual tokens, colors, typography, shadows, radii, spacing, and asset crop targets. Rebuilt pages are allowed as auxiliary evidence for editable structure, naming, and already accepted local repairs, but not as the global visual standard.

## 2. Foundation Discovery

Inspect existing Figma content before creating anything:

- accepted screens
- existing pages named Design System, Components, Tokens, Assets, Library, or similar
- local variables and text styles
- recurring fills, strokes, radii, effects, fonts, sizes, and line heights
- recurring UI structures: buttons, chips, cards, tab bars, status bars, template cards, work cards
- recurring visual assets: logos, mascots, pet renders, thumbnails, decorative marks

If no formal library exists, use accepted pages and clean references as evidence, not as unquestioned truth.

## 3. Foundation Artifacts

Organize work into four artifact layers, but create them progressively:

- Visual Spec: discovered color, type, radius, shadow, spacing, icon, and page-size rules.
- Component Library: repeated native UI patterns only after validation.
- Asset Library: reusable images/cutouts only after crop, alpha, and placement are verified.
- Editable Screens: rebuilt pages; page-local elements are allowed when they are more faithful.

Use pages or sections with clear names when the Figma file needs visible organization:

```text
00 Visual Spec
01 Component Candidates
02 Asset Candidates
UI V7 Editable Screens
```

These pages are organizational aids, not proof of correctness. A candidate stored on a library page is still a candidate until comparison validates it.

## 4. Candidate Registry

Create a concise registry before rebuilding pages.

### Token Candidate

```text
Token: Primary / Teal
Value: #73BDB6
Usage: primary buttons, active chips
Sources: 02 Primary Button, 03 selected chips, 04 Generate Preview
Confidence: medium
Status: candidate
Decision: use locally; promote after comparison passes on 2+ screens
```

### Component Candidate

```text
Component: Primary Button
Common traits: teal fill, pill radius, white bold label, optional icon
Differences: icon varies, width varies by page
Sources: 02, 03, 04, 06
Status: candidate
Decision: create component only after dimensions and typography are validated
```

### Asset Candidate

```text
Asset: Brand Corgi Mascot
Type: generated pet image
Sources: Home hero, Remote hero
Crop/alpha risk: medium
Status: candidate
Decision: keep as page-local until crop and placement match in both pages
```

### Page-Local Exception

```text
Item: Result page pricing card thumbnail group
Reason: one-off layout and crop; global component may overfit
Status: page-local
Decision: rebuild locally; do not promote
```

## 5. Reuse Decision

Use this order:

1. Use approved/promoted tokens, components, and assets.
2. Use validated candidates when their source and target context match.
3. Use page-local editable reconstruction when a candidate may cause drift.
4. Extract a page-local image asset when the visual content is complex.

Never force a candidate component into a page if it makes the page less faithful.

## 6. Editable Screen Build

Build screen sections in this order:

1. frame background and safe area
2. status/navigation
3. primary content structure
4. cards, lists, and controls
5. text calibration
6. images and decorative assets
7. bottom navigation or fixed action areas

Calibrate typography early. Wrong font size, weight, or line height causes spacing drift across the whole page.

## 7. Validation

After each meaningful screen or section:

- export rebuilt screen
- generate full-page comparison
- generate local comparison crops
- classify defects
- fix targeted local areas
- re-export

Use `validation-loop.md` and `defect-taxonomy.md`.

## 8. Promotion

Promote only after validation:

- Token promotion: appears consistently and passes visual comparison.
- Component promotion: repeated structure, validated dimensions, variants identified, does not force mismatched pages.
- Asset promotion: reused, crop/alpha verified, placement stable, useful for handoff.

Promotion means later pages may reuse the item by default. Candidate means later pages may reference it but must verify it.

## 9. Demotion

Demote a promoted item when:

- reuse creates visible drift
- variants were under-modeled
- asset crop contains background contamination
- typography or spacing does not match local reference
- the item was overfit to a single page

Demotion is not failure. It prevents bad abstractions from spreading.

