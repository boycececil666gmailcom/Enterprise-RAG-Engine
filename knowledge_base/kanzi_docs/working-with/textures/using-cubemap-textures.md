---
title: Using cubemap textures
source: https://docs.kanzi.com/4.1.0/en/working-with/textures/using-cubemap-textures.html
---

# Using cubemap textures

Cubemap textures combine six square-shaped images into one texture to represent reflections of the environment. Each image represents the scenery in one of the six directions along the x, y, and z axes from the viewpoint of the cubemapped object.

Before you can use a cubemap texture in Kanzi Studio you first have to create the texture images of the six cube faces for the cubemap. You can create the six texture images in the tool where you created the mesh object on which you want to use the cubemap texture, and import the images to Kanzi Studio. See Importing images.

Make sure that all faces of a cubemap texture use images of the same size and format. When the size and format of the images in a cubemap texture do not match, Kanzi uses the default cubemap texture.

For example, for all faces of a cubemap texture use images that are 256 by 256 pixels large and are 8-bit grayscale.

When the size and format of the images in a cubemap texture do not match, Kanzi Studio uses red type to mark such textures.
## Creating cubemap textures from dds images

To create a cubemap texture from a dds image, in the Assets click Import Assets and import a dds image that contains the images for all faces of the cubemap texture.

Kanzi Studio imports the dds image, creates a Cubemap Texture, and sets the faces of the texture to the corresponding images in the dds image.
## Creating cubemap textures from HDR images

To create cubemap textures from an hdr or exr image, either:

- In the Assets click Import Assets, select the image, and in the Create textures for HDR images dialog select the textures that you want to create.
- If you have already imported the image to your project, in the Library > Resource Files > Images press Alt and right-click the image and select the type of texture that you want to create.

See Using environment textures and Using image-based lighting cubemap textures.
## Creating cubemap textures

To create a cubemap texture:

1.

In the Assets, click Import Assets and import images that you want to use as the faces of the cubemap texture. See Importing images.
2.

In the Library, press Alt and right-click Materials and Textures, and select Cubemap Texture.

When you create a cubemap texture, Kanzi Studio marks it with red type because the texture does not yet have textures assigned for each face of the cubemap.
3.

In the Properties, set the Cubemap Images properties to the images that you want to use for your cubemap texture:

  - NegZ Image to the negative Z-face of the cubemap (the back face)
  - PosZ Image to the positive Z-face of the cubemap (the front face)
  - NegX Image to the negative X-face of the cubemap (the left face)
  - PosX Image to the positive X-face of the cubemap (the right face)
  - NegY Image to the negative Y-face of the cubemap (the bottom face)
  - PosY Image to the positive Y-face of the cubemap (the top face)

Avoid creating mipmaps from JPEG textures, because the JPEG image format causes the quality of the mipmaps to degrade.
4.

(Optional)

In the Properties set the Texture Settings properties.

Use the Texture Settings properties to control the texture filtering. Start by setting the Mipmap Mode property to the mipmap mode you want to use. Then set the Minification Filter and Magnification Filter properties to Linear. Note that using mipmaps increases the memory use.

Usually the best starting point for setting texture filtering is to set:

  - Minification Filter to Linear
  - Magnification Filter to Linear
  - Mipmap Mode to Nearest. If you are sure that the texture is not minified select Base, otherwise start with Nearest. For example, the default value for a Render Target Texture is Base. With this setting, the texture does not have mipmap levels and the base level is always sampled. See Using mipmaps.

Note that some texture formats are available with OpenGL ES versions higher than 2.0. To set the OpenGL ES version, in the main menu select Project > Properties and in the Properties set the Target Graphics API property.

For example, set the Target Graphics API property to OpenGL ES 3.0, import HDR and floating point images in .dds format, and set the color format of textures. See Using OpenGL ES 3.0+ in Kanzi.

Mipmap Mode |

Nearest sample |

Linear sample |

Base |

Number of samples: 1

Uses the nearest pixel in the texture. This combination is equal to point sample. It returns the crudest result of all combinations and can cause aliasing when minified.

Use this combination to get a very sharp result when magnifying the texture.  |

Number of samples: 4

Interpolates between four nearest pixels in the texture.

Use this combination to magnify gradients. However, do not use it for minification.  |

Nearest |

Number of samples: 1

Helps texture caching and helps reduce aliasing. However, it can produce a sharp transition when the texture is used on a flat surface.

Use this combination when you want good performance and cannot afford better quality on your target platform.

This combination is usually the fastest.  |

Number of samples: 4

Takes two samples from two mipmap levels and interpolates between these samples.

Use this combination as the starting point.

This combination is usually the best compromise between quality and performance.

If you know there is no minification, you can set Mipmap Mode to Base.  |

Linear |

Number of samples: 2

Takes one sample from two mipmap levels and interpolates between those samples.

Use this combination for special effects. For example, to implement the rim light effect.  |

Number of samples: 8

Takes four samples from two mipmap levels and interpolates between these samples.

Use this combination when you want the best quality and your platform is powerful enough to effortlessly render the result.

This combination has the largest negative impact on performance.  |

## Using a cubemap texture

To use a cubemap texture:

1.

In the Library > Materials and Textures > Materials, select a material that supports cubemap textures. In the Properties, set the TextureCube property to the cubemap texture that you want to use. See Creating cubemap textures and Creating textured materials.
2.

In the Node Tree, select the Model, Box, or Sphere node on which you want to use the cubemap texture. In the Properties, set the Material or Mesh Material property to the material that uses your cubemap texture.

## Using a cubemap texture as a skybox

To use a cubemap texture as a skybox:

1.

In the Library > Materials and Textures, press Alt and right-click Material Types, and select CubemapSkybox.

Kanzi Studio creates in the Library > Materials and Textures the CubemapSkybox material type and CubemapSkyboxMaterial, which supports showing a cubemap texture as a skybox.
2.

In the Library, select the CubemapSkyboxMaterial material. In the Properties, set the TextureCube property to the cubemap texture that you want to use to render a skybox.
3.

Create a Box or Sphere node that you use to render the skybox. In the Properties, set:

  - Mesh Material to CubemapSkyboxMaterial
  - The size of the node so that it is large enough to fit the content that you want to show inside it:

    - For a Box, set the Width, Height, and Depth properties.
    - For a Sphere, set the Radius property.

  - Generate Mesh Inside Out to enabled

When this property is enabled, Kanzi renders the cubemap texture inside the mesh.

4.

Position a Camera node inside the node that you created.

When you rotate the camera, in the Preview you can see the cubemap texture rendered as a skybox.
## Cubemap Texture property types

For a list of the available property types for cubemap textures, see Cubemap Texture and Texture.
