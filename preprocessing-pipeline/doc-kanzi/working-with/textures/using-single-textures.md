---
title: Using single textures
source: https://docs.kanzi.com/4.1.0/en/working-with/textures/using-single-textures.html
---

# Using single textures

Single textures use a single image for the texture.

Before you can create a texture in Kanzi Studio you first have to have an image you use in that texture. You can create the texture image in a third-party tool and import the image to Kanzi Studio. See Importing images.
## Creating a single texture

To create a single texture:

1.

In the Library press Alt and right-click Materials and Textures and select Single Texture.
2.

In the Properties set the Image property to the image you want to use for the texture.

Avoid creating mipmaps from .jpeg textures, because the .jpeg image format causes the quality of the mipmaps to degrade.
3.

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

## Using a single texture

You can use single textures on Model and Image nodes:

- To use a texture on a mesh, set the material that supports textures to use your texture, and then set the mesh to use that material. See Creating textured materials.
- To use a single texture on an Image node, in the Node Tree select the Image node, and in the Properties set the Image property to the single texture you want to use on that Image node. See Using the Image node.

## Single Texture property types

For a list of the available property types for single textures, see Single Texture and Texture.
