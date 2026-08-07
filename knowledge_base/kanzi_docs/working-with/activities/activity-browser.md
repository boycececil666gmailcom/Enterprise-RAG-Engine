---
title: Using the Activity Browser
source: https://docs.kanzi.com/4.1.0/en/working-with/activities/activity-browser.html
---

# Using the Activity Browser

Use the Activity Browser to create and inspect Activities and Activity Hosts, and to simulate the activation of Activities. The Activity Browser shows all possible UI states of Activities in your application.

To access commands available for an Activity or Activity Host, right-click that item.

To pan and zoom in the Activity Browser window:
|

Action |

Shortcut |
|

Pan |

- Click and drag the middle mouse button.
- Press the Space key, and click and drag the left mouse button.
  |
|

Zoom |

- Scroll the mouse wheel.
- Press the Shift and Alt keys, and click and drag the left mouse button.
  |
## Simulating the activation of Activities

In the Activity Browser, you can simulate the activation of Activities:

- To simulate the activation of an Activity, in the Activity that you want to activate, click .

In the Activity Browser, active Activities are marked with  and their border is blue.

When you restart the Preview, you reset the activation state of the Activities.
- To simulate the activation of an Activity that you control through a controller property of its Activity Host, in the side panel, set the controller property to the value that you assigned for that Activity.

When you set the value of a controller property in the Activity Browser, you change the runtime value of this property. When you restart the Preview or your application, the Activity Host reads the value of the controller property that you set in the Properties or with a Trigger and Action.

Learn how to use a controller property to control Activities by completing a tutorial. See Tutorial: Structure application UI.
- To simulate the activation of Activities in a Data-Driven Exclusive Activity Host, in the side panel, set the value of the Active Activity Index property to the index of the item in a list data object that you want to create.

When you set the value of the Active Activity Index property in the Activity Browser, you change the runtime value of this property. When you restart the Preview or your application, the Data-Driven Exclusive Activity Host reads the value of the Active Activity Index property that you set in the Properties or with a Trigger and Action.

Learn how to use Data-Driven Exclusive Activity Host by completing a tutorial. See Tutorial: Generate UI from a data source.

## Simulating the application of Data Triggers

When you use Data Triggers, you can simulate the application of Data Triggers and show connections between a Data Trigger and Activities that the Data Trigger activates.

The Activity Browser indicates that an Activity or Activity Host has a Data Trigger, with the  icon.

To work with Data Triggers, select an Activity or Activity Host that has a Data Trigger, and in the side panel use these tools:
|

Tool |

Description |
|   |

Shows where a Data Trigger is and where the source and target Activitites of that Data Trigger are. |
|   |

Simulates the state when you apply a Data Trigger.

This enables you to see the state of your application when the conditions for a Data Trigger are met without having to change the property values in your application.  |
|   |

Shows the selected Data Trigger in the Node Components window. |

Learn how to use Data Triggers by completing a tutorial. See Tutorial: Control application UI.
## Changing the order of nodes

To change the order of Activities or Activity Hosts in the Activity Browser, enable the automatic layout tool  and drag the item to the desired position. When changing the order is available, the Activity Browser shows a placeholder in place of the new position.

Keep in mind that you can only change the order of the nodes of the same type.
## Changing the parent of nodes

To change the parent of an Activity or Activity Host in the Activity Browser, enable the automatic layout tool  and drag the item to a new parent.

Keep in mind that an Activity cannot be a parent of another Activity.
## Viewing Activities and Activity Hosts

The Activity Browser has these tools to organize and show the content:
|

Tool |

Description |
|

 |

Lays out items automatically on the Activity Browser canvas and enables changing the parent and order of nodes.

When you toggle off the automatic layout, you can organize Activities and Activity Hosts by dragging them on the Activity Browser canvas.   |
|

 |

Fits the Activity tree to the size of the Activity Browser window.   |
