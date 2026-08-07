---
title: Debugging native Kanzi Engine plugins
source: https://docs.kanzi.com/4.1.0/en/working-with/plugins/debugging-kanzi-engine-plugins.html
---

# Debugging native Kanzi Engine plugins


You can debug your native Kanzi Engine plugins in the Kanzi Studio Preview using Visual Studio.

To debug a native Kanzi Engine plugin:

1.

In Visual Studio create your Kanzi Engine plugin and build it using the Debug build configuration.

See Creating Kanzi Engine plugins.
2.

Import your Kanzi Engine plugin to a Kanzi Studio project.

See Adding Kanzi Engine plugins to a Kanzi Studio project.
3.

In Kanzi Studio in the project which uses the Kanzi Engine plugin that you want to debug select Project > Properties and in the Properties set:

  - Preview Build Configuration to Debug
  - Preview Visual Studio Version to the version in the solution configuration you used in Visual Studio to build your plugin

For example, set it to 2022.

4.

Hold down the Ctrl Shift keys, in the main menu select Preview > Restart Preview, and wait until Kanzi Studio opens the Debug Preview dialog.
5.

Attach the Visual Studio debugger to the Kanzi Studio Preview process:

  1.

In Visual Studio select Debug > Attach to Process.
  2.

In the Attach to Process dialog:

    1.

In the Available Processes list select the `KanziPreview.exe` process titled Debug Preview.
    2.

In the Attach to box make sure that these code types are listed:

      - Managed (.NET 4.x) code
      - Native code

    3.

Click Attach.


6.

In Visual Studio insert the breakpoints in the Kanzi Engine plugin source code.
7.

In the Debug Preview dialog click OK.


Now when you interact with your application in the Kanzi Studio Preview, whenever one of the breakpoints you inserted in the code is hit, Visual Studio stops executing the code and you can debug your Kanzi Engine plugin.
