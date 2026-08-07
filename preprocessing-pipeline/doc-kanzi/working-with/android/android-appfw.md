---
title: Developing for Android with the Kanzi application framework (appfw)
source: https://docs.kanzi.com/4.1.0/en/working-with/android/android-appfw.html
---

# Developing for Android with the Kanzi application framework (appfw)

Use the Kanzi application framework (appfw) when you want to create an application for multiple platforms and you intend to share non-trivial application code between the platforms.

Kanzi application framework (appfw) is a framework for developing cross-platform applications. You write application and plugin code in C++ and extending Android-specific functionality requires writing JNI glue code. When you use Kanzi application framework (appfw), you can render a Kanzi application to only one Android View at a time.
## Android lifecycle events in a Kanzi application

The Android lifecycle events set how your Kanzi application behaves when the activity state changes. Each event maps to an Android activity callback method. A Kanzi application uses these lifecycle events:

- `Lifecycle.Event.ON_CREATE`

```
// Load the native library that provides Kanzi functionality,
// initialize the context, and assign the KanziView for rendering.
// This function calls the KanziNativeLibrary.createApplication() function,
// which loads the Kanzi project.
KanziView.createNativeApplication();

```

- `Lifecycle.Event.ON_DESTROY`

```
// Halt and destroy the Kanzi application.
// This function calls the KanziNativeLibrary.haltApplication() and
// KanziNativeLibrary.destroyApplication() functions.
KanziView.destroyNativeApplication();

```

- `SurfaceHolder.Callback.surfaceCreated` (`KanziView.surfaceCreated`)

```
// When the application surface is created, run the Kanzi application.
KanziNativeLibrary.runApplication(holder.getSurface());

```

- `SurfaceHolder.Callback.surfaceDestroyed` (`KanziView.surfaceDestroyed`)

```
// When the Kanzi application surface is destroyed, pause rendering.
KanziNativeLibrary.haltApplication();

```

- `SurfaceHolder.Callback.surfaceChanged` (`KanziView.surfaceChanged`)

```
// When the format or size of the Kanzi application surface changes,
// resize the application surface.
// @param width: The new width of the surface.
// @param height: The new height of the surface.
KanziNativeLibrary.resizeEvent(width, height);

```

Kanzi does not use the `LifeCycle.Event.ON_PAUSE` and `Lifecycle.Event.ON_RESUME` events because they do not tell whether the application surface is ready for rendering. To pause and resume rendering, `KanziView` uses these functions:

- `SurfaceHolder.Callback.surfaceCreated` (`KanziView.surfaceCreated`)
- `SurfaceHolder.Callback.surfaceDestroyed` (`KanziView.surfaceDestroyed`)

See https://developer.android.com/reference/androidx/lifecycle/Lifecycle.Event.html and https://developer.android.com/reference/android/view/SurfaceHolder.Callback.

This diagram shows the initialization sequence of a Kanzi application on the Android platform.
## Adding Kanzi application framework (appfw) to your Android application

To use Kanzi application framework (appfw) with your existing Android Studio application project:

- Integrate Kanzi libraries
- Add a `KanziView` to your Android activity
- Import Kanzi Studio project assets

### Integrating Kanzi libraries into an Android Studio project

You can add Kanzi to your Android application by making your Android Studio project depend on prebuilt Kanzi Android library and native Kanzi libraries as an Android library sub-project.

To integrate Kanzi libraries into an existing Android Studio project:

1.

From the `<KanziWorkspace>/Templates/Android_library` directory, copy to the root of your Android project:

  - `getkanzi.gradle` file
  - `kanzinative` directory

2.

Remove the content from the `<AndroidProject>/kanzinative/src/main/cpp` directory.
3.

From the `<ProjectName>/Application` directory of your Kanzi project, copy to `<AndroidProject>/kanzinative/src/main/cpp` directory:

  - `CMakeLists.txt` file
  - `cmake` and `src` directories

4.

In the `settings.gradle` or `settings.gradle.kts` file of your project, add:
