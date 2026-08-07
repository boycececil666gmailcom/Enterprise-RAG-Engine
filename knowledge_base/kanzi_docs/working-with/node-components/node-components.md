---
title: Node components
source: https://docs.kanzi.com/4.1.0/en/working-with/node-components/node-components.html
---

# Node components


Use node components to add functionality to a node.

For example, a trigger executes an action when a condition is met and an Animation Player animates properties of the node to which it is attached.

In Kanzi you can use these types of node components:

- Triggers. Use triggers to react to messages or events, and to apply logic. In a trigger use Conditions to set which conditions must be met for the trigger to set off and Actions to set what happens when a trigger sets off. See Triggers, Using triggers.

In Kanzi these triggers are available:

  - Several types of Message Trigger which set off when they intercept a message produced by an event, such as a state change in a UI control or component, or user input. For example, a Button node sends a message when a user clicks that button and an Animation Player sends a message when it starts the playback of an animation.
  - On Attached trigger sets off when Kanzi attaches a node with that trigger to the node tree.
  - On Property Change trigger sets off when a property value changes.
  - On Timer trigger sets off at specific time intervals.


See Triggers reference.
- Animation. Use animation players to play keyframe animations and interpolate property values to dynamic target values. See Animation system.

In Kanzi these animation players are available:

  - Animation Player.

Use the Animation Player to play and control the playback of keyframe animations.

See Using keyframe animations.
  - Float Value Accumulator.

Use a Float Value Accumulator to increment a value of a float property type or a property field over time or per frame.

See Incrementing the value of a property type.
  - Int Value Accumulator.

Use an Int Value Accumulator to increment a value of an integer property type over time or per frame.

See Incrementing the value of a property type.
  - Property Driven Animation Player.

Use the Property Driven Animation Player when you want to use a property type instead of time to control a keyframe animation.

See Creating property-driven animations.
  - Property Target Interpolator.

Use the Property Target Interpolator when you want to dynamically set the target value for a property and want to interpolate the current value to the target value over time.

See Interpolating property values.
  - Property Target Easing Interpolator.

Use the Property Target Easing Interpolator when you want to dynamically set the target value for a property and want to interpolate the current value to the target value over time using an easing function. Easing functions enable you to create lifelike animations that offer a more pleasant user experience.

See Interpolating property values using easing functions.

- Input Manipulators. Use input manipulator components to enable gesture recognition for nodes in your Kanzi application. See Handling user input. In Kanzi these input manipulator components are available:

  - Click Manipulator.

Use the Click Manipulator to enable users to click nodes in your Kanzi application.

See Using the Click Manipulator.
  - Key Manipulator.

Use the Key Manipulator to set the keys that the user can use to navigate your application. For example, you can override the default focus navigation keys and use a specific key to set focus to a node, set a key to open or close a popup-type window, or move focus in the focus chain.

See Using the Key Manipulator.
  - Long-Press Manipulator.

Use the Long-Press Manipulator to enable users to long-press nodes in your Kanzi application.

See Using the Long-Press Manipulator.
  - Multi-Click Manipulator.

Use the Multi-Click Manipulator to enable users to multi-click nodes in your Kanzi application.

See Using the Multi-Click Manipulator.
  - Navigation Manipulator.

Use the Navigation Manipulator to set the keys that the user can use to navigate to different directions in your application.

See Using the Navigation Manipulator.
  - Pan Manipulator.

Use the Pan Manipulator to enable users to move nodes in your Kanzi application.

See Using the Pan Manipulator.

- **Custom node components**. Use a custom node component to add custom functionality to a node.

A custom node component is an isolated piece of logic, which you implement in a Kanzi Engine plugin and you can attach to any node. See Kanzi Engine plugins and Creating custom node components.

## Using node components in the API


For details, see the `NodeComponent` class.
