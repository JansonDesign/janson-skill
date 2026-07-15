---
name: line-drawing-transfer
description: Convert portrait, couple, wedding, and full-body photographs into a sparse black-and-white line-engraving illustration with thick contours, generous paper-white negative space, broken short-line transitions, and restrained deep-shadow cross-hatching. Use when the user asks for 线稿转绘, 黑白线稿, 版画转绘, 钢笔线描, engraving portrait, or wants a photo to match this established portrait illustration style.
---

# Line Drawing Transfer

Use this skill with the `imagegen` skill. Treat the supplied photo as the edit target and any approved prior output as a style reference.

## Style Contract

- Preserve the recognizable people, expressions, poses, clothing, key accessories, and requested crop. For wedding images, preserve both people, their linked pose, wedding attire, bouquet, and relative scale.
- Render only pure black ink on clean white paper. Remove watermarks and unwanted photo backgrounds unless the user asks to retain a scene.
- Use thick, confident outer contours and major structural lines. Keep the main stroke weight visibly heavier than the interior hatching.
- Reserve broad white-paper areas on light-facing face planes, hands, garments, and the background. Do not fill midtones with texture.
- Use sparse, widely spaced directional hatching to describe volume. At every shadow-to-light transition, resolve the hatching into 3 to 5 clearly separated short broken dashes with generous white gaps.
- Use restrained cross-hatching only in the deepest recesses: hair mass, eye sockets, nostrils, beneath the nose and lower lip, under the chin, overlapping fingers, deep garment folds, and similarly occluded areas.
- Simplify intricate materials such as lace, embroidery, foliage, or bouquets into elegant line motifs rather than dense photorealistic detail.

## Workflow

1. Read the `imagegen` skill and inspect the local target image with `view_image` before editing.
2. Identify invariants: subject identity, pose, expression, garment, props, and framing. If a prior approved result exists, include it as the style reference.
3. Use built-in image editing with a compact structured prompt. State that the target image controls identity and composition; the reference controls style only.
4. Specify the style contract, then explicitly forbid gray wash, color, halftone, stippling, pencil texture, uniform fine hatching, text, borders, and watermarks.
5. Inspect the result. If needed, iterate on only one property at a time: line weight, white space, broken transition strokes, cross-hatching, or background simplification.

## Prompt Scaffold

```text
Use case: style-transfer
Asset type: monochrome line-engraving illustration
Input images: Image 1 is the edit target; Image 2 is only the style reference.
Subject: preserve [identity, expression, pose, clothing, props, crop].
Scene/backdrop: [plain white paper / simplified scene requested by the user].
Style/medium: bold black ink engraving on clean white paper; thick confident contours; broad negative space; sparse directional hatching.
Line treatment: resolve every shadow-to-light transition into 3 to 5 separated short broken dashes with ample white gaps.
Shadows: limited cross-hatching only in the deepest recesses.
Constraints: change rendering style only; preserve stated invariants.
Avoid: gray wash, color, halftone, stippling, pencil texture, dense uniform linework, text, borders, watermarks, extra objects.
```

## Background Choice

- Default to a blank white-paper background for close portraits, selfies, or when the original background distracts from the subject.
- For full-body wedding or couple portraits, retain only sparse contextual outlines of important scenery when they support the composition; keep them visibly lighter and simpler than the people.
- Keep the original background only when the user explicitly asks for it.
