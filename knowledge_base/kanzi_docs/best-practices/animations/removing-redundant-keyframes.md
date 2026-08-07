---
title: Removing redundant keyframes
source: https://docs.kanzi.com/4.1.0/en/best-practices/animations/removing-redundant-keyframes.html
---

# Removing redundant keyframes


Sometimes animations contain more keyframes than necessary. Kanzi provides an easy way to optimize animation data, which results in a significantly smaller number of keyframes, often without losing the animation precision at all. For example, in the animation shown here there are too many keyframes than is needed for most purposes.

To remove the redundant keyframes:

1.

In the Library > Animations > Animation Clips select your animation clip.
2.

Right-click the animation you want to optimize and select Optimize Animations.
3.

In the Threshold value dialog box enter the threshold value for the keyframe removal and click OK.

Value 0.1 is a good starting point. This removes all keyframes with a delta value smaller than 0.1. Try different values for your animation, because using another value can optimize your animation even more.

If you want to make sure no information is lost, use 0.

This image shows the example animation after removing all keyframes with a delta value smaller than 0.1.
