---
name: line-art-to-relief-grayscale
description: Convert a supplied line drawing, outline illustration, ink drawing, logo-like ornament, figure, animal, floral motif, religious image, or narrative panel into a sculptural grayscale relief/height-map image for carving, CNC, laser engraving, ZBrush-style relief reference, or embossed artwork. Use when the user asks for 线稿转灰度图、浮雕灰度图、雕刻灰度图、精雕图、深浅层次图、height map、relief map、embossed grayscale, or wants an existing line-art pattern rendered with black-base continuous raised grayscale depth.
---

# Line Art to Relief Grayscale

Convert line art into a coherent relief height field rather than a lit black-and-white picture. Treat pixel brightness as height: black is the base/recess, dark gray is a rear or shallow layer, mid-gray is the body, and light gray is the highest surface.

## Required workflow

1. Inspect the input with an image viewer before editing.
2. Identify the subject, closed shapes, overlaps, negative spaces, intended symmetry, fragile thin details, and likely front-to-back order.
3. Ask only when height polarity or a major overlap is genuinely ambiguous. Otherwise use black-low/white-high.
4. Select one profile:
   - **Isolated subject**: animal, person, deity, single flower, emblem.
   - **Dense decorative panel**: dragon/cloud panel, landscape, furniture panel, multi-object scene.
   - **Portrait or figure**: face, bust, full-body character.
   - **Linear ornament**: border, scrollwork, calligraphic or ribbon-like pattern.
5. Read [references/style-spec.md](references/style-spec.md). Read [references/prompt-recipes.md](references/prompt-recipes.md) when composing or repairing a generation prompt.
6. Use the image-generation/image-editing tool. Preserve the source line art as the content and topology authority.
7. When the target has a local path, include it first in `referenced_image_paths`; optionally add 1–2 relevant style assets from `assets/references/`. State which image is the content source and which images are style-only references.
8. When the target exists only as a recent conversation image, include the smallest sufficient number of recent images and rely on the written style specification; do not mix recent-image inclusion with local reference paths.
9. Inspect the result at full view and thumbnail scale. Iterate only against a named defect.
10. Deliver the final raster and state the polarity. Do not claim CNC readiness unless the result passes the height-map checks below.

## Height construction rules

- Preserve silhouette, pose, framing, relative proportions, major internal divisions, and intentional openings.
- Remove visible ink strokes as strokes. Reinterpret them as boundaries, ridges, grooves, seams, folds, or changes of plane.
- Build three scales of relief:
  - **Macro**: silhouette and global front/back layering.
  - **Meso**: muscles, petals, cloth folds, feathers, clouds, facial planes, architectural masses.
  - **Micro**: shallow veins, hair strands, scales, engraved motifs, edge grooves.
- Separate overlapping objects with narrow darker valleys and value offsets, not cast shadows.
- Use broad, smooth gradients across rounded forms. Place highlights on geometric high points and ridge centers, not according to a dramatic light source.
- Keep the base/background flat and quiet. Use black for empty base in the default profile.
- Reserve near-white for a small number of true peaks. Keep useful highlight headroom.
- Keep delicate details thick enough to survive downsampling and carving. Simplify repeated micro-detail before it becomes noise.
- Avoid texture that changes the height meaning: paper grain, photographic noise, metallic sparkle, glossy specular glare, atmospheric fog, and directional cast shadows.

## Profile guidance

### Isolated subject

Use a black field with strong negative space. Keep most subject values between dark gray and light gray; use white sparingly on the foremost face, chest, beak, knuckles, jewelry, or ridge tips. Model volume continuously rather than outlining it.

### Dense decorative panel

Assign explicit depth bands before fine detail:

- Base and cut-through gaps: 0–20
- Rear ornament/background: 24–80
- Middle layer: 80–150
- Foreground body: 145–215
- Peak accents: 210–240

Allow soft transitions inside a layer while preserving clear separation at overlaps. Reduce micro-detail where layers are already crowded.

### Portrait or figure

Prioritize recognizable head shape, facial planes, hands, and garment hierarchy. Use shallow facial transitions; avoid deep eye sockets, pinched nostrils, waxy skin, or a bright nose caused by simulated lighting. Keep hair, beard, and cloth as grouped masses with secondary grooves.

### Linear ornament

Convert each important stroke into a beveled raised band: darkest at the adjacent base or groove, rising through mid-gray, and lightest near the center ridge. Preserve stroke width rhythm and crossings. Do not leave a black outline sitting on top of gray fill.

## Generation contract

Include these ideas in the edit request:

- exact composition and topology from the supplied line art;
- monochrome 8-bit grayscale relief/height-map semantics;
- black low base and white high peaks;
- matte sculpted clay or CNC relief character;
- continuous, band-free gradients;
- no color, text, new objects, photographic lighting, cast shadows, glow, metallic shine, or background texture;
- no cropping unless requested;
- high resolution and crisp silhouette with smooth internal modeling.

Use the profile-specific recipes in [references/prompt-recipes.md](references/prompt-recipes.md) rather than pasting every reference rule into one oversized prompt.

## Validation gates

Reject or repair the result when any gate fails:

1. **Topology**: silhouette, openings, crossings, count of major parts, and pose still match.
2. **Polarity**: higher surfaces are consistently brighter; recesses and gaps are darker.
3. **Lighting independence**: no cast shadow, one-sided studio lighting, rim light, or glossy highlight overrides height.
4. **Layer separation**: front, middle, and rear forms remain readable in grayscale and at thumbnail size.
5. **Continuity**: gradients are smooth, with no posterization, abrupt airbrush blobs, or accidental halos.
6. **Carvability**: no isolated bright specks, hairline ridges, noisy pores, or floating height islands.
7. **Range**: black base remains stable; near-white is limited to high points; the subject does not collapse into flat mid-gray.
8. **Clean output**: no color cast, watermark, labels, mockup surface, frame added without instruction, or unrelated ornament.

## Repair language

Name the defect and preserve everything else:

- “Remove directional lighting and cast shadows; encode brightness only as geometric height.”
- “Deepen the narrow separation valleys between overlapping forms without changing the silhouette.”
- “Replace the dark outline with a beveled relief transition.”
- “Reduce clipped white areas; reserve near-white for small peak ridges.”
- “Smooth blotchy gradients while retaining the same front-to-back depth order.”
- “Simplify noisy micro-detail and strengthen medium-scale forms for carving legibility.”

Stop after a clean validated result. Do not keep regenerating merely for stylistic novelty.
