---
title: Using the Page and Page Host nodes
source: https://docs.kanzi.com/4.1.0/en/working-with/pages/using-pages.html
---

# Using the Page and Page Host nodes
**Note:** The Page and Page Host nodes are deprecated. Use the Activity and Activity Host nodes to build navigable UIs for your application. See Activities.
Use the Page nodes to create the structure of the user interface in your application, and the Page Host nodes to manage navigation requests and transitions between Page nodes under a Page Host node. For example, you can use Page and Page Host nodes to create different parts of the user interface in your Kanzi application, such as Page Host nodes Home, Media, Navigation, or Settings screens, each having their own hierarchy of Page and Page Host nodes.
You can nest Page Host nodes to create the structure of an application user interface. For example, you can have one Page Host node managing the root-level navigation in the application user interface, such as transitions between the Home, Media, Navigation, and Settings, and add to it child Page Host nodes, each of which manages its own hierarchy of Page nodes, such as the Page nodes of the Media Page Host node.
## Activation of Page and Page Host nodes

When a Page node is active all its ancestor Page and Page Host nodes are active too. When a Page or a Page Host node is active all its content and content of all its ancestor Page and Page Host nodes is visible and users can interact with it. In a simple use case only one Page node in a hierarchy is active. However, you can build a complex structure by activating more than one Page or Page Host node in a hierarchy at the same time. To achieve this enable the Keep Active property on all Page and Page Host nodes which you want to automatically activate. Such nodes become automatically active when their parent Page or Page Host node is active.
### Activation tracking

Page Host nodes keep track of the currently active Page or Page Host node within their scope. When you activate a Page Host node, that Page Host node automatically activates the currently active Page or Page Host node in its scope. This allows the Page Host node to remember and restore its state during activation to the state before it was deactivated.
## Navigation between Page and Page Host nodes

Page Host nodes handle the navigation and transitions between Page nodes. For this reason you must place a Page Host node as an ancestor of a Page node tree hierarchy. To navigate between Page nodes request the navigation system to navigate to the selected page. When you navigate to a Page node, Kanzi transitions the node to a visible (activated) state and the contents of the node become visible to the user. When you navigate away from a Page node, Kanzi transitions the node to an invisible (deactivated) state and the contents of the node are no longer visible to the user. Kanzi supports both animated (over-time) and instant (immediate) transitions between Page nodes. See Setting transitions between Page nodes.
### The role of Page Host nodes in navigation

When you set a Page Host node as an ancestor of a Page node, that Page Host node listens for navigation requests from its descendant Page nodes. When a Page Host node receives a navigation request, it starts the navigation process to the Page node which dispatched the message. The navigation process involves resolving the route from the currently active Page or Page Host node to the target Page or Page Host node, and then performing transitions between Page nodes in the navigation route until the target Page or Page Host node is activated. Each Page Host node manages the navigation within its own scope and does not interfere with other Page Host nodes.
### Navigating between subpages

Page Host nodes contain the functionality to navigate between the next and previous Page and Page Host nodes within their scope. For example, this allows you to build support for navigation using key input. By enabling the Loop Subpages property you can further configure this functionality to set whether you want a Page Host node to loop from the last to the first or the first to the last Page node when navigating to the next and the previous Page and Page Host.
## Creating application structure using the Page and Page Host nodes

Use the Pages window to create and manage your application structure.

To create application structure using the Pages window:

1.

In the Pages window move your mouse pointer over the RootPage and click  twice to create two Page nodes under the RootPage node.

When you create Page nodes in the Pages, you can see the same Page nodes in the Node Tree too.
**Tip:** To pan and zoom in the Pages window, use these shortcuts:
|
Action |
Shortcut |
|
Pan |
- Click and drag the middle mouse button.
- Press the Space key, and click and drag the left mouse button.
|
|
Zoom |
- Scroll the mouse wheel.
- Press the Shift and Alt keys, and click and drag the left mouse button.
|
2.
In the Pages double-click the names of the Page nodes you created in the previous step and rename them to Applications and Settings.
3.
In the Pages right-click the Applications and Settings nodes and select Convert to Page Host.
Use a Page Host node to group other Page Host and Page nodes. The main difference between the Page and Page Host nodes is that the Page Host node manages navigation requests and transitions in its tree.
4.
In the Pages move your mouse pointer over the Page Host node Applications and at the bottom of that node click  three times to create three child Page nodes under the Applications node, and name them Home, Media, and Car.
Each of these Page nodes holds the content for their application. For prototyping purposes in this tutorial you add only images of these applications. However, when you move your application from the prototype phase to the development phase, replace the placeholders with the content of these applications.
Tip
To see the entire structure of Page and Page Host nodes in your application, in the Pages window click .
5.
In the Assets, import the content that you want to show in each Page node.
6.
From the Assets drag to the Pages window the content that you imported.
For example, drag:
- Home_Page texture to the Home node
- Media_Page texture to the Media node
- Car_Page texture to the Car node

When you drop an image from the Assets on a Page or a Page Host node in the Pages, Kanzi Studio creates an Image node with the image that you dropped.
**Tip:** When you click any Page or Page Host node in the Pages window, Kanzi transitions to that node and you can see the transition in the Preview.
7.
In the Pages click each Page. In the Preview you can see the Push transition between the Page nodes.
Tip
When you want to see in the Preview only the content of a selected Page or Page Host node, double-click that node in the Pages and Kanzi Studio opens it in its own tab in the Preview.

## Setting the appearance of Page and Page Host nodes

To set the appearance of 2D nodes:

- You can fill 2D nodes with a solid color, a texture, or a material. See Adjusting the appearance of 2D nodes.
- You can apply a post-processing effect to a 2D node. See Effects for 2D nodes.
- You can rotate a 2D node around all three axes to create a 3D perspective effect. See Creating a 3D perspective effect for 2D nodes.
- You can apply custom rendering to 2D nodes to create post-processing effects. See Applying custom rendering to 2D nodes.
- You can render a 2D node as pixel-perfect. See Rendering pixel-perfect 2D nodes.

## Using the Page and Page Host nodes in the API

To transition to the selected Page node:

```
// Look up child page in the scope of Page host.
PageSharedPtr subPage = host->lookupNode<Page>(path);
// Request animated transition to given page.
subPage->navigate();

```

To transition instantly to the selected Page node:

```
// Make immediate transition, without playing an animation.
subPage->navigate(true);

```

To get the currently active Page or Page Host descendant node:

```
// Retrieve currently active subpage.
PageSharedPtr currentSubPage = host->getDefaultChild();

```

To transition in a Page Host node from the current Page node to the next Page node:

```
// Request animated transition from currently active page to next subpage.
PageHost::NavigateNextMessageArguments args;
host->dispatchMessage(PageHost::NavigateNextMessage, args);

```

For details, see the `PageHost` and `Page` classes.
## Page property types and messages

For a list of the available property types and messages for the Page node, see Page (deprecated).
## Page Host property types and messages

For a list of the available property types and messages for the Page Host node, see Page Host (deprecated).
