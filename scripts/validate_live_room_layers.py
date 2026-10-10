#!/usr/bin/env python3
"""Check livestream layer structure, sticker manifest, and preview reconstruction."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageStat

COORD_SIZE = (1080, 1920)
ATLAS_SIZE = (1920, 1080)


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("background", "title", "sticker-atlas", "positioned-stickers",
                 "sticker-manifest", "full"):
        parser.add_argument(f"--{name}", type=Path, required=True)
    for name in ("stage-back", "stage-products", "preview-host", "live",
                 "preview", "difference"):
        parser.add_argument(f"--{name}", type=Path)
    parser.add_argument("--max-mean-error", type=float, default=10.0)
    parser.add_argument("--max-bad-fraction", type=float, default=0.02)
    parser.add_argument("--bad-pixel-threshold", type=int, default=40)
    return parser.parse_args()


def read_image(path: Path) -> Image.Image:
    image = Image.open(path)
    image.load()
    return image


def alpha_check(name: str, image: Image.Image, *, gutter: bool = False) -> list[str]:
    if image.mode not in ("RGBA", "LA"):
        return [f"{name}: expected a real alpha channel; mode={image.mode}"]
    alpha = image.getchannel("A")
    low, high = alpha.getextrema()
    errors = []
    if low != 0 or high == 0:
        errors.append(f"{name}: expected both transparent and visible pixels; alpha={low}..{high}")
    bounds = alpha.getbbox()
    if gutter and bounds and (bounds[0] == 0 or bounds[1] == 0
                              or bounds[2] == image.width or bounds[3] == image.height):
        errors.append(f"{name}: sticker atlas needs a transparent outer gutter")
    if alpha.histogram()[1:] and sum(alpha.histogram()[1:]) > image.width * image.height * 0.92:
        errors.append(f"{name}: nearly opaque layer suggests a painted matte")
    return errors


def parse_box(box: object, size: tuple[int, int], label: str) -> tuple[int, int, int, int]:
    if not isinstance(box, list) or len(box) != 4 or any(type(x) is not int for x in box):
        raise ValueError(f"{label}: expected four integer coordinates")
    left, top, right, bottom = box
    if not (0 <= left < right <= size[0] and 0 <= top < bottom <= size[1]):
        raise ValueError(f"{label}: box outside {size}: {box}")
    return left, top, right, bottom


def check_manifest(path: Path, atlas: Image.Image, positioned: Image.Image) -> list[str]:
    errors = []
    data = json.loads(path.read_text(encoding="utf-8"))
    stickers = data.get("stickers") if isinstance(data, dict) else None
    if not isinstance(stickers, list) or not stickers:
        return ["sticker-manifest: stickers must be a nonempty array"]
    seen = set()
    atlas_coverage = Image.new("L", atlas.size, 0)
    positioned_coverage = Image.new("L", positioned.size, 0)
    atlas_mask = Image.new("L", atlas.size, 0)
    atlas_draw = ImageDraw.Draw(atlas_coverage)
    pos_draw = ImageDraw.Draw(positioned_coverage)
    mask_draw = ImageDraw.Draw(atlas_mask)
    for index, sticker in enumerate(stickers):
        label = f"sticker[{index}]"
        if not isinstance(sticker, dict) or not isinstance(sticker.get("id"), str) or not sticker["id"]:
            errors.append(f"{label}: missing id")
            continue
        sticker_id = sticker["id"]
        if sticker_id in seen:
            errors.append(f"{label}: duplicate id {sticker_id}")
        seen.add(sticker_id)
        try:
            atlas_box = parse_box(sticker.get("atlas_bbox"), atlas.size, f"{label}.atlas_bbox")
            pos_box = parse_box(sticker.get("position_bbox"), positioned.size, f"{label}.position_bbox")
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if atlas_box[0] == 0 or atlas_box[1] == 0 or atlas_box[2] == atlas.width or atlas_box[3] == atlas.height:
            errors.append(f"{label}: atlas box lacks an outer gutter")
        if atlas_mask.crop(atlas_box).getbbox():
            errors.append(f"{label}: atlas box overlaps another sticker box")
        mask_draw.rectangle((atlas_box[0], atlas_box[1], atlas_box[2]-1, atlas_box[3]-1), fill=255)
        atlas_draw.rectangle((atlas_box[0], atlas_box[1], atlas_box[2]-1, atlas_box[3]-1), fill=255)
        pos_draw.rectangle((pos_box[0], pos_box[1], pos_box[2]-1, pos_box[3]-1), fill=255)
        if not atlas.getchannel("A").crop(atlas_box).getbbox():
            errors.append(f"{label}: empty atlas box")
        if not positioned.getchannel("A").crop(pos_box).getbbox():
            errors.append(f"{label}: empty positioned box")
    for label, image, coverage in (
        ("sticker-atlas", atlas, atlas_coverage),
        ("positioned-stickers", positioned, positioned_coverage),
    ):
        if ImageChops.subtract(image.getchannel("A"), coverage).getbbox():
            errors.append(f"{label}: visible pixels outside manifest boxes")
    print(f"MANIFEST {len(stickers)} sticker(s), {len(seen)} unique IDs")
    return errors


def compose(images: dict[str, Image.Image]) -> Image.Image:
    canvas = images["background"].convert("RGBA")
    for name in ("stage_back", "preview_host", "live", "title",
                 "stage_products", "positioned_stickers"):
        if name in images:
            canvas.alpha_composite(images[name].convert("RGBA"))
    return canvas


def save(image: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix.lower() in (".jpg", ".jpeg"):
        image.convert("RGB").save(path, quality=95)
    else:
        image.save(path)


def compare(composite: Image.Image, full: Image.Image, args: argparse.Namespace) -> list[str]:
    difference = ImageChops.difference(composite.convert("RGB"), full.convert("RGB"))
    if args.difference:
        # Boost subtle variation for visual inspection; metrics use the unmodified difference.
        boosted = difference.point(lambda value: min(255, value * 4))
        save(boosted, args.difference)
    means = ImageStat.Stat(difference).mean
    mean_error = sum(means) / 3
    r, g, b = difference.split()
    largest = ImageChops.lighter(ImageChops.lighter(r, g), b)
    bad = largest.point(lambda value: 255 if value > args.bad_pixel_threshold else 0)
    bad_fraction = bad.histogram()[255] / (full.width * full.height)
    print(f"RECONSTRUCTION mean_error={mean_error:.3f} bad_fraction={bad_fraction:.4%} "
          f"threshold={args.bad_pixel_threshold}")
    errors = []
    if mean_error > args.max_mean_error or bad_fraction > args.max_bad_fraction:
        errors.append("full: reconstructed preview differs from approved preview beyond tolerance")
    return errors


def main() -> int:
    args = arguments()
    if args.preview_host and args.live:
        print("FAIL choose --preview-host or --live, not both")
        return 1
    file_args = ("background", "title", "sticker_atlas", "positioned_stickers",
                 "full", "stage_back", "stage_products", "preview_host", "live")
    try:
        images = {name: read_image(getattr(args, name)) for name in file_args
                  if getattr(args, name) is not None}
    except (OSError, ValueError) as exc:
        print(f"FAIL unable to open image: {exc}")
        return 1
    errors = []
    size_errors = []
    for name, image in images.items():
        expected = ATLAS_SIZE if name == "sticker_atlas" else COORD_SIZE
        if image.size != expected:
            size_errors.append(f"{name}: expected {expected}, got {image.size}")
    errors.extend(size_errors)
    if images["background"].mode in ("RGBA", "LA") and images["background"].getchannel("A").getextrema() != (255, 255):
        errors.append("background: must be fully opaque")
    for name in ("title", "sticker_atlas", "positioned_stickers",
                 "stage_back", "stage_products", "preview_host", "live"):
        if name in images:
            errors.extend(alpha_check(name, images[name], gutter=name == "sticker_atlas"))
    if not errors:
        try:
            errors.extend(check_manifest(args.sticker_manifest, images["sticker_atlas"],
                                         images["positioned_stickers"]))
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"sticker-manifest: {exc}")
    if not size_errors:
        composite = compose(images)
        if args.preview:
            save(composite, args.preview)
            print(f"PREVIEW {args.preview}")
        errors.extend(compare(composite, images["full"], args))
    for error in errors:
        print(f"ERROR {error}")
    print(f"{'FAIL' if errors else 'PASS'} {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
