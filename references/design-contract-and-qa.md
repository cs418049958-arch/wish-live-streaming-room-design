# Visual contract, creative direction, and QA

## Contract table

For each element record `id | exact copy/count | required source | reference role | owner | region/relationship | immutable after phase`. Use owners `scene`, `top-title`, `host-preview`, `physical-stage`, `physical-product`, `marketing-sticker`. An explanatory product image inside a sticker belongs to that sticker; a pack placed on the stage is physical. A line of promotional text visually embedded on a stage still belongs to a sticker or title layer.

Reference priority: latest user annotation or correction > explicit planning requirement > identity/packaging reference > current approved visual > earlier approved visual > style reference > model invention. A reference may control only its named role. The plan controls required room type and functional relationships; unless explicitly asked, do not trace its architecture, furniture coordinates, or colors.

Record `combined`, `independent`, `above/below`, `left/right`, `aligned`, `supported by`, `in front of`, `behind`, and `overlapping without covering copy` precisely. Mark presenter motion range and platform UI no-go zones. Distinguish fixed virtual host from temporary generated host.

## Creative decision

Write one sentence naming the campaign idea and physical/graphic mechanism (for example, a particular architectural curve continuing into title and badge contours). Choose a limited repeatable set of shapes, materials, and accents. Allocate one dominant focal point, one supporting information rhythm, usable negative space, and a foreground anchor. Judge at phone size as well as full resolution. Reject a card-wall, uniform rounded panels, flat logo strip, random confetti, or copy-heavy stage front. Avoid adding unrelated objects merely to show creativity.

For alternatives, keep locked content identical while varying at least three of architecture, camera depth, title structure, stage geometry, lighting, material, and sticker contour. Do not require a prescribed motif if the brand reference points elsewhere.

Seated presenter default applies only when no explicit contrary planning or user direction covers that attribute: frontal face/torso, centered camera axis, close conversational scale, symmetric straight-on table. Apply the landmark ranges and composition-only reference in `references/seated-host-composition.md` from the first spatial preview. Keep the host large and lower-middle; extend the foreground desk across the full bottom without a visible floor strip underneath. An override may affect only one attribute; retain the others. Product count defaults to zero unless explicit inclusion is recorded. Never add packs, silhouettes, boxes, placeholders, or new claims to a zero-product scene.

## ImageGen and text QA

- Number every image and state its permitted job. Prevent a style reference from donating copy or products. Use generation for a new scene; use an edit target for changes to an approved image.
- Start prompts with intended image and main subject; then composition, style, exact short text, locks, and concise avoid list. Remove inactive-phase instructions.
- Quote each exact title or short sticker phrase and its count. Check all Chinese, numbers, units, brand names, and footnotes in the result. Use deterministic text compositing for dense or unstable wording; never fabricate data.
- For requested physical products, compare silhouette, cap/trigger, label hierarchy, color, count, scale, and stage association with the supplied reference. Use the supplied pack as an identity reference during whole-image design; defer production cutouts until Phase 4.
- For a local edit, request one change and check all invariants. Inspect the edited image before accepting it.

If the main product or room is explicitly 除螨喷雾, also apply the font-only pass/fail checks in `dust-mite-spray-title-system.md`. Do not apply that conditional to other categories.

## Gate QA

### Phase 1

- Required scene, title, host, stage, and explicitly placed products match content and layout; absent elements stay absent.
- Background differs structurally from the planning mockup unless replication was requested.
- Concept links title, scene, and foreground without sacrificing host/UI space.
- Product identity, exact count, anatomy, title text, safe areas, and natural overlap pass.
- For seated-host/table scenes, presenter size and landmark positions match the composition contract, hands contact the tabletop, and the desk fills both side edges and the entire bottom. Required floor remains behind/beside the host; no floor strip is visible below the desk.
- Review the whole ImageGen image directly. Do not require pure-background inpainting, RGBA extraction, or layer reconstruction before approval.

### Phase 2

- The whole sticker board has correct module count, grouping, sequence, text, units, footnotes, and uncropped shapes.
- Outer artboard and gutters are solid pure white (#FFFFFF), without tint, gradient, texture, scenery, or a shared ground shadow. Sticker bodies retain substantial colored backgrounds/title blocks consistent with the approved style; white artboard must not flatten all stickers into white-only thin frames.
- Every independent asset/group has a white moat and edge margin of at least 4.5% of the canvas short edge (about 48px at 1920×1080; prefer 48–64px or wider), measured from full extents including shadows, decoration and text. No overlap, tangent edge, cross-group decoration or common base remains. Independent report cards each pass this check; explicitly combined modules stay combined.
- Requested blank certificate areas remain plain white and empty within a sufficiently broad backing/header. Check at full size that each complete group can be separately rectangular-selected without including a neighbor; revise the whole board if spacing fails.
- No room/host/stage/physical product contaminates the board. Do not require individual transparent assets or atlas reconstruction yet.
- Hierarchy works at phone size; silhouettes vary purposefully; no copy is unreadable.

### Phase 3

- Accepted Phase 1 elements and Phase 2 sticker designs remain visually consistent; inspect scoped ImageGen edits for drift. Sticker coordinates, scale, hierarchy, gaps, UI avoidance, and occlusion match plan.
- Review the complete whole-image preview directly; defer positioned layers, cutouts, and production manifests until Phase 4.
- No old position, duplicate, hidden footnote, or unsupported claim remains.

### Production and regression — after full approval only

- Extract all layers and sticker assets now. Inpaint removed regions cleanly; check title/stage/host/sticker alpha edges for halos, mattes, clipping, and unintended pixels.
- Preserve the approved final whole image as the comparison master. Repair extraction rather than substituting a newly reconstructed approval image.
- Approved copy, identity, product count, and relationships survive every revision.
- The validator passes dimensions, alpha, manifest coverage, and full-preview comparison. Inspect the difference image and layered preview visually.
- Keep a preview-only host out of the production delivery while using its retained layer for reconstruction QA. If stage/host occlusion needs multiple sublayers, deliver the needed stack with explicit order.
