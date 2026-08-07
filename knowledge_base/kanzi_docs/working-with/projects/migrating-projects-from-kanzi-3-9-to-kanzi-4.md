---
title: Migrating projects from Kanzi 3.9 to Kanzi 4
source: https://docs.kanzi.com/4.1.0/en/working-with/projects/migrating-projects-from-kanzi-3-9-to-kanzi-4.html
---

# Migrating projects from Kanzi 3.9 to Kanzi 4


The project and plugin templates changed substantially between Kanzi 3.9 and Kanzi 4. Kanzi 4 Kanzi Studio can open and convert a Kanzi 3.9 Kanzi Studio project, but the surrounding build structure (CMake files, build scripts, platform configurations, plugin build setup) and the default materials and shaders do not migrate automatically. This guide explains how to move a Kanzi 3.9 application or plugin onto the Kanzi 4 template structure.

This guide covers the **project and build structure**. For the source-code and API changes you must also apply, see the Kanzi 4.0.0 migration guide and the Kanzi 4.1.0 migration guide.
## Before you start


**Back up your 3.9 project, or keep it in version control.** Converting a Kanzi 3.9 project to Kanzi 4 is **in-place and irreversible**: when you open a 3.9 `<ProjectName>.kzproj` in Kanzi 4 Kanzi Studio and save, Kanzi Studio rewrites the entire project â including every resource file â to the Kanzi 4 `<ProjectName>.proj.kzm` format, and cannot convert it back. Always migrate a copy and keep the original 3.9 project intact.
## Read this first: removed functionality


Kanzi 4 removes some functionality that Kanzi 3.9 projects can depend on. If your project depends on any of the following, plan a different upgrade strategy before you start, because this guide does not restore them:
|

Removed in Kanzi 4 |

Notes |
|

Visual Studio 2017 and 2019 solution generators |

The `generate_cmake_vs2017_solution.bat` and `generate_cmake_vs2019_solution.bat` scripts are gone. Kanzi 4 supports Visual Studio 2022 only, through `generate_cmake_vs2022_solution.bat`. |
|

The Linux `linux_x11_glx_cpp98` platform |

The pre-C++11 Linux platform and its `SConstruct` file are removed. Kanzi 4 requires a C++17 toolchain. |
|

SCons build helpers |

The `configs/platforms/common/config.py` and `start_build.py` scripts are removed. All platforms build with CMake. |

Kanzi 4 also raises the minimum required CMake version from 3.10 to 3.25.
## Choosing your path


For most projects, **migrate your project**: open and convert it in Kanzi 4 Kanzi Studio, then transplant the Kanzi 4 build structure and default resources. See Migrate your project.

If your project is small or a throwaway prototype, **start fresh**: create a new Kanzi 4 project and bring your content into it. See Start fresh and rebuild.

When starting fresh you must rebuild the application structure by hand â node-tree hierarchy, prefab placement, cross-prefab bindings, and render/composition setup â on top of migrating your resources.
## What changes between Kanzi 3.9 and Kanzi 4


Whichever path you take, these change between Kanzi 3.9 and Kanzi 4:

- **Project file format.** The 3.9 root project file is `<ProjectName>.kzproj`; the Kanzi 4 file is `<ProjectName>.proj.kzm`. Kanzi 4 Kanzi Studio converts the older project when you open it (it asks you to confirm), then writes the new format when you save. The conversion is irreversible (see Before you start).
- **Build system.** Kanzi 4 adds command-line build wrappers (`build.bat` / `build.sh`) and a resolver concept: the `cmake/kanzi-bootstrap.cmake` dispatcher selects between the classic `cmake` resolver (a local Kanzi SDK, the default, closest to Kanzi 3.9) and the `kpm` resolver (Kanzi Package Manager) through the `KANZI_RESOLVER` CMake cache variable.
|

Command |

What it does |
|

`build.bat` |

Builds with the `cmake` resolver in the Release configuration. |
|

`build.bat <config>` |

Builds with the `cmake` resolver in a specific configuration (`Debug`, `Release`, `Profiling`). |
|

`build.bat kpm` |

Builds with the `kpm` resolver. |

Replace `build.bat` with `./build.sh` on Linux and macOS. The classic resolver locates a local SDK with the `KANZI_HOME` environment variable, exactly as in Kanzi 3.9. If you passed `-DKANZI_ROOT=<path>` on the command line, rename it to `-DKanzi_ROOT=<path>`.

`generate_cmake_vs2022_solution.bat` generates the Visual Studio 2022 solution; on macOS, `generate_cmake_xcode_ios_project.sh` generates an Xcode project for iOS (a new Kanzi 4 platform).
- **Plugin.** Rebuild your Kanzi Engine plugin with Visual Studio 2022 against the Kanzi 4 SDK and re-import it. See Migrating a Kanzi Engine plugin.
- **Default materials and shaders.** Kanzi 4 reworked the graphics system and updated the default material types and shaders to new GLSL. A converted 3.9 project keeps its old shaders, which Kanzi 4 rejects. See Migrating materials and shaders.
- **Exported binaries.** You re-export the `.kzb` in Kanzi 4. Do not reuse a Kanzi 3.9 `.kzb`.

## Migrate your project


1.

**Convert a copy of your 3.9 project.** In Kanzi 4 Kanzi Studio, select File > Open Project, open the copyâs `<ProjectName>.kzproj`, confirm the conversion prompt, and save. Kanzi Studio writes the Kanzi 4 `<ProjectName>.proj.kzm`.
2.

**Create a donor project to copy from.** In Kanzi 4 Kanzi Studio, create a new project from the template that matches your project (for example **Application with Kanzi Engine plugin**), with materials that match your project (for example **High-performance vertex shaders**). See Creating a project. Use the same project name to avoid renaming files later. This project is the donor: the source of the Kanzi 4 build files and default resources you copy in the next steps.
3.

**Swap in the build scaffolding:**

  1.

Overwrite the donorâs `.cpp` and `.hpp` files under `Application/src` with ones from the converted project.
  2.

Delete the converted projectâs `Application` folder.
  3.

Copy the donorâs `Application` into the converted project.

4.

**Rebuild and import your plugin.** Follow Migrating a Kanzi Engine plugin.
5.

**Replace the default materials and shaders.** Keep your custom materials, but delete the converted projectâs default Materials, Material Types, and Shaders. Replace them with the ones in the donor project.
6.

**Finish.** Fix any custom material or shader that fails to build (see Migrating materials and shaders), apply the C++ API changes (see the 4.0.0 and 4.1.0 migration guides), then build and re-export the `.kzb`.

## Start fresh and rebuild


1.

**Create a new project** from the template that matches your project (for example **Application with Kanzi Engine plugin**), with materials that match your project (for example **High-performance vertex shaders**). See Creating a project. This project has Kanzi 4âs build files and default resources.
2.

**Bring in and import your plugin.** Copy your plugin source files (`.cpp` and `.hpp`) into the new projectâs `src/plugin/src` directory, then follow Migrating a Kanzi Engine plugin.
3.

**Bring your authored content** into the `Tool_project` of the new project: your scenes and prefabs, imported assets (3D assets and their mesh data, images, fonts), and any materials and shaders you created. **Keep the new projectâs default Materials, Material Types, and Shaders** â do not copy the 3.9 defaults over them. See Sharing project items and Combining Kanzi Studio projects into a Kanzi application.

> **Note:** When you import a 3D asset, Kanzi Studio populates the 3D Assets and the mesh-data directories. If the mesh data does not come across, the mesh does not rebuild.
> 4.
>
> **Rebuild your node tree.** Reassemble your applicationâs hierarchy under Screen from your imported prefabs and content.
> 5.
>
> **Finish.** Fix any custom material or shader that fails to build (see Migrating materials and shaders), apply the C++ API changes (see the 4.0.0 and 4.1.0 migration guides), then build and re-export the `.kzb`.
>
## Migrating a Kanzi Engine plugin


1.

**List your source files.** Ensure all source files are listed in the `set` command of the matching `CMakeLists.txt` (`src/plugin` or `src/executable`).
2.

Build the plugin with Visual Studio 2022 against the Kanzi 4 SDK: set `KANZI_HOME` to your Kanzi 4 SDK, then run `build.bat` or `generate_cmake_vs2022_solution.bat`. If you previously built against a different SDK, delete the build directory first.
3.

Register the rebuilt plugin in Library > Kanzi Engine Plugins: delete the existing plugin entry, then right-click Kanzi Engine Plugins > Import Kanzi Engine Plugin and select the rebuilt DLL.
4.

Set the Preview Build Configuration (in Project > Properties) to the configuration you built the plugin for.


Port your plugin manually if your plugin uses Kanzi Engine APIs that changed in Kanzi 4 â primarily rendering, graphics, and platform. See: Kanzi 4.0.0 migration guide and Kanzi 4.1.0 migration guide.
## Migrating materials and shaders


Kanzi 4 reworked the graphics system and updated the default material types and shaders to new GLSL. A converted Kanzi 3.9 project still carries its old default materials and shaders, which use legacy GLSL that Kanzi 4 rejects, so you replace them with Kanzi 4âs.

- **Use the new default materials and shaders, never the 3.9 ones.**
- **Migrate shaders you wrote yourself** to Kanzi 4 GLSL. See the shader-migration steps in the Kanzi 4.1.0 migration guide and Setting the OpenGL ES version.
- **Fix any custom material or shader that fails to build.** Migrate its shader to Kanzi 4 GLSL as above, or re-create the material on a Kanzi 4 default material type. Because materials are shared, you fix this per material, not per node.

## Troubleshooting


- **Materials fail to acquire, or shader compilation errors such as** `ES shaders for SPIR-V require version 310 or higher`. You are still using 3.9 default shaders. Replace them with Kanzi 4âs (or migrate the GLSL).
- **Preview reports an undefined metaclass, or the plugin does not load.** The plugin DLLâs build configuration does not match the Preview Build Configuration, or `KANZI_HOME` pointed at the wrong SDK when you built it. Rebuild against the correct SDK and re-import, and align the Preview Build Configuration.
- **Font-engine warnings, an empty Font Engine list (only âNoneâ), or âPreview cannot startâ / âcannot find a font engineâ.** These are downstream symptoms of the engine not initializing â usually because the materials and shaders fail to build, or the Preview Build Configuration does not match your rebuilt plugin. Fix those first. Once the engine initializes, the warnings clear and the Font Engine list populates with the available engines (FreeType, iType) on its own; you do not select a font engine manually to resolve this.

## Per-template notes

### Basic application


The single source file (for example, `src/basic_application.cpp`) carries over. There is no plugin subtree.
### Kanzi Engine plugin and data source plugin


The plugin subtree under `src/plugin` is self-contained in Kanzi 4: it has its own `cmake/` directory and `packages.json`. Plugin deployment uses the `create_and_deploy_plugin` scripts in the `Application` directory. Follow Migrating a Kanzi Engine plugin.
### Android changes


Kanzi 4 uses Android Gradle Plugin 8 and moves dependency versions to `configs/platforms/android_gradle/gradle/libs.versions.toml`. The native build now lives in a `kanzinative` Gradle module, and the per-plugin Gradle module that Kanzi 3.9 generated for plugin templates is removed. Kanzi 4 also requires NDK 28.2.13676358 and CMake 3.25 or newer; set the Gradle CMake version to 3.30.5, the lowest version the Android SDK provides. Re-apply your Kanzi 3.9 Gradle customizations against this layout rather than copying your old Gradle files. See the Kanzi 4.1.0 migration guide.
