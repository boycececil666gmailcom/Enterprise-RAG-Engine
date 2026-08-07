---
title: Trajectory list box example
source: https://docs.kanzi.com/4.1.0/en/examples/trajectory-list-box/trajectory-list-box.html
---

# Trajectory list box example


This example shows the use of the Trajectory List Box 3D node to create an interactive scrollable list of items. The example implements a simple gallery of photos with a selection effect using an animation.

The Trajectory List Box 3D node, its Circle Trajectory, content shown in the Trajectory List Box 3D, and animation that highlights the centered photo are created in Kanzi Studio. The point of time at which a highlight-animation is launched is defined based on the scroll speed and focused item data available from the user input events that the trajectory list box component produces.

The Trajectory List Box 3D node in the example uses these features:

- Looping. You can clamp the items in the Trajectory List Box 3D node to the defined trajectory start and end or to transition between the start and end positions, as in this example, with the Looping property.
- Trajectory. To use a trajectory for the Trajectory List Box 3D, you need to create it in the Library > Trajectories. You can create circle and line trajectories in Kanzi Studio. To use a spline trajectory, create a spline in a third-party tool, import it, and add the spline as a Spline Trajectory. See Using circle trajectories, Using line trajectories, and Using spline trajectories. You can customize the trajectory by adding and setting trajectory properties such as Item Area Begin, Item Area End, Cursor Offset, and Override Distance.
- **Selection and target behavior**. Selection and target events are handled separately. The target changed message is generated at the moment the user releases the pointer. It contains the information on the item that is brought to the center with the current trajectory movement. The selection message is generated when a user selects an item by clicking or tapping it. You can select the Bring Center selection behavior in Kanzi Studio. You can define more actions for the target and selection events for any member of the Trajectory List Box 3D, or even the trajectory list box component itself, by setting invoked actions for List Box: Target Changed or List Box: Item Selected triggers.

## Getting the example


To get the example, in the Kanzi Studio Quick Start window, click Projects and select the Examples tab. Next to the Trajectory_list_box example, click .

Kanzi Studio downloads the example to the `<KanziWorkspace>/Examples/Trajectory_list_box` directory.
