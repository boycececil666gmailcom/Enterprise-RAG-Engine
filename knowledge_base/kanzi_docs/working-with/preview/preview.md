---
title: Preview
source: https://docs.kanzi.com/4.1.0/en/working-with/preview/preview.html
---

# Preview


Kanzi shows in real-time the changes that you make in your Kanzi Studio project:

- The Preview window shows the content of the currently open Kanzi application. For example, the Preview in this image shows the Kanzi application you can create by completing the Tutorial: Create gauges.

> **Note:** The Kanzi Studio Preview by default uses the TCP/IP for internal communication with Kanzi Studio. If you have a firewall installed on your computer, allow the `Kanzi Preview` process to go through the firewall.
>
> Tip
>
> When you are working with large content, such as 4K textures, the Preview cannot process the data in-memory and can terminate during startup with an out-of-memory error. To enable the Preview to start, in Edit > User Preferences > Advanced tab enable the Export initial Preview data to hard drive setting.
>
> You can estimate whether enabling this setting is necessary by exporting the kzb file of your project. If the size of the kzb file is larger than 300 MB, enable the setting.
>
> By enabling this setting, the Preview loads the initial data to the hard drive, instead of the memory. Enable this setting only when your are working with Kanzi Studio projects where the memory transfer exceeds the 32-bit memory limit of the Preview. When this setting is enabled, the Preview takes longer time to load your projects and start because a hard drive is slower than memory.
> - The Target Preview enables you to see on a target device the changes that you make in a Kanzi Studio project without exporting and redeploying the application.
>
> These are the impacts of Target Preview on development workflow:
>
> - It shows your application as it is, including the rendering and latency, and any behavior that you define in platform-specific code. The content that the Target Preview shows is not a video stream.
> - The Target Preview enables you to revise your design even in late stages of the development. You can instantly test designs and see how your changes look in a real environment, such as on a display inside a vehicle.
> - When you develop an Android application using the Kanzi Android framework (droidfw), you can see full composited application that consists of both Kanzi and Android UI.


See Target Preview.


In the Kanzi Studio Preview you can:

- Control what the Preview shows. See Controlling the Preview.
- Create and position 2D nodes, create and edit Text Block nodes, add triggers, create and position Camera nodes, and zoom and pan around the Preview.

See Editing your application in the Preview.
- Analyze the performance of your application. See Analyzing your application in the Preview.


By default the Preview shows your application using the default Kanzi Studio Preview application.
