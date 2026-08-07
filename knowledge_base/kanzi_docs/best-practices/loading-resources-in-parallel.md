---
title: Loading resources in parallel
source: https://docs.kanzi.com/4.1.0/en/best-practices/loading-resources-in-parallel.html
---

# Loading resources in parallel


When users run your Kanzi application in an environment with a multi-core processor, Kanzi automatically uses multiple CPU cores to load the GPU resources in the kzb files to RAM.

Because the largest amount of data during the loading is processed by the GPU resources, parallel loading of resources significantly improves the loading time of your application.

GPU resources Kanzi loads in parallel include all types of textures, shaders, and meshes. To deploy these resources from RAM to GPU memory and to load prefab templates, Kanzi always uses the main thread. See Images and textures best practices, Shaders best practices, Meshes best practices.

In Kanzi, you can load resource dictionaries of prefabs you use in your project before your Kanzi application shows them to users. For example, you can create a loading screen that your users see while Kanzi is loading the resource dictionaries of the rest of your application in the background.

See Loading node prefab resources asynchronously.

The optimal number of loading threads differs between platforms. When you use the optimal number of loading threads for your platform you can expect a decrease in both the launch and full loading times of your Kanzi application.
## Setting the number of cores used for loading


In the application code, either using the application framework configuration or the resource manager API, you can set the number of cores you want your application to use to load the GPU resources.

To set the number of cores your application uses for loading the resources, in the application code in the `Application::onConfigure` function:

```
// Set loadingThreadCount to the number of cores in the processor
// of your target device.
// For example, to use all four cores of a four-core processor,
// set the value to 3, to use only two cores, set the value to 1.
configuration.loadingThreadCount = 3;

```


You can set the loading preferences for your application in the application code in the `Application::onConfigure` function or in the `application.cfg`. See LoadingThreadCount.
## Disabling parallel loading


To disable the parallel loading of resources, set `ApplicationProperties::loadingThreadCount` to 0. When you disable the parallel loading, Kanzi uses only the main thread to load the resources. When you disable the parallel loading, Kanzi does not allocate the memory manager.

```
configuration.loadingThreadCount = 0;

```


See LoadingThreadCount.
