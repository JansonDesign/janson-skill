# Prompt recipes

Use these as compact building blocks. Replace bracketed text with observations from the actual line art.

## Base edit prompt

> Use the first referenced image as the sole content and topology source. Convert its exact line-art composition into a monochrome 8-bit grayscale low-relief height map. Preserve [silhouette, pose, proportions, major overlaps, openings, symmetry, framing]. Interpret brightness strictly as height: black is the flat recessed base, dark gray is rear/shallow relief, mid-gray is body volume, and light gray is the highest surface. Replace visible ink outlines with crisp silhouette bevels, narrow overlap valleys, shallow grooves, and smooth sculpted planes. Build macro, medium, then fine relief. Use matte carved-clay/ZBrush character, continuous band-free gradients, sparse near-white peaks, and clean negative space. No color, text, new objects, cast shadows, directional lighting, rim light, glow, metallic shine, photographic texture, paper grain, or mockup surface. Do not crop.

If additional referenced images are present, add:

> The remaining references are style-only examples for grayscale depth handling; do not copy their subjects, composition, or ornaments.

## Isolated subject addition

> Place the preserved subject on a uniform black zero-height field with generous untouched negative space. Keep the silhouette crisp and model [head/torso/limbs or main parts] as continuous rounded masses. Reserve the brightest values for [named frontmost peaks].

## Dense panel addition

> Organize the panel into explicit depth bands: base/gaps 0–20, rear ornament 24–80, middle layer 80–150, foreground 145–215, peak accents 210–240. Preserve every major crossing and deepen narrow valleys at overlaps. Simplify repeated micro-detail where needed for clear carving.

## Portrait or figure addition

> Preserve identity and gesture. Model facial planes and hands with shallow continuous transitions; group hair, beard, jewelry, and fabric into medium-scale masses before adding restrained grooves. Avoid deep eye sockets, a pinched nose, waxy skin, or lighting-driven facial highlights.

## Linear ornament addition

> Convert each structurally important stroke into a clean raised beveled ribbon with a light center ridge and darker adjacent valleys. Preserve stroke-width rhythm, intersections, and enclosed negative spaces. Do not leave black outlines printed on top.

## Focused repair prompts

Use one repair at a time:

- **Lighting contamination**: “Keep the same composition and relief forms. Remove all directional illumination and cast shadows; make brightness depend only on geometric elevation.”
- **Lost topology**: “Restore the exact [opening/crossing/limb count/border path] from the source line art while preserving the current grayscale relief style.”
- **Flat interiors**: “Keep the silhouette unchanged. Replace flat filled regions with broad sculpted macro and medium-form gradients.”
- **Weak separation**: “Keep all objects in place. Deepen narrow darker valleys only where forms overlap and strengthen front-to-back value offsets.”
- **Clipped peaks**: “Reduce broad pure-white areas and recover surface gradients; reserve near-white for small ridge tips.”
- **Noisy detail**: “Remove speckles and hairline height islands; merge them into wider, shallower, manufacturable relief detail.”
- **Outline residue**: “Remove printed black contour lines and convert them into silhouette bevels, overlap valleys, or shallow structural grooves.”

## Reference asset selection

Use no more than two style assets with the source image:

- `assets/references/01-isolated-animal.png` — isolated animal, large black base.
- `assets/references/02-human-figure.png` — full figure and costume layering.
- `assets/references/03-buddha-figure.png` — statue, halo, robe, and calm smooth modeling.
- `assets/references/04-dense-dragon-panel.png` — dense multi-layer dragon/cloud panel.
- `assets/references/05-floral-screen.png` — floral/bird screen with raised borders.
- `assets/references/06-narrative-panel.png` — vertical landscape/narrative staging.

Use the closest subject family. Never let a style asset override the source line art.
