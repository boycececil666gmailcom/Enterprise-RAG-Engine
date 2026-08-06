---
title: Using the Stack Layout nodes
source: https://docs.kanzi.com/4.1.0/en/working-with/layouts/using-stack-layouts.html
---

# Using the Stack Layout nodes


Use the Stack Layout nodes to arrange nodes next to each other on the selected axis.

You can set the direction and the starting point for arranging Stack Layout 3D child nodes on x, y, and z axes, and Stack Layout 2D child nodes on x and y axes.
## Creating a Stack Layout node


To create a Stack Layout node:

1.

In the Node Tree press Alt and right-click the node where you want to create a Stack Layout node and select either Stack Layout 3D, or Stack Layout 2D.

You can create a 3D node only in a 3D node, such as the Scene node, and a 2D node only in a 2D node.

> **Tip:** In the Preview select the Stack Layout 2D tool  to create a Stack Layout 2D node by clicking and dragging in the Preview. The  above the Stack Layout 2D shows the direction of the layout.
>
> - When you create a layout whose width is greater than its height, the direction of the layout is on the x axis.
> - When you create a layout whose height is greater than its width, the direction of the layout is on the y axis.
>
> 2.
>
> In the Node Tree, add child nodes to the layout that you created in the previous step.
>
> For example, if you created a Stack Layout 3D node, add several Sphere nodes, if you created a Stack Layout 2D node, add several Image nodes.
>
> As you add child nodes, the Stack Layout node positions them along the axis defined by its Direction property.
> 3.
>
> (Optional) In the Properties set the Direction property to the axis long which you want the Stack Layout node to arrange its child nodes.
> 4.
>
> (Optional) To clear the area around child nodes in a layout, in the Node Tree select child nodes in the layout, in the Properties click , and add and set the margin properties:
>
> - Depth Margin to clear the area in the back and the front of a child node.
> - Horizontal Margin to clear the area on the left and the right sides of a child node.
> - Vertical Margin to clear the area on the bottom and the top of a child node.


## Reversing the order of Stack Layout node child nodes


To reverse the order of child nodes in a Stack Layout node, in the Node Tree select the Stack Layout node for which you want to reverse the order of child nodes and in the Properties enable the Reversed property.
## Setting the appearance of a Stack Layout 2D node


To set the appearance of 2D nodes:

- You can fill 2D nodes with a solid color, a texture, or a material. See Adjusting the appearance of 2D nodes.
- You can apply a post-processing effect to a 2D node. See Effects for 2D nodes.
- You can rotate a 2D node around all three axes to create a 3D perspective effect. See Creating a 3D perspective effect for 2D nodes.
- You can apply custom rendering to 2D nodes to create post-processing effects. See Applying custom rendering to 2D nodes.
- You can render a 2D node as pixel-perfect. See Rendering pixel-perfect 2D nodes.

## Using the Stack Layout 3D node in the API


To create a Stack Layout 3D node:

```
// Create a Stack Layout 3D node named Stack.
StackLayout3DSharedPtr stack = StackLayout3D::create(domain, "Stack");

```


To control the direction of a Stack Layout 3D node:

```
// Set the Stack Layout 3D node to arrange its items along the x axis.
stack->setDirection(StackLayout3D::DirectionX);

```


To add items to a Stack Layout 3D node:

```
// Stack Layout 3D node arranges its items in the order that you add items.
// Create a Model node and ...
Model3DSharedPtr item1 = Model3D::createBox(domain, "item1", Vector3(1.3f, 1.3f, 1.3f), ThemeRed);
// ... add it to the Stack Layout 3D node.
stack->addChild(item1);
Model3DSharedPtr item2 = Model3D::createSphere(domain, "item2", 0.8f, 30, 30, ThemeGreen);
stack->addChild(item2);
Model3DSharedPtr item3 = Model3D::createBox(domain, "item3", Vector3(1.0f, 1.0f, 1.0f), ThemeBlue);
stack->addChild(item3);

```


To reverse the order in which a Stack Layout 3D node arranges its items:

```
// Set the Stack Layout 3D node to arrange its items in the reverse order.
stack->setReversed(true);

```


For details, see the `StackLayout3D` class.
## Using the Stack Layout 2D node in the API


To create a Stack Layout 2D node:

```
// Create a Stack Layout 2D node named Stack.
StackLayout2DSharedPtr stack = StackLayout2D::create(domain, "Stack");

```


To control the direction of a Stack Layout 2D node:

```
// Set the Stack Layout 2D node to arrange its items along the x axis.
stack->setDirection(StackLayout2D::DirectionX);

```


To add items to a Stack Layout 2D node:

```
// Stack Layout 2D arranges its items in the order that you add items.
// Create a 2D node ...
EmptyNode2DSharedPtr item1 = EmptyNode2D::create(domain, "item1", 100.0f, 100.0f, ThemeRed);
// ... and add it to the Stack Layout 2D node.
stack->addChild(item1);
EmptyNode2DSharedPtr item2 = EmptyNode2D::create(domain, "item2", 100.0f, 100.0f, ThemeGreen);
stack->addChild(item2);
EmptyNode2DSharedPtr item3 = EmptyNode2D::create(domain, "item3", 100.0f, 100.0f, ThemeBlue);
stack->addChild(item3);

```


To reverse the order in which a Stack Layout 2D node arranges its items:

```
// Set the Stack Layout 2D node to arrange its items in the reverse order.
stack->setReversed(true);

```


For details, see the `StackLayout2D` class.
## Stack Layout property types and messages


For lists of the available property types and messages for the Stack Layout nodes, see Stack Layout 2D and Stack Layout 3D.
