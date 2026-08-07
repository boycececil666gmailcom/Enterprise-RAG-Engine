---
title: Using the Image node
source: https://docs.kanzi.com/4.1.0/en/working-with/images/using-images.html
---

# Using the Image node

Use the Image node to show a bitmap image.

Use image files to bring bitmap assets to Kanzi Studio. You can import images to Kanzi in these file formats:

- .png, including the alpha channel
- .tga, including the alpha channel
- .psd, including layers. See Importing Adobe Photoshop PSD files.
- .dds, can contain cubemaps, mipmaps, or both
- .bmp, .exr, .gif, .hdr, .ico, .iff, .jng, .jpg, .jpeg, .jif, .mng, .pcx, .pmb, .pgm, .ppm, .pfm, .pict, .ras, .sgi, .tiff, .tif, .wbmp, .xmb, and .xpm

For optimal application performance, make sure that you correctly set up the images in your Kanzi Studio project. See Images and textures best practices.
## Creating an Image node

To create an Image node:

1.

In the Assets window click Import Assets.
2.

Select the files that you want to import and click Open.

1.

Drag an image from the Assets and drop it either in the Preview or any 2D node in the Node Tree.
2.

(Optional) For the image you use you can set the target format that is the most suitable for your application. See Setting the target format for an image.

or

1.

In the Node Tree press Alt and right-click the node where you want to create an Image node and select Image.

You can create a 3D node only in a 3D node, such as the Scene node, and a 2D node only in a 2D node.
2.

In the Properties set the Image property to the image you want the Image node to show.

The Image node inherits the width and height from the image set in the Image property. To set a different size, add and set properties:

  - Layout Width and Layout Height to set the size of the Image node.
  - Content Stretch to set how Kanzi stretches the content of the Image node.

3.

(Optional) Set the image position by setting the Horizontal Alignment and Vertical Alignment properties.
4.

(Optional) For the image you use you can set the target format that is the most suitable for your application. See Setting the target format for an image.

## Setting the target format for an image

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

## Using the PNG compression

When you use PNG compression keep in mind that because the compressed PNG images do not go to the GPU in compressed format, PNG compression affects the loading of a PNG image data from a kzb file to the device memory.

Use PNG compression to store and load images from a kzb file. To improve the performance of your application consider using an image format which Kanzi can send compressed directly to the device GPU. See Compressing textures.

To use the PNG compression:

1.

In Kanzi Studio in the Library select Resource Files > Images, and select the image for which you want to apply compression.
2.

In the Properties set the Target Format to PNG.
3.

In the Properties set the PNG Compression Level property to the compression you want to use for this image:

  - Project default to use the PNG compression set in the Project > Properties in the PNG Compression Level property
  - No compression to not use compression for the image
  - Best compression speed (zlib level 1) creates a larger file, but compresses quickly
  - Default (zlib level 6) creates a smaller file, but takes longer to compress. This is the default option of the FreeImage library which Kanzi Studio uses for PNG images.
  - Best compression (zlib level 9) creates the smallest file, but takes the most time to compress
**Tip:** You can set the value of the PNG Compression Level property in the Project > Properties and in the properties for each image file.

## Applying custom rendering to an Image node

Apply custom rendering to Image nodes to create post-processing effects. For example, you can convert color images in a 2D node to grayscale.

To apply custom rendering to an Image node, use the Foreground Brush property to render the node on the screen with a Material Brush. For example, to render content of a node, such as the image in an Image node or text in a Text Block 2D node, use the Foreground Brush property.

To apply custom rendering to an Image node:

1.

Create a material with which you want to apply custom rendering.

For example, to create a material that converts color to grayscale:

  1.

In the Library, press Alt and right-click Materials and Textures and select Material Type. Kanzi Studio creates a material type and a material that uses the material type.
  2.

In the Library > Materials and Textures > Material Types, expand the material type that you created. Double-click the Vertex Shader to open it in the Shader Source Editor, replace the existing shader code with this code, and save the shader.

```
#version 310 es

in vec3 kzPosition;
in vec2 kzTextureCoordinate0;
uniform highp mat4 kzProjectionCameraWorldMatrix;

out mediump vec2 vTexCoord;

void main()
{
    precision mediump float;
    vTexCoord = kzTextureCoordinate0;
    gl_Position = kzProjectionCameraWorldMatrix * vec4(kzPosition.xyz, 1.0);
}

```

  3.

Open the Fragment Shader, replace the existing shader code with the code in this step, and save the shader.

In the shader, use these Kanzi default uniforms:

    - `ContentTexture` to define the texture that the rendered node provides when rendering
    - `RenderOpacity` to define the opacity of the rendered node

See Shader uniforms.

```
#version 310 es

uniform sampler2D ContentTexture;
in mediump vec2 vTexCoord;
uniform lowp float RenderOpacity;
layout(location = 0) out vec4 fragColor;

void main()
{
    precision mediump float;
    // Use this algorithm to convert the colors in the texture used by
    // the 2D node to grayscale.
    // To integrate to the Kanzi rendering pipeline, the shader must output
    // premultiplied alpha.
    vec4 color = texture(ContentTexture, vTexCoord);
    float grayscale = dot(color.rgb, vec3(0.21, 0.72, 0.07));
    float alpha = color.a * RenderOpacity;
    vec3 premultipliedColor = vec3(grayscale) * alpha;
    fragColor = vec4(premultipliedColor, alpha);
}

```

2.

In the Library, press Alt and right-click Materials and Textures and select Material Brush. In the Properties, set the Material property to the material that you created in the previous step.
3.

In the Node Tree create or select the Image node to which you want to apply the material you created, and set the node to display an image.
4.

In the Properties add and set the Foreground Brush property of the Image node to the material brush that uses the material you want to apply to that node.
5.

(Optional) Set the blending of the image:

  1.

In the Library > Materials and Textures > Material Types select the material type you created, in the Properties click the Property Types dropdown menu, select Blend Mode, and click Sync with Uniforms.

This way you add the Blend Mode property to the materials that use this material type.
  2.

In the Properties add and set the Blend Mode property in either of these places:

    - The Material Brush that uses the material to which you added the Blend Mode property
    - The Image node that uses the Material Brush

For example, in the Node Tree select the Image node, in the Properties add the Blend Mode property, and set it to Alpha: Premultiplied.

6.

(Optional) To adjust the translucency of the image, in the Node Tree select the Image node, and in the Properties add and set the Opacity property.

## Setting the appearance of an Image node

To set the appearance of 2D nodes:

- You can fill 2D nodes with a solid color, a texture, or a material. See Adjusting the appearance of 2D nodes.
- You can apply a post-processing effect to a 2D node. See Effects for 2D nodes.
- You can rotate a 2D node around all three axes to create a 3D perspective effect. See Creating a 3D perspective effect for 2D nodes.
- You can apply custom rendering to 2D nodes to create post-processing effects. See Applying custom rendering to 2D nodes.
- You can render a 2D node as pixel-perfect. See Rendering pixel-perfect 2D nodes.

## Using the Image node in the API

For details, see the `Image2D` class.
## Image property types and messages

For a list of the available property types and messages for the Image node, see Image.
