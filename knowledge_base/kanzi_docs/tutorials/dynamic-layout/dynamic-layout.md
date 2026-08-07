---
title: Tutorial: Making applications with dynamic layout
source: https://docs.kanzi.com/4.1.0/en/tutorials/dynamic-layout/dynamic-layout.html
---

# Tutorial: Making applications with dynamic layout


In this tutorial you learn how to create user interfaces that respond to the changes of the device screen resolution. A user interface with a dynamic layout looks good and is easy to use regardless of the device and its screen resolution.

This video shows the result of the tutorial.

This tutorial assumes that you understand the basics of working with Kanzi Studio. The best entry points for getting familiar with Kanzi Studio are:

- Tutorial: Getting started with Kanzi Studio
- Tutorial: Create a simple in-vehicle infotainment application

## Get the tutorial


To get the tutorial, in the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Dynamic layout tutorial, click .

Kanzi Studio downloads the tutorial to the `<KanziWorkspace>/Tutorials` directory. You can find:

- The tutorial starting point project in the `<KanziWorkspace>/Tutorials/Dynamic layout/Start` directory.
- The completed tutorial in the `<KanziWorkspace>/Tutorials/Dynamic layout/Completed` directory.

## Content of the starting point project


User interfaces with dynamic layout respond to changes in device screen orientation and resolution. Grid Layout nodes form the base of dynamic layouts. To make your Kanzi application layout dynamic, you have to place inside Grid Layout nodes all content for which you want that it responds to the changes in the screen resolution. Then you set up the Grid Layout nodes so that they position and distribute the content the way you want.

The starting point project contains the two Grid Layout 2D nodes you need to complete this tutorial:

- Player node sets the position and size of the media player application (the content with white background). The node contains three columns:

  - The first and third column are set to Proportional with value 1 so that their size is the same in proportion to each other and the size of the entire Player Grid Layout node. These columns contain the elapsed and remaining times of the currently playing song.
  - The middle column is set to Automatic so that Kanzi sets its size based on the size of the node in that column. This column contains the song information and player controls.

- Controls node sets the position of the song title, artist and album name, and the controls of the player. The columns and rows of the node are set to Proportional with value 1 so that their size is the same in proportion to each other and the size of the entire Controls Grid Layout 2D node.

## Make the layout of the user interface dynamic


In this section you make the layout of the user interface (Player and Controls Grid Layout 2D nodes) respond to the changes of the device screen orientation and resolution.

In this project the RootNode fills the entire device screen. Because the size of the RootNode node changes with the device resolution, use its height and width as a base for setting the dimensions of nodes in your user interface.

To make the layout of the user interface responsive:

1.

In the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Dynamic layout tutorial, click Open and select Start project.
2.

(Optional) In the Preview click  to enter the Analyze mode, right-click , and select Debug objects and Grid cells. This way you visualize the columns and rows of Grid Layout 2D nodes.
3.

Set the size of the Player node:

  1.

In the Node Tree select the Player node, in the Properties click + Add Binding, and in the Binding Editor set:

    - Property to Layout Height
    - Expression to

```
clamp(400, 1200, {@../Node.ActualHeight} - 300)

```


Click Save.

The Player Grid Layout 2D node sets the position and size of the media player application (the content with white background). This binding sets the height of the node based on the height of the RootNode node. You use the clamp binding function to constrain the height of the Player node to be:

    - 300 pixels less than the height of the RootNode node

Because the Vertical Alignment property of the Player node is set to Center, this creates 150-pixel margins on the top and bottom.
    - Always between 400 and 1200 pixels

  2.

In the Properties click + Add Binding and in the Binding Editor set:

    - Property to Layout Width
    - Expression to

```
clamp(500, {@../Node.ActualWidth}, {@../Node.ActualWidth} - 300)

```


Click Save.

This binding sets the width of the Player Grid Layout 2D node based on the width of the RootNode node. You use the clamp binding function to constrain the width of the Player node to be:

    - 300 pixels less than the width of the RootNode node

Because the Horizontal Alignment property of the Player node is set to Center, this creates 150-pixel margins on the left and right.
    - Always at least 500 pixels


4.

Set the size of the Controls node:

  1.

In the Node Tree select the Controls node, in the Properties click + Add Binding, and in the Binding Editor set:

    - Property to Layout Height
    - Expression to

```
{@../Node.Height}

```


Click Save.

The Controls Grid Layout 2D node sets the position and size of the song title, artist and album name, and the controls of the player. This binding sets the height of the Controls node to be the same as the height of the Player node.

> **Tip:** You can start creating a binding for a property by right-clicking a property and selecting Create Binding.
>
> This way you automatically add the property to the Binding Editor.
> 2.
>
> In the Properties click + Add Binding, and in the Binding Editor set:
>
> - Property to Layout Width
> - Expression to
>
> ```
> clamp(500, 1300, {@../Node.Width} - 300)
>
> ```


Click Save.

This binding sets the width of the Controls Grid Layout 2D node based on the width of the Player node. You use the clamp binding function to constrain the width of the Controls node to be:

    - 300 pixels less than the width of the Player node

Because the Horizontal Alignment property of the Controls node is set to Center, this creates 150-pixel margins on the left and right.
    - Always between 500 and 1300 pixels


## Make the content in the user interface responsive


In this section you make the content of the Controls Grid Layout 2D node respond to the changes of the device screen orientation and resolution. That way the controls in the user interface change with changes of the screen resolution.

To make the content in the user interface responsive:

1.

Set the size of the Song list node:

  1.

In the Node Tree select the Song list node, in the Properties click + Add Binding, and in the Binding Editor set:

    - Property to Layout Height
    - Expression to

```
clamp(10, 60, {@../Node.Height} / 20)

```


Click Save.

The Song list Image node is the leftmost control in the player controls. This binding sets the height of the Song list node based on the height of the Controls node. You use the clamp binding function to constrain the height of the Song list node to be:

    - Five percent of the height the Controls node
    - Always between 10 and 60 pixels

  2.

Repeat the previous step for the Layout Width property of the Song list node, and use this binding expression:

```
clamp(10, 60, {@../Node.Width} / 20)

```


Click Save.

This result of this binding is the same as for the binding in the previous step, but sets the Layout Width of the Song list node.

2.

Apply the same bindings you created in the Song list node to the other Image nodes in the Controls node.

> **Tip:** To create the same binding in multiple nodes, in the Node Tree, select the nodes and in the Properties, click + Add Binding, or right-click a property and select Create Binding.
>
> 1.
>
> In the Node Tree select the Song list node, in the Properties right-click Bindings, and select Copy.
> 2.
>
> In the Node Tree select the Back node, press the Shift key and click the More node.
> 3.
>
> In the Properties right-click Bindings and select Paste Binding(s). This way you add and apply the copied bindings to all selected nodes.
>
> 3.
>
> Set the size of the Play node:
>
> 1.
>
> In the Node Tree select the Play node, in the Properties click the Layout Height binding, and in the Binding Editor set Expression to
>
> ```
> clamp(50, 120, {@../../../Node.ActualHeight} / 5)
>
> ```


Click Save.

This binding sets the height of the Play Image node based on the height of the RootNode node. With this binding the size of the Play node changes differently from the other nodes in the Controls node.
  2.

Repeat the previous step for the Layout Width property of the Play node, and use this binding expression:

```
clamp(50, 120, {@../../../Node.ActualWidth} / 5)

```


Click Save.

4.

In Kanzi Studio select File > Export > Export as KZB Player for Windows and open the .exe file of the application in the `<ProjectName>/Application Player` directory.

When you adjust the size of the application window you simulate the changes in the resolution of the device screen. Notice how the size of the user interface changes according to the bindings you created in the project.

## Whatâs next?


In this tutorial you learned how to create a user interface the size of which responds to the changes of the device screen resolution. This project contains Text Block nodes the text of which stays the same regardless of the changes in the device screen resolution. You can use the approach you learned in this tutorial to make the size of the text in the Text Block nodes respond to the changes of the device screen resolution.

You can also:

- Learn how to control the position of gauge needles with custom properties. See Tutorial: Create gauges.
- Learn how to create a cluster indicator and control it with a property. See Tutorial: Create cluster indicators.
