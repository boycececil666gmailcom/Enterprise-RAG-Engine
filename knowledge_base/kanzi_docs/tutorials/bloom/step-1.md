---
title: Step 1 - Render the car and headlights
source: https://docs.kanzi.com/4.1.0/en/tutorials/bloom/step-1.html
---

# Step 1 - Render the car and headlights


In this step of the tutorial, you create the render passes that you need to render the car and the headlights separately.
## Get the tutorial


To get the tutorial, in the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Bloom tutorial, click .

Kanzi Studio downloads the tutorial to the `<KanziWorkspace>/Tutorials` directory. You can find:

- The tutorial assets in the `<KanziWorkspace>/Tutorials/Bloom/Assets` directory.
- The tutorial starting point project in the `<KanziWorkspace>/Tutorials/Bloom/Start` directory.
- The completed tutorial in the `<KanziWorkspace>/Tutorials/Bloom/Completed` directory.

## Render the scene


In this section, you create the render passes to render the entire scene.

To render the scene:

1.

In the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Bloom tutorial, click Open and select Start project.
2.

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

3.

In the Library > Rendering > Render Pass Prefabs, select the Compose and Blit Pass render pass prefab, press the F2 key, and rename it to Bloom.

You use this render pass prefab to gather several render passes that you create in this procedure which, when combined, render the car and apply the bloom effect to the headlights.
4.

In the Library > Rendering > Render Pass Prefabs > Bloom render pass prefab, rename:

  - Composition Target render pass to Render Scene

You use this render pass to render the content of the Viewport 2D node Car to a composition target that you later use as input for the render pass to pick only the headlights.
  - Blit render pass to Show Scene

You use this render pass to draw on the screen the Render Scene render pass that renders the content of the Viewport 2D node Car.

5.

In the Node Tree, select the RootNode > Scroll View 2D > Car node. In the Properties, add the Render Pass Prefab property, and set it to Bloom.

Kanzi Studio renders the Viewport 2D node Car using the Bloom render pass prefab.
6.

To apply anti-aliasing to the car, in the Library, select the Render Scene render pass, in the Properties, add the Multisample Level property, and set it to the number of anti-aliasing samples that you want to use.

For example, set it to 4.

See the documentation of the device on which you want to run your Kanzi application for supported values, because the number of anti-aliasing samples depends on the device. If you set the Multisample Level property to a value that your device does not support, Kanzi Engine clamps the value to the largest value supported by the device driver.

## Render the headlights


In this section, you create the render passes and material that you need to render only the car headlights to which you later apply the bloom effect.

To render the headlights:

1.

Select File > Import > Import Project Item(s). Go to `<KanziWorkspace>/Tutorials/Bloom/Assets` and select the `BloomThresholdMaterial.kzexport` file.

Kanzi Studio adds the BloomThreshold material type and the BloomThresholdMaterial material that supports rendering only those regions that are brighter than a specific threshold value.

The fragment shader of the BloomThreshold material type:

  - Maps the color values less than or equal to a threshold value to 0.
  - Maps the color values greater than a threshold value to a cubic equation approaching 1 when the color value approaches 1.

2.

In the Library > Rendering > Render Pass Prefabs > Bloom render pass prefab, create a Group render pass and name it Render Bloom.
3.

In the Render Bloom render pass, create a Blit render pass and name it Blit Bloom Threshold. From the Library, drag the Render Scene render pass to the Properties window, and drop it on the Texture 0 property of the Blit Bloom Threshold render pass.

You set the Blit Bloom Threshold render pass to draw to the screen the texture that the Render Scene render pass creates from the content that it renders.
4.

In the Properties, add and set:

  - Material to BloomThresholdMaterial
  - Material Properties > Threshold to 0.9


You use this render pass to draw to the screen only those regions of the car node that are brighter than the value of the Threshold property. Later you apply a Gaussian blur to these regions to create the bloom effect.
5.

In the Library in the Render Bloom render pass, create a Composition Target render pass and name it Bloom Threshold. Drag the Blit Bloom Threshold render pass to the Bloom Threshold render pass.

You use the Bloom Threshold render pass to render the Blit Bloom Threshold render pass to a composition target, which you later use as input to the render passes that apply the bloom effect. Because Kanzi renders the Blit Bloom Threshold render pass to a composition target, the Preview does not show it.


Introduction Next step
