---
title: Using line trajectories
source: https://docs.kanzi.com/4.1.0/en/working-with/trajectories/using-line-trajectories.html
---

# Using line trajectories

Use a Line Trajectory to create a path with a single straight line in 3D space.

Use trajectories as paths along which Trajectory Layout 3D and Trajectory Layout 2D nodes arrange their child nodes, and along which Trajectory List Box 3D nodes move their items.

See Using the Trajectory Layout nodes and Using the Trajectory List Box 3D node.
## Creating a line trajectory

To create a line trajectory:

1.

In the Library press Alt and right-click Trajectories and select Line Trajectory.
2.

In the Properties set these properties:

  - Length to set the length of the trajectory.
  - Direction to set the position of the trajectory in 3D space.

For example:

    - To set the trajectory parallel to the x axis, set X to 1, and Y and Z property fields to 0.
    - To set the trajectory parallel to the y axis, set Y to 1, and X and Z property fields to 0.
    - To set the trajectory diagonally into the I octant, set X, Y, and Z property fields to 1.

3.

To take the trajectory into use, in the Node Tree select a Trajectory Layout or a Trajectory List Box 3D node and in the Properties set the Trajectory property to the trajectory you want to use. See Using the Trajectory List Box 3D node and Using the Trajectory Layout nodes.

## Line Trajectory property types

For a list of the available property types for line trajectories, see Line Trajectory.
