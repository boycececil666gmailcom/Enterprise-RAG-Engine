---
title: Accessing resources using bindings
source: https://docs.kanzi.com/4.1.0/en/working-with/resources/acquiring-resources.html
---

# Accessing resources using bindings

You can use the `Acquire` binding function to load resources using their resource IDs, which you define in a string property.

The resource ID must be in a resource dictionary of the node where you use the `acquire` function, or one of its ancestor nodes:

- If the resource is not yet loaded into application memory, the `acquire` function loads the resource.
- If the resource ID is not defined, the `acquire` function returns an empty value.

For example, you can create a binding that gets the resource ID of a text resource from a data source, loads the text resource, and sets a Text Block node to show the content of that text resource. If you localize that text resource, the Text Block automatically shows the value of the resource for the current locale of the application. If you change the data in your data source, the binding function gets the resource, to which the resource ID points, and updates the text.

To load text resources based on their resource ID:

1.

In Kanzi Studio create the resources that you want to show in your application.

For example, in a localization table create text resources for labels in a list menu. See Localizing applications.
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
**Tip:** You can start creating a binding for a property by right-clicking a property and selecting Create Binding.
This way you automatically add the property to the Binding Editor.
2.
Create the nodes that show the content to which resource IDs from a data source point.
For example, populate a List Box node with data from a data source, and as the item template use the prefab that contains the node to which you added the binding that loads a resource. See Using list data objects.

When you switch the locale of your application or change the data in your data source, the `acquire` binding function gets the resources, to which the resource IDs point, and updates the content in the List Box node.
