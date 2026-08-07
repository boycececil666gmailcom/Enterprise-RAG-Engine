---
title: Using resource files
source: https://docs.kanzi.com/4.1.0/en/working-with/resource-files/resource-files.html
---

# Using resource files

Kanzi Studio lists in the Library > Resource Files references to files in the resource directories of a Kanzi project. Kanzi Studio synchronizes the content of Resource Files with the files in the resource directories.

In projects that you create using the Kanzi Studio project template, the resource directories are located in the `<KanziWorkspace>/Projects/<ProjectName>` directory. In projects that you create using other templates, they are located in the `<KanziWorkspace>/Projects/<ProjectName>/Tool_project` directory.

Whenever you modify the files in a resource directory, Kanzi Studio updates them in your project.

Resource files are part of a Kanzi application, but do not consume CPU or GPU resources until you instantiate them.

In Kanzi Studio, the Library > Resource Files contains these directories:

- 3D Assets. Kanzi Studio stores the 3D assets that you import to your project in `<ProjectName>/Tool_project/3D Assets`. See Importing 3D assets.
- Images. Kanzi Studio stores image files that you import to your project in `<ProjectName>/Tool_project/Images`. See Importing images.
- Generic. Kanzi Studio stores the files that you add to the Resource Files and that Kanzi Studio does not recognize as either a 3D asset, image, font, or shader, in `<ProjectName>/Tool_project/Generic`.

Kanzi Studio does not process the resources in this directory, but exports them to the kzb file.

For example, if your project uses plugins that extend Kanzi to handle new file formats or data types, you can place such files in the Generic directory. This way you can load files from a kzb file instead of the target device file system.
- Fonts. Kanzi Studio stores font files that you import to your project in `<ProjectName>/Tool_project/Fonts`. See Importing fonts.
- Shaders. Kanzi Studio stores shader files that you create in your project or add to the Resource Files in `<ProjectName>/Tool_project/Shaders`. See Shaders.

## Adding resource files to a Kanzi Studio project

To add resource files to a Kanzi Studio project:

- Drag files from File Explorer to the Library > Resource Files.

Kanzi Studio copies the files to the resource directory that corresponds to the type of each file.

For example, Kanzi Studio copies PNG image files to `<ProjectName>/Tool_project/Images` or `<ProjectName>/Images`.
- In File Explorer, copy files to the resource directories of a Kanzi Studio project.

Kanzi Studio shows the files in the Library > Resource Files.

When you add 3D assets, images, and fonts to the Resource Files, they are not available as project assets in Kanzi Studio. To make them available as project assets, import the assets to the project. See Importing.
## Removing resource files from a Kanzi Studio project

When you remove files from a project resource directory, Kanzi Studio keeps in the Resource Files the reference to the removed files. This way you can replace the removed files in the project without losing references to those files.

To remove a resource file from a Kanzi Studio project, in the Library > Resource Files right-click the file and select Delete.

Kanzi Studio removes the file from the Resource Files and deletes it from the project resource directory.
