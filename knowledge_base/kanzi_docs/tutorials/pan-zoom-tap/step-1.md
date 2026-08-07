---
title: Step 1 - Pan the map
source: https://docs.kanzi.com/4.1.0/en/tutorials/pan-zoom-tap/step-1.html
---

# Step 1 - Pan the map

Use the Pan Manipulator to enable users to move nodes in your Kanzi application.

The Pan Manipulator is one of the input manipulators that you can use to add gesture recognition to nodes in your Kanzi application.

The pan gesture tracks the position of the pointer that moves on the device screen to calculate the amount by which to move a node.

In Kanzi Studio you can use the Pan Manipulator component to install a pan manipulator to a node, and to control the behavior of that pan manipulator.

In this step of the tutorial you use the Pan Manipulator component and pan manipulator to enable moving the map.
## Get the tutorial

To get the tutorial, in the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Pan zoom tap tutorial, click .

Kanzi Studio downloads the tutorial to the `<KanziWorkspace>/Tutorials` directory. You can find:

- The tutorial starting point project in the `<KanziWorkspace>/Tutorials/Pan zoom tap/Start/Tool_project` directory.
- The completed tutorial in the `<KanziWorkspace>/Tutorials/Pan zoom tap/Completed` directory.

## Content of the starting point project

The starting point project contains the content that you need to complete this tutorial:

- The Map node contains an image of a map.

The Map node is aligned to the center of its parent node and the Render Transformation Origin property of the Map node is set to the center of the Map node. When you rotate a node, it rotates around its origin.
- The resource dictionary of the Screen node contains an alias that points to the Map node.

This alias provides a convenient way to access the Map node using the Kanzi Engine API.
- The Pin prefab contains an image of a pin icon.

The Render Transformation Origin property is set so that when you rotate the pin icon, it rotates around its tip.

## Pan the map

In this section you create and use the Pan Manipulator component and a pan manipulator to move the map when the user puts the pointer down on the map and moves the pointer.

To pan the map:

1.

In the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Pan zoom tap tutorial, click Open and select Start project.
2.

In the Node Tree select the Map node, in the Properties add the Input > Hit Testable property, and enable it.

When you enable this property you enable the user to pick a node.
3.

In the Node Components press Alt and right-click Input Manipulators, and select Pan Manipulator.

This way you enable the Map node to react to the pan gesture.

By adding a Pan Manipulator component to a node you install a `PanManipulator` to that node.

Later in this procedure you add application code that defines how to react to the pan gesture.
4.

In the Pan Manipulator set the Recognition Threshold property X and Y property fields to 10.

Recognition Threshold sets the threshold in pixels on the horizontal and vertical axis that a pointer must move before Kanzi recognizes it as a pan gesture.
5.

Select File > Export > Export KZB.

Kanzi Studio creates the kzb file and configuration files from your Kanzi Studio project. Kanzi Studio stores the exported files in the `<ProjectName>/Application/bin` directory or the location that you set in Project > Properties in the Binary Export Directory property. The kzb file contains all nodes and resources from your Kanzi Studio project, except the resources that you mark in a localization table as locale packs.

When you run your Kanzi application from Visual Studio, your application loads the kzb file and configuration files.
6.

In Kanzi Studio, select File > Open Kanzi Command Prompt.

The Kanzi Command Prompt opens the Windows Command Prompt with the Kanzi environment variables set for the version of Kanzi for which you open a Kanzi Command Prompt.

Use the Kanzi Command Prompt to access Kanzi utilities and build tools, such as Gradle and CMake, without using absolute paths or setting environment variables.
**Tip:** You can find the Kanzi Command Prompt in the Windows Start Menu in the Rightware directory.
When you have more than one version of Kanzi installed, make sure that you launch a Kanzi Command Prompt for the version of Kanzi with which you want to work in that command prompt.
7.
In the Kanzi Command Prompt in the `<KanziWorkspace>/Tutorials/Pan zoom tap/Start/Application` directory run the script that generates a Visual Studio solution for the tutorial application.
```
generate_cmake_vs2022_solution.bat
```

This script generates a Visual Studio solution for the application in the directory `<KanziWorkspace>/Tutorials/Pan zoom tap/Start/Application/build_vs2022`.
8.

In Visual Studio open the `<KanziWorkspace>/Tutorials/Pan zoom tap/Start/Application/build_vs<Version>/Pan_zoom_tap_start.sln` Visual Studio solution.
9.

In Visual Studio in the Solution Explorer right-click the Pan_zoom_tap_start project and select Set as StartUp Project.
10.

In Visual Studio open the `pan_zoom_tap.cpp` file and add the code that defines how your application reacts to the pan gesture:

  1.

In the `PanZoomTap` class, after the public section, define the handler for the `PanManipulator::MovedMessage` message:

```
private:

    // Define the handler for the PanManipulator::MovedMessage message from 2D nodes
    // that have an input manipulator which generates pan messages.
    // This handler translates a 2D node for the amount of the pan gesture.
    void onPanMoved(PanManipulator::MovedMessageArguments& messageArguments)
    {
        // Get from the message arguments the node that the user pans.
        Node2DSharedPtr mapNode = dynamic_pointer_cast<Node2D>(messageArguments.getSource());

        // Get the distance in pixels for which the pan progressed
        // since the last message in the pan gesture sequence.
        Vector2 translationDelta = messageArguments.getDelta();

        // Get the Render Transformation property of the Map node.
        SRTValue2D mapNodeSRT = mapNode->getRenderTransformation();

        // Get the current translation of the Map node.
        Vector2 translation = mapNodeSRT.getTranslation();

        // Apply the translation from the pan message.
        Vector2 translationTarget = translation + translationDelta;

        // Get the parent node of the Map node.
        Node2D* containerNode = dynamic_cast<Node2D*>(mapNode->getParent());

        // Get the size of the parent node.
        Vector2 containerSize = containerNode->getActualSize();

        // Get the Render Transformation property Scale property field of the Map node.
        Vector2 mapScale = mapNodeSRT.getScale();

        // Calculate the scaled size of the Map node.
        Vector2 mapSizeScaled = componentWiseMultiply(mapNode->getActualSize(), mapScale);

        // Do not pan outside the boundaries of the Map node.
        // When calculating the boundaries, take into account the current scale of the map.
        if (mapScale.getX() >= 1.0f)
        {
            translationTarget = componentWiseMax(componentWiseMin(translationTarget, (mapSizeScaled - containerSize) / 2), (containerSize - mapSizeScaled) / 2);
        }
        else if (mapScale.getX() < 1.0f)
        {
            translationTarget = componentWiseMin(componentWiseMax(translationTarget, (containerSize - mapSizeScaled) / 2), (mapSizeScaled - containerSize) / 2);
        }

        // Set the new translation.
        mapNodeSRT.setTranslation(translationTarget);

        // Apply the new transform to the Map node.
        mapNode->setRenderTransformation(mapNodeSRT);
    }

```

  2.

In the `Application::onProjectLoaded` function subscribe to the messages of the `PanManipulator` manipulator at the Map node:

```
void onProjectLoaded() override
{
    // Pointer to the domain.
    Domain* domain = getDomain();

    // Get the Screen node.
    ScreenSharedPtr screen = getScreen();

    // Get the Map node using its alias.
    Node2DSharedPtr mapNode = screen->lookupNode<Node2D>("#Map");

    // Subscribe to the PanManipulator::MovedMessage message at the Map node.
    // The PanManipulator generates this message when the user moves the pointer on the horizontal or
    // vertical axis more than the recognition threshold and when the pointer moves between updates.
    mapNode->addMessageHandler(PanManipulator::MovedMessage, bind(&PanZoomTap::onPanMoved, this, placeholders::_1));
}

```

11.

Select the solution configuration that you want to use and run your application.

During development, select the Debug configuration. When you are ready to create a version for production, select the Release configuration.

In the application click and drag the map to pan it.

Introduction Next step
