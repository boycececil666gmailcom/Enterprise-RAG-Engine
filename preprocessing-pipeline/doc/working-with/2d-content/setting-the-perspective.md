---
title: Creating a 3D perspective effect for 2D nodes
source: https://docs.kanzi.com/4.1.0/en/working-with/2d-content/setting-the-perspective.html
---

# Creating a 3D perspective effect for 2D nodes

Use the Perspective Transformation property to create a 3D perspective effect for 2D nodes. With the Layout Transformation Rotation property field you can rotate a node only in the 2D space, around the z axis. With the Perspective Transformation Rotation X, Y, and Z property fields you can rotate a 2D node around all three axes, creating a 3D perspective effect.

The Perspective Transformation property transforms the node after it applies the layout pass, but before it renders the node.

To create a 3D perspective effect for a 2D node:

1.

In the Node Tree create or select a 2D node for which you want to create a 3D perspective effect. For example, create an Image node.
2.

In the Properties add the Perspective Transformation property.
3.

In the Properties in the Perspective Transformation property set:

  - Rotation X to the number of degrees you want to rotate the node around the x axis.
  - Rotation Y to the number of degrees you want to rotate the node around the y axis.
  - Rotation Z to the number of degrees you want to rotate the node around the z axis.

For example, set the Perspective Transformation Rotation Y property field to 45 to rotate the image 45 degrees around the y axis.
4.

(Optional) In the Properties add the Render Transformation Origin property and set:

  - X to the percentage of the node width you want to set the origin on the x axis
  - Y to the percentage of the node height you want to set the origin on the y axis

In Kanzi by default the origin of all 2D nodes is in the upper left corner of the node. You use the Render Transformation Origin property to set the origin of the node.

For example, if you set the Perspective Transformation property to rotate the node around the y axis, to make the node rotate around its horizontal center point set the Render Transformation Origin X property field to 0,5.
