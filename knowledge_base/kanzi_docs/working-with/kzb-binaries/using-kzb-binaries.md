---
title: Using kzb files
source: https://docs.kanzi.com/4.1.0/en/working-with/kzb-binaries/using-kzb-binaries.html
---

# Using kzb files


A kzb file contains contents of a Kanzi Studio project. To run your Kanzi application, you must export the contents of the Kanzi Studio project of that application to a kzb file.
## Creating a kzb file from a Kanzi Studio project


To create a kzb file from a Kanzi Studio project, open your Kanzi Studio project and select File > Export > Export KZB.

Kanzi Studio creates in the `<ProjectName>/Application/bin` directory these files:

- `<project_name>.kzb` contains the content of your project in binary format.
- `<project_name>.kzb.cfg` contains a list of kzb files. If your Kanzi application includes application code, Kanzi by default configures the C++ application to load the kzb files listed in this file

```
configuration.binaryName = "<project_name>.kzb.cfg"

```

- (Optional) `<project_name>.kzb.txt` contains a list of paths to project items in the exported kzb file. You can use these paths to access the content of your Kanzi application in the application code.

To set whether you want to export this file, select Edit > User Preferences and in the Advanced tab enable the Create table of contents of kzb file setting.
- (Optional) `<project_name>.kza` contains your project in XML format.

To create this file, before you export the kzb file select Edit > User Preferences and in the Advanced tab enable the Create XML version (kza) of kzb file setting.


> **Tip:** Kanzi Studio by default names the kzb file `<project_name>.kzb`. You can set the name of the kzb file in the Project > Properties using the Binary File Name property.
>
> Tip
>
> When you want to permanently remove all kzb files exported from a project, select File > Export > Delete Exported Binaries.
>
> Kanzi Studio deletes all exported files from the directory set in the Node Tree > Properties in the Binary Export Directory property. This command deletes all exported files, including those from other projects.
## Opening a kzb file


Kanzi comes with the kzb Player you can use to open kzb files on Windows. For example, open kzb files with the kzb Player to visually inspect the content in kzb files. You can find the kzb Player in the `<KanziInstallation>/Studio/Bin` directory.

To run a Kanzi application on Windows, you need to have Microsoft Visual C++ 2015-2019 Redistributable (x86) installed.

See Deploying Kanzi applications to Windows.

To open a kzb file:

1.

In Kanzi Studio main menu, select File > Export > Export KZB.

Kanzi Studio exports the kzb file from your project.
2.

Open the command line in the `<KanziInstallation>/Studio/Bin` directory and run

```
kzb_player_GL_vs2022_Release_DLL.exe "C:\<KanziWorkspace>\Projects\MyProject\Binary\myproject.kzb"

```


## Setting how Kanzi loads a kzb file


The presence of the Screen node in a kzb file determines how Kanzi loads a kzb file.

To set whether Kanzi Studio exports the Screen node to the kzb file of that project, in the Node Tree select the Screen node and in the Properties set the Disable KZB Export property to:

- Disabled to export the kzb file with the Screen node. This is the default setting. You can start your Kanzi application with a kzb file that has a Screen node. If you load during application runtime a kzb file that contains a Screen node, you replace the Screen node that the application uses.
- Enabled to export the kzb file without the Screen node. You can load a kzb file without a Screen node only during application runtime, when your Kanzi application already has a Screen node.
