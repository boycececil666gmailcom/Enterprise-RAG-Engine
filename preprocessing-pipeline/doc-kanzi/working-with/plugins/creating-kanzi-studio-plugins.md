---
title: Creating Kanzi Studio command plugins
source: https://docs.kanzi.com/4.1.0/en/working-with/plugins/creating-kanzi-studio-plugins.html
---

# Creating Kanzi Studio command plugins

Kanzi Studio plugins extend the functionality of Kanzi Studio and run in Kanzi Studio.

For example, you can extend the functionality of Kanzi Studio to:

- Automate tasks that take a lot of time to do manually in Kanzi Studio, or are prone to errors.
- Import and export content from Kanzi Studio, such as localization tables in a format that Kanzi Studio does not support
- Create editors that abstract the details and speed up the workflow, such as visualization tools that support work on your projects in Kanzi Studio.

You can present a Kanzi Studio plugin either:

- In a Kanzi Studio window that contains the plugin user interface.
- As commands that users can execute from the Kanzi Studio main menu or from a context menu, running the plugin without a user interface.

This topic covers how to create Kanzi Studio command plugins. To learn how to create Kanzi Studio window plugins, see Creating Kanzi Studio window plugins.

The Kanzi Studio plugin API is provided as a .NET framework assembly. You can find it in `<KanziInstallation>/Studio/Bin/PluginInterface.dll`. The Kanzi Studio plugin API provides access to data and commands in Kanzi Studio. When you want to use a Kanzi Studio plugin with different versions of Kanzi Studio, build the plugin with the `PluginInterface.dll` from each version of Kanzi Studio where you want to use that plugin.

To develop a Kanzi Studio command plugin:

1.

Create the base for a Kanzi Studio plugin. See Creating the base for a Kanzi Studio command plugin.
2.

Build and run your Kanzi Studio plugin. See Building and running a Kanzi Studio plugin.
3.

Add functionality to your Kanzi Studio plugin. See Adding functionality to your Kanzi Studio command plugin and Add multiple commands to your Kanzi Studio command plugin.
4.

Debug your Kanzi Studio plugin. See Debugging a Kanzi Studio plugin.

To find detailed information about the Kanzi Studio plugin API see:

- Overview of Kanzi Studio plugin API
- Kanzi Studio plugin API reference

## Creating the base for a Kanzi Studio command plugin

Kanzi Studio command plugins are plugins that you execute as commands and do not have a user interface. For example, use the command plugins to execute a command on the entire or the selected part of the node tree in your project.

Here you create the base for a Kanzi Studio command plugin where you then add functionality that extends the functionality of Kanzi Studio.

To create a Kanzi Studio command plugin:

1.

In Visual Studio select File > New > Project and create a Visual C# Class Library.
2.

In the Solution Explorer right-click the project name, select Add > Reference, and add references to files:

  1.

Select Assemblies > Framework targeting .NET Framework and add the reference to: `System.ComponentModel.Composition`.
  2.

Click Browseâ¦ and add the reference to the `<KanziInstallation>/Studio/Bin/PluginInterface.dll` file.

3.

In the Solution Explorer right-click the project name, select Properties, and:

  - In the Application tab set the Target framework to .NET Framework 4.8.
  - In the Build tab set the Platform target to x64.

4.

Open the `Class1.cs` file and add the using directive for the `System.ComponentModel.Composition` and the Kanzi Studio plugin API:

```
using System.ComponentModel.Composition;
using Rightware.Kanzi.Studio.PluginInterface;

```

5.

Before the definition of the command class where you implement the `PluginCommand` interface, use the export attribute to tell Kanzi Studio that the .dll is a plugin. In this example, you implement the plugin command in the `Class1` class.

```
[Export(typeof(PluginContent))]

```

6.

Set the `Class1` class to implement the `PluginCommand` interface, which you implement in the `Class1` class. Kanzi uses this class to create the plugin command.

  1.

Change

```
public class Class1

```

to

```
public class Class1 : PluginCommand

```

  2.

Implement the `PluginCommand` interface. For example, hover over `PluginCommand`, click , and select Implement Interface.

7.

In all functions replace this line with the code you want to execute:

```
throw new NotImplementedException();

```

Make sure that your plugin handles all its internal exceptions and does not let them reach the Kanzi Studio interface.

For example, set the functions in the `Class1` class to:

  - Use the `CommandPlacement` function to set the menu name of the plugin, and where you want to show the command to launch the plugin:

    - To show the plugin in the main menu use `ContextMenuPlacement.NONE`.
    - To show the plugin in the context menus invoked from nodes and resources, and the main menu use `ContextMenuPlacement.PROJECT_ITEM`.

```
public CommandPlacement CommandPlacement
{
    get
    {
        return new CommandPlacement("myPluginMenu", ContextMenuPlacement.NONE, false, null);
    }
}

```
**Tip:** To hide a plugin from the main and context menus, set the `CommandPlacement` function to return `null`. For example, hide a plugin when you want to execute a plugin command only by using a script to run Kanzi Studio commands. See Automating Kanzi Studio tasks.
```
public CommandPlacement CommandPlacement
{
get
{
return null;
}
}
```
- Use the `PluginContent.Name` function to set the internal name of your plugin. Kanzi uses the internal name of the plugin so that you can change the display name of your plugin without additional changes to the plugin.
```
public string Name
{
get
{
return "Internal plugin name";
}
}
```
- Use the `PluginContent.DisplayName` function to show the plugin name in the Kanzi Studio menu where you can launch the plugin.
```
public string DisplayName
{
get
{
return "Plugin display name";
}
}
```
- Use the `PluginContent.Description` function to set a brief description of what your Kanzi Studio plugin does. Kanzi Studio shows this description as a tooltip when a user hovers the mouse pointer over the plugin name in the menu.
```
public string Description
{
get
{
return "A tooltip with short description of what the plugin does.";
}
}
```
- Use the `CanExecute` function to set whether users can launch your plugin, and where they can launch your plugin:
- When set to `false`, Kanzi Studio shows the plugin in the main menu and the context menu, but users cannot launch the plugin.
- When set to `true`, users can launch the plugin.

Kanzi Studio provides the `KanziStudio` object to plugins. The `KanziStudio` object is the root object for data access and provides the current project, available commands, global undo and redo, and events related to project opening and closing.

For example, use this to enable the command only when a Kanzi Studio project is open

```
private KanziStudio studio;
public bool CanExecute(PluginCommandParameter parameter)
{
    return this.studio != null && this.studio.ActiveProject != null;
}

```

  - Add to the `Execute` function the code you want your plugin to run. For example, use this to print Hello world! to the Log window in Kanzi Studio when you run your plugin.

```
public void Execute(PluginCommandParameter parameter)
{
    studio.Log("Hello world!");
}

```

  - Use the `PluginContent.Initialize` function to place `studio` to a member variable.

```
public void Initialize(KanziStudio studio)
{
    this.studio = studio;
}

```

8.

Build and run the plugin. See Building and running a Kanzi Studio plugin.

Here you created just the base structure for your Kanzi Studio plugin, which only prints a message to the Kanzi Studio Log window. To make your plugin do more than that, add the code that you want your plugin to run to the `Execute` function. See Adding functionality to your Kanzi Studio command plugin and Add multiple commands to your Kanzi Studio command plugin.

To further develop your Kanzi Studio plugin, see Overview of Kanzi Studio plugin API and Kanzi Studio plugin API reference.
## Building and running a Kanzi Studio plugin

To build and run a Kanzi Studio plugin:

1.

In Visual Studio select Build > Build Solution to build the plugin .dll.
2.

Copy the Kanzi Studio plugin DLL file to the `%ProgramData%\Rightware\<KanziVersion>\plugins` directory.

If the `plugins` directory does not exist in `%ProgramData%\Rightware\<KanziVersion>`, create it.
**Tip:** In File Explorer, create a shortcut from your Kanzi Studio plugin DLL file and move the shortcut to the `%ProgramData%\Rightware\<KanziVersion>\plugins` directory.
When you build the plugin, you can see in the Output window the location where Visual Studio stored the plugin DLL file.
Tip
If your plugin has dependency DLLs, use a plugin manifest to declare the entry point. See Installing Kanzi Studio plugins.
3.
Open Kanzi Studio.
Kanzi Studio loads the plugins in the `plugins` directory and adds them to either the main menu or the context menus invoked from nodes and resources.
4.
In Kanzi Studio select the plugin main menu and select the plugin, or right-click a node in the Node Tree and select the name of your plugin to run your plugin.

## Adding functionality to your Kanzi Studio command plugin

After you create the base for a Kanzi Studio command plugin, add functionality to your plugin so that it does something useful. Here you create a plugin that deletes all Empty Node nodes that do not have child nodes.

To delete Empty Node nodes without child nodes using a Kanzi Studio plugin:

1.

Create the base for your Kanzi Studio command plugin. See Creating the base for a Kanzi Studio command plugin.
2.

In Visual Studio open the Visual Studio solution of your plugin and open the class library file that implements the `PluginCommand` interface.
3.

In the `Execute` function write the code that your plugin executes when you invoke the plugin command.

For example, to create a plugin that deletes all Empty Node nodes that do not have child nodes, add to `Execute` function:

```
// Your plugin executes the content of this function. Place your plugin code here.
public void Execute(PluginCommandParameter parameter)
{
    var items = parameter.Items;
    // Print to the Kanzi Studio Log window.
    studio.Log("Deleting all Empty Node nodes without child nodes");

    // When executing from the main menu, items passes empty value as a parameter.
    // When executing from the context menu, items passes the selected items as a parameter
    // (even when multiple items are selected).
    if (items != null && items.Any())
    {
        // If executed from the context menu, start the function that traverses
        // the node tree from the node where it is executed.
        TraverseTree(items);
    }
    else
    {
        // Check that a project is opened.
        if (studio != null && studio.ActiveProject!= null && studio.ActiveProject.Screen != null)
        {
            // If executed from the main menu, starts the function that traverses
            // the node tree from the first child of the Screen node.
            TraverseTree(studio.ActiveProject.Screen.Children);
        }
    }
}

// TraverseTree function traverses the node tree from the node where you launch the plugin.
private void TraverseTree(IEnumerable<ProjectItem> items)
{
    foreach (var item in items.ToArray())
    {
        // If the node is an Empty Node 2D or Empty Node 3D and does not have
        // any child nodes, delete it.
        if ((item is EmptyNode2D || item is EmptyNode) && !item.Children.Any())
        {
            // Delete the project item using a command. This enables you
            // to undo the action performed by the plugin.
            studio.Commands.DeleteProjectItem(new ProjectItem[] { item });
        }
        // Traverse the children of the current node.
        else if (item.Children.Any())
        {
            TraverseTree(item.Children);
        }
    }
}

```

4.

In the `CanExecute` function set where and how you can invoke the plugin command in Kanzi Studio.

```
public bool CanExecute(PluginCommandParameter parameter)
{
    // Allow running the plugin command from the context menu only when a single node in the scene
    // graph is selected. Zero items are called when executing the plugin from the main menu,
    // which sets the plugin to start traversing the node tree from the first child node of
    // the Screen node.
    var items = parameter.Items;
    return items != null && items.Count() <= 1;
}

```

5.

In Kanzi Studio create a project that includes several Empty Node nodes, some that have child nodes, and some without child nodes.
6.

Build and run the plugin. See Building and running a Kanzi Studio plugin.

When you execute the command, the plugin removes the Empty Node nodes which do not have any child nodes depending on where you invoke the plugin command:

  - If you execute the plugin command from the main menu, the plugin removes the Empty Node nodes without child nodes in the entire project.
  - If you right-click a node in the Node Tree and execute the plugin command from the context menu, the plugin removes the Empty Node nodes without child nodes in the context of the selected node.

To further develop your Kanzi Studio plugin, see Overview of Kanzi Studio plugin API and Kanzi Studio plugin API reference.
## Add multiple commands to your Kanzi Studio command plugin

After you create the base for a Kanzi Studio command plugin, add functionality to your plugin. You can create a Kanzi Studio command plugin that implements multiple commands. Here you create a plugin with commands that:

- Print to the Log the invalid kzb URLs in a Kanzi Studio project. See Logging invalid kzb URLs.
- Remove the invalid kzb URLs from a Kanzi Studio project. See Removing invalid kzb URLs.

The plugin finds and removes from the active project invalid kzb URLs that point to resources in the same project or a loaded referenced project.
### Logging invalid kzb URLs

To log invalid kzb URLs in a Kanzi Studio project:

1.

Create the base for a Kanzi Studio command plugin. See Creating the base for a Kanzi Studio command plugin.

For example, create a Visual Studio project named `InvalidKzbUrlFinder` that has a class named `ListInvalidKzbUrls` which implements the `PluginCommand` interface:

```
using System.ComponentModel.Composition;
using Rightware.Kanzi.Studio.PluginInterface;

namespace InvalidKzbUrlFinder
{
    [Export(typeof(PluginContent))]
    public class ListInvalidKzbUrls : PluginCommand
    {
        private KanziStudio studio;

        public void Initialize(KanziStudio studio)
        {
            this.studio = studio;
        }

        // Show the plugin command in the Kanzi Studio main menu named Kzb URL Checker.
        public CommandPlacement CommandPlacement =>
            new CommandPlacement("Kzb URL Checker", ContextMenuPlacement.NONE, false, null);

        // Set the internal name of the plugin command. This enables you to change the display
        // name of your command without additional changes to the plugin.
        public string Name => "LogInvalidKzbUrls";

        // Set the command name in the Kanzi Studio main menu.
        public string DisplayName => "Log Invalid Kzb URLs";

        // Set the tooltip for the command.
        public string Description => "Prints to the Log the invalid kzb URLs in the active project.";

        public bool CanExecute(PluginCommandParameter parameter)
        {
            return studio?.ActiveProject != null;
        }
    }
}

```

2.

In the class that implements the `PluginCommand` interface add the functions that get from the kzb URL of a resource the name of the project that contains the resource.

```
public static Project GetProjectFromKzbUrl(Solution solution, string urlCandidate)
{
    Project result = null;
    foreach (var project in solution.Projects)
    {
        var projectName = project.Name.Replace(" ", "_").ToLowerInvariant();
        if (urlCandidate?.StartsWith("kzb://" + projectName) == true)
        {
            result = project;
            break;
        }
    }

    return result;
}

public Project GetProjectFromKzbUrl(string urlCandidate)
{
    return GetProjectFromKzbUrl(studio.Solution, urlCandidate);
}

```

3.

Add the using directive for the `System.Linq` namespace.

The function you add in the next step uses the LINQ `Enumerable.Where` method.

```
using System.Linq;

```

4.

In the class that implements the `PluginCommand` interface add a function that checks whether a kzb URL points to an existing resource.

```
public static bool IsValidKzbUrl(Solution solution, Project project, string kzbUrl)
{
    var result = false;
    if (GetProjectFromKzbUrl(solution, kzbUrl) == project)
    {
        var projectNameInKzbFormat = project.Name.Replace(" ", "_").ToLowerInvariant();
        var itemPath = kzbUrl.Substring(("kzb://" + projectNameInKzbFormat + "/").Length);
        ProjectItem currentItem = project;

        var parts = itemPath.Split('/').Where(x => !string.IsNullOrEmpty(x));
        foreach (var part in parts)
        {
            currentItem = currentItem.GetChild(part);
            if (currentItem == null)
            {
                break;
            }
        }

        result = currentItem != null;
    }

    return result;
}

```

5.

In the class that implements the `PluginCommand` interface add a function that prints the invalid kzb URLs to the Log.

```
        private int LogKzbUrls(ProjectItem item, int count)
        {
            foreach (var projectItem in item.Children)
            {
                var properties = projectItem.Properties;
                foreach (var property in properties)
                {
                    var propertyValue = projectItem.Get(property);
                    var nodeResource = propertyValue as ResourceReferenceBase;
                    if (nodeResource != null)
                    {
                        var project = GetProjectFromKzbUrl(nodeResource.ResourceID);
                        if (project != null && !IsValidKzbUrl(studio.Solution, project, nodeResource.ResourceID))
                        {
                            studio.Log($"Invalid kzb URL \"{nodeResource}\" found in the \"{property.DisplayName}\" property of \"{projectItem.Path ?? projectItem.Name}\".");
                            count++;
                        }
                    }
                }

                count = LogKzbUrls(projectItem, count);
            }

            return count;
        }

```

6.

In the `Execute` function of the class that implements the `PluginCommand` interface write the code that your plugin executes when you invoke the plugin command.

```
        public void Execute(PluginCommandParameter parameter)
        {
            studio.Log("Finding invalid kzb URLs...");
            // Call the function that prints the invalid kzb URLs to the Log.
            var count = LogKzbUrls(studio.ActiveProject, 0);
            studio.Log($"This project contains {count} invalid kzb URLs.");
        }

```

7.

Build and run the plugin. See Building and running a Kanzi Studio plugin.

When you execute the command, the plugin prints to the Log the invalid kzb URLs, and for each kzb URL the node and property that uses the invalid kzb URL.

### Removing invalid kzb URLs

To remove invalid kzb URLs from a Kanzi Studio project:

1.

Implement a Kanzi Studio plugin that logs the invalid kzb URLs. See Logging invalid kzb URLs.
2.

In Visual Studio add to your plugin project a new class and set the class to implement the `PluginCommand` interface.

For example, add a class named `RemoveInvalidKzbUrls`:

```
using System.ComponentModel.Composition;
using Rightware.Kanzi.Studio.PluginInterface;

namespace InvalidKzbUrlFinder
{
    [Export(typeof(PluginContent))]
    class RemoveInvalidKzbUrls : PluginCommand
    {
        private KanziStudio studio;

        public void Initialize(KanziStudio studio)
        {
            this.studio = studio;
        }

        // Show the plugin command in the Kanzi Studio main menu named Kzb URL Checker.
        public CommandPlacement CommandPlacement =>
            new CommandPlacement("Kzb URL Checker", ContextMenuPlacement.NONE, false, null);

        // Set the internal name of the plugin command. This enables you to change the display
        // name of your command without additional changes to the plugin.
        public string Name => "RemoveInvalidKzbUrls";

        // Set the command name in the Kanzi Studio main menu.
        public string DisplayName => "Remove Invalid Kzb URLs";

        // Set the tooltip for the command.
        public string Description => "Removes the invalid kzb URLs from the active project.";

        public bool CanExecute(PluginCommandParameter parameter)
        {
            return studio?.ActiveProject != null;
        }

        public void Execute(PluginCommandParameter parameter)
        {
            throw new NotImplementedException();
        }
    }
}

```

3.

In the class that you added in the previous step create the function that removes the invalid kzb URLs.

```
private int RemoveKzbUrls(ProjectItem item, int currentCount)
{
    foreach (var projectItem in item.Children)
    {
        var properties = projectItem.Properties;

        foreach (var property in properties)
        {
            var propertyValue = projectItem.Get(property);
            var nodeResource = propertyValue as ResourceReferenceBase;
            if (nodeResource != null)
            {
                var project = ListInvalidKzbUrls.GetProjectFromKzbUrl(studio.Solution, nodeResource.ResourceID);
                if (project != null &&
                    !ListInvalidKzbUrls.IsValidKzbUrl(studio.Solution, project, nodeResource.ResourceID))
                {
                    projectItem.Set(property.Name, null);
                    currentCount++;
                }
            }
        }

        currentCount = RemoveKzbUrls(projectItem, currentCount);
    }

    return currentCount;
}

```

4.

In the `Execute` function write the code that your plugin executes when you invoke the plugin command.

```
        public void Execute(PluginCommandParameter parameter)
        {
            studio.Log("Removing invalid kzb URLs...");
            // Call the function that removes the invalid kzb URLs.
            var removedCount = RemoveKzbUrls(studio.ActiveProject, 0);
            studio.Log($"Removed {removedCount} invalid kzb URLs from the project.");
        }

```

5.

Build and run the plugin. See Building and running a Kanzi Studio plugin.

When you execute the command, the plugin removes the invalid kzb URLs.

To further develop your Kanzi Studio plugin, see Overview of Kanzi Studio plugin API and Kanzi Studio plugin API reference.
