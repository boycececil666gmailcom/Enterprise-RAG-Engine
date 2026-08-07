---
title: Step 3 - Load the locales and instantiate the prefabs
source: https://docs.kanzi.com/4.1.0/en/tutorials/localization-rtl/step-3.html
---

# Step 3 - Load the locales and instantiate the prefabs


In this step you use the Kanzi Engine API to load the locale packs for locales in your application, and instantiate the prefabs containing the buttons and layouts for the left-to-right and right-to-left locales when the user clicks a locale button in the Kanzi application.
## Load the locale packs


In this section you use the Kanzi Engine API to load the locale packs for locales in your application. You use the API to instantiate the correct IVI Grid and LocaleButton prefab with the correct layout for the selected locale.

To load the locale packs:

1.

In File Explorer in the `<ProjectName>/Application/bin/Locale_packs` directory open the `binaries.cfg` file in the text editor and add to the file the Arabic and Hebrew kzb files that contain the locale packs for these locales. Add the name of only one kzb file on each line.

The `binaries.cfg` file already contains the Japanese, Chinese, and Korean kzb files.

```
ja-JP
ko-KR
zh-ZH
ar-AR
he-HE

```

2.

In Kanzi Studio, select File > Open Kanzi Command Prompt.

The Kanzi Command Prompt opens the Windows Command Prompt with the Kanzi environment variables set for the version of Kanzi for which you open a Kanzi Command Prompt.

Use the Kanzi Command Prompt to access Kanzi utilities and build tools, such as Gradle and CMake, without using absolute paths or setting environment variables.

> **Tip:** You can find the Kanzi Command Prompt in the Windows Start Menu in the Rightware directory.
>
> When you have more than one version of Kanzi installed, make sure that you launch a Kanzi Command Prompt for the version of Kanzi with which you want to work in that command prompt.
> 3.
>
> In the Kanzi Command Prompt in the `<KanziWorkspace>/Tutorials/Localization/Completed/Application` directory run the script that generates a Visual Studio solution for the tutorial application.
>
> ```
> generate_cmake_vs2022_solution.bat
>
> ```


This script generates a Visual Studio solution for the application in the directory `<KanziWorkspace>/Tutorials/Localization/Completed/Application/build_vs2022`.
4.

In Visual Studio open the `<KanziWorkspace>/Tutorials/Localization/Completed/Application/build_vs<Version>/Localization.sln` Visual Studio solution.
5.

In Visual Studio in the Solution Explorer right-click the Localization project and select Set as StartUp Project.
6.

Create a set that contains the names of the Arabic and Hebrew locales, and get the property types that you created in Kanzi Studio to set the name and control the locale in the application.

When you add locales, you use the set to check whether the locale is in the right-to-left locale set.

In the localization.cpp file, after:

```
class LocalizationApplication : public ExampleApplication
{
    // Optional type for the string custom property types.
    using OptionalStringDynamicPropertyType = OptionalDynamicPropertyType<string>;

```


add

```
// Create a set which contains the names of the right-to-left locales.
set<string> m_rtlLocales;

// Get the custom property type for setting the name of the locale in the
// LocaleButton node. You created this custom property type in the Kanzi Studio project.
OptionalStringDynamicPropertyType m_localeNameProperty;

// Get the custom property type for setting the locale in the application.
// You created this custom property type in the Kanzi Studio project.
OptionalStringDynamicPropertyType m_localeIdProperty;

```

7.

In the `Application::onProjectLoaded` function, get the Locales and LocaleSelector nodes, the custom property types for setting the name and the locale, and add the Arabic and Hebrew locales to the right-to-left locale set.

Replace the content of the `Application::onProjectLoaded` function with this:

```
void onProjectLoaded() override
{
    // Get the IVI Grid node so that you can add a message filter to it.
    Node2DSharedPtr iviGrid = getRoot()->lookupNode<Node2D>("IVI Grid");

    // Get the custom property type for setting the name of the locale in the LocaleButton node. This custom property type is defined in the Kanzi Studio project.
    m_localeNameProperty = DynamicPropertyType<string>::tryCreate("Localization.LocaleName");

    // Get the custom property type for setting the locale in the application. This custom property type is defined in the Kanzi Studio project.
    m_localeIdProperty = DynamicPropertyType<string>::tryCreate("Localization.LocaleID");

    // Add a message filter to the IVI Grid node to find out when user clicks any of the locale buttons in the LocaleSelector node.
    iviGrid->addMessageFilter(ButtonConcept::ClickedMessage, bind(&LocalizationApplication::onLocaleButtonClicked, this, placeholders::_1));

    // Add the right-to-left locales to the set. You use this set to identify which locales are right-to-left and use the correct IVI Grid layout
    // for the selected locale.
    m_rtlLocales.insert("ar-AR");
    m_rtlLocales.insert("he-HE");
}

```

8.

Under the previous block of code you pasted, in the `Application::onProjectLoaded` function load the localized resources from the locale packs:

```
// Set the name of the directory where you stored the locale packs.
const string localePacksDirectory = "Locale_packs";

// Read the binaries.cfg file that contains the list of the kzb files that contain the locale packs.
string configFileName = localePacksDirectory + "/binaries.cfg";
ReadOnlyDiskFile binariesConfigFile(configFileName);
string binariesConfigContents = readAsText(binariesConfigFile);
stringstream binariesConfigFileStream(binariesConfigContents);

string localeId;

// Load the localized resources stored in the each locale pack kzb file stored in the binaries.cfg file.
while (getline(binariesConfigFileStream, localeId))
{
    // Remove whitespace.
    trim(localeId);

    // Create the path for the kzb file.
    string localizationKzbFilePath = "./" + localePacksDirectory + "/" + localeId + ".kzb";

    // Add the kzb file to the Kanzi resource manager.
    ResourceManager* resourceManager = getResourceManager();
    resourceManager->addKzbFile(localizationKzbFilePath);

    // Get the locale dictionary.
    string dictionaryUrl = "kzb://localization/Locales/" + localeId;
    ResourceDictionarySharedPtr localeDictionary = getResourceManager()->acquireResource<ResourceDictionary>(dictionaryUrl);

    // From the LocaleDisplayName resource ID in the localization table of the locale get the name of the locale that you want to show in the UI.
    TextResourceSharedPtr localeDisplayName = localeDictionary->acquire<TextResource>(ResourceID("LocaleDisplayName"));

    // Get the LocaleSelector Stack Layout 2D node which positions the LocaleButton Toggle Button 2D nodes.
    StackLayout2DSharedPtr localeSelector = getRoot()->lookupNode<StackLayout2D>("./IVI Grid/IVI Grid LeftToRight/Locales/LocaleSelector");

    // Check whether the locale is in the rtlLocales set.
    if (m_rtlLocales.count(localeId) > 0)
    {
        // Get the LocaleButton RightToLeft prefab and set up the button before you add it to the LocaleSelector node.
        Node2DSharedPtr localeButton = createLocaleButton("kzb://localization/Prefabs/LocaleButton RightToLeft", localeDictionary, localeDisplayName, localeId);
        // Add the LocaleButton node to the LocaleSelector node.
        localeSelector->addChild(localeButton);
    }
    else
    {
        // Get the LocaleButton LeftToRight prefab and set up the button before you add it to the LocaleSelector node.
        Node2DSharedPtr localeButton = createLocaleButton("kzb://localization/Prefabs/LocaleButton LeftToRight", localeDictionary, localeDisplayName, localeId);
        // Add the LocaleButton node to the LocaleSelector node.
        localeSelector->addChild(localeButton);
    }
}

```

9.

Define the `createLocaleButton` function, which returns either the left-to-right or right-to-left LocaleButton prefab, depending on whether the application loads a left-to-right or right-to-left locale. After the `Application::onProjectLoaded` function add:

```
Node2DSharedPtr createLocaleButton(string url, ResourceDictionarySharedPtr localeDictionary, TextResourceSharedPtr localeDisplayName, string localeId)
{
    // Get and instantiate the LocaleButton RightToLeft prefab used for the buttons that set right-to-left locales.
    // When you use the full kzb resource URL, start the path with kzb:// followed by the project name and the location of the resource.
    PrefabTemplateSharedPtr localeButtonPrefab = getResourceManager()->acquireResource<PrefabTemplate>(url);
    Node2DSharedPtr localeButton = localeButtonPrefab->instantiate<Node2D>("LocaleButton_" + localeId);

    // Use the LocaleName property to show the name of the locale in the UI.
    localeButton->setProperty(*m_localeNameProperty, localeDisplayName->getText());
    // Set the LocaleID property. You get the value of this property when the user clicks a LocaleButton and use it to change the application to that locale.
    localeButton->setProperty(*m_localeIdProperty, localeId);

    // Add the Index in Group property so that the Locales Toggle Button Group 2D node automatically sets the index of the toggle button.
    localeButton->setProperty(ButtonConcept::IndexInGroupProperty, -1);

    // Set the style of the Text Block 2D node in the LocaleButton so that it sets the correct font for the LocaleDisplayName of the locale.
    // Use this approach only to apply a style from the locale pack without changing the locale in the application.
    StyleSharedPtr style = localeDictionary->acquire<Style>(ResourceID("LocaleStyle"));
    localeButton->setStyle(style);

    return localeButton;
}

```

10.

After the `createLocaleButton` function implement the `onLocaleButtonClicked` event handler for the button click message from the LocaleButton nodes. When the user clicks a LocaleButton button, this event handler removes the existing layout, instantiates and adds the correct IVI Grid node layout, and sets the locale of the application.

```
void onLocaleButtonClicked(ButtonConcept::ClickedMessageArguments& messageArguments)
{
    // Get the value of the LocaleID property from the button the user clicked.
    string localeId = messageArguments.getSource()->getProperty(*m_localeIdProperty);

    // Check whether the selected locale is right-to-left or left-to-right.
    bool rtl = m_rtlLocales.count(localeId) > 0;
    // Set the path variable to the Locales Toggle Button Group 2D node in the IVI Grid layout for the selected locale.
    string pathToNewParent = rtl ? "IVI Grid/IVI Grid RightToLeft/Locales" : "IVI Grid/IVI Grid LeftToRight/Locales";

    // Store the existing Stack Layout 2D node with the LocaleButton Toggle Button 2D nodes.
    StackLayout2DSharedPtr localeSelector = messageArguments.getSource()->lookupNode<StackLayout2D>("..");

    // Remove the existing locale selector node from the tree.
    Node2DSharedPtr oldLocaleSelectorParent = localeSelector->lookupNode<Node2D>("..");
    oldLocaleSelectorParent->removeChild(*localeSelector);

    // Set the locale of the application to the locale whose button the user selected.
    getScreen()->setLocale(localeId);

    // Get the Locales Toggle Button Group 2D node and add the LocaleSelector Stack Layout 2D node to it.
    ToggleButtonGroup2DSharedPtr toggleButtonGroup = getRoot()->lookupNode<ToggleButtonGroup2D>(pathToNewParent);
    toggleButtonGroup->addChild(localeSelector);
}

```

11.

Select the solution configuration that you want to use and run your application.

During development, select the Debug configuration. When you are ready to create a version for production, select the Release configuration.


In the application when you click the Arabic and Hebrew locales, the application instantiates the correct layout for the locale.

Previous step
## Whatâs next?


In this tutorial you learned how to prepare an already localized Kanzi application for right-to-left locales and how to use the Kanzi Engine API to instantiate the prefabs which set the layout for the left-to-right and right-to-left locales. Now you can:

- Learn more about localizing Kanzi applications. See Tutorial: Localize your application and Localization.
- Learn how to add logic to your Kanzi applications using the Kanzi Engine API. See Tutorial: Hello world! and Tutorial: Kanzi Engine API advanced use.
