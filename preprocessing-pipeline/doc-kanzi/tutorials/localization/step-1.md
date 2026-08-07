---
title: Step 1 - Localize text and texture content
source: https://docs.kanzi.com/4.1.0/en/tutorials/localization/step-1.html
---

# Step 1 - Localize text and texture content

In this step of the tutorial, you learn how to add resources to a localization table, how to prepare the text content in your Kanzi application for the translators, and how to add the translated text content to your Kanzi application. You also learn how to create a trigger to change locales and how to localize the textures in your application.
## Get the tutorial

To get the tutorial, in the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Localization tutorial, click .

Kanzi Studio downloads the tutorial to the `<KanziWorkspace>/Tutorials` directory. You can find:

- The tutorial starting point project in the `<KanziWorkspace>/Tutorials/Localization/Start/Tool_project` directory.
- The tutorial assets in the `<KanziWorkspace>/Tutorials/Localization/Assets` directory:

  - The `Fonts` directory contains the fonts that include the Japanese, Chinese, and Korean glyphs.
  - The `Images` directory contains the images that you use for the locales.
  - The `Text` directory contains the translated text of the project as PO files.

- The completed tutorial in the `<KanziWorkspace>/Tutorials/Localization/Completed` directory.

## Content of the starting point project

The starting point project contains the content that you need to complete this tutorial:

- The layout for a mockup application that you localize in this tutorial.
- The text content that you localize.
- The texture that you localize.
- The Toggle Button Group node to which you add toggle buttons for setting the locale of the application.
- The state manager that you use to show the currently selected locale.

## Add resources to a localization table and import the translations

To add resources to a localization table and import the translations:

1.

In the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Localization tutorial, click Open and select Start project.
2.

In the Node Tree, right-click the Screen node and select Add Resources to a Localization Table.

When you use the Add Resources to a Localization Table command on the Screen node, Kanzi Studio enables you to add all resources in your project to a localization table and localize them.

To add resources to a localization table only for a selected node and its tree, right-click the node and select Add Resources to a Localization Table. Kanzi Studio shows in the Add Resources to a Localization Table window only the resources used in that node tree.
3.

In the Add Resources to a Localization Table window:

  1.

Set Localization Table to the localization table to which you want to add the resources. If you do not have a localization table yet, select <Create New>.

A localization table contains the information about which locale uses which resources.

In this step of the tutorial, you localize only the text resources. You localize other types of resources in the next step.
  2.

Click Select All to select all listed resources.

Use the checkbox next to each resource to select that resource. To select or deselect all resources, use the buttons in the bottom left part of the window.
  3.

Click Add.

Kanzi Studio creates resources and resource IDs from all resource types that you selected and adds them to the localization table that you selected. You can find the localization tables in the Library > Localization. You can now localize resources and in the localization table assign resources to locales.
**Tip:** In the top right part of the window, you can select which types of resources you want to show in the window.
By default Kanzi shows the text resources  in the project.
4.
In the Library > Localization, right-click the localization table Localization Table (Main) and select Export Localization Table.
Kanzi Studio exports the localization table template in the POT file format to the `<ProjectName>/Tool_project/Localization/<LocalizationTableName>` directory.
When you localize your Kanzi application for the first time, send that POT file to the translators. This is the template file that contains the strings and their context for each text resource in a localization table.
Translators use the POT template file to translate the text content for each locale. The result of their translation is one PO file for each locale. For this tutorial, you can find PO files with the Finnish (fi-FI locale) and Spanish (es-ES locale) translations in the `<KanziWorkspace>/Tutorials/Localization/Assets/Text` directory. There you can also find the PO files for the Japanese, Chinese and Korean locales, which you add as locale packs in the last step of this tutorial.
5.
In the Library > Localization, right-click the localization table that you exported and select Import Localization Table Manually. Go to the `<KanziWorkspace>/Tutorials/Localization/Assets/Text` directory and import the PO files for the fi-FI and es-ES locales.
Kanzi Studio creates the locales specified in each PO file and adds the translations from the PO files to the localization table. Kanzi uses localization tables to store the localized text resources and information about which locale uses which project resources.
In the Library > Localization, double-click the localization table to open it and see the resources in the localization table.
6.
(Optional) To preview the locales in Kanzi Studio, in the Node Tree select the Screen node, and in the Properties set the Locale property to the locale that you want to see in the Preview.

## Create triggers to change locales

You can change the locale in your Kanzi application by setting the value of the Locale property in the Screen node. In this section, you create controls and use triggers to change the application locale. You also create a selection bar that highlights the selected locale.

1.

Create a prefab for the locale selection toggle button:

  1.

In the Prefabs, click , select Toggle Button 2D, and name it LocaleButton. In the Toggle Button 2D prefab, create a Text Block 2D node.

You use the trigger in the Toggle Button 2D node to set the locale and the Text Block 2D node to display the name of the locale in the application interface.
  2.

Select the LocaleButton prefab and in the Properties, add the Horizontal Alignment property and set it to Stretch.

This way you set the locale buttons to span the width of their parent Stack Layout 2D node LocaleSelector. You create the locale buttons later in this section by instantiating the LocaleButton prefab.
  3.

In the Prefabs, select the LocaleButton > Text Block 2D node and in the Properties add and set:

    - Horizontal Margin property Left property field to 30
    - Horizontal Margin property Right property field to 30
    - Vertical Margin property Top property field to 10
    - Vertical Margin property Bottom property field to 10

You set the margins of the Text Block 2D node to position the locale buttons in the application interface.
  4.

Select the LocaleButton > Text Block 2D node and in the Properties next to the Text property, click . In the Publish Property dialog, name the property Localization.LocaleName and click OK.

This enables you to display a different text for each instance of the prefab.

When you click , Kanzi Studio creates from that property a custom property, adds it to the root node of that prefab, and creates a `##Template` binding to the property in the root node of that prefab.

That way you can set in the root of the prefab instance the text that you want the Text Block 2D node to show.

A node prefab can contain a tree of nodes, each with their own properties. When you edit the nodes in a prefab or any of its instances in a project, you change those nodes in all instances of that prefab. You can customize each instance of a prefab to have its own property values by overriding the property values of the prefab. For example, when you create a prefab for an address book entry, you want to show a different name, number, and photo for each address book entry.

2.

From the Prefabs, drag to the Node Tree to the RootNode > IVI Grid > Locales > LocaleSelector node three LocaleButton prefabs, one for each locale.
3.

In the Node Tree, select each instance of the LocaleButton prefab in the LocaleSelector node, press F2, and name each node after the locale which that button sets.
4.

Set the application to change locale when the user toggles on the first instance of the LocaleButton prefab:

  1.

In the Node Tree in the LocaleSelector node, select the first instance of the LocaleButton prefab. In the Properties add the Localization.LocaleName property and set its value to the locale that this instance of the prefab represents.

The text that you enter here for the locale name is shown in your Kanzi application.

For example, for the default locale set the value to English.
  2.

In the Node Components, press Alt and right-click Triggers and select Message Trigger > Toggle Button > Toggled On.
  3.

In the Node Components > Triggers, press Alt and right-click the Toggle Button: Toggled On trigger and select Set Property. In the Set Property action set:

    - Target Item to Screen
    - Target Property to Locale
    - Value From to Fixed value
    - Fixed Value to the locale that you want to set with this button. For example, to set to default locale, in this case English, select the Invariant Language (Invariant Country) () value.

When the user clicks the button, the Set Property action sets the Locale property in the Screen node to the locale that you selected here.

5.

Repeat the previous step for the other two instances of the LocaleButton prefab:

  - For the Finnish locale:

    - Set the Localization.LocaleName property to suomi.
    - In the Toggle Button: Toggled On trigger in the Set Property action, set the Fixed Value to Finnish (Finland) (fi-FI).

  - For the Spanish locale:

    - Set the Localization.LocaleName property to espaÃ±ol.
    - In the Toggle Button: Toggled On trigger in the Set Property action, set the Fixed Value to Spanish (Spain) (es-ES).
**Tip:** When you need to create the same trigger in several nodes, you can copy that trigger.
To copy a trigger to a node:
1.
In the Node Tree, select the node that has the trigger that you want to copy. In the Node Components, right-click the trigger and select Copy.
2.
In the Node Tree, select the node to which you want to copy the trigger. In the Node Components, right-click Triggers and select Paste.
6.
Create the selection bar that shows the selected locale:
1.
In the Prefabs in the LocaleButton prefab, create an Empty Node 2D node, name it SelectionBar, and in the Properties add and set:
- Background Brush to Color Brush
- Layout Width to 5
- Layout Height to 70
2.
In the Prefabs, select the LocaleButton prefab. In the Properties, add the State Manager property and set it to LanguageSelected.
You use the state manager to control the visibility of selection bar when you toggle between the locales.
7.
In the Node Tree, select the instance of the LocaleButton prefab that sets the English locale. In the Properties, add the Toggle State property and set it to 1.
This way you set the English locale button selected by default when you start your application.

In the Preview when you click a locale name, Kanzi Studio changes the text in the application to that locale and displays the selection bar on the left side of the selected button.
## Use a different texture for each locale

The application contains a texture that you localize to use a different image for each locale.

To localize images:

1.

In the Assets, click Import Assets, go to the `<KanziWorkspace>/Tutorials/Localization/Assets/Images` directory, and import all images to the project.
2.

In the Node Tree in the RootNode > IVI Grid > LocationInformation, right-click the Image node and select Add Resources to a Localization Table.

To add resources to a localization table only for a selected node and its tree, right-click the node and select Add Resources to a Localization Table. Kanzi Studio shows in the Add Resources to a Localization Table window only the resources used in that node tree.
3.

In the Add Resources to a Localization Table window:

  1.

Set Localization Table to Localization Table.

Select the same localization table that you created earlier in this step of the tutorial.
  2.

Select  to show the texture resources in the selected node.
  3.

Select Image.
  4.

Click Add.

4.

In the Library > Localization, double-click the Localization Table (Main) localization table to open the table in the Localization Editor. In the column for each locale, select the image that you want to use for that locale.

For example, for the Spanish locale use Image02 and for the Finnish locale use Image03.

If you do not select a resource or value for a locale, Kanzi uses the default resource or value for that locale. The default value is listed in the Default Value column.

In the Preview when you click a locale name, Kanzi Studio changes the image in the application to the image that you set for that locale.

Introduction Next step
