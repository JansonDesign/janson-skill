---
name: line-art-to-low-frequency-heightmap
description: Convert supplied line drawings, outline illustrations, religious figures, portraits, animals, plants, ornaments, or decorative panels into dark, soft, shallow, low-frequency monochrome grayscale height/depth maps for displacement modeling. Use when the user asks for 低频高度图、柔化灰度图、深度图、位移贴图、暗色浅浮雕高度场、宽缓坡面、弱化细节、用于 Blender/ZBrush/3ds Max/精雕/ArtCAM 建模，or says a conventional relief result looks too solid, too crisp, too bright, too detailed, or too much like a rendered embossed object.
---

# Line Art to Low-Frequency Heightmap

Convert line art into a lighting-independent displacement field. Optimize for smooth 3D reconstruction, not for a visually crisp relief illustration.

## Target standard

Default to the user-approved **dark, soft, shallow, low-frequency** profile:

- black is zero height; brighter values are higher;
- keep the subject globally dark and shallow;
- model large masses with wide continuous gradients;
- deliberately merge small seams, folds, facial grooves, and ornament detail;
- keep rear clouds, smoke, foliage, and supports close to the black base;
- concentrate high values only on a few foreground masses;
- avoid crisp bevels, engraved outlines, bright rims, and display lighting.

This is intentionally different from `line-art-to-relief-grayscale`, which favors a brighter, cleaner, more detailed relief.

## Required workflow

1. Inspect the source at full size.
2. Identify the main silhouette, object counts, limbs, hands, face, crossings, intentional openings, fragile ribbons, and front-to-back order.
3. Select black-low/white-high unless the user explicitly requests the reverse.
4. Read [references/style-spec.md](references/style-spec.md).
5. Read [references/prompt-recipes.md](references/prompt-recipes.md) before composing or repairing a prompt.
6. Use an image-generation or image-editing tool.
7. Put the source line art first in `referenced_image_paths`; it is the sole content and topology authority.
8. Use `assets/references/00-approved-dark-soft-low-frequency.png` as the default style/degree-only reference.
9. State reference roles explicitly. Never copy anatomy, objects, text, pose, or composition from the style reference.
10. Inspect the output at full size and thumbnail scale. Iterate only against one named defect.
11. Normalize the selected output with `scripts/finalize_heightmap.py`.
12. Deliver the 8-bit single-channel PNG and state polarity. Do not claim CNC readiness without machine-specific validation.

## Height construction

Build in three frequencies:

- **Low frequency — primary:** head, torso, limbs, large garment masses, main petals, clouds, waves, and overall depth order.
- **Medium frequency — restrained:** facial identity, main fingers, major folds, vessel rims, important crossings, and large ornament divisions.
- **High frequency — normally remove:** pores, hairlines, dense folds, repeated hatch marks, scale-by-scale texture, tiny veins, and decorative noise.

Preserve topology before detail. It is acceptable for minor internal lines to merge when the main silhouette, part counts, gestures, crossings, and recognizable masses remain correct.

Use broad plane changes and wide soft valleys. Do not convert every ink line into a ridge or incision.

## Default height bands

Treat these as prompt targets, not forced pixel values:

- base and true gaps: 0–8;
- far rear forms and nearly recessed ribbons: 15–65;
- middle garment, hair, supports, and secondary masses: 55–125;
- main face, torso, limbs, knees, and foreground masses: 105–190;
- sparse crest areas: 185–225;
- near-white 240–255: normally below 0.5% of subject pixels.

Prefer a subject mean near 75–115, standard deviation near 45–65, P95 near 175–210, and border maximum no higher than 2. Use these as diagnostics; topology and the user-approved visual degree take priority.

## Subject rules

### Figures and deities

Keep the head shape, calm facial mass, hands, finger-count rhythm, gesture, leg crossings, and feet recognizable. Merge eyelids, lips, fingers, jewelry, and garment folds into soft rounded groups rather than sharp carving.

### Decorative panels

Push rear ornament and negative structures toward black. Keep foreground masses brighter but avoid making the entire panel a pale solid.

### Linear smoke, ribbons, stems, and scrolls

Keep the path and continuity, but allow them to sit very low and dark. Widen fragile strokes enough to survive displacement; avoid bright raised wires.

### Text

Preserve source text only when present. If exact glyph fidelity cannot survive the requested softness, keep the label geometry and ask before sacrificing legibility. Add no text.

## Generation contract

Include:

- exact source topology, object counts, pose, framing, and major openings;
- monochrome grayscale height semantics;
- global darkness and shallow depth;
- broad low-frequency gradients and intentionally reduced detail;
- black uniform base without glow;
- no crop unless requested.

Exclude:

- material rendering, directional lighting, cast shadows, rim light, glow, metallic shine;
- printed outlines, hard bevels, toolpath-like grooves, crisp embossed edges;
- color, texture, pores, speckles, paper grain, watermark, or new objects;
- broad white slabs or a uniformly pale subject.

## Focused repairs

Change one defect and preserve everything else:

- **Too solid or crisp:** lower broad values, darken rear layers, widen transitions, and merge small seams into low-frequency masses.
- **Too bright:** lower the main and rear bands while keeping sparse peak locations unchanged.
- **Too dark:** raise only the main foreground masses and a few crests; keep the base and rear layers unchanged.
- **Too blurred structurally:** restore only face identity, main fingers, major crossings, and object boundaries as broad soft valleys; do not restore line-art sharpness.
- **Weak depth order:** adjust rear/middle/front value offsets without adding outlines.
- **Bright wire-like ribbons:** lower and widen smoke, stems, and ribbons while preserving their paths.
- **Halo or glow:** restore a uniform black base and remove edge haze.

Stop when the output matches the approved low-frequency degree. Do not regenerate for stylistic novelty.

## Validation gates

Reject or repair when:

1. main silhouette, pose, part counts, or crossings drift;
2. black-low/white-high polarity is inconsistent;
3. lighting or shadow controls the values;
4. the subject becomes a bright solid;
5. small details remain sharper than the approved degree;
6. face, hands, or key crossings disappear completely;
7. gradients show banding, halos, speckles, or isolated islands;
8. the border is not black;
9. the output is not an 8-bit single-channel PNG.
