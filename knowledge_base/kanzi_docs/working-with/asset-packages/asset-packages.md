---
title: Asset packages
source: https://docs.kanzi.com/4.1.0/en/working-with/asset-packages/asset-packages.html
---

# Asset packages


Kanzi Studio asset packages are collections of ready-made content that you can import to your Kanzi Studio projects. With asset packages, you can create an asset library with content, such as UI components, materials, brushes, styles, and textures.

Use asset packages to make this content available for use in different Kanzi Studio projects or to share the content within your company for all your Kanzi applications. For example, the Factory Content asset packages that come with Kanzi Studio contain such content. See Factory Content assets.
## Adding asset sources


Any directory that contains Kanzi Studio asset packages is an asset source. See Creating an asset package.

To add an asset source to Kanzi Studio:

1.

In the Asset Packages window, click + Add Asset Source.
2.

In the Select Asset Directory dialog, select the directory that you want to add.


After you add an asset source, you see in the Asset Packages window all the items included in the asset packages that are stored in the directory that you added as an asset source.

When you add an asset source to Kanzi Studio, you make that asset source available to all your Kanzi Studio projects.
## Using asset packages


To use asset packages:

1.

In the Asset Packages window, select an asset source.
2.

To import an item from the Asset Packages to your Kanzi Studio project, either:

  - From the Asset Packages window, drag an item to a node in the Node Tree, to the Prefabs, or to the Preview.
  - In the Asset Packages, right-click the item and select Import Asset Package.


For example, drag an item to the Node Tree and drop it on a node. Kanzi Studio adds that item to the Prefabs, and instantiates it as a prefab in the node where you dropped that item.

## Creating an asset package


To share content with other Kanzi Studio users, you can create your own asset packages. You create an asset package by marking a Kanzi Studio project as an asset package, and by marking in that project all the items that you want to include in that asset package. When a Kanzi Studio user adds as an asset source a directory, which contains an asset package project, they see in the Asset Packages window all the items in that asset package.

To create an asset package:

1.

In Kanzi Studio, in the project from which you want to create an asset package, in the Prefabs and Library, select each item that you want to include in that asset package. In the Properties, add and set:

  - Resources > Export in Asset Package to enabled
  - (Optional) Resources > Custom Asset Thumbnail to the bitmap image that you want to use as a thumbnail for your asset in the Asset Packages window

If you do not set a custom thumbnail, Kanzi Studio generates the thumbnail automatically.

To enable Kanzi Studio to generate thumbnails, make sure that the Preview is running and that Kanzi Studio renders thumbnails. To enable thumbnail rendering, select Edit > User Preferences. In the Advanced tab, enable Render thumbnails.


For example, create from a Viewport 2D node a prefab and mark that prefab to be exported in the asset package.
2.

In the Kanzi Studio main menu, select Project > Properties. In the Properties, in the Profile category, enable the Is Asset Package property.
3.

Save the Kanzi Studio project. The project is now a Kanzi Studio asset package.

When a Kanzi Studio user adds as an asset source a directory that contains an asset package project, they see in the Asset Packages window all the items in that asset package. See Adding asset sources.
