---
title: What is installed with Kanzi?
source: https://docs.kanzi.com/4.1.0/en/installing-kanzi/what-is-installed-with-kanzi.html
---

# What is installed with Kanzi?

Kanzi by default creates:

- Kanzi Studio installation directory at `C:\Program Files\Rightware\Kanzi <KanziVersion>` which contains:

  - Kanzi Studio is installed to `C:\Program Files\Rightware\Kanzi <KanziVersion>\Studio`. The directory contains:

    - `Asset Library` directory contains assets that come with Kanzi, including asset packages, fonts, and materials.
    - `Bin` directory contains Kanzi Studio executable and its dependencies, including:

      - `kanzi_command_prompt.bat`

The Kanzi Command Prompt opens the Windows Command Prompt with the Kanzi environment variables set for the version of Kanzi for which you open a Kanzi Command Prompt.

Use the Kanzi Command Prompt to access Kanzi utilities and build tools, such as Gradle and CMake, without using absolute paths or setting environment variables.

See Using the Kanzi Command Prompt.
      - `PluginInterface.dll` enables you to extend the functionality of Kanzi Studio. See Kanzi Studio plugins.

  - `kanzi-one-software-license-terms.txt` contains the Kanzi One license terms.
  - `third-party-lib-licenses-kanzi-documentation.txt` contains the license information for the third-party libraries used by the Kanzi documentation and tutorials.
  - `third-party-lib-licenses-kanzi-runtime.txt` contains the license information for the third-party libraries used in Kanzi Engine.
  - `third-party-lib-licenses-kanzi-sdk.txt` contains the license information for the third-party libraries used in the Kanzi SDK.
  - `third-party-lib-licenses-kanzi-studio.txt` contains the license information for the third-party libraries used in Kanzi Studio.

- Kanzi workspace directory at `C:\KanziWorkspace_<KanziVersion>` which contains:

  - `Assets` directory contains the RuntimeAssets and kzuiassets Kanzi Studio projects which you can use with Kanzi.
  - `Engine` directory contains Kanzi Engine and the Kanzi Engine binaries:

    - `applications` directory contains the source code for the kzb Player.
    - `cmake` directory contains CMake configuration files for building projects with Kanzi Engine.
    - `configs` directory contains configuration files for building projects with Kanzi Engine.
    - `include` directory contains the Kanzi Engine h and hpp header files.
    - `lib` directory contains Kanzi Engine binary libraries for each platform and CMake configuration files for building projects with Kanzi Engine.
    - `libraries` directory contains third-party libraries required by Kanzi Engine.
    - `scripts` directory contains the scripts for building your Kanzi application for different platforms.

  - `Examples` where Kanzi Studio downloads contains Kanzi example projects that show how some Kanzi features work. See Examples.
  - `Projects` directory is the default location where Kanzi Studio creates projects. See Creating a project.
  - `Templates` directory contains templates you can use as a starting point for programming Kanzi applications. See Creating a project.
  - `Tutorials` where Kanzi Studio downloads contains the projects and assets for the Kanzi tutorials. See Tutorials.

- In the Windows directory for application data that is shared between users Kanzi creates directory `%ProgramData%\Rightware\Kanzi`.
- Paths to build tools in `%ProgramData%\Rightware\<KanziVersion>\kanzi_environment_variables.bat`. Kanzi uses these tools to build applications. See Setting up Android environment for Kanzi Studio.
- Registry entries that associate `.kzproj` and `.kzm` files with Kanzi Studio.
- Registry entries that enables long file path support for Windows and Git, required by the `.kzm` Kanzi Studio project file format.
- When you start Kanzi Studio for the first time Kanzi Studio creates `%AppData%\Rightware\<KanziVersion>\userPreferences.xml` that contains the Kanzi Studio preferences.
- The Kanzi installer saves the Package Manager installer to `%AppData%\Rightware\Kanzi Package Manager` and, if selected, also installs the Package Manager toolchain. See Installing the Package Manager.
- Kanzi Studio stores log messages in the `%USERPROFILE%\AppData\Local\Temp\KanziStudioLogs` directory in these files:

  - `KanziStudio.log` contains messages from Kanzi Studio.
  - `KanziPreview.log` contains messages from the Kanzi Studio Preview. See The Preview log file.
  - `KanziThumbnails.log` contains messages from the process that draws the thumbnails in Kanzi Studio.
  - `KanziStudio_crash<n>.log` contains termination log messages, when Kanzi Studio terminates unexpectedly.
