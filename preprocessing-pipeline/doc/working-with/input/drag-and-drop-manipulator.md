---
title: Using the Drag-And-Drop Manipulator
source: https://docs.kanzi.com/4.1.0/en/working-with/input/drag-and-drop-manipulator.html
---

# Using the Drag-And-Drop Manipulator

Use the Drag-And-Drop Manipulator to enable users to drag and drop nodes in your Kanzi application.

See Enabling the drag-and-drop gesture for a node.

Use the Drag-And-Drop Manipulator triggers to react to the drag-and-drop gesture. For example, you can set the appearance of a node when the user drags and drops that node.

See Using the Drag-And-Drop Manipulator triggers.

The Drag-And-Drop Manipulator is one of the input manipulators you can use to add gesture recognition to nodes in your Kanzi application. See Using input manipulators.

Learn how to use the Drag-And-Drop Manipulator by completing a tutorial. See Tutorial: Drag and drop.
## Enabling the drag-and-drop gesture for a node

To enable the drag-and-drop gesture for a node:

1.

In Kanzi Studio create a project using the Application template.
2.

In the Node Tree create a node for which you want to enable the drag-and-drop gesture.

For example, create an Empty Node 2D node and name it DragAndDropNode.
3.

In the Node Tree select the node that you created in the previous step, in the Properties add the Input > Hit Testable property, and set it to enabled.

When you enable this property you enable the user to pick a node.

By default hit testing is enabled for the Button, Toggle Button, List Box Item Container, Scroll View, Slider, and Text Box nodes.

See Defining which node receives input.
4.

In the Node Tree press Alt and right-click the node that you created and select Alias.

Kanzi Studio creates an alias pointing to the node from which you created the alias and adds it to the resource dictionary of its nearest ancestor node that contains a resource dictionary.

Access alias target nodes using the `#` sign followed by the name of the alias.
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
In the Kanzi Command Prompt in the `<ProjectName>/Application` directory, run the script that generates a Visual Studio solution for the application.
```
generate_cmake_vs2022_solution.bat
```

This script generates a Visual Studio solution for the application in the directory `<ProjectName>/Application/build_vs2022`.
8.

In Visual Studio open the `<ProjectName>/Application/build_vs<Version>/<ProjectName>.sln` Visual Studio solution and in the file that implements the logic of your application create and configure the `DragAndDropManipulator`:

  1.

Define the handlers for the drag-and-drop messages.

For example, after the public section of the class which implements the logic of your application add:

```
private:
    // Define the handler for the DragAndDropManipulator::StartedMessage message from 2D nodes
    // that have an input manipulator which generates drag-and-drop messages.
    // This prepares the 2D node for dragging.
    void onDragStarted(DragAndDropManipulator::StartedMessageArguments& messageArguments)
    {
        // Get from the message arguments the node that the user drags.
        Node2DSharedPtr dragAndDropNode = dynamic_pointer_cast<Node2D>(messageArguments.getSource());

        if (!dragAndDropNode)
        {
            return;
        }

        // Save the point from which the user started dragging the node,
        // relative to the origin (by default the top left corner) of the node.
        m_dragGrabOffset = messageArguments.getPoint();

        // When starting a drag-and-drop gesture on the node, bring the node to front.
        dragAndDropNode->moveToFront();
    }

    // Define the handler for the DragAndDropManipulator::MovedMessage message from 2D nodes
    // that have an input manipulator which generates drag-and-drop messages.
    // This translates (moves) the node by the distance the user drags it.
    void onDragMoved(DragAndDropManipulator::MovedMessageArguments& messageArguments)
    {
        // Get from the message arguments the node that the user drags.
        Node2DSharedPtr dragAndDropNode = dynamic_pointer_cast<Node2D>(messageArguments.getSource());

        if (!dragAndDropNode)
        {
            return;
        }

        // Move the node by traveled distance given by getPoint, relative to the origin of the node.
        // To keep dragging from the same point on the node, subtract the grab offset.
        SRTValue2D transform = dragAndDropNode->getLayoutTransformation();
        transform.translate(messageArguments.getPoint() - m_dragGrabOffset);
        dragAndDropNode->setLayoutTransformation(transform);
    }

    // Offset from the top left corner of the DragAndDropNode where the user pressed down or clicked on it.
    Vector2 m_dragGrabOffset;

```

  2.

In the `Application::onProjectLoaded` function create a `DragAndDropManipulator` and subscribe to its messages.

For example, add:

```
void onProjectLoaded() override
{
    ScreenSharedPtr screen = getScreen();
    Domain* domain = getDomain();

    // Get the DragAndDropNode using its alias.
    NodeSharedPtr dragAndDropNode = screen->lookupNode<Node>("#DragAndDropNode");

    // Create an input manipulator that generates drag-and-drop messages.
    DragAndDropManipulatorSharedPtr nodeDragAndDropManipulator = DragAndDropManipulator::create(domain);

    // Add the input manipulator to the DragAndDropNode.
    dragAndDropNode->addInputManipulator(nodeDragAndDropManipulator);

    // Set the duration of the long press before the drag-and-drop starts to 200 ms. The default is 500 ms.
    // This is the amount of time the user has to press the node before they can start dragging it.
    nodeDragAndDropManipulator->setPressDuration(chrono::milliseconds(200));

    // Subscribe to the DragAndDropManipulator::StartedMessage message at the DragAndDropNode node.
    // The DragAndDropManipulator generates this message when the user has pressed the node
    // for the duration set by DragAndDropManipulator::setPressDuration.
    dragAndDropNode->addMessageHandler(DragAndDropManipulator::StartedMessage, bind(&MyProject::onDragStarted, this, placeholders::_1));

    // Subscribe to the DragAndDropManipulator::MovedMessage message at the DragAndDropNode node.
    // The DragAndDropManipulator generates this message when the finger or mouse moves.
    dragAndDropNode->addMessageHandler(DragAndDropManipulator::MovedMessage, bind(&MyProject::onDragMoved, this, placeholders::_1));
}

```

9.

Build and run your application. See Deploying Kanzi applications.

In the application long-press and drag the node for which you enabled the drag-and-drop gesture.

## Using the Drag-And-Drop Manipulator triggers

Use the Drag-And-Drop Manipulator triggers to react to the drag-and-drop gesture. For example, you can set the appearance of a node when the user drags and drops that node.

The Drag-And-Drop Manipulator has these triggers:

- Drag and Drop Started trigger is set off when the user presses the node long enough for the input manipulator to recognize the drag-and-drop gesture.
- Drag and Drop Moved trigger is set off when the user drags the node with the drag-and-drop gesture.
- Drag and Drop Finished trigger is set off when the user ends the drag-and-drop gesture by lifting their finger or releasing the mouse button.
- Drag and Drop Canceled trigger is set off when focus moves away from the node during the drag-and-drop gesture.

To use the Drag-And-Drop Manipulator triggers:

1.

Enable the drag-and-drop gesture for a node. See Enabling the drag-and-drop gesture for a node.
2.

Define the behavior that you want to set with the Drag-And-Drop Manipulator triggers. For example, create a state manager where you define the states which set the appearance of a node when the Drag and Drop Started, Drag and Drop Moved, Drag and Drop Finished, and Drag and Drop Canceled triggers are set off. See Creating a state manager.
3.

Add and configure a Drag-And-Drop Manipulator trigger:

  1.

In the Node Tree select the node to which you want to add the trigger, and in the Node Components > Triggers add one of the Drag-And-Drop Manipulator triggers.

For example, in the Node Tree select the node for which you enabled the drag-and-drop gesture, in the Node Components press Alt and right-click Triggers, and select Message Trigger > Drag and Drop > Drag and Drop Started.
  2.

In the trigger that you created in the previous step disable the Set Message Handled property.

When you disable the Set Message Handled property, this trigger intercepts the message, but does not stop it. This way you let the input manipulator handle the message.
  3.

In the Node Components press Alt and right-click the trigger that you created, select an action, and configure it.

For example, select Dispatch Message Action > State Manager > Go to State, and in the action set:

    - Target Item to the node for which you enabled the drag-and-drop gesture
    - State to the state which sets the appearance of the node when the Drag and Drop Started trigger is set off

4.

Repeat the previous step to add and configure more Drag-And-Drop Manipulator triggers.

For example, add the Drag and Drop Moved and Drag and Drop Finished triggers.

In the Go to State action of each trigger set State to the state which sets the appearance of the node when that trigger is set off.
5.

Select File > Export > Export KZB.
6.

Build and run your application. See Deploying Kanzi applications.

In the application long-press and drag the node for which you enabled the drag-and-drop gesture.
