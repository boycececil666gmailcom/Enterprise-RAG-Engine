---
title: Using the Viewport 2D node
source: https://docs.kanzi.com/4.1.0/en/working-with/viewports/viewport-2d.html
---

# Using the Viewport 2D node

Viewport 2D node can render both a Scene, which is a 3D node, and 2D nodes, such as Image or Button 2D.

When you create a Kanzi Studio project, that project contains a Viewport 2D node with a Scene that contains a Camera and a Directional Light. For Kanzi Engine, the Scene node is always the first child of a Viewport 2D node.
## Creating a Viewport 2D node

To create a Viewport 2D node:

1.

In the Node Tree or Prefabs, press Alt and right-click a 2D node where you want to create a Viewport 2D node, and select Viewport 2D.
2.

Add content to the Viewport 2D node that you created.

For example:

  1.

In the Node Tree or Prefabs, press Alt and right-click the Viewport 2D node and select Scene.

Kanzi Studio creates a Scene node that contains a Camera node and a Directional Light node.
  2.

In the Scene node, create the 3D nodes that you want to show.

See 3D assets.

## Controlling how Kanzi renders a Viewport 2D node

You can control how Kanzi renders a Viewport 2D node. Kanzi renders the background brush before the content of the Viewport 2D node by default.

To control how Kanzi renders a Viewport 2D node, set the Foreground Hint property to:

- None to render the background brush after rendering the Viewport 2D node. Use it when the content of the Viewport 2D node is opaque.
- Translucent to render the background brush before the content of the Viewport 2D node. This is the default value. Use it when the content in the Viewport 2D node is alpha-blended.
- Occluding to not render the background brush. Use it when the entire Viewport 2D node is filled with 3D content.

## Using the Viewport 2D node in the API

To create a Viewport 2D node:

```
// Create a Viewport 2D named Viewport 2D and add it to the RootPage.
Viewport2DSharedPtr viewport2d = Viewport2D::create(domain, "Viewport 2D");
rootNode->addChild(viewport2d);

// To render 3D nodes in a Viewport 2D you need to add a Scene to the Viewport 2D.
// Create a Scene named Scene for 3D nodes and add it to the Viewport 2D.
SceneSharedPtr sceneNode = Scene::create(domain, "Scene for 3D nodes");
viewport2d->setScene(sceneNode);

// Create a Camera named Camera and add it to the Scene.
CameraSharedPtr camera = Camera::create(domain, "Camera");
sceneNode->addChild(camera);

// Create a Point Light named Point light and add it to the Scene.
LightSharedPtr light = Light::createPoint(domain, "Point light");
sceneNode->addChild(light);

// Create a Box mesh named Box and add it to the Scene.
Model3DSharedPtr box = Model3D::createCube(domain, "Box", 1.0f, ThemeBlue);
sceneNode->addChild(box);

```

For details, see the `Viewport2D` class.
## Viewport 2D property types and messages

For a list of the available property types and messages for the Viewport 2D node, see Viewport 2D.
