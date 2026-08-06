---
title: Using the Sorting Filter
source: https://docs.kanzi.com/4.1.0/en/working-with/filters/using-sorting-filters.html
---

# Using the Sorting Filter


Sorting Filter either orders 3D nodes by their position on the z axis or groups them by their material type.

For example, use sorting filters to optimize the performance of your Kanzi application:

- **Preventing overdraw.**

Excessive overdraw can decrease performance on the GPU in the form of increased fill-rate. See Preventing overdraw with the Sorting Filter.
- **Rendering transparent objects.**

Because visualization of transparent nodes relies on having proper data behind them, in order to solve the blending equations properly, to correctly render transparent nodes, you must render them from back to front. See Rendering partially transparent nodes.
- **Reducing shader switches.**

If nodes are presented in an order that requires excessive switching between shader programs, the rendering can slow down. See Reducing shader switches.


To use the Sorting Filter:

1.

In the Library press Alt and right-click Rendering > Object Sources and select Sorting Filter.
2.

In the Properties set:

  - Source to the source from where you want to collect nodes for filtering. For example, to apply your filter to all nodes in your project, select Root Object Source. You can select the output of another filter as the source from where you collect nodes for filtering.
  - Sorting Type to either:

    - View z to arrange the nodes by their position along the z axis. By arranging nodes into front-to-back ordering before rendering you can prevent overdraw.

Overdraw issues occur when one node is first drawn to an area of pixels in the back buffer, after which another node is presented that occludes the first node, and the same pixels are filled again. Excessive overdraw can decrease performance on the GPU in the form of increased fill-rate. If you order nodes so that the occluding node is drawn first, the occluded pixels do not have to be rendered again because of the depth buffering.

See Preventing overdraw with the Sorting Filter.
    - Material type to group the nodes by their material type.

By grouping nodes by their material type you can optimize your Kanzi application, because that way Kanzi can decrease the number of shader switches. See Reducing shader switches.

  - Either enable or disable the Reverse Order property:

    - When enabled it reverses the current order of nodes.
    - When disabled it keeps the current order of nodes.


3.

To take the Sorting Filter into use, either:

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


## Using Sorting Filter filters in the API


For details, see the `SortObjectSource` class.
