---
title: Tutorial: Kanzi Engine API advanced use
source: https://docs.kanzi.com/4.1.0/en/tutorials/programmer-tutorial/programmer-tutorial.html
---

# Tutorial: Kanzi Engine API advanced use


While you can create a Kanzi application using only Kanzi Studio, you can use the Kanzi Engine API to add logic to your Kanzi application.

For example, to create a phone book where users can add, edit, and remove entries, you create a template for the phone book entries using prefabs in Kanzi Studio, but use the Kanzi Engine API to add, edit, and remove the entries, and load images from the device running the application.

In this tutorial you create a Kanzi application using both Kanzi Studio and Kanzi Engine API. The tutorial introduces you to:

- Kanzi application framework.
- Kanzi Studio kzb file and how to use the Kanzi Engine API to add logic to the application you created in Kanzi Studio.
- Properties, resource IDs, URLs, and aliases.
- Input manipulators to define the input events that nodes generate.
- Event handlers to receive and process the messages.


This video shows the result of the tutorial.

Before you start this tutorial, make sure you have your Kanzi development environment set up. Install:

- CMake 3.25 or newer
- Visual Studio 2022 with the latest updates


- Android Studio. See Deploying Kanzi applications to Android.

You use Android Studio to deploy your Kanzi application to an Android device.


This tutorial assumes that you understand the basics of working with Kanzi Studio. The best entry points for getting familiar with Kanzi Studio are:

- Tutorial: Create a simple in-vehicle infotainment application
- Tutorial: Hello world!
- Tutorial: Getting started with Kanzi Studio


Start with the tutorial
