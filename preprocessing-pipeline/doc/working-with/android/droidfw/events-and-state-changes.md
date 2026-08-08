---
title: Observing state changes and handling events in Kanzi Android framework (droidfw)
source: https://docs.kanzi.com/4.1.0/en/working-with/android/droidfw/events-and-state-changes.html
---

# Observing state changes and handling events in Kanzi Android framework (droidfw)

## Observing state changes

You can implement `KanziViewListener` to listen for state changes in `KanziView`. Use this to inject custom initialization and un-initialization logic.

For example:

- Use the `KanziViewListener.onAttachedToWindow` callback to access domain, register Kanzi Engine Java plugins or manually setup the viewâs node tree.
