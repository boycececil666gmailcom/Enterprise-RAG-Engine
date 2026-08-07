---
title: Step 2 - Zoom and rotate the map
source: https://docs.kanzi.com/4.1.0/en/tutorials/pan-zoom-tap/step-2.html
---

# Step 2 - Zoom and rotate the map


Use the Pinch Manipulator to enable users to zoom and rotate nodes in your Kanzi application.

To calculate the amount by which to zoom and rotate a node, the pinch gesture continuously tracks the position and distance between two fingers that move on the device screen.

Use the Multi-Click Manipulator to enable users to multi-click nodes in your Kanzi application.

You can set in the multi-click manipulator the number of clicks and the maximum amount of time that can lapse between the clicks for Kanzi to interpret the clicks as a multi-click gesture.

In Kanzi Studio you can use the Multi-Click Manipulator component to install a multi-click manipulator to a node, and to control the behavior of that multi-click manipulator.

In this step you first use the pinch manipulator to enable zooming and rotating of the map. Then you use the Multi-Click Manipulator component and multi-click manipulator to enable resetting the position, zoom level, and rotation angle of the map.

You deploy the tutorial application to an Android device, because the pinch gesture requires multitouch support.
## Zoom and rotate the map


In this section you create and use the pinch manipulator to zoom and rotate the map when the user pinches the map.

To zoom and rotate the map:

1.

In the `pan_zoom_tap.cpp` file in the private section of the `PanZoomTap` class define the handlers for the pinch messages:

```
private:

    ...

    // Define the handler for the PinchManipulator::StartedMessage message from the 2D nodes
    // that have an input manipulator which generates pinch messages.
    // This handler prepares a 2D node for a pinch gesture.
    void onPinchStarted(PinchManipulator::StartedMessageArguments& messageArguments)
    {
        // Get from the message arguments the node that the user pinches.
        Node2DSharedPtr mapNode = dynamic_pointer_cast<Node2D>(messageArguments.getSource());

        // Store the initial value of the Render Transformation property Scale property field.
        SRTValue2D nodeTransform = mapNode->getRenderTransformation();
        m_pinchInitialScaleFactor = nodeTransform.getScale().getX() - 1.0f;

        // Calculate a minimum scale value based on the size of the application screen.
        ScreenSharedPtr screen = getScreen();
        m_minScale = max(getScreen()->getActualWidth() / mapNode->getActualWidth(), screen->getActualHeight() / mapNode->getActualHeight());
    }

    // Define the handler for the PinchManipulator::MovedMessage message from the 2D nodes
    // that have an input manipulator which generates pinch messages.
    // This scales and rotates a 2D node for the amount of the pinch gesture.
    void onPinchMoved(PinchManipulator::MovedMessageArguments& messageArguments)
    {
        // Get from the message arguments the node that the user pinches.
        Node2DSharedPtr mapNode = dynamic_pointer_cast<Node2D>(messageArguments.getSource());

        // Get the scale and rotation from the message arguments.
        float scaleDelta = messageArguments.getScale();
        float rotateDelta = messageArguments.getRotation();

        // Calculate the scale by adding the initial scale to the pinch value.
        // Restrict the scale so that the map cannot be smaller than the application screen size.
        float scale = max(m_minScale, scaleDelta + m_pinchInitialScaleFactor);

        // Get the Render Transformation property of the Map node.
        SRTValue2D mapRenderSRT = mapNode->getRenderTransformation();

        // Apply the rotation.
        mapRenderSRT.rotate(rotateDelta);

        // Apply the scale.
        mapRenderSRT.setScale(Vector2(scale, scale));

        // Get the world transformation of the Map node.
        // You use this in the next step of the tutorial.
        Matrix3x3 mapWorldTransform = mapNode->getWorldTransform();

        optional<SRTValue2D> mapWorldSRT = SRTValue2D::create(mapWorldTransform);
        kzAssert(mapWorldSRT);

        // Apply the new render transformation to the Map node.
        mapNode->setRenderTransformation(mapRenderSRT);
    }

     // Define a member variable for the initial scale factor of the pinch gesture.
    float m_pinchInitialScaleFactor;

    // Define a member variable for the minimum scale value.
    float m_minScale;
};

```

2.

In the beginning of the public section of the `PanZoomTap` class add the constructor and set the initial scale factor for the pinch gesture:

```
public:

    PanZoomTap() :
        m_pinchInitialScaleFactor(0.0f)
    {
    }

    ...

```

3.

In the `Application::onProjectLoaded` function create a `PinchManipulator` manipulator and subscribe to its messages at the Map node:

```
void onProjectLoaded() override
{
    ...

    // Create an input manipulator that generates pinch messages.
    PinchManipulatorSharedPtr pinchManipulator = PinchManipulator::create(domain);

    // Add the input manipulator to the Map node.
    mapNode->addInputManipulator(pinchManipulator);

    // Subscribe to the PinchManipulator::StartedMessage message at the Map node.
    // The PinchManipulator generates this message when the user presses two fingers on the Map node.
    mapNode->addMessageHandler(PinchManipulator::StartedMessage, bind(&PanZoomTap::onPinchStarted, this, placeholders::_1));

    // Subscribe to the PinchManipulator::MovedMessage message at the Map node.
    // The PinchManipulator generates this message when the scale or rotation threshold is exceeded
    // and when the tracked touches move between updates.
    mapNode->addMessageHandler(PinchManipulator::MovedMessage, bind(&PanZoomTap::onPinchMoved, this, placeholders::_1));
}

```

4.

Deploy the application to an Android device, because the pinch gesture requires multitouch support:

  1.

Connect your Android device to your computer.
  2.

In the Kanzi Studio main menu select File > Export > Build Android Package.

Kanzi Studio creates an Android package from your Kanzi Studio project, deploys, and runs it on your Android device.


On your Android device use the pinch gesture to zoom and rotate the map.

The map rotates around its center point because the origin of the Map node is set to the center.

## Reset the position, zoom level, and rotation


In this section you create and use the Multi-Click Manipulator component and multi-click manipulator to reset the position, zoom level, and rotation angle of the map when the user double-taps the map.

To reset the position, zoom level, and rotation:

1.

In Kanzi Studio in the Node Tree select the Map node, in the Node Components press Alt and right-click Input Manipulators, and select Multi-Click Manipulator.

This way you enable users to multi-click the Map node. By adding a Multi-Click Manipulator component to a node you install a multi-click manipulator to that node.

By default the multi-click manipulator recognizes two quick clicks as a double-click gesture. In the Multi-Click Manipulator component you can use the Click Count property to set the number of clicks required for the installed multi-click manipulator to recognize the multi-click gesture and to send the multi-click message.
2.

In the Multi-Click Manipulator component set the Multi-Click Timeout property to 300.

Multi-Click Timeout sets the amount of time in milliseconds within which two consecutive clicks must occur for the multi-click manipulator to continue recognizing them as the multi-click gesture.
3.

Select File > Export > Export KZB.
4.

In Visual Studio in the `pan_zoom_tap.cpp` file in the private section of the `PanZoomTap` class define the handler for the multi-click message:

```
private:

    ...
    // Define the handler for the MultiClickManipulator::MultiClickMessage message from the nodes that have
    // an input manipulator which generates the multi-click message when the user double-taps the node.
    void onNodeDoubleTapped(MultiClickManipulator::MultiClickMessageArguments& messageArguments)
    {
        // Get from the message arguments the node that the user double-taps.
        Node2DSharedPtr mapNode = dynamic_pointer_cast<Node2D>(messageArguments.getSource());

        // Remove the Render Transformation property of the node.
        // This way you reset the position, zoom level, and rotation angle of the Map node.
        mapNode->removeLocalValue(Node2D::RenderTransformationProperty);
    }

    ...
};

```

5.

In the `Application::onProjectLoaded` function subscribe to the multi-click message at the Map node:

```
void onProjectLoaded() override
{
    ...
    // Subscribe to the MultiClickManipulator::MultiClickMessage message at the Map node.
    // The MultiClickManipulator manipulator generates this message when the user double-taps the node.
    mapNode->addMessageHandler(MultiClickManipulator::MultiClickMessage, bind(&PanZoomTap::onNodeDoubleTapped, this, placeholders::_1));
}

```

6.

Build and deploy the application to your Android device.

In the application first use the pinch gesture to zoom and rotate the map, and the pan gesture to move the map. Then double-tap the map to set it to the initial position, zoom level, and rotation angle.


Previous step Next step
