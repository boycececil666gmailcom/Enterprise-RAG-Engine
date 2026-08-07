---
title: Using spline trajectories
source: https://docs.kanzi.com/4.1.0/en/working-with/trajectories/using-spline-trajectories.html
---

# Using spline trajectories

Use a Spline Trajectory to import a trajectory defined by a set of points and control points in 3D space you created in a third-party tool.

Use trajectories as paths along which Trajectory Layout 3D and Trajectory Layout 2D nodes arrange their child nodes, and along which Trajectory List Box 3D nodes move their items.

You can import and convert curves, including NURBS curves, to Kanzi splines from .fbx files. Make sure that your third-party software exports splines as curves. See Adjusting a spline created from a NURBS curve.
## Creating a spline trajectory

To create a spline trajectory:

1.

Select File > Import > Import 3D Assets and select the .fbx file containing the spline you want to use for a trajectory.
2.

In the Library press Alt and right-click Trajectories and select Spline Trajectory.
3.

In the Properties set the Spline property to the spline you imported.
4.

To take the trajectory into use, in the Node Tree select a Trajectory Layout or a Trajectory List Box 3D node and in the Properties set the Trajectory property to the trajectory you want to use. See Using the Trajectory List Box 3D node and Using the Trajectory Layout nodes.

## Adjusting a spline created from a NURBS curve

When you use a NURBS curve for a spline trajectory you can adjust the number of subdivisions when importing the NURBS curve to Kanzi Studio. Kanzi uses the value you provide to tesselate the NURBS curve as a Kanzi spline. See Using the Trajectory List Box 3D node and Using the Trajectory Layout nodes.

To adjust a spline created from a NURBS curve:

1.

In the Library > Resource Files > 3D Assets select the .fbx file that contains the NURBS curve you are using for a spline trajectory.
2.

In the Properties set the Curve Tesselation Detail property to the number of subdivisions in the NURBS curve you want to use.

The default value is 16. Set the property to different values to find the result that suits you best.
3.

In the Library > Resource Files > 3D Assets right-click the .fbx file that contains the NURBS curve and select Clean Import 3D Asset File.
4.

In the Library > Trajectories select the spline trajectory that uses the NURBS curve you imported and in the Properties set the Spline property to the spline you imported.

## Spline Trajectory property types

For a list of the available property types for spline trajectories, see Spline Trajectory.
