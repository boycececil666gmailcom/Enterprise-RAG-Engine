---
title: Images and textures best practices
source: https://docs.kanzi.com/4.1.0/en/best-practices/images-and-textures/images-and-textures-best-practices.html
---

# Images and textures best practices

The required memory bandwidth that rendering of large textures and images use can slow down your application. Use these tips to improve the performance of your application by creating and using optimal images and textures:

- The easiest way to optimize the performance of your application is to reduce the amount of detail in your images by using smaller data sizes. See Adjusting the data size.
- Kanzi supports Adaptive Scalable Texture Compression (ASTC), Ericsson Texture Compression (ETC), Block Compression (BCn), and PNG compression for compressing images used in textures. See Compressing textures.
- When users run your Kanzi application in an environment with a multi-core processor, Kanzi automatically uses multiple CPU cores to load the GPU resources in the kzb files to RAM.

Kanzi enables you to configure how many cores you want your application to use. See Loading resources in parallel.
- Use mipmaps to create a set of downscaled sublevels from a large texture. Mipmaps increase the GPU memory use by one third, but improve the performance when the full texture does not have to be sampled. Use mipmaps to improve the performance whenever you scale a textured node.

See Using mipmaps.
- Apply texture filtering to increase either quality or performance. This method can be very effective if you are familiar with the application behavior in advance. See Filtering textures.
- Use a tile atlas to improve application framerate by decreasing the number of texture switches that your application must make during runtime.

See Using a tile atlas.
- Make sure that all textures have the Mipmap Mode property set to at least Nearest. Use the Mipmap Mode value Base only very small textures (for example, 4 by 4 pixels and smaller).
- Make the textures which contain only flat color no larger than 4 by 4 pixels and set the Texture Settings properties:

  - Minification Filter to Nearest
  - Magnification Filter to Nearest
  - Mipmap Mode to Base

- When you use a Text Block Kanzi creates a glyph cache texture for every font and font size combination. You can set the height and width of glyph cache textures to adjust the size of the glyph cache texture either when it gets full, or to optimize the performance of your Kanzi application.

See Glyph cache texture size.
- When your Kanzi application uses a png image which contains invalid ICC profile, Kanzi prints a warning to the log at application runtime. To remove the ICC profile from all png images, in the Project > Properties enable the Remove ICC Profile From PNG Images property.

When you enable this property Kanzi removes the ICC profile from png images in your project during the kzb file export.
- Make sure that all image resources that are used by textures or materials in glTF assets have the Ignore Embedded Color Profile property enabled.

When you enable this property Kanzi Studio:

  - Removes the ICC profile from a png, jpg, or exr image file.
  - Does not perform gamma correction for the image.

When you import to your Kanzi Studio project a glTF or glb asset, Kanzi Studio automatically enables the Ignore Embedded Color Profile property in the image resources used by that asset.
- Make sure that all image resources that use the ASTC, ETC2, JPEG, or PNG format have the sRGB Content property set correctly:

  - If the image contains sRGB color information, set the sRGB Content property to enabled. This is the default setting.

If you disable the sRGB Content property for an image that contains sRGB color information, Kanzi can render the textures that use the image brighter than expected.
  - If the image contains non-color information, such as a normal, roughness, or occlusion map, set the sRGB Content property to disabled.

Textures that contain non-color information are stored in linear format. By disabling the sRGB Content property you set Kanzi to pass the image data to a shader directly, without performing a color space conversion.

- Make sure that all image resources that contain transparency have the Linear Premultiply property set correctly. If you want Kanzi to premultiply the alpha channel in the:

  - Linear color space, set the Linear Premultiply property to enabled.

This is the default value and results in the fewest artifacts in sRGB images.
  - Color space of the image, usually sRGB, set the Linear Premultiply property to disabled.

This can give better results for images created for the standard color workflow.

See Preparing images in third-party tools.
