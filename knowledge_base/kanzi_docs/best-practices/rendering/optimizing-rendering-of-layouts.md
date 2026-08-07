---
title: Optimizing the rendering of layouts
source: https://docs.kanzi.com/4.1.0/en/best-practices/rendering/optimizing-rendering-of-layouts.html
---

# Optimizing the rendering of layouts


Calculating a layout for a node or a sub-tree in the node tree can be a computationally intensive task. In general, any movement in any node of, for example, a Grid Layout node, causes recalculation of the layout, which in turn slows down framebuffer updating.

To optimize the rendering of layouts instead of the Layout Transformation property use the Render Transformation whenever possible. Render transformations do not recalculate a layout and can significantly decrease the amount of recalculations in a layout with many child nodes.

To use render transformations:

1.

In the Preview select the Node tool  and set the transformation tool to use the Render Transformation ().
2.

Use the Node tool to move, rotate, or scale the node in the Preview. See Editing your application in the Preview.


or

1.

In the Project select the node to which you want to apply a transformation.
2.

In the Properties click , and add the Render Transformation property.
3.

Use the Render Transformation property to apply the transformation for the node you selected in the first step.
