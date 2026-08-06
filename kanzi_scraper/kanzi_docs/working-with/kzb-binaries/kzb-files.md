---
title: Kzb files
source: https://docs.kanzi.com/4.1.0/en/working-with/kzb-binaries/kzb-files.html
---

# Kzb files


A kzb file contains contents of a Kanzi Studio project. To run your Kanzi application, you must export the contents of the Kanzi Studio project of that application to a kzb file.

See Using kzb files.

When the user starts a Kanzi application, Kanzi loads the kzb files of the application. Kanzi loads the content from a kzb file to RAM and GPU memory when it needs to render that content. See Resource management.

If your application uses more than one kzb file, you can set in the application configuration which kzb files the Kanzi application loads on startup. See Application configuration > Loading.
## Contents of a kzb file


The contents and size of a kzb file depend on your Kanzi Studio project and how you configure the kzb export in Kanzi Studio. The size of the kzb file impacts the time it takes to load your application and the amount of resources that the application uses.

You can reduce the size of a kzb file by excluding unused project items from the kzb export. For example, this way you can keep in a project items that you do not use in your Kanzi application. See Excluding items from an application.

Kanzi Studio does not export to a kzb file the content of the Description property. The purpose of the property is to store the documentation of project items, which a Kanzi application does not use. See Documenting a project.

By default, the main kzb file that Kanzi Studio creates from your project contains:
|

Content |

Documentation |
|

Animations

Use animation resources to create keyframe animations.  |

Animations |
|

Brushes

Use Brushes to set the appearance of the foreground and background of 2D nodes. For example, with brushes you can define the color of text in a Text Block 2D node, fill a background of a 2D node with an image pattern, or apply a material effect on 2D content.  |

Using brushes |
|

Effects

Use effects to apply post-processing effects to 2D nodes.  |

Effects for 2D nodes |
|

Font families

Use font families to group fonts in your project.  |

Importing fonts |
|

Localization resources

Localization involves creation and use of different resources, such as text, textures, and styles, for locales that you want to support in your application.

When you mark localization resources as a locale pack, Kanzi Studio exports the marked resources to a separate kzb file. This way you can reduce the size of the main kzb file and load resources for a locale only when the user uses that locale.  |

Localization

Using locales  |
|

Materials

Use materials to set the appearance of nodes.  |

Using materials |
|

Material types

Material types define the property types of a material. By adjusting material property values defined by a material type, you set the appearance of a material. Each material type has a vertex shader and a fragment shader, which set the type of properties you can use in a material.  |

Using material types |
|

Meshes

A mesh is a collection of vertices, edges, and faces that define the shape of a solid object in 3D with flat faces and straight edges and the triangles that form the surface between the points.  |

Using meshes |
|

Message types

Use messages to notify about events and exchange information between nodes.  |

Using messages |
|

Nodes from the Node Tree window

The nodes in the Node Tree define the structure of a Kanzi application that Kanzi loads at application startup. Use nodes to show content, to set layouts, and to implement logic and interactions in your Kanzi application.  |

Presentation |
|

Object sources

Use object sources and filters to tell a Draw Objects render pass which nodes in your Kanzi application you want to render. Root Object Source contains all nodes in the node tree of the currently active Scene node.  |

Using object sources |
|

Page transitions

Use page transitions to set how Kanzi transitions between Page and Page Host nodes.  |

Setting transitions between Page nodes |
|

Prefabs from the Prefabs window

Use prefabs (prefabricated templates) to structure your application and to create consistent interfaces. Prefabs allow you to create the building blocks of your application and make the application easier to maintain.  |

Using node prefabs |
|

Property types

Properties provide the means to specify and examine the state, appearance, and behavior of nodes. For example, a property can define a color, indicate whether a button is pressed, or specify the alignment of an item.

Each property in Kanzi is described by a property type. The property type describes the name and category of the property and type of data and values the property can have.

You can create custom property types to support the logic of your Kanzi application.  |

Property types

Creating property types

Property system  |
|

Render pass prefabs

Use render passes to define the rendering of 3D content in your Kanzi application.

In a render pass prefab, you can create a hierarchy of render passes to achieve a specific rendering result.  |

Rendering |
|

Resource dictionaries

Use a resource dictionary to store resource IDs in a node. By default, the Screen node and the root nodes of prefabs contain resource dictionaries, but you can add a resource dictionary to any node.  |

Using resource dictionaries |
|

Resource files

Kanzi Studio lists in the Library > Resource Files references to files in the resource directories of a Kanzi project. Kanzi Studio synchronizes the content of Resource Files with the files in the resource directories.

When creating the main kzb file, Kanzi Studio exports all files in the resource directories, with these exceptions:

- Kanzi Studio does not export the files in the 3D Assets directory to the kzb file. The assets that Kanzi Studio imported from the 3D files, such as meshes, animations, and morphs, are included in the kzb export.
- By default, Kanzi Studio exports the online shader source code in the Shaders directory to the kzb file. If you use binary shaders, you can reduce the size of the kzb file by disabling online shader exporting.
  |

Using resource files

Using binary shaders  |
|

State managers

Use a State Manager to create different states in your Kanzi application.  |

State manager |
|

Styles

Use styles to set the property values of one or more nodes of a certain type.  |

Using styles |
|

Tags

Use tags to group, find, and filter nodes in your project. You can assign multiple tags to a single node.  |

Using tags |
|

Textures

Use textures to show content in Image nodes, to set the look of textured materials, and to show content in Texture Brush brushes. You can create textures from common image file formats.  |

Textures |
|

Themes

Themes enable you to use a single Kanzi Studio project for multiple variants of your product.

When you mark theme resources as a theme resource pack, Kanzi Studio exports the marked resources to a separate kzb file. This way you can reduce the size of the main kzb file and load resources for a theme only when the user uses that theme.  |

Theming your applications

Exporting Themes  |
|

Trajectories

Use trajectories as paths along which Trajectory Layout 3D and Trajectory Layout 2D nodes arrange their child nodes, and along which Trajectory List Box 3D nodes move their items.  |

Trajectories |
