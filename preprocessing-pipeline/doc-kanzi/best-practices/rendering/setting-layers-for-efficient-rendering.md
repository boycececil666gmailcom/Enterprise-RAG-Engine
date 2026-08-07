---
title: Configuring nodes for efficient rendering
source: https://docs.kanzi.com/4.1.0/en/best-practices/rendering/setting-layers-for-efficient-rendering.html
---

# Configuring nodes for efficient rendering

Kanzi uses painterâs algorithm to render 2D nodes, meaning that if you place a background as the first node in the tree, pixels containing content are drawn first for the background and then again for the content.

Rendering some 2D nodes can be computationally heavy. In some cases a 2D child node has to be rendered first to its own render target, which is later composed onto the screen. 2D node composition happens in these cases:

- A Viewport 2D node that has rotation or scale applied.
- Any node that has both transparency and more than one child node with content.

## Viewing nodes rendered to a composition render target

In Kanzi Studio you can see which 2D nodes in your application Kanzi renders to a composition render target.

To view in the Preview the 2D nodes that use alpha blending in the Preview click  to enter the Analyze mode, right-click , and select Transparency.

The Preview highlights the nodes that Kanzi renders to a composition render target with translucent, blue stripes.
