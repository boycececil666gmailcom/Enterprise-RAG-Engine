---
title: Triggers reference
source: https://docs.kanzi.com/4.1.0/en/working-with/triggers/reference-for-triggers.html
---

# Triggers reference


Here you can find the reference for the triggers you can use in Kanzi Studio. To learn more about triggers, see Using triggers.
## Activity triggers


You can use the Activity triggers in Kanzi Studio with Activity nodes to react when the status of an Activity changes. For example, you can set the application to enter a specific state when a certain Activity is activated.
|

Name |

Description |
|

Activated |

Activated trigger is set off when an Activity is activated. |
|

Activating |

Activating trigger is set off when an Activity is in the activating state. |
|

Deactivated |

Deactivated trigger is set off when an Activity is deactivated. |
|

Deactivating |

Deactivating trigger is set off when an Activity is in the deactivating state. |
|

Status Changed |

Status Changed trigger is set off when the value of the Activity Status property of an Activity changes. |

To learn more about using Activities and Activity Hosts, see:

- Activities
- UI structure

## Activity Host triggers


You can use the Activity Host triggers in Kanzi Studio with Activity Hosts to react when the prefab of an Activity is attached to the node tree. For example, you can set the application to enter a specific state when a certain Activity Host attaches the prefab of its specific child Activity to the node tree.
|

Name |

Description |
|

Activity Prefab Attached |

Activity Prefab Attached trigger is set off when an Activity Host attaches the prefab of the Activity that is activated. |
|

Activity Prefab Detached |

Activity Prefab Detached trigger is set off when an Activity Host attaches the prefab of the Activity that is deactivated. |

To learn more about using Activities and Activity Hosts, see:

- Activities
- UI structure

## Animation triggers


You can use the animation triggers with animations. For example, you can set the application to navigate to a Page or enter a state when an animation has finished playing.
|

Name |

Description |
|

Completed |

Completed trigger intercepts the message an Animation Player sends when it plays an animation to the end. |
|

Started |

Started trigger intercepts the message an Animation Player sends when it starts the playback of an animation. |
|

Stopped |

Stopped trigger intercepts the message an Animation Player sends when it stops the playback of an animation. |

To learn more about creating keyframe animations, see:

- Tutorial: Create keyframe animations
- Using keyframe animations


To learn more about using the Property Driven Animation Player, see Creating property-driven animations.
## Button node triggers


You can use the Button triggers with the Button nodes. For example, you can set the application to activate an Activity when the user presses the button or change the appearance of the button based on user input.
|

Name |

Description |
|

Cancel |

Cancel trigger is set off:

- When the user first presses down the button, then moves the pointer outside of the button area, and lifts the pointer.
- When the user sets off a Long Press trigger.
  |
|

Click |

Button: Click trigger is set off when the user presses down and then releases the button while the pointer is still within the button area. |
|

Down |

Down trigger is set off when the user presses down the button. |
|

Enter |

Enter trigger is set off:

- When the user presses down the button.
- When the user presses down the button, moves the pointer outside of the button area, and then moves the pointer back to the button area while still holding down the pointer.
  |
|

Leave |

Leave trigger is set off:

- When the user presses down the button and then lifts the pointer.
- When the user presses down the button and then moves the pointer outside of the button area.
- When the user sets off a Long Press trigger.
  |
|

Long Press |

Long Press trigger is set off when the user presses down the button and holds the button pressed for the amount of milliseconds defined in the Hold Interval property of that button. |

To learn more about the Button node triggers, see Using the Button nodes.
## Focus triggers


You can use the focus triggers to handle how UI elements in your application receive focus. For example, you can set how an overlay reacts to user input when the user opens that overlay.
|

Name |

Description |
|

About To Gain Focus |

About To Gain Focus trigger is set off before the node to which you add this trigger receives focus. |
|

About To Lose Focus |

About To Lose Focus trigger is set off before the node to which you add this trigger loses focus. |
|

Focus Entered Focus Scope |

Focus Entered Focus Scope trigger is set off to a focus scope node when a node in that focus scope receives focus. |
|

Focus Gained |

Focus Gained trigger is set off when the node to which you add this trigger receives focus. |
|

Focus Left Focus Scope |

Focus Left Focus Scope trigger is set off to a focus scope node when a node in that focus scope loses focus. |
|

Focus Lost |

Focus Lost trigger is set off when the node to which you add this trigger loses focus. |
|

Input Outside Overlay |

Input Outside Overlay trigger is set off to the foremost overlay focus scope when input occurs outside that overlay. |
|

Overlay Brought To Front |

Overlay Brought To Front trigger is set off when an overlay focus scope is brought to the front so that that scope receives focus. |
|

Overlay Gained Focus |

Overlay Gained Focus trigger is set off to an overlay focus scope node when a node in that overlay receives focus. |
|

Overlay Lost Focus |

Overlay Lost Focus trigger is set off to an overlay focus scope node when a node in that overlay loses focus. |
|

Overlay Sent To Back |

Overlay Sent To Back trigger is set off when an overlay focus scope is sent to the back so that that scope does not have focus. |

To learn more about using the focus triggers, see Using focus.
## General triggers


You can use the general triggers in Kanzi Studio with any nodes to react when a node is attached to the node tree, when a property value changes, or at specific time intervals.
|

Name |

Description |
|

Data Trigger |

Data Trigger monitors changes in properties and data source values. Use a Data Trigger to apply a property value of a target node with an Apply Property Action or activate an Activity node with an Apply Activation Action. To learn more about data triggers, see Data Triggers and Activating Activities with an Apply Activation Action. |
|

On Attached |

On Attached trigger is set off when Kanzi attaches the node to the node tree. |
|

On Property Change |

On Property Change trigger is set off when the set property value changes. |
|

On Timer |

On Timer trigger is set off between the time interval you set in the trigger. |
## Input manipulator triggers


You can use the input manipulator triggers to handle the user input, such as gestures and touch events. Use the input manipulator triggers to bind the user input to UI components or application functionality.

Only nodes that have the Hit Testable property enabled can receive input. See Enabling the click gesture for a node.

To learn more about input manipulator triggers, see Handling user input.
### Click Manipulator triggers


Use the Click Manipulator triggers to react to the click gesture. For example, you can change the appearance of a node when the user clicks that node.

You cannot use the Click Manipulator triggers with nodes that handle input by default, such as Button and Toggle Button nodes.
|

Name |

Description |
|

Click |

Click trigger is set off when the user presses and releases a node while the pointer is still within the node area and Kanzi does not recognize another gesture. |
|

Begin |

Begin trigger is set off when the user presses a node. |
|

Cancel |

Cancel trigger is set off:

- When the user first presses a node, then moves the pointer outside of the node area, and lifts the pointer.
- When the focus moves away from the node during the click gesture.
- When Kanzi sets off a Long Press trigger.
  |
|

Enter |

Enter trigger is set off:

- When the user presses a node.
- When the user presses a node, moves the pointer outside of the node area, and then moves the pointer back to the node area while still holding down the pointer.
  |
|

Leave |

Leave trigger is set off:

- When the user presses a node and releases the press.
- When the user sets off a Long Press trigger.
- When the user presses a node and then moves the pointer outside of the node area.
  |

To learn more about using the Click Manipulator, see Using the Click Manipulator.
### Drag-And-Drop Manipulator triggers


Use the Drag-And-Drop Manipulator triggers to react to the drag-and-drop gesture. For example, you can set the appearance of a node when the user drags and drops that node.
|

Name |

Description |
|

Drag and Drop Canceled |

Drag and Drop Canceled trigger is set off when focus moves away from the node during the drag-and-drop gesture. |
|

Drag and Drop Finished |

Drag and Drop Finished trigger is set off when the user ends the drag-and-drop gesture by lifting their finger or releasing the mouse button. |
|

Drag and Drop Moved |

Drag and Drop Moved trigger is set off when the user drags the node with the drag-and-drop gesture. |
|

Drag and Drop Started |

Drag and Drop Started trigger is set off when the user presses the node long enough for the input manipulator to recognize the drag-and-drop gesture. |

To learn more about using the Drag-And-Drop Manipulator, see:

- Tutorial: Drag and drop
- Using the Drag-And-Drop Manipulator

### Key Manipulator triggers


You can use the Key Manipulator triggers to create interaction with the keyboard. For example, you can set your application to navigate to a Page node or set focus to a node when the user presses a specific key on their keyboard.
|

Name |

Description |
|

Key Canceled |

Key Canceled trigger is set off when the user cancels a key press gesture. |
|

Key Pressed |

Key Pressed trigger is set off when the user presses a specific key on their keyboard. |
|

Key Released |

Key Released trigger is set off when the user releases a specific key on their keyboard. |

To learn more about using the Key Manipulator triggers, see Using the Key Manipulator.
### Long-Press Manipulator triggers


Use the Long-Press Manipulator triggers to react to the long-press gesture. For example, you can change the appearance of a node when the user clicks and holds the click on that node for the amount of time set in that trigger.

You cannot use the Long-Press Manipulator triggers with nodes that handle input by default, such as Button and Toggle Button nodes.
|

Name |

Description |
|

Long Press |

Long Press trigger is set off when the user presses down in the node area and holds the node pressed for 500 milliseconds or the amount of milliseconds set by the Long Press Duration property of the Long-Press Manipulator in that node. |
|

Long Press Cancel |

Long Press Cancel trigger is set off when focus moves away from the node during the long-press gesture. |

To learn more about using the Long-Press Manipulator, see:

- Tutorial: Pan, zoom, tap
- Using the Long-Press Manipulator

### Multi-Click Manipulator triggers


Use the Multi-Click Manipulator triggers to react to the multi-click gesture. For example, you can change the appearance of a node when the user clicks that node multiple times consecutively.

You cannot use the Multi-Click Manipulator triggers with nodes that handle input by default, such as Button and Toggle Button nodes.
|

Name |

Description |
|

Intermediate Click |

Intermediate Click trigger is set off when the user clicks in the node area during the multi-click gesture before the desired click count is reached. |
|

Multi-Click |

Multi-Click trigger is set off when the user clicks multiple times in the node area. |
|

Multi-Click Canceled |

Multi-Click Canceled trigger is set off when focus moves away from the node during the multi-click gesture. |

To learn more about using the Multi-Click Manipulator, see:

- Tutorial: Pan, zoom, tap
- Using the Multi-Click Manipulator

### Navigation Manipulator triggers


You can use the Navigation Manipulator triggers to create directional keyboard navigation. For example, you can set your application to move focus to the next node in the focus chain when the user presses a specific key on their keyboard.
|

Name |

Description |
|

Key Navigation Canceled |

Key Navigation Canceled trigger is set off when Kanzi recognizes the cancellation of the key-pressed gesture for a navigation key. |
|

Key Navigation Finished |

Key Navigation Finished trigger is set off when Kanzi recognizes the key-released gesture for a navigation key.

For example, this happens when the user releases a navigation key on their keyboard.  |
|

Key Navigation Started |

Key Navigation Started trigger is set off when Kanzi recognizes the key-pressed or key repeat gesture for a navigation key.

For example, this happens when the user presses a navigation key on their keyboard.  |

To learn more about using the Navigation Manipulator, see Using the Navigation Manipulator.
### Pan Manipulator triggers


Use the Pan Manipulator triggers to react to the pan gesture. For example, you can set the appearance of a node when the user pans that node.
|

Name |

Description |
|

Pan Canceled |

Pan Canceled trigger is set off when focus moves away from the node during the pan gesture. |
|

Pan Entered |

Pan Entered trigger is set off when the pan gesture enters the node. |
|

Pan Finished |

Pan Finished trigger is set off when the user ends the pan gesture by releasing the mouse button. |
|

Pan Left |

Pan Left trigger is set off when the pan gesture leaves the node. |
|

Pan Moved |

Pan Moved trigger is set off when the user moves a node with the pan gesture. |
|

Pan Started |

Pan Started trigger is set off when the user clicks a node but does not yet drag that node. |

To learn more about using the Pan Manipulator, see:

- Tutorial: Pan, zoom, tap
- Using the Pan Manipulator

### Pinch Manipulator triggers


Use the Pinch Manipulator triggers to react to the pinch gesture. For example, you can set the appearance of a node when the user zooms and rotates the node using the pinch gesture.
|

Name |

Description |
|

Pinch Canceled |

Pinch Canceled trigger is set off when focus moves away from the node during the pinch gesture. |
|

Pinch Finished |

Pinch Finished trigger is set off when the user ends the pinch gesture by lifting their fingers. |
|

Pinch Moved |

Pinch Moved trigger is set off when the user zooms or rotates the node with the pinch gesture. |
|

Pinch Started |

Pinch Started trigger is set off when the user touches the node with two fingers. |

To learn more about using the Pinch Manipulator, see:

- Tutorial: Pan, zoom, tap
- Using the Pinch Manipulator

## List Box triggers


You can use the list box triggers with the List Box nodes. For example, you can set the application to navigate to a Page when the user selects an item in a List Box node.
|

Name |

Description |
|

List Box: Item Loaded |

List Box: Item Loaded trigger is set off when an item in a list box is created and loaded to the working memory.

To set how many items around the visible items you want to keep loaded in the working memory at a time, use the Keep Alive Item Count property.  |
|

List Box: Item Selected |

List Box: Item Selected trigger is set off when the user selects an item in a list box. |
|

List Box: Item Unloaded |

List Box: Item Unloaded trigger is set off when an item in a list box is unloaded from the working memory.

To set how many items around the visible items you want to keep loaded in the working memory at a time, use the Keep Alive Item Count property.  |
|

List Box: Scroll Finished |

List Box: Scroll Finished trigger is set off when the scrolling of a list box ends. |
|

List Box: Scroll Started |

List Box: Scroll Started trigger is set off when the scrolling of a list box starts. |
|

List Box: Scrolled |

List Box: Scrolled trigger is set of whenever a list box scrolls. |
|

List Box: Target Changed |

List Box: Target Changed trigger is set off when the scroll target of a list box changes.

For example, the scroll target changes when the user selects a list box item and the list box scrolls to bring that item to the center of the list box area.  |
|

List Box: User Scroll Finished |

List Box: User Scroll Finished trigger is set off when the user stops scrolling a list box. |
|

List Box: User Scroll Started |

List Box: User Scroll Started trigger is set off when the user starts to scroll a list box. |

To learn more about using the List Box nodes, see:

- Using the Trajectory List Box 3D node
- Using the Grid List Box nodes
- Using the List Box Item Container prefabs
- Tutorial: Create a contacts list with a Grid List Box


For an example of how to use the List Box nodes, see:

- Trajectory list box example
- Virtual list box example

## Page Host triggers


> **Note:** The Page and Page Host nodes are deprecated. Use the Activity and Activity Host nodes to build navigable UIs for your application. See Activities.
>
> Use the Page Host triggers with Page Host nodes. For example, you can set the application to enter a state when a Page Host node starts to navigate to a Page.
> |
>
> Name |
>
> Description |
> |
>
> Page Navigation Finished |
>
> Page Navigation Finished trigger is set off when a Page Host node finishes navigating to a page. |
> |
>
> Page Navigation Started |
>
> Page Navigation Started trigger is set off when a Page Host starts to navigate to a page. |
>
> To learn more about using Page and Page Host nodes, see:
>
> - Using the Page and Page Host nodes
>
## Page triggers


> **Note:** The Page and Page Host nodes are deprecated. Use the Activity and Activity Host nodes to build navigable UIs for your application. See Activities.
>
> Use the Page triggers with Page nodes. For example, you can set the application to set the focus to a node when a Page node is activated.
> |
>
> Name |
>
> Description |
> |
>
> Page Activated |
>
> Page Activated trigger is set off when a Page or Page Host node becomes active. |
> |
>
> Page Deactivated |
>
> Page Deactivated trigger is set off when a Page or Page Host node becomes inactive. |
>
> To learn more about using Page and Page Host nodes, see:
>
> - Using the Page and Page Host nodes
>
## Prefab triggers


You can use the prefab triggers with prefabs. You can use a Prefab View node to load resources asynchronously from a prefab in the project.
|

Name |

Description |
|

Asynchronous Load Completed |

Asynchronous Load Completed trigger is set off when the asynchronous loading of resources from a prefab has been finished. |

To learn more about loading prefabs asynchronously, see Using node prefabs.
## Property Target Interpolator Triggers

|

Name |

Description |
|

Easing Interpolation Completed |

Easing Interpolation Completed trigger intercepts the message a Property Target Easing Interpolator sends when it finishes interpolating the value of the property it interpolates.

See Getting information about completion of an easing interpolation.  |
|

Interpolation Completed |

Interpolation Completed trigger intercepts the message a Property Target Interpolator sends when it finishes interpolating the value of the property it interpolates.

See Getting information about completion of an interpolation  |

To learn more about using the Property Target Interpolator, see:

- Interpolating property values
- Tutorial: Interpolate property values


To learn more about using the Property Target Easing Interpolator, see Interpolating property values using easing functions.
## Range triggers


You can use the range triggers with components which use range properties. For example, you can set the application to set off an action when the user changes the value of a slider.
|

Name |

Description |
|

Value Change Finished |

Value Change Finished trigger is set off when the range value has finished changing. |
|

Value Change Started |

Value Change Started trigger is set off when the range value starts to change. |
|

Value Changed |

Value Changed trigger is set off when the range value changes. |
## Scroll View triggers


You can use the Scroll View triggers with the Scroll View nodes. For example, you can set the application to enter a state or change the value of a property when the user starts to scroll or stops scrolling a scroll view.
|

Name |

Description |
|

Scroll Ended |

Scroll Ended trigger is set off when the scroll position of a scroll view has finished changing. |
|

Scroll Started |

Scroll Started trigger is set off when the scroll position of a scroll view starts to change. |
|

Scroll Zoomed |

Scroll Zoomed trigger is set off when the zoom level of a scroll view changes. |
|

Scrolled |

Scrolled trigger is set off when the scroll position of a scroll view changes. |
|

Snap Request |

Snap Request trigger is set off when a scroll view requests a snapping target from its hosting component. |
|

User Scroll Ended |

User Scroll Ended trigger is set off when the user stops scrolling a scroll view. |
|

User Scroll Started |

User Scroll Started trigger is set off when the user starts to scroll a scroll view. |

To learn more about using the Scroll View nodes, see:

- Using the Scroll View nodes
- Tutorial: Rotate a 3D model


For an example of how to use the Scroll View nodes, see Scroll view example.
## State Manager triggers


You can use the State Manager triggers with State Managers. For example, you can set the application to play an animation when a state manager enters a state.
|

Name |

Description |
|

Entered State |

Entered State trigger is set off when the state manager enters a state. |
|

Left State |

Left State trigger is set off when the state manager leaves a state. |
|

Transition Finished |

Transition Finished trigger is set off when the state manager completes a state transition. |
|

Transition Started |

Transition Started trigger is set off when the state manager starts a state transition. |

To learn more about using state managers, see Using state managers.

To learn more about the Entered State and Left State triggers, see Reacting when a node enters or leaves a state.
## Text Box triggers


You can use the Text Box triggers with the Text Box nodes. For example, you can set the appearance of a Text Box node when the user starts editing the text in that node.
|

Name |

Description |
|

Composition Text Changed |

Composition Text Changed trigger is set off when the Text Input Manipulator updates the text that the user produced in an Input Method Editor (IME). |
|

Composition Text Committed |

Composition Text Committed trigger is set off:

- When the Text Input Manipulator commits the text that the user produced in an Input Method Editor (IME).
- When a trigger executes the Commit Composition Text action.
  |
|

Text Composition Canceled |

Text Composition Canceled trigger is set off:

- When an Input Method cancels a text composition.
- When a trigger executes the Cancel Text Composition action.
  |
|

Cursor Moved |

Cursor Moved trigger is set off when the user moves the cursor in a Text Box node. |
|

Editing Finished |

Editing Finished trigger is set off when a Text Box node leaves the editing state after the user modified the text content.

When you set in a Text Box node the Edit Mode property to Triggered, you can use the Leave Editing State action to set off this trigger.  |
|

Editing Started |

Editing Started trigger is set off when the user starts to edit text in a Text Box node.

When you set in a Text Box node the Edit Mode property to Triggered, you can use the Enter Editing State action to set off this trigger.  |
|

Entered Editing State |

Entered Editing State trigger is set off when a Text Box node enters the editing state. |
|

Left Editing State |

Left Editing State trigger is set off when a Text Box node leaves the editing state. |
|

Input Method Action |

Input Method Action trigger is set off when the user taps the action button on their on-screen keyboard while editing the text in a Text Box node. |
|

Input Method Available |

Input Method Available trigger is set off when an input method becomes available to a Text Box node.

For example, an on-screen keyboard becomes available when it appears on the screen.  |
|

Input Method Unavailable |

Input Method Unavailable trigger is set off when the input method that is composing text in a Text Box node becomes unavailable.

For example, an on-screen keyboard becomes unavailable when the user hides it.  |
|

Selection Changed |

Selection Changed trigger is set off when the user modifies the text selection in a Text Box node. |
|

Selection Cleared |

Selection Cleared trigger is set off when the user deselects the text in a Text Box node. |
|

Selection Started |

Selection Started trigger is set off when the user starts selecting text in a Text Box node. |
|

Text Changed |

Text Changed trigger is set off when the user modifies the text in a Text Box node. |

To learn more about using the Text Box nodes, see Using the Text Box nodes.
## Toggle Button triggers


You can use the Toggle Button triggers with the Toggle Button nodes. For example, you can create a navigation bar with toggle buttons which navigate between Page nodes in the application.
|

Name |

Description |
|

State Toggled |

State Toggled trigger is set off when the toggle state of a Toggle Button node changes. |
|

Toggled Off |

Toggled Off trigger is set off when a Toggle Button node with two states is toggled off. |
|

Toggled On |

Toggled On trigger is set off when a Toggle Button node with two states is toggled on. |

To learn more about using the Toggle Button nodes, see Using the Toggle Button nodes.
## Toggle Button Group triggers


You can use the Toggle Button Group triggers with the Toggle Button Group nodes.
|

Name |

Description |
|

Toggled |

Toggled trigger is set off when the toggle state of a Toggle Button node in a Toggle Button Group node changes. |

To learn more about using the Toggle Button Group nodes, see Using the Toggle Button Group nodes.
