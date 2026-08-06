---
title: Creating transparent materials
source: https://docs.kanzi.com/4.1.0/en/working-with/materials/creating-transparent-materials.html
---

# Creating transparent materials


To create a transparent material:

1.

Create or select a material and assign it to a node. See Using materials.
2.

In the Library > Materials and Textures > Materials select the material and in the Properties set:

  - Blend Mode to one of these values:

    - Alpha: Automatic

Sets the blend mode to either:

      - Alpha: Premultiplied when the Premultiply Alpha property for the project or an image is enabled. This is the default value.
      - Alpha: Mixed when the Premultiply Alpha property for the project or an image is disabled.


See Alpha premultiplication.
    - Alpha: Premultiplied

Expects premultiplied alpha RGBA in the source pixels, and uses the alpha of the source pixels to blend the source pixels on top of the destination pixels.

This mode is the default and recommended mode for alpha blending, and equivalent to the Porter-Duff **Source Over** mode.
    - Alpha: Mixed

Expects non-premultiplied alpha RGBA in the source pixels, and blends the source pixels with the destination pixels.

For example, use this mode when you dynamically load without preprocessing a texture that uses a fragment shader which does not perform alpha-premultiplication of the RGB color.
    - Additive

Adds the source pixels to the destination pixels.

Use this mode for effects where you want a layer to add color, but not reduce the color of the underlying layer. [](../../_images/blend-modes.svg)

See Blend modes.

  - Blend Intensity to the amount of transparency for your material, where 0 is completely transparent and 1 opaque.
