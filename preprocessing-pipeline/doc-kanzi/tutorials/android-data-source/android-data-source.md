---
title: Tutorial: Data sources for Android
source: https://docs.kanzi.com/4.1.0/en/tutorials/android-data-source/android-data-source.html
---

# Tutorial: Data sources for Android

In this tutorial you learn how to create a data source for Kanzi applications for Android. You learn how to:

- Create a data source using Kanzi Java API.
- Use Android APIs to back the data source.
- Ensure compatibility with the Kanzi Studio Preview where the Android APIs are not available.

This video shows the result of the tutorial.

This tutorial assumes that you are familiar with developing Android applications, Java programming language, and that you understand the basics of working with Kanzi Studio. The best entry points for getting familiar with Kanzi Studio are:

- Tutorial: Getting started with Kanzi Studio
- Tutorial: Getting started with Kanzi Android framework (droidfw)

Before you start this tutorial, make sure that you have your Kanzi development environment for Android set up. See Requirements for Android application development with Kanzi.

To run the application that you create in this tutorial in an Android virtual device, set the virtual device:

- API level to 29 or higher
- Internal storage to at least 8 GB

## Get the tutorial

To get the tutorial, in the Kanzi Studio Quick Start window, click Projects and select the Tutorials tab. Next to the Android data source tutorial, click .

Kanzi Studio downloads the tutorial to the `<KanziWorkspace>/Tutorials` directory. You can find:

- The tutorial assets in the `<KanziWorkspace>/Tutorials/Android data source/Assets` directory.
- The completed tutorial in the `<KanziWorkspace>/Tutorials/Android data source/Completed` directory.

## Create a one-way data source

In this section you create a data source that you can read from a Kanzi application. You create a widget that shows the battery level of an Android device.

To create a one-way data source:

1.

In Kanzi Studio, create a project. In the New tab of the Quick Start window:

  - Set the Project Name to Android data source
  - Select the Android application with Java plugin project template

Use this template to start building a Kanzi Java API data source.

Android application with Java plugin template creates a Kanzi Studio project with a Kanzi Android framework-based application that contains a Kanzi Engine Java plugin.

Use the Kanzi Android framework (droidfw) when you want to create an application for the Android platform, and you intend to use Android APIs and services extensively.

Kanzi Android framework (droidfw) is a framework dedicated for developing Kanzi applications for Android. It exposes the Kanzi Java API, which allows you to write application and plugin code entirely in Java or Kotlin. You do not need to write any C++ or JNI code, but you can still use native Kanzi plugins. Kanzi Android framework (droidfw) provides strong integration with the Android UI, including support for multiple simultaneous Kanzi-based Views and flexible composition of Kanzi and Android UI elements. Kanzi Android framework (droidfw) integrates with the Android Choreographer which runs the Kanzi main loop tasks in the Android UI thread. This enables you to use the Kanzi Java API from your application code without the need for dispatcher mechanisms.

2.

In Android Studio:

  1.

Open the `Android data source/Application/configs/platforms/android_gradle` project.
  2.

In `androiddatasourceplugin` > `java` > `com.example.androiddatasourceplugin` in the `JavaDataSource` class:

    1.

Add a constant that defines the name of the battery level data object.

```
static String BATTERY_LEVEL = "BatteryLevel";

```

    2.

In the `initialize()` method, replace the existing data source setup

```
root.addChild(DataObjectInt.create(domain, "Integer value", 1).get());
root.addChild(DataObjectString.create(domain, "String value", "dummy value").get());
root.addChild(DataObjectReal.create(domain, "Real value", 0.5).get());

```

with

```
root.addChild(DataObjectReal.create(domain, BATTERY_LEVEL, 0.5f).get());

```

  3.

In the Gradle tool window in androiddatasource > androiddatasourceplugin > Tasks > kanzi, right-click either exportJarDebug or exportJarRelease and select Run.

If exportJarDebug is missing, then you need to sync gradle project in Android Studio.

Android Studio builds the Kanzi Engine data source plugin JAR that you use in Kanzi Studio.

3.

In Kanzi Studio, create the content to show the value of the data source that you defined in Android Studio.

  1.

In the Node Tree, delete the Viewport 2D node.

You can delete the Viewport 2D node because you do not create any 3D content in this tutorial.
  2.

In the RootNode, create a Flow Layout 2D node and name it Controls.
  3.

In the Properties, add and set the Horizontal Alignment and Vertical Alignment properties to Center.
  4.

In the Node Tree in the Controls node, create an Empty Node 2D node and name it Battery Widget. In the Properties, add and set:

    - Layout Width to 150
    - Layout Height to 200

  5.

From the Asset Packages > Factory Content, drag the Progress Indicator to the Battery Widget node in the Node Tree.
  6.

In the Node Tree, select the Progress Indicator prefab placeholder. In the Properties, add and set:

    - Layout Width to 150
    - Layout Height to 150
    - Ring Thickness to 0.3

  7.

In the Node Tree in the Battery Widget node, create a Text Block 2D node. In the Properties, add and set:

    - Horizontal Alignment to Center
    - Vertical Alignment to Bottom
    - Text to Battery

4.

In Kanzi Studio, create a data source and take it into use:

  1.

In the Library > Kanzi Engine Plugins right-click the Android_data_source plugin and select Update Kanzi Engine Plugin.

This way you update the load the plugin that includes the changes that you made in the Android Studio plugin project.
  2.

To take the plugin changes into use, restart the Preview.
  3.

In the Window main menu, select Data Sources.

Use the Data Sources window to create, set, and delete the data sources in your project, and to connect data objects from a data source to nodes and resources in your project.
  4.

In the Data Sources window, click Create Data Source and create a data source with these settings:

    - Name to Android data source
    - Data Source Type to JavaDataSource

In the Data Sources window, you can see the BatteryLevel data object that you defined in Android Studio.
  5.

In the Node Tree, select the RootNode node. In the Properties, add the Data Context > Data Context property and set it to Android data source.

By setting the Data Context property you tell your application from which data source it receives data. When you set the Data Context property for a node, all its child nodes inherit the value of the Data Context property. If you want to use a different data context for one of the child nodes, add the Data Context property to that node and set it to the data context you want to use.
  6.

In the Node Tree, select the Progress Indicator node. In the Properties, click + Add Binding and in the Binding Editor set:

    - Property to Progress
    - Expression to

```
{DataContext.BatteryLevel} * 100

```

Click Save.

5.

In Kanzi Studio, select File > Export > Export KZB.
6.

Update the data source to get the battery level from the Android system APIs.

A data source that uses the Android API causes the Kanzi Studio Preview to terminate on Windows because the Android APIs are unavailable. The approach in this tutorial shows how you can use the Android APIs on Android and still allow the data source to return placeholder data when you use the plugin in the Kanzi Studio Preview.

  1.

In Android Studio, create an interface named `DataProvider`.

```
package com.example.androiddatasourceplugin;

interface DataProvider
{
   float getBatteryLevel();
}

```

  2.

To create a placeholder implementation of the interface to use on non-Android platforms, create a class named `DummyDataProvider`.

```
package com.example.androiddatasourceplugin;

class DummyDataProvider implements DataProvider
{
    @Override
    public float getBatteryLevel()
    {
        return 0.5f;
    }
}

```

  3.

To create an Android implementation of the interface that the application uses when it is running on an Android device, create a class named `AndroidDataProvider`.

```
package com.example.androiddatasourceplugin;

import android.content.Context;
import android.os.BatteryManager;

class AndroidDataProvider implements DataProvider
{
    private final BatteryManager mBatteryManager;

    public AndroidDataProvider(Object context)
    {
        Context androidContext = (Context) context;

        mBatteryManager = (BatteryManager) androidContext.getSystemService(Context.BATTERY_SERVICE);
    }

    @Override
    public float getBatteryLevel()
    {
        int batLevel = mBatteryManager.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY);
        return ((float) batLevel) / 100.0f;
    }
}

```

  4.

Update the `JavaDataSource` to use the new providers.

    - Import the Kanzi classes that provide the functionality for the content that you want create.

```
import com.rightware.kanzi.Platform;

```

    - Add a data member for the data provider:

```
private DataProvider mDataProvider;

```

    - In the `initialize()` method immediately after `super.initialize();` add this code to select the data provider:

```
// Construct the proper DataProvider for the current platform.
if (Platform.isAndroid())
{
    mDataProvider = new AndroidDataProvider(getDomain().getPlatformContext());
}
else
{
    mDataProvider = new DummyDataProvider();
}

```

    - Update the definition of the battery level data object to retrieve the value from the interface:

```
root.addChild(DataObjectReal.create(domain, BATTERY_LEVEL, mDataProvider.getBatteryLevel()).get());

```

7.

In Android Studio, build and run the app.

When you run the application on an Android device, the battery widget shows the current battery level of that device.

## Create a two-way data source

In this section you create a widget that you can use to control the silent mode of an Android device.

To create a two-way data source:

1.

In Android Studio, update the data source to include the silent mode related information:

  1.

In the `DataProvider` interface, add:

```
boolean isSilentMode();
void setSilentMode(boolean enabled);

```

  2.

In the `DummyDataProvider` class, add:

```
private boolean mSilentMode = false;

@Override
public boolean isSilentMode()
{
   return mSilentMode;
}

@Override
public void setSilentMode(boolean enabled)
{
   mSilentMode = enabled;
}

```

  3.

In the `AndroidDataProvider` class:

    - Import the Android classes that provide the functionality for the content that you want create.

```
import android.app.NotificationManager;
import android.media.AudioManager;
import android.provider.Settings;

```

    - Add this member:

```
private final AudioManager mAudioManager;

```

    - In the constructor, add this code to initialize the audio manager and request the notification policy access:

```
// Request notification policy access if not granted.
// This is required to change ringer mode when Do Not Disturb is active.
NotificationManager notificationManager = (NotificationManager) androidContext.getSystemService(Context.NOTIFICATION_SERVICE);
if (!notificationManager.isNotificationPolicyAccessGranted())
{
   Intent intent = new Intent(Settings.ACTION_NOTIFICATION_POLICY_ACCESS_SETTINGS);
   intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
   androidContext.startActivity(intent);
}

mAudioManager = (AudioManager) androidContext.getSystemService(Context.AUDIO_SERVICE);

```

    - Add these methods:

```
@Override
public void setSilentMode(boolean enabled)
{
   if (enabled)
   {
      mAudioManager.setRingerMode(AudioManager.RINGER_MODE_VIBRATE);
   }
   else
   {
      mAudioManager.setRingerMode(AudioManager.RINGER_MODE_NORMAL);
   }
}

@Override
public boolean isSilentMode()
{
   int ringerMode = mAudioManager.getRingerMode();
   return ringerMode == AudioManager.RINGER_MODE_VIBRATE || ringerMode == AudioManager.RINGER_MODE_SILENT;
}

```

  4.

In the `JavaDataSource` class:

    - Import the Kanzi classes that provide the functionality for the content that you want create.

```
import com.rightware.kanzi.DataObjectBool;

```

    - Add this member:

```
static String SILENT_MODE = "SilentMode";

```

    - In the `initialize()` function update the data source:

```
ObjectRef<DataObjectBool> silentModeRef =
    DataObjectBool.create(domain, SILENT_MODE, mDataProvider.isSilentMode());
root.addChild(silentModeRef.get());

// Register a Notification handler to update silent mode when Data Source changes.
DataObjectBool silentMode = silentModeRef.get();
silentMode.addModifiedNotificationHandler(new ModifiedSubscriptionFunction() {
    @Override
    public void handle()
    {
        mDataProvider.setSilentMode(silentMode.getValue());
    }
});

```

  5.

In the androiddatasourceplugin > `manifests` > `AndroidManifest.xml` and app > `manifests` > `AndroidManifest.xml` files, add these permissions:

```
<uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS"/>
<uses-permission android:name="android.permission.ACCESS_NOTIFICATION_POLICY"/>

```

  6.

In the Gradle tool window in androiddatasource > androiddatasourceplugin > Tasks > kanzi, right-click either exportJarDebug or exportJarRelease and select Run.

Android Studio builds the Kanzi Engine data source plugin JAR that you use in Kanzi Studio.

2.

In Kanzi Studio, update the plugin:

  1.

In the Library > Kanzi Engine Plugins, right-click the AndroidDataSource plugin and select Update Kanzi Engine Plugin.

This way you update and load the plugin that includes the changes that you made in the Android Studio plugin project.
  2.

To take the plugin changes into use, restart the Preview.

3.

In Kanzi Studio in the Data Sources window, click the Refresh button to read the updated data source contents from the plugin.
4.

In Kanzi Studio, create the user interface for the Silent Mode widget:

  1.

In the Node Tree, press Alt and right-click the Controls node, create an Empty Node 2D node, and name it Silent Mode Widget. In the Properties, add and set:

    - Layout Width to 150
    - Layout Height to 200
    - Layout.Item > Horizontal Margin property Left property field to 40

  2.

In the Node Tree, press Alt and right-click the Silent Mode Widget node, create an Image node, and name it Icon Silent On. In the Properties, add and set:

    - Image to + Import Imageâ¦ and select `<KanziWorkspace>/Tutorials/Android data source/Assets/bell-off.png`
    - Layout Width to 150
    - Layout Height to 150

  3.

In the Properties, add a binding and set:

    - Property to Visible
    - Expression to

```
BOOL({DataContext.SilentMode})

```

Click Save.

With this binding you make the Icon Silent On image visible when the value of the SilentMode data object is `true`.
  4.

In the Node Tree, duplicate the Icon Silent On node and rename it to Icon Silent Off.
  5.

In the Node Tree, select the Icon Silent Off node. In the Properties:

    - Click the binding and in the Binding Editor add `!` to the beginning of the binding expression.

Click Save.

With this binding you make the Icon Silent Off image visible when the value of the SilentMode data object is `false`.
    - Set the Image property to + Import Imageâ¦ and select `<KanziWorkspace>/Tutorials/Android data source/Assets/bell.png`.

  6.

From the Asset Packages > Factory Content, drag the Toggle Button to the Node Tree and drop it on the Silent Mode Widget.

You use this toggle button to control the silent mode.
  7.

In the Node Tree, select the Toggle Button node. In the Properties:

    - Create a binding and set:

      - Binding Mode to Two way
      - Property to Toggle State
      - Expression to

```
{DataContext.SilentMode}

```

Click Save.

With this binding you create a two-way connection between the toggle state of the Toggle Button node and the SilentMode data object.
    - Add the Vertical Alignment property and set it to Bottom

5.

In Kanzi Studio, select File > Export > Export KZB.
6.

In Android Studio, build, and run the app.

When you run the application on an Android device, the Silent Mode widget shows the icon that indicates the silent mode status of that device.

## Update data sources based on external changes

In the previous section, you added the functionality to read constant data from an Android device at application startup. In this section, you set the data source to respond to Android callbacks and update the data source when the silent mode or battery level changes.

To update data sources based on external changes:

1.

Create an interface named `DataChangeListener`.

This interface accepts data changes when they occur.

```
package com.example.androiddatasourceplugin;

interface DataChangeListener {
    void updateBatteryLevel(float batteryLevel);
    void updateSilentMode(boolean isSilent);
}

```

2.

Modify the `AndroidDataProvider` class to receive the updated data from Android.

  - Import the Android classes that provide the functionality for the content that you want create.

```
import android.content.BroadcastReceiver;
import android.content.Intent;
import android.content.IntentFilter;

```

  - Add a member that holds a reference to a `DataChangeListener`.

```
private final DataChangeListener mDataChangeListener;

```

  - Modify the `AndroidDataProvider` constructor to receive and store the `DataChangeListener`.

```
public AndroidDataProvider(Object context, DataChangeListener listener)
{
   mDataChangeListener = listener;

```

  - Add listener callbacks for the silent mode and battery level:

```
// Battery level listener
private final BroadcastReceiver mBatteryReceiver = new BroadcastReceiver() {
    @Override
    public void onReceive(Context context, Intent intent)
    {
        int level = intent.getIntExtra(BatteryManager.EXTRA_LEVEL, -1);
        int scale = intent.getIntExtra(BatteryManager.EXTRA_SCALE, -1);
        float batteryLevel = level / (float) scale;

        mDataChangeListener.updateBatteryLevel(batteryLevel);
    }
};

// Ringer mode listener that indicates whether silent mode is enabled.
private final BroadcastReceiver mRingerModeReceiver = new BroadcastReceiver() {
    @Override
    public void onReceive(Context context, Intent intent)
    {
        int ringerMode = intent.getIntExtra(AudioManager.EXTRA_RINGER_MODE, AudioManager.RINGER_MODE_NORMAL);
        boolean isSilent = ringerMode == AudioManager.RINGER_MODE_VIBRATE || ringerMode == AudioManager.RINGER_MODE_SILENT;
        mDataChangeListener.updateSilentMode(isSilent);
    }
};

```

  - To register the callbacks with Android, add this code to the `AndroidDataProvider` constructor:

```
// To get battery changes, register the battery receiver.
androidContext.registerReceiver(mBatteryReceiver, new IntentFilter(Intent.ACTION_BATTERY_CHANGED));

// To get ringer mode changes, register the ringer mode receiver.
androidContext.registerReceiver(mRingerModeReceiver, new IntentFilter(AudioManager.RINGER_MODE_CHANGED_ACTION));

```

3.

Modify `JavaDataSource` class to handle data updates:

  - Change the class to implement the `DataChangeListener` interface.

```
public class JavaDataSource extends DataSource implements DataChangeListener {

```

  - Add an implementation of the `DataChangeListener` interface.

```
private boolean mUpdateInProgress = false;

@Override
public void updateBatteryLevel(float batteryLevel)
{
    DataObjectReal batteryObject =
        (DataObjectReal) mRoot.get().lookupDataContext(BATTERY_LEVEL);
    if (batteryObject != null)
    {
        mUpdateInProgress = true;
        batteryObject.setValue(batteryLevel);
        mUpdateInProgress = false;
    }
}

@Override
public void updateSilentMode(boolean isSilent)
{
    DataObjectBool silentModeObject =
        (DataObjectBool) mRoot.get().lookupDataContext(SILENT_MODE);
    if (silentModeObject != null)
    {
        mUpdateInProgress = true;
        silentModeObject.setValue(isSilent);
        mUpdateInProgress = false;
    }
}

```

  - In the `initialize()` method, add `this` as an argument to the `AndroidDataProvider` constructor.

```
mDataProvider = new AndroidDataProvider(getDomain().getPlatformContext(), this);

```

  - In the `initialize()` method, modify the existing notification handler to add the `mUpdateInProgress` variable to prevent recursive updates.

```
silentMode.addModifiedNotificationHandler(new ModifiedSubscriptionFunction() {
    @Override
    public void handle()
    {
        if (!mUpdateInProgress)
        {
            mDataProvider.setSilentMode(silentMode.getValue());
        }
    }
});

```

4.

In Android Studio, build, and run the app.

When you run the application on an Android device, the Silent Mode widget updates when the ringer mode changes. To test this, enable and disable silent mode through the device user interface, or use the toggle button in the Silent Mode widget.
**Note:** To change the ringer mode when Do Not Disturb is active, the application requires notification policy access permission. On the first launch, the application will prompt you to grant this permission.

## Whatâs next?

In this tutorial you learned how to:

- Create a data source using Kanzi Java API.
- Use Android APIs to back the data source.
- Ensure compatibility with the Kanzi Studio Preview where the Android APIs are not available.

To learn more about how to use Kanzi Android framework (droidfw) and Java API see:

- Developing with the Kanzi Android framework (droidfw)
- Using Java and Kotlin
- Kanzi Android framework API reference
- Kanzi Engine Java API reference
