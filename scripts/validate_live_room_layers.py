#!/usr/bin/env python3
"""Validate four-stage livestream-room production assets and render a preview."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageChops


COORDINATE_SIZE = (1080, 1920)
ATLAS_SIZE = (1920, 1080)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate a pure background, transparent title, transparent sticker atlas, "
            "positioned sticker layer, and optional stage-products/live layers."
        )
    )
    parser.add_argument("--background", type=Path, required=True)
    parser.add_argument("--title", type=Path, required=True)
    parser.add_argument("--sticker-atlas", type=Path, required=True)
    parser.add_argument("--positioned-stickers", type=Path, required=True)
    parser.add_argument("--stage-products", type=Path)
    parser.add_argument("--live", type=Path, help="Optional fixed virtual-host RGBA layer")
    parser.add_argument("--full", type=Path, help="Approved Phase 3 preview for size checks")
    parser.add_argument("--preview", type=Path, help="Optional JPEG or PNG composite preview")
    parser.add_argument(
        "--allow-proportional",
        action="store_true",
        help="Allow proportional 9:16 coordinate assets and a proportional 16:9 atlas",
    )
    return parser


def open_image(path: Path) -> Image.Image:
    if not path.is_file():
        raise ValueError(f"missing file: {path}")
    image = Image.open(path)
    image.load()
    return image


def ratio_matches(size: tuple[int, int], target: tuple[int, int]) -> bool:
    width, height = size
    target_width, target_height = target
    return width > 0 and height > 0 and abs(width / height - target_width / target_height) <= 0.002


def validate_size(
    name: str,
    image: Image.Image,
    expected: tuple[int, int],
    allow_proportional: bool,
) -> list[str]:
    if allow_proportional:
        if not ratio_matches(image.size, expected):
            return [f"{name}: expected ratio {expected[0]}:{expected[1]}, got {image.width}x{image.height}"]
        return []
    if image.size != expected:
        return [f"{name}: expected {expected[0]}x{expected[1]}, got {image.width}x{image.height}"]
    return []


def alpha_report(
    name: str,
    image: Image.Image,
    *,
    require_gutter: bool = False,
) -> tuple[list[str], str]:
    errors: list[str] = []
    if image.mode not in {"RGBA", "LA"}:
        return [f"{name}: missing alpha channel; mode is {image.mode}"], "no-alpha"

    alpha = image.getchannel("A")
    minimum, maximum = alpha.getextrema()
    bbox = alpha.getbbox()
    if minimum != 0:
        errors.append(f"{name}: no fully transparent pixels; alpha_min={minimum}")
    if maximum == 0:
        errors.append(f"{name}: layer is fully transparent")

    if bbox is None:
        bounds = "empty"
        coverage = 0.0
        errors.append(f"{name}: visible bounds are empty")
    else:
        bounds = str(bbox)
        histogram = alpha.histogram()
        visible = sum(histogram[1:])
        coverage = visible / (image.width * image.height)
        if coverage > 0.92:
            errors.append(f"{name}: visible coverage {coverage:.1%} suggests an opaque matte")
        if require_gutter:
            left, top, right, bottom = bbox
            if left <= 0 or top <= 0 or right >= image.width or bottom >= image.height:
                errors.append(f"{name}: visible content touches the canvas edge; transparent gutter required")

    return errors, f"alpha={minimum}..{maximum} bbox={bounds} visible={coverage:.1%}"


def require_opaque_background(image: Image.Image) -> list[str]:
    if image.mode not in {"RGBA", "LA"}:
        return []
    alpha = image.getchannel("A")
    opaque = Image.new("L", image.size, 255)
    if ImageChops.difference(alpha, opaque).getbbox():
        return ["background: must be fully opaque"]
    return []


def save_preview(
    background: Image.Image,
    title: Image.Image,
    positioned_stickers: Image.Image,
    stage_products: Image.Image | None,
    live: Image.Image | None,
    destination: Path,
) -> None:
    canvas = background.convert("RGBA")
    if live is not None:
        canvas.alpha_composite(live.convert("RGBA"))
    canvas.alpha_composite(title.convert("RGBA"))
    if stage_products is not None:
        canvas.alpha_composite(stage_products.convert("RGBA"))
    canvas.alpha_composite(positioned_stickers.convert("RGBA"))

    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.suffix.lower() in {".jpg", ".jpeg"}:
        canvas.convert("RGB").save(destination, quality=95)
    else:
        canvas.save(destination)


def main() -> int:
    args = build_parser().parse_args()
    paths = {
        "background": args.background,
        "title": args.title,
        "sticker_atlas": args.sticker_atlas,
        "positioned_stickers": args.positioned_stickers,
    }
    if args.stage_products:
        paths["stage_products"] = args.stage_products
    if args.live:
        paths["live"] = args.live
    if args.full:
        paths["full"] = args.full

    try:
        images = {name: open_image(path) for name, path in paths.items()}
    except (OSError, ValueError) as exc:
        print(f"FAIL {exc}")
        return 1

    errors: list[str] = []
    coordinate_names = ["background", "title", "positioned_stickers"]
    for optional_name in ("stage_products", "live", "full"):
        if optional_name in images:
            coordinate_names.append(optional_name)

    for name in coordinate_names:
        errors.extend(
            validate_size(name, images[name], COORDINATE_SIZE, args.allow_proportional)
        )
    errors.extend(
        validate_size(
            "sticker_atlas",
            images["sticker_atlas"],
            ATLAS_SIZE,
            args.allow_proportional,
        )
    )

    coordinate_size = images["background"].size
    for name in coordinate_names:
        if images[name].size != coordinate_size:
            errors.append(f"{name}: size {images[name].size} differs from background {coordinate_size}")

    alpha_targets = [
        ("title", False),
        ("sticker_atlas", True),
        ("positioned_stickers", False),
    ]
    if "stage_products" in images:
        alpha_targets.append(("stage_products", False))
    if "live" in images:
        alpha_targets.append(("live", False))

    for name, require_gutter in alpha_targets:
        layer_errors, report = alpha_report(
            name,
            images[name],
            require_gutter=require_gutter,
        )
        errors.extend(layer_errors)
        print(f"{name}: {report}")

    errors.extend(require_opaque_background(images["background"]))

    if args.preview and not errors:
        save_preview(
            images["background"],
            images["title"],
            images["positioned_stickers"],
            images.get("stage_products"),
            images.get("live"),
            args.preview,
        )
        print(f"PREVIEW {args.preview}")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"FAIL {len(errors)} validation error(s)")
        return 1

    print("PASS four-stage live-room production assets are structurally valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
