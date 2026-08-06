---
title: Using lights in rendering
source: https://docs.kanzi.com/4.1.0/en/working-with/rendering/lights-rendering.html
---

# Using lights in rendering


Use the Gather Lights render pass to collect from a list of nodes the light nodes for lighting 3D nodes in a scene.
## Collecting lights


The Gather Lights render pass collects light nodes for lighting 3D nodes in a scene.

By default a Gather Lights render pass collects either all the light nodes in a scene or the light nodes provided by its nearest ancestor Node List render pass.

For example, in this render pass prefab the Gather Lights render pass collects the light nodes provided by its parent Node List render pass:

You can use any Node List render pass in the same Render Pass Prefab to provide light nodes to a Gather Lights render pass. To learn how to use filters to pass nodes to render passes, see Filters.

To set the Node List render pass that you want to use to collect lights:

1.

In the Library > Rendering > Render Pass Prefabs select the Gather Lights render pass that you want to use to collect light nodes.
2.

In the Properties click + Add Binding, and in the Binding Editor set:

  - Property to Node List
  - Expression to the Output Node List property of the Node List render pass

For example, to collect the light nodes provided by a sibling Node List render pass of the Gather Lights render pass, set the Expression to:

```
{@../Node List/NodeListRenderPass.OutputNodeList}

```


Click Save.
3.

Render 3D content using the light nodes that you collected. See Lighting 3D nodes.

## Lighting 3D nodes


Use the Draw Objects render pass and Draw Objects With Material render passes to draw 3D nodes. Kanzi by default lights the 3D nodes drawn by a Draw Objects render pass or Draw Objects With Material render pass using the light nodes provided by the nearest ancestor Gather Lights render pass.

For example, in this render pass prefab Kanzi lights the 3D nodes, which the Draw Objects render pass draws, using the light nodes collected by the parent Gather Lights render pass:

The Gather Lights render pass has output properties that each contain the set of lights of specific type collected by that Gather Lights render pass. You can manually set a Draw Objects render pass or Draw Objects With Material render pass to use the lights provided by any Gather Lights render pass in the same render pass prefab.

To set the Gather Lights render pass whose output lights you want to use to light 3D nodes:

1.

In the Library > Rendering > Render Pass Prefabs select the Draw Objects render pass or Draw Objects With Material render pass that you use to draw 3D content.
2.

In the Properties click + Add Binding, and in the Binding Editor set:

  - Property to the type of lights that you want to use:

    - Directional Lights for Directional Light nodes
    - Point Lights for Point Light nodes
    - Spot Lights for Spot Light nodes

  - Expression to the output lights property of the Gather Lights render pass that you want to use:

    - Output Directional Lights for Directional Light nodes
    - Output Point Lights for Point Light nodes
    - Output Spot Lights for Spot Light nodes


For example, to use the Directional Light nodes of the sibling Gather Lights render pass of the render pass to which you add the binding, set:

  - Property to Directional Lights
  - Expression to

```
{@../Gather Lights/GatherLightsRenderPass.OutputDirectionalLights}

```


Click Save.

3.

Repeat the previous step to add bindings for the other types of light nodes that you want to use.
4.

Take the render passes into use:

  1.

In the Node Tree select the Viewport 2D node that contains the 3D content that you want to render.
  2.

In the Properties set the Render Pass Prefab property to the render pass prefab that contains the Gather Lights render pass that you use to collect the light nodes and the Draw Objects render pass or Draw Objects With Material render pass that draws the 3D content.
