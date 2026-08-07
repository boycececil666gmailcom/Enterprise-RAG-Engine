---
title: Removing redundant Animation Data channels
source: https://docs.kanzi.com/4.1.0/en/best-practices/animations/removing-redundant-animation-data-channels.html
---

# Removing redundant Animation Data channels

Whether importing animations from a third-party tool or creating them in Kanzi, animations sometimes contain Animation Data resources that do not animate anything. For example, when you add a keyframe for a Render Transformation by dragging the property from the Properties to the Animation Clip Editor, Kanzi adds an Animation Data resource for all property attributes, even if they have not changed.

Note that the static values in Animation Data resources have higher precedence than the local property values of the node. When you delete a channel with a static value, the local value becomes effective. Because sometimes even static values (Animation Data resources without any keyframes) contain valid information and are needed, consider cleaning up unnecessary animation information on a case by case basis.

To remove the redundant Animation Data resources:

1.

In the Library select Animations > Animation Clips and select your animation clip.
2.

Right-click the animation clip for which you want to remove the redundant Animation Data resources and select Delete Animations with One or Zero Effective Keyframes.

These images show the same Animation Clip before and after removing the Animation Data resources without effective animations.
