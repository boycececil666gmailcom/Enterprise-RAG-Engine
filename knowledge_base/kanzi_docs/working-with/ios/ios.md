---
title: Developing Kanzi applications for iOS
source: https://docs.kanzi.com/4.1.0/en/working-with/ios/ios.html
---

# Developing Kanzi applications for iOS

You can use the Kanzi application framework (appfw) to develop Kanzi applications for iOS. You write application and plugin code in C++ and build the application using CMake and Xcode. Before you begin, check the Requirements for iOS application development with Kanzi.

Kanzi Studio generates a ready-made iOS CMake configuration and a helper script for generating the Xcode project when you create a project using one of these templates:

- Application
- Application with data source plugin
- Application with Kanzi Engine plugin

## iOS project structure

The `<ProjectName>/Application/configs/platforms/ios/` directory contains:

- `CMakeLists.txt` â applies iOS and Xcode-specific settings to the executable target. This includes:

  - `XCODE_ATTRIBUTE_INSTALL_PATH` set to `output`. Combined with `DSTROOT=$(PROJECT_DIR)` passed to `xcodebuild install`, this places the built application in `<Application>/output/`.
  - `XCODE_EMBED_FRAMEWORKS` â embeds the Vulkan and MoltenVK frameworks into the application bundle.
  - `XCODE_EMBED_RESOURCES` â embeds the kzb binary files that you export from Kanzi Studio.

- `Info.plist` â defines the launch screen, supported orientations, and the `UIApplicationSceneManifest` that wires the application to the `SceneDelegate` provided by the iOS application shell.
- `Assets.xcassets` â contains the application icon.
- `src/` â the iOS application shell that hosts `KanziView`:

  - `main.m` â `UIApplicationMain` entry point.
  - `app_delegate.*h,m*` â `UIApplicationDelegate` that selects the default scene configuration.
  - `scene_delegate.*h,m*` â `UIWindowSceneDelegate` that creates the `UIWindow` and installs the root `ViewController`.
  - `view_controller.*h,m*` â fullscreen `UIViewController` whose root view is a `KanziView`. This is where you embed the Kanzi view inside the iOS view hierarchy.

The `Application` folder also contains `generate_cmake_xcode_ios_project.sh`, which generates the Xcode project using the CMake Xcode generator and the Kanzi iOS toolchain.

The iOS platform package ships `KanziView` and `KanziViewRepresentable` in the `KanziAppFwKit` XCFramework. The generated CMake configuration links your application target against `KanziAppFwKit` and embeds the XCFramework in the application bundle.

To learn how to build and deploy your application to an iOS device, see Deploying Kanzi applications to iOS.
## KanziView

`KanziView` is a UIKit `UIView` subclass that hosts Kanzi rendering inside an iOS view hierarchy. You place `KanziView` anywhere in your UIKit view hierarchy alongside native iOS content.

In addition to rendering, `KanziView`:

- Drives the Kanzi application lifecycle. Attaching `KanziView` to a window starts the Kanzi application. Detaching `KanziView` shuts the application down.
- Pauses Kanzi when the iOS application resigns active state, and resumes Kanzi when the application becomes active again.
- Forwards touch events to Kanzi.
**Note:** Only one `KanziView` can exist in a process at a time.
## Application factory

`KanziView` requires a C++ `createApplication()` factory function that returns the `Application` instance to run, with the same signature as on every other Kanzi platform. For example:

```
#include <kanzi/core.ui/application/application.hpp>

class MyApplication : public kanzi::Application
{
    // Override onProjectLoaded, onConfigure, and so on.
};

kanzi::Application* createApplication()
{
    return new MyApplication();
}

```

Link this translation unit into your application target alongside `KanziAppFwKit`. `KanziAppFwKit` calls `createApplication()` once per view attach and deletes the returned instance when the view detaches.
**Note:** On iOS, Kanzi does not receive command-line arguments â `KanziAppFwKit` owns the application entry point and calls `createApplication()` without `argc`/`argv`. As a result, `SystemProperties` is default-initialized. To configure your application, use `application.cfg` or override `Application::onConfigure`. See Application configuration reference.
## Adding a Kanzi view in UIKit

To add a Kanzi view to a UIKit application, import `KanziAppFwKit` and place a `KanziView` in your view hierarchy. You can instantiate `KanziView`:

- From code:

  1.

Override `loadView` (or `viewDidLoad`) in your `UIViewController`.
  2.

Assign a `KanziView` instance.
