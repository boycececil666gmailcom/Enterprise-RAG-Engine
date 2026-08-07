---
title: Deploying Kanzi applications to Windows
source: https://docs.kanzi.com/4.1.0/en/working-with/deploying-applications/deploying-kanzi-applications-for-windows.html
---

# Deploying Kanzi applications to Windows

You can build and deploy Kanzi applications to Windows:

- From Kanzi Studio (only Kanzi applications without a C++ application). See Building and deploying Kanzi applications to Windows from Kanzi Studio.
- From Visual Studio (only Kanzi applications with C++ application). See Building Kanzi applications from Visual Studio.

## Building and deploying Kanzi applications to Windows from Kanzi Studio

You can build and deploy to Windows a Kanzi application without a C++ application from Kanzi Studio.

To run a Kanzi application on Windows, you need to have Microsoft Visual C++ 2015-2019 Redistributable (x86) installed.

To build and deploy your Kanzi application to Windows from Kanzi Studio:

1.

In Kanzi Studio create or open the project for your Kanzi application and select File > Export > Export as KZB Player for Windows.

Kanzi Studio builds the application source code and creates these files in the `Application Player` directory of your Kanzi Studio project:

  - `application.cfg` contains configuration settings for your Kanzi application. See Application development.
  - `binaries.cfg` contains a list of all kzb files Kanzi created from your project.
  - `<ProjectName>`.exe contains your Kanzi application and the Kanzi Application Player, which enables you to run your application as a standalone application.
  - `<project_name>.kzb` contains your project in a binary format. See Kzb files.
  - `<project_name>.kzb.txt` contains a list of all project shortcuts, project resources, and nodes.

2.

When Kanzi Studio creates the application, it adds the link to the application in the Status Bar, which you can find below the Library window, and the Log window. Click the link to open the directory where Kanzi Studio created your application.

Your application is stored in the `Application Player` directory of your Kanzi Studio project.

To run the application, run the exe application file.

## Building Kanzi applications from Visual Studio

When your Kanzi application includes a C++ application or a Kanzi Engine plugin, build the application from Visual Studio. See Creating a project and Tutorial: Hello world!.

To build your Kanzi application from Visual Studio:

1.

In Kanzi Studio create a project using one of these templates:

  - Application
  - Application with data source plugin
  - Application with Kanzi Engine plugin

Kanzi creates a Kanzi Studio project in the `<ProjectName>/Tool_project` directory and the structure for the application code of your project in the `<ProjectName>/Application` directory:

  - `bin` directory contains the kzb and configuration files of your project.
  - `configs` directory contains the configuration files for different platforms. By default, Kanzi creates configuration files for several different platforms. The recommended platform for developing Kanzi applications is Microsoft Visual Studio. See Deploying Kanzi applications.
  - `src` directory contains the source code for your application.
  - `CMakeLists.txt` file contains the instructions for CMake to generate the Visual Studio solution for the Kanzi application.
  - `generate_cmake_vs<Version>_solution.bat` is a script that you can use to generate a Visual Studio solution for the Kanzi application. The script generates the Visual Studio solution in the `<ProjectName>/Application/build_vs<Version>` directory.

See Creating a project.
2.

In Kanzi Studio, select File > Open Kanzi Command Prompt.

The Kanzi Command Prompt opens the Windows Command Prompt with the Kanzi environment variables set for the version of Kanzi for which you open a Kanzi Command Prompt.

Use the Kanzi Command Prompt to access Kanzi utilities and build tools, such as Gradle and CMake, without using absolute paths or setting environment variables.
**Tip:** You can find the Kanzi Command Prompt in the Windows Start Menu in the Rightware directory.
When you have more than one version of Kanzi installed, make sure that you launch a Kanzi Command Prompt for the version of Kanzi with which you want to work in that command prompt.
3.
In the Kanzi Command Prompt in the `<ProjectName>/Application` directory, run the script that generates a Visual Studio solution for the application.
```
generate_cmake_vs2022_solution.bat
```

This script generates a Visual Studio solution for the application in the directory `<ProjectName>/Application/build_vs2022`.
4.

In Visual Studio open the `<ProjectName>/Application/build_vs<Version>/<ProjectName>.sln` Visual Studio solution.

For example, if you used the Application with data source plugin or Application with Kanzi Engine plugin template, the Visual Studio solution contains:

  - The project for the Kanzi Engine plugin named `<ProjectName>`. Define your Kanzi Engine plugin in this project.
  - The project for the C++ application named <ProjectName>_executable. Define the logic of your Kanzi application in this project.

5.

In Visual Studio create the logic for your Kanzi application and your Kanzi Engine plugin, and configure the custom components in your Kanzi Engine plugin for Kanzi Studio. See Application development, Creating Kanzi Engine plugins, Defining a data source, and Extending the functionality of Kanzi Engine.
6.

Select the solution configuration that you want to use.

During development select the Debug configuration. When you are ready to create a version for production, select the Release configuration.
7.

Build your application:

  - To build only the Kanzi Engine plugin DLL, right-click the `<ProjectName>` project and select Build.
  - To build the Kanzi Engine plugin DLL and your Kanzi application, right-click the <ProjectName>_executable project and select Build.

Visual Studio builds:

  - Plugin DLL in the `<ProjectName>/Application/lib/<PlatformName>/<ConfigurationName>` and the `<ProjectName>/Application/build_vs<Version>/runtime/<ConfigurationName>` directories

Kanzi Studio uses the plugin DLL in the `<ProjectName>/Application/lib` directory.
  - Application executable in the `<ProjectName>/Application/build_vs<Version>/runtime/<ConfigurationName>` directory.

8.

Run your application:

  1.

In Kanzi Studio, select File > Export > Export KZB.

Kanzi Studio exports the project kzb and configuration files to the `<ProjectName>/Application/bin` directory.
  2.

Place these files to the same directory:

    - From the `<ProjectName>/Application/build_vs<Version>/runtime/<ConfigurationName>` the exe and DLL files.
    - From the `<ProjectName>/Application/bin` directory copy the kzb and cfg files.
    - From the `<KanziWorkspace>/Engine/lib/<PlatformName>/<ConfigurationName>` copy all DLL files.

For example, place these files to the `<ProjectName>/Application/bin` directory.
  3.

Run your application by executing the exe file that Visual Studio built.
**Tip:** To build and run your application from Visual Studio:
1.
In Kanzi Studio export the kzb file.
2.
In Visual Studio right-click the <ProjectName>_executable and select Set as StartUp Project.
3.
Select the solution configuration that you want to use and run the application.
