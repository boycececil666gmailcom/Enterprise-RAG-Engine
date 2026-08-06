---
title: Android System Alert example
source: https://docs.kanzi.com/4.1.0/en/examples/systemalert/systemalert.html
---

# Android System Alert example


This example shows how you can integrate a Kanzi Android framework (droidfw) view in an Android System Alert window.
## Getting the example


To get the example, in the Kanzi Studio Quick Start window, click Projects and select the Examples tab. Next to the SystemAlert example, click .

Kanzi Studio downloads the example to the `<KanziWorkspace>/Examples/Android/SystemAlert` directory.
## Content of the example


The main activity of the example contains an Android button and does not contain Kanzi content. When you click the button, the example shows an Android System Alert window that has an embedded Kanzi view.

To dismiss the alert, click the alert. When you dismiss the alert, the Kanzi main loop is inactive and does not consume any CPU.
## Running the example


To run the example:

1.

Connect your Android device to your computer.
2.

In the Kanzi Studio Quick Start window, click Projects and select the Examples tab. Next to the SystemAlert example, click Open.
3.

In the main menu, select File > Export > Build Android Package.

Kanzi Studio creates an Android package from your Kanzi Studio project and deploys it to your Android device.
4.

On your Android device, start the **SystemAlert** application.
5.

Enable the Display over other apps permission for the SystemAlert application:

  1.

When the application starts, Android shows the Display over other apps permission screen.
  2.

From the list of applications, select the SystemAlert application.
  3.

Set the Allow display over other apps permission to enabled.
  4.

Click the Back button to exit the permission screens.

6.

In the application, click the **SHOW ALERT** button to launch the System Alert window.
7.

Press anywhere on the alert to dismiss it.
