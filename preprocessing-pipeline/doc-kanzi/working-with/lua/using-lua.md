---
title: Using Lua
source: https://docs.kanzi.com/4.1.0/en/working-with/lua/using-lua.html
---

# Using Lua

Kanzi Engine Lua API is a platform-independent interface to the Kanzi Engine using the Lua programming language. It allows you to create application and user interface logic in Kanzi Studio.

When you export a kzb file, Kanzi Studio embeds Lua scripts in the kzb file.

This topic provides an overview of the fundamentals of Kanzi Engine Lua API. For complete API reference, see Kanzi Lua API reference.

Learn how to develop application logic for your Kanzi applications using Kanzi Engine Lua API by completing the Tutorial: Kanzi Engine Lua API basic use.

Kanzi uses Lua 5.4. See https://www.lua.org/manual/5.4/.
## Executing a Lua script

To execute a Lua script:

1.

In the Node Tree or Prefabs, select or create a node. In the Node Components > Triggers, create a trigger where you want to execute the Lua script.

For example, from the Asset Packages drag the Button asset to the Preview and in the Prefabs, use the Button: Click trigger.
2.

In the Node Components > Triggers, press Alt and right-click the trigger where you want to execute the Lua script and select Run Lua Script.

For example, in the Prefabs select the Button. In the Node Components, press Alt and right-click Button: Click and select Run Lua Script.
3.

In the Run Lua Script action set the Lua Script property to + Script File and name the script.

Kanzi Studio creates Lua scripts in the **Library** > **Resource Files** > **Scripts**.
4.

In the **Library** > **Resource Files** > **Scripts** double-click the script that you created. In the Script Editor add the Lua code and click Save.

```
print("Hello world!")

```

When you set off the trigger, it executes the Run Lua Script action, which runs the code in the script. For example, when you click the button, the Lua script prints `Hello world!` to the Log.
## Using Lua variables

In Lua, you can declare:

- Local variables, which are accessible only in the scope of the script where you declare a variable

Kanzi destroys local variables at the end of the scope.

```
local x = 1

```

- Global variables, which are accessible in all scripts and are persistent across multiple script executions

```
if runCount == nil then
    -- Initialize a persistent global variable `runCount` on the first run of this script.
    runCount = 0
end
runCount = runCount + 1
print("This script has been executed " .. runCount .. " times.")

```

## Accessing nodes

When you set off a trigger that executes the Run Lua Script action, the action assigns to the `contextNode` variable the reference to the node that contains the trigger.

```
-- Print the name of the node that executes the script.
local name = contextNode:getProperty(Node.NameProperty)
print(name)

```

To navigate the node tree, start with the `contextNode` variable, then use the `lookupNode` function with:

- Relative path

```
-- To access the parent node.
local parent = contextNode:lookupNode("..")
local parentName = parent:getProperty(Node.NameProperty)
print(parentName)

```

```
-- To access a child node with the name "Empty Node 2D".
local child = contextNode:lookupNode("Empty Node 2D")
local childName = child:getProperty(Node.NameProperty)
print(childName)

```

- Alias in the nearest resource dictionary

```
-- To access a node to which the alias "Home" in the nearest resource dictionary points.
local node = contextNode:lookupNode("#Home")
local nodeName = node:getProperty(Node.NameProperty)
print(nodeName)

```

To access all child nodes of a node, use the `iterateChildren` function.

```
for child in contextNode:iterateChildren() do
    local name = child:getProperty(Node.NameProperty)
    print(name)
end

```

## Using properties

Kanzi Engine Lua API allows you to work with the existing property types. Most Kanzi property types are present in Kanzi Engine Lua API.

To access property types, use their full Kanzi Engine names, such as `Node.OpacityProperty`. You can find the full Kanzi Engine names for all property types available in Kanzi Engine Lua API in Kanzi Lua API reference.

To access the built-in Kanzi property types:

```
-- Set property.
contextNode:setProperty(Node.OpacityProperty, 0.5)

-- Get property.
local opacity = contextNode:getProperty(Node.OpacityProperty)
print(opacity)

```

To access a custom property type, create an instance of a `PropertyType` with the full Kanzi Engine name of the property type.

```
-- Find the "MyProject.MyPropertyType" custom property type.
local customPropertyType = PropertyType:find("MyProject.MyPropertyType")
contextNode:setProperty(customPropertyType, "Hello Kanzi!")
print(contextNode:getProperty(customPropertyType))

```

See Property system and Creating property types.
**Tip:** For most Kanzi property types, you can find the full Kanzi Engine name in the property tooltip.
### Using vector data types

In Lua scripts, you can use as value types these Kanzi math types:

- Vector2
- Vector3
- Vector4
- ColorRGBA
- Quaternion
- Matrix3x3
- Matrix4x4
- SRTValue2D
- SRTValue3D

For example, you can:

- Declare local variables.

```
local a = Vector2(1.4, 0)
local b = Vector3(4.5, -2.3, 0)
local c = Vector4()
local d = ColorRGBA(0,0,0)
local e = Quaternion()
local f = Matrix3x3(Vector2(1,0), Vector2(0,1), Vector2(0,0))
local g = Matrix4x4(Vector3(1,0,0), Vector3(0,1,0), Vector3(0,0,1), Vector3(0,0,0))
local h = SRTValue2D(Vector2(1,1), 0, Vector2(0,0))
local i = SRTValue3D(Vector3(1,1,1), Quaternion(), Vector3(0,0,0))

```

- Assign property values.

```
local srt = contextNode:getProperty(Node2D.LayoutTransformationProperty)
srt:setTranslation(Vector2(10, 0))
contextNode:setProperty(Node2D.LayoutTransformationProperty, srt)

```

- Access the fields of all vector types with zero-based indexing.

```
local v = Vector3()
v[0] = -1.1
v[1] = 1.2
v[2] = 2.3
print(string.format("%.2f %.2f %.2f", v[0], v[1], v[2]))

```

- Use helper functions to create transformations.

```
local j = Matrix3x3.createTranslation(Vector2(10,0))
local k = Matrix4x4.createTranslation(Vector3(10,0,0))
local l = SRTValue2D.createTranslation(Vector2(10,0))
local n = SRTValue2D.createRotation(3.1415)

```

- Perform mathematical operations.

```
local direction = Vector2(10, 10)
local length = direction:length()
local squaredLength = direction:squaredLength()
local normalizedDirection = direction:normalized()

```

- Use overloaded operators for the common vector operations. For example, you can add two vectors or multiply by a scalar.

```
local position = Vector2(0,0)
local direction = Vector2(10, 0)
local rotation = Matrix3x3.createRotationInDegrees(45.0)
local speed = 2.4
position = position + (rotation * direction):normalized() * speed

```

## Creating and removing nodes

To instantiate a prefab:

```
-- Load a prefab at kzb URL.
local prefab = contextNode:tryAcquireResource("kzb://myProject/Prefabs/MyPrefab")
-- Create a node from the prefab.
local node = prefab:instantiate("My Node")
-- Add the node to the node tree.
contextNode:addChild(node)

```

To replace all child nodes of a node with a node that you create:

```
-- Remove all child nodes from the current node.
contextNode:removeAllChildren()

-- Create a Text Block 2D node named "My TextBlock2D",
-- set it to show "Hello", and add it to the current node.
local node = TextBlock2D:create("My TextBlock2D")
node:setProperty(TextBlock2D.TextProperty, "Hello")
contextNode:addChild(node)

```

See Using node prefabs.
## Using messages

You can access all message types that are already registered with Kanzi Engine. However, you cannot define a message type.

To send messages of built-in message types:

```
-- Create an instance of message arguments for a message that you want to send.
local arguments = ExclusiveActivityHost2D.NavigateNextMessageMessage:newMessageArguments()
-- Set the argument values.
arguments:setLoopActivityProperty(true)
-- Send the message.
contextNode:dispatchMessage(ExclusiveActivityHost2D.NavigateNextMessageMessage, arguments)

```

To access a message type by name, create an instance of `MessageType` with the full name of the message type:

```
-- Access a message type and message argument.
local messageType = MessageType:find("ExclusiveActivityHostConcept.NavigateNextMessage")
local propertyType = PropertyType:find("ExclusiveActivityHostConcept.ImplicitActivityChangeRequestMessageArguments.LoopActivity")

-- Send the message.
local arguments = messageType:newMessageArguments()
arguments:setArgument(propertyType, true)
contextNode:dispatchMessage(messageType, arguments)

```

See Using messages.
### Receiving messages

Set up a message handler to receive messages. Create a handler function that accepts a message argument and set the function as a message handler.

To receive messages:

```
-- Access a message type and message argument.
local messageType = MessageType:find("MyMessage")
local propertyType = PropertyType:find("MyMessageArgument")

-- Define a message handler.
function myMessageHandler(arguments)
    local value = arguments:getArgument(propertyType)
    print("MyMessage received, argument = " .. value)
end

-- Add the message handler to the current node.
contextNode:addMessageHandler(messageType, myMessageHandler)

```

## Logging

Kanzi Engine Lua API gives you access to the standard Kanzi logging functions. They are defined inside of the `log` namespace.

```
log.info("info message")
log.debug("debug message")
log.warning("warning message")
log.error("error message")

```

Note that compared to the `print` function, logging functions accept only a single string argument.

```
print("info", "message")
-- Is the same as:
log.info("info\tmessage")

```

## Navigating data sources

You can access a data source, for example, by acquiring it as a resource and then use functions like `lookupDataContext` to modify its data object tree.

```
-- Acquire data source at kzb URL.
local dataSource = contextNode:tryAcquireResource("kzb://myProject/DataSource")

-- Lookup a certain data object from the data source.
local speed = dataSource:lookupDataContext("Data.Speed")

-- Set the current value to the data object.
speed:setValue(200)

```

## Registering Main Loop Scheduler tasks

You can customize the application main loop by registering additional tasks using `MainLoopScheduler` functions.

```
-- Create a task on the user stage.
local token = MainLoopScheduler.appendTask(
   MainLoopStage.USER,
   "MyTask",
   TaskRecurrence.Recurring,
   function() print("Task is executed") end
)

-- If the task is no longer needed, it can be removed.
MainLoopScheduler.removeTask(MainLoopStage.USER, token)

```

You can also register timer tasks.

```
-- Create a timer task on the user stage. Note that time duration is in nanoseconds.
local token = MainLoopScheduler.appendTimer(
   MainLoopStage.USER,
   "MyTimerTask",
   TaskRecurrence.Recurring,
   millis(5),
   function() print("TimerTask has fired") end
)

-- Remove the timer task once it is no longer needed. Note that the stage does not need to be passed.
MainLoopScheduler.removeTimer(token)

```
