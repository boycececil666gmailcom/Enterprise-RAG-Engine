---
title: Using Kanzi Studio render pass presets
source: https://docs.kanzi.com/4.1.0/en/working-with/rendering/using-render-pass-templates.html
---

# Using Kanzi Studio render pass presets


Use render passes to define the rendering of 3D content in your Kanzi application.

To help you get started, Kanzi Studio comes with these render pass presets:

- Default render pass contains a basic set of render passes that first render opaque nodes and then transparent nodes.

See Using the Default render pass.
- Render to Texture Pass contains the render passes that enable you to render to a texture. See Rendering to texture.
- Compose and Blit Pass contains the render pass structure that enables you to blit to the screen Composition Target render passes or textures using a specific material.

See Rendering content to composition targets
- Image-Based Lighting Filter Pass contains the render passes that enable you to create dynamic Environment Ambient Texture and Environment Reflection Texture cubemap textures for real-time image-based lighting.

See Rendering cubemaps for dynamic image-based lighting.

## Using the Default render pass


Use the Default render pass preset to create a basic set of render passes you need to get started.

To use the Default render pass:

1.

In the Library > Rendering press Alt and right-click Render Pass Prefabs and select Default render pass.

Kanzi Studio creates in the Library > Rendering the filters and render passes it needs to first render opaque nodes and then transparent nodes:

  - In Object Sources these Tag Filter filters:

    - Opaque picks the nodes that do not have the Transparent tag.
    - Transparent picks the nodes that have the Transparent tag.

  - In Render Pass Prefabs a Group render pass named Default render pass and inside it:

    - Clear render pass clears some or all of the buffers of the current render context.

By default the Clear render pass in the Default render pass clears the depth buffer.
    - Gather Lights render pass collects the Light nodes in the Viewport 2D node that you set to use the Default render pass, and passes them to its child Draw Objects render passes.

      - Draw Objects render pass named Draw Objects Opaque renders the nodes picked by the Opaque filter.

Draw Objects render pass allows you to set a Camera node to render a specific list of nodes, to filter those nodes, and to control frustum culling. Draw Objects render pass by default renders nodes using the lights provided by its nearest ancestor Gather Lights render pass.
      - Draw Objects render pass named Draw Objects Transparent renders the nodes picked by the Transparent filter.


2.

In the Node Tree select the Viewport 2D node whose content you want to render, and in the Properties set the Render Pass Prefab property to the Default render pass you created.

Kanzi Studio renders the Viewport 2D node using the Default render pass.
3.

(Optional) If your Viewport 2D node contains transparent nodes, in the Node Tree select the nodes, in the Properties next to the Tags property click the Tags button, and select Transparent.

This way you set the Default render pass to first render transparent nodes and then opaque nodes.
4.

(Optional) To set the background of the Viewport 2D node the content of which you want to render, in the Default render pass you created select the Clear render pass and in the Properties add and set the Clear Color 0 property.

## Rendering to texture


Use the Render to Texture Pass preset to create the render passes that you need to render content to a texture.

To use the Render to Texture Pass:

1.

In the Library > Rendering press Alt and right-click Render Pass Prefabs and select Render to Texture Pass.

Kanzi Studio creates in the Library:

  - In Materials and Textures > Textures a Render Target Texture
  - In Rendering > Render Pass Prefabs a Composition Target render pass named Render to Texture Pass, which renders itself to the Render Target Texture resource, and inside it:
  - Clear render pass clears some or all of the buffers of the current render context.

By default the Clear render pass in the Render to Texture Pass clears the first color buffer with transparent black color and the depth buffer with value 1.
  - Gather Lights render pass collects the Light nodes in the Viewport 2D node that you set to use the Render to Texture Pass, and passes them to its child Draw Objects render pass.

    - Draw Objects render pass named Draw Objects allows you to set a Camera node to render a specific list of nodes, to filter those nodes, and to control frustum culling. Draw Objects render pass by default renders nodes using the lights provided by its nearest ancestor Gather Lights render pass. By default the Draw Objects render pass uses the default Camera node to render all nodes in a Viewport 2D node.


2.

In the Node Tree select the Viewport 2D node whose content you want to render to a texture, and in the Properties set the Render Pass Prefab property to the Render to Texture Pass you created.

Kanzi Studio renders the Viewport 2D node using the Render to Texture Pass.
3.

Apply the Render Target Texture you created in the first step to a node where you want to show the content of the Viewport 2D node that you selected in the previous step.

For example:

  1.

In the Node Tree, press Alt and right-click and select Image.
  2.

In the Node Tree, select the Image node. In the Properties, set the Image property to the Render Target Texture that you want to show in the Image node.


## Rendering cubemaps for dynamic image-based lighting


Use the Image-Based Lighting Filter Pass preset to create dynamic cubemap textures for real-time image-based lighting. You can use this preset only as part of a render pass tree that renders content of a scene and you cannot use it directly in a Viewport 2D node.

Image-Based Lighting Filter Pass uses a Cubemap render pass to capture an environment map. See Creating cubemap reflections.

To render cubemaps for dynamic image-based lighting:

1.

Create a skybox:

  1.

In the Library > Materials and Textures, press Alt and right-click Material Types, and select CubemapSkybox.

Kanzi Studio creates in the Library > Materials and Textures the CubemapSkybox material type and CubemapSkyboxMaterial, which supports showing a cubemap texture as a skybox.
  2.

Import an HDR image that you want to use for the skybox. When importing the image, set Kanzi Studio to create only environment cubemap texture.

For best results, use a high dynamic range (HDR) pixel format, such as the R16G16B16A16_SFLOAT.
  3.

In the Library, select the CubemapSkyboxMaterial material. In the Properties, set the TextureCube property to the cubemap texture that you imported.
  4.

Create a Box or Sphere node that you use to render the skybox. In the Properties, set:

    - Mesh Material to CubemapSkyboxMaterial
    - The size of the node so that it is large enough to fit the content that you want to show inside it:

      - For a Box, set the Width, Height, and Depth properties.
      - For a Sphere, set the Radius property.

    - Generate Mesh Inside Out to enabled

When this property is enabled, Kanzi renders the cubemap texture inside the mesh.


2.

Create content on which you want to show dynamic reflections with image-based lighting:

  1.

In the Library > Materials and Textures, press Alt and right-click Material Types, and select PhysicallyBased.

Kanzi Studio creates in the Library > Materials and Textures the PhysicallyBased material type and PhysicallyBasedMaterial.
  2.

In the Library > Materials and Textures > Material Types, select PhysicallyBased, and press Ctrl D.

You duplicate the material type because you later use a variation of the same material type for the content that moves in the environment and whose reflection you want to dynamically show.
  3.

Rename the duplicated content:

    - Material type to PhysicallyBased Image-Based Lighting
    - Material to PhysicallyBased Image-Based Lighting Material

  4.

Create a node in which you want to show reflection.

For example, create a Sphere node. In the Properties, add and set:

    - Mesh Material to PhysicallyBased Image-Based Lighting Material
    - Material > Roughness Factor to 0.2


3.

Create the render pass tree that renders the environment and the content:

  1.

In the Library > Rendering, press Alt and right-click Render Pass Prefabs, and select Group render pass.
  2.

In the Group render pass create:

    1.

Cubemap render pass
    2.

Default render pass


4.

In the Node Tree select the Viewport 2D node. In the Properties set the Render Pass Prefab to the Group render pass.
5.

Adjust the Cubemap render pass:

  1.

In the Node Tree press Alt and right-click the Scene and select Camera and name it Cubemap render pass Camera.

You use this camera only in the Cubemap render pass.
  2.

In the Cubemap render pass set:

    - Override Camera to the cubemap render pass camera
    - Resolution to 256

The higher the value, the higher the rendering quality.
    - Pixel Format to R16G16B16A16_FLOAT
    - Mipmap Mode to Linear

You use Linear because Nearest returns a pixelated result.

  3.

In the Cubemap render pass:

    1.

Create a Clear render pass, and add the Clear Color 0 property.
    2.

Create a Gather Lights render pass and under it a Draw Objects render pass.


6.

Select the content to render in the Cubemap render pass:

  1.

In the Node Tree select the Box that you use for the skybox. In the Properties set Tag to CubemapContent.
  2.

In the Library > Rendering press Alt and right-click Object Sources, select Tag Filter, and name it Cubemap Content.
  3.

In the Properties set the Included Tags to the CubemapContent tag.
  4.

In the Draw Objects render pass, set the Object Source property to the Cubemap Content tag filter.

7.

Create and adjust an Image-Based Lighting Filter Pass:

  1.

In the Library > Rendering press Alt and right-click Render Pass Prefabs and select Image-Based Lighting Filter Pass.

Kanzi Studio creates in the Library:

    - In Materials and Textures > Textures these Cubemap Render Target Textures:

      - Environment Ambient Texture as irradiance texture for diffuse lighting
      - Environment Reflection Texture as reflection texture for reflective lighting


To learn how to use the resulting cubemap textures in your project that uses Physically-Based Rendering materials, see Using image-based lighting cubemap textures.
    - In Rendering > Render Pass Prefabs a Group render pass named Image-Based Lighting Filter Pass and contains these render passes:

      -  Composition Target render pass named Environment Ambient Kernel Pass, which creates and renders to a 2D lookup texture. This pass is executed once during startup. The result is used by the Environment Ambient Texture Filter Pass.

        - Blit render pass named Generate Environment Ambient Kernel Pass, which renders the 2D lookup texture.

      -  Composition Target render pass named Environment Reflection Kernel Pass, which renders a 2D lookup texture. This pass is executed once during startup. The result is used by the Environment Reflection Texture Filter Pass.

        - Blit render pass named Generate Environment Reflection Kernel Pass, which renders the 2D lookup texture.

      -  Cubemap Target render pass named Environment Ambient Texture Filter Pass, which renders to the Environment Ambient Texture cubemap texture.

        - Blit render pass named Filter Pass, which renders the final Environment Ambient Texture.

      -  Cubemap Target render pass named Environment Reflection Texture Filter Pass, which renders to the Environment Reflection Texture cubemap texture and uses a mipmap material to render different roughness values as prefiltered mipmaps.

        - Blit render pass named Blit Base Level Pass, which renders the base mipmap level of Environment Reflection Texture.


  2.

Drag the Image-Based Lighting Filter Pass to the Group render pass and place it between the Cubemap render pass and Default render pass.
  3.

Select the instance of the Image-Based Lighting Filter Pass, in the Properties click Add Binding, and in the Binding Editor:

    - Set Property to the Cubemap render pass Result Texture property of the Image-Based Lighting render pass.
    - In the Library > Rendering > Render Pass Prefabs select the Cubemap render pass and from the Properties drag the Result Texture to the Binding Editor and drop it on the Expression editor.


Click Save.
  4.

In the Library > Materials and Textures > Material Types, select PhysicallyBased Image-Based Lighting material type. In the Properties in the Preprocessor Defines set the KANZI_SHADER_USE_LIGHT_IMAGE_BASED key to 1 and click Sync with Uniforms.
  5.

In the Node Tree select the Scene node. In the Properties add and set:

    - Material > Environment Ambient Texture to Environment Ambient Render Target Texture
    - Material > Environment Reflection Texture to Environment Reflection Render Target Texture


Image-Based Lighting Filter Pass creates and dynamically updates these textures.

8.

Add the content that you want to see dynamically reflected.

For example:

  1.

In the Node Tree create an Empty Node 3D with a Sphere.
  2.

Select the Empty Node 3D and in the Properties add and set:

    - Tag to CubemapContent
    - Render Transformation Translation X to 3


This way Kanzi renders the node and its child nodes as part of the environment and you move it away from the reflective surface.
  3.

Select the Sphere and in the Properties set Mesh Material to PhysicallyBasedMaterial.
  4.

In the Library > Materials and Textures > Materials, select the PhysicallyBasedMaterial. In the Properties set:

    - Base Color Factor to white
    - Emissive Factor to white and high intensity

  5.

In the Library > Materials and Textures > Material Types, select the PhysicallyBased. In the Properties disable KANZI_SHADER_TONEMAP_REINHARD and click Sync with Uniforms.

This way you disable tonemapping.

9.

To change the quality of the reflection, adjust the Environment Ambient Texture by setting the Ambient Sample Count. This way you adjust the resolution of that cubemap texture. Lower resolution decreases the quality, but can improve performance.

In the Image-Based Lighting Filter Pass add and set Reflection Sample Count Minimum and Reflection Sample Count Maximum. Larger sample count increases the quality but decreases the performance.

For example, set both properties to 1024.

These properties control the Environment Reflection Texture sample count:

  - Reflection Sample Count Minimum is the sample count for the first mipmap level after the base level. It requires the lowest amount of samples because of the lower roughness associated with it.
  - Reflection Sample Count Progression controls how the sample count increases from the Reflection Sample Count Minimum. Every mipmap level after the first after base level increases the sample count by this value multiplied by \(2^{mipmap - 1} - 1\).
  - Reflection Sample Count Maximum limits the sample count progression to this value.


For example, if the minimum, progression and maximum are 32, 32, and 128 respectively, the sample count for:

  - The first mipmap level after the base level is 32
  - The second mipmap level is 64
  - The third mipmap level is 128
  - The fourth mipmap level is 128


The sample count does not increase after the fourth mipmap level.


When you move the object that you created to be reflected, its reflection moves accordingly.
