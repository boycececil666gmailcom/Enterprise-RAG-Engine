---
title: Setting the Screen node
source: https://docs.kanzi.com/4.1.0/en/working-with/screens/screens.html
---

# Setting the Screen node

Use the Screen node to set the metrics and the content of the screen of the target device on which your Kanzi application is rendered.

You can:

- Set the Screen size of your application so that its size is fixed or dynamically resizable. See Setting the size of the Screen node.
- Set the color of the areas outside the Screen node. See Setting the color of areas outside the Screen node.
- Make your application fill the entire device screen. See Making an application that fills the entire screen.

## Setting the size of the Screen node

To set the size of the Screen node, in the Node Tree select the Screen node and in the Properties set:

- For a fixed size window, set either:

  - Screen Resolution to a specific resolution
  - Metrics Type to Absolute, and define the absolute Width and Height

- For a resizable window, set Metrics Type to Relative and define the relative Width and Height.

## Setting the color of areas outside the Screen node

When the resolution of the device screen is larger than the resolution of an application with a fixed size of the Screen node, you can set the color of the areas outside of the Screen node with the Screen Clear Color property.

When you use the Screen Clear Color property, and you have Viewport 2D nodes in the node tree, you can render them with a render pass that does not perform color clear. The Screen performs the color clear already.

Set the Screen Clear Color when your Kanzi application does not use copy swap behavior, and:

- Target hardware uses tile-based architecture

or

- Target hardware does not use tile-based architecture, but significant screen area is not filled with opaque rendering, such as with a background image.

To set the color of areas outside the Screen node:

1.

In the Node Tree select the Screen node.
2.

In the Properties set the Screen Clear Color property to the color you want to use for the areas outside of the Screen node.

When you set the Screen Clear Color property, Kanzi clears the screen outside of the Screen node with the color you set before it renders anything else.

## Making an application that fills the entire screen

To make a Kanzi application that fills the entire device screen, in the Node Tree select the Screen node, and in the Properties set:

- Screen Resolution property to Custom
- Metrics Type to Relative
- Width and Height to 1

When you need to override the above settings in the root node of your application, such as RootNode:

1.

In the Node Tree select the root node.
2.

In the Properties add these properties:

  - Layout Width
  - Layout Height
  - Aspect Ratio

## Using the Screen node in the API

To set the locale of a Screen node:

```
// Switch locale to en-US.
screen->setLocale("en-US");

```

To activate a theme for a Screen node:

```
// Activate the theme named "MyTheme" from the theme group named "MyThemeGroup".
screen->activateTheme("kzb://project/Themes/MyThemeGroup/MyTheme");

```

To set a Screen node to handle user input and manage the key focus:

```
// Instantiate the Input Manager and the Focus Manager.
auto inputManager = make_unique<InputManager>(screen->getDomain());
auto focusManager = make_unique<FocusManager>();

// Set the Input Manager and the Focus Manager.
// You must set the managers before you attach the Screen.
screen->setInputManager(inputManager.get());
screen->setFocusManager(focusManager.get());

// Attach the Screen.
screen->attach();

```

For details, see the `Screen` class.
## Screen property types and messages

For a list of the available property types and messages for the Screen node, see Screen.
