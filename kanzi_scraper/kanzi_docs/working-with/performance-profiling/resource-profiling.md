---
title: Measuring the loading and deployment time of resources
source: https://docs.kanzi.com/4.1.0/en/working-with/performance-profiling/resource-profiling.html
---

# Measuring the loading and deployment time of resources


In Kanzi resource profiling enables you to measure the amount of time it takes to load and deploy resources and prefabs in your Kanzi application.

In Kanzi, a resource is an item that you can reuse in different parts of your application. For example, a Mesh Data resource defines the geometry of a Model node, and you can use the same Color Brush in different nodes to set the Foreground Brush or Background Brush properties.

Use prefabs (prefabricated templates) to structure your application and to create consistent interfaces. Prefabs allow you to create the building blocks of your application and make the application easier to maintain.

To use resource profiling:

1.

Enable resource profiling in the application configuration. See Enabling resource profiling.
2.

Implement the logging of resource profiling data in the application code, then collect and log the resource profiling data by running your application. See Logging resource profiling data.
3.

To measure the performance of the loading and deployment of resources in your Kanzi application, analyze the resource profiling data. See Analyzing resource profiling data.

## Enabling resource profiling


To start resource profiling you must enable the resource profiling category.

To enable resource profiling in the application configuration, use the ProfilingCategoryFilter setting in either:

- The `application.cfg` file:

```
ProfilingCategoryFilter = "ResourceLoading=on"

```

- The `Application::onConfigure` function:

```
configuration.profilingCategoryFilter = "ResourceLoading=on";

```


To enable or disable resource profiling during application execution, enable or disable the corresponding profiling category:

- To enable resource profiling:

```
kzProfilingCategorySetRuntimeState(KZ_PROFILING_RESOURCE_LOADING_CATEGORY, KZ_PROFILING_ENABLED_CATEGORY)

```

- To disable resource profiling:

```
kzProfilingCategorySetRuntimeState(KZ_PROFILING_RESOURCE_LOADING_CATEGORY, KZ_PROFILING_DISABLED_CATEGORY)

```


After you enable resource profiling, you can collect resource profiling data and write the data to a file. See Logging resource profiling data.
## Logging resource profiling data


To analyze the loading and deployment of resources in your Kanzi application, log the resource profiling data. Before you can log resource profiling data you must enable resource profiling. See Enabling resource profiling.

After you enable resource profiling, Kanzi profiles the loading and deployment of each resource in your application and stores the profiling data in the resource profiler. Implement the logging of the collected profiling data in your application code. Kanzi provides the `ResourceProfilingPtreePopulator` class which you can use to populate a Boost property tree with resource profiling data. You can then log the profiling data in JSON format using the JSON formatter available in Boost.

To log resource profiling data:

1.

In your application code include the header files that are needed to log resource profiling data.

```
// Defines the standard input/output stream objects.
#include <kanzi/core/cpp/iostream.hpp>
// Provides classes that implement string stream input/output operations.
#include <kanzi/core/cpp/sstream.hpp>
// Provides the functionality for populating a Boost property tree with resource profiling data.
#include <kanzi/core.ui/resource/resource_profiling_ptree_populator.hpp>
// Provides the functionality for translating a Boost property tree to JSON and writing it to a file.
#include <boost/property_tree/json_parser.hpp>

```

2.

Add to your application the code that outputs resource profiling data.

For example, to log profiling data to `cout` in the callback `Application::onShutdown` which Kanzi calls on application exit, add this code:

```
void onShutdown() override
{
    // Populate the Boost property tree with resource profiling data.
    ptree resourceProfilingDataTree = ResourceProfilingPtreePopulator::populatePropertyTree(getResourceManager()->getResourceProfiler());
    // Write the property tree to string stream in JSON format.
    stringstream ss;
    boost::property_tree::json_parser::write_json(ss, resourceProfilingDataTree);
    // Boost json_writer considers "/" to be an escape character and adds "\" before each "/".
    // This affects how kzb URLs are displayed.
    // This code outputs json to cout replacing "\/" with "/".
    string str(ss.str());
    string_view strView(str);
    while (!strView.empty())
    {
        size_t backSlashPos = strView.find("\\/");
        if (backSlashPos == string_view::npos)
        {
            cout << strView;
            strView = string_view();
            continue;
        }
        cout << strView.substr(0, backSlashPos);
        strView = strView.substr(backSlashPos + 1);
    }
    cout << "\n";
}

```

3.

Build your application using one of the Profiling build configurations and run your application. You can see the profiling data in the console window when you exit the application.

To build and run your application on Windows:

  1.

In Visual Studio build your application using the Profiling build configuration.
  2.

When you are running the Kanzi Profiling build on Windows, there is no console window. To log resource profiling data, open the command line interface on your computer and run the application so that you redirect the application output to a file where you want to store the resource profiling information:

```
Application\build_vs<Version>\runtime\Profiling\My_application.exe > MyApplicationResourceProfiling.json

```


Kanzi writes to the output file the resource profiling data, which contains:

- Resource profiling contexts for the Kanzi resource manager main thread (`"Resource manager main thread"`) and loading threads (`"Resource manager loader thread N"`). See Resource profiling contexts.
- Resource profiling data samples (`"ResourceProfilingDataSamples"`). See Resource profiling data samples.


```
...
{
    "ThreadContexts": {
        "Resource manager loader thread 1": [
            ...
        ]
        "Resource manager main thread": [
            { resource profiling context of resourceX },
            { resource profiling context of resourceY },
            ...
            { resource profiling context of resourceZ }
        ],
        "Resource manager loader thread 0": [
            ...
            { resource profiling context of resourceY },
            ...
        ],
        "Resource manager loader thread 2": [
            ...
            ...
            { resource profiling context of resourceZ },
            ...
        ]
    },
    "ResourceProfilingDataSamples": [
        ...
        { profiling data sample for resourceX },
        { profiling data sample for resourceY },
        { profiling data sample for resourceZ },
        ...
   ]
}
...

```


For an example of resource profiling data logged for the Scroll view example, see Analyzing resource profiling data.
## Analyzing resource profiling data


After you enable resource profiling and gather the data, analyze the data collected by the resource profiler.

Resource profiling data contains:

- Resource profiling contexts for the Kanzi resource manager main thread (`"Resource manager main thread"`) and loading threads (`"Resource manager loader thread N"`). See Resource profiling contexts.
- Resource profiling data samples (`"ResourceProfilingDataSamples"`). See Resource profiling data samples.


For example, collect and analyze the resource profiling data of the Scroll view example application.

The resource profiling data contains information about:

- Resource acquisition
- Resource loading
- Resource deployment

### Resource acquisition


Usually at application startup Kanzi acquires the `StartupPrefab` prefab template and instantiates it as a Screen node. To optimize the performance of loading resources, after acquiring the startup prefab Kanzi iterates the descendant nodes of the Screen node and collects the URLs of all resources that those nodes use. Kanzi then acquires those resources asynchronously.

For example, in the Scroll view example application the City node uses the City mesh. Because the City node is one of the descendant nodes of the Screen node, Kanzi acquires the City mesh asynchronously.

In the resource profiling data collected for the Scroll view example application, among the `Resource manager main thread` resource profiling contexts you can find the `ResourceAcquire` context of the City mesh. The `AcquireAsynchronously` attribute of the context is set to `true`, showing that Kanzi acquired the City mesh asynchronously as expected.

The parent of the `ResourceAcquire` context is the `AcquireResourcesAsynchronously` context which is a dependency context of the `MainLoop` context. The `MainLoopCounter` attribute of the `MainLoop` context has the value `"0"`, meaning that Kanzi acquired the City mesh resource asynchronously during the first main loop iteration.

The `AcquireResourcesAsynchronously` context has dependency contexts which are related to acquiring other resources used by descendant nodes of the Screen node.

```
"Resource manager main thread":
    {
        "ContextID": "217960184",
        "ContextName": "MainLoop",
        "DependenciesDuration": "359408700",
        "Duration": "389924400",
        "MainLoopCounter": "0",
        "TimeStamp": "200",
        "DependencyContexts": [
            {
            ...
            },
            {
                "ContextID": "217470528",
                "ContextName": "AcquireResourcesAsynchronously",
                "DependenciesDuration": "0",
                "Duration": "329800",
                "TimeStamp": "3697300",
                "DependencyContexts": [
                    ...
                    {
                        "AcquireAsynchronously": "true",
                        "ContextID": "216087856",
                        "ContextName": "ResourceAcquire",
                        "DependenciesDuration": "0",
                        "Duration": "9000",
                        "ResourceUrl": "kzb://scroll_view/Mesh Data/City",
                        "TimeStamp": "3750800"
                    },
                    ...

```

### Resource loading


The Kanzi loading threads load in parallel those resources that are set to be loaded asynchronously. For each asynchronously loaded resource Kanzi creates a loading task and places the task to the loading queue from which the loading threads pick up loading tasks to execute. Whenever a loading thread executes a loading task, the resource profiler creates a `ResourceLoading` context for that loading thread.

The `ResourceLoading` context of the City mesh is one of the resource loading contexts of the `"Resource manager loader thread 1"` thread. In a `ResourceLoading` context:

- `ResourceLoadingDuration` shows in nanoseconds how long it took for the loading thread to load the resource.
- `TimeStamp` shows when the loading of the resource started.
- `LoadedResourceID` is a unique identifier of the loaded resource. You can use the identifier to distinguish between different occasions of loading the same resource again after the application purged the resource.


```
"Resource manager loader thread 1": [
    ...
    {
        "ContextID": "241268536",
        "ContextName": "ResourceLoading",
        "DependenciesDuration": "0",
        "Duration": "1475600",
        "LoadedResourceID": "217505936",
        "LoadedResourceType": "Kanzi.Mesh",
        "LoadedResourceUrl": "kzb://scroll_view/Mesh Data/City",
        "ResourceLoadingDuration": "1473400",
        "TimeStamp": "3764700"
    }
        ...

```


After the loading thread finishes loading the City mesh resource, it places the loading task of the resource to the finishing queue of the resource manager to be further processed by the Kanzi main thread. The Kanzi main thread processes the finishing queue when loading threads place completed tasks to the queue.

When debugging, you can provide your own callbacks for when Kanzi creates a thread and when Kanzi gives a loading task to the thread with `[Domain::setOnThreadCreation` and `ResourceManager::setOnNewLoadingTask`.
### Resource deployment


When the Kanzi main thread processes the loading task of the City mesh resource, the resource profiler creates the `FinishingQueue::processTask` context. In the `FinishingQueue::processTask` context the `Description` attribute shows the task index of the loading task and the number of tasks in the finishing queue. The processing of the loading task includes resource deployment which is the last stage of resource acquisition. The `ResourceDeployment` context is a dependency context of the `FinishingQueue::processTask` context.

```
"Resource manager main thread": [
    {
        "ContextID": "217960184",
        "ContextName": "MainLoop",
        "DependenciesDuration": "359408700",
        "Duration": "389924400",
        "MainLoopCounter": "0",
        "TimeStamp": "200",
        "DependencyContexts": [
                ...
                ]
            },
            ...
            {
                "ContextID": "242014232",
                "ContextName": "FinishingQueue::processTask",
                "DependenciesDuration": "43838400",
                "Description": "Task index 1, queue size 2",
                "Duration": "43914000",
                "TimeStamp": "59703300",
                "DependencyContexts": [
                    {
                        "ContextID": "241265456",
                        "ContextName": "ResourceDeployment",
                        "DependenciesDuration": "43118600",
                        "DeployedResourceID": "217505936",
                        "DeployedResourceType": "Kanzi.Mesh",
                        "DeployedResourceUrl": "kzb://scroll_view/Mesh Data/City",
                        "DeploymentDuration": "719800",
                        "Duration": "43839600",
                        "TimeStamp": "59705500",
                        "DependencyContexts": [
                            ...

```


The City mesh uses a 3D asset and several materials. Kanzi acquires these resources during the deployment of the City mesh. The `ResourceAcquire` contexts of those resources that the City mesh depends on are added to the `ResourceDeployment` context of the City mesh as dependency contexts.

For example, in the dependency tree of the `ResourceDeployment` context of the City mesh you can see that the City mesh uses the Park2 material which in turn uses the Phong material type. In the `ResourceDeployment` context of the City mesh the `DependenciesDuration` attribute shows in nanoseconds how long it took to load and deploy the resources that the City mesh depends on.

```
"ContextID": "241265456",
"ContextName": "ResourceDeployment",
"DependenciesDuration": "43118600",
"DeployedResourceID": "217505936",
"DeployedResourceType": "Kanzi.Mesh",
"DeployedResourceUrl": "kzb://scroll_view/Mesh Data/City",
"DeploymentDuration": "719800",
"Duration": "43839600",
"TimeStamp": "59705500",
"DependencyContexts": [
    {
        "AcquireAsynchronously": "false",
        "ContextID": "216090208",
        "ContextName": "ResourceAcquire",
        "DependenciesDuration": "16896400",
        "Duration": "16919600",
        "ResourceUrl": "kzb://scroll_view/Materials/Park2",
        "TimeStamp": "59706300",
        "DependencyContexts": [
            {
                "ContextID": "241265368",
                "ContextName": "ResourceLoading",
                "DependenciesDuration": "0",
                "Duration": "1200",
                "LoadedResourceID": "241104440",
                "LoadedResourceType": "Kanzi.Material",
                "LoadedResourceUrl": "kzb://scroll_view/Materials/Park2",
                "ResourceLoadingDuration": "200",
                "TimeStamp": "59724500"
            },
            {
                "ContextID": "241265280",
                "ContextName": "ResourceDeployment",
                "DependenciesDuration": "16864100",
                "DeployedResourceID": "241104440",
                "DeployedResourceType": "Kanzi.Material",
                "DeployedResourceUrl": "kzb://scroll_view/Materials/Park2",
                "DeploymentDuration": "32100",
                "Duration": "16897400",
                "TimeStamp": "59726400",
                "DependencyContexts": [
                    {
                        "AcquireAsynchronously": "false",
                        "ContextID": "216092784",
                        "ContextName": "ResourceAcquire",
                        "DependenciesDuration": "16864100",
                        "Duration": "16882700",
                        "ResourceUrl": "kzb://scroll_view/Material Types/Phong",
                        "TimeStamp": "59731500",
                        "DependencyContexts": [
                            {
                                "ContextID": "241267480",
                                "ContextName": "ResourceLoading",
                                "DependenciesDuration": "0",
                                "Duration": "13800",
                                "LoadedResourceID": "241104544",
                                "LoadedResourceType": "Kanzi.ShaderProgram",
                                "LoadedResourceUrl": "kzb://scroll_view/Material Types/Phong",
                                "ResourceLoadingDuration": "13300",
                                "TimeStamp": "59740100"
                            },
                            {
                                "ContextID": "241265192",
                                "ContextName": "ResourceDeployment",
                                "DependenciesDuration": "0",
                                "DeployedResourceID": "241104544",
                                "DeployedResourceType": "Kanzi.ShaderProgram",
                                "DeployedResourceUrl": "kzb://scroll_view/Material Types/Phong",
                                "DeploymentDuration": "16850800",
                                "Duration": "16853300",
                                "TimeStamp": "59754300"
                            }
                        ]
                    }
                ]
            }
        ]
    },

```
