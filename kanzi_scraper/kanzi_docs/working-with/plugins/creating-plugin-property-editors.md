---
title: Defining a property editor
source: https://docs.kanzi.com/4.1.0/en/working-with/plugins/creating-plugin-property-editors.html
---

# Defining a property editor


In Kanzi Studio when you need a property editor that Kanzi Studio does not provide, you can define your own property editor. You define a property editor as a Kanzi Studio plugin.

For a list of available Kanzi Studio property editors, see Kanzi Studio property editors for property types declared in Kanzi Engine plugins.

To learn how to create a Kanzi Studio plugin, see Creating Kanzi Studio command plugins and Creating Kanzi Studio window plugins.

To find detailed information about the Kanzi Studio plugin API see:

- Overview of Kanzi Studio plugin API
- Kanzi Studio plugin API reference


This procedure shows how to define a property editor that enables the user to select a file.

To define a property editor:

1.

Create the base for a Kanzi Studio command plugin that extends the functionality of Kanzi Studio.

  1.

In Visual Studio select File > New > Project and select:

    - Visual C# > Class Library (.NET Framework)
    - Framework to .NET Framework 4.8


Click OK.
  2.

In the Solution Explorer right-click the project name, select Add > Reference, and add these references:

    1.

Select Assemblies > Framework > System.ComponentModel.Composition.
    2.

Click Browseâ¦ and add the reference to the `<KanziInstallation>/Studio/Bin/PluginInterface.dll` file.

  3.

In the Solution Explorer right-click the project name, select Properties, and:

    - In the Application tab set the Target framework to .NET Framework 4.8.
    - In the Build tab set the Platform target to x64.


2.

Implement the logic layer of the property editor using the `ViewModelFactory` class.

In the `ClassLibrary1` create a class, name it `FileSelectorViewModelFactory.cs`, and replace its content with:

```
using System;
using Rightware.Kanzi.Studio.PluginInterface;
using Rightware.Kanzi.Studio.PluginInterface.Editors;

namespace ClassLibrary1
{
   // Implement the PluginPropertyValueEditorContextFactory interface to allow Kanzi Studio
   // to create an instance of the editor ViewModel. For simple editors instead of
   // implementing your own PluginPropertyValueEditorContext class, you can use the
   // BasePluginEditorViewModel class that implements the PluginPropertyValueEditorContext
   // interface. This interface describes how you handle property value changes in
   // Kanzi Studio.
   //
   // If you want to add a more complex logic behind the property editor then it is a good idea
   // to create a separate ViewModel class that implements PluginPropertyValueEditorContext
   // or inherits the BasePluginEditorViewModel class.
   //
   // For Kanzi Studio to create an instance of the ViewModel, you must implement
   // the ViewModelFactory.
   public class FileSelectorViewModelFactory : PluginPropertyValueEditorContextFactory
   {
      public PluginPropertyValueEditorContext Create(object initialValue, Action<object> valueSetCallback)
      {
            // You can use the BasePluginEditorViewModel that contains the PropertyValue Property
            // which you can bind to a user control.
            return new BasePluginEditorViewModel(initialValue, valueSetCallback);
      }
   }
}

```

3.

Implement the presentation layer of the property editor using a `UserControl`.

  1.

In Visual Studio in the Solution Explorer right-click the project name, select Add > New Item, select a User Control (WPF) file type, and name it FileSelector.xaml.
  2.

Replace the content of `FileSelector.xaml` with:

```
<UserControl x:Class="ClassLibrary1.FileSelector"
      xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
      xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
      mc:Ignorable="d"
      d:DesignHeight="450" d:DesignWidth="800">
   <Grid>
      <Grid.ColumnDefinitions>
            <ColumnDefinition Width="*"/>
            <ColumnDefinition Width="30"/>
      </Grid.ColumnDefinitions>
      <TextBox Name="tbFileName" Grid.Column="0" Text="{Binding PropertyValue}"/>
      <Button Grid.Column="1" Click="Button_Click">...</Button>
   </Grid>
</UserControl>

```


For this property editor you use the `Grid` WPF control to lay out the editor, and create:

    - A text box where you can enter a file name.

You bind the `Text` property of the `TextBox` control to the property that you want to edit: `Text="{Binding PropertyValue}"`. `PropertyValue` comes from the logic layer. This way Kanzi Studio keeps track of changes in the `TextBox` control.
    - A button that you can use to select a file.

To create a button that opens a window where you can select a file, use a `Click` handler for the `Button`.

  3.

Replace the content of the `FileSelector.xaml.cs` with:

```
using System.Windows;
using System.Windows.Controls;
using Microsoft.Win32;

namespace ClassLibrary1
{
   public partial class FileSelector : UserControl
   {
      public FileSelector()
      {
            InitializeComponent();
      }

      // Define the behavior when the user clicks the button in the file selector editor.
      private void Button_Click(object sender, RoutedEventArgs e)
      {
         // Check that the DataContext has the correct value.
         if (DataContext is BasePluginEditorViewModel editorContext)
         {
            // Open the window where the user can select a file.
            OpenFileDialog openFileDialog = new OpenFileDialog();
            if (openFileDialog.ShowDialog() == true)
            {
               // Write the path and file name of the selected file name in the TextBox.
               editorContext.PropertyValue = openFileDialog.FileName;
            }
         }
      }
   }
}

```


4.

Implement the Kanzi Studio plugin class where you define the property editor.

To create a file selector editor, add a class to the `ClassLibrary1` class, name it `FileSelectorSettings.cs`, and replace its content with:

```
using System.ComponentModel.Composition;
using System.Windows;
using Rightware.Kanzi.Studio.PluginInterface;

namespace ClassLibrary1
{
   // This way you tell Kanzi Studio that this class contains plugin settings.
   [Export(typeof(PluginContent))]
   public class FileSelectorSettings : PluginPropertyValueEditorSettings
   {
      // Add the property that sets the editor name. Use this name when you set
      // the value of the editor for a custom property type that you define in
      // a Kanzi Engine plugin.
      public string Name => "FileSelectorEditor";

      // These properties set the name and a description for the property editor in Kanzi Studio.
      public string DisplayName => "File selector editor";
      public string Description => "Enables you to select a file.";

      // This way you enable Kanzi Studio to instantiate the UIControl.
      private DataTemplate dataTemplate;
      public DataTemplate DataTemplate
      {
            get
            {
               if (dataTemplate == null)
               {
                  dataTemplate = new DataTemplate();
                  dataTemplate.VisualTree = new FrameworkElementFactory(typeof(FileSelector));
               }
               return dataTemplate;
            }
      }

      // This way you allow Kanzi Studio to instantiate the DataContext
      // for the property editor.
      public PluginPropertyValueEditorContextFactory PropertyValueEditorContextFactory { get; } = new FileSelectorViewModelFactory();

      public void Initialize(KanziStudio studio)
      {

      }

      // Implement the IsCompatibleWith method to define the base data types that
      // the property editor can work with.
      public bool IsCompatibleWith(PluginPropertyDataType? propertyDataType)
      {
            return propertyDataType == PluginPropertyDataType.STRING;
      }
   }
}

```

5.

Build and prepare the Kanzi Studio plugin for use.

  1.

In Visual Studio select Build > Build Solution
  2.

Copy the Kanzi Studio plugin DLL file to the `%ProgramData%\Rightware\<KanziVersion>\plugins` directory.

If the `plugins` directory does not exist in `%ProgramData%\Rightware\<KanziVersion>`, create it.

> **Tip:** In File Explorer, create a shortcut from your Kanzi Studio plugin DLL file and move the shortcut to the `%ProgramData%\Rightware\<KanziVersion>\plugins` directory.
>
> When you build the plugin, you can see in the Output window the location where Visual Studio stored the plugin DLL file.


When you open or restart Kanzi Studio, in a Kanzi Studio project in the Library > Property Types create or select a property type, and set:

- Data Type to Text
- Editor to File selector editor


When you add this property type to a node, in the Properties use the editor that you defined to set the value of the property type.
## Using a custom property editor with Kanzi Engine custom property types


To use a custom property editor for a custom property type that you define in a Kanzi Engine plugin, in the Kanzi Engine plugin in the property editor metadata declarations for that property type set `metadata.editor` to the name of the editor that you want to use.

The name of the editor is set in the `Name` property of the class where you define the property editor.

For example, to set the custom File selector editor as a property editor, use:

```
PropertyType<string> VideoView2D::VideoFileNameProperty(kzMakeFixedString("VideoView2D.VideoFileName"), "", 0, false,
                                                     KZ_DECLARE_EDITOR_METADATA
                                                     (
                                                         metadata.editor = "FileSelectorEditor"
                                                         metadata.displayName = "Video Filename";
                                                         metadata.tooltip = "Video file to be played";
                                                         metadata.host = "VideoView2D:freq";
                                                     ));

```
