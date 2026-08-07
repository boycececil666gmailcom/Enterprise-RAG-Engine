---
title: Kanzi Engine plugins
source: https://docs.kanzi.com/4.1.0/en/working-with/plugins/plugins-kanzi-engine.html
---

# Kanzi Engine plugins

With Kanzi plugins, you can extend the functionality of Kanzi and customize Kanzi to fit your application development requirements. When you create a Kanzi plugin, you can share the extended functionality with any Kanzi user.

In Kanzi, you can create and use these types of plugins:

- Kanzi Engine plugins extend the functionality of Kanzi Engine. Kanzi Engine executes these plugins on target platforms.

You can create:

  - Native plugins in C++. These plugins work on all supported platforms.
  - Kanzi Engine plugins in Java. These plugins work on Windows and Android. Together with Kanzi Android framework (droidfw), Java Kanzi Engine plugins allow you to extend your Kanzi application functionality on Android operating system without the need to write native glue code.

See Creating Kanzi Engine plugins.
- Kanzi Studio plugins extend the functionality of Kanzi Studio and run in Kanzi Studio.

See Kanzi Studio plugins.

Use a Kanzi Engine plugin to:

- Create custom nodes using the Kanzi Engine API, use them in your Kanzi Studio projects, and see in the Kanzi Studio Preview how they work.
- Create custom property types and messages using the Kanzi Engine API, and use them in your Kanzi Studio projects.
- Define the data entry points to your Kanzi application, and form the contract between the Kanzi application designer and developer.

To learn how you can use Kanzi Engine plugins, see:

- Extending the functionality of Kanzi Engine
- Tutorial: Get application data from a data source
- Node2D plugin example
- Node3D plugin example

Deployment of native Kanzi Engine plugins is flexible. You can use:

- **Static linking** to deploy the plugin with the application binary.

When using this approach:

  - You can use some optimizations that can provide better performance.
  - You cannot remove or update the plugin without updating the application binary.
  - You have to manually register all static plugins during the application startup in `Module::registerMetadataOverride`.

- **Dynamic linking** to deploy the plugin as a dynamically linked library. For example, DLL or SO.

When using this approach:

  - You can add or remove plugins without modifying the application executable.

For example, the Kanzi Studio Preview dynamically loads the plugins specified in the project.

This is not supported on Android and QNX with the LLVM C++ library.
  - You can independently update the plugins deployed as separate binaries.

For example, do this to extend the functionality.

This is not supported on Android and QNX with the LLVM C++ library.
  - You can reference the classes from a plugin indirectly through the content in a kzb file.

Some platforms do not support or have limited support for dynamically linked libraries:

  - Android does not support independent updates of .apk content.
  - Android and QNX with the LLVM C++ library require you to link the dynamically linked plugins during the build time.

Use dynamically linked Kanzi Engine plugins only with Kanzi applications that are built with the dynamic Kanzi Engine libraries, which Rightware ships in a dynamic platform package.

Do not use dynamic Kanzi Engine plugins with Kanzi applications that are built with the static Kanzi Engine libraries. When you build a static executable, the linker can optimize that executable. As a result, the executable does not necessarily have all the functions that a dynamically linked Kanzi Engine plugin calls.

The recommended approach is to build plugins as a DLL for use in the Kanzi Studio Preview and statically link the plugin to your application. This way, you can use the plugin in the Preview and have the benefits of optimization in your application.

Each plugin provides a class derived from `Module`. Before you can use a plugin, you have to register its module. For platforms that support dynamic loading of libraries, Kanzi Engine tries to do this automatically if the plugin is a dependency of the kzb file but has not been loaded or registered yet. For platforms with no dynamic loading or for statically linked plugins, you have to manually register the modules in `Module::registerMetadataOverride`.

The Node2D and Node3D plugin examples provide example code that registers the modules for the Android platform. See Node2D plugin example and Node3D plugin example.
