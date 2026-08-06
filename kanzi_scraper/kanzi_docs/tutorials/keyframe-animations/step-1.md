---
title: Step 1 - Create the animation
source: https://docs.kanzi.com/4.1.0/en/tutorials/keyframe-animations/step-1.html
---

# Step 1 - Create the animation


Kanzi creates keyframe animations by gradually changing the value of the animated properties between keyframes. When creating a keyframe animation that changes the values of the Render Transformation property the attributes of which define the position and size of a node, you create movement keyframe animation. However, you can also create a keyframe animation that changes the values of any other Kanzi property, such as color.

In Kanzi you create keyframe animations in Animation Clip and Animation Data items. To create more complex animations, you can organize animations into Timeline Entry and Timeline Sequence items. See Animations.

In this step of the tutorial you create the keyframe animation and use the Animation Player to play the animation.
## Get the tutorial


To get the tutorial, in the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Keyframe animations tutorial, click .

Kanzi Studio downloads the tutorial to the `<KanziWorkspace>/Tutorials` directory. You can find:

- The tutorial starting point project in the `<KanziWorkspace>/Tutorials/Keyframe animations/Start` directory.
- The completed tutorial in the `<KanziWorkspace>/Tutorials/Keyframe animations/Completed` directory.

## Create the animation


In this section you create the keyframe animation that bounces the BeachBall node on top of the Ground node.

To create the animation:

1.

In the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Keyframe animations tutorial, click Open and select Start project.

The project contains a BeachBall Model node and a Ground Plane node.
2.

In the Library > Animations > Animation Clips, double-click the Animation Clip to open it in the Animation Clip Editor.
3.

In the Animation Clip Editor, set the Current Time to 0.
4.

In the Node Tree, select the BeachBall node. From the Properties drag the Render Transformation property and drop it on the Animation Clip in the Animation Clip Editor.

This way you create a keyframe. This keyframe sets the position of the BeachBall node at the beginning of the animation (the keyframe contains the values of the BeachBall node Render Transformation property attributes).
5.

In the Animation Clip Editor, set the Current Time to 0.45. In the Properties, set the Render Transformation Translation Y property field to 1, and from the Properties drag the Render Transformation property to the Animation Clip in the Animation Clip Editor.

This keyframe sets the position of the BeachBall node as it hits the Ground node.
6.

Set the Current Time to 0.5, scale the BeachBall node on the y axis and move it right on top of the Ground node, and create a keyframe.

Make sure to disable the Uniform option for the Scale attribute and apply the scaling only on the y axis of the BeachBall node.

This keyframe scales the BeachBall node on y axis (the ball squezees as it hits the ground), and positions it right on top of the Ground node.
7.

Set the Current Time to 0.55, return the scale of the BeachBall node to the state before it hit the Ground node, move it right on top of the Ground node, and create a keyframe.

This keyframe returns the BeachBall node to its original size (the ball regains the shape as it bounces), and positions it right on top of the Ground node.
8.

Set the Current Time to 1, move the BeachBall node to its starting position, and create a keyframe.

This keyframe returns the BeachBall node to the position in which it was in the beginning of the animation.

## Play the animation


Use the Animation Player to control a keyframe animation.

To start the animation:

1.

In the Node Tree, select the BeachBall node. In the Node Components, press Alt and right-click Animation and select Animation Player.
2.

In the Animation Player, set:

  - Target Animation Timeline to the Animation Clip.
  - Autoplay Enabled to enabled.

Autoplay Enabled sets whether the animation starts immediately after Kanzi attaches the node with the Animation Player to the node tree.
  - Repeat Count Infinite to enabled.

In the Repeat Count property when you enable the Infinite property, the Animation Player plays the animation infinite amount of times.


In the Preview, you can see the BeachBall bouncing off the Ground.

In the next step, you fine-tune the animation and make the shadow react to the position of the BeachBall.

Introduction Next step
