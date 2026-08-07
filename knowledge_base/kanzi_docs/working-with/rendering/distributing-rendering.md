---
title: Distributing rendering across several frames
source: https://docs.kanzi.com/4.1.0/en/working-with/rendering/distributing-rendering.html
---

# Distributing rendering across several frames

You can distribute the rendering workload across several frames to reduce the amount of work and time required to render one whole frame.

To distribute the rendering workload, you can:

- Use the Progressive Rendering Viewport 2D node to distribute the rendering between multiple render passes. See Using the Progressive Rendering Viewport 2D node.
- Set the update rate of the composition targets of a Composition Target render pass. See Distributing the rendering of composition targets.
- Set the update rate of cubemap reflections rendered by a Cubemap render pass. See Distributing the rendering of cubemap reflections.

## Using the Progressive Rendering Viewport 2D node

Use the Progressive Rendering Viewport 2D node to distribute the rendering workload across several frames to reduce the amount of work and time required to render one whole frame.

Kanzi updates all content rendered by a Progressive Rendering Viewport 2D node every n frames, where n is the number of child render passes of the render pass prefab that the Progressive Rendering Viewport 2D node uses.

For example, if a Progressive Rendering Viewport 2D node uses a Group render pass prefab that has four child render passes, Kanzi updates the content rendered by the Progressive Rendering Viewport 2D node every four frames. When you use a Progressive Rendering Viewport 2D node to render interactive content, this can make such content less responsive.

When you divide complex and rendering-intensive content into even parts, you can use a Progressive Rendering Viewport 2D node to improve the rendering performance of your application.

In a Progressive Rendering Viewport 2D, Kanzi renders one render pass in one frame. To keep the framerate from fluctuating, distribute the rendering into even parts among the render passes used by a Progressive Rendering Viewport 2D node. To distribute the rendering into even parts, make sure that each render pass renders:

- Approximately the same amount of polygons
- Shaders that are of similar complexity
- Textures that are similar in size
- Similar number of textures

For example, use the Progressive Rendering Viewport 2D node to render the content at different update frequencies. To render part of the content at 60 fps and the rest of the content at 30 fps, all content together must render in 16 ms or less (1000 ms / 60 fps = 16.6 ms). If the longest time it takes to render your 60 fps content is 10 ms, to display the rest of the content at 30 fps:

1.

Split the content that you want to render at 30 fps into two or three parts, so that each part renders in 6 ms or less.

To render your 60 fps content every frame at 60 fps, the total render time of both 60 fps and 30 fps content must not be higher than 16.6 ms.
2.

Use the Progressive Rendering Viewport 2D node to render the 30 fps content.

If you split the content into two parts, Kanzi renders the entire 30 fps content every two frames. If you split the content into three parts, Kanzi renders the entire 30 fps content every three frames.
**Tip:** When splitting content into parts, to find out how much time it takes to render each part:
1.
To display the Performance HUD, either:
- In the Kanzi Studio Preview, click  to enter the Analyze mode. Right-click  and select the Performance HUD. See Analyzing your application in the Preview.
- Set the `PerformanceInfoLevel` in the `application.cfg` file or `Application::onConfigure` function when using the Kanzi Engine API. See PerformanceInfoLevel.
2.
Hide the content that you do not want to render. In Kanzi Studio in the Node Tree, select the nodes that you want to hide and either:
- Press Ctrl H
- In the Properties, add and disable the Node > Visible property.

Learn how to use the Progressive Rendering Viewport 2D node by completing a tutorial. See Tutorial: Progressive rendering.

To use the Progressive Rendering Viewport 2D node:

1.

Use Kanzi filters or Combine Object Source items to collect the nodes whose rendering you want distribute across several frames. See Filters and Using object sources.

For example, to collect the nodes using a Tag Filter:

  1.

In the Node Tree, select the nodes that you want to render across several frames. In the Properties, use the Tags property to mark the nodes for rendering in different render passes. See Using tags.

For example, to distribute the rendering into two parts:

    1.

Tag the nodes that you want to render with the first render pass with a tag Pass 1.
    2.

Tag the nodes that you want to render with the second render pass with a tag Pass 2.

  2.

In the Library, press Alt and right-click Rendering and create as many Tag Filter filters as you have tags with which you marked nodes in the previous step. In the Properties, set the Included Tags property to the tag you want to collect with that Tag Filter.

For example, name the first Tag Filter filter Tag Filter Pass 1, and in the Properties, set the Included Tags property to Pass 1.

2.

In the Library > Rendering, press Alt and right-click Render Pass Prefabs, and create the Group render pass prefab that the Progressive Rendering Viewport 2D node uses to render its content.
3.

In the Library, press Alt and right-click the Group render pass that you created in the previous step and create:

  1.

Clear render pass
  2.

For each collection of nodes that you created in the first step, a Gather Lights render pass and inside it a Draw Objects render pass

4.

In the Library, select each Draw Objects render pass that you created in the previous step. In the Properties, set the Object Source property to the filter or Combine Object Source item that collects the nodes that you want this render pass to render.

For example, select the first Draw Objects render pass and set the Object Source property to Tag Filter Pass 1.
5.

In the Node Tree, create a Progressive Rendering Viewport 2D node. In the Properties, set the Render Pass Prefab property to the Group render pass.

You set Kanzi to render the Progressive Rendering Viewport 2D node using the Group render pass prefab.
6.

In the Node Tree, add to the Progressive Rendering Viewport 2D node the content that you collected in the first step.
7.

In the Library, in the Clear render pass, add and set the Clear Color 0 property to produce meaningful color output, including the alpha channel.

### Using animations with progressive rendering

You cannot use an Animation Player or a state transition to animate nodes in a Progressive Rendering Viewport 2D node.

To use animations with progressive rendering:

1.

In the Node Tree select a Progressive Rendering Viewport 2D node where you want to use an animation.
2.

In the Properties set the Timeline property to the Animation, Animation Clip or Timeline Sequence you want to use.

### Applying anti-aliasing to content rendered by a Progressive Rendering Viewport 2D node

To apply anti-aliasing to the content rendered by a Progressive Rendering Viewport 2D node, in the Node Tree select the Progressive Rendering Viewport 2D node, in the Properties add the Multisample Level property, and set it to the number of anti-aliasing samples that you want to use.

See the documentation of the device on which you want to run your Kanzi application for supported values, because the number of anti-aliasing samples depends on the device. If you set the Multisample Level property to a value that your device does not support, Kanzi Engine clamps the value to the largest value supported by the device driver.
### Progressive Rendering Viewport 2D property types and messages

For a list of the available property types and messages for the Progressive Rendering Viewport 2D node, see Progressive Rendering Viewport 2D.
## Distributing the rendering of composition targets

To reduce the amount of per-frame rendering workload, you can set the rate at which Kanzi updates the composition targets of a Composition Target render pass.

To distribute the rendering of composition targets:

1.

In the Library > Rendering > Render Pass Prefabs, select a Composition Target render pass that you use to render content to a composition target. See Rendering content to one composition target, Rendering content to multiple composition targets, and Rendering to texture.
2.

In the Properties, add and set:

  - Render Pass > Update Rate to the rate at which you want to update the content that the Composition Target render pass renders:

    - To update the content every frame, set to 1. This is the default value.
    - To update the content every other frame, set to 2, to update the content every fourth frame, set to 4, and so on.
    - To render the content only once, set to 0.

  - Render Pass > Update Rate Offset to the number of frames by which you want to offset the rendering rate.

This way, you can distribute the rendering of multiple render passes to different frames.

For example, when you have two Composition Target render passes whose content you update every other frame, in one of those render passes, set the Update Rate Offset to 1. This way, Kanzi updates the content rendered by those render passes at alternating frames.
**Tip:** To set the Update Rate and Update Rate Offset properties to different values in multiple Viewport 2D nodes that use the same render pass prefab, you can customize the instances of that render pass prefab. See Customizing instances of render passes.

## Distributing the rendering of cubemap reflections

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
