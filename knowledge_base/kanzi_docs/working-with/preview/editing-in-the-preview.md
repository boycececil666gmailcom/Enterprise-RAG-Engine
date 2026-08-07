---
title: Editing your application in the Preview
source: https://docs.kanzi.com/4.1.0/en/working-with/preview/editing-in-the-preview.html
---

# Editing your application in the Preview

Create and position 2D nodes, create and edit Text Block nodes, add triggers, create and position Camera nodes, and zoom and pan around the Preview.

To edit your application in the Preview use the Preview tools.
## The Preview tools

You can use these tools to edit the content in your project:
|

Tool |

Control |

Description |

Shortcut key |
|   |   |

Use the Node tool to select any node. |   |
|  |    |

Move the selected node. |

1 |
|  |    |

Rotate the selected node. |

2 |
|  |    |

Scale the selected node. |

3 |
|  |    |

Click the square to align the selected 2D node to that side. For example, the setting in this image sets the Vertical Alignment property to Top and Horizontal Alignment property to Left. |   |
|  |    |

Stretch the selected 2D node horizontally. Sets the Horizontal Alignment property to Stretch. |   |
|  |    |

Stretch the selected 2D node vertically. Sets the Vertical Alignment property to Stretch. |   |
|  |

 |

Stretch the selected 2D node horizontally and vertically. Sets the Horizontal Alignment and Vertical Alignment properties to Stretch. |   |
|  |

 |

Use the Layout Transformation property fields to place the selected node. For 2D nodes enter the values for the X and Y property fields. See Optimizing the rendering of layouts. |   |
|  |

 |

Use the Render Transformation property fields to place the selected node. For 2D nodes enter the values for the X and Y property fields. See Optimizing the rendering of layouts. |   |
|  |

 |

Use the Layout Height and Layout Width properties to set the size of the selected 2D node. |   |
|  |

 |

Snap the size or position of the selected 2D node to the nearest coordinates of a surrounding node. |   |
|  |

 |

Use the Scale of the Layout Transformation or Render Transformation properties to set the size of the selected node. |   |
|  |

 |

Use the world coordinates to position the selected 3D node. |   |
|  |

 |

Use the local coordinates to position the selected 3D node. |   |
|

 |   |

Grid Layout 2D tool. Click and drag in the Preview to create a Grid Layout 2D. The size of the area you create defines the size of the layout (Layout Width and Layout Height). See Using the Grid Layout nodes. |   |
|

 |   |

Text Block 2D tool. Click and drag in the Preview to create a Text Block 2D. The size of the area you create defines the size of the layout (Layout Width and Layout Height). See Using the Text Block nodes. |   |
|  |

 |

Enter the text that a Text Block 2D shows. |   |
|  |

 |

Click the square to align the text to that side. For example, the setting in this image sets the Text Vertical Alignment property to Top and Text Horizontal Alignment property to Left. |   |
|  |

 |

Select the font size in device independent pixels you want to use for the Text Block 2D node. |   |
|  |

 |

Select the font you want to use for the Text Block 2D node. Note that the dropdown menu lists only the fonts in your current project. See Importing fonts. |   |
|

 |   |

Stack Layout 2D tool. Click and drag in the Preview to create a Stack Layout 2D. The size of the area you create defines the size of the layout (Layout Width and Layout Height). To set the Stack Layout 2D to arrange its items along either x or y axis, create an area that is longer on the axis along which you want the Stack Layout 2D to arrange its items. See Using the Stack Layout nodes. |   |
|

 |   |

Flow Layout 2D tool. Click and drag in the Preview to create a Flow Layout 2D. The size of the area you create defines the size of the layout (Layout Width and Layout Height). See Using the Flow Layout nodes. |   |
|

 |   |

Use the Camera tool to move around the scene using the preview camera and to create and position cameras in your project. See Using the Camera node.
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
    |   |
|  |

 |

Store the current position of the camera to the preview Camera node. |   |
|  |

 |

Reset the camera to the current position of the preview Camera node. |   |
|  |

 |

Create a new Camera node from the current position of the camera. |

J |
|  |

 |

Orbit Camera lets you move around:

- The nodes that you select in the Node Tree.
- The node that you set with the Constraints > Look At property of the camera.
  |   |
|  |

 |

Free Camera lets you move around without attachment to any point. |   |
|  |

 |

Bring the camera to the 3D object selected in the Node Tree or the Preview. |   |
|  |

 |

Select the Camera node through which you want to view the current scene. |   |
|  |

 |

Set the field of view for the camera in degrees when working with 3D nodes. |   |
## Panning and zooming in the Preview

To pan and zoom in the Preview:
|

Action |

Shortcut |
|

Pan |

Click and drag the middle mouse button. |
|

Zoom |

- Use the control in the upper right corner of the Preview:
- Scroll the mouse wheel.
- Press the Shift and Alt keys, and click and drag the left mouse button.
  |
## Resetting the view in the Preview

When you want to return the Preview zoom level to 100% and position your application screen in the center of the Preview, click  or press Ctrl 1 to reset the view in the Preview.
## Taking a screenshot of the Preview

Use the the Screenshot button  to capture the current view of your application as it appears in the Preview. This is useful for product verification, documentation or to use as project thumbnail for example.

In the User Preferences > Advanced tab, set:

- The Default Screenshot location where screenshots are saved.
- The Screenshot background options which controls how the background of the image is filled.

  - Without Background takes the screenshot with a transparent background.
  - With Screen Clear Color takes the screenshot with the Screen Clear Color as background.
**Note:** The Screenshot background options only take effect if the Background Brush and Foreground Brush properties are set to NullBrush and No Brush. If not, the screenshot background will be filled using the Background Brush defined in the Brush property of the node.
- To take a screenshot of the current view in the Preview window, click the Screenshot  button.
A message in the Status Bar indicates that the screenshot was taken successfully. The image is saved in the location you set in the User Preferences, as a `png` file with the project name and date-time stamp as the name.

## Setting anti-aliasing in the Preview

By default, the Kanzi Studio Preview and the Kanzi Application Player on Windows apply anti-aliasing using 4 samples. For both, you can configure the amount of anti-aliasing that you want to use.

If you have a Kanzi application with a C++ application, to see your content in the Kanzi Studio Preview and Kanzi Application Player the same way as when running your Kanzi application on a target device, you can set anti-aliasing in an `application.cfg` file. See Applying anti-aliasing to an entire application.

To set anti-aliasing in the Kanzi Studio Preview for a Kanzi application without a C++ application:

1.

In the Kanzi Studio main menu, select Project > Properties. In the Properties in the Preview section, set the value of the Preview Working Directory property to the directory where you want to store the `application.cfg` to configure the Preview.

For example, set the Preview Working Directory property to `Application Player`. This way, you can apply the same anti-aliasing setting to the Preview and the Kanzi Application Player on Windows. If the `<ProjectName>/Application Player` directory does not yet exist, select File > Export > Export as KZB Player for Windows. See Building and deploying Kanzi applications to Windows from Kanzi Studio.
2.

In the directory that you set in the previous step, create or open the `application.cfg` file. Add and set the `SurfaceSamplesAntialiasing` parameter to the number of anti-aliasing samples that you want the Preview to use.

For example, to disable anti-aliasing in the Preview, in the `application.cfg`, add:

```
SurfaceSamplesAntialiasing = 0

```

3.

In Kanzi Studio, restart the Preview.
