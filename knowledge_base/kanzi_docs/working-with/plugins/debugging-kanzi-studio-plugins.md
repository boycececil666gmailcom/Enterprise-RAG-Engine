---
title: Debugging Kanzi Studio plugins
source: https://docs.kanzi.com/4.1.0/en/working-with/plugins/debugging-kanzi-studio-plugins.html
---

# Debugging Kanzi Studio plugins

## Debugging a Kanzi Studio plugin


To debug a Kanzi Studio plugin:

1.

In Visual Studio create and build your Kanzi Studio plugin. See Creating the base for a Kanzi Studio command plugin and Creating the base for a Kanzi Studio window plugin.
2.

In File Explorer, create a shortcut from your Kanzi Studio plugin DLL file and move the shortcut to the `%ProgramData%\Rightware\<KanziVersion>\plugins` directory.

When you build the plugin, you can see in the Output window the location where Visual Studio stored the plugin DLL file.
3.

In Visual Studio add the break points where you want to debug your plugin.
4.

In Visual Studio select Debug > Attach to Process â¦, in the Available Processes select `KanziStudio.exe` and click Attach.
5.

Open Kanzi Studio and run the plugin.

## Using the Kanzi Studio Command History


Use the Kanzi Studio Command History to view the commands you have executed in a Kanzi Studio project.

To open the Command History window in the Kanzi Studio main menu select Edit > Command History or press the Ctrl Shift U.

In the Command History window:

- Executed lists the commands you have executed. To undo these commands one at a time, select Edit > Undo or press the Ctrl Z.
- Undone lists the commands you have executed and then undone. To redo these commands one at a time, select Edit > Redo or press the Ctrl Y.
