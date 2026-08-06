---
title: Working with Kanzi Android framework (droidfw) projects
source: https://docs.kanzi.com/4.1.0/en/working-with/android/droidfw/droidfw-projects.html
---

# Working with Kanzi Android framework (droidfw) projects

## Adding Kanzi Android framework (droidfw) to your Android application


To add Kanzi Android framework (droidfw) to an Android application that you created using Android Studio templates either:

- Integrate Kanzi as a library sub-project. This is the recommended approach to start using Kanzi on Android. See Integrating Kanzi as a library sub-project.
- Integrate Kanzi as a pre-built library. Use this approach if the separation meets the requirements of your workflow. For example, if you benefit from not installing Kanzi or required tooling. See Integrating Kanzi as a prebuilt library (AAR).

### Integrating Kanzi as a library sub-project


> **Tip:** This is the recommended approach to start using Kanzi on Android.
>
> When you integrate Kanzi as a library sub-project, you add Kanzi CMake integration to your application as an Android library sub-project.
>
> To integrate Kanzi as a library sub-project:
>
> 1.
>
> From the `<KanziWorkspace>/Templates/Android_library` directory, copy to the root of your Android project:
>
> - `getkanzi.gradle` file
> - `kanzinative` directory
>
> 2.
>
> In the `settings.gradle` or `settings.gradle.kts` file of your project, add:
>
