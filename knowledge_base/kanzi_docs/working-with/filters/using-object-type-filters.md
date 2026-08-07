---
title: Using the Object Type Filter
source: https://docs.kanzi.com/4.1.0/en/working-with/filters/using-object-type-filters.html
---

# Using the Object Type Filter


Use Object Type Filter to collect 3D nodes based on their type.

For example, use the Object Type Filter to collect Light nodes in your project.

To use the Object Type Filter:

In the Library press Alt and right-click Rendering > Object Sources and select Object Type Filter.

1.
2.

In the Properties set:

  - Source to the source from where you want to collect nodes for filtering. For example, to apply your filter to all nodes in your project, select Root Object Source. You can select the output of another filter as the source from where you collect nodes for filtering.
  - Type to the type of node you want the filter to collect.

For example:

    - To collect all Light nodes, select Light.

Kanzi filters lights in the same way it filters other nodes. When you create a filter that picks specific nodes, the lights that light those nodes are not included in the filter.
    - To collect all nodes that can be rendered, select All renderables.

By default this value includes the Box, Model, Plane, Sphere, and Text Block 3D node.

You can set the rendering of nodes in the Kanzi Engine API by calling

```
kzuObjectNodeSetIsRenderable(objectNode, KZ_TRUE);

```


  - Operation to either:

    - Include to collect the nodes of the type that you set in the Type property.
    - Exclude to leave out the nodes of the type that you set in the Type property.


3.

To take the Object Type Filter into use, either:

  - In the Draw Objects render pass or Draw Objects With Material render pass that you use to render the 3D nodes to which you want to apply the filter, set the Object Source property to the filter or to an object source that collects the filter.
  - In the Node List render pass that you use to hold the nodes that you want to render using other render passes, set the Filter property to the filter or to an object source that collects the filter.

Use a Node List render pass when you want to filter anything but the 3D nodes that you want to render, such as Light nodes. Draw Objects render pass, Draw Objects With Material render pass, and Gather Lights render passes can use the result node list of the same Node List render pass.


For example:

  1.

In the Library > Rendering > Render Pass Prefabs create a Group render pass and inside it create:

    - Clear render pass
    - Gather Lights render pass and inside it a Draw Objects render pass

  2.

In the Library select the Draw Objects render pass that you created and in the Properties set the Object Source property to the filter that you created or to an object source which collects the filter.

See Using object sources.
  3.

In the Node Tree select the Viewport 2D node to which you want to apply the filter and in the Properties set the Render Pass Prefab property to the Group render pass whose descendant Draw Objects render pass uses as its object source the filter that you created.

Kanzi Studio renders the nodes collected by the filter.


## Using Object Type Filter filters in the API


For details, see the `ObjectTypeFilter` class.
