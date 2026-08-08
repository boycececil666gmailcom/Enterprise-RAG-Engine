---
title: Using the Pan Manipulator
source: https://docs.kanzi.com/4.1.0/en/working-with/input/pan-manipulator.html
---

# Using the Pan Manipulator

Use the Pan Manipulator to enable users to move nodes in your Kanzi application.

For example, you can use the Pan Manipulator to enable users to move a map. See Enabling the pan gesture for a node.

Use the Pan Manipulator triggers to react to the pan gesture. For example, you can set the appearance of a node when the user pans that node.

See Using the Pan Manipulator triggers.

The Pan Manipulator is one of the input manipulators that you can use to add gesture recognition to nodes in your Kanzi application.

See Using input manipulators.

Learn how to use the Pan Manipulator by completing a tutorial. See Tutorial: Pan, zoom, tap.
## Enabling the pan gesture for a node

To enable the pan gesture for a node:

1.

In Kanzi Studio create a project using the Application template.
2.

In the Node Tree create a node for which you want to enable the pan gesture.

For example, create an Image node and name it PanNode.
3.

In the Node Tree select the node that you created in the previous step, in the Properties add the Input > Hit Testable property, and set it to enabled.

When you enable this property you enable the user to pick a node.

By default hit testing is enabled for the Button, Toggle Button, List Box Item Container, Scroll View, Slider, and Text Box nodes.

See Defining which node receives input.
4.

In the Node Components press Alt and right-click Input Manipulators, and select Pan Manipulator.

This way you enable the PanNode node to react to the pan gesture.

By adding a Pan Manipulator component to a node you install a `PanManipulator` to that node.

To control the behavior of the `PanManipulator`, you can add and set these properties in the Pan Manipulator component:

  - Recognition Threshold sets the threshold in pixels on the x and y axis that a pointer must move before Kanzi recognizes it as a pan gesture. The default value is 5 pixels on both axes.

To disable the pan gesture on either axis, set the Recognition Threshold property field for that axis to -1.
  - Minimum Touch Points sets the minimum number of touches required on the node area for the installed `PanManipulator` to recognize the pan gesture. The default value is 1.
  - Maximum Touch Points sets the maximum number of touches allowed on the node area for the installed `PanManipulator` to recognize the pan gesture. The default value is 10.

5.

In the Node Tree press Alt and right-click the node that you created and select Alias.

Kanzi Studio creates an alias pointing to the node from which you created the alias and adds it to the resource dictionary of its nearest ancestor node that contains a resource dictionary.

Access alias target nodes using the `#` sign followed by the name of the alias.
6.

Select File > Export > Export KZB.

Kanzi Studio creates the kzb file and configuration files from your Kanzi Studio project. Kanzi Studio stores the exported files in the `<ProjectName>/Application/bin` directory or the location that you set in Project > Properties in the Binary Export Directory property. The kzb file contains all nodes and resources from your Kanzi Studio project, except the resources that you mark in a localization table as locale packs.

When you run your Kanzi application from Visual Studio, your application loads the kzb file and configuration files.
7.

In Kanzi Studio, select File > Open Kanzi Command Prompt.

The Kanzi Command Prompt opens the Windows Command Prompt with the Kanzi environment variables set for the version of Kanzi for which you open a Kanzi Command Prompt.

Use the Kanzi Command Prompt to access Kanzi utilities and build tools, such as Gradle and CMake, without using absolute paths or setting environment variables.
**Tip:** You can find the Kanzi Command Prompt in the Windows Start Menu in the Rightware directory.
When you have more than one version of Kanzi installed, make sure that you launch a Kanzi Command Prompt for the version of Kanzi with which you want to work in that command prompt.
8.
In the Kanzi Command Prompt in the `<ProjectName>/Application` directory, run the script that generates a Visual Studio solution for the application.
```
generate_cmake_vs2022_solution.bat
```

This script generates a Visual Studio solution for the application in the directory `<ProjectName>/Application/build_vs2022`.
9.

In Visual Studio open the `<ProjectName>/Application/build_vs<Version>/<ProjectName>.sln` Visual Studio solution and in the file that implements the logic of your application define how to react to the pan gesture:

  1.

Define the handlers for the pan messages.

For example, after the public section of the class which implements the logic of your application add:

```
private:
    // Define the handler for the PanManipulator::StartedMessage message from 2D nodes
    // that have an input manipulator which generates pan messages.
    // This handler prepares a 2D node for a pan gesture.
    void onPanStarted(PanManipulator::StartedMessageArguments& messageArguments)
    {
        // Get from the message arguments the node that the user pans.
        Node2DSharedPtr node2d = dynamic_pointer_cast<Node2D>(messageArguments.getSource());

        if (!node2d)
        {
            return;
        }

        // When starting a pan gesture on the node, bring the node to front.
        node2d->moveToFront();
    }

    // Define the handler for the PanManipulator::MovedMessage message from 2D nodes
    // that have an input manipulator which generates pan messages.
    // This handler translates a 2D node by the amount of the pan gesture.
    void onPanMoved(PanManipulator::MovedMessageArguments& messageArguments)
    {
        // Get from the message arguments the node that the user pans.
        Node2DSharedPtr node2d = dynamic_pointer_cast<Node2D>(messageArguments.getSource());

        if (!node2d)
        {
            return;
        }

        // Get the distance in pixels that the pan has progressed
        // since the last message in the pan gesture sequence.
        Vector2 translationDelta = messageArguments.getDelta();

        // Get the Render Transformation property of the node.
        SRTValue2D nodeTransform = node2d->getRenderTransformation();

        // Get the current translation of the node.
        Vector2 translation = nodeTransform.getTranslation();

        // Apply the translation from the pan message.
        Vector2 translationTarget = translation + translationDelta;

        // Set the new translation.
        nodeTransform.setTranslation(translationTarget);

        // Apply the new transform to the node.
        node2d->setRenderTransformation(nodeTransform);
    }

```

  2.

In the `Application::onProjectLoaded` function subscribe to the `PanManipulator` messages.

For example, add:

```
void onProjectLoaded() override
{
    ScreenSharedPtr screen = getScreen();

    // Get the PanNode node using its alias.
    NodeSharedPtr panNode = screen->lookupNode<Node>("#PanNode");

    // Subscribe to the PanManipulator::StartedMessage message at the PanNode node.
    // The PanManipulator generates this message when the user starts to drag a finger on the attached node and
    // the pan recognizition treshold is exceeded.
    panNode->addMessageHandler(PanManipulator::StartedMessage, bind(&MyProject::onPanStarted, this, placeholders::_1));

    // Subscribe to the PanManipulator::MovedMessage message at the PanNode node.
    // The PanManipulator generates this message when the user continues to drag a finger on the attached node.
    panNode->addMessageHandler(PanManipulator::MovedMessage, bind(&MyProject::onPanMoved, this, placeholders::_1));
}

```

10.

Build and run your application. See Deploying Kanzi applications.

In the application click and drag the node for which you enabled the pan gesture.

## Using the Pan Manipulator triggers

Use the Pan Manipulator triggers to react to the pan gesture. For example, you can set the appearance of a node when the user pans that node.

The Pan Manipulator has these triggers:

- Pan Started trigger is set off when the user clicks a node but does not yet drag that node.
- Pan Moved trigger is set off when the user moves a node with the pan gesture.
- Pan Finished trigger is set off when the user ends the pan gesture by releasing the mouse button.
- Pan Canceled trigger is set off when focus moves away from the node during the pan gesture.
- Pan Entered trigger is set off when the pan gesture enters the node.
- Pan Left trigger is set off when the pan gesture leaves the node.

To use the Pan Manipulator triggers:

1.

Enable the pan gesture for a node. See Enabling the pan gesture for a node.
2.

Define the behavior that you want to set with the Pan Manipulator triggers.

For example, create a state manager where you define the states which set the appearance of a node when the Pan Started, Pan Moved, and Pan Finished triggers are set off. See Creating a state manager.
3.

Add and configure a Pan Manipulator trigger:

  1.

In the Node Tree select the node to which you want to add the trigger, and in the Node Components > Triggers add one of the Pan Manipulator triggers.

For example, in the Node Tree select the node for which you enabled the pan gesture, in the Node Components press Alt and right-click Triggers, and select Message Trigger > Pan > Pan Started.
  2.

In the trigger that you created in the previous step disable the Set Message Handled property.

When you disable the Set Message Handled property, this trigger intercepts the message, but does not stop it. This way you let the input manipulator handle the message.
  3.

In the Node Components press Alt and right-click the trigger that you created, select an action, and configure it.

For example, select Dispatch Message Action > State Manager > Go to State, and in the action set:

    - Target Item to the node for which you enabled the pan gesture
    - State to the state which sets the appearance of the node when the Pan Started trigger is set off

4.

Repeat the previous step to add and configure additional Pan Manipulator triggers.

For example, add the Pan Moved and Pan Finished triggers.

In the Go to State action of each trigger set State to the state which sets the appearance of the node when that trigger is set off.
5.

Select File > Export > Export KZB.
6.

Build and run your application. See Deploying Kanzi applications.

In the application click and drag the node for which you enabled the pan gesture.
