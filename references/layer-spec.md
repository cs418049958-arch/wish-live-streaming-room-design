# Four-Stage Production Layer Specification

## Contents

1. Canvases
2. Approval artifacts
3. Production assets
4. Layer ownership
5. Alignment and transparency
6. Validation

## 1. Canvases

### Coordinate canvas

- 1080 x 1920, ratio 9:16.
- Origin at top-left `(0, 0)`.
- `背景.jpg`, `顶部大标题.png`, `前景展台+产品.png`, optional `人物.png`, and `work/贴片定位层-9x16.png` use the full canvas.
- Never crop a coordinate layer to visible bounds or recenter its content.

### Sticker-atlas canvas

- 1920 x 1080, ratio 16:9.
- `贴片合集-16x9.png` is an asset sheet, not a coordinate layer.
- Place every sticker separately with transparent gutters and fully visible outer contours.
- Preserve module-internal scale and hierarchy; the sticker sheet may use a different global scale from the final 9:16 placement.

## 2. Approval artifacts

- `01-背景标题人物展台产品.jpg`: approved Phase 1 visual containing the spatial skeleton and foreground product presentation.
- `02-贴片结构母板-16x9.jpg`: neutral white content/relationship board.
- `02-贴片设计母板-16x9.jpg`: approved styled sticker board.
- `03-完整直播间预览.jpg`: approved final coordinate preview.

These are review artifacts and visual masters. They are not substitutes for transparent production assets.

## 3. Production assets

### `背景.jpg`

Include only scenic environment: architecture, floor, distant furniture, outdoor scenery, environmental light, and background decor.

Exclude title, logo, host, stage, products, stickers, reports, UI, and foreground marketing decoration.

Use opaque RGB JPEG at 1080 x 1920. Fill removed areas naturally without blur patches, silhouettes, clone seams, or holes.

### `顶部大标题.png`

Include:

- main title;
- title-bound logo;
- subtitle;
- header backing shape;
- decoration inseparable from the title system.

Exclude ordinary marketing stickers, host, physical stage, products, and scenery.

Use RGBA PNG at 1080 x 1920. Preserve approved coordinates.

### `前景展台+产品.png`

Include only:

- physical foreground table, counter, podium, plinth, or product stage;
- referenced hero and secondary products physically placed on or next to it;
- natural product-stage occlusion and shadows that belong to the foreground object group.

Exclude host, scene, title, marketing copy, labels, badges, evidence, and service modules. If a stage-face line is promotional copy, it belongs to the sticker system.

Use RGBA PNG at 1080 x 1920. Create it from the approved Phase 1 foreground assets and verify against Phase 3. Omit only when neither a stage nor a physical product exists.

### `贴片合集-16x9.png`

Include all approved non-title marketing stickers:

- selling-point labels;
- data modules;
- scene cards;
- picture-in-picture frames;
- proof or report panels;
- benefit strips;
- service icons;
- footnotes;
- sticker-bound small explanatory imagery.

Exclude title system, host, physical stage, hero products, and scenery.

Use RGBA PNG at 1920 x 1080. Stickers must not touch or overlap one another.

### `work/贴片定位层-9x16.png`

Include the same approved non-title stickers at their final Phase 3 coordinates on a 1080 x 1920 RGBA canvas. This is mandatory for validation and optional for user delivery.

### Optional `人物.png`

Create only when the user requests a fixed virtual host. Use 1080 x 1920 RGBA and preserve Phase 3 coordinates. A normal live-camera host preview is not a default production asset.

## 4. Layer ownership

Default runtime stack, back to front:

1. `背景.jpg`;
2. live camera host layer or optional `人物.png`;
3. `顶部大标题.png`;
4. `前景展台+产品.png`, when present;
5. `work/贴片定位层-9x16.png`.

When real-world occlusion requires a different order, document it in the visual contract and validate the intended stack.

## 5. Alignment and transparency

- Compare coordinate layers against `03-完整直播间预览.jpg` at 100% scale.
- Do not shift, scale, rotate, or reconstruct approved elements at nearby positions.
- Every PNG must have alpha 0 outside visible content and nonzero alpha on visible content.
- Preserve soft antialiased edges without white, black, checkerboard, or chroma halos.
- Transparent frames must retain transparent interiors when live video should show through.

## 6. Validation

Run:

`python scripts/validate_live_room_layers.py --background 背景.jpg --title 顶部大标题.png --sticker-atlas 贴片合集-16x9.png --positioned-stickers work/贴片定位层-9x16.png --stage-products 前景展台+产品.png --full 03-完整直播间预览.jpg --preview work/图层校验.jpg`

Omit `--stage-products` only when the plan has no physical stage or products. Add `--live 人物.png` only for a fixed virtual host.

If a keyed render must be converted:

`python scripts/chroma_to_alpha.py keyed.png output.png --key FF00FF`
