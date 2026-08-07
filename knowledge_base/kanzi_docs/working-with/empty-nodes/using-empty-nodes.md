---
title: Using the Empty Node nodes
source: https://docs.kanzi.com/4.1.0/en/working-with/empty-nodes/using-empty-nodes.html
---

# Using the Empty Node nodes

Use the Empty Node nodes to group nodes and to set property values of their child nodes.

By default, Empty Node nodes do not have a visual representation, or any functionality other than a transparent background and that they can act as a parent node to other nodes. Empty Node nodes do not have any properties specific only to them.

For example, use Empty Node nodes to:

- Edit the origin of nodes. See Editing the origin of nodes.
- Apply transformation to all its child nodes. See Tutorial: Create reflections.
- Replace the root node of a node prefab. See Replacing the root node of a node prefab.

An Empty Node is a node into which you can put any other node and has these properties:

- It allows absolute positioning of its child nodes.
- Does not restrict the movement of its child nodes.
- Is not a compacting layout.

Empty Node does not have inherent layout characteristics. Empty Node does not resize its child nodes, but places them to a position you specify. The default values of the Layout Height and Layout Width properties of an Empty Node are 0, but it stretches by default to take all the space its child nodes need.

You can use the Horizontal Alignment and Vertical Alignment properties to align the child nodes of an Empty Node only after you specify the Layout Height and Layout Width properties of that Empty Node.
## Creating an Empty Node node

To create an Empty Node node:

1.

In the Node Tree press Alt and right-click the node where you want to create an Empty Node node and select either Empty Node 3D, or Empty Node 2D.

You can create a 3D node only in a 3D node, such as the Scene node, and a 2D node only in a 2D node.
2.

In the Node Tree add items to the Empty Node node.

For example, if you created an Empty Node 3D node, add Sphere nodes, if you created an Empty Node 2D node, add Image nodes.
3.

(Optional) In the Node Tree select the Empty Node node, in the Properties click , add and set the property you want all its child nodes to inherit.

## Setting the appearance of an Empty Node 2D node

To set the appearance of 2D nodes:

- You can fill 2D nodes with a solid color, a texture, or a material. See Adjusting the appearance of 2D nodes.
- You can apply a post-processing effect to a 2D node. See Effects for 2D nodes.
- You can rotate a 2D node around all three axes to create a 3D perspective effect. See Creating a 3D perspective effect for 2D nodes.
- You can apply custom rendering to 2D nodes to create post-processing effects. See Applying custom rendering to 2D nodes.
- You can render a 2D node as pixel-perfect. See Rendering pixel-perfect 2D nodes.

## Using the Empty Node 3D node in the API

To create an Empty Node 3D node using the API:

```
// Create an Empty Node 3D named Empty3D
EmptyNode3DSharedPtr emptyNode = EmptyNode3D::create(domain, "Empty3D");

// Create and add a cube to the Empty Node 3D
ModelSharedPtr cube = Model::createCube(domain, "Cube", 1.0f, KanziThemeOrange);
emptyNode->addChild(cube);

```

For details, see the `EmptyNode3D` class.
## Using the Empty Node 2D node in the API

To create an Empty Node 2D node using the API:

```
// Create an Empty Node 2D named Empty2D
EmptyNode2DSharedPtr empty2D = EmptyNode2D::create(domain, "Empty2D");

// Create and add an Image to the Empty Node 2D
ImageSharedPtr image = Image::create(domain, "Image");
image->setTextureResourceID(ResourceID("DefaultTexture"));
empty2D->addChild(image);

```

For details, see the `EmptyNode2D` class.
## Empty Node property types and messages

For lists of the available property types and messages for the Empty Node nodes, see Empty Node 2D and Empty Node 3D.
