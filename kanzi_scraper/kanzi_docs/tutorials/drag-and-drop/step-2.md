---
title: Step 2 - Implement the drag and drop functionality
source: https://docs.kanzi.com/4.1.0/en/tutorials/drag-and-drop/step-2.html
---

# Step 2 - Implement the drag and drop functionality


In this step you implement the drag and drop functionality.
## Create the drag functionality


In this section you first use the Kanzi Engine API to instantiate the Drag Item prefab template that you created in the previous step of the tutorial. Then you define the behavior when the user starts the drag-and-drop gesture and drags a button. Finally, you create and configure a drag-and-drop manipulator for each button in the navigation bar.

To create the drag functionality:

1.

In Visual Studio in the `drag_and_drop.cpp` file in the `Application::onProjectLoaded` function instantiate the Drag Item prefab that you use to visualize the button that the user is dragging:

```
    void onProjectLoaded() override
    {
        ...

        // Get the reference to the Drag Item prefab.
        ResourceManager* resourceManager = getDomain()->getResourceManager();
        PrefabTemplateSharedPtr dragItemPrefab = resourceManager->acquireResource<PrefabTemplate>("kzb://drag_and_drop/Prefabs/Drag Item");

        // Instantiate the Drag Item prefab.
        m_dragItem = dragItemPrefab->instantiate<Node2D>("Drag Item");

        // Get the RootPage node using its alias.
        Node2DSharedPtr rootPage = screen->lookupNode<Node2D>("#RootPage");

        // Add to the RootPage node the instance of the Drag Item prefab that you created.
        rootPage->addChild(m_dragItem);

        // Disable the Visible property of the Drag Item prefab instance.
        // You hide the Drag Item when the user is not dragging it.
        m_dragItem->setVisible(false);
    }

private:
    ...

    // Define a member variable for the instantiated Drag Item.
    Node2DSharedPtr m_dragItem;

```

2.

In the private section of the `DragAndDrop` class create a function which moves the Drag Item prefab instance:

```
private:

    ...

    // Update the position of the Drag Item.
    void updateDragAndDrop(Vector2 dragPosition, Matrix3x3 dragWorldTransform)
    {
        // Calculate the local drag anchor that is the top-left corner of the button that the user is dragging.
        Vector2 localDragAnchor = dragPosition - m_dragGrabOffset;

        // Restrict the movement of the Drag Item to the x axis.
        localDragAnchor.setY(0.0f);

        // Calculate the global drag anchor.
        Vector2 globalDragAnchor = dragWorldTransform * localDragAnchor;

        // The structure that you use to describe the Render Transformation property of the Drag Item.
        SRTValue2D transform;
        // Set the Render Transformation property Translation property field to the global drag anchor.
        transform.setTranslation(globalDragAnchor);

        // Move the Drag Item for the amount of the dragged distance.
        m_dragItem->setRenderTransformation(transform);

        // Set the icons of the buttons.
        updateItems();
    }

    ...

    // Define a member variable for the offset from the top-left corner of the button where the user pressed down or clicked it.
    Vector2 m_dragGrabOffset;
};

```

3.

Add the handlers for the drag messages:

  1.

To define the behavior when the user starts to drag a button, in the private section of the `DragAndDrop` class define the handler for the `DragAndDropManipulator::StartedMessage` message:

```
private:

    ...

    // Define the handler for the DragAndDropManipulator::StartedMessage message from 2D nodes
    // that have an input manipulator which generates drag-and-drop messages.
    // This prepares the 2D node for dragging.
    void onDragStarted(DragAndDropManipulator::StartedMessageArguments& messageArguments)
    {
        // Get from the message arguments the button that the user starts to drag.
        Node2DSharedPtr dragSourceItem = dynamic_pointer_cast<Node2D>(messageArguments.getSource());

        // Get the size of the button that the user starts to drag.
        Vector2 dragSourceItemSize = dragSourceItem->getActualSize();

        // Set the size of the Drag Item to be the same as the size of that button.
        m_dragItem->setSize(dragSourceItemSize.getX(), dragSourceItemSize.getY());

        // Move the Drag Item to the correct position.
        updateDragAndDrop(messageArguments.getPoint(), dragSourceItem->getWorldTransform());

        // Make the Drag Item visible.
        m_dragItem->setVisible(true);
    }

    ...

```

  2.

To define the behavior when the user is dragging a button, after the `onDragStarted` function define the handler for the `DragAndDropManipulator::MovedMessage` message:

```
// Define the handler for the DragAndDropManipulator::MovedMessage message from 2D nodes
// that have an input manipulator which generates drag-and-drop messages.
void onDragMoved(DragAndDropManipulator::MovedMessageArguments& messageArguments)
{
    // Get from the message arguments the button that the user is dragging.
    Node2DSharedPtr dragSourceItem = dynamic_pointer_cast<Node2D>(messageArguments.getSource());

    // Move the Drag Item and update the icons of the buttons.
    updateDragAndDrop(messageArguments.getPoint(), dragSourceItem->getWorldTransform());
}

```


4.

Create and configure a drag-and-drop manipulator for each button:

  1.

In the private section of the `DragAndDrop` class add a function that creates and configures a drag-and-drop manipulator for a node:

```
// Create and configure a drag-and-drop manipulator for a node.
void createDragAndDropManipulator(NodeSharedPtr dragSourceItem)
{
    Domain* domain = getDomain();

    // Create an input manipulator that generates drag-and-drop messages.
    DragAndDropManipulatorSharedPtr dragAndDropManipulator = DragAndDropManipulator::create(domain);

    // Add the input manipulator to the node.
    dragSourceItem->addInputManipulator(dragAndDropManipulator);

    // Set the duration of the long press before the drag-and-drop starts to 200 ms. The default is 500 ms.
    // This is the amount of time the user must press the node before they can start dragging it.
    dragAndDropManipulator->setPressDuration(chrono::milliseconds(200));

    // Subscribe to the DragAndDropManipulator::StartedMessage message at the node.
    // The DragAndDropManipulator generates this message when the user presses the node
    // for the duration set by DragAndDropManipulator::setPressDuration.
    dragSourceItem->addMessageHandler(DragAndDropManipulator::StartedMessage, bind(&DragAndDrop::onDragStarted, this, placeholders::_1));

    // Subscribe to the DragAndDropManipulator::MovedMessage message at the node.
    // The DragAndDropManipulator generates this message when the pointer moves.
    dragSourceItem->addMessageHandler(DragAndDropManipulator::MovedMessage, bind(&DragAndDrop::onDragMoved, this, placeholders::_1));
}

```

  2.

In the end of the `Application::onProjectLoaded` function call the `createDragAndDropManipulator` function for each button:

```
void onProjectLoaded() override
{
    ...

    // Create a drag-and-drop manipulator for each button.
    // You get the button nodes using their aliases.
    createDragAndDropManipulator(screen->lookupNode<Node>("#Navigation"));
    createDragAndDropManipulator(screen->lookupNode<Node>("#Phone"));
    createDragAndDropManipulator(screen->lookupNode<Node>("#Applications"));
    createDragAndDropManipulator(screen->lookupNode<Node>("#Music"));
    createDragAndDropManipulator(screen->lookupNode<Node>("#Car"));
}

```


5.

Build and run your application.

In the application long-press a button and drag it in the horizontal direction.

You drag an instance of the Drag Item prefab. The left side of the Drag Item is positioned at the input pointer, and the Drag Item does not yet show an icon. In the next section you complete the drag functionality.

## Complete the drag functionality


In this section you first set the icon and position of the button that the user drags. You then reposition the icons of the buttons as the user drags one of the buttons.

To complete the drag functionality:

1.

In the `onDragStarted` function before you call the `updateDragAndDrop` function set the icon for the Drag Item and correctly position the node:

```
void onDragStarted(DragAndDropManipulator::StartedMessageArguments& messageArguments)
    {
        ...

        // Get the data context object of the button that the user starts to drag.
        m_draggedDataContext = dynamic_pointer_cast<DataObject>(dragSourceItem->getProperty(DataContext::DataContextProperty));

        // Set the Data Context property of the Drag Item to the data context of the button.
        // This way you set the Drag Item to have the same icon as the button that the user starts to drag.
        m_dragItem->setProperty(DataContext::DataContextProperty, m_draggedDataContext);

        // Save the point from which the user started dragging the node,
        // relative to the origin (by default the top-left corner) of the node.
        m_dragGrabOffset = messageArguments.getPoint();

        ...
    }

    ...

    // Define a member variable for the data context object of the button that the user drags.
    DataObjectSharedPtr m_draggedDataContext;
};

```

2.

In the `updateDragAndDrop` function, before you call the `updateItems()` function, add the code that repositions the icons of all buttons as the user drags one of the buttons:

```
void updateDragAndDrop(Vector2 dragPosition, Matrix3x3 dragWorldTransform)
{
    ...

    // Get the global pointer position.
    Vector2 globalPointerPosition = dragWorldTransform * dragPosition;

    // Convert global coordinates to local coordinates of the Grid Layout 2D node.
    Vector2 hitTestPoint = *m_grid->globalToLocal(globalPointerPosition);

    // Get the width of the button.
    float cellWidth = m_grid->getActualColumnSize(0);

    // Calculate the index of the button in the Grid Layout 2D node.
    unsigned int cellIndex = 0;

    if (hitTestPoint.getX() > 0.0f)
    {
        cellIndex = floatToUint(hitTestPoint.getX() / cellWidth);
        cellIndex = min(cellIndex, static_cast<unsigned int>(m_grid->getChildCount() - 1u));
    }

    // Remove the data object from the old position.
    m_rootData->removeChild(*m_draggedDataContext);

    // Insert the data object to the new position.
    m_rootData->insertChild(cellIndex, m_draggedDataContext);

    ...
}

```

3.

In the `updateItems()` function in the `for` loop add the `if-else` clause which hides the icon of the button while the user drags it:

```
void updateItems()
{
    ...

    for (; dataIt != endDataIt; dataIt++, nodeIt++)
    {
        ...

        // If the button node is the one that the user is dragging, hide it.
        // You hide the node because you use the Drag Item to visualize the dragging of the node.
        if (m_draggedDataContext && itemData == m_draggedDataContext)
        {
            itemNode->setVisible(false);
        }
        else
        {
            itemNode->setVisible(true);
        }
    }
}

```


## Create the drop functionality


In the previous sections you implemented the dragging of a button. When the user ends the drag-and-drop gesture, the Drag Item stays visible in the exact position where the user releases the pointer. In this section you add the code to make the button look like it falls into its place when the user drops it.

To create the drop functionality:

1.

To define the behavior when the user stops dragging a node and releases the pointer, after the `onDragMoved` function define the handler for the `DragAndDropManipulator::FinishedMessage` message:

```
// Define the handler for the DragAndDropManipulator::FinishedMessage message from 2D nodes
// that have an input manipulator which generates drag-and-drop messages.
void onDragFinished(DragAndDropManipulator::FinishedMessageArguments&)
{
    // Hide the Drag Item prefab instance.
    m_dragItem->setVisible(false);

    // Clear the pointer to the data context object.
    m_draggedDataContext.reset();

    // Assign the correct icons to the buttons.
    updateItems();
}

```

2.

In the end of the `createDragAndDropManipulator` function subscribe to the `DragAndDropManipulator::FinishedMessage` message at the node:

```
// Create and configure a drag-and-drop manipulator for a node.
void createDragAndDropManipulator(NodeSharedPtr dragAndDropNode)
{
    ...

    // Subscribe to the DragAndDropManipulator::FinishedMessage message at the node.
    // The DragAndDropManipulator generates this message when the user ends the drag-and-drop gesture
    // by releasing the pointer.
    dragSourceItem->addMessageHandler(DragAndDropManipulator::FinishedMessage, bind(&DragAndDrop::onDragFinished, this, placeholders::_1));
}

```

3.

Build and run your application.

When you end the drag-and-drop gesture, the Drag Item becomes invisible.


Previous step Next step
