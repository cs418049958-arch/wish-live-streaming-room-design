# Phase-specific ImageGen prompt patterns

Replace brackets with current-contract facts. Keep prompts brief and concrete; delete irrelevant blocks. The built-in image tool chooses its execution model, so do not put API parameters such as model, quality, or background flags in its prompt as if they were controls.

## Phase 1: spatial concept

```text
Create a polished 9:16 Chinese ecommerce livestream room spatial concept for [brand/category/campaign]. One visual idea: [single-sentence concept]. The planning image controls required content, relationships, and safe areas; design a new background composition unless close reproduction was requested.
References: image 1 = planning content and placement; image 2 = brand identity only; image 3 = physical product packaging only, if explicitly required; image 4 = adult host identity/wardrobe only, if required; image 5 = [specific material or lighting mechanism] only. Do not import reference copy or unrelated objects.
Scene and framing: [room type, architecture, camera, foreground/midground/background, materials, light, host/UI occupancy].
Top title: render exactly once "[exact short title]" at [region], with [hierarchy, logo, subtitle and permitted effects]. No extra text.
Host: [count, adult appearance, position, pose, scale or omit]. Stage: [shape, count, location, material and occlusion or omit].
Physical products: [zero, with no pack/model/placeholder OR exact count, reference, hierarchy, placement and association].
Keep [critical protected items]. No ordinary marketing stickers, stage-face offer copy, annotations, watermarks, invented claims.
```

For an explicitly seated host, add only the unoverridden frontal/center/near-table defaults. For 除螨喷雾, add **only** the conditional title-font requirement from its dedicated reference. After generation, verify title and product labels; correct exact type in editable overlays if needed.

## Phase 1: separation, one target per call

```text
Edit image 1, the selected spatial concept. Isolate only [top title OR stage and approved products OR adult host preview] on a genuinely transparent 9:16 canvas. Preserve the object's exact geometry, colors, position, lighting, and soft edges. Remove everything else. Do not recenter, restyle, add text, or paint a white/checkerboard background.
```

```text
Edit image 1 to remove only [title, host, stage/products] and naturally restore the pure scenery behind them. Keep camera, architecture, unaffected pixels, perspective, lighting, and background objects unchanged. No text, packs, stage, person, marketing stickers, blur patches, or ghost edges.
```

If a protected pack/reference cannot be extracted faithfully, isolate the source product first and composite at the approved location; revise the preview before its approval. Rebuild the Phase 1 preview from actual layers.

## Phase 2: sticker family

```text
Create a clean 16:9 asset board of Chinese ecommerce marketing sticker designs. Image 1 is the structure-board authority for exact sticker count, sequence, grouping, copy, numbers, and footnotes. Image 2 is only a palette/material/shape/typography reference from the approved room; do not reproduce its scenery, host, stage, or products.
Stickers, each appearing once: [ID, exact short text, grouping, main/sub role, approximate scale, outline]. Keep combined modules as one unit and independent ones separate, uncropped, with clear gutters. Use the room's [specific motif] across varied contour and material treatments. Reserve legible surfaces for dense contract text, which will be typeset exactly afterward.
Only isolated sticker assets on a neutral board. No room, person, physical stage/product, extra claim, decoration without a job, watermark.
```

Cut every final sticker into a transparent individual asset. Restore exact text deterministically where necessary. Assemble the approval board from those assets; do not ask a model to render a second approximate copy of the approved board.

## Local edit

```text
Edit image 1. Change only [one exact target] from [old state] to [new state]. Keep [specific protected objects, title/copy, identity, packaging, camera, lighting, coordinates] unchanged. Remove the old state completely. No additional objects or text.
```

Inspect the output against the input. If two scoped attempts damage locked content, rebuild only the affected asset/phase.

## Transparency

Ask the built-in tool for real transparent background and preserve the returned alpha. If direct transparency fails and a subject has no magenta, a uniform #FF00FF matte plus `chroma_to_alpha.py` is a repair path; inspect fine edges and translucent material. Never treat a painted checkerboard or opaque white as transparency.
