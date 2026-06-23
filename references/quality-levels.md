# Quality Levels

Use the requested quality level to decide how much validation and correction is required.

## Draft

Goal:
- communicate structure and direction

Allowed:
- approximate spacing
- placeholder icons
- rough image placement

Required:
- text is editable
- major sections exist
- no full-page screenshot as final UI

## Development-ready

Goal:
- support developer handoff and ordinary design edits

Required:
- text, cards, buttons, tags, navigation, and controls are editable
- repeated colors and text styles are reasonably consistent
- complex visuals are separate image assets
- no obvious missing assets
- no obvious overlap or clipping
- at least one full-page comparison exists

Allowed:
- small icon differences
- minor spacing differences
- page-local components when library confidence is low

## High-fidelity

Goal:
- closely match the reference while staying editable

Required:
- full-page comparison
- local comparisons for top nav, primary content, cards, controls, bottom area, and complex assets
- typography tuned against reference
- image crops and masks tuned
- visible major defects fixed
- candidate/promoted status recorded for reused tokens/components/assets

Allowed:
- tiny rendering differences from fonts or antialiasing
- explicit page-local exceptions

## Pixel-critical

Goal:
- push as close as practical to screenshot fidelity

Required:
- repeated export/compare/fix cycles
- defect log per iteration
- local crop checks for all visually dense sections
- imageHash and scaleMode verification for assets
- explicit residual mismatch report

Allowed:
- only documented differences caused by platform rendering, unavailable fonts, or deliberate editability tradeoffs

## Stop Rule

Do not claim "100%" without evidence. Say what was compared, what passed, and what residual risks remain.


