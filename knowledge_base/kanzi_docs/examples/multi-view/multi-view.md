---
title: Mixing Kanzi and Android UI
source: https://docs.kanzi.com/4.1.0/en/examples/multi-view/multi-view.html
---

# Mixing Kanzi and Android UI


This example shows several use cases on how to mix Kanzi and Android UI in an Android application. This example is configured to use the Target Preview on Android.
## Getting the example


To get the example, in the Kanzi Studio Quick Start window, click Projects and select the Examples tab. Next to the Multi_view example, click .

Kanzi Studio downloads the example to the `<KanziWorkspace>/Examples/Android/Multi_view` directory.
## Structure of the example


The application contains these activities:

- NestedScrollableActivity is a Kanzi List Box that is embedded in Android scrollable views, such as `ViewPager2` and `ScrollView`. It shows how gestures work with nested UI controls. See `NestedScrollableActivity.java`.
- OverlappingActivity shows input event propagation when a Kanzi view overlaps another view. When Kanzi UI does not consume an input event, Kanzi propagates the event to the lower layers of the Android UI. See `OverlappingActivity.java`.
- EditTextActivity shows how to use the Android `EditText` to provide input for Kanzi UI. See `EditTextActivity.java`.
- ThemeActivity shows how Kanzi themes work with Kanzi views. See `ThemeActivity.java`.
- NoKanziUIActivity contains only Android UI. Kanzi does not require being present in every activity of the application. See `NoKanziUIActivity.java`.


To navigate between these activities, use the Next button.

When you run the example on a device with two displays, the application shows Kanzi UI on both displays.
## Running the example


To run the example:

1.

Connect your Android device to your computer.
2.

In the Kanzi Studio Quick Start window, click Projects and select the Examples tab. Next to the Multi_view example, click Open.
3.

In the main menu select File > Export > Build Android Package.

Kanzi Studio creates an Android package from your Kanzi Studio project, deploys, and runs it on your Android device.
