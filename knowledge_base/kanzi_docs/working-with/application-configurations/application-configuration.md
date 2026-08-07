---
title: Application development
source: https://docs.kanzi.com/4.1.0/en/working-with/application-configurations/application-configuration.html
---

# Application development


There are several ways to add or customize your Kanzi application behavior and functionality:

- Using configuration you can set the most common startup and runtime parameters for your application. For example, you can configure the application resolution, the kzb files that the application uses, and so on. See Configuring your application.
- Use code behind to add behavior to UI elements in your application. Code behind is the easiest way to add functionality without leaving Kanzi Studio and without creating solutions or project files. You can observe the behavior that is implemented in code behind immediately in the Preview. See Programming Activities with Code Behind.
- Derive a C++ class from the `Application` class which is the base class for all Kanzi applications. Override the various virtual functions of the `Application` class to react to different points in the lifecycle of the application, such as initialization and uninitialization. For example, when the application starts, when the application loads its UI content, and so on. See Reacting to application lifecycle events.
- Use the `MainLoopScheduler` class to which the `Application` class delegates processing of input, ticking of animations, laying out and rendering content, ending with update of the screen through repeated control flow. You can add tasks that execute in the main loop of the application to add recurring or one-time functionality relative to the stages of the main loop of the application. See Modifying the main loop logic.
- Develop Kanzi Engine plugins which can implement functionality that you can reuse between applications.

## Configuring your application


Using configuration you can set the most common startup and runtime parameters for your application. For example, you can configure the application resolution, the kzb files that the application uses, and so on.

You can configure your Kanzi application:

- In the C++ application override the `Application::onConfigure` function of your application class. Kanzi calls this function as part of application initialization before it reads the `application.cfg` and before it initializes the graphics subsystem. Use this function to configure application properties.
- In `application.cfg` by setting the parameters for Kanzi Studio projects without recompiling your application or even without a C++ application.


The configuration you specify in `application.cfg` overrides the configuration you specify in `Application::onConfigure`.

For example, to set in `application.cfg` which kzb file to load

```
# Loads the kzb file named my_application.kzb.
BinaryName = "my_application.kzb"

```


To set the kzb file to load in `Application::onConfigure`

```
// Loads the kzb file named my_application.kzb.
configuration.binaryName = "my_application.kzb";

```


For a list of all the configuration settings you can use for your Kanzi application, see Application configuration reference.
## Reacting to application lifecycle events

### Adding startup logic


You can define the startup logic of your application in these functions:

- Kanzi calls the `Application::onStartup` function once, immediately after starting the application, but before it loads the initial UI contents. Here you can add application start-up logic that requires modifying already initialized Kanzi objects.
- Kanzi calls the `Application::onProjectLoaded` function once, immediately after loading the initial UI contents.

Usually you insert here initialization code that depends on the content that has already been loaded. For example, you can attach initial message handlers or listeners, populate the UI with data, and so on.

For example, this code attaches a handler to a Button after Kanzi loads the node tree:

```
void onProjectLoaded() override
{
    // Get reference to the Screen node.
    ScreenSharedPtr screen = getScreen();
    kzAssert(screen);

    // Look up reference to a button by alias.
    Button2DSharedPtr button = screen->lookupNode<Button2D>("#Button");
    kzAssert(button);

    // Attach a handler to the button.
    button->addMessageHandler(Button2D::ClickedMessage, [this](auto& arguments)
                              {
                                  this->buttonHandler(arguments);
                              });
}

```


This diagram shows the callbacks for startup and shutdown logic. [](../../_images/reacting-to-lifecycle-events.svg)
### Observing application state


You can observe the application state to find out whether an application is running, minimized, or suspended.

A Kanzi application is always in one of these states:

- `MainLoopState::Running` state. This is the normal mode of operation of a Kanzi application. This is the initial state of an application.
- `MainLoopState::Paused` state. The platform can impose rules on application behavior when it is out of focus or minimized. To mark such state, a platform backend can set the application to the `MainLoopState::Paused` state.

In this state, Kanzi stops normal input handling and rendering, and waits to be put back to the `MainLoopState::Running` state. Additionally, it is typical for applications to halt heavy work when in this state.
- `MainLoopState::Quitting` state. This state indicates that either application or the platform requested the application to quit by calling `MainLoopScheduler::quit`. In this state, applications must avoid starting work, unless that work is related to uninitialization.


This diagram shows the states of a Kanzi application. [](../../_images/states.svg)

To find out the application state, call `MainLoopScheduler::getState`.

For example, to prevent adding a task when an application is quitting:

```
void doSomethingRepeatedly()
{
    doSomething();

    // If a condition is met...
    if (someCondition() &&
        // ...and the application is not quitting...
        getState() != MainLoopState::Quitting)
    {
        // ...add another task to the task dispatcher.
        getDomain()->getTaskDispatcher()->submit([this]()
                                                 {
                                                     this->doSomethingRepeatedly();
                                                 });
    }
}

```

### Reacting to application state changes


Use these functions to react to application state changes:
|

Function |

Description |
|

`Application::onSuspend` |

Kanzi calls this function in a frame where no rendering was performed, to determine whether to suspend the application and for what duration. The default implementation calculates appropriate timeout based on active animations, timers, and resources waiting for deployment.

Use this function to customize application suspension.  |
|

`Application::onPause` |

Kanzi calls this function when the application main loop enters the `MainLoopState::Paused` state. |
|

`Application::onResume` |

Kanzi calls this function when the application main loop returns from the `MainLoopState::Paused` to the `MainLoopState::Running` state. |
|

`Application::onShutdown` |

Kanzi calls this function immediately before the application uninitialization. |
## Modifying the main loop logic


The main loop consists of a sequence of stages, where each stage consists of a sequence of tasks. A task is any callable item, including functions, function objects, and lambdas.
