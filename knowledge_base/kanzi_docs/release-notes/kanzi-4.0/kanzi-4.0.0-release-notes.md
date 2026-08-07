---
title: Kanzi 4.0.0 release notes
source: https://docs.kanzi.com/4.1.0/en/release-notes/kanzi-4.0/kanzi-4.0.0-release-notes.html
---

# Kanzi 4.0.0 release notes


These notes list all features, changes and notable fixes from the Kanzi 4.0.0 alpha and beta releases.
## Kzm file format


In Kanzi Studio, introduced the kzm file format to replace the kzproj file format. When you use the kzm file format, Kanzi Studio stores the project in multiple kzm files, instead of a single project file.

The goal of the kzm file format is to improve change review, teamwork, and collaboration on Kanzi Studio projects by:

- Providing granular, human-readable files so you can clearly see and review exactly what changed
- Reducing merge conflicts and making any remaining ones easier to resolve
- Simplifying the sharing of project items between different projects
- Enabling scriptable modifications through diff-friendly files


Kanzi Studio now saves all new projects in the kzm file format. See Kzm file format.

Kanzi Studio can still open kzproj projects, but when you save such a project, Kanzi Studio automatically converts it to kzm and removes the kzproj file. This conversion is not reversible. Once you save a project in kzm format, you can no longer revert that project to the kzproj format.

Kanzi Studio shows a notification to inform you about the conversion before completing the save operation.
## Kanzi graphics


Introduced Kanzi graphics (kzgfx), the render hardware interface (RHI) for Kanzi. Kanzi graphics supports Kanzi applications running on OpenGL 3.3+, OpenGL ES 3.0+, or Vulkan 1.1+. See Kanzi graphics. For information on how to select which API to use, see Graphics library.

In the Project > Properties, use the Preview Graphics API Configuration property to set which API the Kanzi Studio Preview uses. For example, to use the OpenGL renderer set the property to OpenGL.

In the application configuration, you can:

- Set the preferred GPU type that to use with the Kanzi Vulkan backend. See Preferred Vulkan GPU.
- Enable the statistics and validation layers for the Kanzi graphics library. Use this information to check whether your application correctly uses the graphics API. See GraphicsStatisticEnabled and GraphicsValidationEnabled.
- The supported ASTC graphics formats have been extended to include HDR formats, that are exposed as texture formats in Kanzi Studio. See Using the ASTC algorithm


To migrate your Kanzi application, see Introduction of Kanzi Graphics.
## Prism graph editor


Introduced the Prism graph editor, a visual node tool for creating render graphs. You can add or remove rendering nodes and quickly iterate on visual effects. Graphs provide a clear overview of rendering operations, let you adjust properties, and show results instantly. See Prism graphs.
## Android


- Updated all Android application templates to use the latest Gradle 8+ tooling. The templates now support Android Studio Ladybug and JDK 21.
- Refactored the integration of Kanzi into Gradle, replacing the Kanzi Gradle plugin with a transparent, modifiable and copyable sub-project. This means that you can introduce Kanzi into your Android application by copying this sub-project to your Android application. See Adding Kanzi Android framework (droidfw) to your Android application.
- Introduced the Android library template. This template enables you to export an AAR with prebuilt Kanzi C++ libraries. You can use it from any number of Android applications. This means that your application build does not require access to a Kanzi installation, as long as your application project can reach the prebuilt Kanzi AARs from your package management system or version control.

To learn more about this workflow, see Integrating Kanzi as a prebuilt library (AAR).
- Updated the Android NDK version to 26.3.11579264. See Changes to Android NDK version.
- Updated Android application templates and examples to explicitly set CMake version.
- Upgraded the Java language version of both the Kanzi application framework (appfw) and Kanzi Android framework (droidfw) to 11.

## Fallback fonts support


Kanzi now allows you to define a chain of fallback fonts for a font family. If a glyph is missing in the primary font, Kanzi uses the next font in the list to render that glyph. See Font fallback
## Color fonts


Kanzi can now render text with fonts that contain emoji and other colored glyphs. See Color fonts.
## Text layout optimization


- Kanzi now caches shaped text. This improves layout performance when rendering the same text under different constraints.
- When rendering text, Kanzi no longer clips text that fits inside the padding area, but extends beyond the text layout area.

## Resources


Introduced a new Asset Toolkit with easy to use, ready-made components and materials with a similar structure and set of properties, that you can use to create Kanzi applications faster. See Asset Toolkit.
## Kanzi Studio Preview


- In Kanzi Studio, you can now take screenshots directly from the Preview window using the Screenshot button . See Taking a screenshot of the Preview.
- In Kanzi Studio, the visualization of the Debug Objects has been updated.
- In Kanzi Studio, the visualization of the Debug Grid has been updated.
- You can now enable experimental selection outline in User Preferences > Experimental tab

## Kanzi Studio usability


- Improved tooltips in Kanzi Studio:

  - You can now access feature and Kanzi Engine C++ API reference documentation from tooltips.
  - Tooltips now show the default and custom Kanzi Studio shortcut keys. For the list of the default shortcut keys and how to set custom shortcut keys, see Default shortcut keys.
  - You can now copy Kanzi Engine property type name in a tooltip.
  - Kanzi Studio now shows tooltips for property types in dropdown menus.

- You can now view nodes and resources related to the selected item in a dockable Related Items window. The window provides direct navigation to related items.

Open the window from the context menu of any node or resource, or from the Window main menu.
- In the Node Tree, an indicator next to a node now shows when a State Manager, Binding, Data Source Binding, or an Animation sets the values of some properties in that node.
- You can now search for and filter items in the Library window.
- You can now add, edit, and remove identical bindings from multiple nodes at a time.
- You can now start creating a binding directly from a property and view all bindings that affect a property from the context menu of that property.

See Creating simple bindings.
- Kanzi Studio now has a redesigned New Project window that simplifies the creation of new projects. See Creating a project.
- When you rename a project, Kanzi Studio will now update the name of the main project file when you save the project.
- Kanzi Studio lock file now has a static name `KanziStudio.lock`.
- Changed `SaveProject` and `NewProject` commands to accept directory paths instead of project file paths. To migrate your Kanzi Studio scripts, see Changes to Kanzi Studio commands.
- Kanzi Studio now requires that a Scene node is always the first child in a Viewport2D node. This allows for proper handling of focus and better application performance. This change does not require you to migrate your project, but Kanzi Studio does highlight Scene nodes that do not follow these requirements.
- When building an Android package from Kanzi Studio, Kanzi Studio now exports the cfg file based on the project Binary File Name property. For migration instructions, see Changes to Kanzi Studio Android package export.
- You can now access the Screen nodeâs resource dictionary from the root nodes of all prefabs. This allows you to reference and use aliases defined in the Screen nodeâs dictionary within bindings inside node prefabs.
- In the Animation Clip Editor, when using the Keyframe tool , Kanzi Studio now automatically selects the last keyframe created. This allows you to edit the keyframeâs values, without having to switch to the Move tool  and select the keyframe first.
- In the Prefabs window the ellipsis button opens an additional menu, which allows to delete unreferenced items, collapse or expand the tree.
- In the Animation Clip Editor, when using the Move tool  to select a node or curve, Kanzi Studio now selects the control point closest to the cursor if there are more than one.
- In the State Manager, when you try to set the Mesh Material property state, Kanzi Studio now issues a warning instead with workaround instructions.
- In the Asset Packages, when you import the same asset package, Kanzi Studio now duplicates its prefab and increments the number in its name instead of replacing the existing asset package.
- Clicking the expander in Kanzi Studio now expands and collapses all tree items under it when Ctrl is pressed.
- You can now sign in to your Kanzi Account in Kanzi Studio. See Kanzi Hub and Kanzi Account.
- In the Kanzi Studio Node Tree, you can now right-click the override indicator in the Kanzi Studio project and select the source you wish to navigate to from the context menu.
- Kanzi installer now adds a registry entry that associates `.kzm` files with Kanzi Studio.
- Kanzi installer now adds a registry entry that enables long file path support for Windows and Git, required by the `.kzm` Kanzi Studio project file format.
- In the Project Merge, when you select an item that only exists in the source project, Kanzi Studio now shows the properties of that item.
- You can no longer create a project in a root directory, or in a child or parent directory of the existing project.
- Kanzi Studio no longer updates the mesh data version during project load.
- When creating a new Animation, Kanzi Studio now adds two default keyframes automatically.
- You can now access compute materials in selectors from a Kanzi Engine plugin. In the metadata, use the `MaterialComboBox.ComputeMaterialSelector` editor. See Kanzi Studio property editors for property types declared in Kanzi Engine plugins.

## Documentation


- Get answers about Kanzi from the Documentation AI tools. In Documentation:

  - Click Ask AI to start a conversation with the Kanzi AI assistant
  - Use the AI assistant tools to set the Kanzi context for your AI tool. For example, connect to Documentation MCP server through Claude Desktop or Visual Studio Code.

- Kanzi example and tutorial projects are no longer part of the Kanzi installer. You can download the tutorial and example projects in the Kanzi Studio Quick Start window in the appropriate section.
- All example, tutorial, and asset projects are now migrated to the kzm file format.
- The `Node2D_plugin` example now works with any Kanzi project without code modification.
- The `Android data source` example now matches the tutorial code.

## Platforms


- Kanzi Engine now reports mouse wheel events on QNX.
- You can now list EGL attributes in a comma-separated format. See `listEGLAttributes`.
- You can now convert EGL error codes to strings. In the Kanzi Engine C++ API reference, see `kzsEGLErrorString`.
- Converted QNX EGL graphics output API from C to C++.

In the Kanzi Engine C++ API reference, see `qnx::DefaultQnxEGLGraphicsOutput`.
- You can now set the window class name for your application. See WindowClassName.
- You can now set the application ID for Wayland XDG shell in the Kanzi Engine C++ API. See `kanzi::wayland::XDGToplevel::setId` and `kanzi::wayland::XDGShell::setAppId`.
- Added `wayland::WaylandIVIEGLGraphicsOutput` to Wayland platform packages as a graphics output option.
- On QNX, you can now set the context type flags that you want your Kanzi application to use. See QNX context type selection.
- `qnx::DefaultQnxEGLGraphicsOutput` now supports the `QnxWindowBufferCount` configuration option that sets the number of window buffers to use. To ensure compatibility, if you do not set this configuration option explicitly, Kanzi uses the value from the `WindowBufferCount` configuration option. See QnxWindowBufferCount and WindowBufferCount.
- `qnx::DefaultQnxEGLGraphicsOutput` now respects:

  - Default window position and size setting
  - Default window z-order setting
  - Window group name
  - Default display index
  - Surface padding bits setting

- Kanzi no longer supports QNX development platform 7.0.0.
- Event file descriptor values on POSIX systems are no longer limited by `FD_SETSIZE`.
- Changed Wayland class names related to XDG and IVI to follow CamelCase notation. For example, `XDGToplevel` was changed to `XdgToplevel`.
- All platforms now use Kanzi graphics by default. To migrate your Kanzi application, see Introduction of Kanzi Graphics.


- These backends now correctly set the EGL window surface color space attribute:

  - Android WS
  - Emscripten
  - QNX/PBuffer
  - X11/EGL

- Added a configuration option to enable additional debug logs for the Platform layer. See PlatformLoggingEnabled.
- On Linux DRM/GBM platforms, the DeviceIdentifier setting now takes precedence over DRM module identification. Previously, DeviceIdentifier was only used if all DRM modules failed to open.
- Kanzi now provides its own implementation of from_chars() for floating-point numbers for older toolchains that lack support for it.
- The surface opacity settings on the Wayland IVI backend are now interpreted as floating point numbers, instead of integers. See `wayland::IviSurfaceProps::opacity` and `wayland::IviLayerProps::opacity`.
- On QNX, you can now enable self layout mode of the QNX Screen property for a Kanzi application window. See QnxWindowSelfLayout.
- Moved all the platform-dependent windowing and input code into a separate library (kzplatform). The entire externally facing API of kzplatform is considered experimental, and may change in future releases. System libraries are now linked into kzplatform instead of kzcoreui.

## Kanzi Engine C++ API


- Added these helper methods for working with `span`:

  - `as_bytes` converts a span into a span of bytes.
  - `fromBytes` converts a span of bytes into a span of typed objects.
  - `toSpan` converts a container to a span over that container.
  - `asSpan` and `asConstSpan` convert a single element into a span over that single element.

- Added `to_underlying` to cast an enumeration to the underlying type.
- Added `readAsBytes` to load the contents of a file into a vector of bytes.
- Added `containsFlag` and `containsAnyFlag` to test whether a bit field enumeration contains a specific flag.
- Added `VectorMap` to store a small list of key-value pairs in a vector.
- Removed from the `PinchManipulator` the `setScaleRecognitionThreshold` and `setRotationRecognitionThreshold` functions that had no effect.

See Changes to the Pinch Manipulator.
- In the `Renderer` class, renamed the `setActiveGLGraphicsOutput` method to `Renderer::setActiveGraphicsOutput`. See Changes to the Renderer API.
- Removed the `CompositionStack` parameter from all methods that also had the `Renderer` or `kanzi::Renderer3D` as a parameter. You can now access the `CompositionStack` instance from `Renderer::getCompositionStack`. See Changes to the Composition Stack.
- Modified `CompositionStack` to use the `Framebuffer` class with `CompositionStack::pushComposition` instead of `NativeFramebufferHandle`. See Changes to the Composition Stack.
- Removed the `GlRenderValue` and `GlBlendModeRenderValue` classes and the `updateRenderValue` functions. See Changes to the Renderer API.
- Removed the `GraphicsPrimitiveTypeLineLoop` option from the `GraphicsPrimitiveType` enumeration. See Changes to the Renderer API.
- Simplified the methods related to the framebuffer in the `Renderer` class. See Changes to the Renderer API.
- Removed the `kanzi::Renderer3D` class. You can now access these functions through the `Renderer` class:

  - `Renderer::applyCameraMatrix`
  - `Renderer::beginFrame`
  - `Renderer::disableSubRectangleProjection`
  - `Renderer::endFrame`
  - `Renderer::getActiveGraphicsOutput`
  - `Renderer::getCompositionStack`
  - `Renderer::getInheritedAspectRatioMultiplier`
  - `Renderer::getOverrideClusterMaterial`
  - `Renderer::getOverrideMaterialCallback`
  - `Renderer::getOverrideMaterialCallbackUserData`
  - `Renderer::setActiveGraphicsOutput`
  - `Renderer::setSubRectangleProjection`
  - `Renderer::setOverrideMaterial`
  - `Renderer::setOverrideMaterialCallback`


See Changes to the Renderer API.
- Suspension wake-up signal sources now have an interface you can query with `WakeupSignalSource`. See Changes to suspension handling.
- Attaching an event source to the domain using the `Application` class no longer registers the associated event handle with the main loop scheduler. See Changes to event handling.
- Exposed several low-level functions from dynamic Windows libraries.
- Updated the parameters and return types of several Kanzi Engine APIs to use the `size_t` data type, instead of the `unsigned int`. See Changes to several Kanzi Engine APIs.
- Changed `kanzi::optional` (`optional.hpp`) and `kanzi::string_view` (`string_view.hpp`) to `std::optional` and `std::string_view`. In the previous version of Kanzi on some platforms, these were `boost::optional` and `boost::string_view`. See Changes to several Kanzi Engine APIs.
- Changed `kanzi::byte` (`cstddef.hpp`) to `std::byte`. In the previous version of Kanzi on some platforms, it was `unsigned char`. See Changes to several Kanzi Engine APIs.
- You can now load a kzb file from a memory buffer using `Application::loadKzbFile` `(ConstByteSpan fileData, bool setStartupPrefab)`. Keep the memory buffer alive until you destroy the application.
- Removed the default stack states from the `CompositionStack`. All stack states must be explicitly pushed onto the stack. See Changes to the Composition Stack.
- Removed deprecated functions `Renderer::getColorReadFormat` and `Renderer::getColorReadType`. See Changes to the Renderer API.


- Removed deprecated class `kanzi::TextureSwizzleMask`.
- Removed the `kanzi::Tag` class as an abstraction to manipulate tags in nodes. See Changes to Tags.
- Added the ability to set custom sleeping logic for `MainLoopScheduler::yield` with `MainLoopScheduler::setCustomSleepFunctionForYield`, so that it can be optimized for specific platforms.
- Removed all apply functions from the `CompositionStack`. Settings are automatically applied immediately after all push and pop operations. See Changes to the Composition Stack.
- Added API functions for standardized PBR shader properties.
- Removed the `checkGLSupport` and `checkGLESSupport` methods from the `Renderer`. See Changes to the Renderer API.
- `TaskDispatcherBase::executeTasks` now throws an exception if called again while it is still executing, or is called from a thread that the dispatcher doesnât belong to. Previously, doing either resulted in undefined behavior.
- Deprecated and removed all traces of `RenderTargetMode` in `Texture` and related types. See Changes to the Renderer API.
- Deprecated and removed `ProgressiveRenderingViewport2D.MultisampleLevel`. See Changes to Progressive Rendering Viewport 2D properties.
- Win32 string utilities found inside `kanzi/core/platform/cpp/win32/string_conversion.hpp` have been moved from the `kanzi` namespace to `win32`


- The default `SurfaceColorSpace` for Kanzi Engine applications when a configuration is not present was changed from `SurfaceColorSpace::sRGB` to `SurfaceColorSpace::Standard`. This value is consistent with the color workflow configured by default in new Kanzi Studio projects.


- Introduced the `FontFamily` and `FontRuntime` methods to manage fallback font chains.


- Changed the signatures of the `GlyphRun` and `TextFormat` methods. See Changes to text rendering.


- Added interface to the `TriggerTemplate` that enables you to add Actions and conditions to a Trigger template.

## Activities


- Introduced the OptimizeMemory parameter for Activities. When enabled, Kanzi automatically unloads resources used by these Activities once they are deactivated.

See Virtualization.
- Changed the `ActivityCodeBehind` class:

  - In the Kanzi C++ API, in the `ActivityCodeBehind` class, replaced the `onActive`, `onInactive`, `onActivating`, and `onDeactivating` callbacks with `ActivityCodeBehind::onStatusChange`.
  - In both Kanzi C++ (`ActivityCodeBehind`) and Kanzi Java API (`ActivityCodeBehind`), removed `registerStatusChange`, `registerStatusChangeOverride`, `unregisterStatusChange`, and `unregisterStatusChangeOverride`.


To migrate your Kanzi application, see Changes to the ActivityCodeBehind class.
- Changed the `ActivityElementImpl` and `ActivityHostConceptImpl` classes:

  - From the `ActivityHostConceptImpl` class, removed methods:

    - `getActiveOrAttachedActivating`
    - `getAttachedActivityNodes`
    - `getActivityInfo`

  - The `ActivityElementImpl::onAttachedOverride` method is no longer virtual.


The derived classes must not override these methods because the `ActivityElementImpl` and `ActivityHostConceptImpl` classes use the CRTP pattern.

To migrate your Kanzi application, see Changes to the ActivityElementImpl and ActivityHostConceptImpl classes.
- You can no longer manually add Activities to a Data-Driven Exclusive Activity Host. To learn how to use a Data-Driven Exclusive Activity Host, see Tutorial: Generate UI from a data source and Data-Driven Exclusive Activity Host.

To migrate your project, see Changes to Data-Driven Exclusive Activity Host.
- Introduced the Fallback State to the Exclusive Activity Host. Use a Fallback State when you do not want any Activity to be active in an Exclusive Activity Host.

See Using a Fallback State.
- The default alignment settings for Activities and Activity Hosts are now set to stretch horizontally, vertically, and in depth.

## Animations


To set a Bezier interpolation in the Animation Clip Editor, you can now enter exact values for one or more Bezier handles. See Setting the easing function between keyframes.
## Bindings


- You can now use Boolean, integer, floating-point, vector, color, and matrix types as any of the parameters for:

  - Arithmetic operations `+`, `-`, `*`, and `/`. See Arithmetic operators.
  - Math functions clamp, max (maximum), min (minimum), mod (modulo), pow (power), and rem (remainder).
  - Interpolation functions mix, step, linearStep, smoothStep, and smootherStep.

- String conversions of Boolean values in properties and bindings now result in lower case `true` or `false`:

  - In binding expressions, an implicit cast of a Boolean constant to a string now results in lower case `true` or `false` instead of `True` or `False`.
  - In the Kanzi Engine C++ API, a Boolean to string property binding now writes `true` or `false` instead of 1 or 0.


See Changes to properties and bindings.

## Focus


In your custom focus scope, you can now override the focus candidate selection. See `FocusScope::selectFocusCandidate`.
## Kanzi Engine application configuration


- Removed the `MultisamplePreference` application configuration file option, because Kanzi Engine no longer supports implicit multisampling.
- You can now set the surface present mode in application configuration. See PresentMode.
- You can now set a font size for the PerformanceInfo HUD in application configuration. See PerformanceInfoFontSize.
- Added a configuration option to specify the size of a glyph cache texture for non-scalable fonts, such as color fonts with a CBDT table. See Glyph cache texture size.

## Kzb version


Changed the version of the kzb file format to 36.0.
## List Box


Renamed these List Box messages:

- List Box: Item Hidden to List Box: Item Unloaded
- List Box: Item Visible to List Box: Item Loaded


To migrate your Kanzi application code, see Changes to List Box.
## List Box nodes


The default directional navigation keys now move the key focus in the Grid List Box and Trajectory List Box 3D nodes. See Handling the key focus in a List Box node.

To migrate your application, see Changes to the List Box nodes.
## Rendering


- Renamed the Legacy color workflow to Standard that is now also the default setting for new projects. See Color workflow.
- Kanzi now loads 24-bit RGB PNG and JPEG images into memory as RGBA with the default alpha channel.
- You can now specify the mipmap mode for the automatically generated composition targets of 2D nodes. To generate mipmaps when compositing, set the Mipmap Mode property (`Node2D::MipmapModeProperty`) of a 2D node. The default operation is unchanged and does not generate mipmaps.

If you specify a composition target explicitly using the Render Target property (`Node2D::RenderTargetProperty`), the mipmap mode set in that texture takes precedence.

This change also fixes the issue where mipmaps were not generated before blitting the composition.
- Factory Content now includes Skybox Render Pass that allows to draw a cubemap background into your 3D Scene.
- In the application configuration, the default value of the Preferred Vulkan GPU option is now set to use the First enumerated device. This allows user control over device selection, typically through a control panel application. To restore previous behavior, use the LargestMemory option.
- Renamed `kanzi::GlRenderState` class to `RenderState` to remove the platform-specific âGlâ prefix. The render state abstraction is not specific to OpenGL. See Introduction of Kanzi Graphics.

## Tracing


Added a tracing system to Kanzi Engine. The tracing system allows inspection of Kanzi Engine internals and can help you identify performance issues. The tracing system replaces the profiling system. Tracing is disabled for Release builds. See `Tracing` and Tracing.
## Kanzi Engine Lua API


- Functions that take a `PropertyType` argument no longer silently fail by returning `nil` when objects of other types are passed. They now terminate script execution and log a warning.
- Added `log` module with Kanzi logging functions. See Logging.
- Added `DataSource` methods to access and modify `DataObject` trees.

## Lua Data Source


You can now define and simulate the external data dependencies of your application alongside your design in Kanzi Studio using Lua scripts, without the need to write or compile any native code. See Defining a data source using Lua.
## Windowing


- For Wayland backends, added the option to ignore the `frame()` events sent by the compositor, and process input immediately. This is useful when the compositor does not send `frame()` events properly. See Wayland input mode.
- You can now programmatically set usage flags for the QNX Screen property. See QnxUsageFlags.

## Changes


- Kanzi now requires Visual Studio 2022. Kanzi no longer includes libraries for Visual Studio 2017 and 2019. See Upgrade to Visual Studio 2022.
- Kanzi now requires C++17.
- Updated Boost from 1.77.0 to 1.85.0.
- Replaced libjpeg 9d with libjpeg-turbo 3.0.3.
- The Page and Page Host nodes are deprecated and will be removed in the next version of Kanzi. See Deprecation of Page and Page Host Nodes.
- Upgraded ICU library from version 62.1 to 69.1. Removed unused ICU data and features, reducing library file size by up to 4 times, depending on the target platform.
- Removed the ATC and PVRTC algorithms for compressing textures.
- Significantly improved rendering performance when using tags to filter `NodeList` in cases where the tags are not changing.
- Tag properties are no longer inheritable and the change flags include a separate flag for the tag state being changed. This makes older KZBs exported with old tag settings incompatible. The KZB version number has been incremented.
- Morph data is now fully interleaved when rendering sufficiently few morphs as to not require using data textures.
- You can now add the Keep Alive Behavior property to Fonts. This allows you to keep a font file in memory even when the font is not used. See Setting how Kanzi Engine handles individual unused resources.
- Updated application configuration handling for booleans. Kanzi now only accepts `false`, `true`, `0`, and `1` as valid values for boolean configuration options.
- Renamed entities that refer to OpenGL context APIs for clarity:

  - `kanzi::platform::OpenGLPlatform` has been renamed to `kanzi::platform::GlContextApi`;
  - `kanzi::platform::createDefaultOpenGLPlatform` has been renamed to `kanzi::platform::createDefaultGlContextApi`.

- Updated the Monotype iType library to version 6.3.1 and WorldType Shaper to version 5.3.
- Migrated all platforms to use CMake instead of SCons.
- Consolidated `kanzi::Mesh` index buffers into one in the Mesh object itself, instead of each `kanzi::Mesh::Cluster` having their own.
- Added frame-based interval option to the tracing system. See TracingFrameInterval and TracingTimeInterval.
- Renamed the `TracingInterval` configuration option. See Changes to application configuration
- Removed the `Level Of Detail` node.
- Added the KZ_EXPERIMENTAL macro to flag functionality that is subject to change in future releases.

## Notable fixes

### Kanzi Engine


- Fixed the issue that prevented Kanzi Engine from overriding the Scroll View position through the Scroll Position property during scrolling. (FMW-688)
- Fixed the issue that caused Kanzi to incorrectly forward message arguments in a Message Trigger when one of the Actions triggered the same Message Trigger again. (FMW-707)
- Fixed the issue that prevented using kzAssert macros in constexpr functions. (454808)
- Fixed the issue where the getCameraNormalMatrix shader uniform binding function returned an incorrect matrix when the `kzCameraNormalMatrix` uniform has a translation component. (RENDERING-570)
- Fixed the issue that caused Kanzi Engine to terminate or behave incorrectly when an activating Activity in a Parallel Activity Host or Exclusive Activity Host tried to deactivate itself with an On Attached trigger. (SDK-9210)
- In a 2D node, before the first layout pass, the Actual Width and Actual Height properties are now correctly set to 0.0 instead of `inf`. (RENDERING-589)
- Fixed the issue that prevented Kanzi from rendering a Color Brush when a node has overriden the transparent Brush Color property value of that Color Brush with a non-transparent color. (RENDERING-596)
- Fixed the issue that caused Kanzi to use wrong blend mode in a 2D node when the Blend Mode property value was updated at runtime. (RENDERING-597)
- Fixed the issue that caused Kanzi to fail to reload a render target Texture after GPU resource had been invalidated. (RENDERING-669)
- Fixed the issue that caused Kanzi Engine to terminate when using a simple Data Source binding in a Data Trigger condition expression. (SDK-9232)
- Fixed the issue that prevented Kanzi from rendering the content texture of a Texture Brush that was previously rendered without a content texture. (RENDERING-683)
- Fixed the issue in Texture Brush rendering that caused Kanzi to ignore changes in the Brush Vertical Tiling and Brush Horizontal Tiling property values. (RENDERING-675)
- Fixed the issue that caused the `kzWindowSize` uniform to not equal the size of the Screen node when it has an absolute size smaller than the frame buffer size. (RENDERING-415)
- Fixed the issue that caused Kanzi to erroneously disable the shader binary cache for a target platform that does not support any binary shader formats. The shader binary cache only requires shader binary programs. (RENDERING-693)
- Fixed the issue that prevented Text Block nodes with Word Wrap property enabled and Horizontal Margin property set from being displayed correctly in the vertically arranged Stack Layout. (SDK-8946)
- Fixed the issue that prevented the `Node::lookupNode` function to work with absolute paths acquired with the `Node::getPath` function. (SDK-9570)
- Fixed the restoring of a composition target after Kanzi application wakes up from sleep. (RENDERING-1772)
- Fixed the issue that caused the iType font renderer to not render Arabic diacritics with certain fonts. (SDK-9968)
- Fixed the issue that caused the `Object::getDynamicMetaclass` method to return the base `Resource` metaclass for `StateManager` and `PrefabTemplateNode` resources. (SDK-9987)
- Fixed the issue that caused Kanzi Engine to terminate with assertion in debug mode when certain inputs were entered into the Text Box. (SDK-10001)
- Fixed the issue that caused the `WindowsImeBackend` to fail to handle key input with Unicode supplementary characters. (FMW-128)
- Fixed the issue that caused the Text Box cursor to render to a wrong place. (SDK-9952)
- Fixed the issue that caused misalignments in files that use kzProfiling* macros. (INTE-833)
- Fixed the issue that caused Kanzi to miss information about Timer subscriptions count and Recurring Tasks count in the Performance HUD. (FMW-58)
- Fixed the issue that caused Kanzi to incorrectly select and delete characters in the Text Box when using complex scripts. (FMW-127)

### Kanzi Studio


- Fixed the issue that caused Kanzi to import the DefaultBlitMaterial when you create a BlitRenderPass that uses a built-in material. (FMW-416)
- Fixed these bindings issues (FMW-553):

  - Fixed the issue that prevented a binding source property modification from updating a target property, if a parent node of a source node was reparented or renamed, or if a source node itself was reparented after reopening a project.
  - Fixed the issue that prevented validation on a node with bindings, if a parent node of a source node was moved into prefabs.

- Fixed the issue that caused Kanzi Studio to fail with assertion error in debug mode when an apostrophe character `'` was used in the Binding Editor. (EDITORS-320)
- Fixed the issue that caused Kanzi Studio to drop letters that were entered into dropdowns in the UI while holding down the Shift key. (EDITORS-292)
- Fixed the issue that caused Kanzi Studio to terminate when you create a binding with the < Null > target property type. (FMW-632)
- Fixed the issue that caused Kanzi Studio to generate an incorrect KZB name in the application code when the project name contained unqualified characters like a dash or a space. (FMW-620)
- Fixed the issue that caused Kanzi Studio to occasionally fail to load a project given as a command line argument. (FMW-585)
- Fixed the issue that caused Kanzi Studio to terminate with a runtime exception when resolving project merge conflicts on Smart Materials. (FMW-671)
- Fixed issues in the Activity Browser, that caused Kanzi Studio to terminate with exceptions when:

  - You tried to create an Activity Property with a name beginning or ending with the `.` character, or with multiple `.` characters next to each other. (FMW-618)


  - You tried to add a C++ Code Behind to an Activity whose name includes characters that are not allowed in file names. (FMW-722)

- Fixed the issue that caused Kanzi Studio to print an error message to the Log window, when you tried to undo a reparent command on a node with bindings. (FMW-691)
- Fixed the issue in Kanzi Studio that prevented the output of CMake errors to the Log window, if a Code Behind build failed. (FMW-720)
- Fixed the issue which when renaming a project, caused Kanzi Studio to keep a project manifest file with its previous file name in the project directory. (FMW-735)
- Fixed the issue that caused Kanzi Studio to invalidate mesh data, reporting that the property Imported from refers to an invalid path, when deleting an FBX file from a project. (FMW-692)
- Fixed the issue that caused Kanzi Studio to duplicate mesh data in project files. (FMW-78)
- Fixed the issue that caused Kanzi Studio to terminate when loading a project with a name that started with a resource file directory name. (FMW-783)
- Fixed the issue in Kanzi Studio that prevented the deletion of old directories from the file system, after renaming a project item containing children items. (FMW-721)
- Fixed the issue in Kanzi Studio that allowed you to use hotkeys while the Studio UI is disabled. (FMW-804)
- Fixed the issue that caused Kanzi Studio to use absolute path of Kanzi Engine Java plugin files when exporting and importing kzb files. (ANDROID-380)
- Fixed the issue that caused the `gl_FragCoord` and `kzWindowSize` uniforms to be incorrect in the Kanzi Studio Preview at 100% zoom. (RENDERING-415)
- In the Kanzi default physically-based material types, when you enable the `KANZI_SHADER_RECEIVE_POINT_SHADOW` preprocessor define, Kanzi Studio no longer fails to create a binding for the PointShadowMap custom property type. (RENDERING-626)
- Activating multiple morph targets sometimes causes incremental visual degradation in the morph target normals generated by Kanzi Studio. To fix the issue, you can now use the `KANZI_SHADER_USE_MORPH_NORMAL_LIMIT` preprocessor define. See Using morph target normals. (RENDERING-772)
- In an On Property Changed trigger, if you do not set the Property Type value to a proper value, Kanzi now marks it with a warning. (PRODUCT-354)
- Fixed the issue that caused the Import Images command in the Texture folder context menu to increase the import time and print a warning when importing only non-HDR images. (PRODUCT-1185)
- Fixed the issue that caused Kanzi Studio to terminate when you import a font file to a Library > Font Families > <FolderName> > Font Family. (SDK-9963)
- Fixed the issue that caused Kanzi Studio to mark a deleted Font File in a Font Family as ProjectItemReference: null ABSOLUTE instead of removing it entirely. (SDK-9902)
- Fixed the issue that caused the Preview to terminate when you copy a binding from one prefab to another. (PRODUCT-1291)
- Fixed the issue that left unreleased resources during the Preview shutdown. (PRODUCT-1282)
- Fixed the issue that caused tooltips to overlap dropdowns when you open a dropdown fast. (PRODUCT-1294)
- Fixed the issue that caused incorrect displaying of an Action defined in a Kanzi Engine plugin. (PRODUCT-1302)
- Fixed the issue that prevented Kanzi Studio from importing mipmaps of an asset. (PRODUCT-1299)
- Fixed the issue that caused Kanzi Studio to assign a material to a wrong cluster when you drag and drop a material to the Preview window. (PRODUCT-1026)
- Fixed the issue that prevented sharing Cluster Materials between Kanzi Studio projects. (PRODUCT-800)
- Fixed the issue that prevented adding transitions for the controller property of State Manager on child nodes. (PRODUCT-1317)
- Fixed the issue that caused Kanzi Studio to terminate when using an image file with incorrect bitmap format to generate textures for HDR cubemaps. (PRODUCT-1340)
- Fixed the issue that caused Kanzi Studio to show an error during the first attempt to reactivate a time-limited subscription license. (PRODUCT-1349)
- Fixed the issue that prevented Kanzi Studio from updating a shader file to be updated and applied after you changed it outside of Kanzi Studio. (PRODUCT-1353)
- Fixed the issue that caused Kanzi Studio to keep deleted cubemaps in the project file and exported them to a kzb file. (PRODUCT-1323)
- Fixed the issue that caused Kanzi Studio to terminate when undoing an import of an asset. (PRODUCT-1368)
- Fixed the issue that caused Kanzi Studio to hang when importing a Kanzi Engine plugin with bad metadata. (FMW-50)
- Fixed the issue that prevented Kanzi Studio from importing cubemap texture files merged from another project. (FMW-79)
- Fixed the issue that caused the line numbers and its corresponding text to be misaligned in the Bindings Editor, when using a custom display scale system setting. (EDITORS-56)
- Fixed the issue in Kanzi Studio that prevented the Animation Clip Editor window title from updating accordingly when renamed in the Library. (EDITORS-55)
- Fixed the issue that caused the Move tool  of the Animation Clip Editor in Kanzi Studio to keep multiple curves selected, when making selections without Ctrl pressed. (EDITORS-11)
- Fixed the issue in Kanzi Studio that after reopening a project always marked as outdated Kanzi Engine plugin metadata with new lines in tooltips. Kanzi Studio now also warns when metadata contains unsupported characters. (FMW-261)
- Fixed the issue that prevented the Related Items window from opening in Kanzi Studio. (EDITORS-130)
- Fixed the issue in the Animation Clip Editor in Kanzi Studio that caused the first drag-and-dropped property to be added as a child of the Animation Clip directly, instead of the node to which it belongs. (EDITORS-132)
- Fixed the issue in the Related Items window in Kanzi Studio that caused bindings to be displayed incorrectly. (EDITORS-52)
- Fixed the issue that prevented Kanzi Studio from reporting Code Behind building notifications during startup of the Preview. (FMW-202)
- Fixed the issue that caused a TextBox3D node to process user input keys in the Preview window when the editing mode is enabled. (FMW-289)
- Fixed an issue that caused TextBox3D to render selected text incorrectly when using the Kanzi Graphics renderer with the selection background color alpha set to zero. (FMW-355)
- Fixed an issue that caused WriteOnlyDiskFile to incorrectly treat filenames with non-ASCII characters on Win32. (EDITORS-288)

### Kanzi Android framework (droidfw)


- Fixed the issue that caused a Kanzi Android framework (droidfw)-based view to stop processing user input after receiving a multitouch gesture cancellation from Android. (ANDROID-1386)
- Fixed the issue that caused a KanziViewAdapter instance to continue to render and process user input, after being hidden with `KanziViewAdapter.handleVisibilityChange`. (ANDROID-1317)
- Fixed the issue that incorrectly positioned the Performance HUD in applications based on Kanzi Android framework (droidfw). (ANDROID-1166)

## Kanzi Engine Lua API


- Fixed the issue that caused static linkage of Kanzi Engine Lua API to fail, by including the necessary dependencies into Kanzi installation. (ANDROID-1630)

### Platforms


- Fixed the problem with polling Wayland events during idle state, that caused libwayland internal ring buffer to overflow. (INTE-806)
- Fixed the problem with touch on Wayland, where reusing a touch ID within the same touch frame caused Kanzi to terminate with assertion, when compiled in debug mode. (INTE-795)
