---
title: Android resources in Kanzi
source: https://docs.kanzi.com/4.1.0/en/examples/resource-import/resource-import.html
---

# Android resources in Kanzi


This example shows how to use Android resources in a Kanzi Studio project.
## Getting the example


To get the example, in the Kanzi Studio Quick Start window, click Projects and select the Examples tab. Next to the Resource_import example, click .

Kanzi Studio downloads the example to the `<KanziWorkspace>/Examples/Android/Resource_import` directory.
## Structure of the example


These modules make the application:

- `app` module is the main application. It provides the Android resources in this example and registers the `resourceplugin` Java plugin. See `MainActivity.java`.
- `resourceplugin` module is a Java plugin. It provides a custom `ResourceManager` protocol implementation to Kanzi Engine on Android device and for the Kanzi Studio Preview. See `AndroidProtocolHandler.java` and `PreviewAndroidProtocolHandler.java`.
- `rro` module is an example of a runtime resource overlay (RRO). It showcases an overlay of the Android resources in this project. See `<KanziWorkspace>/Examples/Android/Resource_import/Application/configs/platforms/android_gradle/rro/README.md` and the [Android RRO documentation](https://source.android.com/docs/core/runtime/rros).


These nodes in the Kanzi Studio project use the Android resources that are defined in the application:

- RootNode node has the Background Brush property set to the Resource ID with the value `android://color/background`.
- rotary node has the Image property set to the Resource ID with the value `android://drawable/rotary`.
- hello node has the Text property set to the Resource ID with the value `android://string/hello`.
- kanzi node has the Text property set to the Resource ID with the value `android://string/kanzi`.
- hello and kanzi nodes have the Foreground Brush property set to the Resource ID with the value `android://color/text`.

## Running the example


To run the example:

1.

Connect your Android device to your computer.
2.

In the Kanzi Studio Quick Start window, click Projects and select the Examples tab. Next to the Resource_import example, click Open.
3.

In the main menu select File > Export > Build Android Package.

Kanzi Studio creates an Android package from your Kanzi Studio project, deploys, and runs it on your Android device.
