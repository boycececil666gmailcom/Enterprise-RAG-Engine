---
title: Animation system
source: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/animation-system.html
---

# Animation system


Animation system allows you to animate properties over time, control playback, map property value changes to animation.

The Kanzi animation system consists:

- Animations define how to animate a property. For example, an animation defines how to animate a color from red to green, or a float value from 7 to 11. In Kanzi you can create these types of animations:
|

From-to animation defines from which to which value to change the value of a property. You can omit either of these values to animate either from the current value or to the current value of the property. From-to animations use an easing curve that defines the rate of change for the animation. You can use one of the easing curves that comes with Kanzi, or define your own. |    |
|

Keyframe animation uses keyframes that define the property value and time at which the animation reaches that value. In Kanzi you can create linear, step, and BÃ©zier spline keyframes. |    |
- Timelines map the animations to time and to objects you want to animate. The animations themselves do not animate an object, the timelines do. In Kanzi you can create these types of timelines:
|

Property timeline applies an animation to a property of an object. For example, to change the layout size of an Image node, use the property timeline to animate the Layout Width and Layout Height properties of the node. |    |
|

Property field timeline applies an animation to one or more fields of a property of an object. For example, you can use a separate animation for each color channel to change the color of the text in a Text Block node. |    |
|

Parallel timeline allows you to group timelines which Kanzi plays at the same time. A parallel timeline ends when the animations in the last child timeline end. Use this timeline to organize collections of timelines and create a composition of timelines.  |    |
- Animation players receive messages that you can send with actions and generate messages that you intercept with triggers. For example, you can send messages to start, stop, and pause playback, and can receive messages to find out when the animation playback started, stopped, or was completed.

In Kanzi these animation players are available:
|   |

Animation Player.

Use the Animation Player to play and control the playback of keyframe animations.

See Using keyframe animations.  |
|   |

Float Value Accumulator.

Use a Float Value Accumulator to increment a value of a float property type or a property field over time or per frame.

See Incrementing the value of a property type.  |
|   |

Int Value Accumulator.

Use an Int Value Accumulator to increment a value of an integer property type over time or per frame.

See Incrementing the value of a property type.  |
|   |

Property Driven Animation Player.

Use the Property Driven Animation Player when you want to use a property type instead of time to control a keyframe animation.

See Creating property-driven animations.  |
|   |

Property Target Interpolator.

Use the Property Target Interpolator when you want to dynamically set the target value for a property and want to interpolate the current value to the target value over time.

See Interpolating property values.  |
|   |

Property Target Easing Interpolator.

Use the Property Target Easing Interpolator when you want to dynamically set the target value for a property and want to interpolate the current value to the target value over time using an easing function. Easing functions enable you to create lifelike animations that offer a more pleasant user experience.

See Interpolating property values using easing functions.  |

## How the property timeline animations work


Property timeline uses the Kanzi property manager modifier stack. Kanzi applies the animation to the base value of the property, or the previous modifier in the stack (which can be another animation). That way you can stack animations that affect the same property.

When the animation ends it remains alive. The object describing the animation still exists so that the modifier can provide the property value when requested. When you use the Kanzi Engine API to apply multiple animations to an object you have to remove them, otherwise they keep consuming resources. Other systems, like the state manager and the Animation Player, keep track of animations themselves, so that you do not need to.

> **Tip:** In the Kanzi Studio Node Tree window, an indicator next to a node shows when a State Manager, Binding, Data Source Binding, or an Animation overrides the values of some properties in that node.
>
> To navigate to the source of the override in the Kanzi Studio project, right-click the override indicator and select the source you wish to navigate to from the context menu.
## The workflow of animating an object


To animate an object:

1.

Create an animation:

  - For a from-to animation set from which to which value you want to animate a property, set the duration of the animation, and the easing curve.
  - For a keyframe animation populate the animation with keyframes that set the value of a property at the time when the animation must reach that value, and use either linear, step, or BÃ©zier spline keyframe.

2.

Create a timeline.
3.

Assign the animation to the timeline.
4.

Play back the animation.
