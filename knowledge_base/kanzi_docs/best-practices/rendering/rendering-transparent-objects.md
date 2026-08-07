---
title: Rendering partially transparent nodes
source: https://docs.kanzi.com/4.1.0/en/best-practices/rendering/rendering-transparent-objects.html
---

# Rendering partially transparent nodes

Because visualization of partially transparent nodes relies on having proper data behind them, in order to solve the blending equations properly, you have to render the partially transparent nodes from back to front.

When not rendered in a correct way, the partially transparent nodes can waste a lot of resources. If a partially transparent node is drawn before the underlying opaque node, the partially transparent node has to be drawn again after the opaque node. This means that because of the overdraw, those pixels are drawn three times. This is always the case when the nodes are presented in a front-to-back order.

For these reasons always render all the partially transparent nodes after rendering the rest of the scene.

You can define the rendering order of nodes using one or more render pass and filter. See Rendering and Filters.
## Rendering partially transparent 3D nodes in the correct order

To render partially transparent 3D nodes in the correct order, select the nodes in the Node Tree and in the Properties next to the Tags property click the Tags button and select Transparent.

Kanzi Studio DefaultRenderPassPrefab first renders the nodes that do not have the Transparent tag and then the nodes that do have the Transparent tag.
## Controlling how Kanzi renders a Viewport 2D

You can control how Kanzi renders a Viewport 2D node. Kanzi renders the background brush before the content of the Viewport 2D node by default.

To control how Kanzi renders a Viewport 2D node, set the Foreground Hint property to:

- None to render the background brush after rendering the Viewport 2D node. Use it when the content of the Viewport 2D node is opaque.
- Translucent to render the background brush before the content of the Viewport 2D node. This is the default value. Use it when the content in the Viewport 2D node is alpha-blended.
- Occluding to not render the background brush. Use it when the entire Viewport 2D node is filled with 3D content.
