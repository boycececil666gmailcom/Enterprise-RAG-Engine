---
title: Programming Activities with Code Behind
source: https://docs.kanzi.com/4.1.0/en/working-with/activities/code-behind.html
---

# Programming Activities with Code Behind

Code Behind is a workflow where you associate code with an instance of an Activity instead of a type.

In Kanzi Studio in the Activity Browser window you can generate a Code Behind stub for any Activity. This stub is associated with that particular Activity and has access to the properties of that Activity. In Code Behind you can write code that you can associate with the view or controller parts of the model-view-controller pattern.

For example, you can:

- React to changes of the status of an Activity.
- Connect to a remote service when an Activity is activated and save data and disconnect when an Activity is deactivated.
- Install Kanzi command handlers and define their implementations, such as increase the volume when the user presses a button.
- Implement complex UI interaction, such as drag-and-drop of data between UI elements.

Learn how to program Activities with Code Behind workflow by completing the Tutorial: Program Activities with C++ Code Behind.

To program Activities with Code Behind:

- In C++, see Programming Activities with C++ Code Behind.
- In Java, see Programming Activities with Java Code Behind.

## Using Code Behind in the API

For details, see the `CodeBehind` class:

- For C++ in the Kanzi Engine C++ API reference.
- For Java in the Kanzi Engine Java API reference.
