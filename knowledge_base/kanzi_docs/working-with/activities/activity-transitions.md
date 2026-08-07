---
title: Creating transitions between Activities
source: https://docs.kanzi.com/4.1.0/en/working-with/activities/activity-transitions.html
---

# Creating transitions between Activities

Activities use a State Manager to define the transitions for status changes. If you do not create a state manager and define transitions, the transitions between Activity statuses are immediate.
## Activity transition types

To see the animation of a transition, hover over the image of that transition.
### Basic

|

Instant |

Plain |

Crossfade |
|  ![image](../../_static/multimedia/working-with/activity-transitions/instant.png) ![image](../../_static/multimedia/working-with/activity-transitions/instant.gif)  |   ![image](../../_static/multimedia/working-with/activity-transitions/plain.png) ![image](../../_static/multimedia/working-with/activity-transitions/plain.gif)  |   ![image](../../_static/multimedia/working-with/activity-transitions/crossfade.png) ![image](../../_static/multimedia/working-with/activity-transitions/crossfade.gif)  |
|

Fade Out Fade In |

Flip Horizontal |

Flip Vertical |
|  ![image](../../_static/multimedia/working-with/activity-transitions/fade-in-out.png) ![image](../../_static/multimedia/working-with/activity-transitions/fade-in-out.gif)  |   ![image](../../_static/multimedia/working-with/activity-transitions/flip-horizontal.png) ![image](../../_static/multimedia/working-with/activity-transitions/flip-horizontal.gif)  |   ![image](../../_static/multimedia/working-with/activity-transitions/flip-vertical.png) ![image](../../_static/multimedia/working-with/activity-transitions/flip-vertical.gif)  |
### Hinge

|

Hinge Bottom From Front |

Hinge Bottom From Back |

Hinge Left From Front |
|  ![image](../../_static/multimedia/working-with/activity-transitions/hinge-bottom-from-front.png) ![image](../../_static/multimedia/working-with/activity-transitions/hinge-bottom-from-front.gif)  |   ![image](../../_static/multimedia/working-with/activity-transitions/hinge-bottom-from-back.png) ![image](../../_static/multimedia/working-with/activity-transitions/hinge-bottom-from-back.gif)  |   ![image](../../_static/multimedia/working-with/activity-transitions/hinge-left-from-front.png) ![image](../../_static/multimedia/working-with/activity-transitions/hinge-left-from-front.gif)  |
|

Hinge Left From Back |

Hinge Right From Front |

Hinge Right From Back |
|  ![image](../../_static/multimedia/working-with/activity-transitions/hinge-left-from-back.png) ![image](../../_static/multimedia/working-with/activity-transitions/hinge-left-from-back.gif)  |   ![image](../../_static/multimedia/working-with/activity-transitions/hinge-right-from-front.png) ![image](../../_static/multimedia/working-with/activity-transitions/hinge-right-from-front.gif)  |   ![image](../../_static/multimedia/working-with/activity-transitions/hinge-right-from-back.png) ![image](../../_static/multimedia/working-with/activity-transitions/hinge-right-from-back.gif)  |
|

Hinge Top From Front |

Hinge Top From Back |   |
|  ![image](../../_static/multimedia/working-with/activity-transitions/hinge-top-from-front.png) ![image](../../_static/multimedia/working-with/activity-transitions/hinge-top-from-front.gif)  |   ![image](../../_static/multimedia/working-with/activity-transitions/hinge-top-from-back.png) ![image](../../_static/multimedia/working-with/activity-transitions/hinge-top-from-back.gif)  |   |
### Rotate center cross fade

|

Rotate Center Cross Fade |

Rotate Center Top Cross Fade |

Rotate Center Bottom Cross Fade |
|  ![image](../../_static/multimedia/working-with/activity-transitions/rotate-center.png) ![image](../../_static/multimedia/working-with/activity-transitions/rotate-center.gif)  |   ![image](../../_static/multimedia/working-with/activity-transitions/rotate-center-top.png) ![image](../../_static/multimedia/working-with/activity-transitions/rotate-center-top.gif)  |   ![image](../../_static/multimedia/working-with/activity-transitions/rotate-center-bottom-cross-fade.png) ![image](../../_static/multimedia/working-with/activity-transitions/rotate-center-bottom-cross-fade.gif)  |
|

Rotate Center Left From Bottom Cross Fade |

Rotate Center Left From Top Cross Fade |

Rotate Center Right From Bottom Cross Fade |
|  ![image](../../_static/multimedia/working-with/activity-transitions/rotate-center-left-bottom.png) ![image](../../_static/multimedia/working-with/activity-transitions/rotate-center-left-bottom.gif)  |   ![image](../../_static/multimedia/working-with/activity-transitions/rotate-center-left-top.png) ![image](../../_static/multimedia/working-with/activity-transitions/rotate-center-left-top.gif)  |   ![image](../../_static/multimedia/working-with/activity-transitions/rotate-center-right-bottom.png) ![image](../../_static/multimedia/working-with/activity-transitions/rotate-center-right-bottom.gif)  |
|

Rotate Center Right From Top Cross Fade |   |   |
|  ![image](../../_static/multimedia/working-with/activity-transitions/rotate-center-right-top.png) ![image](../../_static/multimedia/working-with/activity-transitions/rotate-center-right-top.gif)  |   |   |
### Rotate corner cross fade

|

Rotate Corner Top Left From Bottom Cross Fade |

Rotate Corner Top Left From Top Cross Fade |

Rotate Corner Bottom Left From Bottom Cross Fade |
|  ![image](../../_static/multimedia/working-with/activity-transitions/rotate-corner-top-left-bottom.png) ![image](../../_static/multimedia/working-with/activity-transitions/rotate-corner-top-left-bottom.gif)  |   ![image](../../_static/multimedia/working-with/activity-transitions/rotate-corner-top-left-top.png) ![image](../../_static/multimedia/working-with/activity-transitions/rotate-corner-top-left-top.gif)  |   ![image](../../_static/multimedia/working-with/activity-transitions/rotate-corner-bottom-left-bottom.png) ![image](../../_static/multimedia/working-with/activity-transitions/rotate-corner-bottom-left-bottom.gif)  |
|

Rotate Corner Bottom Left From Top Cross Fade |

Rotate Corner Top Right From Bottom Cross Fade |

Rotate Corner Top Right From Top Cross Fade |
|  ![image](../../_static/multimedia/working-with/activity-transitions/rotate-corner-bottom-left-top.png) ![image](../../_static/multimedia/working-with/activity-transitions/rotate-corner-bottom-left-top.gif)  |   ![image](../../_static/multimedia/working-with/activity-transitions/rotate-corner-top-right-bottom.png) ![image](../../_static/multimedia/working-with/activity-transitions/rotate-corner-top-right-bottom.gif)  |   ![image](../../_static/multimedia/working-with/activity-transitions/rotate-corner-top-right-top.png) ![image](../../_static/multimedia/working-with/activity-transitions/rotate-corner-top-right-top.gif)  |
|

Rotate Corner Bottom Right From Bottom Cross Fade |

Rotate Corner Bottom Right From Top Cross Fade |   |
|  ![image](../../_static/multimedia/working-with/activity-transitions/rotate-corner-bottom-right-bottom.png) ![image](../../_static/multimedia/working-with/activity-transitions/rotate-corner-bottom-right-bottom.gif)  |   ![image](../../_static/multimedia/working-with/activity-transitions/rotate-corner-bottom-right-top.png) ![image](../../_static/multimedia/working-with/activity-transitions/rotate-corner-bottom-right-top.gif)  |   |
## Adding a transition between Activities

To add a transition between Activities:

1.

In the Activity Browser right-click the Activity to which you want to add a transition and select Add Transition and the transition that you want to use to transition between Activities.

For example, select Flip Vertical to create a transition where Kanzi rotates a node around an axis that runs horizontally through the center of that node.

When you run this command, Kanzi Studio:

  - Creates in the Library > State Managers a State Manager with the ActivityState state group whose Controller Property is the Activity Status property. The state group contains the states that map to the different statuses of Activities.
  - In the Activity sets the Resources > State Manager property to the State Manager that Kanzi Studio created.

2.

Repeat the previous step for all Activities for which you want to create transitions. If you want to use the same State Manager for transitions between Activities, set in those Activities the State Manager property to the same State Manager.

## Creating a custom transition between Activities

You can create your own transitions between Activities.

To create a custom transition between Activities:

1.

In the Activity Browser right-click the Activity for which you want to create transitions and select Add Transition > Plain. When you run this command, Kanzi Studio:

  - Creates a state manager and sets its Controller Property to the Activity Status property. The state manager contains the states that map to the different statuses of Activities.
  - In the Activity sets the Resources > State Manager property to the State Manager that Kanzi Studio created.

2.

Repeat the previous step for all Activities for which you want to create transitions. If you want to use the same State Manager for transitions between Activities, set in those Activities the State Manager property to the same State Manager.
3.

In the Library > State Managers select the State Manager that Kanzi Studio created in the first step and define the transitions by adding and setting properties in each state.

For example:

  - To create a cross-fade transition add the Opacity property to all states:

    - In the Active, Activating, and Deactivating states set it to 1.
    - In the Inactive state set it to 0.

  - To create a fade-in fade-out transition add the Opacity property to all states:

    - In the Active and Deactivating states set it to 1.
    - In the Activating and Inactive state set it to 0.
