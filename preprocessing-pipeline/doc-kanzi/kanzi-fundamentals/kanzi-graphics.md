---
title: Kanzi graphics
source: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/kanzi-graphics.html
---

# Kanzi graphics

Kanzi graphics (kzgfx) is the render hardware interface (RHI) for Kanzi. It provides an abstraction layer that allows Kanzi to use different graphics APIs. Kanzi provides these implementations of the interface:

- An OpenGL-based backend that supports OpenGL 3.3+, OpenGL ES 3.0+, and WebGL 2.0
- A Vulkan 1.1+ backend

Most Kanzi applications do not need to use the Kanzi graphics API directly and instead use high-level concepts from the Rendering system. Use Kanzi graphics directly only to accomplish advanced use cases like compute or manual rendering.

The Kanzi graphics API has these major components:

- Graphics objects represent an entity within the interface, such as a buffer, image, or shader.
- Commands operate on the graphics objects and are collected into command buffers for deferred execution. Operations like copy, draw, and present are typical commands.

The shader programs used by Kanzi graphics are required to provide reflection information in addition to the raw shader source. For most use cases, Kanzi Studio does this automatically when exporting a project, but you can also do this with the Kanzi Shader Compiler library or through manual construction.

The Kanzi graphics API is safe to call from any thread. This is in contrast to the OpenGL family of APIs which require all calls to be made within a thread specific context. The Kanzi graphics OpenGL backend provides a rendering thread to meet this requirement of the API.

Keep in mind that you cannot use a specific graphics API, such as OpenGL or Vulkan, directly from a custom Kanzi application or plugin. Use the Kanzi graphics API instead.

In addition to the backends, Kanzi graphics allows you to configure multiple layers that allow additional behavior independent of the backend. Each Kanzi graphics function call is first routed through the list of layers before being processed by the backend. Kanzi provides these layers:

- Validation layer reports violations of expected API usage.
- Statistics layer contains a set of statistics about Kanzi graphics.

## Graphics objects

You can create graphics objects using the relevant create info object and the `gfx::create` function. Graphics objects are represented through a type-specific handle guard object. The guards are reference counted so that when all references are destroyed, the object itself is queued for destruction.

Once created, the definition of objects is immutable. For example, you cannot resize a buffer or an image. Instead you must create a new object with the new properties.

Object |

Creation struct |

Description |

Buffer |

`gfx::BufferCreateInfo` |

Represents a block of memory that can be in CPU or GPU memory. Typically used to store uniforms, vertex or index data, and other generic usage. |

Image |

`gfx::ImageCreateInfo` |

Represents an image object that can be sampled from a shader. |

Frame Buffer |

`gfx::FrameBufferCreateInfo` |

Represents an on screen or offscreen frame buffer that can be used as a render target. |

Vertex Input State |

`gfx::VertexInputStateCreateInfo` |

Represents a layout for vertex data stored in a buffer. |

Depth Stencil State |

`gfx::DepthStencilStateCreateInfo` |

Represents a set of configuration options about how a depth or stencil image is used. |

Blend State |

`gfx::BlendStateCreateInfo` |

Represents a set of configuration options about how to blend the output of a render pipeline. |

Raster State |

`gfx::RasterStateCreateInfo` |

Represents a set of configuration options about how the rasterizer behaves, such as fill mode, cull mode, and triangle topology. |

Sampler |

`gfx::SamplerCreateInfo` |

Represents a sampler object to configure how an image is sampled by a shader. |

Render Resource Set |

`gfx::RenderResourceSetCreateInfo` |

Represents a set of resources such as buffers, images, and samplers that are required by a render pipeline. |

Compute Resource Set |

`gfx::ComputeResourceSetCreateInfo` |

Represents a set of resources such as buffers and images that are required by a compute pipeline. |

Shader |

`gfx::ShaderCreateInfo` |

Represents a shader program. This could be a vertex, fragment, tesselation, geometry, or compute shader. These are combined with other state objects to form a complete render or compute pipeline. |

Compute Pipeline |

`gfx::ComputePipelineCreateInfo` |

Represents a compute program. |

Render Pipeline |

`gfx::RenderPipelineCreateInfo` |

Represents a render program that contains a complete set of shaders, a depth stencil state, a blend state, a raster state, a vertex input state, and a description of the render target. |

Render Pass |

`gfx::RenderPassCreateInfo` |

Represents a set of render targets and how those targets are loaded or stored in memory. |

Command Buffer |

`gfx::CommandBufferCreateInfo` |

Represents a region in CPU memory that contains Kanzi graphics commands for execution by the Kanzi graphics API. |

GPU Fence |

`gfx::GpuFenceCreateInfo` |

Represents a syncronization object that can be used to allow a thread to wait until a specific portion of a command buffer has been completed. |
## Commands

Commands are recorded in command buffers, and executed with the `gfx::processCommands` function. The loaded backend asynchronously handles the execution of commands.

Command |

Description |

`gfx::CopyBufferCommand` |

Copies memory from a source buffer to a destination buffer. |

`gfx::CopyBufferToImageCommand` |

Copies memory from a source buffer to a destination image. |

`gfx::CopyImageCommand` |

Copies contents from a source image to a destination image. |

`gfx::CopyImageToBufferCommand` |

Copies contents from a source image to a destination image. |

`gfx::CopySurfaceToBufferCommand` |

Copies contents from an on screen frame buffer to a destination buffer. |

`gfx::BeginRenderPassCommand` |

Starts rendering to a specified render pass. |

`gfx::EndRenderPassCommand` |

Ends rendering from the previous render pass. |

`gfx::BeginRenderPipelineCommand` |

Attaches a render pipeline for usage by future draw commands. |

`gfx::EndRenderPipelineCommand` |

Ends the usage of the previous render pipeline. |

`gfx::ConstantDataCommand` |

Updates constant uniform data for use by following draw commands. |

`gfx::DrawCommand` |

Draws a number of triangles or instances based on the currently set resources. |

`gfx::DrawIndirectCommand` |

Issues an indirect draw based on the contents of a buffer. |

`gfx::BeginComputePipelineCommand` |

Attaches a compute pipeline for use by future dispatch commands. |

`gfx::EndComputePipelineCommand` |

Ends the usage of the previous compute pipeline. |

`gfx::DispatchCommand` |

Dispatches a compute operation with the currently set resources. |

`gfx::DispatchIndirectCommand` |

Issues an indirect dispatch based on the contents of a buffer. |

`gfx::PresentCommand` |

Tells the platform layer to present an on screen surface to the screen. |

`gfx::SignalGpuFenceCommand` |

Signals a GPU Fence object. |

`gfx::ResolveMultisampleImageCommand` |

Explicitly resolves a multisampled image. |

`gfx::GenerateMipmapsCommand` |

Generates the mipmaps for an image. |

`gfx::SetViewportCommand` |

Sets the active viewport for future rendering operaions. |

`gfx::SetScissorCommand` |

Sets the active scissor for future rendering operaions. |

`gfx::ClearCommand` |

Clears the render targets from the current render pass. |

`gfx::SetLineWidthCommand` |

Sets the line width when using the line based rasterization option. |

`gfx::BindVertexInputCommand` |

Binds a set of vertex buffers and an optional index buffer. |

`gfx::SetUniformOffsetCommand` |

Sets the offset to be used within a uniform buffer for the following operations. |

`gfx::BindRenderResourceSetCommand` |

Binds a set of Render Resource Sets for future rendering operations. |

`gfx::BindComputeResourceSetCommand` |

Binds a set of Compute Resource Sets for future compute operations. |

`gfx::SubroutineCommand` |

Allows a command buffer to call a second command buffer before execution returns to the next command. |
