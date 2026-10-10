# Four-stage workflow contract

## 0. Contract

Read materials in visual order. Record exact title, copy, digits, units, superscripts, footnotes, logos, product count, packaging reference, required people, room type, objects, platform UI, safe areas, sticker grouping, and spatial relations. Assign one production owner to each element. Treat the latest user correction as priority. Style references donate visual mechanisms, never unapproved claims, brands, products, or layout. Do not reproduce planning annotations.

Ask only when missing information would change product or person identity, offer mechanics, or asset structure. Infer routine art direction from the brief. An illustrative pack shot is not an instruction to place a physical product; record zero until the user or plan explicitly requires one.

Write a one-sentence concept, visual motif, hierarchy, palette, material, stage form, and host/UI occupancy map. Preflight whether the composition can be separated into deliverable layers. Plan any host-stage overlap and title/sticker occlusion before generation.

## Phase 1: spatial composition and extraction

1. Generate the requested 9:16 directions. Each includes background, top title, planned adult host preview, physical foreground stage, and only explicitly required products. Exclude non-title stickers and stage-face promotional copy.
2. Select the strongest valid direction by concept specificity, legibility, spatial clarity, brand/category connection, production feasibility, and product fidelity. For multiple directions, vary at least three systems; keep facts constant.
3. Before showing, derive clean pure background, title RGBA, physical stage/product RGBA, and host-preview RGBA where present. The stage may need front/back sublayers for natural occlusion; store their fixed order internally and offer a single stage asset only if that stacking reproduces the image. If it cannot, retain separate named layers and a stacking instruction rather than flattening an incorrect order.
4. Recompose from retained sources into `01-空间构图预览.jpg`. Verify copy, reference identity, protected products, edges, and reconstruction. Only this image may be approved.
5. Ask whether the present scene/title/host/stage/products direction is confirmed. Stop until explicit approval.

If extraction damages design or cannot reconstruct the draft, repair or regenerate Phase 1 before review. Do not defer this failure to Phase 4.

## Phase 2: sticker family

1. Build `02-贴片结构母板-16x9.jpg` with exact copy, grouping, ordering, and separate uncropped shapes on white.
2. Use structure board as numbered reference 1 for content and relationships; approved spatial preview as reference 2 for style system and occupied regions. Create a visual family of stickers only.
3. Correct all text deterministically where necessary. Prepare each styled module as an individual transparent asset; preserve combined modules as one asset. The approved `02-贴片设计母板-16x9.jpg` is assembled from these same assets.
4. Ask to confirm the styled sticker board. Stop until explicit approval.

## Phase 3: coordinate composition

Place individual approved sticker assets according to the plan, keeping scene/title/stage/product and host preview sources unchanged. Use deterministic transforms. Create `work/贴片定位层-9x16.png`, `work/贴片清单.json`, and `03-完整直播间预览.jpg` from the same operations. Inspect safe areas, order, contrast, occlusion, and exact copy. Ask to confirm full visual and sticker positions. Stop until explicit approval.

## Phase 4: production

Publish approved sources as the layer spec defines. Make a 16:9 transparent atlas from the same approved stickers. Run layer and pixel comparison QA against the approved Phase 3 preview, using internal host-preview layer for comparison where applicable. Inspect the composite on screen. Do not silently redraw during separation.

## Approval and revision semantics

Explicit `确认`, `通过`, `定稿`, `继续下一步` (or equivalents) authorizes the next phase only. A question, partial approval, requested change, or silence is not approval. Ask about only elements actually present; do not mechanically list products/people absent from the scene. Keep the three approval gates even if the user asks for several directions.

Route background/title/host/stage/product revisions to Phase 1, sticker design/copy/grouping to Phase 2, and sticker coordinate/scale to Phase 3. After upstream changes, revalidate and reapprove affected downstream work. For local edits write: target and allowed change; old state to remove; new state; locked properties. If two edits drift, rebuild only the affected asset or phase. Never replace a previously approved full image with a fresh generation for a small placement fix.
