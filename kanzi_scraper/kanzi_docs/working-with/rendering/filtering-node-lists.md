---
title: Collecting nodes for rendering
source: https://docs.kanzi.com/4.1.0/en/working-with/rendering/filtering-node-lists.html
---

# Collecting nodes for rendering


Use the Node List render pass to filter and hold a list of 3D nodes that you want to render using other render passes.

The Draw Objects render pass and Draw Objects With Material render passes draw 3D content in a scene.

By default the Draw Objects render pass and Draw Objects With Material render pass draw all the 3D content in a scene or the nodes provided by their nearest ancestor Node List render pass.

For example, in this render pass prefab the Draw Objects render pass by default draws the nodes provided by the Node List render pass:

You can use any Node List render pass in the same Render Pass Prefab to provide nodes to a Draw Objects render pass and Draw Objects With Material render pass for rendering. To learn how to use filters to pass nodes to render passes, see Filters.

To set the Node List render pass that you want to use to collect 3D nodes for rendering:

1.

In the Library > Rendering > Render Pass Prefabs select the Draw Objects render pass or Draw Objects With Material render pass that you want to use to draw 3D nodes.
2.

In the Properties click + Add Binding, and in the Binding Editor set:

  - Property to Node List
  - Expression to point to the Output Node List property of the Node List render pass whose output nodes you want to render

For example, to draw the nodes provided by a sibling Node List render pass of the Draw Objects render pass, set the Expression to:

```
{@../Node List/NodeListRenderPass.OutputNodeList}

```
