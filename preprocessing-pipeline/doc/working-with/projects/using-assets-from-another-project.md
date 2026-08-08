---
title: Combining Kanzi Studio projects into a Kanzi application
source: https://docs.kanzi.com/4.1.0/en/working-with/projects/using-assets-from-another-project.html
---

# Combining Kanzi Studio projects into a Kanzi application

You can combine the content of several Kanzi Studio projects into a single Kanzi application. This allows you to:

- Distribute Kanzi application development across several teams. Each team can work on a different part of the same application at the same time.
- Include in your Kanzi applications content available only in kzb files.
- Use Kanzi Studio projects that only hold resources that you want to use in multiple projects.
- Simplify the structure of your Kanzi application by splitting it into several Kanzi Studio projects.

For example, when you are developing an in-vehicle infotainment application consisting of several applications, you can develop each of these applications in one or more Kanzi Studio projects. You then use one Kanzi application to combine these Kanzi Studio projects into a single Kanzi application.

To combine Kanzi Studio projects into a single Kanzi application:

- Learn how to structure Kanzi applications that contain multiple Kanzi applications. See Kanzi Studio solution structure.
- Use prefabs and resources from Kanzi Studio projects. See Using prefabs and resources from Kanzi Studio projects.
- Use prefabs and resources from kzb files. See Using prefabs and resources from kzb files.
- Merge content from referenced Kanzi Studio projects. See Merging content from referenced Kanzi Studio projects.

To use theming and localization when you combine multiple Kanzi Studio projects into a Kanzi application, you must make the theme groups and localization tables accessible to the Screen node of the main project of your application. See Using theming and localization in multiple Kanzi Studio projects combined into a Kanzi application.

Learn how to combine content from Kanzi Studio projects by completing a tutorial. See Tutorial: Combine Kanzi Studio projects into a single Kanzi application.
## Kanzi Studio solution structure

A Kanzi Studio solution is a Kanzi Studio project that you use to combine Kanzi applications into a single Kanzi application.

When you create a Kanzi solution, use these guidelines:

- The solution project is the main Kanzi Studio project of your Kanzi application. You use it to combine related Kanzi Studio projects and to build the application code of all Kanzi applications in that solution.
- When you create a solution project, in Kanzi Studio use one of these templates that are most suitable for the type of application that you are creating:

  - Application template creates a Kanzi Studio project with a Kanzi Engine application.
  - Application with Kanzi Engine plugin template creates a Kanzi Studio project with a Kanzi Engine application that contains a Kanzi Engine plugin.
  - Application with data source plugin template creates a project with a Kanzi Engine application that contains a data source plugin template.
  - Android application template creates a Kanzi Studio project with a Kanzi Android framework-based application.
  - Android application with Java plugin template creates a Kanzi Studio project with a Kanzi Android framework-based application that contains a Kanzi Engine Java plugin.

See Creating a project.
- In the Android Studio or Visual Studio projects of the Kanzi Studio solution add the application code where you define the logic of your Kanzi application.
- If a Kanzi Studio project that you want to add to a Kanzi Studio solution contains application code, add the Visual Studio projects of such projects to the Visual Studio solution of the Kanzi solution project.
- Create or pick a project that is suitable for being a solution project where you combine Kanzi Studio projects and kzb files into a single Kanzi application.

For example, this can be a project that contains only application code and gets the nodes and resources from other projects or files, or an existing application that serves as a base for all other applications.
- When you export kzb files for a Kanzi solution, Kanzi Studio exports the kzb files from all Kanzi Studio projects in the solution and copies them to the `Application/bin` directory of the solution project. You can set this location in the Project > Properties in the Binary Export Directory property of the solution project.

When you add Kanzi Studio projects to a Kanzi solution, use these guidelines:

- For projects that you want to add to a solution use the Kanzi Studio project template and define the application logic of all such projects in the Visual Studio solution of your Kanzi solution. See Creating a project.
- When you want to create a project to store common resources that you want to share across projects in a Kanzi solution, press Alt and right-click Library > Project References, and select New Resource Project.

A resource project contains only the Screen node in the node tree and does not contain the default Kanzi Studio project resources, such as the Default Texture and DefaultBackground textures.
- Place the projects that you want to add to a solution in the root directory of the solution project. Do this even if these projects otherwise form a hierarchy.

For example, if you use one project to share resources and other projects refer to it, keep that resource project in the root directory of the solution project.
- When you add to a Kanzi solution a project that refers to external files, copy such files to the directory set in the Preview Working Directory property in the project properties of the Kanzi solution project. By default this is the `Application/bin` directory of the Kanzi solution project.
- Update the solution build scripts when you add new dependencies to a solution.
- If you want to keep the application logic in a project that you add to a solution, when you create a project in Kanzi Studio use the Application, Application with Kanzi Engine plugin, or Application with data source plugin template and add the Visual Studio projects of such project to the Visual Studio solution of the Kanzi solution project. When you do this, make sure to:

  - Update the solution build scripts to include the projects you added.
  - Configure the Visual Studio project of the solution to build and copy the content of the `Application/bin` directory and dependencies used by the project to the `Application/bin` directory of the solution. In Visual Studio solution of the Kanzi solution add to the main project Property Pages > Configuration Properties > Build Events > Pre-Build Event > Command Line:

```
if not exist "..\..\..\bin" mkdir ..\..\..\bin

```

and for each project you add to a Kanzi solution add:

```
xcopy ..\..\..\..\<ProjectName>\Application\bin ..\..\..\bin  /Y

```

- Set all Kanzi Studio projects in the same solution to use the same color workflow. See Color workflow.

## Using prefabs and resources from Kanzi Studio projects

To use prefabs and resources from Kanzi Studio projects:

1.

Open or create a Kanzi Studio project where you want to use content from other Kanzi Studio projects.

From here on this project is referred to as the referencing project.
2.

In the Library, press Alt and right-click Project References, select Existing Project, select a Kanzi Studio project from which you want to use content in the referencing project, and click Open.

Kanzi Studio loads the project in a new tab. If that project contains project references, Kanzi Studio loads the projects to which the references point.

From here on these projects are referred to as the referenced projects.

In the project tabs the Preview icon  marks the project which is active in the Preview.
**Tip:** To view a project in the Preview window, in the project tab either:
- Right-click the tab of that project and select Show in Preview. Kanzi Studio shows the project in the Preview, but does not select the project.
- Double-click the tab of that project. Kanzi Studio shows the project in the Preview and selects the project.
**Tip:** The order of project references in the Library > Project References determines the order in which Kanzi loads the kzb files of the projects when you run your application.
3.
In the Preview click Restart and in the Kzb export dialog click Yes to export the kzb files of the referenced projects.
Kanzi Studio creates the kzb file and configuration files from the referenced projects.
This way you make the content of the referenced projects available to the Preview of the referencing project.
Tip
By default when you start or restart the Preview Kanzi Studio asks whether you want to export the kzb files of the referenced projects. To set Kanzi Studio to always export the kzb files without asking, either:
- In the Kzb export dialog enable the Do not ask me again option and click Yes.
- Select Edit > User Preferences and in the Advanced tab set the value of the Referenced project kzb file export behavior setting to Always export.
**Tip:** When the project that Kanzi Studio shows in the Preview or any of the referenced projects contain changes that you have not yet exported to the kzb files of the projects, in the Preview the Restart button is orange.
To see the projects whose content in the Preview is outdated, hover over the button.
4.
In the project tab bar, select the referenced project from which you want to use a prefab or resource.
5.
To make prefabs and resources available in Kanzi Studio, in the dropdown menus of the referencing project either:
- In the Prefabs or Library select the prefab or resource and in the Properties add and set the Visibility Across Projects property to Public.
In the Prefabs and Library a green icon in the top left corner marks the public items.
Tip
To make an item public directly in the Library or Prefabs, right-click the item and select Make Public.
- Select Project > Properties and in the Properties set the Resource Visibility Across Projects property to Public.
When you set the Resource Visibility Across Projects property of a project to Public, you make all resources of that project available in the dropdown menus of referencing projects.
Kanzi Studio marks public projects with a green marker in the top left corner of the project tab.
Tip
To make a project public directly from the project tab, right-click the project tab and select Make Public.
6.
Use the content from the referenced project:
- To use a prefab, in the Node Tree, create either a Prefab Placeholder or a Prefab View node where you want to use the prefab, and in the Properties set the Prefab Template property to the prefab that you made available in the previous step.
Kanzi Studio automatically sets the Prefab Template property to use the kzb URL of the prefab. You can control prefabs from referenced projects. See Customizing and controlling prefabs from Kanzi Studio projects.
- To use a resource, in the Node Tree, select the node where you want to use the resource and in the Properties set the property where you want to use the resource to the resource that you made available in the previous step.
Kanzi Studio automatically sets the property to use the kzb URL of the resource.
7.
(Optional) Customize and control the appearance of prefabs. See Customizing and controlling prefabs from Kanzi Studio projects.

## Editing referenced projects

You can edit the content of a referenced project by selecting that project in the project tab. However, to make the editing of a referenced project easier, create a cross-reference between referenced projects. This way you see the content of the main project in a referenced project and do not have to switch between the main and referenced projects when you edit the content of a referenced project.

To edit a referenced project in the context of your main project:

1.

In the main project:

  1.

From the Node Tree, drag the root node under the Screen node to the Prefabs.
  2.

In the Prefabs, select the root node prefab. In the Properties, set the Visibility Across Projects property to Public.

This way you create from the root node a prefab that you can use in a referenced project.
2.

In the project tab, double-click the tab of a child referenced project to start the Preview from that project:

  1.

In the Library, right-click Project References and create a project reference to the main project.
  2.

In the Node Tree, delete the root node, press Alt and right-click the Screen node, and create a Prefab Placeholder node. In the Properties:

    - Set the Prefab Template property to the root node of the main project.
    - Add and enable the Resources > Disable KZB Export property.

This way the content of the referenced node is not exported to the project kzb file.

Now, you can view in the Preview the referenced project content in the context of the main project. This makes it easier to edit the content of the referenced project.
## Using prefabs and resources from kzb files

To use prefabs and resources from kzb files:

1.

Open or create a Kanzi Studio project where you want to use content from a kzb file.
2.

In the Library, press Alt and right-click Project References, select Existing .kzb, select a kzb file from which you want to use content in the target project, and click Open.

If the kzb file refers to other kzb files, you must also add the references to those kzb files.
3.

Use content from the kzb file:

  - To use a prefab, in the Node Tree, create either a Prefab Placeholder or a Prefab View node where you want to use the prefab, in the Properties set the Prefab Template property to <ResourceID>, and enter the kzb URL of the prefab you want to use.
  - To use a resource, in the Node Tree, select the node where you want to use the resource, in the Properties set the property where you want to use the resource to <ResourceID>, and enter the kzb file URL of the resource you want to use.

## Customizing and controlling prefabs from Kanzi Studio projects

In a Kanzi solution, when you use prefabs from a Kanzi Studio project, you can set the content and appearance of these prefabs. You can do this by using a property type in the root node of each prefab that you bind to the prefab content that you want to control.

To control prefabs from Kanzi Studio projects:

1.

Open or create a project and add to that project a prefab from a Kanzi Studio project. See Using prefabs and resources from Kanzi Studio projects.

From here on this project is referred to as the target project.
2.

In the project tab bar, select the project that contains the prefab that you want to control. In the Prefabs, select the prefab and in the Properties next to the property with which you want to control the prefab, click .

Kanzi Studio creates from that property a custom property, adds it to the root node of that prefab, and creates a `##Template` binding to the property in the root node of that prefab.

This allows you to edit the appearance of the prefab from the root of the prefab.

For example, if you want to control the progress bar of a music player using a property called Progress, click  next to that property.

From here on this project is referred to as the source project.
3.

In the Preview, click  to restart the Preview, and export the kzb file of the source project.
4.

In the project tab bar, select the target project, in the Node Tree select the node that you use to instantiate the prefab from the source project that you want to control. In the Properties, add the custom property that you created in the previous step.

You can now use the property in the target project to control the prefab from the source project.

## Merging content from referenced Kanzi Studio projects

When you want to bring content from referenced Kanzi Studio projects, you can merge the items that you need.

To merge content from referenced Kanzi Studio projects, in the Library > Project References, right-click the source project from which you want to bring content and select Merge Project.

Merge Project allows you to import only the selected items to the target project. When merging, you can select the project items that you want to import and resolve conflicts for items that exist in both projects. Kanzi Studio merges nodes from the source project to a new prefab. Kanzi Studio creates the nodes and resources even if they exist in the target project and you have not merged it before from the same project reference (in which case it is marked as identical). See Merging projects.
## Loading projects that refer to the same referenced project

Kanzi Studio does not support loading of the same project in multiple instances of Kanzi Studio. In the Library, Kanzi Studio marks with red type project references that are already loaded in another instance of Kanzi Studio. If the kzb file of that project exists, the Kanzi Studio Preview shows the content of that kzb file. If you unload a referenced project, the Preview does not show the content of that project.

When you want to load a Kanzi Studio project as a project reference in multiple Kanzi Studio projects, make those projects part of the same Kanzi Studio solution.

For example, if you have Kanzi Studio solutions named MainProject1 and MainProject2, which both contain a project reference to the Resources project:

1.

Create a Kanzi Studio project.
2.

In the Library > Project References, create project references for the MainProject1 and MainProject2 Kanzi Studio projects.

You can now use the same instance of Kanzi Studio to edit the MainProject1, MainProject2, and Resources projects.
## Using theming and localization in multiple Kanzi Studio projects combined into a Kanzi application

To use theming and localization when you combine multiple Kanzi Studio projects into a Kanzi application, you must make the theme groups and localization tables accessible to the Screen node of the main project of your application in one of these ways:

- Define the theme groups and localization tables in the main project of your application.
- Merge the theme groups and localization tables from referenced projects to the main project that contains the Screen node. You can then use resource IDs to access the resources in the theme groups and localization tables from the referenced projects. See Merging projects.
- Contact the Rightware support team and request the Kanzi Engine plugins that allow you to use theming and localization across multiple Kanzi Studio projects and kzb files. See Submitting a support request.
