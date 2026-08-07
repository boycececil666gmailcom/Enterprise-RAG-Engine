---
title: Tutorial: Create a Gaussian blur effect
source: https://docs.kanzi.com/4.1.0/en/tutorials/blur/blur.html
---

# Tutorial: Create a Gaussian blur effect

In this tutorial, you learn how to apply a Gaussian blur effect and how to apply that effect when a condition is met.

This video shows the result of the tutorial.

This tutorial assumes that you understand the basics of working with Kanzi Studio. The best entry points for getting familiar with Kanzi Studio are:

- Tutorial: Getting started with Kanzi Studio
- Tutorial: Structure application UI

## Get the tutorial

To get the tutorial, in the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Blur tutorial, click .

Kanzi Studio downloads the tutorial to the `<KanziWorkspace>/Tutorials` directory. You can find:

- The tutorial starting point project in the `<KanziWorkspace>/Tutorials/Blur/Start` directory.
- The completed tutorial in the `<KanziWorkspace>/Tutorials/Blur/Completed` directory.

## Content of the starting point project

The starting point project contains the content that you need to complete this tutorial:

- The Button prefab is a customized version of the Factory Content Button.
- The UpdateContent prefab provides the content for the popup notification.
- The PopupBackground texture provides the background for the popup notification.

## Create the blur effect

In this section, you create the blur effect.

To create the blur effect:

1.

In the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Blur tutorial, click Open and select Start project.

In the Activity Browser, the Root Parallel Activity Host contains the CarScreen Activity that shows:

  - The Car node that shows a 3D car model.
  - The ProfileButton that you use in this tutorial to show a popup notification.
**Tip:** If you cannot see the entire content in the Preview, you can adjust the Preview zoom level in the upper right corner of the Preview.
2.
In the Library, press Alt and right-click Effects and select Blur Effect 2D.
The Blur Effect 2D effect applies a Gaussian blur to the content of a 2D node.
3.
From the Library, drag the Blur Effect 2D effect to the Prefabs and drop it on the CarScreen > Car node.
This way, you set in the Car node the Effect Prefab property to the Blur Effect 2D.
The Blur Effect 2D effect by default applies to a 2D node a blur where the radius of the circular area of pixels that blend to each other is 8 pixels.
4.
Control the amount of blur:
1.
In the Library > Effects, select the Blur Effect 2D effect. In the Properties, next to the Blur Radius property, click . In the Publish Property dialog, click OK.
Kanzi Studio creates from the Blur Radius property a custom property and creates a `##Template` binding to that property in the Blur Effect 2D.
2.
In the Prefabs, select the CarScreen > Car node. In the Properties, add the Blur.BlurEffect2D.Radius property.
Kanzi Studio adds to the Car node a To Source binding which pushes the value of the Blur.BlurEffect2D.Radius property to the Blur Effect 2D instance made available through the `Node2D.Effect` property of the node.

You can now control the amount of blur in the Car node by adjusting the value of the Blur.BlurEffect2D.Radius property in that node.

## Control the blur effect with a state manager

In this section, you create a state manager that you use to control the blur effect in the Car node. You use the state manager to animate the transitions between the normally rendered and blurred states. In the next sections, you create a popup notification and use the state manager to blur the content of the Car node when that notification is shown.

To control the blur effect with a state manager:

1.

In the Prefabs, select the CarScreen > Car node. In the State Tools, click Create State Manager.

Kanzi Studio creates a state manager and assigns it to the Car node.
2.

Click Create State twice to create two states and name them Default and Blur.

You use the Default state to define the state of your application when the Car node is rendered without applying blur, the Blur state when the node is blurred.
3.

Click <No Controller Property>, select + Create Property Type, and set:

  - Name to Blur.BlurScreen
  - Type to Boolean

In a state manager, the value of the property that you select as the Controller Property defines the conditions when each state in a state group is active.
4.

In the Blur state, set the value of the Blur.BlurScreen controller property to True.
5.

In the State Tools, select the Default state and in the Properties, set the Blur.BlurEffect2D.Radius property to 0. In the State Tools in the Default state, click Set to save the value of the Blur.BlurEffect2D.Radius property to that state.

This way, you set the Default state to render the Car without applying the blur.
6.

In the Properties, set the Blur.BlurEffect2D.Radius property to 40. In the State Tools in the Blur state, click Set.

This way, you set the Blur state to apply the blur to the Car.
7.

In the State Tools, click Any -> Any. In the State Transition Settings, set Duration to 500 and click Save.

This way, you set the length of the transition between the Default and Blur states to 500 milliseconds.
8.

Click Edit State Manager to deactivate the state tools.
9.

In the Prefabs, select the CarScreen > Car node. In the Properties, remove the Blur.BlurEffect2D.Radius property.

You remove this property because you use a state manager to control the value of this property.
10.

In the Properties, add the Controller Properties > Blur.BlurScreen property.

When the Blur.BlurScreen property is disabled, Kanzi renders the Car node without applying the blur. In the next sections, you create a popup notification and use the Blur.BlurScreen property to blur the Car when that notification is shown.

## Create a popup notification

In this section, you create a popup notification that you show on top of the CarScreen. In the next section, you blur the content of the Car node when the popup notification is shown.

To create a popup notification:

1.

In the Activity Browser, below the Root Activity Host, click , select Create Activity, and name the Activity and its prefab UpdateNotification.

You use this Activity to show a popup notification on top of the CarScreen Activity.
2.

In the Activity Browser in the UpdateNotification Activity, click .

This way, you simulate the activation of the UpdateNotification Activity so that you can see its content in the Preview.
3.

In the Prefabs, drag the UpdateContent prefab to the UpdateNotification Activity prefab.
4.

In the Prefabs, select the UpdateNotification prefab. In the Properties, add and set:

  - Background Brush to PopupBackground
  - Layout Width to 741
  - Layout Height to 604
  - Horizontal Alignment to Center
  - Vertical Alignment to Center

This way, you set the background and size of the popup, and align the popup to the center of the Root Activity Host.
5.

In the Prefabs, drag the Button prefab to the UpdateNotification prefab.
6.

In the Prefabs, select the UpdateNotification > Button node. In the Properties, add and set:

  - Name to InstallButton
  - Label to Install Now
  - Vertical Alignment to Bottom
  - Layout.Item > Vertical Margin property Bottom property field to 55

In the next section of the tutorial, you use this button to close the popup.
7.

In the Activity Browser, right-click the UpdateNotification Activity and select Add Transition > Fade Out Fade In.

Kanzi Studio creates in the Library > State Managers a state manager that defines the fade-out and fade-in transitions, and sets the UpdateNotification Activity to use it.

The UpdateNotification State Manager > ActivityState state group contains the states that map to the different statuses of Activity nodes. In the Active state, the value of the Opacity property in the UpdateNotification is 1, and in all other states it is 0.
8.

In the Library > State Managers, select the UpdateNotification State Manager > ActivityState state group. In the Properties, remove these state transitions:

  - Inactive â> Activating
  - Deactivating â> Inactive

You keep the state transitions that define the transitions to and from the Active state, where the UpdateNotification Activity has full opacity.

Now when you simulate the activation and deactivation of the UpdateNotification Activity, the popup notification takes 500 milliseconds to fade in and fade out.
## Control the popup notification and the blur effect

In this section, you set the blur effect and the popup notification so that when the notification is shown, the content of the Car node behind the notification is blurred.

To control the popup notification and the blur effect:

1.

Show the notification:

  1.

In the Prefabs, select the CarScreen > ProfileButton node. In the Node Components, press Alt and right-click the Button: Click Trigger and select Dispatch Message Action > Activity Host > Activate Activity.

You use the ProfileButton to activate the Activity that shows the popup notification.
  2.

In the Activate Activity Action, set the Activity Activation Path to UpdateNotification.

The path to the Activity that you set in the Activity Activation Path property is relative to the Activity Host node that you set in the Target Item property.

This way, you set the Button: Click Trigger to execute the Activate Activity Action that activates the UpdateNotification Activity.

Now when in the Preview you click the profile button, the notification pops up.

2.

Close the notification:

  1.

In the Prefabs, select the UpdateNotification > InstallButton node. In the Node Components, press Alt and right-click Triggers and select Message Trigger > Button > Click.
  2.

In the Button: Click Trigger, press Alt and right-click Actions and select Dispatch Message Action > Activity Host > Deactivate Activity. In the Action, set the Activity Activation Path to UpdateNotification.

This way, you set the Button: Click Trigger to execute the Deactivate Activity Action that deactivates the UpdateNotification Activity.

Now when in the Preview you click the Install Now button, the popup closes.

3.

Blur the content of the CarScreen behind the notification:

  1.

In the Prefabs, select the CarScreen Activity. In the Node Components, press Alt and right-click Triggers, select Data Trigger, and name it Popup Blur.

A Data Trigger keeps the Actions in that Data Trigger applied for as long as the condition expression in that Data Trigger is met.
  2.

In the Popup Blur Data Trigger, set the Expression to

```
{../UpdateNotification/ActivityConcept.Status} == 0

```

Click Apply.

You set this Data Trigger to keep an Action in that Data Trigger applied only when in the UpdateNotification Activity, the Activity Status property is Active (enumeration value 0), that is, the Activity is active.
  3.

In the Node Components, press Alt and right-click the Popup Blur Data Trigger, select Apply Property Action, and in the Apply Property Action set:

    - Target Item to Prefab Placeholder 2Ds > Prefabs/CarScreen/CarScreen/Car
    - Target Property to Blur.BlurScreen
    - Fixed Value to enabled

This way, you set the Popup Blur Data Trigger to keep the Blur.BlurScreen property in the Car node enabled when the UpdateNotification Activity is active.

Now when in the Preview you:

- Click the profile button, Kanzi shows the popup notification and applies the blur effect to the car.
- Click the Install Now button, Kanzi closes the popup and renders the car without applying the blur effect.

## Whatâs next?

In this tutorial, you learned how to use the Blur Effect 2D effect and how to apply that effect when a condition is met. Now you can:

- Learn how to use render passes to apply a bloom effect on 3D content. See Tutorial: Create a bloom effect.
- Learn more about using conditions to control the activation state of Activities. See Tutorial: Control application UI.
