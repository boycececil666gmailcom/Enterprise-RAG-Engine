---
title: Animations
source: https://docs.kanzi.com/4.1.0/en/working-with/animations/animations.html
---

# Animations

Animations change properties of objects. Animations map input values to output property values.

Kanzi Studio stores animations in the Library > Animations.

In Kanzi you can create keyframe animations that:

- Animate the position of a node by changing the values of properties that define the position of that node. For example, by animating the position you can make a menu appear from the side of your application, or a button bounce when the user clicks it.
- Animate the look and feel of a node by changing the values of properties that define the look and feel of that node. You can animate different property types:

  - Float property types, where you can animate, for example, light intensity, or material color.
  - Boolean property types, where you can animate, for example, values such as visibility when you map a property to the timeline values 0 and 1.

In Kanzi keyframe animations are formed using:

- Animation Data.

Use an Animation Data resource to define the keyframes and target property of a keyframe animation. One Animation Data resource can target only one property or property field. Animation Data resources are independent from the nodes they target. This allows you to reuse Animation Data resources to animate different nodes.

For example, you can use Animation Data objects to create event-driven animations. See Using keyframe animations.

In an Animation Data object each keyframe maps an input value to an output value, which are floating point numbers. Boolean values are mapped so that values less than 1 return false and values that are equal to or greater than 1 return true. Input values can be time or property values, which are used in property-driven animations or bindings.

Kanzi loads keyframes into memory on demand. An animation is kept in the memory while it is used (for example, during an edit operation in the animation clip editor), and saved to disk after the modification is complete. See Editing animation clips.
- Animation Clip and Animation Child Clip.

Use an Animation Clip to combine Animation Data resources into more complex animations. You can reuse the same Animation Data resources in different Animation Clip items. Use an Animation Child Clip to create hierarchical animations.

You can set the hierarchy of target nodes for animation child clips using the Target property. You can set this property using relative paths or, if you set the Reference for Targeting property in the parent clip, absolute paths. If you are using absolute paths, set the reference to the object that the clip is set to target. See Editing animation clips.
- Timeline Entry.

Use a Timeline Entry to manipulate animations, including repetition, scaling, targeting, and blending, and to define the type of animation input: time or property value.

When you set the Reference for Absolute Paths property in a timeline sequence, the timeline entry can track the relative path of the object you set using an absolute path. Set this reference to the object where the sequence is instantiated.

Timeline entries can blend an animation clip they contain. This functionality is used based on hosting timeline sequence level and the entry weight property set in each entry. Entry Weight is defined by Blending Mode and Weight, where Weight is the ratio in which the blending is calculated based on the Blending Mode you selected. If Blending Mode is set to None, blending is not made for the animation. See Editing timeline sequences.
- Timeline Sequence.

Use a Timeline Sequence to combine a set of Timeline Entry resources.

You can also create an animation by incrementing the value of a property type over time using a Float Value Accumulator or an Int Value Accumulator. For example, you can use a Value Accumulator to create a stopwatch or a timer, move a texture on a 3D model, or rotate a 3D model to create an animation. See Incrementing the value of a property type.
**Tip:** In the Kanzi Studio Node Tree window, an indicator next to a node shows when a State Manager, Binding, Data Source Binding, or an Animation overrides the values of some properties in that node.
To navigate to the source of the override in the Kanzi Studio project, right-click the override indicator and select the source you wish to navigate to from the context menu.
## Animation sharing and targeting

Animation sharing means that one animation animates several or a group of nodes. All animations in Kanzi are shared. You can reuse Animation Clip and Animation Data resources in different nodes. See Using keyframe animations.

Target animation takes the animated propertyâs starting value from the nodeâs current property value and the target value from a designated target nodeâs current property value. To use the target animation set a new value for the target nodeâs property and start the animation. As the new animation takes its new starting value from the current property value, the animations run smoothly even if launched in the middle of an ongoing animation.
