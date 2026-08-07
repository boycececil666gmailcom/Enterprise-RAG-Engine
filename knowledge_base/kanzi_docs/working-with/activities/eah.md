---
title: Exclusive Activity Host
source: https://docs.kanzi.com/4.1.0/en/working-with/activities/eah.html
---

# Exclusive Activity Host

An Exclusive Activity Host can have only one of its child Activities active at a time. When one child Activity of an Exclusive Activity Host is active, all other Activities of that Activity Host are inactive. For example, you can use an Exclusive Activity Host to toggle between views in your application.
## Using an Exclusive Activity Host

To use an Exclusive Activity Host:

1.

In the Activity Browser, click  and create the root Exclusive Activity Host.

Kanzi Studio creates an Exclusive Activity Host as the first child node of the Screen node.
2.

In the Activity Browser, below the root Exclusive Activity Host, click , select Create Activity, and create or assign a prefab to that Activity.

For example, create Activities named Media, Navigation, and Phone. For each Activity use the same name for the Activity prefab.

Kanzi Studio creates Activities, assigns them to the Exclusive Activity Host, and for each Activity creates a prefab in the Prefabs.

Every Activity in the Activity Browser has a prefab. In the Activity Browser when you add an Activity, you either select an existing prefab or create a prefab for your Activity. You can only select prefabs that are of the Activity node type.

Activities that you add in the Activity Browser are not nodes in the application node tree. They are only a visualization of the structure that Kanzi creates once you activate those Activities.
3.

Create a property type that you use in the Exclusive Activity Host to control which Activity is active:

  1.

In the Activity Browser, right-click the Exclusive Activity Host, select Create Controller Property, and select the data type for the property type.

An Exclusive Activity Host uses the Controller Property property to set and control which Activity is active in that Exclusive Activity Host. To change the state of an Activity, you can also use:

    - Any Trigger with the Activate Activity Message
    - A Data Trigger with the Apply Activation Action

For example, select Create Controller Property > Enum to create a property type with the enumeration data type.
  2.

Name the property type, and click OK.

For example, name the property type MyActivities.

Kanzi Studio:

    1.

Creates the property type.

When you create a property type with the enumeration data type, Kanzi Studio creates a property type with enumeration keys with the names from the Activities from that Exclusive Activity Host.
    2.

In the Exclusive Activity Host, adds the created property type and sets the Controller Property property to the created property type.

To set which Activity is active in this Exclusive Activity Host, in the Exclusive Activity Host you can set the value of the created property type.

4.

In the Prefabs, add content to each Activity prefab.

For example, in each Activity create an Image node with the name of that Activity.
5.

In the Activity Browser, set the Controller Property property to the Activity that you want to activate.

The Activity Browser simulates the activation of Activities in your application. To activate Activities in your Kanzi application, use Triggers and Actions. See Activating Activities.

When you activate an Activity, Kanzi:

  1.

Creates an Activity node using its prefab.
  2.

Attaches the Activity node to the node tree.
  3.

Makes the Activity visible.
  4.

Sets the key focus to the Activity, if the Activity Host has key focus and is not configured differently. Controlling whether to set focus to an activating Activity.

## Controlling virtualization in an Exclusive Activity Host

By default, when you deactivate an Activity, Kanzi serializes the values of Activity properties for that Activity and its child Activities. Besides the values of Activity properties that you add, this includes information about the focus and activation state of Activities. Keep in mind that Kanzi does not serialize the runtime state of other, non-Activity properties.

For example, you can preserve the information entered by the user in a Text Box even when an Activity that contains that Text Box is inactive and Kanzi unloads its content. To achieve this, in the Activity that contains a Text Box, create a string Activity Property and create a two-way binding between the Text property of the Text Box and the Activity Property that you created.

You can control virtualization of Activities:

- In an Activity. See Controlling virtualization in an Activity.
- With an Action. See Controlling virtualization with an Action.

### Controlling virtualization in an Activity

With the Preserve History property you can control the serialization of Activity properties in an Activity when Kanzi deactivates that Activity.

To control virtualization in an Activity, in the Activity Browser or Prefabs, select the Activity for which you want to control serialization of Activity property values. In the Properties, add the Preserve History property and set it to:

- Enabled to serialize values of Activity properties. This is the default value.

When you enable serialization and deactivate an Activity, Kanzi preserves the values of the Activity properties for this Activity and its child Activities. When you activate that Activity, Kanzi restores the serialized values of Activity properties in these nodes.
- Disabled to disable serialization of values of Activity properties.

When you disable serialization and deactivate an Activity, Kanzi does not preserve the values of the Activity properties for this Activity and its child Activities. When you activate that Activity, Kanzi resets the values of Activity properties in these nodes.

### Controlling virtualization with an Action

With an Action you can control the serialization of Activity properties in an Activity, before activating or after deactivating that Activity. By default, Kanzi restores the serialized state when you activate an Activity.

To control virtualization with an Action:

1.

In the Activity Browser, Prefabs, or Node Tree, select the node from which you want to control serialization of Activity property values.
2.

In the Node Components, press Alt and right-click Triggers and create a trigger with which you want to control serialization of an Activity.

For example, create an On Attached trigger.
3.

To control virtualization when activating and Activity, in the trigger that you created, press Alt and right-click Actions, select Dispatch Message Action > Activity Host > Activate Activity Action, and in the Action set the Reset History argument to:

  - Disabled to restore the serialized values of Activity properties when the user activates that Activity. This is the default value.
  - Enabled to reset the serialized values of Activity properties when the user activates that Activity.

## Controlling Activity persistence in an Exclusive Activity Host

By default, when you deactivate an Activity, Kanzi detaches the Activity from the node tree and deletes the Activity instance.

With the Keep Activity Alive property you can control Activity persistence when Kanzi deactivates that Activity.

To control Activity persistence, in the Activity Browser or Prefabs, select the Activity for which you want to control persistence. In the Properties, add the Keep Activity Alive property and set it to:

- Detach and Destroy. Kanzi detaches the Activity from the node tree and deletes the Activity instance. This is the default value.
- Hide and Disable. Kanzi hides and disables the Activity, instead of destroying it. When you activate the Activity again, Kanzi restores the hidden Activity and shows the same Activity. This node remains in the same state as it was before deactivating, even if you disable virtualization for this Activity.

This way you can skip Activity instantiation when you activate the Activity again.

## Activating Activities

When you activate an Activity, Kanzi:

1.

Creates an Activity node using its prefab.
2.

Attaches the Activity node to the node tree.
3.

Makes the Activity visible.
4.

Sets the key focus to the Activity, if the Activity Host has key focus and is not configured differently. Controlling whether to set focus to an activating Activity.

By default, when you deactivate an Activity, Kanzi serializes the values of Activity properties for that Activity and its child Activities. Besides the values of Activity properties that you add, this includes information about the focus and activation state of Activities. Keep in mind that Kanzi does not serialize the runtime state of other, non-Activity properties.

See Controlling virtualization in an Exclusive Activity Host.

You can activate an Activity using:

- An Activate Activity Message. See Activating Activities with an Activate Activity Message.
- A Set Property Action. See Activating Activities with a Set Property Action.
- An Navigate To Next Activity and Navigate To Previous Activity Actions. See Activating the next or previous Activity.
- An Apply Activation Action. See Activating Activities with an Apply Activation Action.

### Finding out whether an Activity is active

To find out whether an Activity is active:

- Check the value of the Activity Status property for that Activity.
- Check the value of the Controller Property property in the Exclusive Activity Host for that Activity.

### Setting the initially active Activity

To set which Activity in an Exclusive Activity Host is initially active:

- In the Activity Browser, select the Activity you want to be active when the Exclusive Activity Host becomes active.
- In the side panel, enable the InitiallyActive property.

When you enable the InitiallyActive property for an Activity, the Exclusive Activity Host activates it when the Host itself becomes active, without explicitly activating it. Explicit activation overrides this setting.

In an Exclusive Activity Host, only one Activity can have the InitiallyActive property enabled at a time. If you enable the InitiallyActive property for a different Activity, the property becomes unset on the previous one.
### Activating Activities with an Activate Activity Message

Use the Activate Activity Message when:

- The condition for activating an Activity is too complex to be expressed with the value of a property
- You do not know in advance the number of Activities in an Exclusive Activity Host

To activate an Activity with the Activate Activity Message:

1.

Create an Exclusive Activity Host with several Activities whose activation state you can control with a Controller Property.
2.

Create a node with a Trigger that you want to use to activate an Activity.

For example, create a Button node and use the Button: Click Trigger.
3.

In the Node Tree, select the node that you created in the previous step. In the Node Components > Triggers, press Alt and right-click the Trigger that you want to use to activate an Activity, select Dispatch Message Action > Activate Activity Message, and in the Action set:

  - Target Item to the Exclusive Activity Host that contains the Activity that you want to activate.
  - Activation Path to the path from the Exclusive Activity Host to the Activity that you want to activate.

If you nest Activity nodes in other types of nodes, include in the path only the ancestor Activity nodes.
**Tip:** To get the full activation path to an Activity, in the Activity Browser right-click an Activity and select Copy Activation Path. This command copies the entire path from the top-level Activity Host to that Activity.
The Activity Activation Path contains only Activities and Activity Hosts.

To activate the Activities, in the Preview click the buttons that you created.
### Activating Activities with a Set Property Action

Use the Set Property Action to activate Activities when the logic of your application relies on the value of the Controller Property property to activate an Activity.

To activate an Activity with the Set Property Action:

1.

Create an Exclusive Activity Host with several Activities whose activation state you can control with a Controller Property.
2.

Create a node with a Trigger that you want to use to activate an Activity.

For example, create a Button node and use the Button: Click Trigger.
3.

In the Node Tree, select the node that you created in the previous step. In the Node Components > Triggers, press Alt and right-click the Trigger that you want to use to activate an Activity, select the Set Property Action, and in the Action set:

  - Target Item to the Exclusive Activity Host node that contains the Activity that you want to activate.
  - Target Property to the property type that you set in the Exclusive Activity Host in the Controller Property property.
  - Fixed Value to the value of the Controller Property property that you use in the Activity that you want to activate.

To activate the Activities, in the Preview click the buttons that you created.
### Activating the next or previous Activity

To activate the next or previous Activity:

1.

Create an Exclusive Activity Host with several Activities the activation state of which you can control with a Controller Property.
2.

Create a node with a Trigger that you want to use to activate an Activity.

For example, create a Button node and use the Button: Click Trigger.
3.

In the Node Tree, select the node that you created in the previous step. In the Node Components > Triggers, press Alt and right-click the Trigger that you want to use to activate an Activity, select either Navigate To Next Activity or Navigate To Previous Activity Action, and in the Action set:

  - Target Item to the Exclusive Activity Host that contains the Activities that you want to activate.
  - (Optional) To activate the first or last Activity when you set off the Trigger after you reach the last or first Activity in that Exclusive Activity Host, set the Loop Activity property to enabled.

To activate the Activities, in the Preview click the buttons that you created.
### Activating Activities with an Apply Activation Action

An Apply Activation Action keeps an Activity activated for as long as the condition is met in a Data Trigger that contains this action. When the trigger condition is no longer met, Kanzi rolls back the state of the Activity to the state before the action was applied. Use the Apply Activation Action only with a Data Trigger.

Use the Apply Activation Action when you want to synchronize the activation of an Activity with your application logic.

For example, use an Apply Activation Action to show a cluster indicator when a property has a specific value, and then hide the same indicator when the value of that property no longer has that value.

When using a Data Trigger, keep in mind that Actions of a Data Trigger have a higher priority than the Actions of any other Trigger.

Learn how to use a Data Trigger with an Apply Activation Action to control the activation state of Activities by completing Tutorial: Control application UI.

To activate an Activity with an Apply Activation Action:

1.

In the Activity Browser, create an Exclusive Activity Host with Activities.

For example, create an Exclusive Activity Host node with Activities that show the headlights mode:

  - Automatic

    - In the side panel, enable the InitiallyActive property.

This way you set the Automatic Activity to be active by default.

  - High

2.

In the Prefabs, add the content that the Activities show.

For example, add an image for each headlights mode.
3.

(Optional) In the Properties, set the size of the Exclusive Activity Host and position of the Activities in the Activity Host.
4.

Create a node with which you want to control the activation state of one of the Activities that you created in the first step.

For example, from the Asset Packages, drag the Checkbox to the Exclusive Activity Host node in the Node Tree. In the Properties, position the Checkbox in the Activity Host.
5.

Create a Data Trigger with an Apply Activation Action:

  1.

In the Node Tree, select the Exclusive Activity Host node. In the Node Components, press Alt and right-click Triggers and select Data Trigger.
  2.

In the Data Trigger in the Expression, click . In the Node Tree, select the Checkbox. From the Properties, drag the Toggle State property to the Expression field, and edit the expression to

```
{@Checkbox/ButtonConcept.ToggleState}==1

```

This condition expression must evaluate to either `True` or `False`. As a source you can use either a property or a data object from a data source.

Click Save.

This way you set the Data Trigger to execute the Apply Activation Action when the Checkbox is checked.
  3.

In the Data Trigger, press Alt and right-click Actions and select Apply Activation Action.
  4.

In the Apply Activation Action, set:

    - Activity Host Path to .
    - Activity Activation Path to High

The path to the Activity that you set in the Activity Activation Path property is relative to the Exclusive Activity Host node that you set in the Activity Host Path property.

The Activity Browser indicates that an Exclusive Activity Host has a Data Trigger with the  icon.
**Tip:** To get the full activation path to an Activity, in the Activity Browser right-click an Activity and select Copy Activation Path. This command copies the entire path from the top-level Activity Host to that Activity.
The Activity Activation Path contains only Activities and Activity Hosts.

In the Preview, toggle the checkbox:

- When the checkbox is checked, the value of the Toggle State property in the Checkbox is 1 and the Data Trigger activates the Activity that you set in the Apply Activation Action.

An Apply Activation Action keeps an Activity activated for as long as the condition is met in a Data Trigger that contains this Action.
- When the checkbox is not checked, the value of the Toggle State property in the Checkbox is 0 and the Data Trigger deactivates the Activity that you set in the Apply Activation Action.

When the Trigger condition is no longer met, Kanzi rolls back the state of the Activity to the state before the Action was applied.
**Tip:** During the application development, use these Data Trigger tools in the Activity Browser side panel:
|
Tool |
Description |
|   |
Shows where a Data Trigger is and where the source and target Activitites of that Data Trigger are. |
|   |
Simulates the state when you apply a Data Trigger.
This enables you to see the state of your application when the conditions for a Data Trigger are met without having to change the property values in your application.  |
|   |
Shows the selected Data Trigger in the Node Components window. |
### Activating Activities with a Toggle Button Group

You can use the Toggle Button nodes in a Toggle Button Group to activate Activities in an Activity Host. For example, you can create an application navigation bar to allow the user to switch between application screens.

To activate Activities with a Toggle Button Group:

1.

Create an Activity Host with several Activities whose activation state you control with a Controller Property.

For example, create an Exclusive Activity Host with Activities that show different application screens and use a Controller Property to control which Activity is active. See Using an Exclusive Activity Host.
2.

Create a Toggle Button Group with a Toggle Button node for each Activity that you created in the previous step. See Creating a toggle button group.

In the Toggle Button Group order the Toggle Button nodes in the same order as the enumeration options that you use to control the Activities.
3.

Select the Toggle Button Group, in the Properties click + Add Binding, and in the Binding Editor set:

  - Binding Mode to Two way
  - Property to Current Button Index

You use the Current Button Index property to access the index of the Toggle Button that is toggled on in the Toggle Button Group.
  - Source to the controller property in the Activity Host that controls which Activity is active in that Activity Host.

Click Save.

With this binding you create a two-way connection between the toggle button that is toggled on in the toggle button group and the Activity that is active in the Activity Host.

Now when you activate an Activity, Kanzi toggles on the corresponding Toggle Button, and when you toggle on a Toggle Button, Kanzi activates the corresponding Activity.
## Using a Fallback State

An Exclusive Activity Host works like a UI state machine, where each Activity represents a UI state. To explicitly deactivate an Activity in an Exclusive Activity Host, use a Fallback State. A Fallback State cannot contain any content.

For example, use a Fallback State for auto-closing overlays. Kanzi automatically activates a Fallback State when it detects input outside of Activity boundaries. See Focus.

You can activate a Fallback State with:

- Go To Fallback State message. See Activating Fallback State with Go To Fallback State message.
- The auto-closing modal in a focus scope. See Activating Fallback State with auto-closing modal.
- Any of the approaches for activating an Activity. See Activating Activities.

See Activating Activities.

### Activating Fallback State with Go To Fallback State message

To activate a Fallback State with the Go To Fallback State message:

1.

In the Activity Browser, below an Exclusive Activity Host with several Activities, click , and select Create Fallback State.
2.

Create a UI element that you use to switch to the Fallback State.

For example:

  1.

Create a Button node.
  2.

In Node Components > Triggers, press Alt and right-click the Trigger that you want to use to activate the Fallback State, select Dispatch Message Action > Exclusive Activity Host > Go To Fallback State message, and set the Target Item to the target Exclusive Activity Host.

In the Preview, when you click the button, the Exclusive Activity Host activates the Fallback State.
### Activating Fallback State with auto-closing modal

To activate a Fallback State with the auto-closing modal in a focus scope:

1.

In the Activity Browser, below an Exclusive Activity Host with one or more Activities, click , and select Create Fallback State.
2.

To all Activities, except the Fallback State, add the Focus Scope > Focus Scope Type property and set it to Auto-Closing Modal.

In the Preview, when an Activity to which you added the Focus Scope Type property is active and you click outside of that Activity, the Exclusive Activity Host activates the Fallback State.
## Using Activities in the API

For details, see the `Activity2D`, `Activity3D`, `ExclusiveActivityHost2D`, and `ExclusiveActivityHost3D` classes.
