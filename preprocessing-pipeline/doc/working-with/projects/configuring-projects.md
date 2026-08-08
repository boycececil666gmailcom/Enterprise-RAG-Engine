---
title: Configuring Kanzi Studio projects
source: https://docs.kanzi.com/4.1.0/en/working-with/projects/configuring-projects.html
---

# Configuring Kanzi Studio projects

To configure a Kanzi Studio project:

1.

Open the project and in the main menu select Project > Properties.
2.

In the Properties set the properties in these property categories to configure your project:

  - Description to document the project. See Documenting a project.
  - Application Settings to set the directories to which Kanzi Studio exports the kzb file and kzb Player version of the project. See Using kzb files.
  - Binary Export to configure the contents of the kzb file. For example, use these properties to:

    - Optimize the export of meshes and images. See Images and textures best practices and Optimizing meshes.
    - Set how Kanzi loads kzb files. See Setting how Kanzi loads a kzb file.
    - Set the color workflow. See Color workflow.

  - Building to set the application configuration that Kanzi Studio uses to build the project. See Configuring Android builds.
  - Default Assets to set which assets you want to use when you create nodes and resources. See Setting the default assets.
  - Preview to configure the Preview to work with Kanzi Engine plugins. See Creating Kanzi Engine plugins.
  - Profile to set:

    - The name of the kzb file and project descriptions file. See Using kzb files and Documenting a project.
    - The graphics API. See Using OpenGL ES 3.0+ in Kanzi.
    - The font engine for the Kanzi Studio Preview. See Setting the font engine for the Preview and FontEngine.
    - A project to be an asset package. See Creating an asset package.

  - Resources to set how Kanzi and Kanzi Studio handle resources. See Setting how Kanzi Engine handles unused resources.
  - Timeline to set the start and end times of the global timeline of the project.

To view the timeline, select Window > Toolbar > Timeline.

## Setting the default assets

You can set which assets you want to use when you create new nodes and resources.

To set the default assets:

1.

Open the project and in the main menu select Project > Properties.
2.

In the Properties in the Default Assets category set which assets you want to use by default:

  - Default Material sets the material that Kanzi Studio sets to models you create and import that do not have a material.
  - Default Texture sets the single texture that Kanzi Studio sets to all new Image nodes and materials that use textures.
  - Default Cubemap Texture sets the cubemap texture that Kanzi Studio sets to all new materials that use cubemap textures.
  - Import Material Type sets the material type to which Kanzi Studio assigns the materials that you import with 3D asset files.

## Setting how Kanzi loads a kzb file

The presence of the Screen node in a kzb file determines how Kanzi loads a kzb file.

To set whether Kanzi Studio exports the Screen node to the kzb file of that project, in the Node Tree select the Screen node and in the Properties set the Disable KZB Export property to:

- Disabled to export the kzb file with the Screen node. This is the default setting. You can start your Kanzi application with a kzb file that has a Screen node. If you load during application runtime a kzb file that contains a Screen node, you replace the Screen node that the application uses.
- Enabled to export the kzb file without the Screen node. You can load a kzb file without a Screen node only during application runtime, when your Kanzi application already has a Screen node.

## Project property types

For a list of the available property types for a Kanzi Studio project, see Project.
