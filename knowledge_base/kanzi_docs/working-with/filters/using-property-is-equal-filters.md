---
title: Using the Property Is Equal Filter
source: https://docs.kanzi.com/4.1.0/en/working-with/filters/using-property-is-equal-filters.html
---

# Using the Property Is Equal Filter


Property Is Equal Filter collects 3D nodes that contain, or do not contain a specific property the value of which matches a specific value.

To use the Property Is Equal Filter:

1.

In the Library press Alt and right-click Rendering > Object Sources and select Property Is Equal Filter.
2.

In the Properties set:

  - Source to the source from where you want to collect nodes for filtering. For example, to apply your filter to all nodes in your project, select Root Object Source. You can select the output of another filter as the source from where you collect nodes for filtering.
  - Property Type to the property for which you want to filter your nodes.
  - Operation to either:

    - Include to collect the nodes that contain the property you set in the Property Type property.
    - Exclude to leave out the nodes that contain the property you set in the Property Type property.

  - Depending on the property you selected in the Property Type, set the value of the property you want the Property Is Equal Filter to collect.

3.

To take the Property Is Equal Filter into use, either:

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


## Using Property Is Equal Filter filters in the API


For details, see the `PropertyIsEqualFilter` class.
