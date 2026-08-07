---
title: Cleaning up your project
source: https://docs.kanzi.com/4.1.0/en/working-with/projects/cleaning-up-a-project.html
---

# Cleaning up your project

In Kanzi Studio you can remove all items in a project that the project does not use. Removing unused items from your project does not always improve the loading times and performance of your Kanzi application. However, it makes optimization of your Kanzi application much easier because it helps you focus on optimizing the correct content.

By removing content that your project does not use you can decrease the size of the kzb file of your project:

- When you complete your project, it is good practice to delete all resources and prefabs that your project is not using. See Deleting the default textures and images and Deleting resources and prefabs that your project is not using.
- If your project does not use a resource or node, you can optimize the size of your Kanzi application by excluding such items. See Excluding items from an application.
- Remove the Animation Data channels that do not animate anything.

See Removing redundant Animation Data channels.
- Delete the temporary files Kanzi Studio generates when you open a project. See Removing generated files.

## Deleting the default textures and images

When you create a project Kanzi Studio adds to the project several default textures and images. These basic assets enable you to start working on your project without the need to import assets. However, when you are done creating your project, delete these textures to decrease the size of your Kanzi application kzb file.

To delete the default textures, in the Library > Materials and Textures > Textures select the Default Cubemap Texture, Default Texture, and DefaultBackground, and press the Delete key.

To delete the image files that the default textures use, in the Library > Resource Files > Images select the DefaultBackground.png, DefaultCubeMap.dds, and DefaultTextureImage.png, and press the Delete key.
## Deleting resources and prefabs that your project is not using

When you complete your project, it is good practice to delete all resources and prefabs that your project is not using. Deleting unused resources reduces the amount of memory your application uses and you simplify the structure of your project.

To delete resources and prefabs that your project is not using:

1.

In the main menu select Project > Delete Unreferenced Items.

If there are resources or prefabs that your project is not using, Kanzi Studio lists them in the Delete Unreferenced Items window.
**Tip:** To delete only specific type of items:
- To delete unused resources only from specific libraries, in the Library select one or more libraries from which you want to delete unused resources, right-click, and select Delete Unreferenced Items.
- To delete only unused prefabs, in the Prefabs right-click and select Delete Unreferenced Items.
2.
In the Delete Unreferenced Items window select the checkbox next to each item that you want to delete and click OK.
3.
(Optional) To prevent listing those items that you access using the Kanzi Engine API:
- To prevent listing resources, in the Library select the resource, in the Properties add the General > Is Used By Code property, and enable it.
- To prevent listing prefabs:
1.
In the Prefabs right-click a prefab and select Show Prefab Template Properties. The Properties window shows the properties of that prefab template.
2.
In the Properties add and enable the Is Used By Code property.

## Excluding items from an application

If your project does not use a resource or node, you can optimize the size of your Kanzi application by excluding such items.

To exclude an item from an application:

1.

Select the item in the Node Tree or Library.
2.

In the Properties add and enable the Disable KZB Export property.

If you disable a node or resource used by another node or resource that is not disabled, your application will not work. For example, if you disable a Mesh Data resource used by more than one Model node, your application will not work.

## Removing redundant Animation Data channels

Whether importing animations from a third-party tool or creating them in Kanzi, animations sometimes contain Animation Data resources that do not animate anything. For example, when you add a keyframe for a Render Transformation by dragging the property from the Properties to the Animation Clip Editor, Kanzi adds an Animation Data resource for all property attributes, even if they have not changed.

Note that the static values in Animation Data resources have higher precedence than the local property values of the node. When you delete a channel with a static value, the local value becomes effective. Because sometimes even static values (Animation Data resources without any keyframes) contain valid information and are needed, consider cleaning up unnecessary animation information on a case by case basis.

To remove the redundant Animation Data resources:

1.

In the Library select Animations > Animation Clips and select your animation clip.
2.

Right-click the animation clip for which you want to remove the redundant Animation Data resources and select Delete Animations with One or Zero Effective Keyframes.

These images show the same Animation Clip before and after removing the Animation Data resources without effective animations.

## Removing generated files

When you open a project in Kanzi Studio, Kanzi Studio generates temporary files in the project directory, such as compressed images and thumbnails. You can delete these generated files when you move your Kanzi Studio project to version control or when those files are corrupt.

To remove the generated files, in the main menu select Project > Clean Cached Files.
