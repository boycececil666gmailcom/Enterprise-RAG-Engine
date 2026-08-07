---
title: Step 3 - Long-press to drop a pin
source: https://docs.kanzi.com/4.1.0/en/tutorials/pan-zoom-tap/step-3.html
---

# Step 3 - Long-press to drop a pin


Use the Long-Press Manipulator to enable users to long-press nodes in your Kanzi application.

This way you can make the application react when the user presses and holds the pointer pressed on a node for the amount of time that you set in the Long-Press Manipulator.

In Kanzi Studio you can use the Long-Press Manipulator component to install a long-press manipulator to a node, and to control the behavior of that long-press manipulator.

In this step you use the Long-Press Manipulator component and long-press manipulator to enable the user to drop a pin on the map by long-pressing the map. For example, this way you can enable the user to mark a point of interest on the map.
## Drop a pin


In this section you create and use the Long-Press Manipulator component and long-press manipulator to drop a pin on the map when the user long-presses the map.

To drop a pin:

1.

In Kanzi Studio in the Node Tree select the Map node, in the Node Components > Input Manipulators section create a Long-Press Manipulator component, and set the Long Press Duration property to 400.

This way you install to the Map node a long-press manipulator, which recognizes a long-press gesture when the user presses the Map node for 400 milliseconds.
2.

Select File > Export > Export KZB.
3.

In Visual Studio in the `Application::onProjectLoaded` function, after you get the Map node and before you subscribe to the input manipulator messages, instantiate the Pin prefab as a child of the Map node:

```
    void onProjectLoaded() override
    {
        ...

        // Get the reference to the prefab template Pin which shows the pin icon.
        ResourceManager* resourceManager = domain->getResourceManager();
        PrefabTemplateSharedPtr pinPrefabTemplate = resourceManager->acquireResource<PrefabTemplate>("kzb://pan_zoom_tap/Prefabs/Pin");

        // Instantiate the Pin prefab.
        m_pin = pinPrefabTemplate->instantiate<Node2D>("Pin");

        // Add to the Map node the instance of the Pin prefab you created.
        mapNode->addChild(m_pin);

        // Disable the Visible property of the Pin prefab instance.
        // You enable the Visible property when the user drops a pin.
        m_pin->setVisible(false);

        ...
    }

private:

    ...

    // Define a member variable for the Pin prefab instance.
    Node2DSharedPtr m_pin;
};

```

4.

In the private section of the `PanZoomTap` class define the handler for the long-press message:

```
// Define the handler for the LongPressManipulator::LongPressMessage message from the nodes
// that have an input manipulator which generates the long-press message.
void onLongPress(LongPressManipulator::LongPressMessageArguments& messageArguments)
{
    // Get from the message arguments the node that the user long-presses.
    Node2DSharedPtr mapNode = dynamic_pointer_cast<Node2D>(messageArguments.getSource());

    // Get the point where the user long-pressed.
    Vector2 pointerPosition = messageArguments.getPoint();

    // Create a render transformation that contains the translation to the point where the user long-pressed.
    SRTValue2D pinSRT = SRTValue2D::createTranslation(pointerPosition);

    // Position the tip of the pin where the user long-pressed.
    pinSRT.setTranslation(pinSRT.getTranslation() - Vector2(m_pin->getActualWidth() * 0.5f, m_pin->getActualHeight() * 0.8f));

    // Apply the transformation to the Pin prefab instance.
    m_pin->setRenderTransformation(pinSRT);

    // Enable the Visible property of the Pin prefab instance.
    m_pin->setVisible(true);
}

```

5.

In the `Application::onProjectLoaded` function subscribe to the long-press message at the Map node:

```
void onProjectLoaded() override
{
    ...
    // Subscribe to the LongPressManipulator::LongPressMessage message at the Map node.
    // The LongPressManipulator manipulator generates this message when the user presses the node
    // for the amount of milliseconds you set in the LongPressManipulator::setPressDuration function.
    mapNode->addMessageHandler(LongPressManipulator::LongPressMessage, bind(&PanZoomTap::onLongPress, this, placeholders::_1));
}

```

6.

Build and run your application.

In the application long-press anywhere on the map to drop a pin.

## Keep the size and orientation of the dropped pin


When the user zooms and rotates the map, the dropped pin changes size and rotates with the map. This is because you instantiated the Pin prefab, which shows the pin, as a child of the Map node. In this section you add the code to keep the size and orientation of the pin constant.

To keep the size and orientation of the dropped pin:

1.

In the private section of the `PanZoomTap` class create a function which updates the scale and rotation of the dropped pin based on the scale and rotation of the Map node:

```
// Update the scale and rotation of the Pin prefab instance.
void updatePinScaleAndRotation(SRTValue2D mapSRT, SRTValue2D pinSRT)
{
    // Set the rotation to be the negative of the rotation of the Map node.
    pinSRT.setRotation(-mapSRT.getRotation());

    // Set the scale to be the inverse of the scale of the Map node.
    pinSRT.setScale(componentWiseDivide(Vector2(1.0f, 1.0f), mapSRT.getScale()));

    // Apply the render transformation to the Pin prefab instance.
    m_pin->setRenderTransformation(pinSRT);
}

```

2.

In the `onLongPress` function that you added in the previous section, first get the render transformation of the Map node, then call the `updatePinScaleAndRotation` function.

This way you keep the size and orientation of the Pin the same regardless of the zoom level and rotation of the Map node.

Replace

```
// Apply the transformation to the Pin prefab instance.
m_pin->setRenderTransformation(pinSRT);

```


with

```
// Get the Render Transformation property of the Map node.
SRTValue2D mapSRT = mapNode->getRenderTransformation();

// Update the scale and position of the Pin prefab instance.
updatePinScaleAndRotation(mapSRT, pinSRT);

```

3.

In the end of the `onPinchMoved` function that you created in step 2 of this tutorial, update the scale and rotation of the dropped pin when the user zooms and rotates the map:

```
void onPinchMoved(PinchManipulator::MovedMessageArguments& messageArguments)
{
    ...

    // Get the Render Transformation property of the Pin prefab instance.
    SRTValue2D pinSRT = m_pin->getRenderTransformation();

    // Update the scale and position of the Pin prefab instance.
    updatePinScaleAndRotation(*mapWorldSRT, pinSRT);
}

```

4.

In the end of the `onNodeDoubleTapped` function that you created in step 2 of this tutorial, reset the scale and rotation of the dropped pin when the user double-taps the map:

```
void onNodeDoubleTapped(MultiClickManipulator::MultiClickMessageArguments& messageArguments)
{
    ...

    // Reset the rotation and scale of the Pin prefab instance.
    SRTValue2D pinSRT = m_pin->getRenderTransformation();
    pinSRT = SRTValue2D(Vector2(1.0f, 1.0f), 0, pinSRT.getTranslation());
    m_pin->setRenderTransformation(pinSRT);
}

```

5.

Build and deploy the application to your Android device.

When you zoom and rotate the map, the pin that you dropped maintains its size and orientation.


Previous step
## Whatâs next?


In this tutorial you learned how to use the Kanzi gesture components and input manipulators to enable panning, zooming, rotating, resetting the position, and dropping a pin on the map. Now you can:

- Learn how to use the drag-and-drop manipulator to reorder the buttons in a navigation bar. See Tutorial: Drag and drop.
- Learn how to use the Kanzi Engine API to access nodes and resources from the kzb file you created in Kanzi Studio, get and set the property values of Kanzi nodes, use custom property types, instantiate prefabs, load and play animations, load resources from the kzb file, use Kanzi messages to define events, and deploy the completed application to an Android device. See Tutorial: Kanzi Engine API advanced use.
