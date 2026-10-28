---
name: wish-live-streaming-room-design-gpt6
description: Design production-ready 9:16 Chinese ecommerce livestream rooms from planning screenshots, PPTs, spreadsheets, brand and product references. Use for Wish livestream room creation or revision requiring a unified scene, title, host preview, foreground stage, exact marketing stickers, staged approvals, and coordinate-locked transparent production layers. Apply ImageGen reference roles, scoped edits, deterministic text and compositing, and reconstruction QA.
---

# Wish 直播间设计 GPT-6

Create an original, coherent livestream visual and deliver assets that reconstruct its approved preview. Keep four stages: (1) spatial composition, (2) sticker family, (3) final placement, (4) production assets. **Generate whole-image previews directly with ImageGen first. Start all production separation only after the user has approved the spatial composition, sticker design, and complete room.** Do not extract background, title, stage, host, or sticker RGBA assets during Phases 1–3, even internally. Preserve the approved whole image as the master; verify reconstruction after separation in Phase 4.

## Read as needed

- `references/workflow-contract.md`: stage gates, interpretation, revisions, approvals. Read for every task.
- `references/design-contract-and-qa.md`: concept, priority, asset ownership, QA. Read for every task.
- `references/prompt-templates.md`: phase-specific ImageGen and edit prompts. Read before generation.
- `references/seated-host-composition.md`: host scale/position and full-bleed bottom table. Read before every seated-host Phase 1 generation; inspect its composition-only image when bundled. If the image is absent, apply the written landmark table and current user references without blocking generation.
- `references/layer-spec.md`: dimensions, alpha, manifest, validation. Read before Phase 4 separation and delivery.
- `references/dust-mite-spray-title-system.md`: **only** when main product/room is explicitly 除螨喷雾. It governs main-title font alone.

Inspect `assets/four-phase-reference/` only to clarify stage ownership. Never reuse its campaign, products, layout, or style.

## 0. Interpret and art-direct

1. Inspect every supplied page and image. Make a compact visual contract with exact copy, numbers, products, people, relationships, safe areas, reference roles, and evidence for each inclusion. Assign each element one owner: scene, top title, host preview, physical stage/product, or marketing sticker.
2. Distinguish explicit physical product placement from illustrative product imagery. Default to **zero physical products** unless user or planning text requires placement. Lock reference appearance and exact count when requested. Do not invent a host.
3. Resolve conflicts by latest user annotation, explicit plan, identity references, approved visual, then style references. Current user instructions override defaults. Redesign the planning background unless close reproduction was requested.
4. Write one sentence for the visual concept. Connect scene, title, stage, and stickers with a consistent motif and hierarchy. For alternatives, change at least three meaningful systems, such as architecture, title, stage, material/light; do not offer recolors as different directions.
5. Record host, product, stage, and UI regions and occlusion. A seated host defaults to frontal, centered, close to camera with a symmetrical straight-on table only where the plan provides no contrary pose, camera, placement, or table instruction. Preserve unoverridden attributes. Apply `references/seated-host-composition.md` from the first round: a proportionally large lower-middle presenter, tabletop near 67% canvas height, and a full-width desk front continuing beyond the bottom crop. Show required floor behind and beside the host, never as a strip below the desk.

## 1. Approve the spatial composition

Use ImageGen to directly generate a complete 9:16 spatial concept image containing scene, top title, required adult host preview, foreground stage, and **only explicitly required** physical products. Exclude ordinary marketing stickers and placeholders. Number every input image by role. Quote exact short title text and inspect it; typeset deterministically if inaccurate. The generated host is a live-camera preview surrogate unless a fixed virtual host is requested.

Inspect the generated whole image for copy, identity, composition, and occlusion, and present it as `01-空间构图预览.jpg`. Correct visible errors through scoped image edits or exact text correction as needed. Keep the approved flattened image as the Phase 1 master. Do not separate elements, inpaint a production background, or reconstruct layers at this stage.

Ask for confirmation of the actual elements present. Stop until explicit approval; edit the affected area of the whole image for Phase 1 revisions.

## 2. Approve the marketing sticker family

Make `02-贴片结构母板-16x9.jpg`: every sticker on a solid pure-white (#FFFFFF) 16:9 board with exact copy, grouping, sequence, and uncropped outlines. Use it as reference 1 for content and relationships; the approved Phase 1 preview is reference 2 for **style only** and occupied-space awareness. Generate the sticker shapes and material family separately from the room, host, stage, and products. Create purposeful differences in scale and contour.

Keep the **outer artboard and every inter-sticker gutter solid pure white (#FFFFFF)**, with no cream tint, gradient, texture, scenery, or shared ground shadow. This applies to both the structure and designed boards, from the first Phase 2 generation. White artboard does **not** mean white-only stickers: retain substantial brand/style-colored backing blocks, broad title tabs, internal padding, and material depth; do not reduce designs to narrow outlines. Keep a requested blank report/certificate inset white while allowing its outer backing and title block to carry color.

Separate every independent sticker/group with a clear white moat on all four sides: minimum gap and outer margin **4.5% of the canvas short edge (about 48 px on a 1920×1080 board)**, aiming for 48–64 px or more. Measure between the complete extents, including shadow, decorative overshoot, border, and text. Keep explicitly combined modules as one group; give every independent report card its own moat. Confine shadows and decoration to their own asset; prohibit overlaps, tangent edges, connected leaves/ribbons, shared bases, or cropped outlines. Rearrange or proportionally scale the layout before generation to preserve both spacing and readable copy. Inspect these conditions before presenting a board; correct failures with whole-board ImageGen edits. These white-board rules concern Phase 2 previews; Phase 4 deliverables still require genuine transparency.

Quote short exact text once per sticker. Restore long or wrong Chinese copy, numerals, units, labels, and footnotes by deterministic typesetting on approved shapes. Present the whole ImageGen sticker board as `02-贴片设计母板-16x9.jpg`; do not cut out or prepare transparent sticker assets yet. Ask for sticker design confirmation; stop until explicit approval.

## 3. Approve placement

Use the approved Phase 1 whole image as the ImageGen edit target and the approved Phase 2 board as the sticker-design reference. Place the stickers at planned positions and show a complete room image, respecting host and platform UI safe areas. Preserve all other accepted elements with scoped edits; do not generate an unrelated replacement scene. Do not create transparent assets, a positioned production layer, or a production manifest yet.

Show the complete edited image as `03-完整直播间预览.jpg`. Ask for approval of full image and sticker positions; stop until explicit approval. A later Phase 1 or 2 revision reopens that phase and dependent approvals.

## 4. Separate, verify, and deliver — only after full approval

After all three approvals, extract the pure background, coordinate-locked title RGBA, stage/products RGBA when applicable, host-preview RGBA when present, and individual stickers from the approved final whole image. Inpaint exposed background areas, keep approved geometry and positions, and create the positioned sticker layer, atlas, and manifest. Use the earlier approved whole images as supplemental references when necessary. Recompose and compare against the unchanged approved final master; repair extraction rather than altering the master to make a check pass. If a visible design change is unavoidable, obtain approval for that change.

Use approved sources. Deliver `背景.jpg`, `顶部大标题.png`, `前景展台+产品.png` when applicable, `贴片合集-16x9.png`, and `03-完整直播间预览.jpg`. Retain `work/贴片定位层-9x16.png` and `work/贴片清单.json`. Retain `work/人物预览层.png` for QA when a generated host appears; deliver `人物.png` only for a requested fixed virtual host.

Coordinate layers are 1080×1920 at origin (0,0); atlas is 1920×1080 with transparent gutters. Inspect real alpha, text, packaging, edges, ownership, and UI clearance. Run `scripts/validate_live_room_layers.py` with approved full preview, sticker manifest, and preview host if present. Inspect reconstructed preview and difference report; correct mismatches before delivery. The script checks structure and pixels; visually review content and identity.

Use the `imagegen` skill and built-in ImageGen for generated images and edits. Inspect local edit targets with `view_image`. Request real transparency; use `scripts/chroma_to_alpha.py` only when an unavoidable chroma matte has no key color in the subject. Do not promise model or exact API parameters unavailable in the built-in tool. If the user explicitly chooses an API/model workflow, follow authorized controls and normalize delivery dimensions once.

Save task output to the user-selected directory, or `outputs/wish-live-streaming-room-design-gpt6/` in the workspace, with intermediates in `work/`. Do not claim completion without three explicit phase approvals and passing reconstruction review.
