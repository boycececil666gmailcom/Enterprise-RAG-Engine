---
title: Using render target textures
source: https://docs.kanzi.com/4.1.0/en/working-with/textures/using-render-target-textures.html
---

# Using render target textures


Use a Render Target Texture to render content to a texture or to apply anti-aliasing to only a part of your application. You can use render target textures like any other texture. For example, you can use it in a Texture Brush or as an image in an Image node.

See Applying anti-aliasing and Textures.

For example, if your Kanzi application has more than one scene, you can use render target textures to show the content of other scenes in the current scene.
## Rendering content to a texture


To render content to a texture:

1.

In the Library press Alt and right-click Materials and Textures and select Render Target Texture.
2.

In the Node Tree create or select a 2D node the content of which you want to render to a texture.

For example, select a Viewport 2D node that contains the content that you want to render to a texture.
3.

In the Node Tree select the node that you created or selected in the previous step and in the Properties add and set:

  - Render Target to the Render Target Texture to which you want to render the content of the selected node.
  - Off-Screen Rendering and enable the property.

4.

(Optional) To set Kanzi to render the content to the texture only once, in the Properties add the Caching Mode property and set it to Enabled.

This way you set Kanzi to cache the node, and to keep rendering the node from the cache image. For example, enable caching for a node for which you want Kanzi to create the render target texture only once at application startup. See Caching 2D nodes.
5.

Apply the Render Target Texture that you created in the first step to a node where you want to show the content of the node that you created in the second step.

You can use the Render Target Texture in a Texture Brush or as an image in an Image node.

For example:

  1.

In the Node Tree press Alt and right-click and select Empty Node 2D.
  2.

In the Node Tree select the Empty Node 2D node, in the Properties add the Background Brush property, and in the dropdown menu select + Texture Brush.
  3.

Next to the Background Brush property click  and set the Brush Texture property of the Texture Brush to the Render Target Texture you want to show in the Empty Node 2D you created in the first step.
  4.

In the Node Tree select the Empty Node 2D, and in the Properties add and set the Layout Width and Layout Height properties to the size in which you want to show the content of the Render Target Texture.

6.

(Optional) In the Library select the Render Target Texture.

In the Properties, you can set the Height and Width of the Render Target, or use the Automatic setting to set the size of the Render Target based on the size of the node where it is used. You cannot yet use this property with a render pass.

Use the Texture Settings properties to control the texture filtering. Start by setting the Mipmap Mode property to the mipmap mode you want to use. Then set the Minification Filter and Magnification Filter properties to Linear. Note that using mipmaps increases the memory use.

Usually the best starting point for setting texture filtering is to set:

  - Minification Filter to Linear
  - Magnification Filter to Linear
  - Mipmap Mode to Nearest. If you are sure that the texture is not minified select Base, otherwise start with Nearest. For example, the default value for a Render Target Texture is Base. With this setting, the texture does not have mipmap levels and the base level is always sampled. See Using mipmaps.


Note that some texture formats are available with OpenGL ES versions higher than 2.0. To set the OpenGL ES version, in the main menu select Project > Properties and in the Properties set the Target Graphics API property.

For example, set the Target Graphics API property to OpenGL ES 3.0, import HDR and floating point images in .dds format, and set the color format of textures. See Using OpenGL ES 3.0+ in Kanzi.
|

Mipmap Mode |

Nearest sample |

Linear sample |
|

Base |

Number of samples: 1

Uses the nearest pixel in the texture. This combination is equal to point sample. It returns the crudest result of all combinations and can cause aliasing when minified.

Use this combination to get a very sharp result when magnifying the texture.  |

Number of samples: 4

Interpolates between four nearest pixels in the texture.

Use this combination to magnify gradients. However, do not use it for minification.  |
|

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
|

Linear |

Number of samples: 2

Takes one sample from two mipmap levels and interpolates between those samples.

Use this combination for special effects. For example, to implement the rim light effect.  |

Number of samples: 8

Takes four samples from two mipmap levels and interpolates between these samples.

Use this combination when you want the best quality and your platform is powerful enough to effortlessly render the result.

This combination has the largest negative impact on performance.  |

## Render Target Texture property types


For a list of the available property types for render target textures, see Render Target Texture and Texture.
