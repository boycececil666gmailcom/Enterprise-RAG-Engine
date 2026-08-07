---
title: Filters
source: https://docs.kanzi.com/4.1.0/en/working-with/filters/filters.html
---

# Filters

Filters collect and reorganize 3D nodes in your Kanzi project. You can use filters to determine which 3D nodes to render in different render passes.

After you set one or more filters or object sources, a filter collects and outputs a set of 3D nodes that match the requirements you define in that filter.

Use filters to adjust the rendering for the whole or parts of your Kanzi application. To use a filter, either:

- In a Draw Objects render pass or Draw Objects With Material render pass set the Object Source property so that the render pass renders only those nodes that the filter passes to the render pass.
- In a Node List render pass set the Filter property so that the Node List render pass holds only those nodes that the filter passes to that Node List render pass.

Use a Node List render pass when you want to filter anything but the 3D nodes that you want to render, such as Light nodes. Draw Objects render pass, Draw Objects With Material render pass, and Gather Lights render passes can use the result node list of the same Node List render pass.

See Rendering.

For example, you can use filters to:

- Create reflections for nodes. See Tutorial: Create reflections.
- Apply a stencil to 3D content. See Tutorial: Apply a stencil to 3D content.
- Distribute rendering across several frames. See Tutorial: Progressive rendering.
- Render only transparent nodes. See Rendering partially transparent nodes.

These filters are available in Kanzi Studio in the Library > Rendering > Object Sources:

- Contains Property Filter collects 3D nodes that contain, or do not contain a specific property.

See Using the Contains Property Filter.
- Object Type Filter collects 3D nodes based on their type. See Using the Object Type Filter.
- Property Is Equal Filter collects 3D nodes that contain, or do not contain a specific property the value of which matches a specific value.

See Using the Property Is Equal Filter.
- Sorting Filter either orders 3D nodes by their position on the z axis or groups them by their material type.

See Using the Sorting Filter.
- Tag Filter collects 3D nodes that have a specific tag assigned.

See Using the Tag Filter.

## Using filters in the API

For details, see the `FilterObjectSource` class.
