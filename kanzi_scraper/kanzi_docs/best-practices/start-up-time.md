---
title: Optimizing the startup time of your application
source: https://docs.kanzi.com/4.1.0/en/best-practices/start-up-time.html
---

# Optimizing the startup time of your application


To optimize the startup time of your Kanzi application:

- For images in your applications use raw and compressed formats, instead of .png and .jpg formats. When you use raw and compressed formats Kanzi needs to process less data before it sends it to the GPU. See Images and textures best practices.
- Use the parallel resource loading to load and process the resources from your application in multiple threads and deploy the resources to the GPU over multiple frames. See Loading resources in parallel.
- Load first a kzb file which contains the smallest amount of content you can show at application startup, such as a loading screen. Then start loading the kzb files which contain the rest of your application. See Combining Kanzi Studio projects into a Kanzi application.
- Reorganize the node tree of your application in Kanzi Studio. Kanzi loads the resources when it needs them. Reorganize the node tree to postpone the loading of resources until less important parts of the node tree become visible. Doing so the application can skip those resources and start faster.
- Design your application to support gradual loading. For example, show the loading screen while you load the base UI, and once the base UI is loaded and operational, preload the application resources for the other parts of the UI. See Loading node prefab resources asynchronously.
- For your Kanzi Android framework (droidfw) application, use the `DeploymentQueueBudget` configuration setting to control the amount of time that Kanzi spends each frame to deploy resources. This setting can have a large effect on the startup time. See DeploymentQueueBudget.
