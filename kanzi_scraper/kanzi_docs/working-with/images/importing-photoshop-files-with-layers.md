---
title: Importing Adobe Photoshop PSD files
source: https://docs.kanzi.com/4.1.0/en/working-with/images/importing-photoshop-files-with-layers.html
---

# Importing Adobe Photoshop PSD files


You can import Adobe Photoshop PSD files to your Kanzi Studio project and preserve the structure of the PSD file. This allows you to use each layer from a PSD file as a separate node in your Kanzi Studio project.

When you import a PSD file, Kanzi Studio:

1.

Copies the PSD file to the `<ProjectName>/Images` or `<ProjectName>/Tool_project/Images` directory.
2.

Crops the transparent borders from each PSD layer and saves them as png images to the `<ProjectName>/Images` or `<ProjectName>/Tool_project/Images` directory. In Kanzi Studio you can see these files in the Library > Resource Files > Images in a directory with the same name as the PSD file.
3.

In the Prefabs creates an Empty Node 2D node named after the PSD file and a hierarchy of Empty Node 2D nodes corresponding to the structure of the PSD image. Kanzi Studio uses:

  - Empty Node 2D nodes for the PSD layer groups
  - Image nodes for PSD layers
  - Either Image or Text Block 2D nodes for PSD text layers. Which node Kanzi Studio uses depends on the option that you select when you import a PSD file.

4.

Applies transformation to each imported PSD layer using the Render Transformation property to position the nodes to the same position as they are in the PSD file.


For example, when you import a PSD file that contains one layer for the background and another layer that contains a small logo in the corner of the screen, Kanzi Studio creates two png images in your Kanzi Studio project and two Image nodes. Kanzi Studio removes the trashbands from the small logo, meaning that you end up with two images of different sizes. Kanzi Studio positions both nodes in relation to each other using the Render Transformation.

Kanzi Studio does not support all types of Photoshop layers and layer styles. If Kanzi Studio does not import a layer or a style layer, merge or rasterize such layers in Photoshop before you import them to Kanzi Studio.

To maintain pixel precision, use integers for all Kanzi Studio 2D layer transformations and avoid stretching or scaling the content.
## Importing a PSD file


To import a PSD file:

1.

In the Kanzi Studio main menu select File > Import > Import PSD and select the PSD file that you want to import.

Import PSD tool window opens and all layers in that PSD file are selected for importing.
2.

In the right-hand pane select the layers and layer groups that you want to import. If your PSD file contains text layers, you can import them as Kanzi Text Block 2D nodes so that you can edit the text in Kanzi Studio. In the Import psd text layers as option select:

  - Image nodes to import PSD text layers only as Kanzi Image nodes.
  - Text Block 2D nodes to import PSD text layers only as Kanzi Text Block 2D nodes.
  - Image and Text Block 2D nodes inside Empty Node to import PSD text layers as both Kanzi Image and Text Block 2D nodes both stored in an Empty Node 2D node.


> **Tip:** To set your preferred way of importing text layers from PSD files:
>
> 1.
>
> In the main menu select Edit > User Preferences.
> 2.
>
> In the Advanced tab set the value of the Import text layers as setting.
>
> 3.
>
> Click Import.
>
> Kanzi Studio imports the layers that you selected and preserves the rendering of nodes based on the layer hierarchy in the PSD file. The order in which Kanzi renders nodes is set by their order in the Node Tree: Kanzi renders child nodes and sibling nodes lower in the node tree on top of the parent node and sibling nodes that are higher in the node tree. See Configuring nodes for efficient rendering.
>
## Reimporting a PSD file


When you make a change to a PSD file, to bring the changes from the PSD file that you already imported to your Kanzi Studio project, reimport that PSD file.

To reimport a PSD file, in the Library > Resource Files > Images right-click the PSD file where you made changes, and select Reimport PSD.

Kanzi Studio imports the content from the PSD file. When reimporting, Kanzi Studio resets the values of properties that the content in a PSD file sets, such as the Render Transformation property to position the content and the Text property to set the text in a Text Block 2D node. However, Kanzi Studio keeps the values of all the properties that you added after you imported the PSD file.
