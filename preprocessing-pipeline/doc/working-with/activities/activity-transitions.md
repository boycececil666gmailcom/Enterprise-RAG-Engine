---
title: Creating transitions between Activities
source: https://docs.kanzi.com/4.1.0/en/working-with/activities/activity-transitions.html
---

# Creating transitions between Activities

Activities use a State Manager to define the transitions for status changes. If you do not create a state manager and define transitions, the transitions between Activity statuses are immediate.
## Activity transition types

To see the animation of a transition, hover over the image of that transition.
### Basic

Instant |

Plain |

Crossfade |

Fade Out Fade In |

Flip Horizontal |

Flip Vertical |
### Hinge

Hinge Bottom From Front |

Hinge Bottom From Back |

Hinge Left From Front |

Hinge Left From Back |

Hinge Right From Front |

Hinge Right From Back |

Hinge Top From Front |

Hinge Top From Back |   |
### Rotate center cross fade

Rotate Center Cross Fade |

Rotate Center Top Cross Fade |

Rotate Center Bottom Cross Fade |

Rotate Center Left From Bottom Cross Fade |

Rotate Center Left From Top Cross Fade |

Rotate Center Right From Bottom Cross Fade |

Rotate Center Right From Top Cross Fade |   |   |
### Rotate corner cross fade

Rotate Corner Top Left From Bottom Cross Fade |

Rotate Corner Top Left From Top Cross Fade |

Rotate Corner Bottom Left From Bottom Cross Fade |

Rotate Corner Bottom Left From Top Cross Fade |

Rotate Corner Top Right From Bottom Cross Fade |

Rotate Corner Top Right From Top Cross Fade |

Rotate Corner Bottom Right From Bottom Cross Fade |

Rotate Corner Bottom Right From Top Cross Fade |   |
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
