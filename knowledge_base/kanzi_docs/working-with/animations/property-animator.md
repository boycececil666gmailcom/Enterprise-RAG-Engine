---
title: Incrementing the value of a property type
source: https://docs.kanzi.com/4.1.0/en/working-with/animations/property-animator.html
---

# Incrementing the value of a property type


Use a Value Accumulator to increment a value of a property type over time or per frame. While you can achieve a similar result with a keyframe animation or a State Manager, a Value Accumulator enables you to:

- Control the size of the increment at application runtime.
- Loop the value increment.
- Increment the value once per frame, independent of the time interval between frames.


For example, you can use a Value Accumulator to:

- Create a stopwatch. See Creating a stopwatch.
- Create a timer. See Creating a timer.
- Move a texture on a 3D model. For example, to create an animation of a moving road, see Creating an animation of a moving road.
- Rotate a 3D model. For example, to create an animation of spinning wheels, see Rotating a 3D model.
- Create a frame counter. See Creating a frame counter.


Kanzi includes a Float Value Accumulator, an Int Value Accumulator, and messages that allow you to control the playback of Value Accumulators.

When you want to increment the value of a property whose data type is neither an integer nor a floating point, use an intermediate property that is one of these data types, and create a binding to convert the data type. For example, when you want to show the changing value of a property as a string in a Text Block node, bind the Text property to the value of an intermediate property that you increment with a Value Accumulator.
## Creating a stopwatch


To create a stopwatch, use an Int Value Accumulator to increment the value of an integer property type.

To create a stopwatch:

1.

In the Node Tree create a node that shows the stopwatch time.

For example, create a Text Block node to show the elapsed seconds.
2.

In the Library > Property Types create a property type whose Data Type is Integer, and add the property type to the node that you created in the previous step.

You use this property type as an intermediate property that an Int Value Accumulator increments. Later in this procedure you create a binding that converts the value of this property to a string, so that a Text Block node can show it.
3.

In the Node Tree select the node that shows the stopwatch time, in the Node Components press Alt and right-click Animation, and select Int Value Accumulator.
4.

In the Create Int Value Accumulator dialog set the Target Property Type to the property whose value you want to increment.

Set it to the intermediate property type that you created earlier in this procedure and added to this node.
5.

To configure the Value Accumulator to create a stopwatch, set:

  - Increment Size to the value by which you want to change the value of a property every time the amount of time set in the Increment Time Interval property passes.

To create a stopwatch that shows seconds, set it to 1.
  - Minimum Value to the lowest value that the Value Accumulator uses.

Keep in mind that the final value of the target property is the base value of the property plus the total sum of the increments added by a Value Accumulator.

To start the stopwatch from 0, set it 0.
  - Maximum Value to the highest value that the Value Accumulator uses.

Keep in mind that the final value of the target property is the base value of the property plus the total sum of the increments added by a Value Accumulator.

To show a maximum of 59 seconds, set it to 59.
  - Autoplay to disabled.

To manually control when a Value Accumulator changes the value of a property, disable this property, and use Value Accumulator messages to start, pause, resume, and stop a Value Accumulator. You add these controls later in this procedure.
  - Bound Type to how you want the Value Accumulator to handle the increments when it reaches the limits of the range of increments set by the Minimum Value and Maximum Value properties.

To automatically restart the stopwatch after 59 seconds, set it to Loop.

When set to Loop the Value Accumulator wraps the value when it reaches the lowest or the highest value. When set to Clamp the Value Accumulator no longer increments the value when it reaches the highest value.
  - Increment Time Interval to how often you want to change the value of the property in milliseconds.

To change the value once a second, set it to 1000.

6.

In the Node Tree select the Text Block node that you created in the beginning of this procedure, in the Properties click + Add Binding, and in the Binding Editor:

  - Set Property to Text.
  - From the Properties drag the intermediate property type that you created to the Expression text field.


Click Save.

You bind the Text property to the intermediate property type whose value the Int Value Accumulator increments. The binding converts the integer to a string that the Text Block node can show.
7.

Control the Value Accumulator:

  1.

In the Node Tree create a node that contains the trigger that you want to use to start the Int Value Accumulator.

For example, create a Button 2D node and use its Button: Click trigger.
  2.

In the Node Tree select the node that you created in the previous step, in the Node Components in the trigger that you want to use to start the Int Value Accumulator press Alt and right-click Actions, and select Dispatch Message Action > Value Accumulator > Start.
  3.

In the Value Accumulator: Start message set the Target Item property to the Text Block node that you created in the beginning of this procedure.

8.

Create the pause, resume, and stop controls for the Int Value Accumulator. Repeat the previous step, but use these messages:

  - Pause
  - Resume
  - Stop


See Value Accumulator messages.

## Creating a timer


To create a timer, use an Int Value Accumulator to decrease the value of an integer property type.

To create a timer:

1.

Create a stopwatch. See Creating a stopwatch.
2.

In the Node Tree select the Text Block node that shows the time, and in the Properties set the value of the intermediate property to the time from which you want the timer to count down.

For example, to count down from 5 seconds, set the value to 5.
3.

In Node Components in the Int Value Accumulator set:

  - Increment Size to the value by which you want to change the value of a property every time the amount of time set in the Increment Time Interval property passes.

To create a timer that counts down seconds, set it to -1.
  - Minimum Value to the lowest value that the Value Accumulator uses.

Keep in mind that the final value of the target property is the base value of the property plus the total sum of the increments added by a Value Accumulator.

To end the timer at 0 seconds, set it to -5.
  - Maximum Value to the highest value that the Value Accumulator uses.

Keep in mind that the final value of the target property is the base value of the property plus the total sum of the increments added by a Value Accumulator.

To start the timer at 5 seconds, set it to 0.
  - Bound Type to how you want the Value Accumulator to handle the increments when it reaches the limits of the range of increments set by the Minimum Value and Maximum Value properties.

To stop the timer when it reaches 0, set it to Clamp.

When set to Clamp the Value Accumulator no longer increments the value when it reaches the highest value.


## Creating an animation of a moving road


To create an animation of a moving road, use a Float Value Accumulator to increment the value of a property field that changes the position of a texture on a Plane.

To create an animation of a moving road:

1.

In the Library > Materials and Textures press Alt and right-click Material Types, and select the material that you want to use to show the texture of a road on geometry.

For example, create the FragmentPhongTextured material type.
2.

In the Assets window click Import Assets and import the image that you want to use as the road.

Kanzi Studio creates in the Library > Materials and Textures > Textures a Single Texture for the image.

For example, import this image.
3.

In the Library > Materials and Textures > Textures select the texture that shows the image that you imported, and in the Properties set the Wrap Mode property to Repeat.

This way you set the texture to repeat to cover the geometry.
4.

In the Node Tree create a node that represents a road that you want to animate.

For example, create a Plane node, set it to use the FragmentPhongTexturedMaterial material, and in the node add and set the properties of the material and geometry.
5.

In the Node Components press Alt and right-click Animation, and select Float Value Accumulator.
6.

In the Create Float Value Accumulator dialog set:

  - Target Property Type to the property whose property field you want to increment.

To move the texture on the Plane, set it to the Material > Texture Offset property.
  - Target Property Field to the property field of the property type that you selected in the Target Property Type property.

To move the texture on the y axis, set it to the Vector Y property field.

7.

To configure the Value Accumulator to create an animation of a moving road, set:

  - Increment Size to the value by which you want to change the value of a property field every time the amount of time set in the Increment Time Interval property passes.

To move the texture on the Plane, set it to 0.01. To adjust the speed of the animation, adjust this value.
  - Minimum Value to the lowest value that the Value Accumulator uses.

Keep in mind that the final value of the target property is the base value of the property plus the total sum of the increments added by a Value Accumulator.

To set the starting position of the texture on the Plane, set it to 0.
  - Maximum Value to the highest value that the Value Accumulator uses.

Keep in mind that the final value of the target property is the base value of the property plus the total sum of the increments added by a Value Accumulator.

To set the ending position of the texture on the Plane, set it to 1.
  - Bound Type to how you want the Value Accumulator to handle the increments when it reaches the limits of the range of increments set by the Minimum Value and Maximum Value properties.

To loop the animation of the texture, set it to Loop.

When set to Loop the Value Accumulator wraps the value when it reaches the lowest or the highest value.
  - Increment Time Interval to how often you want to change the value of the property field in milliseconds.

For a smooth animation keep the value of the Increment Time Interval property low and adjust the speed of the animation by adjusting the value of the Increment Size property.

For example, set it to 16.


## Rotating a 3D model


You can use a Float Value Accumulator to rotate a 3D model. For example, to create an animation of a spinning wheel.

To use a Value Accumulator to rotate a 3D model:

1.

In the Library > Property Types create a property type whose Data Type is Float, and add that property type to the 3D node that you want to rotate with a Value Accumulator.

You use this property type as an intermediate property that a Float Value Accumulator increments. Later in this procedure you create a binding that creates the rotation using the quaternion data type that you can use for rotation property fields in the Layout Transformation and Render Transformation.
2.

In the Node Tree select a 3D node that you want to rotate with a Value Accumulator, in the Node Components press Alt and right-click Animation, and select Float Value Accumulator.
3.

In the Create Float Value Accumulator dialog set the Target Property Type to the property that you created earlier in this procedure and added to this node.
4.

Configure the Value Accumulator. For example, set:

  - Increment Size to the value by which you want to change the value of a property field every time the amount of time set in the Increment Time Interval property passes.

For example, set it to -2.
  - Minimum Value to the lowest value that the Value Accumulator uses.

Keep in mind that the final value of the target property is the base value of the property plus the total sum of the increments added by a Value Accumulator.

For example, set it to 0.
  - Maximum Value to the highest value that the Value Accumulator uses.

Keep in mind that the final value of the target property is the base value of the property plus the total sum of the increments added by a Value Accumulator.

For example, set it to 359.
  - Bound Type to how you want the Value Accumulator to handle the increments when it reaches the limits of the range of increments set by the Minimum Value and Maximum Value properties.

To loop the animation of the rotating wheel, set it to Loop.

When set to Loop the Value Accumulator wraps the value when it reaches the lowest or the highest value.
  - Increment Time Interval to how often you want to change the value of the property field in milliseconds.

For a smooth animation keep the value of the Increment Time Interval property low and adjust the speed of the animation by adjusting the value of the Increment Size property.

For example, set it to 16.

5.

In the Node Tree select the 3D node to which you added a Float Value Accumulator, in the Properties click + Add Binding, and in the Binding Editor set:

  - Property to Render Transformation
  - Property Field to ROTATION
  - In the Expression click Enter Operation, select the CreateRotation for the axis around which you want to rotate the node and from the Properties drag the intermediate property type that you created to the Expression text field as the argument for the CreateRotation function.

For example, use the CreateRotationX function to rotate the node around its x axis.


Click Save.

You create the rotation on the x axis where you use the intermediate property that the Float Value Accumulator increments, and bind the Render Transformation property field ROTATION to that rotation.

## Creating a frame counter


To create a frame counter, use an Int Value Accumulator with the Increment Mode set to Per Frame. In this mode, the Value Accumulator increments the value once per frame, regardless of how much time has passed between frames.

To create a frame counter:

1.

In the Node Tree create a node that shows the frame count.

For example, create a Text Block node to show the number of frames.
2.

In the Library > Property Types create a property type whose Data Type is Integer, and add the property type to the node that you created in the previous step.

You use this property type as an intermediate property that an Int Value Accumulator increments. Later in this procedure you create a binding that converts the value of this property to a string, so that a Text Block node can show it.
3.

In the Node Tree select the node that shows the frame count, in the Node Components press Alt and right-click Animation, and select Int Value Accumulator.
4.

In the Create Int Value Accumulator dialog set the Target Property Type to the property whose value you want to increment.

Set it to the intermediate property type that you created earlier in this procedure and added to this node.
5.

To configure the Value Accumulator to create a frame counter, set:

  - Increment Mode to Per Frame.

This sets the Value Accumulator to increment the value once per frame, regardless of how much time has passed between frames. In this mode, the Increment Time Interval property is ignored.
  - Increment Size to the value by which you want to change the value of a property on every frame.

To increment by one on every frame, set it to 1.
  - Minimum Value to the lowest value that the Value Accumulator uses.

Keep in mind that the final value of the target property is the base value of the property plus the total sum of the increments added by a Value Accumulator.

To start the frame counter from 0, set it 0.
  - Maximum Value to the highest value that the Value Accumulator uses.

Keep in mind that the final value of the target property is the base value of the property plus the total sum of the increments added by a Value Accumulator.

For example, to count up to 1000 frames, set it to 1000.
  - Bound Type to how you want the Value Accumulator to handle the increments when it reaches the limits of the range of increments set by the Minimum Value and Maximum Value properties.

To restart the frame counter after it reaches the maximum value, set it to Loop.

When set to Loop the Value Accumulator wraps the value when it reaches the lowest or the highest value. When set to Clamp the Value Accumulator no longer increments the value when it reaches the highest value.

6.

In the Node Tree select the Text Block node that you created in the beginning of this procedure, in the Properties click + Add Binding, and in the Binding Editor:

  - Set Property to Text.
  - From the Properties drag the intermediate property type that you created to the Expression text field.


Click Save.

You bind the Text property to the intermediate property type whose value the Int Value Accumulator increments. The binding converts the integer to a string that the Text Block node can show.

## Using Value Accumulators in the API


To create an Int Value Accumulator:

```
// Create an Int Value Accumulator.
IntValueAccumulatorSharedPtr accumulator = IntValueAccumulator::create(domain, "accumulator");

// Set the property type whose value you want to use to set the size of the increment.
accumulator->setIncrementSizeSource(inputValuePropertyType.getName());

// Set the target property type whose values you want to increment.
accumulator->setTargetPropertyType(targetPropertyType.getName());

// Set the frequency of the increments in milliseconds.
accumulator->setIncrementTimeInterval(1);

// Set the minimum and maximum values that, when added to the value of the target property,
// set the lowest and the highest values that the Value Accumulator uses.
accumulator->setMinimumAccumulatedValue(100);
accumulator->setMaximumAccumulatedValue(800);

// Set how you want the Value Accumulator to handle the value of a property when it reaches
// the lowest or the highest value that is defined by adding the value of the target property
// to the minimum and maximum values.
//
// When set to Loop and the Value Accumulator reaches the target property value added to the
// maximum value, the Value Accumulator sets the property value back to the value defined by
// the target property value added to the minimum value.
accumulator->setBoundType(ValueAccumulatorBase::BoundType::Loop);

/// Add the Value Accumulator to the node.
node->addNodeComponent(accumulator);

```


To create a Float Value Accumulator:

```
// Create a Float Value Accumulator.
FloatValueAccumulatorSharedPtr accumulator = FloatValueAccumulator::create(domain, "accumulator");

// Set the property type whose value you want to use to set the size of the increment.
accumulator->setIncrementSizeSource(inputValuePropertyType.getName());

// Set the target property type and its property field whose values you want to increment.
accumulator->setTargetPropertyType(targetPropertyType.getName());
accumulator->setTargetPropertyField(PropertyFieldVectorX);

// Set the minimum and maximum values that, when added to the value of the target property,
// set the lowest and the highest values that the Value Accumulator uses.
accumulator->setMinimumAccumulatedValue(0.1f);
accumulator->setMaximumAccumulatedValue(0.8f);

// Set how you want the Value Accumulator to handle the value of a property when it reaches
// the lowest or the highest value that is defined by adding the value of the target property
// to the minimum and maximum values.
//
// When set to Loop and the Value Accumulator reaches the target property value added to the
// maximum value, the Value Accumulator sets the property value back to the value defined by
// the target property value added to the minimum value.
accumulator->setBoundType(ValueAccumulatorBase::BoundType::Loop);

// Add the Value Accumulator to the node.
node->addNodeComponent(accumulator);

```


To use per-frame increment mode with an Int Value Accumulator:

```
// Create an Int Value Accumulator.
auto accumulator = IntValueAccumulator::create(domain, "accumulator");

// Set the property type whose value you want to use to set the size of the increment.
accumulator->setIncrementSizeSource(inputValuePropertyType.getName());

// Set the target property type whose values you want to increment.
accumulator->setTargetPropertyType(targetPropertyType.getName());

// Set the increment mode to PerFrame. In this mode, the Value Accumulator increments the value
// once per frame, ignoring the time delta. This is useful for frame counters.
accumulator->setIncrementMode(ValueAccumulatorBase::IncrementMode::PerFrame);

// Set the minimum and maximum values for the accumulated value.
accumulator->setMinimumAccumulatedValue(0);
accumulator->setMaximumAccumulatedValue(100);

// Set the bound type to Loop so the value wraps around when it reaches the maximum.
accumulator->setBoundType(ValueAccumulatorBase::BoundType::Loop);

// Add the Value Accumulator to the node.
node->addNodeComponent(accumulator);

```
