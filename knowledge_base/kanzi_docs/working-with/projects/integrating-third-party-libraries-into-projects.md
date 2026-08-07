---
title: Integrating third-party libraries into Kanzi projects
source: https://docs.kanzi.com/4.1.0/en/working-with/projects/integrating-third-party-libraries-into-projects.html
---

# Integrating third-party libraries into Kanzi projects


To extend the functionality of Kanzi you can integrate third-party libraries, such as physics simulation library, into your Kanzi projects. You can find the third-party libraries in the following locations:

- Common header and source files are located in `<KanziWorkspace>/Engine/libraries/common/<LibraryName>/include`.
- Platform-specific header files are located in `<KanziWorkspace>/Engine/libraries/platforms/<PlatformName>/<LibraryName>/include`.
- Platform-specific binary files are located in `<KanziWorkspace>/Engine/libraries/platforms/<PlatformName>/<LibraryName>/lib`.

## Integrating a third-party library into a Kanzi project


To integrate a third-party library into a Kanzi project, add the reference to the third-party library in the CMake project build configuration file located at `<ProjectName>/Application/CMakeLists.txt`:

```
m.env["LIBS"] += ["<LibraryName>"]
m.env["LIBPATH"] += ["</path/to/the/library/location>"]

```


For instructions on how to build the third-party library for the target platform of your Kanzi project, see the documentation of the library you want to include.
