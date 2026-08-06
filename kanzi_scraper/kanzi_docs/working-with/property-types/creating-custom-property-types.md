---
title: Creating property types
source: https://docs.kanzi.com/4.1.0/en/working-with/property-types/creating-custom-property-types.html
---

# Creating property types


Properties provide the means to specify and examine the state, appearance, and behavior of nodes. For example, a property can define a color, indicate whether a button is pressed, or specify the alignment of an item.

Properties provide a uniform way to access data of Kanzi nodes, so that many Kanzi subsystems can manipulate the data. That way you can, for example, animate property values, provide bindings between property values, and monitor property value changes.

Each property in Kanzi is described by a property type. The property type describes the name and category of the property and type of data and values the property can have.

Note that animations can only animate floating point numbers. So, to animate properties that have more than one value (for example, color and transformation), you can split the property data into a set of floating point property data attributes (for example, the RGBA channels in a color property type).
## Setting and using namespaces for custom property types


The names of custom property types must be unique in a Kanzi application. When your Kanzi application uses kzb files exported from different Kanzi Studio projects, to ensure that the names of custom property types remain unique within that application, use in each kzb file a different namespace for custom property types.

When you create property types in Kanzi Engine plugins, use unique names across all plugins and Kanzi Studio projects you use in the same Kanzi application.

In Kanzi you can use these names to access a property type in your application:

- Namespace.Name to access the property type using the Kanzi Engine API.

For example, to access in the Gauges kzb file namespace a property type named Speed, use Gauges.Speed.
- Name to access the property type in shaders.

For example, SpeedNeedle.
- Namespace.Name or Name to access the property type in bindings.
- Display Name is a user-friendly name that you can see in the Library > Property Types.

For example, Speed Needle.


Kanzi Studio projects by default use the project name as the default property type namespace. If the project name contains spaces, Kanzi Studio removes them from the namespace name.

For example, if the name of the project is Primary gauges, the default project property namespace is Primarygauges. For a property named Speed in that project, the full name of the property is Primarygauges.Speed.

To change the project property namespace, in Kanzi Studio in the main menu select Project > Properties and set the Property Namespace property to the namespace you want to use.

Kanzi Studio now by default uses the new project property namespace for all the new custom property types that you create.
## Creating a property type


To create a property type:

1.

In the Library, press Alt and right-click Property Types and select Property Type.
2.

In the New Property Type window, set:

  - In the Naming category, set:

    - Name to set the name for the property when you access it using the Kanzi Engine API.

Property type names cannot contain:

      - A period (.) in the beginning or at the end of a property name
      - Spaces
      - Tabs
      - Slashes (/)
      - Backslashes ()
      - Hashes (#)
      - Opening or closing braces ({})
      - At signs (@)

    - Display Name to set the name for the property when you use it in Kanzi Studio. Enter <Name> to use the same name as the one you set in the Name property.
    - Category to set in which category Kanzi Studio shows your property type in the Properties and Add Properties windows.

Use the Category property to quickly find your property types in Kanzi Studio.
    - Tooltip to set the tooltip text that Kanzi Studio shows for the property type in the Properties and Add Properties windows. Kanzi Studio appends to the tooltip text the Kanzi Engine name of the property type.


> **Tip:** To quickly access a custom property type from the Properties, right-click a custom property type and select Select in Library.
> - Use the Data Type to set what kind of data the property type holds. You can use one of these data types:
>
> - Boolean stores values true or false and has no type-specific properties.
> - Color stores color information for red, green, blue, and alpha channels (RGBA).
>
> Note that even though in Kanzi Studio you can set color values for hue, saturation, light, and alpha channels (HSLA), Kanzi stores them in RGBA. This means you can animate only RGBA values.
> - Enumeration stores a set of key value pairs, so that each unique key resolves to a unique integer.
> - Flags stores an integer bitmask whose bits are individually named. Use power-of-2 values for each bit to prevent overlapping bits.
> - Float stores single precision floating point values.
> - Integer stores 32-bit signed integer values.
> - Matrix 3x3 stores 3x3 matrices of floating point numbers, which you can use to store transformations for 2D nodes.
> - Matrix 4x4 stores 4x4 matrices of floating point numbers, which you can use to store transformations for 3D nodes.
> - Project Item stores references to nodes and resources, and resource IDs, and does not have type-specific properties. You can use the Project Item data type only in application code, for which Kanzi converts the property into the path of the target node or resource in string format.
> - Property Type stores references to other property types. You can use the Property Type data type only in application code, for which Kanzi converts the property into the name of the target property type in string format.
> - Range stores a collection of values.
> - Text stores plain text and does not have type-specific properties.
>
> If you want to create a property type that enables the user to select a node or a resource, or set a resource ID, use the Project Item property type.
> - Vector 2D stores vectors of two floating point numbers.
> - Vector 3D stores vectors of three floating point numbers.
> - Vector 4D stores vectors of four floating point numbers.
>
> - Use the Editor to select the editor that you want to use to set the value of the property type in the Properties window in Kanzi Studio. The available editors depend on the type of data.
> - Use the Is Inherited flag to set whether nodes can inherit from their ancestor nodes the value of this property type.
> - Use the Affect Layout flag to set whether this property type affects node layout. When you enable Affect Layout and the value of this property changes on a node, Kanzi recalculates the layout for that node. Note that recalculating the layout decreases application performance.
>
> For example, if you are using a custom property type to animate content so that the size of its bounding box changes, enable the Affect Layout setting. With this setting the property updates the layout and the rendering.
> - Use the Affect Rendering flag to set whether this property type affects node rendering. When you enable Affect Rendering and the value of this property changes on a node, Kanzi updates the rendering for that node. If the property you are creating does not affect layout or size, you must enable the Affect Rendering to see the effect you want to achieve with this property. For example, enable Affect Rendering if you use this property to set the color of a Text Block node. See Application idle state.
> - Use the Material Rule Property flag to set whether this property type can affect a material rule. See Using a custom property type in a material rule.
> - In the Type Specific category you can set the parameters that are specific to the data type of this property.
>
> For example, you can set the lower and upper value limits for the property type.
> - In the Value section you can set the default value and sorting index for your property.
>
> 3.
>
> Click Save.
>
> Kanzi Studio stores the property type in the Library > Property Types in a folder named after the Namespace set in the Name field of the property type.
>
> You can now add to nodes and use this property type just like any other property in Kanzi. See Using properties in Kanzi Studio.
>
## Moving all custom property types to the project property namespace


To move in your Kanzi Studio project all custom property types to the project property namespace, in the Library right-click Property Types and select Add Property Namespace to Property Types.
## Ordering property categories in the Properties window


To set the order of property categories in the Properties window, select Edit > User Preferences, in the Properties tab in the Property Category dropdown select a property category, and set the position of the property category.

For example, you can set the Transform 2D and your own My Property Category categories to be shown after the Description category.

> **Note:** The General and Description property categories are always shown on the top.
