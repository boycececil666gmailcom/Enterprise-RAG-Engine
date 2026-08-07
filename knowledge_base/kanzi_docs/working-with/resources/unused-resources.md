---
title: Setting how Kanzi Engine handles unused resources
source: https://docs.kanzi.com/4.1.0/en/working-with/resources/unused-resources.html
---

# Setting how Kanzi Engine handles unused resources

When a resource is not used, Kanzi Engine keeps it in the memory until you call `ResourceManager::purge`. You can set how Kanzi Engine handles unused resources when you call `ResourceManager::purge` for each resource separately, or for the resources in the entire project.

You can also set Kanzi Engine to immediately remove from memory resources that are not in use by setting `ResourceManager::setDefaultMemoryStrategy` to `interop::MemoryStrategy::OptimizeMemory`.
## Setting how Kanzi Engine handles unused resources in the entire project

To set for the entire project how Kanzi Engine handles unused resources when you call `ResourceManager::purge`, in the main menu select Project > Properties, and in the Properties set:

- The Resource Keep Alive Behavior property sets how Kanzi Engine handles all unused resources.

  - Allow unload if unused to remove resources when they are not in use anymore.
  - Keep alive to keep the resources in memory even when they are not in use anymore.

- The Material Type Keep Alive Behavior property sets how Kanzi Engine handles unused material types.

  - Allow unload if unused to automatically remove resources when they are not in use anymore.
  - Keep alive to keep the resources in memory even when they are not in use anymore.
  - Project setting to use the value set in the Resource Keep Alive Behavior property.

This setting applies to all resources for which you do not separately set the Keep Alive Behavior property.
## Setting how Kanzi Engine handles individual unused resources

To set how Kanzi Engine handles individual unused resources when you call `ResourceManager::purge`, in the Library select a resource, and in the Properties add and set the Keep Alive Behavior property:

- Allow unload if unused to remove the resource when it is not in use anymore.
- Keep alive to keep the resource in memory even when it is not in use anymore.
- Project setting to use the value set in the Project > Properties. See Setting how Kanzi Engine handles unused resources in the entire project.

To set how Kanzi Engine handles unused resources using the API, use `Resource::isKeepAlive` and `Resource::setKeepAlive`.
