# Defect Taxonomy

Use this taxonomy when comparing rebuilt Figma output against the reference image.

## Severity

- Critical: breaks fidelity, editability, or development use; must fix.
- Major: clearly visible mismatch; fix before presenting as high-fidelity.
- Minor: visible on close inspection; fix if time/quality level requires.
- Note: acceptable difference or intentional implementation choice.

## Categories

### Reference

The source image is wrong or dirty.

Examples:
- neighboring frame included
- browser/Figma chrome included
- wrong scale or cropped bounds
- transparent background accidentally applied to whole screen

Fix:
- recreate clean reference before rebuilding

### Typography

Text does not match.

Examples:
- wrong font family
- wrong font size
- wrong weight
- wrong line height
- text overflow
- text baseline drift

Fix:
- calibrate against accepted text styles or local crop
- load correct font before editing

### Color And Contrast

Color, opacity, or contrast differs.

Examples:
- page background too warm/cold
- teal differs across pages
- card fill too gray
- shadow too heavy

Fix:
- extract token candidates from multiple sources
- tune local fill/stroke/effect
- promote token only after validation

### Spacing And Geometry

Layout dimensions differ.

Examples:
- card too wide
- row gap wrong
- button height wrong
- radius mismatch
- alignment drift

Fix:
- measure local crop
- adjust the specific container or component variant

### Image Crop

Image content is wrong but no background contamination exists.

Examples:
- pet too large
- thumbnail wrong focal point
- hero image clipped

Fix:
- adjust image frame, crop position, or scale
- use exact source crop for complex visuals

### Asset Contamination

Image asset includes unrelated UI or background.

Examples:
- rectangle background around transparent paw
- bottom tab crop includes content above
- screenshot includes neighboring card

Fix:
- recrop from clean reference
- validate alpha on light/dark/checkerboard
- verify imageHash and node target

### Missing Asset

An expected visual element is absent.

Examples:
- decorative sparkle missing
- guide icon missing
- pet thumbnail missing

Fix:
- classify whether it is vector, native, or image asset
- add page-local asset first; promote only if reused

### Wrong Abstraction

A reused component or asset causes drift.

Examples:
- global card component does not fit a special card
- one tab component forces wrong icon spacing
- promoted asset crop does not fit another page

Fix:
- demote item to candidate
- create variant or page-local reconstruction

### Layering And Overlap

Stacking order or clipping differs.

Examples:
- badge under image
- tab bar covers content
- shadow layer floats above text

Fix:
- inspect layer order
- verify masks/clipsContent
- fix parent/child relationship

### Editability

The visual match exists but Figma is not usable.

Examples:
- text flattened into bitmap
- button is an image slice
- cards are not editable

Fix:
- rebuild UI as native layers or component instances
- keep only complex content as image assets


