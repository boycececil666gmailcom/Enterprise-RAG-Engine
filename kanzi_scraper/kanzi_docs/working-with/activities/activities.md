---
title: Activities
source: https://docs.kanzi.com/4.1.0/en/working-with/activities/activities.html
---

# Activities


An Activity is a part of an application UI that is responsible for a task. For example, a media player application can have Activities, such as radio, music player, and AUX.

However, an Activity can also be a smaller task, such as an Activity for the popup volume indicator that appears only when the user changes the volume in a media player. An Activity can be visual, but does not have to be. For example, an Activity that is visual can instantiate a prefab to show a popup window, while an Activity that is not visual can be music playback which plays music in the background regardless of other Activities.

An Activity Host defines the rules for when its Activities are active. Kanzi has these Activity Hosts:

- Exclusive Activity Host and Data-Driven Exclusive Activity Host can have only one of its child Activities active at a time. When one child Activity of a Data-Driven Exclusive Activity Host or an Exclusive Activity Host is active, all other Activities of that Activity Host are inactive.

For example, you can use a Data-Driven Exclusive Activity Host or an Exclusive Activity Host to toggle between views in your application. See Exclusive Activity Host and Data-Driven Exclusive Activity Host.

Exclusive Activity Host

Data-Driven Exclusive Activity Host
- Parallel Activity Host can activate more than one of its child Activities at a time. When you activate an Activity, a Parallel Activity Host brings that Activity to the front. In a Parallel Activity Host you can group Activities, to show the groups in the same order that you defined in the Activity tree. When you activate an Activity in a group, a Parallel Activity Host brings to the front the Activity in that group.

For example, this way you can implement the showing of critical messages, such as engine failure, in front of regular notifications, such as a phone call notification. In both groups a Parallel Activity Host shows the Activities in order of activation. See Parallel Activity Host.


You can add Activities to an Activity Host in real-time. This enables you to use the Kanzi Engine API to generate Activities or to add to the application another application for which the structure of Activities is not known until you run the application. For example, you can use the Kanzi Engine API to generate a large number of menu pages that you want to show to the user.
## Application UI structure and navigation


The Activity, Data-Driven Exclusive Activity Host, Exclusive Activity Host, and Parallel Activity Host together enable you to create a UI that the user can navigate in your application. You implement the navigation as a reaction to user interaction or changes to data coming to the application, by activating and deactivating Activities to switch application views and to show different application layers, such as popup windows. That way you can control which parts of your application UI the user can see and interact with.

Use Activities, Data-Driven Exclusive Activity Hosts, Exclusive Activity Hosts, and Parallel Activity Hosts to form the navigation graph. Activities define the content elements and Activity Hosts define the navigation pattern in your application UI. In each Activity Host, use Activities to create UI content within applications that an Activity Host represents. For example, with Activity Host and Activities you can organize your UI to show different views in your application, such as media player, contacts, and phone view, and to show content in popup windows.

Use the Activity Hosts to activate and deactivate Activities:

- When an Activity is active, the Activity prefab is attached to the node tree, is visible, and the user can interact with its content.
- When an Activity is inactive, the Activity prefab is not attached to the node tree, is not visible, and the user cannot interact with its content.


The Activity and Activity Host nodes inherit from the `ContentLayout2D` and `ContentLayout3D` classes to lay out their content like a Content Layout node. See Using the Content Layout nodes.
## Status management of Activities


Each Activity has the Activity Status property that indicates the state of that Activity. When an Activity becomes active or inactive, the Activity Status property changes and in your application you can react to these changes. When you activate an Activity, its Activity Host instantiates the Activity prefab. When you deactivate an Activity, its Activity Host removes the Activity prefab from the node tree.

The Activity Status property defines these states:
|

Activity Status |

Description |
|

Active |

The Activity is active and shows its content. |
|

Deactivating |

The Activity is transitioning to the Inactive state.

This state is used to synchronize transition animations in a Data-Driven Exclusive Activity Host and Exclusive Activity Host.  |
|

Inactive |

The Activity is inactive and does not show its content. |
|

Activating |

The Activity is transitioning to the Active state.

This state is used to synchronize transition animations in a Data-Driven Exclusive Activity Host and Exclusive Activity Host.  |

In Data-Driven Exclusive Activity Host and Exclusive Activity Host nodes:

- Only one child Activity can be active at a time.
- While one Activity is in the Deactivating state, another Activity can at the same time be in the Activating state.


In a Parallel Activity Host node, more than one Activity can be in the Active state at the same time, therefore any Activity can be in any state.

To set which Activity is active when its Activity Host becomes active:

- In an Exclusive Activity Host or Parallel Activity Host, set the InitiallyActive property of an Activity. See Setting the initially active Activity and Setting the initially active Activities.
- In a Data-Driven Exclusive Activity Host, use the Active Activity Index property. The value of the Active Activity Index property points to the item in the list data object that a Data-Driven Exclusive Activity Host uses to create an Activity.

### Activity transitions


These transitions define an Activity transition:

- Active -> Deactivating
- Deactivating -> Inactive
- Inactive -> Activating
- Activating -> Active


During a status change, Activities use these transitions, including the transitions with the intermediate Activating and Deactivating states. Transitions skipping these intermediate states, such as Active -> Inactive (without the Deactivating state) or Inactive -> Active (without the Activating state), do not take place, even when you create them.

In an Activity tree, when you deactivate an Activity with child Activities, the Activity Host deactivates child Activities immediately without applying the transitions Active -> Deactivating and Deactivating -> Inactive. Whereas, when you activate an Activity with child Activities, the Activity Host activates the child Activities by applying the transitions Inactive -> Activating and Activating -> Active.

To learn how to create transitions between Activities, see Creating transitions between Activities.

In Data-Driven Exclusive Activity Host and Exclusive Activity Host nodes, transitions between Activities proceed as follows:

1.

Activity 1: Status is Active.

Activity 2: The Activity is not loaded.
2.

Activity 1: State Manager plays the Active -> Deactivating transition animation, if any. The Activity Host sends the `ActivityConcept::ActivityDeactivatingMessage` and `ActivityConcept::StatusChangedMessage` messages.

Activity 2: The Activity Host loads the resources of the Activity.
3.

Activity 1: Status is Deactivating.

Activity 2: Status is Inactive.
4.

Activity 1: State Manager plays the Deactivating -> Inactive transition animation, if any. The Activity Host sends the `ActivityConcept::ActivityDeactivatedMessage` and `ActivityConcept::StatusChangedMessage` messages.

Activity 2: State Manager plays the Inactive -> Activating transition animation, if any. The Activity Host sends the `ActivityConcept::ActivityActivatingMessage` and `ActivityConcept::StatusChangedMessage` messages.
5.

Activity 1: Status is Inactive.

Activity 2: Status is Activating.
6.

Activity 1: The Activity Host unloads the resources of Activity.

Activity 2: State Manager plays the Activating -> Active transition animation, if any. The Activity Host sends the `ActivityConcept::ActivityActivatingMessage` and `ActivityConcept::StatusChangedMessage` messages.
7.

Activity 1: The activity is unloaded.

Activity 2: Status is Active.

## Data and logic programming of Activities


For each Activity, you can define properties that are specific to that Activity. These properties are called Activity properties. For example, an Activity for a music player can switch music on and off, or change the volume level.

When you manually create a property for an Activity node, set the namespace of that property to ActivityProperty. You can create properties with int, bool, float, and enum data types. If you use Code Behind for an Activity, Kanzi adds the properties of that Activity to Code Behind.

The values of Activity properties implement the state machine and logic of your Kanzi application, which is why Kanzi preserves the values of these properties even when an Activity is deactivated. When Kanzi deactivates an Activity, it serializes the Activity properties of that Activity and when Kanzi activates that Activity, it deserializes the state of that Activity and restores its Activity property values.

For more information on programming logic of Activities, see Programming Activities with Code Behind.
## Virtualization


The main goal of Activity virtualization is to manage memory consumption in your application efficiently. Since the navigation graph of the entire application can be large, keeping the UI and assets loaded in memory at all times is rarely feasible.

When you activate an Activity, its Activity Host dynamically loads the prefab and asynchronously loads the required resources. On deactivation, the Activity Host detaches the Activity from the node tree and deletes the Activity instance.

By default, acquired resources remain in memory. To change this behavior, you can enable the OptimizeMemory property in the Activity Browser. When enabled, Kanzi automatically unloads preloaded resources for those Activities.

You can also call `ResourceManager::purge` to release the resources of deactivated Activities.
### Controlling virtualization


By default, when you deactivate an Activity, Kanzi serializes the values of Activity properties for that Activity and its child Activities. Besides the values of Activity properties that you add, this includes information about the focus and activation state of Activities. Keep in mind that Kanzi does not serialize the runtime state of other, non-Activity properties.

When you activate a deactivated Activity, Kanzi restores the values of Activity properties for that Activity and its child Activities. When you disable virtualization, Kanzi does not preserve the values of Activity properties.

You can also reset the serialized state of an Activity, before activating or after deactivating that Activity. By default, Kanzi restores the serialized state.

See Controlling virtualization in an Exclusive Activity Host and Controlling virtualization in a Parallel Activity Host.
### Activity persistence


By default, when you deactivate an Activity, Kanzi detaches the Activity from the node tree and deletes the Activity instance. You can set Kanzi to preserve the Activity instance when the Activity is deactivated. When you activate such an Activity again, Kanzi restores the Activity node in the same state as it was before deactivation, even if you disable virtualization for this Activity. This way you can skip Activity instantiation when you activate the Activity again.

See Controlling Activity persistence in an Exclusive Activity Host, Controlling Activity persistence in a Parallel Activity Host, and Controlling Activity persistence in a Data-Driven Exclusive Activity Host.
