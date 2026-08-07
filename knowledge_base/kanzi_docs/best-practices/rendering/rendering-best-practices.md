---
title: Rendering best practices
source: https://docs.kanzi.com/4.1.0/en/best-practices/rendering/rendering-best-practices.html
---

# Rendering best practices

By optimizing the rendering performance you can significantly improve the performance of your application.

Kanzi renders nodes as follows:

- Nodes that are outside of the screen are rendered and transformed.
- 3D nodes with the Blend Intensity property set to 0 are rendered.
- 3D nodes with the Visible property disabled are not rendered or transformed.
- 2D nodes with the Opacity property set to 0 are not rendered and their child nodes are not rendered, but are transformed.
- 2D nodes with the Visible property disabled are not rendered and their child nodes are not rendered, but are transformed.

## Optimizing rendering performance of your applications

To optimize rendering performance of your applications consider:

- Shaders that contain a lot of fragment-based calculations can be the heaviest part of rendering. See Optimizing fragment shaders.
- Recalculation of layout caused by changes in the scene can hinder the performance of the CPU. See Optimizing the rendering of layouts.
- When a property type has Affect Layout enabled and the value of such property changes on a node, Kanzi recalculates the layout for that node. Make sure you recalculate the layout only when needed. For example, recalculating the layout every frame decreases application performance. Affect Layout is enabled in properties that come with Kanzi only if they affect the layout. For custom property types you can set whether they affect layout. See Creating property types.
- Distribute the rendering workload across several frames to reduce the amount of work and time required to render one whole frame. See Distributing rendering across several frames.
- Excessive overdraw can decrease performance on the GPU in the form of increased fill-rate. See Preventing overdraw with the Sorting Filter.
- When rendering opaque content, always render from front to back. Render from back to front only when you have a good reason to do so.
- Because visualization of transparent nodes relies on having proper data behind them, in order to solve the blending equations properly, to correctly render transparent nodes, you must render them from back to front. See Rendering partially transparent nodes.
- If nodes are presented in an order that requires excessive switching between shader programs, the rendering can slow down. See Reducing shader switches.
- Set the render pass of the first Viewport node for each render target to clear all buffers.
- Make sure that all render targets are not cleared more than once.
- Do not clear color, depth, or stencil for any render target more than once.
- Remove overlapping background brushes. For example, if the RootNode node has a background brush set and its child nodes also have a background brush set, remove the background brush from the RootNode node.
- Render animated items in lower quality while they are moving. Improves the performance, but decreases the quality.
- To dynamically change the size of text in a Text Block node, use the Scale property field of either Render Transformation or Layout Transformation properties, instead of the Font Size property. For example, use this approach when you want to animate the size of text in a Text Block node. When you use the Font Size property to dynamically scale the text, Kanzi creates multiple textures for different font sizes and does not release them from the memory.
- Avoid unnecessary fill. For example, avoid:

  - Filling the Screen with a 3D plane. For example, if you use a 3D plane to draw a circular object using just a texture with alpha 0 in the corners, it is in most cases faster to render it if you cut the mesh around the form because of the fill-rate hit.
  - Rendering 3D with alpha set to 0. This causes fill, but has no visual effect.

- Instead of rendering effects in real-time, bake the effects into textures. For example, create textures to simulate shadows and depth of field. Improves the performance, but also increases the memory consumption.

## Viewing nodes that are rendered into texture

Switching between framebuffer objects can cause significant performance reduction on some platforms. Conditions when Kanzi renders a node into a texture can be complex. For example, rotation, scale, or opacity can cause render to texture to occur.

To see whether a node is rendered into a texture, and causing a framebuffer object switch, in the Preview click  to enter the Analyze mode, right-click , and select Framebuffer objects. The Preview highlights the layers that are rendered into texture with transparent, orange stripes.
