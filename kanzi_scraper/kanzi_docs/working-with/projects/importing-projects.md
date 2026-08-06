---
title: Importing projects
source: https://docs.kanzi.com/4.1.0/en/working-with/projects/importing-projects.html
---

# Importing projects


When you import a Kanzi Studio project, Kanzi Studio copies all content from the project you are importing (source project) to the current project (target project). Kanzi Studio replaces all items in the same location with the same name in both projects with the items from the source project.

Kanzi provides these options for bringing content from other projects:

- You can bring only a part of another project to the current project. See Merging projects and Merging content from referenced Kanzi Studio projects.
- You can share individual project items. See Sharing project items.
- You can merge 3D assets from a 3D asset file. See Merging 3D assets.
- If you want to import collections of ready-made content, use Kanzi Studio asset packages.

See Asset packages.
- If you want to import the assets that you created with third-party tools, use Kanzi Studio importing tools. See Importing.

## Importing a project


Save your current project before importing, because you cannot undo this operation.

To import a project:

1.

Open a project to which you want to import another project (target project).
2.

Select File > Import > Import Project, select the project file of the project you want to import (source project), and click Open.

Kanzi Studio imports the source project to the target project.

## Importing a project with data sources that use locally stored data


Typically the data in a data source you import to a Kanzi Studio project is provided by a server to which your application connects. If, however, the source files of the data source you want to import are stored locally in the source project, you must manually copy them from `<SourceProjectName>/Application/bin` to `<TargetProjectName>/Application/bin`. If you do not copy the data files to the target project, the Preview fails to start.
