# Four-stage workflow contract

## 0. Contract

Read materials in visual order. Record exact title, copy, digits, units, superscripts, footnotes, logos, product count, packaging reference, required people, room type, objects, platform UI, safe areas, sticker grouping, and spatial relations. Assign one production owner to each element. Treat the latest user correction as priority. Style references donate visual mechanisms, never unapproved claims, brands, products, or layout. Do not reproduce planning annotations.

Ask only when missing information would change product or person identity, offer mechanics, or asset structure. Infer routine art direction from the brief. An illustrative pack shot is not an instruction to place a physical product; record zero until the user or plan explicitly requires one.

Write a one-sentence concept, visual motif, hierarchy, palette, material, stage form, and host/UI occupancy map. Preflight whether the composition can be separated into deliverable layers. Plan any host-stage overlap and title/sticker occlusion before generation.

## Phase 1: whole-image spatial composition

1. Directly generate the requested complete 9:16 spatial directions with ImageGen. Include background, top title, planned adult host preview, foreground stage, and only explicitly required products. Exclude non-title stickers and stage-face promotional copy. For a required seated presenter/table, use `references/seated-host-composition.md` in every initial alternative; lock presenter scale/landmarks and table side/bottom bleeds before generation.
2. For multiple directions, vary at least three systems while keeping facts constant. Show all requested valid alternatives for the user to select; assess concept specificity, legibility, space, brand/category connection, and product fidelity.
3. Inspect and correct visible copy, identity, anatomy, and occlusion, plus presenter scale/position and full-width bottom-filled table coverage. Present the generated whole image as `01-空间构图预览.jpg`. Do not extract any production elements, remove objects to create a pure background, or reconstruct a layered preview.
4. Ask whether the present scene/title/host/stage/products direction is confirmed. Stop until explicit approval. Retain the approved flattened image as the master.

## Phase 2: whole-board sticker design

1. Build `02-贴片结构母板-16x9.jpg` with exact copy, grouping, ordering, and uncropped shapes on solid pure white (#FFFFFF). Apply the Phase 2 white-artboard and spacing contract in SKILL.md: at least 4.5% of the canvas short edge between full asset extents and at the canvas edges.
2. Use this board as reference 1 for content and relationships; use the approved Phase 1 whole image as reference 2 for style and occupied regions. Generate a whole sticker design board with ImageGen. Keep the canvas/gutters pure white while designing substantial colored backplates inside the sticker silhouettes; reserve white only for explicitly blank report/certificate insets as required.
3. Correct text, board whiteness, and asset separation where necessary and present `02-贴片设计母板-16x9.jpg`. Check full silhouettes including decorations and shadows, not only panel rectangles. Do not extract individual stickers or prepare transparent assets before full approval.
4. Ask to confirm the styled sticker board. Stop until explicit approval.

## Phase 3: whole-image final placement

Use the approved Phase 1 whole image as the ImageGen edit target and the approved Phase 2 board as the sticker-design reference. Add the stickers at planned coordinates while preserving accepted scene/title/stage/products/host. Use scoped image edits for placement revisions; inspect all locked content for drift. Present the complete edited image as `03-完整直播间预览.jpg`. Check safe areas, contrast, order, occlusion, and exact copy. Ask to confirm the full visual and sticker positions. Stop until explicit approval. Do not extract elements, make transparent production layers, or build the production manifest yet.

## Phase 4: separation, reconstruction, and delivery

Only after all three approvals, separate elements from the approved final whole image, using earlier approved whole images as supplemental references. Extract pure background, title RGBA, physical stage/product RGBA, host-preview RGBA where present, and individual sticker RGBA assets. Inpaint revealed background areas and preserve approved object edges and coordinates. If host-stage overlap requires front/back stage sublayers, retain named layers and stacking instructions instead of an incorrect single flattened stage.

Create `work/贴片定位层-9x16.png`, `work/贴片清单.json`, and the transparent 16:9 sticker atlas. Reconstruct from these sources, compare with the unchanged approved Phase 3 master, and run the validator and visual QA. Repair separation mismatches; never replace the approved master with the reconstruction to force a pass. Ask for a scoped design approval only if extraction requires a visible design change. Deliver verified layers and the approved final preview.

## Approval and revision semantics

Explicit `确认`, `通过`, `定稿`, `继续下一步` (or equivalents) authorizes the next phase only. A question, partial approval, requested change, or silence is not approval. Ask about only elements actually present; do not mechanically list products/people absent from the scene. Keep the three approval gates even if the user asks for several directions.

Route background/title/host/stage/product revisions to Phase 1, sticker design/copy/grouping to Phase 2, and sticker coordinate/scale to Phase 3. After upstream changes, revalidate and reapprove affected downstream work. For local edits write: target and allowed change; old state to remove; new state; locked properties. If two edits drift, rebuild only the affected asset or phase. Use scoped ImageGen edits on the approved whole image for small placement fixes. Perform any affected separation again only after the revised full image is approved.
