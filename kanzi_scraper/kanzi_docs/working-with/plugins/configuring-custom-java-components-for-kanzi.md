---
title: Extending the functionality of Kanzi Engine with Java
source: https://docs.kanzi.com/4.1.0/en/working-with/plugins/configuring-custom-java-components-for-kanzi.html
---

# Extending the functionality of Kanzi Engine with Java


With a Kanzi Engine plugin you can extend the functionality of Kanzi Engine and set how Kanzi Studio shows the custom content you create:

- Create your own nodes and property types. See Creating custom nodes and property types.
- Create your own message types that users of Kanzi Studio can use either as triggers or actions. See Creating custom message types.
- Set how Kanzi Studio shows the property types you create in your Kanzi Engine plugin. See Setting custom property types.
- Set the default value of any property type that is defined in the node on which you base your node. See Setting the default value of a property type.
- Create your own Actions. See Creating custom actions.

## Creating custom nodes and property types


In a Java Kanzi Engine plugin you can create custom nodes with custom property types. You can set how Kanzi Studio shows and lets users interact with these nodes.

To create a custom node with custom property types:

1.

Create the node class and give it a metaclass to pass to Kanzi Studio information about this class:
