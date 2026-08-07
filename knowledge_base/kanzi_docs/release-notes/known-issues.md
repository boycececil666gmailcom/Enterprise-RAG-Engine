---
title: Known issues
source: https://docs.kanzi.com/4.1.0/en/release-notes/known-issues.html
---

# Known issues

## Known issues in Kanzi Engine

- Some parts of Kanzi API are written in C. In the future Kanzi releases we will continue the effort of converting the API to C++.
- When linking applications to the libraries provided with SDK without sources generates warning about missing debug information.
- Clipping of rotated child 2D nodes is ignored because of performance reasons. For example, if an Image node has a child Image node, and you rotate the child Image node, the parent Image node does not clip the child Image node.
- Current limitation of the Kanzi Engine is that if a 2D node is forced to render to a render target (for example, Viewport 2D with rotation), clipping is applied even when you disable clipping in a 2D node.
- When you change the Samples property of a Render Target Texture you have to restart the Preview to apply the change.
- When the glyph cache texture in Kanzi Studio is full, the application performance decreases in Kanzi Studio. This does not affect the performance of your Kanzi application when you build it and appropriately adjust the size of the glyph cache texture for your target platform. See Glyph cache texture size.
- The `Node2D_plugin` example prints warnings when you run it in the Preview.
- Kanzi application freezes when user scrolls a Trajectory List Box 3D with negative item spacing absolute value of which is higher than the width of list box items.
- When you create a Prefab Placeholder 3D node, in some cases Kanzi selects a prefab that it cannot instantiate. This can cause undefined behavior and the Preview to show incorrect content.

Workaround:

  1.

Press F8 to exit the Preview.
  2.

In the Prefab Placeholder 3D node set the prefab to the correct prefab.
  3.

Press F5 to start the Preview.

- The TextBox2D is only implemented for Windows platforms, and to use it you need to include the following snippet to `registerMetadataOverride` in your application code:

```
#if defined WIN32
    WindowsImeBackend::registerModule(getDomain());
#endif

```

- This alpha release includes third-party components exposed to several CVE vulnerabilities. The majority of these vulnerabilities are not applicable to Kanzi Engine, while the rest will be addressed in future releases.

## Known issues in Kanzi Studio

- Kanzi Studio may fail to launch on virtual machines and periodically on desktop Windows installations, reporting an unhandled exception error.

The Windows Event Log and/or Kanzi Studio Logs will contain an entry similar to this:

```
Unhandled exception: System.InvalidProgramException: Common Language Runtime detected an invalid program.
  at Rightware.Kanzi.Tool.ApplicationCommon.EnvironmentInitializer.***********(IEnumerable1  , Boolean  )

```

Workaround: Restart Windows or the virtual machine.
- When importing kzm files, Kanzi Studio is unable to load kzm files from subdirectories.

Workaround: In File Explorer, copy each kzm file into the root directory of its resource type. For example, copy a material from the `Project1/Materials/subdirectory/` to the `Project2/Materials/` directory.
- When you import the same dds file twice, Kanzi Studio creates an invalid texture and shows invalid content in the Image property dropdown menus.

Workaround: Update the file in File Explorer, or delete the dds file and its texture before importing them again.
- The device driver for the AMD Radeon R9 M370X included in the Boot Camp update 6.0 causes the Preview to not work. To fix the issue, use the Windows Device Manager to roll back to the previous version of the driver.
- Importing fbx files which contain animations that use custom pivot points, can cause Kanzi Studio to terminate. This is caused by a defect in the FBX importer provided in the Autodeskâs FBX SDK.

After the import fails, open the Kanzi Studio project:

  1.

In the Library > Resource Files > 3D Assets select the fbx file that caused Kanzi Studio to terminate.
  2.

In the Properties disable the Convert Pivot Points property.

    - When disabled, Kanzi Studio ignores the custom pivot points in the fbx file, which can affect the rotation and scale animations for nodes that use custom pivot points.
    - When enabled, Kanzi Studio resets the pivot points to the default positions without making visual changes to animations. This is the recommended setting because Kanzi Studio does not support custom pivot points.
    - Custom pivot points contain an additional transform which Kanzi Studio bakes into a single transform. In some cases, custom pivot points do not contain any data, so disabling this option does not affect the content.

  3.

In the Library > Resource Files > 3D Assets right-click the fbx file that caused Kanzi Studio to terminate, and select Import 3D Asset File to import the file.

- Kanzi Studio does not support importing of animated pivot points.
- Kanzi Studio does not support these glTF 2.0 features:

  - Double-sided materials
  - Point and line primitives
  - Samplers with differing wrap modes for S and T dimensions. Kanzi Studio uses the wrap mode for S dimension for both.

- Kanzi Studio is compatible only with screen DPI settings set to 100%.
- When you close the Node Tree window, the selection in the window does not update correctly.
- Thumbnails are not rendered correctly for all assets.
- Copy-pasting in the Node Tree a Scene prefab that contains a skinned mesh does not work.

Workaround: Drag and drop the Scene prefab from the Prefabs to the location in your project where you want to use it.
- When you reload the changes from a referenced Kanzi Studio project that is opened in another instance of Kanzi Studio, Kanzi Studio can become unstable.

Workaround: Close the referenced project before you reload the changes in the project where the project is referenced.
- When a node contains multiple instances of the same prefab, you cannot create a binding from the node that contains these prefabs to the properties of nodes inside an instance of that prefab.

Workaround: Make the properties to which you want to bind available in the root of the prefab and create the bindings in the root of the prefab instance. See Customizing instances of a node prefab.
- When you change the value of the Prefab Template property of a Prefab View, Kanzi fails to show the default values of the properties of the prefab template. This happens when you change the value of the property in any other way than by setting it in the Properties, such as when you use a state manager or application code. The same issue occurs when you change the value of the Render Pass Prefab property in a Render Pass View.

Workaround: In Kanzi Studio add to the Prefab View or Render Pass View the properties of each prefab template or render pass prefab that you set the Prefab View or Render Pass View to use.
- Kanzi Studio does not support setting the Mesh Material property of a primitive mesh to a material from a referenced project.

Workaround: Use the Material (Model3D.Material) property to set the material. The value of the Material property overrides the value of the Mesh Material property.
- When you disable or delete a to-source binding, the Preview does not show the result of the disabling or deleting.

Workaround: To see the result, restart the Preview.
- When you deploy from Kanzi Studio to an Android device a project that uses the Kanzi Studio project template, and Code Behind functionality, the deployed application terminates on the Android device soon after it opens.

Workaround: To deploy such applications, use Android Studio instead of Kanzi Studio.
- When you deploy from Kanzi Studio to an Android device an application, which loads kzb files listed in the `<project_name>.kzb.cfg` file, the application terminates because of failing to load the kzb files.

Workaround:

In Kanzi Studio first export the kzb files, then build and deploy the Android Package:

  1.

File > Export > Export KZB.
  2.

File > Export > Build Android Package.

- After you rename a Kanzi Studio project, Kanzi Studio treats already existing Code Behind projects like a regular Kanzi Engine Plugin. This means that you cannot open such Code Behind projects using the Activity Browser and starting or restarting the Preview does not automatically start the rebuilding of such Code Behind projects.

Workaround: To build a Code Behind project, manually open and build the Code Behind project in Visual Studio, and restart the Kanzi Studio Preview.
- If you uninstalled NDK 21.1.6352462, the application for the Tutorial: Data sources for Android does not build from Kanzi Studio when you select File > Export > Build Android Package. In Kanzi Studio, the Log window shows this error:

```
FAILURE: Build failed with an exception.
* What went wrong:
A problem occurred configuring project ':app'.
NDK at C:\Users\<User>\AppData\Local\Android\Sdk\ndk\21.1.6352462 did not have a source.properties file

```

This is an issue in the Android Gradle Plugin version 4.1.3 that erroneously defaults to NDK 21.1.6352462 even when `app/build.gradle` sets `android.ndkVersion` to 21.3.6528147.

Workaround: To build the tutorial application, remove the `C:/Users/<User>/AppData/Local/Android/Sdk/ndk/21.1.6352462` directory and run build the application from Kanzi Studio. During the build, Gradle downloads NDK 21.1.6352462, installs it, and uses it to build the tutorial application.
- Some of the tutorials depend on the XML_data_source plugin. Now that the examples and tutorials are not part of the installer, compilation of the project may fail. Workaround: The dependencies can be provided by downloading the Data sources tutorial first. The Get the tutorial step of the affected tutorials now includes this step.
- Overwriting existing Kanzi project functionality does not work correctly with the kzm file format.
- When Importing a project that contains a mesh using morphing with smart materials, the imported mesh does not morph. In Kanzi Studio, the Log window shows this error:

```
[create-vertexinputstate-attributesize] Binding 1 must provide attributes.

```

Workaround:

In Kanzi Studio, after importing the project, save and reopen the project:

  1.

File > Save Project or File > Save Project Asâ¦.
  2.

File > Open Projectâ¦.
  3.

Select the project saved in step 1.

- Automatic resource binding in GLSL shaders does not work in all situations. We recommend that you use explicit bindings for all resources in your GLSL shaders.

## Known issues with Kanzi Activities

- The Activity Browser is functional only when the Preview is active. Because the Activity Browser reflects the runtime state of the Preview application, it is disabled when the Preview is not active.
- Preview Tools do not currently support Activities. Activity and Activity Host nodes lack Preview visualization and interaction capabilities:

  - The Preview does not display a selection overlay for selected Activity or Activity Host nodes.
  - You cannot modify or interact with Activity or Activity Host nodes, or their content, in the Preview.
  - The Node Tool does not function with Activity or Activity Host nodes.

Workaround: To use Preview tools with an Activity, open the corresponding Activity Prefab in the Preview Composition tab. In this context, all Preview visualization and interaction features are fully supported for the Activity.
- The Activate Activity Message and Deactivate Activity Message require an Activity Activation Path that is relative to the Activity Host. However, the Copy Activation Path command copies the full path including the root node, which is incompatible with the message argument format.

Workaround: Manually edit the copied path to remove the root node prefix before using it in an Activate Activity Message or Deactivate Activity Message.
- The Deactivate Activity Message deactivates all Activities along the path to the target Activity, not only the target Activity itself.
- When you add a new transition to an Activity that already has a transition, Kanzi Studio creates an additional State Manager and leaves the previously created State Manager disconnected. Over time, this can result in multiple disconnected State Managers accumulating in the Library.

Workaround: After adding transitions, manually remove any disconnected State Managers from the Library.
- When using the Activities workflow, the Node Tree window shows only the Screen and the root Activity Host. The rest of the Activity hierarchy is visible only in the Activity Browser and the Prefabs window.
- Features of the Node Tree window, such as thumbnails and visibility controls, are not available for Activity content because editing has moved to the Prefabs window and the Activity Browser.
- The Prefabs window does not fully align with the Activities workflow. It allows creation of invalid Activity structures; for example, creating an Activity as a direct child of another Activity, which is not a valid Activity hierarchy.

Workaround: Use the Activity Browser to create and manage Activity structures to ensure valid hierarchies.

## Known issues in the Kanzi SDK

- The Coin example does not run on the x86/x86_64 Android emulator.

## Known issues on platforms

- The standalone android-freetype and android-freetype-itype platform packages contain an unnecessary header file: `Engine/libraries/platforms/android-r21d-aarch64/opengl_es_2_0/include/EGL/eglplatform.h`.
- QNX deprecated the use of QCC as CXX compiler. The compilation of a QNX application fails with the error

```
QCC is not a full path and was not found in the PATH.

```

For workaround, see Known issues on QNX.
- On the QNX platform, these window format values are hardcoded:

  - Buffer size to 24
  - Alpha size to 0
  - Padding size to 8

- These graphics outputs do not support kzgfx:

  - `QnxStream`
  - `QnxEGLPbuffer`

- An Android application may fail to request specific surface properties on the emulator or device when the requested configuration is not available. This is caused by a change where the previous best-match logic has been replaced with strict matching. This issue occurs more frequently on the Android x86_64 emulator, but can also affect other platforms.

Workaround: Request surface properties that match an EGL configuration present on the device.
