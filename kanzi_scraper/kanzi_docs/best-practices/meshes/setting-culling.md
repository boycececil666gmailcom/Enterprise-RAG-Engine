---
title: Setting culling
source: https://docs.kanzi.com/4.1.0/en/best-practices/meshes/setting-culling.html
---

# Setting culling


In Kanzi render passes you can optimize the performance of meshes in your applications by setting the culling properties.
## Setting the cull mode


By default Kanzi culls in 3D content the polygons whose normal points away from the active camera. To override this, you can set the cull mode in a Pipeline State render pass.

To set the cull mode:

1.

In the Library > Rendering > Render Pass Prefabs create a Pipeline State render pass, or select an existing Pipeline State render pass. See Render passes.
2.

In the Pipeline State render pass create the render passes that you use to draw the nodes you want to cull.

For example, create a Clear render pass, a Gather Lights render pass, and inside the Gather Lights render pass create a Draw Objects render pass.

You can use filters to collect specific nodes for rendering. See Filters.
3.

In the Library select the Pipeline State render pass and in the Properties set the Cull Mode property to:

  - Back to make Kanzi not render the polygons whose normal points away from the active camera This is the default value for the Cull Mode property. If you do not set the Cull Mode property in a Pipeline State render pass, Kanzi uses the value for the property set in the nearest ancestor Pipeline State render pass. If there is no ancestor Pipeline State render pass, Kanzi uses the default value.
  - Front to make Kanzi not render the polygons whose normal points towards the active camera
  - None to disable culling

4.

Take into use the render passes you created:

  1.

In the Node Tree select the Viewport 2D node which contains the content that you want to render.
  2.

In the Properties set the Render Pass Prefab property to the Pipeline State render pass or to the render pass prefab which contains the Pipeline State render pass that you created.


## Controlling frustum culling


Use frustum culling when you have a lot of meshes outside of the view frustum of the camera. The view frustum is the volume visible to the active camera and contains the nodes whose bounding volume clips the view frustum. Frustum culling enables you to trade GPU time spent culling the meshes for CPU time.

To control frustum culling:

1.

In the Library select the Draw Objects render pass you use to render the meshes for which you want to set frustum culling. See Rendering.
2.

In the Properties add and enable the Frustum Culling property.

This way Kanzi does not render the meshes when they are outside of the view frustum.
3.

(Optional) In the Node Tree select the nodes that contain the meshes for which you want to set frustum culling, in the Properties click , add the Frustum Cull Margin property, and set it to the amount of space around the node you do not want to cull.

For example, this is useful when a vertex shader radically modifies the geometry of nodes, such as in vertex skinned nodes.


To see if your frustum culling setting works as you intended it to work, in the Preview click  to enter the Analyze mode, right-click , select the Performance HUD, and move the camera away from the node for which you want to control culling. When culling does not occur anymore for the node, the Draw Count value drops.
