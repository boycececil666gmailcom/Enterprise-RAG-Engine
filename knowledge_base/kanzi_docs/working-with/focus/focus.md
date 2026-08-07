---
title: Focus
source: https://docs.kanzi.com/4.1.0/en/working-with/focus/focus.html
---

# Focus

Key focus forwards hardware key messages to the correct user interface element in your application. For example, the user can press the arrow keys on the keyboard to move a slider or press the Enter key to click a button.

Kanzi organizes nodes in focus scopes. Focus scopes are nodes which assist in focus chain navigation handling. They group the child nodes and drive the focus navigation within that group. They also act like a focus proxy, forwarding the focus to one of their focusable child nodes. When you move the focus away from a focus scope, that scope remembers the last-focused child node.

These are the main concepts behind how focus works in Kanzi:

- **Focusable node** is a node that has the Focusable property enabled. A focusable node can receive key input.
- **Key focus node** is the node that currently receives key input, and has the read-only Focused property enabled. A Kanzi application can have only one key focus node at a time.
- **Focus chain** is a sequence of nodes which defines the order in which Kanzi sets key focus to those nodes. Kanzi includes in the focus chain all focusable nodes in your project. [](../../_images/focus-chain.svg)
- **Focus order** defines the position of a node in the focus chain based on the position of the node in the node tree or the value of its Focus Order property. [](../../_images/focus-order.svg)
- **Focus scope** is a node that helps navigation handling in a focus chain. You can set a node to be a focus scope to forward the focus from that node to a child node. [](../../_images/focus-scope.svg)

These are the focus scope types in Kanzi:

  - **Focus group** is a focus scope which forms a group of focusable nodes. When a focus group node receives focus, Kanzi forwards the focus to the focus node of that focus scope.

You can move focus within the boundaries of a focus group and outside of a focus group.
  - **Focus fence** is a focus scope that keeps the focus chain navigation inside the scope and does not allow the focus chain navigation to enter or leave that scope. A focus fence allows the user to navigate the content within the scope boundaries.
  - These overlay-type focus scopes:

    - **Modal overlay** blocks the key and touch input that originates from outside its boundaries and keeps the focus navigation within the overlay boundaries, just like a focus fence. Every Kanzi application has at least one modal overlay: the Screen node.
    - **Auto-closing modal overlay** is similar to modal overlay, except that when the overlay is an Activity in a Parallel Activity Host, the Parallel Activity Host deactivates that Activity when user input originates from outside the boundaries of that Activity.
    - **Modeless overlay** propagates the key and touch input that originates from outside its boundaries, but keeps the focus navigation within the focus scope boundaries, just like a modal overlay.
    - **Auto-closing modeless overlay** is similar to modeless overlay, except that when the overlay is an Activity in a Parallel Activity Host, the Parallel Activity Host deactivates that Activity when user input originates from outside the boundaries of that Activity.

- **Focus state** reports the focus state of a node or nodes in a focus scope. These are the available values for the Focus State property:
|

Enumeration value |

Enumeration key |

Meaning for a focusable node |

Meaning for a focus scope |
|

No Focus |

0 |

The node does not have focus. |

None of the nodes in the focus scope have focus. |
|

Logical Focus |

1 |

The node is the logical focus node of an overlay-type focus scope. The logical focus node was the key focus node before the overlay lost the focus. When the overlay regains the focus, the logical focus node becomes the key focus node. |

A node in the focus scope is the logical focus node of the overlay to which the scope belongs. |
|

Key Focus |

2 |

The node is the key focus node of the application. |

A node in the focus scope is the key focus node of the application. |

To learn more about creating focus navigation for your application, see Using focus.
