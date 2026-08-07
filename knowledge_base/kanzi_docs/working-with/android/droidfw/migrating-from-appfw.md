---
title: Migrating from Kanzi application framework (appfw) to Kanzi Android framework (droidfw)
source: https://docs.kanzi.com/4.1.0/en/working-with/android/droidfw/migrating-from-appfw.html
---

# Migrating from Kanzi application framework (appfw) to Kanzi Android framework (droidfw)


Follow these instructions to migrate a Kanzi application from Kanzi application framework (appfw) to Kanzi Android framework (droidfw).

For example, to migrate the Coin example application from Kanzi application framework (appfw) to Kanzi Android framework (droidfw):

1.

In the Quick Start window, click Projects and select the Examples tab. Next to the Coin example, click .
2.

Make a copy of the application at `<KanziWorkspace>/Examples/Coin`.
3.

In Kanzi Studio, open the Kanzi Studio project `Tool_project/Coin.proj.kzm`. In the main menu, select File > Export > Export KZB.
4.

In Android Studio, open the project in the `Application/configs/platforms/android_gradle` directory.
5.

In the `app/build.gradle`:

  - Set the application `minSdk` to 26 or higher. This is the minimum required SDK version for the Kanzi Android framework (droidfw).
  - Configure the application to use the Kanzi Android framework (droidfw). Replace

```
dependencies {
    ...
    implementation 'com.rightware.kanzi:kanziruntime@aar'

```


with

```
dependencies {
    ...
    implementation 'com.rightware.kanzi:kanziruntime-droidfw@aar'

```

  - Add the `kzjava` library as a dependency.

```
dependencies {
    ...
    implementation 'com.rightware.kanzi:kzjava@aar'

```

  - Set the Kanzi Android framework (droidfw) to Java version 8 or newer.

```
android {
    ...
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_11
        targetCompatibility JavaVersion.VERSION_11
    }

```


6.

In the `app/src/main/res/layout/main.xml`, change the View type from

```
com.rightware.kanzi.KanziView

```


to

```
com.rightware.kanzi.KanziSurfaceView

```

7.

In the activity of the application `app/src/main/java/com/rightware/kanzi/coin/Coin.java`:

  - Remove the Activity lifecycle registration from `onCreate(Bundle icicle)`. The Kanzi Android framework (droidfw) automatically tracks the View lifecycle callbacks.

```
mView = findViewById(R.id.kanzicontent);
mView.registerLifecycle(getLifecycle());

```

  - Load the kzb file in `onCreate(Bundle icicle)` and set the prefab that you want to load in this KanziSurfaceView. In this project, you use the default prefab `StartupPrefab`.

In Kanzi application framework (appfw), the native application code loaded the kzb file, while in Kanzi Android framework (droidfw), the native application code is not used.

```
mView = findViewById(R.id.kanzicontent);
mView.setKzbPathList(new String[]{"Coin.kzb.cfg"});
mView.setStartupPrefabUrl("kzb://coin/StartupPrefab");

```

  - Change the method for handling the screen orientation change from

```
@Override
public void onConfigurationChanged(Configuration newConfig)
{
    super.onConfigurationChanged(newConfig);
    mView.setOrientation(newConfig.orientation);
}

```


to

```
@Override
public void onConfigurationChanged(Configuration newConfig)
{
    super.onConfigurationChanged(newConfig);
    mView.handleOrientationChange(newConfig.orientation);
}

```


8.

In the CMake configuration `Application/CMakeLists.txt`:

  - Replace

```
if(ANDROID)
    target_link_libraries(Coin -Wl,--whole-archive Kanzi::kzappfw -Wl,--no-whole-archive)

```


with

```
if(ANDROID)
    target_link_libraries(Coin -Wl,--whole-archive Kanzi::kzdroidfw -Wl,--no-whole-archive)

```

  - Link the `kzinterop` and `kzjava` libraries to the application. Replace

```
target_link_libraries(Coin Kanzi::kzui Kanzi::kzcoreui)

```


with

```
target_link_libraries(Coin Kanzi::kzui Kanzi::kzcoreui Kanzi::kzinterop Kanzi::kzjava)

```


Now the application uses Kanzi Android framework (droidfw) and you can run it on your Android device.
## Migrating application code


After you migrate an application from Kanzi application framework (appfw) to Kanzi Android framework (droidfw), the C++ code in that application is no longer in use. You can migrate the existing C++ code of the application to Java application or plugin code, or refactor the functionality to a C++ Kanzi Engine plugin. Java API does not implement the complete Kanzi Engine API and therefore the approach to migrating the application code depends on the functionality of your application.

You can remove all except one cpp file. To build an application, CMake requires one cpp file, even if that file is empty. For example, remove the content of the `Application/src/coin.cpp`.

For example, to use Java to show in the Coin example the frame time in a Text Block node:

1.

In the `app/src/main/java/com/rightware/kanzi/coin/Coin.java`, in the application activity, add a method to the `Coin` class:

```
void updateFrameTime(Duration duration)
{
    TextBlock2D frameTime = mView.getRoot().lookupNode("#FrameTime");
    frameTime.setText("Frame time: " + duration.toMillis() + " ms");
}

```

2.

In `onCreate(Bundle icicle)`, add a main loop scheduler task to execute the method every frame:

```
KanziRuntime.Reference runtimeRef = KanziRuntime.acquire(this);

mView.addListener(new KanziViewListener() {
     @Override
     public void onStartupPrefabLoaded(View view, Domain domain) {
         runtimeRef.get().getDomain().getMainLoopScheduler().appendTask(
                 MainLoopScheduler.UserStage,
                 "Update Frame Time",
                 TaskRecurrence.Recurring, duration -> updateFrameTime(duration));
     }
});

```


This is what the `app/src/main/java/com/rightware/kanzi/coin/Coin.java` looks like when you make the changes:

```
package com.rightware.kanzi.coin;

import android.content.res.Configuration;
import android.os.Bundle;
import androidx.fragment.app.FragmentActivity;

import android.view.View;
import android.view.WindowManager;

import com.rightware.kanzi.Domain;
import com.rightware.kanzi.KanziRuntime;
import com.rightware.kanzi.KanziView;
import com.rightware.kanzi.KanziViewListener;
import com.rightware.kanzi.MainLoopScheduler;
import com.rightware.kanzi.TaskRecurrence;
import com.rightware.kanzi.TextBlock2D;

import java.time.Duration;

public class Coin extends FragmentActivity
{
    private static final String TAG = "Coin";
    private KanziView mView = null;

    @Override
    protected void onCreate(Bundle icicle)
    {
        setContentView(R.layout.main);

        mView = findViewById(R.id.kanzicontent);
        mView.setKzbPathList(new String[]{"Coin.kzb.cfg"});
        mView.setStartupPrefabUrl("kzb://coin/StartupPrefab");

        // Force the screen to stay on when this app is on front (no need to clear).
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);

        KanziRuntime.Reference runtimeRef = KanziRuntime.acquire(this);

        mView.addListener(new KanziViewListener() {
            @Override
            public void onStartupPrefabLoaded(View view, Domain domain) {
                runtimeRef.get().getDomain().getMainLoopScheduler().appendTask(
                        MainLoopScheduler.UserStage,
                        "Update Frame Time",
                        TaskRecurrence.Recurring, duration -> updateFrameTime(duration));
            }
        });

        super.onCreate(icicle);
    }

    void updateFrameTime(Duration duration)
    {
        TextBlock2D frameTime = mView.getRoot().lookupNode("#FrameTime");
        frameTime.setText("Frame time: " + duration.toMillis() + " ms");
    }

    @Override
    protected void onDestroy()
    {
        super.onDestroy();
    }

    @Override
    public void onConfigurationChanged(Configuration newConfig)
    {
        super.onConfigurationChanged(newConfig);
        mView.handleOrientationChange(newConfig.orientation);
    }
}

```

## Troubleshooting


Here are some of the most common issues that you can encounter while porting a Kanzi application from Kanzi application framework (appfw) to Kanzi Android framework (droidfw).

- Error:

```
<KanziWorkspace>\Projects\CoinPort\Application\configs\platforms\android_gradle\app\src\main\java\com\rightware\kanzi\coin\Coin.java:21: error: cannot find symbol
    mView.registerLifecycle(getLifecycle());
         ^
symbol:   method registerLifecycle(Lifecycle)
location: variable mView of type KanziView

```


Reason: Kanzi Android framework (droidfw) does not have this API. You do not have to manually register Activity lifecycle callbacks.

Solution: You can remove this call.
- Error:

```
7961-7961/com.rightware.kanzi.coin E/AndroidRuntime: FATAL EXCEPTION: main
    Process: com.rightware.kanzi.coin, PID: 7961
    java.lang.NoSuchMethodError: No static method metafactory(Ljava/lang/invoke/MethodHandles$Lookup;Ljava/lang/String;Ljava/lang/invoke/MethodType;Ljava/lang/invoke/MethodType;Ljava/lang/invoke/MethodHandle;Ljava/lang/invoke/MethodType;)Ljava/lang/invoke/CallSite; in class Ljava/lang/invoke/LambdaMetafactory; or its super classes (declaration of 'java.lang.invoke.LambdaMetafactory' appears in /apex/com.android.art/javalib/core-oj.jar)
         at com.rightware.kanzi.KanziViewAdapter.handleAttachedToWindow(KanziViewAdapter.java:274)

```


Reason: Your application does not meet the Kanzi Android framework (droidfw) minimum Java language version requirement.

Solution: In the `app/build.gradle`, set `compileOptions` to Java version 8 or newer.
- Error:

```
9136-9136/? E/ware.kanzi.coin: No implementation found for long com.rightware.kanzi.KanziRuntime.nCreate(android.content.Context) (tried Java_com_rightware_kanzi_KanziRuntime_nCreate and Java_com_rightware_kanzi_KanziRuntime_nCreate__Landroid_content_Context_2)
9136-9136/? E/AndroidRuntime: FATAL EXCEPTION: main
    Process: com.rightware.kanzi.coin, PID: 9136
    java.lang.UnsatisfiedLinkError: No implementation found for long com.rightware.kanzi.KanziRuntime.nCreate(android.content.Context) (tried Java_com_rightware_kanzi_KanziRuntime_nCreate and Java_com_rightware_kanzi_KanziRuntime_nCreate__Landroid_content_Context_2)
      at com.rightware.kanzi.KanziRuntime.nCreate(Native Method)
      at com.rightware.kanzi.KanziRuntime.<init>(KanziRuntime.java:43)
      at com.rightware.kanzi.KanziRuntime.getOrCreateInstance(KanziRuntime.java:195)
      at com.rightware.kanzi.KanziRuntime.acquire(KanziRuntime.java:67)
      at com.rightware.kanzi.coin.Coin.onCreate(Coin.java:30)

```


Reason: Your application is linking to `Kanzi::kzappfw` instead of `Kanzi::kzdroidfw`.

Solution: In the `Application/CMakeLists.txt` change the linking from `Kanzi::kzappfw` to `Kanzi::kzdroidfw`.
- Error:

```
5629-5629/? E/ware.kanzi.coin: No implementation found for long com.rightware.kanzi.mathJNI.new_ColorRGBA__SWIG_3(float, float, float, float) (tried Java_com_rightware_kanzi_mathJNI_new_1ColorRGBA_1_1SWIG_13 and Java_com_rightware_kanzi_mathJNI_new_1ColorRGBA_1_1SWIG_13__FFFF)
5629-5629/? D/AndroidRuntime: Shutting down VM

--------- beginning of crash
5629-5629/? E/AndroidRuntime: FATAL EXCEPTION: main
Process: com.rightware.kanzi.coin, PID: 5629
java.lang.RuntimeException: Unable to start activity ComponentInfo{com.rightware.kanzi.coin/com.rightware.kanzi.coin.Coin}: android.view.InflateException: Binary XML file line #6 in com.rightware.kanzi.coin:layout/main: Binary XML file line #6 in com.rightware.kanzi.coin:layout/main: Error inflating class com.rightware.kanzi.KanziSurfaceView
    at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:4166)
    at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:4312)
    ...

```


Reason: The application cannot find the native backing for `Kanzi::kzjava`.

Solution: In the `Application/CMakeLists.txt` add `Kanzi::kzinterop Kanzi::kzjava` to the list of linked targets.
