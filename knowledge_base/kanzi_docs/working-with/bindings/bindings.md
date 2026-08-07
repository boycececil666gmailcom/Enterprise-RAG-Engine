---
title: Bindings
source: https://docs.kanzi.com/4.1.0/en/working-with/bindings/bindings.html
---

# Bindings


Use bindings to set the value of a property or property field with the value from another property, property field, or a data source.

Bindings allow nodes, render passes, 2D effects, states, state objects, and styles to automatically update the values of their properties in response to the changing property values, or the occurrence of some external event.

For example, you can:
|

Bind the rotation property field of a node to a property to create a gauge needle that you can control with that property. See Tutorial: Create gauges. |    |
|

Bind the position or size of one node to the position or size of another node. See Tutorial: Making applications with dynamic layout. |    |

With bindings you can modularize your Kanzi project:

- Use bindings in prefabs to provide access only to those properties that you want to set to different values in different instances of the prefab. See Customizing instances of a node prefab.
- Use bindings with data sources to separate the presentation of the user interface from the application data and to remove the dependencies between a Kanzi Studio project and the application code which defines the Kanzi application. This way you can build your Kanzi application according to the [Model-View-Controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) pattern. See Data sources.

For example, you can bind the presentation of a speed needle in the user interface to the data value which represents speed in your application. See Using a data source.


The simplest of bindings bind a property of a node to one of its own properties. You can also bind properties and property fields of one node to those of several different nodes. See Using bindings.
## Components of a binding


A binding has these components:

- Target item, which can be a node, render pass, 2D effect, state, state object, or style.
- Target property and, optionally, property field.
- Source returned by a binding expression.


The source can be a property or property field of a node, render pass, 2D effect, state, state object, style, or data object.

For example, to use a text block to show the current value of a slider, you can bind the Text (`TextConcept.Text`) property of a Text Block node to the Value property of a Slider node. The Text Block node is the target item, Text is the target property, and the Value (`RangeConcept.Value`) property of the Slider node is the source. See Tutorial: Creating a slider.
## Binding modes


Binding mode sets the direction of data flow in the binding:

- One way binding changes the value of a target property when the value of a source property changes.

In a one-way binding, you can bind the target property to a binding expression. See Bindings expressions reference.

> **Note:** When you use a state manager, action, or a style to set a local property value, that removes any one-way binding that targets the property. See Value source bindings.
> - To Source binding sets:
>
> - A property value in the project item that you set as the Push Target of the binding.
> - A property value that is affected also by some other source, such as user input. See Creating a to-source binding.
> - A property value in a resource used by the item to which you add the binding.
>
> For example, you can set a property value in a render pass or 2D effect instance used by a node. See Customizing instances of a render pass prefab and Customizing instances of a 2D effect prefab.


In a to-source binding, you can bind the target property to a binding expression. See Bindings expressions reference.
- Two way binding changes the value of a target property when the value of a source property changes, and the other way around.

In a two-way binding, you can bind a target property only to a source property. See Creating a two-way binding.

## Binding types


These types of bindings are available in Kanzi:

- Value Sources

A value source binding sets the local value of an entire property and provides the value for that property during application runtime.

See Value source bindings.
- Modifiers

A modifier binding modifies a property value, much like an animation or a state manager.

See Modifier bindings.
- To Source

A to-source binding pushes a property value to a node or another project item, or to a resource used by that item.

See To-source bindings.

### Value source bindings


A value source binding sets the local value of an entire property and provides the value for that property during application runtime.

For example, bind the Layout Height property of a 2D node to the Layout Width property of that node, or bind the Text property of a Text Block 2D node to the position of another node. See Creating simple bindings and Binding to the properties of other nodes.

A value source binding replaces any previously set local property value.

Kanzi removes a value source binding when:

- Setting the property value by other means replaces the previously set local value.
- The local property value is removed.


For example:

- A one-way value source binding that sets the Text property of a Tex Box node stops working when the user edits the text. To update the text with a binding, use a to-source or two-way binding instead. See Using a binding to update the text in a Text Box node.
- A one-way binding that sets the Toggle State property of a Toggle Button node stops working when the user toggles the button. To update the property value with a binding, use a to-source or two-way binding. See Using a binding to update the toggle state.

### Modifier bindings


A modifier binding modifies a property value, much like an animation or a state manager.

A modifier binding either:

- Sets the value of a property field.

For example, bind the Layout Transformation property Rotation property field of a node to the Scroll Position property of a Scroll View node to rotate the node using swiping gestures. See Tutorial: Rotate a 3D model.
- Accesses a value source in a binding expression.

For example, bind the Render Transformation property Translation Y property field of a node to the Render Transformation property Translation X property field of the same node to make that node move on the y axis the same distance as it moves on the x axis. See Modifying the value of the property that you bind and getCurrentValue.


Kanzi executes modifier bindings after value Sources bindings. A modifier binding does not replace a local property value.
### To-source bindings


A to-source binding pushes a property value to a node or another project item, or to a resource used by that item.

For example, use a to-source binding to:

- Set a property value that is affected also by some other input source, such as user input.

For example:

  - In a List Box node, the Selected Item Index property.
  - In a Scroll View or Grid List Box node, the Scroll Position property.
  - In a Slider node, the Value property. Updating the slider value with a property.
  - In a Text Box node, the Text property. Using a binding to update the text in a Text Box node.
  - In a Toggle Button node, the Toggle State property. See Using a binding to update the toggle state.
  - In a Toggle Button Group node, the Current Button Index property.

- Set a property value in a render pass prefab instance used by a Viewport 2D node. See Customizing instances of a render pass prefab.
- Set a property value in an effect instance used by a 2D node. See Customizing instances of a 2D effect prefab.

## Material type bindings


Material types have their own special types of bindings for:

- Uniforms

Uniform bindings enable you to modify the values of shader uniforms used by a material type without making changes to the shader code.

See Uniform bindings.
- Temporary Variables

In a material type, a temporary variable binding enables you to store the result of a binding into a temporary variable. You can refer to this variable in other bindings in the same material type.

See Temporary variable bindings.
