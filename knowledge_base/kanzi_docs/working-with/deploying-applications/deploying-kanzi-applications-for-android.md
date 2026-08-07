---
title: Deploying Kanzi applications to Android
source: https://docs.kanzi.com/4.1.0/en/working-with/deploying-applications/deploying-kanzi-applications-for-android.html
---

# Deploying Kanzi applications to Android

## Building and deploying Kanzi applications from Kanzi Studio


In Kanzi Studio, you can build and deploy your Kanzi application to an Android device using a single command. This approach is useful when you want to see how your application works and looks on an Android device while you are still prototyping or developing your application.

The first time you build and deploy an Android package, you need to have a working Internet connection because the build process downloads and installs the Android build tools, SDKs, and library dependencies.

When you build and deploy a Kanzi application created with the Kanzi Studio project template, Kanzi exports the Android package to the `<KanziWorkspace>/Temp` directory. See Creating a project.

To build and deploy Kanzi applications from Kanzi Studio:

1.

Connect your Android device to your computer.
2.

In Kanzi Studio, create or open the project for your Kanzi application and select File > Export > Build Android Package.

Kanzi Studio builds the application source code, creates the .apk package, and installs the package to your Android device.

### Configuring Android builds


You can configure the building of your Kanzi applications for Android using the application configurations in Kanzi Studio. For example, you can set the target architecture, and whether Kanzi should deploy the built package to the attached target device. You can set which application configuration you want to use when you select File > Export > Build Android Package in Project > Properties in the Default Build Configuration property.

1.

In Kanzi Studio, in the Library, press Alt and right-click Build Configurations and select Android Build Configuration.
2.

In the Properties, set the configuration for the Android build.

For example:

  - Set the Build Profile property to Debug to build using the debug build type, instead of the default Release build.
  - Disable the Install to Device property if you want to manually install the .apk package to your Android device.


## Building and deploying Kanzi applications from Android Studio


To build and deploy Kanzi applications from Android Studio:

1.

In Kanzi Studio, create or open a Kanzi Studio project that is based on one of the Android application Kanzi Studio project templates. See Creating an Android application in Kanzi Studio.
2.

In the Kanzi Studio main menu, select File > Open Android Project in Android Studio.

Kanzi Studio opens in Android Studio the Android project from the `<ProjectName>/Application/configs/platforms/android_gradle` directory.
3.

(Optional) The build process depends on the Kanzi Engine and Kanzi Gradle plugins. When you store your project in the Kanzi workspace directory, Gradle automatically detects the project dependencies.

To build a project from a directory that is not in the Kanzi workspace directory, in the `<ProjectName>/Application/configs/platforms/android_gradle/local.properties` file, set the `kanzi.home` property to the location of the Kanzi workspace directory.

For example:

```
kanzi.home=C\:\\<KanziWorkspace>

```

4.

To build the application package, in the main menu, select Build > Make Project.

By default, Android Studio uses the debug build configuration. When you build the Kanzi project, you can find the Android package at `<ProjectName>/Application/configs/platforms/android_gradle/app/build/outputs/apk/debug`.

To build using the release build configuration, open the Build Variants window and set the Build Variant to release.

> **Tip:** If you do not specify the target architecture, Gradle builds the package for all supported platforms. You can set the architectures for which you want to build your package in `build.gradle`.
>
> ```
> android {
> defaultConfig {
> ndk {
> abiFilters 'arm64-v8a', 'x86'
> }
> }
> }
>
> ```
>
> 5.
>
> Deploy your Kanzi application to an Android device or an Android Virtual Device:
>
> 1.
>
> Connect your Android device to your computer. To deploy to an Android Virtual Device, you must create one. See https://developer.android.com/studio/run/emulator.
> 2.
>
> In the Android Studio main menu, select Run > Run âappâ and select the device to which you want to deploy your application.


## Building and deploying Kanzi applications from the command line


To build and deploy your Kanzi application to an Android device using the command line:

1.

In the Windows Start menu in the Rightware directory, select Kanzi Command Prompt.

When you have more than one version of Kanzi installed, make sure that you launch the Kanzi Command Prompt for the version of Kanzi with which you want to work in that command prompt. See Using the Kanzi Command Prompt.

> **Tip:** To open the Kanzi Command Prompt in Kanzi Studio, select File > Open Kanzi Command Prompt.
> 2.
>
> In the `<ProjectName>/Application/configs/platforms/android_gradle` directory of your project:
>
> - To build an Android package, run one of these commands depending on whether you want to use the release, profiling, or debug build type:
>
> ```
> gradlew assembleRelease
>
> ```


```
gradlew assembleProfiling

```


```
gradlew assembleDebug

```

  - By default, Gradle builds the package with all supported ABIs.

To restrict the set of ABIs built, either:

    - In your Gradle configuration, set the abiFilters parameter.
    - At build time, pass the ABIs with the arch parameter.


See https://developer.android.com/ndk/guides/abis#gc.

For example,

    - To build for 64-bit ARM, run:

```
gradlew assembleRelease -Parch=arm64-v8a

```

    - To build for multiple specific ABIs, provide a comma-separated list:

```
gradlew assembleRelease -Parch=arm64-v8a,x86_64

```


To learn about the Android supported ABIs, see https://developer.android.com/ndk/guides/abis#sa.
  - To install an Android package on a device, run:

```
gradlew assembleRelease installRelease -Parch=arm64-v8a

```

  - To start an Android package on a device, run:

```
gradlew startPackage

```

  - To clean old Android package builds, run:

```
gradlew clean cleanNative

```


## Stripping debug symbols


When you build your application for production, to reduce the binary size, you can strip the debug symbols from the native libraries of your application. To do this, pass the `stripNativeLibs` property:

```
gradlew assembleRelease -PstripNativeLibs

```


> **Note:** A bug in the Android Gradle plugin does not allow you to enable this option by default for a particular build variant. See https://issuetracker.google.com/issues/155215248.
