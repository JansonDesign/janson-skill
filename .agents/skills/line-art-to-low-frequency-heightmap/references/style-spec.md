# Dark soft low-frequency height-map standard

## Contents

- Approved baseline
- Visual grammar
- Frequency balance
- Value hierarchy
- Subject handling
- Failure modes

## Approved baseline

Use `../assets/references/00-approved-dark-soft-low-frequency.png` as the default degree-only reference.

It establishes:

- a uniform black or near-black zero-height field;
- an overall dark, shallow subject;
- broad merged gradients instead of crisp relief edges;
- reduced medium and high-frequency detail;
- rear smoke, clouds, waves, and supports close to the base;
- high values concentrated on a few foreground masses;
- no material lighting, cast shadow, or printed outline.

The reference controls softness, darkness, height compression, detail frequency, and peak distribution only. The source line art remains the sole authority for anatomy, objects, pose, text, and composition.

## Visual grammar

### Height, not illumination

Brightness means elevation. A light face or hand is higher, not illuminated. Do not add a light direction, cast shadow, rim light, ambient occlusion, or glossy highlight.

### Low-frequency first

Treat the image like a smooth terrain field:

1. establish black base and major silhouette;
2. place rear, middle, and foreground masses;
3. connect each mass with wide continuous ramps;
4. recover only essential identity details;
5. suppress everything that reads as engraving or surface texture.

### Softness

Use broad transitions comparable to a heavily smoothed displacement map. Internal boundaries may be visible but must not become crisp bevels. Avoid narrow dark seams and bright edge rims.

### Darkness

Keep most of the subject in dark-to-mid gray. Bright values should be spatially concentrated, not spread across every object.

## Frequency balance

### Preserve

- main silhouette and pose;
- face orientation and primary facial mass;
- arm, hand, finger-count rhythm, leg, and foot topology;
- major garment panels and crossings;
- major petals, clouds, waves, vessels, and ribbons;
- exact object counts and intentional openings.

### Merge

- small garment folds;
- individual hair strands;
- minor finger creases;
- eyelid and lip incisions;
- repeated leaf veins, scales, feathers, hatching, and ornament bands;
- tiny cloud curls and secondary surface marks.

## Value hierarchy

Default working bands:

| Layer | Target range |
|---|---:|
| Base and true gaps | 0–8 |
| Far rear / nearly recessed | 15–65 |
| Middle / secondary masses | 55–125 |
| Main foreground masses | 105–190 |
| Sparse crests | 185–225 |

Diagnostic envelope:

- subject mean: approximately 75–115;
- subject standard deviation: approximately 45–65;
- subject P95: approximately 175–210;
- near-white subject pixels: below 0.5%;
- border maximum: no higher than 2.

Do not chase metrics at the expense of topology or the approved visual degree.

## Subject handling

### Figures and deities

Connect forehead, brow, nose, cheek, lips, and chin as one soft facial volume. Keep the face readable without sharp eye sockets or lip lines. Model hands and fingers as grouped rounded forms; preserve count rhythm and gesture but soften separations.

Push rear robes and clouds down. Keep face, selected hands, knees, and foot crests as the principal high zones.

### Smoke, ribbons, stems, and scrolls

Keep continuity and path. Render them as low, dark, broad ribbons rather than bright wires. It is acceptable for far segments to approach the base.

### Dense ornament

Compress secondary ornament into large families of height. Remove one-by-one engraving detail.

## Failure modes

### Crisp display relief

Symptoms: clean bevels, sharp folds, bright borders, every object independently raised.

Repair: widen transitions, lower the subject, merge small structures, and remove bright edge ridges.

### Pale solid

Symptoms: most of the subject is light gray or white, with weak depth order.

Repair: lower broad values and push rear layers toward black while preserving sparse peaks.

### Featureless blur

Symptoms: face, hands, gestures, and major crossings disappear.

Repair: restore only essential medium-scale structure with wide soft valleys.

### Lighting contamination

Symptoms: one side is bright, the other dark, or cast shadows appear.

Repair: rebuild values by depth bands only.

### Wire-like fragile elements

Symptoms: smoke, stems, or ribbons become bright narrow tubes.

Repair: lower, widen, and soften them while preserving their paths.

### Edge halo

Symptoms: a gray glow surrounds the subject on black.

Repair: restore a stable black base and shorten the silhouette transition.
