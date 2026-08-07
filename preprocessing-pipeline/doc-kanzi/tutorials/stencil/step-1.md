---
title: Step 1 - Create the stencil
source: https://docs.kanzi.com/4.1.0/en/tutorials/stencil/step-1.html
---

# Step 1 - Create the stencil

In this step of the tutorial you create the stencil and prepare the stencil and content for separate rendering. In the next step you use render passes to show of 3D content only an area defined by the shape of the stencil.
## Get the tutorial

To get the tutorial, in the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Stencil tutorial, click .

Kanzi Studio downloads the tutorial to the `<KanziWorkspace>/Tutorials` directory. You can find:

- The tutorial starting point project in the `<KanziWorkspace>/Tutorials/Stencil/Start/Tool_project` directory.
- The completed tutorial in the `<KanziWorkspace>/Tutorials/Stencil/Completed` directory.

This tutorial depends on a plugin from the Data source tutorial.

To get the Data sources tutorial, in the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Data sources tutorial, click .

Kanzi Studio downloads the tutorial to the `<KanziWorkspace>/Tutorials` directory.
## Content of the starting point project

The starting point project contains the content that you need to complete this tutorial:

- The project contains a cluster with contacts list on the left side of the speed gauge. In this tutorial you apply the stencil to this contacts list.

The RootNode > Viewport 2D > ContactsList node contains the list of contacts. The project uses the XML_data_source plugin to get the data for the ContactsList node.
- The Library > Meshes > StencilMesh contains the shape you use to define the area of the ContactsList node that you want to show.

## Create the stencil

In this section you use a Model node to create a stencil which determines the area of the ContactsList node that you want to show.

To create the stencil:

1.

In the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Stencil tutorial, click Open and select Start project.
2.

In the Node Tree press Alt and right-click the RootNode > Viewport 2D > Scene node, select Model, name it Stencil, and in the Properties set the Mesh property to StencilMesh.
3.

In the Node Tree select the Stencil node, in the Properties add the Render Transformation property, and set:

  - Scale property fields to 40
  - Translation X property field to 2
  - Translation Z property field to -1

You set the size and position of the Stencil node in relation to the content in the cluster. In the Preview you can partially see the shape of the red StencilMesh through the gaps between the items in the contacts list.

## Prepare the stencil and content for separate rendering

In this section you use Tag Filter resources to separately pick the Stencil node and the ContactsList node. In the next step of the tutorial you use these filters in the render passes to separate the rendering of the Stencil and ContactsList nodes.

To prepare the stencil and content for separate rendering:

1.

In the Node Tree select the RootNode > Viewport 2D > Scene > Stencil node and in the Properties set the Tags property to Stencil.
**Tip:** Use tags to group, find, and filter nodes in your project. You can assign multiple tags to a single node.
2.
Create a Tag Filter which picks the Stencil node:
1.
In the Library > Rendering press Alt and right-click Object Sources, select Tag Filter, and name it Stencil Filter.
Tag Filter collects 3D nodes that have a specific tag assigned.
2.
In the Properties set the Included Tags property to the Stencil tag. This way you set the filter to pick the nodes that have the Stencil tag. You use this filter in the next step of this tutorial to pick the Stencil node for rendering.
3.
Repeat the previous step but name the Tag Filter Content Filter and in the Properties set the Excluded Tags to the Stencil tag. You set the filter to pick the nodes that do not have the Stencil tag. You use this filter in the next step of this tutorial to collect the ContactsList and Directional Light nodes for rendering.

Introduction Next step
