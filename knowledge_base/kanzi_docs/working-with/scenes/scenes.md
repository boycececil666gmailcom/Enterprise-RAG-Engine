---
title: Using the Scene node
source: https://docs.kanzi.com/4.1.0/en/working-with/scenes/scenes.html
---

# Using the Scene node


Use the Scene node to show 3D content in your Kanzi application.

The Scene node can contain light nodes, Camera node, and all other Kanzi 3D nodes.

Once you import or create content in a scene, move the content around the node tree to place the content where you want it to appear in your Kanzi application. Note that for all inheritable properties (for example, transformation), a change in a parent node affects all its children. See Property system.
## Creating a Scene node


Only the Viewport 2D node can render a Scene node. However, you can create a Scene node in the Prefabs and instantiate it when you want to show the content of that Scene in your application.

To create a Scene node:

1.

In the Node Tree press Alt and right-click the RootNode and select Viewport 2D.
2.

In the Node Tree press Alt and right-click the Viewport 2D and select Scene.

When you create a new scene it contains only a Camera and a Directional Light.

## Using the Scene node in the API


For details, see the `Scene` class.
## Scene property types and messages


For a list of the available property types and messages for the Scene node, see Scene.
