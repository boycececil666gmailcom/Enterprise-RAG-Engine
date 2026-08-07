---
title: Application configuration reference
source: https://docs.kanzi.com/4.1.0/en/working-with/application-configurations/reference-for-application-configuration.html
---

# Application configuration reference


You can configure your Kanzi application:

- In the C++ application override the `Application::onConfigure` function of your application class. Kanzi calls this function as part of application initialization before it reads the `application.cfg` and before it initializes the graphics subsystem. Use this function to configure application properties.
- In `application.cfg` by setting the parameters for Kanzi Studio projects without recompiling your application or even without a C++ application.


The configuration you specify in `application.cfg` overrides the configuration you specify in `Application::onConfigure`.
## Setting which `application.cfg` to use


When you have more than one Kanzi application executable file in a directory, you can set a separate configuration file for each executable.

To set which `application.cfg` to use when running your Kanzi application from the command line, enter the name of the application executable file followed by the `-config` option, and the name of the configuration file.

For example, to run a Kanzi application named MyApplication with the myConfiguration.cfg file use

```
MyApplication.exe -config=myConfiguration.cfg

```

## Using the `application.cfg`


To configure your Kanzi application using `application.cfg`, create an `application.cfg` file that contains the parameter names and their values in:

- `<ProjectName>/Application Player` if you have a Kanzi Studio project without a C++ application
- `<ProjectName>/Application/bin` if you have a Kanzi Studio project with a C++ application


When you launch your Kanzi application, the application uses the parameters in the `application.cfg` to configure your application.
## Error handling for `application.cfg`


If an `application.cfg` is missing or is corrupted, Kanzi application logs a corresponding error message and continues to run with the default settings.

If you want to implement your own `application.cfg` error handling, you can create a custom logger to detect such errors. See Creating a custom logger.
## Running an application without reading the `application.cfg`


On some embedded platforms reading the `application.cfg` file can have a performance impact.

To run an application without reading the `application.cfg` file, on the command line launch your Kanzi application with the `-config=""` option.

For example, to run a Kanzi application named MyApplication without reading the `application.cfg` file use

```
MyApplication.exe -config=""

```

## Loading

### BinaryName


You can set which kzb file or kzb configuration file your Kanzi application loads when you launch your Kanzi application.

See Kzb files.
|

In `application.cfg` |

`BinaryName = "name"` |
|

In `Application::onConfigure` |

`configuration.binaryName = "name";` |
|

Value |
|

`name` |

Path to a single kzb file, or to the kzb configuration file that lists all the kzb files that your Kanzi application loads. |      |
|

`application.cfg` example |

```
# Loads the kzb file named my_application.kzb.
BinaryName = "my_application.kzb"

```


```
# Loads the kzb configuration file my_application.kzb.cfg that lists
# all the kzb files that your Kanzi application loads.
BinaryName = "my_application.kzb.cfg"

```
   |
|

`Application::onConfigure` example |

```
// Loads the kzb file named my_application.kzb.
configuration.binaryName = "my_application.kzb";

```


```
// Loads the kzb configuration file my_application.kzb.cfg that lists
// all the kzb files that your Kanzi application loads.
configuration.binaryName = "my_application.kzb.cfg";

```
   |
### FontEngine


You can set which font engine you want to load at application startup to render the text in your application:

- FreeType uses the FreeType rasterizer, HarfBuzz shaper, and ICU bidirectional library, and libunibreak for line breaking. This is the default font engine.
- iType uses the Monotype iType rasterizer and WorldTypeÂ® Shaperâ¢ for shaping.
- When you do not load a font engine, Kanzi does not render the text in your application.


When loading a font engine, keep in mind that:

- In a static build, you must statically link to the application the font engine that you want to load.
- In a dynamic build, Kanzi loads the font engine library.


You can also set which font engine you want the Kanzi Studio Preview to use to render text. See Setting the font engine for the Preview.
|

In `application.cfg` |

`FontEngine = fontEngine` |
|

In `Application::onConfigure` |

`configuration.fontEngine = fontEngine;` |
|

Values |
|

`fontEngine` |

The font engine that Kanzi loads at application startup.

To load the iType font engine:

- In `application.cfg` use `IType`.
- In `Application::onConfigure` use `ApplicationProperties::FontEngine::IType`.


To load the FreeType font engine (the default value):

- In `application.cfg` use `FreeType`. Default value.
- In `Application::onConfigure` use `ApplicationProperties::FontEngine::FreeType`. Default value.


To not load a font engine:

- In `application.cfg` use `None`.
- In `Application::onConfigure` use `ApplicationProperties::FontEngine::None`.


When you do not load a font engine, Kanzi does not render the text in your application.  |      |
|

`application.cfg` example |

```
# Load the iType font engine at application startup.
FontEngine = IType

```
   |
|

`Application::onConfigure` example |

```
// Load the iType font engine at application startup.
configuration.fontEngine = ApplicationProperties::FontEngine::IType;

```
   |
### Font engine dictionaries


You can customize how Kanzi iType font engine wraps words in Thai text by setting a Thai dictionary that you want to use instead of the one that is built into the iType font engine.

See Customizing word wrapping in Thai text with iType font engine.
|

In `application.cfg` |

`ITypeDictionaryUrls = fontEngineDictionaryUrls` |
|

In `Application::onConfigure` |

`configuration.fontEngineDictionaryUrls[fontEngine] = fontEngineDictionaryUrls` |
|

Values |
|

`fontEngineDictionaryUrls` |

Semicolon-separated list of URLs that point to dictionaries that you want to use. The order and format of dictionaries depends on the font engine that your application uses. See FontEngine. |
|

`fontEngine` |

The font engine for which to set the additional dictionaries. Kanzi supports only `ApplicationProperties::FontEngine::IType`. |      |
|

`application.cfg` example |

```
# Set additional backend dictionaries.
ITypeDictionaryUrls = file:///usr/share/itype/thai-dictionary.wtd

```
   |
|

`Application::onConfigure` example |

```
// Set additional backend dictionaries.
configuration.fontEngineDictionaryUrls[ApplicationProperties::FontEngine::IType] = "file:///usr/share/itype/thai-dictionary.wtd";

```
   |
### ModuleNames


You can set which plugins your Kanzi application loads when you launch your Kanzi application.
|

In `application.cfg` |

`ModuleNames= "names"` |
|

In `Application::onConfigure` |

`configuration.moduleNames = names;` |
|

Values |
|

`names` |

List of plugins to load. |      |
|

`application.cfg` example |

```
# Loads the plugin DLL files MyPlugin1.dll and MyPlugin2.dll.
ModuleNames = "MyPlugin1; MyPlugin2"

```
   |
|

`Application::onConfigure` example |

```
// Loads the plugin DLL files MyPlugin1.dll and MyPlugin2.dll.
configuration.moduleNames = {"MyPlugin1", "MyPlugin2"};

```
   |
### DeploymentQueueBudget


Kanzi keeps a queue of resources that are deployed on the UI thread. Use `DeploymentQueueBudget` to control the amount of time that Kanzi spends each frame to deploy resources. When many small resources are in the deployment queue, time budget greater than 0 can significantly decrease the time to load application resources.

The time budget does not set a hard limit on the total amount of time spent on resource deployment each frame. A long running deployment task can take longer than the allocated time.

When set to the default value of 0 milliseconds, Kanzi deploys each frame only one resource from the resource deployment queue.

See Balancing between UI responsiveness and resource loading.
|

In `application.cfg` |

`DeploymentQueueBudget = milliseconds` |
|

In `Application::onConfigure` |

`configuration.deploymentQueueBudget = milliseconds;` |
|

Values |
|

`milliseconds` |

Maximum number of milliseconds to spend on resource deployment each frame. The default value is 0. For Kanzi Android framework (droidfw) applications, the default value is 5. |      |
|

`application.cfg` example |

```
# Each frame Kanzi spends up to 2 milliseconds to deploy resources.
# Kanzi keeps deploying resources until it spends the allocated time budget
# for that frame.
DeploymentQueueBudget = 2

```
   |
|

`Application::onConfigure` example |

```
// Each frame Kanzi spends up to 2 milliseconds to deploy resources.
// Kanzi keeps deploying resources until it spends the allocated time budget
// for that frame.
configuration.deploymentQueueBudget = 2;

```
   |
### LoadingThreadCount


When users run your Kanzi application in an environment with a multi-core processor, Kanzi automatically uses multiple CPU cores to load the GPU resources in the kzb files to RAM.

See Loading resources in parallel.

GPU resources Kanzi loads in parallel include all types of textures, shaders, and meshes. To deploy these resources from RAM to GPU memory and to load prefab templates, Kanzi always uses the main thread. See Images and textures best practices, Shaders best practices, Meshes best practices.
|

In `application.cfg` |

`LoadingThreadCount = threads` |
|

In `Application::onConfigure` |

`configuration.loadingThreadCount = threads;` |
|

Values |
|

`threads` |

Number of CPU cores used for loading the resources. The default value is 3. |      |
|

`application.cfg` example |

```
# Switches off the use of multiple cores for loading your application.
# Loads your application resources using the main thread.
LoadingThreadCount = 0

```


```
# Uses six threads to load your application.
LoadingThreadCount = 5

```
   |
|

`Application::onConfigure` example |

```
// Switches off the use of multiple cores for loading your application.
// Loads your application resources using the main thread.
configuration.loadingThreadCount = 0;

```


```
// Uses six threads to load your application.
configuration.loadingThreadCount = 5;

```
   |
### MaxPendingResources


You can set the maximum number of resources that the loading threads process at the same time. By increasing the number of resources you can speed up the loading, but at the same time you increase the peak memory use during loading because you can load more resources to the memory before they are deployed to the GPU.
|

In `application.cfg` |

`MaxPendingResources = resources` |
|

In `Application::onConfigure` |

`configuration.maxPendingResources  = resources;` |
|

Values |
|

`resources` |

The maximum number of resources processed at the same time by the loading threads. The default value is 0 and sets the maximum number of resources to the number of loading threads +1. |      |
|

`application.cfg` example |

```
# Sets the maximum number of resources processed by the loading
# threads to the number of loading threads + 1. This is the default value.
MaxPendingResources = 0

```


```
# Sets the maximum number of resources processed by the loading
# threads to 20 resources.
MaxPendingResources = 20

```
   |
|

`Application::onConfigure` example |

```
// Sets the maximum number of resources processed by the loading
// threads to the number of loading threads + 1. This is the default value.
configuration.maxPendingResources = 0;

```


```
// Sets the maximum number of resources processed by the loading
// threads to 20 resources.
configuration.maxPendingResources = 20;

```
   |
## Performance

### ApplicationIdleState


Kanzi suspends the main loop when there is no input, tasks, timers, animations, or when there is nothing in the application that updates the rendering.

See Application idle state.

When using application idle state, consider that:

- If your Kanzi application is showing an animation, Kanzi by default throttles the CPU to the maximum FPS. If there are no animations, Kanzi sets the application to idle state. For this reason to conserve the CPU and power, Kanzi by default limits the maximum frame rate to 60 frames per second. Use the application configuration to set the maximum frame rate for your application.

See MaximumFPS.
- If your application relies on continuously executing some main loop tasks, such as functionality that you added to the main loop `UserStage`, disable the idle state.
- When your application is in idle state and the application makes changes to the render pass tree, Kanzi does not trigger the rendering to render the changes. To render the changes in such case, you must manually trigger the rendering by calling on any node the `Node::invalidateDraw` function.

|

In `application.cfg` |

`ApplicationIdleState = value` |
|

In `Application::onConfigure` |

`configuration.applicationIdleStateEnabled = value;` |
|

Values |
|

`0` |

Disable the application idle state. |
|

`1` |

Enable the application idle state. Default value. |      |
|

`application.cfg` example |

```
# Disables the application idle state.
ApplicationIdleState = 0

```
   |
|

`Application::onConfigure` example |

```
// Disables the application idle state.
configuration.applicationIdleStateEnabled = 0;

```
   |
### MaximumFPS


You can limit the number of frames rendered per second by setting the maximum frame rate.

If your Kanzi application is showing an animation, Kanzi by default throttles the CPU to the maximum FPS. If there are no animations, Kanzi sets the application to idle state. For this reason to conserve the CPU and power, Kanzi by default limits the maximum frame rate to 60 frames per second. Use the application configuration to set the maximum frame rate for your application.

See PerformanceInfoLevel.
|

In `application.cfg` |

`MaximumFPS = limit` |
|

In `Application::onConfigure` |

`configuration.frameRateLimit = limit;` |
|

Value |
|

`limit`  |

The maximum frame rate of the application in frames per second. |      |
|

`application.cfg` example |

```
# Sets the maximum application frame rate to 32 frames per second.
MaximumFPS = 32

```


```
# Disables the limit.
MaximumFPS = 0

```
   |
|

`Application::onConfigure` example |

```
// Sets the maximum application frame rate to 32 frames per second.
configuration.frameRateLimit = 32;

```


```
// Disables the limit.
configuration.frameRateLimit = 0;

```
   |
### PerformanceInfoLevel


You can enable the display of Performance HUD that shows the performance information for your Kanzi application. Use the Performance HUD to see how your application performs on target devices and to find performance bottlenecks.

Performance HUD shows this performance information for your Kanzi application:

- FPS shows the number of frames rendered every second.
- Last Frame shows this information for the last frame:

  - Main Loop Counter shows the number of times that the Kanzi main loop has run.
  - Time shows the time in milliseconds it took to render the frame.
  - Draw Count shows how many individual draw calls were executed.
  - Triangle Count shows an estimated total of individual triangles drawn during a frame.
  - Pipeline Count shows how many times a new render pipeline was bound for the last frame. See Reducing shader switches.
  - Pass Count shows how many render passes were used in the last frame. See Rendering best practices.
  - Memory Upload shows how many bytes of rolling staging memory were used on the last frame as well as the total buffer size. Staging memory contains uniform data and temporary storage used for updating GPU resources like vertex buffers or textures. On some platforms unique buffers are used for each type of data.
  - Dispatch Count shows how many compute dispatches were used in the last frame.
  - Timeline Clock shows the time in milliseconds it took to execute all animations in the application.

- Resource Memory Use shows an estimated amount of local GPU memory (VRAM) and non-local GPU memory (RAM) that your Kanzi application uses.

The values that the Performance HUD shows in the Kanzi Studio Preview and when you run the Kanzi application on a target device differ because Kanzi Studio loads and keeps in memory all resources in the application.
- Timer subscriptions shows the number of registered timer handlers in the `MessageDispatcher`. Too many timer handlers can decrease the performance of your application.

You can access the number of timer subscriptions in the Kanzi Engine API by calling `getSubscriptionCount()`.
- Animations shows the number of active and all animations in your Kanzi application.

You can access the number of animations in the Kanzi Engine API:

  - To get the number of active animations, use `getActiveTimelinePlaybackCount()`.
  - To get the number of all animations, use `getTimelinePlaybackCount()`.


You can set the position of the Performance HUD inside the window of your Kanzi application. See PerformanceInfoPosition.

See Best practices.
|

In `application.cfg` |

`PerformanceInfoLevel = level` |
|

In `Application::onConfigure` |

`configuration.performanceInfoLevel = ApplicationProperties::level;` |
|

Values |
|

`level` |

The level of display of performance information.

To disable the display of the Performance HUD:

- In `application.cfg` use `0`. Default value.
- In `Application::onConfigure` use `PerformanceInfoLevelDisabled`. Default value.


To enable the display of the frames rendered per second (FPS):

- In `application.cfg` use `1`.
- In `Application::onConfigure` use `PerformanceInfoLevelFPS`.


To enable the display of the full Performance HUD:

- In `application.cfg` use `2`.
- In `Application::onConfigure` use `PerformanceInfoLevelFull`.


To enable the display of the Kanzi graphics Performance HUD:

- In `application.cfg` use `3`.
- In `Application::onConfigure` use `PerformanceInfoLevelGraphics`.
  |      |
|

`application.cfg` example |

```
# Enables the full Performance HUD in a Kanzi application.
PerformanceInfoLevel = 2

```
   |
|

`Application::onConfigure` example |

```
// Enables the full Performance HUD in a Kanzi application.
configuration.performanceInfoLevel = ApplicationProperties::PerformanceInfoLevelFull;

```
   |
### PerformanceInfoPosition


You can set the position of the Performance HUD inside the window of your Kanzi application. To see the Performance HUD in the window of your Kanzi application, you must enable it. See PerformanceInfoLevel.
|

In `application.cfg` |

`PerformanceInfoPositionX = positionX`

`PerformanceInfoPositionY = positionY`  |
|

In `Application::onConfigure` |

`configuration.performanceInfoProperties.positionX = positionX;`

`configuration.performanceInfoProperties.positionY = positionY;`  |
|

Value |
|

`positionX` |

Horizontal position of the top-left corner of the Performance HUD from the top-left corner of a Kanzi application window. Use 0 to position the Performance HUD to the left of the window. |
|

`positionY` |

Vertical position of the top-left corner of the Performance HUD from the top-left corner of a Kanzi application window. Use 0 to position the Performance HUD to the top of the window. |      |
|

`application.cfg` example |

```
# Position the Performance HUD 100 pixels from the left side and
# 20 pixels from the top of the Kanzi application window.
PerformanceInfoPositionX = 100
PerformanceInfoPositionY = 20

```
   |
|

`Application::onConfigure` example |

```
// Position the Performance HUD 100 pixels from the left side and
// 20 pixels from the top of the Kanzi application window.
configuration.performanceInfoProperties.positionX = 100;
configuration.performanceInfoProperties.positionY = 20;

```
   |
### PerformanceInfoFontSize


You can set a font size for the Performance HUD.
|

In `application.cfg` |

`PerformanceInfoFontSize = fontSize` |
|

In `Application::onConfigure` |

`configuration.performanceInfoProperties.fontSize = fontSize;` |
|

Value |
|

`fontSize` |

You can set a font size in the range from 10 to 100. The default value is 12. |      |
|

`application.cfg` example |

```
# The font size of the Performance HUD is 20
PerformanceInfoFontSize = 20

```
   |
|

`Application::onConfigure` example |

```
// The font size of the Performance HUD is 20
configuration.performanceInfoProperties.fontSize = 20;

```
   |
### PerformanceInfoGraphFilter


You can choose which main loop tasks you want to show as graphs in the Performance HUD. For the names of the default main loop tasks, in the `application.hpp` see the implementation of `Application::initializeMainLoopTasks()`. To see the Performance HUD in the window of your Kanzi application, you must enable it. See PerformanceInfoLevel.
|

In `application.cfg` |

`PerformanceInfoGraphFilter = "category"` |
|

In `Application::onConfigure` |

`configuration.performanceInfoProperties.graphFilter = "category";` |
|

Value |
|

`category` |

The names of one or more main loop tasks separated by semicolons(;). |      |
|

`application.cfg` example |

```
# Enables graphs for tasks Render and MyCustomTask.
PerformanceInfoGraphFilter="Render;MyCustomTask"

```
   |
|

`Application::onConfigure` example |

```
// Enables graphs for tasks Render and MyCustomTask.
configuration.performanceInfoProperties.graphFilter="Render;MyCustomTask"

```
   |
### ProfilingCategoryFilter


You can control the state of performance profiling categories that you use to group performance profilers. See Measuring application performance and Measuring the loading and deployment time of resources.
|

In `application.cfg` |

`ProfilingCategoryFilter = "category=state"` |
|

In `Application::onConfigure` |

`configuration.profilingCategoryFilter = "category=state";` |
|

Values |
|

`category` |

The names of one or more profiling categories separated by pipes (|).

To set the state of all categories, use asterisk (*).  |
|

`state` |
|

`off` |

Disable performance profiling category. |
|

`on` |

Enable performance profiling category. |      |

Separate a list of category-state pairs with semicolons (;).  |
|

`application.cfg` examples |

```
# Enables the MyProfiler category and disables the MainLoopRendering category.
ProfilingCategoryFilter="MyProfiler=on;MainLoopRendering=off"

```


```
# Enables all performance profiling categories.
ProfilingCategoryFilter="*=on"

```


```
# Enables categories Generic and MyProfilingCategory.
ProfilingCategoryFilter="Generic|MyProfilingCategory=on"

```


```
# Enables resource profiling.
ProfilingCategoryFilter="ResourceLoading=on"

```
   |
|

`Application::onConfigure` examples |

```
# Enables the MyProfiler category and disables the MainLoopRendering category.
configuration.profilingCategoryFilter="MyProfiler=on;MainLoopRendering=off"

```


```
// Enables all performance profiling categories.
configuration.profilingCategoryFilter = "*=on";

```


```
// Enables categories Generic and MyProfilingCategory.
configuration.profilingCategoryFilter = "Generic|MyProfilingCategory=on";

```


```
// Enables resource profiling.
configuration.profilingCategoryFilter = "ResourceLoading=on";

```
   |

This table lists the Kanzi startup performance profiling categories and profilers that are included in the Profiling build.
|

Category |

Configuration name |

Profiler |
|

Application initialization |

`StartupInitialization` |

`StartupProfilerRegistry::m_initializationProfiler` |
|

Default resource registration |

`StartupRegisterDefaultResources` |

`StartupProfilerRegistry::m_registerDefaultResourcesProfiler` |
|

Graphics initialization |

`StartupInitializeGraphics` |

`StartupProfilerRegistry::m_initializeGraphicsProfiler` |
|

Startup kzb file opening |

`StartupOpenKzb` |

`StartupProfilerRegistry::m_openKzbProfiler` |
|

Loading threads initialization |

`StartupInitializeLoadingThreads` |

`StartupProfilerRegistry::m_initializeLoadingThreadsProfiler` |
|

Metadata registration |

`StartupRegisterMetadata` |

`StartupProfilerRegistry::m_registerMetadataProfiler` |
|

Plugins loading |

`StartupLoadPlugins` |

`StartupProfilerRegistry::m_loadPluginsProfiler` |
|

Prefabs loading |

`StartupLoadPrefab` |

`StartupProfilerRegistry::m_loadPrefabProfiler` |
|

Prefabs instantiation |

`StartupInstantiatePrefab` |

`StartupProfilerRegistry::m_instantiatePrefabProfiler` |
|

Prefabs attachment |

`StartupAttachPrefab` |

`StartupProfilerRegistry::m_attachPrefabProfiler` |
|

Renderer reset |

`StartupResetRenderer` |

`StartupProfilerRegistry::m_resetRendererProfiler` |
|

Runtime assets registration |

`StartupRegisterRuntimeAssets` |

`StartupProfilerRegistry::m_registerRuntimeAssetsProfiler` |
|

Domain initialization |

`StartupInitializeDomain` |

`StartupProfilerRegistry::m_initializeDomainProfiler` |
|

`Application::onProjectLoaded` |

`StartupOnProjectLoaded` |

`StartupProfilerRegistry::m_onProjectLoadedProfiler` |
|

`Application::initializeGL` |

`StartupInitializeGL` |

`StartupProfilerRegistry::m_initializeGLProfiler` |
|

`Application::resumeGL` |

`StartupResumeGL` |

`StartupProfilerRegistry::m_resumeGLProfiler` |
### MainLoopProfilingSampleBufferCount


You can set the sample buffer size of the main loop performance profiler that is included in the Profiling build. See Measuring the performance of Kanzi Engine and ProfilingCategoryFilter.
|

In `application.cfg` |

`MainLoopProfilingSampleBufferCount = samples` |
|

In `Application::onConfigure` |

`configuration.mainLoopProfilingSampleBufferCount = samples` |
|

Values |
|

`samples` |

Maximum number of samples in the buffer for the main loop performance profilers included in the Kanzi Profiling build. The default value is 1024. |      |
|

`application.cfg` example |

```
# Sets the maximum number of samples in main loop performance profilers
# to 3600.
MainLoopProfilingSampleBufferCount = 3600

```
   |
|

`Application::onConfigure` example |

```
// Sets the maximum number of samples in main loop performance profilers
// to 3600.
configuration.mainLoopProfilingSampleBufferCount = 3600;

```
   |
## Tracing

### TracingSampleMaxMemory


You can control the amount of memory used by the tracing system to store tracing data. A large value allows storing of more samples before overwriting.

Tracing is disabled for Release builds.
|

In `application.cfg` |

`TracingSampleMaxMemory = bytes` |
|

In `Application::onConfigure` |

`configuration.tracingConfiguration.sampleMaxMemory = bytes;` |
|

Value |
|

`bytes` |

The maximum bytes used by the tracing system. |      |
|

`application.cfg` example |

```
# Sets the Tracing system to use 8MB.
TracingSampleMaxMemory = 8388608

```
   |
|

`Application::onConfigure` example |

```
// Sets the Tracing system to use 8MB.
configuration.tracingConfiguration.sampleMaxMemory = 8388608;

```
   |
### TracingStartupInterval


You can set a startup interval to automatically write a trace file to the current working directory at startup. This option provides a convenient method to record the application startup performance.

Tracing is disabled for Release builds.
|

In `application.cfg` |

`TracingStartupInterval = interval` |
|

In `Application::onConfigure` |

`configuration.tracingConfiguration.startupInterval = interval;` |
|

Value |
|

`interval` |

The number of milliseconds to include in the startup trace. |      |
|

`application.cfg` example |

```
# Triggers a startup trace after 5 seconds.
TracingStartupInterval = 5000

```


```
# Disables writing a startup trace.
TracingStartupInterval = 0

```
   |
|

`Application::onConfigure` example |

```
// Triggers a startup trace after 5 seconds.
configuration.tracingConfiguration.startupInterval = chrono::milliseconds{ 5000 };

```


```
// Disables writing a startup trace.
configuration.tracingConfiguration.startupInterval = chrono::milliseconds{ 0 };

```
   |
### TracingTimeInterval


You can set the time interval when Kanzi writes a trace file on a recurring basis after writing the startup trace. At every expiration of the interval, Kanzi writes a trace file to the current working directory and overwrites the previous trace file.

Tracing is disabled for Release builds.
|

In `application.cfg` |

`TracingTimeInterval = interval` |
|

In `Application::onConfigure` |

`configuration.tracingConfiguration.recurringTimeInterval = interval;` |
|

Value |
|

`interval` |

The number of milliseconds to include in each recurring trace. |      |
|

`application.cfg` example |

```
# Triggers a recurring trace every 5 seconds.
TracingTimeInterval = 5000

```


```
# Disables writing a recurring trace.
TracingTimeInterval = 0

```
   |
|

`Application::onConfigure` example |

```
// Triggers a recurring trace every 5 seconds.
configuration.tracingConfiguration.recurringTimeInterval = chrono::milliseconds{ 5000 };

```


```
// Disables writing a recurring trace.
configuration.tracingConfiguration.recurringTimeInterval = chrono::milliseconds{ 0 };

```
   |
### TracingFrameInterval


You can set the frame interval when Kanzi writes a trace file on a recurring basis after writing the startup trace. At every expiration of the interval, Kanzi writes a trace file to the current working directory and overwrites the previous trace file.

In order to enable TracingFrameInterval option, TracingTimeInterval must be disabled.

Tracing is disabled for Release builds.
|

In `application.cfg` |

`TracingFrameInterval = interval` |
|

In `Application::onConfigure` |

`configuration.tracingConfiguration.recurringFrameInterval = interval;` |
|

Value |
|

`interval` |

The number of frames to include in each recurring trace. |      |
|

`application.cfg` example |

```
# Triggers a recurring trace every 1000 frames.
TracingFrameInterval = 1000

```


```
# Disables writing a recurring trace.
TracingFrameInterval = 0

```
   |
|

`Application::onConfigure` example |

```
// Triggers a recurring trace every 1000 frames.
configuration.tracingConfiguration.recurringFrameInterval = 1000;

```


```
// Disables writing a recurring trace.
configuration.tracingConfiguration.recurringFrameInterval = 0;

```
   |
## Glyph cache texture size


When you use a Text Block Kanzi creates a glyph cache texture for every font and font size combination. You can set the height and width of glyph cache textures to adjust the size of the glyph cache texture either when it gets full, or to optimize the performance of your Kanzi application.

Because larger glyph cache textures use more VRAM, try different sizes before you set the final size. The upper limit of the glyph cache texture size depends on the GPU, but usually it is 2048 by 2048 pixels. The default size of the glyph cache texture is 512 by 512 pixels.

Kanzi applies the size of the glyph cache texture to all glyph cache textures.

Because non-scalable fonts, such as color fonts with a CBDT table, contains non-scalable glyph data in relatively large resolution, Kanzi provides a separate set of options to configure a glyphâs cache size for such fonts. For non-scalable fonts the default size of the glyph cache texture is 768 by 768 pixels.
|

In `application.cfg` |

`GlyphCacheHeight = size`

`GlyphCacheWidth = size`

`GlyphCacheNonScalableHeight = size`

`GlyphCacheNonScalableWidth = size`  |
|

In `Application::onConfigure` |

`configuration.glyphCacheHeight = size;`

`configuration.glyphCacheWidth = size;`

`configuration.glyphCacheNonScalableHeight = size;`

`configuration.glyphCacheNonScalableWidth = size;`  |
|

Values |
|

`size` |

Size of the glyph cache texture in pixels. The default value is 512 for regular fonts, and 768 for non-scalable fonts. |      |
|

`application.cfg` example |

```
# Sets the glyph cache texture height to 768, and width to 1024 pixels.
GlyphCacheHeight = 768
GlyphCacheWidth = 1024

# Sets the glyph cache texture height to 1024, and width to 1280 pixels for non-scalable fonts.
GlyphCacheNonScalableHeight = 1024
GlyphCacheNonScalableWidth = 1280

```
   |
|

`Application::onConfigure` example |

```
// Sets the glyph cache texture height to 768, and width to 1024 pixels.
configuration.glyphCacheHeight = 768;
configuration.glyphCacheWidth = 1024;

// Sets the glyph cache texture height to 1024, and width to 1280 pixels for non-scalable fonts.
configuration.glyphCacheNonScalableHeight = 1024;
configuration.glyphCacheNonScalableWidth = 1280;

```
   |
## Optimization

### InitializePlatform


On the integrity_rcar_rwm_aarch64 platform you can set whether you want to initialize the application graphics. Use this approach only as a late-stage optimization when you want to manually synchronize the starting of multiple applications that initialize at the same time.

This configuration controls the initialization of the graphics driver, device window manager, and whether the display is switched on. When you disable this configuration, to enable your Kanzi application to create a window, in the same process you must initialize:

- `PVRGrfxServerInit()`
- `R_WM_DevInit()`
- (Optional) `R_WM_DevInfoGet()`
- (Optional) `R_WM_ScreenBgColorSet()`
- `R_WM_ScreenEnable()`
- Explicitly set the application window width and height. See Application window position and size.


When you disable graphics initialization with this configuration, you must initialize graphics for each application separately where you disabled this setting.
|

In `application.cfg` |

`InitializePlatform = value` |
|

In `Application::onConfigure` |

`configuration.defaultWindowProperties.initializePlatform  = value;` |
|

Values |
|

`0` |

Disable the graphics initialization. |
|

`1` |

Enable the graphics initialization. Default value. |      |
|

`application.cfg` example |

```
# Disables the graphics initialization.
InitializePlatform = 0

```
   |
|

`Application::onConfigure` example |

```
// Disables the graphics initialization.
configuration.defaultWindowProperties.initializePlatform = 0;

```
   |
### MmapMode


On operating systems that support it, you can set how Kanzi instructs the system to memory map files:

- Lazy mapping waits for your Kanzi application to access file contents before mapping that portion of the file.
- Eager mapping maps the whole file immediately.


The behavior of the application is identical between the two strategies, but you can choose when to pay the runtime cost of mapping a file.

By default Kanzi uses the default memory mapping strategy of the system.
|

In `application.cfg` |

`MmapMode = mode` |
|

In `Application::onConfigure` |

`configuration.mmapMode = mode` |
|

On the command line |

`-mmap=mode` |
|

Values |
|

`mode` |

Memory mapping strategy to use.

To use the system default:

- In `application.cfg` use `default`. Default value.
- In `Application::onConfigure` use `MmapMode::Default`. Default value.
- On the command line use `default`.


To use eager mapping:

- In `application.cfg` use `eager`.
- In `Application::onConfigure` use `MmapMode::Eager`.
- On the command line use `eager`.


To use lazy mapping:

- In `application.cfg` use `lazy`.
- In `Application::onConfigure` use `MmapMode::Lazy`.
- On the command line use `lazy`.


Command line settings take priority over `application.cfg`. When you specify multiple instances on the command line, Kanzi uses only the first one and ignores the others.  |      |
|

`application.cfg` example |

```
# Uses lazy memory mapping.
MmapMode = lazy

```
   |
|

`Application::onConfigure` example |

```
// Uses lazy memory mapping.
configuration.mmapMode = MmapMode::Lazy;

```
   |
## GPU resources

### HandleGPUResources


You can set how your Kanzi application handles in the paused state (`MainLoopState::Paused`) the GPU resources that are not stored in a kzb file.
|

In `application.cfg` |

`HandleGPUResources = handling` |
|

In `Application::onConfigure` |

`configuration.handleGPUResources = handling` |
|

Values |
|

`handling` |

The way to handle GPU resources in the paused state.

To do nothing (default value on all platforms except Android):

- In `application.cfg` use `none`.
- In `Application::onConfigure` use `ApplicationProperties::HandleGPUResources::NoHandling`.


To invalidate the GPU resources (default value on Android):

- In `application.cfg` use `invalidate`.
- In `Application::onConfigure` use `ApplicationProperties::HandleGPUResources::Invalidate`.


To destroy the GPU resources:

- In `application.cfg` use `destroy`.
- In `Application::onConfigure` use `ApplicationProperties::HandleGPUResources::Destroy`.
  |      |
|

`application.cfg` example |

```
# Invalidates the GPU resources.
HandleGPUResources = invalidate

```
   |
|

`Application::onConfigure` example |

```
// Invalidates the GPU resources.
configuration.handleGPUResources = ApplicationProperties::HandleGPUResources::Invalidate;

```
   |
## Graphics performance logging

### LogOpenGLExtensions


You can enable Kanzi to print to the debug console a list of the graphics-related extensions on application startup.
|

In `application.cfg` |

`LogOpenGLExtensions = value` |
|

In `Application::onConfigure` |

`configuration.extensionOutputEnabled = value;` |
|

Values |
|

`0` |

Disable the logging of the graphics-related extensions. Default value. |
|

`1` |

Enable the logging of the graphics-related extensions. |      |
|

`application.cfg` example |

```
# Enables the logging of the graphics-related extensions.
LogOpenGLExtensions = 1

```
   |
|

`Application::onConfigure` example |

```
// Enables the logging of the graphics-related extensions.
configuration.extensionOutputEnabled = 1;

```
   |
### LogOpenGLInformation


You can enable Kanzi to print to the debug console this graphics-related information on application startup:

- GL vendor
- GL renderer
- GL version
- Shading language version

|

In `application.cfg` |

`LogOpenGLInformation = value` |
|

In `Application::onConfigure` |

`configuration.informationOutputEnabled = value;` |
|

Values |
|

`0` |

Disable the logging of the graphics-related information. Default value. |
|

`1` |

Enable the logging of the graphics-related information. |      |
|

`application.cfg` example |

```
# Enables the logging of the graphics-related information.
LogOpenGLInformation = 1

```
   |
|

`Application::onConfigure` example |

```
// Enables the logging of the graphics-related information.
configuration.informationOutputEnabled = 1;

```
   |
### LogSurfaceInformation


You can enable Kanzi to print to the debug console these graphics-related properties on application startup:

- Requested and acquired surface properties. See Surface properties.
- Size of the entire desktop and each display.
- Size of the application window. See Application window position and size.

|

In `application.cfg` |

`LogSurfaceInformation = value` |
|

In `Application::onConfigure` |

`configuration.propertyOutputEnabled = value;` |
|

Values |
|

`0` |

Disable the logging of the graphics-related properties. Default value. |
|

`1` |

Enable the logging of the graphics-related properties. |      |
|

`application.cfg` example |

```
# Enables the logging of the graphics-related properties.
LogSurfaceInformation = 1

```
   |
|

`Application::onConfigure` example |

```
// Enables the logging of the graphics-related properties.
configuration.propertyOutputEnabled = 1;

```
   |
## QNX system logger (slogger2)


On QNX you can use the QNX system logger (slogger2) to write log messages. When you redirect log messages to slogger2, your Kanzi application continues writing the log messages to the default logger.

A Kanzi application does not use the default slogger2 buffer, which allows you to use `slog2_set_default_buffer`. Kanzi provides slogger2 that supports logging to only one slogger2 buffer. When slogger2 stops logging, Kanzi calls `slog2_reset`. To change this behavior, see: Cleaning up after slogger2.

Keep in mind that slogger2 initializes after Kanzi reads the configuration for your Kanzi application. For this reason the slogger2 logs do not contain the log messages before that time.

To use slogger2, you can either:

- Configure slogger2 in the `application.cfg` or `Application::onConfigure`.
- Provide a custom slogger2 buffer to the Kanzi logger. See customSlog2Buffer.

### QnxEnableSlogger2


Before you can use slogger2 with your Kanzi application, you must enable it.
|

In `application.cfg` |

`QnxEnableSlogger2 = value` |
|

In `Application::onConfigure` |

`configuration.slog2Config.enabled = value` |
|

Values |
|

`true` |

Enable slogger2. |
|

`false` |

Disable slogger2. Default value. |      |
|

`application.cfg` example |

```
# Enable logging to slogger2.
QnxEnableSlogger2 = true

```
   |
|

`Application::onConfigure` example |

```
// Enable logging to slogger2.
configuration.slog2Config.enabled = true;

```
   |
### QnxSlogger2VerbosityLevel


You can set which log messages you want slogger2 to log. The Kanzi application configuration verbosity levels map to the slogger2 log verbosity levels.
|

In `application.cfg` |

`QnxSlogger2VerbosityLevel = value` |
|

In `Application::onConfigure` |

`configuration.slog2Config.verbosityLevel = Slog2VerbosityLevel::value` |
|

Values |
|

`Slog2Shutdown` |

Maps to the slogger2 level `SLOG2_SHUTDOWN`. |
|

`Slog2Critical` |

Maps to the slogger2 level `SLOG2_CRITICAL`. |
|

`Slog2Error` |

Maps to the slogger2 level `SLOG2_ERROR`. |
|

`Slog2Warning` |

Maps to the slogger2 level `SLOG2_WARNING`. |
|

`Slog2Notice` |

Maps to the slogger2 level `SLOG2_NOTICE`. |
|

`Slog2Info` |

Maps to the slogger2 level `SLOG2_INFO`. |
|

`Slog2Debug1` |

Maps to the slogger2 level `SLOG2_DEBUG1`. |
|

`Slog2Debug2` |

Maps to the slogger2 level `SLOG2_DEBUG2`. Default value. |      |
|

`application.cfg` example |

```
# Sets the slogger2 log level to SLOG2_INFO.
QnxSlogger2VerbosityLevel = Slog2Info

```
   |
|

`Application::onConfigure` example |

```
// Sets the slogger2 log level to SLOG2_INFO.
configuration.slog2Config.verbosityLevel = Slog2VerbosityLevel::Slog2Info;

```
   |
### QnxSlogger2MaxRetries


On QNX versions 7.0.4 and newer you can limit the amount of times slogger2 retries to obtain a buffer.

When you set this limit and slogger2 reaches it, Kanzi drops the log message and increases the dropped message count. You can see the number of dropped messages in the slogger2 logs in the next non-dropped log entry of the variable `code` written before the log message.
|

In `application.cfg` |

`QnxSlogger2MaxRetries = value` |
|

In `Application::onConfigure` |

`configuration.slog2Config.maxRetries = value` |
|

Values |
|

`value` |

uint32_t value that sets the limit. By default a Kanzi application sets this to `Slog2UnlimitedRetries` (`UINT32_MAX`). This means that the number of retries is not limited. |      |
|

`application.cfg` example |

```
# Set the retry limit to 10 retries.
QnxSlogger2MaxRetries = 10

```
   |
|

`Application::onConfigure` example |

```
// Set the retry limit to 10 retries.
configuration.slog2Config.maxRetries = 10;

```
   |
### pageCount


You can set the multiple of 4KB pages that the QNX logger acquires for the internal slogger2 buffer.
|

In `Application::onConfigure` |

`configuration.slog2Config.pageCount = value` |
|

Values |
|

`value` |

Integer value for the number of pages to allocate for the slogger2 buffer. The default is 8. |      |
|

`Application::onConfigure` example |

```
// For example, when you set the slogger2 verbosity level to
// SLOG2_ERROR slogger2 writes to log less frequently
// (low rate logging), and by decreasing the page count
// you can increase the logging pace.
configuration.slog2Config.pageCount = 1;

```
   |
### customSlog2Buffer


Kanzi enables you to register a custom slogger2 buffer and pass it to a Kanzi application. Your Kanzi application then uses the buffer to write logs. For example, you can register a custom slogger2 buffer when you want to give the buffer a custom name or if you want to set any of the properties from the `slog2_buffer_set_config_t` structure passed to `slog2_register`. See QNX system logger (slogger2).
## Graphics library


On the Windows operating system you can select whether you want to use OpenGL ES, OpenGL, or Vulkan in the `Application::onConfigure` function, in the `application.cfg`, or using the command line arguments, if your target supports command line arguments.

On the command line use:

- `--gles` or `--opengles` to use OpenGL ES
- `--gl` or `--opengl` to use OpenGL
- `--vk` or `--vulkan` to use Vulkan
- `--egl` to use EGL
- `--wgl` to use WGL
- `--glx` to use GLX

|

In `application.cfg` |

`SurfaceClientAPI = clientApi`

`GraphicsContextAPI = contextApi`  |
|

In `Application::onConfigure` |

`configuration.defaultSurfaceProperties.clientAPI = clientApi;`

`configuration.defaultSurfaceProperties.contextAPI = contextApi;`  |
|

Values |
|

`clientApi` |

To use OpenGL ES:

- In `application.cfg` use `gles` or `opengles`.
- In `Application::onConfigure` use `SurfaceClientAPI::OpenGLES`.


To use OpenGL:

- In `application.cfg` use `gl` or `opengl`.
- In `Application::onConfigure` use `SurfaceClientAPI::OpenGL`.


To use Vulkan:

- In `application.cfg` use `vk` or `vulkan`.
- In `Application::onConfigure` use `SurfaceClientAPI::Vulkan`.
  |
|

`contextApi` |

To use WGL:

- In `application.cfg` use `wgl`.
- In `Application::onConfigure` use `GraphicsContextAPI::WGL`.


To use EGL:

- In `application.cfg` use `egl`.
- In `Application::onConfigure` use `GraphicsContextAPI::EGL`.


To use GLX:

- In `application.cfg` use `glx`.
- In `Application::onConfigure` use `GraphicsContextAPI::GLX`.
  |      |
|

`application.cfg` example |

```
# Sets the surface target for OpenGL rendering and WGL graphics context.
SurfaceClientAPI = gl
GraphicsContextAPI = wgl

```
   |
|

`Application::onConfigure` example |

```
// Sets the surface target for OpenGL rendering and WGL graphics context.
configuration.defaultSurfaceProperties.clientAPI = SurfaceClientAPI::OpenGL;
configuration.defaultSurfaceProperties.contextAPI = GraphicsContextAPI::WGL;

```
   |
### GraphicsStatisticEnabled


You can enable the statistics layer for the Kanzi graphics library of your application. The statistics layer is always enabled in the debug mode, regardless of the configuration. The statistics layer shows the information about the Kanzi graphics objects in the Performance HUD. See Showing the performance measurement graphs in the Performance HUD.
|

In `application.cfg` |

`GraphicsStatisticsEnabled = value` |
|

In `Application::onConfigure` |

`configuration.graphicsStatisticsEnabled = value;` |
|

On the command line |

`--graphics-statistics` |
|

Values |
|

`value` |

Whether to enable the statistics layer for the Kanzi graphics library:

- `0` disables the statistics layer. Default value.
- `1` enables the statistics layer.
  |      |
|

`application.cfg` example |

```
# Enables the statistics layer for the Kanzi graphics library.
GraphicsStatisticsEnabled = 1

```
   |
|

`Application::onConfigure` example |

```
// Enables the statistics layer for the Kanzi graphics library.
configuration.graphicsStatisticsEnabled = 1;

```
   |
|

Command line example |

Enables the statistics layer for the Kanzi graphics library.

```
--graphics-statistics

```
   |
### GraphicsValidationEnabled


You can enable the validation layer for the Kanzi graphics library of your application. The validation layer is always enabled in the debug mode, regardless of the configuration. Use the information in the validation layer to check whether your application correctly uses the graphics API. Kanzi shows validation errors in the default console.
|

In `application.cfg` |

`GraphicsValidationEnabled = value` |
|

In `Application::onConfigure` |

`configuration.graphicsValidationEnabled = value;` |
|

On the command line |

`--graphics-validation` |
|

Values |
|

`value` |

Whether to enable the validation layer for the Kanzi graphics library:

- `0` disables the validation layer. Default value.
- `1` enables the validation layer.
  |      |
|

`application.cfg` example |

```
# Enables the validation layer for the Kanzi graphics library.
GraphicsValidationEnabled = 1

```
   |
|

`Application::onConfigure` example |

```
// Enables the validation layer for the Kanzi graphics library.
configuration.graphicsValidationEnabled = 1;

```
   |
|

Command line example |

Enables the validation layer for the Kanzi graphics library.

```
--graphics-validation

```
   |
## Surface properties


Surface properties control the properties of the hardware-accelerated graphics surface onto which Kanzi renders. They control the relation between image quality and rendering speed.

The surface properties that you set are considered requests to be matched by the graphics system of the target hardware. Whether a given request is considered an upper bound, a lower bound, or an exact value, is platform-dependent.

To get the platform-dependent default values of surface properties, call `kzsSurfaceGetDefaultProperties()`.
### Color format


You can set the sizes of the RGB color channels and the alpha channel in bits.
|

In `application.cfg` |

`SurfaceBitsRed = red`

`SurfaceBitsGreen = green`

`SurfaceBitsBlue = blue`

`SurfaceBitsAlpha = alpha`  |
|

In `Application::onConfigure` |

`configuration.defaultSurfaceProperties.bitsColorR = red;`

`configuration.defaultSurfaceProperties.bitsColorG = green;`

`configuration.defaultSurfaceProperties.bitsColorB = blue;`

`configuration.defaultSurfaceProperties.bitsAlpha = alpha;`  |
|

Values |
|

`red` |

Size of the red color channel in bits. |
|

`green` |

Size of the green color channel in bits. |
|

`blue` |

Size of the blue color channel in bits. |
|

`alpha` |

Size of the alpha channel in bits. |

The default size of each channel is 8 bits.

To let the platform choose the value, use `"unspecified"`.  |
|

`application.cfg` example |

```
# Set the sizes of the color and alpha channels for a typical
# high-speed rendering application.
SurfaceBitsRed = 5
SurfaceBitsGreen = 6
SurfaceBitsBlue = 5
SurfaceBitsAlpha = 0

```


```
# Let the platform choose the sizes of the color and alpha channels.
SurfaceBitsRed = "unspecified"
SurfaceBitsGreen = "unspecified"
SurfaceBitsBlue = "unspecified"
SurfaceBitsAlpha = "unspecified"

```
   |
|

`Application::onConfigure` example |

```
// Set the sizes of the color and alpha channels for a typical
// high-speed rendering application.
configuration.defaultSurfaceProperties.bitsColorR = 5;
configuration.defaultSurfaceProperties.bitsColorG = 6;
configuration.defaultSurfaceProperties.bitsColorB = 5;
configuration.defaultSurfaceProperties.bitsAlpha = 0;

```


To let the platform choose the color and alpha channel sizes:

- For Android WS, Emscripten, QNX EGL, Wayland EGL, or X11 EGL graphics output:

```
configuration.systemConfiguration[ConfigurationKeyDefaultSurfaceBitsRed] = "unspecified";
configuration.systemConfiguration[ConfigurationKeyDefaultSurfaceBitsGreen] = "unspecified";
configuration.systemConfiguration[ConfigurationKeyDefaultSurfaceBitsBlue] = "unspecified";
configuration.systemConfiguration[ConfigurationKeyDefaultSurfaceBitsAlpha] = "unspecified";

```

- For other graphics outputs:

```
configuration.defaultSurfaceProperties.bitsColorR = KZS_SURFACE_PROPERTY_DONT_CARE;
configuration.defaultSurfaceProperties.bitsColorG = KZS_SURFACE_PROPERTY_DONT_CARE;
configuration.defaultSurfaceProperties.bitsColorB = KZS_SURFACE_PROPERTY_DONT_CARE;
configuration.defaultSurfaceProperties.bitsAlpha = KZS_SURFACE_PROPERTY_DONT_CARE;

```

  |
### SurfaceBitsStencil


You can set the size of the stencil buffer in bits.
|

In `application.cfg` |

`SurfaceBitsStencil = bufferSize` |
|

In `Application::onConfigure` |

`configuration.defaultSurfaceProperties.bitsStencil = bufferSize;` |
|

Values |
|

`bufferSize` |

Size of the stencil buffer in bits.

The default value is 8 bits.

To let the platform choose the value, use `"unspecified"`.  |      |
|

`application.cfg` example |

```
# Set the size of the stencil buffer to one bit.
SurfaceBitsStencil = 1

```


```
# Let the platform choose the size of the stencil buffer.
SurfaceBitsStencil = "unspecified"

```
   |
|

`Application::onConfigure` example |

```
// Set the size of the stencil buffer to one bit.
configuration.defaultSurfaceProperties.bitsStencil = 1;

```


To let the platform choose the size of the stencil buffer:

- For Android WS, Emscripten, QNX EGL, Wayland EGL, or X11 EGL graphics output:

```
configuration.systemConfiguration[ConfigurationKeyDefaultSurfaceBitsStencil] = "unspecified";

```

- For other graphics outputs:

```
configuration.defaultSurfaceProperties.bitsStencil = KZS_SURFACE_PROPERTY_DONT_CARE;

```

  |
### SurfaceBitsDepthBuffer


You can set the size of the depth buffer in bits.
|

In `application.cfg` |

`SurfaceBitsDepthBuffer = bufferSize` |
|

In `Application::onConfigure` |

`configuration.defaultSurfaceProperties.bitsDepthBuffer = bufferSize;` |
|

Values |
|

`bufferSize` |

Size of the depth buffer in bits.

The default value is 24 bits.

To let the platform choose the value, use `"unspecified"`.  |      |
|

`application.cfg` example |

```
# Set the size of the depth buffer to 16 bits.
SurfaceBitsDepthBuffer = 16

```


```
# Let the platform choose the size of the depth buffer.
SurfaceBitsDepthBuffer = "unspecified"

```
   |
|

`Application::onConfigure` example |

```
// Set the size of the depth buffer to 16 bits.
configuration.defaultSurfaceProperties.bitsDepthBuffer = 16;

```


To let the platform choose the size of the depth buffer:

- For Android WS, Emscripten, QNX EGL, Wayland EGL, or X11 EGL graphics output:

```
configuration.systemConfiguration[ConfigurationKeyDefaultSurfaceBitsDepth] = "unspecified";

```

- For other graphics outputs:

```
configuration.defaultSurfaceProperties.bitsDepthBuffer = KZS_SURFACE_PROPERTY_DONT_CARE;

```

  |
### SurfaceBitsPadding


On QNX, you can set the size of the padding in bits to add to the color format of the Kanzi application window.
|

In `application.cfg` |

`SurfaceBitsPadding = padding` |
|

In `Application::onConfigure` |

`configuration.defaultSurfaceProperties.bitsPadding = padding;` |
|

Values |
|

`padding` |

Size of the padding in bits to add to the color format of the application window.

By default, Kanzi lets the platform choose the size.  |      |
|

`application.cfg` example |

```
# Set the size of the padding to 2 bits.
SurfaceBitsPadding = 2

```
   |
|

`Application::onConfigure` example |

```
// Set the size of the padding to 2 bits.
configuration.defaultSurfaceProperties.bitsPadding = 2;

```
   |
### SurfaceColorSpace


You can enable the initialization of OpenGL for the hardware that displays your Kanzi application.
|

In `application.cfg` |

`SurfaceColorSpace = colorSpace` |
|

In `Application::onConfigure` |

`configuration.defaultSurfaceProperties.colorSpace = colorSpace;` |
|

On the command line |

`-surface-color-space=colorSpace` |
|

Values |
|

`colorSpace` |

Enables the initialization of OpenGL for the hardware that displays the application.

- To use the sRGB color space:

  - In `application.cfg` use `"srgb"`.
  -  In `Application::onConfigure` use `SurfaceColorSpace::sRGB`.
  - On the command line use `srgb`.


Use this option when your application uses the linear color workflow, where Kanzi performs operations on color values in linear color space.

The linear color workflow requires:

  - OpenGL extension GL_EXT_sRGB
  - EGL version 1.5 or later, or EGL version 1.4 with the EGL_KHR_gl_colorspace extension


When you use the sRGB color space, Kanzi expects that in the Kanzi Studio project properties the Color Workflow property is set to Linear.

See Using the linear color workflow.
- To use an unspecified color space:

  - In `application.cfg` use `"standard"`.
  - In `Application::onConfigure` use `SurfaceColorSpace::Standard`.
  - On the command line use `standard`.


This is the default.

Use this option when your application uses the standard color workflow, where Kanzi performs operations on color values in the nonlinear gamma color space.

When you use an unspecified color space, Kanzi expects that in the Kanzi Studio project properties the Color Workflow property is set to Standard (default value).

See Using the standard color workflow.
- To pass the shader output directly to the graphics surface:

  - In `application.cfg` use `"passthrough"`.
  -  In `Application::onConfigure` use `SurfaceColorSpace::Passthrough`.
  - On the command line use `passthrough`.


Use this option when you want to perform custom gamma correction for the target display.

Kanzi does not perform automatic output conversion on shader writes, but instead expects the shaders to perform a custom color space conversion.

When you use a custom color space, Kanzi expects that in the Kanzi Studio project properties the Color Workflow property is set to Linear.
  |      |
|

`application.cfg` example |

```
# Set your application to use an unspecified color space.
SurfaceColorSpace = "standard"

```
   |
|

`Application::onConfigure` example |

```
// Set your application to use an unspecified color space.
configuration.defaultSurfaceProperties.colorSpace = "standard";

```
   |
|

Command line example |

Set your application to use an unspecified color space.

```
-surface-color-space=standard

```
   |

See Color workflow.
### SurfaceSamplesAntialiasing


You can set the number of surface samples to use for anti-aliasing.
|

In `application.cfg` |

`SurfaceSamplesAntialiasing = samples` |
|

In `Application::onConfigure` |

`configuration.defaultSurfaceProperties.antiAliasing = samples;` |
|

Values |
|

`samples` |

The number of anti-aliasing surface samples to use.

By default:

- On Windows, the Kanzi Studio Preview and the Kanzi Application Player apply anti-aliasing using 4 samples. See Setting anti-aliasing in the Preview and Application Player.
- On other platforms, Kanzi lets the platform choose the number of anti-aliasing samples.
  |      |
|

`application.cfg` example |

```
# Set the number of anti-aliasing samples to 4.
SurfaceSamplesAntialiasing = 4

```
   |
|

`Application::onConfigure` example |

```
// Set the number of anti-aliasing samples to 4.
configuration.defaultSurfaceProperties.antiAliasing = 4;

```
   |
### SwapBehavior


You can set whether to swap or copy buffers during buffer swap.
|

In `application.cfg` |

`SwapBehavior = swap` |
|

In `Application::onConfigure` |

`configuration.defaultSurfaceProperties.swapBehaviorCopy = swap;` |
|

Values |
|

`swap` |

Sets whether to swap or copy buffers during buffer swap.

To let Kanzi automatically select whether to copy or swap the buffers, in `Application::onConfigure` use `SwapBehavior::Unspecified`. This is the default value.

To copy the buffers:

- In `application.cfg` use `"copy"`.
- In `Application::onConfigure` use `SwapBehavior::Copy`.


To swap the buffers:

- In `application.cfg` use `"exchange"`.
- In `Application::onConfigure` use `SwapBehavior::Exchange`.
  |      |
|

`application.cfg` example |

```
# Copy buffers during buffer swap.
SwapBehavior = "copy"

```
   |
|

`Application::onConfigure` example |

```
// Copy buffers during buffer swap.
configuration.defaultSurfaceProperties.swapBehaviorCopy = SwapBehavior::Copy;

```
   |
### PresentMode


You can set the surface present mode. Not all platforms support this setting.
|

In `application.cfg` |

`PresentMode = mode` |
|

In `Application::onConfigure` |

`configuration.defaultSurfaceProperties.presentMode = mode;` |
|

Values |
|

`mode` |

Sets the surface present mode.

- To queue and swap buffers in the order given during the VBLANK interval.

  - In `application.cfg` use `fifo`. Default value.
  - In `Application::onConfigure` use `platform::PresentMode::FIFO`. Default value.

- To swap buffers at any time. Tearing can occur.

  - In `application.cfg` use `immediate`.
  - In `Application::onConfigure` use `platform::PresentMode::Immediate`.

- To set `FIFORelaxed` mode. Similar to FIFO, but if no image is available, the next image is immediate. This option prefers tearing over showing a stale image.

  - In `application.cfg` use `fiforelaxed`.
  - In `Application::onConfigure` use `platform::PresentMode::FIFORelaxed`.

- To set `Mailbox` mode. Similar to FIFO, but only a single surface is in the queue. If the second surface is prepared before the next VBLANK, replaces the surface.

  - In `application.cfg` use `mailbox`.
  - In `Application::onConfigure` use `platform::PresentMode::Mailbox`.

  |      |
|

`application.cfg` example |

```
# Swap buffers at any time.
PresentMode = immediate

```
   |
|

`Application::onConfigure` example |

```
// Swap buffers at any time.
configuration.defaultSurfaceProperties.presentMode = kanzi::platform::PresentMode::Immediate;

```
   |
### EGLIMGContextPriority


You can create an EGL IMG context with a priority hint. By default, Kanzi lets the platform choose the priority.
|

In `application.cfg` |

`EGLIMGContextPriority = priority` |
|

In `Application::onConfigure` |

`configuration.defaultSurfaceProperties.priority = priority;` |
|

On the command line |

`-egl-img-context-priority=priority` |
|

Values |
|

`priority` |

Enables the creation of an EGL IMG context with a priority hint.

By default, Kanzi lets the platform choose the priority.

To set low priority:

- In `application.cfg` use `"low"`.
-  In `Application::onConfigure` use `EGLIMGContextPriority::Low`.
- On the command line use `low`.


To set medium priority:

- In `application.cfg` use `"medium"`.
- In `Application::onConfigure` use `EGLIMGContextPriority::Medium`.
- On the command line use `medium`.


To set high priority:

- In `application.cfg` use `"high"`.
-  In `Application::onConfigure` use `EGLIMGContextPriority::High`.
- On the command line use `high`.
  |      |
|

`application.cfg` example |

```
# Set the EGL IMG context priority to high.
EGLIMGContextPriority = "high"

```


```
# Let the platform choose the EGL IMG context priority.
EGLIMGContextPriority = "unspecified"

```
   |
|

`Application::onConfigure` example |

```
// Set the EGL IMG context priority to high.
configuration.defaultSurfaceProperties.priority = EGLIMGContextPriority::High;

```


To let the platform choose the EGL IMG context priority:

- For Android WS, Emscripten, QNX EGL, or X11 EGL graphics output:

```
configuration.systemConfiguration[ConfigurationKeyEGLIMGContextPriority] = "unspecified";

```

- For other graphics outputs:

```
configuration.defaultSurfaceProperties.priority = KZS_SURFACE_PROPERTY_DONT_CARE;

```

  |
|

Command line example |

Set the EGL IMG context priority to high.

```
-egl-img-context-priority=high

```
   |
## Application window position and size


You can set the position of your Kanzi application on the screen relative to the upper-left corner of the screen and the size of the application window in pixels. The default size of the window is 640x480 pixels and center of the device screen.

To make the application window fixed size, resizable, fullscreen, or without borders, see WindowStyle.

To set the default display where the application window appears, see DefaultDisplayIndex.
|

In `application.cfg` |

`WindowX = positionX`

`WindowY = positionY`

`WindowWidth = width`

`WindowHeight = height`

`WindowOrder = order`  |
|

In `Application::onConfigure` |

`configuration.defaultWindowProperties.x = positionX;`

`configuration.defaultWindowProperties.y = positionY;`

`configuration.defaultWindowProperties.width = width;`

`configuration.defaultWindowProperties.height = height;`

`configuration.defaultWindowProperties.order = order;`

`configuration.systemConfiguration[ConfigurationKeyDefaultWindowX] = "positionX";`

`configuration.systemConfiguration[ConfigurationKeyDefaultWindowY] = "positionY";`

`configuration.systemConfiguration[ConfigurationKeyDefaultWindowWidth] = "width";`

`configuration.systemConfiguration[ConfigurationKeyDefaultWindowHeight] = "height";`

`configuration.systemConfiguration[ConfigurationKeyDefaultWindowOrder] = "order";`  |
|

Value |
|

`positionX` |

Horizontal position of the top-left corner of the application window from the top-left corner of the screen in pixels. Use 0 to position the window to the left of the device screen. |
|

`positionY` |

Vertical position of the top-left corner of the application window from the top-left corner of the screen in pixels. Use 0 to position the window to the top of the device screen. |
|

`width` |

Window width in pixels. |
|

`height` |

Window height in pixels. |
|

`order` |

Z-order of the application window in decimal or hexadecimal format. You can use this parameter to arrange Kanzi applications when you run more than one application at the same time. The values for this parameter depend on your target platform. By default Kanzi sets the value to `NativeWindowProperties::WindowPositionSpecifiers::WindowPositionUnspecified`, which does not set order. |      |
|

`application.cfg` example |

```
# Sets the width to 1280 and height to 720 pixels and place it 100 pixels
# from the top and 1 pixel from the left side of the device screen.
WindowWidth = 1280
WindowHeight = 720
WindowX = 100
WindowY = 1

```


```
# Places the application window in the top-left corner of the device screen.
WindowX = 0
WindowY = 0

```


```
# Sets the window order to 0.
WindowOrder = 0

```


```
# Sets the window order to 0xff.
WindowOrder = 0xff

```
   |
|

`Application::onConfigure` example |

```
// Sets the width to 1280 and height to 720 pixels and place it 100 pixels
// from the top and 1 pixel from the left side of the device screen.
configuration.defaultWindowProperties.width = 1280;
configuration.defaultWindowProperties.height = 720;
configuration.defaultWindowProperties.x = 100;
configuration.defaultWindowProperties.y = 1;

```


```
// Places the application window in the top-left corner of the device screen.
configuration.defaultWindowProperties.x = 0;
configuration.defaultWindowProperties.y = 0;

```


```
// Sets the window order to 0.
configuration.defaultWindowProperties.order = 0;
configuration.systemConfiguration[ConfigurationKeyDefaultWindowOrder] = "0";

```


```
// Sets the window order to 0xff.
configuration.defaultWindowProperties.order = 0xff;
configuration.systemConfiguration[ConfigurationKeyDefaultWindowOrder] = "0xff";

```
   |
### WindowClassName


You can set window class name for QNX and Win32 platforms.
|

In `application.cfg` |

`WindowClassName = "name"` |
|

In `Application::onConfigure` |

For the legacy graphics output.

`configuration.defaultWindowProperties.groupName = "name";`

For the new graphics output.

`configuration.systemConfiguration[ConfigurationKeyDefaultWindowClassName] = "name";`  |
|

On the command line |

`-window-class-name="name"` |
|

`application.cfg` example |

```
# Sets the window class name to "kanzi" for the legacy and new graphics outputs.
WindowClassName = "kanzi"

```
   |
|

`Application::onConfigure` example |

```
// Sets the window class name to "kanzi" for the legacy graphics output.
configuration.defaultWindowProperties.groupName = "kanzi";

```


```
// Sets the window class name for the new graphics output.
configuration.systemConfiguration[ConfigurationKeyDefaultWindowClassName] = "kanzi";

```
   |
|

Command line example |

Sets the window class name to `kanzi` for the legacy and new graphics outputs.

```
-window-class-name="kanzi"

```
   |
### Window title


You can set Kanzi window title. The default window title is âKanziâ.
|

In `application.cfg` |

`WindowTitle = windowTitle` |
|

In `Application::onConfigure` |

`configuration.systemConfiguration[ConfigurationKeyDefaultWindowTitle] = windowTitle;` |
|

On the command line |

`-window-title=windowTitle` |
|

`application.cfg` example |

```
# Sets "kanzi" as window title.
WÃ­ndowTitle = kanzi

```
   |
|

`Application::onConfigure` example |

```
// Sets "kanzi" as window title.
configuration.systemConfiguration[ConfigurationKeyDefaultWindowTitle] = "kanzi";

```
   |
|

Command line example |

Sets âkanziâ as window title.

```
-window-title=kanzi

```
   |
## Graphics card selection

### DeviceIdentifier


On the platforms that use the GBM windowing system, you can set which graphics card you want your Kanzi application to use.
|

In `application.cfg` |

`DeviceIdentifier = identifier` |
|

In `Application::onConfigure` |

`configuration.defaultDesktopProperties.deviceIdentifier = identifier;` |
|

Value |
|

`identifier` |

Identifier of the graphics card that you want your Kanzi application to use. Default value for GBM is `/dev/dri/card0`. |      |
|

`application.cfg` example |

```
# Sets Kanzi to use the graphics card at /dev/dri/card1.
DeviceIdentifier = /dev/dri/card1

```
   |
|

`Application::onConfigure` example |

```
// Sets Kanzi to use the graphics card at /dev/dri/card1.
configuration.defaultDesktopProperties.deviceIdentifier = "/dev/dri/card1";

```
   |
### Preferred Vulkan GPU


You can set the GPU type to favor when the Kanzi Vulkan backend selects a device to use, where more than one GPU is available. By default Kanzi uses the first enumerated GPU.
|

In `application.cfg` |

`PreferredGPU = value` |
|

In `Application::onConfigure` |

`configuration.preferredGPU = gfx::GpuSelectionType::value` |
|

Values |
|

`value` |

Maps to the Vulkan backend GPU selection criteria:

- To map to `First`, selecting the first enumerated GPU, often controlled by a control panel application. Default Value.

  - In `application.cfg`, use `first`.
  - In `Application::onConfigure`, use `gfx::GpuSelectionType::First`.

- To map to `LargestMemory`, favoring the GPU with the most memory available.

  - In `application.cfg`, use `largestmemory`.
  - In `Application::onConfigure`, use `gfx::GpuSelectionType::LargestMemory`.

- To map to `Discrete`, favoring discrete GPU devices. The device is typically a separate processor connected to the host.

  - In `application.cfg`, use `discrete`.
  - In `Application::onConfigure`, use `gfx::GpuSelectionType::Discrete`.

- To map to `Integrated`, favoring integrated GPU devices. The device is typically one embedded in or tightly coupled with the host.

  - In `application.cfg`, use `integrated`.
  - In `Application::onConfigure`, use `gfx::GpuSelectionType::Integrated`.

- To map to `CPU`, favoring CPU-based graphics devices. The device is typically running on the same processor as the host.

  - In `application.cfg`, use `cpu`.
  - In `Application::onConfigure`, use `gfx::GpuSelectionType::CPU`.

  |      |
|

`application.cfg` example |

```
# Prefer integrated GPU.
PreferredGPU = integrated

```
   |
|

`Application::onConfigure` example |

```
// Prefer integrated GPU.
configuration.preferredGPU = gfx::GpuSelectionType::Integrated;

```
   |
## QNX context type selection


On QNX, you can set the context type that you want your Kanzi application to use. In `application.cfg` and on the command line you can set only one context type. To set more than one context type, set it in the `Application::onConfigure`.
|

In `application.cfg` |

`QnxContextType = contextType` |
|

In `Application::onConfigure` |

`configuration.defaultDesktopProperties.contextFlags = contextType | contextType | contextType...;` |
|

On the command line |

`-qnx-context-type=contextType` |
|

Value |
|

`contextType` |

Type of the QNX context that you want your Kanzi application to use. Default value is `SCREEN_APPLICATION_CONTEXT`.

You can set your application to use these contexts:

- `SCREEN_APPLICATION_CONTEXT`
- `SCREEN_WINDOW_MANAGER_CONTEXT`
- `SCREEN_INPUT_PROVIDER_CONTEXT`
- `SCREEN_POWER_MANAGER_CONTEXT`
- `SCREEN_DISPLAY_MANAGER_CONTEXT`
- `SCREEN_INPUT_MANAGER_CONTEXT`
- `SCREEN_BUFFER_PROVIDER_CONTEXT`
  |      |
|

`application.cfg` example |

```
# Sets Kanzi to use the SCREEN_DISPLAY_MANAGER_CONTEXT context type.
QnxContextType = SCREEN_DISPLAY_MANAGER_CONTEXT

```
   |
|

`Application::onConfigure` example |

```
// Sets Kanzi to use the SCREEN_WINDOW_MANAGER_CONTEXT and SCREEN_INPUT_PROVIDER_CONTEXT context types.
configuration.defaultDesktopProperties.contextFlags = SCREEN_WINDOW_MANAGER_CONTEXT | SCREEN_INPUT_PROVIDER_CONTEXT;

```
   |
|

Command line example |

Sets Kanzi to use the SCREEN_DISPLAY_MANAGER_CONTEXT context type.

```
-qnx-context-type=SCREEN_DISPLAY_MANAGER_CONTEXT

```
   |
## Application window configuration

### WindowStyle


You can set the style of your Kanzi application window. Besides the default window with a border that users can resize, you can set your Kanzi application to launch in a window without a border, in a window of fixed size, and in a window that occupies the entire device screen.

To set the position and size of the application window, see Application window position and size.
|

In `application.cfg` |

`WindowStyle = "style"` |
|

In `Application::onConfigure` |

`configuration.defaultWindowProperties.style = style;` |
|

Value |
|

`style` |

To set a window without borders or any other decorations that users cannot resize:

- In `application.cfg` use `borderless`.
- In `Application::onConfigure` use `window_properties.hpp::KzsWindowStyle::KZS_WINDOW_STYLE_BORDERLESS`.


To set a window that users cannot resize:

- In `application.cfg` use `fixed`.
- In `Application::onConfigure` use `window_properties.hpp::KzsWindowStyle::KZS_WINDOW_STYLE_FIXED`.


To set a window that occupies the whole device screen:

- In `application.cfg` use `fullscreen`.
- In `Application::onConfigure` use `window_properties.hpp::KzsWindowStyle::KZS_WINDOW_STYLE_FULL_SCREEN`.


To set a window that users can resize:

- In `application.cfg` use `resizable`.
- In `Application::onConfigure` use `window_properties.hpp::KzsWindowStyle::KZS_WINDOW_STYLE_RESIZABLE`.
  |      |
|

`application.cfg` example |

```
# Launch the application in a window that occupies the whole screen of the device.
WindowStyle = "fullscreen"

```
   |
|

`Application::onConfigure` example |

```
// Launch the application in a window that occupies the whole screen of the device.
configuration.defaultWindowProperties.style = KZS_WINDOW_STYLE_FULL_SCREEN;

```
   |
### DefaultDisplayIndex


When you run your Kanzi application in full-screen mode on a system with more than one display, you can set the default display where your Kanzi application window appears.

To make the application window fullscreen, see WindowStyle.

You can use this configuration option only on platforms where Kanzi owns the output window. This is not the case on Android. On Android, to launch your Android Activity on a particular display set the intent option with `setLaunchDisplayId(id)` or use `adb` with the `--display` argument. See https://source.android.com/docs/core/display/multi_display/activity-launch.
|

In `application.cfg` |

`DefaultDisplayIndex = index` |
|

In `Application::onConfigure` |

`configuration.defaultWindowProperties.defaultDisplayIndex = index;` |
|

Value |
|

`index` |

Index number of the display. Default value is 0. |      |
|

`application.cfg` example |

```
# Sets the second display as the default display for the full-screen application window.
DefaultDisplayIndex = 1

```
   |
|

`Application::onConfigure` example |

```
// Sets the second display as the default display for the full-screen application window.
configuration.defaultWindowProperties.defaultDisplayIndex = 1;

```
   |
### WindowBufferCount


If the windowing system of your target device supports setting the number of window buffers, you can set the number of native window buffers that your Kanzi application window uses. For example, Renesas window manager and QNX Screen support the setting of the number of window buffers.
|

In `application.cfg` |

`WindowBufferCount = value` |
|

In `Application::onConfigure` |

`configuration.defaultWindowProperties.bufferCount = value;` |
|

Values |
|

`value` |

The number of native window buffers used by the Kanzi application window. The default value is 0 and sets Kanzi to use the default value provided by the native windowing system of the target device. |      |
|

`application.cfg` example |

```
# Set the number of native window buffers used by the Kanzi application window to 3.
WindowBufferCount = 3

```
   |
|

`Application::onConfigure` example |

```
// Set the number of native window buffers used by the Kanzi application window to 3.
configuration.defaultWindowProperties.bufferCount = 3;

```
   |
### QnxWindowBufferCount


Sets the number of native window buffers that your Kanzi application window uses on QNX platform. To ensure compatibility, if you do not set this configuration option explicitly, Kanzi uses the value from the WindowBufferCount configuration option.
|

In `application.cfg` |

`QnxWindowBufferCount = value` |
|

In `Application::onConfigure` |

`configuration.systemConfiguration[ConfigurationKeyQnxWindowBufferCount] = value;` |
|

Values |
|

`value` |

The number of native window buffers used by the Kanzi application window. The default value is unspecified. |      |
|

`application.cfg` example |

```
# Set the number of native window buffers used by the Kanzi application window to 3.
QnxWindowBufferCount = 3

```
   |
|

`Application::onConfigure` example |

```
// Set the number of native window buffers used by the Kanzi application window to 3.
configuration.systemConfiguration[ConfigurationKeyQnxWindowBufferCount] = 3;

```
   |
### QnxStreamBufferCount


Sets the number of native stream buffers that your Kanzi application uses on QNX platform.
|

In `application.cfg` |

`QnxStreamBufferCount = value` |
|

In `Application::onConfigure` |

`configuration.systemConfiguration[ConfigurationKeyQnxStreamBufferCount] = value;` |
|

Values |
|

`value` |

The number of native stream buffers used by the Kanzi application. The default value is unspecified. |      |
|

`application.cfg` example |

```
# Set the number of native stream buffers used by the Kanzi application to 3.
QnxStreamBufferCount = 3

```
   |
|

`Application::onConfigure` example |

```
// Set the number of native stream buffers used by the Kanzi application to 3.
configuration.systemConfiguration[ConfigurationKeyQnxStreamBufferCount] = 3;

```
   |
### GroupName


On platforms with windowing systems that use the window group name, such as QNX, you can set the group name for the application window group. When you run multiple Kanzi applications, in each Kanzi application set a unique name for the window group.
|

In `Application::onConfigure` |

`configuration.defaultWindowProperties.groupName = "value";` |
|

Values |
|

`value` |

The name of the Kanzi application window group. |      |
|

`Application::onConfigure` example |

```
// Set the Kanzi application window group name to Cluster.
configuration.defaultWindowProperties.groupName = "Cluster";

```
   |
### QnxPipelineID


You can set the QNX Screen pipeline ID for your Kanzi application window. A graphics pipeline ID is an identifier that refers to the hardware layering that is specific to your target device.

When you set the pipeline ID, your Kanzi application sets that ID using the underlying system functions. By default a Kanzi application does not set the pipeline ID.

If you set the pipeline ID, make sure that the pipeline order of your target device and the z-ordering of the application windows make sense together. You can set the z-order of a Kanzi application window using the `WindowOrder` setting. See Application window position and size.
|

In `application.cfg` |

`QnxPipelineID = value` |
|

On the command line |

`-qnx-pipeline-id=value` |
|

Values |
|

`value` |

Integer value that contains the QNX Screen pipeline ID. By default a Kanzi application does not set the pipeline ID.

The value that you set on the command line takes priority over the value that you set in `application.cfg`.  |      |
|

`application.cfg` example |

```
# Sets the QNX Screen pipeline ID to 1.
QnxPipelineID = 1

```
   |
|

Command line example |

Sets the QNX Screen pipeline ID to 1.

```
-qnx-pipeline-id=1

```
   |
### QnxWindowSelfLayout


On QNX platforms, enables self layout mode of the QNX Screen property for the Kanzi application window. When enabled, in your application you can control window properties that are otherwise managed by the QNX window manager.
|

In `application.cfg` |

`QnxWindowSelfLayout = value` |
|

In `Application::onConfigure` |

`configuration.systemConfiguration[ConfigurationKeyDefaultQnxWindowSelfLayout] = value;` |
|

Values |
|

`value` |

- `1` - Enables self layout so that you can control layout properties. When enabled, you can set the window properties as listed under the `SCREEN_PROPERTY_SELF_LAYOUT` at [QNX Screen property types](https://www.qnx.com/developers/docs/7.1/index.html#com.qnx.doc.screen/topic/screen_8h_1Screen_Property_Types.html).
- `0` - Disables self layout so that the window manager controls properties. Default value.
  |      |
|

`application.cfg` example |

```
# Enables self layout for this QNX window.
QnxWindowSelfLayout = 1

```
   |
|

`Application::onConfigure` example |

```
// Enables self layout for this QNX window.
configuration.systemConfiguration[ConfigurationKeyDefaultQnxWindowSelfLayout] = "1";

```
   |
|

Command line example |

Enables self layout for this QNX window.

```
-qnx-window-self-layout=1

```
   |
### QnxUsageFlags


For a Kanzi application window you can programmatically set the usage flags for the QNX Screen property. Screen usage flags enable you to constrain the allocated QNX window buffers.
|

In `Application::onConfigure` |

```
m_applicationProperties.defaultWindowProperties.usageFlags = usageFlags;

```
   |
|

Values |
|

`usageFlags` |

For available values, see [QNX Screen usage flags](https://www.qnx.com/developers/docs/7.0.0//////index.html#com.qnx.doc.screen/topic/screen_8h_1Screen_Usage_Flag_Types.html). |      |
|

`Application::onConfigure` example |

```
// To use the OpenGL ES 3.X to render the QNX window buffer.
m_applicationProperties.defaultWindowProperties.usageFlags = SCREEN_USAGE_OPENGL_ES3;

```
   |
### EGLGraphicsFormatID


You can set the EGL graphics format ID for your Kanzi application. EGL graphics format ID is an identifier that refers to an EGL configuration for a Kanzi application that runs on EGL-supported platforms. Use the command line to list EGL configurations available for your Kanzi application.

Keep in mind that when you set the EGL graphics format ID, you override the EGL graphics format settings.

You can set the EGL format ID for these EGL graphics outputs:

- Android WS
- Emscripten
- Wayland
- X11

|

In `application.cfg` |

`EGLGraphicsFormatID = value` |
|

On the command line |

`-egl-graphics-format-id=value`

`-enum-egl-configs`  |
|

Values |
|

`value` |

Integer value that contains the EGL graphics format ID. By default, a Kanzi application does not set the EGL graphics format ID.

The value that you set on the command line takes priority over the value that you set in `application.cfg`.  |      |
|

`application.cfg` example |

```
# Sets the EGL graphics format ID to 1.
EGLGraphicsFormatID = 1

```
   |
|

Command line example |

Sets the EGL graphics format ID to 1.

```
-egl-graphics-format-id=1

```


Lists EGL configurations available for the application.

```
-enum-egl-configs

```
   |
### EGLContextClientVersion


You can set the EGL context client version for these EGL graphics outputs:

- Android WS
- Emscripten
- Wayland
- QNX
- X11

|

In `application.cfg` |

`EGLContextClientVersion = value` |
|

In `Application::onConfigure` |

`configuration.systemConfiguration[ConfigurationKeyEGLContextClientVersion] = value;` |
|

On the command line |

`-egl-context-client-version=value` |
|

Values |
|

`value` |

The EGL context client version that Kanzi tries to use:

- To use the highest available ES version, use `automatic` (`EGLContextClientSelection::Automatic`). Default value.
- The use explicitly unspecified version, use `unspecified` (`EGLContextClientSelection::Unspecified`).
- The use a specific ES version, use `es1`, `es2`, or `es3` (`EGLContextClientSelection`).
  |      |
|

`application.cfg` example |

```
# Sets Kanzi to use ES2 context client version.
EGLContextClientVersion = es2

```
   |
|

`Application::onConfigure` example |

```
// Sets Kanzi to use ES2 context client version.
configuration.systemConfiguration[ConfigurationKeyEGLContextClientVersion] = "es2";

```
   |
|

Command line example |

Sets Kanzi to use ES2 context client version.

```
-egl-context-client-version=es2

```
   |
## Input handling


You can define how your application handles touch and pointer input. When you run your application on a device, you can set whether the application reacts to the pointer of the device, uses a touch screen, or both. You can also set the transformation matrix of the input event coordinates.

A Kanzi application handles input by default. To disable input handling in your application, override the `Application::setScreenOverride()` function with an empty implementation. See Disabling input handling.
### InputTransform


You can set the transformation matrix of the input event coordinates. This transformation only affects input event coordinates, not the orientation of the Kanzi application screen. For example, use this to rotate the touch screen in relation to your application screen.
|

In `application.cfg` |

`InputTransform = transformation` |
|

In `Application::onConfigure` |

`configuration.defaultEventSourceProperties.transformation = transformation;` |
|

Values |
|

`transformation` |

Transformation matrix of the touch screen. |      |
|

`application.cfg` example |

```
# Rotate a touch screen sized 1280x720 pixels by 180 degrees.
InputTransform = -1, 0, 0, 0, -1, 0, 1280, 720, 1

```
   |
|

`Application::onConfigure` example |

```
// Rotate a touch screen sized 1280x720 pixels by 180 degrees.
configuration.defaultEventSourceProperties.transformation = Matrix3x3::createTranslation(1280.0f, 720.0f) * Matrix3x3::createRotationInDegrees(180.0f);

```
   |

The examples use this equation to calculate the transformation matrix:   \[\begin{split}\begin{bmatrix} 1 & 0 & 1280\\ 0 & 1 & 720\\ 0 & 0 & 1 \end{bmatrix} * \begin{bmatrix} cos(\pi) & -sin(\pi) & 0\\ sin(\pi) & cos(\pi) & 0\\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} -1 & 0 & 1280\\ 0 & -1 & 720\\ 0 & 0 & 1 \end{bmatrix}\end{split}\]
### InputTranslation


You can set how Kanzi translates pointer and touch events.
|

In `application.cfg` |

`InputTranslation = translation` |
|

In `Application::onConfigure` |

`configuration.defaultEventSourceProperties.translation = translation;` |
|

Values |
|

`translation` |

Translation of pointer and touch events.

To not apply any translation:

- In `application.cfg` use `none`. Default value.
- In `Application::onConfigure` use `InputTranslation::TranslateNone`. Default value.


To translate pointer events to touch events:

- In `application.cfg` use `pointertotouch`.
- In `Application::onConfigure` use `InputTranslation::TranslatePointerToTouch`.


To translate pointer events to touch events, and preserve pointer events:

- In `application.cfg` use `pointertotouchpreserve`.
- In `Application::onConfigure` use `InputTranslation::TranslatePointerToTouchPreserve`.


To translate touch events to pointer events:

- In `application.cfg` use `touchtopointer`.
- In `Application::onConfigure` use `InputTranslation::TranslateTouchToPointer`.


To translate touch events to pointer events, and preserve touch events:

- In `application.cfg` use `touchtopointerpreserve`.
- In `Application::onConfigure` use `InputTranslation::TranslateTouchToPointerPreserve`.
  |      |
|

`application.cfg` example |

```
# Translate pointer events to touch events.
InputTranslation = pointertotouch

```
   |
|

`Application::onConfigure` example |

```
// Translate pointer events to touch events.
configuration.defaultEventSourceProperties.translation = TranslatePointerToTouch;

```
   |
### InputDiscardPointer


You can set whether the application reacts to the pointer of the device.
|

In `application.cfg` |

`InputDiscardPointer = value` |
|

In `Application::onConfigure` |

`configuration.defaultEventSourceProperties.discardPointerEvents = value;` |
|

Values |
|

`value` |
|

`0` |

Do not ignore pointer input. Default value. |
|

`1` |

Ignore pointer input. |      |      |
|

`application.cfg` example |

```
# Ignore pointer input.
InputDiscardPointer = 1

```
   |
|

`Application::onConfigure` example |

```
// Ignore pointer input.
configuration.defaultEventSourceProperties.discardPointerEvents = 1;

```
   |
### InputDiscardTouch


You can set whether the application reacts to touch input.
|

In `application.cfg` |

`InputDiscardTouch = value` |
|

In `Application::onConfigure` |

`configuration.defaultEventSourceProperties.discardTouchEvents = value;` |
|

Values |
|

`value` |
|

`0` |

Do not ignore touch input. Default value. |
|

`1` |

Ignore touch input. |      |      |
|

`application.cfg` example |

```
# Ignore touch input.
InputDiscardTouch = 1

```
   |
|

`Application::onConfigure` example |

```
// Ignore touch input.
configuration.defaultEventSourceProperties.discardTouchEvents = 1;

```
   |
## Input event devices on Linux


You can configure the input event devices that Kanzi listens to on Linux ports where the native windowing system does not provide input device handling.

This way Kanzi can listen to events directly from the input event devices provided by the operating system.

For example, in Vivante fbdev and WSEGL ports you can configure the input event devices that Kanzi listens to. In X11 and Wayland ports the native windowing system handles input devices.

Kanzi by default listens to all input event devices named eventN, where N is an integer, in the `/dev/input` directory.
|

In `application.cfg` |

`InputEventDevice = path` |
|

In `Application::onConfigure` |

`configuration.defaultEventSourceProperties.inputEventDevice = path;` |
|

Values |
|

`path` |

Full path to one or more input event devices. Separate a list of several paths with a semicolon. |      |
|

`application.cfg` example |

```
# Listens to events from one input event device.
InputEventDevice = "/dev/input/event1"

```


```
# Listens to events from two input event devices.
InputEventDevice = "/dev/input/event0;/dev/input/event1"

```


```
# Disables listening to events from input event devices.
InputEventDevice = "none"

```
   |
|

`Application::onConfigure` example |

```
// Listens to events from one input event device.
configuration.defaultEventSourceProperties.inputEventDevice = "/dev/input/event1";

```


```
// Listens to events from two input event devices.
configuration.defaultEventSourceProperties.inputEventDevice = "/dev/input/event0;/dev/input/event1";

```


```
// Disables listening to events from input event devices.
configuration.defaultEventSourceProperties.inputEventDevice = "none";

```
   |
## Platform configuration

### PlatformLoggingEnabled


You can enable additional logs for the Platform layer. Currently, affects Wayland and DRM/GBM.
|

In `application.cfg` |

`PlatformLoggingEnabled = value` |
|

In `Application::onConfigure` |

`configuration.systemConfiguration[ConfigurationKeyPlatformLoggingEnabled] = value;` |
|

On the command line |

`--log-platform` |
|

Values |
|

`false` |

Disable the additional logs for the Platform layer. Default value. |
|

`true` |

Enable the additional logs for the Platform layer. |      |
|

`application.cfg` example |

```
# Sets Kanzi to produce additional logs for the Platform layer.
PlatformLoggingEnabled = true

```
   |
|

`Application::onConfigure` example |

```
// Sets Kanzi to produce additional logs for the Platform layer.
configuration.systemConfiguration[ConfigurationKeyPlatformLoggingEnabled] = true;

```
   |
|

Command line example |

Sets Kanzi to produce additional logs for the Platform layer.

```
--log-platform

```
   |
## Wayland configuration


When you use Kanzi on Wayland, you can configure Wayland-specific parameters.
### Wayland shell


You can set which Wayland shell Kanzi uses.
|

In `application.cfg` |

`WaylandShell = shell` |
|

In `Application::onConfigure` |

`configuration.systemConfiguration[ConfigurationKeyWaylandShell] = shell;` |
|

On the command line |

`-wayland-shell=shell` |
|

Values |
|

`shell` |

Shell that Kanzi tries to use:

- The XDG shell, use `xdg` (`wayland::WaylandShellType::XDG`). Default value.
- The original shell, use `core` (`wayland::WaylandShellType::Core`).
- The IVI shell, use `ivi` (`wayland::WaylandShellType::IVI`).
  |      |
|

`application.cfg` example |

```
# Sets Kanzi to use the IVI shell.
WaylandShell = ivi

```
   |
|

`Application::onConfigure` example |

```
// Sets Kanzi to use the IVI shell.
configuration.systemConfiguration[ConfigurationKeyWaylandShell] = "ivi";

```
   |
|

Command line example |

Sets Kanzi to use the IVI shell.

```
-wayland-shell=ivi

```
   |
### Wayland input mode


If you do not want to wait for the pointer and touch `frame()` events, you can set Kanzi to process input events immediately.
|

In `application.cfg` |

`WaylandInputMode = value` |
|

In `Application::onConfigure` |

`configuration.systemConfiguration[ConfigurationKeyWaylandInputMode] = value;` |
|

On the command line |

`-wayland-input-mode=value` |
|

Values |
|

`value` |

Wayland input mode that Kanzi tries to use:

- To wait for the `frame()` events, use `retained` (`wayland::WaylandInputMode::Retained`). Default value.
- To ignore the `frame()` events and process input immediately, use `immediate` (`wayland::WaylandInputMode::Immediate`).
  |      |
|

`application.cfg` example |

```
# Enable immediate input mode.
WaylandInputMode = immediate

```
   |
|

`Application::onConfigure` example |

```
// Enable immediate input mode.
configuration.systemConfiguration[ConfigurationKeyWaylandInputMode] = "immediate";

```
   |
|

Command line example |

Enable immediate input mode.

```
-wayland-input-mode=immediate

```
   |
### Wayland app ID


You can set Kanzi app ID. The default app ID is âkanziâ.
|

In `application.cfg` |

`WaylandAppId = appId` |
|

In `Application::onConfigure` |

`configuration.systemConfiguration[ConfigurationKeyWaylandAppId] = appId;` |
|

On the command line |

`-wayland-app-id=appId` |
|

`application.cfg` example |

```
# Sets "kanzi" as app ID.
WaylandAppId = kanzi

```
   |
|

`Application::onConfigure` example |

```
// Sets "kanzi" as app ID.
configuration.systemConfiguration[ConfigurationKeyWaylandAppId] = "kanzi";

```
   |
|

Command line example |

Sets âkanziâ as app ID.

```
-wayland-app-id=kanzi

```
   |
### Wayland IVI surface ID


When you use the Wayland IVI shell, you can set which IVI surface ID Kanzi uses.
|

In `application.cfg` |

`WaylandIviSurfaceId = id` |
|

In `Application::onConfigure` |

`configuration.systemConfiguration[ConfigurationKeyWaylandIviSurfaceId] = id;` |
|

On the command line |

`-wayland-ivi-surface-id=id` |
|

Values |
|

`id` |

The IVI surface ID that Kanzi tries to use. |      |
|

`application.cfg` example |

```
# Sets IVI surface ID to 4000.
WaylandIviSurfaceId = 4000

```
   |
|

`Application::onConfigure` example |

```
// Sets IVI surface ID to 4000.
configuration.systemConfiguration[ConfigurationKeyWaylandIviSurfaceId] = 4000;

```
   |
|

Command line example |

Sets IVI surface ID to 4000.

```
-wayland-ivi-surface-id=4000

```
   |
## Wayland IVI extension configuration


When you use [COVESA IVI extension](https://github.com/COVESA/wayland-ivi-extension) and have Kanzi built with IVI extension support, you can control Kanzi by setting various IVI parameters.
### Wayland IVI layer ID


Kanzi requires a dedicated IVI layer to display its content. You can set which IVI layer Kanzi uses.
|

In `application.cfg` |

`WaylandIviLayerId = id` |
|

In `Application::onConfigure` |

`configuration.systemConfiguration[ConfigurationKeyWaylandIviLayerId] = id;` |
|

On the command line |

`-wayland-ivi-layer-id=id` |
|

Values |
|

`id` |

The IVI layer ID that Kanzi tries to use. |      |
|

`application.cfg` example |

```
# Sets IVI layer ID to 4000.
WaylandIviLayerId = 4000

```
   |
|

`Application::onConfigure` example |

```
// Sets IVI layer ID to 4000.
configuration.systemConfiguration[ConfigurationKeyWaylandIviLayerId] = 4000;

```
   |
|

Command line example |

Sets IVI layer ID to 4000.

```
-wayland-ivi-layer-id=4000

```
   |
### Wayland IVI surface opacity


You can set the Kanzi IVI surface opacity.
|

In `application.cfg` |

`WaylandIviSurfaceOpacity = opacity` |
|

In `Application::onConfigure` |

`configuration.systemConfiguration[ConfigurationKeyWaylandIviSurfaceOpacity] = opacity;` |
|

On the command line |

`-wayland-ivi-surface-opacity=opacity` |
|

Values |
|

`opacity` |

Opacity of the IVI surface that Kanzi uses, in the range 0..1:

- 1 sets the surface to be fully opaque. Default value.
- 0 sets the surface to be fully transparent.
  |      |
|

`application.cfg` example |

```
# Sets the IVI surface to be fully transparent.
WaylandIviSurfaceOpacity = 0

```
   |
|

`Application::onConfigure` example |

```
// Sets the IVI surface to be fully transparent.
configuration.systemConfiguration[ConfigurationKeyWaylandIviSurfaceOpacity] = 0;

```
   |
|

Command line example |

Sets the IVI surface to be fully transparent.

```
-wayland-ivi-surface-opacity=0

```
   |
### Wayland IVI layer opacity


You can set the Kanzi IVI layer opacity.
|

In `application.cfg` |

`WaylandIviLayerOpacity = opacity` |
|

In `Application::onConfigure` |

`configuration.systemConfiguration[ConfigurationKeyWaylandIviLayerOpacity] = opacity;` |
|

On the command line |

`-wayland-ivi-layer-opacity=opacity` |
|

Values |
|

`opacity` |

Opacity of the IVI layer that Kanzi uses, in the range 0..1:

- 1 sets the layer to be fully opaque. Default value.
- 0 sets the layer to be fully transparent.
  |      |
|

`application.cfg` example |

```
# Sets the IVI layer to be fully transparent.
WaylandIviLayerOpacity = 0

```
   |
|

`Application::onConfigure` example |

```
// Sets the IVI layer to be fully transparent.
configuration.systemConfiguration[ConfigurationKeyWaylandIviLayerOpacity] = 0;

```
   |
|

Command line example |

Sets the IVI layer to be fully transparent.

```
-wayland-ivi-layer-opacity=0

```
   |
### Wayland IVI surface visibility


You can set the Kanzi IVI surface visibility.
|

In `application.cfg` |

`WaylandIviSurfaceVisibility = visibility` |
|

In `Application::onConfigure` |

`configuration.systemConfiguration[ConfigurationKeyWaylandIviSurfaceVisibility] = visibility;` |
|

On the command line |

`-wayland-ivi-surface-visibility=visibility` |
|

Values |
|

`visibility` |

Visibility of the IVI surface that Kanzi uses:

- 1 makes the Kanzi IVI surface visible. Default value.
- 0 hides the Kanzi IVI surface.
  |      |
|

`application.cfg` example |

```
# Hides the Kanzi IVI surface.
WaylandIviSurfaceVisibility = 0

```
   |
|

`Application::onConfigure` example |

```
// Hides the Kanzi IVI surface.
configuration.systemConfiguration[ConfigurationKeyWaylandIviSurfaceVisibility] = 0;

```
   |
|

Command line example |

Hides the Kanzi IVI surface.

```
-wayland-ivi-surface-visibility=0

```
   |
### Wayland IVI layer visibility


You can set the Kanzi IVI layer visibility.
|

In `application.cfg` |

`WaylandIviLayerVisibility = visibility` |
|

In `Application::onConfigure` |

`configuration.systemConfiguration[ConfigurationKeyWaylandIviLayerVisibility] = visibility;` |
|

On the command line |

`-wayland-ivi-layer-visibility=visibility` |
|

Values |
|

`visibility` |

Visibility of the IVI layer that Kanzi uses:

- 1 makes the Kanzi IVI layer visible. Default value.
- 0 hides the Kanzi IVI layer.
  |      |
|

`application.cfg` example |

```
# Hides the Kanzi IVI layer.
WaylandIviLayerVisibility = 0

```
   |
|

`Application::onConfigure` example |

```
// Hides the Kanzi IVI layer.
configuration.systemConfiguration[ConfigurationKeyWaylandIviLayerVisibility] = 0;

```
   |
|

Command line example |

Hides the Kanzi IVI layer.

```
-wayland-ivi-layer-visibility=0

```
   |
## Image loading


Kanzi uses third-party image libraries, such as [libpng](http://www.libpng.org/pub/png/libpng.html) and [libjpeg](https://jpegclub.org/reference/), to support different image formats. To make your Kanzi application more secure, you can set limits for Kanzi to use when loading images using these libraries. For example, to prevent the loading of malicious files, you can limit the amount of memory to allocate for each object that Kanzi loads.
### libjpeg


You can set the maximum amount of memory in bytes to allocate for each JPEG object that Kanzi loads using the [libjpeg](https://jpegclub.org/reference/) image library.
|

In `application.cfg` |

`LibJPEGMaxMemory = bytes` |
|

In `Application::onConfigure` |

`configuration.imageLoad.libJPEGMaxMemory = bytes;` |
|

Values |
|

`bytes` |

The maximum number of bytes to allocate for a JPEG object in libjpeg.

Kanzi passes this value to the libjpeg `jpeg_memory_mgr::max_memory_to_use` parameter. This value affects only the space used for virtual-array buffers and is not a guaranteed maximum but merely advisory.

The default value 0 sets no limit on the amount of memory to allocate.  |      |
|

`application.cfg` example |

```
# Sets the libjpeg memory allocation limit to 2 MB (2,000,000 bytes).
LibJPEGMaxMemory = 2000000

```
   |
|

`Application::onConfigure` example |

```
// Sets the libjpeg memory allocation limit to 2 MB (2,000,000 bytes).
configuration.imageLoad.libJPEGMaxMemory = 2000000;

```
   |
### libpng


You can set the maximum number of ancillary chunks in a PNG datastream and the maximum amount of memory in bytes to allocate for a chunk that Kanzi loads using the [libpng](http://www.libpng.org/pub/png/libpng.html) image library.

By default Kanzi uses these limits imposed by libpng:

- Maximum total of 1000 sPLT, tEXt, iTXt, zTXt, and unknown ancillary chunks.
- Maximum of 8 megabytes of memory to allocate for a chunk other than IDAT.

|

In `application.cfg` |

`LibPNGChunkCacheMax = chunks`

`LibPNGChunkMallocMax = bytes`  |
|

In `Application::onConfigure` |

`configuration.imageLoad.libPNGChunkCacheMax = chunks;`

`configuration.imageLoad.libPNGChunkMallocMax = bytes;`  |
|

Values |
|

`chunks` |

The maximum number of ancillary chunks stored by libpng.

Kanzi passes this value to the libpng `png_set_chunk_cache_max()` function.  |
|

`bytes` |

The maximum amount of memory in bytes that a chunk other than IDAT can occupy.

Kanzi passes this value to the libpng `png_set_chunk_malloc_max()` function.  |      |
|

`application.cfg` example |

```
# Sets the libpng limit for the number of ancillary chunks to 500.
LibPNGChunkCacheMax = 500
# Sets the libpng limit for the amount of memory that a chunk
# other than IDAT can occupy to 2 MB (2,000,000 bytes).
LibPNGChunkMallocMax = 2000000

```
   |
|

`Application::onConfigure` example |

```
// Sets the libpng limit for the number of ancillary chunks to 500.
configuration.imageLoad.libPNGChunkCacheMax = 500;
// Sets the libpng limit for the amount of memory that a chunk
// other than IDAT can occupy to 2 MB (2,000,000 bytes).
configuration.imageLoad.libPNGChunkMallocMax = 2000000;

```
   |
## Shader binary cache


On performance-constrained platforms, shader compilations can considerably slow down the application startup and decrease runtime performance. You can use a shader binary cache primed with the set of shaders that your application requires. This way, your application does not have to compile shaders from source at runtime.

See Using binary shaders.
### ShaderBinaryCacheDirectory


You can set the directory where you want your Kanzi application to cache shader binaries. At the time of caching, this directory must be writable. For production purposes, you can make the directory read-only. See ShaderBinaryCacheReadOnly.

To enable the caching of shader binaries, use the ShaderBinaryCacheEnabled setting.
|

In `application.cfg` |

`ShaderBinaryCacheDirectory = path` |
|

In `Application::onConfigure` |

`configuration.shaderBinaryCacheDirectory = path;` |
|

Values |
|

`path` |

The path to the cache directory for shader binaries. You can use an absolute path or a relative path from the working directory of your application. |      |
|

`application.cfg` example |

```
# Sets the shader binary cache directory to /tmp/shader-cache/.
ShaderBinaryCacheDirectory = "/tmp/shader-cache/"

```
   |
|

`Application::onConfigure` example |

```
// Sets the shader binary cache directory to /tmp/shader-cache/.
configuration.shaderBinaryCacheDirectory = "/tmp/shader-cache/";

```
   |
### ShaderBinaryCacheEnabled


You can set your application to cache shader binaries. Use this to optimize Kanzi application performance on platforms where offline shader compilation tools are not available.

The caching of shader binaries requires that Kanzi Studio exports the source code of the shaders to the kzb file. In Kanzi Studio, in the Project > Properties, make sure that the Export Shader Source Code property is enabled. This is the default value.
|

In `application.cfg` |

`ShaderBinaryCacheEnabled = value` |
|

In `Application::onConfigure` |

`configuration.shaderBinaryCacheEnabled = value;` |
|

Values |
|

`true` |

Cache shader binaries. |
|

`false` |

Do not cache shader binaries. Default value. |      |
|

`application.cfg` example |

```
# Enables the caching of shader binaries.
ShaderBinaryCacheEnabled = true

```
   |
|

`Application::onConfigure` example |

```
// Enables the caching of shader binaries.
configuration.shaderBinaryCacheEnabled = true;

```
   |
### ShaderBinaryCacheCollisionCheck


By default, Kanzi stores in the filename of a cached shader binary only a hash of the shader source code. Kanzi then compares that hash to a hash value derived from the requested shader source. Hash collisions, which are rare but possible, result in the use of the wrong shader.

To guard against hash collisions, you can set your application to store the shader source code and perform a full string comparison to make sure that the shaders are identical. If two shaders produce the same hash value, the application logs a warning.

To save disk space and optimize performance, enable the hash collision checks only during development.
|

In `application.cfg` |

`ShaderBinaryCacheCollisionCheck = value` |
|

In `Application::onConfigure` |

`configuration.shaderBinaryCacheCollisionCheck = value;` |
|

Values |
|

`true` |

Check for hash collisions in cached shaders.

Use this only during development.  |
|

`false` |

Do not check for hash collisions in cached shaders. Default value. |      |
|

`application.cfg` example |

```
# Enables checking for hash collisions in cached shaders.
ShaderBinaryCacheCollisionCheck = true

```
   |
|

`Application::onConfigure` example |

```
// Enables checking for hash collisions in cached shaders.
configuration.shaderBinaryCacheCollisionCheck = true;

```
   |
### ShaderBinaryCacheReadOnly


By default, Kanzi can write to the shader binary cache. When your application is ready for production, you can make the shader binary cache read-only.
|

In `application.cfg` |

`ShaderBinaryCacheReadOnly = value` |
|

In `Application::onConfigure` |

`configuration.ShaderBinaryCacheReadOnly = value;` |
|

Values |
|

`true` |

Make the shader binary cache directory read-only.

You can use this when your application is ready for production.  |
|

`false` |

Make the shader binary cache directory writable. Default value. |      |
|

`application.cfg` example |

```
# Makes the shader binary cache read-only.
ShaderBinaryCacheReadOnly = true

```
   |
|

`Application::onConfigure` example |

```
// Makes the shader binary cache read-only.
configuration.ShaderBinaryCacheReadOnly = true;

```
   |
