---
title: Rendering
source: https://docs.kanzi.com/4.1.0/en/working-with/rendering/rendering.html
---

# Rendering


Use render passes to define the rendering of 3D content in your Kanzi application.

For example, in render passes you can define:

- Which Camera that render pass and its descendants use for rendering. See Setting the camera for render passes.
- What nodes the render pass renders. See Collecting nodes for rendering.
- What lights to use to light the content. See Using lights in rendering.
- What material to use to render the content. Setting materials for rendering.
- The format of the composition target. See Rendering content to composition targets.
- Post-processing effects. Creating a post-processing effect.


In a render pass prefab, you can create a hierarchy of render passes to achieve a specific rendering result.

In the Library > Rendering > Render Pass Prefabs each top-level render pass is the root of a render pass prefab.

Kanzi executes the render passes in each render pass prefab from top to bottom the way they appear in the render pass prefab in the Library. Each render pass applies its settings and renders its children. See Using render passes.

For example, the Default render pass, which is one of the render pass presets that come with Kanzi Studio, creates a basic set of render passes that first render opaque nodes and then transparent nodes. See Using the Default render pass.
## Render passes


These render passes are available in Kanzi:
### Blit render pass


Blit render pass blits one or more single textures or cubemap textures on the screen using a specific material.

See Rendering content to composition targets, Rendering multiple render passes or textures, and Creating a post-processing effect.
### Clear render pass


Clear render pass clears some or all of the buffers of the current render context.

You can set the values to which Kanzi clears the color, depth, and stencil buffer.
### Composition Target render pass


Composition Target render pass renders itself and its descendant render passes to one or more composition targets.

See Rendering content to composition targets.
### Cubemap render pass


Cubemap render pass renders itself and its child render passes to an active composition target, such as a Cubemap Render Target Texture and the Result Texture of the Cubemap render pass.

See Creating cubemap reflections.
### Draw Objects render pass


Draw Objects render pass allows you to set a Camera node to render a specific list of nodes using specific light nodes.

The Draw Objects render pass:

- By default uses the default Camera node to render all nodes in a Scene node, or the nodes passed to it by its nearest ancestor Node List render pass. See Setting the camera for render passes and Collecting nodes for rendering.
- By default renders nodes using the light nodes provided by its nearest ancestor Gather Lights render pass. See Using lights in rendering.
- Uses the rendering parameters that you set in its nearest ancestor Pipeline State render pass.
- Allows you to control frustum culling. See Controlling frustum culling.

### Draw Objects With Material render pass


Draw Objects With Material render pass works like a Draw Objects render pass but allows you to set a material that it uses to render content. See Setting materials for rendering.
### Gather Lights render pass


Gather Lights render pass allows you to collect from a list of nodes the light nodes for lighting 3D nodes in a scene.

See Using lights in rendering.
### Group render pass


Group render pass allows you to collect render passes so that you can refer to a single render pass prefab in your Viewport 2D node.

If your topmost render pass can have all your other render passes as its children, you do not need a Group render pass.
### Material Setup render pass


Material Setup render pass allows you to set properties for a material so that all successive rendering with that material uses the property values that you set in this render pass.

See Setting materials for rendering.
### Node List render pass


Node List render pass allows you to filter and hold a list of nodes that you want to render using other render passes.

See Collecting nodes for rendering.
### Pipeline State render pass


Pipeline State render pass allows you to set for its child render passes depth and stencil testing, transparency, and culling. This render pass sets the rendering state before passing the control to its descendants. After the descendant render passes of a Pipeline State render pass execute, Kanzi restores the rendering state. See Setting the cull mode, Applying a stencil to 3D content, and Rendering decals.
## Render Pass Presets

### Compose and Blit Pass


Compose and Blit Pass contains the render pass structure that enables you to blit to the screen Composition Target render passes or textures using a specific material.

See Rendering content to composition targets.
### Default render pass


Default render pass contains a basic set of render passes that first render opaque nodes and then transparent nodes.

Use the Default render pass as a starting point for your render pass tree. See Using the Default render pass.
### Render to Texture Pass


Render to Texture Pass creates the render passes and texture you need to render to a texture.

See Rendering to texture.
### Image-Based Lighting Filter Pass


Image-Based Lighting Filter Pass contains the render passes that enable you to create dynamic Environment Ambient Texture and Environment Reflection Texture cubemap textures for real-time image-based lighting. See Rendering cubemaps for dynamic image-based lighting.
