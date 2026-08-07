---
title: Layouts
source: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/layouts.html
---

# Layouts

In Kanzi there are three types of layouts:

Layouts that base the position and size of their child nodes, such as the Flow Layout, Grid Layout, Stack Layout, and Trajectory Layout nodes. For example, these layouts are useful when the amount of content changes dynamically. |

Content controls that show specific content and usually center the content, such as the Image node and Button nodes. |

Absolute positioning controls that act as containers that group their child nodes, such as the Viewport 2D and Empty Node 2D nodes. |

You can use layout nodes to position nodes in relation to the application screen and other nodes. Layout consists of properties alignment, margins and layout size and that you can define either specific to a node or as a general rule imposed on child nodes by specific layout containers.

See Layout control nodes.
## Universal layout properties

To position items in your Kanzi applications you can use these transformation types:

- Layout transformation transforms the item before it applies the layout pass.
- Render transformation transforms the item after it applies the layout pass, but before it renders the item.

Kanzi applies the render transformation after applying the layout transformation, and does not affect the layout calculations. For example, this allows you to animate nodes within a layout without causing the layout recalculation.

Layout control nodes, such as Stack Layout and Grid Layout nodes, apply their own transformations on all immediate child nodes who in their part define their own layout considering their own child nodes, layout transformations, margins and alignments.

- Alignment defines the gravity of the layout. For example, set the Horizontal Alignment property to Right to align the node to the right side of its parent layout. By setting alignment properties to Stretch, the node stretches to the dimensions of its parent layout. Use the Content Stretch property to specify how a layout handles its content.
- Margin enforces the object spacing relative to the border of its parent layout. For example, set the Horizontal Margin property to set the spacing on the left and right sides of the node in relation to its parent layout.
- Layout properties override the bounding box size of a node. The default layout size is defined by the size of the node based on its bounding box and margins.

For example, a Stack Layout node set in direction on the x axis places its two child nodes next to each other based on their dimensions (bounding boxes). By using the Layout Width property you can override the width of the bounding box: a value smaller than the size of the node makes the node overlap, and a value larger than the size of the node extends the space between the two nodes.

After all the layout tasks are done, Kanzi applies the final transformations from the parent nodes. The RootNode under the Screen node has special rules for its layout if it is a Viewport 2D or an Empty Node 2D. It inherits the defined screen size, unless defined by the layout properties.
