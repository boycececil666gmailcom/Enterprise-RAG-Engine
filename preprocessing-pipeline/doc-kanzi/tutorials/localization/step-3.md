---
title: Step 3 - Load locale packs
source: https://docs.kanzi.com/4.1.0/en/tutorials/localization/step-3.html
---

# Step 3 - Load locale packs

In this step, you use the Kanzi Engine API to load the locale packs you created in the previous step of this tutorial in the Kanzi application.
## Use the Kanzi Engine API to load the locale packs

In this section, you use the Kanzi Engine API to load the locale packs that you created in the previous section. The application initializes the locale packs on startup and triggers loading the resources from locale packs for all locales stored in the `Application/bin/Locale_packs` directory.

To load the locale packs:

1.

In File Explorer in the `<KanziWorkspace>/Tutorials/Localization/Start/Application/bin/Locale_packs` directory, create a `binaries.cfg` file. Add to the file the location and name of each kzb file that contains a locale pack that you want to load. Add the name of only one kzb file on each line.

For example, if you have a locale pack for the Japanese, Korean, and Chinese locales, and you used the ja-JP locale name for the Japanese locale, ko-KR for the Korean locale, and zh-ZH for the Chinese locale, create the `binaries.cfg` file, open it in a text editor, add the names of these locale pack files to the `binaries.cfg` file, and save the file.

```
ja-JP
ko-KR
zh-ZH

```

2.

In Kanzi Studio, select File > Open Kanzi Command Prompt.

The Kanzi Command Prompt opens the Windows Command Prompt with the Kanzi environment variables set for the version of Kanzi for which you open a Kanzi Command Prompt.

Use the Kanzi Command Prompt to access Kanzi utilities and build tools, such as Gradle and CMake, without using absolute paths or setting environment variables.
**Tip:** You can find the Kanzi Command Prompt in the Windows Start Menu in the Rightware directory.
When you have more than one version of Kanzi installed, make sure that you launch a Kanzi Command Prompt for the version of Kanzi with which you want to work in that command prompt.
3.
In the Kanzi Command Prompt in the `<KanziWorkspace>/Tutorials/Localization/Start/Application` directory, run the script that generates a Visual Studio solution for the tutorial application.
```
generate_cmake_vs2022_solution.bat
```

This script generates a Visual Studio solution for the application in the directory `<KanziWorkspace>/Tutorials/Localization/Start/Application/build_vs2022`.
4.

In Visual Studio, open the `<KanziWorkspace>/Tutorials/Localization/Start/Application/build_vs<Version>/Localization_start.sln` Visual Studio solution.
5.

In Visual Studio in the Solution Explorer, right-click the Localization_start project and select Set as StartUp Project.
6.

In this tutorial, you use the custom property types defined in the Kanzi Studio project. To access these custom property types, create a `DynamicPropertyType` and use the same name that you use in the Kanzi Studio project.

In the localization.cpp file in the `LocalizationApplication` class, add:

```
class LocalizationApplication : public ExampleApplication
{

```

7.

In the `LocalizationApplication` class in the `Application::onProjectLoaded` function, implement the event handler that loads the resources for the locale pack kzb files stored in the `Locale_packs` directory and adds the locales to the project.

```
// Set the name of the directory where you stored the locale packs.
static const string localizationFolderName = "Locale_packs";

// Get the Screen node in the kzb file.
// You use the Screen node to access all the other nodes and resources in the kzb file.
ScreenSharedPtr screen = getScreen();
// Domain is a collection of all subsystems and contains the Kanzi resource manager.
// You need to get the resource manager to access the resources in the kzb file.
ResourceManager* resourceManager = getDomain()->getResourceManager();

// Get the LocaleSelector node which contains the locale selection buttons.
// Access alias target nodes using the # sign followed by the name of the alias.
Node2DSharedPtr localeSelector = screen->lookupNode<Node2D>("#LocaleSelector");

// Get the LocaleButton prefabricated template used for the buttons that set the locale.
// Get the reference to the template using the kzb URL.

// When you use the full path of a resource, start the path with kzb://
// followed by the project name and the location of the resource.
PrefabTemplateSharedPtr localeButtonPrefab = resourceManager->acquireResource<PrefabTemplate>("kzb://localization/Prefabs/LocaleButton");

// Get the custom property type for setting the name of the locale in the
// LocaleButton node. You created this custom property type in the Kanzi Studio project.
DynamicPropertyType<string> localeNameProperty = DynamicPropertyType<string>("Localization.LocaleName");

// Get the custom property type for setting the locale in the application.
// You created this custom property type in the Kanzi Studio project.
DynamicPropertyType<string> localeIdProperty = DynamicPropertyType<string>("Localization.LocaleID");

// Read the binaries.cfg file that contains the list of the kzb files
// that contain the locale packs.
string configFileName = localizationFolderName + "/binaries.cfg";
ReadOnlyDiskFile binariesConfigFile(configFileName);
string binariesConfigContents = readAsText(binariesConfigFile);
stringstream binariesConfigFileStream(binariesConfigContents);

string localeId;

// Load the resources stored in the locale pack kzb files.
while (getline(binariesConfigFileStream, localeId))
{
    trim(localeId);

    // Create the path for the kzb file.
    string localizationKzbFilePath = localizationFolderName + "/" + localeId + ".kzb";

    // Add the kzb file to the Kanzi resource manager.
    getResourceManager()->addKzbFile(localizationKzbFilePath);

    string dictionaryUrl = "kzb://localization/Locales/" + localeId;
    ResourceDictionarySharedPtr localeDictionary = getResourceManager()->acquireResource<ResourceDictionary>(dictionaryUrl);

    // Instantiate the LocaleButton prefab.
    Node2DSharedPtr localeButton = localeButtonPrefab->instantiate<Node2D>("LocaleButton_" + localeId);

    // Get the name of the locale that is shown in the application from the
    // resource ID LocaleDisplayName stored in the localization table in the locale pack.
    TextResourceSharedPtr localeDisplayNameResource = localeDictionary->acquire<TextResource>(ResourceID("LocaleDisplayName"));

    // Set the LocaleName property so that the Text Block 2D node in the button shows the name of the locale.
    localeButton->setProperty(localeNameProperty, localeDisplayNameResource->getText());
    // Set the LocaleID property so that when you click the button the application changes to that locale.
    localeButton->setProperty(localeIdProperty, localeId);

    // Set the style of the Text Block 2D node in the button so that it sets
    // the correct font for the LocaleDisplayName of the locale.
    // Use this approach only to apply a style from the locale pack without changing the locale
    // in the application.
    optional<string> localeStyle = localeDictionary->find(ResourceID("LocaleStyle"));
    StyleSharedPtr style = getResourceManager()->acquireResource<Style>(*localeStyle);
    localeButton->setStyle(style);

    // Add the LocaleButton node to the LocaleSelector node.
    localeSelector->addChild(localeButton);
}

```

8.

Select the solution configuration that you want to use and run your application.

During development, select the Debug configuration. When you are ready to create a version for production, select the Release configuration.

In the application, Kanzi loads the locale packs from the kzb files listed in the `binaries.cfg` file, and in the LocaleSelector node instantiates one LocaleButton prefab for each locale.

Previous step
## Whatâs next?

In this tutorial, you learned how to localize Kanzi applications and use in your applications additional kzb files that contain only localized resources for locales. To take this tutorial further, you can use the localization table POT template file to translate the content of this Kanzi application to additional languages. Additionally, you can create other resource types and create different resources for different locales. For example, create several animations and use each for a different locale:

- Find out about all the details of localizing Kanzi applications. See Localization.
- Learn how to localize your Kanzi application for right-to-left locales. See Tutorial: Localize applications for right-to-left locales.
- Learn how to add logic to your Kanzi applications using the Kanzi Engine API. See Tutorial: Hello world! and Tutorial: Kanzi Engine API advanced use.
- Create animations for each locale. See Tutorial: Create keyframe animations.
