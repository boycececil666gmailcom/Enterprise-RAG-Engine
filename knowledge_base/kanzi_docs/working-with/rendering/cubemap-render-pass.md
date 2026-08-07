---
title: Creating cubemap reflections
source: https://docs.kanzi.com/4.1.0/en/working-with/rendering/cubemap-render-pass.html
---

# Creating cubemap reflections

Use the Cubemap render pass to create dynamic reflections of the environment on the surface of 3D nodes.

Cubemap render pass uses a specific Camera node that functions as a reflection probe. You position this Camera node in the center of the nodes that show meshes on whose surface you want to reflect the environment.

Cubemap render pass renders itself and its child render passes to an active composition target, such as a Cubemap Render Target Texture and the Result Texture of the Cubemap render pass.

To reflect the environment on the surface of nodes, set the cubemap composition target as the cubemap texture of the materials that those nodes use.

Each Scene node can have one reflection probe.
## Using the Cubemap render pass to create cubemap reflections

To create cubemap reflections:

1.

In your Kanzi Studio project, in a Scene node, create:

  - Nodes that show the meshes on whose surface you want to reflect the environment.

For example, create a car whose body, windows, headlights, and rims you want to reflect the environment.
  - The environment surrounding the nodes that you want to reflect.

For example, create a Box node that uses a cubemap texture as a skybox. See Using a cubemap texture as a skybox.

2.

For each node whose surface you want to reflect the environment:

  1.

In the Node Tree, select that node.
  2.

In the Properties next to the material, click  to go to that material, and set the Material Type property to a material type that supports cubemap reflections.

For example, use the VertexPhongTexturedCube material type. If your project does not contain the VertexPhongTexturedCube material type, in the Library > Materials and Textures press Alt and right-click Material Types, and select VertexPhongTexturedCube.

To set any Kanzi default material type to support cubemap reflections:

  1.

In the Library, select that material type.
  2.

In the Properties in the Preprocessor Definitions, set KANZI_SHADER_USE_REFLECTION_CUBE to 1.

3.

Render all nodes in a Scene node:

  1.

In the Library > Rendering, press Alt and right-click Render Pass Prefabs, select Group render pass, and name it Cubemap Reflections.

Group render pass allows you to collect render passes so that you can refer to a single render pass prefab in your Viewport 2D node.
  2.

In the Node Tree, select the Viewport 2D node that contains your scene. In the Properties, set the Render Pass Prefab property to the Cubemap Reflections render pass prefab.

You set Kanzi to render the Viewport 2D node using the Cubemap Reflections render pass prefab. The Cubemap Reflections render pass prefab does not have any child render passes, which is why the Preview does not show any content.
  3.

In the Cubemap Reflections render pass prefab, create the render passes that render to the screen the content of the Viewport 2D node.

For example, create a Default render pass.

Default render pass contains a basic set of render passes that first render opaque nodes and then transparent nodes.

4.

Use a Cubemap render pass to render the environment to a cubemap composition target:

  1.

Create a filter that picks the nodes that belong to the environment.

For example, tag with the tag Car the node that contains all the nodes that belong to the car. In the Library > Rendering > Object Sources, create a Tag Filter named Environment, which excludes the Car tag.

See Filters.
  2.

In the Cubemap Reflections render pass prefab, create a Cubemap render pass. In the Cubemap render pass, create the render passes that draw the environment.

For example, create:

    1.

Clear render pass.

This render pass clears the depth buffer.
    2.

Gather Lights render pass.

Gather Lights render pass allows you to collect from a list of nodes the light nodes for lighting 3D nodes in a scene.
    3.

In the Gather Lights render pass, create a Draw Objects render pass and name it Draw Environment. In the Properties, set the Object Source property to the filter that picks only the nodes that belong to the environment.

You use the Object Source property to tell a Draw Objects render pass which nodes you want it to render.

The Cubemap render pass draws the environment to a cubemap composition target, which is why you cannot see the result in the Preview.

5.

Render the cubemap reflections:

  1.

In the Library, press Alt and right-click Materials and Textures and select Cubemap Render Target Texture.

Use a Cubemap Render Target Texture to render a Cubemap render pass to a cubemap texture.
  2.

In the Properties, set the Width and Height property to the dimensions that you want for the Cubemap Render Target Texture.

This way, you set the accuracy of the cubemap reflections.
  3.

In the Library > Rendering > Render Pass Prefabs, select the Cubemap render pass. In the Properties, add and set the Composition Target property to the Cubemap Render Target Texture that you created.
  4.

In the Library > Materials and Textures > Materials, select each material with which you want to render the cubemap reflections. In the Properties, set the TextureCube property to the Cubemap Render Target Texture that you created.

This way, you set Kanzi to render the result of the Cubemap render pass in the nodes that use these materials.
  5.

(Optional) In each material, set any other properties that you want to use to adjust the appearance of that material.

For example, adjust the CubemapColor property Lightness (L) property field to set the brightness of the reflections.

6.

Position the cubemap reflections:

  1.

In the Scene node that contains nodes on which you want to reflect the environment, create a Camera node and position it in the center of those nodes.

You use this camera as a reflection probe, which captures a spherical view of its surroundings in all directions.
  2.

In the Library, select the Cubemap render pass. In the Properties, add the Override Camera property and set it to the Camera node that you created.

This way, you tell the Cubemap render pass the position from which you want it to capture the cubemap of the environment.

In the Preview, when you move the car, the body, windows, headlights, and rims of the car reflect their changing surroundings.

7.

(Optional) Configure the Cubemap render pass to suit your needs.

For example, you can set the rate at which Kanzi updates the cubemap reflections. See Distributing the rendering of cubemap reflections across several frames.

## Distributing the rendering of cubemap reflections across several frames

To reduce the amount of per-frame rendering workload, you can set the rate at which Kanzi updates:

- The content that a Cubemap render pass renders.
- The faces in the cubemap texture to which a Cubemap render pass renders its content.

To distribute the rendering of cubemap reflections

1.

In the Library > Rendering > Render Pass Prefabs, select a Cubemap render pass that you use to render cubemap reflections. See Using the Cubemap render pass to create cubemap reflections.
2.

In the Properties, add and set:

  - Render Pass > Update Rate to the rate at which you want to update the content that the Cubemap render pass renders:

    - To update the content every frame, set to 1. This is the default value.
    - To update the content every other frame, set to 2, to update the content every fourth frame, set to 4, and so on.
    - To render the content only once, set to 0.

  - Face Update Rate to the number of cubemap faces that you want to update in one frame in the Result Texture of the Cubemap render pass.

The Result Texture contains the cubemap texture to which the Cubemap render pass renders itself and its child render passes.

By default, Kanzi updates all six cubemap faces at the rate that you set with the Update Rate property.

For example, when you set the Face Update Rate to 3 and the Update Rate to 2, Kanzi updates the cubemap faces at this rate:

Frame |

Cubemap faces |

n |

+x, -x, +y |

n + 1 |

- |

n + 2 |

-y, +z, -z |

n + 3 |

- |

n + 4 |

+x, -x, +y |

n + 5 |

- |

n + 6 |

-y, +z, -z |

n + 7 |

- |
  - Render Pass > Update Rate Offset to the number of frames by which you want to offset the rendering rate.

This way, you can distribute the rendering of multiple render passes to different frames.

For example, when you set the Update Rate Offset to 1, Kanzi updates the first cubemap faces at the frame n + 1.
