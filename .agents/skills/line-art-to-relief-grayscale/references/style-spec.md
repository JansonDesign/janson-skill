# Approved soft-bright-shallow relief standard

## Contents

- Approved baseline
- Tested acceptance envelope
- Visual grammar
- Detail-frequency balance
- Line-art interpretation
- Subject treatment
- Failure modes

## Approved baseline

Use `../assets/references/00-approved-soft-bright-shallow-standard.png` as the default style reference. It is the user-approved baseline and establishes:

- uniform black zero-height background;
- a bright, shallow, gently compressed subject range;
- broad smoothly rounded macro volumes;
- restrained low-contrast grooves and softly blended overlap valleys;
- readable medium-scale anatomy, folds, grains, ornaments, patterns, and source text;
- smooth seed domes without cratered centers or hard rims;
- soft internal edges, no printed outlines, subdued microtexture, and no photographic lighting.

Use `../assets/references/00-approved-bright-detailed-standard.png` only as a secondary structure reference when a subject risks losing anatomy or meso detail. It must not make the output harder, darker, or more deeply carved than the primary standard.

## Tested acceptance envelope

Four user-reviewed outputs established this working envelope:

| Subject family | Mean | Std. dev. | P95 | Near-white |
|---|---:|---:|---:|---:|
| Soft grain/leaf isolated subject | 166.0 | 38.8 | 221 | 0.83% |
| Human figure with vessel | 155.4 | 39.3 | 209 | approximately 0% |
| Decorative animal with cloud | 159.6 | 42.0 | 216 | 0.17% |
| Dense grain-and-vessel panel | 148.5 | 46.8 | 219 | 0.20% |

Use a general target of subject mean 148–166, standard deviation 38–47, P95 209–221, near-white below 1%, and border maximum no higher than 2. These are diagnostic ranges, not grading targets. Preserve topology and depth order before chasing metrics.

## Visual grammar

### Height, not illumination

Brightness means elevation. A bright region is physically higher, not merely facing a light. Do not use cast shadows, dramatic side lighting, rim light, or glossy highlights to create form.

### Bright soft shallow relief

Keep the subject immediately readable against black. Use a generous light-gray range, broad gentle gradients, and compressed low-contrast internal modeling. Brightness should feel like shallow rounded geometry, not a dense white solid or hard engraved metal.

### Hierarchical depth

Build in this order:

1. black base and true gaps;
2. rear silhouettes and rear ornament;
3. middle masses;
4. foreground subject;
5. small crest ridges and accents.

Rear objects must remain darker than important foreground structures.

### Edge behavior

- **Outer silhouette**: crisp against black, with a short inward bevel.
- **Overlap seam**: narrow, shallow, softly blended darker valley.
- **Internal structure**: soft raised ridge, wide low-contrast groove, or broad plane transition.

Do not use universal outlines.

## Detail-frequency balance

### Macro

Keep head, torso, limbs, large petals, garment masses, or architectural blocks smooth and continuous. Do not cover them with noise.

### Meso

Prioritize meso detail. Preserve facial planes, eyes, nostrils, joints, horn or armor segments, grouped fur, feather bands, cloth folds, jewelry, chain links, patterned panels, and other identity-bearing structures.

Meso detail should be:

- readable at normal view and thumbnail size;
- softer than ink or vector outlines;
- created with wide shallow valleys and modest soft ridges;
- broad enough to survive thumbnail viewing and fabrication.

### Micro

Use microdetail sparingly. Remove pores, paper grain, isolated dots, hairline ridges, engraving noise, dense leaf striations, and repeated texture that does not change topology.

## Line-art interpretation

| Line function | Relief interpretation |
|---|---|
| Outer contour | silhouette edge plus short inward bevel |
| Overlap boundary | narrow darker separation valley |
| Fold or muscle line | shallow groove beside a rounded plane |
| Fur, feather, scale group | medium-scale grouped ridge/groove |
| Decorative stroke | raised beveled band |
| Enclosed negative shape | base-level recess or cut-through gap |
| Hatching | infer the underlying plane; replace many stripes with a few broad folds or veins |
| Construction line | remove unless structurally meaningful |
| Source text | preserve the exact glyph and count as shallow raised/recessed geometry |

## Subject treatment

### Animals

Group torso, head, and limbs as primary masses. Keep eyes, nostrils, joints, hooves/claws, horn segments, grouped fur or feathers, and accessories readable. Make horn segments wide and softly banded; make hanging ornaments softly domed. Do not drill deep black holes into facial features.

### Human figures and portraits

Connect forehead, brow, nose, cheek, lips, and chin as shallow planes. Group hair, beard, fabric, armor, and jewelry before adding grooves. Express fabric folds as broad shallow transitions, fingers as softly separated rounded forms, and shoe soles with only a few broad grooves.

### Deities and statues

Favor smooth idealized planes, readable gestures, grouped hair/beard, jewelry bands, halo/lotus hierarchy, and restrained texture.

### Flowers and foliage

Stage petals from rear to front. Darken roots and overlaps, brighten curled tips and central ridges, and keep leaf veins few, wide, shallow, and low contrast.

### Grain, seeds, berries, and bead-like clusters

Build clustered heads from softly domed units with shallow separation and mild local merging. Preserve important gaps and overall cluster silhouette. Reject concentric center dimples, hard bead rims, sharp rings, and excessive one-by-one engraving.

### Containers and source labels

Model jars and vessels as broad rounded masses. Convert line hatching into curvature, not stripes. Keep rims, cloth covers, knots, plaques, and labels as shallow layered forms. When source text exists, preserve the exact glyph and occurrence count as clean relief geometry; add no new text.

### Dragons, clouds, and ornaments

Preserve serpentine flow and crossings. Separate coils, limbs, mane, clouds, and scrolls by depth bands. Keep scales subordinate to body volume.

### Narrative scenes

Use depth compression rather than fog. Keep background forms lower/darker, primary figures brighter, and small structural details wide enough to remain legible.

## Failure modes

### Global blur

Symptoms: anatomy, patterns, folds, grouped texture, and accessories melt into broad soft blobs.
Repair: preserve macro smoothness while restoring meso detail with shallow valleys and raised ridges.

### Hard or deeply carved output

Symptoms: dark incisions, sharp toolpath edges, metallic highlights, excessive contrast, or every fold and vein cut deeply.
Repair: widen and lighten grooves, soften internal edges, merge repetitive detail, keep outer silhouette crisp, and preserve topology.

### Dense white solid

Symptoms: most of the subject shares one bright value and depth order disappears.
Repair: lower broad main masses, darken rear layers, keep foreground accents brighter, and retain detail.

### Ordinary grayscale illustration

Symptoms: one side is lit and the other shadowed; cast shadows or rim light appear.
Repair: rebuild values from geometric height only.

### Flat emboss filter

Symptoms: every source line receives the same bevel while interiors stay flat.
Repair: build macro and meso volumes first, then add selective grooves.

### Outline persistence

Symptoms: black ink remains printed over gray surfaces.
Repair: reinterpret it as an edge, seam, overlap valley, or shallow groove.

### Noisy carving surface

Symptoms: pores, grain, isolated dots, hairlines, or excessive scales.
Repair: merge noise into wider shallow structures and prioritize meso forms.

### Cratered clustered seeds

Symptoms: each seed has a concentric ring, center pit, or hard bright rim.
Repair: rebuild as smooth domes with shallow soft separation and mild local merging.

### Source text drift

Symptoms: missing, malformed, duplicated, or newly invented characters.
Repair: restore the exact source glyphs and occurrence count while keeping the label geometry unchanged.
