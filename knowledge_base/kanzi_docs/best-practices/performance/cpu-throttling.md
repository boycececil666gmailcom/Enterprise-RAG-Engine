---
title: Application idle state
source: https://docs.kanzi.com/4.1.0/en/best-practices/performance/cpu-throttling.html
---

# Application idle state

To improve the CPU performance Kanzi does not redraw the application content when your Kanzi application is idle.

Kanzi suspends the main loop when there is no input, tasks, timers, animations, or when there is nothing in the application that updates the rendering.

When using application idle state, consider that:

- If your Kanzi application is showing an animation, Kanzi by default throttles the CPU to the maximum FPS. If there are no animations, Kanzi sets the application to idle state. For this reason to conserve the CPU and power, Kanzi by default limits the maximum frame rate to 60 frames per second. Use the application configuration to set the maximum frame rate for your application.

See MaximumFPS.
- If your application relies on continuously executing some main loop tasks, such as functionality that you added to the main loop `UserStage`, disable the idle state.

See ApplicationIdleState.
- When your application is in idle state and the application makes changes to the render pass tree, Kanzi does not trigger the rendering to render the changes. To render the changes in such case, you must manually trigger the rendering by calling on any node the `Node::invalidateDraw` function.

If you want to effectively use the application idle state in your Kanzi application, keep in mind:

- Task dispatcher. The task dispatcher allows other threads to schedule execution of tasks in the UI thread. This way you can wake up the UI thread when changes happen only in other threads. When you add tasks to the task dispatcher, each task wakes up the UI thread. If you want to optimize the CPU performance of your application, add tasks to the task dispatcher only when you need to.
- Timers. Timers keep the application awake and impact the CPU performance. Every time a timer is set off in an application, it brings the application from the idle state. If you are integrating sound in your application, do not synchronize it every frame. For example, set the application to synchronize the sound every 100 ms.
- Changes in layout and rendering.

  - When the Affect Layout setting is enabled in a property that you use to set the size of a node, the application stays awake until Kanzi completes recalculation of the layout and renders the new layout.
  - When the Affect Rendering setting is enabled in a property that you use to render a node, but the change does not have an impact on the node size (the Affect Layout setting is disabled), Kanzi does not recalculate the layout, but only renders again. The application stays awake until Kanzi renders the change.

You can set the application idle state in the application configuration. See ApplicationIdleState.
