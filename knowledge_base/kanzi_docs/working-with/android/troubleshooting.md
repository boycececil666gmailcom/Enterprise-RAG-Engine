---
title: Troubleshooting Android application development with Kanzi
source: https://docs.kanzi.com/4.1.0/en/working-with/android/troubleshooting.html
---

# Troubleshooting Android application development with Kanzi

- When you receive errors similar to these while building an Android package or opening a project in Android Studio:

```
Your build is currently configured to use incompatible Java 21.0.3 and Gradle 7.6.2. Cannot sync the project.

```

```
Unsupported Java.
Your build is currently configured to use Java 17.0.6 and Gradle 6.7.1.

```

```
Unsupported class file major version 61.

```

These errors occur because of a mismatch between the Gradle tools and the active JDK. To resolve these errors:

  - If you created your application with Kanzi 3.9.7 or older, migrate your project to use the newer tooling. See Changes to the Android application templates.
  - Ensure that your application is set to use a compatible JDK. See Installing JDK.

- When you receive this error while building an Android package:

```
FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':app.packageDebug'.
Failed to obtain compression information for entry

```

Make sure that you are using Android Studio version 4.1.3 or newer. This error occurs on Android Studio version 3.1.
- When you receive this error while building an Android package:

```
FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':app.packageDebug'.
Java heap space

```

Increase the available heap amount in the Gradle build system. For example, in Android Studio open the `<ProjectName>/Application/configs/platforms/android_gradle` project, in that project open the `gradle.properties` file and set:

```
org.gradle.jvmargs=-Xmx4608m

```

- When you receive this error while building an Android package:

```
FAILURE: Build failed with an exception.

* Where:
Build file 'Engine\configs\platforms\android_gradle\kanziruntime\build.gradle' line: 103

* What went wrong:
A problem occurred evaluating project ':kanziruntime'.
<PathToKanziWorkspace>\Engine\version.txt not found

```

In the `<ProjectName>/Application/configs/platforms/android_gradle` directory of your project create a file called `local.properties` and in that file set the correct location of your workspace. For example, set:

```
kanzi.home=C\:\\<KanziWorkspace>

```

- When you receive this warning while building an application that uses the Data_source_plugin_template:

```
More than one file was found with OS independent path 'lib/arm64-v8a/libkzcoreui.so'.
This version of the Android Gradle Plugin chooses the file from the app or dynamic-feature
module, but this can cause unexpected behavior or errors at runtime. Future versions of
the Android Gradle Plugin will throw an error in this case

```

Update the Kanzi Gradle plugin to version 0.7.1.
- When you receive one of these exceptions when running your Android application:

```
java.lang.BootstrapMethodError: Exception from call site #0 bootstrap method

```

```
E/AndroidRuntime: FATAL EXCEPTION: main
Process: <process name>, PID: <pid>
java.lang.NoSuchMethodError: No static method metafactory(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;Ljava/lang/invoke/MethodType;Ljava/lang/invoke/MethodHandle;Ljava/lang/invoke/MethodType;)Ljava/lang/invoke/CallSite; in class Ljava/lang/invoke/LambdaMetafactory; or its super classes (declaration of 'java.lang.invoke.LambdaMetafactory' appears in /apex/com.android.runtime/javalib/core-oj.jar)
  at com.rightware.kanzi.KanziViewAdapter.loadStartupPrefab(KanziViewAdapter.java:664)
  at com.rightware.kanzi.KanziViewAdapter.setStartupPrefabUrl(KanziViewAdapter.java:196)

```

Your application is most likely using an incompatible version of Java. Kanzi Android framework (droidfw) and Kanzi Java API require Java 8 (1.8).

In the `app/build.gradle` file of your Android Studio project, ensure that the Java language version is set to a compatible version:

```
android {
    ...

    compileOptions {
       sourceCompatibility JavaVersion.VERSION_11
       targetCompatibility JavaVersion.VERSION_11
    }
}

```

- When using Android Studio to convert a Java project to Kotlin, the default generated gradle script uses the latest version of Kotlin by default. This can result in an error similar to:

```
The minCompileSdk (31) specified in a
dependency's AAR metadata (META-INF/com/android/build/gradle/aar-metadata.properties)
is greater than this module's compileSdkVersion (android-28).
Dependency: androidx.core:core-ktx:1.8.0-alpha01.

```

Make sure that the version of Kotlin is compatible with your project. For example, if your project uses compileSdkVersion 28, downgrade Kotlin to version 1.6.0.

Replace

```
implementation "androidx.core:core-ktx:+"

```

with

```
implementation "androidx.core:core-ktx:1.6.0"

```

or

```
implementation "androidx.core:core-ktx:$kotlin_version"

```

- When you get these error messages from your Android application:

```
I/Kanzi: [info:generic] kzsEGLConfigure(): no EGL configurations with GLES3 support present, downgraded EGL configuration request to GLES2.

```

```
E/Kanzi: [error:generic] Half-float is not supported by current platform, please re-export kzb file(s) without half-floats.

```

The application uses features that are available only in OpenGL ES 3.0. In the Android Emulator, enable OpenGL ES 3.0. See Enabling OpenGL ES 3.0 in the Android Emulator.
- When you receive this error while configuring a CMake build for Android:

```
Kanzi workspace path contains spaces:
  <PathToKanziWorkspace>
Android Gradle Plugin cannot package native shared libraries when the
workspace path contains spaces.

```

This error occurs because CMakeâs file-based API quotes library paths in its JSON response when the path contains spaces. Android Gradle Plugin does not strip these quotes, which causes it to skip imported shared libraries. The result is an APK with no native `.so` files, leading to `UnsatisfiedLinkError` at runtime.

To fix this, move the Kanzi workspace to a path without spaces and update the workspace location in your projectâs `local.properties` file accordingly.
