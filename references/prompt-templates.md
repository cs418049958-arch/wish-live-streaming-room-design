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

For an explicitly seated host and required foreground table, apply the unoverridden defaults in `references/seated-host-composition.md` and add: "Large close conversational presenter, centered frontal, crown at 28–32% height, head including hair 26–30% of canvas width, body including arms 55–60% of width, hands at 64–69% height. Back edge of tabletop at 66–69%, front edge at 74–78%; desk spans both side edges and its front continues below the bottom crop, filling the entire lower area. No visible desk bottom, feet, under-table gap, or floor strip below it. Preserve floor behind and beside the host. Keep natural proportions and tabletop contact." Adjust only attributes overridden by the current brief. When a manual composition is provided, use it as the layout authority and regenerate a seamless whole image without importing paste bands. For 除螨喷雾, add **only** the conditional title-font requirement from its dedicated reference. After generation, verify title and product labels; correct exact type in editable overlays if needed.

## Phase 4 only: separation after all approvals, one target per call

```text
Edit image 1, the fully approved final room master. Isolate only [top title OR stage and approved products OR adult host preview OR one marketing sticker] on a genuinely transparent 9:16 canvas. Preserve the object's exact geometry, colors, position, lighting, and soft edges. Remove everything else. Do not recenter, restyle, add text, or paint a white/checkerboard background.
```

```text
Edit image 1 to remove only [title, host, stage/products, marketing stickers] and naturally restore the pure scenery behind them. Keep camera, architecture, unaffected pixels, perspective, lighting, and background objects unchanged. No text, packs, stage, person, marketing stickers, blur patches, or ghost edges.
```

Use these separation prompts only in Phase 4 after full approval. If extraction is inaccurate, repair the affected asset and compare with the unchanged approved final master. Use protected source products when needed; obtain approval only if a visible design change is unavoidable.

## Phase 2: sticker family

```text
Create a clean 16:9 asset board of Chinese ecommerce marketing sticker designs on a SOLID PURE-WHITE (#FFFFFF) artboard. All external background and gutters must remain pure white: no cream tint, gradient, texture, shared floor, or scenery. Image 1 is the structure-board authority for exact sticker count, sequence, grouping, copy, numbers, and footnotes. Image 2 is only a palette/material/shape/typography reference from the approved room; do not reproduce its scenery, host, stage, or products.
Stickers, each appearing once: [ID, exact short text, grouping, main/sub role, approximate scale, outline]. Keep combined modules as one unit and independent ones separate and uncropped. Leave a pure-white moat of at least 4.5% of the canvas short edge (about 48px on a 1920×1080 board; prefer 48–64px or wider) between complete asset silhouettes on all four sides and at canvas edges, including shadows, borders, text and decoration. Rearrange or scale the layout to preserve those gaps without sacrificing readability. No touching, overlapping, shared bases, connected leaves/ribbons, or cross-group ornaments. Use the room's [specific motif] across varied contour and material treatments. Reserve legible surfaces for dense contract text, which will be typeset exactly afterward.
White is the ARTBOARD color, not a restriction on sticker fill. Give stickers substantial brand/style-colored backing blocks and broad title areas, comfortable internal padding and designed material depth; do not turn them into white-only panels with skinny outlines. If a blank report/certificate inset is required, keep that inset white and empty while allowing a colored title block and outer backing. Keep local shadows short and contained.
Only isolated sticker groups on this pure-white board. No room, person, physical stage/product, extra claim, decoration without a job, watermark.
```

Present the generated whole board for sticker-design approval. Correct visible text where necessary, but defer every sticker cutout and transparent asset until Phase 4.

## Phase 3: complete room placement preview

```text
Edit image 1, the approved whole spatial preview. Image 2 is the approved sticker design board, controlling sticker copy, grouping, shape, colors, and material only. Add each sticker once at [planned coordinates, scale, overlap]. Preserve the accepted background, title, host, stage, product identity/count, camera, and light. Respect [host motion and UI safe areas]. Return one complete 9:16 room image; do not separate elements or output production layers.
```

## Local edit

```text
Edit image 1. Change only [one exact target] from [old state] to [new state]. Keep [specific protected objects, title/copy, identity, packaging, camera, lighting, coordinates] unchanged. Remove the old state completely. No additional objects or text.
```

Inspect the output against the input. If two scoped attempts damage locked content, rebuild only the affected asset/phase.

## Transparency

Ask the built-in tool for real transparent background and preserve the returned alpha. If direct transparency fails and a subject has no magenta, a uniform #FF00FF matte plus `chroma_to_alpha.py` is a repair path; inspect fine edges and translucent material. Never treat a painted checkerboard or opaque white as transparency.
