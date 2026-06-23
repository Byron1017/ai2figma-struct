#!/usr/bin/env python3
"""Create side-by-side comparison sheets for UI rebuild QA.

Example:
  python make_comparison_sheet.py --reference ref.png --rebuilt rebuilt.png \
    --output comparison.png --crop "header:0,0,750,180"
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont


def parse_crop(value: str) -> tuple[str, tuple[int, int, int, int]]:
    try:
        name, coords = value.split(":", 1)
        x, y, w, h = [int(part.strip()) for part in coords.split(",")]
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            'Crop must use "name:x,y,w,h", for example "header:0,0,750,180".'
        ) from exc
    if w <= 0 or h <= 0:
        raise argparse.ArgumentTypeError("Crop width and height must be positive.")
    return name.strip() or "crop", (x, y, w, h)


def fit_width(image: Image.Image, width: int) -> Image.Image:
    if image.width == width:
        return image.copy()
    height = max(1, round(image.height * width / image.width))
    return image.resize((width, height), Image.Resampling.LANCZOS)


def crop_box(image: Image.Image, rect: tuple[int, int, int, int]) -> Image.Image:
    x, y, w, h = rect
    return image.crop((x, y, x + w, y + h))


def draw_label(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str) -> None:
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except OSError:
        font = ImageFont.load_default()
    draw.text(xy, text, fill=(30, 36, 42), font=font)


def panel_pair(
    reference: Image.Image,
    rebuilt: Image.Image,
    label: str,
    width: int,
    gutter: int,
    margin: int,
) -> Image.Image:
    ref_fit = fit_width(reference, width)
    reb_fit = fit_width(rebuilt, width)
    label_h = 34
    panel_h = label_h + max(ref_fit.height, reb_fit.height)
    panel_w = margin * 2 + width * 2 + gutter
    panel = Image.new("RGB", (panel_w, panel_h), (246, 248, 250))
    draw = ImageDraw.Draw(panel)
    draw_label(draw, (margin, 8), f"{label} / reference")
    draw_label(draw, (margin + width + gutter, 8), f"{label} / rebuilt")
    panel.paste(ref_fit.convert("RGB"), (margin, label_h))
    panel.paste(reb_fit.convert("RGB"), (margin + width + gutter, label_h))
    return panel


def compose_sheet(panels: Iterable[Image.Image], margin: int, gap: int) -> Image.Image:
    panel_list = list(panels)
    if not panel_list:
        raise ValueError("No panels to compose.")
    width = max(panel.width for panel in panel_list)
    height = margin * 2 + sum(panel.height for panel in panel_list) + gap * (len(panel_list) - 1)
    sheet = Image.new("RGB", (width, height), (236, 240, 244))
    y = margin
    for panel in panel_list:
        sheet.paste(panel, ((width - panel.width) // 2, y))
        y += panel.height + gap
    return sheet


def main() -> None:
    parser = argparse.ArgumentParser(description="Create UI rebuild comparison sheet.")
    parser.add_argument("--reference", required=True, help="Reference PNG path.")
    parser.add_argument("--rebuilt", required=True, help="Rebuilt/exported PNG path.")
    parser.add_argument("--output", required=True, help="Output comparison PNG path.")
    parser.add_argument("--width", type=int, default=360, help="Display width for each side.")
    parser.add_argument(
        "--crop",
        action="append",
        default=[],
        type=parse_crop,
        help='Optional repeated crop in "name:x,y,w,h" reference-pixel format.',
    )
    args = parser.parse_args()

    reference = Image.open(args.reference).convert("RGBA")
    rebuilt = Image.open(args.rebuilt).convert("RGBA")
    if reference.size != rebuilt.size:
        print(f"warning: image sizes differ: reference={reference.size}, rebuilt={rebuilt.size}")

    margin = 18
    gutter = 18
    gap = 22
    panels: list[Image.Image] = [
        panel_pair(reference, rebuilt, "full page", args.width, gutter, margin)
    ]

    for name, rect in args.crop:
        panels.append(
            panel_pair(
                crop_box(reference, rect),
                crop_box(rebuilt, rect),
                name,
                args.width,
                gutter,
                margin,
            )
        )

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    compose_sheet(panels, margin, gap).save(output)
    print(str(output))


if __name__ == "__main__":
    main()

