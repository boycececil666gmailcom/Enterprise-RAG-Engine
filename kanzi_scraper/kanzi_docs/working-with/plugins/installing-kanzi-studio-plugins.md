---
title: Installing Kanzi Studio plugins
source: https://docs.kanzi.com/4.1.0/en/working-with/plugins/installing-kanzi-studio-plugins.html
---

# Installing Kanzi Studio plugins


Kanzi Studio plugins extend the functionality of Kanzi Studio and run in Kanzi Studio.

For example, you can extend the functionality of Kanzi Studio to:

- Automate tasks that take a lot of time to do manually in Kanzi Studio, or are prone to errors.
- Import and export content from Kanzi Studio, such as localization tables in a format that Kanzi Studio does not support
- Create editors that abstract the details and speed up the workflow, such as visualization tools that support work on your projects in Kanzi Studio.


To install a Kanzi Studio plugin:

1.

Copy the Kanzi Studio plugin DLL file to the `%ProgramData%\Rightware\<KanziVersion>\plugins` directory.

If the `plugins` directory does not exist in `%ProgramData%\Rightware\<KanziVersion>`, create it.

> **Tip:** In File Explorer, create a shortcut from your Kanzi Studio plugin DLL file and move the shortcut to the `%ProgramData%\Rightware\<KanziVersion>\plugins` directory.
>
> When you build the plugin, you can see in the Output window the location where Visual Studio stored the plugin DLL file.
>
> Tip
>
> To install a plugin that has dependency DLLs:
>
> 1.
>
> In the `plugins` directory, create a subdirectory for your plugin and place all plugin files there. For example:
>
> ```
> plugins/
> MyPlugin/
> MyPlugin.manifest.json
> MyPlugin.dll
> SomeDependency.dll
>
> ```
>
> 2.
>
> In the subdirectory, create a manifest file with any name ending in `.manifest.json` that declares the entry point:
>
> ```
> {
> "entryPoint": "MyPlugin.dll"
> }
>
> ```


Kanzi Studio loads only the declared entry point DLL and resolves dependencies from the same directory on demand.
2.

Open Kanzi Studio.

Kanzi Studio loads the plugins in the `plugins` directory and adds them to either the main menu or the context menus invoked from nodes and resources.

> **Tip:** When you download a Kanzi Studio plugin from the internet, Windows can block access to the plugin files, which prevents Kanzi Studio from loading the plugin.
>
> If a plugin does not load in Kanzi Studio:
>
> 1.
>
> Open the Kanzi Studio log file
>
> ```
> %USERPROFILE%/AppData/Local/Temp/KanziStudioLogs/KanziStudio.log
>
> ```
>
> 2.
>
> If the log contains this error message:
>
> `Plugin loading failed for: <PathToPlugin>. Error "Unable to load one or more of the requested types."`
>
> Open Windows PowerShell in the plugin directory, and execute this command:
>
> ```
> Get-ChildItem . -Recurse | Unblock-File
>
> ```


This way you unblock all the files in the directory.
  3.

Restart Kanzi Studio.


## Hot reloading plugins


Kanzi Studio monitors the `plugins` directory for changes while it is running:

- When you add a plugin DLL or a plugin subdirectory with a manifest file, Kanzi Studio automatically loads the plugin.
- When you update an existing plugin DLL, Kanzi Studio reloads it with the new version.
- When you remove a plugin, Kanzi Studio automatically unloads it, closes any open plugin windows, and removes the associated menu items.


You do not need to restart Kanzi Studio for these changes to take effect.
