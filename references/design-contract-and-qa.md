# Design Contract and Stage QA

## Contents

1. Reference priority
2. Visual contract and asset ownership
3. Relationship vocabulary
4. Design-strength standard
5. Phase 1 visual system
6. Phase 2 sticker system
7. Stage, product, and copy integration
8. Color, typography, and maturity
9. Revision routing and local-edit whitelist
10. Multiple directions
11. Phase 1 QA
12. Phase 2 QA
13. Phase 3 QA
14. Regression QA
15. Production-layer QA

## 1. Reference priority

Resolve conflicts in this order:

1. the user's latest annotated screenshot or explicit correction;
2. explicit content and layout requirements in the planning draft;
3. supplied product, logo, brand, and person identity references;
4. the latest approved file from the current phase;
5. approved files from earlier phases;
6. directional style references;
7. model interpretation.

Do not let an attractive style reference override required copy, product counts, grouping, ownership, or position.

Assign every reference one or more purposes:

- `content/layout authority`: wording, quantity, hierarchy, and spatial relationships;
- `product identity`: packaging, color, proportion, and pack count;
- `person identity`: requested adult host identity or appearance;
- `style mechanism`: specified contour, material, lighting, layering, or rhythm.

Interpret arrows, circles, frames, and handwritten marks as placement or relationship instructions. Remove them from finished visuals unless the user asks to retain them.

## 2. Visual contract and asset ownership

Create the contract before Phase 1. Keep it in working notes or prompts; show it only when useful.

### A. Content inventory

| Category | Required fields |
| --- | --- |
| Host | count, adult identity, pose, clothing, action, position, preview-only or fixed |
| Product | reference, exact count, hero/secondary role, scale, position, stage association |
| Title | exact copy, region, line hierarchy, title-bound logos and decoration |
| Stage | count, shape, material, product association, position |
| Sticker | exact copy, count, contour, combined/independent state, position |
| Data | item count, order, number, unit, marker, footnote |
| Evidence | module count, hierarchy, approved wording, position |
| Scene | room type, camera, palette, lighting, depth, safe areas |
| Decor | permitted motifs, density, placement rhythm, title-bound or sticker-bound |

### B. Asset-ownership map

Classify each element once:

| Ownership | Includes | Excludes |
| --- | --- | --- |
| Scene | architecture, floor, distant furniture, environmental light | title, host, sticker, stage, product |
| Top title | main title, title-bound logo, subtitle, header shape and decoration | ordinary marketing stickers |
| Host preview | adult host used to judge scale and safe area | stage, product, sticker |
| Marketing sticker | benefits, data, reports, service strip, scene card, PIP frame, footnote | physical stage and hero product |
| Physical stage | table, counter, podium, plinth, product stand | graphic copy and badges |
| Physical product | referenced pack shots placed on or near the stage | sticker-integrated explanatory miniatures |

For ambiguous items, decide ownership before Phase 1. An image inside a scenario card is a sticker; a hero product placed on the stage is a physical product.

### C. Element-relation map

Record each fragile relationship:

| Element A | Relation | Element B | Constraint |
| --- | --- | --- | --- |
| [data group] | combined with | [data items] | one inseparable sticker |
| [badge 1] | independent from | [badge 2] | never merge |
| [badges] | left/right/above/below | [hero product] | preserve a clear gap |
| [copy] | visually embedded in | [stage fascia] | production ownership remains sticker |
| [secondary product] | supported by | [secondary stage] | never move to hero stage |

Position and relationship are first-class requirements, not optional styling notes.

### D. Immutable list

After each phase approval, lock:

- Phase 1: scene, camera, title system, host, foreground stage, products, product-stage association, palette, lighting, and safe areas;
- Phase 2: sticker count, copy, grouping, contour family, material, and hierarchy;
- Phase 3: sticker scale, final coordinates, overlap, avoidance, density, and reading order.

Repeat relevant immutable items in every edit prompt.

### E. Reference-use map

State the purpose of each attached image:

- `策划稿：控制全部内容、层级与空间关系`;
- `贴片结构母板：控制贴片数量、文案、组合关系和顺序`;
- `第一步确认图：控制贴片的配色、材质、轮廓、字体和节奏，并显示展台与产品已经占用的空间`;
- `产品图：只控制包装外观、比例和数量`;
- `风格图：只控制指定的材质或设计机制`.

## 3. Relationship vocabulary

Use precise spatial words:

- combined / inseparable;
- independent / disconnected;
- embedded in;
- adjacent to;
- aligned with;
- above / below / left / right;
- in front of / behind;
- overlapping without covering copy;
- supported by;
- sharing one stage;
- using a separate stage.

Do not use “place nearby” when the annotation specifies a relationship or region.

## 4. Design-strength standard

The final room should satisfy at least four applicable criteria:

- a title with two-level hierarchy, offset, overlap, cropping, interlock, or controlled motion;
- clear size, shape, or material contrast between primary and secondary modules;
- sticker contours with selective notches, layered borders, interruptions, or transparent depth;
- information integrated with a stage, ring, arc, architectural edge, or perspective plane;
- clear foreground, midground, and background occlusion;
- campaign decoration connected to the scene rather than scattered evenly;
- intentional negative space for the host and platform UI;
- a repeated motif linking title, stickers, stage, and environment.

Reject a technically complete result when it reads as a PPT card wall.

### Prohibited shortcuts

- repeating the same white rounded rectangle for all information;
- distributing every module at equal size and weight;
- pasting stage copy on an unrelated white card;
- using a flat brand-color strip plus default text as the title;
- mixing unrelated title, sticker, and stage systems;
- adding decorative motifs without hierarchy or spatial purpose.

## 5. Phase 1 visual system

Design the top title as a visual system, not a text box:

- follow the required title region and width;
- establish clear primary and secondary copy hierarchy;
- use arcs, rings, folds, layered planes, glow, controlled cropping, or offsets when appropriate;
- make title-bound decoration support recognition;
- reserve open space for later stickers, host motion, and UI around the actual foreground stage and products;
- create foreground, midground, and background depth with the stage and products forming the approved foreground anchor;
- make stage scale, product count, product hierarchy, product-stage association, and occlusion legible before Phase 2;
- exclude every non-title marketing sticker, including stage-face copy and benefit badges.

If the plan does not require a person, do not invent one merely because Phase 1 supports hosts.

When the hero product or room is explicitly `除螨喷雾`, apply only the exclusive main-title font-style and rejection rules in `dust-mite-spray-title-system.md`. Do not let that reference prescribe color, title-region coverage, materials, backing shapes, effects, decoration, or subtitle styling, and do not generalize it to other categories.

## 6. Phase 2 sticker system

### Structure board requirements

- 1920 x 1080 white background;
- every sticker fully visible and separated by clear gutters;
- combined modules remain combined;
- independent modules remain independent;
- exact text, numbers, units, order, footnotes, and labels;
- no physical stage, hero product, host, or room scenery;
- neutral structure styling that does not compete with content.

### Styled board requirements

By default, build three simple, clearly different sticker families for selection. For each direction, use purposeful variation:

- one or two primary material families;
- different scale and silhouette for primary, secondary, data, and evidence modules;
- enough contrast for Chinese copy and numbers;
- selective notches, underlays, rings, strokes, edge light, or translucent depth;
- typography, contour, and material related to approved Phase 1;
- all assets separated, uncropped, and reusable.

Do not turn the 16:9 board into a miniature room composition. Its job is asset design and review.
If ImageGen text fidelity fails, preserve the approved shape/material design and restore exact contract text deterministically before review.

## 7. Stage, product, and copy integration

Use the physical stage to establish:

- hero and secondary product hierarchy;
- foreground depth and perspective;
- a transition between scenery and campaign graphics;
- a visual anchor for the main benefit;
- a connection point for recurring motifs.

Valid visual integration includes translucent fascia, perspective information bands, rings crossing the stage edge, tinted acrylic, controlled type cropping, or a small illuminated benefit.

Production ownership remains separate:

- stage body and table-top hero products -> `前景展台+产品.png`;
- marketing copy, outlines, labels, and graphic accents -> sticker assets and `贴片定位层-9x16.png`.

The sticker may visually hug the stage without being flattened into the physical stage layer.

## 8. Color, typography, and maturity

Derive a dominant base, campaign accent, neutral support, and optional material highlight from brand and references.

- separate scene and sticker values sufficiently;
- do not make all stickers pure white;
- use accent color for hierarchy rather than blanket saturation;
- use metallic tones only as controlled highlights;
- avoid accidental vintage yellow in warm-white rooms unless requested.

Prefer contemporary sans-serif typography unless the brand requires otherwise. Avoid default office fonts, traditional plaque lettering, unsupported calligraphy, childish bubble type, and illegible body copy.

Aim for mature, modern ecommerce energy. Avoid both hard red-gold conference staging and overly cute universal capsules.

## 9. Revision routing and local-edit whitelist

Route changes to the owning phase:

- Phase 1: scene, title, host, palette, camera, global material, stage, product, or product-stage relationship;
- Phase 2: sticker content, count, grouping, contour, material, or type;
- Phase 3: sticker scale, coordinates, overlap, avoidance, density, or reading order.

For each local edit, write:

- `Allowed change`;
- `Old state to clear`;
- `New state`;
- `Locked items`.

Do not ask ImageGen to “improve the whole image” during a coordinate-only correction. After two failed local edits, regenerate only the affected phase.

## 10. Multiple directions

For Phase 2, generate three directions by default. When alternatives are requested in any phase:

- Phase 1 directions should differ in title structure, scene mechanism, stage form, product presentation, depth, or material;
- Phase 2 directions should differ in sticker contour, material, information hierarchy, or edge treatment;
- keep the visual contract identical;
- vary at least three relevant systems;
- never present recolors of the same design.

## 11. Phase 1 QA

- [ ] scene, camera, lighting, and palette match the plan;
- [ ] title copy, title-bound logos, subtitle, and decoration are correct;
- [ ] title has intentional hierarchy and design strength;
- [ ] when the room is explicitly for `除螨喷雾`, every dedicated title-font check in `dust-mite-spray-title-system.md` passes without overriding the planned color or title-area design;
- [ ] host count, adult identity, pose, clothing, and safe area are correct when applicable;
- [ ] physical foreground stage count, shape, material, perspective, and position match the plan when applicable;
- [ ] product reference, exact count, packaging, scale, hierarchy, coordinates, and stage association are correct;
- [ ] products are visually clear and not blocked by the title, person, stage edge, or UI;
- [ ] no non-title marketing sticker, benefit card, data module, report card, or stage-face promotional copy appears;
- [ ] later sticker, live-motion, and UI spaces remain usable around the approved foreground assets;
- [ ] no planning annotation, watermark, or unsupported claim remains.

## 12. Phase 2 QA

- [ ] board is 16:9 and every sticker is fully visible;
- [ ] sticker quantity, copy, numbers, units, order, markers, and footnotes are exact;
- [ ] combined modules remain combined and independent modules remain independent;
- [ ] no physical stage, hero product, host, or room scenery appears;
- [ ] sticker family clearly inherits Phase 1 palette, material, contour, and rhythm;
- [ ] primary, secondary, data, and evidence modules have purposeful variation;
- [ ] no duplicate, omitted, merged, cropped, garbled, or invented item appears;
- [ ] the result is an asset board, not a miniature complete room.

## 13. Phase 3 QA

- [ ] Phase 1 scene, title, host, camera, palette, lighting, foreground stage, and products did not drift;
- [ ] Phase 2 sticker design, count, copy, and grouping did not drift;
- [ ] every sticker matches plan-defined scale, position, order, and relationship;
- [ ] product count, packaging, scale, hierarchy, stage association, perspective, and coordinates remain identical to approved Phase 1;
- [ ] foreground depth and stage occlusion remain credible after sticker placement;
- [ ] stickers avoid faces, product labels, platform UI, and important stage copy;
- [ ] old positions and placeholders are fully cleared;
- [ ] final density, reading order, and visual center are balanced;
- [ ] `work/贴片定位层-9x16.png` matches the preview coordinates.

## 14. Regression QA

After every revision:

- [ ] requested change is complete;
- [ ] old state is fully cleared;
- [ ] current-phase immutable items remain unchanged;
- [ ] approved earlier-phase assets remain unchanged;
- [ ] no previously correct item disappeared;
- [ ] no duplicate, replacement, or unrelated object appeared;
- [ ] copy remains readable and unblocked;
- [ ] composition, palette, material, and camera did not drift.

Reject an edit that fixes the target but damages a locked item.

## 15. Production-layer QA

- [ ] all coordinate layers are 1080 x 1920 and remain at origin `(0, 0)`;
- [ ] sticker atlas is 1920 x 1080 with transparent gutters;
- [ ] `背景.jpg` contains only scenery and is fully opaque;
- [ ] `顶部大标题.png` contains only the approved title system;
- [ ] `前景展台+产品.png`, when present, contains only the approved physical foreground stage and products;
- [ ] positioned sticker layer contains all and only non-title marketing stickers;
- [ ] every PNG has real alpha with transparent and visible pixels;
- [ ] no layer has white, black, checkerboard, or chroma matte contamination;
- [ ] composite preview restores the approved Phase 3 structure without drift.
