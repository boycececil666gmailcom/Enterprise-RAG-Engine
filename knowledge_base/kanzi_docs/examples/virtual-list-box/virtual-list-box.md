---
title: Virtual list box example
source: https://docs.kanzi.com/4.1.0/en/examples/virtual-list-box/virtual-list-box.html
---

# Virtual list box example

This example shows how to create a list box component that displays a set of objects that come from an external data source. In the example, the external data source is a text file which contains a list of image file names. The list box shows the images and their filenames. Because image loading is slow and takes a lot of memory, the displayed images are only loaded on demand when the user scrolls the list box. Build and run the example application using Visual Studio.
## Getting the example

To get the example, in the Kanzi Studio Quick Start window, click Projects and select the Examples tab. Next to the Virtual_list_box example, click .

Kanzi Studio downloads the example to the `<KanziWorkspace>/Examples/Virtual_list_box` directory.
## Content of the example

The main parts of the tool project are:

- Prefab template that specifies how to display a single image with a caption.
- List box that specifies where the prefab instances are placed in a scene. The list box has the Object Generator property set to string CustomObjectGenerator, which means that the contents of the list box do not come from the tool project, but instead from the custom object generator that is specified in the example application code.

The application code defines the CustomObjectGenerator, which reads a text file to determine the set of available image files. The list box asks for all visible objects from the object generator, rest of the objects in the list are âvirtualâ. When the list box is scrolled, the visible objects change, and the list box asks for more objects. For each requested object, the object generator starts a background task to load the requested image, instantiates the image prefab, and gives the instantiated object for list box to display.

## Running the example

To run the example:

1.

In Kanzi Studio, select File > Open Kanzi Command Prompt.

The Kanzi Command Prompt opens the Windows Command Prompt with the Kanzi environment variables set for the version of Kanzi for which you open a Kanzi Command Prompt.

Use the Kanzi Command Prompt to access Kanzi utilities and build tools, such as Gradle and CMake, without using absolute paths or setting environment variables.
**Tip:** You can find the Kanzi Command Prompt in the Windows Start Menu in the Rightware directory.
When you have more than one version of Kanzi installed, make sure that you launch a Kanzi Command Prompt for the version of Kanzi with which you want to work in that command prompt.
2.
In the Kanzi Command Prompt in the `<KanziWorkspace>/Examples/Virtual_list_box/Application` directory run the script that generates a Visual Studio solution for the example application.
```
generate_cmake_vs2022_solution.bat
```

This script generates a Visual Studio solution for the application in the directory `<KanziWorkspace>/Examples/Virtual_list_box/Application/build_vs2022`.
3.

In Visual Studio open the `<KanziWorkspace>/Examples/Virtual_list_box/Application/build_vs<Version>/Virtual_list_box`.sln Visual Studio solution.
4.

In Visual Studio in the Solution Explorer right-click the `Virtual_list_box` project and select Set as StartUp Project.
5.

Select the solution configuration that you want to use and run your application.

During development, select the Debug configuration. When you are ready to create a version for production, select the Release configuration.
