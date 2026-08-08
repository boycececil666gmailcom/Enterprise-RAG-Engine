---
title: Layout example
source: https://docs.kanzi.com/4.1.0/en/examples/layout/layout.html
---

# Layout example

This example shows how to dynamically create a contact list using the Kanzi Engine API. The layout and prefabs that set the structure of the contact items are defined in the Kanzi Studio project. The project uses the Kanzi Engine API to instantiate the prefabs. Build and run the example application using Visual Studio.
## Getting the example

To get the example, in the Kanzi Studio Quick Start window, click Projects and select the Examples tab. Next to the Layout example, click .

Kanzi Studio downloads the example to the `<KanziWorkspace>/Examples/Layout` directory.
## Content of the example

In the Kanzi Studio project:

- gridLayout node arranges the contact items.
- contactCard prefab defines the structure for each contact item.

## Running the example

To run the example:

1.

In Kanzi Studio, select File > Open Kanzi Command Prompt.

The Kanzi Command Prompt opens the Windows Command Prompt with the Kanzi environment variables set for the version of Kanzi for which you open a Kanzi Command Prompt.

Use the Kanzi Command Prompt to access Kanzi utilities and build tools, such as Gradle and CMake, without using absolute paths or setting environment variables.
**Tip:** You can find the Kanzi Command Prompt in the Windows Start Menu in the Rightware directory.
When you have more than one version of Kanzi installed, make sure that you launch a Kanzi Command Prompt for the version of Kanzi with which you want to work in that command prompt.
2.
In the Kanzi Command Prompt in the `<KanziWorkspace>/Examples/Layout/Application` directory run the script that generates a Visual Studio solution for the example application.
```
generate_cmake_vs2022_solution.bat
```

This script generates a Visual Studio solution for the application in the directory `<KanziWorkspace>/Examples/Layout/Application/build_vs2022`.
3.

In Visual Studio open the `<KanziWorkspace>/Examples/Layout/Application/build_vs<Version>/Layout.sln` Visual Studio solution.
4.

In Visual Studio in the Solution Explorer right-click the `Layout` project and select Set as StartUp Project.
5.

Select the solution configuration that you want to use and run your application.

During development, select the Debug configuration. When you are ready to create a version for production, select the Release configuration.
