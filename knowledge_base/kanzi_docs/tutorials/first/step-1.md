---
title: Step 1 - Create a new project and import assets
source: https://docs.kanzi.com/4.1.0/en/tutorials/first/step-1.html
---

# Step 1 - Create a new project and import assets


When you create a new project, Kanzi Studio creates a project directory in your Kanzi Studio workspace and adds to that directory the required file structure for the project. When importing assets to your project, Kanzi Studio copies the imported assets to the project directory.

You defined the location of the Kanzi Studio workspace during Kanzi installation.

In this step, you first create a new project, then you import the assets that you use in this tutorial.
## Get the tutorial


To get the tutorial, in the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the First tutorial, click .

Kanzi Studio downloads the tutorial to the `<KanziWorkspace>/Tutorials` directory. You can find:

- The tutorial assets in the `<KanziWorkspace>/Tutorials/First/Assets` directory.
- The completed tutorial in the `<KanziWorkspace>/Tutorials/First/Completed` directory.

## Create a new Kanzi Studio project


In this section, you create a new Kanzi Studio project and set the size of the application screen.

1.

In Kanzi Studio Quick Start window, click New.
2.

In the New tab of the Quick Start window:

  - Name your project.

For example, name it First Application.
  - For the Materials select High performance vertex shaders.

The vertex-based shading offered in the High performance vertex shaders material type is a good choice for mobile GPUs, because of the lower cost of vertex-based shading.


Click Create to create the project.

This is how Kanzi Studio looks when you create a new project.

> **Note:** The Kanzi Studio Preview by default uses the TCP/IP for internal communication with Kanzi Studio. If you have a firewall installed on your computer, allow the `Kanzi Preview` process to go through the firewall.
> 3.
>
> Configure the Screen node:
>
> 1.
>
> In the Node Tree window, select the Screen node.
> 2.
>
> In the Properties window, set the Screen Resolution property to 854x480 - FWVGA.
>
> This way you set the size of the application screen.


## Import assets


In this section, you use the Assets window to import the images and 3D assets that you need to complete this tutorial.

To import assets:

1.

In the Assets window located in the bottom part of the Kanzi Studio interface, click Import Assets.
2.

Go to the `<KanziWorkspace>/Tutorials/First/Assets` directory, select all files, and click Open.

Kanzi Studio imports the selected assets to your project and shows them in the Assets window.

Use the Assets window to view, select, and use the assets in your project.

When you import 3D assets, Kanzi Studio creates for each 3D asset:

  - In the Prefabs, a Scene prefab for each scene in the imported file.

Kanzi Studio names each Scene prefab after the imported file. When you import a glTF file that contains multiple scenes, Kanzi Studio appends to the name of each Scene prefab the name of the scene.

In each Scene prefab, Kanzi Studio creates the scene hierarchy from the imported file and places the assets from the imported file into that prefab.
  - In the Library, Kanzi Studio places all resources from the imported file, such as Meshes, Splines, Animations, and Materials.


The assets in this tutorial contain only one 3D asset which Kanzi Studio places in the Car prefab. To see the content of the prefab, in the Prefabs window hover over its thumbnail.


Introduction Next step
