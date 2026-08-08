---
title: Node2D plugin example
source: https://docs.kanzi.com/4.1.0/en/examples/node2d-plugin/node2d-plugin.html
---

# Node2D plugin example

This example is a use case for using Kanzi Engine plugins. The example shows how to create a custom 2D node VideoView2D in a Kanzi Engine plugin. The VideoView2D node renders video files whose resolution is divisible by 2 and are encoded with the MPEG-4 codec. The VideoView2D node does not play the audio track in video files. On Android, the example uses a shared image texture utilizing `OES_EGL_image_external` extension for streaming the video from an external context.
## Getting the example

To get the example, in the Kanzi Studio Quick Start window, click Projects and select the Examples tab. Next to the Node2D_plugin example, click .

Kanzi Studio downloads the example to the `<KanziWorkspace>/Examples/Node2D_plugin` directory. The video file is stored in the `Application/bin` directory.
## Content of the example

The example runs on Windows and Android platforms:

- Windows platform uses Microsoft Media Foundation for video playback. You can find the source files for the Windows platform in `<KanziWorkspace>/Examples/Node2D_plugin/Application/src/platform_specific/win32/src`.
**Note:** To run the Node2D plugin example on Windows 10 N and Windows 10 KN versions, you must install the [Media feature pack](https://support.microsoft.com/en-us/kb/3010081) provided by Microsoft.
- Android platform uses the native media player. You can find the source files for the Android platform in `<KanziWorkspace>/Examples/Node2D_plugin/Application/src/platform_specific/android/src`.
- You can find the code common to both platforms in `<KanziWorkspace>/Examples/Node2D_plugin/Application/src/plugin`.

To learn how to create a Kanzi Engine plugin, see Creating Kanzi Engine plugins.
## Using the external texture handle

Android native code and Kanzi application framework run in different context, which is why they cannot share the GPU resources. A widely available OpenGL extension (`GL_OES_EGL_image_external`) provides the support for external texture resources that can be shared between contexts with few limitations. The `Node2D_plugin` example uses the Android media player to render a video stream to a surface view that is bound to the external texture handle. On the Kanzi side, the texture of the node that renders the video is bound to the same external texture handle, and displayed in the render loop.

You can use this approach on other platforms where:

- The device supports the `GL_OES_EGL_image_external` extension.
- A service in another context is capable of providing a texture bound to an external texture handle.

A typical example is a streaming video.
## Running the example

To run the example:

1.

In Kanzi Studio, select File > Open Kanzi Command Prompt.

The Kanzi Command Prompt opens the Windows Command Prompt with the Kanzi environment variables set for the version of Kanzi for which you open a Kanzi Command Prompt.

Use the Kanzi Command Prompt to access Kanzi utilities and build tools, such as Gradle and CMake, without using absolute paths or setting environment variables.
**Tip:** You can find the Kanzi Command Prompt in the Windows Start Menu in the Rightware directory.
When you have more than one version of Kanzi installed, make sure that you launch a Kanzi Command Prompt for the version of Kanzi with which you want to work in that command prompt.
2.
In the Kanzi Command Prompt in the `<KanziWorkspace>/Examples/Node2D_plugin/Application` directory run the script that generates a Visual Studio solution for the example application.
```
generate_cmake_vs2022_solution.bat
```

This script generates a Visual Studio solution for the application in the directory `<KanziWorkspace>/Examples/Node2D_plugin/Application/build_vs2022`.
3.

In Visual Studio open the `<KanziWorkspace>/Examples/Node2D_plugin/Application/build_vs<Version>/Node2D_plugin.sln` Visual Studio solution.
4.

In Visual Studio in the Solution Explorer right-click the `Node2D_plugin_executable` project and select Set as StartUp Project.
5.

Select the solution configuration that you want to use and run your application.

During development, select the Debug configuration. When you are ready to create a version for production, select the Release configuration.
