---
title: Using the Key Manipulator
source: https://docs.kanzi.com/4.1.0/en/working-with/input/key-manipulator.html
---

# Using the Key Manipulator


Use the Key Manipulator to set the keys that the user can use to navigate your application. For example, you can override the default focus navigation keys and use a specific key to set focus to a node, set a key to open or close a popup-type window, or move focus in the focus chain.
## Default keyboard navigation keys


These are the default keyboard keys that you can use to move focus in your application:

- Navigate in the forward direction by pressing the Tab key and in the backward direction by pressing the BackTab key or Shift Tab keys.
- The Button nodes have the Focusable property enabled and can receive focus by default. When a Button node has focus, to press that button, you can use the default keyboard keys Space, Enter, and Enter on the numeric pad.
- The Toggle Button nodes have the Focusable property enabled and can receive focus by default. When a Toggle Button node has focus, to press that button, you can use the default keyboard keys Space, Enter, and Enter on the numeric pad.
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


## Using the Key Manipulator triggers


Use the Key Manipulator triggers to react when the user presses or releases a key. For example, you can override the default focus navigation keys and use a specific key to set focus to a node, show or hide an overlay, or move focus in the focus chain. See Default keyboard navigation keys.

The Key Manipulator has these triggers:

- Key Pressed trigger is set off when the user presses a specific key on their keyboard.
- Key Released trigger is set off when the user releases a specific key on their keyboard.
- Key Canceled trigger is set off when the user cancels a key press gesture.


To use the Key Manipulator triggers:

1.

Add and configure a Key Manipulator:

  1.

Select a node that you want to receive input from a specific key.

For example, to hide an overlay with a specific key, select the node that represents that overlay. When you hide the overlay, Kanzi moves the focus to the previously focused user interface element. See Using focus.
  2.

In the Node Components press Alt and right-click Input Manipulators, and select Key Manipulator.

You use the Key Manipulator to set a node to react to input from a key.
  3.

In the Key Manipulator set:

    - Logical Key to the key to which you want the node to react.

For example, to hide an overlay when the user presses the Enter key, set the Logical Key to Enter.
    - (Optional) Key Modifiers to the modifier keys to which you want the node to react.

For example, to set the node to react when the user presses the Ctrl key and the key that you set in the Logical Key property, set the Key Modifiers to Control.


2.

In the Node Components add one of the Key Manipulator triggers.

For example, in the Node Components press Alt and right-click Triggers, and select Message Trigger > Key Input > Key Pressed.
3.

To close an overlay when the user presses a key, in the Key Pressed trigger create an action that hides the overlay. See Creating an overlay.
4.

(Optional) To set how the Key Pressed trigger handles key press repeats, in the trigger define a trigger condition for the value of the Is Repeat message argument. The Is Repeat message argument indicates whether the key press is a repeat caused by the user holding down a key.

For example, if you set an overlay to both open and close when the user presses the same key, in the Key Pressed trigger create a Trigger Condition, and in the condition set:

  - A

    - Type of A to Message argument
    - Message Argument to Is Repeat

  - Operation to =
  - B

    - Type of B to Fixed
    - Fixed Value to disabled


With this condition you set the trigger to handle the first key press. This way if the application user holds the key down, the overlay does not open and close repeatedly.


When the user presses the key that you set in the Key Manipulator (Enter), the Key Pressed trigger sets off the action which closes the overlay and sets the focus to the previously focused user interface element.
## Using the key manipulator in the API


To handle the press and release of the A key:

```
auto keyManipulator = KeyManipulator::create(getDomain());
anyNode->addInputManipulator(keyManipulator);
keyManipulator->setKey(LogicalKey::A);

auto onKeyPressed = [](auto&)
{
    // Handle the key press.
};
anyNode->addMessageHandler(KeyManipulator::KeyPressedMessage, onKeyPressed);
auto onKeyReleased = [](auto&)
{
    // Handle the key release.
};
anyNode->addMessageHandler(KeyManipulator::KeyReleasedMessage, onKeyReleased);

```


To handle the Left Ctrl modifier key as a key gesture:

```
keyManipulator->setKey(LogicalKey::LeftControl);

```


To handle a key gesture composed of the Shift A keys:

```
keyManipulator->setKey(LogicalKey::A, KeyModifier::Shift);

```


To handle the Left Alt and Left Ctrl modifier keys, set the Left Alt key as the modifier key:

```
keyManipulator->setKey(LogicalKey::LeftControl, KeyModifier::LeftAlt);

```


The key press order matters. Pressing Left Ctrl first and then Left Alt does not result in the same key gesture as pressing first Left Alt, then Left Ctrl. To handle the Left Ctrl + Left Alt key gesture:

```
keyManipulator->setKey(LogicalKey::LeftAlt, KeyModifier::LeftControl);

```


For details, see the `KeyManipulator` class.
