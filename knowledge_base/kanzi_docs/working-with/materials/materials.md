---
title: Material types and materials
source: https://docs.kanzi.com/4.1.0/en/working-with/materials/materials.html
---

# Material types and materials

Material types define the property types of a material. By adjusting material property values defined by a material type, you set the appearance of a material. Each material type has a vertex shader and a fragment shader, which set the type of properties you can use in a material.

Use materials to set the appearance of 3D nodes and Material Brush brushes.

See Using meshes and Using brushes.

In Kanzi Studio in the Library > Materials and Textures you can see the available and add new material types, materials, textures, brushes, and shaders.

In addition to material properties, in a material type you can set the properties that are used in lights. Light properties are usually defined in arrays. The number of items in a light property array specifies how many lights the material type allows. Lights are collected at runtime from lights in the active scene whose light data has any of the light properties in the currently rendered material type. Shader properties visualize the inputs of the shader parsed from the shader code. See Using the light nodes.

Kanzi Studio provides template projects that contain a default set of material types and shaders from the Kanzi Studio `Asset Library` located in `<KanziInstallation>/Studio/Asset Library`. When you create a new Kanzi Studio project you can select from different project templates based on the material types they provide:

- To start with a template that does not contain any predefined material types, select Import material types manually. You can add material types from the Kanzi Studio material library to the project when you need them, or create your own material types. See Adding a material type to your project.
- High performance vertex shaders template is intended for low precision and high performance applications. It contains vertex-based shaders. Most of the GPU specific computation, including applying lights using the Phong reflection model, is done in the vertex shader. This is a good starting point for most devices.
- High quality fragment shaders template is intended for high-precision applications. It contains pixel-shader based materials. Most of the GPU specific computation, including applying lights using the Phong reflection model, is done in the fragment shader. This offers better image quality often at the cost of performance.
- Physically based rendering template is intended for modern applications. It contains materials based on shaders that implement physically-based rendering (PBR) principles. The properties of these materials represent physical properties, such as metalness, and are therefore intuitive to control. Most of the GPU specific computation, including applying lights using a physically-based lighting model, is done in the fragment shader. This offers a more realistic rendering result in many lighting conditions.

High performance vertex shaders, High quality fragment shaders, and Physically based rendering project templates define a set of material types that are available in the project materials library, each with fragment and vertex shaders. See Shaders.

If you are not sure which set of materials to choose, select Import material types manually, and add the materials as you need them.

The type of shading used is often the first bottleneck that causes bad performance. See Shaders best practices.
## Material type bindings

Bindings in material types enable you to:

- Modify the values of shader uniforms without editing shader code. See Uniform bindings.
- Store the results of bindings into temporary variables to which you can refer in other bindings. See Temporary variable bindings.

### Uniform bindings

In a material type, vertex and fragment shaders define the uniforms and property types that you can use in that material. When rendering 3D nodes with a specific material type, uniform bindings allow Kanzi to write values to the render state and use those values for uniforms and property types.

See Using material types, Shader uniforms and Rendering.

Uniform bindings enable you to modify the values of shader uniforms used by a material type without making changes to the shader code.

For example, you can use a uniform binding for a light property type to set the render value in all Light nodes of a specific type in a scene. Kanzi uses that render value to render in the scene all 3D nodes that use the material type that has the binding. See Controlling light uniforms.

In each material type, Kanzi Studio automatically creates default bindings for the uniforms of the material type. These bindings get their values from either:

- Uniform binding functions.

To reduce memory consumption and improve performance, Kanzi provides binding functions for the most common shader uniforms. Kanzi executes every frame all bindings that use these functions.

See Uniform binding functions.

For example:

```
kzProjectionCameraWorldMatrix = getProjectionCameraWorldMatrix()

```

- Property values read from nodes or render passes.

  - Most uniform bindings get their default values from properties of the 3D nodes that are rendered. See Property bindings.

For example:

```
BlendIntensity = {./BlendIntensity}

```

  - The bindings for some common rendering properties, such as `kzProjectionMatrix`, `kzCameraMatrix`, and `kzViewport`, get their default values from properties of render passes. See Render pass properties in material type bindings.

For example, the uniform `kzViewport`, which sets the viewport position and size, is by default bound to the Rendering Viewport property of the render pass that draws the 3D nodes:

```
kzViewport = {##RenderPass/DrawObjectsRenderPass.Viewport}

```

When you add a property to a material type, Kanzi Studio creates a default uniform binding for that property type. See Adding a property to a material type.
### Temporary variable bindings

In a material type, a temporary variable binding enables you to store the result of a binding into a temporary variable. You can refer to this variable in other bindings in the same material type.

Kanzi uses property types to identify temporary variables. This enables you to:

- Refer to a temporary variable without separately specifying its data type. A property type holds information about its data type.
- Detect conflicts between temporary variables.

See Creating property types.

Kanzi executes the temporary variable bindings in a material type each time that a node which uses that material type attaches to the node tree. For example, when a temporary variable binding uses the evaluate binding function to step through a collection of values stored in a range property, Kanzi renders each node using a different value from that collection.

See Temporary variables in material type bindings.
