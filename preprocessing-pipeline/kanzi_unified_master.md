# Kanzi Documentation Master Knowledge Base

> Consolidated hierarchical documentation generated from recursive nested web crawl.



<!-- NODE_START: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/kanzi-fundamentals.html (Depth 1) -->
<!-- SOURCE_URL: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/kanzi-fundamentals.html -->
## Kanzi fundamentals

> **Summary**: This page provides an overview of fundamental Kanzi concepts, including presentation, layouts, resource management, property system, logic programming, animation system, and Kanzi graphics. It serves as an entry point for understanding how Kanzi works and links to detailed documentation for each topic.

Copy page 
 
View this page as Markdown.
 
Here you can learn about the fundamental Kanzi concepts, which can help you understand why Kanzi works the way it works.
[![../_images/presentation.png](https://docs.kanzi.com/4.1.0/en/_images/presentation.png)](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/presentation.html)
[Presentation](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/presentation.html)
[![../_images/layouts.png](https://docs.kanzi.com/4.1.0/en/_images/layouts.png)](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/layouts.html)
[Layouts](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/layouts.html)
[![../_images/resourcefiles96x96.png](https://docs.kanzi.com/4.1.0/en/_images/resourcefiles96x96.png)](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/resource-management.html)
[Resource management](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/resource-management.html)
[![../_images/property-system.png](https://docs.kanzi.com/4.1.0/en/_images/property-system.png)](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/property-system.html)
[Property system](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/property-system.html)
[![../_images/logic-programming.png](https://docs.kanzi.com/4.1.0/en/_images/logic-programming.png)](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/logic-programming.html)
[Logic programming](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/logic-programming.html)
[![../_images/animation-system.png](https://docs.kanzi.com/4.1.0/en/_images/animation-system.png)](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/animation-system.html)
[Animation system](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/animation-system.html)
[](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/kanzi-graphics.html)
[Kanzi graphics](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/kanzi-graphics.html)
## See also
For an overview of Kanzi Studio, see [Tutorial: Getting started with Kanzi Studio](https://docs.kanzi.com/4.1.0/en/tutorials/getting-started/getting-started.html).
To learn how to use Kanzi, see [Tutorials](https://docs.kanzi.com/4.1.0/en/tutorials/tutorials.html).
To learn how to use specific features in Kanzi, see [Working with …](https://docs.kanzi.com/4.1.0/en/working-with/working-with.html).


<!-- NODE_START: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/presentation.html (Depth 2) -->
<!-- SOURCE_URL: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/presentation.html -->
### Presentation

> **Summary**: This page from the Kanzi 4.1.0 documentation introduces the fundamental concept of the node tree, which defines the content structure and layout in a Kanzi application. It categorizes the available nodes into content control nodes (e.g., Image, Model, Nine Patch Image, Page, Text Block, Viewport), interactivity control nodes (e.g., Button, Scroll View, Slider, Text Box, Toggle Button), layout control nodes (e.g., Content Layout, Dock Layout, Empty Node, Flow Layout, Grid Layout, Stack Layout, Trajectory Layout), container control nodes (e.g., Grid List Box, Trajectory List Box), and stage nodes (e.g., Camera, Instantiator, Light nodes, Scene). It also explains the class hierarchy organization, noting that Node is the base class, with Node2D and Node3D as derived classes, and describes how to iterate the tree using Visitor or Abstract Child APIs.

Copy page 
 
View this page as Markdown.
 
## Node tree
![../_images/presentation-banner.png](https://docs.kanzi.com/4.1.0/en/_images/presentation-banner.png)
Node tree defines the content structure and its layout on the screen.
The node tree is constructed from nodes that display content (for example, Image node) and implement logic (for example, Button 2D node). The same node tree supports 2D and 3D nodes and provides the means to connect them.
The relationship between the nodes in the node tree is very important and defines how several Kanzi core technologies work. Rendering order, layout, property and resource inheritance, and input and message propagation all depend on the relationship between parent and child nodes in the node tree.
Kanzi offers the tools to modularize and reuse parts of the node tree (for example, prefabs).
## Nodes available in Kanzi
### Content control nodes
![../_images/content-control-nodes.png](https://docs.kanzi.com/4.1.0/en/_images/content-control-nodes.png)  
|  ![../_images/image-node.png](https://docs.kanzi.com/4.1.0/en/_images/image-node.png)  |  Image. Use the Image node to show a bitmap image. See [Using the Image node](https://docs.kanzi.com/4.1.0/en/working-with/images/using-images.html).  |  
| --- | --- |  
|  ![../_images/model-node.png](https://docs.kanzi.com/4.1.0/en/_images/model-node.png)  |  Model. Use the Model node to show the imported meshes in your Kanzi application. See [Using imported meshes](https://docs.kanzi.com/4.1.0/en/working-with/meshes/meshes.html#using-imported-meshes).  |  
|  ![../_images/nine-patch-image.png](https://docs.kanzi.com/4.1.0/en/_images/nine-patch-image.png)  |  Nine Patch Image. Use the Nine Patch Image node to create a scalable button background that scales with the size of the Nine Patch Image content. See [Using the Nine Patch Image node](https://docs.kanzi.com/4.1.0/en/working-with/images/using-nine-patch-images.html).  |  
|  ![../_images/page-node.png](https://docs.kanzi.com/4.1.0/en/_images/page-node.png)  |  Page. Use the Page nodes to create the structure of the user interface in your application, and the Page Host nodes to manage navigation requests and transitions between Page nodes under a Page Host node. For example, you can use Page and Page Host nodes to create different parts of the user interface in your Kanzi application, such as Page Host nodes Home, Media, Navigation, or Settings screens, each having their own hierarchy of Page and Page Host nodes. See [Using the Page and Page Host nodes](https://docs.kanzi.com/4.1.0/en/working-with/pages/using-pages.html).  |  
|  ![../_images/text-block.png](https://docs.kanzi.com/4.1.0/en/_images/text-block.png)  |  Text Block 3D and Text Block 2D. Use the Text Block nodes to show a small amount of text in your application. See [Using the Text Block nodes](https://docs.kanzi.com/4.1.0/en/working-with/text/using-text-blocks.html).  |  
|  ![../_images/viewport-3d-2d.png](https://docs.kanzi.com/4.1.0/en/_images/viewport-3d-2d.png)  |  Viewport 3D and Viewport 2D. Use the Viewport nodes to set the size of a render target surface onto which Kanzi projects content. See [Viewport nodes](https://docs.kanzi.com/4.1.0/en/working-with/viewports/using-viewports.html).  |  
### Interactivity control nodes
![../_images/interactivity-control-nodes.png](https://docs.kanzi.com/4.1.0/en/_images/interactivity-control-nodes.png)  
|  ![../_images/button-3d-2d.png](https://docs.kanzi.com/4.1.0/en/_images/button-3d-2d.png)  |  Button 3D and Button 2D. Use the Button nodes to create interactions through clicking, tapping, or pressing a key on the keyboard. See [Using the Button nodes](https://docs.kanzi.com/4.1.0/en/working-with/buttons/using-buttons.html).  |  
| --- | --- |  
|  ![../_images/scroll-view-3d-2d.png](https://docs.kanzi.com/4.1.0/en/_images/scroll-view-3d-2d.png)  |  Scroll View 3D and Scroll View 2D. Use the Scroll View nodes to define an area where to generate scrolling messages in response to user input and physics-based animation. See [Using the Scroll View nodes](https://docs.kanzi.com/4.1.0/en/working-with/scroll-views/using-scroll-views.html).  |  
|  ![../_images/slider-3d-2d.png](https://docs.kanzi.com/4.1.0/en/_images/slider-3d-2d.png)  |  Slider 3D and Slider 2D. Use the Slider nodes when you want to allow users to change numerical values using a visual indicator between a minimum and a maximum value. See [Using the Slider nodes](https://docs.kanzi.com/4.1.0/en/working-with/sliders/using-sliders.html).  |  
|  ![../_images/text-box-3d-2d.png](https://docs.kanzi.com/4.1.0/en/_images/text-box-3d-2d.png)  |  Text Box 3D and Text Box 2D. Use the Text Box nodes to add single-line text input to your application. See [Using the Text Box nodes](https://docs.kanzi.com/4.1.0/en/working-with/text/using-text-boxes.html).  |  
|  ![../_images/toggle-button-3d-2d.png](https://docs.kanzi.com/4.1.0/en/_images/toggle-button-3d-2d.png)  |  Toggle Button 3D and Toggle Button 2D. Use the Toggle Button nodes to create interactions through buttons that can have multiple toggle states. See [Using the Toggle Button nodes](https://docs.kanzi.com/4.1.0/en/working-with/buttons/using-toggle-buttons.html).  |  
|  ![../_images/toggle-button-group-3d-2d.png](https://docs.kanzi.com/4.1.0/en/_images/toggle-button-group-3d-2d.png)  |  Toggle Button Group 3D and Toggle Button Group 2D. Use the Toggle Button Group nodes to allow users to select only one option from a set of options that are mutually exclusive. See [Using the Toggle Button Group nodes](https://docs.kanzi.com/4.1.0/en/working-with/buttons/using-toggle-button-groups.html).  |  
### Layout control nodes
![../_images/layout-control-nodes.png](https://docs.kanzi.com/4.1.0/en/_images/layout-control-nodes.png)  
|  ![../_images/content-layout-3d-2d.png](https://docs.kanzi.com/4.1.0/en/_images/content-layout-3d-2d.png)  |  Content Layout 3D and Content Layout 2D Use the Content Layout nodes to present content in a UI control as a single item. See [Using the Content Layout nodes](https://docs.kanzi.com/4.1.0/en/working-with/layouts/using-content-layouts.html).  |  
| --- | --- |  
|  ![../_images/dock-layout-3d-2d.png](https://docs.kanzi.com/4.1.0/en/_images/dock-layout-3d-2d.png)  |  Dock Layout 3D and Dock Layout 2D Use the Dock Layout nodes to place nodes relative to each other along the sides of a Dock Layout node. See [Using the Dock Layout nodes](https://docs.kanzi.com/4.1.0/en/working-with/layouts/using-dock-layouts.html).  |  
|  ![../_images/empty-layout-3d-2d.png](https://docs.kanzi.com/4.1.0/en/_images/empty-layout-3d-2d.png)  |  Empty Node 3D and Empty Node 2D Use the Empty Node nodes to group nodes and to set property values of their child nodes. See [Using the Empty Node nodes](https://docs.kanzi.com/4.1.0/en/working-with/empty-nodes/using-empty-nodes.html).  |  
|  ![../_images/flow-layout-3d-2d.png](https://docs.kanzi.com/4.1.0/en/_images/flow-layout-3d-2d.png)  |  Flow Layout 3D and Flow Layout 2D Use the Flow Layout nodes to arrange nodes along a line. When a line runs out of space, the Flow Layout node places its child nodes in a new line. See [Using the Flow Layout nodes](https://docs.kanzi.com/4.1.0/en/working-with/layouts/using-flow-layouts.html).  |  
|  ![../_images/grid-layout-3d-2d.png](https://docs.kanzi.com/4.1.0/en/_images/grid-layout-3d-2d.png)  |  Grid Layout 3D and Grid Layout 2D Use the Grid Layout nodes to arrange nodes in a grid. See [Using the Grid Layout nodes](https://docs.kanzi.com/4.1.0/en/working-with/grids/using-grid-layouts.html).  |  
|  ![../_images/stack-layout-3d-2d.png](https://docs.kanzi.com/4.1.0/en/_images/stack-layout-3d-2d.png)  |  Stack Layout 3D and Stack Layout 2D Use the Stack Layout nodes to arrange nodes next to each other on the selected axis. See [Using the Stack Layout nodes](https://docs.kanzi.com/4.1.0/en/working-with/layouts/using-stack-layouts.html).  |  
|  ![../_images/trajectory-layout-3d-2d.png](https://docs.kanzi.com/4.1.0/en/_images/trajectory-layout-3d-2d.png)  |  Trajectory Layout 3D and Trajectory Layout 2D Use the Trajectory Layout nodes to arrange items along a trajectory path. See [Using the Trajectory Layout nodes](https://docs.kanzi.com/4.1.0/en/working-with/trajectories/using-trajectory-layouts.html).  |  
### Container control nodes
![../_images/container-control-nodes.png](https://docs.kanzi.com/4.1.0/en/_images/container-control-nodes.png)  
|  ![../_images/grid-list-box-3d-2d.png](https://docs.kanzi.com/4.1.0/en/_images/grid-list-box-3d-2d.png)  |  Grid List Box 3D and Grid List Box 2D Use the Grid List Box nodes to create scrollable lists of items arranged in a grid. See [Using the Grid List Box nodes](https://docs.kanzi.com/4.1.0/en/working-with/grids/using-grid-list-boxes.html).  |  
| --- | --- |  
|  ![../_images/trajectory-list-box-3d1.png](https://docs.kanzi.com/4.1.0/en/_images/trajectory-list-box-3d1.png)  |  Trajectory List Box 3D. Use the Trajectory List Box 3D node to create scrollable lists of items arranged along a trajectory in 3D space. See [Using the Trajectory List Box 3D node](https://docs.kanzi.com/4.1.0/en/working-with/trajectories/using-trajectory-list-boxes.html).  |  
### Stage nodes
![../_images/3d-nodes.png](https://docs.kanzi.com/4.1.0/en/_images/3d-nodes.png)  
|  ![../_images/camera.png](https://docs.kanzi.com/4.1.0/en/_images/camera.png)  |  Camera. Use the Camera node to show the content of a Scene in Kanzi Studio Preview and in your Kanzi application. See [Using the Camera node](https://docs.kanzi.com/4.1.0/en/working-with/cameras/creating-and-using-cameras-for-previews.html).  |  
| --- | --- |  
|  ![../_images/instantiator.png](https://docs.kanzi.com/4.1.0/en/_images/instantiator.png)  |  Instantiator. Use the Instantiator node to replicate the appearance of a 3D node or a tree of 3D nodes that the Instantiator node targets. See [Using the Instantiator node](https://docs.kanzi.com/4.1.0/en/working-with/instantiator-nodes/instantiator-nodes.html).  |  
|  ![../_images/light-nodes.png](https://docs.kanzi.com/4.1.0/en/_images/light-nodes.png)  |  Light nodes. Use the light nodes to create sources of light for a Scene in your Kanzi application. Kanzi has these light node types:
  * Directional Light emits light only in one direction and is suitable for modeling the sunlight.
  * Point Light emits light from a specific location uniformly to all directions (360 degrees).
  * Spot Light emits light from a specific location towards a specified direction in the shape of a cone.

See [Using the light nodes](https://docs.kanzi.com/4.1.0/en/working-with/lights/using-lights.html).  |  
|  ![../_images/scene.png](https://docs.kanzi.com/4.1.0/en/_images/scene.png)  |  Scene. Use the Scene node to show 3D content in your Kanzi application. See [Using the Scene node](https://docs.kanzi.com/4.1.0/en/working-with/scenes/scenes.html).  |  
## Class hierarchy organization
The base class is `Node[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html)`. The base class for 2D nodes is `Node2D[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13794.html)` and allows adding 2D nodes as child nodes. `Node3D[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13806.html)` works in the same way for 3D nodes. `Node[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html)` class does not have the means to connect child nodes, so that the `Node2D[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13794.html)`, `Node3D[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13806.html)`, and derived classes can define what types of nodes they accept as child nodes. For example, Viewport 2D derives from the `Node2D[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13794.html)` class and therefore accepts 2D child nodes, but also accepts one child node of the type Scene. This way Kanzi can arrange 2D and 3D nodes in a heterogeneous tree.
To iterate the tree in a homogeneous way use the Visitor or Abstract Child APIs:
  * For Visitor API, see `Node::visit[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html#ac66822f17f1d32d389a96111c1874a31)` or `Node::visitDescendants[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html#a760a8c66407b67a02110cdc3058f3083)`.
  * For Abstract Child APIs, see `Node::getAbstractChildCountOverride[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html#a03194546370415d478dbf669953883b6)`, `Node::findAbstractChild[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html#a26a7f6ab02e047eb0a7f9b46d20e339c)`, `Node::addAbstractChildOverride[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html#a47fd6950e4128f0931532e58d8a67d68)`, and `Node::removeAbstractChildOverride[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html#a1a5cb72b8b18d10a8fdd680e111eb55d)`.

Each node has the access to its parent. The type of parent pointer is `Node[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html)` because the type of the parent can be either 2D or 3D.

<!-- NODE_END: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/presentation.html -->


<!-- NODE_START: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/layouts.html (Depth 2) -->
<!-- SOURCE_URL: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/layouts.html -->
### Layouts

Copy page 
 
View this page as Markdown.
 
In Kanzi there are three types of layouts:  
|  ![../_images/layout-types-content.png](https://docs.kanzi.com/4.1.0/en/_images/layout-types-content.png)  | Layouts that base the position and size of their child nodes, such as the Flow Layout, Grid Layout, Stack Layout, and Trajectory Layout nodes. For example, these layouts are useful when the amount of content changes dynamically.  |  
| --- | --- |  
|  ![../_images/layout-types-control.png](https://docs.kanzi.com/4.1.0/en/_images/layout-types-control.png)  | Content controls that show specific content and usually center the content, such as the Image node and Button nodes.  |  
|  ![../_images/layout-types-positioning.png](https://docs.kanzi.com/4.1.0/en/_images/layout-types-positioning.png)  | Absolute positioning controls that act as containers that group their child nodes, such as the Viewport 2D and Empty Node 2D nodes.  |  
You can use layout nodes to position nodes in relation to the application screen and other nodes. Layout consists of properties alignment, margins and layout size and that you can define either specific to a node or as a general rule imposed on child nodes by specific layout containers.
See [Layout control nodes](https://docs.kanzi.com/4.1.0/en/working-with/layouts/layouts.html).
## Universal layout properties
To position items in your Kanzi applications you can use these transformation types:
  * Layout transformation transforms the item before it applies the layout pass.
  * Render transformation transforms the item after it applies the layout pass, but before it renders the item.

Kanzi applies the render transformation after applying the layout transformation, and does not affect the layout calculations. For example, this allows you to animate nodes within a layout without causing the layout recalculation.
Layout control nodes, such as Stack Layout and Grid Layout nodes, apply their own transformations on all immediate child nodes who in their part define their own layout considering their own child nodes, layout transformations, margins and alignments.
  * Alignment defines the gravity of the layout. For example, set the Horizontal Alignment property to Right to align the node to the right side of its parent layout. By setting alignment properties to Stretch, the node stretches to the dimensions of its parent layout. Use the Content Stretch property to specify how a layout handles its content.
![../_images/layout-horizontal-alignment.gif](https://docs.kanzi.com/4.1.0/en/_images/layout-horizontal-alignment.gif)
  * Margin enforces the object spacing relative to the border of its parent layout. For example, set the Horizontal Margin property to set the spacing on the left and right sides of the node in relation to its parent layout.
![../_images/layout-margin.gif](https://docs.kanzi.com/4.1.0/en/_images/layout-margin.gif)
  * Layout properties override the bounding box size of a node. The default layout size is defined by the size of the node based on its bounding box and margins.
![../_images/layout-override.gif](https://docs.kanzi.com/4.1.0/en/_images/layout-override.gif)

For example, a Stack Layout node set in direction on the x axis places its two child nodes next to each other based on their dimensions (bounding boxes). By using the Layout Width property you can override the width of the bounding box: a value smaller than the size of the node makes the node overlap, and a value larger than the size of the node extends the space between the two nodes.
![../_images/stack-layout-overlap.gif](https://docs.kanzi.com/4.1.0/en/_images/stack-layout-overlap.gif)
After all the layout tasks are done, Kanzi applies the final transformations from the parent nodes. The RootNode under the Screen node has special rules for its layout if it is a Viewport 2D or an Empty Node 2D. It inherits the defined screen size, unless defined by the layout properties.
## See also
[Property system](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/property-system.html)
[Resource management](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/resource-management.html)

<!-- NODE_END: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/layouts.html -->


<!-- NODE_START: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/resource-management.html (Depth 2) -->
<!-- SOURCE_URL: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/resource-management.html -->
### Resource management

> **Summary**: This page from the Kanzi documentation provides an overview of resource management in Kanzi applications. It explains what resources are, how to set them on nodes using URLs or resource keys, and the benefits of using resource keys for theming, localization, and content modularization. It lists various Kanzi resource types (e.g., aliases, animation clips, brushes, fonts, materials, meshes, textures, render pass prefabs, object sources, resource dictionaries, state managers, styles, text resources, trajectories) with links to detailed documentation. It covers importing resource assets, resource URLs, resource dictionaries and their hierarchical key resolution, default resources, the resource manager for controlling resource lifetime and GPU memory types, and behavior during pause/resume on different platforms.

Copy page 
 
View this page as Markdown.
 
In Kanzi, a resource is an item that you can reuse in different parts of your application. For example, a Mesh Data resource defines the geometry of a Model node, and you can use the same Color Brush in different nodes to set the Foreground Brush or Background Brush properties.
![../_images/color-brush-resource.gif](https://docs.kanzi.com/4.1.0/en/_images/color-brush-resource.gif)
Kanzi resource manager enables you to organize and reuse resources in your applications.
## Setting resources to nodes
In Kanzi you can set the resources to nodes either directly using the resource URL, or indirectly using the resource key. When you set resources in Kanzi Studio, it by default assigns all resources using the URL. If you want to use the indirect setting in Kanzi Studio you need to create a key for the resource in a resource dictionary, and in the property select that key. Because key lookup is hierarchical you can define what the key resolves to by creating resource dictionary entries in the tree.
Setting resources using resource keys enables you to:  
|  ![../_images/resource-management-skin.png](https://docs.kanzi.com/4.1.0/en/_images/resource-management-skin.png)  |   |  ![../_images/resource-management-language.png](https://docs.kanzi.com/4.1.0/en/_images/resource-management-language.png)  |   |  ![../_images/resource-management-content.png](https://docs.kanzi.com/4.1.0/en/_images/resource-management-content.png)  |  
| --- | --- | --- | --- | --- |  
| Create and apply different skins or themes to change the appearance of your application.  |   | Create different versions of your application for different languages and locales.  |   | Override resources to modularize content.  |  
You can share the resources to decrease the memory and runtime requirements of your application. This enables you to reuse the same resource, or to change the resource so that the change is reflected in the entire application. For example, that way you can share a brush that is animated.
Kanzi offers many tools to manage the resources while the application is running. In Kanzi you can:
  * Load resources in multiple threads to use multiple cores in your device and speed up the start up or loading time of your application. See [Loading resources in parallel](https://docs.kanzi.com/4.1.0/en/best-practices/loading-resources-in-parallel.html).
  * Asynchronously load resources to improve application startup or responsiveness. See [Loading node prefab resources asynchronously](https://docs.kanzi.com/4.1.0/en/working-with/prefabs/prefabs.html#loading-node-prefab-resources-asynchronously).
  * Select image from the device storage. See [Loading images from the file system](https://docs.kanzi.com/4.1.0/en/working-with/textures/loading-texture-images-from-the-file-system.html).
  * Localize your application. See [Localizing applications](https://docs.kanzi.com/4.1.0/en/working-with/localization/localizing-applications.html) and [Tutorial: Localize your application](https://docs.kanzi.com/4.1.0/en/tutorials/localization/localization.html).
  * Create and apply a theme to change the appearance of your application. See [Theming your applications](https://docs.kanzi.com/4.1.0/en/working-with/themes/theming-applications.html).
  * Find out whether a resource is in use and unload unused resources. This allows you to create complex applications where not all resources can fit into memory at once. See [Setting how Kanzi Engine handles unused resources](https://docs.kanzi.com/4.1.0/en/working-with/resources/unused-resources.html).

## Kanzi resource types  
|   
 |  ![../_images/alias-icon.png](https://docs.kanzi.com/4.1.0/en/_images/alias-icon.png)  |  Alias Use an Alias to get consistent access to a Kanzi node. You can use aliases to access nodes both in Kanzi Studio and using the Kanzi Engine API.  | [Using aliases](https://docs.kanzi.com/4.1.0/en/working-with/aliases/using-aliases.html)  |  
| --- | --- | --- |  
 |  
|   
 |  ![../_images/animation-clip-icon.png](https://docs.kanzi.com/4.1.0/en/_images/animation-clip-icon.png)  |  Animation Clip Use an Animation Clip to combine Animation Data resources into more complex animations. You can reuse the same Animation Data resources in different Animation Clip items. Use an Animation Child Clip to create hierarchical animations.  |  [Animations](https://docs.kanzi.com/4.1.0/en/working-with/animations/animations.html) [Editing animation clips](https://docs.kanzi.com/4.1.0/en/working-with/animations/editing-animation-clips.html) [Editing timeline sequences](https://docs.kanzi.com/4.1.0/en/working-with/animations/editing-timeline-sequences.html)  |  
| --- | --- | --- |  
|  ![../_images/animation-data-icon.png](https://docs.kanzi.com/4.1.0/en/_images/animation-data-icon.png)  |  Animation Data Use an Animation Data resource to define the keyframes and target property of a keyframe animation. One Animation Data resource can target only one property or property field. Animation Data resources are independent from the nodes they target. This allows you to reuse Animation Data resources to animate different nodes.  |   |  
|  ![../_images/timeline-sequence-icon.png](https://docs.kanzi.com/4.1.0/en/_images/timeline-sequence-icon.png)  |  Timeline Sequence Use a Timeline Sequence to combine a set of Timeline Entry resources.  |   |  
 |  
|   
 |  ![../_images/brush-icon.png](https://docs.kanzi.com/4.1.0/en/_images/brush-icon.png)  |  Brushes Use brushes to set the background of 2D nodes. In Kanzi, all 2D nodes by default have transparent background.  | [Using brushes](https://docs.kanzi.com/4.1.0/en/working-with/brushes/using-brushes.html)  |  
| --- | --- | --- |  
 |  
|   
 |  ![../_images/fonts-icon.png](https://docs.kanzi.com/4.1.0/en/_images/fonts-icon.png)  |  Fonts Use a font to render text. The default font in Kanzi is Fira Sans Regular. To use your own font, import it to your Kanzi Studio project.  | [Importing fonts](https://docs.kanzi.com/4.1.0/en/working-with/importing/importing-fonts.html)  |  
| --- | --- | --- |  
 |  
|   
 |  ![../_images/material-icon.png](https://docs.kanzi.com/4.1.0/en/_images/material-icon.png)  |  Materials Use materials to set the appearance of 3D nodes and Material Brush brushes.  | [Material types and materials](https://docs.kanzi.com/4.1.0/en/working-with/materials/materials.html)  |  
| --- | --- | --- |  
|  ![../_images/mesh-icon.png](https://docs.kanzi.com/4.1.0/en/_images/mesh-icon.png)  |  Mesh Data A mesh is a collection of vertices, edges, and faces that define the shape of a solid object in 3D with flat faces and straight edges and the triangles that form the surface between the points.  | [Using meshes](https://docs.kanzi.com/4.1.0/en/working-with/meshes/meshes.html)  |  
|  ![../_images/textures-icon.png](https://docs.kanzi.com/4.1.0/en/_images/textures-icon.png)  |  Textures Use textures to show content in Image nodes, to set the look of textured materials, and to show content in Texture Brush brushes. You can create textures from common image file formats.  | [Textures](https://docs.kanzi.com/4.1.0/en/working-with/textures/textures.html)  |  
 |  
|   
 |  ![../_images/render-pass-prefabs-icon.png](https://docs.kanzi.com/4.1.0/en/_images/render-pass-prefabs-icon.png)  |  Render Pass Prefabs Use render passes to define the rendering of 3D content in your Kanzi application. In a render pass prefab, you can create a hierarchy of render passes to achieve a specific rendering result.  | [Rendering](https://docs.kanzi.com/4.1.0/en/working-with/rendering/rendering.html)  |  
| --- | --- | --- |  
|  ![../_images/object-source-icon.png](https://docs.kanzi.com/4.1.0/en/_images/object-source-icon.png)  |  Object Source Use object sources and filters to tell a Draw Objects render pass which nodes in your Kanzi application you want to render. Root Object Source contains all nodes in the node tree of the currently active Scene node.  | [Using object sources](https://docs.kanzi.com/4.1.0/en/working-with/object-sources/using-object-sources.html)  |  
 |  
|   
 |  ![../_images/resource-dictionary-icon.png](https://docs.kanzi.com/4.1.0/en/_images/resource-dictionary-icon.png)  |  Resource Dictionary A resource dictionary is a collection of resource IDs pointing to resources. You can add a resource dictionary to any node.  | [Using resource dictionaries](https://docs.kanzi.com/4.1.0/en/working-with/resources/using-resource-dictionaries.html)  |  
| --- | --- | --- |  
 |  
|   
 |  ![../_images/state-managers-icon.png](https://docs.kanzi.com/4.1.0/en/_images/state-managers-icon.png)  |  State Managers Use a State Manager to create different states in your Kanzi application.  | [State manager](https://docs.kanzi.com/4.1.0/en/working-with/state-managers/state-managers.html)  |  
| --- | --- | --- |  
 |  
|   
 |  ![../_images/styles-icon.png](https://docs.kanzi.com/4.1.0/en/_images/styles-icon.png)  |  Styles Use styles to set the property values of one or more nodes of a certain type.  | [Using styles](https://docs.kanzi.com/4.1.0/en/working-with/styles/using-styles.html)  |  
| --- | --- | --- |  
 |  
|   
 |  ![../_images/text-resource-icon.png](https://docs.kanzi.com/4.1.0/en/_images/text-resource-icon.png)  |  Text Resources A text resource is a text string used by Text Block and Text Box nodes.  | [Text](https://docs.kanzi.com/4.1.0/en/working-with/text/text.html)  |  
| --- | --- | --- |  
 |  
|   
 |  ![../_images/trajectory-icon.png](https://docs.kanzi.com/4.1.0/en/_images/trajectory-icon.png)  |  Trajectories Use trajectories as paths along which Trajectory Layout 3D and Trajectory Layout 2D nodes arrange their child nodes, and along which Trajectory List Box 3D nodes move their items.  | [Trajectories](https://docs.kanzi.com/4.1.0/en/working-with/trajectories/trajectories.html)  |  
| --- | --- | --- |  
 |  
## Importing resource assets to your project
You can create some resources directly in Kanzi Studio (for example, brushes and animations). For some resources you have to import assets created in third-party tools (for example, textures and meshes). See [Importing](https://docs.kanzi.com/4.1.0/en/working-with/importing/importing.html).
## Resource URLs
The most basic way to refer to a resource is a URL. URLs can refer to resources inside a kzb file or files on device storage. When you set a resource in a property you need to provide the URL of the resource. When you do that in Kanzi Studio in the Properties window, Kanzi does that automatically for the resource you select. When you set resource properties using the API, you need to provide the resource URL manually. To find the URL of a resource in your project, in Kanzi Studio right-click the resource and select Copy .kzb URL. To reference files on the device storage use the `file:///` URL format.
When using the API you can specify a resource object directly. Nodes that accept resource objects usually provide a method overload that accepts such objects. For example, to set the image in an Image node use `Image2D::setImage[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13754.html#a91e54520299b946f567f9d2293cd84e0)`.
## Resource dictionary
A resource dictionary is a collection of a key-value pair entries for each resource. You can define a resource dictionary in any node. Keys provide means to specify resources indirectly: instead of specifying a resource or a URL to a node, you can specify a key. Kanzi resolves the resource dynamically by looking up the nearest resource dictionary where the key defines to which resource it resolves to. When a key needs to be resolved to an item, the resolving process starts checking the resource dictionaries from the node that uses the key: if a dictionary of that node contains the key, the node uses that key, if not, the node checks its parents’ dictionaries until it finds the key. This process continues recursively until the root of the node tree. If the node does not find the key, it is up to the node to decide what happens then. For example, it is a valid case if an Image node does not show an image. Kanzi controls fail softly when resources are not found, but in plugins it is up to the author of the plugin to define what happens.
## Default resources
Kanzi comes with default resources that enable you to create applications faster. For example, when you create a Scene, Kanzi provides a default render pass, when you create a Text Block or a Text Box node, Kanzi provides a default font. If you need to customize the default Kanzi resources, create or import the resources that fit your needs and use them instead of the Kanzi default resources.
When you create a kzb file from your Kanzi Studio project the default Kanzi resources are included in the kzb file by default.
## Resource manager
The resource manager manages the lifetime, loading, and unloading of resources. You can access the resource manager using the Kanzi API and you can use it to specify the lifetime policies for resources and to remove unused resources. To specify whether resources are always kept in memory, or unloaded when they are not needed, you specify a policy. You can specify a policy globally for the resource manager, or for each resource. If the policy is to keep the resources in memory, you can request manual removal based on the logic of your application. For example, you can manually remove resources when you change a Page node in your application to load a large amount of resources for a new Page node.
The resource manager allows you to define in which memory the GPU resources in your Kanzi application are stored. For example, to set this for a texture in Kanzi Studio in the Library > Materials and Textures > Textures select a texture and in the Properties set the GPU Memory Type property:
  * GPU Only. The resource is deployed to GPU memory and released from the RAM immediately after deployment. Kanzi keeps the resource in the GPU memory unless you release it in the application code.
  * GPU and RAM. The resource is deployed to the GPU memory. Kanzi keeps the resource in both GPU and RAM memory and manages the resource based on the platform and the application. Kanzi automatically manages the unloading of resources. Compared to GPU Only, this consumes more RAM, but provides faster resume times, for example, on Android.
  * RAM Only. The resource is deployed to the GPU only when instructed in the application code. Kanzi keeps the resource in the GPU memory and unloads it when you release it in the application code.

## Pause and resume
When your Kanzi application is in the paused state (`MainLoopState::Paused[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a11119.html#ae35554056f5fa4e74b1d5d5921bf8ea4ae99180abf47a8b3a856e0bcb2656990a)`):
  * On Android, by default, the GPU resources that are not stored in a kzb file become invalid. If your application uses custom resources that it does not load from kzb files, make sure that you reload and redeploy those resources manually when needed. Kanzi automatically restores all other resources.
  * On other platforms, Kanzi does not by default invalidate the GPU resources.

You can set in the application configuration how to handle GPU resources when your application is in the paused state. In the [Application configuration reference](https://docs.kanzi.com/4.1.0/en/working-with/application-configurations/reference-for-application-configuration.html), see [HandleGPUResources](https://docs.kanzi.com/4.1.0/en/working-with/application-configurations/reference-for-application-configuration.html#handlegpuresources).
## See also
[Resources](https://docs.kanzi.com/4.1.0/en/working-with/resources/resources.html)
[Using resource dictionaries](https://docs.kanzi.com/4.1.0/en/working-with/resources/using-resource-dictionaries.html)
[Setting how Kanzi Engine handles unused resources](https://docs.kanzi.com/4.1.0/en/working-with/resources/unused-resources.html)
[Application development](https://docs.kanzi.com/4.1.0/en/working-with/application-configurations/application-configuration.html)
[Application configuration reference](https://docs.kanzi.com/4.1.0/en/working-with/application-configurations/reference-for-application-configuration.html)

<!-- NODE_END: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/resource-management.html -->


<!-- NODE_START: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/property-system.html (Depth 2) -->
<!-- SOURCE_URL: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/property-system.html -->
### Property system

> **Summary**: This page explains the Kanzi property system, which provides a uniform way to access and manipulate node data. It covers property data types, property usage (including attached properties), default values, inheritable properties, property precedence (modified value, local value, named style, typed style, inherited value, default value), and property type change flags (measure, render, draw). It also mentions how to set properties via Kanzi Studio and the Kanzi Engine API.

Copy page 
 
View this page as Markdown.
 
Properties provide the means to specify and examine the state, appearance, and behavior of nodes. For example, a property can define a color, indicate whether a button is pressed, or specify the alignment of an item.
You can work with properties by setting the property values in Kanzi Studio and accessing them in code without understanding how the property system works. However, to take full advantage of the Kanzi property system features, you have to become familiar with how the property system works.
Properties provide a uniform way to access data of Kanzi nodes, so that many Kanzi subsystems can manipulate the data. That way you can, for example, animate property values, provide bindings between property values, and monitor property value changes.
Any property value can be affected by multiple input sources. The property system defines the rules for resolving the property value from all inputs and resolves the current value. For example, you can set the value of a property directly, properties can have default values, styles can affect property values, and animations and state manager can modify property values. By offering rules that are applied automatically, the property system minimizes the number of places where you have to change the values manually.
## Property data type
Each property is described by a property type. The property type uniquely describes where the property is used and the name of the property. The data type defines the type of values that the property can hold.
For example, the `Node::VisibleProperty[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html#ac65905021c8a765bb722d6e9f9f7d190)` property type, which controls the visibility of nodes, is used in the `Node[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html)` class and derived classes. You can use its name (`Node::VisibleProperty[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html#ac65905021c8a765bb722d6e9f9f7d190)`) to find the property type during runtime. Because the data type of the property is boolean, it accepts the values `true` or `false`.
In Kanzi Studio, you can have more specialized property types, but their representation comes only from the available data types. See [Creating a property type](https://docs.kanzi.com/4.1.0/en/working-with/property-types/creating-custom-property-types.html#creating-a-property-type).
For example, enumeration values are represented as integer values even though they limit the range of values to the entries defined in the enumeration.
## Property usage
Most Kanzi properties are defined in the classes that use them. You can use such properties to set the appearance, state, or behavior of the object where you set the property.
For example:
  * In a Text Block node, the Text property defines the text that the node displays.
  * The Visible property controls the visibility of a node and all its descendant nodes.

However, some Kanzi properties configure the appearance, behavior, or state of other objects.
For example:
  * Materials can define the Diffuse Color property that you can assign to nodes using that material.
  * Grid Layout defines the Row and Column properties, but you set them in the child nodes of the Grid Layout node, not in the Grid Layout node.

In Kanzi, these properties are called attached properties.
## Default property value
Each property type defines the default value of that property. When queried, Kanzi returns the default value unless you set the property value directly or indirectly through styles, inheritance, and so on. Using the default value can save time during application development.
For example, the default value of the Visible (`Node::VisibleProperty[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html#ac65905021c8a765bb722d6e9f9f7d190)`) property is `true`. By default, all nodes are visible.
Alternatively, not having a property value is a condition for some property types.
For example, the Layout Width (`Node::WidthProperty[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html#ac1c0a16661818cae4e3aca1a92b854fd)`) and Layout Height (`Node::HeightProperty[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html#a691e8ac252be2a2ac098539a3c01be2e)`) properties let you set the size of a node:
  * By setting these properties to 100 pixels, you force the size of the node to be 100 by 100 pixels.
  * By not setting these properties, you let the node decide its own size.
For example, the Image node can decide its size based on the image that it shows, or a Stack Layout node can determine to be the size of all of its items.

## Inheritable property types
Each property type defines whether the value of that property is inheritable. A node inherits the values of inheritable property types from its ancestor nodes.
For example, `Node::FontFamilyProperty[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html#ae16e1ae057c2999ae85112e3cde944c9)` is an inheritable property type. When you want to use the same font family for all controls that can display text, set the Font Family property only at the top-most level of your node tree. Kanzi applies the same font to all descendant nodes. If you want to use a different font in one of the descendant nodes, add the Font Family property to that node and set it to the font family that you want to use.
## Property precedence
Querying a property value produces one result, but while determining the value, the property system evaluates multiple sources that can affect the property value. The property value sources are evaluated in a specific order.

Kanzi Engine resolves the runtime values based on these precedence rules (the highest first):
  * **Modified value**
Animations and bindings modify and states override the value. See [Animations](https://docs.kanzi.com/4.1.0/en/working-with/animations/animations.html), [Modifier bindings](https://docs.kanzi.com/4.1.0/en/working-with/bindings/bindings.html#modifier-bindings), and [State manager](https://docs.kanzi.com/4.1.0/en/working-with/state-managers/state-managers.html).
Tip
In the Kanzi Studio Node Tree window, an indicator next to a node shows when a State Manager, Binding, Data Source Binding, or an Animation overrides the values of some properties in that node.
![../_images/node-override-notice.png](https://docs.kanzi.com/4.1.0/en/_images/node-override-notice.png)
To navigate to the source of the override in the Kanzi Studio project, right-click the override indicator and select the source you wish to navigate to from the context menu.
  * **Local value**
Local values are property values that you set directly. In Kanzi Studio, all properties in nodes are defined by a local value. You can set the local value using actions, value source bindings, and Kanzi Engine API.
Using the Kanzi Engine API, you can set local property values with:
    * The `PropertyObject::setProperty[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15378.html#a0b1b15386766715ffb41bdd55d5143a0)` function.
For example, to set the value of the Visible property to false, use

```
node.setProperty(Node::VisibleProperty, false)

```
Copy to clipboard
    * Helper functions offered by most of the classes.
For example, you can set the `Node::VisibleProperty[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html#ac65905021c8a765bb722d6e9f9f7d190)` property with the `Node::setVisible[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html#ac39911cd1a064542917a8b41601c8426)` function.
For helper functions, see the reference of the class that defines the property.
See [Value source bindings](https://docs.kanzi.com/4.1.0/en/working-with/bindings/bindings.html#value-source-bindings) and [Triggers](https://docs.kanzi.com/4.1.0/en/working-with/triggers/triggers.html).
  * **Named style**
Kanzi applies a named style to all nodes whose Style property value points to that style.
See [Applying a style to selected instances of a node type](https://docs.kanzi.com/4.1.0/en/working-with/styles/using-styles.html#applying-a-style-to-selected-instances-of-a-node-type).
  * **Typed style**
Kanzi applies a typed style to all nodes of the type that you specify in the style.
See [Applying a style that applies to a node type in the selected scope](https://docs.kanzi.com/4.1.0/en/working-with/styles/using-styles.html#applying-a-style-that-applies-to-a-node-type-in-the-selected-scope).
  * **Inherited value** (if the property is inheritable)
Each property type specifies whether the property is inheritable. Only certain values can be inherited from ancestors.
See [Inheritable property types](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/property-system.html#inheritable-property-types).
  * **Default value and class default value**
All properties have a default value defined in their metadata. Kanzi uses the default value if nothing else affects the value. Each class that inherits the property type can override its default value.
For example:
    * The default value of the Horizontal Alignment (`Node::HorizontalAlignmentProperty[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html#a9442df55b1b71c62eb0e0531cc46c3db)`) property is Center (`Node::HorizontalAlignment::HorizontalAlignmentCenter[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html#ab9b8913468471fe36d4998cac8025c70aded22452001810f594d4285f5e1e0bbc)`).
    * The `Node2D[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13794.html)` class overrides the default value of the Horizontal Alignment property to Left (`Node::HorizontalAlignment::HorizontalAlignmentLeft[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html#ab9b8913468471fe36d4998cac8025c70aff0792a0799686c438faa906ee4467ab)`).
See [Default property value](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/property-system.html#default-property-value).

## Property type change flags
In Kanzi, each property type can have one or more change flags that indicate the effects of changing the value of that property.
For example:
  * The `PropertyTypeChangeFlag::PropertyTypeChangeFlagMeasure[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a11084.html#ggae575b44cdca9c6f73824d09d5671fab2a926af8aa7be56f415119a39e3c9e32c2)` flag is used by property types that affect the size of a node as reported by that node itself, or the size and position of that node with respect to other nodes.
For example, the Layout Width (`Node::WidthProperty[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13774.html#ac1c0a16661818cae4e3aca1a92b854fd)`) property has this change flag. When the value of the Layout Width property changes in a node, Kanzi:
    1. Remeasures the node.
    2. If the measured size of the node changed, measures the parent of the node, the parent of the parent, and so on.
    3. Rearranges the layout of the node, its changed ancestor nodes, and their descendants.
    4. For those nodes whose transform changed, recalculates the transformations.
    5. Draws all nodes.
  * The `PropertyTypeChangeFlag::PropertyTypeChangeFlagRender[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a11084.html#ggae575b44cdca9c6f73824d09d5671fab2a0e93f85804c27ea970393a6c658764b9)` flag is used by property types that change the rendering parameters of a 2D node but do not affect the layout.
For example, the Render Transformation (`Node2D::RenderTransformationProperty[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a13794.html#aa14e140d4749ce47692c18af5ad68501)`) property has this change flag. When the value of the Render Transformation property changes in a node, Kanzi:
    1. Recalculates the transformations of the node and its descendants.
    2. Draws all nodes.
  * The `PropertyTypeChangeFlag::PropertyTypeChangeFlagDraw[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a11084.html#ggae575b44cdca9c6f73824d09d5671fab2a730acafaf5f6466a6117c430bc48eb5d)` flag is used by property types that affect the drawing of a node.
For example, most material properties use this flag. When the value of such a property changes in a node, Kanzi draws all nodes.

In the Kanzi Engine API reference, see `PropertyTypeChangeFlag[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a11084.html#gae575b44cdca9c6f73824d09d5671fab2)`.
## See also
[Creating property types](https://docs.kanzi.com/4.1.0/en/working-with/property-types/creating-custom-property-types.html)
[Using styles](https://docs.kanzi.com/4.1.0/en/working-with/styles/using-styles.html)
[State manager](https://docs.kanzi.com/4.1.0/en/working-with/state-managers/state-managers.html)
[Triggers](https://docs.kanzi.com/4.1.0/en/working-with/triggers/triggers.html)
[Animations](https://docs.kanzi.com/4.1.0/en/working-with/animations/animations.html)
[Using properties in Java](https://docs.kanzi.com/4.1.0/en/working-with/java/using-java.html#using-properties)
[Using properties in Lua](https://docs.kanzi.com/4.1.0/en/working-with/lua/using-lua.html#using-properties)

<!-- NODE_END: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/property-system.html -->


<!-- NODE_START: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/logic-programming.html (Depth 2) -->
<!-- SOURCE_URL: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/logic-programming.html -->
### Logic programming

> **Summary**: This page from Kanzi documentation introduces the various technologies available for programming application and control logic in Kanzi. It categorizes them into four main approaches: Triggers and Actions for reactive logic via the Kanzi Studio UI, State Managers for defining state machines tied to control or application states, the Kanzi Engine Lua API for platform-independent scripting embedded in kzb files, and C++/Java APIs for extensive programmatic control and plugin development. The page also provides links to related tutorials and detailed references.

Copy page 
 
View this page as Markdown.
 
In Kanzi you can program application and control logic using several technologies that are geared towards different users and use cases:  
|  ![../_images/trigger.png](https://docs.kanzi.com/4.1.0/en/_images/trigger.png)  |  Triggers and actions provide reactive logic programming through Kanzi Studio UI. You can use triggers and actions to execute small pieces of logic called actions based on simple conditions defined in triggers. For example, if you want to handle simple events like button press, or perform simple operations like set a property or activate a page, you can use triggers and actions. Triggers define the events and conditions you want to handle and contain actions that you want to execute when the trigger is set off. Actions are small operations that are executed when the trigger event happens and conditions are met. See [Triggers](https://docs.kanzi.com/4.1.0/en/working-with/triggers/triggers.html).  |  
| --- | --- |  
|  ![../_images/state-manager.png](https://docs.kanzi.com/4.1.0/en/_images/state-manager.png)  | State managers expose logic programming through defining state machines tied to internal states of controls or application. For example, use the state manager to define the look of a button when it is pressed and when it is not, or to define the logic of your application, control, or prefab in terms of mutually exclusive states. You can use a state manager to define the logic of a menu. For example, to show whether the sound in a car is muted, or when fuel is low. See [State manager](https://docs.kanzi.com/4.1.0/en/working-with/state-managers/state-managers.html).  |  
|  ![../_images/lua.png](https://docs.kanzi.com/4.1.0/en/_images/lua.png)  |  Kanzi Engine Lua API is a platform-independent interface to the Kanzi Engine using the Lua programming language. It allows you to create application and user interface logic in Kanzi Studio. When you export a kzb file, Kanzi Studio embeds Lua scripts in the kzb file. See [Using Lua](https://docs.kanzi.com/4.1.0/en/working-with/lua/using-lua.html), [Tutorial: Kanzi Engine Lua API basic use](https://docs.kanzi.com/4.1.0/en/tutorials/fifteen-puzzle/fifteen-puzzle.html), and [Kanzi Lua API reference](https://docs.kanzi.com/4.1.0/en/reference/kanzi-lua-api/index.html).  |  
|  ![../_images/c-plus-java.png](https://docs.kanzi.com/4.1.0/en/_images/c-plus-java.png)  | C++ and Java APIs provide the most extensive way to program logic and are geared towards programmers and technical designers. Use the APIs to program applications, develop Kanzi Engine plugins, interface with devices and application execution environment. See [Kanzi Engine C++ API reference](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/index.html) and [Kanzi Engine Java API reference](https://docs.kanzi.com/4.1.0/en/reference/kanzi-java-api/index.html).  |  
## See also
[Tutorial: Hello world!](https://docs.kanzi.com/4.1.0/en/tutorials/hello-world/hello-world.html)
[Tutorial: Kanzi Engine API advanced use](https://docs.kanzi.com/4.1.0/en/tutorials/programmer-tutorial/programmer-tutorial.html)
[Triggers](https://docs.kanzi.com/4.1.0/en/working-with/triggers/triggers.html)
[State manager](https://docs.kanzi.com/4.1.0/en/working-with/state-managers/state-managers.html)
[Kanzi Engine C++ API reference](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/index.html)

<!-- NODE_END: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/logic-programming.html -->


<!-- NODE_START: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/animation-system.html (Depth 2) -->
<!-- SOURCE_URL: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/animation-system.html -->
### Animation system

> **Summary**: The Kanzi animation system documentation explains how to animate properties over time using animations, timelines, and animation players. It covers from-to animations and keyframe animations, property timelines, property field timelines, and parallel timelines, as well as various animation players like Animation Player, Float/Int Value Accumulators, Property Driven Animation Player, and Property Target Interpolators. It also describes how property timeline animations work via the property manager modifier stack and outlines the workflow for animating objects.

Copy page 
 
View this page as Markdown.
 
Animation system allows you to animate properties over time, control playback, map property value changes to animation.
![../_images/animation-system-banner.png](https://docs.kanzi.com/4.1.0/en/_images/animation-system-banner.png)
The Kanzi animation system consists:
  * Animations define how to animate a property. For example, an animation defines how to animate a color from red to green, or a float value from 7 to 11. In Kanzi you can create these types of animations:  
| From-to animation defines from which to which value to change the value of a property. You can omit either of these values to animate either from the current value or to the current value of the property. From-to animations use an easing curve that defines the rate of change for the animation. You can use one of the easing curves that comes with Kanzi, or define your own.  |  ![../_images/from-to-animation.png](https://docs.kanzi.com/4.1.0/en/_images/from-to-animation.png)  |  
| --- | --- |  
| Keyframe animation uses keyframes that define the property value and time at which the animation reaches that value. In Kanzi you can create linear, step, and Bézier spline keyframes.  |  ![../_images/keyframe-animation.png](https://docs.kanzi.com/4.1.0/en/_images/keyframe-animation.png)  |  
  * Timelines map the animations to time and to objects you want to animate. The animations themselves do not animate an object, the timelines do. In Kanzi you can create these types of timelines:  
| Property timeline applies an animation to a property of an object. For example, to change the layout size of an Image node, use the property timeline to animate the Layout Width and Layout Height properties of the node.  |  ![../_images/property-timeline.png](https://docs.kanzi.com/4.1.0/en/_images/property-timeline.png)  |  
| --- | --- |  
| Property field timeline applies an animation to one or more fields of a property of an object. For example, you can use a separate animation for each color channel to change the color of the text in a Text Block node.  |  ![../_images/property-field-timeline.png](https://docs.kanzi.com/4.1.0/en/_images/property-field-timeline.png)  |  
|  Parallel timeline allows you to group timelines which Kanzi plays at the same time. A parallel timeline ends when the animations in the last child timeline end. Use this timeline to organize collections of timelines and create a composition of timelines.  |  ![../_images/parallel-timeline.png](https://docs.kanzi.com/4.1.0/en/_images/parallel-timeline.png)  |  
  * Animation players receive messages that you can send with actions and generate messages that you intercept with triggers. For example, you can send messages to start, stop, and pause playback, and can receive messages to find out when the animation playback started, stopped, or was completed.
In Kanzi these animation players are available:  
|  ![../_images/animation-player1.png](https://docs.kanzi.com/4.1.0/en/_images/animation-player1.png)  |  Animation Player. Use the Animation Player to play and control the playback of keyframe animations. See [Using keyframe animations](https://docs.kanzi.com/4.1.0/en/working-with/animations/triggering-animations-with-the-play-animation-action.html).  |  
| --- | --- |  
|  ![../_images/float-value-accumulator.png](https://docs.kanzi.com/4.1.0/en/_images/float-value-accumulator.png)  |  Float Value Accumulator. Use a Float Value Accumulator to increment a value of a float property type or a property field over time or per frame. See [Incrementing the value of a property type](https://docs.kanzi.com/4.1.0/en/working-with/animations/property-animator.html).  |  
|  ![../_images/int-value-accumulator.png](https://docs.kanzi.com/4.1.0/en/_images/int-value-accumulator.png)  |  Int Value Accumulator. Use an Int Value Accumulator to increment a value of an integer property type over time or per frame. See [Incrementing the value of a property type](https://docs.kanzi.com/4.1.0/en/working-with/animations/property-animator.html).  |  
|  ![../_images/property-driven-animation-player.png](https://docs.kanzi.com/4.1.0/en/_images/property-driven-animation-player.png)  |  Property Driven Animation Player. Use the Property Driven Animation Player when you want to use a property type instead of time to control a keyframe animation. See [Creating property-driven animations](https://docs.kanzi.com/4.1.0/en/working-with/animations/property-driven-animations.html).  |  
|  ![../_images/property-target-interpolator.png](https://docs.kanzi.com/4.1.0/en/_images/property-target-interpolator.png)  |  Property Target Interpolator. Use the Property Target Interpolator when you want to dynamically set the target value for a property and want to interpolate the current value to the target value over time. See [Interpolating property values](https://docs.kanzi.com/4.1.0/en/working-with/animations/property-target-interpolator.html).  |  
|  ![../_images/property-target-easing-interpolator.png](https://docs.kanzi.com/4.1.0/en/_images/property-target-easing-interpolator.png)  |  Property Target Easing Interpolator. Use the Property Target Easing Interpolator when you want to dynamically set the target value for a property and want to interpolate the current value to the target value over time using an easing function. Easing functions enable you to create lifelike animations that offer a more pleasant user experience. See [Interpolating property values using easing functions](https://docs.kanzi.com/4.1.0/en/working-with/animations/property-target-easing-interpolator.html).  |  

## How the property timeline animations work
Property timeline uses the Kanzi property manager modifier stack. Kanzi applies the animation to the base value of the property, or the previous modifier in the stack (which can be another animation). That way you can stack animations that affect the same property.
When the animation ends it remains alive. The object describing the animation still exists so that the modifier can provide the property value when requested. When you use the Kanzi Engine API to apply multiple animations to an object you have to remove them, otherwise they keep consuming resources. Other systems, like the state manager and the Animation Player, keep track of animations themselves, so that you do not need to.
Tip
In the Kanzi Studio Node Tree window, an indicator next to a node shows when a State Manager, Binding, Data Source Binding, or an Animation overrides the values of some properties in that node.
![../_images/node-override-notice.png](https://docs.kanzi.com/4.1.0/en/_images/node-override-notice.png)
To navigate to the source of the override in the Kanzi Studio project, right-click the override indicator and select the source you wish to navigate to from the context menu.
## The workflow of animating an object
To animate an object:
  1. Create an animation:
     * For a from-to animation set from which to which value you want to animate a property, set the duration of the animation, and the easing curve.
     * For a keyframe animation populate the animation with keyframes that set the value of a property at the time when the animation must reach that value, and use either linear, step, or Bézier spline keyframe.
  2. Create a timeline.
  3. Assign the animation to the timeline.
  4. Play back the animation.

## See also
[Creating animations and timelines using the Kanzi Engine API](https://docs.kanzi.com/4.1.0/en/working-with/animations/creating-animations-using-api.html)
[Animations](https://docs.kanzi.com/4.1.0/en/working-with/animations/animations.html)
[Animations best practices](https://docs.kanzi.com/4.1.0/en/best-practices/animations/animations-best-practices.html)
[Kanzi fundamentals](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/kanzi-fundamentals.html)
[Using keyframe animations](https://docs.kanzi.com/4.1.0/en/working-with/animations/triggering-animations-with-the-play-animation-action.html)
[Creating property-driven animations](https://docs.kanzi.com/4.1.0/en/working-with/animations/property-driven-animations.html)
[Interpolating property values](https://docs.kanzi.com/4.1.0/en/working-with/animations/property-target-interpolator.html)
[Interpolating property values using easing functions](https://docs.kanzi.com/4.1.0/en/working-with/animations/property-target-easing-interpolator.html)

<!-- NODE_END: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/animation-system.html -->


<!-- NODE_START: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/kanzi-graphics.html (Depth 2) -->
<!-- SOURCE_URL: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/kanzi-graphics.html -->
### Kanzi graphics

> **Summary**: Kanzi graphics (kzgfx) is the render hardware interface (RHI) for Kanzi, providing an abstraction layer for different graphics APIs (OpenGL 3.3+, OpenGL ES 3.0+, WebGL 2.0, and Vulkan 1.1+). It consists of graphics objects (buffers, images, shaders, pipelines, etc.) and commands (copy, draw, present, etc.) that are recorded in command buffers for deferred execution. The API is thread-safe, supports layers for validation and statistics, and is intended for advanced use cases like compute or manual rendering. Most applications use higher-level rendering concepts instead.

Copy page 
 
View this page as Markdown.
 
Kanzi graphics (kzgfx) is the render hardware interface (RHI) for Kanzi. It provides an abstraction layer that allows Kanzi to use different graphics APIs. Kanzi provides these implementations of the interface:
  * An OpenGL-based backend that supports OpenGL 3.3+, OpenGL ES 3.0+, and WebGL 2.0
  * A Vulkan 1.1+ backend

Most Kanzi applications do not need to use the Kanzi graphics API directly and instead use high-level concepts from the Rendering system. Use Kanzi graphics directly only to accomplish advanced use cases like compute or manual rendering.
The Kanzi graphics API has these major components:
  * Graphics objects represent an entity within the interface, such as a buffer, image, or shader.
  * Commands operate on the graphics objects and are collected into command buffers for deferred execution. Operations like copy, draw, and present are typical commands.

The shader programs used by Kanzi graphics are required to provide reflection information in addition to the raw shader source. For most use cases, Kanzi Studio does this automatically when exporting a project, but you can also do this with the Kanzi Shader Compiler library or through manual construction.
The Kanzi graphics API is safe to call from any thread. This is in contrast to the OpenGL family of APIs which require all calls to be made within a thread specific context. The Kanzi graphics OpenGL backend provides a rendering thread to meet this requirement of the API.
Keep in mind that you cannot use a specific graphics API, such as OpenGL or Vulkan, directly from a custom Kanzi application or plugin. Use the Kanzi graphics API instead.
In addition to the backends, Kanzi graphics allows you to configure multiple layers that allow additional behavior independent of the backend. Each Kanzi graphics function call is first routed through the list of layers before being processed by the backend. Kanzi provides these layers:
  * Validation layer reports violations of expected API usage.
  * Statistics layer contains a set of statistics about Kanzi graphics.

## Graphics objects
You can create graphics objects using the relevant create info object and the `gfx::create[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a11049.html#ga4438f40172c2ddb242362f4ad0317540)` function. Graphics objects are represented through a type-specific handle guard object. The guards are reference counted so that when all references are destroyed, the object itself is queued for destruction.
Once created, the definition of objects is immutable. For example, you cannot resize a buffer or an image. Instead you must create a new object with the new properties.  
| Object  | Creation struct  | Description  |  
| --- | --- | --- |  
| Buffer  | `gfx::BufferCreateInfo[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15846.html)`  | Represents a block of memory that can be in CPU or GPU memory. Typically used to store uniforms, vertex or index data, and other generic usage.  |  
| Image  | `gfx::ImageCreateInfo[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15850.html)`  | Represents an image object that can be sampled from a shader.  |  
| Frame Buffer  | `gfx::FrameBufferCreateInfo[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15858.html)`  | Represents an on screen or offscreen frame buffer that can be used as a render target.  |  
| Vertex Input State  | `gfx::VertexInputStateCreateInfo[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15910.html)`  | Represents a layout for vertex data stored in a buffer.  |  
| Depth Stencil State  | `gfx::DepthStencilStateCreateInfo[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15922.html)`  | Represents a set of configuration options about how a depth or stencil image is used.  |  
| Blend State  | `gfx::BlendStateCreateInfo[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15914.html)`  | Represents a set of configuration options about how to blend the output of a render pipeline.  |  
| Raster State  | `gfx::RasterStateCreateInfo[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15930.html)`  | Represents a set of configuration options about how the rasterizer behaves, such as fill mode, cull mode, and triangle topology.  |  
| Sampler  | `gfx::SamplerCreateInfo[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15866.html)`  | Represents a sampler object to configure how an image is sampled by a shader.  |  
| Render Resource Set  | `gfx::RenderResourceSetCreateInfo[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15894.html)`  | Represents a set of resources such as buffers, images, and samplers that are required by a render pipeline.  |  
| Compute Resource Set  | `gfx::ComputeResourceSetCreateInfo[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15898.html)`  | Represents a set of resources such as buffers and images that are required by a compute pipeline.  |  
| Shader  | `gfx::ShaderCreateInfo[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15842.html)`  | Represents a shader program. This could be a vertex, fragment, tesselation, geometry, or compute shader. These are combined with other state objects to form a complete render or compute pipeline.  |  
| Compute Pipeline  | `gfx::ComputePipelineCreateInfo[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15838.html)`  | Represents a compute program.  |  
| Render Pipeline  | `gfx::RenderPipelineCreateInfo[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15934.html)`  | Represents a render program that contains a complete set of shaders, a depth stencil state, a blend state, a raster state, a vertex input state, and a description of the render target.  |  
| Render Pass  | `gfx::RenderPassCreateInfo[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15950.html)`  | Represents a set of render targets and how those targets are loaded or stored in memory.  |  
| Command Buffer  | `gfx::CommandBufferCreateInfo[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15954.html)`  | Represents a region in CPU memory that contains Kanzi graphics commands for execution by the Kanzi graphics API.  |  
| GPU Fence  | `gfx::GpuFenceCreateInfo[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15958.html)`  | Represents a syncronization object that can be used to allow a thread to wait until a specific portion of a command buffer has been completed.  |  
## Commands
Commands are recorded in command buffers, and executed with the `gfx::processCommands[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a11049.html#ga97a0fc6cc3a2fc0faead588ec5980d98)` function. The loaded backend asynchronously handles the execution of commands.  
| Command  | Description  |  
| --- | --- |  
| `gfx::CopyBufferCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15634.html)`  | Copies memory from a source buffer to a destination buffer.  |  
| `gfx::CopyBufferToImageCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15642.html)`  | Copies memory from a source buffer to a destination image.  |  
| `gfx::CopyImageCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15638.html)`  | Copies contents from a source image to a destination image.  |  
| `gfx::CopyImageToBufferCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15646.html)`  | Copies contents from a source image to a destination image.  |  
| `gfx::CopySurfaceToBufferCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15650.html)`  | Copies contents from an on screen frame buffer to a destination buffer.  |  
| `gfx::BeginRenderPassCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15654.html)`  | Starts rendering to a specified render pass.  |  
| `gfx::EndRenderPassCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15658.html)`  | Ends rendering from the previous render pass.  |  
| `gfx::BeginRenderPipelineCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15662.html)`  | Attaches a render pipeline for usage by future draw commands.  |  
| `gfx::EndRenderPipelineCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15666.html)`  | Ends the usage of the previous render pipeline.  |  
| `gfx::ConstantDataCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15670.html)`  | Updates constant uniform data for use by following draw commands.  |  
| `gfx::DrawCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15674.html)`  | Draws a number of triangles or instances based on the currently set resources.  |  
| `gfx::DrawIndirectCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15678.html)`  | Issues an indirect draw based on the contents of a buffer.  |  
| `gfx::BeginComputePipelineCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15682.html)`  | Attaches a compute pipeline for use by future dispatch commands.  |  
| `gfx::EndComputePipelineCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15686.html)`  | Ends the usage of the previous compute pipeline.  |  
| `gfx::DispatchCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15690.html)`  | Dispatches a compute operation with the currently set resources.  |  
| `gfx::DispatchIndirectCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15694.html)`  | Issues an indirect dispatch based on the contents of a buffer.  |  
| `gfx::PresentCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15698.html)`  | Tells the platform layer to present an on screen surface to the screen.  |  
| `gfx::SignalGpuFenceCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15702.html)`  | Signals a GPU Fence object.  |  
| `gfx::ResolveMultisampleImageCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15706.html)`  | Explicitly resolves a multisampled image.  |  
| `gfx::GenerateMipmapsCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15710.html)`  | Generates the mipmaps for an image.  |  
| `gfx::SetViewportCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15722.html)`  | Sets the active viewport for future rendering operaions.  |  
| `gfx::SetScissorCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15726.html)`  | Sets the active scissor for future rendering operaions.  |  
| `gfx::ClearCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15730.html)`  | Clears the render targets from the current render pass.  |  
| `gfx::SetLineWidthCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15734.html)`  | Sets the line width when using the line based rasterization option.  |  
| `gfx::BindVertexInputCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15738.html)`  | Binds a set of vertex buffers and an optional index buffer.  |  
| `gfx::SetUniformOffsetCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15742.html)`  | Sets the offset to be used within a uniform buffer for the following operations.  |  
| `gfx::BindRenderResourceSetCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15746.html)`  | Binds a set of Render Resource Sets for future rendering operations.  |  
| `gfx::BindComputeResourceSetCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15750.html)`  | Binds a set of Compute Resource Sets for future compute operations.  |  
| `gfx::SubroutineCommand[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a15630.html)`  | Allows a command buffer to call a second command buffer before execution returns to the next command.  |  
## See also
[Rendering](https://docs.kanzi.com/4.1.0/en/working-with/rendering/rendering.html)
`Graphics[](https://docs.kanzi.com/4.1.0/en/reference/kanzi-runtime-api/a11048.html)`

<!-- NODE_END: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/kanzi-graphics.html -->


<!-- NODE_START: https://docs.kanzi.com/4.1.0/en/tutorials/getting-started/getting-started.html (Depth 2) -->
<!-- SOURCE_URL: https://docs.kanzi.com/4.1.0/en/tutorials/getting-started/getting-started.html -->
### Tutorial: Getting started with Kanzi Studio

Copy page 
 
View this page as Markdown.
 
In this tutorial, you learn about the basic Kanzi Studio features by creating a simple Kanzi application. If you want to learn how to use Kanzi Studio, this tutorial is the right place to start.
After completing this tutorial, you can focus on learning how to use specific Kanzi features by completing other tutorials.
This video shows the result of the tutorial.
![../../_images/getting-started-completed.gif](https://docs.kanzi.com/4.1.0/en/_images/getting-started-completed.gif)
Kanzi consists of these main components:
  * Kanzi Studio is a tool where you can create user interfaces, import 2D and 3D content from other content creation tools, and export production binary files. In Kanzi Studio, you can implement the design for your application and work on every aspect of interaction design.
  * Kanzi Engine is a graphics and user interface execution environment for the binary files that you generate from a Kanzi Studio project. Kanzi Engine supports leading operating systems and hardware platforms out of the box. This allows engineers to focus on application development, rather than on optimization and integration.

[Start with the tutorial](https://docs.kanzi.com/4.1.0/en/tutorials/getting-started/step-1.html)

<!-- NODE_END: https://docs.kanzi.com/4.1.0/en/tutorials/getting-started/getting-started.html -->


<!-- NODE_START: https://docs.kanzi.com/4.1.0/en/tutorials/tutorials.html (Depth 2) -->
<!-- SOURCE_URL: https://docs.kanzi.com/4.1.0/en/tutorials/tutorials.html -->
### Tutorials

> **Summary**: This page is an index of tutorials for Kanzi Studio and Kanzi Engine, organized by topic areas such as getting started, UI structure, Android framework, UI controls, input, rendering, animations, localization/theming, instrument cluster, C++ API, and Lua API. It provides links to detailed tutorials covering everything from creating simple applications to advanced C++ and Lua programming.

Copy page 
 
View this page as Markdown.
 
## Getting started
[![../_images/getting-started.png](https://docs.kanzi.com/4.1.0/en/_images/getting-started.png)](https://docs.kanzi.com/4.1.0/en/tutorials/getting-started/getting-started.html)
[Getting started with Kanzi Studio](https://docs.kanzi.com/4.1.0/en/tutorials/getting-started/getting-started.html)
[![../_images/first.png](https://docs.kanzi.com/4.1.0/en/_images/first.png)](https://docs.kanzi.com/4.1.0/en/tutorials/first/first.html)
[Create a simple application in Kanzi Studio](https://docs.kanzi.com/4.1.0/en/tutorials/first/first.html)
## UI structure
[![../_images/activity.png](https://docs.kanzi.com/4.1.0/en/_images/activity.png)](https://docs.kanzi.com/4.1.0/en/tutorials/activity/activity.html)
[Structure application UI](https://docs.kanzi.com/4.1.0/en/tutorials/activity/activity.html)
[![../_images/data-trigger.png](https://docs.kanzi.com/4.1.0/en/_images/data-trigger.png)](https://docs.kanzi.com/4.1.0/en/tutorials/data-trigger/data-trigger.html)
[Control application UI](https://docs.kanzi.com/4.1.0/en/tutorials/data-trigger/data-trigger.html)
[![../_images/data-driven.png](https://docs.kanzi.com/4.1.0/en/_images/data-driven.png)](https://docs.kanzi.com/4.1.0/en/tutorials/data-driven-activities/data-driven-activities.html)
[Generate UI from a data source](https://docs.kanzi.com/4.1.0/en/tutorials/data-driven-activities/data-driven-activities.html)
[![../_images/multi-project.png](https://docs.kanzi.com/4.1.0/en/_images/multi-project.png)](https://docs.kanzi.com/4.1.0/en/tutorials/multi-project/multi-project.html)
[Combine projects into a single application](https://docs.kanzi.com/4.1.0/en/tutorials/multi-project/multi-project.html)
## Kanzi Android framework (droidfw)
[![../_images/android-getting-started.png](https://docs.kanzi.com/4.1.0/en/_images/android-getting-started.png)](https://docs.kanzi.com/4.1.0/en/tutorials/android-getting-started/android-getting-started.html)
[Getting started with Kanzi Android framework](https://docs.kanzi.com/4.1.0/en/tutorials/android-getting-started/android-getting-started.html)
[![../_images/android-data-source.png](https://docs.kanzi.com/4.1.0/en/_images/android-data-source.png)](https://docs.kanzi.com/4.1.0/en/tutorials/android-data-source/android-data-source.html)
[Data sources for Android](https://docs.kanzi.com/4.1.0/en/tutorials/android-data-source/android-data-source.html)
## UI controls
[![../_images/button.png](https://docs.kanzi.com/4.1.0/en/_images/button.png)](https://docs.kanzi.com/4.1.0/en/tutorials/button/button.html)
[Create a button that reacts to user actions](https://docs.kanzi.com/4.1.0/en/tutorials/button/button.html)
[![../_images/toggle-button1.png](https://docs.kanzi.com/4.1.0/en/_images/toggle-button1.png)](https://docs.kanzi.com/4.1.0/en/tutorials/toggle-button/toggle-button.html)
[Create a toggle button](https://docs.kanzi.com/4.1.0/en/tutorials/toggle-button/toggle-button.html)
[![../_images/slider.png](https://docs.kanzi.com/4.1.0/en/_images/slider.png)](https://docs.kanzi.com/4.1.0/en/tutorials/slider/slider.html)
[Create a slider](https://docs.kanzi.com/4.1.0/en/tutorials/slider/slider.html)
[![../_images/list-box.png](https://docs.kanzi.com/4.1.0/en/_images/list-box.png)](https://docs.kanzi.com/4.1.0/en/tutorials/list-box/list-box.html)
[Create a contacts list with a Grid List Box](https://docs.kanzi.com/4.1.0/en/tutorials/list-box/list-box.html)
[![../_images/rotation.png](https://docs.kanzi.com/4.1.0/en/_images/rotation.png)](https://docs.kanzi.com/4.1.0/en/tutorials/rotation/rotation.html)
[Rotate a 3D model](https://docs.kanzi.com/4.1.0/en/tutorials/rotation/rotation.html)
## Input
[![../_images/ui-navigation.png](https://docs.kanzi.com/4.1.0/en/_images/ui-navigation.png)](https://docs.kanzi.com/4.1.0/en/tutorials/ui-navigation/ui-navigation.html)
[Create UI navigation](https://docs.kanzi.com/4.1.0/en/tutorials/ui-navigation/ui-navigation.html)
[![../_images/pan-zoom-tap.png](https://docs.kanzi.com/4.1.0/en/_images/pan-zoom-tap.png)](https://docs.kanzi.com/4.1.0/en/tutorials/pan-zoom-tap/pan-zoom-tap.html)
[Pan, zoom, tap](https://docs.kanzi.com/4.1.0/en/tutorials/pan-zoom-tap/pan-zoom-tap.html)
[![../_images/drag-and-drop.png](https://docs.kanzi.com/4.1.0/en/_images/drag-and-drop.png)](https://docs.kanzi.com/4.1.0/en/tutorials/drag-and-drop/drag-and-drop.html)
[Drag and drop](https://docs.kanzi.com/4.1.0/en/tutorials/drag-and-drop/drag-and-drop.html)
## Rendering
[![../_images/rendering.png](https://docs.kanzi.com/4.1.0/en/_images/rendering.png)](https://docs.kanzi.com/4.1.0/en/tutorials/materials-and-textures/materials-and-textures.html)
[Work with materials and textures](https://docs.kanzi.com/4.1.0/en/tutorials/materials-and-textures/materials-and-textures.html)
[![../_images/blur.png](https://docs.kanzi.com/4.1.0/en/_images/blur.png)](https://docs.kanzi.com/4.1.0/en/tutorials/blur/blur.html)
[Create a Gaussian blur effect](https://docs.kanzi.com/4.1.0/en/tutorials/blur/blur.html)
[![../_images/bloom.png](https://docs.kanzi.com/4.1.0/en/_images/bloom.png)](https://docs.kanzi.com/4.1.0/en/tutorials/bloom/bloom.html)
[Create a bloom effect](https://docs.kanzi.com/4.1.0/en/tutorials/bloom/bloom.html)
[![../_images/stencil.png](https://docs.kanzi.com/4.1.0/en/_images/stencil.png)](https://docs.kanzi.com/4.1.0/en/tutorials/stencil/stencil.html)
[Apply a stencil to 3D content](https://docs.kanzi.com/4.1.0/en/tutorials/stencil/stencil.html)
[![../_images/reflection.png](https://docs.kanzi.com/4.1.0/en/_images/reflection.png)](https://docs.kanzi.com/4.1.0/en/tutorials/reflections/reflections.html)
[Create reflections](https://docs.kanzi.com/4.1.0/en/tutorials/reflections/reflections.html)
[![../_images/progressive-rendering.png](https://docs.kanzi.com/4.1.0/en/_images/progressive-rendering.png)](https://docs.kanzi.com/4.1.0/en/tutorials/progressive-rendering/progressive-rendering.html)
[Distribute rendering across several frames](https://docs.kanzi.com/4.1.0/en/tutorials/progressive-rendering/progressive-rendering.html)
## Animations
[![../_images/keyframe.png](https://docs.kanzi.com/4.1.0/en/_images/keyframe.png)](https://docs.kanzi.com/4.1.0/en/tutorials/keyframe-animations/keyframe-animations.html)
[Create keyframe animations](https://docs.kanzi.com/4.1.0/en/tutorials/keyframe-animations/keyframe-animations.html)
[![../_images/interpolate.png](https://docs.kanzi.com/4.1.0/en/_images/interpolate.png)](https://docs.kanzi.com/4.1.0/en/tutorials/interpolate/interpolate.html)
[Interpolate property values](https://docs.kanzi.com/4.1.0/en/tutorials/interpolate/interpolate.html)
[![../_images/activity-transitions.png](https://docs.kanzi.com/4.1.0/en/_images/activity-transitions.png)](https://docs.kanzi.com/4.1.0/en/tutorials/activity-transitions/activity-transitions.html)
[Animate transitions between Activities](https://docs.kanzi.com/4.1.0/en/tutorials/activity-transitions/activity-transitions.html)
## Localization and theming
[![../_images/localization.png](https://docs.kanzi.com/4.1.0/en/_images/localization.png)](https://docs.kanzi.com/4.1.0/en/tutorials/localization/localization.html)
[Localize your application](https://docs.kanzi.com/4.1.0/en/tutorials/localization/localization.html)
[![../_images/localization-rtl.png](https://docs.kanzi.com/4.1.0/en/_images/localization-rtl.png)](https://docs.kanzi.com/4.1.0/en/tutorials/localization-rtl/localization-rtl.html)
[Localize applications for right-to-left locales](https://docs.kanzi.com/4.1.0/en/tutorials/localization-rtl/localization-rtl.html)
[![../_images/theme.png](https://docs.kanzi.com/4.1.0/en/_images/theme.png)](https://docs.kanzi.com/4.1.0/en/tutorials/theming/theming.html)
[Theme your application](https://docs.kanzi.com/4.1.0/en/tutorials/theming/theming.html)
## Instrument cluster
[![../_images/gauges.png](https://docs.kanzi.com/4.1.0/en/_images/gauges.png)](https://docs.kanzi.com/4.1.0/en/tutorials/gauges/gauges.html)
[Control a gauge needle with a property](https://docs.kanzi.com/4.1.0/en/tutorials/gauges/gauges.html)
[![../_images/indicator.png](https://docs.kanzi.com/4.1.0/en/_images/indicator.png)](https://docs.kanzi.com/4.1.0/en/tutorials/indicator/indicator.html)
[Control an indicator using the state manager](https://docs.kanzi.com/4.1.0/en/tutorials/indicator/indicator.html)
[![../_images/responsive.png](https://docs.kanzi.com/4.1.0/en/_images/responsive.png)](https://docs.kanzi.com/4.1.0/en/tutorials/dynamic-layout/dynamic-layout.html)
[Make your application layout dynamic](https://docs.kanzi.com/4.1.0/en/tutorials/dynamic-layout/dynamic-layout.html)
## C++ API
[![../_images/hello.png](https://docs.kanzi.com/4.1.0/en/_images/hello.png)](https://docs.kanzi.com/4.1.0/en/tutorials/hello-world/hello-world.html)
[Kanzi Engine API Hello world!](https://docs.kanzi.com/4.1.0/en/tutorials/hello-world/hello-world.html)
[![../_images/program-activities.png](https://docs.kanzi.com/4.1.0/en/_images/program-activities.png)](https://docs.kanzi.com/4.1.0/en/tutorials/program-activities/program-activities.html)
[Program Activities with C++ Code Behind](https://docs.kanzi.com/4.1.0/en/tutorials/program-activities/program-activities.html)
[![../_images/programmer.png](https://docs.kanzi.com/4.1.0/en/_images/programmer.png)](https://docs.kanzi.com/4.1.0/en/tutorials/programmer-tutorial/programmer-tutorial.html)
[Kanzi Engine API advanced use](https://docs.kanzi.com/4.1.0/en/tutorials/programmer-tutorial/programmer-tutorial.html)
[![../_images/loading.png](https://docs.kanzi.com/4.1.0/en/_images/loading.png)](https://docs.kanzi.com/4.1.0/en/tutorials/loading/loading.html)
[Load and deploy resources asynchronously](https://docs.kanzi.com/4.1.0/en/tutorials/loading/loading.html)
[![../_images/data-sources.png](https://docs.kanzi.com/4.1.0/en/_images/data-sources.png)](https://docs.kanzi.com/4.1.0/en/tutorials/data-sources/data-sources.html)
[Get application data from a data source](https://docs.kanzi.com/4.1.0/en/tutorials/data-sources/data-sources.html)
## Lua API
[![../_images/fifteen-puzzle.png](https://docs.kanzi.com/4.1.0/en/_images/fifteen-puzzle.png)](https://docs.kanzi.com/4.1.0/en/tutorials/fifteen-puzzle/fifteen-puzzle.html)
[Kanzi Engine Lua API](https://docs.kanzi.com/4.1.0/en/tutorials/fifteen-puzzle/fifteen-puzzle.html)
## See also
To learn why Kanzi works the way it works, see [Kanzi fundamentals](https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/kanzi-fundamentals.html).
To learn how to use specific features in Kanzi, see [Working with …](https://docs.kanzi.com/4.1.0/en/working-with/working-with.html).
[Examples](https://docs.kanzi.com/4.1.0/en/examples/examples.html)

<!-- NODE_END: https://docs.kanzi.com/4.1.0/en/tutorials/tutorials.html -->


<!-- NODE_START: https://docs.kanzi.com/4.1.0/en/working-with/working-with.html (Depth 2) -->
<!-- SOURCE_URL: https://docs.kanzi.com/4.1.0/en/working-with/working-with.html -->
### Working with …

> **Summary**: This page serves as the main index for the Kanzi documentation's 'Working with...' section, providing links to detailed guides on various Kanzi features and workflows. It covers topics such as 2D/3D content, animations, layouts, input handling, data sources, rendering, shaders, state managers, and platform-specific development (Android, iOS, Java/Kotlin, Lua, Rust). The page is a hub for learning how to use Kanzi Studio and Kanzi Engine to create and deploy embedded UI applications.

Copy page 
 
View this page as Markdown.
 
Here you can find information about Kanzi features.
[![../_images/2dcontent96x96.png](https://docs.kanzi.com/4.1.0/en/_images/2dcontent96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/2d-content/adjusting-the-appearance.html)
[2D content](https://docs.kanzi.com/4.1.0/en/working-with/2d-content/adjusting-the-appearance.html)
[![../_images/effect96x96.png](https://docs.kanzi.com/4.1.0/en/_images/effect96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/effects/2d-effects.html)
[2D effects](https://docs.kanzi.com/4.1.0/en/working-with/effects/2d-effects.html)
[![../_images/3dasset96x96.png](https://docs.kanzi.com/4.1.0/en/_images/3dasset96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/3d-assets/3d-assets.html)
[3D assets](https://docs.kanzi.com/4.1.0/en/working-with/3d-assets/3d-assets.html)
[![../_images/activities96x96.png](https://docs.kanzi.com/4.1.0/en/_images/activities96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/activities/activities.html)
[Activities](https://docs.kanzi.com/4.1.0/en/working-with/activities/activities.html)
[](https://docs.kanzi.com/4.1.0/en/working-with/ai-tools/using-kanzi-ai-tools.html)
[AI tools](https://docs.kanzi.com/4.1.0/en/working-with/ai-tools/using-kanzi-ai-tools.html)
[![../_images/alias96x96.png](https://docs.kanzi.com/4.1.0/en/_images/alias96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/aliases/using-aliases.html)
[Aliases](https://docs.kanzi.com/4.1.0/en/working-with/aliases/using-aliases.html)
[![../_images/android96x96.png](https://docs.kanzi.com/4.1.0/en/_images/android96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/android/android.html)
[Android](https://docs.kanzi.com/4.1.0/en/working-with/android/android.html)
[![../_images/animation96x96.png](https://docs.kanzi.com/4.1.0/en/_images/animation96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/animations/animations.html)
[Animations](https://docs.kanzi.com/4.1.0/en/working-with/animations/animations.html)
[![../_images/applicationconfigurations96x96.png](https://docs.kanzi.com/4.1.0/en/_images/applicationconfigurations96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/application-configurations/application-configuration.html)
[Application](https://docs.kanzi.com/4.1.0/en/working-with/application-configurations/application-configuration.html)
[![../_images/assetpackages96x96.png](https://docs.kanzi.com/4.1.0/en/_images/assetpackages96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/asset-packages/asset-packages.html)
[Asset packages](https://docs.kanzi.com/4.1.0/en/working-with/asset-packages/asset-packages.html)
[![../_images/assettoolkit96x96.png](https://docs.kanzi.com/4.1.0/en/_images/assettoolkit96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/asset-toolkit/asset-toolkit.html)
[Asset Toolkit](https://docs.kanzi.com/4.1.0/en/working-with/asset-toolkit/asset-toolkit.html)
[![../_images/automation96x96.png](https://docs.kanzi.com/4.1.0/en/_images/automation96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/automation/automation.html)
[Automation](https://docs.kanzi.com/4.1.0/en/working-with/automation/automation.html)
[![../_images/bindings96x96.png](https://docs.kanzi.com/4.1.0/en/_images/bindings96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/bindings/bindings.html)
[Bindings](https://docs.kanzi.com/4.1.0/en/working-with/bindings/bindings.html)
[![../_images/bookmarks96x96.png](https://docs.kanzi.com/4.1.0/en/_images/bookmarks96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/bookmarks/using-bookmarks.html)
[Bookmarks](https://docs.kanzi.com/4.1.0/en/working-with/bookmarks/using-bookmarks.html)
[![../_images/brush96x96.png](https://docs.kanzi.com/4.1.0/en/_images/brush96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/brushes/using-brushes.html)
[Brushes](https://docs.kanzi.com/4.1.0/en/working-with/brushes/using-brushes.html)
[![../_images/button96x96.png](https://docs.kanzi.com/4.1.0/en/_images/button96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/buttons/buttons.html)
[Button nodes](https://docs.kanzi.com/4.1.0/en/working-with/buttons/buttons.html)
[![../_images/camera96x96.png](https://docs.kanzi.com/4.1.0/en/_images/camera96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/cameras/cameras.html)
[Camera node](https://docs.kanzi.com/4.1.0/en/working-with/cameras/cameras.html)
[![../_images/color96x96.png](https://docs.kanzi.com/4.1.0/en/_images/color96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/color/color.html)
[Color workflow](https://docs.kanzi.com/4.1.0/en/working-with/color/color.html)
[![../_images/contentlayout96x96.png](https://docs.kanzi.com/4.1.0/en/_images/contentlayout96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/layouts/using-content-layouts.html)
[Content Layout nodes](https://docs.kanzi.com/4.1.0/en/working-with/layouts/using-content-layouts.html)
[![../_images/datasource96x96.png](https://docs.kanzi.com/4.1.0/en/_images/datasource96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/data-sources/data-sources.html)
[Data sources](https://docs.kanzi.com/4.1.0/en/working-with/data-sources/data-sources.html)
[![../_images/deploy96x96.png](https://docs.kanzi.com/4.1.0/en/_images/deploy96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/deploying-applications/deploying-kanzi-applications.html)
[Deploying Applications](https://docs.kanzi.com/4.1.0/en/working-with/deploying-applications/deploying-kanzi-applications.html)
[![../_images/dock96x96.png](https://docs.kanzi.com/4.1.0/en/_images/dock96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/layouts/using-dock-layouts.html)
[Dock Layout nodes](https://docs.kanzi.com/4.1.0/en/working-with/layouts/using-dock-layouts.html)
[![../_images/empty96x96.png](https://docs.kanzi.com/4.1.0/en/_images/empty96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/empty-nodes/using-empty-nodes.html)
[Empty Node nodes](https://docs.kanzi.com/4.1.0/en/working-with/empty-nodes/using-empty-nodes.html)
[![../_images/assets96x96.png](https://docs.kanzi.com/4.1.0/en/_images/assets96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/factory-content/factory-content.html)
[Factory content](https://docs.kanzi.com/4.1.0/en/working-with/factory-content/factory-content.html)
[![../_images/filters96x96.png](https://docs.kanzi.com/4.1.0/en/_images/filters96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/filters/filters.html)
[Filters](https://docs.kanzi.com/4.1.0/en/working-with/filters/filters.html)
[![../_images/flow96x96.png](https://docs.kanzi.com/4.1.0/en/_images/flow96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/layouts/using-flow-layouts.html)
[Flow Layout nodes](https://docs.kanzi.com/4.1.0/en/working-with/layouts/using-flow-layouts.html)
[![../_images/focus96x96.png](https://docs.kanzi.com/4.1.0/en/_images/focus96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/focus/focus.html)
[Focus](https://docs.kanzi.com/4.1.0/en/working-with/focus/focus.html)
[![../_images/grid96x96.png](https://docs.kanzi.com/4.1.0/en/_images/grid96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/grids/using-grid-layouts.html)
[Grid Layout nodes](https://docs.kanzi.com/4.1.0/en/working-with/grids/using-grid-layouts.html)
[![../_images/image96x96.png](https://docs.kanzi.com/4.1.0/en/_images/image96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/images/images.html)
[Images](https://docs.kanzi.com/4.1.0/en/working-with/images/images.html)
[![../_images/assetsimport96x96.png](https://docs.kanzi.com/4.1.0/en/_images/assetsimport96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/importing/importing.html)
[Importing](https://docs.kanzi.com/4.1.0/en/working-with/importing/importing.html)
[![../_images/input96x96.png](https://docs.kanzi.com/4.1.0/en/_images/input96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/input/handling-input.html)
[Input](https://docs.kanzi.com/4.1.0/en/working-with/input/handling-input.html)
[![../_images/ios96x96.png](https://docs.kanzi.com/4.1.0/en/_images/ios96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/ios/ios.html)
[iOS](https://docs.kanzi.com/4.1.0/en/working-with/ios/ios.html)
[![../_images/instantiator96x96.png](https://docs.kanzi.com/4.1.0/en/_images/instantiator96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/instantiator-nodes/instantiator-nodes.html)
[Instantiator node](https://docs.kanzi.com/4.1.0/en/working-with/instantiator-nodes/instantiator-nodes.html)
[![../_images/java96x96.png](https://docs.kanzi.com/4.1.0/en/_images/java96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/java/using-java.html)
[Java and Kotlin](https://docs.kanzi.com/4.1.0/en/working-with/java/using-java.html)
[![../_images/kcp96x96.png](https://docs.kanzi.com/4.1.0/en/_images/kcp96x96.png)](https://docs.kanzi.com/4.1.0/en/best-practices/using-kanzi-command-prompt.html)
[Kanzi Command Prompt](https://docs.kanzi.com/4.1.0/en/best-practices/using-kanzi-command-prompt.html)
[![../_images/kzbbinaries96x96.png](https://docs.kanzi.com/4.1.0/en/_images/kzbbinaries96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/kzb-binaries/kzb-files.html)
[kzb files](https://docs.kanzi.com/4.1.0/en/working-with/kzb-binaries/kzb-files.html)
[![../_images/layouts.png](https://docs.kanzi.com/4.1.0/en/_images/layouts.png)](https://docs.kanzi.com/4.1.0/en/working-with/layouts/layouts.html)
[Layout control nodes](https://docs.kanzi.com/4.1.0/en/working-with/layouts/layouts.html)
[![../_images/light96x96.png](https://docs.kanzi.com/4.1.0/en/_images/light96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/lights/using-lights.html)
[Light nodes](https://docs.kanzi.com/4.1.0/en/working-with/lights/using-lights.html)
[![../_images/listbox96x96.png](https://docs.kanzi.com/4.1.0/en/_images/listbox96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/container-controls/list-box-nodes.html)
[List Box nodes](https://docs.kanzi.com/4.1.0/en/working-with/container-controls/list-box-nodes.html)
[![../_images/localization96x96.png](https://docs.kanzi.com/4.1.0/en/_images/localization96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/localization/localization.html)
[Localization](https://docs.kanzi.com/4.1.0/en/working-with/localization/localization.html)
[![../_images/logging96x96.png](https://docs.kanzi.com/4.1.0/en/_images/logging96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/logging/logging.html)
[Logging](https://docs.kanzi.com/4.1.0/en/working-with/logging/logging.html)
[![../_images/lua96x96.png](https://docs.kanzi.com/4.1.0/en/_images/lua96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/lua/using-lua.html)
[Lua](https://docs.kanzi.com/4.1.0/en/working-with/lua/using-lua.html)
[![../_images/materials96x96.png](https://docs.kanzi.com/4.1.0/en/_images/materials96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/materials/materials.html)
[Material types and materials](https://docs.kanzi.com/4.1.0/en/working-with/materials/materials.html)
[![../_images/mesh96x96.png](https://docs.kanzi.com/4.1.0/en/_images/mesh96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/meshes/meshes.html)
[Meshes](https://docs.kanzi.com/4.1.0/en/working-with/meshes/meshes.html)
[![../_images/model96x96.png](https://docs.kanzi.com/4.1.0/en/_images/model96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/meshes/meshes.html)
[Model node](https://docs.kanzi.com/4.1.0/en/working-with/meshes/meshes.html)
[![../_images/morph96x96.png](https://docs.kanzi.com/4.1.0/en/_images/morph96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/morphs/using-morphs.html)
[Morphs](https://docs.kanzi.com/4.1.0/en/working-with/morphs/using-morphs.html)
[![../_images/nodecomponent96x96.png](https://docs.kanzi.com/4.1.0/en/_images/nodecomponent96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/node-components/node-components.html)
[Node components](https://docs.kanzi.com/4.1.0/en/working-with/node-components/node-components.html)
[![../_images/objectsource96x96.png](https://docs.kanzi.com/4.1.0/en/_images/objectsource96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/object-sources/using-object-sources.html)
[Object sources](https://docs.kanzi.com/4.1.0/en/working-with/object-sources/using-object-sources.html)
[](https://docs.kanzi.com/4.1.0/en/working-with/package-manager/package-manager.html)
[Package Manager](https://docs.kanzi.com/4.1.0/en/working-with/package-manager/package-manager.html)
[![../_images/pagehost96x96.png](https://docs.kanzi.com/4.1.0/en/_images/pagehost96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/pages/using-pages.html)
[Page and Page Host nodes](https://docs.kanzi.com/4.1.0/en/working-with/pages/using-pages.html)
[![../_images/performanceprofiling96x96.png](https://docs.kanzi.com/4.1.0/en/_images/performanceprofiling96x96.png)](https://docs.kanzi.com/4.1.0/en/best-practices/performance/profiling.html)
[Performance profiling](https://docs.kanzi.com/4.1.0/en/best-practices/performance/profiling.html)
[![../_images/pluginengine96x96.png](https://docs.kanzi.com/4.1.0/en/_images/pluginengine96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/plugins/plugins-kanzi-engine.html)
[Plugins - Kanzi Engine](https://docs.kanzi.com/4.1.0/en/working-with/plugins/plugins-kanzi-engine.html)
[![../_images/pluginstudio96x96.png](https://docs.kanzi.com/4.1.0/en/_images/pluginstudio96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/plugins/plugins.html)
[Plugins - Kanzi Studio](https://docs.kanzi.com/4.1.0/en/working-with/plugins/plugins.html)
[![../_images/prefab96x96.png](https://docs.kanzi.com/4.1.0/en/_images/prefab96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/prefabs/prefabs.html)
[Prefabs](https://docs.kanzi.com/4.1.0/en/working-with/prefabs/prefabs.html)
[![../_images/preview96x96.png](https://docs.kanzi.com/4.1.0/en/_images/preview96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/preview/preview.html)
[Preview](https://docs.kanzi.com/4.1.0/en/working-with/preview/preview.html)
[![../_images/postprocessinggraph96x96.png](https://docs.kanzi.com/4.1.0/en/_images/postprocessinggraph96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/prism-graphs/prism-graphs.html)
[Prism graphs](https://docs.kanzi.com/4.1.0/en/working-with/prism-graphs/prism-graphs.html)
[![../_images/project96x96.png](https://docs.kanzi.com/4.1.0/en/_images/project96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/projects/projects.html)
[Projects](https://docs.kanzi.com/4.1.0/en/working-with/projects/projects.html)
[![../_images/propertytype96x96.png](https://docs.kanzi.com/4.1.0/en/_images/propertytype96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/property-types/property-types.html)
[Property types](https://docs.kanzi.com/4.1.0/en/working-with/property-types/property-types.html)
[![../_images/rendering96x96.png](https://docs.kanzi.com/4.1.0/en/_images/rendering96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/rendering/rendering.html)
[Rendering](https://docs.kanzi.com/4.1.0/en/working-with/rendering/rendering.html)
[![../_images/resourcefiles96x96.png](https://docs.kanzi.com/4.1.0/en/_images/resourcefiles96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/resource-files/resource-files.html)
[Resource files](https://docs.kanzi.com/4.1.0/en/working-with/resource-files/resource-files.html)
[![../_images/dictionaries96x96.png](https://docs.kanzi.com/4.1.0/en/_images/dictionaries96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/resources/resources.html)
[Resources](https://docs.kanzi.com/4.1.0/en/working-with/resources/resources.html)
[![../_images/rust96x96.png](https://docs.kanzi.com/4.1.0/en/_images/rust96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/rust/using-rust.html)
[Rust](https://docs.kanzi.com/4.1.0/en/working-with/rust/using-rust.html)
[![../_images/scene96x96.png](https://docs.kanzi.com/4.1.0/en/_images/scene96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/scenes/scenes.html)
[Scene node](https://docs.kanzi.com/4.1.0/en/working-with/scenes/scenes.html)
[![../_images/screen96x96.png](https://docs.kanzi.com/4.1.0/en/_images/screen96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/screens/screens.html)
[Screen node](https://docs.kanzi.com/4.1.0/en/working-with/screens/screens.html)
[![../_images/scrollview96x96.png](https://docs.kanzi.com/4.1.0/en/_images/scrollview96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/scroll-views/using-scroll-views.html)
[Scroll View nodes](https://docs.kanzi.com/4.1.0/en/working-with/scroll-views/using-scroll-views.html)
[![../_images/skinning96x96.png](https://docs.kanzi.com/4.1.0/en/_images/skinning96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/skinning/using-skinned-meshes.html)
[Skinning](https://docs.kanzi.com/4.1.0/en/working-with/skinning/using-skinned-meshes.html)
[![../_images/slider96x96.png](https://docs.kanzi.com/4.1.0/en/_images/slider96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/sliders/using-sliders.html)
[Slider nodes](https://docs.kanzi.com/4.1.0/en/working-with/sliders/using-sliders.html)
[![../_images/shaders.png](https://docs.kanzi.com/4.1.0/en/_images/shaders.png)](https://docs.kanzi.com/4.1.0/en/working-with/shader-graphs/shader-graphs.html)
[Shader graphs](https://docs.kanzi.com/4.1.0/en/working-with/shader-graphs/shader-graphs.html)
[![../_images/shaders.png](https://docs.kanzi.com/4.1.0/en/_images/shaders.png)](https://docs.kanzi.com/4.1.0/en/working-with/shaders/shaders.html)
[Shaders](https://docs.kanzi.com/4.1.0/en/working-with/shaders/shaders.html)
[![../_images/stack96x96.png](https://docs.kanzi.com/4.1.0/en/_images/stack96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/layouts/using-stack-layouts.html)
[Stack Layout nodes](https://docs.kanzi.com/4.1.0/en/working-with/layouts/using-stack-layouts.html)
[![../_images/statemanager96x96.png](https://docs.kanzi.com/4.1.0/en/_images/statemanager96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/state-managers/state-managers.html)
[State manager](https://docs.kanzi.com/4.1.0/en/working-with/state-managers/state-managers.html)
[![../_images/style96x96.png](https://docs.kanzi.com/4.1.0/en/_images/style96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/styles/using-styles.html)
[Styles](https://docs.kanzi.com/4.1.0/en/working-with/styles/using-styles.html)
[![../_images/tag96x96.png](https://docs.kanzi.com/4.1.0/en/_images/tag96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/tags/using-tags.html)
[Tags](https://docs.kanzi.com/4.1.0/en/working-with/tags/using-tags.html)
[![../_images/text96x96.png](https://docs.kanzi.com/4.1.0/en/_images/text96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/text/text.html)
[Text nodes](https://docs.kanzi.com/4.1.0/en/working-with/text/text.html)
[![../_images/texture96x96.png](https://docs.kanzi.com/4.1.0/en/_images/texture96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/textures/textures.html)
[Textures](https://docs.kanzi.com/4.1.0/en/working-with/textures/textures.html)
[![../_images/theme96x96.png](https://docs.kanzi.com/4.1.0/en/_images/theme96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/themes/theming-applications.html)
[Theming](https://docs.kanzi.com/4.1.0/en/working-with/themes/theming-applications.html)
[![../_images/trajectory96x96.png](https://docs.kanzi.com/4.1.0/en/_images/trajectory96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/trajectories/trajectories.html)
[Trajectories](https://docs.kanzi.com/4.1.0/en/working-with/trajectories/trajectories.html)
[![../_images/trajectorylayout96x96.png](https://docs.kanzi.com/4.1.0/en/_images/trajectorylayout96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/trajectories/using-trajectory-layouts.html)
[Trajectory Layout nodes](https://docs.kanzi.com/4.1.0/en/working-with/trajectories/using-trajectory-layouts.html)
[![../_images/triggers96x96.png](https://docs.kanzi.com/4.1.0/en/_images/triggers96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/triggers/triggers.html)
[Triggers](https://docs.kanzi.com/4.1.0/en/working-with/triggers/triggers.html)
[![../_images/versioncontrol96x96.png](https://docs.kanzi.com/4.1.0/en/_images/versioncontrol96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/version-control/version-control.html)
[Version control](https://docs.kanzi.com/4.1.0/en/working-with/version-control/version-control.html)
[![../_images/viewport96x96.png](https://docs.kanzi.com/4.1.0/en/_images/viewport96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/viewports/using-viewports.html)
[Viewport nodes](https://docs.kanzi.com/4.1.0/en/working-with/viewports/using-viewports.html)
[![../_images/workspace96x96.png](https://docs.kanzi.com/4.1.0/en/_images/workspace96x96.png)](https://docs.kanzi.com/4.1.0/en/working-with/workspaces/customizing-your-workspace.html)
[Workspace](https://docs.kanzi.com/4.1.0/en/working-with/workspaces/customizing-your-workspace.html)

<!-- NODE_END: https://docs.kanzi.com/4.1.0/en/working-with/working-with.html -->

<!-- NODE_END: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/kanzi-fundamentals.html -->
