---
title: Using the Factory Content assets
source: https://docs.kanzi.com/4.1.0/en/working-with/factory-content/using-the-factory-content-assets.html
---

# Using the Factory Content assets

You can add assets from the Factory Content asset source to your Kanzi application in Kanzi Studio. For a list of the Factory Content, see Factory Content assets.
## Using Factory Content in your project

To use Factory Content in your project:

1.

In the Asset Packages window select the Factory Content asset source.

The Factory Content asset packages contain ready-made components and materials that you can use to create prototype projects faster.
2.

From the Asset Packages drag the item that you want to use in your project to a node in the Node Tree, to the Prefabs, or to the Preview.

For example, drag the Car to the Preview. When you drag an item from the Asset Packages to the Preview or a node in the Node Tree or Pages, Kanzi Studio instantiates that item as a prefab, and adds it to the Prefabs.

## Using Factory Content materials in your project

To use Factory Content materials in your project:

1.

In the Asset Packages window select the Factory Content asset source.

The Factory Content asset packages contain ready-made components and materials that you can use to create prototype projects faster.
2.

From the Asset Packages drag the material that you want to use in your project to a node in the Preview, or a node in the Node Tree.

For example, to use a material for a car body, drag that material to either:

  - Preview and drop it on the car body.
  - Node Tree and drop it on the Model node that shows the mesh for the car body.

When you use a Factory Content material in your project, Kanzi Studio adds that material to the Library > Materials and Textures > Materials, and the shaders used by the material to the Library > Resource Files > Shaders.

To use a material that uses normal map textures, the 3D model where you want to use such material must have tangents. These Factory Content materials use normal map textures:

  - Aluminium Material
  - Carbon Fiber Material
  - Leather Material
  - Rubber Material

To use a material with a normal map texture on a primitive mesh, select the primitive mesh node and in the Properties enable the Generate Tangents property.
