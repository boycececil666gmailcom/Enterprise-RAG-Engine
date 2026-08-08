---
title: Programming Activities with Java Code Behind
source: https://docs.kanzi.com/4.1.0/en/working-with/activities/java-code-behind.html
---

# Programming Activities with Java Code Behind
**Note:** Kanzi supports Java Code Behind only for Kanzi Android framework (droidfw) applications. See Developing with the Kanzi Android framework (droidfw).
Before you can program Activities with the Java Code Behind, make sure that you have your Kanzi development environment set up. See Requirements for Android application development with Kanzi.
To program Activities with Java Code Behind:
1.
In the Activity Browser, create an Activity or Activity Host that you want to program.
For example, create a root Exclusive Activity Host with several Activities.
2.
In the Activity Browser, right-click an Activity or Activity Host and select Add Code Behind > Java. In the Create Code Behind dialog, you can set the package name for the Code Behind.
When you add Java Code Behind to an Activity node, Kanzi Studio:
1.
Copies the Java Code Behind from the `<KanziWorkspace>/Templates/Java_code_behind_template`.
2.
In the `<ProjectName>/Application/configs/platforms/android_gradle/<ProjectName>codebehind` directory creates a Java Code Behind module and project for the Activity to which you added Java Code Behind.
3.
Compiles the Java Code Behind module.
4.
Imports to the Kanzi Studio project the jar file that contains the functionality defined in the Java Code Behind module as a Kanzi Engine plugin.
5.
Restarts the Preview.
When the Preview starts, in the Activity Browser the Activities with Java Code Behind contain the  icon and the side panel shows the commands that are defined in the Java Code Behind.
3.
In the Activity Browser, right-click the Activity to which you added Java Code Behind and select Open Code Behind > Java.
Kanzi Studio opens in Android Studio the Android project that contains the Java Code Behind.
The Java Code Behind is stored in the directory `<ProjectName>/Application/configs/platforms/android_gradle/<ProjectName>codebehind`.
Tip
In the Kanzi Studio main menu, select File > Open Android Project in Android Studio.
Kanzi Studio opens in Android Studio the Android project from the `<ProjectName>/Application/configs/platforms/android_gradle` directory.
4.
In Android Studio in the `<ProjectName><ActivityNodeName>ActivityCode.java` file, add the initialization functionality for that Activity node in the `NodeComponent.attachOverride` function and save the file. In the `NodeComponent.attachOverride` function, you can install message handlers and property listeners, create nodes, set up the look and functionality of the activity, and so on.
This way you provide unique functionality to that Activity node so that you can react to status changes through code.
5.
Use the Java Code Behind in your project:
1.
In the Prefabs, in the prefab that you use for the Activity to which you added Java Code Behind, create a Button or List Box node, or create a List Box Item Container prefab.
For example, create a Button 2D node.
2.
In the Properties, add the Command property and set it to the command that you created in the `<ProjectName><ActivityNodeName>ActivityCode.java` file.
When you activate the Activity with the Button 2D node that you created earlier, and in the Preview click that button, the Log window shows the default message of the MyFirstCommand.

## Troubleshooting Java Code Behind

- When build errors in the Java Code Behind prevent the Preview from starting, you can see the errors in the Kanzi Studio Log window.

To rebuild Java Code Behind after you fix the errors, in the Kanzi Studio main menu, select Preview > Restart Preview.
- When you add Java Code Behind and the Java project has an invalid `build.gradle` definition for the namespace, Kanzi Studio lists the issues in this dialog.

Fix the issues and click Refresh.

Starting with Kanzi Studio 3.9.7, you can add Java Code Behind to Kanzi Studio projects that use:

  - Android Gradle Plugin version 7.2.2 or newer
  - Gradle version 7.3.3 or newer

See Changes to Java Code Behind.

## Using Java Code Behind in the API

For details, see the `CodeBehind` class.
