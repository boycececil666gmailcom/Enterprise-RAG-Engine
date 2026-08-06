---
title: Programming Activities with C++ Code Behind
source: https://docs.kanzi.com/4.1.0/en/working-with/activities/cpp-code-behind.html
---

# Programming Activities with C++ Code Behind


Learn how to program Activities with the C++ Code Behind workflow by completing the Tutorial: Program Activities with C++ Code Behind.

Before you can program Activities with the C++ Code Behind, make sure that you have your Kanzi development environment set up. For developing application logic with Kanzi Engine API, you need:

- CMake 3.25 or newer
- Visual Studio 2022 with the latest updates


To program Activities with C++ Code Behind:

1.

In the Activity Browser create an Activity or Activity Host that you want to program.

For example, create a root Exclusive Activity Host with several Activities.
2.

In the Activity Browser right-click an Activity or Activity Host and select Add Code Behind. If your application is based on a Kanzi Android framework (droidfw) template, select Add Code Behind > C++.

When you add C++ Code Behind to an Activity node, Kanzi Studio:

  1.

Copies the C++ Code Behind template from the `<KanziWorkspace>/Templates/Code_behind_template`.
  2.

In the `<ProjectName>/Tool_project/CodeBehind` directory creates a Visual Studio solution and project for the Activity to which you added C++ Code Behind.
  3.

Compiles the project for the Preview build configuration and Visual Studio version that you set in the project properties.
  4.

Imports to the Kanzi Studio project the DLL file that contains the functionality defined in the C++ Code Behind Visual Studio project as a Kanzi Engine plugin.
  5.

Restarts the Preview.

When the Preview starts, in the Activity Browser the Activities with C++ Code Behind contain the  icon and the side panel shows the commands that are defined in the C++ Code Behind.

3.

In the Activity Browser right-click the Activity to which you added C++ Code Behind and select Open Code Behind. If your application is based on a Kanzi Android framework (droidfw) template, select Open Code Behind > C++.

Kanzi Studio opens in Visual Studio the Visual Studio solution that contains the C++ Code Behind.

The Visual Studio solution for the C++ Code Behind functionality is stored in the directory `<ProjectName>/CodeBehind/build_vs2022`.
4.

In Visual Studio in the `<ActivityNodeName>_activity_code.cpp` file add the initialization functionality for that Activity node in the `NodeComponent::attachOverride` function and save the file. In the `NodeComponent::attachOverride` function you can install message handlers, property listeners, create nodes, setup the look and functionality of the activity, and so on.

This way you provide unique functionality to that Activity node so that you can react to status changes through code.
5.

Use the C++ Code Behind in your project:

  1.

In the Prefabs in the prefab that you use for the activity to which you added C++ Code Behind, create a Button, List Box, or create a List Box Item Container prefab.

For example, create a Button 2D node.
  2.

In the Properties add the Command property and set it to the command that you created in the `<ActivityNodeName>_activity_code.cpp` file.

When you activate the Activity with the Button 2D node that you created earlier, and in the Preview click that button, the Log window shows the default message of the MyFirstCommand.


## Using C++ Code Behind in the API


For details, see the `CodeBehind` class.
