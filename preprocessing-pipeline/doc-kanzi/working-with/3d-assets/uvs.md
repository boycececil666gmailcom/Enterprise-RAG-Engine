---
title: Using 3D models with UVs
source: https://docs.kanzi.com/4.1.0/en/working-with/3d-assets/uvs.html
---

# Using 3D models with UVs

UVs are 2D texture coordinates projected onto a 3D surface. UVs define which pixels on a texture map to which vertex on a 3D model. To use texture coordinates in Kanzi Studio, you need to create a UV layout in a content creation tool, such as 3ds Max. This is called unwrapping or UV-mapping. Unwrap your 3D model in flat 2D space to project a texture for that 3D model so that the flow runs from the start to the end of the model. See Preparing 3D assets in third-party tools.

You can use 3D models with UVs in Kanzi Studio with:

- Texture Offset property.

Using UVs with the Texture Offset property allows you to offset the texture on the surface of the 3D model. For example, to create speed gauges with UVs using the Texture Offset property, bind the Texture Offset property to a custom property which controls the speed.
- Custom property.

When you use UVs with a custom property, you can use that custom property to control the offset by binding it to the Texture Offset property.

To use UVs in your Kanzi Studio project:

1.

Prepare the UV coordinates for your 3D model in content creation software such as 3ds Max. See Preparing 3D assets in third-party tools.
2.

In Kanzi Studio transform the UV texture coordinates using either the Texture Offset property or a custom property. See Transforming UVs with the Texture Offset property and Transforming UVs with a custom property.

## Using 3D models with UVs in Kanzi Studio

To use 3D models with UVs in Kanzi Studio:

1.

Prepare the UV coordinates for your 3D model in content creation software such as 3ds Max. See Preparing 3D assets in third-party tools.
2.

In the Assets window click Import Assets, select the UV-mapped 3D model which you want to use, and click Open.

When you import 3D assets, Kanzi Studio creates for each 3D asset:

  - In the Prefabs, a Scene prefab for each scene in the imported file.

Kanzi Studio names each Scene prefab after the imported file. When you import a glTF file that contains multiple scenes, Kanzi Studio appends to the name of each Scene prefab the name of the scene.

In each Scene prefab, Kanzi Studio creates the scene hierarchy from the imported file and places the assets from the imported file into that prefab.
  - In the Library, Kanzi Studio places all resources from the imported file, such as Meshes, Splines, Animations, and Materials.

See Importing 3D assets
3.

In the Prefabs select the Scene named after the 3D model you imported in the previous step and double-click it to open it as a composition.

To see the Scene composition rendered in the Preview, it must contain a camera and at least one light node.
4.

In the Model composition select the Model > RootNode > Model node and in the Properties set the material for the 3D model to the material you want to use for that model. In this example you use a material which supports textures.

## Transforming UVs with the Texture Offset property

In Kanzi Studio you can transform UV texture coordinates using the Texture Offset property. When you adjust the value of that property, you transform the coordinates where Kanzi offsets the texture.

To transform UVs with the Texture Offset property:

1.

Prepare the UV coordinates for your 3D model in content creation software such as 3ds Max. See Preparing 3D assets in third-party tools.
2.

In the Prefabs select the Model node and in the Properties add and set:

  - Blend Mode property to Alpha: Premultiplied This ensures correct blending of transparency.
  - Texture property to the texture which you want to control with the UVs.
  - Texture Offset property.

You use the Texture Offset property to control the UV coordinates on the 3D model. If you want the 3D model to be invisible when the value of the Texture Offset property is higher than the size of the 3D model, make sure that 2 pixels around the texture are transparent.

3.

In the Library > Materials and Textures > Textures select the texture the position of which you control with the Texture Offset property and in the Properties set the Wrap Mode property to Clamp.

This way there is no texture repetition when the Texture coordinates are offset to values below 0.0 or above 1.0.

Kanzi updates the texture coordinates used in the rendering when the value of the Texture Offset property changes. For example, to create speed gauges, bind the Texture Offset property to a custom property which contains the current speed. When the value of the custom property changes, Kanzi offsets the texture based on the value of that property. See Using bindings.
## Transforming UVs with a custom property

In Kanzi Studio you can transform UV texture coordinates using a custom property. When you adjust the value of that property, you transform the coordinates where Kanzi offsets the texture.

To transform UVs with a custom property:

1.

Prepare the UV coordinates for your 3D model in content creation software such as 3ds Max. See Preparing 3D assets in third-party tools.
2.

In the Library press Alt and right-click Property Types, select Property Type and in the Property Type Editor set:

  - Lower Bound to the lowest value of the property.

For example, set it to 0.
  - Upper Bound to the highest value of the property.

For example, set it to 270.

3.

In the Prefabs select the Model > RootNode > Model node and in the Properties add and set:

  - Texture property to the texture you want to use.
  - Blend Mode to Alpha: Premultiplied.

This ensures correct blending of transparency.
  - The custom property you created in the previous step.

4.

In the Library > Materials and Textures > Textures select the texture you use for the material of the model and set the Wrap Mode property to Clamp.

This way there is no texture repetition when you adjust the value of the custom property. The UV coordinates of the 3D model work as a canvas for the texture.
5.

In the Prefabs select the Model node, in the Properties click + Add Binding, and in the Binding Editor set:

  - Property to Texture Offset
  - Property Field to VECTOR_X
  - Expression to:

```
({@./Speed}/270.0) - 1.0

```

This offsets the texture on the x axis based on the value you set in the custom property. You divide the value of the speed by 270.0 because you use that as the maximum value of the speed gauge. You scale the range of the gauge to match the range of the texture coordinate values which go from 0.0 to 1.0. You subtract 1.0 to shift the coordinates out of the 0.0 to 1.0 range and to make the gauge empty when the value of the custom property is 0.

To offset the texture on the y axis, in the Binding Editor set the Property Field to VECTOR_Y.

When you adjust the value of the custom property, Kanzi offsets the texture on the axis you set in the binding based on the value of that property.
