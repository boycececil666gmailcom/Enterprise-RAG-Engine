---
title: Kanzi 4.1.0 migration guide
source: https://docs.kanzi.com/4.1.0/en/release-notes/kanzi-4.0/kanzi-4.1.0-migration-guide.html
---

# Kanzi 4.1.0 migration guide

Use this migration guide to update Kanzi applications from Kanzi 4.0.0 to Kanzi 4.1.0.
## Project and plugin template structure changes

If you are migrating from Kanzi 3.9 to Kanzi 4.1.0, the project and plugin template structure changed substantially between Kanzi 3.9 and Kanzi 4. The surrounding build structure (CMake files, build scripts, platform configurations, and plugin build setup) does not migrate automatically when you apply the API changes in this guide. For a step-by-step guide to migrating the build structure, see Migrating projects from Kanzi 3.9 to Kanzi 4.
## Changes to property types

Creating dynamic property types with identical names but conflicting settings no longer immediately throws an error. Kanzi Engine will first try to recover by keeping the settings from the initial dynamic property type. The newly created property type is discarded.

Recovery is not possible if: - The newly created `PropertyType` has a different data type than an existing property type with the same name. - You are creating the property types in code using static `PropertyType<DataType>` objects.

These situations will still throw an error. The recovery is intended for property types loaded from `.kzb` files.

Every discrepancy is reported as warning in the logs.

Changes related to property types have the following other consequences:

- `AbstractRange` interface now has a new function `virtual bool equalsOverride(const AbstractRange& other) const` that must be implemented by inheriting ranges.

If the user declares a new type for use with `TypedValueRange<T>`, they must implement `template <> kanzi::detail::propertyDataValueEquals(const T&, const T&)` for that type.
- Elementary Kanzi data types now each have an associated `to_string()` function in `kanzi::` namespace.

## Changes to the build system

- Minimum CMake version requirement was raised to 3.25.

In Android projects, we recommend setting the CMake version used by Gradle to 3.30.5, as this is the lowest compatible version provided by the Android SDK. Alternatively, you can add your custom CMake to PATH environment variable. To specify Cmake version in Gradle, update the `Application/configs/platforms/android_gradle/kanzinative/build.gradle` file as following:

```
android {
  externalNativeBuild {
    cmake {
      ---------------
      version '3.30.5'
    }
  }
}

```

- The `KANZI_ROOT` CMake variable is renamed to `Kanzi_ROOT` to comply with [CMake policy CMP0144](https://cmake.org/cmake/help/latest/policy/CMP0144.html), which requires that the `<PackageName>_ROOT` hint variable match the casing used in the `find_package()` call.

If you pass `-DKANZI_ROOT=<path>` on the CMake command line, set `KANZI_ROOT` in your environment, or reference `KANZI_ROOT` in your `CMakeLists.txt`, rename it to `Kanzi_ROOT`:

Kanzi 4.0 |

Kanzi 4.1 |

`-DKANZI_ROOT=<path>` |

`-DKanzi_ROOT=<path>` |

`set(KANZI_ROOT <path>)` |

`set(Kanzi_ROOT <path>)` |

`$ENV{KANZI_ROOT}` |

`$ENV{Kanzi_ROOT}` |

## Changes to the Renderer API

- `GPUBuffer` is now derived from `GPUResource` and can be used as a property value in Resource property types.

Many functions were removed from GPUResource, notably `setData()` and `setSubData()`. To update a GPUResourceâs gpu-side content, use `gfx` commands to either map the buffer by its handle or allocate a staging buffer and copy it. `kanzi::CommandRecorder::updateBuffer()` can be used as well.

`updateGPUBufferData` has also been added and can be used for easily updating buffers. Internally it calls `kanzi::CommandRecorder::updateBuffer()`.

`setGPUBufferData` has also been added and can be used for easily updating a `GPUBuffer` with whole new data, regardless of the size of the previous buffer. Internally it uses CommandRecorder for updating buffer contents.
- `RenderState::HandleType` is now `RenderStateHandle`. Its `invalid` state is no longer `-1`. Use `RenderStateHandle::Invalid` instead.
- `RenderPass::CameraSettings::initializeFromLight` Function signature changed.

Removed `Renderer` reference and added `RenderPass` reference to support automated directional shadow projection fitting.
- `kanzi::BindingRenderValueLookupContext` is renamed to `BindingGraphicsEntryLookupContext`.

Kanzi 4.0 |

Kanzi 4.1 |

`BindingRenderValueLookupContext` |

`BindingGraphicsEntryLookupContext` |

## Changes to Mesh::CreateInfo and the vertex helper API

`Mesh::CreateInfo` was reshaped so that vertex data is owned per attribute rather than as a single interleaved blob. Several free helpers and one Mesh accessor were removed.

- `Mesh::CreateInfo::vertexData` and `Mesh::CreateInfo::vertexBufferHandle` were removed. Source vertex data and any pre-created buffer handle now live on each `MeshVertexAttribute` as the `initialData` and `bufferHandle` fields.

```
// Before
Mesh::CreateInfo createInfo;
createInfo.vertexData = ...;          // single interleaved blob
createInfo.vertexBufferHandle = ...;

// After â set per-attribute
auto& positionAttr = createInfo.vertexFormat.attributes[0];
positionAttr.initialData = ...;       // bytes for this attribute only
positionAttr.bufferHandle = ...;

```

- `MeshVertexAttribute::stride` was removed. Derive the stride from the format:

```
// Before
auto stride = attr.stride;
// After
auto stride = gfx::getPixelStride(attr.format);

```

- `MeshVertexAttribute::dataType` and `MeshVertexAttribute::dimension` were replaced with a single `gfx::Format` field. For one-off conversions of legacy `(dataType, dimension)` pairs, use the helper `toKzGfx(dataType, dimension)`.

```
// Before
attr.dataType = GraphicsDataTypeF32;
attr.dimension = 3;
// After
attr.format = gfx::Format::RGB32_Float;

```

- `Mesh::getVertexData()` (no-arg) was removed. To retrieve preserved vertex data, use the per-attribute overload:

```
// Before
const auto& data = mesh.getVertexData();
// After
const auto& data = mesh.getVertexData(VertexAttribute::SemanticPosition);

```

- `Mesh::VertexBufferContainer` value type changed from `Mesh::VertexData { GPUBufferSharedPtr buffer; uint32_t stride; }` to `GPUBufferSharedPtr`. Stride is derived from the attribute format; access the buffer directly:

```
// Before
for (const auto& [key, vd] : mesh.getVertexBuffers()) { use(vd.buffer); }
// After
for (const auto& [key, buffer] : mesh.getVertexBuffers()) { use(buffer); }

```

- `adjustForDeviceCapabilities` now returns `vector<Mesh::CreateInfo::Adjustment>` describing what was adjusted (was `void`). Existing call sites that ignore the return value compile unchanged.
- Pipeline validation now treats `UNorm`/`SNorm`/`UFloat` channel types as compatible with shader `float` inputs, `ColorRGBA` clear values, and `ColorRGBA` sampler border colors. This is a loosening: code that was forced to misclassify clear values or border colors to satisfy validation no longer needs the workaround.
- `gfx::reflection::ReflectionInfo::inputAttributes` and `outputAttributes` now map attribute names to `gfx::reflection::Attribute` (`{ location, component, typeInfo }`) instead of directly to `gfx::reflection::TypeInfo`. Code that reads the reflected type must now go through `.typeInfo`:

Kanzi 4.0 |

Kanzi 4.1 |

`attribute.second.type` |

`attribute.second.typeInfo.type` |

`attribute.second.rows` |

`attribute.second.typeInfo.rows` |

`attribute.second.columns` |

`attribute.second.typeInfo.columns` |

`attribute.second.arraysize` |

`attribute.second.typeInfo.arraysize` |

Rendering now validates each bound color attachmentâs blend state write mask against the reflected fragment outputs and the bound attachmentâs channel set at `BeginRenderPipelineCommand` processing. If the blend state enables writes on channels the fragment shader does not produce *and* the bound attachment has those channels, the validator reports `commands-color-write-mask-mismatch`. Write mask bits that target channels the bound attachment lacks are no-ops on hardware per spec ([Vulkan, Shader Interfaces â Fragment Output Interface](https://docs.vulkan.org/spec/latest/chapters/interfaces.html#interfaces-fragmentoutput); [OpenGL 4.6 Core, Â§17.4.2 Fine Control of Buffer Updates](https://registry.khronos.org/OpenGL/specs/gl/glspec46.core.pdf)) and are not reported. Existing pipelines that over-bind attachments must clear `colorWriteMask` for the channels the shader does not write only when those channels are present in the bound attachment.
- `DrawObjectsRenderPass::ViewportProperty` has moved to the `RenderPass` base class and is renamed to `RenderPass::OutputViewportProperty`. The property is now available on every render pass, not only Draw Objects render passes. The underlying property identifier has changed from `"DrawObjectsRenderPass.Viewport"` to `"DrawObjectsRenderPass.OutputViewport"`. Existing serialized assets continue to load because the previous identifier is registered as the legacy name of the new property. Projects using the Java or Lua API must now access the property through `RenderPassMetadata` instead of `DrawObjectsRenderPassMetadata`.

Kanzi 4.0 |

Kanzi 4.1 |

`DrawObjectsRenderPass::ViewportProperty` |

`RenderPass::OutputViewportProperty` |
- The following `Mesh` methods now take a `VertexAttribute::SemanticKey` parameter to identify which vertex attribute to access: `Mesh::getVertexBufferHandle`, `Mesh::getVertexBuffer`, `Mesh::setVertexData`, and `Mesh::setVertexSubData`.

You can also call `Mesh::getVertexBuffer` with a `VertexAttribute::Semantic` parameter to retrieve the vertex buffer for the first attribute that matches the specified semantic.

Kanzi 4.0 |

Kanzi 4.1 |

`mesh.getVertexBufferHandle()` |

`mesh.getVertexBufferHandle({ VertexAttribute::SemanticPosition, 0u })` |

`mesh.getVertexBuffer()` |

`mesh.getVertexBuffer({ VertexAttribute::SemanticPosition, 0u })` |

`mesh.setVertexData(data)` |

`mesh.setVertexData(data, { VertexAttribute::SemanticPosition, 0u })` |

`mesh.setVertexSubData(data, offset)` |

`mesh.setVertexSubData(data, offset, { VertexAttribute::SemanticPosition, 0u })` |
- Removed `kanzi::Renderer::setLogging`. The method has been a no-op since the migration to Kanzi graphics. Remove any calls to `renderer.setLogging()` from your application code. Graphics API-call logging will be reimplemented in a future release.
- Removed `kanzi::Renderer::getLogging` and `kanzi::Renderer::getDumpStateOnDrawCalls`. Remove any calls to `renderer.getLogging()` and `renderer.getDumpStateOnDrawCalls()` from your application code.

## Changes to the Runtime API

`TaskDispatcherBase` is now merged into `TaskDispatcher`, which is now moved from `kanzi/core.ui/platform/task_dispatcher/common/task_dispatcher.hpp` to `kanzi/core.ui/task_dispatcher/task_dispatcher.hpp`.

To migrate:

- Update any include directives of `task_dispatcher.hpp` to the new location.
- If your code references `TaskDispatcherBase`, replace it with `TaskDispatcher`.

`Platform` class and its derived platform-specific classes are renamed to use the `PlatformContext` suffix.

To migrate:

- Replace `Platform` with `platform::PlatformContext` and update the include directive:

Kanzi 4.0 |

Kanzi 4.1 |

`kanzi/platform/kz_platform/kz_platform.hpp` |

`kanzi/platform/platform_context/platform_context.hpp` |
- Replace the platform management functions:

Kanzi 4.0 |

Kanzi 4.1 |

`createDefaultPlatform` |

`platform::createDefaultPlatformContext` |

`destroyDefaultPlatform` |

`platform::destroyDefaultPlatformContext` |

`getDefaultPlatform` |

`platform::getDefaultPlatformContext` |
- If you implement a custom platform, rename your subclass. The header follows the same pattern: replace `kz_platform/<custom_name>/<custom_name>_platform.hpp` with `platform_context/<custom_name>/<custom_name>_platform_context.hpp`.

Kanzi 4.0 |

Kanzi 4.1 |

`AndroidPlatform` |

`platform::AndroidPlatformContext` |

`EmscriptenPlatform` |

`platform::EmscriptenPlatformContext` |

`MacosPlatform` |

`platform::MacosPlatformContext` |

`QnxPlatform` |

`platform::QnxPlatformContext` |

`StubPlatform` |

`platform::StubPlatformContext` |

`WaylandPlatform` |

`platform::WaylandPlatformContext` |

`Win32Platform` |

`platform::Win32PlatformContext` |

`X11Platform` |

`platform::X11PlatformContext` |

`GlContextApi` class and its derived platform-specific classes are renamed to use the `GlGraphicsContext` suffix. The `createDefaultGlContextApi` factory function is renamed to `platform::makeDefaultGlGraphicsContext`.

To migrate:

- Replace `GlContextApi` with `platform::GlGraphicsContext` and update the include directive from `kanzi/platform/context/gl_context_api.hpp` to `kanzi/platform/platform/gl/common/gl_graphics_context.hpp`.
- Replace the factory function call `createDefaultGlContextApi` with `platform::makeDefaultGlGraphicsContext`.
- Replace `getGlContextApi()` with `getGlGraphicsContext()` on your `platform::PlatformContext` instance.
- If you implement a custom OpenGL context by subclassing `GlContextApi`, rename your class. The header follows the same pattern: replace `context/<name>/<name>_context_api.hpp` with `platform/gl/graphics_context/<name>/<name>_graphics_context.hpp`.

Kanzi 4.0 |

Kanzi 4.1 |

`EglContextApi` |

`platform::EglGraphicsContext` |

`EglEmscriptenContextApi` |

`platform::EglEmscriptenGraphicsContext` |

`EglOhosContextApi` |

`platform::EglOhosGraphicsContext` |

`EglQnxStreamsContextApi` |

`platform::EglQnxStreamsGraphicsContext` |

`GlxContextApi` |

`platform::GlxGraphicsContext` |

`WglContextApi` |

`platform::WglGraphicsContext` |

The `platform::GlGraphicsContext` member function `getOGLProcAddress` is renamed to `getGLProcAddress`.

To migrate, rename the calls. If you implement a custom OpenGL context, rename the override accordingly:

Kanzi 4.0 |

Kanzi 4.1 |

`getOGLProcAddress` |

`getGLProcAddress` |

Instead of casting the result of `getGLProcAddress` to the function pointer type yourself, you can use the new `getGLProcAddressInto` member function. It deduces the function signature from the passed pointer, stores the loaded entry point, and returns whether the entry point was found.

Several platform API headers are moved to reflect the reorganization of the `kzplatform` library.

To migrate, update any include directives that reference the old paths:

- `kanzi/platform/kz_platform_api.hpp` -> `kanzi/platform/platform_api.hpp`
- `kanzi/platform/graphics/platform_types.hpp` -> `kanzi/platform/graphics/graphics_types.hpp`
- `kanzi/platform/platform_events.hpp` -> `kanzi/platform/log/platform_events.hpp`
- `kanzi/platform/utilities/utilities.hpp` -> `kanzi/platform/windowing_ng/native_accessors.hpp`
- `kanzi/platform/context/vulkan_functions.hpp` -> `kanzi/platform/platform/vulkan/common/vulkan_functions.hpp`
- Headers in `kanzi/platform/graphics/` moved to `kanzi/platform/graphics_output/`: `graphics_output.hpp`, `framebuffer_graphics_output.hpp`, `windowed_graphics_output.hpp`
- `kanzi/platform/graphics/make_default_graphics_output.hpp` -> `kanzi/platform/target/graphics_output/make_default_graphics_output.hpp`
- Headers in `kanzi/platform/input/` moved to `kanzi/platform/input_ng/`: `event_filter.hpp`, `event_queue.hpp`, `event_source.hpp`, `event_source_properties.hpp`, `events.hpp`, `input_types.hpp`, `wakeup_signal_source.hpp`
- `kanzi/platform/input/make_default_event_source.hpp` -> `kanzi/platform/target/input_ng/make_default_event_source.hpp`
- Headers in `kanzi/platform/context/` moved to `kanzi/platform/windowing/`: `kzs_surface.h`, `kzs_surface_configuration.h`
- Headers in `kanzi/platform/windowing/` moved to `kanzi/platform/windowing_ng/`: `native_handles.hpp`, `window_geometry.hpp`, `window_properties.hpp`, `window_style.hpp`
- Headers in `kanzi/platform/gl/` moved to `kanzi/platform/platform/gl/common/`: `opengl.hpp`, `gl_function_pointers.hpp`, `gl_loaders.hpp`, `kzs_opengl_enum.h`

## Changes to the application framework

- `kanzi/core.ui/application/application_properties.hpp` no longer includes `kanzi/core.ui/graphics/renderer.hpp`.

If your code includes `application_properties.hpp` (directly, or transitively through `application.hpp`) and uses `Renderer` or other types declared in `renderer.hpp` without including it directly, add an explicit include:

```
#include <kanzi/core.ui/graphics/renderer.hpp>

```

- Removed the `GraphicsLoggingEnabled` application configuration option, the `ApplicationProperties::graphicsLoggingEnabled` field, and the `--log-graphics` command-line argument. These had no effect since the migration to Kanzi graphics. Remove `GraphicsLoggingEnabled = 1` from `application.cfg` files and any references to `ApplicationProperties::graphicsLoggingEnabled` or `--log-graphics` from your application code.

## Changes to List Boxes

- New `TrajectoryListBoxConcept` and `TrajectoryListBoxConceptImpl` classes introduced for Trajectory List Box along with the new `GridListBoxConceptImpl` class for Grid List Box.

Allows easier implementation of custom list boxes based on existing behavior.
- `ListBoxTrajectoryPresenter` and `ListBoxGridPresenter` now support CRTP in their derived classes.

Allows easier implementation of custom presenters based on existing behavior.
- All the List Box concepts and Impl classes are moved into the list_box sub-directory for consistency.

## Changes to Android NDK version

- The Android NDK version is updated to 28.2.13676358, and Kanzi now supports 16 KB page sizes by default as required for [Google Play compatibility](https://developer.android.com/guide/practices/page-sizes) on Android 15+ devices.

To migrate, set the `ndkVersion` to 28.2.13676358 in the `build.gradle` file of your application.

## Changes to Material

- In the `Material` class, renamed these public member functions:

Kanzi 4.0 |

Kanzi 4.1 |

`Material::acquireDebugMaterialSolid` |

`Material::acquireMaterialSolid` |

`Material::acquireDebugMaterialTextured` |

`Material::acquireMaterialTextured` |

## Changes to application input events

- Application input events `sleep` and `wakeup` are renamed to `paused` and `resumed`, to be consistent with the application states. Change the event types and function calls in your code to use the new names:

Kanzi 4.0 |

Kanzi 4.1 |

`InputEvent::Type::ApplicationSleep` |

`InputEvent::Type::ApplicationPaused` |

`InputEvent::Type::ApplicationWakeup` |

`InputEvent::Type::ApplicationResumed` |

`addApplicationSleepEvent()` |

`addApplicationPausedEvent` |

`addApplicationWakeupEvent()` |

`addApplicationResumedEvent` |

The previously unused `InputEvent::Type::ApplicationPaused` event now reports that the application is paused and transitioned to `MainLoopState::Paused`. This event serves the function previously held by `ApplicationSleep`.

## Changes to material type commands

- The `SaveMaterialType` command is removed. To share material types between projects, use ExportProjectItems instead.
- The `LoadMaterialType` command is deprecated. To import material types from `.kzexport` archives, use ImportProjectItems instead.

## Changes to the TextBoxConcept API

- Renamed metaclasses of message arguments in `TextBoxConcept` to match the containing class name.

To migrate your Kanzi Engine Lua API and Kanzi Java API applications, rename `TextBoxMetadata` to `TextBoxConceptMetadata`.

## Changes to the TextInputManipulator API

- Renamed metaclasses of message arguments in `TextInputManipulator` to match the containing class name.

To migrate your Kanzi Engine Lua API and Kanzi Java API applications, rename `TextInputConceptMetadata` to `TextInputManipulatorMetadata`.

## Changes to Kanzi Engine Lua API

- Deprecated `PropertyType:new` and `MessageType:new` methods in favor of `PropertyType:find` and `MessageType:find`.

To migrate your Kanzi Engine Lua API scripts, rename `PropertyType:new` to `PropertyType:find` and `MessageType:new` to `MessageType:find`.
- Multiple constructors in Lua were renamed from `create` to `create1`.

Kanzi 4.0 |

Kanzi 4.1 |

`CallbackBindingProcessor:create` |

`CallbackBindingProcessor:create1` |

`NodeEffectPrefab2D:create` |

`NodeEffectPrefab2D:create1` |

`RangeBindingProcessor:create` |

`RangeBindingProcessor:create1` |

`RenderPassPrefab:create` |

`RenderPassPrefab:create1` |

## Changes to Platforms

- Removed `listEGLAttributes` in favor of more flexible `formatEGLAttributes`, which creates a formatted, human-readable string.

To migrate, use `formatEGLAttributes` to format the attributes, then pass the formatted string into `kzLogInfo`.

```
// Before migration.
listEGLAttributes("EGL context attributes", attribs);

// After migration.
kzLogInfo(KZ_LOG_CATEGORY_EGL, ("{}", formatEGLAttributes("EGL context attributes", attribs)));

```

- `platform::createDefaultPlatformContext`, `platform::destroyDefaultPlatformContext`, and `platform::getDefaultPlatformContext` moves from `platform_context.hpp` to a new dedicated header.

To migrate, update the include:

```
// Before migration.
#include <kanzi/platform/platform_context/platform_context.hpp>

// After migration.
#include <kanzi/platform/target/platform_context/default_platform_context.hpp>

```

## Changes to PropertyFieldAnimationTimelinePlayback

The protected constructor of `PropertyFieldAnimationTimelinePlayback` has a new parameter:

```
// Kanzi 4.0
explicit PropertyFieldAnimationTimelinePlayback(
    PropertyFieldAnimationTimelineSharedPtr, ObjectSharedPtr, bool relative);

// Kanzi 4.1
explicit PropertyFieldAnimationTimelinePlayback(
    PropertyFieldAnimationTimelineSharedPtr, ObjectSharedPtr, bool relative,
    const optional<TimelinePlaybackContext::RuntimeEnvironment>& runtimeEnv);

```

If you subclass `PropertyFieldAnimationTimelinePlayback` and call the protected constructor directly, pass `nullopt` for `runtimeEnv` to preserve the previous behavior.

Additionally, copy and move constructors and assignment operators are now explicitly deleted on this class.
## Changes to the PipelineStateRenderPass Color Write Mode

- The `GraphicsColorWriteMode` enumeration is removed and replaced by `gfx::ColorWriteMask`, a bitmask flags type that allows combining individual channel flags.

The `PipelineStateRenderPass::ColorWriteModeProperty` type changes from `PropertyType<GraphicsColorWriteMode>` to `kanzi::PropertyType<kanzi::gfx::ColorWriteMask>`. The `getColorWriteMode()` and `setColorWriteMode()` accessors now use `gfx::ColorWriteMask`.

Because `gfx::ColorWriteMask` is a bitmask, you can combine channel flags using the bitwise OR operator:

```
// Kanzi 4.0
renderPass->setColorWriteMode(GraphicsColorWriteModeRGBA);

// Kanzi 4.1
renderPass->setColorWriteMode(gfx::ColorWriteMask::RGBA);
renderPass->setColorWriteMode(gfx::ColorWriteMask::R | gfx::ColorWriteMask::G);

```

The following table maps old enumeration values to new flag equivalents:

Kanzi 4.0 (`GraphicsColorWriteMode`) |

Kanzi 4.1 (`gfx::ColorWriteMask`) |

`GraphicsColorWriteModeNone` |

`gfx::ColorWriteMask::None` |

`GraphicsColorWriteModeRGB` |

`gfx::ColorWriteMask::RGB` |

`GraphicsColorWriteModeRGBA` |

`gfx::ColorWriteMask::RGBA` |

`GraphicsColorWriteModeR` |

`gfx::ColorWriteMask::R` | `gfx::ColorWriteMask::A` |

`GraphicsColorWriteModeG` |

`gfx::ColorWriteMask::G` | `gfx::ColorWriteMask::A` |

`GraphicsColorWriteModeB` |

`gfx::ColorWriteMask::B` | `gfx::ColorWriteMask::A` |

`GraphicsColorWriteModeGB` |

`gfx::ColorWriteMask::G` | `gfx::ColorWriteMask::B` | `gfx::ColorWriteMask::A` |

`GraphicsColorWriteModeA` |

`gfx::ColorWriteMask::A` |
**Note:** The integer values of the enumeration changed. The new type uses power-of-two bitmask values (`R=1`, `G=2`, `B=4`, `A=8`) instead of the previous sequential indices. Update any application code that stores or compares the raw integer value of `GraphicsColorWriteMode`. `.kzm` project files are migrated automatically when you open them in Kanzi Studio 4.1.
- In the Kanzi Studio plugin interface, `PipelineStateRenderPassColorWriteMode` changes from `TypedProperty<ColorWriteModeEnum>` to `TypedProperty<int>`, and the `ColorWriteModeEnum` type is removed. Update plugin code that reads or writes this property to use raw integer flag values (`Red=1`, `Green=2`, `Blue=4`, `Alpha=8`).
- In Kanzi Engine Lua API, replace the removed `GraphicsColorWriteMode` table with `gfx.ColorWriteMask`:
Kanzi 4.0 (`GraphicsColorWriteMode`) |
Kanzi 4.1 (`gfx.ColorWriteMask`) |
`GraphicsColorWriteMode.GraphicsColorWriteModeNone` |
`gfx.ColorWriteMask.None` |
`GraphicsColorWriteMode.GraphicsColorWriteModeRGBA` |
`gfx.ColorWriteMask.RGBA` |
`GraphicsColorWriteMode.GraphicsColorWriteModeRGB` |
`gfx.ColorWriteMask.RGB` |
`GraphicsColorWriteMode.GraphicsColorWriteModeR` |
`gfx.ColorWriteMask.R | gfx.ColorWriteMask.A` |
`GraphicsColorWriteMode.GraphicsColorWriteModeG` |
`gfx.ColorWriteMask.G | gfx.ColorWriteMask.A` |
`GraphicsColorWriteMode.GraphicsColorWriteModeB` |
`gfx.ColorWriteMask.B | gfx.ColorWriteMask.A` |
`GraphicsColorWriteMode.GraphicsColorWriteModeGB` |
`gfx.ColorWriteMask.G | gfx.ColorWriteMask.B | gfx.ColorWriteMask.A` |
`GraphicsColorWriteMode.GraphicsColorWriteModeA` |
`gfx.ColorWriteMask.A` |
- In Kanzi Java API, replace `GraphicsColorWriteMode` with `ColorWriteMask`, and update `PipelineStateRenderPassMetadata.ColorWriteModeProperty` references accordingly.
- `.kzm` project files that contain `PipelineStateRenderPass.ColorWriteMode` values are automatically migrated to the new flags representation when you open them in Kanzi Studio 4.1.

## Changes to the Kanzi Documentation MCP server

A new unified Kanzi Documentation MCP server is available at `https://docs.mcp.kanzi.com/mcp` with a new mcpb bundle for Claude Desktop at https://docs.kanzi.com/mcp/kanzi-docs-mcp.zip. The new endpoint supports all loaded Kanzi versions.

The existing version-specific URLs (`kanzi-docs-mcp-v3-9.*` and `kanzi-docs-mcp-v4-0.*`) remain supported. To use the new integration, migrate to the unified URL. See Kanzi Documentation MCP server.

If you previously added version-specific entries (such as `kanzi-docs-v3-9` or `kanzi-docs-v4-0`) to your MCP client configuration, remove them after adding the unified `kanzi-docs` entry. Keeping duplicate entries can hang client startup.
## Changes to shader compilation

Starting with Kanzi 4.1.0, shader **source code** in your materials must use GLSL ES 310+ or desktop GLSL 140+ syntax. Legacy GLSL constructs (`attribute`, `varying`, `gl_FragColor`, `gl_FragData[N]`) are no longer accepted. You must update shaders in your Kanzi Studio projects that still use legacy syntax.

This is a change to shader *authoring* requirements, not deployment. Kanzi cross-compiles your shader sources to the GLSL dialect required by the projectâs Target Graphics API setting, so you can still deploy to OpenGL ES 3.0. The exception is if your shader uses features introduced in GLSL ES 3.1 or later â compute shaders, image load/store, shader storage buffer objects, and so on. Features your source uses must be available on the selected Target Graphics API.

To migrate your shaders, apply these transformations:

Legacy syntax |

Replacement |

`attribute` |

`in` (vertex shader inputs) |

`varying` (vertex shader) |

`out` (vertex shader outputs) |

`varying` (fragment shader) |

`in` (fragment shader inputs) |

`gl_FragColor` |

User-defined output variable declared with `layout(location = 0) out vec4 fragColor;` |

`gl_FragData[N]` |

User-defined output variables declared with `layout(location = N) out vec4 fragDataN;` |

Missing `#version` |

Add `#version 310 es` (embedded systems) or `#version 460` (desktop) |

`#version 100` or `#version 300 es` |

`#version 310 es` |

`precision` inside `main()` |

Move `precision` to global scope before `main()`. ES 310 requires global precision for floats in fragment shaders. |

`texture2D(sampler, uv)` |

`texture(sampler, uv)` |

`textureCube(sampler, uv)` |

`texture(sampler, uv)` |

Additional considerations:

- Named uniform blocks must use explicit layout qualifiers. Replace `uniform BlockName { ... };` with `layout(std140, binding = N, set = M) uniform BlockName { ... };`.
- Kanzi reserves descriptor set 0, binding 0 for the automatically-generated uniform block that holds loose uniforms (`uniform float Opacity;` and so on). If you have a material type that uses a custom uniform block at set 0, binding 0, move it to a different binding.
- Your choice of Target Graphics API in Project Properties constrains which ES 310 / GL 140 features you can use. Compute shaders, image load/store, and shader storage buffer objects require Target Graphics API of OpenGL ES 3.1 or later (or the desktop equivalent). A shader that uses only ES 310 *syntax* â `in` / `out`, `texture()`, named output variables â still cross-compiles cleanly to an OpenGL ES 3.0 target.

See Setting the OpenGL ES version for the updated shader authoring reference.
