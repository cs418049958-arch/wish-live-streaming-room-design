---
name: wish-live-streaming-room-design
description: Design high-impact, production-ready 9:16 ecommerce live-streaming rooms from planning screenshots, PPT drafts, spreadsheets, brand assets, product references, and visual references. Use a four-stage approval workflow that first confirms the background, title, host, foreground stage, and products in one composition, then confirms a 16:9 sticker asset board, the final sticker-coordinate composition, and production layers. Use when Codex must reduce ImageGen prompt overload, preserve exact planning relationships, create design-led marketing stickers, and deliver a pure background, transparent sticker atlas, transparent foreground stage-plus-products layer, and transparent top-title layer.
---

# Wish Live Streaming Room Design

Turn a rough livestream plan into a high-design 9:16 visual through four small, separately approved generation and composition stages. Generate the spatial skeleton—background, title, host, foreground stage, and only explicitly requested products—together in Phase 1 so their perspective and visual center are judged as one composition. Keep marketing stickers out of that call and design them separately in Phase 2.

## Required references

Read before acting:

- `references/workflow-contract.md`: four approval gates, stage ownership, revisions, and deliverables.
- `references/design-contract-and-qa.md`: visual contract, design-strength rules, and QA for each stage.
- `references/prompt-templates.md`: phase-specific ImageGen prompts.
- `references/layer-spec.md`: production layer ownership, dimensions, transparency, and validation.

Conditional reference:

- When the brief explicitly identifies the hero product or room as `除螨喷雾`, read and enforce the typography-only rules in `references/dust-mite-spray-title-system.md` before writing any Phase 1 prompt. This font-style rule is exclusive to dust-mite-removal spray rooms; it must not prescribe title-region coverage, palette, materials, lighting, backing shapes, or decoration, and must not apply to other product categories.

Inspect `assets/four-phase-reference/` when the supplied planning material resembles a planning-board workflow or when stage ownership is unclear. `背景+标题+人物+前景的展台和产品.png` demonstrates the required Phase 1 scope, while `贴片结构母板-16x9.jpg` demonstrates Phase 2 separation. Use them only to understand stage ownership. Never reuse their campaign copy, products, layout, or style.

## Non-negotiable workflow

### 0. Interpret and contract

1. Inspect every supplied planning page, annotation, product image, logo, person reference, and style reference.
2. Convert them into a visual contract: exact content, quantities, copy, reference purposes, element relationships, immutable items, safe areas, and final asset ownership.
3. Classify every element before generating:
   - `scene`;
   - `top title system`;
   - `host preview`;
   - `marketing sticker`;
   - `physical stage`;
   - `physical product`.
4. Treat the latest user annotation as the highest-priority spatial instruction. Do not allow a style reference to override planning content or relationships.
5. If the product category is `除螨喷雾`, add only the conditional title-font contract from `references/dust-mite-spray-title-system.md` to the immutable Phase 1 requirements and its QA checklist. Derive every color, material, title region, backing shape, and decorative treatment from the current planning material and user references.
6. When the plan calls for a seated host and the user does not explicitly specify another camera or pose, apply the seated-host default: center the host on the camera axis; keep the face, torso, seated pose, and shoulder line square to the lens; render the foreground table as a left-right-symmetrical straight-on front view; and move the host-table group toward the camera so the table reads as a close foreground anchor rather than a small midground prop. Treat any later explicit request for an off-center host, side pose, three-quarter view, or oblique table as an override.
7. Treat the planning draft as content and functional authority, not as a default background visual to reproduce. Preserve its required room type, business relationships, host pose, mandatory objects, and safe areas, but redesign the background layout, furniture arrangement, perspective depth, material system, lighting, and thematic decoration. Reject a first-pass background that mainly traces the plan, swaps colors, or changes only small decor. Allow close reproduction only when the user explicitly requests it.
8. Set the Phase 1 physical-product count to `0` by default. A product shown incidentally or illustratively in the planning draft does not authorize product inclusion. Add physical products only when the user or planning text explicitly requires them, then lock the specified references and exact count. Otherwise keep every table and stage free of product packs, models, silhouettes, and placeholders throughout later revisions.

### 1. Spatial-skeleton approval

Generate one 9:16 approval image, or the requested number of genuinely different Phase 1 directions. Every candidate may contain only:

- background environment and spatial perspective;
- top title system, title-bound logos, subtitle, and header decoration;
- adult host or hosts only when the plan calls for people;
- physical foreground stage, counter, table, plinth, or product stand when the plan calls for it;
- referenced hero and secondary products only when explicitly requested, with exact count, packaging, scale, hierarchy, placement, and stage association; otherwise no physical product of any kind;
- palette, lighting, material language, depth, host safe area, and platform-UI safe area.

Exclude all non-title marketing stickers. Do not place temporary copy cards on the stage. Save as `01-背景标题人物展台产品.jpg`.

Run Phase 1 QA, show the image, and ask exactly:

`是否确认当前背景、标题、人物、前景展台与产品方向？确认后我将设计16:9贴片母板。`

Stop. Until explicit approval, revise only Phase 1.

### 2. Sticker asset-board approval

1. Extract every marketing sticker from the visual contract into a clean `1920 x 1080` white structure board. Keep every sticker visible, separated, uncropped, and labeled by its exact copy and grouping. Save as `02-贴片结构母板-16x9.jpg`.
2. Use that board as ImageGen reference image 1. Use the approved Phase 1 image only as the style-system reference; its stage and products establish available sticker space but must not be copied onto the board.
3. Ask ImageGen to redesign the sticker family while preserving exact quantity, copy, order, grouping, independent-versus-combined state, and internal hierarchy. Do not generate a room, host, stage, or physical product in this call.
4. If ImageGen alters Chinese copy, numbers, units, or footnotes, keep its approved shape and material design but restore the exact text with deterministic typesetting before review. Never approve garbled text.
5. Save the styled result as `02-贴片设计母板-16x9.jpg`.

Run Phase 2 QA, show the board, and ask exactly:

`是否确认当前贴片设计？确认后我将按策划稿位置合成完整直播间预览。`

Stop. Until explicit approval, revise only the sticker board. Do not alter approved Phase 1.

### 3. Coordinate composition approval

1. Use the approved Phase 1 visual—including its locked foreground stage and products—as the unchanged base.
2. Place the approved stickers according to the plan without moving, replacing, duplicating, or regenerating the approved stage or products.
3. Prefer deterministic layer composition. Do not use full-image ImageGen regeneration merely to place assets. If one sticker needs perspective integration, edit only that sticker with a strict whitelist.
4. Create both:
   - `03-完整直播间预览.jpg`;
   - internal `work/贴片定位层-9x16.png`, containing all non-title marketing stickers at final coordinates on a full transparent 1080 x 1920 canvas.

Run Phase 3 and regression QA, show the preview, and ask exactly:

`是否确认当前完整成品及贴片位置？确认后我将输出透明贴片合集、纯背景、前景展台+产品和顶部大标题。`

Stop. Until explicit approval, revise only composition, scale, or the affected previously approved asset. Never silently redesign Phase 1 or Phase 2.

### 4. Production separation

Use the latest explicitly approved Phase 3 preview and its approved source assets as the sole production master. Output:

- `贴片合集-16x9.png`: all approved non-title marketing stickers, separated on one transparent 1920 x 1080 canvas;
- `背景.jpg`: pure 1080 x 1920 scene with no title, host, stickers, stage, or products;
- `前景展台+产品.png`: coordinate-locked 1080 x 1920 transparent layer containing the approved physical foreground stage and referenced products; this is required whenever either appears in Phase 1;
- `顶部大标题.png`: coordinate-locked 1080 x 1920 transparent layer containing the approved top title system and title-bound logos, subtitle, and decoration.

Retain `work/贴片定位层-9x16.png` for validation and provide it when the user requests a one-click positioned overlay or editable placement reference. A generated host is a composition surrogate for the live camera and is not a default production asset; output `人物.png` only when the user explicitly needs a fixed virtual host.

Run `scripts/validate_live_room_layers.py` and inspect its composite preview. Use `scripts/chroma_to_alpha.py` when a generated PNG has an opaque chroma matte. Do not redesign, restyle, reframe, or move approved elements during separation.

## Image generation rules

- Use the `imagegen` skill and ImageGen for every generative image creation or edit. Inspect each local target with `view_image` before editing.
- Keep each ImageGen prompt phase-specific. Never include inactive-phase requirements “for completeness”; the staged workflow exists to prevent long-prompt omissions.
- In Phase 2, the white structure board must be reference image 1 and the approved Phase 1 visual must be used only to transfer palette, material, contour, typography, decorative rhythm, and awareness of the occupied foreground area.
- Repeat the current immutable-element list in every revision prompt. After each edit, verify the requested change and every previously correct locked item.
- For a seated host, repeat the centered frontal host, camera-square shoulder line, symmetrical straight-on table, and close-foreground distance in the immutable list unless the user explicitly overrides one of them.
- In every first-pass Phase 1 prompt, state that the planning draft controls required content and relationships but must not donate its background composition. Require a visibly new spatial layout, furniture arrangement, depth, material, lighting, and decor system unless the user explicitly requests replication.
- In every first-pass Phase 1 prompt, set physical products to `0` unless explicit inclusion is recorded in the visual contract. When the count is `0`, repeat “no pack, product model, silhouette, or placeholder” in all later Phase 1 edit locks.
- Require natural adult anatomy, correct Chinese, exact product counts, clear packaging, safe margins, and a usable host area.
- Reject repeated pure-white rounded cards, default-office typography, flat banner titles, equal-weight modules, and unrelated decorative stickers.
- For a `除螨喷雾` room, reject Phase 1 before presentation when any dedicated title-font guardrail in `references/dust-mite-spray-title-system.md` fails. Do not defer a typography problem to a later phase.
- Do not treat a white, black, checkerboard, or chroma matte as transparency. Every PNG production layer must contain a real alpha channel with both transparent and visible pixels.

## Output location

Use the user-selected directory. If none is provided, use `outputs/wish-live-streaming-room-design/` under the current workspace. Keep temporary boards, masks, keyed renders, and previews in `work/`.

## Completion criteria

Do not claim completion unless:

- the user explicitly approved Phases 1, 2, and 3 in sequence;
- every phase passed its content, relationship, design-strength, and regression QA;
- the final preview preserves the approved Phase 1 scene, title, host, foreground stage, products, and the approved Phase 2 sticker system;
- `背景.jpg`, `前景展台+产品.png` when applicable, `顶部大标题.png`, and `work/贴片定位层-9x16.png` are coordinate-locked at 1080 x 1920;
- `贴片合集-16x9.png` is 1920 x 1080 with separated, uncropped sticker assets;
- all PNGs use true transparency;
- the composite preview shows no coordinate drift, opaque matte, clipped edges, missing modules, or layer contamination.
