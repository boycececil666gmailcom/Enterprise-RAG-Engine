---
title: Animations best practices
source: https://docs.kanzi.com/4.1.0/en/best-practices/animations/animations-best-practices.html
---

# Animations best practices

To create more efficient animations:

- Remove the keyframes that do not affect the precision of an animation.
- Remove the Animation Data channels that do not animate anything.
- Avoid excessive use of bezier interpolation between keyframes, because bezier interpolation is more expensive than linear, step, and smooth step interpolation.
- After you import an animation that is heavily sampled, check whether the keyframes are using Bezier interpolation. To significantly reduce the CPU workload, select all keyframes and use linear interpolation. This rarely has an impact on the visual quality of the animation.
- To dynamically change the size of text in a Text Block node, use the Scale property field of either Render Transformation or Layout Transformation properties, instead of the Font Size property. For example, use this approach when you want to animate the size of text in a Text Block node. When you use the Font Size property to dynamically scale the text, Kanzi creates multiple textures for different font sizes and does not release them from the memory.
**Tip:** In the Kanzi Studio Node Tree window, an indicator next to a node shows when a State Manager, Binding, Data Source Binding, or an Animation overrides the values of some properties in that node.
To navigate to the source of the override in the Kanzi Studio project, right-click the override indicator and select the source you wish to navigate to from the context menu.
