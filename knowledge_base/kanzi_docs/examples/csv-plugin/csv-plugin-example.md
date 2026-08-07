---
title: CSV plugin example
source: https://docs.kanzi.com/4.1.0/en/examples/csv-plugin/csv-plugin-example.html
---

# CSV plugin example


Kanzi uses the gettext PO file format to handle localized text resources and sets the text direction based on the first character in a string.

In PO files, you can use Unicode characters. With Unicode characters, you can also control text direction, such as the direction of left-to-right text in right-to-left locales. To learn how to control text direction with Unicode characters, see [How to use Unicode controls for bidi text](https://www.w3.org/International/questions/qa-bidi-unicode-controls).

When you use Unicode characters, make sure you insert them correctly. On Windows and Linux, you can use the Character Map application.

To learn more about the gettext PO file format, see [The Format of PO Files](http://www.gnu.org/software/gettext/manual/gettext.html#PO-Files).

If you want to define your own import and export format for the localized text resources, use the Kanzi Studio localization plugin API to create a Kanzi Studio plugin. You can find an example of such plugin, which uses CSV to export and import text into localization tables, in the `<KanziWorkspace>/Examples/CsvPlugin` directory.

> **Note:** When localized text contains a combination of simple and complex scripts, or left-to-right and right-to-left locales, in some cases the Kanzi Studio Localization Editor renders the text differently from the Kanzi Studio Preview. To fine-tune the text, use the Unicode control characters in the Localization Editor or in the PO files.
>
> When you import localized content with the CSV plugin:
>
> - Ignores the content of the first two cells in the first two columns (the ResourceID and the Default Text).
> - Ignores the changes to the Default Text column for existing resource IDs.
> - Imports the content with resource IDs that do not yet exist in the localization table.


The Kanzi Studio localization plugin API is written in .NET 4.0 and the `CsvPlugin` example plugin is written in C#. See Kanzi Studio localization plugin API reference.

The CsvPlugin example directory contains:

- `bin` directory contains the Kanzi Studio plugin created from the `CsvPlugin.sln` example Visual Studio solution.
- `lib` contains the library dependencies for creating localization plugins.
- `Properties` contains a file with the plugin .dll metadata, such as version information.
- `Src` contains the source files used in the `CsvPlugin.sln` solution for the example plugin.
- `CsvPlugin.sln` is a Visual Studio solution that implements the Kanzi Studio plugin you can use to import and export localized text resources using .csv files.

## Importing and exporting localized text resources using a custom file format


To import and export localized text resources using a custom file format:

1.

Create a plugin using the Kanzi Kanzi Studio localization plugin API. You can find the reference documentation for the [Kanzi Studio localization plugin API](https://docs.kanzi.com/latest-4-0/en/reference/kanzi-localization-api/index.html) online.

For an example plugin that enables you to import and export localized text resources in .csv file format, open the `<KanziWorkspace>/Examples/CsvPlugin/CsvPlugin.sln` example in Visual Studio.
2.

When you are done writing your plugin, create the plugin .dll, and copy the plugin .dll to the `%ProgramData%/Rightware/<KanziVersion>/plugins` directory on your computer. If the `plugins` directory does not already exist there, create it.

For example, if you are using the example `CsvPlugin.sln` solution, when you are done writing the plugin:

  - You can build the plugin without the Visual Studio using the Microsoft Windows SDK for Windows 7 and .NET Framework 4. In the Windows command line run the MSBuild.exe in the directory that contains the Visual Studio solution for your plugin.


Or

  - In Visual Studio Solution Explorer right-click the `CsvPlugin` project and select **Build**.


The `CsvPlugin.sln` solution is configured to create the plugin .dll in `<KanziWorkspace>/Examples/CsvPlugin/bin`.
3.

Open Kanzi Studio and open an existing or create a new project. If you already have Kanzi Studio opened, restart it to load your plugin the first time.
4.

If Kanzi Studio successfully loads your plugin, in the Library right-click any localization table and in the context menu select the commands you added with the plugin.

For example, if you use the `CsvPlugin` example plugin .dll, the plugin adds context menu commands Export CSV and Import CSV.
5.

When you make changes to your plugin, after creating the .dll and copying the plugin .dll to the `%ProgramData%/Rightware/<KanziVersion>/plugins` directory, restart Kanzi Studio to take the newer version of the plugin into use.
