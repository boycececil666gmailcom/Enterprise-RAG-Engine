---
title: Step 2 - Apply the stencil
source: https://docs.kanzi.com/4.1.0/en/tutorials/stencil/step-2.html
---

# Step 2 - Apply the stencil


In this step you use render passes and the Stencil node to show only a selected part of the ContactsList node.

You use render passes to first write to the stencil buffer the shape of the Stencil node. Then you use the stencil testing to draw to the screen only the parts of the ContactsList node which the Stencil node covers and that you wrote to the stencil buffer.

The stencil buffer is an image in the current framebuffer which you can use to control which pixels Kanzi renders. You use render passes to discard or render specific pixels in your content depending on the values of the stencil buffer. This way you can limit the area of rendering to the shape of a node you use as a stencil. The shape of the node works as the gap in the stencil, determining which parts of your content are visible.

To apply the stencil:

1.

In the Library > Rendering press Alt and right-click Render Pass Prefabs, select Group render pass, and name it Stencil render pass.

You use a Group render pass to collect the render passes which apply a stencil on the content.
2.

In the Library > Rendering > Render Pass Prefabs > Stencil render pass create a Clear render pass, in the Properties add the Clear Stencil property, and set it to 0. This way you clear the stencil buffer by writing the value 0 to all pixels in the stencil buffer. You use the stencil buffer later in this procedure to limit the area of rendering to the shape of the Stencil node.
3.

In the Node Tree select the RootNode > Viewport 2D node and in the Properties set the Render Pass Prefab property to the Stencil render pass.

This way you set Kanzi to render the Viewport 2D node using the Stencil render pass.

The Stencil render pass does not draw anything on the screen yet, which is why in the Preview the Viewport 2D node is empty.
4.

Write to the stencil buffer the shape of the Stencil node:

  1.

In the Library > Rendering > Render Pass Prefabs > Stencil render pass create a Draw Objects render pass, name it Draw Stencil, in the Properties add the Object Source property, and set it to the Stencil Filter Tag Filter.

You use the Object Source property to pass to a Draw Objects render pass only the nodes you want it to render.

Here you set the Stencil render pass to render only the Stencil node.
  2.

In the Library > Rendering > Render Pass Prefabs > Stencil render pass create a Pipeline State render pass, name it Stencil Write, and drag the Draw Stencil render pass to the Stencil Write render pass.

You use this render pass to write to the stencil buffer.
  3.

In the Library > Rendering > Render Pass Prefabs > Stencil render pass select Stencil Write, and in the Properties add and set:

    - Color Write Mode to None

This way you make the Stencil node invisible.
    - Depth Write Enabled to disabled

This way you prevent the Draw Stencil render pass from writing the Stencil node to the depth buffer.
    - Stencil Test Function to Always

You use this property to control how the stencil test compares the stencil reference value to the value in the stencil buffer. You set the property to Always to always pass the test.

This way you make the Draw Stencil render pass write to the stencil buffer the Stencil node.
    - Stencil Function Reference Value to 1

By setting Stencil Function Reference Value to 1 you make the Draw Stencil render pass write to the stencil buffer with the value 1.
    - Stencil Pass Depth Pass Operation to Replace

This way you replace the current value in the stencil buffer with the value of the Stencil Function Reference Value property.
    - Stencil Write Enabled to enabled

This way you write to the stencil buffer the shape of the Stencil node with the value 1, and leave the value 0 everywhere else.


5.

Render the list of contacts:

  1.

In the Library > Rendering > Render Pass Prefabs > Stencil render pass create a Gather Lights render pass.

You use this render pass to collect in the Viewport 2D node, which uses the Stencil render pass prefab, the Light nodes that light the list of contacts.
  2.

In the Library > Rendering > Render Pass Prefabs > Stencil render pass > Gather Lights render pass create a Draw Objects render pass, name it Draw ContactsList, in the Properties add the Object Source property, and set it to the Content Filter Tag Filter.

Kanzi now renders the ContactsList and Directional Light nodes. However, Kanzi does not render the Stencil node because the Content Filter excludes the nodes with the Stencil tag.
  3.

In the Library > Rendering > Render Pass Prefabs > Stencil render pass create a Pipeline State render pass, name it Stencil Test, and drag the Gather Lights render pass to the Stencil Test render pass.

In the next step you use the Stencil Test render pass to limit the rendering of the Draw ContactsList render pass to the area you wrote to the stencil buffer earlier in this procedure.
  4.

In the Library > Rendering > Render Pass Prefabs > Stencil render pass select Stencil Test, and in the Properties add and set:

    - Stencil Test Function to Equal
    - Stencil Function Reference Value to 1


This way you limit the area of rendering of the ContactsList node to those pixels which have the stencil value 1, so that the render pass draws only the part of the ContactsList node which overlaps the Stencil node.


Previous step
## Whatâs next?


In this tutorial you learned how to apply a stencil to 3D content so that Kanzi renders only a selected area of the content. Now you can:

- Learn how to use render passes to apply a bloom effect on 3D content. See Tutorial: Create a bloom effect.
- Learn how to use a List Box node to create a list of contacts which receives data from a data source. See Tutorial: Create a contacts list with a Grid List Box.
- Learn how to define a data source in Kanzi and get the data for your Kanzi application from a data source. See Tutorial: Get application data from a data source.
