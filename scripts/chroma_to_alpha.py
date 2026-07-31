#!/usr/bin/env python3
"""Convert a solid chroma-key matte to a decontaminated RGBA PNG."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from PIL import Image


def parse_hex_color(value: str) -> np.ndarray:
    value = value.strip().lstrip("#")
    if len(value) != 6:
        raise argparse.ArgumentTypeError("key must be a 6-digit RGB hex color")
    try:
        return np.array([int(value[i : i + 2], 16) for i in (0, 2, 4)], dtype=np.float32)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("key must contain only hexadecimal digits") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Remove a uniform chroma-key background and write a true RGBA PNG."
    )
    parser.add_argument("input", type=Path, help="Opaque keyed source image")
    parser.add_argument("output", type=Path, help="RGBA PNG destination")
    parser.add_argument("--key", default="FF00FF", help="RGB key color in hex; default FF00FF")
    parser.add_argument(
        "--tolerance", type=float, default=42.0, help="Distance that becomes fully transparent"
    )
    parser.add_argument(
        "--softness", type=float, default=55.0, help="Additional distance used for a soft edge"
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    key = parse_hex_color(args.key)
    if args.tolerance < 0 or args.softness <= 0:
        raise SystemExit("tolerance must be >= 0 and softness must be > 0")

    source = Image.open(args.input).convert("RGBA")
    array = np.asarray(source).astype(np.float32)
    rgb = array[..., :3]
    original_alpha = array[..., 3] / 255.0

    distance = np.linalg.norm(rgb - key[None, None, :], axis=2)
    alpha = np.clip((distance - args.tolerance) / args.softness, 0.0, 1.0)
    alpha *= original_alpha

    safe_alpha = np.maximum(alpha[..., None], 1.0 / 255.0)
    recovered = (rgb - (1.0 - alpha[..., None]) * key[None, None, :]) / safe_alpha
    recovered = np.clip(recovered, 0.0, 255.0)
    recovered[alpha <= 0.0] = 0.0

    result = np.dstack((recovered, alpha[..., None] * 255.0)).astype(np.uint8)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(result, mode="RGBA").save(args.output)

    alpha_u8 = result[..., 3]
    visible = int(np.count_nonzero(alpha_u8))
    total = int(alpha_u8.size)
    print(
        f"WROTE {args.output} size={source.width}x{source.height} "
        f"alpha_min={int(alpha_u8.min())} alpha_max={int(alpha_u8.max())} "
        f"visible={visible}/{total}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
