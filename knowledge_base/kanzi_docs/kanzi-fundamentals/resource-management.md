---
title: Resource management
source: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/resource-management.html
---

# Resource management


In Kanzi, a resource is an item that you can reuse in different parts of your application. For example, a Mesh Data resource defines the geometry of a Model node, and you can use the same Color Brush in different nodes to set the Foreground Brush or Background Brush properties.

Kanzi resource manager enables you to organize and reuse resources in your applications.
## Setting resources to nodes


In Kanzi you can set the resources to nodes either directly using the resource URL, or indirectly using the resource key. When you set resources in Kanzi Studio, it by default assigns all resources using the URL. If you want to use the indirect setting in Kanzi Studio you need to create a key for the resource in a resource dictionary, and in the property select that key. Because key lookup is hierarchical you can define what the key resolves to by creating resource dictionary entries in the tree.

Setting resources using resource keys enables you to:
|   |   |    |   |    |
|

Create and apply different skins or themes to change the appearance of your application. |   |

Create different versions of your application for different languages and locales. |   |

Override resources to modularize content. |

You can share the resources to decrease the memory and runtime requirements of your application. This enables you to reuse the same resource, or to change the resource so that the change is reflected in the entire application. For example, that way you can share a brush that is animated.

Kanzi offers many tools to manage the resources while the application is running. In Kanzi you can:

- Load resources in multiple threads to use multiple cores in your device and speed up the start up or loading time of your application. See Loading resources in parallel.
- Asynchronously load resources to improve application startup or responsiveness. See Loading node prefab resources asynchronously.
- Select image from the device storage. See Loading images from the file system.
- Localize your application. See Localizing applications and Tutorial: Localize your application.
- Create and apply a theme to change the appearance of your application. See Theming your applications.
- Find out whether a resource is in use and unload unused resources. This allows you to create complex applications where not all resources can fit into memory at once. See Setting how Kanzi Engine handles unused resources.

## Kanzi resource types

|
|   |

Alias

Use an Alias to get consistent access to a Kanzi node. You can use aliases to access nodes both in Kanzi Studio and using the Kanzi Engine API.  |

Using aliases |      |
|
|   |

Animation Clip

Use an Animation Clip to combine Animation Data resources into more complex animations. You can reuse the same Animation Data resources in different Animation Clip items. Use an Animation Child Clip to create hierarchical animations.  |

Animations

Editing animation clips

Editing timeline sequences  |
|   |

Animation Data

Use an Animation Data resource to define the keyframes and target property of a keyframe animation. One Animation Data resource can target only one property or property field. Animation Data resources are independent from the nodes they target. This allows you to reuse Animation Data resources to animate different nodes.  |   |
|   |

Timeline Sequence

Use a Timeline Sequence to combine a set of Timeline Entry resources.  |   |      |
|
|   |

Brushes

Use brushes to set the background of 2D nodes. In Kanzi, all 2D nodes by default have transparent background.  |

Using brushes |      |
|
|   |

Fonts

Use a font to render text. The default font in Kanzi is Fira Sans Regular. To use your own font, import it to your Kanzi Studio project.  |

Importing fonts |      |
|
|   |

Materials

Use materials to set the appearance of 3D nodes and Material Brush brushes.  |

Material types and materials |
|   |

Mesh Data

A mesh is a collection of vertices, edges, and faces that define the shape of a solid object in 3D with flat faces and straight edges and the triangles that form the surface between the points.  |

Using meshes |
|   |

Textures

Use textures to show content in Image nodes, to set the look of textured materials, and to show content in Texture Brush brushes. You can create textures from common image file formats.  |

Textures |      |
|
|   |

Render Pass Prefabs

Use render passes to define the rendering of 3D content in your Kanzi application.

In a render pass prefab, you can create a hierarchy of render passes to achieve a specific rendering result.  |

Rendering |
|   |

Object Source

Use object sources and filters to tell a Draw Objects render pass which nodes in your Kanzi application you want to render. Root Object Source contains all nodes in the node tree of the currently active Scene node.  |

Using object sources |      |
|
|   |

Resource Dictionary

A resource dictionary is a collection of resource IDs pointing to resources. You can add a resource dictionary to any node.  |

Using resource dictionaries |      |
|
|   |

State Managers

Use a State Manager to create different states in your Kanzi application.  |

State manager |      |
|
|   |

Styles

Use styles to set the property values of one or more nodes of a certain type.  |

Using styles |      |
|
|   |

Text Resources

A text resource is a text string used by Text Block and Text Box nodes.  |

Text |      |
|
|   |

Trajectories

Use trajectories as paths along which Trajectory Layout 3D and Trajectory Layout 2D nodes arrange their child nodes, and along which Trajectory List Box 3D nodes move their items.  |

Trajectories |      |
## Importing resource assets to your project


You can create some resources directly in Kanzi Studio (for example, brushes and animations). For some resources you have to import assets created in third-party tools (for example, textures and meshes). See Importing.
## Resource URLs


The most basic way to refer to a resource is a URL. URLs can refer to resources inside a kzb file or files on device storage. When you set a resource in a property you need to provide the URL of the resource. When you do that in Kanzi Studio in the Properties window, Kanzi does that automatically for the resource you select. When you set resource properties using the API, you need to provide the resource URL manually. To find the URL of a resource in your project, in Kanzi Studio right-click the resource and select Copy .kzb URL. To reference files on the device storage use the `file:///` URL format.

When using the API you can specify a resource object directly. Nodes that accept resource objects usually provide a method overload that accepts such objects. For example, to set the image in an Image node use `Image2D::setImage`.
## Resource dictionary


A resource dictionary is a collection of a key-value pair entries for each resource. You can define a resource dictionary in any node. Keys provide means to specify resources indirectly: instead of specifying a resource or a URL to a node, you can specify a key. Kanzi resolves the resource dynamically by looking up the nearest resource dictionary where the key defines to which resource it resolves to. When a key needs to be resolved to an item, the resolving process starts checking the resource dictionaries from the node that uses the key: if a dictionary of that node contains the key, the node uses that key, if not, the node checks its parentsâ dictionaries until it finds the key. This process continues recursively until the root of the node tree. If the node does not find the key, it is up to the node to decide what happens then. For example, it is a valid case if an Image node does not show an image. Kanzi controls fail softly when resources are not found, but in plugins it is up to the author of the plugin to define what happens.
## Default resources


Kanzi comes with default resources that enable you to create applications faster. For example, when you create a Scene, Kanzi provides a default render pass, when you create a Text Block or a Text Box node, Kanzi provides a default font. If you need to customize the default Kanzi resources, create or import the resources that fit your needs and use them instead of the Kanzi default resources.

When you create a kzb file from your Kanzi Studio project the default Kanzi resources are included in the kzb file by default.
## Resource manager


The resource manager manages the lifetime, loading, and unloading of resources. You can access the resource manager using the Kanzi API and you can use it to specify the lifetime policies for resources and to remove unused resources. To specify whether resources are always kept in memory, or unloaded when they are not needed, you specify a policy. You can specify a policy globally for the resource manager, or for each resource. If the policy is to keep the resources in memory, you can request manual removal based on the logic of your application. For example, you can manually remove resources when you change a Page node in your application to load a large amount of resources for a new Page node.

The resource manager allows you to define in which memory the GPU resources in your Kanzi application are stored. For example, to set this for a texture in Kanzi Studio in the Library > Materials and Textures > Textures select a texture and in the Properties set the GPU Memory Type property:

- GPU Only. The resource is deployed to GPU memory and released from the RAM immediately after deployment. Kanzi keeps the resource in the GPU memory unless you release it in the application code.
- GPU and RAM. The resource is deployed to the GPU memory. Kanzi keeps the resource in both GPU and RAM memory and manages the resource based on the platform and the application. Kanzi automatically manages the unloading of resources. Compared to GPU Only, this consumes more RAM, but provides faster resume times, for example, on Android.
- RAM Only. The resource is deployed to the GPU only when instructed in the application code. Kanzi keeps the resource in the GPU memory and unloads it when you release it in the application code.

## Pause and resume


When your Kanzi application is in the paused state (`MainLoopState::Paused`):

- On Android, by default, the GPU resources that are not stored in a kzb file become invalid. If your application uses custom resources that it does not load from kzb files, make sure that you reload and redeploy those resources manually when needed. Kanzi automatically restores all other resources.
- On other platforms, Kanzi does not by default invalidate the GPU resources.


You can set in the application configuration how to handle GPU resources when your application is in the paused state. In the Application configuration reference, see HandleGPUResources.
