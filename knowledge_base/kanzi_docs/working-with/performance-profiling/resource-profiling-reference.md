---
title: Resource profiling reference
source: https://docs.kanzi.com/4.1.0/en/working-with/performance-profiling/resource-profiling-reference.html
---

# Resource profiling reference


Here you can find the reference for resource profiling data.

Use resource profiling to measure during runtime how long it takes to load and deploy resources and prefabs in your Kanzi application.

To learn more about resource profiling, see Measuring the loading and deployment time of resources.

Kanzi resource profiling data contains:

- Resource profiling contexts for the Kanzi resource manager main thread (`"Resource manager main thread"`) and loading threads (`"Resource manager loader thread N"`). See Resource profiling contexts.
- Resource profiling data samples (`"ResourceProfilingDataSamples"`). See Resource profiling data samples.

## Resource profiling contexts


A resource profiling context represents a scope that executes code path which triggers resource loading or deployment. A resource profiling context sampler creates a resource profiling context when the execution of the scope where the sampler is defined, triggers resource loading or deployment. The duration of a resource profiling context is the same as the duration of the resource loading or deployment triggered by the execution of the corresponding scope.

In scopes where resources are loaded and deployed Kanzi creates samplers for the profiling contexts of resource loading and deployment `ResourceProfilingLoadContext` and `ResourceProfilingDeployContext`.

This table lists the common attributes of resource profiling contexts. All contexts have these attributes.
|

Common attribute |

Description |
|

`ContextID` |

Unique identifier of the resource profiling context.

Use the identifier to find out in which thread the context was created, the parent context, and the thread which triggered the execution of the context.  |
|

`ContextName` |

Name of the resource profiling context. |
|

`DependenciesDuration` |

Time in nanoseconds it took the Kanzi main thread to load and deploy resources on which a resource depends. |
|

`Duration` |

Time in nanoseconds it took the Kanzi main thread to load and deploy a resource and the resources on which this resource depends. |
|

`TimeStamp` |

Time point of entering the scope of the resource profiling context.

Use the timestamp to find out when different resource profiling contexts were created relative to each other.  |
|

`DependencyContexts` |

List of dependency contexts. |

This table lists the profiling context types and the attributes that they have in addition to the common attributes.
|

Resource profiling contexts and context names |

Description |

Additional attributes |
|

Main loop

`MainLoop`  |

The profiler creates this context when the application loads or deploys a resource during the Kanzi main loop iteration. |

`MainLoopCounter` - The iteration during which the context is created. |
|

Resource acquirement `ResourceAcquire` |

The profiler creates this context when resource acquisition triggers the loading or deployment of the resource. |

- `AcquireAsynchronously`:

  - If resource loading is asynchronous, `"true"`
  - If resource loading is synchronous, `"false"`

- `ResourceUrl` - The kzb URL of the resource which the application is acquiring.
  |
|

Resource loading

`ResourceLoading`  |

The profiler creates this context when the application loads the resource. |

- `LoadedResourceID` - The unique identifier of the loaded resource. Use this attribute to distinguish between different occasions of loading a resource again after it was purged.
- `LoadedResourceType` - The type of the loaded resource.

For example, `Kanzi.Material`, `Kanzi.PrefabTemplate`, `Kanzi.ResourceDictionary`, or `Kanzi.ShaderProgram`.
- `LoadedResourceUrl` - The URL of the loaded resource.
- `ResourceLoadingDuration` - The time in nanoseconds it took a loading thread to load the resource.
  |
|

Resource deployment

`ResourceDeployment`  |

The profiler creates this context when the application deploys the resource. |

- `DeployedResourceID` - The unique identifier of the deployed resource.
- `DeployedResourceType` - The type of the deployed resource.
- `DeployedResourceUrl` - The URL of the deployed resource.
- `ResourceLoadingDuration` - The time in nanoseconds it took the Kanzi main thread to deploy the resource.
  |
|

Acquirement of an anonymous resource

`AcquireAnonymousResource`  |

The profiler creates this context when the application acquires a resource that does not have a resource ID. This usually happens when acquiring a resource dictionary. |

N/A |
|

Asynchronous acquirement of resources

`AcquireResourcesAsynchronously`  |

The profiler creates this context when the application acquires multiple resources asynchronously.

See Loading node prefab resources asynchronously.  |

N/A |
|

FinishingQueue: process task

`FinishingQueue::processTask`  |

The profiler creates this context when Kanzi processes a task which loads or deploys a resource. This context is usually the parent of one or more Resource loading or Resource deployment contexts. |

`Description` - Information about the index of the resource loading task and task queue size.

For example, `"Task index 1, queue size 2"`.  |
|

Prefab template instantiation

`PrefabTemplateInstantiate`  |

The profiler creates this context when the instantiation of a prefab template triggers resource loading or deployment. |

`Description` - The root node of the prefab instance.

For example, `"Node root: Screen"`.  |
|

Prefab template node instantiation

`PrefabTemplateNodeInstantiate`  |

The profiler creates this context when the instantiation of a node in a prefab template triggers resource loading or deployment. |

`Description` - The name of the node in the prefab instance.

For example, `"Node name: Viewport 2D"`.  |
|

Node attachment

`Node::attach`  |

The profiler creates this context when the attaching of a node to the node tree triggers resource loading or deployment. |

`Description` - The name of the node that is attached.

For example, `"Node name: Plane"`.  |
|

Message trigger

`MessageTrigger`  |

The profiling system creates this context when the handling of a message trigger results in resource loading or deployment. |

`Description` - The source of the trigger message.

For example, `"Message source: Button 2D"`.  |
|

Application process deployment queue  `Application::progress` `DeploymentQueue`   |

The profiler creates this context when the execution of the `Application::` `progressDeploymentQueue` function triggers resource loading or deployment. This context is always a child of the Main loop context. |

N/A |
|

Application process deployment queue override (default)  `Application::progressDeployment` `QueueOverride(default)`   |

The profiler creates this context when the execution of the Kanzi implementation of the `Application::progress` `DeploymentQueueOverride` function triggers resource loading or deployment. |

N/A |
|

Waiting loading queue task completion  `WaitingLoadingQueue` `TaskCompletion`   |

The profiler creates this context when the resource that the application is acquiring is being loaded by one of the loading threads and the main thread has to wait for that loading thread to finish loading. |

N/A |
## Resource profiling data samples


A resource profiling data sample includes a summary of profiling information related to a profiled resource, including references to the resource profiling contexts in which the resource is acquired, loaded, and deployed.

You can find a list of all the resource profiling data samples in the `"ResourceProfilingDataSamples"` section of a resource profiling data file. See Logging resource profiling data.

Use the `ContextID` attribute of a resource profiling context to find out in which thread the resource profiler creates a resource profiling context, what is the parent context, and the thread which triggered the execution of the context. See Resource profiling contexts.

This table lists the attributes of a resource profiling data sample.
|

Attribute |

Description |
|

`DeploymentDuration` |

Time in nanoseconds it took to deploy the resource |
|

`LoadingDuration` |

Time in nanoseconds it took to load the resource |
|

`ResourceID` |

Unique identifier of the resource profiling data sample |
|

`ResourceType` |

Type of the profiled resource |
|

`ResourceUrl` |

URL of the profiled resource |
|

`Success` |

Whether Kanzi successfully loaded the resource |
|

`AcquireContext` |

Resource profiling context in which the application or Kanzi acquired the resource |
|

`LoadingContext` |

Resource profiling context in which Kanzi loaded the resource |
|

`DeploymentContext` |

Resource profiling context in which Kanzi deployed the resource |

This is the resource profiling data sample of the City mesh in the Scroll view example.

```
"DeploymentDuration": "43838400",
"LoadingDuration": "1473400",
"ResourceID": "217505936",
"ResourceType": "Kanzi.Mesh",
"ResourceUrl": "kzb://scroll_view/Mesh Data/City",
"Success": "true",
"AcquireContext": {
    "AcquireAsynchronously": "true",
    "ContextID": "216087856",
    "ContextName": "ResourceAcquire",
    "DependenciesDuration": "0",
    "Duration": "9000",
    "ResourceUrl": "kzb://scroll_view/Mesh Data/City",
    "TimeStamp": "3750800"
},
"LoadingContext": {
    "ContextID": "241268536",
    "ContextName": "ResourceLoading",
    "DependenciesDuration": "0",
    "Duration": "1475600",
    "LoadedResourceID": "217505936",
    "LoadedResourceType": "Kanzi.Mesh",
    "LoadedResourceUrl": "kzb://scroll_view/Mesh Data/City",
    "ResourceLoadingDuration": "1473400",
    "TimeStamp": "3764700"
},
"DeploymentContext": {
    "ContextID": "241265456",
    "ContextName": "ResourceDeployment",
    "DependenciesDuration": "43118600",
    "DeployedResourceID": "217505936",
    "DeployedResourceType": "Kanzi.Mesh",
    "DeployedResourceUrl": "kzb://scroll_view/Mesh Data/City",
    "DeploymentDuration": "719800",
    "Duration": "43839600",
    "TimeStamp": "59705500",
    "DependencyContexts": [
        { ... }
}

```
