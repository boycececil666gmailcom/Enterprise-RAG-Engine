---
title: Using messages
source: https://docs.kanzi.com/4.1.0/en/working-with/triggers/using-messages.html
---

# Using messages


The message system provides a way to notify about events and to exchange information.
## Messages and arguments


`MessageArguments` is the base class for arguments passed in messages. Kanzi provides built-in message types for different nodes and triggers. For example, the `ButtonConcept::ClickedMessageArguments` message for the Button: Click trigger and the `Page::ActivatedMessageArguments` message for the Page Activated trigger.

You can extend the `MessageArguments` class by writing your own message types.

Message type describes:

- The nature of an event or information

For example, `ClickManipulator::ClickMessage` and `ListBoxConcept::ItemSelectedMessage`.
- Arguments to describe the data associated within the message

For example, the `InputManipulator::InputMessageArguments::HitTestPointProperty` and `ListBoxConcept::ItemSelectedMessageArguments::SelectedItemIndexProperty` properties.


You can describe and access the message arguments with the `PropertyType` objects. `MessageArguments::setArgument` function sets and `MessageArguments::getArgument` function retrieves arguments with the underlying storage type for arguments, such as float, boolean, and vector3.
## Creating custom messages in Kanzi Studio


To create a custom message in Kanzi Studio:

1.

In the Library press Alt and right-click Message Types and select Message Type.
2.

In the Properties set:

  - Category to the category where you want Kanzi Studio to show this message in context menus.
  - Arguments to the arguments accepted by the message type.
  - Routing Mode to the routing mode of the message type.

    - Tunneling mode passes the message through the outermost parent node of the recipient node.
    - Bubbling mode passes the message through the closest parent node of the recipient node.


See Setting the handling of trigger messages.
## Using messages in the Kanzi Engine API

### Dispatching messages


To dispatch messages use `Node::dispatchMessage`. This function defines the message type and arguments and calls all the handlers and filters which are registered for the node for that message type. `Node::dispatchMessage` notifies the handlers and filters immediately before the function call returns, which enables the handlers and filters to react to the message immediately.

When you dispatch a message it travels in two phases: first tunneling, then bubbling. During the tunneling phase the message travels down the node tree from the first child node of the Screen node (the root node) to the node where the message originated. From there the message bubbles back up the node tree to the root node.
### Reacting to messages


All messages in Kanzi are routed messages. When a message is dispatched, the system walks through the node tree from the first child node of the Screen node (the root node) to the source node of the message in a process called tunneling, and then walks back up the node tree to the root node in a process called bubbling. When you want nodes to react to a message when that message passes, add message handlers or filters to those nodes. A message filter intercepts messages from any node while a message handler listens only to messages from a specific source node.

At each passed node in the node tree the system looks for handlers and filters for the dispatched message. This allows you to install handlers and filters at any place in the node tree to intercept messages before they reach their destination, or to gather messages from several sources.

To register message handlers and filters that react to:

- Bubbling messages use `Node::addMessageHandler` and `Node::addMessageFilter`
- Tunneling messages use `Node::addTunnelingHandler` and `Node::addTunnelingFilter`


To remove all types of handlers and filters use `Node::removeMessageHandler`.

To define a simple example node, one message type, two callbacks which are suitable for message handlers and a counting mechanism to verify the callback invocations:

```
// Counts how many times the callbacks are invoked to verify that the calls occur.
static int callCount = 0;

// Define an example node, which presents a message type and a callback method.
class ExampleNode : public EmptyNode2D
{
public:
    // An example message type.
    static MessageType<MessageArguments> exampleMessageType;

    // Create the node.
    static ExampleNodeSharedPtr create(Domain* domain, string_view name)
    {
        ExampleNodeSharedPtr node = make_polymorphic_shared_ptr<EmptyNode2D>(new ExampleNode(domain, name));
        node->initialize();
        return node;
    }

    // An example callback method.
    void exampleNodeCallback(MessageArguments& message)
    {
        // To let the message continue moving in the node tree, set the message to not handled.
        message.setHandled(false);
        ++callCount;
    }

private:
    // Construct the node.
    explicit ExampleNode(Domain* domain, string_view name) :
        EmptyNode2D(domain, name)
    {
    }
};

// An example callback function.
void exampleCallback(MessageArguments& message)
{
    message.setHandled(false);
    ++callCount;
}

// The message type definition.
MessageType<MessageArguments> ExampleNode::exampleMessageType(kzMakeFixedString("ExampleNode.exampleMessageType"), nullptr);

```


To add a handler that consumes the messages sent by the node itself with `Node::addMessageHandler`:

```
// Initialize a node.
ExampleNodeSharedPtr node = ExampleNode::create(domain, "node");

// Add a message handler that intercepts messages dispatched from the node itself.
Node::MessageSubscriptionToken token = node->addMessageHandler(ExampleNode::exampleMessageType, &exampleCallback);

```


To remove the handler with `Node::removeMessageHandler`:

```
// Remove the handler that intercepts messages dispatched from the node itself.
node->removeMessageHandler(token);

```


To add a bubbling handler with `Node::addMessageHandler`:

```
// Initialize a child node.
EmptyNode2DSharedPtr child = EmptyNode2D::create(domain, "child");

// Set the node you created earlier to be the parent of the child node.
node->addChild(child);

// Add a bubbling message handler that accepts messages from the child node.
Node::MessageSubscriptionToken bubblingToken = node->addMessageHandler(ExampleNode::exampleMessageType, function<void(MessageArguments&)>(&exampleCallback), child.get());

```


To remove a bubbling handler with `Node::removeMessageHandler`:

```
// Remove the bubbling handler.
node->removeMessageHandler(bubblingToken);

```


To add a tunneling filter with `Node::addTunnelingFilter`:

```
// Add a message filter that intercepts tunneling messages.
Node::MessageSubscriptionToken tunnelingToken = node->addTunnelingFilter(ExampleNode::exampleMessageType, node.get(), &ExampleNode::exampleNodeCallback);

```


To remove a tunneling filter with `Node::removeMessageHandler`:

```
// Remove the tunneling filter.
node->removeMessageHandler(tunnelingToken);

```


To dispatch a message use `Node::dispatchMessage`:

```
// Initialize the message that you want to dispatch.
MessageArguments message;

// Dispatch the created message from the child node. If the message dispatcher has any handlers
// or filters added for ExampleNode::exampleMessageType, Kanzi invokes their callbacks immediately.
child->dispatchMessage(ExampleNode::exampleMessageType, message);

```
