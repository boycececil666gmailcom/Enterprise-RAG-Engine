---
title: Tutorial: Animate transitions between Activities
source: https://docs.kanzi.com/4.1.0/en/tutorials/activity-transitions/activity-transitions.html
---

# Tutorial: Animate transitions between Activities

In this tutorial, you learn how to create animated transitions between Activities.

This video shows the result of the tutorial.

This tutorial assumes that you understand the basics of working with Kanzi Studio. The best entry points for getting familiar with Kanzi Studio are:

- Tutorial: Getting started with Kanzi Studio
- Tutorial: Structure application UI

## Get the tutorial

To get the tutorial, in the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Activity transitions tutorial, click .

Kanzi Studio downloads the tutorial to the `<KanziWorkspace>/Tutorials` directory. You can find:

- The tutorial starting point project in the `<KanziWorkspace>/Tutorials/Activity transitions/Start/Tool_project` directory.

To learn about the content of this project and how to create such a project, see Tutorial: Structure application UI.
- The completed tutorial in the `<KanziWorkspace>/Tutorials/Activity transitions/Completed` directory.

## Add a transition between Activities

Activities use a State Manager to define the transitions for status changes. If you do not create a state manager and define transitions, the transitions between Activity statuses are immediate.

In this section, you create an animated transition between Activities.

To add a transition between Activities:

1.

In Kanzi Studio, open the `<KanziWorkspace>/Tutorials/Activity transitions/Start/Tool_project/Activity transitions.proj.kzm` project.

In the Activity Browser, the Cluster > Gauge View > GaugeViewActivityHost > LeftArea > MaximizedMinimizedSwitcher > MaximizedLeft > MaximizedWidget Exclusive Activity Host contains Activities that show battery, music, and navigation widgets.

In the Preview, you can switch between the Activities by clicking the buttons on the left. The transitions between the Activities are immediate.
2.

In the Activity Browser, right-click the WidgetBatteryMaximized Activity, select Add Transition > Flip Horizontal, and name the animation state manager Maximized Widget State Manager.

The Flip Horizontal transition animates the horizontal rotation of an Activity around its center.

When you run this command, Kanzi Studio:

  - Creates in the Library > State Managers the Maximized Widget State Manager with the ActivityState state group whose Controller Property is the Activity Status property. The state group contains the states that map to the different statuses of Activities.

For example, in the Inactive state, the Activity is rotated around its center 180 degrees along the y axis.
  - In the Prefabs > WidgetBatteryMaximized Activity prefab, sets the Resources > State Manager property to the Maximized Widget State Manager.

3.

From the Library > State Managers, drag the Maximized Widget State Manager to the Prefabs and drop it on these Activity prefabs:

  - WidgetMusicMaximized
  - WidgetNavigationMaximized

This way, you add the Maximized Widget State Manager State Manager to all Activities in the MaximizedWidget Exclusive Activity Host. You use the same State Manager to apply the same transition animation to all Activities in an Exclusive Activity Host.

Now, when in the Preview you click the buttons on the left to switch between the Activities, Kanzi applies to them the animated horizontal flip transition.
## Adjust the transition to animate multiple properties

In the previous section, you added a predefined Activity transition. When Kanzi animates a transition between Activities, each Activity goes through one of these sets of states:

- Inactive â> Activating â> Active
- Active â> Deactivating â> Inactive

You can set the property values that Kanzi applies to an Activity in each of these states.

In this section, you:

- Animate the opacity of the Activities during a transition.
- Make the Activities at the same time flip horizontally and scale down and back to their original size.

To adjust the transition to animate multiple properties:

1.

In the Library > State Managers > Maximized Widget State Manager > ActivityState state group, select the Inactive state. In the Properties:

  - In the Perspective Transformation property, set the Scale property fields to 0.5.
  - Add and set the Node > Opacity property to 0.

This way, in the Inactive state, you scale the dimensions of the Activity down to half of their original value and make the Activity completely transparent.
2.

Select the Active state. In the Properties, add and set the Node > Opacity property to 1.

This way, in the Active state, you make the Activity opaque.
3.

Select the Activating and Deactivating states. In the Properties:

  - In the Perspective Transformation property, set the Scale property fields to 0.5.
  - Add and set the Node > Opacity property to 0.2.

This way, in the Activating and Deactivating states, you scale the dimensions of the Activity down to half of their original value and make the Activity look faded.

Now, when you switch between the Activities, the transition animation:

- Flips the Activities horizontally.
- Scales the Activities down and back to their original size.
- Fades out the deactivating Activity and fades in the activating Activity.

## Adjust the curve and speed of the transition

In Kanzi, you can use different easing functions to create more lifelike transition animations that offer a more pleasant user experience. An easing function defines the animation curve, that is, the rate at which a property value changes. By default, Kanzi uses a linear easing function.

In this section, you first animate the change in the size of the Activities with a different easing function. You then adjust the speed of the transition animation.

To adjust the curve and speed of the transition:

1.

In the Library > State Managers > Maximized Widget State Manager, select the ActivityState state group. In the Properties, click the Activating â> Active state transition.
2.

In the State Transition Settings, click  to add a transition animation and set:

  - Property Type to Perspective Transformation
  - Easing Mode to Ease out

This way, you make the animation start out fast and then reduce speed.

The Ease out easing mode is the opposite of the default Ease in easing mode, which makes an animation start out slow and then increase speed.
  - Easing Function to Back

The Back easing function makes the animation go past the target value and return to it, creating a bounce in the animation.
  - Amplitude to 0.5

This way, you set how far past the target value the Back easing function makes the animation go.

Click Save.

With this transition animation, you make the size of the activating Activity increase past the original size, then return to the original size in the Active state. Kanzi applies the default linear transition animation to the opacity and rotation of the Activities.
3.

To adjust the speed of the transition animation:

  1.

In the Properties, click the Inactive â> Activating state transition. In the State Transition Settings, set Duration (ms) to 200 and click Save.

This way, you set the length of the transition from the Inactive state to the Activating state to 200 milliseconds.
  2.

Repeat the previous step for these state transitions:

    - Activating â> Active
    - Active â> Deactivating
    - Deactivating â> Inactive

Now, when you switch between the Activities, Kanzi animates the transitions at a higher speed.

## Whatâs next?

In this tutorial, you learned how to work with the Activity transition animations.

To continue learning how to use animations in Kanzi, you can:

- Learn how to create keyframe animations. See Tutorial: Create keyframe animations.
- Learn how to interpolate property values. See Tutorial: Interpolate property values.
