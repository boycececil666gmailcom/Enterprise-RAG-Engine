---
title: Using the Navigation Manipulator
source: https://docs.kanzi.com/4.1.0/en/working-with/input/navigation-manipulator.html
---

# Using the Navigation Manipulator


Use the Navigation Manipulator to set the keys that the user can use to navigate to different directions in your application.
## Default directional navigation keys


These are the default directional keyboard keys that the user can use in a Kanzi application:

- The Slider nodes have the Focusable property enabled and can receive focus by default. When a Slider node has focus, to move the knob of that slider, you can use these default keyboard keys:

  - Home to move the slider knob to the beginning of the rail
  - End to move the slider knob to the end of the rail
  - â and â to move the knob of a horizontal slider
  - â and â to move the knob of a vertical slider


To move a slider knob with the arrow keyboard keys, in that Slider node set the amount that the knob moves for each key press with the Step Value property.
- The Scroll View nodes that you create in Kanzi Studio have the Focusable property enabled and can receive focus by default. When a Scroll View node has focus, to scroll that node, you can use the default keyboard keys â, â, â, and â.
- When a List Box node has the focus, you can use these default keyboard keys to navigate the focusable list items:

  - â and â to move the focus between the focusable items in a List Box that scrolls on the y axis.
  - â and â to move the focus between the focusable items in a List Box that scrolls on the x axis.
  - Home to move the focus to the first focusable item.
  - End to move the focus to the last focusable item.
  - Page Up and Page Down to move the focus backward or forward by one page in a Grid List Box node. One page corresponds to the size of the visible area of the Grid List Box node.


See Handling the key focus in a List Box node.
- When a Text Box node is in the editing state, to move the cursor in that text box, you can use these default keyboard keys:

  - â to move the cursor one character backward.
  - â to move the cursor one character forward.
  - Ctrl â to move the cursor to the word boundary that precedes the cursor.
  - Ctrl â to move the cursor to the word boundary that follows the cursor.
  - Home to move the cursor to the beginning of the text content.
  - End to move the cursor to the end of the text content.


When a Text Box node is in the editing state, to modify the text selection in that text box, you can use these default keyboard keys:

  - Shift â to move the active cursor in the text selection one character backward.
  - Shift Ctrl to move the active cursor in the text selection to the word boundary that precedes the current position.
  - Shift Home to move the active cursor in the text selection to the beginning of the text content.
  - Shift â to move the active cursor in the text selection one character forward.
  - Shift Ctrl â to move the active cursor in the text selection to the word boundary that follows the current position.
  - Shift End to move the active cursor in the text selection to the end of the text content.
  - Ctrl A to select all text.


## Using the Navigation Manipulator triggers


Use the Navigation Manipulator triggers to react when the user starts, finishes, or cancels a directional navigation key gesture. For example, you can use a specific key to enable the user to move the key focus in a specific direction.

The Navigation Manipulator has these triggers:

- Key Navigation Started trigger is set off when Kanzi recognizes the key-pressed or key repeat gesture for a navigation key.

For example, this happens when the user presses a navigation key on their keyboard.
- Key Navigation Finished trigger is set off when Kanzi recognizes the key-released gesture for a navigation key.

For example, this happens when the user releases a navigation key on their keyboard.
- Key Navigation Canceled trigger is set off when Kanzi recognizes the cancellation of the key-pressed gesture for a navigation key.


To use the Navigation Manipulator triggers:

1.

Create and configure a Navigation Manipulator:

  1.

In the Node Tree or Prefabs select a focusable node that you want to receive directional navigation input from keys. See Using focus.

These nodes have the Focusable property enabled and can receive focus by default:

    - Button, Toggle Button, Slider, and Text Box nodes that you create using the Kanzi Engine API or Kanzi Studio.
    - Scroll View nodes that you create using Kanzi Studio.


For example, in the Prefabs select a prefab that you use to instantiate a vertically stacked group of menu buttons. You can by default move the focus between the buttons in the forward direction by pressing the Tab key and in the backward direction by pressing the Shift Tab keys. See Moving focus in the focus chain and Showing when a user interface element has focus.
  2.

In the Node Components press Alt and right-click Input Manipulators, and select Navigation Manipulator.

You use the Navigation Manipulator to set a node to react to directional navigation input from one or more keys.
  3.

In the Navigation Manipulator add and set one or more navigation key properties to the keys to which you want the node to react.

For example, to configure the keys with which the user can navigate up and down, add and set the Up Navigation Key and Down Navigation Key properties.

2.

Create and configure the trigger for a navigation key that you set in the previous step in the Navigation Manipulator:

  1.

In the Node Components create one of the Navigation Manipulator triggers.

For example, in the Node Components press Alt and right-click Triggers, select Message Trigger > Key Navigation > Key Navigation Started, and name the trigger.
  2.

If you set more than one navigation key property in the Navigation Manipulator, use a trigger condition to configure which navigation key sets off the trigger that you created.

In the Node Components press Alt and right-click the trigger, select Trigger Condition, and in the condition set:

    - A

      - Type of A to Message argument
      - Message Argument to Navigation Direction

    - Operation to =
    - B

      - Type of B to Fixed
      - Fixed Value to the navigation direction to whose navigation key you want the trigger to react.

For example, if you want the trigger to set off when the user presses the key that you set in the Navigation Manipulator using the Down Navigation Key property, set Fixed Value to Down.


  3.

In the Node Components press Alt and right-click the trigger that you created and select the action that you want the trigger to execute when the user presses the navigation key that you configured in the Navigation Manipulator.

For example, select the Move Focus action and in the action settings set Direction to Forward.

This action moves focus to the next node in the focus chain in the forward direction, similarly to how the focus moves when the user presses the Tab key.


When the user presses down the key that you set in the Navigation Manipulator, the Key Navigation Started trigger sets off the action that you created.

In this example, when the user presses down the â (Arrow down) key that you set in the Navigation Manipulator in the Down Navigation Key property, the focus moves to the next menu button in the forward direction.
3.

Repeat the previous step to create and configure another Navigation Manipulator trigger.

For example, create another Key Navigation Started trigger and in that trigger create:

  - Trigger Condition to set off the trigger when the user presses the key that you set in the Navigation Manipulator using the Up Navigation Key property.
  - Move Focus action where you set Direction to Backward.


In this example, when the user presses down the â (Arrow up) key that you set in the Navigation Manipulator in the Up Navigation Key property, the focus moves to the next menu button in the backward direction.


You can set more navigation keys in the Navigation Manipulator and create triggers that define what happens when the user presses those keys.

For example, in the Navigation Manipulator set the End Navigation Key property and create a Key Navigation Started trigger with a Try Set Focus action that sets focus to the last button in the group when the user presses the End key.
## Using the navigation manipulator in the API


For details, see the `NavigationManipulator` class.
