---
title: Using OpenGL ES 3.0+ in Kanzi
source: https://docs.kanzi.com/4.1.0/en/working-with/rendering/using-opengl-es-30.html
---

# Using OpenGL ES 3.0+ in Kanzi

Kanzi supports deployment to OpenGL ES 3.0, 3.1, and 3.2. Shader **source code** in your materials must use GLSL ES version 310 or later syntax regardless of the deployment target â Kanzi cross-compiles shaders to the GLSL ES dialect matching the projectâs Target Graphics API setting. With OpenGL ES 3.0 and above you can use integer textures, floating point, and multiple render targets. For example, this allows you to have more precision with the rendered images, you can apply better looking post-processing effects, use HDR for textures and cubemap textures, and create seamless cubemaps. With OpenGL ES 3.1 you can additionally use compute shaders, image load/store, and shader storage buffer objects. With OpenGL ES 3.2, you can also use geometry and tessellation shaders.

Before you use OpenGL ES 3.0+, make sure that your target platform supports the API version.

To select the version of OpenGL ES to use in Kanzi:

1.

In the Kanzi Studio main menu, select Project > Properties and set the Target Graphics API to the OpenGL ES version your target platform supports: OpenGL ES 3.0, OpenGL ES 3.1, or OpenGL ES 3.2.
2.

In your shader source files, add as the first line the OpenGL ES version tag.

Kanzi requires `#version 310 es` or later as the version tag in shader source code, regardless of your Target Graphics API. Earlier tags such as `#version 300 es` are not accepted. If Target Graphics API is set to OpenGL ES 3.0, the shader is cross-compiled to `#version 300 es` at export time, provided the source does not use features that were introduced in GLSL ES 3.1 or later.

  - For shaders that do not use features introduced after GLSL ES 3.1, add

```
#version 310 es

```

  - For shaders that use geometry or tessellation shader features (which require Target Graphics API OpenGL ES 3.2), add

```
#version 320 es

```

## Setting the shader families to export

When Kanzi Studio exports a kzb file, it compiles shaders for the families listed in the Target Shader Family property. By default, Kanzi Studio compiles shaders for all three families: OpenGL, OpenGL ES, and Vulkan. To reduce the size of the kzb file, remove the families that your target platform does not use.

The GLSL or GLSL ES version that Kanzi Studio uses for the OpenGL and OpenGL ES families depends on the Target Graphics API setting.
**Note:** When Target Graphics API is Vulkan 1.2, Kanzi Studio exports only Vulkan SPIR-V shaders, regardless of the Target Shader Family setting.
To set the shader families to export:
1.
In the Kanzi Studio main menu, select Project > Properties.
2.
In the Binary Export category, set the Target Shader Family property. Click Shader family to select the families to include:
- OpenGL â Kanzi Studio compiles GLSL shaders for OpenGL desktop platforms.
- OpenGL ES â Kanzi Studio compiles GLSL ES shaders for OpenGL ES mobile and embedded platforms.
- Vulkan â Kanzi Studio compiles SPIR-V shaders for Vulkan platforms.

To include multiple families, select each from the menu. Kanzi Studio shows the selected families as a comma-separated list in the property field.

## Setting the color format of textures

You can import to your Kanzi Studio project HDR and floating point images in .dds format and set the color format of the textures that use these images.

To set the color format of textures:

1.

In the Library > Resource Files > Images, select the image whose color format you want to set.
2.

In the Properties, set:

  - Target Format to Raw
  - Color Format in Raw to the color format that you want Kanzi to use to interpret the texture

3.

In the Library > Materials and Textures > `Textures`, select the texture that uses the image whose color format you set in the previous step. In the Properties, set:

  - Wrap Mode to Clamp
  - Mipmap Mode to Linear or Nearest

## Setting the format of a render target texture

Set the format of a render target texture to define the target pixel format used by the GPU.

To set the format of a render target texture:

1.

In the Library > Materials and Textures > `Textures`, select or create a Render Target Texture.
2.

In the Properties, set the Format to the target pixel format that you want to use.
3.

If your render target textures are in integer target format, set the Minification Filter and Magnification Filter properties to Nearest.

## Selecting runtime graphics backend

On the Windows operating system you can select whether you want to use OpenGL ES, OpenGL, or Vulkan in the `Application::onConfigure` function, in the `application.cfg`, or using the command line arguments, if your target supports command line arguments.

On the command line use:

- `--gles` or `--opengles` to use OpenGL ES
- `--gl` or `--opengl` to use OpenGL
- `--vk` or `--vulkan` to use Vulkan
- `--egl` to use EGL
- `--wgl` to use WGL
- `--glx` to use GLX

In `application.cfg` |

`SurfaceClientAPI = clientApi`

`GraphicsContextAPI = contextApi`  |

In `Application::onConfigure` |

`configuration.defaultSurfaceProperties.clientAPI = clientApi;`

`configuration.defaultSurfaceProperties.contextAPI = contextApi;`  |

Values |

`clientApi` |

To use OpenGL ES:

- In `application.cfg` use `gles` or `opengles`.
- In `Application::onConfigure` use `SurfaceClientAPI::OpenGLES`.

To use OpenGL:

- In `application.cfg` use `gl` or `opengl`.
- In `Application::onConfigure` use `SurfaceClientAPI::OpenGL`.

To use Vulkan:

- In `application.cfg` use `vk` or `vulkan`.
- In `Application::onConfigure` use `SurfaceClientAPI::Vulkan`.

`contextApi` |

To use WGL:

- In `application.cfg` use `wgl`.
- In `Application::onConfigure` use `GraphicsContextAPI::WGL`.

To use EGL:

- In `application.cfg` use `egl`.
- In `Application::onConfigure` use `GraphicsContextAPI::EGL`.

To use GLX:

- In `application.cfg` use `glx`.
- In `Application::onConfigure` use `GraphicsContextAPI::GLX`.

`application.cfg` example |

```
# Sets the surface target for OpenGL rendering and WGL graphics context.
SurfaceClientAPI = gl
GraphicsContextAPI = wgl

```

`Application::onConfigure` example |

```
// Sets the surface target for OpenGL rendering and WGL graphics context.
configuration.defaultSurfaceProperties.clientAPI = SurfaceClientAPI::OpenGL;
configuration.defaultSurfaceProperties.contextAPI = GraphicsContextAPI::WGL;

```
## Enabling OpenGL ES 3.0 in the Android Emulator

When you deploy to the Android Emulator an application that uses OpenGL ES API level higher than 2.0, enable OpenGL ES 3.0 in the Android Emulator.

To enable OpenGL ES 3.0 in the Android Emulator:

1.

In Android Studio, in the Device Manager, for the running virtual device, select Extended Controls.
2.

In the Extended Controls window, select Settings > Advanced. Set the OpenGL ES API level option to Renderer maximum (up to OpenGL ES 3.1).
3.

To apply the changes, restart the Android Emulator.
