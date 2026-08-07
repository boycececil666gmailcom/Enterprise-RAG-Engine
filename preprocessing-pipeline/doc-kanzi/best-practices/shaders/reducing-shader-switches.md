---
title: Reducing shader switches
source: https://docs.kanzi.com/4.1.0/en/best-practices/shaders/reducing-shader-switches.html
---

# Reducing shader switches

Kanzi must switch shaders every time a rendered batch has a different shader compared to the previous batch. Because materials can have their own vertex and fragment shaders, in some cases your application has to switch shaders several times during the rendering of a scene.

Vertex and fragment shaders are each compiled into a shader program and are sent to the GPU whenever it needs to be used. The GPU only stores one program at a time. At least one shader switch must be made for each material in a scene. If objects are presented in an order that requires excessive switching between shader programs, the rendering can slow down.

You can see the number of shader switches (Pipeline Count) in the Kanzi Studio Preview Performance HUD. See Troubleshooting the performance of your application.

Shader switching decreases the performance of your application, so keep shader switching to a minimum. To reduce shader switches:

- Try to use the same shader as much as possible. The downside of this approach is that it can increase the uniform sending count.
- Render objects by material type to improve performance. See Rendering nodes by material type.

## Rendering nodes by material type

To render nodes by material type:

1.

In the Library press Alt and right-click Rendering > Object Sources and select Sorting Filter.
2.

In the Properties set:

  - Source to the source from where you want to collect nodes for filtering. For example, to apply your filter to all nodes in your project, select Root Object Source. You can select the output of another filter as the source from where you collect nodes for filtering.
  - Sorting Type to Material type to group the nodes by their material type. By grouping nodes by their material type you can optimize your Kanzi application, because that way Kanzi can decrease the number of shader switches.
  - Either enable or disable the Reverse Order property:

    - When enabled it reverses the current order of nodes.
    - When disabled it keeps the current order of nodes.

3.

In the Library > Rendering > Render Pass Prefabs create a Group render pass and inside it create:

  - Clear render pass
  - Gather Lights render pass and inside it a Draw Objects render pass

4.

In the Library select the Draw Objects render pass that you created and in the Properties set the Object Source property to the filter that you created or to an object source which collects the filter.
5.

In the Node Tree select the Viewport 2D node to which you want to apply the filter and in the Properties set the Render Pass Prefab property to the Group render pass whose descendant Draw Objects render pass uses as its object source the filter that you created.

Kanzi Studio renders the nodes collected by the filter.
