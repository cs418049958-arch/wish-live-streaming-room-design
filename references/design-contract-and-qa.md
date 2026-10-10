# Visual contract, creative direction, and QA

## Contract table

For each element record `id | exact copy/count | required source | reference role | owner | region/relationship | immutable after phase`. Use owners `scene`, `top-title`, `host-preview`, `physical-stage`, `physical-product`, `marketing-sticker`. An explanatory product image inside a sticker belongs to that sticker; a pack placed on the stage is physical. A line of promotional text visually embedded on a stage still belongs to a sticker or title layer.

Reference priority: latest user annotation or correction > explicit planning requirement > identity/packaging reference > current approved visual > earlier approved visual > style reference > model invention. A reference may control only its named role. The plan controls required room type and functional relationships; unless explicitly asked, do not trace its architecture, furniture coordinates, or colors.

Record `combined`, `independent`, `above/below`, `left/right`, `aligned`, `supported by`, `in front of`, `behind`, and `overlapping without covering copy` precisely. Mark presenter motion range and platform UI no-go zones. Distinguish fixed virtual host from temporary generated host.

## Creative decision

Write one sentence naming the campaign idea and physical/graphic mechanism (for example, a particular architectural curve continuing into title and badge contours). Choose a limited repeatable set of shapes, materials, and accents. Allocate one dominant focal point, one supporting information rhythm, usable negative space, and a foreground anchor. Judge at phone size as well as full resolution. Reject a card-wall, uniform rounded panels, flat logo strip, random confetti, or copy-heavy stage front. Avoid adding unrelated objects merely to show creativity.

For alternatives, keep locked content identical while varying at least three of architecture, camera depth, title structure, stage geometry, lighting, material, and sticker contour. Do not require a prescribed motif if the brand reference points elsewhere.

Seated presenter default applies only when no explicit contrary planning or user direction covers that attribute: frontal face/torso, centered camera axis, close conversational scale, symmetric straight-on table. An override may affect only one attribute; retain the others. Product count defaults to zero unless explicit inclusion is recorded. Never add packs, silhouettes, boxes, placeholders, or new claims to a zero-product scene.

## ImageGen and text QA

- Number every image and state its permitted job. Prevent a style reference from donating copy or products. Use generation for a new scene; use an edit target for changes to an approved image.
- Start prompts with intended image and main subject; then composition, style, exact short text, locks, and concise avoid list. Remove inactive-phase instructions.
- Quote each exact title or short sticker phrase and its count. Check all Chinese, numbers, units, brand names, and footnotes in the result. Use deterministic text compositing for dense or unstable wording; never fabricate data.
- For requested physical products, compare silhouette, cap/trigger, label hierarchy, color, count, scale, and stage association with the supplied reference. Prefer protected source cutouts when an exact pack must be preserved.
- For a local edit, request one change and check all invariants. Inspect the edited image before accepting it.

If the main product or room is explicitly 除螨喷雾, also apply the font-only pass/fail checks in `dust-mite-spray-title-system.md`. Do not apply that conditional to other categories.

## Gate QA

### Phase 1

- Required scene, title, host, stage, and explicitly placed products match content and layout; absent elements stay absent.
- Background differs structurally from the planning mockup unless replication was requested.
- Concept links title, scene, and foreground without sacrificing host/UI space.
- Product identity, exact count, anatomy, title text, safe areas, and natural overlap pass.
- Pure background inpaints removed areas cleanly. RGBA title/stage/host edges have no halo, matte, clipped contour, or unintended pixels. Internal recomposite reproduces the preview.

### Phase 2

- Every module has one ID and correct grouping, sequence, text, unit, footnote, shape, and alpha cutout.
- Atlas-ready assets reconstruct the styled board; no room/host/stage/physical product contaminates the sticker assets.
- Hierarchy works at phone size; silhouettes vary purposefully; no copy is unreadable.

### Phase 3

- Approved Phase 1 and 2 pixels remain stable. Sticker coordinates, scale, hierarchy, gaps, UI avoidance, and occlusion match plan.
- The positioned layer is built from the same sticker files and transforms used by the preview.
- No old position, duplicate, hidden footnote, or unsupported claim remains.

### Production and regression

- Approved copy, identity, product count, and relationships survive every revision.
- The validator passes dimensions, alpha, manifest coverage, and full-preview comparison. Inspect the difference image and layered preview visually.
- Keep a preview-only host out of the production delivery while using its retained layer for reconstruction QA. If stage/host occlusion needs multiple sublayers, deliver the needed stack with explicit order.
