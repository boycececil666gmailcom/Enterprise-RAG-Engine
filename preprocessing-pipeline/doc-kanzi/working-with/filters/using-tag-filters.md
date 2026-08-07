---
title: Using the Tag Filter
source: https://docs.kanzi.com/4.1.0/en/working-with/filters/using-tag-filters.html
---

# Using the Tag Filter

Tag Filter collects 3D nodes that have a specific tag assigned.

For example, with tag filters you can:

- Create reflections of nodes. See Tutorial: Create reflections.
- Apply a stencil to 3D content. See Tutorial: Apply a stencil to 3D content.
- Distribute rendering across several frames. See Tutorial: Progressive rendering.

To use the Tag Filter:

1.

In the Library press Alt and right-click Rendering > Object Sources and select Tag Filter.
2.

In the Properties set:

  - Source to the source from where you want to collect nodes for filtering. For example, to apply your filter to all nodes in your project, select Root Object Source. You can select the output of another filter as the source from where you collect nodes for filtering.
  - Included Tags to tags of the nodes you want to include in the filter results. If you include more than one tag, the filter returns nodes that contain at least one of the listed tags. See Using tags.
  - Excluded Tags to tags of the nodes you do not want to include in the filter results. If a node contains only one of the tags listed in the Excluded Tags, the filter does not return that node. This is so even when the same node contains tags you added to the Included Tags.
**Note:** Kanzi filters lights in the same way it filters other nodes. When you create a filter that only includes a specific tag, the lights that light the tagged nodes are included in the filter only when you add the tag to those light nodes. It is often more convenient to either:
- Exclude the nodes you do not want to render.
- Tag all light nodes with a separate tag and include that tag in all your filters.
3.
To take the Tag Filter into use, either:
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

## Using Tag Filter filters in the API

For details, see the `TagFilter` class.
