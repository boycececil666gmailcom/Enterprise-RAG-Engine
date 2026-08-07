---
title: Step 1 - Create a contacts list and get contacts from a data source
source: https://docs.kanzi.com/4.1.0/en/tutorials/list-box/step-1.html
---

# Step 1 - Create a contacts list and get contacts from a data source


In this step of the tutorial you first create the Grid List Box node which you use as a contacts list. You then set the Grid List Box to receive the contacts data from a data source.
## Get the tutorial


To get the tutorial, in the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the List box tutorial, click .

Kanzi Studio downloads the tutorial to the `<KanziWorkspace>/Tutorials` directory. You can find:

- The tutorial starting point project in the `<KanziWorkspace>/Tutorials/List box/Start/Tool_project` directory.
- The completed tutorial in the `<KanziWorkspace>/Tutorials/List box/Completed` directory.


This tutorial depends on a plugin from the Data source tutorial.

To get the Data sources tutorial, in the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Data sources tutorial, click .

Kanzi Studio downloads the tutorial to the `<KanziWorkspace>/Tutorials` directory.
## Content of the starting point project


The starting point project contains the content that you need to complete this tutorial:

- The Container node sets the background for the contacts list.
- The ContactItem prefab defines the initial layout for each contact entry.

  - The ContactPhoto node shows the photo for a contact.
  - The ContactName node shows the name for a contact.


You can find the ContactItem node in the Prefabs window.
- XML data source data source plugin which you use to get the data for contact entries from an XML file. This plugin uses the `ContactsList.xml` file as the source of data for the contact entries in this tutorial. You can find the `ContactsList.xml` file in the `Application/bin` directory.

To view the Data Sources window, in the Kanzi Studio main menu select Window > Data Sources.

## Create a Grid List Box node


In this section you create the Grid List Box node that you use to show the list of contacts.

To create a Grid List Box node:

1.

In the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the List box tutorial, click Open and select Start project.
2.

In the Node Tree press Alt and right-click the RootNode > Container node, select Grid List Box 2D, and name it ContactsList.
3.

In the Node Tree select the ContactsList node, in the Properties add the Item Template property, and set it to ContactItem.

With the Item Template property you set which prefab template you want a Grid List Box node to use for the items in its list.

## Get the List Box items from a data source


In this section you use a data source to populate the ContactsList that you created in the previous section.

In Kanzi the List Box nodes use virtualization to enable you to manage the memory consumption in your application. By using virtualization a List Box node keeps in memory only the items that are visible and the number of items that you set in the Keep Alive Item Count property. When the user scrolls a List Box node, that node loads new items and removes the items that it no longer needs to keep in memory.

While you can manually add items to a List Box node, use that approach only for lists with a small amount of static items and while prototyping. To show a variable number of items in a List Box node, always use a data source to populate List Box nodes.

To get the List Box items from a data source:

1.

In the Node Tree select the ContactsList node, in the Properties add the Data Context property, and set it to XML data source.

By setting the Data Context property you tell your application from which data source it receives data.
2.

In the main menu select Window > Data Sources.

Use the Data Sources window to manage the data sources in your project.
3.

In the Node Tree select the ContactsList node, from the Data Sources window drag the XML data source > contacts data object to the Properties to the Items Source property.

The Items Source property sets the source that provides the data for the items that the node shows.
4.

In the Prefabs select the ContactItem > ContactPhoto node, from the Data Sources window drag the XML data source > contacts > Item > contact > photo data object to the Properties to the Image property.

This data object provides the photo for each contact item in the contacts list.

When you drag a data object to a property that has a single field, Kanzi Studio creates a binding that binds the value of that property to the data object that you dragged to that property.

The value for the Image property of the ContactPhoto node now comes from the XML data source photo data object.
5.

Repeat the previous step for the ContactItem > ContactName node but drag the XML data source > contacts > Item > contact > name data object to the Text property.

This data object provides the name for each contact item in the contacts list.


The ContactsList node now receives the photos and names for the contact items from the `ContactsList.xml` using the XML data source data source. In the Preview you can see the contact data.
## Set the layout of the Grid List Box node


In this section you set the layout for the ContactsList node and the size of the list items to present the content in the application.

To define the layout for the list box content, in the Node Tree select the ContactsList node and in the Properties add and set:

- Cell Width to 400
- Cell Height to 45

You set the area reserved for each item in the Grid List Box node. If the items do not fit in the cell, the node clips them.
- Layout Width to 400
- Layout Height to 360

You set the area in which the items in the Grid List Box node are visible. If all items in the Grid List Box node do not fit in this area, the node clips those items that do not fit. The user can scroll the Grid List Box node to access all items.
- Horizontal Alignment to Center

This way you align the ContactsList node horizontally to the center of the Container node.


The Preview now shows the updated layout for the list box and its items. To change the name of a contact in the contacts list, in a text editor change the values in the `ContactsList.xml` file, and save the `ContactsList.xml` file.
## Set the selected item to move to the center of the Grid List Box node


In this section you set the selected item to move to the center of the Grid List Box node.

To set the Grid List Box to scroll the selected item to the center of the node, in the Node Tree select the ContactsList node, in the Properties add the Selection Behavior property, and set it to Bring Center.

In the Preview when you click a list item, the List Box brings that item to the center of the node.

Introduction Next step
