---
title: Setting materials for rendering
source: https://docs.kanzi.com/4.1.0/en/working-with/rendering/rendering-materials.html
---

# Setting materials for rendering


In Kanzi you can use these render passes to set materials for rendering:

- Draw Objects With Material render pass allows you to render nodes in a Viewport 2D node with a specific material.

For example, use the Draw Objects With Material render pass to create different rendering modes. See Creating a night vision mode.
- Material Setup render pass allows you to set properties for a material so that all successive rendering with that material uses the property values that you set in this render pass.

For example, use the Material Setup render pass to set the output of a Composition Target render pass as the texture of a material. See Creating an infinity mirror.

## Creating a night vision mode


You can use the Draw Objects With Material render pass to render all nodes under a Viewport 2D node with a specific material. For example, you can create a night vision mode.

To create a night vision mode:

1.

Create the content that you want to render in night vision mode.

For example, use the Car from the Factory Content.

See Using the Factory Content assets.
2.

Create and apply the render passes that you need to render the content in night vision mode:

  1.

In the Library > Rendering press Alt and right-click Render Pass Prefabs, select Group render pass, and name it Night Vision.

You use this Group render pass prefab to collect the render passes which apply the night vision mode to your content.
  2.

In the Node Tree select the Viewport 2D node the content of which you want to render in night vision mode, and in the Properties set the Render Pass Prefab property to the Night Vision render pass prefab.

This way you set Kanzi to render the Viewport 2D node using the Night Vision render pass prefab. The Night Vision render pass prefab does not have any child render passes, which is why the Preview does not show any content.
  3.

In the Night Vision render pass prefab create:

    1.

Clear render pass

This render pass clears the depth buffer.
    2.

Gather Lights render pass

Gather Lights render pass allows you to collect from a list of nodes the light nodes for lighting 3D nodes in a scene.
    3.

In the Gather Lights render pass create a Draw Objects With Material render pass.


You can use a Draw Objects With Material render pass to render all nodes under a Viewport 2D node with a specific material that you set in the Draw Objects With Material render pass.

Because you have not yet set the Material property in the Draw Objects With Material render pass, Kanzi uses the default materials to render the content in the Viewport 2D node which uses the Night Vision render pass.

3.

Create the material that you want to use for the night vision mode.

For example, in the Library > Materials and Textures > Material Types press Alt and right-click VertexPhong, select Material, and name the material Night Vision Material.

This way you create a material which uses the VertexPhong material type.

> **Tip:** If your project does not contain the VertexPhong material type, in the Library > Materials and Textures press Alt and right-click Material Types, and select VertexPhong.
> 4.
>
> In the Library > Rendering > Render Pass Prefabs select the Draw Objects With Material render pass and in the Properties set the Material property to the material that you created in the previous step.
>
> Kanzi now renders all nodes in the Viewport 2D node, which uses the Night Vision render pass prefab, with the material that you created.
> 5.
>
> In the Properties click the  next to the Material property to open the properties of the material that you created, and set the properties of the material to achieve the look you want.
> 6.
>
> In the Library > Rendering > Render Pass Prefabs select the Clear render pass, in the Properties add the Clear Color 0 property, and set the Lightness (L) property field to 0.
>
> This way you clear the color buffer with black color to make the background of your scene black in the night vision mode.
> 7.
>
> Control the switching between the day and night vision modes.
>
> For example, create a State Manager where you define states for:
>
> - Day mode, which sets in your Viewport 2D node the Render Pass Prefab property to DefaultRenderPassPrefab.
> - Night vision mode, which sets in your Viewport 2D node the Render Pass Prefab property to the Night Vision render pass prefab.


See Creating a state manager.

Now when you switch between the states you created, Kanzi alternates between rendering your content normally and in night vision mode.

## Creating an infinity mirror


Material Setup render pass allows you to set properties for a material so that all successive rendering with that material uses the property values that you set in this render pass.

For example, you can use the Material Setup render pass to create an infinity mirror effect.

To create an infinity mirror:

1.

In the Node Tree create:

  - A Viewport 2D node which contains the 3D content that you want to mirror.

For example, use the Car from the Factory Content.

See Using the Factory Content assets.
  - A node that you use as a mirror.

For example, in the same Scene node as the content that you want to mirror, create a Plane node.

2.

Create the material that you use to render the 3D content in the mirror:

  1.

Create a textured material.

For example, in the Library > Materials and Textures > Material Types press Alt and right-click Textured, select Material, and name the material Mirror Material.
  2.

In the Node Tree select the node that you want to use as the mirror and in the Properties set the Mesh Material property to the material you created in the previous step.

3.

Render the 3D content in the mirror:

  1.

In the Library, press Alt and right-click Rendering, and select Compose and Blit Pass.

Compose and Blit Pass contains the render pass structure that enables you to blit to the screen Composition Target render passes or textures using a specific material.

The Compose and Blit Pass render pass preset contains these render passes:

    - Composition Target render pass renders itself and its descendant render passes to one or more composition targets.

      - Clear render pass clears some or all of the buffers of the current render context.

By default, the Clear render pass in the Compose and Blit Pass clears the first color buffer with transparent black color and the depth buffer with value 1.

For example, to clear the first color buffer with a different color, set the Clear Color 0 property to the color that you want to use as the background color of the content that Kanzi renders to the Composition Target render pass.
      - Gather Lights render pass collects the Light nodes in the Viewport 2D node that you set to use the Compose and Blit Pass, and passes them to its child Draw Objects render pass.

        - Draw Objects render pass named Draw Objects allows you to set a Camera node to render a specific list of nodes, to filter those nodes, and to control frustum culling. Draw Objects render pass by default renders nodes using the lights provided by its nearest ancestor Gather Lights render pass. By default the Draw Objects render pass uses the default Camera node to render all nodes in a Viewport 2D node.


    - Blit render pass blits one or more single textures or cubemap textures on the screen using a specific material.

By default, this Blit render pass draws on the screen the first color texture to which the Composition Target render pass renders its content.

  2.

In the Node Tree select the Viewport 2D node whose content you want to render in the mirror, and in the Properties set the Render Pass Prefab property to the Compose and Blit Pass.

You set Kanzi to render the Viewport 2D node using the Compose and Blit Pass.
  3.

In the Library in the Compose and Blit Pass create a second Composition Target render pass and drag the Blit render pass to that Composition Target render pass.

You use the second Composition Target render pass to render the first Composition Target render pass to a composition target.

You create two Composition Target render passes because the rendering behavior is undefined if you simultaneously write to and read from the same render pass.
  4.

In the Compose and Blit Pass create a Default render pass.

Default render pass contains a basic set of render passes that first render opaque nodes and then transparent nodes.

You use this render pass to render to the screen the content of the Viewport 2D node.
  5.

In the Compose and Blit Pass create a Material Setup render pass and in the Properties set the Material property to the material that you created earlier in this procedure.

For example, set it to Mirror Material.
  6.

In the Properties add the Texture property, from the Library drag the second Composition Target render pass to the Properties window, and drop it on the Texture property of the Material Setup render pass.

Here you set the value of the Texture property for the material that you created, so that Kanzi uses the value when rendering content using the Compose and Blit Pass. This way you set Kanzi to render the Composition Target render pass 2 in the node that uses the Mirror Material.
  7.

In the Library select the Compose and Blit Pass > Composition Target render pass > Clear render pass and in the Properties set the Clear Color 0 property to the color that you want to use as the background color of the scene in the mirror.


Kanzi now recursively renders the contents of the Viewport 2D node in the mirror.
