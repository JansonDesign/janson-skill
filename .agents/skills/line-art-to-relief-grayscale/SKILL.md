---
name: line-art-to-relief-grayscale
description: Convert supplied line drawings, outline illustrations, ink drawings, logos, ornaments, figures, animals, plants, food/grain clusters, labeled vessels, religious images, or narrative panels into bright, soft, shallow, smoothly modeled monochrome grayscale relief/height maps. Use for 线稿转灰度图、浮雕灰度图、雕刻灰度图、精雕图、深浅层次图、柔和浅浮雕、height map、relief map、embossed grayscale, CNC/laser/ZBrush relief references, or when an existing line-art composition must become a black-base, white-high sculptural grayscale image with rounded masses, restrained low-contrast grooves, preserved source text, and no printed outlines.
---

# Line Art to Relief Grayscale

Convert line art into a coherent height field, not a lit grayscale illustration. Treat brightness strictly as elevation: black is zero height, dark gray is rear/shallow relief, mid-gray is the main body, and light gray is the highest geometry.

The default approved look is **bright, soft, shallow, and clean**:

- keep large forms smoothly rounded with broad gentle gradients;
- keep facial planes, hands, folds, horn segments, grains, clustered seeds, ornaments, and source text readable at medium scale;
- use wide shallow low-contrast grooves and soft raised ridges instead of black outlines or hard carving;
- keep clustered seeds as softly domed forms with mild local merging, never cratered beads;
- keep near-white sparse and preserve a pure black zero-height field;
- avoid both extremes: do not make the subject dense/solid, and do not blur away identity-bearing structure.

## Required workflow

1. Inspect the source with an image viewer.
2. Identify the silhouette, closed shapes, overlaps, negative spaces, fragile details, symmetry, and front-to-back order.
3. Use black-low/white-high unless the user explicitly requests reversed polarity.
4. Select one profile:
   - **Isolated subject**: animal, person, deity, single flower, emblem.
   - **Dense decorative panel**: dragon/cloud panel, landscape, furniture panel, multi-object scene.
   - **Portrait or figure**: face, bust, full-body character.
   - **Linear ornament**: border, scrollwork, calligraphic or ribbon-like pattern.
5. Read [references/style-spec.md](references/style-spec.md). Read [references/prompt-recipes.md](references/prompt-recipes.md) before composing or repairing a prompt.
6. Use an image-generation or image-editing tool. Keep the source line art as the sole content and topology authority.
7. For local inputs, place the content source first in `referenced_image_paths`. Use `assets/references/00-approved-soft-bright-shallow-standard.png` as the default style-only reference. Add at most one closest subject-family reference when necessary.
8. State every reference role explicitly. Never copy subjects, poses, objects, ornaments, text, or composition from style references. A user-approved reference overrides generic styling but never overrides source topology.
9. Inspect the result at full size and thumbnail scale. Iterate only against a named defect.
10. Normalize the selected deliverable to an 8-bit single-channel grayscale PNG and run `scripts/finalize_heightmap.py` to record range metrics.
11. Deliver the raster and state polarity. Do not claim CNC readiness unless the height-map validation gates pass.

## Construction rules

- Preserve silhouette, pose, framing, proportions, major internal divisions, intentional openings, and part counts.
- Reinterpret ink as silhouette bevels, overlap valleys, seams, shallow grooves, or changes of plane. Remove visible printed strokes and hatching.
- Build three scales:
  - **Macro**: silhouette, primary masses, global front/back hierarchy.
  - **Meso**: facial planes, muscles, grouped fur, petals, folds, feathers, horn segments, jewelry, architectural masses.
  - **Micro**: restrained veins, hair, scales, engraved motifs, and edge grooves.
- Give meso detail priority. It must remain readable without becoming sharp line art.
- Use a crisp outer silhouette with a short inward bevel.
- Separate overlaps with narrow darker valleys and value offsets, never cast shadows.
- Use broad continuous gradients on rounded masses and soft low-contrast local ridges/grooves on structure.
- Keep the background uniformly black and free of glow, texture, haze, or floor shadows.
- Keep near-white sparse. Broad main masses should remain light gray rather than clipped white.
- Make delicate details wide and shallow enough to survive downsampling and carving.
- Convert repeated ink hatching into a few broad structural folds or veins; never preserve every stripe.
- Preserve source text only when present. Render it exactly as shallow raised or recessed geometry, never as printed ink; add no new text.
- For seeds, berries, beads, or sorghum-like clusters, use smooth domes, shallow soft separation, and mild local merging. Reject concentric dimples, hard rings, and sharp bead rims.

## Default value hierarchy

Treat these as prompt targets rather than deterministic pixel guarantees:

- Background and true gaps: 0–8
- Rear or shallow forms: 45–125
- Main body masses: 120–205
- Foreground structures: 165–225
- Small peak accents: 210–238

Across the approved plant, figure, animal, and dense-panel tests, successful results had a non-black subject mean near 148–166, standard deviation near 38–47, a 95th percentile near 209–221, border maximum no higher than 2, and less than 1% of subject pixels at 240–255. Treat this as a style envelope, not a forced histogram.

## Profile guidance

### Isolated subject

Use a large uniform black field and generous negative space. Keep the subject bright enough to read immediately, but vary rear, middle, and front layers. Model head, torso, and limbs as broad masses. Preserve medium-scale identity details—eyes, nostrils, joints, hoof/claw forms, grouped fur or feathers, accessories, and patterned relief—through shallow grooves and raised ridges.

### Dense decorative panel

Assign explicit depth bands before adding detail. Keep rear ornament dark, middle layers separated, foreground forms brighter, and small crest accents lightest. Reduce repetitive micro-detail before it turns into noise, but keep important medium-scale crossings and motifs legible.

Preserve exact source labels or characters when present. Give rear plants, middle stems, foreground containers/figures, and label details distinct but gently compressed value bands.

### Portrait or figure

Prioritize recognizable head shape, facial planes, hands, gesture, and garment hierarchy. Keep eye sockets shallow. Group hair, beard, jewelry, armor, and cloth into medium-scale masses before adding restrained grooves. Express garment folds as wide shallow transitions, hair as grouped masses, fingers as softly separated rounded forms, and shoe soles with only a few broad grooves.

### Linear ornament

Convert each important stroke into a raised beveled ribbon: darker adjacent valleys, a mid-gray body, and a lighter center ridge. Preserve stroke-width rhythm, intersections, and enclosed openings without leaving printed outlines.

## Generation contract

Include:

- exact topology and composition from the source;
- monochrome 8-bit grayscale height-map semantics;
- the approved bright-soft-shallow, smoothly modeled standard;
- a uniform black zero-height base;
- clear meso detail without global blur;
- matte clay/ZBrush/CNC-relief character;
- continuous band-free gradients;
- no color, new or garbled text, new objects, photographic lighting, cast shadows, rim light, glow, metallic shine, paper grain, pores, or background texture;
- no crop unless requested.

## Validation gates

Reject or repair when any gate fails:

1. **Topology**: silhouette, pose, openings, crossings, and major part counts match.
2. **Polarity**: higher geometry is brighter and recesses are darker.
3. **Lighting independence**: no cast shadow or directional highlight controls the values.
4. **Layer separation**: rear, middle, and foreground remain distinct.
5. **Meso clarity**: face, joints, folds, grouped texture, ornaments, and patterns are readable at normal viewing size.
6. **Continuity**: gradients are smooth, without posterization, halos, or airbrush blobs.
7. **Carvability**: no isolated specks, pores, hairline ridges, or floating height islands.
8. **Range**: black base stays stable; broad white clipping is absent; the subject does not collapse into one flat gray.
9. **Text fidelity**: source text is exact, count-correct, and integrated as relief; no additional text appears.
10. **Format**: final PNG is 8-bit single-channel grayscale.
11. **Clean output**: no color cast, watermark, unintended label, frame, mockup surface, or unrelated ornament.

## Focused repair policy

Name one defect and preserve everything else:

- **Too blurred**: recover medium-scale relief using shallow darker valleys and soft raised ridges; do not sharpen into outlines.
- **Too solid**: lower broad body values and increase rear/middle/front offsets without erasing detail.
- **Too dim**: raise the main subject range while keeping the background black and near-white sparse.
- **Too hard or deeply carved**: soften edge transitions, widen and lighten grooves, merge repetitive microdetail into broad forms, and preserve topology.
- **Weak separation**: deepen only overlap valleys and adjust layer offsets.
- **Outline residue**: replace printed contours with bevels, seams, and grooves.
- **Noisy detail**: merge speckles and hairlines into wider, shallower structural forms.
- **Cratered seed clusters**: remove concentric dimples and hard rims; rebuild seeds as smooth domes with shallow soft separation and mild local merging.
- **Text drift**: restore the exact source glyphs and occurrence count without changing labels or composition.

Stop after a clean validated result. Do not regenerate for stylistic novelty.
