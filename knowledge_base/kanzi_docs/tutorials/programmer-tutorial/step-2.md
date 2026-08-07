---
title: Step 2 - Access the content created in the Kanzi Studio project
source: https://docs.kanzi.com/4.1.0/en/tutorials/programmer-tutorial/step-2.html
---

# Step 2 - Access the content created in the Kanzi Studio project

In this tutorial you create a widget store where you can browse and select widgets in one view and select widgets to see their descriptions in another view. When running the project at the end of the previous step you saw only the application background. The kzb file you created from the Kanzi Studio project and loaded using the API in the previous step of this tutorial, includes all the nodes and resources you need to create the application logic using the API:

- A Grid List Box 3D node named Widget Grid List Box is the node into which you dynamically load the widget representations using the API. The Grid List Box node defines the layout and interaction behavior for the items it shows.

You can find it in the Node Tree window in Widget Store Screen > Widget Store Root Layer > Main Scene Viewport > MainScene.
- A prefabricated template named Widget Item Prefab which defines the properties of each widget item listed in the Widget Grid List Box list of widgets. To add widgets to the Widget Grid List Box node, you create instances of this prefab with a different name, icon, and description for each widget.

You can find it in the Prefabs window.
- An Empty Node 2D node named Widget Description Layer is used as a description panel that shows the description for the selected widget. This node is hidden until the user selects a widget from the Widget Grid List Box.

You can find it in the Node Tree window in Widget Store Screen > Widget Store Root Layer.
- Custom property types used to set the widget name, description, and texture.
- Aliases to access the content from the kzb file using the Kanzi Engine API, and the resource IDs for the animation clips.

You can see the aliases in the resource dictionary for the node you select in the Node Tree in the Dictionaries window.

To access content from the Kanzi Studio project using the Kanzi Engine API:

1.

To create the prefab instances and add them to the Widget Grid List Box node you need to get access to these assets by loading them from the project. To access the loaded project assets in the application code later, create and store the assets in the member variables of your application class.

```
private:

    // Grid List Box 3D node which contains the widgets.
    GridListBox3DSharedPtr m_widgetList;

    // The currently selected widget in the Widget Grid List Box node.
    GridListBox3D::ItemSharedPtr m_selectedItem;

    // The camera of the scene.
    CameraSharedPtr m_camera;

    // Transformation target for the camera animation.
    SRTValue3D m_cameraTransformationTarget;

    // Animation clip for animating the camera.
    SRTValue3DAnimationSharedPtr m_cameraAnimation;

    // Timeline playback for animating the camera.
    TimelinePlaybackSharedPtr m_cameraPlayback;

    // Timeline playback for highlighting the item.
    TimelinePlaybackSharedPtr m_widgetHighlightPlayback;

    // Timeline playback for enabling the Back button.
    TimelinePlaybackSharedPtr m_backButtonEnablePlayback;

    // Animation clip item for animating the selected widget.
    SRTValue3DAnimationSharedPtr m_selectedItemAnimation;

    // Description panel that contains the description of the selected
    // widget and the Back button.
    NodeSharedPtr m_widgetDescriptionNode;

    // Animation clip for animating the visibility of the widget description.
    BoolAnimationSharedPtr m_widgetDescriptionVisibilityAnimation;

    // Timeline playback for animating visibility of the widget description.
    TimelinePlaybackSharedPtr m_widgetDescriptionVisibilityPlayback;

    // Text Block 3D node that shows the widget description in the
    // Widget Description Layer node.
    TextBlock3DSharedPtr m_widgetDescriptionTextBlock;

    // Back button on the widget.
    NodeSharedPtr m_backButton;

    // Animation clip for disabling and enabling the Back button.
    BoolAnimationSharedPtr m_backButtonEnableAnimation;

    // User-defined property type for storing the names of widgets.
    OptionalStringDynamicPropertyType m_widgetNamePropertyType;

    // User-defined property type for storing the descriptions for widgets.
    OptionalStringDynamicPropertyType m_widgetDescriptionPropertyType;

```

2.

In the `ProgrammerTutorialApplication` class after the `Application::onConfigure` function add the `Application::onProjectLoaded` function.

When you place a function inside the `Application::onProjectLoaded` Kanzi calls that function after it loads your application.

```
protected:

    // Initializes application when project is loaded.
    void onProjectLoaded() override
    {
    }

```

3.

To access the nodes in the kzb file you first have to get the Screen node and then use either aliases or relative paths to get each node.

Use an Alias to get consistent access to a Kanzi node. You can use aliases to access nodes both in Kanzi Studio and using the Kanzi Engine API.

Because you move nodes in the node tree of your project while creating your application in Kanzi Studio, the easiest way to keep track of them is to use aliases. You can retrieve alias target nodes with bindings or the Kanzi Engine API using the hash sign (`#`) followed by the name of the alias, regardless of the node location in the project. See Using aliases.

For example, in this tutorial the alias for the Widget Grid List Box is named Widget list and is stored in the resource dictionary of the Widget Store Screen node. Use #Widget list to access the Widget Grid List Box node using its alias in the API.

```
void onProjectLoaded() override
{
    // Get the Screen node in the kzb file. You use the Screen node to access all the other nodes and resources in the kzb file.
    ScreenSharedPtr screen = getScreen();

    // Access content from the Kanzi Studio project binary.

    // Get the reference to the Widget Grid List Box node to which you add instances
    // of the Widget Item Prefab prefabricated template.
    // You can set to which node the alias points in the Kanzi Studio project.
    m_widgetList = screen->lookupNode<GridListBox3D>("#Widget list");

    // Get the reference to the Camera node. You need the reference to the Camera node
    // so that you can animate it when the user selects a widget.
    m_camera = screen->lookupNode<Camera>("#Camera");

    // Create target transformation for camera animation.
    m_cameraTransformationTarget = SRTValue3D(Vector3(1.0f, 1.0f, 1.0f), Vector3(degreesToRadians(60.0f), degreesToRadians(0.0f), 0.0f), Vector3(-1.5f, 7.0f, -5.0f));

    // Get the reference to the Widget Description Layer node. This node is shown
    // when the user selects a widget and is used as a panel that contains the
    // widget description.
    m_widgetDescriptionNode = screen->lookupNode<Node>("#Widget description layer");

    // Get the reference to the Text Block node in the Widget Description Layer node
    // where the widget description is shown.
    m_widgetDescriptionTextBlock = screen->lookupNode<TextBlock3D>("#Widget description");

    // Get the reference to the reusable prefab (template) for the widget icons.
    // Domain is a collection of all subsystems and contains the Kanzi resource manager. You need to get the resource manager to access the resources in the .kzb file.
    ResourceManager* resourceManager = getDomain()->getResourceManager();
    PrefabTemplateSharedPtr widgetItemPrefabTemplate = resourceManager->acquireResource<PrefabTemplate>("kzb://programmer_tutorial/Prefabs/Widget Item Prefab");

    // Get the reference to the back button in the description layer.
    m_backButton = screen->lookupNode<Node>("#Back button");

    // Create animation clip for disabling and enabling back button.
    m_backButtonEnableAnimation = FromToAnimation<bool, StepEasingFunction>::create(getDomain(), chrono::seconds(1), false, true);

    // Create animation clip for hiding the description layer.
    m_widgetDescriptionVisibilityAnimation = FromToAnimation<bool, StepEasingFunction>::create(getDomain(), chrono::seconds(1), true, false);

    // Create animation clip for animating selected list box item.
    m_selectedItemAnimation = FromToAnimation<SRTValue3D, LinearEasingFunction>::create(getDomain(), chrono::milliseconds(800),
            SRTValue3D(Vector3(1.0f, 1.0f, 1.0f), Vector3(degreesToRadians(0.0f), 0.0f, 0.0f),  Vector3(0.0f, 0.0f, 0.0f)),
            SRTValue3D(Vector3(1.0f, 1.0f, 1.0f), Vector3(degreesToRadians(60.0f), 0.0f, 0.0f), Vector3(0.0f, 0.0f, 1.0f)));
}

```

4.

In this tutorial, you use the custom property types defined in the Kanzi Studio project. To access these custom property types, create a `DynamicPropertyType` and use the same name that you use in the Kanzi Studio project.

Resources are wrapped in a shared pointer and properties are wrapped in an optional.

```
class ProgrammerTutorialApplication: public ExampleApplication
{
...
    // Optional type for the string custom property types.
    using OptionalStringDynamicPropertyType = OptionalDynamicPropertyType<string>;

protected:

    void onProjectLoaded() override
    {
    ...
        // Get the custom property type for storing the widget name. This custom
        // property type is created in the Kanzi Studio project.
        m_widgetNamePropertyType = DynamicPropertyType<string>::tryCreate("Programmertutorial.WidgetName");

        // Get the custom property type for storing the widget description. This custom
        // property type is created in the Kanzi Studio project.
        m_widgetDescriptionPropertyType = DynamicPropertyType<string>::tryCreate("Programmertutorial.WidgetDescription");
    }
    ...
};

```

Previous step Next step
