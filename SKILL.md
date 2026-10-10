---
name: wish-live-streaming-room-design-gpt6
description: Design production-ready 9:16 Chinese ecommerce livestream rooms from planning screenshots, PPTs, spreadsheets, brand and product references. Use for Wish livestream room creation or revision requiring a unified scene, title, host preview, foreground stage, exact marketing stickers, staged approvals, and coordinate-locked transparent production layers. Apply ImageGen reference roles, scoped edits, deterministic text and compositing, and reconstruction QA.
---

# Wish 直播间设计 GPT-6

Create an original, coherent livestream visual and deliver assets that reconstruct its approved preview. Keep four stages: (1) spatial composition, (2) sticker family, (3) final placement, (4) production assets. Do internal extraction and reconstruction **before** the relevant approval. Never ask the user to approve pixels that cannot be reproduced from the deliverable layers.

## Read as needed

- `references/workflow-contract.md`: stage gates, interpretation, revisions, approvals. Read for every task.
- `references/design-contract-and-qa.md`: concept, priority, asset ownership, QA. Read for every task.
- `references/prompt-templates.md`: phase-specific ImageGen and edit prompts. Read before generation.
- `references/layer-spec.md`: dimensions, alpha, manifest, validation. Read before Phase 1 extraction and Phase 4.
- `references/dust-mite-spray-title-system.md`: **only** when main product/room is explicitly 除螨喷雾. It governs main-title font alone.

Inspect `assets/four-phase-reference/` only to clarify stage ownership. Never reuse its campaign, products, layout, or style.

## 0. Interpret and art-direct

1. Inspect every supplied page and image. Make a compact visual contract with exact copy, numbers, products, people, relationships, safe areas, reference roles, and evidence for each inclusion. Assign each element one owner: scene, top title, host preview, physical stage/product, or marketing sticker.
2. Distinguish explicit physical product placement from illustrative product imagery. Default to **zero physical products** unless user or planning text requires placement. Lock reference appearance and exact count when requested. Do not invent a host.
3. Resolve conflicts by latest user annotation, explicit plan, identity references, approved visual, then style references. Current user instructions override defaults. Redesign the planning background unless close reproduction was requested.
4. Write one sentence for the visual concept. Connect scene, title, stage, and stickers with a consistent motif and hierarchy. For alternatives, change at least three meaningful systems, such as architecture, title, stage, material/light; do not offer recolors as different directions.
5. Record host, product, stage, and UI regions and occlusion. A seated host defaults to frontal, centered, close to camera with a symmetrical straight-on table only where the plan provides no contrary pose, camera, placement, or table instruction. Preserve unoverridden attributes.

## 1. Approve the spatial composition

Create a 9:16 concept containing scene, top title, required adult host preview, foreground stage, and **only explicitly required** physical products. Exclude ordinary marketing stickers and placeholders. Number every input image by role. Quote exact short title text and inspect it; typeset deterministically if inaccurate. The generated host is a live-camera preview surrogate unless a fixed virtual host is requested.

Before showing the image, internally derive a pure background, coordinate-locked title RGBA, stage-plus-products RGBA when applicable, and host-preview RGBA when a generated host appears. Inpaint newly exposed background areas, preserve accepted object edges, then recompose **from those very layers**. Fix extraction, copy, occlusion, and drift before presenting `01-空间构图预览.jpg`. An attractive flattened image alone cannot pass. The approved reconstructed preview is the Phase 1 master.

Ask for confirmation of the actual elements present. Stop until explicit approval; rebuild affected layers for Phase 1 revisions.

## 2. Approve the marketing sticker family

Make `02-贴片结构母板-16x9.jpg`: every sticker on a neutral 16:9 board with exact copy, grouping, sequence, and uncropped outlines. Use it as reference 1 for content and relationships; the approved Phase 1 preview is reference 2 for **style only** and occupied-space awareness. Generate the sticker shapes and material family separately from the room, host, stage, and products. Create purposeful differences in scale and contour.

Quote short exact text once per sticker. Restore long or wrong Chinese copy, numerals, units, labels, and footnotes by deterministic typesetting on approved shapes. Prepare separable RGBA sticker assets internally and build `02-贴片设计母板-16x9.jpg` **from those assets**. Ask for sticker design confirmation; stop until explicit approval.

## 3. Approve placement

Composite approved Phase 1 layers and sticker assets at planned coordinates, respecting host and platform UI safe areas. Build `work/贴片定位层-9x16.png` from the same placed instances. Avoid full-frame ImageGen regeneration for placement. A local perspective or occlusion edit must change only its sticker asset and be checked against locked items.

Show `03-完整直播间预览.jpg` made by deterministic compositing. Ask for approval of full image and sticker positions; stop until explicit approval. A later Phase 1 or 2 revision reopens that phase and dependent approvals.

## 4. Deliver and verify

Use approved sources. Deliver `背景.jpg`, `顶部大标题.png`, `前景展台+产品.png` when applicable, `贴片合集-16x9.png`, and `03-完整直播间预览.jpg`. Retain `work/贴片定位层-9x16.png` and `work/贴片清单.json`. Retain `work/人物预览层.png` for QA when a generated host appears; deliver `人物.png` only for a requested fixed virtual host.

Coordinate layers are 1080×1920 at origin (0,0); atlas is 1920×1080 with transparent gutters. Inspect real alpha, text, packaging, edges, ownership, and UI clearance. Run `scripts/validate_live_room_layers.py` with approved full preview, sticker manifest, and preview host if present. Inspect reconstructed preview and difference report; correct mismatches before delivery. The script checks structure and pixels; visually review content and identity.

Use the `imagegen` skill and built-in ImageGen for generated images and edits. Inspect local edit targets with `view_image`. Request real transparency; use `scripts/chroma_to_alpha.py` only when an unavoidable chroma matte has no key color in the subject. Do not promise model or exact API parameters unavailable in the built-in tool. If the user explicitly chooses an API/model workflow, follow authorized controls and normalize delivery dimensions once.

Save task output to the user-selected directory, or `outputs/wish-live-streaming-room-design-gpt6/` in the workspace, with intermediates in `work/`. Do not claim completion without three explicit phase approvals and passing reconstruction review.
