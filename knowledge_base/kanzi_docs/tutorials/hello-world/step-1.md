---
title: Step 1 - Create project with C++ application and print to debug console
source: https://docs.kanzi.com/4.1.0/en/tutorials/hello-world/step-1.html
---

# Step 1 - Create project with C++ application and print to debug console


In this step, you first create a Kanzi Studio project with a C++ application. You then add the code to the C++ application to print Hello world! to the Kanzi debug console.
## Get the tutorial


To get the tutorial, in the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Hello world tutorial, click .

Kanzi Studio downloads the tutorial to the `<KanziWorkspace>/Tutorials` directory. You can find the completed tutorial in the `<KanziWorkspace>/Tutorials/Hello world/Completed` directory.
## Create a project with C++ application and print to debug console


To create a project with a C++ application and print to the Kanzi debug console:

1.

In the Kanzi Studio Quick Start window, click New:

  1.

Select the Application item from the list of available project templates.
  2.

Choose the name and location for your project.

For example, name your project Hello world.


Click Create.

Kanzi creates a Kanzi Studio project in the `<ProjectName>/Tool_project` directory and the structure for the application code of your project in the `<ProjectName>/Application` directory:

  - `bin` directory contains the kzb and configuration files of your project.
  - `configs` directory contains the configuration files for different platforms. By default, Kanzi creates configuration files for several different platforms. The recommended platform for developing Kanzi applications is Microsoft Visual Studio. See Deploying Kanzi applications.
  - `src` directory contains the source code for your application.
  - `CMakeLists.txt` file contains the instructions for CMake to generate the Visual Studio solution for the Kanzi application.
  - `generate_cmake_vs<Version>_solution.bat` is a script that you can use to generate a Visual Studio solution for the Kanzi application. The script generates the Visual Studio solution in the `<ProjectName>/Application/build_vs<Version>` directory.

2.

In Kanzi Studio, select File > Export > Export KZB.

Kanzi Studio creates the kzb file and configuration files from your Kanzi Studio project. Kanzi Studio stores the exported files in the `<ProjectName>/Application/bin` directory or the location that you set in Project > Properties in the Binary Export Directory property. The kzb file contains all nodes and resources from your Kanzi Studio project, except the resources that you mark in a localization table as locale packs.

When you run your Kanzi application from Visual Studio, your application loads the kzb file and configuration files.
3.

In Kanzi Studio, select File > Open Kanzi Command Prompt.

The Kanzi Command Prompt opens the Windows Command Prompt with the Kanzi environment variables set for the version of Kanzi for which you open a Kanzi Command Prompt.

Use the Kanzi Command Prompt to access Kanzi utilities and build tools, such as Gradle and CMake, without using absolute paths or setting environment variables.

> **Tip:** You can find the Kanzi Command Prompt in the Windows Start Menu in the Rightware directory.
>
> When you have more than one version of Kanzi installed, make sure that you launch a Kanzi Command Prompt for the version of Kanzi with which you want to work in that command prompt.
> 4.
>
> In the Kanzi Command Prompt in the `<ProjectName>/Application` directory, run the script that generates a Visual Studio solution for the application.
>
> ```
> generate_cmake_vs2022_solution.bat
>
> ```


This script generates a Visual Studio solution for the application in the directory `<ProjectName>/Application/build_vs2022`.
5.

In Visual Studio, open the `Application/build_vs<Version>/<ProjectName>.sln` Visual Studio solution.

For example, if you named your Kanzi Studio project Hello world, the Visual Studio solution is called `Hello_world.sln`.
6.

In the Solution Explorer, right-click the Hello_world project and select Set as StartUp Project.
7.

Open the `hello_world.cpp` file.

By default, the template adds the `kanzi.hpp` header file, which includes other Kanzi headers, and the Code Behind identifier. In this tutorial, you do not use Code Behind.

This application class uses the `ExampleApplication` class, which simplifies application development by handling the registration of the required modules.

```
#include <kanzi/kanzi.hpp>

// [CodeBehind libs inclusion]. Do not remove this identifier.

#if defined(HELLO_WORLD_CODE_BEHIND_API) && !defined(ANDROID) && !defined(KANZI_CORE_API_IMPORT)
#include <Hello_world_code_behind_module.hpp>
#endif

using namespace kanzi;

class HelloWorld : public ExampleApplication

```

8.

To use the logger to print to the Kanzi debug console, include the `log.hpp` header file:

```
#include <kanzi/core/log/log.hpp>

```

9.

Replace the content of the `Application::onProjectLoaded` with the code below.

When you place a function inside the `Application::onProjectLoaded` Kanzi calls that function after it loads your application.

```
void onProjectLoaded() override
{
    // Prints Hello world! to the Kanzi debug console.
    kzLogInfo(KZ_LOG_CATEGORY_GENERIC, ("Hello world!"));
}

```

10.

Select the solution configuration that you want to use and run your application.

During development, select the Debug configuration. When you are ready to create a version for production, select the Release configuration.

The `log.hpp::kzLogInfo` function prints **Hello world!** to the Kanzi debug console.

When you run the application in the debug mode, Kanzi shows the debug console. By default, a Kanzi Studio project contains an empty scene.


This is what your `hello_world.cpp` looks like when you complete this step.

```
#include <kanzi/kanzi.hpp>
#include <kanzi/core/log/log.hpp>

// [CodeBehind libs inclusion]. Do not remove this identifier.

#if defined(HELLO_WORLD_CODE_BEHIND_API) && !defined(ANDROID) && !defined(KANZI_CORE_API_IMPORT)
#include <Hello_world_code_behind_module.hpp>
#endif

using namespace kanzi;

class HelloWorld : public ExampleApplication
{
public:

   void onConfigure(ApplicationProperties& configuration) override
   {
      configuration.binaryName = "hello_world.kzb.cfg";
   }

   void onProjectLoaded() override
   {
      // Prints Hello world! to the Kanzi debug console.
      kzLogInfo(KZ_LOG_CATEGORY_GENERIC, ("Hello world!"));
   }

   void registerMetadataOverride(ObjectFactory& factory) override
   {
      ExampleApplication::registerMetadataOverride(factory);

#if defined(HELLO_WORLD_CODE_BEHIND_API) && !defined(ANDROID) && !defined(KANZI_CORE_API_IMPORT)
      HelloWorldCodeBehindModule::registerModule(getDomain());
#endif

      // [CodeBehind module inclusion]. Do not remove this identifier.
   }
};

Application* createApplication()
{
   return new HelloWorld;
}

```


Introduction Next step
