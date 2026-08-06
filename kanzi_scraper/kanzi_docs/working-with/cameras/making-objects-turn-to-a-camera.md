---
title: Making nodes turn to a Camera node
source: https://docs.kanzi.com/4.1.0/en/working-with/cameras/making-objects-turn-to-a-camera.html
---

# Making nodes turn to a Camera node


You can set 3D nodes to automatically turn towards a Camera node.

For example, the Plane nodes in the top image automatically turn towards the default camera of the Scene node, while the bottom image shows the same scene, but the nodes do not turn towards a Camera node.

To make nodes turn to a Camera node:

1.

In the Node Tree select the nodes that you want to automatically turn to a Camera node and in the Properties add and set the Constraints > Face to Camera Mode property.

When you set the Face to Camera Mode property, Kanzi by default sets the default camera of the Scene node as the target camera towards which the nodes turn.
|

Look at sets the nodes to rotate along all axes to turn to the target camera. |    |
|

Billboarding sets the nodes to rotate with the rotation of the target camera, keeping the nodes rotated perpendicular to the field of view of the target camera. |    |
|

Cylindrical sets the nodes to turn to the target camera so that they turn around an imaginary cylinder on the y axis, but do not rotate along the x axis. |    |
2.

(Optional) To make any camera in the Scene node the target camera, in the Properties add the Constraints > Face to Camera Target Camera property, and set it to the Camera node towards which you want the nodes to turn.
