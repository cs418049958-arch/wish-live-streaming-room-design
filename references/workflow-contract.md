# Four-Stage Workflow Contract

## Contents

1. Input interpretation
2. Visual-contract gate
3. Phase 1: spatial skeleton
4. Phase 2: sticker asset board
5. Phase 3: coordinate composition
6. Phase 4: production separation
7. Approval semantics
8. Revision routing
9. Content fidelity
10. Reference conflicts

## 1. Input interpretation

Read planning material in visual order and identify:

- brand, channel, campaign, product category, and audience;
- exact title, selling points, offer text, evidence text, footnotes, and disclaimers;
- product references, exact pack counts, hero/secondary hierarchy, and stage association;
- room type, camera, host count and styling, safe areas, and platform UI;
- every sticker, video window, scene card, benefit badge, report panel, and service module;
- references that are directional only and may not donate copy, brands, prices, products, or claims.

Remove planning grids, arrows, annotations, placeholders, crop borders, and reference watermarks from finished visuals. Ask only when a missing decision would materially change product identity, a real person's identity, the campaign mechanism, or the final asset structure.

## 2. Visual-contract gate

Before generation, complete the contract in `design-contract-and-qa.md`.

Record:

- every element, copy item, number, unit, marker, product count, and footnote;
- combined-versus-independent sticker behavior;
- exact adjacency, alignment, embedding, occlusion, and reading order;
- reference purpose and conflict priority;
- immutable items for later revisions;
- ownership as scene, title, host preview, marketing sticker, physical stage, or physical product.

Do not start from an unstructured summary. Do not allow one asset to belong to multiple production classes unless the contract explicitly describes a deliberate composite.

## 3. Phase 1: spatial skeleton

Generate `01-背景标题人物展台产品.jpg` at 1080 x 1920 or a proportional 9:16 size that is normalized once.

Include:

- scenic environment, lighting, depth, and perspective;
- top title system and title-bound logos, subtitle, and decoration;
- adult host preview when required;
- physical foreground stage, counter, table, podium, plinth, or product stand when required;
- referenced hero and secondary products with exact count, packaging, scale, hierarchy, coordinates, and stage association;
- live-host and platform-UI safe areas.

Exclude:

- all non-title marketing stickers;
- stage-face promotional copy, badges, data, reports, benefits, and service modules.

This phase decides spatial mood, title hierarchy, host styling, camera, palette, material language, foreground depth, product hierarchy, stage perspective, and product-stage association. Generate the foreground stage and products now so their silhouette, scale, occlusion, and visual center are evaluated before stickers are designed. Do not spend prompt budget on later-stage information modules.

After QA, ask:

`是否确认当前背景、标题、人物、前景展台与产品方向？确认后我将设计16:9贴片母板。`

Do not continue without explicit approval.

## 4. Phase 2: sticker asset board

### 4.1 Structure board

Create `02-贴片结构母板-16x9.jpg` at 1920 x 1080 on white:

- place every marketing sticker separately with generous spacing;
- preserve combined modules as one unit and independent modules as separate units;
- retain exact copy, numbers, order, labels, footnotes, and internal hierarchy;
- keep every outer contour fully visible;
- exclude room scenery, people, physical stage, and physical products;
- use neutral structure styling; this file controls content and relationships, not final aesthetics.

Sticker-integrated scene or product imagery may appear only when it is part of the sticker's approved information content. A physical hero product or stage is never reclassified as a sticker.

### 4.2 Styled board

Use the structure board as ImageGen reference image 1 and the approved Phase 1 image only as a style and occupied-space reference. Create `02-贴片设计母板-16x9.jpg`.

Transfer:

- palette;
- material;
- contour language;
- typography;
- edge treatments;
- decorative rhythm.

Do not transfer the Phase 1 room composition, stage, or products into the board. Do not merge stickers, omit long-copy modules, crop contours, invent claims, or add a host, stage, or physical product.

If ImageGen produces a strong sticker shape but changes Chinese copy, numbers, units, markers, or footnotes, retain the visual asset and restore the contract text deterministically before showing the board. Garbled or approximate text cannot pass Phase 2.

After QA, ask:

`是否确认当前贴片设计？确认后我将按策划稿位置合成完整直播间预览。`

Do not continue without explicit approval.

## 5. Phase 3: coordinate composition

Build `03-完整直播间预览.jpg` from approved assets:

1. use the complete approved Phase 1 visual as the unchanged base;
2. place Phase 2 sticker assets at plan-defined coordinates;
3. preserve the approved foreground stage, product count, product-stage association, packaging, scale, perspective, and coordinates;
4. preserve host, UI, copy, and safe-area clearance;
5. create `work/贴片定位层-9x16.png` at the same time.

Prefer deterministic compositing so placement does not regenerate previously approved pixels. Use ImageGen only for a narrowly scoped perspective integration or occlusion repair; repeat the full immutable list and reject collateral change.

This phase decides only sticker scale, placement, overlap, avoidance, information density, and reading order. It may not redesign or move the approved scene-title-host-stage-product system or the approved sticker family.

After QA, ask:

`是否确认当前完整成品及贴片位置？确认后我将输出透明贴片合集、纯背景、前景展台+产品和顶部大标题。`

Do not continue without explicit approval.

## 6. Phase 4: production separation

From the approved Phase 3 sources, produce:

1. `贴片合集-16x9.png`: separated non-title sticker assets on transparent 1920 x 1080.
2. `背景.jpg`: pure opaque 1080 x 1920 scenery.
3. `前景展台+产品.png`: coordinate-locked transparent 1080 x 1920 physical foreground stage and products, when applicable.
4. `顶部大标题.png`: coordinate-locked transparent 1080 x 1920 title system.
5. internal `work/贴片定位层-9x16.png`: coordinate-locked transparent stickers for validation and optional delivery.

Keep `03-完整直播间预览.jpg` as the approved visual reference. Use the approved Phase 1 source to isolate the foreground stage and products without sticker contamination, and verify its coordinates against Phase 3. Do not regenerate these assets during separation.

The generated Phase 1 host normally represents the live camera subject and is not delivered as a production layer. If the user requires a permanent virtual host, add `人物.png` as a separate coordinate-locked RGBA layer and include it in validation.

## 7. Approval semantics

Treat `确认`, `通过`, `定稿`, `继续下一步`, or equivalent explicit approval as authorization for only the next phase.

Treat requested changes, partial approval, questions, or silence as not approved. Approval of Phase 1 does not approve Phase 2 or Phase 3. The latest explicitly approved file in each phase becomes immutable input for the next phase.

## 8. Revision routing

When changes are requested:

- revise Phase 1 only for scene, title, host, palette, camera, global material language, foreground stage, product count, product appearance, product hierarchy, or product-stage placement;
- revise Phase 2 only for sticker copy, quantity, grouping, contour, material, or typographic hierarchy;
- revise Phase 3 only for sticker scale, coordinates, avoidance, overlap, density, or reading order;
- after a Phase 1 change, reconfirm Phase 1 and re-check whether Phase 2 styling must be regenerated;
- after a Phase 2 change, reconfirm Phase 2 and rebuild Phase 3;
- after a Phase 3 change, reconfirm Phase 3 and regenerate every affected production layer.

For a local correction, define allowed change, old state to clear, new state, and locked items. After two failed local edits that damage locked content, regenerate only the affected phase—never the whole four-stage project by default.

## 9. Content fidelity

- Preserve business text, numbers, units, labels, hierarchy, footnote markers, brands, and relationships.
- Do not invent claims, safety conclusions, institutions, certificates, promotions, subtitles, or products.
- Do not copy sample text, prices, logos, or products from directional references.
- If approved legal copy cannot render reliably, preserve its module and reserve the typesetting area rather than fabricate content.
- Preserve supplied product shape, cap, trigger, label hierarchy, colors, proportions, and pack count.

## 10. Reference conflicts

Use the priority order in `design-contract-and-qa.md`. The latest annotated screenshot overrides older placement interpretations. A style reference may influence design mechanisms only; it may not change approved copy, quantity, grouping, ownership, or coordinates.
