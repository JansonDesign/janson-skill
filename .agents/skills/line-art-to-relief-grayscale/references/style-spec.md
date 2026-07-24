# Relief grayscale style specification

## Contents

- Reference-set evidence
- Core visual grammar
- Line-art interpretation
- Subject-specific treatment
- Failure modes

## Reference-set evidence

This specification was distilled from 300 source images spanning isolated animals, people, Buddhist figures, floral screens, landscapes, narrative scenes, dense dragon/cloud panels, furniture panels, and ornamental motifs.

Across the full set:

| Metric | Median | Middle 50% |
|---|---:|---:|
| Image width | 1099 px | 668–1818 px |
| Image height | 1103 px | 779–2118 px |
| Mean gray value | 73.6 | 47.9–103.7 |
| Standard deviation | 70.3 | 60.5–83.4 |
| Near-black pixels (0–15) | 44.4% | 23.4–63.3% |
| Near-white pixels (240–255) | 0.43% | 0.09–2.52% |
| Midtone pixels (48–207) | 40.8% | 26.8–54.1% |
| 95th percentile value | 209 | 183–231 |

Interpret these as a style envelope, not a mandatory histogram. The dominant pattern is large black base area, substantial continuous midtones, and restrained near-white peaks.

Category differences matter:

- Isolated zodiac/animal images use very large black fields and compact smooth forms.
- Figures and statues use softer macro modeling and low edge activity.
- Landscapes and dense panels use more midtones, higher local edge activity, and explicit multi-layer staging.
- Furniture/panel sets may use a brighter overall field because the whole rectangle participates in the relief.

## Core visual grammar

### Height, not illumination

Read value as elevation. A bright patch means a physically higher surface, not simply a surface facing a lamp. This is the defining distinction from ordinary grayscale rendering.

### Low-relief compression

Compress a three-dimensional subject into a shallow depth range. Preserve important overlaps by assigning front-to-back value offsets. Avoid full 3D perspective protrusion that would create extreme depth or undercuts.

### Hierarchical depth

Establish depth in this order:

1. base field and cut-through negative spaces;
2. rear silhouettes and background ornament;
3. middle masses;
4. foreground subject;
5. local crests and engraved detail.

Do not let a local highlight on a rear object become brighter than the main foreground without a clear structural reason.

### Edge behavior

Use three edge types deliberately:

- **Outer silhouette**: crisp boundary against the base with a short inward bevel.
- **Overlap seam**: narrow dark valley separating two masses.
- **Internal form transition**: broad gradient or shallow groove.

Avoid universal black outlines. They look printed and often invert the implied height at the edge.

### Value economy

Use the deepest black for base and true gaps. Use dark gray for receding planes. Concentrate the visual information in midtones. Use near-white only for a few highest ridges, facial centers, jewelry, flower tips, horn edges, or frontmost accents.

### Surface character

Aim for matte carved clay, wax, wood master, or ZBrush height-map character. Keep gradients clean and slightly idealized. Avoid real-material albedo, pores, reflections, and photographic texture.

## Interpreting line art

Treat line function before assigning height:

| Line function | Relief interpretation |
|---|---|
| Outer contour | silhouette edge and short inward bevel |
| Overlap boundary | darker separation valley |
| Fold or muscle line | shallow groove beside a rounded plane |
| Vein, feather, scale, hair | low-amplitude secondary ridge/groove |
| Decorative stroke | raised beveled band |
| Enclosed negative shape | base-level recess or cut-through gap |
| Hatching | infer the surface plane; do not reproduce every hatch |
| Construction/sketch line | remove unless structurally meaningful |

When a line can represent either an edge or a printed mark, prefer the interpretation that produces a manufacturable continuous surface and preserves the subject’s identity.

## Subject-specific treatment

### Animals

Group torso, head, and limbs as primary masses. Use fur, feather, or scales as shallow secondary modulation. Keep eyes, nostrils, claws, and teeth legible without drilling deep black holes.

### Human figures and portraits

Model forehead, brow, nose, cheek, lips, and chin as connected planes. Keep eye sockets shallow. Group hair and fabric into large locks/folds before adding grooves. Hands and faces receive more value separation than minor costume texture.

### Deities and statues

Favor calm symmetry, smooth idealized planes, readable hand gestures, jewelry bands, halo/lotus layering, and restrained surface noise. Separate the figure from halo and throne with explicit darker bands.

### Flowers and foliage

Stage petals from back to front. Darken petal roots and overlap valleys; brighten curled tips and central ridges. Keep stems as tapered raised bands and leaves as broad planes with shallow veins.

### Dragons, clouds, and ornaments

Maintain continuous serpentine flow. Separate body coils, limbs, mane, and clouds by depth bands. Treat cloud scrolls and border motifs as beveled ribbons. Prevent dense scale texture from overpowering body volume.

### Narrative landscapes

Use atmospheric depth only as height compression, not fog. Keep background mountains low/dark, architecture and trees mid-level, and key figures/foreground objects higher/brighter. Use negative gaps to keep small scenes legible.

## Failure modes

### Ordinary grayscale illustration

Symptoms: one side bright, the other dark; cast shadows; rim light; dramatic studio lighting.

Repair: remove illumination logic and rebuild value from geometric height.

### Flat emboss filter

Symptoms: every line receives the same bevel; interiors remain flat; the result resembles a software effect.

Repair: construct macro and medium volumes first, then add selective edge bevels.

### Plastic or chrome look

Symptoms: sharp specular streaks, glossy hotspots, metallic reflections.

Repair: request matte sculpted material and diffuse height gradients.

### Muddy layering

Symptoms: adjacent objects share one gray value; overlaps disappear.

Repair: assign explicit depth bands and deepen only the junction valleys.

### Outline persistence

Symptoms: black ink remains on top of gray surfaces.

Repair: reinterpret the line as an edge, groove, or seam.

### White clipping

Symptoms: broad white patches lose surface form.

Repair: lower high values and reserve 240–255 for tiny peaks.

### Noisy carving surface

Symptoms: pores, grain, isolated dots, hairline ridges, too many scales.

Repair: remove micro-noise, widen important details, and prioritize silhouette plus medium-scale form.
