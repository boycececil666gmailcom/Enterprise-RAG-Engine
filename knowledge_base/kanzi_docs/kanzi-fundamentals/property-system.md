---
title: Property system
source: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/property-system.html
---

# Property system


Properties provide the means to specify and examine the state, appearance, and behavior of nodes. For example, a property can define a color, indicate whether a button is pressed, or specify the alignment of an item.

You can work with properties by setting the property values in Kanzi Studio and accessing them in code without understanding how the property system works. However, to take full advantage of the Kanzi property system features, you have to become familiar with how the property system works.

Properties provide a uniform way to access data of Kanzi nodes, so that many Kanzi subsystems can manipulate the data. That way you can, for example, animate property values, provide bindings between property values, and monitor property value changes.

Any property value can be affected by multiple input sources. The property system defines the rules for resolving the property value from all inputs and resolves the current value. For example, you can set the value of a property directly, properties can have default values, styles can affect property values, and animations and state manager can modify property values. By offering rules that are applied automatically, the property system minimizes the number of places where you have to change the values manually.
## Property data type


Each property is described by a property type. The property type uniquely describes where the property is used and the name of the property. The data type defines the type of values that the property can hold.

For example, the `Node::VisibleProperty` property type, which controls the visibility of nodes, is used in the `Node` class and derived classes. You can use its name (`Node::VisibleProperty`) to find the property type during runtime. Because the data type of the property is boolean, it accepts the values `true` or `false`.

In Kanzi Studio, you can have more specialized property types, but their representation comes only from the available data types. See Creating a property type.

For example, enumeration values are represented as integer values even though they limit the range of values to the entries defined in the enumeration.
## Property usage


Most Kanzi properties are defined in the classes that use them. You can use such properties to set the appearance, state, or behavior of the object where you set the property.

For example:

- In a Text Block node, the Text property defines the text that the node displays.
- The Visible property controls the visibility of a node and all its descendant nodes.


However, some Kanzi properties configure the appearance, behavior, or state of other objects.

For example:

- Materials can define the Diffuse Color property that you can assign to nodes using that material.
- Grid Layout defines the Row and Column properties, but you set them in the child nodes of the Grid Layout node, not in the Grid Layout node.


In Kanzi, these properties are called attached properties.
## Default property value


Each property type defines the default value of that property. When queried, Kanzi returns the default value unless you set the property value directly or indirectly through styles, inheritance, and so on. Using the default value can save time during application development.

For example, the default value of the Visible (`Node::VisibleProperty`) property is `true`. By default, all nodes are visible.

Alternatively, not having a property value is a condition for some property types.

For example, the Layout Width (`Node::WidthProperty`) and Layout Height (`Node::HeightProperty`) properties let you set the size of a node:

- By setting these properties to 100 pixels, you force the size of the node to be 100 by 100 pixels.
- By not setting these properties, you let the node decide its own size.

For example, the Image node can decide its size based on the image that it shows, or a Stack Layout node can determine to be the size of all of its items.

## Inheritable property types


Each property type defines whether the value of that property is inheritable. A node inherits the values of inheritable property types from its ancestor nodes.

For example, `Node::FontFamilyProperty` is an inheritable property type. When you want to use the same font family for all controls that can display text, set the Font Family property only at the top-most level of your node tree. Kanzi applies the same font to all descendant nodes. If you want to use a different font in one of the descendant nodes, add the Font Family property to that node and set it to the font family that you want to use.
## Property precedence


Querying a property value produces one result, but while determining the value, the property system evaluates multiple sources that can affect the property value. The property value sources are evaluated in a specific order.

Kanzi Engine resolves the runtime values based on these precedence rules (the highest first):

- **Modified value**

Animations and bindings modify and states override the value. See Animations, Modifier bindings, and State manager.

> **Tip:** In the Kanzi Studio Node Tree window, an indicator next to a node shows when a State Manager, Binding, Data Source Binding, or an Animation overrides the values of some properties in that node.
>
> To navigate to the source of the override in the Kanzi Studio project, right-click the override indicator and select the source you wish to navigate to from the context menu.
> - **Local value**
>
> Local values are property values that you set directly. In Kanzi Studio, all properties in nodes are defined by a local value. You can set the local value using actions, value source bindings, and Kanzi Engine API.
>
> Using the Kanzi Engine API, you can set local property values with:
>
> - The `PropertyObject::setProperty` function.
>
> For example, to set the value of the Visible property to false, use
>
> ```
> node.setProperty(Node::VisibleProperty, false)
>
> ```
>
> - Helper functions offered by most of the classes.
>
> For example, you can set the `Node::VisibleProperty` property with the `Node::setVisible` function.
>
> For helper functions, see the reference of the class that defines the property.


See Value source bindings and Triggers.
- **Named style**

Kanzi applies a named style to all nodes whose Style property value points to that style.

See Applying a style to selected instances of a node type.
- **Typed style**

Kanzi applies a typed style to all nodes of the type that you specify in the style.

See Applying a style that applies to a node type in the selected scope.
- **Inherited value** (if the property is inheritable)

Each property type specifies whether the property is inheritable. Only certain values can be inherited from ancestors.

See Inheritable property types.
- **Default value and class default value**

All properties have a default value defined in their metadata. Kanzi uses the default value if nothing else affects the value. Each class that inherits the property type can override its default value.

For example:

  - The default value of the Horizontal Alignment (`Node::HorizontalAlignmentProperty`) property is Center (`Node::HorizontalAlignment::HorizontalAlignmentCenter`).
  - The `Node2D` class overrides the default value of the Horizontal Alignment property to Left (`Node::HorizontalAlignment::HorizontalAlignmentLeft`).


See Default property value.

## Property type change flags


In Kanzi, each property type can have one or more change flags that indicate the effects of changing the value of that property.

For example:

- The `PropertyTypeChangeFlag::PropertyTypeChangeFlagMeasure` flag is used by property types that affect the size of a node as reported by that node itself, or the size and position of that node with respect to other nodes.

For example, the Layout Width (`Node::WidthProperty`) property has this change flag. When the value of the Layout Width property changes in a node, Kanzi:

  1.

Remeasures the node.
  2.

If the measured size of the node changed, measures the parent of the node, the parent of the parent, and so on.
  3.

Rearranges the layout of the node, its changed ancestor nodes, and their descendants.
  4.

For those nodes whose transform changed, recalculates the transformations.
  5.

Draws all nodes.

- The `PropertyTypeChangeFlag::PropertyTypeChangeFlagRender` flag is used by property types that change the rendering parameters of a 2D node but do not affect the layout.

For example, the Render Transformation (`Node2D::RenderTransformationProperty`) property has this change flag. When the value of the Render Transformation property changes in a node, Kanzi:

  1.

Recalculates the transformations of the node and its descendants.
  2.

Draws all nodes.

- The `PropertyTypeChangeFlag::PropertyTypeChangeFlagDraw` flag is used by property types that affect the drawing of a node.

For example, most material properties use this flag. When the value of such a property changes in a node, Kanzi draws all nodes.


In the Kanzi Engine API reference, see `PropertyTypeChangeFlag`.
