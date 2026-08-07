---
title: Textures
source: https://docs.kanzi.com/4.1.0/en/working-with/textures/textures.html
---

# Textures


Use textures to show content in Image nodes, to set the look of textured materials, and to show content in Texture Brush brushes. You can create textures from common image file formats.

See Images.

In a Kanzi Studio project, image files are located in Library > Resource Files > Images. These image files correspond to files on your hard drive. When you modify a file on the hard drive, Kanzi automatically applies the modifications to the textures generated from that file. If you remove the file from the hard drive, you cannot use the file in your Kanzi project.

Loading time of images depends on their size and compression:

- **Image size** defines the time required to load the data into RAM.
- **Image compression** can reduce the size, but keep in mind that before your application can use the image, it must decompress it, which is often slower than loading the raw data. You can often achieve the fastest start-up times when using Raw image format, where data is loaded into RAM and sent to the GPU memory. See Image Compression.
- **Texture compression** you can use on devices with GPUs that support the selected compression algorithm. When using compression, the data size is smaller both when loading from kzb file to RAM and when loading from RAM to the GPU memory. Also less GPU memory is reserved. Depending on the target hardware, by using texture compression you can reduce loading times. Before using texture compression, make sure that your target platform supports the texture compression format you selected.

Kanzi supports ASTC, ETC, and BCn compression formats.

If your target hardware does not support the selected texture compression algorithm, when you run your Kanzi application on your target device, Kanzi prints a warning message to the log. Kanzi paints black the surfaces where you use compressed texture formats that your target hardware does not support.

See Compressing textures.

## Texture types


These textures are available in Kanzi:
|

Single textures use a single image for the texture.

See Using single textures.  |    |
|

Cubemap textures combine six square-shaped images into one texture to represent reflections of the environment. Each image represents the scenery in one of the six directions along the x, y, and z axes from the viewpoint of the cubemapped object.

See Using cubemap textures.  |    |
|

Volume textures use a single 2D image, made up of many cross-section slices of a 3D shape, to define a 3D volume texture. This technique is often used for effects like smoke, fire, or clouds, where 3D data would be too resource intensive or difficult to generate procedurally.

See Using volume textures.  |    |
|

Use a Render Target Texture to render content to a texture or to apply anti-aliasing to only a part of your application. You can use render target textures like any other texture. For example, you can use it in a Texture Brush or as an image in an Image node.

See Using render target textures and Using OpenGL ES 3.0+ in Kanzi.  |    |
|

Use a Cubemap Render Target Texture to render a Cubemap render pass to a cubemap texture.

See Creating cubemap reflections.  |    |

You can use .exr, .dds, and .hdr images with half float and floating point data to bring HDR images to your Kanzi project. See Setting the color format of textures.
## Setting the image target format


When you export your project to a kzb file, Kanzi Studio reads the images in the project using the format of the original image and writes the images to a kzb file in the format you set with the Target Format property for each image.

If the file format of the original image is the same as the format you select in the Target Format property, Kanzi Studio does not modify the image when it writes the image to a kzb file under these conditions:

- Premultiply Alpha is disabled, or the alpha channel does not need to be premultiplied

To change this setting, in the Project > Properties use the Premultiply Alpha property. You can override this value in the properties of the image file where you want to use a different setting.
- Generate Mipmaps is disabled

You can set the value of the Generate Mipmaps property in each image file.
- Round up Image Dimensions to Nearest Power of Two property is disabled

You can set the value of the Round up Image Dimensions to Nearest Power of Two property in the Project > Properties.

When you enable the Round up Image Dimensions to Nearest Power of Two property, Kanzi Studio rounds up the width and height of the images in your project to the nearest power of two during kzb file export. For example, Kanzi Studio exports an image of the size 40 by 30 pixels to the kzb file in the size 64 by 32 pixels.


If your image is in JPEG or PNG format and you do not want Kanzi Studio to modify the image that it exports to a kzb file, in the image Properties enable the Use Original Image property.

To set the image target format:

1.

In the Library > Resource Files > Images select the image for which you want to set the target format.
2.

In the Properties set the Target Format property to the image format you want to use in your Kanzi application.

The format you select is important because this influences the size of the kzb file and the loading time when your Kanzi application loads the image. Make sure that your target device supports the target format you select for the image. See Images and textures best practices and Compressing textures.
3.

If the image format you selected in the previous step supports compression, configure the compression scheme you want to use. See Compressing textures.
4.

For image formats that support sRGB:

  - If the image contains sRGB color information, set the sRGB Content property to enabled. This is the default setting.

If you disable the sRGB Content property for an image that contains sRGB color information, Kanzi can render the textures that use the image brighter than expected.
  - If the image contains non-color information, such as a normal, roughness, or occlusion map, set the sRGB Content property to disabled.

Textures that contain non-color information are stored in linear format. By disabling the sRGB Content property you set Kanzi to pass the image data to a shader directly, without performing a color space conversion.

5.

If you want Kanzi to premultiply the alpha channel in the:

  - Linear color space, set the Linear Premultiply property to enabled.

This is the default value and results in the fewest artifacts in sRGB images.
  - Color space of the image, usually sRGB, set the Linear Premultiply property to disabled.

This can give better results for images created for the standard color workflow.


See Preparing images in third-party tools.

## Using textures in the API


For details, see the `Texture` class.
