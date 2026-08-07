---
title: Using Kanzi Engine plugins
source: https://docs.kanzi.com/4.1.0/en/working-with/plugins/installing-kanzi-engine-plugins.html
---

# Using Kanzi Engine plugins

Kanzi Engine plugins extend the functionality of Kanzi Engine. Kanzi Engine executes these plugins on target platforms.

Use a Kanzi Engine plugin to:

- Create custom nodes using the Kanzi Engine API, use them in your Kanzi Studio projects, and see in the Kanzi Studio Preview how they work.
- Create custom property types and messages using the Kanzi Engine API, and use them in your Kanzi Studio projects.
- Define the data entry points to your Kanzi application, and form the contract between the Kanzi application designer and developer.

To learn how you can use Kanzi Engine plugins, see:

- Extending the functionality of Kanzi Engine
- Tutorial: Get application data from a data source
- Node2D plugin example
- Node3D plugin example

## Adding Kanzi Engine plugins to a Kanzi Studio project

To add a Kanzi Engine plugin to a Kanzi Studio project:

1.

In the Library right-click Kanzi Engine Plugins and select Import Kanzi Engine Plugin.
**Tip:** You can automate the importing of Kanzi Engine plugins using a script. See Importing a Kanzi Engine plugin using a script.
2.
Select the DLL or JAR file of the plugin that you want to import and click Open.
Note
Starting with Kanzi Studio 3.9.5, the path of Kanzi Java plugins must follow this pattern:
- For debug, the path must be `lib/java/Debug/<PluginName>.jar`.
- For release, the path must be `lib/java/Release/<PluginName>.jar`.

See Changes in support for Debug and Release build types for Kanzi Engine Java plugins.

When you select in the Library > Kanzi Engine Plugins the plugin that you imported, in the Properties you can see a list of the content that the plugin brings to the Kanzi Studio project. For example, in the Properties you can see a list of property types, component, data source, render pass, node component, and trigger action types provided by the selected plugin.
3.

For DLL plugins, make sure that the settings in your Kanzi Studio project match the solution configuration that you use in Visual Studio to build your application and plugin projects.

For example, if you use the Release solution configuration in Visual Studio 2022, in your Kanzi Studio project in the Project > Properties set:

  - Preview Build Configuration to Release
  - Preview Visual Studio Version to 2022
  - Preview Working Directory to `..\Application\bin`.

With these settings you set the Kanzi Studio Preview to work with the plugin.
4.

In the Library > Kanzi Engine Plugins select the plugin and in the Properties make sure that the Is Enabled property is enabled.
**Tip:** Use the Is Enabled property to enable or disable any Kanzi Engine plugin in your project.
5.
Restart the Preview by pressing Ctrl F8, or by selecting Preview > Restart Preview.
You can now use the content provided by the Kanzi Engine plugin in your Kanzi Studio project.

## Checking a Kanzi Engine plugin for changes

Before you update a Kanzi Engine plugin in your Kanzi Studio project, you can compare the differences between the Kanzi Engine plugin that you currently use and another version of that plugin. Kanzi Studio compares the plugins and lists the differences and problems.

To check a Kanzi Engine plugin for changes:

1.

Build or copy the DLL or JAR files of a Kanzi Engine plugin to the same location where the previous version of the plugin is located.
2.

In Kanzi Studio in the Library > Kanzi Engine Plugins right-click a plugin and select Inspect Kanzi Engine Plugin.

Kanzi Studio compares the DLL or JAR of the Kanzi Engine plugin that is currently in use to the file that you copied in the previous step, and lists the differences.

## Updating a Kanzi Engine plugin in a project

When you want to use in a Kanzi Studio project a different version of a Kanzi Engine plugin, you must update that Kanzi Engine plugin in your Kanzi Studio project.

To update a Kanzi Engine plugin in a Kanzi Studio project:

1.

Build or copy the DLL or JAR files of a Kanzi Engine plugin to the same location where the previous version of the plugin is located.
2.

Update the Kanzi Engine plugin in one of these ways:

  - To update a specific Kanzi Engine plugin, in the Library > Kanzi Engine Plugins right-click that plugin and select Update Kanzi Engine Plugin.

When Kanzi Studio loads the new version of the plugin, it shows the changes in the properties and classes defined in the plugin.
  - To update all Kanzi Engine plugins in a project or solution, in the Library right-click Kanzi Engine Plugins and select either:

    - Update Kanzi Engine Plugins in Project to update the plugins in the Kanzi Studio project
    - Update Kanzi Engine Plugins in Solution to update the plugins in the Kanzi Studio project and referenced projects

When Kanzi Studio loads the new versions of the plugins, it prints to the Log window the changes in the properties and classes defined in the plugins.
  - To update Kanzi Engine plugins using a script, see Updating a Kanzi Engine plugin using a script and Updating all Kanzi Engine plugins in a project or solution using a script.

## Removing Kanzi Engine plugins from a project

When you remove a Kanzi Engine plugin from a Kanzi Studio project, Kanzi Studio removes the reference to the Kanzi Engine plugin, but does not delete the dll file of the Kanzi Engine plugin you removed.

To remove a Kanzi Engine plugin from a Kanzi Studio project in the Library > Kanzi Engine Plugins right-click the plugin you want to remove and select Delete.
