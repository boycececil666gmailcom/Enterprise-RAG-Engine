---
title: Triggers
source: https://docs.kanzi.com/4.1.0/en/working-with/triggers/triggers.html
---

# Triggers


Use triggers and actions to create interactions. Use triggers to set off actions, such as setting a property to a certain value or setting the state of an application.

For example, Kanzi generates messages from user input and these messages are handled by nodes according to specified behavior.

Nodes define most of the message handling behavior, such as scrolling in a List Box node. However, to meet the requirements of your application, you can define additional behavior. For example, a Button node sends a click message when a user clicks that button, but you can define what happens after the sent click message. An example action is that a click triggers an animation that highlights the button that the user clicked.

All Kanzi nodes can send and receive messages and you can intercept these messages with triggers. Some nodes by default receive messages from specific user input events. For example, a Button node by default receives click messages and a Scroll View node by default receives scroll messages.

In Kanzi these concepts relate to defining event-driven logic:

- **Input and hit testing.** Input is first recognized in a hit testing phase, where all nodes that have Hit Testable property enabled participate. If a pointer event (for example, mouse button down) is performed on top of nodes that participate in hit testing, only the topmost component receives the input. If a node has a manipulator that reacts to the received type of input, it can send messages (for example, a click message). See Defining which node receives input, Using input manipulators and Using triggers.
- **Input manipulators.** An input manipulator reacts to a specific type of input gesture, such as pan, click, or long press. In Kanzi Studio you can use nodes that already contain specific types of manipulators, or you can add input manipulators using the Kanzi Engine API. For example, a Scroll View node contains a pan manipulator and a Button node includes a click manipulator. See Using input manipulators.
- **Messages.** Nodes use messages to communicate. The messages travel between nodes using a process called tunneling and bubbling. The message reaches its target node during tunneling and during bubbling messages travel to ancestor nodes, until a trigger intercepts the message and sets it as handled. This enables you to place triggers in nodes themselves, or their ancestors. For example, you can place a trigger called radioButtonHandler to the parent of multiple buttons. See Using messages.
- **Triggers.** Triggers react to messages, a change in data, or events and apply logic. Kanzi includes the most common action types, such as Set Property or Go to State, but you can use the Kanzi Engine API to define to which messages triggers react. Each trigger includes settings, such as the Set Message Handled property, which prevents the message from bubbling up to other triggers, and conditions which you can use to define conditions under which the trigger sets off. You can add multiple triggers to a single message or event and each can have specific settings and conditions. See Using triggers and Triggers reference.
- **Actions.** An action is an outcome of a trigger. Kanzi includes general actions like Set Property, Write Log, Activate Theme, and actions you can use to control a specific type of item such as, Go to State, Set Scroll Target, or Activate Activity. See Actions and messages reference.
