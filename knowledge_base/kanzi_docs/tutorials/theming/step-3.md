---
title: Step 3 - Export and use the API to set the application theme
source: https://docs.kanzi.com/4.1.0/en/tutorials/theming/step-3.html
---

# Step 3 - Export and use the API to set the application theme

In this step of the tutorial you export the kzb files for both baked themes (defined in the Car variant theme group) and non-baked themes (defined in the Cluster theme theme group), and use the Kanzi Engine API to enable the user to change the non-baked themes in the application.
## Export kzb files

In this section you first set in the Kanzi Studio project how you want to export the themes in the project, then you export the themes.

This section shows how to export themes you defined in the Cluster theme theme group with themes you defined in the Car variant theme group as theme packs.

A Theme resource pack is a kzb file which contains only the resources for a selected Theme.

Use this approach when the storage or memory on your target device is limited, but you want to change the application theme at runtime without having to load additional kzb files.

For example, with this approach you can create from one Kanzi Studio project applications for two car variants (Gasoline and Hybrid), where each has two themes (Classic and Modern) between which you can switch in the application.

This is just one of the approaches of how you can export themes from your project. To find the approach that is most suitable for your product and target hardware, see Exporting Themes.

To export kzb files:

1.

From the Prefabs drag the Theme selector prefab to the Node Tree and drop it on the RootNode node.

In the next section you use the Kanzi Engine API to create a button which enables users to change the application theme.
2.

In the Library > Themes select the Car variant theme group and in the Properties set:

  - Export Baked Usages to enabled.

When you enable the Export Baked Usages property you can bake the resources from themes in this theme group.
  - Selected Theme to Car variant/DefaultValues. When you export the kzb files with this setting, Kanzi Studio sets the main kzb file to use the resources set in the default values in that theme group.

3.

In the Library > Themes select the Cluster theme theme group and in the Properties set the Selected Theme property to Cluster theme/DefaultValues.
4.

In the Library > Themes double-click the Cluster theme theme group to open it in the Theme Editor and click  next to the Classic and Modern themes.

This way you mark a theme to export theme resources.

When you enable the exporting of Theme resources the  icon in the Theme column turns blue  and Kanzi Studio exports the resources used in that Theme.
5.

Select File > Export > Export Baked Theme Binaries and in the Themes and Locales to Bake on Export window disable the Export Main Kzb setting.

In the Themes and Locales to Bake on Export window you can select which baked themes in the Car variant theme group you want to export.

Click Export.

Kanzi Studio creates:

  - One kzb file for each theme in the Car variant theme group, and exports the kzb file to the `<KanziWorkspace>/Tutorials/Theming/Start/Application/bin/<ThemeGroupName>=<BakedThemeName>` directory.

This kzb file includes the application node tree and all the resources that are used by more than one theme (common resources).
  - One kzb file for each theme in the Cluster theme theme group, and stores the files in the `Theme_packs` directory in each `<KanziWorkspace>/Tutorials/Theming/Start/Application/bin/<ThemeGroupName>=<BakedThemeName>` directory. Kanzi Studio uses theme names for the names of the theme packs kzb files.

Each of these kzb files includes only the resources used by that theme, without the common resources (which are stored in the Car variant kzb file).

6.

In a text editor:

  - Open the `Application/bin/Car variant=Gasoline/theming.kzb.cfg` and change

```
theming.kzb

```

to

```
Car variant=Gasoline/theming.kzb

```

  - Open the `Application/bin/Car variant=Hybrid/theming.kzb.cfg` and change

```
theming.kzb

```

to

```
Car variant=Hybrid/theming.kzb

```

## Add code to change the cluster theme

In this section you add the application code to start the application with the Classic theme and create a message handler which you add to the Theme selector Button 2D node to switch between the two themes you created in the Cluster theme theme group.

To add code to change the cluster theme:

1.

In Kanzi Studio, select File > Open Kanzi Command Prompt.

The Kanzi Command Prompt opens the Windows Command Prompt with the Kanzi environment variables set for the version of Kanzi for which you open a Kanzi Command Prompt.

Use the Kanzi Command Prompt to access Kanzi utilities and build tools, such as Gradle and CMake, without using absolute paths or setting environment variables.
**Tip:** You can find the Kanzi Command Prompt in the Windows Start Menu in the Rightware directory.
When you have more than one version of Kanzi installed, make sure that you launch a Kanzi Command Prompt for the version of Kanzi with which you want to work in that command prompt.
2.
In the Kanzi Command Prompt in the `<KanziWorkspace>/Tutorials/Theming/Start/Application` directory run the script that generates a Visual Studio solution for the tutorial application.
```
generate_cmake_vs2022_solution.bat
```

This script generates a Visual Studio solution for the application in the directory `<KanziWorkspace>/Tutorials/Theming/Start/Application/build_vs2022`.
3.

In Visual Studio open the `<KanziWorkspace>/Tutorials/Theming/Start/Application/build_vs<Version>/Theming_start.sln` Visual Studio solution.
4.

In Visual Studio in the Solution Explorer right-click the Theming_start project and select Set as StartUp Project.
5.

In the `theming.cpp` file in the `Theming` class create:

  - A struct which defines the theme name and kzb file URL and a vector which you use to store the names and kzb file URL for application themes.
  - A variable you use to keep track of the currently active theme.
  - A const string you use to set which baked theme you want to load at application startup.

```
class Theming : public ExampleApplication
{
    // Structure describing a theme.
    struct ThemeDescriptor
    {
        explicit ThemeDescriptor(const string& name, const string& url):
            m_name(name),
            m_url(url)
        {
        }

        // The name of the theme.
        string m_name;
        // The kzb file URL of the theme.
        string m_url;
    };

    // Collection of all theme descriptions.
    vector<ThemeDescriptor> m_themes;

    // The index of the currently active theme.
    int m_activeThemeIndex;

    // The name of the baked theme to load.
    static const string m_carVariant;

...

}

```

6.

After the `Theming` class use the `m_carVariant` variable you created in the previous step, to set which car variant you want to load at application startup.

```
// Select which baked theme to use.
// To start the application for the Hybrid car variant, set to 0.
// To start the application for the Gasoline car variant, set to 1.
#if 1
const string Theming::m_carVariant = "Gasoline";
#else
const string Theming::m_carVariant = "Hybrid";
#endif

```

7.

In the `Application::onConfigure` function use the .kzb.cfg file Kanzi Studio creates when exporting kzb file to load the application with the baked theme you can set in the previous step.

```
void onConfigure(ApplicationProperties& configuration) override
{
    configuration.binaryName = "./Car variant=" + m_carVariant + "/theming.kzb.cfg";
    configuration.defaultWindowProperties.width = 1920;
    configuration.defaultWindowProperties.height = 720;
}

```

8.

In the `Application::onProjectLoaded` function

```
void onProjectLoaded() override
{
    // Add names and URLs for all themes.
    m_themes.push_back(ThemeDescriptor("Classic", "kzb://theming/Themes/Cluster theme/Classic"));
    m_themes.push_back(ThemeDescriptor("Modern", "kzb://theming/Themes/Cluster theme/Modern"));

    // Load metadata from all kzb files which contain theme resources.
    ResourceManager* resourceManager = getResourceManager();
    resourceManager->addKzbFile("./Car variant=" + m_carVariant + "/Theme_packs/Cluster theme=Classic.kzb");
    resourceManager->addKzbFile("./Car variant=" + m_carVariant + "/Theme_packs/Cluster theme=Modern.kzb");

    // Activate the first theme at application startup.
    m_activeThemeIndex = -1;
    changeToNextTheme();
}

```

9.

After the `Application::onProjectLoaded` function create a function you use to activate the next theme in your application.

```
// Activates the next theme.
void changeToNextTheme()
{
    // Get the Text Block 2D node in the Theme selector Button 2D node so that you can change the text to show the name of the next theme.
    Button2DSharedPtr themeSelectorButton = getRoot()->lookupNode<Button2D>("Theme selector");
    TextBlock2DSharedPtr selectorThemeTextBlock = themeSelectorButton->lookupNode<TextBlock2D>("#Next theme name");

    // Get the descriptors for the next theme and the theme following the next theme.
    const int nextThemeIndex = (m_activeThemeIndex + 1) % m_themes.size();
    const int followingThemeIndex = (m_activeThemeIndex + 2) % m_themes.size();
    const ThemeDescriptor& nextTheme = m_themes.at(nextThemeIndex);
    const ThemeDescriptor& followingTheme = m_themes.at(followingThemeIndex);

    // Set the name of the following theme.
    selectorThemeTextBlock->setText(followingTheme.m_name);

    // Set the application theme to the next theme.
    getScreen()->activateTheme(nextTheme.m_url);
    m_activeThemeIndex = nextThemeIndex;
}

```

10.

In the `Theming` class after the `Application::onProjectLoaded` function create the `onChangeThemeButtonClicked` event handler where you define how the application reacts when user clicks the Theme selector button in the application.

```
// This message handler defines how the application reacts when the user clicks the Theme selector button in the application.
void onChangeThemeButtonClicked(ButtonConcept::ClickedMessageArguments& /* messageArguments */)
{
    changeToNextTheme();
}

```

11.

In the `Application::onProjectLoaded` function after loading the metadata from theme kzb files add the message handler that you created in the previous step to the Theme selector node.

```
void onProjectLoaded() override
{

...

    // Register the message handler for the Button: Click message used by the Theme selector node.
    Button2DSharedPtr themeSelectorButton = getRoot()->lookupNode<Button2D>("Theme selector");
    themeSelectorButton->addMessageHandler(ButtonConcept::ClickedMessage, bind(&Theming::onChangeThemeButtonClicked, this, placeholders::_1));

...

}

```

12.

Select the solution configuration that you want to use and run your application.

During development, select the Debug configuration. When you are ready to create a version for production, select the Release configuration.

In the application when you click the Theme selector button, you switch between the Classic and Modern cluster themes which you defined in the Cluster theme theme group.

Previous step
## Whatâs next?

In this tutorial you learned how to theme a Kanzi application to create different appearance of the same application and how to use a single Kanzi Studio project for more than one variant of your product. To take this tutorial further you can create assets for additional cluster themes and car variants. You can also:

- Find out about all the details of creating themes for your Kanzi applications. See Theming your applications.
- Learn how to use Kanzi Data Sources to separate the user interface from the application data. See Tutorial: Get application data from a data source.
- Learn how to localize your application. See Tutorial: Localize your application.
