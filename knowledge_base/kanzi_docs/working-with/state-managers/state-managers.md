---
title: State manager
source: https://docs.kanzi.com/4.1.0/en/working-with/state-managers/state-managers.html
---

# State manager

Use a State Manager to create different states in your Kanzi application.

For example, you can define the appearance and behavior of a button during different states, such as how the button reacts when a user selects, presses, holds, or releases that button. Kanzi uses its animation system to animate the transitions between states. See Animation system.

Each state manager consists:

- **State groups.** State groups contain states, define controller properties, and transitions between states in a state group. A typical transition defines a period and interpolation paths between property values of two states. You can define transitions using a general guideline for all properties, using interpolations for each property as specified, or using animation items.
- **States.** Each state contains a collection of properties that define the appearance and behavior of the node to which you assign the state manager. In each state group only one state can be active at a time. A state can also define interactions either by enabling or disabling controls input using the enabled property, setting the state as a condition for the trigger in trigger settings, or by explicitly defining triggers and actions for each state.
- **State objects.** State objects define the properties of nodes for a specific state. For example, you can assign a state manager to a Button 2D node which contains a Model node that defines the look of the button. State object sets the properties of the mesh set in the Model node using the Target Object Path property. For example, ./Mesh.

For example, a state manager for a button can contain three state groups: button pressed, button released, and hover over button. Each state group contains enabled and disabled states that through state objects define the appearance and behavior of the button when it is in one of the states, and the transition between the states.

You can define the changes between states in these ways:

- Set a controller property for a state group and a value for that property for each state. These can be implicit properties, such as the Is Down property of the Button nodes. The state changes when the property changes, whether as part of the inherent logic of the node or a specified Set Property action or animation. See Using a controller property to set states.
- Using the State Manager actions Go to State, Next State, and Previous State. If you use the State Manager actions and a controller property, note that when the controller property changes, it overrides the previously set state. See Using state manager actions to set states.

Learn how to use state managers by completing one of these tutorials:

- Create a toggle button. See Tutorial: Creating a toggle button.
- Create a button and control its state with the Is Down property. See Tutorial: Creating a button.
- Create a turn indicator and control it with a custom property. See Tutorial: Create cluster indicators.

## Easing functions

Use an easing function to make UI elements more lifelike. Because objects in real life never start or stop immediately, an appropriate easing function can help you create a more pleasant user experience.

See Using state transitions.

Hover over the image of an easing function to see the type of animation that it creates.
|

**Back** |   |   |
|

Ease in |

Ease out |

Ease in out |
|  ![image](../../_static/multimedia/working-with/animations/back-in.png) ![image](../../_static/multimedia/working-with/animations/back-in.gif)  |   ![image](../../_static/multimedia/working-with/animations/back-out.png) ![image](../../_static/multimedia/working-with/animations/back-out.gif)  |   ![image](../../_static/multimedia/working-with/animations/back-in-out.png) ![image](../../_static/multimedia/working-with/animations/back-in-out.gif)  |
|

**Bounce** |   |   |
|

Ease in |

Ease out |

Ease in out |
|  ![image](../../_static/multimedia/working-with/animations/bounce-in.png) ![image](../../_static/multimedia/working-with/animations/bounce-in.gif)  |   ![image](../../_static/multimedia/working-with/animations/bounce-out.png) ![image](../../_static/multimedia/working-with/animations/bounce-out.gif)  |   ![image](../../_static/multimedia/working-with/animations/bounce-in-out.png) ![image](../../_static/multimedia/working-with/animations/bounce-in-out.gif)  |
|

**Circle** |   |   |
|

Ease in |

Ease out |

Ease in out |
|  ![image](../../_static/multimedia/working-with/animations/circle-in.png) ![image](../../_static/multimedia/working-with/animations/circle-in.gif)  |   ![image](../../_static/multimedia/working-with/animations/circle-out.png) ![image](../../_static/multimedia/working-with/animations/circle-out.gif)  |   ![image](../../_static/multimedia/working-with/animations/circle-in-out.png) ![image](../../_static/multimedia/working-with/animations/circle-in-out.gif)  |
|

**Cubic** |   |   |
|

Ease in |

Ease out |

Ease in out |
|  ![image](../../_static/multimedia/working-with/animations/cubic-in.png) ![image](../../_static/multimedia/working-with/animations/cubic-in.gif)  |   ![image](../../_static/multimedia/working-with/animations/cubic-out.png) ![image](../../_static/multimedia/working-with/animations/cubic-out.gif)  |   ![image](../../_static/multimedia/working-with/animations/cubic-in-out.png) ![image](../../_static/multimedia/working-with/animations/cubic-in-out.gif)  |
|

**Elastic** |   |   |
|

Ease in |

Ease out |

Ease in out |
|  ![image](../../_static/multimedia/working-with/animations/elastic-in.png) ![image](../../_static/multimedia/working-with/animations/elastic-in.gif)  |   ![image](../../_static/multimedia/working-with/animations/elastic-out.png) ![image](../../_static/multimedia/working-with/animations/elastic-out.gif)  |   ![image](../../_static/multimedia/working-with/animations/elastic-in-out.png) ![image](../../_static/multimedia/working-with/animations/elastic-in-out.gif)  |
|

**Exponential** |   |   |
|

Ease in |

Ease out |

Ease in out |
|  ![image](../../_static/multimedia/working-with/animations/exponential-in.png) ![image](../../_static/multimedia/working-with/animations/exponential-in.gif)  |   ![image](../../_static/multimedia/working-with/animations/exponential-out.png) ![image](../../_static/multimedia/working-with/animations/exponential-out.gif)  |   ![image](../../_static/multimedia/working-with/animations/exponential-in-out.png) ![image](../../_static/multimedia/working-with/animations/exponential-in-out.gif)  |
|

**Linear** |   |   |
|

Ease in, Ease out, Ease in out |   |   |
|  ![image](../../_static/multimedia/working-with/animations/linear.png) ![image](../../_static/multimedia/working-with/animations/linear.gif)  |   |   |
|

**Power** |   |   |
|

Ease in |

Ease out |

Ease in out |
|  ![image](../../_static/multimedia/working-with/animations/power-in.png) ![image](../../_static/multimedia/working-with/animations/power-in.gif)  |   ![image](../../_static/multimedia/working-with/animations/power-out.png) ![image](../../_static/multimedia/working-with/animations/power-out.gif)  |   ![image](../../_static/multimedia/working-with/animations/power-in-out.png) ![image](../../_static/multimedia/working-with/animations/power-in-out.gif)  |
|

**Quadratic** |   |   |
|

Ease in |

Ease out |

Ease in out |
|  ![image](../../_static/multimedia/working-with/animations/quadratic-in.png) ![image](../../_static/multimedia/working-with/animations/quadratic-in.gif)  |   ![image](../../_static/multimedia/working-with/animations/quadratic-out.png) ![image](../../_static/multimedia/working-with/animations/quadratic-out.gif)  |   ![image](../../_static/multimedia/working-with/animations/quadratic-in-out.png) ![image](../../_static/multimedia/working-with/animations/quadratic-in-out.gif)  |
|

**Quartic** |   |   |
|

Ease in |

Ease out |

Ease in out |
|  ![image](../../_static/multimedia/working-with/animations/quartic-in.png) ![image](../../_static/multimedia/working-with/animations/quartic-in.gif)  |   ![image](../../_static/multimedia/working-with/animations/quartic-out.png) ![image](../../_static/multimedia/working-with/animations/quartic-out.gif)  |   ![image](../../_static/multimedia/working-with/animations/quartic-in-out.png) ![image](../../_static/multimedia/working-with/animations/quartic-in-out.gif)  |
|

**Quintic** |   |   |
|

Ease in |

Ease out |

Ease in out |
|  ![image](../../_static/multimedia/working-with/animations/quintic-in.png) ![image](../../_static/multimedia/working-with/animations/quintic-in.gif)  |   ![image](../../_static/multimedia/working-with/animations/quintic-out.png) ![image](../../_static/multimedia/working-with/animations/quintic-out.gif)  |   ![image](../../_static/multimedia/working-with/animations/quintic-in-out.png) ![image](../../_static/multimedia/working-with/animations/quintic-in-out.gif)  |
|

**Sine** |   |   |
|

Ease in |

Ease out |

Ease in out |
|  ![image](../../_static/multimedia/working-with/animations/sine-in.png) ![image](../../_static/multimedia/working-with/animations/sine-in.gif)  |   ![image](../../_static/multimedia/working-with/animations/sine-out.png) ![image](../../_static/multimedia/working-with/animations/sine-out.gif)  |   ![image](../../_static/multimedia/working-with/animations/sine-in-out.png) ![image](../../_static/multimedia/working-with/animations/sine-in-out.gif)  |
|

**Smoother step** |   |   |
|

Ease in, Ease out |

Ease in out |   |
|  ![image](../../_static/multimedia/working-with/animations/smoother-step-in.png) ![image](../../_static/multimedia/working-with/animations/smoother-step-in.gif)  |   ![image](../../_static/multimedia/working-with/animations/smoother-step-in-out.png) ![image](../../_static/multimedia/working-with/animations/smoother-step-in-out.gif)  |   |
|

**Smooth step** |   |   |
|

Ease in, Ease out |

Ease in out |   |
|  ![image](../../_static/multimedia/working-with/animations/smooth-step-in.png) ![image](../../_static/multimedia/working-with/animations/smooth-step-in.gif)  |   ![image](../../_static/multimedia/working-with/animations/smooth-step-in-out.png) ![image](../../_static/multimedia/working-with/animations/smooth-step-in-out.gif)  |   |
|

**Step** |   |   |
|

Ease in, Ease out |

Ease in out |   |
|  ![image](../../_static/multimedia/working-with/animations/step-in.png) ![image](../../_static/multimedia/working-with/animations/step-in.gif)  |   ![image](../../_static/multimedia/working-with/animations/step-out.png) ![image](../../_static/multimedia/working-with/animations/step-out.gif)  |   ![image](../../_static/multimedia/working-with/animations/step-in-out.png) ![image](../../_static/multimedia/working-with/animations/step-in-out.gif)  |
