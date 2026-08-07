---
title: Importing animations
source: https://docs.kanzi.com/4.1.0/en/working-with/animations/importing-animations.html
---

# Importing animations


In many third-party tools, animations contain information about the target of animations. When you import animations to Kanzi Studio, Kanzi organizes objects and animations in the following way:

- The visual content is placed inside a scene that contains the objects.
- Kanzi Studio creates a timeline sequence, adds for the scene an Animation Player, and sets the Target Animation Timeline property of the Animation Player to the timeline sequence.
- For each animated object, Kanzi Studio creates a timeline entry and sets the animation target for that timeline entry for that target.
- Kanzi Studio places all animation data under the corresponding timeline entries.


Keep this in mind before you move objects from the imported scene to another scene, or when you want to use the animations in event-driven and background animations.
