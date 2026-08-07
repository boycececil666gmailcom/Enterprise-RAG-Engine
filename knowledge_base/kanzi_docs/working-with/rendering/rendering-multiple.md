---
title: Rendering multiple render passes or textures
source: https://docs.kanzi.com/4.1.0/en/working-with/rendering/rendering-multiple.html
---

# Rendering multiple render passes or textures

You can use a Blit render pass to blit multiple Composition Target render passes or textures to the screen using a specific material. By default, a Blit render pass blits only one texture, which can be a texture resource or the result texture of a Composition Target render pass.

For example, you can blit the result textures of multiple Composition Target render passes to the screen using a specific material to create post-processing effects, such as bloom. See Tutorial: Create a bloom effect.

To learn how to use a Composition Target render pass to render to multiple composition targets and blit the result textures to the screen, see Rendering content to multiple composition targets.

To render multiple render passes or textures:

1.

In the Library > Materials and Textures > Material Types, duplicate the DefaultBlit material type. Rename the material type to BlitMultiple and the material to BlitMultipleMaterial.
**Tip:** If your project does not contain the DefaultBlit material type, in the Library > Materials and Textures press Alt and right-click Material Types, and select DefaultBlit.
2.
In the BlitMultiple material type, double-click the Fragment Shader to open it in the Shader Source Editor.
3.
In the Shader Source Editor, add the uniforms that you want the Blit render pass to use, modify the shader to use them, and click Save.
For example, to make the shader mix the Texture 0 and Texture 1 properties using the custom property Weight to weigh between them, replace the contents of the shader file with
```
#version 310 es
precision mediump float;
uniform sampler2D Texture0;
uniform sampler2D Texture1;
uniform float BlendIntensity;
uniform float Weight;
in vec2 vTexCoord;
layout(location = 0) out vec4 fragColor;
void main()
{
fragColor = mix(texture(Texture0, vTexCoord), texture(Texture1, vTexCoord), Weight) * BlendIntensity;
}
```
4.
In the Library > Materials and Textures > Material Types, select the BlitMultiple material type. In the Properties, click Sync with Uniforms.
Kanzi Studio:
1.
Creates in the Library > Property Types the custom property types that you defined in the fragment shader.
For example, the Weight property type.
2.
Adds the properties, which you defined in the shader, to the BlitMultiple material type and the materials which use that material type.
For example, the Texture1 and Weight property types.
5.
In the Library > Materials and Textures > Materials, select the BlitMultipleMaterial material, which uses the BlitMultiple material type. In the Properties, set the Blend Mode property to Alpha: Premultiplied.
You set Kanzi to blend the textures that it blits on the screen using this material.
6.
In the Library, press Alt and right-click Rendering, and select Compose and Blit Pass.
Compose and Blit Pass contains the render pass structure that enables you to blit to the screen Composition Target render passes or textures using a specific material.
The Compose and Blit Pass render pass preset contains these render passes:
- Composition Target render pass renders itself and its descendant render passes to one or more composition targets.
- Clear render pass clears some or all of the buffers of the current render context.
By default, the Clear render pass in the Compose and Blit Pass clears the first color buffer with transparent black color and the depth buffer with value 1.
For example, to clear the first color buffer with a different color, set the Clear Color 0 property to the color that you want to use as the background color of the content that Kanzi renders to the Composition Target render pass.
- Gather Lights render pass collects the Light nodes in the Viewport 2D node that you set to use the Compose and Blit Pass, and passes them to its child Draw Objects render pass.
- Draw Objects render pass named Draw Objects allows you to set a Camera node to render a specific list of nodes, to filter those nodes, and to control frustum culling. Draw Objects render pass by default renders nodes using the lights provided by its nearest ancestor Gather Lights render pass. By default the Draw Objects render pass uses the default Camera node to render all nodes in a Viewport 2D node.

  - Blit render pass blits one or more single textures or cubemap textures on the screen using a specific material.

By default, this Blit render pass draws on the screen the first color texture to which the Composition Target render pass renders its content.

7.

In the Node Tree, select the Viewport 2D node whose content you want to render to a composition target. In the Properties, set the Render Pass Prefab property to the Compose and Blit Pass.

Kanzi renders the scene in that Viewport 2D to a composition target and uses the Blit render pass to draw the content on the screen.
8.

In the Library > Rendering > Render Pass Prefabs, select the Compose and Blit Pass > Blit render pass. In the Properties, add and set:

  - Blit render pass > Texture 1 to a texture or bind it to the result texture of a Composition Target render pass that you want to use

For example, add the Texture 1 property and set it to a texture resource.
  - Material to the material that you want the Blit render pass to use

For example, set it to the BlitMultipleMaterial material whose fragment shader you edited earlier in this procedure to make the material support mixing two textures.
  - Material Properties > Weight to the amount that you want to show each texture

To give more weight to Texture 0, decrease the value of the Weight property, and to give more weight to Texture 1, increase the value. For example, to show the average of the textures set by the Texture 0 and Texture 1 properties, set Weight to **0.5**.
