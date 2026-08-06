---
title: Using hardware composition
source: https://docs.kanzi.com/4.1.0/en/working-with/materials/using-hardware-composition.html
---

# Using hardware composition


Hardware composition provides a high-performance way to composite multiple windows using the layers of the display controller. Composite multiple windows if your Kanzi application consists of multiple applications layered on top of each other, such as a cluster with an overlay. When you use hardware composition you can develop and run each of these applications separately.

Hardware composition creates a composition target that you can use like a texture. To get correct results, the hardware composition must use premultiplied alpha. See Alpha premultiplication.

When the Screen Clear Color property of the Screen node is set, Kanzi writes the color value directly to the screen output. This means that the Screen Clear Color RGB values must be premultiplied with the alpha value.

If the hardware composition does not use premultiplied alpha, you must convert to non-premultiplied alpha the RGBA values that Kanzi outputs. To convert the RGBA values to non-premultiplied alpha:

1.

Set Kanzi to draw the expected output to a texture.
2.

Draw that texture to the screen with the Blend Mode property set to Opaque and using a fragment shader that outputs RGBA values in which you divide the RGB values by the Alpha value.


For example:

1.

In the Library > Materials and Textures > Material Types duplicate the DefaultBlit material type, and rename the new material type and the material which uses that material type.

> **Tip:** If your project does not contain the DefaultBlit material type, in the Library > Materials and Textures press Alt and right-click Material Types, and select DefaultBlit.
> 2.
>
> In the Library > Materials and Textures > Material Types double-click the Fragment Shader of the new material type to open it in the Shader Source Editor, and replace the content of the fragment shader file with:
>
> ```
> #version 310 es
>
> precision lowp float;
>
> uniform sampler2D ContentTexture;
> in mediump vec2 vTexCoord;
> layout(location = 0) out vec4 fragColor;
>
> void main()
> {
> vec4 color = texture(ContentTexture, vTexCoord);
>
> if(color.a > 0.0)
> {
> color.rgb /= color.a;
> }
>
> fragColor = color;
> }
>
> ```
>
> 3.
>
> In the Library > Materials and Textures > Material Types select the material type whose fragment shader you edited, in the Properties click Sync with Uniforms, and in the Delete Property Type dialog click Yes to delete the bindings and property types that the material type no longer uses.
> 4.
>
> In the Library > Materials and Textures > Brushes create a Material Brush and in the Properties set the Material property to the material which uses the material type that you created.
> 5.
>
> In the Properties next to the Material property click  to go to the material that the Material Brush uses, and make sure that the Blend Mode property of the material is set to Opaque.
> 6.
>
> In the Node Tree select the RootNode node and in the Properties add and set:
>
> - Composition Brush to the material brush that you created
> - Force Composition to enabled
