---
title: Using object sources
source: https://docs.kanzi.com/4.1.0/en/working-with/object-sources/using-object-sources.html
---

# Using object sources

Use object sources and filters to tell a Draw Objects render pass which nodes in your Kanzi application you want to render. Root Object Source contains all nodes in the node tree of the currently active Scene node.

When you create a new Draw Objects render pass, Kanzi Studio by default renders all nodes in the Scene or Viewport 2D node which uses the render pass.

Use Root Object Source with filters and Combine Object Source to render only specific nodes in your project and achieve the desired rendering effect. See Filters and Rendering.

Root Object Source does not have configurable properties.
## Creating a Combine Object Source

Combine object source collects and combines nodes from one or more input sources.

To create a Combine Object Source:

1.

Create at least two filters. See Filters.
2.

In the Library press Alt and right-click Rendering > Object Sources and select Combine Object Source.
3.

In the Properties set the Input property to the filters or other combine object sources that collect nodes in the node tree.

## Using a Combine Object Source

To use a Combine Object Source:

1.

In the Library > Rendering > Render Pass Prefabs select or create the Draw Objects render pass which you want to use to achieve a desired rendering result. See Rendering.
2.

In the Properties set the Object Source property to either a filter or Combine Object Source.

The Draw Objects render pass now renders only the nodes collected by the selected filter or object source.

## Using Combine Object Source in the API

For details, see the `CombinerObjectSource` class.
