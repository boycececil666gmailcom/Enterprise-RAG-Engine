---
title: Step 1 - Prepare the content
source: https://docs.kanzi.com/4.1.0/en/tutorials/drag-and-drop/step-1.html
---

# Step 1 - Prepare the content

In this step of the tutorial you first create the prefab that visualizes the item that the user drags, then you set the texture for each item.
## Get the tutorial

To get the tutorial, in the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Drag and drop tutorial, click .

Kanzi Studio downloads the tutorial to the `<KanziWorkspace>/Tutorials` directory. You can find:

- The tutorial starting point project in the `<KanziWorkspace>/Tutorials/Drag and drop/Start/Tool_project` directory.
- The completed tutorial in the `<KanziWorkspace>/Tutorials/Drag and drop/Completed` directory.

## Content of the starting point project

The starting point project contains the content that you need to complete this tutorial:

- The Navigation Bar prefab.

The prefab is a Toggle Button Group 2D node with a Grid Layout 2D node that contains Toggle Button 2D nodes. The buttons use the Navigation Item prefab.
- The Navigation Item prefab.

In the Navigation Item > Image node the Image property is bound to a data object that you create in this tutorial to set the icon of each button.
- Textures that contain the icons for the Navigation Item nodes.
- The resource dictionary of the Screen node contains aliases that point to the Grid Layout 2D, RootNode, and button nodes.

These aliases provide a convenient way to access the nodes using the Kanzi Engine API.
- The Shake Animation Clip.

You use the animation to shake a node when the user is dragging that node.

## Create visualization for the button that the user drags

In this section you create a prefab that you use to visualize the button that the user is dragging. Instead of dragging the button to a new position, you move an instance of this prefab that looks like the dragged button. When the user ends the drag-and-drop gesture, instead of setting the positions of the buttons in the Grid Layout 2D node, you set the order of the data objects that set the button icons.

To create visualization for the button that the user drags:

1.

In the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Drag and drop tutorial, click Open and select Start project.
2.

In the Prefabs click , select Empty Node 2D, name it Drag Item, inside it create an Empty Node 2D node, and in the Properties add and set:

  - Background Brush to Drag Item Background Color Brush

This way you set the background color of the prefab to be lighter than the navigation bar.
  - Opacity to 0,7

This way you make the prefab partially transparent.

You implement the drag-and-drop so that when the user drags a button, they drag an instance of the Drag Item prefab.
3.

In the Prefabs > Navigation Item right-click the Image node and select Copy, then right-click the Empty Node 2D node and select Paste.

You copy the Image node to the Drag Item prefab because you want to make the visualization of the node that the user is dragging look the same as the Navigation Item node.
4.

Select File > Export > Export KZB.

Kanzi Studio creates the kzb file and configuration files from your Kanzi Studio project. Kanzi Studio stores the exported files in the `<ProjectName>/Application/bin` directory or the location that you set in Project > Properties in the Binary Export Directory property. The kzb file contains all nodes and resources from your Kanzi Studio project, except the resources that you mark in a localization table as locale packs.

When you run your Kanzi application from Visual Studio, your application loads the kzb file and configuration files.

## Set the icons for the buttons

In this section you create the data objects that you use to set the icons for the buttons.

To set the icons for the buttons:

1.

In Kanzi Studio, select File > Open Kanzi Command Prompt.

The Kanzi Command Prompt opens the Windows Command Prompt with the Kanzi environment variables set for the version of Kanzi for which you open a Kanzi Command Prompt.

Use the Kanzi Command Prompt to access Kanzi utilities and build tools, such as Gradle and CMake, without using absolute paths or setting environment variables.
**Tip:** You can find the Kanzi Command Prompt in the Windows Start Menu in the Rightware directory.
When you have more than one version of Kanzi installed, make sure that you launch a Kanzi Command Prompt for the version of Kanzi with which you want to work in that command prompt.
2.
In the Kanzi Command Prompt in the `<KanziWorkspace>/Tutorials/Drag and drop/Start/Application` directory run the script that generates a Visual Studio solution for the tutorial application.
```
generate_cmake_vs2022_solution.bat
```

This script generates a Visual Studio solution for the application in the directory `<KanziWorkspace>/Tutorials/Drag and drop/Start/Application/build_vs2022`.
3.

In Visual Studio open the `<KanziWorkspace>/Tutorials/Drag and drop/Start/Application/build_vs<Version>/Drag_and_drop_start.sln` Visual Studio solution.
4.

In Visual Studio in the Solution Explorer right-click the Drag_and_drop_start project and select Set as StartUp Project.
5.

In the `drag_and_drop.cpp` file in the `Application::onProjectLoaded` function create the data objects and set the data context:

```
    void onProjectLoaded() override
    {
        Domain* domain = getDomain();

        // Create a data object named Root.
        m_rootData = DataObject::create(domain, "Root");

        // Create data objects and add them to the Root data object.
        // Add to each of the data objects a string data object which contains the kzb URL of a texture.
        // In the Kanzi Studio project you can find the textures in the Library > Materials and Textures > Textures.
        DataObjectSharedPtr item0 = DataObject::create(domain, "item0");
        m_rootData->addChild(item0);
        item0->addChild(DataObjectString::create(domain, "image", "kzb://drag_and_drop/Textures/Navigation"));

        DataObjectSharedPtr item1 = DataObject::create(domain, "item1");
        m_rootData->addChild(item1);
        item1->addChild(DataObjectString::create(domain, "image", "kzb://drag_and_drop/Textures/Phone"));

        DataObjectSharedPtr item2 = DataObject::create(domain, "item2");
        m_rootData->addChild(item2);
        item2->addChild(DataObjectString::create(domain, "image", "kzb://drag_and_drop/Textures/Applications Home"));

        DataObjectSharedPtr item3 = DataObject::create(domain, "item3");
        m_rootData->addChild(item3);
        item3->addChild(DataObjectString::create(domain, "image", "kzb://drag_and_drop/Textures/Sound Loud"));

        DataObjectSharedPtr item4 = DataObject::create(domain, "item4");
        m_rootData->addChild(item4);
        item4->addChild(DataObjectString::create(domain, "image", "kzb://drag_and_drop/Textures/Car Wheel"));

        // Get the Screen node.
        ScreenSharedPtr screen = getScreen();

        // Set the Data Context property of the Screen node to the Root data object.
        // By setting the Data Context property you tell your application from which data source it receives data.
        screen->setProperty(DataContext::DataContextProperty, m_rootData);
    }

private:

    // Define a member variable for the Root data object.
    DataObjectSharedPtr m_rootData;

```

6.

In the private section of the `DragAndDrop` class create a function that assigns the icons to the buttons:

```
private:

    // To assign correct icons to the buttons, set the Data Context property for each button.
    void updateItems()
    {
        // Create an iterator that iterates through the data objects in the Root data object.
        DataObject::ChildConstIterator dataIt = m_rootData->beginChildren(), endDataIt = m_rootData->endChildren();

        // Create an iterator that iterates through the buttons which are
        // child nodes of the Navigation Bar > Grid Layout 2D node.
        Node2D::ChildConstIterator nodeIt = m_grid->beginChildren();

        // Set the Data Context property of each button node to the correct data object.
        for (; dataIt != endDataIt; dataIt++, nodeIt++)
        {
            Node2DSharedPtr itemNode = *nodeIt;
            DataObjectSharedPtr itemData = *dataIt;
            itemNode->setProperty(DataContext::DataContextProperty, itemData);
        }
    }

    // Define a member variable for the Grid Layout 2D node.
    GridLayout2DSharedPtr m_grid;

    ...

```

7.

In the end of the `Application::onProjectLoaded` function call the `updateItems()` function:

```
void onProjectLoaded() override
{
    ...

    // Get the parent Grid Layout 2D node of the node that the user is dragging.
    m_grid = screen->lookupNode<GridLayout2D>("#Grid Layout 2D");

    updateItems();
}

```

8.

Select the solution configuration that you want to use and run your application.

During development, select the Debug configuration. When you are ready to create a version for production, select the Release configuration.

Kanzi assigns the icons to the buttons using the data objects that you created.

Introduction Next step
