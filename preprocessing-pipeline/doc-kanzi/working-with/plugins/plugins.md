---
title: Kanzi Studio plugins
source: https://docs.kanzi.com/4.1.0/en/working-with/plugins/plugins.html
---

# Kanzi Studio plugins

With Kanzi plugins, you can extend the functionality of Kanzi and customize Kanzi to fit your application development requirements. When you create a Kanzi plugin, you can share the extended functionality with any Kanzi user.

In Kanzi you can create and use these types of plugins:

- Kanzi Studio plugins extend the functionality of Kanzi Studio and run in Kanzi Studio.

For Kanzi Studio you can create:

  - Kanzi Studio command plugins are plugins that you execute as commands and do not have a user interface. For example, use the command plugins to execute a command on the entire or the selected part of the node tree in your project.

See Creating Kanzi Studio command plugins.
  - Kanzi Studio window plugins are plugins that you use in a Kanzi Studio window and have a user interface. For example, use the window plugins to create an editor or to visualize the content in your project.

See Creating Kanzi Studio window plugins.

- Kanzi Engine plugins extend the functionality of Kanzi Engine. Kanzi Engine executes these plugins on target platforms.

See Creating Kanzi Engine plugins.

Kanzi Studio plugins extend the functionality of Kanzi Studio and run in Kanzi Studio.

For example, you can extend the functionality of Kanzi Studio to:

- Automate tasks that take a lot of time to do manually in Kanzi Studio, or are prone to errors.
- Import and export content from Kanzi Studio, such as localization tables in a format that Kanzi Studio does not support
- Create editors that abstract the details and speed up the workflow, such as visualization tools that support work on your projects in Kanzi Studio.

## Kanzi Studio data model

Kanzi Studio project is a hierarchical structure of project nodes. Each node has a set of properties and can have a set of child nodes or items. Different types of project items, such as nodes, models, textures, and animations have their own characteristics. For example, textures specify the image used in the texture and filtering. To change the data in the project Kanzi Studio uses commands. For example, set values to properties, or create new items.

Kanzi Studio provides the `KanziStudio` object to plugins. The `KanziStudio` object is the root object for data access and provides the current project, available commands, global undo and redo, and events related to project opening and closing.

You can access the nodes, resources, and properties in the project using the current project node. Use libraries for different types of nodes and factory for new project nodes and resources. Nodes provide the access to properties, child nodes and items, changes in the current node and descendants, and events.
