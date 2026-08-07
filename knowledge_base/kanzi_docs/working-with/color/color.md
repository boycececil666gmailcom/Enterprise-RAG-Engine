---
title: Color workflow
source: https://docs.kanzi.com/4.1.0/en/working-with/color/color.html
---

# Color workflow

## Linear and nonlinear gamma color spaces

The purpose of the sRGB color space is to represent colors for display on computer monitors. Currently sRGB is the standard for the nonlinear gamma color space. It is needed because human perception of light is nonlinear, and computer monitors have a nonlinear response to light intensity.

The human eye distinguishes between darker shades better than lighter shades. For this reason it makes sense to preserve more accuracy for dark intensities when storing and displaying images on screens. The nonlinear gamma color space achieves this with gamma correction, which puts the intensity of each pixel in an image through a power function:   \[I^{\gamma}\]

Images are usually stored with an encoding gamma applied to them, and screens apply a decoding gamma. This image shows the graphs of the gamma transfer functions that Kanzi uses to convert between the linear and gamma color spaces.

This image shows a gradient where the intensity of the light emitted by your screen increases linearly.

Applying a decoding gamma to the above gradient results in this gradient where the perceptual light intensity increases linearly.

The problem with the nonlinear gamma color space is its unsuitability for graphics operations. Performing color calculations in nonlinear space leads to inaccurate results in color and alpha blending. Linear color space is needed for mathematically correct lighting and color blending calculations.

In linear color space numerical intensity values correspond to their actual intensity, which makes it possible to add and multiply color values correctly. Linear color space rendering provides more accurate results and more realistic surface shading, particularly with physically based rendering techniques.

These images show an example of blending in nonlinear gamma (left) and linear (right) color space. Blending in nonlinear gamma color space results in overly bright blends and saturated bands. [](../../_images/legacy-blending.png) [](../../_images/linear-blending.png)

Kanzi by default uses the the nonlinear gamma, or standard, color workflow, where Kanzi operates on color values in the gamma color space. See Using the standard color workflow.

Kanzi also supports the linear color workflow, where Kanzi operates on color values in linear color space. See Using the linear color workflow and Converting applications from standard to linear color workflow.
## Using the linear color workflow

In the linear color workflow Kanzi enables realistic lighting computations and correct color blending. To achieve accurate rendering of color and light, Kanzi converts all color values to linear color space before performing operations on them. Kanzi then converts the color values back to the gamma color space for storage or display.
### Images

To configure the images in your Kanzi Studio project for linear color workflow:

- In the Library > Resource Files > Images for each image resource that uses the ASTC, ETC2, JPEG, or PNG format set the value of the sRGB Content property:

  - If the image contains sRGB color information, set the sRGB Content property to enabled. This is the default setting.

If you disable the sRGB Content property for an image that contains sRGB color information, Kanzi can render the textures that use the image brighter than expected.
  - If the image contains non-color information, such as a normal, roughness, or occlusion map, set the sRGB Content property to disabled.

Textures that contain non-color information are stored in linear format. By disabling the sRGB Content property you set Kanzi to pass the image data to a shader directly, without performing a color space conversion.

- Kanzi by default premultiplies the alpha channel of images in linear color space. To premultiply the alpha channel in the color space of the image, in the Library > Resource Files > Images select an image and in the Properties disable the Linear Premultiply property. See Preparing images in third-party tools.

### Color property bindings

To set color values in binding expressions in the linear color workflow:

- Specify `Color4` values in sRGB color space. See color4.

For example:

```
Color4(0, 0.75, 0.25, 1)

```

- Specify the values of individual RGB color channels in linear color space.

Use the sRGBToLinear binding function to convert a color channel value to linear color space.

For example:

  - This binding expression is equal to `Color4(0, 0.75, 0.25, 1)`:

```
color = Color4(0, 0, 0, 1)
color.g = sRGBToLinear(0.75)
color.b = sRGBToLinear(0.25)
color

```

  - This binding expression is equal to `Color4(0, 0.879, 0.535, 1)`:

```
color = Color4(0, 0, 0, 1)
color.g = 0.75
color.b = 0.25
color

```

### Shaders

In the linear color workflow shaders expect color input to be in linear color space and they output color in linear color space. To preserve accuracy when storing color values in 8-bit per channel texture formats, Kanzi converts the color values back to the sRGB color space before storing.
### Graphics API

The linear color workflow needs either:

- EGL version 1.5 or later, or EGL version 1.4 with the `EGL_KHR_gl_colorspace` extension.
- Vulkan 1.1 or later.

## Using the standard color workflow

By default Kanzi uses the standard color workflow. This performs operations on color values in the nonlinear gamma color space. This provides less precise rendering results than the linear color workflow.

Use the standard color workflow when you:

- Deploy your application to a device that does not support linear color space.

To support linear color space, your target platform must implement EGL version 1.5 or later, or EGL version 1.4 with the `EGL_KHR_gl_colorspace` extension, or Vulkan 1.1 or later.

When your Kanzi application requests linear color space but the target device does not support it, the resulting behavior varies between target platforms.

For example, your application can:

  - Print to the log a warning about lack of support for EGL_GL_COLORSPACE, and fall back to the legacy color space.
  - Terminate with this error:

```
eglCreateWindowSurface() failed: EGL_BAD_ATTRIBUTE

```

- Migrate a project from earlier versions of Kanzi.

In the standard color workflow Kanzi does not convert color input. If you use the Kanzi Engine API to create a `ColorRGBA` object, provide the color values in the sRGB color space.

To use the standard color workflow:

1.

Configure your application to use an unspecified color space by setting either:

  - In `application.cfg`:

```
SurfaceColorSpace = "standard"

```

  - In the C++ application in the `Application::onConfigure` function:

```
configuration.defaultSurfaceProperties.colorSpace = "standard";

```

See SurfaceColorSpace.
2.

In Kanzi Studio in the Project > Properties set the Color Workflow property to Standard.
3.

Write your shaders to output colors in the gamma space of your target display, which is likely sRGB. See Shaders.

## Converting applications from standard to linear color workflow

To convert your application from the standard color workflow to the linear color workflow:

1.

Configure your application to use the sRGB color space by configuring the linear color workflow:

  - In `application.cfg`:

```
SurfaceColorSpace = "srgb"

```

  - In the C++ application in the `Application::onConfigure` function:

```
configuration.defaultSurfaceProperties.colorSpace = "srgb";

```

See SurfaceColorSpace.
2.

In Kanzi Studio in the Project > Properties set Color Workflow to Linear.
3.

In the Library > Materials and Textures > Material Types for each material type make sure that:

  - Bindings do not contain needless manually added sRGB conversions.

For example, you do not need to use the linearTosRGB binding function to convert color values from linear color space to sRGB color space. In the linear color workflow shaders expect color input to be in linear color space.
  - Shaders do not apply gamma correction at input or output.

In the linear color workflow shaders expect color input to be in linear color space and they output color in linear color space.

4.

In the Library > Resource Files > Images for each image resource that uses the ASTC, ETC2, JPEG, or PNG format check that the sRGB Content property is set correctly:

  - If the image contains sRGB color information, set the sRGB Content property to enabled. This is the default setting.

If you disable the sRGB Content property for an image that contains sRGB color information, Kanzi can render the textures that use the image brighter than expected.
  - If the image contains non-color information, such as a normal, roughness, or occlusion map, set the sRGB Content property to disabled.

Textures that contain non-color information are stored in linear format. By disabling the sRGB Content property you set Kanzi to pass the image data to a shader directly, without performing a color space conversion.

5.

To get the desired color blending result, adjust the partially transparent colors in your project where needed.

For example, nodes filled with these color brushes look different in the standard and linear color workflow modes:
|

Standard color workflow |

Linear color workflow |
|   |    |
