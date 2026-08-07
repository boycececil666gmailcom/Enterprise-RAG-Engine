---
title: Actions and messages reference
source: https://docs.kanzi.com/4.1.0/en/working-with/triggers/reference-for-actions.html
---

# Actions and messages reference

Here you can find the reference for the actions you can use with triggers in Kanzi Studio. To learn about triggers, see Using triggers.
## Activity Host actions

Use the Activity Host actions to set an Activity Host to activate or deactivate a specific Activity.

Name |

Description |

Activate Activity |

Activates the child Activity that you set in this action. On successful activation, Exclusive Activity Host automatically deactivates the previously active Activity. |

Deactivate Activity |

Deactivates the child Activity that you set in this action. You can use this action only to deactivate an Activity in a Parallel Activity Host. |

To learn about using Activities and Activity Hosts, see:

- Activities
- UI structure

## Apply actions

Use an Apply action when you want to apply a value to a property or activate an Activity node only when a condition expression in an Data Trigger evaluates to true. When the condition expression in that Data Trigger no longer evaluates to true, Kanzi reverts the changes that you set in an Apply action.

You can use an Apply action only in a Data Trigger.

Name |

Description |

Apply Activation Action |

Keeps an Activity node activated for as long as the condition expression is met in a trigger that contains this action. When the trigger condition expression is no longer met, Kanzi rolls back the state of the Activity node to the state before the action was applied. See Activating Activities with an Apply Activation Action. |

Apply Property Action |

Sets a property to the requested value for as long as the condition expression is met in the trigger that sets off this action. When the trigger condition expression is no longer met, Kanzi rolls back the value of that property to the value before this action was applied, or to the value set while Kanzi was applying this action. |

To learn about data triggers, see Data Triggers.

To learn about the Activity nodes, see Activities.
## Animation Player actions

Use the Animation Player actions to control the playback of animations an application.

Name |

Description |

Pause |

Pauses a running animation. |

Resume |

Resumes an animation. |

Start |

Starts an animation. |

Stop |

Stops a running animation. |

To learn about animation actions, see Using keyframe animations.
## Exclusive Activity Host actions

Use the Exclusive Activity Host actions to set an Activity Host to navigate to an Activity.

Name |

Description |

Navigate To Next Activity |

Navigates to the next Activity in an Exclusive Activity Host. |

Navigate To Previous Activity |

Navigates to the previous Activity in an Exclusive Activity Host. |

To learn about using Activities and Activity Hosts, see:

- Activities
- UI structure

## Focus actions

Use the Focus actions to set the application to set focus to a node or to move the focus in the focus chain.

Name |

Description |

Move Focus |

Moves the focus to the next focusable node in the focus chain direction that you set in this action. |

Focus > Move Scope Focus Forward |

Moves the focus to the next focusable node in the forward direction within the focus scope node that you set in this action. |

Focus > Move Scope Focus Backward |

Moves the focus to the next focusable node in the backward direction within the focus scope node that you set in this action. |

Try Set Focus |

Sets the focus to the node that you set in this action. |

To learn about using focus actions, see Using focus.
## General actions

Use the general actions to create interactions based on user input.

Name |

Description |

Move Focus |

Moves the focus to the next focusable node in the focus chain direction that you set in the action. |

Run Lua Script |

Executes the Lua script that you set in the Lua Script property in the action. See Using Lua, Tutorial: Kanzi Engine Lua API basic use, and Kanzi Lua API reference. |

Set Property |

Sets the value of the property that you set in this action. |

Try Set Focus |

Sets the focus to the node that you set in the action. |

Write Log |

Writes a message to the Log window. See Using Write Log action. |

To learn about properties and the Log window, see Tutorial: Getting started with Kanzi Studio.
## List Box actions

Name |

Description |

Move Focus |

Moves the key focus in a List Box node to the Focus Move Target that you set in this action:

- Next focusable item
- Previous focusable item
- Last focusable item
- First focusable item
- Next page in a Grid List Box node
- Previous page in a Grid List Box node

Try Set Focus To List Item |

Sets the key focus in a List Box node to the item at the index that you set in this action. |

To learn about using the List Box nodes, see List Box nodes.
## Page actions
**Note:** The Page and Page Host nodes are deprecated. Use the Activity and Activity Host nodes to build navigable UIs for your application. See Activities.
Use the Page actions to set the application to navigate to a specific Page node.
Name |
Description |
Navigate to Page |
Navigates to the Page node that you set in the action. |
Navigate to Parent |
Navigates to the parent Page Host node of the Page node that you set in the action. |
To learn about using the Page and Page Host nodes, see Using the Page and Page Host nodes.
## Page Host actions
**Note:** The Page and Page Host nodes are deprecated. Use the Activity and Activity Host nodes to build navigable UIs for your application. See Activities.
Use the Page Host actions to navigate to either the previous or next Page node in a Page Host node.
Name |
Description |
Navigate to Next |
Navigates to the next Page node in a Page Host node that you set in the action. |
Navigate to Previous |
Navigates to the next Page node in a Page Host node that you set in the action. |
To learn about using the Page and Page Host nodes, see Using the Page and Page Host nodes.
## Prefab View actions

Use the Prefab View actions to load resources asynchronously from a prefab in your Kanzi application.

Name |

Description |

Start Asynchronous Load |

Starts the asynchronous loading of resources from the prefab you set in the action. |

To learn about loading prefabs asynchronously, see Using node prefabs.
## Scroll View actions

Use the Scroll View actions to set the application to scroll a Scroll View node or a Grid List Box node in a specific direction or to a specific position.

Name |

Description |

Scroll Down |

Sets the scroll delta to one step down and starts scrolling in that direction. Use this action to scroll a Scroll View node or a Grid List Box node. |

Scroll End |

Sets the scroll delta to the end and starts scrolling in that direction. Use this action to scroll a Scroll View node or a Grid List Box node. |

Scroll Home |

Sets the scroll delta to the beginning and starts scrolling in that direction. Use this action to scroll a Scroll View node or a Grid List Box node. |

Scroll Left |

Sets the scroll delta to one step left and starts scrolling in that direction. Use this action to scroll a Scroll View node or a Grid List Box node. |

Scroll Page Down |

Sets the scroll delta to one page down and starts scrolling in that direction. One page equals the layout height of the node that this action targets. Use this action to scroll a Scroll View node or a Grid List Box node. |

Scroll Page Up |

Sets the scroll delta to one page up and starts scrolling in that direction. One page equals the layout height of the node that this action targets. Use this action to scroll a Scroll View node or a Grid List Box node. |

Scroll Right |

Sets the scroll delta to one step right and starts scrolling in that direction. Use this action to scroll a Scroll View node or a Grid List Box node. |

Scroll Up |

Sets the scroll delta to one step up and starts scrolling in that direction. Use this action to scroll a Scroll View node or a Grid List Box node. |

Set Scroll |

Sets the scroll position of a Scroll View node. |

Set Scroll Target |

Sets the scrolling target of a Scroll View node. |

To learn about using the Scroll View nodes, see:

- Using the Scroll View nodes
- Tutorial: Rotate a 3D model
- Scroll view example

To learn about using the Grid List Box nodes, see:

- Using the Grid List Box nodes
- Tutorial: Create a contacts list with a Grid List Box

## State Manager actions

Use the State Manager actions to set the application to enter or leave a specific state.

Name |

Description |

Go to State |

Go to State action sets a state manager to the state that you define in the action. |

Next State |

Sets a State Manager to the next state in the state group that you define in the action. |

Previous State |

Sets a State Manager to the previous state in the state group that you define in the action. |

To learn about using state managers, see Using state managers.
## Theme actions

Use the Theme actions to control themes.

Name |

Description |

Activate Theme |

Activates the theme that you set in the action. |

To learn about using themes, see:

- Using Themes
- Tutorial: Theme your application

## Value Accumulator messages

Use a Value Accumulator to increment a value of a property type over time. You can use the Value Accumulator messages to control the playback of Value Accumulators.

Name |

Description |

Pause |

Pauses the animation applied by a Value Accumulator to its target property value. |

Resume |

Resumes the paused animation applied by a Value Accumulator to its target property value. |

Start |

Starts the animation applied by a Value Accumulator to its target property value. |

Stop |

Starts the animation applied by a Value Accumulator to its target property value and resets the value of the target property to its initial value. |

To learn about using Value Accumulators, see Incrementing the value of a property type.
## Text Box actions

Use the Text Box actions to select and edit text in Text Box nodes.

Name |

Description |

Backspace At Cursor |

Deletes a character using backspace.

For example, in a text that uses a left-to-right script this action deletes the character on the left side of the cursor.  |

Backspace Word At Cursor |

Deletes the characters until the next word boundary using backspace.

For example, in a text that uses a left-to-right script this action deletes the characters between the cursor position and the closest word boundary on the left side of the cursor.  |

Clear Selection |

Clears the current text selection. |

Cancel Text Composition |

Discards the composition text that the user produced in an Input Method Editor (IME).

This action works only when the Text Box node is in the editing state.  |

Commit Composition Text |

Commits the composition text that the user produced in an Input Method Editor (IME).

This action works only when the Text Box node is in the editing state.  |

Delete At Cursor |

Deletes a character using delete.

For example, in a text that uses a left-to-right script this action deletes the character on the right side of the cursor.  |

Delete Selection |

Deletes selected text. |

Delete Text |

Deletes the text between the character indexes that you set in the action using the Start Position and End Position properties. |

Delete Word At Cursor |

Deletes the characters until the next word boundary using delete.

For example, in a text that uses a left-to-right script this action deletes the characters between the cursor position and the closest word boundary on the right side of the cursor.  |

Enter Editing State |

Makes a Text Box node enter the editing state. |

Leave Editing State |

Makes a Text Box node leave the editing state. |

Insert Text |

Inserts text at the character index that you set in the action using the Position property. |

Insert Text At Cursor |

Inserts text at the cursor position.

In the Insert Text At Cursor action set the value of the Text property to the text that you want to insert.  |

Move Cursor Backward |

Moves the cursor one character backward. |

Move Cursor Forward |

Moves the cursor one character forward. |

Move Cursor Home |

Moves the cursor ahead of the first character of the text content. |

Move Cursor To End |

Moves the cursor after the last character of the text content. |

Move Cursor To Next Word |

Moves the cursor forward to the next word boundary. |

Move Cursor To Previous Word |

Moves the cursor backward to the previous word boundary. |

Move Selection End Backward |

Moves the handle that marks the end of a text selection one character backward. |

Move Selection End Forward |

Moves the handle that marks the end of a text selection one character forward. |

Move Selection End One Word Backward |

Moves the handle that marks the end of a text selection one word backward. |

Move Selection End One Word Forward |

Moves the handle that marks the end of a text selection one word forward. |

Move Selection Start Backward |

Moves the handle that marks the beginning of a text selection one character backward. |

Move Selection Start Forward |

Moves the handle that marks the beginning of a text selection one character forward. |

Move Selection Start One Word Backward |

Moves the handle that marks the beginning of a text selection one word backward. |

Move Selection Start One Word Forward |

Moves the handle that marks the beginning of a text selection one word forward. |

Select All |

Selects all text in a Text Box node. |

Select Text |

Selects the text between the character indexes that you set in the action using the Start Position and End Position properties. |

Select To End |

Selects text from the cursor position until the end of the text. |

Select To Home |

Selects text from the start of the text until the cursor position. |

Select Word At Cursor |

Selects a word. |

To learn more about using the Text Box nodes, see Using the Text Box nodes.
