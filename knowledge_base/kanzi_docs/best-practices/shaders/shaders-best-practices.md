---
title: Shaders best practices
source: https://docs.kanzi.com/4.1.0/en/best-practices/shaders/shaders-best-practices.html
---

# Shaders best practices

Your application spends a considerable amount of time executing shader programs. Especially with mobile and embedded hardware, shaders can be the source of many problems, including performance bottlenecks and graphical artifacts. When used properly, shaders can help you produce amazing graphical quality and performance by distributing computation between the CPU and the GPU. You have to decide whether to perform computations in the fragment or the vertex shader.

A vertex shader of a shader program is run once for each vertex while its fragment shader is run once for each pixel. Usually there are an order of magnitude more pixels than vertices. For this reason, the best practice is to calculate as much as possible in the vertex shader and use the results in the fragment shader.

To use geometry and tessellation shaders, the hardware where you want to run your Kanzi application must support OpenGL ES 3.2 or Vulkan 1.1. Note that geometry and tessellation shaders can decrease the performance on tiled rendering architectures. For this reason, it is recommended to avoid using geometry and tessellation shaders on mobile and embedded hardware.

Some of the most common shader bottlenecks are:

- Unnecessary calculations in the fragment shaders and heavy fragment shaders. See Optimizing fragment shaders.
- 3D models with long vertex shaders. If the vertex shader is the bottleneck, reduce the number of instructions to improve performance. If the fragment shader is the bottleneck, the optimizations in the vertex shader do not affect the performance.
- Displays with a lot of fragments that require filling a lot of pixels on the screen.
- Vertices that are sent to the GPU and processed by a vertex shader. Triangle count provides a hint of vertex count drawn per frame. See Troubleshooting the performance of your application.

Kanzi Studio provides these templates for different shader profiles:

- High performance vertex shaders template is intended for low precision and high performance applications. It contains vertex-based shaders. Most of the GPU specific computation, including applying lights using the Phong reflection model, is done in the vertex shader. This is a good starting point for most devices.

The vertex-based shading offered in the High performance vertex shaders material type is a good choice for mobile GPUs, because of the lower cost of vertex-based shading.
- High quality fragment shaders template is intended for high-precision applications. It contains pixel-shader based materials. Most of the GPU specific computation, including applying lights using the Phong reflection model, is done in the fragment shader. This offers better image quality often at the cost of performance.
- Physically based rendering template is intended for modern applications. It contains materials based on shaders that implement physically-based rendering (PBR) principles. The properties of these materials represent physical properties, such as metalness, and are therefore intuitive to control. Most of the GPU specific computation, including applying lights using a physically-based lighting model, is done in the fragment shader. This offers a more realistic rendering result in many lighting conditions.

Depending on the graphics hardware and the complexity of the scene, shaders can have a big impact on application performance.

You can optimize performance by decreasing the precision for uniforms and shader inputs and outputs in shaders. Precision in shaders is specific to OpenGL ES and Vulkan.

For mobile and embedded devices, use:

- Low precision for all variables that range [-2..2].
- Medium precision for other variables that do not require the full precision of 32-bit floating point.

Shaders are material-specific. You can modify shaders directly in Kanzi Studio. See Editing shaders.

Best practices for using shaders in your Kanzi application are:

- Optimize fragment shaders by decreasing precision and moving calculations from fragments to vertices. See Optimizing fragment shaders.
- If nodes are presented in an order that requires excessive switching between shader programs, the rendering can slow down. See Reducing shader switches.
- When users run your Kanzi application in an environment with a multi-core processor, Kanzi automatically uses multiple CPU cores to load the GPU resources in the kzb files to RAM.

Kanzi enables you to configure how many cores you want your application to use. See Loading resources in parallel.
- Make sure that the shaders calculate only the amount of lights that you use. Limit the number of lights in the Scene nodes in your application to the amount that your shaders calculate.
- Use shader tools, such as PVRShaderEditor, to get comprehensive information on the performance cost of your shaders.
- Make sure there are no errors or warnings in your shaders.
- Place into separate shaders the functionality that you want to use in more than one shader and reuse that shader code. See Reusing shader code. To reuse shader code across projects without copying files, use the Kanzi shader include library. See Using the shader include library.
