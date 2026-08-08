---
title: Using brushes
source: https://docs.kanzi.com/4.1.0/en/working-with/brushes/using-brushes.html
---

# Using brushes

Brushes are graphics objects that describe how 2D content is drawn.

Use Brushes to set the appearance of the foreground and background of 2D nodes. For example, with brushes you can define the color of text in a Text Block 2D node, fill a background of a 2D node with an image pattern, or apply a material effect on 2D content.

Most 2D nodes have a foreground and a background. With brushes you can change the appearance of both.

These brushes are available in Kanzi:

- Color Brush to fill a 2D node with a solid color.

See Filling 2D nodes with a solid color.
- Texture Brush to fill a 2D node with a texture.

See Filling 2D nodes with a texture.
- Material Brush to fill a 2D node with a material.

See Filling 2D nodes with a material.

Kanzi Studio stores brushes in the Library > Materials and Textures > Brushes.

For example, with the brushes you can:

- Set the color of 2D text. See Setting the color of text in 2D text nodes.
- Define the appearance of brushes in different application states. See Controlling the appearance of brushes.
- Create post-processing effects for 2D nodes. See Applying custom rendering to 2D nodes.

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
**Tip:** To quickly edit a brush, in the Properties next to the Background Brush or Foreground Brush property click  and edit the brush.

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

## Setting the color of text in 2D text nodes

To set the color of text in a Text Block 2D or Text Box 2D node:

1.

In the Node Tree create or select a Text Block 2D or Text Box 2D node.
2.

In the Properties add the Foreground Brush property.
3.

Set the Foreground Brush property to an existing Color Brush or select + Color Brush, name the brush, click  next to the property, and set the color of the Color Brush you created.
**Tip:** To quickly edit a brush, in the Properties next to the Background Brush or Foreground Brush property click  and edit the brush.

## Controlling the appearance of brushes

You can define the appearance of brushes in different application states. For example, when you use a brush to fill a Button 2D node, you can change the appearance of the brush when the user presses the button.

To control the appearance of a brush, create a state manager which sets the properties of the brush in the node which uses the brush.

To control the appearance of a brush:

1.

Create a brush and use it to fill a 2D node.

For example, create a texture brush and set the Background Brush property of a Button 2D node to the texture brush that you created. See Filling 2D nodes with a texture.
2.

Create a state manager which you use to control the appearance of the brush that you created in the first step.

For example:

  1.

Create for the Button 2D node a state manager that has two states named Released and Pressed and set the state manager to use the Button > Is Down controller property. See Using a state manager to set button states.
  2.

Set the appearance of the brush in the Released and Pressed states.

For example, in the Properties next to the Background Brush property click , set the Brush Modulate Color property, and in the State Tools click  in the Pressed state to save the property value to the Pressed state.

Now when you interact with the node in the Preview, Kanzi changes the appearance of the brush that you created.
## Applying custom rendering to 2D nodes

Apply custom rendering to 2D nodes to create post-processing effects.

For example, you can convert color images in a 2D node to grayscale.

To apply custom rendering to a 2D node, use the Composition Brush property to compose the node on the screen with a Material Brush, and enable the Force Composition property.

To apply custom rendering to a 2D node:

1.

Create a material with which you want to apply custom rendering.

For example, to create a material that converts color to grayscale:

  1.

In the Library, press Alt and right-click Materials and Textures and select Material Type. Kanzi Studio creates a material type and a material that uses the material type.
  2.

In the Library > Materials and Textures > Material Types, expand the material type that you created. Double-click the Vertex Shader to open it in the Shader Source Editor, replace the existing shader code with this code, and save the shader.

```
#version 310 es

in vec3 kzPosition;
in vec2 kzTextureCoordinate0;
uniform highp mat4 kzProjectionCameraWorldMatrix;

out mediump vec2 vTexCoord;

void main()
{
    precision mediump float;
    vTexCoord = kzTextureCoordinate0;
    gl_Position = kzProjectionCameraWorldMatrix * vec4(kzPosition.xyz, 1.0);
}

```

  3.

Open the Fragment Shader, replace the existing shader code with the code in this step, and save the shader.

In the shader, use these Kanzi default uniforms:

    - `ContentTexture` to define the texture that the rendered node provides when rendering
    - `RenderOpacity` to define the opacity of the rendered node

See Shader uniforms.

```
#version 310 es

uniform sampler2D ContentTexture;
in mediump vec2 vTexCoord;
uniform lowp float RenderOpacity;
layout(location = 0) out vec4 fragColor;

void main()
{
    precision mediump float;
    // Use this algorithm to convert the colors in the texture used by
    // the 2D node to grayscale.
    // To integrate to the Kanzi rendering pipeline, the shader must output
    // premultiplied alpha.
    vec4 color = texture(ContentTexture, vTexCoord);
    float grayscale = dot(color.rgb, vec3(0.21, 0.72, 0.07));
    float alpha = color.a * RenderOpacity;
    vec3 premultipliedColor = vec3(grayscale) * alpha;
    fragColor = vec4(premultipliedColor, alpha);
}

```

2.

In the Library, press Alt and right-click Materials and Textures and select Material Brush. In the Properties, set the Material property to the material that you created in the previous step.
3.

In the Node Tree, create or select a 2D node to which you want to apply the material that you created. For example, create a Stack Layout 2D node. In the Stack Layout 2D node, create an Image node.
4.

In the Properties, add and set:

  - Brush Composition Brush to the material brush that uses the material you want to apply to that node
  - Node 2D > Force Composition to enabled
  - (Optional) Render Target > Multisample Level to the number of anti-aliasing samples that you want to apply to the content
  - (Optional) Node > Opacity to control the translucency of the node

## Using brushes in the API

For details, see the `Brush` class.
## Brush property types

For a list of the available property types for brushes, see Brush.
