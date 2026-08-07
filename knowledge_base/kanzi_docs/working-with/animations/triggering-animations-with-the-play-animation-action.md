---
title: Using keyframe animations
source: https://docs.kanzi.com/4.1.0/en/working-with/animations/triggering-animations-with-the-play-animation-action.html
---

# Using keyframe animations


Use the Animation Player to play and control the playback of keyframe animations.
## Playing keyframe animations


To play a keyframe animation:

1.

Create a keyframe animation and a node that you want to animate with that animation. See Creating keyframe animations.
2.

In the Node Tree select the node that you want to animate, in the Node Components press Alt and right-click Animation, and select Animation Player.
3.

In the Animation Player that you created, set the Target Animation Timeline property to the animation that you want to use.
4.

(Optional) In the Animation Player set the animation playback:

  - Autoplay Enabled sets whether the animation starts immediately after Kanzi attaches the node with the Animation Player to the node tree.
  - Relative Playback sets whether the property values set in the animation are added to the property values in the target node or replace the values of these properties.
  - Restore Original Values After Playback sets whether the values of the animated properties return to their initial values when the animation ends.

For example, if the initial value of a property you animate is 0 and at the end of the animation the value is 1, when you enable the Restore Original Values After Playback property, Kanzi returns the value of the animated property to 0 when the animation ends.
  - Playback Mode, Duration Scale, and Repeat Count set in which direction, at what speed, and how many times the animation plays.

To make it easier to reuse an animation, instead of setting these values in an Animation Player, set these values in a Trigger with which you control an animation in a Dispatch Message Action > Animation Player > Start action. See Controlling keyframe animations.


## Controlling keyframe animations


You can control keyframe animations using the animation control actions in any trigger.

To control keyframe animations:

1.

Create a keyframe animation, a node you want to animate with that animation, and add the Animation Player to the node that you want to animate. See Playing keyframe animations.
2.

In the Node Tree create a node where you want to control a keyframe animation in the node that you created in the previous step.

For example, create a Button node.
3.

In the Node Components > Triggers use or create the trigger that you want to use to control the keyframe animation.

For example, use the Button > Click trigger.
4.

In the Node Components > Triggers press Alt and right-click the trigger that you want to use to control the keyframe animation, select Dispatch Message Action > Animation Player and select an action:

  - Start to start an animation
  - Pause to pause a running animation
  - Resume to resume a paused animation
  - Stop to stop a running or paused animation

5.

In the animation control action that you created set the Target Item property to the node that contains the Animation Player that you want to control with this action.

If the node contains more than one Animation Player, set the Target Node Component Name property to the name of the Animation Player that you want to control with this action.

If you want to control all the Animation Player components in a node, leave the Target Node Component Name property empty.
6.

Set the animation playback:

  - Playback Mode property sets how Kanzi plays the animation:

    - Normal plays the animation as it is defined in the animation.
    - Ping pong first plays the animation as it is defined in the animation and then plays the animation in reverse.
    - Reverse plays the animation defined in the animation in reverse.

  - Duration Scale property defines the duration of the animation. For example:

    - When set to 1, the animation is of the same length as it is defined in the animation.
    - When set to 0,5, the animation is half as long as it is defined in the animation.
    - When set to 2, the animation is twice as long as it is defined in the animation.

  - Repeat Count sets how many times the animation is played.

In the Repeat Count property when you enable the Infinite property, the Animation Player plays the animation infinite amount of times.


Kanzi applies the values of the Playback Mode, Duration Scale, and Repeat Count properties in the Animation Player > Start action on top of the values set in the Animation Player.

For example, if in the Animation Player the Playback Mode property is set to Reverse and the Repeat Count property is set to 2, and in the Animation Player > Start action the Playback Mode property is set to Ping pong, the Animation Player plays the animation timeline first twice in reverse and then twice in normal mode.

## Getting information about the animation state


When Animation Player starts, stops, or reaches the end of the animation it plays, it sends messages you can intercept to find out about the state of that animation. For example, you can use these messages to chain animations.

To get information about the animation state:

1.

Create a keyframe animation, a node you want to animate with that animation, and add the Animation Player to the node you want to animate. See Playing keyframe animations.
2.

In the Node Tree select a node where you want to get the information about an animation played by the Animation Player.

For example, if you added the Animation Player to the BeachBall node, but want to get the information about that animation in the RootNode node, select the RootNode node.
3.

In the Node Components press Alt and right-click Triggers, select Message Trigger > Animation Player, and select the message trigger that provides the information that you need:

  - Completed trigger intercepts the message an Animation Player sends when it plays an animation to the end.
  - Started trigger intercepts the message an Animation Player sends when it starts the playback of an animation.
  - Stopped trigger intercepts the message an Animation Player sends when it stops the playback of an animation.

4.

In the message trigger that you created in the previous step, set the Message Source property to the node that has the Animation Player for which you want to find out the state of the animation.

For example, if you want to get the information about the animation of the BeachBall node in the RootNode node, in the Trigger Settings set the Message Source to the BeachBall node.
5.

In the trigger that you created, create the action that you want to use when the Animation Player sends the message that your trigger intercepts.

For example, create an Animation Player > Start action and set it to start another animation.

## Using Animation Player in the API


To create an Animation Player and set its timeline:

```
// Create animation player.
AnimationPlayerSharedPtr animationPlayer = AnimationPlayer::create(domain, "player");
// Set timeline.
animationPlayer->setTimeline(timeline);

```


To attach the Animation Player to a node:

```
node->addNodeComponent(animationPlayer);

```


To start the animation:

```
// Start playback in animation player by sending PlayMessage
// to the node where animation player is attached.
AnimationPlayer::PlayMessageArguments playMessageArguments;
playMessageArguments.setPlaybackMode(Timeline::DirectionBehaviorReverse);
playMessageArguments.setDurationScale(2.0f);
playMessageArguments.setRepeatCount(2);
node->dispatchMessage(AnimationPlayer::PlayMessage, playMessageArguments);

```


To pause the animation:

```
// Pause playback in animation player by sending PauseMessage
// to the node where animation player is attached.
AnimationPlayer::PauseMessageArguments pauseMessageArguments;
node->dispatchMessage(AnimationPlayer::PauseMessage, pauseMessageArguments);

```


To resume the animation:

```
// Resume playback in animation player by sending ResumeMessage
// to the node where animation player is attached.
AnimationPlayer::ResumeMessageArguments resumeMessageArguments;
node->dispatchMessage(AnimationPlayer::ResumeMessage, resumeMessageArguments);

```


To stop the animation:

```
// Stop playback in animation player by sending StopMessage
// to the node where animation player is attached.
AnimationPlayer::StopMessageArguments stopMessageArguments;
node->dispatchMessage(AnimationPlayer::StopMessage, stopMessageArguments);

```


To detach the Animation Player from the node:

```
node->removeNodeComponent(*animationPlayer);

```


For details, see the `AnimationPlayer` class.
## Crossfading animations between states


When your application transitions between states that each drive a different animation, the Animation Player can crossfade between the outgoing and incoming animations. To use crossfading, add an Animation Player with the same name to each state. When the State Manager transitions between the states, it matches the Animation Player components by name, and crossfades between the outgoing and incoming animations over the transition duration.

See Blending animations.
