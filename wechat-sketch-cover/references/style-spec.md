# Fixed Warm Hand-Drawn WeChat Cover Specification

This file is the only visual specification for wechat-sketch-cover. It defines one style, one composition, and one output size. There are no variants or user-selectable settings.

## Canvas and geometry

- Final canvas: exactly 1923 x 818 pixels, PNG.
- Descriptive ratio: approximately 2.35:1; the pixel dimensions are authoritative.
- Safe outer margin: keep important title strokes and illustration details at least 64 pixels from every edge.
- Left title zone: x=80..760, y=120..650, approximately 40% of the canvas.
- Right illustration zone: x=820..1840, y=70..750, approximately 60% of the canvas.
- Keep a clear visual gap between the zones. Do not add a divider line.

## Fixed palette

Use only this warm family:

| Role | Color |
|---|---|
| Paper background | #FCEECF |
| Paper highlight | #FEF6DB |
| Deep brown ink | #3D2418 |
| Warm brown shading | #936336 |
| Orange accent | #E96A00 |
| Golden fill | #D7A365 |

Hex values are rendering guidance. NEVER show color names, role labels, or hex values as visible text.

## Surface and rendering

- Warm cream paper with subtle grain, speckles, and faint uneven pigment.
- Deep-brown hand-drawn outlines with visible pressure variation and slight natural wobble.
- Loose pencil, pen, and marker fills with visible stroke direction.
- Minimal depth: light hatching and soft hand-drawn shadows only.
- Simple stick figures, cards, arrows, stars, checkmarks, notes, folders, screens, or content-specific objects.
- Friendly editorial sketchbook feeling: explanatory, warm, clear, and restrained.

## Fixed composition

- The exact article title is the visual anchor on the left.
- Break the title naturally into two or three large lines without changing any character.
- Use expressive Chinese brush-marker or hand-lettered forms in deep brown.
- Add one loose orange underline beneath the title and at most three small orange doodle accents.
- Place one coherent conceptual scene on the right. It must express one core meaning through physical objects and actions.
- Right-side panels may contain abstract lines, dots, or checkmarks, but no additional readable words.
- Preserve breathing room; avoid filling every gap with decoration.

## Reference image policy

assets/style-reference.png is a QA baseline only.

Compare only:

- palette and paper texture;
- hand-drawn line quality;
- title hierarchy;
- left-title/right-illustration balance;
- icon vocabulary, spacing, and visual warmth.

Ignore and never reproduce:

- the reference title;
- OfferPilot or interview-specific meaning;
- the dashboard/workbench arrangement as literal content;
- people, objects, or UI details unless independently required by the new article.

NEVER pass the reference image to image generation.

## Negative constraints

- No subtitle, tags, captions, labels, random English, letters, numbers, or additional readable text.
- No logo, watermark, brand mark, QR code, barcode, signature, or page badge.
- No photorealism, photography, realistic portrait, 3D rendering, glossy product mockup, or cinematic lighting.
- No blue-purple neon, cyberpunk, cold corporate technology style, rigid business-PPT grid, or high-saturation gradient.
- No pure-white background, pure-black ink, dense wallpaper pattern, excessive decoration, or crowded infographic.
- No title truncation, paraphrase, translation, invented punctuation, or spelling changes.

## Prompt template

Use case: infographic-diagram
Asset type: WeChat Official Account article cover

Primary request:
Generate exactly one ultra-wide warm hand-drawn notebook-style article cover.

Exact visible text:
"[TITLE]"

The quoted title is the only readable text allowed in the image. Reproduce every character exactly. Do not translate, shorten, paraphrase, add a subtitle, or add any other readable words, letters, numbers, labels, signatures, or branding.

Content context:
[SUMMARY]

Core meaning:
[CORE_MEANING]

Right-side visual metaphor:
[METAPHOR]

Content-grounded objects:
[OBJECTS]

Canvas and composition:
- Compose for an approximately 2.35:1 ultra-wide canvas that will be normalized to exactly 1923 x 818.
- Keep all important content at least 64 pixels from the canvas edges.
- Reserve the left 40% for the title: two or three large lines, deep-brown Chinese brush-marker lettering, with one loose orange underline.
- Use the right 60% for one coherent hand-drawn conceptual scene.
- Keep a clear gap between title and illustration.

Style:
- Warm cream paper background with subtle grain and speckles.
- Deep-brown, slightly imperfect hand-drawn outlines.
- Warm brown shading, orange accents, and muted golden fills.
- Loose pen, pencil, and marker texture; light hatching; minimal depth.
- Friendly editorial sketchbook mood: explanatory, warm, clear, restrained.

Constraints:
- The title must remain the dominant left-side element.
- The right side must communicate one idea, not a multi-topic infographic.
- Interface-like panels may use abstract scribble lines, dots, arrows, and checkmarks only.
- No additional readable text.
- No logo, watermark, brand mark, QR code, barcode, signature, or page badge.
- No photography, realistic people, 3D, glossy rendering, neon, cyberpunk, cold corporate technology styling, or business-PPT layout.
- No pure-white background, pure-black ink, high-saturation gradients, dense decoration, or edge-crowded content.

Generate one image only.

## QA pass

A candidate passes only when all are true:

1. The title matches the supplied title character-for-character and is readable.
2. No other readable text appears.
3. The title occupies the left zone and the content metaphor occupies the right zone.
4. Paper, palette, line quality, and texture match the fixed specification and QA reference.
5. No forbidden visual element appears.
6. The normalized PNG measures exactly 1923 x 818.
