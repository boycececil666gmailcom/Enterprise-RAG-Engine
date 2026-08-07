---
title: Deploying Kanzi applications to Linux
source: https://docs.kanzi.com/4.1.0/en/working-with/deploying-applications/deploying-your-application-to-linux.html
---

# Deploying Kanzi applications to Linux

Before you can build a Kanzi application for your target platforms, set up and configure the Kanzi build environment for your target platforms. The build environment includes tools that the Kanzi build system uses to build your application for your target platforms.

The most convenient way to build Kanzi applications for Linux is to do the building on Linux. If you have the Linux toolchain for Windows, you can build Kanzi applications for Linux on Windows. In that case point the Kanzi build scripts to that toolchain.

You can configure the input event devices that Kanzi listens to on Linux ports where the native windowing system does not provide input device handling.

See Input event devices on Linux.
## Supported build systems and library linking

Kanzi platform packages support these build systems:

- CMake. Note that this platform package contains `-cmake` in its name.

The platform package contains the `Engine/cmake/toolchains/<toolchain_file>.cmake` file that lists the CMake options used to create it.

Kanzi platform packages support these library linking options:

- Static.

To build an application with statically linked libraries, use the CMake define `-DBUILD_SHARED_LIBS:BOOL=OFF`. This is the default if `BUILD_SHARED_LIBS` option is not specified.
- Dynamic.

To build an application with dynamically linked libraries, use the CMake define `-DBUILD_SHARED_LIBS:BOOL=ON`

## Building Kanzi applications for Linux

### Building Kanzi applications using CMake

For example, to build the kzb_player application for Linux using CMake:

- Using x86_64 Wayland platform package, with the shared library linking:

```
cd Engine/applications/kzb_player
mkdir build
cd build
cmake -GNinja
      -DCMAKE_BUILD_TYPE=Release
      -DCMAKE_TOOLCHAIN_FILE=../../cmake/toolchains/linux-x86_64-wayland_egl.cmake
      -DCMAKE_INSTALL_PREFIX=../bin
      -DKANZI_BUILD_SHARED_LIBS:BOOL=ON
      -DKanzi_DIR=../../lib/cmake/Kanzi
      -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON ..
cmake --build .
cmake --install .

```
