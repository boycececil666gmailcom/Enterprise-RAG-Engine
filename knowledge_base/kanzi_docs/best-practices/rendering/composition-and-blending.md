---
title: Composition and blending
source: https://docs.kanzi.com/4.1.0/en/best-practices/rendering/composition-and-blending.html
---

# Composition and blending

Composition makes it possible to draw layered graphics where you can control the look of each layer, which depends on the look of its underlying layer.

Blending combines a translucent upper layer with a lower layer, producing a new blended color. The alpha channel of the upper layer sets the opacity of the layer.

To set how Kanzi blends two layers, use the Blend Mode property. See Blend modes.

During compositing and blending Kanzi expects the input texture data to have premultiplied alpha, and Kanzi outputs premultiplied alpha. Kanzi supports complex compositing of multiple layers and you can use the output from Kanzi with an external compositing window manager.
## Alpha premultiplication

RGBA pixels have values for the red, green, and blue color channels, and the alpha channel, which determines the pixel opacity. To achieve alpha blending, Kanzi premultiplies the RGB channels from texture data with an alpha value.

```
{Red * Alpha, Green * Alpha, Blue * Alpha, Alpha}

```

The use of texture data makes texture filtering and interpolation work correctly with alpha.

The shaders that come with Kanzi are designed to output RGBA values with premultiplied alpha. When you write shaders, you must multiply the output RGB values of the fragment with its alpha value. This way the color values of the pixels in partially transparent nodes do not bleed outside the edges of the partially transparent area and you avoid issues, such as white edges around partially transparent nodes.

Kanzi Studio by default multiplies the RGB values with the alpha value when you export a kzb file.

To change this setting, in the Project > Properties use the Premultiply Alpha property. You can override this value in the properties of the image file where you want to use a different setting.

For example, set Premultiply Alpha to False for the images of those textures that your Kanzi application loads dynamically without preprocessing, and that use a fragment shader which does not perform alpha premultiplication of the RGB color.
## Blend modes

To set how to combine the color and alpha values of pixels in one layer (source), with those of the pixels in another layer (destination), use the Blend Mode property.

The value of the Blend Mode property that you set in a node or render pass overrides the value of that property set in the material used by the node or render pass.
### Color blending modes

This section describes the color blending modes in Kanzi.

Each description includes:

- The equations that Kanzi uses to compute the result color (\(C_{out}\)) and alpha (\(Î±_{out}\)) of the composition of the source (\(src\)) and destination (\(dst\)).
- Visualization of how the blend mode operates on overlapping source and destination images with opaque (left) or partially transparent (right) content:

|  |   |

Opaque |

Partially transparent |
|  |

Destination (\(dst\)) |    |    |
|  |

Source (\(src\)) |    |    |
#### Alpha: Premultiplied

|

Expects premultiplied alpha RGBA in the source pixels, and uses the alpha of the source pixels to blend the source pixels on top of the destination pixels.

This mode is the default and recommended mode for alpha blending, and equivalent to the Porter-Duff **Source Over** mode.   \[\begin{split}&C_{out} = C_{src} + (1 - Î±_{src}) * C_{dst} \\ &Î±_{out} = Î±_{src} + (1 - Î±_{src}) * Î±_{dst}\end{split}\]   |    |    |
#### Additive

|

Adds the source pixels to the destination pixels.

Use this mode for effects where you want a layer to add color, but not reduce the color of the underlying layer.   \[\begin{split}&C_{out} = C_{src} + C_{dst} \\ &Î±_{out} = Î±_{src} + Î±_{dst}\end{split}\]   |    |    |
#### Multiply

|

Multiplies the source and destination pixels.

This mode is the opposite of the Screen mode.

For example, you can use this mode to create a partially transparent overlay that is darker than its backdrop. See Using color blending to create an overlay.   \[\begin{split}&C_{out} = C_{dst} * C_{src} \\ &Î±_{out} = Î±_{dst} * Î±_{src}\end{split}\]   |    |    |
#### Screen

|

Adds the source and destination pixels and subtracts from the result the product of the source and destination.

This mode is the opposite of the Multiply mode.

For example, you can use this mode to create a partially transparent overlay that is lighter than its backdrop. See Using color blending to create an overlay.   \[\begin{split}&C_{out} = C_{src} + (1 - C_{src}) * C_{dst} \\ &Î±_{out} = Î±_{src} + (1 - Î±_{src}) * Î±_{dst}\end{split}\]   |    |    |
#### Alpha: Automatic

Sets the blend mode to either:

- Alpha: Premultiplied when the Premultiply Alpha property for the project or an image is enabled. This is the default value.
- Alpha: Mixed when the Premultiply Alpha property for the project or an image is disabled.

See Alpha premultiplication.
#### Alpha: Non-premultiplied

Legacy mode. For non-premultiplied input use the Alpha: Mixed mode instead.

The Alpha: Non-premultiplied mode expects non-premultiplied alpha RGBA in the source pixels, and blends the source pixels with the destination pixels. Note that this results in an incorrect alpha channel in the destination framebuffer. You cannot use this mode when rendering to a texture which is later blended as a foreground.
#### Alpha: Mixed

|

Expects non-premultiplied alpha RGBA in the source pixels, and blends the source pixels with the destination pixels.

For example, use this mode when you dynamically load without preprocessing a texture that uses a fragment shader which does not perform alpha-premultiplication of the RGB color.   \[\begin{split}&C_{out} = Î±_{src} * C_{src} + (1 - Î±_{src}) * C_{dst} \\ &Î±_{out} = Î±_{src} + (1 - Î±_{src}) * Î±_{dst}\end{split}\]   |    |    |
### Alpha compositing modes

This section describes the Porter-Duff blend modes in Kanzi. The Porter-Duff blend modes were defined by Thomas Porter and Tom Duff in their 1984 paper [Compositing Digital Images](https://graphics.pixar.com/library/Compositing/paper.pdf).

Use the Porter-Duff blend modes for alpha compositing. The Porter-Duff blend modes combine two layers based on the alpha channels of those layers. If the target framebuffer does not have alpha channel, or the alpha value is constant 1, many of the alpha compositing modes can produce unintuitive but correct results. For example, the Source Out mode produces the same result as the Clear blend mode.

When you use alpha compositing, make sure that the alpha channel of the render target is suitable for alpha compositing. For example:

- Use a parent node which you composite by enabling the Node 2D > Force Composition property. This way you render the nodes to a cleared render target.
- If the window surface is translucent, use the Clear blend mode to clear the target framebuffer.

By default Kanzi composites nodes using the Alpha: Premultiplied mode, which corresponds to the Porter-Duff **Source Over** mode.

In Kanzi to achieve the behavior of the Porter-Duff **Destination** or **Source** mode, in the destination or source node disable the Node > Visibility property.

Each description includes:

- The equations that Kanzi uses to compute the result color (\(C_{out}\)) and alpha (\(Î±_{out}\)) of the composition of the source (\(src\)) and destination (\(dst\)).
- Visualization of how the blend mode operates on overlapping source and destination images with opaque (left) or partially transparent (right) content:

|  |   |

Opaque |

Partially transparent |
|  |

Destination (\(dst\)) |    |    |
|  |

Source (\(src\)) |    |    |
#### Opaque

|

Replaces the destination pixels with the source pixels.

This mode is equivalent to the Porter-Duff **Source** mode.   \[\begin{split}&C_{out} = C_{src} \\ &Î±_{out} = Î±_{src}\end{split}\]   |    |    |
#### Clear

|

Sets the destination pixels to transparent black.   \[\begin{split}&C_{out} = 0 \\ &Î±_{out} = 0\end{split}\]   |    |    |
#### Exclusive Or

|

Draws the non-overlapping source and destination pixels. In the overlapping source and destination pixels reduces the source alpha by the inverse of the destination alpha, and the destination alpha by the inverse of the source alpha, then merges the pixels.   \[\begin{split}&C_{out} = (1 - Î±_{dst}) * C_{src} + (1 - Î±_{src}) * C_{dst} \\ &Î±_{out} = (1 - Î±_{dst}) * Î±_{src} + (1 - Î±_{src}) * Î±_{dst}\end{split}\]   |    |    |
#### Source Atop

|

Discards those source pixels that do not cover destination pixels, and draws the rest of the source pixels over destination pixels.   \[\begin{split}&C_{out} = Î±_{dst} * C_{src} + (1 - Î±_{src}) * C_{dst} \\ &Î±_{out} = Î±_{dst}\end{split}\]   |    |    |
#### Source In

|

Draws those source pixels that cover destination pixels, and discards all destination pixels.   \[\begin{split}&C_{out} = Î±_{dst} * C_{src} \\ &Î±_{out} = Î±_{dst} * Î±_{src}\end{split}\]   |    |    |
#### Source Out

|

Draws the source pixels with alpha reduced by the inverse of the destination alpha, and discards all destination pixels.   \[\begin{split}&C_{out} = (1 - Î±_{dst}) * C_{src} \\ &Î±_{out} = (1 - Î±_{dst}) * Î±_{src}\end{split}\]   |    |    |
#### Destination Atop

|

Discards those destination pixels that are not covered by source pixels, and draws the rest of the destination pixels over source pixels.   \[\begin{split}&C_{out} = Î±_{src} * C_{dst} + (1 - Î±_{dst}) * C_{src} \\ &Î±_{out} = Î±_{src}\end{split}\]   |    |    |
#### Destination In

|

Draws only those destination pixels that intersect with the source pixels, and discards all source pixels.

You can use this blend mode to implement a mask effect. See Using alpha compositing to create a mask effect.   \[\begin{split}&C_{out} = Î±_{src} * C_{dst} \\ &Î±_{out} = Î±_{src} * Î±_{dst}\end{split}\]   |    |    |
#### Destination Out

|

Draws the destination pixels with alpha reduced by the inverse of the source alpha, and discards all source pixels.

You can use this blend mode to implement an inverse mask effect.   \[\begin{split}&C_{out} = (1 - Î±_{src}) * C_{dst} \\ &Î±_{out} = (1 - Î±_{src}) * Î±_{dst}\end{split}\]   |    |    |
#### Destination Over

|

Draws the destination pixels over the source pixels.   \[\begin{split}&C_{out} = (1 - Î±_{dst}) * C_{src} + C_{dst} \\ &Î±_{out} = (1 - Î±_{dst}) * Î±_{src} + Î±_{dst}\end{split}\]   |    |    |
### Advanced color blending modes

This section describes the advanced color blending modes in Kanzi. When using OpenGL or OpenGL ES, these modes require the `GL_KHR_blend_equation_advanced` and `GL_KHR_blend_equation_advanced_coherent` extensions. When using Vulkan these modes require the `VK_EXT_blend_operation_advanced` extension.

Each description includes:

- The equation that Kanzi uses to compute the result color (\(C_{out}\)) of the composition of the source (\(src\)) and destination (\(dst\)).

All advanced color blending modes use this equation to compute the result alpha:   \[Î±_{out} = Î±_{src} + (1 - Î±_{src}) * Î±_{dst}\]
- Visualization of how the blend mode operates on these overlapping source and destination images:

|  |

Destination (\(dst\)) |    |    |
|  |

Source (\(src\)) |    |    |
#### Multiply (advanced khr)

|

Multiplies the source and destination, resulting in a darker color. This mode is otherwise similar to the Multiply mode, but it handles alpha in the same way as the Screen mode.   \[C_{out} = C_{dst} * C_{src}\]   |    |    |
#### Overlay

|

Combines the Multiply and Screen modes. Where the destination is light, the source becomes lighter, and where the destination is dark, the source becomes darker. This mode preserves the highlights and shadows in the destination. |    |    |       \[\begin{split}&C_{out} = \begin{cases} 2 * C_{src} * C_{dst} & \text{if } C_{dst} <= 0.5\\ 1 - 2 * (1 - C_{src}) * (1 - C_{dst}) & \text{otherwise} \end{cases}\end{split}\]
#### Darken

|

Compares the colors of the destination and source and selects the darker one.   \[C_{out} = min(C_{dst}, C_{src})\]   |    |    |
#### Lighten

|

Compares the colors of the destination and source and selects the lighter one.   \[C_{out} = max(C_{dst}, C_{src})\]   |    |    |
#### Color Burn

|

Darkens the destination to reflect the color of the source, producing a result with higher contrast, saturated mid-tones, and reduced highlights. White source color produces no change.

This mode is the opposite of the Color Dodge mode.  |    |    |       \[\begin{split}&C_{out} = \begin{cases} 1 & \text{if } C_{dst} >= 1\\ 1 - min(1, \frac{1 - C_{dst}}{C_{src}}) & \text{if } C_{dst} < 1 \text{ and } C_{src} > 0\\ 0 & \text{if } C_{dst} < 1 \text{ and } C_{src} <= 0 \end{cases}\end{split}\]
#### Color Dodge

|

Lightens the destination to reflect the color of the source, producing a result with lower contrast, saturated mid-tones, and blown highlights. Black source color produces no change.

This mode is the opposite of the Color Burn mode.  |    |    |       \[\begin{split}&C_{out} = \begin{cases} 0 & \text{if } C_{dst} <= 0\\ min(1, \frac{C_{dst}}{1 - C_{src}}) & \text{if } C_{dst} > 0 \text{ and } C_{src} < 1\\ 1 & \text{if } C_{dst} < 0 \text{ and } C_{src} >= 1 \end{cases}\end{split}\]
#### Hard Light

|

Multiplies or screens the colors:

- A source color lighter than 50% gray lightens the destination as if screening it.
- A source color darker than 50% gray darkens the destination as if multiplying it.

Black source color produces black and white source color produces white.  |    |    |       \[\begin{split}&C_{out} = \begin{cases} 2 * C_{src} * C_{dst} & \text{if } C_{src} <= 0.5\\ 1 - 2 * (1 - C_{src}) * (1 - C_{dst}) & \text{otherwise} \end{cases}\end{split}\]
#### Soft Light

|

Darkens or lightens the colors:

- A source color lighter than 50% gray lightens the destination as if dodging it.
- A source color darker than 50% gray darkens the destination as if burning it.

The result is softer than with the Overlay mode. Black or white source color produces a distinctly darker or lighter result, but not pure black or white.  |    |    |       \[\begin{split}&C_{out} = \begin{cases} C_{dst} - ( 1 - 2 * C_{src}) * C_{dst} * (1 - C_{dst}) & \text{if } C_{src} <= 0.5\\ C_{dst} + (2 * C_{src} - 1) * C_{dst} * ((16 * C_{dst} - 12) * C_{dst} + 3) & \text{if } C_{src} > 0.5 \text{ and } C_{dst} <= 0.25\\ C_{dst} + (2 * C_{src} - 1) * (\sqrt{C_{dst}} - C_{dst}) & \text{if } C_{src} > 0.5 \text{ and } C_{dst} > 0.25 \end{cases}\end{split}\]
#### Difference

|

Subtracts either the source color from the destination color or the other way around, depending on which one is brighter. White source color inverts the destination color. Black source color produces no change.   \[C_{out} = abs(C_{dst} - C_{src})\]   |    |    |
#### Exclusion

|

Creates an effect that is similar to Difference but lower in contrast. White source color inverts the destination color. Black source color produces no change.   \[C_{out} = C_{src} + C_{dst} - 2 * C_{src} * C_{dst}\]   |    |    |
#### HSL Hue

|

Uses:

- Hue of the source
- Luminosity and saturation of the destination
  |    |    |
#### HSL Saturation

|

Uses:

- Saturation of the source
- Hue and luminosity of the destination
  |    |    |
#### HSL Color

|

Uses:

- Hue and saturation of the source
- Luminosity of the destination
  |    |    |
#### HSL Luminosity

|

Uses:

- Luminosity of the source
- Hue and saturation of the destination
  |    |    |
