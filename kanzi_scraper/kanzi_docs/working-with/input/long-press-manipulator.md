---
title: Using the Long-Press Manipulator
source: https://docs.kanzi.com/4.1.0/en/working-with/input/long-press-manipulator.html
---

# Using the Long-Press Manipulator


Use the Long-Press Manipulator to enable users to long-press nodes in your Kanzi application.

This way you can make the application react when the user presses and holds the pointer pressed on a node for the amount of time that you set in the Long-Press Manipulator.

For example, use the Long-Press Manipulator to open a context menu. See Enabling the long-press gesture for a node.

You can react to the long-press gesture using:

- Long-Press Manipulator triggers in Kanzi Studio. See Using the Long-Press Manipulator triggers.
- Kanzi Engine API. See Reacting to the long-press gesture using the Kanzi Engine API.


The Long-Press Manipulator is one of the input manipulators you can use to add gesture recognition to nodes in your Kanzi application. See Using input manipulators.

Learn how to use the Long-Press Manipulator by completing a tutorial. See Tutorial: Pan, zoom, tap.
## Enabling the long-press gesture for a node


This section explains how you can enable the long-press gesture for any node. To enable long press for a Button node, see Using the Button triggers.

To enable the long-press gesture for a node:

1.

In the Node Tree create a node for which you want to enable the long-press gesture.

For example, create an Empty Node 2D node, name it LongPressNode, and add content to the node.
2.

In the Node Tree select the node that you created in the previous step, in the Properties add the Input > Hit Testable property, and set it to enabled.

When you enable this property you enable the user to pick a node.

By default hit testing is enabled for the Button, Toggle Button, List Box Item Container, Scroll View, Slider, and Text Box nodes.

See Defining which node receives input.
3.

In the Node Components press Alt and right-click Input Manipulators, and select Long-Press Manipulator.

This way you enable the LongPressNode node to react to the long-press gesture. By adding a Long-Press Manipulator component to a node you install a `LongPressManipulator` to that node.

In the Long-Press Manipulator component use the Long Press Duration property to set the amount of time in milliseconds that the user must press the node for the `LongPressManipulator` to recognize a long-press gesture.
4.

Use the Long-Press Manipulator triggers to react to the long-press gesture. For example, you can change the appearance of a node when the user clicks and holds the click on that node for the amount of time set in that trigger.

See Using the Long-Press Manipulator triggers.

## Using the Long-Press Manipulator triggers


Use the Long-Press Manipulator triggers to react to the long-press gesture. For example, you can change the appearance of a node when the user clicks and holds the click on that node for the amount of time set in that trigger.

The Long-Press Manipulator has these triggers:

- Long Press trigger is set off when the user presses down in the node area and holds the node pressed for 500 milliseconds or the amount of milliseconds set by the Long Press Duration property of the Long-Press Manipulator in that node.
- Long Press Cancel trigger is set off when focus moves away from the node during the long-press gesture.


To use the Long-Press Manipulator triggers:

1.

Enable the long-press gesture for a node. See Enabling the long-press gesture for a node.
2.

Define the behavior that you want to set with the Long-Press Manipulator triggers.

For example, create a state manager where you define the states which set the appearance of a node when the Long Press and Long Press Cancel triggers are set off. See Creating a state manager.
3.

Add and configure a Long-Press Manipulator trigger:

  1.

In the Node Tree select the node to which you want to add the trigger, and in the Node Components > Triggers add one of the Long-Press Manipulator triggers.

For example, in the Node Tree select the node for which you enabled the long-press gesture, in the Node Components press Alt and right-click Triggers, and select Message Trigger > Long Press > Long Press.
  2.

In the trigger that you created in the previous step disable the Set Message Handled property.

When you disable the Set Message Handled property, this trigger intercepts the message, but does not stop it. This way you let the input manipulator handle the message.
  3.

In the Node Components press Alt and right-click the trigger that you created, select an action, and configure it.

For example, select Dispatch Message Action > State Manager > Next State, and in the action set:

    - Target Item to the node which uses the state manager you created to set the appearance of a node when the Long Press trigger is set off repeatedly
    - State Group to the state group which contains the states between which you want to switch when the Long Press trigger is set off


## Reacting to the long-press gesture using the Kanzi Engine API


You can define in application code how your application reacts to the long-press gesture.

To react to the long-press gesture using the Kanzi Engine API:

1.

In Kanzi Studio create a project using the Application template.
2.

Enable the long-press gesture for a node. See Enabling the long-press gesture for a node.

When you enable the long-press gesture for a node in Kanzi Studio, you create in that node a `LongPressManipulatorComponent`, which installs to the node a `LongPressManipulator`.
3.

In the Node Tree press Alt and right-click the node that you created and select Alias.

Kanzi Studio creates an alias pointing to the node from which you created the alias and adds it to the resource dictionary of its nearest ancestor node that contains a resource dictionary.

Access alias target nodes using the `#` sign followed by the name of the alias.
4.

Select File > Export > Export KZB.

Kanzi Studio creates the kzb file and configuration files from your Kanzi Studio project. Kanzi Studio stores the exported files in the `<ProjectName>/Application/bin` directory or the location that you set in Project > Properties in the Binary Export Directory property. The kzb file contains all nodes and resources from your Kanzi Studio project, except the resources that you mark in a localization table as locale packs.

When you run your Kanzi application from Visual Studio, your application loads the kzb file and configuration files.
5.

In Kanzi Studio, select File > Open Kanzi Command Prompt.

The Kanzi Command Prompt opens the Windows Command Prompt with the Kanzi environment variables set for the version of Kanzi for which you open a Kanzi Command Prompt.

Use the Kanzi Command Prompt to access Kanzi utilities and build tools, such as Gradle and CMake, without using absolute paths or setting environment variables.

> **Tip:** You can find the Kanzi Command Prompt in the Windows Start Menu in the Rightware directory.
>
> When you have more than one version of Kanzi installed, make sure that you launch a Kanzi Command Prompt for the version of Kanzi with which you want to work in that command prompt.
> 6.
>
> In the Kanzi Command Prompt in the `<ProjectName>/Application` directory, run the script that generates a Visual Studio solution for the application.
>
> ```
> generate_cmake_vs2022_solution.bat
>
> ```


This script generates a Visual Studio solution for the application in the directory `<ProjectName>/Application/build_vs2022`.
7.

In Visual Studio open the `<ProjectName>/Application/build_vs<Version>/<ProjectName>.sln` Visual Studio solution and in the file that implements the logic of your application define how to react to the long-press gesture:

  1.

Define the handlers for the long-press messages.

For example, after the public section of the class which implements the logic of your application add:

```
private:
    // Define the handler for the LongPressManipulator::LongPressMessage message from the nodes
    // that have an input manipulator which generates the long-press message.
    void onLongPress(LongPressManipulator::LongPressMessageArguments&)
    {
        // Add the code that handles the long-press event.
    }

```

  2.

In the `Application::onProjectLoaded` function subscribe to the `LongPressManipulator` messages.

For example, add:

```
void onProjectLoaded() override
{
    ScreenSharedPtr screen = getScreen();

    // Get the LongPressNode node using its alias.
    NodeSharedPtr longPressNode = screen->lookupNode<Node>("#LongPressNode");

    // Subscribe to the LongPressManipulator::LongPressMessage message at the LongPressNode node.
    // The LongPressManipulator manipulator generates this message when the user presses the node
    // for the amount of milliseconds you set with the LongPressManipulator::setPressDuration function.
    longPressNode->addMessageHandler(LongPressManipulator::LongPressMessage, bind(&MyProject::onLongPress, this, placeholders::_1));
}

```


8.

Build and run your application. See Deploying Kanzi applications.

In the application press the node for which you enabled the long-press gesture. The application executes the behavior you defined in the handler for the `LongPressManipulator::LongPressMessage` message.
