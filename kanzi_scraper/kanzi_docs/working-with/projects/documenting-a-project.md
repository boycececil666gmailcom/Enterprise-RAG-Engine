---
title: Documenting a project
source: https://docs.kanzi.com/4.1.0/en/working-with/projects/documenting-a-project.html
---

# Documenting a project


Add documentation for nodes and resources in your Kanzi Studio project to describe the purpose of items in your project.
## Documenting your project


To document your project:

1.

In the main menu select Project > Properties and in the Properties in the Description property write a description for your project.

You can see this description in the Kanzi Studio Quick Start window when you hover over the project name.
2.

In the Node Tree or Library select the item for which you want to add a description, in the Properties add the Description property, and write a description for that item.

Use the Description property editor to format the content. You can include hyperlinks in the description.
3.

Select File > Export > Export Descriptions.

Kanzi Studio exports a plain text file that includes the name, path, and description of items that have the Description property. Kanzi Studio exports this file in the same directory where the project file of the project is stored. When you export a kzb file, Kanzi Studio excludes the Description property.

> **Tip:** Kanzi Studio by default names the descriptions file `<project_name>_descriptions.txt`. You can set the name of the file in the Project > Properties using the Descriptions File Name property.
>
> When Kanzi Studio exports the descriptions, it adds the link to the text file in the Status Bar, which you can find below the Library window and in the Log window. Click the link to open the directory that contains the exported file.
>
