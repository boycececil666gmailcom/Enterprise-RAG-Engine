---
title: Resources
source: https://docs.kanzi.com/4.1.0/en/working-with/resources/resources.html
---

# Resources

In Kanzi, a resource is an item that you can reuse in different parts of your application. For example, a Mesh Data resource defines the geometry of a Model node, and you can use the same Color Brush in different nodes to set the Foreground Brush or Background Brush properties.

You can find all resources in a Kanzi Studio project in the Library window.

The Dictionaries window shows the resources in:

- The resource dictionaries that the node you select in the Node Tree can access. See Using resource dictionaries.
- The localization tables and theme groups in the project. See Localization and Theming your applications.

## Library views

By default, the Library shows all the resources in a project. Kanzi Studio provides Library views to show only selected resources in your project. You can enable these views in the Window menu:

- Animations shows animation data, animation clips, timeline sequences, and timeline entries in your project. See Animations.
- Bookmarks shows the shortcuts in your project. See Using bookmarks.
- Materials and Textures shows brushes, materials, material types, shader formats, and textures in your project. See Using brushes, Material types and materials, Using binary shaders, and Textures.
- Meshes shows the mesh data in your project. See Using meshes.
- Property Types shows the custom property types in your project. See Property types.
- Rendering shows the object sources, render passes, and filters in your project. See Using object sources, Rendering, and Filters.
- Resource Files shows the resource files in your project grouped by file type. See Using resource files.
- State Managers shows the state managers in your project. See State manager.
- Textures shows the textures in your project. See Textures.
- Trajectories shows the trajectories in your project. See Trajectories.

You can add any window as a tab to any other window to see more than one type of content in the same window.

See Customizing the Kanzi Studio interface.
## Load resources asynchronously

In Kanzi, you can load resource dictionaries of prefabs you use in your project before your Kanzi application shows them to users. For example, you can create a loading screen that your users see while Kanzi is loading the resource dictionaries of the rest of your application in the background.

See Loading node prefab resources asynchronously.

Use resource profiling to measure during runtime how long it takes to load and deploy resources and prefabs in your Kanzi application.

Resource profiling data helps you find out which resources to load asynchronously.

See Measuring the loading and deployment time of resources.
