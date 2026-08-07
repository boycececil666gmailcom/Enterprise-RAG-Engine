---
title: Creating property-driven animations
source: https://docs.kanzi.com/4.1.0/en/working-with/animations/property-driven-animations.html
---

# Creating property-driven animations

Use the Property Driven Animation Player when you want to use a property type instead of time to control a keyframe animation.

For example, with property-driven animations you can control the position of a gauge needle with a property type using a keyframe animation.

To create property-driven animations:

1.

Select or create a keyframe animation.

For example, to create a keyframe animation that you can use to rotate a 2D gauge needle:

  1.

In the Animation Clip Editor, click Create Animation.
**Tip:** Kanzi Studio creates an Animation containing two keyframes automatically, as any animation would require at least two. You can remove, replace, adjust or add to these as needed.
2.
In the Properties, set:
- Target Property to Render Transformation (Node2D.RenderTransformation)
- Property Field to Rotation Z
3.
In the Animation Clip Editor, use the Move tool  to select the animation in the canvas area.
Tip
In this example you create a linear animation which requires only the two keyframes that Kanzi Studio has created automatically. To create a more complex animation, select the Keyframe tool  and click the animation to add more keyframes.
4.
Select the Move tool , select the first keyframe and set:
- Time to 0
In property-driven animations you control the time of the animation with the Time Controller Property Type that you select in the Property Driven Animation Player. You do this in the last step of this procedure.
- Value to the value to which you want to set the animation target property or property field when the value of the controller property is 0
In property-driven animations you control the value of the property set in this animation with the Value property. In this example you control the value of the Node2D.RenderTransformation property, Rotation Z property field.
For example, set Value to -140.
When you set the value to -140, the animation rotates the gauge needle from its original position by 140 degrees in counterclockwise direction.
5.
Select the second keyframe in the animation and set:
- Time to the highest possible value of the property with which you want to control the animation
For example, set Time to 240.
- Value to the value to which you want to set the animation target property or property field when the controller property is at its highest value
For example, set Value to 100.
When you set the value to 100, the animation rotates the gauge needle from its original position by 100 degrees in clockwise direction.

2.

Add the property with which you want to control the animation to the node that you want to control with a property-driven animation.

For example, to create a property type and use it to control the rotation of a speed needle:

  1.

In the Library, press Alt and right-click Property Types and select Property Type.
  2.

In the New Property Type window set:

    - Name to Gauges.Speed
    - Display Name to Speed
    - Data Type to Float
    - Lower Bound to 0
    - Upper Bound to the highest value in your speed gauge

For example, set it to 240.
    - Slider Step to 1

  3.

In the Node Tree select the node that you want to control with a property-driven animation.

For example, select the Image node that shows the speed needle that you want to rotate.
**Tip:** In Kanzi by default the origin of all 2D nodes is in the upper left corner of the node. To set the origin around which you want to rotate the node, in the Properties add the Render Transformation Origin property and set its property fields:
- X to the percentage of the node width you want to set the origin on the x axis
- Y to the percentage of the node height you want to set the origin on the y axis
4.
In the Properties add the property with which you want to control the animation.
For example, add the Speed property that you created.
You must add the property, with which you want to control the animation, to the node where you use the Property Driven Animation Player.
3.
In the Node Components press Alt and right-click Animation, and select Property Driven Animation Player.
4.
In the Property Driven Animation Player that you created set:
- Target Animation Timeline to the Animation Data, Animation Clip, or Timeline Sequence that you want to use for this property-driven animation.
For example, select the animation that you created in the first step in this procedure.
- Time Controller Property Type to the property type that you want the animation to use instead of time.
For example, select the Speed property type that you created.

When you change the value of the property that you set in the Time Controller Property Type, the Property Driven Animation Player changes the value of the property and property field set in the animation. In this example, the Property Driven Animation Player changes the Render Transformation property Rotation property field to rotate the SpeedNeedle node.
## Using Property Driven Animation Player in the API

To create a Property Driven Animation Player and set its timeline and time controller property:

```
// Create property driven animation player.
PropertyDrivenAnimationPlayerSharedPtr player = PropertyDrivenAnimationPlayer::create(domain, "player");
// Set timeline.
player->setTimeline(timeline);
// Set type name of time controller property.
player->setTimeControllerPropertyType(timePropertyType.getName());

```

To attach a Property Driven Animation Player to a node:

```
node->addNodeComponent(player);

```

For details, see the `PropertyDrivenAnimationPlayer` class.
