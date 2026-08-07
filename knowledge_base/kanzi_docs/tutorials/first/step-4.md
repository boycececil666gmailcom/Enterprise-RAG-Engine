---
title: Step 4 - Create states for the Car screen
source: https://docs.kanzi.com/4.1.0/en/tutorials/first/step-4.html
---

# Step 4 - Create states for the Car screen

In this step, you use the Kanzi state machine to show the car in your application from different angles and to animate the transition between those states.
## Create the car shadow

In this section, in the Car Settings Activity you adjust the material used for the car shadow.

To create the car shadow:

1.

In the Activity Browser, in the Car Settings Activity, click .

Under the car model you can see a black plane. This is because the alpha blending mode is incorrect for the material used to render the shadow texture.
2.

In the Prefabs, select the Car > RootNode > Shadowplane node. In the Properties, next to the Cluster Material property, click .

This way you go to the properties of the Shadow material.
3.

In the Shadow material Properties, set the Blend Mode property to Alpha: Automatic.

## Create states

In this section, you create different states for the car, each state focusing on a different part of the car. In the next section, you create the UI controls to move between these states.

In Kanzi, the state manager is one of the most important features for creating rich user interfaces.

To create states:

1.

In the Prefabs, double-click the Car Settings Activity to open it in a new Preview tab.

When you open Car Settings on its own in the Preview, the background is black because by default the background of Activities is not set. In this tutorial, the Activities show the background of the Screen > RootNode.
2.

In the Node Tree, select the Car Settings > Viewport 2D > Car > RootNode > Camera_Root node.
3.

In the State Tools window, click Create State Manager to create a state manager in the Camera_Root node.

You can find the State Tools window below the Preview window.

Kanzi Studio creates a new state manager and assigns it to the Camera_Root node.

When the State Tools are active, the Preview tab is orange and you can create states using the State Tools. In this state, Kanzi Studio tracks all property value changes and you can use the State Tools to store these values to states.
4.

In the State Tools click Create State to create a state.

Create three states.
5.

Double-click the name of each state and name the states Brakes, Roof, Suspension.
6.

In the Node Tree, select the Car Settings > Viewport 2D > Car > RootNode > Camera_Root > Camera node.
7.

In the Preview, select the Camera tool  and click .

When you enable this option, Kanzi Studio stores the current position of the free camera to the Camera node you select in the Camera tool dropdown menu.

In this case, this is the Camera node that you selected in the Node Tree.
8.

In the Node Tree, select the Car Settings > Viewport 2D > Car > RootNode > Car node. In the Preview Camera tool, click  to bring the camera closer to the car.
9.

In the Preview, in the Camera tool, use the orbit camera  to set the position of the car. In the State Tools, click  to save the current camera position to that state.

For example, when you are satisfied with the position, in the State Tools in the Brakes state click  to store the current position of the Camera node to that state.

Orbit Camera lets you move around:

  - The nodes that you select in the Node Tree.
  - The node that you set with the Constraints > Look At property of the camera.

To move with the orbit camera, use these controls:

Control |

Description |

Click and drag the left mouse button. |

Rotate |

  - Click and drag the middle mouse button.
  - Press the Space key, and click and drag the left mouse button.

Pan |

  - Scroll the mouse wheel.
  - Press the Shift and Alt keys, and click and drag the left mouse button.

Zoom |

Hold down Alt and click the left mouse button. |

Select or deselect a node. |
10.

Repeat the previous step until you create positions for all states.
11.

In the Preview, click  to enter the Interact mode. In the State Tools, click each state to see what your application looks like in that state.
12.

In the State Tools, click Edit State Manager to deactivate the State Tools.

## Create the controls to transition between states

In this section, you create the controls to transition between the states that you created in the previous section.

To create the controls to transition between states:

1.

In the Node Tree, press Alt and right-click the Car Settings > Viewport 2D node, select Stack Layout 2D, and name it CarControl.
2.

In the Node Tree, select the CarControl node. In the Properties, set the Direction property to Y.

Use the Direction property to set the axis along which you want the Stack Layout node to stack its child nodes.
3.

In the Prefabs, click , create a Button 2D prefab, and in the Button 2D create an Image node.

You use this prefab to control the state manager you created earlier in this step.
4.

In the Prefabs, select the Button 2D > Image node. In the Properties, add and set:

  - Layout Width and Layout Height properties to 100
  - Layout.Item > Vertical Margin property Top and Bottom property fields to 5
  - Next to the Image property click .

This enables you to show a different image for each instance of that prefab in your project.
**Tip:** To add a property, in the Properties, right-click, select Add Property, and select the property that you want to add.
5.
From the Prefabs, drag the Button 2D prefab to the Node Tree and drop it on the Car Settings > Viewport 2D > CarControl node. Drag the prefab three times to create three buttons.
Kanzi Studio instantiates the Button 2D prefabs in the CarControl node.
6.
Select each Button 2D prefab instance, press F2, and rename them to Brakes, Roof, and Suspension.
7.
In the Node Tree, in the CarControl node, select the first of the instantiated Button 2D prefabs:
1.
In the Properties, add the FirstApplication.Button2D.Image property and set it to the StateBrakes image.
2.
In the Node Components, press Alt and right-click Triggers, and select Message Trigger > Button > Click.
3.
In the Node Components, press Alt and right-click the Button: Click trigger, select Dispatch Message Action > State Manager > Go to State, and in the State Manager: Go to State action set:
- Target Item to Prefabs/Car/Car/RootNode/Camera_Root
- State to Camera_Root State Manager/StateGroup/Brakes

8.

Repeat the previous step to set the remaining two Button 2D prefabs:

  - Use the StateRoof and StateSuspension images.
  - Set the Go to State action to point to the states Roof and Suspension.
**Tip:** To add triggers that have a similar setup, in the Node Components:
1.
Right-click a trigger and select Copy.
2.
Select the node where you want to add the trigger, in the Node Components, right-click Triggers, and select Paste.
3.
Edit the trigger and its actions.

In the Preview, when you click the buttons in the CarControl node, Kanzi Studio transitions to that state using the default linear transition. You can adjust the transitions using the State Transition Editor. See Using state transitions.
## Adjust the position of the buttons

In this section, you adjust the position of the buttons that control the states of the car.

To adjust the position of the buttons:

1.

Click the Screen tab under the main menu to show the entire application in the Preview.
2.

In the Activity Browser, activate the Car Settings Activity. In the Prefabs, select the Car Settings > Viewport 2D > CarControl node. In the Properties, add the Transform 2D > Render Transformation property and set:

  - Translation X to 20
  - Translation Y to 75

Previous step Next step
