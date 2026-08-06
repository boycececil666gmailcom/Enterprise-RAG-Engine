---
title: Using a data source
source: https://docs.kanzi.com/4.1.0/en/working-with/data-sources/using-a-data-source.html
---

# Using a data source


After you define your data source, or if you have a dll of the plugin that defines your data source, add and enable the plugin in the project where you want to use that data source. See Defining a data source.

To work with data sources in your Kanzi Studio project, select Window > Data Sources.

Use the Data Sources window to create, set, and delete the data sources in your project, and to connect data objects from a data source to nodes and resources in your project.
## Creating a data source


Before you can create a data source in Kanzi Studio, you must define a data source in a Kanzi Engine plugin. See Defining a data source.

To create a data source:

1.

In the Data Sources window click Create Data Source.
2.

In the Create Data Source window set:

  - Name to the name you want to use for this data source.
  - Data Source Type to the type of data source you want to create.


Click OK.
3.

If your data source requires you to set any additional properties, set the properties in the Data Sources window. In the Data Sources window click  and set the properties for that data source.

For example, click  to set the file from which this data source generates its data objects.
4.

In the Data Sources window click  next to the data source to create data objects from that data source.

Hover over a data object to see the data type and the current value of that data object.

When the data source plugin creates data objects from your data source, you can use that data in your project. See Using data objects.


> **Tip:** In the Kanzi Studio Node Tree window, an indicator next to a node shows when a State Manager, Binding, Data Source Binding, or an Animation overrides the values of some properties in that node.
>
> To navigate to the source of the override in the Kanzi Studio project, right-click the override indicator and select the source you wish to navigate to from the context menu.
## Using data objects


Before you can use data from a data source you have to define a data source in a Kanzi Engine plugin and create a data source. See Defining a data source and Creating a data source.

This section describes how to use Boolean, float, integer, and string data object types. To learn how to use list data object types, see Using list data objects.

To use data objects:

1.

In the Node Tree select a node where you want to use a data source (or one of its parent nodes), in the Properties add the Data Context property, and set it to the data source from which you want to use the data.

For example, add and set the Data Context property to the RootNode node.

By setting the Data Context property you tell your application from which data source it receives data. When you set the Data Context property for a node, all its child nodes inherit the value of the Data Context property. If you want to use a different data context for one of the child nodes, add the Data Context property to that node and set it to the data context you want to use.

> **Tip:** You can set the data context by dragging a data object from the Data Sources window and dropping it on a node in the Node Tree to which you want to assign that data context.
> 2.
>
> Bind the value of a data object item to a property of a node in which you want to use the data from the data source you set in the Data Context property:
>
> - For single field properties, from the Data Sources window drag the data object and drop it on the property the value of which you want to get from that data object.
>
> Kanzi creates a binding that binds the value of the property to the data object from the data source set by the Data Context property.
> - For properties with more than one field, in the Properties click + Add Binding, and in the Binding Editor set:
>
> - Property to the property to the field of which you want to bind the data object.
> - Property Field to the property field to which you want to bind the data object.
> - From the Data Sources window drag the data object and drop it on the Expression window of the Binding Editor.


Click Save.

Kanzi creates a binding that binds the value of the property field you set in the Property Field property to the data object from the data source set by the Data Context property.


## Using list data objects


Before you can use data from a data source you have to define a data source in a Kanzi Engine plugin and create a data source. See Defining a data source and Creating a data source.

This section describes how to use list data object types. To learn how to use Boolean, float, integer, and string data object types, see Using data objects.

To use list data objects:

1.

In the Node Tree select a Grid List Box or a Trajectory List Box 3D node for the items of which you want to use data from a data source, or one of its parent nodes, in the Properties add the Data Context property, and set it to the data source from which you want to use the data.

For example, add and set the Data Context property to the RootNode node.

By setting the Data Context property you tell your application from which data source it receives data. When you set the Data Context property for a node, all its child nodes inherit the value of the Data Context property. If you want to use a different data context for one of the child nodes, add the Data Context property to that node and set it to the data context you want to use.
2.

In the Node Tree create or select the list box node and in the Properties add and set the Item Template property to the prefab template you want the list box node to use to show the data from the list data objects in your data source. See Using the Grid List Box nodes and Using the Trajectory List Box 3D node.
3.

From the Data Sources window drag a list data object type to the Items Source property of the list box node.

Kanzi creates a binding that binds the value of the Items Source property to the list data object from the data source set by the Data Context property.

With the Items Source property you set the data object which provides the data for the list items in a Grid List Box node.
4.

In the Prefabs select the prefab which you set in the Item Template property of the list box node, and bind the data objects inside the list data object to the properties of the nodes which define the list item, to populate the list box items with the data from the data source. See Using data objects.

## Updating data sources


If the Kanzi Engine plugin that defines your data source does not update your data source, you can update the data source manually.

You can update data sources in these ways:

- To update a specific data source, in the Data Sources window click  next to the data source you want to update. When you update a data source Kanzi Studio creates data objects from that data source.

Hover over a data object to see the data type and the current value of that data object.
- To update all data sources in a project or solution, in File > Update select:

  - Update Data Sources in Project to update the data sources in the Kanzi Studio project
  - Update Data Sources in Solution to update the data sources in the Kanzi Studio project and referenced projects

- To update data sources using a script, see Creating and updating data sources using a script.

## Changing the properties of a data source


To change the properties of a data source:

1.

In the Data Sources window click  and set the properties for that data source.

For example, click  to set the file from which this data source generates its data objects.
2.

In the Data Sources window click  next to the data source whose properties you set, to apply the changes to the properties of that data source.

## Deleting a data source


To delete a data source, in the Data Sources window click . When you delete a data source Kanzi Studio deletes the data source from the project and sets the value of all Data Context properties which used that data source to <No Data Source>, but keeps all bindings which used that data source.
## Using data sources in the API


For details, see the `DataSource` class.
