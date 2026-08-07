---
title: Using the Multi-Click Manipulator
source: https://docs.kanzi.com/4.1.0/en/working-with/input/multi-click-manipulator.html
---

# Using the Multi-Click Manipulator

Use the Multi-Click Manipulator to enable users to multi-click nodes in your Kanzi application.

See Enabling the multi-click gesture for a node.

You can react to the multi-click gesture using:

- Multi-Click Manipulator triggers in Kanzi Studio. See Using the Multi-Click Manipulator triggers.
- Kanzi Engine API. See Reacting to the multi-click gesture using the Kanzi Engine API.

The Multi-Click Manipulator is one of the input manipulators you can use to add gesture recognition to nodes in your Kanzi application. See Using input manipulators.

To enable the click gesture for nodes, use the Click Manipulator. See Using the Click Manipulator.

Learn how to use the Multi-Click Manipulator by completing a tutorial. See Tutorial: Pan, zoom, tap.
## Enabling the multi-click gesture for a node

This section explains how you can enable the multi-click gesture for any node.

The Text Box nodes support the double-click gesture by default. When you double-click a word in a Text Box node, Kanzi selects that word.

To enable double-click for a Button node, see Enabling the double-click gesture for a Button node.

To enable double-click for List Box items, see Enabling the double-click gesture for List Box items.

To enable the multi-click gesture for a node:

1.

In the Node Tree create a node for which you want to enable the multi-click gesture.

For example, create an Empty Node 2D node, name it MultiClickNode, and add content to the node.
2.

In the Node Tree select the node that you created in the previous step, in the Properties add the Input > Hit Testable property, and set it to enabled.

When you enable this property you enable the user to pick a node.

By default hit testing is enabled for the Button, Toggle Button, List Box Item Container, Scroll View, Slider, and Text Box nodes.

See Defining which node receives input.
3.

In the Node Components press Alt and right-click Input Manipulators, and select Multi-Click Manipulator.

This way you enable the MultiClickNode node to react to the multi-click gesture. By adding a Multi-Click Manipulator component to a node you install a `MultiClickManipulator` to that node.

To control the behavior of the `MultiClickManipulator`, you can add and set these properties in the Multi-Click Manipulator component:

  - Click Count sets the number of click required for the `MultiClickManipulator` to recognize the multi-click gesture.
  - Multi-Click Timeout sets the time in milliseconds within which two consecutive clicks must occur for the `MultiClickManipulator` to recognize them as part of the multi-click gesture. By default if two clicks occur within 250 milliseconds, Kanzi recognizes them as a double-click gesture.
  - Send Intermediate Click Messages sets whether to set off the Intermediate Click trigger at each click that occurs during the multi-click gesture.

Intermediate Click trigger is set off when the user clicks in the node area during the multi-click gesture before the desired click count is reached.

4.

Use the Multi-Click Manipulator triggers to react to the multi-click gesture. For example, you can change the appearance of a node when the user clicks that node multiple times consecutively.

See Using the Multi-Click Manipulator triggers.

## Using the Multi-Click Manipulator triggers

Use the Multi-Click Manipulator triggers to react to the multi-click gesture. For example, you can change the appearance of a node when the user clicks that node multiple times consecutively.

The Multi-Click Manipulator has these triggers:

- Multi-Click trigger is set off when the user clicks multiple times in the node area.
- Multi-Click Canceled trigger is set off when focus moves away from the node during the multi-click gesture.
- Intermediate Click trigger is set off when the user clicks in the node area during the multi-click gesture before the desired click count is reached.

To use the Multi-Click Manipulator triggers:

1.

Enable the multi-click gesture for a node. See Enabling the multi-click gesture for a node.
2.

Define the behavior that you want to set with the Multi-Click Manipulator triggers.

For example, create a state manager where you define the states which set the appearance of a node when the Multi-Click and Multi-Click Canceled triggers are set off. See Creating a state manager.
3.

Add and configure a Multi-Click Manipulator trigger:

  1.

In the Node Tree select the node to which you want to add the trigger, and in the Node Components > Triggers add one of the Multi-Click Manipulator triggers.

For example, in the Node Tree select the node for which you enabled the multi-click gesture, in the Node Components press Alt and right-click Triggers, and select Message Trigger > Multi-Click > Multi-Click.
  2.

In the trigger that you created in the previous step disable the Set Message Handled property.

When you disable the Set Message Handled property, this trigger intercepts the message, but does not stop it. This way you let the input manipulator handle the message.
  3.

In the Node Components press Alt and right-click the trigger that you created, select an action, and configure it.

For example, select Dispatch Message Action > State Manager > Next State, and in the action set:

    - Target Item to the node which uses the state manager you created to set the appearance of a node when the Multi-Click trigger is set off repeatedly
    - State Group to the state group which contains the states between which you want to switch when the Multi-Click trigger is set off

## Reacting to the multi-click gesture using the Kanzi Engine API

You can define in application code how your application reacts to the multi-click gesture.

To react to the multi-click gesture using the Kanzi Engine API:

1.

In Kanzi Studio create a project using the Application template.
2.

Enable the multi-click gesture for a node. See Enabling the multi-click gesture for a node.

When you enable the multi-click gesture for a node in Kanzi Studio, you create in that node a `MultiClickManipulatorComponent`, which installs to the node a `MultiClickManipulator`.
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
**Tip:** You can find the Kanzi Command Prompt in the Windows Start Menu in the Rightware directory.
When you have more than one version of Kanzi installed, make sure that you launch a Kanzi Command Prompt for the version of Kanzi with which you want to work in that command prompt.
6.
In the Kanzi Command Prompt in the `<ProjectName>/Application` directory, run the script that generates a Visual Studio solution for the application.
```
generate_cmake_vs2022_solution.bat
```

This script generates a Visual Studio solution for the application in the directory `<ProjectName>/Application/build_vs2022`.
7.

In Visual Studio open the `<ProjectName>/Application/build_vs<Version>/<ProjectName>.sln` Visual Studio solution and in the file that implements the logic of your application define how to react to the multi-click gesture:

  1.

Define the handlers for the multi-click messages.

For example, after the public section of the class which implements the logic of your application add:

```
private:
    // Define the handler for the MultiClickManipulator::MultiClickMessage message from the
    // nodes that have an input manipulator which generates the multi-click message.
    void onNodeMultiClicked(MultiClickManipulator::MultiClickMessageArguments&)
    {
        // Add the code that handles the multi-click event.
    }

```

  2.

In the `Application::onProjectLoaded` function subscribe to the `MultiClickManipulator` messages.

For example, add:

```
void onProjectLoaded() override
{
    ScreenSharedPtr screen = getScreen();

    // Get the MultiClickNode node using its alias.
    NodeSharedPtr multiClickNode = screen->lookupNode<Node>("#MultiClickNode");

    // Subscribe to the MultiClickManipulator::MultiClickMessage message at the MultiClickNode node.
    // The MultiClickManipulator manipulator generates this message when the user multi-clicks the node.
    multiClickNode->addMessageHandler(MultiClickManipulator::MultiClickMessage, bind(&MyProject::onNodeMultiClicked, this, placeholders::_1));
}

```

8.

Build and run your application. See Deploying Kanzi applications.

In the application click multiple times the node for which you enabled the multi-click gesture. The application executes the behavior that you defined in the handler for the `MultiClickManipulator::MultiClickMessage` message.
