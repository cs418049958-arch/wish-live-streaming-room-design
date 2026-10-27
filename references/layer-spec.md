# Production layers and reconstruction

**Apply this specification only in Phase 4, after spatial, sticker, and complete-room approvals. Phases 1–3 use whole-image previews without production separation.**

## Canvases and ownership

Final coordinate canvas: 1080×1920, (0,0) top-left. Use this full canvas for `背景.jpg`, `顶部大标题.png`, `前景展台+产品.png` where applicable, `work/贴片定位层-9x16.png`, and internal `work/人物预览层.png` where applicable. Do not trim or recenter. Sticker atlas: 1920×1080 with alpha gutters. An atlas is an asset sheet, not a positioned layer.

- `背景.jpg`: pure opaque environment, with title/host/stage/product/stickers removed and revealed areas inpainted.
- `顶部大标题.png`: title, title-bound logo, subtitle, backing, integral title decoration; nothing else.
- `前景展台+产品.png`: physical stage and explicitly requested physical products, with their attached shadows; no marketing copy. Omit only when both are absent.
- `work/人物预览层.png`: generated host surrogate for visual approval and comparison, never a default delivered asset. A requested fixed virtual host may be published as `人物.png`.
- `贴片合集-16x9.png`: separately framed approved marketing stickers, complete and uncropped; no title, scenery, stage, physical product, or host.
- `work/贴片定位层-9x16.png`: stickers extracted in Phase 4 and placed to match the approved Phase 3 final coordinates.

Default preview stack back-to-front: background, preview/live host, top title, stage/products, positioned stickers. If physical host-stage occlusion requires another order, split the stage into named front/back transparent sublayers and retain the stack in the contract; do not pretend one layer can reproduce an impossible interleave.

## Approval-to-separation rule

Use ImageGen whole images for Phase 1 spatial review, Phase 2 board review, and Phase 3 complete-room review. Keep them as approved references. Only after final approval, use the approved Phase 3 whole image as the separation authority and earlier approved whole images as supplemental references. Extract all production layers and sticker assets in Phase 4, then reconstruct and compare against the unchanged approved final master. Repair extraction errors without redrawing the accepted design or replacing its master with a reconstruction. Normalize built-in generated image dimensions to final coordinate canvases once, before extraction. When the user explicitly chooses an API with custom size controls, valid 9:16 and 16:9 generation sizes include 1152×2048 and 2048×1152; resize to final delivery dimensions once.

Each transparent PNG must have real alpha zero outside visible objects and nonzero within. Inspect semitransparent glass, glow, hair, shadows, rounded contours, chroma spill, clipped edges, and title/sticker counters. Inpaint pure background behind removed items. A matting key is a fallback only.

## Sticker manifest

Create `work/贴片清单.json` with an array of approved sticker IDs and atlas boxes plus final positioned boxes. Values are pixel edges `[left, top, right, bottom]` in corresponding canvases. Example:

```json
{
  "stickers": [
    {"id": "main-benefit", "atlas_bbox": [24, 32, 640, 310], "position_bbox": [44, 620, 720, 890]}
  ]
}
```

Combined modules have one ID. Keep all atlas boxes nonoverlapping, inside bounds, and padded from canvas edges; positioned boxes may overlap intentionally. This manifest catches missing asset slots and unexplained visible pixels; manually inspect exact copy and duplicates because pixel checks cannot establish semantic correctness.

## Validate

```bash
python scripts/validate_live_room_layers.py \
  --background 背景.jpg --title 顶部大标题.png \
  --sticker-atlas 贴片合集-16x9.png \
  --positioned-stickers work/贴片定位层-9x16.png \
  --sticker-manifest work/贴片清单.json \
  --stage-products 前景展台+产品.png \
  --preview-host work/人物预览层.png \
  --full 03-完整直播间预览.jpg \
  --preview work/图层回拼.png --difference work/差异图.png
```

Omit stage and preview-host flags only when genuinely absent. Use `--live 人物.png` for a fixed virtual host instead of `--preview-host`. The script checks dimensions, alpha, manifest coverage, and difference against the approved preview using tolerance for JPEG encoding. Visually inspect both output images. If the preview contains a host but no retained preview host layer, reconstruction QA is incomplete: restore its preview layer before claiming completion.
