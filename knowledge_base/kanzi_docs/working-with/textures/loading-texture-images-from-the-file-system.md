---
title: Loading images from the file system
source: https://docs.kanzi.com/4.1.0/en/working-with/textures/loading-texture-images-from-the-file-system.html
---

# Loading images from the file system

You can create textures from images in Kanzi Studio or load and use images in your Kanzi application from the file system of the device where you run the application.

To load images from the file system:

1.

In Kanzi Studio create a project using the Application template.
2.

In the Node Tree create a node on which you want show a texture and in the Properties set the Material property to a material that supports textures. See Using material types and Using materials.

For example, in the Node Tree create a Box node and in the Properties set Material to VertexPhongTexturedMaterial.
3.

In the Node Tree select the node that you created in the previous step, in the Properties add the Texture property, and set it to a resource ID.

For example, set the Texture property to the resource ID BoxTexture.

This way you assign to the Texture property a resource ID which you later use to show a texture.
4.

In the Node Tree press Alt and right-click the node you created and select Alias. See Using aliases.

Kanzi Studio creates an alias pointing to the node from which you created the alias and adds it to the resource dictionary of its nearest ancestor node that contains a resource dictionary.

Use an Alias to get consistent access to a Kanzi node. You can use aliases to access nodes both in Kanzi Studio and using the Kanzi Engine API.
5.

In Kanzi Studio, select File > Export > Export KZB.

Kanzi Studio creates the kzb file and configuration files from your Kanzi Studio project. Kanzi Studio stores the exported files in the `<ProjectName>/Application/bin` directory or the location that you set in Project > Properties in the Binary Export Directory property. The kzb file contains all nodes and resources from your Kanzi Studio project, except the resources that you mark in a localization table as locale packs.

When you run your Kanzi application from Visual Studio, your application loads the kzb file and configuration files.
6.

Place the image that you want to use in the texture to the `<ProjectName>/Application/bin` directory.
7.

In Kanzi Studio, select File > Open Kanzi Command Prompt.

The Kanzi Command Prompt opens the Windows Command Prompt with the Kanzi environment variables set for the version of Kanzi for which you open a Kanzi Command Prompt.

Use the Kanzi Command Prompt to access Kanzi utilities and build tools, such as Gradle and CMake, without using absolute paths or setting environment variables.
**Tip:** You can find the Kanzi Command Prompt in the Windows Start Menu in the Rightware directory.
When you have more than one version of Kanzi installed, make sure that you launch a Kanzi Command Prompt for the version of Kanzi with which you want to work in that command prompt.
8.
In the Kanzi Command Prompt in the `<ProjectName>/Application` directory, run the script that generates a Visual Studio solution for the application.
```
generate_cmake_vs2022_solution.bat
```

This script generates a Visual Studio solution for the application in the directory `<ProjectName>/Application/build_vs2022`.
9.

In Visual Studio open the `<ProjectName>/Application/build_vs<Version>/<ProjectName>.sln` Visual Studio solution.

For example, if you named your Kanzi Studio project MyProject, the Visual Studio solution is called `MyProject.sln`.
10.

In Visual Studio in the Solution Explorer right-click the MyProject project and select Set as StartUp Project.
11.

In the C++ application load the texture.

```
// In the main class of the application use the onProjectLoaded()
// virtual function to load a file from the file system.
virtual void onProjectLoaded()
{
    // Get the Screen node of your application.
    ScreenSharedPtr screenNode = getScreen();
    // Get the Box node using the #Box alias.
    Model3DSharedPtr box = screenNode->lookupNode<Model3D>("#Box");
    // Load the texture from the <ProjectName>/Application/bin directory.
    box->addResource(ResourceID("BoxTexture"), "file://./Red.png");
}

```

12.

Select the solution configuration that you want to use and run your application.

During development, select the Debug configuration. When you are ready to create a version for production, select the Release configuration.

When you launch the application, Kanzi loads the image stored in `<ProjectName>/Application/bin` and creates a texture from the image. When Kanzi loads the application kzb file, it sets the texture to the node you get in the `Application::onProjectLoaded` function.
