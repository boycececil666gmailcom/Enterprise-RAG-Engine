---
title: Project
source: https://docs.kanzi.com/4.1.0/en/reference/node-and-resource-reference/project-reference.html
---

# Project

## Project properties

|

Name |

Description |

Inherited |

Exported to Kanzi Engine |
|

Name |

Name of the project item |

No |

No |
|

Binary Export Directory |

Directory name for the KZB files |

No |

No |
|

Application Export Directory |

Directory into which KZB Player version of the project is exported. |

No |

No |
|

Target Shader Family |

The shader family used when exporting shaders. When Target Graphics API is Vulkan 1.2, only Vulkan shaders are exported. |

No |

No |
|

KZB Endianness |

Endianness of the KZB data. Use the endianness of the target device for optimal performance. |

No |

No |
|

Optimize Meshes |

Whether to perform the vertex cache optimization for exported meshes. Kanzi Studio sets the vertex cache of the meshes to the value you set in the Target Vertex Cache Size property. |

No |

No |
|

Target Vertex Cache Size |

The size in bytes of the vertex cache on the target hardware. Kanzi Studio uses this value when you enable the Optimize Meshes property. |

No |

No |
|

Plot Animations |

Whether to plot non-linear animations into linear animations during export. |

No |

No |
|

Default Vertex Attribute Data Type |

The default data type used in model vertex buffers. Half-float decreases mesh data size by half, but decreases the accuracy too. |

No |

No |
|

Round up Image Dimensions to Nearest Power of Two |

Whether to round up the width and height of images to the nearest power of two during kzb file export. For example, when you enable this property, Kanzi Studio exports a 40 x 30 pixel image to the kzb file in the size 64 x 32 pixels. |

No |

No |
|

Remove ICC Profile From PNG Images |

Whether to remove the ICC profile from the PNG images files during kzb file export. |

No |

No |
|

PNG Compression Level |

Affects how PNG images are compressed when exported to kzb. Can be overridden per image. |

No |

No |
|

Export Shader Source Code |

If all shaders in the project are binary shaders and you do not use the shader binary cache, you can reduce the size of the kzb file by disabling this property. |

No |

No |
|

Property Namespace |

The property namespace to prepend to the newly created custom property types in this project. When you change the value of this property, Kanzi Studio asks you whether you want to change the existing custom property type names which use this namespace. |

No |

No |
|

Color Workflow |

The color workflow used when Kanzi Studio embeds color into the kzb file: * In Linear mode Kanzi Studio converts all color values to linear color space before exporting them to the kzb file. This is the default. * In Standard mode Kanzi Studio does not modify the color values. When you change the value of this property, the Preview restarts. |

No |

No |
|

Default Build Configuration |

Kanzi Studio uses this configuration to build the project. You can add new build configurations in the Library > Build Configurations. |

No |

No |
|

Default Material |

The material that is used in newly created models and imported models without a material. |

No |

No |
|

Default Texture |

The texture that is used for new Image nodes and materials that use textures. |

No |

No |
|

Default Cubemap Texture |

The cubemap texture that Kanzi Studio uses for new materials that use cubemaps. |

No |

No |
|

Import Material Type |

The material type under which the materials are imported from 3D asset files, such as COLLADA. âAutomaticâ option assigns imported materials under different material types depending on their material effect. Note that only basic effects such as Phong and textured Phong are recognized. |

No |

No |
|

Premultiply Alpha |

Whether to premultiply alpha for images during .kzb file export. You can override this project-wide setting in the Properties of each image. |

No |

No |
|

Description |

Add a description of the purpose of this item. To export descriptions to a plain text file, select File > Export > Export Descriptions. When you export the kzb file, this description is not included in the exported file. |

No |

No |
|

Preview Build Configuration |

Use release setting for performance and debug setting for debugging Kanzi engine plugins. Kanzi engine plugins must have a DLL available with the same ES wrapper, build configuration and Visual Studio version as specified for the preview. |

No |

No |
|

Preview Visual Studio Version |

Preview Visual Studio version setting is required for Kanzi engine plugin compatibility. Kanzi engine plugins must have a DLL available with the same ES wrapper, build configuration and Visual Studio version as specified for the preview. |

No |

No |
|

Preview Graphics API Configuration |

Preview Graphics API Configuration is used to select the graphics API used for rendering within Preview. |

No |

No |
|

Preview Working Directory |

The working directory of preview. Accepts relative path from Kanzi Studio project directory or an absolute path. |

No |

No |
|

Java Project |

Whether the project contains Java plugins |

No |

No |
|

Full Screen Preview Layer |

Whether or not to display the preview root layer as fullscreen |

No |

No |
|

Show Children in Layer Thumbnails |

Whether to show the child items in the thumbnails of the layer view that have direct content, such as image and viewport. |

No |

No |
|

Binary File Name |

Name for the binary (KZB) file. <projectname>.kzb by default |

No |

No |
|

Descriptions File Name |

Name for the file into which item descriptions are exported by default |

No |

No |
|

Target Graphics API |

The version of OpenGL used when exporting shader parameters. |

No |

No |
|

Font Engine |

Sets the font engine that Kanzi Studio Preview uses to render text: * FreeType uses the FreeType rasterizer, HarfBuzz shaper, and ICU bidirectional library, and libunibreak for line breaking. This is the default value. * iType uses the Monotype iType rasterizer and WorldTypeÂ® Shaperâ¢ for shaping. * None to not load a font engine. When you do not load a font engine, the Preview does not render the text in your application. |

No |

No |
|

Is Asset Package |

When enabled, saving this project will export a manifest file that is used for locating importable assets in this project. Mark the assets to be exported with âExport In Asset Packageâ property. |

No |

No |
|

Resource Keep Alive Behavior |

The keep-alive behavior to be inherited by resources in the project. Can be used to deny unloading of resources. |

No |

No |
|

Material Type Keep Alive Behavior |

The keep-alive behavior to be inherited by material types in project. Can be used to deny unloading of material types. |

No |

No |
|

Start Time |

The starting time of the global timeline. |

No |

No |
|

End Time |

The ending time of the global timeline. |

No |

No |
## Project available properties

|

Name |

Description |

Inherited |

Exported to Kanzi Engine |
|

Description |

Add a description of the purpose of this item. To export descriptions to a plain text file, select File > Export > Export Descriptions. When you export the kzb file, this description is not included in the exported file. |

No |

No |
|

Preview Background Color |

Sets the background color of the Preview for this project.

When you do not set this property, the project uses the color that you set in **Edit** > **User Preferences** > **Preview** > **Background Color**.  |

No |

No |
|

Resource Visibility Across Projects |

Sets whether the resources of this project are available to referencing projects: * Private makes the resources available only to this project. This is the default value. * Public makes the resources available in the dropdown menus of referencing projects. To override this setting for an individual resource, add and set the Visibility Across Projects property for that resource. |

No |

No |
|

Thumbnail |

Sets the thumbnail that Kanzi Studio shows in the Quick Start window. |

No |

No |
## Project messages

|

Name |

Description |

Inherited |

Exported to Kanzi Engine |
|

Activity Host: Activity Prefab Attached |

An Activity Host sends this message when it attaches the prefab of the Activity that is activated. |

No |

Yes |
|

Activity Host: Activity Prefab Detached |

An Activity Host sends this message when it detaches the prefab of the Activity that is deactivated. |

No |

Yes |
|

Activity: Activated |

An Activity sends this message when it is activated. |

No |

Yes |
|

Activity: Activating |

An Activity sends this message when it is in the activating state. |

No |

Yes |
|

Activity: Deactivated |

An Activity sends this message when it is deactivated. |

No |

Yes |
|

Activity: Deactivating |

An Activity sends this message when it is in the deactivating state. |

No |

Yes |
|

Activity: Status Changed |

An Activity sends this message when the value of its Activity Status property changes. |

No |

Yes |
|

Animation Player: Completed |

Occurs when an Animation Player completes animation playback. |

No |

Yes |
|

Animation Player: Started |

Occurs when an Animation Player starts animation playback. |

No |

Yes |
|

Animation Player: Stopped |

Occurs when an Animation Player stops animation playback. |

No |

Yes |
|

Button: Cancel |

Occurs when a user lifts their finger outside of a Button that they previously pressed. |

No |

Yes |
|

Button: Click |

Occurs when a user lifts their finger on top of a Button that they previously pressed and when the time set by the Auto Press Interval property in the pressed Button expires. |

No |

Yes |
|

Button: Down |

Occurs when the user presses down the Button. |

No |

Yes |
|

Button: Enter |

Button: Enter trigger is set off: * When the user presses down the button. * When the user presses down the button, moves the pointer outside of the button area, and then moves the pointer back to the button area while still holding down the pointer. |

No |

Yes |
|

Button: Leave |

Button: Leave trigger is set off: * When the user presses down the button and then lifts the pointer. * When the user presses down the button and then moves the pointer outside of the button area. * When the user sets off a **Button: Long Press** trigger. |

No |

Yes |
|

Button: Long Press |

Occurs when the user presses down a Button and holds the Button pressed for the amount of milliseconds defined in the Hold Interval property of that Button. |

No |

Yes |
|

Click: Begin |

Occurs when the user presses a hit-testable node with a Click Manipulator.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |
|

Click: Cancel |

Occurs when the user first presses a hit-testable node with a Click Manipulator, then moves the pointer outside of the node area, and lifts the pointer.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |
|

Click: Click |

Occurs when the user presses and releases a hit-testable node with a Click Manipulator, while the pointer is still within the node area and Kanzi does not recognize another gesture.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |
|

Click: Enter |

Occurs when the user presses a hit-testable node with a Click Manipulator and then every time the user moves the pointer on top of that node while still holding down the pointer.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |
|

Click: Leave |

Occurs when the user presses a hit-testable node with a Click Manipulator and then every time the user moves the pointer outside of that node.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |
|

Command: Command |

Command message arguments |

No |

Yes |
|

Data Trigger |

Monitors changes in properties and data source values. Use a Data Trigger to apply an action to either set a property value of a target node or activate an Activity node. |

No |

Yes |
|

Drag and Drop: Drag and Drop Canceled |

Occurs when focus moves away from the node during the drag-and-drop gesture. |

No |

Yes |
|

Drag and Drop: Drag and Drop Finished |

Occurs when the user lifts their finger after starting the drag-and-drop gesture. |

No |

Yes |
|

Drag and Drop: Drag and Drop Moved |

Occurs when the user moves their finger after starting the drag-and-drop gesture. |

No |

Yes |
|

Drag and Drop: Drag and Drop Started |

Occurs when the user holds their finger for 500ms on the node. |

No |

Yes |
|

Focus: About To Gain Focus |

Kanzi sends this message before a focusable node receives focus. |

No |

Yes |
|

Focus: About To Lose Focus |

Kanzi sends this message before the focused node loses focus. |

No |

Yes |
|

Focus: Focus Entered Focus Scope |

When focus enters a focus scope, Kanzi sends this message to the focus scope node that contains the node that gains focus. |

No |

Yes |
|

Focus: Focus Gained |

Kanzi sends this message to the node that received focus. |

No |

Yes |
|

Focus: Focus Left Focus Scope |

When focus leaves a focus scope, Kanzi sends this message to the focus scope node that contains the node that loses focus. |

No |

Yes |
|

Focus: Focus Lost |

Kanzi sends this message to the node that lost focus. |

No |

Yes |
|

Focus: Input Outside Overlay |

Kanzi sends this message to an overlay focus scope when the application area outside the boundaries of that overlay receives input. |

No |

Yes |
|

Focus: Overlay Brought To Front |

Occurs when an overlay focus scope becomes the foremost overlay scope in the overlay focus scope stack. |

No |

Yes |
|

Focus: Overlay Gained Focus |

When an overlay scope gains focus, Kanzi sends this message to the overlay scope node that contains the node that gains focus. |

No |

Yes |
|

Focus: Overlay Lost Focus |

When an overlay scope loses focus, Kanzi sends this message to the overlay scope node that contains the node that loses focus. |

No |

Yes |
|

Focus: Overlay Sent To Back |

Occurs when an overlay focus scope is no longer the foremost overlay scope in the overlay focus scope stack. |

No |

Yes |
|

Key Input: Key Canceled |

Occurs when Kanzi recognizes a key-canceled gesture. A key-canceled gesture occurs when Kanzi recognizes that the user canceled a gesture. |

No |

Yes |
|

Key Input: Key Pressed |

Occurs when Kanzi recognizes a key-pressed gesture. A key-pressed gesture occurs when Kanzi recognizes a key event that contains all the elements that compose that gesture. |

No |

Yes |
|

Key Input: Key Released |

Occurs when Kanzi recognizes a key-released gesture. A key-released gesture occurs when Kanzi recognizes the release of one of the elements that compose that gesture. |

No |

Yes |
|

Key Navigation: Key Navigation Canceled |

Occurs when the key-pressed gesture is canceled for the navigation direction. |

No |

Yes |
|

Key Navigation: Key Navigation Finished |

Occurs when Kanzi recognizes the key-released gesture for the navigation direction. To capture key navigation gestures for a node, create a Navigation Manipulator component in that node. |

No |

Yes |
|

Key Navigation: Key Navigation Started |

Occurs when Kanzi recognizes the key-pressed and key repeat gestures for the navigation direction. To capture key navigation gestures for a node, create a Navigation Manipulator component in that node. |

No |

Yes |
|

List Box: Item Loaded |

Occurs when an item is loaded to the working memory. To set how many items you want to keep loaded in the working memory at a time, use the Keep Alive Item Count property. |

No |

Yes |
|

List Box: Item Selected |

Occurs when an item is selected. |

No |

Yes |
|

List Box: Item Unloaded |

Occurs when an item is unloaded from the working memory. To set how many items you want to keep loaded in the working memory at a time, use the Keep Alive Item Count property. |

No |

Yes |
|

List Box: Scroll Finished |

Occurs when the List Box stops scrolling. |

No |

Yes |
|

List Box: Scroll Started |

Occurs when the List Box starts to scroll. |

No |

Yes |
|

List Box: Scrolled |

Occurs when the List Box scrolls. |

No |

Yes |
|

List Box: Target Changed |

Occurs when List Box gets a new target item. |

No |

Yes |
|

List Box: User Scroll Finished |

Occurs when the application user stops scrolling the List Box. |

No |

Yes |
|

List Box: User Scroll Started |

Occurs when the application user starts to scroll the List Box. |

No |

Yes |
|

Long Press: Long Press |

Occurs when the user presses a hit-testable node with a Long-Press Manipulator and holds the press for the time that you set in the Long-Press Manipulator.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |
|

Long Press: Long Press Cancel |

Occurs during the long-press gesture when the user moves the focus away from a hit-testable node with a Long-Press Manipulator.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |
|

Message Trigger |   |

No |

Yes |
|

Multi-Click: Intermediate Click |

Occurs when the user presses and releases a hit-testable node with a Multi-Click Manipulator that is set to send messages for intermediate clicks.

To set a Multi-Click Manipulator to send messages for intermediate clicks, in the Multi-Click Manipulator enable the Send Intermediate Click Messages property.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |
|

Multi-Click: Multi-Click |

Occurs when the user presses and releases a hit-testable node with a Multi-Click Manipulator a specified number of times (default 2) within a set amount of time (default 250 ms) between presses.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |
|

Multi-Click: Multi-Click Canceled |

Occurs during the multi-click gesture when the user moves the focus away from a hit-testable node with a Multi-Click Manipulator.

You cannot use this trigger with nodes that handle input by default, such as Button and Toggle Button nodes.  |

No |

Yes |
|

On Attached |

This trigger is set off when the item is initialized. For example, when you add a node to the node tree, or enter a state that contains this trigger. |

No |

Yes |
|

On Property Change |

Occurs when a property is changed |

No |

Yes |
|

On Timer |

Occurs when timer interval is elapsed |

No |

Yes |
|

Page (deprecated): Activated (deprecated) |

Page has been activated. |

No |

Yes |
|

Page (deprecated): Deactivated (deprecated) |

Page has been deactivated. |

No |

Yes |
|

Page Host (deprecated): Page Navigation Finished (deprecated) |

Page host has finished navigation process. |

No |

Yes |
|

Page Host (deprecated): Page Navigation Started (deprecated) |

Page host has started navigation process. |

No |

Yes |
|

Pan: Pan Canceled |

Occurs when focus moves away from the node during the pan gesture. |

No |

Yes |
|

Pan: Pan Entered |

Occurs when the pan gesture enters the node to which the Pan Manipulator is attached. |

No |

Yes |
|

Pan: Pan Finished |

Occurs when the user lifts their finger after Kanzi recognizes a pan gesture. |

No |

Yes |
|

Pan: Pan Left |

Occurs when the pan gesture leaves the node to which the Pan Manipulator is attached. |

No |

Yes |
|

Pan: Pan Moved |

Occurs when the user changes the position of their finger and that change exceeds the recognition thresholds. |

No |

Yes |
|

Pan: Pan Started |

Occurs when the user presses down their finger on the node. If the user lifts their finger before exceeding the position change threshold, Kanzi cancels the pan gesture. |

No |

Yes |
|

Pinch: Pinch Canceled |

Occurs when focus moves away from the node during the pinch gesture. |

No |

Yes |
|

Pinch: Pinch Finished |

Occurs when the user lifts their finger after Kanzi recognizes a pinch gesture. |

No |

Yes |
|

Pinch: Pinch Moved |

Occurs when the user changes the position of their finger and that change exceed the scale or rotation threshold. |

No |

Yes |
|

Pinch: Pinch Started |

Occurs when the user presses down their finger. If the user lifts their finger before it exceeds the scale or rotate threshold, Kanzi cancels the pinch. |

No |

Yes |
|

Prefab View: Asynchronous Load Completed |

Occurs when asynchronous loading of resources from a prefab has been finished. |

No |

Yes |
|

Property Target Easing Interpolator: Easing Interpolation Completed |

Occurs when Property Target Easing Interpolator completes its interpolation. |

No |

Yes |
|

Property Target Interpolator: Interpolation Completed |

Occurs when property target interpolator completes interpolation. |

No |

Yes |
|

Range: Value Change Finished |

Occurs when the range value stops changing. |

No |

Yes |
|

Range: Value Change Started |

Occurs when the range value starts changing. |

No |

Yes |
|

Range: Value Changed |

Occurs when the range value has changed. |

No |

Yes |
|

Scroll View: Scroll Ended |

Occurs when the scroll position of a Scroll View node stops changing. |

No |

Yes |
|

Scroll View: Scroll Started |

Occurs when the scroll position of a Scroll View node starts changing. |

No |

Yes |
|

Scroll View: Scroll Zoomed |

Occurs when the zoom level of a Scroll View node changes. |

No |

Yes |
|

Scroll View: Scrolled |

Occurs when the scroll position of a Scroll View node changes. |

No |

Yes |
|

Scroll View: Snap Request |

Occurs when a Scroll View node requests snapping target from the hosting component. |

No |

Yes |
|

Scroll View: User Scroll Ended |

Occurs when the user stops scrolling a Scroll View node. |

No |

Yes |
|

Scroll View: User Scroll Started |

Occurs when the user starts scrolling a Scroll View node. |

No |

Yes |
|

State Manager: Entered State |

Occurs when a state manager has entered a state. |

No |

Yes |
|

State Manager: Left State |

Occurs when a state manager has left a state. |

No |

Yes |
|

State Manager: Transition Finished |

Occurs when a state manager finishes a transition to a state. |

No |

Yes |
|

State Manager: Transition Started |

Occurs when a state manager begins a transition to a state. |

No |

Yes |
|

Text Box: Composition Text Changed |

Occurs when the text produced in an Input Method Editor is updated in a Text Box node. |

No |

Yes |
|

Text Box: Composition Text Committed |

Occurs: * When the text produced in an Input Method Editor is committed to the cached text in a Text Box node. * When a trigger executes the **Text Box: Commit Composition Text** action. |

No |

Yes |
|

Text Box: Cursor Moved |

Occurs when the user moves the cursor in a Text Box node. |

No |

Yes |
|

Text Box: Editing Finished |

Occurs when a Text Box node leaves the editing state after the user modified the text content. |

No |

Yes |
|

Text Box: Editing Started |

Occurs when the user makes the first modification to the text in a Text Box node that is in the editing state. |

No |

Yes |
|

Text Box: Entered Editing State |

Occurs when a Text Box node enters the editing state. |

No |

Yes |
|

Text Box: Input Method Action |

Occurs when the user taps the action button on their on-screen keyboard while editing the text in a Text Box node. |

No |

Yes |
|

Text Box: Input Method Available |

Occurs when an input method becomes available to a Text Box node. For example, an on-screen keyboard becomes available when it appears on the screen. |

No |

Yes |
|

Text Box: Input Method Unavailable |

Occurs when the input method that is composing text in a Text Box node becomes unavailable. For example, an on-screen keyboard becomes unavailable when the user hides it. |

No |

Yes |
|

Text Box: Left Editing State |

Occurs when a Text Box node leaves the editing state |

No |

Yes |
|

Text Box: Selection Changed |

Occurs when the user changes the text selection in a Text Box node. |

No |

Yes |
|

Text Box: Selection Cleared |

Occurs when the user clears or resets the text selection in a Text Box node. |

No |

Yes |
|

Text Box: Selection Started |

Occurs when the user starts selecting text in a Text Box node. |

No |

Yes |
|

Text Box: Text Changed |

Occurs when the user changes the text in a Text Box node. |

No |

Yes |
|

Text Box: Text Composition Canceled |

Occurs: * When the text composition in a Text Box node is canceled by Input Method that is in text composition state. * When a trigger executes the **Text Box: Cancel Text Composition** action. |

No |

Yes |
|

Toggle Button Group: Toggled |

Occurs when the toggle state of a **Toggle Button** node in a **Toggle Button Group** node changes. |

No |

Yes |
|

Toggle Button: State Toggled |

Occurs when the toggle state of a Toggle Button changes. |

No |

Yes |
|

Toggle Button: Toggled Off |

Occurs when a Toggle Button is toggled off. |

No |

Yes |
|

Toggle Button: Toggled On |

Occurs when a Toggle Button is toggled on. |

No |

Yes |
