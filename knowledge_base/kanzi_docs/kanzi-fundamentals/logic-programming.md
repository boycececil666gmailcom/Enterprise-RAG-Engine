---
title: Logic programming
source: https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/logic-programming.html
---

# Logic programming

In Kanzi you can program application and control logic using several technologies that are geared towards different users and use cases:
|   |

Triggers and actions provide reactive logic programming through Kanzi Studio UI. You can use triggers and actions to execute small pieces of logic called actions based on simple conditions defined in triggers. For example, if you want to handle simple events like button press, or perform simple operations like set a property or activate a page, you can use triggers and actions.

Triggers define the events and conditions you want to handle and contain actions that you want to execute when the trigger is set off. Actions are small operations that are executed when the trigger event happens and conditions are met. See Triggers.  |
|   |

State managers expose logic programming through defining state machines tied to internal states of controls or application. For example, use the state manager to define the look of a button when it is pressed and when it is not, or to define the logic of your application, control, or prefab in terms of mutually exclusive states. You can use a state manager to define the logic of a menu. For example, to show whether the sound in a car is muted, or when fuel is low. See State manager. |
|   |

Kanzi Engine Lua API is a platform-independent interface to the Kanzi Engine using the Lua programming language. It allows you to create application and user interface logic in Kanzi Studio.

When you export a kzb file, Kanzi Studio embeds Lua scripts in the kzb file. See Using Lua, Tutorial: Kanzi Engine Lua API basic use, and Kanzi Lua API reference.  |
|   |

C++ and Java APIs provide the most extensive way to program logic and are geared towards programmers and technical designers. Use the APIs to program applications, develop Kanzi Engine plugins, interface with devices and application execution environment. See Kanzi Engine C++ API reference and Kanzi Engine Java API reference. |
