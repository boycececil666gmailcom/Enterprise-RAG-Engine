---
title: Using the Camera node
source: https://docs.kanzi.com/4.1.0/en/working-with/cameras/creating-and-using-cameras-for-previews.html
---

# Using the Camera node

Use the Camera node to show the content of a Scene in Kanzi Studio Preview and in your Kanzi application.

In the Kanzi Studio Preview, you see a Scene through the Camera node that is set as the preview camera of that Scene node. Turning a Camera node into a preview camera.

Do not scale a Camera node, or its ancestor nodes, using the Render Transformation or Layout Transformation property. When you scale a Camera node, you affect the projection so that it does not match the parameters that you set.
## Setting the position of a Camera node

To set the position of a Camera node:

1.

In the Preview, select the Camera tool.
2.

In the Camera tool, you can select the Orbit Camera or Free Camera:

  - Orbit Camera lets you move around:

    - The nodes that you select in the Node Tree.
    - The node that you set with the Constraints > Look At property of the camera.

To move with the orbit camera, use these controls:
|

Control |

Description |
|

Click and drag the left mouse button. |

Rotate |
|

    - Click and drag the middle mouse button.
    - Press the Space key, and click and drag the left mouse button.
  |

Pan |
|

    - Scroll the mouse wheel.
    - Press the Shift and Alt keys, and click and drag the left mouse button.
  |

Zoom |
|

Hold down Alt and click the left mouse button. |

Select or deselect a node. |
  - Free Camera lets you move around without attachment to any point.

To move with the free camera, use these controls:
|

Control |

Description |
|

W |

Move forward.

Hold down Shift to double the speed.  |
|

S |

Move backward.

Hold down Shift to double the speed.  |
|

A |

Move left.

Hold down Shift to double the speed.  |
|

D |

Move right.

Hold down Shift to double the speed.  |
|

Q |

Move up. |
|

E |

Move down. |
|

Click and drag the left mouse button. |

Rotate |
|

Click and drag the middle mouse button. |

Pan |
|

Scroll the mouse wheel. |

Set camera speed.

Scroll down to decrease the camera speed.

Scroll up to increase the camera speed.  |
|

Hold down Alt and click the left mouse button. |

Select or deselect a node. |

3.

When setting the position of a Camera node, use these controls:
|

Control |

Description |
|

 |

Store the current position of the camera to the preview Camera node. |
|

 |

Reset the camera to the current position of the preview Camera node. |
|

 |

Create a new Camera node from the current position of the camera. |
|

 |

Bring the camera to the 3D object selected in the Node Tree or the Preview. |
|

 |

Select the Camera node through which you want to view the current scene. |
|

 |

Set the field of view for the camera in degrees when working with 3D nodes. |
**Tip:** You can control the position of a Camera node when you use the Node tool in the Preview window.
To move with the Orbit Camera, hold down Alt and use these controls:
- Click and drag the left mouse button to rotate.
- Click and drag the middle mouse button to pan.
- Scroll the mouse wheel to zoom.

To move with the Free Camera, hold down the right mouse button and use these controls:

- Move the mouse to tilt and rotate the camera angle in any direction.
- Use W, S, A, and D to move the camera position forward, backward, left, and right.
- Use E and Q to move the camera position up and down.
- Scroll the mouse wheel to set the camera speed.
- Hold down Shift to double the speed when moving.
- Use F to bring the camera to the 3D object selected in the Preview
**Tip:** To place:
- A node to the position of the current view of the Camera in the Preview, in the Node Tree, right-click that node and select Align With View.
- The Preview view to the location of any node, in the Node Tree, right-click that node and select Align View To Selected.

For example, to place a Camera node to the position of any node in a Scene node:

1.

Right-click the node to whose position you want to place a Camera node and select Align View To Selected.
2.

To store that position to the Camera, right-click the Camera and select Align With View.
**Tip:** You can focus the current view of the Camera on the selected node by using the Focus To Selected command from the context menu, or with a double-click (for non-prefab nodes) on the selected node in the node tree.
## Turning a Camera node into a preview camera

In the Kanzi Studio Preview, you see a Scene through the Camera node that is set as the preview camera of that Scene node. By default, the Preview uses the default camera of the Scene.

To turn a Camera node into a preview camera, in the Node Tree either:

- Double-click that Camera node.
- Right-click that Camera node and select Activate Camera in Preview.

When you set the preview camera, Kanzi Studio:

- In the Scene node, sets the Preview Camera property to the Camera node that you turned into the preview camera.
- In the Node Tree, marks the preview camera with (Preview).

Keep in mind that your Kanzi application uses the camera that is set in the Scene node with the Camera property. In the Node Tree, Kanzi Studio marks this camera with (Default).

## Viewing the active Scene from the preset viewpoints

The Camera tool allows you to quickly view the content of an entire Scene from one of the preset viewpoints: front, back, top, bottom, left, or right side. Unless you switch on the option to store the current position of the camera (), the preset viewpoints do not change the position of the Camera nodes in a Scene. See Setting the position of a Camera node.

To view the entire active Scene from a preset viewpoint:

1.

In the Preview, select the Camera tool.
2.

Use these default shortcuts:
|

Preset viewpoint |

Default shortcut |

Shortcut description |
|

View a scene from the left. |

Shift 1 |

Left Camera Preset |
|

View a scene from the right. |

Shift 2 |

Right Camera Preset |
|

View a scene from the top. |

Shift 3 |

Top Camera Preset |
|

View a scene from the bottom. |

Shift 4 |

Bottom Camera Preset |
|

View a scene from the front. |

Shift 5 |

Front Camera Preset |
|

View a scene from the back. |

Shift 6 |

Back Camera Preset |

To set your own shortcut keys, in the main menu, select Edit > User Preferences and there select the Shortcut Keys tab.

## Creating a Camera node

In the Node Tree or Prefabs, you can create a Camera node in a Scene node or any 3D node.

To create a Camera node in the Preview:

1.

In the Preview, select the Camera tool.
2.

Use either the Orbit Camera or Free Camera to move to the location where you want to create a camera. See Setting the position of a Camera node.
3.

Click .

Kanzi Studio creates a Camera node in the position of the camera.
## Setting the projection type of a Camera node

3D projection makes it possible to display 3D objects on a 2D surface.

These projection types are available in Kanzi:

- Perspective projection shows objects closer to the camera larger than those that are further away. This is the default projection type. See Perspective projection.
- Asymmetric perspective projection lets you control the field of view of each angle of a perspective projection. See Asymmetric perspective projection.
- Orthographic projection shows a 2D view of a 3D scene without providing a sense of depth. See Orthographic projection.

### Perspective projection

Use perspective projection to provide a realistic view of a 3D scene. Perspective projection sets a camera to show objects closer to the Camera node larger than those that are further away. This is the projection type most commonly used for 3D scenes, and the default projection type in Kanzi.

To use perspective projection:

1.

Select a Camera node.
2.

In the Properties, add and set:

  - (Optional) Projection Type to Perspective.

This is the default value.
  - FOV Type to set the direction of the field of view:

    - X FOV sets the field of view along the x axis.
    - Y FOV sets the field of view along the y axis. This is the default.

  - FOV to set the field of view of the camera in degrees.

The default is 45 degrees.

### Asymmetric perspective projection

Use asymmetric perspective projection when you want to control the field of view of perspective projection separately toward the left, right, up, and down.

To use asymmetric perspective projection:

1.

Select a Camera node.
2.

In the Properties, add and set:

  - Projection Type to Asymmetric perspective
  - Asymmetric FOV to the field of view toward the left, right, up, and down in degrees.

By default, the field of view extends 45 degrees to the left, right, up, and down.

For example, to match a perspective projection with the default 45-degree field of view along the y axis, set the Asymmetric FOV property:

    - Up property field to -22.5
    - Down property field to 22.5

### Orthographic projection

Use orthographic projection to show a 2D view of a 3D scene without providing a sense of depth. The orthographic projection lines are orthogonal to the projection plane, and the distance from the camera does not affect the drawing size of objects.

To use orthographic projection:

1.

Select a Camera node.
2.

In the Properties, add and set:

  - Projection Type to Orthographic
  - Orthogonal Type to the type of orthogonal coordinate system that you want to use:

    - Absolute sets the camera to display an area whose size matches the size of the parent Viewport 2D node in pixels.
    - Relative sets the camera to display an area whose width is scaled with the value of the Orthogonal Plane Size property. This is the default.

  - Orthogonal Plane Size to set the half width or half height of the view plane of a camera that uses the Relative coordinate system:

    - When FOV Type is set to Y FOV (default value), Orthogonal Plane Size sets the height of the view plane.
    - When FOV Type is set to X FOV, Orthogonal Plane Size sets the width of the view plane.

The default value is 1.0.

## Setting the camera for render passes

When you use render passes to define the rendering of 3D content, you can set in each render pass the Camera node that the render pass and its descendants use to render content. See Rendering.

By default, render passes use the default Camera node in a Scene node to render content. In any render pass, you can add and set the Draw Objects render pass > Camera property. This way, you set the render pass and its descendant render passes to use a specific camera. The value of the Draw Objects render pass > Camera property set in a render pass overrides the value that you set in an ancestor render pass.

For example, in this render pass prefab, all Draw Objects render passes by default use the Camera node set in the Camera property of the Scene node. If you in the Group render pass add and set the Draw Objects render pass > Camera property, all render passes in that render pass prefab use that camera, unless you set their Camera property.

The Draw Objects render pass calculates the values of these properties from the property values of the Camera and passes them to shaders:

- Calculated Camera Matrix sets the `kzCameraMatrix` uniform.
- Calculated Camera Position sets the `kzCameraPosition` uniform.
- Calculated Homogeneous View Position sets the `kzViewPosition` uniform.
- Calculated Projection Matrix sets the `kzProjectionMatrix` uniform.
- Calculated Projection Near And Far Planes sets the `kzCameraNearFarPlane` uniform.

See Shader uniforms.

You can set these properties in a render pass. The values that you set override the property values that you set in the Camera node.
## Using the Camera node in the API

To create a camera with an orthographic projection:

```
// Create a camera named Camera.
CameraSharedPtr camera = Camera::create(domain, "Camera");
// Set the projection of the camera to relative orthogonal.
camera->setOrthogonalProjection(Camera::OrthogonalCoordinateSystemRelative);

// Make the viewing box display [-width,width] x [-1, 1] x [-1, 1] portion of the 3D space.
// The width of the viewing box is determined by the viewport aspect ratio.
camera->setOrthogonalPlaneHeight(1.0f);
camera->setZNear(-1.0f);
camera->setZFar(1.0f);

```

To create a camera with a perspective projection:

```
// Create a camera named Camera.
CameraSharedPtr camera = Camera::create(domain, "Camera");
// Set the projection of the camera to perspective.
camera->setPerspectiveProjection();

// Make the viewing box display a horizontal 90 degree cone of the 3D space.
// The vertical cone angle is determined by the viewport aspect ratio.
camera->setFovType(Matrix4x4::FieldOfViewType::YFov);
camera->setFov(90.0f);
camera->setZNear(0.1f);
camera->setZFar(100.0f);

```

For details, see the `Camera` class.
## Camera property types and messages

For a list of the available property types and messages for the Camera node, see Camera.
