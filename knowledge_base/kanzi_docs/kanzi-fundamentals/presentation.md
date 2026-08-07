---
title: Presentation
source: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/presentation.html
---

# Presentation

## Node tree


Node tree defines the content structure and its layout on the screen.

The node tree is constructed from nodes that display content (for example, Image node) and implement logic (for example, Button 2D node). The same node tree supports 2D and 3D nodes and provides the means to connect them.

The relationship between the nodes in the node tree is very important and defines how several Kanzi core technologies work. Rendering order, layout, property and resource inheritance, and input and message propagation all depend on the relationship between parent and child nodes in the node tree.

Kanzi offers the tools to modularize and reuse parts of the node tree (for example, prefabs).
## Nodes available in Kanzi

### Content control nodes

|   |

Image.

Use the Image node to show a bitmap image.

See Using the Image node.  |
|   |

Model.

Use the Model node to show the imported meshes in your Kanzi application.

See Using imported meshes.  |
|   |

Nine Patch Image.

Use the Nine Patch Image node to create a scalable button background that scales with the size of the Nine Patch Image content.

See Using the Nine Patch Image node.  |
|   |

Page.

Use the Page nodes to create the structure of the user interface in your application, and the Page Host nodes to manage navigation requests and transitions between Page nodes under a Page Host node. For example, you can use Page and Page Host nodes to create different parts of the user interface in your Kanzi application, such as Page Host nodes Home, Media, Navigation, or Settings screens, each having their own hierarchy of Page and Page Host nodes.

See Using the Page and Page Host nodes.  |
|   |

Text Block 3D and Text Block 2D.

Use the Text Block nodes to show a small amount of text in your application.

See Using the Text Block nodes.  |
|   |

Viewport 3D and Viewport 2D.

Use the Viewport nodes to set the size of a render target surface onto which Kanzi projects content.

See Viewport nodes.  |
### Interactivity control nodes

|   |

Button 3D and Button 2D.

Use the Button nodes to create interactions through clicking, tapping, or pressing a key on the keyboard.

See Using the Button nodes.  |
|   |

Scroll View 3D and Scroll View 2D.

Use the Scroll View nodes to define an area where to generate scrolling messages in response to user input and physics-based animation.

See Using the Scroll View nodes.  |
|   |

Slider 3D and Slider 2D.

Use the Slider nodes when you want to allow users to change numerical values using a visual indicator between a minimum and a maximum value.

See Using the Slider nodes.  |
|   |

Text Box 3D and Text Box 2D.

Use the Text Box nodes to add single-line text input to your application.

See Using the Text Box nodes.  |
|   |

Toggle Button 3D and Toggle Button 2D.

Use the Toggle Button nodes to create interactions through buttons that can have multiple toggle states.

See Using the Toggle Button nodes.  |
|   |

Toggle Button Group 3D and Toggle Button Group 2D.

Use the Toggle Button Group nodes to allow users to select only one option from a set of options that are mutually exclusive.

See Using the Toggle Button Group nodes.  |
### Layout control nodes

|   |

Content Layout 3D and Content Layout 2D

Use the Content Layout nodes to present content in a UI control as a single item.

See Using the Content Layout nodes.  |
|   |

Dock Layout 3D and Dock Layout 2D

Use the Dock Layout nodes to place nodes relative to each other along the sides of a Dock Layout node.

See Using the Dock Layout nodes.  |
|   |

Empty Node 3D and Empty Node 2D

Use the Empty Node nodes to group nodes and to set property values of their child nodes.

See Using the Empty Node nodes.  |
|   |

Flow Layout 3D and Flow Layout 2D

Use the Flow Layout nodes to arrange nodes along a line. When a line runs out of space, the Flow Layout node places its child nodes in a new line.

See Using the Flow Layout nodes.  |
|   |

Grid Layout 3D and Grid Layout 2D

Use the Grid Layout nodes to arrange nodes in a grid.

See Using the Grid Layout nodes.  |
|   |

Stack Layout 3D and Stack Layout 2D

Use the Stack Layout nodes to arrange nodes next to each other on the selected axis.

See Using the Stack Layout nodes.  |
|   |

Trajectory Layout 3D and Trajectory Layout 2D

Use the Trajectory Layout nodes to arrange items along a trajectory path.

See Using the Trajectory Layout nodes.  |
### Container control nodes

|   |

Grid List Box 3D and Grid List Box 2D

Use the Grid List Box nodes to create scrollable lists of items arranged in a grid.

See Using the Grid List Box nodes.  |
|   |

Trajectory List Box 3D.

Use the Trajectory List Box 3D node to create scrollable lists of items arranged along a trajectory in 3D space.

See Using the Trajectory List Box 3D node.  |
### Stage nodes

|   |

Camera.

Use the Camera node to show the content of a Scene in Kanzi Studio Preview and in your Kanzi application.

See Using the Camera node.  |
|   |

Instantiator.

Use the Instantiator node to replicate the appearance of a 3D node or a tree of 3D nodes that the Instantiator node targets.

See Using the Instantiator node.  |
|   |

Light nodes.

Use the light nodes to create sources of light for a Scene in your Kanzi application.

Kanzi has these light node types:

- Directional Light emits light only in one direction and is suitable for modeling the sunlight.
- Point Light emits light from a specific location uniformly to all directions (360 degrees).
- Spot Light emits light from a specific location towards a specified direction in the shape of a cone.


See Using the light nodes.  |
|   |

Scene.

Use the Scene node to show 3D content in your Kanzi application.

See Using the Scene node.  |
## Class hierarchy organization


The base class is `Node`. The base class for 2D nodes is `Node2D` and allows adding 2D nodes as child nodes. `Node3D` works in the same way for 3D nodes. `Node` class does not have the means to connect child nodes, so that the `Node2D`, `Node3D`, and derived classes can define what types of nodes they accept as child nodes. For example, Viewport 2D derives from the `Node2D` class and therefore accepts 2D child nodes, but also accepts one child node of the type Scene. This way Kanzi can arrange 2D and 3D nodes in a heterogeneous tree.

To iterate the tree in a homogeneous way use the Visitor or Abstract Child APIs:

- For Visitor API, see `Node::visit` or `Node::visitDescendants`.
- For Abstract Child APIs, see `Node::getAbstractChildCountOverride`, `Node::findAbstractChild`, `Node::addAbstractChildOverride`, and `Node::removeAbstractChildOverride`.


Each node has the access to its parent. The type of parent pointer is `Node` because the type of the parent can be either 2D or 3D.
