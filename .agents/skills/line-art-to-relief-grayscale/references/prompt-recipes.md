# Prompt recipes

Replace bracketed text with observations from the actual source. Keep the prompt compact and label every image role.

## Default base edit prompt

> Use the first referenced image as the sole content, topology, text, and composition authority. Convert its exact composition into a monochrome 8-bit grayscale low-relief height map. Preserve [silhouette, pose, proportions, part counts, overlaps, openings, symmetry, framing, exact source text]. Use the approved bright-soft-shallow standard from the style reference without copying its subject or composition. Brightness strictly means geometric height: black is the flat zero-height base, dark gray is rear/shallow relief, mid-to-light gray forms the main body, and small lighter accents mark the highest geometry. Replace ink outlines and hatching with a crisp silhouette bevel, shallow softly blended overlap valleys, wide low-contrast grooves, soft raised ridges, and broad smooth planes. Build rounded macro volumes first, readable medium-scale structure second, and restrained microdetail last. Keep facial planes, hands, joints, folds, segments, clustered grains, ornaments, patterns, and exact source glyphs clear but soft-edged. No printed outlines, hard carving, cratered beads, color, new or garbled text, new objects, cast shadows, directional lighting, rim light, glow, metallic shine, pores, paper grain, or background texture. Do not crop.

## Reference-role clause

> Image 1 is the sole content/topology/text source. `00-approved-soft-bright-shallow-standard.png` is style-only and controls brightness, softness, shallow depth, low-contrast grooves, smooth rounded masses, and height hierarchy. Any additional reference is subject-family style-only. Do not copy subjects, poses, objects, text, ornaments, or composition from style references.

## Isolated subject addition

> Place the complete subject on a uniform black zero-height field with generous untouched negative space. Keep the silhouette crisp. Use rear forms around 45–125, broad main masses around 120–205, foreground structures around 165–225, and only small crest accents around 210–238. Aim for a bright, soft, shallow result with readable meso detail rather than a dense white solid, hard engraving, or featureless blur.

## Dense panel addition

> Assign explicit depth bands before detail: base/gaps 0–8, rear ornament 35–100, middle layers 85–160, foreground 145–220, and small peak accents 205–238. Preserve major crossings, object counts, labels, and motifs. Reduce repetitive microtexture, but keep important medium-scale structures and exact source glyphs legible.

## Portrait or figure addition

> Preserve identity and gesture. Model forehead, brow, nose, cheek, lips, chin, and hands as shallow connected planes. Group hair, beard, jewelry, armor, and fabric into medium-scale masses before adding restrained grooves. Make garment folds wide and shallow, fingers softly separated, hair grouped, and shoe-sole texture broad and sparse. Avoid deep eye sockets, pinched nostrils, waxy skin, and lighting-driven highlights.

## Clustered seeds or grains addition

> Build each seed or bead-like unit as a smooth softly domed form with shallow soft separation and mild local merging. Preserve important gaps and the exact cluster silhouette. Do not create concentric dimples, center pits, hard bright rims, or sharp one-by-one bead engraving.

## Source text addition

> Preserve the exact source text, glyph shape, placement, and occurrence count. Render it as shallow raised or recessed relief integrated into the original label or plaque. Add no other characters, letters, numbers, logos, or text.

## Linear ornament addition

> Convert each important stroke into a clean raised beveled ribbon with darker adjacent valleys, a mid-gray body, and a lighter center ridge. Preserve stroke-width rhythm, crossings, and enclosed negative spaces. Do not leave black outlines printed on top.

## Focused repair prompts

Use one repair at a time and preserve everything else.

- **Too blurred**: “Keep the silhouette, tone range, and depth order unchanged. Recover facial planes, joints, grouped texture, folds, segments, ornaments, and patterns as medium-scale relief using shallow darker valleys and soft raised ridges. Do not sharpen them into outlines.”
- **Too solid**: “Keep all current meso detail. Lower broad body brightness and apparent thickness, darken rear layers, and strengthen front-to-back offsets. Preserve the black base and limit near-white to tiny crest points.”
- **Too dim**: “Raise the subject’s main gray range while keeping the black background unchanged, rear layers darker, and near-white sparse. Do not flatten the layer hierarchy.”
- **Too hard or deeply carved**: “Keep topology, composition, and tone order unchanged. Widen and lighten internal grooves, soften hard edge transitions, merge repetitive carving into broad smooth planes, and remove metallic or toolpath character.”
- **Weak separation**: “Deepen only the narrow valleys at overlaps and adjust layer value offsets without changing the silhouette.”
- **Lighting contamination**: “Remove directional illumination, cast shadows, and rim light. Encode brightness only as geometric elevation.”
- **Outline residue**: “Replace printed contours with silhouette bevels, overlap valleys, seams, or shallow structural grooves.”
- **Noisy detail**: “Remove speckles, pores, hairlines, and repeated noise; merge them into wider, shallower, manufacturable relief structure.”
- **Cratered seed clusters**: “Keep the cluster silhouette, seed count rhythm, and gaps unchanged. Remove concentric dimples and hard rims; rebuild each unit as a smooth dome with shallow soft separation and mild local merging.”
- **Text drift**: “Keep the label geometry and composition unchanged. Restore the exact source glyphs, placement, and occurrence count; remove all additional text.”

## Reference asset selection

Always use:

- `assets/references/00-approved-soft-bright-shallow-standard.png` — user-approved universal brightness, softness, shallow depth, low-contrast grooves, and rounded modeling.

Optionally add one closest subject-family asset:

- `assets/references/00-approved-bright-detailed-standard.png` — secondary structure reference only when meso detail is at risk; do not let it harden the style.
- `assets/references/01-isolated-animal.png` — alternate animal shape handling.
- `assets/references/02-human-figure.png` — full figure and costume layering.
- `assets/references/03-buddha-figure.png` — statue, halo, robe, and calm modeling.
- `assets/references/04-dense-dragon-panel.png` — dense dragon/cloud layering.
- `assets/references/05-floral-screen.png` — floral and bird relief.
- `assets/references/06-narrative-panel.png` — vertical landscape/narrative staging.

Never let a style reference override the source topology.

## Finalization

Normalize the selected output to an 8-bit single-channel grayscale PNG and record metrics:

```bash
python scripts/finalize_heightmap.py <generated-image> --output <final.png>
```

Use the metrics as diagnostics. The tested envelope is subject mean 148–166, standard deviation 38–47, P95 209–221, near-white below 1%, and border maximum no higher than 2.
