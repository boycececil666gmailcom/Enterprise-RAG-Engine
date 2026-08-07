---
title: Step 3 - Create prefab instances and load images from the file system
source: https://docs.kanzi.com/4.1.0/en/tutorials/programmer-tutorial/step-3.html
---

# Step 3 - Create prefab instances and load images from the file system

In this step of the tutorial you create a reference to the Widget Item Prefab prefab node. You use this prefab to create the prefab instances that represent the widgets in the Widget Grid List Box node, set the name, icon, and description for each widget, and populate the Widget Grid List Box with the Widget Item Prefab prefab instances.

To create prefab instances and load images from the file system:

1.

Acquire the Widget Item Prefab prefab. You use the prefab instance to present the widgets in the Widget Grid List Box node, and use the animation clips to bring the focus to the selected widget when the user selects it.

To access the resources and nodes in the kzb file you can use either resource IDs or kzb file URLs. Accessing resources using their resource IDs is the preferred way. When you access the resources you need to specify the type of the resource you are acquiring.

  - When you access a resource using the resource ID, you need to use a node with the resource dictionary that contains the resource ID of the resource you want to get.
  - When you access a resource using the kzb file URL, you need to use Kanzi resource manager.

When you use the full path of a resource, start the path with `kzb://` followed by the project name and the location of the resource.

For example, to access the Widget Item Prefab created in the Prefabs, use path

```
kzb://programmer_tutorial/Prefabs/Widget Item Prefab

```

You can find the full paths of all nodes in a kzb file in the kzb.txt file Kanzi Studio generates every time you export a kzb file from a Kanzi Studio project. For this tutorial you can find the file in the `<KanziWorkspace>/Tutorials/Programmer tutorial/Start/Application/bin` directory.

```
void onProjectLoaded() override
{
...
    // Get the reference to the reusable prefab template for the widget icons.
    ResourceManager* resourceManager = getDomain()->getResourceManager();
    PrefabTemplateSharedPtr widgetItemPrefabTemplate = resourceManager->acquireResource<PrefabTemplate>("kzb://programmer_tutorial/Prefabs/Widget Item Prefab");
...
}

```

In Kanzi resources are shared so that you can reuse them. Multiple calls to the `ResourceManager::acquireResource` that map to the same resource URL return the same resource. The resources in Kanzi are reference counted with shared pointers. You store the shared pointers as member variables because you continually use these resources. When the application is destroyed the shared pointers are also destroyed and Kanzi automatically releases the resources.
2.

In the `ProgrammerTutorialApplication` class create the constructor for the `WidgetDescription` struct that defines the widget name, icon, and description, set the number of widgets, and define the array of widget descriptions.

```
class ProgrammerTutorialApplication : public ExampleApplication
{
private:
    // Struct which contains the widget description.
    struct WidgetDescription
    {
        // Constructor.
        explicit WidgetDescription(const string& widgetName, const string& iconName, const string& description) :
                widgetName(widgetName),
                iconName(iconName),
                description(description)
        {
        }

        // The name of the widget.
        string widgetName;
        // The name of the widget icon file.
        string iconName;
        // The description of the widget shown in the description panel.
        string description;
    };

    // The size of the array and the number of items you add to the array
    // define how many widgets your application contains.
    typedef array<WidgetDescription, 14> WidgetDescriptionArray;

    // Create the array of widget descriptions.
    static const WidgetDescriptionArray widgetDescriptions;
...
};

```

3.

After the `ProgrammerTutorialApplication` class initialize the `widgetDescriptions` array where each array entry contains the name, image file name, and description of the widget.

```
// Initialization of the widget description array.
const ProgrammerTutorialApplication::WidgetDescriptionArray ProgrammerTutorialApplication::widgetDescriptions =
{
    WidgetDescription("Browser",      "Icon001.png", "Browser description"),
    WidgetDescription("Mail",         "Icon002.png", "Mail description"),
    WidgetDescription("Game",         "Icon003.png", "Game description"),
    WidgetDescription("Time",         "Icon004.png", "Time description"),
    WidgetDescription("Calculator",   "Icon005.png", "Calculator description"),
    WidgetDescription("Camera",       "Icon006.png", "Camera description"),
    WidgetDescription("Movie",        "Icon007.png", "Movie description"),
    WidgetDescription("Calendar",     "Icon008.png", "Calendar description"),
    WidgetDescription("Chat",         "Icon009.png", "Chat description"),
    WidgetDescription("Music",        "Icon010.png", "Music player description"),
    WidgetDescription("Ninja",        "Icon011.png", "Ninja description"),
    WidgetDescription("Splatter",     "Icon012.png", "Splatter description"),
    WidgetDescription("Superstar",    "Icon013.png", "Superstar description"),
    WidgetDescription("Chess",        "Icon014.png", "Chess description")
};

```

4.

In the `ProgrammerTutorialApplication` class in the `Application::onProjectLoaded` function, after storing the acquired resources and nodes and acquiring the Widget Item Prefab, add the `for` loop to populate the Widget Grid List Box node with the instances of the Widget Item Prefab prefab instances. Note that the horizontal scrolling is a built-in functionality of the Grid List Box node.

```
void onProjectLoaded() override
{
...
    // Populate the widget list.
    for (WidgetDescriptionArray::const_iterator it = cbegin(widgetDescriptions), end = cend(widgetDescriptions); it != end; ++it)
        {
            // Instantiate the Widget Item Prefab prefab.
            Node3DSharedPtr widgetItem = widgetItemPrefabTemplate->instantiate<Node3D>(it->widgetName);

            // Add the instance of the Widget Item Prefab prefab to the Widget Grid List Box node.
            // The Widget Grid List Box takes the ownership of the instance.
            m_widgetList->addItem(widgetItem);

            // Apply a translation to all widgets that are in the second row to arrange them
            // in a honeycomb formation. You arrange the widgets into three rows.
            // When the Widget Grid List Box arranges its items you tweak the position of the widgets
            // by applying the render transformation.
            if (distance(cbegin(widgetDescriptions), it) % 3 == 1)
            {
                widgetItem->setRenderTransformation(SRTValue3D::createTranslation(Vector3(2.75f, 0.0f, 0.0f)));
            }

            // Apply the texture to the icon by changing the IconTexture resource ID to point
            // to the image in the file system. The images are located in the working
            // directory of the application you are running.
            widgetItem->addResource(ResourceID("IconTexture"), "file://./" + it->iconName);

            // Set the name and the description for the widget using the same custom property
            // types you accessed in the previous step of this tutorial.
            // When you create a prefab in Kanzi Studio, the nodes of which you want
            // to customize in each instance of the prefab, Kanzi adds to the root of
            // the prefab the properties you want to edit, and creates a binding to
            // these properties in the nodes.
            widgetItem->setProperty(*m_widgetNamePropertyType, it->widgetName);
            widgetItem->setProperty(*m_widgetDescriptionPropertyType, it->description);
        }
}

```

When you run your application you can see instantiated and arranged Widget Item Prefab prefabs in the Widget Grid List Box node. Each widget in the Widget Grid List Box node has a name and an icon and you can scroll the list box horizontally. In the next step of this tutorial you implement the events that take place when the user selects a widget from the Widget Grid List Box.

Previous step Next step
