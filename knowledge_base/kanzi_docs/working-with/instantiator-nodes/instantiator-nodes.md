---
title: Using the Instantiator node
source: https://docs.kanzi.com/4.1.0/en/working-with/instantiator-nodes/instantiator-nodes.html
---

# Using the Instantiator node


Use the Instantiator node to replicate the appearance of a 3D node or a tree of 3D nodes that the Instantiator node targets.

Instantiator node contains a reference to a target node or a tree of nodes. When Kanzi renders the Instantiator node, it copies the appearance of the node that the Instantiator node targets. This means that all changes to the target node are always reflected in the Instantiator node. For example, you can use the Instantiator node to create a reflection.

Each Instantiator node has a unique transformation, so you can use more than one Instantiator node to target the same node. You cannot override other properties in the Instantiator node, so all instances are identical. However, each Instantiator node is rendered separately. For example, this enables lights to differently affect Instantiator nodes in different positions.

To create truly unique instances of a node, convert that node to a prefab, and use instances of that prefab. See Using node prefabs.

Note that the Instantiator node affects only rendering. Because the layout size of an Instantiator node is 0, you cannot use it in layouts. The instantiated nodes are not interactive.

Learn how to use the Instantiator node by completing a tutorial. See Tutorial: Create reflections.
## Creating an Instantiator node


To create an Instantiator node:

1.

Create the content that you want to replicate using an Instantiator node.
2.

In the Node Tree press Alt and right-click the node where you want to create an Instantiator node and select Instantiator.

You can create an Instantiator node only in a 3D node.
3.

In the Node Tree select the Instantiator node and in the Properties set the Instantiated Node property to the node that you want to replicate with this Instantiator node.

Kanzi Studio instantiates the node.
4.

In the Properties set the transformation of the Instantiator node.

For example, add and set the Render Transformation property to scale, rotate, and position the instantiated node.

## Creating an Instantiator node from a node


To create an Instantiator node from a node:

1.

In the Node Tree press Alt and right-click the node that you want the Instantiator node to show and select Instantiate Into an Instantiator.

Kanzi Studio creates an Instantiator node and sets its Instantiated Node property to the selected node.
2.

In the Properties set the transformation of the Instantiator node.

For example, add and set the Render Transformation property to scale, rotate, and position the instantiated node.

## Using the Instantiator node in the API


To create a reflection using an Instantiator node:

```
// Create an Instantiator node named Instantiator3D.
Instantiator3DSharedPtr instantiator = Instantiator3D::create(domain, "Instantiator3D");
// Set the node that you want the Instantiator node to reflect.
instantiator->setTarget(targetNode);
// To mirror the target node across the xz plane, set the scaling of the Instantiator node
// to a non-uniform value. This inverts all triangles, so you must disable the backface
// culling rendering for the Instantiator node.
instantiator->setRenderTransformation(SRTValue3D::createScale(Vector3(1.0f, -1.0f, 1.0f)));

```


For details, see the `Instantiator3D` class.
## Instantiator node property types and messages


For a list of the available property types and messages for the Instantiator node, see Instantiator.
