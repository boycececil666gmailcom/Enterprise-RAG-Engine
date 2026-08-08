---
title: Jetpack Compose example
source: https://docs.kanzi.com/4.1.0/en/examples/compose/compose.html
---

# Jetpack Compose example

This example shows how to use Kanzi Android framework (droidfw) with Jetpack Compose on Android. For the Gradle files, the example uses Kotlin DSL.

Requirements:

- JDK 17
- Gradle 8.0 or newer
- Android Gradle plugin 8.1.2 or newer
- Android Studio Giraffe or newer

## Getting the example

To get the example, in the Kanzi Studio Quick Start window, click Projects and select the Examples tab. Next to the Compose example, click .

Kanzi Studio downloads the example to the `<KanziWorkspace>/Examples/Android/Compose` directory.
## Content of the example

The main activity `ComposeActivity` contains these Kanzi-based composables:

- `CoverFlow` loads a Kanzi prefab from a kzb file.
- `End` instantiates a Kanzi Text Block node and sets the text that the node shows.

## Running the example

To run the example:

1.

Connect your Android device to your computer.
2.

In the Kanzi Studio Quick Start window, click Projects and select the Examples tab. Next to the Compose example, click Open.
3.

In the main menu select File > Export > Build Android Package.

Kanzi Studio creates an Android package from your Kanzi Studio project, deploys, and runs it on your Android device.
