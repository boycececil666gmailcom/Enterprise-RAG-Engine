---
title: Editing animation clips
source: https://docs.kanzi.com/4.1.0/en/working-with/animations/editing-animation-clips.html
---

# Editing animation clips

Use an Animation Clip to combine Animation Data resources into more complex animations. You can reuse the same Animation Data resources in different Animation Clip items. Use an Animation Child Clip to create hierarchical animations.

To edit an animation clip or animation data items, in the Library > Animations > Animation Clips double-click the animation clip or animation data item you want to edit. Animation Clip Editor opens. [](../../_images/animation-clip-editor.svg)
## Animation clip editor toolbar

Tool |

Description |

Shortcut key |

Pan the animation canvas by clicking and dragging the canvas.

You can zoom using the mouse wheel or by pressing the middle mouse button. To zoom either x or y axis, click and drag the right mouse button.  |

S

Right mouse button  |

Select and move the animation channels and keyframes.

You can select multiple timeline entries. Selected items are grey shown in the Properties.  |

V |

Scale more than one selected keyframe:

- Left mouse button scales the selected keyframes along x and y axes.
- Right mouse button scales the selected keyframes along the x axis.
- Middle mouse button scales the selected keyframes along the y axis.

X |

Add keyframes after selecting at least one animation channel. |

I |

Toggle snap for animation canvas.

When you enable snapping, the cursor moves only to the points on the grid that you can configure in Edit > User Preferences > Animation Editing tab. Snapping grid is different from the grid in the animation canvas.

To set the snap mode, in the User Preferences set Snap mode to:

- Custom allows you to set x and y axis snap distances for keyframes and handles
- Snap to grid snaps to the Animation Editor grid based on the zoom level

To set whether you want to snap keyframe Bezier handles to a keyframe or the Animation Editor grid, in the Animation Editing tab, use the Snap relative to keyframe setting and set the relative horizontal and vertical snap distances.
**Tip:** To enable snapping temporarily while you drag a keyframe or a keyframe Bezier handle, hold down the Shift and Alt keys.   |   |
Scale the animation canvas so that all keyframes are visible. |   |
Set the animation clip start and end times to the first and last keyframes in the animation clip editor. |   |
## Copying and pasting animation items

When copying an item, the default paste performs a deep copy: all the items under the copied item are duplicated.

Items in Animations can have the same children under many parents. To copy these items you can use:

- Paste as Instance. Use Paste as Instance when you want to create just a link to the item you want to copy. For example, if you have an animation clip with Jumpy animation, when you copy the Jumpy animation to another animation clip, Paste as Instance creates just the link to Jumpy animation.

To paste an item as instance, right-click the item and select Paste as Instance.
- Paste Item and Instance Children. Use Paste Item and Instance Children when you want to create a new copy of the root item and only links to its children. For example, if you have a Hippie animation clip with animation, when you copy the Hippie animation clip, Paste Item and Instance Children creates a new animation clip and only links to the animation. When you change Hippie animation clip, the changes do not affect the new animation clip, because Hippie animation clip and the new animation clip are two different items. However, if you change the animation under Hippie animation clip, the changes affect the animation under the new animation clip, because they are instances of the same item.

To paste an item and create instances for its children, right-click the item and select Paste Item and Instance Children.

## Removing animation items from their parents

When you want to remove an item from one parent (for example, Animation Data from an Animation Clip), but want to keep it under the other parents, right-click the item you want to remove and select Remove from Parent.

Kanzi Studio removes the reference, but preserves the item in question in its library.
