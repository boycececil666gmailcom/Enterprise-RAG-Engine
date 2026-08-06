---
title: Using mipmaps
source: https://docs.kanzi.com/4.1.0/en/best-practices/images-and-textures/using-mipmaps.html
---

# Using mipmaps


Use mipmaps to create a set of downscaled sublevels from a large texture. Mipmaps increase the GPU memory use by one third, but improve the performance when the full texture does not have to be sampled. Use mipmaps to improve the performance whenever you scale a textured node.

For example, a 256 by 256 pixels texture has mipmap levels that reduce the texture to 128 by 128, 64 by 64, and so on until 1 by 1 pixel. The performance improves because smaller mipmap levels fit better in the fixed-size texture cache in the GPU.

When you create mipmaps in a third-party tool and include them in a .dds file, Kanzi Studio extracts the images for mipmap levels and uses them.

Avoid creating mipmaps from .jpeg textures, because the .jpeg image format causes the quality of the mipmaps to degrade.
## Generating mipmaps for a texture


When you import an image that does not contain mipmaps, you can generate the mipmaps for the texture from that image in Kanzi Studio.

To generate mipmaps for a texture:

1.

In the Library > Resource Files > Images, select the image for which you want to create mipmaps.

Avoid creating mipmaps from .jpeg textures, because the .jpeg image format causes the quality of the mipmaps to degrade.
2.

In the Properties, enable the Generate Mipmaps property.
3.

In the Library > Materials and Textures > Textures, select the texture that uses the image for which you want to generate mipmaps. In the Properties, set the Mipmap Mode property to Linear or Nearest to take the mipmaps into use. See Filtering textures.
4.

When you export the kzb file of your project and Kanzi Studio asks whether you want to preprocess the images, click Yes. If you do not preprocess images in Kanzi Studio, Kanzi Engine generates mipmaps when it loads your application on the target device. This increases the loading time of your application.

> **Note:** Kanzi cannot generate mipmaps for images that use ASTC or ETC compression.
>
> Tip
>
> To manually generate mipmaps for images, in the Library right-click the image for which you want to generate mipmaps and select Preprocess images.
>
## Creating mipmaps for composition targets


You can create mipmaps for composition targets when you render 3D content with a Composition Target render pass or Cubemap render pass. For example, use this to create a low-quality blur effect that is quick to render.

This procedure explains how to create mipmaps for the composition targets that Kanzi creates automatically. To create mipmaps for a Render Target Texture, see Creating mipmaps for a Render Target Texture.

To create mipmaps for composition targets:

1.

Create the render passes that you need to render your content to one or more composition targets.

For example, in the Library > Rendering > Render Pass Prefabs, create a Compose and Blit Pass. See Rendering content to composition targets.
2.

In the Library > Rendering > Render Pass Prefabs, select the Composition Target render pass or Cubemap render pass for whose composition targets you want to create mipmaps. In the Properties, add the Mipmap Mode property, and set it either to Linear or Nearest. See Filtering textures.
3.

(Optional) To customize how Kanzi creates the mipmaps, you can set a mipmap filtering material for each composition target.

Kanzi Studio comes with a set of mipmap filtering materials that you can use.

To set the mipmap filtering materials:

  1.

Set your render pass to use the mipmap filtering materials:

    - For a Cubemap render pass, add and set the Mipmap Generation > Cubemap Mipmap Material property to the material that you want to use.

For example, set it to the DefaultCubemapMipmapFilterMaterial. If your project does not contain this material, in the Library > Materials and Textures press Alt and right-click Material Types, and select DefaultCubemapMipmapFilter.
    - For a Composition Target render pass, add and set one or more of these Mipmap Generation properties:

      - Color Mipmap Material 0, Color Mipmap Material 1, Color Mipmap Material 2, and Color Mipmap Material 3 to set the mipmap filter materials for the color composition targets.

For example, to set the material for Composition Target 0, add and set the Color Mipmap Material 0 property to DefaultMipmapFilterMaterial. If your project does not contain this material, in the Library > Materials and Textures press Alt and right-click Material Types, and select DefaultMipmapFilter.
      - Depth Mipmap Material to the material that you want to use for the depth attachment of the first composition target.

For example, set it to the DefaultDepthMipmapFilterMaterial. If your project does not contain this material, in the Library > Materials and Textures press Alt and right-click Material Types, and select DefaultDepthMipmapFilter.


The default mipmap filtering materials can use these properties as inputs to their shaders:

  - Current Mipmap Level reports the mipmap level that is being rendered.
  - Mipmap Source Texture reports the texture that contains the render target texture for which the mipmap is created. The shader must sample only from mipmap levels that are less than the Current Mipmap Level.

4.

(Optional) By default, Kanzi generates the mipmaps when the Composition Target render pass or Cubemap render pass creates the composition target. When you continue rendering to the same composition target in another render pass, creating the mipmaps immediately is likely to waste GPU time. To avoid this, in the render that creates the composition target, add and disable the Composition Target render pass > Resolve Immediately or Cubemap render pass > Resolve Immediately property.

## Creating mipmaps for a Render Target Texture


You can create mipmaps for a Render Target Texture to which you render 3D content with a Composition Target render pass. For example, use this to create a low-quality blur effect that is quick to render.

To create mipmaps for a Render Target Texture:

1.

In the Library > Rendering > Render Pass Prefabs create a Render to Texture Pass.

Render to Texture Pass creates the render passes and texture you need to render to a texture.

See Rendering to texture.
2.

In the Node Tree select the Viewport 2D node the content of which you want to render to a texture and in the Properties set the Render Pass Prefab property to the Render to Texture Pass you created in the previous step.

Kanzi now renders the Viewport 2D using the render passes you created.
3.

In the Library select the Render to Texture Pass that you created, in the Properties click  next to the Composition Target 0 property to go to the Render Target Texture resource, and set the Mipmap Mode property to either Linear or Nearest. See Filtering textures.
4.

Use the Render Target Texture in a node where you want to show the 3D content. See Using render target textures.
