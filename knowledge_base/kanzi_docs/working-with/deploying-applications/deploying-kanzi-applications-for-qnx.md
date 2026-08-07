---
title: Deploying Kanzi applications to QNX
source: https://docs.kanzi.com/4.1.0/en/working-with/deploying-applications/deploying-kanzi-applications-for-qnx.html
---

# Deploying Kanzi applications to QNX

Before you can build a Kanzi application for your target platforms, set up and configure the Kanzi build environment for your target platforms. The build environment includes tools that the Kanzi build system uses to build your application for your target platforms.
## Requirements

To build and deploy Kanzi applications to QNX, you need:

- QNX software development platform 7.1.

Library requirements from the QNX software development platform:

  - slog2

You can get the QNX development tools at [https://blackberry.qnx.com](https://blackberry.qnx.com/).
- For Cmake-based platform package: CMake 3.25 and Ninja 1.10.x

Before deploying your Kanzi application to your QNX target device, make sure that device is running the QNX Screen service. See https://www.qnx.com/developers/docs/7.1/#com.qnx.doc.screen/topic/manual/cscreen_about.html.
## Supported build systems, STDLIB implementation, and library linking

Kanzi platform packages support these build systems:

- CMake. Note that this platform package contains `-cmake` in its name.

The platform package contains the `Engine/cmake/toolchains/<toolchain_file>.cmake` file that lists the CMake options used to create it.

Kanzi offers QNX platform packages that are based on these STDLIB implementations:

- LLVM. Platform packages explicitly mention `cxx` in the name of the platform package archive.
- GNU. Platform packages explicitly mention `gpp` in the name of the platform package archive.

Kanzi platform packages support these library linking options:

- Static.

To build an application with statically linked libraries, use the CMake define `-DBUILD_SHARED_LIBS:BOOL=OFF`. This is the default if `BUILD_SHARED_LIBS` option is not specified.
- Dynamic.

To build an application with dynamically linked libraries, use the CMake define `-DBUILD_SHARED_LIBS:BOOL=ON`

On QNX with the LLVM C++ library, when you use in your Kanzi application a kzb file with a plugin dependency, do not use the runtime linker. Link the plugin SO to the application when you build the application executable. See https://www.qnx.com/developers/docs/7.1/#com.qnx.doc.neutrino.sys_arch/topic/dll.html and https://www.qnx.com/developers/docs/7.1/#com.qnx.doc.neutrino.utilities/topic/q/qcc.html.
## Building Kanzi applications for QNX

### Building Kanzi applications using CMake

For example, to build the kzb_player application on Linux for QNX 7.1 using CMake:

- With the LLVM STDLIB implementation, from a -cxx platform package, with the shared library linking:

```
cd Engine/applications/kzb_player
mkdir build
cd build
cmake -GNinja
      -DCMAKE_BUILD_TYPE=Release
      -DCMAKE_TOOLCHAIN_FILE=../../cmake/toolchains/qnx710-aarch64-cxx-qnx_screen.cmake
      -DCMAKE_INSTALL_PREFIX=../bin
      -DKANZI_BUILD_SHARED_LIBS:BOOL=ON
      -DKanzi_DIR=../../lib/cmake/Kanzi
      -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON ..
cmake --build .
cmake --install .

```

- With the GNU STDLIB implementation, from a Non-cxx platform package:

```
cd Engine/applications/kzb_player
mkdir build
cd build
cmake -GNinja
      -DCMAKE_BUILD_TYPE=Release
      -DCMAKE_TOOLCHAIN_FILE=../../cmake/toolchains/qnx710-aarch64-gpp-qnx_screen.cmake
      -DCMAKE_INSTALL_PREFIX=../bin
      -DKanzi_DIR=../../lib/cmake/Kanzi
      -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON ..
cmake --build .
cmake --install .

```

## Deploying Kanzi applications to a QNX device

To deploy Kanzi applications to QNX:

1.

Build your Kanzi application for QNX. See Building Kanzi applications for QNX.
2.

Connect your QNX device to your computer.
3.

From the `<ProjectName>/Application/bin` directory copy to your QNX target device:

  - Kanzi application exe file
  - kzb files that your Kanzi application uses
  - `application.cfg` file which contains a list of all the kzb files your Kanzi application uses

4.

On your QNX target device open the command line and add execution rights for your Kanzi application on that device:

```
// Adds execution rights on the QNX target device
// for the Kanzi application called MyApplication.
chmod 755 MyApplication

```

5.

On the command line start the application on your QNX target device:

```
// Starts the Kanzi application called MyApplication.
./MyApplication

```

## Printing Screen display information

You can list QNX Screen display information for your Kanzi application.

To print Screen display information:

1.

Deploy your Kanzi application to QNX. See Deploying Kanzi applications to a QNX device.
2.

Run the application with the `-enum-qnx-displays` command-line argument:

```
./MyApplication -enum-qnx-displays

```

The application prints for each display this information and exits:

- Display ID
- Whether the display is attached
- Whether the display is detachable
- Whether the display is focused
- Current resolution of the display
- (Optional) If you run the application as root:

  - All available video modes
  - Current video mode

## Setting QNX Screen usage flags

You can programmatically set the usage flags for the QNX Screen property. Screen usage flags are properties that you can use to constrain the allocated QNX window buffers. See QnxUsageFlags.
## Known issues on QNX

- When you run multiple Kanzi applications and receive an error like this

```
error:generic:/home/admin/ws/0/ui/Engine/source/core.ui/platform/windowing/qnx_screen/kzs_window_native.cpp:179> Unable to retrieve window size

Process 1482838 (ClusterApp) terminated SIGSEGV code=1 fltno=11 ip=000000121378c348(/var/data/j01/bin/kanzi/./ClusterApp@_ZNSt7__cxx1115basic_stringbufIcSt11char_traitsIcESaIcEED0Ev+0x0000000000007d78) mapaddr=00000000004d4348. ref=0000000000000010

```

In each Kanzi application, you must set the `NativeWindowProperties::groupName` to a unique name. See GroupName.
- QNX deprecated the use of QCC as CXX compiler. The compilation of a QNX application fails with the error

```
QCC is not a full path and was not found in the PATH.

```

When you compile a QNX application for Kanzi versions before 3.9.4, in build configuration files replace the deprecated QCC compiler command with the q++ command.

  - For CMake, edit `Engine/cmake/toolchains/qnx7*.cmake` to replace

```
set(CMAKE_CXX_COMPILER QCC)

```

with

```
set(CMAKE_CXX_COMPILER q++)

```

  - For SCons, edit:

    - `Engine/configs/platforms/qnx/config.py` to replace

```
default.env["CC"] = os.path.join(toolchain_bin, "QCC")
default.env["CXX"] = os.path.join(toolchain_bin, "QCC")

```

with

```
default.env["CC"] = os.path.join(toolchain_bin, "q++")
default.env["CXX"] = os.path.join(toolchain_bin, "q++")

```

    - `Engine/scripts/build.py` to replace

```
re.compile(r'^([^/]*/)*QCC$'),

```

with

```
re.compile(r'^([^/]*/)*q\+\+$'),

```
