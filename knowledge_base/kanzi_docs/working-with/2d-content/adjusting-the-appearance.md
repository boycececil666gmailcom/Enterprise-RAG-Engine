---
title: Adjusting the appearance of 2D nodes
source: https://docs.kanzi.com/4.1.0/en/working-with/2d-content/adjusting-the-appearance.html
---

# Adjusting the appearance of 2D nodes


You can adjust the appearance of 2D nodes by filling their background or foreground with a brush. For example, you can set the background color of an Activity node, fill a Text Block 2D node with a texture, or apply a material to a Button 2D node.

You can fill 2D nodes with:

- Solid color. See Filling 2D nodes with a solid color.
- Texture. See Filling 2D nodes with a texture.
- Material. See Filling 2D nodes with a material.

## Filling 2D nodes with a solid color


Use a Color Brush to fill a 2D node with a solid color.

To fill a 2D node with a solid color:

1.

In the Library press Alt and right-click Materials and Textures, select Color Brush, and name the brush.
2.

In the Node Tree select the 2D node that you want to fill with the brush you created, in the Properties add the Background Brush or the Foreground Brush property, and select the brush you created in the first step.

For example, create a Button 2D node, in the Properties add the Background Brush property, and set it to the brush you created in the first step.
3.

In the Properties click  next to the property you added in the previous step and set the color of the color brush you created in the previous step.

In the Preview you can see that the Color Brush you created fills the node for which you set the property.

> **Tip:** To quickly edit a brush, in the Properties next to the Background Brush or Foreground Brush property click  and edit the brush.
>
## Filling 2D nodes with a texture


Use a Texture Brush to fill a 2D node with a texture.

To fill a 2D node with a texture:

1.

In the Library press Alt and right-click Materials and Textures, select Texture Brush, and name the brush.
2.

In the Node Tree select the 2D node that you want to fill with the brush you created, in the Properties add the Background Brush or the Foreground Brush property, and select the brush you created in the first step.

For example, create a Grid Layout 2D node, in the Properties add the Background Brush property, and set it to the brush you created in the first step.
3.

In the Properties click  next to the property that you added in the previous step to go to the brush used by that property, set the texture you want this texture brush to use, and adjust how the Texture Brush uses that texture:

  - Brush Modulate Color sets the modulation color for the brush.
  - Brush Horizontal Tiling affects the scale of the texture coordinates to set the horizontal tiling of the texture.
  - Brush Vertical Tiling affects the scale of the texture coordinates to set the vertical tiling of the texture.
  - Brush Texture sets the texture for the brush.


## Filling 2D nodes with a material


Use a Material Brush to fill a 2D node with a material.

To fill a 2D node with a material:

1.

In the Library press Alt and right-click Materials and Textures, select Material Brush, and name the brush.
2.

In the Properties set the Material property to the material you want to use to fill a 2D node.

If you do not have any materials in your project, create a material. See Creating a material.
3.

In the Node Tree select the 2D node that you want to fill with the brush you created, in the Properties add the Background Brush or the Foreground Brush property, and select the brush you created in the first step.

For example, create a Button 2D node, in the Properties add the Background Brush property, and set it to the brush you created in the first step.
4.

To adjust the appearance of the material, set the Material properties either in:

  - The Material Brush.

For example, to change the ambient color, texture, and blending of the material for the Material Brush, add and set the Ambient Color, Texture, and Blend Mode properties.
  - The node which uses the Material Brush.

For example, to change the ambient color, texture, and blending of the material for a node, add and set the Ambient Color, Texture, and Blend Mode properties in that node.


## Rendering pixel-perfect 2D nodes


Pixel-perfect rendering ensures sharp rendering of a 2D node by rounding the translation and scale of the node to a full pixel.

Kanzi does not by default render 2D nodes as pixel-perfect. When you position a 2D node at a fractional pixel location, anti-aliasing can cause that node to have blurry edges.

> **Tip:** A Kanzi Studio project by default has a style that makes Kanzi render the text in all Text Block 2D nodes as pixel-perfect. See Rendering pixel-perfect text in a Text Block 2D node.
>
> To render a pixel-perfect 2D node, in the Node Tree or Prefabs, select that node and in the Properties, add and enable the Node 2D > Snap to Pixel property.
