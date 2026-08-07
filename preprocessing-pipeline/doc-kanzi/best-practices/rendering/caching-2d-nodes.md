---
title: Caching 2D nodes
source: https://docs.kanzi.com/4.1.0/en/best-practices/rendering/caching-2d-nodes.html
---

# Caching 2D nodes

To improve the performance of your application, you can cache the rendering of 2D nodes that become static after a certain point or change only seldom. Use this method to speed up the rendering of complex nodes.

When you enable caching for a 2D node, that node generates a cache image for itself, renders itself to it, and for future frames uses this generated cache image instead of rendering itself again.

You can:

- Set Kanzi to update the render cache automatically when needed. See Using automatic render cache updates.
- Control the render cache updates manually. See Controlling render cache updates manually.

To cache the rendering of 3D content, configure the caching in the parent Viewport 2D node of the Scene node that contains the 3D content that you want to cache.

Because caching consumes GPU memory, it is by default disabled. When caching is disabled for a node, Kanzi renders that node normally and frees all resources associated with the render cache.
## Using automatic render cache updates

Use automatic render cache updates for complex nodes that are expensive to render and whose rendering does not change often. You can set Kanzi to cache a 2D node and automatically update the render cache when the rendering of that node or its descendant nodes changes and the cache image no longer correctly represents that node. For example, when the size or shape of a node change.
**Tip:** When you want to enable automatic cache updates for a complex node whose rendering does not change often but that has child nodes whose rendering changes often, move those child nodes to a separate node.
To set Kanzi to update the render cache of a 2D node automatically, in the Node Tree select the node, in the Properties add the Render Target > Caching Mode property, and set it to Automatic.
This way you set Kanzi to cache the node the next time it renders the node and does not detect changes in the rendering of the node or its descendants.
When you enable automatic render cache updates, Kanzi keeps checking for changes to the node or its descendant nodes during rendering:
- If the nodes are static, Kanzi recreates the cache image or renders the nodes using an existing and still valid cache image.
- If the rendering of the nodes changes, Kanzi invalidates the cache image and renders the nodes normally without caching.

## Controlling render cache updates manually

When you know exactly when the render cache of a 2D node needs updating, you can control the cache updates manually. You can enable caching for a node and set Kanzi to update the render cache when the node or any of its descendants change. For example, use the Set Property action or a binding to invalidate the render cache that you want Kanzi to update.

To control the render cache updates manually:

1.

In the Node Tree select the node that you want to cache, in the Properties add the Render Target > Caching Mode property, and set it to Enabled.

This way you set Kanzi to cache the node the next time it renders that node, and to keep rendering the node from the cache until you invalidate the cache.

If Kanzi already cached the node, it does not automatically update the cache.
2.

To set Kanzi to update the render cache, invalidate the render cache by disabling the Cache Valid property in the node whose render cache you want to update.

Set the cache invalidation to happen when you know that the node or any of its descendants change and you want Kanzi to update the render cache the next time it renders that node.

For example, in a trigger that sets the node to change, create a Set Property action that disables the Cache Valid property.
**Note:** Invalidating the render cache does not free any resources allocated by the node.
To free the resources associated with the render cache, set the Caching Mode property to Disabled.
