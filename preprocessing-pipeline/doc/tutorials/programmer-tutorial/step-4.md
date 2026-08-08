---
title: Step 4 - Create the interaction handler for selecting a widget
source: https://docs.kanzi.com/4.1.0/en/tutorials/programmer-tutorial/step-4.html
---

# Step 4 - Create the interaction handler for selecting a widget

In this tutorial you create an application in which users can scroll the list of widgets contained in the Widget Grid List Box and enable them to select from that list a widget represented by a Widget Item Prefab. The Grid List Box 3D node provides the horizontal scrolling you can set in the Kanzi Studio project, but you need to define the application logic that handles the widget selection.

In this step of the tutorial you implement the functionality that handles the selection of the widget item when the user clicks a widget:

- Trigger the animation that zooms the camera to a position so that the selected widget is highlighted on the left side of the application window.
- Trigger the animation that orients the selected widget towards the camera to highlight it.
- Make visible the description panel represented by the Widget Description Layer node on the right side of the application window. The description panel contains the description for each widget, a back button and a buy button. When the Widget Description Layer is visible, the scrolling of the Widget Grid List Box is disabled. While the camera zoom animation is going, the Back button is disabled.

To create the interaction handler for selecting a widget:

1.

In the `ProgrammerTutorialApplication` class after the `Application::onProjectLoaded` function implement the event handler for selecting the widgets in the Widget Grid List Box. Use the index of the selected widget to retrieve the selected widget from the Widget Grid List Box node.

```
class ProgrammerTutorialApplication : public ExampleApplication
{
...
private:

    // The handler for the ListBox.ItemSelected message from the Widget Grid List Box.
    // Brings the selected list box item to the front.
    void onListBoxItemSelected(ListBoxConcept::ItemSelectedMessageArguments& messageArguments)
    {
        // Retrieve the index of the selected list box item from the message arguments.
        optional<size_t> selectedItemIndex = messageArguments.getSelectedItemIndex();

        if (selectedItemIndex)
        {
            // Remove old playbacks to reset the values.
            // You implement this function in the next step of the tutorial.
            removePlaybacks();

            // Retrieve the selected list box item by its index.
            m_selectedItem = m_widgetList->getItem(*selectedItemIndex);
     ...
        }
    }
};

```

2.

A target animation repositions the camera. The animation takes the current transformation of the node and animates to another transformation defined by another node. Now the stored camera transformation is updated with the translation of the selected widget. Create the animation for the camera, and start the animation.

```
void onListBoxItemSelected(ListBoxConcept::ItemSelectedMessageArguments& messageArguments)
{
...
    if (selectedItemIndex)
    {
        ...
        // Calculate a new value for the camera animation target node and start the animation.
        {
            // Get the current transformation.
            Matrix4x4 selectedItemTransformation = m_selectedItem->getFinalTransformation();
            // Get the camera's relative transformation target position.
            SRTValue3D transformationTarget = m_cameraTransformationTarget;
            // Add the position of the selected item to the target camera transformation.
            transformationTarget.setTranslation(selectedItemTransformation.getTranslation() - transformationTarget.getTranslation());
            // Create the animation for the camera.
            m_cameraAnimation = FromToAnimation<SRTValue3D, LinearEasingFunction>::create(getDomain(), chrono::seconds(1), nullopt, transformationTarget);

            // Start the animation.
            PropertyAnimationTimelineSharedPtr cameraTimeline = PropertyAnimationTimeline::create(getDomain(), ".", Node3D::RenderTransformationProperty, m_cameraAnimation);
            SceneGraphTimelinePlaybackContext cameraContext(*m_camera);
            m_cameraPlayback = cameraTimeline->createPlayback(cameraContext);
            getDomain()->getRootTimelineClock()->addTimelinePlayback(m_cameraPlayback);
        }
    }
...
}

```

3.

Now that the transformation target of the Camera animation is updated, you can initiate the highlight animation for the selected widget. The highlight animation rotates the widget around its x axis from fixed values 0 to 60 degrees and is defined in the `Application::onProjectLoaded` function.

```
void onListBoxItemSelected(ListBoxConcept::ItemSelectedMessageArguments& messageArguments)
{
...
    if (selectedItemIndex)
    {
   ...
        // Start the animation for the selected item.
        PropertyAnimationTimelineSharedPtr selectedItemTimeline = PropertyAnimationTimeline::create(getDomain(), ".", Node3D::LayoutTransformationProperty, m_selectedItemAnimation);
        SceneGraphTimelinePlaybackContext selectedItemContext(*m_selectedItem);
        m_widgetHighlightPlayback = selectedItemTimeline->createPlayback(selectedItemContext);
        getDomain()->getRootTimelineClock()->addTimelinePlayback(m_widgetHighlightPlayback);
    }
}

```

4.

Disable input for the Back button when the animation starts.

```
void onListBoxItemSelected(ListBoxConcept::ItemSelectedMessageArguments& messageArguments)
{
...
    if (selectedItemIndex)
    {
    ...

        // Start the animation to disable input for the Back button.
        PropertyAnimationTimelineSharedPtr backButtonEnableTimeline = PropertyAnimationTimeline::create(getDomain(), ".", Button3D::HitTestableProperty, m_backButtonEnableAnimation);
        SceneGraphTimelinePlaybackContext backButtonEnableContext(*m_backButton);
        m_backButtonEnablePlayback = backButtonEnableTimeline->createPlayback(backButtonEnableContext);
        getDomain()->getRootTimelineClock()->addTimelinePlayback(m_backButtonEnablePlayback);
    }
}

```

5.

Get the widget description from the Programmertutorial.WidgetDescription property, and set the value of the Text property of the Text Block 2D node to the value of the Programmertutorial.WidgetDescription property, and make visible the Widget Description Layer that contains the panel on the right side of the application window.

```
void onListBoxItemSelected(ListBoxConcept::ItemSelectedMessageArguments& messageArguments)
{
...
    if (selectedItemIndex)
    {
    ...
        // Show the widget description by setting the Widget Description Layer visible.
        if (m_widgetDescriptionVisibilityPlayback)
        {
            getDomain()->getRootTimelineClock()->removeTimelinePlayback(*m_widgetDescriptionVisibilityPlayback);
            m_widgetDescriptionVisibilityPlayback.reset();
        }

        // Set the widget description to the description text. The description is taken from the widget node.
        string widgetDescription = m_selectedItem->getProperty(*m_widgetDescriptionPropertyType);
        m_widgetDescriptionTextBlock->setText(widgetDescription);

        // Set the Widget Description Layer visible.
        m_widgetDescriptionNode->setVisible(true);
    }
}

```

6.

In the `Application::onProjectLoaded` function register the message handler for the `ListBoxConcept::ItemSelectedMessage` of the Widget Grid List Box node after populating the widget list.

```
void onProjectLoaded() override
{
...
    // Add a message handler for selecting the Grid List Box 3D item events.
    m_widgetList->addMessageHandler(GridListBox3D::ItemSelectedMessage, bind(&ProgrammerTutorialApplication::onListBoxItemSelected, this, placeholders::_1));
}

```

When you click a widget, the application highlights the widget using the two animations you specified, makes the Widget Description Layer node visible and shows the widget description in the Widget Description Layer.

Previous step Next step
