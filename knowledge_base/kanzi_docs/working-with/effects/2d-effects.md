---
title: Effects for 2D nodes
source: https://docs.kanzi.com/4.1.0/en/working-with/effects/2d-effects.html
---

# Effects for 2D nodes


Use effects to apply post-processing effects to 2D nodes.

In Kanzi Studio you can find the effects in the Library > Effects.

These effects are available in Kanzi:
|

Use the Blur Effect 2D effect to apply a Gaussian blur to a 2D node.

See Using the Blur Effect 2D effect.  |    |
|

Use the Mask Effect 2D effect to apply a mask to a 2D node.

See Using the Mask Effect 2D effect.  |    |
|

Use the Outline Effect 2D effect to apply an outline to the content of a 2D node.

See Using the Outline Effect 2D effect.  |    |
|

Use the Shadow Effect 2D effect to apply a shadow to the content of a 2D node.

See Using the Shadow Effect 2D effect.  |    |
|

Use an Effect Stack 2D effect prefab to apply multiple effects to a 2D node.

See Using multiple effects.  |    |
## How Kanzi applies 2D effects


Kanzi applies 2D effects to the visual shape of the content in a node and its descendant nodes.

When you want to apply an effect to a node but not to its descendant nodes, place the descendant nodes in a sibling node of the node to which you apply the effect. Position that sibling node in the node tree below the node to which you apply the effect. Make sure that the sibling nodes are of the same size, layout, transformation, and opacity.
## Effects and layout


When you use effects, keep in mind that:

- Kanzi does not take effects into account when calculating layout. When your design does not allow an effect to exceed the layout bounds, make sure that there is enough space in the layout for that effect.

For example, in a layout that contains a Text Block 2D node where you apply a drop shadow, in that Text Block 2D node ensure sufficient space for the shadow by setting the Horizontal Margin and Vertical Margin properties.
- When Kanzi applies an effect to a 2D node, it composites that node and clips its descendant nodes to the node bounds, regardless of the value of the Clip Children property. This happens because the size of the render target texture matches the size of the node.

## Impact of effects on application performance


For every instance of an effect Kanzi requests the composition manager to provide a temporary composition target. Kanzi composition manager reuses temporary composition targets if they are compatible in size and parameters.

The final performance of an application that uses effects depends on:

- The amount of allocated memory, and therefore the bandwidth required to render the UI of the application
- The number of draw calls
- The number of render target or texture switches


To find the most efficient way of using effects, test the performance of your application with these approaches:

- Apply a separate effect to each UI element to minimize the area.
- Apply an effect to a group of UI elements that cover a larger area.

## Applying anti-aliasing


When you apply an effect to a 2D node, Kanzi renders that node to a composition target. By default, Kanzi does not apply anti-aliasing to the child nodes of a composited node. For example, when you rotate these nodes, their edges can look jaggy.

To apply multisample anti-aliasing:

1.

In the Node Tree or Prefabs, select the node to which you apply the effect.
2.

In the Properties, add the Render Target > Multisample Level property and set it to the number of anti-aliasing samples that you want to use.

See the documentation of the device on which you want to run your Kanzi application for supported values, because the number of anti-aliasing samples depends on the device. If you set the Multisample Level property to a value that your device does not support, Kanzi Engine clamps the value to the largest value supported by the device driver.
