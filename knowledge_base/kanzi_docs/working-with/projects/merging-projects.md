---
title: Merging projects
source: https://docs.kanzi.com/4.1.0/en/working-with/projects/merging-projects.html
---

# Merging projects

When merging projects you can reuse resources and nodes you created in another project. Merging projects allows you to import a complete project or only selected resources and nodes. During merging Kanzi provides conflict resolution.

Kanzi provides these options for bringing content from other projects:

- You can bring an entire project to the current project. See Importing projects.
- You can merge 3D assets from a 3D asset file. See Merging 3D assets.
- You can bring to the current project only a part of another project. See Merging content from referenced Kanzi Studio projects.
- You can share individual project items. See Sharing project items.
- If you want to import collections of ready-made content, use Kanzi Studio asset packages.

See Asset packages.
- If you want to import the assets that you created with third-party tools, use Kanzi Studio importing tools. See Importing.

## Merging Kanzi Studio projects

To merge projects:

1.

Select File > Import > Merge Project, select the project you want to merge (source project) to the currently open project (target project), and click Open.

The Project Merge dialog opens.
2.

In the Project Merge dialog set:

  - Select referenced items. Select the checkbox when you want Kanzi Studio to automatically select all items to which the selected item refers.

For example, when you check the Select referenced items checkbox and select a mesh that has a material, Kanzi Studio studio automatically selects the material, material type, and shaders used by the mesh you selected.
  - **Transformations**. If Kanzi Studio encounters a conflict in object transformations when an object in the target is replaced with an object from the source, set Keep transformations from to:

    - Target Project: <ProjectName> to keep the object transformations you use in the target. Kanzi Studio remembers all transformation changes you made to the objects in Kanzi Studio.
    - Source Project: <ProjectName> to import the object transformations you use in the source.

  - **Materials**. If Kanzi Studio encounters a conflict in object materials when an object in the target is replaced with an object from the source, set Keep materials from to:

    - Target Project: <ProjectName> to keep the materials you use for the objects in the target. Kanzi Studio remembers all material changes you made to the objects in Kanzi Studio.
    - Source Project: <ProjectName> to import the materials you use for the objects in the source.

3.

Select the checkboxes next to the items you want to merge from the source to target. Depending on the existence of the selected item in the target project, the name of the item is written using:

  - **White** font. Items exist in the source, but not in the target. When you select such items, Kanzi Studio creates them in the target.
  - **Red** font. Items exist in both the source and target, but differ between the two.

Before you can continue with the merging, you have to resolve conflicts by choosing to use either the item in the target or the source.
  - **Purple** font. Items exist in the target, but not in the source. When you select such items, Kanzi Studio removes them from the target.

4.

If you are merging projects with data sources that use locally stored data, see Merging projects with data sources that use locally stored data.
5.

If you are merging projects that contain Kanzi Engine Plugins, see Merging projects with Kanzi Engine plugins.
6.

Resolve conflicts. When your target and source both contain the same item and properties of this item differ, you have to decide which properties you want to keep:

  - Click Resolve to source to use the values in the source to resolve all conflicts.
  - Click Resolve to target to use the values in the target to resolve all conflicts.
  - Click Use base project to select a base project for resolving conflicts between the target and the source. For example, Use base project is useful when you are merging two projects or assets that are modifications of an initial project.

When using three-way merge, this is how conflict resolution works in Kanzi Studio:

    - If the difference is only between the base project and the target, Kanzi Studio uses the change in the target.
    - If the difference is only between the base project and the source, Kanzi Studio uses the change in the source.
    - If the change is between both the base project and the target, and the source and the target, you have to resolve the conflict.

  - To resolve conflicts manually, select the item in the source tree and in the conflicts pane select for each property whether you want to keep the value used in the target or the source.

    - You can select several properties and click Resolve to Target to keep the values used in the target or Resolve to Source to keep the values used in the source.
    - You can select a single value you want to keep from the Target or Source column.

Once you have resolved all the conflicts, the font color of the item name in the source tree changes to green.
7.

Click Merge. Kanzi Studio merges the source with the target by placing the content of source into the corresponding places of the target.

## Merging projects with Kanzi Engine plugins

When you merge projects with Kanzi Engine plugins that have the same name, but different component types, data sources, messages, or property types, you cannot resolve the conflict in the Project Merge tool.

To merge projects with conflicting Kanzi Engine plugins:

1.

In Kanzi Studio open the project which does not use the correct version of the Kanzi Engine plugin.
2.

In the Library > Kanzi Engine Plugins right-click the plugin and select Update Kanzi Engine Plugin.
3.

Merge the Kanzi Studio projects. See Merging Kanzi Studio projects.

## Merging projects with data sources that use locally stored data

Typically the data in a data source you merge to a Kanzi Studio project is provided by a server to which your application connects. If, however, the source files of the data source you want to merge are stored locally in the source project, you must manually copy them from `<SourceProjectName>/Application/bin` to `<TargetProjectName>/Application/bin`. If you do not copy the data files to the target project, the Preview fails to start.
## Responding to kzm file changes

When Kanzi Studio detects that kzm files in the project directory changed outside of Kanzi Studio, for example, after a `git pull` or a file copy from another project, it shows a **Project modified** notification dialogue with these options:

- Reload â reloads the project from disk. If you have unsaved local changes, reloading discards them.
- Merge â opens the Project Merge dialog so you can selectively merge the on-disk changes into your local version. This option is only available when you have unsaved local changes.
- Ignore â keeps your current project state and discards the on-disk changes.

Kanzi Studio monitors all files with `.kzm` extensions in the project directory and its subdirectories.
## Merging projects using version control tools

After configuring your version control tool you can use the Kanzi merge tool for Kanzi project updating and merging. For the integration Kanzi requires a version control tool that provides the necessary parameters to the Kanzi merge tool.
|

Example of parameter types |

Description |
|

MINE |

The parameter for the source project. |
|

THEIRS |

The parameter for the target project. |
|

BASE |

The parameter for the base project. |
|

MERGED |

The parameter for the merged project. |
## Integrating the Kanzi merge tool with a version control tool

To integrate the Kanzi merge tool with a version control tool:

1.

Configure your version control tool to use the Kanzi merge tool (`<KanziInstallation>/Studio/Bin/KanziMergeTool.bat`) for .kzproj files.
2.

Pass to your version control tool the absolute path to the `KanziStudio.exe`. For example, `C:\Program Files\Rightware\Kanzi\Studio\Bin\KanziStudio.exe`.
3.

Set the version control tool parameters for the Kanzi merge tool. For example, these parameters can be called MINE, THEIRS, BASE, MERGED.

## Integrating the Kanzi merge tool with SVN version control software

To integrate the Kanzi merge tool with SVN version control software, add Kanzi merge tool as an external program for merging files with the .kzproj extension.

For example, if you are using Tortoise SVN, in TortoiseSVN select SVN > Settings > External Programs > Merge Tool > Advanced and set:

- Filename, extension or mime-type to .kzproj
- External program to

```
<KanziInstallation>/Studio/Bin/KanziMergeTool.bat "<KanziInstallation>/Studio/Bin/KanziStudio.exe"  %mine %theirs %base %merged

```

For example, if your installation of Kanzi is in `C:\Program Files\Rightware\Kanzi`, use

```
C:\Program Files\Rightware\Kanzi\Studio\Bin\KanziMergeTool.bat "C:\Program Files\Rightware\Kanzi\Studio\Bin\KanziStudio.exe" %mine %theirs %base %merged

```
