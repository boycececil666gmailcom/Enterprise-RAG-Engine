---
title: Android Service example
source: https://docs.kanzi.com/4.1.0/en/examples/transitionanimation/transitionanimation.html
---

# Android Service example


This example demonstrates the usage of the Kanzi Android Service to provide Kanzi functionality to multiple independent client applications. The applications use seamless cross-application transition animations when switching between them.

The example also shows prefab preloading. When you launch the service host application before starting a client, the service preloads Kanzi content so that the client can display the Kanzi content immediately.
## Requirements


- JDK 17
- Gradle 8.7
- Android Gradle plugin 8.6.0
- Android Studio Giraffe or newer
- Android device or emulator with API level 29+

## Getting the example


To get the example, in the Kanzi Studio Quick Start window, click Examples. Next to the Transition Animation example, click .

Kanzi Studio downloads the example to the `<KanziWorkspace>/Examples/Android/TransitionAnimation` directory.
## Building and installing


To build and install the example:

1.

Ensure that your Android device or emulator is running and connected.
2.

Build and install each of the applications:

```
cd Examples/Android/TransitionAnimation/Application/configs/platforms/android_gradle
./gradlew installRelease

cd Examples/Android/TransitionAnimation/Launcher
./gradlew installRelease

cd Examples/Android/TransitionAnimation/Settings
./gradlew installRelease

```

3.

Grant the **Display over other applications** permission to the service host (**Application**) only. The service host renders the transition overlay, so only that application needs this permission.

To grant this permission:

  - Go to Settings > Apps > Application > Advanced > **Display over other applications**.


> **Note:** On Android Automotive devices, you cannot grant the **Display over other applications** permission through the Android UI for newly installed applications. For alternatives, such as signing with platform keys or granting the permission with adb, see Developing with the Kanzi Android Service.
> 4.
>
> Launch the Launcher application from the app drawer. The client app automatically connects to the Kanzi Android Service and displays the Kanzi content.
> 5.
>
> Use the bottom navigation bar to switch between the Launcher and Settings applications. The cross-app transition animation is shown during the switch.
>
