---
title: Exporting Themes
source: https://docs.kanzi.com/4.1.0/en/working-with/themes/exporting-themes.html
---

# Exporting Themes


When you are done creating themes for your application, you need to export the Themes from the Kanzi Studio project of your application to kzb files and deploy them to your target device. Kanzi provides two main approaches to use Themes in your application: non-baked and baked Themes. You can combine these approaches to get the result you need.
## Non-baked Themes


In Kanzi Studio when you export a kzb file for a non-baked Theme, Kanzi Studio includes in that kzb file the resources for all Themes in that project. The nodes use the resource IDs to get the resources for the currently selected Theme. When you set your application to use a non-baked Theme, Kanzi changes the resource to which the resource ID points.

On a target device non-baked Themes require less storage than baked Themes, but use more memory at runtime. When you use non-baked Themes, you can change the application Theme without having to load additional kzb files.

See Exporting non-baked Themes and Exporting non-baked Themes with Theme resource packs.
## Baked Themes


In Kanzi Studio when you export a kzb file for a baked Theme, Kanzi Studio replaces each resource ID in all nodes in that project with the resource to which the resource IDs point. In a baked Theme, the nodes do not get resources using resource IDs, but get the resources directly.

On a target device baked Themes require more storage than non-baked Themes, but provide better performance and use less memory at runtime. When you use baked Themes, you can change the application Theme only after loading additional kzb files.

See Exporting baked Themes and Exporting baked Theme Group items with Theme resource packs.
## Selecting the suitable approach


Using Themes which are baked, non-baked, or which combine both approaches, you can theme your application to better fit the purpose of your application and the capacity of your target device.

The procedures in this topic show different configurations you can use to export a themed project. All procedures are based on a sample project named Cluster which has two Theme Group items, where each Theme Group has two Themes:

- The Variant Theme Group defines the car variant where the cluster is used:

  - Sport Theme defines the cluster for the sport variant of cars.
  - SUV Theme defines the cluster for the SUV variant of cars.

- The Color Theme Group defines the color of the car:

  - Blue Theme defines the cluster for blue cars.
  - Red Theme defines the cluster for red cars.

 [](../../_images/example-themed-project.svg)
### Exporting non-baked Themes


Use this approach when your target device has enough storage and memory to fit the entire application including the resources used in all Themes and when you want to change the application theme without having to load additional kzb files. See Non-baked Themes.

To export non-baked Themes:

1.

In the Library > Themes double-click each Theme Group and in the Theme Editor make sure that all Themes have the exporting of Theme resources disabled.

When you enable the exporting of Theme resources the  icon in the Theme column turns blue  and Kanzi Studio exports the resources used in that Theme.

For example, in the Variant and Color Theme Group items make sure that all the Themes have exporting of Theme resources disabled.

> **Tip:** If you do not see in the Theme Editor the  icons in the Theme columns, in the Library > Themes select the Theme Group and in the Properties set the Export Baked Usages property to disabled.
> 2.
>
> Select File > Export > Export KZB.
>
> Kanzi Studio creates one kzb file which includes the application node tree and resources for all Themes in all Theme Group items and exports the kzb file to the `<ProjectName>/Application/bin` directory. Deploy this file to your target device. [](../../_images/non-baked.svg)
>
### Exporting baked Themes


Use this approach to optimize your application for use with a single Theme so that you can run it on a target device with very limited storage or memory. When you use this approach and want to change the application theme, you have to shut down the application and start it with the kzb file which contains the baked Theme in which you want to run your application. See Baked Themes.

To export baked Themes:

1.

In the Library > Themes select the Theme Group items which contain Themes you want to bake and in the Properties enable the Export Baked Usages property.

For example, in the Library > Themes select the Color and Variant Theme Group items and in the Properties enable the Export Baked Usages property.
2.

Select File > Export > Export Baked Theme Binaries and in the Themes and Locales to Bake on Export window set:

  - Export Main Kzb to disabled
  - For each Theme Group select either:

    - < All > to bake all Themes in that Theme Group.
    - < Skip Baking > to not bake any Themes in that Theme Group.
    - < Theme group default value > to bake the default resources and values in that Theme Group.
    - A specific theme to bake the resources and values that you set for that theme.


For example, for the Color Theme Group select < All > to bake all Themes in that Theme Group.


Click Export.

Kanzi Studio creates one kzb file for each Theme you selected in the Themes and Locales to Bake on Export window and exports the kzb files to the `<ProjectName>/Application/bin/<ThemeGroupName>=<BakedThemeName>` directories for each Theme Group and Theme combination. Each kzb file includes the application node tree and baked resources for that Theme. Deploy to your device only the kzb file with the Themes or Theme combinations you want to use. [](../../_images/baked.svg)

### Exporting non-baked Themes with Theme resource packs


A Theme resource pack is a kzb file which contains only the resources for a selected Theme.

Use this approach when the storage or memory on your target device is limited, but you want to change the application theme at runtime without having to load additional kzb files.

For example, with this approach you can create from one Kanzi Studio project applications for two car variants (Sport and SUV), where each has two Themes (Blue and Red) between which you can switch without loading additional kzb files.

To export non-baked Themes with Theme resource packs:

1.

In the Library > Themes select the Theme Group items which include the Themes from which you want to create Theme resource packs and in the Properties disable the Export Baked Usages property.

For example, in the Library > Themes select the Variant Theme Group and in the Properties disable the Export Baked Usages property.
2.

In the Library > Themes double-click each Theme Group and in the Theme Editor click  next to the Theme name the resources of which you want to export to a Theme resource pack.

To export the default resources of the Theme Group to a Theme resource pack, click  next to the Default Value column.

When you enable the exporting of Theme resources the  icon in the Theme column turns blue  and Kanzi Studio exports the resources used in that Theme.

For example, in the Variant Theme Group enable the exporting for the Sport and SUV Themes. In this example, with this setting you create an application for two car variants (Sport and SUV), where each has two Themes (Blue and Red) between which you can switch without having to load additional kzb files.
3.

Select File > Export > Export KZB.

Kanzi Studio creates:

  - One kzb file which includes the application node tree and all the resources which more than one Theme uses (common resources), and exports the kzb file to the `<ProjectName>/Application/bin` directory.
  - One kzb file for each Theme you selected for export in the Theme Editor and stores the files in the `<ProjectName>/Application/bin/Theme_packs` directory.

Each kzb file includes only the resources that Theme uses, without the common resources (which are stored in the kzb file which includes the application node tree and common resources). Kanzi Studio uses Theme names for the names of the Theme resource packs kzb files.
 [](../../_images/non-baked-themes-with-theme-packs.svg)

### Exporting baked Theme Group items with Theme resource packs


Use this approach when you want to create an application with a specific set of baked Themes. You bake those Themes that do not change within a car variant. For example, with this approach you can create from one Kanzi Studio project applications you can deploy to two car variants (Sport and SUV): because in the car you do not want to switch the variant of the car, bake the Variant Theme Group, but do not bake the Color Theme Group so that you can change the color in the car. In this example you store the Color Themes as Theme resource packs, you can switch the color Theme only after loading the kzb file which contains the resources for that Theme.

This example is a combination of exporting baked Themes and non-baked Themes with Theme resource packs. See Exporting baked Themes and Exporting non-baked Themes with Theme resource packs.

To export baked Theme Group with Theme resource packs:

1.

In the Library > Themes select the Theme Group items the resources of which you want to bake and in the Properties enable the Export Baked Usages property.

For example, in the Library > Themes select the Variant Theme Group and in the Properties enable the Export Baked Usages property.
2.

In the Library > Themes select the Theme Group you want to export as non-baked, in the Properties disable the Export Baked Usages property, and in the Theme Editor click  next to the Theme name the resources of which you want to export as a Theme resource pack.

To export the default resources of the Theme Group to a Theme resource pack, click  next to the Default Value column.

When you enable the exporting of Theme resources the  icon in the Theme column turns blue  and Kanzi Studio exports the resources used in that Theme.

For example, in the Color Theme Group enable the exporting for the Blue and Red Themes.
3.

Select File > Export > Export Baked Theme Binaries and in the Themes and Locales to Bake on Export window set:

  - Export Main Kzb to disabled
  - For each Theme Group select either:

    - < All > to bake all Themes in that Theme Group.
    - < Skip Baking > to not bake any Themes in that Theme Group.
    - < Theme group default value > to bake the default resources and values in that Theme Group.
    - A specific theme to bake the resources and values that you set for that theme.


For example, to bake all Themes in a Theme Group, select < All >.


Click Export.

Kanzi Studio creates one directory in `<ProjectName>/Application/bin` for each Theme Group and Theme combination which contains:

  - One kzb file for each Theme Group for which you enabled Export Baked Usages property and selected for exporting in the Themes and Locales to Bake on Export window. This kzb file includes the application node tree and all the resources which more than one Theme uses (common resources), and stores it in the `<ProjectName>/Application/bin/<ThemeGroupName>=<BakedThemeName>` directory.
  - One kzb file for each Theme you selected for export in the Theme Editor. Each kzb file includes only the resources that Theme uses, without the common resources (which are stored in the main kzb file), and stores the files in the `<ProjectName>/Application/bin/<ThemeGroupName>=<BakedThemeName>/Theme_packs` directory. Kanzi Studio uses Theme names for the names of the Theme resource packs kzb files.
 [](../../_images/baked-with-theme-packs.svg)

## Deleting exported files


When you export Themes you can quickly end up with a large amount of files and directories. To permanently remove all kzb files exported from a project select File > Export > Delete Exported Binaries.
