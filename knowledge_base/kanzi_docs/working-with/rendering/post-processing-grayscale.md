---
title: Creating a post-processing effect
source: https://docs.kanzi.com/4.1.0/en/working-with/rendering/post-processing-grayscale.html
---

# Creating a post-processing effect


Use materials and render passes to create post-processing effects for 3D content. In post-processing, you use a specific material to apply an effect on the content in a framebuffer that you draw to the screen using a render pass.

This topic shows how you can create a simple post-processing effect where you can adjust the level of color saturation. You can learn how to create a more complex post-processing effect by completing a tutorial. See Tutorial: Create a bloom effect.

> **Tip:** Kanzi Studio comes with several physically based rendering material types, which include a built-in tone mapping shader. See Shaders and Using material types.
>
> Tip
>
> The `<KanziInstallation>/Studio/Asset Library/MaterialTypes` project contains several material types that you can use to create post-processing effects. For example, use the `MaterialTypes/Postprocess/DirectionalGaussianBlur` material type to create a simple blur effect. See Using material types.
>
> To create a post-processing effect:
>
> 1.
>
> Define a post-processing material.
>
> For example, modify the DefaultBlit material to include the adjusting of the level of color saturation:
>
> 1.
>
> In the Library > Materials and Textures > Material Types, duplicate the DefaultBlit material type. Rename the material type to PostProcessingBlit and the material to PostProcessingBlitMaterial.
>
> Tip
>
> If your project does not contain the DefaultBlit material type, in the Library > Materials and Textures press Alt and right-click Material Types, and select DefaultBlit.
> 2.
>
> In the Library > Materials and Textures > Material Types > PostProcessingBlit, double-click the Fragment Shader to open it in the Shader Source Editor. Replace the contents of the shader file with
>
> ```
> #version 310 es
>
> precision mediump float;
>
> uniform sampler2D Texture0;
> uniform float BlendIntensity;
>
> // Defines the amount of color saturation.
> uniform float Saturation;
>
> in vec2 vTexCoord;
> layout(location = 0) out vec4 fragColor;
>
> // Converts an RGB color value to grayscale.
> float colorToLuma(vec3 col)
> {
> return col.r * 0.2126 + col.g * 0.7152 + col.b * 0.0722;
> }
>
> void main()
> {
> vec4 color = texture(Texture0, vTexCoord);
>
> vec3 grayscale = vec3(colorToLuma(color.rgb));
>
> // Interpolate between the color and grayscale values using the Saturation
> // property to weight between them.
> fragColor = vec4(mix(grayscale, color.rgb, Saturation), color.a) * BlendIntensity;
> }
>
> ```


Click Save.
  3.

In the Library > Materials and Textures > Material Types, select the PostProcessingBlit material type. In the Properties, click Sync with Uniforms.

Kanzi Studio:

    1.

Creates in the Library > Property Types the Saturation property type that you defined in the fragment shader.
    2.

Adds the Saturation property to this material type and the PostProcessingBlitMaterial material.

You use this property type to control the level of color saturation in the effect.


2.

Use render passes to apply the post-processing effect.

For example, to apply a post-processing effect that sets the level of color saturation of 3D content:

  1.

In the Library, press Alt and right-click Rendering, create a Compose and Blit Pass render pass preset, and name it Post-process Color Saturation.

Compose and Blit Pass contains the render pass structure that enables you to blit to the screen Composition Target render passes or textures using a specific material.

See Rendering content to composition targets.

In the Library > Rendering > Render Pass Prefabs each top-level render pass is the root of a render pass prefab.

In a render pass prefab, you can create a hierarchy of render passes to achieve a specific rendering result.
  2.

In the Node Tree, select the Viewport 2D node that contains the 3D content to which you want to apply the post-processing effect. In the Properties, set the Render Pass Prefab property to the Post-process Color Saturation render pass prefab.

Kanzi now renders the Viewport 2D node using the Post-process Color Saturation render pass prefab.
  3.

To use a post-processing effect, set a Blit render pass to render your content using a material that supports that post-processing effect.

For example, in the Library, select the Post-process Color Saturation > Blit render pass, and in the Properties, set the Material property to the PostProcessingBlitMaterial material.
  4.

To control a post-processing effect, add and set the properties that you created for the material that supports that post-processing effect.

For example, to control the level of color saturation, in the Library, select the Blit render pass, and in the Properties, add the Saturation property and set it to the desired value.
