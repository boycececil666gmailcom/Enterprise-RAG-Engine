---
title: Localizing applications
source: https://docs.kanzi.com/4.1.0/en/working-with/localization/localizing-applications.html
---

# Localizing applications


Localization involves creation and use of different resources, such as text, textures, and styles, for locales that you want to support in your application.

Kanzi uses localized resources indirectly using resource IDs that hold a separate value for each locale. To keep track of localized resources and locales Kanzi uses localization tables. You can see all localized resources and locales used by your application in the localization tables in the Library > Localization.

To localize your Kanzi application:

1.

Add the resources from your project which you want to localize to a localization table. See Adding resources to a localization table.
2.

Localize resources. See Localizing text resources and Localizing other resources.
3.

Edit localized resources. See Editing localized resources.


You can also localize themes. See Localizing themes.

Learn how to localize your Kanzi applications by completing a tutorial. See Tutorial: Localize your application.
## Adding resources to a localization table


If you have a complete Kanzi application you want to localize, or if you added content to a Kanzi application that you already localized, you have to create the resource IDs for the items you want to localize and add them to a localization table. After you create the resource IDs for the resources you want to localize and add them to a localization table you can start localizing your Kanzi application. See Localizing text resources and Localizing other resources.

To create resource IDs and add them to a localization table:

1.

In the Node Tree, right-click the Screen node and select Add Resources to a Localization Table.

When you use the Add Resources to a Localization Table command on the Screen node, Kanzi Studio enables you to add all resources in your project to a localization table and localize them.

To add resources to a localization table only for a selected node and its tree, right-click the node and select Add Resources to a Localization Table. Kanzi Studio shows in the Add Resources to a Localization Table window only the resources used in that node tree.
2.

In the Add Resources to a Localization Table window:

  1.

Set Localization Table to the localization table to which you want to add the resources. If you do not have a localization table yet, select <Create New>.

A localization table contains the information about which locale uses which resources.
  2.

Select the resource type you want to show in the Add Resources to a Localization Table window. For example, to show only text and image resources select  and .
  3.

In the table that lists all resources of the type you selected, click the checkbox next to the resource you want to add to the localization table you selected. To change the resource ID, double-click the resource ID and enter a new name.

Kanzi Studio creates a single resource ID for Text Block nodes which use the same value for the Text property. These nodes share the same entry in a localization table.
  4.

Click Add.

3.

You can start localizing your Kanzi application. See Localizing text resources, Localizing other resources, and Editing localized resources.

## Localizing text resources


Kanzi uses the gettext PO file format to handle localized text resources and sets the text direction based on the first character in a string.

In PO files, you can use Unicode characters. With Unicode characters, you can also control text direction, such as the direction of left-to-right text in right-to-left locales. To learn how to control text direction with Unicode characters, see [How to use Unicode controls for bidi text](https://www.w3.org/International/questions/qa-bidi-unicode-controls).

When you use Unicode characters, make sure you insert them correctly. On Windows and Linux, you can use the Character Map application.

To learn more about the gettext PO file format, see [The Format of PO Files](http://www.gnu.org/software/gettext/manual/gettext.html#PO-Files).

If you want to define your own import and export format for the localized text resources, use the Kanzi Studio localization plugin API to create a Kanzi Studio plugin. You can find an example of such plugin, which uses CSV to export and import text into localization tables, in the `<KanziWorkspace>/Examples/CsvPlugin` directory.

> **Note:** When localized text contains a combination of simple and complex scripts, or left-to-right and right-to-left locales, in some cases the Kanzi Studio Localization Editor renders the text differently from the Kanzi Studio Preview. To fine-tune the text, use the Unicode control characters in the Localization Editor or in the PO files.
>
> See CSV plugin example.
>
> To localize text resources:
>
> 1.
>
> Create text content in your Kanzi Studio project using Text Block nodes and add text resources to a localization table. See Adding resources to a localization table.
> 2.
>
> In the Library > Localization, right-click the localization table that contains the resources that you want to localize, and select Export Localization Table.
>
> Kanzi Studio exports to `<ProjectName>/Localization/<LocalizationTableName>` the localization table template to a POT file, and as many PO files as you have locales in that localization table.
>
> - (Optional) If you want to export all localization tables in your project, right-click Library > Localization and select Export All Localization Tables.
>
> Kanzi Studio exports to `<ProjectName>/Localization/<LocalizationTableName>` one localization table POT template file for each localization table, and as many PO files as you have locales in all localization tables.
>
> 3.
>
> This step depends on whether you are translating your Kanzi application for the first time or whether you are doing an incremental translation:
>
> - If you are translating your Kanzi application for the first time, send the POT file to your translators. The translators create one PO file for each locale.
> - If you are doing an incremental translation, send the POT file and the PO file for each locale to the translators.
>
> Each PO file contains only the resources that have already been translated for that locale. To add to a PO file the resources that have not yet been translated for that locale, the translator needs to update the PO file from the POT template file using a gettext translations editor.
>
> 4.
>
> After you receive the PO files from the translators, save them to `<ProjectName>/Localization/<LocalizationTableName>`.
> 5.
>
> In Kanzi Studio, in the Library > Localization, right-click the localization table whose content your translators localized, and select Import Localization Table.
>
> Kanzi Studio imports all PO files in the `<ProjectName>/Localization/<LocalizationTableName>` directory to the selected localization table.
>
> - (Optional) If you want to manually select the location from which you want to import the PO files for your project, select Import Localization Table Manually.
> - (Optional) If you want to import PO files for all localization tables in your project, in the Library right-click Localization and select Import All Localization Tables. Kanzi Studio imports all PO files in all directories found in `<ProjectName>/Localization`.


### Setting text order in a localized string


The order of presenting information differs between languages. Kanzi allows you to set the order of information in a localization string.

To set the text order in a localized string:

1.

Set up a project for localization:

  1.

Create a node that shows the localized text.

For example, create a Text Block 2D node and name it PhotoDeletionMessage.

See Using the Text Block nodes.
  2.

Create a data source or properties that you use in the localized content.

For example, create these properties:

    - AlbumName whose data type is Text
    - PhotoCount whose data type is Integer


See Creating property types.
  3.

In the Node Tree, select the Text Block node that you created earlier. In the Properties, add the properties that you created and set:

    - AlbumName to New York
    - PhotoCount to 10

  4.

Create a localization table with text resources and locales.

For example, create a localization table and in it:

    1.

Add a text resource and name it PhotoDeletionMessage.
    2.

Create the locales en-US and fi-FI.


See Creating localization tables, Adding resources to a localization table, and Using locales.

2.

In the Localization Editor, create the strings for each locale. Use curly braces `{}` as placeholders for the content that you want to insert from a data source or property.

For example, in the localization table create these localization strings:

  - For en-US

```
{} photos were deleted from the album {}

```

  - For fi-FI

```
Albumista {1} poistettiin {0} valokuvaa

```


In the fi-FI locale, you use the indexes inside the curly braces to change the order in which values from properties appear in the localized text. You set the default order in a binding that you create in the next step.

Use the curly braces for localization strings in PO files. See Localizing text resources.
3.

In the Node Tree, select the node that displays the localized text. In the Properties, click + Add Binding and in the Binding Editor set:

  - Property to Text
  - Expression to

```
# Use the acquire function to load the PhotoDeletionMessage text resource from
# the localization table using its resource ID, and cast it as a string type.
message = string(acquire("PhotoDeletionMessage"))

# Replace the placeholders in the localization strings with the values from
# the PhotoCount and AlbumName properties.
format(message, {@./PhotoCount}, {@./AlbumName})

```


Click Save.

In the en-US locale, the properties appear in the order in which you pass them to the `format` function. In the fi-FI locale, you use the indexes inside the curly braces to change the order of the parameters. See format.


In the Node Tree, select the Screen node and in the Properties set the Locale property. When you change the locale, the AlbumName and PhotoCount properties appear in a different order depending on the locale.
## Localizing other resources


Besides translating the text content into multiple languages, Kanzi enables you to use different resources for each locale, including animations, brushes, composers, fonts, materials, meshes, textures, and styles.

You can use this procedure to localize resources of all types.

To localize other resources:

1.

Create or import content to your Kanzi Studio project and add the resources used by this content to a localization table. See Adding resources to a localization table.

For example, if you have five locales and want to use a different set of textures for each locale, import to your Kanzi Studio project the images for the textures for each locale. See Importing.
2.

In the Library > Localization double-click the localization table that contains the resources you want to localize.

Kanzi Studio opens the localization table in the Localization Editor.
3.

In the Localization Editor find the resource you want to localize, double-click the resource cell in the locale into which you want to localize, and enter the text or select the resource ID for the resource you want to use for that locale.

  - If you do not select a resource or value for a locale, Kanzi uses the default resource or value for that locale. The default value is listed in the Default Value column.
  - To use a resource from the file system, in the cell for which you want to set the resource select < URL >, and enter [file://](file://) followed by the absolute or relative path to the resource in the file system.

4.

Repeat the previous step until you select resources for all resources and locales.

## Localizing themes


Kanzi enables you to localize themed applications.

To localize themes:

1.

For each theme the content of which you want to localize, create a prefab from the content that includes the text nodes you want to localize. See Creating and using a node prefab.
2.

Localize the text resources:

  1.

In the Prefabs select the prefabs you created in the previous step and add their resources to a localization table.

See Adding resources to a localization table.
  2.

In the Library > Localization double-click the localization table you created in the previous step to open it in the Localization Editor, add the locales to which you want to localize themes, and localize the text resources. See Localizing text resources.

To add a locale click + Create Locale, enter the name for the locale, and click OK.

3.

Use Prefab View nodes to show the localized content:

  1.

In the Prefabs under the node where you want to show the localized content create a Prefab View node and in the Properties add and set the Prefab Template property to one of the prefabs you created in step 1.

You must use a Prefab View node so that you can dynamically change the prefab that the Prefab View instantiates. See Prefab Placeholder and Prefab View nodes.
  2.

In the Prefabs right-click the Prefab View node you created in the previous step and select Add Resources to a Theme Group.
  3.

In the Add Resources to a Theme Group window:

    - Set the Theme Group to the theme group to which you want to add the resources.

A theme group contains the information about which theme uses which resources.
    - Rename the Resource ID to something that is meaningful in the context of your project.


Click Add.

Kanzi Studio adds to the theme group the resource ID which points to the prefab shown in the Value column. In the Prefab View node from which you add the resources to a Theme Group, Kanzi Studio sets the value of the Prefab Template property to the resource ID.
  4.

(Optional) In the Prefabs copy the Prefab View node you created in step 1 to the places where you want to show the same content.
  5.

In the Library > Themes double-click the theme group to which you added the resources, and in the Theme Editor for the resource ID you created in step 3 select the correct prefab for each theme.

4.

In the Dictionaries window to view the resource dictionaries of localization tables and theme groups in the project, click Locales and Themes, and select different locales and themes to see the localized themes in the Preview.

## Loading localized resources using resource IDs


You can load localized resources using their resource IDs, which you define using a string property. For example, you can set a node to show the content of a localized resource whose resource ID you get from a data source. Kanzi automatically shows the value of the resource for the current locale of the application.

To load localized resources using resource IDs:

1.

In Kanzi Studio in a localization table create the resources that you want to show in your application.

For example, create text resources for labels in a list menu.
2.

Create a data source where string data objects set the resource IDs of the resources that you want to show in your application. See Defining a data source and Using a data source.

For example:

  1.

In the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Data sources tutorial, click .
  2.

In the Library, right-click Kanzi Engine Plugins, select Import Kanzi Engine Plugin and import the `<KanziWorkspace>/Tutorials/Data sources/Completed/Application/lib/Win64/GL_vs2019_Release_DLL/XML_data_source.dll` Kanzi Engine plugin.
  3.

In the Data Sources, create a data source.

You use that data source to provide data for the items in a List Box node. See Tutorial: Get application data from a data source.


```
<menu type="list">
    <items>
        <item>
            <name type="string">Sounds</name>
        </item>
        <item>
            <name type="string">DateTime</name>
        </item>
        <item>
            <name type="string">Car</name>
        </item>
        <item>
            <name type="string">Display</name>
        </item>
        <item>
            <name type="string">Language</name>
        </item>
    </items>
</menu>

```

3.

Load the resources:

  1.

Use the `acquire` binding function to load a resource based on its resource ID.

For example, select the Text Block node where you want to show the content to which a resource ID points, in the Properties click + Add Binding, and in the Binding Editor set:

    - Property to Text
    - Expression to

```
acquire({DataContext.item.name})

```


You bind the Text property to the content of the text resource whose resource ID you define in the data source in the menu list item in the name string data object.

> **Tip:** You can start creating a binding for a property by right-clicking a property and selecting Create Binding.
>
> This way you automatically add the property to the Binding Editor.
> 2.
>
> Create the nodes that show the content to which resource IDs from a data source point.
>
> For example, populate a List Box node with data from a data source, and as the item template use the prefab that contains the node to which you added the binding that loads a resource. See Using list data objects.


When you switch the locale of your application, the `acquire` binding function gets the resources, to which the resource IDs point, and updates the texts.
## Editing localized resources


In the Localization Editor you can set and edit the resources that locales use.

To edit the localized resources:

1.

In the Library > Localization double-click the localization table that contains the resources you want to edit.

Kanzi Studio opens the localization table in the Localization Editor.
2.

In the Localization Editor:

  - To edit values used by locales, double-click the cell for the resource and set the value used by each locale.

    - If you do not select a resource or value for a locale, Kanzi uses the default resource or value for that locale. The default value is listed in the Default Value column.

Black cells mark entries which use the default value.
    - To use an empty string for a text resource, enter a value, delete the value, and then press Enter.

Gray cells mark entries which use an empty string.

  - To add a locale click + Create Locale, enter the name for the locale, and click OK.
  - To add a resource to a localization table manually, click + Add Resource and select:

    - Create and select the type of resource you want to create.
    - Add Existing and select a resource that already exists in your project.

  - To delete resource IDs from a localization table that are not used in the project, click , select the resource IDs you want to delete and click OK.
  - To delete a resource ID from a localization table, right-click the resource ID and select Delete Resource ID.
  - To see only the resource IDs used by the nodes that are selected in the Node Tree, click .
  - To convert a text resource to any other resource type, and the other way around, right-click the row header of the resource you want to convert and select either Convert to Resource, or Convert to Text.

Note that you can convert the resource type only for resources that are not already in use.


## Using a kzb file URL for a resource in a locale


After you add resources used in your project to a localization table, you can use a kzb URL to point to the resources in another Kanzi Studio project.

To use a kzb file URL for a resource in a locale:

1.

In the Library > Localization double-click the localization table that contains the resources for which you want to use a kzb file URL.

Kanzi Studio opens the localization table in the Localization Editor.
2.

In the Localization Editor double-click the cell for the resource and in the dropdown menu select < URL >.
3.

In the cell enter the kzb file URL of the resource you want to use.

For example, to use a font from another Kanzi Studio project, enter the kzb file URL pointing to that font.

## Creating locale packs


A locale pack is a kzb file that contains only the resources for a specific locale. Using Kanzi Engine API you can load the application resources used by a certain locale when you set that locale. That way you reduce the size of kzb files in your application.

When you want to export a resource that is used by a locale pack to the main project kzb file, in the Library select the resource and in the Properties add and enable the Is Used By Code property. All resources that have Is Used By Code property enabled are exported only to the main project kzb file and not to any locale packs that use them.

To create a locale pack:

1.

In the Library > Localization add to the localization tables the resources used by the locale you want to add to your Kanzi application in a locale pack.
2.

In the Library > Localization double-click any localization table and in the Localization Editor click  next to the locale name the resources of which you want to export to a locale pack.
3.

In Kanzi Studio, select File > Export > Export KZB. This command:

  - Creates one kzb file for each locale that you marked in the localization table as a locale pack. When Kanzi Studio exports locale packs, it names the kzb files after the locale whose resources they contain. Each locale pack file contains only the resources used by that locale.
  - Creates the main kzb file that contains the entire Kanzi Studio project, except the resources of locales that you mark as locale packs in the localization table.
  - Stores the locale pack kzb files in the `<ProjectName>/Application/bin/Locale_packs` directory, or the `Locale_packs` directory in the location that you specify in the Project > Properties in the Binary Export Directory property.

4.

Use the Kanzi Engine API to load the locale pack in your Kanzi application. See

Tutorial: Localize your application.

## Showing resource use


In the Localization Editor you can see in the currently selected context in the Node Tree whether resources are used and where they are used.

To show resource use:

1.

In the Library > Localization double-click the localization table where you want to inspect the use of resources.

Kanzi Studio opens the localization table in the Localization Editor.
2.

Use the Localization Editor:

  - To show in the localization table only the resources in the currently selected context in the Node Tree, click .
  - To list the nodes that use a resource, right-click the resource ID and select Show Usage.


## Creating localization tables


Kanzi uses localized resources indirectly using resource IDs that hold a separate value for each locale. To keep track of localized resources and locales Kanzi uses localization tables. You can see all localized resources and locales used by your application in the localization tables in the Library > Localization.

You can create several localization tables to:

- Keep the resource types separated. This makes the application development of a large project easier.
- Separate resources based on the parts of your application. When several application developers work on the same application, each can have a localization table for their own area of the application.
- Enable you to send the content from different parts of the application to translators.


To create a localization table, in the Library press Alt and right-click Localization, select Localization Table, and name the localization table.
## Using localization in multiple Kanzi Studio projects combined into a Kanzi application


To use localization when you combine multiple Kanzi Studio projects into a Kanzi application, you must make the localization tables accessible to the Screen node of the main project of your application in one of these ways:

- Define the localization tables in the main project of your application.
- Merge the localization tables from referenced projects to the main project which contains the Screen node. You can then use resource IDs to access the resources in the localization tables from the referenced projects. See Merging projects.
- Contact the Rightware support team and request the Kanzi Engine plugin which enables you to use localization across multiple Kanzi Studio projects and kzb files. See Submitting a support request.
