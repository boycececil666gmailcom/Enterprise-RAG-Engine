---
title: Parallel Activity Host
source: https://docs.kanzi.com/4.1.0/en/working-with/activities/pah.html
---

# Parallel Activity Host

Parallel Activity Host can activate more than one of its child Activities at a time. When you activate an Activity, a Parallel Activity Host brings that Activity to the front.

In a Parallel Activity Host you can group Activities, to show the groups in the same order that you defined in the node tree. When you activate an Activity in a group, a Parallel Activity Host brings to the front the Activity in that group. For example, this way you can implement the showing of critical messages, such as engine failure, in front of regular notifications, such as a phone call notification. In both groups a Parallel Activity Host shows the Activities in order of activation.
## Using a Parallel Activity Host

To use a Parallel Activity Host:

1.

In the Activity Browser click  and create a root Parallel Activity Host.

Kanzi Studio creates a Parallel Activity Host node in the RootNode node.
2.

In the Activity Browser below the root Parallel Activity Host click , select Create Activity, and create or assign a prefab to that Activity.

For example, create Activities named Seatbelt, Phone Call, and Engine Failure. For each Activity use the same name for the Activity prefab.

Kanzi Studio creates Activities, adds them to the Parallel Activity Host, and for each Activity creates a prefab in the Prefabs.
3.

Create a node with a trigger that you want to use to activate or deactivate an Activity.

For example, create a Toggle Button node and use the Toggle Button: Toggled On and Toggle Button: Toggled Off triggers.
4.

In the Node Tree select the node that you created in the previous step, in the Node Components > Triggers press Alt and right-click the trigger that you want to use to activate an Activity, select the Activate Activity action, and in the action set:

  - Target Item to the Parallel Activity Host that contains the Activity that you want to activate.
  - Activation Path to the path in the Parallel Activity Host to the Activity that you want to activate.

If you nest Activity nodes in other types of nodes, include in the path only the ancestor Activity nodes.
**Tip:** To get the full activation path to an Activity, in the Activity Browser right-click an Activity and select Copy Activation Path. This command copies the entire path from the top-level Activity Host to that Activity.
The Activity Activation Path contains only Activities and Activity Hosts.
5.
In the Node Components > Triggers press Alt and right-click the trigger that you want to use to deactivate an Activity, select the Deactivate Activity action, and in the action set:
- Activation Path to the path in the Parallel Activity Host to the Activity that you want to deactivate.
If you nest Activity nodes in other types of nodes, include in the path only the ancestor Activity nodes.
- Target Item to the Parallel Activity Host that contains the Activity that you want to deactivate.

In the Preview click the toggle buttons to activate and deactivate the Activities in the Parallel Activity Host.
## Controlling virtualization in a Parallel Activity Host

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

1.

To control virtualization when deactivating an Activity, in the trigger that you created, create a Dispatch Message Action > Activity Host > Deactivate Activity Action.

For example, use this approach to reset the state of application UI shown by an Activity when user cancels a selection and the application deactivates that Activity.

## Controlling Activity persistence in a Parallel Activity Host

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

See Controlling virtualization in a Parallel Activity Host.

You can activate an Activity using:

- An Activate Activity Message. See Activating an Activity with the Activate Activity Message.
- An Apply Activation Action. See Activating Activities with an Apply Activation Action.

### Finding out whether an Activity is active

To find out whether an Activity is active, check the value of the Activity Status property for that Activity node.
### Setting the initially active Activities

To set which Activities in a Parallel Activity Host are initially active:

- In the Activity Browser, select the Activity you want to be active when the Parallel Activity Host becomes active.
- In the side panel, enable the InitiallyActive property.

When you enable the InitiallyActive property for an Activity, the Parallel Activity Host activates it when the Host itself becomes active, without explicitly activating it.

In a Parallel Activity Host, you can enable the InitiallyActive property for multiple Activities.
### Activating an Activity with the Activate Activity Message

Use the Activate Activity Message when:

- The condition for activating an Activity is too complex to be expressed with the value of a property
- You do not know in advance the number of Activities in an Activity Host

To activate an Activity with the Activate Activity Message:

1.

Create an Activity Host with several Activities.
2.

Create a node with a trigger that you want to use to activate an Activity.

For example, create a Toggle Button node and use the Toggle Button: Toggled On and Toggle Button: Toggled Off triggers to activate and deactivate an Activity in a Parallel Activity Host.
3.

In the Node Tree select the node with the trigger that you created in the previous step, in the Node Components > Triggers press Alt and right-click the trigger that you want to use to activate an Activity, select Dispatch Message Action > Activity Host > Activate Activity Message, and in the action set:

  - Target Item to the Activity Host that contains the Activity that you want to activate.
  - Activation Path to the path from the Activity Host to the Activity that you want to activate.

If you nest Activity nodes in other types of nodes, include in the path only the ancestor Activity nodes.
**Tip:** To get the full activation path to an Activity, in the Activity Browser right-click an Activity and select Copy Activation Path. This command copies the entire path from the top-level Activity Host to that Activity.
The Activity Activation Path contains only Activities and Activity Hosts.
4.
To deactivate an Activity in a Parallel Activity Host, repeat the previous step but add the Dispatch Message Action > Activity Host > Deactivate Activity Message to the trigger that you want to use to deactivate that Activity.

In the Preview click the toggle buttons to activate and deactivate the Activities in the Parallel Activity Host.
### Activating Activities with an Apply Activation Action

An Apply Activation Action keeps an Activity activated for as long as the condition is met in a Data Trigger that contains this action. When the trigger condition is no longer met, Kanzi rolls back the state of the Activity to the state before the action was applied. Use the Apply Activation Action only with a Data Trigger.

Use the Apply Activation Action when you want to synchronize the activation of an Activity with your application logic.

For example, use an Apply Activation Action to show a cluster indicator when a property has a specific value, and then hide the same indicator when the value of that property no longer has that value.

When using a Data Trigger, keep in mind that actions of a Data Trigger have higher priority than the actions of any other trigger.

You can learn how use a Data Trigger with a Apply Activation Action to control the activation state of Activities by completing Tutorial: Control application UI.

To activate an Activity with an Apply Activation Action:

1.

In the Activity Browser, create a Parallel Activity Host with an Activity.

For example, create a Parallel Activity Host node with an Activity named LowBattery.
2.

In the Prefabs, add the content that the Activity shows.

For example, add an image for a low battery warning.
3.

(Optional) In the Properties, set the size of the Parallel Activity Host and position of the Activity in the Activity Host.
4.

Create a node with which you want to control the activation state of the Activity that you created in the first step.

For example, from the Asset Packages drag the Slider to the Parallel Activity Host node in the Node Tree. In the Properties, position the Slider in the Activity Host.
5.

Create a Data Trigger with an Apply Activation Action:

  1.

In the Node Tree select the Parallel Activity Host node, in the Node Components press Alt and right-click Triggers, and select Data Trigger.
  2.

In the Data Trigger in the Expression click , in the Node Tree select the Slider, and from the Properties drag the Value property to the Expression field and edit the expression to

```
{@Slider/RangeConcept.Value}<=20

```

This condition expression must evaluate to either `True` or `False`. As a source you can use either a property or a data object from a data source.

Click Save.

This way you set the Data Trigger to execute the Apply Activation Action when the value of the Value property in the Slider equals or is lower than 20.
  3.

In the Data Trigger press Alt and right-click Actions, and select Apply Activation Action.
  4.

In the Apply Activation Action set:

    - Activity Host Path to .
    - Activity Activation Path to LowBattery

The path to the Activity that you set in the Activity Activation Path property is relative to the Activity Host node that you set in the Activity Host Path property.

The Activity Browser indicates that an Activity Host has a Data Trigger with the  icon.
**Tip:** To get the full activation path to an Activity, in the Activity Browser right-click an Activity and select Copy Activation Path. This command copies the entire path from the top-level Activity Host to that Activity.
The Activity Activation Path contains only Activities and Activity Hosts.

In the Preview drag the slider knob:

- When the value of the Value property of the slider equals or is lower than 20, the Data Trigger activates the Activity that you set in the Apply Activation Action.

An Apply Activation Action keeps an Activity activated for as long as the condition is met in a Data Trigger that contains this action.
- When the value of the Value property of the slider equals 21 or higher, the Data Trigger deactivates the Activity that you set in the Apply Activation Action.

When the trigger condition is no longer met, Kanzi rolls back the state of the Activity to the state before the action was applied.
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
## Using Activities in the API

For details, see the `Activity2D`, `Activity3D`, `ParallelActivityHost2D`, and `ParallelActivityHost3D` classes.
