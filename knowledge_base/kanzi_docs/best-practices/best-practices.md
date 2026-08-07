---
title: Best practices
source: https://docs.kanzi.com/4.1.0/en/best-practices/best-practices.html
---

# Best practices

When creating applications for embedded and mobile devices, even seemingly small details can have significant impact on the performance of your Kanzi application on target devices. Kanzi graphics pipeline is optimized to allow 60 frames per second for 3D instrument clusters and human-machine interfaces. Use the best practices covered in this section of documentation to create optimal Kanzi applications for your target hardware.

Even though Kanzi provides many ways that enable you to create applications that consume less memory, CPU and GPU capacity, and device battery, how you create your application has a large impact on its efficiency.
## Thread safety

Kanzi is thread-agnostic and does not guarantee thread safety. To make your Kanzi application code thread-safe:

- Do not call Kanzi functions from custom threads unless the API documentation specifies that you can call the function from any thread.
- Synchronize between threads all access to shared data.

## Pay attention to the log messages

Kanzi prints warnings and errors to the Kanzi Studio Log window and the Kanzi debug console to help you find the problems and bottlenecks in your Kanzi application. Pay careful attention to these messages. To ensure that your Kanzi application works correctly and performs optimally on your target platform, resolve all the issues shown in the warnings and errors. Even seemingly unimportant warnings can have a significant impact on the loading times and performance of your Kanzi application. For example, see Adjusting the data size.
## Use the Kanzi Command Prompt

The Kanzi Command Prompt opens the Windows Command Prompt with the Kanzi environment variables set for the version of Kanzi for which you open a Kanzi Command Prompt.

Use the Kanzi Command Prompt to access Kanzi utilities and build tools, such as Gradle and CMake, without using absolute paths or setting environment variables.

See Using the Kanzi Command Prompt.
## Kanzi best practices

Here you can find the information about best practices when working with Kanzi.  [](start-up-time.html)

Performance   [](animations/animations-best-practices.html)

Animations   [](images-and-textures/images-and-textures-best-practices.html)

Images   [](meshes/meshes-best-practices.html)

Meshes   [](rendering/rendering-best-practices.html)

Rendering   [](shaders/shaders-best-practices.html)

Shaders   [](using-kanzi-command-prompt.html)

Kanzi Command Prompt   [](../working-with/projects/cleaning-up-a-project.html)

Cleaning projects
