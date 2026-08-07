---
title: Using the Dock Layout nodes
source: https://docs.kanzi.com/4.1.0/en/working-with/layouts/using-dock-layouts.html
---

# Using the Dock Layout nodes

Use the Dock Layout nodes to place nodes relative to each other along the sides of a Dock Layout node.

A Dock Layout node arranges its items in a subtractive way: after positioning the first node, the Dock Layout node uses the remaining space to position the next node, and so on. When arranging its child nodes, a Dock Layout node uses its entire size.

You set the side along which you want to place a node in a Dock Layout node with the Side property.

A Dock Layout node arranges its items in a subtractive way: after positioning the first node, the Dock Layout node uses the remaining space to position the next node, and so on. When arranging its child nodes, a Dock Layout node uses its entire size.

Dock Layout nodes determine the position of their child nodes by:

- The order in which the child nodes appear in the node tree.
- The value of the Side property in each child node of a Dock Layout node. The Dock Layout node sets each child node to occupy that entire side.
- The number of the child nodes in a Dock Layout node.

## Creating a Dock Layout node

To create a Dock Layout node:

1.

In the Node Tree, press Alt and right-click the node where you want to create a Dock Layout node and select either Dock Layout 3D, or Dock Layout 2D.

You can create a 3D node only in a 3D node, such as the Scene node, and a 2D node only in a 2D node.
2.

In the Node Tree, add child nodes to the layout that you created in the previous step.

For example, if you created a Dock Layout 3D, add several Plane nodes, if you created a Dock Layout 2D, add several Image nodes.

As you add child nodes, the Dock Layout node automatically positions them.
3.

In the Node Tree, select all child nodes of the Dock Layout node. In the Properties, add the Dock Layout > Side property and set it to:

  - Left to set the child node to occupy the left part of the Dock Layout node.
  - Right to set the child node to occupy the right part of the Dock Layout node.
  - Top to set the child node to occupy the top part of the Dock Layout node.
  - Bottom to set the child node to occupy the bottom part of the Dock Layout node.

For example, set the Side property for:

  - Image to Top
  - Button to Bottom
  - Temperature-F to Right
  - Condition to Right
  - Temperature-C to Left

4.

(Optional) When you want the last child node in a Dock Layout node to occupy the remaining space of the Dock Layout node, add to the Dock Layout node the Last Item Fill property, and enable it.
5.

(Optional) To clear the area around child nodes in a layout, in the Node Tree select child nodes in the layout, in the Properties click , and add and set the margin properties:

  - Depth Margin to clear the area in the back and the front of a child node.
  - Horizontal Margin to clear the area on the left and the right sides of a child node.
  - Vertical Margin to clear the area on the bottom and the top of a child node.

## Setting the appearance of a Dock Layout 2D node

To set the appearance of 2D nodes:

- You can fill 2D nodes with a solid color, a texture, or a material. See Adjusting the appearance of 2D nodes.
- You can apply a post-processing effect to a 2D node. See Effects for 2D nodes.
- You can rotate a 2D node around all three axes to create a 3D perspective effect. See Creating a 3D perspective effect for 2D nodes.
- You can apply custom rendering to 2D nodes to create post-processing effects. See Applying custom rendering to 2D nodes.
- You can render a 2D node as pixel-perfect. See Rendering pixel-perfect 2D nodes.

## Using the Dock Layout 3D node in the API

For details, see the `DockLayout3D` class.
## Using the Dock Layout 2D node in the API

For details, see the `DockLayout2D` class.
## Dock Layout property types and messages

For lists of the available property types and messages for the Dock Layout nodes, see Dock Layout 2D and Dock Layout 3D.
